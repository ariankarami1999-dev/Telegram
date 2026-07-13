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
<p>@Futball180TV • 👥 584K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 17:39:15</div>
<hr>

<div class="tg-post" id="msg-99946">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6sNxZAJI1uZy5Nj4Y5YDylcBWTHYQqdJ1CJ7HuLIDyoXrPjJbDAKL5FMjaP4EMwU2ZQCFudDng01QHvq8CxI34uMM6PvRyWON7LglJApb85PwiWn0V0M4s68tz8VAP6d-eLli6CNUajnr-gl1G37_69Ga1JLnzORxW4CSsvOxdwHgRSbqBfdNRmvYPq0DNLXBQBNvXi6REcW2X6gIWvOJS6L5tIS0IPClTgTqSyzWXhgdOf3sGphTdoeqF9nXhpEzogzb5Ks-snBEcdU7r20zPQXeqtlQaqz1FI5Ij-aw9Lxx8h5QzNgOnUmex6pB7D-kpuz8_WpqV3J2qWA1jzTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#رسمیییییی
؛ قرارداد پائولو دیبالا با باشگاه رم به مدت‌یک فصل تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/Futball180TV/99946" target="_blank">📅 17:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99945">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLAi3uEGgNh2_LuGUfF7WyQt8df4PsFsLN5Mhfam4LUWi9At-s8BHt9C_TZN-tIAuRi0LKSpgRj6XM7L7wXt3ynsvpY6bFevLjBtal9n1ONSdyxLjrVKCE_ZFpIjvkNqi-KuYvchIeYCHO1pdNp5596FNpP7fy-HZGzwUJHpRW43YfyLSmK6AchrxyVnqzY6P70angz44fAw3mecwF-xustks1Zh43mqJX8ACbh7Kp1JE5zH7fe2vsNe88ZzeON7xaZwhLbSYlekMo27acp9Iai0WfyBQ_lsavXJ-GAK9tFhCL3WUpWRUlJzHSa0QgEaWHdvl_2OHnNVsCcV77P7kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو: لوکاس دینیه به پاریس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/Futball180TV/99945" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99944">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PncgdPLScyhH81lfXf-zbnqdIUDKlpL5p6BwMBLnyDDxRj8-IzSA63d0t8SK846CsUWJ0iC0NUngX1dllEkapoF-ZjZF5d4qIteUzHMi_QGCuXpYPf0l-6CqghQWKPOBRr_pE3zc_jW__FCnRmcTlkqc0PlUdYZRZ2bt_AVjEH3cPCBA2zjAhoJFien2BzVkMxVRpWGrI-cbhkwG-RqFdYROzeSaX44gr1bUUrItHE__kdBKJSuqC9q7grghbAVz4P29jreWDZctWAecwhodq88ism8Jtw4K5WmeVvv_PpGwSKU_oSbQ-NLMUhy7cesgLcINKIaBGd6x4i7kxQwdaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب احتمالی منچستریونایتد در فصل‌بعدی با توجه به بازیکنان فعلی‌اش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/99944" target="_blank">📅 17:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99943">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/as9Er5NVujF2avYEIwJnYZxLkuHlqeyVQTpQfKNr8C2inqDyMP7kQL3pVkpSj0n1CR27GKIBPf9zdJjNjLfhPHurUdDTXXI0UvRrxDvOcW2XGm1rSm0TflJX-rzQQQDjbZO_-m4EwZeMLokSBoU4OZjZ2deJWuQ4oHQTAPkmjdTYQLn8PAlCnsW_K9VX3aFYAxC78DgEsvcvf_7Fi8lPg9UeGt8wz4S6RKeqohWGRWTaRxPKouOSdkzO26E21ydHF26RXQTG2AICI1d2A44qDeDVjZrldqz42C-Ea4ePiz3cXgK6Y1IOt_Ab47FWr8-UHjMDfUAGjf1pHXjG1DGF0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو:
لوکاس دینیه به پاریس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/99943" target="_blank">📅 17:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99942">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d594556eb.mp4?token=n7LzaGqi2Z_17xye51obpOp4BcbywFClEwOw4LzJOWVyi-0jtfI9VLLAYMEjhnuJL1EW2cep0OoA7IY_v5Cv444fqDUeDLslKaZovkkm84FDh6ELcs-4zKf_xsNhM0WqrxUjjKEa_u_2SJ1sBSCjYDtH5SGBXwqyQ4vfw42Kr60WDOH4BjegNmM9M7LFp1kLYMDmFR0axXf864Vz0RlErfnnJFwR1rdpYxU1sdRTVuCd5TgPwyRITjwbYmGvWZ3R9Ls__WBETX3Zc4ZnnkSoOMwp74QqacBNM-J5BVJS4o3f6Tj8wt40cWWJn0hh5RU7qSo0P2MmLA5LNwnXX_TSNTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d594556eb.mp4?token=n7LzaGqi2Z_17xye51obpOp4BcbywFClEwOw4LzJOWVyi-0jtfI9VLLAYMEjhnuJL1EW2cep0OoA7IY_v5Cv444fqDUeDLslKaZovkkm84FDh6ELcs-4zKf_xsNhM0WqrxUjjKEa_u_2SJ1sBSCjYDtH5SGBXwqyQ4vfw42Kr60WDOH4BjegNmM9M7LFp1kLYMDmFR0axXf864Vz0RlErfnnJFwR1rdpYxU1sdRTVuCd5TgPwyRITjwbYmGvWZ3R9Ls__WBETX3Zc4ZnnkSoOMwp74QqacBNM-J5BVJS4o3f6Tj8wt40cWWJn0hh5RU7qSo0P2MmLA5LNwnXX_TSNTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🏆
هماهنگی‌جالب مسئولان برگزاری مسابقات جام‌جهانی قبل از آغاز هر بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/Futball180TV/99942" target="_blank">📅 17:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99941">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfVhuL4J4tv8xly37QISpmq0MaPN8XjAVDOXjEl64QVF1bL2SIQUlyXR8KWrl18t0vGI1FnSwuAHPoZ4MvFM_DVMNvdrBZDqnaiisgqzrZhyVetIagpRZ68ImKs2fkn01mCvfubFzFbJKX8ZatKdta6HzDCq4UO0xH7N1lKrUo1MfEssZf78kNcdCNa0Wu4GDyo2jFgZxjEixA6VWR6qhAeqndLp5h-9FPgNnlO-tXZcw2i3sBeBm_GH4MA0OA3EOnzGjGosMkUcP1xXFrbuzNYNWQs1hyP4kRmUuAzB82e_7e31d3-YF0EP8l12Jfkaqm4QMFULhJbCQpJFvIKH0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملکرد امباپه تو 2 جام جهانی اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/Futball180TV/99941" target="_blank">📅 16:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99940">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPSLxFIE3l2C0zy-Vbg7VTnOKZXhOBKwYEOqVHqRrKAK_9kYKpALCrAZxzQr1MSk87Yht6sT3lRkNC3P9gMj_fWQDJfnasHKi6oE06oFKeUIGXzQ43v5Q5m9PYNvakiPIjH4I5xIUI_ilHsnxUtsEQ7LOCad7rBsBuyYJAk8iQLxpqN02__TbOBoneA-aT8MdsOO9VYCEH3mzg4CE4mhbGEgEg2-qGSwJ0X9jmruQruIUZ8rrwc5vnY2hDNnenKgOZU9nVk2Og49dWWjHf7ce0adqc9cx2DAs7pyGOKqFJ_kVlcR9mVaID-gpvfVcTCXDT6eaqev-oKzxy2zwEeZQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بیشترین دقایق بازی بازیکنان هر باشگاه تا این لحظه در جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/99940" target="_blank">📅 16:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99939">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/99939" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">❌
با هر 1 میلیون شارژ ،
🅰️
🅰️
🅰️
هزارتومان شارژ اضافی بگیر
🅰️
بدون‌قیدو‌شرط
⚽️
تنها سایت مورد
#
تایید
ما
✅
اپ اختصاصی بدون فیلتر</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/Futball180TV/99939" target="_blank">📅 16:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99938">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1pzLui_xaZQY5_Nx4fry0TzUPhHfYKWg-hdVTQTW216---vP9zITokIgP-6_FRMxbp2zcmmktIeNRXmAe9zOXt1cGcI55MxvycjIAW8CkWNsrq5CkOwaM86vjE23qoI_tCAqUc83R9v0bjBbjr88U6UBCryLRujOnz5aMrGpAaKxoH-jBqnqQgz1_Oxe3geu2syv-IRxvv6xmeM8BJjf8Vqx6N8q74bk0y3QWY7XarkSVSSVr7splCTrgQu2PjzpB-iaLM1UbkXPRhu6rCRmguuaAkaC5EVZPZnzV-DIb8LBJByM8I1gNS8g-NsANqBN5JVUPegm9D3998QrszWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تنها سایتی که ریسک شرطبندی
🅰️
🅰️
🅰️
آورده پایین#بت_اینجا هست،بخاطر اینکه :
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی میده
+
🤩
🤩
🅰️
کش بک بابت هر باخت
🏅
بهترین فرصت سرمایه گذاری و چند برابر کردن سرمایه :
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r21
@betinjabet</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/Futball180TV/99938" target="_blank">📅 16:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99937">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef0fc183e.mp4?token=OwbUu9-zNHR1gTOO5yEKDE3C7zvXVkwM9RCb8PXiliE5xPPhER_4zbe4wkdhKeRqBHlTNoaaPzPs0Vj_bm_M126N_a723DAMJOK73D4LJtf9ny-OfGzZZk3kDT5MGHMs5Up8EL_BvwzHJ9JlDrPNrcXt__hmf2bmT5g5Bh5ci3WdY6G5jUjKbnXMYwnBkiafOujTxsKc6DBkGZJyxeCCJFNqEtMQkBanhUPIFyIoAxic-xZCKGnUVD5y5lR7Vnbe5-R5Dr4Sya7KIOsbtqrTIG2QgsvkKj2Qo7MowyQ-0aF4QOaKujYT78JW-tZqE5TfyVK1Z7cWJuAZLW0xR92L5Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef0fc183e.mp4?token=OwbUu9-zNHR1gTOO5yEKDE3C7zvXVkwM9RCb8PXiliE5xPPhER_4zbe4wkdhKeRqBHlTNoaaPzPs0Vj_bm_M126N_a723DAMJOK73D4LJtf9ny-OfGzZZk3kDT5MGHMs5Up8EL_BvwzHJ9JlDrPNrcXt__hmf2bmT5g5Bh5ci3WdY6G5jUjKbnXMYwnBkiafOujTxsKc6DBkGZJyxeCCJFNqEtMQkBanhUPIFyIoAxic-xZCKGnUVD5y5lR7Vnbe5-R5Dr4Sya7KIOsbtqrTIG2QgsvkKj2Qo7MowyQ-0aF4QOaKujYT78JW-tZqE5TfyVK1Z7cWJuAZLW0xR92L5Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
حمله بیرانوند به عادل فردوسی پور به خاطر اصلاح شایعه مجری صداوسبما. شایعه‌ای که درباره تعریف و تمجید ژوزه مورینیو از تیم ملی ایران دست‌به‌دست می‌شد، با توضیح و اصلاحیه عادل همراه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/Futball180TV/99937" target="_blank">📅 16:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99936">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
مصاحبه جدید املاکی: یک توافق داشتیم و آنها آن را نقض کردند. آنها توافقاتی که داشتیم را زیرپا گذاشتند بنابراین ما فقط قرار است به آنها به شدت حمله کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/99936" target="_blank">📅 16:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99934">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92cdfd4ea7.mp4?token=n4GC2kt3liL7VsZ0EsztDkLNWbJKv2U8LBEdm45LRslW6wE2e4nZ_bER1XIvxaFrNk-eZUvpUl0TgnPimf5UryFHbg4HwtXRmvNN0cONPOlifxQ_PGY4cvQwXHuTtNT57b3sDvqQfkJYHjHGYhghEkD29a8BPmu0d7Igy6SdnkgOW81IMl4dT0giBw6MvqnpLbuw1v5nI8fS7W_yTIB--j7vHAmaxflSMr3TiZdUcbrEdiP0ZYhcQPmD2oa0eORyf5Jr41WojSKNvrE0nJbEQI__xRzeWo4R-vIM9xqBgGVWrMFRq0NQUIfk0qZLGCPrwv9_ygWuv0Dc7TPsZXxc-h9UZ0mpBd_4ojKu4USioa0mO64oUGSVr6sZCA5cxbC4D9WAkLRGfIWXUmtFbqWpsKzTU7UvRrcOE-nzPeqwM2L0ibjeF6y2E5OyJAgLdlpH7tiXHiTgQ2RaN3gEs2BBLNNh7MmLOB0VQ6JL92lTSSDrfEykJ72r0e3TGH3-R3fqsZBzTVHVFRq4DunvCATk8YD3ZGgl0HO7igZOgCp66Fy-MJWsvLD-sxPTauHjQ1YNnMRHU0uGBivX1rNRT08tH4MI_6wX2d4U5UVKAf2y_JkNXP2HmzpZKlBQMXmsmlGQlCkkKoWCex7eGUFWVzlD1dXxkGcmntcOzsZX3FWCm5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92cdfd4ea7.mp4?token=n4GC2kt3liL7VsZ0EsztDkLNWbJKv2U8LBEdm45LRslW6wE2e4nZ_bER1XIvxaFrNk-eZUvpUl0TgnPimf5UryFHbg4HwtXRmvNN0cONPOlifxQ_PGY4cvQwXHuTtNT57b3sDvqQfkJYHjHGYhghEkD29a8BPmu0d7Igy6SdnkgOW81IMl4dT0giBw6MvqnpLbuw1v5nI8fS7W_yTIB--j7vHAmaxflSMr3TiZdUcbrEdiP0ZYhcQPmD2oa0eORyf5Jr41WojSKNvrE0nJbEQI__xRzeWo4R-vIM9xqBgGVWrMFRq0NQUIfk0qZLGCPrwv9_ygWuv0Dc7TPsZXxc-h9UZ0mpBd_4ojKu4USioa0mO64oUGSVr6sZCA5cxbC4D9WAkLRGfIWXUmtFbqWpsKzTU7UvRrcOE-nzPeqwM2L0ibjeF6y2E5OyJAgLdlpH7tiXHiTgQ2RaN3gEs2BBLNNh7MmLOB0VQ6JL92lTSSDrfEykJ72r0e3TGH3-R3fqsZBzTVHVFRq4DunvCATk8YD3ZGgl0HO7igZOgCp66Fy-MJWsvLD-sxPTauHjQ1YNnMRHU0uGBivX1rNRT08tH4MI_6wX2d4U5UVKAf2y_JkNXP2HmzpZKlBQMXmsmlGQlCkkKoWCex7eGUFWVzlD1dXxkGcmntcOzsZX3FWCm5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تقابل تاریخی انگلیس و آرژانتین چهل سال پس از بازی دو تیم در جام‌جهانی ۱۹۸۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/99934" target="_blank">📅 16:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99933">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MT3p8IiX3zMzJohaocdfM8POq0EJs-QYYNdE7NMkxmW1zEVyFnwBj0kBMd1iF_0PqeOhFA1EanDnbOYE6JJwWtUyoqYxH6KHOfKmpn3erXfMEYphDfWG6TAZMa7QeR7Sil8bKXEV7BUmX1BjTcuid1DBemIwXbNqX8lD1YfWQkVSYJQIa11lcS75QRIUlWSBDfsNWsQnUQOkwdtpnIi8dh2wZoq0KXF1j_RnfcpBr1lD4VDqgBDtMOslbkXOO8dqMXH1O_LgTP67wTe_VDeVaTKkctXKlBke3uKyqvx9TuDO1glegngoG6yGCRENPpzc12dRf_ooozn2mPjhxv4x4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: بزودی یوری تیلمانس به منچستریونایتد HERE WE GO SOON
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/99933" target="_blank">📅 15:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99932">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wn_yrDLVVLfRVvET2XqlqXhOopnVjrdMFjlRB2pvGosIUeEX9zLX-79Kjg-5hFD1HdP85ARwsA3FY9pBWSnmkgxZ387IPfu7qXfoRpxZvy75B7z6MSmfgNIfTVCX1LJq0sE0Z8Vmidz6bjBQTpUfaMWLWMuWAmBwhE0QIeZ4KqH5ZojCopkfKF_-5sLqZXzovCPJ_M-dMxje3Q5GYKuGCaObgm359hbWwH02y8I0_2YcxVnXXLy3yPwpsbgSaxeVs_-S3hAG1IR_-_ZzFUpnPgPCW2df3Pn5Y4uaIeHgRGw6nTV79wOmtr8TeJ9Rwbd7xyxfEuWCPifQjwFGkHkQ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عشق بارسایی ها تو تستهای پیش فصل این تیم شرکت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/99932" target="_blank">📅 15:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99931">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇫🇷
🇪🇸
تیزر جذاب از بازی اسپانیا
🆚
فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/99931" target="_blank">📅 15:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99930">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/155791f176.mp4?token=X3kIjuKnvGD1EDLluy872Vb5nL99gpZmVsnUjpmyRQURMe1D9haL7CiduEBB9EbXElfo3QHEuYpIYrpa30xDdF7rHBBTIxuVDOnKOCSame504bvXRUZm30d0gOSIHZDa35zjNaqHUx6DO0DYCiqQCXG6g2xUMGbynWiW-JNnakcKqycck9Zxqtv_K7v9A0pQXo2nzbdJ-j4xRRZ1-KVzLsggE0wFKIndz9uOqPo8EsaBeJLXSLrxwUYwnew1PSUmY5QUrkXSvAf3BmC5RzTnt4O12P8C5H66n7BEgCrVCNQ0zFaWDlamScB7sYceUlsc6pV4XE29KoVcv-cmgkchEL4txWyL0-rouu57Rnyhg760MLYXVkJ2Bz_YDA_pZIvGpnR3PkIQyFZTE2uMLwplq_1LyGwt7hZCc3ds4P1WFnIz6JKd9w1rclIWUBuJDheSwCJ8VxtdywtngitZ8vUM1b_3Po-ewFnWBJ9mqZh96fHxHwUjx_7Qmv38Y6w_juBTfiTSzqC2Eo074yJGkhQEzWqTj0mej88OjFCAlZG9y6LuvYRom3PJ2qUsUgJG320qKt8F8Tn8mv8IqEdz_lUbnA48qMsOWb3fYiFRixTmIt_z-1XGO-uFl7SSERR9H6zsSlM5K3H1KxApIMkG50km56Qs5nynEKvDTkZGUGxu1Xc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/155791f176.mp4?token=X3kIjuKnvGD1EDLluy872Vb5nL99gpZmVsnUjpmyRQURMe1D9haL7CiduEBB9EbXElfo3QHEuYpIYrpa30xDdF7rHBBTIxuVDOnKOCSame504bvXRUZm30d0gOSIHZDa35zjNaqHUx6DO0DYCiqQCXG6g2xUMGbynWiW-JNnakcKqycck9Zxqtv_K7v9A0pQXo2nzbdJ-j4xRRZ1-KVzLsggE0wFKIndz9uOqPo8EsaBeJLXSLrxwUYwnew1PSUmY5QUrkXSvAf3BmC5RzTnt4O12P8C5H66n7BEgCrVCNQ0zFaWDlamScB7sYceUlsc6pV4XE29KoVcv-cmgkchEL4txWyL0-rouu57Rnyhg760MLYXVkJ2Bz_YDA_pZIvGpnR3PkIQyFZTE2uMLwplq_1LyGwt7hZCc3ds4P1WFnIz6JKd9w1rclIWUBuJDheSwCJ8VxtdywtngitZ8vUM1b_3Po-ewFnWBJ9mqZh96fHxHwUjx_7Qmv38Y6w_juBTfiTSzqC2Eo074yJGkhQEzWqTj0mej88OjFCAlZG9y6LuvYRom3PJ2qUsUgJG320qKt8F8Tn8mv8IqEdz_lUbnA48qMsOWb3fYiFRixTmIt_z-1XGO-uFl7SSERR9H6zsSlM5K3H1KxApIMkG50km56Qs5nynEKvDTkZGUGxu1Xc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😆
امیرحسین رستمی
: در برنامه شوتبال من خیلی از مهمون‌ها رو نمی‌شناختم، به علی علیپور گفتم تو جوونی بپر سریع برام یه لیوان آب بیار خیلی از بازیکنان تیم ملی میومدن توپ رو نمیتونستن گل کنن ولی من گل میکردم اونجا رو کات میکردیم از اول میگرفتیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/99930" target="_blank">📅 15:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99929">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrLYaRZPo9T94UOBy3JmGxFtM-Hfh5T3Fmtw3g2YR1vRytq52w1-TVtHuWtTYVaNQB4RbNfRprjoQSfSg19v4RjsNiAfQiT1jdO8jWdBgl1UVgKe4wdJi_8NzUXnDUntNqAT30Rjx48Qf_gD9Br6p0lf2lpT8BXWmxstBRe4JXI3R4HNulahcs0D3W34ERbXcSDe9INNXXD4aExbEENFOvyufxhVh6ESaD4l23Qb426IH5WsHCz3dM1UzEjHwzAAg2EKU0ZDKxy1uYCOChEIhfsmYOaT8Ut6jI4E51ScPkBoql37EVDj92FzNT3Wh2YOKwK-__SnHc9vH5OtJWaD6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه رم قرارداد پائولو دیبالا را به مدت یک فصل دیگر تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/99929" target="_blank">📅 15:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99928">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/99928" target="_blank">📅 15:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99927">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/99927" target="_blank">📅 14:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99926">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/99926" target="_blank">📅 14:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99925">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99925" target="_blank">📅 14:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99923">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpFLp8xjrv-wiG8Oov_xDKoZNabLotV_Btpb8kKFThri54wibq2lkJ1xFDg_pF-vwyo3I5ynKTLu1DIH9_LeMtzBKfj20m3W6x0Ru7bnlkiJveEpolmlZf58gFzwfyuhRcVCamSprVrw1w5aa0oajARmw9GhyYEOngVImKlXa4xZECYdVwoqRA8DW8CeO9M1ccePw_GamSNkDIwHYgRQla5Zdzxxf411jPKsdI0UOh426gIdVzUuj6O1Kz8YnZlk4-ENML6B4Gong-R5ODmDEeJyIVtG1QWgw_FMUbycSTGY_ho-UQk5mKjVNiiizpiuwhH8FSrb98GZ0yOGf4DgwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DF8t1Lc0u-yDpi8fkIICDoumD5IvF8EbKZo9a0eTSb4Vrqr0e59OfWYqBgkAT0jxwXLyd-kIDsmuo8iPzse31CjvybHSjQUrPTY1UbNaMK8242ki9V2-4wMbP-EVbzwUYnpdjcIousFxJVLDT3x3Q90Bg1Tc_B5w1-iCdbfy-m9UTXFe8SOfFOLKIx52qi_Q02ETk7vmc-8QU9vCWbuDI-vO5Zvktven2G6m7nBCIDPeMmITmMMHDsfhEFa1-w2ZPsp9pCideWuVcjRb6uNeOq33gz7GGI43hbeVcE5tuJRUoi5rU_V0taTQOf-cLX1zEy_N6_rSVNZqpbp9_eBNDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏆
دو داور فرانسوی، تورپن و لتیکسیه، از ادامه قضاوت در جام‌جهانی کنار گذاشته شدند. دلیل این تصمیم حضور کشور فرانسه در نیمه‌نهایی است. این دو داور از شانس‌های اصلی قضاوت فینال جام‌جهانی بودند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99923" target="_blank">📅 13:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99922">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgRoCLaYsARDL_LhEtIsO93xtjwUo_QJ5anYlXscxwvfCHq7Gp2M71zBytmuVEXb5By0-mzf2L06Veswb71IRZZn2stV_5Q-B9s3sufzhlDepeR7S0RF-JhTteEge2n1Nn31f961NOI7p0AaNYbuqLLzq_RfGBiD-qUqpNRVcLhwCITPcXMPk1QdHxUJfT_iKD7fS3qAgqGGDxWk1R4yGN1sgVPXfhvjmYLWZktRjlVImny8zHITHRZZfMHf7d5UWhVuiiCv5LlvZ_KvwKcOMwlGIBLmMsHHzo_InKfm0RdSdfEbQS917q79JAO4qK6X7xlsOh7gNBKqLq2crLyScQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: بزودی یوری تیلمانس به منچستریونایتد HERE WE GO SOON
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/99922" target="_blank">📅 13:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99921">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/99921" target="_blank">📅 13:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99920">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scbTP5wsLTJGDa53mvf8WEBqSyjLqV9gitqEvh3kL7rlnVyJTr5-O36PMka6fkJPA4ZcGbu6xN7mxHSQ-WLk14kkfPCv9ZCVEwXjoNgppjKayz_4Fk9paEJSm9RX-HTqFzaNgWEvDdORVu7klvXfiaaZJxOaUGHXN9xdI-6qflGh8mSAIhM1ses04UwHYj29Jzf_L3g6WBK7oB4qZMv4LLAGiFh6bPYitFXZLttkv3xmro76ScuuUtri4tS345SUm-1go9AzgFEc3VBJIcUHTCK1keg9pK7SEfXbwpyE8pcK_Z0Jehj8ovR3O0V2li7nyAd6psNp74AZyi1yo_-LYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری دیوید اورنشتین: باشگاه منچستریونایتد درحال مذاکره جدی با استون‌ویلا برای جذب یوری تیلمانس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/99920" target="_blank">📅 13:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99919">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
دیوید اورنشتین: باشگاه منچستریونایتد درحال مذاکره جدی با استون‌ویلا برای جذب یوری تیلمانس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/99919" target="_blank">📅 13:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99918">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99918" target="_blank">📅 13:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99917">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/99917" target="_blank">📅 13:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99916">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E35c1MilQwzBq7K4IkdOYh6ZNibXP6a0PVf77Zu_2C1HZUc9zYMtX59ayAt_R7eGKqOESvjU3i-tSl_tjD8HL1NiZD9UImxvCnqEzv1X-jIA3qdoVl2hqE1y4_VJBOW-JoiSy5xIGfe4t-CPZOHUKlKowbKLpn9XCeHggqN8KcXY_H3R_sj8jxtPIi_lND7xH6pGZcPjWFGhLdTeUtMdDe01U3xkgusddffN0nlCwEJWvGSt-eV-kVRfUxYGvqNYQCr5LY5-fjzPTs68FJzPX5vlNSGZOneBdlzjhopAq9wtSAVRT8BsrWkXpnXUFEu7CMUbKf98ZJnA8tK3ZoRDfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوری از رومانو: رئال‌مادرید درحال مذاکره برای تمدید قرارداد یک بازیکن بسیار مهم و حیاتی است که این بازیکن وینیسیوس و شوامنی نیستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99916" target="_blank">📅 12:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99914">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/99914" target="_blank">📅 12:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99913">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/99913" target="_blank">📅 12:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99912">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
❌
🔴
مدیریت بانک‌شهر بدنبال ایجاد تغییراتی در بدنه مدیریتی باشگاه پرسپولیس است و اگر اتفاق خاصی رخ ندهد احتمالا پیمان حدادی بزودی از مدیرعاملی سرخپوشان جدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/99912" target="_blank">📅 12:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99911">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYq0C2JJLZbhl6nAdRV9AuMc7iRCxqv4FMVhG-gHqamd2k1egnGg0_L92xlLLFZ5EwE4sISxuNgFLDV7ztee041D3k7nxnYVUCsX_nzdsvEE0GWpcVLjncnTqPqlbRW3_dc9N4VU6Q1tExCrrMRyyIbtngTEScyLZGUKH1p0fQrSkBS1zFIYgnNPN0FnbZ4e4IVhttNRh4ObZug9pE3DGfClYI1nTdT4h_oSmazFW04HJwz-lavZpT3-F8GJdwfn9F-eMRBz9kaMTTuMgNd9LY2hMJrPAX_sJipnAglE53aRfi5V2epyFOTF2TPKbrNfc4WJVswK5KnlpHB1Z3P7sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
👀
مسیر جدید فن‌های کریستیانو رونالدو :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99911" target="_blank">📅 12:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99910">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOlBIXjDHxngUmz-Usv_aKtBao7MlmpwOzC4PmIu4C_DoT1Pt7hUl1hKDrXrkMaGb_oZrUAEVSHrsbXOKJayt0KiTOknkC7knJUQQaK95aaoty2kGLpf5utSPoawnwNfSaF5YVhi3FuwyIIhgDIjoxgHbRPmUGGVQ_b8C7wmAEz6F5HhOt3FAFW1o3c3EeHq5O3Bm9TOh4C3-dKIm1eas-vHia4mLB86IKp-ykxL6HtMn0Pryk6_EGpA53EbY3eRVk_RSc-FABQkr8pzPf0hDtuBik2LcleDFbqw79ePivPBm228mE2rcsvn8nVB9WLsxKppK0lx43-SDqt_gTO58g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🎙
ژوزه‌مورینیو:
«من سال 2003 شروع به کسب جام‌ها کردم و آخرین جامم را در سال 2022 به دست آوردم. این یعنی 20 سال افتخار و قهرمانی. به همین دلیل است که می‌خواهید داستان من را بشنوید. همانطور که می‌دانید، فیلم‌های مستند درباره افرادی ساخته نمی‌شوند که هیچ دستاوردی نداشته باشند.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99910" target="_blank">📅 11:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99908">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/99908" target="_blank">📅 11:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99907">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNeQVsFCGTE_IOaTJPe8BRgp9lD0iv5Vzm78rbLPPpnXCYvIBT4OVyI6vgbDec1OaBu194VrgXTKsqlMtLmf1ZVEr1Jd_2-ecfiRgSPYWEizNmLeOfaeRfUQNtOgDwDL7rR6K28qAK30s993UJGIo-sxM2_6aoCwq0Z1goMyERqyd60cSjiyQeG6pQLE2DuIs_MaZLZtWUV_sdFTJXnjWdYzkaZOgoocr_ABpY7ccopJpnzqAC15aXvbtm5hHWgGprWXZSGB1SS0-SWWD5cj--8CMFsSrlHHn7bWU18KE-3uNdjblS-jlSgGZOBSzSK7T7VW7xCYnZDP72JQJMqEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لامین یامال بعد از اینکه سال‌ها 18 سالش بود بالاخره امروز 19 سالش شد.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99907" target="_blank">📅 11:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99906">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99906" target="_blank">📅 11:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99905">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQLQz7t4rlzAubz99pGUx1XMlZeZmK_DtdzGEj89RQwhVnVlgxEdup7SBIqumsAAncqYESv9-OWsZjzCW3KyWOSRCf1nVV8oXb8vfR3X5ac_4V_MKF7Y5DvgY_lzQcdgyshD7vsqJEAh3gl30ktZHC_up8S0jSmXn6VblWV3u95lrNwj35XCZo-ANHXCbyFestDJd7OrFy9VmDyTuC5debQN9HV6yAFAm9Gi3utMbI904Cbq8C9hjxlCvP0HQ6XB7EHBW_CV4_nhW5dZXt8vCLp1YPQ6jT9nuQuLb0AGU32xHkNTu8N7ybOUQUxSh5bCtluG-NBTZICnjQk2eORC2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇫🇷
🇪🇸
استوری گاوی قبل بازی با فرانسه:
اونا نمیتونن شکست مون بدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99905" target="_blank">📅 11:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99904">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahnvmazHVPX3VIeRs6xyHP8NnC1O47mBFPwKHxn464PgAciB9N-tqJ0NBJixhdU_btwgGb21BK3AY8kAchewtM7NIUoTS_k9QrK5dPA0mOZ2wrVlDZEkL9MNCM0XKZNVHTBIdvDxlp87eZt8UXuHt3LJ0n85L6yKDPpJFI8mzWi0G4DAhvd1v2D90ROfY8epMeQSeoDnK06S87tmo6ZG5dqYYDNPnL--DY8iUh4oa7Elj12paEehhEOY0ch-3hbDIYTNrskDoM7cEJpGZXFQ46pIYUy_nTrweRNdqgBPkdwC2mBdaHkXEH622oRSkIxvB9zGgVcCQEUX5_uCXTSQ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇳
نیکولو شیرا:
پاتریک ویرا کاندیدای سرمربیگری تیم ملی سنگال است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/99904" target="_blank">📅 10:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99903">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99903" target="_blank">📅 10:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99900">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YzIENjrFoBglLezmIMb_JaQ1Hok7VEg3iQk8Lc_3Ni67QOdC0Mokq_7Bn87xxLkc77IeJYoqFMOLkDI_hjnANWBMbWuQR93orVwZTG0N0PT6b4hzIOyd6R12TIojdtSlLK8uycQFYZoCE4WqyQJwCs78iKmmacBUhTVK7cJ3jJIe5PQSWBMwL8asrTMi7I6WWG_c5YafZtu9SpH3-9aWnN52J_WeVL0ljQVnQNBv9FH0AlvYx0wD8HZ0Z-rU-9rj9hqU3YUP7n0epA38zIGHgncYzlw_rrHHZzisZVfUtrq9EKxmgp8fIVJKyQXzcmNOsTLqyQfZCbMkdtC72aoEZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c9F4jbyPOYEo5jEurrtHh0X52lG5g7p14DzSko1gGfUswWq-UO69dpT0ngs6ytlTTADeWlC7GgNAl4ejD6fT53G4ngD0oLu5xBabRNt_jN4HjcXksz0HQmUFtQTgtk7gaekc6ohGFwRkPWo_xwLKsjL_M7hyGgIeorC7M2Tay_nX-zoGlzgCTFpMTkfO-VSClR_gSrem3ItZxZYb4X8Ni7stR49u8U496zNvUWlhHsh6_z9EZ6TCmwK4r0xN5tNng9uS8msbmz0OdOsaJjCE8VvWJL6AXcUAfj6pSF8igxdRBZNkNKg_qGGKXIAOQY_SQuO3rkBpaNZtavXMHaouXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oluk-eTn8Co8kxSnvBPmqfGbWLLMF1kVzha-a_QiqBVr6FqxCE7soc0zRKw3emBbNFOX3z6P3OLYrJCgxYEySrWA3RyGsZDURNfFqkAt50n6CBVuY9hWQhV3IFia3tTRjFPmB0rlVA_mgghF4Q7QkGEixzmqe03wllZ7Lxn4lCiEt2OvQsSD_9SMvaKTbsA71a6abkKGQAlXykLBnzqbCAV9di8FCjLma63CYTOhZO7SL3KHCJPxsM-avpjSS_ksh_B2RRYtjTM2-XHVceyXs1bXYwhPBxH7X79vm_lcsuQh4DJmm5QMhAYPdamcuJbZmhaUDQyGFZAq2G_GcZpK_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
یک سال پیش در چنین روزی چلسی با برد 3-0 مقابل پاری سن ژرمن برای دومین بار در تاریخ خود قهرمان جام باشگاه های جهان شد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99900" target="_blank">📅 10:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99899">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/99899" target="_blank">📅 10:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99898">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeYIr-42A0UplpFprR-iscW601g38KsL-VTUpatxwEEEmw91W-cB3o7kOF-uUkHVFrGSqyun6c0ijtl6OuwYcYKRiKQs4k-2sKoemiBPyNmeHLYuBmx53i8dc6_4TjINOnjQOVuYoM4apeDOlE53k3GmZQ-wfMMRpyfapA_ch6dAunpPp21dHIKwzGTUKGBUT2IdlrpeupTe8-tonSwssbyJ9umyISwLzsS5YO2mYPJHR4QJgAhS1pkCkqnoZXIqYizvwbLEyx5Qpm4qBl7HGgGsrONQNHalUngJTPUaUIkurE9tbKzJK25kh6Lp82T9Gnukrc8FYdd91KBaseCYzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙️
نيكو ويليامز [
🇪🇸
]: امباپه یک بازیکن فوق‌العاده است، اما ما بهترین بازیکن دنیا را داریم: لامین یامال."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99898" target="_blank">📅 10:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99897">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2501cb2ee1.mp4?token=dMUqpOde4tZIAJp69cESfKup1OP8EAID1sclks7LYk0rlrX2Cn1uAx96C9dtdxU4NuD1LG3UNpqzKU1_rBtzpcj1F9ovVaP8XJVoS4WwcXdwfnItdC0m4aQs_wZUSLm8MjGaY_jli0V25IoNU-RqIL4LSltcvAFVSXOKbd7Mg6-FFEDzBo31nVbRlhCfc5xuG5SAUoQspuz3GVVnKJ7T2By--_jQx8sRHLnaV6Xo1ilXTlx2Le6hrdmPO2LysYhAs-CoEX2HAfG5DRcCkeqbOvc0NFtA6V3hZT2igB0Og8g25484cd5Dxuhk5FvBW1_5GHJKcaw5jr9BaCBsuCbUwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2501cb2ee1.mp4?token=dMUqpOde4tZIAJp69cESfKup1OP8EAID1sclks7LYk0rlrX2Cn1uAx96C9dtdxU4NuD1LG3UNpqzKU1_rBtzpcj1F9ovVaP8XJVoS4WwcXdwfnItdC0m4aQs_wZUSLm8MjGaY_jli0V25IoNU-RqIL4LSltcvAFVSXOKbd7Mg6-FFEDzBo31nVbRlhCfc5xuG5SAUoQspuz3GVVnKJ7T2By--_jQx8sRHLnaV6Xo1ilXTlx2Le6hrdmPO2LysYhAs-CoEX2HAfG5DRcCkeqbOvc0NFtA6V3hZT2igB0Og8g25484cd5Dxuhk5FvBW1_5GHJKcaw5jr9BaCBsuCbUwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/99897" target="_blank">📅 09:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99896">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99896" target="_blank">📅 09:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99895">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/99895" target="_blank">📅 09:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99894">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HyhNIu_tvETGUxXQdKoDh07F4ivZCC9GzqV8InDCMsc42eMEPxYNpNiN9aPG4b6Xwzi88C1sVuOzll7CFmkVwSaWK0QJgnb77VTLD6Efo0amtysJOYAG-ivJ2DTztoncl5Ocv3eMGW8WArfu2MY_yXjDpC8_skzR7HHcu1BxeH3HmvEt6b3T7rSedpIr7Sqkrel-ytXxorgCW3TYbkFNYAwZjEfTeITlS6ZeQ_thfWPX4lwpAYmZgGAoRcil1sTbu6gnI6_JY-nctPKFpNFHfoQObstqMdSUKdTpC_x1tkrrky1wFPhLU7frL7AG8msixb-spNT3AdIcQRdGiQ9asA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
🇪🇸
ایوان‌بارتون داور اهل السالوادور بازی اسپانیا و فرانسه را قضاوت خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/99894" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99892">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I9ykGQsB3opHWoaXLHx3oEjK2L_LvU7B5jBzuduJR5cy5RHBUEiC6Sh-58aO4xviiiXJlO_106w5LWAbNDiEVX5WvngzdcAfoUnuGdSPuHvgCBytAEs3WkEZYdYDu51Dt9Q4bC1HPBhiJog_6YjqepWeNpdixtqZZs0Z_sGLMugbdtlmnXGrIg3e7PaNSYfVR8uFBrAsUYv3fu2aNawPjEZJsDHkyiFWKnNHoAuynHtgIswnHuPDcAk3ozwVtbdQeDr3wuPAOfz1Fjc79xI6h5Hb-WxPRFtw43iZ_ljz78QLCoXYCKg--Z0rj_qOaKXGZ3HIqWnLxzgTfN4AtHaGPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CLI0sGZIP5DHpvE_sW_TXQNNB5bf1dMvr6_bpgyrYRhzH6ThyFpThHWO3WOyPiz5J2eLkrtr7yZN6cDRnHhtitE1xlKFMQdAYL11FkNYcJQe0aMS3KFvLH6rFCfIvQtOfNJao-FpLhJMv21CC1lJwSgMLRkZGKizXSUrPmaz3jLcBEXClmKk1usIy0sI_io9-u32gI4ubTPYdZ582F9-mQ_xAsuDX1GT-BLBl_RSVKCKBYgxIhZUkFELX8GNaFZ6X4Edt9Iw8EwrhUhjuuRpML5Hqu4cHRcUWpYEXFY6FVBcYlYAE3vkq84U2dUZ4bvrdFJT9TQYeGl0CrvO7ZuuIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جورجینا در کنار رونالدو با کپشن “Daddy
💘
” که میگه کریس حسابی حالش خوبه، نگرانش نباشید و برید به بگاییای خودتون برسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/99892" target="_blank">📅 05:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99891">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1MpkHxCuzrwfTG_BpQ_fBb6sB8Xv8u-k1Ue2fAu-LKUmdXd4PnEfoAAOBurYyJmqhsh_IvXTOHCJKiGQBMAnBAm9vtwQjWJanJqiz7xpgGEOpUq9FxVB3tqJabNJiKGxqNxOejVzxehwK8zJJH6oq3CSQVNmgp_tm34Wa_WW2MkSuW70UR94LVpia_KZvTr2KSy4qQQ31bwAXJ1iBGA7xs7j2XjLBhFKFZ8mXmPPVxjPOd1WQ5NRRdqBWugcOn86R7VZbv-KG4Q5T3W8emYhDGMNzo9Iz7wzFEXNbHVFUrBug0qvXQYAMf-pKkN4HyOA9XwxR4gZ8kmEFCIf4ZqNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
#فوری
از بن‌جیکوبز: الاهلی عربستان در ساعات اخیر با ارائه پیشنهادی نجومی به مارسی و دستمزد فوق‌العاده به گرینوود خواستار عقد قرارداد با این بازیکن شده. مذاکرات گرینوود با فنرباغچه پیشرفت خیلی‌خوبی داشته و فقط دلارهای سعودی میتونه این انتقال رو منتفی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/Futball180TV/99891" target="_blank">📅 02:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99890">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/Futball180TV/99890" target="_blank">📅 01:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99889">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🇪🇸
🎙
خوان لاپورتا: ما تو بارسلونا برای هرکسی دولاپهنا نمیشیم. یه پیشنهادی برای اتلتیکو ارسال شده و هیچگونه تغییری قرار نیست اتفاق بیفته. بزودی می‌بینید که‌پرونده آلوارز به کجا میرسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/99889" target="_blank">📅 01:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99888">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6_MuqOXpfY33DAfjo5zNjnIXrZkAJ8p8Kh712HkIzH7VdwdJAt-vd44x2qzeAdyXk0m5AP38-s7Uuxs8Hx4Mh_XJEquEBiYjR2hejWEjlKMQWFlYerQWpkQ2rVM60c3mUTGs4LxFP6530qqJTyTLZXBlL-ZvRdmoUOiaSqxzNahLNAWIW4SNysq0B9PZky0Qc_gF5bGDhcwfaMjJGDvr3iSW11Y0BAfifnEcNDzC3_fuwt_WB8Bx5cX3e5MpVhcDCq8q6fwuvqzyOg7MEY_VEISAxEEYIWLuMkIXpaqOyTohANTLs2X5d3FOcxgP2kXdfyZjbBfQ0haVY43k2fotg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوووووری؛ اسپورت: باشگاه بارسلونا حداکثر مبلغ ۱۳۰ میلیون یورو برای جذب آلوارز به باشگاه اتلتیکومادرید پیشنهاد خواهد داد و رقم بیشتری پیشنهاد نمی‌دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/99888" target="_blank">📅 01:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99887">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpeinUb_4yNFA_GzYZ1w4FaRJOKl6GZl22-migZ9J8KKP7AlfbRo2iL0QFrMuQ3F4ExSkr4-aWSl31azgSV7bMOJDi5cPLyWyrtlTrtETv6COAsvBUPCbmMAyBh61wTuv7MLVWUFpL71iDzBLkhmC5D1tmKTkck7vaYK4p9ffx2_75HoHnmWbVSsnhts7Pb8PCltte_3Z9_wXew1DiFfCjEz8-EGWQEaE8v7u_5Wo71_n9e2QtBPm_phOPSH_KzPXNY6ZHKajusuvD9IeVWq-s40d57jwgV2v9US--dYTi69TEWdes5DqP9fw50XEvHkWQZJQFu8xH6-Q6ffmms89A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
💪
‏ سوخت‌رسان‌های متعدد در خلیج‌فارس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/99887" target="_blank">📅 01:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99886">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2Nm0Za5btTUE8UejvOaA1zQjRlWxDfiavAL4VsztLSlJ18a9wAwssBqamj4cHz9gP_8uzE0hp1ClUer7zlMrFTfEf2cFa5qjZfsDSzSUWw7UAyyBbShRAstVk1YWXsvwbwRqeydWhVDvZ9IcCBGqlB_GXOLO_VHmmRR5AGgYe4XQDccCzMgcRkedtMK-LkhQ149EcSpXLALQAZI66Kl2RK2G1xfAjPpTtXPUaL_iB-If2SEKCd1ayUeaike78twwl4KpeuJ_l7CVNxpgGh8syucxEcNIrcMHvqtyF_O7-Jm3EacmmnXr1B9cHRSeXKTVp03dNpa1c8_LzofBzOu2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوری
از رومانو: رئال‌مادرید درحال مذاکره برای تمدید قرارداد یک بازیکن بسیار مهم و حیاتی است که این بازیکن وینیسیوس و شوامنی نیستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/99886" target="_blank">📅 01:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99885">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvXAKU4ph54-DG5YYr2s1r5duA1PdK9bhbfae9qjcJ5eAOSKFcO_c83HG662VqW2_inO8Ok0pGxDs9oUzXZP6YbuC2oRmx4QUQu1HC4wdnzxfaCmSY2-95qv-JneIeYf4Hf8NXYwX9JXtOgRwQa39004sUnkDfCyW9r3B87j0ykaA1KPoRqjgop1vfB_6yGdJ8hiCxx3mQdDpMm6QI-7Yw8Jzs45FD-q7r-DcqHglv-9Afh2tf8k2rGBn8MpMoThmJCfE5MBPxHybzCnfccq54yELGcgOoYk9nNAioU8U0QymSiZPolxTGDM1uOy0gAPX_A94T6JpExsWjl_sfKndQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لامین‌یامال با توپ ویژه فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/99885" target="_blank">📅 01:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99884">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6AVIHPuXV7COfxdy0tUQLnG2cjqWNqFK81Kwh0FL4SQOv_1Y6XatiEd4ikw0cQVATXulKBPL9MXmt-M2DubURBDW1a9oI3mRmHodaeAJqgfo3RKzMbSBHXKx9Ff2EFaZmnOI3S2ClpPCqFVsywkOzeXVGMxw9qEQjrVEDwPEXsHPPYHMImhorAbdhvlOx__vzpHxrUcTjD9-fF0B7d6MM7LWt_0N-I4fUt4lYA5EPL_n5_VzZ2Vyfvz60R-CoO9xdM--w1sN_zQAHiMIG8zPsPO0sJG-Lwr7MFZO1xMEqExf9Cc0GB_PEh76vzT9hZnkNIgqYTt-VOs5gObleMMLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
سنتکام-حمله به جنوب ایران آغاز شد
ساعت ۵ بعد از ظهر امروز به وقت شرق آمریکا، نیروهای فرماندهی مرکزی ایالات متحده حملات بیشتری را علیه ایران آغاز کردند تا به تضعیف توانایی آنها در حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه هرمز عبور می‌کنند، ادامه دهند. فرمانده کل قوا دستور این حملات را برای پاسخگو کردن نیروهای ایرانی صادر کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/99884" target="_blank">📅 00:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99883">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
انفجارهای متعدد در سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/99883" target="_blank">📅 00:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99882">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
چندیدن انفجار‌های شدید و پیاپی در مناطقی از بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/99882" target="_blank">📅 00:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99881">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
#فوووووری؛ شنیده شدن صدای انفجار در مناطقی از استان هرمزگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/99881" target="_blank">📅 00:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99880">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M7NVehrm82z0G5tp7ik7wuM27a0A8hGBmwAIqfBXAlmbskG1F5f9508cXMbgO_AsPk8MVl3fbbUJkWIslLarF0-u4I8Bu1E_iq_HgYjVoEbpSdQu6mpEhpBgC5vubAvtBJAPZHUsvvHUmYXMnPEyNNensON_WdwAB9cx92DF4LizWCl3dhdEf9eIfkZJ1X7s2HFfMSSrvUZ3_tnY7KywhjhOGb6XlfjNYWc6mYLURKkMAznscdZQ7h4rJdW3gF9wdJS7bJ8U93nb1aj6jtH2uDeUk-jj-ca5vw5K9hprNfkg8GmUDasm2MjfiiZzgzM9j8sUhS8ZA03fuX4ZBIgx2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
پرواز سه سوخت‌رسان از فرودگاه بن‌گوریون اسرائیل به سمت(احتمالا) خلیج‌فارسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/99880" target="_blank">📅 00:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99879">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
#فوووووری
؛ شنیده شدن صدای انفجار در مناطقی از استان هرمزگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/99879" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99878">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab9b193566.mp4?token=OwE_mE5RhDRyREzDKtMRJlSDq6kgvE_chI-Bb7SMx6EaYPGd-pPCBWjMpYeDp2FJQpnHYQqLm7l6gHznamEB06E07O-zYvLupCpjSbXfFojZKTp6FwVsF-hLBsItPgm1Hb3VpxcYVVCmL3g92xhSIFXEhoTRGFgOQZ_zC3Uky-AthLc0mKld5jA3Vv0ylcSmgvqWlKSyzg1nM9E_0IoRQX-p4aRGKFtL8TiuQWUYHfbz04cvUT9vKKrbEZwGVLegkxZoy5rGbwafjAaUMCfqc2cvhjJUGLca3uajlzomIe4vWb18HpLT0KmS9vJ2ZEAlVIV8G2XMHt0ZUucRDaDRwBCV7iDCAZpghJb5MDQs-eB3hp0Eo6bht2YL8L61GBabalTUPPhq6pG_E2b63rNmw05gAFfuPcEi18L7ihsBRagl5FzoHugfrjxqyAj6BGrxP0ERDwfRAk831LoQdqrey5Z2hG_RAr6zfrJwZnBhaI9AI9fpfGAm_Sx9y9YUN1cBhvifQWsSF2igCPDmjsGfRJWuYN4uaLfMLNqy2dNu1SsdcU7QzKndxVyiM0jn68reZBWuIN13OciqeokezmxmCG7lr8j2w4hxUb4XlBIa8Q2ZCCieIZvWVe8UQ62Fa-G373I8VhdxUHFM0Oz02Ift6k7fyxIEPpwF4boprkhGymU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab9b193566.mp4?token=OwE_mE5RhDRyREzDKtMRJlSDq6kgvE_chI-Bb7SMx6EaYPGd-pPCBWjMpYeDp2FJQpnHYQqLm7l6gHznamEB06E07O-zYvLupCpjSbXfFojZKTp6FwVsF-hLBsItPgm1Hb3VpxcYVVCmL3g92xhSIFXEhoTRGFgOQZ_zC3Uky-AthLc0mKld5jA3Vv0ylcSmgvqWlKSyzg1nM9E_0IoRQX-p4aRGKFtL8TiuQWUYHfbz04cvUT9vKKrbEZwGVLegkxZoy5rGbwafjAaUMCfqc2cvhjJUGLca3uajlzomIe4vWb18HpLT0KmS9vJ2ZEAlVIV8G2XMHt0ZUucRDaDRwBCV7iDCAZpghJb5MDQs-eB3hp0Eo6bht2YL8L61GBabalTUPPhq6pG_E2b63rNmw05gAFfuPcEi18L7ihsBRagl5FzoHugfrjxqyAj6BGrxP0ERDwfRAk831LoQdqrey5Z2hG_RAr6zfrJwZnBhaI9AI9fpfGAm_Sx9y9YUN1cBhvifQWsSF2igCPDmjsGfRJWuYN4uaLfMLNqy2dNu1SsdcU7QzKndxVyiM0jn68reZBWuIN13OciqeokezmxmCG7lr8j2w4hxUb4XlBIa8Q2ZCCieIZvWVe8UQ62Fa-G373I8VhdxUHFM0Oz02Ift6k7fyxIEPpwF4boprkhGymU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
بیرانوند: این نیوزیلند بود که ما را دست کم گرفت و می‌گفت کشور جنگ‌زده هستیم تا بتواند ما را راحت ببرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/99878" target="_blank">📅 00:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99877">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/99877" target="_blank">📅 00:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99876">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b76e61623.mp4?token=bg3KzUt6KaF9exmYhvYmoq7UoDfk6R0xT611g0kitrUuJo17vXVGbphHYPELAMMJmGZGQtNdXw6cG3J3JEUZMKJcEHP5zpJDxm-eyKhuVehN3Zldym5ygJxSx4EQCkGV613nXvjC3WS7tGwhSNMFEBQ0RW_XwAiiH-nLlxynNJQQlN0swHTzBeimsJ0VB7LE7YewCos1gvu6WC5hRwBCpm-W1Z1c2ZzWdZPyEiufopM3zmOwZluyVq__p7NwVEF0FqvQz2FDnnddNXaPQMqSTr9dc17kmo6Eu8Qc9Bm3XfcOCqHc0eX8q9mmZ9gbuvkHnvg1Gt1I6NuZV5OXVFJv0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b76e61623.mp4?token=bg3KzUt6KaF9exmYhvYmoq7UoDfk6R0xT611g0kitrUuJo17vXVGbphHYPELAMMJmGZGQtNdXw6cG3J3JEUZMKJcEHP5zpJDxm-eyKhuVehN3Zldym5ygJxSx4EQCkGV613nXvjC3WS7tGwhSNMFEBQ0RW_XwAiiH-nLlxynNJQQlN0swHTzBeimsJ0VB7LE7YewCos1gvu6WC5hRwBCpm-W1Z1c2ZzWdZPyEiufopM3zmOwZluyVq__p7NwVEF0FqvQz2FDnnddNXaPQMqSTr9dc17kmo6Eu8Qc9Bm3XfcOCqHc0eX8q9mmZ9gbuvkHnvg1Gt1I6NuZV5OXVFJv0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/99876" target="_blank">📅 00:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99875">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7990a07676.mp4?token=FhgE8jZQ2W8ZRYwsFYJY37H7w_4B4U1urJn33HwBmd9u_cEMZSncWCpz47fuBDT9MSEQqbNdZXSHD3yZzjImrP9q_L8gIqpUc5DUL0Udgg6nBiABcYL0-q7JtIGSZEe4tPRnRsRagTOQCKvJAaJQGSV5GEePyahM36pX5zgbn2p-I_wJUesjZt97A3S2bD_KPcQyfCz9izem6ACd05M0AMzy2kkRIw6ixrbCMMyIbfsDpx6d81BGyG5dTs7T09KBMOtLjS_d4Lsxx-W76GF7kcbOQEzimTy7Yi_vcVvwnevqkH6cAdS5PI7RMWFkyeQnPd5s0Up9fwLFtg4l3fS_UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7990a07676.mp4?token=FhgE8jZQ2W8ZRYwsFYJY37H7w_4B4U1urJn33HwBmd9u_cEMZSncWCpz47fuBDT9MSEQqbNdZXSHD3yZzjImrP9q_L8gIqpUc5DUL0Udgg6nBiABcYL0-q7JtIGSZEe4tPRnRsRagTOQCKvJAaJQGSV5GEePyahM36pX5zgbn2p-I_wJUesjZt97A3S2bD_KPcQyfCz9izem6ACd05M0AMzy2kkRIw6ixrbCMMyIbfsDpx6d81BGyG5dTs7T09KBMOtLjS_d4Lsxx-W76GF7kcbOQEzimTy7Yi_vcVvwnevqkH6cAdS5PI7RMWFkyeQnPd5s0Up9fwLFtg4l3fS_UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
علیرضا بیرانوند: هرکسی جای قلعه نویی بود و با این نتایج برمی‌گشت، مجسه او را می ساختیم. خیلی از کارشناسان خارجی گفتند که باید مجسه بازیکنان ایرانی را بسازید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/99875" target="_blank">📅 00:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99874">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_HPkN_30u7NFGqF5o1UUsja_UkM5w6BSTpYz-6C2iaoiHX7pd18vzMqGxLlDDJuzaY1fGrLouSl9yIIgxmKyR_uT_wECpUyWKOlcvFLNTatj6noww5ydbOdOTs8gMequM7si0mB2iD4GHKMaXPV11nldIaFrZ5HDFH9hlvF0GaJaCQGtrW-Vm7mfyCo7AtFROcE7k2wRcTqfDmcAiOBsYnY5I2dKiaxv4sEtPcVxwjLPZuyaLsxTq6is3m8k4He_C0I-QeTeb-cKHKyoHXQ85v-v8IkPVkPMVC_Po7-3hsTRJEkMqV7qsIv-oz3r71XEr119F9kIn3v8EPZO8ZVSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوووووری
از موندو: بارسلونا در صورت جدایی فران‌تورس و عدم موفقیت در جذب خولیان آلوارز به سراغ پدرو نتو ستاره چلسی میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/99874" target="_blank">📅 00:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99873">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFj8KzL3oxkeG_1y8H78pPdWctNkfKE74utPUjtrjJtE_l5vVdkEVZhxV6ggtL77bc-vPO9OZ1t342Z6WohY3XXCb5QAR33ygM-pXLjeKAaVT0D21caBn3lD6UwO5bE2U0XJ-Q62H6I8SlPwNI2HW-s_8V7s4iOb5msAV6yLSQmyeFsKxNauYBPrwXa4Q8mqfMbq4keNsB-IHba_-Q-HC9bTXaaIwklREDCQmo2H6QRy5nN3da6AW2pu6lcefqzOpQuQ0XWCiOupkSP_2yghIKDO12om1KxpobNo_LWp5MiXupzQTYWwF400DJ8-eXo_R66XTpXsKcr6_IbOfVNqdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جود بلینگهام با توپ ویژه فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/99873" target="_blank">📅 00:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99872">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
‼️
🎙
بیرانوند: ما بدون باخت به ایران برگشتیم و این برای مردم ما یک افتخار است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/99872" target="_blank">📅 00:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99871">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/99871" target="_blank">📅 00:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99870">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIDn8PbNp_o8ZKDxV7U5EUQNI5lh41j97aHZq1kFSptgboO2zrJxpf8zltUshytUhAtOvLG7KrKnd3p1lU7-GBqCzuX_XTGeKHXkntAvN8oUGqgT08zOGvok6gNj1WfQXhAW4sIfGKuYBlnPzCTdHxbK2-uFsaU1sdQiAdL0aC18L1dzJ79xzuqEbL3UeVyVSFJeC2GmSHj8aab94MNm2HbrdWydeDtGjYIM_yr66w9uh5gAZHzY6MngfnXpEsO9ZFcgPPddYB1VTLF1xxbNkALQXBTylxOFFLzO0l2v1I9A23Vp-482AbEEKY3x2FP7tDIzEzKg8P7ZD1z6iPzakw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/99870" target="_blank">📅 00:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99868">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FI-l9dZwsP4zeA6Onv7UtB0JlZIz0NcyIGgX08ajIBZTF-HfX6FWJDdHP1SRqxyGYs9a5xw-gkAr3t9FvKMZ9t8svxqRzndevn21IGfTJb4hCdn5-nm9yg-1hh7Ku48iKW0aWhYWtOBxqSe2NM_3W4_GLj-eIsfs1nOxDcRfUWX4MVMUo08URNKxjfO5TzhaYcQ03mMUeLKhlLjI0zHWrirHncvbg7y6dVsDxe8W_qyL_o4aAkj6zsMu--6O8nNyb3WgXxT0ajtavlMasDa295kJbeKOqlzM30FuiOaMVDzIF-FonajNR7nJ6DIg-qwe5qIPza6DXY-_-UlrvwJtQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#فوووووری
؛ باشگاه لاشخور اینتر درحال مذاکره با جان‌استونز برای جذب رایگان این مدافع مستحکم تیم‌ملی انگلیس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/99868" target="_blank">📅 00:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99867">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
⭕️
🤩
باشگاه نساجی مازندران موفق به هایجک کسری‌طاهری از پرسپولیس شد تا حضور این ستاره جوان در جمع شاگردان مهدی تارتار منتفی شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99867" target="_blank">📅 00:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99866">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fMCWcKjLa65pdmOK5nTmlBYiFq5rmR1p2t1w87a1BWYCE2HIE8kmEgD5TmhA_qCG-5SWCCjzwdMpKZ9EWxZlKl_lVUc33AZZ6cdK-lhdi2aYF5ghSPJzJ1UWuh6iaJIjTU7EYK4oyz5u-5B0BuIm4zd8jCy3y_s8q4kZILD1gHBz3ICifglwBn4nV8X2d68Z2GrGDmMwdKwNmp3tzawGXKEVrEe6NoxBVgvpNUIgExuIdBY6jPv9reT_fis3ZfdRJD1JcttcjpmyVkAC5P7wiVuZWg24h42z8Rkk6g0a1PEYLdUuMUL1dCvcSpcg-Z5P9LhJz7aEURw-7zs9AsWUPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری
از فلوریان پلتنبرگ: یوهان مانزامبی ستاره ۲۰ ساله فرایبورگ پس از درخشش در جام‌جهانی با تیم‌ملی سوئیس به استون‌ویلا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/99866" target="_blank">📅 23:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99865">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UNDBrH_khc4LtFAIW2LJVId27a15Fhsu8D-qPafArMn_4gFGEoPAqOyKpUWZ_xCmy7zg3nM9RjDjDf196jzzLVelHTzqtOkwgqT-ERkdIxvMoDfuSDcltEXSsOCjLNNuqiyIo1TanWfPsvLRxXxYAHtLkPPmeCj41i04nS57Xqjj37gT9YsK4eQr8vvxrGqK45RHEkZmHg8qHFO9rIKCitvcnwpsfkoNy76GxhcEyaemIg-TMq2549E2tMawujNVo1uirdkPHclkuM2_DuQ6MgT2e8FYssuUsci6I9pXomUoppUf34LsFaBUEtCaR3SZ5Q51RdhxmYBYr5pB6wpKGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇧🇪
#فوری
از رومانو: یان سومر گلر فصل قبل اینتر به کلوب بروژ بلژیک HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/99865" target="_blank">📅 23:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99864">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLocnbEAf-FThfeWAH98s0G9kvSnNdNx-tpy_IUJSA-1gEOG6gOfu3t9-QHYVMPMa_OwIgAw_vnQ89to76ja4_G29koR66Hznup7n4Q4Lba8ht2cTPmEsy9UEedxyM-O4B2Sjs3IYUHZlHds0t7x0GbekU98Zr0y1Xwu-ePe7HDwX2gZBNTRNahNqu72YGOGPGR7D4-1sHX-lGq_EUIBR7ACoTDKEcYdphgdBQVi1S3QO6m2o7jWHdVgrMDD4rULDUlEW3aa675Ef1cVVgXYVlX-80qDydLt6-eRVWO1aqzbz6PxDYWWypXG2CVoVnqWPde6ccgXcIQKu-rcutUAbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو هم دیشب تماشاگر ویژه بازی آرژانتین بوده
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/99864" target="_blank">📅 23:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99863">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyaDBMF9zO8duZkJQ6JR7OO0ATCkZxtBBLiLNE2-QP-H-wbsoXuJWxejJUstxnGyLs6xg6yU8JI0V3MxJAw3wNkULd9AyDXSgOOyIsIr0lvJdyC5IxxMltg9GCd3Pe5YGntcHITUijxphOFGuofJXWPlNtiuRO0lnHuwrDr4Sb07T5DprNtZ5PuM55L3RSJtgrmx6ECvEycu0wD1UCaCk9xMQo2xqKukQ-PFAye2LLa7QdgoSiTnvUx9Y6rHH-h5eMXpFa8T1HvSZ573igzr5-vXgTdZucjnFRPBrO_2LO_ZWOZxzz7erayLas-EkiVhq57nKREZ5feIk7gP29cNEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلوارز و دختر کوچولوش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/99863" target="_blank">📅 23:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99862">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6IcwJ5KOC6SiO93sUQPRn4WiMjBzs8F6zEyDFKZhMhZHv9crsshealiJ5AhCeXPaQs8piNm4ydNP-tr2VajNhLSXWlhvdTh9i2tOm-tvcVSMerT1YYkpNIecl4rGPU9926VP83HlTLq21Njd1rgKDvV5jJM4la56ACGl9GW5qsQAWrJ1BVjPbQ1pqt8K8WztUB8fD0Pnqp8vP389RvmvBNsMAIvvLROtScknptLweZ7Zt8nWpI61sxnTnGDxDWNrcJ6-Wd9E29b9rtKBWPkuo_jRGiiaJ8Z2FYM7ur5eeYb0ofFg-QA23FDlwEfwFVUP4_tPMTfl7ANtlY2QnCATQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیگو فورلان ، سرمربی جدید تیم ملی اروگوئه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/99862" target="_blank">📅 22:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99861">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saPWlVI1PAMCtODPf5yDFxW7tx9GdudcU7IUoo6ylGvWztdXv0awVyLretKaTz-lV6B0yAZJ3hllxNu_y7A00fKbllYWQ2GrMLiDKuRO2eGt5-XPU9ZUFlVnW7KqDLamYqMiyvFDNf_X5kBxuhPOuJnqqPpRRamiRG6Xld225ZIjyHPXsDkMrQRSJ5S3x4JnjvUQrlHlHHM64Hi3HBsrMRXPQUfI5yGA38voD_5Av72YJlfkL237u8fKIRTvfruO07-FZYjm2Kj62PYSuGq4nRQt8Oqt-q5F1ukTTj87ur1tX_du8asjuqPLkUagwsqNpyAP0FIHqROfzIQ21RUvig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
کیت دوتیم اسپانیا و فرانسه مقابل هم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/99861" target="_blank">📅 22:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99860">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6hwmMp6Z4_ZmEXTcvjMUGQ9mnhZEOdWxwKZckZH61rAmTHxXQf9fLAhQo4ZFTvpC0Mau7913Y0jDW76nSQUrMYhyUGuhjTu9oj0oGmf7fqXq7oF5BuPA5cLl3mKwkeImV-nEY9VM9ZJBMNvX3nBNfcJPX31fEFdtYkst3izBIZz5obXZLyjtS09w6TtXU7lpHEvj28yShwYSF6Uekj2u4mrRk1Tfw8rXmRG6zo0j4zMPWLcVSkikPILTQoT5HLhGa_Oj0THRx3Aq-JHjtVHdoNERZyJhqMMCkhpzpVPC1Yso0vYTjRoQBKaBwiFrKgnj3nLQ6BPxIyTyASGu4_sAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
کیت دوتیم اسپانیا و فرانسه مقابل هم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/99860" target="_blank">📅 22:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99859">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGQErw2LGMmoZKasn3jrvOrVbalAG2-CVellDHXYkA-mTO_mkeUDKeU1Yz7xmW2c6WXAk8Onc6_Kkh9ybcPXTjZx69XcDVOXpX-t_zBCUFLTl7NG7fb0bl1ETLKGyiFUi7aLvsHwuPAE4mmP_rQrWmb8MrgS9zkceX4F-3-AUu9ybSG-2ZWg7f9yDulcvwrifvVKnclELV5N2LvKnfgm_lZR5Jhngz8usiaDw_lde6C44bnyuzwGa4Squh_dJsEWh3stRa59lQmoaI2I9rgpT1FneQ7gQaVOqGuFsx61YUkMz7BIUH-evQ2lpUzclQ_j7lACdj7fUGLaHdmcmdSc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دلا فوئنته:
هنوز لامین واقعی را در جام جهانی ندیده‌اید، فقط منتظر بمانید تا طوفانی که ایجاد خواهد کرد را ببینید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/99859" target="_blank">📅 22:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99858">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeSxxes0TNcReIy17pCcTqWD7P2lFtEA2FL0W4KFxspof5bqMgYJJCe1Q3zsOk7H4Lb15Z7ppC1paLXrQ-YszucLqu2GgnXrN9wp87VdLVJI2HAgqYBAFHJWzR-EsfT6TT7iOfaJEJqmuA5J2Mlza3ojpj9kwrzYjLFX3hf3MvPdt7wOoe0pn8WuY8M9b2l7nKDE8jQOosWIOyL0fQJDFGHMeUEm4TkhsX0-KAuPBWR1C1I62TunFO6htKnnRrbKWuOs4LTPI1ULs2PoQL-gVTXCMJlcQhwBujhnu_Lw5oyzcwuK-FjF96VEAQ1B3Zcos2VGoVDX_lhPYbTeiDmmyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رئال مادرید معتقد است که اگر انگلیس یا فرانسه قهرمان جام جهانی شوند، توپ طلا باید به جود بلینگهام یا کیلیان امباپه برسد. آنها معتقدند که این می‌تواند شبیه توپ طلای ۲۰۲۵ باشد، زمانی که رودری به دلیل یورو آن را از وینیسیوس جونیور پیشاپیش گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/99858" target="_blank">📅 21:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99857">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
رومانو: آدیمی چهارشنبه در بارسلونا خواهد بود. سپس تست‌های پزشکی و امضای قرارداد، همه ظرف 24 ساعت انجام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/99857" target="_blank">📅 21:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99856">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
کانال 12 اسرائیل مدعی شد:
ایران قصد داشت ترامپ را در جریان سفرش به ترکیه ترور کند. اطلاعات خارجی این توطئه را کشف و به مقامات آمریکایی هشدار داد، که منجر به تعویض هواپیمای ترامپ با پرواز برگشت او به واشنگتن شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/99856" target="_blank">📅 21:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99855">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3PjyYejPfBFJDMSYUJTCATgVqNQhGVUSmteBaMNnCTxvU07qE2hjdEDEoqg6YfB5iW6m-iBM6paoUksLfL5SYLNp80l4Cvvz_E0mR236YJRfnEqd1npi12lcksRLOsJBZenkaqRIacwB_lAhxCklTaAJ0pZ3jkxPQb9rum9AVKUUb6QjqG63mYTauwvK6guTNLUtmWjn2Xk6lwdYAzSdZaP-43hVIaJjk_e33a56Oho5fjY9zhLG2KDnj0PzwBq_w2Vn2hj7_wWQbjzzKf5Dsk-QIdgIMb8OSm-zajKMi4yRj0STbTuWx8uN3mL8slZ3-Zzmrq_OrCMhNuSud4jEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🗞
🇪🇸
#فوووووری
رومانو: فران‌تورس علاقه‌ای به تمدید قرارداد با بارسلونا ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/99855" target="_blank">📅 21:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99854">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vhkt-lwLt0VEcEzP3tVJttgoBXKIchfJQIYPZGD8G3ubLhf-gf3vgT9VEFK9m3gE6bLrpiRhT2TfrG9FUaqfylwqz8W4xNFXjuiNCFjXW5CeFtv8coX7fEqNu-tDMtT3-2_4VJUSAabCFB9URwR-7P_9kHSxO9bZMN_cMWDJDmmTQVW6_T8KAkKtcibJbgOkvJNWjNVbqXAj0V9B3rXre1c28Ke1Ogp3no9XMM227KJV-jBHFEEu17uDx-Af0P2Aw8zx7tkl3XJ7VcGgoSrhHtZBmiInPW4dSRruJ8nLW1IT4Bmq2LjeT-_R824tUmE8vl0Qaaxdfp7f_-3gNUzrLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
#
فوری
؛ رومانو: میسون گرینوود در آستانه عقد قرارداد با فنرباغچه ترکیه قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/99854" target="_blank">📅 21:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99853">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfqY1uwmBHp3QZyEI1gOcHpjZTlC8Cjt7Y-PyELRqGx1F59S3HBYybWZVjgPp2uImkY-qiKdNO38fKV9h6343RMnu2kIW1G3nbIWfbnZCmXrf8TF2XpDfnQVVfcNhEt4qHFmE_PmIW6uy_CYVIWR7gedH1ii4RVTK1tjErrWKA0ySmDO47jYdtG7u_JhTP8_MLhmm83dMPoXBJWzoZbrGGx-EwBMH3ydA2d2rgyLA2s34e54dhLxhPhSjI-sfvQZw7TWJVF276g3-zFOTG6_oibrA40KPJDdZo2yWIX6JAqyPfUSERbLCC98h-Uk215YQ68sNN0QLq9zZlIm2mNrVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوان لاپورتا مهمان ویژه بازی اسپانیا و فرانسه در دالاس خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/99853" target="_blank">📅 21:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99852">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7nO46Mfh_F0othygQcsWmA4iD-Y5LolDzzGBfo9iv8hM_LV1jnPKnJXDduJdJRN2bDRLwhwCgD6hO1YJDBtIiTK1QPPxpWd7N5IqWoukacea_P0tzAoG1glTNu8syKnmCQRg_u7I75XrYTXme48KCoJtTFlTwBC0BoruhmbWDnXsoB_wxxcasNhknSyj4Gxo4k8h8WZ3DZVMmdbCmfRTqj_aokanNztnergcXtZE1DMchSvUJmEeTnFrfM3ewTbZd6ua9cswGVO9TiTjRMpME3ADSpEBKe7QSjefX93hhbGYDd89h2JFR848YCv4r3-nG2yqQBQ_jx6TGgRxkm6Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب احتمالی فرانسه مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/99852" target="_blank">📅 21:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99851">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeLPrwMK0U2YnOVcRpvOeZos5O6PWmlhWGMGC4Y6wKPxOsUlLZnzCqAhPM3TbsxGtTPlur8HFnemkjgTy6nmbGu18b4-codkC9eKCeOOXMDOuNUrtS4FJw73iCuxrVdfKWMuATKWtBZNTRmufMZK6aXBMQaw2PQs8SKy9uAFWaaf1FmabICNqge-npBLpgRVo3Is6pGX8ZiFV9qQrNhJAb5_RO3ZNawOSbXnv82wmg_tFN_qc1WTjVYeWLc80A0mTv29SaCudroLJ8VQPkRU5gxp-9eHqh2CCJlMkFI3gvJyQqN4YSVAo7IkTEfEvmAPu7rGcZ_VYkSYz6odKwaPyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/99851" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99850">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99850" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99849">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/RGH_6_l-QMWE2T2I_FJYem18tyFCoVg6-dkp6f-SeJ2A_ypokOloa7PRzwxua2hYibzOLYCUW87rlPoejlLK9vLmYRJdXW1Tdm7Sgb4p5g5IbmLWjTYWXJQ5mDBDznuBKUUN8gov0GAwHZL54cGF2Hwz6VgFaNXdZ6IlMy-xaBcKakc_1BmwNvdvju_GnW11WhavGA-k5TOyRfR63LP6lW0tI0Lncv43m83yEqNU2m-LbdYzQ-UseIyO89pecMg28pBauP7cR0a8JvUSlb21C84MBwZvDNl7mhSothrjmTYmoxjhSxmGrJ2QGd_J3lkpknK5bDhdPxy3H3ONqLgdTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99849" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99848">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYHBKRZAciVLouqwIFVNQWzkYuM8NngmoxyRvVloNg2qxYe-RRttUjtmviCCLwgZPtBooMMpqw4mpAVPL-8SXm7FYp1jimFSMky7t45sKESJdRWy8T6ACK8v95w7_rrg_PkP3ED63G9HBAJHMkLoy_7EeGk7lmuMlCrQFGmTFijb7Oc6fZ1Jc6FR9mGDUJcagTccir4ZWa-ya-DLMvHdx_JLWKzE1vrK4NJyHeoylwOP01l_1iQ2U3lVGNR4D5ZjO2ZGJyVXkXLjfHNb2wDOoqm30jB9NHaa9bDv_NRHO0KrORLPrTw9SlDlt03bsBX9YJGb1LY65iIF45rfxaPjNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فودن و پسرش تو تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99848" target="_blank">📅 20:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99847">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6429d99ef1.mp4?token=mRXT_tWP9UWjfAoLRrRp2YzZLYFHn1NpamaOT1NJrELDw2kRqvR6jCO5ZRospj8D0bT1XJfgRjx8uha5gcA8pMIlnYMOPovKSm20B03CVNjq3OZ5J_-Z3LaUL2Y_MKxV4RuS1j62D6A6E5nsccbsHxxPqNi5B9WXMxKvwB2JKI1lfxb2cDWQF5C7WA00JW4O2VbDwON2-crQaKYpUwgE4EN7qfllvvomT7SWQQ8PTXQpFnEjjSqTWM9JOggJSfj8Hm-UCwrmd3fY4XKLkb5p6HmRomQqKENLOV5Y6ZgyVY2MTMJWJiCxS-h_KWgTrJ97dtxMFAAuCamN1KGPbrpZAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6429d99ef1.mp4?token=mRXT_tWP9UWjfAoLRrRp2YzZLYFHn1NpamaOT1NJrELDw2kRqvR6jCO5ZRospj8D0bT1XJfgRjx8uha5gcA8pMIlnYMOPovKSm20B03CVNjq3OZ5J_-Z3LaUL2Y_MKxV4RuS1j62D6A6E5nsccbsHxxPqNi5B9WXMxKvwB2JKI1lfxb2cDWQF5C7WA00JW4O2VbDwON2-crQaKYpUwgE4EN7qfllvvomT7SWQQ8PTXQpFnEjjSqTWM9JOggJSfj8Hm-UCwrmd3fY4XKLkb5p6HmRomQqKENLOV5Y6ZgyVY2MTMJWJiCxS-h_KWgTrJ97dtxMFAAuCamN1KGPbrpZAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نروژی‌های دیوانه بعد از حذف جلو انگلیس
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99847" target="_blank">📅 20:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99846">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvvB5_XAvgpAfpAmerJNvERUohq7VsRgDiK9Xde40LT-QejWINXwIwkUk_1kKE_9FCfYraTYkPMXN6rntzbWZbuoD8pmtZE6VExXYp2w-E_lWRJWlJq6ghhNvu2xBYXPClpI2nzACOWwuAjp9oT6XOq5jRr_RbKuxw5LOej844QafSyEUGBwddp-jSvj1QGSZas8VoPvTCAqsGH2rKIlxgWLY82mmJ7YLDCHYeHZfMDKNbI9yB6ioqWrlLmnJIFpKu0wlglLGKiZR1ypsJxoulBeKS_Ydr1t-tCqAoYkt2ZKwDGmnW2zr2AvY-LvLSmayOqCtZHmng_j9BTHlt-ahw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/99846" target="_blank">📅 20:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99844">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWr9kVo8ueUu5nB1KocTpSuSATQS03zvIjgHxbnSNoFj4l33QbfYAZPohicKB6Ssl0Q9VvPCcdfF9E14Rv1br5mS41Dra5sTjK8FQTtYKfGfdNHIIWkJgawjaCYK2igDCdLzchiRBxjWeeAU7oJ5nVSnsdUL7OEUKgVf7dpBw6c61qpY0KnUnluLvchDlh6ZRex03Caa5r7dVQY9xt7o1n_SC8ASNSokvAxjVMgIoaKltQgZ9NZgTns6bU6VWtAKOJrRzNpnpgrEvn01v0WXfDcOC-GZw_fmyrs49Bqz2rqDdXw1xQsGEyMJUTG-NeIdQ_COvjCw8rL5-WTGc4v6zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
چهار تیم برتر جام‌جهانی در ادوار مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/99844" target="_blank">📅 20:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99843">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه به قشم در عصر امروز خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/99843" target="_blank">📅 19:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99842">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/984b701bc8.mp4?token=ACzm9wIfKdNByHqJpWOXzc0gbGYm2RQfC4gjhls56HD9U5fNryQ6m4Qb-Kax8JYnvch635-FNtLiGzUZjeJFxn8mMv0EfDSuVK2ietIRo_tqt7bB3GtGumWXHyVmNBQYWLq8ReQP8BmCkXTvbE7zX87cd9bcZARpGcc5yDFXbeU48VJ-25rvPDiB6E3lmdd8-5pbBgHmDJqp6E8XJBvJbbir1r-aDq3jQ5PZidJ-KEYW4RXAinFPOhAfWBKy1hzO8IQlIi_xY7n-05Cowg7zjD2-a_k2DhLxFuE0htCZgre0yXrtCIq44UYAS_BQhqB_vGYBGM00i6jX1rTZT5hy5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/984b701bc8.mp4?token=ACzm9wIfKdNByHqJpWOXzc0gbGYm2RQfC4gjhls56HD9U5fNryQ6m4Qb-Kax8JYnvch635-FNtLiGzUZjeJFxn8mMv0EfDSuVK2ietIRo_tqt7bB3GtGumWXHyVmNBQYWLq8ReQP8BmCkXTvbE7zX87cd9bcZARpGcc5yDFXbeU48VJ-25rvPDiB6E3lmdd8-5pbBgHmDJqp6E8XJBvJbbir1r-aDq3jQ5PZidJ-KEYW4RXAinFPOhAfWBKy1hzO8IQlIi_xY7n-05Cowg7zjD2-a_k2DhLxFuE0htCZgre0yXrtCIq44UYAS_BQhqB_vGYBGM00i6jX1rTZT5hy5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتسب به حملات آمریکا به جنوب ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/99842" target="_blank">📅 19:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99841">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
رسانه های عربی: ایران با موشک های کروز درحال حمله ی گسترده به ناوهای آمریکایی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/99841" target="_blank">📅 19:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99840">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
دقایقی پیش صدای چند انفجار از سمت شرق بندرعباس و محدودهٔ دریایی قشم شنیده شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/99840" target="_blank">📅 19:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99839">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d63368dc.mp4?token=OXReVfUbPDVl4smLTG-OsCO0gXp3Y7U9uybTTh4XrV44PdGxhszWnr29f3nS-hVRLs48T6j4awrm6i255jw6hk8_2PsVJJh4I94mV0TBJFNjLPMI4mLgx9cPJF3zkD2qkZtyqcmfgqB42DY-s6uh3rkUl4Sb49NjmkWpXcNk151l24GPtT6Y6J3bajL4UyAdgDmAZgE7xsD37CTa4YUvpzf-1Qx0qhB1nfa1gHhHoF4IOC3Bt1GhgBTG9KA4Xyqay9bQ-ZWDz75Vz56eIY8bXrqlYDUf9uwwAylt9FpQw4grUXyCRHozWl-F6sBuWTMO4xUUqMpvj9J0tGiISyh7KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d63368dc.mp4?token=OXReVfUbPDVl4smLTG-OsCO0gXp3Y7U9uybTTh4XrV44PdGxhszWnr29f3nS-hVRLs48T6j4awrm6i255jw6hk8_2PsVJJh4I94mV0TBJFNjLPMI4mLgx9cPJF3zkD2qkZtyqcmfgqB42DY-s6uh3rkUl4Sb49NjmkWpXcNk151l24GPtT6Y6J3bajL4UyAdgDmAZgE7xsD37CTa4YUvpzf-1Qx0qhB1nfa1gHhHoF4IOC3Bt1GhgBTG9KA4Xyqay9bQ-ZWDz75Vz56eIY8bXrqlYDUf9uwwAylt9FpQw4grUXyCRHozWl-F6sBuWTMO4xUUqMpvj9J0tGiISyh7KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
وضعیت پشم ریزون پایگاه آمریکا در کویت پس از حملات دقایقی قبل سپاه پاسداران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/99839" target="_blank">📅 19:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99837">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VP46htSLcATX7o0xTC000nmvPEFn7vgmnlUdEWpuK0bCHgX7x9p5y49_k_xMVGzYVWVp_E3OQvA65yMgSYG6D0tcdQPQF25DPLiJgliy9JxwK9vri3nUQuExvV3Rl9amC58WXL0Gt3qdLu8e5g2mDiumtDndWljdxHr0DwSYnWSobiAn6p_N5RQIfNv4BZG5g-G7gkUcQZSSgxYP2OG9Rna_FrWLqHtbE8kPpnB4-GaR1WtzQpyeupRZipqC9vWVhMHazbUergoG-86sk62AHKibYnLi6tt2QHolqF1zzaJepEJvpE9GZT073UdkG60fw_MfNSAOKqRYjpj-oA8sYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g-pceACASEUhN5EdcKQnD23-Wr23um7opxBFwMnt0LpO7w66WORlSEOMb7ug2ImGr6WJdX4xrQjps8Sf8cyCe24miP_jJ8ZAfgirW0UrN9rm35DODLkcg4wEBeWhOKyVDIC9AQnhXrHa5w-PTPdQZ_HFemV8RoGNQQuyuLEMG9Aj5nlWA7D9nxJXDaQrNRvHaiI6EVf0ADLdDun6CFE0xtQFrGQE4zrFvqs50r8YbOfYAvrQpblOgcrcFxtSct2-9lX0z2_oBcZU7y_p3wmWQjFrOt7DRVkf7eRJKyFWaSwXiHD3MnnkLj5VPVeTMND4_G1RM5F6rZlor2IvyTSeSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه افتخارات تیم های حاضر تو مرحله نیمه نهایی جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/99837" target="_blank">📅 19:25 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
