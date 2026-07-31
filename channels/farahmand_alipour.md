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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 23:44:28</div>
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
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjOPiJkM5-EEDM6Bj7OV6FYwa6uuVXOBiL-mXDklkcvICj9qBgt2UZtADLR8kiyyeOHfyQcn0FfLZdo9ahC6WTCE0Gy3eF6J_AGRCc6jpnP73GoufsqCZZNizMdGkZTUO49khBUxM4Y6TBU2vIOrdghJElvyZEl5IEKOaMh7yuWN69SA0jg0l0idBUPSC9aBI8wPpcNuXekSRjEz7Jvd8TkQdToAqfOjoCcsa8Qgze6YuKR176p9Qk2dAQHVGpE4zzljhITcIpBkHsGB0OiIhUdx0VZqTRhxzBzphO0T1rgW6byolugK1p47bRTt68SFGrPMKK28I-AJjm0aM8p2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjIQTM80iQK69zWeK1zv2hRR6NfL3wncov7BnLo3ze6n_keZzpyBK1vl5c4KapxAjE3O0y6vVlg8WgIA2uFu9ji5D8zywqX9ho0Kqvr_2fcYIHssdNypK6zYLRgiyV7lmBr5XMuduQIcUo85FnSXHKTF21c5j51idawfac2Bw0DCD44sZJZghFvZwzJqcrlEZlB_LW6QE5nHkDmtkH6fA2YqMQG5HTtD6v8ISDpmyT9QyyxsXk4wN47Lc-AqMHkeTwWzW9uARkCB7smN3iFsM1nEqy4MCf1aMQk7sSZ1R7i_DyDjHRlIHDFXBPsmRuiUmnO9GAaYzkOS1EObA5m8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5SNeWkjycX6gsJJwtvo20Mpl26SZZjX19Gi5my1d3P89yGGHjNGX5Nb7B9HX3xHy1hSjl1LHA2YguAot4MmdK9Iqc2jXoJdEQJuGH_hl_a6SzgMO_5Q2_Q4ueCYlF9SWiYxniCXq7mimIN5jvMhQL8V-LgiZPrRMmFrwC7D8xQOkAVJ_jbDkFDgbJGLV3-I9-I58jLC6-5e9E65UTRvfMOvsufXjtX96ST-BYDKr1xk33PWoaF0-KoIJbmhf3vHtfYb8KpmjX4H60z4_JGadulFYnxuXRxALiwZYDfx2YkROe3M9MjCs44ByzEDodPV_Qn10wxXaVt0y3ID6TVyfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0dbeuUShWM30A_kcihgPofaUCtPNvenAZqq6Y6HkEQ0PEo-xt4qg281D3PmxKVo0S6c3h5XGhG8roFn54Osm0dfLCMx1fNM_hRpo24dJrmZdIImiAVEEGl2n1Asn5OaWQtL_Rx9fHVJ62o0Ml6hs2t0NcQ9RKKXIvTPQb0bWDzKZrxFtDLuS32HRey8R35BESCXF8ZoIJfE22sRsn0N0te6LMPVJ3KwEZUFjyPtTkcI0P0XQiZwGOt24oXXc8qmz5oRQy2tH3uLEON-I7dvVbMOtYa3HajQA_2JT-widb9tMdfT_g11s9psXz7OkHnf30w6WOZur8mdeCB97sDhYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0zeHLwcL_94UpOnVwHJeR-SjOVAwRNEQoorPnaFWQ1ohNkbzQK4p3iiQl9uEkdgpLe2LnBgv3grpS7bFiErOV3cDg5J7skPJ1Ki4uwUSIpNXd-N78Xy5XMWlb_a8QerRDqBcjhthQRFwffUFxCic89OYyk1zoGFsIXSMCqWdSsN0Z3LWgw5PWsPkrPTiFta-EksSqP8n5_uEJdZHT4kK57drrgogCbn0DMDAxQDxKE7wC3cItTpLv_N1J_jjecwzBtAtuuv3oxcuQ9rcVjp2y0oUeZUXqr88NGUkO_6atSFzTMtaiZB_ti_i1XeA0NO4YNHIzjrFR4kBNQDHyh7Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5P76CyG4bVOYZoppovkF2x3KEB2a0Bm8ajKs3D4u0xTvsXMf4OYFfV8M49NvXT8IRKwANSh1ScxXHMGskLkujk2SYWBPtDpjAl46UvK4S6OGqAkva3ZEpS3CXjeC-0eeRqDuptKGmQMtplBiRMhwiQsMFKcUs2x2HNZDlMo9_W_qMjhKWuJuhLkms754rUBXzBsSDUNadQsSWxxtfC8x9dERl6p_eYSw6Z-mLIfXVrJkUEMp6j2RQzJjf28ojuskHK9vYH9r_WP4hQByAe_OxxpXnf1Se9jyYLQpR4bRv3un-h9NdgIAi28xGbzwzlkITL6IGlMWozSljuzOyEVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbjCfFse6t1YbjGml3SlfdHI1-j75JHeGDhn4CS_Sz-Rd--b5MZznij5rB4fQ4rEKfwImdBEWA-mRXcsH0yGj4aSfxDjXKmsln8BTxFIyRyf27zQwZMl5Phoen1u2BSs-VNlElHQzEHHRLuJqzEbHgJFBpglCiSpdMe3gbomE3CGpb1yXPwMsydJY8PR4jOBjywxPBDamF1tyPmULlV3w2BgKY54m-6EcAgSpIZ2NnxkQHMUws0yY5A-jGdlu1A3uzjBtvABiqALg-v8C9G-MZ_Sn4QaMV6CaiaelQ_J-JpPbTah2xg8Bp7h8loPSGRqbuEO7jK6KHPygUymChN3bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzplK5f28XodfOAsA_ylJJdCBmjAquuDUzgZRrmVfnV5Vbiqm5740GHpPvCeldx4-H8VDSB-v9Wnr9mJqTq_dFRSicj7NDftDcIk82bat5cVa2izNg-n6nCvx8To8vf8febN4l4S_0UuBGvoCVZYgmpnOxZxKA_mq4y9kPjVem-ocqXX5caeQcSJmLx_5wm16Al-_lOIMKqR_CAxw98igC6XzwPXiI_nkoSG6AOHPT7SpXaghYpt5ck67skuRMlvhbfBearnwPWsXXLfR_m8T7ZkCSpoCKvYbGhwP79KNRgTOQDlKfysb6xGo4GOusl9JuNKTt0dG9WAHM68m5ip3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSPvh9-sCRcjjAOAYl8vG7DvQEYc57RLwIwKaaFr1wXZmmqJWQy4QXNr4RRmVPX5znGi-9HBFkQ7uJUpMeDe5dI3AanvQL8GXqdAHm07GFV52BcduWvnhWj6Rf27PBh-mlJaIFPsz4_PoGlWvEoW04cOQOHP7Kp7hwqAigd3uMGEaOupp1SPPyCoxIswTYDxJOG2GNFipRg9C13-mkATA17jr0A_ymHw7Ifpl7wMCfkQMVltUO7R9MgaKfVzDEJw8BMUBMiqTlMs86c097qloeQWK0g94DcGLhW6_9_6pEdYrggpmwjbOjvCElDITuH8LvyefVT3L16B6eNHMvKMAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBw2WkkAo4b42MT0RjvgoKJgGk3GJEGi5GwCwG9gCedBvcCN1VT-5soDxBIqfRyNW4xinSVZUtJGuQZVyx-Q6TjpKRRaTVS62Uc0L3c4DHpggZQjmLdoMHP4q_JhjC5PLSQ2KrdCv8iZ__SC2PquMI7ye3a4BhZz_LU15bY_Y_5zjcqVFRTZniEYylhm-pcwWVbVjnn_74nZgJ1fuL3jEACPYWyhXNvXJDBDyVVNEPsmMKSsZbSREu5KIKPUp4cWmu8WcZQbEqkn8hd131TOkvrJoSu_H8_KtxjFEYEvOjsejOEQEkPcDSQxy1Sd7RENX5uuUrXbUBsDKG9RUOSNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPGgi5ZjgFc6Uw59Dt5YtpEt_KYf139gk8pyemhyIofH6YRE-nZl9MjZnGX2fzKdgVZIYAhVTaixHBu-GLt8ntcLm4qQHqOXn-6KO08c7i-N9w-NcCzHMoUeZLK8V6Jj-KadoVDbNS1r_saSkqKGTGawK3MnSakppYBH7Et9XM2TPY773B_C5juq8-aJbD9Qf-iIjMwL-RWzAJ2FA9x___Cvo-ofG0yWekPioW5fHMVf333rqcFW7jGqSh0gvyKSastCbhQLCqtFCKVCCd67-rb7ZXwojTbupeZxMgN07jTMWiZt7En9hPfoslDGA-V6IoD9MOZqsBLfKSHaSihR9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfomKTJEvJ5IQy1B_uN6_3DK_AeidEDu_BkjTK-Kxu3kradNVlWEq7Px2oxAO_nsLZR_WEucpSctqux_A120VXTe_xd1OQ02C9GLa-WjQqS6p99IUNkwm4vrxM6n5aYKgF_n6orRVzEF0DNuGNlgjEVeIinSTmrVSaMEA_r7zIZ7MPv6jXRGSlgDDqK9FXxqjShM5xqYDd5cgPJtSFNl-npAE1Q767IGxDKCQwwflUn4xdr2E3Voui9wwi1WvwMVcGrv3ZK0zCL_r5giLSlORDLMowwozELE6mW2Bdt-WgtmGTnaJwzjZU1zUgXfyIGyJnX3tmMhy0CK2PtKnv7OTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=Jl3X-Al7GJc5Vfw_38gegbT2wLP23EQz3s1s4ApipqYWw-1HP9F8Ep6wHydzuXIGXuQYw5kIn4iJ1TW7jdK64te65J2m0CzZE7hdItMCeXPTLsdojRWOnso54dssdr6aGVZiO2NRNVz8aFn6o2sjvNzkDLX4oCiekuL3sCk68n5pccecfH-Bz07MkoEH3GTH4F7JwSXsXRmX33uxV2m_8Je2v3RRwCDM49yr_338yeQoPcgoyy7ZwspeKN38Sp0SNCSSVr8LQ8etp94Qm0eRevwjjoWYvO80v9EgnaP1eovwfIxb2pWVe_1hqdqc5PHO_lXQj4CUXXo3eJWJp7nA4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=Jl3X-Al7GJc5Vfw_38gegbT2wLP23EQz3s1s4ApipqYWw-1HP9F8Ep6wHydzuXIGXuQYw5kIn4iJ1TW7jdK64te65J2m0CzZE7hdItMCeXPTLsdojRWOnso54dssdr6aGVZiO2NRNVz8aFn6o2sjvNzkDLX4oCiekuL3sCk68n5pccecfH-Bz07MkoEH3GTH4F7JwSXsXRmX33uxV2m_8Je2v3RRwCDM49yr_338yeQoPcgoyy7ZwspeKN38Sp0SNCSSVr8LQ8etp94Qm0eRevwjjoWYvO80v9EgnaP1eovwfIxb2pWVe_1hqdqc5PHO_lXQj4CUXXo3eJWJp7nA4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0J3akIBP-pOFGf6ThYZUBFz4EYDZOy9p496s1dJLfOxIhTBGoTKM-_E-G6PzOlZbxLV5pdaJwxDbOF4ObAJJuY6Ibi78dFR5FZAU0KOjCIOKRQQa0gn76mOsKEp0Pd7gfR-eugEisVVjwCJ_W1Db1RuP-tBcWT943Qtt_3RBPK7MOUiILwCwpBB3-Q4E5WzMOWmdnllJtfHdsj1ipOcUliF4fIdHCXc2sPqUxxkU_x3IHlFoKzW5WyEjMY0ZWmEStbOpEsmotQAWI1ebtH09yrKTAjmhJ1gYQO6-FCypMPT5CgkF6QrT-C2KydN47XSm4QdTMkxysxG29V8m2PSIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nfh9pybUNKvwwc_lxjWw5Bi0YUwhCYpPusHoz8Ph57emgFPUbknOKK0lGMTk3RBW7cR1XdprLYuwJGot15w2BDnU8qlYBmRwIFpZ1DoKtc4-a_8ejQKRtb5bTIbxubdNdB3FGvDFf4FxCgY1JXwZz-T26uVKcylvbp5BXkJ7ixUudHKvs7aPFSRyUMVG5cQS5raOw8f3KxtIH2lqqHQ8BX2JriDWxve0ylV9_snP4HJYqmJNUqHpM_Cy4TD9ZXNqjtnrtCDdFeOErzA4za17ULIBGx5YtVUsV1ILZmQEEbYLrBq92D23F1jJZ8M0J4_wgLLrEJVS05LTEeDOOeYZlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRedu-4rSaYBtAruP0AwqFFkAkeOKrnsbF7mttAqXTSAYkKLL3xoX7VlAG150GKi3HOPrYejmKch43IMUOAYw_UN_q-CuITkPWjLT1LkwT1SDzJeJm8Y5T0l9F4h6mKin8fAZuILRRc2Nk-NUAGKdJqibG5GkOFnF1pVow3JfaXw7S-9-wRQYCUeAD1TMFs2VSZs6PqaO0pk9YyWL1LkztIwiTt6A_6iifWwgkdz_8iCNpeOowrU6wsgQh6SD7lVQEzL4ScF4JFJ1G68xrsHHUmrvJvWuMnOknz2ykRfnO_O4_rz71cC0tFZllAENZ0avJT-05RGO4sma-66I4YxOA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLYK63n90dmYK3c_GGS_AFrMId7kxCs_z3-UA5YQG5rCtVtWMOzfgrPD4BpGtu3IpOVWiFIoffAC3dNPc5Pdj6ItJ1clpgAbJL2KbUkApZtgNw1ERzfORpbsb1W4ei6x8DBBv5vqXF2BtUiQ4nW82QYFbiEES1w-BwwcmFHl6sD3GGSZ_epqByspCx_RJ-gLY8t59fRdQtNGRwRQupWponjl_WbKh51FlCERgytJvCtVHN01wyV0npsq-lUPpeP6t7QpLRjVSvaMqj6hlYDPL8yhjEq6VrWhDBDtSHR72xdln3-wbJFY0qN_-Cujt5utSNx2nyjXqpTpewZKgf45cDDs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLYK63n90dmYK3c_GGS_AFrMId7kxCs_z3-UA5YQG5rCtVtWMOzfgrPD4BpGtu3IpOVWiFIoffAC3dNPc5Pdj6ItJ1clpgAbJL2KbUkApZtgNw1ERzfORpbsb1W4ei6x8DBBv5vqXF2BtUiQ4nW82QYFbiEES1w-BwwcmFHl6sD3GGSZ_epqByspCx_RJ-gLY8t59fRdQtNGRwRQupWponjl_WbKh51FlCERgytJvCtVHN01wyV0npsq-lUPpeP6t7QpLRjVSvaMqj6hlYDPL8yhjEq6VrWhDBDtSHR72xdln3-wbJFY0qN_-Cujt5utSNx2nyjXqpTpewZKgf45cDDs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MA-iZ86bjQ3xjYPI6EjuF5HoZlzd3O98Jhy0NPq9MhaRBfA3ijPx9FfxRftfP9zdMyd0k0v7xj_pyOuj7CySC2AbEy4bMa5Uy5x6SYxsJD4ARs9y8XmcIlAfo4kSzn15GYzQ7lncUvyH810H7fDOfSP8lKfG7r4AQiHG7XINIyhWbZ326su0vbM8AS9t6iUr2t8dXfld1XWY9K6Nqi4P428ljvj8lFb5xHpYoxnttZKGsnd7Xml6wMjJq8P9FRhDp5eaNco2aqcGERdbP8IQ4iJtzwzoq9AxdaduYhD2KZ5EoTHuCF2Fdyn6Hnu5Rt9L678N8b9_EBuAjyp9OLeM0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YnrC-5lYvwzr5lzxeHXyoA5wRsHL_d-DwpCpfeOPCMcf1-2qUgTNByV8zz4Tv6DScDzEOEcwjmOkZXyYlSfqL_6aRKxB7tA9F0rP48Ex7Kamf9eqkGxzfNv9_ya3lRQ-4xaVDMy63S7ebQVs9LwHgk7T0ttChG7Vsd4KKgABX_iVyHO4hWl9tsAd8a9Bj42zS2Mr8fkgcr2kGdoH6Z5zkQSZ-h4VEvEjHAkpQMKHTd5rb01UCV_hY3zwJ6wNpO6vtLX7GjMeGOdYoPs4EgNN9dO084AZX7Eazl7lf-xr3THycqaZOFLlDXNuTkHgfPUlP20cJQKCOGFhkkQE4XuCcw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=Je1QjDvNAiP2zGk-WIh1VBKi8_SI4Llb_h9sr7dI-kWrZ4YrS-0SK9ehuHNEUo79OCqvDBvVb3lanfQgFKequSm3eCxsz2yTko88rABjVzrS5oeBKxdssMwIA5-nqQtTBdlzDkZLnoV8JjDDq2A8eeHEr-2GtZIY_O2oBiA1mpvUxixkL0Nq6KqHySMvsDRegR1hhbHVgHaWBPzU4eBoVjafN-Mjt_3jP6plRu0YB7LWCMBkcoQuGwULxA5abKikeWLQgIhxKesM5iAHNK6Tqc5rzU0WYQA-WI8EDeDCDHrCxQhIOmFO2KwNHzIBwL8-C5MocoF-FAnZ3Egq-Tsx6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=Je1QjDvNAiP2zGk-WIh1VBKi8_SI4Llb_h9sr7dI-kWrZ4YrS-0SK9ehuHNEUo79OCqvDBvVb3lanfQgFKequSm3eCxsz2yTko88rABjVzrS5oeBKxdssMwIA5-nqQtTBdlzDkZLnoV8JjDDq2A8eeHEr-2GtZIY_O2oBiA1mpvUxixkL0Nq6KqHySMvsDRegR1hhbHVgHaWBPzU4eBoVjafN-Mjt_3jP6plRu0YB7LWCMBkcoQuGwULxA5abKikeWLQgIhxKesM5iAHNK6Tqc5rzU0WYQA-WI8EDeDCDHrCxQhIOmFO2KwNHzIBwL8-C5MocoF-FAnZ3Egq-Tsx6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=oaweptRnuB25cPfjVvQxc4vaUEehGIk2ulJ84HfkiCfsVQU619DfPABtYRmKq1wckXbK6adBwZtC8_LHLW8WJVvu7rBniKJBdSFdhYeqk7bvKo5wIhZ7zVTYVjjeAVOHE48c2zFUI_DOQSdKZ6bY1_JUgCgXUbEffCw4oOwCJfe6pIUOy8xklJWKkUnQqWeGmT7HORhB5Lc0ntvlQKFIqpEsHd9CrwA2RfBJcJ67DjTd5YL6PkeWPssN5-n84IXc9OEpxwJXUt1CL7AlwjjIKR9xK1A36WAZXvruXUKmcDKifaS4tZgjyZoLmd4DtS6-tVZENUmbQ4i7XG4jHLu7Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=oaweptRnuB25cPfjVvQxc4vaUEehGIk2ulJ84HfkiCfsVQU619DfPABtYRmKq1wckXbK6adBwZtC8_LHLW8WJVvu7rBniKJBdSFdhYeqk7bvKo5wIhZ7zVTYVjjeAVOHE48c2zFUI_DOQSdKZ6bY1_JUgCgXUbEffCw4oOwCJfe6pIUOy8xklJWKkUnQqWeGmT7HORhB5Lc0ntvlQKFIqpEsHd9CrwA2RfBJcJ67DjTd5YL6PkeWPssN5-n84IXc9OEpxwJXUt1CL7AlwjjIKR9xK1A36WAZXvruXUKmcDKifaS4tZgjyZoLmd4DtS6-tVZENUmbQ4i7XG4jHLu7Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1enD5jrCQ71kKoHbZv_uXJQ4dDETGdEAb5a8Q_eNu7Iclgy2EXIYjZtussOejxuvHwCJeknG6Wv6iSgfij7FpVyqmK-r10rxZLvAaj0xUJ3A_fFOCGQpvJso1h0vdDmvl-ZldAFptG8oSF_8QzifFMyjbfN6jxLjvzTuGl8-uQWRQN3PZPIgnybbywoCWEPIdjYYOz-9ORye_aPhFa-r9InTSPHIo698vaHTeXizvtNlejpUo2QYOv9UJwbE8WCOr-Y7q8cpjhVl73QzqebRQ72nji0khkEHwfwVn43W7yhmlCWMJ8tOTr5KLBjSf-yaVWYjDvEcmh1UKu8z_KRPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTwNbXEI10KqxDoJqsJuFWtu4_5okIFYjpXs-mhL4e4fGC1_Jb6P72--4w3eHREvRM9BGtGSD-tFGlONZUMAxBWTtlyN2mQj4_TNTgSEKgwsL-CgiRr0ojaoLLIMwGsleXOnyUBv7nMBrUuEcID5EU3c2TsHuy6TLs5c-G3tnzv3UInetTmHR0GuY9lqsnUVdjEMCoEGRDegZm8H700iHY5U6a9-os0BuV8aW5td3Gn4yRUKTP_hZ_dFTUB3B8neolqPOsT9ASkaKL_zgP83UBF4WoC3DGCosOM1f1t73ZNxll5BkyRWZ1FrUrgFLN5LyG5VidMdMapXxlNQvoYRDw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=nTbaIRd94u2R_1ucI35qJwc0-P666Gz1DHgLCjxtIuYsF-BJW5a_I7NDLvUG7JhL1vlqQmTrtio9yV-PkrATT_djhefDTNLRIT-95iLf3x259HJyJF6sdXUzFxW_VfUJqAuMeKuUymuVGNbw5ZD2BejKXu5I8JzIs_Ciflnn-VnGe680_lydrx-V8nQVP84LnsUNn-AoMpRmtggUgq6_3OTL6whrh0sm4ualxn9vz0OaAbn8xvbRsxxZ7PrjpxzIeO7jPMw3Pq5InHc3XpMDF4vk63WH5WQb8mXUFMW3KOYW1-EIKlqAF0ppbGd3xWm08fu_NBs6NK7401jGreuN3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=nTbaIRd94u2R_1ucI35qJwc0-P666Gz1DHgLCjxtIuYsF-BJW5a_I7NDLvUG7JhL1vlqQmTrtio9yV-PkrATT_djhefDTNLRIT-95iLf3x259HJyJF6sdXUzFxW_VfUJqAuMeKuUymuVGNbw5ZD2BejKXu5I8JzIs_Ciflnn-VnGe680_lydrx-V8nQVP84LnsUNn-AoMpRmtggUgq6_3OTL6whrh0sm4ualxn9vz0OaAbn8xvbRsxxZ7PrjpxzIeO7jPMw3Pq5InHc3XpMDF4vk63WH5WQb8mXUFMW3KOYW1-EIKlqAF0ppbGd3xWm08fu_NBs6NK7401jGreuN3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=GRi9ha8w-a5RL2fKbFTOnPU7CmVX8ApUfJ---sLALDjj1XYD8lvBhAy0O2E0ApoKpOd01BJU7012tCBGWoP4-600IkMKNV_HmHnHBjWwKXl__XLcaSLl3bXUrMorfHPjaQpGMt1dikGA9xUBdB4V1eQPxwy5PSqmCdMJd_zfNaGJkwQv3cH-nnY7mGBKk672zFoWqbVHBOaiH1VTroGjUwcDAS6sRk8yPJdQmuPcXdguN7mQWSLLMhdJpskdadY6NRvREItqW3Legnt9p_BqzfHmvjJ1NWn4lpWhJPK6njX6ZD4cwLrOUSTC-ApoiCQ1XOHiFo5cDH8cGHztb_qfyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=GRi9ha8w-a5RL2fKbFTOnPU7CmVX8ApUfJ---sLALDjj1XYD8lvBhAy0O2E0ApoKpOd01BJU7012tCBGWoP4-600IkMKNV_HmHnHBjWwKXl__XLcaSLl3bXUrMorfHPjaQpGMt1dikGA9xUBdB4V1eQPxwy5PSqmCdMJd_zfNaGJkwQv3cH-nnY7mGBKk672zFoWqbVHBOaiH1VTroGjUwcDAS6sRk8yPJdQmuPcXdguN7mQWSLLMhdJpskdadY6NRvREItqW3Legnt9p_BqzfHmvjJ1NWn4lpWhJPK6njX6ZD4cwLrOUSTC-ApoiCQ1XOHiFo5cDH8cGHztb_qfyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcQb3x6MFe3rJVrcHjpWkYL1wEZCPhShS2jC2pL84XugiiUttGIMy3Odndc5T-XK0p9nypfjP8z5Vv_yXLlBFFf1d6aRKk06RYNJf20ghy1AnJtBSBN3SIJMhOLOf-mzenN8W3memzuJsyBw-ParF3YuysS-IHnSbRWDvTnVQVcLoszJiv34CPCDFhVfbU7CcZq09qTrKVSvINCnMsl6VJoPR7WUtMdSwfUSvnbvLJ282pLPWL8OFLnZAZgPXLH5SUH9XaGInNuEA49MH6nqN6XZbEnmsaVTQVb3YKXgKfuCiCTxTEooKMRggxr4DdZSQ2ANxpJ7BJ8NPnnEtHSHyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzxhFQPCN8o5PcdMurlU7fKZhwrbMD22r8NoRGs3FSbGudhBmy_x1Ccc7TPnC4IMK6ZICgsrm6yQY_hn7lAW6KzWPmzMCaFu-Khv35wVaOyY1J1sbv_CpQkixhfeEprWTuNlTLcJa3XFt9OJ5oNzHDhyvyk74kji_Cw5s_i-a0YpE574mvnw4W8uTkepbpabzWhqyTBuIYCs4kzbEWY-9pQYlJwFw0MVW9pyZh734WOo6n9G7VsnV80dKwLxA8o2fO1PnjwVGOVy5m9G90bPqm06aos0n5w2xKyQ6ldXdiYfaVtqj_N5f_fjPRL4BCZ16Jh0xpedb2I5k6MrFl2Pmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPsZAw-VQwwo68Jj4IjetBgHrc8PNJRB6cwQxTP0BZ62jvHk_YWiDLi9qcGOBhVzGlxD7mrJ58oNaMYXmg_qg4zRL9gXvTKWH1cvM6YnsgYZiXWG1YkWfu-JfmlnjPyUauHCG63hyIa3aL7l8YF7wKKAoA7S403Fqbz5JdEBuTqDiC90ZVeW6G6B2UGL2NdvPbzg41tgPCsfblSOuQkoH-HR02S8RYzDQNxSjOo5mZMqq3P-JS9537U8TRdwp0nXXrFT9BWvCWrl1bODhHKehTnPf9726e8ZP06HNv5lbm-esvGjgaERQhBda8sQ19gx2pUkrYHin2s1TMCx4gMRDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZQ8jYFxsRjN90IBDY99SHmIno4vqwnnfb4tvLi-8r-DUE2uWk9PZDpmJh8RORNANfpp6E6VqgNUMuG9_ZRixtAbEau1O7newnJnPV4xVe7rJQaXnwl5FwJzWgz9NXie8bm5f8ze8VDQxxkQopv8PR_Wu5YCwUY7EyIMM7u9om2jpOVg20FH4MD_FBh1fWJewR183XP8_MwJ4MauIHGNcKQoesAKIk2l7DdJfRn22Ar5AiGBgSqqf_x4cPC3H9Jn36TUSocDKTVwBMZvZuGPzRJdIiGB7eRlH2cxtHQlr11qMXAzo31A_4DG7RdHX_pkEFEQHoFDtdJrKEJrBSE1zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U07alxCCNcZJN9rmoj-rZu5xNSX0ST-N6EA73SOlGC75MNp2lCQF6zGuiwGWgQvOy_8SxgHbywaaB5poZGXO7Wt586Jpqmycd5FBddBuCK9desdTzwTIaNEV_7tamrIwp2Yz8uxH84Iwb8lsmVk4A71sHnBk2TXXVTA0J72x5FqoAX5L6gPMDQFF8lRhZDfHv_G-MtN6lAozHAyQ775vl7CBw1SAaNgWD205INNKLqqrtY5S07u9XXCxYl4-n4F17WSdN2SyNZpYjgFQFeqwwsC5BO-mzs9gGrOApKkp5WUHyW4zm4RLOFxU8MnzA_dyuAi0ghcGUuRf2cVwLsGxpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ivNC7zEVd-SWfTWOlK_9-gGGOuuFf6APh7lxXCJk5om0c1kelyYH_PsJXYv9WOWZiraBzOWZkIXICfaM_o3mSEQH55tVXMwdC2IeYwVrN-cQSVdaKWBWSPvokDbzooHzIEZ4F-c2cd-3oVRrBLaYJlnZpvbmixJi_ReinXkNkw02NMf7LsCxhRdXQ-GhMdmpAljVsBVUr5jc88kNB5xsjuorEfWUb8xF-fTpKPLvLPXC0F-EkjmkyqnfFZeJM5uyOTm_m9HacbhuNb591Rs1uO3zqpXxa1BLwjLrhPptKHcarJKrr9oqfUj8_X8jjkeNVxiJjUq9KL1UuUcj9hbDZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rfDaknfdl_2xLI8FlAILy7tLZEfLPqLCP4hRuUIB4UwYtfzBuCEMsb65BXvQF1ntoBs-r3gnalJukOBDD3hu6TZsKRB-JNAPXoUAW6Q8cltl99hya8UPqoKtkd5NNfOY-rO_D1XOP742uxjtoF34xpEEsjg8oAO4STB7aheI3Avz2HyeWtqixoBhCSMstAv-v7GArCZUu5Wzu--AFvpRHP94eQVRkarFpzs-GgV1r7sb_E3xwu60zaP5PmMeTCPNWIAPlHJz8eLfuIfvsvolnN9cmJnZM5Nvi_kcAJQROTIxQsWoeEv5WVsk76jgoNUu3t5oLahdZddy09R5EGa09A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jhxuUaNRyLqdh6lfKlrrzE5_l4vYD2nwgKZ7HK9SUZriPz2ZTYM2u-xq7eJJ0-ihEx-WQMbOMITNuIr47ZR_I1aeGdsUvohcnJJU6G1-I29C_9xnE8NlZ_DN3B7SBKiqEuTN8hGFQ_AaVt13d1L6uUi6eYx_aNb8PyGBV9nOi96g6K8XuBmiD9yEIUxC8UrZgwacDMF6Ct9h2TcYANuCAEl2rndvYDyuBdQtBGB8gNzrMVDKFIx2YFxOlc6xjT3yTC-Sp_FFix6ng2gDe4y33M3yzG673VSIoFz2Vg6hNoV5vnd-OiX06b-tttNhHckgSK85KyNf2lViEVvbNOQXvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1Oi_ywweVul1d42pCZq_xIFHooI-fh3C1ui-i3m9Qt2Y4QkFLfBwGkUyUAFYSpX1kYquASRPOSQd8n-NdmS3RYbNyJZ6KCeunDi5Cxnrwb8XFgVCWKeEkidmI0ut6FEkGwqpv4sIUSrRjKcZrH5GxvOunfkRFKppHLsuv9bENDz0X4nwUPDNAa7R1Dh4-W7F4eGIzwJuhsv8WUafxRdOV7CSDC4s6bRhAkDotPLrfqvpvS4DXV-oMrNIEFh09bq9RvnngOMKmSMqjgjoqs8Hp6rGSDpsqsbFAY_8vS0HtTx3Sw2R7AejPuZwA0ihRjWa3hAP2RxUWPUpKaVnYb4Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZKL3m1q_cgUbt7lonJmlfHYrqgQvRji2-MdKWZdj5xCD6fa9muVI7hNZMDYLcacW5A02kEUFAkJLcpGye-u9q1qlk9xdKvRnBbgSsT6njl1niC3lyLYGECbMeJr04_Ws0EW8EJDtUtStXNdqBmtBnNc52QRwXEAI-mY23rTNjSMXTTwi9qS_EZZe6u5DZ7bCabmMbcLA-nASDxiDklYRdCrOXATanQ6hN1S0EQfZHexCy8h3Hfdp3VhDf6t5bEKd2aZW3xcsyNf_6kFbleeP7JLmtYE2Cw0wxAt1Ff3FYOF4ZG4z3_-BoTqH6gz61-YOPtouI6vHUA3DKb2Og3A5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=gK0OdzA5DepDhOMgbKqyF4rHjzs4IPFAYPb6kLeG2B0god3XNJqGJBktQPixz7S9vw-SpuDb0jXN8vu8P-lYe3nvbJvqoBBC0WbtwxEXfXoxW7m2R5a2IMXrhlDHDfOOWkgOfEodiHrygaPm0DDkR-dp0FxZtQiUnGoEvUiesnV26zBFy24qKWZPxxLfDZ71-Kk9oX9PeuJiWLoWc7VxqutxZQR9YXrJAsl-h7W_xolUDRUVueJVcnTHTQ602nAfBHzO1VfCVvzDGmmK5O3WKGzPhdAH_E3e6GPRE3fn2oMBdJi3LpVppnHz_lyx40YXR55Wclf1h5bPguFd5BcXYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=gK0OdzA5DepDhOMgbKqyF4rHjzs4IPFAYPb6kLeG2B0god3XNJqGJBktQPixz7S9vw-SpuDb0jXN8vu8P-lYe3nvbJvqoBBC0WbtwxEXfXoxW7m2R5a2IMXrhlDHDfOOWkgOfEodiHrygaPm0DDkR-dp0FxZtQiUnGoEvUiesnV26zBFy24qKWZPxxLfDZ71-Kk9oX9PeuJiWLoWc7VxqutxZQR9YXrJAsl-h7W_xolUDRUVueJVcnTHTQ602nAfBHzO1VfCVvzDGmmK5O3WKGzPhdAH_E3e6GPRE3fn2oMBdJi3LpVppnHz_lyx40YXR55Wclf1h5bPguFd5BcXYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=T-ZKRNkloPkDIDbov0N6ZwJm-qHeZ31Y_QvoxQLNwsYrxK_nsW1Nf33_UOzvDzIRzYyXlF48pdjyfkvRcOe2xkp7Ef25aJuZf9vI6YkNTF3y2bO59By_KHKAOp-HUn0boZ11KCikTWZtZW5Qps5Qhtv4eMDHtSKFmPfFizV_Dg0VlDU5P4k-dNH_45CtZQhmhHVXWPjwxKN5YZjHDOXC9FqdUvTgCDayJvgYvpDbiTO1Je-sktr2gizVJU-kcBSr-k2Bc2hMlA-oy_YRRdEMZd8wbbUV7nldDiEb2QNJgu4MOIvre9H0W4UVo4g6hz0KCphaG0Tby53kPX2k6YLYaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=T-ZKRNkloPkDIDbov0N6ZwJm-qHeZ31Y_QvoxQLNwsYrxK_nsW1Nf33_UOzvDzIRzYyXlF48pdjyfkvRcOe2xkp7Ef25aJuZf9vI6YkNTF3y2bO59By_KHKAOp-HUn0boZ11KCikTWZtZW5Qps5Qhtv4eMDHtSKFmPfFizV_Dg0VlDU5P4k-dNH_45CtZQhmhHVXWPjwxKN5YZjHDOXC9FqdUvTgCDayJvgYvpDbiTO1Je-sktr2gizVJU-kcBSr-k2Bc2hMlA-oy_YRRdEMZd8wbbUV7nldDiEb2QNJgu4MOIvre9H0W4UVo4g6hz0KCphaG0Tby53kPX2k6YLYaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=L7ccOT_2uqpCQzs8mIeUrQMFA9bkD5rd5knJb7IJOWkpAaxaCfdAgofllxaJRAlMOq6V1evQO2Z1qz_0ZECtw2D5QgjAaMqAzn7dBuxUeKAxz2QYB39wxzNIsKtQbzAXqVbjKZwm_jHzK4xgmUKEA6WV6D1DLdyHu2BWQPb_Ij0XVMNeTsfyzsBlLtl4GZi4xgMhVAw5NtwtIz_AnklrgXFW67CvvpJ42CcA2M0BTeeHOnM83ZdMm7i6PVkQMI4_bVQzjR1HcbdD-Xcyw7khP1b4dB_SiRbLFWRtrN49PkV97GNIbK5bDuHM3yItOq7QZeAiIxMZ9npCwps0MWkorqqiUdh6dkFubzjSqrPszmsX4cwCGmWkMZUdR04nHMRwXwdilNxd3ujwGo2uYW3_T7yVF2TAp9iJmPvFXyAGE4-SbKiKzFEhaMjg5eQT_ES8hxbAYSLzv3lo-byX3DAHODDf8ei9QrXz4RqR-_yEbfVgpRaCjUYQM1TUNBQPxvtz2mjO0TLiaGJDSvnw29L7rEcoVsqBWzOPNmqG_TNl2pc9URyLSIjGLzY-ySpyMLYGCh_HnoM0RuMDBO3Rwni8rQOl7opjw-JTrgm7BCIYWwKeCjgDuJodtUXxDn1WywAfme2855MGjVnk4duhVGsY2B2eeA1fMa0OSuS6qX_5q3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=L7ccOT_2uqpCQzs8mIeUrQMFA9bkD5rd5knJb7IJOWkpAaxaCfdAgofllxaJRAlMOq6V1evQO2Z1qz_0ZECtw2D5QgjAaMqAzn7dBuxUeKAxz2QYB39wxzNIsKtQbzAXqVbjKZwm_jHzK4xgmUKEA6WV6D1DLdyHu2BWQPb_Ij0XVMNeTsfyzsBlLtl4GZi4xgMhVAw5NtwtIz_AnklrgXFW67CvvpJ42CcA2M0BTeeHOnM83ZdMm7i6PVkQMI4_bVQzjR1HcbdD-Xcyw7khP1b4dB_SiRbLFWRtrN49PkV97GNIbK5bDuHM3yItOq7QZeAiIxMZ9npCwps0MWkorqqiUdh6dkFubzjSqrPszmsX4cwCGmWkMZUdR04nHMRwXwdilNxd3ujwGo2uYW3_T7yVF2TAp9iJmPvFXyAGE4-SbKiKzFEhaMjg5eQT_ES8hxbAYSLzv3lo-byX3DAHODDf8ei9QrXz4RqR-_yEbfVgpRaCjUYQM1TUNBQPxvtz2mjO0TLiaGJDSvnw29L7rEcoVsqBWzOPNmqG_TNl2pc9URyLSIjGLzY-ySpyMLYGCh_HnoM0RuMDBO3Rwni8rQOl7opjw-JTrgm7BCIYWwKeCjgDuJodtUXxDn1WywAfme2855MGjVnk4duhVGsY2B2eeA1fMa0OSuS6qX_5q3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0bKbHdbQfVMHvamXl1T9CrInxS_MlKAX0dLNYM8QuIfA1R6KW5IZ1LqXQ0WajgWVZaJ68mDB0rRzOwppx4JcXLiecNNPvKgdR7qqRaOE4DfcDVJ6RJnACuSdzpO5IOcq5_pOudgzQhSzVDDzeLTciJCqNSrwLYGfH7m4hVO1sRdZV_7PbG0dOYEY2yTQHUfkzLBBMgVYwvxo1Eatr4OBsWD8eGhMkBaoQN1jdaPLvUIANdq8GhxtiXDL4FVDpIWj8I_P5PDiX72Pkp3FDJe-H3BXERlAmsJV9Sg4IIsTPoTLjqMpdBxyBtjtYIj1CvvdKqX1W2mJQhq8rUorXmLHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=sbSakbrI83CiKw_rv73xv0RoisTkb0mKyefJPPYDagF30Dk3hZNwm85LUB943_9a7vg2bYryXijPbUOoiZcbsGxss2WRoqkUSZdssKMwDedRHUvb77L9OBQTa3s9vgEOhMUvYHJABy6e_qxMEBYJOOqCZ9rpQjjpN9EfoWTi02CoGil1voY3PasyUaXtiU3mjfWcidruBNkftJhzO8ggXnQdBkVbWsxR_Xn7uvkpE15c8I2aP8Kwe53YYBTLZZYaCuMYBGqE0RJf78EsRqXSio41xWd4LPSHdknMq1Q7O7gnoYNkc_0Fnz_o7pCBQ6IjAl71I6YYnGGQ3h4t1nP01A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=sbSakbrI83CiKw_rv73xv0RoisTkb0mKyefJPPYDagF30Dk3hZNwm85LUB943_9a7vg2bYryXijPbUOoiZcbsGxss2WRoqkUSZdssKMwDedRHUvb77L9OBQTa3s9vgEOhMUvYHJABy6e_qxMEBYJOOqCZ9rpQjjpN9EfoWTi02CoGil1voY3PasyUaXtiU3mjfWcidruBNkftJhzO8ggXnQdBkVbWsxR_Xn7uvkpE15c8I2aP8Kwe53YYBTLZZYaCuMYBGqE0RJf78EsRqXSio41xWd4LPSHdknMq1Q7O7gnoYNkc_0Fnz_o7pCBQ6IjAl71I6YYnGGQ3h4t1nP01A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqUwayi6j4PNu6ae476-KSbonXa1XnBVnzwrf99qN9eRPbRWQuEQCgwUJCLrN_S1jI1tqSUgiY4jD9k-4LNMXgvtjYlg99beWo9pz8jq7Q_5O_UvUbxfngn8c0FwDx0pFK4e5MNSW9GadtKN26o9vyGMZkgKlZmVuOVU_mpXXEyPfBW5rba0EGV8LrWtlHr8PFi52zGGjwVrpwegj4r9MZ14hoBzIJ3pQKqLMjqV7MS3f0Vo76G2uVz4ikkux58rAzrokYdRLR-t41wXQE7CaJ30ChrUImgGxv3cYTA-rBakY1eoJTfkwb6zqgZvNOrONgt4H2CWLipctBLQWpPcsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZR1qESL29oySAAwIVQ-2PZyAiXOfmfFgv4_BocyF5ptQfCn1DH-aVRITybgWzXyeuNoGWUe3Os4cf-rG6DoIjJzyuzp1A_M2g4aRsf7jl6WXBaDTMpw3ocJG2U4ib2V9_zpz3toFfJUrxMQIMKvIRkYRfQtzTqFgMgy1bMk6WySUbiVrqyytP3PTQkq85TnGO_lPehiITpW7PSewPcqdQ2mZjKcNkFgnn2hbbv0M22oILox8kvGGln8gpw3oEL4VHlJjr2uQSMUpPIUorwUOoi4zU7xZ9gcWM4wTkVZVCMIxXZ4_8EmjBWMla8fwpHzeUo8139nOO3rSOb0EZ-cxHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kj4j0zalsSrrz242POQ62icTzTUfsINYgZhM8uWUBX-UQSy7PsXeaSyILqJxuXk07kDWio-lALkR_2szjzyXcQ5emsJdqwVrI9NVWbHx4owa8Cm_RvDV1k5ZEMhQ2Fd2CmIXhUH-f8fX-wrdlVEBO2kPdJUfLV9hycrgJ6CL5LnieO1hB-MtLbuJSiyS7iryOtcApGE8SRyBtWScItpGAuQuWvt7_1phbM1P_taF-GZf01YrorSqGf4jEMyBGVSyMHdn83iORFlnzq4W5_S_kuNWOxCsuEtPciMgpdbjvaK7xOTw3WYQVHjgT6LYV-7DlBxbFxPVLz9PXmQGLdzMaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZB6lG5B_5Tyk5lVsHxTef5wULmHmF_8wOYq5HjedI8Lb-hkZ1af-Lo24jVYPzi8rnbSfFf-h92llBddoizgZ96SsgXCsgGYzV159gxXUl6fn2enuUQVN7mZIcefqsSXS9IW0vdFhTcHlzzmmbquDG0q6p3eL8qFhJ2C-ZgX-XN4C8Ah30diwDokYtd3c2WGx0Es72T7V2Crd7qn_pf550ufDFuF7cMf1jRTfJOEzkM4N3ioyNnLwHmGjAqzlOhWhzO3TMzrFuF1sr3ygyYt9zpQ3G2MN2oICKUPT1pdLoxCKOZ34IVY0rJPe7jKzrweKGzQOY0GR57PPHX31LjqPvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sSEl1qzdXl7F6W0cBtlw_RNi-kJ5EFiCmbzSv8cyGG7PW0rRMWOYrAcg5cM4Uyiz721TZluLjeKuhYr25u_ndjLkHAqmE3IensnkR6S7KYfETIHNYCssLO4mJCiEuuaPx9NJDv0KWxrYkOwTEF0nwS2-6IhYdkWjLPsYMwU0bvbd33ypOqnP8poB4YW1ix-FwVY_qJyx0vtpOwLSfg3P_swLTEIMZeNFq6S5av4tjBNDX8_8ZwrhIZv4vRKZX9RdVSdUm_mTZ5Ynmz2VRT9MQKQIO2LEupCFRB2buyU69kQFnYUsWGtO09a7JX3zjDRt88p-gLT3bnri7L0drz3mIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d44rkWo8YxgMp0s7S6-9OnjnTRWKn05VuZD6PFtcKOnmnb1wIOiGigwFHmYkFwhfWL6ws6-vo5LAUMsLq7gc4E-ZfotYisAj9lf8iYdcyaR-FPO910uSzwWT67HYxhXB9eItCwBNA1-3G41zrLS_th0W2EF2lYyIEXPlOcJz_NJrrqdI7BpDqnnyLFou8dW3wFfuYEppU07oFoEkR6T30MGXvg1TlYNHIX5rSDp8h6fA54y0o3uTsfWIxTe5s4X-VL7xNSIH8r10OFByTxdThVx47qDkvrvndEOWpIWHuQo3HUVmJNXtfGDFjKM-Fh1yYw6_xXIMe4Bm0JC65aXrRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D-6m283k0pXsGZvts9-kKuo8K8Ec-mH-rFCaFYRn-ktNSUCZOE14di42sSiXr3lQsYLCCBf8a-vENUgz1olwFl8vASmOF-S-FtVsLCh8j9BRwekzRrlDNxJ92m64Ko8rTnoerFDPeWd8hlb4CG_W1i_5JY20zKnIid1Y5Pgs8SQ1KPQmgZy5mO4R2YJ9nePFFSxQfSkkvkqg2ForUWKRBx0pbhDHJMJ2Icz_TWLa9zp1Nj0qOcnNqgq_VX8CMRL3_q8mHlT6GMTyESCBuhEIYx42ULh3iWNSIooYfIPJ_morfpqbQtYzEuOE7u6_NA1T7pAWp5F3ksQj32twJKK3zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oFI5K65qTRTApfwAD4xR3gWe9pinDCb9hjWnIRmpeAs9bVpGviHTmSmfy9859ZdrkZA4O-vjpgZ91JeOCYEyMqvckpEry50OdlKEpCNsP1deowEsGDjHKKhlw-g4cPvfppCMS4vcr11UrAJ3q-OIZKogQ5GwFUtItql6l2VPYWH5ex8cNu8ueUpi1ORu2h58ibeiXKdXRsvJ_m8Kn7N90N4Ju2YtZjtH4uCQ5Ueq5O8t9d-Bf3A1CoCXbEbwJf7XBpPsX0JQ_WPlYdX-w5ithrJ_Q1qeTI1POmUGKNKKSXNg1zw5DW0wayYFS-MQygjIUEMemW6UWkpKjFQPpHMCwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/huTSZN5t5FozgDF9FfsNENCr-P7lLL0CsPcoKbROKALQPpw4T4meyPq52uYuWF__zLMtfYX46bercuYAJLxSekFXFzRg1BFmdzIFTSXoj9x7_q9r0xKbY0j_P5bZUerotj954V1V4yRJoA3DU2mLtGuG7u8zPZEP7JFLwJrhD4duGfeTvTSI8iAudQeygm2dio-2HrtQLzbke_o4GrAdf_nk1SktSV33BR0zXr6mv2oGR4dSmR5YJUD3GGoh3D3HtMIMYdmMeS5lf0jo7Cj1pI-V59vFHoD4cMdDcGF5TVj8X8kq519r7RMYjr2L23Err_HRT24kZV_jYAmJTzComw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hj1Q_MLKmSQTBNfOrkc7lzfZPaoVvBdMiT9PYLnioJJrWA2xKRcEiRCPpzKBrDkpEzCVp7lrzqYZbHMBi7cVFenxA1IBCJuMqOlf8y8bILxn1dAdpDPGjS_Si_UpGl3kzglPxq3ofedyateJtXPhFMNrJjudEOkbia1fMH1M41aFUgjNiFPkm1HKIO63n01uMBYljjuhjQP5dwLV62S6msUEXvHR5zPgPYebSgTILAIV2N0ZBc3hxJY33cMRNuJlwmPs3anRIQ2NQb00AH75q152cCpumPIo7ruVVdAbZny9hcz4i7G5iTAimsu09DIvwOmiWD6wO68CW1-6Jw8LCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNv4JNhN90rq6t_d-2MLb4LGBgkJdRJmCr4-NRYuH1F5tO83Ty2dRQF6jvUWZ76fdY3tJwxIiHXVQR2rHSYegKSwwL_GpBd8NY5uCWAuKeTG8IGFirNt1iftd1xWrz8bKqWcPuezooHTh2KMK9KvmAKiT00eGO1BK5UB8yarMSM7OI8jeavBCCBEBHywf2XaYZ0cYxFm2CP3CPtvFLIX_nJPzhmhRVlK4CIuAnTEktU56WFLohhnocsMY-1Fnc3iXzTmqCf_E_wMMca3aK73Vnx4Z1n4xp_So0VFdKqRovExhb3NghUijJGSmo5b7MWI0nDEnolFaiCTdb8qvO4uFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzEa7ZaHVFowXzIXZD5eHbLtv9vz-qrgHcGUhU68Yyfhjm92LvpwPPn-FGISo2MbdNDBlekccbWfq1QgDDjMnUX6dbd1Swf22hfG1tc7hmfvEY5VXTtBSMmKOKmQY7YqnsFHWKYHie3eS0gFTwbMQ_XGJzMzjgYR_YWCCfYaJqCU_j6tjPRhzd6umlpcnlGkXuGy95byq446HpEjkNNgU6ihN5V7EnWWTFEHTRkrnGG7TuZBAZ_04pS3ccnrAhDuZpGhmoOBFeCNiwS4Y6RRFUER5uaGKt-aKRFFuiw07izfCt0w46Nge-eB44pmkzCv95IhRBjkd3NmoZmdSBF-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gbQmc_-y4Y--yQHG4YJ4A44pKTZKzUMGiAcqcIhQBynUtk5czfNlRSoaCcD56MsgSV_xjFg4s5QFpngQIvudgtxaZ3a8ooNZq5-v_Fjm1c4DvWDGtg8dDfQYuDjIAqdAbuTNbStUC9tVEYn3DZcY1rn2WHrHFlxfTLT_TKGPyAhPmfhL1AWSiJGTyNJ9m944OcrWFvwcYzmzClIecuUqxK5T50RGSD7CxxPLybg877KyQwbaILpzmxhRthTvQ859AjTe5uB7PF5AJmiYVI2pX53Tk_9gH5t3JxssGRiv7jNHKUHkv4iZXUg5WNEWvf1tsooTbPdBB5sw1inMu9QFeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GPclXAclUE2OmaEiwSRw8mlbrsY_GobGcez5cIBHbKysoiA27awXN9PoD_G_mGbXOk3_2GTnRuxfUtIf-LbBHRtTGgxmkZMXgPMdYXE5RxQ-oj17kTa_6XJQaM7aZBWISRJ7NJgaY6SZ3xwYYWfYvbemdm4jWBj9MvpuojbqnTJuubJpBv5lvzABbvPgj6GuMakZ9eKLzFarHEPHvVIs_8BBK8NbdutEsV7r1mWYlYkFP6jtRBgOHLvNvY-0YHYva2iGyBWSGKdbqJMaL8sd77FizwBfee4gc-Gk2VG5Md2o4qkzsiGYlG4PDw0VDPGCmD1Uwt2_Dn5YpHSxOX5AGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDe08E4cpWTph2AdjPD767tZW675uEuPakcT0hG6F_7Yk7QLY1i3VXnVQ_Vj-OcUHkFAdl9XoEMoOFuTZin6qrF8e0Dp4Q8YtwSVf3nU8b5egKOYX4AhNw18ha_IV_4EEVXz5Cu_amyIwxOGqyvf-o6PV4sRtlG_3p-xmeK6RDgGKQLZLqh_luwrpx2W63Noccm376DwGD0hj1qsE4eu4-pNgefkCJbh7M2Fhw6epfXdYyeQJS_x2YZ2CRsYiS3e3VsA1US0ycbtUWQGybVnkNMhchK_7l3lgZoEEfStVi3p93kdYDUkp2wBGKLkgFP-W6GBqEaYv4k2ZNmWDcT0Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NnJwIKS07v2SUgsFqt1_qdd3U5kcEJi5EAn7Ki3rBzf1yjbTg9zQuFsmXbOsdRKkDp_Y_ZpNJ7DOZUXYjN5pvRd6ZfdFve4pDMlRywF4H_bkrCpP_XW1H3U_WLUsuWjmb1l5GtuavzIvtP0H4ybNwCWByKIb67_giZlQAaMesQ193Urz8-V31KUsUGYdhSYCK46l7l2rLhw5iDIyox3hkE_PHZPY5dOF5fsXF4T8z0gDA3mSO_Pkv6t-__c4unrOnZgJkdEl9Pmr3nWlj5Z7HmQrckhvQY9Dk0ty3_B3njktJ8E1It1x-3SVmDlY86wTgQzBVViiMgxaZH4cgs9eDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdh_q_JECRyhjt8RsmpTWhoWbdGL_yCqtNzS0D2hRm_-Qw4hFN2ldsFwfa4TrWcbEDPFd6hkM-PdJv7jseBpZ-0UQahkUU1qnN4sg6IRq8GebxeGarxV3f8OzF_hDG7lTid6JVV3sJnMNeJoBIOUS9idwVLjw-kX5SiwAS0jh0VYD5RaqaATHa5F9GVQvhrYmPsGD-fCRUynntPq7YTjPAmKb18BckK3DZc2Yex0XcpewLkzpJ8-uEGYdht8hi8Ok9yZyE65ljHsH9uduNr4GCO5s9QtZBUUVVNJmoiKut_rHRzLwA1b0bFYs4LyuVoWP3XYBDsTuFowGpxB1Q5_CQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=fLTInPiGe6ANbTQwalXv9xf0hktBEGK2ejGkdIcX0qTOpv8iPUt6i5JtpEJ_bdT4DMYAE4ASpG0zyK6kgsSSw2JjbeT0xi0uA90OpyqFwDzEecMG2XQDfXYxf0jQFqXec-boVUnGOEy1Cq_nxRCDi1WMzBvWkHEgszofKsUA7ZodU7DKYhR8_SV5kKq8Ldxt7X_Cpo5Gbhlj2Bdb6rpbML19_h7eXkg28eUaM01HbJ7efKJvWNj78tt6zokUtk4VMQ-qjXOTdfTbiKAsaeZf9Z7SJTAdyppxrDiUzwJROPPj93XWugr9flfEufVGHr0BpyZlW_GUIM0e2JP_m5xqtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=fLTInPiGe6ANbTQwalXv9xf0hktBEGK2ejGkdIcX0qTOpv8iPUt6i5JtpEJ_bdT4DMYAE4ASpG0zyK6kgsSSw2JjbeT0xi0uA90OpyqFwDzEecMG2XQDfXYxf0jQFqXec-boVUnGOEy1Cq_nxRCDi1WMzBvWkHEgszofKsUA7ZodU7DKYhR8_SV5kKq8Ldxt7X_Cpo5Gbhlj2Bdb6rpbML19_h7eXkg28eUaM01HbJ7efKJvWNj78tt6zokUtk4VMQ-qjXOTdfTbiKAsaeZf9Z7SJTAdyppxrDiUzwJROPPj93XWugr9flfEufVGHr0BpyZlW_GUIM0e2JP_m5xqtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ju5nsqrsKcPSEYeFfn3fc9H-3LAwoWRUWtAJkXmUsWgqbjv3DFWTdaT2lv9OyNW-YSzU_WOVb0rE1aRduy5stqlgRdaSPu99g62AzF7RxNiOpYhYiJGDToMniri1j2HXQPNDYG8rewA4mi2A23KNT9BMbBR6ZzpaXMfg4QfQOpASmTQ_4QVJYrIfRwAzP3xc9Dubg-hweZDZcEN-kWNi-FjoqN6VXCAGFjUvx6W4JHJC-vuVZrpO28QJqGJeSt5a8Nk4kROA7BekpSrT3CzUOdvJqsT8keUSdKNLxdFxUAbZP0vICBn_EEXVYP3LLOnB0W0VfvsWzkm0cleievfyDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCilWnkvhhfJ9Skv9BO4asoleD4WWe_XWfmj69ZX8r98EWthLaGtntX96-GgjnWrrB0sqSSMe6o8jDkkB7s6JJeSboq_VLobn0RcCt9e5AET92KAyRcPknyFRqBnKNd2Dk7ZZDiQ5Qr4dnqpCocZzaAPtkiP5FsYTyaZi4W35nWZWYS6Fg2RbL7i9-zzK9sr3p8WggoSEgMJR1AUjCQTRaARqettEVz0Ge4bEwO_EaQsfqRCMvb-i2rCgOsUEw0NLkw0FwjmsJmpfVfFPD1XULVx0GEL39ilNXethbYrih2-XYYkG4metkL6Sk6_N_GHf2EBTvPw5p_m0L5r9ljykg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCnXnoEYIZmH8_mGXwqsEM1QKasYducSSr0J0BVth5N-kTQZEIXIIMpcAbwn5sdZD10sHzJ-HRjL1YvByn0MXHjnmP6YvEutd-xfpZWkUijQe-kjeHffYmylEWADbtPnJZwSP92_q50sSjdDdBXDQOnQ56zJfj4TDi7PbHcrpbPIjqO9CnqWxZi1UJIrXw39dmEzwK5krB0ehpJW5grzUoOxKAgRAGicA8XbbxlVEPuUPbtxIdJBktLsWwHuUs78HPEQwFNGmCtG8jmeAO2hcNnT6V03-k3IqcIXUFFToUWr-VyjgxsKihYfifp2PlG52MDSYgtmHmfcLh641c0aoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
