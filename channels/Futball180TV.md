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
<img src="https://cdn5.telesco.pe/file/gNNVh2833jllNBAAH0LtGceiQcALpzka1QtHFEjyV2-vEJydTmamlHEyCM4cWvCzGzfPZROuz29eXgqDhzrBDAt_EeGVWUFJ8Za8-uBiExI8_oaAaS-DnjZaOIzumN-DCI8oi03mS2fymuFA_itAzKqDNGDXc_gqKbPNJ97heZ03tq4NhSQeSIbiTVDDfY5zFnA0rCiu1rxZWfvx4R58G-ntJbB02j5ev6sxDuG4UWiOAGa14KOcQ_U6cd5ywP5eugl11OuUwU-1Gou5u1SU1lMuids4XdZz5x1tlNWe9XIVGe72ueAJz3MotP7TDt1YyIjtK3o6D3hrIgu5Mr0OiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 514K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 02:31:12</div>
<hr>

<div class="tg-post" id="msg-92786">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3tTDv5HAAmZtYr8SLUnorpXO1ZIlxLi2ZRnz6eGzpyrotwz1BmXTMqFYos-WWXnt7OVEySzirrTaFgMkHxqLPfcKWHWXM9cOeh0AcDWrF0VoyVD6dOMEtkTTU4mpgyJXNP2U2CzjbW0-qsMWmtTOBjRdiNc8PgJVEi-QgkvyhmtV2xMqfB1-ntOFCG0-gxw4fGSc99idq2q7htFNN-qo8L1Q3ctmM2z3uFMAmY5vRWZjpFfUM15V_kMBpFTx9Vi0LRmTzGicJK6kU3cgMg9v7_O8z27dgMAPkyPhRZ7XnEL_S7DFW6arspY7mdNwP2X4qbfnrpW3kWg_pBdJcuD9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/Futball180TV/92786" target="_blank">📅 02:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92785">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kh1kez6hGCrUV49gWjUmX8yv5z3jWU9qKEVnZABKI--N11wOllQfWiiuitV0Qy-MWBsVyQeAg4FY0EN0D3E041Zug4dancliY9e2PqYRzwekGWC_4i9CQfCxNcUrdI7nDogiCle6JWb684UENApCcjM5_xvzMeRx-THWdjADkGSqq_ZYfTHAnWNzJUOS8Gvbo2ACrvjsX5vE-G5Yrruzze6_UnpN0CuAri6FY1PtDegKkZ4dNZOfdmmWyP6qAMq9U9CwxratfTD6Uq2zYqWFeoGvrMSVjWU5lI7FBzE-np2aVtezWw-j99Zu3xNiCmMktsRUR8qtE_q3L8tSwr8qrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار وینیسیوس در جام های جهانی :
5 بازی
2 گل
2 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/Futball180TV/92785" target="_blank">📅 02:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92784">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🏆
پایان نیمه‌اول؛ برزیل
😃
-
😃
مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/Futball180TV/92784" target="_blank">📅 02:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92783">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سوپر سیو بونو نزاشت برزیل دومی رو بزنه</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/Futball180TV/92783" target="_blank">📅 02:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92782">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">برزیل داشتتتت میزدددددد</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/Futball180TV/92782" target="_blank">📅 02:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92781">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/Futball180TV/92781" target="_blank">📅 02:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92780">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ایبانیز هم کارت گرفت از اون بازیهاس که احتمالا اخراجی بده</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/92780" target="_blank">📅 02:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92778">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwGEtrgBI178E9xFjo5Csls_q3Du1vFo_oWANyQTllkp5ZtDdLLHKCLyoCzpKW126kybU_RHj2A58W6zIrsg_yhBJCbt_ZAUM-FFQf2agV4U_rgLyuV-5M-6FenKmhss8IwOUjwNm3unQnhNi_t5pPoLBEDSA4UJdYY3ai-DiaMhcBZU3DHGb0AI9E2R9T5pmulXwJpuDS_sYrebXYq7I2jrNeoaS5VuPSbS684FYUty9PzlBZBPZCoeQcejSs0xk9TammlX3044LYSVLDh6bsRdDNyVY_93-Ea3lL3BYtJH6Z9YPjWRGpUO-XQrYKwOyTMXqh7DErKSljmaYBY3Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
گل‌اول برزیل به مراکش توسط وینیسیوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/92778" target="_blank">📅 02:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92777">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کاسمیرو کارت گرفت</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/92777" target="_blank">📅 02:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92776">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f79c357bf.mp4?token=YQaw2FZ5IwRnK5s5riVJkwvbZX6eSEiV_JZpSggLxCVsI4feyYDt3Wg4uqpybXqeIGYJ_sReKj7dDIEqIfiZWi-rI-1LeCYQMuxJ-ey9pjREtlKqzKKC26gb-h8twCBMkm_rnEJykMwHV7hMGjThsxEeqEkkYb26TYgKChAys3w55ngD-tNHtahH0eUvKO9rZqtBR4CfzJcReGA-fF2C3TI_hHPCwpaoC8iRzduL65TFSa0djbroY5mh4LjM7DybaHE1N2hWqcHyddpjNdE94g8IILEnETgOnQ0bQnWQ-tfr_fXrju65jxLn2Yhq4cuzKCenOxEgQJcUtZ1s5e4xKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f79c357bf.mp4?token=YQaw2FZ5IwRnK5s5riVJkwvbZX6eSEiV_JZpSggLxCVsI4feyYDt3Wg4uqpybXqeIGYJ_sReKj7dDIEqIfiZWi-rI-1LeCYQMuxJ-ey9pjREtlKqzKKC26gb-h8twCBMkm_rnEJykMwHV7hMGjThsxEeqEkkYb26TYgKChAys3w55ngD-tNHtahH0eUvKO9rZqtBR4CfzJcReGA-fF2C3TI_hHPCwpaoC8iRzduL65TFSa0djbroY5mh4LjM7DybaHE1N2hWqcHyddpjNdE94g8IILEnETgOnQ0bQnWQ-tfr_fXrju65jxLn2Yhq4cuzKCenOxEgQJcUtZ1s5e4xKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل‌اول برزیل به مراکش توسط وینیسیوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/92776" target="_blank">📅 02:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92775">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">لبم به لبااااات وینینینننننییییییییی</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/Futball180TV/92775" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92774">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">چه گلییییییی زددددددد
😐
🔥
🔥
🔥
😐</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/Futball180TV/92774" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92773">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رحمت تو کونش عروسیه
🤣
🤣</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/Futball180TV/92773" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92770">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وینیسیوس
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/92770" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92769">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گلللللل برزیل بازی رو مساوی کرد</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/92769" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92768">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">برزیللللللللل</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/92768" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92766">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oYekJ7lZW1nGAFn9mkR1sCjWPKvWc3c2kXTDgjWjQ991t_OoEDcSjnxjUCMWGnQRjinKpVoEDSO5vAYY8WPW0UVQ5DGCw6rufhf0zkrnIFLo_mF3c_dCwkatV2kuE5QT-Moell0rRaFUMPHu8bqs-y4KNCTb8AgLMBuOfXLnADoUlqulpq6XNE-q2hzLToKvv0qua6YsBuY9CzMCTZViKCQ5QBIbYSFu3WlMXo3lbnkFJ0JEtY9vY5yLeC-PnUe6dTZdlRQ7sxf8zk1bVl1gY4oqzcdzWImP5BLIU612jImctObHacF7E0sS-Z_ijWACwMtDvJrH1fT-TKz_y4JBWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتشه که آنچلوتی ابروهاشو بده بالا</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/92766" target="_blank">📅 02:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92765">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وقت استراحت یا همون کولینگ بریک</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/92765" target="_blank">📅 02:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92764">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🇩🇪
#نقل‌وانتقالات|بایرن‌مونیخ بدنبال جذب اسماعیل سیباری ستاره فصل آیندهوون هلند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/92764" target="_blank">📅 01:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92763">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
گل اول مراکش به برزیل توسط اسی سایبری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/92763" target="_blank">📅 01:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92762">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وقت استراحت یا همون کولینگ بریک</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/Futball180TV/92762" target="_blank">📅 01:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92760">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/81f3af91f3.mp4?token=Hrd7Jr6yR3dZnbUkBMzGhPpAB0EVxg6rDc4hHW7yvcGSBtQnoBxIfuCdVoWDunzZp9tYhuco02oL_dOcqcuGmlR9GQLu86uNRFb287C_Nvqa7e0j_CmO35hXmdlr043Xe-OXMpGCQLqxpxQakQbYlWqfeYp9bjA6Nji5tSoVD7_L9P21xVDXVZRfhNQiZGHGwGmzHR3PBshI14jJqvEkovNuTcAveCLqeACh0MVl0pX9-gQGgIQH-Qg0ntBLR6d8LSHcANdoUEtCh10KRhNLihVJM9CWNQoWGWjntOeT0w8eoPSbvrbxhPx_LwIE3HZR01DqOsk3ZoKuYUgjKzLR1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/81f3af91f3.mp4?token=Hrd7Jr6yR3dZnbUkBMzGhPpAB0EVxg6rDc4hHW7yvcGSBtQnoBxIfuCdVoWDunzZp9tYhuco02oL_dOcqcuGmlR9GQLu86uNRFb287C_Nvqa7e0j_CmO35hXmdlr043Xe-OXMpGCQLqxpxQakQbYlWqfeYp9bjA6Nji5tSoVD7_L9P21xVDXVZRfhNQiZGHGwGmzHR3PBshI14jJqvEkovNuTcAveCLqeACh0MVl0pX9-gQGgIQH-Qg0ntBLR6d8LSHcANdoUEtCh10KRhNLihVJM9CWNQoWGWjntOeT0w8eoPSbvrbxhPx_LwIE3HZR01DqOsk3ZoKuYUgjKzLR1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل اول مراکش به برزیل توسط اسی سایبری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/92760" target="_blank">📅 01:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92759">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">😡
😡
😡
😡</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/92759" target="_blank">📅 01:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92754">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اقاااااا کیرم تو ابروهاااااتتتتتتتتتتت</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/92754" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92753">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اسماعیللللللللل</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/92753" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92752">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گلگلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/92752" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92751">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ضربه پاکتاااا گلللل نشددددد</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/92751" target="_blank">📅 01:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92750">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/92750" target="_blank">📅 01:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92749">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">برزیل بازیو‌ دستش گرفته</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/92749" target="_blank">📅 01:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92748">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">این تیاگو مهاجم برزیل شاید فک کنید نزدیک ۴۰ سالگی باشه ولی ۲۴ سالشه فقط
😐</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/92748" target="_blank">📅 01:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92747">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وقتشه که آنچلوتی ابروهاشو بده بالا</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/Futball180TV/92747" target="_blank">📅 01:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92746">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کیرم تو کله کچلششششش
😐
😐
😐</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/Futball180TV/92746" target="_blank">📅 01:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92745">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مهاجم جقی برزیل چرا نزددددد
😐
😐
😐</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/92745" target="_blank">📅 01:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92744">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/92744" target="_blank">📅 01:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92743">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تا الان مراکش ۶ شوت
برزیل ۱ شوت
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/Futball180TV/92743" target="_blank">📅 01:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92742">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کیرممممم دهنت آنجلوتی این چه تیمیه
😐</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/92742" target="_blank">📅 01:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92741">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کیرممممم دهنت آنجلوتی این چه تیمیه
😐</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/Futball180TV/92741" target="_blank">📅 01:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92740">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">این چه بازییه اقای انجلوتی اخه
😑</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/Futball180TV/92740" target="_blank">📅 01:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92739">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بازی خیلی پر سرعتهههههه</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/Futball180TV/92739" target="_blank">📅 01:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92738">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رافینیا داشت میزددددد</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/92738" target="_blank">📅 01:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92737">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/92737" target="_blank">📅 01:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92736">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">۲۰۰۰ دلار روی برد برزیل بت زدم پس اگر گل خورد و اینجا بی ادبی کردم ببخشید ، از الان بگم
😐
استرسسسس
گاییده
منو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/92736" target="_blank">📅 01:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92730">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کم‌کم بریم سراغ بازی حساس امشببببب</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/92730" target="_blank">📅 01:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92729">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
آقا دایرکت رو هم تا بعد بازی باز کردیم
هر بازی مهم تا بعد بازی دایرکت باز میشه
حال کنییییییید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/92729" target="_blank">📅 01:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92727">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/348e53e8ff.mp4?token=tN-Mg-VCvCYMDM4YquNdeI0JKKwsUuN3SPdzcjSKJ0Ld_-6xzWWo-Oe5ssT8uUwDdXhpi1mRXgiQABqHqtN0V2UknVhANEvOc9ZdMWs1OWdL0KD2vQtxeuLnMqc64E3lTJyvbequTNQVuLrGaT0Fqwb2cUVFO_IoerPw6pwZvg67evPro6P-b08aNw4gW9NM9DLQRn0c9ficZ6S8PcwAlmNIeY0gRX4Fz-H4MmVeWaE1sG9RVw8irWwjnPmPeLuSIs1jt4nYwkib-kgq3cgYIoLIf8OoiY6HfVzmB79D3wQTmJty7-lLNWj7wurIf3bYXZ6OY_X5Pv8w84D4sX-1gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/348e53e8ff.mp4?token=tN-Mg-VCvCYMDM4YquNdeI0JKKwsUuN3SPdzcjSKJ0Ld_-6xzWWo-Oe5ssT8uUwDdXhpi1mRXgiQABqHqtN0V2UknVhANEvOc9ZdMWs1OWdL0KD2vQtxeuLnMqc64E3lTJyvbequTNQVuLrGaT0Fqwb2cUVFO_IoerPw6pwZvg67evPro6P-b08aNw4gW9NM9DLQRn0c9ficZ6S8PcwAlmNIeY0gRX4Fz-H4MmVeWaE1sG9RVw8irWwjnPmPeLuSIs1jt4nYwkib-kgq3cgYIoLIf8OoiY6HfVzmB79D3wQTmJty7-lLNWj7wurIf3bYXZ6OY_X5Pv8w84D4sX-1gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
خانواده وینیسیوس در استادیوم مت‌لایف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92727" target="_blank">📅 01:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92726">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37d498d84b.mp4?token=VNWotA8mKXK6xhrQEZfpkRwAFiAmbF0G6fwMiaLMf7lAqgtrDiU9o_ryGIW8pEBp2-K_Q-PyHMgNiSzO2OE3GxFl_-ACRhdopprOXUDxu0XkV44hOhuSPnvCJbSe-lVhwg4qhIA9uS23lzte4vicqXiBtrM9Jmjrpo90AU_RVO4hHnt-bCLq8lX-76IzhSwFOl5UBQ9eGZb0TO_2vNjFFkAepGNTg5qCulugrQpOsf_GtNUTJ3yUnk83dcgyvZdVbYUlzuwNOmmOWumVCgs90iTAmzz0ORuRjvOrbsEY49T5lClnDK_NTnfHbP9ZtW6OvRkQtDQsRf78iY5SiW4KYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37d498d84b.mp4?token=VNWotA8mKXK6xhrQEZfpkRwAFiAmbF0G6fwMiaLMf7lAqgtrDiU9o_ryGIW8pEBp2-K_Q-PyHMgNiSzO2OE3GxFl_-ACRhdopprOXUDxu0XkV44hOhuSPnvCJbSe-lVhwg4qhIA9uS23lzte4vicqXiBtrM9Jmjrpo90AU_RVO4hHnt-bCLq8lX-76IzhSwFOl5UBQ9eGZb0TO_2vNjFFkAepGNTg5qCulugrQpOsf_GtNUTJ3yUnk83dcgyvZdVbYUlzuwNOmmOWumVCgs90iTAmzz0ORuRjvOrbsEY49T5lClnDK_NTnfHbP9ZtW6OvRkQtDQsRf78iY5SiW4KYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نيمار همراه با تراویس اسکات از روی سکو ها قراره بازیو ببینن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/92726" target="_blank">📅 01:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92725">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">۲۰۰۰ دلار روی برد برزیل بت زدم پس اگر گل خورد و اینجا بی ادبی کردم ببخشید ، از الان بگم
😐
استرسسسس
گاییده
منو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/92725" target="_blank">📅 01:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92716">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2DYcKKtfgj1z-UbOUUS5WuREk2h_ulIK5is3DCsHUHHwstEzhbZyuakkrrgutfJPNTEgPpEdRJjocRRN0JWssR0pp63FFNL0ZsigVJHXncz4LPbByuJ6tjdJbAPtnFVZMItnPGdQXzMMzv5T9jc0YeGw1ooAxRBe21etkkrVz8iIUimP5tMMPO6R3fzO5YHwOG8PqJgXOv7OtXbxeE41Zrs2xWLeYFSo5jzsLkdrF_qgsUxzMJ0vKWJ2pCrY2rgGInCrkwYn7VdGnOrtBvqG9fFSI6BkZUW1BQGSkXErrGkjGYnQXdkbLeNwE0npQTpQCkETY9JOBKAQ1OnT_oKJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OkEK4PkXAYoK_XWBcS8r7QWAN-iYMjuUXckTz9ArE66SbGi2fUpyW8zeiDY8ulFdsH6F7DJPEvJhhH_c6es0EbaykFqLiA4HTNmnWO43KeuZxEmTEK7tu0FOd2GBQYwE5HHcElZ70SG7A6eDctTuggA5oLGT8blhbeKozFEib5KGxsfMvfn93NvtptCJsseQphIIkg3rj0nWcxRUkUVzxeqU3cHyLhm1CLESekgNAoioRGa0Ydb0KEQc4IA2w-Mup80vX2Gzwo_-mibE333xAsRc3w8K6FO2oQB-pd_mXE-_Aa5z9RGkBh9VzPc7TiZ7oROGPQo30ZQSCdJihpJ4GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KfRsR6ACbZAU9okI7WBsrgqxqkz0YUAENPVx0q7CSOrpnN1Q8OpsSOQ6SkagEjOfURE8pmQ97811pqVwN7YW_JkDVwllQCCjLYi3_L-XC_W6uK7O8XojFCeitLY5YGTF07IXcQq0CpldRJMoYsXuVm0L7dtu06Lm-0nbllrYlriFXKVOihhLa5QN3sU_sPXdkJc9Pyft3ulul-HZjdHOawIuYElgiSWmzn-t-jtvZAte_wpDNEc_d3DlaAQbfZVQQZSRBpsUbg-V2tHZKlP_cJnk5QNN9uSuRzpTeZz0zUJ2qMTnAU-scHcF7xNUe0PTf3ZjW-b2fQcHy-F0qMSrlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/em3guflenZzH5Evh6Of0OqsPED9W0AwO-4gUa8PblRjP0RMt8CeuyY0WKHbxAz7PBk-tppLAqBTMJZkUxcCgrhONSOU860AVRZsTAn758HGe2r80luT9ILqlqZJPLzHBB_PxSwk8IQ0DVkBmXBEYDrd33hPaoUx1saiS58UO8BD2CyPSjiTwuKLqYMVpR8bPRAZBoYiQS9ZGARzkqJM23WP1syYJ63GVaocXi2VGV-tkZr1UWPmHHkZ0b17Vb778p2TNCz1I5rPfLLYI-6H7wZOvaRHkDTjtXnXErfZpZeFkqtQ4Hza_VWsrPyaMjYzGhIun7uiekWIPqfQPiBCS8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O9u-2MZXL6hxNjav8l1qhHVxfI-Qd5RT6kZyPB4sWraLaFixBPJQzadVlJLV3ikQyUWSx-mVMsM4cbSjCzlWOJDAdREi6XKGPPG4JPE3WHKmpakTwRbW7nufVNiD5GAJZmPcG6HjPlsQ2AIyj4aIUd1HVOw0Scn4m4r4rCFqnsT8Ca8eeqvUmR4h6vW8YMZwFqxXht6IXcMY_Gl151Mu61KkOJ3GrP31j8cnbeTDGhl4x5GGRf1HCr53bYHfNWonuzwHvUMQEu8FRs-wpXLhbFW7I9ZmGrFXHdcpskZLnNhx21I8ekoHPssNiA8dD6LnEQb7gXdxvB-2MTfuI81Ivg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VHbyASEptNl974eFL2PeBO30vtYtRFNrcU8qv9tCmN7YtZKXLqxUvF3o_TLJIHOo5MmAR4toNXaGDGF-EytsXtVN-XXemwuO4ax4tGfeKtfwyVshMD_Jo9wjwdsrZ5Xd7lYcpbbevx0VarnPkEjgwCiEZg7juYvVv3MT5W6hb5oBIFb5-GLOu2S954ZJzweTDvfctJRExu7_0USlMW1iSOpadYwXxBiHzO-abC2SJIvl5Wcr45im0MjgvG9NS80BVw5fONQitvtJKNemJYukEDipYn-UB4AdMla9QoKv3Vv7hSFu5M-o1xfLxXodzkmod_JOdfqs1zk4ZDrWdnsydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rJGA4usEQefbaZyQLHk2hyi1euXCgiLn2hPrKuipPxsu9pimzLII-nrtHJJzRsSLEZZRWqf6-eEbgtwuCFKeKiWKWP-2xTmVEoTwq3jZTBkqkBPZP2lInHiaxbK27MKzFfFKQvb-eJa6nI_JVM9oIz_CZ5ItucNEf3BS0Ombvuvzl7OV-020u9oEtOr8dI3qkPpFjoY9NlRRtypbyxQhvwBxbJegdEaU7qKLIRnpcLNhFQY0Eqjxq_y6BheqDqbeaHbrGVK9VImvfl7qkj4AxlskSICxJVfLxGI8Ptgb9kN9h6Jkwiw5FMT8SVrtFAOYN-8gwFRNaK6nj2eGcxhOUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rjOcXozHOW-c-z88z94pmxD_94FNyKmDouNzSrBOd-1bvBin6ad_5v3cpU9Fw2j7SZgZXAq6_Tfi0IM3D0VTxTdNmCt0P0w6NRSyY-Q0tO9Q7Vcq57hmqV8v3Px0xMlbcERVY6rXg4rMMMwXu8OEYnnM72DtMmGMnmAB14m5urcDwoEuUBPbS4UQpmMVIwYzk5yolZePGajV1Pc-YcPJJ-lth1rsECXgnW0jtJ7IE4R63O_1Jy0aAYqoKGqr9x41fpXUnncW-zKJV4zjQu217bemp9C-SROi7OLGGW_emaDMTHCSkuBPiEDTZ4EvoWbDh-3coTZuIv7hlMTW_C1gHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FprqC5mEfXUKsQmpa4Sx4IFtPhszlZxoI_gZrvGWXZFpsA4s-XCDRC0eAszql5710omSgZ-Qn7WN3gonRXAHP6ewRY1Zz9_LiadNWyqtrOIr1qVDpt4QqRtoZdmoss_scX67vcxRZK5vWPkWzwPj6nrOJn8n08DKIT5ZuG--y8xcLqnBAlu3DUeZPWjBC-fc_LjQarMFQxCE5ESwCJJn6TK_nH6isekIA3fm2G0a8aRj2vqwslLxAAEdyr1coCEnyC-xxDaIRTgO79M5Li-MEsfGXSqw2msiNQoeLpAcdwSm9rshqEMDFXqzN7IRNV2D81GasAzawCdMWTPIfMC_3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاتای جذاب برای نیمار فنا
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92716" target="_blank">📅 01:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92715">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f94225cfe4.mp4?token=U-m1LzmOX4Q5rBtnZEmmgRD3Fl4A2vDdP-4KdOq1rjVDgmfWSZ4hryT7QUY0s59MrvEQ8bYcMK76T1_crIxKRMoFyOUblPgUA6Ny16f6goVib_8NnoaZDHTO3KJK6y51fGFuzHwKrCySoYEvWPGMO0cxWxYyrW_oE2xQhwGn9SbaFY3EAb-X7YDWVRybE61TXkEhHlG4oDF8ur5iBfrXURCeQ2kJeDhrcuo6KyJ4h6HpaqJYG4Ts2zr_ZSvyeRv7Eg_iL6b_D-wVpSH7xkJe8pHEwfsPG7qotElhRrGDCx9ga0Nzk1y1djRjtmIALutussKFR3Nhw00AaH0k32UkmDErSspQv6B6pL0X6ZNUu-xOqs0ZzUQMiRqnQsm7PteZ_BWVOQrKPGH2vJLlcqzi6lp3rfxxbAR1M2SfTvoAEm8bpeXDQF7vG_Y1wGoEBZt5PtSvR1r_D7ZD4P2VkmSygVPdG8X8HcCA-fB6ChQkmFjAEQxg6b3-GYy6EWM7CUfCt4nAdwIDMVbUCwVKIUdTfl4Q8ghIcTc1j6uKnIG6pIb0pTdx8GAwy2jgXXOZslfjpDyhtsh_XMHctVGViYsN2liPH-moY5lwNNW2TP6FY-B74qnT1BGPnu6PWjQXcpwUGdSoa4UrfoqrcGQx1rUZq3eaVAhq4b95z_IoPBhDU20" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f94225cfe4.mp4?token=U-m1LzmOX4Q5rBtnZEmmgRD3Fl4A2vDdP-4KdOq1rjVDgmfWSZ4hryT7QUY0s59MrvEQ8bYcMK76T1_crIxKRMoFyOUblPgUA6Ny16f6goVib_8NnoaZDHTO3KJK6y51fGFuzHwKrCySoYEvWPGMO0cxWxYyrW_oE2xQhwGn9SbaFY3EAb-X7YDWVRybE61TXkEhHlG4oDF8ur5iBfrXURCeQ2kJeDhrcuo6KyJ4h6HpaqJYG4Ts2zr_ZSvyeRv7Eg_iL6b_D-wVpSH7xkJe8pHEwfsPG7qotElhRrGDCx9ga0Nzk1y1djRjtmIALutussKFR3Nhw00AaH0k32UkmDErSspQv6B6pL0X6ZNUu-xOqs0ZzUQMiRqnQsm7PteZ_BWVOQrKPGH2vJLlcqzi6lp3rfxxbAR1M2SfTvoAEm8bpeXDQF7vG_Y1wGoEBZt5PtSvR1r_D7ZD4P2VkmSygVPdG8X8HcCA-fB6ChQkmFjAEQxg6b3-GYy6EWM7CUfCt4nAdwIDMVbUCwVKIUdTfl4Q8ghIcTc1j6uKnIG6pIb0pTdx8GAwy2jgXXOZslfjpDyhtsh_XMHctVGViYsN2liPH-moY5lwNNW2TP6FY-B74qnT1BGPnu6PWjQXcpwUGdSoa4UrfoqrcGQx1rUZq3eaVAhq4b95z_IoPBhDU20" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
حاجی ینی ریدمممممم
😂
😂
😂
ابوطالب‌حسینی امشب شیث‌رضایی رو‌ دعوت کرده بود بعد داشت فضا رو احساسی می‌کرد که مثلا شیث فکر کنه مادرش تو استودیو حضور داره یهو از ممد نصرتی رونمایی کرد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/92715" target="_blank">📅 01:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92714">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhWET-xLm_BQVK0ia0joi7Evx9VNW53ij3RYVXQyH0sP5s-tistnnT_Bko4ruDCSyQ_wAvdyLkrlSvwb1guieIx66cf_x5ym0VK4D8E_Kzw9Z3iqjhV2pxh6tp1A40NyQ-ezYHQTVHb9oycj0-kfFaV8XY5eFlqhOK_Bl5WX72CejWDiYrva6QlJPmgZUZeRYv1fqTpKgQv7hdaUY7bQU5_dKZrrQDueuT6A4dfgiQw1XBzeA5SkzOt-isPT_e90KBmfJ6nPqpDkU1BqJxnYA7eJ3AfeNlLpIeem8vhU00Kd7zZ98Gsz8ZSiWDeVBKj530kgs8_bApudrFA51j2rZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇰🇷
🙂
تو حاشیه تمرینات امروز، بازیکن کره‌جنوبی داشت وسط تمرین یواشکی از گوشیش استفاده می‌کرد که یه نفر از کادرفنی این تیم اومد گوشیشو ازش گرفت
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/92714" target="_blank">📅 01:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92713">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a5295136.mp4?token=QH2uukYOpRbssr05AhgDbH_qwLbiM9HgHau6yFNOHbxApKoOI40jYavwdoFsDWID2XRReKDfmIxcX9F8TukWdX9vUmYpUQJpXBHJeg1uK9XBE4WA86MNDnmC11anEAlhjchCnfsLO0TBlEHHA2QVUoGVpHER8L4kzxtYiQa9-hue9OUSI3DPsNWy7ioGTxSHMqgc3CGPvmlII91RxZ6zz5tYR-FlpqYtmFzVKtzwUomXB9p7KXVeZzIaKq-Cqn8nTCwdx1ib772ssK2lTvDxSKFtl1mqiirH7r2CrgaNvNlC5bJxvq0kI6K9QqtMA0U--l_sgA4hMbdiRFGMSTPsag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a5295136.mp4?token=QH2uukYOpRbssr05AhgDbH_qwLbiM9HgHau6yFNOHbxApKoOI40jYavwdoFsDWID2XRReKDfmIxcX9F8TukWdX9vUmYpUQJpXBHJeg1uK9XBE4WA86MNDnmC11anEAlhjchCnfsLO0TBlEHHA2QVUoGVpHER8L4kzxtYiQa9-hue9OUSI3DPsNWy7ioGTxSHMqgc3CGPvmlII91RxZ6zz5tYR-FlpqYtmFzVKtzwUomXB9p7KXVeZzIaKq-Cqn8nTCwdx1ib772ssK2lTvDxSKFtl1mqiirH7r2CrgaNvNlC5bJxvq0kI6K9QqtMA0U--l_sgA4hMbdiRFGMSTPsag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
آقااااا جیمی‌جامپ بازی قبلی رو دریابیددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/92713" target="_blank">📅 01:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92712">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15ed350a6.mp4?token=nmoQBl54IQMjoWwb4JrQF-mvQHuM_G0acSuGdArIcFtkISTd_v4e5FFwi6FEobAXxKbNXZu705SWQ-i9OqoaqpbO2eyh2AHkl894OINFYh-ERJqVw9f9nU9iy_p9DgKkBVfvQiZsqU0QTeChI_0QP3nm-PRPk92-DNl_Oz81oDlovR5vfN2UsDmZZKw_bwz_l3OIoUS4uLXq38GTn2dDIcEaCa6mukFTui7l_iGRD_gyK8kaBiwk7Iob4ZRbOVzEF7dmXJVSi4VPtT9f8ThqMaBdTP9GAUMQeMaAdKS65pHXpyfLWyzln5ytk1EHWqnY5EZz4d_6pe5V_X6jHqHh9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15ed350a6.mp4?token=nmoQBl54IQMjoWwb4JrQF-mvQHuM_G0acSuGdArIcFtkISTd_v4e5FFwi6FEobAXxKbNXZu705SWQ-i9OqoaqpbO2eyh2AHkl894OINFYh-ERJqVw9f9nU9iy_p9DgKkBVfvQiZsqU0QTeChI_0QP3nm-PRPk92-DNl_Oz81oDlovR5vfN2UsDmZZKw_bwz_l3OIoUS4uLXq38GTn2dDIcEaCa6mukFTui7l_iGRD_gyK8kaBiwk7Iob4ZRbOVzEF7dmXJVSi4VPtT9f8ThqMaBdTP9GAUMQeMaAdKS65pHXpyfLWyzln5ytk1EHWqnY5EZz4d_6pe5V_X6jHqHh9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
هواداران اسکاتلندی در آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/92712" target="_blank">📅 01:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92711">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnMKQ3WxWTIFgSvWVGiLgFimE0tgWjnUXQbijfRTpLKUr_GgKKM4ZxzMVrkY5rxAlrBwyJvdVGQlAXy6reki-M1Ja__ZPW2D0XFK_TmZPRbrPdlB-Ydhz0zP5FOhRSt_kXfCyffElwsBNXS9_FafNbdOrU2BEUgVVIRh98FnBAADmnALCOJhFZpAkt2M9B3IUnAGn8N2h1ZwikOrIlSLLydkk-80OrMFYtfQB6WhHNQTDwrZtq6fVMAZazL3vcPcQ_t6OyVPrQ4_21m95YRlhMq9Yf9pzaZc6q5Hmq5YTysTK2veTRcll1Q4MZOQqfmLxW4errMO3gT6no_8s9kK3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوئیس با این آمار نبرد
😐
😐
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/92711" target="_blank">📅 01:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92710">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwD3b4yajv_dy-FzQ_HQVrgXqn-U17dqzHfIaScRXNCfaWbfgW0nGm09rdGQ8gpYQKvwZtRYQtu07DcQfyiL82X0kgqoqMIBXSzYZe0UIEoJZ0WJCd40VQ6SDjE2te-wiidovzTrpkgjauVg4v0uuWmzz2_Ls7a0NWhc_VfjBDca_e4w0Btz42gjV9hJJMb0Z7kqCulh1VYFPWAUBi4PqKdFohjD60v8WG6lbvyM79_NNZ4eiV_LD57-L28EbZCdi7VNljQ4nAtWUrmrn_A4v3N4lVxAtpabvGq8aEkF1I9d3zac7NpI-G7HTeT0e4UuOGZ2IlmJPyNibIJCVmIq3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
دریافت مدرک رسمی «دیپلم تا دکتری» فقط در ۱۰ روز!
✅
قانونی، قابل استعلام، کاملاً غیرحضوری
✅
مناسب مهاجرت، استخدام، ارتقاء شغلی و ادامه تحصیل
✅
ترجمه رسمی و تأیید توسط تمامی نهادها
☎️
مشاوره تخصصی و رایگان
:
https://t.me/irantahsilat_chat
📺
عضویت در کانال
:
https://t.me/+1I9Ex4YFtcZkOTY0
https://t.me/+1I9Ex4YFtcZkOTY0</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92710" target="_blank">📅 01:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92709">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMYUGoNPEY8fHDIX9aXJAVrvhH4em2MV_QONG19bCJlamgUtyo6cnwAygtIJzG5gVW_pJYBh0NpZHI2sPJDlnSw4-kbfFXorKAn_kaN0ZoUwuXNr1lpHaKFGWoHdXeiN35-9OPaU6XTUN-KAnAiD6_n6a0IrwzcrRgpfCv0c4WcU-Xv-zF5DNqPlJQgog3eW--7Vb5k0wrfQ82PpgKabG3z3F4U4DuNunPtnDVhQpRqDe9gut0ZOo0d4_ynP77EPnqEvhuI9ut_ZJqGMWUhXJllHJ7f7ksrnZlbxZe-5F9Gs-PL9mqX-IhMrpI8pjGAA0ndJoQSjv7MNw3hXdsoN6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/92709" target="_blank">📅 01:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92708">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAFMT92UD7ZNYTjdhG3ieXbN3gWNhyTzufWXewcAGkULZJMgE563SukIRWjm3L9vwluQt8euBky-3srrxYyz83Ilj1-QpKT1EPHYr9jLL_m4WmzPcoARpBhMJMHj8-vttrIHrGcMp_Tm3e28ZLB8htP_u7VtIyIgTRZXejPnmF8lED4WoWXLMkthe5GRJwh3mTK-OBkpD1Gc4mbQIbW8z0wmDxL44fU1MvVDehCI5TT59gUY3CZ8sAibL3iw-VFqsW-xW5PBsfdZj65i3dYe0y_73ZHjZbvEmH4eGoGp_4CPGjCaqqPeDX-uxmBEgRxXFz1n21gu9IZMSLU7-J6_Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از نیمار دوست داشتنی قبل بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92708" target="_blank">📅 00:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92707">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcGm544FGkqdKENHuqu_pIO-21F2zmeZ70uHC0oa3tTKa59OWYfOdviQg-tzRl5194fDl-61xSjGtfhp5OBvsqut4zx_5tpEq4XTf13_5Duxmyi_Hou3md6o8qpAyIIrwxLiLYjvkThkIHE7LsgZDcEtP0ix-r6qzi9K9BdwHp5zsN3Q7XFVqlaCe1H5T2YlI5q7qv7NaAjS_8MM8njWa6OyEZnlRQmTm-voWgoYOobR7F26FS8KatSaV0fmxInBZL1wjifHBuWK9MIUSrXVG9U7bA4DM-QfVYp45kq_zulZgijZaXAIY4AQrtVjn-cBwiOlom3p-RXoghOnDihxjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|کار بزرگ  قطر در گام‌اول؛ سوئیس با ستارگانش به تساوی‌دست یافت
🇶🇦
قطر
😃
-
😃
سوئیس
🇨🇭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92707" target="_blank">📅 00:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92706">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqwCHkKNRYRLQKzqOdOugicvbovkdGBsocde1J50yABTlF6ErePgpkYV0_5C4REDZMIvh5Fi1AFIEOO_9S3hVlIIa4B44wAF2ZFOVa74NDpf58nLu93vZ4batPNV0voEC6I0k_wOqn3JyXyPZCNkD-_zVjOcn2XZOJm2DH873ihINkvjEiHO0W1yUUvP5NGhmIiCzsvP1JLc0c1gawTIghiDnnh6CGzN-rcHHzIEYvgzd-n2q8m10QCd1qgco9HN_Cu769QPGHV99ETyCX_kLx-ewO0Kd5bf5d18YqRMxRP7UG0Wbq2CySuE_Vw6D9wMVEW9nwWtUv_2-fvLcOggfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات گنگ از اشرف حکیمی قبل از بازی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92706" target="_blank">📅 00:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92704">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0Js7klBcJGDbi9xC_pbZuOJwzjt2_qpsjyUIsCoq7KQEhw6LyT9gG8nP5tLEZ1PlIFAIALPP_sxWQtDZnntPY83W3bp-dVSO-hQ9SPY5exUC4DP01oWMrT_gGAYIngSSFAvAkhpwJo5DsQM5AcUUwg_Sw8bq0to-ku8fjrbZEeXHIxdrsMm1NOw4QsR8879YjgzFySS3rjPeTPDzv3UZ70J34jnZj722F6xZ6PI4OYvFUDl9GvAj9b7OCPUjZIuIBOBoAtIOt6ca5QnUu81ctoqGypDXp41I0OkQXPbWgUMq3YndogBcHyAwKBObPv-5pb63JvYpsrBcFhMTG2u0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🙂
🏆
جدول دیدنی گروه B جام‌جهانی در پایان هفته‌اول مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/92704" target="_blank">📅 00:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92703">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewk-vRmtKAw37h08qKGMXGQxyF9GW9SmF9_dKAeLJPm1pBtqm3Cp1IAnGBpkxa6yaqg_k8gCajvycWq-16nfZolXmju-yOljZ_NIfMSZI2iEjtwE3wsZ6JVsymcemRVKTPtHNDLd_4_-5_ggqZGoUIH1Phkm_sRfdYbnSJsuJ1OKeuAFj-E0Cfl4w2bTsjPXfC0UIBov15jOqW55j-CSuqi73IDxxXBttluhdiYtw-2UNyvRY341ZelTG_vo4DZFMDJGV7uSn930ys17fxiitzXE96DGY4vh7WqfCt3KGE-6jdVDfvxSdQzY6JeTEbHYlBafIVf_41qEw-dUEqx2SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|کار بزرگ  قطر در گام‌اول؛ سوئیس با ستارگانش به تساوی‌دست یافت
🇶🇦
قطر
😃
-
😃
سوئیس
🇨🇭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/92703" target="_blank">📅 00:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92702">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpct1ZMp-FXduVr10ux0MyySYHOH92zzio65s2QuMLbcsj_bZz2G3lnD9E3vmb9XMseiau9hZLdrOiOKDmICKBBYy2qQ9QrPH__JtGdzcqyD_OKkb87aJ-OHZmWYsNPuqVrVDUEpOqg1zUsGMD1UisxWr8AVEIgEqp1PW3aN_7D98abyRxOnffw64RuDbo6sItq2gG9rpKVLX8I67bSkwfRBhKrvBWXRuol02BvwQlIognYiDlpSvCxkE8k5CMm0kLGjMOzbpE_QRdXSMhcNMPUDNW-ByuHSPH6By7Xz9wH-lo38U8nFvw0EwhgPEcg7Hb62qDi1k9spITj9oobhYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇶🇦
#فکت
؛ بوعالم خوخی دومین بازیکن قطری تاریخه که موفق به گلزنی در جام‌جهانی میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/92702" target="_blank">📅 00:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92701">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🏆
🇨🇭
گل‌اول سوئیس به قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/92701" target="_blank">📅 00:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92700">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5Q8TxG-lgBDyU74IQmxBrTXwGlG5W0ebv0EK8YEZ6uCnvePL7angvBxB-zDjSVL4o_WRBuVhuwJeVN0UDsaz3PJxu4ObFqx2uVrFq0yzq5dF_dzWWQwm1UGIRMUkY5ouJo8CEj6zxpz1CaExOxVPoggLwLCrq712UJSGTvS7xyQSCNE3msVwI3JpX0-gA8ljW9ok2wjRYBjeqOuEEohbXd6TvmlDKFiLAeqzchtCMpYF2rtZkYyBsgSKcAu6m30HnbLO17CpNCtYG1Bd_ZK7KsTT_rbdUuNbDhuHp_o4-WmgkcULWTxcM6ayIyOg5wgdb78Q_qEZJqNPp6Jv5DHsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوئیس با این آمار نبرد
😐
😐
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/92700" target="_blank">📅 00:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92699">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egIZ_gAHY-j62khg7axr-BhRhoNXpQnqhpGlLFZ6GMymDHB2i8rnfPOjNNog6OYDJbsMczhHZRlt53Mk5HJmpKvuPDJyUEx1Kg8spKUtwcgZml5OGKm5vDnRSPqVSfBhJdCc9Z82gILuhWNQWwnQh0qpMgXxeVN7n360UQkIQZTD9mVVwREiYhch1N18T36PCMFgpLvwdnGnx8y8YdW6jGU6YY15wyoDFilkxy9jP0NVS1BTsQA-GCYiTiDIbJGzWSD4vhPmQdoCBcFoB6uMhMAoIoMuhPDPjkYQpR0p4Ip_MSJjbIe_zqEk6rSyG1oWUr0MK60FPRosWpc9EFXn1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
گل‌تساوی قطر به سوئیس در دقیقه ۹۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/92699" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92698">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بازیکنای قطر بعد از بازی ریختن وسط زمین
😂
😂</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92698" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92697">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf4bc984f2.mp4?token=Gb9ZalqCqZ60xRzYdltXbQQ7eBzeAaZlaBAAtjFOSJnMHI0fzKLlDF5aYVI9Xair2SdekzlEQsxRxvja6VcLPSxcqZEnSaf9tgFq78qd877RHYz6hEPaS_AcIsX0fwMc857p3TaNMk1PP2lDW77mODuRrcWk6fT2CmXTfIwH-hTb15ATrwohC6JlU7apET33oSFR-t-qysV2IR0_pygeVC4nTWhRLaJbiBOM6FCHIfDplHnG0DCLESngH_JpnBfzm51b-KPC4j1WOnpRDXpfRWJRV5wJ-o0lth9WCiAyMNgkB7a3pIMJsXylTKDHbAiV_p2yXyLdHk0B3MelfkC_rJPOLqLNi8IaXseQhZadSktOH2Mzmv4yZOgtUxYYxKq6FCHDDQyPQXq3rNn7MWA4A0Pa-lqqyb4O3IIGeLKqgDdiKHhQBibBZ020TAg2Y1UWFhQwKxum5IFnR3bDSiEjxFBP_9LIIQ2tsoGDNR1PBTNEzmcK38R3ET4WjurT17PYtm_jvSHEzkP-_sN2e8PO_67VO5enusNzxkLNX-2GrAeABsTIpkq2NnO-uP2BryDgf__1sgA5Iw1yHqw-28C17Mdlak0FjTZjeJOPQw0ElPDS6Qqf5RV3ntxgT66P55Lq9k7GA28wYjyiQHHEApR7qP_F4mqTiPehx3aB-D_MqoY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf4bc984f2.mp4?token=Gb9ZalqCqZ60xRzYdltXbQQ7eBzeAaZlaBAAtjFOSJnMHI0fzKLlDF5aYVI9Xair2SdekzlEQsxRxvja6VcLPSxcqZEnSaf9tgFq78qd877RHYz6hEPaS_AcIsX0fwMc857p3TaNMk1PP2lDW77mODuRrcWk6fT2CmXTfIwH-hTb15ATrwohC6JlU7apET33oSFR-t-qysV2IR0_pygeVC4nTWhRLaJbiBOM6FCHIfDplHnG0DCLESngH_JpnBfzm51b-KPC4j1WOnpRDXpfRWJRV5wJ-o0lth9WCiAyMNgkB7a3pIMJsXylTKDHbAiV_p2yXyLdHk0B3MelfkC_rJPOLqLNi8IaXseQhZadSktOH2Mzmv4yZOgtUxYYxKq6FCHDDQyPQXq3rNn7MWA4A0Pa-lqqyb4O3IIGeLKqgDdiKHhQBibBZ020TAg2Y1UWFhQwKxum5IFnR3bDSiEjxFBP_9LIIQ2tsoGDNR1PBTNEzmcK38R3ET4WjurT17PYtm_jvSHEzkP-_sN2e8PO_67VO5enusNzxkLNX-2GrAeABsTIpkq2NnO-uP2BryDgf__1sgA5Iw1yHqw-28C17Mdlak0FjTZjeJOPQw0ElPDS6Qqf5RV3ntxgT66P55Lq9k7GA28wYjyiQHHEApR7qP_F4mqTiPehx3aB-D_MqoY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
گل‌تساوی قطر به سوئیس در دقیقه ۹۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/92697" target="_blank">📅 00:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92696">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سوئیس کیری کیری نبردددددد
😂
😂
😂
🤣
🤣</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/92696" target="_blank">📅 00:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92695">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اللههههههه اکبرررررررر
😂
😂
😂
🤣
🤣</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/92695" target="_blank">📅 00:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92694">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یا خدااااااا
🔥
🔥
🔥
🔥
😐
😐
🔥
🔥
😐</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/92694" target="_blank">📅 00:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92692">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">چه دقیقه اییییییییییبی</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/92692" target="_blank">📅 00:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92691">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پشمام قطر گل مساوی رو زدددد</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/92691" target="_blank">📅 00:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92690">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">قطررررررررر زدددددددد
🔥
🔥
🔥
🔥
😐</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/92690" target="_blank">📅 00:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92689">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گللللللل قطر</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/92689" target="_blank">📅 00:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92688">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گلگلگلگلگللگلگلگل</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92688" target="_blank">📅 00:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92687">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cX9cCsUMgReuoVHEefJJcs4ZTR-NhG6UGks4nuqDXyFJE-rwl5MYPkiXKxoFDx6AYB-1bGVj557PKQRupru0JheAUYjhcxQrsI3Eb6irYD6wABuAjlGQ2X6cPVOoONxHxfpZC1DXgATyRXdmV9aJaUmMSBl2KcInuKR4S4dmtvwCVhxNQsy0aaZLe0nrWjAcFjKs2tUt343zcJpACSlwKTkr3ywM9Ya0x5YOmyHI_hmK3pe_UUcZT_vss0hRW2wrinECfEYA61LsTBU2bUK3HlFY7VdZnSKXrEUCv63S3_n3bpJq4gI4sT49huFuGcKnzKHv8FdKGwhhsdQ1QTRP6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بشر انگار نه انگار 41 سالشه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/92687" target="_blank">📅 00:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92685">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بازیکنای سوئیس تو بازی امشب عجیب کص پا بودن وگرنه نتیجه جور دیگه رقم میخورد</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92685" target="_blank">📅 00:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92684">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SL8V6jxmr8Bf0Qpb-CUEnRCN25_WmHQwfoBFkRD4Wp5jPZKWFzpLhJ7KrtGHEw4gVXG_Ee3dUlq7E3v_axjRXHaVCX8N0ELirh94WupCrCcQ9acYFakFLT6wnd9OD3DoyBe78R0-TXYXoVLd7VdwACdObNGM8dO24cijFPnQSETFdtMXs12ppBQpJtEJYkmNIpyaghPaoGK5GiEHofR3j37F6i_6BsHt2nOWF8RX_Eexzts7WFJaBP8ZPJ-lnemTSoryuhsF7YOu9N0XRW8M-BzjreCRVHRnyfwwDRZUR7Qva5zx6KyGgs5cdOcIUX6xZu3o2VTgnWDdGSV4TaIeuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🎙
🏆
کلوپ در مورد کولینگ بریک:
فوتبال گروگان مدیران اجرایی شده که تو دفتر‌های  خنک و مجهز خودشون نشستن. این وقفه‌ها رو به عنوان «سپر حفاظت از سلامت بازیکنان» و مبارزه با گرما معرفی کردن، اما در واقعیت قفس طلایی برای اسپانسرها هستن.
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92684" target="_blank">📅 00:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92683">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3a1d64a3.mp4?token=v7MpeVm7YiM5SNhfLABSWJqJ6iyQANhHxuXTxCetmQO-fe7StpTRaHkxLhGtNFuCugTVNPKrXvyAntly0C6_4ymSfMcS3W-NBiBPy8vheKVirfG7GQ18sDsg33YVGjgeDav9wWVvOSRcxsg9mKUVKfiQW4F1xabsHhM3hJqjvGLZXvdqRYl3WZTtiWBLATN14YYH3cMpfuH8DDnDHNV9QpNijDdXPSoMaQsUFyq_rsJoBnSr37Z2fmkUSD_gNJ__CHmTu5t6Gi2OWRHSTj8dLNUlGOiLgHlYtQ1lYJJu28j4fiIsvFXjUPqH45VQ-8tk_sriz0bCbezG1NhTGxDHqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3a1d64a3.mp4?token=v7MpeVm7YiM5SNhfLABSWJqJ6iyQANhHxuXTxCetmQO-fe7StpTRaHkxLhGtNFuCugTVNPKrXvyAntly0C6_4ymSfMcS3W-NBiBPy8vheKVirfG7GQ18sDsg33YVGjgeDav9wWVvOSRcxsg9mKUVKfiQW4F1xabsHhM3hJqjvGLZXvdqRYl3WZTtiWBLATN14YYH3cMpfuH8DDnDHNV9QpNijDdXPSoMaQsUFyq_rsJoBnSr37Z2fmkUSD_gNJ__CHmTu5t6Gi2OWRHSTj8dLNUlGOiLgHlYtQ1lYJJu28j4fiIsvFXjUPqH45VQ-8tk_sriz0bCbezG1NhTGxDHqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
آفتاب‌گیری رونالدو و رفقاش در سواحل آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/92683" target="_blank">📅 00:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92682">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi0_ozdJwqZszQBnV4EZu4azFYV9dlsfX628fngZiN-uV-wr9ygBnZCCKVToYG_tRVeTTNBl25pCUVD4SbwUCIPluuPbBUaAJChYFxMf_8oAG2iOsLFDTCwe5ijYIuwqytndPXzStWOelmDyEcrpSpNEWmouXMbmqvBaiXfOKWdvZvzfv1sYgOVrUjZpNFXuXVLXN4fFmQdFYByCn6rmYMAWiUnsOpuCdTffKfOrWX73-84sog6FdoMtHOVva_hkyEeO7ysViUdS3TSU1V2GKlgFiR6x7DilvVvTOC119AoNf2WEoecmreHCCWYTeZW9Y7ijyUKD0RWz7cXYPPBozg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇧🇷
ترکیب تیم‌ملی برزیل مقابل مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/92682" target="_blank">📅 00:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92681">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8gOGKal05fJi6eiPU7MpY2WBQLUJD2lzywYQPTEMU0IiYLbV9yNcidrD8z4H6EdRPgdHrdrJYANHWR1EibkVt8bsmekqhoXtA2NIZ7Te4BXvRk_FFUGUoiH1XLL16Kbu_R5386t8T9y1sqDKmJDZD2hkY9SHGtMG5PtSR1C3s9UqjnshigYV85De4hD_XNNHDAV9ezDCmhN75thNFHIk1iNDIZ3kd8VQjClsz477lJO8LJQfHuT_QosoVW5pAGsiX7RPFJh6hUnmolDEoeNhCP-U0JLZbuyD1W6HWk22SnlmobKd-xW043gE7tqijNL_sXuBdaIKeJGLnKP26gpXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دیگو سیمئونه: «من بازی خولیان آلوارز رو دوست دارم و اونو به همه بازیکنان ترجیح میدم مگر اینکه حرفی از مسی وسط باشه.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/92681" target="_blank">📅 23:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92680">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">قطر تا اینجا کون اورده ۴ ۵ تایی نشده</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/92680" target="_blank">📅 23:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92679">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نیمه دوم بازی شروع شد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/92679" target="_blank">📅 23:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92676">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U89P75MdcfrogNGyOCVU4k9LbcECqMc6rvKfG3gwzDYaf1zd_NdF49PJlrHL-626o2T4JXsp4llxaCfpdTGmirx4N2ibfL8UK1_WtpWptH7Z0PrUE7jm7jvmHSL6wDamlW0-nStLxcxdkoZdurTc7XG1qvPZRg61E86CTMuH2kx__ulNHN6icE4VUJBUbDOoFROl0lNRxk7OFyr657_W0ilpUCYCsr6jeg18ERaPEEhkS8OfwmlaPKV_7HWxDN-oiLfXtZQ-jUSe30jEC7UqOGANEXtj1e4znB2kTfVVyJ2L1O7L7dT1AMLnRMXH1Heu2MGvXQjiRZRt4h4akYpsEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OKPjN3jh1YMiod3YXi_30x0v9o1pLTH8pZb1az3RfDbzWap9HQwUY2gVtVzMA7aVoPSwgGzaKStS5hkMrCtdf8NsRn2p6jfWdRCPlyWfnTLV8U7UPJuDB9zR1IXePOd370y6hg4BZWmHsRLsqp-pSvBLLn9359nbcY-FIP7zVbESm2zSqLtgsNENzqoB4fLDtaZszPZy85p9LN1eqIIVGeGIJ26g4hhigo_6H5GOaHdxuLN_OQvb28PRMPXGkkL-cd0hXdzdpCN8h5GCYQxN-34aDcBZNXOudzm6KH6s_dVgfVh4q7qK0xqIRw4pG3CvR7-ScYWv7Nq3GqbrzIoa-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VjH-DTR6yUIy2EZlEXq9ZwisrCMLAcRUONAgBV_PbrnKq-5njVkJvllEYnfmMhWu7HdcR2D7Qa0PKi5lhgsBR_43kkz8mwdf4L36QmEOTzLTCNh8bJ3YAkRwvEBtwo1GQ0VfEKRewAv4LMwKqrqlHp499HSkBEvBbZ9v-b2PK29876VUtCe7rppyE_hGmDoiLHesspYtgkrFtjW2CKFpEd06o6ZfKLApPMp5WGT67ViWnY2iKXQL_Uy9WV69x4R4ms_obByiy84UJhRfry3YDikc_ZPk4eh_VWehJLdZSulhFS4fLHmJpRsKPBLsmP3adtQtwlkmhbLw2XWwfnPpYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇩🇪
بازیکنای آلمان از بازرسی ها پشماشون ریخته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/92676" target="_blank">📅 23:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92675">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qtDVKGiXO5T9nLLmhbPEPKk6Pk9nJuxf7KsGVSmxYMAUESYkLGf5WcOUoP1up5mTTKgGVvj3bSFXFa5TkYDnWm5ZrgURKj3YAo3r_Xtn2rFCyb12Yl2SAnIoXYhuTu4oeMJt_OvH3RtgjlzXVoYdcujwFS61kXJfswjBs34gc0IjrdSCKK2k3LdnY8Qh8rv2uBy0MQz-W29OnU9WqtDyxS_nSCUyIEZluKNLW1DfALj1nNLu226CDga2I3bPFYgHQ1WhVImnzrw-gLFaRIP6pp8WqDhUtQCQnSHZ9rpmEql6pAeZF9IL1ZUBExJU6JH1Udi6A0PqXyShuqL5gV_7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وطن بالاتره یا شوهر؟🫩
وطن
👍🏻
شوهر
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/92675" target="_blank">📅 23:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92673">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WZoI1cfwlycI53kH0WoDiKrQkVmZICp_wCO16rbDMHIfpm6LArgf_ZyD7QfrqBzZW4NIcns4K4b0em86v5Q7BQ85nVpb6luNI8idsErwITCVQYiVIMJafr5l7XRGL9G2BL6biFb2Qk0sAVfzfy8JZ7BkgTzZe1tYK4ZMvOi9Dhm-FjAiDitTY-xuYo238K0RVbfjiySiYw8jtfh-9aW8nF88sbfHEgNIXCjs1IigeUXyR6MpFrVk_6batsydaMQ_63oscAFDrmKANLc5O9-foCa1Ow512Gq39H8Z0wUeVFNaQ5gFUMTgul84nCsdH8pV-DC18uBaQW_SaZ8hUkzprw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XtiVtaRL3CuqZdGxPpdawmz3Sbj_bPGXp7QBlBZsnq0ZgqDGzzdXx1DAJa80mS8AgsFIfUSPBrb54NvwSGp8EQESt_F2GSJHsMDnp84pu0feoqM3yfRxdNCxWGEgqfbDHCepjctL9xCDp5xmrBD_lMQ9aNmQgBBGeli0WHE9m2ufKhXzG6iEYeRTANqcdS4kqwbMARHGSrWL4bU36iy2BDN-KzfiGT7Gl5uGE9chNEKPljalSZirtsiyCfv-FBy3TytpZm09EPtgwQFn43OiXcnwTMuBIODzHMkZBWN_pN3mH7Jq4S5DvpBtGMPAx2_c3zBsl2cHKReVRgxmjpxKJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریس رونالدو لباسا رو کنده تا سواحل آمریکا رو جلا بده
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/92673" target="_blank">📅 23:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92672">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcVr-CdEdYAyfrwfNZ2wvF57ylzKFY_1gBkgL5aqtVeoKiFpnB1RC74pxQYta0Ok-SHyDEBOkG7rTKyHYUIBOtx13eADD5C9Ttwof70z89WQUA-bEvT8fSpyUye99UlSju-n4pGwABEuT_I_I3aDiB4mrGSXCe51fhsylHoSezQkKTWC6VBCE0EE9qlppOn-w2MorEBtIl1v6M7JACxQt8anhImvi8tDW6v7Kl16Q44iVQyOnVXTjoQz__h7EMB_cYa9rlNnJ4gvfBiWHp56IxicNuognQqViiouW-e0LPGGFRfiSPgrXT_nuI3kxbf8w7XwK5LFs8nZVqNOb5uJ5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ماتئو مورتو: آلوارو آربلوا در حال مذاکره با فولام برای سرمربیگری این تیم است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/92672" target="_blank">📅 23:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92671">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvuK2f3VBWTGGsl63eR-PKpqb7Nx_8eWY5hgEHKb2jI234HUop6QkQmnVHAJYnTB2o2j90na5pTyEU6Jgt07vGVHrV_iSNgDkCop5Yy25ZqvZqMZc4Yus33ap3lpZGJ0bGF-3X5Uf2YwqrT5mT88arJGSserHCs8-2QZQinzsfFHj6v3nYao1Biz_XlT3F4uyyCHx-iWEBx7OXRfZQsxaNC30VNdBPMuRC2gNvjsCZ-LVU9fz4ogilz6RUFmOzryBAjysxPk7ICj_Sdf7QnmW769h3h3So8mPvXyXDhY7nbABtr-2zGG4hr4ghAVLynoA_eHa_v1lTGAUDlF4gBabw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
این توپو بازیکنای سوئیس گل نکردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/92671" target="_blank">📅 23:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92670">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNVrW3BzcwWYKcXrFOSlzsYqD_xlwF5u2ltQFJ0heBJHlEDrH7EsOdjnY6dFv__JYA1ImjILeuCQZcG4xfVdXl8lvbFft8G7eppTMNucTqaB6GhCIvcxXe-Dkokxrbd3eeorZg9lVDUGbyYw4BK4uzc0rC594dKIOsVmkgtxCp8OMM8DUYNnWWUIoHFVnhIGBthdk56KZfQz5E9PamKvHGwnXn8mJsVseJqXqhKEnV-ODJGlyTcQMKy1uuaUsk73mJS3KQreAO5bogN2I3iNrro-0ocDJ09m3kRFlU6_23WJYHidZ3je5q2Lg870QQZDcf4IKD1iG4CWW7Ws8a3n7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماتون بریزه
دروازبان قطر ۵ تا توپ رو سیو کرد و تو ۴۵ دقیقه نمره ۷.۷ گرفت
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/92670" target="_blank">📅 23:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92669">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پایان نیمه اول
⬛️
🇶🇦
0️⃣
🏆
1️⃣
🇨🇭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/92669" target="_blank">📅 23:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92668">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">واااااای چیووو نزدددد سوئیس</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/92668" target="_blank">📅 23:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92666">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">چه سوپر سیوی داشت گلر سوئیس</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/92666" target="_blank">📅 23:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92665">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gueaukzKjw9CHlF7AD2fTXzkD9BqrnuaGMIqn_OV0znYaf6_Jh9O-qF_OoqMBxm2DoBXPrjSFrgfhPUhRQrcTUkax39xakcWg_6D7QscjyhDW8bJB2z59Yfe8p-XKrFDLkRxlVKRgKrWUkk-CQmRgesAXVGfZZYP12LVNTV-mp8jUc0g_1AiObnQP5k1SQZVim8n80-q6_HE3J8wS4WHWi5Rknqi0e4NMq9yxi1ocXvWDgmkbIRlkDv7gENt55jfDU_n1wOCGWjgCmkNOQFAcg_8XM_LOkwXwHgbaGj1cJScrx6y6itAeU3Puqy6zp7JlpFH0MSbhh0YmHfamoEi9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گل‌های امبولو در چهار تورنمنت بزرگ اخیر:
⚽️
یورو 2020
⚽️
⚽️
جام جهانی 2022
⚽️
⚽️
یورو 2024
⚽️
جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/92665" target="_blank">📅 23:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92664">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/04f957d097.mp4?token=mJ8Uks_yHUfaQvI-CSwai69xV3JCSB5-9guu1CJFtD5LkO280mRH2bo6g_wa_w69x4M6i9nLiVblOuQW-gF3X4R_epQ4Eo2n6laoM_8HVpgxpCmJLfIKFkKwuA9EV4NV4Rrq-hhHlHCkYzdPmnDM7rcLZ6rlmNu8B_2zn7OHX8HYhqieSUi0kl2OaGvy8lLYbzoLfunVSAKUYhhD19bwY6ytND__K95ivX9QFf2xOvVZ_cnnEQd4y4QdxvOcHEiko6ll7I4AYc_OPZSoU0opVUlrzCWpcLzJpiVuf1lC2t7yeYlyLoxcIAgfgZOBjF921NDSEewD1Otd9BVSBK5Y3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/04f957d097.mp4?token=mJ8Uks_yHUfaQvI-CSwai69xV3JCSB5-9guu1CJFtD5LkO280mRH2bo6g_wa_w69x4M6i9nLiVblOuQW-gF3X4R_epQ4Eo2n6laoM_8HVpgxpCmJLfIKFkKwuA9EV4NV4Rrq-hhHlHCkYzdPmnDM7rcLZ6rlmNu8B_2zn7OHX8HYhqieSUi0kl2OaGvy8lLYbzoLfunVSAKUYhhD19bwY6ytND__K95ivX9QFf2xOvVZ_cnnEQd4y4QdxvOcHEiko6ll7I4AYc_OPZSoU0opVUlrzCWpcLzJpiVuf1lC2t7yeYlyLoxcIAgfgZOBjF921NDSEewD1Otd9BVSBK5Y3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇨🇭
گل‌اول سوئیس به قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/92664" target="_blank">📅 23:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92662">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پنالتی برای سوئیس</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/92662" target="_blank">📅 22:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92661">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پنالتی برای سوئیس</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/92661" target="_blank">📅 22:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92660">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سوئیس نزدیک بود بزنه که گلر قطر واکنش نشون داد</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/92660" target="_blank">📅 22:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92659">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بازی قطر و سوئیس شروع شد</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/92659" target="_blank">📅 22:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92658">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tvq5HV-glAO4KWocW0R65d7aPBsRBN-S8gTO4Cbg7D84pcGaHfCe4z606LruRdzhLcTQfU2zbpoiHpXQt3OIjEJcEsGA7OKybFeOan7374XVNxJvNi4T7GGn7Z--nU3_FL7ZdPiWcatXu4DGXyRLP-25h3SQyddAdluuxOYMgXC0XCiFiVhfZEkJKzm-ax1XW-yM1t1zYHjXrQjEic5k2dUnOr8GuFUzX2ZpYz1LQmX_189cXcM6bmJjhPfpzuuOWDjAREU-Qqvgsw38o45OomCfkuG5jrCIoGHncvkY0__j_24fKEyAdf6AJs2MENC5qXHWxa7xA5fFkOUOks8kNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🔺
توییت جدید نیمار در توییتر؛ امشب قراره بازی کنه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/92658" target="_blank">📅 22:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92657">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnKjRNIfyvcwx93wEr0z0mSKjpKjAJb-e-6PjcBEUO_p4p6iIGEMQN0VuLUhlc0cnmRqJ7xOHQHB6uNrhN3YWHUtcozM37sjQ1j9g-QqBUp_tkBD6Jd3adIQHImrshsArAgDRZo3DAMl1A9rDt7FGoQjIh9droq91_rW5EIPiMDlGSV0mJ5V4CyK0E6fnUP164jNGAB951Bb9RS5gY_vOj5RH8CdoKLUifwy-00HDlq5u0lTYz-v8NJp_DrnAg7RUvDfosNAIQPUFi3Z-dC5jrC1hKTtUaI_hhnf_jhqDJqrm94qd0VkEhtUjb6Rgk_yRsPQFAirSBmHuJ-ePWefUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
📊
🏆
براساس نظرسنجی‌ها از تماشاگران، رضایت مردم از میزبانی آمریکا به نسبت کانادا و مکزیک در مقام بالاتری قرار داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/92657" target="_blank">📅 22:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92656">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90512a635.mp4?token=KkYYcfo9ORkjSk8duxlVuhM7CizLXE2g3YiEqj9fGRKITgj-z5-tIjqrM6RGKOQHuPHSB5UJOtA1ABLqBsquA03r4zIO7_swvRJtlJFOUlij4oEyoYH1ocNYmgy4rdv_-Jhu6JWi0GYMD9RPXSQoVO_OdzkrbivwPHKjAVf3x3QiNC8tLrltnaXcR4DGweFSI7-HXa4INjMJPZJHwL_7MaAN9siLyE-s8YTEmfhHu11r3EAZT6X3jiBnx7wSPibH7FTaz9IKOuphwghGmJTwtLBz_5HZNOI6lkOELprjhgSaoUp6wYj9I6WpQhy-OmV8UW61yc0JIyi3r8ycAziesw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90512a635.mp4?token=KkYYcfo9ORkjSk8duxlVuhM7CizLXE2g3YiEqj9fGRKITgj-z5-tIjqrM6RGKOQHuPHSB5UJOtA1ABLqBsquA03r4zIO7_swvRJtlJFOUlij4oEyoYH1ocNYmgy4rdv_-Jhu6JWi0GYMD9RPXSQoVO_OdzkrbivwPHKjAVf3x3QiNC8tLrltnaXcR4DGweFSI7-HXa4INjMJPZJHwL_7MaAN9siLyE-s8YTEmfhHu11r3EAZT6X3jiBnx7wSPibH7FTaz9IKOuphwghGmJTwtLBz_5HZNOI6lkOELprjhgSaoUp6wYj9I6WpQhy-OmV8UW61yc0JIyi3r8ycAziesw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
🏆
مراکشی‌ها در آستانه بازی امشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/92656" target="_blank">📅 22:03 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
