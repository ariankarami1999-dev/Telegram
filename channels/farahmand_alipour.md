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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 22:19:56</div>
<hr>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjOPiJkM5-EEDM6Bj7OV6FYwa6uuVXOBiL-mXDklkcvICj9qBgt2UZtADLR8kiyyeOHfyQcn0FfLZdo9ahC6WTCE0Gy3eF6J_AGRCc6jpnP73GoufsqCZZNizMdGkZTUO49khBUxM4Y6TBU2vIOrdghJElvyZEl5IEKOaMh7yuWN69SA0jg0l0idBUPSC9aBI8wPpcNuXekSRjEz7Jvd8TkQdToAqfOjoCcsa8Qgze6YuKR176p9Qk2dAQHVGpE4zzljhITcIpBkHsGB0OiIhUdx0VZqTRhxzBzphO0T1rgW6byolugK1p47bRTt68SFGrPMKK28I-AJjm0aM8p2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjIQTM80iQK69zWeK1zv2hRR6NfL3wncov7BnLo3ze6n_keZzpyBK1vl5c4KapxAjE3O0y6vVlg8WgIA2uFu9ji5D8zywqX9ho0Kqvr_2fcYIHssdNypK6zYLRgiyV7lmBr5XMuduQIcUo85FnSXHKTF21c5j51idawfac2Bw0DCD44sZJZghFvZwzJqcrlEZlB_LW6QE5nHkDmtkH6fA2YqMQG5HTtD6v8ISDpmyT9QyyxsXk4wN47Lc-AqMHkeTwWzW9uARkCB7smN3iFsM1nEqy4MCf1aMQk7sSZ1R7i_DyDjHRlIHDFXBPsmRuiUmnO9GAaYzkOS1EObA5m8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5SNeWkjycX6gsJJwtvo20Mpl26SZZjX19Gi5my1d3P89yGGHjNGX5Nb7B9HX3xHy1hSjl1LHA2YguAot4MmdK9Iqc2jXoJdEQJuGH_hl_a6SzgMO_5Q2_Q4ueCYlF9SWiYxniCXq7mimIN5jvMhQL8V-LgiZPrRMmFrwC7D8xQOkAVJ_jbDkFDgbJGLV3-I9-I58jLC6-5e9E65UTRvfMOvsufXjtX96ST-BYDKr1xk33PWoaF0-KoIJbmhf3vHtfYb8KpmjX4H60z4_JGadulFYnxuXRxALiwZYDfx2YkROe3M9MjCs44ByzEDodPV_Qn10wxXaVt0y3ID6TVyfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0dbeuUShWM30A_kcihgPofaUCtPNvenAZqq6Y6HkEQ0PEo-xt4qg281D3PmxKVo0S6c3h5XGhG8roFn54Osm0dfLCMx1fNM_hRpo24dJrmZdIImiAVEEGl2n1Asn5OaWQtL_Rx9fHVJ62o0Ml6hs2t0NcQ9RKKXIvTPQb0bWDzKZrxFtDLuS32HRey8R35BESCXF8ZoIJfE22sRsn0N0te6LMPVJ3KwEZUFjyPtTkcI0P0XQiZwGOt24oXXc8qmz5oRQy2tH3uLEON-I7dvVbMOtYa3HajQA_2JT-widb9tMdfT_g11s9psXz7OkHnf30w6WOZur8mdeCB97sDhYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0zeHLwcL_94UpOnVwHJeR-SjOVAwRNEQoorPnaFWQ1ohNkbzQK4p3iiQl9uEkdgpLe2LnBgv3grpS7bFiErOV3cDg5J7skPJ1Ki4uwUSIpNXd-N78Xy5XMWlb_a8QerRDqBcjhthQRFwffUFxCic89OYyk1zoGFsIXSMCqWdSsN0Z3LWgw5PWsPkrPTiFta-EksSqP8n5_uEJdZHT4kK57drrgogCbn0DMDAxQDxKE7wC3cItTpLv_N1J_jjecwzBtAtuuv3oxcuQ9rcVjp2y0oUeZUXqr88NGUkO_6atSFzTMtaiZB_ti_i1XeA0NO4YNHIzjrFR4kBNQDHyh7Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5P76CyG4bVOYZoppovkF2x3KEB2a0Bm8ajKs3D4u0xTvsXMf4OYFfV8M49NvXT8IRKwANSh1ScxXHMGskLkujk2SYWBPtDpjAl46UvK4S6OGqAkva3ZEpS3CXjeC-0eeRqDuptKGmQMtplBiRMhwiQsMFKcUs2x2HNZDlMo9_W_qMjhKWuJuhLkms754rUBXzBsSDUNadQsSWxxtfC8x9dERl6p_eYSw6Z-mLIfXVrJkUEMp6j2RQzJjf28ojuskHK9vYH9r_WP4hQByAe_OxxpXnf1Se9jyYLQpR4bRv3un-h9NdgIAi28xGbzwzlkITL6IGlMWozSljuzOyEVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbjCfFse6t1YbjGml3SlfdHI1-j75JHeGDhn4CS_Sz-Rd--b5MZznij5rB4fQ4rEKfwImdBEWA-mRXcsH0yGj4aSfxDjXKmsln8BTxFIyRyf27zQwZMl5Phoen1u2BSs-VNlElHQzEHHRLuJqzEbHgJFBpglCiSpdMe3gbomE3CGpb1yXPwMsydJY8PR4jOBjywxPBDamF1tyPmULlV3w2BgKY54m-6EcAgSpIZ2NnxkQHMUws0yY5A-jGdlu1A3uzjBtvABiqALg-v8C9G-MZ_Sn4QaMV6CaiaelQ_J-JpPbTah2xg8Bp7h8loPSGRqbuEO7jK6KHPygUymChN3bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7J2uektna_ROR7arJuz3sTUxNibt-L5yk6xtiGC-aDTOMVZt7f3BmrjUFNzp9gb1NefAFd2LdD5OIVDF4UlT7hwuPmZDvyTp9V23QYKP7_Hh-7sCzmitD2bxeuH-8fCc_UwVof-FTkPtM1fIhjIGjZXoEjgDorN0iwBlVphf5BWXMbye9bLIbQNnQaFr7Cc1l-cSujr2zAQUypNGEnGgT6Ni4Sn63Jz7QIftEl7ser4pkzvXK1J6fIbm8LdWSiH1t0YW-8wdzR8fiMEvA5Ge7vhD-O8gbi-nctTSH5ZcdvtgGUGcu4AtlSiQXylTUp-U_ZMHkothw5yMB7CLA4POA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzplK5f28XodfOAsA_ylJJdCBmjAquuDUzgZRrmVfnV5Vbiqm5740GHpPvCeldx4-H8VDSB-v9Wnr9mJqTq_dFRSicj7NDftDcIk82bat5cVa2izNg-n6nCvx8To8vf8febN4l4S_0UuBGvoCVZYgmpnOxZxKA_mq4y9kPjVem-ocqXX5caeQcSJmLx_5wm16Al-_lOIMKqR_CAxw98igC6XzwPXiI_nkoSG6AOHPT7SpXaghYpt5ck67skuRMlvhbfBearnwPWsXXLfR_m8T7ZkCSpoCKvYbGhwP79KNRgTOQDlKfysb6xGo4GOusl9JuNKTt0dG9WAHM68m5ip3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5bZ2KmJtao6yntQKWjPwQle9fMRmz-HU_zvGSpa7wmmYc3K_-muXjoNoBaxHwVAIKkgfxnLpq5BNdHYT6ehDjPUbuWCHmbK4BYfK9iWwgLbaP2BgVIC7yhJdvXab-koOOKJxcOin6Yqw5I6haA4HNbcHprjicAXn1mmbhPZai8sfnL5-cqx68-3AnMcQv8lDmzjU6AB5znp2Ai1qjo8T_1jw1vOtf7XMWCGS_HvsWPbFJSHWeYfp2OOZ4H21MOjrEX6HN5fYyGFTky41zN3pFDGvnXPhH0386MbKo8VlwKoj8WKc0ZVP5YlNEwfBArvKuZvZJeYTpjjKzMu98vJkHAs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5bZ2KmJtao6yntQKWjPwQle9fMRmz-HU_zvGSpa7wmmYc3K_-muXjoNoBaxHwVAIKkgfxnLpq5BNdHYT6ehDjPUbuWCHmbK4BYfK9iWwgLbaP2BgVIC7yhJdvXab-koOOKJxcOin6Yqw5I6haA4HNbcHprjicAXn1mmbhPZai8sfnL5-cqx68-3AnMcQv8lDmzjU6AB5znp2Ai1qjo8T_1jw1vOtf7XMWCGS_HvsWPbFJSHWeYfp2OOZ4H21MOjrEX6HN5fYyGFTky41zN3pFDGvnXPhH0386MbKo8VlwKoj8WKc0ZVP5YlNEwfBArvKuZvZJeYTpjjKzMu98vJkHAs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnGfTNNvyU-H_T9dqwvde_iM0JiYB0ErByd11Kwq1JN0vBxM2wrbROGY57_6Iq3NRo7VfxfoT-3AD2MVoiW9rWFSd6tChNW9V30ahmfdsSWc1GQbNziq-FNc6sKXiDoAYzQ0ksWYK5fnDHlqGkcYmQhVAt94Ox6IimhRZgD7VZSwKtX08SaUeJhJF15Z2Y1bXkYv14IE3KYxhPfLLuj7AU-QZbvL8SqNY3SO4Hkni1sOFzAv-rgdWzS7CHi2x8MKxr75Uan5sHMmzcp0SHBsdEWZwaYZIkaVzY-ujcJqw44L8hQzILS3gmbjg6ZC-ov6PT4VI-s12t9tu2J3-eDyD_ts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnGfTNNvyU-H_T9dqwvde_iM0JiYB0ErByd11Kwq1JN0vBxM2wrbROGY57_6Iq3NRo7VfxfoT-3AD2MVoiW9rWFSd6tChNW9V30ahmfdsSWc1GQbNziq-FNc6sKXiDoAYzQ0ksWYK5fnDHlqGkcYmQhVAt94Ox6IimhRZgD7VZSwKtX08SaUeJhJF15Z2Y1bXkYv14IE3KYxhPfLLuj7AU-QZbvL8SqNY3SO4Hkni1sOFzAv-rgdWzS7CHi2x8MKxr75Uan5sHMmzcp0SHBsdEWZwaYZIkaVzY-ujcJqw44L8hQzILS3gmbjg6ZC-ov6PT4VI-s12t9tu2J3-eDyD_ts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=RQ3oeNRfg3fO-sVuw7_mcNqYhGprWorwPpv-6NqSCbCUDb_XAEpXcGAGkAzPdrtBJjYkqQa22kTng9WnOef_Vsfz70OEzMYb36SuEZQhrs_jj_ALGNRtTJcOLQTel_NE4JlbpqtsLAp_4G1PwsJVvf1PT7IMpVXI9msNACFRLsc3JDHNFJ59PPfkocnD1niu49J-0JfKrWfAjG29rQAN7eQOe3XnDB7NdGOeTL5fVu0PqtFJrIw_jHIzISWgGeCkDM7Vq8r0LcKnJ5jK5EZo1dLCrZtM11fcmhF3OcGpe26Op9_cnLLnvazhOLbNSAm-WTFbOXq7SfijwxzSXEgFkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=RQ3oeNRfg3fO-sVuw7_mcNqYhGprWorwPpv-6NqSCbCUDb_XAEpXcGAGkAzPdrtBJjYkqQa22kTng9WnOef_Vsfz70OEzMYb36SuEZQhrs_jj_ALGNRtTJcOLQTel_NE4JlbpqtsLAp_4G1PwsJVvf1PT7IMpVXI9msNACFRLsc3JDHNFJ59PPfkocnD1niu49J-0JfKrWfAjG29rQAN7eQOe3XnDB7NdGOeTL5fVu0PqtFJrIw_jHIzISWgGeCkDM7Vq8r0LcKnJ5jK5EZo1dLCrZtM11fcmhF3OcGpe26Op9_cnLLnvazhOLbNSAm-WTFbOXq7SfijwxzSXEgFkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSPvh9-sCRcjjAOAYl8vG7DvQEYc57RLwIwKaaFr1wXZmmqJWQy4QXNr4RRmVPX5znGi-9HBFkQ7uJUpMeDe5dI3AanvQL8GXqdAHm07GFV52BcduWvnhWj6Rf27PBh-mlJaIFPsz4_PoGlWvEoW04cOQOHP7Kp7hwqAigd3uMGEaOupp1SPPyCoxIswTYDxJOG2GNFipRg9C13-mkATA17jr0A_ymHw7Ifpl7wMCfkQMVltUO7R9MgaKfVzDEJw8BMUBMiqTlMs86c097qloeQWK0g94DcGLhW6_9_6pEdYrggpmwjbOjvCElDITuH8LvyefVT3L16B6eNHMvKMAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBw2WkkAo4b42MT0RjvgoKJgGk3GJEGi5GwCwG9gCedBvcCN1VT-5soDxBIqfRyNW4xinSVZUtJGuQZVyx-Q6TjpKRRaTVS62Uc0L3c4DHpggZQjmLdoMHP4q_JhjC5PLSQ2KrdCv8iZ__SC2PquMI7ye3a4BhZz_LU15bY_Y_5zjcqVFRTZniEYylhm-pcwWVbVjnn_74nZgJ1fuL3jEACPYWyhXNvXJDBDyVVNEPsmMKSsZbSREu5KIKPUp4cWmu8WcZQbEqkn8hd131TOkvrJoSu_H8_KtxjFEYEvOjsejOEQEkPcDSQxy1Sd7RENX5uuUrXbUBsDKG9RUOSNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=TCMsRRe5cXvivn5pVeYKX06n6TYliQvUX-E6yc3lsm-p04LkI8MQkAC5VkvAC7bGeVuHEDlx2aYDQqjDRAso5dQVjzDyTgFEOT_3nZJ7KE0Zq3Ty-4pO8DxNxGQip0YYMgmNg7EhG4MwReXlGzuAWjWr5ELXPuSQj_9xkv0YMxnNrx20O5gLrYH8ndUrxEZhvpE7CJ1hyW-2-OXqukSA2WxXtdmUF5nrel7X4QbR3LQ9_EQkhf0FLl2aAUqbcDsfnhgSQq_L2Me8uTKt4DcSLIZMYjFfiA4zuLB0y57c2gbvc7t95C5c0bRORg7I9dCuk2kDw_JUVB9gqGU6ik_hNhMhgaKvpV8-mgJH-_Bd06hSTktVn7EwEZImCQxepYfn3revcI43snyfqWne2M1-A2VOvHYwO00JCCpAahmSLT96cDf3yOP0HL8ijIw9rF-jZZOJ3rzRh3deQY28a8RMEc4gDeBh0nAXOdNYvS-9pw3_PgXOIc8Y67YYaYNzk0FBbBQxHe9mq8nPUd-n7QcO7Ryb9Wl2jcOmzOmxh822pkoIZhXvmx6ZlWXCSfaN_LUaPZHFpjcISlPiqU6Lmh8BHiU4B0s2km1fV1JX_fhtD8yTHoBWWHGq6ko7s19X0mlV0bhWj065J8z7ZSENZ5kool8nOElhbo3K20dtSvU3x4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=TCMsRRe5cXvivn5pVeYKX06n6TYliQvUX-E6yc3lsm-p04LkI8MQkAC5VkvAC7bGeVuHEDlx2aYDQqjDRAso5dQVjzDyTgFEOT_3nZJ7KE0Zq3Ty-4pO8DxNxGQip0YYMgmNg7EhG4MwReXlGzuAWjWr5ELXPuSQj_9xkv0YMxnNrx20O5gLrYH8ndUrxEZhvpE7CJ1hyW-2-OXqukSA2WxXtdmUF5nrel7X4QbR3LQ9_EQkhf0FLl2aAUqbcDsfnhgSQq_L2Me8uTKt4DcSLIZMYjFfiA4zuLB0y57c2gbvc7t95C5c0bRORg7I9dCuk2kDw_JUVB9gqGU6ik_hNhMhgaKvpV8-mgJH-_Bd06hSTktVn7EwEZImCQxepYfn3revcI43snyfqWne2M1-A2VOvHYwO00JCCpAahmSLT96cDf3yOP0HL8ijIw9rF-jZZOJ3rzRh3deQY28a8RMEc4gDeBh0nAXOdNYvS-9pw3_PgXOIc8Y67YYaYNzk0FBbBQxHe9mq8nPUd-n7QcO7Ryb9Wl2jcOmzOmxh822pkoIZhXvmx6ZlWXCSfaN_LUaPZHFpjcISlPiqU6Lmh8BHiU4B0s2km1fV1JX_fhtD8yTHoBWWHGq6ko7s19X0mlV0bhWj065J8z7ZSENZ5kool8nOElhbo3K20dtSvU3x4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=HAmrOIJQgcGps75U4nu4rfgZ3d3YqUMcl5cAOhHg9eoLUNLxGIbntHGo_K6OVP-DJgNXmK584lUct5YKmbRNYtSUwOMcdRckreLkCg-5ld-4CWIgPGCyDcMLRuD5RfrVLxlw-ux_crQYYLsVH3eOvF1I38TTq6a-CeBYB5pF62-X7mt4KUVRPEK9gFYPWNzetYdl9h_J2jCrPnSgh-gtSHYv63mRZMcUPWuCNTyA9dgfcGNyoO10Q-a_doN4xI7XVKKnccYjT4J5D0B4FvbL6Py2AcdwSb2qnBony8IX_P-l-9rzbZoM9uv3fApR6HwPYTrph6JhbAYKYzV7PryB5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=HAmrOIJQgcGps75U4nu4rfgZ3d3YqUMcl5cAOhHg9eoLUNLxGIbntHGo_K6OVP-DJgNXmK584lUct5YKmbRNYtSUwOMcdRckreLkCg-5ld-4CWIgPGCyDcMLRuD5RfrVLxlw-ux_crQYYLsVH3eOvF1I38TTq6a-CeBYB5pF62-X7mt4KUVRPEK9gFYPWNzetYdl9h_J2jCrPnSgh-gtSHYv63mRZMcUPWuCNTyA9dgfcGNyoO10Q-a_doN4xI7XVKKnccYjT4J5D0B4FvbL6Py2AcdwSb2qnBony8IX_P-l-9rzbZoM9uv3fApR6HwPYTrph6JhbAYKYzV7PryB5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPGgi5ZjgFc6Uw59Dt5YtpEt_KYf139gk8pyemhyIofH6YRE-nZl9MjZnGX2fzKdgVZIYAhVTaixHBu-GLt8ntcLm4qQHqOXn-6KO08c7i-N9w-NcCzHMoUeZLK8V6Jj-KadoVDbNS1r_saSkqKGTGawK3MnSakppYBH7Et9XM2TPY773B_C5juq8-aJbD9Qf-iIjMwL-RWzAJ2FA9x___Cvo-ofG0yWekPioW5fHMVf333rqcFW7jGqSh0gvyKSastCbhQLCqtFCKVCCd67-rb7ZXwojTbupeZxMgN07jTMWiZt7En9hPfoslDGA-V6IoD9MOZqsBLfKSHaSihR9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYS7918eZSq7mxNZ4OU7P1CIwiUklikXEwgjH_Be7dSaj6hW3fAWVFfy_yXB8CeEXGrkGUGAF6r2zMOqWT0A8PfbW4fLtN1LnqJfxrn6rJbsyOdCE0BXUJzfidGclpr8jcOTrM9Cl9wn9xghzPtgdV6F1SL62srYbaRvVwGiD2jQkAH-7-anyfzJBQ9YZz6z19N2MBNmjSqsnsZKwjXBDBdZFQdHTI1fx7ZzcWa7r0VJmBKKX_jDvwI435qI1I2d6fIYkOS2l5XY_TrwaC-48iPVel8JxLm_efuX-Zk0m15bt-p7KDJqWcEDn2c_5kiusLuDU0Lmn7PGXCk3RJot3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v63i8QpCT5Jxhl8jef3L5SWDTNKt8Vu5xfiWQHKgKbiupDeCNGXIm5rOwDZQqhtVgZ-EYm068pET4dM8SsTwQwwK_CyUTbxHIH8SXs1mC5v2eeZypPXPdLuVeYCzF-jRYSTfVloP2yXapdb43EKKyeXv1QhSZ3gpnR_rXLxTbd3Pcvq8bJKAhpcR004RERn6PJqVYPvTF4zLwxNtZw2slHUQJhSrav_BkKpCUuKXMw0Ozbw6rQdLHbXVy3mUfA980ucOGgs7C1UP1dCm4dZZ_6Okb_mPdl88qQ2aB-7581SQFZ3Sz53tvhR2oHzmm1ELBN6DYFZOXfdICaivLHJ1GQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=Q9IxZEvjz4hxdz1A6XEYa8iNAUhJ-19wCbBeIwa4J0THZ1sFN-FMBDD-Lc8bR35zX6JPWFVjsaympSmb5ADzIXKQhxSpA07SBazyqcPaQ24LCZOo5fx5UPcg5Vv6SL_wiF-Uir7xDrxLFWET-qCm19zgpBI_UBE_skfiqlUGvpRXz01tQuefm73XAC2uliC1sjdM9o9S9n4ui8gU8VBINFZVIPphsCJ5TQ5lqqbdb4_f_LsfDXG5Ye6pK28tM8HEIyV4hhwTEISTIjha-CEC3mfzfMFzS1h0WhW4f4dP2CmJ-GbyM2ASU8RIGjPWzlgnZMctJHtxOSPFwf3zVriIqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=Q9IxZEvjz4hxdz1A6XEYa8iNAUhJ-19wCbBeIwa4J0THZ1sFN-FMBDD-Lc8bR35zX6JPWFVjsaympSmb5ADzIXKQhxSpA07SBazyqcPaQ24LCZOo5fx5UPcg5Vv6SL_wiF-Uir7xDrxLFWET-qCm19zgpBI_UBE_skfiqlUGvpRXz01tQuefm73XAC2uliC1sjdM9o9S9n4ui8gU8VBINFZVIPphsCJ5TQ5lqqbdb4_f_LsfDXG5Ye6pK28tM8HEIyV4hhwTEISTIjha-CEC3mfzfMFzS1h0WhW4f4dP2CmJ-GbyM2ASU8RIGjPWzlgnZMctJHtxOSPFwf3zVriIqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=XPfSSc1Q3EddBzr9BNJ2g6e0DC9JuFTcVaK_QjstvAHxKPBhN6dvHmdJ6sFs8HgbSYVsCxj--wDhGty8HdhQlIDtLrmtKnPEVbtp4fd_mez_J3P3PGtL1nx46SpoPNzNojjZor39KK3ELC3awI3OrNAosxxUG6j8jBeKW3Ba-ofZLlJQq5-znsP37ytmWZgRxpsZy9mJGXnuudoES-3fQKtKbXYbrqF2HaV6Mq-82_G4HQoKdXQa-FtJZXgGrToRXj9vmMtTofugp-0dz8Qc2bZ1Pn-7EhXMXhnq3xBNHP6oHoN97GWucTyot2KVtylJgbUYUj5NbrlMjRVrs5UJj6gYtOE6in4mceHGlvL6af-rTHIwQhrZ51sX9ufGO-MIDT55rV3wtzlANW8gE_wHVWYascG-xY60YnMDgp_PPL2kzt6U5MC_h4hMY7Kfjad-Bdr3hgDNsWrfFPuT5sYRLaTLiD1ohHaQPIiltxKgttKqN99-MMSI2OPoz9phT0Hg7pcT6smYHl3gyfnxWxQgufPqVfi15G6HO7BUqG20Cnb8xuqfMkrKW2bG5UF-qdH3SgtPvwFE1guUbwJbK4OKYbcEVstAqI4Y9W8aRPUid8X-CCo1xdy8ACgeS8B-EpvNRefyTA13xo8yRTMcaK2fP6a5J_fTJRhKHS_YB1ruIuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=XPfSSc1Q3EddBzr9BNJ2g6e0DC9JuFTcVaK_QjstvAHxKPBhN6dvHmdJ6sFs8HgbSYVsCxj--wDhGty8HdhQlIDtLrmtKnPEVbtp4fd_mez_J3P3PGtL1nx46SpoPNzNojjZor39KK3ELC3awI3OrNAosxxUG6j8jBeKW3Ba-ofZLlJQq5-znsP37ytmWZgRxpsZy9mJGXnuudoES-3fQKtKbXYbrqF2HaV6Mq-82_G4HQoKdXQa-FtJZXgGrToRXj9vmMtTofugp-0dz8Qc2bZ1Pn-7EhXMXhnq3xBNHP6oHoN97GWucTyot2KVtylJgbUYUj5NbrlMjRVrs5UJj6gYtOE6in4mceHGlvL6af-rTHIwQhrZ51sX9ufGO-MIDT55rV3wtzlANW8gE_wHVWYascG-xY60YnMDgp_PPL2kzt6U5MC_h4hMY7Kfjad-Bdr3hgDNsWrfFPuT5sYRLaTLiD1ohHaQPIiltxKgttKqN99-MMSI2OPoz9phT0Hg7pcT6smYHl3gyfnxWxQgufPqVfi15G6HO7BUqG20Cnb8xuqfMkrKW2bG5UF-qdH3SgtPvwFE1guUbwJbK4OKYbcEVstAqI4Y9W8aRPUid8X-CCo1xdy8ACgeS8B-EpvNRefyTA13xo8yRTMcaK2fP6a5J_fTJRhKHS_YB1ruIuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7ivVpJrOJ8pNfYpk5PJ8yvrygX1UJJGTEFlqUuWv7zm63qpNYPVmgU3pwpzX4cIPUFMMokx2snUkU4CfJmU8gB9hicmaVGW_IFsJYPtCvunwO6RYj69GMpSidaibLZx_Z4je8k-NIflBrwcgbh-x0yRkTUnDdmxQBAyjmG3RVXUdDTiPZ4aE5K4Dr4v_mZdF8EJUfcwY4f9GwmOA3J7_-s9gok-EdIZKarQ_5dykkKLo3SJjYfD8QRKyXyzIXws50INrVLyIEG-zqFIactkc_zR5b7qZ70O_3DjJ6RBbRs3PbCe63BtNlQIuKzz9QTedNZSADbF-5Qworl487h_0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfomKTJEvJ5IQy1B_uN6_3DK_AeidEDu_BkjTK-Kxu3kradNVlWEq7Px2oxAO_nsLZR_WEucpSctqux_A120VXTe_xd1OQ02C9GLa-WjQqS6p99IUNkwm4vrxM6n5aYKgF_n6orRVzEF0DNuGNlgjEVeIinSTmrVSaMEA_r7zIZ7MPv6jXRGSlgDDqK9FXxqjShM5xqYDd5cgPJtSFNl-npAE1Q767IGxDKCQwwflUn4xdr2E3Voui9wwi1WvwMVcGrv3ZK0zCL_r5giLSlORDLMowwozELE6mW2Bdt-WgtmGTnaJwzjZU1zUgXfyIGyJnX3tmMhy0CK2PtKnv7OTA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=Jl3X-Al7GJc5Vfw_38gegbT2wLP23EQz3s1s4ApipqYWw-1HP9F8Ep6wHydzuXIGXuQYw5kIn4iJ1TW7jdK64te65J2m0CzZE7hdItMCeXPTLsdojRWOnso54dssdr6aGVZiO2NRNVz8aFn6o2sjvNzkDLX4oCiekuL3sCk68n5pccecfH-Bz07MkoEH3GTH4F7JwSXsXRmX33uxV2m_8Je2v3RRwCDM49yr_338yeQoPcgoyy7ZwspeKN38Sp0SNCSSVr8LQ8etp94Qm0eRevwjjoWYvO80v9EgnaP1eovwfIxb2pWVe_1hqdqc5PHO_lXQj4CUXXo3eJWJp7nA4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=Jl3X-Al7GJc5Vfw_38gegbT2wLP23EQz3s1s4ApipqYWw-1HP9F8Ep6wHydzuXIGXuQYw5kIn4iJ1TW7jdK64te65J2m0CzZE7hdItMCeXPTLsdojRWOnso54dssdr6aGVZiO2NRNVz8aFn6o2sjvNzkDLX4oCiekuL3sCk68n5pccecfH-Bz07MkoEH3GTH4F7JwSXsXRmX33uxV2m_8Je2v3RRwCDM49yr_338yeQoPcgoyy7ZwspeKN38Sp0SNCSSVr8LQ8etp94Qm0eRevwjjoWYvO80v9EgnaP1eovwfIxb2pWVe_1hqdqc5PHO_lXQj4CUXXo3eJWJp7nA4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oC0P_OlR9yoG9k2kz0Oo63AUAeVcpx-pZz_vT9ouXG27fHK7PhQeHMbzoDjknJ8s4Yrm7tqCH4m8gQzUl87gnOPDzbVTGOfiOprH2yPBe0fccjNDGygiiGXGrX_e6pnsuFTsf5Ft1qpuNyJHs90yL90Z5DKTXXJgQ4yYkKFPTJjDmovToM5xNE0JioQimZN-nbaZKFg_L6IPtFh19Ca6l-RNMO0PcAC_Jjj3d6DobB7yTZK-5dbIiBdASeO9nlYsCE4Ur4uNDlYX5lWGevMbfIWGArlWnJmEFro97LsMQH35Vba_-y6NuHDKI_CjXDCndQlSXykQNgnB14kOCAYleA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nfh9pybUNKvwwc_lxjWw5Bi0YUwhCYpPusHoz8Ph57emgFPUbknOKK0lGMTk3RBW7cR1XdprLYuwJGot15w2BDnU8qlYBmRwIFpZ1DoKtc4-a_8ejQKRtb5bTIbxubdNdB3FGvDFf4FxCgY1JXwZz-T26uVKcylvbp5BXkJ7ixUudHKvs7aPFSRyUMVG5cQS5raOw8f3KxtIH2lqqHQ8BX2JriDWxve0ylV9_snP4HJYqmJNUqHpM_Cy4TD9ZXNqjtnrtCDdFeOErzA4za17ULIBGx5YtVUsV1ILZmQEEbYLrBq92D23F1jJZ8M0J4_wgLLrEJVS05LTEeDOOeYZlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMeU1yC0lIUWZVuaQuiQwzOdOeMX_XcUWOW-nQP0MUOGOJMitxRyGAlWfFDS6AeFcQLWmom1yuf_eTtx8oQD05sX-UiYOEhxitiyfUirZ1JNYgXONPN-w4RiHlSNPdbGB5NT_eGPvVnYfB2XNQVdf58ne_glAgom2UtTuzFDxUyUXtZv3Qh1xLj4lmzcDYyN4xwQ0HvUT-W-7zi4L1MzIj2nDleWE7xWZMnqEQfDGOBCtMCIZA8gJnxudtOzltvQbjM1ahQR8ZJq5MSBsOphvyzYqOI3k3cZTIrxRmCkfz1wDq7Z_ri8mrzTgjsGH5Tpx4d6KFD2YROsOinbxBA26g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oddR2KzkgtboV--V5IMXViW572SkHSPJzfRINyPrNbBp8zcNaSZTiHARB7OnutvRBQ8XsSyQ6FZZ1vfX9-B7ag0WOHxZbEJZhGW_n-EhGJu-7OkauBo4b9W28831P2m6XzN2_s_tTZKwcaxITzJ3qQcP6LXQT1jmMxMCaeIql2nHbQOCsTv6A7kFT1v0I4ZBzBVq__gnDfqDnx_UNBfUuO8zNEutSATEsWZXm142OYw5WtTc_g99F2QXvcCw5x3Ieoic_a1zzW51Pu876cGyTO10mUDi3GUTSoIa4_jIrWRCmYHTnultlh74vFXssSbo1fDjvxmq72QXZvsBfXsOCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E11nAbfSSr9BDT2AvrDe69ae4M7_mhTuYAHH_tRkW347Xn2C2QymmdkVduT9eFfl6H3WTUiPgpN0irnxZ8gXGgsE24L2BzEpN1hPvYX-qRhcviJ1Fhl1BJBzPmW_ptNdhzAk7mgv_sSSORRwwZwhxdLcaAwMrVV9paTr5iOIX4OfnUvN6pRwok6aAM3NdGqewbwiHHoyl7XqW1sn0hxotydKi83kJoSFzYqLa2ZCtDyzaHw0ml_OoAd-WsNRmRfSM4TCiY7VFtSeELM3q8O3lTVLmDjUxpaRqWvD4cKxEc7GoNAdHRe4injyubJi2zE9VIr_NYd4m2-n1pN7CM2UuA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=LSxXf9z9z_J-LPtfZoXePZmUE5U-Y5b06SyEisju4ajoO2awoGwAS52nLkBXL5hFjtA6kWbxv12RaTCtdn9B-VyNxhkIlp3Im4XP7MesHO3gAniI8xtI7RC61h1uf98eKeqVc0_Bo5OmTDRzSfSm3TyTsyvB8q7aKh9hRDG89ux33uaGLNyDHmFTx10bMYD8TqiIFKd6sGvZWkRM0zlenzcDa23D70jSLvPYXHxf9QTQRUbO8C-5roc9qBzw-qEHuCjHu43exO38hpthuCTE9YC4oaAK_8UsxYLoB_V0oFUDUPV6tm-wDAq-h-6t66Usg9APgKfAnSfPWHo2EGe5yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=LSxXf9z9z_J-LPtfZoXePZmUE5U-Y5b06SyEisju4ajoO2awoGwAS52nLkBXL5hFjtA6kWbxv12RaTCtdn9B-VyNxhkIlp3Im4XP7MesHO3gAniI8xtI7RC61h1uf98eKeqVc0_Bo5OmTDRzSfSm3TyTsyvB8q7aKh9hRDG89ux33uaGLNyDHmFTx10bMYD8TqiIFKd6sGvZWkRM0zlenzcDa23D70jSLvPYXHxf9QTQRUbO8C-5roc9qBzw-qEHuCjHu43exO38hpthuCTE9YC4oaAK_8UsxYLoB_V0oFUDUPV6tm-wDAq-h-6t66Usg9APgKfAnSfPWHo2EGe5yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=JKaP_RvKiAhPs9PF3O_zDbrc9FIBOyoxt-sHLhmucMq_jEkkRolXSqJ20G1ZguvXmo9zfatYRYgG8uss8FkXTJzp5AL8KHPCf2tLmPlwapuxWfpciwN_px-IRwDkhRLk-0yXNEMQFJY35qDuWDVfitiNcQwjHxOXs7ccJ8zZ5jw6bkp5_erqO3wqjUaQ8-O1FjLGBoCBSmYESZGVi32KBz9HVBW0bcHC6DCKPlsGmIMYPL2JvItvQTVItSVXKq_u4gmQ_JycXuKONK3PfgZgtTQHX6f82GhKZI682JcfnO_jmODxSco4AXef4qGQkmFgMFKAg0SsW2oQHCb0s-0V2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=JKaP_RvKiAhPs9PF3O_zDbrc9FIBOyoxt-sHLhmucMq_jEkkRolXSqJ20G1ZguvXmo9zfatYRYgG8uss8FkXTJzp5AL8KHPCf2tLmPlwapuxWfpciwN_px-IRwDkhRLk-0yXNEMQFJY35qDuWDVfitiNcQwjHxOXs7ccJ8zZ5jw6bkp5_erqO3wqjUaQ8-O1FjLGBoCBSmYESZGVi32KBz9HVBW0bcHC6DCKPlsGmIMYPL2JvItvQTVItSVXKq_u4gmQ_JycXuKONK3PfgZgtTQHX6f82GhKZI682JcfnO_jmODxSco4AXef4qGQkmFgMFKAg0SsW2oQHCb0s-0V2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYYX3dWoQdSQ8QvThuOmPF-dk14KdpMi6pC7PY9oT-ZknhKdRVkCq36ed5ev7F3fxeIYnZckhjS0iz_5beLAOOhu5dCVmuX59x3N0kA0l4XA3PJO5BHJoOjjf2yIlmwc0pjv6t4gzD662IktBWQccAlpAA0wm-TPkXn_O7iLXGB2xaX1k8f0itWJbeApfrqZPzkaEhHCMKuoh8JnDuVmgkJgY5uytaxOeYUjNqTxmI8HynfoLD3RNAWwytQrglTF0WSNJ8flUKpVGaCxJESCXvTbZrkNJTfsYASUvZfei0eY2bRSL71gOZIfUVejj_17_b4ig7InnL8m8NPXXaHarA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MY5ulLG6-ZdwWBvD_JDhFggRAfCu41UvpyQjgsXM4Edgb-kLikyYPXQaI5XFTberjYztQAwB3xaUq4a842T5k4ylAg1AYgWng2mvRONxJltJ26-o15fFbiPt1agmkWimimOMsruiGH_xfhjGas6_UYdIQYltjUOdrkx-9assExo2RmGmYLM0__Ia7nWq44-k_5rEW-6yw-Ypc6gIzLiMnv8CtCrooO1Rj9Qspo4vbm6mvBnNG-ZOn4_Y5p8Z41uy6S4WGwIOJbEN1Wufm-VmQ9PwIR-zIL_G-7_iHptF-gp7UpGjXKBcO3b8VLjydsA6lXw7toJ9piWZN6dkyiOTgA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=iu239BbUAxsrAvQyXSJfUlZPculvxV6CyuawYHqIWCOl0rAKwQUaj4HLMfaIW9CxXutX5D63xjMhSTFGqMIu-3OVOz04-3aY7nR14TxRWn9Sms9PskLvdhwAFlWQLjjJls0lDfkKJGdSw63pZOTEQpXvWw4hsFtLNVvqgRzR2eDf18zGsWC6ntrtC9wutWKekBPNDmMhg5EXb4CrxAkwmhUjGEp98AoT_pKUc76XeUV0Z7yLW96oI-ckpwpps3NQaqQdk6LEI_nmiy4IeCyrD-1jyn_NekKXt0jXNNx7EbH_wQiIEH7PkeRvPwF_wHLXfuvYjt1u_CpXSfOZmIsMjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=iu239BbUAxsrAvQyXSJfUlZPculvxV6CyuawYHqIWCOl0rAKwQUaj4HLMfaIW9CxXutX5D63xjMhSTFGqMIu-3OVOz04-3aY7nR14TxRWn9Sms9PskLvdhwAFlWQLjjJls0lDfkKJGdSw63pZOTEQpXvWw4hsFtLNVvqgRzR2eDf18zGsWC6ntrtC9wutWKekBPNDmMhg5EXb4CrxAkwmhUjGEp98AoT_pKUc76XeUV0Z7yLW96oI-ckpwpps3NQaqQdk6LEI_nmiy4IeCyrD-1jyn_NekKXt0jXNNx7EbH_wQiIEH7PkeRvPwF_wHLXfuvYjt1u_CpXSfOZmIsMjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=GbObdGuIpHx-QtVuTNa1JBYrn53FEMS8fLrw4qOquLNV1G0NLrU2_wb8K7TVgGps5xoFAo8AjjT89TVjAu-IvdE5FP1StqMvuMlE-UCPIeDXvgZOHQZLPFgw1E6l2cix4B4FLRuEdVbgp0TruPyWxebPj73gwAW5uIyW9oWl5ijnfAFkMy39zq6D0Nl2PA3Z42GJm_fnPXR2ujyANBtYtGmNHAxMN7_MxkpmxIfbjxym-RFpadxx0r5MMnxNntBhjB6xeBKmPW_XQGyYqtpvNItMxq0Kcdc44BZqzo1rmiBzvn4MEWHpxAPTLlq8BI7qUP8ly3tYaVvby79qAlEkAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=GbObdGuIpHx-QtVuTNa1JBYrn53FEMS8fLrw4qOquLNV1G0NLrU2_wb8K7TVgGps5xoFAo8AjjT89TVjAu-IvdE5FP1StqMvuMlE-UCPIeDXvgZOHQZLPFgw1E6l2cix4B4FLRuEdVbgp0TruPyWxebPj73gwAW5uIyW9oWl5ijnfAFkMy39zq6D0Nl2PA3Z42GJm_fnPXR2ujyANBtYtGmNHAxMN7_MxkpmxIfbjxym-RFpadxx0r5MMnxNntBhjB6xeBKmPW_XQGyYqtpvNItMxq0Kcdc44BZqzo1rmiBzvn4MEWHpxAPTLlq8BI7qUP8ly3tYaVvby79qAlEkAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfQBh4dUQVbaSiQegbDcNReFFW9YN_WkmrZJskMH-1CpOSNhHBw6LfbrKBj8hBMRr7RmcSO19fkLkVkwoboDdAOh8vRS3TNx_S80aJiEBsdT_1VB0DzXneLVYazzKGaV71tiwqgt3HQMb7o4eQDxdH-9MfQ45HhYWpPpPgYy4c8HYXroYMDuSKEGwwW47IksZgxpwceHw71B8Wzwb-Wqp4Na85C8g5rJKin6av-1U2AzmrvteSxIvIavTss__ez2yNYCPlDFOGZTRQAoIVkATi25PnTMgWpXr_oJ-pEBcUqVixMIxv42-gK9LQ6tad4G0jKE7qJ1CLJn0ECuJOoK1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvIkPTkkExZAGyWjs9p1D7vw7tXIx7m_1Q6gCAHdtuwQ7zI9pP94inJnqAzW_8kybOLPtWaT3ihyoKuELA5_COwlE9gt4eZttQn-_G_eau-nInriuxap9ik_k8Kd0L3PtoxWwXuyUh8d_IBw5Qkpx7IqEc1aSQpJrVzYMip1ykkfx7Nsdzo3eADifrhNGbSHiW87VTEYWMsJuZ_Arii8vEsP-fHa7cWSUlSB0AASbeL6GPq9k9UwGsWTZ8kaeWTswnKBeVaQ5zdu1Tf0kGOFMdF-kRrJ4la2Ebk6zN8wSxNfM49Hb4zOsyOPmLBca8k_yGW0LQdeJ8yaMX69AyeWfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJtxepV20g95vXrGeRgP94SOanZ4sMmi2LWwDsJ7NibJA8FgBVvXo60nchMZ5Wj1EPZEbPjHNsBhZBm1ttwgZX0d0evkrAENRHDI-rmFF-XAWjU-oT-rZgsjLjj05TB6UG8aM2479R0Q3R3m_s4OhTtF-ORSrfW2FLQfInTRqpefckP80r01Sy07HBkqzyOU7PSvHoqz4V0DNb03WIgq17X3-JDdGNJWKWTYVG3XhG4q76agV9qIMiKpwlXiWX59Fh7EynCZtyi08mdyx4gKI9bTNnrUXHuZfzZ14TgoovcshaTmCleo01fEhCRU-38_SLwRnvizCM833Nhgsg2F3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQdAXHdHMpjSkYpXMfAUcEoJ5K0pWJ5UA01IWnQq7MKAHQVuow5WHMUU_yc8czaPPSEqQuRKqggUTGCCF2R0ilnNE6JMa_8W8_OqLGlbgV66SpXs91_-IPSlXeAAntRl7fhH3MI-PzN8u6JgrTB_PYe7rMN3xOPdOobh3Nm24IF-H4nUjqZ1PkVLnXlJAWrhzenZ6O-I7B0mGMDxhJ3JowdY58cHRGsAa4VahRtBkGPDVTIXK0nP7jsUhre0VvrGqzFDSMb0VW5NFkCdJkD1aSwlQPFwDtik8TCTJEhMlt31A2CtSiteWaErITmSmN7fuUtkeiGFammyeC2THK3bFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U07alxCCNcZJN9rmoj-rZu5xNSX0ST-N6EA73SOlGC75MNp2lCQF6zGuiwGWgQvOy_8SxgHbywaaB5poZGXO7Wt586Jpqmycd5FBddBuCK9desdTzwTIaNEV_7tamrIwp2Yz8uxH84Iwb8lsmVk4A71sHnBk2TXXVTA0J72x5FqoAX5L6gPMDQFF8lRhZDfHv_G-MtN6lAozHAyQ775vl7CBw1SAaNgWD205INNKLqqrtY5S07u9XXCxYl4-n4F17WSdN2SyNZpYjgFQFeqwwsC5BO-mzs9gGrOApKkp5WUHyW4zm4RLOFxU8MnzA_dyuAi0ghcGUuRf2cVwLsGxpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tJhhQf0kiQhRoCzDRDsMaN1mMYx1hFjGF0AqYJ0UcLe1H0FLEVlPw0hz_WxrJzpeobnt53pGmSNnXA1ZFqbH89_v8ppIKfWp-wWMe2vSQLvyMdzszemqG0_W-EngcEcd_4v7hYMt8A-9OuekkiI8k4Hxb51E7G5oOMIIPeyzb3KGPC5HqpQfONRJ2bTzztW7f8KmvVj-BiK2dfyQ3ONEyUgTRXSLmXT4Z1Nw6EjeOWtRUutZsVQm6dggFM7krX_iygSUvVOvlQIQUeAFDy3pbNGSFHWr7jSk01yv808ZprRszqEuR7N0e2RNvdRH_H5v373c6Af1_O1BbVR1Q1lqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJh7DmkyXtqPn9LV9d-ZPrS2OgqsZOMtu4qqFtn_IzTFZCAwJFfSo23V_VPoceM8_95YEhmuZcVgtUInIoZRVC11yJYzDjcoEKsum0IczeLbWfDDEjhQMRlawje6x5i8vgZm-BsHtMn76bj7ZYmu05TxLs9JTI4nFVnFnrVlMa4pJKi6ilGxMETG_xPG0Trt0s_l9YgnBtYwblgYqFwRqmzs1WIA9NOLCm7Nmaubka4y7LxXT5gw3DiNJSQn3frLZi6YbcVmMyPsYhykpA5sghO5-Wgj3y3K56GAOLGVEH28sZbdsZ6F2Dp6tJv7Hmoa7nuF8KPDu2LR5ZVPJhYlSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N2bWKUqlbFc2T9gWMbrXP98GQZyFctUVbU05qERWl7wgY0aYbofisU68qtP20IwRpPC7pL6IX79fUBk34ACJoSytot5x2nLTBcc0o5A6g8K_fUI9wV2xNSAnGFN2Lefz_Vam6HtNtCqJsk4fpzfen_HTvVa1T9jbUGt6nm2AKyVNZp71jgGlRAFA5HopHpxDnwIqSLB6RfZtc1aDk1PADzlZNWoC__Pqh8uhlZBftMxbmH-JLUHQ03saUjzbMCfRAH8mSEY3tUL-VL90METp51lo0-v6F2IZ9PM4RTRmRglAHl5-TkbBx7I52n7suOgKMfY2oX2_7WotK4L5ME5WJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdIHuCAJ7Qm_VZGRlwYtnk_Z5jpiUtCUOby5t0A-FLEvU8-qST2WcrlVsaIE8yWhIUf8y6I1olExEVyTLWwVLiJnIN0Xm7-0Qdl5f3P3mCQZ6QOuZDn8XyFs-36RVpgF_JIOpfIBH3-YEcp44sGRYpSvKlL9kNhdKXVUH2mF_TnCrzf-METLlVtFkMuYj5-PA9qK62rJdQrsNZj0lJGdkNenEVdK0JzIzGBvUL9ONwYeNVLpzaeQrm2XO1AFg_20ndmrIJtrqE5RrSgy7IFvTYVXifzNyaGmgOebbJc8S-Mf0wdB5ymEWJoeTh2n6ST8mfkuYVYeU-0KlVOMbKLr8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4Xyrbmdih6KLrURjogQxaHLo7UdICpueAHwt-4oXS5UV4V0QeoFR69BwPj-wb35nFcYLrKhXohJBEvg18Y81JHePWUU-1W4faNn7vsHkW9umkwEWALN1EUMMF7iTNHBBguTNFg5D_UnQWFk-bmuBjqYLYAxZ4tqeTYPeFh6LNAT3rhlstu4jx279V8q0LyppvyV2BTpDqPx38t1JTJjCENEga-OiIGCdbXCRW9JL_rn-TblvNdR4VQL2nghv3ue8uM0fHhoHn77dgXbkR-p-tMzlYlMG9w_FN97hL6oULk3CczgQzUq9HHXv56LQRqsoK5wHGa3pXUSDBBfDSF5-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=B4OnzkbslZ5OssX6gul-t4wlThlOS0EtUlGz-8E7o25blgj4r477rKYBMVGfBlQB3f4fSPRwpc3POr0fl9Hfa3JZEJzqQlYexUNfUQSIOrJZ5s1tnTJn0aEDA2W74P6eTp5hnYWMHbZxZULuNYPArekdBf-Ousrq1f_wpSrJjQ2kRoeJt_mOHb5aMfFtRUnmt70F1xW3lNnSJTFKC9dWFsnrQceGwfuqCL3YSTXCRbN8ilX2yO7KICJaHbRnq0-0jj7Mc5vOP-m8zopPE8vlaynCBXicgC9AblK9g-44N5GmZxhF0UfW4Dl2Z4Fw3WIe-A-qLT86hvSpWR-ZJd5tTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=B4OnzkbslZ5OssX6gul-t4wlThlOS0EtUlGz-8E7o25blgj4r477rKYBMVGfBlQB3f4fSPRwpc3POr0fl9Hfa3JZEJzqQlYexUNfUQSIOrJZ5s1tnTJn0aEDA2W74P6eTp5hnYWMHbZxZULuNYPArekdBf-Ousrq1f_wpSrJjQ2kRoeJt_mOHb5aMfFtRUnmt70F1xW3lNnSJTFKC9dWFsnrQceGwfuqCL3YSTXCRbN8ilX2yO7KICJaHbRnq0-0jj7Mc5vOP-m8zopPE8vlaynCBXicgC9AblK9g-44N5GmZxhF0UfW4Dl2Z4Fw3WIe-A-qLT86hvSpWR-ZJd5tTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=Q0gXWALOZgaM6yg8lVCR-4yaSJuVX4lk3aDka5wYH1is69v4ZyHqaFt-F1ERe_I1j-eAVAUiygGra5YTRxy7q2__h8bkIPNUBcdzZHd3cwgFqeLXMC0tdGPOtHMU5-0pZugsaUhJGK-Sgoky3dRxTms8BBd76-QrZf2goE3FKyjH0WJjVgsjAlB35-7oy0E7E-7oP4tSSFyp1Tbk1-wQA6Jy8RR0Laqrw-Mu_GT81I2OWwQF4I541G_Q-sWqJdfQGE-ry3SSt6EFo0eQhtpgg5vs5V-rr2RR7fzPsykHuBg0Ma4sQTJTfR8u4ajx6DiOGVmbJQL3cNar55v-zPqMIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=Q0gXWALOZgaM6yg8lVCR-4yaSJuVX4lk3aDka5wYH1is69v4ZyHqaFt-F1ERe_I1j-eAVAUiygGra5YTRxy7q2__h8bkIPNUBcdzZHd3cwgFqeLXMC0tdGPOtHMU5-0pZugsaUhJGK-Sgoky3dRxTms8BBd76-QrZf2goE3FKyjH0WJjVgsjAlB35-7oy0E7E-7oP4tSSFyp1Tbk1-wQA6Jy8RR0Laqrw-Mu_GT81I2OWwQF4I541G_Q-sWqJdfQGE-ry3SSt6EFo0eQhtpgg5vs5V-rr2RR7fzPsykHuBg0Ma4sQTJTfR8u4ajx6DiOGVmbJQL3cNar55v-zPqMIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=pOl6AsfLtW-E6kd14Htf8xEmlcudR94otzYGJ6yxYgkxFsL5OxMyQi28vJLp5wHu8791Cks_6Su_y9IryZ_vH06gFxyG4A-gi2DM5eaYB6fHJ3TYqCZzw80_Q45K_woOKvGpIfe618Sx7zrhcEB7d7RtYMDK35ly6CtHtrpiFUyjo_sRFD-Nl0DbRzEjcVZajunXnMfBPQ5iG8EO2ceP-3L9LxjMnFLIBaYfKOBDQW-DE1tV_qhfHbgRvUuttnG6hYLjWv6ONwr_FvoyVHWumeotnrDHXqcwLj3zqWq9jYWJStEV1F7-Pel6z67Ol2d5hvzT7_LDnhYl5JJsWbDdzyha-rz5GaISgqpBI0Jjp43cEFk5LjnqC3DJubDjsbpVmhDVBWq4DTd4gHkpN6a_EyupodddDrZE5MFpqu1wsh_4KhYzzkzVi9MlnYB8pL1IUdhIveoJumWLLjoQ-XK5we_1ytUBwwdpDf8WEbXxRFU0fnYGNHXZC2BOZLJ4B4BV4mGMD_d3ESSU8gLDaWeM-YD-yKhq3F8msaSOTzsZibCgh7URBQp353ra22zBkVFPpipKSHaUFemcRj_97NcrsiH8hDNhCuZUVxA6XB8D4XfnB9UPcggZBHt_uPWAbj2ebhA8SsVZf6AayIhIp7brvplfK38VUIbzZ_qp6y61OF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=pOl6AsfLtW-E6kd14Htf8xEmlcudR94otzYGJ6yxYgkxFsL5OxMyQi28vJLp5wHu8791Cks_6Su_y9IryZ_vH06gFxyG4A-gi2DM5eaYB6fHJ3TYqCZzw80_Q45K_woOKvGpIfe618Sx7zrhcEB7d7RtYMDK35ly6CtHtrpiFUyjo_sRFD-Nl0DbRzEjcVZajunXnMfBPQ5iG8EO2ceP-3L9LxjMnFLIBaYfKOBDQW-DE1tV_qhfHbgRvUuttnG6hYLjWv6ONwr_FvoyVHWumeotnrDHXqcwLj3zqWq9jYWJStEV1F7-Pel6z67Ol2d5hvzT7_LDnhYl5JJsWbDdzyha-rz5GaISgqpBI0Jjp43cEFk5LjnqC3DJubDjsbpVmhDVBWq4DTd4gHkpN6a_EyupodddDrZE5MFpqu1wsh_4KhYzzkzVi9MlnYB8pL1IUdhIveoJumWLLjoQ-XK5we_1ytUBwwdpDf8WEbXxRFU0fnYGNHXZC2BOZLJ4B4BV4mGMD_d3ESSU8gLDaWeM-YD-yKhq3F8msaSOTzsZibCgh7URBQp353ra22zBkVFPpipKSHaUFemcRj_97NcrsiH8hDNhCuZUVxA6XB8D4XfnB9UPcggZBHt_uPWAbj2ebhA8SsVZf6AayIhIp7brvplfK38VUIbzZ_qp6y61OF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvCe-oTwoRxqjHrPToEV3hNBpg-d_rcZIa76KIyxW7XbOP7gIenqB4kuM8mJOWJCGpDxV88FKQlkvwc0Nzl724amdz55bMSU05Bl30NlImqwCdC4fDvI0-f4Ycvk7AZWlnQb1ibplGON73YRYAwZsD3rhKiWeXmiVKNjxHxWYQqI8mkXpZywSx0sHJACHHvpJqoeiwfLH4aLAsZBNcbp0srvODOSvGvDmAnRvGjHbxho4hxEsEOfj4NG7nPvV1iL7KNc7s9Pmd21DOKaF7j0GfFaguoWVirfdypKIfSjncwgNs5Q9y6q324z9RvZPTL77dlT3g0Y0Ae32zhKZUxD2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=ZJuhDuwhmpk42xpsmMv-tw0N8JeQvAAdt49qzn2cQ5FwgF8goatAeMDgNCjMHG_G7jVPT99mjxyBK5FeGyNKfPawJxabG3Whq_uLqerQGiZ-bUJAww27NOc9noxw-KybScWkLOIDuEMBPlJd-VqvX0xGEeNku0sKAmZb3LX5fvZdehHWOEAqif-zXO77-qleRZCniEGF34zozN8zBYtyl32hF1MuhPC5quMf3GC49eKsKsHVXOJJ1QwFHnGDo-ixGQliCmu4B0s9CiZhkW-gaPGNs1StsAbidFFAVo80yRSVdnkBJ0gp-V-O4uSfuQtuBhduVTL7tDApnQeIfkggNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=ZJuhDuwhmpk42xpsmMv-tw0N8JeQvAAdt49qzn2cQ5FwgF8goatAeMDgNCjMHG_G7jVPT99mjxyBK5FeGyNKfPawJxabG3Whq_uLqerQGiZ-bUJAww27NOc9noxw-KybScWkLOIDuEMBPlJd-VqvX0xGEeNku0sKAmZb3LX5fvZdehHWOEAqif-zXO77-qleRZCniEGF34zozN8zBYtyl32hF1MuhPC5quMf3GC49eKsKsHVXOJJ1QwFHnGDo-ixGQliCmu4B0s9CiZhkW-gaPGNs1StsAbidFFAVo80yRSVdnkBJ0gp-V-O4uSfuQtuBhduVTL7tDApnQeIfkggNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6U-xZ2eCCU2NphztdwWJ8z5g0S9iBKFs1K7y_H3_jU-y5P4oVni9wCqWvm0s9I0BXAS-ADFGhofcJeq_kgavnrbbv4NPA7xxPCwFnF9LcczFCIMMXEoXx0Q2n3PlNlLbzBT8CBP5fCCF9ew4pX44cPZSHZhOoHKi82AtcpJsSCnMaMIMHZgdFSRNa6Ppyle95pKqdc4yFiwBSUCwNRFBS9KTYbMV7yG9Cyx-Y7SqRN-1aJVzHEJV8B1lp2AJs0z5QsAWmLhBTGZLvrc9yd19mDCfPw7KQVzVrKDLLFixwRgb3w1YEAp7LGu1svD6RTujFBZAu0GKZgy3zyaNu1ZqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTdwpKAv0QzXPVYgmnuWcp1ZDPQeZn2i7sOKXbdMmyTX3rLhSSg4XNP7Wi9nMVV5jFlqR7uZaLmMG3lwO5Hxq0OUvfAuEpxLF0jdIExSj0Pm9QFX97pnhX_LFotJ2_BLcIQ2Cw-mNlEKCE3Regxs_RB2TL6cF0Z4D3aHcwQDxk24MoIkElh4bifHcTZGMaUns0cbYIz2AlVCQq2yY17B_nUfkTJ-QMxWEt_1aDgRO498pbL5Mze6sH98E3VKPYDCqHZOvOVjdMgwtLsdnzLZDKjJChedbcp1GKOUF8-RLJQtBdnbIcyObGZLzGobMsr0Dy4U-xcpafPnMf4vPIDYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D51rcmS5zHUMyvpODzglZq6RWFr2HjoHWAhTO4hN8j00yDjXKZb2B7djJBe1U623pv7dWiaga85ACjUjSQSmGZ6Foa9CAt3Z9WxEST_vVm3giyMlw3ybgWkqDABd8AXOBF_vVy8Wc7gI1scZCEHjhBAki-7Xjhwt0Tgw6jIaABWZIj6GD74eeg_kF4WaSbDeyMrCXVCyLca1h0L6QdScSOFZMge9fmHw64TNWLivRfnGMiDLJSr1mMFCBob8mRgIGaqau4geNKoVihq6GgcpUOUoMeNpAF6RAtVhryvLoINfkDW6cgQQhQkdMUTiJB-CMgyNz5zBrr3h77_8oHMduQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JbkCyUafP1SrShuFiHG1s14rsTGIqpIZH1TuHSwPSw-WBvDuI16z2WI_O6YY64Vb6eESvofzXhOh3w1h_iZyebzWolT9WJKB0Y0Bf9Jg71WZVs20Iz4lrjak3jXbOwDjudsw2uLn18rrSjB4fpY76dbpW98j7T9xrd5LRpODgpQAv0Zo0Idp2MT8G-FPP8ubYQexp1zOM29r9BP0uZpDDW2LEdNIbV60Zj1AUxdrPOzEkCbznLKAxurJLNf58pXKKGhCYlQbJGcTs2LRDxsR906ZDtWqmgSXHq9rhRCMdFzeBo_xzEatqTy38lsYTmdtnQXC8l6qpvr-uayC4m_3AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWE9TFKr7wR5aatnE1Umw1GpFJJSMsnScPTLQKBE3JVmxlNvEhWYrMKjVqBWoD259JcG0vKmWvhPy6Wf7UOnU2XzwRo64QNbTLjBZ6RK4AUYl9enyM_m4bkd6HBngdwh_TwRsFPg1JU7NYUFvj6xG4Gp7SQeFiNA59eGZoWivrB2fH482w7eYYws9o_cAfBiOSiefXuaHfsFxZYqFfs-qj97RMpektxDcPBEG4XatDFWfK5r8sQCWkX3dLCoRS0XoSBheYbi2hmfaBsgx-XmnrrQ9OCyAC5WepjX6bQP8stIEkFRY2ZrzLVRa-BQq-MK7FCQ_GG8hXhQsVA4QflR1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-pjVo1z1mxNvqt3IzM6vbRpTM4Kv8bhSjuqHap-2_aTDu3ojMiAY3DxnQpMbLnq-2Jstq8hkpXYyEAOngIab8fUbq5Km322YZzJKI-oxywnnfu9n8w0DNzaWAowTwwNxY2q_7DAd1-fysW_jD5T4msfbgn4PphwJcKxFBn_iu1CxYwMOfPJw1hmyUtAlEqO3Bqq0RIFU9cZaCzTEIqgkTcRtBwZ4pGqRcR3JArrlmxGLUaDg4T5Z2RItM8-se5i1P5vv1jIS3VfezChV8D6auKYAcVPmM8Rr3uX3w2axfVejv_wpePAB9ewUBCCFwIiqa_MfEZVE1RtCl8YHGXuaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-re4pGNje3rReGEovwnVAP5zLzjS16mHx9JCdG1X0k2gTdJatOCPaZgY-dwDV8bZFzEMD-JPxQmuvuiQe9qQk0RlS13fsEdHDlhQAXZO5CxZobaPtBMYWFlyevAPD_G0HrFPaViCXg1HEmVSmX2GJ51lU7S2dd6F20HWgmO4RbEjH2hnW-tPobIzAwi5RJUwpgUuFHRcKAzkI7np6t8U7XUuD1uHKDE9XsFV46kQ7oP4_qR6gqP-gEEzZAaB_lMZDSX0DNXK8qtVLYm9MXOBtLLFBkvR7dtM2eGDNOc9QuvG56IK6uLI5DXDPg_XarzW7WuRG4z2GCiw0hS0GcIuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dmkjtktQAV60YFpvYbNwJljMCoiYDDcCkY45KyBol77uBjjaIsKMephM6l3cWf2_C0y_1uCO6ZMZmj--iKAU_jnDg8sGVszexGshJAlOqhv1opsg4ehS7I2xXZz4ocA0W0HKfpJeCkk2i0vGIripnpE_CVcf3Op8tN5yFNURLfiti_97YoZjJQn7EDxagN2LB9p7U88ZXgH1x4HnWCyWfY40N7ZlMtUrD_LXRJnGVCl7nu2AOnAChhjBqzKOmcg7dRPhxmCFS2wWBdGPgant79x76dtk5Yat6kEgMfFLGhTYLH9HrUorSYoZbpBtR1z-y_MdQ30Lv8QgfGkDJ7SRag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j54s1DLdmzNT4P7gn1WkmP2il5WQ27KCneRQtjydWoHZJJu1mFYH64hAjrXrFiEkywP3DsXqmqjDxLtsTr4Rcl16XdeWL4JWdL6R_94BSvKyOEmsEIkL6ynnw37JRwDzwdDZbFaHOItMpzWeqDmmI7oRG05gRVhzimZ55EuX8cCpIp23RS8UzAyTjnSRGkl76l2-9w7Zjh4laxWuo3yE5-AJoZmXBhQBbbHZSEV2BodsMWRe5iiTfX1N8wx_Mp4GDxVNTr_mWh2in1x9DBpCEZK4b8hLV4xPUDUWBr5-xm3cyteGDvZwUcKNVLaJ4tRwq_Itc6SMbGZNaaHFpgcvTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zkp4dFgytxX-Mf-crDdVmSzbweWacG51zYD38EZJ8S9BNK_o4dnKpGtesYMu0QLCfEbSZ-L4HgO9ZApCfaL4-LKO1-8bNlIxb5BHCaxMZ5F-UJtySFArT-KQYjcEHTfGEvPIMGdqlyfgzfXJ8zHbbFXLD4weCYQhL2r_SfHAxSF_4rboi3e7EPtzuvx7Zc2cDhO5BbGIpp4fcObgXuOVLlS-GNHGu1csWlYxMnC7isAvU9KY_TSROh9CS04RbMN2t4gOWDpwHkxtGFZdy_XMovpYYcdaImD22HJBn3xBWOoOcttc1T_bNrJJmDtKeLAx6yuM_dJhZ7tSurf9EAl4vA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nn_6ee94XB6cIwOpx0GCFh_u2ncRi-9gaknK0H37-gSrJWyd5ltQlbRgVSrKba34lIc3xxfBnMXnQ9ZiJp8vb6fT_mnJBpCtpQQ98VxEWQZUYOZaZ9w2o89QjPWCuxzzO5qvvJqKNULySobBPshoRJ8bgcvH7HVPbZq7cEPvVUG97CvDWs0fHj0EThbbhq4t0haEKq8cpZB4ytkccKWylh7lo2YxR2oHe7YrEWldJ-GwdqE1asRMJjEEUVJfQSHAZ7hb-5w-K5N9iiOUEBiiaj9_m1hVM_fkQgORFmwDbN1cDnTHkfpZcFoKkzbM43t3L3RANYpF7L1VM1PieZDHCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKcTi9WZKUt2LswarJ5fTDfHxomIGxbK5t4v_9dgPnItIw1W28wMT5V8WwbVJE_LNe4R1OgjaA59IMobW7hLRY6siOrcqyqDOMS_UVNwcQgpDkIDsjmqsGBiueh2DqdF67OgQXoq7J4HoEYnwHwKYUxvqo-rR5XnFrZ8TTj-aWeEyyfXyQYos4h3FUDhgyFr2g3IuULkii_TkV-T9T2abxXkOE7v_IhAHtbVGfaMln9ITObBy-mBD--1N_jkNa6V8qTfjdHqBuvXoGT10P5mW9ZpL-jgHhCAjziUrZPRO5--6-8acGoiT7AQVhaSHlkRNAL5R6NrNZ42vQ3AUxwMqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXdT-1HeZz5wMcJQtbJT8Wy6phmn4X2Hpk-lBfrH20DNDqkr5w7j9r5KzXT8W_jAGYx5XtQLcd4MGqM5Bnd-BfrivJ9Ow3eur2l9lmPb1f3M5XufHQ07grscnLbpipET5Y0eslt1LZ_ZKA6KLkXQxD8JSjzoboJmfG41i595fufTiIY0g9LWDF23uBW2fVPfALNqJ-igKj95DLhXxeUbChDxRUuk31hXYRMdrmDp9rrprJhwjH0Z6MIKWcLJqTOdMDcMj6XHRUqbxS8aAH9Vql5tziHXFcCBirjZUHITlJmc3qN_cyH6Fiwgb10vR1cLexuTyYAyT32qRWksM6MMrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oXFiNxHZxu77IHD3BCmX3Z36Bl-sY5dsBZ24NUqxeEMeeCoujgEelYW7oWQbQ4xKZS0NvCIuuACD_ZDiWNG4uUwKgvn6v-eXoYeahEVIzQYV6r8YU4OJaX4PjEf9AgWS7a1yJr9rKZgcJGMXyQ70fjixNt_wMUsSmxWBKnAuTVzbzMGVwglodmyc2_UMlHhjt84cfFcUCWLFqBxXOSgSIWhqcunyFNwRnW3UYMymWuTYSE3bMysC_yayZBSHXnHUzQnBw4SxknY6kqJO0kcqB3IhSQeSpMf3LLwI_FdWNVTJfhCtk2SN8YHk5LX1UL2ZOLg6R4evvkr-gYEdqx32Iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k_7sWVXH-J49O5qxf7cWg7wLM5myXBmQKdwLhv3nwjINv4oNWnINS8vGxjUrjFglzSfwwapUxNajNiOKrldSVQIm9jEXDN2bJP0JgLYbyfdlYDR6w_4SXJnil4P7hxq_K4hH2VXZj2uPW11oMWEAKtSXtVlStBktk42TdhC5TkT7MVCmfah8vCNquiTCEU-ED6Vw3U8fyWGL12UP-J3YWbKJebZc7KL7k8cucTAoE1Ns6d3SX3dnpJdB8UWFx9wbDZ1NVR4fF5al6wIZTZQU7qQqiCNSBGAM8IW4uzCAJ1QNg8DPM8askCTLU644QkAt9TJzfuSVfZWsj9KSe55Ekg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OTnmGsQXxE0ZFbO32fbTHlb2fgiXJXQng5QXp-thvcUU7WuWKG6aF92g1y9DrRfb7nba5URb5vlaafxDwsRd45rTYjox-eY6mPsDMrbvtLZwU9ck93ZFqCpAwXPaxg8O4XcxeKJhh_tDlFLxD9Rbf7DVLe3az8u8h77wIbkTahiEW6WGYfqwqZuWWbpa9qO50SP0VxbPBASsqxZd8sEe4QvxFJJgvVtQyWgKr2eKSH8PA1AeeKX9twZMgUUJv8uzbD00qrmQhLKvO_cp_Ks6i3qfDcbtwE3PmuoCaf1lOWqPizDdTZiymI0sVbiKS8AYDPcvvlA6-JhwjhSOrEPEcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYGpBQLtPTttuybBB1bNY69JIT6gpdZJQ_DEBwa5Nc9ncPhRhkfkspPE638qoFNWXTsmH_rkViIHHB2bpxvlUfBXewkHjox9xkrXIVvpks1tzFZbMo9uKWYl2YTUAauJc11EmxDeRCCvjJbBuWt2mQdN7FG2Be6ihcPU3beInl1Z4Mf_wnREdNPI9MxPrAAxeJGj9UTMyOFhzlBCAWFrFJbBqUKHmTZcsnvRSlLI8GObH4hHtVnGpZylOzchF_F83qmvEkQM4MtJf1-sPpGhMFj7pJwR_tniTCu5CR41NF_58M-urb1tI5GesV4OjaNsaXigZKXjGF8ix33lr7G5Qw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=UTUkmjXzjMQpcSqVQcttAbQBOtPSUWUxyphqUtflfcYtyZK-vtM3nwcABAndNoi4VVKxqPyTFZAsEJCo2pIhI7q0J_AVcaAbB_ZpI5BjH2PWtVUFewUYb_aDNV8Lr8JyzdXxnbLVPojrNQo7i1e62nB0J8mScX0WIx1RaxLUach4fy2SUwZdct9nusCbZJ_s_HXPEVHwRPtIAVoL71QmsXd05i9sagmlq9XPipxWCnvNeS_Q5vy6ALkSQ3BWe8AEUCdJMBuRm_qptBXVWrAjnthDIvGbJ93NYNIsV-ov27bhDekMD_OiBl6CZdYLkspNO4MvuC3z_Yp3gOw0gZKdng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=UTUkmjXzjMQpcSqVQcttAbQBOtPSUWUxyphqUtflfcYtyZK-vtM3nwcABAndNoi4VVKxqPyTFZAsEJCo2pIhI7q0J_AVcaAbB_ZpI5BjH2PWtVUFewUYb_aDNV8Lr8JyzdXxnbLVPojrNQo7i1e62nB0J8mScX0WIx1RaxLUach4fy2SUwZdct9nusCbZJ_s_HXPEVHwRPtIAVoL71QmsXd05i9sagmlq9XPipxWCnvNeS_Q5vy6ALkSQ3BWe8AEUCdJMBuRm_qptBXVWrAjnthDIvGbJ93NYNIsV-ov27bhDekMD_OiBl6CZdYLkspNO4MvuC3z_Yp3gOw0gZKdng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwXGR2r_7Poir24uO-lNQPXiATUjrttSrxbenFGyGtlFTwr-vaa93BzxjigSMPWTf2BTyJxJBuAL0BDumEkDO8Ov62fc5sngvZLHaVXb7GmjDX5WxXCYi-Yw6YWjwhrY7sMyBbvifJT9fNM8HD_aukzYqMQoxD7aKUVQPM0ItDLlFCfmvn_m5DMz_JwE-NxHJWcjTz_cHwUVc6AhhEqrXnn_6wwOgeWG6KlTRbphL5EuyZWHQeuMGregEcP3-gAZdieG5AeVV5HaTi5_xZrFRKo17586dFiYPlZ0giHnW2dsbrpAnoQzq64ilayyEstipt5yleJ-a8J_93QwLeHYVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/in7-Jn-J_rov_LkGtyxo-anlyVnrvWwJlO6oUY-pcdKFNn4GlF95pPgxOmXOwHYosl7SjuKt4tpFDk5GSi52XoyCSxqAzT3hE-HqZCCByIFCJh6Mf8qSeO15XMtnNJgjlJ-jUgrh43bPbi3HgrpIzPw_T_RMu2u9tvvgngWWoVkgg1sZXFkGsPdXrnMW-4YVLkBlyWpuUsgjDcuT96dVAghXYJA5NScYuWwJgNql3cz6Ae-H8VdsLoyhBG_44AGKwvuXdck1nCgxC9KAAQrw0kzB4Vu1I8xFKutRmBDVYzhrKs9O6oKxoKW_MgRvBM_KuiCj25fMYlCxparqL5vPDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIbRKJIFtoqSQ9_ESZS1F_oGcXTq3YGlkyASd7_rTQqvl8aOGxVxtOnm0_PH-BtKd5h05w-5CBZGF0OMkcKf5NxuUUlvGS0zzmLOc4zsOtx35OGUaWUj059miLpWaB19GIK-njIbrXjJ0OetQ5de0aB37CkwLqNzbl5ESpMmX2J7qCtu1koF8t6Zm7HLS_dC6_gDoTSJpBfDQiQyjHl7ytNuqfqOuFVKAx823EdQPypxendvz-XUn6A4VfrQaboQWujJ8LBXZiVVak3DVHv75caGzGuABfMDxkzyK0gc1IaqHfGbnqi_gnXkwQy2IGhH84lv-AgTvsS_JJ8_EbfgHw.jpg" alt="photo" loading="lazy"/></div>
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
