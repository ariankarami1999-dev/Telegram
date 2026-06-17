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
<img src="https://cdn5.telesco.pe/file/UBNIVpxf4FvS2rIN6QVoufTh_hwWFV9w9g0GpKpalLqYCMZwloDseJscb0f--MArqt5Yq2DYNeFQXq50mppWj0BrcpfnsPElqi-ZbomdYoELk_0nUXRbylUjLT41ka_Yedtpj8FmUTd4Ema1zOd7RsfJ72PdGsK2p_NgVJpKuE-5lwNjywTjr4fYRM1AJK_QFqetUonKFtJlW3Ean20XeJoA-NOnDtS6_4UewVd0XTxhIKgq78koBs23bbdVtKoVEhh0FuFkwjJgoG5DZU9KwQiIpZHqL4Ox8Sqp37VxmyQKuycyrYfFGp4wh0XG4l3H9y9QkODK8OU-hnWYDfb2DA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 636K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 17:36:46</div>
<hr>

<div class="tg-post" id="msg-93933">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iItNt5hAKEBjVFDfk0_ko-ZO0SRfwgw7sra307hNELGXkIhFm-xY74Qqfe3Cv23DPEJFIrjWcCpiNp4f3C24yMNEcwhzouSDaNDuhtfqjPDLF2tdOlmvEWXDcO0pVSh1R-CqC7ouZ1g-ywPV-FoIDNvi_WlI4qwvANVgMbiig3wAVIG7SZcUU2REC5qRzD3zak9qRxjG_iPNZWxUmwgjLsnPnUetAO6q9zA__v-LOn1MTbYBj8l-vYqYKFbXnJkphj-wUMjzGD_PHJ4BdjpVwJFKTAIo-cVo5sMsIOy7oJQ7x28NnRiaQh7kEocgA2kmtbmHMUt3oZ6mElbwoMbH2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Diamond
💎
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/Futball180TV/93933" target="_blank">📅 17:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93932">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jf_mNi1QwGoseJ0Bd4olD3E_qIeYHI5st6_vuu2hImZpyMnU7uWo0in3UaBAmGvKV-XMQF7NDjl12iHLojss8CVKePzcJOBtkp2pBHLuo059u34YClTPdXHfetkPBdCFiGov4x7lwFSTAAF-eHKGroK8_5MFR1G5w2i5ev5RKkd4zey9ed9LbLnoxaUuMNr0scKTqRPfWvxNNV8qPYhpUx74jWycMszdzRZl1xdirVLutI4Q3KGHkg5NfqzBbcaOjR2p5zJdDAxiGDkvHARkCS6Poom8xQ9NHgfJeTrot1v0yPl55784txgXP6Zn7kfzxyDR8o2hPMCFyuysmBqOzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رونالدو نازاریو:
زمان آن فرا رسیده است که جهان از پنهان کاری دست بردارد و این واقعیت را بپذیرد که لیونل مسی بهترین بازیکن تاریخ است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/Futball180TV/93932" target="_blank">📅 17:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93931">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‼️
🎙
روایت تلخ رضا جاودانی از پشت پرده برنامه جذاب و پرطرفدار «مردان آهنین»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/93931" target="_blank">📅 17:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93930">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c860678c61.mp4?token=JCOmqvDWEe-0xDfaisAoyZtPJbHff36t_zAAhKq4h9wVgFrhSGyOHH0Atjdb4BKJ1NXYQyDjP0Hum9gvJKFdbTG8cX0ix0dmg1pFxWuig8GoZFC_z7QzdqzG_cUqnqJgzugGvyQaU4f_I6vFhI07ALdZWTfz0-4ueIyrElQkmvq84fm6amt6xm70veLpjqgGhe1Nmuvfu3jPTafjuYLgKSoE8uv2D4a-niN1qDTHUQCUWZF9ysVWM5X9ip3pp1sPmTyInEykk7-46DEICS5S-VA8JAZbM1tQhtMxGcjlH8pkkClY8xjsns8EWH7_q3UsEzcjMLaPg1SZaBK74DgyNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c860678c61.mp4?token=JCOmqvDWEe-0xDfaisAoyZtPJbHff36t_zAAhKq4h9wVgFrhSGyOHH0Atjdb4BKJ1NXYQyDjP0Hum9gvJKFdbTG8cX0ix0dmg1pFxWuig8GoZFC_z7QzdqzG_cUqnqJgzugGvyQaU4f_I6vFhI07ALdZWTfz0-4ueIyrElQkmvq84fm6amt6xm70veLpjqgGhe1Nmuvfu3jPTafjuYLgKSoE8uv2D4a-niN1qDTHUQCUWZF9ysVWM5X9ip3pp1sPmTyInEykk7-46DEICS5S-VA8JAZbM1tQhtMxGcjlH8pkkClY8xjsns8EWH7_q3UsEzcjMLaPg1SZaBK74DgyNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمرینات سخت و نفسگیر شین‌مین‌ها دفاع 20 ساله کره‌جنوبی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/Futball180TV/93930" target="_blank">📅 17:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93929">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3804d558c.mp4?token=FzdAzJoBKAS4sW2GjWFAQMv6Fb9rqKFMhW626jZrUib0TqMPwy2AotqjUB5cv1Tqz3maR0_lHDl5Gr8qMA6WMVXxoZcuaFxbWqdurUVEeasJ7Z_bxqFACiXqjRmgKa9KNj1qeWMjBouLZ31dn2ySONdJDvDltd90_f8vo5oqOWjeC8ftSwTeXoD8AwpaiQ2-s9chvHOlXJvhZkDW6RCmsC8D1hYS9S7hjfLgNLAju6oXY8K2hWOM46q5JZGNq-3-faRujzHY4YBqmRVa-qc0IBOCUyew0hzDfeCqr_DhxoTPe77inhnWyJMqzbfDYipDXuPcyTnH70rfLGt0m3tBNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3804d558c.mp4?token=FzdAzJoBKAS4sW2GjWFAQMv6Fb9rqKFMhW626jZrUib0TqMPwy2AotqjUB5cv1Tqz3maR0_lHDl5Gr8qMA6WMVXxoZcuaFxbWqdurUVEeasJ7Z_bxqFACiXqjRmgKa9KNj1qeWMjBouLZ31dn2ySONdJDvDltd90_f8vo5oqOWjeC8ftSwTeXoD8AwpaiQ2-s9chvHOlXJvhZkDW6RCmsC8D1hYS9S7hjfLgNLAju6oXY8K2hWOM46q5JZGNq-3-faRujzHY4YBqmRVa-qc0IBOCUyew0hzDfeCqr_DhxoTPe77inhnWyJMqzbfDYipDXuPcyTnH70rfLGt0m3tBNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
🔴
اعتراف امیرحسین قیاسی به استقلالی شدنش؛ بعد از گل آفساید گولسیانی برای پرسپولیس توبه کردم و استقلالی شدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/Futball180TV/93929" target="_blank">📅 17:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93922">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f4sBd0x0QjYGjegmjfI4-ahOVFO7bqeItg6JqjUIdDNwKCudNqhC0lBxIMde0b4h9AnMzKOnPp2Vf3kpdZRijDUMofwVy_wsYQxMRwprY2q4CJ-VpZG3dd_9hwkg1H5MhHmM4iH1ubVES4LAz-75FmhrYo98Vjy9hVWGbzXW5N-CJz90SLL3BU2k3sTVcvOI-BRk0WFft1jAwpOOCC0F2rC8eAPtWOqLrfRekcy9Ij0kzluZ0df7UcuDTbwJrXZSsFXAr8b2YcnMtJzkLO0CH9-7_xMmP9X-q9pGe8POYrQXyGlfmSMuniU6jFna75i4dooA6TPp-imsGCeH5BiPEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aCAgsYpPDVwmbI4If5eIPnC-bEhivpMjngpNx07Sa6JEonquXtlg_51E2ePRlSZWkBLLl4HJXK6Ldvm4MsFnfPefCH03NqvDiPBA1Nd0T9yWEnjVriCr0jKg7jOQdrFdvk_t8B568LAUFsMkvMqRvScvgjEq-Y4BPpNcQhXDxst9HGlhIZc7xxks9x9EFF62-gBcSr0R4Vq0Vp1PM3wpjoOkJPpV9WKFFD9no4is_4_i3Fgqz_sxlz7YtAUDe6YMXmTKn4vknMdpWLA3HXA8v3E_yNvQi5rCF8UfhVqLOXwxWHMccbSvQCDUra2PQXAcMa-13eQQwfIDhaP9IMWT8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3VOezO1rXchWDeLJMxD1mZhaIu9bLE0jmYNEOpnmXpeXP0Nuz6Xp1wXPo-1_25xpdyU8_34R6gndfla0sfUfbSbVP0eIWKCnc2Mg-LuKYagGMul2xWKuW5hAakmBly1mvSZqxnVXlvtJ2w9weHJ7ojgzteqIBntSig0XEa9GFJIiQ5d5N6CObYBXwZYCOswhowGew0JdPaJ7ZZJ5odjulvtZp6VPZyFaf0U8qfUfInpqziV8aeCHvND5MCAe1jt95zcjdD6H5kMqBqYrkkdvPnw2gvpiH790yzj0a7SOfHFDil1ZvGomSB-7k8Fw_K5ehcSsI2kZlHJmFP39IupoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7hVIGMv0f-juJs-ArowbZp87_IbHoVkowau1C47bPUSh-uiQ6169YXW5XgyQa8F-cQKxZYPiN73R3K9IpQzWjoEhBLmJR5-FTycxTlpIUPMFcoQRNESOqp6fw9M2sa1xo_wS2dqDXffzQ_2IR-9aR5ZQIemngHco_ql24he0GMwwNPgz5ikXkgqpoZ8o-a-EtUSptQvLAwdkRLqiA_taYRHws5jXWikL4xiVhQtJ3I7xKsqz7Z74wLEnH3mBHVUZcKbR2oFIfuHARAQvGJvtrB9kCwejHVjUrLnNaE3A44WMgSPogi_A_YxPA21qrAw5FiJ7bjJd1Xmv-6wR04WqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NoJ8MFYpnD_MTWDauXZzUpMS-nE0BZ2TKfVBqCUovxnBLF2r_b571YYe2MvaKK2LUyRlUad1DA--It5MArbR19Jr6CRxJegABQWBZ0_WlVRAA1h-SOXblL4WKnEL9vEHhC2NKbnYuKDrUD28cVT0laTuxPjegkVVD6QTNQfxfJWM-lwW63CkeQTPN833g29r926LS4cVQK0oleK3yFlVxmda_ZMMX4EvV5l-4SPp77772lLoGNVCUCXc4YKIPFYhnhL_kQuhnsPcsxWl5_Y-dBJNJvFKGWGhKlxkNB2-S3e0aR_Sqnqt0vGSYtdPIzO_a0EN_o2R-EqR1Fm2ErGFRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CpbS7EnNbJHks-8OLHdbTq2C0Lud2KM_0FfuwBUrVfksYwHmqbKWCPtds-DiYCYeheIdZpaV3tUpkDOyJiaBTTdD0pN-KUkALrGS24_Ie67gmsdVCIQ7Pa2D2bXyhFecZYfiKT2kQuOYr0YCqgiyhq7gqGQvv0jQQWGJgEjF6c9lTWrgO6IIu_D31AeQai43dH-7Ii6OiEte3aQj0TwM5mOS3mcIHvmmo0yVDUpIuCMSkHE3rfQswPezNJ3-1i9vZiOqWCwHXvweKn68ahrQ-1llH9O0dTGFa1Dkq8v65g8H9cKLZu3hYH8OHA3y3JqxsCH7iALSq7ie4AMTE6gASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DblquF1ZAgP9I8jzMlUcBleoqT1tEQLJCEEKNxZJe4m6CCaAom-yDpXLj87_AfMM4t7_ZyocQufvX4YTYCuqLL77mNFR_29vkefT8H2MP5SRF0pi0Q_vc27NxVi774yBuhQz_ZdGPG-kG7tEszRPEZ6wnSdd2GEPtCLwxwwShTTKne5rerK4aGy2egZhK-rrIA6nwMOMXJP9VJQ4G1eexBWIx5BZt35eobuQlBSM6HcsVNLxvoOz-eZzBoAhXQCLiIoeHRfqXAeLwAkauyNmDZQ8q6fOPGyQK6YG6mQmirNsg9im_Rul77qGhHWjIDWUHMnwd6Of3VA_iRxMRBn09g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
بازیکنای آرژانتین و زیدیاشون هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/93922" target="_blank">📅 16:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93921">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f946f90fc.mp4?token=G_fFZf_zUQnd0TeARIiMQ4sOEafKcx7PcNJbCtv8q183GMtx7qm3YQfjQVaBkq4YvNWW0DY0eSBrLVYTV3Dpj-Dj0dodxufNjrXvyGz1SEI_aPihkH-BZEPd3tXfwAGnl3CpJFkD4r2ZCDrf3n_kyxaRgdYnZFOI-B2wagy79nVTd0BaoM1X7VOu4STO8wT0DP4P8cbwez-LdgmR0mkiQi8EBHItRUzwJtkkjJBcfHjfqu5SmHhScSeRE16zlU7N1rhEcF5NBwm8riexUYM8ns5zJnXi5GPqxRKaJN2516sz2xuMkY5BoJ0mW-U7GvWifADuIh_gReISuiLPdhXqsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f946f90fc.mp4?token=G_fFZf_zUQnd0TeARIiMQ4sOEafKcx7PcNJbCtv8q183GMtx7qm3YQfjQVaBkq4YvNWW0DY0eSBrLVYTV3Dpj-Dj0dodxufNjrXvyGz1SEI_aPihkH-BZEPd3tXfwAGnl3CpJFkD4r2ZCDrf3n_kyxaRgdYnZFOI-B2wagy79nVTd0BaoM1X7VOu4STO8wT0DP4P8cbwez-LdgmR0mkiQi8EBHItRUzwJtkkjJBcfHjfqu5SmHhScSeRE16zlU7N1rhEcF5NBwm8riexUYM8ns5zJnXi5GPqxRKaJN2516sz2xuMkY5BoJ0mW-U7GvWifADuIh_gReISuiLPdhXqsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
حواشی امباپه در ماه‌های اخیر از زبان عادل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/93921" target="_blank">📅 16:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93920">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7zEpHbzCQT-97YdET0RXhkh51j5JJL8dn9CUL6HUv_s8UQVYgmLoSYbE3nVD2UxCs-enstHmFy_ztMwDgKf4VGxzn_zp9tmA555qXeATkWBYMg--9aKl7mdd_i1qUvwZDysb23mYAe-Djd79DeQ_EJc_sZAu3gqKU-Z5s1QJxLS_wdkWjKa3yaJfEDx36vRxyohVB05jTlqRyuqDeykHywxm4GeII4Y_U080rhD37cWXBc6J7I3vJkxUskeVCtCpX8RI5IKTPrHnefBoQJHqMeywrJTmu48DGVulZCTjIkIVUKLLYrSdKzyQDaXVtCOQVetbVwqMZZdj-drmlnv5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔺
#
فوریییییی
از خوزه فلیکس دیاز:
رائول آسنسیو ممکنه رئال مادرید رو در این پنجره نقل‌و‌انتقالاتی ترک کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/93920" target="_blank">📅 16:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93919">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S_CCSyMy2RPO97lcnDd2YeQeNAloX9uVF7ZnKeqM1hwI1pCxLjwJxkYyzm43TLa00RP7DUH7uUudzrP9FAVR8wN3-2IMaAaU9Yefvnf057Z29KTdtwt5Abhi2lEmVqHSmq9H1iqwBFqu_hue78efHL_mQKImGah-p1uiEdYFmZSfiIr6v-sR5Ykk6DYUs-QIx2MIaLvdEm3r7aORFTMclHEuzzGEMuxgUd-YoCF-fTtMgf4ndXHsjPd_viqmqSRxD5DuuTv-p4ZkjuHheZZgRtq8cTD_vYHsPY-n94ZcDtR90pLgy3Wou42-HZ-MRvFxHXSonnQmXX6mJUXqmyLmog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
مسی در پنج بازی آخر خود در جام جهانی:
🇦🇷
🆚
🇦🇺
مقابل استرالیا | گل + جایزه بهترین بازیکن زمین
🇦🇷
🆚
🇳🇱
مقابل هلند | گل و پاس گل + جایزه بهترین بازیکن زمین
🇦🇷
🆚
🇭🇷
مقابل کرواسی | گل و پاس گل + جایزه بهترین بازیکن زمین
🇦🇷
🆚
🇫🇷
مقابل فرانسه | دو گل + قهرمانی جام جهانی + جایزه بهترین بازیکن تورنمنت
🇦🇷
🆚
🇩🇿
مقابل الجزایر | هت‌تریک گل + جایزه بهترین بازیکن زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/93919" target="_blank">📅 16:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93918">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58ee7676f0.mp4?token=u2qCR74ayHpiNL2WS2awZBQTm5vZs4u6PTDDf_sHbza1lpx7_OKZkDcdgwNktrvZ11uinauxGyyAkIVjYk90c_IH70w9OrOo1XZWWTeW2Re5wBdYyGfQr1rFHPnKgzQQ2fGu8eSN8eK6MHEVRHLF_25KTZMp-hSKqEe-l5CyGPrn0NfwLQCTqSoCUSPSmSyb2DRxWnQVuYES1AZe9jDF6jsz5m7OcPsYdb-oP5DSB_GFGHf0dEDIqcQQF5fOXxCABeK2Fv2J_GjA9ylO-uV9M7eVEOLqH8SkTsXiLagwAQWQypXqHeOWL0U_Ws3BcNw68wtf1gbHuJNHrYyIOpwSog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58ee7676f0.mp4?token=u2qCR74ayHpiNL2WS2awZBQTm5vZs4u6PTDDf_sHbza1lpx7_OKZkDcdgwNktrvZ11uinauxGyyAkIVjYk90c_IH70w9OrOo1XZWWTeW2Re5wBdYyGfQr1rFHPnKgzQQ2fGu8eSN8eK6MHEVRHLF_25KTZMp-hSKqEe-l5CyGPrn0NfwLQCTqSoCUSPSmSyb2DRxWnQVuYES1AZe9jDF6jsz5m7OcPsYdb-oP5DSB_GFGHf0dEDIqcQQF5fOXxCABeK2Fv2J_GjA9ylO-uV9M7eVEOLqH8SkTsXiLagwAQWQypXqHeOWL0U_Ws3BcNw68wtf1gbHuJNHrYyIOpwSog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👀
انصافا این دوتا دختر ایرانی خیلی خوشکل چالش موزیک جام‌جهانی شکیرا رو رفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/93918" target="_blank">📅 16:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93916">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gN8dKCwYVX9uBmk98ZNNogNVVo5pbrOtoOUOALnPtq5Bq1X1sd8JlSKof--0CLxeE7XOave-qFCImcH5JitVewTzqmLsOAkI9AoIDy7CYbgdQ671SqZeEdDMukYgRYzNDQgjE2dB5BtOqpcKZJGWJq41QYu9NIzS6Jgd0JEiENYLQYWHdsLg5yEOdz6e0u_LjEq6DJaDizwNKet4_xZfOyGhicD1xsfc81c0EsXhQ3uh72JIhEdB9vUhNLVcOO2XP9xVMh8s0_WqRppopproKUmfUjl19WN7PAElGAE2qJ86i4D2RWCS5yEDDGXfcP6VVvcF3JBMa4cBMtGZcnEKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
متئو مورتو:
ژابی روحش هم خبردار نبود که کوکوریا فروخته شده، هیچکس تو باشگاه چیزی به اون نگفته بود! وقتی رومانو توییت HERE WE GO زد تازه فهمید که بازیکن تیمش فروخته شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/93916" target="_blank">📅 16:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93915">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871e6d3b20.mp4?token=oAkxonzC5K5n7OoGnf0V29cKxQ6Z6RlQLjiE-8FU5OUsdi9e4WqvHCiJp-UIp0HmX3j218X7RwNku5Z90Et5weGITASC3YdcvSl7n3F-1NTVePwEs-hrIZLjXbS2vm1rbTy5edRpya95J_0ncBm1OVNY1BfEzlaFdxlvo4V1Wi4Wh6A3ydbP8u2OWws580jQyWmNDhirzRAhmhoSCS99iMRhn_B-ielSMM7XuuE-sZqP-M2z0Z9U0CAOp8-e6lLqzbLT4PcKbErk0EtuwHzyI2MsyvnTnninJ7Bugt5ayYQno0KJZ8Q10GYNuZEh8c5FQrpb_pStocQAYfjUdpWgjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871e6d3b20.mp4?token=oAkxonzC5K5n7OoGnf0V29cKxQ6Z6RlQLjiE-8FU5OUsdi9e4WqvHCiJp-UIp0HmX3j218X7RwNku5Z90Et5weGITASC3YdcvSl7n3F-1NTVePwEs-hrIZLjXbS2vm1rbTy5edRpya95J_0ncBm1OVNY1BfEzlaFdxlvo4V1Wi4Wh6A3ydbP8u2OWws580jQyWmNDhirzRAhmhoSCS99iMRhn_B-ielSMM7XuuE-sZqP-M2z0Z9U0CAOp8-e6lLqzbLT4PcKbErk0EtuwHzyI2MsyvnTnninJ7Bugt5ayYQno0KJZ8Q10GYNuZEh8c5FQrpb_pStocQAYfjUdpWgjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
▶️
تحلیل جواد نکونام از ریدمان قلعه‌نویی مقابل نیوزیلند؛ عادل و جواد جفتشون روی کیری بودن این تیم نیوزیلند تاکید کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/93915" target="_blank">📅 16:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93914">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9036c6b9f.mp4?token=pvTR2Ot2iizJB75stkDAZLkzQqmX28QnrhBFfwbR_LUTKZRXfQbRKacxSxu1W9PVwWtDyYL3MbPVjN1hiWrBgxTvLjU5rldHimzejEOeIBTArpUle4N_toAxDfVGvlEgNcTA4KqAL5Av7wsQzvF2xyv_T4KkbXX5c9ModIss0IYIok2JnSIWkr52--uumQUtqOytViK4KR2GpMxwZ_mQErcF-Nv9h-YqIS5m0gZNHOs8uNOxyr4QAtHVMDM6LC7WwNKRJYoca3rlKMsx3lqp6gTER7oQMTcytvVjhO6xzZurg5aWVN4VO2HAZj_XEWhy8uXTpbXppDcppIbV84Gm3zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9036c6b9f.mp4?token=pvTR2Ot2iizJB75stkDAZLkzQqmX28QnrhBFfwbR_LUTKZRXfQbRKacxSxu1W9PVwWtDyYL3MbPVjN1hiWrBgxTvLjU5rldHimzejEOeIBTArpUle4N_toAxDfVGvlEgNcTA4KqAL5Av7wsQzvF2xyv_T4KkbXX5c9ModIss0IYIok2JnSIWkr52--uumQUtqOytViK4KR2GpMxwZ_mQErcF-Nv9h-YqIS5m0gZNHOs8uNOxyr4QAtHVMDM6LC7WwNKRJYoca3rlKMsx3lqp6gTER7oQMTcytvVjhO6xzZurg5aWVN4VO2HAZj_XEWhy8uXTpbXppDcppIbV84Gm3zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت‌های جنجالی و تند علیرضا مرزبان مربی سابق سپاهان علیه اعضای تیم‌منتخب ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/93914" target="_blank">📅 16:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93913">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
رئال بابت پرونده نگریرا رسما از بارسا به فیفا شکایت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/93913" target="_blank">📅 15:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93912">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
رئال بابت پرونده نگریرا رسما از بارسا به فیفا شکایت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93912" target="_blank">📅 15:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93911">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc6d87c9a.mp4?token=GV1H9BFtiPwm-dWj4j9JHUEz5Gf5Np4pG7KdICmcMmIas1mkNBo--NA6541El2nbKsSmIQMvwoDrZO0LCFv9OqN2Ndxwhqv7CE7TlTo05PDQfUYILxzQNUKc-FxxpVPXTumcvpAePyqjHrPmrskqTU9crwCrgoywr_FpYn8VQJmzQ-qR_DhxyWQg_iPO-MyprxIGQztTwKQmbFbxZZzm2sf5zgnGdBbDq-J_myZm5fznafFFfnYbFsHrTouEyZgPt04yHQmsQRvfEAurNtZD6DOlVIGIG497s06eBE3FiwVi-J9JRSUIHZIRw5lA0mUsxuPu9N2IYxO-Tj3pK7XcAl-ohZcin-WG7S61B_46nwSxpM5LduiW6xQouEWlzHQE0wttU3Bv-ynHfFNblGTABtZTyIj0HnyAWyxlAHszYIrBw9fenL4PXHusp6eyC7NQf2R_7LD20kGnwFlysPpdW3l96IdAsJay1HTcBf6_JaXzangEwEVNGrszoylM00pJpi1OSXfv03Vuv9WR6H3mEG5n9eB2q2ajPLtyGAsjFx2D0Th0Y4PJ7cnGFnQCd70SzYqVeTE1XUx3uKfwL4XB2HXRhL175YfC6r647DtRmegqZVYLcE9V3JGefZNvxb1UrT4SynbqUsUW8nH6SHuoN4eZsKMFQLoLerHowoYVZhE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc6d87c9a.mp4?token=GV1H9BFtiPwm-dWj4j9JHUEz5Gf5Np4pG7KdICmcMmIas1mkNBo--NA6541El2nbKsSmIQMvwoDrZO0LCFv9OqN2Ndxwhqv7CE7TlTo05PDQfUYILxzQNUKc-FxxpVPXTumcvpAePyqjHrPmrskqTU9crwCrgoywr_FpYn8VQJmzQ-qR_DhxyWQg_iPO-MyprxIGQztTwKQmbFbxZZzm2sf5zgnGdBbDq-J_myZm5fznafFFfnYbFsHrTouEyZgPt04yHQmsQRvfEAurNtZD6DOlVIGIG497s06eBE3FiwVi-J9JRSUIHZIRw5lA0mUsxuPu9N2IYxO-Tj3pK7XcAl-ohZcin-WG7S61B_46nwSxpM5LduiW6xQouEWlzHQE0wttU3Bv-ynHfFNblGTABtZTyIj0HnyAWyxlAHszYIrBw9fenL4PXHusp6eyC7NQf2R_7LD20kGnwFlysPpdW3l96IdAsJay1HTcBf6_JaXzangEwEVNGrszoylM00pJpi1OSXfv03Vuv9WR6H3mEG5n9eB2q2ajPLtyGAsjFx2D0Th0Y4PJ7cnGFnQCd70SzYqVeTE1XUx3uKfwL4XB2HXRhL175YfC6r647DtRmegqZVYLcE9V3JGefZNvxb1UrT4SynbqUsUW8nH6SHuoN4eZsKMFQLoLerHowoYVZhE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کنایه‌های تند مجتبی‌پوربخش به میثاقی بابت تماس تصویری با خبرنگار حزب‌الله وسط برنامه فوتبالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/93911" target="_blank">📅 15:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93910">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ui0ZsaeB8a-NwHujIa8eB4BrNrwBIC7dijk3hcRz5U9mzwW5ZofmhDjxw-A-r7NaPEUuXTjEsMbNCmcooJjM7jAS-_yKRLO-nFpBCp8DiNj9AIzxBxucm2RZXOKmai6AYe8GEW9eRP6h9uhHLD7PrSE95cvi8JtrYqO07iDmF-uOBIW3YKSi-wdVjxfcMxK6vT6mU67OBXbzJlGsUJ3tG8iu-nKFqF9I3oyS4Hwqi7-tjmshXpLO7_lnmqYS1mPjOMS8n5k1xOLtb-RTk65cSAZkYm0Yu3JR9bY8Cr9bE5yhk44Y8OgTq-SgbbJ1zZNXqNc2NiJSy4ja2GtNMDg_pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی قصه خودشو با توپ و چمن نوشت؛ قصه‌ای که سال‌هاست فوتبال برای دنیا تعریفش میکنه.
👑
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/93910" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93909">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🏆
ترامپ:
وقتی تیم‌های مراکش، الجزایر، تونس و مصر را می‌بینم، از خودم می‌پرسم چرا این کشورهای شمال آفریقا با هم متحد نمی‌شوند و یک تیم بزرگ تشکیل نمی‌دهند؟ اگر این کار را می‌کردند، به‌راحتی قهرمان جهان می‌شدند. این نشان‌دهنده کمبود رهبری است؛ شاید بعد از اینکه کار نجات آمریکا را تمام کردم، برای ریاست آفریقا نامزد شوم تا آنجا هم کلی پیروزی به دست بیاوریم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/93909" target="_blank">📅 15:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93908">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/568815587f.mp4?token=LLWcErIWWGPKPiP5jyJFEqByjcc9wpTlKAykA-nyeWQrCV4hPcMC70vmL8jgJqrlwlf3YQNDAQA9W_TqtnZL5MyR5RNo_KT5B5pYG3iD1Gqq9W6wjblw_kxZySA6gOzWFfZukgivAL0y55PQj6P8TcDH42SSfvidCK9TSe_3kop0TcDKAMRNkLXrOO6ojM6qIgrk0lzH-uTNcKmHa95d36FhRw_2a1NQPqmPmLJ_bKQBKRHgVQEntia7_JJQp6SsKika2QmAyfE9lJ5qqBjDea72V1KCOyDi5I1uOAOMCY-7rDBQscPvvdy0o7-h5g5D54AQCeQnClZMSQKv7DbKUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/568815587f.mp4?token=LLWcErIWWGPKPiP5jyJFEqByjcc9wpTlKAykA-nyeWQrCV4hPcMC70vmL8jgJqrlwlf3YQNDAQA9W_TqtnZL5MyR5RNo_KT5B5pYG3iD1Gqq9W6wjblw_kxZySA6gOzWFfZukgivAL0y55PQj6P8TcDH42SSfvidCK9TSe_3kop0TcDKAMRNkLXrOO6ojM6qIgrk0lzH-uTNcKmHa95d36FhRw_2a1NQPqmPmLJ_bKQBKRHgVQEntia7_JJQp6SsKika2QmAyfE9lJ5qqBjDea72V1KCOyDi5I1uOAOMCY-7rDBQscPvvdy0o7-h5g5D54AQCeQnClZMSQKv7DbKUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥲
خوانندگی بدل‌اندی در کنار رونالدو و سوارز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/93908" target="_blank">📅 15:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93907">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8d4vYdaqJPSC1wJQgUTbTPCkLWcuvcQbfxZQ_9dumnPm4lI8SEfG60-N0HoY09RmQVrrdPUv3nVtaZRU-vOeAe1RhSbExvx7H9QXmHRnPE_VX-yXzR0jWKUyU0gYOm4KaUSoD8yU-W7pxX2F5elVuHA5dP1seCBopjRk5ALgqYf6ZdkyTE77-STBgtdUFVjHZBNrDjqNUWFk-SGjrKDhdKQvWHzThrpyiK4BRnqFsk7tPmMnQVCas17IeVwBpDGR_5S7dSqpbWt9eo7qFwzRrQfbi4vRnEJ6AoSD3Gsczv3dbbS44FtsIK6CePU867PJdzkTA3wj5OVfExobtjeKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین:
هدف ما قهرمانی در جام جهانیه، این موضوع اصلا جای بحث نداره و از روز اول هدف اصلیمون بوده. میدونیم کار خیلی سختیه، اما تو سال‌های اخیر بارها بهش نزدیک شدیم؛ دو فینال یورو، یک نیمه‌نهایی و یک یک‌چهارم نهایی جام جهانی. امسال هم با مربی جدید و چند بازیکن جدید، انگیزه و هیجان زیادی داریم؛ هرچند فشار این تورنمنت همیشه فوق‌العاده بالاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/93907" target="_blank">📅 15:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93906">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/059027f16e.mp4?token=eeQC_d_vXfQ3EAfBIdgywpmZhxy9Ktvsko_LSYucbK1PuJNlLXlwLz9dBqFgDz0I5z9tgpMA-eBNwWlCsB9pbrEkG5ot3esBHgWTC_u4ycc8aYcNBKb5b0fnzMAbSebCZWdq6mdUhZH0iSAeWj84V7fMfUepoS-iR-r8zMnuVpRPms5fK-lpck9h35hNgYa-HdlYVWwzqRoM4BTJXITSsB3pG3BdiWDZzR9pvUUNApAN-3EiDbTgjJs3QUv29yTHJVChfeaXQnX0jawB2n0D9yVINA71Jgm5nAhwdZd5VXloqC68yjKUNPBfSgKlVeP9-hH7pBq67ili6pIgms30ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/059027f16e.mp4?token=eeQC_d_vXfQ3EAfBIdgywpmZhxy9Ktvsko_LSYucbK1PuJNlLXlwLz9dBqFgDz0I5z9tgpMA-eBNwWlCsB9pbrEkG5ot3esBHgWTC_u4ycc8aYcNBKb5b0fnzMAbSebCZWdq6mdUhZH0iSAeWj84V7fMfUepoS-iR-r8zMnuVpRPms5fK-lpck9h35hNgYa-HdlYVWwzqRoM4BTJXITSsB3pG3BdiWDZzR9pvUUNApAN-3EiDbTgjJs3QUv29yTHJVChfeaXQnX0jawB2n0D9yVINA71Jgm5nAhwdZd5VXloqC68yjKUNPBfSgKlVeP9-hH7pBq67ili6pIgms30ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
ابوطالب‌حسینی بدل‌اندی رو‌ آورده برنامش سر به سرش میذاره
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/93906" target="_blank">📅 15:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93905">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2fuRmXlzzOjGsncA6FnmaAxqc-iD87tS0y2kyCOh5J9bHoFuoGXzP8f4EOgKoczDWKj5pgcOURLAzOerbYMj4HGcSwTv-eBQjrRaAoP3ZnbvZRyI8f64NGHUM65en7CBUN1ylVbneFHqSvL03VgR_2zkJJ8k1qzgHwoEIVx9VZ5T-O6JZBGMBWxUZNKkTjyZxSO2LgLvbtOKGZJai6nw4QRQe1UUUqy0aurM3bMs_jmkvdHX_kV2B9wXIoLRQfNAsmetoVE4MSZhNqz0LPjhHMII1pROpL4ny9QzR60eSs6pJBX7HG-BsZR_N8JZt3LsA7eAYYm9ifhZQ172hqF8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
خوزه فلیکس دیاز:
هدف اصلی رئال مادرید، مایکل اولیسه است. مدیران رئال بعد از پایان جام جهانی برای جذب این ستاره اقدام خواهند کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/93905" target="_blank">📅 14:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93904">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5799d9a11a.mp4?token=e8pkT6KKkPWCkkzNUJmUuxCGFPEazZwkNK2b4onOaCNbV7anUyTCw0cmoNa-u2WkWfpXvK_FjMCz1o8NLc0gp1c0ZNjjRTQRvIY65OXg6KLwRgK8Kf2N94fke_NlfqaIBnMGYjM4Y3-OWbfduCf0Rc9-x2v4IQ7gsgVgWsghrf0-1UrableH-KiEj4eTUJcKRjEaTxDty7radO7iq_DGDTjxzvPCAJEfTROjXtauQo0c4c5oTGc9UFi5t6WAj-FKqL8DdLanJZgZIPlFjHfXWScTSzlokgpZb67P0UDqPWho_IrcPmPd6RE5oSwIRmNQ9pVcy3QuVLUffXUmUHzCAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5799d9a11a.mp4?token=e8pkT6KKkPWCkkzNUJmUuxCGFPEazZwkNK2b4onOaCNbV7anUyTCw0cmoNa-u2WkWfpXvK_FjMCz1o8NLc0gp1c0ZNjjRTQRvIY65OXg6KLwRgK8Kf2N94fke_NlfqaIBnMGYjM4Y3-OWbfduCf0Rc9-x2v4IQ7gsgVgWsghrf0-1UrableH-KiEj4eTUJcKRjEaTxDty7radO7iq_DGDTjxzvPCAJEfTROjXtauQo0c4c5oTGc9UFi5t6WAj-FKqL8DdLanJZgZIPlFjHfXWScTSzlokgpZb67P0UDqPWho_IrcPmPd6RE5oSwIRmNQ9pVcy3QuVLUffXUmUHzCAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
شوخی خداداد و خیابانی با مجید جلالی و داستان ساعت رولکس معروف قلعه‌نویی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/93904" target="_blank">📅 14:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93903">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99108c1877.mp4?token=Th2xC7A9GULIyQdMT10DyIQR1HNixrdoxnAeTVhCLj8s_R2p8C9FNavKFPknwPKwBawzkX489z-Q8JJHnIIrIhf5wanBV8-mVA5JUvofVzCyEO9b05eUltWi9IgLPqRF_pmxTbJylVQUtsbHWnzD09pDWQ-PSj3iVls7Bs5m5Mrxcih3bNQO0Epe5Hwa_yBGPQb0F9BatoIPVFvuErVflAmnlPkH4qXlPYj5a4Iio-rAHSSnqxmqk-j0HO9VrNwEXNBpCTtDlVkBvbraLgbWsizginpt3_eAejrvLIhnLAw2l_9BY00SrSkN9dTaJiP53yBSg5tqeGn-Kmrfujc_lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99108c1877.mp4?token=Th2xC7A9GULIyQdMT10DyIQR1HNixrdoxnAeTVhCLj8s_R2p8C9FNavKFPknwPKwBawzkX489z-Q8JJHnIIrIhf5wanBV8-mVA5JUvofVzCyEO9b05eUltWi9IgLPqRF_pmxTbJylVQUtsbHWnzD09pDWQ-PSj3iVls7Bs5m5Mrxcih3bNQO0Epe5Hwa_yBGPQb0F9BatoIPVFvuErVflAmnlPkH4qXlPYj5a4Iio-rAHSSnqxmqk-j0HO9VrNwEXNBpCTtDlVkBvbraLgbWsizginpt3_eAejrvLIhnLAw2l_9BY00SrSkN9dTaJiP53yBSg5tqeGn-Kmrfujc_lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
تاکید مجید جلالی روی موضوع بهتر بودن قلعه‌نویی از ژوزه‌مورینیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/93903" target="_blank">📅 14:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93902">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba9c2b70c.mp4?token=jNJajgSFoy18XnUz8lE9PqbLOayh6GkLZeYWhgTfVBOz1K1jyI_z6XTiHyliBqf0Tv2OrFVr1PrO2nImG5kfvO1h_gr94q2MVRM4sBBW4QlbrldcoqPN3BLGSBL6Hc8-5Yaign05JCNvxJ63TJTo5diEW_vXQqEoywGaqeI6uZpwJZjvWfRusHCjBqTKrNlqy7BRbbfDKcucIUzMfoykVJsbgEFC4YuCdHrc4ZeExQ5WPT1nVmEPSMZj6uKPL-MwJ5z-gRVyAtUP8GofmGjeXKVpu5xt5JtNVbseCXsuGlaWMUTHOGbqWHmmf09rKEQ1SfLh8-uHrE6NDDYm7g50jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba9c2b70c.mp4?token=jNJajgSFoy18XnUz8lE9PqbLOayh6GkLZeYWhgTfVBOz1K1jyI_z6XTiHyliBqf0Tv2OrFVr1PrO2nImG5kfvO1h_gr94q2MVRM4sBBW4QlbrldcoqPN3BLGSBL6Hc8-5Yaign05JCNvxJ63TJTo5diEW_vXQqEoywGaqeI6uZpwJZjvWfRusHCjBqTKrNlqy7BRbbfDKcucIUzMfoykVJsbgEFC4YuCdHrc4ZeExQ5WPT1nVmEPSMZj6uKPL-MwJ5z-gRVyAtUP8GofmGjeXKVpu5xt5JtNVbseCXsuGlaWMUTHOGbqWHmmf09rKEQ1SfLh8-uHrE6NDDYm7g50jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇧🇩
شادی پشم‌ریزون مردم بنگلادش از گلزنی و درخشش فوق‌العاده لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/93902" target="_blank">📅 14:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93901">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5wekczXM-Xt00jEceOvfbhaNovJGW7tuzbGR2hgmpod8Dug0styBmPa9DcfnnCRm-9y-Gnj2UmeC9r-Vr0hniIeI_tbDoLkb08CiQY0e2RMKdVvGCkjiHQ1AtzOJX_-qkMbO5GdarnNwIcIBQX9470lR2FdTjWMPHm7YbNcoDsNCPMS0gINhwlfMh7mPJ9KGIsU0pVYrz9MuXwuf-IkcpoHapJ800p5GjWTAn_Kzl-fNyzHz0uIqCCM58p_XsoSVT9z94Z41dTtFJciMNhJTnrjzXieKk5nMjuyUwiMcr34ro0N5iRhypmRdN7U2v-zx_2ojdVjMQtZ5cj4-ddYAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
؛ رئال‌مادرید طی ساعات آینده اولین پیشنهاد خودشو برای جذب باستونی به اینتر ارائه میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/93901" target="_blank">📅 14:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93900">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFCSHVv356643x5rA-uBN_pQ_nDIdS8eaCP1h2e4SbmLFQOFBjrpBAGKexjaNdVLDe6FAqC5OLIbIGzPKZQGO3w86MQnDYEj6yW4dc_lkFOPFsVlLtHbMR-HK86zjf0YV8YGrux5bMNjAmyHMngc-wrhd7nWnR6Bgm8HQAXRXbR3qyuAiuch7Vo09Tp7yQT-qLvyZU6wHPqm6vLwqkDVCTrNT6m8pZpyW3JSjeKXpF1FeZ-Q004fSuMulhpuVTLKsNWEQX18FMx2ZfuSFkA0QnK9TT8tw9WiipAJAr-IoGwkd19k2LFKHd0FghHTkxPu3ZeTVLg_XEeVf90_k4YUvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اگه کریستیانو رونالدو امشب گل بزنه، به اولین بازیکن تاریخ جام جهانی تبدیل میشه که در ۶ دوره مختلف این رقابت‌ها گلزنی کرده.
🇵🇹
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/93900" target="_blank">📅 13:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93899">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7feb575370.mp4?token=TTlofqKQ3bJo1xY_4Bst2DSJ35cyJDejdqqDiqh2zl1WgvseePLclulEJlEalB-1ppHulXcD3PBaotwCHrQZPHVlU6gtBA5KYE-6RyfvNMSgrdRpm9UjD1cu8V3YZ27b-JWwaxNc5lFwgL1OtEpIkqoSvP4UrQipA2F96jZSj3mFPyuarsZPCceu-w-Y5mDrspSRfSExnDuUtxhEoboR3jDE28JIDsRQM5A54f1jGmKT8gbr1YLTVaZ98fO0XJZM9b2bRqa1SfpIsFZ3LKZZ9QxaKbeg_5VgQ18aJUfmdZYjC44qHmqvFDp8RXjNLgoO8f2GfAUk63-irsFvyrQOgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7feb575370.mp4?token=TTlofqKQ3bJo1xY_4Bst2DSJ35cyJDejdqqDiqh2zl1WgvseePLclulEJlEalB-1ppHulXcD3PBaotwCHrQZPHVlU6gtBA5KYE-6RyfvNMSgrdRpm9UjD1cu8V3YZ27b-JWwaxNc5lFwgL1OtEpIkqoSvP4UrQipA2F96jZSj3mFPyuarsZPCceu-w-Y5mDrspSRfSExnDuUtxhEoboR3jDE28JIDsRQM5A54f1jGmKT8gbr1YLTVaZ98fO0XJZM9b2bRqa1SfpIsFZ3LKZZ9QxaKbeg_5VgQ18aJUfmdZYjC44qHmqvFDp8RXjNLgoO8f2GfAUk63-irsFvyrQOgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت تیم‌منتخب ایران در جام‌جهانی ۲۰۹۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/93899" target="_blank">📅 13:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93898">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuWRs_QRwIQom2nvSzUql2RUXspfVT2i1hmBdD2kPY6MIYxPhmTOMhb34-fqjaAasSmp67nD5zU0wwMl2ZADElyUgOsEEom-7E8GtuCGAuktTwAGgEa9D84OaWI9uqgyGNNJgOX1TkvHX2fb9CLquLddl563LVQgOUBgmXzm1YsxR2phWsh4NpgU_klcKi_v0I96nZSRnkfCuYNW61sJxEw2k78Y9-Flnwq9C1oasGRi2NVzoAH4DJWkMrmjfKFYeZ3VAscan91mJjSwaBJbovQpIeLIMSzpSNskugtJkkS84Jlxe5H8_pz9qnVvh52bv3Kx1Ffa9ZJA1Qhwwb3JPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید بانو وندا با کیت آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/93898" target="_blank">📅 13:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93897">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONKUjGJI7IXBoTWeYs8hzH_YxEdWEVwUlxNvX6oD9nV31w6vFSqYh-fSJL07Lb1i_vKLPPXd6cBsFt-tJnz8SBfz3gSillRpxa5bEOvtmBEGYKzoMtiCssa7TdHoMUmTo9Uz69kw_eeagJu46zs3Mbr1LdbqoxRQSZS0YRF2QIxPvFQmgDV9qrsHwxFuWmVbOvBSbhSOyOrkWzVeWbxsp7Y42aWouxMRBjSeV9ruElFARPidwWswOPO1RQyslKhKjtiw3pv7UNA3OEb4P4gdZsaSSxKYn2axKGqGcignz-kDVwb4TcRP6_uhPNSo8X3jgc5PSpxxTbB9yBQaMPGR6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🇪🇸
رئیس اتلتیکومادرید: به‌نظرم فصل بعدی خولیان آلوارز بازیکن تیم ما خواهد ماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/93897" target="_blank">📅 13:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93896">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18bb140549.mp4?token=KxTgLi2K8BwAUwJfQ4tRDPhaG4ThJR8C40blvw4KrLpsuuxzM2LwPbCR-aVQTuuRfuXO_qd7XtmCGYIrEHynpre6E6WMmnNEPJauU-7bktNm9RkpD1XEVCaZ_1Q-xe6EZ0kJuLjDTn1A2ik71lTSpdPrOPVlEXKOm7NyiqoQ5Defwh7OJvRKYovEMjWdZTec5DN0LMZC4KrgjAdADmzDvEkNVAyzc-xRtl4EnpqKGUA-JuEFd_ijjqVmGnAIaQ0KMk1IVSm4IMh7PppT8hKtOu4mHb21eFcIbDue1prDTq0GKs6iNECNi1gfEnfgze78950ucJ6q_gk-gQC6ZA3FDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18bb140549.mp4?token=KxTgLi2K8BwAUwJfQ4tRDPhaG4ThJR8C40blvw4KrLpsuuxzM2LwPbCR-aVQTuuRfuXO_qd7XtmCGYIrEHynpre6E6WMmnNEPJauU-7bktNm9RkpD1XEVCaZ_1Q-xe6EZ0kJuLjDTn1A2ik71lTSpdPrOPVlEXKOm7NyiqoQ5Defwh7OJvRKYovEMjWdZTec5DN0LMZC4KrgjAdADmzDvEkNVAyzc-xRtl4EnpqKGUA-JuEFd_ijjqVmGnAIaQ0KMk1IVSm4IMh7PppT8hKtOu4mHb21eFcIbDue1prDTq0GKs6iNECNi1gfEnfgze78950ucJ6q_gk-gQC6ZA3FDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
بدل رونالدو:
این‌طوری نیست که من بدل رونالدو باشم چون اون خودشو شبیه من کرده نه من شبیه اون؛ رونالدو صد تا عمل جراحی کرده ولی من نچرالم
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/93896" target="_blank">📅 13:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93895">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51823a43bc.mp4?token=qYlYmANOOO3SMN1P9H7FtD4EPQ_FXXvmFbyXv2YlPOKm5QnYawNi82gpA1lZVxUHXbzGhv5hYbvBUEx6Wdnh-JV4aoEPSYn-iZADCNPoEOEjjpicJbtWkah8VeFrQGq71Uv4x9NSbX9ZFXL9YrSiZMUG0mn1QQRNovIGz2Wa1WANs4TgG1Yp_U3PDCwYH395eXM3VI1R4dsCZ_CPJOZ08Aopm-5zZ-a-SK9rXFJw7l8w3tNXTztoMV45yD-bVSXBOVDA0CocJhKUZwA9mtIPLzTyVhwbZgMDK8nzUI4FM016G1BIhRcJC_lFXmEcJVDsgL8csDFy9FPKry2A5TlN-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51823a43bc.mp4?token=qYlYmANOOO3SMN1P9H7FtD4EPQ_FXXvmFbyXv2YlPOKm5QnYawNi82gpA1lZVxUHXbzGhv5hYbvBUEx6Wdnh-JV4aoEPSYn-iZADCNPoEOEjjpicJbtWkah8VeFrQGq71Uv4x9NSbX9ZFXL9YrSiZMUG0mn1QQRNovIGz2Wa1WANs4TgG1Yp_U3PDCwYH395eXM3VI1R4dsCZ_CPJOZ08Aopm-5zZ-a-SK9rXFJw7l8w3tNXTztoMV45yD-bVSXBOVDA0CocJhKUZwA9mtIPLzTyVhwbZgMDK8nzUI4FM016G1BIhRcJC_lFXmEcJVDsgL8csDFy9FPKry2A5TlN-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاوره اخذ مدارک دانشگاه آزاد
واحدهای معتبر تهران
کارشناسی، کارشناسی ارشد، دکترا
با استعلام
💥
(
بدون پیش پرداخت
)
💥
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
Telegram :
👇
👇
👇
👇
@irantahsilat_iau
Instagram :
👇
👇
👇
👇
Https://instagram.com/uni.irantahsilat
جهت ارتباط با ادمین
👇
:
@madrakuni</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/93895" target="_blank">📅 13:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93894">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🏆
🇪🇬
ویدیو وایرال‌شده زیبا از مربی مصر درحال توزیع آب میان هواداران داخل استادیوم. بنده خدا از آذوقه بازیکنا به تماشاگرا داد تا گرما زده نشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/93894" target="_blank">📅 13:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93893">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51ab3ff261.mp4?token=NB_xpiNt--r7D500pCApEVyYD1ykI3sCDtgeIq2a4DiAMgL_TyD2hiUNc53igwBqz3V1aYumh2lCHJlfeClINQRO5T0Hcg2vVFV-cpi6kH9JKy0NieE-mpwL89usedLHedmalWDt919vsRDzbp_i5Uv62U50SGzNe__mA1-LbYX8BpYBB-8h7SE1dxGULHH3zFJW7rAxGJUowAwYJ3O0RlvIJb6SJ2no2laJ0FGPf2oie6LGAkOyGqt83Alswow6rZO-2qXisdUL5LxaPEPyQIBID6ojMepP-fJuy7DzNQZL0nzpXDBqmlie_lXmKMFl2ToYEB3C1hWLaNjxj1AZRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51ab3ff261.mp4?token=NB_xpiNt--r7D500pCApEVyYD1ykI3sCDtgeIq2a4DiAMgL_TyD2hiUNc53igwBqz3V1aYumh2lCHJlfeClINQRO5T0Hcg2vVFV-cpi6kH9JKy0NieE-mpwL89usedLHedmalWDt919vsRDzbp_i5Uv62U50SGzNe__mA1-LbYX8BpYBB-8h7SE1dxGULHH3zFJW7rAxGJUowAwYJ3O0RlvIJb6SJ2no2laJ0FGPf2oie6LGAkOyGqt83Alswow6rZO-2qXisdUL5LxaPEPyQIBID6ojMepP-fJuy7DzNQZL0nzpXDBqmlie_lXmKMFl2ToYEB3C1hWLaNjxj1AZRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
نظر دین‌هویسن ستاره رئال‌مادرید درباره کورتوا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/93893" target="_blank">📅 13:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93892">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e6f682474.mp4?token=H3asiiEwNVdj8jE7loVTLuZ2_7EBdRNS7pYOxwXB2XvjLZPxhyACCAPUoVAayPl0G5PM5kmU0_ZoXFXX60873HVb-WTyGwtC_eG5sL5w5L5raMWVBKRteW4tyQePbO6_Tc3VyfbpBR8Iz3NMbLEMEK2lHj8AD200-DmFK81RziY5v23Yh9TPhADwPE26bIMMRpiwGVtKD2fDGES9dPJa8EtKKFAIOid7OoSANWFWYcwbzxjc3WlG6mrsCZ85_uayaoFFH318w02C6omORTS7qbcoznXY26DA0gW7KOndgoZqEBEXqr_LNi-0rYon7SDFmUpLgzBngaDI_dhcjNlEqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e6f682474.mp4?token=H3asiiEwNVdj8jE7loVTLuZ2_7EBdRNS7pYOxwXB2XvjLZPxhyACCAPUoVAayPl0G5PM5kmU0_ZoXFXX60873HVb-WTyGwtC_eG5sL5w5L5raMWVBKRteW4tyQePbO6_Tc3VyfbpBR8Iz3NMbLEMEK2lHj8AD200-DmFK81RziY5v23Yh9TPhADwPE26bIMMRpiwGVtKD2fDGES9dPJa8EtKKFAIOid7OoSANWFWYcwbzxjc3WlG6mrsCZ85_uayaoFFH318w02C6omORTS7qbcoznXY26DA0gW7KOndgoZqEBEXqr_LNi-0rYon7SDFmUpLgzBngaDI_dhcjNlEqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
😂
صحبت‌های یه خانوم اصفهانی درباره بیرانوند:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/93892" target="_blank">📅 12:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93891">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/93891" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/93891" target="_blank">📅 12:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93890">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFV1emPqj_TJY4FCyCsYHP2oHoNyK3-Wt7z0S61v8-_12KB_I1A1jmrxtEK4XWgQnqny7mrQFEoB302OQPwC7fqahTfMUXKbftyvUq_u_t9fx6lSGzi0IEal0jxb2fzNiWBnnX6ZzSrWJdBXoympchKim-P7o9PbmEFzZoqwQSHPi1P0RP6WxSg9rU34gbFwXTQl3uwXEcrAKsP2svl9F65SxCW9hrmWyexvJ1EglQHLeUBaxflGkDn3IueKold8TJRyX8D6adFvYy4Zd09BOx2RtCJo5uC9MNnhhnj6wf16IjIV48N-UAjVTLMhCFH0C-jckGsWL3TlH9qSHapl8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/93890" target="_blank">📅 12:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93889">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlpHXXPOwUcnWnbuE1vrZt5ZXr0GlaBs24aAZcotAbblzvXVxT18xX9nPB7R3-cgnR2RwT8cJLUnt5HgK7bQbmZ0Mt_UjPh7k7UFhhGbDPQIAoQwg0r2ZhoY8_PpAR_8hKdbjhMpHg-sBgJXmTKqQmUEUHXBSimNdFluPeu4tyYx7HgDkvm21r0luFYfXLzUO1AcobbilpULKZeiR_G5CM38DOkIVdqSKFOa4AVbbGhz7Xh7iB0Pl3m9GyTt2o-NZgA4SaKBv6iQqe_87mWhW2vcXx0SQhoUAk2UhcIPBv5Ed1e9PIOiJ1i3oueMN7-v1IDFuchhtxcwE7MoxLcLIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇦🇷
تمامی گلهای بین المللی لیونل مسی با آرژانتین تاکنون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/93889" target="_blank">📅 12:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93888">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33232f8760.mp4?token=GrpoKfmgvm8RtVMUl2uYgPQOOiiQwTr6pkGm4vKUt5r34YPFTmyhevY8pPcSkOhh4QZH70NpwuoUpasEVAFuYxRXKX3vcrhVuKfs9RR9eBi7zaXOmWsx_J37K7HBiryh0JXyx7lmQkUWmyDzDIgBMknZwa6DvJ1Xdko0NT4-EJS47lYhaznqE3xAyuN4uUdrDyAqc7LsKsOkYzT2HVB-inGhOlVUQqQu4f0c-M4MuSHo9uccqpujqUuWl_-e3ni9k1rVEkpvokNK5VZdt5Qdc6FRFR2-gXELSD8TXesRG6mC3LgUKxn8t4Sb_WenBEslTFwLYsABnZhdKN5wARwdzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33232f8760.mp4?token=GrpoKfmgvm8RtVMUl2uYgPQOOiiQwTr6pkGm4vKUt5r34YPFTmyhevY8pPcSkOhh4QZH70NpwuoUpasEVAFuYxRXKX3vcrhVuKfs9RR9eBi7zaXOmWsx_J37K7HBiryh0JXyx7lmQkUWmyDzDIgBMknZwa6DvJ1Xdko0NT4-EJS47lYhaznqE3xAyuN4uUdrDyAqc7LsKsOkYzT2HVB-inGhOlVUQqQu4f0c-M4MuSHo9uccqpujqUuWl_-e3ni9k1rVEkpvokNK5VZdt5Qdc6FRFR2-gXELSD8TXesRG6mC3LgUKxn8t4Sb_WenBEslTFwLYsABnZhdKN5wARwdzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
▶️
عملکرد تماشایی گلر کیپ‌ورد مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/93888" target="_blank">📅 12:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93887">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjQcEbQuEk9XBG9aroYRtR7EXHYkOb0Y8ai7b0LBb5REPku6R5_xBIAimLZAoxh3KNHVGSPKV8shl2vXMzLAymXQdG8zS1XyRf_xZo_pz2peDCVikUZlKCs-DheFpSLIMttzvH8bwouBNXYSkk35XgdyNWiKk1TOBdG887sVXv7UBWJnOR-owGggFeCv2GvNFwwn8nB5s2e8vwaaHF_EqpwV6L2HrJ9JS1vSM9z7ogGbGHnsYvHD-a3KRXUe9S2RVeB9lVGl7-12Y1UbSxpmXpDq4HnqR6BepyjciVC_kVUzVEM8cQ81GwXI9kZof-04W-CutDsOZ-wKM6pD9yXYNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
برناردو سیلوا رسما تا سال 2028 به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/93887" target="_blank">📅 12:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93886">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e52fd3bd1e.mp4?token=ezV1sK9du2MLep9mThgnmoG3Gau-sKw6OmJ01RfyLOp4rho6QXU4olBqhm-eUD5OkdaYH7XHru5XsdJkLjmmXWod4-elElwnZ-rCNwKCF4X1tULJMOpjFVWAu9PG5aeTI71GlWvJQwMWGmdOMlzDtjZGB8L9LjTjfb0KnPxjsAEjbnjtRouHp4hCl4l7r-8C7g_0DK1V7T_JlilwQww_-LM29TGUAxDFa9OGQC2XpgNOS7Uui81uSw8QeGodOi7SVvt1bp4L79XXIBdoBnfvz8Mas27IjgXasDML9vJk38LRin_YsmHjAZVoJnmlOVx1aF5eoGYAulMQ4iH63rrqYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e52fd3bd1e.mp4?token=ezV1sK9du2MLep9mThgnmoG3Gau-sKw6OmJ01RfyLOp4rho6QXU4olBqhm-eUD5OkdaYH7XHru5XsdJkLjmmXWod4-elElwnZ-rCNwKCF4X1tULJMOpjFVWAu9PG5aeTI71GlWvJQwMWGmdOMlzDtjZGB8L9LjTjfb0KnPxjsAEjbnjtRouHp4hCl4l7r-8C7g_0DK1V7T_JlilwQww_-LM29TGUAxDFa9OGQC2XpgNOS7Uui81uSw8QeGodOi7SVvt1bp4L79XXIBdoBnfvz8Mas27IjgXasDML9vJk38LRin_YsmHjAZVoJnmlOVx1aF5eoGYAulMQ4iH63rrqYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های امیرعلی اکبری راجب هالک ایرانی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/93886" target="_blank">📅 12:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93885">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc16e86e4b.mp4?token=ibDPSwLpOxGBo18FD9cDNnaf0K9HQOfUF7bx13iJH7_NjXjTmvfclT5ueAqTe7Ow3aFBZY-TyucRSdXz1Emkkan3SvOIQjsWFaXhVMJVCxQVa3qS63RDEEJ9tM7PGRiWrUZDdNbguiYYlLnIqkiqJtPPiDOuMrQcLBck0brtzRetIOasMSWXyszTO8VIiuNrJh1huLouFj3LRxbsMBBIJEqxP1_xnizkOpUeO5haOf7AhjjJQfgwwvtm2RQ7C8dgjxx4SMkk7MFP37To-XkrJYhVfxfHCIxa8-oYf2MLZpUnCJhdzcUN89ZrU2sIjg6cix3hVNI6o8XA453L_Vk0oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc16e86e4b.mp4?token=ibDPSwLpOxGBo18FD9cDNnaf0K9HQOfUF7bx13iJH7_NjXjTmvfclT5ueAqTe7Ow3aFBZY-TyucRSdXz1Emkkan3SvOIQjsWFaXhVMJVCxQVa3qS63RDEEJ9tM7PGRiWrUZDdNbguiYYlLnIqkiqJtPPiDOuMrQcLBck0brtzRetIOasMSWXyszTO8VIiuNrJh1huLouFj3LRxbsMBBIJEqxP1_xnizkOpUeO5haOf7AhjjJQfgwwvtm2RQ7C8dgjxx4SMkk7MFP37To-XkrJYhVfxfHCIxa8-oYf2MLZpUnCJhdzcUN89ZrU2sIjg6cix3hVNI6o8XA453L_Vk0oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👀
🇲🇽
خانومای‌مکزیکی این‌روزها حسابی دارن پسرای خوشکل اروپا رو کف آمریکای شمالی ترور میکنن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/93885" target="_blank">📅 12:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93884">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a17b1db4.mp4?token=dQ6q20xqss-B1DfGeRf6eS7Ie3MF1LWWrHGe666EORCqy0T51grC2louyOvBsW9PGRxdyOHjnV6f657D8BaxZD1AQ2guaz_2WKFevFfegqUTAiMlv2J2WxOvce_twdbJPmw8h_7qZCluurxTZ15GiCRyoM0KFF8LEW8InmXjTCFBepRP6LlsaXbOIklvUuTtS-PVnGVwfxSdhGpvy8FDFrD8aU9pnRSfLasKwAPqNzwu93MIXx4KDASZdsc6i5D7ttscWqiGQZ-nSDMfpSKEmzSfwszGKEB4G1sSMOxOJvaoqm1s-ceV-v1nLNGhsfgzvcUnEKywqRRypnlx3uGOfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a17b1db4.mp4?token=dQ6q20xqss-B1DfGeRf6eS7Ie3MF1LWWrHGe666EORCqy0T51grC2louyOvBsW9PGRxdyOHjnV6f657D8BaxZD1AQ2guaz_2WKFevFfegqUTAiMlv2J2WxOvce_twdbJPmw8h_7qZCluurxTZ15GiCRyoM0KFF8LEW8InmXjTCFBepRP6LlsaXbOIklvUuTtS-PVnGVwfxSdhGpvy8FDFrD8aU9pnRSfLasKwAPqNzwu93MIXx4KDASZdsc6i5D7ttscWqiGQZ-nSDMfpSKEmzSfwszGKEB4G1sSMOxOJvaoqm1s-ceV-v1nLNGhsfgzvcUnEKywqRRypnlx3uGOfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خواهشا تو عالم مستی فوتبال نبینید. خارش گاییده شد بنده‌خدا
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/93884" target="_blank">📅 11:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93883">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd5190b2e1.mp4?token=PJmBUcRS8GERN5a1dLqtia85FbzBJ3xvJUA7MrzKXACReIuC3OX3tPF6G8YiIhlm3pxbhRMKbNgBan_ebRNKdLQdHSPQSExDm88LvlsZeVmDuqtwf2RK5JIFKXwwLPyPk8pfBc68NPa8nY6mLmON0fBCfX14HN-2hGeor2QZV-QKlWRwTgoG7TefSXVQsc_ay-rx0IKyndeVUkZ57PiGJd5r-5OLvFmyTTF7pJMBcyPcokIPGcHiGtB1NqTBXi0es_vDcB7OR7lb7A0vNMfspSgdgojOJJDCyR_uUZqwKFqikPCgbLAFC9r8KohiLVptPfzKBlISJXWBg1X2a_aVAEn3S6HIdmLt5aRXW_G1av5g5Buf9dqzcJls6bULOOZNqWxSUbVzccDt9727TXwl3hBmTV076tpdYax8irTRV0prhEat3WwJ3Kx1dUvBPhMqUYlwDAz8OXsf6y8Rx40CjCltBsyGu6HM_st9JF03rh87O1tmLUg7Y7xX6NCPfNbuRwf6FZ3WTb2-CkNnaAuppqko0NBTQeSgRlcPpeWZyi0QVFQlFwyYAMcsAZIr0GomXvSrk5DcdHAW3i3xEU8iHn_1u38mzxqGNCmSiGQEhJSa7C5cHSP_lS0n3GjRULAj9IrM5OvgBQs4Om1expXXhQKEnYblEaIX0Tq36eQmadY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd5190b2e1.mp4?token=PJmBUcRS8GERN5a1dLqtia85FbzBJ3xvJUA7MrzKXACReIuC3OX3tPF6G8YiIhlm3pxbhRMKbNgBan_ebRNKdLQdHSPQSExDm88LvlsZeVmDuqtwf2RK5JIFKXwwLPyPk8pfBc68NPa8nY6mLmON0fBCfX14HN-2hGeor2QZV-QKlWRwTgoG7TefSXVQsc_ay-rx0IKyndeVUkZ57PiGJd5r-5OLvFmyTTF7pJMBcyPcokIPGcHiGtB1NqTBXi0es_vDcB7OR7lb7A0vNMfspSgdgojOJJDCyR_uUZqwKFqikPCgbLAFC9r8KohiLVptPfzKBlISJXWBg1X2a_aVAEn3S6HIdmLt5aRXW_G1av5g5Buf9dqzcJls6bULOOZNqWxSUbVzccDt9727TXwl3hBmTV076tpdYax8irTRV0prhEat3WwJ3Kx1dUvBPhMqUYlwDAz8OXsf6y8Rx40CjCltBsyGu6HM_st9JF03rh87O1tmLUg7Y7xX6NCPfNbuRwf6FZ3WTb2-CkNnaAuppqko0NBTQeSgRlcPpeWZyi0QVFQlFwyYAMcsAZIr0GomXvSrk5DcdHAW3i3xEU8iHn_1u38mzxqGNCmSiGQEhJSa7C5cHSP_lS0n3GjRULAj9IrM5OvgBQs4Om1expXXhQKEnYblEaIX0Tq36eQmadY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇸🇦
هوادارای ایران و عربستان کف لس‌آنجلس داداشی شدن و عشق و حال راه انداختن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/93883" target="_blank">📅 11:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93882">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzegrH4CZQEPQ5zhxvFycV6mVKneclItaUYwVqG76r155Tc7ryMgVOwkKJCU6LRYVHLzDtQdizWQr7neRhLPnNGVYs4kPhdnDeN-LFB85-kULDma416dzDGUMGNfEQzjcUmjnKVjk-PKWJ8Kfv4-uf_BIQl27n9PKVHP_wGCraZ4fE2GhoN6RB4GlckB6OTXUoZBvMCaq-g6c1DUzMLxg6v5Sc2fsEfCe5aMQx_dzyV1z52NRtL05SCAvRYDgrMz2nU3034j7dT6fNf3QyyLVSwkqkPQtUE6UwUYx8Jxe6ZwyG7zWdPjAy1BNwtlrbbDqXLcUUXGrO2hHN6pw62mOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر جنجالی رسانه‌های اسپانیایی از کص‌ خنده‌های یامال و زیدش بعد ریدمان جلو کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/93882" target="_blank">📅 11:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93881">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INAES9rE8YCDbG0FIJhYUoIwPvoEzmBBlxiYVNWzzGamXPDGsj0dKd34QcnOPSIap9I5Ck2XaD23IIBPh13Rz4osiWYE8QgdmNs9fa6mvr9Zlq2nvj3AiL36AUVxr-2ThSfHEX4GAa0Tp64UkAtqJY44xOQWkeLz67NtkZfCJO-zJRVg4APrBcT-BxIljX062xs8Upgw4VNtKsxbiJhiIWppZ4ecHgh6rIQLFxhwmNwrArBIxsWSOwGbomBmxkOOe-_ex_2JvxBWxFZfssurvfBDjoacwQbE9jruhCDU9HrsiHr-1J84iY_SnbBRA_jxI8B0H54uIMD_fuvMljiyIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
لیونل مسی:
دیگه چیزی بیشتر از این نمیتونم از خدا بخوام، اون خیلی بیشتر از چیزی که تصور میکردم بهم داده. الان فقط میخوام از فوتبال لذت ببرم. خوشحالم که منو یکی از بهترینای تاریخ فوتبال میدونن و بابت این همه محبت و احترام قدردانم.
🩵
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/93881" target="_blank">📅 10:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93880">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12875b1bbf.mp4?token=Jp0tBxzFWjaL4QyAvRas7Q7p-msI39l2MwLecHZiPD-XLLVUK8u2PGeK4dJpoPOa2DkOzn_FqleXZoY7VLrS8CCiYIBUYoomt_V_1Mcyen4OHk-Lq3clx-fe1uWwQH7IQs34nQWcPCM3VC8BXMlVWf6Pxe111ONwqpyCHf_F9aEFXn6O5HSOVXV4y5zRadM8S2Wcqvza4HElptrXHpQDVxej3XzlF3W9_X_bdeU-LGz0Xh8t03B9yH2Q1emc0lA9jdgKftzLhJYVIPUUEc7utVIKwzfqv4bDWP6zDBU6HlQvE6-7MWZaJxi5_Ef1hU55dbsJ4Pnc4VVj0vdzcZ1HvoNaVzOhQtS31fxV30valIjktVMOBKwe-YMCBlDk6P6VvKfOPSi4tG0VSZg94KmvRVXeAYf3XlxBjqLpFYxVl8Isy7WywUGd0U3PQ2Zfy9pbdTAMz0RAlwcNDUIcvwkEGlxzCU7aTCxd4Gt4BrPQ1BAJVdYGA9bJBSNCNjEGhWlb-TUkpTDyxquLB3vAeGRkYC9RfLKmMe-X_eGKI08EZMKVqQQSu4zW5GDqBCn7cIIHVXs3e5vgT2QltwcNhW9etTie4uIMRmiOzEuUsdvYHb2GTgwaEkV9EU8bEBieUJXObXlKyIdGWgfKwpua9t6Ut0AwAeqhQzwSx3SuYinHIvY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12875b1bbf.mp4?token=Jp0tBxzFWjaL4QyAvRas7Q7p-msI39l2MwLecHZiPD-XLLVUK8u2PGeK4dJpoPOa2DkOzn_FqleXZoY7VLrS8CCiYIBUYoomt_V_1Mcyen4OHk-Lq3clx-fe1uWwQH7IQs34nQWcPCM3VC8BXMlVWf6Pxe111ONwqpyCHf_F9aEFXn6O5HSOVXV4y5zRadM8S2Wcqvza4HElptrXHpQDVxej3XzlF3W9_X_bdeU-LGz0Xh8t03B9yH2Q1emc0lA9jdgKftzLhJYVIPUUEc7utVIKwzfqv4bDWP6zDBU6HlQvE6-7MWZaJxi5_Ef1hU55dbsJ4Pnc4VVj0vdzcZ1HvoNaVzOhQtS31fxV30valIjktVMOBKwe-YMCBlDk6P6VvKfOPSi4tG0VSZg94KmvRVXeAYf3XlxBjqLpFYxVl8Isy7WywUGd0U3PQ2Zfy9pbdTAMz0RAlwcNDUIcvwkEGlxzCU7aTCxd4Gt4BrPQ1BAJVdYGA9bJBSNCNjEGhWlb-TUkpTDyxquLB3vAeGRkYC9RfLKmMe-X_eGKI08EZMKVqQQSu4zW5GDqBCn7cIIHVXs3e5vgT2QltwcNhW9etTie4uIMRmiOzEuUsdvYHb2GTgwaEkV9EU8bEBieUJXObXlKyIdGWgfKwpua9t6Ut0AwAeqhQzwSx3SuYinHIvY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🚨
‼️
بخشی از درگیری شدید ایرانیان در سکوهای استادیوم سوفای لس‌آنجلس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/93880" target="_blank">📅 10:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93879">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaFFmBREUfV8PKycW-P8iJ56DKG4tOeW2sIQcjIeo-IBniz9flYzOBQQjTC8cJks2RuiNarOr-T5XCzsWCvcEkuokSyayJXvjqN40fYC_D6F6hxEdipi9uApduzYZtmoNQ2DBzm6oUibaU7edZdK4wCOoH9gxgwPZppwTAHOqfkxL-t5QGn6rwlW26VIPRHffX5o40zpDbkq0E1mIIZNAtGbKiiMcCwBA70ERAvs8NX0k8Vkd64nBv6yP2UnuC5Fj5bGS8aHGuzdRphdhMP7tu-4yxkiclRJXPbcmlcUOYgtccVUZNikAq9xQu8RI4zeVv0eVKe3wHdzBO56Hqmo3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
آرژانتین در 7 بازی اخیرش مقابل تیمهای آفریقایی در جام جهانی برنده شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/93879" target="_blank">📅 10:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93878">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyaguQ6njFQxKXhZ0Bd1BJ5zUTQvaSeQtwWfFZ9B0-QpF2xbkrR_l9LCMUm4bbYD3amoNfO8i-crBD2xamoT7svA1eu22T3j6nNLa3dfyPO85Rs0B9sbO8JMhQ7PGBDsrfHCUckkosJmn-c1K0QaMbWYTSgcbABp-Kx39Ae2s0ni9a46zNwtC0BI3vb0AaAEYgftGC4hwxOakW7dPKLoHG56KQrLH7177PE1UPTa_OyFm5TxAls7iIu1VGkxwKaWVqodudFGS12WEvQyiWCG4ogkF30pzhGiheF39zFz9ujNWpyDPbGpqq-_n3GA99nITd9BPyNSksQjubd1hx6EqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🔥
🏆
زوج‌ایرانی جذاب در محل بازی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/93878" target="_blank">📅 10:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93877">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bf4a59c61.mp4?token=nCmqg4gwDJ0mTlxHJFQFFyNve_s5qoO058AUcKQHX_pASv8FD5G1GX-kLkAyN3nIub66ZhNLpNfS10KPp08JINDAh4SRf5D8k94ve7kmgqZAP1T5fCI0pNhzHAxZoKSGinMxG1JQ6jxT0jtci6MXRwtkP17z7pVErjQSDvCmBdyTu5WoIFr_viJlRZ1upOIvqzj-ZdWD-YjS3MOGcGPffVovWuwZFUvOzlAeCuTXV636HyBroinH07osLGaizz0LTEtoAZ7EIRkJS0CRIv6e4CzKZMnKLo8NK801qhEroJGCflHoawZ1j2SdqrRmWWDhheyUg0Ielci3xntaVc_Q6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bf4a59c61.mp4?token=nCmqg4gwDJ0mTlxHJFQFFyNve_s5qoO058AUcKQHX_pASv8FD5G1GX-kLkAyN3nIub66ZhNLpNfS10KPp08JINDAh4SRf5D8k94ve7kmgqZAP1T5fCI0pNhzHAxZoKSGinMxG1JQ6jxT0jtci6MXRwtkP17z7pVErjQSDvCmBdyTu5WoIFr_viJlRZ1upOIvqzj-ZdWD-YjS3MOGcGPffVovWuwZFUvOzlAeCuTXV636HyBroinH07osLGaizz0LTEtoAZ7EIRkJS0CRIv6e4CzKZMnKLo8NK801qhEroJGCflHoawZ1j2SdqrRmWWDhheyUg0Ielci3xntaVc_Q6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
تنگه گشاد شد دیگه چه صیغه‌ایه؟
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/93877" target="_blank">📅 10:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93876">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUtFZY2KfAHmUJDFv8sebVMmRXZ3jkTYUjKCA8ILWR2yaS0YQUE7nSL6taaWW02ZVetmVTnCeJJcz8CrxxK76vF0CPirzj25xv4bfpVhR5Qeo11MyEZbRLez6JlU1Uk5DN0P5i-M5mv3ZkbMiikDehWnZJVCxtMx6MIm3PnurrxAI4QfMLLeJNqir6QkY9dlaGY_9AEQqB0MVqemNLLY9Gmw3gfcRtw6vcrbRXPjJk5NbhaTCq3C_AXOO_0xCWCVMY9MVLSleBxtLfI9Hce_R_otfbSS6YsqpyS020srJ3i6L8Vi-MoSVybyD0nHYei1vGN3e6xd-lGQBJir7PAI7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه J جام‌جهانی پس از پایان هفته اول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/93876" target="_blank">📅 09:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93875">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc3df4ad3.mp4?token=op0m6FBIqCz95vNIEIN1wrxC3ACZ0DTmNF8NeYqDbbIrNYQn_GQdZLmiFxDzTTJCycquuHH1aJRuKZBFxFm2-PFdF5Maa8KKd3qWOWJgJWUZeRgoJcsObgLcHubzXrJs8uKpzcR0fh3B3yrVzOI-wFynPUZZPDS9mksm3nXFJkAlGTTNkJ4JErrRBRTx2mmpOsItAskLS8xQh8ZKvdBHmSVHbGGqwiwkZo2GRMqYdhzZHVXbgM3Pi-eC4LUBCwAjAWLrU-KzkXXlhvnN6fLhBxZIi_8oJaHyp6w22JHLgK8Y_umz349jhlPkp0a8Ey663tSBxJht8bljluPO6Atrdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc3df4ad3.mp4?token=op0m6FBIqCz95vNIEIN1wrxC3ACZ0DTmNF8NeYqDbbIrNYQn_GQdZLmiFxDzTTJCycquuHH1aJRuKZBFxFm2-PFdF5Maa8KKd3qWOWJgJWUZeRgoJcsObgLcHubzXrJs8uKpzcR0fh3B3yrVzOI-wFynPUZZPDS9mksm3nXFJkAlGTTNkJ4JErrRBRTx2mmpOsItAskLS8xQh8ZKvdBHmSVHbGGqwiwkZo2GRMqYdhzZHVXbgM3Pi-eC4LUBCwAjAWLrU-KzkXXlhvnN6fLhBxZIi_8oJaHyp6w22JHLgK8Y_umz349jhlPkp0a8Ey663tSBxJht8bljluPO6Atrdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
تیکه عادل فردوسی‌پور به خوش‌چشم کارشناس مسائل سیاسی صدا و سیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/93875" target="_blank">📅 09:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93874">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRLwXu2izIEj4uiCLvTGyH5xNaQqEgGkb7HRea47gJVPs8K5SxDwrMWd52aKbAM4jg5if3uDWC3ocPSK8rcRtxGuMXFWsRKVO22_8HT1sdF-fzuK0rMw-OnMMZEMybCGWt1SdBy3smhFCPEwpyk-wenZsznKL0yID7ZSoLKx_M8u8c00n8P26jZHqzjOhRe1rJwGTJQbERKw9hO5CFGuTCHl3uuqKq4cNKNAQJ0erAkZAemDyVRtt6-wG7TkgOBvNcooocbG2ChlVd4QpAFy68fPNCp7X2Lo4s4V5E1OJR6Pk54WG1HHM_wwKB8mWA7fiFjMztDXqlVDRDqvBw3_pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|ایستادگی اردن کافی نبود؛ اتریش جشن پیروزی گرفت.
🇦🇹
اتریش
😆
-
😃
اردن
🇯🇴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/93874" target="_blank">📅 09:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93873">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گلللللل سوم اتریش ثانیه های آخر با پنالتی</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/93873" target="_blank">📅 09:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93865">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LiSMAPGnhJQqiLs-QsV_2uJcv2XY--m06DJ98nk8YVd_CQUVUNYPn_sCgsRma0ljCKlndFxb24NrH6Qs0hzWo7cjyQvGFtSiA-tnogvXtP-nNPZfepxL-O4IF5zorjnSmwozFAuuHbwMRyjMJMjm-UFVSkVND5HC-6BwB6wetCAmZxvwKj-J3fVRDepxJItq4HramGsj0gXV6SCQWysOSUEiO6XgLsWg0AhnySW37OVnAryidGUzJ8hGELkFVmc-Q0WZY3_0GgjBSve5DdM9Z__5iKZrRdagfmeAG8KZb7lSRZi8EixhMSNiXcVD59NkpS0vYF3Usc4CcThZGwgK0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NdnD03abEPyD6JXywPlHfDcKWuaXLJ_Qvn3ANgNj-mri5XQbDyGpLraTuc57m4ME28nwQKztb9zczi6eJHNMlCP3afzrbvYRV1Esj2WUrHpHhHlBvId0Dbz518fV1LJ292LfZSLLasaA34_OXBAUbP1f0UoQvHz9EyFHC7dMNs-SicZYwxyRjh6AZ3S_nIpZtCqzeDJ9KlTadnGK0cDcIRd6BZkmofD2zcKm6MMtfp2BT3cJ-_2_TJUtsrQra_t0Y554etxwzfPq_ssGSG6JzmvEqySWSM82Pe8hn-QSGJAHnrjTgrxOTLvkZyB1kLJMqyJe176VR_9TX3qnlHYTJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z7hdbJIZM8-B4PDHZRGjfEEyreTG3OZfbJWgY4K7VkeVJWjM05PnJNdIwstfVAA73AEjNUWhgUOvLH2dv7ivuA6_CQrNAgWEZfMXZ0CjvHyt5AwqS49wrLlGzugWHXYQbYrmeeTSK-xLZJ3G8he9U2V8wRf-KhJmBu44pWf6aLwMXAqTMDD6LOfoSOvfv8kANyfp-dN7_ebMB0lPdLziB_c-kXX7AIejPQgipEw0GNVDLjPup-fFoDKBhuOnihC-4vGAIcanI_KgS6ipYqlZlP1r64nRZDxHh9RnKixR8Vkxxnxhs_M9Vmwi1Z1bDyJIGFjQisk6OKqH1yznsYopFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOVZVqAsdvh1XWSaC_wn5AjScm7jZAKTSh1YCbiyrudLhOzPuCO0QNDDnruc9CbK8ONjjJbVTPvAZnn1DTxsWUfbDdjNvcvxpVCzBGBJx-T9ap5T8ymmeSe2oq5zRZYhO0JTFh9kQ6HG9s9Mu0ICBwg2F4F6WANn5upQVZpuTUweQ_EJNniHmDW0xiin4zbYGmpHg2QkIsdvyZeBaublH9sh04o3hPBKGGDebDmR3XyfDayezEaUh2iida1O3ya_dNoRTJq_ShFEHBugdJ8nfhDEFrT0DWJIoFtGbAiVfvWICDnq8f_aC69IIFF3eRCIhT-4cFCTesIrMtzo1DBKsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eLdEz073a-VMeGfF3-DaRt3QCxBOXH1ePpWHt5zo6TbozvPUTH4dsUf3mmXWBDK4vu-L4rnhZF8pQQ8bBQmziVstqjh2o0IDCXJWq66psl1dbKUcltAdEiy5V4BgyBcfKhxnQGg_xaTNWp8M0GDddLpcuHSi6tj6ztyyCagnR0hMF6hhFTgautxV9P7G7QP5HfFnp56TZ-ZeVrvvrsuCZEEaMs_qC2Rfp85EVNK1Akq3IcQTKngcgz3eMj3TEgfE7OoOsDY58JiG-azCK3yLMEWv5wUqIjxdxdfqD6s6fJWb0movewhVs9IssPkHsL3W4uzBVlXTo1T4HKO5XMmF5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0fg5q-TbX5j0DRfUGc7SltZrnDY7qfFDob8pJMCmA47mfe8t-LHruXrWgT1JKX2DCi24iuZXQklsdE1sGkekiseM5uJU8BXySVa7B-PgY_aLaRObm0wHWCdOYGpZo5SHSC6MlAN_-mw9TI1DgaKpV39xzgR8jIf6N9ILqRMmwgnZRFsp6vteRRrCpZTJwW3UICxqmozNxUJ9VRgdWIPoI6wrhRVSPFhtA6zOddPnEH0mjHYQbyBoY6ekzgo34g8PnHLtLFwf1FfIP0rCBYbOWD1tYAHjMSdFLqPj3Xy1_WRUvdP_0cUbUeFEUIO7npyXyUftMNWvXn03S3oQ13Ppg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oT09njQj_3cC-QeyzfInwfVuy_fngaXMQr-jbyHjXZ43LWujVc0A9Vb8w3U833HQF4OpV3p4GTb1ahWcLAxq7f7CsfRko6wCjGn8F0UWBXH207L9_u3uQbDjF9Y0ygg8nPqaanW2wTLNspGGxm6gMcRPpP1-HtMGeVxrC02dLINWa-dKZk4-QDE8aTYSF9U1O25mvIszwAvKbrNBqBe78kI5XQd5a36vvG7w1uO6HA6gn3eO5pucye-hdvG7HB5FtWry_WfkKg3g8VWmy9xT0UZ70fCLgnvneDChbP66BVdJyAo8bSGpiy8ZP1um3h5DzSkiSY56xnfrgTkdcLS6Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmOcYzx519ZNgOLND9ZqZMFjrhtiZoRGVIyF5aV7zb671qKhyIuAdEo6knNM1oxh1epgKAJ5wXbOVbTTrgcxRQZq_SqvIluR7bwRhS-55eMt9hEEh5DeQsqMn3iZMLH0Np0vXU7WOsxlN72_3G4XqngdIMZtFBNRMFuXQovDXYa4F7NlHNWlUST-Uo0wasdvZ-uSEbfdtZBk1-VTo0DcYA7tiv_FgVI5fX0sjg9pVMFh18TU3s5zD6bCkEI8P8SfTZjI7_KKF3kHbj4Mu9iGdNXHmZOCSjF4gwWUiRCD4P_bx_t9aWBtS5gTKFkIw0QJRsfxajH0dECcS0j3vKnxJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
بازیکنای آرژانتین و زیدیاشون هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/93865" target="_blank">📅 09:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93864">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گللللل دوم اتریش</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/93864" target="_blank">📅 09:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93863">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKCiwv1Hq-kxVjsI3XkDZKWoUCPpvj-v088wdVn3ANGBy48bUsseErL_pa55F_rSYpHhfQe5uzlY2Yi6BBLLfuWtCd7UNet0yuiCofOE-WZ1xO6RIKpbD6k3GhWcMKWezQYVhO5NXkGHtw0kYAXtzeUbymuUGS2sQVkC5aF28Y82MSMhWwHs4X4Knfu19wxZXr95qPZejuoN-WsOSiUc1tI9ELtc81_g-ab9iC5dzikAF94qbrg37VM46uCWGkkVyfxifml-OS7JSaKN8mpDeEDZTsZbfTgXwUDT_vaXMAX8Kr5-wq9zgfeu4UMnxtNh_IDA6KAUi5aQmxRsd1vwWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«تو به رکورد کلوزه رسیدی و از رونالدو نازاریو هم به عنوان بهترین گلزن تاریخ جام جهانی عبور کردی...»
🇦🇷
لیونل مسی: واقعا باعث افتخاره که اسمم کنار این همه اسطوره قرار میگیره، از جمله رونالدو نازاریو... اون یکی از بهترین بازیکناییه که تا حالا دیدم. رونالدو نازاریو یکی از بزرگ‌ترین بازیکنان تاریخ فوتباله، ولی با این حال نفر اول این آمار نیست. پس آخرش اینا فقط یه عدد و آمارن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/93863" target="_blank">📅 08:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93862">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اردن و اتریش بازیشون 1-1 جریان داره</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/93862" target="_blank">📅 08:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93856">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gAHyBtj0GH1ktAI_Oq9K2L5AYMRRggGGSFJegSOYZN0BQP6bLSwapb3FovR5El16C-YNQ35F5xBb0NuUHp4aBtsnZK50K55icW_2d5yi5CKoUiP2N1AVLOCYzjvVWDXiEAM_DIwJGZRSQs9xQySEarnmGRLamXyemdTXXDogsAXClHurTnt8sHc4O3MtEhFBUvjEZJpEZMHch3D5N295NEUiUN56BLdJhhcPYF182bclaHZa3-emGcEAYdYdVfvJfdsf0UD0UrD9Yi9DRVOoxMUx2tDT4uidJAITSRKnGBy2Ugo-EkgPLn6m9xfoj5dpfLjczcWKNfXDHEX9AbZ7sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/saGLDcjwaOVVlJ_pfepyzTj_nyGq_xfsKGVzuzuA85TjLJJZx53EhXq6k6_bFKsvH3QMkqBz9QkjQVgeFTm1Mtyp5hktdlEaNtbz0rKeJnYoGwX9myekQLeGGKqZSvOijeXEFptLhIwEqgqadEwXEm4ATIt3kpKOMkFLJDsB8gXkMyxNhD7SiiA2QFmDmy0de5lMy4lzaUwqQKZihT_ShfMPW3psEUb6MO5CcqIIlf3i8iG3A8FwX3fLO05QT8W4vkomCpdxCDIe4tSiz_gZEUgm7t5ODjLa3Oiwk5YFHNDxSY4GImsTSfXRHvXYh32hiOXIsvNQI51Ad8psK3xLMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FFvhbqTIZukCzvt48rNRLUJtBX8WXflQMDQZBK8DJVDCqWDSSL66mkK1FWWee2NTKMYT3oOzPaGOpX4LtYjK2TbQFYglKcXxqkY0slXEMXkTgRnuVMu92YjOZC2DXuPlm3MNTSbUktmdRqm5RpH4NaTJeHn10SYxmieLaR-i1jGZRvhJty_cxxguUogTf0_otEBvhX1lB1F_yjslhbo_5ecRuj67fnJEXYotEAR2bNNUi24vSK8bNDrde_kwD3LNoUs0bwHpgr1y9HPUSYkvDo6XP0Z6gAIqlCSXfdNeS2Ge8pxwXClBDV3tI-sd3RRA6-hkUStnBZRHUa1cqQLU4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nX33RhzGlJoFniw2Lra19fhoL_tz6UEFhMCBcSvsT8xISOLHZZfPDOgRJv-p5UVmrGB3a2bE-4qdzw_Hvc3uqGaa1tSmbZcdsOw09n6NF4p6UxjFNchavqymge9xhSLVZ9lfb4oALm_PhbbffWaMUE3VUnRg65cNlQ5G2cei_k9BOoWINMsX7iRhQO18jUz0JeQzOpF4EmxzSHBDAf1aVlTYDuVPFjamNPMuba59FxfJnobT8CBMBNZ7Af0Cs0OqWaIuLQbMTRURlVh8asvzL-58tl6UFsPQ1sz_jKKGsN1AD1T7R3qIgz06IAdXopnSxK6tvfjtbXUxgGZhTvlxlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SWFeL3plEbFC94cCNC0QH7h4tPG4pdkdFPDBzusixwE4obQqF7PbJ7iz6UhOuakHhe8b1qieq7NBIW4BpV4SnAy8bg0F7RkVkpWVRAE5Rf9oq6QI7RNAc7QYDjyAlpF7kJA8k7_91bijz9OkHZXlPQWr2SzhAGJWaen9fanZZEJ7vl2tEU7JLFcMyw5Ud1kFXf4dukqQtyp2b1raioLpeBsv68xWyNgLNMGACI6ApoD5Huoofy9NkaZUFp4paedagQDK5-ggfpBEQFJ7poUkW8hjkvoXW9u4Dw8H3_-rdz_d53qD1fqrW3GgzjEPbCN1SwpOuI2P5xD3OVBzYPo2Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nce-1J7u7MJH5n9HC1n85OGdJg5KD0WDEx6uv7FeUXhbCw844ZeE7JooKSZi5CyTXXQh5yJlCtzs6L7-3rnWJkgxmeRxLkgywMNl2bEwVfqvqcgPpndtUB1ef-KW-i37quNwfNV1Z1aCJJUsGFa_BcADgbRVGQ26CX4ellRDV183LrRiobf6soUccl14h-2XGQ_h7PDxvMkR9Zzldn3oJkh_7gKsbfG91FxLBpi9--KlT3UP_gUudeA0HeZiONYlPsHxZOMGQIhP6SXMsin2VWkCptdrh5Mh4BJzfK0nOE7NIbeKUttMD0u1XEPxuSinDLHePrb815UjEoQb-SOu5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روز دیوانه کننده جام جهانی
🏆
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/93856" target="_blank">📅 08:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93855">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sy4hc2F3xwgCLd9wSgl_z8pDZLgFgF1Bh4bjAShSs5JjgAy_YFeDvz2ANXgfPU-C0C3PhLxBNarD83IjcG1ZGPWTjwie5iswi2p0YWTPlraLjtwRNcriV18e_nWamxucaRSJhrVfuNQej43lyEhTE-ccuu7mgNWd4BBJv5siPp7glCc-NwLVqj3bTi-toeTLv-KaMouyCHUjckULxFTNCR-ibsFyWOAoMIm9Q72GAQ9BlsFVqCEbulfkhyt7F29EoqjQDH9GYysS_5bZt3_xyFjR-T_WkDm4S7gvcB7t7uGzy0DFp_2C_4eHm3PORr5qzacpRMCPhizgecZY1zTkLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇦🇷
لیونل‌مسی درباره گریه کردناش: روزهای سختی سپری کردم. این جام‌جهانی آخرمه و شدیدا احساساتی شدم و گریم گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/93855" target="_blank">📅 06:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93854">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🎙
🏆
🇦🇷
رودریگو دی‌پائول: برای لیونل‌ مسی ارقام فردی اصلا مهم نیست و هرکاری میکنه که مجموعه آرژانتین نتیجه بگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/93854" target="_blank">📅 06:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93853">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YC4oORBq0ZST8prSSxOQZNs_y6JqOm14FeTCPcKqK_u8vnfmEaaptITNk-cwFgs1EfArC2GxXo2otiypBWP8XlmNrOj3namZFQqGCch5BCnMMVPoRnNrmRRr-h3Nv1ruy9-11zCw_-hJT9KrifHGxOzf_pM6lzb1Mi-QKltj9rvAvx__hHxzeJ8uCnnxHvF1DhXsLACdejafgejlunFCjcOe4fDVa_MaIDOr5LmPJvpJQzQxtCR5UIWYma20_EoEHQ3Ot53COhPKhXIglMfrAYOICG-MXN5KZvTpIREKhkR-Da3QmZsLPSd8zTwYTRkgxBc0dX3p4cUmZmUGwg05xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💥
واکنش هالند به درخشش لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/93853" target="_blank">📅 06:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93852">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f19dfd3f.mp4?token=GTgQL4y9Yn2B__NIIvk2HgDm-mMT-HZjWiwVSv6iq1A2wdPcp_IVRR_HAmK7HhqtveOLdlOscsJxTjYeAwkM5IsdUalaFLYGjiNiruuAe2Ixv7og7eEZB9Mrn37loNWxm6KCTw0F_NnkCdfnbLT26kWNtZIesgXSHhHl_5tjMYpv2SWWeYRbbem38p00x98cvM1ou3Pl4fBjSpMSuEOnbIXJqc7Y-eixz0TpbBWR3WgJkmqfirn7GePjP5TavPD-QOjrGKVb2mHJCkjSG2GLRrVkPkXWsvpO8gue2HN5UcIHKAJWpb07HcY2JYeLPYPks1sXZY2JUfGCxQyptP9Iqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f19dfd3f.mp4?token=GTgQL4y9Yn2B__NIIvk2HgDm-mMT-HZjWiwVSv6iq1A2wdPcp_IVRR_HAmK7HhqtveOLdlOscsJxTjYeAwkM5IsdUalaFLYGjiNiruuAe2Ixv7og7eEZB9Mrn37loNWxm6KCTw0F_NnkCdfnbLT26kWNtZIesgXSHhHl_5tjMYpv2SWWeYRbbem38p00x98cvM1ou3Pl4fBjSpMSuEOnbIXJqc7Y-eixz0TpbBWR3WgJkmqfirn7GePjP5TavPD-QOjrGKVb2mHJCkjSG2GLRrVkPkXWsvpO8gue2HN5UcIHKAJWpb07HcY2JYeLPYPks1sXZY2JUfGCxQyptP9Iqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🔥
خنده‌های لیونل‌مسی حین دریافت جایزه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/93852" target="_blank">📅 06:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93851">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StifDIMZjoRDDpJXotr1dyTZq9JJ7bYKHGWPF9BUoqejSgGmCretK_xTmIQllMUVUCAK9dT06httu_eNSOKwJXzEOQ-33lC-a5vcMNEIDEkpd2H3pWjNRdPRYzcCxPP43bYPd-BkZdgViPxb0LXbiCmWrbHjHVJTMVmk9QhWB8-pY-e8avRu-U7WN1nG220JaEXGnThxw_gDnZCm5zuBaNOOk0197qnXF2ZcMpVDcU9eMsfCyk00z7JH1R4l_ZhbEqEOIuk_SVv0lun5MeLkIpp4riuYKHP60IEAn70hElFgSl6VSelUp09eSnarf1Xy-cDU6AUPSG1o9wTU8qoaKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
✔️
لیونل‌مسی بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/93851" target="_blank">📅 06:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93850">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryqa3jcz4xHe5pBh5LXU4Vg0ds-5iGA3GM-1EIsLB1NJ84V9sO6Tn77BYFxWAqO-BKiIo-7Cxw1koCBMlwzS2WyMA_KSUbI2Jhq4CTB2OEsbz7Ay1xgTAsfqL80r3M9Ywj0J5EZIOnAHB1abmJsJLyeOtnxQPsXX7pYQMTsX_iZu-_iR4yOrvHvgLXimV72wfZBsVsMltWBBJk1426mwqer8B_OloIogQ2segoMJnSLkSCdx6v82YzsFqO3x5aojUtYfupbqS1E8VsqP4-p24yv4q6YPm5CnIS8NE_XdNGI1PiG4FwzA5K1YSInNBYDTFsfIFE_R_4RAVjaek1Yzmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
لیونل‌مسی با ثبت سه گل درحال حاضر بهترین گلزن جام‌جهانی ۲۰۲۶ هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/93850" target="_blank">📅 06:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93849">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A62wlSNuaZF2lJclSaQfrM_uCOyKFTnaXADCt-u2v5UGYyq-1M-9ltucucW3ydkaCi1hynZmLsYVKSIGKexQ-AVTSVbbdgOgIOZ0zSj1-RfWEX-U6Nh59ExB0icr938Fi_4shNmSCzN0L1_D4fWg-asxKI3oBVVbsWRAARvZ7hLud82Y9Xwb1rcuOJot9FSQvCwms_6nthYQoXnXBg_McP48xfGRbQNcU14pGwYklMcVZoy-jYAbZ0eVwS4oanA38WV27rttaWtlNxzrRLe68LYyH2LXkeNZBQdFA_lK1zwWy2xuIDytv1htGFgTY1Y4NFUVWANy3aA3bsw-bi0BZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
پستی‌کوتاه برای درک عظمت و تاریخ سازی اسطوره لیونل‌مسی
🔺
بهترین گلزن تاریخ جام جهانی (16 گل)
🔻
بیشترین پاس گل در تاریخ جام جهانی (8 پاس گل)
🔺
بیشتر از یک‌هتریک در تاریخ جام‌جهانی
🔻
بیشترین رکورد دبل در تاریخ جام‌جهانی
🔺
بیشترین جایزه بهترین بازیکن زمین.
🔻
بیشترین تاثیرگذاری در تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/93849" target="_blank">📅 06:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93848">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCgfa9e1ojwSIxCOLmSerFjogH8pWVJx6VPOLX_P4o3mWZkJTtP4bX3EzzylPt8-EnSvwaXbL9sKmjExHCC3P2klNJxwMz_EdJDwVUFt6vcYin5cmhbUphWZi_9JDctpzQdfQL2-fCVloF3WfNMByq22QmLJwby_RuEJfSp4eNJQtIV-iqx1SQGbr-8PMDDksy3QCAw0tC-y_u-nmGc_SWerH5Ds7UMGrHHcAJ2fZV1dK_QqtopQu0PeJ9TRAA7bQbDRh479pj1HiqEm-11IxI7jlaI8m25g9tp9XT6LnoRzdfzkc1sYvI2vHqdZoHO8wxl_P-tKluEgXCM-OHxKXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
#فکککککککت
؛ در تاریخ جام‌جهانی لیونل‌مسی با کسب ۱۲ عنوان بهترین بازیکن زمین، با اختلاف در صدر قرار داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/93848" target="_blank">📅 06:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93847">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZxGaX-Lx6Fm4jsGBDAAe1ZfCdL5tp1imhPcfqb2eBtysHIX1DL9Dij7JSVlS-2c_gK923TTifJ4L6-an5Y3vTOF5QAuNVFa0K4JMsi53x5SDGKICKcbhbbSKxa83UysiclbF9ryqa_gn2qcMcyeDnbxSz8huWnSA84uUUNQVIJWUEgTs5-Ob23FtU9vts52BxfZWSjN8eFi8Q3LTzMT6_apgXrgBzEs7dYgm_GUgF5ctJxtUC8bONXM3jxNxut3pFKsDaPbYZwhexVC_wRk1aIUAhEWp2tLArntVaEpPtnSzg_sdCPxoV2S1FO6JECdWRbyHhNKix4mHm2SV8Sy0-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🏆
#فکت
برگگگگگگگگگ ریزون؛ تعداد گل‌های لیونل‌مسی بعد ۳۵ سالگی در جام‌جهانی از مجموع گل‌های اسامی زیر بیشتره
كريستيانو رونالدو
‏- تيري هانری
‏- مارادونا
‏- ریوالدو
‏- نيمار
‏- هری‌کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/93847" target="_blank">📅 06:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93846">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyZJ415ZorXJv5v4DUTNR7Sv-P2Jqv5ZoMFM8T5ZRN3nLDd7IWH_LgtaOqFWUEu0RtmAFuOf74hyxijRo_edytir8DEOwJG_3vtQ1HcQw7Lo4MBxbiaEz6a0ESyoNf8Zms6cT49PL_clwwafXpcbWUAUy0pI8KBYMsU3ZJ6O4zwFKDRE02GKMmZteDG7FLrn7aEB1Ih0_E3nx-Nckfrf5nQ4AUc-82Bg6wa_Mf-9CFNPM1xUc5VmBNCSRmfQlXApIaJuy2bWLH80zOODbmbgDh8b57V76d-p2p0SOrJ4spjhQ8wEm6fVex6ubHjmlMqj0EXEosPS15zDUimoI9h5Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
پشمااااااااااتوووووون فر بخوررررره؛ لیونل‌مسی در تاریخ فوتبال روی 1328 گل تاثیر مستقیم داشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/93846" target="_blank">📅 06:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93845">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NeB08NsA2PGB8sG-boQLqScZSxWR_uDKD9tYo-MVuNURhrKb7vQ_RXq3jUasG-wqzfOPZ05JjLygTsf-tc5LHPh1jPzoT5KyD7onZ18oDPXzoKKg8w0wOgOQeQqseg2HKFK0uNUDwXvstLgkihtHlvyVflMdHAn80XoItwLqc8P86rGGzK8bt_g95ynxBjrTFgYxHmIfbmen6ZIlsLr1VcmXGwwLjczPC2BQcu1uFKZPeqbpnSiijsaN_AISb8lj5WRBFvbxx1BiwshnS1bLx4IdG1YPOCUW4lpvsiidqGY-3QwvWZz5x1tUv9LeIcxO2tEB_yD0TAbmd4Se6qN9cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|یک‌دقیقه سقوط برای کسانی که ندیدند؛ شاهکار لیونل‌مسی در کانزاس‌سیتی؛ آرژانتین در شب متلاشی‌شدن رکوردها‌ توسط اسطوره مسی، الجزایر را درهم کوبید
🇩🇿
الجزایر
😏
-
😆
آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/93845" target="_blank">📅 06:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93844">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
حفیظ‌الدراجی گزارشگر بین‌اسپورت: رونالدو برای اثبات اینکه در تاریخ بین بهترین‌ها قرار داره، فرداشب و تا پایان جام باید شاهکار کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/93844" target="_blank">📅 06:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93843">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">📷
🔥
🔥
🔥
🔥
🔥
شااااااات تاریخی از صحنه هتریک لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/93843" target="_blank">📅 06:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93842">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imYnaYyeig8Zysy81C2saVbX1t9sB8Ymn8frS71yixETW7yKKnoQMbZX1Kze-k1MFGUz09NjXEggigc4kRoaXxE2Jgtn-GJlSuXsEmsc7YhYtZKK2KS06YbZ3oFk1gtrgKz1bhZL9KJBI-hN46bZhek5ptZvTQQiPDFMeN4SHVRzQCfncjswM1en4t929QbAJYmZYhMayXJVFi4KIBwBuabuUe-fsJD4TgxFaiBXiasZnKvv_MUm9daOQZZy74FA1HqB_0P8q4kd_Te15Knq4PyXa6t2i9mZ0gX7OvZilVPPUmFhLOlejZPhZBAK7I1a6E3jDr_ouzsxs-tQLYbCKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
🔥
🔥
🔥
🔥
🔥
شااااااات تاریخی از صحنه هتریک لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/93842" target="_blank">📅 06:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93841">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5XuGKtQ9M4JntrAU4UUHs91c8Z3BdCAXO6tGBv5_rqMaRBHpCB1RqMBdw5DWbvOjJM6q54UFVwqOOOEg0r4gn854PDuf4JJjtUwNCjrtWhtMoZvStiR7MJ20whivWUPJNBmX55Gs2tGr5emgoInDrMXRLZSm3Mj8dL8oagvbtIJzeDNSno2pkwy3_oVrgDywsQoUrMDZ9TkeaHapz7euI9itGXD6N8c2x0zbcoCz6nlVixNMF_RRA2WZ48eYJjoHZ5w2p253IUYhap1EGlhV97uYfnkPsriOsHeiHSJPNKwyGDfIqWgJ4bjsAuAVxT8vgE53t5nBgargDHDp01TqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😛
😛
مسی اینجورررررری کنار زمین لش کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/93841" target="_blank">📅 06:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93840">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fwk4JCUuInY6lJohFAS4wnvUzRVEXmY0C8XqwaR-vRnmsGJRwJcU7vSjpRpW7gzgAJmzZk8_j17t0qF5B98luRcNiprl7BZ0E098In4ChbWnRTCkqIKskGerXslK4gbEmgUkwZWGnYzuFveMvjGIZn5b-jV-xzlkgMF-gsd62zLvGes9bEZ7iwvBM6YwVaZYeE7wgnPYglfKZ0nLcLPHhqWHj5tJApANeqeixcPp4fHzUAKAZ6HD2BIMf9RQjv1f-gWwqs692yw9d1wEb_4XAazd8gXQug_dV6TyB_u9HjHPyRqq-ndab76rcwMrn8zdytaqRrv5m0Dw5nHoYyx0PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
همچنان درحال تکمیل کلکسیون تصاویر جادویی امشب مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/93840" target="_blank">📅 06:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93839">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ud8RXUHJD_7XhJ8rR_hraJLQg3iK7t3w5usMxNa3tdp7yiFxbhm9goqpdEkNh1QG5ONkF1QDjzW93nmF7sX5EAFIcRwn59trp1pWyHBwffe1at-fORhmwdIQ7Zzrg-U9qP97SLWn1eqJobOmcOGclU-gAygkbqA4NGjnOcLqJrmzRMd93FyYqbHNm9gR0dPBpKc-LpwhGTCWa28q2cdSz1Fa7QYDiTtv3XtANubeNl__Moe7DB_jAYO2hFmpsob0Om_KQUxJz5yVvDWfSzrEyJvzpK-yv0M1gWSAPwiy3CzLZhV6neBtSQZzuOJkTbidqBxrTPvwxDSQyn42QlisGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
بهترین گلزنان تاریخ جام‌جهانی؛ از الان برا مسی و امباپه رده اول و دوم‌رو کنار بذارید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/93839" target="_blank">📅 06:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93838">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8IbBOoSeasHHZ2tsdctarhqgpHb3DpHLnaZkDgqDScsdy-C9kxUIomymAWlYbz3bc8PvyhEDOII3HgaKB-Cenj09H1OwopMk4ZRydrOrVrmgzgBZeCgxJaOdDpy2HR-Zav8P3npxKzlJDYyrUBxpz0nuCUbSLTQn6AZsIsbGE0BBkf66SmATOwvtvvngKWnpEYnngkOqOQKvih7N76fsvRKb70DzqWz6SzrDxWRM0AW-uk5O3648J2l_nvf69rROIOoR4psV7qNInpPxDY93xxPVAIsRD1bxbt60ZSpoqG3RFgzu4Gez9PskG-J3_LovtkhcgvgEgQGrWjXZJ32bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
📊
لیونل‌مسی با عبور از رونالدو، بیشترین تعداد هتریک در بازی‌های ملی تاریخ را ثبت کرد
‏— اسطوره مسی (11) هتریک
‏—اسطوره كريستيانو رونالدو (10) هتریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/93838" target="_blank">📅 06:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93837">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فتح‌الله‌زاده الان داره پیشنهادشو برا مسی آماده میکنه بده تحویل بکام</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/93837" target="_blank">📅 06:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93836">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
گزارشگر بین‌اسپورت بعد گل سوم مسی:
چطور برای فرزندانم در آینده بگویم که ابر مرد تاریخ فوتبال در زمین نقاشی می‌کرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/93836" target="_blank">📅 06:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93835">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هوادارای آرژانتین تو کونشون عروسیه</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/93835" target="_blank">📅 06:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93834">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
لیونل‌مسی تعویض شدددددددد</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/93834" target="_blank">📅 06:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93833">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔥
🔥
🔥
شب بیداری اینجوریش قشنگههههههه</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/93833" target="_blank">📅 06:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93832">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e341d92384.mp4?token=N3kDiKgM93VhDAY_cVL_WoHJMuewrx2oCUNtmh67gaKwAQWhIrcMXzdrP9-o6BOx1oYH9AONfyD_gbB9Asee96FLMsck3UeODL3UQwfc_PmYkJTX_Pi2w-5NL2stWiDRhk-BR9lglT9EvD5av38KDiNdiLnyHw485VbEdQl2QiWGeSBOJ7WWXj_4QuKerhxkRb1y1THYSZT5_xGgJSgv-W_aiuRQPzk-J11RfDi0KBqzZuUhMyLGXBaiQviCAkGg9XXa6dJMszRPn6XXjxAgl_PwXx0f_KtYjRUCH0CKmr71cL1S1QJ06Zgb7ymv0g9SZNAkONwXr19h-HV5OJvQZoc8bTDz38gtdx_8frDGaHr7rTil5hkHrUPvsNcjpvoGJXgAMa1uT5z0DKxwpK0795lpYDP1-3MnqCCXHNoYKOuIixpLASE2ALmPF541f0OBa2i0leUvbi5sqvp1hsPZxJke06U50zLq38_Q5i7IEz_Qdg5vVKmIMq-rGQx_lNJ2trcnzjwPWTianxj1qvIDkIuhgERlhZHoPuw96Pkq8yme0C2roB8IMfCC6kIiI3aPPFy_l3g5AEl0V2cTYSoJK9_Zg_AL_dvjh6ujr5cED_liGbcWAJevac7c78bn6JNjYKt9i9IGq8w9cy2Fso21dAt_9LpDNt9xUmxYVDH6cKg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e341d92384.mp4?token=N3kDiKgM93VhDAY_cVL_WoHJMuewrx2oCUNtmh67gaKwAQWhIrcMXzdrP9-o6BOx1oYH9AONfyD_gbB9Asee96FLMsck3UeODL3UQwfc_PmYkJTX_Pi2w-5NL2stWiDRhk-BR9lglT9EvD5av38KDiNdiLnyHw485VbEdQl2QiWGeSBOJ7WWXj_4QuKerhxkRb1y1THYSZT5_xGgJSgv-W_aiuRQPzk-J11RfDi0KBqzZuUhMyLGXBaiQviCAkGg9XXa6dJMszRPn6XXjxAgl_PwXx0f_KtYjRUCH0CKmr71cL1S1QJ06Zgb7ymv0g9SZNAkONwXr19h-HV5OJvQZoc8bTDz38gtdx_8frDGaHr7rTil5hkHrUPvsNcjpvoGJXgAMa1uT5z0DKxwpK0795lpYDP1-3MnqCCXHNoYKOuIixpLASE2ALmPF541f0OBa2i0leUvbi5sqvp1hsPZxJke06U50zLq38_Q5i7IEz_Qdg5vVKmIMq-rGQx_lNJ2trcnzjwPWTianxj1qvIDkIuhgERlhZHoPuw96Pkq8yme0C2roB8IMfCC6kIiI3aPPFy_l3g5AEl0V2cTYSoJK9_Zg_AL_dvjh6ujr5cED_liGbcWAJevac7c78bn6JNjYKt9i9IGq8w9cy2Fso21dAt_9LpDNt9xUmxYVDH6cKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔥
🔥
🔥
هتریک اسطوره تاریخ فوتبال دنیااااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/93832" target="_blank">📅 06:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93831">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
لیونل‌مسی بهترین گلزن تاریخ جام‌جهانی لقب گرفتتتتت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/93831" target="_blank">📅 06:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93830">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پشماممممم
مگه میشه
چیه این فوتبال
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/93830" target="_blank">📅 06:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93829">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خداااا نفسم بندددددددد اومدددددد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/93829" target="_blank">📅 06:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93828">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">قلبممممممم داره میگیرههههههههه</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/93828" target="_blank">📅 06:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93827">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وااااااای</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/93827" target="_blank">📅 06:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93826">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هتریییییکککککک لیووووووو مسیییییییییییی</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/93826" target="_blank">📅 06:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93825">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">هترییییککککککککک</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/93825" target="_blank">📅 06:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93824">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خدااااااااا</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/93824" target="_blank">📅 06:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93823">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">هتریککککککک کردددددد</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/93823" target="_blank">📅 06:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93822">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/93822" target="_blank">📅 06:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93821">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">زیدان تو ورزشگاه داره ریدمان پسرشو جلو مسی از نزدیک میبینه</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/93821" target="_blank">📅 06:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93820">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBZR77WtRZlwb6SHtqWA4BjyMjeIU9OZuk0_mW_nO4tzg-ZdLBWxeOw2qrzJ8J-59NJfp3R82I8X61mYGqCc3l2xFNjUorzH4MI8RvmgTIte8XuiGGGvjGusX4MJ9icXnsxjyGes9NJRyFSjbC9ZhZPILtax2FSp2KSBM04rEOkg8A0Hacw7U6htkiI1yRqZIAJyulgQVjINC2W0I9EnXiiXl9OAZhZGmnriGPmz9S2ek2Oa0jAeX5FrER8WjCqm9XMxM4BuYBQ9hZWNeUZXRsHo-KZC12TOy9h2fATMTCn_Q_C-kChOvnS_6kZcAfW1S856fG7GRjg5vFPVAbfelg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
69045 نفر تماشاگر درخشش امشب لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/93820" target="_blank">📅 06:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93819">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">داوررررر رو مسی خطا نگرفتتتتت</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/93819" target="_blank">📅 06:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93818">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پنالتی نبوددددد</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/93818" target="_blank">📅 06:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93817">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJzCkuNmVkwzhGtUCzLhU08HG_H1L1t6-A8Od2erofpbc-F5__MiQUHPgs3vGl4FP8oEsluzQOa5z78-SLJpRYcvJszDJy-d2yB7VRBnz1lXeN2fYextyiY5mV875Ia0RPnS8kUCTD4-7QfJP_o3MhoBQHcMQwgesyK_vn3sSZubGLlP5tdBn5HsnD67ML1I3RsbA2EL4DHED_o942FLocjx7JzfXzpq32UGTXuMwZio01H6H_TG10SR9g296Ke-sEwzCwDI3kLWZ9qrB4crCxfOHLqY1f4Uetmzb4W1Z-EGy_cdfh7LJwBfGDiPneCuIgvRxH6Xz4tXcC7ac_D7MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/93817" target="_blank">📅 06:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93816">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
📊
#فکت؛ لیونل‌مسی مسن‌ترین بازیکن تاریخ که در جام‌جهانی دبل کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/93816" target="_blank">📅 06:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93815">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فرازمینی
👽
👽
👽
👽
👽
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/93815" target="_blank">📅 06:04 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
