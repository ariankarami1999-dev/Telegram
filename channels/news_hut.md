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
<img src="https://cdn4.telesco.pe/file/LienQdsnIEOBD34zlNN7AF5XR2I0bVQIfoTgnLx1Ve3Hl127ma6K9Xs9vCJNZEutkQuwzignQpdpMuqemmvud4IJdNmkyecKJ70fgV3vH3PZ008UOU5gGszotkFN--ZAZaR4twhvZTaXtkoZlddr8O3jmE5CKhWPOR79hUU_E6gWyHvExpSv7V3DuY6JzW0cldtS0HU4jcPaRciZ-Zkzll92Fl8-2Wf-lAn8NhFEh9x0mSXuBZnL3iT3KnT-NdC8tFUyl7GG7wk-Iu-iEoo_lgUOw5TlZBx7WHs48tvncXfrE5SfV7Sauo5jJGQXbgMvx5dEQhIhZRoAfum8zRkfNw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 109K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 16:28:12</div>
<hr>

<div class="tg-post" id="msg-71571">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cc03db8a0.mp4?token=a8AB7E8K5HM-KZbCWlkiK-T-VEKFOhVjVnVfy-vyN3Z_5cdqw7PoUuzhgAL_jBul5iqbX6CgDn40m_P9_oIZVQ9kyN0uoCntPdJ0v3WQ7VQ8XzTHHtLXx3lP_jye1uWim5y7X5AMEEN4Go7mbuPuXu1kH3gOf5ng0A-CPGrU_ec-mueSvtKSjdTKMKyoKqioH2iTvG-dzBEkldx1PUp2G9zJ0mv6DAbxFBH5PjXQgEGmVX1iE7rvngkM8gq-UtXWK9942L8iOpOhqFmtyXGy8IT5hj3zfMhB-fUFpT7MdOwsEaNygQuaZ3ER_qwPiwAAjQuEkPmh8BMO36lydaA8QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cc03db8a0.mp4?token=a8AB7E8K5HM-KZbCWlkiK-T-VEKFOhVjVnVfy-vyN3Z_5cdqw7PoUuzhgAL_jBul5iqbX6CgDn40m_P9_oIZVQ9kyN0uoCntPdJ0v3WQ7VQ8XzTHHtLXx3lP_jye1uWim5y7X5AMEEN4Go7mbuPuXu1kH3gOf5ng0A-CPGrU_ec-mueSvtKSjdTKMKyoKqioH2iTvG-dzBEkldx1PUp2G9zJ0mv6DAbxFBH5PjXQgEGmVX1iE7rvngkM8gq-UtXWK9942L8iOpOhqFmtyXGy8IT5hj3zfMhB-fUFpT7MdOwsEaNygQuaZ3ER_qwPiwAAjQuEkPmh8BMO36lydaA8QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیویی جالب از یک پهپاد اوکراینی که به سمت یک کشتی روسی در حال حرکته و یه بالگرد روسی تلاش می‌کنه اونو بزنه ولی، این پهباد در نهایت خودشو به کشتی میرسونه و منفجرش میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/news_hut/71571" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71570">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31fa8bd2c9.mp4?token=dO6z-tE9xhCp5OGePrI0RLOFQgjCHUGRdmB6vUYlOohjdqDxbU88aBlru01toNithPLjFbgavXSL19hpSs28TYjFv_pGwHrcGD5GxVXV1yNSi3iV32Yc-EP2P67wUXvXIPjzd4JOTPZQZA_R9p-OL58-6RRL41NkNct_wTiyJR-1Zsj2UWWffzzCCqp8LEvTN-67fCRi4HoB8_PyhTOnx48k1G1NjsoF2rO5oI96t3DNwe-njOjZCBzNRBRC647u8_1Dp79ox40_zm2x5GiPaxQG1oXfvaPAb8Ph9EcrLQjWuJQS98Sa2SFTKKzlqSgAb8DNZpCsyJXeDX28upGpgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31fa8bd2c9.mp4?token=dO6z-tE9xhCp5OGePrI0RLOFQgjCHUGRdmB6vUYlOohjdqDxbU88aBlru01toNithPLjFbgavXSL19hpSs28TYjFv_pGwHrcGD5GxVXV1yNSi3iV32Yc-EP2P67wUXvXIPjzd4JOTPZQZA_R9p-OL58-6RRL41NkNct_wTiyJR-1Zsj2UWWffzzCCqp8LEvTN-67fCRi4HoB8_PyhTOnx48k1G1NjsoF2rO5oI96t3DNwe-njOjZCBzNRBRC647u8_1Dp79ox40_zm2x5GiPaxQG1oXfvaPAb8Ph9EcrLQjWuJQS98Sa2SFTKKzlqSgAb8DNZpCsyJXeDX28upGpgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری صداوسیما:
از جنگ تحمیلی دوم حدود ۱۵ ماه اینا هست میگذره دیگه
مقامات صهیونیستی و امریکایی پر تکرار گفته ان که با حمله به ایران ظهور مهدی موعود رو به عقب انداختیم
دلیل اصلی بمباران تاسیسات هسته‌ای ایران به عقب انداختن ظهور بود
اونا نگاهشون آخرالزمانی هستش
@News_Hut</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/news_hut/71570" target="_blank">📅 15:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71569">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d522fc2430.mp4?token=cAAEdZTFPJ4vICtfg278BLKLUEiA2UKp8i6XH491KBwFqdz4ZYiTge7qcqHxqFKDMnDi3w96Mw_w1GN7n-I2FjDvzaQpZsz3Ur9gpM336yd-cNU8uwl1gLBWjqZBeBkaYCLtDZ7v7kv7Hj98bmMHznvyt4G6w20WjhDRmFzuSJe6dpjXicMq_0OA56-EgpSuEjAXvx0D2pHvHLn9hWoWnKeyFVFRs-DG7Slv0lsA08LnrrxiDAKgdhrj0qGXPVgHkAJQG-t2VLccUuD6HnNfQDMLnb33yYCXoszAnjeO0bZT8lrSS0fg4oX0vYLcDaXBscDls0oQeRHtK0Bmm0D4RzSDinXB2rXae08HrWUoHH4Un70GtuSWwd5rla5yd6O1sQ_Q2vBzzr-bour1jJ-yI8GSpLxQwByB9H0f4YiLVDW77SHYeUknAlS_8eHkqAA6IixrOJVMyPhRyI-AkXEksbY4_mxp-DRzSfEyYaFtYLCwZFDvojlmlMXUydijlwzV9O8JnvK650wtCpiR1_zBZB3-n-JGbqczhDp-ZKVCodqAJ9NiivironV9cIPtrjNTxY7JOM2-h8cHhUTP5dJL_iE_Q8O0EO7wGfT7m4Qg2bIFhxl-8Tu9HarM32-Nbh_6lXyw_GaJnViNA-pLDz-SDRAdT4Q2ZXkbiVxfbCDR1og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d522fc2430.mp4?token=cAAEdZTFPJ4vICtfg278BLKLUEiA2UKp8i6XH491KBwFqdz4ZYiTge7qcqHxqFKDMnDi3w96Mw_w1GN7n-I2FjDvzaQpZsz3Ur9gpM336yd-cNU8uwl1gLBWjqZBeBkaYCLtDZ7v7kv7Hj98bmMHznvyt4G6w20WjhDRmFzuSJe6dpjXicMq_0OA56-EgpSuEjAXvx0D2pHvHLn9hWoWnKeyFVFRs-DG7Slv0lsA08LnrrxiDAKgdhrj0qGXPVgHkAJQG-t2VLccUuD6HnNfQDMLnb33yYCXoszAnjeO0bZT8lrSS0fg4oX0vYLcDaXBscDls0oQeRHtK0Bmm0D4RzSDinXB2rXae08HrWUoHH4Un70GtuSWwd5rla5yd6O1sQ_Q2vBzzr-bour1jJ-yI8GSpLxQwByB9H0f4YiLVDW77SHYeUknAlS_8eHkqAA6IixrOJVMyPhRyI-AkXEksbY4_mxp-DRzSfEyYaFtYLCwZFDvojlmlMXUydijlwzV9O8JnvK650wtCpiR1_zBZB3-n-JGbqczhDp-ZKVCodqAJ9NiivironV9cIPtrjNTxY7JOM2-h8cHhUTP5dJL_iE_Q8O0EO7wGfT7m4Qg2bIFhxl-8Tu9HarM32-Nbh_6lXyw_GaJnViNA-pLDz-SDRAdT4Q2ZXkbiVxfbCDR1og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇾🇪
تصاویر بسیج قبایل حوثی، ستون‌های طویلی از خودروهای تویوتا (تکنیکال) مجهز به سلاح را در بیابان به نمایش می‌گذارد؛ تصویری که نماد کلاسیک جنگ یمن است.
قبایل «بنی‌حشیش» برای پیشروی به سوی «مأرب» — آخرین پایگاه عمده دولت در شمال — اعلام آمادگی کرده‌اند.
وانت‌های تویوتا مجهز به سلاح، همچنان ستون فقرات نیروی زمینی حوثی‌ها را تشکیل می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/news_hut/71569" target="_blank">📅 14:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71568">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRCZJIJuQWtzaUxPAoL_6TT8UqFzw9B-EEvM19uEXfeEDkWc6E2ty_joRTlcX2YYNYsVAoMfZuLedG3BIRLFKphQlfjx9NjmwgAGIgNT5jjesjmFBVZnQ4aCX79YODsjO2BJd0Yw1goqYiofoK_WwUmVSp-Bog_OEIMHe83XbiZSnmMKqcTHywa3SjF53gozJGVONOc4oV3yde9C7GnzDY77cSWCK-tz1jb0qgdid638H5xRTMRJDdDsoCJeXGkao-ds2Q_E4jp1twGEGzsB0lawMSjxMUd6cGEf-CguQ98yCHQWkKpcJoXPX_P1dSXu4OCQr-VoU4kGALpMHa1HrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
اکسیوس: محمد بن سلمان، ولیعهد عربستان سعودی، روز پنج‌شنبه دو بار با دونالد ترامپ، رئیس‌جمهور آمریکا، تماس گرفت و از ایالات متحده خواست تا هم‌زمان با پیشروی حوثی‌ها به سوی یک نقطه راهبردی و حیاتی در دریای سرخ، به آن‌ها حمله کند.
ترامپ این درخواست را نپذیرفت و مقامات آمریکایی اعلام کردند که در حال حاضر هیچ برنامه‌ای برای مداخله مستقیم علیه حوثی‌ها وجود ندارد.
دریاسالار کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، نیز روز پنج‌شنبه برای هماهنگی‌های اضطراری به ریاض سفر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/news_hut/71568" target="_blank">📅 14:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71567">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363bcb9915.mp4?token=eHcCaHwzZNauaXrVghd8dA7RhBYdmqssfex8Z6vYxWQkwsw3B-yLcFNNYR6K4w5U2ImFxMir8I8VqrFdkvkD-p3sh7h1V2Pnhp1H0iFGvC50GRJY-mEEhbrib_e_VqSN3xyX6APmvpPNzhq7MFXPAqIrQ12oomnPTNgO3hgw1R974Z9Ap8XkJecp87hlEkjgdEXIY4MUkxGtMkVoEzcEaqB9N6YzCLIDUKLPr6pRAAZo1IDscceyBWFQ2tOnDazFtBDR1OJ0xztumBb2d9uIM5VTts_nF7tIpXPFAbJnjmoEVxQQv2Sm98__F-l8Rhxxd1c2yt7TWjNp_E4pz8mWoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363bcb9915.mp4?token=eHcCaHwzZNauaXrVghd8dA7RhBYdmqssfex8Z6vYxWQkwsw3B-yLcFNNYR6K4w5U2ImFxMir8I8VqrFdkvkD-p3sh7h1V2Pnhp1H0iFGvC50GRJY-mEEhbrib_e_VqSN3xyX6APmvpPNzhq7MFXPAqIrQ12oomnPTNgO3hgw1R974Z9Ap8XkJecp87hlEkjgdEXIY4MUkxGtMkVoEzcEaqB9N6YzCLIDUKLPr6pRAAZo1IDscceyBWFQ2tOnDazFtBDR1OJ0xztumBb2d9uIM5VTts_nF7tIpXPFAbJnjmoEVxQQv2Sm98__F-l8Rhxxd1c2yt7TWjNp_E4pz8mWoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کنعانی مقدم:
اگر رهبری اجازه دهند، ظرف ۲۴ ساعت از سلاح هسته‌ای استفاده خواهیم کرد
خرید فیوز هسته‌ای از کره شمالی، کار خیلی ساده‌ای است و ۵۰ تا فیوز می‌توانیم بخریم
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/71567" target="_blank">📅 13:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71566">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67e4c7321.mp4?token=qrZ1j8E8z--WK-8pg1kvEvcdrgJyA5ASnrujxv3_0GkaFYioIbRrD9zCe7UsZ07j4Z0tomhaURvXcjO7yCL9-bmTwODHXkWUY8ZQRYoIGG5mwaHH1W7cg3-h8XeWJhl1GYUJsH0V7MnRMkvUi1YhecFSIFkI-u1uHO4CS9-t61T6-xw218mh5ijQRlRXcxYt-p1cdyohsqOlf3ksigVyvNwQrTOkeqi6kUmizJ6RNjxIq8FgNtxcSzpghM1GAJu8dejey8nmf0d0TlZhauWxMebq71giqxtYyfTGcNC0dirBCERoY7s8ik-fJDMlPmQ8NUkijYNHtmIcKUhadTD8DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67e4c7321.mp4?token=qrZ1j8E8z--WK-8pg1kvEvcdrgJyA5ASnrujxv3_0GkaFYioIbRrD9zCe7UsZ07j4Z0tomhaURvXcjO7yCL9-bmTwODHXkWUY8ZQRYoIGG5mwaHH1W7cg3-h8XeWJhl1GYUJsH0V7MnRMkvUi1YhecFSIFkI-u1uHO4CS9-t61T6-xw218mh5ijQRlRXcxYt-p1cdyohsqOlf3ksigVyvNwQrTOkeqi6kUmizJ6RNjxIq8FgNtxcSzpghM1GAJu8dejey8nmf0d0TlZhauWxMebq71giqxtYyfTGcNC0dirBCERoY7s8ik-fJDMlPmQ8NUkijYNHtmIcKUhadTD8DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎯
ویدیویی از هدف قرار گرفتن نیروهای انصارالله توسط نیروی اسنایپر مورد حمایت عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/71566" target="_blank">📅 13:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71565">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0000373bd7.mp4?token=i3Ks90fpRi1db52xpdk65WNXG3OtqXvGzCvB00r5mHegXYSsgn51F_RuWghyxrW2P_pOwPWA2zqSnfsjyAXcq3xgIKmTKDcXqB66iqGyANyMTr-8rO1UIfzfpP2piO5g_zuduCzaYnA7uhGjWfTxDYXtfSD84iN1JPDGr7_Yxy0qP5_nqKKMMQHsdeUU9XXqmzBEiiXzXUcI4-QFvZH1AgHTVUp1k73A2u0jNMgN_bb3HXfeSIZxzGtByHTVUqcpXHN5gg6TMfpyfmhxaMT1cwfLp_BPbYQI8bQs-EtwOenHIzmPUIkMH0vlwa72JnfEDlJpjyZtGaQZx8STEtDncA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0000373bd7.mp4?token=i3Ks90fpRi1db52xpdk65WNXG3OtqXvGzCvB00r5mHegXYSsgn51F_RuWghyxrW2P_pOwPWA2zqSnfsjyAXcq3xgIKmTKDcXqB66iqGyANyMTr-8rO1UIfzfpP2piO5g_zuduCzaYnA7uhGjWfTxDYXtfSD84iN1JPDGr7_Yxy0qP5_nqKKMMQHsdeUU9XXqmzBEiiXzXUcI4-QFvZH1AgHTVUp1k73A2u0jNMgN_bb3HXfeSIZxzGtByHTVUqcpXHN5gg6TMfpyfmhxaMT1cwfLp_BPbYQI8bQs-EtwOenHIzmPUIkMH0vlwa72JnfEDlJpjyZtGaQZx8STEtDncA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
این رهبران جدید و رهبران واقعی که رئیس‌جمهور ترامپ از آن‌ها صحبت می‌کند، چه کسانی هستند؟
🇮🇷
پزشکیان:
به گمانم باید این را از خود او پرسید، چرا که هر روز حرف متفاوتی می‌زند.
یک روز می‌خواهد ایران را نابود کند و روز دیگر می‌گوید ما دوست ایران هستیم؛ یک روز می‌گوید ما را به رسمیت می‌شناسد و روز دیگر می‌گوید ما را قبول ندارد.
بنابراین، ما مطمئن نیستیم که باید کدام اظهارنظر را بپذیریم و بر اساس کدام‌یک عمل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/71565" target="_blank">📅 12:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71564">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71564" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/71564" target="_blank">📅 12:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71563">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4eYwVEm7Pa9hFanOE-glFn_GiuG1iPmpVTQ7FfMlxglDaAaoYWbjd4ZWreNmqmDcLT_ShGTGGJS43CRrB56Zt0cjns2SRRRABOGO1IlC8BRDj-HisQ-WmTe9j6G9DUTlaT6xWQFmmlC3qB0nAic3JUIhwyAcDVC-upQ8wn-JlV4ByxZhift8VrD5zB59a9rKwQzJ-VIbmODeo8siaYsXhmp6kQ_7cPEYJApPGaKSCqt1ttGnxBc-6pJfoYeVzMAPNr88wv2DodvuZvsbRW-l8gbv4AjAEDqldBd6JM5L-w_AOVFlWXz0FyE3IMjt1R2piH7t2O3L73kaSD6emqP1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد بزرگ منچستر در راه است!
نبرد هیجان انگیز
⚽️
منچستریونایتد
🆚
منچسترسیتی
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ دربی اخیر منچستر:
⚽️
منچستریونایتد: ۲ برد، ۲ تساوی، ۱ شکست و ۵ گل زده
⚽️
منچسترسیتی: ۱ برد، ۲ تساوی، ۲ شکست و ۵ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/71563" target="_blank">📅 12:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71562">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaRvadwEeb8wKN7pRj3G-8g1txTgAhotpYyvKijSTFvpbBSpZ7khFj0k4kcRfxtXNgZ7UcKrPsgRtjbrF7SWhd2kAxHvP6upmXlU9tJpLyZmfGBuYMN9Z3r_tLO5cvXpk9oNKB7p22efvLaE7As-QPmm100b486FPra1FFJ9SHMcBcgB9oIo13mQ8-dKFb5uiNdBogHtNugavbFiq-gdYMDcJdou4BCxbEiktBZbo1iFWbBS6PEnFb2FtZNF_lANfEQp2u2HjUw9myWEWDVqdDUOxW1pmRSWsmiC7LpqHT-3eXykx5qRhLst_-IVJfvsk8smIGVnQHMY0XVfBX9XlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
روز یکشنبه در گزارشی اعلام کرد که بر اثر اصابت یک پرتابه ناشناس به شناوری در حال عبور از تنگه هرمز، در آن کشتی آتش‌سوزی رخ داده است.
این سازمان اعلام کرد که مقامات محلی در حال کمک به تخلیه خدمه کشتی هستند. در این گزارش، نام شناور یا اطلاعاتی درباره تلفات، خسارات و یا پیامدهای احتمالی زیست‌محیطی آن ذکر نشده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/71562" target="_blank">📅 11:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71561">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇷
🇯🇴
ویدئویی از پرتاب انبوه موشک‌های رهگیر «پاتریوت PAC-3» از پایگاه هوایی «موفق سلطی» در اردن در سه روز گذشته، برای مقابله با موشک‌های بالستیک ورودی ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/71561" target="_blank">📅 11:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71560">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c7237eb3.mp4?token=l4dTAJfhQybP3i2Zyv7jdH2LCqton29PTGaOd9z2_xDSGI6DDOE9--LOcfF2ULasqZnNspe58fSbH4LtbYPuftABpLCakjB7Jp3ZAYxpCwtbdbLg208YJWx7Ms6xBTwFXpUN4UaxI5a-b7HL2Dm-rGObbXJMUTxX4pX02Umxh86MT-k9iY2XvdXYn8A8j4BDSKCWdEBgsYqrPRVTRrxCII8rifNwcl2hbG-_NBChGry-D7cvydQKWQSUXjI6zZAU_1HWz-IgZYrYAu5czyWhq3oz4nreI5U0qTBG_KoMsZLJvPyb2F34GPDp-BC3tu1pt9J0p3hC5AHkMAlFZQ5pTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c7237eb3.mp4?token=l4dTAJfhQybP3i2Zyv7jdH2LCqton29PTGaOd9z2_xDSGI6DDOE9--LOcfF2ULasqZnNspe58fSbH4LtbYPuftABpLCakjB7Jp3ZAYxpCwtbdbLg208YJWx7Ms6xBTwFXpUN4UaxI5a-b7HL2Dm-rGObbXJMUTxX4pX02Umxh86MT-k9iY2XvdXYn8A8j4BDSKCWdEBgsYqrPRVTRrxCII8rifNwcl2hbG-_NBChGry-D7cvydQKWQSUXjI6zZAU_1HWz-IgZYrYAu5czyWhq3oz4nreI5U0qTBG_KoMsZLJvPyb2F34GPDp-BC3tu1pt9J0p3hC5AHkMAlFZQ5pTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
نظرات متناقض هادی چوپان درباره هانی رامبد:
بعد از قهرمانی
بعد از جدایی
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/71560" target="_blank">📅 11:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71559">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097559287c.mp4?token=M8BQDzaxOr6A4KapiV79BKl6CqBANJCn5hJws7kqIO94HQMN6bjrU-oyeQTSRRKWO32Xy0oR_rZC5ks1I5UGUJUl4-upMYEEO4dSKAyHPvJLyBtUCDal0ZOd2q41FEw7-P_X2wA1Tslf9OmRcE6pf25VlpBy2K4wUsfUaVmvtn7N0JUKNhQdrvkgZqFBN1MYb-9r6JCS6tpIVxKYWYYprem4vTvz-yAjyoD5hL-Tszhxf9lNY2_lZ1YD2jLotxmeX5oePG4vxs_Te9pUPwatkUOZOTlrYkPzq-Svx0o0odcUQToWCoyWGUfaR3ecLAKuCfwefXIy5okDJZjcrRMPGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097559287c.mp4?token=M8BQDzaxOr6A4KapiV79BKl6CqBANJCn5hJws7kqIO94HQMN6bjrU-oyeQTSRRKWO32Xy0oR_rZC5ks1I5UGUJUl4-upMYEEO4dSKAyHPvJLyBtUCDal0ZOd2q41FEw7-P_X2wA1Tslf9OmRcE6pf25VlpBy2K4wUsfUaVmvtn7N0JUKNhQdrvkgZqFBN1MYb-9r6JCS6tpIVxKYWYYprem4vTvz-yAjyoD5hL-Tszhxf9lNY2_lZ1YD2jLotxmeX5oePG4vxs_Te9pUPwatkUOZOTlrYkPzq-Svx0o0odcUQToWCoyWGUfaR3ecLAKuCfwefXIy5okDJZjcrRMPGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
تلاش ابی برای بوسیدن دست یکی از بازیگران برنامه عشق ابدی که ویدئوش به شدت در حال وایرال شدنه!
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/71559" target="_blank">📅 10:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71558">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427cd49fec.mp4?token=IozFKnLVQtjleAst_awlqq0ulzkUiZS3e8dKVkMf6ROZPGLk5URu00jO9vMvsmYODPU-wx3fzMLI0OMpAbnaG04HlYypntEZNMBp_P4AYz2W44ylzRI4HNB0i0MzMzXyV3GpdAQsiB2qZLft6PRnAPgnwDUbVBCpeYY79zMRD9u-ZWkCPYY6ZUIRdWncCKOdgzAxlkesW7SvuNbeutV_ezIQXrLyNmNhEv3ivSu3Nty13bg70Nbsb7PURdUNjFP6iKIUiSfGcwzkvxAbz_GHmrlJPvE1Mjjr0pjKnbgm447RnOZfvHBCngzFUEsjz2xK4i2qkwnkUwIFlpHmBOn5uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427cd49fec.mp4?token=IozFKnLVQtjleAst_awlqq0ulzkUiZS3e8dKVkMf6ROZPGLk5URu00jO9vMvsmYODPU-wx3fzMLI0OMpAbnaG04HlYypntEZNMBp_P4AYz2W44ylzRI4HNB0i0MzMzXyV3GpdAQsiB2qZLft6PRnAPgnwDUbVBCpeYY79zMRD9u-ZWkCPYY6ZUIRdWncCKOdgzAxlkesW7SvuNbeutV_ezIQXrLyNmNhEv3ivSu3Nty13bg70Nbsb7PURdUNjFP6iKIUiSfGcwzkvxAbz_GHmrlJPvE1Mjjr0pjKnbgm447RnOZfvHBCngzFUEsjz2xK4i2qkwnkUwIFlpHmBOn5uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئو وایرال شده از 9 اسفند - روز شروع جنگ و بمباران تهران و واکنش  دانش‌آموزانی که خرکیف شدن
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71558" target="_blank">📅 09:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71557">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🇮🇷
امیر تیموری فرماندار شهرستان قشم:
یک کشتی تجاری حدود ساعت ۵ صبح امروز در محدوده جزیره هنگام و ساحل شیب دراز جزیره قشم مورد اصابت قرار گرفته است.
در این حادثه  یک نفر شهید  و سه نفر مجروح شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/71557" target="_blank">📅 09:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71556">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBgwnoR2pVSwXuwG1_7sRDK0F3EjMGNy-smuYjNvu5pyiK4TQ_RjXxJ5i15aGH-Fjj08xwuKL0n7RrJXbzdO-7ln30ipCoenaxfNiJmAIe9dlpVtyspXkJFUwZJFSXu8FUjzjCY1KlAUYHIU8XDMw4VUN_VPre80X9YyTV0-No3_A4YZ-84FTUCXlQWVGH1mh_U7f7GF_cuCVTJPROmf6o-dAlt4A-HCdCOp1OAeS792YjIbI_X-ycgE_MG5OGkQHmk7InOA79vF_9eJddLQkQk4AJ-ogdIYocEzLpXS5x2Azy5zv2yk-o79VRqBTwpMFbMMTAnsSMIQd2_beEhrvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇮🇷
📰
وال استریت ژورنال:
مقامات آمریکایی می‌گویند ایران پیش از حمله موشکی بالستیک ۱۷ ژوئیه به پایگاه هوایی «موفق سلطی» در اردن — که منجر به کشته شدن سه سرباز آمریکایی و زخمی شدن چهار تن دیگر شد — تصاویر ماهواره‌ای با وضوح بالا از نهادهای چینی دریافت کرده بود.
این مقامات معتقدند که تصاویر مذکور با این حمله مرتبط بوده و احتمالاً به ایران در شناسایی دقیق‌تر اهداف ارزشمند کمک کرده است.
آن‌ها دولت چین را به مشارکت مستقیم در این حمله متهم نکرده‌اند و هویت نهادهای چینیِ دخیل در این ماجرا نیز مشخص نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71556" target="_blank">📅 09:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71555">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🦖
2 چالش، 2 کد مخفی، 2 جایزه 1$ در سایت بین‌المللی TREXBET !   فردا در دو زمان مشخص، عکس‌های چالشی داخل استوری کانال منتشر میشه؛ اما کدها همین‌طوری به دستت نمی‌رسن…
👀
🔎
باید با دقت بگردی، Promo Code یک‌دلاری رو پیدا کنی و قبل از بقیه داخل سایت ثبتش کنی! …</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71555" target="_blank">📅 01:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71554">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uI4KODdw0np8bFpp2qTPkQ5BfRlSYaKDX_oYXwjOb8MHpVT0BkGxoj07X6kFxw5jgfeyQuK_OqsgS8L4IeNUFupIP_aP03LvtM7OGWvUVz81k4Bw53QjUgb4-hG8FywT_fW-PV0hDDGAouiWgtkst9-RLDqTyTUeeAoeOWjFnQFqew4nScoLEkFdv2VGhXiwi8FQAX_5OpJAdzeTA7oiWFLMP-cOFkOqRTxRRhQO4ceiT6VJZt6pXKjJ5MOQFW01_AoAZ1_Wdox72pV_4vM4HF9XxelgzuY_FGOuY8VH1VmuybtlNzWx_6IVpV5rvLCCxxaFIjJzU_Xm9AphgPueEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
2 چالش، 2 کد مخفی، 2 جایزه 1$ در سایت بین‌المللی
TREXBET
!
فردا در دو زمان مشخص، عکس‌های چالشی داخل استوری کانال منتشر میشه؛
اما کدها همین‌طوری به دستت نمی‌رسن…
👀
🔎
باید با دقت بگردی،
Promo Code یک‌دلاری
رو پیدا کنی و قبل از بقیه داخل سایت ثبتش کنی!
⏰
چالش اول → 18:30
⏰
چالش دوم → 20:00
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71554" target="_blank">📅 01:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71553">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad61e1e00.mp4?token=XWVjf2dPapHfvDJya118UZqFKHDCzZBcUJZZ6nmJlXaDCSr01wktYjcfdSb2NDP64vwyYqPPK0SGh7NXWP2lwnPrbx5V6QDRkvS_V-dWDmirBpdRF09DvncB6mZt8CtVjpFJ56BkvvSoTIxiF-AxF63-WWNDhb7k1CC41-5yo_6DKlSuFO4PK46bhA5Sh3qWflNWceTj44GPns5xpEC1GYguHlmRXF00gNj2P0q3ayssNexRt5nB7hJWHPBZ3yfnms0cgbd2qIIVQ4g66b5gcXBgCoWrCDRVP-WYbXu6s3NgbI3nAh55_OqJ8iOJeJ5dXonhyFouTej3zbhysK2xHFKsoJXsOMb7ntw-L_DR7yjH9cyEpnmif24zKYLAmStIQ-8UB3zqHG5JNV-DJaP1u1TTKvm3QwKlaljKFqSYOy9W4XytgW47i_fNMPwq2hmTgxvuNeD8RovLxX0bIs2UjrSizwa-NFAHfZWnfLcTBdu3KcDd8nae9ILOi9FtYOwX13uQzIR55aezqYRqjGsVbobNPDlNQlMj32gv0EhRKvvYWCJbfQPZqWJcJF5a_mlfM0b_ldYgosfjVKjTlesL6Gbmcjse6mWvR-wYFUoAc5R6LA4EXthPMkeR5IP4YiyY750OvzWXZflYV-yUrKBP5204vnCbFeGkbG2i-_ItDlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad61e1e00.mp4?token=XWVjf2dPapHfvDJya118UZqFKHDCzZBcUJZZ6nmJlXaDCSr01wktYjcfdSb2NDP64vwyYqPPK0SGh7NXWP2lwnPrbx5V6QDRkvS_V-dWDmirBpdRF09DvncB6mZt8CtVjpFJ56BkvvSoTIxiF-AxF63-WWNDhb7k1CC41-5yo_6DKlSuFO4PK46bhA5Sh3qWflNWceTj44GPns5xpEC1GYguHlmRXF00gNj2P0q3ayssNexRt5nB7hJWHPBZ3yfnms0cgbd2qIIVQ4g66b5gcXBgCoWrCDRVP-WYbXu6s3NgbI3nAh55_OqJ8iOJeJ5dXonhyFouTej3zbhysK2xHFKsoJXsOMb7ntw-L_DR7yjH9cyEpnmif24zKYLAmStIQ-8UB3zqHG5JNV-DJaP1u1TTKvm3QwKlaljKFqSYOy9W4XytgW47i_fNMPwq2hmTgxvuNeD8RovLxX0bIs2UjrSizwa-NFAHfZWnfLcTBdu3KcDd8nae9ILOi9FtYOwX13uQzIR55aezqYRqjGsVbobNPDlNQlMj32gv0EhRKvvYWCJbfQPZqWJcJF5a_mlfM0b_ldYgosfjVKjTlesL6Gbmcjse6mWvR-wYFUoAc5R6LA4EXthPMkeR5IP4YiyY750OvzWXZflYV-yUrKBP5204vnCbFeGkbG2i-_ItDlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🟥
گزارش فاکس‌نیوز:
جنگنده‌ها از ناو «یو‌اس‌اس جورج واشنگتن» (USS George Washington) در حال برخاستن هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71553" target="_blank">📅 01:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71552">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEo_jk_YzPIwW9VJA36CCG1whM4HDklxY2UnceDmV7xyZhNgjE3tkdVsPmsPDOz7eDy4jSVJpdcwqzebWc3ejz12E7WDWE_6wKpyNs88QJDWB8p4bUQUC6OuwdYYL2CzwTCuTowq3NC3JnJAKAm8FpI0kFQtewR54fLFAubqG-kMsx2usJHWAYVE5L7C6ECU5VLwbARZZnWODwL-7rQR958M4PP7qVppxgftrl99ZWAvEUwFLxLZqmOJKsseHQY7vJf64zQZofKPD1AJGdEw0wzU92m31a-MSXDr2n4ztBMgMbSAgXUa45wtfkh4pCg0erhsYE7j1ZKrn9tvWmGQhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوری
؛کانال۱۴ اسرائیل:ایران برای خروج از پیمان منع گسترش سلاح‌های هسته‌ای (NPT) و آزمایش بمب هسته‌ای آماده می‌شود.
حاجی‌دلیگانی، نماینده مجلس، از آماده بودن طرحی با قید سه فوریت خبر داد و افزود: «باید هرچه سریع‌تر آزمایش‌های لازم برای سلاح هسته‌ای را انجام دهیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71552" target="_blank">📅 00:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71549">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_pB17JBreSLNDp78-YcPC5S-ZMrgnTJXx1a0bJ0MmLpSqobCMqgVppuqrrh05SX5Vw9jYndYjvskVCQTNLHP4JqXK0BgAqAFJrNoXN9ITXUECv9uaaFEiNs_X9wpUso9pER_-9EXFqo-cuAWMor_1TS-R87m61ToCHSUjiExGFwLDdrh1t6j5LGdyo1wW8ijTi2VrXMVAIAenT5ZJ-6L143qgL8NU-hNkZqTV6D6EX5CDFUMpDUfPP6ieBEicyi4CytfZtpNmxonUaNEDFCAVxgHejDohI2iArdU2fW_YChGui8swoSZK6OkqieUaNMSvBAuUkJn3BNeyFIDza-6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ddef7d0b.mp4?token=W6BQSa3kqjithhwRsJsxdWnbWGcXELts1LjAnlE-iAE5iWgg94Mr4yTB6L4OXp49wLLGOKa3ev700et3HFwkf3d4MPBpFHLVa-FGBU6TkkRM-2SHaIAov29uRDOtua5O7Ng4HpjzXouNFiD1sTdkgO_MqRm_3LGXA020UdeH8qHG1HKdOspESB-c9FFyeaw_rOBgA_AEs6jgIPBN1n26dc85QFpAhbXm22fPNjf6FbxvBz165GYET2VBdmZHqetWWwUB89xlQqmwPW4SoCvLRC5_URUGROSUl56bxupoKNg4suj6qgECYGI_rTf6vYM8o_nM3v3m1QGt9SQe5wVkhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ddef7d0b.mp4?token=W6BQSa3kqjithhwRsJsxdWnbWGcXELts1LjAnlE-iAE5iWgg94Mr4yTB6L4OXp49wLLGOKa3ev700et3HFwkf3d4MPBpFHLVa-FGBU6TkkRM-2SHaIAov29uRDOtua5O7Ng4HpjzXouNFiD1sTdkgO_MqRm_3LGXA020UdeH8qHG1HKdOspESB-c9FFyeaw_rOBgA_AEs6jgIPBN1n26dc85QFpAhbXm22fPNjf6FbxvBz165GYET2VBdmZHqetWWwUB89xlQqmwPW4SoCvLRC5_URUGROSUl56bxupoKNg4suj6qgECYGI_rTf6vYM8o_nM3v3m1QGt9SQe5wVkhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
درحالی‌که شرکت اپل ایران رو تحریم کرده، قمی‌ها طی یه حرکت عجیب، همزمان با مراسم معرفی محصولات جدید اپل، خودشون هم به‌صورت جداگانه یه ایونت برگزار کردن و از آیفون‌های جدید این شرکت رونمایی کردن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71549" target="_blank">📅 23:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71548">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac8d39358d.mp4?token=TXpnDMUGlslTBMSXberwThFq30XwvwRO3VVYVn4AHVBkoCbkP7jopMpVAtWja0RrmgNfIA5FFl4a4bJQkaG6n-Gzh_6IWiCjPcETMW7uCb2_paLgsmAZXgmdbuGkhoxF9RK0YqhLxz5mzM8quJv_25kMrq5kyzULmxgnnx-3H_N6-vscaMez1pTEfZkSmXOyFfun9zYP8MV4xTr6XDOA3-wyOK3CX2qcPuPoCL2r_AjBs4Do7w5DLrEhcBvIkJDM5ClzIz_ugVpnD4LmbAegYJVYEN9hXxC4NfzdUk5FGk8GaXaRZfJ5diDcSO1-ON_LejbjuZ1NJvt59gSmT-5bnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac8d39358d.mp4?token=TXpnDMUGlslTBMSXberwThFq30XwvwRO3VVYVn4AHVBkoCbkP7jopMpVAtWja0RrmgNfIA5FFl4a4bJQkaG6n-Gzh_6IWiCjPcETMW7uCb2_paLgsmAZXgmdbuGkhoxF9RK0YqhLxz5mzM8quJv_25kMrq5kyzULmxgnnx-3H_N6-vscaMez1pTEfZkSmXOyFfun9zYP8MV4xTr6XDOA3-wyOK3CX2qcPuPoCL2r_AjBs4Do7w5DLrEhcBvIkJDM5ClzIz_ugVpnD4LmbAegYJVYEN9hXxC4NfzdUk5FGk8GaXaRZfJ5diDcSO1-ON_LejbjuZ1NJvt59gSmT-5bnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
لحظه‌ای که جورج دبلیو بوش خبر حمله به برج‌های دوقلو را دریافت می‌کند
جورج دبلیو بوش آن صبح در مدرسه ابتدایی Emma E. Booker در ساراسوتای فلوریدا بود و برای دانش‌آموزان کلاس دوم در یک برنامه کتاب‌خوانی حضور داشت.
نکته جالب این است که بلافاصله از جا بلند نشد و کلاس را ترک نکرد. چند لحظه در همان صندلی ماند و سعی کرد آرامش خود را حفظ کند تا دانش‌آموزان وحشت نکنند.
چهره‌اش به‌وضوح تغییر کرد و حالت شوک و نگرانی در آن دیده می‌شود. دانش‌آموزانی که آنجا بودند بعدها گفتند تغییر حالت چهره او را به‌خوبی به یاد دارند.
جالب‌تر اینکه او حدود هفت دقیقه دیگر در کلاس ماند و بعد از پایان بخش کوتاه کتاب‌خوانی، از کلاس خارج شد و در همان مدرسه برای خبرنگاران صحبت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71548" target="_blank">📅 23:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71547">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e621bd826.mp4?token=Lmum7MK4gVHw0k9n5MVrFnJBLXoEIkGanWEe1u0QE1PRSdZG0xisAswLs-B1VpGLepD3Hbh9lV3pxYMglMtyOq6A8jtvA6Vg8urvd5caxltL8X2LjkIN8OVjQCAvjVYV8_7qtRdoIv3-OoyhLG0oGt59wLkG6nVUYAThjQxtJvK2wJ6-u0NJeKwelhCWAaZMmy8H0E0zdvxklhBFmQeWyL5_Zu0cl241AM3wVRTyAggQO_VtIVmCT_ei33OaQzeidiBcD3FyM9JcbdfUP-U9fewYfLA0k8wADUxSJRomo3JgJyO83B9J6RyjoYJbXfBAV2DIonJ_lVuH2FxhEMD-FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e621bd826.mp4?token=Lmum7MK4gVHw0k9n5MVrFnJBLXoEIkGanWEe1u0QE1PRSdZG0xisAswLs-B1VpGLepD3Hbh9lV3pxYMglMtyOq6A8jtvA6Vg8urvd5caxltL8X2LjkIN8OVjQCAvjVYV8_7qtRdoIv3-OoyhLG0oGt59wLkG6nVUYAThjQxtJvK2wJ6-u0NJeKwelhCWAaZMmy8H0E0zdvxklhBFmQeWyL5_Zu0cl241AM3wVRTyAggQO_VtIVmCT_ei33OaQzeidiBcD3FyM9JcbdfUP-U9fewYfLA0k8wADUxSJRomo3JgJyO83B9J6RyjoYJbXfBAV2DIonJ_lVuH2FxhEMD-FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو مشهد اردهالِ کاشان، از " نمادِ مشت گره کرده‌ی علی خامنه‌ای " رونمایی کردن ولی انقد بد ساخته بودنش که صدای طرفدارهای حکومت رو هم دراوردن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71547" target="_blank">📅 22:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71544">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qKYqgh1QM4KBwE4qlApLz3M4OKw2C2t_Qjju19fs-0q9RnP4tLn6H4ijm27QgVrj7hde1-n0rpctI8Y1rcrNJajY-RJBwrTks1ld-Mm86eX-mkToKkW6E421KcbFQWQDOCVgeOCNDjOZR7lwKkJGw-MVL1XzuEcwcmHhJe0yBx9kzSLdyg4gmzO6EEpMp9UAypnyuV_s1PMbXMsLL1S35bFxdseeEFf-oHHBraxQswyIMUesC9AYDHw0M42fR9SgvzqV1-cAkR4f03X3Wlyih-n5GNgNLruB_NERS4FyFOLSZeacYqvYnKUxjH4syFFM0TFTJTAvPO9USTAX7_yTLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ehp-GWeYkLyLx81OyQMaKX1JxwcnZNZULO94GIIoPVb2OhWIvmQASvHmtIuND8d6BCw-h8MV7o3IeI5Yp4ZQz-ZHjgwpE80nt6947iZ0CUO7r1qDhHf4qLzw4Vw_-EoE9bU77VUd9twUkN79kKBqdx6mx4nZDnR9l0_3kiGVHHkM-4Az5x7Fh0QVZn2UUm2ZY0clWy_wQOVOzkCiYlWneuUSIIMvQnOZ1GnJKJy30_CzJkewmipH7FWJeNKddxW6aP8KlbiIDceC0lSvbE5KxvbTz0_P_tpV_8JnwhN-hP9f-yYonNHjg9oYm8N0S5PNHSfY0lXm5emuwTvd17wQxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qu2XJKhCzdj-F9eu6LF-9FknqtYx5hw1ilL3hB5_6AQP2zqp1M6B-tS4fcWlOYnqGzSkZsHvKYUdMFTyZrYhvTWNzgFmTqYXRV5hpNJ_mhrvoGvBuZnn73xhu4lhyZWtYc6aEJugBMtEEzXpus-wCAPX4vLvgQBpkjA150AaGs4eoQuYuK7WcUe50YRfuoLbETj583AmO-8u-uRCwLb17SWkdilMPmVE6Oz1sf9S5K5PxBRdASSwj2XDID2uE1R3H5DAC4S6EWCx19aYrYgMbnF9J1fPjMOa6-wryN-bNFlxO8S9s_Tvb7_GI-e5W7oKKVMEeUUvhydXE0hw4sEXyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚠️
کشتی‌ها و نفتکش‌های آسیب‌دیده ایرانی در خلیج فارس.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71544" target="_blank">📅 21:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71543">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
شلیک یک موشک/پهباد به سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71543" target="_blank">📅 21:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71542">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-O0QuWigpruDFjh3UUzD-qk3DP-g3UFQl30MB5TxcBvfVo1cwuX_v7mzGLYxEjHm_S36zRfgRVnHlUhaxxhnFxsMpSyW8yS1e_6R74aAshLaWh8CVIB3mezowWo9NmCm1wVsvdiaUD5cIihW1SA8w-NMHDmwMcR51OJVdkb44fJbjnN_h7tvj3xnFSiSdploHAi4Dim-z_KT9jzTvHAUhGlK6n_s26tJal5OoMiI5hHBUfQmkX4_TI9p_c9xPLU3OLd8KUdWDmvfWAiWHe1KspSLxuDKEiQs09JJ8h1jLQdYoRDM4PxDjgpGRTjFhaFQiQgWyWgO_p6yPY-Vn2fjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
شعار جدید عرزشی‌ها برای حسن روحانی
😂
نهپاد: نفوذی هدایت پذیر از راه دور
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71542" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71540">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a60a908ab2.mp4?token=eYgvVlI6tzsDl-u6tIJMiOqQTZ2RsyCCs6mtYUnX2DfHCzz_N_P1S9FsEBMIAUVsjMkrXOAmDqFUzpI40q1OBPffvPwfKe_OW5PyIaPdznGcaWC_JaW9I73obiyJVfRFLaxZ9jVaoBb1VXpqKtWOlIdjEZVthq3wp5cYMoGWWmYiwTma4aFaN1c4nphpWbn9KTH9dahg4H-8kFmNRfk74j6p7UHLWNGLuSsSI9UtTId484XPzRgbarA7H1Wc4LYpGu1UWtZZZbIeFKmopJNjD3AiGLL1IHqbUWMg4FRX4ERPnUvYY1WvX0Tl4939vB6jgGwQpeBkWNPmXjbYBuZYaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a60a908ab2.mp4?token=eYgvVlI6tzsDl-u6tIJMiOqQTZ2RsyCCs6mtYUnX2DfHCzz_N_P1S9FsEBMIAUVsjMkrXOAmDqFUzpI40q1OBPffvPwfKe_OW5PyIaPdznGcaWC_JaW9I73obiyJVfRFLaxZ9jVaoBb1VXpqKtWOlIdjEZVthq3wp5cYMoGWWmYiwTma4aFaN1c4nphpWbn9KTH9dahg4H-8kFmNRfk74j6p7UHLWNGLuSsSI9UtTId484XPzRgbarA7H1Wc4LYpGu1UWtZZZbIeFKmopJNjD3AiGLL1IHqbUWMg4FRX4ERPnUvYY1WvX0Tl4939vB6jgGwQpeBkWNPmXjbYBuZYaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
❌
🇾🇪
حملات هوایی جنگنده‌های عربستان سعودی به استان البیضاء یمن
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71540" target="_blank">📅 20:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71539">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOQYGUII_C8KrED11cqdF92WAhDC3304dl8vZcFJz565oDSfE7FLf149WCJCI_ppJfYGEUGqZ0yN55638UQ3RavFm3mPTA-Q7fllyhJydQ7H5T8QdGG3uoKoAYw4dpUitW_-vNHz681b2LrAGxFksgdhj07xk6GvSqzmGfjQGhoLRI6mjLfGaTPV3b4woXNTMRD5qF1OF05SDOdac8o-wrtbX-WYxsF_I39OaZ71V_XX9S7cyyeAQgvZIIYMe8uqYeNuJGXmcxIXCTkshy1RprHVvFD5J0m8Sjtw6IYQPLitjzAyB4OXbu8KnKEN9UCy2ok8H2O5fFlczYMzTxXTRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
علی قلهکی:
مذاکره متوقف شده است چیزی وجود ندارد که میانجیگر داشته باشد.
عاصم منیر هم جمع بندی ندارد که اگر وارد جنگ یمن شد، بتواند پیروز شود و پرتابه‌ای سمت تاسیسات حیاتی پاکستان نرود
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71539" target="_blank">📅 19:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71538">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qylr4U_Hd_n84K6D1sCjhZww-dR2DtNc_5os5Byelu16xawPHg79IMtJoJBBXy_ceX1cu6sDuO4-utRQp3djFwDaaNb7XO8hQ9jur2V5bq40UKb_0mbYk3H7-QoMQQuoTq35puEam4h1HjJX9gvzkbaEjLFgJ16ohMZ9eNogEae86g-wyNef9ZPumpG9r6p3aRZTik8SkcREBiWfyVvQnmlDyDTsCR6Gh_ReDBs3JxNgXb7fi1HSIh64PdE5LZ-dJuOM8ZOJAalZXOKRO5kJxxD9Fw4ppOtWKsYaXBtBxQOjbeJd5DhOENaqakU2PXOO-nV5foOznNwVqVPqy-mnhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
فرماندهی مرکزی ایالات متحده:
از زمان ازسرگیری محاصره موسوم به «دیوار فولادی» علیه ایران توسط آمریکا در ۶۰ روز گذشته، نیروهای سنتکام مسیر ۱۰۰ کشتی تجاری را تغییر داده‌اند.
حتی یک کشتی هم بدون مجوز نیروهای آمریکایی از این محاصره عبور نکرده است و نظامیان آمریکایی همچنان با تمرکز کامل بر این مأموریت متمرکز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71538" target="_blank">📅 19:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71537">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇧🇭
❌
🇮🇷
بحرین اعلام کرد تا زمانی که روابط دیپلماتیک با ایران از سر گرفته نشود، در هیچ‌گونه نشستی با این کشور شرکت نخواهد کرد و بدین ترتیب پیشنهاد عمان برای برگزاری نشست وزرای کشورهای حوزه خلیج فارس و ایران پیرامون مسئله هرمز را رد کرد.
🗣️
بحرین چهار شرط تعیین کرد:
توقف حملات
پرداخت غرامت
احترام به حاکمیت
حل‌وفصل اختلافات از مجاری قانونی.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71537" target="_blank">📅 19:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71533">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b779ef03e.mp4?token=QnjeGk4JTy6kYDXd1kQ6jW2VXtQ5ZiPf3-d4JA-ILSVv-HHzsLmj4oZybtCKrMbtVG4zHpiSVVsq-Mz7DFzqi7fPElEORabgJCTVJBpcuCjrnyGpMoNwRkKaTIgxLgmZFkjNgotQhgbVTPNWgqUjR20dACjLiFqwbruChsRbLgKMTbeMNp_gZaB22-s61nk3P__JNWDRGYgtWUKbMyqJ3JA2sSpggjcdClz-9VDAhBL7Gy-YkNMjFJY9_f0Adz-AvhguJwO9_zOQetDSGrJu7YlxAEPa5bbW_l514ZLhsjSL_wQaubPgKQszZHqoANNcjfAFbg3XtHeDK582dVaNbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b779ef03e.mp4?token=QnjeGk4JTy6kYDXd1kQ6jW2VXtQ5ZiPf3-d4JA-ILSVv-HHzsLmj4oZybtCKrMbtVG4zHpiSVVsq-Mz7DFzqi7fPElEORabgJCTVJBpcuCjrnyGpMoNwRkKaTIgxLgmZFkjNgotQhgbVTPNWgqUjR20dACjLiFqwbruChsRbLgKMTbeMNp_gZaB22-s61nk3P__JNWDRGYgtWUKbMyqJ3JA2sSpggjcdClz-9VDAhBL7Gy-YkNMjFJY9_f0Adz-AvhguJwO9_zOQetDSGrJu7YlxAEPa5bbW_l514ZLhsjSL_wQaubPgKQszZHqoANNcjfAFbg3XtHeDK582dVaNbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین  به اهدافی در چهار منطقه روسیه حمله کرد که حملات ساراتوف تایید شده‌ترین و چشمگیرترین آنها بود.
مرکز لجستیک عظیم اوزون در ساراتوف (با بیش از ۱۰۰۰۰۰ متر مربع مساحت، بیش از ۳۰ میلیون قلم کالا ذخیره شده، تا ۹۰۰ هزار سفارش در روز).
طبق گزارش‌ها، پالایشگاه نفت ساراتوف (روس‌نفت، که قبلاً بارها هدف قرار گرفته بود) نیز آتش گرفت.
در ولگوگراد، فرماندار تایید کرد که آوار به یک مرکز صنعتی و یک ساختمان آپارتمانی برخورد کرده است.
منابع اوکراینی می‌گویند که هدف صنعتی، پالایشگاه ولگوگراد لوک‌اویل بوده است.
برخی ادعا می‌کنند که از موشک‌های کروز در کنار پهپادها استفاده شده است.
انفجارهایی در انگلس (محل پایگاه بمب‌افکن‌های استراتژیک روسیه) گزارش شده است، اما هنوز هیچ اصابت تایید شده‌ای به فرودگاه وجود ندارد.
بنا به گزارش‌ها، منطقه بندری کاسپیسک/داغستان نیز هدف قرار گرفته است - پس از حمله تایید شده شب گذشته به بندر ماخاچکالا.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71533" target="_blank">📅 18:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71532">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71532" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71532" target="_blank">📅 18:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71531">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSWR8pwup2w9baJFdEILpUSt6j0G9gYMhCIoRIq6nxAYTNwQQuwtuWgV5A9zoi4EibyMMV5tC0NoM_HoO1T3BTCE0-E2mrYrtXHh1cKShWUbAKIVI5JRumpmrH_jvFFHawLyouDIl_8QUt0_99rJxbTiJx4E89yG_zq2NKO0RQgs15RDyhIV6ncZLQyyebrVOGyW7jIoQkHT8EZZ7K2iV8XN2RKAYkF087G0jUlS3nA7c4t25_Yk0FZte8eVU-lXfXsOqBVdgZCGMcb0wcKC1R0u1_KsVrrkUbaF8BnIjj1Ck59GUGUulmKd60d9bcNzW3Pmn-lgykuciKKFE7csjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
میلان
🆚
لاتزیو
⚽️
را در
TrexBet
پیش‌بینی کنید.
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
میلان: ۳ برد، ۱ تساوی و ۱ شکست و ۹ گل زده
⚽️
لاتزیو: ۴ برد، ۱ شکست و ۶ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71531" target="_blank">📅 18:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71530">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/554b629d89.mp4?token=rJ8ws2h0OoqP9hw5a8cfmVA2H8E7aVLVfGm-ByV7h7QgfWXXGGz2-dPb935EKIU64SQ-EUyWi_QkYFWmS_ek63KR-5SB3vdPvRrfDwOWXt4wNf1d8w3jF0FVb8aYV44V7T0uGp1VUIJr6MrLvYWZ9TSbJREDfdAGpZd-ByYKn4vVfMrI4oo7_j_ommMe5NFEpU6ln2oaD2-7ce5W-R11-t0dq1X-ymv9wYMmGb1LDE_hrSgowbFTuJee4bE7T9XD_sVZmv8Ihv2oc5lvIBw8uHB3yeRKkLU3g20VNhy42TiEJfw4wdyQsq4XGTE5pDCApooJCgqrToEv9L2WEGmMH3Qns49LrHnQcXDhfOo8B8qWBmQqZHZ0rO8lS4xaEzmu1wKjTX1nqZCYZ12Vp-UXxskvFJ12uNBwwxQjOclYcEakbAgG-zcnokgu07Ej0c9ubVoOasSwrpuvkom3uU8dqZRE3dfTvccVnHtfY3DP0ujps5IoFTLzP5EORfOuU4t6yxWFNdkfPdmeejEHx6Cf3vjj-csIAPlqUh2YJBp2ITmgW2Vz1eyVvHOv3csIi9vovuIgCf3lOyU2aycZ4FvwUg343lZgCyjDanHlZ7JenqM8nV_PpnQlwIV-F4r2ATMEtX9JQdYX5_JvisiDVHYwxFKwLpInwoIRAkRmRkP0_oo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/554b629d89.mp4?token=rJ8ws2h0OoqP9hw5a8cfmVA2H8E7aVLVfGm-ByV7h7QgfWXXGGz2-dPb935EKIU64SQ-EUyWi_QkYFWmS_ek63KR-5SB3vdPvRrfDwOWXt4wNf1d8w3jF0FVb8aYV44V7T0uGp1VUIJr6MrLvYWZ9TSbJREDfdAGpZd-ByYKn4vVfMrI4oo7_j_ommMe5NFEpU6ln2oaD2-7ce5W-R11-t0dq1X-ymv9wYMmGb1LDE_hrSgowbFTuJee4bE7T9XD_sVZmv8Ihv2oc5lvIBw8uHB3yeRKkLU3g20VNhy42TiEJfw4wdyQsq4XGTE5pDCApooJCgqrToEv9L2WEGmMH3Qns49LrHnQcXDhfOo8B8qWBmQqZHZ0rO8lS4xaEzmu1wKjTX1nqZCYZ12Vp-UXxskvFJ12uNBwwxQjOclYcEakbAgG-zcnokgu07Ej0c9ubVoOasSwrpuvkom3uU8dqZRE3dfTvccVnHtfY3DP0ujps5IoFTLzP5EORfOuU4t6yxWFNdkfPdmeejEHx6Cf3vjj-csIAPlqUh2YJBp2ITmgW2Vz1eyVvHOv3csIi9vovuIgCf3lOyU2aycZ4FvwUg343lZgCyjDanHlZ7JenqM8nV_PpnQlwIV-F4r2ATMEtX9JQdYX5_JvisiDVHYwxFKwLpInwoIRAkRmRkP0_oo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
پست جدید هیچکس (سروش لشگری ) توی اینستاگرام که وایرال شده؛
«هنو به یادتم»
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71530" target="_blank">📅 18:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71528">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4b43f033.mp4?token=usW4mDcrWQvbNLvtbFC4O7HJPK8f_8Zez61nj9SOu86gBSqxaXIuAqzNVYDMQrN6QNu6A_osDqjP2Yz8_f-S0llKC-asV0KZJiF3PPRDFGUVMiH3E7W97xL1V_2vszV8vutiSDiB5ykT6aIhCNst0K2M10yzv73YwlTNVjZDbyGAENhw6bop6PMdtEqJjf9Utw3m0Uu5hd7L8ReZupTW6N8_ljL3Uz43X1UR5JtY2quADL8hVR1MgLa4v2tsFCYpOkio03PZCyz9dMTm4JNRmNKrK1pyVeSWz722KoCcxffDsp8-ixDWgXSdQAYmnWbJIxOw4t5oEJ3APGRA9wq1-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4b43f033.mp4?token=usW4mDcrWQvbNLvtbFC4O7HJPK8f_8Zez61nj9SOu86gBSqxaXIuAqzNVYDMQrN6QNu6A_osDqjP2Yz8_f-S0llKC-asV0KZJiF3PPRDFGUVMiH3E7W97xL1V_2vszV8vutiSDiB5ykT6aIhCNst0K2M10yzv73YwlTNVjZDbyGAENhw6bop6PMdtEqJjf9Utw3m0Uu5hd7L8ReZupTW6N8_ljL3Uz43X1UR5JtY2quADL8hVR1MgLa4v2tsFCYpOkio03PZCyz9dMTm4JNRmNKrK1pyVeSWz722KoCcxffDsp8-ixDWgXSdQAYmnWbJIxOw4t5oEJ3APGRA9wq1-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
شعار «مرگ بر روحانی» در تجمع شبانه عرزشی‌ها
:
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71528" target="_blank">📅 17:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71527">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e506b56e1e.mp4?token=qPahvCUSqjpooTMom5B-FdEFqW-2gevF5hGwt5i9auiM_447iQd562pDuIMq53LIS4oYCCL42IHbwg1zLxkn4PxBp95vPP0_xkdNmrX9pQToAQ9hqNAWZO96WnCdLktANXuqkO8QD6pUua7dWrnUbhLMxddogJ8FkFhWN9kt24alAw_tZQRTW2KvgdvLfX3g4hlvG99Mss0o1sEEipbHsCAO-Ot3KJczq0MbtpNBcyajlth1eE26MwQ39za6aDzvWXZPGsFY0RqM6Gi4xFdOVVyO73oFnneP0LfBPCRuR0_zqBPMr0qns9CJPB6Ccr4FlA_uQaKo1sgE3ELTzZ3IZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e506b56e1e.mp4?token=qPahvCUSqjpooTMom5B-FdEFqW-2gevF5hGwt5i9auiM_447iQd562pDuIMq53LIS4oYCCL42IHbwg1zLxkn4PxBp95vPP0_xkdNmrX9pQToAQ9hqNAWZO96WnCdLktANXuqkO8QD6pUua7dWrnUbhLMxddogJ8FkFhWN9kt24alAw_tZQRTW2KvgdvLfX3g4hlvG99Mss0o1sEEipbHsCAO-Ot3KJczq0MbtpNBcyajlth1eE26MwQ39za6aDzvWXZPGsFY0RqM6Gi4xFdOVVyO73oFnneP0LfBPCRuR0_zqBPMr0qns9CJPB6Ccr4FlA_uQaKo1sgE3ELTzZ3IZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
یک شهروند ایرانی با انتشار ویدیویی اعلام کرد ترکیه مرزش رو به روی ایرانیا بسته و اجازه عبور و مرور رو نمیده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71527" target="_blank">📅 17:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71526">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89e47bf456.mp4?token=o0z7Z3g32ssT0PSdQPNzCn27tTw0d8VdbfDOSFfjel_shb7OlNdogDzVPqjJYoQ63LS4xmUIPiUPeAEtJA54eUTMBH7xuO00OiA4N2wqhbuzU9YZFk80Ty3HRPMZzFzw3tE12XE1NtLsXbkhkvcTnLPaynHuVMzdf66EQiYNfBmqQRwF8LNlQpWfbM0A7-p_FZdYso8pHydkHvIy9SkCv9pZgklISzmnO5H4hwBQkyA_GXF29NFlPER0e68ziR57OWvdCAkXJJkXCe0Lnmgk3xBNBESC1YPdZQJvpdRGcRGLAlgt_-8DlnXRdbqInTX-aObhX-kMle9kEoMs3PASTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89e47bf456.mp4?token=o0z7Z3g32ssT0PSdQPNzCn27tTw0d8VdbfDOSFfjel_shb7OlNdogDzVPqjJYoQ63LS4xmUIPiUPeAEtJA54eUTMBH7xuO00OiA4N2wqhbuzU9YZFk80Ty3HRPMZzFzw3tE12XE1NtLsXbkhkvcTnLPaynHuVMzdf66EQiYNfBmqQRwF8LNlQpWfbM0A7-p_FZdYso8pHydkHvIy9SkCv9pZgklISzmnO5H4hwBQkyA_GXF29NFlPER0e68ziR57OWvdCAkXJJkXCe0Lnmgk3xBNBESC1YPdZQJvpdRGcRGLAlgt_-8DlnXRdbqInTX-aObhX-kMle9kEoMs3PASTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو از عشق و ابراز علاقه زیبای یه پیرمرد و پیرزن ایرانی توی پارک خیلی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71526" target="_blank">📅 16:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71525">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/401752fb0e.mp4?token=sctHqOAuaQsIj6OomJjOfXgVcEAGzGTr3qNqcMV2Ale7MJWMW0jgozc6hvuiwP45YSls2i22PMtcHjo5-Gv6tbWfYM2LH237Of_D6zdRDaNhSLb7oCGaWeenefuhT8r_OuJ_lYGauuy8R39yimasRVztQxXSl2mlPhtgaPjHmNxPaNIj8b2iWMgcyti2_JMXZCpYxvGKxLwil_na7mX-VbADp_hm1mAP-P4ODnjbeXNuwYoIym1eXkyCTVXhnUVpqLCGzhQElJQrMLUF00vKrrQxD_PPf5WY-yuSCBwkTE7-0gM1kSbI7NNCUTX59sgkJysAm_cie9T6MYzUHMcfQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/401752fb0e.mp4?token=sctHqOAuaQsIj6OomJjOfXgVcEAGzGTr3qNqcMV2Ale7MJWMW0jgozc6hvuiwP45YSls2i22PMtcHjo5-Gv6tbWfYM2LH237Of_D6zdRDaNhSLb7oCGaWeenefuhT8r_OuJ_lYGauuy8R39yimasRVztQxXSl2mlPhtgaPjHmNxPaNIj8b2iWMgcyti2_JMXZCpYxvGKxLwil_na7mX-VbADp_hm1mAP-P4ODnjbeXNuwYoIym1eXkyCTVXhnUVpqLCGzhQElJQrMLUF00vKrrQxD_PPf5WY-yuSCBwkTE7-0gM1kSbI7NNCUTX59sgkJysAm_cie9T6MYzUHMcfQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه دختر حامی حکومت:
چرا پزشکیان ۱۷ شهریور که تولد مجتبی خامنه‌ای هست بنزین رو گرون کرد؟ چرا روز تولد خودش گرون نکرد؟
میخواین همه تقصیرات رو بندازین گردن امامِ ما یعنی مجتبی؟ کور خوندین!
ما دیگه فریب بازی‌هاتون رو نمی‌خوریم که میخواین علیه رهبرمون کودتا کنین.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71525" target="_blank">📅 16:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71523">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e93a51beb4.mp4?token=Sx7PcaJ33Nd365hrTDB7TJcUtI8BBCbKAXYw19j4Rh9U_utGYSS4aeK5vmZYzGlpDHFLJwQ2-CWsXaaspAoozKtmOGpueru9E5GIitPnHmAKyeAQU5-nwARI-oxeoQOukIzKkrg7cPwgo5lw98a65xCd_o-vW6TeXgS_mxmN8q4o8IOa6XNTf2cpuxgITSY2IfXMfq_tIqhnGJmXosUFLRpcmbEqGkV1HQpr6zbjBj6m7H0BKIfLcRB9MlcloL-8BUDFtvH80HrKHcmKAga9CysVEw9sh8X46pU5fI3mhmBxfM8etTa1W8Zl1nBc_9uekLVMUwxuH-8NJNYuMckiH6BmFIfqvB82D74sboar39auj6G2G42fI55jWaQ09M0LtRHnjYQeBcxfRsrMrsdbDxDxzTThn9zkmXHxZ1q2T3uBVuWlXUyc2p7BhJ7_GZjr_iSBBsa7a14uIl2t8kQWQWmCQFk1o_C3fgjIrddwR7Stx36PX7liu3wC8wRN8_RbYw3--sAbZFXG5x5ldYKkKGZGCdWlWrCa-pBFMRi4DZF28jYdMTDnrOh4AHV7gp5A8Rcrv7aPW5TwCok75zZMIrYcGTlVgZaeWlxoeZqXMQtd5v9x6U78vhqfHClPO1z63G2-PL2XwsvfB17wQddWZYW-H5kwTOljMdAtsu391do" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e93a51beb4.mp4?token=Sx7PcaJ33Nd365hrTDB7TJcUtI8BBCbKAXYw19j4Rh9U_utGYSS4aeK5vmZYzGlpDHFLJwQ2-CWsXaaspAoozKtmOGpueru9E5GIitPnHmAKyeAQU5-nwARI-oxeoQOukIzKkrg7cPwgo5lw98a65xCd_o-vW6TeXgS_mxmN8q4o8IOa6XNTf2cpuxgITSY2IfXMfq_tIqhnGJmXosUFLRpcmbEqGkV1HQpr6zbjBj6m7H0BKIfLcRB9MlcloL-8BUDFtvH80HrKHcmKAga9CysVEw9sh8X46pU5fI3mhmBxfM8etTa1W8Zl1nBc_9uekLVMUwxuH-8NJNYuMckiH6BmFIfqvB82D74sboar39auj6G2G42fI55jWaQ09M0LtRHnjYQeBcxfRsrMrsdbDxDxzTThn9zkmXHxZ1q2T3uBVuWlXUyc2p7BhJ7_GZjr_iSBBsa7a14uIl2t8kQWQWmCQFk1o_C3fgjIrddwR7Stx36PX7liu3wC8wRN8_RbYw3--sAbZFXG5x5ldYKkKGZGCdWlWrCa-pBFMRi4DZF28jYdMTDnrOh4AHV7gp5A8Rcrv7aPW5TwCok75zZMIrYcGTlVgZaeWlxoeZqXMQtd5v9x6U78vhqfHClPO1z63G2-PL2XwsvfB17wQddWZYW-H5kwTOljMdAtsu391do" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ درباره ایران:
«ما کنترل تنگه هرمز را به دست گرفتیم. تمام مین‌ها را پاکسازی کردیم.
من گفتم: «خب، پس چرا آنها مین‌روب‌های ما را هدف قرار نمی‌دهند؟»
گفتند: «قربان، این مین‌روب‌ها زیر آب هستند. آنها همیشه در زیر آب فعالیت می‌کنند.»
گفتم: «چرا این کار را می‌کنید؟»
گفتند: «خب، به‌طور کلی، وقتی مین وجود دارد، بیرون از آن منطقه هم خصومت و درگیری زیادی وجود دارد.»
یعنی اگر در یک آبراه مین وجود داشته باشد، معمولاً افرادی هم هستند که به سمت شما تیراندازی می‌کنند. بنابراین اگر زیر آب باشید، آنها نمی‌دانند شما آنجا هستید.
حالا دیگر هیچ مینی آنجا نیست، هیچ چیز دیگری هم نیست. و اگر ببینیم آنها [دوباره مین‌گذاری می‌کنند/اقدام به این کار می‌کنند]، آن‌وقت می‌بینید چه اتفاقی می‌افتد.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71523" target="_blank">📅 15:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71522">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb4e73a23.mp4?token=tXQsCOg3EBAivO8Bfx7PS6izRF4fyP4EsbPopsQmoaFB1clfckPXu9nkFtmk-DBUvn1rbvy7s5SD8iCH9I4ESYJ-udCCr57EFPigEF41jD38xBoTlDlXfcvfeN1n12qknaupbUWKJP9ydbEx-ijSQY7ehun5GK_4TTzOqJVyY3JNaiteJONx9cUie-ynNR745SdvI3_YiL1ho175Cy6_tEXCzlhA3RcpCu9a311KIiX6_IMjl-1jnppMWsd_ZpGCSsZhGcSEPPvu0rA_IDj-6m5o31BaV8GXHzaFd6qnTTAe072Ir7ojCpp81HBoGvdrNyC9s1loEPRZK6BnzT6nyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb4e73a23.mp4?token=tXQsCOg3EBAivO8Bfx7PS6izRF4fyP4EsbPopsQmoaFB1clfckPXu9nkFtmk-DBUvn1rbvy7s5SD8iCH9I4ESYJ-udCCr57EFPigEF41jD38xBoTlDlXfcvfeN1n12qknaupbUWKJP9ydbEx-ijSQY7ehun5GK_4TTzOqJVyY3JNaiteJONx9cUie-ynNR745SdvI3_YiL1ho175Cy6_tEXCzlhA3RcpCu9a311KIiX6_IMjl-1jnppMWsd_ZpGCSsZhGcSEPPvu0rA_IDj-6m5o31BaV8GXHzaFd6qnTTAe072Ir7ojCpp81HBoGvdrNyC9s1loEPRZK6BnzT6nyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
هادی چوپان :
هانی رامبد از پشت بهم خنجر زد.
گفت پشت جمهوری اسلامی نباید باشی ولی من قبول نکردم و اونم همکاریشو کامل باهام قطع کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71522" target="_blank">📅 15:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71521">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFgPKE2HIOVoKo10Q1Z2ZbHWcqHKBz-XPhWVIEaaWmTn3n_wgG3xCLhunDQDsDcccgwtbrAyY-WjCJ7EM5UKDJMEmlyUUKmtbvBpdmusNjoMSif8FcsJgzYH9LhWSV5716UwQ-hVzejp_j9yvOydXYZO4ofc5JfE9HDzYbbrxR8vOd_hfmHC4ASGqrLff-T4TdkxxdA-VsY698WJtT17EEUHvaxdwxKW2CMjK8yKbHXCZ9zR8XljrbhL_YgySKFoYpsU6N7DxSTAwfI6DiEKPEoLg_I8JOwW5og3I9IW1u_v6OIA-20CiFQMEYThJn-YPGYDSn8K3a6ImKx5i6JgJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇦🇪
پزشکیان در جریان حضور در اجلاس سران بریکس با محمد بن زاید آل نهیان رئیس امارات متحده عربی دیدار کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71521" target="_blank">📅 14:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71520">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=T3d5hz_GBdqvXHcEiwXcA8MnOa3GMwv9OTMpdumN2nsQgoCm-VZWnlhoOjeOElBQNnmOwUXg4tH511Hww5CqXoy7u4EGm0R0XpDwlsQzsnwlVeoB4PEAPU6QErsBH1-pAJ-YxsdjW5vd-S0CUh5t0OZ5m9Qh-mf2HZL6RGNFIpL44gn1BwfsqGEoeurBaxxYaSFra2blIjNZZ8VMsEmbPuZTSoZRLSRuXWXtMfsL5Rqum4x3IC8a6x6IdZMKhhPgbr4Ja3ygHXBtF6MsavzRs9_dZ9EaL6OsZ-hWqt_WB1bY6wHPsavMIhfTN62HHMjvrYF19l6TMA0DwRJ0wZiKk37NsATYCziBJRJ4W8Fols0LAEN5AwR-Adxfq0qYGXHutvhUh4UQXb2y5IXW27JzxPoIHyxPH2Ko4_UideCUhYb0huIjFOZQ-Je8ZlHFsacXMKt0nBQchhGW7RYKeSB_9lKleqLOOXCXHxx9M8BTPagdLExF2uJ4Zm2Nhk0kFFqErGCQvKCNOA8kL7jS4e6XKKmkxWLYyaz-T6_xnnl3hAqAhorigdmA2FEKbh2LyenPO5R2e291uEf2Q3uKlPL6_pF_hmOPwYzYkrE6hhOKSVK6Zj8kL1zbCxpguPOtn_rTyV2-0P9qccC4YV6VeVOFOUHx3oLAT48YMxh_kQYePAI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=T3d5hz_GBdqvXHcEiwXcA8MnOa3GMwv9OTMpdumN2nsQgoCm-VZWnlhoOjeOElBQNnmOwUXg4tH511Hww5CqXoy7u4EGm0R0XpDwlsQzsnwlVeoB4PEAPU6QErsBH1-pAJ-YxsdjW5vd-S0CUh5t0OZ5m9Qh-mf2HZL6RGNFIpL44gn1BwfsqGEoeurBaxxYaSFra2blIjNZZ8VMsEmbPuZTSoZRLSRuXWXtMfsL5Rqum4x3IC8a6x6IdZMKhhPgbr4Ja3ygHXBtF6MsavzRs9_dZ9EaL6OsZ-hWqt_WB1bY6wHPsavMIhfTN62HHMjvrYF19l6TMA0DwRJ0wZiKk37NsATYCziBJRJ4W8Fols0LAEN5AwR-Adxfq0qYGXHutvhUh4UQXb2y5IXW27JzxPoIHyxPH2Ko4_UideCUhYb0huIjFOZQ-Je8ZlHFsacXMKt0nBQchhGW7RYKeSB_9lKleqLOOXCXHxx9M8BTPagdLExF2uJ4Zm2Nhk0kFFqErGCQvKCNOA8kL7jS4e6XKKmkxWLYyaz-T6_xnnl3hAqAhorigdmA2FEKbh2LyenPO5R2e291uEf2Q3uKlPL6_pF_hmOPwYzYkrE6hhOKSVK6Zj8kL1zbCxpguPOtn_rTyV2-0P9qccC4YV6VeVOFOUHx3oLAT48YMxh_kQYePAI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ:
ببینید، ما کار فوق‌العاده‌ای انجام دادیم. می‌دانید، ما آنجا را تحت کنترل گرفتیم. ما واقعاً با اقتدار کامل بر «تنگه هرمز» مسلط شدیم و هیچ‌کس متوجه این ماجرا نشد.
ما کنترل بسیار قدرتمندی بر آن داشتیم.
ما یک محاصره دریایی اعمال کردیم که واقعاً بی‌نظیر بود.
ما تعداد زیادی از شناورها را بیرون می‌کشیم؛ به‌طور میانگین روزی ۲۵ شناور را خارج می‌کنیم که بیشترشان در شب انجام می‌شود.
اما به‌طور متوسط، هر روز حدود ۲۵ شناور را از کار می‌اندازیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71520" target="_blank">📅 13:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71519">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎙
خبرنگار:
آقای رئیس‌جمهور، جنگ در ایران چه زمانی پایان می‌یابد؟
🇺🇸
ترامپ:
فکر می‌کنم خیلی زود. گمان می‌کنم احتمالاً درست پس از پایان دوره [فعلی انتخابات] باشد. آن‌ها سعی دارند تا جای ممکن مقاومت کنند تا وضعیت انتخابات را پیچیده سازند. اما فکر می‌کنم مردم متوجه ماجرا هستند، چرا که ایران نمی‌تواند سلاح هسته‌ای داشته باشد. موضوع بسیار ساده‌ای است؛ مسئله خیلی ساده‌ای است. ایران نباید چنین سلاحی داشته باشد. آن‌ها تنها دو هفته با دستیابی به سلاح هسته‌ای فاصله داشتند.
اگر این کار را نکرده بودند [و جلوی آن‌ها گرفته نمی‌شد]، اسرائیل را نابود می‌کردند، خاورمیانه را به آتش می‌کشیدند و به برخی شهرهای اروپا — و حتی فراتر از شهرها — حمله می‌کردند. و احتمالاً پیش از آنکه ما بتوانیم آتش را خاموش کنیم، به خود ما هم حمله می‌کردند. اما آن‌ها نباید سلاح هسته‌ای داشته باشند. با این حال، می‌گویم که [این اتفاق] به‌زودی رخ خواهد داد و قیمت نفت به‌شدت سقوط خواهد کرد. وقتی آن اتفاق بیفتد، قیمت نفت به‌شدت پایین خواهد آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71519" target="_blank">📅 13:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71518">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⏺
🇮🇷
قرارگاه قدس نیروی زمینی سپاه:
درپی انهدام یک تیم تروریستی حرفه‌ای که قصد اجرای عملیات ترور در سراوان را داشت، ۴ نفر از این تروریست‌ها به هلاکت رسیدند؛ همچنین تعدادی سلاح و مقادیری مهمات و مواد انفجاری از مخفیگاه این تیم کشف گردید.
در این عملیات که تا پیش از ظهر امروز ادامه داشت ۳ نفر از پاسداران گمنام امام زمان(عج) نیز به شهادت رسیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71518" target="_blank">📅 13:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71517">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8136d3aa.mp4?token=e1wVLSQAWhN1aAcv100D9TP6VHC50JB7YNGsFnEudQtxT5Oq3MN-6pqt-QkY4_ziJWWqT3-02Pb3i3_-aRyRVl3aiY4jvx_Uv0p92lH5fzvG1qpPCmZPRCv-YAzYv9vK6NR6491uziXv-dsUaWicqva8DOd3LKhOdEVNmkSLz1qJRrtwDnVDYdbiSkPlKi4Eg0VU0bNlr3SOIHWH9h85cPuYK8NZI2bTLTEarbi5IXcj839-ARBuhvLbIFFIwNp-xYhfpRnxdwrs8L5oFGnu2FPjlzui8TyR1tI0YP6IyzV0qNlvpWTAue6qTZBkka8r57UoPlvodEjp53SrYi6XRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8136d3aa.mp4?token=e1wVLSQAWhN1aAcv100D9TP6VHC50JB7YNGsFnEudQtxT5Oq3MN-6pqt-QkY4_ziJWWqT3-02Pb3i3_-aRyRVl3aiY4jvx_Uv0p92lH5fzvG1qpPCmZPRCv-YAzYv9vK6NR6491uziXv-dsUaWicqva8DOd3LKhOdEVNmkSLz1qJRrtwDnVDYdbiSkPlKi4Eg0VU0bNlr3SOIHWH9h85cPuYK8NZI2bTLTEarbi5IXcj839-ARBuhvLbIFFIwNp-xYhfpRnxdwrs8L5oFGnu2FPjlzui8TyR1tI0YP6IyzV0qNlvpWTAue6qTZBkka8r57UoPlvodEjp53SrYi6XRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا ایران مسئول حمله به خط لوله «شرق-غرب» است؟
و به نظر شما عربستان سعودی چه کاری می‌تواند انجام دهد؟
🇺🇸
ترامپ:
خب، فکر می‌کنم همین‌طور است. احتمالاً همین‌طور است.
آن‌ها در حال حاضر در وضعیت آماده‌باش و هوشیاری کامل هستند، اما فکر می‌کنم مسئول آن هستند.
آن‌ها مدتی است که کنترل آن را در دست دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71517" target="_blank">📅 13:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71516">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9946b1f32a.mp4?token=i7Ih4Im-0bOKo_tZoAxSwT8U8iDv92b_7i66AWFz8hSEkckrk9_PDjH6MSKZBMany52cIdBNG-u95HM8Cp_FIXmSJSSgQ1K8P8uwjAfpWgwZXr-RIZiA9xcjxZ6CWuEvDKSVP_N4f3uhL0merzbG2pxcSg7pSaUc5YYREK5YlccVFHfpK8skPtjczEnNvzyOLDc7T15Upn-DSr0I2rvKU1MyB-nlSRFHdviC5OdO8kCYAVUU6f_X5c3GF70yPDzqEM6-7boU_JduLJg11gkKuEit6cmpiVcAVxI7EbN0LjLxEn3L60gbjawF1zofKpN71xm8uIkcL6wWZnuFMYgHNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9946b1f32a.mp4?token=i7Ih4Im-0bOKo_tZoAxSwT8U8iDv92b_7i66AWFz8hSEkckrk9_PDjH6MSKZBMany52cIdBNG-u95HM8Cp_FIXmSJSSgQ1K8P8uwjAfpWgwZXr-RIZiA9xcjxZ6CWuEvDKSVP_N4f3uhL0merzbG2pxcSg7pSaUc5YYREK5YlccVFHfpK8skPtjczEnNvzyOLDc7T15Upn-DSr0I2rvKU1MyB-nlSRFHdviC5OdO8kCYAVUU6f_X5c3GF70yPDzqEM6-7boU_JduLJg11gkKuEit6cmpiVcAVxI7EbN0LjLxEn3L60gbjawF1zofKpN71xm8uIkcL6wWZnuFMYgHNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
این رستوران توی تهرانه
نوشته : هیچی کتلت بی بی نمیشه:)))
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71516" target="_blank">📅 13:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71515">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0f6d97e2.mp4?token=SNCVRfkphCQtOFkC1XG702kzgCR8M8tWBfVl7xJfG95awN6B0Z01W3N-Iww90xKmjZWhib7cjx6u4T6M8m42eX1upblcEHDYq4FfXDcQW0Y-6AZFwekEWRJZoiFVNROnBBpqRAB7NCpsd8CiR8d1uBFVB62zMKKVA-sZu-jNHBVv6v_4vmKJ4eRQJIu_PV1M5XOLy5BTEUSnv6UCJl0JQOigVlQkkJYwXv-P5MDGRYJgdYLykpd_ugqJOFvkLeChzh7ZOpnKtzhUQeTBuyIDT1gfDVPlGvsLTNUN1taUxrY84CPsxpvd3nx46BGt5eydYC-OSD8PfftHP5pQIrkO7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0f6d97e2.mp4?token=SNCVRfkphCQtOFkC1XG702kzgCR8M8tWBfVl7xJfG95awN6B0Z01W3N-Iww90xKmjZWhib7cjx6u4T6M8m42eX1upblcEHDYq4FfXDcQW0Y-6AZFwekEWRJZoiFVNROnBBpqRAB7NCpsd8CiR8d1uBFVB62zMKKVA-sZu-jNHBVv6v_4vmKJ4eRQJIu_PV1M5XOLy5BTEUSnv6UCJl0JQOigVlQkkJYwXv-P5MDGRYJgdYLykpd_ugqJOFvkLeChzh7ZOpnKtzhUQeTBuyIDT1gfDVPlGvsLTNUN1taUxrY84CPsxpvd3nx46BGt5eydYC-OSD8PfftHP5pQIrkO7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
🇺🇸
پست جدید دونالد ترامپ در تروث سوشال:
با این رئیس جمهور بازی نکنید، زیرا نتیجه خوبی نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71515" target="_blank">📅 12:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71514">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2j1DldnAJgpqz45pRD3Hxo_KXkOGDVll13zbKp6zmiO1XveKMWKgR-UYPmBUnu0wv8tWIY4l2y1nQCXpDXYEAj0fbh5oUDo-Mk6BlwctgGeBpEZdN2uWSzfU9V7Dc--I0CtXKyPUZx4BaiL0TXKN9BJpXgTx75wMmufs9jA8tD3D9GmzLf6ecfoKgmVVP8U9CDfpV5DfN3EvU3OZA6Uy1bsew-vbQYM-MG2BR2M8HtC1G_YMhK4TKKn6C1EfKa-nWIhmxaOX_c8iBnapLt05wxioy2CmCxH2_6AGAU0zGBxzg4mbWztqesNjU3yAU09bsGuUr8hVcN_bT22Y_3JgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
طبق پیش‌بینی‌ها، یکی از پربارش‌ترین پاییزها تو راهه.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71514" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71513">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71513" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71513" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71512">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzgQuX6HDRWh9iOQ_qfGBOQTd_xI9VMlfuJNug9pBDNeznXIvY_gSsJHGUSsydISmyuc-mCV5W3i8_5YZShyXTCiyhlnD64EdIHZ1v7IEHQTBPtw36cv1ryWNRtijhi37VPeMfBAGWySzV1kRbNg1tyuJ0QAr5rxiVgc6GF5iNx5ISDGR8g99vKZYOKNEtfddWmw_t-1gvr0ECWYNt2keK-6wo-C7au5v2TEPsA1I57Q58pSRg4zA0rEWwiBLBMdijpCr2sodel4rqd35rusevaj6N9x4irg5_-CIz5SBVxZzEpyDKeQn8jX9ukwj7vz5NF1u4rtDueVlCBdapKV2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت‌بین‌المللی
TrexBet
پیش ‌بینی کنید.
چلسی
🆚
لیدز یونایتد
فولام
🆚
لیورپول
اورتون
🆚
تاتنهام
ساندرلند
🆚
آرسنال
رایو وایکانو
🆚
رئال مادرید
میلان
🆚
لاتزیو
کالیاری
🆚
آتالانتا
پادربورن
🆚
دورتموند
🦖
🦖
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب برای بازی‌های امروز
🦖
واریز آسان و امن از طریق کارت به کارت و ارز های دیجیتال
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71512" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71511">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🇮🇷
معاون امنیتی و انتظامی استاندار سیستان‌وبلوچستان: محل تجمع اعضای «گروهک‌های معاند و تروریستی» شناسایی شده و نیروهای امنیتی در یک عملیات غافلگیرانه به آن ضربه زده‌اند.
در گزارش‌های اولیه، نام جیش‌العدل/جیش‌الظلم به‌عنوان عامل درگیری امروز به کار برده شده که هنوز به صورت رسمی تایید نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71511" target="_blank">📅 12:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71504">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d436ab6a3.mp4?token=ZgoeTBRXD3-d1QU48vWtnYfJh5uk9AgpfRR3b87HRciNMNB1t5wD7q9uvNgi0UNEr4C8w9KaTlMnEIt_fJM1IPed72e7DBBUrLEzGdzCngyCwzxlqX5QzH_5MCn0GdYBqWft-08WtLreIH9itJoakCT3VClVY9q0_GTpUvdAhN5rHUuW5eys7pBGNb59MqKUwIOKmow3wN96VtTHGVjIYc97l9zUzTohtlfL4zElHwfE5tdimnDjGQg8kTv4-xCnJZGM1w8fkN6W9IMs1vPT4D_mwltMaCdeiDFEZiOhg10S3HAVDjQm3JewqS0tB1LH461tyFOrl5fzMl_BlUEHLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d436ab6a3.mp4?token=ZgoeTBRXD3-d1QU48vWtnYfJh5uk9AgpfRR3b87HRciNMNB1t5wD7q9uvNgi0UNEr4C8w9KaTlMnEIt_fJM1IPed72e7DBBUrLEzGdzCngyCwzxlqX5QzH_5MCn0GdYBqWft-08WtLreIH9itJoakCT3VClVY9q0_GTpUvdAhN5rHUuW5eys7pBGNb59MqKUwIOKmow3wN96VtTHGVjIYc97l9zUzTohtlfL4zElHwfE5tdimnDjGQg8kTv4-xCnJZGM1w8fkN6W9IMs1vPT4D_mwltMaCdeiDFEZiOhg10S3HAVDjQm3JewqS0tB1LH461tyFOrl5fzMl_BlUEHLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
درگیری های بی سابقه نیروهای جمهوری اسلامی و نیروهای مسلح در سراوان سیستان بلوچستان
ویدیو ها مربوط به چند ساعت پیش
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71504" target="_blank">📅 11:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71503">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🇮🇷
🇮🇶
رسانه عراقی نایا به نقل از یک منبع:  دستور فوری و جدیدی از سوی فرماندهی کل نیروهای مسلح به بصره ابلاغ شده است که بر اساس آن، گذرگاه مرزی شلمچه با ایران از همین لحظه و تا اطلاع ثانوی به‌طور کامل بسته می‌شود. این تصمیم شامل تردد مسافران و همچنین جابه‌جایی…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71503" target="_blank">📅 11:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71498">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba81cb21e1.mp4?token=cafgTLhEXhQkuS8utAYVc5Iu6EiOIZdKuoei-SjHtQ0qUckU2zlri2rwrL7rrAf_DGS_9Gplq1D8yyhob8AO6IQlguPX6L6NOUh3akuSlyGNUyOi3gq08zgtf-YSgRuNB-4xFkjkZ05AHHWbuepQ_HVP9W9DO09TJ8IrPc1muIt3_6BhGZ_wUzo8vbzxtlAiURFoxlnJQKocIFrlyUj9mRiFfiOI8WxbQmWjf9sX-4U4LNzT5EvBGBMW4xR0492saXxO2T4mPAA-ohnCp5LdReJ4P32Z97zgKoDPyaj143nWmPn8OLf1sKBsktswaqETwNdOE8wpq5e_cyri4mWnLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba81cb21e1.mp4?token=cafgTLhEXhQkuS8utAYVc5Iu6EiOIZdKuoei-SjHtQ0qUckU2zlri2rwrL7rrAf_DGS_9Gplq1D8yyhob8AO6IQlguPX6L6NOUh3akuSlyGNUyOi3gq08zgtf-YSgRuNB-4xFkjkZ05AHHWbuepQ_HVP9W9DO09TJ8IrPc1muIt3_6BhGZ_wUzo8vbzxtlAiURFoxlnJQKocIFrlyUj9mRiFfiOI8WxbQmWjf9sX-4U4LNzT5EvBGBMW4xR0492saXxO2T4mPAA-ohnCp5LdReJ4P32Z97zgKoDPyaj143nWmPn8OLf1sKBsktswaqETwNdOE8wpq5e_cyri4mWnLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پسر تهرانی بعد از اینکه با دوس دخترش کات کرد، رفته تمام اکسای دختره رو جمع کرده، واسش دسته جمعی آهنگ خوندن تا قشنگ دختره رو بسوزونه و عقده هاش رو خالی کنه...
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71498" target="_blank">📅 11:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71497">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa7081550.mp4?token=s2sZ1AcIipeQjtApBGcw5DFEgPkdv3x7jh3ohvQxuMTZjWzl21ufl7a80PAB5ULybECJtwYlEnJXkppXIztVSP7XKBWqDL4Xr258laX3nXQVwYmt_zFbrepvFZYXm2V5p-Z-EGH1pvmTGa42rbcEAEeSfOfgC4Fs0NElhPWFZRqSPkGv0YoLOtNnvUZiSLKcz93oD8EB4wOwm-dFkhY1fFSc69EATicfSXYdByHf_WhqoZoPQERPMz_6sVRXhIGfcc8CZ3UK_8W0BzFbc-s3JGzlFjIVP6TkXYYSz-FoJJ5VI42YFLNSJgUcOTBKuAbkSq92PKLwmtgSvJAoalkJw4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa7081550.mp4?token=s2sZ1AcIipeQjtApBGcw5DFEgPkdv3x7jh3ohvQxuMTZjWzl21ufl7a80PAB5ULybECJtwYlEnJXkppXIztVSP7XKBWqDL4Xr258laX3nXQVwYmt_zFbrepvFZYXm2V5p-Z-EGH1pvmTGa42rbcEAEeSfOfgC4Fs0NElhPWFZRqSPkGv0YoLOtNnvUZiSLKcz93oD8EB4wOwm-dFkhY1fFSc69EATicfSXYdByHf_WhqoZoPQERPMz_6sVRXhIGfcc8CZ3UK_8W0BzFbc-s3JGzlFjIVP6TkXYYSz-FoJJ5VI42YFLNSJgUcOTBKuAbkSq92PKLwmtgSvJAoalkJw4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇹🇷
یه گزارشگر تو شهر وان ترکیه طی یه گزارشِ خیابونی، نظر مردم این شهر رو درباره گردشگران ایرانی پرسیده که حسابی وایرال شده؛
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71497" target="_blank">📅 10:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71495">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faeed5163b.mp4?token=pyCk05WkqR4TPNHCE_IQl-JWR4kBlwH671YSg_d-uKYteDUTzwL7ZwQI5WqrHdCrWcxno4bNSEPwdGlaMjp8E4gscqtvL3SQn4jTMFHg0Wj_hDJh7ylbirEofJAGsCx-L7215Xo-oqoFxjy-INeicuvg27dAh-62j_OCWH26ci_ggMkx1E7uMAWdoSPJmKg5g9hAfo2pvJIBwlOOSQ3ILecAyJOi--6nUVSXZhXNqvv5m9Ychy3-BEFm8d9q28iEYFiZzoyYxNqZxPhYsdpzRZHNfLeQcRR4CKtikpytqSbIKiJU-ivsSY3xq_JZd7xjHxZT3NfLohHfl-ps4FnB1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faeed5163b.mp4?token=pyCk05WkqR4TPNHCE_IQl-JWR4kBlwH671YSg_d-uKYteDUTzwL7ZwQI5WqrHdCrWcxno4bNSEPwdGlaMjp8E4gscqtvL3SQn4jTMFHg0Wj_hDJh7ylbirEofJAGsCx-L7215Xo-oqoFxjy-INeicuvg27dAh-62j_OCWH26ci_ggMkx1E7uMAWdoSPJmKg5g9hAfo2pvJIBwlOOSQ3ILecAyJOi--6nUVSXZhXNqvv5m9Ychy3-BEFm8d9q28iEYFiZzoyYxNqZxPhYsdpzRZHNfLeQcRR4CKtikpytqSbIKiJU-ivsSY3xq_JZd7xjHxZT3NfLohHfl-ps4FnB1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئو وایرال شده و پشم ریزون از کنسرت تیلور سوییفت؛
خودتون ببینید به چه دلیل وایرال شده
😏
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71495" target="_blank">📅 10:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71494">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‼️
خورلسوخ، رئیس‌جمهور ۵۸ ساله مغولستان، هنگام بازدید از یک یگان نظامی، حرکت پرس سینه را با وزنه ۱۰۰ کیلوگرمی در ۲۰ تکرار انجام داد.
او که پیش‌تر افسر ارتش بوده، نامش در لغت به معنای «تبر برنزی» است، باشگاه هارلی-دیویدسون مغولستان را تأسیس کرده و در یک گروه موسیقی گیتار می‌نوازد؛ او همچنین جانشین «باتولگا» شده است که خود قهرمان جهان در رشته سامبو بود.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71494" target="_blank">📅 09:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71493">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a695c5e874.mp4?token=Oqzbdb2f6zMapj465_pOOtNkCXoFBGrBT_IQHheyFweuE8fyuSTSn2ZDRYb9xeegFszPW54r3BzikD3OFwxbJVkrBVt9ulysbamxhDFSUoUthSJomzwuFdm8G5F67udQFUh6sRHTioL4WiV0CakUDjRZ5AvbjwdeFkFconUGhKLd4tG_lEBOW4tyqolP2mz_U5DdrqlY_mXGbQ5pt-PZGEWA2YHkFnsBT9kut9GjcvA4hEvNDD6_mKrsFtAM69anP1CUISUjSz3frRJbA6KUBIslAywBjI3Hl-MtnIkH8AohJcbduPdh3ttltcZdSlSFTpeHkTtj_hxG_EztvA8iiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a695c5e874.mp4?token=Oqzbdb2f6zMapj465_pOOtNkCXoFBGrBT_IQHheyFweuE8fyuSTSn2ZDRYb9xeegFszPW54r3BzikD3OFwxbJVkrBVt9ulysbamxhDFSUoUthSJomzwuFdm8G5F67udQFUh6sRHTioL4WiV0CakUDjRZ5AvbjwdeFkFconUGhKLd4tG_lEBOW4tyqolP2mz_U5DdrqlY_mXGbQ5pt-PZGEWA2YHkFnsBT9kut9GjcvA4hEvNDD6_mKrsFtAM69anP1CUISUjSz3frRJbA6KUBIslAywBjI3Hl-MtnIkH8AohJcbduPdh3ttltcZdSlSFTpeHkTtj_hxG_EztvA8iiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حسن روحانی خطاب به ارزشی ها : انتقام خامنه‌ای رو امام زمان که ظهور کنه میگیره
وسط مذاکره برای اینکه راهی پیدا کنیم که جنگ زورتر تموم شه یه عده میگن باید انتقام بگیریم خب چجوری ؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71493" target="_blank">📅 09:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71492">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🇮🇷
🇮🇶
رسانه عراقی نایا به نقل از یک منبع:
دستور فوری و جدیدی از سوی فرماندهی کل نیروهای مسلح به بصره ابلاغ شده است که بر اساس آن، گذرگاه مرزی شلمچه با ایران از همین لحظه و تا اطلاع ثانوی به‌طور کامل بسته می‌شود.
این تصمیم شامل تردد مسافران و همچنین جابه‌جایی کالاها می‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71492" target="_blank">📅 07:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71491">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/71491" target="_blank">📅 01:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71490">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvvDibFONYB5_aKymZzWxFQIrOTq6LKRZ24_daV8J2GWtUgI_sIXxJaFAJ3PUqyqC5qxVmPUQ7IDjWL5nNsnx2lDj48eQK2-jWzHe-FOC141rhcx77f6NY-qyq-qO9a04qeqmalXY7_0tcIyPLBrr65tXatx0gwfPVngTQlNaamHpOr_c9ySJTSRurTsUXPVRuB3aPzYjqGU5DPiJnH2Bd53eXWEjOCa0hpnyqOqCGgBUKBPcC_i7Scetb8QWoUidrn1ngUjJq_A02i2JcIvRueNChuii3hgCYMbfR0dYABvKrfe42Q1EeF3ZqomG9zbAPLvNcxNNmYSSGOjVXDlNw.jpg" alt="photo" loading="lazy"/></div>
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
دو زمان، دو کد، دو فرصت شکار 1 دلاری.
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/71490" target="_blank">📅 01:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71489">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c20cfcda3a.mp4?token=IOrFcNjxgDl3PLJcpNXJDySmWgq0ziOFt4d9o7UP8uCIndMBAafW5AEG85XfDUy-3CPiFXZIaWB98WYWPQJUCDoUG0HF7Al6xSXiwBzjBryx7CbYgBHMYN4TjP_nHjrxJW0ui68ajfj6irUdojux8ztntttzfAKnIdn5h04AuxcRj0p12upHXJs70WnVQoQlDkWG7UEmgVQT4o6XadHHTq26L8pyX6iTu0jb_WGRu4MRnnIaAT-bywJbBRhCLeLMdVGUjgKGNIAULxcbAzR7bgIlJ0wjRHLeLKaKo9s2c_Up7J_VLMifselV-jJBIlnVh5IC8AXOxS21rNWmchsL2A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c20cfcda3a.mp4?token=IOrFcNjxgDl3PLJcpNXJDySmWgq0ziOFt4d9o7UP8uCIndMBAafW5AEG85XfDUy-3CPiFXZIaWB98WYWPQJUCDoUG0HF7Al6xSXiwBzjBryx7CbYgBHMYN4TjP_nHjrxJW0ui68ajfj6irUdojux8ztntttzfAKnIdn5h04AuxcRj0p12upHXJs70WnVQoQlDkWG7UEmgVQT4o6XadHHTq26L8pyX6iTu0jb_WGRu4MRnnIaAT-bywJbBRhCLeLMdVGUjgKGNIAULxcbAzR7bgIlJ0wjRHLeLKaKo9s2c_Up7J_VLMifselV-jJBIlnVh5IC8AXOxS21rNWmchsL2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
❌
🇾🇪
تصاویری از حملات هوایی نیروی هوایی سلطنتی عربستان سعودی به بندر «مخا» در جنوب غربی یمن که تحت کنترل انصارالله قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/71489" target="_blank">📅 00:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71488">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8WyFsq5tysr_K--Ob8gYxqeIu4PY0qJkVIBbeu1npTFfpNfJ-sB98hh1AWwW95ExpmJUPhJRwXigk9UBZPJ00OgPRXQjVruJt60IO_t8EuKx2OLme00eeLvLJ5ttSyBIKA1SjibkUbpKXAxocKsJ4oySefECyXCl-gHK5cwLpKfRP8Oqt3lVih9CAg51NrxOSHKqOum81uA5vFELISKXpX_qM8eNQAdvYq5DbBjNdWS8JWdpRIUMzVZ4YnShlsTO3CbESemI0N5wswdNsDrNdIfS2MAbKKcGwd-huUdwaAk4jzwfVq5WxkTJtSO7eLpp-YUm4SbxlIGvwSH0hnEHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با پول ۲۰۷ در ایران تو کشورهای مختلف چه ماشینی میشه خرید؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/71488" target="_blank">📅 23:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71487">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2da32c63e2.mp4?token=H09h15v4U_wYIt8JTCg-3ZJ265v4bfh8kq__cmnEITtp_GlCVLoXICHg5wm6MGObnru6QEkWf0uhL8nziBXDXAvk34WPw5MPJJF64g9VQ6U2rtb-yEfq93uReDVP0mb7dGDRgtyhyK8Ta_3RtCISTJb6DQgZSqod9ihP2fJzgMt_epsNJkKa8IV3jxO1OWZ7UtEPhsSo8SH-_o3hAn5O8hHypJ9CraOKOYWTFWv8fjNDKZLws7yt5Yui7fU4OI08C7hf1Xz0CgnG71U1dsjynZQO9-KcV1oHL9CLkfnw6lkjzhji7xNM_HuC_jL0w7cjDNRCdQHxl9wVyuBtHj6LZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2da32c63e2.mp4?token=H09h15v4U_wYIt8JTCg-3ZJ265v4bfh8kq__cmnEITtp_GlCVLoXICHg5wm6MGObnru6QEkWf0uhL8nziBXDXAvk34WPw5MPJJF64g9VQ6U2rtb-yEfq93uReDVP0mb7dGDRgtyhyK8Ta_3RtCISTJb6DQgZSqod9ihP2fJzgMt_epsNJkKa8IV3jxO1OWZ7UtEPhsSo8SH-_o3hAn5O8hHypJ9CraOKOYWTFWv8fjNDKZLws7yt5Yui7fU4OI08C7hf1Xz0CgnG71U1dsjynZQO9-KcV1oHL9CLkfnw6lkjzhji7xNM_HuC_jL0w7cjDNRCdQHxl9wVyuBtHj6LZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇱🇧
🇱🇧
رسانه های نزدیک به حزب‌الله لبنان وویس هایی رو از اعضای حزب‌الله منتشر کردن که در زیر ارتفاعات علی‌الطاهر در تونل ها گیر افتاده بودن و درخواست کمک میکردن.
همه این افراد بعد از حملات ارتش اسرائیل و نابودی تاسیسات زیرزمینی کوه علی‌الطاهر کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/71487" target="_blank">📅 23:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71486">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68083de4e6.mp4?token=YEX7cHxFG-fzT07o5L6iF9CoSSGMN7UVJLggDUZjzMczvNpEORlgd07BWUiG9Pusco-fKJmED3CdBhH_ffqxr09g9A1cRmYNPZaMaFT2Fw6rE0XW8TRQ-L2rzvpfxVQqqU8jjROf7-ZFybz5V9Uufj3Nv6XD1DH6bNwPn-8T4lzoDwce6OpTelcay3pldu8TMpRF-HkGEyIysL7_RZwhQoquPmVycrfpB9SQHlCKs_S1t5QAdj5DIBJJDN58UyhAlajqMvrJcho00WfnjP8qT_yoOUJ2fID41O_RHh7jk0N-nNQkIjQbT7hk5YRs71_oMQiney3Qqif0fTmOWnwkYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68083de4e6.mp4?token=YEX7cHxFG-fzT07o5L6iF9CoSSGMN7UVJLggDUZjzMczvNpEORlgd07BWUiG9Pusco-fKJmED3CdBhH_ffqxr09g9A1cRmYNPZaMaFT2Fw6rE0XW8TRQ-L2rzvpfxVQqqU8jjROf7-ZFybz5V9Uufj3Nv6XD1DH6bNwPn-8T4lzoDwce6OpTelcay3pldu8TMpRF-HkGEyIysL7_RZwhQoquPmVycrfpB9SQHlCKs_S1t5QAdj5DIBJJDN58UyhAlajqMvrJcho00WfnjP8qT_yoOUJ2fID41O_RHh7jk0N-nNQkIjQbT7hk5YRs71_oMQiney3Qqif0fTmOWnwkYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یه دختره که پارتنرش یه ترنسه
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/71486" target="_blank">📅 22:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71485">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c1f7e0a7d.mp4?token=luRpwgXxtG8kGZiZSndKyein1GhNJ9G99tSzN86UzCSN_LyA8xnaNemKrkwVZbLdn9DysmfN73EMMzGd8WC-KjA4TbXSE9xHvBOP1eL8h9Ykfgth9buJjW3GVms5qUXB6O4aCBfQD0J-N-Dan3PuzwHZJJ5jPIA7aCfYyd8iWf5J44S7Po8vMwDwGTVfgnyaiLiZg2xI0KRxtfufGgGskoGK_vyGM-7SHB4wuTvqVJDF6x58q1vlWFbEbG0VRRmFsEoNQnBUHsNd0-DpICrsEazd-EPo1nbj5psUrSIENElZ8I6C7Z15m2IkxwmgnCgeQySebd7PtsDakzGpTcCVNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c1f7e0a7d.mp4?token=luRpwgXxtG8kGZiZSndKyein1GhNJ9G99tSzN86UzCSN_LyA8xnaNemKrkwVZbLdn9DysmfN73EMMzGd8WC-KjA4TbXSE9xHvBOP1eL8h9Ykfgth9buJjW3GVms5qUXB6O4aCBfQD0J-N-Dan3PuzwHZJJ5jPIA7aCfYyd8iWf5J44S7Po8vMwDwGTVfgnyaiLiZg2xI0KRxtfufGgGskoGK_vyGM-7SHB4wuTvqVJDF6x58q1vlWFbEbG0VRRmFsEoNQnBUHsNd0-DpICrsEazd-EPo1nbj5psUrSIENElZ8I6C7Z15m2IkxwmgnCgeQySebd7PtsDakzGpTcCVNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای زن دعوت شده به صداوسیما درباره ترامپ و نتانیاهو:
ما میخایم با پول حلقه های ازدواجمون طناب داری بر گردن نتانیاهو و ترامپ بندازیم
درست ۷ کیلو و ۲۰۰ گرم طلا به قاتل ترامپ جایزه میدیم
ما میخایم خون بر شمشیر پیروز بشه
از مامان های محترم تعهد گرفتیم و به مقدار توانشون طلا کمک کردن که به قاتل ترامپ بدیم
از ارزشمند ترین دارایی هامون می‌گذریم تا ترامپ کشته بشه
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/71485" target="_blank">📅 21:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71484">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🇮🇷
۱۰ دقیقه پیش، نیروی دریایی سپاه پاسداران یک موشک کروز ضدکشتی را از سیریک به سمت تنگه هرمز شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/71484" target="_blank">📅 20:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71483">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dcbed492f8.mp4?token=sF5ANiWDrS99WAeKEMRS-SQCVwxgF79t_AxtJEX4fus_goK7KhqUFkSMnEQhZRSINVVXWYdpEBcRGZm0F9_iZyr6pGDJE6w2MM5pptO2LtfFA148LueurnW1WCtEu9TyjNctSQJdzBXo5WWKeW9AcZ1JarOAepQCotZqSteUNNvOCWDN2weHIF1Qy00DUiUDIVdlfl3t_tFx8KmUxK7d5XhktmV8_tOla4HjnMilRa8raCON5Jz1NYtAhVa7rOVzbjyltJEX3owZxZcklV9WSNRlF8rITMNjA-Kdd25Ix5mD_FqjCBcGc1cxf7JdAvtem4gtpa-1pcsuCXbzuMKIYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dcbed492f8.mp4?token=sF5ANiWDrS99WAeKEMRS-SQCVwxgF79t_AxtJEX4fus_goK7KhqUFkSMnEQhZRSINVVXWYdpEBcRGZm0F9_iZyr6pGDJE6w2MM5pptO2LtfFA148LueurnW1WCtEu9TyjNctSQJdzBXo5WWKeW9AcZ1JarOAepQCotZqSteUNNvOCWDN2weHIF1Qy00DUiUDIVdlfl3t_tFx8KmUxK7d5XhktmV8_tOla4HjnMilRa8raCON5Jz1NYtAhVa7rOVzbjyltJEX3owZxZcklV9WSNRlF8rITMNjA-Kdd25Ix5mD_FqjCBcGc1cxf7JdAvtem4gtpa-1pcsuCXbzuMKIYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
آتشفشان ساکوراجیما در جزیره کیوشو ژاپن فوران کرد و خاکستر و مواد آتشفشانی را تا ارتفاع چند هزار فوتی به هوا فرستاد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/71483" target="_blank">📅 20:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71482">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d66564850.mp4?token=mNfhMY7g-n6TsWP5mfHlZTPNvedCPZFMo60DgUPDxJBHL2Hdp4YMtCP52zsdwAgrpQQ7g-F7z7XlQybGNKM2JRyDsQ6wfv4tzoi21fBSMizTa0OXYO6H79lIb-guKoFl1DyB8ZjLlEK5sp-iX3KpvdB7JZH8TIZRBHHvwJm3K-EObymYA5L8ar5TXB6RTZT7eq5_p6Go0y6iWu1mTvDj3KZykwCsMbR0RrG1cYRVPaIWfZEakgpxTrv21qDWKtFmwYs4ApYhnchCvKSrNMTlwZXk5oYztiGolynT7Aih1zkto6pZsNthk9VzQBAaMmEcSELSVxhajQnRX3_QeJ1k0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d66564850.mp4?token=mNfhMY7g-n6TsWP5mfHlZTPNvedCPZFMo60DgUPDxJBHL2Hdp4YMtCP52zsdwAgrpQQ7g-F7z7XlQybGNKM2JRyDsQ6wfv4tzoi21fBSMizTa0OXYO6H79lIb-guKoFl1DyB8ZjLlEK5sp-iX3KpvdB7JZH8TIZRBHHvwJm3K-EObymYA5L8ar5TXB6RTZT7eq5_p6Go0y6iWu1mTvDj3KZykwCsMbR0RrG1cYRVPaIWfZEakgpxTrv21qDWKtFmwYs4ApYhnchCvKSrNMTlwZXk5oYztiGolynT7Aih1zkto6pZsNthk9VzQBAaMmEcSELSVxhajQnRX3_QeJ1k0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
صحبت های عجیب
پوریا بختیاری کارشناس اقتصادی در مصاحبه با علی ضیا درباره ابراهیم رئیسی:
نزدیکان رئیسی گفتند که حاج‌آقا خودش اقرار کرده که اقتصاد متوجه نمی‌شود.
بعد گفتیم خب، یعنی باید برای رئیس‌جمهور کلاس اقتصاد بگذاریم؟
گفتند نه، کلاس اقتصاد که نه؛ حاج‌آقا ذهنش می‌پرد و خسته می‌شود. بیاییم موشن‌گرافی بسازیم.
ما یک تیم انیمیشن آوردیم که برای رئیس‌جمهور مملکت کلیپ‌های اقتصادی درست کند. قانون هم گذاشته بودند که هر کدام از کلیپ‌ها بیشتر از سه دقیقه نشود، چون ذهن حاج‌آقا می‌پرد.
ببینید چقدر این موضوع تلخ و «دارک» است که برای رئیس‌جمهور مملکت و بالاترین قدرت اجرایی، بروی انیمیشن درست کنی تا بلکه اقتصاد را بفهمد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/71482" target="_blank">📅 19:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71481">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90c5de5a1.mp4?token=u0CnQIyp5aO-vtXjq6mC4Nk-gFZcoSVUSNmLYXiR8eqhWBI1rp3kYsnI2li9qcTtFxGMW-hboKS4I9ZB1IrGL07bTBh2iCxTxNBIUKYFFzrRobpx59z41nHDd4U8V5UvEmfEjBC3qj97UKHRx-Q7OLPjI57pt7QzwWPiA5iF8gnU4e1VVWU3KcK5X7WkasAW-R7UPkX43yWwGTgpRi6k82o1Lz0DULCtIvj9O90fNvnOWXNYkp1V7YRvjXl1sGhOoUHm9qVwTyeFxEdugKx_tqOionz5JtGXJJgcJFjyZ6w2Zy5847BkamuW51KpiH3TjIhY-EgSDldxk11wJvxgoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90c5de5a1.mp4?token=u0CnQIyp5aO-vtXjq6mC4Nk-gFZcoSVUSNmLYXiR8eqhWBI1rp3kYsnI2li9qcTtFxGMW-hboKS4I9ZB1IrGL07bTBh2iCxTxNBIUKYFFzrRobpx59z41nHDd4U8V5UvEmfEjBC3qj97UKHRx-Q7OLPjI57pt7QzwWPiA5iF8gnU4e1VVWU3KcK5X7WkasAW-R7UPkX43yWwGTgpRi6k82o1Lz0DULCtIvj9O90fNvnOWXNYkp1V7YRvjXl1sGhOoUHm9qVwTyeFxEdugKx_tqOionz5JtGXJJgcJFjyZ6w2Zy5847BkamuW51KpiH3TjIhY-EgSDldxk11wJvxgoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین پایگاه دریایی نووروسیسک روسیه - بندر اصلی باقی مانده ناوگان دریای سیاه - را با حمله ترکیبی پهپاد و موشک در طول شب هدف قرار داد.
لیست خسارات تایید شده قابل توجه است
؛
ستاد کل ارتش می‌گوید سه کشتی جنگی (مین‌روب ژلزنیاکوف، ناوچه حامل کالیبر، دریاسالار اسن، و کشتی پهلوگیری پیوتر مورگونوف) به علاوه انبار سوخت مورد اصابت قرار گرفته‌اند.
اطلاعات و OSINT اوکراین، ناوچه دریاسالار ماکاروف، یک کشتی موشک‌انداز بویان-ام (غیرعملیاتی ارزیابی شده)، کشتی گشت‌زنی واسیلی بیکوف، چندین قایق موشک‌انداز و دو رادار دفاع هوایی در نزدیکی گلندژیک را اضافه می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71481" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71480">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71480" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71480" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71479">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vp3gm2nea3gH6jK2b0nedwjgXCunD961QIoBAX1qOvn6_JgzpBVB6re7Uxv7shys8ZyTqyyuTwPNrOoh48HVd0v5nwsC6nqLqXiS9U169q1AY06SbTD02kswwGPc0oxSxtOymtBv4zJTvTgvW3yxGeZAWnktL7-TRoEn6fxNZ_l-jGFxsnrDXQrQ_DtXDtsSHs22Dzf-lOoyPyuvMb-7N189ajCHwGr3S4SZnKR_75r_5ZMGXMpKim63cokUWSTyWDhXofiLn4VRbSvNMoI-IOuHVK0AB8jjqd9C73eWcir-NIRVkoz7qoIjIjl-xmzdkJ5gY3DWLrQ1gQBh89-zlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71479" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71478">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYC3EZSUA8uLL24QO7iQcVw_QP0rad6dyecskYfcLQ__SeeD1L8-z0xoRWDMZ6AMbo2VZ6TPys1ObWWxOKn58UcsEtlpOjBZ6vtmjxyCCzBd2pu6fEJIa6902M_ASoNTXD4_qE5gQQYtEyqpzvFcpj0Rzp6G5rvGVCNo2J0RrnR9TlfKgXrteYxgYgayz3nDqA1mS4tTvrraRu6BqwtsJcH6lmy_aY8RzDJ4c4WlurE3jgLdWBiXvxDXvq8OclfjjMeRXUAq8xePmuWTW20ID5nh9e7B-zbrFefWR8ck1T3BdDn0a4rKVO6Xg5u74o1fqwxTl-2pXeE_wxcUG3wJ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
می‌خواهم برای رئیس‌جمهور دونالد جی. ترامپ، خانواده‌اش و مردم آمریکا آرزوی «شانا تووا» (Shana Tova) داشته باشم؛ سالی نو همراه با شادی و سلامتی.
در طول سال گذشته، ایالات متحده و اسرائیل با یکدیگر به پیشرفت‌های تاریخی دست یافته‌اند. ایران و محور شرارتِ آن، ضعیف‌تر از هر زمان دیگری شده‌اند، در حالی که اتحاد میان آمریکا و اسرائیل قوی‌تر از همیشه است.
من به رئیس‌جمهور ترامپ بابت اعمال محاصره علیه رژیم شرور ایران و فشار اقتصادی بر بزرگ‌ترین منبع بی‌ثباتی در جهان، تبریک می‌گویم.
مردم اسرائیل در مقابله با نیروهای ترور، در کنار مردم ایالات متحده و رئیس‌جمهور ترامپ ایستاده‌اند.
در سال پیشِ رو، ما همچنان به تلاش برای امن‌تر ساختن جهان برای همگان ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71478" target="_blank">📅 18:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71477">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0625ae5db9.mp4?token=bxu-lsCeouId_Z2sHZA3nfXZvhbnmlHAgRlqYlamYdclDRb32Nq4mS16UerFMp7em3FFAmlPj2FVGjm3b_0GHSZj8rVlRGOiVqa3b5RFMkmUZieO0SOUO8JFcWzn478RPfuXac2_HqTRD6m-2QjzfwZmxcO4PpxsX4iAJ2oDLgi8JeIvqlMbXHXyygT85vQBWnKmhXDejkXyLVX2XLra6R8Lk_cEZfYMALYQO_arEKKmcYjfGk59e32AezLIXpqCW8OA8wF5opV3loW7dMoFSduXwesxZe1y_EhPw-MW9Q_LhQCC2GeYCTBBnlBaPhdZmJTsME6Lfe615TyiWGnhNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0625ae5db9.mp4?token=bxu-lsCeouId_Z2sHZA3nfXZvhbnmlHAgRlqYlamYdclDRb32Nq4mS16UerFMp7em3FFAmlPj2FVGjm3b_0GHSZj8rVlRGOiVqa3b5RFMkmUZieO0SOUO8JFcWzn478RPfuXac2_HqTRD6m-2QjzfwZmxcO4PpxsX4iAJ2oDLgi8JeIvqlMbXHXyygT85vQBWnKmhXDejkXyLVX2XLra6R8Lk_cEZfYMALYQO_arEKKmcYjfGk59e32AezLIXpqCW8OA8wF5opV3loW7dMoFSduXwesxZe1y_EhPw-MW9Q_LhQCC2GeYCTBBnlBaPhdZmJTsME6Lfe615TyiWGnhNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ما به نیروهای نظامی‌ای که هم‌اکنون در تلاشند تا اطمینان حاصل کنند بزرگ‌ترین حامی تروریسم در جهان — یعنی جمهوری اسلامی ایران  — هرگز و به هیچ وجه به سلاح هسته‌ای دست نخواهد یافت، ادای احترام می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71477" target="_blank">📅 17:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71475">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=Dbtxg8D-rqrC9PT5L9CF0UJx0n5T2dotiAxe5GEJcRLAwghAwV5yEKZO893g6i5e5jobqFLJb8t7PyJ3GTYOrKfxI-Ny3cuZnuKn2fTo1uO0pbioZPtQuwF6nRwlSwLYN8G5wa1Lm0KDICXbrazZcV0_blHjT2__m9W96rzjHKxOez0OZxVYpENTT0Y6ggysmfNrfJ6PveXIlK6xOWXFg0Y9OB-9SpuigeXZyVywwFFJL7tWk49pHBjP6k9Jy_64F-asKLYlJlAk6k8Xv-VjT7mxoHKo5euR2_C2M_N2Jh_7Qi_ahFbSxhduyvHvMcK8RMX62vgV4Zgu15TbCQ9ouQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=Dbtxg8D-rqrC9PT5L9CF0UJx0n5T2dotiAxe5GEJcRLAwghAwV5yEKZO893g6i5e5jobqFLJb8t7PyJ3GTYOrKfxI-Ny3cuZnuKn2fTo1uO0pbioZPtQuwF6nRwlSwLYN8G5wa1Lm0KDICXbrazZcV0_blHjT2__m9W96rzjHKxOez0OZxVYpENTT0Y6ggysmfNrfJ6PveXIlK6xOWXFg0Y9OB-9SpuigeXZyVywwFFJL7tWk49pHBjP6k9Jy_64F-asKLYlJlAk6k8Xv-VjT7mxoHKo5euR2_C2M_N2Jh_7Qi_ahFbSxhduyvHvMcK8RMX62vgV4Zgu15TbCQ9ouQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ واقعه ۱۱ سپتامبر را به جنگ خود علیه ایران پیوند می‌دهد:
به همین دلیل است که امروز می‌جنگیم. ما چاره‌ای نداریم؛ تنها گزینه، پیروزی است. ما سرسختانه می‌جنگیم. برای پیروزی می‌جنگیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71475" target="_blank">📅 17:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71474">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c788d5732.mp4?token=XWJSiDf7XJDdu5mY_XZj1vCoJp2tsRlu14KASpS7Wf0A238kmCzkMKWzPoW--LnI4PkS5oj6uD6pJF2-PCJyOi53CWLpyoISk5LfLlyhYIxedkCJZzwFaLoUQPcEI1VrE6D4tK3Y2iHD_fB_Gc5JbyiLz1DNI_ks68Y5nEzexa2UHZ5yI3nRxK1HtjF9SwOkvO9VdKIlp4-5Bs56D5o8uKPr7x3O2XgEML3hp7sszs1md5rcDVp1exYVVsV4S4UxHUrXrpXIOEMnRJ6sc175iY3cV6G6BkDjouUi5vhGeDufd_LbnUL-K1AnHNaR-9fgHSav_0nvYf_A6ycFgTvumw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c788d5732.mp4?token=XWJSiDf7XJDdu5mY_XZj1vCoJp2tsRlu14KASpS7Wf0A238kmCzkMKWzPoW--LnI4PkS5oj6uD6pJF2-PCJyOi53CWLpyoISk5LfLlyhYIxedkCJZzwFaLoUQPcEI1VrE6D4tK3Y2iHD_fB_Gc5JbyiLz1DNI_ks68Y5nEzexa2UHZ5yI3nRxK1HtjF9SwOkvO9VdKIlp4-5Bs56D5o8uKPr7x3O2XgEML3hp7sszs1md5rcDVp1exYVVsV4S4UxHUrXrpXIOEMnRJ6sc175iY3cV6G6BkDjouUi5vhGeDufd_LbnUL-K1AnHNaR-9fgHSav_0nvYf_A6ycFgTvumw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
آنچه اکنون در مورد ایران شاهد آن هستیم، حیوانی است که در تنگنا گرفتار و زخمی شده است.
این آخرین نفس‌های رژیمی رو به احتضار است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71474" target="_blank">📅 17:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71473">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/971b0d1003.mp4?token=HMTaOdZm2tpnHPhqAHui9TSWaMhg_rbu3Ji0dUXuDfHIok1tMSbMsKNAk_p1Qf4w50gbv4LnseUJ2cOv9sWRSEmsJeAtaqVVnDPeU6VhhDxQQKgTFyPc3hC1ewPpA2_-bgvYNqpX-bJv0sYnTWrkRDnX-WOObq3PXE5AluBWxR7sv6jHcbSQS3AVNVOfclIPjn9WXnh0ijJH0cbakd_a3Ah_iNWyvTtm3UGfLjT-nVfamRJZSmZLwxOdIaT3sL3F1l7FCmRdvSMP2TLuH-qdtP0YY1L5-fkkOK_eRWdXxQIvvQ90GrpmZ2ooUlJjEtNeu2_gNxvmHgXqHJw_U50grg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/971b0d1003.mp4?token=HMTaOdZm2tpnHPhqAHui9TSWaMhg_rbu3Ji0dUXuDfHIok1tMSbMsKNAk_p1Qf4w50gbv4LnseUJ2cOv9sWRSEmsJeAtaqVVnDPeU6VhhDxQQKgTFyPc3hC1ewPpA2_-bgvYNqpX-bJv0sYnTWrkRDnX-WOObq3PXE5AluBWxR7sv6jHcbSQS3AVNVOfclIPjn9WXnh0ijJH0cbakd_a3Ah_iNWyvTtm3UGfLjT-nVfamRJZSmZLwxOdIaT3sL3F1l7FCmRdvSMP2TLuH-qdtP0YY1L5-fkkOK_eRWdXxQIvvQ90GrpmZ2ooUlJjEtNeu2_gNxvmHgXqHJw_U50grg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇱
اعتراض ربات های انسان‌نما در مقابل وزارت امور دیجیتال لهستان و سردادن شعارهایی با مضمون«ما خواهان قانون‌گذاری هستیم»و «از مشاغل دفاع کنید»
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71473" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71472">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3ddeb433.mp4?token=RHrI13O3UrIRYpgZtekIxjzIOnciYtbMEUG_uDH4nByNRQsTBOPKEBZoM19i31Hyf5C9ekySMRsv98MozolzmJY597B39_BiLAXNuiWdsdWdLutqDTXbA1M7xwJLkF1NeO1pTSNCU00goSfsGJQf7nM2tPosk2Ka2y9fVbT2-Leq79Adzm0sL0q0zL5J7cpxv4frLXdWdJDYFjuqbhIo-rDI6Tc8F-YzH4s3fYOJq3CdQ-HdA601MN8PNojksUhISTBFojOPJvHQyej27ocK17T0gFkFUOPWXdWw92pal9FYqkIUT6oiAtdEVWI5ATGZmGwi5pWNk-XmQOKKah8_PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3ddeb433.mp4?token=RHrI13O3UrIRYpgZtekIxjzIOnciYtbMEUG_uDH4nByNRQsTBOPKEBZoM19i31Hyf5C9ekySMRsv98MozolzmJY597B39_BiLAXNuiWdsdWdLutqDTXbA1M7xwJLkF1NeO1pTSNCU00goSfsGJQf7nM2tPosk2Ka2y9fVbT2-Leq79Adzm0sL0q0zL5J7cpxv4frLXdWdJDYFjuqbhIo-rDI6Tc8F-YzH4s3fYOJq3CdQ-HdA601MN8PNojksUhISTBFojOPJvHQyej27ocK17T0gFkFUOPWXdWw92pal9FYqkIUT6oiAtdEVWI5ATGZmGwi5pWNk-XmQOKKah8_PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
❌
🇶🇦
هم‌زمان با نخستین سالگرد حمله هوایی اسرائیل به دوحه (قطر) در سپتامبر ۲۰۲۵ — که نخستین حمله اسرائیل به خاک قطر محسوب می‌شود — تصاویر جدیدی از این رویداد منتشر شده است.
این حمله، مقامات ارشد حماس از جمله «خلیل الحیه»، مذاکره‌کننده ارشد این گروه را در جریان مذاکرات آتش‌بس هدف قرار داد.
اگرچه رهبران ارشد حماس از این حمله جان سالم به در بردند، اما شش نفر، از جمله پسر خلیل الحیه و یک مأمور امنیتی قطری، کشته شدند.
این تصاویر جدید که منبع آن‌ها شبکه تلویزیونی «العربی» (Al-Araby TV) اعلام شده، لحظه اصابت را از زوایایی که پیش‌تر دیده نشده بودند، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71472" target="_blank">📅 16:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71471">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e182f67792.mp4?token=XmpYdciRstj6eWjKna_U-kWMZDrp7UpQJiOxJ8RdyIufFR9A0awz6T3oX10NWlt18gHoyxQNec-ZJ4PjHQpLopGPnrgn6VzSLaQm1FLOJpBMjpz7-6YYit0hGzGvWjOV4GiCUf1c6LGMaAPGZBeRqgvwwbk3XjcklXN4gLMzLsQa7jZyAg7mUaklcpm0Q2ApEuBhTl_CtV4GnopjKgv71Y0FPyEECRauxVosKbH0NZdY8Ydha8vk5_FjjCVIz7WGYeyTDhUZIlKixHi4aMcqDr9tw1uqPGZYswS6X5cewqj10zje57RjnFVEJ6WDABb7o7PllM-hxT2Vm7Y-mKIWHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e182f67792.mp4?token=XmpYdciRstj6eWjKna_U-kWMZDrp7UpQJiOxJ8RdyIufFR9A0awz6T3oX10NWlt18gHoyxQNec-ZJ4PjHQpLopGPnrgn6VzSLaQm1FLOJpBMjpz7-6YYit0hGzGvWjOV4GiCUf1c6LGMaAPGZBeRqgvwwbk3XjcklXN4gLMzLsQa7jZyAg7mUaklcpm0Q2ApEuBhTl_CtV4GnopjKgv71Y0FPyEECRauxVosKbH0NZdY8Ydha8vk5_FjjCVIz7WGYeyTDhUZIlKixHi4aMcqDr9tw1uqPGZYswS6X5cewqj10zje57RjnFVEJ6WDABb7o7PllM-hxT2Vm7Y-mKIWHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه های این بانو درباره وظایف زن مرد توی ازدواج ۳ میلیون ویو گرفته واقعا مفید بود
😏
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71471" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71470">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28a9989cd.mp4?token=Pz3XJ9lT2odIKr7PEEWddXautiBeob1iSxIaMzun61QjhTn0nFFGXfkcePjEpc69a2DryQieu6q5U3RuLqUC6wG2D6df9HsuDfJP6WmWP6xRaQIcZbDhEsXyc0PfYgy1ztHPbcQmfxYVej2BfbI6IHus7-0HTcdt720szp926QtYlrUlDowWXcVQCk9lgsr2acVOAHhuzgvZCmignZchvNqYHl7kcsnDP-fpQOPNUV1tMds97WLtZTZG4VsqCq8RECnue68SeoqXxb26tzWqUz6erdtdud6pXEn7qd-PBAep2tA-GiX8IBQC6Ou-s-R3u6hyFxEahIKchoGfqnpekw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28a9989cd.mp4?token=Pz3XJ9lT2odIKr7PEEWddXautiBeob1iSxIaMzun61QjhTn0nFFGXfkcePjEpc69a2DryQieu6q5U3RuLqUC6wG2D6df9HsuDfJP6WmWP6xRaQIcZbDhEsXyc0PfYgy1ztHPbcQmfxYVej2BfbI6IHus7-0HTcdt720szp926QtYlrUlDowWXcVQCk9lgsr2acVOAHhuzgvZCmignZchvNqYHl7kcsnDP-fpQOPNUV1tMds97WLtZTZG4VsqCq8RECnue68SeoqXxb26tzWqUz6erdtdud6pXEn7qd-PBAep2tA-GiX8IBQC6Ou-s-R3u6hyFxEahIKchoGfqnpekw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شرکت پخش فرآورده‌های نفتی:
موفق شدیم رقم ۱۰ هزارتومان را در پمپ بنزین‌ها نشان دهیم و برچسب‌های صفر ثابت را بردارید
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71470" target="_blank">📅 15:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71469">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc8b06f7d.mp4?token=YXV2h17QdHJ7NXgeDB-TUzphQPxdc6Nscc1hqWx-xzCKj59UDqTX4VndTlT-q-two-NXzQ8hJhWHLaqxJNJxncLUXM16xTYs5nPuB94kDvGS-6Irec_D3exusJ7xOAOc6mRn3KRp1ExYuW0DJLhv7yh4IjIDsI21U0lJPW19LGaXVEugtlKNiW_8PsVNBfN5KJ5o49P50QwMHZjY_5Pgiu_Lm_67FifqdjKeJAzcL-4unRdvActIHe-dPfmKOfdBuMqbOHLdtQArVqhF1od7NEQ-ojT_IbLZB6Tqpm_tTUz3NhdeYIi5095sFVx6aoOTcx5NgVn11VFH13xQ_BTSHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc8b06f7d.mp4?token=YXV2h17QdHJ7NXgeDB-TUzphQPxdc6Nscc1hqWx-xzCKj59UDqTX4VndTlT-q-two-NXzQ8hJhWHLaqxJNJxncLUXM16xTYs5nPuB94kDvGS-6Irec_D3exusJ7xOAOc6mRn3KRp1ExYuW0DJLhv7yh4IjIDsI21U0lJPW19LGaXVEugtlKNiW_8PsVNBfN5KJ5o49P50QwMHZjY_5Pgiu_Lm_67FifqdjKeJAzcL-4unRdvActIHe-dPfmKOfdBuMqbOHLdtQArVqhF1od7NEQ-ojT_IbLZB6Tqpm_tTUz3NhdeYIi5095sFVx6aoOTcx5NgVn11VFH13xQ_BTSHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔞
اگه بدون کاندوم رابطه جنسی برقرار می‌کنید؛
این پست رو یه گوشه‌ای تو تلگرامتون ذخیره کنید که یه روزی بدجوری به کارتون میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71469" target="_blank">📅 15:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71465">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54fcf2b7ac.mp4?token=JJ7R2g7Pzl-jmJV_xadMOIfVla9kyeC1ouWgi_Ovfi2Y0wljUp9XALrBQo2KH9dS6Ht7baFagrlWO2Lbnv1w6pfO0W1GZliUPnhQimYg4zN-RrRk6JyKp6llKIlZoOQMjj0m2_-XID-JaUT7pBqHKNwitZ_DDHgLvRc-qcF8_b872FHwCOUdO-L_xq-Ysm5ucVw-0GlqFxfu3MzmiJs_nR5xflhaDlAK3zgxYOE36T4cAyB7HRCi4KTUgV7UTp4zjznGsE808gDbLX5lO3x27xgy09HDCBMSCUUBCCg85eZwVb_lCXKNwtSFp88R15VQ6457BVGKTEI449ay5KyZ4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54fcf2b7ac.mp4?token=JJ7R2g7Pzl-jmJV_xadMOIfVla9kyeC1ouWgi_Ovfi2Y0wljUp9XALrBQo2KH9dS6Ht7baFagrlWO2Lbnv1w6pfO0W1GZliUPnhQimYg4zN-RrRk6JyKp6llKIlZoOQMjj0m2_-XID-JaUT7pBqHKNwitZ_DDHgLvRc-qcF8_b872FHwCOUdO-L_xq-Ysm5ucVw-0GlqFxfu3MzmiJs_nR5xflhaDlAK3zgxYOE36T4cAyB7HRCi4KTUgV7UTp4zjznGsE808gDbLX5lO3x27xgy09HDCBMSCUUBCCg85eZwVb_lCXKNwtSFp88R15VQ6457BVGKTEI449ay5KyZ4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
در ۱۱ سپتامبر ۲۰۰۱، شبکه تروریستی القاعده به رهبری اسامه بن‌لادن، حملاتی هماهنگ‌شده علیه ایالات متحده انجام داد.
🗣️
در این عملیات، ۱۹ عضو القاعده چهار هواپیمای مسافربری را ربودند.
🇸🇦
۱۵ نفر تبعه عربستان سعودی.
🇦🇪
۲ نفر از امارات متحده عربی.
🇪🇬
۱ نفر از مصر.
🇱🇧
۱ نفر از لبنان.
دو هواپیما به برج‌های دوقلوی مرکز تجارت جهانی در نیویورک برخورد کردند و هواپیمای سوم به ساختمان پنتاگون در ویرجینیا اصابت کرد.
هواپیمای چهارم نیز در پنسیلوانیا سقوط کرد؛ پس از آنکه مسافران برای بازپس‌گیری کنترل هواپیما تلاش کردند.
در مجموع، ۲٬۹۷۶ نفر در این حملات کشته شدند و هزاران نفر نیز مجروح شدند.
تحقیقات گسترده FBI، ارتباط مستقیم این حملات با القاعده و نقش این شبکه در سازماندهی و آموزش هواپیمارباها را تأیید کرد.
پس از حملات، آمریکا عملیات نظامی در افغانستان را با هدف سرنگونی حکومت طالبان و مقابله با القاعده آغاز کرد.
اسامه بن‌لادن سرانجام در ۲ مه ۲۰۱۱ در پاکستان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71465" target="_blank">📅 14:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71464">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇹🇷
پهپاد «آکینجی» (AKINCI) ترکیه اکنون با موفقیت موشک‌های UAV-300 و UAV-122 ساخت شرکت «روکت‌سان» (ROKETSAN) را آزمایش و شلیک کرده است.
نقطه عطف این آزمایش، شلیک موشک بالستیک مافوق‌صوت UAV-300 بود که با اصابت دقیق به هدف در فاصله‌ای بیش از ۲۵۰ کیلومتر، توانمندی آکینجی در انجام حملات بالستیک دوربرد را به اثبات رساند.
موشک کوچک‌تر UAV-122 نیز در جریان این آزمایش با موفقیت شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71464" target="_blank">📅 14:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71461">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd5a9f3c7.mp4?token=PN--3f9019znpTS1YlX6d1nF51wONd20308_KUg43nR8BrsjIHnE4UJBHsDdPX5M84GkftScenTajZBtCkoETbv441XtpplAmk4fXymnV2BqPdsNI3IL1G3W_NDTmQbZdX9KPawqRyqptfJExR3HSoTJoFYhgB1WybE6AaYb_4vuAdopkSsWkWBUEvBZLIDz-bfmwtIZRoPZE2xzQDZfHQgcCnzaqXklu43I5nvgmTlTx2TMdHRMLH2IiTAwbzXfQ6yzmABB8aYQg5XhzZx9h0Mb0HR_Nrkn7k59GDKfa7kz7HzJq70N2HnO6DgFs-HQffD6Typz9JgGJD_aOHY7dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd5a9f3c7.mp4?token=PN--3f9019znpTS1YlX6d1nF51wONd20308_KUg43nR8BrsjIHnE4UJBHsDdPX5M84GkftScenTajZBtCkoETbv441XtpplAmk4fXymnV2BqPdsNI3IL1G3W_NDTmQbZdX9KPawqRyqptfJExR3HSoTJoFYhgB1WybE6AaYb_4vuAdopkSsWkWBUEvBZLIDz-bfmwtIZRoPZE2xzQDZfHQgcCnzaqXklu43I5nvgmTlTx2TMdHRMLH2IiTAwbzXfQ6yzmABB8aYQg5XhzZx9h0Mb0HR_Nrkn7k59GDKfa7kz7HzJq70N2HnO6DgFs-HQffD6Typz9JgGJD_aOHY7dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حمله شناورهای بدون سرنشین (USV) اوکراین به بندر سوچی در منطقه کراسنودار روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71461" target="_blank">📅 13:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71460">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijWuIy3deFq6pthaOdn_85E8uBOLcXB75CRReS88ssIexrJ12S4lQ6-2h2qvE3Z9JH_kBJ-S2GtHhG5wLhztCACZz-tu65CcgfaI84L3T39Q2UBkNV86aMXDcc0VFMBr-Fwf6MclHr6TlyVFA4jb-tnvHNxHV0uXEln5WiPXH9Ujl9yZvtGv6ryIgID4j0A0cELnvTxYK6eMsqiVUzY_6NzlLoyP7elTtGWsf2jIUZSv5bHsYgvcXABXkvi_-75HRiwJbPNhRCdhiBDdJ3TjO-cbLWKMWahau0xhq4LN1dBiyvJlHh1yCygW5IBS2HIfd8gmj-LHmHsEdPfRCuuTwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇾🇪
🇾🇪
حوثی‌های یمن جزیره پریم (میون) را تصرف کرده و کنترل خود را بر تنگه باب‌المندب تکمیل کردند.
⏺
🗞
خبرگزاری رویترز نیز در گزارشی جداگانه اعلام کرده است؛
حوثی ها به شهر ساحلی «ذوباب» — که درست در کنار این تنگه واقع شده — رسیده‌اند.
حوثی‌ها اکنون تقریباً تمام نوار ساحلی یمن در دریای سرخ را در کنترل خود دارند.
این دستاورد سرزمینی را می‌توان از نظر راهبردی، مهم‌ترین پیشروی در کل جنگ یمن دانست.
جزیره پریم در میانه این تنگه ۲۹ کیلومتری قرار گرفته و عملاً آن را به دو مسیر کشتیرانی مجزا تقسیم می‌کند.
تسلط بر این جزیره و همچنین نوار ساحلی مجاور آن بدین معناست که حوثی‌ها می‌توانند کشتی‌های عبوری را با استفاده از توپخانه و تسلیحات کوتاه‌برد تهدید کنند؛ نه صرفاً با موشک‌های دوربرد و پهپادهایی که از مناطق داخلی‌تر شلیک می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71460" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71459">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71459" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71459" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71458">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVqBzBOc3Mp-Q_YyXYq0-xtXWG3wizdF9AnxKRnmuIqLxzgyyoM9CiTzLU9hzmwmOPhBQjXwUFGHWOLSSFcayZ2WOqsMRup7vBf_4_nJ53AWDK50f8yVc4pkbuthzCsAFYEH3reRtcPepQU6lHdde_w5Twx_jjXqF-tAhio3abLUGPDZ0pkf5eGr0Z85IJ2c4z7uCm8UtTPdGgP0O1FYp1U48mPM4El0Msg8bamm9QYP9Zs39XlUAXiw7MnY2BjK2EurVa38SuUfUvPvm5S0YqXbc3pt6E5WWnEqlv0YrkG4aMPJeNzZJTuuRQyqnkRkkBP7F6NsPYg-y9T3PI2PlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
والنسیا
🆚
سویا
فیورنتینا
🆚
ونزیا
شالکه
🆚
انیون برلین
مارسی
🆚
رن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71458" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71457">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4149a89627.mp4?token=LMPeXuc1a3jMSVYGyh0AHObB1Tp8zlWZ6H4TWHoWAagZGVyURT1cOBtyGGwnLLk6mvAvQJlLIJVN2WOC6QFcC6xbbg4qIzIFK57mFHkwPgYM90VwgFR2Rpd-aIKDJHQC41flobV3EGJv5wEWdhDmGRUkaZuGGMIKhe40pwPywpnrCX8un7FRMtM2yqit3Pjq7T26ndFe5cee9bPGmD23LG6AD5XzmmfRV-CjIGJhyGhOjEHpYh1n2Gcz1DxRpd8ZoU0tkrolJl2Y3R5IE0RnA7-SYcJGx0zqBRsGQiEEiCw2KpVsoWSCZ80RdCdKhjXq7sYrvtGuxqVZ4bF8TMUTYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4149a89627.mp4?token=LMPeXuc1a3jMSVYGyh0AHObB1Tp8zlWZ6H4TWHoWAagZGVyURT1cOBtyGGwnLLk6mvAvQJlLIJVN2WOC6QFcC6xbbg4qIzIFK57mFHkwPgYM90VwgFR2Rpd-aIKDJHQC41flobV3EGJv5wEWdhDmGRUkaZuGGMIKhe40pwPywpnrCX8un7FRMtM2yqit3Pjq7T26ndFe5cee9bPGmD23LG6AD5XzmmfRV-CjIGJhyGhOjEHpYh1n2Gcz1DxRpd8ZoU0tkrolJl2Y3R5IE0RnA7-SYcJGx0zqBRsGQiEEiCw2KpVsoWSCZ80RdCdKhjXq7sYrvtGuxqVZ4bF8TMUTYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کارشناس صداسیما: ما ۵۰۰ میلیون تُن طلا داریم.
ـ مجری:  الحمدلله
+ کل طلای استخراج شده تو جهان ۲۲۰ هزار تنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71457" target="_blank">📅 12:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71456">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/27045da6d6.mp4?token=IUdmVVJgPuHwHtQawibI7NxFbuP3OkLNJdpMj8Klrnf42llpglKY7lL10FjkAI3JWVg6s_cfpabVKdJ395gJx_K_1sThFs3JXmN8x_ivx4VWHw3of80mLxMGup_PMO7hRMczg8deJKx1NvopNTYjRMan7dPbRMUmr27m1VP48awRBOiitwFRMt--2IpezeOLw-5qwVIzcjxmaHltoTdb1J9xehb7C1veKCiP8XH0PRP5t3dyweUW-xaTRsayaFyiYydDBW98RTYDH_0v8z1Jvypoap7-WRcHnOknmRmW9hRn7qk8B1yYem7Y8QCIxzyEho_xMY7nVCg9mr-MrDGtFw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/27045da6d6.mp4?token=IUdmVVJgPuHwHtQawibI7NxFbuP3OkLNJdpMj8Klrnf42llpglKY7lL10FjkAI3JWVg6s_cfpabVKdJ395gJx_K_1sThFs3JXmN8x_ivx4VWHw3of80mLxMGup_PMO7hRMczg8deJKx1NvopNTYjRMan7dPbRMUmr27m1VP48awRBOiitwFRMt--2IpezeOLw-5qwVIzcjxmaHltoTdb1J9xehb7C1veKCiP8XH0PRP5t3dyweUW-xaTRsayaFyiYydDBW98RTYDH_0v8z1Jvypoap7-WRcHnOknmRmW9hRn7qk8B1yYem7Y8QCIxzyEho_xMY7nVCg9mr-MrDGtFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به زنش گفته دست پختت رو سگم نمیخوره! اونم برای اینکه شوهرش رو ضایع کنه، رفته غذاشو گذاشته جلوی سگ!
در نهایت سگه این شاهکارو خلق کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71456" target="_blank">📅 11:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71455">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c6ecedd2b.mp4?token=beiQxyoHCoIec8y-R15gmLEvUeP7n0fHPraC0uewdxaPBwXyUbzvkfWtMEqgUeNF5rwUVpbxUQjlEDvwqQtoe-0sxWUn0OTjfkEkoq9FYBXJMwm0XsFxGMsmop9J6LHCgYfpoyWBEWZFLqmPyeoFKFE8RORUEt0xGVcbJwIg0lvMe8y4bU9keAeBL-E_JgSnONk8Ax_sXBBEtiZv0OmYbjyGl6NgoYskgabA270qXVmvlt3Zzaxywz_CgIlq93QkF3CiMSDS7Q7w_ARuBpo9f5Aq4z-xXXB0MWoFG4mJeJHT1WZDGPl4fzM1ZTTdp1QdxSg-oi7VSnsd0xX6qoBXlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c6ecedd2b.mp4?token=beiQxyoHCoIec8y-R15gmLEvUeP7n0fHPraC0uewdxaPBwXyUbzvkfWtMEqgUeNF5rwUVpbxUQjlEDvwqQtoe-0sxWUn0OTjfkEkoq9FYBXJMwm0XsFxGMsmop9J6LHCgYfpoyWBEWZFLqmPyeoFKFE8RORUEt0xGVcbJwIg0lvMe8y4bU9keAeBL-E_JgSnONk8Ax_sXBBEtiZv0OmYbjyGl6NgoYskgabA270qXVmvlt3Zzaxywz_CgIlq93QkF3CiMSDS7Q7w_ARuBpo9f5Aq4z-xXXB0MWoFG4mJeJHT1WZDGPl4fzM1ZTTdp1QdxSg-oi7VSnsd0xX6qoBXlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این آقا یه ویدیو از چینی‌ها گذاشته که یه شیشه‌دودی واسه ماشین ساختن که با یه بیلبیلک میشه درصد دودی بودنش رو کم و زیاد کرد؛
حالا به جای اینکه پشمای ملت از تکنولوژی بریزه، 98 درصد کامنت‌ها اینه:
بهترین مکان واسه اونایی که مکان ندارن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71455" target="_blank">📅 11:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71454">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c4f2b29b.mp4?token=TyWzkrufhByzTO5RjtouVcHXJX15kr50FemdyTagjRA_PUnuuSL2GFhUJLHOD1_Vb9foWyOLJv9Bon121tUmaycjCwSCAnuxJUct1CaiOQ7yhaU88c_d8sx5mWbuDajjeUd0ACkvEPbxMFSk87flvqd6jD44GFMVhSNGG6l2QOasiRIGd7DyciBnc5QS4y0K5dj2sNZ7IUiyLHGa9mE_RTw-EAjnjM-zOlVq0aXsLJuDghwjvNg_FlJK-L4RlRprBnPhQTg-3y_-iCdQNAcxakxPCvixV7aecVfxrWLNxES9fqV7ccGEkUujKxIdYuo2VlbsE8l9cYPOnbXJYXzJJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c4f2b29b.mp4?token=TyWzkrufhByzTO5RjtouVcHXJX15kr50FemdyTagjRA_PUnuuSL2GFhUJLHOD1_Vb9foWyOLJv9Bon121tUmaycjCwSCAnuxJUct1CaiOQ7yhaU88c_d8sx5mWbuDajjeUd0ACkvEPbxMFSk87flvqd6jD44GFMVhSNGG6l2QOasiRIGd7DyciBnc5QS4y0K5dj2sNZ7IUiyLHGa9mE_RTw-EAjnjM-zOlVq0aXsLJuDghwjvNg_FlJK-L4RlRprBnPhQTg-3y_-iCdQNAcxakxPCvixV7aecVfxrWLNxES9fqV7ccGEkUujKxIdYuo2VlbsE8l9cYPOnbXJYXzJJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
از سالن زیبایی مذهبی برای عروسی رونمایی شد، از آپشن‌های خاص این سالن میشه به این موارد اشاره کرد:
رد شدن از زیر قرآن هنگام ورود به سالن.
عکس گرفتن با سران مملکت که کشته شدن.
پخش مداحی و قرآن به جای موزیک.
داشتن وضو توسط پرسنل قبل از میکاپ.
خوندن نماز دسته جمعی برای خوشبختی.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71454" target="_blank">📅 10:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71453">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9e0d9418.mp4?token=m5-DOSnoiJQB3LhBOZDEAkF6_er2FdvZa4sXtGJxBfjV805o6tJggi6F2veLN8QsxKA3a4-AdP-AjZljTrKBZYP-kNedmPV0ZUZYUm1kiP043I63bEf_y7vgFsP9_3VPHSp2KtDFxOZiW4wNmuoZ8PNwjF3bdsI6AMz1cIFYRuBhnHxhGyVkLya5FDb5nzZ4bEMnDMOS1pW088R1J14bzJmqRiFVFJ8rEj6VGoLpPWWP74myfu1hA6dY8c2edtjry6EWWGArjjgRvRF6LyPsGFyxXPGyVNsmxz66b4yh-bzWXafkxVqb-e1R4XWC4bBSo65XzrSoI9LIMGsHLmbShjPME4Uam3Aa6TcXPe2EMiCBo6XtH0ZS1xTF_aykpCB8rW6IodRFrlCrnfplPmPUYvW5zdvEdQSior8z4NtD8iyQ9h4vh1-00U7W9jRs3i3KzrFZJBAk2ha0I6zNCbn6chqWDJtV3eNJKUBDMPwAeQVSLNQSaZ9SM07ceGCsI2aWLt24lO8uttaCAQaJwhJLMKBjB8FTSqgcJiQXjCcE3JOIOobCgh3jyWMb5LhjaB9UC8707D1VasETZt0tMV5l13A8ZpTUTtBaSp2K5XHJ_0r0MOAX1UvBEPgRi2kpdRz_roz4mE19_LS8-S_NmsQ4jF714ZA1-kc0X3-twIfGRK0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9e0d9418.mp4?token=m5-DOSnoiJQB3LhBOZDEAkF6_er2FdvZa4sXtGJxBfjV805o6tJggi6F2veLN8QsxKA3a4-AdP-AjZljTrKBZYP-kNedmPV0ZUZYUm1kiP043I63bEf_y7vgFsP9_3VPHSp2KtDFxOZiW4wNmuoZ8PNwjF3bdsI6AMz1cIFYRuBhnHxhGyVkLya5FDb5nzZ4bEMnDMOS1pW088R1J14bzJmqRiFVFJ8rEj6VGoLpPWWP74myfu1hA6dY8c2edtjry6EWWGArjjgRvRF6LyPsGFyxXPGyVNsmxz66b4yh-bzWXafkxVqb-e1R4XWC4bBSo65XzrSoI9LIMGsHLmbShjPME4Uam3Aa6TcXPe2EMiCBo6XtH0ZS1xTF_aykpCB8rW6IodRFrlCrnfplPmPUYvW5zdvEdQSior8z4NtD8iyQ9h4vh1-00U7W9jRs3i3KzrFZJBAk2ha0I6zNCbn6chqWDJtV3eNJKUBDMPwAeQVSLNQSaZ9SM07ceGCsI2aWLt24lO8uttaCAQaJwhJLMKBjB8FTSqgcJiQXjCcE3JOIOobCgh3jyWMb5LhjaB9UC8707D1VasETZt0tMV5l13A8ZpTUTtBaSp2K5XHJ_0r0MOAX1UvBEPgRi2kpdRz_roz4mE19_LS8-S_NmsQ4jF714ZA1-kc0X3-twIfGRK0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر موقع پریود اومده نوار بهداشتی استفاده کنه و با یه صحنه شوکه کننده مواجه شده!
خودتون ببینید...
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71453" target="_blank">📅 10:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71452">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6849173423.mp4?token=WOR3dGXCemMvtopw-mG6fLVN45vr5Y3mHyG4ThXdvQOlCJ1k3MGA4AjHB1QhBQBGfYXdNmyn8jk5sG_rJkG8Qk9F3lJyZ7-JsVeEDxgUO0h7IzcdlVe5kwYDzdR_AWZ5Bmh5ldhMtSGtwYk5NTV63qnYH366w9XlPRKZ8hYPocSSzqSzn7r-2pO_n9KgAza4t5fetXoWjx0gIvaxBodZwjo3yMr2fafUYHQI3yQnFxxfgAermMZ6b1K2jvAmTkvTYiQz7Jta2A381ePvWPTybxfnUTHC_Q29WfwTXPrG-Qdi5lGdbY3zfhAlMCK2HDXfMDuYqxwyLRVYxHKrqtc9PgaHVpnZR1pW06W1g1vaCMQ57o1Wa_e8dS3diKFbnKgeNWd0YI3qeixB-fz0V8L-gU2wL6bv_xWmWkjugOt7JtkLQIBaTq_FuZILmRbXcYzXddPLT5rkgmM7jo3ceHWVjTTbThgxVVhOjPQBwvtAXm8ehOTVbI1PPcuitA-XTM6M4CbGZ5tuyWFVbbltk7FdjdVSoljSXZB7vt_rdzfNS6nd5efx5ApAfcFDaXulzSp2P60DjR379EPTlFqf0kwhgpbEB_6t1PcKzvNRPfUuPle_oI4Z2lKARS9aUo9itFXzbDdMGypm289g70amV1qjfXZ4aZpeWAROigbE67jkRJ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6849173423.mp4?token=WOR3dGXCemMvtopw-mG6fLVN45vr5Y3mHyG4ThXdvQOlCJ1k3MGA4AjHB1QhBQBGfYXdNmyn8jk5sG_rJkG8Qk9F3lJyZ7-JsVeEDxgUO0h7IzcdlVe5kwYDzdR_AWZ5Bmh5ldhMtSGtwYk5NTV63qnYH366w9XlPRKZ8hYPocSSzqSzn7r-2pO_n9KgAza4t5fetXoWjx0gIvaxBodZwjo3yMr2fafUYHQI3yQnFxxfgAermMZ6b1K2jvAmTkvTYiQz7Jta2A381ePvWPTybxfnUTHC_Q29WfwTXPrG-Qdi5lGdbY3zfhAlMCK2HDXfMDuYqxwyLRVYxHKrqtc9PgaHVpnZR1pW06W1g1vaCMQ57o1Wa_e8dS3diKFbnKgeNWd0YI3qeixB-fz0V8L-gU2wL6bv_xWmWkjugOt7JtkLQIBaTq_FuZILmRbXcYzXddPLT5rkgmM7jo3ceHWVjTTbThgxVVhOjPQBwvtAXm8ehOTVbI1PPcuitA-XTM6M4CbGZ5tuyWFVbbltk7FdjdVSoljSXZB7vt_rdzfNS6nd5efx5ApAfcFDaXulzSp2P60DjR379EPTlFqf0kwhgpbEB_6t1PcKzvNRPfUuPle_oI4Z2lKARS9aUo9itFXzbDdMGypm289g70amV1qjfXZ4aZpeWAROigbE67jkRJ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
❌
ویدیویی پشم‌ریزون که ارتش اسرائیل از عملیات تخریب تونل‌های زیر ارتفاعات علی‌الطاهر در جنوب لبنان منتشر کرده
😨
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71452" target="_blank">📅 09:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71451">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c57019ecf0.mp4?token=bza0V80qWIMVqmBgr8VxT6-pk5vdG9u0ExXA-hxB1yuEHew2N8BMpZvZ4Qr3BOAvml6bFUfc5FbaBVlXmWOencnpyT09JbblXF2tQwSwOcCw2OS3jEAgDhyQANRsIxQ9zpBEOzLDErSj86QPZUbkR1NCmzHbn3yJQkQrmpLMV7TVdrcRQF7LGItexwHZT4_KJeMTawNA2gKp9XfBMgZjmmDOkATNcGN2IN5KFIlseapSgo7bDZB0bOQ4WFb317DUorSHn2nF0ykM4hErE_CkkwEUw58i0O6Imj4GqQrzfAoX_x1zd4zN56xjaOB57zC5GpK-KmN1qgMovDtFhwp9RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c57019ecf0.mp4?token=bza0V80qWIMVqmBgr8VxT6-pk5vdG9u0ExXA-hxB1yuEHew2N8BMpZvZ4Qr3BOAvml6bFUfc5FbaBVlXmWOencnpyT09JbblXF2tQwSwOcCw2OS3jEAgDhyQANRsIxQ9zpBEOzLDErSj86QPZUbkR1NCmzHbn3yJQkQrmpLMV7TVdrcRQF7LGItexwHZT4_KJeMTawNA2gKp9XfBMgZjmmDOkATNcGN2IN5KFIlseapSgo7bDZB0bOQ4WFb317DUorSHn2nF0ykM4hErE_CkkwEUw58i0O6Imj4GqQrzfAoX_x1zd4zN56xjaOB57zC5GpK-KmN1qgMovDtFhwp9RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ:
اگر ایران سلاح هسته‌ای داشت، ما با آن‌ها تماس می‌گرفتیم و می‌گفتیم: «جناب، آیا ممکن است با هم دیداری داشته باشیم؟»
آن‌وقت رفتارمان با آن‌ها بسیار متفاوت می‌بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71451" target="_blank">📅 08:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71450">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534815e8ce.mp4?token=CzNgT05DqzGU45mMknYBy-s5gYqS_w78igrFmOMaWHs21SZlBv9JCPRfFW83_qcrcwQ4RuOmT1fUnpbLt89v3ttBVKV-Iwfqb2F5X2XoTegwgN27fn5kDMknw6dHV1rF6ccgHNO4vGh-VtncSISa5mg56Di3UmjgnAu7eIFLb4IFwP1Roh19mJjw86TjzvuJZiP66jjZ-bNVHBdN94ZJi4vfmJr5o4M4gCkfbJ9hEJZWNjbnIpdPQDn7JqyLuzDeu-53QlvAcPdHiWghA9bpvtG2lVUgl9J-ME5iweNtVORz8uLgv3Lvz1JCnI_Z5W4iOtm_zrJLRFQxhkeyh8KcoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534815e8ce.mp4?token=CzNgT05DqzGU45mMknYBy-s5gYqS_w78igrFmOMaWHs21SZlBv9JCPRfFW83_qcrcwQ4RuOmT1fUnpbLt89v3ttBVKV-Iwfqb2F5X2XoTegwgN27fn5kDMknw6dHV1rF6ccgHNO4vGh-VtncSISa5mg56Di3UmjgnAu7eIFLb4IFwP1Roh19mJjw86TjzvuJZiP66jjZ-bNVHBdN94ZJi4vfmJr5o4M4gCkfbJ9hEJZWNjbnIpdPQDn7JqyLuzDeu-53QlvAcPdHiWghA9bpvtG2lVUgl9J-ME5iweNtVORz8uLgv3Lvz1JCnI_Z5W4iOtm_zrJLRFQxhkeyh8KcoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
دیشب ما ۲۲ قایق را از تنگه هرمز بیرون راندیم. می‌دانید، ما کنترل تنگه را در دست داریم. آن‌ها کنترل تنگه را در دست ندارند. آن‌ها هیچ‌چیز را کنترل نمی‌کنند.
آن‌ها تورم ۳۰۰ درصدی دارند. حقوق ارتش خود را نمی‌پردازند. حقوق نیروهای انتظامی‌شان را هم نمی‌دهند.
و بالاخره زمانی فرا می‌رسد که ارتش و نیروهای انتظامی دست از شلیک به معترضان برمی‌دارند. شگفت‌انگیز است که چطور آن‌ها [تاکنون] چنین کاری می‌کنند.
می‌دانید، چین با استفاده از تانک ارتش این کار را با موفقیت انجام داد. یادتان هست؟ کشورهای دیگر نتوانستند. ترکیه نتوانست این کار را بکند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71450" target="_blank">📅 08:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71449">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fa815d3aa.mp4?token=ne4C9x6WPmEfWzizS64jXKZ9FlP7YgbXmgIjuCo0IetpUHEe0I0z6sYg8_LLWHo4qvQg0ZejFugM9cjcKOvfjprr5hEydrk_zBcBRlCkCmZEjDADirzmy2BZ-Jyf3hN6gNIDTlnBWEdQFg7PWntspw7mG_U7ETsC5gA_WIP_b8dsAfssVkkxch7RNebcJFjw0yCO9APdqZTRG6mSljpJGTKGdeSII97e-vklwgVNyEqgHU3doUDeJC7qJa6TMI_KWbrv4kNzFT7rZuVXx2jbM9MOYx_sadX9SQGTnzsHLSxRm-UBModcDk0PuLkA1QdSm0R3_aFoMgDGFzZczx1bPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fa815d3aa.mp4?token=ne4C9x6WPmEfWzizS64jXKZ9FlP7YgbXmgIjuCo0IetpUHEe0I0z6sYg8_LLWHo4qvQg0ZejFugM9cjcKOvfjprr5hEydrk_zBcBRlCkCmZEjDADirzmy2BZ-Jyf3hN6gNIDTlnBWEdQFg7PWntspw7mG_U7ETsC5gA_WIP_b8dsAfssVkkxch7RNebcJFjw0yCO9APdqZTRG6mSljpJGTKGdeSII97e-vklwgVNyEqgHU3doUDeJC7qJa6TMI_KWbrv4kNzFT7rZuVXx2jbM9MOYx_sadX9SQGTnzsHLSxRm-UBModcDk0PuLkA1QdSm0R3_aFoMgDGFzZczx1bPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
حتی نومحافظه‌کاران هم می‌گویند اگر قرار است وارد ایران شوید، باید تمام‌عیار وارد شوید؛ فقط بروید و کارشان را تمام کنید.
🇺🇸
ترامپ:
خب، شاید به خاطر انتخابات چنین کاری نکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71449" target="_blank">📅 08:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71448">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2230f2a78e.mp4?token=odgYKwBylkF0oa9sYFK_OLtI-MwDltiXg1OYcTzrAkFQV1Yw86HVSGMrsckk_il-gxQJJ-LMD-MxOV8gaMJdSp2gZ38Wj-owgCvRrSNw6M6jgMGFqu33b9OyNwSml8-n3L2-ZN11KLJjXKMokNjUmTqm8ldE8wD4xSn-pMS-shtbcVW5VfYiYirHtqBcaOif_jhGzmAQgJ7MaXbp6Cxoli-MRcBfeDSDOwqvYQ7X6TEqxfpaudzphZnvgsyHXXMByqTqSmmgEWd_GjSWn3OFpNwQmf2IbRY-dkj48w57YTF9Vdl2Yeu3SUhvBFAUF1piFOZutpWSVR2KQW5uALBpJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2230f2a78e.mp4?token=odgYKwBylkF0oa9sYFK_OLtI-MwDltiXg1OYcTzrAkFQV1Yw86HVSGMrsckk_il-gxQJJ-LMD-MxOV8gaMJdSp2gZ38Wj-owgCvRrSNw6M6jgMGFqu33b9OyNwSml8-n3L2-ZN11KLJjXKMokNjUmTqm8ldE8wD4xSn-pMS-shtbcVW5VfYiYirHtqBcaOif_jhGzmAQgJ7MaXbp6Cxoli-MRcBfeDSDOwqvYQ7X6TEqxfpaudzphZnvgsyHXXMByqTqSmmgEWd_GjSWn3OFpNwQmf2IbRY-dkj48w57YTF9Vdl2Yeu3SUhvBFAUF1piFOZutpWSVR2KQW5uALBpJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
اگر ما توان نظامی ایران را درهم کوبیده‌ایم، پس چطور آن‌ها همچنان موشک شلیک می‌کنند؟
🇺🇸
ترامپ:
آن‌ها همیشه می‌توانند موشک شلیک کنند. آن‌ها تعداد زیادی موشک داشتند و هنوز هم تعدادی دارند؛ هرچند بخش عمده‌ای از توانشان نابود شده است.
تولید موشک برایشان دشوار است. بخش اعظم تأسیسات تولیدی آن‌ها از کار افتاده، اما همچنان موشک در اختیار دارند. آن‌ها همیشه تعدادی موشک خواهند داشت، و ما [موشک‌هایشان را] سرنگون کردیم.
آن‌ها ۱۱ موشک به سمت ما شلیک کردند و ما تک‌تک آن‌ها را سرنگون کردیم. البته اجازه دادیم دو تا از آن‌ها رد شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71448" target="_blank">📅 08:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71447">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a731a8039.mp4?token=vodtk8-K8IW2CJdR-MzuhXRuuVBR1B_hOGNvzgFDmSfFy91KxuboMHq6JEeJo49od249vKGwX61xpsWFVsVIBHKw8iGhJIBEKYIIEqaS_mPED-hkJBSo8g_Ig32UkltYPNe0V6DUC01_Qg0ky2HBfqONXwGCJv2apteKBanEJYh7JClfmhlmtud4usnrhA5UUjD2LP1fr0w2ltwVeESEtl8HK6I4f9nLb8xDhq9t9K7gsbAoxqFBxtV0cyTNYub1T0pVb_1o2dNxOC7KVCKtGwv4BYuSdHfP5_NlZzWKYp_J53pj1jBT7laXRmQ99obkHPZ9Xeat50Jwpzj8D1IYmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a731a8039.mp4?token=vodtk8-K8IW2CJdR-MzuhXRuuVBR1B_hOGNvzgFDmSfFy91KxuboMHq6JEeJo49od249vKGwX61xpsWFVsVIBHKw8iGhJIBEKYIIEqaS_mPED-hkJBSo8g_Ig32UkltYPNe0V6DUC01_Qg0ky2HBfqONXwGCJv2apteKBanEJYh7JClfmhlmtud4usnrhA5UUjD2LP1fr0w2ltwVeESEtl8HK6I4f9nLb8xDhq9t9K7gsbAoxqFBxtV0cyTNYub1T0pVb_1o2dNxOC7KVCKtGwv4BYuSdHfP5_NlZzWKYp_J53pj1jBT7laXRmQ99obkHPZ9Xeat50Jwpzj8D1IYmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
ماجرا درست پس از انتخابات به پایان خواهد رسید.
نمی‌گویم چه زمانی، اما فکر می‌کنم درست بعد از انتخابات تمام می‌شود.
آن‌ها به‌سختی و با لنگ‌لنگان پیش می‌روند؛ در مخمصه‌ای عمیق گرفتار شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71447" target="_blank">📅 08:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71446">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dedfdd2dfa.mp4?token=bYQ5T5KeCdhTSITGLHL8tEK7ByxCBwX_6EbYis78a4pEtNkmHoDO6wcyFMqN1tQQ5LMoBl5frZcETZs8f-OFPgT77nBPpvWUiR4AbsZpbZd7AFhcXUMDI3F0ZMM4Q8m-WF5-IrzWCLZ3Mc-TidO820YEkTLTfhE5OfT0E2xKaicPRD-s20dG26rnfRTkNEG3ox_0Y3sk8MOzl6IZqXrpOZfGFOMB8UYMf63rGLoEG8F-i3aHc6XkbgqzYATo8HJwvOF5S9K-FH7016mpYU00Lw02cd8veDHMi2szM0Y29yjlIECzaC0WieGPxdebMaTanbrd4gkzhSayVJany62AEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dedfdd2dfa.mp4?token=bYQ5T5KeCdhTSITGLHL8tEK7ByxCBwX_6EbYis78a4pEtNkmHoDO6wcyFMqN1tQQ5LMoBl5frZcETZs8f-OFPgT77nBPpvWUiR4AbsZpbZd7AFhcXUMDI3F0ZMM4Q8m-WF5-IrzWCLZ3Mc-TidO820YEkTLTfhE5OfT0E2xKaicPRD-s20dG26rnfRTkNEG3ox_0Y3sk8MOzl6IZqXrpOZfGFOMB8UYMf63rGLoEG8F-i3aHc6XkbgqzYATo8HJwvOF5S9K-FH7016mpYU00Lw02cd8veDHMi2szM0Y29yjlIECzaC0WieGPxdebMaTanbrd4gkzhSayVJany62AEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
اگر ماجرای ایران پیش نیامده بود، با خیالی آسوده به سمت پیروزی در انتخابات میان‌دوره‌ای پیش می‌رفتید؛ ۲۲۵ [کرسی].» آیا حسرتی دارید؟»
🇺🇸
ترامپ:
«نه، من به واژه "حسرت" اعتقادی ندارم.
آدم همیشه ممکن است کمی به کار خودش شک کند؛ چند نفری هم این سؤال را از من پرسیده‌اند.
اگر قرار بود دوباره آن کار را انجام دهم، دقیقاً همان‌طور عمل می‌کردم. من توانمندی هسته‌ای آن‌ها را از بین بردم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71446" target="_blank">📅 08:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71445">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71445" target="_blank">📅 01:35 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
