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
<img src="https://cdn5.telesco.pe/file/tDWV2_ApRonjYs_Tms2fFOjKcfHNNtM9nCLnyxqerfLyxSXxrnoKIYbL7HzV2qGKdijxm32HUFbtSLH4pkbwXrp9XQb0WKLq4PdUpKOg8oI1WgW8eeS-rpA0BHsPRSqdW5uHvF3WeLPmUMgyXJUqXlnSAOwcnzA9piwYsOXfllKTjlYi0Mi2OZSP93TdlEfIjGS39JncT5J4dczSA8dAB3kVxwAcdNMo2SyIgZJ-iQmAM-A8BoiP7Ua1aNmDXczcJqlbuiP8tLg0zkYievyNXvDcPD5QdafIGmR4cxbF47tDpJ2OurakDf_n6Nx6xVMz4ep5InfdtauFoOTgvAhkYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 443K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 14:28:49</div>
<hr>

<div class="tg-post" id="msg-104706">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f87467034f.mp4?token=U9m6Ve8uXLOklQETj5O3XwuoPKpv5_C9BdAABFUZOd0QkPVHS3NJ3rVPoUk5S0N7lwMafi5U6jbCdopdgOYWfpSKab4C8RVgMyRB9dWsLTVvkyvVLOsPXACL26x0vG042r0_-FmI8VlneRXpbILDIpiYcG6Xd-4z06jT3W2r5V0ubcByQj8zArdO32vYb-30L8kWpsKfsYfqxpOKy5ZC3VifLerbb0wOLuwlSxsmTsUUU-IcRdgj6Pqa6Vlw338hnMTSEmZ5q_YgPqy06cPMu9rY-m0bsFxzAip15L9elaSxheFDvOtuHsxcLZj-2okaVr8tGNP96_flJ-Y4WAASRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f87467034f.mp4?token=U9m6Ve8uXLOklQETj5O3XwuoPKpv5_C9BdAABFUZOd0QkPVHS3NJ3rVPoUk5S0N7lwMafi5U6jbCdopdgOYWfpSKab4C8RVgMyRB9dWsLTVvkyvVLOsPXACL26x0vG042r0_-FmI8VlneRXpbILDIpiYcG6Xd-4z06jT3W2r5V0ubcByQj8zArdO32vYb-30L8kWpsKfsYfqxpOKy5ZC3VifLerbb0wOLuwlSxsmTsUUU-IcRdgj6Pqa6Vlw338hnMTSEmZ5q_YgPqy06cPMu9rY-m0bsFxzAip15L9elaSxheFDvOtuHsxcLZj-2okaVr8tGNP96_flJ-Y4WAASRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
سردار آزمون به تیم ملی بازمی گردد؟
🎙
فاطمه مهاجرانی سخنگوی دولت در یک مصاحبه جدید از تلاش های خود مبنی بر بازگرداندن سردار آزمون به تیم ملی خبر داد و گفت:  سردار آزمون فرزند این کشور است و اگر خطایی کرده نباید از خانه بیرونش کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/Futball180TV/104706" target="_blank">📅 14:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104705">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BA2bPmOpe3_aJPKVmiW1QHz9PsiNBpwToRLHy-EtI0DeT7WGGwXLIoU_K-6SdPaNL3C367D_DIivNObkMh0njWohR3d2PU3e5XzApbNlWtY_j6-pzuTsrR5PaqK7BM17rgmMidyewvuVzY_txsBHbh387qNnMQEcrOgbZoM_uW75EnwTgNkHMHi_VgeJsyP85PzXaRNpWaO2-08sJdtUzlLH22-VDDpeeBRffaai-qFxzm8JOz3ONlwfC_6Tc5z9wsOHK2RZN1cOvwtphCNnacHxD09vpWymNVC2SF2uIxIEddFom3Nt0XJs7JbSTSiOZKHShhLADxm6bLjzJE-VVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🤯
🏴󠁧󠁢󠁥󠁮󠁧󠁿
در اتفاقی عجیب دومینک‌سوبوسلای تمام پنالتی‌های خودش رو به سمت چپ و بالای دروازه زده و با این وجود هیچ گلری نتونسته توپش رو بگیره و دوتا پنالتی که خراب کرده هم به تیرک خورده!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/Futball180TV/104705" target="_blank">📅 14:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104704">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635ed4f4de.mp4?token=eR0TzBm2ekmnr8D9mHMp7Or48sIQe0CqksjMq5CG2At5eMs457YlMSuUw0YjG2jJvfr8O0elu_xnfNATMAq9EsdYby_kwNBSK7T3UmfqlE061YW8pQH7bDCOSHmgZzWT7mfkMq74AmVIbB5rqAYlpFZoP9TCt283SE6aCBu4QrnQQH17bwvgWDggMCxXTxNmwNP3Udcdmhp5ZRTE7DANgCqtQ9QZHkfLmc5kkV6NyLL7m2o69I4JiwSXztWlyO4VO2FtNx7beNZyg1s3BE6EbsqFZPo2JXYhFODaR0W56z6mHtPM2cAOjsECYPZIVKkt7QwsHULUbOjZRyB6qWgS9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635ed4f4de.mp4?token=eR0TzBm2ekmnr8D9mHMp7Or48sIQe0CqksjMq5CG2At5eMs457YlMSuUw0YjG2jJvfr8O0elu_xnfNATMAq9EsdYby_kwNBSK7T3UmfqlE061YW8pQH7bDCOSHmgZzWT7mfkMq74AmVIbB5rqAYlpFZoP9TCt283SE6aCBu4QrnQQH17bwvgWDggMCxXTxNmwNP3Udcdmhp5ZRTE7DANgCqtQ9QZHkfLmc5kkV6NyLL7m2o69I4JiwSXztWlyO4VO2FtNx7beNZyg1s3BE6EbsqFZPo2JXYhFODaR0W56z6mHtPM2cAOjsECYPZIVKkt7QwsHULUbOjZRyB6qWgS9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
شور و هیجان بالای گزارشگر خانم لیگ‌آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/Futball180TV/104704" target="_blank">📅 13:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104703">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e638c7d28e.mp4?token=HQi_TlPqHRwewkIXVSnWtNkduzb9F38j671dv2imvp65_d-_rMm55knIPoFz1dez7DMUMZxnJmCkJHxnv0XYLSiX1nEc0q576Z4KA6aRtzrt7ap4TbDcej9baV8qCOVXoan1Isq9dcZ4h072HgoZbOFlbXODRz_mSeAux6hmaE6VU5wCYjP2w06NbMUtx86FbFkpd6lT2q0zZB53sUx5ES6xnR4EKfL7ykGMWgQfHiDX8MebQyORCYFlx5ej1Jh4rdqVDQT8Cnrq8BpfeD3ttYSPd-ZeqbcfIheY-dtg2uYL2d1rFj6sQjMfUnkVcwgjGMeCOtwcWgeVwkND0vI8Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e638c7d28e.mp4?token=HQi_TlPqHRwewkIXVSnWtNkduzb9F38j671dv2imvp65_d-_rMm55knIPoFz1dez7DMUMZxnJmCkJHxnv0XYLSiX1nEc0q576Z4KA6aRtzrt7ap4TbDcej9baV8qCOVXoan1Isq9dcZ4h072HgoZbOFlbXODRz_mSeAux6hmaE6VU5wCYjP2w06NbMUtx86FbFkpd6lT2q0zZB53sUx5ES6xnR4EKfL7ykGMWgQfHiDX8MebQyORCYFlx5ej1Jh4rdqVDQT8Cnrq8BpfeD3ttYSPd-ZeqbcfIheY-dtg2uYL2d1rFj6sQjMfUnkVcwgjGMeCOtwcWgeVwkND0vI8Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدون شرح
❤️‍🩹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/Futball180TV/104703" target="_blank">📅 13:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104702">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chCVwnWmDd99iXRNyinDI0r1rJ34Xvr9FOD3eX58rEOiogRdhC9SSEQtEHodg0SLKSc635jOLFeubDswgnGWOLHw0wzs6pcuN5SrZAXe5mvaf4hXehsaC8lBlGN11AdQbAdhGiCnv5fRZeY2sv8yRQHtXraV4nwLUAtcrwL1nQYIni_g70MVMAobpvecypM6w3rf4s6cbMuuFsmAeIrHVPIbXVTNOZUnUS1brhkJgfkje50tyyZ0DiB41YcfmcTjXakLOOZouXBjKs3nEcNa18ziWh8BOxlzBAT081vDmZ3Va4QwmPrz_tzhC5aNDpYBvtmzFp9xEx_a6Pv6UnsBNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
#رسمیییییی
؛ قرارداد اردشیر قلعه‌نویی تا پایان جام‌ملت‌های آسیا تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/Futball180TV/104702" target="_blank">📅 12:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104701">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🇪🇸
صحنه عجیب از کتک‌خوردن خشن هوادار الچه توسط پلیس اسپانیا در بازی اخیر مقابل بارسا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/Futball180TV/104701" target="_blank">📅 12:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104700">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f195b85bac.mp4?token=Q4ruGs19cozHJj5MGExbrh64nQclo3aItXu6r6KBfVQO3HIxsoyaZr35dYKXCAs56um7lIn6b6ZVDenGRUt6eFBps6N03HVLIAZ0leQBZ_PAT7h4Hx-Wuhw3bazpjvyCe3kV1TGQ0RGfaP9wH9_mXv1xWy36J-oOVZYjjCNEcWAgz0nh4S7S8FRryi7u_6FrR91cTyZS3by5u-S8hg6qe7k9ZQEHWFPIC_u1yifemXLbuJNyyjTZkb4LZusrag1yQEbJnmlJHX5XBtg49_qJWXTQ1lVIwBr8PzQBL_x2ClM0j_MWzI3h2CJPfNhY4cvN4Pufuu5VmV3ZojUyTuU7WLhPdBIEUi5IxUkzLlEgaQghIdvH60l5Wszgwwd4Cow2QnBr-4sGx-J0hGBWgUAoyCHTYhenbrFzgSEwJ-x9o94JVQD6LTz9u96yhnosbkttLSMPtNpFUQ3fzPEk27qc2F8QTLyn1tIhswpBDYGRRdBHvvb-1Ze51atApIGAAYMZs3QPdXrdgPhRuy3LjwU6jy5kal1lKyh4bgOzOyn7YL_IsTYFckG_61QBhYHHb1yxwfJTZnHt7a4i4o3CvimceqbWdX-NKJmODbb82qNQNxw56GhCTT6MCljBW0XQAn7Oye39hT767a-dzJkNHrs2NwopbhXrjdOPz7PxGmoPQU0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f195b85bac.mp4?token=Q4ruGs19cozHJj5MGExbrh64nQclo3aItXu6r6KBfVQO3HIxsoyaZr35dYKXCAs56um7lIn6b6ZVDenGRUt6eFBps6N03HVLIAZ0leQBZ_PAT7h4Hx-Wuhw3bazpjvyCe3kV1TGQ0RGfaP9wH9_mXv1xWy36J-oOVZYjjCNEcWAgz0nh4S7S8FRryi7u_6FrR91cTyZS3by5u-S8hg6qe7k9ZQEHWFPIC_u1yifemXLbuJNyyjTZkb4LZusrag1yQEbJnmlJHX5XBtg49_qJWXTQ1lVIwBr8PzQBL_x2ClM0j_MWzI3h2CJPfNhY4cvN4Pufuu5VmV3ZojUyTuU7WLhPdBIEUi5IxUkzLlEgaQghIdvH60l5Wszgwwd4Cow2QnBr-4sGx-J0hGBWgUAoyCHTYhenbrFzgSEwJ-x9o94JVQD6LTz9u96yhnosbkttLSMPtNpFUQ3fzPEk27qc2F8QTLyn1tIhswpBDYGRRdBHvvb-1Ze51atApIGAAYMZs3QPdXrdgPhRuy3LjwU6jy5kal1lKyh4bgOzOyn7YL_IsTYFckG_61QBhYHHb1yxwfJTZnHt7a4i4o3CvimceqbWdX-NKJmODbb82qNQNxw56GhCTT6MCljBW0XQAn7Oye39hT767a-dzJkNHrs2NwopbhXrjdOPz7PxGmoPQU0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
امروز 4 شهریور، روز بزرگداشت نمادین کوروش بزرگه.
🔴
هیچ منبع تاریخی دقیقاً نگفته کوروش بزرگ کی به دنیا اومده، فقط حدود سالش معلومه؛چهارم شهریور رو آدمای امروز، مخصوصاً کسایی که به تاریخ باستان علاقه دارن، به شکل نمادین به اسم تولد کوروش بزرگ گذاشتن
🔴
دلیلش هم اینه که ماه شهریور توی تقویم باستانی نشونه قدرت و فرمانروایی بوده، واسه همین گفتن خب چه روزی بهتر از این واسه کوروش بزرگ
🔴
پس در واقع چهارم شهریور تاریخ واقعی زادروز کوروش بزرگ نیست، بیشتر یه جور روز نمادین و فرهنگی برای بزرگداشت این قهرمان ملی تاریخ ایرانه
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/104700" target="_blank">📅 12:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104699">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTNNN0dJ14e-tIMvdhwwZeWHAo-Q0ogFb5hNxpqc3Dx5DiBmyG5SrwiDvljISbvUgmq4S_0Ip_LuPFpr3NLgWtQPV1VJppPRDWnqXkLCs6IRdEzOgl_9D6528gqvNOqo78YqTJHknbGJG1oeLbbSyxLbOn4Yoo3z2H0gdBAP4ixEeuKa30ALLzfyZJ1SD92_gHEif3lsB0Pm3c9KOgEW7r7tGLzOgfEmxqUMtywmVk0TPHLv1JbZAICQjQQ1KMZ7x6sl9tlhwfOuMjysC-KuGbAQ8Sp62QEUgFFUQakKNQ2nziKHXqFREdpfbJIJuNfLCV9w0BzqjDfCytN60gE7-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رونمایی از توپ‌فصل‌آینده لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/104699" target="_blank">📅 11:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104698">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P50JFLoGv862rZPxklnzgqK5_xuCWsc3hpDseo_raC2xHVwPy3pZ_p0NkZn9frJexi7dBs53TR1sGwQ6TnSYS6X_fHQ5pA_e7YgN9waLc2ilckHsbF85spziZeVNklsXBVbO37xJpN_r0-ZPQD3C-8ndoyQ7_FwQ-QoMSr3qaKFVN3ZHZGC6I67NSDosVDV0OBrv8ZV34bBU3jgSoYP02CF6crCphojWB9-mTSAbEf0GkndvKzk1KLLbMBOdl6kd4Y8c-lRlI_L2Rae3god6DadaywB2wNVJcB8JazRXdINBMvgDNdIoSsY6nnHVY9umHQdthuDpkZmlid2bXxJyNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
منابع خبری اسپانیا: خولیان الوارز با تیم اتلتیکو تمرین نمیکنه
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/104698" target="_blank">📅 11:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104697">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jx2VITk8BX2yM8dTacZa2eZfjqn5aRkhWzNy6r4Aj_IE5YOGwhIW6KYHX8sCpH1NQrzpT8lthehJzmUK-HjymSMecEWyzbegqbIYaPYYze_ltDHVWId2l1sbiszISh2pIColv49v_Mc8oTEnKnU0J-4F2r2SfGlMh_mIRvVd5T2kRCrR5JtAhyCCxfcvN3ERNAu-Szvq-xlQccevJOXNN_KpQal3NU1CA7Wg72odHDoUl9SSLVVCZKyftZOoRutjCaPF627ejvb-Z2XWIMCue6Cju1P3cmJTwK1HnMAXbhQItea0gORjl5aPAyjoSSfs3ZNZSxZ1qsnBoRNTxIbQMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
کنان‌یلدیز ستاره تیم‌ فوتبال یوونتوس بدلیل مصدومیت ۳ ماه از میادین دور خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/104697" target="_blank">📅 11:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104696">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290e961780.mp4?token=IzTDlAhIqBjrBg8u-HEzBIAL_GfuNEW7fO7UbB5WbFxSt8TmKN16QJL_K-HV-WJMSFD13R7Rw5Yy4QPINTDCR1Z4F6XUsH2BVKLNtJP9FyFvP-Q8CRAl3UQEllQU1vvrTrp-OYDmH8CtLVBfslmJmqLiF93dbY30j7yP5_ortnk6TBGn8JM3h4KKa8h98_4xZnC7gzNwcSpVkqTqAHgWaex5UaC2AquIJ9w5Pd27ItszTZrnURlye2O0kcLjzr_89DBsVEqfvsAkD7v0gJHP96n279j-nkQiJK-we_VrvN4xMiIqvoFZxx-aM0SwnLUXrmsiTzMZyCm9suM5m_d7zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290e961780.mp4?token=IzTDlAhIqBjrBg8u-HEzBIAL_GfuNEW7fO7UbB5WbFxSt8TmKN16QJL_K-HV-WJMSFD13R7Rw5Yy4QPINTDCR1Z4F6XUsH2BVKLNtJP9FyFvP-Q8CRAl3UQEllQU1vvrTrp-OYDmH8CtLVBfslmJmqLiF93dbY30j7yP5_ortnk6TBGn8JM3h4KKa8h98_4xZnC7gzNwcSpVkqTqAHgWaex5UaC2AquIJ9w5Pd27ItszTZrnURlye2O0kcLjzr_89DBsVEqfvsAkD7v0gJHP96n279j-nkQiJK-we_VrvN4xMiIqvoFZxx-aM0SwnLUXrmsiTzMZyCm9suM5m_d7zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚠️
تفاوت آزادی بیان در ایران و استرالیا‌ از زبان اسطوره داوری دنیا علیرضا فغانی
وقتی مجری از او درباره فیلترینگ فوتبال ۳۶۰ به‌دلیل انتقاد سؤال می‌کند، پاسخ علیرضا فغانی شنیدنی است.⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/104696" target="_blank">📅 11:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104695">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/104695" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/Futball180TV/104695" target="_blank">📅 11:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104694">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gl4FUyyLAbA3PaQ84IJGkzPL_phsCJ47hM1I5FWqf3fcuv18ITPve9bGYo3qOVDaCNKcPSabiAZdLQutG_7b6q_LmO6d6Fafdo59nix8lBHIbrxeXvzi1-RcOT2o_vcpwxHBicuS2Zza3Cy7o8wd7MWTj-F9A9WD1Wb0HhtqwBfXt8NPZvYMrenLs4TG6YIxdFNUG5e5Qy0lnfRa9Tw-04_VpKJ-YAcEOSjWTxVFMS2Um4iNoIZ0dF_Hs-PFZ3xUr6fUkG3xdosS20lZXQU8blepC_PSBbRRSjUy7EPLbpcB5xemtDpUeJ9aAIEZweqWsod3WvtjMbdVco4G6BS4xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r4
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/Futball180TV/104694" target="_blank">📅 11:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104693">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb7772379.mp4?token=bHdPmFMrNlPYsnEKIo1np5obuog1Xah9D_A9zpfezBtIqhiUA1N2Y2ZdN0aO9LTVE4G5wYcOvUA8bNSgOFNcqIgcG6-m6KAS4Iyb2aqCEH5Kni_Ehd2SlYDUHNFNfXKFHz-JJusrfdVSeywf2WOMaceKiLRNNKaWUdZ9Lizkt-wzrXHwQzb4S96vieXg_RbMZ5-XD4lAi9gsc0HPs2gLGM9w1krTg8ODxO5d-VvoTZrC_jkoSCUExcPdRczqXNc7Rtkv2m8dDp-_1IUEj6gon67GUi4bFEXyNlxhl1Pb4p_C-haid7tvOVRbgIZWV3oS5sk83pbtDLT34Qh7ZyRw0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb7772379.mp4?token=bHdPmFMrNlPYsnEKIo1np5obuog1Xah9D_A9zpfezBtIqhiUA1N2Y2ZdN0aO9LTVE4G5wYcOvUA8bNSgOFNcqIgcG6-m6KAS4Iyb2aqCEH5Kni_Ehd2SlYDUHNFNfXKFHz-JJusrfdVSeywf2WOMaceKiLRNNKaWUdZ9Lizkt-wzrXHwQzb4S96vieXg_RbMZ5-XD4lAi9gsc0HPs2gLGM9w1krTg8ODxO5d-VvoTZrC_jkoSCUExcPdRczqXNc7Rtkv2m8dDp-_1IUEj6gon67GUi4bFEXyNlxhl1Pb4p_C-haid7tvOVRbgIZWV3oS5sk83pbtDLT34Qh7ZyRw0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ژاوی هرناندز در اولین کنفرانس مطبوعاتی به عنوان سرمربی تیم ملی هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/104693" target="_blank">📅 11:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104692">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fdf3f04ed.mp4?token=W9tJWbzZjs_OsA_Bg-ymNVki6dmdl2_Aem1jFdak8GRplFp8r8EykEUhSoHT5AO9roaSCHo4zo9sJ-PB9pXdiUWld30RJc157Fw5_NC-AGp16hMAfOFOO0xi5cQMP8D21b50mkZfgVH8SsDPHRvYwvhHuyft6p65pctr7cfqsdxjgEArahwM0hja8k6XzoIFpKpj4-CoOyxbYDMnp_HNiK80FVvPzXUEU2mM5q2lWx8xaLegJbnCS21eZ1IM-gqEEb0BF2oMAjzhxKuUAjG-Z9rzYollowHPC7pXoq5l9jL43aFlH70p84EGGcgcV2A5DRq8eJ33C-hKhPjmmPpAQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fdf3f04ed.mp4?token=W9tJWbzZjs_OsA_Bg-ymNVki6dmdl2_Aem1jFdak8GRplFp8r8EykEUhSoHT5AO9roaSCHo4zo9sJ-PB9pXdiUWld30RJc157Fw5_NC-AGp16hMAfOFOO0xi5cQMP8D21b50mkZfgVH8SsDPHRvYwvhHuyft6p65pctr7cfqsdxjgEArahwM0hja8k6XzoIFpKpj4-CoOyxbYDMnp_HNiK80FVvPzXUEU2mM5q2lWx8xaLegJbnCS21eZ1IM-gqEEb0BF2oMAjzhxKuUAjG-Z9rzYollowHPC7pXoq5l9jL43aFlH70p84EGGcgcV2A5DRq8eJ33C-hKhPjmmPpAQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلنگر و صحبت های جالب انریکه درباره رفتارهای دمبله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/104692" target="_blank">📅 10:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104691">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mboyftFkAB2MmapyYujar8KYgt9Q5au2acjqE2eUjlK5QaytAkLgHhLG7bmR1OVioSagR1Irwi_WoEROWVXDm2BWwLezWjkkwRXpucO1WTm82B8Uz28eWhHTyPklEphzJW7zXq7eQylu-ly_TkA_ejUP17IBsrdOsSfiUs6jUHGmZt6hYOpvbDyc7QumE1Ituj7i6Pi7LDQDcd9LWC3FK7xDPsXJyvtyk6at5pi96mV88zlHeyIgrxpnKQUewzbH6YyDh7Zluji41_Z4QXk483JYxB0fKdhdC5slPO7cOFwG0e7YkKIim1QJwpYiK9uSOC-Vo1t732DPyLeDGwJMhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
اعلام اسامی داوران هفته چهارم لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/104691" target="_blank">📅 10:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104690">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521128dbfe.mp4?token=H1B4H4s2lUHJXgD1I2REBC1DHf-DfIbnAsWLNbmXkyWjkoNZdhibx7AMvBqy_jwxJECjJEXzmwx0Ez6ZcEdMeCLDqIhZPJM2FVanjNjsUWGhUPj95eEHUpMKHHcj95OU_2SHgISe6wa2qr43ohK6KNUFGbe09Qor_nN5k6wqo44eUFrhksltsG9McFZewJkhwUrfj6j_9xmW5ThspahLlH0m_ieInsvq2FIARXNMiw5aSulj91GJaJBCKmYkyW49K0aauGIVvWM7KFkmwn-E1rv-la4BFh9FtkWdLpFjlPiXpOOLdtK4thZzK3fx_oXCHDNbDZvCL3895j5aHiSE1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521128dbfe.mp4?token=H1B4H4s2lUHJXgD1I2REBC1DHf-DfIbnAsWLNbmXkyWjkoNZdhibx7AMvBqy_jwxJECjJEXzmwx0Ez6ZcEdMeCLDqIhZPJM2FVanjNjsUWGhUPj95eEHUpMKHHcj95OU_2SHgISe6wa2qr43ohK6KNUFGbe09Qor_nN5k6wqo44eUFrhksltsG9McFZewJkhwUrfj6j_9xmW5ThspahLlH0m_ieInsvq2FIARXNMiw5aSulj91GJaJBCKmYkyW49K0aauGIVvWM7KFkmwn-E1rv-la4BFh9FtkWdLpFjlPiXpOOLdtK4thZzK3fx_oXCHDNbDZvCL3895j5aHiSE1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حشمت مهاجرانی سرمربی تاریخ‌ساز فوتبال ایران، به ثمر رسیدن اولین گل تاریخ ایران در جام‌‌های جهانی رو با روشن کردن یه سیگار جشن گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/104690" target="_blank">📅 09:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104689">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWIhflvYA5_rhy7tMYndxuTivw8uPZomPUEHI8NEgxJgduw160k_bSUAh381X988V0Zifn7GcFZpFDM9ge7LZiHRLEp6KrAJELMuLK3AHxxPL2-94OVIHwzmaFwTqU2qGlMMbA0exlsvNfqZoVySOaAhWueO6t5bgH81qVUQlsE5eMd_QiCuuUk9ATOHoA9k5dYaF7BY8zBKEhH0DGr1pjF7Nf_LZd4Fl8WdXW-j9hsv_T69v9z4ohlCUOrc9oan2nV8soCYoquZGxke4kw_CDx21cmL49q3gj3HBKxGEtUIZeVXda70NmofgRzR6C6rcVKEBtXXJY2Fwfh-Gcuzvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
📊
محمد صلاح در دوران فوتبالش در تمامی ۹۰ دقیقه مسابقات گلزنی کرده بجز در دقیقه ۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/104689" target="_blank">📅 09:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104688">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fdb56b243.mp4?token=uHCHEryLMTVwhx2iQ6SQH2ABSJlvzi2IQrAuTlmD0kEn__2ZpKq3y4w0loUKnm7EhrX-8Lr1X5xliKINf-0nIvBkb8eXXFmILiTqXZAEAFLASBmhXlOW5EgduELUv1w9srnNx2JCJfBngD1DseCFlWviO-wGiDA5OYPlF4SY6-SxUuMTmMCtStvvEaDxVqzCkA90ePM0EYuH5ApYrsOvtlWCPNxiAatRYd-MP6DjAmDAoSvULcq118IPD3YcpIlEB37dN_M5O5zIDaiCQjcOVqcnwWn6aaeW6x16y2GUIQEMU4_HUNIk212pJUcK6ueGnAbKVOAZcQvtpCN7qcJYkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fdb56b243.mp4?token=uHCHEryLMTVwhx2iQ6SQH2ABSJlvzi2IQrAuTlmD0kEn__2ZpKq3y4w0loUKnm7EhrX-8Lr1X5xliKINf-0nIvBkb8eXXFmILiTqXZAEAFLASBmhXlOW5EgduELUv1w9srnNx2JCJfBngD1DseCFlWviO-wGiDA5OYPlF4SY6-SxUuMTmMCtStvvEaDxVqzCkA90ePM0EYuH5ApYrsOvtlWCPNxiAatRYd-MP6DjAmDAoSvULcq118IPD3YcpIlEB37dN_M5O5zIDaiCQjcOVqcnwWn6aaeW6x16y2GUIQEMU4_HUNIk212pJUcK6ueGnAbKVOAZcQvtpCN7qcJYkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‏
✅
نخستین تیزر رسمی از سریال مرد سه هزار چهره به کارگردانی مهران مدیری منتشر شد. این سریال بزودی از شبکه‌سه پخش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/104688" target="_blank">📅 09:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104687">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKgWpSE4CiGeAyNx7d-j9L6ZCO3tgvJjZrbBrQW3nxaMvYUti7GNjCq1gg1RWDvqWCJxD7A_H1rmcuMVtDxmxz7E7rnz48bsq6z8wD18Y3r_dCG93tM_A3Nm6jswKglcCuVQXLmZ78VpzUlW1YZXexaT-Yta_pdmykU4FDbLnx8n650x1ZOdJ4IJ_zNPhnhHbdNlI9lZ6xBGB5s2JTCxf9eBchzJJRQuNsadvZpgf-nffB7Y6hekVLEB2w7t8vANluYNl9-IYvxbGCG6VXeXp0V-q4VVC6MilwD8ovMIwb9ErtBh-4ZwyXRcgn1KPaEI9F0oWv0stt82jvjyz-oUFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق‌گفته برخی منابع خبری، باشگاه منچستریونایتد قصد داره در ساعات پایانی نقل‌وانتقالات برای جذب کاماوینگا از رئال رقم ۵۰ میلیون یورو پیشنهاد بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/104687" target="_blank">📅 02:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104686">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/strj968iBg21O0GxBSf7vUAmtUd229hKj872xWTv7fSYyyt-gAnHn2aGXZZ9psCl4Ao_fgTDiQedZVQbi3BY_dg4MmhVLg4AleULEyUYhyu6VFZj0tS5_qQtXG1cMG-uT2ZEmb4JDYxyaQkwP_yGtbPTAI14Uhy3RdsQujv_9vkEqvP5G1Q2Su2yN-2OhO3trzP6lCwudpdme96S5aQNcnNq_N3B6NnAL-AD7cr3pUns7lnYJwZwsuDEUwXXbq2iCYgko41OOlaJTatrAim_a7k2G9rk519I4xQkbv8RPKsVzUoKdCedKUJDm6Nwth_UUQ7_yBrBHcMYlGaNrnH8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇦🇹
تیم‌لاسک‌اتریش که در بازی رفت سه بر صفر از سلتیک‌ باخته‌بود، امشب تو یه کامبک سوپر تونست ۵ بر ۱ برنده بشه و در مجموع به مرحله گروهی لیگ‌قهرمانان اروپا صعود کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104686" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104685">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Llml9zT4zGGHkVQfaOCq8GBZ9AE5xZkSZ5o4fQCRWR07zqzPNCuS1BJ-edtL-4TrUGai1E09pXs62z5YbxpN5ozLoZc3jsxcUdzDYM6LTtsSa7zWeKOGExbW5ue5wzBjjpS_T2bhMWRwNO6py3lJBD8TbA9LReuIIn7VkjRebDHkpWF3YqGDCZxJPFhvXe66-KO8-QLMzTtV0oq3S5hm-zPtPOB7aBdkhlA2Ok18XRzMZul71-lU1RhIKeJihIMPXlrUnC8CXowJ6HZmInqhCb1gICYtPzndIxdUwqRnjTntgu94-ekcQeolTyWJLMRGSjBT7kmYXhkZGbkTntguKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارسلونا ۱۵۰ میلیون یورو دست به نقد ایستاده که آلوارز رو بگیره بعد خیل‌مارین مادرقحبه نمیذاره آلوارز جدا بشه. حالا اتلتیکو باید بمونه و یه تیم ناقص و‌ آلوارزی که دروازه‌خالی هم احتمالا به زور براشون گل بزنه
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104685" target="_blank">📅 01:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104684">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXSwaOcJiQtnU66KGfMoyr4VkeSXOxY8aUV1chUGawF7jk0TLArwtF2wgxIWM7wKoFLI4tG_0I84uRowmy74VnfW6VhjjGDTWasfWt3dEBAOnUhiIFJz6bk1l69_Fu9TtojMLNgD7gLWNjJL5C5YFz2NmvyQKI-IabaFy68F46HVBLH0UzjvoqZiaXTKUGHD2Xlm-M0sHSMeF_X-etQ5qPCun0AB4ITDDVOg3z3Z3n5LbEetCmuCpVvNeJaRZ2G62XeXwD3c-xmbrWc06OQ40kTIBdS_Yovb4wb8VmIAYfoZXxtpfTSoqFIJ5ffr_U8k4uhIWrWemW0Q_imuJiHSNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇳🇴
باشگاه بودو گلیمت نروژ با برتری قاطع مقابل حریفش راهی دور گروهی UCL شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104684" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104683">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBGpwAf8Q3oCenKdjEpz00ym0uVLdwFstIeTxEqf1fkdHVEHOaXeZEbbR9CYjHqTmBViA8rCIPNOnRkFyMDxq7elfmrBbAlelSHDm6ToZCqhUVQ5kAekqryM1debpyEvmGlfe6iLejBXo9LOPqPQ8StGsa_Lux-qcJWm2basWTfm2iLi2capMZB4LyX1WL_SotmfRxCI93GgfSCoNwTXMoeF090OA6gOv6cCQEMTQgYFs4CPm82_2rfp6DIGm9A0sZV89wqYGi46SXHgssU68XRk58N9gjZ3zr2g4HmF4WDC77a9fMze56UCCdr9Iyz-TkNz2tXYk3dhaduuSCvZvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
✍️
اتلتیکو مادرید نتوانست با تیجانی ریندرز قرارداد ببندد، زیرا شرایط مالی دشواری در این باشگاه وجود داشت.  ‏
🎙
پدر تیجانی ریندرز:
🔻
‏"ما امیدوار بودیم که با اتلتیکو مادرید همکاری کنیم و دو پیشنهاد باشگاه القادسیه را رد کردیم. آن‌ها بسیار علاقه‌مند بودند،…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104683" target="_blank">📅 00:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104681">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NC5JZ3tHZkCcZrERv-PctH5AIztWlgLUryv4Y--HvWtKa_fndzYH73Rg2tYmRfaeeKsxBXQMhFNQtixF4Wux_fD8p20ZCJNtNABUhoRg_HkE56521TcefX-WMTsUXWfEVJYotOP-W2XT7NZPChX2ax5DNbmdF7pR6FTrst02WUgr6hb1VQ78o4tmh2MZsi_y4jFRsKsfcvgJHqZz4Brw86-dWUxuY221FWWBZfOzFlWdzLLlXQt2EBdAp-Xdx8LUcKJRlIVaLzUl6DMeTSJd7bshycMJZIAajcTc0x2NiMv1qpus6l0z9jsrpKJyhH1LaobtaRYcmPT8r5xn7QkeLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇸🇦
رومانو: اولی واتکینز قطعا از تیم استون‌ویلا به الهلال خواهد پیوست و مارتینلی هم بعد جدایی قریب‌الوقوع از آرسنال در یک قدمی حضور در تیم اینزاگی قرار داره
!
گمونم خدا به تیم‌های ایرانی اساسی حال داده که قرار نیست با الهلال فعلا بازی کنن
😢
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104681" target="_blank">📅 00:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104680">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i02N9uwU5fnfB16qogmhiAUElHC5lqYS_3__W6d3LlnzNvCLlyvmfAMyvVExF5zyW31M5LsapDlpGIV4fl2pLcMI-3T02eqeDsyI0OXzMIsuxWtES_ljcHPipGzxcPkld_sLu6Bn7v8TXLnoj9CFJvaCMNwBbtiEIgCehCgio-tbY6IETNsVcnlw7t5qwsrLIeI_T0abj0XFjfLXMX88d_o6A_-z8xiXMO6AIF9Yc0eaaBuWCsEK6xWlwEgWoDhp-Fa8k9PtOLcNQNUlOe-fxMQqpGAQYQQlQjxCeZpvQs7qw9ziS_PfVUtz1X7hIcUAiRJOqBxSV-v0ngzN_cK-nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
✍️
اتلتیکو مادرید نتوانست با تیجانی ریندرز قرارداد ببندد، زیرا شرایط مالی دشواری در این باشگاه وجود داشت.
‏
🎙
پدر تیجانی ریندرز:
🔻
‏"ما امیدوار بودیم که با اتلتیکو مادرید همکاری کنیم و دو پیشنهاد باشگاه القادسیه را رد کردیم. آن‌ها بسیار علاقه‌مند بودند، اما در نهایت به دلیل مشکلات مالی، از این معامله منصرف شدند."
🔻
‏ما بلافاصله دو پیشنهاد از باشگاه القادسیه را رد کردیم. تیجانی هیچ تمایلی به انتقال به خاورمیانه نداشت.
🔻
‏آن‌ها برای بار سوم دوباره تماس گرفتند و پیشنهادی را از طریق تماس تصویری ارائه دادند. سپس، ما برای بررسی این موضوع به آنجا رفتیم. آن‌ها به دنبال این هستند که بزرگترین و بهترین باشگاه در آسیا شوند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104680" target="_blank">📅 00:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104679">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/104679" target="_blank">📅 00:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104678">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=mj4HVYt6Ra8-pbF21Fefb8BtKhoBnv3R_cZ6YJ7qsF275mkhC-YOif69uQRTwYfnwWmIyCev8wjG5kXITuEGXit0ZcFdJvgx3SJQZblbSY8v42-fe3djcuIhGD7nSmSIWA6Q6nm7BSloD6YCpcqqFItdpMDLTFuZ5LpgCHUN6j6M6cGb0FZEE7nI78jW999ygs0a1nc1Y4jVvzTwOuHfVg_dQR0jw3hrAojLGEOKW-tBuCgKuGcFqmTc43FhG63U_nrZFIPKZzBdvauXBrKsaCxvUl7fPZ9lh315CPSudn_22sNjkkL9pkkt1i7EKVg663tgzi86fXIN8YL3hFSJ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=mj4HVYt6Ra8-pbF21Fefb8BtKhoBnv3R_cZ6YJ7qsF275mkhC-YOif69uQRTwYfnwWmIyCev8wjG5kXITuEGXit0ZcFdJvgx3SJQZblbSY8v42-fe3djcuIhGD7nSmSIWA6Q6nm7BSloD6YCpcqqFItdpMDLTFuZ5LpgCHUN6j6M6cGb0FZEE7nI78jW999ygs0a1nc1Y4jVvzTwOuHfVg_dQR0jw3hrAojLGEOKW-tBuCgKuGcFqmTc43FhG63U_nrZFIPKZzBdvauXBrKsaCxvUl7fPZ9lh315CPSudn_22sNjkkL9pkkt1i7EKVg663tgzi86fXIN8YL3hFSJ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a3
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104678" target="_blank">📅 00:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104677">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🏆
باشگاه صباح آذربایجان برای اولین بار در تاریخ خود، به لیگ قهرمانان اروپا فصل 2026/27 صعود کرد. این باشگاه آذربایجانی در سال 2017 تأسیس شد و کم‌قدمت ترین باشگاهی است که در لیگ قهرمانان شرکت می‌کند، با عمر کمتر از 10 سال.
🇦🇿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/104677" target="_blank">📅 00:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104676">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvpSOlBJSGInGCbb7B6Kva3hgijoTaK8C7kOfvZa62QKMS-bdG__2i0KaX2jGYH_QYFSKQBJWwf7QlQaYVrtmVMtc6eHiMuspH0Z3WD5rwRs0JxDWKuOYSVL4hu6QmmFs7br5cJfDCMXyhbX4TR0K6VGKxZxfLE9qwlPJ1nRzNePw0V7uSh-S2oDoBLwFm6WiWohSG7fwRno3ZgODIicdgjA6KPBNZGX-81Ab0xAoWzTxWlnMpcHGkRNSRerYswutqRmlAHD1eoz7hT3iWGNZqVJoSW9BIHP0jo3hZ6gR6uaQXBCGBCUTCHyJjLB6tlPFwTnJv3feepVtXKmZRvfFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
باشگاه صباح آذربایجان برای اولین بار در تاریخ خود، به لیگ قهرمانان اروپا فصل 2026/27 صعود کرد. این باشگاه آذربایجانی در سال 2017 تأسیس شد و کم‌قدمت ترین باشگاهی است که در لیگ قهرمانان شرکت می‌کند، با عمر کمتر از 10 سال.
🇦🇿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104676" target="_blank">📅 23:56 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104675">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmXtvoZQtIlHgorfkRcogJ5LIbcixsuwNelS2nuUJi1jQqwriFjgu1D8aPoUQBfFoal1nm_e7rQzkLhtuh8-gOXdjTvIlSEDz--EKpnKM1qOAKZQk68IoVV28qSOBm7kLGRd_ZzphUDCdNDJnaY4N8F5DXD3grH5ZKqcxFZ_7qLxBNfoaQ4hQ0oHlWUQc3MsOu1M1-2QZu9uprILqnvlT6j0FY8bNN91q2LXYzveNLetlolwTiHyLCR06K0iOKZ8Uw5aH93FTN37aqIMZGU9M5MOfmo8U0YdbEXx8tsE0eLSq2-cO4Puzetwdwn2R6Cz-3o1SfSE5eIwX-Dpp8WdNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚑
🇮🇷
#فوووووری؛ اوستون اورونوف در بازی امروز دوستانه پرسپولیس مصدوم شده و تا فردا وضعیت دوری احتمالی‌ش مشخص خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/104675" target="_blank">📅 23:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104674">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41704fa8fe.mp4?token=mHHHDv2Iq8Nbqdk3s_cvvKYpZBUcU48MLZ0aloefqjsdhEWmEbSqSGAh3py6Xxk5NoA6b-WacnMSt_xAm3ZuS325XDmGkA1dF3SAjajtX127dgbciyLE-dnR-riWKVALCQrTkTsqlb08d-Ke7kCSqKhXcf2wWccOIqy80eCPvJZRoSAVrQR1FsC3oHq3kR0QscnP_B-22WqCVjKT9NVciq2NSbg4t2HXzb_28U5zb3l7uY7JEuH17bCfEXa0bQPWFNVAX7DM9hXYz616Y7ifAqTPLNJxL3fhTTvx27HCYyIlMKVk3QAYyaqbv90Jp56q4iLu9J6iH9OCZHAcJiDsNW0gF4pla3hw9LOFXBu7xJmF38hT6Yfv9ONGfSW4f_xIjp2TlBej9ME41GgY7fabB3IbpGUib860623XEEqTuVofDSxkyjfSMOOjnICXZGu8-z3_rBpcqEYeDQ1g9P4z_SJ_3kShQQtfe924jd9vkt-XsoA_tlLrmQjJ-66VOLo__1YZDQSxrYMUVwAFHKVMvHo0e7n9Vk48CCO2rZpP7eE0kYKaMDvfpvk9v_bSPA5KrDNBD8xRtp0P2RJbcZrJd2NemdhRicTVouoklPO1DJWxySUYHYqEffZI0wkA_i329cvTHbxXhNjsh1kW1jq4B5cJjXhEszEalkXl2612jo0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41704fa8fe.mp4?token=mHHHDv2Iq8Nbqdk3s_cvvKYpZBUcU48MLZ0aloefqjsdhEWmEbSqSGAh3py6Xxk5NoA6b-WacnMSt_xAm3ZuS325XDmGkA1dF3SAjajtX127dgbciyLE-dnR-riWKVALCQrTkTsqlb08d-Ke7kCSqKhXcf2wWccOIqy80eCPvJZRoSAVrQR1FsC3oHq3kR0QscnP_B-22WqCVjKT9NVciq2NSbg4t2HXzb_28U5zb3l7uY7JEuH17bCfEXa0bQPWFNVAX7DM9hXYz616Y7ifAqTPLNJxL3fhTTvx27HCYyIlMKVk3QAYyaqbv90Jp56q4iLu9J6iH9OCZHAcJiDsNW0gF4pla3hw9LOFXBu7xJmF38hT6Yfv9ONGfSW4f_xIjp2TlBej9ME41GgY7fabB3IbpGUib860623XEEqTuVofDSxkyjfSMOOjnICXZGu8-z3_rBpcqEYeDQ1g9P4z_SJ_3kShQQtfe924jd9vkt-XsoA_tlLrmQjJ-66VOLo__1YZDQSxrYMUVwAFHKVMvHo0e7n9Vk48CCO2rZpP7eE0kYKaMDvfpvk9v_bSPA5KrDNBD8xRtp0P2RJbcZrJd2NemdhRicTVouoklPO1DJWxySUYHYqEffZI0wkA_i329cvTHbxXhNjsh1kW1jq4B5cJjXhEszEalkXl2612jo0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
ویدیو وایرال شده از دعوای خیابونی عجیب در گیلان که یک مرد در دفاع از همسرش دست به کتک‌زدن دوتا خانم دیگه زده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104674" target="_blank">📅 23:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104672">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPgKD_YPWxZfT0mHKEOQbBtlL7gIB3nwZ7NY66BOO0HXHSHMMJGh8dZVerODTxGDc0gkk6JA5blXqyizRARN3WboHaFJFBAJ8G6Mx8cRqplsMY2-1yoBhQ803B1_sCu9YWKUW5mK1jUTho6YPOgLJwd9PxzzexEIMvvuf21MIONExeN0rmtUorOY4KfSheHJwzE3mxiB8R6IE6OziSFvcGEprUl_dRX4MMWir_mZyyiotwno1BmB2Bmb0J2HwsbG0dGJolWHPTOw-xXg9LY5YCdT2pO_RO4a1w9RNM4o8Zb3skCj612OM8pKb6X-OKz2ucni2FulOS5S-n82UZ76qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برونو فرناندز، برنده جایزه بهترین بازیکن لیگ انگلیس برای فصل 2025/26، بر اساس رای اتحادیه بازیکنان حرفه‌ای.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/104672" target="_blank">📅 23:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104671">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-IUV-zrkjXx5vD8hvZSHru7u9cWzR0LM8i3pAnJrDSLUQekq9wDFIbv3xEp7frVVjX8nY8BZ785AY9foc4N8JgspgEVs49GKN1pvZGeMhrpzUyK1yOsuMl8fIAUq4aseoKoeLNssBifcXaYUFEwjTTHyeje0geVGZ7ZRNObzhx2UiNwEmxTY20_5uU-I0EWmW8X7m5vosZULQAm4PEaFZ1CjAH8DzFGeM5LX-Nc7wiLBcHp-0FlGg-Us9FqP9K5TSWrjWjbRBkMxR3UkowM82TJUoc_r7Xh5BmN30MnFjI8ozR87Jyi5Y_y_eI3IgycpzmhbZAzetbh2_mFiGINEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب منتخب فصل‌گذشته پریمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104671" target="_blank">📅 22:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104670">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/090cee5ae0.mp4?token=YajBG8Kk2tx5k__VNbu_9kNM7EyTVKFRIaW5Kjl-wdn6npz-BFnecjw2uO-_L5KV2ec5oeg0emcnA-11sMy_q9gw_nZEzAKam2txNK1Mj_m-zODKGRf8EgS2VSiGAK44BXqgmGmsLzm19HYstowC0LMGmi9xfd38z1YE0IvUDMZxm4h0w1ScDy8Cp-F92PGPTYw6ERiCqeFykqPZ6ZxRFaxlam8WtYHMo3mSedLY8_axbUMiJJeLNrUnlTlEN8DBzaSzRGEAnJ4UJ4LU1Sv9hI8720tzJLByJwB-drYkMa6jngaRTiVbzdhawtdminKkD7qYiZU7fdm9pDGfBXDjxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/090cee5ae0.mp4?token=YajBG8Kk2tx5k__VNbu_9kNM7EyTVKFRIaW5Kjl-wdn6npz-BFnecjw2uO-_L5KV2ec5oeg0emcnA-11sMy_q9gw_nZEzAKam2txNK1Mj_m-zODKGRf8EgS2VSiGAK44BXqgmGmsLzm19HYstowC0LMGmi9xfd38z1YE0IvUDMZxm4h0w1ScDy8Cp-F92PGPTYw6ERiCqeFykqPZ6ZxRFaxlam8WtYHMo3mSedLY8_axbUMiJJeLNrUnlTlEN8DBzaSzRGEAnJ4UJ4LU1Sv9hI8720tzJLByJwB-drYkMa6jngaRTiVbzdhawtdminKkD7qYiZU7fdm9pDGfBXDjxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🎙
سخنگوی دولت پزشکیان: احتمالا قیمت آزاد بنزین به حوالی ۱۰ هزار تومان میرسه و ارقام بالایی که مطرح شده صحت نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/104670" target="_blank">📅 22:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104669">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkIdq8kzk-yR94lC_aw0MGvGB07lXsOx7T-ZTpQUCvx0P33CQ-AQJk537CLMVCTlwxIh9McVVmAYE_M9SVypo0vv5dqjPpo5RBymO-BUgdtfum7xdwxMN5m8X_adPCpFv7Wz9ry0nvDbDwreYpMZY6-IOTsDHYkQYUM04qMOie8lBiqebGCeo-eQvsna4rkE8IU3_Tgl-37BfHfM8bqfFmPsv0QRpo-ZmrDZ8onBC5KVO5pt5YSbldJL-3AFwxpyFmHdurFQaKflZrMu_EYntZjBCzusq9DdDTGAtivoIu155o93vkbFveWzoSPWaaikRPvHPQ8foGDuIH18Javs2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گستون‌ایدول خبرنگار مطرح آرژانتین: مذاکرات سیتی و چلسی درباره انزو فرناندز آغاز شده. ژابی‌آلونسو در جریان این انتقال هست و در صورت توافق مشکلی با جدایی این بازیکن نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/104669" target="_blank">📅 22:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104668">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2063216dff.mp4?token=qPn1YJbN8kBir1t-AZj07fMdBh4BxNWr7zNJmupolQ0ZP_KbtHSqqNlt3v3J78EuMT_CCrZUoWmJVn-dYpNSkRl4U1rF1ik5cZZiN970bVHdItwrVC7ae-QXEANMkEmXALPh_FttsP1FNK9h-4n8LIuNMf5J_fHiO9pDdRg5y3xf9rDdzkN_eo8q2xETGedP-oiXOO1hPPgfVuW6jWjF5Uodk0QFqWKyju-coFQFdVepxKzCdEAbmJqPTFKgm5eGz0fAmRHEeu_KvZJOvltN7VbdU8lrMD_kN3qln3-kINhTUskcbkYvjcYqzeyUGvt0d1WIHUlBCUkCK_BR-txmzodiaJbl6V_-2hgYtC4cPiK07NBreZ3c2K21Uq1IZOZoXJ88qJVa9fGn4Acb87GoAXELhFRzlJCbB5Krq79BeP1-iSoVY-AqanPCG50qaVw8D_M7FHrfvfbxX0BI-66KlE3dUhtJX6j3FgV4_3Hp0sy69VAPE2iw0A9l0-3ArPQy1AU3N_yqKDfbUlZ67oE802T1FZeYBb5eBXjsUT3JFE2Ja0sJ9egtWbTy6zEu68NlcbxerWlw10jI5A1adoWmF4EIDSfjYEv5b65dXUyzbaOUUO7quunFaRyKytg4RQW5aDh60UHF1eGesjnEKkRXib4--tqatAHQAB2ytan_KN4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2063216dff.mp4?token=qPn1YJbN8kBir1t-AZj07fMdBh4BxNWr7zNJmupolQ0ZP_KbtHSqqNlt3v3J78EuMT_CCrZUoWmJVn-dYpNSkRl4U1rF1ik5cZZiN970bVHdItwrVC7ae-QXEANMkEmXALPh_FttsP1FNK9h-4n8LIuNMf5J_fHiO9pDdRg5y3xf9rDdzkN_eo8q2xETGedP-oiXOO1hPPgfVuW6jWjF5Uodk0QFqWKyju-coFQFdVepxKzCdEAbmJqPTFKgm5eGz0fAmRHEeu_KvZJOvltN7VbdU8lrMD_kN3qln3-kINhTUskcbkYvjcYqzeyUGvt0d1WIHUlBCUkCK_BR-txmzodiaJbl6V_-2hgYtC4cPiK07NBreZ3c2K21Uq1IZOZoXJ88qJVa9fGn4Acb87GoAXELhFRzlJCbB5Krq79BeP1-iSoVY-AqanPCG50qaVw8D_M7FHrfvfbxX0BI-66KlE3dUhtJX6j3FgV4_3Hp0sy69VAPE2iw0A9l0-3ArPQy1AU3N_yqKDfbUlZ67oE802T1FZeYBb5eBXjsUT3JFE2Ja0sJ9egtWbTy6zEu68NlcbxerWlw10jI5A1adoWmF4EIDSfjYEv5b65dXUyzbaOUUO7quunFaRyKytg4RQW5aDh60UHF1eGesjnEKkRXib4--tqatAHQAB2ytan_KN4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🥶
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتیاس‌یاسله بعد ترک عربستان و بازگشت به اروپا؛ عجب حرارت و شوقی داره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104668" target="_blank">📅 22:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104667">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufPKx0pe1tfloX-9rHpZaajypWye5GvHifwFDytHw2Twvgmle-jHBfqHSdBtcPgLuSVCD_mEKtw7c7mMS4TgdNv5wfmmT5sldlNXcjtjhlZeKHV6dZxVwHKmfSRuXkZ4b9uIKTvNr1vAcgCwmJQiRTSfVUDYo9u58uFgF96-L3x1fdvoBmkMCuaA75_7iBZ5CGa-yWfFz2wSe8kfmiCoREb-cny_2iDuMTAbO0NwGmd1pXfNHD9i2lf-ZDgJNoP4Xafs47XwX_ygvb8OrLbraev-QhV2uNZw28IYmPD59pI1HuMjW5PjQl9bQBeYmXzrLzmnt1chBc5e4D4gXngKHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نیکو اورایلی جایزه بهترین بازیکن جوان لیگ برتر انگلیس را برای فصل 2025/26 از آن خود کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104667" target="_blank">📅 21:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104666">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INxxEOueIh2wigXmARUWgXzaXDw114aFaS2iyyJ8F521lM1Fv49h3F9mT2FukEJeZfAv_W7FcrbbyLq2iTqcpS7r54Hg-mcwDYjgTAui5ySv_YPBcQiF6WG_A7QtHGhgFOrv2bx9VpiTG1CSQtbHIy_twLmD7xQ076beMtiLxwOXaPgpOtSamYLFDVyIRif93Fce1gTN6sdmcsYVTY-Qvhh-gz9hQIRquJYfDrsA3eNxIj0N-TnUZbqCVWT-MeuTth36xx3MaLIW773TJdlrqBgvNFZIsk57WIf3jiClqu9GedA32pHtWr751WTNAzg5pvPyDPm7JmWIMBTmU1P2rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته اول لالیگا اسپانیا
🇪🇸
والنسیا
🆚
رئال بتیس
🇪🇸
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۲۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104666" target="_blank">📅 21:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104665">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccff2e7a05.mp4?token=Fkd7m3x14qTWNX5TqdWy_pjfFZlH_ycLDOsWB7hZr7GM8183ADv8PO9zAOdU3uunx30eZnxbPEGGG3lhJAV2QF85Gup5xUEz507QcQrKhL6K_1HGwTOBRxObz7w89nRg2pb-ZX-Jubn1ClyaykEijbWuOSxBwKamlV7WGjuo3njNweFpypEq1YCRBu6dbHUcWNNZdQT7z1luqFpl4I2oKqxKgzYJXsuHtafwdJvSHE_aWy0Sxlv_YvbaM0QNDJUN3TWMmVCvIQ2i8ZOtFf99wESvnu7csp3cqAvIfcojeWVYK2EbIOxvy3OKeIibXqU3nqFwFmoGnUimIV85iORK4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccff2e7a05.mp4?token=Fkd7m3x14qTWNX5TqdWy_pjfFZlH_ycLDOsWB7hZr7GM8183ADv8PO9zAOdU3uunx30eZnxbPEGGG3lhJAV2QF85Gup5xUEz507QcQrKhL6K_1HGwTOBRxObz7w89nRg2pb-ZX-Jubn1ClyaykEijbWuOSxBwKamlV7WGjuo3njNweFpypEq1YCRBu6dbHUcWNNZdQT7z1luqFpl4I2oKqxKgzYJXsuHtafwdJvSHE_aWy0Sxlv_YvbaM0QNDJUN3TWMmVCvIQ2i8ZOtFf99wESvnu7csp3cqAvIfcojeWVYK2EbIOxvy3OKeIibXqU3nqFwFmoGnUimIV85iORK4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⚪️
ممبینی دبیرکل فدراسیون فوتبال: قبل از جلسه فردای هیئت رئیسه  تقریبا به این نتیجه رسیدیم که قلعه نویی سرمربی تیم ملی در جام ملتهای آسیا باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104665" target="_blank">📅 21:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104664">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/az_modGAQEjKo7EHG5ogsfyq6ZJIWZ2NPEpmdO7cDQEmptW-OqL0FeP0HhlqoBvxwrzWKgxmQkfdzGPbELTDADA887dWE3kKwtcsxUDVymcL0el82oee1Zor-EhNoxQcmy4izcYDxxGk0MokMIiMvDcPjY1fDzuOkW8BqBt4CkKnXMEWLEglYRelJUVuwYZosHKOzPlmVNiuBghhGXnZJr7lYW1UPd341nfrg8eWw0L093xiuGI0HcuoED0UN7LgAAa0gyNrx3b6ZbwpPMZJ-yOpP8k4EWLfAlLMXyUpflCgWkDn5HDdUZLRZ15Q1BYpNmZnfhZWlYeM1WUjhbVmNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚑
🇮🇷
#فوووووری
؛ اوستون اورونوف در بازی امروز دوستانه پرسپولیس مصدوم شده و تا فردا وضعیت دوری احتمالی‌ش مشخص خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/104664" target="_blank">📅 21:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104663">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db2b316284.mp4?token=qXZAnRBfxL32uZOA2VC1UWuLRiIT64MBc82hRA4W6nJ9hMvljersqHX5X9nC8n3tGGJuxLAPQ89xmSOm3sT0G3xTr6FLQwcS9B-T1E0zmbVLFdl5BcQyogtn_STOIpRVuTB-fUgYkz983tcJC5-ivQDbjldzoiawgyz-Ol9e8q6U2SoLKUVtzVL6qqwpMZlNqKx4JvGjDeSVekXeI-sa5B5i5x2pIoT-JTX2KeO6KNJ57OPJNUNYFwdMmmFuaV80A6G9MCxaxhiTsON9pRnsVeIL47xvMslp8IXGeMbNFdYO2xeA0ypSFVRGLXPClH4TOpPG0tpBLZwIWsruISKeRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db2b316284.mp4?token=qXZAnRBfxL32uZOA2VC1UWuLRiIT64MBc82hRA4W6nJ9hMvljersqHX5X9nC8n3tGGJuxLAPQ89xmSOm3sT0G3xTr6FLQwcS9B-T1E0zmbVLFdl5BcQyogtn_STOIpRVuTB-fUgYkz983tcJC5-ivQDbjldzoiawgyz-Ol9e8q6U2SoLKUVtzVL6qqwpMZlNqKx4JvGjDeSVekXeI-sa5B5i5x2pIoT-JTX2KeO6KNJ57OPJNUNYFwdMmmFuaV80A6G9MCxaxhiTsON9pRnsVeIL47xvMslp8IXGeMbNFdYO2xeA0ypSFVRGLXPClH4TOpPG0tpBLZwIWsruISKeRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
اشک ریختن هوادار فولاد خوزستان در بازی دیشب در آرزوی دیدار با رامین رضاییان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104663" target="_blank">📅 21:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104662">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7BYaw66mZjuArE8zBTW6SEgePcW1ir6dYDzLzBrL7G9DMWMrmxSW-52yf56aqHwrvzHsEVhb2y3DfR1FtcqCI5aV0ZBBXfkidg4X38-m9eg4by1N49VmNqBFCtc9rm5FHJhcp0EzQACvaPC0sAW2cYvyqUwXTYz-z28E2cGz2uFEQHEd72QC2DLw8p5Wm148PUhyb1zZGIZ_m6ykGVPbIReq2YIRgacRrGkIPPQGBPtZ0k0HJ9tH-4y_udIiMr79joRS_xKEOp0QGTYxPg1mYX16jWPQeLtutrWnTxIsyCkUD26WGxUa6KCtNJS3kmohqZuprO0pOs2jy-0QiyfHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فابریزیو رومانو: لیام دلاپ با 50 میلیون یورو از چلسی به ناتینگهام
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104662" target="_blank">📅 20:39 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104661">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r2WhKSwmWdGkikdndUKTuGycmTY2xfApadti52xGZrEZYdA1c8GH5f5swJG_iJbnH3Y27g9iWeWoplmGgPaaARRs8jLmMf69iiTpMw3oxwV8KtK6FTOQkMOp5TqIZby5JZkMiNrsFrqx3e9gueaH85qiz8XwfXS42FNHSGorBJNhXh5tOKCvL-VNNONSy8JGIwIsaivz4AfsvHUZWtAk8wHPYr_gblzObgSE6rFd3OruuKrTp_gSD0C2_0G38ydpvZf52oA8hqUGqhYOp4FMjPE6jFz9vyvHc03uTTcGCq-FjGw11E7QvZdezVj8TOlHvvnku42k8eEgN9wEPJ9Z8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رونالدو در ترکیب فیکس النصر مقابل الاتفاق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104661" target="_blank">📅 20:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104660">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELC1B9N8wm9dL3t3nDhCFdYr_ZftJ805twFGWbha6XBuxhGM0R4SdKqZoNWBhIvtoqaFYEjN0RGJWuJNIsyzAUJYiQtGtB9_LT807NNkf0HFJwO2dyfK0qiKkwzQNeRIWHQgC-uA3VIA3kA36BDJoZWhJIoIaCbytKAv-EnJfrXX5iZ2ZxpEz43ytgVWn-27gMGVHE8fthj3mLsLr5sSBtbP5C1Vz92vpARqsNZO2ksKbiF-_hfk9JIUXZW3zaqpWLvDZU-QmCdg595PROC2zETOhJCVIozh5LEBw_eb178gkhYi9HqCizU63smVEYwT406o9bs7Hdir0JY-Aes5yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✅
🇮🇷
🇮🇷
بیانیه باشگاه سپاهان: رفتار عارف حاج‌عیدی مصداق بارز رفتار غیراخلاقی بوده و از تمام هواداران استقلال عذرخواهی میکنیم و تنبیه‌انضباطی متناسب برای این بازیکن در نظر گرفته خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104660" target="_blank">📅 20:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104659">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1H448Hn49_iHW_mX-m0st_TLsjCzuVdwu81Mo5EwS3tKzNp3BeMbUF1iIqo4_kRLGxOc37TGyuxeTNAU5hgPFki0OTFcltWL9ewSyQ8sNITmOOIW96krW6iwzZev7sONLJ1ozGbZY219g7DrczorlIejCXOkBLBgwbbx_lGi28qmJWjHzuj2nq-QokPp8N3LBxB_apPludXGqFz4ai6p28nOF9Z0hBmwGdm85PO-51jMjw9MyqxuYFY22LflQiVFLlFsi6Sr7oim5ntJbTYWZV078TjpBU0E5n_G5Q3F2UzEeW04iANOaGf4K9wBbYemJxupan5aS6vAaiCX0bL1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
دیوید اورنشتین؛
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
لیورپول و پاریسن‌ ژرمن امروز در حال انجام مذاکرات کلیدی بر سر یک توافق احتمالی برای بردلی بارکولا هستن.
🔻
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بارکولا میخواد به لیورپول بره و نمی‌خواد قرارداد جدیدی با پاریسن‌ ژرمن امضا کنه.
🔻
🇫🇷
پاریس این بازیکن رو حدود 145 میلیون پوند ارزش‌گذاری کرده، در حالی که لیورپول می‌خواد معامله‌ای نزدیک به 100 میلیون پوند انجام بده.
🔻
✅
مذاکرات امروز دو تیم گامی مهم در جهت مشخص کردن اینکه آیا میشه به توافقی دست یافت یا نه، تلقی میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104659" target="_blank">📅 19:49 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104658">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48bb1d2255.mp4?token=aLjuZmoOyrNqftjpLRC0B26_S0yR0N8WVoFXxFpXeB-ebZ60-hQLAxHAVnbVx8x3eveVZSolF4JkFv2fqx33tv2Usd7IvDlbLf1zWk7OVbqwXSDKJptorxCfm7Bv3E2fjqio-X55zlFyIBb-jpDNvDruHY8ODOGdv6BU2tcKUBVaZ9-efebmh8Z_PuQpA1_ZpVo3Xr0BZTpKvugQXw9WlqCYaHi3bTr6mBIRyZUTh7mCfaC6EdKmqpb4hKurFoPa46zC8m7AXYotR06CFowHrbqtZfyIl2jVvFyIAMVw8PtvII2dVQ8_aVHcurR9_tTPVX7s4sAS4YJlqrlVI2nQZov6dngxCbxDLV0phHLykvKNKXdrpQsKzhyQDvSHgpJHhrJyjtapgAogJmjjTdpEPZuU5cKfDVOlKvBt9hH0socFuYAahMsNvUqLj4xd34ws9GbbOSZPYyjoLIcDTSQAZ1nu92dMxozSM6dr-RqIi2NEDs3OEpgU9GGXemZtWqMtF6PoNpe5lWKabfKB5nBuz5yCVg52NrWpOZkIxcfWmfR-FsY53d8PLv5xXWj_exLMN3OIDh0ntoInNq7k1B3j7yUSuS-Fe1Tryl4EeevgUeRIYnQZzMgQZbf4Hj6XzxemUMnIjvcKXua1dYnuxERyjgLlmSKfcxFg37vE2aUjnYc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48bb1d2255.mp4?token=aLjuZmoOyrNqftjpLRC0B26_S0yR0N8WVoFXxFpXeB-ebZ60-hQLAxHAVnbVx8x3eveVZSolF4JkFv2fqx33tv2Usd7IvDlbLf1zWk7OVbqwXSDKJptorxCfm7Bv3E2fjqio-X55zlFyIBb-jpDNvDruHY8ODOGdv6BU2tcKUBVaZ9-efebmh8Z_PuQpA1_ZpVo3Xr0BZTpKvugQXw9WlqCYaHi3bTr6mBIRyZUTh7mCfaC6EdKmqpb4hKurFoPa46zC8m7AXYotR06CFowHrbqtZfyIl2jVvFyIAMVw8PtvII2dVQ8_aVHcurR9_tTPVX7s4sAS4YJlqrlVI2nQZov6dngxCbxDLV0phHLykvKNKXdrpQsKzhyQDvSHgpJHhrJyjtapgAogJmjjTdpEPZuU5cKfDVOlKvBt9hH0socFuYAahMsNvUqLj4xd34ws9GbbOSZPYyjoLIcDTSQAZ1nu92dMxozSM6dr-RqIi2NEDs3OEpgU9GGXemZtWqMtF6PoNpe5lWKabfKB5nBuz5yCVg52NrWpOZkIxcfWmfR-FsY53d8PLv5xXWj_exLMN3OIDh0ntoInNq7k1B3j7yUSuS-Fe1Tryl4EeevgUeRIYnQZzMgQZbf4Hj6XzxemUMnIjvcKXua1dYnuxERyjgLlmSKfcxFg37vE2aUjnYc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💥
ستاره استقلال رکورد جهان را شکست
🏋️‍♀️
عبدالله بیرانوند از تیم استقلال در جریان لیگ برتر وزنه برداری با مهار وزنه ۱۷۲ کیلوگرمی رکورد یکضرب دسته ۸۵ کیلوگرم جهان را یک کیلو جابجا کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104658" target="_blank">📅 19:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104657">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c5505a725.mp4?token=TGSOXFY-5EqISWS4yXPk8jr7Jg2J_YWiWqVwRV2NjkGC_ggyAUlkwFlVcZng-859xnUemBnEM8YHX_fIkZUJ-vYQPK_diZaOmqLPakZ-JOEIMgwhApiBcBaZouQ7_2zI7htyQVA9fSgJeOAjNiHvtC35ivvOYTZso10xYvYxykFhoqp6ZGRY4MX72cOqrtYhhmmlRQ3jKbEBhJurewnM2F5D0wKWZm7T1BVid2l4ng0_iqJd_bSrNdjGJshbbr5HnHCVtjbsCtnmGAvTdFjx6g9MYB3_Ul6t1F0vnqvvMWWR0DWxjvsVJ02d66y1gKcd0tw-ANsIEDd06I25CHpPjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c5505a725.mp4?token=TGSOXFY-5EqISWS4yXPk8jr7Jg2J_YWiWqVwRV2NjkGC_ggyAUlkwFlVcZng-859xnUemBnEM8YHX_fIkZUJ-vYQPK_diZaOmqLPakZ-JOEIMgwhApiBcBaZouQ7_2zI7htyQVA9fSgJeOAjNiHvtC35ivvOYTZso10xYvYxykFhoqp6ZGRY4MX72cOqrtYhhmmlRQ3jKbEBhJurewnM2F5D0wKWZm7T1BVid2l4ng0_iqJd_bSrNdjGJshbbr5HnHCVtjbsCtnmGAvTdFjx6g9MYB3_Ul6t1F0vnqvvMWWR0DWxjvsVJ02d66y1gKcd0tw-ANsIEDd06I25CHpPjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
❌
⚠️
علی‌محمدزاده: پژمان جمشیدی از اتهام رابطه جنسی عادی هم تبرئه شد
!
💬
محمدزاده وکیل پژمان جمشیدی بازیکن اسبق سایپا و پرسپولیس و تیم ملی فوتبال ایران: قبلا هم پیش‌بینی کرده بودم که رای پرونده پژمان جمشیدی چه خواهد شد. خوشبختانه، متهم یعنی پژمان جمشیدی از اتهام تجاوز به عنف و حتی از اتهام رابطه جنسی عادی هم برائت گرفته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104657" target="_blank">📅 19:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104656">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ کارلوس‌بالبا هافبک باشگاه برایتون با عقد قراردادی به ارزش ۷۰ میلیون پوند به تیم منچستریونایتد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104656" target="_blank">📅 19:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104655">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icdicnOApzqDy5NNXP4jujg8KlHy_h5T_0TTk9HPixey1A81SkE5XQiV_5VbxYBiRyseHk66NkgI_34JwFEaUTwN-JLIvmt3TlzW2LCbxU7dJFVoqRjS8EuHZhIbjxGUHazuWUf01qTiR2ttsWHD5lqwsCP7Z865WRptmuKDsGOo3ZmJNqnbdBouhwxolm3Y5LFhww181OKiyZAz9uZZpTaX4TJMsmQUcOzJWE4-lCF_KvyDgvT43Q8brN2SPqOYAtWVpDvydajwFQnVVutPfrpH0q-sCEja86Clz4XbXJDDvo23mbNLUzsCoOxNa-L7SE_Vzy5eptFG4DRk7cgBWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔴
پرسپولیس در دیداری تدارکاتی با نتیجه 2-0  تیم امید این باشگاه را شکست داد.
⚽️
شهرآبادی و ایگور سرگیف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/104655" target="_blank">📅 19:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104654">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuYiM-OCiEYGIbPiUapPJ32x4NxFa_8Z3SvIgGpmPW2T5bNMKvSni4s0mUkDXK7xZh2iPNhQ6AUxsjSOOKzQS_Xki3xZz5NIOr3xz5Gpv_Ti52aFPU1kII8rBJs_ATG2FmWzxdC4IidOSD_XQRhxfMm8cWY-mEBdBTsojKzD83eiukA9aohhYfmqcE791e9ktjuTVXYpdl_AFUkPEiNWvd24I5lUr5eVSvXyCjUW1vXpIZBwXFuznoZ225RFg3mr5K96LDAfml90nsqxsMZseryLoZeGAP93GZTLjFgc4nh-lS6RWxC0Xz60yv3zg_bagJvvskTAuA6SU3eRqHOaOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
حرکت منشوری و عجیب عارف حاجی‌عیدی هافبک سپاهان پس از بازی دیشب خطاب به هواداران استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104654" target="_blank">📅 18:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104653">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33e507f396.mp4?token=R_HPgxSD3Taew2fLM9zVTbUGg6zRdYS74Wez2C1cytnR9fNJt_To1NHxkpNjO1CpvVTNBtdJJx9yz4rwYDjVfq5Q9cEjK5ZtGiBBAqVhsVtXT_6bGQEqtFZqCq3aXnEFZ_hKt5N4XkWZikKto88dDlL2q-pL0pjLyd6F1027lNNRWAD7o4zIqD8ZCx65akTtImbXPPQafc5cCbu3EJNumeKV1heo-T6rumrkVSOepUnMkZbRuFeWyBcfSvVwTRHyXji2w73tye5yo5PbC6GeWTbJ3I29c8xKWzqhpnbrCBmV6FWpJ-gieIvcgWpA99G4WNKmRzG84lcwdlutnFJYCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33e507f396.mp4?token=R_HPgxSD3Taew2fLM9zVTbUGg6zRdYS74Wez2C1cytnR9fNJt_To1NHxkpNjO1CpvVTNBtdJJx9yz4rwYDjVfq5Q9cEjK5ZtGiBBAqVhsVtXT_6bGQEqtFZqCq3aXnEFZ_hKt5N4XkWZikKto88dDlL2q-pL0pjLyd6F1027lNNRWAD7o4zIqD8ZCx65akTtImbXPPQafc5cCbu3EJNumeKV1heo-T6rumrkVSOepUnMkZbRuFeWyBcfSvVwTRHyXji2w73tye5yo5PbC6GeWTbJ3I29c8xKWzqhpnbrCBmV6FWpJ-gieIvcgWpA99G4WNKmRzG84lcwdlutnFJYCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
واکنش محمدحسین میثاقی به تصمیم سهراب بختیاری‌زاده برای نیمکت‌نشین شدن علیرضا کوشکی: با تصمیم سهراب حال کردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104653" target="_blank">📅 18:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104652">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/104652" target="_blank">📅 18:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104651">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAreygZXCiYr2iyv2zAxoWseEBQAT4_uQj5gKQRaKm5wUNZDJotNzDm7B-XaebtKjdoI7axseny37S2fWEgmkaVDAIlJhE0GQiamo8k6ACeiJU6FksMPEDRGxA-icRtHl6qdQe5utuvGZuUSwPNl8X-DM9RUTAWs2JM0W328N2MB42IJ9e6gE4YTUvDsPNbzWyH3Gk5I8Zi3aVEF_YC5uGaGkx4oY2D7d9YAKtt4xZkzDWapAzaLgpYgUp8nIgw2QbiNM1XNo-U2GB47i21XnvQIPg02oT_Szu0AGHBi2r5uDpmycbo8-1hCaEJL7TTQ8inXfc0T83cQ3pAjsYlU8uwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAreygZXCiYr2iyv2zAxoWseEBQAT4_uQj5gKQRaKm5wUNZDJotNzDm7B-XaebtKjdoI7axseny37S2fWEgmkaVDAIlJhE0GQiamo8k6ACeiJU6FksMPEDRGxA-icRtHl6qdQe5utuvGZuUSwPNl8X-DM9RUTAWs2JM0W328N2MB42IJ9e6gE4YTUvDsPNbzWyH3Gk5I8Zi3aVEF_YC5uGaGkx4oY2D7d9YAKtt4xZkzDWapAzaLgpYgUp8nIgw2QbiNM1XNo-U2GB47i21XnvQIPg02oT_Szu0AGHBi2r5uDpmycbo8-1hCaEJL7TTQ8inXfc0T83cQ3pAjsYlU8uwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
g3
⭐
کانال اطلاع رسانی سایت:
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104651" target="_blank">📅 18:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104650">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9040b715e4.mp4?token=ksSdX30cJazwUegkqMWZalzY_EbuGNQKnnuN4B7BhLevDHKPRbKIirStVee-J5T7BjbR4NFLFG31ASdfyRMj65dwaR3PUoecpQnPNijTQK8lGmdESbY2yu1_2YGedMjEPbTZuhWYk8qqW_R5eq72D4AWg5ZFyOaLsQjcgmaRUP3VE8fYc7fVLcp8MxLjgRtc7x0iXDkmLUPMaeEuOloOP1zOzsCTne9bRSRBkZIDXpCFsJHw9MYCQyC0DHm6etS8VR3cLPwuq7EXqf51_U2EZ2S-dGxEI4DYegOajVtLp8TbWtayrrNeN6lGGlP3w0ASvqlLgC1Mds4H5ibmBGRZVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9040b715e4.mp4?token=ksSdX30cJazwUegkqMWZalzY_EbuGNQKnnuN4B7BhLevDHKPRbKIirStVee-J5T7BjbR4NFLFG31ASdfyRMj65dwaR3PUoecpQnPNijTQK8lGmdESbY2yu1_2YGedMjEPbTZuhWYk8qqW_R5eq72D4AWg5ZFyOaLsQjcgmaRUP3VE8fYc7fVLcp8MxLjgRtc7x0iXDkmLUPMaeEuOloOP1zOzsCTne9bRSRBkZIDXpCFsJHw9MYCQyC0DHm6etS8VR3cLPwuq7EXqf51_U2EZ2S-dGxEI4DYegOajVtLp8TbWtayrrNeN6lGGlP3w0ASvqlLgC1Mds4H5ibmBGRZVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نباید هم بترسید؛ آقایان مسئول می‌گویند از تحریم و تهدید و محاصره اقتصادی نمی‌ترسند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/104650" target="_blank">📅 18:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104649">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
⚠️
بخش دیگر از مسابقات جهانی ربات‌های انسان‌نما اینبار در رشته وزنه‌برداری!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/104649" target="_blank">📅 18:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104648">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47d29aa087.mp4?token=JFbA7xaJvCOYOMjplSXKloyWPBLk9rc2JlpDDMSfWIb3hGdQlTRJ1DLQFIcD_CnfuMyDHdVL313_9Eu3tH16jrI9cHAErKt7IlknmofjLTdduwTdzHbt985mTM_1jqlK59V9JvwZtUremqTtTLnynmrHU-keJBZ4p3K1-bYdpWraLOr4QIzB8VD3MIP3ArhJLQ7vHU9rNjapPwTJOLTRjUqFLcD3WzK7cvSib6hkD8HCVKcI5GcHwAB02fb-4J5t5su62Koyr02SzPN2HfII2w07S0cIYRR-mjcxr1FkaDGEGsL2moOLxt8x3KTSs7co5fCP22ffOU8vceBfh75pNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47d29aa087.mp4?token=JFbA7xaJvCOYOMjplSXKloyWPBLk9rc2JlpDDMSfWIb3hGdQlTRJ1DLQFIcD_CnfuMyDHdVL313_9Eu3tH16jrI9cHAErKt7IlknmofjLTdduwTdzHbt985mTM_1jqlK59V9JvwZtUremqTtTLnynmrHU-keJBZ4p3K1-bYdpWraLOr4QIzB8VD3MIP3ArhJLQ7vHU9rNjapPwTJOLTRjUqFLcD3WzK7cvSib6hkD8HCVKcI5GcHwAB02fb-4J5t5su62Koyr02SzPN2HfII2w07S0cIYRR-mjcxr1FkaDGEGsL2moOLxt8x3KTSs7co5fCP22ffOU8vceBfh75pNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای تارتار والا دیشب پرسپولیسیا نه پرس کلوپ، نه‌پاسکاری گواردیولا و نه سانترهای آرتتا رو ازت ندیدن برادر. قبل حرف زدن دقت کن استاد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/104648" target="_blank">📅 17:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104647">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f287b16532.mp4?token=pU_zkF4DSII4B6u3CLd92qpuZJjTSBU8sy13t2nRe_lHe2Rs6djS45azxBv1syTAO9CIGKN4I6mJWgfKqOT6LDhs_b3RdHTyIf4nt2qTXIp3m_bJMSIgaYzKiTIYAQDM687asOh2g5pn6R_E1WD92Q7eWaOxYrYG-Ab-tpG-ndHCtubnmiB2IPFiWgkK-9nHloFVOpRM-5lba5qNTF67lE23Px8TG57fB_I57P4c88wcM7_flDVQv2BEkWy0g0cSwC7MaG_hqLL8e5MkLOsoRUjk1VJftbi_ChXDlFNJSAYX4U6ICYGLy_lN1CGc5OvOC2dUh0ZN4xFlZG_xP9mTzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f287b16532.mp4?token=pU_zkF4DSII4B6u3CLd92qpuZJjTSBU8sy13t2nRe_lHe2Rs6djS45azxBv1syTAO9CIGKN4I6mJWgfKqOT6LDhs_b3RdHTyIf4nt2qTXIp3m_bJMSIgaYzKiTIYAQDM687asOh2g5pn6R_E1WD92Q7eWaOxYrYG-Ab-tpG-ndHCtubnmiB2IPFiWgkK-9nHloFVOpRM-5lba5qNTF67lE23Px8TG57fB_I57P4c88wcM7_flDVQv2BEkWy0g0cSwC7MaG_hqLL8e5MkLOsoRUjk1VJftbi_ChXDlFNJSAYX4U6ICYGLy_lN1CGc5OvOC2dUh0ZN4xFlZG_xP9mTzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
😃
رونمایی از ربات رونالدو در مسابقات جهانی ربات‌های انسان‌نما در پکن چین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104647" target="_blank">📅 17:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104646">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xw3LpqSfVczRoNE15DFayvB2-OKaGvcINWNPdKTi2OJwD0sIDHKnuHrXe9AGKBj0NCVwS5CMJ6HPuE6uijDEnzyZ8hYcuP4x4KSo8ndTX4I6s2DAcI_Xoqov5aCMGCXyO9e-KIwYJbF9_QcWwkQ2fDGGLgNxTleJi_Fb_SXlCmTjUKpu7xzNEwTt1QDWhWwAcu46zQLznS5rhvo2A6-DGbQnYhNg_3Qi7h75qndYhu8qrwKQlMbH24-q9whU_-Vv9gJIT2zuBtPjVLszzPVghsZzdwP77KWU2BZNatSvwMfmb5x2ZtCQgJPg0YKIxqlo3NQdBzAVhk8sTdeUH9w5mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
روزنامه RAC1: بالده اگ پیشنهاد خوب نرسه به موندن فکر میکنه و فک میکنه میتونه فلیک رو متقاعد کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104646" target="_blank">📅 17:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104645">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2f481f1fe.mp4?token=NQ9-IkU33mLTtJDCxpL-MEddl7J3UIVxc36xA2vFQDi_DdC6hnIA7koQ-rTLcTRCbBQ3V3SYUkkRKxtceOTukjcCC1vK5IFWudiRzofSYvTEeOXvkcl2M-LA49gjpn966f-I_vWxvMbZWnp5XgwDIysgk5jsiPsODXXRaWtSQJSK9E9s9SWdsO8hKC2sa9FpjbtlIL0mxcOIA_h24iHp7wkMEs4OY1AmtB1HscB48zVw6gs2ZnQlYU7ytblgAJEe1ZZ7k8E5_3tfzxLth32UzuC1fuEBLqOywh_yWYEUKYyuSM162V0Q4uRePDg5GNqjh2Nv4Hk1lXTzX43IyfV3zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2f481f1fe.mp4?token=NQ9-IkU33mLTtJDCxpL-MEddl7J3UIVxc36xA2vFQDi_DdC6hnIA7koQ-rTLcTRCbBQ3V3SYUkkRKxtceOTukjcCC1vK5IFWudiRzofSYvTEeOXvkcl2M-LA49gjpn966f-I_vWxvMbZWnp5XgwDIysgk5jsiPsODXXRaWtSQJSK9E9s9SWdsO8hKC2sa9FpjbtlIL0mxcOIA_h24iHp7wkMEs4OY1AmtB1HscB48zVw6gs2ZnQlYU7ytblgAJEe1ZZ7k8E5_3tfzxLth32UzuC1fuEBLqOywh_yWYEUKYyuSM162V0Q4uRePDg5GNqjh2Nv4Hk1lXTzX43IyfV3zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتایج اینترمیامی با حضور کاسمیرو:
4 باخت،  2برد،  2مساوی.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104645" target="_blank">📅 16:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104644">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29f38711d1.mp4?token=lJdcqrFCiQMe99Qq2LSJKq-a4x4a-ViYMT7NSt_HFxbiNCWhBeon7H4NgvSMX4t6HfiF1Exx8KTNUgwEMoTAPuWDDxQ8p9S_GDtinCaN65a1ulofRBGcLDGTvzf4h0ZffBTEupmmM-KsVlKshfR-TlCaN35qHnP61ocxOlAhewWPilLmq5FFf1y77RC9N9eenFjQvqZc4Ta0QoDGngNZT8Z-Seo25tKBlWc8SUIVsiC6fL36Tw9Y08nSgHbH9pi2FyFbDKUhjbrOswu3gRhP4H9irqpa9pNnJNJw2wlYSL2v0gPOJVzFgFZ619edU7_ODMIFYuvTyz9qHxBxKFp-Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29f38711d1.mp4?token=lJdcqrFCiQMe99Qq2LSJKq-a4x4a-ViYMT7NSt_HFxbiNCWhBeon7H4NgvSMX4t6HfiF1Exx8KTNUgwEMoTAPuWDDxQ8p9S_GDtinCaN65a1ulofRBGcLDGTvzf4h0ZffBTEupmmM-KsVlKshfR-TlCaN35qHnP61ocxOlAhewWPilLmq5FFf1y77RC9N9eenFjQvqZc4Ta0QoDGngNZT8Z-Seo25tKBlWc8SUIVsiC6fL36Tw9Y08nSgHbH9pi2FyFbDKUhjbrOswu3gRhP4H9irqpa9pNnJNJw2wlYSL2v0gPOJVzFgFZ619edU7_ODMIFYuvTyz9qHxBxKFp-Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هری‌کین در نقش هافبک در بایرن‌مونیخ
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104644" target="_blank">📅 16:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104643">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88cac48e79.mp4?token=MMdiCgg6fUXh9YUUQCUO5-CY-tplY9RpblVPY_fL1gSJk4jrE63-TEn7u6vDgsQQeaWFEOpcsxCMORCx2QBWgNAs3qVl7VzpmY9sAM9o7ftK1SNcF5f3yTPh8i7cXJ1BU90X8gyV2UcsLgPfjlS5wmNaqyxxsyi0XI_Rs4CCuJ9eFFl9X42oD2Wl0jGTCryt1qgjN96tja2SxX8Xa67XnnZBTDFEG6VFv-F_nylIEy39UrNynvT8JjUyt1YuYLY64GKMEztNz4t_JlEJBqFOWTsJnxJnNt75kmK4hj9QfpZXX5aOtekJgW5MOmuJHoWozPGzr13MLcPUOKhtZfjOTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88cac48e79.mp4?token=MMdiCgg6fUXh9YUUQCUO5-CY-tplY9RpblVPY_fL1gSJk4jrE63-TEn7u6vDgsQQeaWFEOpcsxCMORCx2QBWgNAs3qVl7VzpmY9sAM9o7ftK1SNcF5f3yTPh8i7cXJ1BU90X8gyV2UcsLgPfjlS5wmNaqyxxsyi0XI_Rs4CCuJ9eFFl9X42oD2Wl0jGTCryt1qgjN96tja2SxX8Xa67XnnZBTDFEG6VFv-F_nylIEy39UrNynvT8JjUyt1YuYLY64GKMEztNz4t_JlEJBqFOWTsJnxJnNt75kmK4hj9QfpZXX5aOtekJgW5MOmuJHoWozPGzr13MLcPUOKhtZfjOTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😞
وضعیت روانی خولیان آلوارز در اتلتیکو دقیقا با این موزیک میشه شرح داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104643" target="_blank">📅 16:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104642">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed5ac9e8f.mp4?token=ED2diYvwzsBnCyn4oNIrIlRvSu1xcV4FeAVrvoJvbCrBMPW1yCQYpSsXpt__CQlEoL4CoBEqR35fQTPMIy5Uw0bjlvXqgt7qPSvza1_D8QNDsdaXPbVVe8QaAYREpAIq3ASAF0wWB9TK6j5Op9VSAKXBk77w4mvzSHj_s2XqtfG2wwqPCPYuXEPtjSlu0baj_9zm0ykhpcu4qj-9_qTecLprRIjDQTpaOPP5HlbF4inc8LaovzRF2XAX0MbDXIiIrQoQkbf8yeOcmCccF7-bISGJReodtbbtF0C9FC7pFFhaV4aJJf69NZPS4_WroJGa3W0PivTborJVpmbt9um4JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed5ac9e8f.mp4?token=ED2diYvwzsBnCyn4oNIrIlRvSu1xcV4FeAVrvoJvbCrBMPW1yCQYpSsXpt__CQlEoL4CoBEqR35fQTPMIy5Uw0bjlvXqgt7qPSvza1_D8QNDsdaXPbVVe8QaAYREpAIq3ASAF0wWB9TK6j5Op9VSAKXBk77w4mvzSHj_s2XqtfG2wwqPCPYuXEPtjSlu0baj_9zm0ykhpcu4qj-9_qTecLprRIjDQTpaOPP5HlbF4inc8LaovzRF2XAX0MbDXIiIrQoQkbf8yeOcmCccF7-bISGJReodtbbtF0C9FC7pFFhaV4aJJf69NZPS4_WroJGa3W0PivTborJVpmbt9um4JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چلسی که بوی قهرمانی لیگ‌برتر به مشامش خورده
👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104642" target="_blank">📅 15:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104641">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
▶️
❗️
صحبت کنایه‌آمیز و جالب امیرمحمد زند درباره‌ وضعیت فوق‌العاده فاجعه‌بار مملکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/104641" target="_blank">📅 15:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104640">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61023bc5f8.mp4?token=dWwWieqdB08D_YkMmkFSYAM1vqYu7FyjVt8a78NcG7eAAlYpBQOKaEOgPlxd3mIXg5yZE1RTlsK7Wz2q3XVMPQMIDqAJ9r7qhrmd_w3VChCak3vgNZ_Rdd4Pcju7L1eDgQz2Vgp1rcAjCK_uPR2BPxWWJJn1Xt9G4_C2I8hNy-5mUbVq1mkoMVTVDxVvYIFmtNkSoSqGjNKWYNWA_TBcJEFvvd9H_sy9vwX20CPKSqd0PvyHovgxztPKcIdpoSXtiYH2sQTbYCpfCqW-wULOquqP9yNuhSVEpXoMTLbCejNKUEnT1qZ5wMr1Ngg8-guiHqjNGxeYwGbhO_hU8Oz74g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61023bc5f8.mp4?token=dWwWieqdB08D_YkMmkFSYAM1vqYu7FyjVt8a78NcG7eAAlYpBQOKaEOgPlxd3mIXg5yZE1RTlsK7Wz2q3XVMPQMIDqAJ9r7qhrmd_w3VChCak3vgNZ_Rdd4Pcju7L1eDgQz2Vgp1rcAjCK_uPR2BPxWWJJn1Xt9G4_C2I8hNy-5mUbVq1mkoMVTVDxVvYIFmtNkSoSqGjNKWYNWA_TBcJEFvvd9H_sy9vwX20CPKSqd0PvyHovgxztPKcIdpoSXtiYH2sQTbYCpfCqW-wULOquqP9yNuhSVEpXoMTLbCejNKUEnT1qZ5wMr1Ngg8-guiHqjNGxeYwGbhO_hU8Oz74g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک خبرنگار اینفانتینو را گیر انداخت و مستقیم از او پرسید:
«به فوتبال خیانت کردی؟ چرا استعفا نمی‌دی؟»
اینفانتینو اما هیچ جوابی به سؤال‌ها نداد؛ فقط نگاهی به خبرنگار انداخت و گفت:
«چه مدل مویی! آرایشگاه می‌بینمت.»
وقتی جواب سؤال‌ها رو نداری، حداقل درباره مدل مو حرف بزن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/104640" target="_blank">📅 14:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104639">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fizbhcWCadJ_RjdJ_dforNIfPxsNlP-YzR7879al39DeYquC_8n6ZiHpbHaKpwME_kgLUcFjbQQeAGg8NyhqZrWnluYmlk7AhSj0j6JYjKmfi59wJ6epRZ7vBB_s1o4vKS16ZZ9SypcRJg1onV1mIv2d13Dlew4QnI2rc5bsjmFQHEoj4E6Xq-WrcspYWoLn-TIWvWBgHkp7WI2eSNDBGzgLgF8vvrVfmHCyR6Zu-8gslF4ZjWhW3x1cxo7oZgyjE5j-KfJgbXKxesNtPB3p6LHiFTgKUtOZLXBFw2Jx2mPNweQN1U0Y5aiexDdu-Sayqjai7mT9Df_PpbpV6sIvcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
اسطوره آرتتا چیز ببخشید تارتار دیشب گفت که بازی دادن به جوونا تاوان داره. حالا عکسو باز کنید ببینید سن بازیکنان ترکیب اصلی دیشب پرسپولیس چند بوده
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104639" target="_blank">📅 14:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104638">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dauExanztqhG34kye-0EwvAM7TqB3n0xwf7sJQzdsbFB1-PeatDxkAgBcFzQ41h4Q7wMsmKQHUEyLxO9adWpug04EJK1c3y387GOY_SHbI-ZzLpDS_pyWTpXWQX__qV4jfLSFAIKfH_P-Q_UL188GzDYzhKIaNpYtJeVXFi9OVPTYgBR15s9WEjxo7Q5BTeoYUwHaKdtyQ0opU9LuiQcSBwlEe-9r1qveHmIF9ox9JhZ9-L7pViLATdfgysOulN1IqTFvLtjhKWyoFb_UnrgjDYEUOmJ2zgE9E1ZtM3UhPVZpL7qnYNpLCnFn7QNkBHuG6FBUsvtQeD4iBMfU6p64g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
منتخب هفته‌دوم لالیگا؛ پنج بازیکن از بارسا
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/104638" target="_blank">📅 14:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104637">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f029f12cc.mp4?token=grK2mTPLjBLOyJck4yO_uoNbcCjG5CzJr3tLXWmjVSkbaNEzUKjxnIvm6EcJMFe4HzjUrKl8ca1I-ZdXTQ_b8-XDOVuJYZktRSNcf19dcsFV4SL3n74wSgumhvn5X2_-7A6SNz_O6eQJxDDjm5wHbrVL99Y10ZPNm9aFtnTjPyM6Kmmd-L3SrhMzC1TbiNPFoD4dFf1CMohExhAARvGYt3chJCvX_1ZeZk-ukzDVEy9RpBPzJMu39kXU2cwNMoMmBjCjjLz-oAt_-pgtQicoC6z3tiPu6g7X8dx4zVBNPv7G6TO3EvZs6iaM_xtP_y01svPxAwcHfvPwKlupi5skHxUBNX1-2rxm-cZx4Mk-u503hGHgdibJgcdICWPtk5RTBswOOUDarFgUzrlXKK50TDwqy01SaWE6sjp-p-p7KR9ff92d1DKG_TRLZW50FGjmC2830gOF8QppQGpQpslYv8ye60atReWsTpHqIX-Ekd07lHLR7zcsVvsbkfICfXFt3JMPs2vTJ6RqLuseKlnK6PYYPEJLJGV-8Mg-rx94S4QwZ7xvHJGKophO8QNcRvKJhKk7hYK8B0y2H-xbYXdk6WI7yAs698YgU98Lvsj5YphzL7taeKlfaoKd1xOLOYSO4ibbpAcns6W-gymssXsZGQPRhQ5sBBK4hIrmybAXpTM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f029f12cc.mp4?token=grK2mTPLjBLOyJck4yO_uoNbcCjG5CzJr3tLXWmjVSkbaNEzUKjxnIvm6EcJMFe4HzjUrKl8ca1I-ZdXTQ_b8-XDOVuJYZktRSNcf19dcsFV4SL3n74wSgumhvn5X2_-7A6SNz_O6eQJxDDjm5wHbrVL99Y10ZPNm9aFtnTjPyM6Kmmd-L3SrhMzC1TbiNPFoD4dFf1CMohExhAARvGYt3chJCvX_1ZeZk-ukzDVEy9RpBPzJMu39kXU2cwNMoMmBjCjjLz-oAt_-pgtQicoC6z3tiPu6g7X8dx4zVBNPv7G6TO3EvZs6iaM_xtP_y01svPxAwcHfvPwKlupi5skHxUBNX1-2rxm-cZx4Mk-u503hGHgdibJgcdICWPtk5RTBswOOUDarFgUzrlXKK50TDwqy01SaWE6sjp-p-p7KR9ff92d1DKG_TRLZW50FGjmC2830gOF8QppQGpQpslYv8ye60atReWsTpHqIX-Ekd07lHLR7zcsVvsbkfICfXFt3JMPs2vTJ6RqLuseKlnK6PYYPEJLJGV-8Mg-rx94S4QwZ7xvHJGKophO8QNcRvKJhKk7hYK8B0y2H-xbYXdk6WI7yAs698YgU98Lvsj5YphzL7taeKlfaoKd1xOLOYSO4ibbpAcns6W-gymssXsZGQPRhQ5sBBK4hIrmybAXpTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
یه پسر حدودا ۲۲ ۲۳ ساله با گل رفته بود ورزشگاه رامین رضاییان رو ببینه، رامین پیداش نشد و ایشون هم نشست یه گوشه گریه کرد:)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104637" target="_blank">📅 13:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104636">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c97e761449.mp4?token=LUsQVwTDCap31Cdfgzte0W1DVDjFrBax9MjSnTsSbYDco4x8Lays3yCSpV2movLCMcWht44Fyo4N8h8d0iFlso1OOgJQtwS7BbPkPtzRa68Z5LMygdTIewXjm7fiqlZqtWwTElUFIzoaZxiimjg-Fajn7ivjcuqUbQz_wj5u0r0I2yUedjIHez8raT0KiBHKBzo9toZ0qt4FFhbI3a0a_X2FbEBY8IQs0WRKbiNUlFEz0xj3lLL_6eDMtgojNSqRevQNv3O7u56WjBHchD_tfFdjErc3BV8srAlArIqcK1nLfA8NbzXb9Mcf8VAX6PKfa3thpVwTrhfw7QdB8m36eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c97e761449.mp4?token=LUsQVwTDCap31Cdfgzte0W1DVDjFrBax9MjSnTsSbYDco4x8Lays3yCSpV2movLCMcWht44Fyo4N8h8d0iFlso1OOgJQtwS7BbPkPtzRa68Z5LMygdTIewXjm7fiqlZqtWwTElUFIzoaZxiimjg-Fajn7ivjcuqUbQz_wj5u0r0I2yUedjIHez8raT0KiBHKBzo9toZ0qt4FFhbI3a0a_X2FbEBY8IQs0WRKbiNUlFEz0xj3lLL_6eDMtgojNSqRevQNv3O7u56WjBHchD_tfFdjErc3BV8srAlArIqcK1nLfA8NbzXb9Mcf8VAX6PKfa3thpVwTrhfw7QdB8m36eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حسن‌روشن: بنظرم تارتار امسال موفق نمیشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/104636" target="_blank">📅 13:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104635">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdIjRw4KPIRK001AoxuFFLxHVSLKdvQVfhtJc_5760v9K12Ml2zCeDVWrzRUNIf8FmLDXgQMN-2opCQ0uC2RCMvo8CZ0aQdUNhaZylohO47tDMCQn36Qe93J25FJMEbnkt6odFEUHRoAxXROi0D3Y6IEr2w5J39_vP5__nYJxKgSDHF9jQqN5rBZKYaLUBmRhMtpbQisZOlaXXd0B90kykS6EEQ8lHE9HUTLEpfB5c5q01jtxQdI_CfdHP0PSOdbobOHqZyfFBwab42YOoY0Db0-gYr3v4Xfc7YpiyvworsewX5d6ogPa7CQvzwdOWgLDEOegHiT2jNM_Bi75chjpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
☑️
منتخب هفته‌اول لیگ‌برتر انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/104635" target="_blank">📅 13:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104634">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffcea03907.mp4?token=IoIGCy3fKJiWWKCvCVzfcje2hGvR_IbCzkENVUMm6jAZL29TOeOaqjReZLs69gjm-KyB6qmpyVz8Sot9IqLEiYLhY4GI6qP2RdLb2zavgRd3hbY1sT8ZDUUg4debv23kDQCT5s8ixaeDiFihlk7g5V2TdUas5zSelTWsvd9rjhMsxRl3oL4uZdRPyWn4UfpidlpTK8b5wHYaaa6Zb7HTckk64QShw_MlD5gqpeEn6QiI_KzsFGnydyNShzr9cZPr2HHI-TyjXWBGrBHE-iaWAZSyvIQ5fWMcZINfZ3F7eRkrFQzosqzh58EQTWNn8Fv5zbfZAJxULvtBXrkerar_AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffcea03907.mp4?token=IoIGCy3fKJiWWKCvCVzfcje2hGvR_IbCzkENVUMm6jAZL29TOeOaqjReZLs69gjm-KyB6qmpyVz8Sot9IqLEiYLhY4GI6qP2RdLb2zavgRd3hbY1sT8ZDUUg4debv23kDQCT5s8ixaeDiFihlk7g5V2TdUas5zSelTWsvd9rjhMsxRl3oL4uZdRPyWn4UfpidlpTK8b5wHYaaa6Zb7HTckk64QShw_MlD5gqpeEn6QiI_KzsFGnydyNShzr9cZPr2HHI-TyjXWBGrBHE-iaWAZSyvIQ5fWMcZINfZ3F7eRkrFQzosqzh58EQTWNn8Fv5zbfZAJxULvtBXrkerar_AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
سعید دقیقی: دوست داشتم سرمربی استقلال بشوم اما نشد و بوژوویچ را انتخاب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/104634" target="_blank">📅 12:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104633">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15b0b27abd.mp4?token=TRSNpr0JbK-Kn_uz-9-vqYSRDVDp48ZB9N09yxcZD41bp7TXl8Whj4UA4JilGWQUTL0Hk_Cv7zYAYsr56I68BD7Aq2EsEShYEiKIocKfn4k6XTduP9gRowFaeHjm5GExl40OSHt6WlCmPSDqtMCat0NZve0-SRlJQLQQT3bwFYNMlsHnVOpcZq5ptYhjsmLpwarq3GMG7Jrgj8kEFaaN_Rbblbe_HP2e0nvCVn5t5DGE0_1nsapZr9RWrGJ8gc6JpZCxYatEoAAJ26gJABVJjYXwpMY08PLUUpmZfSHSp6KtmKLG6l1E1_XzFbp3HbneiFj7cUJcS21Wv05qe0XPZoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15b0b27abd.mp4?token=TRSNpr0JbK-Kn_uz-9-vqYSRDVDp48ZB9N09yxcZD41bp7TXl8Whj4UA4JilGWQUTL0Hk_Cv7zYAYsr56I68BD7Aq2EsEShYEiKIocKfn4k6XTduP9gRowFaeHjm5GExl40OSHt6WlCmPSDqtMCat0NZve0-SRlJQLQQT3bwFYNMlsHnVOpcZq5ptYhjsmLpwarq3GMG7Jrgj8kEFaaN_Rbblbe_HP2e0nvCVn5t5DGE0_1nsapZr9RWrGJ8gc6JpZCxYatEoAAJ26gJABVJjYXwpMY08PLUUpmZfSHSp6KtmKLG6l1E1_XzFbp3HbneiFj7cUJcS21Wv05qe0XPZoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
🇪🇸
گوشه‌ای از عملکرد درخشان لیواکوویچ سنگربان جدید بارسلونا در فصل‌آینده فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/104633" target="_blank">📅 12:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104632">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c053ee6d8.mp4?token=OVkEyT1z9ViDHNaDoZiInvj1SOhgIHjh3x-3JZWYIZyMW_pDTsIjMZxkgWz5JZD50-BE_zZLhTqYWoxF3puL5ZnKkCzuJh2NfKj5564uIHRYIfobLbXeBf86ZmyXr8EBgq5FSjcFdDNRxx2HLGxuopkSWioKDLaDTeQbweX1fxKW_OU38nYux4EiPErnekrLb76kRA5n3LtcQWgfJZ9rzE5pN4qX3p7RtvLzliEgc9YNytW0hPBugwB9XzUlJ-11KeAl5QIwyDnGWoQybBbXI-dVnZZXsfDPaoflzO8r9vZI3ziCxI0MuDqBWRofqOBwu6gprwPMxhWxqqyKFqMjxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c053ee6d8.mp4?token=OVkEyT1z9ViDHNaDoZiInvj1SOhgIHjh3x-3JZWYIZyMW_pDTsIjMZxkgWz5JZD50-BE_zZLhTqYWoxF3puL5ZnKkCzuJh2NfKj5564uIHRYIfobLbXeBf86ZmyXr8EBgq5FSjcFdDNRxx2HLGxuopkSWioKDLaDTeQbweX1fxKW_OU38nYux4EiPErnekrLb76kRA5n3LtcQWgfJZ9rzE5pN4qX3p7RtvLzliEgc9YNytW0hPBugwB9XzUlJ-11KeAl5QIwyDnGWoQybBbXI-dVnZZXsfDPaoflzO8r9vZI3ziCxI0MuDqBWRofqOBwu6gprwPMxhWxqqyKFqMjxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
امیرحسین اصلانیان بازیکن سابق پرسپولیس: عکس من خیلی طرفدار داشت. به پژمان جمشیدی جواب تندی دادم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104632" target="_blank">📅 11:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104631">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7472fb85f9.mp4?token=t_lzDsMQxHYRy4CI7MV-KDSR7JBWAf44Gs4E977xVz_jqsA2gGWBCGk5FJ5OK_5lT4djwp0SThdsi_cFyqvKOlzeTFvnp8bUI8-TAiG7Jp7l2aKXM0yEFezVGpv2ChvRzCJInwJV9OfxlC57MvJonjUp9hk-ZbWNhKPKQnFcIro_IrvSXRkKH5ORh0RNbtDBICULvjHPBfRnMaSQ7tMzvU9ZWSYuBkY2J2s3qONShXlY3VZ1SiXe73VDoWLe-Fp0Oe5SnXLvRJvUOt-kdzy4JZ2U7iJWCcJwTzm8TqGXzzPu3UFVHuuOrDoWT-L_t6QgkhN9ObmpKCILFMg-U653KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7472fb85f9.mp4?token=t_lzDsMQxHYRy4CI7MV-KDSR7JBWAf44Gs4E977xVz_jqsA2gGWBCGk5FJ5OK_5lT4djwp0SThdsi_cFyqvKOlzeTFvnp8bUI8-TAiG7Jp7l2aKXM0yEFezVGpv2ChvRzCJInwJV9OfxlC57MvJonjUp9hk-ZbWNhKPKQnFcIro_IrvSXRkKH5ORh0RNbtDBICULvjHPBfRnMaSQ7tMzvU9ZWSYuBkY2J2s3qONShXlY3VZ1SiXe73VDoWLe-Fp0Oe5SnXLvRJvUOt-kdzy4JZ2U7iJWCcJwTzm8TqGXzzPu3UFVHuuOrDoWT-L_t6QgkhN9ObmpKCILFMg-U653KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
شهربانو منصوریان: میخواهم پناهنده شوم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104631" target="_blank">📅 11:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104630">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzJa-Rl_K93mxPDIwxGvF8nQ0ehka7l8HaY-lGlTRojAfXeGddyh-MxcHa3gFBlkUKemRjMyuhpRu0BSJZhg9-_HfHkh8sIISyNHnkaZgFbm-uOCPmVHApQY7n3bDOTyifbtTYsIoByeu5_fB69XZh1I2PmJzFfMNE4P6-sbkJ9U8z_2o9PJzbCJ73oUjWIGp9cV6es17sM_Lou2tewjqMRU6evuwDSFpmIx6fFFvX0K8uCvwlqvGHx0a2k6PSI01dLo9d7pqsXrOGpdWmi8N0cZMbUTg_8pZYAJ_4oPfuyJCi9ueCUpsiO-nPFQv5Vi3RxMjoSM8TOBr5ucK0oiIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
بول بالوس (روزنامه‌نگار تخصصی در اخبار بارسلونا در نشریه The Athletic):
✅
جذب یک مهاجم شماره 9 همچنان اولویت اصلی بارسلونا است.
⚠️
بارسلونا نسبت به احتمال جذب خولیان آلوارز بدبین شده است، زیرا اتلتیکو مادرید هیچ نشانه‌ای از آمادگی برای تغییر موضع خود نشان نداده است.
⬅
بارسلونا تا پایان دوره نقل و انتقالات، تلاش خود را برای جذب خولیان متوقف نخواهد کرد.
⬅
اگر هرگونه نشانه‌ای از سوی اتلتیکو مبنی بر امکان انجام این انتقال به دست بارسلونا برسد، بارسلونا بلافاصله اقدام خواهد کرد.
👀
❌
احتمال زیادی وجود دارد که بارسلونا در صورت عدم موفقیت در جذب خولیان، هیچ مهاجم جدیدی جذب نکند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104630" target="_blank">📅 10:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104629">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2q7doSLdNZIEZ0qQVJvonB7WPv_gqFt_ntoDtJAVMy4kqOvBnaEVNH2-YupPYTFDJd5MVlIMG2RVDxUNehDjSvArqliiYYWxBkUQvvc0JB9qbaXkQt7hnnbg4Ey0kgfIvF5SMWOH6vbIGsjLcFEK-oeudHWRtn02F1ghtAqXqLHNYudR_iNQglku_3r-5ffZnONOZ9BTPadvuvwVL4mbBUlVmWtXYF9_nxqKsVpvrzI_CMNiFpAvUtslxcvtKwPsTBG_Ju5RgMrRsWoZwFAJuefGr7mb7WGhnUT2R5M86qSR9HaOSonoI4uKRzN6lY_oDzhAlDtKmgZ4_mS84Kcmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گستون‌ایدول خبرنگار مطرح آرژانتین: مذاکرات سیتی و چلسی درباره انزو فرناندز آغاز شده. ژابی‌آلونسو در جریان این انتقال هست و در صورت توافق مشکلی با جدایی این بازیکن نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/104629" target="_blank">📅 10:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104628">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RH6VufuTAWye40kakKiySj4azlDg6mf3Si9xR1uRi5ytZ697iEsVfEijY_2EMRqjKBoqSz036NU7ZgMi90l5Ju_p0nsQf7iwNY4-rE7a3V3UxLArMt-MCmvImBbg5rHll1iNr450tqVeE15qwp3EQGHQwrCoYeAYFlLXm3__Bxt3KNUXNPAae7l-ez0u-XQ7CezIe5bNgZ4j0cT1quLHsyRy5XCXyEgUFY6zAR6ev1Wc5kfYs6ezQXCz9PUPjA5kW0CvhhlPg2hjOW-N6U_DCG2zPWAIn1JG1eKeejfqcIwwRgeH0OmKFSp7Y6YQLurVK4kD5kVX_mrEd0M98iALnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
نشریه The Athletic: بارسلونا با نظر مثبت هانسی‌فلیک، لوکبا مدافع لایپزیگ رو زیر نظر گرفته اما جذب این بازیکن در روزهای پایانی نقل‌وانتقالات به خروج بالده گره‌خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104628" target="_blank">📅 10:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104627">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfrVjS4E23XfENlehNymytINSGqPUSh2HV_1DhBA2pjYiU5pK_TZGcANwtwDy0rJnuJH47bSPbcaP9DSyUHDOgGzNgfvZxPFmMc-FYEbJKsRACyQaOcL6FGJmWnCR3I38FZqnUF9PaHvijm24x32D3X51A08grlCkP5MN7bxkTtQKCum80eYa21sTsa1r_Lkg7bJrSlqmxpZhZu0SU0sXcXbkNp6L4kwq6mOHeiorEORiiKPnt0iIeOwSk3u2wOQ1Ms0tRifkfNMNDFn07UBqPVV_8d41lL52OJ7KRzofRlg6-RqWnjUyCzsbP3nqek9gBZ-0crtX8BkpPbJUlY0Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
‼️
انیس مارتی: بارسا بعد بازی اتلتیکو - ویارئال تصمیم گرفت که خولیان رو تنها نذاره و قراره تا اخرین لحظه منتظر بمونن و اگ این تابستون نشد ، ژانویه و تابستون بعدی براش تلاش کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104627" target="_blank">📅 10:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104626">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/104626" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104626" target="_blank">📅 10:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104625">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHG9HpmFjMFte4ddh0ix6opzSs35AYSYQ192BEzZzObAaYnhaorceERDbWCXOgi7pqEMA6lGplusVXTkvqdCnQlPn-lLgkS4DllSTiJv4Y-Z9VG9414qU-tJGVQr0nUaSEXH0EeOuo-6ynQArEQxi1CYeV3W4R_eXTq9iZio4ltXE5gk_CGNV2GlT1r0sk2o3xSangL6I2txNWvRu1gJk5kXvKYEKPaa-a1NuD2ENT6EoRhsL_ewvWaSLioCo_-ALu2J1WxeuiGIGx_uEJqgcx9mUnloY1L7isoLiz3DPOBsTQS36-bvTIZa7x_5SQ7vhbQE-oyJQnDZrOSKI9xoaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r3
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104625" target="_blank">📅 10:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104624">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/638bfc01fb.mp4?token=GeIB2Yufr5DKOBVNuRgsI30ip426KiE3AOOhRHlHFCR1vo4oAOtW9ChtZoRuxrTY_ltQt253WM4eAjW1S0s2nXv_Vp7vLoMwYSQ0o0GcK6q8iPkDhrhFvukDgC2gFr5eqKhHec8fRZHkkhCtVk7LolZ7dLqRLCzdDhtFfvMwK_dfrBvhmQOOpNFk1ORSTzBaIrF-cKTAif0q8_qg5HzX4kMDLKbV_jastKHPnTlcrFTxDXYyFjMsfE4AzSM7YsLuuiW9t7HAa1TAFySS0v2GXd-IV_OJemMZCfIy38DfAKgdqSvl3xWQ9Pt14s2-cWAylhCtWJ3-v_F8lhrRh5ctgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/638bfc01fb.mp4?token=GeIB2Yufr5DKOBVNuRgsI30ip426KiE3AOOhRHlHFCR1vo4oAOtW9ChtZoRuxrTY_ltQt253WM4eAjW1S0s2nXv_Vp7vLoMwYSQ0o0GcK6q8iPkDhrhFvukDgC2gFr5eqKhHec8fRZHkkhCtVk7LolZ7dLqRLCzdDhtFfvMwK_dfrBvhmQOOpNFk1ORSTzBaIrF-cKTAif0q8_qg5HzX4kMDLKbV_jastKHPnTlcrFTxDXYyFjMsfE4AzSM7YsLuuiW9t7HAa1TAFySS0v2GXd-IV_OJemMZCfIy38DfAKgdqSvl3xWQ9Pt14s2-cWAylhCtWJ3-v_F8lhrRh5ctgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
روایت بامزه داودسیدعباسی از اولین روز حضورش در تیم‌فوتبال استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/104624" target="_blank">📅 10:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104623">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a51e8569ef.mp4?token=IvxCNEmOVjip58ijntPHs-OIIO8eM9lJhaWwMFV_Slagah2EjpYyGqDSSx2NKA3N-F-myN6FEHbp6mLlzuOMCgzcUds-xVfxiRkGSfV6r84LXawpnutdghC77jg8u8Z7xYU2tUgCiiEa9Ttrj_nHh1B1DZY0kXodcqfK30Z561KLHeO18AWht9xb5MmaozwKS6hNBsIvTdnt6sKFw7VDb4YnTYcN3Vm6dSNM9S2WNAl7Tta8uT0mRJ6PG8ssOqU7fgIJXKgvU6oGS2MkRprN632WTOmYJePSXAd_c1Ct3R6ty1nZiL7ioIKws__H87EO1wq4xYhkrvAm2AwBy3REFoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a51e8569ef.mp4?token=IvxCNEmOVjip58ijntPHs-OIIO8eM9lJhaWwMFV_Slagah2EjpYyGqDSSx2NKA3N-F-myN6FEHbp6mLlzuOMCgzcUds-xVfxiRkGSfV6r84LXawpnutdghC77jg8u8Z7xYU2tUgCiiEa9Ttrj_nHh1B1DZY0kXodcqfK30Z561KLHeO18AWht9xb5MmaozwKS6hNBsIvTdnt6sKFw7VDb4YnTYcN3Vm6dSNM9S2WNAl7Tta8uT0mRJ6PG8ssOqU7fgIJXKgvU6oGS2MkRprN632WTOmYJePSXAd_c1Ct3R6ty1nZiL7ioIKws__H87EO1wq4xYhkrvAm2AwBy3REFoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صفر تا صد قهر سیدحسین و روزبه از زبان میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104623" target="_blank">📅 10:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104622">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMKZX33eed5GC_s-IvoZD4TbAi7hDCVnpovSrtbxnp8uPvnkUnulyUF12IEyB4jU9pXQfI458k1iW7wqsyGBreYyd659HNl5cqvqvkJG27VSRTM8Q2CT6MQMgeLP7I9QbwxGvX1CldA8yJUq1cHLIUJuUij0uEbn0Gz4i0mNa8gVHkVbXZ8HYVC9AEiGXMeDhF_JOBv6mDZxQg1IKpA73rnZsjwxRjlr1Z6FBlKX62gct_IMaeL5aD8qSTYNks8pTD0Y7jGu6gHA_FXopegVGb7xPdvyGOTb6yHyrpK5t3JT9GhF8yLQvHPsDEAmy-Z28SbXeFiuTtbc4jWZQ4Gu-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
⚽️
امشب و فرداشب بازی‌های پلی‌آف لیگ‌قهرمانان اروپا برگزار میشه و قرعه‌کشی دور گروهی روز پنجشنبه انجام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104622" target="_blank">📅 10:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104621">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/288552d3bc.mp4?token=IhzB_uoKXLgHOZGvQPE3uSYyuGQittO-19-7KY3vG_qotmsbeaHJ-QbdeGqf8oLsYNFOjLrOFXxCDfXUs6mGfnC5QfR_VP2TB4OJr0rf4uk449JTLN2neOYl9NieTjjyMSwsp1A6SrnxwXdQXfxFBNCESs2_888Qqa8sZJvTn3NQfDK-ZdvjsWdeteUZYtIMcp2NS5AzbFqikdpvvYRr2rkvopCw6sve4zkbeS6OVtXMgswq9VbekMCZM6H7uqmBgmoFxhXjxgLkFNtrXJS-PpPCki5wAWK46t2gT2hywrdFFcU-BhvmkESyFJOKT6zNuYykO-2NdauEJpzNPGF_Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/288552d3bc.mp4?token=IhzB_uoKXLgHOZGvQPE3uSYyuGQittO-19-7KY3vG_qotmsbeaHJ-QbdeGqf8oLsYNFOjLrOFXxCDfXUs6mGfnC5QfR_VP2TB4OJr0rf4uk449JTLN2neOYl9NieTjjyMSwsp1A6SrnxwXdQXfxFBNCESs2_888Qqa8sZJvTn3NQfDK-ZdvjsWdeteUZYtIMcp2NS5AzbFqikdpvvYRr2rkvopCw6sve4zkbeS6OVtXMgswq9VbekMCZM6H7uqmBgmoFxhXjxgLkFNtrXJS-PpPCki5wAWK46t2gT2hywrdFFcU-BhvmkESyFJOKT6zNuYykO-2NdauEJpzNPGF_Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🎙
الهه منصوریان: همان‌طور که با علی دایی بد هستند، با ما هم بد هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/104621" target="_blank">📅 09:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104620">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9080d9bf87.mp4?token=JL8mjrJqhbJBlsbDlfoXqwsnF_hrGMO4EOFLi1bV2l7gXxO4s7PJC2D0_75nAEP078IKkfzAzMCoZML2t-AcDp1txqeqBOeQgiJ3RJzkLG0oh8YbHofAB97Kutb28aitsBiduW_bfq04eT3vur10_ITcNJLR_D04mIDQ6fi8LsuJRgRozuYVASCKO3J3s61w_pQNjQTFdJxQGBSk9tufepPYp1q6jQbqvHySBnld1jbUyZDW2BmVPg7O_j6WthrL_DR-XhvE_7NgNjfDz7-h4cv4RTKGL6VeBMwON06IHAVEuWUErLeMz5nmka-BKSrrOMWbbtWKGGIUC1e3FIWqpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9080d9bf87.mp4?token=JL8mjrJqhbJBlsbDlfoXqwsnF_hrGMO4EOFLi1bV2l7gXxO4s7PJC2D0_75nAEP078IKkfzAzMCoZML2t-AcDp1txqeqBOeQgiJ3RJzkLG0oh8YbHofAB97Kutb28aitsBiduW_bfq04eT3vur10_ITcNJLR_D04mIDQ6fi8LsuJRgRozuYVASCKO3J3s61w_pQNjQTFdJxQGBSk9tufepPYp1q6jQbqvHySBnld1jbUyZDW2BmVPg7O_j6WthrL_DR-XhvE_7NgNjfDz7-h4cv4RTKGL6VeBMwON06IHAVEuWUErLeMz5nmka-BKSrrOMWbbtWKGGIUC1e3FIWqpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محرم نوید کیا مربی سپاهان در برنامه عادل فردوسی پور گفتن که باید به عقل کسی که حسین نژاد نبرده جام جهانی شک کرد ، منظورش با آقای قلعه نوعی بوده ، در اینجا جواب هاشم بیک زاده بازیکن سابق تیم ملی ، و استقلال و سپاهان بشنویم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/104620" target="_blank">📅 09:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104619">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66e469197b.mp4?token=rkZwVdeAArROPyrJuzzYYDr1IKDWeTEzhr7EjJmLDPoBDC2L_09TtOq8YmXOYC5OGqO4WbGLaqibOY5yi8P0Ul3kkTot-L7oJhDwJnth453zP3CXaOydMYqbgB_m49aLJEcNl_mRrcjTRf3PDEWJJ_cbAWnyLxCk17-_U3InxKJmR03EYt_VlxiSwGRzf-QNgU1PCAWOdO6Bt2FtuocSp1Gdv9YiptCHPt4iJBIP1sTBgUrZbENyHPx351VXX50Xf8fB_UE_VHXIJnIL9ZubM2OD8FJDUeUOj8JyTdwgSppTTPRXxE3-SQk4gNxtpGyPt0Ozzr5txiKjrBuiwQILlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66e469197b.mp4?token=rkZwVdeAArROPyrJuzzYYDr1IKDWeTEzhr7EjJmLDPoBDC2L_09TtOq8YmXOYC5OGqO4WbGLaqibOY5yi8P0Ul3kkTot-L7oJhDwJnth453zP3CXaOydMYqbgB_m49aLJEcNl_mRrcjTRf3PDEWJJ_cbAWnyLxCk17-_U3InxKJmR03EYt_VlxiSwGRzf-QNgU1PCAWOdO6Bt2FtuocSp1Gdv9YiptCHPt4iJBIP1sTBgUrZbENyHPx351VXX50Xf8fB_UE_VHXIJnIL9ZubM2OD8FJDUeUOj8JyTdwgSppTTPRXxE3-SQk4gNxtpGyPt0Ozzr5txiKjrBuiwQILlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
واکنش کورتوا به انتقال رودری به بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/104619" target="_blank">📅 09:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104618">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/431f50241e.mp4?token=P5zA-kkd0qXU2i99GaLS7qGvIIZyomRCA7ymMyNfjCNjXqdRYYlFrtBDonudI2mYc3poDcj8Q60osjQgfaRfzQlGnJDfKxfSUuK0sXqD7BZrKSTAbmQNC4DU1Km62JDsU4Z39VkAso3WTL3zVgy9exGqY-oU9OLDIex573EbIzrKDkf7jDCWSFOsz_h70YYuK0mM9_ipjgFRgKa8NyjeyBlG05O4JBYWE_5FtoBOnkrj5nQ18LgKq2c6K7YbiUg13zFwk0CzCn-Z1gextzogca109RJupmSNfSAN8a5BC5E20qdzlOyAIFOaRohuoK_h3UitWbVyAHekubWvusBq_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/431f50241e.mp4?token=P5zA-kkd0qXU2i99GaLS7qGvIIZyomRCA7ymMyNfjCNjXqdRYYlFrtBDonudI2mYc3poDcj8Q60osjQgfaRfzQlGnJDfKxfSUuK0sXqD7BZrKSTAbmQNC4DU1Km62JDsU4Z39VkAso3WTL3zVgy9exGqY-oU9OLDIex573EbIzrKDkf7jDCWSFOsz_h70YYuK0mM9_ipjgFRgKa8NyjeyBlG05O4JBYWE_5FtoBOnkrj5nQ18LgKq2c6K7YbiUg13zFwk0CzCn-Z1gextzogca109RJupmSNfSAN8a5BC5E20qdzlOyAIFOaRohuoK_h3UitWbVyAHekubWvusBq_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
▶️
آهنگ‌ خاطره‌انگیز جناب سندی به نام "حلیمه" که این‌روزها مجددا بین مردم جنوب کشور حسابی وایرال شده. به امید سرافرازی میهن بزرگ ایران و ریشه‌کن شدن تمامی ظالمان...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/104618" target="_blank">📅 02:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104617">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8e39602d0.mp4?token=QI4HWuhIwt1L_YHc7cCRq_w2u20y-Hw_xJyfUHFxwI-0-eQHBdQfKDqAClThwMu5JYFT311ku0w-dTB0ZBnK1CbahasuDTFwawJ97GH8zRhcCFr-z6kifTeIzfbMipEXLNCvs3hn1813O59WjMwTtDdUqll4G-0_8tXS2Myfh-dWDaHrMtOLVSThV2FbPAAzf7-6qX3luPYvFaKlwEM2u3L38cTBM8m4SENp9ZNVQxLCzeJAf8ZeBYM-JxuBGT5R7pm8bELyqHezc-SRUY3xLn3hS7VQ1zQAPHtq09OzDBA9N0xBztYcIb6Men9eh2fv9R_ZUFIlqqJ5_fQar_m9n4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8e39602d0.mp4?token=QI4HWuhIwt1L_YHc7cCRq_w2u20y-Hw_xJyfUHFxwI-0-eQHBdQfKDqAClThwMu5JYFT311ku0w-dTB0ZBnK1CbahasuDTFwawJ97GH8zRhcCFr-z6kifTeIzfbMipEXLNCvs3hn1813O59WjMwTtDdUqll4G-0_8tXS2Myfh-dWDaHrMtOLVSThV2FbPAAzf7-6qX3luPYvFaKlwEM2u3L38cTBM8m4SENp9ZNVQxLCzeJAf8ZeBYM-JxuBGT5R7pm8bELyqHezc-SRUY3xLn3hS7VQ1zQAPHtq09OzDBA9N0xBztYcIb6Men9eh2fv9R_ZUFIlqqJ5_fQar_m9n4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
سخنگوی سازمان‌لیگ: بحث قهرمانی فصل‌گذشته استقلال هنوز مطرح نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/104617" target="_blank">📅 01:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104616">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8c7133cd.mp4?token=uJOp69M_98cSrTHTOSzxDUCx07I-c97mz53pSFhMkKLM0xdyaYFJgFZZEOUQrJCrYnIuFwF5CuENzKM52ES9FLpHn6Awcb_6foKrvUyjF51r0baPfHInnj-JrfRWVKldOULvprWBN-y4ZquqGq-cSoZL_zHF04p5sarvvsdIRAdCWF7a519nyhdm_HMZDLK1ZsBzdCkGpXSe5oxsYQ7kPqEUw6EITT7qJaoqF0nEP6bBdvKNz8Qp8oyT5yhlRT-WFhKy2kc4xoqbc46F3RDDQIyK4_XR2s82bfk69QHDk6FEIp73V8tgKz92aKZZF8xD7m1eVPxL5YysphdXwy_AHjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8c7133cd.mp4?token=uJOp69M_98cSrTHTOSzxDUCx07I-c97mz53pSFhMkKLM0xdyaYFJgFZZEOUQrJCrYnIuFwF5CuENzKM52ES9FLpHn6Awcb_6foKrvUyjF51r0baPfHInnj-JrfRWVKldOULvprWBN-y4ZquqGq-cSoZL_zHF04p5sarvvsdIRAdCWF7a519nyhdm_HMZDLK1ZsBzdCkGpXSe5oxsYQ7kPqEUw6EITT7qJaoqF0nEP6bBdvKNz8Qp8oyT5yhlRT-WFhKy2kc4xoqbc46F3RDDQIyK4_XR2s82bfk69QHDk6FEIp73V8tgKz92aKZZF8xD7m1eVPxL5YysphdXwy_AHjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
از حواشی بازی استقلال و سپاهان که حسینی حاضر به خوش‌وبش با روزبه‌چشمی نشد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/104616" target="_blank">📅 00:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104615">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBKnbHvPoEV2PjQiL3wsKekMr8QPp3uOZlOvlrYW4jRVbXh7ux_49UeVAWgQN9HM24G0lSi1CVwYUXjkVsy0oRve17V7MfoCLOWTqNjD_GLwAt02CpSfysrK6KN2du2XUYWlSwMeVIXXzc6EQETlaXpAS731U6bRV8BEHZqNYfbTB35v-RYt9aMAaqhndKHMCKG4vDXchTwgsSS2JWQjyGytx9_RdKBLPkGOaBWqE1ySuLL8QPSfwqHcvuMQoTP6rCXUplu4uz3fHgaYXA0_LeYdqYB7P3nFYhKHQ9fWOUuQjV6XYosFsWkFWx2_Is9nwQOgWPy9hD6V5fAMhS5zAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌اول لیگ‌برتر فوتبال انگلیس؛ غرش شیرهای لندن در خارج از خانه؛ جدال سرمربیان فصل‌گذشته رئال‌مادرید به سود ژابی‌آلونسو خاتمه یافت
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی
😆
-
😀
فولام
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/104615" target="_blank">📅 00:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104612">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d62852b4d.mp4?token=Snlp31mFJAoaa9Do1NN9YExDAhzQFqz0dT7skU7mI71UcD5FWYLa2ELPRg7Fa6tueAovVZIWt0NXtyhNyN4o-K1cXcSybh9DTSSo5pn0K7vXp7bTdNDStVvZpWxyIAHR-sA10IcwjTP19-uCkm1NFLLvIRa7JPPDHPgvqR5zeSnBwOI0tBd7_Libf61ki3VTNXL13mXdMyluuZ3IIYlbQ-zu_OEuOKPzSZORWndEkV05wXfWKHFmCukf3uKp260JjqhTx6KfCHZCZHxSB1rr49b8_8RvxK7TRbVmD6-7zjM6wLNqrPJ0LR3loyAygM3SIK_00jaeBUnsnbVhagX2tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d62852b4d.mp4?token=Snlp31mFJAoaa9Do1NN9YExDAhzQFqz0dT7skU7mI71UcD5FWYLa2ELPRg7Fa6tueAovVZIWt0NXtyhNyN4o-K1cXcSybh9DTSSo5pn0K7vXp7bTdNDStVvZpWxyIAHR-sA10IcwjTP19-uCkm1NFLLvIRa7JPPDHPgvqR5zeSnBwOI0tBd7_Libf61ki3VTNXL13mXdMyluuZ3IIYlbQ-zu_OEuOKPzSZORWndEkV05wXfWKHFmCukf3uKp260JjqhTx6KfCHZCZHxSB1rr49b8_8RvxK7TRbVmD6-7zjM6wLNqrPJ0LR3loyAygM3SIK_00jaeBUnsnbVhagX2tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
👤
🇮🇷
#فوووووری
از علوی سخنگوی فدراسیون فوتبال:
🔴
سرباز شدن علیرضا بیرانوند؟ تاریخ بازی کردن بیرانوند تا 31 شهریور در کارتش که در اختیار سازمان لیگ است درج شده است و بعد از آن سرباز خواهد شد اما اگر نامه دیگری بیاید این تاریخ می تواند آپدیت شود و بیرانوند تا جام ملتها می تواند در تراکتور بازی کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/104612" target="_blank">📅 00:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104611">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZtA5CQ4f37-z4kelpbkGNiWNrhzabt8YJi4xXSWsuU33Kc6yktR4TuRJ-22rV98iUTIZEj7Lx_LLPWk9JlX9Tq-xhYzPlVYV_JvvQCQ-Av1sMx2qw--eacmK9dh-eUanunI8t6b9iHUGhZ6AKvaZat4RuGGH_7Vl8UKV6CwoJsrKylT4JGGD4AqVG5pJhCJrwo9RBPS3bOdwi65kgzU2G8Au0IpO1yGd8Ty7UhdQIDHbo9l-4WrCq_u7czMM8i2glm-qppF2QLhmAg_NX8ggpa4c1i7MDTQOyXkoee60nAFVFISHlds9ov97gRJx2VWOc9njCVs5ojmtKvgj6w9Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
📱
انتقاد شدید جواد کاظمیان به عملکرد تارتار در بازی امشب: کمر پرسپولیس رو شکستی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/104611" target="_blank">📅 00:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104610">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5710ee96dc.mp4?token=ItQYsFL-BdCKod-FZK15udzBr4zhsVlNqw6XtkSm902NspLI-aXY19u9x0PH-HfdHnmiq-NoSZ3Owr1XT8HrLDvcvSdaQQtltlQPCmev4fqoUMw5qFx3rA5NyBi2OYol5-loZKOIKjQQc2F0zNmsDrtwAeVaR3GXwB4amBI2XU8laL5rL9hft9qjBdnFXocXX9SPUh5bd6XF5SUFxcf7r2JjMKsbDFq_zJbQ6uY_XhEYH6SKRfIwFlkCQ1BhsgniG9-htdMx5Yl4dxKFMSGm2u2Bb4QYHH8FDhiKivc_0g4Dcji8jbQMqvWoZZet9V8EFZ2im_EmGxMdhlYtktAYFglHXnBNuY9sqkiKeP1vskr8qQCTvh0-Nka9NF0Kbsd2nRTjBzjRZBnLjtRkcQRL9IyNgbE1x1RNHM68CnpHxUfgthR2D0qj7yVARdmLEfskgGhNli1_p8l1vastdzvbIIHbgNUK7W5ge0IO4I5ByFmsQ_ovsSNmRULzSLn0gFSa2nYd-8NlPItb7b7bgIBk9Hmgc0dcBkuVyfWuoA52HhqbQfV53mSxRcwL92_vSrMgOnySPg5WYu53wQcOYMSKCOTS-CgyadenUqJ0aGS4PA_2WjpqdmxVf_CHcVOYM2Oib47X7IqgnwhSfZLK_EqbOHwzJl4ijBRtyoz7remYKls" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5710ee96dc.mp4?token=ItQYsFL-BdCKod-FZK15udzBr4zhsVlNqw6XtkSm902NspLI-aXY19u9x0PH-HfdHnmiq-NoSZ3Owr1XT8HrLDvcvSdaQQtltlQPCmev4fqoUMw5qFx3rA5NyBi2OYol5-loZKOIKjQQc2F0zNmsDrtwAeVaR3GXwB4amBI2XU8laL5rL9hft9qjBdnFXocXX9SPUh5bd6XF5SUFxcf7r2JjMKsbDFq_zJbQ6uY_XhEYH6SKRfIwFlkCQ1BhsgniG9-htdMx5Yl4dxKFMSGm2u2Bb4QYHH8FDhiKivc_0g4Dcji8jbQMqvWoZZet9V8EFZ2im_EmGxMdhlYtktAYFglHXnBNuY9sqkiKeP1vskr8qQCTvh0-Nka9NF0Kbsd2nRTjBzjRZBnLjtRkcQRL9IyNgbE1x1RNHM68CnpHxUfgthR2D0qj7yVARdmLEfskgGhNli1_p8l1vastdzvbIIHbgNUK7W5ge0IO4I5ByFmsQ_ovsSNmRULzSLn0gFSa2nYd-8NlPItb7b7bgIBk9Hmgc0dcBkuVyfWuoA52HhqbQfV53mSxRcwL92_vSrMgOnySPg5WYu53wQcOYMSKCOTS-CgyadenUqJ0aGS4PA_2WjpqdmxVf_CHcVOYM2Oib47X7IqgnwhSfZLK_EqbOHwzJl4ijBRtyoz7remYKls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌سوم چلسی به فولام توسط کول‌پالمر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/104610" target="_blank">📅 23:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104609">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f61c2bb38.mp4?token=gYuDWroX3q245HZMg__en58ekYsnkcw1vjEaHyzGukb_k6MrTDgQwa42n-u1QRFo-p2Fc_Bf_yBczoaNGzb97d3vx1rxZDpM3iXZCdr5zyyUB0nsmVvn0PUFSX9GV51KPP-Pk7uE9Kq3j9vPi6cK7TF11qP_mI2KLfrTmKCGTPN6dB1zPdNEv7dzDHc7X898L0EcaPUO1YYymObHixy01pZy9LRQGPzmcRX5mvLmZur1V4QaocuypEiXOhVCaj_JvZ9KNGzcVNYaNVUpO0EusOWfj_se3MxoOd--3xC_SXbVIvs-64Qa7Px82oPgkc6ujoRH2sDHuPAWpUolLJXJ0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f61c2bb38.mp4?token=gYuDWroX3q245HZMg__en58ekYsnkcw1vjEaHyzGukb_k6MrTDgQwa42n-u1QRFo-p2Fc_Bf_yBczoaNGzb97d3vx1rxZDpM3iXZCdr5zyyUB0nsmVvn0PUFSX9GV51KPP-Pk7uE9Kq3j9vPi6cK7TF11qP_mI2KLfrTmKCGTPN6dB1zPdNEv7dzDHc7X898L0EcaPUO1YYymObHixy01pZy9LRQGPzmcRX5mvLmZur1V4QaocuypEiXOhVCaj_JvZ9KNGzcVNYaNVUpO0EusOWfj_se3MxoOd--3xC_SXbVIvs-64Qa7Px82oPgkc6ujoRH2sDHuPAWpUolLJXJ0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
🇮🇷
🇮🇷
استوری طعنه‌آمیز و فوق‌جنجالی علیرضا بیرانوند
پس از برتری در بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/104609" target="_blank">📅 23:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104608">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/19774d8b5c.mp4?token=Ue8wbCYBXeFnsZJcCUWe0hemJLRIZvaQLcZ0LWSIBtTqMuHEFxDKNVJfeREK7H20470dsW8zFtYz4PPhlo9kVh6GQuL0NJzR9kyyKtnf1RJX_O1r2L3TSTdUeV1VPZNWfqYAmmd1Nz_1Wet8Q9KVr-90DTR3dxtpE_TNhSYQ3GB5OBLbYe5KjYXPLvj0Pk1awvoLkY_oAEY0CJbFJyOxPEQE95oMBTqUy1fwHbQeGwzjNWHqASl8Q9Mb2xERcmGorh4q3LRGj4eM675FB-zCSIkOFKLOTiBXa9Tlti2oG1i6n_8ujO_PcHdMmMjcBQnD00s-95fSwkd5ohpVXZmiQgrqF_IveQtKO1GIoeHnfey6GfjqsTphso2AWsm3JkGyVECf1JYUDTJ5MTaBhBFPHfwJx8v4PRHDpYmy3IsQFwqlgWDePasjZNzdGsM22uUkfsvgEuq0j2js5V5MyV4rryZDjklbMG3XiBkRfVaNeW7mWgK5wPBf5SNCxIVDjGrH7OUje5bDRbqwYc5Ua4eOEzrHYQrg3Tl0ar8Xa_iV4t_gyTcIOwCXEzBT_yng5m9QpMoDjhjqnhEf6NObLRAqdO9irgLnERTmBWwKfYLy7AhGQ0UdxNU_VfPuZtullrAG6TXAO_zJQo2MwOGP7B2cFLahSKP1D_D4DqF3dQjcfX0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/19774d8b5c.mp4?token=Ue8wbCYBXeFnsZJcCUWe0hemJLRIZvaQLcZ0LWSIBtTqMuHEFxDKNVJfeREK7H20470dsW8zFtYz4PPhlo9kVh6GQuL0NJzR9kyyKtnf1RJX_O1r2L3TSTdUeV1VPZNWfqYAmmd1Nz_1Wet8Q9KVr-90DTR3dxtpE_TNhSYQ3GB5OBLbYe5KjYXPLvj0Pk1awvoLkY_oAEY0CJbFJyOxPEQE95oMBTqUy1fwHbQeGwzjNWHqASl8Q9Mb2xERcmGorh4q3LRGj4eM675FB-zCSIkOFKLOTiBXa9Tlti2oG1i6n_8ujO_PcHdMmMjcBQnD00s-95fSwkd5ohpVXZmiQgrqF_IveQtKO1GIoeHnfey6GfjqsTphso2AWsm3JkGyVECf1JYUDTJ5MTaBhBFPHfwJx8v4PRHDpYmy3IsQFwqlgWDePasjZNzdGsM22uUkfsvgEuq0j2js5V5MyV4rryZDjklbMG3XiBkRfVaNeW7mWgK5wPBf5SNCxIVDjGrH7OUje5bDRbqwYc5Ua4eOEzrHYQrg3Tl0ar8Xa_iV4t_gyTcIOwCXEzBT_yng5m9QpMoDjhjqnhEf6NObLRAqdO9irgLnERTmBWwKfYLy7AhGQ0UdxNU_VfPuZtullrAG6TXAO_zJQo2MwOGP7B2cFLahSKP1D_D4DqF3dQjcfX0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم چلسی به فولام توسط مورگان راجرز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/104608" target="_blank">📅 23:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104607">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a39f5d717.mp4?token=ScOT2NLrspDLhyCC0IH0Lr5aXZaeK3K2tFV62Qy-P5aot6gXFaBdJUgwKRKl0Fp44R-LVbeaUeguT632-3ljPG8-3iD2g9HMxqwI2Q3xkMHpLG70ZW_R_xhnNd23BPoDiHKEfX4-t7uEa47HncNLcs11s29AqO9aWKh00Y5t9pQSJB5KdIzLds8_4oAmv6OYGl88BvIwvZRL90cG5KUh5Th6C8Iy1Ul_zIxOexEppMukiVWlFaLkSNPRW0VAapOFjZ3ee-v1sMvmbGlmJSbkvyH-RqfLMTsR8956bXje3bOExjk-7g9uJS11EvLW_0oXBEc4I-KvRBJuOXVBQtF0mKGw5SE8AqSiqGc1uDWlwMvGwzxmUm2J7atxEHO16sj1YsenCVSP2msulG8QRcaL8VDM1_Xg3LnHavmiT0ggsbmif4uJn_Kcb37YWJW22pRQPQ0AzZUtEEGXhx3vkKBHkvPMuxUkmKhRbtMib60tAcp8xl9sbb2F4Jx5Ih4wAt4QHqcGHE5L4PUR3xA3BG7hUHTFEMVItc7LPJANrqOBRy-_Vt7haektmsMA5aBBDOpuZB2gWKqPI0eOBY7JoPUgY1eSCLtfKwRYPy9nF3vMZy99YWeOI3uAHebJI6OtpZr7LFs5J-FzUTUf2neN74R8ExhqhTEjs3aF1_t2XWdXZ6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a39f5d717.mp4?token=ScOT2NLrspDLhyCC0IH0Lr5aXZaeK3K2tFV62Qy-P5aot6gXFaBdJUgwKRKl0Fp44R-LVbeaUeguT632-3ljPG8-3iD2g9HMxqwI2Q3xkMHpLG70ZW_R_xhnNd23BPoDiHKEfX4-t7uEa47HncNLcs11s29AqO9aWKh00Y5t9pQSJB5KdIzLds8_4oAmv6OYGl88BvIwvZRL90cG5KUh5Th6C8Iy1Ul_zIxOexEppMukiVWlFaLkSNPRW0VAapOFjZ3ee-v1sMvmbGlmJSbkvyH-RqfLMTsR8956bXje3bOExjk-7g9uJS11EvLW_0oXBEc4I-KvRBJuOXVBQtF0mKGw5SE8AqSiqGc1uDWlwMvGwzxmUm2J7atxEHO16sj1YsenCVSP2msulG8QRcaL8VDM1_Xg3LnHavmiT0ggsbmif4uJn_Kcb37YWJW22pRQPQ0AzZUtEEGXhx3vkKBHkvPMuxUkmKhRbtMib60tAcp8xl9sbb2F4Jx5Ih4wAt4QHqcGHE5L4PUR3xA3BG7hUHTFEMVItc7LPJANrqOBRy-_Vt7haektmsMA5aBBDOpuZB2gWKqPI0eOBY7JoPUgY1eSCLtfKwRYPy9nF3vMZy99YWeOI3uAHebJI6OtpZr7LFs5J-FzUTUf2neN74R8ExhqhTEjs3aF1_t2XWdXZ6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🇮🇷
❗️
درگیری شدید هواداران در دربی خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/104607" target="_blank">📅 23:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104606">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e7c831cb3.mp4?token=YZSYe054L888Cn-_KMFE-4q4sFHlfDWMHkBCGzQB5XI69fbJt_VSQ16ojSvfwTVCKD1X6ctpkO1BfzY3qO-CJjsCR9uLAolRa2nqhj36QBAWpFgE9xnVtg5yYIAkDk1p77ZQ7XasY4PH5C5A3YT62N-x3rqkY5qj4cJYCrwYEXOJBOZ0KoIqkRUzjTySKMoFJWrxSK8w3HYlXrMQGlQ35HSh8icj2Q5RGIazdPem3XOf-xiDdLSfgIQXnX8OcGaVglDg0vwqb6eaxIy9YdE3IpBubV2gMWPOGRnbd8X4k_hrtjF8kYfIBD_wveEiKccWTVNFnj11vnT1rpPgAInbfg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e7c831cb3.mp4?token=YZSYe054L888Cn-_KMFE-4q4sFHlfDWMHkBCGzQB5XI69fbJt_VSQ16ojSvfwTVCKD1X6ctpkO1BfzY3qO-CJjsCR9uLAolRa2nqhj36QBAWpFgE9xnVtg5yYIAkDk1p77ZQ7XasY4PH5C5A3YT62N-x3rqkY5qj4cJYCrwYEXOJBOZ0KoIqkRUzjTySKMoFJWrxSK8w3HYlXrMQGlQ35HSh8icj2Q5RGIazdPem3XOf-xiDdLSfgIQXnX8OcGaVglDg0vwqb6eaxIy9YdE3IpBubV2gMWPOGRnbd8X4k_hrtjF8kYfIBD_wveEiKccWTVNFnj11vnT1rpPgAInbfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول فولام به چلسی توسط جاشوآ کینگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/104606" target="_blank">📅 23:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104605">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/49528cc115.mp4?token=eV07gTCZHjTPipSn3Udck2_HcgMyQKnVbJam3oGCYaSnBzHFB_w61e-a-OcZjUI9OFh5cO3lZliXioKj-R1Gpm8xZbhIQfWRiQd906ErzRcUyBPwCYGXlBr1gJDIgVwwAzOjPf4vAkRMOeWsB4c2ea9_euxmaZNWZK-VoquNGMYSrgjfFemm6p1-nKuPaoKj59NaRgBBzinfUzZD8KGHfRSIIBYFfcNPvpH_ATDLOMbBU61Bbgv5Y_PBmOVrZIb580b_m1_ZQdqHsPI0J6uKXupSBPxEPY_1jcIVG9vsWqpPjWrc0606fhevOPo0i9-ygMJvidurZC_8GWGdMF8xoFqCcVvGRdQaQ6OeczakKbi-KgTWi82Etjf7VHuOeDMKJu_Tkrwd2vq6xSiPDvXOLQr6r4wA33XQGc11tzgxhNYCFfTIyqi5qnYjSTzTp9E8vXiqkQuxIDgPddgOliZ2XQKQeFW2Rfvec8SkGKOzH5iSA_HOtkvL9LpHxYd4Nn8muvwmWhuG15HDZoTsEEkqW-Nry5Ty7me64JVRLTTCM2jPk4CkaayExaxyJk3TsSo4tIjU9Jz1YwHyoDZci0wAq_gni-aPapEOD5vdV7OfJJtQJkqrfHXRaE4720IyV1JK0ABkCtaarobqvPkFnP_hb_VW7upn_qtcdlbNZb8hEpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/49528cc115.mp4?token=eV07gTCZHjTPipSn3Udck2_HcgMyQKnVbJam3oGCYaSnBzHFB_w61e-a-OcZjUI9OFh5cO3lZliXioKj-R1Gpm8xZbhIQfWRiQd906ErzRcUyBPwCYGXlBr1gJDIgVwwAzOjPf4vAkRMOeWsB4c2ea9_euxmaZNWZK-VoquNGMYSrgjfFemm6p1-nKuPaoKj59NaRgBBzinfUzZD8KGHfRSIIBYFfcNPvpH_ATDLOMbBU61Bbgv5Y_PBmOVrZIb580b_m1_ZQdqHsPI0J6uKXupSBPxEPY_1jcIVG9vsWqpPjWrc0606fhevOPo0i9-ygMJvidurZC_8GWGdMF8xoFqCcVvGRdQaQ6OeczakKbi-KgTWi82Etjf7VHuOeDMKJu_Tkrwd2vq6xSiPDvXOLQr6r4wA33XQGc11tzgxhNYCFfTIyqi5qnYjSTzTp9E8vXiqkQuxIDgPddgOliZ2XQKQeFW2Rfvec8SkGKOzH5iSA_HOtkvL9LpHxYd4Nn8muvwmWhuG15HDZoTsEEkqW-Nry5Ty7me64JVRLTTCM2jPk4CkaayExaxyJk3TsSo4tIjU9Jz1YwHyoDZci0wAq_gni-aPapEOD5vdV7OfJJtQJkqrfHXRaE4720IyV1JK0ABkCtaarobqvPkFnP_hb_VW7upn_qtcdlbNZb8hEpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول چلسی به فولام توسط ژائو پدرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/104605" target="_blank">📅 22:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104604">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L57WPhhabREphklyFAJgcMdbAwAEvS1aMfhPmyt6AVZj7k3xW_NTlDynkb0vlTr74EEnv7KHgJO-lFrQeob2U9ZZBf5PF667ltHF1I0QuTYrc7v7KFR-a-vPsEP0uSUPeOEEqpdllzkmhEbFF17EaG2BdXOtMeetX_ZlRjr21vqg0FTzH2CwJ1VH3gYh9KhQ-Yq5k7n8Bw9nBhmNFwbd_eO5dSm3x-yP5sfbeoSmjGyXJsn51cu7RlAD5zqVOC9EIOKdrGijyKQ9tRDjIlYNI7zGjDGjGNoTcDnYxStDmpCJanIbJcv6zxMCiufQdnCb4pptkVB6cWIPBXbIiL8WQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
نتایج‌‌بازی‌های این‌هفته لیگ‌برتر فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/104604" target="_blank">📅 22:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104603">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b217109864.mp4?token=mRb9wTf8xR6TbXQ8rNCWsGPVvX5deU41Y99JQXvNY-j5-m3r6__ZXbvC7rU8PBeygompVN_hkQVIyJp2e1XTt1FfFEer6UZliqDW3Nj-86rd6dIZW4lCOtx8H-CXS76iDCX4KVOR3I_x2kaEcGAMGhhspPIUxH6iqf8sD_8UMCl240PyMIyf94gAChPOhDb2TfpHE33Dsl-WAx-QOLuws-KF7CCIt3UofeBlQNDBED7bA9CYyZqhCEfjA6I0IXRKgy8wo428HE6acc9g9ypD__cgpXenn-2ZfluzsL4uUOPqzsgLHEYD0kwyw_Gs5YnNU_Lb7ntQZV-xTigLTHXYj1170HNS4CNkI0Bqin9q3siAbMrHYuVPN5gMJ9ke9kAhFS9bDkDNjXppF1o9ow863fLdvOpxxFJrkKN0JGwj7BGa7V0X7cmISCaAKnB_Qz7m9lbawL_iA6Vm-EQG6kZYaLLVu74nsyTLK8DjYFvmRUr7O88ta9T7rMD8ulgcd___xs_bPjmOUGR5IILfkEos8OB5B9URghEtnG6P0p1Fq0bu7azhz3j-lFi_xHQYJegCriwxf9GO2MEUUrT7jP7vGkw5-8SIX6UHuvSblDA3zx0eOKz5PCbSWYR6IaqO6ipRClWQDPffOeOWX1tSVG2HNad97BJNQzMCB2iG1oajIXM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b217109864.mp4?token=mRb9wTf8xR6TbXQ8rNCWsGPVvX5deU41Y99JQXvNY-j5-m3r6__ZXbvC7rU8PBeygompVN_hkQVIyJp2e1XTt1FfFEer6UZliqDW3Nj-86rd6dIZW4lCOtx8H-CXS76iDCX4KVOR3I_x2kaEcGAMGhhspPIUxH6iqf8sD_8UMCl240PyMIyf94gAChPOhDb2TfpHE33Dsl-WAx-QOLuws-KF7CCIt3UofeBlQNDBED7bA9CYyZqhCEfjA6I0IXRKgy8wo428HE6acc9g9ypD__cgpXenn-2ZfluzsL4uUOPqzsgLHEYD0kwyw_Gs5YnNU_Lb7ntQZV-xTigLTHXYj1170HNS4CNkI0Bqin9q3siAbMrHYuVPN5gMJ9ke9kAhFS9bDkDNjXppF1o9ow863fLdvOpxxFJrkKN0JGwj7BGa7V0X7cmISCaAKnB_Qz7m9lbawL_iA6Vm-EQG6kZYaLLVu74nsyTLK8DjYFvmRUr7O88ta9T7rMD8ulgcd___xs_bPjmOUGR5IILfkEos8OB5B9URghEtnG6P0p1Fq0bu7azhz3j-lFi_xHQYJegCriwxf9GO2MEUUrT7jP7vGkw5-8SIX6UHuvSblDA3zx0eOKz5PCbSWYR6IaqO6ipRClWQDPffOeOWX1tSVG2HNad97BJNQzMCB2iG1oajIXM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
‼️
مهدی ترابی: قهرمان آخرین دوره لیگ برتر ما
هستیم؛ حق تراکتور کسب سه امتیاز بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/104603" target="_blank">📅 22:05 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
