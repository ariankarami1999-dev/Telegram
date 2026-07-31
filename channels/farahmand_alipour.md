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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 01:04:36</div>
<hr>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjOPiJkM5-EEDM6Bj7OV6FYwa6uuVXOBiL-mXDklkcvICj9qBgt2UZtADLR8kiyyeOHfyQcn0FfLZdo9ahC6WTCE0Gy3eF6J_AGRCc6jpnP73GoufsqCZZNizMdGkZTUO49khBUxM4Y6TBU2vIOrdghJElvyZEl5IEKOaMh7yuWN69SA0jg0l0idBUPSC9aBI8wPpcNuXekSRjEz7Jvd8TkQdToAqfOjoCcsa8Qgze6YuKR176p9Qk2dAQHVGpE4zzljhITcIpBkHsGB0OiIhUdx0VZqTRhxzBzphO0T1rgW6byolugK1p47bRTt68SFGrPMKK28I-AJjm0aM8p2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjIQTM80iQK69zWeK1zv2hRR6NfL3wncov7BnLo3ze6n_keZzpyBK1vl5c4KapxAjE3O0y6vVlg8WgIA2uFu9ji5D8zywqX9ho0Kqvr_2fcYIHssdNypK6zYLRgiyV7lmBr5XMuduQIcUo85FnSXHKTF21c5j51idawfac2Bw0DCD44sZJZghFvZwzJqcrlEZlB_LW6QE5nHkDmtkH6fA2YqMQG5HTtD6v8ISDpmyT9QyyxsXk4wN47Lc-AqMHkeTwWzW9uARkCB7smN3iFsM1nEqy4MCf1aMQk7sSZ1R7i_DyDjHRlIHDFXBPsmRuiUmnO9GAaYzkOS1EObA5m8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5SNeWkjycX6gsJJwtvo20Mpl26SZZjX19Gi5my1d3P89yGGHjNGX5Nb7B9HX3xHy1hSjl1LHA2YguAot4MmdK9Iqc2jXoJdEQJuGH_hl_a6SzgMO_5Q2_Q4ueCYlF9SWiYxniCXq7mimIN5jvMhQL8V-LgiZPrRMmFrwC7D8xQOkAVJ_jbDkFDgbJGLV3-I9-I58jLC6-5e9E65UTRvfMOvsufXjtX96ST-BYDKr1xk33PWoaF0-KoIJbmhf3vHtfYb8KpmjX4H60z4_JGadulFYnxuXRxALiwZYDfx2YkROe3M9MjCs44ByzEDodPV_Qn10wxXaVt0y3ID6TVyfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0dbeuUShWM30A_kcihgPofaUCtPNvenAZqq6Y6HkEQ0PEo-xt4qg281D3PmxKVo0S6c3h5XGhG8roFn54Osm0dfLCMx1fNM_hRpo24dJrmZdIImiAVEEGl2n1Asn5OaWQtL_Rx9fHVJ62o0Ml6hs2t0NcQ9RKKXIvTPQb0bWDzKZrxFtDLuS32HRey8R35BESCXF8ZoIJfE22sRsn0N0te6LMPVJ3KwEZUFjyPtTkcI0P0XQiZwGOt24oXXc8qmz5oRQy2tH3uLEON-I7dvVbMOtYa3HajQA_2JT-widb9tMdfT_g11s9psXz7OkHnf30w6WOZur8mdeCB97sDhYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0zeHLwcL_94UpOnVwHJeR-SjOVAwRNEQoorPnaFWQ1ohNkbzQK4p3iiQl9uEkdgpLe2LnBgv3grpS7bFiErOV3cDg5J7skPJ1Ki4uwUSIpNXd-N78Xy5XMWlb_a8QerRDqBcjhthQRFwffUFxCic89OYyk1zoGFsIXSMCqWdSsN0Z3LWgw5PWsPkrPTiFta-EksSqP8n5_uEJdZHT4kK57drrgogCbn0DMDAxQDxKE7wC3cItTpLv_N1J_jjecwzBtAtuuv3oxcuQ9rcVjp2y0oUeZUXqr88NGUkO_6atSFzTMtaiZB_ti_i1XeA0NO4YNHIzjrFR4kBNQDHyh7Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5P76CyG4bVOYZoppovkF2x3KEB2a0Bm8ajKs3D4u0xTvsXMf4OYFfV8M49NvXT8IRKwANSh1ScxXHMGskLkujk2SYWBPtDpjAl46UvK4S6OGqAkva3ZEpS3CXjeC-0eeRqDuptKGmQMtplBiRMhwiQsMFKcUs2x2HNZDlMo9_W_qMjhKWuJuhLkms754rUBXzBsSDUNadQsSWxxtfC8x9dERl6p_eYSw6Z-mLIfXVrJkUEMp6j2RQzJjf28ojuskHK9vYH9r_WP4hQByAe_OxxpXnf1Se9jyYLQpR4bRv3un-h9NdgIAi28xGbzwzlkITL6IGlMWozSljuzOyEVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLWvRidvF2WGX36rJFyIkgIwMU8tz8LI1R-TjkWtDoaERDn2JcMfma3Q7dP8EIs_jRegQ0dIh3TLudy0PfUgwTUDcJTqdMdrkrk4ng3c08s-aKyfzgOlabmkZYEKrPfJ0fLz7uqIOaX4kiYylFMCzCMZlmED0hTfpoNNlnW0_w5KhXtk6CtgXIE7Yux4q3PNQACmqO-SmVqFStMtIXYbudWQSHcBuwg9KKTG9NgTNq1Ntf5wVpT8lX2mWEEnwUtyE9ul4XcU3Ab1ufnofnPVjn7IPANWiqY8r0C3IbmKPBLZ5FGqWr8-KnmX0-Pv5ufuK_OOhabkqLEbXY50RDJlAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=epwSbDFccUQ7k0o5tbn8RVo6rNJUHV5KrpNQfy6PqGMnjPhLqBGAHst5B1CVf4A4EKaefDz1-TnVcvyazkzZP_rcTlsJLudy61CIoKrEx7BGt3QL9HliAkuLG9fZZ5niJXG0TtMsAA74MKHv46_8okFsy1D3v8gxfL82x_8akuWzHRjRp5zdNul8sVlgDv5ZtVjOdIN8CPYm0px4wKoDRUrH-R3e-DwE8sINQb8BF8DuwSRYPlMtL3g2LxDQ4CVQcPeh3pywkJS9fevYclGnsHmUwLaNZQHibmYDzZpNVvctzocsNCt4OpAadWcmRBHp3Nt5DAyofyCPR2t-GDfdAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=epwSbDFccUQ7k0o5tbn8RVo6rNJUHV5KrpNQfy6PqGMnjPhLqBGAHst5B1CVf4A4EKaefDz1-TnVcvyazkzZP_rcTlsJLudy61CIoKrEx7BGt3QL9HliAkuLG9fZZ5niJXG0TtMsAA74MKHv46_8okFsy1D3v8gxfL82x_8akuWzHRjRp5zdNul8sVlgDv5ZtVjOdIN8CPYm0px4wKoDRUrH-R3e-DwE8sINQb8BF8DuwSRYPlMtL3g2LxDQ4CVQcPeh3pywkJS9fevYclGnsHmUwLaNZQHibmYDzZpNVvctzocsNCt4OpAadWcmRBHp3Nt5DAyofyCPR2t-GDfdAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEXtfY8-FEUVtVRd5xFjB7FTDSe3H-iwxnqqV4pDaLdkv0y7wbH0AXhiWInvM1lBBqrvzxqKv2iNdnxi0KUn1Ar_hxL1JYTFcgkKNVTDAzSFwNpn4JAq4ySOeEHQ0G2P827Nz3JrOA_hK1_ex3B-i-CB-8rjALMoiXsNCrr55NwigTZEG4TpaGuYWY8FxGPhSh33Rvg49G_ah-EwktzSJjGN0mYDf5sN8LvAcuuG5TRqW_b6ZQCm1IiFiBoABDuYEQub4Gx9WXdbQZMWwV0To61Ic3vgcleuZTBnmShL9terCQdWPlTGWrZBtNBeGNtE3D1XpjQgYNvBYjV_OpIW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbjCfFse6t1YbjGml3SlfdHI1-j75JHeGDhn4CS_Sz-Rd--b5MZznij5rB4fQ4rEKfwImdBEWA-mRXcsH0yGj4aSfxDjXKmsln8BTxFIyRyf27zQwZMl5Phoen1u2BSs-VNlElHQzEHHRLuJqzEbHgJFBpglCiSpdMe3gbomE3CGpb1yXPwMsydJY8PR4jOBjywxPBDamF1tyPmULlV3w2BgKY54m-6EcAgSpIZ2NnxkQHMUws0yY5A-jGdlu1A3uzjBtvABiqALg-v8C9G-MZ_Sn4QaMV6CaiaelQ_J-JpPbTah2xg8Bp7h8loPSGRqbuEO7jK6KHPygUymChN3bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7J2uektna_ROR7arJuz3sTUxNibt-L5yk6xtiGC-aDTOMVZt7f3BmrjUFNzp9gb1NefAFd2LdD5OIVDF4UlT7hwuPmZDvyTp9V23QYKP7_Hh-7sCzmitD2bxeuH-8fCc_UwVof-FTkPtM1fIhjIGjZXoEjgDorN0iwBlVphf5BWXMbye9bLIbQNnQaFr7Cc1l-cSujr2zAQUypNGEnGgT6Ni4Sn63Jz7QIftEl7ser4pkzvXK1J6fIbm8LdWSiH1t0YW-8wdzR8fiMEvA5Ge7vhD-O8gbi-nctTSH5ZcdvtgGUGcu4AtlSiQXylTUp-U_ZMHkothw5yMB7CLA4POA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d00Th3p_xUeho7xH8oDh82GYjBxUPEIYx5iNVUG6MeWcaOSsvjq3goePJvg9e329fByXl1sBQRhfRJHApw2iZZFETQeBElPRDYywebdE8tQ_y86hZs7nnfvkdn5nEWMjPuvUZuPUVwfbUXpt8ZJVRdKO2FtBClfW9-mpypDXZIgsZZTi2SVUDYXzycpylcoDqQ8GFT3_vz-d9QFEKjqc5XWTgR6ng_ExteIX-LllNj4C74o1xYS65oNVZgDFeDLxUqLqMqI_fkTuRcNsrafHW4gwgE4eYBHH3GKayCeBe8qSqk-ex8Zi8MiGtb3Xd9bz-lItazun5IAw5lk15oo4gA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzplK5f28XodfOAsA_ylJJdCBmjAquuDUzgZRrmVfnV5Vbiqm5740GHpPvCeldx4-H8VDSB-v9Wnr9mJqTq_dFRSicj7NDftDcIk82bat5cVa2izNg-n6nCvx8To8vf8febN4l4S_0UuBGvoCVZYgmpnOxZxKA_mq4y9kPjVem-ocqXX5caeQcSJmLx_5wm16Al-_lOIMKqR_CAxw98igC6XzwPXiI_nkoSG6AOHPT7SpXaghYpt5ck67skuRMlvhbfBearnwPWsXXLfR_m8T7ZkCSpoCKvYbGhwP79KNRgTOQDlKfysb6xGo4GOusl9JuNKTt0dG9WAHM68m5ip3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5bZ2KmJtao6yntQKWjPwQle9fMRmz-HU_zvGSpa7wmmYc3K_-muXjoNoBaxHwVAIKkgfxnLpq5BNdHYT6ehDjPUbuWCHmbK4BYfK9iWwgLbaP2BgVIC7yhJdvXab-koOOKJxcOin6Yqw5I6haA4HNbcHprjicAXn1mmbhPZai8sfnL5-cqx68-3AnMcQv8lDmzjU6AB5znp2Ai1qjo8T_1jw1vOtf7XMWCGS_HvsWPbFJSHWeYfp2OOZ4H21MOjrEX6HN5fYyGFTky41zN3pFDGvnXPhH0386MbKo8VlwKoj8WKc0ZVP5YlNEwfBArvKuZvZJeYTpjjKzMu98vJkHAs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5bZ2KmJtao6yntQKWjPwQle9fMRmz-HU_zvGSpa7wmmYc3K_-muXjoNoBaxHwVAIKkgfxnLpq5BNdHYT6ehDjPUbuWCHmbK4BYfK9iWwgLbaP2BgVIC7yhJdvXab-koOOKJxcOin6Yqw5I6haA4HNbcHprjicAXn1mmbhPZai8sfnL5-cqx68-3AnMcQv8lDmzjU6AB5znp2Ai1qjo8T_1jw1vOtf7XMWCGS_HvsWPbFJSHWeYfp2OOZ4H21MOjrEX6HN5fYyGFTky41zN3pFDGvnXPhH0386MbKo8VlwKoj8WKc0ZVP5YlNEwfBArvKuZvZJeYTpjjKzMu98vJkHAs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnGfTNNvyU-H_T9dqwvde_iM0JiYB0ErByd11Kwq1JN0vBxM2wrbROGY57_6Iq3NRo7VfxfoT-3AD2MVoiW9rWFSd6tChNW9V30ahmfdsSWc1GQbNziq-FNc6sKXiDoAYzQ0ksWYK5fnDHlqGkcYmQhVAt94Ox6IimhRZgD7VZSwKtX08SaUeJhJF15Z2Y1bXkYv14IE3KYxhPfLLuj7AU-QZbvL8SqNY3SO4Hkni1sOFzAv-rgdWzS7CHi2x8MKxr75Uan5sHMmzcp0SHBsdEWZwaYZIkaVzY-ujcJqw44L8hQzILS3gmbjg6ZC-ov6PT4VI-s12t9tu2J3-eDyD_ts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnGfTNNvyU-H_T9dqwvde_iM0JiYB0ErByd11Kwq1JN0vBxM2wrbROGY57_6Iq3NRo7VfxfoT-3AD2MVoiW9rWFSd6tChNW9V30ahmfdsSWc1GQbNziq-FNc6sKXiDoAYzQ0ksWYK5fnDHlqGkcYmQhVAt94Ox6IimhRZgD7VZSwKtX08SaUeJhJF15Z2Y1bXkYv14IE3KYxhPfLLuj7AU-QZbvL8SqNY3SO4Hkni1sOFzAv-rgdWzS7CHi2x8MKxr75Uan5sHMmzcp0SHBsdEWZwaYZIkaVzY-ujcJqw44L8hQzILS3gmbjg6ZC-ov6PT4VI-s12t9tu2J3-eDyD_ts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=RQ3oeNRfg3fO-sVuw7_mcNqYhGprWorwPpv-6NqSCbCUDb_XAEpXcGAGkAzPdrtBJjYkqQa22kTng9WnOef_Vsfz70OEzMYb36SuEZQhrs_jj_ALGNRtTJcOLQTel_NE4JlbpqtsLAp_4G1PwsJVvf1PT7IMpVXI9msNACFRLsc3JDHNFJ59PPfkocnD1niu49J-0JfKrWfAjG29rQAN7eQOe3XnDB7NdGOeTL5fVu0PqtFJrIw_jHIzISWgGeCkDM7Vq8r0LcKnJ5jK5EZo1dLCrZtM11fcmhF3OcGpe26Op9_cnLLnvazhOLbNSAm-WTFbOXq7SfijwxzSXEgFkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=RQ3oeNRfg3fO-sVuw7_mcNqYhGprWorwPpv-6NqSCbCUDb_XAEpXcGAGkAzPdrtBJjYkqQa22kTng9WnOef_Vsfz70OEzMYb36SuEZQhrs_jj_ALGNRtTJcOLQTel_NE4JlbpqtsLAp_4G1PwsJVvf1PT7IMpVXI9msNACFRLsc3JDHNFJ59PPfkocnD1niu49J-0JfKrWfAjG29rQAN7eQOe3XnDB7NdGOeTL5fVu0PqtFJrIw_jHIzISWgGeCkDM7Vq8r0LcKnJ5jK5EZo1dLCrZtM11fcmhF3OcGpe26Op9_cnLLnvazhOLbNSAm-WTFbOXq7SfijwxzSXEgFkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSPvh9-sCRcjjAOAYl8vG7DvQEYc57RLwIwKaaFr1wXZmmqJWQy4QXNr4RRmVPX5znGi-9HBFkQ7uJUpMeDe5dI3AanvQL8GXqdAHm07GFV52BcduWvnhWj6Rf27PBh-mlJaIFPsz4_PoGlWvEoW04cOQOHP7Kp7hwqAigd3uMGEaOupp1SPPyCoxIswTYDxJOG2GNFipRg9C13-mkATA17jr0A_ymHw7Ifpl7wMCfkQMVltUO7R9MgaKfVzDEJw8BMUBMiqTlMs86c097qloeQWK0g94DcGLhW6_9_6pEdYrggpmwjbOjvCElDITuH8LvyefVT3L16B6eNHMvKMAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBw2WkkAo4b42MT0RjvgoKJgGk3GJEGi5GwCwG9gCedBvcCN1VT-5soDxBIqfRyNW4xinSVZUtJGuQZVyx-Q6TjpKRRaTVS62Uc0L3c4DHpggZQjmLdoMHP4q_JhjC5PLSQ2KrdCv8iZ__SC2PquMI7ye3a4BhZz_LU15bY_Y_5zjcqVFRTZniEYylhm-pcwWVbVjnn_74nZgJ1fuL3jEACPYWyhXNvXJDBDyVVNEPsmMKSsZbSREu5KIKPUp4cWmu8WcZQbEqkn8hd131TOkvrJoSu_H8_KtxjFEYEvOjsejOEQEkPcDSQxy1Sd7RENX5uuUrXbUBsDKG9RUOSNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=TCMsRRe5cXvivn5pVeYKX06n6TYliQvUX-E6yc3lsm-p04LkI8MQkAC5VkvAC7bGeVuHEDlx2aYDQqjDRAso5dQVjzDyTgFEOT_3nZJ7KE0Zq3Ty-4pO8DxNxGQip0YYMgmNg7EhG4MwReXlGzuAWjWr5ELXPuSQj_9xkv0YMxnNrx20O5gLrYH8ndUrxEZhvpE7CJ1hyW-2-OXqukSA2WxXtdmUF5nrel7X4QbR3LQ9_EQkhf0FLl2aAUqbcDsfnhgSQq_L2Me8uTKt4DcSLIZMYjFfiA4zuLB0y57c2gbvc7t95C5c0bRORg7I9dCuk2kDw_JUVB9gqGU6ik_hNhMhgaKvpV8-mgJH-_Bd06hSTktVn7EwEZImCQxepYfn3revcI43snyfqWne2M1-A2VOvHYwO00JCCpAahmSLT96cDf3yOP0HL8ijIw9rF-jZZOJ3rzRh3deQY28a8RMEc4gDeBh0nAXOdNYvS-9pw3_PgXOIc8Y67YYaYNzk0FBbBQxHe9mq8nPUd-n7QcO7Ryb9Wl2jcOmzOmxh822pkoIZhXvmx6ZlWXCSfaN_LUaPZHFpjcISlPiqU6Lmh8BHiU4B0s2km1fV1JX_fhtD8yTHoBWWHGq6ko7s19X0mlV0bhWj065J8z7ZSENZ5kool8nOElhbo3K20dtSvU3x4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=TCMsRRe5cXvivn5pVeYKX06n6TYliQvUX-E6yc3lsm-p04LkI8MQkAC5VkvAC7bGeVuHEDlx2aYDQqjDRAso5dQVjzDyTgFEOT_3nZJ7KE0Zq3Ty-4pO8DxNxGQip0YYMgmNg7EhG4MwReXlGzuAWjWr5ELXPuSQj_9xkv0YMxnNrx20O5gLrYH8ndUrxEZhvpE7CJ1hyW-2-OXqukSA2WxXtdmUF5nrel7X4QbR3LQ9_EQkhf0FLl2aAUqbcDsfnhgSQq_L2Me8uTKt4DcSLIZMYjFfiA4zuLB0y57c2gbvc7t95C5c0bRORg7I9dCuk2kDw_JUVB9gqGU6ik_hNhMhgaKvpV8-mgJH-_Bd06hSTktVn7EwEZImCQxepYfn3revcI43snyfqWne2M1-A2VOvHYwO00JCCpAahmSLT96cDf3yOP0HL8ijIw9rF-jZZOJ3rzRh3deQY28a8RMEc4gDeBh0nAXOdNYvS-9pw3_PgXOIc8Y67YYaYNzk0FBbBQxHe9mq8nPUd-n7QcO7Ryb9Wl2jcOmzOmxh822pkoIZhXvmx6ZlWXCSfaN_LUaPZHFpjcISlPiqU6Lmh8BHiU4B0s2km1fV1JX_fhtD8yTHoBWWHGq6ko7s19X0mlV0bhWj065J8z7ZSENZ5kool8nOElhbo3K20dtSvU3x4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=HAmrOIJQgcGps75U4nu4rfgZ3d3YqUMcl5cAOhHg9eoLUNLxGIbntHGo_K6OVP-DJgNXmK584lUct5YKmbRNYtSUwOMcdRckreLkCg-5ld-4CWIgPGCyDcMLRuD5RfrVLxlw-ux_crQYYLsVH3eOvF1I38TTq6a-CeBYB5pF62-X7mt4KUVRPEK9gFYPWNzetYdl9h_J2jCrPnSgh-gtSHYv63mRZMcUPWuCNTyA9dgfcGNyoO10Q-a_doN4xI7XVKKnccYjT4J5D0B4FvbL6Py2AcdwSb2qnBony8IX_P-l-9rzbZoM9uv3fApR6HwPYTrph6JhbAYKYzV7PryB5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=HAmrOIJQgcGps75U4nu4rfgZ3d3YqUMcl5cAOhHg9eoLUNLxGIbntHGo_K6OVP-DJgNXmK584lUct5YKmbRNYtSUwOMcdRckreLkCg-5ld-4CWIgPGCyDcMLRuD5RfrVLxlw-ux_crQYYLsVH3eOvF1I38TTq6a-CeBYB5pF62-X7mt4KUVRPEK9gFYPWNzetYdl9h_J2jCrPnSgh-gtSHYv63mRZMcUPWuCNTyA9dgfcGNyoO10Q-a_doN4xI7XVKKnccYjT4J5D0B4FvbL6Py2AcdwSb2qnBony8IX_P-l-9rzbZoM9uv3fApR6HwPYTrph6JhbAYKYzV7PryB5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPGgi5ZjgFc6Uw59Dt5YtpEt_KYf139gk8pyemhyIofH6YRE-nZl9MjZnGX2fzKdgVZIYAhVTaixHBu-GLt8ntcLm4qQHqOXn-6KO08c7i-N9w-NcCzHMoUeZLK8V6Jj-KadoVDbNS1r_saSkqKGTGawK3MnSakppYBH7Et9XM2TPY773B_C5juq8-aJbD9Qf-iIjMwL-RWzAJ2FA9x___Cvo-ofG0yWekPioW5fHMVf333rqcFW7jGqSh0gvyKSastCbhQLCqtFCKVCCd67-rb7ZXwojTbupeZxMgN07jTMWiZt7En9hPfoslDGA-V6IoD9MOZqsBLfKSHaSihR9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYS7918eZSq7mxNZ4OU7P1CIwiUklikXEwgjH_Be7dSaj6hW3fAWVFfy_yXB8CeEXGrkGUGAF6r2zMOqWT0A8PfbW4fLtN1LnqJfxrn6rJbsyOdCE0BXUJzfidGclpr8jcOTrM9Cl9wn9xghzPtgdV6F1SL62srYbaRvVwGiD2jQkAH-7-anyfzJBQ9YZz6z19N2MBNmjSqsnsZKwjXBDBdZFQdHTI1fx7ZzcWa7r0VJmBKKX_jDvwI435qI1I2d6fIYkOS2l5XY_TrwaC-48iPVel8JxLm_efuX-Zk0m15bt-p7KDJqWcEDn2c_5kiusLuDU0Lmn7PGXCk3RJot3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v63i8QpCT5Jxhl8jef3L5SWDTNKt8Vu5xfiWQHKgKbiupDeCNGXIm5rOwDZQqhtVgZ-EYm068pET4dM8SsTwQwwK_CyUTbxHIH8SXs1mC5v2eeZypPXPdLuVeYCzF-jRYSTfVloP2yXapdb43EKKyeXv1QhSZ3gpnR_rXLxTbd3Pcvq8bJKAhpcR004RERn6PJqVYPvTF4zLwxNtZw2slHUQJhSrav_BkKpCUuKXMw0Ozbw6rQdLHbXVy3mUfA980ucOGgs7C1UP1dCm4dZZ_6Okb_mPdl88qQ2aB-7581SQFZ3Sz53tvhR2oHzmm1ELBN6DYFZOXfdICaivLHJ1GQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=Q9IxZEvjz4hxdz1A6XEYa8iNAUhJ-19wCbBeIwa4J0THZ1sFN-FMBDD-Lc8bR35zX6JPWFVjsaympSmb5ADzIXKQhxSpA07SBazyqcPaQ24LCZOo5fx5UPcg5Vv6SL_wiF-Uir7xDrxLFWET-qCm19zgpBI_UBE_skfiqlUGvpRXz01tQuefm73XAC2uliC1sjdM9o9S9n4ui8gU8VBINFZVIPphsCJ5TQ5lqqbdb4_f_LsfDXG5Ye6pK28tM8HEIyV4hhwTEISTIjha-CEC3mfzfMFzS1h0WhW4f4dP2CmJ-GbyM2ASU8RIGjPWzlgnZMctJHtxOSPFwf3zVriIqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=Q9IxZEvjz4hxdz1A6XEYa8iNAUhJ-19wCbBeIwa4J0THZ1sFN-FMBDD-Lc8bR35zX6JPWFVjsaympSmb5ADzIXKQhxSpA07SBazyqcPaQ24LCZOo5fx5UPcg5Vv6SL_wiF-Uir7xDrxLFWET-qCm19zgpBI_UBE_skfiqlUGvpRXz01tQuefm73XAC2uliC1sjdM9o9S9n4ui8gU8VBINFZVIPphsCJ5TQ5lqqbdb4_f_LsfDXG5Ye6pK28tM8HEIyV4hhwTEISTIjha-CEC3mfzfMFzS1h0WhW4f4dP2CmJ-GbyM2ASU8RIGjPWzlgnZMctJHtxOSPFwf3zVriIqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=XPfSSc1Q3EddBzr9BNJ2g6e0DC9JuFTcVaK_QjstvAHxKPBhN6dvHmdJ6sFs8HgbSYVsCxj--wDhGty8HdhQlIDtLrmtKnPEVbtp4fd_mez_J3P3PGtL1nx46SpoPNzNojjZor39KK3ELC3awI3OrNAosxxUG6j8jBeKW3Ba-ofZLlJQq5-znsP37ytmWZgRxpsZy9mJGXnuudoES-3fQKtKbXYbrqF2HaV6Mq-82_G4HQoKdXQa-FtJZXgGrToRXj9vmMtTofugp-0dz8Qc2bZ1Pn-7EhXMXhnq3xBNHP6oHoN97GWucTyot2KVtylJgbUYUj5NbrlMjRVrs5UJj6gYtOE6in4mceHGlvL6af-rTHIwQhrZ51sX9ufGO-MIDT55rV3wtzlANW8gE_wHVWYascG-xY60YnMDgp_PPL2kzt6U5MC_h4hMY7Kfjad-Bdr3hgDNsWrfFPuT5sYRLaTLiD1ohHaQPIiltxKgttKqN99-MMSI2OPoz9phT0Hg7pcT6smYHl3gyfnxWxQgufPqVfi15G6HO7BUqG20Cnb8xuqfMkrKW2bG5UF-qdH3SgtPvwFE1guUbwJbK4OKYbcEVstAqI4Y9W8aRPUid8X-CCo1xdy8ACgeS8B-EpvNRefyTA13xo8yRTMcaK2fP6a5J_fTJRhKHS_YB1ruIuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=XPfSSc1Q3EddBzr9BNJ2g6e0DC9JuFTcVaK_QjstvAHxKPBhN6dvHmdJ6sFs8HgbSYVsCxj--wDhGty8HdhQlIDtLrmtKnPEVbtp4fd_mez_J3P3PGtL1nx46SpoPNzNojjZor39KK3ELC3awI3OrNAosxxUG6j8jBeKW3Ba-ofZLlJQq5-znsP37ytmWZgRxpsZy9mJGXnuudoES-3fQKtKbXYbrqF2HaV6Mq-82_G4HQoKdXQa-FtJZXgGrToRXj9vmMtTofugp-0dz8Qc2bZ1Pn-7EhXMXhnq3xBNHP6oHoN97GWucTyot2KVtylJgbUYUj5NbrlMjRVrs5UJj6gYtOE6in4mceHGlvL6af-rTHIwQhrZ51sX9ufGO-MIDT55rV3wtzlANW8gE_wHVWYascG-xY60YnMDgp_PPL2kzt6U5MC_h4hMY7Kfjad-Bdr3hgDNsWrfFPuT5sYRLaTLiD1ohHaQPIiltxKgttKqN99-MMSI2OPoz9phT0Hg7pcT6smYHl3gyfnxWxQgufPqVfi15G6HO7BUqG20Cnb8xuqfMkrKW2bG5UF-qdH3SgtPvwFE1guUbwJbK4OKYbcEVstAqI4Y9W8aRPUid8X-CCo1xdy8ACgeS8B-EpvNRefyTA13xo8yRTMcaK2fP6a5J_fTJRhKHS_YB1ruIuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7ivVpJrOJ8pNfYpk5PJ8yvrygX1UJJGTEFlqUuWv7zm63qpNYPVmgU3pwpzX4cIPUFMMokx2snUkU4CfJmU8gB9hicmaVGW_IFsJYPtCvunwO6RYj69GMpSidaibLZx_Z4je8k-NIflBrwcgbh-x0yRkTUnDdmxQBAyjmG3RVXUdDTiPZ4aE5K4Dr4v_mZdF8EJUfcwY4f9GwmOA3J7_-s9gok-EdIZKarQ_5dykkKLo3SJjYfD8QRKyXyzIXws50INrVLyIEG-zqFIactkc_zR5b7qZ70O_3DjJ6RBbRs3PbCe63BtNlQIuKzz9QTedNZSADbF-5Qworl487h_0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quPqalXUpJZCWemVBAk-dP94sF0f49IYOoYFMp31Ejj60SmYGnaU4nffAmyn7naYzsHDNL9aN8oXqPn4kdQnT3uW3C665zxryH1dd7u6cbUZLyM689FZgCenN4rnZGkafZLQIBTkN2ordN6WwBWJW2XxwPbwjm2RIGALE7DwunjEjRWJPepX73VXS7gsjrqTZfTG8HGMEiYnX4kAVAYIatDDvLd7uN7MDCOXNeofJ6aU5fknNO2ucQNR7sxbdPCwSVNyyyyvW5WizeyU78DlBIIOuClh6uZUkJ2JiRvP_9UqGwGnWitf0tn8cR11UbyY5D7BcYO_GqU4rF4hCStp1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=CS7Rx05elmO7wn65nUJ9G3NBUWEfzg6F0uNffahEeS99U92Qfeuzk3tojibvJc61zPUHhOjgBXRdWXZGO-fUgkp1-li3gqdzDHgYIis4_7AD0LZWaQ5b7ozzj0YZPzYs3wjJQbmUGlDHofHhZtKEJcUQo9H5oDR0fqPRH39ZDStfRROGtzvNeF0nBLx71aiKs1x3BU7IsOCN6PIscTitgUzVk7lTB2loMjxAH0t2uqOIkqQHsjFCGUxpbBW3MB1Yg-_S7jpdVFvM66PfgoLrF9yWrnfC1VSCabs8wJvTaydRnkORL1NDHWA6k6-Z4B8bmHxMM2MEU7t6T3CqYOblQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=CS7Rx05elmO7wn65nUJ9G3NBUWEfzg6F0uNffahEeS99U92Qfeuzk3tojibvJc61zPUHhOjgBXRdWXZGO-fUgkp1-li3gqdzDHgYIis4_7AD0LZWaQ5b7ozzj0YZPzYs3wjJQbmUGlDHofHhZtKEJcUQo9H5oDR0fqPRH39ZDStfRROGtzvNeF0nBLx71aiKs1x3BU7IsOCN6PIscTitgUzVk7lTB2loMjxAH0t2uqOIkqQHsjFCGUxpbBW3MB1Yg-_S7jpdVFvM66PfgoLrF9yWrnfC1VSCabs8wJvTaydRnkORL1NDHWA6k6-Z4B8bmHxMM2MEU7t6T3CqYOblQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PozjZQYNRUFoXabr5cW2xj1xnwlZv0P1_dcK8W7yG_02CYfFFyvUZh7Nxi7UiWtTMjxuize4oFO5dVHHBlIocrmbld5_0nO27Bb3XqDO227vhmLhF_yojchYAv9uwXnHF768Lg2OIITnUKAE4jf9pv-T6Tz1kHDJC3Vdn0YnMgQfhLox7x6gnfm1ng49Qc9nroRS8okZllpfFVzpXdq-yx_jBueZOxQCg3xCh-HHri-SqdBrUac8RzMu6IZWEStP0j0pp_HpJziAvqVVd9hC0Tqi9q5_H-ks4YZ21ZR_v-SROGZ9M3cuR6UjSCDbERXVYrQ2o4EfMiUQxiBKySO2ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2YcvLt25bgAvqSvW0ogfabWzS9wsUPvxd26CtM1IHbjnJN6j9YGY8Ngb5nAfofw-GC3NkkGRPWoSmu1J8h51dk8nchZYoLkDgy30nuDAXAeTPqWmY8KrXe-4fQ1r0h8t1OKNTDQSjCveypxVrSkP7MuXTxlfOtPm_uKocSiedJGuybFKe58lDBLmn3mogLTcWnyYykmVSW5slVutAJc6flGsBPK9-Buyz51LIYCyyVbGxr4sLTMm-i4eUZjmI7qZBXHC3mOka6fKzhQUFGgrIl-2HRNw6q2ZKLUXUNs2HDHADrCWzfmKDXSUOCWTUxNN-uxj3qAKamEhDLYjyKMpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQ1PJ39t66IgevEH93eOzAd5kfvXqsv3fH5q61IR8auOIySX7VyHV7rEwF525AIchTgucq854Pzmipae1FaZ7pfk0BpjEwJi-uANFtI1DMxHx1FN0kG_kE381F7bBJYgB41cWJWKXtPKOKtOh9mf2gAwWpKsl24RTRXlFZL9CsrBhPnotKcxpLxtiXCGN2cRbs_iQb7RN2tg1AHCtXz0JzeghdgD0Ke9UAvi7_rZTB-2bBfNBRFNv_AIzjE6cW3lW-lzo2YBhfQ38RrC1kq-CYbkqQZBwNDcKpqIsp0uG5tK4laPHmXerMmxqawvOAMU8FAaljKDPw3krf_HW59X_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLWCGrcY0rtOI8HZzg_5g3hEb48Fm4GYdJtl1pbFEAaf14A-aqIPQsMGmDRQmkBdH2792FwVTpjZKfOfs8LKhuvewwDkmvWqcMJWsQIOW4J7kiZaoMQlkmcSQU-WFrEYlSrs-J1UaFE0ix_wlSZRpprX0JPGUV47iuRZThoQjobs0FdZyCdT8ccjwLBywXpL6YXYM9PlltuH_ouwMPDhGKT9W7tuK6zMr_7c-QLQfMXv3T_S7L7iWiklqt-J2HhO1rhpnwyjuIv0b2SGY8pI_QKV1a117FjGBA0YgNHZP_U4SGHSV310l-j6y148zeLkNCUcagJ_EJUCeBUkMbHZlbsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLWCGrcY0rtOI8HZzg_5g3hEb48Fm4GYdJtl1pbFEAaf14A-aqIPQsMGmDRQmkBdH2792FwVTpjZKfOfs8LKhuvewwDkmvWqcMJWsQIOW4J7kiZaoMQlkmcSQU-WFrEYlSrs-J1UaFE0ix_wlSZRpprX0JPGUV47iuRZThoQjobs0FdZyCdT8ccjwLBywXpL6YXYM9PlltuH_ouwMPDhGKT9W7tuK6zMr_7c-QLQfMXv3T_S7L7iWiklqt-J2HhO1rhpnwyjuIv0b2SGY8pI_QKV1a117FjGBA0YgNHZP_U4SGHSV310l-j6y148zeLkNCUcagJ_EJUCeBUkMbHZlbsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hTNbHMJ4-mTSVe7l2Qtu631Za-g6OhhIOZrStylokRpsouxPYSRhhbZNCySNMc9S9MU_BJv77_wEykiR-seveALymwxc96J38QCw_vRbrCO0uus0m9nizFCBaGHryj2xXwDEK55n-cx8IYCdxKJs3bHjUE3W8YHt4wGRI-VAipAKakq9T9nMnTvqrzR7VZr-4sTi1POT50T1ba5wfDiUsoNPKGJJtyIhzpqAufrQA8AYbRXIchGjCY8lIkvPlA7pSkeIIo5iaH3BNvk4IbrClbhBdfagy3xaqQgHARQ4FLhLGp1rmg3p6TSllD7ZtGyNckAI6_SjWOn3AaKldVA-Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oYCZB7WKnpzGbYSW74EdTbq2X9xPJKBMFjZ9tvZIQJK92oPmN2MliAPUWOMd29HbJR3Sov7rj9yvRIpcv7hDuNmEFvp-M5w8gBAhGkMYvhuC2bvEYvlaR8YICk_P8edFQCfOwDzaSZS8wUI46__CujLyZ3wWwcnHTCmZjmKubCOwWDPpXOqR4sIWslqs2152ulYwZzDqLIEvQQgyESV-2Io06AAPCRhJW1syxybxqFxG2TOEplzZkv_QQPzlX8VEbbZe6fxZELolSv0W5GeYeg8agnIXZGt8Xd-FDCJUGzDFRkfhIZk5pBX6uEejYgBPTBXFLzJUlo_L7xz0Kp0hIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=NEgXmOCW3eyDSfmxAoaVBL7DFx8IWpCFnZHrnaqMGkPkemNdl9umbHRkZYhOVIcoiXQNQ_q2GkCwPkVZBCaCTSWdXF4h_OXmnqWdDYxcOV3C-u20Ra9P1SQSt6mhWMAbIVSclcwT9Q4jrlErLCmhkbKZg4w095ReRCTZAmncufT8O_Frel_GpvK2mniSTIJz-MxLjVTqDzpboQAod_PgaIZJrNOJXuWawlMejPNFExhvGM5berwW3XY2TFSDa5Svw7zh8oS539h0ig2b-bMIPVpNcb7YA_Kzq_LBfSEWA4FOcsXawvxEJfHR44NHuTAQ_yts_KwMWsmFrvAsHnct8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=NEgXmOCW3eyDSfmxAoaVBL7DFx8IWpCFnZHrnaqMGkPkemNdl9umbHRkZYhOVIcoiXQNQ_q2GkCwPkVZBCaCTSWdXF4h_OXmnqWdDYxcOV3C-u20Ra9P1SQSt6mhWMAbIVSclcwT9Q4jrlErLCmhkbKZg4w095ReRCTZAmncufT8O_Frel_GpvK2mniSTIJz-MxLjVTqDzpboQAod_PgaIZJrNOJXuWawlMejPNFExhvGM5berwW3XY2TFSDa5Svw7zh8oS539h0ig2b-bMIPVpNcb7YA_Kzq_LBfSEWA4FOcsXawvxEJfHR44NHuTAQ_yts_KwMWsmFrvAsHnct8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=hViqSTkqDvYO2QW2yH-sf6DLo2brgRpawqOttHtmbFCXWtecSbbCAIg3Q0fsgX7N6purfZG4y8tLABj3W8n55VSmpq3mKMMMnbhRiplr0zVcBFrKy9jpfMXMt5LloZDprNczimehORoz8ChPEJGVoAdfRholFW17973FF1nu-obpEPP_kzVzoxPhsijr_GVT7KUYbd8cPtOWWwVJ1YLi07Q34z3UW_2lv6WRTkM9hBeq2NIkaxea-x1b8YoopYZgz1pgYKaIsNIpRLZodLd9wN1tmjHPk84jBYBZA9U9ebTTSlbBaZiXBEOJdgD2gIN3u7Ow_Sb4mck1IVeJG5PuFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=hViqSTkqDvYO2QW2yH-sf6DLo2brgRpawqOttHtmbFCXWtecSbbCAIg3Q0fsgX7N6purfZG4y8tLABj3W8n55VSmpq3mKMMMnbhRiplr0zVcBFrKy9jpfMXMt5LloZDprNczimehORoz8ChPEJGVoAdfRholFW17973FF1nu-obpEPP_kzVzoxPhsijr_GVT7KUYbd8cPtOWWwVJ1YLi07Q34z3UW_2lv6WRTkM9hBeq2NIkaxea-x1b8YoopYZgz1pgYKaIsNIpRLZodLd9wN1tmjHPk84jBYBZA9U9ebTTSlbBaZiXBEOJdgD2gIN3u7Ow_Sb4mck1IVeJG5PuFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMfXVOoL8Tv_XglVlbzRaWXdgIo94zb0ib5t-cK9-MFv30IRaqBkgRR1Llj3qc5pEW8YxBHBmeqA1ZucVNqPu0cHIEwznJ5wnursfQe4p_MHwuFOrIZtzP_2OAN1k9FV7UKhYClzI9nyNGP76UZwYVsaj0RIZgOEVmhrsm8ypnUkeimhZS4TljJr4GY6kIFLyJ6eXz8CvI6dreP4Qtj7sd2Qitv0uQQUCM2B1MmD1WyVVyDmLC4WtkciIRHOXnwqdoYi_13_CcdQuL43NHl7kIDVHd7xMM6rZlv7Nd8LLO1u2DGvGoWSEF3n8dh2VWXUPYEpH2wwtQRo5_-2_TyRXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=bEQDND8fmVMENoaPAMRMwamTdFQg7DYXS83i06BZBVZZFtWcvyYfozxID7wUuB60FXfV54rKtawhG8GVWBllVx0IxhZDzgJV94iTeJDfq0R9J9NShznpwqP-SkkWGRd2STnlrMz_VyzEdpW2J0MLn9Mn2DTvKnQjIy3juFPXiQRZ02IEHbf_jnMt6wlivjQwXFBMAB54MwLV1bkK7IfKVaQmHoqau8Hc1dMHwq8kuKhaqlxDC3T0xAsHdEVercNO9Pe8WVE73bVObxi0rj4MNW1DiNIMcqkLrdpsz9nE1aEodO2CdrgDO3mGLrnBsBD1jtJT0gQ5HbAq_s6i4W5v0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=bEQDND8fmVMENoaPAMRMwamTdFQg7DYXS83i06BZBVZZFtWcvyYfozxID7wUuB60FXfV54rKtawhG8GVWBllVx0IxhZDzgJV94iTeJDfq0R9J9NShznpwqP-SkkWGRd2STnlrMz_VyzEdpW2J0MLn9Mn2DTvKnQjIy3juFPXiQRZ02IEHbf_jnMt6wlivjQwXFBMAB54MwLV1bkK7IfKVaQmHoqau8Hc1dMHwq8kuKhaqlxDC3T0xAsHdEVercNO9Pe8WVE73bVObxi0rj4MNW1DiNIMcqkLrdpsz9nE1aEodO2CdrgDO3mGLrnBsBD1jtJT0gQ5HbAq_s6i4W5v0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=iFyX9tHkwfJKcmDcNMrkf3VIqP81oeOvSS5xHaR7y6ouI_YE76JSaJuxWyQ4gTPppq1g7X97lekXi-SjdLou4D0T4i3k32JdKRdWrLAkF0SSxhd6dZgP98Wcq3P_IDcR_qQqNVZyd9OA_u2zM6AQzxYpv7ANYxcR6pRuQpDHzlH9587s_K94lUxwD6f9tHbDlM4tMq2rqa_QUaNEC2ozSxZWD87WG-T0Np3B6kXMzCbW0JCTC2vLVsAPQgSaliuqEPobUWz-ggEClyWd5pmnoukRtO90EHC7jDNxi1_dbcWHCwS8rMhPuRuEpNw5k7Em2IOV8hAoUC0bCSQCzIdAdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=iFyX9tHkwfJKcmDcNMrkf3VIqP81oeOvSS5xHaR7y6ouI_YE76JSaJuxWyQ4gTPppq1g7X97lekXi-SjdLou4D0T4i3k32JdKRdWrLAkF0SSxhd6dZgP98Wcq3P_IDcR_qQqNVZyd9OA_u2zM6AQzxYpv7ANYxcR6pRuQpDHzlH9587s_K94lUxwD6f9tHbDlM4tMq2rqa_QUaNEC2ozSxZWD87WG-T0Np3B6kXMzCbW0JCTC2vLVsAPQgSaliuqEPobUWz-ggEClyWd5pmnoukRtO90EHC7jDNxi1_dbcWHCwS8rMhPuRuEpNw5k7Em2IOV8hAoUC0bCSQCzIdAdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItFpq9F7kSJ6bRjOuJ0-MYHR5LdU9o1B6iP934DtrlZlUFt5L4FYCtIFPJYkXZ1QsU5qEAjwgnTy4QKa4y6XCB9U8N72vkZOtKuRB09d_sZadv8kbUxcZb8152vHvCLuN_m6qQPQeXQNWZ3EzYREU38I9ofEtP-2mtZl7o7JyExhx0_0o7j_gIYio7MZeRaJ4FyQo5dN63BLU39Cq4C83QZ72koVxKr2mZSIHbPqXSEYG7J6C3D-7DMyYL3lq-20RSl7cf6y43fH0XisFf2ntZNVwe4z571f8CV8ur3qm9Fhq2kQZbVf3UCusFOuUzHk5joRCwpNGd3-bPnjxYPn0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yd6Miw5cdA2QWt35wayWjw4o8ue8Cjlw8y_H5kWfm78K91BrpONWeHnjDFfOiBG6_7qFH1lV0_4z7UvU_uhZiZa3dQS1mnDKuYvaSRLlsZih2xZay0eVJBrWL9elLr-qT_G3ynhckopVatACd87SjNLrh-RJBm2KbG4h6Js5uE65xHz5Xc5WVdLugVspGg0Bu4rbNjTKExSLUrFn2wd2qCXOz1yYw9KI-RtzgkSWCbehBhG37Lx4j3fvdLp9mg4ZF4_GDneL7GEldp2WHBYYG-JZZjmvj05YscfJsWtisimpMF6HNuucxnQqO5R-K3X1ej8S4jBDRf2YfEOTk2o1JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CD7FPQPt5VcJX7UHYy10u4uOUXNqaYUS3Qp12G-e6A3NHQwJN1wIvmfZM4xpV2H_lRxrYhskfjpGKkB1X0oWSAqh9MIQxQ2pl-6FNXrrrfNMVZD-P-d-x5rqaalyIZZBsWWQlcmj6LHFdr_Z8nHjtpueie1NpztKXtB3rsxExCq4tocIVDVxc1P6Qg66cLm3eeHZHiHg2Rrdk02wJUY8eEToVaKu2o8vFl2FM9bKpT06t-sR83jTO2191PDW06dkZE8ZzDUcv_3Daq4Tz7S0iXiPeISGd-FIOmEwQ-926ElYd7YPEXjKcoo_QfwgPzEsyB8SS78p7J7r99gj682OQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUPgTWaGBEXkLlofZ2ibpkFRSdeCLbaChmpdHdhXc3AL7TRCMfdZnqwUm-kIIV1d5RGnCIUSUbVzuZVJwwheLeXUSeH4LmG4p3MrZ-Es3ucqdmvkZebM3q8dcJ27xhQKgN4xpgJ6WU4WhGVWUGQvgfsc3uPdTpt1CfPZn3KbZj_lq8xajsqL9cWq2kCr-uwI6rqLW-gG5axb5cP2s-AQkKe2J_0iIMOm0wUCWbhl52xN3ighNGFhApVGlQiWXiKFL0RAPQgu5cXSLAMHkrY7UmGqjAkN1pODMih0sjc6Lbd0F8dby0AoS_apyaigWhGmXuQUTgqU8pVe5Q0tt2VHVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U07alxCCNcZJN9rmoj-rZu5xNSX0ST-N6EA73SOlGC75MNp2lCQF6zGuiwGWgQvOy_8SxgHbywaaB5poZGXO7Wt586Jpqmycd5FBddBuCK9desdTzwTIaNEV_7tamrIwp2Yz8uxH84Iwb8lsmVk4A71sHnBk2TXXVTA0J72x5FqoAX5L6gPMDQFF8lRhZDfHv_G-MtN6lAozHAyQ775vl7CBw1SAaNgWD205INNKLqqrtY5S07u9XXCxYl4-n4F17WSdN2SyNZpYjgFQFeqwwsC5BO-mzs9gGrOApKkp5WUHyW4zm4RLOFxU8MnzA_dyuAi0ghcGUuRf2cVwLsGxpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ngy8n3yMl86hbAOWeXQIJSx7E-UvpgbE4CUwmXQvH3wta3xl_d5rEVO9dy2Wu8H7drpQmfXleOx8DczdEsCr9j82kufe1SDv1SbRQJsUfJxYizo89eLmMZcwA3wA4XtpY5260rytjb8yuSlzsc_gWMGYN94i9ojtC_8vTOxZO6iyXsvJC2QEDXKaifgY6cJzt6B3Fa3MRf33JTPpHJwX5OoSjCHVEWeD1MQS4pSc5eS6xVaZIQaU6imdO3WjllfsE81pukht4LNsO25gfECRmPoRiMyQksKXVjUXijsF-z7tjnYG-oLi1I7gTZO20DhgJje8lNKdAJkV2YqI9nPv2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/luuifrM1novcyVdD1ioDXo59rlP8JKWWNiFjxQN8H8hZVMhQ-VTciwcShtEECShc3KTc1hpRjgrcty-hKX2B9HaWshVPWB6un1GCb-N3rP1ExtFUIbr-UgPyUuRUqC0vqIORTTBe7CxqXKebq8-Jx-XmNGlKZRXHwntRvlVgC-2UQPgMthkg6Gt6ayFo9Rv20Dp5SBNLlbwGyuhe_luMM4-cVOeR9tjlmiNtsaDblDY0SdrrffGVhhN5Hi8bu45x3XiCk-2WJ8pKNo4m5C4Io-h30mnt2Hk23REgkOMRSh-UfDOnee1sWnKebAp2Y_zxDjTjPKZ63oxg2P96oWxU0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GbzJ-h5clm8k7Xnke9_aIdT_Q81jwhPOH-D_DN1IQ-7qRkfVmXN-v58YenrqkEZ0vxPoXfuyEt1AXxwRfbcTrNFuTkQKyx27n0Y3O0Y0UxCMLiyRniTVpYQ7CLF1bsNAy2DQV7K5gmUoZkfxUpHLaTGjyFTl793yH5iCT9yxO6waGezvbXvq1txAjcSeaIijxzV522wgqx5ImnMC7iLkvAgODQUpn_V1GrjzGCUFM6wlkCfV-ddair0TJY9b8FxHX5o5c-EYqHqMaXO0LFX_veRCLNijM0K2uWUGBKL7ZP0tpMD0bdAIkbcxAyczTRUXKjsMN3QbBtSnB52Mx-MfAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKiUrSOQCkJAh1jE0dwTGEla6lP14zAWBCwUpNO2WfZqX5k0cMSogJgR6MuCDxyWzldyln_vFiPcnVv22hbu_AAiJ9EYNb4XREHqHe5NSyTNs-wYMp9WPnNeetKL9b3FhQGz3og0lal1i3Q89byGvMKxS-AfjswAVqY9zaqApaRJ5cMBIOurm94YULQm9GR6nWH1RTAhMONNgJFAdYmvNqj0NnIeh-hgBenkxkX50Nwwa26_iwo_UYaPrrNH7MlhmRnSvV1EmwvqsP12liP-Gb7gl7lb0yf6UADlmQ15n2SRw07RzAgPdywnSxa7nOxLK4NUdadcDP3XuswCTKqVyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnozasHfg6Yoci8TH87pUJ9juReRjRvPyhNy67hqF6QvP9-LDK3cmUYH-ogwUXlXVnSE8xQRxZNmemaqLiAw4qNgarttE39rU68i3Bf7xCMvtubg6QT49Y8-8RHH8viHPZmnRPzzLfZmNSMsb0Oyy7M30GWdoRF7f17IoEKE8ijpymolqnrCX8mxJCK795m5IDXRBbBXvNQuHeO2PSL5zF1AzWoIF5OQCPW1igMwKBbwbejzYi7LSm9x2pp0eWHGQxIqkjdNFAbvch_cu5VJ6LztfvyURpu5E4dLzvCd9HpsIIV4HXuz7FkxXYu_TM5sqcn_gfyr8bco33CZ8zEhiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=TcXg94pcaE6sMk02nIh4LjWKD1gmqahbfZhC02sZaaNqWeFrsqfwDPlxWiKrlvGIMa-WndL4uN2qXGn-9tvXTEfXgZxy0nBbr031_fH7aOzvrYCzSv4zXKPsxZvSigifJHMUezkgO4Jj8Hs10cJb_EvPssqw8IKRbLKPnqFzTVUSOWqsiIe1Wo-b3hjt-yLl0fGTUW3zyZKo_gmekgvv6DELb8lHnleofa-9TFG9R5FjT5LjfQGN6WE47IyqRa8_SohM_JWKdaAyEgke1BiCUFB1eQBj9HGFvdAZikBzJrVdENTe4_cgSgRMTvCuf3svPRQo3lLkFrIu93nLj7uiRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=TcXg94pcaE6sMk02nIh4LjWKD1gmqahbfZhC02sZaaNqWeFrsqfwDPlxWiKrlvGIMa-WndL4uN2qXGn-9tvXTEfXgZxy0nBbr031_fH7aOzvrYCzSv4zXKPsxZvSigifJHMUezkgO4Jj8Hs10cJb_EvPssqw8IKRbLKPnqFzTVUSOWqsiIe1Wo-b3hjt-yLl0fGTUW3zyZKo_gmekgvv6DELb8lHnleofa-9TFG9R5FjT5LjfQGN6WE47IyqRa8_SohM_JWKdaAyEgke1BiCUFB1eQBj9HGFvdAZikBzJrVdENTe4_cgSgRMTvCuf3svPRQo3lLkFrIu93nLj7uiRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=Rrrr8JO66TYSDVNj3TJFfa7KOmhDeQk0vKflJVipBDW9_bJq6FIkNBi-7vK4QAKyrBU3U2JrJxw6GRiKPUNQl0l0CAU26Ak9CqqxLdlbStlyG__ErpUlPZc9TuqdV7VST5MTWbRHNmiP5LCTNfm0cGvXCHTgvNHpw3cfBbZwYhHgNXYEDibs5OjpCRDBdaqbqwvq8wtGPep_svVddchHFRuhQaoNyvAQNXUO_x9erdi2q74JX9fUReMiz5W65JpqAqfbjsTp2OYwW11a2qrKRgKtS_W5fPYNIYoO8UmmNgTOgSlhSuxqwG1Sws9kJzhvjERJT28QSY4XYo0Ch3LFOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=Rrrr8JO66TYSDVNj3TJFfa7KOmhDeQk0vKflJVipBDW9_bJq6FIkNBi-7vK4QAKyrBU3U2JrJxw6GRiKPUNQl0l0CAU26Ak9CqqxLdlbStlyG__ErpUlPZc9TuqdV7VST5MTWbRHNmiP5LCTNfm0cGvXCHTgvNHpw3cfBbZwYhHgNXYEDibs5OjpCRDBdaqbqwvq8wtGPep_svVddchHFRuhQaoNyvAQNXUO_x9erdi2q74JX9fUReMiz5W65JpqAqfbjsTp2OYwW11a2qrKRgKtS_W5fPYNIYoO8UmmNgTOgSlhSuxqwG1Sws9kJzhvjERJT28QSY4XYo0Ch3LFOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=Ehsmzm1mPP0LvyzLRLmmxxwTGRi1yR4FQwmJ2TCwW5MKO6ENciaIU_t7OTAwd_AcWrHb8GKJPFS_Xf1sAZybC2JSfoY9Hn2xCcf-eU7dHkD9WbqngKv5IzYIw3qiX4pdXkMvBFQUmxuPsE0hwepcc77144PuwSzoDGW1xfXSUb-utVazBCwzZVAIm5NheiA6SGJS8feAJAHxwe2-jYWQs8JqIwMqUXCqpIph3LVu62IFknqmbSTm1fDl8FJSZNZzbJfGrqsNTh28m5QCnXWLUL2s_CgBLq65uJ9mPH0nxq29NgaJTSXLmaGPJwIsIpaseWoIxpgBhspwkweIdWkTu4c4o9pGOa9CLyRULmWVMphAD-t6cyObsslO0t9FE-VUKosc9tYuCD_ELsvTsRLC6xmSM-izBOm3-n4ipuqGbiNNMMrZ4b2YvMpA1_TYCrEXJnxTxqi9LfdDFKfKhErxA14n0zthmEaOOGZopybv6kJqhAYdMqn3_OvZvTK1f3hjdr9O9-5VPsYwP5uGELzetrrROlE2A2Le-8iWACNvgIU5g3VQRCQp9HwB47kj3jZvCQx_2mrFJWIPd8JWIY4m_x1OgwGlXeC5OYaszFiUoaQTXLHRi_j2JPp3prRKfQfpqrpLzs-Xbs0Ff91e2bUuGVHvTI-aAOHYkKgGLHhZgyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=Ehsmzm1mPP0LvyzLRLmmxxwTGRi1yR4FQwmJ2TCwW5MKO6ENciaIU_t7OTAwd_AcWrHb8GKJPFS_Xf1sAZybC2JSfoY9Hn2xCcf-eU7dHkD9WbqngKv5IzYIw3qiX4pdXkMvBFQUmxuPsE0hwepcc77144PuwSzoDGW1xfXSUb-utVazBCwzZVAIm5NheiA6SGJS8feAJAHxwe2-jYWQs8JqIwMqUXCqpIph3LVu62IFknqmbSTm1fDl8FJSZNZzbJfGrqsNTh28m5QCnXWLUL2s_CgBLq65uJ9mPH0nxq29NgaJTSXLmaGPJwIsIpaseWoIxpgBhspwkweIdWkTu4c4o9pGOa9CLyRULmWVMphAD-t6cyObsslO0t9FE-VUKosc9tYuCD_ELsvTsRLC6xmSM-izBOm3-n4ipuqGbiNNMMrZ4b2YvMpA1_TYCrEXJnxTxqi9LfdDFKfKhErxA14n0zthmEaOOGZopybv6kJqhAYdMqn3_OvZvTK1f3hjdr9O9-5VPsYwP5uGELzetrrROlE2A2Le-8iWACNvgIU5g3VQRCQp9HwB47kj3jZvCQx_2mrFJWIPd8JWIY4m_x1OgwGlXeC5OYaszFiUoaQTXLHRi_j2JPp3prRKfQfpqrpLzs-Xbs0Ff91e2bUuGVHvTI-aAOHYkKgGLHhZgyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STQx9iYVwzcYnWmTTZQmeTbkCgUGspCR5HSgs7eosz9Wzl4xaL5nsvog-5CR8P3U1uvTe6fvuUSGYVDU7ZgLvtUaji8Mkv4pGF13X22nZPOUn5MULSUMgS-FtYVDAuSDCYUGuwRLANzyUDqe9ZuRT_frcTjFGUyhZWrBVTT8RAsTV6zlFBxj88hxuvVAQXnC_cULSDnNvxdX1bFo3_-qPqsVZcKqdzCV2-tKZa1zaeA0vSsfbBFZJxdhHM8MWkbaYb9nVvf-CNR8UzVGO3hAJiceNfM9TDSdxVdd_Le901g9FzAIy5AXQhrAiTXLFAbjPW2A-qBDe6pSSnrsgL953w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=pX3WhsEXJZMjkwbASzlKVjp1Xg3KbB9CWuV3xKiBrhaHLZxNgz3MJ1WDkglTtC-ha7_FCWNhSuYHvdk9rzrUWDB80Xeies_k4Ucz49iWaxh83S4tfLz-YFhk45o8j8ze--UNOYLvVCyqEifbux_cDBqxJlWC_VFhEy7ZMAUi3H_vhS_6g9L1D1VqRcsCX0bs57DSxwt299uOOpjSq7p7wXoJG37nEDRpyKq8fWapivzIQ-XveTysSEUGwmThrFLYrWBjjxxPnYRofQeUSvIr3iyYFwqPbyY_4k62CXs7ZIwxbX0rgqpF2UQLouiNxczhjDqHl0Wv75NMYtLf-3IVNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=pX3WhsEXJZMjkwbASzlKVjp1Xg3KbB9CWuV3xKiBrhaHLZxNgz3MJ1WDkglTtC-ha7_FCWNhSuYHvdk9rzrUWDB80Xeies_k4Ucz49iWaxh83S4tfLz-YFhk45o8j8ze--UNOYLvVCyqEifbux_cDBqxJlWC_VFhEy7ZMAUi3H_vhS_6g9L1D1VqRcsCX0bs57DSxwt299uOOpjSq7p7wXoJG37nEDRpyKq8fWapivzIQ-XveTysSEUGwmThrFLYrWBjjxxPnYRofQeUSvIr3iyYFwqPbyY_4k62CXs7ZIwxbX0rgqpF2UQLouiNxczhjDqHl0Wv75NMYtLf-3IVNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMO1p3wc53oHOorDXO2Dznry9Pxp1bOrKLSF_2Ru21uwSkqc8BL0rnhiotNhRifmW9Zq1YTIQt_0EWaxv371uDQ2U6qR9dH5cWorkZpdPl0wemABvcICqT6KPuzzzCW0_pmzY5W7cPUyxhuV16cnCUlbtfuxWs2TNctxwNp5MKW-UcA6IPYE0qq6LMLnR7vSuqr8lsm5w1y_Uo97dtW3H7nDdCJaF7SXzSUiBPHjv61EHMjNLPx0xTpsARD5EVl1hHl26HCU6lts2_ujSMgXYB2yiaHLFyWYQg0uK5PeshIHLwI-nifQjsXAZqg_OIiGyEYrMwBXTGy0OhDVm0aD8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhiWasJY9jNIdWCljh8wGy5m-3fhRP6PeRLQH4EO6zaouyGdtA_fAQMpiU9Znwu6pA_d1SicQCylNL7_-txf2yHm2X8mdhoqbFyN1-jAHPRZN0k_x_m7y-kd-KWUGSWvdrPOWl-f7-sqydPCUZZTJXASi2OWW7GpT8Qd3CYy8T3nH3Rr2ZzHbY35p6tpSN2EiTRH79X3ms_lYx5WhW2HH-7c6fRolAFE5LPjoPUt112l6UyQf5cUFu7dgd0cHBogkD_BruRbGm0EHtm1NgE3qGIzJ4AJ6yBqahmjypNjU6PRM2c1xJU_rUfa1X7ms2tbo4gI9f-UMl-8Nf7wiVJ2Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c-JVkJQeVNJl9EFJMykHiCwKNBZ-P_XVZN-XycXVKLAATRAeMe5V7mHlUv3yBzII0EgdKV0UTuzDV-lrJKsA8VIXA_GaVxi8wjgBdYqcBUNUlkRbXuCfNS8fdtXTCRIKWa1rMMbRTMrqDoLh3lkj8QEvVK71VtSGVFCNC3-o-jIkmkTtFKvY525xuDTvB-7F6PFGfRLTid9U0sfV5p4OMG-1fgAC57MPpQv_x0zYp5NiFiozQQoF5TwvC0Ygfsm_whfsO_vxl50hqXlHY9W0wvPGUULqy9PUm5prO8946LiIqdA7TQUD8R-f4IRgVaNhbtTOziWIUAfSX2iDKp9YkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RaIg-6-DwAvoOYRbwZfESPZF8cABhaKxouPjsRhiUVIjNVFAWkdJgiYO0KNyoEzESpHLFm8dcxAjw3ogZldK9bpNl5Mh6-JK4t8srjWEjTaIdNkABtqBWYXlVpxetdEDdkXMWJy1duNyRD8c7gf2GipbWbZA12nmgKevNXITcKXepPv6tjVY71pNbkZyLWQrp_zkYk5aD_8ZhLJwbr48PdEo-2fUO6otEaUxcbON_c1PYHkmsgMQI7Czt1FwASMDI-f7-AlHuS38XejOqfmuxM2S0WJfCwbwXp3hT1BgvUii6BfuXXP2iDhVS5tjOu8wAk6PQSM2veVB_WQE3s_RoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SjYQDk2rylyEFl0JdRsX4HwTtM6rdcdmNKtYEL2ozbK-p0NuVMIASRDPh61-YlnaLOPbvr6Ewe99c4-AZsFaM61eTN9TY5_IExnCoP2INya1oyW2cRx_rst0kNAygcGoGMtlaYtvVu7TWd5PM3VTONdMrrLfkMEAy_ejPBiIWfrk5AjAup4e7COC-Z4hrjzgD6CL74h9xqD2ysOJ4EXBL58FixUegBLHEdVyksYauZtXXne79jN2T480br1VqnarkVd2CktnFOcUJoqThSvLG1m9D9YSIuN0MnFdbpysUgdxVG03_cTZMkD_HHjcKhTbbs6VQuHM8altDdFbcuh7NA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjI2f9bRS2bVhz44Cbh5xlbUTjxcPWQs1BOlOuIT0yIczSYSSdKtVfygMgEqP1J8jH-GwHVidbyyVYfXdtFZ-sdBResOB4-2YDKnL_NkGD96dwYnfD4n2UrkNAwmuze_etrYEIrUoOHwFq09us9kNDHETEs31VGoWj_reHRwS6YUHYbiKIHjmLNDQ6CJTO4wJdJw5QBGjYzCcgPcBp3BPO4OdUQjnt9x3xwKRacrbkVCucfyE0sHgoeNCTd0w_014bzBdeSmPJqAoovyoove6EIYl7nELIHOq2UDDgObuzKccLj5WwNrzb8_C-VA-VHJEY6IQcDqaFMWlZ6lc2K9Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDzxuoiVMHlWtv6Utwf8o8jTMIb0J7SUlxdm0Tycx6G13bu0-THyYp5KaEDe3vQe_yQsbKmVQEKHWO0l7igi0a4LkQTrs1hdAMKuIcvU0claD-wA4i80eX9Nq26ozx7eKHKqhePgP94DeDQafaQNPC8HVKPlZlVT4KyJU4SGWzOihy7GaUzbtEh3JpzD77O1wHVFdW1Qx8s9wUVHBafAlqM7apK4_A1969fDb9XXpwMpo6VlX4sPDnyEnwothrp2UbF9PSorJypP4txZMYUojzMjDhLPwEwkUg_CzcdstbXT_JwY67Q8AU_KwrNGV96MPPDhUXSHZdvNFtnzVyj_SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uA_GRUpFgx7VUemtHQOZ2WUJ5ru-13TrtF83HuGRgFQ9SFRMATb3VenuAZjt5S5ZUl7KrBrYT1QsqG9BJWLA11XNecddLH5UTXcDNxgTH8IbHBC6saSZ_FSjnXNynYgMTwIc16KTnSYBsSbnDGa8dFWfa9vbttuYomEucf0THteYeILUIwNoMcuXajJJwGtMwVkycjf_JcWAYclqmjHz-pz-6UoeLxQ5u0aiKkXHs9y9IKQfUn-7MVuFv-lHihzQqq8GPUnlp6lIE-BAq83J_y9_WCsj96lr2o5vm2IcwVxe9FexiOdF6obNuNetc2DX8rSdfoDhECRj_jKMXMtu9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z--_w9yTYnZ1BcNCf3F889o6FRKzsOzjZiV1q-NnKVOnb1Ltqs9NdOPFtiesttc6fnl2Z3m0TG00jbp0RlFRoj0GIQ4xh3Kf29jzaNJrOnLK0037htlUH5-j_jSS5opliXgMCn-5k7K8U3pMtZ8wZgki4J8jz4Dk-IoFlAPOWTBl1wNdA1sjRMeMa7LjKpecq0kSRlrOXjBi0olczTkZEegiznyDOvUDbraeHcdz4uQ-4YmWFNPjr3EOwyoqayw55YbBwnsmEQcg8gzLZIWSY3Uj20NTngu5l9S_rt2vxhIaXvHI26wUbdALEMqyRlj5Lg6Nu6tnFxV9p3yrn9PBbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vHCe6k1aUckAYidmHX_wkomhAJ2slckx6gITVpRu5daMf1KlYvU2odzQWPRFi7OJRjWoYmd-a6C3c5uTiEkiahz2XrI90fGWJ6EWKnX2CJ8juSfFsOvp1V8K3QDarom6dfMuLgTWjdyoidJQNPXn3gwQa04BzCwbdd2e3ct44YJSick9TlR97HbDCFM_oigHkprs6V-SoD0e_rPbCnqx-IdT3FRBPRxIITqDGNbQmBzK1m0oc170-gk4vuUuCkphtKK_3XSw9XTtnu_muadUa8xfkjXUnjdgLNA1Cj_hJts1gnl7huPGPRKPs36cweiRNLbMBPhzKHVmak_DIw-yrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sopyA3haA3yA4BYcacPit2nzWVYLJOyzrbo1c5DhIzR_4GPM1aW2ppg7ot7gStQaZhMzJDtnklbBcqptPt-u-mN6LvqUbkIq1rMnKW8RreUl50IZKc0pRu-HDzAQBXQtMbq4Hsuy2cUtk4BYoCx8kFKRIXUQjHJVdIThDHUVbhhFnI-RWcCtB3znMksVDdudZWCFzOoYFCX076Z4Z1USuBCkynxhNvdLMW4x4zIoBiEUV459R_bY7g3D9qDm4KdGISIRHObv0DoNQKQEIkn6krUwzVv9w1zyxsWnSXXu1JWPQDpduvpxvt13BoAvPjEi_ZkhYmbtQ6IUZmawNP7x5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtLzaLCynj-4Y3LvWnYY9mwV_x0tPTMMvpAaSOq0VEPiww-fNA8uja0Qw7rjPr9-_t4rrH6pm3DPMCXtXT3Sz_A-JvpogDwHCLknH8sqRPTD27V3Q6UuB5GilVkNhtTXsMoMd7teDpdYbjoexax392lf-GSxzJiq7KQYk4mVrw2NFTV69T7SrNTNB8AsjMLhxbjwrJ3BsZKr3jVQy_v-YUTCuQLsaJdFe31ceQUKIJk7HzQ4_MUbevsL2iyU5Mpz6UQ4O98xmtEieSTOhQU4g-qaTkme0jMkYtDRtI77RBr3e7eg44IBXWH3ChmaHWPHitQ27iOc-Beyam-ee94DMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AFLzAXK3edOUV6lw_bavISUYhzw36qCCIKsTG0m5Psk3G26M27wbkWN2rL9RpkvJ-Owog5QmbOoAwuX-H4GcLHWWBjkULKiCThknP_5Kl8pJVOhNUoDdWqyCXnGFuz624lqxOm4H4yNGZ-FPWDeykU7WMSUoViuWs8tf35nrLHnam-8xnnpYdwfQPoWQ9GGuf9g5TMfcvw4uFDDhT5io9IhzxcJr9zM53-3I-RWUWhOZok-tzOk7OYC0KsPdJq7Wxl48SFA2KAOPDejln0B6K46dum9nuAMbp4jpZqcD9lN13En85XWFpq8z0-2IdzUyUF-JTnp_LRg4cr2I9R3XTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D09UPguHFc_RMcpvUdaQRxJkvcNRlfuU_lWIUpxYJ6OwVNIy4tSXcZKMJfJg9R0G1Z-d0NsxUMssQjcSKKSjRKdv8STUGktD49el13EmSHHsc1nl37Z_VJfcAqxZnfQzHNwHGoTkJNLxkgVSlae3GIQi_VU4wcIsTa4DDHxPW7RvltvvQdKie7xqfD9t6FwFHyg7LEuatBzk6Lqrt4eeq7QX8QmM5wmWwsBbZg7MbLuQacoxEt-0gjNQPlbFwOFFQPkfMC17N5ysVWfYBolclg7vPVRBC7M9GwhD_aT0ODf9SBvOacA5LSPq4n4cyTUeenbsoh-03UKPtqZ1bpnGyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UL2LsMsgS6W11mTiA9uVAPsRfN2B55GGqAURQz8xelf8RhkQjo4A3UUDVEbCH3R7CJ5Y4upFVXx3-N9CRwC0YUTAn5h_8JE7nCa7Wgu_cyU7DS7a6ySNyQ78Ve4PL2i0ECbvZbcSWXY6eH5gF79OKxuigtskXAOTVFAY3TMd7qu0x92YWgSY1HX-6NQ-iLPzGhWaM2eDCSInSKBTP43_gUGgELaMMt3oGF2_LDs9vqRn3v7ZJmpo9Cmr8tFPO2xCLTMErIosm-z3J_l7xXn-Qbi4Uxj74AVoNSllT6GoozjB-knEFNNfesY39jQlx9fCKDnAY7mnC1suYTyEUkPHeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LKUC8NdJYktk_7gu7dvgN8ZhZAo0ZpP6U0T3m1r5hBTEoxWFMdARATMbsKKBPBhHZPHEabPlRU4FNbcoF-PQCRwXdlnSe8Qj2UA5En2nH_voDILT_YqvKwoBHQbCP78NjnXN5e9Wm2xb2p8AYAnSIdAGy6j3qGGC-rIcWXwb2Y3nVBYz3XI0h9AoNpii6SZ2-vOuuHBcFAwpHe10y67IZ4bE1B6TW3hfeFaX5PnGLS6m0vuIUAT-N8JHAO_QowaiTUbIhaFSTEsmNPH5obn-mYMBMA1-SPD6c-8wnfYS58qrdP24DPFXzeNhgVqt5EWW5hXcEVG12XyvC5GODhybCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRcC2kero2rTkp4i00qXrS7Bxt9DX-aeni7DGXTtmy9OWKDjBI7Jt0SDxx-CdxtUlKsqNNoLaHvEovE80jzO8TPIbPZvbB4hlAs-NogN8Fp8yV5A-iT-EFqS1G4-Lr4o2CEMR6pGwacDVF0zlczGpQNyFOjuJ_iB2juULCXTWUS_m_r_PrJA0Ej4-om2D3KJKt7_t-HsBgjFfxJli0UUhBNHWHv96HWnyIyNkVKmPVj2i0Eqo06TyCaPS6rlOEOGCjFhaubmtjGEsBCLUSfiyLE7p8FV6RriXDRkTzLCj2A-dr_EDZEbOtCGEW7Cfr1MhhrcBDLcWwuBvOMPDfUGDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=nugVNG8i77fFuNAPfeKoy25zrUUuwSbGk2_hnDwf0O7nEoCOj2zSUK090nifMRYhzTIa7oNTYKYM5rjr6T24mrG3ljdAsxDpK8oNXmEWr2BmUOOzTvHkGT8-eb13ljZRyvxJEZTZz05YPsJdRj8J5ZJKIgEAhpE3R2CMTgXbCkWXNfAV7tdYMozzBYV6IAHxULjJvDvKl65LWt77_nlc1sNu_35SJQbSObwRuYhYSuhyvhPcTw9UzqtiF-pt7D97KnoFlCXabeDhq3Y1GdSOokpOZQn8c8ovBKS_alE3LDquu725QVUCD__-BEvm2Z9Tlx9xXBGVIxWCWf4ba2BpzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=nugVNG8i77fFuNAPfeKoy25zrUUuwSbGk2_hnDwf0O7nEoCOj2zSUK090nifMRYhzTIa7oNTYKYM5rjr6T24mrG3ljdAsxDpK8oNXmEWr2BmUOOzTvHkGT8-eb13ljZRyvxJEZTZz05YPsJdRj8J5ZJKIgEAhpE3R2CMTgXbCkWXNfAV7tdYMozzBYV6IAHxULjJvDvKl65LWt77_nlc1sNu_35SJQbSObwRuYhYSuhyvhPcTw9UzqtiF-pt7D97KnoFlCXabeDhq3Y1GdSOokpOZQn8c8ovBKS_alE3LDquu725QVUCD__-BEvm2Z9Tlx9xXBGVIxWCWf4ba2BpzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGSX8Zxqzy4cIL34dRiFz-JBm-e_tysQb0GWkcI3BuElI-uI-5CapciInVVNwYqCovGrhZKOcmFv3KBrj_28-5ogmZ7jwAQSSev0WQEqwnwi4DFkw7huAqnEci0EnOvTdab3pEL_MCcPWJslyPFvwQUo1tC2Kn_GMb7NBNn1wrgr8mxZHEDWRXji9YiKJHX_3-tsDB_ILF4Y7oIXMzLavlo-R3tCzNAWKBsVv0dWagvDAUIxMzOVT_uVTEhKGPsWttQSpfl1eh5X8vygCmlVkLs26_27m7boENEhqu3ZVRz801oYmesFDzpoY4p8p3DhRTi6LmK8qhnwYBOqQZ57ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWLo9Md6_h0pO-glYF31jvJA4SpTylhYxd-EK0zMnb043cuuMWchtiqqhW37JS6DDLSBdjj0IjXvkYTbeoO7XWc04q40h86W8eOJYlmruocFouDxo_3otgci-hfaszGeRKI3jbfpnup14M5NNJoe4tRotPmz9O5m61YjiUwQMnS2xFjnOIck5sLXJN_Qp4SZ8GJRBKAgtRjJCXtS-RzDlsuv4zJA1UeUyqNoptwsENACNTb8DoxhfaXfuwOQi5icmcj8_P8dFDB6qIGqlE6MyaBI5Wd1GPtqtEgGbYpfoaBpkbFS5RvZV32HaAo0V8ickSd-QihtB2J-jw0bovsoWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpRJNIwD9sK7vtmYzTKMyt-7MR4g7SsoFhO7pkOmmWA4e_3su3Y0DrBpBYfUWyUywdtotH4RonsCHyzO-WnZHRWasz4hYXev9q4GidjAb4yJTMSCUC4hKseiR0pSRr6uleOlgOLU7_vCRl8FHyXqSFZNy_tGuAd_Sz8aJLxWVqnfussA2t1ChSdOyC-47PbJAxLze1pyX_nWZwFnZM4resVhVGug7VCz7bN4ZbFY4DdKfvss3LhBN1FKG-5ONuJziAgtt9M8jd8YkJWx9GSWzx_0-RYaQkDrMPc3zSSf3ToGgwHhgtGlhHLof4l7Xh2FArbYb6kdm_yuJLoeXaZzEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
