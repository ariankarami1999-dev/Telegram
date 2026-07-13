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
<img src="https://cdn5.telesco.pe/file/BIyWJRse90IGVeilFk4VGoazZQRUVio0U94t8byJJb6UYCTWWnzNMYo7flh7T2bz_gAAvVWWqH3sxLt65pjATZfNSWObkOjmhstV8sCCj5oZTY0Vf4CpPCo99kRyW3xrXXPS6PuazTZlaEcE_xhk40_ogXOvMVEbM-EnUSYsP9b6f1uIimkQvgHTzyB-Wcex_ZNHgojao7hSQquyGNzEint8KnOJaFCnLJy0HOy78C7HTA0soLqqC5mzOEOnVYcRTLLXH-ztEn_ro66fPURw2Facupr-PjEuEdsDezars8FNHcGRzjlBe6abcyJzh11mM5DWZKxyur86C8DOEDsnwg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 585K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 15:05:09</div>
<hr>

<div class="tg-post" id="msg-99928">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb6395bcd6.mp4?token=QZm3rr77Q6BAav0mvgDaEoyhe3RgFdSAjt7SljVAHuHRw_jD32GY6JdfLAdN4kmSpIfM2Kcu8RK5xqMWz7TCABa1X2DFDAQE3zHm75evUN4jC1BL9pc3qT_MMLHrzPl4iXTAW5VSFauvmvfaG1sLypu8FOLVEu71PiunPpgtMKRiGgrdx5TOTOmVxirgWE79DDo-XmiOn789uO8xu6zX-cFDF5PaoJPE0fK9MrFcDKSvSqPSOwyLxvP-RBCtLo2jh4sIM8ehkZvozxKGv0WCvUa7ijY1V8PK6cGdfFCRCvba0ZeEhsWNxWq4nf3iF76WGEIzxGxEIm9DnTv5rezFVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb6395bcd6.mp4?token=QZm3rr77Q6BAav0mvgDaEoyhe3RgFdSAjt7SljVAHuHRw_jD32GY6JdfLAdN4kmSpIfM2Kcu8RK5xqMWz7TCABa1X2DFDAQE3zHm75evUN4jC1BL9pc3qT_MMLHrzPl4iXTAW5VSFauvmvfaG1sLypu8FOLVEu71PiunPpgtMKRiGgrdx5TOTOmVxirgWE79DDo-XmiOn789uO8xu6zX-cFDF5PaoJPE0fK9MrFcDKSvSqPSOwyLxvP-RBCtLo2jh4sIM8ehkZvozxKGv0WCvUa7ijY1V8PK6cGdfFCRCvba0ZeEhsWNxWq4nf3iF76WGEIzxGxEIm9DnTv5rezFVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
انتقاد بامزه فیروز کریمی از مهدی طارمی: «میگفتید دونده می‌آوردیم جای شما!»
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 928 · <a href="https://t.me/Futball180TV/99928" target="_blank">📅 15:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99927">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cee2da53d.mp4?token=j6ZWCSqXe3sXM_HPN08xqMa-GQUjHFzkbBv1I_RuyK8PFVg5vGQ2VnAm3GwFJbxvzWYt3lQbxjf0qbRCTAu2bnoZyDoDfM05n6yi8iRkJEXoTfOOnK1uhmdtBU79vLtwJMxe7R7vGEge-LBp89pGIwf-GgGRxh1tsbGUu0sk7Fo0AQl9HdiBwO8svnNYsQ60qJC3mQ_pg9Xy7js3hdqdWYJQ_J_eOToapji9NRVhcFF2DdYMK7tsrXK8EfJWlxXrHEp3Fs7zG2H428VNl2M8-7lZh4SPnQfOgw8i_LVnMCMARxnxqe99N2UCTHR4GqaNMsxm08Lw3-hzoCinFVlIlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cee2da53d.mp4?token=j6ZWCSqXe3sXM_HPN08xqMa-GQUjHFzkbBv1I_RuyK8PFVg5vGQ2VnAm3GwFJbxvzWYt3lQbxjf0qbRCTAu2bnoZyDoDfM05n6yi8iRkJEXoTfOOnK1uhmdtBU79vLtwJMxe7R7vGEge-LBp89pGIwf-GgGRxh1tsbGUu0sk7Fo0AQl9HdiBwO8svnNYsQ60qJC3mQ_pg9Xy7js3hdqdWYJQ_J_eOToapji9NRVhcFF2DdYMK7tsrXK8EfJWlxXrHEp3Fs7zG2H428VNl2M8-7lZh4SPnQfOgw8i_LVnMCMARxnxqe99N2UCTHR4GqaNMsxm08Lw3-hzoCinFVlIlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😞
😁
عذرخواهی علیرضا بیرانوند از همسرش اکرم بخاطر تشابه اسمی که با اکرم‌عفیف داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/Futball180TV/99927" target="_blank">📅 14:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99926">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3c7adc098.mp4?token=lnM058BSfCjjQzilTvQnjGS0yTE6q3ZTs0vOvtZro7tu_e0M_rE-vsbEujBMlI-M0ABQaRKA8PzaMIe3vbiv18gJYzjCrEiVHyq7uB3GRyfCUF91dKIlIEmNeLFNcrEhlxqwG5n3yoTXWidHH9cTqt5dUDq3VVXf9VeFP-T7daAh0ILISZIY-4KmuU2xgLQiBJYWIPCPUUeOflsmouT50YS1nT7bNPDdW0y5pUjnATpEWyiOWLmZBQDrPa59ByrI2nLIFpQ_Rk84qaY351g0pPSe5Aj3OICnFXrFqdw2FJH6l5uhYOEFGWgQKpq2GoeIaXLdiO9YYcySjzf-R9WhcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3c7adc098.mp4?token=lnM058BSfCjjQzilTvQnjGS0yTE6q3ZTs0vOvtZro7tu_e0M_rE-vsbEujBMlI-M0ABQaRKA8PzaMIe3vbiv18gJYzjCrEiVHyq7uB3GRyfCUF91dKIlIEmNeLFNcrEhlxqwG5n3yoTXWidHH9cTqt5dUDq3VVXf9VeFP-T7daAh0ILISZIY-4KmuU2xgLQiBJYWIPCPUUeOflsmouT50YS1nT7bNPDdW0y5pUjnATpEWyiOWLmZBQDrPa59ByrI2nLIFpQ_Rk84qaY351g0pPSe5Aj3OICnFXrFqdw2FJH6l5uhYOEFGWgQKpq2GoeIaXLdiO9YYcySjzf-R9WhcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چهل سال بعد از دو گلِ تاریخی دیگو آرماندو مارادونا، این بار مسی مقابل انگلیس قرار خواهد گرفت.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/99926" target="_blank">📅 14:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99925">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1294ecf8b.mp4?token=ZISrpEaK0SMs498Sg4SKqxNrRgm1dPRIf013LXy7GAm05lUNQnAcI6H9s0iPvola4Vu8kevL25_T0b5VVmiKfWtyEhEjkmytk63HNbMUS2s6EDnHrtg_QsIBhZ9NlkbAbl_LU9dG8DVKlDfuXp3DCoiz_AnVSe2vOih4DE08g89SSKMW325KUR76BzESLZI85XvAP-Dg_bwWoSooow_oUCN9aT6x5befuwb4Hroa4lEHzxJkD9GocqMOi8UO2l8a8NTeqTO2b0fX0Hm1SDz7RVSKbqU_MjQr9A3R7UmOrjaXlhlsfb6yx30NJmuVRdTLeuJ81-l8RNsKRg1P-3wuyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1294ecf8b.mp4?token=ZISrpEaK0SMs498Sg4SKqxNrRgm1dPRIf013LXy7GAm05lUNQnAcI6H9s0iPvola4Vu8kevL25_T0b5VVmiKfWtyEhEjkmytk63HNbMUS2s6EDnHrtg_QsIBhZ9NlkbAbl_LU9dG8DVKlDfuXp3DCoiz_AnVSe2vOih4DE08g89SSKMW325KUR76BzESLZI85XvAP-Dg_bwWoSooow_oUCN9aT6x5befuwb4Hroa4lEHzxJkD9GocqMOi8UO2l8a8NTeqTO2b0fX0Hm1SDz7RVSKbqU_MjQr9A3R7UmOrjaXlhlsfb6yx30NJmuVRdTLeuJ81-l8RNsKRg1P-3wuyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
🔵
علیرضا بیرانوند:
مهدی رحمتی بهم گفت مدیران استقلال نمیخوان‌باهات قرارداد ببندن پاشو برو پرسپولیس من قراردادم رو باتیم استقلال تمدیدمیکنم‌. من‌ رفته بودم که دیگه قرارداد ببندم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/99925" target="_blank">📅 14:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99923">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpFLp8xjrv-wiG8Oov_xDKoZNabLotV_Btpb8kKFThri54wibq2lkJ1xFDg_pF-vwyo3I5ynKTLu1DIH9_LeMtzBKfj20m3W6x0Ru7bnlkiJveEpolmlZf58gFzwfyuhRcVCamSprVrw1w5aa0oajARmw9GhyYEOngVImKlXa4xZECYdVwoqRA8DW8CeO9M1ccePw_GamSNkDIwHYgRQla5Zdzxxf411jPKsdI0UOh426gIdVzUuj6O1Kz8YnZlk4-ENML6B4Gong-R5ODmDEeJyIVtG1QWgw_FMUbycSTGY_ho-UQk5mKjVNiiizpiuwhH8FSrb98GZ0yOGf4DgwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DF8t1Lc0u-yDpi8fkIICDoumD5IvF8EbKZo9a0eTSb4Vrqr0e59OfWYqBgkAT0jxwXLyd-kIDsmuo8iPzse31CjvybHSjQUrPTY1UbNaMK8242ki9V2-4wMbP-EVbzwUYnpdjcIousFxJVLDT3x3Q90Bg1Tc_B5w1-iCdbfy-m9UTXFe8SOfFOLKIx52qi_Q02ETk7vmc-8QU9vCWbuDI-vO5Zvktven2G6m7nBCIDPeMmITmMMHDsfhEFa1-w2ZPsp9pCideWuVcjRb6uNeOq33gz7GGI43hbeVcE5tuJRUoi5rU_V0taTQOf-cLX1zEy_N6_rSVNZqpbp9_eBNDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏆
دو داور فرانسوی، تورپن و لتیکسیه، از ادامه قضاوت در جام‌جهانی کنار گذاشته شدند. دلیل این تصمیم حضور کشور فرانسه در نیمه‌نهایی است. این دو داور از شانس‌های اصلی قضاوت فینال جام‌جهانی بودند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/99923" target="_blank">📅 13:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99922">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgRoCLaYsARDL_LhEtIsO93xtjwUo_QJ5anYlXscxwvfCHq7Gp2M71zBytmuVEXb5By0-mzf2L06Veswb71IRZZn2stV_5Q-B9s3sufzhlDepeR7S0RF-JhTteEge2n1Nn31f961NOI7p0AaNYbuqLLzq_RfGBiD-qUqpNRVcLhwCITPcXMPk1QdHxUJfT_iKD7fS3qAgqGGDxWk1R4yGN1sgVPXfhvjmYLWZktRjlVImny8zHITHRZZfMHf7d5UWhVuiiCv5LlvZ_KvwKcOMwlGIBLmMsHHzo_InKfm0RdSdfEbQS917q79JAO4qK6X7xlsOh7gNBKqLq2crLyScQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: بزودی یوری تیلمانس به منچستریونایتد HERE WE GO SOON
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/99922" target="_blank">📅 13:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99921">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bae154b9d.mp4?token=OQ6mpAnmbGTNuSHFKEBZ77gFTZiYe_5A2urGIDU2TtqhzTYXN8RqPD6JC6k0SbmDEa5SHFHDU7eGOhCMd3CRB8bJMRaOI1ANs8f7u12ImNsRw09oPisNzKuRwwiuC5lioz1VkZCt7VNIoNl1RLny0EOaZHn6GvI82S8ndgq6tgiMGJ0ZBMQgbTyDNrVOLqSuIh4mKGbfHH8JwwfopXQ1lL3ZkYzpG6TXX0WrOdezoIaCMAioqDTeEhVjFXhQHigdmIf-5l8aj0Lq-Bg33H6MBy2vsgRX62-uQs4FdkA53VQY70Hbcilrd2f0ddavDAulHaQOxZU0RPC8e0YsmkFriw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bae154b9d.mp4?token=OQ6mpAnmbGTNuSHFKEBZ77gFTZiYe_5A2urGIDU2TtqhzTYXN8RqPD6JC6k0SbmDEa5SHFHDU7eGOhCMd3CRB8bJMRaOI1ANs8f7u12ImNsRw09oPisNzKuRwwiuC5lioz1VkZCt7VNIoNl1RLny0EOaZHn6GvI82S8ndgq6tgiMGJ0ZBMQgbTyDNrVOLqSuIh4mKGbfHH8JwwfopXQ1lL3ZkYzpG6TXX0WrOdezoIaCMAioqDTeEhVjFXhQHigdmIf-5l8aj0Lq-Bg33H6MBy2vsgRX62-uQs4FdkA53VQY70Hbcilrd2f0ddavDAulHaQOxZU0RPC8e0YsmkFriw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرحسین رستمی: وریا غفوری رو یه ایران میپرستن...
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/99921" target="_blank">📅 13:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99920">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scbTP5wsLTJGDa53mvf8WEBqSyjLqV9gitqEvh3kL7rlnVyJTr5-O36PMka6fkJPA4ZcGbu6xN7mxHSQ-WLk14kkfPCv9ZCVEwXjoNgppjKayz_4Fk9paEJSm9RX-HTqFzaNgWEvDdORVu7klvXfiaaZJxOaUGHXN9xdI-6qflGh8mSAIhM1ses04UwHYj29Jzf_L3g6WBK7oB4qZMv4LLAGiFh6bPYitFXZLttkv3xmro76ScuuUtri4tS345SUm-1go9AzgFEc3VBJIcUHTCK1keg9pK7SEfXbwpyE8pcK_Z0Jehj8ovR3O0V2li7nyAd6psNp74AZyi1yo_-LYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری دیوید اورنشتین: باشگاه منچستریونایتد درحال مذاکره جدی با استون‌ویلا برای جذب یوری تیلمانس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/99920" target="_blank">📅 13:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99919">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
دیوید اورنشتین: باشگاه منچستریونایتد درحال مذاکره جدی با استون‌ویلا برای جذب یوری تیلمانس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/99919" target="_blank">📅 13:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99918">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70585e20b2.mp4?token=uldHDi6XMcGZyFCK_xJHaUDwevaofO7ArAwbOk5VzZa6g5AaTTOUJWcc5xfiiOwLzMmgalz8M4fhExdOEQoKUkADdQUzakRKpz1OzdHxY3vuqaxaPfSxsw0Qyq-NNHnuw07yt3e6vbTYAMRdcPyD37GS-YsXxHlIKXKwdiMfrPhAkh86ckza4_d95ZjbjKLTvUfyoe_65TyY7g4O7pBqEW8nfxTuvFpBEskkKP0wlugRqm3p8Ez89a44SzXqCgxttUo7e2dzvriA5UnFxDLUd6uagXaOJLd7hr1LtVtg8u9RcKILcWpx5hzWok6KmUNpxlTsjQQ14St89IYl-I0Xgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70585e20b2.mp4?token=uldHDi6XMcGZyFCK_xJHaUDwevaofO7ArAwbOk5VzZa6g5AaTTOUJWcc5xfiiOwLzMmgalz8M4fhExdOEQoKUkADdQUzakRKpz1OzdHxY3vuqaxaPfSxsw0Qyq-NNHnuw07yt3e6vbTYAMRdcPyD37GS-YsXxHlIKXKwdiMfrPhAkh86ckza4_d95ZjbjKLTvUfyoe_65TyY7g4O7pBqEW8nfxTuvFpBEskkKP0wlugRqm3p8Ez89a44SzXqCgxttUo7e2dzvriA5UnFxDLUd6uagXaOJLd7hr1LtVtg8u9RcKILcWpx5hzWok6KmUNpxlTsjQQ14St89IYl-I0Xgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تیکه ابوطالب به صحبت‌های اخیر بهاره افشاری: لطفا چمن مارو بذارید‌تو کیسه مشکی اگه خانم بهاره افشاری ناراحت نمیشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/99918" target="_blank">📅 13:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99917">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7de78bd0d8.mp4?token=C8WNryPMahWxRfhnB2wyDGZ4Amt1folOyLU4lr3atJiX91buyKuHFPYvHPxxeU6064ffr4ttDBoMJgSzn8OQ-EQMPoxJgLagVdkjaHSU2d3rDV9N36saam_DJHUXUIE3YkMbt5GjJul2wGo83cnNfKlWwW0ShUhdSYWWRGWDWZAe-Ew6kSQi87MWGzoNl8trzkhv-JuHHAAaWhGxleLZ-3p5s2n9p9hQPGv1im7aT2tREyAK6bPjaz8eYims5A-9W2g-KxGhrQz_e3O1Svm5T4_fcakzRPgsTRCl7I7CGGptKiFKgWA09rxWObVRBpdab6uhvrgfT3Xdh9QD9w3yFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7de78bd0d8.mp4?token=C8WNryPMahWxRfhnB2wyDGZ4Amt1folOyLU4lr3atJiX91buyKuHFPYvHPxxeU6064ffr4ttDBoMJgSzn8OQ-EQMPoxJgLagVdkjaHSU2d3rDV9N36saam_DJHUXUIE3YkMbt5GjJul2wGo83cnNfKlWwW0ShUhdSYWWRGWDWZAe-Ew6kSQi87MWGzoNl8trzkhv-JuHHAAaWhGxleLZ-3p5s2n9p9hQPGv1im7aT2tREyAK6bPjaz8eYims5A-9W2g-KxGhrQz_e3O1Svm5T4_fcakzRPgsTRCl7I7CGGptKiFKgWA09rxWObVRBpdab6uhvrgfT3Xdh9QD9w3yFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روحیه ستودنی حمید علیدوستی عزیز در مبارزه با بیماری سرطان
👍
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/99917" target="_blank">📅 13:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99916">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E35c1MilQwzBq7K4IkdOYh6ZNibXP6a0PVf77Zu_2C1HZUc9zYMtX59ayAt_R7eGKqOESvjU3i-tSl_tjD8HL1NiZD9UImxvCnqEzv1X-jIA3qdoVl2hqE1y4_VJBOW-JoiSy5xIGfe4t-CPZOHUKlKowbKLpn9XCeHggqN8KcXY_H3R_sj8jxtPIi_lND7xH6pGZcPjWFGhLdTeUtMdDe01U3xkgusddffN0nlCwEJWvGSt-eV-kVRfUxYGvqNYQCr5LY5-fjzPTs68FJzPX5vlNSGZOneBdlzjhopAq9wtSAVRT8BsrWkXpnXUFEu7CMUbKf98ZJnA8tK3ZoRDfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوری از رومانو: رئال‌مادرید درحال مذاکره برای تمدید قرارداد یک بازیکن بسیار مهم و حیاتی است که این بازیکن وینیسیوس و شوامنی نیستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/99916" target="_blank">📅 12:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99914">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b696c11339.mp4?token=J_fN7Zc36M4ZkhArVdiw-2DEQEnoVGz1b5v1FXi3-K0F86GujowF_V2eU8rim2XE0yAdc-GIDUHx1YFp4Kg_3h7a-0FfHja38R_YFw_mteh3XTXUAQLLp5YD7CWD6SFews3qcLIU7PSMfa8xymeUpkeGIxK7e18gO3ns1hfpZBt4fVXB40ODnWPr2FVI5jKVzaP4OPw751PZPOtOL5uhOURsMUSB3MDWiT3qqmNma36Sj7Lp3Kh5-kpMoIqU9M_mWzvPm1LEFJrvOiACFtvdYA9WRGVZt_2yUU2vRDMAk2vwt3LR5e3E5vhJif_4tOHAEhSCwOqGhSADUDWBTyKwgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b696c11339.mp4?token=J_fN7Zc36M4ZkhArVdiw-2DEQEnoVGz1b5v1FXi3-K0F86GujowF_V2eU8rim2XE0yAdc-GIDUHx1YFp4Kg_3h7a-0FfHja38R_YFw_mteh3XTXUAQLLp5YD7CWD6SFews3qcLIU7PSMfa8xymeUpkeGIxK7e18gO3ns1hfpZBt4fVXB40ODnWPr2FVI5jKVzaP4OPw751PZPOtOL5uhOURsMUSB3MDWiT3qqmNma36Sj7Lp3Kh5-kpMoIqU9M_mWzvPm1LEFJrvOiACFtvdYA9WRGVZt_2yUU2vRDMAk2vwt3LR5e3E5vhJif_4tOHAEhSCwOqGhSADUDWBTyKwgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
آتش‌زدن پیراهن لیونل‌مسی در مصر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/99914" target="_blank">📅 12:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99913">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb9971900e.mp4?token=BZbRxAB8JXHJXLuTtQYK7WudCXDw7sGrx1Y8kr-pYdpHuT5wh1sfVGmBGbYfS6DU8W4bmRByBZLdZvXHOE16P8pMZXU0e4VLQd-aTl_B_KCZzoIxCyxOczKccqJCKC6mAxtIfAOSDo8OiI5eFDLZI8nDCwI-iAXlZqNVSCLefWj02_O6UdSbhFvEvvFerqroSifcGRaIPZYlQwPRl-997lFGJ6z_Y-UFkshI32Mx546hXupiZfROe3yQvtOQo4DI5QiEILC9AqVhS-SAYD9qdc9AWxCaJAxbHb9m8x4yCltZDX6MLP6d7nkSSYEAF3DkT8MXkYBrZ_dnTFXczOmm5YY6vzt4a5sTQkVEkHNKkDFTgtXh8F7Se7nQZjsMLbuJfOXWH1n_SdtzSZV9-nu-HcvCHDaT7w9VtPNyV6eKMoPP14HTlnpaHaL6j1C75aNvVk0OgC2Xcj1nre1cGA6Fh3a9kzsuI4ct5ohSvN6UjjSx6SwNes2U0ieMqvrh8bU5wgYjZWLZVZqU0D8glzEX5ISPBTpEAdtNqYhqwKSWdOyV7IhrjxTeKyPrl9FjRTCRD5-Ea96bQl20Jh8-bsLQmI5yfBMAiHovyPKrEwcwxXY6EEYX7Q339rwRe_HytFJATTBggw3uZPaENtFql8nv1G_v6U3K_XbAbyofwqotWyM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb9971900e.mp4?token=BZbRxAB8JXHJXLuTtQYK7WudCXDw7sGrx1Y8kr-pYdpHuT5wh1sfVGmBGbYfS6DU8W4bmRByBZLdZvXHOE16P8pMZXU0e4VLQd-aTl_B_KCZzoIxCyxOczKccqJCKC6mAxtIfAOSDo8OiI5eFDLZI8nDCwI-iAXlZqNVSCLefWj02_O6UdSbhFvEvvFerqroSifcGRaIPZYlQwPRl-997lFGJ6z_Y-UFkshI32Mx546hXupiZfROe3yQvtOQo4DI5QiEILC9AqVhS-SAYD9qdc9AWxCaJAxbHb9m8x4yCltZDX6MLP6d7nkSSYEAF3DkT8MXkYBrZ_dnTFXczOmm5YY6vzt4a5sTQkVEkHNKkDFTgtXh8F7Se7nQZjsMLbuJfOXWH1n_SdtzSZV9-nu-HcvCHDaT7w9VtPNyV6eKMoPP14HTlnpaHaL6j1C75aNvVk0OgC2Xcj1nre1cGA6Fh3a9kzsuI4ct5ohSvN6UjjSx6SwNes2U0ieMqvrh8bU5wgYjZWLZVZqU0D8glzEX5ISPBTpEAdtNqYhqwKSWdOyV7IhrjxTeKyPrl9FjRTCRD5-Ea96bQl20Jh8-bsLQmI5yfBMAiHovyPKrEwcwxXY6EEYX7Q339rwRe_HytFJATTBggw3uZPaENtFql8nv1G_v6U3K_XbAbyofwqotWyM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینید و بشنوید از سرود زیبای بازیکنان تیم ملی آرژانتین در رختکن پس از صعود به نیمه نهایی جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99913" target="_blank">📅 12:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99912">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
❌
🔴
مدیریت بانک‌شهر بدنبال ایجاد تغییراتی در بدنه مدیریتی باشگاه پرسپولیس است و اگر اتفاق خاصی رخ ندهد احتمالا پیمان حدادی بزودی از مدیرعاملی سرخپوشان جدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99912" target="_blank">📅 12:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99911">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYq0C2JJLZbhl6nAdRV9AuMc7iRCxqv4FMVhG-gHqamd2k1egnGg0_L92xlLLFZ5EwE4sISxuNgFLDV7ztee041D3k7nxnYVUCsX_nzdsvEE0GWpcVLjncnTqPqlbRW3_dc9N4VU6Q1tExCrrMRyyIbtngTEScyLZGUKH1p0fQrSkBS1zFIYgnNPN0FnbZ4e4IVhttNRh4ObZug9pE3DGfClYI1nTdT4h_oSmazFW04HJwz-lavZpT3-F8GJdwfn9F-eMRBz9kaMTTuMgNd9LY2hMJrPAX_sJipnAglE53aRfi5V2epyFOTF2TPKbrNfc4WJVswK5KnlpHB1Z3P7sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
👀
مسیر جدید فن‌های کریستیانو رونالدو :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99911" target="_blank">📅 12:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99910">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOlBIXjDHxngUmz-Usv_aKtBao7MlmpwOzC4PmIu4C_DoT1Pt7hUl1hKDrXrkMaGb_oZrUAEVSHrsbXOKJayt0KiTOknkC7knJUQQaK95aaoty2kGLpf5utSPoawnwNfSaF5YVhi3FuwyIIhgDIjoxgHbRPmUGGVQ_b8C7wmAEz6F5HhOt3FAFW1o3c3EeHq5O3Bm9TOh4C3-dKIm1eas-vHia4mLB86IKp-ykxL6HtMn0Pryk6_EGpA53EbY3eRVk_RSc-FABQkr8pzPf0hDtuBik2LcleDFbqw79ePivPBm228mE2rcsvn8nVB9WLsxKppK0lx43-SDqt_gTO58g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🎙
ژوزه‌مورینیو:
«من سال 2003 شروع به کسب جام‌ها کردم و آخرین جامم را در سال 2022 به دست آوردم. این یعنی 20 سال افتخار و قهرمانی. به همین دلیل است که می‌خواهید داستان من را بشنوید. همانطور که می‌دانید، فیلم‌های مستند درباره افرادی ساخته نمی‌شوند که هیچ دستاوردی نداشته باشند.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99910" target="_blank">📅 11:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99908">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5142dd144e.mp4?token=eZb-OtcScw2zHMx2rEM-Cv1xeAMfzB-puNDT_Cg3UVJUmUnetBUbiB104_NRi024lRY5wtVC2lLedSUEUaHsFj0PPKvKC2DgoZJzp4t-l6tGj5ZlzclSK76deLceXNT3UkvJYd7mV3LIpEr1qx5GuxBksX_1Ox5FKBi-WQBLaI5SrOFI23xSSAR9OTOjGlP2vBKIjVKwQJDQcd_t_ivZgIl7Mkg7A3YuuijybSaRmv_WLJ_6vwrYtLoWEEZsFfiVReuDgdjldgz4QHIXPSydBl1BRRehrkEjOR2_SbD-yFhVZk0O4ZGqF728fxxP4eU2WW29gAru8G-FYhDxksIgVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5142dd144e.mp4?token=eZb-OtcScw2zHMx2rEM-Cv1xeAMfzB-puNDT_Cg3UVJUmUnetBUbiB104_NRi024lRY5wtVC2lLedSUEUaHsFj0PPKvKC2DgoZJzp4t-l6tGj5ZlzclSK76deLceXNT3UkvJYd7mV3LIpEr1qx5GuxBksX_1Ox5FKBi-WQBLaI5SrOFI23xSSAR9OTOjGlP2vBKIjVKwQJDQcd_t_ivZgIl7Mkg7A3YuuijybSaRmv_WLJ_6vwrYtLoWEEZsFfiVReuDgdjldgz4QHIXPSydBl1BRRehrkEjOR2_SbD-yFhVZk0O4ZGqF728fxxP4eU2WW29gAru8G-FYhDxksIgVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🏆
🇩🇪
سال 2014 درچنین‌روزی؛ آلمان با گل «ماریو گوتزه» در وقت‌های اضافه مقابل آرژانتین به پیروزی رسید و برای چهارمین‌بار فاتح جام جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/99908" target="_blank">📅 11:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99907">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNeQVsFCGTE_IOaTJPe8BRgp9lD0iv5Vzm78rbLPPpnXCYvIBT4OVyI6vgbDec1OaBu194VrgXTKsqlMtLmf1ZVEr1Jd_2-ecfiRgSPYWEizNmLeOfaeRfUQNtOgDwDL7rR6K28qAK30s993UJGIo-sxM2_6aoCwq0Z1goMyERqyd60cSjiyQeG6pQLE2DuIs_MaZLZtWUV_sdFTJXnjWdYzkaZOgoocr_ABpY7ccopJpnzqAC15aXvbtm5hHWgGprWXZSGB1SS0-SWWD5cj--8CMFsSrlHHn7bWU18KE-3uNdjblS-jlSgGZOBSzSK7T7VW7xCYnZDP72JQJMqEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لامین یامال بعد از اینکه سال‌ها 18 سالش بود بالاخره امروز 19 سالش شد.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99907" target="_blank">📅 11:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99906">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/724b974651.mp4?token=ABd-XAgSmzn2O1nLXvcMc_8TSTKf_DrxUMYt1B27euHEKoCkmoowUdJ4e-LtHCUnOq0iD4wn1eSk05eFYD3xDM4RL9zmbKj-SVtKIl7uGQUz3nanUoJo1JXn_lsZ1FYp5M9pEBDgnzkmXyCwLvfdA1R_iBq90VFKEqbSCFAa5tarVV9ym_FGCK3288jG_gqQIhZ_weZmCV6t0mKAlypCif-T_9AC3tpsmdL_ZXvh3tXzffbQfF9njcrJlSXPnsO6aKQBaL3sZg_VXr2haD88gH0MSEC8-YYCjtKKnzEN3jTqAKLz1msDroZhfoxF9XqZpwn7nSgvq1B_TZj3CFNk1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/724b974651.mp4?token=ABd-XAgSmzn2O1nLXvcMc_8TSTKf_DrxUMYt1B27euHEKoCkmoowUdJ4e-LtHCUnOq0iD4wn1eSk05eFYD3xDM4RL9zmbKj-SVtKIl7uGQUz3nanUoJo1JXn_lsZ1FYp5M9pEBDgnzkmXyCwLvfdA1R_iBq90VFKEqbSCFAa5tarVV9ym_FGCK3288jG_gqQIhZ_weZmCV6t0mKAlypCif-T_9AC3tpsmdL_ZXvh3tXzffbQfF9njcrJlSXPnsO6aKQBaL3sZg_VXr2haD88gH0MSEC8-YYCjtKKnzEN3jTqAKLz1msDroZhfoxF9XqZpwn7nSgvq1B_TZj3CFNk1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمو رشید وقتی میخواد از مصدومیت بگه
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99906" target="_blank">📅 11:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99905">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQLQz7t4rlzAubz99pGUx1XMlZeZmK_DtdzGEj89RQwhVnVlgxEdup7SBIqumsAAncqYESv9-OWsZjzCW3KyWOSRCf1nVV8oXb8vfR3X5ac_4V_MKF7Y5DvgY_lzQcdgyshD7vsqJEAh3gl30ktZHC_up8S0jSmXn6VblWV3u95lrNwj35XCZo-ANHXCbyFestDJd7OrFy9VmDyTuC5debQN9HV6yAFAm9Gi3utMbI904Cbq8C9hjxlCvP0HQ6XB7EHBW_CV4_nhW5dZXt8vCLp1YPQ6jT9nuQuLb0AGU32xHkNTu8N7ybOUQUxSh5bCtluG-NBTZICnjQk2eORC2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇫🇷
🇪🇸
استوری گاوی قبل بازی با فرانسه:
اونا نمیتونن شکست مون بدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99905" target="_blank">📅 11:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99904">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahnvmazHVPX3VIeRs6xyHP8NnC1O47mBFPwKHxn464PgAciB9N-tqJ0NBJixhdU_btwgGb21BK3AY8kAchewtM7NIUoTS_k9QrK5dPA0mOZ2wrVlDZEkL9MNCM0XKZNVHTBIdvDxlp87eZt8UXuHt3LJ0n85L6yKDPpJFI8mzWi0G4DAhvd1v2D90ROfY8epMeQSeoDnK06S87tmo6ZG5dqYYDNPnL--DY8iUh4oa7Elj12paEehhEOY0ch-3hbDIYTNrskDoM7cEJpGZXFQ46pIYUy_nTrweRNdqgBPkdwC2mBdaHkXEH622oRSkIxvB9zGgVcCQEUX5_uCXTSQ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇳
نیکولو شیرا:
پاتریک ویرا کاندیدای سرمربیگری تیم ملی سنگال است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/99904" target="_blank">📅 10:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99903">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e42b519e.mp4?token=elBTL3Vns8aQghaiyO7Ktq4g7_OrE-MTL-1cYzLbzp-oL4DVBgNn9gBqvOWdYW6VewvghiG9IY_tHw82jvvA8flOsoe4Zc1V6g_mc7YbFr4Jn_7eaQ3vW-RECnxuvzExBUkcHV0-HZ79UMTDsj58kHXi4YL7RC4FCZ-PM5DqJ7MSo-QcvV5nW4z14IfHoiFQnMTIQ4ZYgRfGH4EI1tUeIdGtP7IOkdXfc1V6Oxi7NcM6Hfudw0IFY8VbSZGG809iKUGecfQn_yP65qkf9YEQneT9QVPwYbMwD20SMcy78GR6quwThCzOp6R6ZrEf3jbuVittGwrW8Vhm4caegrscDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e42b519e.mp4?token=elBTL3Vns8aQghaiyO7Ktq4g7_OrE-MTL-1cYzLbzp-oL4DVBgNn9gBqvOWdYW6VewvghiG9IY_tHw82jvvA8flOsoe4Zc1V6g_mc7YbFr4Jn_7eaQ3vW-RECnxuvzExBUkcHV0-HZ79UMTDsj58kHXi4YL7RC4FCZ-PM5DqJ7MSo-QcvV5nW4z14IfHoiFQnMTIQ4ZYgRfGH4EI1tUeIdGtP7IOkdXfc1V6Oxi7NcM6Hfudw0IFY8VbSZGG809iKUGecfQn_yP65qkf9YEQneT9QVPwYbMwD20SMcy78GR6quwThCzOp6R6ZrEf3jbuVittGwrW8Vhm4caegrscDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصدومیت لیونل‌مسی در بازی سوئیس از ناحیه چشم که خطر به سرعت رفع شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99903" target="_blank">📅 10:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99900">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YzIENjrFoBglLezmIMb_JaQ1Hok7VEg3iQk8Lc_3Ni67QOdC0Mokq_7Bn87xxLkc77IeJYoqFMOLkDI_hjnANWBMbWuQR93orVwZTG0N0PT6b4hzIOyd6R12TIojdtSlLK8uycQFYZoCE4WqyQJwCs78iKmmacBUhTVK7cJ3jJIe5PQSWBMwL8asrTMi7I6WWG_c5YafZtu9SpH3-9aWnN52J_WeVL0ljQVnQNBv9FH0AlvYx0wD8HZ0Z-rU-9rj9hqU3YUP7n0epA38zIGHgncYzlw_rrHHZzisZVfUtrq9EKxmgp8fIVJKyQXzcmNOsTLqyQfZCbMkdtC72aoEZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c9F4jbyPOYEo5jEurrtHh0X52lG5g7p14DzSko1gGfUswWq-UO69dpT0ngs6ytlTTADeWlC7GgNAl4ejD6fT53G4ngD0oLu5xBabRNt_jN4HjcXksz0HQmUFtQTgtk7gaekc6ohGFwRkPWo_xwLKsjL_M7hyGgIeorC7M2Tay_nX-zoGlzgCTFpMTkfO-VSClR_gSrem3ItZxZYb4X8Ni7stR49u8U496zNvUWlhHsh6_z9EZ6TCmwK4r0xN5tNng9uS8msbmz0OdOsaJjCE8VvWJL6AXcUAfj6pSF8igxdRBZNkNKg_qGGKXIAOQY_SQuO3rkBpaNZtavXMHaouXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oluk-eTn8Co8kxSnvBPmqfGbWLLMF1kVzha-a_QiqBVr6FqxCE7soc0zRKw3emBbNFOX3z6P3OLYrJCgxYEySrWA3RyGsZDURNfFqkAt50n6CBVuY9hWQhV3IFia3tTRjFPmB0rlVA_mgghF4Q7QkGEixzmqe03wllZ7Lxn4lCiEt2OvQsSD_9SMvaKTbsA71a6abkKGQAlXykLBnzqbCAV9di8FCjLma63CYTOhZO7SL3KHCJPxsM-avpjSS_ksh_B2RRYtjTM2-XHVceyXs1bXYwhPBxH7X79vm_lcsuQh4DJmm5QMhAYPdamcuJbZmhaUDQyGFZAq2G_GcZpK_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
یک سال پیش در چنین روزی چلسی با برد 3-0 مقابل پاری سن ژرمن برای دومین بار در تاریخ خود قهرمان جام باشگاه های جهان شد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99900" target="_blank">📅 10:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99899">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7079ceb818.mp4?token=gUwXxAVyrX1x4T3Y7M0nRK8A5SfvO3RTvE4aykILkaO34Vo1k_ceYgaL_yacLvVXwzDmt9WxW8fDIwaImgIsgVvoJXKZuJuOXnYAqSYLxLSHdoPUbKE4pXppj_YMisb370sh6c0nSo1EsOkjDkUh__qGcWoHTvX7Lfi33a-Ity3LeMUR30FD1nHgrnB6-0O4UKt4sDnBolaH5FgUswW-X1pr_E_HcRszWuUIDIROQZp3A2UjWTTNP258ykDNvnFrutjTdi8buYz98MJAq68KFPFVpRGRjEnVyq7Ke16fmXTpeLbUARnU2of2x-BWcesyOKn4tBGZMUnr1x5hYK2zSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7079ceb818.mp4?token=gUwXxAVyrX1x4T3Y7M0nRK8A5SfvO3RTvE4aykILkaO34Vo1k_ceYgaL_yacLvVXwzDmt9WxW8fDIwaImgIsgVvoJXKZuJuOXnYAqSYLxLSHdoPUbKE4pXppj_YMisb370sh6c0nSo1EsOkjDkUh__qGcWoHTvX7Lfi33a-Ity3LeMUR30FD1nHgrnB6-0O4UKt4sDnBolaH5FgUswW-X1pr_E_HcRszWuUIDIROQZp3A2UjWTTNP258ykDNvnFrutjTdi8buYz98MJAq68KFPFVpRGRjEnVyq7Ke16fmXTpeLbUARnU2of2x-BWcesyOKn4tBGZMUnr1x5hYK2zSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
جیدن آدامز؛ روایتی تلخ از درخشش و خودکشی در طول یک جام‌جهانی!
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99899" target="_blank">📅 10:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99898">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeYIr-42A0UplpFprR-iscW601g38KsL-VTUpatxwEEEmw91W-cB3o7kOF-uUkHVFrGSqyun6c0ijtl6OuwYcYKRiKQs4k-2sKoemiBPyNmeHLYuBmx53i8dc6_4TjINOnjQOVuYoM4apeDOlE53k3GmZQ-wfMMRpyfapA_ch6dAunpPp21dHIKwzGTUKGBUT2IdlrpeupTe8-tonSwssbyJ9umyISwLzsS5YO2mYPJHR4QJgAhS1pkCkqnoZXIqYizvwbLEyx5Qpm4qBl7HGgGsrONQNHalUngJTPUaUIkurE9tbKzJK25kh6Lp82T9Gnukrc8FYdd91KBaseCYzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙️
نيكو ويليامز [
🇪🇸
]: امباپه یک بازیکن فوق‌العاده است، اما ما بهترین بازیکن دنیا را داریم: لامین یامال."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/99898" target="_blank">📅 10:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99897">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2501cb2ee1.mp4?token=fNJVRXNspI4K92-WB6n58L-kIr_EpMJNdVd3LWj4SfxWc3Z3rd4uDIWvSTSwSDRM4YFB5rnXaxcqxMlkgJGkdmZedumhEzWIr_6XAdPYf58tVNoZAIwxrlbjkdgvSwbUI7WsqEqJo2Txx0SzKDJgod8meNEko-PhmCQgNLO5na7b0YSQ_owY-mMz85CSsHUJ_lSKxwS5shER5ZNjjzvsCFF9gbjzQKEANCByBrbxfJcjAoU6sT8WW6dttdWAvEteYDM07xouZFtEu8-aEr4n5ZTN22NK1mhKe9cuaJ1TOJfIwesIMA5CXzciceHH8dHeHJWAaoLM3STjfILzgK6hAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2501cb2ee1.mp4?token=fNJVRXNspI4K92-WB6n58L-kIr_EpMJNdVd3LWj4SfxWc3Z3rd4uDIWvSTSwSDRM4YFB5rnXaxcqxMlkgJGkdmZedumhEzWIr_6XAdPYf58tVNoZAIwxrlbjkdgvSwbUI7WsqEqJo2Txx0SzKDJgod8meNEko-PhmCQgNLO5na7b0YSQ_owY-mMz85CSsHUJ_lSKxwS5shER5ZNjjzvsCFF9gbjzQKEANCByBrbxfJcjAoU6sT8WW6dttdWAvEteYDM07xouZFtEu8-aEr4n5ZTN22NK1mhKe9cuaJ1TOJfIwesIMA5CXzciceHH8dHeHJWAaoLM3STjfILzgK6hAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
خیابانی و خداداد عزیزی دیشب نزدیک‌بود وسط برنامه زنده به همدیگه تجاوز کنن که برنامه رو وسطش قطع کردن
😂
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99897" target="_blank">📅 09:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99896">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f0aac58e8.mp4?token=MFI9qYvAHfq_AyxoqJaE1c5XlfhACcGUpOotvmYRcFVQj_qHVxqCFj269nwmrD6MNUVMEfdKVZbTc61Bm4MtTbXwyEiuHGrhWYvcvfznYbRe1IeRiHCVNMvN9fIhGDxP0FGOcp8qd80rxZH28QdgHoRwXkLQ4sAqmDBOnelBkU9PJZ0MQvXK2yB9nUMw0Oi8XuY-l7CXmhNKc8xdJdq27p2DRYTKRH13Y4GogPO9j-C5wXDKkzAnoC-iK3x0MCgzmzvRcmV_v05U4CC0yAwvuEzJ0nRLMebR8kDG-8DcMlXY976tMyj4AXCfwEjTtxQB0zCnLpsB2A0tKGU63SN4Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f0aac58e8.mp4?token=MFI9qYvAHfq_AyxoqJaE1c5XlfhACcGUpOotvmYRcFVQj_qHVxqCFj269nwmrD6MNUVMEfdKVZbTc61Bm4MtTbXwyEiuHGrhWYvcvfznYbRe1IeRiHCVNMvN9fIhGDxP0FGOcp8qd80rxZH28QdgHoRwXkLQ4sAqmDBOnelBkU9PJZ0MQvXK2yB9nUMw0Oi8XuY-l7CXmhNKc8xdJdq27p2DRYTKRH13Y4GogPO9j-C5wXDKkzAnoC-iK3x0MCgzmzvRcmV_v05U4CC0yAwvuEzJ0nRLMebR8kDG-8DcMlXY976tMyj4AXCfwEjTtxQB0zCnLpsB2A0tKGU63SN4Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
خاطره هاشم بیک‌زاده از احمدی‌نژاد و روحانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/99896" target="_blank">📅 09:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99895">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a56d32af8.mp4?token=piCVvmZybIRhjvv2HAgIDkkGceW91R93TDTLyx_9HG5tPu9dcAg2uluCE5ToTHbG0BolqUKb5cJP0u9umboL5YJpJu-4JGB97f-OszW6RTHLW1ogTFchYJU9WVecfaWBhiShAu98AM-51H0fmqY2XNdJi0JTkfpOduAUTRT8wEtPPBEECc745bTuCNxqqzLKGuQHGUJblJB6aHB5q__rpgQ0EA6S27XByJvvIMUO6tJVJp8wecTRavuRHUnZKUyat37As26BtBD-z-9XystjKYujN9tji9CzcIc8w7dGxSACMn78lI88eRSUVWbWxjckqOqDCy_uzJVxE3F7yvVPzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a56d32af8.mp4?token=piCVvmZybIRhjvv2HAgIDkkGceW91R93TDTLyx_9HG5tPu9dcAg2uluCE5ToTHbG0BolqUKb5cJP0u9umboL5YJpJu-4JGB97f-OszW6RTHLW1ogTFchYJU9WVecfaWBhiShAu98AM-51H0fmqY2XNdJi0JTkfpOduAUTRT8wEtPPBEECc745bTuCNxqqzLKGuQHGUJblJB6aHB5q__rpgQ0EA6S27XByJvvIMUO6tJVJp8wecTRavuRHUnZKUyat37As26BtBD-z-9XystjKYujN9tji9CzcIc8w7dGxSACMn78lI88eRSUVWbWxjckqOqDCy_uzJVxE3F7yvVPzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
🎙
خاطره شنیدنی رضا جاودانی درباره شکیرا
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/99895" target="_blank">📅 09:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99894">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HyhNIu_tvETGUxXQdKoDh07F4ivZCC9GzqV8InDCMsc42eMEPxYNpNiN9aPG4b6Xwzi88C1sVuOzll7CFmkVwSaWK0QJgnb77VTLD6Efo0amtysJOYAG-ivJ2DTztoncl5Ocv3eMGW8WArfu2MY_yXjDpC8_skzR7HHcu1BxeH3HmvEt6b3T7rSedpIr7Sqkrel-ytXxorgCW3TYbkFNYAwZjEfTeITlS6ZeQ_thfWPX4lwpAYmZgGAoRcil1sTbu6gnI6_JY-nctPKFpNFHfoQObstqMdSUKdTpC_x1tkrrky1wFPhLU7frL7AG8msixb-spNT3AdIcQRdGiQ9asA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
🇪🇸
ایوان‌بارتون داور اهل السالوادور بازی اسپانیا و فرانسه را قضاوت خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99894" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99892">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I9ykGQsB3opHWoaXLHx3oEjK2L_LvU7B5jBzuduJR5cy5RHBUEiC6Sh-58aO4xviiiXJlO_106w5LWAbNDiEVX5WvngzdcAfoUnuGdSPuHvgCBytAEs3WkEZYdYDu51Dt9Q4bC1HPBhiJog_6YjqepWeNpdixtqZZs0Z_sGLMugbdtlmnXGrIg3e7PaNSYfVR8uFBrAsUYv3fu2aNawPjEZJsDHkyiFWKnNHoAuynHtgIswnHuPDcAk3ozwVtbdQeDr3wuPAOfz1Fjc79xI6h5Hb-WxPRFtw43iZ_ljz78QLCoXYCKg--Z0rj_qOaKXGZ3HIqWnLxzgTfN4AtHaGPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CLI0sGZIP5DHpvE_sW_TXQNNB5bf1dMvr6_bpgyrYRhzH6ThyFpThHWO3WOyPiz5J2eLkrtr7yZN6cDRnHhtitE1xlKFMQdAYL11FkNYcJQe0aMS3KFvLH6rFCfIvQtOfNJao-FpLhJMv21CC1lJwSgMLRkZGKizXSUrPmaz3jLcBEXClmKk1usIy0sI_io9-u32gI4ubTPYdZ582F9-mQ_xAsuDX1GT-BLBl_RSVKCKBYgxIhZUkFELX8GNaFZ6X4Edt9Iw8EwrhUhjuuRpML5Hqu4cHRcUWpYEXFY6FVBcYlYAE3vkq84U2dUZ4bvrdFJT9TQYeGl0CrvO7ZuuIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جورجینا در کنار رونالدو با کپشن “Daddy
💘
” که میگه کریس حسابی حالش خوبه، نگرانش نباشید و برید به بگاییای خودتون برسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/99892" target="_blank">📅 05:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99891">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1MpkHxCuzrwfTG_BpQ_fBb6sB8Xv8u-k1Ue2fAu-LKUmdXd4PnEfoAAOBurYyJmqhsh_IvXTOHCJKiGQBMAnBAm9vtwQjWJanJqiz7xpgGEOpUq9FxVB3tqJabNJiKGxqNxOejVzxehwK8zJJH6oq3CSQVNmgp_tm34Wa_WW2MkSuW70UR94LVpia_KZvTr2KSy4qQQ31bwAXJ1iBGA7xs7j2XjLBhFKFZ8mXmPPVxjPOd1WQ5NRRdqBWugcOn86R7VZbv-KG4Q5T3W8emYhDGMNzo9Iz7wzFEXNbHVFUrBug0qvXQYAMf-pKkN4HyOA9XwxR4gZ8kmEFCIf4ZqNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
#فوری
از بن‌جیکوبز: الاهلی عربستان در ساعات اخیر با ارائه پیشنهادی نجومی به مارسی و دستمزد فوق‌العاده به گرینوود خواستار عقد قرارداد با این بازیکن شده. مذاکرات گرینوود با فنرباغچه پیشرفت خیلی‌خوبی داشته و فقط دلارهای سعودی میتونه این انتقال رو منتفی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/99891" target="_blank">📅 02:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99890">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f230afe8.mp4?token=OPmuzuAp63MhAIxW10_zKYPPq1Im41Ge8qlpsWX0BLFoecMWm2H9-Gob1SnIl__KuMqiFM0SId_15OMOe2wggz_oswgfKpWCNVtZ8LtN1NP_BFLLHm178Zml3GUMIE3dSt5nCW9BUzM1X2UlDEMJ-0aw9gaJOa9q7AT4n6cEcBAW8FH7kNIbbQXuJR6Ux4d2fquh8pjOGUxwXjmNkNOTaXsVyGcEETmNVZR46-CpCJy6srnHTCQZwF-kHmz9gGkwXW7JDVMVHcL6_fCXeIsdxk-IzRYovtm9w1048H_Byz-WOzfVLYEqtjz68f-y5MOEJJmzetCt3Uck78c-bazjyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f230afe8.mp4?token=OPmuzuAp63MhAIxW10_zKYPPq1Im41Ge8qlpsWX0BLFoecMWm2H9-Gob1SnIl__KuMqiFM0SId_15OMOe2wggz_oswgfKpWCNVtZ8LtN1NP_BFLLHm178Zml3GUMIE3dSt5nCW9BUzM1X2UlDEMJ-0aw9gaJOa9q7AT4n6cEcBAW8FH7kNIbbQXuJR6Ux4d2fquh8pjOGUxwXjmNkNOTaXsVyGcEETmNVZR46-CpCJy6srnHTCQZwF-kHmz9gGkwXW7JDVMVHcL6_fCXeIsdxk-IzRYovtm9w1048H_Byz-WOzfVLYEqtjz68f-y5MOEJJmzetCt3Uck78c-bazjyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
🔵
دختر علیرضا بیرانوند: بابام استقلالیه و دوس داره بره استقلال
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/Futball180TV/99890" target="_blank">📅 01:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99889">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🇪🇸
🎙
خوان لاپورتا: ما تو بارسلونا برای هرکسی دولاپهنا نمیشیم. یه پیشنهادی برای اتلتیکو ارسال شده و هیچگونه تغییری قرار نیست اتفاق بیفته. بزودی می‌بینید که‌پرونده آلوارز به کجا میرسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/99889" target="_blank">📅 01:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99888">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6_MuqOXpfY33DAfjo5zNjnIXrZkAJ8p8Kh712HkIzH7VdwdJAt-vd44x2qzeAdyXk0m5AP38-s7Uuxs8Hx4Mh_XJEquEBiYjR2hejWEjlKMQWFlYerQWpkQ2rVM60c3mUTGs4LxFP6530qqJTyTLZXBlL-ZvRdmoUOiaSqxzNahLNAWIW4SNysq0B9PZky0Qc_gF5bGDhcwfaMjJGDvr3iSW11Y0BAfifnEcNDzC3_fuwt_WB8Bx5cX3e5MpVhcDCq8q6fwuvqzyOg7MEY_VEISAxEEYIWLuMkIXpaqOyTohANTLs2X5d3FOcxgP2kXdfyZjbBfQ0haVY43k2fotg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوووووری؛ اسپورت: باشگاه بارسلونا حداکثر مبلغ ۱۳۰ میلیون یورو برای جذب آلوارز به باشگاه اتلتیکومادرید پیشنهاد خواهد داد و رقم بیشتری پیشنهاد نمی‌دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/99888" target="_blank">📅 01:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99887">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpeinUb_4yNFA_GzYZ1w4FaRJOKl6GZl22-migZ9J8KKP7AlfbRo2iL0QFrMuQ3F4ExSkr4-aWSl31azgSV7bMOJDi5cPLyWyrtlTrtETv6COAsvBUPCbmMAyBh61wTuv7MLVWUFpL71iDzBLkhmC5D1tmKTkck7vaYK4p9ffx2_75HoHnmWbVSsnhts7Pb8PCltte_3Z9_wXew1DiFfCjEz8-EGWQEaE8v7u_5Wo71_n9e2QtBPm_phOPSH_KzPXNY6ZHKajusuvD9IeVWq-s40d57jwgV2v9US--dYTi69TEWdes5DqP9fw50XEvHkWQZJQFu8xH6-Q6ffmms89A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
💪
‏ سوخت‌رسان‌های متعدد در خلیج‌فارس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/99887" target="_blank">📅 01:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99886">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2Nm0Za5btTUE8UejvOaA1zQjRlWxDfiavAL4VsztLSlJ18a9wAwssBqamj4cHz9gP_8uzE0hp1ClUer7zlMrFTfEf2cFa5qjZfsDSzSUWw7UAyyBbShRAstVk1YWXsvwbwRqeydWhVDvZ9IcCBGqlB_GXOLO_VHmmRR5AGgYe4XQDccCzMgcRkedtMK-LkhQ149EcSpXLALQAZI66Kl2RK2G1xfAjPpTtXPUaL_iB-If2SEKCd1ayUeaike78twwl4KpeuJ_l7CVNxpgGh8syucxEcNIrcMHvqtyF_O7-Jm3EacmmnXr1B9cHRSeXKTVp03dNpa1c8_LzofBzOu2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوری
از رومانو: رئال‌مادرید درحال مذاکره برای تمدید قرارداد یک بازیکن بسیار مهم و حیاتی است که این بازیکن وینیسیوس و شوامنی نیستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/99886" target="_blank">📅 01:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99885">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvXAKU4ph54-DG5YYr2s1r5duA1PdK9bhbfae9qjcJ5eAOSKFcO_c83HG662VqW2_inO8Ok0pGxDs9oUzXZP6YbuC2oRmx4QUQu1HC4wdnzxfaCmSY2-95qv-JneIeYf4Hf8NXYwX9JXtOgRwQa39004sUnkDfCyW9r3B87j0ykaA1KPoRqjgop1vfB_6yGdJ8hiCxx3mQdDpMm6QI-7Yw8Jzs45FD-q7r-DcqHglv-9Afh2tf8k2rGBn8MpMoThmJCfE5MBPxHybzCnfccq54yELGcgOoYk9nNAioU8U0QymSiZPolxTGDM1uOy0gAPX_A94T6JpExsWjl_sfKndQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لامین‌یامال با توپ ویژه فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/99885" target="_blank">📅 01:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99884">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6AVIHPuXV7COfxdy0tUQLnG2cjqWNqFK81Kwh0FL4SQOv_1Y6XatiEd4ikw0cQVATXulKBPL9MXmt-M2DubURBDW1a9oI3mRmHodaeAJqgfo3RKzMbSBHXKx9Ff2EFaZmnOI3S2ClpPCqFVsywkOzeXVGMxw9qEQjrVEDwPEXsHPPYHMImhorAbdhvlOx__vzpHxrUcTjD9-fF0B7d6MM7LWt_0N-I4fUt4lYA5EPL_n5_VzZ2Vyfvz60R-CoO9xdM--w1sN_zQAHiMIG8zPsPO0sJG-Lwr7MFZO1xMEqExf9Cc0GB_PEh76vzT9hZnkNIgqYTt-VOs5gObleMMLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
سنتکام-حمله به جنوب ایران آغاز شد
ساعت ۵ بعد از ظهر امروز به وقت شرق آمریکا، نیروهای فرماندهی مرکزی ایالات متحده حملات بیشتری را علیه ایران آغاز کردند تا به تضعیف توانایی آنها در حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه هرمز عبور می‌کنند، ادامه دهند. فرمانده کل قوا دستور این حملات را برای پاسخگو کردن نیروهای ایرانی صادر کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/99884" target="_blank">📅 00:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99883">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
انفجارهای متعدد در سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/99883" target="_blank">📅 00:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99882">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
چندیدن انفجار‌های شدید و پیاپی در مناطقی از بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/99882" target="_blank">📅 00:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99881">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
#فوووووری؛ شنیده شدن صدای انفجار در مناطقی از استان هرمزگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/99881" target="_blank">📅 00:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99880">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M7NVehrm82z0G5tp7ik7wuM27a0A8hGBmwAIqfBXAlmbskG1F5f9508cXMbgO_AsPk8MVl3fbbUJkWIslLarF0-u4I8Bu1E_iq_HgYjVoEbpSdQu6mpEhpBgC5vubAvtBJAPZHUsvvHUmYXMnPEyNNensON_WdwAB9cx92DF4LizWCl3dhdEf9eIfkZJ1X7s2HFfMSSrvUZ3_tnY7KywhjhOGb6XlfjNYWc6mYLURKkMAznscdZQ7h4rJdW3gF9wdJS7bJ8U93nb1aj6jtH2uDeUk-jj-ca5vw5K9hprNfkg8GmUDasm2MjfiiZzgzM9j8sUhS8ZA03fuX4ZBIgx2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
پرواز سه سوخت‌رسان از فرودگاه بن‌گوریون اسرائیل به سمت(احتمالا) خلیج‌فارسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/99880" target="_blank">📅 00:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99879">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
#فوووووری
؛ شنیده شدن صدای انفجار در مناطقی از استان هرمزگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/99879" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99878">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab9b193566.mp4?token=OwE_mE5RhDRyREzDKtMRJlSDq6kgvE_chI-Bb7SMx6EaYPGd-pPCBWjMpYeDp2FJQpnHYQqLm7l6gHznamEB06E07O-zYvLupCpjSbXfFojZKTp6FwVsF-hLBsItPgm1Hb3VpxcYVVCmL3g92xhSIFXEhoTRGFgOQZ_zC3Uky-AthLc0mKld5jA3Vv0ylcSmgvqWlKSyzg1nM9E_0IoRQX-p4aRGKFtL8TiuQWUYHfbz04cvUT9vKKrbEZwGVLegkxZoy5rGbwafjAaUMCfqc2cvhjJUGLca3uajlzomIe4vWb18HpLT0KmS9vJ2ZEAlVIV8G2XMHt0ZUucRDaDRwCP9KGUqM1Uebkd7y3dJapn8jIQ6Yvk8UuuVsUxxH_pP5L1-fFUSmk1U_4e9bGe1EtJ6suxhKlRhYbGN_defSfissUpD9piLhGnNi1l_URbdQtaONcmdWRMDV7-IyLiBKEsqvKMqgJCyzGVy45IKNUl4kelxOIWAp3hFNXM9rpB5-N62lpHQp1lw-elD_NnqrJzSsGjcN9z7Tzutff2K81BAPkU6K0in0LFLMXMIal8aWazSG8zQT_69jsj3yJzdOWxq5Va1s15M6qrvu0eT9c8fAwj1PsfhJN4wGEtrAcM5I16rAm3iY7c89BWal1jUU55n-ocXmfTtO-xuyz_4zKY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab9b193566.mp4?token=OwE_mE5RhDRyREzDKtMRJlSDq6kgvE_chI-Bb7SMx6EaYPGd-pPCBWjMpYeDp2FJQpnHYQqLm7l6gHznamEB06E07O-zYvLupCpjSbXfFojZKTp6FwVsF-hLBsItPgm1Hb3VpxcYVVCmL3g92xhSIFXEhoTRGFgOQZ_zC3Uky-AthLc0mKld5jA3Vv0ylcSmgvqWlKSyzg1nM9E_0IoRQX-p4aRGKFtL8TiuQWUYHfbz04cvUT9vKKrbEZwGVLegkxZoy5rGbwafjAaUMCfqc2cvhjJUGLca3uajlzomIe4vWb18HpLT0KmS9vJ2ZEAlVIV8G2XMHt0ZUucRDaDRwCP9KGUqM1Uebkd7y3dJapn8jIQ6Yvk8UuuVsUxxH_pP5L1-fFUSmk1U_4e9bGe1EtJ6suxhKlRhYbGN_defSfissUpD9piLhGnNi1l_URbdQtaONcmdWRMDV7-IyLiBKEsqvKMqgJCyzGVy45IKNUl4kelxOIWAp3hFNXM9rpB5-N62lpHQp1lw-elD_NnqrJzSsGjcN9z7Tzutff2K81BAPkU6K0in0LFLMXMIal8aWazSG8zQT_69jsj3yJzdOWxq5Va1s15M6qrvu0eT9c8fAwj1PsfhJN4wGEtrAcM5I16rAm3iY7c89BWal1jUU55n-ocXmfTtO-xuyz_4zKY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
بیرانوند: این نیوزیلند بود که ما را دست کم گرفت و می‌گفت کشور جنگ‌زده هستیم تا بتواند ما را راحت ببرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/99878" target="_blank">📅 00:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99877">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6782dde8a.mp4?token=Bc1yrtcUGH-5ZgyjKEy7iZjipxiemjTtdNFX6jwYPL0ZnxnaHviLd664-gzG6jI5SFhx8HqN3tWwBK66RhJ3rxS5fJb-x2JyGCeB4vT7OCX4Y8WHLYO5EBmCnPSCUncrSeH6zWfm-8iO7HWItCco2F_d4lnLXALyCcoOJNpWFOWsFo28qMVzGKyEsTWKIveIPrf9k6aq0dk6rVfhyR-4A9AaktpwHY0RjE2eeEccj5C7ldcVnt-CP_fcQHJ4AjkEvzxofGvlf4nZt3ulNngL4zN9OKxN1h6pR9CSeOiNwNT8chKOMYs9CSUj4wQIKiaX53bj8B2xmlKW3eRBzpTnxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6782dde8a.mp4?token=Bc1yrtcUGH-5ZgyjKEy7iZjipxiemjTtdNFX6jwYPL0ZnxnaHviLd664-gzG6jI5SFhx8HqN3tWwBK66RhJ3rxS5fJb-x2JyGCeB4vT7OCX4Y8WHLYO5EBmCnPSCUncrSeH6zWfm-8iO7HWItCco2F_d4lnLXALyCcoOJNpWFOWsFo28qMVzGKyEsTWKIveIPrf9k6aq0dk6rVfhyR-4A9AaktpwHY0RjE2eeEccj5C7ldcVnt-CP_fcQHJ4AjkEvzxofGvlf4nZt3ulNngL4zN9OKxN1h6pR9CSeOiNwNT8chKOMYs9CSUj4wQIKiaX53bj8B2xmlKW3eRBzpTnxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
😆
بیرانوند: آخرین بازی دوستانه ما پیش از دیدار با نیوزیلند، با کارمندان کمپ تیخوانا بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/99877" target="_blank">📅 00:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99876">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b76e61623.mp4?token=JJkiJ8_FfocatcoV41c9-1SiLgn0fjnXE12_SK-bOT1IaWD-KhJAsXIhGQUaz42WeWVBpO_0BIggaCNNByHV-R0CssbC5WWKZecPaG451s3VzPRm56OCDBwOsSJdJTSrBaURDCpdOS2fIzZOIywvgviwrmHRTRb-KDCmrGNtCMbK7mN43k3p0sKAIAwIqSvQZbPM68vn9csi1kXerXJGosbPahV9zSKAL8bMyphKViPlBHqxoiGe0l7LPFHPsSGuBo4vvGf5HVzaIw5mj4czYlASWVSynT4Jg8OsgQpB3yTVDecTq0pCSxyNfIKTBOqNh5HkcKCLhfuC-YCG9Uv5Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b76e61623.mp4?token=JJkiJ8_FfocatcoV41c9-1SiLgn0fjnXE12_SK-bOT1IaWD-KhJAsXIhGQUaz42WeWVBpO_0BIggaCNNByHV-R0CssbC5WWKZecPaG451s3VzPRm56OCDBwOsSJdJTSrBaURDCpdOS2fIzZOIywvgviwrmHRTRb-KDCmrGNtCMbK7mN43k3p0sKAIAwIqSvQZbPM68vn9csi1kXerXJGosbPahV9zSKAL8bMyphKViPlBHqxoiGe0l7LPFHPsSGuBo4vvGf5HVzaIw5mj4czYlASWVSynT4Jg8OsgQpB3yTVDecTq0pCSxyNfIKTBOqNh5HkcKCLhfuC-YCG9Uv5Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجری شبکه سه خطاب به بیرانوند و اعضای تیم‌منتخب فوتبال‌ایران:
از ته قلبم بهتون خسته نباشید میگم
در ادامه رو به دوربین:
به زحمت این بچه ها باید احترام بگذاریم
😐
😐
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/99876" target="_blank">📅 00:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99875">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7990a07676.mp4?token=Czqq7AmCzIx8Dgvt7uRbQ7ruoBL_TCXchBn0EujwHm6oR9zuU78amhDIMipupiJ6WBjWgTQXWQjsIATUUUaw1wCeGl5uMkqOcRRLxrzSaBL1ZmEDrsfoptwbTxxU1i4IrOSiXnl9rd_TfVEHs3keixJmFJOxlX4GNO-3VEmv18OmNk6GJDLio3phpJ-EJb3sAzitvC5I_6oOIcQqiiDM306hAklnFydLeifN2YqHDYX--ErkCDytqM01Bcy_Qns5XJ9Mot1zCfB5F_2d1IeEIB5YZ3VgaREEGwiyjMLgMlJ5M1FsylvBVd3Q3zCf4n9w1YEAGNXCyCJ39WnOg-BdBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7990a07676.mp4?token=Czqq7AmCzIx8Dgvt7uRbQ7ruoBL_TCXchBn0EujwHm6oR9zuU78amhDIMipupiJ6WBjWgTQXWQjsIATUUUaw1wCeGl5uMkqOcRRLxrzSaBL1ZmEDrsfoptwbTxxU1i4IrOSiXnl9rd_TfVEHs3keixJmFJOxlX4GNO-3VEmv18OmNk6GJDLio3phpJ-EJb3sAzitvC5I_6oOIcQqiiDM306hAklnFydLeifN2YqHDYX--ErkCDytqM01Bcy_Qns5XJ9Mot1zCfB5F_2d1IeEIB5YZ3VgaREEGwiyjMLgMlJ5M1FsylvBVd3Q3zCf4n9w1YEAGNXCyCJ39WnOg-BdBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
علیرضا بیرانوند: هرکسی جای قلعه نویی بود و با این نتایج برمی‌گشت، مجسه او را می ساختیم. خیلی از کارشناسان خارجی گفتند که باید مجسه بازیکنان ایرانی را بسازید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/99875" target="_blank">📅 00:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99874">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_HPkN_30u7NFGqF5o1UUsja_UkM5w6BSTpYz-6C2iaoiHX7pd18vzMqGxLlDDJuzaY1fGrLouSl9yIIgxmKyR_uT_wECpUyWKOlcvFLNTatj6noww5ydbOdOTs8gMequM7si0mB2iD4GHKMaXPV11nldIaFrZ5HDFH9hlvF0GaJaCQGtrW-Vm7mfyCo7AtFROcE7k2wRcTqfDmcAiOBsYnY5I2dKiaxv4sEtPcVxwjLPZuyaLsxTq6is3m8k4He_C0I-QeTeb-cKHKyoHXQ85v-v8IkPVkPMVC_Po7-3hsTRJEkMqV7qsIv-oz3r71XEr119F9kIn3v8EPZO8ZVSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوووووری
از موندو: بارسلونا در صورت جدایی فران‌تورس و عدم موفقیت در جذب خولیان آلوارز به سراغ پدرو نتو ستاره چلسی میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/99874" target="_blank">📅 00:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99873">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFj8KzL3oxkeG_1y8H78pPdWctNkfKE74utPUjtrjJtE_l5vVdkEVZhxV6ggtL77bc-vPO9OZ1t342Z6WohY3XXCb5QAR33ygM-pXLjeKAaVT0D21caBn3lD6UwO5bE2U0XJ-Q62H6I8SlPwNI2HW-s_8V7s4iOb5msAV6yLSQmyeFsKxNauYBPrwXa4Q8mqfMbq4keNsB-IHba_-Q-HC9bTXaaIwklREDCQmo2H6QRy5nN3da6AW2pu6lcefqzOpQuQ0XWCiOupkSP_2yghIKDO12om1KxpobNo_LWp5MiXupzQTYWwF400DJ8-eXo_R66XTpXsKcr6_IbOfVNqdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جود بلینگهام با توپ ویژه فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/99873" target="_blank">📅 00:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99872">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
‼️
🎙
بیرانوند: ما بدون باخت به ایران برگشتیم و این برای مردم ما یک افتخار است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/99872" target="_blank">📅 00:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99871">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/99871" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👌🏼
تنها
#سایت
با بونوس های واقعی
😮
به ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان شارژ میده
💰
✅
نصب اپلیکیشن بدون فیلتر
🚫</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99871" target="_blank">📅 00:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99870">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2JFohRzV8CHXXGBOD_kIiCdFMR2Geug99iZ8JHiVz_Sram_XSlFyAeyHc_8V570zdH5hSZhtUkPLFuNpjiXmI4Vq8UASjJmEmf09SJHlD0REn8JqAOq3szwbdxW4gd7r_xNfWMDaRmnCVbZ8HVbadn6E92lgkT7T901MW3o3ZEYsWH4Y7EqfZM11ZQjT0PpCeQsb2viho9mKDauw7cOG4UDN8sUNkr0EInDMEzL8Riw54sdl_N1vPh7m76_UKgEBQheKiGpmNRHl1CC_qR5TFFBipf3Iycpa4hfEsxRcVZ4krrWhL3CkzGIL-1H6CrJHsD4_KNI1vVevVGAlP0nxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هر
1,000,000
شارژ مساوی با 1,200,000 شارژ در سایت بدون قیدو شرط
💖
💵
هر بار حسابتو شارژ کنی
0️⃣
2️⃣
🅰️
شارژ اضافی میگیری بدون محدودیت
🔴
اگر هم باخت بدی همون لحظه
0️⃣
2️⃣
درصد  مبلغ باخت به حسابت برمیگرده.
⌛
همه بونوس ها بی قیدوشرطن:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
a22
@betinjabet</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/99870" target="_blank">📅 00:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99868">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wB4GpmYkkKBLcIGr6bxc6SFSuCQo-Y1Xd0vUyVow9VC4TnO7G9NDRqlYVttDzi96_jE7VpwaPLzwVhBEDOp9xx-aDzwZvXxcnOXeLZ0zC8LwZ3W3UkMPKzB2dDizXfylWsz6hjzug2cFHIqNVnZ_8vn9ym0DopKbmkPnPu-LcLzWSRoIpshhGPVuetKcRKQ7Uys6RGGAxZouFCF_CLv0e9WCQ5ihD4g4WxD24p964we1cxI7Z42SNzIpABqCzvRrRF_0d6ItZeCevPvZBcmBrGNbcmSMUAEbefbYYQlLx5RbcDcBMORRgNe8Ed_-qKo_A-FfgbWWB7KJ2AO1qmuJxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#فوووووری
؛ باشگاه لاشخور اینتر درحال مذاکره با جان‌استونز برای جذب رایگان این مدافع مستحکم تیم‌ملی انگلیس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99868" target="_blank">📅 00:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99867">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
⭕️
🤩
باشگاه نساجی مازندران موفق به هایجک کسری‌طاهری از پرسپولیس شد تا حضور این ستاره جوان در جمع شاگردان مهدی تارتار منتفی شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/99867" target="_blank">📅 00:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99866">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VYIzn2elXtaKEVVbQ3xGgne1IVSkEY0vKxwUxJADLNMDdf7iUden2vgVkSBJR3-Kpd13nQO_yHFL_hiR6cQ-4KepoBKkegFNqOqN4zVGH58DxFlkH9BQK3LsXqMnqpf64lUxyTyTLOm2qWgLeyx_8JNXg1ffQxs7O-JQ1ouJwFwWpW82xJSaK3spQNLqh39wEggPt-RMP4oH_C4vdaYDNuzXwUsDprx05uunFEK4VTL9Dx_GQINnWFXUPScVly6PZ7X-oWlHHNPYaLDrOxmyrvOAAfjhzBnLXEiN3VdB9yEHRAvxJ_2kioT5SPftpv7zroF8IuEC9Ielj467X2XyaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری
از فلوریان پلتنبرگ: یوهان مانزامبی ستاره ۲۰ ساله فرایبورگ پس از درخشش در جام‌جهانی با تیم‌ملی سوئیس به استون‌ویلا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/99866" target="_blank">📅 23:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99865">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rC5cKzW18xgFgAF78LMgS_TlU4PSUfwGLyO0sCuX1hXKqfoAY0tlTKVTvAXh32krE3pINa679d3Vb_bgXR6aDd08SCTcnS0YVsAriNmAlDG9A5Cw4BsFLa1Zz2YqlnlgsFwbe3TUnYAaXpjmidv8GpxV26p6uiQbXpoIlqHQD0RE0KnOHDC5XVTzOo6vVPPRqfDhetzsxoSPyH-6AmBhSo9RxkdLGwauPtUX6pH57f0ecorj2kSLsgjPwan-uXBIyZvlwawU6lpCesRxmF_t5rP8uqI09h71rT731Pl8a4diLLlhGa3OzhdmyWg5U8yJW5Skvnawlu9ldYaTxyyYfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇧🇪
#فوری
از رومانو: یان سومر گلر فصل قبل اینتر به کلوب بروژ بلژیک HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/99865" target="_blank">📅 23:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99864">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLocnbEAf-FThfeWAH98s0G9kvSnNdNx-tpy_IUJSA-1gEOG6gOfu3t9-QHYVMPMa_OwIgAw_vnQ89to76ja4_G29koR66Hznup7n4Q4Lba8ht2cTPmEsy9UEedxyM-O4B2Sjs3IYUHZlHds0t7x0GbekU98Zr0y1Xwu-ePe7HDwX2gZBNTRNahNqu72YGOGPGR7D4-1sHX-lGq_EUIBR7ACoTDKEcYdphgdBQVi1S3QO6m2o7jWHdVgrMDD4rULDUlEW3aa675Ef1cVVgXYVlX-80qDydLt6-eRVWO1aqzbz6PxDYWWypXG2CVoVnqWPde6ccgXcIQKu-rcutUAbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو هم دیشب تماشاگر ویژه بازی آرژانتین بوده
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/99864" target="_blank">📅 23:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99863">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxfYLOXDEErLHv9NZ-p0DiZawxszuhN8g0YOsgvAVtgLVs1PowBz7z658Ci2oYBgr_XbOthOQzG0ycUrKClYCOJ56bFt9UMvdgB6E_SM5F6sV8dT2htgyLZrnLSLUmXKcA3bxPgXSe5fVWwr8T56PANl_WQktfl8iiv68B_OltrM3rQyewNxFICB6hl7ZZGb0cByM7v7U7CqHC5Kd9e10kRqilMn0I6r2-e8WTkdVdQD7Ath2Ys94Vjml-IB4XzYM73OwT9j9lSWjgVTkLG1M-G2ILSdcDuLdNfdyft8tR_6vp6bM51bMVqEpS8GAbqYWJ8Ubjb5UXOXsN5rozIL0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلوارز و دختر کوچولوش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/99863" target="_blank">📅 23:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99862">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1K1voygGvdYs8eRd7znc54OTQFmWVte3gy9CQLZ22cGZ9YyImUw45YmEi-xi4IPfyzEGc02Pfl00XgWfYID64AIJx-k0mT3AwXhZphqQ5EYjx2m-RPCKvmFJvdU5oXA0lx_DKSQEdAFSFZ-5r5FePQ5BJUL6eNtT4HBdWBxte08Fph-v4achgOI_0_RZXRCjqo_mP-8e42bxYpEyF2vuWuT_anRhB_x3Q-pXB9efH9w-3RWcJSmG07ye45K7mbJL5R9joAaLnN3eLHkbMMUriusmZNTWVwHuIgFKeaw0p3V4fGwwkv2JOK7q-lTkjxJ0A7MArNCU4Xw4HMvIJzMLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیگو فورلان ، سرمربی جدید تیم ملی اروگوئه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/99862" target="_blank">📅 22:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99861">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8Nki0ZLe9cCsCJudne-vIQTRZf1xpTBUMTi7hJe9zdMSXEGOWbqTojvahW6NX6f1jnbuvn5Runr9CM_BUer2AaZ29Hpj7sLy98LKpAYM3yRjIKTRo8ZaFNMbXPRNqz3rxoUHmq3Dy6Po3hRpIZVr1inMIMO8EWpu7aAPB-l1mJ4QW-Y-lOEBrXmzVUqLiccYAlLjorw10Csuxs8lweGryu93jxwO7FgLGEh0rpJNprY6m9daGHu_ZdjZK0QOAGNG3zmgxbQBTiY97Kz6VmWB5qJYC8MjoCQEdbL8YyPBTViVErJgKyBrZFZKVJxRwlBjH8JZu4fkW-DXTRTh_oP4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
کیت دوتیم اسپانیا و فرانسه مقابل هم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/99861" target="_blank">📅 22:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99860">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJmTkD0sxJPBlqPACK2oLxCbgRnJjjMrgJlC60XNXXwOyRrRO0i9GYOFyG792pEjRt21qw-tQDPyTC73vzvVkXAIEU5OJWP7CsrLSlDG-9O_go5ADIdWKAcvD-hBMMLsW2_0yr-RXMOLUxY38-_bMDC0KBQH6HHlGrpfJnKXSWpFOc4aOPQQiUMYxBYP1nVnA2kfL7F78jhheuCW_CBxPlf15OVqQ2MhsiL97N-4emsI2erA1p9Slo--9kNSkCzqQoWQ-2ztCqv_W9rVDaNS1vbosSzB_dEtiNkH5pKXP9yHpzuX3Q62ov0wuN0lvi4mjlFiIRVakZV3oTf50GbIHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
کیت دوتیم اسپانیا و فرانسه مقابل هم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/99860" target="_blank">📅 22:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99859">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtyXndgH6UqjBbkcOsEDibBMHw3m4v5C_wymCJYx4TDM4kneA3_2xBEYur3oABLfCi1unSOVKG6_wPCuwt-7SPGeK6eoQSCK55_rgFZaR_E00djW-FtieITZ7Txr8b89W9Vv4H6HVaLftFBDsF4wf8ogvRlu6DH1U92i2uvpPBuGtzA5iQCSEBXIlnubladkOZCxWfohUCP6cwoj8a83VYjpSnMr2PF5EUVXCfW6C_SvqUOud6yxNLtSKj6bgAJTDFEDmPSxUSGlq26HiFqtc3I4BDIZWYK8Q84UjshNxMH79g7V0PVSicm-4u5kKXQAXQZL7pX_UT_oe74JqX5Twg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دلا فوئنته:
هنوز لامین واقعی را در جام جهانی ندیده‌اید، فقط منتظر بمانید تا طوفانی که ایجاد خواهد کرد را ببینید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/99859" target="_blank">📅 22:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99858">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBcugmDAKqW8VSAAHT8QraLHs4PhYUAC0d6CbACqxASl0qsJDlS7UzkXrgSQ0ov9FmbaOHALsdxotSXHsjBzEAUu5uTU4mxPXTXAAI6fNpc9E7LxenB2g9HiXF53-5izDayBQ8d5BEHzU7oycfoBIJlRZ-07gp7SoUBxvUJpxkdgJDL2KsGK1-9ZTYD22kxcUiQCaScKZs72SvR0j6jmUXpGRVCXJeszKyc7eviPGpZRu63Yfr22GhoVLs-HqaHREANU9WLMgd-rsmlhRfqLOAxmeaYYCdr13mhu10sGmOPBRv9JqFz2lkgbgVc_lVKcyWwp4VOOy7ZFZJxuomqs7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رئال مادرید معتقد است که اگر انگلیس یا فرانسه قهرمان جام جهانی شوند، توپ طلا باید به جود بلینگهام یا کیلیان امباپه برسد. آنها معتقدند که این می‌تواند شبیه توپ طلای ۲۰۲۵ باشد، زمانی که رودری به دلیل یورو آن را از وینیسیوس جونیور پیشاپیش گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/99858" target="_blank">📅 21:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99857">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
رومانو: آدیمی چهارشنبه در بارسلونا خواهد بود. سپس تست‌های پزشکی و امضای قرارداد، همه ظرف 24 ساعت انجام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/99857" target="_blank">📅 21:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99856">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
کانال 12 اسرائیل مدعی شد:
ایران قصد داشت ترامپ را در جریان سفرش به ترکیه ترور کند. اطلاعات خارجی این توطئه را کشف و به مقامات آمریکایی هشدار داد، که منجر به تعویض هواپیمای ترامپ با پرواز برگشت او به واشنگتن شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/99856" target="_blank">📅 21:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99855">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfzPhr-o_S_t2q2z-kK0Zkb983r-hwYsYuTfRt-wFapqVju46-9lv3AOelukiYDDgEhLN2tqPkLkRjIUb-dutKLadKB0UQVwWabGaNyaC6LtXFyr48SXMT2o0L09jLLKp-TKdph_ikz1Z2SIPcPe_2qMmye6naVrtHHG8pmfAIUaTpitcdqO1ym6QbgO7Q-oJ_bapRyD5VKtLwMfjtSWQ5FZuXcSzuZIATkZL6IHuagMi_gmwA1w0XjaZTSF3ljSOcLS7POOTLviIXHjzTcqMNRS_2L1OehLDbqCSNKaoC-BfSy2Lep1Pjfd8lWcpjpr8aibPR--Tq9m-2Nnm1GiFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🗞
🇪🇸
#فوووووری
رومانو: فران‌تورس علاقه‌ای به تمدید قرارداد با بارسلونا ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/99855" target="_blank">📅 21:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99854">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sdpr88VgnWwwTa9Blt8oHGVRr0P3PbjVSRErjsNH_1BohDKXqVyPZpA8dvSc_HT_PjjwFwk76UfEMUyISHnzlr56aVyPU8JKd7X0vxKcVWYXRkvl6wyHOnD38YO-cYQjXG41QT6aLlhGwtLsUl8Ja21y4Hzggzi8F0PNJLlF5RStpYdjWInxg2pksoskMd98JWn9Ltu9WaKZE3rctAhkX5apNgp_eJyexCB_4KBo1s-S7kCrC4ZaKl5V8ylrLSPhQbau7EjGXIeuoSSDet-605U3zfbDHyIR7e_MutnduF7PJDxBaa2pq0aFa8o72w5TX4FveA_i14u9I0kFfQRV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
#
فوری
؛ رومانو: میسون گرینوود در آستانه عقد قرارداد با فنرباغچه ترکیه قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/99854" target="_blank">📅 21:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99853">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNTq_JBDLnm-Niwaum5hoBsTl2rct6NBRvVoZCTnQdOoyjwxg2ehTYQ2ISHwCaVxFYgsv6N3ZMszRKLq_pYN4bBIqpwXfQsKGtsYYB686BwU65SfnaAQobqKkcr7mFNj0Sg8jrLxRL8RGC4dl7NXQxL0rF5LORpdainyyAwGTZnJNkIJlggWelnu3j5IxE2KiGQwNLb7H0u-EzBLdx-EZ5waaYd7xaCCj1WY4TJx2V-UbUfOPGnWb3FEcgIPKwknOzuhe-WPDZyqEYfq_iOTNH1FUVxRk34-aVamB04RXqTqsKRG8BROUp47mG_u1gsX3lSCoqLrry4hCLNewHp2jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوان لاپورتا مهمان ویژه بازی اسپانیا و فرانسه در دالاس خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/99853" target="_blank">📅 21:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99852">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFkqDUbdt7wEQBMvawnCJVoQsKdA0CZmYGh6TG7fSilS7zAilkyMZU_aDeCSkan7PAIwL9YatBdIk6jO2BBJbEN2WommN0mpiDyMq_DKOKuzPmLtZB6y9qQv2aoGnuyRJufqr1aoqx25FgAJ7Z8VS756xVhJqvfnBZxjLSQdEYUXD4CYe3K5_8cN0goPXBdo9sQXkY1yZp1X7BrhCqGn2kTU9j94uZfXKjy7zPvnA58GarbJaICAOK6VhECXyDCtAsZKydLOEPgvDgRTwK9efDFYmhgRikAgHX4yG7chfeFsfOZ2eicWkD8-4ZGSMbY67XXk9_EfCtx19594vjgPKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب احتمالی فرانسه مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/99852" target="_blank">📅 21:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99851">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTuBEEtIfW7cXm2fSuEhfUHx47zLTlL8pN2k-S-kYEnkmtSuDcmHKixuSpiVUbF8zlZMkTzLbDRdGkiTywb_vVV01wzhremmX1uw18-wTzWBNOoY8_ZkLZu7M2dgCpttwgK0Kxv4-JKYJqdlGGBkrgO3tnMxrSdJoLvbiZcqA5cwgjvSlaYLlfb7d8Yg0ixXCIJSR4aHBXrZ5eXlyZvUH8A6A71BCUp1Dr6JFt7bZaJXlNlQk_AWy5YU9-GkNVgSTlIx5lB4q7sSBBhIJUpCBsLOKkgnmH97AYrq_bpKYjCNyu9MLS74-NCCle-AZHqpBKPWE0zCmO3lVRItwkEbrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بیشترین تعداد پیروزی کسب شده توسط بازیکنان در تاریخ جام جهانی:
1- اسطوره مسی، 22 پیروزی
🇦🇷
🤯
2- کلوزه، 17 پیروزی
🇩🇪
2- امباپه، 17 پیروزی
🇫🇷
3- کافو، 16 پیروزی
🇧🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99851" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99850">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/Futball180TV/99850" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🚀
🛡
ثبت نام آسان و سریع
✔️
📱
اپ
ل
یکیشن را روی موبایل اندروید خود
نصب کنید و بدون نیاز به
🔤
🔤
🔤
وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99850" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99849">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/bgtnuR8F6-RqBeUcDoK4tc4wTR5C_yY6mIPX-RP3iA40jj41ekPqiVME3qNcCpJ1otIvBkMian7u27Fd0xhvKGq_iV9_rVgqLdzFN5UQsyUC_sbpW1Gcrj2okRSCG62DtUSk7t-NplA7PKMKGBR4qK8Exh5AJaDEuca9I23sR_uHQkBF1N2g6Z3U_D09Bbn3bhq4VOvSMOYE9RT4iwlUMhEOue-NXre2jkw2KD1ij-dmQDpo71li8OSvwhc5KTVK7GP03iJw6Ue7VVEfSa5qFHoggiroWoI5j7goy_y0XcyWO2QgjBwD0007vcLG3Oia3zGW_9rc9QxJRoEEKbjbhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎆
تورنومنت بزرگ
POpOK
Gamin
💥
فرصت ویژه برای علاقه‌مندان به بازی‌های کازینویی
🆒
📈
رقابت کن، امتیاز جمع کن و سهمت را از جوایز میلیادری بگیر
💰
😮
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
برای هر واریز
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
🏦
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از واریز
🔣
0️⃣
3️⃣
کش بک هفتگی
📇
امتیاز وفاداری همراه با انواع هدایای نقدی روزانه مخصوص کاربران فعال لنزبت
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
📱
https://www.lenzbet1.space</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99849" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99848">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ce2KIK4p2C1WleKHlcyrYoJK4fjm8t_GUJYNWpegqVB0bRnmjKSWwvYdHLr1zwnuYwe-oXn-F4Ri4mLi3j5YEjESJUpqPhxKmLp_ZZwZBkXTrSn4zZhcLy0JAD7Ps6v4F-P3HNjmsiRnHgUjWEwLbGwLxKOExe7UWut7P2_hAFqEgJcG76MaQsfh8wgVDmW7c_6UtXd6VeCeddoYPiF_g6uFT1_EaudfbficT1tcPk7QJZ8ijUHJ4kXiYrt-LS351aTavWtMoG_ZCWOsMcJ9ym7-lVXUSBXH2L13tfbInQYFknn4kyk_dffpigMF69tFKMmLonXo_na2dWBo22hjpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فودن و پسرش تو تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/99848" target="_blank">📅 20:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99847">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6429d99ef1.mp4?token=Gm2DtSQiQxcKSphWKrI7CpksltGeKzCYhcmyEvtb6IJwONYqi5zfIt30i_uks65d2yZEJkgZwJptw3Ufhgqwn_6iN8PVLdvLr9I3HJJ1y1Hl3V3tQkx_y5x5g5a2ApE3LRO9ZOtQoOXAe9CXi4-tZSeTlKP1ALMwNG7tjt7uZ7c5bHF-nrEhgfF-DWE8SkXfqxdVXrH5D-EfSmyIRqOYn5TIdwGRQ5E6w9DaYtnRgGx7gI75TaRPLm_t2xBaUYUlCkPj4OuiAIKotcNCGdx3l7Y-mBpys3N1poK4xugHeWm2Nrpa4vyfc6Z8cR6hLzKhlkLE-j3jOfDy7VzF6oJOJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6429d99ef1.mp4?token=Gm2DtSQiQxcKSphWKrI7CpksltGeKzCYhcmyEvtb6IJwONYqi5zfIt30i_uks65d2yZEJkgZwJptw3Ufhgqwn_6iN8PVLdvLr9I3HJJ1y1Hl3V3tQkx_y5x5g5a2ApE3LRO9ZOtQoOXAe9CXi4-tZSeTlKP1ALMwNG7tjt7uZ7c5bHF-nrEhgfF-DWE8SkXfqxdVXrH5D-EfSmyIRqOYn5TIdwGRQ5E6w9DaYtnRgGx7gI75TaRPLm_t2xBaUYUlCkPj4OuiAIKotcNCGdx3l7Y-mBpys3N1poK4xugHeWm2Nrpa4vyfc6Z8cR6hLzKhlkLE-j3jOfDy7VzF6oJOJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نروژی‌های دیوانه بعد از حذف جلو انگلیس
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99847" target="_blank">📅 20:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99846">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EahLhlGwuoIM02YjxEdgUvDyH_amXb2OYbK0Mr51ILc3euvzdnoivLhSrzRELhh0tEQZMpx79mAqs0dZtkxYyx-i8o33dwDejHJ6GoOUEXs0WjiLxQIhslKbPBnxc84mH2FYu2rg7sb_Q-7w-pxau-htpprelw7cbsBEArFRMVsoX0YdvK-JTOcPvc48RY4-agkktaBC_zFCpqPQVr25sAK-Hs95GFHLSoKqLms56tTc7k9mtyeVQH2UIIiQVIpVKO4teecAOJk8bB7oQL1rm9SHkQDE5IVLr3hY7iE9PkLugVd61oakbPmZfB78R9MgyuMCtac6sHWAYN4fYSJE2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
یک تیر و سه نشان، فرصتی متفاوت برای سپرده گذاران؛
از اعتبار یک میلیارد ریالی تا قرعه کشی هزاران جایزه در جشنواره حساب های قرض الحسنه بانک کشاورزی
🔻
جشنواره بزرگ قرعه کشی حساب های قرض الحسنه پس انداز بانک کشاورزی با هزاران جایزه ارزنده و امکان دریافت اعتبار خرید کالا تا سقف یک میلیارد ریال، تا پایان تیرماه ادامه دارد.
🔗
مشروح خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99846" target="_blank">📅 20:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99844">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0Yaa_Ku5qYJeOj7EvFIiHCJLgkLEUhT5OC3ROsVREmnngFUM8cCLVlg5KhrD7kD7kUh4ZvQF6-3dDRNcuKBRANM1rdJUXBNvwhLp9gFL9WHFc2qYjXAaYohWPi3EOUlS6wwKCFmzcqTBP4shoQeJZyttX-IYVIQONB1ZfdaD2jemB_RqhL8iIqLmTBYkMpLiwB-Rrd9vdm7j1JFsSTgXl-b1Dvqb2YdlIGqJQjQNOCJ1BM89Z_qsZgqV_OGYm9BnV4689TqIFs12CpicoMN3nh605GPh8GN_LNost58fkuoJy2fh984ts4bTZAMXT2ysryO_CxM_nk8Y-0eneJOEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
چهار تیم برتر جام‌جهانی در ادوار مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/99844" target="_blank">📅 20:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99843">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه به قشم در عصر امروز خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/99843" target="_blank">📅 19:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99842">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/984b701bc8.mp4?token=BCc9iBlcKXul7yeZpJP9lcrh8OHdZEI8eSkLlbO5V9CXBcjUPtnJewrlyLhJAZ1ftll9dRg3ckjZHVjjQDxpymZlXmA4CK8frT8niikehCsZqpFOzuk6ty8t0-i-Dnay5BLpW1JDrqM5ak3FGHk0Egw1U11403bb3pziIZu3sXXHUZQPyqOKEwBgxC0f57hzxLCX4vlXx_nGXzG8aBmNt7MA-UE8D9j3qnK_zc7SD9BRbQIY7kIQvVAnpLlS7lfPI9NP2uQQlp2pFS3M_eeuHytbhZE78jyncNsbRrjjuhJxh2M4a9zldGEGYTXdYTVmD5esIbQpk85bG7CWF-RTRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/984b701bc8.mp4?token=BCc9iBlcKXul7yeZpJP9lcrh8OHdZEI8eSkLlbO5V9CXBcjUPtnJewrlyLhJAZ1ftll9dRg3ckjZHVjjQDxpymZlXmA4CK8frT8niikehCsZqpFOzuk6ty8t0-i-Dnay5BLpW1JDrqM5ak3FGHk0Egw1U11403bb3pziIZu3sXXHUZQPyqOKEwBgxC0f57hzxLCX4vlXx_nGXzG8aBmNt7MA-UE8D9j3qnK_zc7SD9BRbQIY7kIQvVAnpLlS7lfPI9NP2uQQlp2pFS3M_eeuHytbhZE78jyncNsbRrjjuhJxh2M4a9zldGEGYTXdYTVmD5esIbQpk85bG7CWF-RTRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتسب به حملات آمریکا به جنوب ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/99842" target="_blank">📅 19:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99841">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
رسانه های عربی: ایران با موشک های کروز درحال حمله ی گسترده به ناوهای آمریکایی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/99841" target="_blank">📅 19:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99840">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
دقایقی پیش صدای چند انفجار از سمت شرق بندرعباس و محدودهٔ دریایی قشم شنیده شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/99840" target="_blank">📅 19:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99839">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d63368dc.mp4?token=RU1JRFQloRd6p4p88DvYiWOHCNWYQMQJPLluuWu0HghYtbNVPPqpJiZj1ERId2tT4Omse5uzo5F7NSCuOQMaTRFORf2qHWI59EE7dh5mG56qN1M2rck0TSwzRXm0Kwgu9_J5eUa3sWqZBtQ4Zhm0CK0UoKqJjmUqW9BGP301i3_3Vkg21j32RXsqBIDYOO5oGXlhMxblaeLwnT3KqtwJruKDQCgLBlU4IDkUNKVMFaB38tb9oLHLYoul8VvHelaqCqPh7qI77rM-X9LvNz0myWmN3BqwJrzFXbIHEjWdmvhxmpiBHCdPPQa8A_zg1ppq7xxmBW0yLAY-8CkTh7Yysg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d63368dc.mp4?token=RU1JRFQloRd6p4p88DvYiWOHCNWYQMQJPLluuWu0HghYtbNVPPqpJiZj1ERId2tT4Omse5uzo5F7NSCuOQMaTRFORf2qHWI59EE7dh5mG56qN1M2rck0TSwzRXm0Kwgu9_J5eUa3sWqZBtQ4Zhm0CK0UoKqJjmUqW9BGP301i3_3Vkg21j32RXsqBIDYOO5oGXlhMxblaeLwnT3KqtwJruKDQCgLBlU4IDkUNKVMFaB38tb9oLHLYoul8VvHelaqCqPh7qI77rM-X9LvNz0myWmN3BqwJrzFXbIHEjWdmvhxmpiBHCdPPQa8A_zg1ppq7xxmBW0yLAY-8CkTh7Yysg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
وضعیت پشم ریزون پایگاه آمریکا در کویت پس از حملات دقایقی قبل سپاه پاسداران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/99839" target="_blank">📅 19:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99837">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d4aONpDvns1a4RALV8m9v_37of8SOzWXfQTViSBgLSZNXJTNfcLeQmgtkMgSI67SOlYavUL4gJwFnkWRvIInuiYFIXT-5htGxUa-EZyBS0cAOpZcl68FTLKxU6l5yLDhkhYsBiKzU0CZBFD3Xce5960lHdTTTqDh9nlzQXvF7zs-R7SYjlGXugUOUExQDvTGn8ImbG8CyquJxBgWRJlq1EWIpSBfZPiRk1vOI7MuMDS58W2nuY2LpObMyz5jbfG-n9K3VOqimjT2eRgbk1BbqcDCMlosmNf__5sCgSjxRBKkvFSUCm6QKT9VgE-BI8-LbO-_UE-Xavkv5BJxJLEi9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kSaYmwxqjUMjFy5cBfGpc2ZtQzwwkyBXGbGQmlvU9wtGo5gOoWXNguDzZgJghnl4YEbYauad0alfm1p8u6Gipgpo6hu0n_SsNp4YaPBqUuZ-TklAlikpHgLp0Zoo3Bh2Rcag6CnNwxFXYz7p5ZxUlMFF08AmHivR70oRPbPbBXgDdGkISHrfxBFDdbDqMJY9nKgqLUVJi8_LLx70tdeRJjVzymsfVVmcneYom8eKGryCWvmDIWP5Ic_STyzsgP1EJJX516FzQ4fpGCK0Ie2JJD2qoNaurVYEkT7DqgxYGFL7xtIKmSKktCbypZu0Lh43OHI7vR_ytTxGMO3DHWA8KA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه افتخارات تیم های حاضر تو مرحله نیمه نهایی جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/99837" target="_blank">📅 19:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99836">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbfbyIL6ae6vM_1MPti9OeYHcGRu-sCGFsrWNJqUBBUcd-2HtEpGhYUNh8u8GwU5vwm8jVeG8sGwxWa6ZUQ5gIyArde5C0vtJsMof7zYxbVErEGzmHSfJHtxmK3ZttQe1Vp9Mgt2wb6oAp4max_HbAKQAcWiOvHYDVDUhwTcP3zO8GXLwQ_f7xYzM9WBab8pudqL2JpLLoqHUsPobvMkEssmfC_4ZLiFomml1wLe99UtRhSfbO1RGqBG-U_8O-hFiP7BKhlJJjF6JD3AWuOgdOtmrew_Xm_Ki-THiJ5weeEuGjOEVCf5UkXRC1AtUmcyfcjKcsmdbMckLNuTS3IeGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
متئو مورتو:
بارسلونا و اتلتیکو به زودی مذاکرات جدیدی در رابطه با آلوارز انجام خواهند داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99836" target="_blank">📅 19:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99835">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owYpB_so1ETL0Howrn6UTlFKlRL6n3sf0AQsdVD7hSGVkC50NgP92s8DgtFBF34BJdFRq78nuZ0XSANmegzB9Djw_2fn2LdG4k_VYZsceq1EgWTl_Oz1FxbW0RtkLxtqHJWM9WBvV-fDmo8bRZK3p0YtJKnFzPR54MU8vQ3oIniQ3e8DcI6f_KQEcJ8lTF9nYkCZcHQhJTr8snrpW4sN3x7BrrkH1To6vr23VAEo-MnSKe4JQWCRfReF9ZuuQaJ_E8NTbINli1d_KokVgqCUClj5KB-ZschZqIyzGzm0Gxq-8L6L1FLsftNkSISZQsKh-Mrany7ZXY3cFR_k0lb9rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🆚
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
🆚
🇪🇸
🏅
تکرار فینال دوره قبل یا شگفتی در راه هست؟
🔥
🏆
اسپانیا و فرانسه از یک سمت و آرژانتین و انگلستان از سوی دیگری برای رسیدن به افتخار حضور در فینال جام جهانی ۲۰۲۶ با هم مبارزه میکنند.
👀
⚡️
آیا این بار هم یاران مسی و امباپه در فینال بهم میرسند یا مسیر فینال متفاوت خواهد بود؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/99835" target="_blank">📅 19:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99834">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onEQuA--V8y4atbCWPkDM-83CGC6nHdkvEx0GQQYLwLwmiwJD1UUwCiIQ0hdK8U96gePSLTlrlQ8UxIhX0S7_VJvI5nqI8ucnF67ZfjmWwFy0Qtxx9l8LtQtYGXYwGSyRaH1Zn8T4Xk4UNzQ799Yr-ntklvxTKbvIsZl-gQTs6NxUf0Rlm7OnDAqTWLNgxc7xi9SMYMnn593bzUWfqFh6qsiZMI5vbdx-hraDjwgpLHs0K9qtcH9YnZDdEcmy8DbETzHSe5S9hQRhDnkM1SzefjL1Bjgsq7By6oSgJg53_35_YRSlORH9CzT2xO3VpF9OONtdIC4DdbgzuPC8DUxXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار فوق العاده رودری:
لمس توپ: 712 بار
مجموع پاس ها: 638
پاس های صحیح: 597
پاس های موفق در یک سوم حمله: 170‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99834" target="_blank">📅 18:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99833">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04227938e0.mp4?token=KsUCAUGRDUEtw4YXItWwh5HWE-2GD4Kjcaez0BWbnAwSLSOQlNIijNPjfgmKpPmMag2b1zJLe_RVwzDG2VVNYoB1DBQacxs7pqhkgCWoODhPtpH8bAqKUp9a_fBw7b1QatpUTQVXOOXqeOq8sm9o3kIv11LwpA_AqaQTsx8KDioe2Vz4CmJhop54M-VynxWsFmBZKeB6MsKqYrDoTDOpatP99eD_VDAMSIMQSLEhkMbyDPpOQ8cD7w3hLceEIW12CtLo9wEskyxTUgubWwIB-XZ3sgcS20hYtKBEZErTmiy8vENTiDZ8Nq9ZxoFv-xe9Gw_FR68BbXnzODTsRylrLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04227938e0.mp4?token=KsUCAUGRDUEtw4YXItWwh5HWE-2GD4Kjcaez0BWbnAwSLSOQlNIijNPjfgmKpPmMag2b1zJLe_RVwzDG2VVNYoB1DBQacxs7pqhkgCWoODhPtpH8bAqKUp9a_fBw7b1QatpUTQVXOOXqeOq8sm9o3kIv11LwpA_AqaQTsx8KDioe2Vz4CmJhop54M-VynxWsFmBZKeB6MsKqYrDoTDOpatP99eD_VDAMSIMQSLEhkMbyDPpOQ8cD7w3hLceEIW12CtLo9wEskyxTUgubWwIB-XZ3sgcS20hYtKBEZErTmiy8vENTiDZ8Nq9ZxoFv-xe9Gw_FR68BbXnzODTsRylrLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
ژاپن این‌شکلی داره فوتسال خودش رو گسترش میده؛ واقعا همه‌جوره باید حسرت بخوریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/99833" target="_blank">📅 18:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99832">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54e8db96a.mp4?token=eeucswoKPqKtczKc2v2Yi0jCU2VY0PBYi7hh6CGVyw9rsPc4BR7QRVFV3y9nVnDM6wT62A4UmcwlXCaBHiwNOtXxdp81xbtBDZ9ktie0_Nv1NY0a8rEfZSCvjmRGiYt2TpgH5lbo-4M2YO3ES1vs4IQGUiWGjg_0sxdsoKoFYKXRHwh-v0FTAAHXx4o44XsZajeR8jJZ3YXp6jZsGLcCKdwFRdgmz1Pj6qpUvXdObfgX-PWlF34u4cM1lL3Bd87NeEol6EJMm3mKsCEhuhD4Uw2whwi9fIeBuH-KPxg_fOEtR2j_IGUFgAQha8jwNq8W3b50R-gFyEOdDi4pY7MOAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54e8db96a.mp4?token=eeucswoKPqKtczKc2v2Yi0jCU2VY0PBYi7hh6CGVyw9rsPc4BR7QRVFV3y9nVnDM6wT62A4UmcwlXCaBHiwNOtXxdp81xbtBDZ9ktie0_Nv1NY0a8rEfZSCvjmRGiYt2TpgH5lbo-4M2YO3ES1vs4IQGUiWGjg_0sxdsoKoFYKXRHwh-v0FTAAHXx4o44XsZajeR8jJZ3YXp6jZsGLcCKdwFRdgmz1Pj6qpUvXdObfgX-PWlF34u4cM1lL3Bd87NeEol6EJMm3mKsCEhuhD4Uw2whwi9fIeBuH-KPxg_fOEtR2j_IGUFgAQha8jwNq8W3b50R-gFyEOdDi4pY7MOAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ماجرای تل سر یامال و عبارت EGO YAMAL
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99832" target="_blank">📅 18:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99831">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kV1885hk_QlXVdd47vD0yUfHNupZmzpGCgxAeKo52yK_eiguHCaetQJZATpxXZCUFVYe_FmxOzHNLOEX_6G7REZGhNtBkjm0o92rkmwf-B-GrdluXB1ZStGnZRm2JOx9G3Qeu2RAzht_dS6_CDPUGZHf0eo0-XpKbj40BlEG97e92KO5cbpunzj8fgY8qr_BCyqc6D5t2HR1LPhkqQP4Cixzl4sODOZKBEc9gzVWJVZvcoKL6bUCWFCOoGV2Tnli0n_be99_N7_RFu91CxJIxX7Q5rfYzJRam4Ec_7vDU2bQQw3uyqeoAD4LGHibX0ZWMBoxmE7R9YH7EX3LRaPFCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇸🇦
اسپورت: الهلال عربستان اعلام کرده که هیچ قصدی برای جذب رافینیا نداره و این بازیکن جزو گزینه‌های تیمش نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/99831" target="_blank">📅 18:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99830">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c48ece8c0f.mp4?token=DrTOslGlEETFDE6pU75m6zqJscO9brbDamszJLNlA4_zNHbOC0mCUtld05t7vMRkLjcRo4myRKG2KXdBQGf_dzU_boej9SxRC6ynyLxBl1c6eOzktRzZD8L_fYc6z-nzcw5Ou3UkPy0JsfMXJ7hqX9v-tNiJM3C9yKH3P6z_Eg0IQ-K6ptlKhBlXp9XVy3rs3AIdKpYexd15JjWwIm_zCuyWpJ2RKEVCWr-axM7CbxQYcBcMQi5fbFkZSpG9K7lSm1P2s-NFWPLJNVmp6eii5OCSmoDpiduN5hyLBkEDfK2-9qvOLcvcdl0TuVFStkxEfK7yWUoVLcq-nhy41xBp7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c48ece8c0f.mp4?token=DrTOslGlEETFDE6pU75m6zqJscO9brbDamszJLNlA4_zNHbOC0mCUtld05t7vMRkLjcRo4myRKG2KXdBQGf_dzU_boej9SxRC6ynyLxBl1c6eOzktRzZD8L_fYc6z-nzcw5Ou3UkPy0JsfMXJ7hqX9v-tNiJM3C9yKH3P6z_Eg0IQ-K6ptlKhBlXp9XVy3rs3AIdKpYexd15JjWwIm_zCuyWpJ2RKEVCWr-axM7CbxQYcBcMQi5fbFkZSpG9K7lSm1P2s-NFWPLJNVmp6eii5OCSmoDpiduN5hyLBkEDfK2-9qvOLcvcdl0TuVFStkxEfK7yWUoVLcq-nhy41xBp7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇳🇴
هالند تو این صحنه خودشو خیلی کنترل کرد که کون سورلوث نذاره. احمق اگه پاس میداد شاید گل میزدن شاید صعود میکردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/99830" target="_blank">📅 18:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99829">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e3eb539b.mp4?token=Qd3rTqFO6iVcXxalIhG91d4Z84ELoII_t8dWpPjNeUtyC9K-21npEmed0oynqOapMEKcZoBVlC216EcwEssY00H-l2r8QHQXS4fgXXDK2Wf-RgRYd3-MRFDtp98Byv9EgUpZ2helxZ2P6q5NmWoEsqLsCbNdaHzf5wT76LZb78T59ZY6YVc7Lm_0Xqf6d0F2KvcCBXOyOlRhFEo9SsQFShGLAtptkwCDR7ujJdqt_4Xttp8sfwABfZyJSF26nLscF_iULxStWAhX2o91VwEfjq0vASkAff8cpmJ8AENAxCid5RX2rmuOpMTVUeqXLInIRQ4zQHUL8ApSr2yzegdIag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e3eb539b.mp4?token=Qd3rTqFO6iVcXxalIhG91d4Z84ELoII_t8dWpPjNeUtyC9K-21npEmed0oynqOapMEKcZoBVlC216EcwEssY00H-l2r8QHQXS4fgXXDK2Wf-RgRYd3-MRFDtp98Byv9EgUpZ2helxZ2P6q5NmWoEsqLsCbNdaHzf5wT76LZb78T59ZY6YVc7Lm_0Xqf6d0F2KvcCBXOyOlRhFEo9SsQFShGLAtptkwCDR7ujJdqt_4Xttp8sfwABfZyJSF26nLscF_iULxStWAhX2o91VwEfjq0vASkAff8cpmJ8AENAxCid5RX2rmuOpMTVUeqXLInIRQ4zQHUL8ApSr2yzegdIag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
نیمار بعد حذف از جام‌جهانی دوباره رفت سراغ عشق و حال و کار همیشگی خودش ینی پوکر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99829" target="_blank">📅 17:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99828">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4744b6de28.mp4?token=pMzKCYCmnVxVmcCCDZ4S0XzoMJo9kfQy2KztfeutIl4vgjMrSbvGfswieqrXUWI1G3w2kbwvsY3PG1wfeE39krdEsa3eTh3wi_19ZfxUl6iBKC6R4cQywAU4InGAVXgaRc6XR7QBOor49Uj3TTL8etebIhILuSOTI2ZCzoIr5EQOS314siJgiWZP784UqdY78nNTIRxP1PdsMxJw9X_YL3fCbBcg4cA3F-aLI6ElfFBdx7Y4MeYfQjhfJUx726lHaGn8kGMXd4gpLfOqu_IPPkpQZ5XgokE_HMPpH6BMNWFlgP1dq_l4VulSUYypN6t2Jh0g0m1KxCkl8jpVtASASw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4744b6de28.mp4?token=pMzKCYCmnVxVmcCCDZ4S0XzoMJo9kfQy2KztfeutIl4vgjMrSbvGfswieqrXUWI1G3w2kbwvsY3PG1wfeE39krdEsa3eTh3wi_19ZfxUl6iBKC6R4cQywAU4InGAVXgaRc6XR7QBOor49Uj3TTL8etebIhILuSOTI2ZCzoIr5EQOS314siJgiWZP784UqdY78nNTIRxP1PdsMxJw9X_YL3fCbBcg4cA3F-aLI6ElfFBdx7Y4MeYfQjhfJUx726lHaGn8kGMXd4gpLfOqu_IPPkpQZ5XgokE_HMPpH6BMNWFlgP1dq_l4VulSUYypN6t2Jh0g0m1KxCkl8jpVtASASw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمو رشید آوردن تو ویژه برنامه جام‌جهانی غافل از اینکه دوباره برامون حماسه آفرید
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/99828" target="_blank">📅 17:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99827">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cad474a63.mp4?token=qV7YrEl1sb6VD2cn9ruNLwrWoKlz6U4H5ZRKR6KXnvhShS8zeNFtqR0iba1FEPU8JGf0t1QX6-5dF5iMgj_QmSQmeYD4a5yJkKN7vR9fRNoVeVw8n8SnN-lrIZZEEY-IjbDW_Fai4IBaSvgNIpZFELFLDd4VxCLMkFR4HlTEN5xwvUE9YV73HU9Fkxw6ggkeB-es0YWq_1Ko4s4E3MR-kjRIpgs5Eu2jKN47d6GZcNDqphQroxA9oAgpxmHBVFqjjRksb47ep9xGR-kb3DebZR98rmi6gnxDZb5L9YFYSrRrycqprqMTdJ2a-QZm1T-zD8F5uiAybo5qVLPYN5LKeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cad474a63.mp4?token=qV7YrEl1sb6VD2cn9ruNLwrWoKlz6U4H5ZRKR6KXnvhShS8zeNFtqR0iba1FEPU8JGf0t1QX6-5dF5iMgj_QmSQmeYD4a5yJkKN7vR9fRNoVeVw8n8SnN-lrIZZEEY-IjbDW_Fai4IBaSvgNIpZFELFLDd4VxCLMkFR4HlTEN5xwvUE9YV73HU9Fkxw6ggkeB-es0YWq_1Ko4s4E3MR-kjRIpgs5Eu2jKN47d6GZcNDqphQroxA9oAgpxmHBVFqjjRksb47ep9xGR-kb3DebZR98rmi6gnxDZb5L9YFYSrRrycqprqMTdJ2a-QZm1T-zD8F5uiAybo5qVLPYN5LKeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
صحبت‌های جالب سیروس میمنت بازیگر سینما نسبت به اتفاقات تیم‌قلعه‌نویی در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/99827" target="_blank">📅 17:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99826">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BexgPKa8U0k0q2U2s_wZNmMK-_hgcDCiFV1dnAAUUvemY5HnG2MMJRtCh7ZeoV5zyGzv-9k9v6XDXzAayS_gfFSg0dQWFSar3ocMD9Ti3rYnkH2zfac1xWMtQ2UIIajssXEszGoLgVhfggIIVzpmZii4baU8klOJccSZiI__BF7iZaBTIA5wh6gjUSb1HDElsZKaskgb-94mqqx6fKknY2TahgINfRCeFmUZ6hwT8WqvSB9RQigPtsm7Y1LMn3RccL-beKmeWe-893_qsQXe1FJWKt-RyE1hNJVE-eVFP0H8Xh46RpXHUXC7nZJPSBr3is10U8AgCx1V1oY4cxV5WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
ترکیب منتخب مرحله یک چهارم نهایی جام جهانی براساس نمرات سایت هواسکورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99826" target="_blank">📅 16:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99825">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇲🇽
ویدیو فیفا و انتشار تصاویر ثبت‌شده از دوربین علیرضا فغانی در حین‌بازی انگلیس و مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99825" target="_blank">📅 16:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99824">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e7ba265f.mp4?token=D5_g3IbYM7ra3Jz5np5uEzoXlK3bUWAXyNNFXCg48ILZjYUfCW7YxJlL43af6RKtUc49TDNz0Zlii01Qw_JthVV3lxEi8AKmRJxroCvynsID3piPyZNo_SSgxGBVncxs9QSvQtV_t97Lsmlp2HPknvGwsZSzReJBAuS0xosyPdeW6TfIf6sCetqSq0vw2SUOluNLc2bsSCqXtoinGVqnGgSmvzt87zzzWdwuW2eyhnlPjsQ7s8gfwEqXcbAJPRHGYf0PmxNgfsLBY3aq0KaBSblZCS4ROwP3G5NQjvmhkCl5lKIcTiFDCGOXr6z9NTn9s10V_O-jBDYnCog1jc_acw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e7ba265f.mp4?token=D5_g3IbYM7ra3Jz5np5uEzoXlK3bUWAXyNNFXCg48ILZjYUfCW7YxJlL43af6RKtUc49TDNz0Zlii01Qw_JthVV3lxEi8AKmRJxroCvynsID3piPyZNo_SSgxGBVncxs9QSvQtV_t97Lsmlp2HPknvGwsZSzReJBAuS0xosyPdeW6TfIf6sCetqSq0vw2SUOluNLc2bsSCqXtoinGVqnGgSmvzt87zzzWdwuW2eyhnlPjsQ7s8gfwEqXcbAJPRHGYf0PmxNgfsLBY3aq0KaBSblZCS4ROwP3G5NQjvmhkCl5lKIcTiFDCGOXr6z9NTn9s10V_O-jBDYnCog1jc_acw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
👀
عاشقانه‌های حسین‌ماهینی و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/99824" target="_blank">📅 16:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99823">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/affcde1f8c.mp4?token=AIJiGC1ymd0-oAdkq_uW2wEe31F2pM-yeJo9RdQyDMz-QOXw_1hdX4VlCcrVcjt4GtZSA62aiIF56sUQDjguBH4HTgI1iIIq38rh3eLwcxVjIDugcpQNaPReWtEpIQS9CtZGNTTv0yzSRAk8j7_415t_4nBtA-BYx4VRIx5Q5sBLjkUd4Xi9VgM1DVxi4EaHU9piho7Py-XO7qon7Lz8Qe6iDb12mRsrnoDBwEiPQg-AyrSMmn38LgCj424pB9ONmZwbZQf3tpsGap53InIXKJioK5WTEQGJ3BoCdTIygUKd_hcpWfd3_QDEqRPQNc88bE9dQFCqhKa3JeS7NBkaFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/affcde1f8c.mp4?token=AIJiGC1ymd0-oAdkq_uW2wEe31F2pM-yeJo9RdQyDMz-QOXw_1hdX4VlCcrVcjt4GtZSA62aiIF56sUQDjguBH4HTgI1iIIq38rh3eLwcxVjIDugcpQNaPReWtEpIQS9CtZGNTTv0yzSRAk8j7_415t_4nBtA-BYx4VRIx5Q5sBLjkUd4Xi9VgM1DVxi4EaHU9piho7Py-XO7qon7Lz8Qe6iDb12mRsrnoDBwEiPQg-AyrSMmn38LgCj424pB9ONmZwbZQf3tpsGap53InIXKJioK5WTEQGJ3BoCdTIygUKd_hcpWfd3_QDEqRPQNc88bE9dQFCqhKa3JeS7NBkaFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
واکنش دیوید بکهام به گل دیدنی بلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/99823" target="_blank">📅 16:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99822">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3eeeaa3f.mp4?token=tzJOqfe-gyj7REf5fhVzLxsr-S6Mb3GNSlAdNljEqvO5kyVaSRoTgg32XNC-CwrnF2W1vCIk2VJrZUf-wZDYFVxMJPWLRSk8RVmtR50ubxsOP5mmWfVtsZAzai9glkIEiXNtUa7JEP90QYDDS_UPC2HsMNA9_nBxd2PkcvcoWEB2ApcxmR_TRc-BGs_F0LXeVqma_WTMTF3-7DH5pu6yBaFizgwo0d0f5BK_GMx7QFXdWJejOezlNdpOMt_hNId90av8EPN-F6Gl8krpgFydiUmlbhLnWa_wNzDTg8qrrTj7CdJ6lwN4s_nBSCgSlipJuMXoPGOKMNs58n8JeKgVxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3eeeaa3f.mp4?token=tzJOqfe-gyj7REf5fhVzLxsr-S6Mb3GNSlAdNljEqvO5kyVaSRoTgg32XNC-CwrnF2W1vCIk2VJrZUf-wZDYFVxMJPWLRSk8RVmtR50ubxsOP5mmWfVtsZAzai9glkIEiXNtUa7JEP90QYDDS_UPC2HsMNA9_nBxd2PkcvcoWEB2ApcxmR_TRc-BGs_F0LXeVqma_WTMTF3-7DH5pu6yBaFizgwo0d0f5BK_GMx7QFXdWJejOezlNdpOMt_hNId90av8EPN-F6Gl8krpgFydiUmlbhLnWa_wNzDTg8qrrTj7CdJ6lwN4s_nBSCgSlipJuMXoPGOKMNs58n8JeKgVxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عیش‌و‌نوش محمدصلاح در کشور مصر بعد حذف شدن مقابل آرژانتین در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/99822" target="_blank">📅 15:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99818">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cs-4IYIffuPveBXXkLTu-xHakjgXps4hABfxEUY560fJkNF7e27NYfI6RYIvt6YtEiwPDZPmZvKc1oZcdzVOYEXs2QIyA6TU4AlqE9Ssd7MbKxtB-Ddls1vGpiWj9qoy0YM8Zr4aeVaJmGEvv-8r3xzHCf9-3BbBzeAm2AmfE1y6APILD0RyTnEHJi8inpqeiWozs48iTJfRWIb5fSpljUKyiwgPQvwvbPXvuTosJUlQ1dunBFMM7P8KsBEWHB1wxkf43k2Zw7JI3AzgwtRLl7ego1zMbCZ0OXrs_HBrynZwtLPYkwjn4Fa6DidMq1t-GvxzoNz-fQUCkg56gbEjHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SaSncV0xpFjg_GDZu31A-le1MUFGj5_ZFNqm1CrHb2k8PVehRQVeXCtNtvLAMXU0GMP7LSwhfQjkt2me8gxNjDJBkGXxh4cF0WLa0Y_UAzIDKPuxuZZvWq91yCa7-enVRVi9Jt3_axeMgOWAY9rN6VU4W3RypjOZQz6WFoz5NxbX4vOfoaBb-3tlK8XG5JGRBErWuxKvoXOu_bjJkjdXlihdIvDZFg0CulDEEP0P9jixqWRb7sfaRWOg2OitH4k3mjd9YID9qqZZ-bx5-MSMcnHAUMJFB0sPU-DAEAbn_qc6kD10NvpgQiANGIFT1nV9PCJMy9l6q9wmAAFmIokbbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IjSmzbiHum2Jgvm1G4-1O3cobqRs240VG8NHdTJFqzCB0g4Gv35jLP0J71yKwXZVGKGcxz36-E7PCTiLinsCvoplgkBXgnMuYQlRdXemVJTUdaKx3m46r7TJdaq16JWCuwbd1vpmkMLBASWKkuMAPi6QX3UyXKaRKl_2OYPIpDaNcN2dMrKvUIqug1kQ5OjEBUrspPQSyzJNq0CZcF8oFgLPSa47Ytrw4thF2b-HeI9tSTbKOZjWioQlIb7Qs_tAOSy0jSmhbF_wms6hHuTHSRQUO4WHjS3pvEfDPCN7qWq-UtLm2Mw9DKyZ3lqY_VMnbQaxFs-MLVAx_9822JKGTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CqakEXnVhwKfTPNXSvfdz1bB6eQ6aCKgzjXt7nnOJSnXIjdfRfsfoErRyk5-jo5U3Ig5Xi0Lz9ZVp1UNAy8Pc3odmRSqaxJYJRy-slK0Xi6WfIVCGmoE97jJ8iWoTDk3ALoQ3QdVY1Ok2aP3BumAK3VfNOLnPJnV2JLgFznUJD_AT3hRF6SOYMmTMIuWQ2qXHDzPXab5mQF5jmOUFTFqnj8GewAiiWERkGSTnFtKFtSM6rgSfKjipjhX2lqdgcwCKMUkJeVbGzhiuMLUfwptZ15_YI1S_M_-BFFYNP2hHiLwTIHochix8pYqRTG-G62Y3Nw57WzyA4P-bMmiOKUPDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏆
استادیوم‌هایی که میزبان ۴ بازی باقی‌مانده جام جهانی ۲۰۲۶ خواهند بود:
🏟
• استادیوم AT&T [
🇫🇷
🇪🇸
]
🏟
• استادیوم مرسدس بنز [
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
]
🏟
• استادیوم هارد راک [بازی رده‌بندی].
🏟
• استادیوم مت‌لایف [فینال جام جهانی].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/99818" target="_blank">📅 15:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99817">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRnKEVeGS0OpeLDVSjZWUaXlFQxFoT86Xp_6451plDSxm9KunibtdByQU4xSNiX2XBEj2VkQL6jcFhn6EPoaXioIKqmIGNaaAXitkNOFakiY9BRE35nJd3uldK2lF5qFcQEjpquJJZN-F35NByElWcSbMOs1EFjl5Uo477zjMNH6BYcnBkJfkS18x0ZqIUi-3OAf1D0GY5E4_h89zTK9fvw4RH4RnCQHyzmDON0m9gGJNIVmrbkPVr54-Re5LMIC51RlMp8hCyehVgc2uFSadRZoJm76NrVSMMDy5Qrz3I3gPXcpdOArqpu_-EHgBoVOMDwD91SGURZc8JhOL-WXbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد تیم ملی انگلیس در آخرین تورنمنت‌های رسمی و بزرگ:
🏆
جام جهانی 2018 — نیمه‌نهایی
🏆
یورو 2020 — فینال
🇶🇦
جام جهانی 2022 — یک‌چهارم نهایی
🏆
یورو 2024 — فینال
🏆
جام جهانی 2026 — نیمه‌نهایی
🤔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/99817" target="_blank">📅 15:16 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
