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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 19:04:48</div>
<hr>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjOPiJkM5-EEDM6Bj7OV6FYwa6uuVXOBiL-mXDklkcvICj9qBgt2UZtADLR8kiyyeOHfyQcn0FfLZdo9ahC6WTCE0Gy3eF6J_AGRCc6jpnP73GoufsqCZZNizMdGkZTUO49khBUxM4Y6TBU2vIOrdghJElvyZEl5IEKOaMh7yuWN69SA0jg0l0idBUPSC9aBI8wPpcNuXekSRjEz7Jvd8TkQdToAqfOjoCcsa8Qgze6YuKR176p9Qk2dAQHVGpE4zzljhITcIpBkHsGB0OiIhUdx0VZqTRhxzBzphO0T1rgW6byolugK1p47bRTt68SFGrPMKK28I-AJjm0aM8p2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjIQTM80iQK69zWeK1zv2hRR6NfL3wncov7BnLo3ze6n_keZzpyBK1vl5c4KapxAjE3O0y6vVlg8WgIA2uFu9ji5D8zywqX9ho0Kqvr_2fcYIHssdNypK6zYLRgiyV7lmBr5XMuduQIcUo85FnSXHKTF21c5j51idawfac2Bw0DCD44sZJZghFvZwzJqcrlEZlB_LW6QE5nHkDmtkH6fA2YqMQG5HTtD6v8ISDpmyT9QyyxsXk4wN47Lc-AqMHkeTwWzW9uARkCB7smN3iFsM1nEqy4MCf1aMQk7sSZ1R7i_DyDjHRlIHDFXBPsmRuiUmnO9GAaYzkOS1EObA5m8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5SNeWkjycX6gsJJwtvo20Mpl26SZZjX19Gi5my1d3P89yGGHjNGX5Nb7B9HX3xHy1hSjl1LHA2YguAot4MmdK9Iqc2jXoJdEQJuGH_hl_a6SzgMO_5Q2_Q4ueCYlF9SWiYxniCXq7mimIN5jvMhQL8V-LgiZPrRMmFrwC7D8xQOkAVJ_jbDkFDgbJGLV3-I9-I58jLC6-5e9E65UTRvfMOvsufXjtX96ST-BYDKr1xk33PWoaF0-KoIJbmhf3vHtfYb8KpmjX4H60z4_JGadulFYnxuXRxALiwZYDfx2YkROe3M9MjCs44ByzEDodPV_Qn10wxXaVt0y3ID6TVyfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0dbeuUShWM30A_kcihgPofaUCtPNvenAZqq6Y6HkEQ0PEo-xt4qg281D3PmxKVo0S6c3h5XGhG8roFn54Osm0dfLCMx1fNM_hRpo24dJrmZdIImiAVEEGl2n1Asn5OaWQtL_Rx9fHVJ62o0Ml6hs2t0NcQ9RKKXIvTPQb0bWDzKZrxFtDLuS32HRey8R35BESCXF8ZoIJfE22sRsn0N0te6LMPVJ3KwEZUFjyPtTkcI0P0XQiZwGOt24oXXc8qmz5oRQy2tH3uLEON-I7dvVbMOtYa3HajQA_2JT-widb9tMdfT_g11s9psXz7OkHnf30w6WOZur8mdeCB97sDhYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0zeHLwcL_94UpOnVwHJeR-SjOVAwRNEQoorPnaFWQ1ohNkbzQK4p3iiQl9uEkdgpLe2LnBgv3grpS7bFiErOV3cDg5J7skPJ1Ki4uwUSIpNXd-N78Xy5XMWlb_a8QerRDqBcjhthQRFwffUFxCic89OYyk1zoGFsIXSMCqWdSsN0Z3LWgw5PWsPkrPTiFta-EksSqP8n5_uEJdZHT4kK57drrgogCbn0DMDAxQDxKE7wC3cItTpLv_N1J_jjecwzBtAtuuv3oxcuQ9rcVjp2y0oUeZUXqr88NGUkO_6atSFzTMtaiZB_ti_i1XeA0NO4YNHIzjrFR4kBNQDHyh7Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5P76CyG4bVOYZoppovkF2x3KEB2a0Bm8ajKs3D4u0xTvsXMf4OYFfV8M49NvXT8IRKwANSh1ScxXHMGskLkujk2SYWBPtDpjAl46UvK4S6OGqAkva3ZEpS3CXjeC-0eeRqDuptKGmQMtplBiRMhwiQsMFKcUs2x2HNZDlMo9_W_qMjhKWuJuhLkms754rUBXzBsSDUNadQsSWxxtfC8x9dERl6p_eYSw6Z-mLIfXVrJkUEMp6j2RQzJjf28ojuskHK9vYH9r_WP4hQByAe_OxxpXnf1Se9jyYLQpR4bRv3un-h9NdgIAi28xGbzwzlkITL6IGlMWozSljuzOyEVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLWvRidvF2WGX36rJFyIkgIwMU8tz8LI1R-TjkWtDoaERDn2JcMfma3Q7dP8EIs_jRegQ0dIh3TLudy0PfUgwTUDcJTqdMdrkrk4ng3c08s-aKyfzgOlabmkZYEKrPfJ0fLz7uqIOaX4kiYylFMCzCMZlmED0hTfpoNNlnW0_w5KhXtk6CtgXIE7Yux4q3PNQACmqO-SmVqFStMtIXYbudWQSHcBuwg9KKTG9NgTNq1Ntf5wVpT8lX2mWEEnwUtyE9ul4XcU3Ab1ufnofnPVjn7IPANWiqY8r0C3IbmKPBLZ5FGqWr8-KnmX0-Pv5ufuK_OOhabkqLEbXY50RDJlAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=epwSbDFccUQ7k0o5tbn8RVo6rNJUHV5KrpNQfy6PqGMnjPhLqBGAHst5B1CVf4A4EKaefDz1-TnVcvyazkzZP_rcTlsJLudy61CIoKrEx7BGt3QL9HliAkuLG9fZZ5niJXG0TtMsAA74MKHv46_8okFsy1D3v8gxfL82x_8akuWzHRjRp5zdNul8sVlgDv5ZtVjOdIN8CPYm0px4wKoDRUrH-R3e-DwE8sINQb8BF8DuwSRYPlMtL3g2LxDQ4CVQcPeh3pywkJS9fevYclGnsHmUwLaNZQHibmYDzZpNVvctzocsNCt4OpAadWcmRBHp3Nt5DAyofyCPR2t-GDfdAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=epwSbDFccUQ7k0o5tbn8RVo6rNJUHV5KrpNQfy6PqGMnjPhLqBGAHst5B1CVf4A4EKaefDz1-TnVcvyazkzZP_rcTlsJLudy61CIoKrEx7BGt3QL9HliAkuLG9fZZ5niJXG0TtMsAA74MKHv46_8okFsy1D3v8gxfL82x_8akuWzHRjRp5zdNul8sVlgDv5ZtVjOdIN8CPYm0px4wKoDRUrH-R3e-DwE8sINQb8BF8DuwSRYPlMtL3g2LxDQ4CVQcPeh3pywkJS9fevYclGnsHmUwLaNZQHibmYDzZpNVvctzocsNCt4OpAadWcmRBHp3Nt5DAyofyCPR2t-GDfdAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEXtfY8-FEUVtVRd5xFjB7FTDSe3H-iwxnqqV4pDaLdkv0y7wbH0AXhiWInvM1lBBqrvzxqKv2iNdnxi0KUn1Ar_hxL1JYTFcgkKNVTDAzSFwNpn4JAq4ySOeEHQ0G2P827Nz3JrOA_hK1_ex3B-i-CB-8rjALMoiXsNCrr55NwigTZEG4TpaGuYWY8FxGPhSh33Rvg49G_ah-EwktzSJjGN0mYDf5sN8LvAcuuG5TRqW_b6ZQCm1IiFiBoABDuYEQub4Gx9WXdbQZMWwV0To61Ic3vgcleuZTBnmShL9terCQdWPlTGWrZBtNBeGNtE3D1XpjQgYNvBYjV_OpIW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbjCfFse6t1YbjGml3SlfdHI1-j75JHeGDhn4CS_Sz-Rd--b5MZznij5rB4fQ4rEKfwImdBEWA-mRXcsH0yGj4aSfxDjXKmsln8BTxFIyRyf27zQwZMl5Phoen1u2BSs-VNlElHQzEHHRLuJqzEbHgJFBpglCiSpdMe3gbomE3CGpb1yXPwMsydJY8PR4jOBjywxPBDamF1tyPmULlV3w2BgKY54m-6EcAgSpIZ2NnxkQHMUws0yY5A-jGdlu1A3uzjBtvABiqALg-v8C9G-MZ_Sn4QaMV6CaiaelQ_J-JpPbTah2xg8Bp7h8loPSGRqbuEO7jK6KHPygUymChN3bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ijcuw-5ciz40_ZiXHg2sKAPVPZyWFNrZQtAhsx7FqEbRaazz7BOdbQN8yzPmu5qTLeTuFmcwl2EMLvTaiuOuynvhn409RihWd4PZ5omK_iazIXLuGekF3Ag-hgek_HltpzsEh0ivN4vZNnYH0T58qZI0Y5m5FjeKxDxlYnLGq3BsjQmBaM4-R25cYQHi8FKhxjZDjLeJ2bO4PAKQV-IWNoEpWFRRXED2FJ3W6kG2kNahCVnT-0712xBrQJnXME6QjAUmRBFoynV5oEFdLMbm9r--RLz_nmNqrnTT7cUPKFuCuN9YQLKQgzBerGthXkXfLAbNEt8lEgtW1W2QVDAmSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQkPLrhj-titKRKHHAP81Rfz5Glgg1fVqesasC1Mh4NJOZRWF24RbgqT8632qm_Uvas5TFV8ZOWdTSei84_Y73KLfdVdkBZzwvrUx4Q7YISmLlN5W92iPhIOVBCDKPy-1o9BfskNYqwZ5VkLlm2SfXG6SCoqYaVqOJSlHiblQwi8W_kSKkv_extXawn4EI7f__UPF6AZ1j046tKtlFrCd1eMoB9OVzLLwdQsGHeyBDm88Z9eWaP9HPhtYiLUgqlmWTKBgxrMWBCWP5JxDhZ6cw3eX_bTMygLFesO4tP2jDhYzMI3XSi6rlAU_hobFX1SXs65CHpOM2DT4zGUHtyE4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJTbJSpqbqSaOCek2vdptcdZUu4kyEq5SZTIs0BfZPVY7YFEAkjrJLQ6oNUGUPW_FXV1TuLMrCt4NorkCr_W2QwBW2KGd6WMhWKthJn6rQIHY2_ihhjonyp2rYAQxoiqzjKaSwm6bWAq3fnAqHjvjtdO63qTBfy2gw8CR5q1i4cd0Ma3QTER7UzJF9qp0yp0NApfwuLFxjHf2TFOkDDgavENc5pvQB8qrb_oPpmZB1wnYE3Tjiv79-ccH96dWD0qBxHYTpChQRaiKLqYKsmo-vI9pd8XjfFY8YNsJx3e7lkGWxFbuBelrCIaFIAoeIzJ-Ylwe-napoYGevUq4aEFhlWk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJTbJSpqbqSaOCek2vdptcdZUu4kyEq5SZTIs0BfZPVY7YFEAkjrJLQ6oNUGUPW_FXV1TuLMrCt4NorkCr_W2QwBW2KGd6WMhWKthJn6rQIHY2_ihhjonyp2rYAQxoiqzjKaSwm6bWAq3fnAqHjvjtdO63qTBfy2gw8CR5q1i4cd0Ma3QTER7UzJF9qp0yp0NApfwuLFxjHf2TFOkDDgavENc5pvQB8qrb_oPpmZB1wnYE3Tjiv79-ccH96dWD0qBxHYTpChQRaiKLqYKsmo-vI9pd8XjfFY8YNsJx3e7lkGWxFbuBelrCIaFIAoeIzJ-Ylwe-napoYGevUq4aEFhlWk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnEmiwrkOCmmcckACx6StekFIyu0bfnbFPwNOgioUX3-q3BNqqUckxmcybSJQQhqOUZM1e_DbBmjhKNuJ_UpHT_pcRrR8TXUQkdSLjI2DOuIqKT5vRgxkGejm19VyTEZhCU8fk51X2V3hluTWXJEbUtDxAS2-MgJ_K0fFRa7yaXyznYuOhiTyZNV-iji1UmhCrg09UlMqsSN3K2iauKzOEzCuZSojYIDvAXpBEirNAJ8WLRS8Sa0mHYdXSlaO4osU3rFv9Se0r3_3fpoVWuHVI1bP2CrcoaidnMI-o4vEO7lR4x7iJtinSKLwPU6Ex7H_T9Ahv-LHS7t8hsUzZGF3_H0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnEmiwrkOCmmcckACx6StekFIyu0bfnbFPwNOgioUX3-q3BNqqUckxmcybSJQQhqOUZM1e_DbBmjhKNuJ_UpHT_pcRrR8TXUQkdSLjI2DOuIqKT5vRgxkGejm19VyTEZhCU8fk51X2V3hluTWXJEbUtDxAS2-MgJ_K0fFRa7yaXyznYuOhiTyZNV-iji1UmhCrg09UlMqsSN3K2iauKzOEzCuZSojYIDvAXpBEirNAJ8WLRS8Sa0mHYdXSlaO4osU3rFv9Se0r3_3fpoVWuHVI1bP2CrcoaidnMI-o4vEO7lR4x7iJtinSKLwPU6Ex7H_T9Ahv-LHS7t8hsUzZGF3_H0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=H53NeDBn396VwzPfDraeJao7y6e7Coxhdw-p9o88SVYLjmMRV3MTfu-fO9_ubKJ9RiUj8L1zQLS8e0VTRNv2XucFzr0cl0jJ1vTvgv2rL4nt2oE9L8Ubhf43FLkUK56hnSTQ_4lGB2LZQkcsdJMmXynrsHTlFLrxL4A0CizlnTrT9nwLzj12Z_U4Qy7LxWn3d4DBXlU59-oBFaoFlZAq5beSy_61vQI1CCEG4bJ3mU0deZMRE9FZAIYibKipZLSECNTCf9uz5548Y8dlaWAO1vxo1qdKn_9bUjr3Q5mH55mkfxQOFDp7jRx5JbqlrsoJGAl_jpgX46Qke_BvPQuvBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=H53NeDBn396VwzPfDraeJao7y6e7Coxhdw-p9o88SVYLjmMRV3MTfu-fO9_ubKJ9RiUj8L1zQLS8e0VTRNv2XucFzr0cl0jJ1vTvgv2rL4nt2oE9L8Ubhf43FLkUK56hnSTQ_4lGB2LZQkcsdJMmXynrsHTlFLrxL4A0CizlnTrT9nwLzj12Z_U4Qy7LxWn3d4DBXlU59-oBFaoFlZAq5beSy_61vQI1CCEG4bJ3mU0deZMRE9FZAIYibKipZLSECNTCf9uz5548Y8dlaWAO1vxo1qdKn_9bUjr3Q5mH55mkfxQOFDp7jRx5JbqlrsoJGAl_jpgX46Qke_BvPQuvBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WG8MwYaJOsydNebQq0-o9ZvK-7sdCWBv_pRDwRL2JO8r-ARRTi7msghU90XrCME10q3HXcjgbF0MUA1_AhXO_Aw8d_YOWPzLBsYbAgwfpKfCsQWG4gRlo74xJOJ_bPjE3lGpKcVBkIZjO9_ZjnkM6xz9FhNhEW5mh-43t-hWXgKax2T5zd_ZbM6wVNGkw7MercNbhE8wpHwGzdLWdQiwArpLLoHuQcPJibw8oFbWu4ESpFgEqYHr1iaMyfBi69cV8IDbEoPw8glMKBiRoZc9OE__rVniWgHhG2U_EfJENzs5ovTBxWO0kuIX5cZKt3uymWAcFO9Z-dTOoK_8fxf_2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVU4gzS01o1j3l6gn9BojFej6uM7f8Hc5NfNfa1UCyPU_kAHNM27dd9zh7dRVFfRbfLUx5nYfHizTXEc7JQYVCbfqbsx6v4RiuY26LaWBwIpLMM3xBcR1QUXku60k0sr31rfyGuQDOSU1HimjB9PJWAJ6tFD_RKYtdtWUN2fabyF6ZKFQeB449qB7AUe2VuqaBIg9z_duCqP1WaTr57V8jenXVtq4eGT4S8GaJhdN-U0tFcAvgrjfeFKjhq6EKEeurkQ3PkHfJ49WFLdUUmvklGmX9pISfYyD3Or0RPcJGdGhj_ZUkMxrq2cmogKbu6pD3IMSQ1dl8pOsQTgYOCGYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=ARbEcvxowumP_yUccmXb91dGt1r_AZ0_NJ3KS-BxMPi2ezUZ0vXf8OrIT5mK94CBkhVZ27UjzHXNMW0VeMZLGtkY0z5_jH8VQTCwnBc3J-bTQ63tCXu6CKqO5-JWUMHtGyEiZA40a9U4W9XSJYk5EYVFOBsDomEg4k6rZc6t3ZF3bMt6I1i4XP2DzTc7v0uXL-B-oE5UusAgrgiJU15X95QtFtp7rxFX3xa6LjObTBAF5XShxBiGU3SC-9WqIT100ZWY7OH1sSVlDJU7RZLCpF31rBgJuv1Iylf2BaUholczgQTDv6MaQLcQmOIQYnQhsEkYV8O0opLEf_cXQny_ZSoVBCp2NbCqxdnYwoH8pxPU02n7kq9nhUqdloAgwwI92iPQ3tN7x9QnViJim79cJk50toJyzUZBeKcxBtib4TdQZ7qt8pFUHbS2XIyQ9bD-7BelvskNAT3NRoBPz3IVXfG-nIM9oJmjVw_4WT9Z_iH2ONhWR-zMdJZmscQYDQCJi_83M64jqzRl9l1uGpQQBPcwBcLPXLH8ahoAFNnu1fqt2lqfiOXCREbIvcOx96Mbhtv8R9YsSnu4qJt7zznHvabYQTNa87f3TZ1232cycylZLC8GMlsPq3i28CUGAy-MKAO_h86Bsb0b94TuGuNpE6Kf5fxdXoUDMM_jz8-Vb6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=ARbEcvxowumP_yUccmXb91dGt1r_AZ0_NJ3KS-BxMPi2ezUZ0vXf8OrIT5mK94CBkhVZ27UjzHXNMW0VeMZLGtkY0z5_jH8VQTCwnBc3J-bTQ63tCXu6CKqO5-JWUMHtGyEiZA40a9U4W9XSJYk5EYVFOBsDomEg4k6rZc6t3ZF3bMt6I1i4XP2DzTc7v0uXL-B-oE5UusAgrgiJU15X95QtFtp7rxFX3xa6LjObTBAF5XShxBiGU3SC-9WqIT100ZWY7OH1sSVlDJU7RZLCpF31rBgJuv1Iylf2BaUholczgQTDv6MaQLcQmOIQYnQhsEkYV8O0opLEf_cXQny_ZSoVBCp2NbCqxdnYwoH8pxPU02n7kq9nhUqdloAgwwI92iPQ3tN7x9QnViJim79cJk50toJyzUZBeKcxBtib4TdQZ7qt8pFUHbS2XIyQ9bD-7BelvskNAT3NRoBPz3IVXfG-nIM9oJmjVw_4WT9Z_iH2ONhWR-zMdJZmscQYDQCJi_83M64jqzRl9l1uGpQQBPcwBcLPXLH8ahoAFNnu1fqt2lqfiOXCREbIvcOx96Mbhtv8R9YsSnu4qJt7zznHvabYQTNa87f3TZ1232cycylZLC8GMlsPq3i28CUGAy-MKAO_h86Bsb0b94TuGuNpE6Kf5fxdXoUDMM_jz8-Vb6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=ACVPuaA03d4GIcdoBp6K65cdYWn-sxwTH9_52DdnKZvq_a3ldR-RJP-AJZ0YXDhmycuAW0kI6AZhXGbMUEvX9SztoAcneWKb4z1EdZnFK49-rNRcEAk0R4OkmhkCZeg-jaSDfIr_0EgskhtifydK5L7vjKSkHDs_NSCeSTZFUJ4gz9yDisrVSpx_BE4oQ4uFr1Snp2O-H-NkOCjDiQu84f4xG3HuT1fMagz47FGEwVLhtFzVjH7xW0npPEtjj0aNSH2syz9o7Kz2JVfbj65pjdwlLkSIRQ_PxUT56XOVFgb6OAkzVV-iqTREaU9clPvb28FL-EjHiZGFv7VzkOi5CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=ACVPuaA03d4GIcdoBp6K65cdYWn-sxwTH9_52DdnKZvq_a3ldR-RJP-AJZ0YXDhmycuAW0kI6AZhXGbMUEvX9SztoAcneWKb4z1EdZnFK49-rNRcEAk0R4OkmhkCZeg-jaSDfIr_0EgskhtifydK5L7vjKSkHDs_NSCeSTZFUJ4gz9yDisrVSpx_BE4oQ4uFr1Snp2O-H-NkOCjDiQu84f4xG3HuT1fMagz47FGEwVLhtFzVjH7xW0npPEtjj0aNSH2syz9o7Kz2JVfbj65pjdwlLkSIRQ_PxUT56XOVFgb6OAkzVV-iqTREaU9clPvb28FL-EjHiZGFv7VzkOi5CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9_ClW-d7iqtz_cBu-pU03AditGyTCxsVgpxbEX24TpFfpz3jHS7fc0FGkKNL01s4a7aZlVrQeuM9cdSYvc8EfPxWbJwPS-fk9euDDhNXZ3E356tW4rTWurcFli-2CDvc5NZ2qUcPC8zHDhha-0MSgCDpHUGXnBzLPusdstxIZ7KwEgSgipMZvAqqU5Mm4TG4KO2mnkSWczLQVva7snxa2LnHJYFMn30NF1n-H6iem7m6qYlNYArAicFF0wg25yjQyzokWHZRNIboKcK_2G4CIMA_SwIlw8NADSzUxa1aUwkSSM4ZpxOdIMrdus8Eq6H0I7CU0aePaHSgIY-YPh22A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z_iZvD0tbYWWOFR58V-YIz-tVzfRJKXO--_IK_KD1R2CeOpm_wPSN3z9uRGHb_CN7PPU43XnlPpeesnFw--SMR-1tmwXa0nOqLoIGuXHh_M7B8LolBgVjvGJHwSokFb3hqltFsPHsFQ1bSZ-I_Rj2tek4ZwSEEHxF_vSUTWUOA1kVqt8gGnXUn_GVbXunmdlnEn_gkbjrgl27v4741RYKR3WuFwo-ysgPb6dGlBurJGTqZSOq2gd-DiMUey-MUcoyd7faM6GW3dBdSVhmcjW49zYKQTRL9idXsk9G913rACzvOA93wtynvmO59kFLTB7u7VIJcE5FsAzSSgTPBEZ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZ9uRXJ2EAUJ_4xr_XFrxu_IusCszr_vi-QRQkrYaIHwQ5MIUSHDn_CR6N9jk7pAY90rBbCy42WqRPbQq0OrJ6-lyPu4nZwnwM-79T9O-E1GuPijA2mMVsChLEJDL1mookb92qToPqt1ZT0yDbv22krQ3LYjtt4GpQQmes3D4i3cWkqhX0JwnDd3bMpEgFYM7JD_hhl-x44SjcAI2DLWSXFlU4w2QfkzYvQjPHbLRg7U2hP2w8RxtOqlEuORaRin3lsvIS3capytft-d_epZSQA1k6Jm2dK3d8ckn_jrpP38XfCT3uJImcfbXITFM6PuLY_EJaJ-wj0i10aDxgs4PA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=cvZfu-LfMr15lFbRSh6b39mky7wJBopZXE9djTfqQKKqOIU-YG6h4Tth7njRIAd__wUzw9wMsezVRrXhgsUqn4eI2t_6MdxBkqpr9-V4tBaP0OInhUOB6X_T1X-ABjt4ECPQGpxD3Y4mpybq22hjUSsIgozqMA9HDt_dFFLiuqFTxUx0aj5VeCLK3QJ9quTKW4Oj9vm6MpVH8cu9oluHtF2fsvBdql-QRxe7m6DVuf60lnxByOli6iYhAD70RozX9KrjOX4eBnQNFMEYlQ6vFsLOf6ADPe0G68yqStEYz8DGReOogsPV89nWMTHHIdciTrRcgYWEPDcfSi72uR0HAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=cvZfu-LfMr15lFbRSh6b39mky7wJBopZXE9djTfqQKKqOIU-YG6h4Tth7njRIAd__wUzw9wMsezVRrXhgsUqn4eI2t_6MdxBkqpr9-V4tBaP0OInhUOB6X_T1X-ABjt4ECPQGpxD3Y4mpybq22hjUSsIgozqMA9HDt_dFFLiuqFTxUx0aj5VeCLK3QJ9quTKW4Oj9vm6MpVH8cu9oluHtF2fsvBdql-QRxe7m6DVuf60lnxByOli6iYhAD70RozX9KrjOX4eBnQNFMEYlQ6vFsLOf6ADPe0G68yqStEYz8DGReOogsPV89nWMTHHIdciTrRcgYWEPDcfSi72uR0HAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=Rui_wkuQM2b_Jtip77xYzOyrUevN4ao_AbB8Qn3Zuth3ll_gOzJschAMj1fMSVC2U97fTiAj7HGlDefMHFTut-alJliAR6pDk6CJbZPvfQ-gtCyQhymh34KkLGA0plw3jxRA2mLF__P22ZbG_TPkb0gl9GMAm2i9WxJwFyhe_Gmw2GA2KkN3zFMWfAVQsWoriWSgD0QVc7Vdud3y2EgJIztToldTlFzMafj8qaLMNC8F8_uKc-wEL2S76wdtUhRk_U0s3swBVcihbdbz_S4iiIVf-EgyR_8DNaGMhdJvmGavV2XUySySGPSaMGXcQbm-63EIC-yfTnFoCeodUjh5HQSWTjJT3A5E6PMEI3Xgg1DZretLMZBRsTVq1LpzHYwJL5coWsfB9PE3vue2_nsEpV5tz9wXaFZ_b2aHttshDEVD7nmqafK0pDK_I3UY3WIjtTR53MUXj9duefOXzRdd6LSd4SdxhncvhgEHiD9kiUrlDbA253PdtNYULakvAwf2uWVQaPOhchVecLWXFiUqCtbeguZvnHqUvaN1NZnHnlAku_Ksx_HAglTIrAlDBugptirT6I25b4IVT1pfdZNBhwkCN_AFAGaEyhbuZKeA5VTPtlH3x42tQt7XDPmlStHPyz7lo8O_xi0-kHZOnBMmkoxHa1XTm5VXzB3466zPMlY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=Rui_wkuQM2b_Jtip77xYzOyrUevN4ao_AbB8Qn3Zuth3ll_gOzJschAMj1fMSVC2U97fTiAj7HGlDefMHFTut-alJliAR6pDk6CJbZPvfQ-gtCyQhymh34KkLGA0plw3jxRA2mLF__P22ZbG_TPkb0gl9GMAm2i9WxJwFyhe_Gmw2GA2KkN3zFMWfAVQsWoriWSgD0QVc7Vdud3y2EgJIztToldTlFzMafj8qaLMNC8F8_uKc-wEL2S76wdtUhRk_U0s3swBVcihbdbz_S4iiIVf-EgyR_8DNaGMhdJvmGavV2XUySySGPSaMGXcQbm-63EIC-yfTnFoCeodUjh5HQSWTjJT3A5E6PMEI3Xgg1DZretLMZBRsTVq1LpzHYwJL5coWsfB9PE3vue2_nsEpV5tz9wXaFZ_b2aHttshDEVD7nmqafK0pDK_I3UY3WIjtTR53MUXj9duefOXzRdd6LSd4SdxhncvhgEHiD9kiUrlDbA253PdtNYULakvAwf2uWVQaPOhchVecLWXFiUqCtbeguZvnHqUvaN1NZnHnlAku_Ksx_HAglTIrAlDBugptirT6I25b4IVT1pfdZNBhwkCN_AFAGaEyhbuZKeA5VTPtlH3x42tQt7XDPmlStHPyz7lo8O_xi0-kHZOnBMmkoxHa1XTm5VXzB3466zPMlY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O99QiuFxySyInU6k3gujLNk3dd84Hx5RdEWv1nCfUisJe94ImzkUdxnWGRqoEFCHzurSPDeEtz8P1dFnYmIH45AeBNhtoB8UfOUOe-t15Qhac2Xu4wxNuPOI0giSSMN5xlEdbFG-vVZ5x6pm9L_PckW-x4S1zYyrbmEXYPvaJdLLC0d0LuMNdniKvH5frPfdJgo8a7oKaAqcsQzwe2u9_JprpbiiYDheHaY6FNRk6zeqOLd_RamsXMZ1h6Pxmz7eRzZdasOprRTWW0ezNrIwi8neerJy0bUiRCO6Sbm_oRGkmxIO9cDoxJj46aE9jdC0zCcr5D5TDRIU-b-XxAjHfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSa3jUggFPf-HxnthkAvFkvnvBQVC7VaM9KcrVKa-Ab43fi2qv_IaE8K5jtQU102dT0Zp9AUHJZqKs-HFZxgrovzZEQxOtK2th0UpdJuLunYq90LuVA0eQLQQt0kZM6EHRKPxkfmY6CtcTvUIFszmEb0GJxjyBaA9XqMVNndOOGdv_7eXPI3ix916YebrV5bji77-K1gvVgFZWk_G0K50U4xio_NklvkCPYedOhoNiG-SW9GUKIVWyqb3EYogL6Emymps6wddSQMnY4BgAWcCWzAVWvMGp_k6CQCzBkcD2BhPE7h7o_90abYVbEzaLA4-K6KR-8PxzSc-oqX78ZLZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=ddRanKHPUT45UZCpTo6GQCejwyboFBWlqS-23tjDWDe90j1NwoLrXWPtqp4wLbXN0t_YFcpBnS69jIQGs67dKtCyuBssFJNZYOOCUqrZ5drUg_MuGsrilliqCjLCDL8FpmwrDYA4OPJ7qgjqvZOet80iJ1ODOiRiVDyP3R0tck_vFxr2JbdtRpINd2nPrwKgaMtlNBtnlJ2wJszIRkbvIlH-Gpwxx6vEDUywjIi3ySaLcpGdg1wmTS71afs1ekXYlQC8ad9cbYpdeil3PVES-NjbNQwJqM77uWXEPOJVkitkljWVOx4d9jiaCkx4EgnsqbN1lQetVWfvDtl2bXrFdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=ddRanKHPUT45UZCpTo6GQCejwyboFBWlqS-23tjDWDe90j1NwoLrXWPtqp4wLbXN0t_YFcpBnS69jIQGs67dKtCyuBssFJNZYOOCUqrZ5drUg_MuGsrilliqCjLCDL8FpmwrDYA4OPJ7qgjqvZOet80iJ1ODOiRiVDyP3R0tck_vFxr2JbdtRpINd2nPrwKgaMtlNBtnlJ2wJszIRkbvIlH-Gpwxx6vEDUywjIi3ySaLcpGdg1wmTS71afs1ekXYlQC8ad9cbYpdeil3PVES-NjbNQwJqM77uWXEPOJVkitkljWVOx4d9jiaCkx4EgnsqbN1lQetVWfvDtl2bXrFdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCxiJ6aZh3bJp_XvZ_GrZu2SYEF1Er6554USUzEDSne6Xk5kCs3cq_RGOXL3ka3CLV8LUwRriiNZu3jgYZkSYXWWhfkH4Aj6ooTwj1FPGgQCcTBdP9yYHs10RNhZPmDTT-Q6Kdz7xNv3MnUywoA_rqLh4t5uWUn9EkvvMFNRhVjT5DD6MSMw2XTUSjkB196TJknfkLD26zGKPIcy5cqUMFTvElWtvWoM4zo1JZD8vcWY7bgX_V9VsDTpcOhtENadAo2uCSK-6Dvh1A6eE--P7kwdIEmMa7cGCbLKhbb_M-2MY0nVAzkBL0IzbGfRl0vdWIf3MaXhphI0vwxOTf54Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KohGzsGUrNAy8OfoPGOmocpVRMfeeZkn7L68OxSqankdbYdkykfM1WYwypbgpglo7sPiUqNO5TyqjnZOLP0hYExAiz88ZZLX6sJAOZ-xwxyDq3zr3uk-1x_Aorc8UH5EUK5MN1CKXBwDRP88meUErJQsM9lF4jX16zArT1LPGOAq7sdnJF-apptVfGh2DSmDg-Z30zmTNvxmHxigcCcFRlIk8Ms77TTY4l_QApnjxCBygq0BQGPKo3YS36I6vGo8V1-6kV4oxwSPS0Y1yOta3X3XD-XUfA-cwMKnhuWv_XxQpgmTATikuKyGobf94tz7siNoCxJCzVXTyT9cNhgYgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0g-R4lctkULFwFWG4ynHiBpD8D_g5mtdgG_DncZFNxR_j6wGNHtDfc6vLAB9qHmDNL8kNbmEzN0q_Tgj0E5h_sRyLWcdGvwHHAT7MR-C-TkD-aJ7X87nRGglkRutisQtYlxUd0fHdzRnAHO7ZSYrU9SaHY2NjdTVQxnEe3P1XjEsaVEihyosH116D0AlHUdOnyRIYpOBvlKLkeTdPts96NrZFYtARQkluTjfxX5RrVD4VBurVVz0SXLx-F5kxN8ZqWA1hqQ82mh3WQ0_8e2JyTUTh4xCDZgCX_khoYgzphmFEWUcD7AQchjmUv2XPDpD2Hn_TaeYiNvziahFnC86A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=IMsUy8DsYT1QPxa188V02J6sDw7-e2tNENYrgW9Ghn4Ecv446C8W1ir_TFIDYBbXzcrQon2Qfe6xKt-c1hctZiMEsDhK2KtDZPSkERYIdl2x_bqOj240Gtc22bYpFQCNYvLFGCxsiCILbZbX_F0f3Tq7bH82_zrVxuEcamvjCrsUBtkb9muXZra9BhotO0hCKslr1Wge1XO1mSAMfUI3OXk5jkAV3gc1toYlqOpWAYwu29qg_ExCy9YPWzDNJSJoRFTGnijB2tSkvYix_kY6l-UixB7ANspiSgTtnRVw7n0aIjBKvut3Lv7DmOrGnZEfWypHw9vi6j--ytQ-IXt1mwHY2sH6_ZAUHvlCuSeKfYkyULFE_P2MX13JS8Gnt0MbdlpwKLWtqN9E4nWmA05HfilWscq6Ev37JaVv_p1Y5ZBqJD9PB3Z3B6AWUCv7pKFCX3Wi2R8hsYPk6QMI7MBFCc3Vyi2Qk78BcrDZeeS6uihBnt_PgC8Ta-KaWFsz3SLbBTJSbrjCToFIkJF0pWIZOkIyPJNSWYqyLHazfRMCL0WE0R1JJHJDlR4rSM-h2TLa1_vFlV0_zb32LJ8kz2COweP4qM-kWZSFCP7fwuSDvHcx6Ylb5fWcSeC2CxWEVexCJeXg36Nl5jTVyqKwRn5HTKlGlZTE4KSmZpFhD_3g-9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=IMsUy8DsYT1QPxa188V02J6sDw7-e2tNENYrgW9Ghn4Ecv446C8W1ir_TFIDYBbXzcrQon2Qfe6xKt-c1hctZiMEsDhK2KtDZPSkERYIdl2x_bqOj240Gtc22bYpFQCNYvLFGCxsiCILbZbX_F0f3Tq7bH82_zrVxuEcamvjCrsUBtkb9muXZra9BhotO0hCKslr1Wge1XO1mSAMfUI3OXk5jkAV3gc1toYlqOpWAYwu29qg_ExCy9YPWzDNJSJoRFTGnijB2tSkvYix_kY6l-UixB7ANspiSgTtnRVw7n0aIjBKvut3Lv7DmOrGnZEfWypHw9vi6j--ytQ-IXt1mwHY2sH6_ZAUHvlCuSeKfYkyULFE_P2MX13JS8Gnt0MbdlpwKLWtqN9E4nWmA05HfilWscq6Ev37JaVv_p1Y5ZBqJD9PB3Z3B6AWUCv7pKFCX3Wi2R8hsYPk6QMI7MBFCc3Vyi2Qk78BcrDZeeS6uihBnt_PgC8Ta-KaWFsz3SLbBTJSbrjCToFIkJF0pWIZOkIyPJNSWYqyLHazfRMCL0WE0R1JJHJDlR4rSM-h2TLa1_vFlV0_zb32LJ8kz2COweP4qM-kWZSFCP7fwuSDvHcx6Ylb5fWcSeC2CxWEVexCJeXg36Nl5jTVyqKwRn5HTKlGlZTE4KSmZpFhD_3g-9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eswJczP3StcjEfNoUHvbuPk-XjPb-HcCoeZKCrQL5imJvManjnmQIStZ4NIMbeR4XT3WfLlsoAz0X18Zduk4odWpinNnbqmjEJFOD-TmlQ6e3IKl4TMdQtlvQXi7VjhnrdRauW0KpnVlX2aqOzoNVtnUhEHTslXIpXZrMdl_wgv1Fgd1qvqkZLIClOw-HoSF8HScQffv1vDvgdDSOzcXaY9Wt6ngo27ntlNZeTxuQQ7NQ2P2j26kce32oiYvjnBFmnvb5NEqNLibf4j1TcXYBF27l3HpqABQ7NOa5_YuHR4ChjdhgBSlBiBdGgr5YuxPRO3yFa2kzTpuGzAFjhzpDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N3xqyt6vExKvzWmIM0_lWu1mrTwNN5wORr-d3ck8PvVqIlA-Z2lxDY4ft966QMKBtFzX19dCKcshSe43Z9md9j6ALVdLKL4uRuGRg1QWPJR_3THEWVRlvpWU5ytK70PJqt03Zv_JDTP-50UzLZ49-_Twu4I4glg2FWAQ4s3aVaWY4ekI1YoE6Q0BMxihxQfrjFQDTEaNTJAeS9pyKs3LXJf9rS6TsMudQqu0cF5SVFDnPoPuHpf1DwNGxykMXGubnjDgH-296ENGQvIRU5foP7-Vfrtsyt9XmsVIFfIIWKFdxiYK-RCw-VE3paroW9bh_Dmb7cGnvqw8HjYwrHJNXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=ZsVvGz_s737zqSvrPsOk_t1PibEDUqZoxJ9jdan77dHS-o6dIOX39_GKO3ErfV4aar0vbXPBcpthS7h0xjHkPFn8_zwQLz97GuPHlFsxG2XwOpnE_oAAZrRTuA_pPvKGI6NkKlfTgi22FJIrvjQSapGxksYO22zrNwr7gVhRmN9yb8BUZibbzcJb_NP9Dw6659U95xCFidjHMM8s0m4GDAV9fdmgl4UI-LL39WbKdY2vT4UwwiVyqD2ryHYGQK6M4Xs9aAi9ktkKmSptweHov-EmuvdPSXLz915xyFdoDjjO2-ETRDkU61I-fpmufXrMY1p_0in3CQ_DR2Sm4RyQxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=ZsVvGz_s737zqSvrPsOk_t1PibEDUqZoxJ9jdan77dHS-o6dIOX39_GKO3ErfV4aar0vbXPBcpthS7h0xjHkPFn8_zwQLz97GuPHlFsxG2XwOpnE_oAAZrRTuA_pPvKGI6NkKlfTgi22FJIrvjQSapGxksYO22zrNwr7gVhRmN9yb8BUZibbzcJb_NP9Dw6659U95xCFidjHMM8s0m4GDAV9fdmgl4UI-LL39WbKdY2vT4UwwiVyqD2ryHYGQK6M4Xs9aAi9ktkKmSptweHov-EmuvdPSXLz915xyFdoDjjO2-ETRDkU61I-fpmufXrMY1p_0in3CQ_DR2Sm4RyQxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=bL0CXz9Y-A-uQPAKGJb-7IOTuAoN7QK-_3q7oVNwOMW4F3ZJkuLfKjGxmjL0Qa7EAjxTGmgBykRUF_hh-GYoM0TEYM0TEpE274s3-8nEVHL91AnZwxrFZo6FY0fFRv4k-uBp-w9BIrgEKfam5x60GajlMvITVCv22BDtkzR94f9MeP0C6JaaT-ATVagTaonDoDQ5r0xjEVAQIjANfYsRRNZQ-MZ5DGHYCWCMecH1jT41riBjEiyWR76OOPGJ1jt1n9E1LjwaFYiQSD49CKJrfX4qtvoB1JgQtoqRpCbP0nDVIiqe3B6Qzl-VGVcKJMpxV-287hVVHYh_2xTUOOiaoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=bL0CXz9Y-A-uQPAKGJb-7IOTuAoN7QK-_3q7oVNwOMW4F3ZJkuLfKjGxmjL0Qa7EAjxTGmgBykRUF_hh-GYoM0TEYM0TEpE274s3-8nEVHL91AnZwxrFZo6FY0fFRv4k-uBp-w9BIrgEKfam5x60GajlMvITVCv22BDtkzR94f9MeP0C6JaaT-ATVagTaonDoDQ5r0xjEVAQIjANfYsRRNZQ-MZ5DGHYCWCMecH1jT41riBjEiyWR76OOPGJ1jt1n9E1LjwaFYiQSD49CKJrfX4qtvoB1JgQtoqRpCbP0nDVIiqe3B6Qzl-VGVcKJMpxV-287hVVHYh_2xTUOOiaoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEjZgw3Yw2r5EDVtxsz5-M6PPpAziZB2R0JtV0o4DYMgbRor8sfJ5GdgbRKbD2AKwBP4L684OWbqokukvleWlu6DLkZ9HsTczFeO1saPvTnXD006XFMXNDWmSG8TSQs5EtilDj2L6qYXkJey_9ZAGNiNTkUFuUaERNpLCbpQq2itfWjYnQRbwl1OQyawrRqiq5cR2KTp-jsUKDIL2rx6hdZK7Dz5Ditpf7y-mWYLSUIcbAewoaSzSioJsEk6i7pfnVXuluP-YWCyLZlsQgRJm_UaMyX5MYEI1m1eKpN8AXiKuvIW9bvBd1GYjqIA6y6n3b_-hv16K4bzVu9unqeMmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYQtpqT-x25DgIbDWAb9TNXgqxGShg0FRn0rgwXNs7V6slr_hf0qJgV4b8LVn1cZ4SLfduwVZqhcywBNKN6BxrJbqRLiIfV-NnSs3AXxA4t_zBAhIW0cKOkEfTAKAxnHz4EHPZWURHEBL1AX4j-QFU8fgAELkTpcbVrpDi_dEwsGAwfQVVZgaM2Z5wdrEHAE2UnHsOn8FZv6QEtmoL2CYbqUyayYBKZ4whj5K9u0ER7gYNtA8rBgkcrIEYi1zmyrZzGQRNWmS3UQOb1TO9fybRByL8Pi2-6TETqb0cCY7IptoF3HSFUensxYWsfBma4KgFsthxS6HBJeYye27XlVgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=TpuqfeNuDNdDOjhVHdWpVfuciu5xNWRBJs8kfntq1yao46OdIyJVhlwCxBGy-IGtlX4pt6XkYHD8IxaAcJ6PPfcDxXY-_aN5QhmaGY1ZsvTRWg2wCv9znl-VivvtXHn--IpYxGVVEf84mwnqggAlFlJ9MAHPL4AXXSBDzhpCkc7Fmh8NUZdXYyudbzQFUaUISc35kBuA-iIVK8n9H5RsEa7HRjvn40flE55zVYGstzRJMhL_GQsN4zVosPJ0SrEh_7tchHtB_vBNUIBBkJR80VgmcTcoPcjBT7RZrUrVAc-PYCGjHwz2D0RLlDJRhFlV7XGdAtVwsjRSnlh7OmydXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=TpuqfeNuDNdDOjhVHdWpVfuciu5xNWRBJs8kfntq1yao46OdIyJVhlwCxBGy-IGtlX4pt6XkYHD8IxaAcJ6PPfcDxXY-_aN5QhmaGY1ZsvTRWg2wCv9znl-VivvtXHn--IpYxGVVEf84mwnqggAlFlJ9MAHPL4AXXSBDzhpCkc7Fmh8NUZdXYyudbzQFUaUISc35kBuA-iIVK8n9H5RsEa7HRjvn40flE55zVYGstzRJMhL_GQsN4zVosPJ0SrEh_7tchHtB_vBNUIBBkJR80VgmcTcoPcjBT7RZrUrVAc-PYCGjHwz2D0RLlDJRhFlV7XGdAtVwsjRSnlh7OmydXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=FLDeWjz4rRBJsbFUGlCb46Tthq6lmZCrRLAAQrly9p7lDhXKmGg7a6gyrJCYbUZzE3j29SHeq8BbThqqLyN8i3Ua5vn35359aR4oMVvX3GbgLxUN0VECTEB12_5dpWAk6oIlt5NL1qLXpdej_IzTjxKn5Ojn1dI9Y-aCJAhTjKq6KbtXcjBupWbokkAU8aqHMtyVJrXb_7HNOcNQJTSrjSNWtORZjgjCI25kFXC21OocAQQZ27qZJtccQuCsvgcqOzekV3NL5YLgsUw3toV_PHtTt2_s3wUTvtJgWE4D352oUQBIhJU1ij9PH-k9O9O8HWBcaEdsPkVRmXj-9IufSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=FLDeWjz4rRBJsbFUGlCb46Tthq6lmZCrRLAAQrly9p7lDhXKmGg7a6gyrJCYbUZzE3j29SHeq8BbThqqLyN8i3Ua5vn35359aR4oMVvX3GbgLxUN0VECTEB12_5dpWAk6oIlt5NL1qLXpdej_IzTjxKn5Ojn1dI9Y-aCJAhTjKq6KbtXcjBupWbokkAU8aqHMtyVJrXb_7HNOcNQJTSrjSNWtORZjgjCI25kFXC21OocAQQZ27qZJtccQuCsvgcqOzekV3NL5YLgsUw3toV_PHtTt2_s3wUTvtJgWE4D352oUQBIhJU1ij9PH-k9O9O8HWBcaEdsPkVRmXj-9IufSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_7C_0lsMKRBFiU-mxmI4PlIz26JXICiot2fti1RyAvDyGulUxwX1MUwF7rhC-O_flntgIvZYjgUniSCZWys64vNqTgTaeNFmxgDrRPXU31Wdue6JYDG8jLK3SJWwxHztRSxU2M2ECVKSZCPUn_oO08qPBwWDh3IiPvazg_hKFVwuWgpV_hdm_1S3TZI5RjnWdfPyrd2_18iTL0eiXoPeG0ZrjC3HffcnOPA6jNoB3SgZ8eS6lktlIpi88XapadoXj3IVWbyGujJiYOUeOSZPt13B9pwPZufQ9XOAtm6eVwr5hlstXAEIRxXNOXi8F9uEs-HR6fUaZ1Ltv7ZWV5jdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CP8VR189eLYTqfdRj-KoaPOd0CaV7t3ugUGiuMJGJgs9wHvOs7LgFiPiLkHYUrwQ6vWNDONXX9tWkE4-3CjoIGq_Cu4XnLvcuN-Hm80HZZCvf0qSHvnrLOavFaCwaVFUpD58sYDU50C05A3hGpeHiHLMPSxUwV_7IiCfoFjtq5NbSISzOqMm4O37IVNwpHA_zPV03Bs6K8Nj4n4oFau1N7g_8iM8WOgU9PFQ1RQxCkeoczOX_UJlZIXFSq3xgef0kSMAQoDAEQdXJGv9UMGfq5HX6PjgW06Evj4iUv4GfjppKHi_T8_gFkvWAtDoxytzKpWV3UW_dDT-vSppIlPkwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjbiioSsXOR2zP7zSrAYHI00mutdDzHB5kG549fNP5Mqhw-82Qox3bPuEe-BDoo9BahmusLrn_Hw8TAOxUJ8MF8AwOSuPQORGS-tBKFalxCvf8-OPkJuYjQ59AjflQfxUW-QCPUcA6l7IL7gANwUyIph9jI66xUlFU-PKpoiKqHimMGl6d3aKB_mnergm3_S4DWq6G---vSiT0mj1SBmj6ZDtdDEmK4c6Gk2YsCbm6mKtwYMJyJnhrO0XWQO0JWq_6NWQg2uX7sxzr5pIT9PtYnzMWNjsqmHXo7sHnr5we1UVkpylq0blsu_-vFRzOTtM47W2iL6WYI2w62-v-P7EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZnFZT-ArgfzuGGqq2Ho_tjcVwWxSCHtL6hcZBmaeya98GW27YhCzLLCx3ujgVz3TkR7AusDoSc9Oioe3WDL-PTkcDI3NO-4Hud0-Y49zDsra-h9AqlleMLzh2N-S1_jjyeLw94l_eGBCGtdrAnOBZAi-pqayIdWfqJ2HkE-2XCfi4Auj3t03F27jNXXmaDLLv1fHAZqDZ7mi2MLhFw3Hm2IoIyn_8LdaO2j-JgfN57fy5VHzUZC07Ted-Boejtt7pUqktg2OjUTSk8eCsTbegesL6AIMCALRF2FK5f6PCJQwmIP1kn-SZzXmN4-qdWI18o_3kzKDOlg2XmPMADV2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xq_S6bmGO8VId-LN637yu1ayR6v2JV0YdoLmXKOotK1chxyIRwlm-zLauPVpazUR0O0dp6k7I_Q3mJTDnqO3NEWTASBhvx7dHJmOFm-Z0fFkDDRaXco2TlUd193utmhF8X9zTWJueXo0R1xZgxs_eZjmxeZqFxsXoJyuvO3ZBNJhkFYoxt-NPJzXePCeB1pHNTvuI3Y1Lbeepu8do-9eouBVHoVfHIdlVeEFlkd5Cqz8yFwgdVjnwrSuSzLLRgsITLYY94D8pM6HxWUuTqtHMdFb4VI-XAsXLTopdzh3QivNHPqoi0CDp-8VPjSwnRD-DM6z09wJNI2pUbLR6sp2hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXKuShCPX1EjIqYHa1ZVX9kGz4M1aMSqc9pJLNarDhvQ2nb6qnyKgB5T-Kr7wTZKnwB8VtFYK3BThCSASMSig8f-2PvYQ13osUHG-LtBCVX7hXBm0MHCXufNjl-NMyrHPGr8-GHQ_7p7FICGLdrpp7S2hrNoAVg2gSsmEl2YCNqzRXQN7UGQdLWqpGs39PWchSDXer1Idtx-avdxZzLRxGh47jxSpSuGiR8CcbV5khGi5uWZOrbn3xzuoyWOlPwOExJiREgn0FzHznwGoF-CeWBrKGmOSRhBkzpHbZ7ifjQMlLpppGfcsm5l6Y12zK7GYv9kuCbeBk7etQb--Qcrnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pAMTi1ZWTROXdC6qeDnYW4iPs79QtxSpZrAjM6nXB6BVLPtGJB4oHUNIW22tiH_zt7ctzrWRC-zlJrAzMF0-RRz9VPNTwOKFXoRazP-RGOkaqzLzwrjK-7ph2A3nfzV0Kx6iJQq8gBG70oVVTCbNwrkkOhBPbNpFA--6Va1JoEA5gGQFI0MACiVYepsYANhUvO--aTuB3NCNK636ULv9K2NHwh3xT_E-Yr9bNjr9gb9v45u0QyXto1-URSJLuzZL1eCCUHeY_UmPXvHJUik5ewpK2zURdfZF8Eg5Qo-CKhpEfe1wkAaLQPEGHmFx0dFFZMmAnfUoXAfaucT6_RGu7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pz7Dc-LU0JQXGNNPNsWxqh3dGpfnKimQTTGcofBt9iO8xEWRT4Kfjx4qkYj7mZAaTKD30liHNODiMyRtIcZBNmh8aao4WFBahqZSGKVWXN1NsXtQX0felR1OmpPbuVi27eNsV8ULkTa2NwWoBZS9zsw-nMalUeM1WuF2lmwY0hySEzfLJFlGj_zcAs4BpeuHYkLyiY-E86UoPikaxgbzV3DtkCK9MHAQf_XrohOlkliYK_EAMvRqnXerCgDuFAo7AsrrfhYZpKrh3w_2XvzcN2RuI7ZsvWtlhn15KoCWbgganX0txxc2F-AlM55-lHnxCSuAW1lTwbbBqGOx7XL09w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMHCGr7vsIP0wmOFBCrX0QH9c71kofbL8uroGGAHCiHf5oij1qAdAMmboTV1Jh-eBcFleq4fzPrITcgucgg49ckuctNDRbs4sBw_urlRFsjl3Lqkvm6q1bxHe7Fl6bxkL9V8twgnLj-dnqRChpwk8kgXOx1Kb-Y-UHp_wLdrBfYP41vuABqkP7pPIZKgsbdQjMPJaQKk3ZDHuJ2W7EL9EAmpJTmIoPwj71PrpL2DojpWDwmxutg9-KIh7vHlTiUfTR89sl3Tye7daXIafFWz42838iHErUmsT9hTl75BecVpo7iwQuq27jldUX53ns0nzn-KRUZ2W2hzpKyxdiI5FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BlPKbIp0PONnLWfvmnlzOt3H-GeIdCstQM1PGYVx2Aybe0CMv9qmF6I87r7nYMTsQtvZKIxVm4rqGzsjzGgCA6aSCmzuB5U52UIdAmu8t7PSVVOMP9l8mqnW5K1NSE0zeFjRV-Yd5fjxEDjRQ4h8Ec9m2twlEMrNHN929ellho6aRzbb832PhUAD_tYd7dkddVgqz2Z6VWz5xjcebdzkG3qdtUu70R80MqDvDmoU4MsNTea_Hrx7HiNpyhHi38ItPFvPpN6toTANAcDfdNzt7FKacNyVPW8sVNKi5v94pAhINrtspf-Y3tH3JbZAX3UCKgtXa-vvTop8EHz69AKJkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=rD6dt8LXYtTW99V481KNPuWqXpJ-cU0DCa5hyt6RQi7m34OIftDQqehQ27C74xAITN4IkCOpoWoL2Y3rcRmK_pqKlgtUtVlgkNwZmMB-uCydjMJQU8-yHQ5opA4pWCk4iwwabVo9OYv1yNp2yO-K-Qq82jrfaxaTut3OYrGt_2P8rxGt2efQ19ITn_-LnR3zW1X0aNQdp1orz1R5fEQ5BpJwU_rJmge4sNRM2oHX0pJoCw9qPuXs93UzAyKWsj13QgsYEuGpduL358k94V-uAvD7-06sgQl0LagIIRuQrRNR8waBqp4Rt5evxO8GWDVmo18C3QaKUAV7ocHAJMI1Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=rD6dt8LXYtTW99V481KNPuWqXpJ-cU0DCa5hyt6RQi7m34OIftDQqehQ27C74xAITN4IkCOpoWoL2Y3rcRmK_pqKlgtUtVlgkNwZmMB-uCydjMJQU8-yHQ5opA4pWCk4iwwabVo9OYv1yNp2yO-K-Qq82jrfaxaTut3OYrGt_2P8rxGt2efQ19ITn_-LnR3zW1X0aNQdp1orz1R5fEQ5BpJwU_rJmge4sNRM2oHX0pJoCw9qPuXs93UzAyKWsj13QgsYEuGpduL358k94V-uAvD7-06sgQl0LagIIRuQrRNR8waBqp4Rt5evxO8GWDVmo18C3QaKUAV7ocHAJMI1Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=CzWiPrEfI0szVMbrcdKsdqscOc-ASmOUbdaZgVJ5J_GNjCQJVk8UeoGfVHI2Rteszir08gHdHCo5Tbr4W-aJsOC97tnepbwXlTNUoqrsVjSbdovcW-JAYQiEhtwp0FAmeS60g7HtuzD3-bwKGmeiTAyXxfOrS0ILMl6kctcP595IQWZJHS-YHRFRqDDDzVZIaFJPEeNLPTSbyK9vUmeUyeC2XSQqE_Nd9ftMXJsRGLsqSm4Aa6avznQ1Wu0YIZxJjUc5_gBIw_cPLO-QoAJgCCOyD3BBDU5Qo0-oe6sQjqLorAJFh6eji0ak5-wdA1KxqJaKGQB6z1H_ZRKZb2gq7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=CzWiPrEfI0szVMbrcdKsdqscOc-ASmOUbdaZgVJ5J_GNjCQJVk8UeoGfVHI2Rteszir08gHdHCo5Tbr4W-aJsOC97tnepbwXlTNUoqrsVjSbdovcW-JAYQiEhtwp0FAmeS60g7HtuzD3-bwKGmeiTAyXxfOrS0ILMl6kctcP595IQWZJHS-YHRFRqDDDzVZIaFJPEeNLPTSbyK9vUmeUyeC2XSQqE_Nd9ftMXJsRGLsqSm4Aa6avznQ1Wu0YIZxJjUc5_gBIw_cPLO-QoAJgCCOyD3BBDU5Qo0-oe6sQjqLorAJFh6eji0ak5-wdA1KxqJaKGQB6z1H_ZRKZb2gq7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=r74ywAR0AZrAWAhc-cAk0hxZ9DiUG0fCSKFJ29ZMr1MJ8p8OIRUV2J9jfjkKwRi1lFSlGCWHUmvntyfGZSLG_5pAUeZEjm-XmDsMILXHepdTmUXdfV6w3HgzLDEhFJvD0Ju_jy7mAyjxrE3vds_UTG3aMwHdHsHhLHLGCZqFxmuNLL6OjbbiaTSHJiOHUAGGNLHcdbSnlEcbY3cVQeHjxpvNpsSKAd4Lc6vCvNcjFlc1iarmM0WxzUbpM4UBbiQloQmRr5aQArhghiUB1Mzs3PBalxQDoKJrhELaI1Js66tXky-W641ITSvwle0BF16wwL1KwPmHrLi2mmO0cb7lVBSTZskce2o0h8Ll5aSe9c2PxkHcyt6Sv7xezHyZyjv18Fe-NBQabYu-LKwHh5JPTyFo6yZx3-_8ag_qkGBI8vA59lRzSflER9X4VG6ul-XiJ1lUprWnloZzWunRWukGP28GNJsx09rJcj58BDeplg-Fhh_-1y9afGepB_OWI3b4gaIsMq0SijH2VOUJhMZV7oTjH3KcYkq6fVDaAoLPwJwK_P9zlzYDcjI3xNZkWGrjgk7_YAkKWYCX8kVH1-bY5h32GFtaZCOETSSweP9jmgmbO8Nt3l79bEGJ0uFDJ3b-pf9EDUrxEpoec4AK_dIZYgMGrsHPb1A5ZMVmHpmoDIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=r74ywAR0AZrAWAhc-cAk0hxZ9DiUG0fCSKFJ29ZMr1MJ8p8OIRUV2J9jfjkKwRi1lFSlGCWHUmvntyfGZSLG_5pAUeZEjm-XmDsMILXHepdTmUXdfV6w3HgzLDEhFJvD0Ju_jy7mAyjxrE3vds_UTG3aMwHdHsHhLHLGCZqFxmuNLL6OjbbiaTSHJiOHUAGGNLHcdbSnlEcbY3cVQeHjxpvNpsSKAd4Lc6vCvNcjFlc1iarmM0WxzUbpM4UBbiQloQmRr5aQArhghiUB1Mzs3PBalxQDoKJrhELaI1Js66tXky-W641ITSvwle0BF16wwL1KwPmHrLi2mmO0cb7lVBSTZskce2o0h8Ll5aSe9c2PxkHcyt6Sv7xezHyZyjv18Fe-NBQabYu-LKwHh5JPTyFo6yZx3-_8ag_qkGBI8vA59lRzSflER9X4VG6ul-XiJ1lUprWnloZzWunRWukGP28GNJsx09rJcj58BDeplg-Fhh_-1y9afGepB_OWI3b4gaIsMq0SijH2VOUJhMZV7oTjH3KcYkq6fVDaAoLPwJwK_P9zlzYDcjI3xNZkWGrjgk7_YAkKWYCX8kVH1-bY5h32GFtaZCOETSSweP9jmgmbO8Nt3l79bEGJ0uFDJ3b-pf9EDUrxEpoec4AK_dIZYgMGrsHPb1A5ZMVmHpmoDIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qf8AOqFchgdXZoZAb6AWswAzPoBHgkrisk78lokXSKbsZ-VnxK9fZbJzWZVg4oAPppEQSuZnxpkK0_MVeHNTM5SqjtyZWbR-7206hiHCAGT_H4E8WeIKYwcngmgJvp6b9bnBJ2u-R0W5KFcB93TX1J8l-9JZ5I7KQm1z5zuq2tefGSqq9EartBwF1jvRUeIW_QpCXyLGbeRUnci6vOeNV3TvyeSq_PYEHBmOp_WGKorinteO2Xfp8tEM7YBsruttKmamZ7mpMNXV1v_QmxmsSL_W6hkJyCOKBXdIEyXW7SikmJ2GGAPsedN84zAH7m9uI6Ru4Knelyvk3xQYbSLmcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=Y1JWXo7fJcQFqpCeVpNAihIJ_Ll-Lpz98wGle_Ib9KE0xbKQaZW3HtYo9v4ETKXdZv3I-WiwVPRokEwcvXPxzHFOmuXYCqees-aGRaGk1YPhCFB8djErI5dQFauIAQ9ed9OPnqswEzPkSFoXVkVn3vdNfnNCBR9cfH1IKamTLcw_tOCNOXrG5sUF53GjQDuimGqKPnKZJgp7I_XDz4Ku3GlkGPb1lWaEP_u6y0ZheCLFQhcWFVVI0kpAwhaLss3UMfjvmJNDB693u1WfS7EB0rqAEVPMbBUIY46DnGcTc8Ak-Uq8GVQffunHDmecGW491v1o_bbt_F0vaE4T-ZFzRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=Y1JWXo7fJcQFqpCeVpNAihIJ_Ll-Lpz98wGle_Ib9KE0xbKQaZW3HtYo9v4ETKXdZv3I-WiwVPRokEwcvXPxzHFOmuXYCqees-aGRaGk1YPhCFB8djErI5dQFauIAQ9ed9OPnqswEzPkSFoXVkVn3vdNfnNCBR9cfH1IKamTLcw_tOCNOXrG5sUF53GjQDuimGqKPnKZJgp7I_XDz4Ku3GlkGPb1lWaEP_u6y0ZheCLFQhcWFVVI0kpAwhaLss3UMfjvmJNDB693u1WfS7EB0rqAEVPMbBUIY46DnGcTc8Ak-Uq8GVQffunHDmecGW491v1o_bbt_F0vaE4T-ZFzRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXtuvllmCI5w4mJf3J_ngj9tlIBX8GJrBR_pGIVG2X4HRawY_W3FYXb4gTthk2q-O6KdeEOSxLoOtA6Pi7Yk4IkQ6LW0zCzceKNIlLqqRfxc3Ch3DCFsMmi25Fk600nQdqhn2s9HSmS5c69wfs559XuACZkwB40nEJYSI9yuGI8QWMQNeTm4ygqLu5YDLhPxBe5IQW5NvEViMOJZ1sWZK2unM22ztjF4bJK1sa-gk5xj9zHYZRyEzxDSEJ1TY4UpACdYDHvxoN-nM5-ri0m7akliUfo6ek8h-DfUIJBGENVYcmxa_uGE9TQhPBNt3YxHx1PtHILpUnRIspODAlKwKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfjQfAt0OK1eeQM5_8qK3tN7gfujBEd5gIWU5Y_6cxgHOpv3w4L7oN1-dml2lQYuEEyRndqhj0_vFj-o4J_MtOsU1Z4Qq2RDhmASY1jNu9msM5fXrX3-vo0U3obfUOXmEeo1opJaFHO4ChLQP7JaYUwYIVsvDpVctayeT3b-s-sCzHvwzNAnKqs9ket8VaFosij-_idwQmfHPh-Gwz-oxqOKj7teIlmbq2gmNfAD9L3J8aroV9d1l4iAmx17bBMvOrD3X_rsC54RaCCn-wDyKi7PPGisJjD8FB3D99r5Wc0jnlKdJ6grJ4JdAVUitto3pVGDx_XnGYsCivRlKKfBlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RPL3iUbdjSBW_qISXoTXHTptS8Mdg4LgmkJnBq98E3ERsNGXvHHDYemhu4w1bb72tIJEnJxT2ZVY0CQegBOWjI_-MLGIzQv5EsPkpJz-WwPDUOGpvv81MpNroyhHpaX3ABul2gEztW537_Kb7uKY_YlzyTR9Cum98rH-Dvw7g9S9Y-nWg7ldTo_46bDzt0N6Lf2pRhEOqsqDTUsCbRjJ3kI3_A5MsYr7o1W5jCeDNHxuTKXNBEFvXtdxhbZbfz4EdyqvwCovrmPVVzy6PKY20T29sAgO5-W-NsYewf1FYBIOaUAQccdhgp_Ua_eYQdnsHO_T09uEA0E7uyMy_xHq8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B8ezfdgmbBwiosykebA24hXObszJZK9Ad38X7eTiWIhZ-DeHtK-V5yDC37tq5rwE7NfNqIwkL1aHX47dd3EeJ4UVM1n95PPmaxjHLYuMhjQly3v8_ax5ojjUx7Z5N6k1z8lp1hY3IMluZS9gQaydiukfgKJ4TYrVxhJNuU_l-oFCiLrKLi3NB6kihNYI8fwRIPZ6Bs-BTbN_lekije46Xf7nH0KZVPUyXB8N4QcOa8d1IXmLTe0u8hSEoHW2YGnN0M1osPeakTw_g01mVTixquNeb56RBRHVbakwM9IS2jH5lC4ALyp4p4NYu5obA17RYtkqC0_VH398HQiri6wE8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2CNWiY41andxtsCBz9klB5Hd898eyLc_0rCkD0_m08S3NBbra_Ow0IKFQo3ZsxjSvQWrZRypoF6sgd3d1FVApw_RKtXv_3UDS2e20nH02VfJOx43HMt4zjgh8djyM0Lm8pEnWr695NMRWKKA2PydG95hBVCyqxhGGP_igFLWQgKS_VSNMm5Yu56F5vAywyT41w9sLsFvxQmhGADbeSzs07dXZxnEklG77aAce3jwhdfMVELE_7VGd11DWOv6T9vEL5ynpO00tQUJ7ki1rgtltmgsKT4f9aSfG2gWR1hwTyFaBJHIb1PbV_ICTBZHRyzm1VyvFPOhGxs78zM0B5w4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDDXogpezbtJXIhzMMTTyeNSUGAMCqSnhLEw7BQjFQZrI9fcoWTTg63vIHFPAUNu1DaeIIClHJ7uEjpSOzx2slqUbh3LIhH9LdpA7HDGGHgn9qsGZ3YN3JZe8VE7gqKCG6BYD-zCY2UkMN_mXTpQP5iC1NsvlCMoPJaRjYu2VVMj5me2bfX6Eh5XdXuDILGaRoIPM4VpRb7R_8VJgYCxoYQQbEmpw3gimAfXC3_ZGpyVkKW0NF7Ci3PddHmrapufPpDDi1oAuvhuY9jPAw08QztEygrpWCna1wdViJ6ZzAWWISBVPsfKVHucV4Agm0KOI1WQXEU7bFkNg4gi57Ik8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EG1THmyk_8oAQuwKkaTJYd83W__mWLr9IqBPONOssqOgrUCN9G8tJvHUlM_8Q9TRs-EpgXlZN5g51qmWy8GK_43ZfgU74W6abMSAf67zTp0PyNitI68aWLsBtABHWP76lusoCi8liZ1VWFNLPbkG4npZrkdpaemW1SpfeWtMJBLRcakKh4EQs-kFsbujt_5_REjj65uNPpckxO9CEMVaFxbF3LGgCsk2obZMR6nxVY9-m79nsKh3PfW3U074i6Ub9U-9SahKo5Lb03r5uBX1CvtCWQx5NIqTJeOyB3tFloBz4GRTba1fqRp0OHFS1RiKRrDWXTdHnouP1a4c3aaMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ces8o03RRzq6Y6zc4hyaNthHu0iBR8hw31nhKM5VxpCIB5oTCd71tWHKwt7rl_kGwZ_DHKkbDj43xBtCmjE6BdIAU-VkxXno89tnhc2FQ7KmJwDtdXJPhITOspROVj4LyBJe8jWBVRKm2WGhAil1pi-c4SGmHLtlb4am6opVxpT2ai747IMwlptcygjbSYUTZzpzQV4jlGDMj_m23BkhewZq6wN7yhAn4wjY6Rt-rXVUENKy_amDMdwJj5CA1-tpeAYlOUYpkH_YTYk65FLicu103S5WbH-8jro_Awv4em4qjdbKgjNW07Ai00hZamd_MQ4tKnNzoelnDReRXISffg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LTtQ0FgD53gLxJxxf9DMetz9dfazi0beLDq6fyD_F1LMQLUc4JStDefD7PmiINhC3eTh_oI25OTdIQz44nk3o9WLaIAykahbGl9-Z9Jy_kZBgFCX9t_NZPzl_XYDjREMXKCKOmTpnIPN17B-cmKuiMJ_Z3EwC3rNf_K-b52mh0R1COvr1-txDO30h0a8YBx9D6g-UPhqWE3UaUA5BbR5kWch2tVs7SkR-nYI17vqbwAaBs1KnveiPwIqNDCYEoOk3LBKvq2aEzePcBXpzUmJCAn6cTLZAo2lSKutmd-ehVeBzViigYcTCdE5O108C2GCR577G79p1aiWE_Y2Myz3qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZSnQMktyURfR3efgVnse5IwhYaDx4hndSb7lSbaKk8tyQf0uo_izqnKH_clAOlLTq_lHK9ZvLQb0ztyE94qKH-P5ITinxG9QSiAW0psSZaXKdSxjQSLUnuQSFA9a3_QKAet_UMOjS2LQ7fVUPYTCThX9gumsWVWiSGrU2g9CkdKeopfnayJHO6LikWDcwx4YWym-IVzgLZe8UZpKGF1ZgertMz6V4w_dx0vpADBwVBkHgcQLE7MrVrD2mC367wVfzfrBlLbHDdEbQo_gvE9Ff7nORuDpC41csRqPaD5pRIgqrOQNgWhIXr4S158PqRsNHzYS62dFzWrxphMxZPQ8qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPLNYIezC4jt2mLVvP1MCIDNXw29_eGMJ5kLJ7alOs4Aij6DDwpgZN38zSK4T1ICB1LNeyfPcgHGe5mHBjCadMV9XFtONWJbtNCV4vo2ekajzE7ytqYo9vQT3pN269QksNPbgHaC_KE-AFVx1QQVEB2EHWajaGCx-69YdQNZYJyoHCeGLHl9LC2EthNiJpqq7qnjKtW48Q2iZfNHCT9jE86kwVZQZtU1IpcSMvQBYYInujjMud9NY3KLIDDn3W-XvL1DGPovW6K2rdol9TU-j0vzuh6YK_dXvfFeFXxqmsrHecnZsVfiejhlKtK6K277Z96nbF_msJuV2dFqh45YFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCwurTrx0M0SY0uf8P7Y4XsGj4aZPpFqc6dHM5tIOtVm9sejZgt_ro1wq2-F8gjnEHSuj11vEWkhlUoZAcS3vU57DOUuWLZ_-_HxbnL9ka4aW5YUYh7gNTajUerZaDWTqGNUR567gJE6b5fHHahn4R5yJE24TB5Q9qXjhYtey0D2lqxZ4sS8A2qtuSln-2OY8ls6ZybF63-ABATkHcL4bDCVnfY40Agg0snkk3xHxYt8bgIfj1C2yXhvOd_nCHm2O6K2GnXhGmCO35aIM6onxpuFeCR_Kf2faY32AQu0PDjUGUm8aDzI4XVlzxKN2EU-Ig4e9bNXVS9bvw8nGFjusw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JibuTMoG42VrJOjyhjkMsQ1JzWjwCKSOF9N0m3v16XwOuosn6Xve9cJtGnXOG9hr5Gt3CDeHZ57flCu3hawrGxND98SUYZMdPGPZKjLT4RlZyiR_8WKitNukeSFLzx023J-dG2oHDiOAupIJrU8uyuS8_8K3sNaqEES7KZCGtODTUn21SAXlC9opvF9f9Llk1WsFxapvw8ZMcIqlQIathO2uU2H-MJ8k2EKSYqRvHCJKwlHYmpbyHHsbmDJnhT0ChIsfRreRf6wJkzD2LdNg3EO_ElpbmGd0uq-Xn4HcQXBq6rznHSmXoSOWfCaFv48bpslqUQedlX1GzkurK4Enrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HkJ_3-2Z5vACrQ0N_jBBPXZ7qOWCKqR-VlCzHF5k-bK1k-fn5LMKov77rhwLZQF__kqPgB37YYHfZpGtTAysyteTWRNcvxSJD0n4UohTgp0jgkN4w30mvMWgP0622lhIEP2eeD_191LkT7mpUASoqiongAEmfQAXPbcV_XbeLMWw0NWAVV6_VzZUaj0KvbeniW2ZIux07bk2m2Nm7E8uIZhWwNyCWlH3Igkb_xPS4nJwF0C9SBFCKXlurpDEEqtuYz0agyUj62Bc0NfTo07UylJ9Gpb7sa5__a2ELMcqhl75tk_0bmPQTfZkeBiX9bJu9h_RWzJS3V_1AYLwicT2Pg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nGobMKVykXqJGhxIScIp94rq9JALYx5qEK35PACR4hAIDrlLNnTjpjRRXj3UNzRyw61HAags281eTSzxScalz3PqGERG30f7UxHTdsflicykXwEvIXj03a6U5WpQ-yphhFmPwtfXTbWGN4mcbXG6ijrSILAJkPtQnVGUZgFrx0N-1t7AXSyMbqM9mUvBlql4g8w0qLTYSRHjzWxjNnrdrqY9uhc71cJbq8GEzzKFLy6a-8_nhckpFB6u6lfH5X5cE_LbcO7RCsVzHgSDeD7dmadflKtYBbgvEAP93gcDFd-sa3FpSQLngEoSg8K73SRytVmr7IUnGj2CmiuF9RTmhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QdSLw6LEZ2BY-KlcJ322FP_xXgbvLw0V_yRigaFGkNwntsVBdyD4FK6bA1HlbVO0ITNfx4e7ac6_EtW0t7teboG5TkK3MzoQ8N72qQ7izG70LgmvvL4b4Zy_FU6jWJ7LJujVI2TJI3ujdFY4vtC_d4CTm40rrHSRFZQbR1Af85yaSdQ8pXM6iaxfw6DYOQSflAHo-J5O6E91QatfmW9Qjm5BSpnwMVhe2GdPIr6IL42JMiY5H-x7qMZWLko3itpSKNT6tdX2WUVwjpts6pBaduAMQRbzkcUSWpQh76KyhPAjIGlHrYnDzWbIN8ijDspUlJxGaFPnxoNMaAMaqi8tMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7hsFRTMwyTiWJWpCHeHm1z1a8Q-WrIx_6IADm8zSow5d5_9VDD4JgbuZh-gQLrzJJlHo3uBcJ7rgXYntxOz6ImTZMK2NMSsj-983rb1iQQGYyS7VsOiGlXX7s8_IJQEHTpuSEwU3IA2oNolnsRzEdgzGqBA9JLs4rrRi7HOGyjYB8CXzeBIGtHe_xHk_xC81chLh3GOYFH-fRAKyTnHrkqQ5xe7VOb6PzyPhxxRBkE-Uz6pAloKmQ77e8xWZX8b9fgXoJ6aLUuHoMhFytxhj5z5tnSWZoVkhkZ10c7Abc9oqd-cuQa10GShy4VhNeMXDQ6k-9vQhC0ZSugMb8ozAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=Uqc06CxZMJ37nqtFJMhBCflGqtoYtT_JK46uqKh9bgiuAmuQFVa1ezu0LVpwdtP5JO1LYjOMxvTkHmyPpNQt8_mZUffjt-KkykCc-XrbYsG2YuaqLTEY-TLHOp6Z03aZ7_5doZibbWmVgnYTlOnvhm1fQ1NTM7W4rk4-IpI3ykJnTVLtVnOaNWhgI-1rIa1VBW-fT9SW8rjmnARhW64xoqfgkekJyGrD1lFuYdQR7czlGeOhUpQ9uua4qj71HqLW6jbNQ8pfbIikSWeKEPSx01_ZItN-RUjCbGDOnYNjLTP43iAqJG4LYWu4IZQzRfIT-hZYdYDP3LicIv-fcKc3qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=Uqc06CxZMJ37nqtFJMhBCflGqtoYtT_JK46uqKh9bgiuAmuQFVa1ezu0LVpwdtP5JO1LYjOMxvTkHmyPpNQt8_mZUffjt-KkykCc-XrbYsG2YuaqLTEY-TLHOp6Z03aZ7_5doZibbWmVgnYTlOnvhm1fQ1NTM7W4rk4-IpI3ykJnTVLtVnOaNWhgI-1rIa1VBW-fT9SW8rjmnARhW64xoqfgkekJyGrD1lFuYdQR7czlGeOhUpQ9uua4qj71HqLW6jbNQ8pfbIikSWeKEPSx01_ZItN-RUjCbGDOnYNjLTP43iAqJG4LYWu4IZQzRfIT-hZYdYDP3LicIv-fcKc3qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvqL-w0rHdA7sC9AoiGdUtVgYeVWpmFcs9S6BHZ8uhwXguO8-7rHA5n62AfDiXMT4MDgO7OyhxSoBL40-m7V4SoWbPeuYdzr_EuFF4ZwVhwRAHyQJ3_EPoGt2XHJ2CU69qWPt820KTtoaV9qv-W4SkgVfyg9ecwsJksKUy6cuZea4W_JDZ8iiuSqu4nKwf6RQHs7UO3N_Trem-TrtUnvUukd7O3FcFos7E8c0ZyQMlxOh-lrH6PoXI1kpfOZON7PniQmnhMMUH3R9EcYPdQw7or38RwY1HTij3bZZ1xVjXgSZteY8RseNa6HCktQwedXweCeMF9UzbbyZYTkBgBf3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icvpISZpFlcXmpnt4KrNkuFSC5g60-1NztUfkYicGUS_fEcynH8n3E4L8UrYGteboqNclGhtho53XTNcOrkQLYn_7vfKQgEEDGqj37vXvLZY33eAxUE6ubkDzGP2c7r_81pTvWQ9lpzlbjKS61vFM8p7xnLQzHoEfz4L2eCvViWrwHxL5nxKAzDrusEiefMv_5W2mZokUGN3Ox1WOOK98-aOgj0qp5x156LoolfC3qT3tzGS1qAeYDop9TG6l43E7dkJwwyIMs4hF4uWjfQrL7TkWCW_GE61TyjyF93NMkiaZYReFZlSrdTQ4Hy4nY7vyBjWrwl6EmLC6lNS-1x2tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SByM7XJfxgS_5-KzqaShjewyyAzrDbo_efhXrd-ADl0Z6MeQsu-OVa8Dgh0GZNa7Vox_g98tNn19gLmWLX_XCiu4Os9y5UMcfOVN2ev2rqBJRGob7owNKlaDwEFt04tORs4FBqkFNOffXC7P3MfjVR6v2m5_vQfIIhZ58nhQDPR_C3hcCgY2hrcK6jVw-67znjjxOEkbOFhRUbZNx4mCE4aC5hkRXgdqNHwUeVroN1QF1_5efhR9rtSGqlDDsLRAI--0R61KXTF3QHh4q3WwV28FbmblWdUlO9K7E4JJUTRK8vlnGxMVZMWkrtDs5ArkIVn2jngDtPDfS_qNjaE6Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #3</div>
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

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=OtCg9tzxU-GRe5m78yEhbCOOF65IOkNL0wrhLi0Q0pmZ7RzxYrEbkx89BCQBsBSIq1TfSNwbZ75PNdA7h0sRWfcRsDfm4RfQpxP7fFCPJQRSkFzlQy0EmEiKNFtfMB2hNvQh2jXN_sss2q2feONfGHH22Qje0tRcCWB4GRB7Aqwo21OYlgmiY7buVuxFiIEkEo1OV4EUEo4XD0kb34aYbIvNTENxgGK9BkMveLwV4MxcxXwxb3v-4VQfe7E1h2d6OBcZR72cEdpaalMOUyOkkf61X-t9mdVvvG3h_BgLWVIC_E3d_IxRan1XdxvSrso9CFZxc-0h2-rOmZC3KlgOwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=OtCg9tzxU-GRe5m78yEhbCOOF65IOkNL0wrhLi0Q0pmZ7RzxYrEbkx89BCQBsBSIq1TfSNwbZ75PNdA7h0sRWfcRsDfm4RfQpxP7fFCPJQRSkFzlQy0EmEiKNFtfMB2hNvQh2jXN_sss2q2feONfGHH22Qje0tRcCWB4GRB7Aqwo21OYlgmiY7buVuxFiIEkEo1OV4EUEo4XD0kb34aYbIvNTENxgGK9BkMveLwV4MxcxXwxb3v-4VQfe7E1h2d6OBcZR72cEdpaalMOUyOkkf61X-t9mdVvvG3h_BgLWVIC_E3d_IxRan1XdxvSrso9CFZxc-0h2-rOmZC3KlgOwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrequu0Rk8vdX6ePn6--YZPV_73xaN-foJNaWhjgkOa-X3U47-B_Kacr0mGKG8DfGVdny6qaidS7rJvoSYztY4RHDaA0ElEGtPnUaxGZflxRsp536-3PQCmekvF3wJS6hhLgxp0QDVdzdnK-mXdYy8oUMvPVQz30u7fAqvX3W97O-XtgWlYgwI_4w2Bu8vK6y7XF1LoUY7ZajK0YysuAp0pyJDC2dFeMLsOcJqYUowxCDbbIZCXaAieLleqyX3UruEUZMmAITEgTiVkelT_ej3pYgGTEMRLDIZOhmHcuugps0D1MxIIGWZpa83sIMk6Qc6O0YIrBTK0VV6Vus5fx7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
