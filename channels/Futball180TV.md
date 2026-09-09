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
<img src="https://cdn5.telesco.pe/file/V4lToKpjSDviDx3cL2dVUVl_BlVhYAOIAzmvbMWO2IwWQ4ZnQMiV5mPQrKwhdZseFAnRx_Kdyp4qUfDYmaiLuAPef37Wx6oicsKyX8VEGzByvNrWQs-bLlLiOBjPU0zfSdseHBx3wTcmkgrj3zkqZWr9NW6iLlUSIZ0ojH9G6FpIEzIzvff9zxgFt0R7TUmiQMHzGJaPMphIHvuR3b3KsfTftKIrlL4_8KjOONKLGf6gHzhFOQKoNpGSQwKru9VtBcShUFvc9X3HxVGA8w7xQUxs26fY1VwELmJWslRjdqjBWm9w7nSevNID7fHgOrmFTZhsIw0siuBInRdJRYtmYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 421K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 15:07:03</div>
<hr>

<div class="tg-post" id="msg-105992">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f76b6880.mp4?token=sqCOUg-nYJGZ4EytkRUcDdnhqsADBa_lVnbrS2vm0YB2jZwHD291a3145UdEDfW9J_ezZ6ovdO2v5gtlxQfGPzNoOHSMTanMoUWjuOW5OWNv4ElwICNU-OUoU5J-JnbeocDd8QuY-ledI9Vg0PMxi4fjY_ch069mWy3S_sMTCBfB0iOIkTx5TWvkbL9HNaQruEo-dfzxulVPQi4G_kRg1jwB6fQAkb_uIrh6-AMZGNCChd4AwnFCW7I9pDAK-pJ7QuVcJtUd7lC0HZ3NPrixGSzwEdhzIDP1xL30KqNmIW06ybrI_cDVVfgC9zHIvH7sxbAv6RqHxpDlXiuTURbCAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f76b6880.mp4?token=sqCOUg-nYJGZ4EytkRUcDdnhqsADBa_lVnbrS2vm0YB2jZwHD291a3145UdEDfW9J_ezZ6ovdO2v5gtlxQfGPzNoOHSMTanMoUWjuOW5OWNv4ElwICNU-OUoU5J-JnbeocDd8QuY-ledI9Vg0PMxi4fjY_ch069mWy3S_sMTCBfB0iOIkTx5TWvkbL9HNaQruEo-dfzxulVPQi4G_kRg1jwB6fQAkb_uIrh6-AMZGNCChd4AwnFCW7I9pDAK-pJ7QuVcJtUd7lC0HZ3NPrixGSzwEdhzIDP1xL30KqNmIW06ybrI_cDVVfgC9zHIvH7sxbAv6RqHxpDlXiuTURbCAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
ماجرای صفرهای ثابت پمپ بنزین‌ها مشخص شد؛ جدیدترین شاهکار مسئولان برره‌ای مملکت
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/Futball180TV/105992" target="_blank">📅 14:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105991">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6385fe8792.mp4?token=AkhsA3B1Jtad_fIttjuqY3Ai8IeQPIA2ZAN7uYZeWNZ4JCdSMHctyH1-atOUH5YdZoE-uoNn9HBW498pp5Led6CH7b_e26-dh4JLjGgaRKuZK7ZSRiF8vy_SSPFC8ku1t11dUviuXNVireyIWNLQRJtRRyN7fxeKI2LTvNIgZr7Znm6thuy7e4N3MqkWkxKx0os2Yjj0-E9jh5atCUCOgJ2ONvLHZUasmDpnbD-_G_tQYWtJ7kx3vc5DWHvEnBHzZkijPOXKukmLn-orxZh9NnuBSXc5CgBaaCPIrhT0RsPZuZrVnQzcIoSCFtVIUGoRJkfLdLUi2HACqLEkcAx-TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6385fe8792.mp4?token=AkhsA3B1Jtad_fIttjuqY3Ai8IeQPIA2ZAN7uYZeWNZ4JCdSMHctyH1-atOUH5YdZoE-uoNn9HBW498pp5Led6CH7b_e26-dh4JLjGgaRKuZK7ZSRiF8vy_SSPFC8ku1t11dUviuXNVireyIWNLQRJtRRyN7fxeKI2LTvNIgZr7Znm6thuy7e4N3MqkWkxKx0os2Yjj0-E9jh5atCUCOgJ2ONvLHZUasmDpnbD-_G_tQYWtJ7kx3vc5DWHvEnBHzZkijPOXKukmLn-orxZh9NnuBSXc5CgBaaCPIrhT0RsPZuZrVnQzcIoSCFtVIUGoRJkfLdLUi2HACqLEkcAx-TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇮🇷
🇮🇷
رشوه مادربزرگ استقلال به نوه‌هایش که شدیدا به تیم فوتبال پرسپولیس علاقه‌مند هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/Futball180TV/105991" target="_blank">📅 14:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105990">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBUuZYnpWp8PcE8WQSaQc9vOZb3vNqVERQRWcrU6l6JWMWGfYBM9-39mD6Wu-hKwV66NHfsN4p0LCHyAK7D9p-XNbf8j-S-EibtnGyPnq-IlJZUWJ1jy19_GQAtxZ0KZBi3tujwzRM39bu72uGQcFt2oVYAXvJPGPaJYUcRuskDr3ImO6riwNZhh1hgfbRkZkYqPqK8RaWEesIbgKLn3I5itDO3fKqxpXrGTFh1lVI57KPI8m7A7vr3rTUKHjtmqRbRhK-vE3A7xzWk6fEjj5UPyAkL6vfxpnPd-0lHmmYBNgd7SsO4xap6_DumUYqvXh20f0Yzh9PupmpyyB6kBQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
رقبای بارسلونای تحت هدایت هانسی‌فلیک که بیشترین گل‌رو از این‌تیم دریافت کردند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/Futball180TV/105990" target="_blank">📅 14:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105989">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3a4352655.mp4?token=kmhlS8e-s-j4M2xiH48KRo5SANETYD8mLyri9Af1aji9iPZnnzBYT4QL5PvoHVRhznrxuHEelQwQjMMxJLVRh7GEqY7QLvbmRCMa297A2TzfUVCgarfHeo4R8-lk5vgfafzzZdQvdvNBw5WvN659Il8xlOT-YQ-kLghdquCV84uzJ4fjoTq7686Yk-tVeBqBQoYrfu5-Y6AoGZ5wJJ8pUApPLH4eEUE-eciEaZuf4JNP-zo4VNiiB6iiL1aCi8YW6zCbrLf4TDzeNNHSy42p0mcf-g7jZyzc185UobHIt0VPm440G1E-FF9lAjpbTpmTkoAradERdqgCg4lVvGkiLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3a4352655.mp4?token=kmhlS8e-s-j4M2xiH48KRo5SANETYD8mLyri9Af1aji9iPZnnzBYT4QL5PvoHVRhznrxuHEelQwQjMMxJLVRh7GEqY7QLvbmRCMa297A2TzfUVCgarfHeo4R8-lk5vgfafzzZdQvdvNBw5WvN659Il8xlOT-YQ-kLghdquCV84uzJ4fjoTq7686Yk-tVeBqBQoYrfu5-Y6AoGZ5wJJ8pUApPLH4eEUE-eciEaZuf4JNP-zo4VNiiB6iiL1aCi8YW6zCbrLf4TDzeNNHSy42p0mcf-g7jZyzc185UobHIt0VPm440G1E-FF9lAjpbTpmTkoAradERdqgCg4lVvGkiLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
فرق زندگی در ترکیه و ایران از نظر خواننده ترکی؛ عایشه‌گل: مردم ایران به دنبال پول جمع کردن هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/Futball180TV/105989" target="_blank">📅 13:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105988">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3185992aac.mp4?token=U7HSTdOFjkQ-CPtUy4rNVn98qkPhYgAWHNXMj1mK2FqondM8WsMf_bmvdxWLOL_ZuSJmp8P_0hEK1478B8vl0i5GgoTyVJCg6wDSN76PA7OUv0dfZ8nVRoqzJu_mHMN-QvAKVq5Dpe1klFm8ED7wKx4qE0VOpYOBD6v-T1pYZlWO8I4P1pE_vz1TvJ_HQG3YD5tok0sy4CcE7oMw8fBY7pk_hRmAolrHG29XnBqBH4iQTWHL5ZFIpiT6_yBxO-injURTnd_wMxfi1I10LNXwY9HQJBVID3m9Y9uyL3UUBAVkK86Dvm3pmirmQexrVgR-jHR_jFmpcAwLcoTMsNmWNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3185992aac.mp4?token=U7HSTdOFjkQ-CPtUy4rNVn98qkPhYgAWHNXMj1mK2FqondM8WsMf_bmvdxWLOL_ZuSJmp8P_0hEK1478B8vl0i5GgoTyVJCg6wDSN76PA7OUv0dfZ8nVRoqzJu_mHMN-QvAKVq5Dpe1klFm8ED7wKx4qE0VOpYOBD6v-T1pYZlWO8I4P1pE_vz1TvJ_HQG3YD5tok0sy4CcE7oMw8fBY7pk_hRmAolrHG29XnBqBH4iQTWHL5ZFIpiT6_yBxO-injURTnd_wMxfi1I10LNXwY9HQJBVID3m9Y9uyL3UUBAVkK86Dvm3pmirmQexrVgR-jHR_jFmpcAwLcoTMsNmWNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇪🇸
توصیف عادل فردوسی‌پور از ریدمان فوق پشم ریزون دیشب رئالیا در بازی با اینتر!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/105988" target="_blank">📅 13:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105987">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/058b97f620.mp4?token=sfEGUGlUGzQBAwzgcfk_p_sidZN0aSzGiTFltVIx1lFbIRydHyQ8v_jLFaHUhQXfaSrLT3KyDJtBU23dYxczaAEGTRxy1kiWdBKwrWVpe5TXLig2ABd8_GCvTTcsx7rkS3ifcl-wJ92QCkjOsYppwfPk8TD5HR7LbfonWdLr8O-3PEpNuRMWRMZTieP7-rC79w6y6AfDMay_J_b31jewBqrFY7Cxool37oNc42F04fdXNlMbiOQaRsGj3WbQc6iCXJZolKjZQUw3sdAynUxKYbTktnuoc0eugeZVS8A_mjuG5Nu8l7wnjyd3NGbojcrtdoOA_1pu1lYgsevhVP5iV7Sve25PBYtiQYpwCaY2Gdl-rgqFAvCvgyeIQ2woM-BwDLz-rtOnndc_sJr1CYNZteG9cnYwSgGLTm3exa2Gw1DP1F6U_Wn6pRfT-qYZFORaeFMnLC5PZeyKHekIxAhdeOY2hdMQIOaaGT51SR6nZml1D0LFZ0OtLQk2JVrgloFji2mXDf33SJoL2tiHfECI2xvG3X-1add2kT9YOa6FGrQmYwUgm3TiEkqvC2Jlra8_0fQAnJ2Cdfo3DeiOqkXPibs1rbyKWmlz4RchpvGnZMOkyeJoJ9shN75q10IzO3VPiRsagQhNNLF_NWvGxtB8xhrmtfHf-uf92Hx5zfTfa5k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/058b97f620.mp4?token=sfEGUGlUGzQBAwzgcfk_p_sidZN0aSzGiTFltVIx1lFbIRydHyQ8v_jLFaHUhQXfaSrLT3KyDJtBU23dYxczaAEGTRxy1kiWdBKwrWVpe5TXLig2ABd8_GCvTTcsx7rkS3ifcl-wJ92QCkjOsYppwfPk8TD5HR7LbfonWdLr8O-3PEpNuRMWRMZTieP7-rC79w6y6AfDMay_J_b31jewBqrFY7Cxool37oNc42F04fdXNlMbiOQaRsGj3WbQc6iCXJZolKjZQUw3sdAynUxKYbTktnuoc0eugeZVS8A_mjuG5Nu8l7wnjyd3NGbojcrtdoOA_1pu1lYgsevhVP5iV7Sve25PBYtiQYpwCaY2Gdl-rgqFAvCvgyeIQ2woM-BwDLz-rtOnndc_sJr1CYNZteG9cnYwSgGLTm3exa2Gw1DP1F6U_Wn6pRfT-qYZFORaeFMnLC5PZeyKHekIxAhdeOY2hdMQIOaaGT51SR6nZml1D0LFZ0OtLQk2JVrgloFji2mXDf33SJoL2tiHfECI2xvG3X-1add2kT9YOa6FGrQmYwUgm3TiEkqvC2Jlra8_0fQAnJ2Cdfo3DeiOqkXPibs1rbyKWmlz4RchpvGnZMOkyeJoJ9shN75q10IzO3VPiRsagQhNNLF_NWvGxtB8xhrmtfHf-uf92Hx5zfTfa5k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
💙
بختیاری زاده: بازیکن به تیم امید نمی دهیم/ تیم امید مهم است ولی شرایط تیم ما مانند تیم های دیگر نیست/  فقط آن زمانی که قانونی باشد بازیکنانم را در اختیار تیم امید قرار می دهم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/105987" target="_blank">📅 12:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105986">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fx2-7pu1dhP8W7xYhRIW2zEPoXSpTbuWiBSlhN59NVUUGoLEXJiE_gkzrq2HEUA-p--xPUjDGa0jBSWwc36h3df7cAbnr8XDdD2gRyclUxjw9eIRnPHvD61kcmGgFEu7yEQjZAb4Aj5KVQEYi_PKlfgquoeveaOVnEw-l2iKgSIYrw0tFX0rRXT3pAZsvLTmF9oXLaFA9vw3UQoN24HOi-TXdGZo6mhSfE7D5PlDil-sAcvs9TATMKeCjLlZZRYrWjPF9Bs7Wl7Ml5NWJpVmzZUBuLmI65N-jGx4lmcyn_jl00BmEpESTyPSAoTDa77DyP94hrwGpUZKDbSTOWImMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
⭕️
⚪️
یاشار سلطانی فعال رسانه نوشت: ‏در پرونده فساد فوتبال⁩، برای تعدادی از مدیران ارشد و چهره‌های فدراسیون فوتبال به اتهام اختلاس⁩ کیفرخواست صادر شده است
مهدی تاج⁩
‏محمدمهدی نبی
‏احسان اصولی‌صفا
‏تهمورث حیدری
‏خداداد افشاریان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/105986" target="_blank">📅 12:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105985">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105985" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/Futball180TV/105985" target="_blank">📅 12:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105984">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z026uW3CunrBYV1BYH69uKYViT0FAXIFBluk0pIAHR3pmK5Yq_8VFYE3rKNa6YjmRKg5fvWfRaqFMmBFnDjyuNO6_jDFGhRmXeniI51MVGtJboEcQ-CPGrFRg3Sl0Cz7rYxmkVf-rlRoUe5WJ8-Dgeld6x01RzV-rePpoQEtd-UBxw1FN7PSm2OR3AM-mAyKEsajaFIxxISoRlNik4dYgVFJhqF1IDgp26AxhWXpKeqrV2YoWOGrYKI6J7MUWFwV3DDGMSd3UVFXryoQJ16JnKLHFsuSTccE0DJBuJ6GWNoVwFFI5b3Y2Gve7IkdWBUqPtMAYnwhuErkW6SpBPtM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
اتلتیکو مادرید
🆚
لیورپول
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در تقابل‌های اخیر:
⚽️
اتلتیکو مادرید: ۵ بازی، ۲ برد و ۳ شکست، ۸ گل زده
⚽️
لیورپول:  ۵ بازی، ۳ برد و ۲ شکست، ۱۰ گل زده
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
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/105984" target="_blank">📅 12:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105983">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cd51b2d93.mp4?token=bhDwR3jApRuwb9-lYiOYy5_w5oti8htsbQsTJ0akkz7-_swaQtugn8AXA5FlLU9Wzjz48QYdJqMqtmVRtaHL6NBGMsW1xbBpyYuiZTz77MkqM5b3JjYmwCdyh6BIlXos--C3cnAz-SvvSTDBHC1AX9v_2mDspVJ9Rt4LjscPGogPSrxpPWgjkkBhzc2BsolYZUJSGb1GpF-I48ZeRz0JYVhCvLEZ7GJEC4rtW16DGlEejpy1V4Q-W4B6L_U2IJjVwo2FfAvj2Utfs_Yw7-zN8u5NFTuR2LmxBAxH0qAUhmzapSisUkXBNSTnFCuSMIydtfNun9viRnTsT8cxax2WN28XnbYSzqmddAfvpEoHUsTXfp6Pud7AoS2SeJ9rcxvWXf3LsffGPBAdQ42CsCzS3LKBvUGc-rP88QoK_lm6j_mW_3rjjJYPEpDQSMjMJVt4wol2ilfaYmxTh6grYo8nMsOBnkpxFS6gPlWz3cb_gheFLce_GM7G83qOjZAUrxkQvkHfdIAi-EZzFVQ-8v0FPIII37Ha7oBEGTEF27tx2dhqln5aUrai-5cBs5mSldsO5_twF1uAWvMvjTx4wuT5vO3WZTkSsQFoRqH835p9G19IK8wwEr8LwICW5T75Gry5lWvvaRk47spD0TaKsUwAaDO7jLG-pbs7-yE76YzgeTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cd51b2d93.mp4?token=bhDwR3jApRuwb9-lYiOYy5_w5oti8htsbQsTJ0akkz7-_swaQtugn8AXA5FlLU9Wzjz48QYdJqMqtmVRtaHL6NBGMsW1xbBpyYuiZTz77MkqM5b3JjYmwCdyh6BIlXos--C3cnAz-SvvSTDBHC1AX9v_2mDspVJ9Rt4LjscPGogPSrxpPWgjkkBhzc2BsolYZUJSGb1GpF-I48ZeRz0JYVhCvLEZ7GJEC4rtW16DGlEejpy1V4Q-W4B6L_U2IJjVwo2FfAvj2Utfs_Yw7-zN8u5NFTuR2LmxBAxH0qAUhmzapSisUkXBNSTnFCuSMIydtfNun9viRnTsT8cxax2WN28XnbYSzqmddAfvpEoHUsTXfp6Pud7AoS2SeJ9rcxvWXf3LsffGPBAdQ42CsCzS3LKBvUGc-rP88QoK_lm6j_mW_3rjjJYPEpDQSMjMJVt4wol2ilfaYmxTh6grYo8nMsOBnkpxFS6gPlWz3cb_gheFLce_GM7G83qOjZAUrxkQvkHfdIAi-EZzFVQ-8v0FPIII37Ha7oBEGTEF27tx2dhqln5aUrai-5cBs5mSldsO5_twF1uAWvMvjTx4wuT5vO3WZTkSsQFoRqH835p9G19IK8wwEr8LwICW5T75Gry5lWvvaRk47spD0TaKsUwAaDO7jLG-pbs7-yE76YzgeTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
بختیاری زاده، سرمربی استقلال:
صالح حردانی و وساطت دیگران؟ این جلسه برای بازی با پیکان است و قبلا در موردش حرف زدم. تنها چیزی که روی آن متمرکز هستم پیکان است. همه بازیکنان برای من عزیز هستند اما نام استقلال برایم مهم تر است و اجازه بدهید روی بازی فردا تمرکز کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/105983" target="_blank">📅 12:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105982">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72b7d3e3a6.mp4?token=dcmPxbcPOrzAbq11Bvwafo-VN9AzUCyrT35PUFjZTgRrcV6YQToRl3GhIc72v76If-7GIYmasZswqJXROaCJDGZD4DtHrwPUXwFwkPZ31bOQQ_tP2DAhAsZVtPcLWKmxQfRl4mKu1Trt2-Iuj4cwhsuGac-XxD6IvH2KBgFnAWX6g4dPKKKSvdF1xgZm9jjC6RiFk009mO91CpifagTg_zFEeBwClKU3dpmnuFqBfsfh-RQ26ccsyWjPipiYAl9c_-sBQb7LI0y0Kbz13Ml7PlRqwS25vHlF9ahKaVz696JRUgL3bvQQgiFhAgKbtC_H3iaDNdTtIH51YsOcVNLxFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72b7d3e3a6.mp4?token=dcmPxbcPOrzAbq11Bvwafo-VN9AzUCyrT35PUFjZTgRrcV6YQToRl3GhIc72v76If-7GIYmasZswqJXROaCJDGZD4DtHrwPUXwFwkPZ31bOQQ_tP2DAhAsZVtPcLWKmxQfRl4mKu1Trt2-Iuj4cwhsuGac-XxD6IvH2KBgFnAWX6g4dPKKKSvdF1xgZm9jjC6RiFk009mO91CpifagTg_zFEeBwClKU3dpmnuFqBfsfh-RQ26ccsyWjPipiYAl9c_-sBQb7LI0y0Kbz13Ml7PlRqwS25vHlF9ahKaVz696JRUgL3bvQQgiFhAgKbtC_H3iaDNdTtIH51YsOcVNLxFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
🇩🇪
🇪🇸
دیشب چهار هزار سکو برای هواداران ویارئال تو ورزشگاه دورتمند اختصاص داده بودن که خالی مونده بود. فقط ۳۹ نفر از ویارئال حضور داشتن که طرفداران دورتمند اونارو وسط خودشون جا دادن تا از تماشای بازی نهایت لذت رو ببرن و البته خیلی دوستانه تا آخر بازی کنار هم نشسته بودن
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/105982" target="_blank">📅 12:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105981">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d0af12019.mp4?token=iQpUsEFqK7r_7FzKJVyI_66hJys8fOexBc8D7N8msfG4qvJKayqHgb_QbKVPWwmLcpGF-nb9icbrEPbdOj6p3WG_G6f19R0nv_hqa294QcXIjhjY-iSLisf56leT793pMA1-bZzHpdPo5wWtbxXqMOLPT5alvyfz01aLLAOnxkpFoDEuXJ6Arjd6Ren302pcJcQncB2jl3rbc-VcNdoWImEsv7c-P0qbz2B-DJTxHrjQwYNUgBfv58W1AA1OkiY9nPEt_fzWe_4Yh4-5R4bskOB7hWX-sGmBRGeXJEz9s0BLOYsY6Q6_ZMiBw63_hvvdXL-4lDgVg5GOKwN-Z1nrgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d0af12019.mp4?token=iQpUsEFqK7r_7FzKJVyI_66hJys8fOexBc8D7N8msfG4qvJKayqHgb_QbKVPWwmLcpGF-nb9icbrEPbdOj6p3WG_G6f19R0nv_hqa294QcXIjhjY-iSLisf56leT793pMA1-bZzHpdPo5wWtbxXqMOLPT5alvyfz01aLLAOnxkpFoDEuXJ6Arjd6Ren302pcJcQncB2jl3rbc-VcNdoWImEsv7c-P0qbz2B-DJTxHrjQwYNUgBfv58W1AA1OkiY9nPEt_fzWe_4Yh4-5R4bskOB7hWX-sGmBRGeXJEz9s0BLOYsY6Q6_ZMiBw63_hvvdXL-4lDgVg5GOKwN-Z1nrgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🔴
یادته آن شب ماله‌کشیدی؟ شاید اگر آن شب با خداداد برخورد می‌کردی امروز می‌توانستی پاسخ پسرت را بدهی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/105981" target="_blank">📅 11:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105980">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🎙
🇪🇺
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نظر هالند درباره اولین بازی ایوب‌بوعدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/105980" target="_blank">📅 11:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105976">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XzaDtV-DnlkZrVzo_fovfsVUR4OHLlX8MACrucV5A_G0QPk4C_4qwGPjFPQmz-wSod-W0Ives7vLInLKMM3Hc5uEWKn2_IGLloJiOVKhYGsJzT6ZsYYIoF3wIaCdROBzd1TmV40bzafGh_6t-NeUkuZwmyQQY2KcWg6L2ZggfYbL5vvHIu1A2d8qVDclXxzCaBsewMHreGrRDYaqa0O3gMTwP-51HkHkYJTsfuQRZjTGHh0QTK0r4KEjPR8pPTanlPgTlKYPel025uNVzox6w6B7GPbV5Qh9WJ5a1m_07YSbj2jjB2TWqfR-qoFhFFCr2JeStJN55rCJbDqYjgw5VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tPOn-GOZxx6BYzzsp_k7BrU0CQ4G7ERqSs9NiOL8z2nwDzuF_wvZSAazH9-EMaW63faGaxMP9roCv-jRn_OnN70zViUxMkNxQgs75xZNL_tJ6F7Eguzp5wRbD0e696hV9OgaFXI60hEceVeAZuCLSUn58KJ7lwoUQIdnQGwRoBirxlKa5n9f9xLVhlqjnzFKWXfajdBXHNLnaq5_0raIqJfs45NoTfyK8KB25gJhIjDmQylT_x14HnSN6AA2BWABKb3hI8H9woAotgY2dU9PxmyUrBWVpmi_Hxk1MSA_0QrUub6PtY0X4wzpEnJQyNR6GU3XDiSC-cun7TV_oo38qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S-R4ENLxYdd1dcofDGfGN3CcOhtjbdPIQYlzm4Osfj-RvG8fH9gYppHDhJeiGl8gregBRwwp48nR7szX2A0lPM_34KdUPGhbzAO3seRtNX9nj-yusZFF0H2lTgrFQbnc3s2MZhKCcGtQBK7c7Y3oAK9FJAtUdPPw0GLl_dEqOi50PlrWYHh_4D8cw9_AacMFNt9Gqwh2wpyqXcFHmDSigB4zrrGLJ9R2AdWfr9GWPUj_TbvlNqwZ0yD6vJpbuUDJuUkluhWBjO8lKv-teOpruiojTTfHpnBtcGQ6U-cmVO84X_VAlJ51YsVGIHIm2Kfve62hCzD66cp9nlLdNHbAtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PUPdWcEsqZ78_42BokBn_rc2LlAgqr-UyF8IGY2fuuv09zCQlm2Sh0rrb31tg4nv94wB5jUM0N3CgCcuThGDztL1umvNqPPbNzDUZACDbT_wOnGQqFz_K6AMVGvsIUoQQBevuMpw1Pfe_5f2b4mzPAj_Tdhr0ScCsTYXYTa22-DVernpJskpLXVWpDH2fPrjFJQPxXMjcM_xUhXfwxW1wtQyv-k2gPkgL43mB2tjsUXRLQ-H5XqmbQmhC2nLOrnd4at23YKHmNWyU0ECVJmuZWtgthe94TJJf4jeX_S5dIcwP4CbsD0LzGdjQ3-mdohVYuoAoIXK-sSUAsm9rDnt6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👍
✔️
🇮🇷
تمیز کردن سکوهای شهرقدس توسط دو بانوی بافرهنگ پرسپولیسی پس از بازی با ذوب‌آهن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/105976" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105975">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5rvpErIHOJEnSN3OzppyGJuTvcSWuaRSWjXrehwk8aEj_vYKl4TsqRAbqf18LqcaaH18Vz-Et-B3McYgzQFDoYdlXCicWYleI-maua3XPNzT71vkmz_lUQBDWCQHTKy11TKwUy2RJ4X1X2O9AE82TQs-LDSR2Ar61cZqoFdJfEvCKJmovTIQpZGGJM-IVEcG72EV0ztQjbZ9VVtmN4IF0vQUidXtX15YMR2gt1WGh1UZXIYKTT0xRvYbs34DlAMhBWjN1KYQZcnDAiZpkNOJCc2y8ACF-0kpn5DIIX0P_FN7a4TD2iWGPVQleGx2vgHJfKs6IIKQZZ9BYqe_qdoXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
تصویر جدید مهدی‌قایدی و خانوادش؛ عکس زنشو هم سانسور می‌کنه تا مثل قبلی بگا نره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/105975" target="_blank">📅 10:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105974">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d195a639.mp4?token=gRZgHRJ3eXafP4xzPmDqyBV_-qMVlAKUis3b9y92sa28BDGcA6ugFNbZ245borYLq26DMd0gYS1Dwp1sx59YotrzxlsMavLjBkKuPACIc264LvCqm2TIZGmKOYPpjVhEcnRENGPd_CKCuSQdkf2JoMwusZPlT7OEDgCkotys-ehVbpJAjjX04sw5qTuVYGXAnuts5KEfOO0m-AjszjHGwEkSnwFRXuoJqGmoJClK76gLIcMDRMHBgpFjMbF4HlNt5h_O1wp-Xnm2mawq_TODVNysZtiFa-Px3wmhvzhy2aX9XA2VzC7bfhPSHKiYEYNi_UH2XHLIOhURIV1JyiKf9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d195a639.mp4?token=gRZgHRJ3eXafP4xzPmDqyBV_-qMVlAKUis3b9y92sa28BDGcA6ugFNbZ245borYLq26DMd0gYS1Dwp1sx59YotrzxlsMavLjBkKuPACIc264LvCqm2TIZGmKOYPpjVhEcnRENGPd_CKCuSQdkf2JoMwusZPlT7OEDgCkotys-ehVbpJAjjX04sw5qTuVYGXAnuts5KEfOO0m-AjszjHGwEkSnwFRXuoJqGmoJClK76gLIcMDRMHBgpFjMbF4HlNt5h_O1wp-Xnm2mawq_TODVNysZtiFa-Px3wmhvzhy2aX9XA2VzC7bfhPSHKiYEYNi_UH2XHLIOhURIV1JyiKf9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان خداداد عزیزی و عالیشاه با صدای علی دایی
😂
‼️
🚫
حاوی الفاظ نامناسب.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/105974" target="_blank">📅 10:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105973">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32b4f4b4bf.mp4?token=Mxada3QFpM6Hph9Akrp1WWFQJjdIKl6lYPfQAptWgtYaoafht_7C0iVB82d731VcCF29I7v33tmZbIvFh-TMwJGggb_SpWhVZ5u2JuE5PeFxTdZ-p3jNTmPCwhmltNxMuxIER2kEVqKJS1ZTzl5U8lrzVkc1D9SoyVJyR58CoNK9pEeL9YYIM1oM65wPXRiVZwtH7u17W_tB0CQd8fjtW-jFqvUimXdCOSOwLr0dHmGiTpJBGagSjZPTFCIeufZKwlXVkMSCrTgL4jMrdAiElPiybOt9PA8K19CE5gnJlx2W__icxtO5as1Bo__2p-KYlnNdmZivhQwtrQTgYNPMcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32b4f4b4bf.mp4?token=Mxada3QFpM6Hph9Akrp1WWFQJjdIKl6lYPfQAptWgtYaoafht_7C0iVB82d731VcCF29I7v33tmZbIvFh-TMwJGggb_SpWhVZ5u2JuE5PeFxTdZ-p3jNTmPCwhmltNxMuxIER2kEVqKJS1ZTzl5U8lrzVkc1D9SoyVJyR58CoNK9pEeL9YYIM1oM65wPXRiVZwtH7u17W_tB0CQd8fjtW-jFqvUimXdCOSOwLr0dHmGiTpJBGagSjZPTFCIeufZKwlXVkMSCrTgL4jMrdAiElPiybOt9PA8K19CE5gnJlx2W__icxtO5as1Bo__2p-KYlnNdmZivhQwtrQTgYNPMcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
🇪🇸
شعر مایکل ریچاردز در وصف امباپه پس از درخشش در بازی دیشب مقابل اینتر
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/105973" target="_blank">📅 10:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105972">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf52ab1a36.mp4?token=dWHux1f34gEkg638O-FD2zrank3mTOGIf3vuTB1LuEviKTecrfLcZnmSfxUgOxkyPvG4sYCAbpCD0qJfKHqYxmdFa3gYXAVe2fNs_IuqlUKPd7vdQwhQlZAUUOCbZP6qrNknL7tu0f15sNc-aMjMhuxm4DlNRMDVc2SsYOxL9_Xc2ou_0NRXzsy2_0u-gsdtvpW1WUzayMXm6DDBpSYyFfSQA5dGfYRIxAKGIZv-zwEByi0j2iq7Tk8PD0gFL4gPJ6K4ikueSsQgcRT66-PbZnzGH1-cM9Tvj9uHcMJLlOCQ8mU0d6EsSSZEvpibHA39Mc_GV1RGIRJsOddaxk-8yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf52ab1a36.mp4?token=dWHux1f34gEkg638O-FD2zrank3mTOGIf3vuTB1LuEviKTecrfLcZnmSfxUgOxkyPvG4sYCAbpCD0qJfKHqYxmdFa3gYXAVe2fNs_IuqlUKPd7vdQwhQlZAUUOCbZP6qrNknL7tu0f15sNc-aMjMhuxm4DlNRMDVc2SsYOxL9_Xc2ou_0NRXzsy2_0u-gsdtvpW1WUzayMXm6DDBpSYyFfSQA5dGfYRIxAKGIZv-zwEByi0j2iq7Tk8PD0gFL4gPJ6K4ikueSsQgcRT66-PbZnzGH1-cM9Tvj9uHcMJLlOCQ8mU0d6EsSSZEvpibHA39Mc_GV1RGIRJsOddaxk-8yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
نادر محمدی دیشب برای سومین بار با اوت دستی تو روسیه پاس‌گل داد و حالا اکثر رسانه‌های ورزشی جهان کرک و پرشون ریخته و گفتن که این بازیکن قشنگ به سیستم آرتتا تو آرسنال میخوره
😂
😂
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/105972" target="_blank">📅 09:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105971">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d2267479.mp4?token=VC2nw6_mpOW8C0smenGGq38k1IuhF09_6elSQQWsm-MToB3hC2-XLDXcf7Kwzmfdy-Oi8r2rRftIKMmT2TpgrMfPtpIIrtq76E23QXinnXNL8MDRSEUyCD6dVRitO6ZvC0aQyOlpiMSAbi1GEnlRrk2cl0GvgjSHQSiTlAJu7l6qBbEEKIiI0LDznN6T1PnALTUC0ye8IIohbXhGIOT8wP7SVgBvfkBrmMgxZ6-pZqQwcikOVXLBw2A_UYApWwlteOmwbkpLyPTbcHghnU2HzsFctaG0tQYQgTdyM1On8cj4vNNftjAEEoapHYtEUClYTn3S0QOFCauKQqqu1ISaeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d2267479.mp4?token=VC2nw6_mpOW8C0smenGGq38k1IuhF09_6elSQQWsm-MToB3hC2-XLDXcf7Kwzmfdy-Oi8r2rRftIKMmT2TpgrMfPtpIIrtq76E23QXinnXNL8MDRSEUyCD6dVRitO6ZvC0aQyOlpiMSAbi1GEnlRrk2cl0GvgjSHQSiTlAJu7l6qBbEEKIiI0LDznN6T1PnALTUC0ye8IIohbXhGIOT8wP7SVgBvfkBrmMgxZ6-pZqQwcikOVXLBw2A_UYApWwlteOmwbkpLyPTbcHghnU2HzsFctaG0tQYQgTdyM1On8cj4vNNftjAEEoapHYtEUClYTn3S0QOFCauKQqqu1ISaeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇺
🇪🇸
اینجا لیگ قهرمانانه رفیق! قلمروی پادشاهی رئال مادرید.
🔥
☠️
👑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/105971" target="_blank">📅 09:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105970">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15481b67bd.mp4?token=UvHbxnXDCTjXOkjXC-Dg25v9JCfRQt5ESrY03x6j5iTTpg6jtH-iJDxXT4jTqwolWE_OZDd59aeN_NVpXFP-uwXFijTHQVWHjADvlMvAzw9WqyhecUUbxigBn_Ezfz5TjHAcweWBE8XMrEEmYujV5cfQ1n2Xra6C9SWoxN70xTUyl_de58NUMI6LAxAwPWWXdR4hs_hISyw3TIGIYqSk5jeiYeNuTGcTyrDkqYI4EXZC0IXqZTV5CB8RijDL9oI_mgXZ1Vh3OxvMjl6VyxatyvsKL6Wo0qeWWrJeNGV-5Z5lZhYQ_P2cAJmaAO7TATWUmQlkQfYEKDdL3PT5U7U3-nbr8FbL3VV0lkPBDwD-4D4QuVgVOciJUDkVLCiJM2T0O4eMvc1DZGK345wcqu2lEZEbmnSwF9Ws2CPb4B_PQgEy2ljy9BomRx7AhHFCCyIMUXuXiZj5WCWOQCWgPD6ypUnC_de40-6TjZfSROX2XXD9HxA9TNEq5VW4H-pIPdLsRVzmlmD4LuoLNlrmoCTY_GvKIdt38OphqSgaQb6S6CWOz2eaCw_UP7nMFNWEEaagL0BJXvkJZA3wVBcjdo_7Asbv_7jJvmgV9fe3CRiDPbDZlJXSX4Q8QRCi0vaZXMlNv_H445amd8HcZhVAKrw8I-lpLZUz6z7k-klkWdoVtUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15481b67bd.mp4?token=UvHbxnXDCTjXOkjXC-Dg25v9JCfRQt5ESrY03x6j5iTTpg6jtH-iJDxXT4jTqwolWE_OZDd59aeN_NVpXFP-uwXFijTHQVWHjADvlMvAzw9WqyhecUUbxigBn_Ezfz5TjHAcweWBE8XMrEEmYujV5cfQ1n2Xra6C9SWoxN70xTUyl_de58NUMI6LAxAwPWWXdR4hs_hISyw3TIGIYqSk5jeiYeNuTGcTyrDkqYI4EXZC0IXqZTV5CB8RijDL9oI_mgXZ1Vh3OxvMjl6VyxatyvsKL6Wo0qeWWrJeNGV-5Z5lZhYQ_P2cAJmaAO7TATWUmQlkQfYEKDdL3PT5U7U3-nbr8FbL3VV0lkPBDwD-4D4QuVgVOciJUDkVLCiJM2T0O4eMvc1DZGK345wcqu2lEZEbmnSwF9Ws2CPb4B_PQgEy2ljy9BomRx7AhHFCCyIMUXuXiZj5WCWOQCWgPD6ypUnC_de40-6TjZfSROX2XXD9HxA9TNEq5VW4H-pIPdLsRVzmlmD4LuoLNlrmoCTY_GvKIdt38OphqSgaQb6S6CWOz2eaCw_UP7nMFNWEEaagL0BJXvkJZA3wVBcjdo_7Asbv_7jJvmgV9fe3CRiDPbDZlJXSX4Q8QRCi0vaZXMlNv_H445amd8HcZhVAKrw8I-lpLZUz6z7k-klkWdoVtUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❗️
🇮🇷
باشگاه پرسپولیس دیشب طی یه حرکت سوپر و عجیب، تمامی فحاشی‌های اخیر خداداد عزیزی رو در قالب یک ویدئو تو لایو باشگاه پخش کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105970" target="_blank">📅 09:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105969">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0U8Cn28Wm4mCnYQ_JYK5_VbECtVlz0P1_qV07u9yJqrp5z650IadL5ZCZsErwRiifhcRuF34Emqf2NMD1Szqb6WmwYeLeIqaK2e8IhqzpcG_Xp2K-BJ8Seep6_XofE44QdPy4aEh8QVcgPZwyHwUaHDrQWdZZDKB9BztNN-vWUj65qv1G-3pxgZ9D4w1gV8XkmGTv1pV6xbpzi0Uwlt355tIFAQVvE5dhtO6pAyNK3rp3xuM-EELgACH9BXLcMBONCOHHvdOJsTp3dvYGcY6ccI_jA2v-4-ICRiZmxof8ZzbwZbixG13f99w3VU2QW61d4LTI73-R-duMEjtAoqWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
🇪🇸
مقایسه اسکواد دوره اول رئال‌مادرید تحت هدایت ژوزه‌مورینیو و ترکیب‌فعلی در اختیارش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/105969" target="_blank">📅 09:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105968">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار ۱ دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105968" target="_blank">📅 01:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105967">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYqYepU2n98kMU46HxqqguFnUEU0WjoV4l36dkfVzAWmUZMHUBHEl-l4edImunBZ1FjCn4bI1x_p5wRzlW8kHhKMkRaAm_YSx1CqEqVPOGZPWlt244u5m7jeKY880h8-sZpN6iUqNUWQXhpG2dwqXtAr9TBC7Flgt-zF-1JmUkuXAAxmtGbER3num0hcH8W_rwA4t63M_11QrzMQq1lJaIv1elPUbWG7XFMLs603sREcKlVpnDW3eUJ44o4kp-qwKT8UedyN-jcryud_7MChnitl-AVlCWL45q8uAcNoBpUYErF5Gd0MEuSJ5oEKXCSVMT8wZaYnGx67iCVOVyn8Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار ۱ دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105967" target="_blank">📅 01:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105966">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105966" target="_blank">📅 01:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105965">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خب دیگه بگیرید بخوابید. تا وقتی بی‌بی دست به کار نشه این موشک زدنا اسمش ترقه بازیه
🚬
🚬
🚬
🚬
🚬
🚬
🚬
🚬
🚬
🚬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105965" target="_blank">📅 01:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105964">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=UooiTrV5aHL9eskj8_v1LL--PhGlANeQErnJXQQWQ_F6K3dMQ3HEQ9VHREDdTMdADquP3F9JoDYvEYm3PZbbL2qTzFLS-MAoMeXe5nYv2o01qIXXyKF3Jt45Ew2Y_IYVebQgLjQRN4UttcsoAIWTPr1042MLVD2D7OBIkErnlQ3oiVC-bJQOsNq4rh4n8Vbwmo_o9Y6V-TtH4AlvE2ijfKL3-WjBDkDdUpda1rsOC4M3P0a_cdvrvduwEipv4v4XwbHxyfhJ4Stgl3k3p3Qjc-dGlsMd5m-grOqIFd4Ei5pGs5ccrmxzhZtlGRnBT9h2X3Fmmeg2YdGIYDRZJcCiRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=UooiTrV5aHL9eskj8_v1LL--PhGlANeQErnJXQQWQ_F6K3dMQ3HEQ9VHREDdTMdADquP3F9JoDYvEYm3PZbbL2qTzFLS-MAoMeXe5nYv2o01qIXXyKF3Jt45Ew2Y_IYVebQgLjQRN4UttcsoAIWTPr1042MLVD2D7OBIkErnlQ3oiVC-bJQOsNq4rh4n8Vbwmo_o9Y6V-TtH4AlvE2ijfKL3-WjBDkDdUpda1rsOC4M3P0a_cdvrvduwEipv4v4XwbHxyfhJ4Stgl3k3p3Qjc-dGlsMd5m-grOqIFd4Ei5pGs5ccrmxzhZtlGRnBT9h2X3Fmmeg2YdGIYDRZJcCiRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
لحظه باز شدن موشک با کلاهک خوشه ای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105964" target="_blank">📅 01:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105963">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
⭕️
⭕️
⭕️
یک منبع ایرانی نزدیک به سپاه جمهوری اسلامی: امشب از موشک‌های خیبرشکن استفاده کردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105963" target="_blank">📅 01:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105962">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4c52f8bf8.mp4?token=LBL4L1RHuwKs5SUID3p3mrqf8c-rDcMIZjuQ0mr_VNMNaitu-HP-POMDyh86vq3qAp_kIMr7ktrGuoIOzbNWozmDC1zcuZ8k9vDxvxAGyZDv6U9wbSXdeJ6afpytBhQ66v_b0H0zjPi8MB7S0SEUGYr0GrKBdexNOg_90zyvyH8ibwq58MsXskw7Y3_bGhQ0xtBrqHY5FZR7n_dp97YuAthUmHTI31kzikaaSujyYZmOEE6GfpM5b8L2YKfs4h-kmlMDNv5RdcLJWQKrGNkLAzm1krP0O9M2PjFnlK_GVeWTgNgSW3bobYEOsXqQ7S2cPb5eV6CngdeQtqrI81h3ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4c52f8bf8.mp4?token=LBL4L1RHuwKs5SUID3p3mrqf8c-rDcMIZjuQ0mr_VNMNaitu-HP-POMDyh86vq3qAp_kIMr7ktrGuoIOzbNWozmDC1zcuZ8k9vDxvxAGyZDv6U9wbSXdeJ6afpytBhQ66v_b0H0zjPi8MB7S0SEUGYr0GrKBdexNOg_90zyvyH8ibwq58MsXskw7Y3_bGhQ0xtBrqHY5FZR7n_dp97YuAthUmHTI31kzikaaSujyYZmOEE6GfpM5b8L2YKfs4h-kmlMDNv5RdcLJWQKrGNkLAzm1krP0O9M2PjFnlK_GVeWTgNgSW3bobYEOsXqQ7S2cPb5eV6CngdeQtqrI81h3ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
تصاویر منتسب به حملات دقایقی قبل سپاه به مناطقی از اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105962" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105961">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
حداقل ۲۰ موشک به سمت اردن شلیک شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105961" target="_blank">📅 01:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105960">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXB6m2hnuFmfnUatvwHm6Go15NHTbzt77qN-yB8Cwl-P9w_uKIi7nLpd4BGuqCSHHN4k4gZXCv8NOM8RytViFBnChf1u3gidDGaZZFQtXGrPqEffd04nwaEYDshHnUNrMONT2VG_5YUNiWi0W8zlxHNuz52Ar0h21nP84T8jLhjyUwUhSRRQLuPoSwY0jjIOEExWe0IeuTKMrw717Tb5wJIgJ8fkOTfs8xO5cipYkCW89-FKGzQ9zoQPVcueWE4OZPaJ-nilAtQl-XzBqOXytW_ow0WbCxnC4cqaifAH8sID808OeN-FOd3BG4c_IQTjBamOby8OwitCVUWnQz-KXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
حداقل ۲۰ موشک به سمت اردن شلیک شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105960" target="_blank">📅 01:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105959">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b19aa63524.mp4?token=sBcsgfIxDxEHhGXpaTgN3HyD09tJGWY6J5WwJ5gjJQfGB0MEwdTId83DbzZ45USsb8lR7Fd-7UzghuXox-8uPVyifk8dvwksK60tgmfJzJRIgtyVNyoPqWNWTsD5ZGgfC9OZThxrSObuek942lpuxeI0MDdIzSdROApOMMTuquAIbfIZv3OPgn1SK4IvbrqnjDL2u0mGcZwBXQ_EuNrbsYdtb5zII8rSwZPDtZ6ALlvBuzGvelo3FbP7cAktcU5cHBryB8kwzUZseok_sdn2WZelOpU6GZxO5KWopFC58NHJ4LcZJg9imMgf4St1orNgpCZ4pUQSJ7sURQ4iWEap-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b19aa63524.mp4?token=sBcsgfIxDxEHhGXpaTgN3HyD09tJGWY6J5WwJ5gjJQfGB0MEwdTId83DbzZ45USsb8lR7Fd-7UzghuXox-8uPVyifk8dvwksK60tgmfJzJRIgtyVNyoPqWNWTsD5ZGgfC9OZThxrSObuek942lpuxeI0MDdIzSdROApOMMTuquAIbfIZv3OPgn1SK4IvbrqnjDL2u0mGcZwBXQ_EuNrbsYdtb5zII8rSwZPDtZ6ALlvBuzGvelo3FbP7cAktcU5cHBryB8kwzUZseok_sdn2WZelOpU6GZxO5KWopFC58NHJ4LcZJg9imMgf4St1orNgpCZ4pUQSJ7sURQ4iWEap-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
گویا یه دونه موشک به پایگاه آمریکا تو اردن خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105959" target="_blank">📅 01:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105958">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شلیک مداوم موشک‌ از مناطق مختلف ایران به سوی کشورهای عربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105958" target="_blank">📅 01:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105957">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🏆
ژوزه مورینیو: برنده توپ‌طلا؟ بنظرم کسی که یک فصل هیچ‌جامی نگرفته هم میتونه برنده بشه. نظرم بدون شک امباپه هست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105957" target="_blank">📅 01:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105956">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d6b878d2e.mp4?token=oVgfbiWXKH_anjTsHsTURhZa1J_Qp-p0E1WMtQzkGWqxI3qoU3NLKRlBTrA5amXPMKA9CLB3825zPxcq6iUuaSJs2omTyvUuodVTfegAvRXGA94_bIGxqBUb-Py7r6lHCpgN47lXSS8ls4Oj93T7XezcuwSVGZKCLkmwOv6gdoBUYDtilcG2PbkfjHzXD1hW6jjJms8nhYbKj36Tae5wz4l6CbgbvRWni90PrZl_hoq6whHRFRV8AL__VP_SxgKz4FU8fbQ1gDItxnKrwePdOVEwEAIJpeIdS8NnFgpmIMd9L8oXDmn2vguKKFKO3drTAws6scGNO-CVIpaek39NUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d6b878d2e.mp4?token=oVgfbiWXKH_anjTsHsTURhZa1J_Qp-p0E1WMtQzkGWqxI3qoU3NLKRlBTrA5amXPMKA9CLB3825zPxcq6iUuaSJs2omTyvUuodVTfegAvRXGA94_bIGxqBUb-Py7r6lHCpgN47lXSS8ls4Oj93T7XezcuwSVGZKCLkmwOv6gdoBUYDtilcG2PbkfjHzXD1hW6jjJms8nhYbKj36Tae5wz4l6CbgbvRWni90PrZl_hoq6whHRFRV8AL__VP_SxgKz4FU8fbQ1gDItxnKrwePdOVEwEAIJpeIdS8NnFgpmIMd9L8oXDmn2vguKKFKO3drTAws6scGNO-CVIpaek39NUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شلیک مداوم موشک‌ از مناطق مختلف ایران
به سوی کشورهای عربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105956" target="_blank">📅 01:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105955">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
⭕️
لحظاتی از شلیک موشک‌های ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105955" target="_blank">📅 01:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105954">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721dcb7629.mp4?token=ZVvq_Nme4gTbdX9x4aSdcqYT97wj00Q7eqHiewOUQNKW9F60RSIF2b1OBSu1eaNEaXhzB6kpVyhdOB6x85aazoCa98e0TdGL4_O3Iz_3whCOULXc7uzeGySAe0zOyxWcn4EfBRxd4ouiNtuXAe7X5ZoCNmBJKrQ7qxRGbFgWGxKOnV0C_WqYJHy--SkQdV0JQKVCGll8SsHaJf87nbaqPxGeTJvAp3OIR8q3tkz9k5AfIwaaBdyI0Vj6MNxpGbYLL3U0MCLYkyLBXkLQtRYWqmiN7LJuNpUC1ScPz7ohuGkfU0vlatQiIB9E2q9beIOdRWMGJ7j6XPtzB1_Q3ashnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721dcb7629.mp4?token=ZVvq_Nme4gTbdX9x4aSdcqYT97wj00Q7eqHiewOUQNKW9F60RSIF2b1OBSu1eaNEaXhzB6kpVyhdOB6x85aazoCa98e0TdGL4_O3Iz_3whCOULXc7uzeGySAe0zOyxWcn4EfBRxd4ouiNtuXAe7X5ZoCNmBJKrQ7qxRGbFgWGxKOnV0C_WqYJHy--SkQdV0JQKVCGll8SsHaJf87nbaqPxGeTJvAp3OIR8q3tkz9k5AfIwaaBdyI0Vj6MNxpGbYLL3U0MCLYkyLBXkLQtRYWqmiN7LJuNpUC1ScPz7ohuGkfU0vlatQiIB9E2q9beIOdRWMGJ7j6XPtzB1_Q3ashnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
لحظاتی از شلیک موشک‌های ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105954" target="_blank">📅 00:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105953">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
📰
صداوسیما: دقایقی‌پیش ارتش آمریکا به یک شناور تجاری در نزدیکی جاسک حمله کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105953" target="_blank">📅 00:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105952">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSgICVKToHSbQrAYSPoTxBEMxh3Q5PgskxJ4LTkwdSeN3brdONqnDCH8GAcct9e0yvEuBNke355nBaynIeDKgC2OvQawg0lMowYJJ-TUZty7NN5JAEA5BogSwIH5_HHozYWYLGD13bRRbj2k9DG1DDi-_FThEDrVJktqbDBi28HB4qWTt9Xlag-1gN2aHHKp319yP-IfR9dGlLQf7yuEVw3fqNwKqYbZhQi5opAEz1Wh9KeYiYgyGrrVRxxw_U0HbS-kDEPSe0fGejabrO3fOXdEZS4lfBIKrUWn3p28VGJNoqDCIksHmLNAgXNos5nJNFaKyWe5f5jjbgdhgpe4jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
موشک‌های سپاه به سوی بحرین و کویت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105952" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105951">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pO9t9jPtBQlhpK6breBoWc9U_l3R0WMVqgV4cRpTUJTPywZ0lRwO1FHzomJCMVR0D1zKtLW3drS6c-gm6eo20w_CoxIsocoGagC7Z0qBd5cfYBEQ7C4Q4ZGMizD0NDBu2tS4DH_OYwbpywepTijIto0rcIzELHihSY0-sAvlWvYlSDEXngVyHDlkDIbUeTmcgXcHcL1r31Sm5t6YaYpqUPX9qhJv_uFXy9_thAjqD54qkBnZoNtWZ6Wy357biyybeoW4MfZqeoI86dqrY2g0E3XSlJheny2yLakv0E6ZACEwQsOLblyeInup1VenRvfWzO23ljwZIWEE2k4hg5N2Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گزارش‌ها از شلیک موشک از مناطق مرکزی ایران به سوی اهدافی در خلیج‌فارس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105951" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105950">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گزارش‌ها از شلیک موشک از مناطق مرکزی ایران به سوی اهدافی در خلیج‌فارس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105950" target="_blank">📅 00:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105949">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pfhv1Py-LNEAq2rh7EqGM_2YDoZhmM6IszXu1y8JrDx4xk1gSwS2tKtBvSxG_7ULYownNq5BPxfHW4K-qLodZt5-66vyStWg6hjTOgHAKDrDKTwzXqwWblenJqi4ais1mCGE8bKIEe-tHJlwodjCzAzhsockYry1saK28Y2_FtfB9r5vS8Wls7iBkGZ9eoTwXbfc_J2WEhQYUPn5KtT6-ZS-QRSXWvLrNCHkg9oeoaAm1Mm2FliU251ek_Rv7SOygjOUy4P33cy7ssDIb7C7xcjrMSDES_E3ltnFPg7wzLawCJDiv1AI1kBBhSqmH2iHrpFyuBT7BaEe_Rv3-XZXmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⏸
🇮🇹
🇪🇸
هایلایت بازی جذاب و تماشایی رئال مادرید مقابل اینتر با گزارش ابوالفضل عامری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105949" target="_blank">📅 00:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105948">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXHlPHGcGY5XMm8GK0f8i38tJCZbmJlcSZ0hULWTNhjAhVzd0febTNvVTX9VXvOnntHt-11ODDdvCsXvurOrdnhzW8yxN4wxmwXld5gqd1niEy5IZWOULXCPbGpdANjjOoZ1MdkAAjmCTBDBGWrz3UmMiyYi0WTNkyt_o-x8YMvNf6xAQXtPb13qDtDhxHTR0fULXzgXKHUwArh_FgLPtSeZ7kIzvIaF-hqpvIG--tU8w6ou7d4WSyCTdl4SoKBNXtCMsqvPso3iXl3b9GJ3gkWDLSEtomVdDYVMlEQhpYDMMaarv4lcnLLDM8lijt1Gm8jdXt-1U3SzzreQEMLFSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
🇪🇺
📊
ارلینگ‌هالند در لیگ‌قهرمانان اروپا:
‏59 بازی
؛
‏59 گل.
👀
🐐
اسطوره، لیونل مسی، برای رسیدن به 60 گل در لیگ قهرمانان اروپا به 80 مسابقه نیاز داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105948" target="_blank">📅 00:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105947">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
⏸
🇮🇹
🇪🇸
هایلایت بازی جذاب و تماشایی رئال مادرید مقابل اینتر با گزارش ابوالفضل عامری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105947" target="_blank">📅 00:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105946">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYgq7fQkwEpKIPxuzaSrhxnlFGcBeE3ig3tebW2OwB9xFE0S4mnRAXv9sIh50taH_Wud3Y9JLphI5kVdclqHx9Q0hA2qujWlo2Nif0r7nMb5pY__SC2CV8sTiWhIdiH0hSyHwscvV-IIrEEvXoZlk9TFWWJ9ZxyUQFM28VMUoB0MvkMJDflc5mGwlNlDd5aUYOo90Va0Wr01XkpxnzY_VHY40ARq_JLLZJulRyhV5ubc8Ur0iuVpEpXgeEGXS9FMVDd4Tz5qlVf90ewoUlStWoBDXsSrxXvqKvqOPIbQ-tI_FhNj1dIHgX1_c9xJLTVVeqK9b2plRKhFwuikzwFK4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇮🇹
🇪🇸
والورده بهترین بازیکن دیدار اینتر و رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105946" target="_blank">📅 00:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105945">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eq_ZbT8hbQLqt9zYDXaCIPAtNRTR0PdSvxDcSwvWl7UBKX-hdhdQyuXZUGPWCRHQ0OCBwDuHts2_riVp2dhKIU0-TmiPW-0gYYsPiMFlRylA0VnqRLW9e3SZ1yAC60DX1Kqjg53R3GfdmS0rfu15FEjC0tG_8T8wpIIwvQbtfDS-yR1BS5_39TIapy1uTca8_4D3uC62zXRf0bQXO6mSCGesBXdqbJf_UDoMdyceN4tGkp1vnvffBHjKZRojgh4XX3joM6hehk-_Wj-JXkkxU5gaAgxWLEiC3pqdDR2RadI6G3YYJ1Bmrrg_GS-_1RY4eig0NKQ_x1ktGSLyNxss1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇺
نتایج بازی‌های شب‌اول لیگ‌قهرمانان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105945" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105944">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/275f4f92c8.mp4?token=ZuFLBSsqbRV-vO9hHGw-9eCxFzsko7lBD6_Yu8gs0f9HPtHBMwy9yG4BsHLiGPkAlT34jMBJV4wudddZUx4XouyoTcrKyLBm0oqimuPj1afVJU_ruxEyPuJNvdDtb8_5m3yBHsTF4Wb8X_x6At6qsqJXQBWh1JNmOMplVzOoGDaFyXgColU5Nbh9yEWz4lfTekT4wDqnJSJ5ruW2lPD0zex4zUPGn9UhtyHcB-puZJ0gQJpA-KU7NufUaLs7EJrYmZDnejgz773RZNtRTztzIQLZxb733b1gB9cfhaNEPzH_7GcJuoW349ihrmxBCTsJSlFn6DcAzH-nHaf4FpjIng" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/275f4f92c8.mp4?token=ZuFLBSsqbRV-vO9hHGw-9eCxFzsko7lBD6_Yu8gs0f9HPtHBMwy9yG4BsHLiGPkAlT34jMBJV4wudddZUx4XouyoTcrKyLBm0oqimuPj1afVJU_ruxEyPuJNvdDtb8_5m3yBHsTF4Wb8X_x6At6qsqJXQBWh1JNmOMplVzOoGDaFyXgColU5Nbh9yEWz4lfTekT4wDqnJSJ5ruW2lPD0zex4zUPGn9UhtyHcB-puZJ0gQJpA-KU7NufUaLs7EJrYmZDnejgz773RZNtRTztzIQLZxb733b1gB9cfhaNEPzH_7GcJuoW349ihrmxBCTsJSlFn6DcAzH-nHaf4FpjIng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم منچسترسیتی به پورتو توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105944" target="_blank">📅 00:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105943">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRbocyXztnzullTYz_sakELivuTO-N2pI1hfUCng6wzPlqbvu9UXu9YsTSYHhlXIINHEKsELgpaiaW7bS-QFEfN3Q9Sn8U4SELpl9Tftxf-r7TZ-MrjMCplF7F87nHdTeuK69mUIRGDQimJwO5Q8vEXv3EQMzbRo8aRg6gVzhmKfoMm_9uxtdEhIauOspdWzVng9VST-HuVxmsTbx0ExE8B5C6rkEMkn5dClM-ZtRcKaFNj0b2Aqf3clVA1napNibm8KHgo0PFLIUhNT_Lar1a909l1Z8VWh51tS0u9wTAXu2gt6758cw-EAGPJU68vb3qSIQs48ZPUNQ3LsErWPuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
هفته‌اول UCL؛ برتری سخت و نفس‌گیر کهکشانی‌ها در خانه؛ درخشش دروازه‌بانان و فرصت‌سوزی مهاجمان باعث رد و بدل شدن گل‌های کمتر شد!
🇮🇹
اینتر
😃
-
😀
رئال‌مادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105943" target="_blank">📅 00:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105942">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c99ae7fc.mp4?token=a-G7svvHvwa1H9GbyiFMFGyEIHPh12hWdn1GPP8nyyo-Rbwg2ZfMTYSL6kxTJSxYK9yJXlZUyDLzR5KL07mRXkk7KlGW5QtUVmjFsXlh81L4_iiMR_H9R-UjwBQTtuEJFejyla0_UANPsuPkBXVi3fWKZEOUjUWdnmqDujsHAi2l0dpivDM0U8Ml1Nza6UL5drqXfoSvxZY-SU4Jm7y3_O9I1b_3-a5KGRgWP4WUJWciEX3LQd5UOQjJRVk76Z3w3853VRrcEHtR63Lmz5QfJFaErXCz3sRrpgDfceC5E1t1V2E1167mo3HpFrgIgXHDVhTkjGoaLOnhZfcDGGVxvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c99ae7fc.mp4?token=a-G7svvHvwa1H9GbyiFMFGyEIHPh12hWdn1GPP8nyyo-Rbwg2ZfMTYSL6kxTJSxYK9yJXlZUyDLzR5KL07mRXkk7KlGW5QtUVmjFsXlh81L4_iiMR_H9R-UjwBQTtuEJFejyla0_UANPsuPkBXVi3fWKZEOUjUWdnmqDujsHAi2l0dpivDM0U8Ml1Nza6UL5drqXfoSvxZY-SU4Jm7y3_O9I1b_3-a5KGRgWP4WUJWciEX3LQd5UOQjJRVk76Z3w3853VRrcEHtR63Lmz5QfJFaErXCz3sRrpgDfceC5E1t1V2E1167mo3HpFrgIgXHDVhTkjGoaLOnhZfcDGGVxvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
گل اول اینتر به رئال مادرید توسط آگوستو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105942" target="_blank">📅 00:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105941">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رئال کیری بازی در بیاره مساویو میخوره</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105941" target="_blank">📅 00:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105940">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">لائوتاروووووووو</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105940" target="_blank">📅 00:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105939">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">لائوتاروووووووو</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105939" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105938">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اینتر یکی زددددددددددددددد</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105938" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105937">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گلگلگلگلگلللگگلاگا</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105937" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105936">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
سپاه پاسداران: تا لحظاتی دیگر تمامی بنادر بحرین و کویت هدف حملات قرار می‌گیرد. منتظر باشید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105936" target="_blank">📅 00:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105935">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">رئال بازم نزدددددددد</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105935" target="_blank">📅 23:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105934">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105934" target="_blank">📅 23:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105933">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گلر اینتر با اینکه کیری بازی در آورد ولی حداقل ۵ تا گل خریده برا تیمش</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105933" target="_blank">📅 23:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105932">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">امباپه بازم نزدددددد</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105932" target="_blank">📅 23:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105931">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کورتوا نبود الان بازی چهارتا گل بیشتر داشت</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105931" target="_blank">📅 23:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105930">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lP2s3_CEuLb7qcSSeWczJwjjeSfjwdeK3ymZfLjdH2ewLFS3oWSgjhAHH3dY0tkkeC7kO08p5Ax1DNpkf2RcEYgH5vwqczka1uSCUlgNzoorBTF522A-o3uk9eNiZGiGJZhKvCXHJZF7V-Sl4Z-KsY0mkDN95w7thFb5QKvjSOwT3ZgGx7JN1an_LxzyE-c3kzCgc0SbrezzgK0HN-t6CNBArNfe-kKh9lhzFiLiXXCYRS1l8SbQlK1Ho44Op6I0vLhT0ZJxx8BvQIEpzyJNMFWwMQa9AsOqxS46q-J2Nz2eZfCFndzZXqhZFp-AOOTWGZknJ1Hq6lNGyp_vIbOnzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلینگهام جقییییی
😐
😐</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105930" target="_blank">📅 23:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105929">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بلینگهام جقییییی
😐
😐</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105929" target="_blank">📅 23:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105928">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">چه دروازه خالی نزدددددد
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105928" target="_blank">📅 23:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105927">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105927" target="_blank">📅 23:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105926">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105926" target="_blank">📅 23:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105925">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGYlS9vtvWxziz-ffFLUCra9pYCNlYiiuYhaeROg7sFiiwWhI_CWVd8o0Xp5YG2ze0l3BvMYZHCp0gNtUHIcrD3gSDUErz6GCO2PctPnT-FylIEwwyXGDKq5vXWzdQGn8GMjkNOUO1m7wRXMIVSmNzyuLDtoQQfxKXimZrnPwKHt5z676eqjLWsJlipn0MaZKU2M-DYxxekkiA6wBuamJi73WM35eV6VL9APr1bk4RQJsu64OeDZytjSZF0iDPOetL5tJSIcTeMz1PiLHRx20zNongkDFjTXMVF2VPDUyb-vZELA_cq6LzKCrERAEKpDZlnKSU-z943j4jjcWv4teg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔥
وضعیت نتایج تا دقیقه ۵۷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105925" target="_blank">📅 23:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105924">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کورتوا خداااااسسسستتتتتت</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105924" target="_blank">📅 23:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105923">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/baae1563dc.mp4?token=onghrHN-xUDSU8MkZu-cTQebodVOGj_gMI4nmlbRkgGHhAeImlOyt03KyIWpVeBSmiWkv_h4jJOyyYGKBWdxUr8KTtrhlI_rGd11m4y5qR5XMZKti_YuRUQ0G3EfKMytwjcCCqmAHrZqJ01_2OjWt-XwvuUQ6MNkKDYYhJdLgCMEoyQoQv75RmOVvKpsmNLt4TKEtLOeLYOuV_P5kUArzjMvWxyQ3Ii1aRrIVdInbHw7Kpx3HZoppnfrwpxtIzcVWtO0SFZc9aaHSHYbMs3Ixw6mbdXRsKMmlzyy8GajYVdBlN4hDpqlwkJyuZmA9wkBolz8NLRg8kD-3-4N1b4q-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/baae1563dc.mp4?token=onghrHN-xUDSU8MkZu-cTQebodVOGj_gMI4nmlbRkgGHhAeImlOyt03KyIWpVeBSmiWkv_h4jJOyyYGKBWdxUr8KTtrhlI_rGd11m4y5qR5XMZKti_YuRUQ0G3EfKMytwjcCCqmAHrZqJ01_2OjWt-XwvuUQ6MNkKDYYhJdLgCMEoyQoQv75RmOVvKpsmNLt4TKEtLOeLYOuV_P5kUArzjMvWxyQ3Ii1aRrIVdInbHw7Kpx3HZoppnfrwpxtIzcVWtO0SFZc9aaHSHYbMs3Ixw6mbdXRsKMmlzyy8GajYVdBlN4hDpqlwkJyuZmA9wkBolz8NLRg8kD-3-4N1b4q-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول منچسترسیتی به پورتو توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105923" target="_blank">📅 23:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105922">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">امباپه چه تک به تکی ریددددددددد</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105922" target="_blank">📅 23:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105921">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105921" target="_blank">📅 23:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105920">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گلگلگلگلگلگگلگل برای سیتی توسط هالنددددد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105920" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105919">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
📰
فاکس نیوز: امشب برای سربازان امریکا دعا کنید  نیروهای آمریکایی به طور فعال در حال حمله به نفتکش‌های ایرانی در اطراف جزیره خارک هستند، به نقل از فاکس نیوز  ایران گفته است که در مقابل به پایگاه‌های آمریکایی حمله خواهد کرد، اما بدیهی است که ایران *خیلی…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105919" target="_blank">📅 23:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105918">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
📰
فاکس نیوز:
امشب
برای سربازان امریکا دعا کنید
نیروهای آمریکایی به طور فعال در حال حمله به نفتکش‌های ایرانی در اطراف جزیره خارک هستند، به نقل از فاکس نیوز
ایران گفته است که در مقابل به پایگاه‌های آمریکایی حمله خواهد کرد، اما بدیهی است که ایران *خیلی حرف‌ها* می‌زند
امشب برای نیروهای آمریکایی در منطقه دعا کنید
و برای خانواده‌هایشان که بدون شک نگران پسران، دختران، شوهران و همسرانشان خواهند بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105918" target="_blank">📅 23:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105917">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIyUflIQrkp65uZ9TKZqdVDq9YXHulXeI4V81qYnwyP7AU4Ul48QQUXUzrgYmwGgFEVMbFXwTROMzYeCrGy0Y4ckaDUpbqThBBwHDF9rvBInb5nCaLVIyZAQ49wLcQfC2FTSwypzi63RXpqbpZgrUQP5ia3Nnn_wXbAmdkxD7oL1ElUXRbMAND92G0j2svL_QFvGFOWz69qdI4UNOSS60yEBgefaMPcAHUu-9nd3NnVW-nMoGtNCgsZSWKa2Z70GS1vM-A_HIipb8mcOTN9ukUYqgE1PXv693EcQTEdBnWKQ15guTXtk1zZ4l2fYyVnqintMqIGdu6ltuE1Rue1iiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت آخری که رئال‌مادرید گل نزد
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105917" target="_blank">📅 23:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105916">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کورتوا مصدوم شده</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105916" target="_blank">📅 23:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105915">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کورتوا مصدوم شده</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105915" target="_blank">📅 23:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105914">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گلگلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105914" target="_blank">📅 23:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105913">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گلگلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105913" target="_blank">📅 23:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105912">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23f212f578.mp4?token=KbpHJFuIsE9TycTV8SqnsuW7WQ7O1mUZknTLA4NZhMCV4rkDwFUNo9JS14sTDd8E4OPCLenuqhlOJ1178o3FZSfyPj7sOPUYzqWmt-rxbwoNwu9tV6MlgZJwuS3_AnjfsidJznqmf-n3p_ZTb97w48a8qfCyX_r7q0vAFsAXWOF6r1IN-_M3AGZIglBtXjqeg9yFv1oRQZHkDSqqowYnCuGPGd2esJwmg4tbIIJu_ufsnYfwA0XQkx8pH5OfKBuVzUXUK1GfPL3ZBP4xSqsF6Jewu7WfsI3bQmT-QBVMCQQBs0pjW41YN7OiQNvqRYNO5ixb4YSoUHpYyq1G2fyD1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23f212f578.mp4?token=KbpHJFuIsE9TycTV8SqnsuW7WQ7O1mUZknTLA4NZhMCV4rkDwFUNo9JS14sTDd8E4OPCLenuqhlOJ1178o3FZSfyPj7sOPUYzqWmt-rxbwoNwu9tV6MlgZJwuS3_AnjfsidJznqmf-n3p_ZTb97w48a8qfCyX_r7q0vAFsAXWOF6r1IN-_M3AGZIglBtXjqeg9yFv1oRQZHkDSqqowYnCuGPGd2esJwmg4tbIIJu_ufsnYfwA0XQkx8pH5OfKBuVzUXUK1GfPL3ZBP4xSqsF6Jewu7WfsI3bQmT-QBVMCQQBs0pjW41YN7OiQNvqRYNO5ixb4YSoUHpYyq1G2fyD1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
اشتباه فوق‌العاده کیری گلر اینتر در صحنه گل دوم رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105912" target="_blank">📅 22:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105911">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">انتقام بارسا رو قراره مورینیو از اینتر بگیره
😆
😆
😆
😆
😆
😆
😆
😆
😆
😆
😆</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105911" target="_blank">📅 22:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105910">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اشتباه فوق‌العاده کیری گلر اینتر
😂
😂
😂
😂
🤣</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105910" target="_blank">📅 22:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105909">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رئال‌مادرید دومییییییییییی</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105909" target="_blank">📅 22:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105908">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گلگلگلگلگلگلگلگلگلگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105908" target="_blank">📅 22:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105907">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/25403f5ba8.mp4?token=GWBfRvNDaL47Fpg7qr2ibicRmWKr4-BlzZ4l3zkt2klCX3F7tfRFQqhNLU2SgTMnDbXA3i6ee4KklzH-Bib_iW_TRv-kDne7cPS_V19H20_HJjC4uvpPzoq2URUtUK4c6lJNUN2muRzc0JyZzyjpk5CP_Z4KZMDLDiE-6H1sZQL4wnKz-L8gLsyssBT5IweXPYU_PCd4vTnKe5KHB3wUiqwHUa03DLPS9zAq7-7Ntuj03nOxQssokCJMgnHvRLs4vOXNn-UGJtPhBpPFF4cBDxwBA4FvG-xgls4Ig1XDu3tVgJMgs2kQgxJzNXDSAJUYP2r8j9T3rJuYaP3mNAoEYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/25403f5ba8.mp4?token=GWBfRvNDaL47Fpg7qr2ibicRmWKr4-BlzZ4l3zkt2klCX3F7tfRFQqhNLU2SgTMnDbXA3i6ee4KklzH-Bib_iW_TRv-kDne7cPS_V19H20_HJjC4uvpPzoq2URUtUK4c6lJNUN2muRzc0JyZzyjpk5CP_Z4KZMDLDiE-6H1sZQL4wnKz-L8gLsyssBT5IweXPYU_PCd4vTnKe5KHB3wUiqwHUa03DLPS9zAq7-7Ntuj03nOxQssokCJMgnHvRLs4vOXNn-UGJtPhBpPFF4cBDxwBA4FvG-xgls4Ig1XDu3tVgJMgs2kQgxJzNXDSAJUYP2r8j9T3rJuYaP3mNAoEYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
گل‌اول رئال‌مادرید به اینتر توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105907" target="_blank">📅 22:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105906">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">امباپههههههه زدددددددد</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105906" target="_blank">📅 22:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105905">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105905" target="_blank">📅 22:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105904">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYewiCHHDAWZeyE4ZmjOXXrHM-_5uzk5Ka90S9lu2pYfsmRIDUlSCF7pEtJnSmAQQTdupWlCgqYWhtSBdlzrVUHGfv5bqR_SVF70lRHp_39wG26NEE6EWoFcMV9ZTKMH6F7m4FO6Tj9bfYJG1AqHBhx60rgfjjYtbsH2EfN3EzlZKcRN2SPix4p_0ALOEV671fVSUnYsnWEMDAIWedmdRykSobMdpeFhv1LykIlBTeAo5tnBOQdY2vr23ee6ix6ALuwAJmc-GHlBp-sIaBX8Lcjy7l0kkWYopYd66_XNBIbQT6m7-_XO2DiVfvjMIJqVZfww66ScMuLkonI5j1VtCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نتیجه اخلاقی از فوتبال ایران:
فحاشی ناموسی در رکیک ترین حالت ممکن ۴ ماه محرومیت داره.
جمله "شاشیدم تو این فوتبالتون" ۶ جلسه محرومیت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105904" target="_blank">📅 22:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105903">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f233f0dc0e.mp4?token=Q_VEloRc4zExFEB68Nfph7ZwTxMzFBZLZiszZK2AUVx85rEWPJ1JI19H5GqG0UNA-C5Scc7y_jAIqntc-QbRSlRLIyS3C8UWJAVd9Y2VLnF8RtH-VLbDo5-HV57X9I-e4ZnC-KynqMq4lOE3hIHY7jkaSfKJjiBu7abSo7XgQrQjDi7uvgr3nen07leVVu47r74e-AP3wLzHowtXtke87G4sq_FRcuwFD_W_tyVa5Im__5oAZg2eYNJvIaO0FBn68EiAurwqEfdxKsgZ-_9-J6n-mh5PnhqBA-5RL2aYUfh4xObqylwgQeoQQOKrsGzJCtP2OeAR9qC-pxOMXq5nhrARhxl1zsivQIvIM55q3uFAtr7lsEh7uecyv_luWNTxzgstLHWpjbs_nR_XWz5WsYPc1w-ysEyIsZpzheIwq9Ci9NzbA1ZAvBnb-XbHcibmdWtiEMJYDEJY6QN4LYHppRqSq1lGGFEaPqfZuRAjuP-YKiZWmmcJOY_SmqettsN56wnXgrYKGCg8TmU6BJUHTjo7xU8a0VZNpqXSp9h8xPEP4YnOFyNQEwObuABgFTCESIz78Ed694PTndn-ImRm7HvvSLQoanTi7O4ONCogZftxyj1SVkPI1KY3OuNbhORIN_2XsPEQJ3nQuXcPsd4JOw-_U3Sb8P6L1EkcYiqU628" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f233f0dc0e.mp4?token=Q_VEloRc4zExFEB68Nfph7ZwTxMzFBZLZiszZK2AUVx85rEWPJ1JI19H5GqG0UNA-C5Scc7y_jAIqntc-QbRSlRLIyS3C8UWJAVd9Y2VLnF8RtH-VLbDo5-HV57X9I-e4ZnC-KynqMq4lOE3hIHY7jkaSfKJjiBu7abSo7XgQrQjDi7uvgr3nen07leVVu47r74e-AP3wLzHowtXtke87G4sq_FRcuwFD_W_tyVa5Im__5oAZg2eYNJvIaO0FBn68EiAurwqEfdxKsgZ-_9-J6n-mh5PnhqBA-5RL2aYUfh4xObqylwgQeoQQOKrsGzJCtP2OeAR9qC-pxOMXq5nhrARhxl1zsivQIvIM55q3uFAtr7lsEh7uecyv_luWNTxzgstLHWpjbs_nR_XWz5WsYPc1w-ysEyIsZpzheIwq9Ci9NzbA1ZAvBnb-XbHcibmdWtiEMJYDEJY6QN4LYHppRqSq1lGGFEaPqfZuRAjuP-YKiZWmmcJOY_SmqettsN56wnXgrYKGCg8TmU6BJUHTjo7xU8a0VZNpqXSp9h8xPEP4YnOFyNQEwObuABgFTCESIz78Ed694PTndn-ImRm7HvvSLQoanTi7O4ONCogZftxyj1SVkPI1KY3OuNbhORIN_2XsPEQJ3nQuXcPsd4JOw-_U3Sb8P6L1EkcYiqU628" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال رئالیا از اتوبوس تیمشون
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105903" target="_blank">📅 21:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105902">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUVpAZ5OjoAI6TvMLJRpnf2WzpulPHM9Bo7jsclF6g5dIuwmbaJwpaeAWCxdEj9OSX6dIh2tWBqrCb905DiorsBGRzwwZ6LCIvOc7OzCLHaaTZKDnSDzhMNeKO8WIfAMeUuFSfjWF0sHdluezHN4zIcAjqQs7F5eb_dbjCbD6Xof4IEotDsToDUaFcrr3tPlIVldabPgrTTnP05FdRQf0sPy-JuEoVzkfzsO5TkT5o20EpTNcoqC7eXkNlcwACXFMVYzFjWBFUoOMPRYZKeXcQ-C3GqTNWJbukKPfJxofn-eCVVHRCUZo6WQTyNp7iwnZ0YGaa6gd40E0ZdY0KlqAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
👀
🇪🇺
اگر کیلیان امباپه در بازی مقابل اینتر گلزنی کند، به عنوان پنجمین گلزن برتر تاریخ لیگ قهرمانان اروپا، هم‌تراز با رائول گونزالس، با [71] گل شناخته خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105902" target="_blank">📅 21:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105901">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
‼️
🇮🇷
تاجرنیا: از سازمان لیگ تقاضا دارم قهرمان فصل قبل لیگ برتر را اعلام کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105901" target="_blank">📅 21:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105900">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38f65ddf7.mp4?token=cFB_FtI80gMmcYDcRXauZeDxcmcb04z0glyK5_kZISUfrxAPGjBVVkUUxDHmb71ISgjCzqV8l1rz99nJM4ncFUEGeIbtlHEb-03XwmA6-6O0EsuNsHkrxRPAQQ0i2CaQsISxGF_HRODTHvTLo8EjvjXNHn_pEffrrS51j1AtphwDAuQMYmn_w0exvF35PjUYNTBafUDO3d8SeUqGj2NGzNvHIH3T6GF3yOauydBeXlXaj22YXZvV_TYIF5UAejZ-ZrX8rpv4Zo_BZLkIlDtQKlPjks4SvXa3v05O5JXfKFfoad0z_SgdDw-2eHeoSeMtOOiunoTyhxvCGW5DUxxbLH0AQ1DP0JRhOk-9HGtlJVvwFRiolViEk4QJX2bYo_Q3BRaTzBgB9eoGVq2vnNzAOxDbqCiPtU9nsjK2X2aoYIMXLJ3fhThYJwgS6t8wVgfKt6tl6ARhEPAC5E806UjpEnmSJEjutPK8NrhpyF_IV7yyDjyXoXBRJ5czqNOHCI83dYL-dIMKp7aGPFAtR2B7MumCy18vsLLVgbwYFe1kFnV7bK0ixiu2Rgz98eiBxzYaUwGV-zaSk4HXKdx4v_J7uOXzwhKzDE8F-TGCTm-l0TZ9CIV5hbZ_7XyS8n6G91vdKf0k6okq4jJbhSWQ0xr547Bto80musbXPllRZKM3Cgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38f65ddf7.mp4?token=cFB_FtI80gMmcYDcRXauZeDxcmcb04z0glyK5_kZISUfrxAPGjBVVkUUxDHmb71ISgjCzqV8l1rz99nJM4ncFUEGeIbtlHEb-03XwmA6-6O0EsuNsHkrxRPAQQ0i2CaQsISxGF_HRODTHvTLo8EjvjXNHn_pEffrrS51j1AtphwDAuQMYmn_w0exvF35PjUYNTBafUDO3d8SeUqGj2NGzNvHIH3T6GF3yOauydBeXlXaj22YXZvV_TYIF5UAejZ-ZrX8rpv4Zo_BZLkIlDtQKlPjks4SvXa3v05O5JXfKFfoad0z_SgdDw-2eHeoSeMtOOiunoTyhxvCGW5DUxxbLH0AQ1DP0JRhOk-9HGtlJVvwFRiolViEk4QJX2bYo_Q3BRaTzBgB9eoGVq2vnNzAOxDbqCiPtU9nsjK2X2aoYIMXLJ3fhThYJwgS6t8wVgfKt6tl6ARhEPAC5E806UjpEnmSJEjutPK8NrhpyF_IV7yyDjyXoXBRJ5czqNOHCI83dYL-dIMKp7aGPFAtR2B7MumCy18vsLLVgbwYFe1kFnV7bK0ixiu2Rgz98eiBxzYaUwGV-zaSk4HXKdx4v_J7uOXzwhKzDE8F-TGCTm-l0TZ9CIV5hbZ_7XyS8n6G91vdKf0k6okq4jJbhSWQ0xr547Bto80musbXPllRZKM3Cgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
تاجرنیا: خلیفه و گودرزی از نیم فصل بازیکن استقلال هستند. بحث انتقال خلیفه و گودرزی از آلومینیوم با مدیریت باشگاه آلومینیوم توافق شده است. این دو بازیکن از نیم فصل بازیکن استقلال هستند و حتی واریزی هم انجام شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105900" target="_blank">📅 21:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105899">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7YryO1oUQ63K2bYnsJNTAHNq0I4GRvP1JQn4ObLH7SiTcWF5d5xgrawiJp0feZ9HoLYBE-9ouLsSA0gdaq80hmy20d4R2yQVkr9aY7zpa8u8qKcrniZrZWIr8XA0JWaxw9eJ6NQJ8eCLXEVfP7G_gYg0BLFjLKtvzL4tMw0dgh1XyjbYZe5X9uzC7UN78semPGJ7CsfGhYmV1XIEWdaoD2-csdTp9F5f0N6kwOoOkTm_FSXzxSvTMn4elFMniI4hod5fZEFHWPI14oPGYcBywnmtqVjucsRTAJvy67EQoYPR4fA8FT79WzLHVevFmOdIkRYmrQ99hdVnyuQfzsiPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇵🇹
ترکیب منچسترسیتی و پورتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/105899" target="_blank">📅 21:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105898">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMGXvWVS9D6CzaYRuEIqfq-ASmRnIZ4TEffFySbB-FqtxzrjhBaA899Z2ZqqHHj1sUbivmUwWFxrT_UNV5cZbzXrHuAK4qImQrLMlGCROIMY9EmU6MlZetLzlt8OQLnsMhyESBIeHtx2K1ZA4SC8SkMvGRfWy0A3QD3X5vpqhOlbJQLr0hn5-nHQTXg0Vr07nsdiSA5JfZsHpv-ZGFR-b9JBjcMLKQusTY-uHzfnEYkh98kc0pm0dKJ89AVPER5ffw4iXxoEqmWLXKVt-xE6Iz1PRcYfTmud6lw8aQnYb8buMR6gTOeRqVkfPA-AgnwWE-eomNa48nXOW7iI0rEhdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🇪🇸
ترکیب رئال‌مادرید مقابل اینتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/105898" target="_blank">📅 21:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105897">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trY4hmDxFOStLy_So3LlcTC82CROHWe-AMHsaEww2tu8PI0V25Iux5PwXTPUL9Ao_OK4_hXr_JZXO_RoAyaxAx7KXT1Ga0Ifv3rh4CEs5UN7KNZJEHF-FPuuzftqwi7yXsYkGzo1xGotrrA0PKdfArZ7BcyUec7kJ_aR1Lu4Z8vrWpUPU1Yeevoc7uxbj6cXk8aS79YTSVzolgYoW5X9aCBKVKmwgLOv6myFpneJk3sX5irEK8vjzUsnELFszH2WHZualeVi1uDJqyuUEpwmKwCo4x2rESVc3SRUE3cvxlm2W1g6_-JikrIWg1HLxo7ByOFbMBAEP5JhpkGFnzHkLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🇪🇸
ترکیب رئال‌مادرید مقابل اینتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/105897" target="_blank">📅 21:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105896">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWENlNn3Ss7bF3RCmZ5zlaombGossv1Lc7QbykC7UsV89zEovBF01nrFwLLVWh-zVMPzjK4bFiyCo_8a1Hm-1l5vo-w2QfaNgBSBpgh0bSY1dSrP90d8LNg7t9LIs9ntU2H-lUmedZX-Jukt03_CJ7m8d-cYBJE2UKKmG8zK_RbK_5SIWhfWRgjRGCDuN4Svcd1i8JfVCHcLlDM6FRUNNKdZYckklYUPxbz-O1OPN9UlIpw6qZE5v6skGTcOn4yQKtFz-oet7bvzxfV0LbgVM2ck2P7TImfujfTL74s2labP4nkbZjo3OVqkOU0tV4nI3X_o09j25Oj_rrurvqUhXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🇪🇸
ترکیب رئال‌مادرید مقابل اینتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105896" target="_blank">📅 21:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105895">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRNsqT_Ai0qedB5_Bs3CejgP1Mxr77EIQrl5O1sLrIyFIhAJ2NG2ya9-IOEaQyODj9kCtc_qP35E3qwMpxWYxYZwR0ApRo-ySzm3tDUcUN2U2E-apEdwXNeqzJyuz-cpdEnSWMsQdfxkgVExJaLwcxIbukg_1PPMIwBvlRp8sb_s6cgahZsZsx778DdtOsRQfj4db6DOJpgjtX8n0e3DDYP4d6Et8LpHjLat3EXV8_v5DbQjF-giMUf_eBxcz8k3BjpkqpIaQPjfThwj5ggiTj8CZ8Klg0UXH_n0HJtxIX1CWlnJfT18KvKEaNRUl7_CQOpG6c4BpFuz-lzChdF2tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😢
رئال سقف برنابئو رو برای خیس کردن اینتر بسته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/105895" target="_blank">📅 21:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105894">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntXQIr9nEpJjccAfUFtbrclwn5MxyvlM2G2umiQILheM5uBo726h4kIeB91UCPvJ3I4GG76Lixi_JxCLqSJp2ZAvBwFRVMRSu3QLGHCzFT-LvhCWao4-4KujL8NUn9qSivX8_OKO-OVwqI9kc4YdHQADyDj_Sbg4pqZHmyYtUice-MMvKTFgiVNeixanykRXMcTQgkF4lwfacxYNhtc7rpjFR20S6vEs0Ands9sU4uoq3FDp39XxtCE0zEMp-aG2sTxiI-Dh20C4azw05Zrreql-L1oEMm4G4-A8EDkb6HxOjh4BOp_MWARS6vgAVWIKQgH28WuY7de1CZAO-Zd-gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🇪🇺
دیگو سیمئونه: خولیان آلوارز جایی در ترکیب فرداشب تیمم مقابل لیورپول نداره و باید از روی نیمکت بازی رو ببینه تا شرایط روحی و روانی درستی دست پیدا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105894" target="_blank">📅 21:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105893">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ecv8HX-izr_Xi5x9QqYtHokzBMcC3drzCeAG7y3EfwFNczyXj9mwiyzzgF3kZiy1o1mxg8dh7cFkkeARuR9_FaswacTtm66Z55Ildcxzspsl_2pLWj8ALzYDhPmFEDkO-Ek-MkqYEfCe8RJQI0fV1PFihE7MT7NRtcDloue7GQQD47ncUT4-2kA_U1eSpwYV0PPVzmvSowcDyWrC7Ze70RTGvR5f4WhQWsU9e3W2pmbuepdGnUxAOfdcT-jNsSAJPj_D22ufxb33_SdlZ12bVHEqSepkaAIx1VbBlvuX7pbaKjHWq2n6AoKoPJHfi29t07E5zV27F06SXVRpXFXB-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار سال ۲۰۲۶ با باشگاه و تیم ملی:
🇧🇷
رافینیا:
بازی: ۴۰
گل: ۲۱
پاس گل: ۸
❌
نامزد توپ طلا نشد
❗️
سادیو مانه:
بازی: ۵۵
گل: ۲۴
پاس گل: ۱۳
✅
نامزد توپ طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105893" target="_blank">📅 21:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105892">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1bc3d2a35f.mp4?token=DddDfSj9H5i7NH5TYj-q5AP8N8rjuYZSEvpoaqW4AkEx68mHVp_ZbyjwRY9Iu320gieyIBVLhMKLLw8FNK3FlFZPfls7bCwWy_4BG6JqWRW_L49GoDcgg6c9yOEFWpwlLecvsqT97UE8XYKjluyeRjYwlNdpb6a8xzs8DbCeiHDj5hfHX2NLjwBVRtfCuhPsfOe0FAHHyAwk3r9gCeATixuA8YEf-wjuF2FvNy7MrDf5uaF1hAgHntT2g4nDch8I384HGhCp7eJJUkp5YRKEEi4OpYzHjxQXlIYDCIV_X80V8ybLYDd7cUEPZW1HAn82tpShCXowFlN7P8XMGNqQcg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1bc3d2a35f.mp4?token=DddDfSj9H5i7NH5TYj-q5AP8N8rjuYZSEvpoaqW4AkEx68mHVp_ZbyjwRY9Iu320gieyIBVLhMKLLw8FNK3FlFZPfls7bCwWy_4BG6JqWRW_L49GoDcgg6c9yOEFWpwlLecvsqT97UE8XYKjluyeRjYwlNdpb6a8xzs8DbCeiHDj5hfHX2NLjwBVRtfCuhPsfOe0FAHHyAwk3r9gCeATixuA8YEf-wjuF2FvNy7MrDf5uaF1hAgHntT2g4nDch8I384HGhCp7eJJUkp5YRKEEi4OpYzHjxQXlIYDCIV_X80V8ybLYDd7cUEPZW1HAn82tpShCXowFlN7P8XMGNqQcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپرگل تماشایی آاک‌یونان به لاسک اتریش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105892" target="_blank">📅 20:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105891">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a209d7f89d.mp4?token=VhBvtGKlLzNuhlDuLganhY4mpRvJ1KTfx_IRzaWxcpt5Qb4oIQ2SJLlR4f8nMszDoQ6MYYX3_mBB3vtls41Psu7L0mEIsqP7VdEDFxIeN1bWBLgI8aKgVi4jJLA4PclQQwK10KR1IKDOKCt4YzWQAM9SDnjyVM6omFgJZwTyicdtCxKSbxErjVws8AYd0baW6GWegmNFACJyBnF-_gTPFvZ8Aa6JQj98cxETTI3Fx6VdX3LSxrNvFKlEVXca1L7IPL_4NARYJ2bDSjTTlXilz4ZUjfFwon5Zygtyl0qrMeDbRY8IC4gpPSwoS3Wex-n025eySimdbBykwBSACuwAbw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a209d7f89d.mp4?token=VhBvtGKlLzNuhlDuLganhY4mpRvJ1KTfx_IRzaWxcpt5Qb4oIQ2SJLlR4f8nMszDoQ6MYYX3_mBB3vtls41Psu7L0mEIsqP7VdEDFxIeN1bWBLgI8aKgVi4jJLA4PclQQwK10KR1IKDOKCt4YzWQAM9SDnjyVM6omFgJZwTyicdtCxKSbxErjVws8AYd0baW6GWegmNFACJyBnF-_gTPFvZ8Aa6JQj98cxETTI3Fx6VdX3LSxrNvFKlEVXca1L7IPL_4NARYJ2bDSjTTlXilz4ZUjfFwon5Zygtyl0qrMeDbRY8IC4gpPSwoS3Wex-n025eySimdbBykwBSACuwAbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇪🇺
اولین گل‌فصل لیگ‌قهرمانان اروپا؛ گل اول تیم استون‌ویلا مقابل کلوب‌بروژ بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105891" target="_blank">📅 20:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105890">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxUt0bePxSvm83rFv9jQZ6tsYR2W2cWyup8iL81Gt1mWPhFmgzGRog08HElPgo8ivO4UdGTo8oGRzRE8RrdxUzt_5uCjeB037agp9fXRoSDF2cOz4vaY6AZ2cIrKt0ITzLi-M_YecYWX4Gf0ruqTI1Jw8E5ti2wjMTBd0uXqQ-i9r9IVmjOITAlBLAft-iifRhZ7S56WOelw-3WCTAygriYXrnHgWi2bxbqV_GkTQym9AtdUun1wtyKywsGdY90Qg-ZNP8JRvsyo9M3x3HpN9MZB8kBRAEvQ-RFloXUwIsgStis9dXXbllkIJY1gqia4CZXBjwwoBoFR9qjBI0EDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
غایبان پرشمار رئال‌مادرید برای بازی با اینتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105890" target="_blank">📅 20:03 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
