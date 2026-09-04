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
<img src="https://cdn5.telesco.pe/file/o3U_RGU4cBMrjTx_VOKfs3bxtOVel8LeXrM1e7Yu3-x6Bgxjd84Fe-vPWfoqjD2p-HP2ylGY0XLePBVnc6htGsD2Cp26QHgOf5VqC17MIVF2LSRu3eqi4AOlFJow5du3lf2tTxCqZqdeNv9Pk8lCLn4X-kxZK5Sv1JRwXVcC9nbcE1algj1tnXwvmBS2dxt4h6Css1haMhopy-6p66Ioc5X8kDj9EECIB_5gDDGaY4H77xSPRwDgt3VXOoE7-SNWWhsvIO1tFcyeLAKmZKC2TwwbDTJcx055uUcBP7evxw8a01tIeHJEy_8ySLXuccahGREk1WS05Jn171NgXQ7BjA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 428K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 20:46:44</div>
<hr>

<div class="tg-post" id="msg-105512">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0ab284a6.mp4?token=ToCNVxYOHXbpDJ11_ZlWoH4BmUP8YvMeJXcP49nNGRC6sn50GmLTVFIINmFxPGWzbXxowfsNtAN1BAcciAMr5In5bPshlGYmUJXFEXG0dpmQhEpExUFJLfHO2rHcVFwQBgWWNEWkzIO9JJxfAieeH40cfQcsEgC6smkYxL6AZah-bEsExtd7Ec5EKmecajMZrZARNp9CNbPREC_Zz_EW6-dkJlGdxBLG5AkRDHhYHffcERLWzVKvjG5joR2UBYmodz4T4Y8vKNHe7FwkJZXsEZEwa-QNACTcDY7Mc6zLpDKbEeIJPYa0NdOnckRUOgmLVId1dJnqi7ttju4OZABf9DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0ab284a6.mp4?token=ToCNVxYOHXbpDJ11_ZlWoH4BmUP8YvMeJXcP49nNGRC6sn50GmLTVFIINmFxPGWzbXxowfsNtAN1BAcciAMr5In5bPshlGYmUJXFEXG0dpmQhEpExUFJLfHO2rHcVFwQBgWWNEWkzIO9JJxfAieeH40cfQcsEgC6smkYxL6AZah-bEsExtd7Ec5EKmecajMZrZARNp9CNbPREC_Zz_EW6-dkJlGdxBLG5AkRDHhYHffcERLWzVKvjG5joR2UBYmodz4T4Y8vKNHe7FwkJZXsEZEwa-QNACTcDY7Mc6zLpDKbEeIJPYa0NdOnckRUOgmLVId1dJnqi7ttju4OZABf9DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
🇮🇷
یاسر همرنگ داور سابق فوتبال:
❌
با یک عکس نمی‌توان راجع به دادن کارت قرمز قضاوت کرد. تنها ایراد وارده به بنیادی‌فر چک نکردن ناخن بازیکن است. داور VAR زمانی داور را می‌تواند صدا کند که یک صحنه‌ای از عمل «وحشیانه» بازیکن موجود باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/Futball180TV/105512" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105511">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae761380ef.mp4?token=Ucb9yrQkQfBCPoyay72_t5pHs5zslPYi_gBEpZTGBpG0rlOZnTM-MOrtWxcEEY3JJVSw56IqF1Yki1t5k1RAUCCmSmdMT79s74iftnLH72c1fAGjdEluCE8z79ZBHwjK9cVw3JIi7LJR1hFaNR6HfgC2XpNDT6iLFqgeRFqcueMhIhTWxrbwTBgq1iBkPDE4Pxg6P1bMpsVSWTLPF0ICYinl5DnCxHXLPNClgTotZFaDmH_AU5LoS6fgfkLHDc91L034rl2PisxiX-fZJqBarPZGwQmBwfSy2tvkCH1S_A982h45U-tj-AGJinGQcRdfa1rzr3rpquHC6Nv9HS_4jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae761380ef.mp4?token=Ucb9yrQkQfBCPoyay72_t5pHs5zslPYi_gBEpZTGBpG0rlOZnTM-MOrtWxcEEY3JJVSw56IqF1Yki1t5k1RAUCCmSmdMT79s74iftnLH72c1fAGjdEluCE8z79ZBHwjK9cVw3JIi7LJR1hFaNR6HfgC2XpNDT6iLFqgeRFqcueMhIhTWxrbwTBgq1iBkPDE4Pxg6P1bMpsVSWTLPF0ICYinl5DnCxHXLPNClgTotZFaDmH_AU5LoS6fgfkLHDc91L034rl2PisxiX-fZJqBarPZGwQmBwfSy2tvkCH1S_A982h45U-tj-AGJinGQcRdfa1rzr3rpquHC6Nv9HS_4jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
‼️
⚠️
جلالی: هنوز هم سر حرفم هستم؛ قلعه‌نویی در اروپا بود، از مورینیو بهتر می شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/Futball180TV/105511" target="_blank">📅 20:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105510">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e88a7236c.mp4?token=To8z_nHBVqD6ZQaDcHwysKELZeqAXMguxxN5u7yNxGhez2zhIXQZXuK920MCZ_8qFxNLEDVtURPDKuXvlTvjPxPeOFkNZpCjo8k8JdxGJr0iBxmQuiEI0VP6atLQUb3M4dROaFqdDwYP2Q2eqfIhMMd64S18AZmCqurAg1Qp8dTfolwGDqaiOkAg92jj_d3jLMZrnlHOStRGuyD8P8-4hjNmkxsBY1pLQtYL828zSMwrheyG4QyIdLzYrXKyTcqWAOxnAMe32dWRj2zfjTOU92ruTT2WslP31K6jqPnTDTe7XM1Ioua5Aox8fWCCaJdHP5S7Uf8w1BHR-xCr5-6QFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e88a7236c.mp4?token=To8z_nHBVqD6ZQaDcHwysKELZeqAXMguxxN5u7yNxGhez2zhIXQZXuK920MCZ_8qFxNLEDVtURPDKuXvlTvjPxPeOFkNZpCjo8k8JdxGJr0iBxmQuiEI0VP6atLQUb3M4dROaFqdDwYP2Q2eqfIhMMd64S18AZmCqurAg1Qp8dTfolwGDqaiOkAg92jj_d3jLMZrnlHOStRGuyD8P8-4hjNmkxsBY1pLQtYL828zSMwrheyG4QyIdLzYrXKyTcqWAOxnAMe32dWRj2zfjTOU92ruTT2WslP31K6jqPnTDTe7XM1Ioua5Aox8fWCCaJdHP5S7Uf8w1BHR-xCr5-6QFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
نصیرزاده مدیرعامل سابق تراکتور: بیرانوند در صورت سربازی باید به لیگ یک برود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/Futball180TV/105510" target="_blank">📅 19:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105509">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2862cc83d9.mp4?token=Z4UvvD8guqivj20CO7Ct-H8mIE_x32BkpwPtskKuKMO6hG38e4f2RFuMAnV8w2bzZ0oeCRS2qrlRoxVXcDvAEDr6BdDQMKNWHLvmywwxA8eVBTvcbupafobihK9O8wXe6EM_UrwGHBsQ-BoSI7C6CtZuY5jFmP4q7tz7NAul4tDdRDwKaMi81v39YG9QT3K9cvs7Ii9KB8SS9Gh6tOl0h9gyCGNaZt3Ew4Uz_XJuhi2srtB10weIVw1lU-fU4E7QExfpsGK8f5eUQ_HZvbDxTELKQ5QM3byjEQHX3HigGP7X1wXoCew-vwatsUIcyz73e7Ba0wDt1IaTneA_B884iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2862cc83d9.mp4?token=Z4UvvD8guqivj20CO7Ct-H8mIE_x32BkpwPtskKuKMO6hG38e4f2RFuMAnV8w2bzZ0oeCRS2qrlRoxVXcDvAEDr6BdDQMKNWHLvmywwxA8eVBTvcbupafobihK9O8wXe6EM_UrwGHBsQ-BoSI7C6CtZuY5jFmP4q7tz7NAul4tDdRDwKaMi81v39YG9QT3K9cvs7Ii9KB8SS9Gh6tOl0h9gyCGNaZt3Ew4Uz_XJuhi2srtB10weIVw1lU-fU4E7QExfpsGK8f5eUQ_HZvbDxTELKQ5QM3byjEQHX3HigGP7X1wXoCew-vwatsUIcyz73e7Ba0wDt1IaTneA_B884iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
🇮🇷
آنالیز گل‌های دربی اخیر پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/105509" target="_blank">📅 19:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105508">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‼️
⚠️
رضا قیطاسی تو مسابقات طناب‌کشی بازی‌های جهانی عشایری موفق به کسب مدال نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/105508" target="_blank">📅 18:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105507">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33404ffbf8.mp4?token=fpzRgYmKT9jneVGNxkiJmdFCvZugWwz65EEW3vRYrORnWTks-3MujZuh93MAZjsX3hTJ9C6kfJMlG4lnaxIxS3m8LWVEK0ZRE8tt3Sj4YpCzdaooZoI88ZSUqH9YOvDtd3FJyiD1q6jcCrEvkpVr6Ciy35bDmvv-VKSXT_YaYRN7btJvzkyjH1ANLjBSCH4b1SlAE5l6Gmg5KelbBqb6IRKZ98Z4tdTj3vcNg5wOSwd2SnqbrvvC4DR8a_Jbc5-xTKekmPeRAsfhlmfywrsIPuzI6_k2mit77M_MaHHdhB6yoiG_OQri4o3pwpectznyLfcDClr0slbm2CMHDAp8jaMT1LROF9_RbOK66V0uUvO0SXx1ueIrVsO1AMAir3HL7hTAlCXEGEdXwMMnF6RUAdPmeQe0kXvq_c5hvfkYYpbWYSyjsbFvGUO2Ei1s0EoBUGQUUvET8ooSYFY5ZRfOgtP6C42GLY7sNOB9n214LAnq1ZuPr5y_uXCNA0z74Q4LNzkEHNya0M_A1hnzAbHD55n2sXVIU8Bw-QJ4jzvCbAS41sN5ZUk3GUGnvWrz-iDhsCDoMWX4IDxFMW8cv8Dy_puBt4BCBoFMmSCrrNOJHgegw6XAh2qHmzm_9v7JWoRyKj0kFfFAo72Qn5HxW3FiI0pZjcpUWSMdfL7-AnzUSgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33404ffbf8.mp4?token=fpzRgYmKT9jneVGNxkiJmdFCvZugWwz65EEW3vRYrORnWTks-3MujZuh93MAZjsX3hTJ9C6kfJMlG4lnaxIxS3m8LWVEK0ZRE8tt3Sj4YpCzdaooZoI88ZSUqH9YOvDtd3FJyiD1q6jcCrEvkpVr6Ciy35bDmvv-VKSXT_YaYRN7btJvzkyjH1ANLjBSCH4b1SlAE5l6Gmg5KelbBqb6IRKZ98Z4tdTj3vcNg5wOSwd2SnqbrvvC4DR8a_Jbc5-xTKekmPeRAsfhlmfywrsIPuzI6_k2mit77M_MaHHdhB6yoiG_OQri4o3pwpectznyLfcDClr0slbm2CMHDAp8jaMT1LROF9_RbOK66V0uUvO0SXx1ueIrVsO1AMAir3HL7hTAlCXEGEdXwMMnF6RUAdPmeQe0kXvq_c5hvfkYYpbWYSyjsbFvGUO2Ei1s0EoBUGQUUvET8ooSYFY5ZRfOgtP6C42GLY7sNOB9n214LAnq1ZuPr5y_uXCNA0z74Q4LNzkEHNya0M_A1hnzAbHD55n2sXVIU8Bw-QJ4jzvCbAS41sN5ZUk3GUGnvWrz-iDhsCDoMWX4IDxFMW8cv8Dy_puBt4BCBoFMmSCrrNOJHgegw6XAh2qHmzm_9v7JWoRyKj0kFfFAo72Qn5HxW3FiI0pZjcpUWSMdfL7-AnzUSgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
تلاش‌جالب یک پدر ایرانی برای گزارش دربی برای پسر روشن‌دلش که حسابی دیدنیه
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105507" target="_blank">📅 18:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105506">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b357d488.mp4?token=mW9_wAoqEVhRjL_gu05ZB0S509Ibh7k1FhziIGE2KE4EoIf9SR8fCk0NZDC5pFrHi3iIz-prkP2Sa4eqGgRz49nEssoqlxw6YZFkguYIUveoCdxEJw0lkkI4KmsBmgibRXDy9M6tM8mBFus1GUH_CrDW-Ow9XRfUcw4U6jhNvXtWEf3TTT4yPRoJ4ykTWIgPxczxKgkITd99gN_amS-Zdko2hUqSoIjWOoPW1L8E4ZBrDqoi2zl2JrFbTFLV_pT4VkKmQ_F4Sdfn5HUxxSu9rBNf_hha3QcRC-b16qxEbYsOgmV2ROeLa7EkoewiFv8eJKS7xL5UQlGZWQ2P8xqRAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b357d488.mp4?token=mW9_wAoqEVhRjL_gu05ZB0S509Ibh7k1FhziIGE2KE4EoIf9SR8fCk0NZDC5pFrHi3iIz-prkP2Sa4eqGgRz49nEssoqlxw6YZFkguYIUveoCdxEJw0lkkI4KmsBmgibRXDy9M6tM8mBFus1GUH_CrDW-Ow9XRfUcw4U6jhNvXtWEf3TTT4yPRoJ4ykTWIgPxczxKgkITd99gN_amS-Zdko2hUqSoIjWOoPW1L8E4ZBrDqoi2zl2JrFbTFLV_pT4VkKmQ_F4Sdfn5HUxxSu9rBNf_hha3QcRC-b16qxEbYsOgmV2ROeLa7EkoewiFv8eJKS7xL5UQlGZWQ2P8xqRAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
افشاگری محمود فکری: خیلی از دربی‌ها رو از بالا دستور میدادن مساوی بشه و ممکنه هنوز اینکار رو بکنن
❌
نتیجه دربی رو خیلی از پشت پرده کنترل میکنن، خودم هم شاهدش بودم بارها و میدیدم به مربی ها میگفتن بازی رو مساوی تموم کنید یا به داور ها گوشزد میکردن اگه یک تیم گل زد جوری بچینید تیم مقابل هم گل بزنه یا بهش میگفتن اگه مساوی بود ریتم بازی رو بگیر تا با همین نتیجه تموم بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105506" target="_blank">📅 18:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105505">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105505" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/105505" target="_blank">📅 18:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105504">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTkdFlDO5z6QXGJI33U8u87x-nguGGIVx-wo44tuU1lUdG0guyzZZn72iSiuhDHbaZig5PJ4rtfPb9mN3jIPUccb1cByXGCVM1aLQheZEe1oQG8KVe4dUDdQRkANU_FlNISUHg4Frjx4SRKe3GGiaT4vYKhXLFKlvR48t2YhQOJYG8dLs1Jm5ETXA1e6aIrZR8z8xDXaKK7wXNInZHGUNNrQSShWJwjpeVEXFTqnFG3pTuLjaPypN8sPy0NoP1bnhh7mJwPxkKrLxeutWslfwTmEdJ4GqhAW5mwjA68jA9XB6y3VSgGSccs8RLYDt1r3c2igPjV9rUE7njx_-JbFKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
پاری‌سن‌ژرمن
🆚
موناکو
⚽️
را در سایت بین‌المللی
TrexBet
پیش بینی کنید.
📊
مونامو ۲ برد | ۱ تساوی | ۲ شکست | ۹ گل زده
پاریس ۲ برد | ۱ تساوی | ۲ شکست | ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/105504" target="_blank">📅 18:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105503">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHpZsHViVL3JxMlVl3G3t0gO8nseiuRBoMyR1_VrU0EcmK4kOmgV2pnQ45I8x6DCiPyjmATmKfa1Lhg_VFmdVclKlpdpcAMIks3BP1slTReUFHZly3KBjM8XGLdPBN1d8DbHNVfkDzA0DaaqZ37GpKOT4FKHbIqIkM1IX52hVILF3G12dokECphzIKWBu4j8XNwJhJWg__2faPGzJMBMQKwrTBPYO3Kwa5pP7RzW6xmcU9bkbiTs8DflhR6cvknawv3XN5dsq33VjnnHYld4PjcY62npCK7T-_pESonC8Ao0wpUFP5yH4VeUyo8YEUWUwxBRrioWK5K6WK33HlLWbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
🇮🇷
هوادار استقلال در حاشیه بازی دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/105503" target="_blank">📅 17:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105502">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ea454a991.mp4?token=bI28t2a0Bh4nRwEL-0pi9LvVu2I43_BextT0GRdMk7nTMDxARJ50HOyGBjBUhQCEirxf3muHTBHMlCE0lU5tHDp-MjFoIvu0D23Fh7DSIoNMWc75ZY_qebq37dXtDVwubNPJoE8E2irsKYdf-GQlrlCZbhqTz4liPeEpjn7a5RbBf7HLMvyRN9SaxsNAPKfMyvcl03RH1-kAMl7NW4Ydg6JvHT0Z1SOm4-Q-VNbu40ZXvr89Ck7FdMBufOsKw_bnRiUrohmIO5867BtbzIWuz776iXT--2CyIqsckPq6_QLKIQMNgeDEAj70znX__r2KOx5qqNaaN4msMgis2F3dvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ea454a991.mp4?token=bI28t2a0Bh4nRwEL-0pi9LvVu2I43_BextT0GRdMk7nTMDxARJ50HOyGBjBUhQCEirxf3muHTBHMlCE0lU5tHDp-MjFoIvu0D23Fh7DSIoNMWc75ZY_qebq37dXtDVwubNPJoE8E2irsKYdf-GQlrlCZbhqTz4liPeEpjn7a5RbBf7HLMvyRN9SaxsNAPKfMyvcl03RH1-kAMl7NW4Ydg6JvHT0Z1SOm4-Q-VNbu40ZXvr89Ck7FdMBufOsKw_bnRiUrohmIO5867BtbzIWuz776iXT--2CyIqsckPq6_QLKIQMNgeDEAj70znX__r2KOx5qqNaaN4msMgis2F3dvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚔️
🇮🇷
🇮🇷
نبرد جالب و دیدنی تیکدری و صالح حردانی در حاشیه دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/105502" target="_blank">📅 17:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105501">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10152fc52.mp4?token=ls9YYlMhRqKcLfG0wG4G5Yw0XpNoNUMC3tTgWlkWChigVzRRF805kUcXG4TzLXaQ_PPmYuEdaqucCiow_aDnUNjDOJjwfuFMyfH_4UJFQtYCAjYts7z_rWMGONKwNkxaIznvRwdFf67NAJzN4VMghs98wumls69sGIhuRP4EpY5Xk42E4WVggDBJpiqLhFjJkxc1fGd2joBbOyT0lF1rPvAP7oJsQBUEfMnTVAAb9n0TOLpBiZldY_o9b8eYQNFXB-Wny3nG8f_IvdTvgL2oWr9qONiXR0GoHdwLTkSvqm--fYXc__z4eP4UC0OC-9CE8pHqMickXGRD1oDUVMxIpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10152fc52.mp4?token=ls9YYlMhRqKcLfG0wG4G5Yw0XpNoNUMC3tTgWlkWChigVzRRF805kUcXG4TzLXaQ_PPmYuEdaqucCiow_aDnUNjDOJjwfuFMyfH_4UJFQtYCAjYts7z_rWMGONKwNkxaIznvRwdFf67NAJzN4VMghs98wumls69sGIhuRP4EpY5Xk42E4WVggDBJpiqLhFjJkxc1fGd2joBbOyT0lF1rPvAP7oJsQBUEfMnTVAAb9n0TOLpBiZldY_o9b8eYQNFXB-Wny3nG8f_IvdTvgL2oWr9qONiXR0GoHdwLTkSvqm--fYXc__z4eP4UC0OC-9CE8pHqMickXGRD1oDUVMxIpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
🇮🇷
علی‌تاجرنیا: خودم پیش قدم میشم و‌ مشکل بین صالح و اقا سهراب رو حل میکنم. چیز خاصی نیست. هر تصمیمی سهراب بگیره باید احترام بزاریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/105501" target="_blank">📅 17:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105500">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89dcbb7663.mp4?token=hIWBsE4F1HG74LaJR3fZYq1_HAzABtbbr-PbjxXnfptKaDELOwPlVVjofuTNRkA4XiSkhTkm3VjsCaZzdaXIB6VQ4dQ2MtneYM6J1FzqF-I2oOsXG2W9MXrM7gnYgW4W9I6zLE_jB5CkxBKsLB4kpA4bNYkk7LMfJXzT6lxTIRvqX3Bon1UK2wR1vBhXkqWGdSOYKwCnwpJ4UkqVySHauLn43J_glRyAt3lDODu5DZgOp8e0FjWrLkBjXx4lVzrepsUUGV3lXaf5T6F4fCkWEHacc_XqauEmhXqBSzKVxa6xYwKB-xAE3pqVz_MnRqEjLJIgViIW6OS2yQf-e_S7Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89dcbb7663.mp4?token=hIWBsE4F1HG74LaJR3fZYq1_HAzABtbbr-PbjxXnfptKaDELOwPlVVjofuTNRkA4XiSkhTkm3VjsCaZzdaXIB6VQ4dQ2MtneYM6J1FzqF-I2oOsXG2W9MXrM7gnYgW4W9I6zLE_jB5CkxBKsLB4kpA4bNYkk7LMfJXzT6lxTIRvqX3Bon1UK2wR1vBhXkqWGdSOYKwCnwpJ4UkqVySHauLn43J_glRyAt3lDODu5DZgOp8e0FjWrLkBjXx4lVzrepsUUGV3lXaf5T6F4fCkWEHacc_XqauEmhXqBSzKVxa6xYwKB-xAE3pqVz_MnRqEjLJIgViIW6OS2yQf-e_S7Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
💙
بیژن طاهری سرپرست استقلال: بعد از 23 شهریور که بازی آسیایی را برگزار کردیم اگر سرمربی ما صلاح بداند بازیکنانمان را به تیم امید می دهیم/ در اردوی قبل پرسپولیس به تیم امید بازیکن نداد اما محرومش نکردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/105500" target="_blank">📅 16:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105499">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🇮🇷
❌
صالح‌حردانی بدلیل انجام برخی کارهای بی‌انضباطی خصوصا در بازی دربی، از سوی سهراب بختیاری‌زاده تا اطلاع ثانوی از حضور در تمرینات منع شده و احتمالا بازی روز یکشنبه مقابل آلومینیوم اراک غایب خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105499" target="_blank">📅 16:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105498">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rD5hztz3TZ16twDQjj86PTmC_5SQszjO_g2eiKT338ws6RiWXWiBN1Qj-JNgKuDnni-wM9XgiM0sfzSb5HNwq3rPvP8OmpWvlVS2K95gV3KtKpxGQF_MoaQFJYIjnS-btrf4TADSGRr_ydy2m7AE5-lo6GTKhixr4ULrOOTdKUEroxYdlbN07YlCIKY_-VoAUTYopFlfZnI0qLXxFiX9hoyVU7rph31gEWfTZRWQuZO7btELp0IngCldTE9iNeSgj9TRpfN23vPkLuQlqlheVQzjqtic1w1-f_dk-Fgp-1ZKxCkygsVJJDWy572PFtPKy1T5ntw9HTBYifR_18mnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
لحظه‌جنجالی و کمتر توجه شده از ناراحتی صالح‌حردانی از کادرفنی استقلال بابت نزدن ضربات کاشته‌های حساس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105498" target="_blank">📅 16:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105497">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhmV58yeRkUA8WAVEJXmG89Sg_kfyMpf86PFRvlMfA5AucMTnwSqr14321_aOmSduT8i9WXBO05SAhFN8k1rxCYhr7gM9y4VISeohIsXlzbkZNyP6QUzlU8gpa7t0fltpXYb4NQs2WbD-VI96U7LKuIyS8nFCzz8QPjuhNhB1_HBoLB7z_Say0hIwvBjBaGpdb7lutgugqMnQl02gQnw7Qu1FVqnqnbA826uXnQ9DpyQ1pIb2pmwT_1qDV-imjUSsXXs-COUx4-KKyoxLZthi1rYCzuI18tQjqnhbXOcRIckaEXtYhXjjFcQ9__NaZgvIHGZjtD96p2aPKKU0bwGhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
ترکیب منتخب بازیکنان بدون‌تیم؛ چقدر ستاره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105497" target="_blank">📅 16:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105496">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👀
⁉️
🏆
توپ‌طلا رو باید بدن کوارتسخلیا یا نه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105496" target="_blank">📅 15:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105495">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c1e785e5.mp4?token=lwVUfxLLHdiTQGmuDTRxSnuy9ELwTNkoyVIEGhm2F3R_3FGuRR8T7im4PXZqCrIDJJKrqhLlvG-fzmzbC52R6xH2PbB3T9mFV-pyhVlt0wTlh34CtX416ZUKGWPdxVYtV0PN0LVS8rbJkTXjtMVndqirVDVcqaPHTLDvDbJ8NzmG1yWXeQFi0YoJ6aG-yusUEVAFR_e6VT6c1t6vVXXsIU-X6zzOnyOKfVpfwqs5s8uaTz_CuVC2agEvutA5gWyri9sCduA5sDdiHJ5-EgP7qtWKNUg0dyOCVi0zwEaqDa3_MZ7EE5FujHOFF-HjGMp51aWPhnke3tgUgG-SmJOw-lbF7tva3531cXEidCSWqTYgYdujN5uWGyJdhpj93GdrKxjFX-luItKaOizopj6WSUl2excZMK_UuspN4MFyWcKrNj0Kxl8Zo6hhMbCiMTu2KWKSGmVFtvKFhZGjvZ98H0A7N7NUDAOGdfqOTLY4_X4NSgT-FBL_QJcqzdlqOYCG9riwy0RBpS8BbPAIkkPO3gAV5NixOV1Da7o3SnFDsXG4gahRxQ52YTCqSVjd4xHjclNb5C2FDKEzcMyx0eFSGDzk84iMD09jdlOxZiydNINM0_SgkMdKOYJiKTum61_YHhzIGBy5fKvlTpDqvAJAsywsM7pgLh7sLHz9g1yTCjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c1e785e5.mp4?token=lwVUfxLLHdiTQGmuDTRxSnuy9ELwTNkoyVIEGhm2F3R_3FGuRR8T7im4PXZqCrIDJJKrqhLlvG-fzmzbC52R6xH2PbB3T9mFV-pyhVlt0wTlh34CtX416ZUKGWPdxVYtV0PN0LVS8rbJkTXjtMVndqirVDVcqaPHTLDvDbJ8NzmG1yWXeQFi0YoJ6aG-yusUEVAFR_e6VT6c1t6vVXXsIU-X6zzOnyOKfVpfwqs5s8uaTz_CuVC2agEvutA5gWyri9sCduA5sDdiHJ5-EgP7qtWKNUg0dyOCVi0zwEaqDa3_MZ7EE5FujHOFF-HjGMp51aWPhnke3tgUgG-SmJOw-lbF7tva3531cXEidCSWqTYgYdujN5uWGyJdhpj93GdrKxjFX-luItKaOizopj6WSUl2excZMK_UuspN4MFyWcKrNj0Kxl8Zo6hhMbCiMTu2KWKSGmVFtvKFhZGjvZ98H0A7N7NUDAOGdfqOTLY4_X4NSgT-FBL_QJcqzdlqOYCG9riwy0RBpS8BbPAIkkPO3gAV5NixOV1Da7o3SnFDsXG4gahRxQ52YTCqSVjd4xHjclNb5C2FDKEzcMyx0eFSGDzk84iMD09jdlOxZiydNINM0_SgkMdKOYJiKTum61_YHhzIGBy5fKvlTpDqvAJAsywsM7pgLh7sLHz9g1yTCjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
👍
همسر رشید مظاهری: شوهرم قبل از انتشار آن استوری خود برای من فرستاد و گفت که اگر حتی روزی به اعدام و زندان محکوم شوم، فدای یک تار موی ملت چون همین افراد من را معروف کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105495" target="_blank">📅 15:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105494">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de11aaaa44.mp4?token=exoaFXDRE83Mot7SNHOlWoyaQi54gXwVDrVPL4NcAx51fAegfrz7WXLJVyX5e6EqjjpsNrPfiBHwgVJ77JLG_zr5Zh_E6NQwwBmuT0scIk08YTRYsuyWHZmL2NZ8jK7i0SL-iL-_CyYxCNT7vfOfcbXtCJuOK4b7gG1qqPKvZvbl-qP_PZL-qbq_ibcf6JL4Mfk0sEjYoXsg-rMZNWMAPJxxioAbpRHBI1Hv6Wvh5HzfDQYK6vs0kihHS1itPyzsqovBSPtKGjuJn1Gc5rvfVIKHbp7Y-A0nnMbeaySYb3k3uF44Of9TFajlPZtiLvyb1VGuEl5Ec4A0muk9uN7LVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de11aaaa44.mp4?token=exoaFXDRE83Mot7SNHOlWoyaQi54gXwVDrVPL4NcAx51fAegfrz7WXLJVyX5e6EqjjpsNrPfiBHwgVJ77JLG_zr5Zh_E6NQwwBmuT0scIk08YTRYsuyWHZmL2NZ8jK7i0SL-iL-_CyYxCNT7vfOfcbXtCJuOK4b7gG1qqPKvZvbl-qP_PZL-qbq_ibcf6JL4Mfk0sEjYoXsg-rMZNWMAPJxxioAbpRHBI1Hv6Wvh5HzfDQYK6vs0kihHS1itPyzsqovBSPtKGjuJn1Gc5rvfVIKHbp7Y-A0nnMbeaySYb3k3uF44Of9TFajlPZtiLvyb1VGuEl5Ec4A0muk9uN7LVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
از یک دربی تا دربی بعدی...
💵
دلار: +۱۰۰,۰۰۰ تومان افزایش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105494" target="_blank">📅 14:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105493">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a3572f3e6.mp4?token=U8zDWh8onfSbaxWpV0kJz6sS1WDfmMDa8HhsfUCLGtFpUwb4WY-7mCARcd5iWaW1iOH-q7zVfz9nt_GUqA287d3tzcII6yWKFe_S4vrjoYF2wA3FBOoomWSMYKl9ntC760m76uQgbt69mSeOZiPtK5n-dTBxzL6qC8loikcrqFLXL5rSzDXbijrGWxtqa6S4BCGDSImmEE1QDve0Q2VD4SL6kQN1eb0WNcRWGQ2sE52cNR0GhCJAyxkJMlwyqhc8oBHurnfWZbGkc6POczrhs4ry2MP4QAUqaebEt4ZI3bJhKdiDaimmTGoEvtuhh5ROWWfK0tgq8X5t9SfQJI-4Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a3572f3e6.mp4?token=U8zDWh8onfSbaxWpV0kJz6sS1WDfmMDa8HhsfUCLGtFpUwb4WY-7mCARcd5iWaW1iOH-q7zVfz9nt_GUqA287d3tzcII6yWKFe_S4vrjoYF2wA3FBOoomWSMYKl9ntC760m76uQgbt69mSeOZiPtK5n-dTBxzL6qC8loikcrqFLXL5rSzDXbijrGWxtqa6S4BCGDSImmEE1QDve0Q2VD4SL6kQN1eb0WNcRWGQ2sE52cNR0GhCJAyxkJMlwyqhc8oBHurnfWZbGkc6POczrhs4ry2MP4QAUqaebEt4ZI3bJhKdiDaimmTGoEvtuhh5ROWWfK0tgq8X5t9SfQJI-4Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی فوتبال به هیچ‌جای زندگیت نیست
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105493" target="_blank">📅 14:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105492">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0801904cfa.mp4?token=XFZHPGyEzPvkbeTnUousnuPI_1VOOIibBJX-ANw-ke004qfDVlWDo7pzq6zzUZLNBHKK5Ee3rz-s3MMwb-kKtQ1neWSBcu1Lmejs5n5LG6bnywSqmp16zuwVs-KtvZ385QVJpD_7ocYuEZQYyKGX6Rb-hzUU7O1WYy9Q6o-jlORcDIRHd3gCvm3TaujiXGVOhIGtS_ZGpEnA9rcOzmRMMkuFXM6lr9kO78w9HDxpFAx15qb6uBithgGZV1cxqs7kS9wmb0lYbmLLMCWpro9Ro30We7fH8DbaatUdnRUNRQUIYedpPFGfVL2YcwTRuzbmSFf3D_-tY5EPU-odJD5E0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0801904cfa.mp4?token=XFZHPGyEzPvkbeTnUousnuPI_1VOOIibBJX-ANw-ke004qfDVlWDo7pzq6zzUZLNBHKK5Ee3rz-s3MMwb-kKtQ1neWSBcu1Lmejs5n5LG6bnywSqmp16zuwVs-KtvZ385QVJpD_7ocYuEZQYyKGX6Rb-hzUU7O1WYy9Q6o-jlORcDIRHd3gCvm3TaujiXGVOhIGtS_ZGpEnA9rcOzmRMMkuFXM6lr9kO78w9HDxpFAx15qb6uBithgGZV1cxqs7kS9wmb0lYbmLLMCWpro9Ro30We7fH8DbaatUdnRUNRQUIYedpPFGfVL2YcwTRuzbmSFf3D_-tY5EPU-odJD5E0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وارث شماره ۱۰ آرژانتین که‌ خواهد بود؟
🇦🇷
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105492" target="_blank">📅 14:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105491">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/878e055f11.mp4?token=L6hjQyl77778a_i-m_2DE5XhsdPVvvopsSc5S3T1N4y1JJpbS6sxiU2hKNh0_hjWXftiUiFLSxu9oEs76dwp8GBVrxwdelT6jfbkqNEWc_kwqbiQLc0Ov6PHVT8GM_k3-BjQLvwuNxyBJbdWg0gKvlxSGK-cl1KHFPkaMZbnsJqwibknIgsn8vPeXsosOpky-MB5tJpUDU-f-ZpX7XcjYX9VPRaw8pLAzjQVvk4LsTlBji6tj1m8wFXpOKv61wd5iz2E7zaK7e7aNntW-68Js5CGPcX9EeSt4R2q8YIlQwzzZYXatM7NX_ASNW5axApQzKZ_Jxl5_kISHSekujsKpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/878e055f11.mp4?token=L6hjQyl77778a_i-m_2DE5XhsdPVvvopsSc5S3T1N4y1JJpbS6sxiU2hKNh0_hjWXftiUiFLSxu9oEs76dwp8GBVrxwdelT6jfbkqNEWc_kwqbiQLc0Ov6PHVT8GM_k3-BjQLvwuNxyBJbdWg0gKvlxSGK-cl1KHFPkaMZbnsJqwibknIgsn8vPeXsosOpky-MB5tJpUDU-f-ZpX7XcjYX9VPRaw8pLAzjQVvk4LsTlBji6tj1m8wFXpOKv61wd5iz2E7zaK7e7aNntW-68Js5CGPcX9EeSt4R2q8YIlQwzzZYXatM7NX_ASNW5axApQzKZ_Jxl5_kISHSekujsKpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤯
برند Dyson یه مسواک ۵۰۰ دلاری ساخته که دوربین داره! با AI بین دندونا رو می‌بینه و خودش دقیقاً همون‌جا دهان‌شویه می‌پاشه، و تصویر زنده داخل دهنتونم روی گوشی نشون می‌ده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105491" target="_blank">📅 14:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105490">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📊
🇮🇷
🇮🇷
آنالیز جذاب و دیدنی از پلن‌های مختلف استقلال و پرسپولیس در دربی اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105490" target="_blank">📅 13:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105489">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105489" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105489" target="_blank">📅 13:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105488">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtV6-fze1BceOfLA2o1-HF1dRSKuB_B5ew6L6rYXUXReyAuXrFbAjc8mPfwLOcVtS9blp6BuZH-h8dsso37jC0Mukz5MsedAnmYFS7gZFkaGuE2fvfWubt9482D__56482srjk-4nsNNjj3HE_plGQCLXj8nVwYn_T0bc79iavfG-R2eaAtmytuxdy2OZOXgRz44V352eKG1i9BXKeZ96awhV90RXZBRdhL8t92IyOOEJLINMrPlEY8ozNiDS-sx-DP5ypE6vDjRmz7o2ErKXKpW5Gq4UG3ccXXXMbnO5NBWV1186cmKqr5X1u4URUWKkzW2th4pqL5H5Mkgoxt1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب رئال بتیس
🆚
رئال مادرید را در سایت بین المللی
TrexBet
پیش بینی کنید
📊
نگاهی به آمار دو تیم در ۵ بازی اخیر
رئال بتیس: ۲ برد، ۱ تساوی، ۲ شکست در ۵ بازی
رئال مادرید: ۵ برد در ۵ بازی اخیر
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105488" target="_blank">📅 13:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105487">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21372e66e5.mp4?token=jiGl1YyuY_acXfiXeSE1AT1QP11Y70HA0hEM5JYKsvY-ZHSsL3Y1wbLlNIbWbQzNIH0TkUeLBt2b_i_yB2kmwcYFnR_bn0gp4p4dpJvSVhQCk0PyjlTwSlCtlgdS3ZPgRMBC5CEiCH1TaOW6ppbEZl_um5KA1hKB9rhsWtrqCE4C0dYnQA08siE90efY2TlcF7eH9rMkWFQhEY4Y8sYEOAV4bZDNOsKZKzMNWnBRXWNlc0MFzkSueRt_nhFqjJ0zBF__Hc_yayJUvcX6TdTvH09bxjWTOmQqswdQdkWykoVxNUUb4_a6TD05tNKvlnRiQv5tA8uGlYTGIJTBSEljFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21372e66e5.mp4?token=jiGl1YyuY_acXfiXeSE1AT1QP11Y70HA0hEM5JYKsvY-ZHSsL3Y1wbLlNIbWbQzNIH0TkUeLBt2b_i_yB2kmwcYFnR_bn0gp4p4dpJvSVhQCk0PyjlTwSlCtlgdS3ZPgRMBC5CEiCH1TaOW6ppbEZl_um5KA1hKB9rhsWtrqCE4C0dYnQA08siE90efY2TlcF7eH9rMkWFQhEY4Y8sYEOAV4bZDNOsKZKzMNWnBRXWNlc0MFzkSueRt_nhFqjJ0zBF__Hc_yayJUvcX6TdTvH09bxjWTOmQqswdQdkWykoVxNUUb4_a6TD05tNKvlnRiQv5tA8uGlYTGIJTBSEljFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
👤
اسطوره معین دیشب به یاد بانو هایده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105487" target="_blank">📅 13:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105486">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtH-vggpyCgItwp7tu0JlR3yV2UPviLuU01BK3XvVDcEL_ig6veQgS1i5Fl3Qas3rpK4fuXpuYgxBxjaqavrqqEp_5KQ8W1DrqZKMd9dBwQokpfbosdFuPgNTxSzyJ9HdLPIG3IGJ_0rHOHSyy4Ch2bl_cCZvPJS-xtsBhYK6dicEyHvMxEyJ7CgHZubiLefjk-CqTugnOi5Lbn-lloDiOmiXPaKH44pROIFVm0dPA-CIytDXbYjAv0HVjbw2VL5Mm5Q3b2yj9VRvc33WVQ-MgWcG8MxuT5-Y4PhPaXN1ZLXz1_-01kw_9PqkaB19f_BVLoFqPJZQHQjSCGk275bdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درصد برد ژابی‌آلونسو در تیم‌های مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105486" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105485">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00fbdf9821.mp4?token=LL9zAJme216Kum9rCCsZZ5PLP8HEmYuXtok5WZkoe2fTzMp0EGa_NQeHp0ISOkDRVGcGE6VE6Q8bwfzm4mxRQInXnVeTVs0PaD0VJuA35zcUj6w3KAqMUcdN1GZtffyhMLy__lVXfMOFs4UnmFgziTpcLTkbuXDaQjrWTRYoI8jzAdoUz92zinKSfEIWt7XkIEDLi0BMCnysgwlGcpTkiH_-FPsJRV5FyHYVoMJ4H3hAxfh_IhWW3pC70vSqN-V-8ufljx1SOCJZ_L5Jd_8ePUaL9Tnk4xykvs_fA_FJ-3qrfquAQM5FFj-gYjI6W-wbh5ClG1wF-uzUFxaPrTUR6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00fbdf9821.mp4?token=LL9zAJme216Kum9rCCsZZ5PLP8HEmYuXtok5WZkoe2fTzMp0EGa_NQeHp0ISOkDRVGcGE6VE6Q8bwfzm4mxRQInXnVeTVs0PaD0VJuA35zcUj6w3KAqMUcdN1GZtffyhMLy__lVXfMOFs4UnmFgziTpcLTkbuXDaQjrWTRYoI8jzAdoUz92zinKSfEIWt7XkIEDLi0BMCnysgwlGcpTkiH_-FPsJRV5FyHYVoMJ4H3hAxfh_IhWW3pC70vSqN-V-8ufljx1SOCJZ_L5Jd_8ePUaL9Tnk4xykvs_fA_FJ-3qrfquAQM5FFj-gYjI6W-wbh5ClG1wF-uzUFxaPrTUR6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
اتفاق عجیب؛ نیمه دوم بازی شمس آذر و تراکتور ۱۶ دقیقه وقت تلف شده داشت اما داور دو دقیقه اعلام کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105485" target="_blank">📅 12:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105484">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjfZv_2lVVSZvCjb8hiRMduQGRafq0KEwbqYKXZLlGyE132F0JlSp5LGVXxQMF76ZKgOWdIss9k4uZWQq5UPJ8IHJpOwNBjvz-ov_Zw8ZjMwQ7jjsNwnsoDx4xMJr98cU_z2DaCEAIPkTinZfco5E-x3HAKsa8ZXGC_lcwK0_KOtlfxvHI2bsXn6rrP-cJC_WvySVpOu1wsCq1nqGYhdbr7e6qvqPFCVCeCqO9mpNUIyTQR8lK32B45klAXd_axK6C6wueC-gvXLNTxPDhcGws5Y0QoDMDAuLrnWNwr6AniQM2JagnJNkYXzgz4qC0boj6s6APLECiBWaXDiyKRRxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
👀
نگاهی‌بهترین‌گلزنان فعال در دنیای‌فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105484" target="_blank">📅 11:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105483">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👍
▶️
اجرای ترانه حماسی ‌"ای‌ایران" توسط اسطوره معین در کنسرت چند هزار نفری خودش در ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105483" target="_blank">📅 11:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105482">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPEepEj0gkV0AmsDNW47diCY1H-MRNi4byn4JV3Sf2WTTV0AASzZ6DCZ6NI4UNY9WNv1jY4VZ9YEkcKsqZzF1fwRZJrARHooxpPslgi8fkl43brqMmufxd2JdVrRAahPf6Ebck8384vD3g7l7JRdbOE07O0yUDL7LVDZfqcHfZt4Tqqbwcu3F0srB-QEl156J44AaaszP1lkX7NUdkAL7BAzxea1lWQrlp9ORF58kVmyHJcFxwQcNvcWlI6m_fgWFkWJEC9mOXXkiJk849tS0UiXZaXFD3uqM9HkQP5qyxNSaL-O_JDv1al5YxdtBgLNEF_ZBWQoHPepaUCSFT6w5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مورینیو دربارهٔ بازنشستگی لیونل مسی از تیم ملی:
صحبت کردن دربارهٔ مسی مسئلهٔ پیچیده‌ایه. چیز زیادی برای گفتن نیست. هیچ کلمه‌ای نمی‌تونه کیفیت او رو به‌ عنوان بازیکن توصیف کنه. او با ۳۸ یا ۳۹ سال وارد این جام جهانی شد و دقیقا همون‌طور بود که همه دیدیم.
او یکی از اون بازیکن‌هاییه که دلتنگ‌شون خواهی شد. مجبور خواهیم شد برای لذت بردن از این سال‌های آخرش بعضی بازی‌های MLS رو تماشا کنیم کاری که شخصاً زیاد خوشم نمیاد ازش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105482" target="_blank">📅 11:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105479">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2EY2N2Ez4hPsTjCaBJnWtxvUSLZzgGkOTiepUfi9QBBOHo-NPCc_7X40pj9JdsJVUeqpOUWFvqGU5-drGlX05yFGa0DglkpaV9Zgysh2bTo27lFrSJSXohnBrPRl2fWdYWcSIq30duIWwSpLpNnQIQ3ZyJflvmGQKwwpjAVopEKGc51TPQXXgoox4geyRBmkEevU_NqFV5pUiQKhki_mZQZ3MIgXrHiaHihAtddIy9rgUSBPZ4RoYl-kBucsi2Uz7jBxf-cVKcKBAwTHKuOzxR1wCIN7kpLSwZfhBcBzqnkqcgfOC3t8p57PDsFOG76WgqYFtQNECeROGGouHSqDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/htpm7fWm7mKF0Kanh01Q08VId8HnGbeWmi6SvMQmikKTpHv8JpdB0v-ALksC3WP7W4rBn7ik0H4W2K02ZDG_4_ip2dkn2iLbuz1e95pKnpcjL9A0p8NI6HMyirAfIiVTZNkwzg0wdcpXjxKF3DrALyFkIyLRcYsFjhSJE8fsJ3K5mu-9LsIjxiE1XtPosWYVQPivsTcTSOfmWBUzJC4ZN1SY9UpHN4GqsoVBfso8QB8ZizlGsQmJsmukRkgfkf35Chc8YuB4fu7kcubxNv6cvptSJKITr5JPiI8Jf1PGjpX-U4LvLmvDfXbd9ut0jmSdANvoYUbWiexHpJXXebJGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oCXf0n2anAqLxVFE2ldlSPytaBw5H_IJuzJ0cyJPUdKe7N5BmuN7KDWrVFfBtow2yQrmhuDViNECnlklhyBfEvrbyaSEPidQQ2mSouGccPjtpU5OLUjqDoFxlj157hgaEIyRTw28k5Uxj6vn3CdOymCQzy1-Z9QKSmDzyNB47q5qeSerGClmz-o6TPASCN5DnjvfSFchuM4ZB9d0jReCOvTO1oX4IMtOqAZNbOxEwM7xf51BJJSUljoceLB2He1E_EvEAKqC0DKZeOy9b1eZZJjkhGLlLTnkuxQJpK02Yt8JJnbTa1N1Gu8UAbrtrqSQ6yHRUjxbKryt91OQrtIcdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکاس جذاب در حاشیه دربی
👀
💥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105479" target="_blank">📅 10:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105478">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👍
💥
عایشه‌گل دیشب رفته کنسرت معین و از لذت بی‌نهایت صدای اسطوره ایران بهره‌مند شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105478" target="_blank">📅 10:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105477">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb75d47bec.mp4?token=hw_4LlxmO_K31mcJ6BQEWmXtEzyuIc1WqOJvFPBaUJYm5_G6GKIrnSCRU_XKIcAqHyC6JcfC4kyBEHe1HoV3AQ4C724b1__r7jylUPQVdNgL_shIUBlGYlQgYpz2XzICF8qmX8tZdqvzRxVeXr37u7UBMSIQJ9ZDXEBE8wJ_F4BaFDLCuD6mLz_Tr2CFn2JXVQm5ub0qEjHILvuVogiZ-nwS2yJqFKFtdXOYCPu1ULwhAp1EskGxoEXNU_jSRVlEuW3lltDXKq1_QKE5qEguJZTZrTxLP3aOXt46YziOdlWvRbdJZvo8M1oatqolxxhyofTXL--tKiybUdjO8lzyVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb75d47bec.mp4?token=hw_4LlxmO_K31mcJ6BQEWmXtEzyuIc1WqOJvFPBaUJYm5_G6GKIrnSCRU_XKIcAqHyC6JcfC4kyBEHe1HoV3AQ4C724b1__r7jylUPQVdNgL_shIUBlGYlQgYpz2XzICF8qmX8tZdqvzRxVeXr37u7UBMSIQJ9ZDXEBE8wJ_F4BaFDLCuD6mLz_Tr2CFn2JXVQm5ub0qEjHILvuVogiZ-nwS2yJqFKFtdXOYCPu1ULwhAp1EskGxoEXNU_jSRVlEuW3lltDXKq1_QKE5qEguJZTZrTxLP3aOXt46YziOdlWvRbdJZvo8M1oatqolxxhyofTXL--tKiybUdjO8lzyVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خولیان آلوارز در اتلتیکومادرید موندنی شد.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105477" target="_blank">📅 09:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105476">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0670f6d10.mp4?token=NGGFFqv5gSiGjqR3vAThp5VugoAik9vaKrNFH9NECeb27l9N7MeWwD48VrRZZh_34ScO8YicGPRKczqXJe9CBcoOnPNEVX9nMQbI3hiZBfoW95r-rToBIviqWc7_KYisejDWQP7zb6PSsMzh6X56hAEpgJYpTFBBpJ91IRxVGiqlfqwEvQcZXyfDwJfM2MNIs0_0VOByNuDP_o3YZbAX1kEm-BVu5gEjy7-g1SFJcATvcDQ7Mi7degXCxio5AOMwSVxI-JfVDysUJ2Md37qrD8YnLTsmTkNz4KAGxIT_UawBieDbyRnrbhKbW7vGHu66dmCS2YJOEr7zOWtUrfM45iYWkMNpUKL4E3Zq0JIJ1wTbjNuoSUFeN9lAQSmLllcQjDvIzSsM8zmwLBI9L5dMiw6vdm3qETpiX3E0Bfj7BY0KUQqyCw4oSQxWHiCZIQ3q-OYmIBD40JefeG8IaOPHV8l3Y6fxaYyrZ7TX45wwK0zalpnv1ZhpHqPMDk_xUC843iKC-PC_ZhWctMMHFp0LJORJW3FCII7EsJpISjf_FmpXa1fyryvGAFX_45MCp7imusQLy9mwbnVOkOh9qeYpWATwYB6L6WeeQu50gU_U8m3MlF35m1WnBtB3WfyGrsgZz4_BtVAk1SAemRUN6sCis_dPyapdpPx4lvrJG4Ls1iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0670f6d10.mp4?token=NGGFFqv5gSiGjqR3vAThp5VugoAik9vaKrNFH9NECeb27l9N7MeWwD48VrRZZh_34ScO8YicGPRKczqXJe9CBcoOnPNEVX9nMQbI3hiZBfoW95r-rToBIviqWc7_KYisejDWQP7zb6PSsMzh6X56hAEpgJYpTFBBpJ91IRxVGiqlfqwEvQcZXyfDwJfM2MNIs0_0VOByNuDP_o3YZbAX1kEm-BVu5gEjy7-g1SFJcATvcDQ7Mi7degXCxio5AOMwSVxI-JfVDysUJ2Md37qrD8YnLTsmTkNz4KAGxIT_UawBieDbyRnrbhKbW7vGHu66dmCS2YJOEr7zOWtUrfM45iYWkMNpUKL4E3Zq0JIJ1wTbjNuoSUFeN9lAQSmLllcQjDvIzSsM8zmwLBI9L5dMiw6vdm3qETpiX3E0Bfj7BY0KUQqyCw4oSQxWHiCZIQ3q-OYmIBD40JefeG8IaOPHV8l3Y6fxaYyrZ7TX45wwK0zalpnv1ZhpHqPMDk_xUC843iKC-PC_ZhWctMMHFp0LJORJW3FCII7EsJpISjf_FmpXa1fyryvGAFX_45MCp7imusQLy9mwbnVOkOh9qeYpWATwYB6L6WeeQu50gU_U8m3MlF35m1WnBtB3WfyGrsgZz4_BtVAk1SAemRUN6sCis_dPyapdpPx4lvrJG4Ls1iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
یادآوری تلخ‌ترین خاطره مشترک وریا و سیدجلال؛ خط خوردن از تیم ملی برای جام جهانی ۲۰۱۸؛ از خداحافظی زورکی کیروش برای سیدجلال تا غافلگیری وریا از خط خوردنش از تیم‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105476" target="_blank">📅 09:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105474">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtG2f-G0nqFT2Q9AAbws032oSTd3-VAqaUxQ0ET1cF809zpRB0IQg0Nk9Surg_h0ZdPZf0cnAeYgDtPKv85MEHMW4fGD5HkGeBb2HcrBENs-v-yWxxYEc1VK2-d8rp8zuFdKPnbdRorzxtxORtA8MJVIT6zUNtJ_HX5yo_p8Yct48OaQKXFxtxEiQJLZYZVaowl-CQUHE7XbnT0jPNcpqCkwJrzIuLC5it0C6i9pE54PtFeHne_whGgva5BW9keuV9U5w4L9ydL8RYI3lQUMRtiFmfke9ONLkXD2DNVVDN659g1yykLj-39UZ1OHWLm15Q0Dxgq8h0mKDrplkCo-Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وریا غفوری عزیز و همسرش
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105474" target="_blank">📅 09:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105473">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/084453a784.mp4?token=OQfcvDj8paVQdrwWmDCXaAO_vswJVYBMotJ6FSNK3Y6FDz0QOll1RxUhDGsKHISdSHn5LGcHrrTDTk2vZjKRlQ8l4giUbdnMLS2qRPe3qz7OJ6iGU7EB-oGvZDpidn9PatleJGpEoWeHR9F0q56w50TejzTRDO3PocJXekzb50Ry68BrNa96Pzc3QKVCxX7-X-9iHx42GHhj6lrsVbBqRZNckqWDEunJ221RV8DhpkqxgOD4mr8ykLVSwhyNOismhkmfU_zCukMr5HqG58Ks7oRUsJKzoGpgsTXvxJumtemLq_oVxGFbCocW8CrkPjzezv44eK9KEEMeTkVoJy4S5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/084453a784.mp4?token=OQfcvDj8paVQdrwWmDCXaAO_vswJVYBMotJ6FSNK3Y6FDz0QOll1RxUhDGsKHISdSHn5LGcHrrTDTk2vZjKRlQ8l4giUbdnMLS2qRPe3qz7OJ6iGU7EB-oGvZDpidn9PatleJGpEoWeHR9F0q56w50TejzTRDO3PocJXekzb50Ry68BrNa96Pzc3QKVCxX7-X-9iHx42GHhj6lrsVbBqRZNckqWDEunJ221RV8DhpkqxgOD4mr8ykLVSwhyNOismhkmfU_zCukMr5HqG58Ks7oRUsJKzoGpgsTXvxJumtemLq_oVxGFbCocW8CrkPjzezv44eK9KEEMeTkVoJy4S5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
⚠️
اوج قدرت صداوسیما مردمی در تمسخر و تحقیر رئیس جمهور بزرگترین کشور دنیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105473" target="_blank">📅 08:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105472">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105472" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105472" target="_blank">📅 01:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105471">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQsK48TWshORhKCWUX8yZB5RQUPxOvLF0kNIyjXLIoMhNtY2ZBQRXPB2pKm9sblZVhnLNbH_L_hcMttgGcKxqCjeiVeC5kxkPvfrnBXbOErc8tEUJ_GHuus5rsyaP_7GDc0FLhNKcRFfh674bsrrM8pEalJe2rvXdOmVsku_4pWHMbIpsSqn1cpWh8ScPaTRUhpL6T558P12ZLKPht4nPUccBokfefwOLpFpjqJqDJ8vmNsZJqrsiG_4M9KDHRc8QZyTX08Qnznzj5sF9Y51VDU1m39kIVdXWXEdq72GUiaCA9yMmdlM2cYWNLc5tqIEcbjYWKotoz0Ir49GXMkDYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105471" target="_blank">📅 01:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105470">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105470" target="_blank">📅 01:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105469">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a64bed0c.mp4?token=Bs0tcA4u6vClyM33-eYIjb1acncUZ6yopEAniurEF38OXIqDvYfCTjn_q6gJL-3wp6fMEE_0al88x3zpwHoUmHgucRNcC7o6zriLiC--TA_X829DP5BPpPd5t3vPmx7EQOA29fTnN0W-WAD9kzqTcCOXrMI3iBdibpqy_fZgmv78nZ6eRmyDaUhg1-lFKHqMTDDtNNYC7kfObrCB3G2mkZuDKn1sGH0Lh0DMwkQBHDNQnHRQPSRtXHKvSQUTXG5VMNaCqzJb01OR-ak95JgnTFyqzlCJ-Rkua0grc-FVeJqBo3fux57fGGNEnOcdSukRvdLEeupjR4zRo6iMbFCpdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a64bed0c.mp4?token=Bs0tcA4u6vClyM33-eYIjb1acncUZ6yopEAniurEF38OXIqDvYfCTjn_q6gJL-3wp6fMEE_0al88x3zpwHoUmHgucRNcC7o6zriLiC--TA_X829DP5BPpPd5t3vPmx7EQOA29fTnN0W-WAD9kzqTcCOXrMI3iBdibpqy_fZgmv78nZ6eRmyDaUhg1-lFKHqMTDDtNNYC7kfObrCB3G2mkZuDKn1sGH0Lh0DMwkQBHDNQnHRQPSRtXHKvSQUTXG5VMNaCqzJb01OR-ak95JgnTFyqzlCJ-Rkua0grc-FVeJqBo3fux57fGGNEnOcdSukRvdLEeupjR4zRo6iMbFCpdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
واکنش‌ها به صحنه جنجالی دربی:
🇮🇷
بیژن‌طاهری سرپرست استقلال: کنعانی قشنگ انگشت خودشو فرو کرده و کشیده!
❌
میثاقی: بنظرم باید طول درمان بگیره!
🇮🇷
محسن‌خلیلی: صحنه خیلی قشنگیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105469" target="_blank">📅 01:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105468">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7cfe803aa.mp4?token=vjge9kEUfT9KtfdFN-gZGAqNLg9ILTea5WsfZXeoc1ie95MflDxR2v-HsUt2dhTr6kKCdUMJvU7nzXAEbD8mUj88pTRl3wVZyUrewcT7_uZr-zSSo11irqNtsx_sbqolRotGsoSPlUEzI1R1LBMSQg3ImSHTPWBCP3mmp2hKW9vWtPcqneaZHCI39V4KAPu4IboXhjsZyO98DIQdURSwiLuyVBWuxlOkwFb0zimZ9etDfP4-FEMymW8ZaH5koDGTRDaSGxYeIczZIf_fyg_sKp2TeQK1hceCTC7Cj7Kaa1wCTfhw4JzqTTJU7dxX1EeN1aFQD0BEV2ExNdw8lu8Tfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7cfe803aa.mp4?token=vjge9kEUfT9KtfdFN-gZGAqNLg9ILTea5WsfZXeoc1ie95MflDxR2v-HsUt2dhTr6kKCdUMJvU7nzXAEbD8mUj88pTRl3wVZyUrewcT7_uZr-zSSo11irqNtsx_sbqolRotGsoSPlUEzI1R1LBMSQg3ImSHTPWBCP3mmp2hKW9vWtPcqneaZHCI39V4KAPu4IboXhjsZyO98DIQdURSwiLuyVBWuxlOkwFb0zimZ9etDfP4-FEMymW8ZaH5koDGTRDaSGxYeIczZIf_fyg_sKp2TeQK1hceCTC7Cj7Kaa1wCTfhw4JzqTTJU7dxX1EeN1aFQD0BEV2ExNdw8lu8Tfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇮🇷
تصویری از ناخن‌ بلند کنعانی زادگان در صحنه درگیری با آقاسی که در برنامه فوتبال برتر نشان داده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105468" target="_blank">📅 00:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105467">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e73b0c80d.mp4?token=KH4iuhCgu-_OjTK3O4Tip-pYvimaQOsTzwr-y-ooKpoF4qt9wrTMw4KyGv_O9XBo9chq2WNYByWnMeCTlAihuv1tpxqL48m1Q0PDw2s-qvghqiG1xw_wwZJqbz9Ibem8j9JXzHuy1GjRq2F1RmxF9xNsHWWvFGBZjm4lrDiiC4vOcWftXfkCnd6fla7Grc8R3hCQaqnvUM90kUVj3-JByezf-_qBQJ-4f_HeBuGbUDjz-xfcBDPmWtu_2jsnWY2ophvefxsIX6kzvW8JUqrRNjiLL_ZyGn6LGW2pb3aW2Z_zS13rHkYgYmyFxiwro1Usm3U4jQxxcyUdWRt3XJ0xmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e73b0c80d.mp4?token=KH4iuhCgu-_OjTK3O4Tip-pYvimaQOsTzwr-y-ooKpoF4qt9wrTMw4KyGv_O9XBo9chq2WNYByWnMeCTlAihuv1tpxqL48m1Q0PDw2s-qvghqiG1xw_wwZJqbz9Ibem8j9JXzHuy1GjRq2F1RmxF9xNsHWWvFGBZjm4lrDiiC4vOcWftXfkCnd6fla7Grc8R3hCQaqnvUM90kUVj3-JByezf-_qBQJ-4f_HeBuGbUDjz-xfcBDPmWtu_2jsnWY2ophvefxsIX6kzvW8JUqrRNjiLL_ZyGn6LGW2pb3aW2Z_zS13rHkYgYmyFxiwro1Usm3U4jQxxcyUdWRt3XJ0xmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
📹
🇮🇷
🇮🇷
🟨
نظر اتاق VAR در دیدار دربی درباره صحنه درگیری کنعانی زادگان و آقاسی نظرش بر کارت زرد بوده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/105467" target="_blank">📅 00:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105466">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2b5d1c797.mp4?token=bLp-izXhh5tg-N3pq4rLANgP2cH8Kjvb6r-JOlnf3fBe5lN_GeeHyJTpV3MEuofPhOSMcbDwIuSDYHD8rvCOfDmI3d8eHinuXHTwgdghSb4k3XRz-hH8_LNObasCvQwl6Tp6Sn_4Kao-OrKFP_L-0rPxGvQffvkmT4lJaq4mMYyrijD_pNiDOn3fUqNnCleKDBwbqiPvLoDMikli-wOEruR3dExpv6wTv3c35uFdWGnNWf_P-u7FSmPxnr-lqN9LJb7qRmFnZw1wjqx3SsWx6xDlYm8_NrXnXeTsIzA76WvWDNuGje_IfKx_l9OwRhn-qD7AXBfZTflM8pG24l5jFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2b5d1c797.mp4?token=bLp-izXhh5tg-N3pq4rLANgP2cH8Kjvb6r-JOlnf3fBe5lN_GeeHyJTpV3MEuofPhOSMcbDwIuSDYHD8rvCOfDmI3d8eHinuXHTwgdghSb4k3XRz-hH8_LNObasCvQwl6Tp6Sn_4Kao-OrKFP_L-0rPxGvQffvkmT4lJaq4mMYyrijD_pNiDOn3fUqNnCleKDBwbqiPvLoDMikli-wOEruR3dExpv6wTv3c35uFdWGnNWf_P-u7FSmPxnr-lqN9LJb7qRmFnZw1wjqx3SsWx6xDlYm8_NrXnXeTsIzA76WvWDNuGje_IfKx_l9OwRhn-qD7AXBfZTflM8pG24l5jFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💙
بیژن طاهری سرپرست استقلال: آدان دیگر به استقلال بر نمی گردد باشگاه هم پولش را می دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/105466" target="_blank">📅 00:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105465">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b23d335e1c.mp4?token=ZfiELP4RiyKOnXBmcf0fclVs_XCFFc0Ah5Nv_HD4svIim6beAvhB6BJebn-UEeyNYU5OCcXgOGlQSk_GEun6UZPPT1C5STuiup7IvtZIWGixb_7WE9Ic_r97WtpPGoiJhfy-YYW6DtcAQeRTSqsRLCaxPExJsso6WUsL7xGpIo0Gou2Tqu-JB_bjehYkT4kdt_gt5F5_KBh6DCpgoaSBHGRwngE44Wk9L7fXtYIiYmeGe1V94czcAJJAggq0q7OYWT1qOOCEqL_HXrRsASaasw54E7MfzjMlSWt5g1a03-SwaezT_psBXQme_jPBp_qxXIJpALB_IqxwVyhoOg5rVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b23d335e1c.mp4?token=ZfiELP4RiyKOnXBmcf0fclVs_XCFFc0Ah5Nv_HD4svIim6beAvhB6BJebn-UEeyNYU5OCcXgOGlQSk_GEun6UZPPT1C5STuiup7IvtZIWGixb_7WE9Ic_r97WtpPGoiJhfy-YYW6DtcAQeRTSqsRLCaxPExJsso6WUsL7xGpIo0Gou2Tqu-JB_bjehYkT4kdt_gt5F5_KBh6DCpgoaSBHGRwngE44Wk9L7fXtYIiYmeGe1V94czcAJJAggq0q7OYWT1qOOCEqL_HXrRsASaasw54E7MfzjMlSWt5g1a03-SwaezT_psBXQme_jPBp_qxXIJpALB_IqxwVyhoOg5rVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
محسن خلیلی مدیر پرسپولیس: برای دربی 5 بازیکن جدید در پرسپولیس بازی کردند اما استقلال تیم پارسالش در دربی به میدان رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/105465" target="_blank">📅 00:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105464">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12003f9a0f.mp4?token=Gq3uj1WYkq7N397RjbeOQ8kwIVlu28XTsriM-Zy0usLoz4ST5i8OIJK3JRymrhAKlWY09V9azJ891EWQc7dcQqvvU9iYV1EIfXfojXu1RoAz3F89MZJNcypIO5VED-135EsDmC1bcKq4j-shO2bxVVP5L6ffd5vhGQ2xIwdbCODSCRDO3w2N42leP2Qwsz8KPOOFrZgmKvt2ymsx-uSRz25PYjSD76awAyq01lFVARSfZOeLJ4n-XPhya104NgpvJemzTPzZQZmPEd-j67bhq5wn-n5R_p82_ju3EG9IgrTGuWhHbNg-1Q50-Ht2evh7c63ZZSUsh_viv4TdVgnhdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12003f9a0f.mp4?token=Gq3uj1WYkq7N397RjbeOQ8kwIVlu28XTsriM-Zy0usLoz4ST5i8OIJK3JRymrhAKlWY09V9azJ891EWQc7dcQqvvU9iYV1EIfXfojXu1RoAz3F89MZJNcypIO5VED-135EsDmC1bcKq4j-shO2bxVVP5L6ffd5vhGQ2xIwdbCODSCRDO3w2N42leP2Qwsz8KPOOFrZgmKvt2ymsx-uSRz25PYjSD76awAyq01lFVARSfZOeLJ4n-XPhya104NgpvJemzTPzZQZmPEd-j67bhq5wn-n5R_p82_ju3EG9IgrTGuWhHbNg-1Q50-Ht2evh7c63ZZSUsh_viv4TdVgnhdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
محسن خلیلی مدیر پرسپولیس: من شاهد هستم که تارتار واقعا دارد در پرسپولیس زحمت می کشد اما یک سری هجمه ها روی این مربی وجود دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/105464" target="_blank">📅 00:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105463">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b35cee8f1.mp4?token=Ympgz0wB_FrETUiu76-LiStXl9m5864_5A-dy0oidkbxzOFY0wTjQnWwWkYQqtfwbSluuRQaqsfP1VTpCgd8257Z_B3VlBz1nmO0S9HoWYpqv98laSIbaGthEpfS06lMqVlWJEDv6yjpX7aSDUdOZnFAACIBlzn_j382nKB3U2mlIyqlNXIB0nfebbA-gnKDXaYHjZq6WA_BC3AXhM4KJDKZPXGlso-T8E5bPuZl-Qz3wfpDM5Pu6jE-TggwjqW1CubAw0YZ0BWbTM5OXr929XFYdIWieBeRohEvfKvt5ZWIetwL6pFiRsj-UllljgDpB2vPGHi7iOjwotN1q0z6RF7O-EWrUCvRCoSIDfCUmuXFai-hRNLbXDRCIsLy_J9FgMkBixhhi3xU34STze9wtLDsallqi4OZKrLDtSEQDOLbFkgTOMCLFRzxb_izZq7HO0WtWrMs84LKDF--aOz6Lrhgy_FwZEJjAlQXaYe0uCPJmhkVoqPlRxfbONZtv4JvBUNjQEVLCPHqI8JOjppcuSz3YXfJW94VYzTwK7x6PoGys_ZJUCeeOq9D2og73CbV69UI8pxl6dyRZZGMXcBjKg3BNL6ewyUUtYTtZtrolKLA6ygwJ5LjG2unDHyhE3eo6ngoYjWUYGWnr83hGyOINVtVAfFw2zvRINkwkRJhj1M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b35cee8f1.mp4?token=Ympgz0wB_FrETUiu76-LiStXl9m5864_5A-dy0oidkbxzOFY0wTjQnWwWkYQqtfwbSluuRQaqsfP1VTpCgd8257Z_B3VlBz1nmO0S9HoWYpqv98laSIbaGthEpfS06lMqVlWJEDv6yjpX7aSDUdOZnFAACIBlzn_j382nKB3U2mlIyqlNXIB0nfebbA-gnKDXaYHjZq6WA_BC3AXhM4KJDKZPXGlso-T8E5bPuZl-Qz3wfpDM5Pu6jE-TggwjqW1CubAw0YZ0BWbTM5OXr929XFYdIWieBeRohEvfKvt5ZWIetwL6pFiRsj-UllljgDpB2vPGHi7iOjwotN1q0z6RF7O-EWrUCvRCoSIDfCUmuXFai-hRNLbXDRCIsLy_J9FgMkBixhhi3xU34STze9wtLDsallqi4OZKrLDtSEQDOLbFkgTOMCLFRzxb_izZq7HO0WtWrMs84LKDF--aOz6Lrhgy_FwZEJjAlQXaYe0uCPJmhkVoqPlRxfbONZtv4JvBUNjQEVLCPHqI8JOjppcuSz3YXfJW94VYzTwK7x6PoGys_ZJUCeeOq9D2og73CbV69UI8pxl6dyRZZGMXcBjKg3BNL6ewyUUtYTtZtrolKLA6ygwJ5LjG2unDHyhE3eo6ngoYjWUYGWnr83hGyOINVtVAfFw2zvRINkwkRJhj1M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🇮🇷
🇮🇷
نظر محسن خلیلی و بیژن طاهری درباره برگزاری دربی در اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/105463" target="_blank">📅 23:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105462">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/125703b27b.mp4?token=hFRWnq7hUvYoWshLXk1Iy1nTx0yDuOTKesC0agIhBmunaBidJyVKaqB7MEGmZ8MsoeiM12_aekR47o1WqB0sGdoETGTZ4rd8n0Rgr3HSLxupwEdVVIPHuv7cmWqfUsB8nWEhJh1Cm19SDKyNs3_pjGuPrlPEpFn57HKLbaGXTbnDYMZvcObJIrCkvFWoY8xHgSbs9wEeoqzJDyGtjrXCmeFLjg1sdOFYQKVshk6vSyUMpJ_9lMMnw7Vzj2iztyUOkAyPse-0ASTy6qOvK6wJmgyKbeIO7SaapE0CxM6AsFi7nWzcyDa09OzZ2behtau_WoLClOf6UiyPEcQkmxAp3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/125703b27b.mp4?token=hFRWnq7hUvYoWshLXk1Iy1nTx0yDuOTKesC0agIhBmunaBidJyVKaqB7MEGmZ8MsoeiM12_aekR47o1WqB0sGdoETGTZ4rd8n0Rgr3HSLxupwEdVVIPHuv7cmWqfUsB8nWEhJh1Cm19SDKyNs3_pjGuPrlPEpFn57HKLbaGXTbnDYMZvcObJIrCkvFWoY8xHgSbs9wEeoqzJDyGtjrXCmeFLjg1sdOFYQKVshk6vSyUMpJ_9lMMnw7Vzj2iztyUOkAyPse-0ASTy6qOvK6wJmgyKbeIO7SaapE0CxM6AsFi7nWzcyDa09OzZ2behtau_WoLClOf6UiyPEcQkmxAp3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇶🇦
رسمی؛ السیو رومانیولی از لاتزیو به السد قطر پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/105462" target="_blank">📅 23:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105461">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a92fff150f.mp4?token=h6T0-SIJ7dLuO5bD9UCHOwwDRf49zQF54OUS7lLR7fT5v03b3JeKCBz9yqIhtvpNRTb2OqkhpOHt246CvYxB9p8uoAG9j41tFfk41kMXMaCQxGorcH7f2xVOvm1FwnYVVxse2ra1eDa3O4WdyATpm1_Cqo4x35HB_6blOyuff0mn5F93p7dpfSxUmsZqmxf_7lR1480KxJogwiqUuaNhCn82CWbJUgHsVrkjqg1JUuUBwxUfcvwJ74BY4mMAV7iQH6TgHdJs3Gz7bOtefq1Ws411CxGwkwxD3T5Qv36mhzrkSkAzopLK91ZfkEznZGbzdkYsUD2LUegCqcd8mqLE5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a92fff150f.mp4?token=h6T0-SIJ7dLuO5bD9UCHOwwDRf49zQF54OUS7lLR7fT5v03b3JeKCBz9yqIhtvpNRTb2OqkhpOHt246CvYxB9p8uoAG9j41tFfk41kMXMaCQxGorcH7f2xVOvm1FwnYVVxse2ra1eDa3O4WdyATpm1_Cqo4x35HB_6blOyuff0mn5F93p7dpfSxUmsZqmxf_7lR1480KxJogwiqUuaNhCn82CWbJUgHsVrkjqg1JUuUBwxUfcvwJ74BY4mMAV7iQH6TgHdJs3Gz7bOtefq1Ws411CxGwkwxD3T5Qv36mhzrkSkAzopLK91ZfkEznZGbzdkYsUD2LUegCqcd8mqLE5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
گابریل‌ژسوس بعد از حضور در تمرینات فلیک:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105461" target="_blank">📅 22:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105460">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFlWBBY2e47p1HG-ifhZcWAcn3rko2K09P_P7xQwIIZq024pD7EC7FG5OfONZDLk738JsYZ3tV59pUq-Izk3VcXvRvfj8kmCUStaow9XZdVKg_ha7_blqSRsfTNcdgbE_k0l7ejI1m4oX4uXhDLFG2teLCF-wNiZ6sVyjlaLdi4YN-5MTd4v1-wmWE0MyeHIwSPRgnCvc9_fiy-hOe0mC8rRX4MCbfm9Lsp3CvWjaKRtbAW7lPZ4Ys8lt5QIbz4DacpwK58YL1u3qxI7g41IXnp24h8-Q3mJGsk1efMlyFPpDCRYDr0pAYsrw5h9rBYFZ4PSw5-FyTSmM8DRHSwEKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرید حضوری با اسنپ‌پی، یه خرید معمولی نیست؛ شانس بردن BMW داره!
😎
🚗
با اسنپ‌پی می‌تونی از بیش از ۲۰ هزار فروشگاه حضوری خرید کنی و هزینه‌اش رو ۴ قسطه و بدون سود و کارمزد پرداخت کنی.
🎉
🥳
همه‌اش همین نیست؛
۵ هفته، ۵ برنده، ۵ جایزه در هر هفته هم در انتظارته:
🏆
۵ گرم طلا
📱
گوشی Galaxy S25FE
📱
گوشی iPhone 17
💻
لپ‌تاپ MacBook Air M4
🎮
کنسول PS5
این شهریور، حضوری خرید کن و شانس بردنت رو بیشتر کن:
👇
👇
👇
https://l.snpy.ir/iozfb
https://l.snpy.ir/iozfb
https://l.snpy.ir/iozfb</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105460" target="_blank">📅 22:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105459">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c856b1122.mp4?token=dRehqhEoN1jVkSQ0ylVzs7VcoUUItxZU588Wm6vBnws44OoUl8AeFLWVqp7S7WE20MLactMBy87ycSKx91qpZQxNvpEtbcBj9TqRKODpxU6Y6uXN3Kpw4E3A8yRjLo16M3we8QB9qeGOMAid-iJlXqwQ40xngwX_JUpA_mQP8nb-qjo_WScMEFmCC-OoEZXP-nHGQ_r5w0v6MBImO57bOJ12lyoEuMoPBwnUWcyh6fDMIqWRwERGw3JDCfC2RuodvXipweyOqUNNjELSYrSNfyhLn96Eqz9gasrIfN_0wkIn-7VTvxRan6AInJZ4-BoXEh2QAUcCf5YeZQkEdUTXpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c856b1122.mp4?token=dRehqhEoN1jVkSQ0ylVzs7VcoUUItxZU588Wm6vBnws44OoUl8AeFLWVqp7S7WE20MLactMBy87ycSKx91qpZQxNvpEtbcBj9TqRKODpxU6Y6uXN3Kpw4E3A8yRjLo16M3we8QB9qeGOMAid-iJlXqwQ40xngwX_JUpA_mQP8nb-qjo_WScMEFmCC-OoEZXP-nHGQ_r5w0v6MBImO57bOJ12lyoEuMoPBwnUWcyh6fDMIqWRwERGw3JDCfC2RuodvXipweyOqUNNjELSYrSNfyhLn96Eqz9gasrIfN_0wkIn-7VTvxRan6AInJZ4-BoXEh2QAUcCf5YeZQkEdUTXpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
بابک‌زنجانی از دزدان قهار مملکت: پیشنهاد ۲۰۰۰ میلیاردی خرید سایپا رو دادم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105459" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105458">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tn4Op6ziUyAaZQ65ELMC9Ml904ZlxFRs1MULZ2_SqaMOg1jSoDqNqki3Dr5aPpUH6iW_ywBknSldh8G5zSXA4XFUUBob1WiQJEa4KrXi37k0Q6ae2UA9TyPr9QMAA_7VEjaXeeQqUuBp4GA9rjA8h95reoniO8Hyp6DDIPlPHPqqU-UUfvKCKPPX9Rga5FUXNQAlbXOMmmXsMxi8kcDaaq_EgI1_azLVpIU5_JuNrhkEF__UkRayPxtnlpeU4fzb-wJeYdkawEQXAxzwn049QnhAxESPt3IuaMr_BtFi3KMITQzgWDivNZcqafxc5lhum49q2JF6zStiD9wFMrquaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
💸
درآمد باشگاه بارسلونا برای اولین بار در تاریخ، از یک میلیارد یورو فراتر رفت.
🤯
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105458" target="_blank">📅 21:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105457">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/666c84fc7d.mp4?token=sjLGKtZzhjyRYj4CYfGcBmebOZ9zhXKBT8vQKZ5EWvbJyNXIVzoDIV9mI2ovPLsueVzsqeUMIl1FrADVtlatcwkI7yW-wP_Gm97DTYLSBdnbMrOLAJSllh-3kHgHrK6qSFX1IuhubCcmViGaw-F3eUGfenfizZSKlfvQQ9RIPBB5SkEJ7qQSyPo95tbSApfHnIIE1QTdjfxwcMmCYYG8ZmaroibTm4j1Z29oihisHuOB5nfRA3JH5i83SH5PMfd68BWob9gHn1yYY4BBVyK3hukr9mIq-pG48PhbmfME6N-aHjWqHmxt_Hi-NzzL_y6IGTXjezAXaqMqie5wXqpeiDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/666c84fc7d.mp4?token=sjLGKtZzhjyRYj4CYfGcBmebOZ9zhXKBT8vQKZ5EWvbJyNXIVzoDIV9mI2ovPLsueVzsqeUMIl1FrADVtlatcwkI7yW-wP_Gm97DTYLSBdnbMrOLAJSllh-3kHgHrK6qSFX1IuhubCcmViGaw-F3eUGfenfizZSKlfvQQ9RIPBB5SkEJ7qQSyPo95tbSApfHnIIE1QTdjfxwcMmCYYG8ZmaroibTm4j1Z29oihisHuOB5nfRA3JH5i83SH5PMfd68BWob9gHn1yYY4BBVyK3hukr9mIq-pG48PhbmfME6N-aHjWqHmxt_Hi-NzzL_y6IGTXjezAXaqMqie5wXqpeiDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
چنتا سوپرگل زده شده روی کار‌تیمی تماشایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105457" target="_blank">📅 21:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105456">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‼️
⚠️
دعوای خیابونی تو شیراز که یه دختر به ماشین پسرا زده بعد میخواسته در بره و ادامه داستان...
😐
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105456" target="_blank">📅 20:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105455">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f597aa331.mp4?token=f3AGmEfEjvmP03aYzn-J0DH00B7XENdBp547Wn6imCqZDoGI18MNuUzkUbBxCBzFVfF2Jry5U032bTkyABx-C-NF__0mXBj4Rbccmdb1xOpDlKCCnBOipzZ7fKPtV6IIlIea7erj7yxIqoR6mTiphydPhzNvkgRtA1rraSirPsJNqJ_Koz3ba7agI41zfS2GWLBbfQO3HJamd6Sc1ZyPjB2eKYVHWbyT0UVHrL0vwkSZiOeaVWB1GtdLh2L6qaa2yHrWjfvoOIEJat5PhCd4qGnbUkXh2VUS6YQM9Rgf_2FZQ2y26MrxabrkKxtLD9rAM2li4QVf21OT1sFZexNh5L_nWlx33QO7j5GUbwu81CIwzK6oIDs2RXoqnL8jWYfGuv9jljiid0NtSp-g0-W7dXgq4Tl6kx2g9GJX8_Jr-Y04TOqccLY0ypEcPile-8MfEYb-Gh4pty34Sn7qMXXSbMSW9Wk_3DrF3D3j2jEwCK7a5fos7s-2etX5hG2wGEGZd5ztYW0WmGIhJRLiRrfkWsFFXy_gNWrH4E4juev7eVMvhDFKg17ha37SFXCsjHFV_vy8j8Xr3FJgCok9UxJvnPTKdY4QG-NWKi9U6LjkuinGZb-idhsdTe8R5zsu_usrzsuuleQ1Yj-LJaKwsmKP9uefQnbrgm1NL566vZIeE7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f597aa331.mp4?token=f3AGmEfEjvmP03aYzn-J0DH00B7XENdBp547Wn6imCqZDoGI18MNuUzkUbBxCBzFVfF2Jry5U032bTkyABx-C-NF__0mXBj4Rbccmdb1xOpDlKCCnBOipzZ7fKPtV6IIlIea7erj7yxIqoR6mTiphydPhzNvkgRtA1rraSirPsJNqJ_Koz3ba7agI41zfS2GWLBbfQO3HJamd6Sc1ZyPjB2eKYVHWbyT0UVHrL0vwkSZiOeaVWB1GtdLh2L6qaa2yHrWjfvoOIEJat5PhCd4qGnbUkXh2VUS6YQM9Rgf_2FZQ2y26MrxabrkKxtLD9rAM2li4QVf21OT1sFZexNh5L_nWlx33QO7j5GUbwu81CIwzK6oIDs2RXoqnL8jWYfGuv9jljiid0NtSp-g0-W7dXgq4Tl6kx2g9GJX8_Jr-Y04TOqccLY0ypEcPile-8MfEYb-Gh4pty34Sn7qMXXSbMSW9Wk_3DrF3D3j2jEwCK7a5fos7s-2etX5hG2wGEGZd5ztYW0WmGIhJRLiRrfkWsFFXy_gNWrH4E4juev7eVMvhDFKg17ha37SFXCsjHFV_vy8j8Xr3FJgCok9UxJvnPTKdY4QG-NWKi9U6LjkuinGZb-idhsdTe8R5zsu_usrzsuuleQ1Yj-LJaKwsmKP9uefQnbrgm1NL566vZIeE7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
یه‌گل‌بخودی جدید در پریمیرلیگ ایران در بازی فجر سپاسی و مس‌شهربابک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105455" target="_blank">📅 20:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105454">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJLD1AFPocMiTsXZFr0A5sJsPI5OVCHrS-bfIFyX1aRIzZW75tfGmQLAc4DolgbEEdq7lyd9FsUov1PjEZEI9kR2PNVUszegWimLgVWOaxdb7bZ7dWzr-0_LcHP2ebeE_zX7_U46VTvXDro5lQ1VJwy0vvIKY_esFQNtE6xUfPB0dCQO8QNeJ_h5eUJ8ZOXK56DmGNNIPDq3crfH7IzWeQOZkWTBnr1R0o3-8LrQJoPxbBcVw0a8h_AFELovtK5CCDYZaG_ynVNT2M3nLiZ3FfMWBMe6SqNG83H-eUyBCI2n3-IgMJhYidfoaGxAKw46Urxkia_8SewwKYIw3-Hmnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
مارکوس یورنته پس از قهرمانی با اسپانیا در جام‌جهانی از بازی‌های ملی خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105454" target="_blank">📅 20:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105453">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONNw5lUyl3cMZmk6UabdCOOIa-tmO5LM8GNC2w9-_QGbHNa6dW02ZuOqBXJLWVys3iwcgZFnH2K4fBgCMqqLSQDemORoZLPIKw2VFWwo-_2Hkk-bNKL8FkPixGAzL8LDVZRroYzqGl-BjNe-APgjlmo3d2a6lUF2mr-_PdW4aQ9x9nsH0jhV0_OmrLv1vjwne1YDHR8_tX-4tW2HgdeKPvI_B-gDDn9F9u_rnsYhe2BqBE1Gn4QErAR8NnM3pgwG0OwzV4gkzK51UqRKtCykxenKo9mdgshZ53urxkvJLTrvH68SkvGtTWFNChgv1c9zVpCCzz42PyUeKKnIPR_GKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇸🇦
رسمی؛ گابریل مارتینلی وینگر برزیلی آرسنال با قراردادی 4 ساله به الهلال پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105453" target="_blank">📅 20:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105452">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixwC2WIMbbnRERfdLa3obaPYBJy5LdB7iPL4spMAsWEX51aB7EC9jVXsD1Ey9vCYNGNHVQFkeIYyosILKR0lON9QUEzLW_lgfZwsWo9f3WAnyyDT6wZ-KNV5nZdY8xPGYfFjP3rSCxHPo6z83z2Vi2HHPW0u6xfOYu0o-NUFoto5dj7L491qNiUut5JpNWhhNAaXVhEkWK8IJTjWf3Jqngpx3sX_sK27ZQ6Kb8perYM_MMNhQJnlv4BDQut6NB59TObLTs_jMlwHlU3OBrukcGqGKoKmAAjtPlc3XCsPmRp9UATohziau-tfs4rQavfYh-of08hMKFrBJ7GxsspBJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✍️
کوین یامگا، ستاره سابق استقلال و نساجی با جدایی از تیم الفاسی مراکش به کونگ آن هو چی مین ویتنام پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105452" target="_blank">📅 19:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105451">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pn8QgOeDfaWDpuVM3v_VjG7SuNC_xiiJeo5lZ4uld9Vk6cCt74pS9YVyoWKKSR2mOCgTF-xSlMXyVMy8BQnm9SXjr85zLOBg1qx5YuJ5sjL9pAWYvzBigcO3jmi7Ho4__sDzGuDlyUG4zh7IpybBqGFbWlJ77cfu4Z88WbzZnkRUcYJ_sc1-7qeeF7nDChWm36bdvWihDnw0wgC99a1198Y6XPcn2dWYhc9owDAfKv_L9wyzSDGlzQvee7PCB9pU0dKCuCxlAbHESXo1oYKQ-EC2sw2kCZ01Eu6BmXJvLyF5tPq5fAYbMOgbO-vjGK7QhER1Kkeg1y864XeTx1jrIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
گرانترین نقل‌وانتقالات تاریخ فوتبال
🇫🇷
نیمار از بارسا به پاریس—  222 میلیون یورو
🇫🇷
امباپه از موناکو به پاریس — 180 میلیون یورو
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انزو از چلسی به سیتی— 145 میلیون یورو
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ایساک از نیوکاسل به لیورپول - 145 میلیون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105451" target="_blank">📅 19:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105450">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IERVUwvid1_jE1yxNOsUmx6nDpMTnoJT3F_VFH9sXZegg-3QHc2QAPqk0JL4QNMxo82ID9ZpIwGzm9nWqsV90QeKOUPPy_QTI33ieGRuLi7wwe1fROXhgZ5hO_TUroL5Bl4WibD_iukdLfHDhHMz5ZTg1RDMn6jdG27iO247jKv-K1A97vIqP72MC7srnYLqsHNGKPxKc_8VXu--BW0L-7-SBE8tgDQXSy9Bx0Zp3XrvfTLWYHO_XAMmm1nuqMmxXdqpft6KS2uOPCPXrBn7bSisBW_p0yU1X7b4E0PH_BBW9LwiXitlrVehUDLP-4hNS5n_diQV1nWA4S_d0rYI7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسلامی می‌تونست تو این صحنه گل برتری استقلال رو بزنه ولی یهو از نوسان قیمت دلار سردرد گرفت.
📱
«ℳ𝒪ℋ𝒢»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105450" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105449">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfXmKGM1zAxmMxn2f7u87eju8R0MW_Bz3wwGoAkTOK7J0UctZP4Zhhz1opXctxMFUuGJgGfKbHEvVlHeYRx06y2AGsulgITqNNYxXzKfgxYuWgyGRyQnFHA40a15FFcMfZecxokyKj7Yz9skXxTaUYWIPFJlWMbv17DJS_6TNoODLGDVpT5V95Co-Omj7lVCVAuXH3JkAdE2pt00AI615l0yBGCXhJic87bvY3FWvHEstXFKqBR68pDtcSLOz-HRS-FSwH9cQ6PfO0vueZJsLmqOrNxly4LdtRMY9hUJcatEIc1NpCW26hq4iI2nppoM_ZFsqd9dJ68kBfjVhj8HYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد خط‌حمله بارسلونا و رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105449" target="_blank">📅 19:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105448">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9XDmwWWvO-euKoA-pyVXsxrc9WWFD3cLmfLcxaSZzHzMU6h8uYVT8nRhctwpPiFbdFX_Bwolnc5gXZ56N5_ow3mM0Iog9Vi6HJixRsDXPyLJG5LPQwlkLplWhhk36r3vmKO4NHiiUpZZ7E524XsvJEH4snHG5vaC66e7pbKf316RKlaPIox6ug3zlBkhgXlKNQV9Gh7AQybkOED0NSKaRjejcfW4ELWuTjQhi3UESXAToS4esdTl48mE01RXJ_h7LeCNvWV0D_LXv8p6Mi6jGdOIE8sQ1BDnrpIcBhghQ_sSqHNbsE4tDhrJspy_dIDQup5zXN4kTB0QZ62Zy60VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
آسنسیو مدافع رئال‌مادرید از اتهام پخش کردن تصاویر لختی یک دختر ۱۹ ساله اسپانیا تبرئه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105448" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105447">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzXnCGIfNKY_j2c_EeUMf_EKfJ1TNg34288MASD8IC8ORa11dSx6dMIqCGUML4-5L5FFEmuuvd0uL-NBdvUvt83DLnuoIlFaVWW3HHMT2yJ-UOlZJFIOQk604KikPLKJ4dP_3bbLYi0zTOLCMTn-i6SBa_NVndMwDswWTCNdgnUumHAOy3DXnUaWknxRvn3MCdBN-ChE3Ur9ZUWXj0pWEqMwgQZmRKGVgK9G_xm8oTYjDmjBnYkWkFw3cVSnz4I8QTCPuozpT1lDemAO6GP0WoQ1nLwv_SewUmiBIvqbcFpusKY2EHOpOKWNdvSlJk20auNmYYhytHb1tyy-JvIfvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
😳
ترکیب منتخب ماه آگوست بارسلونا چیز ببخشید لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105447" target="_blank">📅 18:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105446">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d07bdd0548.mp4?token=pPFdVlTzG9RlqG2V1XDVcdK9G9IFbj3vkL2_BbwCipUUwe8ODvjbxSfdBC_NLlBbEXdzUXt68RBevLKFi1jxbpMpVL_cz0S4-cBT7oOIiyXp9fIRiqzBv9HdsXVFc_xErzmbvWSTobZ16sASCZxaykfqMEXLW-ItwjIPsS2S0sQ3oYKhv1lx_FvMK0caegJ7L3V5JyDCg063xN6_-syUEIwhcTdA0rAhsfHwjWVT8-9S6Oe1Nge-x4JJifoS-zPTOI3qe9S3GJeX7EuZeJnR1gRPCljKF9Hbt6Qq8DsmV9Dup9yeEqhnqlpii9if0mDo1H6giFsf_2cNinUsylWNow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d07bdd0548.mp4?token=pPFdVlTzG9RlqG2V1XDVcdK9G9IFbj3vkL2_BbwCipUUwe8ODvjbxSfdBC_NLlBbEXdzUXt68RBevLKFi1jxbpMpVL_cz0S4-cBT7oOIiyXp9fIRiqzBv9HdsXVFc_xErzmbvWSTobZ16sASCZxaykfqMEXLW-ItwjIPsS2S0sQ3oYKhv1lx_FvMK0caegJ7L3V5JyDCg063xN6_-syUEIwhcTdA0rAhsfHwjWVT8-9S6Oe1Nge-x4JJifoS-zPTOI3qe9S3GJeX7EuZeJnR1gRPCljKF9Hbt6Qq8DsmV9Dup9yeEqhnqlpii9if0mDo1H6giFsf_2cNinUsylWNow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
آمریکا برای اینکه به پرسنل ناو هواپیمابر آبراهام لینکلن یه حالی بده، برای تعطیلات فرستادشون تایلند. از طرفی تایلند هم به پرسنل ناو آمریکا اعلام کرده که خدمات جنسی زیادی در پاتایا دریافت نکنند تا فساد اخلاقی در بین زنان این کشور گسترش پیدا نکنه
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105446" target="_blank">📅 18:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105445">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105445" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105445" target="_blank">📅 18:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105444">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mufw5h5Nt5uN6X8WjxDs2X_FcD_ACSUp9tDF6WsJU6hhso8sN-t5Ia1Uf1AlTH_jGXzCXcenATAtfo4TpK52f9bz6wJm-cHCUlA6ELQnx47UtjwvIU1Y4amJgfEvMVqPEJ8RCjNIoL-Acx3jXPQznsPqnnMHcIjFySdES2MJWlIQ2Y2g6wgJdyOhgZ0wW3nW0EjSeEKrwjCBsMixlt3RURkGUjW4O5kcO7bSHpTybJ-bRbSl83YRRX4eiSboNcVEsS-YR-q0YqYSNji2SgnePCFp7BtdccGQdG_WQxS_YVV_mldvb50ZKlcumIAugeb3rKlz1OEya-9XxCVq_atzwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان
US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105444" target="_blank">📅 18:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105438">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kGmzs68lntiV5MmvqesDeKg4R6WGaOiQMdH0S1bVjisOW5eAhrigoQ7Ov51XwgYCiN88JsCvHoPX6KuArQ7Sq2oh2-nXXtt9s9_FA1jaQYWHv_yVmiBn49vs2qpbbQXPw0PKn87qMpkna_zafzwLeFybxzfnrHtdySvwb-xQnZYQkkFm01M3BsgSrBvcB0LKY1G5PWFMNb4OmC-7gdzT8mFntNBpxxpIsjRgS4-_7IKwvlV_PlD68KqIBKZ35eUXLzpOe6-fKe6QUddEKzL4VOIQoyQ4hNJhNH0lJUzWZA84i60NX1E42QVAiqKsEuaddih-d3ETzIKC8sUTgik8rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/is34hG5nw7mcjdclma03sVTjv2EprYlBD4vUlxiPQA166PxL0UgfCP2KZAbo2vC7zIXrCFXey1wEvFScWjAc7j4mh40-wVbbiti4RJHssYS1tRQENMU6bdibskj1NWUkcjvUlxgpjGWOyF8KDJP2zsQCHyibMopWfZUD2gCFOYOVh3eA4PjERwhkFMzp5_1cAYPaA1XT_H0OdaicKtNOx731Ejc2nQFzOjPwbkBPK33cp6-_icYhPjBRjGxQkQG07RPkoCNwRGuuqmbl6U-nKzJ6nH5twZa_hKgbzRHWnTuVEsJAaVrzYgTo2zFsyQOW5Edr_GxktA72Api-csQn4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ciwJ_1wZB-jMPAWzKJWLWSvIo5ot7XHFjGTA6rEGRLZx1PBZeWTebQ3ljfXAHVcj3cORdZZAgFHGUWrMn4qBZXTOWg16_A1qJaXxG852tfdsfZ-w9AX0JDbc47yubuf1_x0uR1skINDNcBzS5a_IdlxqRWVRuTdg-oUoFz04GaAl8s-ICZO8BvwRQfo0VfIAJ2IpwZhQ8btVbIodT6p-tvoTlFNtowN3kYn9iBNYu0gXLKCJu4KAveQYT7ma4qz_0ayfyRnzNvB2XM4-UTJsTo1h-6YWBm7THv62xAGAuY6ktGqQptXfVYeqjQWBvAf7xwXA7_w-AFPEGG87CCov7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QjpM-dGdNgzmFdTkAJCA2OuBarsRBkrPQtMOCPcHJfZMxTMVz1WMxHDkPMtXqlqWYeNbH-BPLX7Dp3TFzuxV2O6Bbmlhf0A-j_z7WAdhE7WJDm6qQxDo7KcU-BDJEP-QWN9QDRVOIgKIXVpy4-1paWLsQ34MnEKiOWc3HmJxoacJSvw84_o7oBYZKkFoeCcvGOmKmurCHgl0zhI9CaqTt664-tz3L_bBVLIsq8DRdpiXnRZzlk_WMcetqtACWtLGKk_XZf_ghk8Qg3mOLHvaBO3BSlqn8IP01W6u-yyjF80mwkbFndnp__io71Oyld8em9AjfBJgYTOV0BE1v3Twcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k4V_fVde7e_iBZtHQASgpHnnV1TzHUYC_FW1M343AEbeq0_czlx8STzNqlSzm5wq8KFddxluVl2jNut73pGmwMvTHDqkW2DkXomQ6KmF6CvCYHk1xG-srn4hsRyTyvyBQcmc6-1hZg5Tx7lv7P93LFfje5ql7CHHlWQZ8Yj8aHCCoNRINnRPOX0CxUK9kAUpr9Rrm4f00PffHAmO1cuhY2skQW_oWLMqBMuH-jZiI6PYNvXUTDNjAib_FlM5XMTv9Mr5MN3dijVzZZ3i1GNke2i0J9Bo_KlnFEFIiT00lnsqUBHX8ljHzcrjeoKjuxX2y7WkIVkLoyRs83LOELmbyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
هوادار بانو استقلال در دربی نقش‌جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105438" target="_blank">📅 17:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105437">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3894ae1ef2.mp4?token=ZCIeJ-L06bqVtHrbR5CCLLans09P8b8KVToEPJo92SWY2_VGMJZqiv52jepwFKhl9YFsQAlVtgEkI603HdQb-RWbfke5y70Qduv-G1L6Qr1QsPka_VKA9Mo5iHSzaw3tpe5uiX62yGJuGQg5DKElMEdVCoX48fprmvapgHa-IF1c30uX4EpqMW9M0WNV-ga1rr48TtdzeJ2a3qm6Tx0wA0yn4FbOe5FzXKSwn3COlZF5PGdiOJfh-N0Ywmmzrc-eq0yphT5RoLXbHalthJBa7yAW0UN2QIvq2frUXOfoIZuEK4asBgXcm2dYyhEAqKjnLLrPYdjgqe9WktpBOQrxnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3894ae1ef2.mp4?token=ZCIeJ-L06bqVtHrbR5CCLLans09P8b8KVToEPJo92SWY2_VGMJZqiv52jepwFKhl9YFsQAlVtgEkI603HdQb-RWbfke5y70Qduv-G1L6Qr1QsPka_VKA9Mo5iHSzaw3tpe5uiX62yGJuGQg5DKElMEdVCoX48fprmvapgHa-IF1c30uX4EpqMW9M0WNV-ga1rr48TtdzeJ2a3qm6Tx0wA0yn4FbOe5FzXKSwn3COlZF5PGdiOJfh-N0Ywmmzrc-eq0yphT5RoLXbHalthJBa7yAW0UN2QIvq2frUXOfoIZuEK4asBgXcm2dYyhEAqKjnLLrPYdjgqe9WktpBOQrxnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تلفظ نام سرمربیان ۲۰ تیم پریمیرلیگ که ویدیو بامزه و جالبی هست
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105437" target="_blank">📅 17:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105436">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f4ef259e8.mp4?token=pW4LO8WUfkxHAvffgr9ZLxEP_kudF52Xfjgo01lOP_SPc-zbPJiByqQM2yeSMOSo-rYvHqSyKzb3l_J32jyLR4efGIDJM9mvgUnfnJ9ulTsrQATCXqLIsS20upRakkkmt1eupvtHgH-b2AfauU8Av-K5D4VowHo3NqO8-BqHb9oSlfr13cCGC3Ge_gX2NSz8lm_nzVHEmYtr3HZd4aZF4QnNk17tAbwleBVKlxM8d4pWvlztngKo3ok0TBc4uJzXhaahprBnSjKbmLT6pAIbTqbuociPa9IV9pi0jwhbmhsBLpNMD-3J8o2a7iOvoTmqhrflsgWIUVqRxJPxpvwLEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f4ef259e8.mp4?token=pW4LO8WUfkxHAvffgr9ZLxEP_kudF52Xfjgo01lOP_SPc-zbPJiByqQM2yeSMOSo-rYvHqSyKzb3l_J32jyLR4efGIDJM9mvgUnfnJ9ulTsrQATCXqLIsS20upRakkkmt1eupvtHgH-b2AfauU8Av-K5D4VowHo3NqO8-BqHb9oSlfr13cCGC3Ge_gX2NSz8lm_nzVHEmYtr3HZd4aZF4QnNk17tAbwleBVKlxM8d4pWvlztngKo3ok0TBc4uJzXhaahprBnSjKbmLT6pAIbTqbuociPa9IV9pi0jwhbmhsBLpNMD-3J8o2a7iOvoTmqhrflsgWIUVqRxJPxpvwLEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇹
سازوکار نقل‌وانتقالات در باشگاه کومو، از زبان میروان سوراسو، رئیس باشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105436" target="_blank">📅 16:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105435">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f719399999.mp4?token=XciOYSgFXbDslqHM826YgyAQLLHSTI056tF3_CwLEPqS7MBj2nwqRK5liPoX8SE2-ym6YEhlxDlem2i3T86RAKUWAhm23jsORO0BCW4YP3Wr_p6rFQuxMhrYI39VsdOsMx_JWfMsBb62sUOW68CrsqBuaSJbltd5hkDofF_r57nOhlkaZFBycUdouM2Pr7Sn6obaYrsCWyrf3U2IRoiYvYE_KoeDN1R5vDt-LQM2rpYX-JeVU9GzZ-O0p9xI4MfQP-it7hIlvdfQxk-rFMwMsHn171Es00JEdD8MSt92IK5yC5MxHEO-Z7AnzbCUBCqZY8GoeTV2NVxDLFvln6snRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f719399999.mp4?token=XciOYSgFXbDslqHM826YgyAQLLHSTI056tF3_CwLEPqS7MBj2nwqRK5liPoX8SE2-ym6YEhlxDlem2i3T86RAKUWAhm23jsORO0BCW4YP3Wr_p6rFQuxMhrYI39VsdOsMx_JWfMsBb62sUOW68CrsqBuaSJbltd5hkDofF_r57nOhlkaZFBycUdouM2Pr7Sn6obaYrsCWyrf3U2IRoiYvYE_KoeDN1R5vDt-LQM2rpYX-JeVU9GzZ-O0p9xI4MfQP-it7hIlvdfQxk-rFMwMsHn171Es00JEdD8MSt92IK5yC5MxHEO-Z7AnzbCUBCqZY8GoeTV2NVxDLFvln6snRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
امیرحسین صادقی خطاب به فشنگچی: کم‌کاری کردید باختید بعد می‌گویید استقلالی‌ها دوپینگ کرده بودند؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105435" target="_blank">📅 16:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105434">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/855a5a9849.mp4?token=W15OvAefVuFvA3ifTg4LnZkRMhtPIZVHYdyS-uim2wESZi7siKd-326OPbKhrVqJnzGmygQDV2nrAZTqm1vK1WxF9a7Hxsm_ZX8sLEui2GyvpM3X0lfi_gLCKX3CrSSKdN2QxX9UjQM9yjjOZxfhKItKbYJPGxms6TJGMXh41O_f9KG_bQFOkdf-xpnwN6Dl-R4mrXUNiUQT2Gi0wmY3pXrysXgtI1XxdccLbyDhi-_xnSIpnqEqR3UWMAqHGjhViHPgQQrK0ybE7JooddlN4JbGeTEMeVI9naD8lVgAw8ptpy-fEKp2PqWkX_612rtJg8MrOXRnwnldGOmB2MDwPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/855a5a9849.mp4?token=W15OvAefVuFvA3ifTg4LnZkRMhtPIZVHYdyS-uim2wESZi7siKd-326OPbKhrVqJnzGmygQDV2nrAZTqm1vK1WxF9a7Hxsm_ZX8sLEui2GyvpM3X0lfi_gLCKX3CrSSKdN2QxX9UjQM9yjjOZxfhKItKbYJPGxms6TJGMXh41O_f9KG_bQFOkdf-xpnwN6Dl-R4mrXUNiUQT2Gi0wmY3pXrysXgtI1XxdccLbyDhi-_xnSIpnqEqR3UWMAqHGjhViHPgQQrK0ybE7JooddlN4JbGeTEMeVI9naD8lVgAw8ptpy-fEKp2PqWkX_612rtJg8MrOXRnwnldGOmB2MDwPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
🇮🇷
روایت وریا غفوری از گلی که آخرین برد استقلال در داربی‌ها را رقم زده: مسخره‌ام کردند، به خودم قول دادم گل بزنم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105434" target="_blank">📅 16:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105433">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d62c5ae06.mp4?token=RjU1fhUAAb9lL5knnFO-ranFigjynJpUjdU9KDAq-yCxwsFTS04KGP163dXjO1b5sHn0XHtRKItI68ov_l3t6c7v3yMPVv76LcTAFSI--X2lAltA2pzepN_j_DgALTAeexOGfjAUtbV-LX53TT9YNhVXH4nTcJlvzBKt4EAdPGg_WigKM27CeTavw6F7NoYS5615dCZEG3kC9PPzpjh08QVY8wemfKRbe0n-oeCxiE4EmcCE9frsiaXFL1DpiPCyf1nvyYotfw_dVwVk8f48vlBxAD7jTMuHzjkOgjokTQPtqLZHTXLOY4yrOogyubbYgiRXBE4UqV0Wq9GfaN84pLEb4vm6b2GVOnTMMoCwaqNT-xMw572UqM4IeFS4ltdp1PjPXp7L5WMAYaxaeY278ijbtBjYttCzq10_jq9Hcun26Z9ZbpXhil9TeA4ieCmEnFTMkoqXhhIRkNQJMOX4rFN19xxSqUB-YCBgeonI3eBvPiXMZ3-eRPH3dGYNexeOYU538QO0x7rpVwOszDDTZAGsXmOu2S3b23JCExOkVZH4xjQThaAFX79XLWiUYLraJsirGrtMvdPMY7lQAZS-XaKkqkRTFZG5KdblH51QuGbMQFNR6umqvDsLDk4fbt2NcpLKrJNqZC3zIr7QDqShxPAja5lnx5QnDsr2cCrkAGI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d62c5ae06.mp4?token=RjU1fhUAAb9lL5knnFO-ranFigjynJpUjdU9KDAq-yCxwsFTS04KGP163dXjO1b5sHn0XHtRKItI68ov_l3t6c7v3yMPVv76LcTAFSI--X2lAltA2pzepN_j_DgALTAeexOGfjAUtbV-LX53TT9YNhVXH4nTcJlvzBKt4EAdPGg_WigKM27CeTavw6F7NoYS5615dCZEG3kC9PPzpjh08QVY8wemfKRbe0n-oeCxiE4EmcCE9frsiaXFL1DpiPCyf1nvyYotfw_dVwVk8f48vlBxAD7jTMuHzjkOgjokTQPtqLZHTXLOY4yrOogyubbYgiRXBE4UqV0Wq9GfaN84pLEb4vm6b2GVOnTMMoCwaqNT-xMw572UqM4IeFS4ltdp1PjPXp7L5WMAYaxaeY278ijbtBjYttCzq10_jq9Hcun26Z9ZbpXhil9TeA4ieCmEnFTMkoqXhhIRkNQJMOX4rFN19xxSqUB-YCBgeonI3eBvPiXMZ3-eRPH3dGYNexeOYU538QO0x7rpVwOszDDTZAGsXmOu2S3b23JCExOkVZH4xjQThaAFX79XLWiUYLraJsirGrtMvdPMY7lQAZS-XaKkqkRTFZG5KdblH51QuGbMQFNR6umqvDsLDk4fbt2NcpLKrJNqZC3zIr7QDqShxPAja5lnx5QnDsr2cCrkAGI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🥇
رضا قیطاسی پرچمدار ایران در بازی های جهانی عشایری به مدال طلای مس رستلینگ (چوب کشی) دست یافت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105433" target="_blank">📅 15:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105432">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44a16cd1aa.mp4?token=pABQICULdVzgeyaC8-BULsxTg0JL8yikl4Xj5PNNAW6HtZgyQxzUB18WZXFxmup0ZgH9GN5fZviW_z_mVmG6Vh3VTRydTKCnbkDqu2TFWl2F4fVQFAPikgRfus-_xzdHmTMUs-t9IvvytluePOv-f4QpT9vtjsgJDUjDxjCzIhRHsRmPJI2RkNvt7z-GqDDzR_E6atj1zu_WUGEqQ0CDczeyt3iM4NEwxOXvh5UpkuB0RTQGyMsDiNIpQM76rv2JR1W4ZCPaudyBvauAVN0FxAd3Igs3PGGbMKsYdzk5qQSF0zEjxBOitsV5ct9tSD5mSbwG7vuG_LbFpSoOjLpHMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44a16cd1aa.mp4?token=pABQICULdVzgeyaC8-BULsxTg0JL8yikl4Xj5PNNAW6HtZgyQxzUB18WZXFxmup0ZgH9GN5fZviW_z_mVmG6Vh3VTRydTKCnbkDqu2TFWl2F4fVQFAPikgRfus-_xzdHmTMUs-t9IvvytluePOv-f4QpT9vtjsgJDUjDxjCzIhRHsRmPJI2RkNvt7z-GqDDzR_E6atj1zu_WUGEqQ0CDczeyt3iM4NEwxOXvh5UpkuB0RTQGyMsDiNIpQM76rv2JR1W4ZCPaudyBvauAVN0FxAd3Igs3PGGbMKsYdzk5qQSF0zEjxBOitsV5ct9tSD5mSbwG7vuG_LbFpSoOjLpHMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
اسپویلِ بازی بارسا-اتلتیکو در این فصل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105432" target="_blank">📅 14:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105430">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M4BRTO-EqIqj0MU_Uek8Nkdj5bu3FJgakSy8SeeVswVEwAkGmVQtusecuYc7zEwad7-X7KPHpA21rgH1FSBmJb03Sz7ZhJpyxKKoEvBf0cyl36j776nWBnaLRvqv6XajRTHelGmqbIwq-XlI50TEQ2-pJMDcZDZy3Yw38rgTbPI33J0XwHb0-6ew9_pdk1TtNZxq55pATw-pIaFAlsAv-eemCMTNQWJp3BNTVzLdNLCn4xCeFqrSSRFjlOPKiOSGsHviJwK59N8YVKhHtDLmMKZLcAqsFWAJ03EfQm1Jb3wmri4IeI2df_LUcuNDrpMMqY-y5TgyhaDJ28-G-TsKoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ALRmtkBWWXaWZS7LZWfhSKBGk9A-VXFd-B-gIPoddwmkj-K-IE7xJYlJ9EVxcROvM5jaAJj4zAdJ8ZyL-NavIN22MjT6Ft0oatFpAffbY1H1A0gItTZW9OmJMBNy8dzVPDzNQgErX61OjbNbG0jKIVdg6D3Xf5WOvuaBLsti6tbp0o8vQgootfsgoUUY-vCHhvRAHQqDRulRvAPoUDStu2Jc28RHSx0S_Y7f3usI66GVefWXxiHGSZ-ucguv_m_8jKCHc4slJUHIVsIvjNKgOblcMC1I3xe3ijIswq5MJhu8LIAMYb1FHFUEaAGQmjkJFj03iv9rpJhQcFMAQ78SHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
عیش‌ونوش لامین‌یامال و‌ زیدش در پاریس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/105430" target="_blank">📅 14:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105429">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HesrXs6uee_a9FkaE9f3AMucy3gyCIS-RVIdtnDX0927LNpQnYetob5DdhuE5VhdskdNrPyewx9lG-9Dx_yCI8YUTtz7_nWK9xA25AgQ_QIBm3jBoDHtID5U1KHUb45JEIZTv6WwdsCqJRpkX-InYqQccaAxwlCquyHuWI0mM1Xh7VcM4-RykqxNYuFT82EY098y0OSxRAZiO5sl1xVKWC_hur5aNrm_PBDdXabAkowjHpO0eeKZKOOGX4M78eeT-c1pncZ8U5dwO3ztGQWH_fjlOmpiDQud2j8gwbczl8GkxTBqiYApFimMAf3SrbOYvMvC7cf65PrTkbk5fXk5Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
‼️
ویدیو لحظه حمله حسین کنعانی و چنگ زدن به عارف‌آقاسی مدافع استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/105429" target="_blank">📅 13:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105427">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAtMK-8hg38qEDAn_H9MXcCNzaeIRFlA5MrIOjpsIcroOqcEM083_9XzvrLIOxQqVjrsA3jsyAknIU9riHhFKcBqKco_crE7qR_qwWLsvuIku4V5gmrlSXOXyoDGV3MSFrMKH8_IQLZE2iz0ojGOXwAiAckr5FihRfJJpk3C5NqRhmAemvDM_lFof5ut8qSMEgM5rwM9xirLQ25DpZKAx9AVz8yKCYlmLrkac3VYfRNKZ_KIiF5LIKEmaftNZvZrsYnCnCcR1zzzHLOz0CpilBCAA6NtfcOhetU2Gg_Gg0tB6Pt8HU6E6wMOZ4ktn0Zld8dM2IaATODbGQNtxCCRCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📱
استوری کنعانی‌زادگان کاپیتان پرسپولیس از صحنه مشکوک دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/105427" target="_blank">📅 13:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105426">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FA7h_EUx95vkcJY0ORge8VvolsGdH7zYPgATtJ67b2192PXgzMSivtGLaf3zSfv42eL_l96dXXYaZB_4MgAxJlolS5liDGhnuVUScLzeUHjWUNFgP9v_U0z1Rl3RbZ2YrFNLux9ese5IAPXsuiiLbOrpeHQpQJVKG9dQD6LUC83EWwzIB5cjF_8DXtoe22bj088HAkyiLxrK2RmE025FS8tlas6VFQ_7Cnqsxg3KA8dRe3ZT2sNUa6-BXU-K3mrKzdirhnXiCEF8s_e9YOQZC0HZX3SrZskx8D_thU-FRCKaSeHiXYSpKaI7qoHVZJ6o_OKEhLFANYaq14xlNd3giQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شکایت رسمی پرسپولیس از استقلال؛ پای ۳-۰ وسط است!  باشگاه پرسپولیس با استناد به الزامات سازمان لیگ، از استقلال شکایت کرده است. سرخ‌ها مدعی‌اند آسانی و اشورماتف طی دو فصل اخیر بدون پروانه کار و اقامت قانونی به میدان رفته‌اند و در صورت تأیید تخلف، باید نتایج…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/105426" target="_blank">📅 13:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105425">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a05e1941b9.mp4?token=WgAKQJAyijfYV1i2VMegVJ7ZJ56R5MoMzFBYESsqvlkxUw34SKMj6iTGvOWfN-ngMIMs-IibA-ue2OT1VnSldvf42wVAmvl1hITAGb3ZLzJ1fz9fvkLjE5Rsd2U1ipgrraLxlaHPhKy7K2tPDxsWMoUKXHh6An3dzt7SPeKMyardST5cc7BhI-R6AAFGTxRH_zp6b5psCwwipNkqrER8zCXl8CuJQZQ9cygj4HEH_UjvjQMOAETYliKjGCfW6_Rh8T4IygQznmYzN_ag8ASuSowtKheM9Z5ii95UZfOxCB0ALAZvkIf07C73sZcEKXJMYcwwZzWun55cstHudamQPyBYT5FOOX3CY_CkCD3r101zlqFXEpotbHNTrmO3pQ0KHPeRHW77yPkoxV0xMh0juMYDNY_mDlJbugNZUr3kNAlFxCx12vjiBweo4Q3ocoXrdOVjAQHCgMK_UT_k_s9oGKMVfnnfAenX1Kla1jPzpcGPqK7FnUjUvuGODZOp_XGHzRJPjlR23mNtKMyIOMdhTiU6DgpA8yMU4k2LxEXdJGDvAVcPRGlclEa31cOq1g7pe0XOJ-IGToHYDcoIdVsq1q9l55b4SalgbskhBKxvLMuHhHGzM0MEQSAH4IfTlwAeuy9MSIH8qJ3XvOvpswAO1xHVCydVKDspcgj-ai30-O4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a05e1941b9.mp4?token=WgAKQJAyijfYV1i2VMegVJ7ZJ56R5MoMzFBYESsqvlkxUw34SKMj6iTGvOWfN-ngMIMs-IibA-ue2OT1VnSldvf42wVAmvl1hITAGb3ZLzJ1fz9fvkLjE5Rsd2U1ipgrraLxlaHPhKy7K2tPDxsWMoUKXHh6An3dzt7SPeKMyardST5cc7BhI-R6AAFGTxRH_zp6b5psCwwipNkqrER8zCXl8CuJQZQ9cygj4HEH_UjvjQMOAETYliKjGCfW6_Rh8T4IygQznmYzN_ag8ASuSowtKheM9Z5ii95UZfOxCB0ALAZvkIf07C73sZcEKXJMYcwwZzWun55cstHudamQPyBYT5FOOX3CY_CkCD3r101zlqFXEpotbHNTrmO3pQ0KHPeRHW77yPkoxV0xMh0juMYDNY_mDlJbugNZUr3kNAlFxCx12vjiBweo4Q3ocoXrdOVjAQHCgMK_UT_k_s9oGKMVfnnfAenX1Kla1jPzpcGPqK7FnUjUvuGODZOp_XGHzRJPjlR23mNtKMyIOMdhTiU6DgpA8yMU4k2LxEXdJGDvAVcPRGlclEa31cOq1g7pe0XOJ-IGToHYDcoIdVsq1q9l55b4SalgbskhBKxvLMuHhHGzM0MEQSAH4IfTlwAeuy9MSIH8qJ3XvOvpswAO1xHVCydVKDspcgj-ai30-O4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔥
🇮🇷
🇮🇷
تمامی موقعیت‌های خطرناک دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/105425" target="_blank">📅 13:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105424">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7SBbzSD0ZUGepiR-qm2A9Ny3LKVD0lEQ7r6JZwiSSkYXRhcY5_dhRP4Z5ZaDvibOWA_pDsqT635lGT_r-yN26z0cxX1iREMQhau-YNkL2R5fZa_UW2IWYZkgFdd3rysbbaTcgDEDsl-XRfrH82h7D0_BtjMXSRo1E7qagn9vYjM1CqNLGXFEmEz8VCFSInJHGBUXu631PpLjkJV6J73zOWaPGi23dFQpMvrqZFBSF7G-HTFMYJN6tUx04d2fRW3WL9deA3P9pBRogXGKNKSmao4P_0NNgh3M-Og3ftoSeUqJntWMiFBMT_zkRVOLNi5dLSlpJVr_XkndCgmcoHd5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
لحظه‌جنجالی و کمتر توجه شده از ناراحتی صالح‌حردانی از کادرفنی استقلال بابت نزدن ضربات کاشته‌های حساس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/105424" target="_blank">📅 12:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105423">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105423" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105423" target="_blank">📅 12:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105422">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkSRVir4A2f0VmWdRfQLwvHBEC29xPBZJMDq4ZmGZT4y7HJxg3bUqjZiN92bXy2GCPl3NiyHyKKuA7B2oETsDZeU6Xy-Wtxk9ArYq_AXkVzDoHBD_3LTWn70W8krSG_pl86W53FCFOMxyuUS9Oy_HtkhLr8yRUTD1Vv7rff-ikPRtzPn67jrjo5U1xKmWrdZUI08L5OrhGKON9JOd7xCPJ-_j6vxUCvJkLjFofQDG2KQmBHQeZfkysB1YRjhiR8bA2Ony0nEWw8TGLOxCHxQp_dEBsDcigIMzN70JN93opRuhci2dhvsmwXzKJAyzLb04ZD4U7292v_F1M0GU9G2FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/105422" target="_blank">📅 12:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105421">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/857b23b6b5.mp4?token=ucLbjrfakyh0uY1xSScOdhv77jN-PmcIjYqdkrVQzp9FkHti2NAYqbfNRAxvR996Gi9yzCL2l-7HBb8q6krMajWbfJpiH9xHPKZm2qbTfC20hbHOUbaLSzslq4thbao93rauOKEeGQpXvKb5Kaltboe8UKw5GL7Gm5axOsJEvXlIiE7B2ZjAv0PAlutjPDJfxOApHFKVRafTqfaOaNNXqHGXoSXRL81OpFbASbDkaV4A9YT8Kw7OJj-_SEqEu40aUtlB83HGmKRCUeymEGVOZQTJDu_y1AjeY0obCmRg648YbZMD16_3gZ3-zULhRTXUvoh8cG4Hfma8df9hm-4w-wSd3RxUMFLGVekh4_vMi66865_fq8NN9kyn0wH7DJ4UTLAklIB9U1FhA3WJVeZ-lV43XBBxYHiGEiDNz9s87-o35G4P_GvcYonmsKnw-cv_4mIuFiPcgMz7OuKBUYe5k5S2xMsTB7GbjdnzaMQVBxxuYr2HWL589GkLkCqL1Z-hsUA5Nc0fFTYYb18G_MgeVPK0UDhdLnU6eToUAMfD7SYd1-8uzSwPl6mQwDs9OZkn1yDeSCbhgCY7PcFhnhFJNzBmniOYuF6lRTRg6pFywSoxKO5--V1hm_uvJsEQ4JR6F6aO4rURd0D8dRFYPny9LkjsQ6rOSBw6fFFDUv-zXVs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/857b23b6b5.mp4?token=ucLbjrfakyh0uY1xSScOdhv77jN-PmcIjYqdkrVQzp9FkHti2NAYqbfNRAxvR996Gi9yzCL2l-7HBb8q6krMajWbfJpiH9xHPKZm2qbTfC20hbHOUbaLSzslq4thbao93rauOKEeGQpXvKb5Kaltboe8UKw5GL7Gm5axOsJEvXlIiE7B2ZjAv0PAlutjPDJfxOApHFKVRafTqfaOaNNXqHGXoSXRL81OpFbASbDkaV4A9YT8Kw7OJj-_SEqEu40aUtlB83HGmKRCUeymEGVOZQTJDu_y1AjeY0obCmRg648YbZMD16_3gZ3-zULhRTXUvoh8cG4Hfma8df9hm-4w-wSd3RxUMFLGVekh4_vMi66865_fq8NN9kyn0wH7DJ4UTLAklIB9U1FhA3WJVeZ-lV43XBBxYHiGEiDNz9s87-o35G4P_GvcYonmsKnw-cv_4mIuFiPcgMz7OuKBUYe5k5S2xMsTB7GbjdnzaMQVBxxuYr2HWL589GkLkCqL1Z-hsUA5Nc0fFTYYb18G_MgeVPK0UDhdLnU6eToUAMfD7SYd1-8uzSwPl6mQwDs9OZkn1yDeSCbhgCY7PcFhnhFJNzBmniOYuF6lRTRg6pFywSoxKO5--V1hm_uvJsEQ4JR6F6aO4rURd0D8dRFYPny9LkjsQ6rOSBw6fFFDUv-zXVs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
افشاگری همسر رشید‌مظاهری از شرایط این گلر شریف سابق استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/105421" target="_blank">📅 12:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105420">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZE3hjDUnx6_dvZdVyaMLJm3X0eKodqmAMxEs5b2WuAD6wiJt2vCgzesJULWlGiuW4mQ3AF_hPPfOO8N0C8S2HHp--CvzsTNbAsN8t-FWzcSgDBKbN7mWiJjJ-ydQj37iCQVocQDa5hoUgMGJbE97NOFYdX_se3eQu70Ksn4UdBPUwIR3P3XGX1UBzu64OTdKrq0M59cAXLNqgq00rJ9mwpjjLYrQC9X67BUO7adgg5v_K5otc-NYXXIW8gzwQzUI54wxwaOHDNJUuB_T6LZ8MIprurQYP9bMKs62CCtoN7iUt80bopEiJkhJAWAeIqJQO0R1SkAqQx2-0RkWw2ZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
✅
🇮🇷
پست اینستاگرامی مهدی تارتار سرمربی تیم فوتبال پرسپولیس پس از داربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/105420" target="_blank">📅 12:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105419">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSQm6bEzzlVu1CNEzBZ84pQqbaeG8ScyUGTj4XdCB0JPd7z-A_iGveDb2nKSxWThXGPu9IpxIU1LztfXvRHe9zAAqnZ4kdtMQ7Sj_ZgbvZts1v0FDnABAnnspR1bKRUjwSCXIcQfgE5gZHYj_z3Y4WM5sIBEblB1fBIlUlINN2ivRGltLF1LAR8JhzzSsegtrz78zjnwlCOH3qscp2rWv4FpI6JMf7SzBcWyFv-8FYErlmduGHQH0auGlisovviSvCAqiZ3lsMQZEUfTAtm-TRBXQHeWcOr3lSj-EbQPWWHdqpP2ldQWy0P3nkQXTMx2QXvHmTXA92eEkx83qFhwIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
اعتراض تند مدیررسانه‌ای باشگاه استقلال به عدم اخراج حسین‌کنعانی‌زادگان در دو صحنه
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105419" target="_blank">📅 12:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105418">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
📹
🇮🇷
🇮🇷
نظر مارک کلاتنبرگ درباره صحنه جنجالی بازی دیشب دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105418" target="_blank">📅 12:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105417">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scd2JGwg54hskl1xxtE1a4_wzPqR7p-gM73u363POX_0dTasYLVft5ZrR_0F9Zktb1J48Uy_e23-_Qk8wg5EqRjGJbqpp5ZOMonDVg1fyhvjl0Src8OJKtVOxAM_cB8NYN-y8rJC-c-AlgJ9xuf5JwBLoGz2sUjjTMV-gylBl7ZtWTcINP1ODNXrktUSURein0abQ329HHrb-zWct2evZGoa3SDIvL1m1tFf4x2N8iHHwUsvFuM2iofEbT56lRz7n7WE6VqUlm0__KInyHP1mygQYmvrsi_eIGDBKrjvHdqNCQvZRDfEHUxqzbaVkG7GTZTBG8FkcQ6RoHIyP_fl0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇮🇷
محمود خردبین اسطوره پرسپولیس و دخترانش درحال تماشای بازی دیروز دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/105417" target="_blank">📅 11:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105416">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4fbd0e6c.mp4?token=qpLCmhD-I7eJbet44Pt2AF8Xfe9NCnZ8kT3w6w2s3Et8wQqBDDqwhJMu-k-xfBveIUIG6GyREhdyeB-Q1ASGslwgxhmXiiCMbo5axxfdem4XJ1qsXT4yZg2J5zuC6aUX69jjECkZRoRFhfxCu-5j3gnZTSmOnq6dXZIo5PoT8HdMDXg_IbhxUdX1hclGPmlkear6iAn_3LnXcmzTVYLEsAn01wDH2OoXiJG63q8crR47YtSLu3mlA76qyMjME3kI7VxRzHv443bg0okTyQktgTROpiUezOP-gscq73hJ8oHRy-69_uK1KRYsZ2uZutS1H4ucIC7yEVpZQZGoMCapSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4fbd0e6c.mp4?token=qpLCmhD-I7eJbet44Pt2AF8Xfe9NCnZ8kT3w6w2s3Et8wQqBDDqwhJMu-k-xfBveIUIG6GyREhdyeB-Q1ASGslwgxhmXiiCMbo5axxfdem4XJ1qsXT4yZg2J5zuC6aUX69jjECkZRoRFhfxCu-5j3gnZTSmOnq6dXZIo5PoT8HdMDXg_IbhxUdX1hclGPmlkear6iAn_3LnXcmzTVYLEsAn01wDH2OoXiJG63q8crR47YtSLu3mlA76qyMjME3kI7VxRzHv443bg0okTyQktgTROpiUezOP-gscq73hJ8oHRy-69_uK1KRYsZ2uZutS1H4ucIC7yEVpZQZGoMCapSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
داوود رفعتی: بنظرم داور دربی کوپال‌ناظمی بود اما چون تلویزیون رسمی پرسپولیس یک شب قبل از اعلام این داور رو معرفی کرد،‌ فدراسیون تصمیم به تغییر گرفت
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/105416" target="_blank">📅 11:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105415">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e40e7ca6dd.mp4?token=YLXoMYmUZxxQvajUubKl7eCTJFDxP0Tl7cJt24krf6m6hmeKL6Z8Yg1c09eGJxokpwbeogLZ9c7Q8NBW1GW5nUl40B7EZMhiG9hM-6c2WSs-eu7hkkeUdrGNRXeE5OiR1nweXCFdq89EXC97zVWVlbcHbz2Ib_NKQiRwm-yGG83ZaDwn1ynwg8JBjxp-eaoE2jcpZour-5AYaBH1C0ZKv2jQ2DEC7rNNWF4J3bfrD6U90bDwMUIUHzpV4cqxjmdlt0HtpNzOSf0fJq5aapv9OqYp3EZrgXSBa5og6ZxPU-7Q93Wtv8bcREQDaj29-wyHJH2I1FGSmLMy04_CxY9JTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e40e7ca6dd.mp4?token=YLXoMYmUZxxQvajUubKl7eCTJFDxP0Tl7cJt24krf6m6hmeKL6Z8Yg1c09eGJxokpwbeogLZ9c7Q8NBW1GW5nUl40B7EZMhiG9hM-6c2WSs-eu7hkkeUdrGNRXeE5OiR1nweXCFdq89EXC97zVWVlbcHbz2Ib_NKQiRwm-yGG83ZaDwn1ynwg8JBjxp-eaoE2jcpZour-5AYaBH1C0ZKv2jQ2DEC7rNNWF4J3bfrD6U90bDwMUIUHzpV4cqxjmdlt0HtpNzOSf0fJq5aapv9OqYp3EZrgXSBa5og6ZxPU-7Q93Wtv8bcREQDaj29-wyHJH2I1FGSmLMy04_CxY9JTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
هواداران اسنابروک حریف دیشب بایرن یه طرح قبل بازی زدن شبیه ترن‌هوایی که خیلی پشم ریزون و جالب بود. تیمشون هم در نهایت از جام‌حذفی کنار رفت
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/105415" target="_blank">📅 11:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105414">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da46dad11a.mp4?token=kzeugA0Bo-yC4iTYKdMVmzrGPRi0PChdItPz4RaLYX0BbFR-VS-tw9uXLHUzxnFt4AYqMTW1j8JtAg0_eiRL4CedkAWUYMoJ4HkuBdWBkeUZvMN7VWcPUH59F_nJ76wnyGu8AlAaCnkA6zOEfnYRJ7YBBtASsFpfC-NbixreH7f2E7zm9OK5NeEV5XJX6428vK11WZrE-dm8inFaePT316H-tlfLvd-mkSHo5pyBJ1w5hpb9iWG1GnBXs_bpf61rQjo2W4ru3kjBWEdNrSjncdXSXEYTGxKfv2m7M4EXxqOEVh4kgkTr1ssDDZ-zRpUmOBqIec3tMk6cTCiu9MYAZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da46dad11a.mp4?token=kzeugA0Bo-yC4iTYKdMVmzrGPRi0PChdItPz4RaLYX0BbFR-VS-tw9uXLHUzxnFt4AYqMTW1j8JtAg0_eiRL4CedkAWUYMoJ4HkuBdWBkeUZvMN7VWcPUH59F_nJ76wnyGu8AlAaCnkA6zOEfnYRJ7YBBtASsFpfC-NbixreH7f2E7zm9OK5NeEV5XJX6428vK11WZrE-dm8inFaePT316H-tlfLvd-mkSHo5pyBJ1w5hpb9iWG1GnBXs_bpf61rQjo2W4ru3kjBWEdNrSjncdXSXEYTGxKfv2m7M4EXxqOEVh4kgkTr1ssDDZ-zRpUmOBqIec3tMk6cTCiu9MYAZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
ناراحتی شدید ایگور سرگیف از تارتار بابت  تعویض شدنش در بازی مقابل استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/105414" target="_blank">📅 10:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105413">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4lvG707281t4-OPZfPY05zmZeD1E3xcgAPjiVka7M5Fsy76ld6wNRwI-OcImxonucVX8Gl3jIni0gEEijJuQs4plEdZlFOuhAKnYr6axSlSptQXy-KtJWyToQzuyBv1LXrwyMawv6UvrOXREUmDx6kX1jL4sDng9UMz1aEpu3ZjpR9MDXt_ElwIb-GYDwe5pgPUavDeuD9FsmSo2f6iQ2gZLqFWYqoazhM2NWyr_jJxsayHvXjMOpqqSiv4B5PAELyTjl4CmavNDOsi3xmHA4u43vfsdUgSAj-bF8Jj4_vVqDjiKku4Q5KLlCqlxHLUaODFhllC4NGbnYAmWcfl0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇭
✅
قرارداد کارلوس کی‌روش با تیم‌ملی غنا پس از درخشش در جام‌جهانی تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/105413" target="_blank">📅 10:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105412">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwkDQQE_tjn-r6a7nzYmGhJVE-3bQD_VzgT00ccmZHl-CH-Aogm99bTPMoAf35kqTqlGFvdX1rPUs7GTIzTFxa3pkbAMHz9L-E4bOxoCoHo5I3PjdNjKsSzl7BufJEWC7ftVn1OcQBmAuEpUm6DKbFg3TMNEE_RKuTLB9UVckZ6k92v66obakcfBqFAF4v_EtEV_4wjO-9SBP0DTLU3gXXsBcNnRNO-THZR-aJ84tzPAowe-wCln7zhKffrLzCY_wV2-_nBBDK_UKF0u9ifYQI287pdvhFu_Jtk4JyGO9mJATas24aDGV2a7ULMj9JX5yLVeFdKwntdFlAbhLtl6kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📱
استوری کنعانی‌زادگان کاپیتان پرسپولیس از صحنه مشکوک دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/105412" target="_blank">📅 10:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105411">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4193fef239.mp4?token=cVm7Fz_XrI6t162JghhTwfNWW3ekOVWoy42n8wq0PI5jsgQbFQJTJXuf32OBYDrMVDlVaPTcolxg0Aw08whoW-Xmq6ZArApozOq4T26Mepl54yrEBGjo16fm6WqZQNbXJtqF51MYJL5XVr1s2iMs31MIXq-wkAIR93YmtxkqAtwXjlfB1vLjYUg1sT5IHxBSjtoxSAiuQaIHv9iKI_T44mZgqqoP1s2z4b7qNxCRP7t8FUafcmYsvof4ECVQyFGtMTCe_7g5gLfKn4ImlVW2n1Zf9o__ThtFQDIsZrP4xlpPD6FpeKlcib-bCBkX3JrLFw0aRr2zVksn1ioQG3NK1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4193fef239.mp4?token=cVm7Fz_XrI6t162JghhTwfNWW3ekOVWoy42n8wq0PI5jsgQbFQJTJXuf32OBYDrMVDlVaPTcolxg0Aw08whoW-Xmq6ZArApozOq4T26Mepl54yrEBGjo16fm6WqZQNbXJtqF51MYJL5XVr1s2iMs31MIXq-wkAIR93YmtxkqAtwXjlfB1vLjYUg1sT5IHxBSjtoxSAiuQaIHv9iKI_T44mZgqqoP1s2z4b7qNxCRP7t8FUafcmYsvof4ECVQyFGtMTCe_7g5gLfKn4ImlVW2n1Zf9o__ThtFQDIsZrP4xlpPD6FpeKlcib-bCBkX3JrLFw0aRr2zVksn1ioQG3NK1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
لحظه‌جنجالی و کمتر توجه شده از ناراحتی صالح‌حردانی از کادرفنی استقلال بابت نزدن ضربات کاشته‌های حساس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/105411" target="_blank">📅 09:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105410">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e92a23e71a.mp4?token=VzUrtpHiifboseSWtEmC5yI7zGVBq0hToZvi_0MciMKWAsQ9OxCuJY7y2xN6dN2qBZpdRq4hbHjexKUsEsTi64pMJv7O-I-5HJm5cgV30aJ8M0meA0AKScHkXunDJu4iLbzIctpeVwgu2sgcwuQZyQkPxIOg9VM3OeHbvbDZn7CLY_QA4VUKDegkMYFmXOxaMS9su9tMz3wuTYIdgF3CycjeiGnt1wa4DyBQCuYKa9KK58Qh2YHGR8WU7Iyd7xusOeSgue89WhN7tFtl0A7llJyKDW_HpVpIg9j9Qin4ZvG-DESYInYn4fqo36pA68HLPt8UCrpLi_WHDNcCQOmDTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e92a23e71a.mp4?token=VzUrtpHiifboseSWtEmC5yI7zGVBq0hToZvi_0MciMKWAsQ9OxCuJY7y2xN6dN2qBZpdRq4hbHjexKUsEsTi64pMJv7O-I-5HJm5cgV30aJ8M0meA0AKScHkXunDJu4iLbzIctpeVwgu2sgcwuQZyQkPxIOg9VM3OeHbvbDZn7CLY_QA4VUKDegkMYFmXOxaMS9su9tMz3wuTYIdgF3CycjeiGnt1wa4DyBQCuYKa9KK58Qh2YHGR8WU7Iyd7xusOeSgue89WhN7tFtl0A7llJyKDW_HpVpIg9j9Qin4ZvG-DESYInYn4fqo36pA68HLPt8UCrpLi_WHDNcCQOmDTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
🇮🇷
🇮🇷
توصیف‌‌جالب عادل فردوسی‌پور از دربی جذاب و تماشایی پس از سال‌ها!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/105410" target="_blank">📅 09:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105409">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff9c433cb.mp4?token=UpqaGblbTTcw9e2Ox5byf9Dji_2iZ_Z6QPSSwWzu1N4KF02U2n2aPvnNMQ8j8JHMZ9Uivgqms1d0fv8jNw2yZtLWSaybZ52TOIlQlzwcyL03aJnPhvPbpM-sbUGmI1TmitEy9IBacwKokR3AVTUOkjGmJHgt7EDjDudMy_d-GCRaFLV3D6xQXNtgLdSnW7MJvtWTHARXzzY3Nb5b4YcrbmoqQkheMa-UTcBMIuRYvycKXnmEkHx28bEPepIRJ7lB63Srwclt8CXp_g8xC_cJn07Lra4UkXfYp6V2u61OvaYX8kMYybtgKBP62N0AUucjfaHb2simHvnusvGgKeeYvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff9c433cb.mp4?token=UpqaGblbTTcw9e2Ox5byf9Dji_2iZ_Z6QPSSwWzu1N4KF02U2n2aPvnNMQ8j8JHMZ9Uivgqms1d0fv8jNw2yZtLWSaybZ52TOIlQlzwcyL03aJnPhvPbpM-sbUGmI1TmitEy9IBacwKokR3AVTUOkjGmJHgt7EDjDudMy_d-GCRaFLV3D6xQXNtgLdSnW7MJvtWTHARXzzY3Nb5b4YcrbmoqQkheMa-UTcBMIuRYvycKXnmEkHx28bEPepIRJ7lB63Srwclt8CXp_g8xC_cJn07Lra4UkXfYp6V2u61OvaYX8kMYybtgKBP62N0AUucjfaHb2simHvnusvGgKeeYvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📹
🇮🇷
🇮🇷
نظر مارک کلاتنبرگ درباره صحنه جنجالی بازی دیشب دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/105409" target="_blank">📅 09:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105408">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/603e84d100.mp4?token=Bh7s5uUVQjlPncIcI7cB_6HfP2PdQwD2nKhtArc792Wz_C0AbiKf06tM38LcuZb6g3dDFzvgM0s-t6kzcroiF1aA2pimHIKb2ppn8VVv2vFrdH8vkxRVbgv9knO4bQMh30ddx5ojiRVv1aFR-gzrXNm2eF0NvDB2UKdWu-GoPuoFZuHV9sjqMs2VL7MgdXmcbP_PB-j2SYwU3XIGTGIDcH8Qz1vvqeNW1ZcUcazRqGkj1o0zsW7Pvx1wRID4tEta1mCCMf6vxvgm7w5jjT4_OLHwuBi3W3zbBuPNiQkImxleIupD7Y68lEbdJt4ZqLJtQe-6aDfiBlERkK5RAx0Drg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/603e84d100.mp4?token=Bh7s5uUVQjlPncIcI7cB_6HfP2PdQwD2nKhtArc792Wz_C0AbiKf06tM38LcuZb6g3dDFzvgM0s-t6kzcroiF1aA2pimHIKb2ppn8VVv2vFrdH8vkxRVbgv9knO4bQMh30ddx5ojiRVv1aFR-gzrXNm2eF0NvDB2UKdWu-GoPuoFZuHV9sjqMs2VL7MgdXmcbP_PB-j2SYwU3XIGTGIDcH8Qz1vvqeNW1ZcUcazRqGkj1o0zsW7Pvx1wRID4tEta1mCCMf6vxvgm7w5jjT4_OLHwuBi3W3zbBuPNiQkImxleIupD7Y68lEbdJt4ZqLJtQe-6aDfiBlERkK5RAx0Drg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
👍
وریا غفوری: یاسر‌آسانی جدا از فوتبال خوبش یک انسان شریف هست و در ایام حضورش در ایران برای یک فرد کم‌بضاعت خونه خریده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/105408" target="_blank">📅 08:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105404">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d578329cd4.mp4?token=cg1v1GMbUvtiDW-E5p9gum0Z0gaPjqN0Tzk6b3PAZZMRchzALcvSJP-smHJrlW9O5rfY5LORgfDvrJeD0aqBDswHWKIwtPhx7z5P75M-fdec_biXd6xry-Fa7FmDwDu1Q7sh_v2AlQysvMkqb3MRzRnbFItbMyJQ_z0bL5LIrhCb-qICLDmv7WefepljouVhGOg6d4qKvimIV4OKedWb6_hkz6oNaghngxW8i2gvINw694ku665EXd0YOWCPI3XMbQn52dvRgCa5x-HHOz7ghMrubLNuLPejfbBtgoAPJ9uIincb_gzwplR2US0U_ivwUJjtqy0uBP3Ru_qS7CtBJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d578329cd4.mp4?token=cg1v1GMbUvtiDW-E5p9gum0Z0gaPjqN0Tzk6b3PAZZMRchzALcvSJP-smHJrlW9O5rfY5LORgfDvrJeD0aqBDswHWKIwtPhx7z5P75M-fdec_biXd6xry-Fa7FmDwDu1Q7sh_v2AlQysvMkqb3MRzRnbFItbMyJQ_z0bL5LIrhCb-qICLDmv7WefepljouVhGOg6d4qKvimIV4OKedWb6_hkz6oNaghngxW8i2gvINw694ku665EXd0YOWCPI3XMbQn52dvRgCa5x-HHOz7ghMrubLNuLPejfbBtgoAPJ9uIincb_gzwplR2US0U_ivwUJjtqy0uBP3Ru_qS7CtBJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
‼️
ویدیو لحظه حمله حسین کنعانی و چنگ زدن به عارف‌آقاسی مدافع استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/105404" target="_blank">📅 00:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105403">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pvl2WsACVE7IdiYz_s56wjj6z_jmty4OsUg3XvcRp1Gt_FHZEyGMcs-h5kRJbngXs4sCELYptHeCmURZJIjvSV8bld6-u_HIpZselM4_vGESW80yB4Mrh-I2b4U2Rxm235uso6L4L7g27wQTsCu_tk3uFw_IL6wXd226hGBYJX1XPYL9gQX5n6YhJe_8X5_imG4LgSNfOQxqN0wEkfYhR6myBVr4mcUFBHzPSK48VYmT3NW16J0HDcdSL3OJZ3NKyXRwVDwgE_1H5n4xrMWvLVngB0z08RDbJBZVZbv3EXfBY3Z8pEF5OaLZpvaO3LuTmkpv9hVe30MDZpH7SrSgZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👍
فدراسیون فوتبال آرژانتین برنامه‌ریزی کرده که همه بازی‌های هفته آینده مسابقات مردان و زنان توی دقیقه ۱۰ برای یک دقیقه متوقف بشه تا تماشاچی‌ها و بازیکنا لیونل مسی رو تشویق کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/105403" target="_blank">📅 00:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105402">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e447de2235.mp4?token=HF4lQOb4rbiI0P4HmPnU5TVGTmS23o-ANq39DDWucKm9DlMUfxO8f21XmqxaD2R7TIazTG70xeY1_WYdu4DhSjzH9qmQr7F0OgjlfFp11pLGOlvB49xzgWGxzGRZlzcCxdnLrxkUwNSgYAh_UCz8VqCHtJyUNWgO5iUMYo_xMS6GCvaN9Tz_C-GKW4WAs19HIRtsWeYMaptgXB5bDhvG3fS9d0w77ATWaqQMlKpWyRRXrme3Z10b0Db4ZRHZJzaLR_aA65slYn07dGF9fDN2aUd4Bfe8Tsexgyc1Qw0NVlaD4xk0VQS_hFYXcowj0juM_oKAZcbl9LK3kcJjXEYnMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e447de2235.mp4?token=HF4lQOb4rbiI0P4HmPnU5TVGTmS23o-ANq39DDWucKm9DlMUfxO8f21XmqxaD2R7TIazTG70xeY1_WYdu4DhSjzH9qmQr7F0OgjlfFp11pLGOlvB49xzgWGxzGRZlzcCxdnLrxkUwNSgYAh_UCz8VqCHtJyUNWgO5iUMYo_xMS6GCvaN9Tz_C-GKW4WAs19HIRtsWeYMaptgXB5bDhvG3fS9d0w77ATWaqQMlKpWyRRXrme3Z10b0Db4ZRHZJzaLR_aA65slYn07dGF9fDN2aUd4Bfe8Tsexgyc1Qw0NVlaD4xk0VQS_hFYXcowj0juM_oKAZcbl9LK3kcJjXEYnMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚠️
🇮🇷
تارتار: ارونوف؟ هیچکس از پرسپولیس بزرگتر نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/105402" target="_blank">📅 23:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105401">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
‼️
🇮🇷
❤️
کنعانی زادگان: از اول بازی استقلالی‌ها موز و سنگ به سمت ما پرتاب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/105401" target="_blank">📅 22:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105400">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c06eb0d1ff.mp4?token=gLGmi9qw_0pwqCBSW19HoSJTBraEu1tRDBqE4o14JmGC0SbJFk_h926chevYxp9xzgY8NG8nRkFW3Eei5jNp6DbZPjTbuG1Xh_SIZcc4nfd8FY82urpD8JmUDvcZUq-3ilzug6nw-eC7Gf1pQ-xEmRuJ22sjPF6QKePksKE81d0mF7L7yIUIGMhycDTHPFIzXj7bWHzsZudgc8nsNQFCBt20TuJmXovbGz6kCrCdtU9cH1XJ3rpZCpQ-BFdMqo613BzbOkATiebGO_ipLNLN3J-dmjfli88hPYraeJjDW-g_ubxJyO02MCAlOHmLddUocG6odiRvMcDeRVywiQkpqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c06eb0d1ff.mp4?token=gLGmi9qw_0pwqCBSW19HoSJTBraEu1tRDBqE4o14JmGC0SbJFk_h926chevYxp9xzgY8NG8nRkFW3Eei5jNp6DbZPjTbuG1Xh_SIZcc4nfd8FY82urpD8JmUDvcZUq-3ilzug6nw-eC7Gf1pQ-xEmRuJ22sjPF6QKePksKE81d0mF7L7yIUIGMhycDTHPFIzXj7bWHzsZudgc8nsNQFCBt20TuJmXovbGz6kCrCdtU9cH1XJ3rpZCpQ-BFdMqo613BzbOkATiebGO_ipLNLN3J-dmjfli88hPYraeJjDW-g_ubxJyO02MCAlOHmLddUocG6odiRvMcDeRVywiQkpqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
📹
مارک‌کلاتنبرگ در لایو برنامه عادل فردوسی‌پور: موعود بنیادی‌فر باید حسین کنعانی‌زادگان را اخراج می‌کرد و این تنها اشتباه فاحش داور بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/105400" target="_blank">📅 22:48 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
