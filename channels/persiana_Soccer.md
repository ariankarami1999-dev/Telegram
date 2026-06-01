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
<img src="https://cdn4.telesco.pe/file/XP37CadWaq5oiZz5omsQZVNmPh49tGQ_gUTGJyJHSObyF8dsQCUhLa28nu6ofrmoa-j1Ak03PH6KqGtrNE_uQKcLKkIrRPoZQIDiuBh4PzmmKUw0QwyD0eS7p1mYOll3ON5MQaBEDJUBwceVEs5y1gGYuwPiJ4VDNBVoUJm3drIPskwGUfGn40ApK0jCC_eyp623kkNrhMncmqPYGvRD0jJRiJL05rfw5qDtzSspZinGfO5r5QF9Z_d2oheIehR-Aw5mGbxTPGu2Ksr4Y4pRqLeiqrK0xAlsuIKQqxe5EKu5rQNKhHscJI7TVJJ_sLBQVgAIW6qoOvdimnVqPIP6Fw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 178K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 13:09:42</div>
<hr>

<div class="tg-post" id="msg-22599">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ab989954.mp4?token=FSaFU6DwOva3n9mL6zMMDeA9jaanc6BvWOlzNiz9B2M0XErSi8-nM-GcztK1IZzU-uYfYZZ-gQioTAr13O2dEzMprf6zt0KbjGxmIaBh6slrD54GjHHRieyH7x15WkLmPdh-Q6Wr6_pCSvr9S2ZnE3-Gflly2QWsPiWCvXsPztyYeVd4Qj0XSMsGbsDu3Su6zSLmJ7OLCcHaOtNqF2ZAQkJOklklxXNJJp0TYmuhfhPE5HWSlg5l8HswzVNIK2KqX3Nb7laV7oGScp2WXfBqx5wz9aQnJJls74WO-q0Xkccyf5s7im8cLMo-S84xkbaw7wTzh2ZjSYDSMyXJtoi_UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ab989954.mp4?token=FSaFU6DwOva3n9mL6zMMDeA9jaanc6BvWOlzNiz9B2M0XErSi8-nM-GcztK1IZzU-uYfYZZ-gQioTAr13O2dEzMprf6zt0KbjGxmIaBh6slrD54GjHHRieyH7x15WkLmPdh-Q6Wr6_pCSvr9S2ZnE3-Gflly2QWsPiWCvXsPztyYeVd4Qj0XSMsGbsDu3Su6zSLmJ7OLCcHaOtNqF2ZAQkJOklklxXNJJp0TYmuhfhPE5HWSlg5l8HswzVNIK2KqX3Nb7laV7oGScp2WXfBqx5wz9aQnJJls74WO-q0Xkccyf5s7im8cLMo-S84xkbaw7wTzh2ZjSYDSMyXJtoi_UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قشنگ ترین توضیح درخصوص بازی تخته و این زندگی؛ واقعا هم همینطوره. عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/persiana_Soccer/22599" target="_blank">📅 13:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22598">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSOEfCsf-kQoER68Jnx5H0a3UzOCgtsODKyBJgWGBj0BvLpVjHA5QvZ5eX01IEVAWSe5Xgruru2fLiQFFuPSGEcWquIdy7GHr10iuu0MzWelPC0wEO7KzyEc1sZa3ltPZVczXQbRnMsg-mnIMFTpfbp61omP1f1HaU8xL8kCjmsfrLHFOK85cC4N2hhUwMASY2MIL9CvNumgo8NsebOWUhDLdz53h5ingCDB6p4fZ1O3QgYRKo0jtnOi6YL2uIqsXv_dpsl9bEJBUZ19LEaUbk9XWvfuK3fHyLFit1bU-sNfOWAlSoKHmDnF-fwmn6QSBT_o84QzYebWYjzJVRbfBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|گاتزتا:سران‌باشگاه منچستر یونایتد مذاکرات‌رسمی‌خود رابرای جذب رافائل لیائو ستاره پرتغالی‌آث‌میلان‌آغاز کرده‌اند و قصد دارند این بازیکن روبعداز جام جهانی 2026 به خدمت بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/persiana_Soccer/22598" target="_blank">📅 12:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22597">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a3a620208.mp4?token=M-zzoCl35HRqU3ge_RG_RozybfnHWrRKHzn1pBJDC3IpBO0uW04MKGP3j9SflBlQTtc9FS8vIeT6KS7Mc9uOputhAo6AEbPETs6R12ydPDGERKACbpjQkLFr6GiM_zK2xuqf0ZjxUtjQnK4Sc0Hu8-hpVSYpVkLnznQNJpZEBwTkE9rYUcZyFAeX-SSPSpcpW-Ts19O7YYW1XxCVk-ZXSDUYGjn08vzu_qzONJk_W4xKiSt_rsdQo_747EZw-g_0cnBVm39wVP-7y6xA_KQxo6acbzn-ulzCoJMaBcLwOvZcDtDlAUeIlzGDdWZBaIxY8o7e_KXeOMKRZMSlKqMRIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a3a620208.mp4?token=M-zzoCl35HRqU3ge_RG_RozybfnHWrRKHzn1pBJDC3IpBO0uW04MKGP3j9SflBlQTtc9FS8vIeT6KS7Mc9uOputhAo6AEbPETs6R12ydPDGERKACbpjQkLFr6GiM_zK2xuqf0ZjxUtjQnK4Sc0Hu8-hpVSYpVkLnznQNJpZEBwTkE9rYUcZyFAeX-SSPSpcpW-Ts19O7YYW1XxCVk-ZXSDUYGjn08vzu_qzONJk_W4xKiSt_rsdQo_747EZw-g_0cnBVm39wVP-7y6xA_KQxo6acbzn-ulzCoJMaBcLwOvZcDtDlAUeIlzGDdWZBaIxY8o7e_KXeOMKRZMSlKqMRIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه وقتی‌میبینه که با خوب بازی کردن در جام‌جهانی و قهرمانی‌فرانسه به عثمان دمبله توی گرفتن دومین‌توپ‌طلا قطعی‌اش کمک میکنه
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/persiana_Soccer/22597" target="_blank">📅 12:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22596">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuevOqArDmPBRL47Irf8PkkLbtXcBwu0ppmOjHnlKWEJLAPkYiCZQZS-YxtM8LYlTsvHg9PzctCqY9oLmUSqPaRAy4TWel__uTlIABYZKpXJ9mWHQU8IjqcIGUZb3dDaUzrBZoeNDxHagskmJ3hVFOdf6ZZ_5Fl7myEUnjp87ig1X8IUq8FLil3fm08-jBIofoHZAsx1mjlEQWjRzYIw0QVW4zUDnxKi3tGMt314YvL5Cf4L2KXY3EwPNI_0-L_6ybtTlG58WQ32dnBR99fObRQ8TxSOEuaZDxuMfWRQ6P-lJaPfcPJL5ufeJAfNviAuguxb-BhwLtl5qH0cDCAgng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22596" target="_blank">📅 12:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22595">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H66DFs371PTNbNuLz1h_P3bDqZEB3cZE2wwGpCrZ_3OCSqEUzrJMQlbutnCbPZWzxQ7cpxPOi9lzu2TGnkbT6g0TZrMcE8oatLaoIGjkls0Jk2xv1hWNzsFCI8OcU0KxFkQMbqe5ipb6vu-Hv5uKWNLFO5DNrekiF6TSokuVT3H7vAOPXQEB1Sr4gG9Ijsyl1vS8qkS-NGvCLBjQZm23tMDhSvlaBlPDymIqIp-K-yIvrTP_AgDzLWDysm5MJC3MZaUUIej2OwZ_Jk94qoKoPyX3vwKQRXqoqXBVmbwJKkLhg4RHFQOKs-4kBUSGmNnKis29nDdgJFfMa4B833my4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جرارد رومرو: یوشکو گواردیول مدافع سیتی نیز همچون خولیان آلوارز در خواست جدایی از منچستر سیتی کرده. فلیک عملا با تماس هاش داره راه انتقال ستاره‌های مدنظر خود به نیوکمپ رو هموار میکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22595" target="_blank">📅 11:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22594">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3238aa793a.mp4?token=Ssb-6oMi6ZXpJfp0-7WaGMtxl6tSLgdmNpJfvpFG_JgKrn7D_Ag9yskEO93VNEaHnCck3lQ2Wk7TtGK7tanEn9JsHGRNbW06faxr0MACkMBRwL8Iu1t7AgQBYnLReyacVDiJVp87LLI7CaSEmAFVKnvOpHxVuHrGAwwDuhajoyj-8jVWUwiU6VQaB4YexgMdDKJASTb1Ko-t5mNQNyuvhQj57IrUc2aVFuxFDAOObd-RF4A9ediaixfMmuNwWUeyldqS74UduuhaPS_P8HCAH0rN1nClbz3SNbr27Ak9wnw5lVAfYXjlr3XrRq5EZ0nNFAW8His1Tl19yExhBzaksltw4CsyX4I46JCH-yv5AwZNDrskIAF4_534S_kPRgFE_u5m8C-aqKtICTxss6jbwgE24ySLYkxW39dnU5rsIdA6z4bJk1IMoBap_KmqQabYCRojh7Cry6FOEBM4wxMMAmfk6Wz7rmQ_EOnGIkOwnraFMHJ-HE_-T4YQL1mIHtz76mM9sWNciYztTPVlYh9vdB3NaBoF6vq5aEP0kdJoPGBuYhdthrIKlTWinaB2Sevut3rmryHvXxC7t1MedcR5KfYrgWBnrjAamcpn1qe2RA0th16kzxTROoyhifXZQgJMUE-AVizOkVzkgyWMs-B28gLv0n15dpPcRDzflZ0I-zk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3238aa793a.mp4?token=Ssb-6oMi6ZXpJfp0-7WaGMtxl6tSLgdmNpJfvpFG_JgKrn7D_Ag9yskEO93VNEaHnCck3lQ2Wk7TtGK7tanEn9JsHGRNbW06faxr0MACkMBRwL8Iu1t7AgQBYnLReyacVDiJVp87LLI7CaSEmAFVKnvOpHxVuHrGAwwDuhajoyj-8jVWUwiU6VQaB4YexgMdDKJASTb1Ko-t5mNQNyuvhQj57IrUc2aVFuxFDAOObd-RF4A9ediaixfMmuNwWUeyldqS74UduuhaPS_P8HCAH0rN1nClbz3SNbr27Ak9wnw5lVAfYXjlr3XrRq5EZ0nNFAW8His1Tl19yExhBzaksltw4CsyX4I46JCH-yv5AwZNDrskIAF4_534S_kPRgFE_u5m8C-aqKtICTxss6jbwgE24ySLYkxW39dnU5rsIdA6z4bJk1IMoBap_KmqQabYCRojh7Cry6FOEBM4wxMMAmfk6Wz7rmQ_EOnGIkOwnraFMHJ-HE_-T4YQL1mIHtz76mM9sWNciYztTPVlYh9vdB3NaBoF6vq5aEP0kdJoPGBuYhdthrIKlTWinaB2Sevut3rmryHvXxC7t1MedcR5KfYrgWBnrjAamcpn1qe2RA0th16kzxTROoyhifXZQgJMUE-AVizOkVzkgyWMs-B28gLv0n15dpPcRDzflZ0I-zk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قشنگ ترین توضیح درخصوص بازی تخته و این زندگی؛ واقعا هم همینطوره. عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/22594" target="_blank">📅 11:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22593">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gW3MGIlTEZQKTaH8kb5b60x8wdckerAh5lIswEfOY3qzFc1dtBnzMOh6YDZG0UORT9Wzp0tYRXOfOZ72duWnA5eKS95HqlivBYyITpntWmaGZn-psj6LVncqGtuvdTFvLFJ6bgep2YJ4kUJYVZbAzmJY0L0yNgDzUJoswYhzZ5IS_O7WEY60Q1ALnVRnm_uG6KhtxtQZuxnYi9fjoENy4xTyxEMSnbA9K6ZDSB9pnImg8yAQ7qHPTxsveC9OZ3zhKTXq4QUdNZ2oy9XSb-8CwfY4siy2_Ss497qH1EDxmLWCsQJRSwFCobBQt8mv4P1qNFfRP-p4HgPt-Xl0jAmLOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/22593" target="_blank">📅 11:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22592">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQJg94Mf16w8J8gFfetNDRBlM7N0gWKmSNHiHjScaEBJuySrpISmXQOZ1IWCp8A-FhLmRXZ42FZ2dWQ3QhhtuuL-IkbPrY7cqljgp8_jpPIpHMdoil13yICEIkdVtq6H12D1wjqkGgbyjlIaDBZIj_01aA3lbp2q1eL5lhwM78hY-HQFRgIxGtQ9kemr5YPOaeZD-MbfbSuzfQ4r_OB4cKKQfVEPNEjEsMX0r_4Nygo4yy0sfnNQ6O4ubQLOOpuSfVlzOIJ9DNmFdB0RSUlKw0sEK4YGJ1pO2oWIiwjQ-Ft5P-k4FityUlno8WPVA-2024uT-I7X0HDp71CfnckdrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌های حاضر در مرحله یک چهارم نهایی رقابت های جام حذفی؛ تراکتور تبریز نیز حدف شد!
✅
استقلال، فولاد، شمس آذر قزوین، ملوان انزلی، خیبر، پیکان، سایپا،گلگهر؛قرعه‌کشی‌این مرحله بزودی انجام میشه و بازی‌هااواخر اسفند برگزار خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/22592" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22591">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjUbbmlF5AbRNz-6hyQAFwfaIg18-iv5vmrJN4Q1pPpvAbR60xpLhvQCEP4VqpM8PrmWRpuKALoI6WlHVLCSxl_zOYO0IBaQPMX7os4T4dl0d1q9anJQRqpWq1F-S-fuIhIDpnqdkCBfQpCkEYzwWd22GGfX9W7OrdaVjIQJfQZEiuBW0mx2Z9Aib8WtyoqjJ-ZmrW8n_MMuFb0Lh99I5ZqrxZdRVv0y6jHMuMbRXfB8GDfMFMtuqpqAelpWTxNaokOiVPRcWpmwKPxpI0sph3ZuYfUIW0aqLzlsSkrmbFFIY3t2kWh9Ri8gIKo7mV4-TFlyoY3II_HB4uLGauRd-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد صلاح فوق ستاره سابق لیورپول از طریق نماینده خود به عربستانی‌ها گفته هر باشگاهی به من دستمزد سالانه میده، قرارداد 3 ساله میبنده و تیمش روبرای قهرمانی میبنده من اوکیم که به آن‌ تیم بروم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/22591" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22590">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeI_GIvRMLywwDHzx4KSbl4mMsLsGPgbK5nCv6GR_ZWAzM-hMV50s589DOul4waNkB4BXn_8GK1XhNP7-jqyaeUIiqzyrxdrtXGcLJJK_Oo1TcNO2YrSD_xcc_P6hCVzyYGZsqU_1p-bc7H99ESXfMGMa6u7l_9v9vsTjf2_mjbvbyRBbH1-uvPYsAyirf2I0MV6GhJv6VvOKqmu2ogRn4QzXiJ7gGTUFpjN89qbcD487d7Va3BdXLVwlMp3jPy5wF8gzQEBnCFeaU0r44tNKZ81QmqatUJ5bXa5C5Mq1zCaMBD1bKfW7qFwyI6UlAD6rBviFxKSU7WsErR4rb6lcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
شانستو
#رایگان
امتحان کن
⚠️
میدونستی توی
#وینرو
میتونی  رایگان شرط ببندی؟
👍
تنها کاری که باید بکنی اینه که عضو سایتش بشید و
🤩
🤩
🤩
هزارتومان جایزه بگیرید بدون نیاز به واریز
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r11
📱
@winro_io</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/persiana_Soccer/22590" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22589">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxyyEioMtDohreMhThjEhSXIZ-2c7a7pmyb9ZJXrLFHPW3xkNaYBCFTBzBXAjnjDD2bSdKafyH-moNa4MyS_BL15pnoOGRGhYAfljeSUV2uus6SYDPK9yifx1BqoUtPWb61zJ5l2oW8UFBl908gBQvNpRMYjJDQMHlb_I05lI8pFE2aM_lmYKHdiyB8ArUreCtcF7i1ykpT5ISbMGlATRQET4tfWWsTTyZQYZoRY9bSW9iTRMX6Xgdd14RicJKernS8iAa-EGtc6MfhZFaPidFV4VR1D6htTzuljzwomzaBUEQF8050re7xZ4On_PO42VYQ3xZMIsvPVvEsXlDaKcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|رسانه‌ های معتبر فرانسوی خبر از احتمال مذاکرات‌باشگاه رئال مادرید با ژائو نوس ستاره پرتغالی تیم PSG در روزهای اینده میدهند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/22589" target="_blank">📅 10:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22588">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppH_dGXXT5vbkh5zDw1FoaAcVbOki-H3WwWAYPLz8yyISH7p4Ks45a2uEqioEw3tWbizO8x6xFLAS_L1YJgZWqwjG_wLGOq6xswFqaVteBk3e12YQtCBOdw2xcSHD_RS1P9mfNlr1YSsp3hmzhGvvyzD2wPRj_t4gE9gfPEV6KSfU29neWBJ7aw1IUl72b84o7gfhj5oVdFacr7K3zHQF2lpcfCOr9qAfxzbBg97sAPsGeRtrdba-4xk3jZuI2ZfKjk6NWoLCYw4wr3PVrf0298KpZb_X1d3y0sysjMKKCzJoZ7khG2BGrwPFcD8guALCA_bzWMNxI-Qrb21vM9yfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظی فرعون مصر با هواداران لیورپول با چشمانی اشک‌ بار؛ محمد صلاح فوق ستاره مصری لیورپول بعد از انجام 442 بازی برای این‌تیم بالاخره از جمع لک لک‌ها جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/persiana_Soccer/22588" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22587">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=GStwOGlJWuBsJnccdNFmN4ndVGbXLSTIQdm-mr1KqREkTXwY0e0SbyRh-Ir8B45EnU97sWMjZk-oT9E56LbqQBWi7_bROYFFJkLI14w0iSxgEBsVr_wWKYZ3UCT1jJZCk8AT340reRLdfSvzxkKzyCw4xqwTx2ARyHVY_GKokBgz46_xL5jaEi3CZ17jtyVKudpqPkqFdRkVBXJRsy-gxkCKTju0J6PsW73PbqqfLS3IG6Ru8jbZgLs8RA4SdHPikJy2C_0bsBYwkqWgbrYgyF5dvkGd_73UUF7-x61iXuoQoKrtwJ6q9A7il6vOOqDdxFG8aTruE4czkXO6E3z1Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=GStwOGlJWuBsJnccdNFmN4ndVGbXLSTIQdm-mr1KqREkTXwY0e0SbyRh-Ir8B45EnU97sWMjZk-oT9E56LbqQBWi7_bROYFFJkLI14w0iSxgEBsVr_wWKYZ3UCT1jJZCk8AT340reRLdfSvzxkKzyCw4xqwTx2ARyHVY_GKokBgz46_xL5jaEi3CZ17jtyVKudpqPkqFdRkVBXJRsy-gxkCKTju0J6PsW73PbqqfLS3IG6Ru8jbZgLs8RA4SdHPikJy2C_0bsBYwkqWgbrYgyF5dvkGd_73UUF7-x61iXuoQoKrtwJ6q9A7il6vOOqDdxFG8aTruE4czkXO6E3z1Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تو رژه قهرمانی آرسنال بیشتر از جام لیگ برتر به باسن هینکاپیه‌پرداختن؛بن‌وایت میکروفن‌گرفته دست داره اهنگ میخونه هینکااااپیه
🍑
تو نشونمون بده
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/22587" target="_blank">📅 09:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22585">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYs0vgL6iXnJAS4uoA96lkocX_wSIWx-SBST0rMV9ys0YArIsfYWyTEvVqb8HSc-TNZCqf2cgDt6n5PHYyRoruUJ7YICxs61DJTKiNA-oQ4MBa77o_awMCuKmqPCDjHDOUr-KH-TCXfjHVtjSUvYz5fBVPWopEGSI-DLL9ot5xS-t-leFIUsdUefrZsBKZjQx3RXpxqzl-RIF9xRUUGeIywBHPIAl1Ck_fwLD0a1_S1W8H4QGGPXGVDAzycOj2OuAyYcXDOJL-sowbpoHquAchUcK4sk0C7OllyndPYin3OhhRWIxkWtGXActRBtt7S9-hFUDsNT-yKGwJxC43sikg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار‌های دیروز؛ از برد قاطع مانشافت برابر فنلاند تا برتری آمریکایی‌ها مقابل سنگال  بازی شاگردای آنجلوتی مقابل پاناما هم تا پایان نیمه‌اول با نتیجه 2-1 به سود سلسائو در جریانه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/22585" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22584">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9282b8e98b.mp4?token=rr1v9onKhKyl3GyUmeASouVQwnWu_2fo7TNOed52a4o55a3H3mUCsMVAJzVDKjas_qc07kqec7MdGHg2WZ88KvkFZuHngb52cAiuiEXycrs2bXP1ANJirx2Vp5X-gs6HNMISFMqjL3tiQRbECYKGpeexwy_7dJBzGaDQ1H-_9gmEkZKawny9TepVgsx7a8YFPuT1CIv_GRPd7gsuANeKKM8d78i0VRmTmQJx4C4d6kMDoQkG8FJ2v6JuBlmR3KvWYPOBNj55VUEI1wVpTPv6BMg_nw2uSrYLoBFMTCyyCkxuCW_B6305UD6w5azGvV-9wE6LmmQie8n3Ock0Xlov5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9282b8e98b.mp4?token=rr1v9onKhKyl3GyUmeASouVQwnWu_2fo7TNOed52a4o55a3H3mUCsMVAJzVDKjas_qc07kqec7MdGHg2WZ88KvkFZuHngb52cAiuiEXycrs2bXP1ANJirx2Vp5X-gs6HNMISFMqjL3tiQRbECYKGpeexwy_7dJBzGaDQ1H-_9gmEkZKawny9TepVgsx7a8YFPuT1CIv_GRPd7gsuANeKKM8d78i0VRmTmQJx4C4d6kMDoQkG8FJ2v6JuBlmR3KvWYPOBNj55VUEI1wVpTPv6BMg_nw2uSrYLoBFMTCyyCkxuCW_B6305UD6w5azGvV-9wE6LmmQie8n3Ock0Xlov5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یادی‌ کنیم از این ویدیو پارسال؛ میکا ریچاردز به‌مارکینیوش‌میگه‌میتونم مدالتو لمس کنم؟ هانری هم میپره وسط و میگه بخاطر اینه تاحالا بدستش نیاورده؛ مارکینیوش هم میگه منم مثل تو بودم
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/persiana_Soccer/22584" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22582">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUUp8BBKyd0Q0C2SJMPf-pXRJzPqejb20-JCU-_RPv6vAfWSgxL6YOfMv-9NnbffWCj7_i3_EjyzqzdcL-nC1fuwvezY6f-FjjqqHUuNE0Xv8pPXTYpjhezmyS_moBdBoWw1a47uav0xPys27FexDN1HH7Tahwlz5RntU5cEO2WDGi33pH5zFyIYBBRpyz05SM0xHM_0rWkan3wx874UIvCGVXYIWkaDB0A8rmFhTrKWV6dpFVmq7Zrkt5yFSAV4niNwNhVqvHpA-z7zppoebIMQlIp_F2Dh2ncwUezix4uHFwXF0GHkvRncZS3YbtjKhZpe7yzo7AdAxNLmaKc0uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از جدال یاران هالند برابر سوئد تا تقابل ازبک‌ها با میزبان جام‌جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/22582" target="_blank">📅 01:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22581">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnHxV2M5TpVPlBHtSc-6I1F4rMabV027yqVslyLkPwiKF94HLxbosjmnl4NQ7gmNa3sHIJETFG6KMj00Yt8R5HgYrW8s1TGtJqQk3J2u7zDyvxvhg1FalKWRhpcJcaglZrokV2r0lncxycRmmGjnYhuJZtJzkGqzfXBQYKgvyU23oSLUjOPASpp0GH9JTL3xdOdi-F8LIyv4JfM0ZxWB1q691GVk0HXtuN7AWVN5LwH_AdgHuYkqJIj1yXvGWzZNRpvvYYuUH0DBQxDqZYfWeb-tR4K70GW1lnky2a47VDyROkJsRj0f9B4D5YBxhEoyrwARoB0GZQTga6-nBrzdNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار‌های دیروز؛
از برد قاطع مانشافت برابر فنلاند تا برتری آمریکایی‌ها مقابل سنگال
بازی شاگردای آنجلوتی مقابل پاناما هم تا پایان نیمه‌اول با نتیجه 2-1 به سود سلسائو در جریانه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/22581" target="_blank">📅 01:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22579">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q0u8p8nB0ASwGJdnD2_OSV0qIA3DHC4d6wqcqaWWkIuiE11CGVi4kPubFVpP2OuQx0oU3SMtsCZSDq9Ks1G1NlMzbbawCzVlnh1aWM3XxD4sgmOapjMXCxxOopJA-aaF-cWIluXruytNAQM9O-2y-llRhY5Rnyu_wqKLc4-pe7gwA2OeksmkRZZssEzOW8688x2b0IE782LqYZGU8I0lqELBbbXcYD3qN27mxR2rbwGuAbVp-enUv__I_nUEjJvfS2fr6B7-CrplT84c9AOCMtQFgiCSpXW4pjSWQs3i_BNUartFG_g6owPqFsj1LrD7oJln44Gx2O0wpR6aClOywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3EzfDPluca4AOX5zqi_tFcK2OFqBmdDtyOeBBXuaFciLwxOpgA5aOijvP2Aa8CyvE3CGdz0lyTLS5GekFPUrObvaZqNmIaLuHxMVRkAgvDPRxhB8lV_wEtg_Jceb0-On_lT3XjXNDTXolMsbWc9IMRI4UWWyZsyFupdjzQKECAyKRpNSVQwM8lAQOtzP3hhRPIEsoQhsjLV0uQRJsb2wRgYj1InFyTnsllzV631CJfwW0BSWBDRV30emZMS8iuqsBDKqPQbMOGkkrbapzb10xY-6dRxoGgajsMS3n0YdjZdK168Y0scBTQp6GWEm72a0bO8LDmeL3q9GHvUeAl1sA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
مری‌راک مدل اونلی‌فنز قبل بازی فینال لیگ قهرمانان به سافونوف وعده یک «شب پرشور» به ازای هر سیو رو داد. همسر سافونوف که از این موضوع مطلع شده بود گفت: شوهرم اصلاً نمیدونه که «شب پرشور» چیه. برای اون شور و هیجان یعنی حل کردن پازل، تماشای مسابقه تلویزیونی‌وخوابیدن‌راس‌ساعت ۱۱:۳۰ شب چون صبح باید بره‌سرتمرین؛ بخاطر سبک بازی آرتتا، سافونوف در طول ۱۲۰ دقیقه سیوی نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/22579" target="_blank">📅 00:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22578">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9kH829V85T7pt2n1r8H8fPW3JQ04IfWP3pztu-yMgHjOm2f4UU7SgVYJPeeQOyVCdX74b9-9kInFeRDFeFdBBJf0U2_FHHXP02xUHPwBwm9puokT-lwmxreLavtBa6rB7hwQJPVw6AF-7mNsmsxb4kuPW0tadT8f9NcbvHzCqbZYdDlBs4pBTBUiGZaq-N_-pH-7vsLad8wGzZK7Y4qSGD-O-uK9pP3eRuRYkxXMVyU3iYLRo21TvlQpvfIOBY9TbGnQrEHtAI1ZDmRLoxp7i83i6gDuj_OLMObGoltayztrIsSY0zG3pIoMC7FQ3ZsCUKBYK8gPmVBJ8pxUtc3zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درحالیکه اخیرا رسانه‌ها خبر از مذاکرات باشگاه استقلال با محمدخلیفه گلرآلومینیوم دادند اما اعلام کردیم خلیفه‌ازتراکتور آفر دریافت کرده نه استقلال؛ حالا امشب‌هم علی تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال نیز اعلام کرده که هیییچ گونه صحبتی با او و باشگاه آلومینیوم…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/22578" target="_blank">📅 00:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22577">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/909763a6a9.mp4?token=XRRq9wJMFi44EkkBeNoAK4IaHaqBoOWzlcd-f38jiKo-F-g6RGpvHSzCzaYT3PUrWCJUofovoucI7aEYAOQho0IXX3hkv3g9Lu5cGHixnVGSX4VplOsk9bY9oxQ_tLjXYPVWmoVVjH7xjljUwi_ckd74GfxQ9H1nBMJhE_rVbM1sZrys_S7d3LCNHtYriWzP1xchjk6Xhl1vyLxaeg3dVv2M8WogAluGWBXfvNEyKeGa8H3YzXEW8Pc8fKqwg-JKeNNpFPbc6FePEAZNBuxwIyuUUdBloVvmJDSbyy8sHA9TwoIzkVZXAcxR5n5spalu_0eh7ZK9nXSeWT-YmYhmIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/909763a6a9.mp4?token=XRRq9wJMFi44EkkBeNoAK4IaHaqBoOWzlcd-f38jiKo-F-g6RGpvHSzCzaYT3PUrWCJUofovoucI7aEYAOQho0IXX3hkv3g9Lu5cGHixnVGSX4VplOsk9bY9oxQ_tLjXYPVWmoVVjH7xjljUwi_ckd74GfxQ9H1nBMJhE_rVbM1sZrys_S7d3LCNHtYriWzP1xchjk6Xhl1vyLxaeg3dVv2M8WogAluGWBXfvNEyKeGa8H3YzXEW8Pc8fKqwg-JKeNNpFPbc6FePEAZNBuxwIyuUUdBloVvmJDSbyy8sHA9TwoIzkVZXAcxR5n5spalu_0eh7ZK9nXSeWT-YmYhmIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
پاری سن ژرمن انریکه کاری کرده که دیگه تیم ها برای قرار گرفتن در بین 8 تیم برتر اونقدر تقلا نکنن؛ جالبه که از این 8 تیم 6 تیم رو امسال برده، مقابل سیتی بازی نکرده و فقط مقابل اسپورتینگ باخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22577" target="_blank">📅 00:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22576">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFcAJ2FJBydCQP-51rh1HWyF_TzA8z6pKcy258CvQZNnxaGQu_IFE5h0p2EOjQi7gp50Rddx_f3x9CfwEeMsytfJp6_NDeHPLEP2dyB-KRhJ3PxPvDMk-JNCbM72j4H6aTiuOBy0k3H_WKZfXvF8eMDWLp98tmYCJyX8-BBSJuo3Tx39ZvuKv3_Sfx9GVqZv4cwDlRuL8xX5MOPJ4H3TLSkii8Tb7TXhpPaMsGLbB0S0t2g-BG1eGe1rHS_WXffgjowTQI57XvM02DYuZkv_ldURiyWtvFlRSmN7fbluz2Ab1j3eteJ-CMboiFXPD7YpHL7hQnOtpA9uhPPBAlr2og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگر همین الان توی سایت
#وینرو
عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت‌مستقیم وسریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
🔴
این فرصت محدود رو از دست ندید:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a10
📱
@winro_io</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/22576" target="_blank">📅 00:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22575">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYpcNptPHWbLUajd2z0hIuMaAsxwh6eQ0B8h8EIS4TmEjEQENxqVIqRNYghIbhIiEFKX_6U-1cAUHRrvTL-G3Tygi_fxw4Ox_x6hJHMtRF0jlfVySCJgOHOebYo3CuljCC622HmYTvly0-J0okhrfXVcIKkh6VQxY8ne2hzXOlZdn10bBfphywawg4zu09oJz9KXGk-2OsYlEbmQvFmEWi4K0gbLNNfhRx10qw29jmKywVCpBmnFnklGfkYAOBlUtWEPm13G9DJeyBm4dX-st8FxBA8mmNeH--aaNS9O6VvTOoE9xseDy9WYCUqxsg1TYYa-y0on3Yl1YYN9CMeR0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
پاریسن‌ژرمن بعدِ قهرمانی در لیگ قهرمانان اروپا فصل ۲۰۲۵/۲۰۲۶ توانست‌درآمدی‌نزدیک‌به ۱۵۰ میلیون یورو از محل جوایز نقدی این رقابت‌ها کسب کند.
🔵
نکته‌قابل توجه اینه طی دو فصل اخیر، مجموع درآمد این باشگاه از UCL به حدود ۳۰۰ میلیون یورو رسیده؛ رقمی که بدون در…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/22575" target="_blank">📅 00:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22574">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfN16u-jI8ikx4fmYEpGA_sBC10JBP36dNQZGmsCCcM3DmYQC48dvGlScrZTVfrS32LP7_V_uf0Ix8L1ThqgXNyNhIlZoaCqpf30s-YADra9Sm6JmoCjAw07rQcJv75JXJF3Nda-ZXvP8rfAa8hdsgd8JUtXf-4unc8U-TiEp8zya9cwHzqVrYgpumxYKXJkihmTohpi6_VHpNgD2HghSIsN-n3Jz7DgcD9AsAol94LJlNJvtzzolthh1F0Hf-_wl7qKPZqwSswRFWPzqnJyq1Pg8aa2CSyxI4gSn_fz-6XOog-J_rp80jxP8sBc_LXINTQ4rbFkXoEndCPLcL-CRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس پیشنهاد مالی بسیار بالایی رو بمدت‌سه‌فصل به آریا یوسفی داده و احتمال قبول‌کردن‌این‌آفر فوق العاده از سوی این بازیکن ملی‌پوش‌بسیارزیاد است. سالانه 80 میلیارد تومان پایه دستمزد + 20 میلیارد تومان آپشن.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/22574" target="_blank">📅 23:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22573">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpwaV265nzEhpibO5EbkbrP8ifELAlGIEW7vwF5kEsje0ZPmuYNfVPeta55-5knlMGV432my9h1v132o89I9_7Eq10kglowlQ0teCj6-XLy4gro7J_J2hiRtNF5RtAcdkldRgFJSNYFkZ-ktsZY_-W7txXcYXLqnPm85LETeFzT_ufDH2om3gLKJgc0icVuKNltFsrydhuJL_e-4Miz8DmJRNbT54B3gYz7wNDaS7kvp772FkXp6zRXCMMA4WGoGnCXGOOD46cygdM3k3E4UbxSEmLPA3DfNjbF0qEp-7osw4aREXULS8f2IvmZwe0jGDrJsEPqPdQGnBhamuHxM6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22573" target="_blank">📅 23:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22572">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3f2e6ecbb.mp4?token=cmi0NFfJGkEbUHje0Yg5f6cTOSILQFXRPnMqh1KHkekUPchrpXZMq6nCqugi6JTW8oasElZ9caY3x_prR_WwGwpM752PyfeciLJqTy49_hv2hGr7Zfzzp2kjhEXTnQ0KAD_s3f157QMBf-McnNkGDH5OS3EBPtEy_emMCUoqKKN28-NpS-s7RYHR0mxIdSxOAHAj3ZYmCiGG6vb9XD9KljwCuk95367Ir7NhGOtPIrL-DWNn9_w58hZP8jUY_CdgMBh8z7-6g7MCtqctGtQFmfc-eb8JrUKeJGk1UE2UOXlHe59ZETCOFw2XjHnc7nLDkfjtus6DgDys0u5nncLLGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3f2e6ecbb.mp4?token=cmi0NFfJGkEbUHje0Yg5f6cTOSILQFXRPnMqh1KHkekUPchrpXZMq6nCqugi6JTW8oasElZ9caY3x_prR_WwGwpM752PyfeciLJqTy49_hv2hGr7Zfzzp2kjhEXTnQ0KAD_s3f157QMBf-McnNkGDH5OS3EBPtEy_emMCUoqKKN28-NpS-s7RYHR0mxIdSxOAHAj3ZYmCiGG6vb9XD9KljwCuk95367Ir7NhGOtPIrL-DWNn9_w58hZP8jUY_CdgMBh8z7-6g7MCtqctGtQFmfc-eb8JrUKeJGk1UE2UOXlHe59ZETCOFw2XjHnc7nLDkfjtus6DgDys0u5nncLLGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
یه فلش بک بزنیم به زمانی که لالیگا اسپانیا برای رئال‌ مادرید و بارسلونا درواقع یه فارمرلیگ بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22572" target="_blank">📅 23:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22571">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNpPXuLUbfZlLy7X3al3zMl6tddPAbqBJkmlAlT-2SBl-cRkcW3FlkHutIdRmZi5onslfYsw2cq7blGgrj9IP09AVRBkVRQaPJ6jQeIH6A9Tm6zvFM4n6X-P2MlUt3qAcOKTdr0Po_yO4PWRnDXIy4AJFG4oB2JX-gIVW74v0ygWRnN_0nFnD3ITSnnVLBDVONBTJ4cvfOgdRoQwogh4C4waQiJ_1a4bimWcQjih2Pfz26CBUF-PKrko2ls-iUTh6lJq3Q2Nfq5EzDIr3QaonFYKLjnm3T0RseHp3YjRwnNshHvb4u3mNy3koE36zp6VPIfgQqcHaUD_QOcNwYiwQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابراهیم کوناته‌مدافع‌فرانسوی‌لیورپول قراردادش رو با این باشگاه تمدید نکرد و رسما از جمع لک لک‌ها جدا شد. کوناته هم اکنون بازیکن آزاد بشمار می‌آید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22571" target="_blank">📅 23:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22570">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7N4yts73V3RMAzNufduT82myXUF8klB7HdzYvLY1W_eefLJBFXTcD2api5IgbDed4RVH1FybV20pUDtoQVhKfGu-sXsLwNsJdl7J6FJjjQDH50gLjzK7__KoXrlTsnu0pTYJVL3ZPGGWaa3BzKlDs_49Zid3YSX-oG-o3Y_deqU5-ROzXKCCHPnoBjGMgplaVuGFGd7RQOLRqO1iZ6KQwmNC_y-CDgHQlY3gmAcf8_YTen_CYJhoqNToxt1odOI4-K2xVVy5XnDk7tmKmEtdyCEaXfHu0ab32PlE3sErZkoRUByQIoOxon3eR0AI9qgK_jJioyBUibgIP52PfcBxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ایجنت نونو مندس مدافع‌چپ پرتعالی PSG در تلاشه که درتابستان پیش رو این بازیکن رو راهی رئال مادرید کنه. مندس اعلام کرده درصورت جدایی ازPSGتنهاحاضره راهی رئال مادرید بشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/22570" target="_blank">📅 22:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22568">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S3xToXfdCK5KFJLhFAbE09DMSuncsjdwghR5FupsOTqE4zlTZQgHEpgoMaRkCGZ1vH_1Zz76Qbl7ajBNU_E_5ixFa6l5Cf8-DS3YvoLr2V2SMbv0pTrNmaOGF3QZDmD0UqZGh9YroNsr3vEFOlBt7Icopv30QmJYTJiWyV2locnw3bjEwNpswlELCQspcxLiyoltUDgaCs-p6SPn8GF7CO1dsBy09s8ePykr94lpXChjpm0yjcyG1ZaESc33wE7qVPSLB0Zlbv6U4eAdPGm49XMS9ny1D5b9LJB_HVDSOpwVClH7c1jCoQ9jTkJ_3pRAK4W2aXoRhXy6NT49RyTGBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NTQD5MEuhdlZ8bOsEq32ANEJMglUVq1-X2cEm8-qni_ulAXi11L7ZlD5lAczsp0YrxghbLIF2yJyt1CPzDe1-QPLQ9Ztiz0-Mm1EB25e5nB2Af6FsB-YCFJLi3M5DlVmDFtVnIO-jDxSACPIC4HJgtJ1INPRHdUGzxT3iiZ4hvsfxVbk2DDvxf8AMIfN6GnkkRex9_-K4_X05dULaMxn7ldrjtcJcyz90B97PLXVnP6pLRPG_ufsHho8PurXeE9MgGcYn6l0W9n5m_oAf0nEeD2RUUibFUw9QQ-9Kf3Vk2rsSan3ncsyd3XHuoVbex-RHxj3m1soP9xvxTY-jQVsBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
فواید پیاده روی رو ببینید؛ گشاد بازی رو کنار بزارید؛ فقط یه‌ساعت پیاده روی عادی میتونه بیشتر ازاون چیزیکه فکرش رو میکنی بدنت رو تغییر بده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22568" target="_blank">📅 22:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22567">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5GfJdhAdx1W8S9HB5kKJl8HurguIs1Wil2m8PlQbvBfb0is5N4NTXolya6sThPeihSZEZmb3Cm9M33if6n7UJGdLHL5I0158VpW4K7hxT4CvhLcEkd94z9JB6y3o5LBs-uWcO2DmYkY1dxWWhP-g9CImHobimadhV-JkLu9kaegAXggjZWtlnd-M2ArxADluuy8VIXt1puOfT-LbZbJtheReGjsucteOsOvgxkRTcvKvXM_zFwUa9MiKZ4bmJuL9zgP2LDGepPeFNMZJYklMyVOi6pt0ffjPneCO-I-QY0pvNYWtgX9K5Elt6-7tq5AXsmsBKghZSHTIR3K_8MceQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|فرناندو پولو خبرنگار موندو: خولیان آلوارز بزودی‌قراردادش رو با باشگاه بارسلونا امضا خواهدکرد. ایجنت آلوارز به باشگاه‌های آرسنال و چلسی اعلام‌کرده‌است که ستاره آرژانتینی اتلتیکو مادرید با آبی اناری به توافق کامل رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22567" target="_blank">📅 22:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22566">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3mrONUUofdlMCyp365TEzLjcuEHel4UBAhsKINZYphE8hIJ2csjCoy4jyCzsT_wtT9Rua6xBdDOjInFyl9cE7hyF63w_BCtpsRAhLAUJpDX32OB9YQuI5V7LyMWJIz6FJ8EfgM6IAzUuTC02l8CIIhodS6D6u6M5gzbnSaGuDNzHOo0NMVGJDy0LBX_UiIbGO2GDCrg4knyusp17t2uXgpLmcZe2spu0saeLau0njcRNbrFJ9ybwb3-bSrcC_6_XihfPFQvfHMdtuFhZCirHrfbfQIfsm05oBoBSRfJKQ6O5ZmLQqyu39ucEfkhEFHeFsp4KVqQi_uQnMiLjrcp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 20 روز پیش پرشیانا
🎙
رئیس‌سازمان‌لیگ: به این نتیجه‌رسیدیم که امکان برگزاری ادامه رقابت های این فصل لیگ برتر مقدور نمیباشد و براساس جدول فعلی سه تیم اول رو به رقابت‌های آسیایی فصل اینده معرفی کردیم.
‼️
همچنین درصورتی که سنگ اندازی نشود بعد…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22566" target="_blank">📅 22:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22564">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkzRfdNYcxB58oqGamzCH-1IQ5tVzP2l9gClvGyoRYNp4yVeGABUseYCrDRPG5-Ptwb9xttWVnlhdM8j-YpoA6qmtJI53aQ30YBhf-QlbydJ6Vd4Ie-Uo3wYriXT76q4NzTZ_xfvI_9bqNuPtqESZM_IfKFXmZY1EQYHsoxJV_kOIQ7VMYkeXP2Ymtt9-YvZJTvIcMcRWnyyl766zx4Vfgqa_MtsF98YmJtia7dvD7Xji0JcpQ5gTOfCQL26f9nwKibkGkTMcEZMRNi8ZHx7-dNg0JBMrhaLRHhaZKnhhokxgxKHxC2itkFyLiS2s-09bO13Tc5tJp7Fbiyo5nSxiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IxpjTHT3O_tL26xv0s5UMhH11s6WshrW7xYoDgtQm9yndkTkZjkxc_p3UeFsALjQaCCV7rJtXDy9PGfvl0iKdLzsXj2Iexuh8AIIg5AveltGkd-FHfDpppUTspp7zgm2U2Do5DUnO3E213JcWkHg6csYBEp1-hH5jv8bww1pVZAbiGHluvzCTCqexZdmTgP3gFMTlU1w2D_u9C6FR0wKG7UqNRNZci-vT8ktMAJP6wcap_ei6xMYfxzGZsmqhXeNN5iAszvRq-g7L8sCi6NryegyOFGrGLfhbKkY4picLPa_WD8fkwKt3eId7P0lmN07Ea7Nzbu7MK3nnUClfqqxfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
خبرنگار معروف ترکیه‌ای:
رویایم قهرمانی پرتعال با کریس رونالدو در جام جهانی است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22564" target="_blank">📅 21:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22563">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1dc755209.mp4?token=HNi029BPcVND0Cx9H5bC0iyICut0Ut32JOB9A_GTccGXhwaZfCs9nkdytvfM8kM9ZJSilKH5J8I_8FoWDmasfXL7nEUlfDU7JA9t2NmjX4GlFtfu-O-7M8CPMgbLyQU7I0umS0_pfu_uxCygRsCV4xm0CJXr3l0CJcHeCdDDhtBsYUa4vICeEtRJB4Rq5vA7OfpfWN-X88cugor8LplbBpp6u6jdsu3Gz25TOGFUjcqXbMm-_dD-qldqd1fkI1-5drCZV5ra0YrAQwD4qpc9SuFjSS2V5AXgBMZ2QkHFudN2M_2WY3bGyzueP4AVWHsucWsI31AWab6soHEHp6asZGuO_-iK2lysfyvnLZZUsG8wkhATAfml_sZDdHoeEJAimUWitZyEaBTOFPL6jhu4ZSZSaNb_Q5d3nWE4AxrcLSXhag-xzZwEzJaLorS54wMLt1FkMg2ESXZT74RXO4H8YXY7k0FbjlzDEGPX-qOHoCnc63IIdt7UU2IzA21rh54gPd-hFPYVhtVBvqJ8-jNQfo7DL_BQdeAgTV1gk7ywX_BVvmZNiQGwcWvMcgiTgYPM6Olf7UilpgyRHQrmApLhHQ8Ka39tOYvaCRqzqSbPZADb7fgUfZg_S3nkjSXPQuVI3qVYgWO5QNSIPcGURziW6SzJChWJr967AMygMRVulnI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1dc755209.mp4?token=HNi029BPcVND0Cx9H5bC0iyICut0Ut32JOB9A_GTccGXhwaZfCs9nkdytvfM8kM9ZJSilKH5J8I_8FoWDmasfXL7nEUlfDU7JA9t2NmjX4GlFtfu-O-7M8CPMgbLyQU7I0umS0_pfu_uxCygRsCV4xm0CJXr3l0CJcHeCdDDhtBsYUa4vICeEtRJB4Rq5vA7OfpfWN-X88cugor8LplbBpp6u6jdsu3Gz25TOGFUjcqXbMm-_dD-qldqd1fkI1-5drCZV5ra0YrAQwD4qpc9SuFjSS2V5AXgBMZ2QkHFudN2M_2WY3bGyzueP4AVWHsucWsI31AWab6soHEHp6asZGuO_-iK2lysfyvnLZZUsG8wkhATAfml_sZDdHoeEJAimUWitZyEaBTOFPL6jhu4ZSZSaNb_Q5d3nWE4AxrcLSXhag-xzZwEzJaLorS54wMLt1FkMg2ESXZT74RXO4H8YXY7k0FbjlzDEGPX-qOHoCnc63IIdt7UU2IzA21rh54gPd-hFPYVhtVBvqJ8-jNQfo7DL_BQdeAgTV1gk7ywX_BVvmZNiQGwcWvMcgiTgYPM6Olf7UilpgyRHQrmApLhHQ8Ka39tOYvaCRqzqSbPZADb7fgUfZg_S3nkjSXPQuVI3qVYgWO5QNSIPcGURziW6SzJChWJr967AMygMRVulnI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفت قیچی‌ برگردون‌های برتر تاریخ رقابت های لیگ برتر انگلیس؛ عالی بودند از دست ندید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22563" target="_blank">📅 21:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22562">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZuEXiWtAiMPyPWhHsepSTfd3schnNxe6zvzAwkxskczSFO5TP7_5WkHUnOhH695-4BAJsMR9-wuRVWHILBXUNCvUjSfAXgMkwF3NZDX214rN9nbrPyMdQ_5FsCTCS0N_0a7yH7mZ67UqRv-EiP_i3yhEW_6bQsUtvHzHh7apSCK2oQ7KTw3NbwoG2ICnRasNnXF5iIdoMEK2oLAcWXOrrl2_kD2NHAle5Nvda7iv_rLLH8pCSAROosqXhvCTD9jNjM_hxjeVHB_0wW_CUn0_gZ88IyYNLorVHoIytFUdfBazJ9fx3MBQW_fwgPSZ3tBrw6c1SRTF-LVP7wbsaCDcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
#تکمیلی؛ خبرنگار موندو: داروین نونیز از طریق مدیرام الهلال آمادگی‌خود را برای پیوستن به بارسلونا اعلام کرده‌است. باشگاه الهلال اخیرا ستاره اروگوئه‌ای خود را به آبی‌اناری‌ها پیشنهاد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22562" target="_blank">📅 21:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22561">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOkJk9uEYzJlIs1dQbaHfEZej-tvKB_fpUEY-aU3rJWXlYMrAcrHEqTnzYiXCxLWH3cvbuFtyxMMLoAAI3N5sUfWzloF2M1a0s3ZzPN4w6MEUxuGN74sLyCo0bUmX60V_6LlEyZQZlIxfLs6im6XKGqvNYBTLh58bVPJ9k6m007DkucSGOjt258FMRGPw6QVCiTGcln0neUEqu5txhreTo9VgPn9BedwzKzpcprGDVm-Ps9IFU8sgs93cjrs_Lpbhsq8WpiYSgpmeCJ5xD80w5S3UXvnWXIASMbWu1jAWuuVYWNscJIrIpjFZvhbqCzGTlZzeNVrY6gF5DiAZZTqpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ مدیران باشگاه پرسپولیس بامدیران‌دوتیم چادرملو اردکان و گل گهر سیرجان تماس‌گرفته‌اند تا رضایت این دو باشگاه رو برای رفتن سرخپوشان به آسیا بدست بیاورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22561" target="_blank">📅 21:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22560">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwSw8l3CoYBASAH4Vfu6-kwlAGrZilSj-uH5wfruleN2dCvIwuJNdXgWErIbH9-QYCE5oWDzoUDVm_NwUEZnheop0cNPZEwFD82J_V1pNBh0-76WXsTmtfv_oQHXPk62aWHL8lNK91SvgartT_dQjSkgGxRXzoqzeTZNghDSwMFpTt0ndj9qvnqDjPyFr5zMmGdo_zsv0h2ZQP8a3-lF_dGjsGKyTV7znIv0Hlmvl5n265O2DQclM2urJXqKL4J3Zfo1-LcHqlDvVmteg-nhfFQC7hUIquINwOpaKdoLaHHuvZGBMj5Kv_WgOnxDuwxjhXAdkH8EwpXwPxWT8EePpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی اسطوره‌داوری ایران در اعتراض به کشتار بیش از ۵۰ هزار نفر توسط نیروی سرکوب جمهوری اسلامی در جریان انقلاب ملی ایرانیان، با بازنشر یک‌ویدیونوشت: «برای بقای کثیف خودتون، جون عزیزانمونو بلعیدید. قرار ما با شما؛ نه دادگاه، نه‌بخشش. رقص و پایکوبی روی…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22560" target="_blank">📅 20:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22559">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbXCeYBXh437DePugyxYydZ7qWYfvRwG3I5nk0VWOkSR0_u7fwZQNZDPtjjtAGGJEwVAuyg07YjaNm4x9AFVWqGI0FoP_Yibm92nYqm0tThqF855b4vq6oMvYCzgulpb6F39iQPwPZJ8oT-Bp77xY0cV_UaVUCh7endzPtO3G9Pa-crMNkug037SUWV29XWsDNU54PsgpREOS1JWjAowO6JbWmZPVKp2IyGMebGZ4WppnMDIVnHUuxS0E8XNW216wvl804qCweCcueK1cgH5BTu2-joWA6AcCSBiEQrwVowtpxdaGd1l8rSwVhlDPzhI1oOejrNnr5aLbSfeDGF1tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرنوشت عجیب امباپه در UCL: سه فصل آفر رئال مادرید رو رد کرد همون سه فصل رئال قهرمان چمپیونزلیگ شد. بعدش این دو فصله که اومده رئال مادرید که PSG تیمش سابق داره پیاپی قهرمان این رقابت‌ها میشه. دمبله هم تو قهرمانی دبل کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22559" target="_blank">📅 20:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22558">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55a2c0be9f.mp4?token=d34cmd1hk-O-BOEjOTjXxYPhI6mLN29sCVT5vqbC6d750isSVHbtkfNUB_x2lmvvERgcUl7i3D0kXGR4y670Y0UC6aDFtsyl1V8Ietz6wwBwSD3WrtRBZuZYFy72_8mrpzXzdeVhYuFDHAqVMU0-SN6odCMIN-O0gWf9woAQ0SJ9TKI_piVMayYDCehDaVbMod0GPKjgEwsaaEcyu2d_uF5mELUQbAIdmFxmc1fYPIAAYUPKL6M7Zb4kVO3syU3FAQlvEAjem7VuVNrA0bhRNmqqusuGUBVcX2EGObWA-6Zg05RLpEdsoAmW_1EsyFVXf5jnaBCyXk5_HB5b51EQ6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55a2c0be9f.mp4?token=d34cmd1hk-O-BOEjOTjXxYPhI6mLN29sCVT5vqbC6d750isSVHbtkfNUB_x2lmvvERgcUl7i3D0kXGR4y670Y0UC6aDFtsyl1V8Ietz6wwBwSD3WrtRBZuZYFy72_8mrpzXzdeVhYuFDHAqVMU0-SN6odCMIN-O0gWf9woAQ0SJ9TKI_piVMayYDCehDaVbMod0GPKjgEwsaaEcyu2d_uF5mELUQbAIdmFxmc1fYPIAAYUPKL6M7Zb4kVO3syU3FAQlvEAjem7VuVNrA0bhRNmqqusuGUBVcX2EGObWA-6Zg05RLpEdsoAmW_1EsyFVXf5jnaBCyXk5_HB5b51EQ6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازهواداران‌بانو تیم‌های حاضر در رقابت های جام جهانی 2026؛ شما طرفدار کدوم تیمید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22558" target="_blank">📅 20:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22557">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJZGuWdzRkpAZgIvjN4RL4jactHnn4ljLYky75wTxZIL4zqIXz4uJiYsFz-KegJp2ZhswPUGeXTmEnCXYBS77LlI3Y3iQm0v4KWld2AdIsHVl3ThS419gS2ncMHN_DrkvL7h1nQxH2bvyohoLSJal8ncGAwXzICjXBZ3QxBBrScwMq2Ainjyh3qZc_JsGf-BFKWREGsetVUkNfFWPmJytanoCnjlGQgst-Ft7nP_YNJR-F_TS87anvQpk3ZhO4ju54RwUCm4F5pejXG-GWtKblFADT7PQn5MxsjMpg_PHS5P4zT7U9BUvfHEquceGPW6JrspdBV4MbmDDqVGAZEWDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری
؛ مسعودپزشکیان دقایقی‌قبل به دلیل تسلط کامل‌فرماندهان‌سپاه ازسمت‌خود استعفا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22557" target="_blank">📅 20:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22556">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gF6DP41XbeLiNYMtzQ6PacKfsYZ5PFiwUwpIddW136Dwz5jiOYmhpyBnFeyGV_aTPzatL8bCw9Zg5gx_ENs_Sj_Nt0PG3bnrffzPpphahF_g5yUcTDq8dkRozUstSxaOhENk0QKuG6amYKLyi29xldXsyCdBQatuqpuK9VEQNM26XKypEwncvYVFqWJkLnserbkoam1Pp8syBEZ2lUezY1dVhgtu6WpiK_yfXaXhBlHxTx60MZbTM08-xCFMxi6vgHnRAkh_1Z4F_T1BK52ajae2FPZq9RRm6qKRNswmnhx2LP_bybZpz51K2YSQY2P5FwKqUGzB-qwntcxjt5H4Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بااعلام‌کنفدراسیون فوتبال آسیا؛ مجوز حرفه ای باشگاه سپاهان برای حضور در سطح دوم رقابت های لیگ‌ قهرمانان‌ آسیا صادر نشد و فدراسیون موظفه که یک باشگاه لیگ برتری دیگر رو به AFC معرفی کند.
🔴
درصورتیکه که فدراسیون باشگاه پرسپولیس رو به AFC معرفی کند. اونوقت سرخ…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22556" target="_blank">📅 19:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22555">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjHuHFy82UmObqOkyjKT_dcRfJRZJYdq8dMqJ_DsyYWC64hkgwK-tVt_4wvBTlIEmmKT4V_jRZsNjuSCRpnMzP5_Lpc8L56317gDPYnkZugYKysUFTtrMsmIUXHY7oVQFhfCYukwN2WpmqbDsqBbdXPCPJn1vu1L3PQNsfNN8tRAW4wPWJVzkT8kKd-9R7dIc0pdEUodd9FDPYKxqcfgKbidgiTksI61AiNrU-YpdUkeeT-oNUs-wIHVyTJy6SlMdqfQkjS56-zpStfRSf_9Ezs3VvoTdJwzKDJe5CesR0D6OXmVgZJr8rRK3ISramNiR0DC3qommzYgFTgV7ReGlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|کوناته مدافع‌ فرانسوی لیورپول به‌سران این‌باشگاه اعلام کرده که پس از جام‌جهانی از جمع شاگردان اسلوت جدا میشه. از رئال‌ مادرید به عنوان مقصد احتمالی این بازیکن یاد می‌شود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22555" target="_blank">📅 19:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22553">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVC4vuzCxKS20Jz-NgVbQ1j6N2IBlf9TZvILoI6kpbqE6ZppbhoAGDTCm_U2EwCf9oZ20OaXzgZuxnjOhCCFWwnLjsHN_1N1oins6HivaD4pSOdSF0ICDT0XovdNTaFQ54sAzKPqOSZ7bH5ndcLckcTuldqY0YEVGu52Cfj_k4UukOIoLK0gwzkU0zYnB1oqwm_UZTwwoYb_FZAuWvi2Nnvhe12niJNUM5poNJRThFtfLIc-QFWmbzX5D2o4iNC1XQZJKhrHxVIyYYqUUvzmajoJMpf1R8jwa6nGC2Fq04kcNDD5EtnwkhZJrfVRSJhb7CzSSdplHrjYqUuHi-prnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|موندو:برناردو سیلوا پرتغالی تصمیم نهایی‌اش را برای‌پیوستن به بارسا گرفته و به هانسی فلیک برای‌عقدقرارداد دو ساله با آبی اناری‌ها قول داده. انتظار میره بزودی رونمایی انجام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22553" target="_blank">📅 19:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22552">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCtwGVF6iZk_e0FI1LxFTJvKIgkmssBnuDSI6GQnNiVWXS-DayzQAepsG1kC50LEPl3yhUpBkIvc00yMURyyl8rELHsUGNMI94WCe5nE-8Riqq6FLbQ3xh9OPVv_2bErEu0fIt8JreGbySkThNZojZq59um0n096-T5GWMgHGbIANDJ6SEf1oQiokB3fWmc1t7foahiavgdEiRJeN_QJmTiB_O8eoT-1QW1EIRw4iOEiLEMrV4P3nuXZno9C1wcPO3VmhUNH9pOlKtJPLn5n7E1_lixCJQa6U7LfsgvdrEu2eYI3GrfI_kZlzvCuMwDcAbZN5n-m3110e-I7Tzj_yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛مدیران‌پرسپولیس به فدراسیون فوتبال اعلام کرده اند درصورتیکه این باشگاه فصل اینده در سطح دوم‌رقابت‌های‌لیگ قهرمانان‌آسیا حضور داشته باشد موافقت خود را با قهرمانی این فصل استقلال اعلام خواهند کرد. پیش‌تر تنها باشگاهی که مخالف قهرمانی استقلال در این…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22552" target="_blank">📅 18:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22550">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/av17zHrAdgxtnYsUQhTuIp_6V1zhmwoIxqQJXUHSep5S20BNo11fNcUNevGWHmFCAaFLK8YBU-f4rc6ZnpsWIOJColw6Ur3JNloMj7ml_uXYu-XMqfsolGjgyE3Ijo64w6NTp17xH3JH4D9Mv0hqLhptOcqI_R3u-2142CC90ljH7pYZuEu7sORWkRCJ7bOhe0PAzAfk_6KJ1ECXoPbkoSDpw5yLBveVsYkyGOuzQrOIvyiAKpV1e-hrrzUCE21cB_lyzOfhLcSUJqHv1YIHxJo9XlaSHqqRmfNB0S8kP-Sz14-MFGao29U7SIM_lusk0f2hZ5NHTqWNhYuCYVYklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZYJZ3Nfvg3H5YQ1Vs7VjUTE_Q-uJa6MmG_SAPoMPQyv5VAvlM9GI_aToT6zxxJTdiLB7zRdXk4b8ugTocgObJ3CzOWr-VrhX-spoL804Eg-La2f1ypBW5DIto2RoKLVh00LX9TLI6gOieZ8SN29yuQgckfy25ckv2xXPha6vMOz1X2Hx1z4CyAuOqVUQoHZ7bMliFbq87B_GcE9lYvzqQE1SYdKU5qGIiMoDbGo9XKM7NxEPhGqrtnPE4pL1VYNpPD4Jpl1_SX7KBC7PPCwGVjfDcls57201k-4O70kaXdJ4x3nwJILyOQRRHhDOcgR_eUpDNup5C-JY71yrgsy10Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
👤
رقص‌تماشایی خوزه مورایس بعداز قهرمانی الشارجه درسوپرکاپ امارات؛ برگای بازیکنان ریخته. انصافا دانش‌سرمربیگری‌رو داره فقط تو ایران خیلی زود قضاوت‌ها شروع شد. حتی یه جام هم آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22550" target="_blank">📅 18:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22547">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6XTbt85aL-WNxwB0viXXRHxVAYGMlrjmSBqdfwZiu5kfvcIjRgIUGbKz--cyln1hxS4_Y-kXUArprt5tNDk50H66FU6wzw86AhU5SwrR6mJbXykhpj-OAiQZ8Y93Jd9EthTwWWMIGpSsG5kfnGKb8nv36vIZ7yU08bf6Q0_3DRGklo7HgG-INRmdN7TifFCcVX21kl96gKC_QhN58WIPym_jYh3OtC01Fm77HLgvWpB0vK6isPXHeVF90G0LWdDt6Uy-WvbERVsqdF6-SG5ARUcWWc1qEbvWjrFoXQ2hx2Bm2f_cl3f0CQWfpKwAdhYtHBLW6haJ9eTWr23p7R5PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛
مالکان باشگاه پرسپولیس از عملکرد مدیریت سرخپوشان در فصل گذشته‌رضایت‌کافی ندارند و ممکن است بزودی اولویت‌نهایی و آخرین فرصت‌رو به حدادی مدیرعامل فعلی‌این‌تیم بدهند و درصورت‌ادامه عملکرد ضعیفش او رو از مدیرعاملی باشگاه پرسپولیس کنار بگذارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22547" target="_blank">📅 18:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22546">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa9a136cd.mp4?token=GU1cgsWQb1qaPEBOJWyQa5lFI_-7B9eIMjxjumfJFvjXKHfjst74ionQU9GClmvDErcTPU5xh0UjT3B6dMVHQ2jPa9I2ucyNUcGUn2wsEmrNfFOgFkITD1qBn3sslZNgFPr5dmosBeGpltsLT4l4Ggo2Qi1B3aIp7HD_ws5aidV124peJAP5weTAh-ruAwydUFQro4jW4LoLKyRuK2GHeAxAYXnav1hW6JPSPcN_1_06PR7OK33M7-ql_Cgr7bGeHzaTzkRMKGGDhXjrn5y2kvZM5Zr9E8CCraP1CdK4P4Coz76_JSSaxpFlJLP1UmpBothO2j5fcbGurZbIHqqS7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa9a136cd.mp4?token=GU1cgsWQb1qaPEBOJWyQa5lFI_-7B9eIMjxjumfJFvjXKHfjst74ionQU9GClmvDErcTPU5xh0UjT3B6dMVHQ2jPa9I2ucyNUcGUn2wsEmrNfFOgFkITD1qBn3sslZNgFPr5dmosBeGpltsLT4l4Ggo2Qi1B3aIp7HD_ws5aidV124peJAP5weTAh-ruAwydUFQro4jW4LoLKyRuK2GHeAxAYXnav1hW6JPSPcN_1_06PR7OK33M7-ql_Cgr7bGeHzaTzkRMKGGDhXjrn5y2kvZM5Zr9E8CCraP1CdK4P4Coz76_JSSaxpFlJLP1UmpBothO2j5fcbGurZbIHqqS7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
آماده‌ترین و بهترین‌خط هافبک حال حاضر در جام جهانی؛ بنظرتون پرتغال میتونی امسال قهرمان بشه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22546" target="_blank">📅 17:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22545">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lt8RxDaWbZM85ruxIzXeO-0n2CNT4EdFJdTwLsL2T4FWxVKGYikixGoQiXOVLKuLeUVenhTVmcOoayEVw5J_59Qqd-useBIti6t1Kk8VRkpPmo1qXoMpFuVH9qXfQ8bA3Ika9btqG7bDrtWrw4HueLix7mTCuvrYdjxNsT019POzcTQRiXM6uy3vCakhis97656xFjdtu9yRwPSEWBv5Q0J8BJLfWUe6LViL8izYWOhgVmr4VCuex8FFpzfLchcPyG0aGIxiXhNH1P2sqCbv4-71iAkrjQ4Ww-qpb8hS6R9xX59jmmSwiWtXC-XG26ZOdMKKpKt5iQ22lNgGZyqeEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیویی جالب از جمع‌آوری سریع و پشم‌ ریزون صحنه کنسرت فینال دیشب در کمتر از دو دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22545" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22544">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYSs65hm-hwRxImADxJMdjfddOnsAn70FK9YNDyHJrJTBpzczsxGgVrOgGsoKWFRfp3snWRXtvr1E-hBR4zthtzNLoKAwlfJ5aMbVz2FQnk5dF_XVbHjqfjkg3FZr7IriAvKBcwTUtNPKV7MixiG_J9sJhLCKLD3pyHButsevD9723UpXrYb9-zMhoR2AasGCjHo-GgzHlp4nsMaaMmrSL83mlv1PmVe0DZ_CFNPTNfEvyonH5N9Y8zDd80ZY4LNdTT4KEevpwbBQlUn4FW1Wfg9Iew9iWRMyWCXxV1y8lv6C58ULj2SKkU_-ijD1PF6PS2Bzfp0KgviOVJa2CaxcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|بارسا آمادس که ۱۳ میلیون یورو بابت فعال کردن بند فسخ قرار داد رشفورد به منچستریونایتد پرداخت‌کنه اما شیاطین سرخ مبلغ ۲۲ میلیون یورو برای فروش رشفورد میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22544" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22542">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbzNVe4O6hEkv0acOpWhA9gHmmJn4D-8s6-01iVjTM0gv1C4buqd600pRNcIia9WZ0qw75sjf11keB_4XWYELsWVW6gMnDKwIHdRA-lBjs38rne892NYDg52XU_fMgyl_wlkgYtMTmgt6QN15fffJRHLD01U3gH1eHR22zy9r0ro3dygVnUEfrX18t8fcuklvVtqwyHkt0Z--utlvuPx0zczlc4rfUVBD8TMNQ5wlfeUUz5WVAz_QwDt4FHjGgNDy0YVVxc2VrCymeQIhk26I_LfuTxdrFPDN1z7fmh-uvrHAFv_Lj8LE6xvLxyTrzyoPAQzsK3-FBmjwyhAHDvt6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22542" target="_blank">📅 17:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22541">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11672147cd.mp4?token=LTBKQXe5dE7hz57lowOU-s4Qq-E6QrvZsYA9dcPOWN-OZgyIangu14OHo-Gj_D6DOlJuTbCyiRaUptfSVn6dhW2nqAYnMiqQUwN0x_WeqIk7BtlwxUX4GJwyktJMXhXX-j9KHAg56-5tcoszaOG9RK2pTlegawZ5o2H_BTP3HTS3kQu5RVRGXlmN3ZbfMrMCtTUl_UOyLyiDvXz3h91jH_hLfeWx9G_xB-kLvbH7Ef8eM64W4D-cttnod1xgvS2MXMl6HpvQEqNmCLMhivttQCCMrwUhJSKvfXAuPA4dhVpYCqkzZAYjg8D0cGvrxCfOMZ-_K59tvQOFLS5DXBz9XabMuZlrFk7xRZ7d5BWP08LvilSy6ux2B52N7xezOzxEfs4-CpqxJJPTMrNUDfUp-cMTOnIRWX-C78x9J-hATmZVA9TUqAWJ8RTwwb84VmcEvmS1EAbVHVYsrb_Pe-9QjFQ73kH25FRJV42yS98CcK1wYJEnBvp85zTqsR9eaFOD5o4B6HqmaWLCfRXl5Yur68bTdyrzaP3wOkaTmS_jzzPTSGeTPAxnKW1ViHckHBZBPEVSgl_xTklgDrtGAyNvs64BRjprOAZQ82fdBF0ZHPbnCFlzlSoe4GKeRcU-6TpHnfR_ISOgf3TjvttwestTuV5sAVGtNNBM6uvrYx681VU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11672147cd.mp4?token=LTBKQXe5dE7hz57lowOU-s4Qq-E6QrvZsYA9dcPOWN-OZgyIangu14OHo-Gj_D6DOlJuTbCyiRaUptfSVn6dhW2nqAYnMiqQUwN0x_WeqIk7BtlwxUX4GJwyktJMXhXX-j9KHAg56-5tcoszaOG9RK2pTlegawZ5o2H_BTP3HTS3kQu5RVRGXlmN3ZbfMrMCtTUl_UOyLyiDvXz3h91jH_hLfeWx9G_xB-kLvbH7Ef8eM64W4D-cttnod1xgvS2MXMl6HpvQEqNmCLMhivttQCCMrwUhJSKvfXAuPA4dhVpYCqkzZAYjg8D0cGvrxCfOMZ-_K59tvQOFLS5DXBz9XabMuZlrFk7xRZ7d5BWP08LvilSy6ux2B52N7xezOzxEfs4-CpqxJJPTMrNUDfUp-cMTOnIRWX-C78x9J-hATmZVA9TUqAWJ8RTwwb84VmcEvmS1EAbVHVYsrb_Pe-9QjFQ73kH25FRJV42yS98CcK1wYJEnBvp85zTqsR9eaFOD5o4B6HqmaWLCfRXl5Yur68bTdyrzaP3wOkaTmS_jzzPTSGeTPAxnKW1ViHckHBZBPEVSgl_xTklgDrtGAyNvs64BRjprOAZQ82fdBF0ZHPbnCFlzlSoe4GKeRcU-6TpHnfR_ISOgf3TjvttwestTuV5sAVGtNNBM6uvrYx681VU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی جالب از جمع‌آوری سریع و پشم‌ ریزون صحنه کنسرت فینال دیشب در کمتر از دو دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22541" target="_blank">📅 17:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22540">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0b950725.mp4?token=G-z3dfhIDAI_TdzQz-uZd335oy7XDwaja8085h2x-Ki11RbqXZ4NDMYG9QuRrYTrUNDcJegxU2iMjaT4pb_LQcumZoRR9LepRgtFwFj27f3mNMBQt70QCSlN61t9JhFgSvs_VKrKqksmzNlCOMAw589igh5N5TG0EKLOcWer2zUuxrLDpcyvzS5HzRPgQ-C7YELMIAHk2p7v5KMXKSFwJvn2c5r2Z6kEQEttZEcZ4m0USsm2pC6sja12ZhoWg0MsIMX7XmwZHT9DXJK3BS3Cgji0PDnbRivv7bdyWwlDMBFOhR-2tthulAHaD1-91HZuEouc50AP9n0VAyXGwZR6vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0b950725.mp4?token=G-z3dfhIDAI_TdzQz-uZd335oy7XDwaja8085h2x-Ki11RbqXZ4NDMYG9QuRrYTrUNDcJegxU2iMjaT4pb_LQcumZoRR9LepRgtFwFj27f3mNMBQt70QCSlN61t9JhFgSvs_VKrKqksmzNlCOMAw589igh5N5TG0EKLOcWer2zUuxrLDpcyvzS5HzRPgQ-C7YELMIAHk2p7v5KMXKSFwJvn2c5r2Z6kEQEttZEcZ4m0USsm2pC6sja12ZhoWg0MsIMX7XmwZHT9DXJK3BS3Cgji0PDnbRivv7bdyWwlDMBFOhR-2tthulAHaD1-91HZuEouc50AP9n0VAyXGwZR6vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
پاریسن‌ژرمن بعدِ قهرمانی در لیگ قهرمانان اروپا فصل ۲۰۲۵/۲۰۲۶ توانست‌درآمدی‌نزدیک‌به ۱۵۰ میلیون یورو از محل جوایز نقدی این رقابت‌ها کسب کند.
🔵
نکته‌قابل توجه اینه طی دو فصل اخیر، مجموع درآمد این باشگاه از UCL به حدود ۳۰۰ میلیون یورو رسیده؛ رقمی که بدون در نظر گرفتن درآمدهای روز مسابقه و فروش بلیت محاسبه شده و صرفاً مربوط به جوایز و سهم‌های مالی یوفا است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22540" target="_blank">📅 16:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22539">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4b71efa6.mp4?token=CdKcBJR2aMM7XCnpWN4zeNOKOEu0JYR-FqvelzvBwgXZOYR0VSxcyc3BIp2GwQ5riMd_YKvl_s2bvuOXrcSfIP5VDSxqIIxmYEts31myAJ-W8I8yCNpCrzvXq9vXsEXH2KMcYl1SezzK5U3jOoGteE-KYKXCyPBbqAabjtGnpFju3ntKnYe3LrhVdESZuatCeDg95Doa0vlbVo7_oAl-NhWb9wgSBCvc054wfad_ctX3L5BWsjMAgqp9pOtfkbYul3UYs6o0-RrdxGsVNp-pEPk_rrwWV1zH4W1I-lVluJRa6L6Uh_JwuLPQHWR8wVTsbhXgDxSYs1gXCevd6rI2qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4b71efa6.mp4?token=CdKcBJR2aMM7XCnpWN4zeNOKOEu0JYR-FqvelzvBwgXZOYR0VSxcyc3BIp2GwQ5riMd_YKvl_s2bvuOXrcSfIP5VDSxqIIxmYEts31myAJ-W8I8yCNpCrzvXq9vXsEXH2KMcYl1SezzK5U3jOoGteE-KYKXCyPBbqAabjtGnpFju3ntKnYe3LrhVdESZuatCeDg95Doa0vlbVo7_oAl-NhWb9wgSBCvc054wfad_ctX3L5BWsjMAgqp9pOtfkbYul3UYs6o0-RrdxGsVNp-pEPk_rrwWV1zH4W1I-lVluJRa6L6Uh_JwuLPQHWR8wVTsbhXgDxSYs1gXCevd6rI2qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ایشون هم یه مدل اسپانیایی هستن که دیشب روقهرمانیPSGمبلغ 3 میلیون‌دلار شرط بسته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22539" target="_blank">📅 16:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22538">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇮🇹
برترین گل‌های فصل سوبوسلای در لیورپول؛ دومینیک سوبوسلای مجاری از باشگاه میلان نیز آفر رسمی دریافت کرده و احتمال این انتقال بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22538" target="_blank">📅 16:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22537">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNU3eoWvoCeOnaCdfKWF2PdSJqChKrTIQhuxKQ3Rd5LI-0b2gjIp3PdeAIXo9EUQZcENhxjjkoiKeWr7CPEJwaDwQM7XCfSyFV_HV9ctKnGOKmk0JJ_zdr0dWaTyR-zAACaF7K-8FM3DcHQytJTASbNMx4QRp1a3WWU0ckVbjpUyRN6x5HPVv2P9c74rKp5vW8kGzlFUftFuw_4aKPZywiXtaV6h_gOH7gkWR2lQQghJL0IkBi0Fp_lS7OkZbtiM3oahpHozwECGH3uNshbzZ6yWQUfUDBVyeonKW087gxEhfoaTlqNKcGj5SMDCPPzihbePzj4n5nOl393QUfwAfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
یه احتمال فوق‌العاده جذاب؛ اگه پرتغال و آرژانتین در گروه‌ های خود بعنوان صدرنشین صعود کنند و درمراحل حذف بالا بیان در یک چهارم نهایی بهم میخورند و یک جنگ تمام عیار بین یاران کریس رونالدو - لیونل مسی خواهیم‌دید. تقابلی تاریخی که شاید اخرین تقابل این دو…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22537" target="_blank">📅 15:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22536">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuZleizWRydQbAmz7D7eWLpIymfs_jN-dXGpEI_8xR26RR17ZNT4Df23Xbjy_PVAkgYKjpOoeE8bjzzAUvt1UT4OB7wSqbp-JkCggdXXPKLJZO6Mksh1KU4nDbYDm_zd83NTUK6WduF8D9i0sPN9k5qi-s6No5Us7W8qg-CVU-SSoDeEtOVSoq95ZjcuaAzc-h2XDAigfsJD-spqq3oBcDiO3tynXxzpctZ74SgcXUaGMweHils_3hMXZ4-ZtBNJIvNo3f3LO-INeEY9_Mekq9G8iXUS-_04-x1fmRlYyFPljC9ewWu3qHEgMGPSaY1ACcNVcGZ5KMVohYhlGkPb_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22536" target="_blank">📅 15:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22535">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePLzc2mMsdbNURBlQqp4e8V6lcRtIHYwnycdUUTfvaRk57maqxaDspgg5u7-y45s9xcDi7j1B_uJq2auRJvx16zN10rAd11_d5JGQWtn3bZcrl0pSZkOOSBeL2UvIKQJCqS0P6fEnO1I1kpprwhMYOIyLoT1RgMU2B8DH1gh0VqlF2lygoAMEzzSRJf0XuZzY2rCKilu04NfCCvKLSz7eL5sbEgsnrWNBys_RyWx-FlOk0CEAp6JCKluVEBFEE63XO5ZMJ9GExBxAkIj-ksyS18d73Z3tmu6Xo5CKkoACaPp9FcTA_TcmsyAMDBKu0n4JLMa-pxCp8zdSn2YHHK0Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکیپ فرانسه: باشگاه رئال مادرید مذاکرات اولیه‌خود را بانماینده مایکل اولیسه وینگر راست فرانسوی بایرن مونیخ آغاز کرده. سران رئال میخوان اولیسه رو در این تابستون جذب کنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22535" target="_blank">📅 14:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22534">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLZx_syeHkxHbFFUYPj1_masC8kF5yOlAVwGTUJQRpYc3gfgILFWxcrznAHbuCuUs9TexOi1TY7TB6AH8D_Z6RvUyI8hFnfWUPZjYgfd-xBpR8Ua-tBYCeRoMxnDvlX3qbWdwpriT2f0vLE-JSaQV3bvKest7_c9PAaWFJxEHP-5uFsQBpE0z_bVyVNEM0TIFes_QU6zD3qlQJG5EBDQrs1XYIrMY_pKW7O2D9PC7WHbvmU1FMnTvVD0K1yeih10_2-3prwEdiwM4EVoK_RhYdx39w-IsHKYNABZa35WwpxtRUnXjuoVYMIRv6u4eNBF78Ad_Wl72VPcMLjoJmFjWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22534" target="_blank">📅 14:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22533">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇫🇷
عاشقانه‌های‌بازیکنان‌باشگاه پاری‌سن‌ژرمن با زن و بچه هاشون بعد فینال شب گذشته و قهرمانی UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22533" target="_blank">📅 13:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22532">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGxwlKkdmRBjl_gt_nZH7v2ru3opijnIG6foi6lFPh1qJ1GOC5WRdHvXCtEoL-JDmmbCVyiNgIv97fbg3iJUsConEvkRugRI0Zf7twsFIfcWZWERoy16KSLzlKqyY2KWX2X0jIJyPfx1Yq77Ad2LFCKEqYTrVkuYvsBFVOLOewl75VWcWqRpK2RHSnfg0iSx_EwOPLaOxM5dM8xEveSoMzre3VuprVMV-3pU1sZn-NZs5mwulY8nl-vusDhivvvvJeeuHB7ifyFHNcJEA99EQ18ov4gwo3pjoYpMckDgiGboGI9SiNtEhzU2zjKnZf0zjgBlhY7mMiBFNw99_4y2pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرنوشت عجیب امباپه در UCL: سه فصل آفر رئال مادرید رو رد کرد همون سه فصل رئال قهرمان چمپیونزلیگ شد. بعدش این دو فصله که اومده رئال مادرید که PSG تیمش سابق داره پیاپی قهرمان این رقابت‌ها میشه. دمبله هم تو قهرمانی دبل کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22532" target="_blank">📅 13:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22531">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">▶️
تعدادی از آیکونیک‌ترین و فوق‌العاده‌ترین گل‌های والی که قبلش هم توپ رد با سینه کنترل کردن.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22531" target="_blank">📅 13:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22530">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6ESDA6rydptPVOgTTrQNVhvOTXs2pdHSIeGDjdNhEhewskH0WTkMrR3reH5TqJSg0BzYi2UEkSNKdZSO3ap5CSGipxTChyGIaVFkNoSh0t-mEKXss1zA5FT_IfhwNINWzojxn72KbiZY7Nlx1AcSYiiQ7SywnrotOvxksaaFn554qFG5rWWvZyGab-GuesgooBNgWPTYR0jMvBAD-0PrtQyA0IJDvP7AOG9RBTQyIHHHLsReaflMnbyXWL1C1i16ty4hVxwtxuU7jp383Wyv6RVWrlhTXL6_s1eGlbCczu2X2iGLzaLfrYpPXUKNRedBL3mAmkUUPjllelyI-VaTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇵🇹
#نقل‌وانتقالات|رافائل لیائو به شکل رسمی اعلام‌کرد که‌دراین‌تابستون‌رسما از میلان جدا خواهد شد. مقصد بعدی ستاره تیم ملی پرتغالی یکی از تیم های لیگ برتر انگلیسه. منچستریونایتد اولویت اوله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22530" target="_blank">📅 13:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22529">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-YxdqHODIYy1sk4CQjqRK8ihEeW2WZ_AOto4w6IZN2Zmnvr9NuEEr-7hsIUcc2I_GUGlt4AODZUyBvlKIDapWhRO-OKIiT7nQM0uwJL1D5M_PsFJ6rfwxDb0MK6050ZCO4d2_INiq72ck2AeLQ2dimZn_A2kERPzMooG-hEJvjy1t3CCznArojTwRsWTlFkm-dlTwtAwKW38Lpd_so1OuuijMNAtDPljdK0H-_f7DMdhduxASZN4F6IxVbDhN2Ck6CyOJZNXu0D6X38skjUNaf-O4p39E_bUCMLDgJGAgoOVmYpyf3TG_xIixZzWbdFA9cfi59GNRU-8O3KtU8xeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو آموزشی‌نحوه‌واردکردن‌فرکانس جدید بصورت دستی در رسیورماهواریاهست؛ شبکه‌های یاهست که بالا معرفی کردیم همشون تاپ ترین هستن که بازیارو باگزارش‌فارسی، کیفیت فوق العاده، بدون سانسور و تبلیغات‌آزاد دهنده و جلوترازصداوسیماپخش میکنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22529" target="_blank">📅 12:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22528">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8oMygDe8yjcErJmYXO0XC3u2pQoE0Wb93ctadBxrtbPg3Eh9Q1duCiCA39IL9iF_BqesWp99Y4ZYYgR2S_lM4vsTMhoc7-kV4TKePR725ybqS6aSunfOFjJHpSMejOcRfBnsxIRtFQ-awO5VtaS8_ZDhXKVvdmYR9DBykcfgKmQMvt6vB_Y-UV25pIn2YF0A3Kao7FsUvD9Xgez32sntaipMtCAhZhHb5ZaWMhkaAgal6yiXNmuhdX88cFjpLjqZmE6_Cs9o8GtHcEn-J006QHTdUcC4z6ExBibZt_j8K0BCH6PuWYVpqeXas-zbj5AdhrodcpBqNGsI6ptLGAvgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخرین‌اخبار منتشر شده؛ باشگاه بارسا طی ساعات آینده پیشنهاد برگ ریزون 135 میلیون یورو برای جذب خولیان آلوارز به اتلتیکو ارائه خواهد کرد و این بار این باشگاه با این آفر موافقت خواهد کرد و این انتقال رسما انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22528" target="_blank">📅 12:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22527">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/460d6cadb7.mp4?token=HdFvUIfZWEH4fmKoO62qX2gcN0ioQBRbYPcsPq73RKi7lXNDMv6RECth0lua9dDulVDdQ4Z-nAzXdC4HsorUkNRNObkk_gFGM_bxi9E-fKebWs_izTeuMlNbF1TR5Cbf3dwLecFMkbRPHvYsG1D4I1bVRGF9Bg0gLtYfUbzCbuvpK5PN_VMBQC9bPElf565ZXAb9xzQ-gFxmxdVbP7YbNms95Ysm3NEWUu_9zszgVHdX5Bja0Rl2ntK0eINqQ54TFqXRxd-JJUUbtVQPLLRDaqsjGwDqv9PFGhoxsvjeqXBmxxb7klhXTuE4VXqs4hana3KVpD48QsO2TVbyGewePg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/460d6cadb7.mp4?token=HdFvUIfZWEH4fmKoO62qX2gcN0ioQBRbYPcsPq73RKi7lXNDMv6RECth0lua9dDulVDdQ4Z-nAzXdC4HsorUkNRNObkk_gFGM_bxi9E-fKebWs_izTeuMlNbF1TR5Cbf3dwLecFMkbRPHvYsG1D4I1bVRGF9Bg0gLtYfUbzCbuvpK5PN_VMBQC9bPElf565ZXAb9xzQ-gFxmxdVbP7YbNms95Ysm3NEWUu_9zszgVHdX5Bja0Rl2ntK0eINqQ54TFqXRxd-JJUUbtVQPLLRDaqsjGwDqv9PFGhoxsvjeqXBmxxb7klhXTuE4VXqs4hana3KVpD48QsO2TVbyGewePg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بااعتماد به نفس کامل به کراشت گفتی بیاد ورزشگاه بازیتو ببینه که تحت تاثیر قرارش بدی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22527" target="_blank">📅 12:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22526">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmzsCe8xOp9tk7Ci2ElHArf3tLwGlI9dkyYbMTbSo4dkOGVmgRrxka1xAsthkfOdfVkGTi5icg3Y6gIm1ocxWVWbFTl8Muel5En3gjYIIfCfleDb_IEhk2KU39Wcr9So9e2HCQ5_TFz2-fc5dTfMGPfKb5uVk6yy5xGIzhRg7kaEQgsDtFLoc_bxnuLBkQI5U5iWh7VYI-v_dIcupFxwIovoogsYojPwsUFh-WK9u-lxIBBj6evRl_wb2vJ59V4vySDsJjNjhZIyOknJxFwzM0ACnXL1sMPsW29hIJqXeg5iuyjEs_so9eo9V37SxRxBFZOPkSeJb9enTJLQgRkZNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ به احتمال فراوان فصل اینده رقابت‌های لیگ برتر 18 تیمی خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22526" target="_blank">📅 12:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22525">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55166b2d48.mp4?token=JdU7Z3T0Z1zVsZ5pFygirKh-mTpka4Db7C31EmhxLa_7JqhZzorXTY4dUsYEW7eUlC_-wMSS1vM1qgqp-2Br44p4y-teugmJcIepwqxnEn7YPVP6aKURMLhIE6HknhzQ0PmfRtRm_Uf3mks4jehjYBiP-hV7wJkLtk_dTtBJScTjKdPv_-DJzy1Kw7L09LBpFgHp9Cmt8GqhzjFhvLnJfJVtK44h3O2pf-bkKMDlKt44GLdDKaH9hqwY9lYaz3_ZRytJhhQRT7hixTyJCePXNYEMTlroNSWUDwjeQgChB0J1KnrASBzna84fWkje7MS31AqXPVdsfr-EwMZx5eZvdDd1Iv_7sKoeTA8cqLjZ5O2IMWyfr9OeZpkTj0d8LSbK5KHyaxPRnCxEwly9NdWfsqvdTXWXGmLTy5iQmUH27VROj0EIT4n8ktxFSR-35-WbvqQ4iUrY4pLwcGSD2B8lO4IDUr9t7iPDVfLqEbbeOvgcS-96zfaIUfS2yobmqk1eSvjQn7f-3vyQgrHdfh-48fc0QYQAWdPMdvbszNkzoug5Q0G1jR3PCH6F3sF7MTlKAW8CS36vgGmCMg6avomHZSBbUnf1R4ebF1R83Yq3g7AVkiRcWmguWHhKfqIjUa7GSF19_sja6RgDAZS-PXuL6sHRF04IphDaNLevYLMeOL8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55166b2d48.mp4?token=JdU7Z3T0Z1zVsZ5pFygirKh-mTpka4Db7C31EmhxLa_7JqhZzorXTY4dUsYEW7eUlC_-wMSS1vM1qgqp-2Br44p4y-teugmJcIepwqxnEn7YPVP6aKURMLhIE6HknhzQ0PmfRtRm_Uf3mks4jehjYBiP-hV7wJkLtk_dTtBJScTjKdPv_-DJzy1Kw7L09LBpFgHp9Cmt8GqhzjFhvLnJfJVtK44h3O2pf-bkKMDlKt44GLdDKaH9hqwY9lYaz3_ZRytJhhQRT7hixTyJCePXNYEMTlroNSWUDwjeQgChB0J1KnrASBzna84fWkje7MS31AqXPVdsfr-EwMZx5eZvdDd1Iv_7sKoeTA8cqLjZ5O2IMWyfr9OeZpkTj0d8LSbK5KHyaxPRnCxEwly9NdWfsqvdTXWXGmLTy5iQmUH27VROj0EIT4n8ktxFSR-35-WbvqQ4iUrY4pLwcGSD2B8lO4IDUr9t7iPDVfLqEbbeOvgcS-96zfaIUfS2yobmqk1eSvjQn7f-3vyQgrHdfh-48fc0QYQAWdPMdvbszNkzoug5Q0G1jR3PCH6F3sF7MTlKAW8CS36vgGmCMg6avomHZSBbUnf1R4ebF1R83Yq3g7AVkiRcWmguWHhKfqIjUa7GSF19_sja6RgDAZS-PXuL6sHRF04IphDaNLevYLMeOL8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لحظه پنالتی آخر آرسنال و قهرمانی پاری سن ژرمن در فینال لیگ قهرمانان با گزارش جذاب فرشاد محمدی مرام که یکی‌از آرسنالی‌های دو آتیشه هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22525" target="_blank">📅 11:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22524">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91b2ba8656.mp4?token=tKUVJ2Nb_cTcgocb3fgb92MkjnyLyhE9mwD-bddHFXgEKdy-81F6t_Vbqnflb8vzT5N8JdkN6P0Ub3GSNE-KbqV0sql609ZOHu3O_WY81jyeu_6-ji__bdrbdoSILgKpliXuWn6CijukniKzIB7uiff7OUCSSGU0pfcQ1v4MVepHbzyM4qMZUPGCMTYigY0MMgOTeP0teVasMJb2NdNL1mbb2KGEWQP52XtPMKWl6_N5OWSlnCjLjod6lc1-7YfahHRf3XfTEam7TTDutQgr5qhSH-oyrqfnECvqb8qR5QVrj2Bb9xxR0xoNlSLrORTbpmVG4MrPr54_-8NQ55RZmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91b2ba8656.mp4?token=tKUVJ2Nb_cTcgocb3fgb92MkjnyLyhE9mwD-bddHFXgEKdy-81F6t_Vbqnflb8vzT5N8JdkN6P0Ub3GSNE-KbqV0sql609ZOHu3O_WY81jyeu_6-ji__bdrbdoSILgKpliXuWn6CijukniKzIB7uiff7OUCSSGU0pfcQ1v4MVepHbzyM4qMZUPGCMTYigY0MMgOTeP0teVasMJb2NdNL1mbb2KGEWQP52XtPMKWl6_N5OWSlnCjLjod6lc1-7YfahHRf3XfTEam7TTDutQgr5qhSH-oyrqfnECvqb8qR5QVrj2Bb9xxR0xoNlSLrORTbpmVG4MrPr54_-8NQ55RZmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
واکنش عجیب ایوان تونی بازیکن تیم الاهلی به قیچی برگردون کریس رونالدو ستاره النصر
😳
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22524" target="_blank">📅 11:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22523">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHuPvuQQTI9HoJ3QZvhWe8bewImWODNjPeoaCADyzqKlSD6-jkVyn78vRlM-Y3Xxrc3X5AMlgDlkKB01ADjnXvLUFYFI8pQZnqjjfPsTY2IXnD4Cgm3xOKHQssMkkwNPBdpwwel2ksDcYpjjJPwVkVD_YeKkCutNLlFCoo1AND6M80Q2tgwDyn0OBYVtIIAKT_jun1OuIaJs0BcCCJpQH3vQvl29NOMjHfIZx8vERxlnivjRtie1xHV27Hj_Ch5V_A16pB3uTmpfiNEhx5ylRfdMLmtdkAD5hjicx8fLlY9QgGIk1FjJseat31EPWFmJM3jd37v4rr9Df2veKKxzIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ مدیر برنامه های الهیار صیادمنش مهاجم24ساله سابق تیم فنرباغچه و هال‌سیتی درگفتگویی‌کوتاه بارسانه پرشیانا اعلام کرد اولویت این بازیکن برای فصل آینده حضور در فوتبال اروپاست اما اگر تصمیم‌به‌بازگشت به لیگ برتر داشته باشد اولویت او باشگاه…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22523" target="_blank">📅 10:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22522">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1346d9dda7.mp4?token=EPYzpC8qT17fSxnGwd-35Xv5q7SAnqPcD07gOvfAsAj3SJr9z3n0x7Bbm-GzrNhnaWmURZt8s2TuHGa0fllpDtNCLcP1336NL_qPI7XUWpq1FVPYKQX3ENLrN-4TEbYkjjPLFlvCJYoQ_27BPBRlK6a14E0h9z7IcEIVotJRwr581Yw4rE7l-MScZjyOHNcV3hFH3r4WQwU86Ovqgs78bd1M_7jBOrz33q0wgScDL3Pv_XXccwx-oozsrIE_GSzLlSDLSdNUgkyzA5vqCWLJ8aDUfBnyFbNh5oRBf6q4MLtzCuv2XNtMx1I33ym83y5l4QcCzufaRgpitNYOORApQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1346d9dda7.mp4?token=EPYzpC8qT17fSxnGwd-35Xv5q7SAnqPcD07gOvfAsAj3SJr9z3n0x7Bbm-GzrNhnaWmURZt8s2TuHGa0fllpDtNCLcP1336NL_qPI7XUWpq1FVPYKQX3ENLrN-4TEbYkjjPLFlvCJYoQ_27BPBRlK6a14E0h9z7IcEIVotJRwr581Yw4rE7l-MScZjyOHNcV3hFH3r4WQwU86Ovqgs78bd1M_7jBOrz33q0wgScDL3Pv_XXccwx-oozsrIE_GSzLlSDLSdNUgkyzA5vqCWLJ8aDUfBnyFbNh5oRBf6q4MLtzCuv2XNtMx1I33ym83y5l4QcCzufaRgpitNYOORApQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ژوزه مورینیو سرمربی‌ سابق چلسی:
ابراموویچ مالک چلسی به من‌گفت‌که برای مهاجم کی رو در نظر داری؟ منم بهش گفتم دیدیه دروگبا؛ گفت اون کیه؟ کجاست؟ گفتم شما فقط پول بده و حرف نزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22522" target="_blank">📅 10:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22521">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c743e5df08.mp4?token=Ukg6YSFANXP_bRh0nzWa4X64yvzC4ZLmhjKrk114wDI0343-tnSDnC56hXoF83Kubw895TGaainmKoEqh5rD0JkNVWstL839sCnQRqTKBTuwMWINY7etGmHEERe9GP3OdzI6Q35ci-kA4OEjUpOtroK0kXaJWJqSKS5YWhErNLZLwn5EWapyzzikuSvPabJsiHH98ydNfhs7tdmAWC9BfURF4Z41ZQxBetcs74iXN2P9qCX6SnKSmivul_ePIrGfPiDzeSqAUeJWLrICKlf_FD2ByuxxWYajtJlCGA_1ZyKL8SO0RB5dfGlNbCcRyiT64gdGb93eJHqyPwn8w70zNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c743e5df08.mp4?token=Ukg6YSFANXP_bRh0nzWa4X64yvzC4ZLmhjKrk114wDI0343-tnSDnC56hXoF83Kubw895TGaainmKoEqh5rD0JkNVWstL839sCnQRqTKBTuwMWINY7etGmHEERe9GP3OdzI6Q35ci-kA4OEjUpOtroK0kXaJWJqSKS5YWhErNLZLwn5EWapyzzikuSvPabJsiHH98ydNfhs7tdmAWC9BfURF4Z41ZQxBetcs74iXN2P9qCX6SnKSmivul_ePIrGfPiDzeSqAUeJWLrICKlf_FD2ByuxxWYajtJlCGA_1ZyKL8SO0RB5dfGlNbCcRyiT64gdGb93eJHqyPwn8w70zNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یجوری هم متعجب شد از اخراج شدنش که فکر کردم یه خطای ساده انجام داده!!! دِ اخه مرد حسابی زمین فوتبال رو با رینگ بوکس اشتباه گرفتی
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22521" target="_blank">📅 10:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22520">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b417aa36e.mp4?token=H2j42yU0EIw9I93sJSr_pfAL-56pgB0nyvj2Oy26wYdToiuR_1CoG4sOVBSyqVOx56d7Shrll9x733OUdeMBYSYHv2Ui6HwO408H1YyQ-PQ1gVZ9pylRSEjwDAXG9Nebkjvo3zkeftsDukNtCm_WeI6AYuj5MqsoKaJMnk5kyNLiKjqij7PPMOqKKedmxBB52BfmfZnRJhmYGUnqT0_-1laafSvtenTUck2NnIfejK140Sufkyik7NTyiAoTtVOfdJPP8t546z6ac8lVppmdp5V46tPA4Smrs7eIXR0HuHQFRgWV2ew0_S-O__s0HhXLp7uK8pTI4kGD3kFGFLe1QpEliUM0ULInqENXvIi67xyZrLO9ZoKaHcHbA94TbBtaQKW2eSrQjILrBXog-3pcme_9tz9-lNK54qdllZftkZVjuvWP96VHQV1TBx4PcGB8yWFbtxzLmyVv9hmaUksqnQCcqKmqBZLNNny-fwSwB84zUg8MeWkQXvKZzATeqOLasZIXlt8xEMcgtBc_D7008AIyZ4tunDAQCaJB5xEWkofcoMcbs68lYb1nXGzydThgDVZ3TyVGEEgFDj0W5IZdCW87xFiOJ1gUIZhv75p6CTO1rCEpltSv-NHnHxdm5hq8S73lJCtwBAVCgIedMu5OKKEn4_VApmAD-J1jZba6LY4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b417aa36e.mp4?token=H2j42yU0EIw9I93sJSr_pfAL-56pgB0nyvj2Oy26wYdToiuR_1CoG4sOVBSyqVOx56d7Shrll9x733OUdeMBYSYHv2Ui6HwO408H1YyQ-PQ1gVZ9pylRSEjwDAXG9Nebkjvo3zkeftsDukNtCm_WeI6AYuj5MqsoKaJMnk5kyNLiKjqij7PPMOqKKedmxBB52BfmfZnRJhmYGUnqT0_-1laafSvtenTUck2NnIfejK140Sufkyik7NTyiAoTtVOfdJPP8t546z6ac8lVppmdp5V46tPA4Smrs7eIXR0HuHQFRgWV2ew0_S-O__s0HhXLp7uK8pTI4kGD3kFGFLe1QpEliUM0ULInqENXvIi67xyZrLO9ZoKaHcHbA94TbBtaQKW2eSrQjILrBXog-3pcme_9tz9-lNK54qdllZftkZVjuvWP96VHQV1TBx4PcGB8yWFbtxzLmyVv9hmaUksqnQCcqKmqBZLNNny-fwSwB84zUg8MeWkQXvKZzATeqOLasZIXlt8xEMcgtBc_D7008AIyZ4tunDAQCaJB5xEWkofcoMcbs68lYb1nXGzydThgDVZ3TyVGEEgFDj0W5IZdCW87xFiOJ1gUIZhv75p6CTO1rCEpltSv-NHnHxdm5hq8S73lJCtwBAVCgIedMu5OKKEn4_VApmAD-J1jZba6LY4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کدبیس سه‌شبکه‌جذاب ماهواره‌ یاهست که بعد بالااومدن نیاز به‌واردکردن‌کدبیس دارند. اولش دکمه F1 میزنید بعدپشت‌بندش‌سه تا 3 بعدش یه صفحه میاد که باید کدبیس رو وارد کنی:  کدبیس شبکه جام جهانی HD:  BISS:2585AB552585CD77  کدبیس شبکه ورزش تاجیک HD: BISS:03A01BBE20C16D4E…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22520" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22519">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baebe6400d.mp4?token=WSNW6Efdg9hTO3oO2KmaSAaiK-GaQiQBrk18DzscF-HnHpyrjxBS5OhX5BC68-cRlX5v2DJIMrn7xtL8y8ENkk8yTbUHQXbiQDOlEiXAxDM9ukQjJy_zYoYqfQF1BzBvcti6h8YyDZM4hKTNMYC5HmA8CACheGMiy9eQbk0DjMsmDgUG93HhMomC4Lrh9G1cSHbVbfL3APvNAgK9nA9OzlmSgzWtKX1-RVfOUsf4frgiEKOEcV3obgbE0MQayIdbtiO7JOCJgsAE_XCUnyiuYzQhD3E5VBaHjIq6R4lVyg82YTY24n6xZPHWOIkCNiCFeHbhCu8mq_NQZvR9nv81eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baebe6400d.mp4?token=WSNW6Efdg9hTO3oO2KmaSAaiK-GaQiQBrk18DzscF-HnHpyrjxBS5OhX5BC68-cRlX5v2DJIMrn7xtL8y8ENkk8yTbUHQXbiQDOlEiXAxDM9ukQjJy_zYoYqfQF1BzBvcti6h8YyDZM4hKTNMYC5HmA8CACheGMiy9eQbk0DjMsmDgUG93HhMomC4Lrh9G1cSHbVbfL3APvNAgK9nA9OzlmSgzWtKX1-RVfOUsf4frgiEKOEcV3obgbE0MQayIdbtiO7JOCJgsAE_XCUnyiuYzQhD3E5VBaHjIq6R4lVyg82YTY24n6xZPHWOIkCNiCFeHbhCu8mq_NQZvR9nv81eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ویتینیا: اونا تا میتونستن وقت تلفی کردن، اما در همچین بازی‌هایی بایدصبورباشی؛
ویتینیا علاوه برکسب‌جایزه بهترین بازیکن فینال یه‌آمار فوق‌العاده هم ثبت کرد؛ هافبک پرتغالی، در فینال لیگ قهرمانان اروپا مقابل آرسنال باثبت ۱۴۱ پاس صحیح، با رکورد تاریخی ژاوی درسال ۲۰۱۱ مقابل‌منچستریونایتد برای بیشترین تعداد پاس‌صحیح دریک‌بازی فینال از زمان شروع ثبت‌دقیق‌داده‌ها درفصل ۲۰۰۳/۰۴ برابری کرد؛ او همچنین باثبت مجموع ۱,۵۸۹ پاس صحیح در این فصل‌از رقابت‌ها و تعداد پاس‌های‌بالای ۱۰۰ در ۹ بازی مختلف، به‌تنها بازیکنی در کنار ژاوی تبدیل شد که به چنین دستاورد بی‌نظیری دست یافته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22519" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22517">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLG0x_CL-uMWBtF7E3vxrhdL7kQiVygFO5JhHqPuJT14OTUnxrMUBEFMwtzKbPEFLWTbCbczSZNftCfdtqf9p6MgBPEy37DYwaFb4kVobhISvnpnrQ-RmJCZtCCSueYv0sExlw6kwCTInlkKZIZNH7TgNh62E1hNWcv7pUDitMFsAGRJYjPzzQk3Evvqya47wIPqtIG6ZXtXuEdNCkXb4WEPpaULtY5lCu8EtFmEUhHTJxANRDoQcgIYRUa5cppx1Z8nhL01nqZMjeeezmItDQ2AVxKTsCdOAlCaRiqEhg2E50TC75gXXd2hT0Cg77k1vlzCd-Uc6cOGVBh0Mzyi1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با بازگشت نیمار جونیور به تیم ملی برزیل برای جام جهانی؛ وینیسیوس جونیور شماره 10 این تیم رو به نیمار برگردوند و خودش شماره 7 پوشید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22517" target="_blank">📅 09:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22516">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucqoSfCDqwQqXiO8fv0ysRO4U-VfmPtd_NGUOkM4ZYp3y4-0zGb-o0MDp6-vHqhsgfvRZov_vHCiTRQOMVYPsZvinJ-V43qTf_KlptIoBSnbQVKmxLXw-cgXYdCKbDyUA8XYsm-N2n9Dbce_0G_wa8QbKGga8O-UJCVCc0uG34CycUJA9pztfg0Skod_heV0bTwetoamC8mVqEFh-r68Kefux6HovSXZyPYwRiJLBzBx3RwgPYrJqUCoZUatBkpbTJ3SOKR4FQf8T3inRJjQ6LTnUAS3SGGmunEmmzrnX1lGgVR76pw8CKuKktBFVYwcAoRxjVSzLXRncgSIqpyzCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|گاتزتا:سران‌باشگاه منچستر یونایتد مذاکرات‌رسمی‌خود رابرای جذب رافائل لیائو ستاره پرتغالی‌آث‌میلان‌آغاز کرده‌اند و قصد دارند این بازیکن روبعداز جام جهانی 2026 به خدمت بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22516" target="_blank">📅 09:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22515">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cukc3P985jCY8mnUdn47GZ0JQiD1DifdXJ1z925zWMfPRJwrAXI_O81pFb6pR1geV_7YHTsayrdqsSpyjXs8x9kLV4loLqINRZ7W7hmqUoh8GDi9W2ncNwfmu_Qpl3e2HqPFgxAoDtr_fqCdOC2AEbPNRqht7d6d5KT96xZZTdWn4PEfcJV8k7yNRCZnGQ72pUikutd28YzAJYnPJiWFFc-l_YBAUz8P6NH7GpYXhFYNbeo5NfWguBI9XoKCX7GXqHN6rIWfYg5_r5pU0FnW9xFhWwdCjaIyl8UeHu5R5FXXGLfzurVTaZIUk9rZu70PH8GfM87d_B6f85AwNtZCrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ برناردو سیلوا ستاره سابق باشگاه منچسترسیتی؛علاوه‌بر بارسا از اتلتیکومادرید نیز آفر دریافت کرده که اعلام کرده اولویتش عقد قرارداد و پیوستن به‌باشگاه بارسلونا است. این انتقال بزودی و به شکل رسمی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22515" target="_blank">📅 09:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22514">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WS0Oop227nx4EbtFYI0C-8TmCV-qGzXf27yaSEDdrugIT65MxbynwTzyuddqbXaAaz1rHq82Z5m0XPz9LCVZAkn9dzQuCbvj2kJXA4C6gEeRov4A4TKKGF1rJeT7HSkB_d7Ll_qqOMPGBd0-ZMeMUCZ9KC9KyoaCrNBqkf40p44Q_cYg2hiL_ukm0NkhBlrFE1t95gEroVVUx3QmnW_ebQIxhA3zaBz6OsImoZsilzOdL6AkNPDY7npCsTzDRL2z9o2lO9DXkEVHdwJR0az1YQkyKaIs3Sy-vAFxyYWK8uRCOJiC7NH0wM_t1wtalKyPBJ0Q4wyfv9SYsiT_ag7x5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
مدیربرنامه‌‌های دراگان اسکوچیچ سرمربی سابق‌تراکتور: به‌باشگاه‌تراکتور قول دادیم که امسال اسکوچیچ راهی تیمی از ایران نشود اما اسکوچیچ از ابتدای فصل آینده با یکی از سه باشگاه سپاهان، پرسپولیس یا استقلال قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22514" target="_blank">📅 00:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22512">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jg5QcwB8FF68O7Y6EAeNAPOpU6QFU4w1JY4nGCqcujiFYBN1sWoczyc71-z3lOrJ-H1koDV86xuaoNjQYGwVDOZ9Q7kt6cjM_2AVSU9moC7WmLpuGL9jZEP_ZCEoE4Dz-i8FkZeS6HKDa5JDHW67PM3_FKUTwBN5VOAtfc0hn5hOHk5So03zZH1ApXrydwuzfYzKIUwK5Yr4oSS1elaAcoiQSkTKwDDA-hpVtMes4kNn_7-Anl6-IhCr6jvKhe8IOCBZE6apmBoVSEM2PfU_D8bv9WnN9xBWGzLDIa0yXxvz07nQZ_JtjGSeQ1Nf_08Rfh2ntKg8ILHlMxEuSOvccQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌بازی‌های‌مهم‌‌امروز؛
آغاز مسابقات دوستانه ملی پیش از آغاز رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22512" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22511">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cz0tTMSX-rEwVD0i8OCHSZdQzfIPrWxU5gpUocMvfPXfrzxWbQ-5SxYPFKoxzEahSNKL1_CP2SsBUA1S8q7MywoQzk97IWr5hr7Y51PcRQfvkAep00Cks657r89rcjzGBj6YKMDI7J3wUHR4vxSrLM6e8tOVFyHJJeGgyFUxGKmyzmaJOpl1ymrMz2LbddWWgdA7Slp54NkhDl4mbe8yyMVmqPP50vuJKSWSzBB2BOiPq-uE0msJaq4BciBhYKdmLrUiN7_RumcupfCCO7LpFN4Ub92LVOB8YVw9ZmsFrfXD2zprFEnUFoYJp8RvRWJ12kIQB2IhdtpSCCWNNnTe3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهادیدارمهم‌دیروز؛
دومین قهرمانی پیاپی شاگردان انریکه در UCL با شکست توپچی‌های لندن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22511" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22509">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_Wv_eGNjWvMrTM6fMBFdoO2Flt3VgVTdweuqcEc7YAObH-ZRvRkXG3KJ6RA8SxycAzobGgTLw7kNfj3WCvytkd-bLir0RvWfTEkxuP1w-lidWyUXN1AB5WKlacRZI4nhD6NZ49WwirfrZl2ernsLGpNmw-7APcRds_vqNy_aLOl7KESKXP4-gzrHDHYo9P0azy3ceKqvt-aHwLsWdGYL3eXoZKdipx4RhxjmCCW9dksRbDJFO3wowsyZtnlyGPYqTU6N4xcCzXBhZyOloj72CTg5R_WgSv2T2OORno8CRSdEvDhW-QcXZN-S4xZwHgXVpEVaMZ0LqKTlbsirMNxNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های دوران سرمربیگری هانسی فلیک‌ و ژوزه مورینیو سرمربیان فصل‌آینده بارسلونا
🆚
رئال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22509" target="_blank">📅 00:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22508">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkDYXd3brWcdyXYZLCi4C8S4R8eJnLPWgYp1ZdFbn0SU2-l8qhwml9iAJSFSEOhZ6cQauQU2USX8MFO0H-O5ZKofqpLC-NIhdmZPdwnKoSl3-kxedt-liUxYBUFLtM4-C-lFj_DVwURlkxMYQOXE0zFw7nFNcqd7Sie1d8LDCCr5l7UooD_TzCKzn1Y3bkEAYbRXVcq07jYM-zgFJDIOSi84Ub7Ublz3ZlTiZPkrfF2QvYJAd7-ojxN-1cUZal7KDP0LEaWXtMb85hVRwoXGRa1-l2RQTf7F6rotP1pxzJsCSiQL2H8OqDk-FipHLL1Gd6vGXsMht1KLiFGOq8ALQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22508" target="_blank">📅 00:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22507">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTHNnphwbZzfgMlePtbU8KgfNHy0IsQdI11a1neVCdcCAqhrc_DwK0ocyogJTKiqDL8wshLRnyRMdnBOGFInikfhzXHGFn6h7k9qqKLXYSmgbpBonOtolHEN0Oyi8nDDsoRm-10ms1I6pkxAqRAImAkcDcP8jai5pu8hKDS7WVVWcu4P4qZm6Q4El7ye_fvsvetPNJJ0tlAnhsN-t4fm_7h-EL7BW_OGneocekbFGwa8ZziFPVjtcyouOT8NJb0wPt1QecwyvG7LDP8CpFJB11xMVTbRhBO6d0hP90IuDn4epeR9mudQsarERGv05ZbYRM9GI0UolSYzmrjpvKJgKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
تمامی قهرمانان ادوار مختلف رقابت های لیگ قهرمانان اروپا؛ رئالی‌ها همچنان‌بااختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22507" target="_blank">📅 23:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22506">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsXWaLmme6jNVuVc5WmhKHfezbWZ0nDN0lbGp77sJ5R87ewAloC624ORRMoWrMsaePcujBMoHsQgk-EfDSIYrncn5KbmyF_Wc8gYB81WrkW0o0BYbVaFsAsbaWfRwb_nBMgq8frCP0YyBmbjbvFECXzvJYRqrdekK68Pr1FMtSrGrXddFg65AD64jJi8Cb7EUduHthWoj-e0_cbCtTodZ3sO0YHXopmk9gHCHj7c2IXu_8BCXUjw618AZ5LdJ9SZU3kDPyVaXD4sej6gaqvsnV9_pUtjEDEvgplbJi7vRgQ2mM0zEp7kFlPl0DR-hmEjr68E8zkHI0hx8gX_jo-2RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌ضربات‌پنالتی دیدار حساس امشب دو تیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22506" target="_blank">📅 23:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22505">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d5a3b7a3.mp4?token=fhPKgSUFQnq5rhWlJBFKt2YgVlakyBXlri0dBu-IIt5u6IjW4yEdiDYIzLzAZ8bm_2brq880I5DjxHQJIoEbzhJg2_m0pBiNXPmwaVKWoMWM9H0HeYVuH4cdlhJrSN76ZhEpg3Dl2ubBfBUIf6dGWQWy9MYoefkB_RZ2J7xb25z2ADrX1KNVl7jqv5BJpyOunzwRFmlb_BbZiy1qCg7P5Rh_olgODiu1o5REPm-JhqdUG-BsADmmiEMiFPjmhR0vcea-t_HuVfYWD4SL3uno5VYfo2ecsfGZc2E-uoXedXY-yxCvrCpobVGtB72W1eWkBhJnpuN6-c6Z4dWnq_fehw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d5a3b7a3.mp4?token=fhPKgSUFQnq5rhWlJBFKt2YgVlakyBXlri0dBu-IIt5u6IjW4yEdiDYIzLzAZ8bm_2brq880I5DjxHQJIoEbzhJg2_m0pBiNXPmwaVKWoMWM9H0HeYVuH4cdlhJrSN76ZhEpg3Dl2ubBfBUIf6dGWQWy9MYoefkB_RZ2J7xb25z2ADrX1KNVl7jqv5BJpyOunzwRFmlb_BbZiy1qCg7P5Rh_olgODiu1o5REPm-JhqdUG-BsADmmiEMiFPjmhR0vcea-t_HuVfYWD4SL3uno5VYfo2ecsfGZc2E-uoXedXY-yxCvrCpobVGtB72W1eWkBhJnpuN6-c6Z4dWnq_fehw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اینم‌نسخه‌اصلی صحبت‌های امشب عادل فردوسی پور برای دوستانی که قصد استوری کردنش رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22505" target="_blank">📅 23:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22504">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a1e84d8c.mp4?token=K6HCChIdbdE3lpdMZn1SuEnsucfY05j6LpmsA7goBYsXgNiuxv_Mq8ZXHCbmjnuyxTgoNcueW1jNF03mVFfenRBJ8zCpH_ES2YlLz09i7Po97bSlIcVJa4IZFhgu5YwLz2Lx8q7L4B8Nbfd2QncK8lAvKX0NENiROBfzxq5sjcICZBEz0hacgaf6U_3VdNXaFFB7HK1s87hTJbcJZS84B3_7vQeEPeZzIceY1ewVf_Srgf4_hUDTNMhnSTpOejIglA7YbPl08-DuQPnkpy_Y-9pvVfVqvF9OdkDLBPE_I70I9eknCggttgUChx4JcCLAvjWicOLTaKR54kGhosE81g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a1e84d8c.mp4?token=K6HCChIdbdE3lpdMZn1SuEnsucfY05j6LpmsA7goBYsXgNiuxv_Mq8ZXHCbmjnuyxTgoNcueW1jNF03mVFfenRBJ8zCpH_ES2YlLz09i7Po97bSlIcVJa4IZFhgu5YwLz2Lx8q7L4B8Nbfd2QncK8lAvKX0NENiROBfzxq5sjcICZBEz0hacgaf6U_3VdNXaFFB7HK1s87hTJbcJZS84B3_7vQeEPeZzIceY1ewVf_Srgf4_hUDTNMhnSTpOejIglA7YbPl08-DuQPnkpy_Y-9pvVfVqvF9OdkDLBPE_I70I9eknCggttgUChx4JcCLAvjWicOLTaKR54kGhosE81g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
صحبت‌‌های فوق العاده ارزشمند و گران‌ بهای عادل خان فردوسی‌پور درشروع‌مسابقه امشب فینال چمپیونزلیگ و تسلیت به خانواده‌های داغدار دی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22504" target="_blank">📅 23:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22503">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZIc7ODvRrNWRdKZ5-6-XFz9SqzXVCHJJYCKBcKYnh5v2qj8dkNintCFGwU_JB1Thw2XIqPuYnIs-rwyXQnBC20Nne3aLOrLFCuGs4Cqc6dP2EtB5ON9VYGlxS0Qz0ynzbO2ZnyxsXEq4Q8qI9GC0ohDbyqa711KekvAwPeIKPYyrrW1pB-L9Qldc7IUtbV8TYSNHBl_dkE1oztF-gcjPinb-41IzX-u05X51TgVRJhEDuSllpdBV-FY-xe_QU_ZNvkARoz4DSsFeZ2GmqiRXS-9xLtxXJhcFQQozMcEG70fXNy-gBKlTtk0cc2nbbznPiNav-jpsqHeAaLbIa8xRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22503" target="_blank">📅 22:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22502">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d915ebc4d.mp4?token=vvyigQdfnS_J1EHuBa8nSeBrWAIq-X-2wnd6yJ0U_WSusC4rts7mvA1Qhv_t0N-98ay9tw1-XCnL-PJxyPG2fmLABR_B6a1K5AISJJCyFevvTPPtm3ld7Su5iOQES-XIwcRBcTIpv3g6t8yiMz2jTDFZj95qOrxkf6mRgpP8JBKyZF0zLPfdQrWM5VPhNe2Nr1k8spaMSPSwIK8naQLGMX2mbUqwlBKv7PSIcuH1tbJj8QqclQdnDi4IL6661_L1WK9qitIiA-QQ_VAYF3s8kO1M_w4NQXArEGzmsTrmRLdObGQtQS8FBGILCo3ANOrbmhm_hRNhgTyqKhWrOvf3qrV34PZHyOWMQ-FO4WeV88tDgvrKsuBKQCskKEZ_ySkQQJDhSADAedDpNVzzM4Do_MEHik55n1rfZK5twwOloMlTDlYybBVP2aOl_r3sv778xlMA8ODTvhhPL8hg_SxyqOMd55v_BMAfGaK4MLA9qgIMB6g8cMym1QMYAtKaA32mSIMl979EkGp1GHUo3UwIKi8ULgXf6mef9dn2ogf9nU2Xa6VEzH7hOHfu2-Yp71PzSDoOG9galcrFO5JwwMGP-6htzBrbtHLOHLhk5vdvTchioBhXAyn4XqETm3B8Zxj-Wn8RCrIxj-zgh0qO6bi8ZhuSU-GWX5m1GFkhR8RMYUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d915ebc4d.mp4?token=vvyigQdfnS_J1EHuBa8nSeBrWAIq-X-2wnd6yJ0U_WSusC4rts7mvA1Qhv_t0N-98ay9tw1-XCnL-PJxyPG2fmLABR_B6a1K5AISJJCyFevvTPPtm3ld7Su5iOQES-XIwcRBcTIpv3g6t8yiMz2jTDFZj95qOrxkf6mRgpP8JBKyZF0zLPfdQrWM5VPhNe2Nr1k8spaMSPSwIK8naQLGMX2mbUqwlBKv7PSIcuH1tbJj8QqclQdnDi4IL6661_L1WK9qitIiA-QQ_VAYF3s8kO1M_w4NQXArEGzmsTrmRLdObGQtQS8FBGILCo3ANOrbmhm_hRNhgTyqKhWrOvf3qrV34PZHyOWMQ-FO4WeV88tDgvrKsuBKQCskKEZ_ySkQQJDhSADAedDpNVzzM4Do_MEHik55n1rfZK5twwOloMlTDlYybBVP2aOl_r3sv778xlMA8ODTvhhPL8hg_SxyqOMd55v_BMAfGaK4MLA9qgIMB6g8cMym1QMYAtKaA32mSIMl979EkGp1GHUo3UwIKi8ULgXf6mef9dn2ogf9nU2Xa6VEzH7hOHfu2-Yp71PzSDoOG9galcrFO5JwwMGP-6htzBrbtHLOHLhk5vdvTchioBhXAyn4XqETm3B8Zxj-Wn8RCrIxj-zgh0qO6bi8ZhuSU-GWX5m1GFkhR8RMYUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیوکامل‌ضربات‌پنالتی دیدار حساس امشب دو تیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22502" target="_blank">📅 22:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22501">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50097d1448.mp4?token=RNRJhqSCRRNzt7J9JX-105LWVVMWM-uy9wxy1kQHh_r0q0vWWHioTgaqg6534hG6Ez3g0QtSN2AGxjrlvLFIsojUdqvZPaB6jMgt-APh83S3uQ6FsIjMYJZd85ZiH8Q259ibAcklF03kqpdlbu7G-Uo_Pk22SBryApHP-ld1EA84xHUQSvFaCY4lLHuObvkgTWqMyoikHmYgQrJCm5f6v_OG57RMOkdV-Fn9_CbUnprIdPh3ePLKIghqiY5jyfOn2Le-ueovmEHNuzHV0MEvfLXZIwtcN3j0UHQZzfnha_shQvb0dx5tUqGHLTtUIZQJxecukTvF-Qv7nLZyoM6rMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50097d1448.mp4?token=RNRJhqSCRRNzt7J9JX-105LWVVMWM-uy9wxy1kQHh_r0q0vWWHioTgaqg6534hG6Ez3g0QtSN2AGxjrlvLFIsojUdqvZPaB6jMgt-APh83S3uQ6FsIjMYJZd85ZiH8Q259ibAcklF03kqpdlbu7G-Uo_Pk22SBryApHP-ld1EA84xHUQSvFaCY4lLHuObvkgTWqMyoikHmYgQrJCm5f6v_OG57RMOkdV-Fn9_CbUnprIdPh3ePLKIghqiY5jyfOn2Le-ueovmEHNuzHV0MEvfLXZIwtcN3j0UHQZzfnha_shQvb0dx5tUqGHLTtUIZQJxecukTvF-Qv7nLZyoM6rMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22501" target="_blank">📅 22:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22500">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCG8XIbk8y0yuxmPFmIN9ds__d4jDOhsdwqt_bqREG0rhKpBaoQbsmvWP34BsGtTKME7By1Cnn_RDebCqmIRPk3Zkfd4fq8oS5n4vwfTjPFMCZZgWyDs-r0ddQ5XC09iVtUV4hHykEmhwzeYwPa8M5rwERQo7iYq6Svozqzb9ygHYhkOXmrLftTXxBjaP3S8Qa6E7y822e2lXi-dvF7Lc-h6ELhUve3KcQqW0VhKQfQZ8VCl89sKbFzdPxU2bcWf2lRaGkwgJAichcju0a-zcFLAc5pcwwsOAowdqb19NIsj38lz9AN20B5wG3CzUO5c0FwyqVud18tYP1qVaTw98Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیدار فینال‌لیگ‌قهرمانان‌اروپا مابین تیم‌های پاری‌ سن‌ ژرمن و آرسنال پس از تساوی یک-یک در اوقات قانونی و اضافه، به ضربات پنالتی کشیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22500" target="_blank">📅 22:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22498">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHoNvIUEry1dUI-O-py39WKsFZvGl6-xk41dzrtyOIqN4AJXHmV35Jpg6gloYBWVC5ne-ALRWOcK93_dXmjSQ_Khh9_aNvgm1WDAMVouHi7d-YQh6k9ruVMerhNMQdrnHDawS0opWNhc-nVEvx87TZ9cGg36ELWyPUNd8Kdrpz3OtoMOSzMbPWD-y94hN4m56g-YWu22hf4EuOz4KUKCQmp4QqP7cSCFu5HT6MTDlrq6vnujq8Xx5_kqcDKzpYsk4Z2iFQXUTrhn0AzZIHzbsobqgfPMBzNPGTtiAsfHYCi96TIjg2HeVneMP3HcBWC2nwbgF6KO4L8N35PE12APHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازی مهیج و دیدنی امشب دوتیم ارسنال
🆚
پاری سن ژرمن بوقت‌های اضافی کشیده شد. آمارو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22498" target="_blank">📅 22:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22497">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHudjAVYa0SHYV0Imt1zJvFoeEQ25dI7ijk7A31EiOOr3yLoNECAkcHm0Eayi5rtAxSZpB_gTgMjXi7-lBatx621Ug1VXxSznjGk_WLjApE5RGmUrZ4bvQI0aGtSvCXj8XnQJMBBIRb47TH8RSxYvluPyEJFmXbuOBhcy4HlJ4qZYoqJPwPAVfQbDg6XANCc53Tvqgeth_X5POXJs3AogTTb7oe9Jqp9QLShEpCCxFeov1Q8tPlT2YCaQVEHiV7JaYGa8eAicTg41wW1sEZfgseCIXTq0g3rWY2qsIU0Dp1f03U2NAsNJyf1mni3a8_QwHEgztPzGHThxhm-mwHSAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|سران باشگاه منچستریونایتد به درخواست مایکل کریک سرمربی جوان خود با ارائه پیشنهادی 100 میلیون یورویی بدنبال جذب فرمین لوپز ستاره اسپانیایی باشگاه بارسلوناست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22497" target="_blank">📅 22:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22496">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euVT_v2piJfZ18Loq64bLeSwNYVsA0vmMy9wm1S-vZEgoUCt-jCtxNI1rt46BHGhQA8m5BDEOA-RwK8lXpPbohz7J-RiYiQlJmOXy_Jcjv9yALbKPDP12eV8ElErIE_Nzh7zTsNw4Oa3yV7q-hAB11QxBWGcdsA29ewbhPThcID2TWMAIwhy8PoSJEcqo1DZK4bdMvA2EdzE2lYGhIF34uXUYpjjM3y2xmj8c5ph73nZ-IDEa_mmhIvtECc8Brt7AZaaduVEuG3PGDptKG1GoWERAtiBKVZxKgzi8_dvPPqWRtUW9l8iS79r-TEJpPTOoBSRRviijR87kNeRsNYXNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22496" target="_blank">📅 21:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22495">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvMSOTea3Sn8r_o7L_UyyU2C0k9XjPwnH-k3CxK3dbyMWsT4kMZW6fsDU4hB5RAeXAfRIrT_lHY6Q5axZ_DYNzib4QXblEyEHw6NAkTvXdxKfSw-cWx83O5p6rsUNGOZIV-sPWfH6a2vNKqFqPo0MbLt-lk9lL_Zy0BK8v42KSyG-4Q9A7VczhZEvGsjM7-GfLW7OmFb0lJpJcrmr_ZjPOE9Ms05hU0Fk3GMRsTWm8Vu1LBlTAc-Je_FP0-8MrOwoP-a9xkilmYWCC1ICmz7m9Q0wgbY6iDWQAMUcaydCL9xjLYEfeCY5fByu46O4kdYitK5mTSzoWONxcrDsjaTpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تنها 45 دقیقه تا قهرمانی تاریخی آرسنال میکل آرتتا درلیگ‌قهرمانان‌اروپا و کسب دومین جام ارزش مند و شیرین فصل؛ جای عارف خیلی خالیه.
💔
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22495" target="_blank">📅 21:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22494">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2Fak6tNLHWI9ZkpaGzwcd_fNzJu9DaZcyP1uw-4mUobu0YT6eUytYd1ZE5ERiCqGlgphr70S9ldWhq1NDHTyRooFpMJgkDFp034yuCD7odFrNdLJdirQtLdoWlvxYyZ8r4eICPG5ZePGHUsH1qR7fSNaulOf_KqCbK2uQv642DEUMA531BvW6qst_Ksw4U4Z_GyGTyeJ7N51Bbj56zeP3QonMSHRDKc5dXFWO_M511pX847HEOMgMqRGDZoYV4Tsoowfa1qxHYuIhYSfH6rOdG4kUo4DxX3qemRhdfGvZ-LpD-0vR3qC-J50h2uhv_wCh-vSaS2q6cKAAdZipKRjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس پیشنهاد مالی بسیار بالایی رو بمدت‌سه‌فصل به آریا یوسفی داده و احتمال قبول‌کردن‌این‌آفر فوق العاده از سوی این بازیکن ملی‌پوش‌بسیارزیاد است. سالانه 80 میلیارد تومان پایه دستمزد + 20 میلیارد تومان آپشن.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22494" target="_blank">📅 20:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22493">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsVBSObVjg-xOnOGd8p9rjRcUKyLc_x6hLxzQ52DTHvUATMyadgUhLj8Ape7GEnQuShjXYtdg-JIPy6A6gGwNjcLW3aC1AtPJwm324uCKk2ZohNdZZjyFuHRgZ9u8_lFRu1nbQLNPyQv9JzrGaQmA1mwukphprgN67aes6gm8G03AP-UFFs2p6Jg4REh7vqjeHGmiZRRio8Ju8AQjGYit4DkDPG6U4vW0h1966WIEfv1E4B7WAfSosmM-nfcfXohFGoaMfSWvUqcDVby_bu9q4BOKDOEcjDoXM129dSwxvz_utL1ufM_IpX0FZmEBj2CYbLv1NJ_nuhMf7Mg0sD6aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
علاوه بر دریک؛ این‌مدل‌انگلیسی طرفدار آرسنال اعلام کرد روی قهرمانی‌این‌تیم درلیگ قهرمانان اروپا دربازی امشب با PSG پنج میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22493" target="_blank">📅 20:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22492">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a443979ea7.mp4?token=TZLek3GLLBBKbpEwX_zgn1d8O2yhcrOFgiRt2EwSV04LMfy78LEvQ4q7ffqa7_ay3kwU5y-iUitOMnwg9RopTRYPp-FGzjSLOeXizWdeK7FM9BOT7Zau41VieEW05lm0hbqZXkh3fCgBEW0Dapl60ws8B4MRRoqGfgiFo5VT7a8x9XhBXKIGBWcGy-clXyfSCqpC10AP3qbko7Rn4jKmWLCP5WdOghPuUO_Dhsg85FkbY7BCqUGy63fe8qt0DZk_sFk1pLqErlu7Yy3nUEAD8HCsJ2GvNtog-KemAkwkktL2qwy_VmjyxhR83940Agplad7r1lXpzSZUM56L7lVwYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a443979ea7.mp4?token=TZLek3GLLBBKbpEwX_zgn1d8O2yhcrOFgiRt2EwSV04LMfy78LEvQ4q7ffqa7_ay3kwU5y-iUitOMnwg9RopTRYPp-FGzjSLOeXizWdeK7FM9BOT7Zau41VieEW05lm0hbqZXkh3fCgBEW0Dapl60ws8B4MRRoqGfgiFo5VT7a8x9XhBXKIGBWcGy-clXyfSCqpC10AP3qbko7Rn4jKmWLCP5WdOghPuUO_Dhsg85FkbY7BCqUGy63fe8qt0DZk_sFk1pLqErlu7Yy3nUEAD8HCsJ2GvNtog-KemAkwkktL2qwy_VmjyxhR83940Agplad7r1lXpzSZUM56L7lVwYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دریک رپر معروف کانادایی یک میلیون دلار روی قهرمانی آرسنال تو چمپیونزلیگ شرط‌بندی کرده.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22492" target="_blank">📅 19:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22491">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdCQbw9pxvtfkTHUxaDOKjJO4tYtQicGay6896qfloN4U8DvB6NQxIWIjAKGWfjUtGCMPgu429vy7_77MOhQGRplY9s3iLArpZVyiCO0QLYkpajCEV_1BlzTxeW85x4xy2jb_bTNmihMULlGB9qcsYImsg5Gc1xTyHJszU4lflOWrjqujxgHyQVeDNNDp-tCi4xGpwJ23Y3tCVbkXfP9JerCnXaBSNFxdy3RDvwpCr-kxUONU-g3ATRv0CZv11t3QAvIBrbhxtRUPR2DfCQ1FyQscS-voP4ocFStq5YTjMLJ9PnvNxVXh6TrVfMI37qEk1rZVGUo9EpwNaC_UyEBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای گذشته نیز خبر دادیم؛ آریا یوسفی و محمدامین حزباوی دوستاره جوان تیم سپاهان مدنظر اوسمار ویرا برزیلی قرار گرفته است. آریا یوسفی علاوه بر باشگاه پرسپولیس از یک باشگاه اماراتی اماراتی نیز آفر رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22491" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22490">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLVgz7SnQrckwqFrhBKYQc_5RA_E90IASe8sCg3MyyhFuiBTK9JmxGY1s5gHAeO0AfdneftOyc3OMXIV5NLllSiPhRjiuXzFxwQl7rwiURGZWv_POnV8pv5WbHxAUZXEYMsl1X0GF0bq6RBUhblPPhimF4pJRjUcyekQM1Uwtl8mUnt4pR-3FFk7t32tR7_0hr2wm-MurTD4T3uVGkps377qPINE2HFjKGbFneeSsC6flFPu-OHcisBqQcmYSipk-7Td1htxcdJpJ5QsOW_fe09gL-loORJeVY2Yk3genAj50oHCxzjzLhEio2mUjLuDjLuqQ-1w8WcFfwENlZregw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22490" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22488">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNJb5kf3Kb5cyLS3hnDxUhdwNBQM5f7pMxuVOfznTwEDMAm8v8lAUmPcft6yvOIrECbC09o2et9eWTlNDhvaVbUhEnEvagrzNDEmK1BKdGUHs3dYZhEqzw-4Rl4Ccd7k_lgkToZ6izsIOK_rDhZlbEreYBUFvNXVbVfGMeIZ1AR4tZ4bfXgLslRZ2VzuYZtQAm8bBEDc3XznG1q3wlwSvq1fcp1eavFGtMLmsKqBmUOdPJskHz1Us6g5GXkFXOk8zbSnwJoQEFroCp7oSP4tSDqTipSXU4Sh23cKkJmT_JBdSY2k023_YE1-Cbc7641WbeJvBndMgr8y2lEi956jmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای گذشته نیز خبر دادیم؛ آریا یوسفی و محمدامین حزباوی دوستاره جوان تیم سپاهان مدنظر اوسمار ویرا برزیلی قرار گرفته است. آریا یوسفی علاوه بر باشگاه پرسپولیس از یک باشگاه اماراتی اماراتی نیز آفر رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22488" target="_blank">📅 18:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22486">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IP7sjpx1L2V3a3AiA7jPpTrMaHVNr2--jLgFBO_uRNLOoOBtHmQVMo-0iUN6_1euT3kB1Kkj0B__x7I9e6tf_h8jKfJW1E1i4Bo4lTfx-skj3glzd9jHtvJV6mkdXdh6qP6lr6b1wxtOzM5HO6vidY2licCEAY6iPJVoY-YAzUHFYHcQhOO78zAYaDxE7kbPzglnKEmngd7NFE-esWqoiffJjKbxTP_qPfCKH0WJJDkRXSGtx3hMpnRbc0lD2G46mpRiX2SatCmGXqSTO4hI-Qc3fHAUP96wlHTpeP6vCdDB_V_FZVc2lplwRPCFKW-EU0fDnnJSZ4a3_1JdjZDGXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iv3hmt-CmDrxEcw1pR8NufDjGhQgSAOELOhHZ3MJVU6MRSDxGDQX97AVjukze6YNaIZF0azp8uLl2uQ_8DCUCRXHXPNTQKo9XmdT2bNRZc8_Ojs5t9ezXsZdFdTvktGUNJEQSCiypfy99srhYYg5c4Pl3rXTDR1CFs_fSdVJ2v1wW4W6Hlq7mswp3MUy4wEC447MTPRGP7vLTCRDQOWnrvXZYIgk7CrcXRO-u2iUj7u3I6Tm-Z96EHp7c-rMWU_R8XD1nu7lQrZhuq2Yworp34xUxWCtTlkmkcEmUQqZvUccZK1sYIFvh71sBz6C2uWnBIJSeQIvJas1ivQVty_WBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
شماتیک‌‌ترکیب‌دوتیم‌پاریسن‌ژرمن و آرسنال؛ ساعت ۱۹:۳۰ با گزارش عادل‌فردوسی‌پور ببینید‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22486" target="_blank">📅 18:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22485">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRFnamdz9cYgwZMnuec3TrXvi-trEREH5_W7ZzXjRr0hQJmLVbni7dsbn9oZYO9tyi8GI2_5t7zyppTOIFU-zAZKsuUne4UorHObd6JsFwGJbJdfOyIT3gaZaCE4c24SrEehqBQKPBpo_cKJ5plGg0L5JPQKLmEUnQIMu0BFvh-MZh5l_GFtoj1x6TzEpX7Tf0jdUjCGS9cvVi9tu5ca9oax-F_MSG0-SIaKyjwhG9BTBspVTN_oupIT3-obVDoGd6SfZC_e3662iVc85YG5ZFra09N-LIcXePBWF_o-bEAKP8N-k-tqGzpupqqeG3CYDpUBkR1M_UKQFJiNxrtAIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکردفوق‌العاده‌داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان‌اروپا؛ رایا درصورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22485" target="_blank">📅 17:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22483">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bF-zbxFoNexZvoVqPaHvdNBrd53j9DyKNcA5iXOMl5XmgL1k9PYMHeQapcp2rjZbseSdzExTVZ8H_c0BL-xhHYrvE71OHiIohZfciahyoW1R28OBS3N6RZ0KTlbYJc-WopKR8CGau-G2pmUanRXtpgwzgWURiPdbe3J24ecx6IMrw26ILENSHGFla14YKGG0ECOIF_22DjbZzY58z_6eIFzwnzWrMjgopCKWIY11C6mlERF7-YqvP-5ZHlh-vmiHKlbuok4nstJVsmLNfrO2SfG5UbvfACDUWOF8UVDYHu27SZLzazOv7JdKpaEZcgn6M504yKDITXNb7tyUk4jcMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22483" target="_blank">📅 17:35 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
