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
<img src="https://cdn5.telesco.pe/file/t9V3qwRjqkK3Gm4E0f9xr6BO-LmX9NjH0IqfYWSeWlsIiSvL_YOIVhZ1R-3F8MBPhgvlotiG2ZurOOXQ-OoTbaBIX-tMSKqbYpGvVPOGbS57znO2LKARPlNPdroTfHYV5ts-gfEf7-XqzdGCRqBAM20tscYAu12dUkHjTSDDR9Aj-VNj7oL9I4pZdF8cPOpaGKa3e9e3rldKuTi3VGlWrNu53nhPT5H4cJiiTWpxYaMDY3ewNCMpD5rYCtExd_sNS-dPgS2Vqjt2uJkyFca9KmZlu5J3YxIcARAHVqpaJUlnIltmy8pqnrHNqxDi9H7xA0MxNKnD5DttpJ23a847yg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 503K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 13:01:52</div>
<hr>

<div class="tg-post" id="msg-102552">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEOVHNaZv2Jxpa4FGlutaaQ1RN5oZTeTOac107O3ExlLld8x7-VadbIqSuuLrzTF40_8ltaCjUQ9p_nbge5HvDBAYjNhgxSh7_yre8yTREqJ9qkLg_V9tbEyDjiBKI379_1ohdzErultbb1__og8ixJVCWW26nMZSiA_qgnPIWRnHT98LLzMlO0MakrcdqQUsph1RpQ-pYUkd411SUr7E3UFDuRSU5WvPKLJczswAboac73jrhnvgnPhszQasabTwy5DQ4H8rWAe4667xZwOHPDrWqSVIS2Nl7EiL-P5_9NmebeLm61HBwqHmI9cGSC3bUtpcAZ0IHZZhRRcq4f7Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
مصطفی‌متدین از مدیران صنعتی هلدینگ پتروشیمی خلیج‌فارس در آستانه مدیرعاملی استقلال قرار دارد. این شخص پیش از این مدیریت سازمان توسعه هلدینگ‌خلیج‌فارس یا به اصطلاح شرکت "پیدمکو" را برعهده داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/Futball180TV/102552" target="_blank">📅 12:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102551">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbWpYUj6mrKFYAaIskFT2Bmr0zTJfJoyxk1QMRn0bRYspK79gEyC4Ui8Cg351pDGVRjKYTzClNOLzjNERUte11TgdMqYd_Q0uYFucdHjH-_DbLifbRYE2ePvIL6xnzAgpotLEgMGOw3eunQlFxJ2uvKovdTmUzf0JO_coqPROYc0ssS9QouZAQVEzhf9sjBd-8gN2d3D-xFHEPIKczIc6P921UFhwlT6TPnPuGpXwOvk_yD-0sa9ujO74puX7mnyAcVBf2vj0THcsgLS7lMv0ozFd20iZZuFk-dzpdgfhrmdPDxn_3zTdQJwbClCAsQulgxx3M7qlL7W8BPRWgpL3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبرنگاران ترکیه‌ای: باشگاه تاتنهام با رقم ۵۵ میلیون یورو بدنبال جذب اوسیمن ستاره آفریقایی تیم گالاتاسرای است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/102551" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102550">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpMD_1FG6n3vd4aatAz4wQbDPL61KikOWUNgLMz6OcqbIcouug5_F_8InnD8NRM2mNRiRQasEm45dJkAVBb5q_occWGpw9aj0mg27J0Mw1L4Tcj201mKBn3psSMElUx97Z9EHyNHH1EtHzzlVU8NuGDF7XgLPXGcul3X6VuEyb9X6-ho8kI5E5sSVGgpadFTzJeQcHJBBLIsOxyh-ZGV3UwjAD1Az_qJr-x37Gfyh461L5O3t5d4KiuKN2AYRsJ8QPt0kS0ze7jvacwD8XXNuqKji1PRIIYdXTro13kG96hxLgt1P3AiZtAEdWu6saQaOEwzXaPERnqAp7zi5ylLjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
تصویری از مهران مدیری در سریال جدید مرد سه هزار چهره در نقش «مسعود شصتچی»
+سریال تا چند هفته آینده از شبکه سه پخش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/Futball180TV/102550" target="_blank">📅 12:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102549">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a514ca93e0.mp4?token=fmM8ErJMyZU7WMiWpZ9GuXHNwWRKM3UuE1EIwt6CfA4ESrMEMBGtowdWramKjb-4gXfcTg9ydnzETn5TPmas9Qy8DqZenV4wGO8Q9x10qh25CZH9qWnM2R4gL9mYrALIB-6DBmO7ZBJBpJkVilYnf2Iu58sYmiRF9WrdfTdW2BvDO1KHoivP8vwSqi2lhqDp_XzJL-4qpU4iYjLbOM19tC6XX9Yw6QWu_cwhfVxJfMAMSYDAV5k6yhdo7AqisrKOreuaKJF87n5tZSde1fUJnTB1WDljyZv1I5vSYX2nGTgvgU85onfFMlMUnasvnoLklRUA781w2gjAKvoOTJba1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a514ca93e0.mp4?token=fmM8ErJMyZU7WMiWpZ9GuXHNwWRKM3UuE1EIwt6CfA4ESrMEMBGtowdWramKjb-4gXfcTg9ydnzETn5TPmas9Qy8DqZenV4wGO8Q9x10qh25CZH9qWnM2R4gL9mYrALIB-6DBmO7ZBJBpJkVilYnf2Iu58sYmiRF9WrdfTdW2BvDO1KHoivP8vwSqi2lhqDp_XzJL-4qpU4iYjLbOM19tC6XX9Yw6QWu_cwhfVxJfMAMSYDAV5k6yhdo7AqisrKOreuaKJF87n5tZSde1fUJnTB1WDljyZv1I5vSYX2nGTgvgU85onfFMlMUnasvnoLklRUA781w2gjAKvoOTJba1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سورپرایز شدن مورینیو از عملکرد خیره کننده و درخشان کاماوینگا.
😢
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/Futball180TV/102549" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102548">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8a29e5339.mp4?token=APPzhk5ndpZACGZg-UD4Dy5ayB1yU8Hme-iHa0wGnZD6FJJBC1H_eQH_BxHCL6lRplsuLDYJ3lQ24ebxCZXy24a37bgseQ5tizY2ANqaDrashsGikCJxI9hJPouggjrYd8JqVjQxPdFgjjcS0Ulk6BW0YhX2vtexWP5EgLi6tD3suRjGkWrefyVlt-29PeXzU05kk4Ka4YFdpP5xrWDA9Lh9DAcPkl60dRZlq_CVPOJ0hoCWZX7Da0PumS55hQHoctvBtEiaz4qlktG1nUnHVxeRib_RzTTTnPi69IKzpmherHP8um6YopdqblNKOw5aIsXqXnjDb3bDVYzB4zPFXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8a29e5339.mp4?token=APPzhk5ndpZACGZg-UD4Dy5ayB1yU8Hme-iHa0wGnZD6FJJBC1H_eQH_BxHCL6lRplsuLDYJ3lQ24ebxCZXy24a37bgseQ5tizY2ANqaDrashsGikCJxI9hJPouggjrYd8JqVjQxPdFgjjcS0Ulk6BW0YhX2vtexWP5EgLi6tD3suRjGkWrefyVlt-29PeXzU05kk4Ka4YFdpP5xrWDA9Lh9DAcPkl60dRZlq_CVPOJ0hoCWZX7Da0PumS55hQHoctvBtEiaz4qlktG1nUnHVxeRib_RzTTTnPi69IKzpmherHP8um6YopdqblNKOw5aIsXqXnjDb3bDVYzB4zPFXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
عملکرد ضعیف کریم‌آدیمی در اولین بازی بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/Futball180TV/102548" target="_blank">📅 12:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102547">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/233ef33c09.mp4?token=AOnxDC33RA_1PWs1JpxW-13tPCFlFAXaCoUeIxfpMMFxFfGBFSl7x2_25URN0R5Ok2uWXtA4RGDK7xSXgHzkDYPh1FRnyrvl3USBkaDFqRd2FRSu9Gz8dzKO83pm6eZBwUM1y4BihGdtDyGvxYK1n0CiIv_DCHzIkz-aKgAPMnIQA7wskY-PxP21ctWLR0cftKVbpsCfZtKpePdPgML476xNVT3oIYmF9J7HCp7U3zSvnoIyGZCtDnYGXzRVWU8lJwE6Gb8507aLfBoc6zzh_RapwaQaQ4fkbvz7vjg23UT2vqa4Qs62BHPtAwt6JfshcG-wNS7cLHjIg7VwsjCvDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/233ef33c09.mp4?token=AOnxDC33RA_1PWs1JpxW-13tPCFlFAXaCoUeIxfpMMFxFfGBFSl7x2_25URN0R5Ok2uWXtA4RGDK7xSXgHzkDYPh1FRnyrvl3USBkaDFqRd2FRSu9Gz8dzKO83pm6eZBwUM1y4BihGdtDyGvxYK1n0CiIv_DCHzIkz-aKgAPMnIQA7wskY-PxP21ctWLR0cftKVbpsCfZtKpePdPgML476xNVT3oIYmF9J7HCp7U3zSvnoIyGZCtDnYGXzRVWU8lJwE6Gb8507aLfBoc6zzh_RapwaQaQ4fkbvz7vjg23UT2vqa4Qs62BHPtAwt6JfshcG-wNS7cLHjIg7VwsjCvDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زندگی‌ برادر زمانی که لوگوی این لیگ‌ها عوض نشده بود:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/Futball180TV/102547" target="_blank">📅 11:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102546">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2090c572a4.mp4?token=XroAY9u-8DgYpJtxbAovszkiZuV-loKCtMbmlKgzvp7fA3xAiEo4ATiIaAgw-NI_ZuDGxGZE_p2nzzmb97T4wd9fwvlcRwxTkmhZsqu-OKuJ-TJNGjE4lGB0rrhouQdsdWVz5onQHgGODh_kDI1X9xN6nLcLrkoHLR4lHxIs3rAB_wGz_P-QBQqvUo9Vig3Gs0GzoZSL2aegpBK9SjcX-mA16h4fU_t879dNGXqFkjMPteB6Q0ODxKceKVlJ5FQAi3hOEhYDe46RlT9NCcJ0rJIpiaBjWA1jJ1aDOvelEmCxs_QwM7b0-mXOszD106saoSP4yLmkMilJg1xGdIzvXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2090c572a4.mp4?token=XroAY9u-8DgYpJtxbAovszkiZuV-loKCtMbmlKgzvp7fA3xAiEo4ATiIaAgw-NI_ZuDGxGZE_p2nzzmb97T4wd9fwvlcRwxTkmhZsqu-OKuJ-TJNGjE4lGB0rrhouQdsdWVz5onQHgGODh_kDI1X9xN6nLcLrkoHLR4lHxIs3rAB_wGz_P-QBQqvUo9Vig3Gs0GzoZSL2aegpBK9SjcX-mA16h4fU_t879dNGXqFkjMPteB6Q0ODxKceKVlJ5FQAi3hOEhYDe46RlT9NCcJ0rJIpiaBjWA1jJ1aDOvelEmCxs_QwM7b0-mXOszD106saoSP4yLmkMilJg1xGdIzvXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
تمرینات سخت و نفس‌گیر بادیگارد لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/102546" target="_blank">📅 10:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102545">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f010d3bc34.mp4?token=sHLKZyBA7IwEiSBJ9BXep9YZ9p3YMGnRYCfXBkd0bq-6f3Px3Rx6deDyd26QxbUaDq85MVofagixtMoZA0u5rrd63AgKDHhMDvAwdwypD-PMWTEEpiokA1nKgb4jPiCkUinIy3TfToP2JbOYoTV10BPPQyJH5e-J35hZeEuCOgyFYmTwvfpB-T_-9zEvdQP8TMd_iWhgFOU8YcJc22_QItBxkWsa-T0dDZgqQuzm638vWN5GhV4i_1tCf4PlOZcaLq-irAKw8SIsHYjktmv-U0BDP7CHRp--wFmBOuyG34awma5Yxwq0PyLBWdfPlKQg9DrRJQ4ODQMiJuIEOUNNrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f010d3bc34.mp4?token=sHLKZyBA7IwEiSBJ9BXep9YZ9p3YMGnRYCfXBkd0bq-6f3Px3Rx6deDyd26QxbUaDq85MVofagixtMoZA0u5rrd63AgKDHhMDvAwdwypD-PMWTEEpiokA1nKgb4jPiCkUinIy3TfToP2JbOYoTV10BPPQyJH5e-J35hZeEuCOgyFYmTwvfpB-T_-9zEvdQP8TMd_iWhgFOU8YcJc22_QItBxkWsa-T0dDZgqQuzm638vWN5GhV4i_1tCf4PlOZcaLq-irAKw8SIsHYjktmv-U0BDP7CHRp--wFmBOuyG34awma5Yxwq0PyLBWdfPlKQg9DrRJQ4ODQMiJuIEOUNNrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لواندوفسکی هم در آمریکا پاش به گلزنی‌باز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/102545" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102544">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a652d9a082.mp4?token=da_snm1DjMbDeDEx8bWfCfcMB53QQXAL4Knkp_eNGEd1PafEmimg2-3DZS7F7SaxY3dMpiokVknUUexauau0kpRWzbcAW86LqIchSdIZvD0E89oqFR1LW_-zhOKYPEpl1HoAFBdJfdHcWoFBcpadtOTAj4zfsgmeaxeuF-ENW1JVmVj51F0F1vut-h_XEKkp_CuiJ6PstWUAjicofHMWBmjV0rXABp-o6PcKEmnq0X8XJGljlJM5nRSbhYrse9Iv1f08YoUpjEnCeTMmPaQqGsWfEATaIFMB-f3x33J0UocVBobLqOCU6KE7QogZTOue_hQpypk-ti-7VGds8Ewkew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a652d9a082.mp4?token=da_snm1DjMbDeDEx8bWfCfcMB53QQXAL4Knkp_eNGEd1PafEmimg2-3DZS7F7SaxY3dMpiokVknUUexauau0kpRWzbcAW86LqIchSdIZvD0E89oqFR1LW_-zhOKYPEpl1HoAFBdJfdHcWoFBcpadtOTAj4zfsgmeaxeuF-ENW1JVmVj51F0F1vut-h_XEKkp_CuiJ6PstWUAjicofHMWBmjV0rXABp-o6PcKEmnq0X8XJGljlJM5nRSbhYrse9Iv1f08YoUpjEnCeTMmPaQqGsWfEATaIFMB-f3x33J0UocVBobLqOCU6KE7QogZTOue_hQpypk-ti-7VGds8Ewkew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
گل‌زیبای لوئیز سوارز در بازی اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/102544" target="_blank">📅 09:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102543">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ebf3b2b10.mp4?token=YXt4-0nT7LDHdfzKjkRWc2Td2ufOgF2fM4-eR1u1xQjyNrwJ0lR_pMBONntFZta5TthzbssuUgsT9v_CHPErLPAFuQIKPDmkGfw3LbqVWePIxbaU9rKIarkajV6c9-O_N2it-AqajB12JHg_qZUWjTCTun8OB0QXVwmwqj3OYVy3I-Xjy4tDkEKYlgbB1IEi6AA0n7SyQEapDZRAdTk6r9dh6VxZgjw26h1-vMYp_HaiuGM_c5Lw8NWDxCizwKgEckpNfGKmYR7YvO5nwDJvhYfr8worTqO7C1MRE4y2opUijLPECCgOd5SQK3C6P71iUQSrtGS8T6OfI9z1BG1xVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ebf3b2b10.mp4?token=YXt4-0nT7LDHdfzKjkRWc2Td2ufOgF2fM4-eR1u1xQjyNrwJ0lR_pMBONntFZta5TthzbssuUgsT9v_CHPErLPAFuQIKPDmkGfw3LbqVWePIxbaU9rKIarkajV6c9-O_N2it-AqajB12JHg_qZUWjTCTun8OB0QXVwmwqj3OYVy3I-Xjy4tDkEKYlgbB1IEi6AA0n7SyQEapDZRAdTk6r9dh6VxZgjw26h1-vMYp_HaiuGM_c5Lw8NWDxCizwKgEckpNfGKmYR7YvO5nwDJvhYfr8worTqO7C1MRE4y2opUijLPECCgOd5SQK3C6P71iUQSrtGS8T6OfI9z1BG1xVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
⚠️
استاد کاسمیرو دیشب گل‌کاشت و تو بازی اینترمیامی موفق به ثبت گل‌بخودی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102543" target="_blank">📅 09:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102542">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q59OSAtfrpCUVoTduRY2AMt69f2btWXtgTsWicBIRsiRBvbyE2kZLBtuHnBjJ4R3TMySAgRXHPEOICG4V9aGxevlSb7Sse0FUy6McXh5NH97S9DYfwJlvXKXb_-oKIo014lLqRawODUwk-LB3NA23CGjwobErFgpvQ6ku61OURlFLSgfVNUTNdNTm3_dpN1oHfgWTlI2LMhU0jZDnqgdby7pxCxwqW-j7EzZp7jtrIMb331sIj8rDYdsThpVR6Iw6QbqcvDVTAtgQUqY7gQe6ML3FmyhlOHz_r07Qt1gQ57WszTuDRcTBCkODRxIj60EGRIKM9fOU-ZO2QBz5drzqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
لیونل‌مسی دیشب برای اینترمیامی در روزی که تیمش به تساوی رسید، حدود ۴۰ دقیقه بازی کرد که موفق به ثبت گلزنی نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/102542" target="_blank">📅 09:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102541">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f4f92fcd.mp4?token=K8IznZSWnVgNFFhHNSYcQ50euXnqmlg7CeMIUtCfsHl1n9ctJAVlkW78O27fQmFOMeTOa1lrVBUWgFTB-sKCn0YKKSD75LKcqcaAw75gWB2VWLbyeG6lcq4iPRexAU5wqr_b2BjzHZpThfaVg1aXLxesWpSGhun7WEK5DxNAm7BX0vhYPBLCKkAR6iM0rP9EYvZ6ioP5a5ejdECjNLfv8dAoCaU8-UNlY9c_ecrzAeR9prxQOi2R2qhidRWg7-dX5daaOA2JBTCdkJGfZ6Z8OrA5WPoujQHAqe5smA7cDdmk_s5VqE7MvNQD8BAHXvhssRAYk7R3nJyI_Vt92WShEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f4f92fcd.mp4?token=K8IznZSWnVgNFFhHNSYcQ50euXnqmlg7CeMIUtCfsHl1n9ctJAVlkW78O27fQmFOMeTOa1lrVBUWgFTB-sKCn0YKKSD75LKcqcaAw75gWB2VWLbyeG6lcq4iPRexAU5wqr_b2BjzHZpThfaVg1aXLxesWpSGhun7WEK5DxNAm7BX0vhYPBLCKkAR6iM0rP9EYvZ6ioP5a5ejdECjNLfv8dAoCaU8-UNlY9c_ecrzAeR9prxQOi2R2qhidRWg7-dX5daaOA2JBTCdkJGfZ6Z8OrA5WPoujQHAqe5smA7cDdmk_s5VqE7MvNQD8BAHXvhssRAYk7R3nJyI_Vt92WShEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این تعویض کارلتو که خودشم پشماش ریخت و خندش گرفت؛ بازیکن ۱۸ ساله ۱۸ ثانیه بعد از ورود
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102541" target="_blank">📅 02:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102540">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4mqedJitNRF6rkZPo1zftI--9rDYWGAMGlm3EsVq6-1hFepkx7C46JgcqGr7bqlIziJk2NTM3rt3U1zxBXMrsfSh_zkVkcwLbdoEklnNQcKiApsok3XZ2N7BvAknU-S4HNp3ZkGvLtSg-dE4yFzsGCXB5A6BD7Edl5znpR1AtIRd7Dk98KXtve3jARVDSoyIz_102Ny3IsHvSgeDLKSlRSUT_wUXGEO-ZLYmXfUe_LiK6f160s0p7e46HnqGt1Y_s3A5ia3P4wL1OSQYmhfDJGWbY4EHGlGdymRAu4RXR8bKqPVyJLs5_dkI3QOsY2-NkpudajEDKUCFEUlrxSobw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
تیم پورتو پرتغال برای بار ۲۵‌ام قهرمان سوپرکاپ فوتبال این کشور شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102540" target="_blank">📅 01:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102539">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f4c2f037.mp4?token=T3Y7ldJ_JObOz7PCt2gVaM3qIw5QanJvLftxYBCP0xWxM_vv1eFHitbkL7nnCJ4bSB0bJelo2B4QvGHO500mDoLvKd7N04-UaCTlHCnlcpqZBoQS5_9H-GA0Gtw11megndRAy6fxBOVRSRGpzf0l3WbEDZcuhkIlyHkovxD4Ra3XFIAWCmDXG9mEXF4PNKPQucJHaLG3rJEOvX_U4FQf82QDyHWfAMpQDs9kYvC4mRp84ZkP_bxN8jgVs6Vi3KkAN5afOm3y6RqrDmIHlkJTwxd8Z70qt9V3_TdByOqAd59eliSjhXNT2zbmtVRJenFhBtzfEG6AUU423DR_gGvuyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f4c2f037.mp4?token=T3Y7ldJ_JObOz7PCt2gVaM3qIw5QanJvLftxYBCP0xWxM_vv1eFHitbkL7nnCJ4bSB0bJelo2B4QvGHO500mDoLvKd7N04-UaCTlHCnlcpqZBoQS5_9H-GA0Gtw11megndRAy6fxBOVRSRGpzf0l3WbEDZcuhkIlyHkovxD4Ra3XFIAWCmDXG9mEXF4PNKPQucJHaLG3rJEOvX_U4FQf82QDyHWfAMpQDs9kYvC4mRp84ZkP_bxN8jgVs6Vi3KkAN5afOm3y6RqrDmIHlkJTwxd8Z70qt9V3_TdByOqAd59eliSjhXNT2zbmtVRJenFhBtzfEG6AUU423DR_gGvuyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح برگزاری فینال مسابقات زارم کلایه استان گیلان رو ببین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102539" target="_blank">📅 00:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102538">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93530c3ba8.mp4?token=P_wd8NUSf94dEYxIvCH6OEai1J7J_EUSOiNsm_KNvMUlWTrg32R0BOiJdZd-ksgs7u7Z9z45GR3cTWCTk1x-UpFo9tIjW7EAAyEGYnctobZG6cIXju4x9q12te4WqPafk5h1uDZUJ724FLUh7G9ufyEdnxULbaoWOJCbKywUvCTUmjoWMTfdsgZ5YTuZ0TPN25iyurQk2pamuMNQWeHurTiM2IKlQl2hm7UTg69qGRHVuE6zwe4AfLmTxsNZ2UVQ_Pw2WnwUUf-gooNP54kdopoZ2H8gmPDEk4Y8h4mqZ09KzyfjScjsmrVqCW7dB792GkjXYxV_mzXfIMF3msCAqEqd7gdZbi1dUe9g6DC57gOecC17l_jXlF3Tn4mq3iIJjY-K4X6Gp0BEqBBSK3oNco7cR9l8w5THXER7_lJyKXmm7Gljl8x0k2vzVjDl8EbVeHslPns2ZS4VlhZ8-Rg6SfL4xfjxzGKv4LEBxJ6genSDPaeVqCk4VE7e-BQ28Plqr0Dlwpi2MHDictaYOXUYGH_mO_osDRK8JWdRWoumpi0MPtHuhYd5YYJIa0tTeC4Njj2tD7vyZa8EwhQ3NwPAaTkCStO5vGsb8VjR29BmGmZVkJ_if58CXDUzitmKWDZuWz5vmh9cARg8wDOO12J2A5JSb55VqPDlsR7-NObDUZ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93530c3ba8.mp4?token=P_wd8NUSf94dEYxIvCH6OEai1J7J_EUSOiNsm_KNvMUlWTrg32R0BOiJdZd-ksgs7u7Z9z45GR3cTWCTk1x-UpFo9tIjW7EAAyEGYnctobZG6cIXju4x9q12te4WqPafk5h1uDZUJ724FLUh7G9ufyEdnxULbaoWOJCbKywUvCTUmjoWMTfdsgZ5YTuZ0TPN25iyurQk2pamuMNQWeHurTiM2IKlQl2hm7UTg69qGRHVuE6zwe4AfLmTxsNZ2UVQ_Pw2WnwUUf-gooNP54kdopoZ2H8gmPDEk4Y8h4mqZ09KzyfjScjsmrVqCW7dB792GkjXYxV_mzXfIMF3msCAqEqd7gdZbi1dUe9g6DC57gOecC17l_jXlF3Tn4mq3iIJjY-K4X6Gp0BEqBBSK3oNco7cR9l8w5THXER7_lJyKXmm7Gljl8x0k2vzVjDl8EbVeHslPns2ZS4VlhZ8-Rg6SfL4xfjxzGKv4LEBxJ6genSDPaeVqCk4VE7e-BQ28Plqr0Dlwpi2MHDictaYOXUYGH_mO_osDRK8JWdRWoumpi0MPtHuhYd5YYJIa0tTeC4Njj2tD7vyZa8EwhQ3NwPAaTkCStO5vGsb8VjR29BmGmZVkJ_if58CXDUzitmKWDZuWz5vmh9cARg8wDOO12J2A5JSb55VqPDlsR7-NObDUZ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت‌های جنجالی قالیباف درباره لحظات حساس اولین‌روز جنگ با آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102538" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102537">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی #فووووووری
❌
بمب پرسپولیس در استانه انفجار، اگه بشه چییی میشه عجببب بمبی بشه تو تاریخ ایران
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102537" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102536">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FhRVZ1p3vUA9mSnKobfgjgPwwWy0A-BZ2HeLO5bandlWkyr9dwa66RGFgvz2e9fXFa2A5xvQn74nV2pgMr5gByA6vhB9aloXZwxMg7-jpQ5WbGRp81crj35kaldrCKXCBgUdSBt0XTFAHD79BACmJSRW8FzJbV_UZr0j4x2n3c9kHfhgwMTuCTa4pQSnH31OGr9ng1Yh4F-2U_9S5g1CHppXsaYIONcFsaSwLGXDh5M9PCK6CRcGEvOf4JqyFdI1SuHsJgy7cqHxhxz1K-zEdn71-eRPo8y1c7F9PVjTM4nIoMswAnvOcHkJqw2AtQpr7fk8AHu9cMHYRVNLj7hsKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی
#فووووووری
❌
بمب پرسپولیس در استانه انفجار، اگه بشه چییی میشه عجببب بمبی بشه تو تاریخ ایران
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102536" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102535">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f15b1aab08.mp4?token=jXgD_uzKAljLQxdVNlMfnMzQlARduqxP2e0tJYzKOOGFzNeycYkVoljzhArrDBr9J0_50glsWKrUysH_bQ5jJJl7NUyoGMfjdVncPEU7_DBQra759fLbO4wn-kKDX-iAtfxaC5tnpCRYjoczGGqGkKl6gYC_qLr-j3cDPPZGEEj809FUpf1cN9H8Da0rLwU3dzk1bDdZhskoXUtAi8BpSfDv4ChIuSvAk0TG0yz21AmykPhgyftHK5Kqy4ejmWavCjGZHN8WwtplBIgTnk9UUWclB1SEhpXqp-KvVUXi0rY_bY8wiK_D8_CNPflZnIaBybmMYlZw24zUUpPxf_Yr0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f15b1aab08.mp4?token=jXgD_uzKAljLQxdVNlMfnMzQlARduqxP2e0tJYzKOOGFzNeycYkVoljzhArrDBr9J0_50glsWKrUysH_bQ5jJJl7NUyoGMfjdVncPEU7_DBQra759fLbO4wn-kKDX-iAtfxaC5tnpCRYjoczGGqGkKl6gYC_qLr-j3cDPPZGEEj809FUpf1cN9H8Da0rLwU3dzk1bDdZhskoXUtAi8BpSfDv4ChIuSvAk0TG0yz21AmykPhgyftHK5Kqy4ejmWavCjGZHN8WwtplBIgTnk9UUWclB1SEhpXqp-KvVUXi0rY_bY8wiK_D8_CNPflZnIaBybmMYlZw24zUUpPxf_Yr0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاخدااااا از این سوپر پاس کاماوینگا به توپ جمع کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102535" target="_blank">📅 00:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102531">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JknzRKYM4_5KGm2KXs9a-a2LV_dApPxOCOrkSdKK8mw9DzaynicoxDSTO-EaeD_EJYUx5moPOdy5Zx87RZ9SYXcQbovq1sA9g14siNPaoTJl_trB2xMw3PyJr5Lns77eTXst5BqVauaVl4sWeuVYn5Va8Fs6c-Urd5iSM7uF1RppQ4rnV-gU7GIP-gQoiWZ2j_fDxNkfliM8DkYsrLw0tpdWv0HdKFwoR1TzuwbV_TZdIr1Pnk_eRllfIFMnLeZ3h5OfBu4Hw_y2cxDYu7mJPwxVKlR6hWgrxPD2i5uA0cuwgHfzzjCbkh61XWIny1V7z_k6qqebUiqwryxcgAEOcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HH4fCfzuLFS1Dxaok1vh5ogWnRSjxamZUbuNaLdIT0bvgr9OTV6hwl8z9tJK8aPgpILePZNGbfiSE-dvMnWIIdQptnnFD40jk7NQbEpJ0Vmyn7JfZESFs8JsGhABX7IxOx3w6K7NeB9PO_mnsiCn03zwFW1YZ6O7cUV4cNf9F3c9HdWEX5HGc76MGZPU4GZaj1lIeBW0cYBcvzQgEn8gskWYkZIM3B2AftbLe1wx-mqbkU018gyB1p2L1TDjfPVHRREvp809ZrIWF4J4nxgMeRprgy2RTxiQAyIz-PpNszp2M7qQSkUJIGpx_2FeuMdeBaOlAEbZ1Wl3N7r9aQ1CJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYzDJktUan2Nrwzp4tB9NQ8mT05rUxh1ZdExUzWIhRijwyp7Zp6etjZjmPbT0rtPrUQcLxQYA_DP1AQBEbrbngtfCjUfWRcBj8iNdYqNPmXlmWec5XuQXa0TSXfESfNA8deC4FIQpWKHx7t1YaIq0XJcxt0YACbkweF9Y4kMrVgm2kVB-3zqItkDPGWag4umywRn5my65UyXATlZrAqgG9Zc6RBX8RUvk_cH93qFBlmidsCJb9f_3Fc3-Mb4x5YJkG7s1csTZajPcP2WaOT5g3FNSu2xbF-4hKs1a8Suum-s65qHxmBZYBEqa9ErToWK0i0ZiF7jwMmN4yL-IALgRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQL8tpikhzUyf3yu1vuyPD_6M85a5LZ-hmoUkVbw1dy-D_DD95WwpYPtotTkXh6lwOdL8cDtRJIVnIDtWjIZQSBsq7rA6xrOJgtCB3u_VljwLqwbQTeAE9MS76VDhSTvYVMplmjooaRuWvhXvp8YQXrtG9bjP5CPIlXjZF9SvGje1WMQVqWMbUkJzFnbhjrOxoe8nSBHeMPFG2BjZ_1cnFYoSlS8wCr4gXxau9Lo08ELtWNYgrrwzxd3E9VhptVOKiXJpBTFbcHVtd40p5_3oecO-r9P5Y5WkFf2gwtoOprGT37NG4zyUgajkGcpOCIjib4W2oS0AA-sG1kfM7cxRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
عشق و حال وینی و بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102531" target="_blank">📅 00:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102530">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twqWlLkXVmKF1HQFMYrOnd2M8-fpmV9WSGyrIMl6hGwsBLTrn6zG70Djl1EQrcNolES4wCcRvXg2eGr657y1dtBtL3nxVtTOr0tsD5Es95fg2BvsMDrnImOIkHNARe6vD2uLjtk6nvQij2YXZuzawRhLXXf3u07Dc4vsbozYmDT_o1tmmlYpIe3SZRCC51MA1frdZhX7BhBGOgxe8fa6ECoBSzc28x7cPwhUrM6koOO-Y0wedvytFict-PAFR-LjWItuCJtWz-1awPJB8U2jOAtj9vcf843JWQi982sSWLNMrYaNrGw1z-voNym3zt6Y19A8mY0N6zz8mV15s9CfPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
مورینیو بعد از مساوی امروز.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102530" target="_blank">📅 23:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102529">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kox515Y72BUGgFGGtEmFNSzZbDrjvWxSK5rX-YSopoZD5N7Fh5amIHuZ2BjRJVyP-1d_yFQVx6Eh9QNed4JXq7T_ax_kUNB3nz7OjhpxXyhsLkBXSOvXIKGrkR6fS2Gs52MCh0G9UC_KO4soAmzkDGW50VSMPr9uB8T03MQBYHlUgRjIlkMhq8rN5ulvDPQTPmwEoH7ralFi23CdWORQ8nU9aSw-tU7JAYj4oPEYFjJXs8NJ3zOFs0sthtkUfOxb_iS1JghscVbGoeMRLswbcEErsZJfv0l5QHAqRkjcH7P1NPWOUuaSP1xTkm_I5DWAzDeblw4QBKzu-PgENQF_Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
تیمایی که ولبک در اون بازی کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102529" target="_blank">📅 22:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102528">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRVqbnNpHD82jytaMXYvPdEMMyjlnOVqez-NFRFrtKB8REuqGqT8D6_xeAfJfnqaXx3egKW-iVpUBE08_Jb0MvhG6AtPbZ96Z5DKSBA4ohfWfzbsGCBgQ9UeL5b2_Xsg15m9dxWheU-na4FyGCa4lW6gj5CqF_hQLOmlt09KZW6OU7BXB1A73SD8DakWUUOCHnolDco79YxN_Znj2ThJMz0tJRBkEvFhpjWybHzukctKwcP0FlswGoQZRDC0VgHPaxZskxVWyOYFO5qxQkXlBt5vF5-lrgHEAjrx6Jv7tsNpCMzCMCrOiH2mjMJGcwShdcNvPGAG3l7RQ73Qh_dPjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
رئال هم تو بازی دوستانه از فیورنتینا کامبک خورد و بازی مساوی تموم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102528" target="_blank">📅 21:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102527">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRE_f7iurJeg7UcLCDWdQl7HyCsig1KRk13BAUCRiiuXU7mJpdnR-dmJej0olDVOYd3e1WtcUkt3K0DR_vV77uma7jBKwxF9fYp8bINTyPaf-3w2Q7DAOItV0LRuJXeBrJ3qa3qoaGzZTbkQAiGU1LJUHlnYqbn_6BU7NoXaQPSzMLgKB8o9pz_LpWou605CaQEtKRhwaFLtyE4kEY9ggevURgkCWXu1LK6GtrK99RsDEah54TIzLK-1D1C8aQNrJ6tJYZDrSS5bk2ZcW7TKAG79ZqfZMeEPXToWf0Fc7ZI21CqKa-jLS1qXl6KBLGRwzPHBI1IMqDIlRsJ10iMJFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کارلوس اسپی:
🔺
پنجشنبه: بستن قرارداد.
🔺
جمعه: اولین تمرین.
🔺
شنبه: اولین حضور در بازی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102527" target="_blank">📅 21:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102526">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEnPaJgz3m16Vbtf754c1LGe-_CKH2KRjk4YV6Yh5NeSBqt30gkRPkVC2ugjVE1EyfVqNumHcYXRs5-cuqNIDAgw0vK8wl01VcxXNBRked29UAh-7g821rTliAGZlXWD-Pmg3pfAE7gxdcq7LvxNoM1i8_DlfNJAzmftmv7ZgetaGZSG0aM1-6Y7suXwkuVbcf_c9ooI26gMy33jD6Rxy3GfFzDD1RDfT95_FCMaB_eoGDIXD79dfJ1cm6C5YhOqDAMMP_prxIYEDnMpxLPa0PGi11MJKn_mKX-O-nYchJQg8jctIUENMkPBAqNPim-IgZdLduqU0xyhJfNW0UAmrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی‌دوستانه|ترکیب آرسنال مقابل ژیرونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102526" target="_blank">📅 20:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102525">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpLdDLned7CzrS_MMladjmqit0-LdwOVRcp0KaHAFWW8qRDsCG0D4Uq6DjNFGmekvc1OtKiMIx7EpQFW0r35JmUkRQPYELwztUec6OBhtYh5rcMDrjHgVy4nNEM2Md-8taupAe7kLeE3bbzC_KbHVDpYUZqE31QeMsliqOPvU1_uNmR-Gr4YJGc-AkPJDO0UUY-gRUKcK6WWYWcLPhqe_r4HjHYdjk7Z8lCxSSzNucj3vYyvith0EmrvWo8O8S-nlXT9tyO6jnMLnBUM3z7tupRNfD77kl59HaPLx2DrRr5I7q3KPOV0GzFJx3Py799fmoiRgMEUS1OPgqDZGHMVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامبد جوان با زنش چیکار میکنه اینجوری شده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102525" target="_blank">📅 20:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102524">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jl1uYlRzxyT4LaYjkNF-c-hYYGHo9f3n4JhvqGFg1KOsvwfg2mYvs0yv26GE0LcxtPIqvO_5wRxXDG6YQxh32rf61vgbBNDI9I8gW3Z5mrrl3Lw-U-Tp0M3LomiQGg4BOqYnhiSWmsDlCYDDz0y1Aeh76Gje9h0wb0UgGGax2w8qvLJ-HnEX_6bbUv-huz-SmoHSuBP8AT4xztaeATtu2VqiKJjWfCCpVzL5452sufIVJve3zC3yi7DUELxqtiKesNjwtCaccyIlsH7Fq8GnU14QlNhiGkKYDMMRzZxGB_SOBqtk3ZEhXizzTAjwHlC8Q8oayL-qrc67UVw4BKE9Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دنی ولبک رسما به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102524" target="_blank">📅 19:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102523">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glkDk1TpHpEH_xI-sRKyRRbYSdVAPGvp5uZhuaUjCA0Ni01uV68MJFhU96aInrStqNoKPKOhhFq0eQK7i2l9sK-yhHg0aUMNSyUs-slpmY4HeTUJrXvyDG1fBcg5tPXmrI6oeZmO2OQZB7haBDMKmDGtkPNXSP_mnusiyfxLVdB_zMc0ZMwAeGRj_j_bawtAAnkXc1u60CDQ25WKO2KsIGimlXNFBRNoPAzQDX6cF4BdC9a7jeJzqk6vvfzVh1fkWy7a5l98Kj9NlTx7nseurKkXooGPjghwKdNZqfKEUWPJwYtAKm3M5GnTDL8CRSq2AuojX481gmm3LNeb0WHCAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بن جاکوبز:
جایگاه اینفانتینو در فیفا بشدت در خطره و احتمالش زیاده که برکنار بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102523" target="_blank">📅 19:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102522">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFzJwqHhULAWRh4mjkvDg-mSh8MZ5CBQVM4ZuC7ZXAqMM4waIbq5heXz4ZCS5_yxzy1tjmqb8Hji9lM9yOVadbYZAltbD84z_7CeV--3EUDQ-jVUsiWGJXfxBVnnYVqtamQro03-r8ZAagzCRSxn2VAo91E1Kp-AedJlOkm5JsjWXtH4FJE1jPZayj5eWUESHEKEpmPQvvq-pDTMy4KI_ojeRtnDSchjZjRly9AU2vvfIWODFWF59xcHFufHFetmj7sg1lvmo7hdc8JUJNuaglaT1lGd0H3p0WWdiSoBbNdvcSMwk6OLt32Ll8HawAbMmmXuGZ1MWPOHiarodDleBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
🔺
انتقال های رئال مادرید به آرسنال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102522" target="_blank">📅 18:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102521">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aK3mt4c64I8ukYlsSRD0ghwoS5vi2dQtRPTmeoA1x1sVuJHDbqezeR0bYsq72FXhMiIYcIqo4wJrzLg70ibny0xXo-QKdOntZHQzTuXKzvOPKecHn9q9WaJHva1DcMQc4VDHwctheG7s1tIKSjsSCuGZxHqJskIcZWi-ys_3__B750lS5k-l-a8z_HjpEScw6h7OByq40zVac8VH8EgMDh9yLiIGIcXCsmZTJUzSvIeGg46r8WWAB-bnGkjzMk9PvzWfW9YHWTKIh1IRzetJSaW-AeboA4no0Q-LeAVrKNxlAV99gUkh5E03CuS8AGpOIP7xrgjyqz2PWXdDFOWAag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مقابل فیورنتینا در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102521" target="_blank">📅 18:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102520">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHbGciny2o4HtLespz4FhB8Y5pJIrPAV9O2yhc5IF2YCe9oEobjcNcyiycmtPjAnjC9PQrRoTz8F88rT8EYdYCRpW_nu_0Fk2g9CwFLTOTcWrcz3Z6zYCyi9WqzeQRV0LGEedEZf1R7ikJ45bm9P1PR4_tFEWWlGGltMTGM24lN9vRvf3qjtUXxAKmeGdW_4HDYpCGaU83Vv2eGo5ssP-fZA0FkcdS2nSIB9t5YDzP-7dQP39ga2CzWJtRy3XvRSiyhVbwzFcm5MKMrTQwHt1O3WPIeIw_mYIGpn5dqDxHy3rdoPkAbO600l9fpTywF-I_rBFT081gOrY-Zyin3FfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوکاسل رسما لخت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102520" target="_blank">📅 17:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102519">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDLtTZskk0arUtgRSQDD3Ged5rlHNDTgTowXMFpA_sdJuyhuEY0GYYXScMfnZitTqytHGpp5KHMjdtdKEOZJQFNAVaif4EzJjESvqy4yHGP72tLNQtrQmkXIuo62rF058KoATdrOyxsM429SkQfSwDfGDGyIvp_RzfLgspb3Y9phW9mTBuisehbLhUDMVGMhFC9xEO9JSHmsSxv94kyc3IB7V-hBLEA5P4S9Xc8_DrUnHHkzNAgftil8ta3UiTz4_LGAuizfAnx8BRMII6F3sp0Z9GMODKFrGDGi-yprhalo2c_h-S9h-5yxpeytpZsDi76yQQEvXDaymM-vFMajaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
چلسی پیشنهاد سه باشگاه اروپایی برای جذب ژائو پدرو را رد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102519" target="_blank">📅 17:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102518">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSTe5GUpPpf36_5jQhP8745vJLVaF57zuojfzGkbXRmgI5YzLacmSCxsiR16b2PW3lLkVLvm6RgxL5s36Tqzk1lqEnRvlUo1eUwidvhMmSnEpanPd4diDL0Rx3Og6OdaJqabekdc2_rU7cb52qIUaT1ZeYHOXuC8aD0oB5NGoMvxusU8ofM-iIstOq6Hibxbi7WblZv810pSaCYGIMiVzmDf3-kIIoK1C0j4d0K2B37EM2BTZ233VmewSsXLIZQYswrENwwbDAdPh6ILJ5wiA3YRz5uUFatoI-qlEa4m6QIO08HPyN5dAJaIYjwh9ox1Yxg5XHR0OmTn-NxxIbx8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس طاقچه بالا میزاره و ممکنه بره آرسنال؟!
من یک ایده دارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102518" target="_blank">📅 17:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102517">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb462e454.mp4?token=Jx5uPb2Nyl_48mk66BoRJeD7YsjMeNd3W9kDJp4_4glTi7Xzh9yPVrkr6MwF2oqgs_EBThO4KlrRQULCu-Y1oXPScnqpoJlNQll4dA7jSbt3L3Tunalef1Oo4cbmy3YL7GWCCTJC9H0dPznSMV7s-ukKlD3LfTEs6HF9Ay2tIH_7BmAqW7GB3GlenEmH9AgNrqcI0NTo_RRE4MB5LhwAylLslLu73UihjIQLZKM-XKPDRkR2bEXlXgdPEbp4sx0bVm3IB8sWXcg6_58YTU5TcXJio_qVQ-TTx5-pPCxHlnJXr-c1edIETTxivVprrIBsEkUPJavqVjJNeezOKO7VgyjT91wW6SSiC9v2PfrKyo7t2ywUe29hWjEfUCchfHhRkSna2gQhdLKZacEZOPu-qICnV_8ziebjPW89r6zzKJMXDm3BLqXW7f5sJ-O9Dp37dKrnJZNxUoSTzo2H1ZZsf_wryuitA8kQcP1e2Dt90C5eP1NAdXecDipDzZ2Nab-b4_lPU4Ic9gTVSwrA_mt0WnEnjCrUhwVklFUGMaVIIVZLfvSLazbtiO8fpRIQc_MXT91ZMs3KJZp_3BVWVyYlXjUBy0W8gliKhaBCGcTXSxCHyHPNSA6T1SUlpAlSwPHmKwz02eXL1bF5V38CfaRf8Q1jaDlsIB6B6McIcM7JmDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb462e454.mp4?token=Jx5uPb2Nyl_48mk66BoRJeD7YsjMeNd3W9kDJp4_4glTi7Xzh9yPVrkr6MwF2oqgs_EBThO4KlrRQULCu-Y1oXPScnqpoJlNQll4dA7jSbt3L3Tunalef1Oo4cbmy3YL7GWCCTJC9H0dPznSMV7s-ukKlD3LfTEs6HF9Ay2tIH_7BmAqW7GB3GlenEmH9AgNrqcI0NTo_RRE4MB5LhwAylLslLu73UihjIQLZKM-XKPDRkR2bEXlXgdPEbp4sx0bVm3IB8sWXcg6_58YTU5TcXJio_qVQ-TTx5-pPCxHlnJXr-c1edIETTxivVprrIBsEkUPJavqVjJNeezOKO7VgyjT91wW6SSiC9v2PfrKyo7t2ywUe29hWjEfUCchfHhRkSna2gQhdLKZacEZOPu-qICnV_8ziebjPW89r6zzKJMXDm3BLqXW7f5sJ-O9Dp37dKrnJZNxUoSTzo2H1ZZsf_wryuitA8kQcP1e2Dt90C5eP1NAdXecDipDzZ2Nab-b4_lPU4Ic9gTVSwrA_mt0WnEnjCrUhwVklFUGMaVIIVZLfvSLazbtiO8fpRIQc_MXT91ZMs3KJZp_3BVWVyYlXjUBy0W8gliKhaBCGcTXSxCHyHPNSA6T1SUlpAlSwPHmKwz02eXL1bF5V38CfaRf8Q1jaDlsIB6B6McIcM7JmDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چرخ تو اکسپلور میزنی میبینی پر شده از کلیپای عروسی ورژن ایرانی رونالدو و جورجینا
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102517" target="_blank">📅 17:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102513">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9mPog6CqJWD24_nDW0t33EgqaNDkRe-MvIEKqSIqiOc0IFz8L1Z9zG1tLSwds4igbXmL33RpwsBm-d6iaR3J5id3QbsBmBeHartAqaZX5s_MlX0brRsCPadrmmPTW0CK5R7s4wfKDZqcFv3rV3jiifiTTE0Pjtau7SlgyX28w83iTRVW8OP5I54aHHPmHC7ghlHBCA9TBuHQDL5ezlUnfxCm411HBTvpKYl_QTPtbVtXwzH8Xgeq-bJV_ZoOkrARc9LhB4fyomXuvso7JxN2jUi5dFS7JTvgxWlMTk397Vc_GhyKba0TAWWqTian2by4uXew5LQpS3OfloyUFaI9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/et96n4ctRLLvGR_7CTPF97BW5lp2ZDUzRG-KaQANdhDWICDuvSrQJdW5bIE--bBD4wsU4iPKlkhtnT_155WvQXd-RQESbam2hvs2tAAfA00H4Cv1NDbAoT6U9HnMbyAK0aQkx7PYszDQSBu_K_ayFG1WVqhL5q-Wt9AV3gueQyHcGltHjeFAJTCvCLG_BPpjO-NBNktrlHQmDgUw6rpec3BlyHxvNQwEG3vqj7Mc06bNsQPREQLCUUOo88q64VylLKNooMBSULqxdkrF6UEEIVzsw0hb3tZn7aCqH117gAjx0abtWb24MibNYGjk_RKgW96DX5eRKFgY7ZDsK4XmOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z2zxW45bJ-6YE8gVkIj46lJZSheQOEY0WA3VtNyw2fDfTtrnI0QIEHZwTcDcndeLIVBLzcg8jL3ZdyDvgMjjZmEBXSyGgmku0_X2boZlqdIn0BPjdZI0i__Su42zsbb6IM-bjD0s_nWpxJHRCZ2ezEYfUJIjgVBPLn9ZsSz7lntTZNv-HtUljoT3YXouU5yEBzAzuYpPVDuV3dlVK46avhvMHOY_GwSBOgkcwtI476nqwbINrTB1CrOxvyqnV_syBjbTg9UhH0f09G56D3lA5BLxoi0wJKLnBsYwTbimDzt_gN8R-PkWEiYYyo_VJOLsYnWqWbZK-OiUXX-Jfw44Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l61Lkd8Uz-GcPmg-QHGLj23gRPH0XPKsYSTpMCe5_JK3nnMDswdc-3eRYccL_ibp2IQwkKIp0h5XbW1a1MN2jUH5vDm8OhHPPgJzYcVVLGka2MmDEYXeXLuq1RsDlOfPLxK8wPrfz6ob5BEq9g4DFyy1LFvQENqktkzyih8a78G5hEUI-4GTQ5wE7wyhJQUOdAwRpzMbULwO-ciW18rNy-UMGmCaQm_sfOjdAgVlRWN4uVOWfo8m3gd0AwHigP7QM1xC4J5i4ialRb71d9GXxWB6Kd2oGOLSYSbwyHxwukEDg_vca4odq5a1M_YjvcH4eEa9GMDa0Ornn6s5gotQDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پستای جدید جورجی جون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102513" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102512">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LF0ozzzbzSoPRX8D-DFhceHe4U158gTJNqe1q0gEP8nimrbzEua6XoFu7kC1uBf-_5cjsyYwXrHJH5b9y7pZR2ZgaEdBRzwTNZaa8zWEDz1hOOxT0LVjfPQZgH4Xyc1mucCkI0TIuL3eugFV9lBOWvT43nuQKmBBsdXhhCUCexmEqhSxCVCd1VpOfcbCza6OlEMBNBRUN6_uAclh1IpHV7NBwa9IcshcNsliLBWTmWZdZWQHLpmoF-dsc-H6wpEiTq7OssVi9rCitF3AJvs6XTr9wtsZKrT0QdZ3HhJqcyi1PBjtMYuV8DDEZPQlGmtxgk_nDyHice2sEaH17BAijg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔵
اینتر با نتیجه [3-1] در ضربات پنالتی مقابل منچسترسیتی پیروز شد. بازیکنای منچسترسیتی سه پنالتی رو خراب کردن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102512" target="_blank">📅 17:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102511">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f1ded84b.mp4?token=vKrMMnb0bUQgs82qoy-dIzJU35G2R4gW1OSGZXfCKgbD8uJhZDVmTXWXLOpaHD_YnIXKDHSN5mRz_qpZe8w3I9Ed0UC3vx-fzQhIPNbdefh8jSYKRFAS91rIPDWyM8V2PPNxipxNhf1HylcXdgAbMqEqg_oXtRYelVYGgL497yGmVQJDqM59fMOQq5OltA6J4QfAWiM0SPCdnU1jgPq7pGT-cX1M0sJMD7pN1Gp3AKC2e7iNP_j9RCtIeWRmC4j8uM3p5ZoA3m35rOTbYBa8LOZ1PnXIkErffK_l7gvARV3yHK9lCx5jX19hw6mw0lhiXNAxz2vqz-IbPuLuXTZFEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f1ded84b.mp4?token=vKrMMnb0bUQgs82qoy-dIzJU35G2R4gW1OSGZXfCKgbD8uJhZDVmTXWXLOpaHD_YnIXKDHSN5mRz_qpZe8w3I9Ed0UC3vx-fzQhIPNbdefh8jSYKRFAS91rIPDWyM8V2PPNxipxNhf1HylcXdgAbMqEqg_oXtRYelVYGgL497yGmVQJDqM59fMOQq5OltA6J4QfAWiM0SPCdnU1jgPq7pGT-cX1M0sJMD7pN1Gp3AKC2e7iNP_j9RCtIeWRmC4j8uM3p5ZoA3m35rOTbYBa8LOZ1PnXIkErffK_l7gvARV3yHK9lCx5jX19hw6mw0lhiXNAxz2vqz-IbPuLuXTZFEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اگر پاس گل پوشکاش داشت، اوزیل بیشترین رو توی افتخارات‌ش میداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102511" target="_blank">📅 17:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102510">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GK8fXXuEYGP_r2-UEq176jm0BFwcZ8ygKyjH3YK07C4UdzdXXZYsaNCK8_AvPJmOP8d1BRRRJTpcnl2DqqDcasD4z4_bs3yy1vlHu9D-9_e9ltwYxuCwJBhWbxVRXOyCr48sM_pfr4NyzC1R3C5oIanTcbuV4TWHbFddGPOY45DY_L-D39AgyYpuRam43CHW-HDbEutFkxMq1eY7M5yhRmiCEmFzHxhwEQ2oMoCv5Nc3YJn3oa6Cv2guthKF0-6sntIxShL4q7A9847JtVyb7nGOocEgp5V2NrQFArmaWMAvb2oT_bgKwclN7dpL2OlOUHX8SK7XClsnI0-EhbJAww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اورنشتین | اگر وینیسیوس با رئال مادرید به توافق نرسه حاضره همین فصل به آرسنال بره.
ماریو کورتگانا: آرسنال ماه‌هاست که برای جذب وینیسیوس به طور مخفیانه حرکت می‌کند. آندریا برتا، مدیر ورزشی، با اطرافیان وینیسیوس گفتگوهایی داشته است. چهره‌های کلیدی آرسنال نیز به نمایندگان او اعلام کرده‌اند که او مهره کلیدی یک پروژه مستحکم خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102510" target="_blank">📅 16:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102509">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzcNNldFcRO37RtUz2tcIwp3nSSb9hLmeez-FoGIMHSEkWnDSm00A6LTb9kWagrmPvN8VHRUataONxhwZF2RXETRRQgyzBtNJ7Fs6Lz0ON9EIbReQfID1w3c84_Ix3vcxiecx0DW7N1s0OXE_auB1icgfP314sxuRgwpLikKNbmPd0gfyb4g4jUlFjDiS17fkUJtchKZSNKZoZawFX3dqZAycmIVqXmR-6Ucx5US4WaRoqSCCeM6RUokzWiBkOaXP2FJOLgBZzQ3mmv2f6r2Y4HmTLg_HoZfbOqG-ErmJG7BwWF-UAKXrORN96qi2jRTreEc0PGsBKutmNpFJZa-XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رودرا - ESPN:
طبق اطلاعاتی که به من رسیده، انتقال یان دیومانده به رئال مادرید با مبلغ ۱۲۲ میلیون یورو + ۱۰ میلیون یورو بند پاداش نهایی خواهد شد. همچنین انتقال رودری حدود ۶۵ میلیون یورو هزینه خواهد داشت و باشگاه در حال حاضر منتظر نهایی شدن انتقال بوعدی است.
⚽️
@Futball180TV
‌</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102509" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102508">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDK3XyaCOYOh_Nki8LUYkP-O_Tsa1meXZRuVmd-3dGDNztCiJrpJ1zDBGnauhPFySh1eey4UZKOEcyZqRLZXTL2nQ0fXQGDPxlG-86z3VXjzByz9zT6_TSNwlhQ0QBU-IzRACZ6eYA8xRNeDVVZ-Xclse_8mp-_gDO70FE6bu6pcDqimSMcFqlmuJvdrOHbPUrtRrIdWHT0HPv4sa6E35nAgGS7F8yJ7aTAfA7o1VaP3q_WlgjCmaKfgyBWGlYZHmPO2qLGSEXYxOCf5O1aBCzoVlOOpfLC-52cbrFqwMuXPwgDnbVdoN0wg67emi950zvK7q9tQhQhnWj9O02GpxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین شات از عشقتون وینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102508" target="_blank">📅 16:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102507">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qC3NNI4nfvTJ3ScMGpePfWP_Slvtaj-3lwdfl-llb7agLlRBLfvh9q1xxhrTwcnpHT8ERkwqhEptynD598-_KzveJUjw0dRwLWPB36ROzQHr1KwSJZXZLtI-hbAi5cBLOdHbf2DLhFI23bhzDOu0U7iyybMiHgjRbtwtnlzt1BKy5LtNDGOzFBTcLvwkwemssK54ydRsz3ijCgjsm4Ca-OAklRSo9zfMGtO7VshmSeVUyhhdoTMZ66Mjm13S4VW5iOeRe-FF0ENWLhs6S8AMyxiJ08aijYarJz2_7Z1AX6xqf0AdUcHhfomRnZxNcpgs2z5TX2FGlkGg3ceQAHvNpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
چلسی در یک دیدار تماشایی موفق شد به تاتنهام 10 نفره 2-1 ببازه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102507" target="_blank">📅 15:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102506">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jyh7qsz8SjN6bgz9iZ7R7fth7jAOOfZ2Nm1N2iNGxmi0PfsG_MAt74z7N1uFW-DEqTrTjqiLnp9mODbYhHcasGrePxtqE6gK2n6knrz_n7N-_tO7BBtnpJIUYvbppve66AgUKDzMaZIkEpv2Z_G-pZKHPfwixejHFz1w1kIX_O30ckr1iB-RddZAxHw1iKTxclU5ISYUEFqUI4h9sMGCQSPieoVPQUAJC8IX9Xjziz5PH6iqvX6o2Bk2AFv69BtOiCEwsLWqxds8iIjRGFtjd5dljvq2yDSpHMjcuVwtWP-il4yt3ozjTJAwO9YxPzuVXhsNpWL-JstNMZ49IKULwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
تام هالند:
بدترین تصمیم عمرم که خیلی ازش پشیمون هستم اینه که طرفدار تاتنهام شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102506" target="_blank">📅 15:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102504">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a1fTku8wXouns6Mo_HDXaJEzmQaxqI_1vWgkHxiITZRzBISgpPmErvuYolpHQlAJCaZvY18XE8btor6ZtH2ZjoB1NQOJAYy01m73cxXnO6qZmiiQGtWQi-CKtByFUKS60mARMXdJVog6Xjh5haUcBa8_oOL2Uu26rklt2AnL3rUYrhTQT1o6OtNHLHZMyyu3ZGvxt1Jj7zM1g1bIzq9rdZfqFEk0XRORq3fqLAvrYqSISJE3fIy-l73rZjUXnhpQQv5_tFU_WBHbwewvwloTsGh2oSYaNlxliFW2G-cCfESsSbUZEfYQP_cZ20918UAPey1VGDv97kzU9QdDPFloag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c8hRvbnrxQ6JicqOV-REYPrUXFHeTGCbT6aOGmaFD5abVYlSqRZreCk981cRB6GRBcg3EXrhGgMJzoBhiJAbaU-uIO7sMM-tFQNlVOKM9gDb1u5HZC3sKd3C2IrEwwxK_EWSluI2vf0JytYTJfkh02SQpKelu_mFiXcs8lDg3QQ9EKTsNrVkKlb-uz7Otvu1e18Arj-SEYfzB1c3TulZPtk1XaaB_Ha7qESiipxTnnRx6PeCSX3t0PebIrjIv_yDOzP68IeP_C1vyUvypl9xqaIk9kiq_kSoh7krSHKt5rADd3mBbksFCVYLiW5zpsK5gfMD68Cdbh5P3CAJAC8Wkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
یه پستچی رفته بسته‌ کوکوریارو تحویل بده که کوکوریا نه تنها باهاش عکس گرفته بلکه بدین شکل یه عکس هم با مدال جام جهانی ازش گرفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102504" target="_blank">📅 14:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102502">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rySRZayF4adT-0-oh0JNzBjdI-FfAX0BlTBHthvJp9cQ-gFIqmwEKXX9hgkBKRMmZB4HIPTKGFBx_Li_95ZGmEaFg1u-EfuhpLnjDWq3LubQDz-KSyfKFnwa4Z_EiVs1FhbwT7m9IE6nKit8MkEIwpSM9QYzY5O-s2DJXD-x6vW2yTbfNmd2y5aGQ8JnmiLBO7_hCKZCorkIhXBnHddkhteMmB2lxvg5o0V8MJFE_OripxdOY6eNmAVqPxibxuanS1oTt-taDukTl7LvyQ1lRUdie_Y-EI6R7V12LGLJNtU4RArqb2YUFAlbJI3d2B8Q5_BoPDanFrzdSESHK6ol_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Du80yLNkx_Q7p_wgn-PwHpOhnBWTopFUGhaKxi59HValggMwMhz1eIu5cEcm5Jjr9ziGAjx_hUemx1_mpphuRMxtpbZ02bMdJKaQIcUC7Rr_xnNvDqu43f3UJC7lxfuNzIrBQaN6yaqPTTDW_AJ0rRiNfjvfFFvmaUHstColpHQFz6FXjmK1vAz9_St8DsC7eXEE8nRbtuJGyTU1H7lXXL20z_sruyifNWcQ5rBUH2x6fsPqlihW_dwUWXuKSf9VxTdzrhzuYWRIs_hY2ZYtfOAFfkBC7SzUJahtX0gAOrRsE99og_DuSI46v9f7N-jHBXHU-Vf0I1f_EwSIDnuINA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
⚪️
نقل و انتقالات بارسا و رئال تا به اینجا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102502" target="_blank">📅 13:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102501">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaXnKbdocshkc-On-fxFtgWsEX0lgOCgcDWVukQjoUhwoy80Kf8xq9jzO7uJNNp4Q2CtftxRP4ZnTZXA6hOZaEi5Q1aFnonxOPLGUBhSoSDbwIqI4T8vAwXqzi0KrnqVoY33cPQICiJEEcuJ1Wf-cIC0OTswrIJSPul2nvjJfEC5BqcrjGySmoYKCD-0SgXBscMJojNZOKoNfFjWWqUgZqnDNM1RAz9C8UZ3WdntT11GJoYuA0_9CFlDziyiBiuLknYOKqQmNpzANgulAiqD7W0TOdxOVOt-MaGv5roo4_S6vDYshbUjELFvvUF7bAEMD17qtytw2q7Fkbt_bm1jwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رامون آلوارز:
اطرافیان وینی هرگونه توافق بین این بازیکن و آرسنال رو تکذیب کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102501" target="_blank">📅 13:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102500">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRzZowdkKBn1EreMTpzXQqE30HO8l4T-9pzuvKrhLpcTmLhE5Ez-qAq_LNOXWXh71xknz74j1Z5JpOImmY-cRfWdLh2K40E7yYMXS3tzcJ-MalJii9M1Ml7cGIFc1peoyk3GdrsKTnzMfTB6FeijP6-y_BjRSaZ3QYVZWWrHEGjA9r3beZs9458puyGt0L48HB5Wy4ZB_kLvOeTEj-Z2VL1Wma9oVOE4jPT4-piHdeILGd1KtiWyQ2rN0y6_8cCmcP7utjOP04SN3Ci31aJF3a_hQlfc2_-nrsFyqchJdGdJlrIsYwSl8Ob3BBm_aH5Z865zJ59Fzcn5Lww01K_wzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
• کریستیانو رونالدو به یک ویدیوی کوتاه در اینستاگرام که او را به عنوان مشهورترین ورزشکار تاریخ معرفی می‌کند، پاسخ داد:
"خیلی ساده."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102500" target="_blank">📅 12:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102499">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29d00a9ff8.mp4?token=kRDFI1XbrD7ZKKY10-StZrkgwlGRuAjkL1NBf6UoiInEP-KqCNIrGy0ywIQxr9lTzBkpEeU_H2D4XDEsE4CuXlIhqX8-_tG4LM1y9XIGbero581uxrlIm--2R4Mx_RalrTIrys0QyxPF9cUA0ypvCCU9HwMBS9ULqLsd3h9i7iv84_U8uTec4RY_v8xTEADe2-WLbeBj_CB5V8zedf6TqL0PuwtSUiww1RIl6nziOlW8lXBAHNebIoqiS76DSOx6XTZTOafOYYRmXkLP0KH3D_FmYssM_xiBdd-a_gau7AMTNqoxFY_lvK-h-7hjzVMAl1jCxgM4TOeEGGb4eLBJrKcVL8FE_xUB4LwoUXfczFauze_qw6dUeYg7Qzep4gTdaC4uIRp8P7PDDInC2uGH0tXuj9sw5QV15NTsfQKwkxjvcMm0g-AvUd3nLm8ApnJ13nU3OAF0NO4ioo6yzBCZhiBHwSlzelQjcG3rkWQmWWA_5cHPpPra6nz_rdF1DnlsbUbCxbywltfTA7iBLDwiLcdPpz8kS3ExA37eM6I8jPvENs8Ku5QalzzoHZ0m0EER202r_SkDAR1LzSJW8QANdBGcznRR3ToA7jQCm8MQ4rbjLzA1LUgpVmtGnzJ2XtRGYBrqkQHBFP5mfTRBUCQAEEHeXd03s1EdIKbGIYcSxPI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29d00a9ff8.mp4?token=kRDFI1XbrD7ZKKY10-StZrkgwlGRuAjkL1NBf6UoiInEP-KqCNIrGy0ywIQxr9lTzBkpEeU_H2D4XDEsE4CuXlIhqX8-_tG4LM1y9XIGbero581uxrlIm--2R4Mx_RalrTIrys0QyxPF9cUA0ypvCCU9HwMBS9ULqLsd3h9i7iv84_U8uTec4RY_v8xTEADe2-WLbeBj_CB5V8zedf6TqL0PuwtSUiww1RIl6nziOlW8lXBAHNebIoqiS76DSOx6XTZTOafOYYRmXkLP0KH3D_FmYssM_xiBdd-a_gau7AMTNqoxFY_lvK-h-7hjzVMAl1jCxgM4TOeEGGb4eLBJrKcVL8FE_xUB4LwoUXfczFauze_qw6dUeYg7Qzep4gTdaC4uIRp8P7PDDInC2uGH0tXuj9sw5QV15NTsfQKwkxjvcMm0g-AvUd3nLm8ApnJ13nU3OAF0NO4ioo6yzBCZhiBHwSlzelQjcG3rkWQmWWA_5cHPpPra6nz_rdF1DnlsbUbCxbywltfTA7iBLDwiLcdPpz8kS3ExA37eM6I8jPvENs8Ku5QalzzoHZ0m0EER202r_SkDAR1LzSJW8QANdBGcznRR3ToA7jQCm8MQ4rbjLzA1LUgpVmtGnzJ2XtRGYBrqkQHBFP5mfTRBUCQAEEHeXd03s1EdIKbGIYcSxPI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
ویدیو جالب و وایرال شده از رقص امین‌حیایی بازیگر محبوب سینمای مملکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102499" target="_blank">📅 11:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102498">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86343d5e54.mp4?token=XdwSfD6dNBMR2_OxBaDXyzAcNumdMAIsJPQ6LJmlqzslHWUSt6gK_fPCjZQ-PUNKg2NirMCcjyXvKucbcuXVhvwaNbjNda-uW-lc4o-aD_si8vtO1Ri23ahk8rRzVo5kXXu0OpMfgzNRkIH9LCks4UzhzXDJ2qCUb4hOqRYGEib_m9gfgViDX_t30cDFj1AQzI6I7n9Hv0mX7fkQCLKo3eTkYK2dBt9rrJGrXD5TYyAMD2mIKQOMRbz7K0_rfrGhjdkZUNjd3llAKWvkNC37W7VuP_fhl39Bo9WypeM8fkC0UOfPKusehcL-IGLYqL1hL02GZbSmK8E7Jt5z8kEysRVmFT_E6XL1YZHi3znjOvpAaGqR1qNjOKkjrtmUNIb7InRGmkXWvQVIatwqRE_lH_wEBuTCLGLO8u9TdTBBW49k74PryfJBNeGcOJxmXZhXZkd18lN7DmQaqL6u6pT2R3nZFyfRmUQ_pQZ0e4nZPMLWuh5vruPikwt4ExiLUfotNE85iwDLKUGu_DLExAZHubpFILbK43RSh-9R6GJnEmbKzHJ8rcOM_eZ-RYZbLcnniRJoPqmDuYiCc8Hz6tSzMHo5qMTVXrrUdipa0vI3bas7Dq7HCWZFgUEBp4Z5Jd0Vlbv6WQMmYKFWETMXASPVXt7DLwujtMR2BiPOszW6Jmo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86343d5e54.mp4?token=XdwSfD6dNBMR2_OxBaDXyzAcNumdMAIsJPQ6LJmlqzslHWUSt6gK_fPCjZQ-PUNKg2NirMCcjyXvKucbcuXVhvwaNbjNda-uW-lc4o-aD_si8vtO1Ri23ahk8rRzVo5kXXu0OpMfgzNRkIH9LCks4UzhzXDJ2qCUb4hOqRYGEib_m9gfgViDX_t30cDFj1AQzI6I7n9Hv0mX7fkQCLKo3eTkYK2dBt9rrJGrXD5TYyAMD2mIKQOMRbz7K0_rfrGhjdkZUNjd3llAKWvkNC37W7VuP_fhl39Bo9WypeM8fkC0UOfPKusehcL-IGLYqL1hL02GZbSmK8E7Jt5z8kEysRVmFT_E6XL1YZHi3znjOvpAaGqR1qNjOKkjrtmUNIb7InRGmkXWvQVIatwqRE_lH_wEBuTCLGLO8u9TdTBBW49k74PryfJBNeGcOJxmXZhXZkd18lN7DmQaqL6u6pT2R3nZFyfRmUQ_pQZ0e4nZPMLWuh5vruPikwt4ExiLUfotNE85iwDLKUGu_DLExAZHubpFILbK43RSh-9R6GJnEmbKzHJ8rcOM_eZ-RYZbLcnniRJoPqmDuYiCc8Hz6tSzMHo5qMTVXrrUdipa0vI3bas7Dq7HCWZFgUEBp4Z5Jd0Vlbv6WQMmYKFWETMXASPVXt7DLwujtMR2BiPOszW6Jmo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
پنج گل برتر فصل‌گذشته لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102498" target="_blank">📅 11:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102497">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qndSKeYsu6bF70fWISQ7EEXvKvn9ii0TZSXVXCMpH55RqIUPWR0qCg9De3ulxGQc9GiUbW3nXitMAXl9o7qkiBKaJspQL6AS2VHM39KOUFmqUJO2EJU4XCBptqe5LLlATpZQqjCOHUcJfOFRricBGbuvtnX_oCi9b6UbLlNf4EYnfGahssa2flsq_nyBVQNl3PGo_dOD47OIOB_jsBRQyjY2yXyJKAzfIluJoF-IDNd682_fpTkBPkNIlncAAZ74UVSvYvOKNju4WIxHCBEdAahateki4_AFYUMWJBoLsfuyJAVxXeo7xJUXqD-Bhy0GdhfU199un5rtYIAgrdEh5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
اینفانتینو با انتشار بیانیه‌ای اعلام کرد که طرح فروش بخشی از سود جام جهانی به شرکت‌های سرمایه‌گذاری خصوصی، به طور کامل لغو شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102497" target="_blank">📅 11:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102496">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e324940235.mp4?token=iNLfGjQEFg6Smd3qtE7M1ktzZDpl4PnFOYWVsEHOnVOwk9OHbwr_jfr7C7IxdASmrXwiDZISoN-XjdbsNr8Z77Kzlcl37lFdMzfdk1Df54p2PCXlh0yJxApyP_vE95DDqM8N_j4iCW9ak_L50uGXs7DvAPLEMuAc1mHDD0nh1hyHZ4JDIOYle7SpGyV_A--dPOgoESBCQtzGtdjOVwWzFaZ02EJIvM41jDR06tNsin_6uRrEmSQpWmOc0l8sX8MASFSNWkttw52waK07_yDHg3DBLNYJsXwq9lTsCc3BKZknD-34Cpzjvusz6OtCzMYTNmhx-RePkAM16bpUc42i8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e324940235.mp4?token=iNLfGjQEFg6Smd3qtE7M1ktzZDpl4PnFOYWVsEHOnVOwk9OHbwr_jfr7C7IxdASmrXwiDZISoN-XjdbsNr8Z77Kzlcl37lFdMzfdk1Df54p2PCXlh0yJxApyP_vE95DDqM8N_j4iCW9ak_L50uGXs7DvAPLEMuAc1mHDD0nh1hyHZ4JDIOYle7SpGyV_A--dPOgoESBCQtzGtdjOVwWzFaZ02EJIvM41jDR06tNsin_6uRrEmSQpWmOc0l8sX8MASFSNWkttw52waK07_yDHg3DBLNYJsXwq9lTsCc3BKZknD-34Cpzjvusz6OtCzMYTNmhx-RePkAM16bpUc42i8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
و بالاخره تحقق رویای دوران فوتبالی کاسمیرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102496" target="_blank">📅 11:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102495">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👀
🔥
هشت سوپرپاس‌گل ثبت‌شده فصول اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102495" target="_blank">📅 10:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102494">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8VVCfHlV6FGkeI1G7P8nshV9YZVtVEhmWeWJM3Nd2PXenumaFDObjAYD-PfrLxpA4iRLCo67NmbrN0-V15ejs98JGr3hwsmw1zP-8Ka3BK1EbQKgw1moDJyyWQLYNk3bIg9QUSdMYjSOBBdfqFv9d5TF9W-BOBliR8qVG5VP4VfR61r7hlun-zpnW-sj9FjYzNgqMKVucu_BqSP025l2fx6AjNFT4lwBoaxb19G-OEZCWXgSsTlme7vHitZ58It36F1CmMmEWmZtfzWGab-WcAYCbWlraAAoHKUXzW8cX4BRuzg3fPOk63RhI96yYZKWF9O4p-WWA5r6LCPBp_uJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه آمار مسی و هالند زیر نظر پپ‌گواردیولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102494" target="_blank">📅 10:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102493">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv4GrqDx529r2Ct-w5NGjpl6KaEo44jyDKgkLPLeNYM9IYtOUba-hVCEcTTCV7jdxMZ5dxHhFg-uzWZFd4RqZ5RCYlidXIIMkthp2FwP4xPBvkNGwwun4EBwyBHKxNpzgLNdXhzYAS5PnNSXIL6rdNNCQuQzIiit3XkheNWLAl-tZiOmBBsGRcI57Q7fZy7IOz5oEmS-QPjc2jcOdbN0zd6yQ3jqHeHQ5MIHphkpVwoTJ9XdUTcauLv0xtpEZSbMVsYBnF-CyGNawxdr2fYVR53mzuZj7T3KhxcCTl2-18ER45tP4gSiuZs7Lz0JlB_kjxAqhaUW_gej4RCOSdFepQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام قهرمانان ادوار مختلف پریمیرلیگ ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102493" target="_blank">📅 10:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102492">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1s8sAJIsersJ1yLARKRSWZ_XHOLKLJ8mtNE8CICLK5ffBbeyfAR-sAIZgeQ4uDS9GwA3odz0Ax_HsEb1l3FJ41DX_4WhMod2l7WZqBHv-JgL8g7IAlD7q3GYMpPEY6wCZDCem-0goPdMFIAUkbIqF2f-pd2dp5VVpMR2O10j-YBQyjiHruhAkub5KA7Hg3CPK3cdW--nLqW0KWTXpZwBCr1qCIKgRVYY6CKfff1S9iw3-xGVdc6ywxtI8epV3CEpTRtZb12AY1Kf2kFMAZTymOHEDirIJxQlSw4DxFvmt3ZY52rXCuGkwcvSmQmVL-JzILepArOEzBt-JoEio3jmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
باورنکردنی است که برخی از زنان چه توانایی‌هایی دارند!
💪
ژوستین وانهائورمات، هافبک بلژیکی تیم زنان کریستال پالاس، در سه‌ماهه سوم بارداری خود همچنان در حال تمرین کردن است
❤️
او ۷ ماهه باردار است و همچنان با تمام توان به تلاش و فعالیت ادامه می‌دهد
👏
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102492" target="_blank">📅 09:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102491">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnaZecuy1ETUkbZqPKy_3eJqeZzlrhOnox0D2cSz1AmHCZOf156F2lyi3fD63E1gHVZGwlEr9XXUTQCBxlx_a5UNr-XxEhNNovxRTBUzwVj2Ey6R5NihTQbj2fiQsrtUk1Mo4hgrrPO7BxTCcIGvIqc98Vz-jCbTh-IS0FloEA2o-QDBsnzmr7dJTHbdLpw6Z5DOpVZqczyUhRj0BWW1iwO27bK_c2Zpx1cmv9OE9N3keSkIesbPFVeuBcruZsLnIDMahDm6-SnkdOujyLxxKTm7Ryj5XLuJ1dHG5lmeNPjNRtKKIoKcG3wxRCYQ_ChT74A4tkBR7eLNBZfxXtlJEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇫🇷
فوریییییی از فابریزیو رومانو: پاریس بازم وینگر خرید! مگنس آکلیوش، وینگر راست ۲۴ ساله موناکو به پاریسن ژرمن پیوست. مبلغ انتقال ۵۰ میلیون‌یورو و تا سال ۲۰۳۱؛
هیر وی گو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102491" target="_blank">📅 09:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102490">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17b2ecad4.mp4?token=OrmQ6H3JssX6D3ShGV4awqhxY6M94V8QAA7vuSV1hn0quL5geJ-lDspcWsBLHpxJZl8AJFpJHx-kuNjadUoH5hw1IDvKU9VUAVkeqsCUfysrqkGxx0ug1P5KuNIu1sv0OmKTlIa6GT-55hmIA5zcYGGAUoTGL1CTQSOiRN5kHYRCJXFpXTVxAVlgxdtIE1He07Izecx-CJf6ObzAWkmThLM2Y29FJ6_CueRdBxmP7ndBZGfplVnEZFDQ19x3WytqbThvksnhd0t5l1wFYxdq8OBYcDvHeU332j32hig9jdk88Q_EZYRHaF0aNDGlBX125H8UTR2Dw4Uf7ceNz85Xp0nPvggtyRIaZ0_nTf9dTFGOycXXTF7t6qXPkMNaIjM3dwS5rzsc7vPctQcf0_9C5N9KqKAJnqUtwwjVRIBZQAxGn3yOWMFSCtz1gQIIcP4NKqCozvsCtbLNY2ISbAYOkzdaOXLCJ7cvlCkhTjvcP6R5gb1yPR8P825I7XuOy8MUCTxCKMwwj8dCyU6i3P8iHUOqNv5npbl1aeSeXwpZKsxp1WBtBKCQtFE5r_NdGfvIW5UNeP64WHlXYGW3DvCGfbw6wzNfhUW-1KgHYTqAhYwzs2uQLIOz6zjCpF1czpzxO1My4860JNx6MYOjG3F347jG3cRGnqiDEpTUM3J3Zbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17b2ecad4.mp4?token=OrmQ6H3JssX6D3ShGV4awqhxY6M94V8QAA7vuSV1hn0quL5geJ-lDspcWsBLHpxJZl8AJFpJHx-kuNjadUoH5hw1IDvKU9VUAVkeqsCUfysrqkGxx0ug1P5KuNIu1sv0OmKTlIa6GT-55hmIA5zcYGGAUoTGL1CTQSOiRN5kHYRCJXFpXTVxAVlgxdtIE1He07Izecx-CJf6ObzAWkmThLM2Y29FJ6_CueRdBxmP7ndBZGfplVnEZFDQ19x3WytqbThvksnhd0t5l1wFYxdq8OBYcDvHeU332j32hig9jdk88Q_EZYRHaF0aNDGlBX125H8UTR2Dw4Uf7ceNz85Xp0nPvggtyRIaZ0_nTf9dTFGOycXXTF7t6qXPkMNaIjM3dwS5rzsc7vPctQcf0_9C5N9KqKAJnqUtwwjVRIBZQAxGn3yOWMFSCtz1gQIIcP4NKqCozvsCtbLNY2ISbAYOkzdaOXLCJ7cvlCkhTjvcP6R5gb1yPR8P825I7XuOy8MUCTxCKMwwj8dCyU6i3P8iHUOqNv5npbl1aeSeXwpZKsxp1WBtBKCQtFE5r_NdGfvIW5UNeP64WHlXYGW3DvCGfbw6wzNfhUW-1KgHYTqAhYwzs2uQLIOz6zjCpF1czpzxO1My4860JNx6MYOjG3F347jG3cRGnqiDEpTUM3J3Zbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
بازی‌خاطره‌انگیزمیلان و یونایتد در UCL 2010
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102490" target="_blank">📅 09:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102489">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">هایلایتی‌از بازی‌جذاب الکلاسیکو در فصل ۲۰۱۲/۱۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102489" target="_blank">📅 09:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102488">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BX3OSkCfk2t2h9NBtjmwjCYM_YUE1KEdH2WX3GB5E0PMbpkJjPDY_ntHsPTdBCbL0kondH1gKVZkeYQBc8pkC_A5wPsCKhjrlkDngDdA7jHo0KhKadfSWzpremONv7IcJ8d7Nf4I5dR91NxLZb-wl1ndFcQlLK58pG3AnyrO65R3Ki7a1yWcmqtpQi-kL0vyYngJgB1dXWlO6IKeg-a5z8QEA6eROBBXBPGQrwlezd8NceBQPTlxLxZUTNGfAHr182LrVZyZhTur9s59Y3vb-RqAr8-Dp5x_ozxCG1NQ8boWDBbtZmETh-JyyZLQ1P0CFENZE4LlreiJkLfRLuAiRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای اون ترکیب لجندری بارسا چی میخوردن؟
مسی عالیه :)))))))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102488" target="_blank">📅 05:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102486">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJLZiX8KxUpLcNdY_Xk7B4oSI_9EKq9Fm5XfBdhmu1kBhAv6K8AjjjfTuvW1QyCxVrtVCh2sL4Xxw5ya1xAw4Er4xRSGUsuQv8hFlsJqTNrf0_rqoPajhOe0IItWdqYo4194nd4diZYu9a-V13sznmBsrSCLuEwrAmXUZbUagCzLuNBhHx3AgV3Nr4848Q0JTW3FnfAWZtCMVW7YsVBPHDZFNpwQtpHNRRn_B-RJ_yzf1Bscj7lUfS1ClciVxXbPQIUHq6XADS9tar5DeKH7LubteK1IGWqEh-tfI06B1xGcVKquHU_LTCavoAUMUvKsvCvGmb0RuDJNN6U4TbFkOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
گوئدس ستاره باشگاه آژاکس با رقم ۵۰ میلیون یورو بزودی به psg ملحق خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/102486" target="_blank">📅 02:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102485">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇱
کانال ۱۲ اسرائیل: نتانیاهو در دیدار اخیر با ترامپ موفق به راضی کردن رئیس جمهور آمریکا برای بمباران زیرساخت‌های انرژی ایران کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/102485" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102484">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkFqO7B16e_Di_xoQ23syLVeipEEFL70DCEtpK_HHIyQ8bFgW3gs2Bcmr0Furm1V7woUyvJ3EQeAydwczQ4NbgACez423yDz0AyMMN4q1HAIIxSYJM4eEg7LKZfHGwU_VEwxWPurYuDxaePp8Exbb8axKysWxcABXwQijyP5w8UiLQePfLIMrDzehO5Z-LXMWxOv-Rlfw3N79pzQ0R3NOzveXIWWhNaIsIN34NShIz0JAEOqivVBrSGPXf8ABQsRGfjNwoSRk-5smQU-Dvgr238xGrX-ZLJfuvvSp0EH_7KE0mtV8qD6yhYUaXkuYWBjIxmpydbPoIyr-ncWKCzQ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب بروبچ محله تامی شلبی حسابی واسه جود سنگ تموم گذاشتن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/102484" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102483">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/102483" target="_blank">📅 01:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102482">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQS9DRJ-HcvnIn4aoL-Wi21VPsYfmEz2MPTLJn7m0oO9RUHVtkOjpbuZpS5JEt4AU3J6HrXmp2deULUuvyk_X-O_z2qkQ3D7jaPHk6nzKsB_WsoBh5cFA0-rPxNGll2PQGJpcM2osYw6F9BHuVme40rMddyyH8Sj8Fj-lGPz6g4-SgJlh7XhCTvURblv3BadUw21vndyuuLQxwClNQJZWPylg2szwo_GEkeIv9R_Rn9NpQbXBddSj00jbMZ3ZTNjblYn_Z0OVp3dvcfDlhd_P3ipN9Fl__oS5d44Dd69ZjxtuPZLGVlDBEd8oiDBcjt1SkTxWTO7w3KtgL8gX2vvcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/102482" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102479">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gTSwdRqMsr2QPb5OoRnGUNXSUt7DURvEmXvSI8w3G9nKTuROJxutWU6p-AfynukSEx-W55M0AzNJ3r9NNeSGc3Myeg665qguZM_GlBcs-lFvUpB8Ysjh6ILQl_NZ_1-sG9Z2ocbl3_8kkWeCP6rzpQ-XuZOai9Ito1yXL6cFT77HkO3mtjipLvXPAcx07AvkCpQTr-GOmT3SWnAb0bJ-8zLIAkflh9QEBxn_0TiqxNBAeW_ZvtmRhdfaqIX6jO0DvQrC7O-ika3s5UReaGnFsYyBJpJgaBE9hW9kY_BrTXJOjdS2MIR1oVRYhqDOSioFoYo15n5fsGD3Cq5Qo7kX2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u9DEf1ioaHNlVLySy-VcPBwtL4C9BRF6vwD6B8JK9BAaYgt59r3xyJFoIopim4lKTp0DEwbZYDL0GIF_ztzBGmZmt06Ytclu5dALgW8X2OS9c4wFD9oqM5cupIC_UTpMt-KqFB5Kq58B-k6K6PcLEp80itOdicaWjOJgEvbt5OsiUBNw_DIvI6yPBi0p-9ecDYEo-9zt17rzrqptX5OnwQatbKXz308xwyE0Og_lXun4v4IBVNQLO7B1JRhw-RaL_BC-Mi4_As2ShmPBwc-O6Zb_qQ2Mtp5mAGzwuZIOSHbzOXKfhyiPhZd8DmH7UGpszHAK7q-Hh7lJMEyEOb_y6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XB94diPf4AP72CYGlC2xXQpPOu1j-y4mFYnKM6Z4L_D3VpuBCbFFpAGYmluxmaOFZa94bnflgRFsxU7vC_ExjsnKphXrB6VdVIl-hrdw5ks7o7ka_6Xr8PtCo3TTuRvalvOLdxnt9eMt-KfjXniF51LauHUa3Bb0BMaJpdBQOkuok50euJFObqZpwOI0U7zjcG_x6s74w8xFvy3dd-4n59QJNfVcj6YeXOFEQtM4jQzH0dsv9c_3OHJMAQaXqPiD0x0qi4xhYQhStqs7txHqijNObaJ7Z3i87P7QBqgUPEElpLBUJ8p_JgUnVr14QEdXuyWIC_N2UQwH0qJ0vF4mHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
باشگاه فوق العاده محبوب آگزبورگ از کیت خودش رونمایی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/102479" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102478">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLQBGh0DWQM-YJ03l2qELzOTly-lO5gxwwcp5PCisskdgTSuCF2kZCYlEeJ8aLErlX1vHiMBYMaKP9RPQpn8BJyNvawyMF0O8zpZMXmloNcHiOGO5vtWfFEzzFfK5hVRdwGyg435VUpG_sED6w5lBpe2ta-r5IpmsRFpaELnzwIwiEID_znUv3DF7FizrNyhYF7dRmdl-v0x-5H-GZyOEaEq5EmxfwPjNLb3WUgNwNvcQmeHbTmoH1h2VSem3nkXCF8CR4gT3TQDnS3ssY7Fo9EAWnsTjuu7DYpXwx_Rc44iKFQxHhoHUcEASdMdXBdmU8nwiVCYFBTjUi2KAexGkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
هندآف آرسنال رسانه نزدیک به آرسنال:
وینیسیوس شخصا با آرسنال به توافق رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102478" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102477">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی،…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102477" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102476">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=mNmnWj0Fg8iCFcfR5xVndVBPTvb1vgvuFMCxYCTCFtYjhckuOy897u7_IRy1LnkyVSuC9ponh4INi8U5dlY1PV0e5cuzxjdv7gSXi74320PCPqPRP0dy6Pko_FOOiYZXgpNdCVzRZphUFxtwSgJOTX5OFLAoPXH2LtN1K67ykeywGliTInpIm1ldUWljl65lxD0tr8pvvhfaXuUofz1ZS1_kaWlpVd-L7sZEA_yIcoYzLNgK1WvKJB6_-iaF6s8TynQnr8O40mrO6278KbQE7MJK97rkuIhTSIQxydxf5WgtbxRl0Vej4i0aZfG7uX4xhYadL9q8UMqq_CbPEzFNnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=mNmnWj0Fg8iCFcfR5xVndVBPTvb1vgvuFMCxYCTCFtYjhckuOy897u7_IRy1LnkyVSuC9ponh4INi8U5dlY1PV0e5cuzxjdv7gSXi74320PCPqPRP0dy6Pko_FOOiYZXgpNdCVzRZphUFxtwSgJOTX5OFLAoPXH2LtN1K67ykeywGliTInpIm1ldUWljl65lxD0tr8pvvhfaXuUofz1ZS1_kaWlpVd-L7sZEA_yIcoYzLNgK1WvKJB6_-iaF6s8TynQnr8O40mrO6278KbQE7MJK97rkuIhTSIQxydxf5WgtbxRl0Vej4i0aZfG7uX4xhYadL9q8UMqq_CbPEzFNnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی، باشگاهی و دوستانه)
🔹
پیشنهادهای دقیق گل بالا/پایین (Over/Under) و گلزنی هر دو تیم (BTTS)
🔹
بدون ادعای واهی ضریب ۱۰۰! فقط سود مستمر با مدیریت سرمایه.
آمار ما در ماه گذشته خودش گویای همه‌چیزه. فرم‌های امروز رو از دست نده
👇
🔗
[
ورود به کانال و دریافت فرم‌های رایگان امروز]</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102476" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102475">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GC599jkIGJX1-QzQ0iP293sqGM9ZPI2S3b799DCbIlm7Foj-P0d_uB5GzO8nfKE_hYut2-k0mwT38Mo7z7BKwn07afE02Y6bLz6GdiVozzTnwb5NubcY_d82yBlhNk3fN8aAdNrfYNRcH60gIYyJbaR-FaJ1EVlwErLiyturZpYQG_4R-3wxt0V6sV-Rz-6HEo8lqKFGaf3h-CePim62NBQqfalxpLGXVt7UaxiLIx-tOWmCxpJgnlPJIVXv1VZyLQTB1_rZRIWxPg5Y-3oNBrTCW3MGDDNOBIr5MUSrcGfGzdolQ7P4W6mKQ9ReGfYSuDPNM7DtntLyVNeUrI5n9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بارسلونا در یک بازی دوستانه مقابل بیرمینگام شکست خورد. بیرمینگام با نتیجه 3 بر 2 در ضربات پنالتی به پیروزی رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102475" target="_blank">📅 00:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102474">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7bE1zZsxPLU7dAmUCT0e7YiI9yv0IBjkRHvfaWWlSOj8e22TCVPhWZNLzN4kJ6c-ixtArzkkwq4MNcBW9jlJTk8E6im2qZ9dHWHrH0PKcSobyQoDxDP3meyBx9mX6XdNM6oH80znFi9UPgPZFr4bJcTDF5F3wkdQGmHTEUgZfR8Q-ctfBRoWQ1x6m1EWgekjhtazAvoBYatwkynDlnKkPW62Cw8VAKsIKH3J7kc1-X5M0VwO-FVlcrs9YF8UI_j1846vaHKbPDX_gv5Q2TmBX0hVVEV8G1jhULasF8qJPVhVDFAbHxdtTvUTaCDd_QcVnARMTZ9wT9Lc-rGTuA8UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دوست دختر یامال
😦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102474" target="_blank">📅 00:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102473">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCZMjRConR-zLdG776cErCtQ8SBiEjMCyHzNpI4xIKErM9mYTeqFolmA9Z2M4P16IgAcwasnMfvhgm-06qxwY3dmJqv_yb2QamVr0hg-O1n1MdsnjxAfYCMZ0oiD7mRvxaYmu-F70UzYHCBscLws8b-YKG5UjZGLryjSmjUXu0gUSgAJwHLMRC5Ora3CRi2k9-7KHFle9VfQ6usph9-dcZ34jd1UTS2tjW6egxhzxDROqNYR86VMEr79gVELHRwx2w3jHPm6IjmY3tEqHzs7tdxm82YFmi0gBAzVJ7T8Sg2KNO5Qp2HUkGjA9bfilL0aYSaog7-fQRUVlMOqmWd7lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🤩
خداحافظی امید عالیشاه با هواداران پس از 13 سال حضور در پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102473" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102472">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMc7i6CcefyueuyV93kLX8PWxaZNFgdImB3fPbA9V0187uKG77PZAN8Rj_g4W1I5o5abdPMLx0etwQQnWonTpt5cYooXrVTUh7Q5BHiQFU8fEh1uRvVXvbG8EgT2zGHoQOe3-GIWx5PTYGhwS1mTWudZyW_Jp6QNL_gCmvv1FQaSVh1vzxE-gINNqQ3srMNRiOLudPRcyo3GKKhcRBMuS4jYVAbZMBaflaXhn8cwbeNkZpRpY_6Ab1bhvY4WL9kDa462ZrAD4O5tFZ3jk13wMXVIaktJIGFD_5QDQ5p9OJSDrvdyvU3VFaIVJTz8XQG7C7rKluzuS_L0SlaVM5gerg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
مسی و کاسمیرو تو تمرینات اینترمیامی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102472" target="_blank">📅 23:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102471">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c665525c.mp4?token=hTkVO3o9OjlxYPDLFAPkz7o8lB8ejbusjzvBXZnTuWxiMYp1FIU6VYXQ_F6GA7ya91Wej1WjMWqMtkT3dwHAMSY-MLT4Qe4_82Dflo1E6Bka2BonsxZvthQasIsZflDvBOZ25Iv4KTHHfgPdEay2HMlrlyhUPRAKwREaSSyM1L7AFmOVhH-E7SNSYb0Vq9G9m3u96Wh74qRvmsc8C2WTsvKfGg7f7EcinZeM3q1CGn-G_-1U40AQZIoYz_KXHK_GFS4OYziEyVwJ-YJ_kN5HzDtVbbeUsMkyhyKeJEZN5KsLYYYDZ_1LrLSmVnecGAYL3_5W-LP3ahnvSH0he_0dDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c665525c.mp4?token=hTkVO3o9OjlxYPDLFAPkz7o8lB8ejbusjzvBXZnTuWxiMYp1FIU6VYXQ_F6GA7ya91Wej1WjMWqMtkT3dwHAMSY-MLT4Qe4_82Dflo1E6Bka2BonsxZvthQasIsZflDvBOZ25Iv4KTHHfgPdEay2HMlrlyhUPRAKwREaSSyM1L7AFmOVhH-E7SNSYb0Vq9G9m3u96Wh74qRvmsc8C2WTsvKfGg7f7EcinZeM3q1CGn-G_-1U40AQZIoYz_KXHK_GFS4OYziEyVwJ-YJ_kN5HzDtVbbeUsMkyhyKeJEZN5KsLYYYDZ_1LrLSmVnecGAYL3_5W-LP3ahnvSH0he_0dDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین ووزینیا که تو جام‌جهانی تک تک تیما رو سرویس کرده بود، جلوی علی علیپور اینجوری فحش خورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102471" target="_blank">📅 22:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102470">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpeGs3nx96bvmOx8f9GFjcFC8y1JtVXkjfRmXIvWA56bPTPjYTJRBOslQf-VdoBrlY2WseCUIVNPh7Ius80WwyWihwimB2izgJX9K0hjw_jROPrrcaDinLMRFU5zIRnCNpUaoobyvOSP93OHEBn9FpHLwj35NjKqud2s14RWqgjqVGokH4pDSP0nN6jdsOzkWxRSqPubqGa8x6q6c9vce716axmT-UJ-MZp0cuUy0u6Wfx1ueX1qtu52FDiHDtBW-9xjMoteUt6LWs5RDwig_ysxxBphjYZJWI-2x9XurK4dZQ01Qj3ZZY8iIzkZoaInVmdBXSrxc8HBE3FYJEP_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ار‌ام‌سی:
مندی تو وضعیت مالی بدی قرار گرفته در حدی‌ که مدال و کاپ جام جهانی خودشو 54 هزار یورو فروخته.
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102470" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102469">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261dc7eb19.mp4?token=BBD-EOqiUp_sHaIJmOz8U72WJQ8bagYs2cN9l_dYMzznVxThblVG0MmFTrsJmZ9Ao44zwZ9uVEPcmiVpiGwKHYXsrD0RWuGM7k94bdkFWg240Ws9urTFpjWWLhDFlt1Hf4cmRTlTqWopMAOpncQ9wAwxu4WzakZkbLBdqZYQUb3V_MlGwyV1QgIfNMg1hrGmn58j7DuE9J9DRsW0f7_nIpud6IPbuBvKKK_Txwr21UgguDijje9__t2JXiQml0Yj4-Fe0CA3Od6m_l9UoVAd8PICG7sI_8htPfo5av9JvGrHkWo5HRRaZPwrhVDFJTCOl72FLsAQYGTO38YAlt1pGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261dc7eb19.mp4?token=BBD-EOqiUp_sHaIJmOz8U72WJQ8bagYs2cN9l_dYMzznVxThblVG0MmFTrsJmZ9Ao44zwZ9uVEPcmiVpiGwKHYXsrD0RWuGM7k94bdkFWg240Ws9urTFpjWWLhDFlt1Hf4cmRTlTqWopMAOpncQ9wAwxu4WzakZkbLBdqZYQUb3V_MlGwyV1QgIfNMg1hrGmn58j7DuE9J9DRsW0f7_nIpud6IPbuBvKKK_Txwr21UgguDijje9__t2JXiQml0Yj4-Fe0CA3Od6m_l9UoVAd8PICG7sI_8htPfo5av9JvGrHkWo5HRRaZPwrhVDFJTCOl72FLsAQYGTO38YAlt1pGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
تام هالند یک‌بار به ارلینگ هالند دایرکت داد و از او خواست به تاتنهام بیاید، اما ارلینگ اصلاً متوجه نشد فرستنده، بازیگر اسپایدرمن است. بعد از اینکه ماجرا جنجالی شد، هالند برای تام پیام فرستاد و توضیح داد هیچ قصدی برای بی‌احترامی نداشته و فقط او را نشناخته بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102469" target="_blank">📅 22:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102468">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5dLn7BMjxKs9N6kY2_vg2FAU0R6h5B215DdrI5ZWNEcPz8XJc-xiTGSzSrBP8ardIZvQPvKWZu1hrxLB0Pe7GlKVo1fdxfw9KrGgqNS121-FmLR60i1yXNYvCl29WGtv-kuLGDFuZZk4FIunmC4AFvW-KXdODf3_WzgLIqTT2zYftUfKCDBNWtuMzimGKaGnDPoJPmeF3RRO4EXzBdlcWoMH2yQJmtAVTz-oOEZQYdOagEpd9YLLlCyEmS6gfmXWvbzaio4SUvcDItalJv6gZTM0DqqJQOrIU7DfQkaxcBydzRWvTS0V3pg2XqCeqog-5cdGsWoEDujgEWeHZNB8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
بمب لاپورتا ترکید:
جسی بیسیوو، وینگر بلژیکی کلوب بروژ،
به بارسلونا پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102468" target="_blank">📅 21:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102467">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gua9AxtR3VIPTqSEQ9OItFakJ2lQcymU2Cc00K39KnTJHFAb1qEPHpdU0OpQBAAuDtd0VAK5z9rz58GBcXHtwDVKB1XIkJewOLoafuzUyCoL-mtbhJonHrXoTag_O-DQpwKcDYTGY7ll6rNA-1pCAi3RvWAky_hwqruqXeP-cxF9SZlPzmbeDI_TpY5ednWg3-_x2DFe5pkg9Qx3RPLnShJqnY5sbIwV6wIDOVm-2-1UWVQHtGBlcov8O57zyqlqxH86snLUvIKa0NWY7eAQWq3RxLPSpRZ0OFe7rO9DC5uKTIO88v3RK9w4HniZgyD3bOI-eUNK39nJiPnMMRfB6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب امشب بارسلونا در بازی دوستانه مقابل بیرمنگام‌سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102467" target="_blank">📅 21:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102466">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f4d6d3d7.mp4?token=mcYyTVPWO2d26ZO085slORlvsZNsajAiNZKqGc2Yo4FB5SeMxXxgK4j4zGBXBA-9PVkuk7ZcbDt9HuEuYyxcgFVezD-IHMGxFyfP1lGp8FZNyqyAyg7qOHDueMzPwbxn_9NSA7ixVRwtwXlX0_t_L5DiDvIhi8K01yLLL5-ANYVQHh4Hm5T1hoTUl5FSjqJOqd_qVD2--jL1Pw4vs6AZj3u181o65uIGc-LTjPTIW_WQF48Fql0x6-J0CJEwI6P-zt5_4adYBb3kCSFgZ0XyLanZ02thmq_0e6iVmHfr1_ICz4hObD_HxRIL5m1tpsAMLPlMndlvRvqqwsf9K6CLrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f4d6d3d7.mp4?token=mcYyTVPWO2d26ZO085slORlvsZNsajAiNZKqGc2Yo4FB5SeMxXxgK4j4zGBXBA-9PVkuk7ZcbDt9HuEuYyxcgFVezD-IHMGxFyfP1lGp8FZNyqyAyg7qOHDueMzPwbxn_9NSA7ixVRwtwXlX0_t_L5DiDvIhi8K01yLLL5-ANYVQHh4Hm5T1hoTUl5FSjqJOqd_qVD2--jL1Pw4vs6AZj3u181o65uIGc-LTjPTIW_WQF48Fql0x6-J0CJEwI6P-zt5_4adYBb3kCSFgZ0XyLanZ02thmq_0e6iVmHfr1_ICz4hObD_HxRIL5m1tpsAMLPlMndlvRvqqwsf9K6CLrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔹
وقتی منچسترسیتی حریف پیکان نشد! سال ۲۰۰۲ پیکان با سرمربی‌گری ذوالفقارنسب برای آمادگی در رقابت‌های لیگ برتر، یک اردو در انگلیس برگزار کرد که در بازی دوستانه مقابل منچسترسیتی موفق به توقف این تیم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102466" target="_blank">📅 21:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102465">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcb0e2d66.mp4?token=H4Dle5s5Xke4n9r1AaDy_Q65f7HK-2ngPU38skuzNlC1iFSgPO0iDJwdae1L0SKz6-f5gIxMmWGr3LWXlxovY6P94YCwtLWdoSGLN4L15lNY6leT8Q1C8R7OL-ccgdWBtNKQpReoQwtlSdYPXIFEyNL9sQWt5IEFGQdDWKu2YjCYr8SO7Gk4nBpRPQ-abjgyq4STWUhzO7r9CF87_lMpR_DxXQ_XFrfvadKyfTtZ584331RZ2X7NopscEqxc5hSe67UMlCk9-olRzJOZrPqCOqichQdiW41gclHsVk_Gr6vZyPyDjwLAQOoKw6ggdNERenCKoPa7EBiozCBhxAZ45A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcb0e2d66.mp4?token=H4Dle5s5Xke4n9r1AaDy_Q65f7HK-2ngPU38skuzNlC1iFSgPO0iDJwdae1L0SKz6-f5gIxMmWGr3LWXlxovY6P94YCwtLWdoSGLN4L15lNY6leT8Q1C8R7OL-ccgdWBtNKQpReoQwtlSdYPXIFEyNL9sQWt5IEFGQdDWKu2YjCYr8SO7Gk4nBpRPQ-abjgyq4STWUhzO7r9CF87_lMpR_DxXQ_XFrfvadKyfTtZ584331RZ2X7NopscEqxc5hSe67UMlCk9-olRzJOZrPqCOqichQdiW41gclHsVk_Gr6vZyPyDjwLAQOoKw6ggdNERenCKoPa7EBiozCBhxAZ45A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚪️
رونالدو چرا رئال رو ترک کرد؟ شرح ماجرای جدایی اسطوره فوتبال از زبان خودش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102465" target="_blank">📅 21:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102464">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ed94c011.mp4?token=sMYUsVsIz_pTw-HyP7npHesZU_6E6DXJmuHzOjqgriVNhYq_8kCmlV24ct8i3Q1oK5PRkTMSpV99nL37Dbi8ZBpoyn47oKfZJqiPLNscvLFKT2OYkg2N5oYaa3WsHoJejKOqWwqzZQX52GeyksbAmf2Bpx228fhxqAgoy0JRxkE0JqsGWq2xZK-GJe0kCjYxQ3elzs0tFbQ5fnmYBxLuGWE3nIR6O-m3zz295CDf7EZlC2MP1ZNZ1-8Cc2apYPu5EFbGAnd5Xwo5QCJzpP3q20H5ILGA12RBypJ96PEmFL33SETXdj_h0xuSls6VS6yrtpy8fcp5fd-pGwVHfreSrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ed94c011.mp4?token=sMYUsVsIz_pTw-HyP7npHesZU_6E6DXJmuHzOjqgriVNhYq_8kCmlV24ct8i3Q1oK5PRkTMSpV99nL37Dbi8ZBpoyn47oKfZJqiPLNscvLFKT2OYkg2N5oYaa3WsHoJejKOqWwqzZQX52GeyksbAmf2Bpx228fhxqAgoy0JRxkE0JqsGWq2xZK-GJe0kCjYxQ3elzs0tFbQ5fnmYBxLuGWE3nIR6O-m3zz295CDf7EZlC2MP1ZNZ1-8Cc2apYPu5EFbGAnd5Xwo5QCJzpP3q20H5ILGA12RBypJ96PEmFL33SETXdj_h0xuSls6VS6yrtpy8fcp5fd-pGwVHfreSrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یک تازه داماد پرسپولیس را حذف کرد!
از ماه عسل برگشته بود و چهار ماه حتی توپ به پاهاش نخورده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102464" target="_blank">📅 21:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102462">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102462" target="_blank">📅 20:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102461">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=cNFbd--czywaLyFZL0c_Fvxu2GvPLy7ztT6QWsW2w0iHwUdT_2ldiWrmP3cjSe9wL1FJ_IY_Hg72OLlNWVIu5DWKQuGOplTnjurwC7V8JNfHWGAshfOuErGbDySl0zCf3ye5lpHshN6Heber4bqBGC_xrBwC7x-4Tkl0zOIDkQ60bBgFoIQO_g3tvQ93jv_SDpNAVkqSkVYtzfaf3DkL-fTlcuPT_FDJCiBqtDuYZIzGT8TvNQy-GGbMyesEmsV3ptDGphODbA322XMpKkZUKlWaQQF_dZ583rx2Z7hXGaPfp3unRMTnb5w66wyv1yr-4OVR-RJeLaY68O0-qQIuNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=cNFbd--czywaLyFZL0c_Fvxu2GvPLy7ztT6QWsW2w0iHwUdT_2ldiWrmP3cjSe9wL1FJ_IY_Hg72OLlNWVIu5DWKQuGOplTnjurwC7V8JNfHWGAshfOuErGbDySl0zCf3ye5lpHshN6Heber4bqBGC_xrBwC7x-4Tkl0zOIDkQ60bBgFoIQO_g3tvQ93jv_SDpNAVkqSkVYtzfaf3DkL-fTlcuPT_FDJCiBqtDuYZIzGT8TvNQy-GGbMyesEmsV3ptDGphODbA322XMpKkZUKlWaQQF_dZ583rx2Z7hXGaPfp3unRMTnb5w66wyv1yr-4OVR-RJeLaY68O0-qQIuNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شزنی جنس رسیده بهش و مشغول دلقک‌بازی تو تمرین بارساست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102461" target="_blank">📅 20:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102460">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace3163b65.mp4?token=lt2tZA26OQeQ0gJXJkd59TZXu0OYjzo5B-h1YwDVuJd6P4DXFJDW9zatUdf5QRDOc6LjfuLiGTSTBr5Bwo3KPu01g-aufnGYk9Xi5d7ZFbpCHdUrfUMEqH8oELb71ctjHdnI94WRxcMAq4mHc8Mmy9t80KadLjKwNTuVmYdixN9qhfPk3bVtZtxPLW_Rj4nl4ixL8xECiJslx2Yn8EQH5-KqqAcS84nsGlfZdOIe-tZluN7HTp2omyFTnmDykSgMwEdZxtg6--MnWsxVShlS8OTumSfMt9pCtPpRXAptuh5hrXjWpMO96KlzQ3nmhajmEvrN9YyYYNgziEhoKS0Qwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace3163b65.mp4?token=lt2tZA26OQeQ0gJXJkd59TZXu0OYjzo5B-h1YwDVuJd6P4DXFJDW9zatUdf5QRDOc6LjfuLiGTSTBr5Bwo3KPu01g-aufnGYk9Xi5d7ZFbpCHdUrfUMEqH8oELb71ctjHdnI94WRxcMAq4mHc8Mmy9t80KadLjKwNTuVmYdixN9qhfPk3bVtZtxPLW_Rj4nl4ixL8xECiJslx2Yn8EQH5-KqqAcS84nsGlfZdOIe-tZluN7HTp2omyFTnmDykSgMwEdZxtg6--MnWsxVShlS8OTumSfMt9pCtPpRXAptuh5hrXjWpMO96KlzQ3nmhajmEvrN9YyYYNgziEhoKS0Qwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کول پالمر:
برای بازی مکزیک - انگلیس بیدار موندم، ولی بین دو نیمه خوابم برد!
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102460" target="_blank">📅 20:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102459">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASW-oTVV0kZksUWixqY1ltpE8sE71NHKwOMdl0ADq6cMbG2bGvwXA-G-YzGsss6sRE8eCM202JxDTSAj6rEXCNdG0ugVgZRvLbpAA3eTAyR42ILmjh_zp-z0Lf8_VILY9iN5TC3caewmIUPpCPxWnyQLV-Dph1E97xQ1-E154QUj9bCJe89x9vM51wij05hxcPJtac1l8FQkLLK5N1DfukKoEgJevG6ePnEPt4zfdrh5LpKRssb48KuRJqtsRLk4uHd8PhUKGRL-ri5Fa9_DV-038geKLp7IuvlhnXLrxdpTL495HMdK3uvLnCCCBX78mqroxAUVzK54SyijU6ENRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102459" target="_blank">📅 20:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102458">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRHM3sPpGKnh53VtmBe2Q3KnA3CRcSU20aG7xyIxYNyit6L022VawWsRp7liMWfsThesKoA78JbGfwlRZZ8HQuM5q-qJf1qzKKD56X_EDN9wdc5SgXyhJPo70WX8M8tE5fr6RG_RupV5uk9Wa7BxlKEtAZej7w6-e6OKOtZ9ybOu__lcdI4_q3zx_FcSBoGF0LgaTILbPEqdZfRYAil-IR66oAYy1jJZM0036GiZRAEKsFcRyZi3YIX8WOXcyeP_VGcytRmGHytGK955oOkEy8ZkQPS7zXOL6ZXXyk20IRd1kV2m-JJ21ge51CPGAh9Vy7lbRX7_MER6M2MgAjUTFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
فقط سه بازیکن توی ۱۰ فصل اخیر تونستن در ۵ لیگ معتبر اروپا هم بیش از ۲۰۰ گل بزنن و هم حداقل ۵۰ پاس گل ثبت کنن:
😀
محمد صلاح
🇫🇷
کیلیان امباپه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102458" target="_blank">📅 20:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102457">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnmgMv8V6-KAuCxcgL23KUNj4Yt1c3lPOkzV169-jA-QvNMFIi_NFWQiHupI3YiwPHxCWYeBU30GfaP6mXKp0JgGz9TlQ6j3C5cyHRzUbT2FqSl3fjIiIYw3ZDifY3qzyntdNtEq9AewD9VvmkyuHV2O2FqIYTufGis3hfjpq2a6l88hvcnmw04bm-RwVMRodPm8jgNaa_sziL67kevD923o_Bgn1J71_iBtTCs_r9gBUbnylCEIBydz0L2tbcucOMjo3DKpQXMXO6e2FU-wBd1K2XghYwRl5cK9Q4KU7qkbI_G1ol_Xr2AoG9whugHpts5kgHso9VJE3e5O9ulShw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102457" target="_blank">📅 20:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102456">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102456" target="_blank">📅 20:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102455">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0tfPVV_5V6JVoab7TtzXmzNPcGzQNcZkMbIYnOf_dsIvmBB6jfudqi2nfAp9FvfDWmqD0wvxuzQost5FkEVmawZwOctv5nzRYpxPkBhbexHzWqU1yow4i53Sd8NVzW-TT81vr-RJS3NW_NyGrxjn78KAW2FDSshtWacwvWMDQ8RZDok1LUCcLeQHUiSdgjbmMopLZHMKV2KsP1RqD6VuQVevI9L7--aQndlgq92Ax7IM55pyzqSJY6ce9Ilf1Rw0PQIq7hMdD-HgRxkhYQWebkPEvj24gQPpE38GSFnW6-X0kphBYj-Zzt02PZYNidKEZ5emxOwHEE_8dS27RbfAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102455" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102454">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKTLx68NYnmxLrCu_NKWqBYz0HpiduycSeH3FAgTrxyJzlOSkBQqAjTznjmqaIJnvkT_m6YBAO7BtrCZwRsTMn_JaIlJa4QWpCEt2iiTtPSTUMiqUk7fQ2hJavBwvAmIcnnwBqP_gIqdfwRhj4hIWmNwv4onFTdBwS1fS3vRkt9c6HErIMdtZ2b0yw9mjlpJKLCuF_BR9Nz02AGfFzUcflLxBdigGIgCiGkznLoPD8Xf7x7_2ooJVFwiN-jlauurkfZPm6mwiUCuV2j16LpqxGzJtj7vdZLxOmfBad3L8n_AVcLiUzc_BGTtyDSoExTpv6KoYbjsAXOy0Z7NBZFJzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇯🇲
وینی و عشقش تو تعطیلات در جامائیکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102454" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102453">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
📹
🔵
🟠
پخش زنده بازی دوستانه استقلال و فولاد ساعت 17:30 از لینک زیر
👇
https://t.me/+E5pLb4kNVJZiOGI8</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102453" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102452">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کاسمیرو به همراه خونواده که دیروز به این شکل بعد از معارفه عکس دست‌جمعی گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102452" target="_blank">📅 19:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102451">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZFhdW7J6luFZX7Jb77gaxcJvVkrVDteMHgAHEUZ7nJ9wRk2Xm0eafR4UqtS601bbL_RBb0QCnzScOjxhG72sClSMfZqICiFMM1MA5olCoox76cjs9v1YscAmn1_ub2Za9KIiwFD4k2qyJ4B0tIbW0xwiDVwD4uxiLyejz7Dg2rd1D9hjOKn3DIxjbPo3yhsF-Z5pfdEfi4uomLXzNZTy53uQEwUzDNVsB2kLlpsA7THPYod2LvgUQcFDyVqtysyygwDS0rw6JspSqmvZ9Lv8UitxAgQfDedTQE2QPnYbSKPYsct4kDMoO-nD6Vq_ljDmmoD7a94AeN8Izwn3u30SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
رسانه ESPN برزیل: رئال‌مادرید هیچگونه افزایش مبلغی در پیشنهاد تمدید قرارداد به وینیسیوس ارائه نمی‌دهد و پیشنهاد فعلی همان آخرین پیشنهاد تمدید قرارداد است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102451" target="_blank">📅 19:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102450">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMa_FKrCAxViRNGLZjbuRvoJB7wQcVRELc_s5YwW64vyvQIHFRan8NU1C9QWVj0IHPTsOl8_roVtc0tGKEAlfyuo8kJLYc7ZuARb-teVcLmc8qD4Ky78Jk0tI1wl6s0HRLl1BTWCVJ1783UG_TW2hN2tz2wPxUGJ41ZZIN-O6S81UbXCbVKs2zwqYsmrNW4fTsNKOV9SxKb-UBD3svaIVgWIHDnO9C5k5S9-eBW2DOsmgeddBK893Ngv8kYwyaf2YqW-G8VvdE1DV9qsyFvxXzMARYD8fsjH9ig_9Ois7YNvz-gwE2u8IX8NX1Ztx-xd_EVzROYddABJu1veQEfUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
اینفانتینو: جام‌جهانی ۲۰۳۰ بهترین دوره از تاریخ این مسابقات خواهد بود چون در کشور زیبای مراکش برگزار می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102450" target="_blank">📅 19:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102449">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHlrNNnRpDfCiearNE15Ib647TUrFBjfCG78MAfhbn1Rh-v7Dc_CLmoPCcXY-4233qhEKrlMIWWGomoW0DchrVLaqyyHgCTr0r2Ze-diNJ9l_egITquzbo3DgnzU1HYTjyjSKJkmtC5kYiwCRBZPx4ZmamUtrvTwH66YFnN-vQssYCnd8OgctpaIUhZT1yGSWzg8tz1uRaAJMuFT0j2eJY3amy2ZQ_kTYHV2uQp3jdM2ySktPbyOTh2csS6Ndz9BIYEIMnDozs0orCa0LmU9EaVgRblli7ORJ3vfwn9zXh5Ac_YBptYfduGBxRp7Gt3qkdMXWYHWbnmm8gZmGmm-uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس تعدادی از بازیکنای فوتبال
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102449" target="_blank">📅 19:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102448">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSV58_GHZfiP_vgQ9ceSGKTjRGRtLTBgELFpOmEY-g4WK1eoM203RHknVKJ3WcT2_SVNGc072Fu61MlZLUJ4gbxTm9yjOsF4Ttij9z_EPzQdm4DpvDDKecwaoae9A_YQAIP8iXu0ImTOSKOPAUJ6vyPN4wYTRsmXTSkG6CGBqDt1ze2PLpG14xOghyznvq_fKY_qgouD9vq6Tqif-D_3E4N-7GIXeYFyl1yduN9exb3T39D1v1ti-kWAmWGhAF9OaQsroN5pvxdCYR9otmyV9l2lIviDx04MX7xZ5n6eT2Sh6ObqNIBy1zlP8Shm5oYQZ2FEWzrBPSnWpngxzl8PcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
اسپی:
انتقالم به مادرید خیلی یهویی اتفاق افتاد و همه چیز خیلی سریع انجام شد، رویایی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102448" target="_blank">📅 19:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102444">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bzQuC6lumdzvQ6c397dNbuw5i-y1nMmtxwbhI5z7PiJIeJk0dCZYQQhmjeG3gVSMEg52fLFwR8DjQJ3ZIBu9GRIyGlS60pmslpKqPfM7kH3Ikz7IuhiDvOXLRFTo3MmWqTAlLWNx3l1mr6el2PWVDchsUszbLJUhosjOSUYtecVU7u1de81z7BVv4xlGpxak13S85-V9TWnJmzPcJArb1hkv0UYoC2R3GkDDd3Ff_3STqAa5Q8oQ0Vo2dwhqfQKiIIzE4DJWwf0HthAIDPraO2hYN1P7r3wpRvPtNCtA5S7eqlLB3nsiXplAe2K7E81iMSaar2ec5kKKO6wsJtLpnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u_7kCu6aShk28ERTgKCTOMbN6HeQC6iFLCoQWVw0XRoHymQFr5BnCBPdu-tPLehOlAE_JbtC1aWTwVp9ooIwvpi4PBJyjOydMFIxJe8PEGKbiH6Db5Em2ShEF0soDcgkGAJAqx1qbmgtGRenvSxPDcGiI8vT0l8GSQQHglYraSDefusfXYOu5enxIy-hhNFDHy2ZMC5rOakLmB3oTXBLYxp5PCAe_rj9y5Kv8cay3w4EISfTp9kPpKOr84OT82waIpluaKJgzCCcvrGQ1DMufRu8hP3GDyo1A80O_T-Y2EOxl5CshLAJn9yZXcKNJ_lq5gJjlpVBdYkK1o2oCdfclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHETVVG8y7AUXwJjhuWBNp9_-nVBO25Dq3wnILoyB2_LacTjqRUkwV472V5foYJch0pFSG1NZ6nMbMBUZ7Cmo2rWFsPAp82e1gaH-2Kq9PVap5NiTX5-KXCfQIU5eRkUVXIquGJ0sgtMI1-UUtcYCAXOE9041LYODRZjOx4WNsvM6O1md0DF3dTPBKC77lvGDiaa-YexNt7CbbEdcqO9XkwGqukizOOjMfUeztpnhrwR7QmXlWy9RARH3074tDNJbjbO9pA_kWrtcMA0vvnHTaEaVuhC7QTlv8rCxJmirJuJ5j2vQMzGYqv3h62RFombL11URl5Ky8OL75zgOuOX-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y5XJjcRte4T84H8NRzsYIafSCfCz60dhxqLNMIhTr1TES3grBqIgr-t3Rg5XOHr0luuL9NGIiV0i9vJz3HkhyeOyZa3Lys-k8q4wOYJsckWo-BkmT_EBX_bhUlw1xszpCHaxk3h_AdFSvSRs1_4I7QMMayxANwPQmHBsZcV-TjnRBKUJ6NDYoJ-XRrDymaGyGwUEnk7tp7bRNC7i_xx-OAsZUOOFTbX8eFsQIVxffY6w9Ij-Qoth_ibLimk3W3M_-NbIInXz2GlnaJOy9m9uvmMHjP_eNzF_PiYd5eki9KfPVT1FCuUT9g2WsQ1lPiNDSiFYay7VndNFNwcx_hVw5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
عشق و حال لامین یامال با دوست دخترش اینس گارسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102444" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102443">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQZYg63xrAYXPTaSgwm5-q3wSu-anlA_bKmg6GN0lutjsAzCY4xfJqyHjA8Z-eef3bk0Vb__WEWKtaSXjdvAFLBA3fxoW9CxBWk4dKyX0R49N-hR9d6f9_O0oukvjOjlaWXFUJr20PSwL3JVdfn5WdgLdnI3KaVB9K4A9UxRW0IEf3bL5U1C5yUpBTP4Iei_YHzURDx2VvbXEzWHicv9dTUXi6CyS3z2FqhZP4M6Y3en1vTC9fPXhkj7yigUuzPUZgyB9KGtxU2c9c6-lIsz9SxSYmtH4ai4sHvQAXyjl19B_kUVH3si2Ls_FmTS9_KblCXIWEmGm_5mtIDI9D1Uhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی دوستانه مقابل فولاد</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102443" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102442">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3L44C9kf7DpK4oozH8KfWpxSV9s5AEnAuqM50rTJcxfc3PnDYiJcrEQ_TEU7k2poiTY0PX2I7mEv3zBVTvA-JVtohKuCXjLT3ArP0A6jX3V9v_sYXp6DESY6wDUGmcMv01ApQOdwDUQFWBBKSdsIVjrOmC4k0GXqPljebcYTXOHmlLls3Kkse22ZELhLvQpwuo5eQmQqbCNcOg_HB150iSMHqBGZOiWZdaDRvxNgZ3emVA5hAghXJSLpp0jPBWYbwcegP2lvF1Ezsg5_YJ0Ay54W05pjufXGQOsD52jliJBJq8MYcfwxMyD4kNlEVOY6ZOzSnqs4lnqLn3Suir63Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فوووووری محرومیت دوپینگ میخائیلو مودریک لغو شد و او به زودی به اردوی چلسی در هنگ کنگ ملحق میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102442" target="_blank">📅 18:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102440">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keV8rCoetCeXo6lytdaI_C7F4y75GvYKyRpb6dtcWewH-F2k6RLH_P2OGEF2vov2AVdc4p5tS31Zm9xsbi0zHX75JFiqke8L8asDOVN94_srCtMXadl9DXZC7XqdcBQZXc-n3uUsfBf9zRG0Lxi9YnYtfXco-wg_AERZi1THUN2ALyFs7iDjiPeIjDQzZte23Ry6bujPYByzeVx_-Hii9li-N2iV3whTCBw4mrzXQc2lfU4lmhgMPBnF-NjbpRgGrjSs8ab_Q_3aIugIDWZHU0KFKermVSDeYNKHkTuJTeGj89rpkfOJjEcR4yIZiVsVyw5smjPvoOQ5VCVdBp8-Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/re_L-KrFA1Cyc_TBXTWqhZ-mu6ckRvWnT_m3qdmQP5UH8vPDHOtxjJsgMnTAXIFDXQg7nSJr_qgm-pWeaJ1QNTcS6Zm6ap46MHnBd75J6MqfyAwVZUfSaeRU51_6N3npbXq-NcySs8atW3eMNQuN5OT_WMdX8P8TqPpBvJVzlnUtcJXmM-PiYDzn3QRovQ68lfpSaNtBNDX1PBfnQjWbLcQarZFX92RBgqXA2GCw304KRGYSx6w2jJLGmBvIwgGzcFSSMupS0JLIfBwmhLhDwdnW99gYZOIPkcp6riRrgBFZlmn0byyd4rn63xZyRNdsqEZxrZaWte5aAu7c6vXwEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیر شدیم و خودمون خبر نداریم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102440" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102439">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NL_bosH61kRC2OliQOKGXbnz_xk0GVXwl9yJ9NrbBPlhsmBQmC-hItNhSEYs2tuEbzADxJ1uBF12f0Ou7qJ2yjglFsKD64XkqBRABV6jgaY88yh8F_myjzaj2deIC9SoHp_qqT6eMvXNHXViVA-4pEA4EPaP300M5ypiykZVAkgxAuCkADlmWFRy9sQadwi0hNPIrpGTDCywg1p5YPjl8rdw3WAgauf1u7dj7MpR-tvaw74Zf8MrDrW0plLXtAPEupRDGdCtN1NqBvpGsXT3kakoiywEUKRq-KXFhH6FSxEieuUZhPJqLm8mxfeeXxk7OvzrGn__xn3nVPMLX1wyPrstc0T7YZui5mdvBsNSTYCuLpv0GJEpphF1dWFJOzazGRLPZEdyVT_bemdMAGnfD2E6X6bdxTv68gW9Yzhx7Ze2yoiyQwWFvY8NzpjNVEglX6uqLaVqnhixrwq6GJie-26w87Eh0GzII7_WU9WwX6aBUegWjgeYg7VASk6mFkzwEhq48a_-Fdtt5886j_KqSVQo1LHfvA11xQWAIHvgD5VUBrTXeWznSVBJqkJhGW4a5W0B52kybQQpl9mCpSKJUzoO156ABOZUVt_6j1PD-c6G8PsIC5fJhYcEscuHwfZ05A_0tMKE-rCfkraT1jcBPrl7oCO5f9WrJfjtvpdl2Wc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NL_bosH61kRC2OliQOKGXbnz_xk0GVXwl9yJ9NrbBPlhsmBQmC-hItNhSEYs2tuEbzADxJ1uBF12f0Ou7qJ2yjglFsKD64XkqBRABV6jgaY88yh8F_myjzaj2deIC9SoHp_qqT6eMvXNHXViVA-4pEA4EPaP300M5ypiykZVAkgxAuCkADlmWFRy9sQadwi0hNPIrpGTDCywg1p5YPjl8rdw3WAgauf1u7dj7MpR-tvaw74Zf8MrDrW0plLXtAPEupRDGdCtN1NqBvpGsXT3kakoiywEUKRq-KXFhH6FSxEieuUZhPJqLm8mxfeeXxk7OvzrGn__xn3nVPMLX1wyPrstc0T7YZui5mdvBsNSTYCuLpv0GJEpphF1dWFJOzazGRLPZEdyVT_bemdMAGnfD2E6X6bdxTv68gW9Yzhx7Ze2yoiyQwWFvY8NzpjNVEglX6uqLaVqnhixrwq6GJie-26w87Eh0GzII7_WU9WwX6aBUegWjgeYg7VASk6mFkzwEhq48a_-Fdtt5886j_KqSVQo1LHfvA11xQWAIHvgD5VUBrTXeWznSVBJqkJhGW4a5W0B52kybQQpl9mCpSKJUzoO156ABOZUVt_6j1PD-c6G8PsIC5fJhYcEscuHwfZ05A_0tMKE-rCfkraT1jcBPrl7oCO5f9WrJfjtvpdl2Wc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چند تا از شوت های کارلوس رو ببینید، زمانی که فوتبال تا این حد راجب کسب و کار و پول نبود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102439" target="_blank">📅 18:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102438">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=FDftw3jD30E88puM0LQcpAb47QuEajgMMt5tHiJaXAYW0-9EKkpcTEZIsQYGL_rAAlIzjQoOD3ReiqC6-aqfUzLIJoJHz4gBc3NS2L3RAHrCcx22JtmDp94fj8sH6n4jYaC4v2jOTFc1Ms-7W0Vpu1-0NUrI8SVRZ6eilwazTzw1CC3iVZa63HjI3UT1w0c1Kg9VG669KgRW4rLzU7SN8AKBpC3ZwAgZ3H7mF2cu0-95OjOT0AOCwsdpJHsQl4_ijVlhwiq8YHcsUHn1eYZZ-09eRgw5VUE6nnbhQS35w82dJnA4S35Teygty2Pnnj7QQ-q4BiReldZ3Yw3Xf8lWQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=FDftw3jD30E88puM0LQcpAb47QuEajgMMt5tHiJaXAYW0-9EKkpcTEZIsQYGL_rAAlIzjQoOD3ReiqC6-aqfUzLIJoJHz4gBc3NS2L3RAHrCcx22JtmDp94fj8sH6n4jYaC4v2jOTFc1Ms-7W0Vpu1-0NUrI8SVRZ6eilwazTzw1CC3iVZa63HjI3UT1w0c1Kg9VG669KgRW4rLzU7SN8AKBpC3ZwAgZ3H7mF2cu0-95OjOT0AOCwsdpJHsQl4_ijVlhwiq8YHcsUHn1eYZZ-09eRgw5VUE6nnbhQS35w82dJnA4S35Teygty2Pnnj7QQ-q4BiReldZ3Yw3Xf8lWQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی‌از وینیسیوس‌جونیور در سن ۱۶ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102438" target="_blank">📅 18:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102436">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Enf89d8a-hsxCNixKxhs5O-khys-usczGWLE1lI3wAuFaBCB4_ZK58MhnxFYg9dBoypvtrFkkKkTkRk8uTL9qm1OcVxJVxPgkQKkq4cQrQLYj5nenvsP85No0ME8ZCeiK0a-JMiVNSEGg7Jfc2dDUCM4CMdefNk2iWyfEuOYWtCAe9iUzOQs3w7qAcNgd041V5Q9mGTijzv4oXCyZMd4v3hUviBdhRKmM6UMwdibVGQvB29rjwuiW8mh2A1SwGaLZljSvlLXhZeTA-m7bsxoiXEOlYv1DDDgZMvlB0jauwIW7ZQ8n_rGPR56FwHZkfI9QYGoRbn_OVdc26hYC539_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OuIVEMn7AWEJiErIkilFuNI5BPA93p7WeR3Wj8-9AglB_mgGvFt2K_CDveUfPAop_ZjOMYCYZaBnBMvdPuspqfvtB1CZGNtQJGoTL-Fj1R2lq8wKnAPgPsUc5gq_vtJ3NlB9iww60Mhm8JbJpwtH6m6i6MM43esujHFqG5zg7YrJUEygPPsL38IfoGN9sBw3dDHhSszr8CBdI3pUsw7Ie-h6HBdL8ACi1xDlm8wFALZ9ppxhAAhbwd6Uw_Q4Bd7WW1iJtcTcj05qmOIqvsedslCP53P0ONE6mmEvU6ZmLCwiMYzNJ8bsuErmAoxwPmgfeSjsfbNp8bc3-pksAVmLHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
فوری، محرومیت سنگین چلسی:
🗣
باشگاه چلسی به مبلغ 10 میلیون پوند جریمه شد.
🗣
همچنین، به طور تعلیقی از ثبت بازیکن جدید در دو دوره نقل و انتقال محروم خواهد شد. به این معنی که اگر بار دیگر خطایی انجام دهد این بار پنجره قطعی بسته خواهد شد.
🗣
در ابتدا 6 امتیاز از مجموع امتیازات چلسی در فصل آینده کسر شد، اما باشگاه درخواست تجدیدنظر داد و این رأی باطل شد.
🗣
این رای بخاطر تخلفات نقل و انتقالاتی در دوره آبراموویچ مالک قبلی باشگاه صادر شده است. مالکان جدید این باشگاه خود این تخلفات را گزارش دادند که باعث تخفیف در حکم نهایی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102436" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
