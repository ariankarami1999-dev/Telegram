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
<img src="https://cdn4.telesco.pe/file/vgx5oraikqM_9-MbJruknH2f-YxSaAUZaL1sKvjkuI64aMtoaGfwEdwARppnsnGlGfPmatTn91jLERqR7hyyuZeMUeLoUCqamu61WqL7UAqr2mF1hmkqyt7DtP4LzSF8Kkt6UASxjdk81UQCgAy4ghMUnf9OTuDvtREU5uEi9SYnT_drcnNTq9PUnFV9TDNiknXFca5-SrRViS1sefJiAt7J2_Gbksrh0J4MDp6VkuetZfpHzFLvhr9nGCegjHhDKurOWYM0tn5UENJ6Fm5AeviuCLDl1ANVwZirGl_al4eg5yRS0MD9xMEFsaJUllTg256rofMwW3OfllSkHdr3Uw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 11:29:05</div>
<hr>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=DcVN2-PqljwoGYHadtohHMUa_VHbnxYH3JA4sw-IaByqhpg_AhjhflfF65dUl9T3emFFphePrQNyAdOVx4tojYSQ71cqH6RjJm5l5PbW8RlQHRcgoaF6PKwzqVeJAdARBe8iGYYFoem0KlqS_h-gKs9e0oj4B_7DbDSZ9JLAzYjaFhs0RiJH-iRA4XHLmKvBvfLCuOYek-h4guEb_9FL016kgdJ3LFgkOh7xcQjoLU3Aj_zmoVVyCpjPgJwWt0pBHNg9f2gmllSB1ID9C5aim70bkyAvaP64dzeEKFqaHDUCIG5O946X7o6G35VOek07mEedmiplnZo6Ih9tFXBiJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=DcVN2-PqljwoGYHadtohHMUa_VHbnxYH3JA4sw-IaByqhpg_AhjhflfF65dUl9T3emFFphePrQNyAdOVx4tojYSQ71cqH6RjJm5l5PbW8RlQHRcgoaF6PKwzqVeJAdARBe8iGYYFoem0KlqS_h-gKs9e0oj4B_7DbDSZ9JLAzYjaFhs0RiJH-iRA4XHLmKvBvfLCuOYek-h4guEb_9FL016kgdJ3LFgkOh7xcQjoLU3Aj_zmoVVyCpjPgJwWt0pBHNg9f2gmllSB1ID9C5aim70bkyAvaP64dzeEKFqaHDUCIG5O946X7o6G35VOek07mEedmiplnZo6Ih9tFXBiJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farahmand_alipour/5886" target="_blank">📅 09:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=qPZkZ2no-TUJERbp0BqarMkK1-zTFe3Rl-FRnLDpSSE9fVl9BE5pK0vHKR27ynFUkqIC75DaQRZEua0eMXh32JUcm2cTmZ7xodpyuO-uvCLFqskwbLEgjse51g5NqQb8GWdRDs78jz-TTT75DvLJVCYyDFNp_W6mu2jYtGwzdEUEPM4e2j3NcRMiKz7fEoE4n64Lbc5LBRerQtJPzEc6PEXDrQ0U24lqvd_qydcWgAG9sdG127t8Dsjh9uxh0U2zdgHTwyosp07GQ-MuzRDfwEU2sPHzq_cTyLjIJRcFLL3itbgI7ncLXwxqxqkqi8Tbel76N1EMbDF28Qdgp0VZ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=qPZkZ2no-TUJERbp0BqarMkK1-zTFe3Rl-FRnLDpSSE9fVl9BE5pK0vHKR27ynFUkqIC75DaQRZEua0eMXh32JUcm2cTmZ7xodpyuO-uvCLFqskwbLEgjse51g5NqQb8GWdRDs78jz-TTT75DvLJVCYyDFNp_W6mu2jYtGwzdEUEPM4e2j3NcRMiKz7fEoE4n64Lbc5LBRerQtJPzEc6PEXDrQ0U24lqvd_qydcWgAG9sdG127t8Dsjh9uxh0U2zdgHTwyosp07GQ-MuzRDfwEU2sPHzq_cTyLjIJRcFLL3itbgI7ncLXwxqxqkqi8Tbel76N1EMbDF28Qdgp0VZ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم که میشه سیل جمعیت رو دید :)</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farahmand_alipour/5885" target="_blank">📅 09:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=OIWGfNFlH9dAUY4rnUM5dVqT7CsOq1TPfhABNqVF841JN7qng-ny9jjxIjTmXi6j9rqY86mvtoykhfzO2LQfVE-Iun_e-ZJey4J3LDNuogEuP4fYQ5SUhUNbepFX7AUrLUk0eHtJZYbuiIAyxSHI7-i-BdYAToNOzHK1lL00JQkucYSm9Mis7tUpVGk0cVZBSfF9Sxj3eJtXjCSRHDFN8n1PGWoWKSCOtnhlMki7TLzeudIrpmRuYDZwQDgqUXvqkuvcY8vkkWOt0527PU-w2L7gicNkNX3CsrifiyoOOr3xDHdwLpXAk2Rt6FLcmgsvZP7b9k3Xr0Po592DCC-F3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=OIWGfNFlH9dAUY4rnUM5dVqT7CsOq1TPfhABNqVF841JN7qng-ny9jjxIjTmXi6j9rqY86mvtoykhfzO2LQfVE-Iun_e-ZJey4J3LDNuogEuP4fYQ5SUhUNbepFX7AUrLUk0eHtJZYbuiIAyxSHI7-i-BdYAToNOzHK1lL00JQkucYSm9Mis7tUpVGk0cVZBSfF9Sxj3eJtXjCSRHDFN8n1PGWoWKSCOtnhlMki7TLzeudIrpmRuYDZwQDgqUXvqkuvcY8vkkWOt0527PU-w2L7gicNkNX3CsrifiyoOOr3xDHdwLpXAk2Rt6FLcmgsvZP7b9k3Xr0Po592DCC-F3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضائلی عضو دفتر خامنه‌ای هم انتقاد کرده از صدا و سیما که «مردمی که رو دست خوردن» رو هم گلایه‌هاشون رو منتشر کنید.  یکی ازش پرسیده از «بانی»  چرا انتقاد نمیکنی.  که خب معلومه ، بانی خودشون هستن :)</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farahmand_alipour/5884" target="_blank">📅 09:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KurUdiUQFJDGZqJXu1SBJedos0rvnPIFfCvFY1SOvWVZrZdermD7LLdRFYig2qdIbmOzaf8WEOH9f8-xdYscR08qrSIf9lQonRZyCqkQO2X9G3THwY_MpQlSDKUcWA6TvFDasivDstk3POdATCk2AfD9zYxn0R57vogTSMGwMCHN4fV5Ngj9oSHhUTx6TM6EUlCtRM3ggjFxGP9l2-SjQ7Taw0uOyVdL8xCCHc8KApurfKbKNyj7o3IJrSXx-O9ROj5f7T8s_kc5-YLCBp63QCIjZfhgff-m51OL7ZOZOndW0gXsAV1LpH--EAyi3eJ1AtTRgSuEz2GjOf4u9ORHEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم مجری شون اشاره  به حذف این مسیر میکنه. همه رسانه‌هاشون هم بسیج شدن بگن  نه! چون جمعیت زیاد بود،  ما مسیر تشییع جنازه رو کوتاه کردیم!  در حالی که مگه میشه اینهمه روز اینها رو با اتوبوس و….. بردید،  چند ساعت مونده به برگزاری میگید به خاطر اینکه جمعیت…</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farahmand_alipour/5883" target="_blank">📅 09:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=Zzu4y7QB3enEN-DVaV0NQ_YlTP3X0tkS7oSPBkxCkHAbIPmGcevN8r3CoN1M_0J4tYSA6iNANiGGrCuzxplLRxVFRBCQS8bUG3S0qDGoMSQ30UxGl1MscrfV1FU0ASQRHJzy6w9bz4-yh7XZXH2Xnu64Q7TuBp52T7RoxDjSTYBIoXcir-FvcZT_bHWst5281nIGcqVDJnnBcZF6jBDWscZkPxnMy21WyJB0s0hzRPW1Ax3PV-27IY_rjTP-5rFvO9MpfoHyQY08dCu5TQCVG8UXJXPY8thL9TEE4VT7SrnN8x-BHejSb5pxBrAKUEDYipSsKYjzTFWQlKOxuo9U4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=Zzu4y7QB3enEN-DVaV0NQ_YlTP3X0tkS7oSPBkxCkHAbIPmGcevN8r3CoN1M_0J4tYSA6iNANiGGrCuzxplLRxVFRBCQS8bUG3S0qDGoMSQ30UxGl1MscrfV1FU0ASQRHJzy6w9bz4-yh7XZXH2Xnu64Q7TuBp52T7RoxDjSTYBIoXcir-FvcZT_bHWst5281nIGcqVDJnnBcZF6jBDWscZkPxnMy21WyJB0s0hzRPW1Ax3PV-27IY_rjTP-5rFvO9MpfoHyQY08dCu5TQCVG8UXJXPY8thL9TEE4VT7SrnN8x-BHejSb5pxBrAKUEDYipSsKYjzTFWQlKOxuo9U4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول مسیر خیابان دماوند تا میدان امام حسین حرف شد A بعد مسیر میدان امام‌حسین تا دانشگاه شریف لغو شد! B در آخر تبدیل شد به مسیر دانشگاه شریف تا میدان آزادی C که میشه چیزی در حدود ۲ کیلومتر</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farahmand_alipour/5882" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2iBDKl-qD_N0WFKAQ_iU6vIq7Pf1w5-xVRkNqESU8Vyc2BRLMfmANjJNXArnN9VOEXnOzpG3t_cpvwt8NzZko76mM7cXBbyFx1Gsk1AGSHgCwOuXlHDrG98RY06DoAbNktWueA5O3QGoOLUJsQa8n3ZF4XYglyjiKIldw25nH77wMtref8ojlWYcm5C1vn4gpDw5HY4xqEzc298trGT-gGMhJo5HTtORDEJNqwvlqztqMyJxBr-rwcP_-GzBTaWp25mu8VmniWUlEvIESR0n_EheGgTuxQY_TDmMI9gVVvKYNuOENbj5ap15_nOX0BqcYolOA043aqZyKNu-Y74JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟  دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.  صبح اینو لغو کردن، بعد مسیر امام حسین  تا میدان انقلاب رو لغو کردن :)…</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farahmand_alipour/5881" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=eYs5x5BXhvb2rOoTbiqz0exptwqHh05uKm5JmdgblFewI6Tox-bxfGcRYkw4t--nE-aXhvRkQHWHRx9L4ia8YsT4Axz_e0hT8qTO6AtUTgvCRus7UKMZVgAdp7uREBjYqw4lnaTgcSXEKgEr-LBG0bt_Ci6yYp5j-uJUikZKQMe_6l_i6rHLgThgcbCYySL_Wm29i7XDJeHpePbpG5GqQWkAQlfY5SG8tqq79BnTNaUQlBlpmaXWhXWSAOJL1vUGx3ZvWtWw2Qg28mL1H0dd3FMVhkTDkuefxQGfiwGu294jBNjbCwLDb14L8CtBJW31KpuzQjBRllRolVewsxtA5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=eYs5x5BXhvb2rOoTbiqz0exptwqHh05uKm5JmdgblFewI6Tox-bxfGcRYkw4t--nE-aXhvRkQHWHRx9L4ia8YsT4Axz_e0hT8qTO6AtUTgvCRus7UKMZVgAdp7uREBjYqw4lnaTgcSXEKgEr-LBG0bt_Ci6yYp5j-uJUikZKQMe_6l_i6rHLgThgcbCYySL_Wm29i7XDJeHpePbpG5GqQWkAQlfY5SG8tqq79BnTNaUQlBlpmaXWhXWSAOJL1vUGx3ZvWtWw2Qg28mL1H0dd3FMVhkTDkuefxQGfiwGu294jBNjbCwLDb14L8CtBJW31KpuzQjBRllRolVewsxtA5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟
دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.
صبح اینو لغو کردن، بعد مسیر امام حسین
تا میدان انقلاب رو لغو کردن :)
بعد تبدیل شد از حوالی دانشگاه شریف
تا میدان آزادی! که حدود ۲ کیلومتره ! ۲ هزار متر!
مسیر حدود یک ششم شد!!</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farahmand_alipour/5880" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=LHH656aXiV45U8Ql5WWK-aazA9WIsJ2i4lf9dgzKlHts7ENCIUrWGk7rBZwN5Eae64iirM2QYDn_wvwF9wTx4RPYqxkdFCzz203-9YuanPyNsluVWTaBkGdGVVocrYadCbEUtdzwNYsGOIFxLqIRPruvUlBJ9ubo6kWfhYyDByDK4nBP8orLbVdbSNCXJ67q0D6HD9ckhwqVUQzfEMUGBGuVz_gfDpMyJeLXIxU2BSdXMgH_1aXtIhvZUKdGStnRK9xT4rDviUlipdQa9PghGp1LqwjGZMUJocDDnwczc7g4FYjb0NEPGoocaOOn5cyBY6VfgI9DEBFII-QCKgzIzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=LHH656aXiV45U8Ql5WWK-aazA9WIsJ2i4lf9dgzKlHts7ENCIUrWGk7rBZwN5Eae64iirM2QYDn_wvwF9wTx4RPYqxkdFCzz203-9YuanPyNsluVWTaBkGdGVVocrYadCbEUtdzwNYsGOIFxLqIRPruvUlBJ9ubo6kWfhYyDByDK4nBP8orLbVdbSNCXJ67q0D6HD9ckhwqVUQzfEMUGBGuVz_gfDpMyJeLXIxU2BSdXMgH_1aXtIhvZUKdGStnRK9xT4rDviUlipdQa9PghGp1LqwjGZMUJocDDnwczc7g4FYjb0NEPGoocaOOn5cyBY6VfgI9DEBFII-QCKgzIzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنتی ۱۰۰ ساله که هنوز انتخابات در ایران
در دست اوست. اینکه چه کسی نماینده
مجلس شود و یا رییس جمهور شود و…..
مکارم شیرازی هم که هنوز
«حرام است » می‌گوید، ۱۰۰ ساله است
، خامنه‌ای در ۸۶ سالگی کشته شد
اگه فقط میخواست به اندازه جنتی  و مکارم
- تا اینجا -عمر کند، باید تا ۱۴ سال آینده هم حاکم  ایران می‌بود!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=n7VSooJAdq5r85H5fTWn7pPB-JGK9yceyQZqMFm9COxMISkZE5IG3CL3Izc41MLNo4K1AkkQW8vvj4Ktbvwp0HMFXROq-AzQOb7MEGOgwvYgTVaP4hyP5WIbKZysPnI8O8gZXhJLzV6GnHoXVmhNPStqxwKJyDPQWFn6rgU044mBVt3WjRuekCrrNrZ2xEudBE3FEhKsDDaBaBkJ_ea1N-Oyj_7wSJUpUnKwINJeiW4Eoj8mUff1gMEWvmGK_-LfKvgOcWDKtuXKGLMDdoBz-cjWz1yyj1KhtdIUH87G1ZbOs928Xu4gTXWXtIsz90_nptfx7h6EKkUKdSiBXk-7cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=n7VSooJAdq5r85H5fTWn7pPB-JGK9yceyQZqMFm9COxMISkZE5IG3CL3Izc41MLNo4K1AkkQW8vvj4Ktbvwp0HMFXROq-AzQOb7MEGOgwvYgTVaP4hyP5WIbKZysPnI8O8gZXhJLzV6GnHoXVmhNPStqxwKJyDPQWFn6rgU044mBVt3WjRuekCrrNrZ2xEudBE3FEhKsDDaBaBkJ_ea1N-Oyj_7wSJUpUnKwINJeiW4Eoj8mUff1gMEWvmGK_-LfKvgOcWDKtuXKGLMDdoBz-cjWz1yyj1KhtdIUH87G1ZbOs928Xu4gTXWXtIsz90_nptfx7h6EKkUKdSiBXk-7cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحیدی ، مهم‌ترین چهره نظامی جمهوری اسلامی که برای ۴ ماه نیز از نظرها پنهان بود،
این مدلی و با موتور اومده دور دور :)
حکومت آخوندی - مدیریت آخوندی</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=j9Es14Giub-MvbFIHY44D5GOKPX3LmKkxyuOmTHB6FgXDeZs0ItISgSJT9dEET5HF2Ri-3TZL3MuJqFuRk71EEYe7HL3ivVYnpgtrxI880M0ApwOuuvj0UOam1bTLYAf994KTT7XCK6PRsR4-EXPnZ81ltEtujZ2JfhxEKytT9J5greXGTqSWVslV-Ky3S-TLdEzUAdUMzUPcf7xWnVxPyXvjIzChv5oaRKnLpGkGjRD8YpIrdO4zIxefzLOAUUTmxheunGH8ZtMPHsaUNjHHxgh_DprDp7wsthSvUVnbYhfmgCJFeJkkZNn4bbFZvWN7einQebFp7pz4bmuZx-5sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=j9Es14Giub-MvbFIHY44D5GOKPX3LmKkxyuOmTHB6FgXDeZs0ItISgSJT9dEET5HF2Ri-3TZL3MuJqFuRk71EEYe7HL3ivVYnpgtrxI880M0ApwOuuvj0UOam1bTLYAf994KTT7XCK6PRsR4-EXPnZ81ltEtujZ2JfhxEKytT9J5greXGTqSWVslV-Ky3S-TLdEzUAdUMzUPcf7xWnVxPyXvjIzChv5oaRKnLpGkGjRD8YpIrdO4zIxefzLOAUUTmxheunGH8ZtMPHsaUNjHHxgh_DprDp7wsthSvUVnbYhfmgCJFeJkkZNn4bbFZvWN7einQebFp7pz4bmuZx-5sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت آخوندی - مدیریت آخوندی :)
«برای مردم یک جو ارزش قائل نیستن!
مردم رو بازی بدید!»
تازه فهمیدن!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=EN7X8pslPaydKhWDhyH9cHudxxsS4gmKAbIPYcEfyNTVVy0A1Hm-paeOxTYkZfSlmXvxUUq3qS3mP7kZlxlAydbnki9vDMgiRtDeovv47XL3XyTHPKpcKPNW-00U7hatJKkZdmHTmlmPs2uQvqgSNTHecgxBldLXSgBPbtUXlLkzvPlDuHuqyEmsgvQa-T4AqvQ3Y_pcOoYNkTdS-GsFlB6Y8pNnrPFUR54yiyJ5qjgBrZn0jWCRNa4Iw9krzTwa65N3PST5KwI3HVHJ5BgHViG97GzvSbKJDTrWF99l1F0UAlVvqxIDzokMQFQWVkfIC81gdGLJGicEnG6AZKPM4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=EN7X8pslPaydKhWDhyH9cHudxxsS4gmKAbIPYcEfyNTVVy0A1Hm-paeOxTYkZfSlmXvxUUq3qS3mP7kZlxlAydbnki9vDMgiRtDeovv47XL3XyTHPKpcKPNW-00U7hatJKkZdmHTmlmPs2uQvqgSNTHecgxBldLXSgBPbtUXlLkzvPlDuHuqyEmsgvQa-T4AqvQ3Y_pcOoYNkTdS-GsFlB6Y8pNnrPFUR54yiyJ5qjgBrZn0jWCRNa4Iw9krzTwa65N3PST5KwI3HVHJ5BgHViG97GzvSbKJDTrWF99l1F0UAlVvqxIDzokMQFQWVkfIC81gdGLJGicEnG6AZKPM4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=FJf8RM0ZtWqYt8xvSFARTk-TxCl8ICfBkiqMSRRyX5C0lrIVceVKTcJ6zAJuCZ1mR9TptuNlCkP_4BxcUjx6BO5x2JlflCXjQ5esIE6SEjJSnt_qkw8BbgTdrnOUrfroFLVX1s2ZowrvH8OSZYJjZzn9tLmuI3CGDdK-9vDiSOZ-EAVZMpBAAiJqxZ4Tqpi2N16NYZ6JPXv0eYTX1OJfpoSExQvBVewOo3C1dRycNQTOUOIC0bhVryFXv79NsMZTcSHu7UbzeMKNyTMcNTPfTRuSJnZTQUMypB9yJ_dCi0xJQ4gAD30656o9DV769uVSvqDDw4cvc51hu8UnRlf8sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=FJf8RM0ZtWqYt8xvSFARTk-TxCl8ICfBkiqMSRRyX5C0lrIVceVKTcJ6zAJuCZ1mR9TptuNlCkP_4BxcUjx6BO5x2JlflCXjQ5esIE6SEjJSnt_qkw8BbgTdrnOUrfroFLVX1s2ZowrvH8OSZYJjZzn9tLmuI3CGDdK-9vDiSOZ-EAVZMpBAAiJqxZ4Tqpi2N16NYZ6JPXv0eYTX1OJfpoSExQvBVewOo3C1dRycNQTOUOIC0bhVryFXv79NsMZTcSHu7UbzeMKNyTMcNTPfTRuSJnZTQUMypB9yJ_dCi0xJQ4gAD30656o9DV769uVSvqDDw4cvc51hu8UnRlf8sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=on3LibvBC5XQ74LOr-E7JsTa78I4IuXi_CVTJGTFYBiZ8jr4ZDxFddP6rlq80WPFigVtOdm1LBdy4O-cHmWmZieui5DfuYHRsZkA5a2FzDbGrInN5_x9CCLOyJRq7ZsjeQw4YaY5kv6yF7QXx2dW1itXWZJhkISV4SvMLRLcXvJ3i7sjlDkP8_-5cvme2JEZ3kNbZ6whbN9Lijzu2crsxwAd9fNmoiKLwOQPlWJBk6G78ClNZZeDQ-y0VRc1pWfbVcCXBlQi6TmomJM3nWOt1G6J2gPnIhfiZnRxbGhJqMfrGdO_29ItfGwzKX1tsAaU3GJbXBH1-S4NfVHNd9u8AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=on3LibvBC5XQ74LOr-E7JsTa78I4IuXi_CVTJGTFYBiZ8jr4ZDxFddP6rlq80WPFigVtOdm1LBdy4O-cHmWmZieui5DfuYHRsZkA5a2FzDbGrInN5_x9CCLOyJRq7ZsjeQw4YaY5kv6yF7QXx2dW1itXWZJhkISV4SvMLRLcXvJ3i7sjlDkP8_-5cvme2JEZ3kNbZ6whbN9Lijzu2crsxwAd9fNmoiKLwOQPlWJBk6G78ClNZZeDQ-y0VRc1pWfbVcCXBlQi6TmomJM3nWOt1G6J2gPnIhfiZnRxbGhJqMfrGdO_29ItfGwzKX1tsAaU3GJbXBH1-S4NfVHNd9u8AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKmWCFdbC177garEVpFywZO6OmDQ9P9kz0ezJgd8awrRRslhQ5BAAK5cYAv3PoxzQ_Tudt8S083hsY8r6vJlhVJmU3qqS-bzzeCBinluBBghH1o38ZoNsvZ1xW8a2GrddkNnGnxjE-ZyfgXhrpk55Lek1EZK86M6AG7pxX_sM3cfDgS9gRbiFVT_QHwFZiZPO0IpG-YeV-0qWmCqGlo4-0V4NWIUl-AlHzsRk8fs2nLD1j60UygG1hXco2-6oP0lV_UjTZ5r5ZfGttKB8mudw1YZ-WWcqtUtH_9VPPEEqM0Ty52izVpTkUgA_wO0kBJP0Rb3-Mq9uPyNNOrwvepNTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvtO3LOf-ey7zuX8oyt6TTsNPMHSPhS7j0ryCGzS167avYU9_aQZE43YdsJs0vE3dQm92-uQpAaAFLeQLXtqYw8Tw-ZE0s6Yrq6gp8bUZhiZJ7F2_ZnBIK-tYj13C5bXeiyT3IKNvHtAx6u9sx1O2JMkinOX4QefxCl-g7tMrDWxGVwVYsBCn646ybrvliAPP-EA5wDvZe61pMQ6F-65svFNATzEt90qpCvmiTGyM4iL1KChGd4qIkK4iHaETNzRxfEOXLfFrqOffypKfep9i-C-FR4-m5axW164qMWJfjtcv6cQfHKfWvmAnEW0Gqk3vnrtqRJVUFz9tGPo8BLKwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266ca65797.mp4?token=YIfwKlGFZdCJSUCyFx4rUzhHnQ0eoEgWOZN4uIBvPWnHruEKVemQYR3msZDhIq17HMOBjXeQT1GDeq4qpT5FZOcYOetL4uXbOb-WQf6Qj6JSktJT5suQqOOLnK036IA3yu4eYEzZMqI9YrQ88nSXzZOZkwp02i7-MpfT_DTI5xpoqlvVZfVfSjQqeuaUR2Niv-oeTohfjSVBmXIwILvnsVUqtWARjQmDQoWhHJV8EyaH-AVnkVB6ac1vgiia6q1wMuA8MmDK9hn8IAZzc1WYnLSFV44cOtWsZtI6Doava_tJH8OP6llOv8doCIs-3t0ikuwZOEChn3D0CFwVJXOCfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266ca65797.mp4?token=YIfwKlGFZdCJSUCyFx4rUzhHnQ0eoEgWOZN4uIBvPWnHruEKVemQYR3msZDhIq17HMOBjXeQT1GDeq4qpT5FZOcYOetL4uXbOb-WQf6Qj6JSktJT5suQqOOLnK036IA3yu4eYEzZMqI9YrQ88nSXzZOZkwp02i7-MpfT_DTI5xpoqlvVZfVfSjQqeuaUR2Niv-oeTohfjSVBmXIwILvnsVUqtWARjQmDQoWhHJV8EyaH-AVnkVB6ac1vgiia6q1wMuA8MmDK9hn8IAZzc1WYnLSFV44cOtWsZtI6Doava_tJH8OP6llOv8doCIs-3t0ikuwZOEChn3D0CFwVJXOCfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقام انتقام!
بسیار به جاست که یادآوری کنم
اولین گروهی که رفت دنبال انتقام و خونخواهی
خامنه‌ای، گروه تروریستی حزب‌الله لبنان بود!
و پاسخ نتانیاهو چنان بود که جمهوری اسلامی برای نجات حزب‌الله و بیرون کشیدنش
از زیر دست و‌‌ پای اسرائیل،
به آب و آتش زد و  پایان جنگ در لبنان رو به عنوان شرط اول مذاکراتش با آمریکا عنوان کرد! در انتها هم بخش زیادی از خاک لبنان دست اسرائیل موند و یک میلیون شیعه حدود ۴ ماهه که آواره‌اند!!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5868">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClYufeb9wKFbF4T8LtD6rBgPNWzPVcYxpA4MlAL5jEMDA-FLsTyYzBVyKyd_5zyO5DBsPh_PhQsNJkIuacEIDT06nufAQG7vNto8CfzNPo5OEq6a6M7Ti9n49ksPIq4Tvf5_r5ipc31bk48cYwlvO0yUwugqKoFmEwpXRsO8END4AQTLsq2ro8Fp3NJxIKJMThUwGUWAnwKYBW5aTgcg9gSZSwwEmWn4p9LyVZ93dAy3Ml6kuH5VHJ-yxzQlc9jjDkLLDAcjpuq_775w0-q8x4EZLugElZ2kDZJE0rXX32QSMoZzBu9ouvqa5useApbqM76A2AYULgzCLgGgtmofYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه تروریست‌ها
الجزیره از دیروز شیون و زاری میکنه!
زمان جنگ هم، در حالی که جمهوری اسلامی به قطر موشک میزد،
الجزیره به سود آخوندهای جمهوری اسلامی گزارش میداد.
وجود جمهوری اسلامی سود هنگفتی به قطر میده.
قطر و ایران یک میدان مشترک گازی دارند، بزرگ‌ترین جهان.
۸۳ درصد درآمد قطر از همین میدانه!
راز ثروت و جایگاه قطر از همین میدانه.
سالی بیش از ۸۰ میلیارد دلار به جیب خاندان حاکم بر قطر واریز میشه. کشوری که جمعیتش (بومیانش) کمتر از ۳۰۰ هزار نفره. چیزی که باعث شدت قطر ثروتمندترین کشور جهان باشه بر اساس درآمد سرانه!
جمهوری اسلامی اما به خاطر تحریم‌ها قادر به صادرات گسترده و رقابت با قطر نیست!
تداوم جمهوری اسلامی، یعنی تضمین اینکه قطر همیشه بدون رقیب می‌تونه از این میدان برداشت کنه و درآمد هنگفت داشته باشه.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5867">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اگه توی یکی از کوچه خیابون‌های ایران
شنیدی  «خدا بیامرز» یا «خدا لعنتشون کنه»
حتی بدون اینکه اول
و آخر جمله رو هم شنیده باشی،
می‌دونی درباره کی دارند حرف میزنن!
و همین خودش خیلی چیزها رو
نشون میده.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoGGDnauTsXpitLjekDRcMBs1NKi37ofizs0UBvw1q0moC6-xZqhNVWgpoxFQfga5m-UnlYkE8gNeb-gc4XeV_uT6pLPlACohAF0MX6eRjBK2wroYFO8y_QN4JrMAw3KFwHGaxq9-ORwL52MP_6sIH28A-17d5TUbAGTb_Vx3ggIDfIzZLKKlkgYduM12l2Vh3QOqp49cHC2RrkxMysT4G1Z0IpsNLAebDWw3hrqXlLyl9p6rT-uUCc8rwP1No2ya1LWEEuOJFB7vv7aB5clWMtuSmeldZRd4ahwt_1xNVCZLdMc9RXmI9DpMcv_uZIqvjM_57leLxosaaplZw9Rxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51396b862.mp4?token=VweTnpf-7Dpkw63e2WkTzP4DNsDkR81Gc57SoLKz6051ffglmDfGpkTQ1PD1sA6DnahwclhRm3htDE2fv2AXGFuh0wB3Jo6d_2lba5ZAH-ek25uebjnCHIcCBhhkfXdgbhXpY4mWhZd8cVjRLdFSSrbg8YqTdpwzEjFI-wAFe2irCsSrgyTowJ_AeuGJe1aabJq_cwFVJdRN6SURPjJJknvV-ICV8neJRm44EA7w7wjPDVTvorJHvcn-ARFeQg_F20sTkS53HsRh8Jwndads9aJnSVz07fwbA27yWjjHk3yCcabkJLThnopd_36kJeEqqHHmQs73DrBxJBsgeiLQIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51396b862.mp4?token=VweTnpf-7Dpkw63e2WkTzP4DNsDkR81Gc57SoLKz6051ffglmDfGpkTQ1PD1sA6DnahwclhRm3htDE2fv2AXGFuh0wB3Jo6d_2lba5ZAH-ek25uebjnCHIcCBhhkfXdgbhXpY4mWhZd8cVjRLdFSSrbg8YqTdpwzEjFI-wAFe2irCsSrgyTowJ_AeuGJe1aabJq_cwFVJdRN6SURPjJJknvV-ICV8neJRm44EA7w7wjPDVTvorJHvcn-ARFeQg_F20sTkS53HsRh8Jwndads9aJnSVz07fwbA27yWjjHk3yCcabkJLThnopd_36kJeEqqHHmQs73DrBxJBsgeiLQIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک گروهی در جمهوری اسلامی نشسته بودن و برای هر هیئتی که برای ادای احترام می‌رفت، یک آیه خاص قرآن انتخاب کرده بودن!
یک تئاتر و شوی آخوندی!
مثلا برای گروه‌های تروریستی حماس و حزب‌الله این آیه‌ها بود که آفرین به شما! کارتون عالیه! ادامه بدید!
برای عربستان این بود که مسلمین دو گروه شدن، خوب‌هاشون (جمهوری اسلامی) مبارزه میکنن و بدهاش (عربستان) کافر شدن!
برای حسن خمینی هم یک صحنه‌آرایی کرده بودن و یه آیه‌ای بود که مثلا تو به اندازه کافی جهاد نکردی! (خامنه‌ای خیلی جهاد کرده بود!)  و….
ولی از اونجایی که این خودش نوه خمینیه و خودشون این درس‌ها و مکرها رو به بقیه یاد داده بودن، وسط خوندن آیه ، احترامش رو جمع کرد و با خودش برد!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5864">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=GgwycXy8dSHYxFg0_J_0dYRHx8SHOM0R-vTd2E9VWgyqTkacEPVihsSgEqmstgL48CTqqaWEZzmGVdQavHIKEScwG9uOhUV5L4fYgs8BJnG3kFQODN0du66qwH8lvUFpnqmox6bhjnlnwsTpuaz99Y540fNwwcm6SDuzqb_Vt0rvzbureujWxeWfx6yflIuqm2U1Fpzgny9Xd7znUymub5rB5Smj0k7RE4tk7BWcyGbZ6iTSRmmRfsUdEJeeVz5KBhySCOa9vUYzbc33hDfIX66JfRVzBhXHe0so0AYH_3h9sW6c1kHtrmLAtmzCNU6zepd8RHdBU2_foVmUw_ARbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=GgwycXy8dSHYxFg0_J_0dYRHx8SHOM0R-vTd2E9VWgyqTkacEPVihsSgEqmstgL48CTqqaWEZzmGVdQavHIKEScwG9uOhUV5L4fYgs8BJnG3kFQODN0du66qwH8lvUFpnqmox6bhjnlnwsTpuaz99Y540fNwwcm6SDuzqb_Vt0rvzbureujWxeWfx6yflIuqm2U1Fpzgny9Xd7znUymub5rB5Smj0k7RE4tk7BWcyGbZ6iTSRmmRfsUdEJeeVz5KBhySCOa9vUYzbc33hDfIX66JfRVzBhXHe0so0AYH_3h9sW6c1kHtrmLAtmzCNU6zepd8RHdBU2_foVmUw_ARbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با امن شدن اوضاع، سه پسر خامنه‌ای هم پس از ۱۲۰ روز غیبت دوباره ظهور کردن،
اون یکی‌شون همچنان در غیبته.
رافضی‌های جمهوری اسلامی اینقدر کینه‌توزن
که برای مراسم خامنه‌ای، ۳ رئیس جمهور قبلی
(احمدی‌نژاد، روحانی و خاتمی) رو هم
دعوت نکردن!!
بعد در میانه جنگ میگفتن «علاج در وطن است»! حتی برای خاکسپاری رهبرتون هم روسای جمهور خودتون رو هم حذف می‌کنید و راه نمیدید!! تا این اندازه تمامیت خواه و کینه‌توز!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5863">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=s3UZRX7a7TgznHKdfUbiNVcr-fBJPQAq0QySsXQcvHr9srRdhXCz7T4D7fZWU30BNJGNiLqqGbWNtRTpXB-A5S55t7in7mZZh5jogFZxMfHEwpQtGlkUlpZYlDfOIVFOQQZ8nJhQHqkHkTv7C6bgN-7iHFDygy9uot_2tee82MwMIPi7j24f1gvuiJXeMCB3oiXPelKubQNtW2a-3-jPsU3749Ova4CzSZgDDwCJdJUDJIyPzPwoYe4xzc2l54Y6el-NYpJHbXHNytCDrH79fq9J3OgBOs70gfdybz9OVbDp4RQnwn7QwaY-u-YMZ5A7RFVBuo84AyokDHKNhEJIiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=s3UZRX7a7TgznHKdfUbiNVcr-fBJPQAq0QySsXQcvHr9srRdhXCz7T4D7fZWU30BNJGNiLqqGbWNtRTpXB-A5S55t7in7mZZh5jogFZxMfHEwpQtGlkUlpZYlDfOIVFOQQZ8nJhQHqkHkTv7C6bgN-7iHFDygy9uot_2tee82MwMIPi7j24f1gvuiJXeMCB3oiXPelKubQNtW2a-3-jPsU3749Ova4CzSZgDDwCJdJUDJIyPzPwoYe4xzc2l54Y6el-NYpJHbXHNytCDrH79fq9J3OgBOs70gfdybz9OVbDp4RQnwn7QwaY-u-YMZ5A7RFVBuo84AyokDHKNhEJIiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۲۰ روز رفته بودن توی ۷۰ تا سوراخ قایم شده بودن
الان که می‌دونن همه جا امنه اومدن بیرون
میگن انتقام بگیریم!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqN-60uvUDxackBBW_9EyDf0qisn0NT-i-qmtHOsdz30ubC4SSXPCDO3ZXei3Kpx0AXTkfOxpu3I4orDnvYG-r0UaBOkTmvnGhurPTlvxMgSHqjaP55OwcuT880qfZlrAOPOJKctZyv-0MFLtbAF9D8sMaHOKuQIj7K5_Toc6gAIHdTunxzPhseLX0MdrcZ3bONtoPZmmWXhxBO0AP9rdWRGBBHrEFXs-iGaP38JrgIl6gyW6ZkMk_xEx3RIQs89yvQFTtE9KErq5WFiw8xoEsi6ouRQ3PIkv5Y7FQm4wqic1nP6bNp7Ri30-FwxXBsJnDlc9VSakJfWpjgtUFbiKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKiZe7WRTRMyCLBlk6PtVIBvOPL3sr8sa2Vy1JkOBODmgcai9w6rGHux4ztheshAuhyTvts3Z9abzNGgAKTWQWu3zoFa8LC5y_720balSc0EHdA5JtRxl3B_vFj9mPhcbtS9hGHyWsysNdM-Lipjqax8mZBTLnqxp7RdkNnxYRGxz2cj3KEjg5Q-pHjePguIboPZgJ3W62pchpqb7VMp3xxxqs0PU44WgBUv6DN8NBbKxEdGkadXf8iUVcYJ837NJdAN_o-BZLmoiLMJtKQ__Y07tbx-FcaL4ijLrw4mUjB5-Sm8j7WzXw1SthY0Z4yBK-Unu7I7BCx2f7jf1N1lNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری
حاکمان ایران، مربوط به «غازان خان»
حاکم مغولی ایران بود.
پدربزرگش «هلاکو» نوه چنگیز خان،
وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،
برای او مراسمی به رسم مغولی گرفتند
پنهانی و خصوصی،
حدود ۳۰  دختر  بسیار جوان ایرانی را بهترین لباس‌ها پوشاندند، جواهرات به آنها آویختند
و آنها را در کنار جسد هلاکوخان، زنده به گور کردند تا در جهان دیگر، در خدمت هلاکو باشند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=hK0kK2grIdkzG9Ak7DIPKO-8hQPjIQSGeelcOEMddu1uJyJ6_K-HEiSzenuWjjX9-PmN74r1EUgM-q-cg0hzZjRn2zafTg1jrqArcjs9alIUjTNtkPgFi-JWpVgn1GK_BhopQ3LQ-St2kyWjA_au0PWCAtu7G1XVTExzbQZhtEcMM8pW0Urei1IjZZ_eBgOptCAeWzt6a62a-fscFKjS4RYaikKn29cnMagvc7N1sqyrV2v42AG5yQX3pNVgJZ3ba1SZDRH1-sRf57tZ6ja2u_maXFpYH7mzvxu7HORom3G8wmmAywY9LHiyvZnqx-9nLgybZHXj0FGuAaw1bDn5cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=hK0kK2grIdkzG9Ak7DIPKO-8hQPjIQSGeelcOEMddu1uJyJ6_K-HEiSzenuWjjX9-PmN74r1EUgM-q-cg0hzZjRn2zafTg1jrqArcjs9alIUjTNtkPgFi-JWpVgn1GK_BhopQ3LQ-St2kyWjA_au0PWCAtu7G1XVTExzbQZhtEcMM8pW0Urei1IjZZ_eBgOptCAeWzt6a62a-fscFKjS4RYaikKn29cnMagvc7N1sqyrV2v42AG5yQX3pNVgJZ3ba1SZDRH1-sRf57tZ6ja2u_maXFpYH7mzvxu7HORom3G8wmmAywY9LHiyvZnqx-9nLgybZHXj0FGuAaw1bDn5cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها رو!
آقامون چقدر قشنگ رفت :)
چقدر دنیا رو زیر و رو کرد :)
در نحوه رفتن آقاتون، چشاتون قشنگ می‌بینه، ولی انصافا کار خودش نبود،
کار اسرائیل بود!
ولی بله همون زیر و رو شدن دنیا بود که
باعث شد که یه مدل قشنگی بره!
برکات رفتنش هم خیلی زیاد بود!
طوری که رهبر جانشینش ۱۲۰ روزه
که معلوم نیست  اصلا هست! نیست!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=sW3yyPXhfVn1NbK4V2pO68yRcyaTVCYPoi_Ypg7pI-5R6VEj76Vl0b3Zp_dygA2TVBtnHxq0pTKGhbAqbViyZjRY1hLF_cjLwjpPKvODEYAqeGitcU2pLjQhTHUQAsWgjWz3l5Kb8UL2YSrVn9Inxndh5-24l9A77CjHycythNvxhpyhwzZxxpFJ1uSU3A64aFKwBuFSolhcH2qKjUz6E12snehFWDudkQH53BEHi0DoER2NwscSdkk-mXHpWigL77YD3I4EJRdH9gKZfy6pjnk0tI_W49uTZSewyZ1gAT-v513yHvJQyrxET4TwgG7u4fjAIqk-JGX2zOwYHPdpFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=sW3yyPXhfVn1NbK4V2pO68yRcyaTVCYPoi_Ypg7pI-5R6VEj76Vl0b3Zp_dygA2TVBtnHxq0pTKGhbAqbViyZjRY1hLF_cjLwjpPKvODEYAqeGitcU2pLjQhTHUQAsWgjWz3l5Kb8UL2YSrVn9Inxndh5-24l9A77CjHycythNvxhpyhwzZxxpFJ1uSU3A64aFKwBuFSolhcH2qKjUz6E12snehFWDudkQH53BEHi0DoER2NwscSdkk-mXHpWigL77YD3I4EJRdH9gKZfy6pjnk0tI_W49uTZSewyZ1gAT-v513yHvJQyrxET4TwgG7u4fjAIqk-JGX2zOwYHPdpFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGdoGxmkx6vg9ypJoTpz9gooXY68hmFDQnzZ5G6g6exRtL8O2aUZc1ncAiUwc-4ImnsZV-a3p5-O6xcda7THf3R6IZYbAlmOGznYxv8TskhRD9cRcBpcinWFupiB34S_pXY9uY7padNZCnf4KnAXSPQ926mog6VdOW7nehZ1d1qasiOwjo3AcZ5S8MaY3Of0vzxT8q5Fx-H_z6hlJn4EbD-avLO10TW0IbQtK1QLswEl5_iYHRVP7w-OxKvy3seyBoux1eYF29FM5upPtKdbAN0JxKhU-Ep3iwxYu4WwqGkUh9R1Ee4fFYBW86zjjtDrSp8mzwiR4FJSQgv7UsMq1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Crt5gk0szPbh7nLteVr-v-u9-uRuRaGeelxShoBAQi4H_sThEujcewVSXYytwCJhO9NzDMBY1LNgK9Lurb5tLDzsJaFnRphAP0fmHGhMjQ9yEqwVtizNSkZdPNlCsAyO6MyNttaATRdOlu7noxzWSTn0ic0rG7ZGwabBweEYJcj9F1RpXsdcscs8jTwnQ07Oei1nB4u4pkDlXuxm5pmV3MrOGdSL-MTirUa4nuURUO2iXAa4CkEUjxHVELW_odCLHoQKIBUVrhhuQk5h_mEYvgWdX9SGDms7MwVjx0L_YCZLs-TsMa8AEPHvpCLcI-qsv6zU7k_GqwNfavVztq14ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6Oc44Fam8-lerpxRWutHFistaFe28TI9XPB7uD3KJN07uXhTSI1Ja-RJLUDQlWRlQFohtpZawlzkRHuLYzUgY6oEyHbbv3o8anFG1Xw-N-PncSwkbDb0byAEh-UG37zcu8X8mS9WJh1SwGjqzBCsqsgFTVWGus3-SCmBqiCOx3amYPN0qbKnP2tyIsbojIkfzCBjiRoBQhjCYZtLmWDLS11SEZG5ZBC0PlpFGrqWCLbn1FUQw9fdb8BqwPT5NUuj9bbWWEUz67uSTHKwXlbKFx3K-qM7jO0oNOFBJ80hEuup1oIaeAL0mYzOGRPeb2JAPM29VZ6MbVBHBRWfqbLQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeX_kFpbFeVr0o1roCJ7d_Dgbg3q9Iv0G_-Y3x19RZNsfhzReu3YAFAUtO6xe7rvJCNu6pwiFa90hSxFc1R1a1qXlQwGRggJ7w52N4VTEbhXr0gEAxp6drWzxUVciRnnEVI3ABeIh_09nLHFckvzQ_vzwpvczOue_50cl1czXDyzf7Qh1KVoEbhvqtZTltwiLZJgzZrNQ5mCtQ52Z9dBRu6A48jZL-B0GJcNcDbCYXw5VhGz5g9yFoA9l6KubO63vMIVAWH-au2OOZ1U9CfQE0vg0J23ZgwSNmGqhnBHLGZLwGmNYLgsMHQaFsqDY2jVKdv0YRDYnWne1xt18G5nEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5-8zlIMqmT3grOzHPfGMGTck4vUpIZ2Wzqi4cTyPlpXZoUW9ueSRKWgIF6UxKBtlwy2eVZi21h9J2YNPY8o5xpzpuEuU_K-Il24U91kXW-V3qRSlliimhVUf-sl56yKpzLCuwxEbI0d4CFGfcBhOMdrO9_efmZejhNwgF-99YWnHmGkyB0na-nes5J08j37L2gnlOab7VLB0ky_weTjIMHEOtmGdk4ijIkS3Fy7uEkZKBmkZw_2IZt_WHwXwbrDMIrUhckrMqpRpEwsLIjSKl3bLxVD0PDBY6H4a5q5gVtoat7UCr7ROblRlX5Y2mYp-CclbATRbjXFx_LMKILMpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان «معاون وزیر خارجه» فرستاد
اندونزی سفیرش در تهران رو!
ترکیه معاون وزیر خارجه و معاون رییس جمهور
دولت لبنان «هیچ نماینده‌ای»
در هیچ سطحی نفرستاد!
تشکیلات خودگردان [دولت] فلسطین «هیچ»!
امارات «هیچ»!
سوریه «هیچ»!
مصر «هیچ»!
تونس «هیچ»
کویت «هیچ»!
بحرین «هیچ»!
مراکش «هیچ»
اردن «هیچ»
لیبی «هیچ»
جیبوتی «هیچ»
سودان «هیچ»
ولی امر مسلمین جهان :)</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiJavhm8HzsPvZ3JXvqSdvvBx03SaU-X4KVyCCjY236bUnBB2FYRRJgVTrEkhDKPP2E0QMYShzjv7uso1pgLijoIKSAk1D6gbzs2-V6csZ9HqOMoXQ1zV_54Q2dRHKgyk35dvvJuJLC1q-zqzkodTNeoaz3q4NHMRMZY75rOgCWeLoGEFs3TesFimemF4osw0KfMN_dy9TE15YEMXK3PBFkisdpu9pQsDH_arpzDsny-Q7i9n6Bzs5tqKzp2csWMdjtibD7MkLeZbyRT-fZWfU3-r17XpgYSbk6ZVLuQ6mEDG_QMURSk8WpkfGzoE1PuJTScFTWEtCZ5JEDxwgARbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=jwbqf5PiTV0E-rlNoT_lzQcQpw_OcZMsCY7psL21RyvwNnkEGb203De_s8bGt6C9STyx4sO9rUAWCw7fvf3vuasRSp-SJjirofwF6RrUBxnDGZaKDkBU3VCXL-fK0YUkDn7h38OKigvrTGLm0cL-D3qcOWcVq-hLawVJLEqsmD5LEEhQcLfsBrER-ns8y3vE9QB8G3d7Sz_RDKRmgtUQ_FZkRmbB3Y6_SwjFZrtWVKOCgPFXcTnkCwl4F7e_mmQ3g6yAV30QqJfNizDVfvGsuaJgESNZmOE05Hi77g1uykpeFmwJ7hFjQPY2DLFKTk_IsI3SP95C1KYjjBnYlkbBDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=jwbqf5PiTV0E-rlNoT_lzQcQpw_OcZMsCY7psL21RyvwNnkEGb203De_s8bGt6C9STyx4sO9rUAWCw7fvf3vuasRSp-SJjirofwF6RrUBxnDGZaKDkBU3VCXL-fK0YUkDn7h38OKigvrTGLm0cL-D3qcOWcVq-hLawVJLEqsmD5LEEhQcLfsBrER-ns8y3vE9QB8G3d7Sz_RDKRmgtUQ_FZkRmbB3Y6_SwjFZrtWVKOCgPFXcTnkCwl4F7e_mmQ3g6yAV30QqJfNizDVfvGsuaJgESNZmOE05Hi77g1uykpeFmwJ7hFjQPY2DLFKTk_IsI3SP95C1KYjjBnYlkbBDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=QyyiCVRgrB-zEgFWs9jNMBzhDZDQuiC53oFN0sS3jnElUPRe283Ny6okFjTivEtwr2zzHg4alBJSQL_oKodgoCkn7N6ur9tH4vh5Z19A6jtp-ur8KmiBCtniMg9O9GT7U-ehBQqGKaLLRgLeWO6OG4PbUJV4kEMWsSSgABVZIiZdI-nWMglGtxeai1H9BfN4_x_iBAP4mRXVJDUYOCDS8QIzcKajZxaKz3hrD5CqcjTLup4wUaKGIt3fDRKCSDyzoJcmu-Kay-UZCY2FRS0Gb8vZfGYx0O8E0xHsut5wtFTKeK3p6A4KrfyfLtbPbclWQhEom9ITTCPzSOXDh5UL4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=QyyiCVRgrB-zEgFWs9jNMBzhDZDQuiC53oFN0sS3jnElUPRe283Ny6okFjTivEtwr2zzHg4alBJSQL_oKodgoCkn7N6ur9tH4vh5Z19A6jtp-ur8KmiBCtniMg9O9GT7U-ehBQqGKaLLRgLeWO6OG4PbUJV4kEMWsSSgABVZIiZdI-nWMglGtxeai1H9BfN4_x_iBAP4mRXVJDUYOCDS8QIzcKajZxaKz3hrD5CqcjTLup4wUaKGIt3fDRKCSDyzoJcmu-Kay-UZCY2FRS0Gb8vZfGYx0O8E0xHsut5wtFTKeK3p6A4KrfyfLtbPbclWQhEom9ITTCPzSOXDh5UL4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=XLSE5LpXC7zL-na1K8QY31i0vTjD3-kRGR0Xtvcseie_KenilVj0SR8LSRdOjwzqQNJWRzNuuQVlQZkvN1QlrTUYv0rX3CmpVe5m05TRn2CB5jYEwkUmZocGZTQ88v9O6qHigZa7Ey6JL1XG3VKj-UK6dYkMrYI3s5oVbGGvKmZl9O2IBRWwIaL6ixwAFUNAjiELtDQbto8-F0stTws30wl3YtgP27c0HX0rvcNkX30xc2_odt7uwHVAI1dkOmOGFawx6UqPVX4y0uhp3bnAO3Vdbv0aA1tFcWNSgVcpbufOT5PpgauIPMijmx6sFUyGG0x2E_Oqkku4avPiZ--6Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=XLSE5LpXC7zL-na1K8QY31i0vTjD3-kRGR0Xtvcseie_KenilVj0SR8LSRdOjwzqQNJWRzNuuQVlQZkvN1QlrTUYv0rX3CmpVe5m05TRn2CB5jYEwkUmZocGZTQ88v9O6qHigZa7Ey6JL1XG3VKj-UK6dYkMrYI3s5oVbGGvKmZl9O2IBRWwIaL6ixwAFUNAjiELtDQbto8-F0stTws30wl3YtgP27c0HX0rvcNkX30xc2_odt7uwHVAI1dkOmOGFawx6UqPVX4y0uhp3bnAO3Vdbv0aA1tFcWNSgVcpbufOT5PpgauIPMijmx6sFUyGG0x2E_Oqkku4avPiZ--6Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=aiJ_ow9-PGAyh8VRzripKSNOibSeAcBIw7Y7qrPYhpdhyq6IvDiL45snnochCuYD6p2XIf3s9xZr5Ji5QOsSPEj2y2wYdJZotq7x5SHnWVGurfHhNASqvmwTgqlxfeEZ5m-RwucsjRAuz7CXcp3thGR_Wo9IMTuH1WuM-GVh8lIXP0Oew7c_V_I6LCy-dnKPAMNE1F-oCe835B2vTSshFwNFBFht56Yzi5ByZfQ4ULs4VpC1qpKYoZCVyYKvd3QvF5oKLmV00q50riKdfI81RftZf9eI22LHF7EpUt8_GPfvd3eV4Wow4NjlLKfGU4qtHMMK7D6mHuC0Bawk20IKYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=aiJ_ow9-PGAyh8VRzripKSNOibSeAcBIw7Y7qrPYhpdhyq6IvDiL45snnochCuYD6p2XIf3s9xZr5Ji5QOsSPEj2y2wYdJZotq7x5SHnWVGurfHhNASqvmwTgqlxfeEZ5m-RwucsjRAuz7CXcp3thGR_Wo9IMTuH1WuM-GVh8lIXP0Oew7c_V_I6LCy-dnKPAMNE1F-oCe835B2vTSshFwNFBFht56Yzi5ByZfQ4ULs4VpC1qpKYoZCVyYKvd3QvF5oKLmV00q50riKdfI81RftZf9eI22LHF7EpUt8_GPfvd3eV4Wow4NjlLKfGU4qtHMMK7D6mHuC0Bawk20IKYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=FKfuM_43PZTpYacTB2TY04kVoui9aDqHvfkNC-h-PxmeiZ8mLf6au-rD70eYpJJQDktwnu7KOdXhWH9XpXkU8K7PdekmmHJ72QW5jcbwNl_ntyA4588CXHoZcYMguADfa1kWCJJgulfa6iJFCrEDA2oylFQq2oZakUqcyxB_iaPXPu35GNMg1qblYohU_Q7oNpOuBT-6zYkzJ_fEyhlmPq98TwRCcP9cZ9saILLQIrxNPgwMGZetxtcdC9UG6Fsl3k-6Ok-xWeRqj4uZp0uj73OIKNBTOPyxkmIIbPac_vqXWcaYcaVOjC5crFibOuS-oEhdZUvtuKNQO-4zTnMyjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=FKfuM_43PZTpYacTB2TY04kVoui9aDqHvfkNC-h-PxmeiZ8mLf6au-rD70eYpJJQDktwnu7KOdXhWH9XpXkU8K7PdekmmHJ72QW5jcbwNl_ntyA4588CXHoZcYMguADfa1kWCJJgulfa6iJFCrEDA2oylFQq2oZakUqcyxB_iaPXPu35GNMg1qblYohU_Q7oNpOuBT-6zYkzJ_fEyhlmPq98TwRCcP9cZ9saILLQIrxNPgwMGZetxtcdC9UG6Fsl3k-6Ok-xWeRqj4uZp0uj73OIKNBTOPyxkmIIbPac_vqXWcaYcaVOjC5crFibOuS-oEhdZUvtuKNQO-4zTnMyjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=qVpXTH4ObBLwzKH16Y95J_fJRhZhAp82Ep9wdIgcgLjbVyhmDhuHRNFQnaJW14qqkxeTdQ14b47HI3Btr-S0mSicjwkG5h9akuE3PASyQugvGFgmZc7gaYFTADKW5ITSEZoQIrh8AKDv5QZrYhJpbAsf8c3NXePauZUpDA7Mmpu1JuUeoXwiYvHC2cL8L4uaxWMLHBXJ9su40bek2aOeml9FzkdnDfmcilcF5QUxPMgLip0vc8Xwao7Yqw3pQ-xiukAztdO5LUzGt5CWPC_gpY3_wVKDrB0Jzhpv6cco9IXuqRq3kanykUQC2JwMQJermWlnljDJFDO64TwYfTKXOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=qVpXTH4ObBLwzKH16Y95J_fJRhZhAp82Ep9wdIgcgLjbVyhmDhuHRNFQnaJW14qqkxeTdQ14b47HI3Btr-S0mSicjwkG5h9akuE3PASyQugvGFgmZc7gaYFTADKW5ITSEZoQIrh8AKDv5QZrYhJpbAsf8c3NXePauZUpDA7Mmpu1JuUeoXwiYvHC2cL8L4uaxWMLHBXJ9su40bek2aOeml9FzkdnDfmcilcF5QUxPMgLip0vc8Xwao7Yqw3pQ-xiukAztdO5LUzGt5CWPC_gpY3_wVKDrB0Jzhpv6cco9IXuqRq3kanykUQC2JwMQJermWlnljDJFDO64TwYfTKXOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟
با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟
چون مبارزه آنها برای “ایران” نیست!
ایران اصلاً موضوع دعواشون نیست!
آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند
(دشمنی‌شون با اسرائیل هم فقط به خاطر اینه که مورد حمایت آمریکاست، و الا سال‌های اول تأسیس اسرائیل، شیفته اسرائیل بودن، شوروی خیلی زودتر از آمریکا، اسرائیل رو به رسمیت شناخت.)
شاه به درستی به اینها گفته بود: بی‌وطن!
خودشون هم میگن که مبارزه‌شون “جهانیه”!
“انترناسیونالیسم” (که بنی‌صدر میشد، “انترش” ماییم!)
به همین دلیله بهترین دوستان جمهوری اسلامی در جهان یا کمونیست‌های سابق هستن (مثل پوتین و چین و ونزوئلا و…)
یا کمونیست‌های فعلی: کوبا، کره شمالی و …</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIZnq4FhG1iI-9lzvRu1fvcGjFh_mzHm0lQPcXwc7t_jBYHs6tCi_ilHuBqyVm4PIWkrCSUXumQjqMDZQ-fSxAuO0RTNicZVSNzUlNPO9HZtwOvhbttA1_EXaqQXOiQ6pCr5TFJ7Tuvim7x9kCjCKiUO1cE2JzNuTMXCepsuRdWjZ7rukiiwfkklqVmSM0S34KRK7eYS7DxfXWnmczw2KjhhurUYNoZlHR7XTwsXUxc2xk4NFOeRk-E0jyCMxPNGFwmh6sDNOySk1cBz_Ce2tGrJIPjmIFMsKfRkNQBYYEWw1esISyexIPC_fvki7MMgyKSiGV95MtdnoULnARxEmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=dE3XAzHS_iYnn5Yz-XitPhvOAaezKaVnWD-cjWRWO8fkVNcopzRZuLhaq5OK2AoMzFZB6nFQYM2IbdcCPC15c-TgYMqvU0xo1-ce9mdvWwE2227mS4tvvfXfRoGq45l3Ud1XOsJiWGM9R_Us1l72F9358lQnQ3DwvgbUCmooRHAFnG7iDOfQxuv63SSHUG_4s1mu6uh8gRcHuwEOak_SGEbzqMCc_sSojcrLESMDi2-ua1E9hXha72Mpi9gYnxdmfjeSpyOy8YP_HW0lFmKKO2dTKnUSun1sOZFrEXk7oEumIAUFEbLFUscXRzvrPod12X4FWy-amhMxBT9YE6wPWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=dE3XAzHS_iYnn5Yz-XitPhvOAaezKaVnWD-cjWRWO8fkVNcopzRZuLhaq5OK2AoMzFZB6nFQYM2IbdcCPC15c-TgYMqvU0xo1-ce9mdvWwE2227mS4tvvfXfRoGq45l3Ud1XOsJiWGM9R_Us1l72F9358lQnQ3DwvgbUCmooRHAFnG7iDOfQxuv63SSHUG_4s1mu6uh8gRcHuwEOak_SGEbzqMCc_sSojcrLESMDi2-ua1E9hXha72Mpi9gYnxdmfjeSpyOy8YP_HW0lFmKKO2dTKnUSun1sOZFrEXk7oEumIAUFEbLFUscXRzvrPod12X4FWy-amhMxBT9YE6wPWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=CqnG_QXBg6w-4kj4ELNDRroODX4zINrQ2JiQ4734mXE3gqQLrYx7lfl6i_0nVBReyG6lZWnqhnlkFg87NuY8LDcr2bCRgED_furHBYhERsUp9wW-Q_ETzAIPcs7Pj9XRvd6eBmCA5tAGcykI6DCP1L_czTaJIQ8jiwag7Rtf1_upp_2EdN2S-ZhCdaXu0JMI9QUB3lbq3Jrcca7bKJYb8V5U_Zd7TwR3B46YRMR0vJwvUdxTIG3Ctg5NmaFGuk4toeiSW6ODk4rDC_MPb4JP33RqU_PezPSltWPXyqhbwrANZPTn5Q1YQeV6rjwvAh5_--1PB36XG5FyDyVw_SgRjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=CqnG_QXBg6w-4kj4ELNDRroODX4zINrQ2JiQ4734mXE3gqQLrYx7lfl6i_0nVBReyG6lZWnqhnlkFg87NuY8LDcr2bCRgED_furHBYhERsUp9wW-Q_ETzAIPcs7Pj9XRvd6eBmCA5tAGcykI6DCP1L_czTaJIQ8jiwag7Rtf1_upp_2EdN2S-ZhCdaXu0JMI9QUB3lbq3Jrcca7bKJYb8V5U_Zd7TwR3B46YRMR0vJwvUdxTIG3Ctg5NmaFGuk4toeiSW6ODk4rDC_MPb4JP33RqU_PezPSltWPXyqhbwrANZPTn5Q1YQeV6rjwvAh5_--1PB36XG5FyDyVw_SgRjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ۷ اکتبر ۱۰۰۰ روز گذشت.
گروه تروریستی حماس در یک حمله غافلگیر کننده در عرض فقط ۳-۴ ساعت دست به کشتار بیش از ۱۲۰۰ نفر زد
از جمله در حمله به شرکت کنندگان در فستیوال موسیقی رعیم، ۳۶۴ نفر را کشت و تعداد زیادی را زخمی کرد.
این حمله در سحرگاه انجام شد، قبل از طلوع آفتاب و در حالی که جوانان حاضر در جشنواره موسیقی خواب بودند.
آنها همچنین ‌۲۵۱ نفر را ربودند و با خود به غزه بردند.
با آنکه بارها اعلام شد که در برابر آزادی گروگان‌ها، اسرائیل حملاتش را متوقف می‌کند، اما حماس با عدم آزادی گروگان ها به مدت دو سال باعث طولانی شدن جنگ و ویرانی سراسر غزه و کشته شدن بیش از ۷۳ هزار تن شد.
فردای ۷ اکتبر، حزب‌الله لبنان نیز دست به حمله به شمال اسراییل زد که سپس به یک جنگ گسترده بین اسرائیل و حزب‌الله و حذف حسن نصرالله انجامید.
اسرائیل در این مدت نه تنها رهبران ارشد حماس و حزب الله که شخص خامنه‌ای و اعضای خانواده اش و بیش از ۴۰ تن از ارشد ترین مقامات نظامی و سیاسی ‌ج‌ا را نیز به قتل رساند و گفته می‌شود ابراهیم رئیسی، رئیس جمهور وقت ج‌ا نیز ترور شده است.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBIc077r_6Ao4j1_QCjyyKrViqbyPrK9mShzt_Qaowfo91jWQRS24kFRj-GhVctA8iWcPtFyAdZDxzP4BmMDzwT2u6YfU8DnU3b0dKYYW04qbkChxGASfV1b8ti2Pu1dkFdF-pIOKPyOOJZ5E7AMqxHpDabWoYOXgcZQaL3JZStB-kAUtzTrdewAYZfP40dov2DgF9DGtuY0ZNHA2YX1cxD55SgxfiRpARC8OamzEDZ-HKcr3CZ-bCLmJiqfaXn1LXDcvCXuKZ4VTxfHnUYG7Fw-XSVxnXOgHhkv6A1gaATx-7qI53jBMQlcgb8XAQdIVoErbguVQncpFLGsRKkWVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyN60yv8RsfUMEha7YtMN7QBt9bYuOJrQcES1Sy-Zmb0324SMVUT4BXpnxsUhE4F1qTAawjdXMks15lpi-N1S6gWe-GMBtYQEnSizQe9kgkmnsrNzP-nz_blan2XxQ4zlooyvRJglqwUKR33IRtr1WtGPM6puJUIMLDvwdH7H-H1u4tuGm08yUkO_JBtLo6_4pTkv8CJj846Y3vffAyCpeAH7tiIUXn3sBGuMPAhFp2P-_V8dDn7ipt2WByT5kk5-MLfBVJQpoFwTlRzsX59PY4bzRIcMv8RU5Gj2NZ7EHsY1_xtl49y0w_iyGpGRx3WoC3Rx0wNsFugOoMazEnAtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgk5H_L9OLMz01Ec8kGeo7IhOlnaA4mnVVIDj61w0tEzc-VkbvBOyYgisReLUV8Odo77PvK1mVVkti0vhLdee2cqX0ql5gIKKzMGXcESQR37ySEhRNCGlyv_cwWCVnzViZ6OS1RYxfYLnSwg3M7pv9EpnmNTVf2LKvVjJP7B04rO0GKyilz8kG5Lo8ZYivkxqyRtujZBvQLVPoVVfUpcjGdWspasPOgJvaDPjqwFeC9P8P9GCUk-yFlkz24RKfECnTussZA_Ys0aspP2JmTFHCQ3vHUhdtq3Tt3SpILJKbdi1z_aB3mX29VUe1UMqifKkcwKl_nrAdqSd3bNGFhgqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jywS1nWTfxh35b6idTUVK8wPeUEHsMI3ZIQgUZ3Ae1l6M68ayiQh6FB60EvO83xyayZoSQA400pMjvpCmo_gKZbTqodhxJEuRui_i6ruH-btu1Iu6DLURgTy3rbGrqrpCz8FPsHJx8gEBmu2qo1uiVLAX_8acs0oMAX1fVHUIKjjgguaRD49zMXB09wVOgYlZbRgNAaymo6gdNcL4kWcj4zzkNXiUiA4cfb7ugJz5Tx4Uimnk6s8U1Or3OdzYcbziGagYKke6zONCjpWrVUSXxzBrRqckqH3ENJU9BJfytMSXgOBArabycKQs-H6ckk2gZeyPxBaPhYIfqmY46nEWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9eQA5HTiOn3tcFZnnQPCwgA5OnCYNEQ6YMQv4zaKr2zr9SmfT6mIbK8E644KChTG5MyfLA0WOzX5U_EzDzzrhS4DVNDViNGGccQWMF5v26SAudgdLWzX_jfs3pIoLQdyF8xGkBJqBsW5sHCFmAMn16DSGRGw2BFJQCVVvxyAq9yWYKXskhlXmza6Zr0V7T42u2JkWOQ6UtbvZYtWjuvUYYjH16-fRGnfsa9DqQRqrBZu5DWuUjwqySjLv-j7t01ygJMmH8JpQqQ9ZfTjp-4LNsKpOqpZLSCbhxuFZaiIxkUFjuEfsTGDBOVotePaHnbmerZLR9zrlqXZELOUyBzYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqi08tQyQ8MpAjjGH5hxC4-CX0-yGr7BikXmz7NvHx10RV-JiY4Scp7a1zJTjAo_oezYsQ7Q-8pDd-01QLVEupcLVfVHZkoGIxVNyGxIKTAUAqB7GaRTUQQnSlgzkqeNGssURFUOZcoEyQQjOEFjbCMpX8Frez7z6n90bYyftAtTYDh9nMjHx-puHwBfke7ZpCkYAqpOJAZDmtbNUX25kRzLNeVDmoLC6jLucSABZr9AbFNLh6Tk1b8o13VwWngsrCdRMRMAVS0TPD6ja2V7ZM997cebjOKgd3uL82FWfLXhS28NNJKZyJvRxQw87nUe3QxvFCkZ0tjePTaxn29O7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DyF2iHesCq6kuExu1EZ3ailLtPI6URMvXr8y-GPoqrdZHTrVuDA19vTY9MEUyGeyaoR7MwZ3hvYxkWPj39C_1rNlVv59cj_MpHBbeAwhnaA5cvdhnx8OaV7YHDW0wRBaqd-ybyGsMPBmkMNHzi7kZipS2oDevDL43yJxB5FcdV-Ofv3MuGeZMKzWCwfdgBot5feYglk1QSXMQMfOrjmLR_MLtkZwXr8KseNDEsysHZbP0aEkmjmJxJCEPyQu3qXfG4P7OP4EXcOVgqSDjKCiQY-YtF28ayG5iiaGRd58cuKG0I4bRRreXgtFTeL2Q8HiIYYAJcBsArXHJ_xgQII5ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iunptb41vMb9XCPkVXxsDvH59qPunxEOhJLpdbP0kY_6yjniHBnugsl6ELGUeEQEzUaNhbmsS-Ltj86IveeaE7atc-xyPTPEYRX58bbmB8HXVctRAqUqY_1Hsr3-SxXXGOefYLBuzpqE29bNXq5hVlD6E_M49euLOTRNEoyHi5bXXDW0F6iiH98nATgT5Z9z1haIZT7oG5jqz2_EQpcCyUW6Un4viTHqXqr17UBpPvRqhE7X2MW9ZxfRhFizjJDUNnLiwLn5XyYb0GqeGpPC0t4-kSCouRpJug5GCPQDbtRhctFjU50O_NjOzP8aq7rZe7AOlsF4rEKBJM-FDAb55w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jezbQB_WqLQqF2-x25lbiJs5bOZUoXd3qJAs-jq70X1rH80spN2aQOhFVKw1LOzhXim8qsSLhrTFCPom6RgRbzQRxzSwG_No6EEXgckv5KUwMSu71UJb8CwCwHMv4uB1pBE0ovA5puWhFVuzCm86s8OEyw12PR8IZ1UaP_F-OeKiXp4ldf5bClO8X0cTu4FRhBCQ4g9eJfZY34MBtxlwunP3IbF0BOTWybFQPE37Ulzmzrju3LBsHhvZYWr-7L2EIymDNfTbAw4pttHrMMb8-Fem9U95ZQQtFb_oEI1M3X2MMsyJoTvA8YUQXGfkhl8i4KkhXYXeCv0l3UnoxAQ0Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NF3H3FummN3flH0uaOK5XiSGLKpdkJ2R2zptOzYpbeTUz4YjFuWoWzP2GVsr0AYwDGzT6VF8SgCAj7WEBSLkctcqh2s3t8GM5-zgpsmAyJ3-tVHQm1FKTvUSbseqgDzCRAerqROKLJHEXL14MaGOJGRK-aqWCWfJ3Bu-oRW7D7VJwE-hfPAdW0b5D6xba0-5Adkmf6lvHwIo32M6Y2nGgJO6bytdANE8lNH9qCtON1jR2SGyBCDIrRoDrWz1ruvmG9bjKGpl3TmRSku8ZnLr-61Uu_GQuU-G1HXJxRchR8hdKZ3oXAK30jeqOpw_3zRw3dn227WqMQxovqja7QmPWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BT-aPWNYqwDNDK7V6YTaT8pivITBcJUH3ZUwnk4WdhwtzOtJQeOQvOi32Qxko9iOsxzA2vP_mPNMT7gIOnb9UVw7jRbUkZqoL7TfMhHUMhntXw3Fc5sFzOCo21QxqKIlKEtuRoD7IG1LKluiqYeRBA_vcids-4XHKEhnmD6UclKn9U60uOWB8ZdDF4rmM1p-M8HUg6jAJdWNujQDaneAQ__xQf2FQzsag10uny8Nc10l0Bz3pLM2RpUGiSowgI7pdIqmFKxfZ-7sou6_yYjXnA4zEC9I596xav1uphoP_2XTMgG45_AzLZ6WDKg6rPGy1DsTyM6MwQS-Uy6XlwIPEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeENMIGvR81AG7m6Ovxx60baC2JoHQZ3v1qhmBFRsgRiKGDLd69-wbyjYlyhcoMz7J5rk2aIsQNhMfa0s2xLxJCHHDpZSGOWEtpSNKFx_kRlx-IMtpSjfxOtQ1t-hcMNZT5FhafWnRfBeSFGb7k29Bg_6SbZ5_itxi1ca7dwD2TjH5oS46Nl1l2P0B-WNGgyCacHQNbanYvhZt8uZoGo31xAlpRpB3nSyWuwvMDKHdjbQ0P63yYi55b1sz7fqgGe9WFW6GKvBqdYLDyvQVJ0Of7-eLhag7ko-HIitUzJCPVKsQw3r5aDjwtqHlaflyIKT7uh-QeVQYacUKZYC3xk5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد
به نام «روضه الشهدا»
توسط «حسین واعظ کاشفی»
این کتاب عملا مبدا روضه خوانی
و ذکر مصیبت در ایران شد.
و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)
برگرفته از همین کتابه!
حکومت صفویه خوندن این کتاب در همه مساجد و تکایا و….. گسترش داد.
بحث حدود ۴۰۰ سال پیشه.
(کتاب دو سال قبل از به قدرت رسیدن
شاه اسماعیل صفوی نوشته شده بود،
صفویه اون رو گسترش داد)</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=o7tJwUg8hgkUn6mxby_LHWVKTvOT5EkWotmvw9vL52oDOBpcWgjrTZRrfTggIHa2oIAOss3XN8X4xjccbrmCcB9ll4R22Cytnm0Xu_2nfANER23NG0oPMLh5k3r8cVXEyjXaHSZ3MYDNnQBVo10qOFxIn5YAWAEtDgF65dJATGGn7C0_FXMDRdWmaLBz3_3cLc29lQx6Ypyi5JwEhYobesyQJzubZH01LiD-Wr9rDUb5uh2dt8Y0LqlzskGNbgRc47QOnKtNfTfCDpINYKwwyDn1_BpYOWrPI6hK68LqCIHP_tOkYy5v7tgkS8rwOGniPoYqfb04L56g8HtFZI2w-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=o7tJwUg8hgkUn6mxby_LHWVKTvOT5EkWotmvw9vL52oDOBpcWgjrTZRrfTggIHa2oIAOss3XN8X4xjccbrmCcB9ll4R22Cytnm0Xu_2nfANER23NG0oPMLh5k3r8cVXEyjXaHSZ3MYDNnQBVo10qOFxIn5YAWAEtDgF65dJATGGn7C0_FXMDRdWmaLBz3_3cLc29lQx6Ypyi5JwEhYobesyQJzubZH01LiD-Wr9rDUb5uh2dt8Y0LqlzskGNbgRc47QOnKtNfTfCDpINYKwwyDn1_BpYOWrPI6hK68LqCIHP_tOkYy5v7tgkS8rwOGniPoYqfb04L56g8HtFZI2w-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=Ymx87HRj3yw6JBIJh8EoB-eMu3irP2TfS8VpPoFzvPdJDtGvD518wUCOUBhLoRQ0xYOyiJ-YqiNDs3F0BdxBqJKr1uVFchk97vvj6YyFAfzX6a2PCTA_RnAXAQs4BkFztXUNpQ1RmqB-Tinlc2Yok0jD1KokF0EkBqXYuIYZu4g-LjAnKG-ovLniBekVgH60s7IUyko0LqeBWRYHbGRimH0HYhDAxiIH0jNavd6X8ECQuusm8niF5iVS0eISRFk6YTuop-q9DcFLVno2DAyCgUAUqFhogJl7bMo_rsxJGNUxfZ1hSoMBvzKMbmmPz96s2kXECh0KQbHE5Ltr0ljThw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=Ymx87HRj3yw6JBIJh8EoB-eMu3irP2TfS8VpPoFzvPdJDtGvD518wUCOUBhLoRQ0xYOyiJ-YqiNDs3F0BdxBqJKr1uVFchk97vvj6YyFAfzX6a2PCTA_RnAXAQs4BkFztXUNpQ1RmqB-Tinlc2Yok0jD1KokF0EkBqXYuIYZu4g-LjAnKG-ovLniBekVgH60s7IUyko0LqeBWRYHbGRimH0HYhDAxiIH0jNavd6X8ECQuusm8niF5iVS0eISRFk6YTuop-q9DcFLVno2DAyCgUAUqFhogJl7bMo_rsxJGNUxfZ1hSoMBvzKMbmmPz96s2kXECh0KQbHE5Ltr0ljThw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=TYjyidM6u3mE0UMOnyC-euhjXBkAWzRrWFNzedp3gWwLaoS-DxMGcd0nJhRFNijfvXkOEpMX3X0_FsrKrI7RtENpezm9_LTiDYF3wXKS9aABVC5eg6kYq_JXSO7hE0Li2g-WbHpePy1G3mrvl9xtJzVkJS7Dfco04Jt6_LI5hX5r8IAJNSJ8Ap493rIGdGJstaiuiNX0jf_irwB6T4WNI2ilyKnmhlNQgENqy9dD3i-rTrWEFyVWHKk0dlu10srkQ4xuLJIogXT0vd5Tvb9lbskHnpVyKa_q3W7ym3LCBce1dsAM2iKxsl44xFLjN6w_J7T2IR2lg0iy0KrRBMt6jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=TYjyidM6u3mE0UMOnyC-euhjXBkAWzRrWFNzedp3gWwLaoS-DxMGcd0nJhRFNijfvXkOEpMX3X0_FsrKrI7RtENpezm9_LTiDYF3wXKS9aABVC5eg6kYq_JXSO7hE0Li2g-WbHpePy1G3mrvl9xtJzVkJS7Dfco04Jt6_LI5hX5r8IAJNSJ8Ap493rIGdGJstaiuiNX0jf_irwB6T4WNI2ilyKnmhlNQgENqy9dD3i-rTrWEFyVWHKk0dlu10srkQ4xuLJIogXT0vd5Tvb9lbskHnpVyKa_q3W7ym3LCBce1dsAM2iKxsl44xFLjN6w_J7T2IR2lg0iy0KrRBMt6jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=rgBC8qx6t7DA280X-S5uZNYp6czJO07ydVOX3bjYG8_iHmpJm0gDKjMA3jwoce9l_aODBRq-C1xGjvfyPGAzO8iEIl43oTOmhCgt17tc_VCp6tzlZDGTS-IlSymzYkPwVUYsp2T_6apQj2D8UY20gl3VxEy7Hnfgly5lV3b-UTzcu2V9XQEwofplCPzQbt43be5GuZUdCVsIXsGBT3nxi0Dcm6ywAnhwY_d6lFFTHpjsaGKHUXnZud9UQZkaL_jD_Eft-vLtWDquSHYRy5-zl8jHjUkSeTT0O3G6RcsQ71hA92TghaZHyI50HbE244V8-3-iAyDmEgJQLOyvnYfukg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=rgBC8qx6t7DA280X-S5uZNYp6czJO07ydVOX3bjYG8_iHmpJm0gDKjMA3jwoce9l_aODBRq-C1xGjvfyPGAzO8iEIl43oTOmhCgt17tc_VCp6tzlZDGTS-IlSymzYkPwVUYsp2T_6apQj2D8UY20gl3VxEy7Hnfgly5lV3b-UTzcu2V9XQEwofplCPzQbt43be5GuZUdCVsIXsGBT3nxi0Dcm6ywAnhwY_d6lFFTHpjsaGKHUXnZud9UQZkaL_jD_Eft-vLtWDquSHYRy5-zl8jHjUkSeTT0O3G6RcsQ71hA92TghaZHyI50HbE244V8-3-iAyDmEgJQLOyvnYfukg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=QomGZ_ZWbEXETI-fWKtFon0uXWaFdZqlpKOBNSwfaB0Y1RTl7ALchNkkyXoB0tlz8RfTdUg8eK5c9ndAJ_7O3IZ1kKq1KDqe6b5hzAEmjrFnzYQRQiBiFDmMFiit8OsJaaQcmqXT7zn-9lTceY_7_RYVdgnIXkL-1PACpSWUk6hb4Z3LjV4dussKlMYNtuH1ol9plIRkjk4jzTzA7odAemo1xFVpK9Wxxa38OTEIzm9Y3n9EY3uwNLxj8a4G5ruMmvvF1-hDB7I8JR5_QJ5-ceBaZnkDTV6qZoKfXA9oS--XGuaRZHJgTHNv59nDkietXWGmNylmER5yyJjb41RYUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=QomGZ_ZWbEXETI-fWKtFon0uXWaFdZqlpKOBNSwfaB0Y1RTl7ALchNkkyXoB0tlz8RfTdUg8eK5c9ndAJ_7O3IZ1kKq1KDqe6b5hzAEmjrFnzYQRQiBiFDmMFiit8OsJaaQcmqXT7zn-9lTceY_7_RYVdgnIXkL-1PACpSWUk6hb4Z3LjV4dussKlMYNtuH1ol9plIRkjk4jzTzA7odAemo1xFVpK9Wxxa38OTEIzm9Y3n9EY3uwNLxj8a4G5ruMmvvF1-hDB7I8JR5_QJ5-ceBaZnkDTV6qZoKfXA9oS--XGuaRZHJgTHNv59nDkietXWGmNylmER5yyJjb41RYUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=ro0ZABtFdqtzq-cl94zyDT4lfy8tLUi56-nqLyT62WS0QA53V0GOeDxZmQZ9akeVVHpJaBlcGMMDmM1MAnLQG0CvpOY8a2Cq3ypRWap5IvQN4BGRGifyRUu6SKWzIa3EsDeKQh8FjkPOfcgLKCXTwwLVGUirWFhd8Dckm_XrMyUXaaP8ei0-aLRu-Zc3W1CsOhxR-HHoJpAIKdPoalKKhvfXWxBlcd7UkOvwNPb62J0PTnrreheg4GNrrGwwlqP3AyoKdv47sKv48y6xgpjTOD4UwB1SliXG9TU8wjPPgMybTONMIqNe8scT9oVkRHgxt3YbC0D8bEq-L2-QtzOP5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=ro0ZABtFdqtzq-cl94zyDT4lfy8tLUi56-nqLyT62WS0QA53V0GOeDxZmQZ9akeVVHpJaBlcGMMDmM1MAnLQG0CvpOY8a2Cq3ypRWap5IvQN4BGRGifyRUu6SKWzIa3EsDeKQh8FjkPOfcgLKCXTwwLVGUirWFhd8Dckm_XrMyUXaaP8ei0-aLRu-Zc3W1CsOhxR-HHoJpAIKdPoalKKhvfXWxBlcd7UkOvwNPb62J0PTnrreheg4GNrrGwwlqP3AyoKdv47sKv48y6xgpjTOD4UwB1SliXG9TU8wjPPgMybTONMIqNe8scT9oVkRHgxt3YbC0D8bEq-L2-QtzOP5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=gn8df0dbxW1oEcHTKnsknY2KRYKDj5odt8a98oc81HgpNWET7w7tsmguOBbQlnCvzDmLO86SZ6UOabiCCo74glKSdWiWB8qkWjStP_PdYVxBAtlGzii8JEo3XiArJWUv46Y6VaEm4dJHj1pwLgJ9d7No7MJQB-7WtRUELZIwt6MG8Eodhk_P9Py2a7jkIRcNWRXd3E8BUmTXTo5JAedUu4rFXR2y8vYeFROQMTQZYPGKLlvgVy42jHfc5U-q6tzbhmwgR1MHpeKMEFKb0w9K84YKQQRKgFGPBW3ry9p9HT-7vLgt1nvRgWI9S6Fj4QjD0jkTi3o4fsko-ErkO-jDgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=gn8df0dbxW1oEcHTKnsknY2KRYKDj5odt8a98oc81HgpNWET7w7tsmguOBbQlnCvzDmLO86SZ6UOabiCCo74glKSdWiWB8qkWjStP_PdYVxBAtlGzii8JEo3XiArJWUv46Y6VaEm4dJHj1pwLgJ9d7No7MJQB-7WtRUELZIwt6MG8Eodhk_P9Py2a7jkIRcNWRXd3E8BUmTXTo5JAedUu4rFXR2y8vYeFROQMTQZYPGKLlvgVy42jHfc5U-q6tzbhmwgR1MHpeKMEFKb0w9K84YKQQRKgFGPBW3ry9p9HT-7vLgt1nvRgWI9S6Fj4QjD0jkTi3o4fsko-ErkO-jDgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7lI9-n2tkTmiTzMrSNsnxqj9N_wA17VWl4w7vMFVrRxyeE0_s3QvBdKzqNbbX7zbMwvUiA9X4a6uzCVapHxByMKG03s3VrcYZM4Nui0T82CwRCnJdgAYYy6bSYblrea9dg9JzopAIusUdRnVfi7ZosjbFqfJ_4QRxB7q4anJdnirBd_6QdN0rNCoK4vtwyP-XjRy8Qm2kiJ_RCCHCz7jSQl-Bxie1DXl-V8tngT_nLDcewCO4u6azN-ire5NY0UktP7I5PlXXjCY8j7Zv2NpKdnAsjvTcdodYn_1A4W6o8lv8WdoCv1JT7Go0I4tx4n5Wi-VucHeqauvyYnJ_gZsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=OcQLUlYVtpdoNHv5WfsrthalSPmKOEiU6Bp4bvXx2Er2NA7rXJ_2V4QiCL5J3JZoeSuHD7PkChkHVV_1R1nNrhNbEoRx1LewdvAVkK7RaLcYttZYEmZoxKR1xKe1SWAgPoZJsnpvQyczhnD8IVFPrkpBhzIuj0A3J1w8C5-I3iOZ7e-Ca0MmS7rZhOASO0IvTQN6FfzOCZFHuahsU7rmj-0iNJlSKTKOzQ1EE4-vPkK0pgXGOR0t1gbjnBf-h1tfy24zVasqqQpCKjkIFU2GpalTDl5V1tApo3jxRNaeNrhL7g-uKm5JTwsvBvCmgm5aLSr0Kd34-lBBqk-xUm2E6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=OcQLUlYVtpdoNHv5WfsrthalSPmKOEiU6Bp4bvXx2Er2NA7rXJ_2V4QiCL5J3JZoeSuHD7PkChkHVV_1R1nNrhNbEoRx1LewdvAVkK7RaLcYttZYEmZoxKR1xKe1SWAgPoZJsnpvQyczhnD8IVFPrkpBhzIuj0A3J1w8C5-I3iOZ7e-Ca0MmS7rZhOASO0IvTQN6FfzOCZFHuahsU7rmj-0iNJlSKTKOzQ1EE4-vPkK0pgXGOR0t1gbjnBf-h1tfy24zVasqqQpCKjkIFU2GpalTDl5V1tApo3jxRNaeNrhL7g-uKm5JTwsvBvCmgm5aLSr0Kd34-lBBqk-xUm2E6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=lrBt9LEWupP9I6uF8olQSeWOhWd7wkZaaJxO3CLUKnAW2hxFSom8AS6gNQMyaHp3rv9jrjbVhXd2xM7-jH9MQA9UzIZdSbFISz16Il6tbSOyYYT2ShvkuggRgab2THdb7EtDTceCOibf5c6NAu4E6kw3aMJghnGN8QIbIVPk7mlspk3qq668IWn2REnAXvYSSuEehCJcEUCL7Fhd4SXlqiblwStxgQLJBvWdmdbY5PlHE0I7QGne1MoBf8UWXt9xU-0zuBv4-YOe5n6oTZZ7sWsLH3mFRtnk17HK0DTBYV8sYbklG4cSDlWje5nbmm23SG4DDV0fqKBqesE1idGRNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=lrBt9LEWupP9I6uF8olQSeWOhWd7wkZaaJxO3CLUKnAW2hxFSom8AS6gNQMyaHp3rv9jrjbVhXd2xM7-jH9MQA9UzIZdSbFISz16Il6tbSOyYYT2ShvkuggRgab2THdb7EtDTceCOibf5c6NAu4E6kw3aMJghnGN8QIbIVPk7mlspk3qq668IWn2REnAXvYSSuEehCJcEUCL7Fhd4SXlqiblwStxgQLJBvWdmdbY5PlHE0I7QGne1MoBf8UWXt9xU-0zuBv4-YOe5n6oTZZ7sWsLH3mFRtnk17HK0DTBYV8sYbklG4cSDlWje5nbmm23SG4DDV0fqKBqesE1idGRNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=IQPmhV6SPh2l0LopLUwggPs-07jwCH42zPfbPJMbA7Z-BHhVzym5swZw4HvfTNGND0G-P1fEMxcKLOm6La3OyEN5891XT6WbRN-mhGPg2DvxOnPqRew7JU6g8EcIIanKMFilmUqbzV6YGFq57U6YgEIQQ-3R0Bw6xCRQjUxsVXV_Ji0peg1891QNNKvXqCsixfDVdik4lF1b0QTn_yuyln3VtDzFlrLAMMgTbLL-QqAEb6o08gVY-dObLJs-2tfpORPrpmCI_gzhEbqi4Y8HhJ4Gn5voKRm0IZX36tyxnD7Rt6ahukXa4HE4F8ty9hyUq10MaN-o5jtg3YjXp_LEWyGUFWlvQ2qYWGt-qpzS0vd5sJgI0NHT-zmdOtFKTPa8gLc6Ge1lUkqWw_3r02eVaveAwGIYveCPu-wDsI4HTNiIU3uQY3_v6SP0oZnTYCDw793q20O4RkoNTwkLVqisN56wRvSLK7Sp8f_hBGBSxvB2PgGpgmPThXuVT7rO6GQyYb3EIRq4NSjqGBINeDLDXdNNKQi3nRmYcck1D5crnBHG6ec16H8Y8KhTos6J1fyowQFnTzbvB_A2p4rtHeRNv1NTNOVMeixGArijZX9jHZKfU2PW8eVgE3dzhxiXDwzts0v_P1NvFn7762vpxRK70iD_6ZgzNlpAqM-3R2Pols0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=IQPmhV6SPh2l0LopLUwggPs-07jwCH42zPfbPJMbA7Z-BHhVzym5swZw4HvfTNGND0G-P1fEMxcKLOm6La3OyEN5891XT6WbRN-mhGPg2DvxOnPqRew7JU6g8EcIIanKMFilmUqbzV6YGFq57U6YgEIQQ-3R0Bw6xCRQjUxsVXV_Ji0peg1891QNNKvXqCsixfDVdik4lF1b0QTn_yuyln3VtDzFlrLAMMgTbLL-QqAEb6o08gVY-dObLJs-2tfpORPrpmCI_gzhEbqi4Y8HhJ4Gn5voKRm0IZX36tyxnD7Rt6ahukXa4HE4F8ty9hyUq10MaN-o5jtg3YjXp_LEWyGUFWlvQ2qYWGt-qpzS0vd5sJgI0NHT-zmdOtFKTPa8gLc6Ge1lUkqWw_3r02eVaveAwGIYveCPu-wDsI4HTNiIU3uQY3_v6SP0oZnTYCDw793q20O4RkoNTwkLVqisN56wRvSLK7Sp8f_hBGBSxvB2PgGpgmPThXuVT7rO6GQyYb3EIRq4NSjqGBINeDLDXdNNKQi3nRmYcck1D5crnBHG6ec16H8Y8KhTos6J1fyowQFnTzbvB_A2p4rtHeRNv1NTNOVMeixGArijZX9jHZKfU2PW8eVgE3dzhxiXDwzts0v_P1NvFn7762vpxRK70iD_6ZgzNlpAqM-3R2Pols0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=BStCjUvC-FrtwdDaF0K29-viG36qAZI2_WQncYe54vw-3AgjqQUlYEdYNdyDJp6RiioqR_r2aFV2ki_KoUY0V1pu4mBc77-vIN6_twVv4FeEQ-dErCy2X4Yg0FsWXOLda-bPtk1mYYJuMF5AnXYydqKCHYxB4fiOc2bHf_sqldSDCBhLvLJlHoxQEglNaSrddDzkrtifav9znp9KcD0MEUYTnK7j2UiOV54TVQvldPwdIiX0mfWxLGEd30JGHidG_Crl4cLuiVJsodBP3OXdMolYbEN6kS4jniHEWP87xTKxAU1v5RaxvsUCH6EMsQHJzqBExJBrFl6aCI-VYXybXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=BStCjUvC-FrtwdDaF0K29-viG36qAZI2_WQncYe54vw-3AgjqQUlYEdYNdyDJp6RiioqR_r2aFV2ki_KoUY0V1pu4mBc77-vIN6_twVv4FeEQ-dErCy2X4Yg0FsWXOLda-bPtk1mYYJuMF5AnXYydqKCHYxB4fiOc2bHf_sqldSDCBhLvLJlHoxQEglNaSrddDzkrtifav9znp9KcD0MEUYTnK7j2UiOV54TVQvldPwdIiX0mfWxLGEd30JGHidG_Crl4cLuiVJsodBP3OXdMolYbEN6kS4jniHEWP87xTKxAU1v5RaxvsUCH6EMsQHJzqBExJBrFl6aCI-VYXybXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه تروریستی حماس
در شهر رفح در نوار غزه یک تونل ساخته به طول ۱۶ کیلومتر!
تقریبا به طول خط دو متروی تهران!
که این تونل از طریق خونه‌ها و مدارس
به سطح زمین ارتباط دارند.
این یکی از تونل‌هاست!
خود گروه تروریستی حماس سال ۲۰۲۱ ادعا کرده بود که ۳۶۰ کیلومتر تونل ساخته!
این همه پول رو صرف ساخت تونل و موشک و
اسلحه و….. کردن که مثلا مبارزه کنن!
میارزه هم کردن و نابود شدن و ۷۰٪ خاکشون رو هم‌از دست دادن! می‌تونست صرف مدرسه و دانشگاه و بیمارستان و غذا بشه!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=vj9m7QKrvB_VhOK4wvp_PPPZMqcQs_yV6j_sp59Gq18u69h26K1T5BSYYTBaNMBxZ7NBTOu-IDaeEt89OKNtK7c_vRN2EBg4AfTdlgKrhY8Ub0tX90k-fM57vvnz8b7K_6ycd5UFagDUc59eTkGmnh0rUQfKA-jEP0kgKN2mTzg3HNCqU_ltxxKx_1K5QtFczGfmWEPuLJvDZVE15pL1LvO-t6_zihys69EN99xNQIHtNRHzGnuJS-LnMcuYMZR7UU6rlgDMMJCYLLBPBk1Ez079UhdQaQy7Z92jKue9hdjqoxmfcgZ3TFBjCzp4depDTfcuYVZDW4FLaWdMUIQGKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=vj9m7QKrvB_VhOK4wvp_PPPZMqcQs_yV6j_sp59Gq18u69h26K1T5BSYYTBaNMBxZ7NBTOu-IDaeEt89OKNtK7c_vRN2EBg4AfTdlgKrhY8Ub0tX90k-fM57vvnz8b7K_6ycd5UFagDUc59eTkGmnh0rUQfKA-jEP0kgKN2mTzg3HNCqU_ltxxKx_1K5QtFczGfmWEPuLJvDZVE15pL1LvO-t6_zihys69EN99xNQIHtNRHzGnuJS-LnMcuYMZR7UU6rlgDMMJCYLLBPBk1Ez079UhdQaQy7Z92jKue9hdjqoxmfcgZ3TFBjCzp4depDTfcuYVZDW4FLaWdMUIQGKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dmt4SiGYd0O8Mb5jwEPcMezrcfzrhjOqNnTA0sgn2P8NfuSsKp1cYqCmXh_Z1QtmqBH9DbOLi-pWO_z1nUrY_mpE3LRAQtqN29JieAInW92LKoO1ZjK1PZluk9AIM2u7XLCgH20lk8TyARjbvTXj4Ld8biYtD7yhyc3Ukqhgz8UIiU_w5TksrG2CH85gLb6tEnMwcZaiwmkwB6TPZCN7UTc1H-zY3R36M_qRGluK6ahfd-IgADyOK8skkYzHtkDyrFRZQ2LwedHkgtiYEsJxEbegY4JqZCnAKehjFFBCZ-iHFrD6cLTCAw3gCgVUEkhHRBwhIU9qB-sS70tCDBZrxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGBotHLHuDUz-fCH5rYswRjp_rvbnqBlrnt44yX6a-74_0HJKOi31L2vyxBwcgwvUhcysxw0FdqoYeZLq_p1OzpyFk_k8tRq3apBzf-hMvDCGHok-3Lj6jIT_h9ykfv4rPffhizdc7zdDWLc72iTz01cdRy-yPUJvCKGHZyLjv5G1IZzLytHQQrqAkUq3WxkTpKElWVWfmhJ2hiK4qALoRFKjFj6nW1vG2CtzRNUhrcw7uWf95Z5hqbtymeTeL6c3Jmn8H3OuPjLFf_9h-2lX8vfzs3Ws36Ewc8bO4FkS6TB2IEfOOqgnvPV-zdT0qVcqpwTOtedFNzww3qfjtrOhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=MTcig-VO_44XuNVlaboCZAi9d9ecijjoyB9BXXg6wtzEZ2EGaGu3OkgfwTy_7sZRG5Xmcu-EsQRO-ukvaNnzScngT6Vb9MoyEVkDhgCAhZjGXtE59Sz8PGqBrBiXyDL744ccuHTX6n_Zu0ZA3T9uf7twQA5glv1z2Uamkal0kET5E2VXF69c_H282NyBQ7LcXm05H6dxIQQnqLE0tiLEYiidwvsK9BnecWtp38rhhtjc_B_QhtqdWYUA9sGlav-lNPeyu9i6chJLkvH8v864_ZcXeOiOf_rBLG32HFsljpTJxWf7u-I3fydp4vlsWIlQrHm_UKUI7eHutD-hwQPsz4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=MTcig-VO_44XuNVlaboCZAi9d9ecijjoyB9BXXg6wtzEZ2EGaGu3OkgfwTy_7sZRG5Xmcu-EsQRO-ukvaNnzScngT6Vb9MoyEVkDhgCAhZjGXtE59Sz8PGqBrBiXyDL744ccuHTX6n_Zu0ZA3T9uf7twQA5glv1z2Uamkal0kET5E2VXF69c_H282NyBQ7LcXm05H6dxIQQnqLE0tiLEYiidwvsK9BnecWtp38rhhtjc_B_QhtqdWYUA9sGlav-lNPeyu9i6chJLkvH8v864_ZcXeOiOf_rBLG32HFsljpTJxWf7u-I3fydp4vlsWIlQrHm_UKUI7eHutD-hwQPsz4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkI_7bjv0zRFvaa8zCzPE4KiRHA-3yShwuLDUDLa8Tuee5EixmpCGAHy6WtQuR6nq9ZKPY9K5-HVlO0Cp1LfH8XxTxHMafxINacxqcr-Ztoo-vfSQG0PXiwyXJFXQkfO61lu8AlJ7bE1xpFFheGgsB7TfNsLGp9tfmqQwOuDzyWV1y32a0ZARFLls4RucXIoe0ifBN9TRhZfhKi_XrLdSmZXn-bCMyNxXW_eiiql5fA1I3VdduF5yrxAz36z3Qb61NqaXBgSD5ooMjXiVyyLSnPEidj4aoGK9JO62ZHyG5AUuFjhr8tZEn-5XYaA_wiYGBTRGwN7zodWYuoO7iei7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iDMVOyC7lE8JrwOAQaOGXTEf7cekW9GLBdw83xZt_5yHwri7OjkhTF14Youn6G8hprb0qAeNJrB8NvmlWAO8rhb-GnnL4ML50JaeDj6ou6s9bAlMp641sKldm2m-oMXqXeGv5DrXDAT45CDM5u8UhGCCrXGQGiWy0-pW1kJ_DqRxDqIObAO2epdC9T5C2WRZ8FyERnyUfZyRuksexaLryak5Y0Jk1UMRD6UOrQSBlCdJ6teaGhyUDp-hKSwhHZmtk271VV7S4877dufZ_i7zofwkziGsp-h4atLmdqJpIbaV1RwUqPxnpW7QFYyBG8L4i469V-hgTPx7RgLwbhmcKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UGXlSeLMJxCpmZHaBDw8-V5qVChFcG8KKiuYPntgbfIt1MuTPk8BJBaDmyePtIW_gR6iQB_GNEli5hv5S36zg4xiB0X08ylOyeDxgq-opN0TBg3AabVeTduP6SHCBYLOBXVNaqZ_NGQiK3kNXc0DXWqFtr-Q49OLFBWAClQdt3mjf_1Wb8mtjGx8iAd9BUOGyL_JW15cCT75EpKTO1uFJ3B7h3aAHEqcwMFw1-BNkO0HKIg0Xj4JjySfePzWG4meYUYfbwVU9D6qSGXLkqmWYuzNiHT9aVhmy3iCnBT3DpUy_Alyx3BFRo0ujsJntM3Ky5VyZcvMI6yRJunXnNX4oQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPzuUnB-Yx9fC_srQt0jXH78onKBUdDRbKY1hAvy3sPyIMHNL3IPWpAFZ-P2NVRWSu-0TUjASWIRiY8JRrlqZM7gyrUwy1jMKAxp7KWWLTRwoCxbPDG4V4hPDn_P7nVXNSXLUI64QoXk1h9jIT_fVBNJpCYKWHlH71PfgUnGTmSwr6pECWKPalCDyKPoaDfJXp5dC-6xN17OAOcXncYLqZ5J4sM_rhx-JusHMyGYfp1zjX_xuLjNojvFOCrfQ6CF2i7_Z_-CutpiIKpPuoA8IDh69YaeItbJbB0VhYwKVIDFwG0opidBbyn4MWOBsA5RAQTxQxawEOzMjiZ9iQvyKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=JNLXQW6JGqQ_Va0s9_OvxAbe8_yeBW6AQLywvzdRrvKmpT9gb76tfvUZMnnJ-i6XjXMJCJv4Nbs1TAMoLpZYJQW-LnPbm8Pz0D3p8bvhL5rg-_idfdLZMObB75GcuFJJhJda1qElbuEYEs9Yn4YdaOWsatRaUiRygOtRM7I_2borJ9zWRGtjiioC9r8Fvd6Ttm5l6ByqekI6MU0sDrm97p2pgaYucwJNz9yh4TjblMDcNc6APyVnNHKIYt4-QcuB3BhyoAyP32tz9TnSeUQFHa2Yt5OUjkz0mmsIHX3P1LriDBBWzm7tAREutaAR0VpShqa6Aj8ii5DMIKwubqeOWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=JNLXQW6JGqQ_Va0s9_OvxAbe8_yeBW6AQLywvzdRrvKmpT9gb76tfvUZMnnJ-i6XjXMJCJv4Nbs1TAMoLpZYJQW-LnPbm8Pz0D3p8bvhL5rg-_idfdLZMObB75GcuFJJhJda1qElbuEYEs9Yn4YdaOWsatRaUiRygOtRM7I_2borJ9zWRGtjiioC9r8Fvd6Ttm5l6ByqekI6MU0sDrm97p2pgaYucwJNz9yh4TjblMDcNc6APyVnNHKIYt4-QcuB3BhyoAyP32tz9TnSeUQFHa2Yt5OUjkz0mmsIHX3P1LriDBBWzm7tAREutaAR0VpShqa6Aj8ii5DMIKwubqeOWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=UGiBi7g948xh6d-dtqD0fXvOst--tdvCvQQUWr4eKonx6uLQHqKxdYWKHUnm4NDBkzOgAQ-PnkAHq3UwiY7eRVDSauM0-FBMHHuo4XDFrXliuoHeYTNW09U7sX2rRRkhWQrW8OP9teaIyKijvt0p1uIe9XBFnEc5_9tqeAud0a2QmR6nGbvLZsGTHmWBIyfAUvQm_1cE5vICq9lbmM3XINw_7sy_fIh9NwxztWEZjtOwlG-ZyCeQkZibqgIBAAsylKFzzppGDh5kxIo4tprzA8bl-LTmLWo_m23K7m2gfDCbh6j1R_9GaUiTXyIzJzIzigy17HMKpXSheGsbIT6Feg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=UGiBi7g948xh6d-dtqD0fXvOst--tdvCvQQUWr4eKonx6uLQHqKxdYWKHUnm4NDBkzOgAQ-PnkAHq3UwiY7eRVDSauM0-FBMHHuo4XDFrXliuoHeYTNW09U7sX2rRRkhWQrW8OP9teaIyKijvt0p1uIe9XBFnEc5_9tqeAud0a2QmR6nGbvLZsGTHmWBIyfAUvQm_1cE5vICq9lbmM3XINw_7sy_fIh9NwxztWEZjtOwlG-ZyCeQkZibqgIBAAsylKFzzppGDh5kxIo4tprzA8bl-LTmLWo_m23K7m2gfDCbh6j1R_9GaUiTXyIzJzIzigy17HMKpXSheGsbIT6Feg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiOU7fHY3ig_UGYxKbWbZXFBkaWoPBVmgOc64k7re6DsXoRQ2ZP8gFA4Wk8FjvHn_2ZH9eaovq54vJZ_vP-OP8ji5ID_aB8wYoVtktimrSQ90e8QA9CZ7uOYjEN5S4ifvo4GcoUAzSEQ8kUMrMVie4g9Of_p2xNePPWeJUAPAS-5Uh8n-umV1UpERardA_RooS4O41iWsQApOHtV821DQGSoqvyMEe__DzyrXaXsGIOTp-i-7E5Wq3rMqZDJMzLms0Nracx0nGNSpySVH3LNb5Qc4rztsXmumqfkycGFwnNFq1Qo8c31OThYEqeniN4lCayZdJqAgtTYUVaRiNzfUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=GyQcEFJFvQWLkvky2l7gyb8faumztKuds8X7Fe-OaSbbB7j08e88eiP4Fkc_g_DzA4rgm5pujGbtNi6TY_T6FPCzJTPsCZVpZSEiHNufG_gBvv6Wm1ARpRvO0Yp8U09JontwQje7VYu9lqlz50dc5SpYJqTtB54eemUrzi16FpQfdGeACz4xhU5yy2ft_iJYlu5ixXYraTuZ3FgC4Gn3uT_BQU_TMMdSdxbJIEkRRe1BLgP3BSxX8ATwA_Kd00c6tYS4nKUyFrx4fbNcszs2ox0UKLrjyGsw7FPHedBxgNC2Lt8tk37x_v3WtW0qboU4TaJgVG3xWbWLzwwaHIV5aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=GyQcEFJFvQWLkvky2l7gyb8faumztKuds8X7Fe-OaSbbB7j08e88eiP4Fkc_g_DzA4rgm5pujGbtNi6TY_T6FPCzJTPsCZVpZSEiHNufG_gBvv6Wm1ARpRvO0Yp8U09JontwQje7VYu9lqlz50dc5SpYJqTtB54eemUrzi16FpQfdGeACz4xhU5yy2ft_iJYlu5ixXYraTuZ3FgC4Gn3uT_BQU_TMMdSdxbJIEkRRe1BLgP3BSxX8ATwA_Kd00c6tYS4nKUyFrx4fbNcszs2ox0UKLrjyGsw7FPHedBxgNC2Lt8tk37x_v3WtW0qboU4TaJgVG3xWbWLzwwaHIV5aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=oGmSEFBX28735s7mm6AClmO-XalsP-Cpc5yRiLVhyG0Z_y6khVTnqm0ZboE9bqdpwB-AG3-jBdKHnNNQYEnons1aE1kCLzyasVHI_CjXSH7CeYOGMJNusEh0ynaku2RiIcoXbiGz1agG-Dxe4-EOeBWQ3kN5FtNVYPt0uSLK-607avoR6oKJqQudezSP97vBIZtb2VbH9GZTeL68-XctXrzstoNimOY-FIKSMI9qlga3pVoXeBEsCWtsjx6xzcBKmalSW08Xy4JkgnUTbhLGy84VEDDuodVsu_Of-3IOQ4XPY75QV2Xq3AIW5GDHtOAqOnUQvznzJ5JBsqv262EwMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=oGmSEFBX28735s7mm6AClmO-XalsP-Cpc5yRiLVhyG0Z_y6khVTnqm0ZboE9bqdpwB-AG3-jBdKHnNNQYEnons1aE1kCLzyasVHI_CjXSH7CeYOGMJNusEh0ynaku2RiIcoXbiGz1agG-Dxe4-EOeBWQ3kN5FtNVYPt0uSLK-607avoR6oKJqQudezSP97vBIZtb2VbH9GZTeL68-XctXrzstoNimOY-FIKSMI9qlga3pVoXeBEsCWtsjx6xzcBKmalSW08Xy4JkgnUTbhLGy84VEDDuodVsu_Of-3IOQ4XPY75QV2Xq3AIW5GDHtOAqOnUQvznzJ5JBsqv262EwMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=HTeEHtdj1NbsPpCDGgm-4RPVwp8SITlf0ZEsKxmZfVDhqFmva8krJmUPVuWe4EJudiowMobLTFn0WmyEb-gGDPpInjS3z-tKH1i3rUHl3vpTBy3tdyEOHwEd4hfK8hJ5CVZZJEZLE4_wI_lxI5xHDjPjVyVWsMZbVIQ4rOZHnLMy8Y74c0KKXXttxUWSb3dmuGGzyIxuNSfF9g1zBESCNUcSNL3YNP2QYU_SRE6kppGDML0xBz-A6Do-eFrT8JnL-kNzqHCoVg6hZSZyt4SQGyxJH0L5VAgNxTYJTu1MPHnlzY73iBnsi7ez3svK3rG31whkg6kRjaWih2-2wmaYTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=HTeEHtdj1NbsPpCDGgm-4RPVwp8SITlf0ZEsKxmZfVDhqFmva8krJmUPVuWe4EJudiowMobLTFn0WmyEb-gGDPpInjS3z-tKH1i3rUHl3vpTBy3tdyEOHwEd4hfK8hJ5CVZZJEZLE4_wI_lxI5xHDjPjVyVWsMZbVIQ4rOZHnLMy8Y74c0KKXXttxUWSb3dmuGGzyIxuNSfF9g1zBESCNUcSNL3YNP2QYU_SRE6kppGDML0xBz-A6Do-eFrT8JnL-kNzqHCoVg6hZSZyt4SQGyxJH0L5VAgNxTYJTu1MPHnlzY73iBnsi7ez3svK3rG31whkg6kRjaWih2-2wmaYTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afTCecoWo-b9hDVPK1Rk9prFPT4g5FgU9o-UK1GoXvQQJXvMhu5m8Pj_ckuuZxCwp4V7J6nQADn2bKH-Scvk8UEgXtgqUBDTmkKamlLhp9wrfOMDzEgL7ctAuNLn5GI0MA_RS9LpGaLPPshxH-sadrQmeoaTBdt_bqJ5pdgCoLwKsRdKwdyMZGLCLYmjswQtidVqdy0zIpAwF659x5cg-Yqv_dPrXegCmGbDK4AX2ibaToXa0C7qErKUHQHmsStqheHyaODqXIzfvmsrlew-5OPJ1ZDQA5k9B_khAFU6gNKXpmFCmSTLTMNlwYgig9MbCj6lx1FCXtwWAX3cY6UgCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=g-GsUR3LWgjuI-kl4RQjwwPOoICUECFZ7IoeR6SjXGoUVieWpssLoxl_xWjCvt7D8sllpBN_02-4Nh2XaevPjMqcQTDa3UAd2c1nr48Yp1fVOSuNRxpLdLU1p60tYMJpiO6s2P_PlNhiv-MRKw54ZB1axB2-OFG7MbuzPkp3WEsBX_zOWCOZ1fn9v_OQ-PciviIJ1FBp6K7XLQQ4r0qozUPy2XHHliapTmBs4YR5OAt-JRxL31lQcogFQFjVg4ci85c5af54lFYmWsGKD8QSK4P0x7fw42C3H3cxtMnoYS2_CDQ57V6UM867dWjOu9pa_-MOyH4EjCI5Qor1HmcZrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=g-GsUR3LWgjuI-kl4RQjwwPOoICUECFZ7IoeR6SjXGoUVieWpssLoxl_xWjCvt7D8sllpBN_02-4Nh2XaevPjMqcQTDa3UAd2c1nr48Yp1fVOSuNRxpLdLU1p60tYMJpiO6s2P_PlNhiv-MRKw54ZB1axB2-OFG7MbuzPkp3WEsBX_zOWCOZ1fn9v_OQ-PciviIJ1FBp6K7XLQQ4r0qozUPy2XHHliapTmBs4YR5OAt-JRxL31lQcogFQFjVg4ci85c5af54lFYmWsGKD8QSK4P0x7fw42C3H3cxtMnoYS2_CDQ57V6UM867dWjOu9pa_-MOyH4EjCI5Qor1HmcZrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTJMKJkLX8sp1QZ9229xBZssTsVbRAVHqplzkPZr0qpjREF_fBtWwZgpxWjoRSC0YaIh5XJu15dO1UXA4yJIDRaO9vOY9A4KOJZv_n-5XLuO-euebd7ynCgqPaNytQCbu-Rf2mtuEBF3c54Zuunum9IGkrLo6u9yLZboPxP7w53_E9hV5Y9xJNO0sz15BoyplQ-an284j3aZ1Vf8ckiYeUNBJFBeQSSMyxkSH7mzNamlqMnnfiDVeSPKaifKo5ZWTiqam43YWB6misiDQskSUi1VptQd2pvG8pYBbEuYm3kF1YHkeLB_vWOfW_Dc4GKERsdpzQEsAmYnldeecsW45Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPNqjSnZcFmbIOzWRJHjzjmiinlVwt8_Nq3WxynThg2RNd3PghZxlsGBQAXUSBv5FRj3K1-FP3zRFq1g3wc0Y31FK62ZHNjOf6n1_y8HPbqmmIVZPqvJN9bT6rpRJVwxK0-wnu84_rAO5vWWx1iRqHmpYtnGraG01j7ytvviCUiXC41JoN5cYPdHA14y9Dwtb3XH3t962t9uF7VqrYw2IcXWGccBdo66bWt2U2yFARIw2WfT-IOx41pP4eUAuRyKkZW7cKObrCHFJJdCA1Sq0GyJQzcOG8Mzor9PbOdi_DK2DnNQYdHFHCokzvkiIspVdl4OL2JWvpGuQX8WdNhLMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=ZeiVtYkAgpj97wR6-8-3YTpl_2xi_D3DPQNVoBgfGDv7nzE4p8xlftRuurtXSOW_Fs07J0onofQvrM1fI7sysrNTAe7UczxC7IJrPez3oFK-WSY0hN6EoiRkCcDhU41nib6NCDflqKr8fTLPh7CLj8rCDfjJcLnPld69Tp22zEzaPFoPUZCX16NH-YdNFZRFHoeZjsqsM0OXYkuCyioYOQpL_609YhEjWVLwaR659VNapUr6Qbv5ANWbhmLKK0n2dwSoagvpfT-cYN2WQmuFiX92wwdJ-Jm2uG9k_ic5wUmNcRd6PA1ZkNi0_bApz5T0QXLDZGP1MMAyTtAcWq5D5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=ZeiVtYkAgpj97wR6-8-3YTpl_2xi_D3DPQNVoBgfGDv7nzE4p8xlftRuurtXSOW_Fs07J0onofQvrM1fI7sysrNTAe7UczxC7IJrPez3oFK-WSY0hN6EoiRkCcDhU41nib6NCDflqKr8fTLPh7CLj8rCDfjJcLnPld69Tp22zEzaPFoPUZCX16NH-YdNFZRFHoeZjsqsM0OXYkuCyioYOQpL_609YhEjWVLwaR659VNapUr6Qbv5ANWbhmLKK0n2dwSoagvpfT-cYN2WQmuFiX92wwdJ-Jm2uG9k_ic5wUmNcRd6PA1ZkNi0_bApz5T0QXLDZGP1MMAyTtAcWq5D5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0mGMKJpaxAJjFzmI7glYCdzEaX56fKYrZuO4H5Tff0kwtOCUqDekM9wZXlEIKDVoqqmX_lodMElqEfJeaNwc99e5Spsjcq_M10xUA-HGDgKZE-nitzbsiPj7MD9iVu_CsJiLeVo7AjTHa1xYsPF4AhQcRyOIFdEBpviai49oam8iLVvPRDFQQdJQQpIivldisHvDTa5pzVJ7ttl_hx86gX9Yd0I1ZDcba4r5v53Ry6LQ_xcRlG3C6BQF--oUnvHGLydSZ8pyTSwgEAF-EcVB1YDnYigLTCCq-t-Rsv7igt-GZ6HfgZpSu8Wfz5xY9JzD57UQsMjEvCjIF_ZOq40wDCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0mGMKJpaxAJjFzmI7glYCdzEaX56fKYrZuO4H5Tff0kwtOCUqDekM9wZXlEIKDVoqqmX_lodMElqEfJeaNwc99e5Spsjcq_M10xUA-HGDgKZE-nitzbsiPj7MD9iVu_CsJiLeVo7AjTHa1xYsPF4AhQcRyOIFdEBpviai49oam8iLVvPRDFQQdJQQpIivldisHvDTa5pzVJ7ttl_hx86gX9Yd0I1ZDcba4r5v53Ry6LQ_xcRlG3C6BQF--oUnvHGLydSZ8pyTSwgEAF-EcVB1YDnYigLTCCq-t-Rsv7igt-GZ6HfgZpSu8Wfz5xY9JzD57UQsMjEvCjIF_ZOq40wDCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=fgkGyFsQHB5hwus89PMKv5YZsFFBtv2nDKfDqZY8lEhJVbRLW0TrIC4gJDkNoZY9B6SwmLt9zQThIk7drTF4RzZxXNvCzwpYIVYXNs5W_n8Kmsr3z9twQODNsUFtAo64Eh0xsp-c8c1fWcr9ToXShqY3rtP7T148ZyERze_WAYHn4Gks0HYVvnLVb4-2uNzNO1M62O0739xO-Lyr22Pm6mm3GP-bWj1RzfJkRcEb0fKQLZ3_m5v3w6mOjYMugVJI-saKOczQJ3tDLhKKmt8TDqWMbX3KSE5CR4Z_aIS4apClvqewRxMvM1IfsDZh9TZZpKrvOb-DCubHVi5_tk5Cpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=fgkGyFsQHB5hwus89PMKv5YZsFFBtv2nDKfDqZY8lEhJVbRLW0TrIC4gJDkNoZY9B6SwmLt9zQThIk7drTF4RzZxXNvCzwpYIVYXNs5W_n8Kmsr3z9twQODNsUFtAo64Eh0xsp-c8c1fWcr9ToXShqY3rtP7T148ZyERze_WAYHn4Gks0HYVvnLVb4-2uNzNO1M62O0739xO-Lyr22Pm6mm3GP-bWj1RzfJkRcEb0fKQLZ3_m5v3w6mOjYMugVJI-saKOczQJ3tDLhKKmt8TDqWMbX3KSE5CR4Z_aIS4apClvqewRxMvM1IfsDZh9TZZpKrvOb-DCubHVi5_tk5Cpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdR86ev7IamA_g5l2mNeUELtlRekSpJb5u4HZWsSs0gaXz-vSe4r8X33_nlDES5pd3rDiPk3TRQvvKd2D1q9B7KrETpzt0vpzJaCaWbpF_YTuGZ2cmKxdoVOBqef6e6gNJj1M0NDpssCIIC8M-Hcb1mXEB1OJBYM9daE3HCzOxfducBX38bwSA3h_n_JRRrhrXfzbyHpXGwheuIo4kL-4K3ykEbIrkWxmsJdVFIeqORPIQzB-civ5LB9Kqkj-fsjs8qr3qWPHORet7mH1CwkUjT469PdaE0yKjTZwI6qLbNHRvsoGMvjTCOMt9y5eqOKdGn8zWoPB8jQDH1fheVF4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=cGQTb9oNjweMdmUrT6kw5b3zqrcwShfmwxM_MAgNkCzhaqpIxMaotoZFGyNA4lYXK5m0khRvPemvL3iq9P87EaG7UAaomRRqjM6E8jTdpAVWAz0_xEMI4ALVJ29KPtGE7VgeTJiXIZL-Z_xXX1XpPr09QzzGrt7J12ZYKP2sTK87XgwYcHYfPwcli6o8ZoLs1psiuDwXWTeSXsbeQI6uJiQvKdqiDhl5kx5gboxLe00jTaXO7gxUCPFThh97zyWtzTyNdTIV1H_D0kx43LW6kAr0NySnj1jmSh5V-zUJuMCYfCzBJqNwQ976a_xqSmbCaccUw4v27YWWe8p4MNSeuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=cGQTb9oNjweMdmUrT6kw5b3zqrcwShfmwxM_MAgNkCzhaqpIxMaotoZFGyNA4lYXK5m0khRvPemvL3iq9P87EaG7UAaomRRqjM6E8jTdpAVWAz0_xEMI4ALVJ29KPtGE7VgeTJiXIZL-Z_xXX1XpPr09QzzGrt7J12ZYKP2sTK87XgwYcHYfPwcli6o8ZoLs1psiuDwXWTeSXsbeQI6uJiQvKdqiDhl5kx5gboxLe00jTaXO7gxUCPFThh97zyWtzTyNdTIV1H_D0kx43LW6kAr0NySnj1jmSh5V-zUJuMCYfCzBJqNwQ976a_xqSmbCaccUw4v27YWWe8p4MNSeuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=Z9T2Yr2EemmwaJZnKhyjc45mdmlEF6MmP9Nn3M-GEXYYBT2C5OFveH0PoQfkRMbGrf4ByBR3Wx-i5D55QPlB9zKXZ0PaA3vmhn2LuxPFPsTACa3xQxPJSWd4Bl8HC4Netg-ukwwYsPOq6zfSECN82SjKOoeenmOi5BMf-NoQ1jiQgwMO-r87faUZAtumokUL4OWTWGV-80gyQ_2d2l9l1Af3x4i9upmjp4zSCVz4FhnzKzJuomAsP_3tFD28otcEj7rFel2jD_QyUbff1PCYg523_elRfOLsNhKAvXz3HW014cih-GKcAI3DrhnkfIcY-pQUXeWToq_CbFC3gt3a1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=Z9T2Yr2EemmwaJZnKhyjc45mdmlEF6MmP9Nn3M-GEXYYBT2C5OFveH0PoQfkRMbGrf4ByBR3Wx-i5D55QPlB9zKXZ0PaA3vmhn2LuxPFPsTACa3xQxPJSWd4Bl8HC4Netg-ukwwYsPOq6zfSECN82SjKOoeenmOi5BMf-NoQ1jiQgwMO-r87faUZAtumokUL4OWTWGV-80gyQ_2d2l9l1Af3x4i9upmjp4zSCVz4FhnzKzJuomAsP_3tFD28otcEj7rFel2jD_QyUbff1PCYg523_elRfOLsNhKAvXz3HW014cih-GKcAI3DrhnkfIcY-pQUXeWToq_CbFC3gt3a1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=pcLD0FlD4RBWF8ShlNo_w8TXE5sS79bIqp2UHcJ52srPvE3Ish-717xqxjknmanjgfDG8lbFdFR_H53-Uv932ywubdtr4xL0Tgjs-Htru8TqZymui8nCjh3vgIvCSdwsLsc3WBZNk412M2T4xVaEpch9a7H6NV6f6i-eTT67fVvJPR4_p1zQKfwQi7wbFDoJIIGiAHgfJ1_g7bpsP9O8_ilHSLsEu4Yw2lDd6WfZhhiQL1Thgn_TA0PFdpUGemZ6a_FlqKItux9CcCY0HMJMmcwCsmhxgqvClSUKe2BWCEIbUQNn5mwODoj0cJszDFZMsoNkC4gJBTu7I8JqC1z9ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=pcLD0FlD4RBWF8ShlNo_w8TXE5sS79bIqp2UHcJ52srPvE3Ish-717xqxjknmanjgfDG8lbFdFR_H53-Uv932ywubdtr4xL0Tgjs-Htru8TqZymui8nCjh3vgIvCSdwsLsc3WBZNk412M2T4xVaEpch9a7H6NV6f6i-eTT67fVvJPR4_p1zQKfwQi7wbFDoJIIGiAHgfJ1_g7bpsP9O8_ilHSLsEu4Yw2lDd6WfZhhiQL1Thgn_TA0PFdpUGemZ6a_FlqKItux9CcCY0HMJMmcwCsmhxgqvClSUKe2BWCEIbUQNn5mwODoj0cJszDFZMsoNkC4gJBTu7I8JqC1z9ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=NSNi546MsuYJLLZEPq3mNlgb4mwtQD2zXHwPSkXKduPLIIMx5B0E6G-lVdmkHoZ7vo8lGYrsgYv0TJ0G3hUlc9cwGrSBeiqoe3iWJ9pmh0QgW_BOHcHTInCE2hKe22kopv8v_BQESYJNBbDRqVWFF6KNvlfv7KDmy-NACrpaoQ59rvuAoqf0EbO2qyjGyjFNjLumEyMQAlc-33BqXg9LIaEujOoFUrwBriUwkH8tM76j6HCtJVNCSVrHYAH9zsKoHn4ptsh5Yy2_Omeoh7eNLBViYhlSD1wY0sQ4fNe3jS0T_RrKOAzki6UOwEV_etcdKJlGq_fBZ28DMOjTrxrzJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=NSNi546MsuYJLLZEPq3mNlgb4mwtQD2zXHwPSkXKduPLIIMx5B0E6G-lVdmkHoZ7vo8lGYrsgYv0TJ0G3hUlc9cwGrSBeiqoe3iWJ9pmh0QgW_BOHcHTInCE2hKe22kopv8v_BQESYJNBbDRqVWFF6KNvlfv7KDmy-NACrpaoQ59rvuAoqf0EbO2qyjGyjFNjLumEyMQAlc-33BqXg9LIaEujOoFUrwBriUwkH8tM76j6HCtJVNCSVrHYAH9zsKoHn4ptsh5Yy2_Omeoh7eNLBViYhlSD1wY0sQ4fNe3jS0T_RrKOAzki6UOwEV_etcdKJlGq_fBZ28DMOjTrxrzJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsi7jjaY6LpLzaABw7zfQ0nvUUtyFf3mDkSPKhB67GsQzDBrDGw6khYg7FRNshRcyDb4wYFpD7aqr9Tk1UPFsHMMOR_4OSk5ck-whzr2cRg_iDo5EffkJTCul9q1H0KxJ1d5up1FbSTVPu9QbIDTk7G_57rHbyCRXC4uijGUyphyB2tT2JAHFN7f9pb6r8T1QwSFA8XSjotY9wdRFdlFNLSlN1CyKg8nVvPmjKYRy41FKuFjYOxJ3A747vJX7aq5voJKs1ct7SSK2ghXnkpeOeyBjD2HU5vd_HQ-W5Z4r6Is0lFQr7lOSgUFHYCMAVE4L44gWKtNkrFOpAVtFyCFNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نبیه بری» دبیر کل حزب امله
همون حزبی است که «موسی صدر»
در لبنان راه اندازی کرده،
همون حزبی که جمهوری اسلامی رفت دو شقه‌‌‌اش کرد
و از دلش، گروه تروریستی حزب‌الله رو ایجاد کرد و باعث یک جنگ حدود دو ساله بین شیعیان لبنان شد.
یعنی روی هم اسلحه کشیدن!
سوریه در زمان حافظ اسد حامی شیعیان امل شد، و جمهوری اسلامی حامی حزب‌الله لبنان.
سایه یکدیگر رو هم با تیر میزدن! برای سال‌های طولانی!
حزب امل، از زمان سقوط رژیم اسد یتیم شده.
جمهوری اسلامی ماهانه حدود ۵۰۰ هزار دلار به نبیه بری پول میده. میشه سالی حدود ۶ میلیون دلار، مه در برابر حدود یک میلیارد دلاری که به حزب الله میده تقریبا هیچه! اما همین ۶ میلیون دلار امورات نبیه بری رو میگذرونه، که در چنین روزهایی دهان باز کنه و به سود جمهوری اسلامی حرف بزنه! بعد از ۳۰ سال دشمنی!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=oRyfYaR_YJYiVAp5v4ZkZTe5N6-lLoJj5msSvMV5O9y91uHQsAV0j4iiR87tut44EeegYOSA-XkdoBlj_i7g4hu2z4O903yg8NDxhsPsm-RAF7m771Csw8x9KmcgHjIav05aSI3DHoDssenHn1DYGfsG6KSu0M7YMs2-m-J5YEeWAv3IzBXjgFxx57y4ZXASXjTynwQU6wjW9XLSkKuAVrtSIOxTc6Wzg3KxPhjEMS7ht8cTwkfVOWDi7M3juYw6yBHNQSF2h6rmcXj3D47NyIMkNBd5h-puPhtmcAU_raj32BSdk717sNRVRU-f0t14bt20qpzmD9oLKgcneajp9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=oRyfYaR_YJYiVAp5v4ZkZTe5N6-lLoJj5msSvMV5O9y91uHQsAV0j4iiR87tut44EeegYOSA-XkdoBlj_i7g4hu2z4O903yg8NDxhsPsm-RAF7m771Csw8x9KmcgHjIav05aSI3DHoDssenHn1DYGfsG6KSu0M7YMs2-m-J5YEeWAv3IzBXjgFxx57y4ZXASXjTynwQU6wjW9XLSkKuAVrtSIOxTc6Wzg3KxPhjEMS7ht8cTwkfVOWDi7M3juYw6yBHNQSF2h6rmcXj3D47NyIMkNBd5h-puPhtmcAU_raj32BSdk717sNRVRU-f0t14bt20qpzmD9oLKgcneajp9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=CUHdSzklZipIWFMfKgVyx24EXFXT989FMprPZtI7iZnzfdFlYm-xaDIlzVxwlFY8gjB84TON1rG0P5OPTP4MSx30VGjlX5xtf8EXMG4mBUZWZAWUuWu2w3scDkOpPQ4Kg2GuLg8rlUYDSYwt4Xusk-5JRrsUOPwltEuUlT3QEIo6x8YPqFpAEyxZMWIT8MptDiVE9yNgaJYfQRwxEw6mA0Q-LN68YeG8E6bXVj1DyS52i2-teSYVg6hB0Asraf21iByGR4ETFVkS9hcv6Sf89smL0eMiqlZSGLhXPUgbmtL7utmbfU_1aj2hR2jWB5YoTSTOrOqYJAawQPdDVFFIog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=CUHdSzklZipIWFMfKgVyx24EXFXT989FMprPZtI7iZnzfdFlYm-xaDIlzVxwlFY8gjB84TON1rG0P5OPTP4MSx30VGjlX5xtf8EXMG4mBUZWZAWUuWu2w3scDkOpPQ4Kg2GuLg8rlUYDSYwt4Xusk-5JRrsUOPwltEuUlT3QEIo6x8YPqFpAEyxZMWIT8MptDiVE9yNgaJYfQRwxEw6mA0Q-LN68YeG8E6bXVj1DyS52i2-teSYVg6hB0Asraf21iByGR4ETFVkS9hcv6Sf89smL0eMiqlZSGLhXPUgbmtL7utmbfU_1aj2hR2jWB5YoTSTOrOqYJAawQPdDVFFIog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SS5MdwYmiuURtjrhCDxniYaNGHbg4UhYy2cEX0GSIoytTkcJuczEBXDsUU4nFbLRIcYLqaUHvTPDplPkfwcb3iB5A5cm2pbCpnp1UTAC2jTJMrI6saspk_VFcCC-RhR6xoDOfl08c4JQrMXrDRNQ4udeSegL_iCXwp83NicBpQLelA9RklkNIDweev7v2N1aU4plGp0TE8cPzMO0nfIj0KH8YLtEvRAODU0JDttgsdkgq63pmhhzxNFUuZ0_nNQMHln4MV87Clz7U9FxwzVKUPt1y3HYNg2YsZ8g4B3Vo9TqWeREr_gBSRRaeYxJes9DGS4S4YVbye13fu19OzzndA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=sNB4CErNn1G5Eq8k2aHYLTQKaLelhq6VFDugLqdFbLLsLMk4TANgk3rghUT5SoriuhDZSHJMuSQJP_Bv9x8NEZ4bdwdYaXw4h9Ecn6D4n-eT0kfGMuUs5yCH28nx--GChbCvLq6eWdblgfS6IHXvK-5ZZr7kF6i47MxqsKZ8aZD0rLH8G14_MBaPSJo7H0sGFsyAa4kkJ7ldLjIi81RXooHUU-shhErmT7ab3BJfLXDQcJMDvOmrV2u3WXYo3tWsJ2XeNnl2t57hOpgnbqwqjKdYlaRXE03RcZBOgcVPdZrxfX4ucg483PfZN0w3FXlJNT0Gxe-k9mcxDNopwoufuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=sNB4CErNn1G5Eq8k2aHYLTQKaLelhq6VFDugLqdFbLLsLMk4TANgk3rghUT5SoriuhDZSHJMuSQJP_Bv9x8NEZ4bdwdYaXw4h9Ecn6D4n-eT0kfGMuUs5yCH28nx--GChbCvLq6eWdblgfS6IHXvK-5ZZr7kF6i47MxqsKZ8aZD0rLH8G14_MBaPSJo7H0sGFsyAa4kkJ7ldLjIi81RXooHUU-shhErmT7ab3BJfLXDQcJMDvOmrV2u3WXYo3tWsJ2XeNnl2t57hOpgnbqwqjKdYlaRXE03RcZBOgcVPdZrxfX4ucg483PfZN0w3FXlJNT0Gxe-k9mcxDNopwoufuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
