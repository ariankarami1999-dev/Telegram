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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 20:50:37</div>
<hr>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjOPiJkM5-EEDM6Bj7OV6FYwa6uuVXOBiL-mXDklkcvICj9qBgt2UZtADLR8kiyyeOHfyQcn0FfLZdo9ahC6WTCE0Gy3eF6J_AGRCc6jpnP73GoufsqCZZNizMdGkZTUO49khBUxM4Y6TBU2vIOrdghJElvyZEl5IEKOaMh7yuWN69SA0jg0l0idBUPSC9aBI8wPpcNuXekSRjEz7Jvd8TkQdToAqfOjoCcsa8Qgze6YuKR176p9Qk2dAQHVGpE4zzljhITcIpBkHsGB0OiIhUdx0VZqTRhxzBzphO0T1rgW6byolugK1p47bRTt68SFGrPMKK28I-AJjm0aM8p2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjIQTM80iQK69zWeK1zv2hRR6NfL3wncov7BnLo3ze6n_keZzpyBK1vl5c4KapxAjE3O0y6vVlg8WgIA2uFu9ji5D8zywqX9ho0Kqvr_2fcYIHssdNypK6zYLRgiyV7lmBr5XMuduQIcUo85FnSXHKTF21c5j51idawfac2Bw0DCD44sZJZghFvZwzJqcrlEZlB_LW6QE5nHkDmtkH6fA2YqMQG5HTtD6v8ISDpmyT9QyyxsXk4wN47Lc-AqMHkeTwWzW9uARkCB7smN3iFsM1nEqy4MCf1aMQk7sSZ1R7i_DyDjHRlIHDFXBPsmRuiUmnO9GAaYzkOS1EObA5m8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5SNeWkjycX6gsJJwtvo20Mpl26SZZjX19Gi5my1d3P89yGGHjNGX5Nb7B9HX3xHy1hSjl1LHA2YguAot4MmdK9Iqc2jXoJdEQJuGH_hl_a6SzgMO_5Q2_Q4ueCYlF9SWiYxniCXq7mimIN5jvMhQL8V-LgiZPrRMmFrwC7D8xQOkAVJ_jbDkFDgbJGLV3-I9-I58jLC6-5e9E65UTRvfMOvsufXjtX96ST-BYDKr1xk33PWoaF0-KoIJbmhf3vHtfYb8KpmjX4H60z4_JGadulFYnxuXRxALiwZYDfx2YkROe3M9MjCs44ByzEDodPV_Qn10wxXaVt0y3ID6TVyfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0dbeuUShWM30A_kcihgPofaUCtPNvenAZqq6Y6HkEQ0PEo-xt4qg281D3PmxKVo0S6c3h5XGhG8roFn54Osm0dfLCMx1fNM_hRpo24dJrmZdIImiAVEEGl2n1Asn5OaWQtL_Rx9fHVJ62o0Ml6hs2t0NcQ9RKKXIvTPQb0bWDzKZrxFtDLuS32HRey8R35BESCXF8ZoIJfE22sRsn0N0te6LMPVJ3KwEZUFjyPtTkcI0P0XQiZwGOt24oXXc8qmz5oRQy2tH3uLEON-I7dvVbMOtYa3HajQA_2JT-widb9tMdfT_g11s9psXz7OkHnf30w6WOZur8mdeCB97sDhYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0zeHLwcL_94UpOnVwHJeR-SjOVAwRNEQoorPnaFWQ1ohNkbzQK4p3iiQl9uEkdgpLe2LnBgv3grpS7bFiErOV3cDg5J7skPJ1Ki4uwUSIpNXd-N78Xy5XMWlb_a8QerRDqBcjhthQRFwffUFxCic89OYyk1zoGFsIXSMCqWdSsN0Z3LWgw5PWsPkrPTiFta-EksSqP8n5_uEJdZHT4kK57drrgogCbn0DMDAxQDxKE7wC3cItTpLv_N1J_jjecwzBtAtuuv3oxcuQ9rcVjp2y0oUeZUXqr88NGUkO_6atSFzTMtaiZB_ti_i1XeA0NO4YNHIzjrFR4kBNQDHyh7Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5P76CyG4bVOYZoppovkF2x3KEB2a0Bm8ajKs3D4u0xTvsXMf4OYFfV8M49NvXT8IRKwANSh1ScxXHMGskLkujk2SYWBPtDpjAl46UvK4S6OGqAkva3ZEpS3CXjeC-0eeRqDuptKGmQMtplBiRMhwiQsMFKcUs2x2HNZDlMo9_W_qMjhKWuJuhLkms754rUBXzBsSDUNadQsSWxxtfC8x9dERl6p_eYSw6Z-mLIfXVrJkUEMp6j2RQzJjf28ojuskHK9vYH9r_WP4hQByAe_OxxpXnf1Se9jyYLQpR4bRv3un-h9NdgIAi28xGbzwzlkITL6IGlMWozSljuzOyEVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLWvRidvF2WGX36rJFyIkgIwMU8tz8LI1R-TjkWtDoaERDn2JcMfma3Q7dP8EIs_jRegQ0dIh3TLudy0PfUgwTUDcJTqdMdrkrk4ng3c08s-aKyfzgOlabmkZYEKrPfJ0fLz7uqIOaX4kiYylFMCzCMZlmED0hTfpoNNlnW0_w5KhXtk6CtgXIE7Yux4q3PNQACmqO-SmVqFStMtIXYbudWQSHcBuwg9KKTG9NgTNq1Ntf5wVpT8lX2mWEEnwUtyE9ul4XcU3Ab1ufnofnPVjn7IPANWiqY8r0C3IbmKPBLZ5FGqWr8-KnmX0-Pv5ufuK_OOhabkqLEbXY50RDJlAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=epwSbDFccUQ7k0o5tbn8RVo6rNJUHV5KrpNQfy6PqGMnjPhLqBGAHst5B1CVf4A4EKaefDz1-TnVcvyazkzZP_rcTlsJLudy61CIoKrEx7BGt3QL9HliAkuLG9fZZ5niJXG0TtMsAA74MKHv46_8okFsy1D3v8gxfL82x_8akuWzHRjRp5zdNul8sVlgDv5ZtVjOdIN8CPYm0px4wKoDRUrH-R3e-DwE8sINQb8BF8DuwSRYPlMtL3g2LxDQ4CVQcPeh3pywkJS9fevYclGnsHmUwLaNZQHibmYDzZpNVvctzocsNCt4OpAadWcmRBHp3Nt5DAyofyCPR2t-GDfdAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=epwSbDFccUQ7k0o5tbn8RVo6rNJUHV5KrpNQfy6PqGMnjPhLqBGAHst5B1CVf4A4EKaefDz1-TnVcvyazkzZP_rcTlsJLudy61CIoKrEx7BGt3QL9HliAkuLG9fZZ5niJXG0TtMsAA74MKHv46_8okFsy1D3v8gxfL82x_8akuWzHRjRp5zdNul8sVlgDv5ZtVjOdIN8CPYm0px4wKoDRUrH-R3e-DwE8sINQb8BF8DuwSRYPlMtL3g2LxDQ4CVQcPeh3pywkJS9fevYclGnsHmUwLaNZQHibmYDzZpNVvctzocsNCt4OpAadWcmRBHp3Nt5DAyofyCPR2t-GDfdAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEXtfY8-FEUVtVRd5xFjB7FTDSe3H-iwxnqqV4pDaLdkv0y7wbH0AXhiWInvM1lBBqrvzxqKv2iNdnxi0KUn1Ar_hxL1JYTFcgkKNVTDAzSFwNpn4JAq4ySOeEHQ0G2P827Nz3JrOA_hK1_ex3B-i-CB-8rjALMoiXsNCrr55NwigTZEG4TpaGuYWY8FxGPhSh33Rvg49G_ah-EwktzSJjGN0mYDf5sN8LvAcuuG5TRqW_b6ZQCm1IiFiBoABDuYEQub4Gx9WXdbQZMWwV0To61Ic3vgcleuZTBnmShL9terCQdWPlTGWrZBtNBeGNtE3D1XpjQgYNvBYjV_OpIW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbjCfFse6t1YbjGml3SlfdHI1-j75JHeGDhn4CS_Sz-Rd--b5MZznij5rB4fQ4rEKfwImdBEWA-mRXcsH0yGj4aSfxDjXKmsln8BTxFIyRyf27zQwZMl5Phoen1u2BSs-VNlElHQzEHHRLuJqzEbHgJFBpglCiSpdMe3gbomE3CGpb1yXPwMsydJY8PR4jOBjywxPBDamF1tyPmULlV3w2BgKY54m-6EcAgSpIZ2NnxkQHMUws0yY5A-jGdlu1A3uzjBtvABiqALg-v8C9G-MZ_Sn4QaMV6CaiaelQ_J-JpPbTah2xg8Bp7h8loPSGRqbuEO7jK6KHPygUymChN3bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ijcuw-5ciz40_ZiXHg2sKAPVPZyWFNrZQtAhsx7FqEbRaazz7BOdbQN8yzPmu5qTLeTuFmcwl2EMLvTaiuOuynvhn409RihWd4PZ5omK_iazIXLuGekF3Ag-hgek_HltpzsEh0ivN4vZNnYH0T58qZI0Y5m5FjeKxDxlYnLGq3BsjQmBaM4-R25cYQHi8FKhxjZDjLeJ2bO4PAKQV-IWNoEpWFRRXED2FJ3W6kG2kNahCVnT-0712xBrQJnXME6QjAUmRBFoynV5oEFdLMbm9r--RLz_nmNqrnTT7cUPKFuCuN9YQLKQgzBerGthXkXfLAbNEt8lEgtW1W2QVDAmSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAHnLNTXX17KBO8A2FlITftp3ArkHMx6mKWlLst-7rve8nuDGMVlC--DjOFkl8yRGwtvmQB8s_av19MjbQO1jpmUH5tr-YZhWPCBnRWGFJgzJHeL3D586KNKr9VNhozBSO4vgSAOMjARBVM9Y_6hecjkSUcnVFR8w9pTsfM_IKfuleFulEYl9p3G3I4Olvyami_039-0MUBEjrr23XjXhgL-inJa5TEhnmmiRUnDUPKR7acYbKadZcrKhtNFMGG4AeJLGcCGpubd1iXrJWGiA0cWYAbh5GdP9YWjgwQaEUoiMI5UdGoiRLN8MYCoIc6kLSnj-xEgtC0eF1TcOTkjJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5CC9PkTvuzFTnuZ0HT-x2MFdR4EGOrZMrBaGCn2Jq8y5EYVR4c7uNgs4dFuJh9xfNtImrMYYjkIjvDlbBhyxfpaLAKA3W73DsBDcmqhS3Ox5Cmf8vXO1kzN0CBSGkAYnAbV5Jjd8ga38CHnNGWU8MqOjbrGa2phjO4hUQpTsIV04je-TLIuRKgUv3XPIkO1Oi7Pc5BuJaBXV_Z1XoWdyGB64jt0IjZ2aGXexqB8pjFrOL--FEnO7s3C84iyRq_fWspaYpoLcCbynLIIbfuDyVV0XnQoVvZEE0ayu9_V2Cd1xkvZo-GkhCaHHANqHzHcIzUSCKhSynwysezwJQZ9rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJS9KLX91swYnngQos5WDgd2PTUI_Nou70LzQZuOr7GzJwMU6k-1Z9Ta3jLwQuciDQy09j8F3GTWxMuvgU4fcIDLx8fb2ih-buF4G2d27Zm2B-4uNO_xRAZsIrG40IviK7f7nE2aeHSP10EjsX9GcV7k_-n6TJ17SDkpCoCoBvV5DxT34X_kJ5ABkbJ3gA--gjQNSJj0YdLOiIzPTcCIMM9-Mq93FBQmqAnx9wK4fHYMKHwRw5LIsuFJ6ve9yMGVQc4VV1xi20D9SVMCAO_E-_nu7WgqMHze5SQQs9XteOc8p3bqybopu2vzdzX2LWdumnwY9TBXOGw3RosoFHez3T6k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJS9KLX91swYnngQos5WDgd2PTUI_Nou70LzQZuOr7GzJwMU6k-1Z9Ta3jLwQuciDQy09j8F3GTWxMuvgU4fcIDLx8fb2ih-buF4G2d27Zm2B-4uNO_xRAZsIrG40IviK7f7nE2aeHSP10EjsX9GcV7k_-n6TJ17SDkpCoCoBvV5DxT34X_kJ5ABkbJ3gA--gjQNSJj0YdLOiIzPTcCIMM9-Mq93FBQmqAnx9wK4fHYMKHwRw5LIsuFJ6ve9yMGVQc4VV1xi20D9SVMCAO_E-_nu7WgqMHze5SQQs9XteOc8p3bqybopu2vzdzX2LWdumnwY9TBXOGw3RosoFHez3T6k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRf58BM1soe3afBLnwcuolqCL0jIx-lO7mGGXt5EI4Gkg8KmOXrhhMHT3dp4zVoIVF-Y-RbuiJ6soDe3KC2PmFUFjfHrH4HMvaCGmNbPGIJpf-NEL0Mt4LjaOEAzHh0w5IEyBei9NyFPdO9Qo931eyoREkvmHo3OOHwMfmqKH2iI6fRKM06VvO4XdgXINLFHedWyIwbx-sL01dEHGu7WuJ7fSOPjE51SdCyF8qrGlVD4EvdOG3dFZclnEGJJtAYFlN4D2E5M-VRYGYGmAW8ZExu7TzfikZKlhk8Xb1wBWwxvv95Ekmor1SgEbeDT8UwDVlStRA5eqa6Obp_eonUgHDer0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRf58BM1soe3afBLnwcuolqCL0jIx-lO7mGGXt5EI4Gkg8KmOXrhhMHT3dp4zVoIVF-Y-RbuiJ6soDe3KC2PmFUFjfHrH4HMvaCGmNbPGIJpf-NEL0Mt4LjaOEAzHh0w5IEyBei9NyFPdO9Qo931eyoREkvmHo3OOHwMfmqKH2iI6fRKM06VvO4XdgXINLFHedWyIwbx-sL01dEHGu7WuJ7fSOPjE51SdCyF8qrGlVD4EvdOG3dFZclnEGJJtAYFlN4D2E5M-VRYGYGmAW8ZExu7TzfikZKlhk8Xb1wBWwxvv95Ekmor1SgEbeDT8UwDVlStRA5eqa6Obp_eonUgHDer0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=fhJigePYH-LWLca48m4sRcRUPqxRMnBoiFvYJJm7wwWEHrbbaJSII-P9krBmLOISyFs4CY_GpigtTmDsm6lHTqznT_jwk667q4M_yJmvzmMLzLcqiIQGjsYN69_HYXcCg2TQGWaMS6rydKUcJtl7w10lrqw-KAC3DZm4tTNu_Q0Dc7xZuyNMvDEspEYlFBBInn7R8Fd5OXuA4qVWn1X5Z5JkKo8MPNZslLm8zgzD7OD6g42yvCZpkmN_GFfPQ3cGu6mMztST-3vIwMs2XjdjsiJKI8eXiOQqpINrUsN3RxhXdsylj2ZpX8JkcjOjckezYE8xcra_opDX7aD6mpEzFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=fhJigePYH-LWLca48m4sRcRUPqxRMnBoiFvYJJm7wwWEHrbbaJSII-P9krBmLOISyFs4CY_GpigtTmDsm6lHTqznT_jwk667q4M_yJmvzmMLzLcqiIQGjsYN69_HYXcCg2TQGWaMS6rydKUcJtl7w10lrqw-KAC3DZm4tTNu_Q0Dc7xZuyNMvDEspEYlFBBInn7R8Fd5OXuA4qVWn1X5Z5JkKo8MPNZslLm8zgzD7OD6g42yvCZpkmN_GFfPQ3cGu6mMztST-3vIwMs2XjdjsiJKI8eXiOQqpINrUsN3RxhXdsylj2ZpX8JkcjOjckezYE8xcra_opDX7aD6mpEzFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbCi8H_ouf3r_aTetLPdWG6x84Ya98hSe6j-P5VW_2pvYiYfYJd352dzAhhZaTW2AVZ9dHs3p_Kf-_fFvoDFL7Pv8emvE9cJ32YKubS8DoQAtcWmYgHNU5DVi4Ro1BKKHc2OUgghhTqjl64j1MTPhawiT2gLNdc38UdA90vN5jhOGCu_EaSz6D94TP8luA4K_q5qtrBr2ER6xyvQkA2oSNpUbpQoSUxpXBwHvHIVRwdoVzQJ0zAnWa_mkNK3sLh5Vx8QTMguQVDd_yDos-W2CP3Ssh1pSHoIjnE3t3vWWdRjTWHe9PD2dTgBLEd7bOSsQRipzkosig83c_-184a3Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUCautNpjZ2n6Q1at0OT7ZrwaMVhN0WfwrllZmGxz9dgLWnG8Q_a_CQOJt3ZZ4ZwTjYjGgjuTB3zZ3e7femDzwduHRq9oab6Ya02nO23XuP15zMY3e0iUpINtM9bBYJCJ1ZwsBr95pqAmdy8w8qJIQtgvabRVALL0SvtVDjRM8zh118Gl7fBpxeJnr4BLxL_ZWECpmxhx1mwco_4oTplXefGD1FzujlYNKcB1e6APbCyZnTkY7MVhLUa_xADF4F0ns5t0kABZWWg_h4xfNG0rX-3fyBlYPSAGhpzCkktdY99JtUefOakQr0B0Qq8CJwFCAtscutCGryoU4YQQeyyqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=Gers70DdMtRul5pBHTVuVBssXaY0TGmyKifPdUoxCT5uNeCOyVhkghpSnmsEpmp017YmNixkDlKRhKVT0bslI1mkU05QFn-xy-VKzuO21v9Oi-xOtUvgi4TSq7j086T6fhi1MBjLPivnve29OwuKN8CcFUYD2gHCDLyH9txOydGuDXYpcxNy29G-RtEiS6WrLKH0Cg_3VZWD2SeXrn0thgI4Pl4xfGZFp8ApEQenczQRhzN4DiCkKNKVV9CTbNuALGetbg-ZG8x2HLkDwUeWfTXlhpmNSoOFexd6_aDSDZoqliwSlgRG5IcrblGN69jhrdfm3dHHZZM7d0GvJAHqURVUVMfvUbKVAxZ3swuU9N2q4VY0g44iyU-7nGXJHow7ocGFJwCzPGuXY-Jh4tvFgQky1xnW303K9h-Q-xp7lNvDj7h0AQmq-OgkvBt_JIbJiJj3035ioD58M2oSHRg7MyxBWSblxCOZx3IiwZ8X4TbaF1a3vaHIjUj81Dfx7AUUctT7Ia9ibWGsCqE7cuxk_QFP2knZ1kEb0OqUPuKoeFhsSuL2VkQ4x_fLbGuZbU9BgGRSDWMTnZhWeo_TnZpX1YrH2nXGq_KPZiXiCjjbB0ci9IZnuYUHFg68IpmI1mewpBBkfNtzmMItSKALkp7e7j5HldzWKOKhhUbq9RV2C1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=Gers70DdMtRul5pBHTVuVBssXaY0TGmyKifPdUoxCT5uNeCOyVhkghpSnmsEpmp017YmNixkDlKRhKVT0bslI1mkU05QFn-xy-VKzuO21v9Oi-xOtUvgi4TSq7j086T6fhi1MBjLPivnve29OwuKN8CcFUYD2gHCDLyH9txOydGuDXYpcxNy29G-RtEiS6WrLKH0Cg_3VZWD2SeXrn0thgI4Pl4xfGZFp8ApEQenczQRhzN4DiCkKNKVV9CTbNuALGetbg-ZG8x2HLkDwUeWfTXlhpmNSoOFexd6_aDSDZoqliwSlgRG5IcrblGN69jhrdfm3dHHZZM7d0GvJAHqURVUVMfvUbKVAxZ3swuU9N2q4VY0g44iyU-7nGXJHow7ocGFJwCzPGuXY-Jh4tvFgQky1xnW303K9h-Q-xp7lNvDj7h0AQmq-OgkvBt_JIbJiJj3035ioD58M2oSHRg7MyxBWSblxCOZx3IiwZ8X4TbaF1a3vaHIjUj81Dfx7AUUctT7Ia9ibWGsCqE7cuxk_QFP2knZ1kEb0OqUPuKoeFhsSuL2VkQ4x_fLbGuZbU9BgGRSDWMTnZhWeo_TnZpX1YrH2nXGq_KPZiXiCjjbB0ci9IZnuYUHFg68IpmI1mewpBBkfNtzmMItSKALkp7e7j5HldzWKOKhhUbq9RV2C1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=IcEua5sIq0ULQNRWUZjKD5FBoQdd0aIDh5lq9NuDy89rFH7a7ZDWpuIGG-F5E_-22NBUp0adfVoHpTSXCGkTdDEISbYUPK7CSVkaje1JFwVsdNHYHVOw8h6WSimuK7e__OMn8BkcGeTWz6EtgWkLg5BpELsTRwHDjsGFe8jbl-kh2zmaOPiI3Mewiks0QQga0mBVcIISN5sQwHJcgwLaioNVIMN3wNblX0gUi_VXSMLcHqsbHrEWwiek2ssR60mV33POun9wa42JugIjAwi4Pmm0fg-lv9G8PTEr6Uhx94kydNcCnDqeD0gIc5nnAy_L3IyZ3TNrOV99f1UIxfnW0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=IcEua5sIq0ULQNRWUZjKD5FBoQdd0aIDh5lq9NuDy89rFH7a7ZDWpuIGG-F5E_-22NBUp0adfVoHpTSXCGkTdDEISbYUPK7CSVkaje1JFwVsdNHYHVOw8h6WSimuK7e__OMn8BkcGeTWz6EtgWkLg5BpELsTRwHDjsGFe8jbl-kh2zmaOPiI3Mewiks0QQga0mBVcIISN5sQwHJcgwLaioNVIMN3wNblX0gUi_VXSMLcHqsbHrEWwiek2ssR60mV33POun9wa42JugIjAwi4Pmm0fg-lv9G8PTEr6Uhx94kydNcCnDqeD0gIc5nnAy_L3IyZ3TNrOV99f1UIxfnW0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxC3_ixWxYxPMs1HIbnIDkh1qR1FdupyYVuX2dP-nXNTmZtLmhN1SnexIIgLUxiq6E2vgToONHHy2Ai2Ehnact0q0XUfdh91lVSRFrPf7MhBw4ffEo8JqAfnQjghMC00ywY6yr7aROhCHTgXq5CkE767TSqMjvDId-xsDQf5dLnN-Wke5yMrfmJ0AxAhBlP1xqAu2IRc8Yslgf94m01WQczxu_dXtAoki9dZmRkICEkMYgb_ucoPi4euzlRXYRVV0HEI_I7jx9SJS6hVPLkEciOY579Z8CBPTNsHoR9nh_U8-_wvKtWOK4m_mw6yCA3g4Tt0HgdG8Ui53GPaKxk-Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z_iZvD0tbYWWOFR58V-YIz-tVzfRJKXO--_IK_KD1R2CeOpm_wPSN3z9uRGHb_CN7PPU43XnlPpeesnFw--SMR-1tmwXa0nOqLoIGuXHh_M7B8LolBgVjvGJHwSokFb3hqltFsPHsFQ1bSZ-I_Rj2tek4ZwSEEHxF_vSUTWUOA1kVqt8gGnXUn_GVbXunmdlnEn_gkbjrgl27v4741RYKR3WuFwo-ysgPb6dGlBurJGTqZSOq2gd-DiMUey-MUcoyd7faM6GW3dBdSVhmcjW49zYKQTRL9idXsk9G913rACzvOA93wtynvmO59kFLTB7u7VIJcE5FsAzSSgTPBEZ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GvlqLPuWiB5-r9kKlt3PSYa2S5gdo9A-R5WuJZMv56o6cqQCNyesZpYM5pym8KbG1CxaVvJOKDO-J4z9AavegtZHR1JTWUuZDqJHu-lO3Bf4DiCZKg8dl7WBv5dUL-NIZr-ZZyCKvDd0aZMlQzh-UIYWGlDe3RS2KQcdNZWaHnyTZim20Y3C4QPtAh5NoEBh98NKSpYFMvz0kfP7NUHU1m3lnzq7n2ffwQ79BQu-ADojFVnWY_azJqqthEvqGqFr_3EwzpSQHY1qgK-X1Qp0Y728teWK9SLuREaUO9hOLq1dcSTTfi_su2tmhizCmqMGGE2Gp90ovRa3Q62DG6agdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=u5rHtu2lxChQ3Q4fGMnqKOkKfiNZvoVP3AWgK0w2AENbhSpL83PBFvdbs53GjtnBMMfzObc_OU9e21Xn9AYtph9ZdV6Y-Ebl38PNl2NQ6GSN1Klwr9oSnGe24HhUYkqW8R7xKRve7HfUIr8rYrPYFPGUf-ZnYonsiILRbM-VjmIkfxzp1abVoKHuWVwykqEmBYTelBd-ZnZCKR8w75W_mKg6Xjym4065wdpE0B6m4Prt784DXOYfk1KQ_PU0-HW37pxfkzhWHaKlTZdwM6PcvZcWMwyQuVyhv6vIA97DZyWZZLqLp3avFQ81oWtPceiLivNQ839Gk8PBt6GfnPBu_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=u5rHtu2lxChQ3Q4fGMnqKOkKfiNZvoVP3AWgK0w2AENbhSpL83PBFvdbs53GjtnBMMfzObc_OU9e21Xn9AYtph9ZdV6Y-Ebl38PNl2NQ6GSN1Klwr9oSnGe24HhUYkqW8R7xKRve7HfUIr8rYrPYFPGUf-ZnYonsiILRbM-VjmIkfxzp1abVoKHuWVwykqEmBYTelBd-ZnZCKR8w75W_mKg6Xjym4065wdpE0B6m4Prt784DXOYfk1KQ_PU0-HW37pxfkzhWHaKlTZdwM6PcvZcWMwyQuVyhv6vIA97DZyWZZLqLp3avFQ81oWtPceiLivNQ839Gk8PBt6GfnPBu_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=mm7UcG0Z5zSCqDOcHZI6p5drqqwPlZRO7WcQZqckZ9gSxVVz0Uzw7Fi704eV7bxVh14M1hFyJLfWkPTFiCxIdvDH0SJPVYgg1nkEABZLoYrXPxxgIC3VRcRaL18OROSbrXWuPaD4rI6ntFQhhW2WrGI95qpJR4uyAfN88stdcNW6U3fHqVEgixIlG21TSCCcKb01XugkDzl4C6HhIAgloLk-HCijgyy6OwEItU_FlPnobDlV3EUUlfqQZyf7qCIrDbSutLFJLf0EPWB_iqJoK1eGlmjlb-I-Svi3TbiuqybY3OE9cBYqW4-x9Wokj5CWtNmqPSINmwzzfq9k9iuNmYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=mm7UcG0Z5zSCqDOcHZI6p5drqqwPlZRO7WcQZqckZ9gSxVVz0Uzw7Fi704eV7bxVh14M1hFyJLfWkPTFiCxIdvDH0SJPVYgg1nkEABZLoYrXPxxgIC3VRcRaL18OROSbrXWuPaD4rI6ntFQhhW2WrGI95qpJR4uyAfN88stdcNW6U3fHqVEgixIlG21TSCCcKb01XugkDzl4C6HhIAgloLk-HCijgyy6OwEItU_FlPnobDlV3EUUlfqQZyf7qCIrDbSutLFJLf0EPWB_iqJoK1eGlmjlb-I-Svi3TbiuqybY3OE9cBYqW4-x9Wokj5CWtNmqPSINmwzzfq9k9iuNmYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfnTQ-bt6L9KbxHgI03JlB9icWszjSPzxyzkEPcZg-U6K-3f8XF9aGfDqFSTwnLnEwEFSqijZ2MPmZj6SVLfPbCQUwtfbFSI3IelDVEB91lVusct_DkLSXirnyOsQ1DLZ4M3lsaEi4J0mYCyp2rxfatP8x23MG4OTxAJQuIAXK0nRMngKeWvpJyVM2WDqWNR0BQ9Wasg6FkAx2zyyJ_fI-3yq7nXoY_aUN_cmEehbmxRHhJDxPXh29r85zJPKe70N9OxZojCQcunHo9AhVWhACfew-LzR12HWuP_GdAoNLND3BehIL6iaI4I99FeXon8Vr46STtPho-Ofd4eUaloKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQguYQZdzZrqbULcjbQBE2pbIv1xTjgMzL9-9NC1XwchSRmCbwR_ykQll1QEsus2GK1mFtQCtt5D6-4cNpjI2193wxL71mn78AHJJyTP8JbEt9MJvmJ0_8YKN-Ew6PRa2VinI-LQU_YawtL2GGXxmC7WTBO0W_2oAxu_7WroKVdwhiuPEUZR64plsT_KV8CyrVtVuSvPjbN0jzIkzv-_72YV3P4_lAPZGzu3qPgO1HILTBll9IsMHP5-LEjvXS-hHd_cqynmynMOMyrocxSAUcgBnHXXAqB-ICSKPhLH29z-H8H0SGoKNDRHOFv3tZ8Bt67f060Z7HrUZejq-r_9Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=TQuOWkQx_OxzNvxKncFn6IUKT6q-9CzuNoxdyRfar60mGmxte5wXwEtOovXalOrbMvN2VuqYb3I31ysEbjcZZrs1hwa0FwvrzHg5rRwWppf1RkUX7w0eO0QS-sJoDcYg5ymMUC4lkR9cT6n2a0YYmn2tHQ1qb-efhYKXS3xxP9Bjz_fCQ1_lUL_ATgeGDR28b7NQ8505VQ--Hj2WGjD_9M09jYyg7xvxtxpPTYFep4FmYj73-sYjji-qVLa5SMeoJdATjNqitB-WXXzXFZhCsJ6XHWkaksECIO4rcRGurbtSQAPQCAi2nbeHMr8LUyFD7ntZjQjmO6oJX9D-NF365Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=TQuOWkQx_OxzNvxKncFn6IUKT6q-9CzuNoxdyRfar60mGmxte5wXwEtOovXalOrbMvN2VuqYb3I31ysEbjcZZrs1hwa0FwvrzHg5rRwWppf1RkUX7w0eO0QS-sJoDcYg5ymMUC4lkR9cT6n2a0YYmn2tHQ1qb-efhYKXS3xxP9Bjz_fCQ1_lUL_ATgeGDR28b7NQ8505VQ--Hj2WGjD_9M09jYyg7xvxtxpPTYFep4FmYj73-sYjji-qVLa5SMeoJdATjNqitB-WXXzXFZhCsJ6XHWkaksECIO4rcRGurbtSQAPQCAi2nbeHMr8LUyFD7ntZjQjmO6oJX9D-NF365Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shYm4yN0J969Ii69Ocjee1XTA1CGc78_e2NxuR5nqixJDxb_YiMMZ8kmBDRMuZ6JSOdiPT_83LZGsWHRUblb2IGcDKpYhsxcT05o95H9Wm2J8h5Bw4l6T4AnkqJYYvbdva06qLKs20KRBZiz7wK3gUUWxxKh14IpOFEfDrXyRUjaKurDMVSvrUv2eyTWYTmQPgRlgMSbkUa9XW26vpmfaD4lHT7joDn7JW90PNmX9vL3aP4o4861RCis1nZPf9m-UNj4hgS2qbBL5_L7nLvj94qu-Sk8UJxh6asHjT3OkI7Jtyjt1md0oIGE0wNVtVbdWSt1jFZ5OQRfvIk6SUtsDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afsAEhM28l4Vocqw8BQqq8dxJgATh-jTf8H0AVan-GYhZbzyK_BI2OTEWjbqGplb1xMA0dltsi9ADtyd0eukrRPsEMhrRat-rNioQCU9cRpTbfJulPVu90qC2rvo1lXnRnVMV4DTwY6xa0AaNi3DGTRwQc6AHvsREtCgVgqVmpW7UxH7FZlfcerDqcxfahiU9EQaInvlmV2CwAOa0hAIm4SulT2H5GUwGKeS8TNnkLUQ1dxuNWJF9qO_vZAh54PNvib49Mgx9lBialsNMfkcMJp4laPSkZahtFex1FuRQpTC6nZutpAEDb7ARjcUwjQZKGuqx0lOFvr-UYsYc43UFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTY9vtnjMJu8ilXYfBTi9o4JVQQ8qAhyCUsGRncx9ApIGbOI7KNQ11N9Ut49jdE8Sz3bdFZBP69RHiyrdI_aI4hUQCQbzL6Xnk3GhtzM76UFu_zz6hYmF6kkgfeb4ypXHyAszSI7LAGxCFRGHpRXQdoj_LvsAWFQN7EkP1HkVUiMsYbm0FP--P50vbRi0I4wLmN-LxByPWqeBuVKx2yV7T1zqoyQt9AWBbNbKAsc_eG3HrMH5v8xm9TJopoV8PxafTGedhvwaLbUMdwegCh6PaXTWHRjsng5pLbML5FBMhp6RA3tcK9-sssPgkqIdXJU63jLsYTy8XepxXFh5memBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9IxA-cxFMB2LFNK3bXJGsEEJaoGtGzdE65WncxOJbE3MIDBH8_z-59Ngh23qnCiVXhcfXZfB9kCeRbUPFVXBxzAiZKCGJZP6WgAYzjdVfm-RK9muZQG-DftpMVHneTrkmsGeCQ2NTdN-jOSlROQkpc901Rh4OMDPX2dEeQr9jpHYaeBzkAG1jXr7GhJgGbxdjSbsms42dD7ReApUxR6XiCCkDao66QrllJcjp31EZ7gL9O8Xawg3WcIw8_RxKofdaEgYSLEXSDMNLWk1X_UZ1o8iN7vZwNdBvvVcS2zO3Jx9FYuTsQtSgSWvfpkFZ2mTzUMj_ZvPCQUupenlUrD81lJc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9IxA-cxFMB2LFNK3bXJGsEEJaoGtGzdE65WncxOJbE3MIDBH8_z-59Ngh23qnCiVXhcfXZfB9kCeRbUPFVXBxzAiZKCGJZP6WgAYzjdVfm-RK9muZQG-DftpMVHneTrkmsGeCQ2NTdN-jOSlROQkpc901Rh4OMDPX2dEeQr9jpHYaeBzkAG1jXr7GhJgGbxdjSbsms42dD7ReApUxR6XiCCkDao66QrllJcjp31EZ7gL9O8Xawg3WcIw8_RxKofdaEgYSLEXSDMNLWk1X_UZ1o8iN7vZwNdBvvVcS2zO3Jx9FYuTsQtSgSWvfpkFZ2mTzUMj_ZvPCQUupenlUrD81lJc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BXZY7Q4ROnFUz837qLU6o8yFT9y2r41IutagfRf0EpTUJjw4d5fnla4zhMHxQB9wvzk76SChDYmd2CzJlHQ2vf40jrc-akGhgcjlVXCTgUwNALdNf9z3Yp-a1fXM0KsNwlcJSc9YCzeqQ_hhRyBKRtcVBmHP3hvekCqsQ7lsboWbtE-n3pgnuS4l4jM-OVlduN0hd-s41eImMg71eV9KdQiYFSgNIU-gso2KK1xko9XXwbnYs6iin83lMO7IGUQJr2oQSFzfkkvg8VtOwGcwXD92jKlk80Ek9wCm86ru1e4MVd6VGnTtZ4v9wE5B22Ph3XJTKmgJ9oamvMKGHNxKZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I-TTq-mCGmf42QckIzgmb8HzAknrLIQxIyWWD6nbuMn8xqpM7Io7cjrF8x2F-5y05W2JWGFOAYkBaTyzcuVIrGQrAizpxLIl7jJv-OsXAU-TuEAtS0D0rZcD28VxZXG_qCp27McsqajTW8NTlFC15eYV0CvRpnBUVRnzlnUDo5UoZpfTv3pJ1mKmG2BPO8z5CB-0ZPCkNYSU4KPZfKD7mIrAPUjWLdoKxjpNuBtinv9U5OwrLpQlOsUXoHZiEkgBREcaXihYuEt6mDvSqOQ4cvNbEl_gOzb8wxxTBcJYMd-3kXmg7Qm49IpawEcKsImeMCb9S0jt-i2Z5hxYFOLOwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=j7DTdXlOXvPB3_rtbPZv5C1BvfyYV8-RHmudB80FkZPH7ujfvOnRQGn3Fqt5P10hNOZ0zLDU8S6QXxha9eajx2zQUsGI2vsEVULZm771fOePQYHcOhWDpuKDDoqsVT-fdRhs8BAZbW0NUFddTGd0HorjPg1jBnm7gu7U_xaEmIkfxmS2nzjWRZ4CWGusryMZ0naUx8kiM_qJFFd7tcq1_L4sQrw_VJ02HX_MLRJCUhIFuk8Tn47J_Gr30LJpdte3nDbnPaywToInH1A-pWzCFA_XmsNiseF3vTLAQ_1koqMyhXomXTqAAJo3tk7qQ7yQbRezBC7emR42cajHv7UVcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=j7DTdXlOXvPB3_rtbPZv5C1BvfyYV8-RHmudB80FkZPH7ujfvOnRQGn3Fqt5P10hNOZ0zLDU8S6QXxha9eajx2zQUsGI2vsEVULZm771fOePQYHcOhWDpuKDDoqsVT-fdRhs8BAZbW0NUFddTGd0HorjPg1jBnm7gu7U_xaEmIkfxmS2nzjWRZ4CWGusryMZ0naUx8kiM_qJFFd7tcq1_L4sQrw_VJ02HX_MLRJCUhIFuk8Tn47J_Gr30LJpdte3nDbnPaywToInH1A-pWzCFA_XmsNiseF3vTLAQ_1koqMyhXomXTqAAJo3tk7qQ7yQbRezBC7emR42cajHv7UVcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=ENqe-Irx_ruN8PpUyA_ywEVZDFEyHxd2yRKVmAhJeXrzOqjOVpsI376kynmzIOqzj29QWWraLRe2q5sqp8nb-7mXl8Tvk9sINzUfoMXVbFLSYCEJeD03l8veBZwF-m4iZEtNJaahRzkNEnGAxyZk-bwhC8Uiq5Rupu_CVY4cMlExjmMZvTFhzlKXWdMkxvCV-54dBGbPyUOAQnUvlFWXiJm-LVNk2qOufVmELhK5b8dR-aphrGx0ZCxfY4hfR-usIdwxKrtnIkMDrREYl-su-mRCYAWRgxe1k3eAPcnX0udBgBSuvpnJ7icfwPDpA9o36kF84xFAya0gAfUH0ZWwrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=ENqe-Irx_ruN8PpUyA_ywEVZDFEyHxd2yRKVmAhJeXrzOqjOVpsI376kynmzIOqzj29QWWraLRe2q5sqp8nb-7mXl8Tvk9sINzUfoMXVbFLSYCEJeD03l8veBZwF-m4iZEtNJaahRzkNEnGAxyZk-bwhC8Uiq5Rupu_CVY4cMlExjmMZvTFhzlKXWdMkxvCV-54dBGbPyUOAQnUvlFWXiJm-LVNk2qOufVmELhK5b8dR-aphrGx0ZCxfY4hfR-usIdwxKrtnIkMDrREYl-su-mRCYAWRgxe1k3eAPcnX0udBgBSuvpnJ7icfwPDpA9o36kF84xFAya0gAfUH0ZWwrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlFOCI2cKuBRbHnCcaERmh962Y1YGPZuX6pJiqP-n33N-1st878GOCO-lGZmHlEDTM0Ob-yktcg8_VijwlOu_18YUKJozOBdlb0e5ZTKpVL8cwqjqGUzL3SASIq5nTbAREUw5AG7-GVJZQR041iBQgdXq_HyvjloKj-FefH2VlpZCzGiBK-4B_X9GDdouoHjKgYncuaZCsOKX2GQ7twRTLXc4fdL4rdB-AapYf0xYn5wJzwIXjcNSk3yf7hKqgMhd56sk08DL_xmxMgHgXRmHkYuFXpWvUmKuV9KI-1LM4WPOmPpb08vnXrNq5kX0XNY4ay6HK6Ya4B_nQof6-dKkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PM_NJaEF3tIMPoEa2UJIaD7r_BnwHSF88aRx4OKqdJfpyTbyuqbu-t9tm5F2B_Hj3kKlKmhstTvzFjWUt3-jaAzBeSnxKRs2RLvPRT9TDebyZeoGylRpIl-s8eGfNymI63RtTclclj_WgNRMVKFQTeBcfa3QFOk_iI8GPq-GAXJNOODa6CwNNzpu1BkFJikeYHg98CqKiUR9bHs3A5q8BQEYJgk2yODT6Y6E35Kto1jiVcquIPcYXBzWlud5ViYhyZBSNhRIRFO72Tl3vFasGPewPJv12lPW3wc2pKn95iPNBzu2IZoMbZtOkzHS1aPpERNvvm-ZF4tnEadeC0CU_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=QyHjZAtNjLTVhGtY0KVacPmYQKoZLfXDUMM3Hf7j-7CCJXq7Wrq1jzg8n_VmwG5nG_7ZN7V7S3ebJaO9o_lagCXPi0JdJQFfmIGWngDoOV3_-oHJqDtyJ4QAbx5N-KOV-qBU_e4CT69RoPKfxQvnDgH7PFoqnmrwqForu5Sr_hZovQLUnMOC7OliX34YC2KLLanQLM2Qv_A-qQOSbn2oJT7-iGOk7uC-WEMGDAg0POfgCwOpQwZwnVZ7cF08xnKXmj1nWQKedGUdTuQrucxofV4dWqzxMbi8GqN02uF6WNJP4wsYYgaC4YU2KDgqZEt7FS1olcz1DJpTB7R-BWqAlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=QyHjZAtNjLTVhGtY0KVacPmYQKoZLfXDUMM3Hf7j-7CCJXq7Wrq1jzg8n_VmwG5nG_7ZN7V7S3ebJaO9o_lagCXPi0JdJQFfmIGWngDoOV3_-oHJqDtyJ4QAbx5N-KOV-qBU_e4CT69RoPKfxQvnDgH7PFoqnmrwqForu5Sr_hZovQLUnMOC7OliX34YC2KLLanQLM2Qv_A-qQOSbn2oJT7-iGOk7uC-WEMGDAg0POfgCwOpQwZwnVZ7cF08xnKXmj1nWQKedGUdTuQrucxofV4dWqzxMbi8GqN02uF6WNJP4wsYYgaC4YU2KDgqZEt7FS1olcz1DJpTB7R-BWqAlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا و عربستان شب گذشته
به چندین مقر گروه تروریستی حشد الشعبی
در عراق حمله کردند و تاکنون اعلام شده که ۳۲ تن از این نیروهای وابسته به ج‌ا کشته شده‌اند!
حملات به مقرهای حشدالشعبی در ۷ استان عراق صورت گرفت بصره، کربلا، نینوا، کرکوک ،
دیالی و واسط.
در ۷۲ ساعت اخیر حشد الشعبی بیش از ۳۰ حمله پهپادی به عربستان انجام داده بود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=jiZCpHwevmsjA71fqh4hD0FnvmH9QbBZ8JmUVnn3Eqar9Rq-wfr-2nXBXCSzuygE9gK4rtLLyiFqAxEMUWxTswFVXilf4jmcnHS9WKA1J6ISN6utMvhynG9BvEkl1uvlKtUlPwlbAVib_3BHzImMpjaQp9LtrsIw3eXSx8zquc8q3zONPzj81ADezVtB0W6RsIQSw0fyRU0hRlkSY66OErzSKsjnHfl5xNxDbXs9j5UF5xt_vHP2Fg5u-h5DNcDa3V-Jkv-wZQ5xMOmrMeXhCVZ3DfaeSFd6CMpZR6X5ba1Ku4FPxdTm6i6NsLStsyNUc9h_kFgjvlgtFjJrKpsCnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=jiZCpHwevmsjA71fqh4hD0FnvmH9QbBZ8JmUVnn3Eqar9Rq-wfr-2nXBXCSzuygE9gK4rtLLyiFqAxEMUWxTswFVXilf4jmcnHS9WKA1J6ISN6utMvhynG9BvEkl1uvlKtUlPwlbAVib_3BHzImMpjaQp9LtrsIw3eXSx8zquc8q3zONPzj81ADezVtB0W6RsIQSw0fyRU0hRlkSY66OErzSKsjnHfl5xNxDbXs9j5UF5xt_vHP2Fg5u-h5DNcDa3V-Jkv-wZQ5xMOmrMeXhCVZ3DfaeSFd6CMpZR6X5ba1Ku4FPxdTm6i6NsLStsyNUc9h_kFgjvlgtFjJrKpsCnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ae8E2VHQm2XMksfr36a8lebFeONP-IRPBFwbNtR2guqFGz6nIfdJNwcdS1-lCtkEtKV4sgDrKpR7o6oVvu1I4Euq5OMu77W81sT9u04sMF6jHd_NoTRMGAVmZozWn6vMkVvLBFS8pxgbCeNsQKPkMRQQdzK1Sz69iAt0-5XtEKGEaiIKv-puOgMHEqlhta937H8wp8XXuf7LIy99r4Wc1RiUlFciZ8Lm0PEhC3McJXhMCnpHMlQlO1RSxzeReXPl_INDhKoJtkc5c9EFgiydZ79n6147WgVv-hglmlM3L8TZG1MtNd6bzFj99y6cKr23lhZhbPDl0H3pJQUqpJcokQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iffQ-xV9ME6qEPn7tWMAcK0IfkLd8a2iasbG92qhNoCiJhE4mVelGW1qgiQCBbZnW_w8w7PIKSHPpoE2J6Ktktp8P-9aT54OOUruP1iYgyJWVu4_FCR6WQKVH1U3wQaTIoCBMPB0d2XiUqF0nl3KpS5Kfg512djn81ZRptBUzT4D6trqN6UN2FyZWBDEzYZfkKgpHERA89lnDBk1T3RBNzs4idlwX9rjCSMNvaAjWD2CAdzdGwtBXdCCVGIvVqnemenE8aTSJq5Zt3RNEYlKtvldTtnfFpdD2n9mPKhdDwoosL8PS4BJhEDhRItwzUQJHhu_ibuxnXsOavlsz83q2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ip4bCnheDIQlx0WsTsJFPHqGgcC7ucZiipvoZmi0NMC3B3i36bsAP9wlG1-7GLctQBu-EKnywU-QRrXteJrHRypTJ-7VcySaUH8pdS8V3qHfDBrwuZIVO2xkwGJpGqAyzF900OzKiAX_jADQzNlIndi3VN8aP5zJ7vQn9vnwwGBdlVq9LmYQgpZZIccKzWP9nr_SlDLGwcOFYAF4476fwP3cf5NGwKwn3XGx52kZ7UVM8V-PT9X4wab2ZOfCdL2b8Mj2UH9t_pBoL4boBVzeajhQEY3mUlWsVNc8rZDL7BXnkiKGJicPMN538O9MecE7xfuzfbBd2TPNoaJyFo1i_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQDuU_0aEHN1MhzmyijpXVIUUSCgiznjGtyptQFHUCXpEb6e1OAGiIw5NfceLONka1ZL0uZxPMz0JUvZRTCntnpsA7Zs4Gb_IrlEicpH7wpqbkwNXWGf_csK-9LvAjioMCEcWac4cHyV8iOyFcrKnktiTilpJUKUDBH5uCzGx9hKn26bblYC19OyguO-S96q0uns1-OV78Ea3kFlJq9mjti0PjTJcC7NijTWBVIheTAHeMMqa87fYsyhKmIQzBi02F1jM8vcLj8nUZ4vS56WecOghLF-dAB1qzogwqh_bKQ8TJ67KLvoglZRg30xxEQVtzjxx241QyCfeyQfWHdhLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N3TCw-W6AJ5FzigserFOayVe0FK4XYktoHET3zFfRaDemM-iC1LduN8HAotsljnzloJnTB3o2b0b45Sopdb0DE1LfTB0nP71lARbOC2V0WcTcQzL9KuUEr-4w83dzgRxmROWsR_cMe0lzB2zn2yQAy7Z6Amq2GA24PlXH9cGoTdREOq02-QpjzmX6IxUVQVLTXpJgNUx4HJR4TDvqXoJv9NoEfN9QLCgWkyzkYh8QEvsiyqQs0IvOya7SveUWs1hlmEaAJmoY9kZZpbwCux5DK9AhcOZq4vHICS-qQHO-JqgUyc27ywwM5-au7tLq2YqfXYaLMBL1nq4dt0OYsD5mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EL-IPX9h1f5Rp3f7UXU6sSlCg023rcO6231Xz2KYfxh9K7zuUavPqtx6FBoAuLADylTxJUcXWD0UhcfRgHAV4tKKYb6f4A9tWCBuIXv6i3ttKAa7CTxttBXpjMpsnNnPxKylnCVh0qRBJ9JQNGuO1oOC5idjmi2JfH-1s81CZlRFBwpZN6iHTqfdHp-_wrhk1EIUOK2fG7MIBSyZoiR3Xsaftsz5nYobNC29qFAvYsa72tvr17hxKuppHOZNno0Ty8btSdAwJNfroxk9Y3LEHgzVMbYuE0upuwqcjRSBLDBi-EESGDGINFRVG-KYUbXp8I48YyQKgGl4jFBF09Byqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nYX8PutQ5-SXOaz42jQgo7nklIiN9BIqVUx7mmQNma2DI4lMXzuEr7QcPL-EkhtZvgQH7lVI-D_j8uk4PS-nKL9bmxEPX-lwcuhReGCK7HZrRScOjPB0Jsue5VA1g-uGbmYNc_UqhlP41cVv0wmLJt6h8fi829pfqKi1NRcufLaC1kt3szvsOUAm0Li4vOeyI4GaO93L7bPhdNTGE1bbIIOJy9ORdB_Zqc-Gxb8cSC72h3VIOKVanDgNQ8Yxu94zzcwIJ9OFTRxA-YtpCc0TgHMpm6SyxZpRI-dssRJ54rZ872Z86KsWz2Wog_aPZYBGxAv53JA4pzdIG5NbIEhMcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XD7GlVB29-2M9BZWjI-J7fcOeIXCJaLDt0-Bx2kfz2bWXprrUP3IM5BVPuTvoHXTxB8L_wOfUjZTYDfRI0kHxZNaz1SIoO4NQKHzgZymY7hPCY-xBhx0D0haNB2ygqz39ehP3XaOxGg5Q7KYIz8g1D538ie3y8IRBbIGXvUA3x7ZUwkROaqjlPWeN86JSMknP3QVuzFGzi9NMah-h8cvBjHu2472_ELvCK4n2tNtLHtJhaHVvqnt6UgOF-YmmXdkT-nMiNerxGn4skokYgfdqUqaothHgmlTtpLcPV-BpYyw0C3zCPC_FEcwFc6ztY5aJGgsIhWaGL2OpDsTvhu5rQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mi_qIfFPQXxEFXsd97bs-mUtpLmgJvej96E-e1YfJaN80QeqSJgERCDwvx5b4Z0Io7ukAjzPheG2tkRr73Jui7OrXlf9CRAZB5aeMKOJWwdimEvJzE0vgiE8rHIh23NUuRQuxQP7LGqYpCmFSuZ0WlRgyzmzEpADKzOhMTnmKpEDW0C-uAYdkMcDQbuWT63VhsUVjEgtaMiHLgDOujuimVWp5DlCeW-zm80E8Fuj_RtlAD6Fvwvw_O4BVOY9Le0PrGmNj_vq0rFbpUB4QrpoEcW0Hxd0wfda68fM55P38MobCwZkfjafM_pr4gHJo5f-gjNr1yjEHwWr1y4krfnxQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMyc4yOzfusNwnhNCw5kmg5czPQNJFGLzWOQ27ulk-lBApPt51gxoV96vEqmM4EcSR831k0arSijMzJfuztLMVGXvBahnEXOG1pj_xBhGgeFAhawwZfeoxZlpvRc9IrhZLrIkg66WouhDSSL9mzRZdxDD_qO_o0a18GeZtwWxsaU4qdeU7JJOc0j9L8Mij8SYb-7tVo24PbOsi4AnrE2nDlAHUJ3qE90_2tVELWJjPGFYuRvWeLYFjOJhhNXyT2XSav96lxOvchqgJtXbI6i2Kr9XrhSybjzqKijXUUPmjy5Ix_Af8bNWnrtJ3nQqykI02dP_-0vjh3I73YrEvO3zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=b5EKhgSBhUjYg_pR9CQT_tzJ1CW08TlUw8Eorx6Pw9IzCksIeVguumvxjWl3sQzeD8yItemvwl6oJWcVYFixDMUwp72uFmiu3d-CRhZi2O29Ry-eLSG12gNn7lxv_nW7uwvzTLQ93tjSPREDqeKPnNSxrZPgRDNfPb9qVu3g-tWsytEG7Byhj3vc-0llpncQQzg0_hzbA5a3HyptQPJNrsCHekzqyXQW73P-gZ_KUva4dlS7kWol_G-5trdiroUZeHiimajZuWPX7namk-6t_sREItYBnDggr6SNnbrSqOGdFxmK4u1Vuh9ahNasi9XVk7BBA6R47lgJHXqS5oIZOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=b5EKhgSBhUjYg_pR9CQT_tzJ1CW08TlUw8Eorx6Pw9IzCksIeVguumvxjWl3sQzeD8yItemvwl6oJWcVYFixDMUwp72uFmiu3d-CRhZi2O29Ry-eLSG12gNn7lxv_nW7uwvzTLQ93tjSPREDqeKPnNSxrZPgRDNfPb9qVu3g-tWsytEG7Byhj3vc-0llpncQQzg0_hzbA5a3HyptQPJNrsCHekzqyXQW73P-gZ_KUva4dlS7kWol_G-5trdiroUZeHiimajZuWPX7namk-6t_sREItYBnDggr6SNnbrSqOGdFxmK4u1Vuh9ahNasi9XVk7BBA6R47lgJHXqS5oIZOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=TMW2wmZspdBMTQ4WIZWkE04ywiJ4fvZSY8Ul_8HtCSi_RSgfn-LsN7xiYyATucaG4o738Mj37oYhOlroQ-COOJMw2fOhQMIvOtA9Wm1C-FVD1HB-3T7gqQmGF0DIuPMJXX1ND4vmDIO6hLygl5-iLXUVtKGjBi8dJJZ-F84JXJ6WbHb9UTP2b7O8Njn6O83BJJeuEsKYnC9FVs22l1mcRjd346P4CqB4lUbUa4XNUmnEDCYGOIW3q3TeXVUBa6VCY3hYiB32dcaHYUU3VmIIt3IHz1c093CVlWTuBZZHRAe7AjFqHvmNrm8iVigrKAiZ-cMlcyjEd3we32E1o0MGrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=TMW2wmZspdBMTQ4WIZWkE04ywiJ4fvZSY8Ul_8HtCSi_RSgfn-LsN7xiYyATucaG4o738Mj37oYhOlroQ-COOJMw2fOhQMIvOtA9Wm1C-FVD1HB-3T7gqQmGF0DIuPMJXX1ND4vmDIO6hLygl5-iLXUVtKGjBi8dJJZ-F84JXJ6WbHb9UTP2b7O8Njn6O83BJJeuEsKYnC9FVs22l1mcRjd346P4CqB4lUbUa4XNUmnEDCYGOIW3q3TeXVUBa6VCY3hYiB32dcaHYUU3VmIIt3IHz1c093CVlWTuBZZHRAe7AjFqHvmNrm8iVigrKAiZ-cMlcyjEd3we32E1o0MGrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=IOtSu5G531VxXbiPUdKfxyZDmQlP7p1znIiNT4riIUmPgzr4uw_ycPXN84D_s7P_4BHSHYf7iAvHbhHU0DV5CcT4snOXklgRRMncQ7Hx4Me8A4qDFkyZ3-8_PCgiPaMV1TG2jbLEI9NIIRGVI-CKIGxJkfZbDt0nft8_ZfLAzq2ocjf4_yiKDTtQu1C8GQMal5NyqfP2OnWuWo2V-cDdLIhMUoOFnjjfkz7mSCzKYXSFb3o5aW5v-Rw9WJo2Wi5uo3g-T-jvv7Vt-_iEAzkl8lz2mUHaRWLuAOEbOXqsR5bOClvVdV6wbyCUVXyCoYTEZQbmb5ZMqZm7dG3sXxpkDUcDq1nn-p_0Ckg0ko0zMtz61FJCDJfTYrCS5Az-nhXBc3FwL7zFRzTUHxSTQUp7abYssD3VorG7xBxLsRBsc1hC-IdOU4KqqrSmhvxv2d1_ShdyesT2EwEBQ71OmxNhYS_xT0i20uWEpOyBNZYUsbQkT7syXA6KUxINWCrncn0_6Tx7wuyydweSo0x4p2-fHFBGOuEFI0Uh3TljEHxIyma0WKUZy7Mp4URC5EhgbR1KILqLDdSmNrpqg1mWl8MHnsZbGciT3aGTBVFnxa3DKdsJmApc3ni_xzzAjDipXZVy4Av9LYK-gfxAHkEjO9d1k3vmdmFfOWCJRwUvXOfEF-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=IOtSu5G531VxXbiPUdKfxyZDmQlP7p1znIiNT4riIUmPgzr4uw_ycPXN84D_s7P_4BHSHYf7iAvHbhHU0DV5CcT4snOXklgRRMncQ7Hx4Me8A4qDFkyZ3-8_PCgiPaMV1TG2jbLEI9NIIRGVI-CKIGxJkfZbDt0nft8_ZfLAzq2ocjf4_yiKDTtQu1C8GQMal5NyqfP2OnWuWo2V-cDdLIhMUoOFnjjfkz7mSCzKYXSFb3o5aW5v-Rw9WJo2Wi5uo3g-T-jvv7Vt-_iEAzkl8lz2mUHaRWLuAOEbOXqsR5bOClvVdV6wbyCUVXyCoYTEZQbmb5ZMqZm7dG3sXxpkDUcDq1nn-p_0Ckg0ko0zMtz61FJCDJfTYrCS5Az-nhXBc3FwL7zFRzTUHxSTQUp7abYssD3VorG7xBxLsRBsc1hC-IdOU4KqqrSmhvxv2d1_ShdyesT2EwEBQ71OmxNhYS_xT0i20uWEpOyBNZYUsbQkT7syXA6KUxINWCrncn0_6Tx7wuyydweSo0x4p2-fHFBGOuEFI0Uh3TljEHxIyma0WKUZy7Mp4URC5EhgbR1KILqLDdSmNrpqg1mWl8MHnsZbGciT3aGTBVFnxa3DKdsJmApc3ni_xzzAjDipXZVy4Av9LYK-gfxAHkEjO9d1k3vmdmFfOWCJRwUvXOfEF-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xr4erSRhn7NY6-ymzv-Na4w_ustX-EGwXRTiXAWwT_4XOq8ePNCt7hzw_CdFuGg-iqRbhlJxY-PM60vLyo4owlwNM2u4ogUIQ3CI03MN3sIMKJd7SbJ4J02tq8zRQLfGdMe10TG29Z17aTyCKcmedVHBLKF4hYZzmv7yMlQ1rbhtD6boXCV0RgI4z4ymjoONd4ArHqlz_pKEVOILEzH3x2uWuMwT61T9Cduj2Dnl4tQewwHE9e-disuDAlM5JMgIvR6bUORJzEKpvYJsXKf5bA3JZIG-sXmUgPDWlVp6E6xOayS9TtvdWx93iheb6-ldTGV3YR7Uwbolrr2pfJzP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=oA0j48YVrHc6DhkAmqZAqux0BDEjV6YmIisS-lkIZ_nsCvJh2wr4yOGjoJwN6BDGtlJY1JNUy8GVj7OmAp8JXu7oaeXwn_UaY01ud7QTe6JM4-A9tB2DRFWTK9Oad0uRQiDuDMbLzLMX_71NZ-ctXLtWo6E_53Y-3JMxaG06btFpEKJ5XYthdIYlGI_lL8HwzrR8C4NnLh18mcDnWEp0Gy4blSOd3J0YC1yW4ftDb4ysx5yc9addGa-nb0-797rCG9NGag_iSnB8CcJKMQvq_46UdvsmIh4wsQ-HGubG6WoXWJMB96sVQqlelmqvaBce3QyC2ca3jGuHqjQS4R_rrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=oA0j48YVrHc6DhkAmqZAqux0BDEjV6YmIisS-lkIZ_nsCvJh2wr4yOGjoJwN6BDGtlJY1JNUy8GVj7OmAp8JXu7oaeXwn_UaY01ud7QTe6JM4-A9tB2DRFWTK9Oad0uRQiDuDMbLzLMX_71NZ-ctXLtWo6E_53Y-3JMxaG06btFpEKJ5XYthdIYlGI_lL8HwzrR8C4NnLh18mcDnWEp0Gy4blSOd3J0YC1yW4ftDb4ysx5yc9addGa-nb0-797rCG9NGag_iSnB8CcJKMQvq_46UdvsmIh4wsQ-HGubG6WoXWJMB96sVQqlelmqvaBce3QyC2ca3jGuHqjQS4R_rrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZHin-N7lgC-LwgFXUwT1yrAaQcjfITEHyUYKQpCCEFJnt9wPTHSR0yaNrRuSVmviXWNvl7iW6m6cwHDs7mD4MxGBy8ls8kzjmbboUWsuuQG7RJ3F5Ez_rbmWNAOPhSzw2GwEohQ12WjYimfDkE6wuobbi3J7ezBhbys12wECGyAZX2FDGbG_-Qpw7cYSEs311YmQyPjf6V3-K9Pih5qMEv9Z0lWpt7bssNr11_lddGYaWPv5dPXFh4nCkeq47VrR2WFvaQklkxdpSmshi9yJFYBgTBDjT0dDt9Mi7ZBSfnGy-j8VLuzBlTV6W_M_1fWm_Tnwzyf2JCR_SqobBX_xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIN8jYRAwZQDEefy_zYEDdoQDuqKIWq5mdJyGAVM04lBxrFuYP2l2Kh5JKsdag1jZopwaagWUEhXyctqr6KbISfNtePWRCpLhD5oXg3RJQ9t7Fw0XE4Qe3x7PcWd1RrXlL8dZQrTcX63VoI-6Wt6aZ0vnMv4wT5VZCyuZ8DQFHY2tKv4q5fbGp35Cgqs2R_5u2Q2ookXiGjCmdDpp4t3R4-nJOkVmSnpGcZgcHyW5HM-3_gm6ZLDwlmLtPdl-jcA12lZ92A7KuJXpDjQo6RwqADTpIR7AKM7WAe_7_Z-pqrnfHbMpv4coLazXJNSar7ncgcxy2WVV3ORO5FfDK85UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JBU0kuUGuIV5DZ9T0pV1qWzsdSL6HmxLQtrU73R4P9zFqH0-MiVtEbZLSvdWBzYJQcYN8-82fRXUnryUWI6RzTkSIpjU0Skdr34cLRFwpyoSyhqYmiU-Le7jACypJ3WAu6LemXB0W7lZDi08B5Rdl2ONNSNfRuibrlh2CxPD01qv21MDwe8cl6qU5TSno-m_m4Cd-i159Zcp3I93TQ2assBmEZXu-7FRZvZMcZ-Iwa0DUfjdZCbHiHISserI538g789RRTp1HuF2-taSVE7Q1EBwJgzHcYUU0l7fSlxc_o6Vcfge0C8tJw_wxYmjKQ-EL4iSjxZsX1mKM8cLBwwPsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RVYkdB0FRJ83NFObfGzH8bf8xCLSmngESrQY8TXt-0ikzQM6WkHWV1tpjvJS7-oXWwTm7sApLqRcp0B_uZws49lwiVXV1xjcTamjhetyjjT7Yd8iYiEuIvkFIxbBG9y65Giy0duCbAwOwKvSOxJkE5WGEFeivBDEyCz2QvKGa8Q6N-e-wrIyRjUKG6ysq2A6N7d550NcSDXkoFixG8qPDXLcm75l-pbHXLPuEsa3vCyVUXtykE197BXtpd3ECNkFEhjZt5TjiJ4Sn1Oi_EWpBJZLYKvANWMO_dCp91jVNgAjoD4fkjpabkBTUmM8B1381-4C7PG-IP_j6QA_0eRUsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fR-CkJ9q4Imvpi0kct2pT_mLO9WHdeTF309vZt5Jn-dexYpINuwhhcfSlcRd94iyor8qk-LbikwzQRSZZ1yXudMs4_LVgKfbVnNFsLoGp97amEzNEc_CpYQEQJJFZ1duovnIZiCqFxA_814yJBJe3hKzxMpc6ExlfVwVBXOIzMc4sKWQUV42CBsgUsr3R7ZHExl9zLhZ9mZb_Hp7WNlHdiNGSn7FLCTCZ3pauBOm7p-o2Kkh2bY8-Mkzs2cFH3EV7rnOsjbtNvsZhYJEbxrmUyv2t4iAEZdgo5ixlDgBhNUxmVzuR0F_-n7JxpwWNbtKx9OQCveV010VTOTdcA48CA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANDoa-YDVTDoTDSEJ8_mVkmoSLuimLdCyimckb4kmzCmn5V6puLaPU30FSmEkj09ps1ytsWBBx0oUj46J51_fDuf5DoyrN5sifyNi5QnryuPGKS3rbdFE3ySEwYiKgcctLvmYI_9BRUs7tuFEF00gSQ70f7GWvnho_Ip7ULlkVduGRhDi0Bsidpa91FDem1pjWIrVFu57a2vJNHR2MTBvRd1A8SpWBTlKko7vFh5pHjrbd6Dyym8dccqOH4QUUdqNJael8PHaMf1PGYwTQU5R9-3HYq4jBGDhPh-Uto1RgwCo2f1t028SOZoFMLYKocsF5HAiV4ntw2DcbMyLv2y-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UdVV5_s6fcH5oaqNDAsNqpZOTSAlt59VIGgG1lc-t7ANlemNVxHM5in3jrlmewT0UeGdCtJrmSMUB_Jdl6RyMgHofkrzhzDcfgaVUqGmO-SeT4PITwirUWKV-dkBi-JPjNPlWtlh6q77dZHibiyuEOGMTZX7BtTrsWdsYHaNWHZ9F6ZdGoilzY63U3Ywshfl5ll-NIg67wEFk1WEY8TY093DQbJeYcyRA6mifPqday9gPAY81YyFIH1mEOtGfaQj9rwWyxpfnccTn3wVV3E4WVg4j4UdYeDHGIbEiCveM2S1yWSKHv1tSz1XaXYD5dS8JT1Pf2yvgOz6Hpyt9HEIZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W9-nkyNxvX04dSvVGapSL7tXRAtoSkBqvVebHr9vcSXNArR_o0wauR-GRmgAq65dHgNxTjSNhPxyhF19RKB4BJmxAUnCnBMK1V_PQCQi78eXqqYdoW-uDcjjOn3F4F38iIgq_0rE95Oc33NB6E_929wBQK0uet-dYrK8ImVT6-bM2NuLjggQvPvhlcbhnvV25p0c5dXVuf-8USox1tFX0be2tc-kKypS4V0PAc1IoGWSb3rCJetq8YdO6YpX3zilGDYfLGhvWoeZnDuAI55tHAPJDqti0t4Nx2NzeivrPkGWkXXhuroVWjnzEIex4L7iDMW_kxNkMx2l3Q0mwlDAXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DaZGkYfc_zJiEyRpAdqYII4FM6eEvJCw2-vG1rpt4J8ue4niUEpJHtLwkjFtH6fXDLf3vNV-1gt0HSMAERvqd8AISghL1rEqa9JQ0xO5AhPOBjk51m0gamn9nYRzuWSAC4O7Ck0aJwfup2LReWep3sYZj31sZmBiVzc7G-sx8v_jWmubtHXv7SUtjTDEZuBGsBdd5EHApeY5l7Xe19uTOv-gZzBxF_p0tvthsM10QRzn60nNG6-qSfbq5UjfbK1dUfuwhHYDvIutebWEGDle212G2un_AbwWBtON7BYubOIiVJMjeRH48bP9DjhRnZWrElStkN-duC7NQI1bjAyJtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iAzPfQFNHFVyatSf52QXey-CPv_GWGVRn4WvFiCubpcff-xoWOC95ZhJ7n_x0u-iZmEHQAqD3glFTkHlKNs3FkXx951OaGoIbkaEPFLy8KWCj3wBW1cqTYPEwKgPP_TqWgeHtM5T4HT5L5sAZxux84wT_TPRg2ReNZ2CR9WcoaW1tAyVQt9KKIIFPzON7THrfyvd4xiY-Ic8p3CuTKN2t1uKHVte0appp9vmgLczX9sYX4Z84Yqb-hhcXFAVRsK1ZMgmqGb8neIayb8znSyS1lkRnO3nrmanp_cp7NH-PHo5_QymN8Io6lTOfTmucMIHKfojoqtY0aQ6GwlhQCahuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWGImv6nk81687UdeGi6WjMvCApZBXZ7hoxps-o7nJEBLJaPhjcg6kH2NNBEw49oNfEDtF_9nkYSEM5oWwSaI7YeHso5_qMg2-e1E2_io9EHmYqHbijWRGusg0S_dYUbgiFj5Mjl6E2pwdekJFqIU4LHb5Lsz88xGz2nO5sK5LojXToIYJprqkXN0064_kHyaOgKht5hLaJaAvMODbb3dmpgJoqYfu8dkk4KdDpKCQ7NEqNfjZXhLWdOZ2uBNHN_m5Ex2ytqb-tkgdnHZvOi4K8QQ8Xx5cmMRkNkZlIni-7qVjUR5o-QCf2Zta5m44rS6Vr1xhXgR2ScZ1nJxnwt8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5Ov_StfbNil-WtRK3zFD_U-Mv3_sIQs4sSfUdkHsInAJg6Ucbky_BBNva3599fIY_dDAXmKsadtkBbAbkHmuA63QTXoQQ9NJXysYSP1tYFS-pXcKEH7PTc7O1-q08g6n-EAogPchLShiXzqjKQFoIvXvbdfDGCuCzpV0YTLjX6yxHhgY51UuJtfIpKNmLg6XdX9ATBFSW0W0-Jsy_TDRdUC7TyBWSz_HspZmsP7XO0Kw-0YUFawcEftgEQfACk72it0T-RVr7hlLqB-agVd2e69GNdUta1EX0f4-95zlAvVEcjmMUfWObHEgJcbuQLp84gHp7PUTC8fIAcj3vsTNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EI84RHkdQEIR2Kl1ca7wQOrZ4N2U6Nj3Rd3GXhv40DtVTm6gYsE3k5xyyWaBWhGFV2B_3Ez3TZ4Duuw3tampmk3eAs_4sJkUw15hCTRKzr5pZBbVBTn5wrCMKtLXIvKSfyFWmYoC3qeXqr2ll4WEgvuYAIRTXXjjMSOzc80Ptd7OldsV-_UUFuhVMdG8XXUx_OsfrBQK1KfTNjT11yRyx1yZN3dZ6R_jneTbS_WjCWmR03CUnGHjTePvQVQ-ArmeOhHcXuwA5jCg4aIOsRk_p-JdBToiCIBzr6XAly2n0EjeuHyQMEGB23y_iZFSDC4kVyJcCXDniB_x2vsm4_P8QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p7ZjAdhFdhgxTYmK8a1VjH5TDRjpJDjUQ3wtQ6f2jg6gFlXAi-LAgqoKP3llZx-e18jgIVz8lDKrJr8FV01natH2eUlfztb1BoqjBqbyQTjdGp_sdnlj3bnCq9_t5SclvfORBGf8PTpieKPFG3UA8D-nFVLdGmcM_ThHZue9e-zIM5-UZsmshI0vmqmp0Fcb7ykEZr4CVcP6pvqkSizE4uTTt92OVUXMS91zswT0w9YtYnlA3ENI9vGJo_ujJ2UY7IJiiEQ6Ft0ATsZWYMjQjtYz-3Spp8vmwlyVuTQfUyrUQJDSOVTsKgLpnyAQGXGaT8SlBtfC4JborJB-ldi-kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GzE1fCLD_6Nm0hcd8M2Gtd0EZR2PNbRcoMg-oJbL-BgrIpvJh4VgBdmAeakjw_tVak3sA_8nv5XqujgkEM-7LQ-0p8c3YiJ33__CwF9l0GpkQD1xqQJvhQyLDsMz6TSfs114dMbx_ISvAeAAL10Hm49lchuXLfedDPVgStDAfkkW6CSXI_Mx7u8oMUd-QWIkirJW4_CVIlcHVU_IsC-7uq6PqNhAnJkz8weQyG6z14O_yeoAzwUXV1vKYkHBNVFPuwO-3icKB7hld4G2bsUY_EMlnJgUd-sz_BS0mqUA3hyVpgZ6GWnhudk-V5rHS6hltktupBr5fxckZOe-DfZgEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mDi-hsYh4LQLo-vrZ_yGTgmGOdTqrVhgq_qoon8mVpAdcr7wfBiYBQW6zxlJJY2BR8wr0A7yKs8PNCUCHO6dC9X1LKrBNXEcQTahgKG1G7_E9WJxKvH9WCtdZWvmrWYUnA5vr_JMPQxn9BbnC-nD7LO8EdU3PR5LzgWx-ujNE6Q0bVON1uGxIZWps_kp4-AQ5qXTIDRq_oskBSSXSBfLPCF1AN3ct8ENesBRx-pJNd1twcUV4JrpJ3i83hm5-eFsoLNTiZa5k6xpPVSLfp4yB1swo2-9TXPiFK6VAikAsD8WYKT8KeqkziI2Cdm63pLy1PEQg2CnwbncO_SAxcly9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLBY2gTYIkelxCpXooYrnHifN_Yn0XhKwxjpMPED9sqcaedRfLzQJ0IRpccUxDIKHniQpCYK0ywpYhEnWMt9m6PaOWwCWxoDvOdZ237kKdqEN3v9Icbz9L17ANthLavKsTpvMvhZQiHKmLTFlmbQ9gaKuXMfJXyX1k3G01iaNpNChSDO3UL1KnwVkHBTaopleS9CfR23U80AKRrveNClFFayChA5WTzEsKNQ1y40Jl4JKQ9JGIUtUV2X73qeU7bC6p35JDdhrS714NUca_qxPuLvW2Wj7SJCWW6IbqlzPprxdGXhmZG2ttgc8Wf0-1KodfQYMZVlEzPVvGjp6uYoow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=AU9a4xSE8OWEchPPsg62I_oL3LZO7X7KnTM-WmhNxOsk_p3SFAMaWFIAkfJdqyG9XYDJ64oFBIETIaM7KXJ20cwrN0HFRsJ_L-PGoJfbhU7u1V--0C6VGPMyFu6SKC89nFB1cJxRchvJ79Wy-E2FZH7JifehrOn7Xd2h_zAaT3vWisKPFexQfNCLdY3MjH0guVxbvvg0EAvjlJ4vJNs25BN30y0blnmvklEvzKEEgs0BeOkN51Y_Op5aTCvINXO5pYFueJPYcxtC3ir9viNu3s5mzZvOlQKvi0_b8YRdFa5xpD51koCTpfpXyNMhKfAoKPoyTngarvfWSX2PU_y9LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=AU9a4xSE8OWEchPPsg62I_oL3LZO7X7KnTM-WmhNxOsk_p3SFAMaWFIAkfJdqyG9XYDJ64oFBIETIaM7KXJ20cwrN0HFRsJ_L-PGoJfbhU7u1V--0C6VGPMyFu6SKC89nFB1cJxRchvJ79Wy-E2FZH7JifehrOn7Xd2h_zAaT3vWisKPFexQfNCLdY3MjH0guVxbvvg0EAvjlJ4vJNs25BN30y0blnmvklEvzKEEgs0BeOkN51Y_Op5aTCvINXO5pYFueJPYcxtC3ir9viNu3s5mzZvOlQKvi0_b8YRdFa5xpD51koCTpfpXyNMhKfAoKPoyTngarvfWSX2PU_y9LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByXBWAW3BO5bQBo4hHCAq8JtfdPfYFOXjaXNzrynrmACF4wUCqtc3NF_H0rCpC9Kl84pNv-aECclpKifMcbCGs4coYQJEsAzPUNqWOR5_CiKFbYc7mQJSDy1KD42Pnk9oijWvRe7YLen9Kc2HwR9U5noX24ujznXbLYodXUF69dBhjeRFWDBlJt0xiaGdwBFuwJ2gS8N66SciOMDM_4ZjAY0I7zDQpGNanKmCjtzPCEO1KVwSgi_OF89LRK_5-PZkZ4aAEZaPx4B9ZNUPODdCEWDFKn4nPvb3BX3NT6q4UoG9UfJNoH2nrvQGvMYa0OMS6qWP854tZ_7vMC0wkWk3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWwedqMQ2cbDuxEP5v5mwP40wy2TXt-kzjh2ybEsFWN-HLn_i-m_z2vAjcnbOPPugVb-0nNJ5u19DnrGSgPUZi8oB5zaI6rtpqWYzwrbtlmC3SxSH6jdnUPCaOJWtKQmkCoJLtLjBQzYsXenQlQAvVp815FTQdIGS9uJRH3diw1w8LTfq4k_BdpTpqVPYkvxie9Z8HJkDPi5YIg0A-ZqbYp_DUAnuOmXaXLmRqfj1KYCjuAnSrhcZ3LmegwtXnRzYp_3ifQSFVVBTaxpuKqfTQBwK5Q06CXVc3fYNgjndUtVmOyrgm3bgu0wawC3o4H-wsvfHfFJJ0SMh4n8-DdbGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-j4eafosAiSIyBn07Jn7g-oncLAakeCE_vDh7ATtEOU4otBYDYD7kX_dwRP7phJL-h1P_xNLTKTc9qjS4KIeOSdiS1VF8Xzyun4k1mxc7Bv0SVC8FOct1e6NH9koiPOXYeB0S88muPACfxCboJ8FyuC3Ke3t1E6plyMTf5iOti-IVdNeRSeiqWi2GZ-O1K9F5QOK0L56jWBYdFLEXcivxLGHlhXp6_5WXwU4PkD4A_Ec4APQ5HW9ANVuESHYYh7sV2U_ikNiEl5SjaNN0Ygy2-wpY7naq3PxJVrUtDqPfc18ubTpvD7cHxehwSaz-a3iy4nkaxIbgP9kJlQFCyb_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دو روز پیش صدا و سیما،
بخشی از سخنان پزشکیان رو سانسور کرد!
اونجایی که اشاره کرد که خامنه‌ای در نهایت
طرفدار مذاکره شد و کوتاه اومد!
وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که
صدا و سیما مطالبش رو درست پوشش نمیده!
و میگه یک گروهی خط می‌دن به سخنرانان و مداحان
در خیابان تا علیه «تفاهم‌نامه» صحبت کنن
در حالی که به قول عراقچی،
این تفاهم‌نامه، بهترین تفاهم ممکن بود!
[همونهایی که موشک به کشتی‌ها میزنن
همونهایی هستن که این تجمعات رو سازماندهی میکنن،
اینو عراقچی هم می‌دونه،
همون‌هایی هستن که در صدا و سیما هستن!]
قبلش هم صدا و سیما،
بخشی از حرفهای قالیباف که مسئول اصلی مذاکراته و رئیس مجلسه رو سانسور کرد!
(یادآوری : هم قالیباف و هم عراقچی خودشون  از مجموعه ۳ پ هستند! و باهاشون اینطور برخورد میکنن!)
این دعوا از اول انقلاب به وجود اومد!
صدا و سیما شد ملک طلق
و منبر اصلی «ولی فقیه» و شد چاقویی
علیه دولت!
حتی علیه خود دولت خامنه‌ای! وقتی
خامنه‌ای رئیس جمهور بود،
رادیو علیه‌اش یک برنامه پخش کرد و‌
رفت گریه کرد و قهر کرد و…..!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
