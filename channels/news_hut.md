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
<img src="https://cdn4.telesco.pe/file/uu80JguCHYCfODhGgxz9v8L7JMB3Q5Ct-d7ds3i0FpM656p_AlqOQX1rvbhTc-Qcqb7RYVB1zGxvV6ELkT6wfN1jDz11BReN5Hl9jnijXARKApDs9HZD69jRcYKcM83KowVZo2oN8IXYmJnSE-ggL2pnH-xfoyzqAQhV8yNn9_sUEDzDOqaQEcxfBAdizcyqIgZcNgA6ruLEvcYBzI_Tucwjs_Fu5XrtvK8TnFk08QhFyiAtUX2Ffg5ZY3VnbClSV6vaRymdkBhvxDTorsniFQFCD4ysasFe0YpSD6rFP8hMRX4Z0ZfMSq3IrCVbMXGgtiUOK4Xqx8SJMQCVw7xXJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 123K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 14:41:49</div>
<hr>

<div class="tg-post" id="msg-70137">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arCzrcRV_6bS83KAZXHUaBHftwIPysJtQki4Jhex9Cp9SAKqrGZPczgjkraIoGezTkm55011v0kQieUkyJMRaP1b0urgdNZ9EBg8LCZRCF1FhiASkx56NpDnr48t0mtlxieJ4D_bIJvZXMUFXC9VILUGjsJ_r4GQ_K6pJOXn1lePFEpBpat3g9hg9nZmKfdJR8KK0Gpv-woeNAylKMBZU-C4AYqI_nM7HA2hx-0exWFpswxTEWr1ImM2mTUmFM99oorfBrzq7BmdaJ_J-cmR-e_zMuMuzAMlFOr_4lLWr7jEe21YnXTcELpPvSvwbXpLaUl6kYC4bSNoWnbdzIZ0IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سند ازدواج کریس رونالدو و جورجینا:
در صورت جدایی و طلاق ، جورجینا ماهانه "100 هزار یورو" تا آخر عمر دریافت می‌کنه و مالکیت خونشون تو مادرید، به ارزش تقریبی "6 میلیون یورو" هم به جورجینا واگذار میشه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/news_hut/70137" target="_blank">📅 14:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70133">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Obvc03cHEUNElZ623XzVDc_BKTOUmw_KdB9i-0n2iYAK471fQ5plWMrAuBFUFgqP8brHGzptLWMpOWeDlqA_bypDXsPNuYShZv5-g-f7RehSY7UZ40U4lDFufVKt4tqOAC2p_VXwzBQlf-HLQu0wb-yM2tkRWo2y-voOt8IdDQCjuVDy9H_PM7kNL-UX6j_BzjPOJtNvclnni4PJoRJTPdJS9lHbv8_AfVsQkArD8WMJPnVkALZUiRJKn6NW0_OdBPLDwMKJfGtJP6kMlJBPnmqXLxbAPp4wn0mQFssXdo_o9IGvUkHTtNG3vAwyauSRzIbJpXG0ZKOz1onmAyjcEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lleE8uyHAyoZS1iYVLGzcoWByDvWx7JbGFAE8eFB2PsRuWLOoQgIbRVb-HCGRgtp4Qc4lFR0BZhA2pFYJz141lZG5V6ZcYpisG19az0-faYY2hn5i65iO12T7gyfAgntNC0M8AvD2SH5aodyvBiwiJqwfKbPe0YeQ6S5NB2uKByZUA0-WZAGvRislNTprOKLkYBr_SasXk-4Bt72HIN0f819YjjdK3dO7NCIWa0gB4VKI4dxDR-m4m51J_NTzTEX4uKoAe_ZjVa_IFr-5RmjnACijxsM284WwTtTWUR4bSUQk9X1P7eHdoAClrfoo9vQevmsaCZRB_Z2RS49vC-lQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b276eb7f.mp4?token=vhmaImlYph7Zfa4O3L0WFAWjVXaKbTvXtpIZGFte0DGhmIg1Ig8GoB1rMPR5OwnbO8Q_LiyQyNBYiC49_w149tvko3t205jNuH4_WBcYPUVKs4jm-nFfxPI9VTAws1DvPDngZXFn6boB6t8fBg1lWUmkzjGnMOjIc4YcGMP-MSpilj-4cOVSKYCoaKw6Xp2M1VyTW5_3_b1q3vN-wRgKKQfH5SfHRpu_Y5-IQi0-40lSvA1Bfs88PeLkZCdOOPiawlq9rBHDZLaBsYzAaf5Ce3TqwfmEF9bbF2cLfIOqQP9C7LgCzNQPbBja5eXHHlP_a6uC8I4qbN8_A1pn8bYBvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b276eb7f.mp4?token=vhmaImlYph7Zfa4O3L0WFAWjVXaKbTvXtpIZGFte0DGhmIg1Ig8GoB1rMPR5OwnbO8Q_LiyQyNBYiC49_w149tvko3t205jNuH4_WBcYPUVKs4jm-nFfxPI9VTAws1DvPDngZXFn6boB6t8fBg1lWUmkzjGnMOjIc4YcGMP-MSpilj-4cOVSKYCoaKw6Xp2M1VyTW5_3_b1q3vN-wRgKKQfH5SfHRpu_Y5-IQi0-40lSvA1Bfs88PeLkZCdOOPiawlq9rBHDZLaBsYzAaf5Ce3TqwfmEF9bbF2cLfIOqQP9C7LgCzNQPbBja5eXHHlP_a6uC8I4qbN8_A1pn8bYBvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇨🇳
اختراع جدید چین؛پدافند پشه‌کش:
این دستگاهِ قابل حمل، با استفاده از هوش مصنوعی پشه‌های درحال پرواز رو تشخیص میده و با لیزر نابود می‌کنه.
قدرتش هم خیلی زیاده و می‌تونه تا 30 پشه رو تو هر ثانیه بکُشه و تا 6 متر هم پوشش میده.
@News_Hut</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/news_hut/70133" target="_blank">📅 13:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70132">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8ff4c5f43.mp4?token=gu-EIl9-43owfeMV5LrxnzJfpM1fs3FdNfO6Xr8UNY_GNn5-_sdkvOWVaBf7398_trvFC73QkJKbVTcoZSkdeEpKUi_c5QbVBEMzMl6uJGzFm12HR0VTaWHgOIPKOvTM7m5-ByeeGNU9wfoRpmqvcrKB6EovQYyPpOQI_t8lxA-kh8_Z68NpyahnxOTk_oII-6fcJUptB7NKigCNfcNK6dyN30x82R7dpAomYx0F9z-7UHFjAvbkEWHg7xeGae42gAxmXMSxR_BQ2k_s38Nbbb1-6TK45-4GFs84B0saHZ5JB6APiugkw4hS859cbU0a7vI62s7XOqaEDoQw2IZxdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8ff4c5f43.mp4?token=gu-EIl9-43owfeMV5LrxnzJfpM1fs3FdNfO6Xr8UNY_GNn5-_sdkvOWVaBf7398_trvFC73QkJKbVTcoZSkdeEpKUi_c5QbVBEMzMl6uJGzFm12HR0VTaWHgOIPKOvTM7m5-ByeeGNU9wfoRpmqvcrKB6EovQYyPpOQI_t8lxA-kh8_Z68NpyahnxOTk_oII-6fcJUptB7NKigCNfcNK6dyN30x82R7dpAomYx0F9z-7UHFjAvbkEWHg7xeGae42gAxmXMSxR_BQ2k_s38Nbbb1-6TK45-4GFs84B0saHZ5JB6APiugkw4hS859cbU0a7vI62s7XOqaEDoQw2IZxdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
صحنه‌هایی بر فراز منطقه مسکو در روسیه، پس از حملات پهپادی اوکراین به کولدینو و دوموددوو.
@News_Hut</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/news_hut/70132" target="_blank">📅 13:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70131">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇷
چهلم بعد از ۵ ماه؟
در روزهای ۲۷، ۲۸ و ۲۹مرداد  مراسم چهلم علی خامنه‌ای برگزار خواهد شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/70131" target="_blank">📅 12:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70130">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e871b80a60.mp4?token=CDyME8H6YP1JybpA0VdMcg6oEOGNQ45p8jSI3WVGc32RMGy-1zS-HZMtnwZj8yxII0MRUlZtfm-JSRuAJ-ePrW-SQqpOz2wioarvWwU0RjHdF8i3FsVLWNF2xUdEF8IxPyOMEgvCmCmp03YNyrs5lmolMB-HyRlmH5G2mWrKxYFA672wyZ1CioZn6LxhMHs6iGUq6IVgEWlwwWJ8tGM0l4GH5U9yKSvQG7oARWoPGhpgnh9jkoBbFebTG6ggN7uQkjjuyjeSqe6GUeazYObMpsmeaRyoJZh7Zw9HWca0cIPWqTvBG00R-9OTfqQz6Nz7w9sdVotbZcYNqh_gkhYyBA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e871b80a60.mp4?token=CDyME8H6YP1JybpA0VdMcg6oEOGNQ45p8jSI3WVGc32RMGy-1zS-HZMtnwZj8yxII0MRUlZtfm-JSRuAJ-ePrW-SQqpOz2wioarvWwU0RjHdF8i3FsVLWNF2xUdEF8IxPyOMEgvCmCmp03YNyrs5lmolMB-HyRlmH5G2mWrKxYFA672wyZ1CioZn6LxhMHs6iGUq6IVgEWlwwWJ8tGM0l4GH5U9yKSvQG7oARWoPGhpgnh9jkoBbFebTG6ggN7uQkjjuyjeSqe6GUeazYObMpsmeaRyoJZh7Zw9HWca0cIPWqTvBG00R-9OTfqQz6Nz7w9sdVotbZcYNqh_gkhYyBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به یه خانم گفتن معیارات برای همسر آینده‌ات و مشخصات خودتو بنویس؛
نتیجه نهایی عجیب و جالب بود!
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/70130" target="_blank">📅 12:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70129">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70129" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/news_hut/70129" target="_blank">📅 12:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70128">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyAZN2IkFlW19GLj4v1DcKJZLeDBG4rIPzswfdkhUHnY9Tn5GaqDsWtMG5Jn6F4KHUf-93j-y80qvscIbtAm6x_M8YEqhKSpJ3Hsoj1EhdJPJ6TnG7P747j14ZzMxuPjghSXKwjnWHGllWVSWoBHOf0MhMd5fheD5xN9yUKTlXmEgFpKH5rO-OFUZPMkmkX0FzQEaXCnv2jMyNuwapM9qXtTEKZLNukT4N2OJpEImQeYwnluV_HQQ20fnA1Qe6PufjtdLQffdBRQ3LEqXsi09l_RvEsWpP5EWilguSeSFhdHv44pBhRQyoQWQ1-vaRfv__zq504stHkoZgUfVOML2g.jpg" alt="photo" loading="lazy"/></div>
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
r25
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/news_hut/70128" target="_blank">📅 12:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70126">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a53c7e6e.mp4?token=swhDmo_zZV6DWv2bqo0gMD2PoGJfcWq1l0BfnyKTJNuRlBj60oq710NCRgKpImd3HQafRIOc9N--amkmWAYbMpvt-NqFnJ005rkqyL3uApDUqGzmJGzq0rTxhjpdMq7iNonN8soiXpeQjY_48CckSsv-HVsTsaOa5GPS4pKAv8-uXVVkqNyAyy697rKWS6BnYAmZh7Kzhjb6h2tGGbhL0pRumi6hWouKhigbGWcDimf-JLYhQomImc282vlO-QD7_TowdxJ7z8GiTVgENrt4npWpFC0tn9LPHobSl6YJzqQELCxhbFYLPF_l0UZZzwE2rEdhgwAVdsNHUKxB25661w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a53c7e6e.mp4?token=swhDmo_zZV6DWv2bqo0gMD2PoGJfcWq1l0BfnyKTJNuRlBj60oq710NCRgKpImd3HQafRIOc9N--amkmWAYbMpvt-NqFnJ005rkqyL3uApDUqGzmJGzq0rTxhjpdMq7iNonN8soiXpeQjY_48CckSsv-HVsTsaOa5GPS4pKAv8-uXVVkqNyAyy697rKWS6BnYAmZh7Kzhjb6h2tGGbhL0pRumi6hWouKhigbGWcDimf-JLYhQomImc282vlO-QD7_TowdxJ7z8GiTVgENrt4npWpFC0tn9LPHobSl6YJzqQELCxhbFYLPF_l0UZZzwE2rEdhgwAVdsNHUKxB25661w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
شاید براتون جالب باشه؛ کلیپ سمت چپی برای یه پسرایرانیه که بعد از سال‌ها تلاش، این حرکتو زد.
اما کلیپ سمت راستی یه نفر اومده با هوش مصنوعی همین پسره رو تبدیل به دختر کرده و گذاشته تو پیجش و حالا میلیونی بازدید گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/70126" target="_blank">📅 12:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70122">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SpOhV8KuVLPd8vSpvg5d73cCQx48ht6GGvgFuNB1jTTevVprUTSzGNcWXB-TrWB_ZD-nxdlSuf-WAZxCdjfupCc8DlDmb5FVHiRgt52QnHKIVQxqUOBrUHKjiy3KnpwEpEY-m1M63ua4TmJQsENSeyGtwRNJLr50i_kFMIU_1a9IxxOVB5h1p24W9OwJ_SzzCqh4667d_1azbeF6nt6_NkI5EQFSOO3YZXRC3vPlP4Im5pQGfNYqo6K4RwQaXk8_yfltn7oCVSBEuKO2Vv-wpve8nnliODaIlw26IRBgeXFXNwu-pX1egP4WKrReisntqderkHzfX2CttBmNrl_CSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GWOD9fNEzxlfwe6JCiVDRI9_WndQTMEneoGn-gaI4sr7d0ABxLWOMbqb3QxA-oppeMbNRmp_7p-S_MNtGgwJdRWl2K7CgxiXen2ifCdmts76f_h0uH4bafl2-WPQ-yq5ROACp1UU3CY7osRMcpOGl_tmhGcCvVwVxJayQuLb66c8grxwaLvDmeN5JT9h9auymF9WSEbg7a8Issw6NnfJ-aCAmZQZMqNLnu-CWmdNYKB4rJr4TmHChJO3Prb3C4SC8NlfiqI1NqCMrWz8CqnwQYmQgI2S_hHW_iIpPjXwWEt5xKnd3Jd4mHbD-Zh_WHRILhvp8thO_A8sw1QeCwvSoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CSY0zJhyrg4iK1GWTZ3hupGO0DhPz6zOe6F0gOxA-F3H5XXoJ013ID2-lP0KA6doWW4CGrnyMXS_sGy1uSSzBvCao99IlozyPVnkEHRxOV_f5j408r2a6fknqfnvEJa-VwzfVfAEnah5JACtNPrXsL3Cd8x0BitCki6UPrIu83udDtmau6KleUvItFdDHapGGon0Kt6JfMe-RmZr6Q43fcHnjFgykj8yY_qkSE1zTgM1Ha3kFqUEQ12eK5VdH-u8Xdm4VMmx9QBzo_YGxwQ5-vo2hWtNwWEuj2qgHsKBEIkBGXBbIrnVD77t_eNqfQL0okO6IMVifvgf8QID_Rl8NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gAvK3ZJZpUZh6HHnFvJ8UgUMFw9ENCE8iBhZHo_ew5tekgIqde7GqVQyd_LbCRzFw3-XfUrow2Jg1MQFQhR2_r1QMkWIWnJfb82shr3Cz6gjnDfGHj7VKHqc9OmnHtGHHTi5aE96PTyI_BTlXvYNwERdTLXwdHNjEx5kiaUH4R0i9y2zD45SjuQk828KnglugFGlh0ZJk9FsujZWlmz11rbQPggUs8gGqFGnWdc6hBmrXhyEWHpAio4lExFeeMcQf8O7MPjmb5h8Mt5iqU9Jsb5dZjjtI0il64Q4rIhbuhdBptSCnoRIE7MvJSaeZKkqind64guZ-KQbKHUKxVASeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
👀
رامین رضاییان رفته دایرکت یه خانم دو رگه ایرانی-امریکایی به اسم «جول فرشاد» که بازیگر سریال ایفوریا هم هست و ازش درخواست نود و ...کرده.
خود بانو "جول فرشاد" هم با استوریایی که گذاشتن این موضوع رو تایید کردن:
بله میخواهم تایید کنم که این شایعات درست هستن. به زودی جزئیات این ماجرا رو با شما در میون میذارم.
اون (رامین رضاییان) جلوی دوربین گریه میکرد و از مردم ایران طلب بخشش میکرد ولی تو دایرکت از من درخواست هایی با موضوع خصوصی و نامناسب داشت.
خطاب به رامین رضاییان: میتونی منو بلاک کنی ، عکس پروفایلت رو عوض کنی  و هر روز سعی کنی اکانت هام رو هک کنی اما نمیتونی حمایت ملتی رو بدست بیاری که مدام بهش دروغ میگی و بهش پشت میکنی.
‌
‌
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/70122" target="_blank">📅 11:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70121">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad5ddb268.mp4?token=iSUguVjKIP5CxzAlRzW6NKEffR2kcyPUYsIZlnKxdLG6RDyhAXsxf_CiTdG8GrmBGR6gnGVf2n8TDvVSORe6BbP9lov5SDmrQfbzWOyRQvDKdaW09pFn-fBpZQsSfwVkBJYZa6Q1IRfJhczRWLA7WqYP2Xy8DvilIVqCBcfehpMgd-F1Mq_pW39pjZBRQ43zEuPS1xnWUBTJF4Ez5okt81i-L-AHkIf2udqqe8Bs_EaY1s15fK_BrIUK1w6uwEnoOiNbIo4l_DnUnhBa2EipIHT1A3zYNmisSLLRKwUHrXQfVPlZR199rippiymQkygNPytI3FTgTLCJYgS5vCux2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad5ddb268.mp4?token=iSUguVjKIP5CxzAlRzW6NKEffR2kcyPUYsIZlnKxdLG6RDyhAXsxf_CiTdG8GrmBGR6gnGVf2n8TDvVSORe6BbP9lov5SDmrQfbzWOyRQvDKdaW09pFn-fBpZQsSfwVkBJYZa6Q1IRfJhczRWLA7WqYP2Xy8DvilIVqCBcfehpMgd-F1Mq_pW39pjZBRQ43zEuPS1xnWUBTJF4Ez5okt81i-L-AHkIf2udqqe8Bs_EaY1s15fK_BrIUK1w6uwEnoOiNbIo4l_DnUnhBa2EipIHT1A3zYNmisSLLRKwUHrXQfVPlZR199rippiymQkygNPytI3FTgTLCJYgS5vCux2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی چندین مرکز توزیع تجارت الکترونیک در مسکو را هدف قرار دادند و طبق گزارش‌ها، انبار "وایلدبریز" در منطقه کولدینو دچار آتش‌سوزی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/70121" target="_blank">📅 10:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70120">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d61d35336a.mp4?token=Yn3OWGayv-CUH7IyIGvNLkMnP6SN3AfPbGApIy1ZkaIsrzpltudC82Ogf8471b3WZ5AGoL5gItdq7e8hwsv-AjTWZioDLo3EH4sG2YOFq50rMrgU0XtAu9s-yriH8mWMGZPbu2n4zwhICqRwxhQ-Hv0SEdafXEZjv9AvrgWla3JnMp1hfcjullUuqYofM61iQf9xuL4ERE-Qkv6u1M_bCPS4BB-CMm4KGkRUFpeZ-ddL5MRktMwpB1-cm3KnBPXkVpo-x226DHmywvcK44EyitlwOFLCsFJSOb_BxHk4lQpaL8TB3_Vft1AQK4TV5MarWdz08IL3pisFIXiSk5DUYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d61d35336a.mp4?token=Yn3OWGayv-CUH7IyIGvNLkMnP6SN3AfPbGApIy1ZkaIsrzpltudC82Ogf8471b3WZ5AGoL5gItdq7e8hwsv-AjTWZioDLo3EH4sG2YOFq50rMrgU0XtAu9s-yriH8mWMGZPbu2n4zwhICqRwxhQ-Hv0SEdafXEZjv9AvrgWla3JnMp1hfcjullUuqYofM61iQf9xuL4ERE-Qkv6u1M_bCPS4BB-CMm4KGkRUFpeZ-ddL5MRktMwpB1-cm3KnBPXkVpo-x226DHmywvcK44EyitlwOFLCsFJSOb_BxHk4lQpaL8TB3_Vft1AQK4TV5MarWdz08IL3pisFIXiSk5DUYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از افرادی که وظیفه نگهداری از جنازه علی خامنه‌ای رو داشت:
زمانی که محل نگهداری پیکر رهبر هنوز مشخص نبود منو بردن تو محل نگهداریش جای خلوت تاریک و تنها بود، تو اون لحظه تمام غربت تاریخ شیعه رو دیدم بعد با خودم گفتم خدایا مگه میشه رهبر یه جایی باشه که حتی یک نگهبانم نداشته باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/70120" target="_blank">📅 10:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70119">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtMCxb4XIJQ-IXKYOkgYPeiaYyoIL3DVhDjsdRKhZ9VSc816V85m_u4pF1Yum3HivCkSFH_yWfYHfRfkwCi3OlRwMmUwTtfv2_Z3NmXXGEUs68_NbV9w8cA7iF6wGyNra6UXODts3H8YMmE-h7jslubmi8Q11mb5xkKv1j_KZDiEB6znPHGxbL0wjFmmvqG6HyE5EBVo5q55qnmTF4yJzq-AbaAdN5g9O9vc4b-D9mqtza5UWUuVFPW4OiYcF9E7me2MBOY6SfpXoanFjRLMy7r508T-ksoUfZXZov_Iu2KAybqeqPLm30sQhr-00whFzzcSIKChkAm-bBwD6cdftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پسره:
۵/۵/۵ با یه دختر وارد رابطه شده و نزدیک ۱۳ روز باهم تو رابطه بودن.
بعد از اینکه کات کردن، آقا پسر یه لیست تهیه کرده و خرجایی که کرده بوده رو فاکتور کرده و فرستاده برای دختره.‌‌
اونم کل دنگش رو داده، البته جا ۱۹۰۰، دو میلیون براش زده و گفته فقط گموشو...
لیوان یکبارمصرفم حساب کردی مشتی؟ باز خوبه پول اینترنت و شارژی که مصرف کردی رو تخفیف دادی
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/70119" target="_blank">📅 10:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70118">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6731c5b6.mp4?token=MiVifhNUOurG0df8_SF2-s-fD9Bad3EyWRfRXxI_gfQ2RF_jEQx0wV7vjW5r50eO9IJy-MjlZJlNwQcZUvgLDdcO5eRy8OW94l4tQmCHmT3b0Mi9qoxOdFUATG6fybilQ-NFvsVhH6jfBu47T0K8WyOxyxQvu8irnGnWb3q-4MhCXv59rzJVUavkeC94fNC7SxqiuxvR7566gKnGg8-Qmsnk3AUhkQXyxXCJEZ5MrtRQEc-PR2Nx5V8E5YF1w6v-8zkjdDkCSdQ--kpLCLR3KJaOvoEUO657ufNvdy6CdhxkP3oCvefmhPg6aEcSLu_v8Xw9tJNwDxCVRIpz39O-pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6731c5b6.mp4?token=MiVifhNUOurG0df8_SF2-s-fD9Bad3EyWRfRXxI_gfQ2RF_jEQx0wV7vjW5r50eO9IJy-MjlZJlNwQcZUvgLDdcO5eRy8OW94l4tQmCHmT3b0Mi9qoxOdFUATG6fybilQ-NFvsVhH6jfBu47T0K8WyOxyxQvu8irnGnWb3q-4MhCXv59rzJVUavkeC94fNC7SxqiuxvR7566gKnGg8-Qmsnk3AUhkQXyxXCJEZ5MrtRQEc-PR2Nx5V8E5YF1w6v-8zkjdDkCSdQ--kpLCLR3KJaOvoEUO657ufNvdy6CdhxkP3oCvefmhPg6aEcSLu_v8Xw9tJNwDxCVRIpz39O-pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
احمد آریایی
‌
نژاد نماینده مجلس:
مهسا امینی به درک واصل شد!!
اونوقت رئیس جمهور قبلی ما اومد گفت مگه میشه یه نفر همینطوری بیوفته بمیره ؟
بخدا یه ادم عادی هم میدونه ممکنه یکی یهو بمیره اما هشت ماه برای مملکت تبعات اغتشاش داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/70118" target="_blank">📅 09:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70117">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=MvWJd2EOHwJGJ7Jhb_GyGwOevXf6oI0x35-X3zTv09PY-E6TTJa-C_IZAcjYX2Ogh7UzULO8eZI41ccrucgPL-mJLoDyM3Gku8VT3vaNpE-FRHzwFpwxuS5km6RnQ06PmTXzzq0B161UuQQuiThCn0z-k2pudzIM18kTxx-G_e5g-bkebhDLsVi4OyDMYDi0CVzYb3q05SG5WwAxKp5ODk6DkS4WcM9M0nMKa3N77z8VxL_OjIN9QL3U-kDkW6ifgz-rxS2LN9rid-C4W1g2S1j2O2TAlUD4ptASUad8DdSlEgn-QhLne_Y96URIVfQ7mm5x9tSb-lJCcrZY2gcteIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=MvWJd2EOHwJGJ7Jhb_GyGwOevXf6oI0x35-X3zTv09PY-E6TTJa-C_IZAcjYX2Ogh7UzULO8eZI41ccrucgPL-mJLoDyM3Gku8VT3vaNpE-FRHzwFpwxuS5km6RnQ06PmTXzzq0B161UuQQuiThCn0z-k2pudzIM18kTxx-G_e5g-bkebhDLsVi4OyDMYDi0CVzYb3q05SG5WwAxKp5ODk6DkS4WcM9M0nMKa3N77z8VxL_OjIN9QL3U-kDkW6ifgz-rxS2LN9rid-C4W1g2S1j2O2TAlUD4ptASUad8DdSlEgn-QhLne_Y96URIVfQ7mm5x9tSb-lJCcrZY2gcteIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اسنپ لیستی منتشر کرده از حواس پرتی های مردم که وسایل خودشون داخل تاکسی ها جا گذاشتن :
261 هزار کارت بانکی
178 هزار کیف
137 هزار موبایل
یه کنسول PS5
لباس عروس
یه قابلمه قرمه سبزی
یه قفس طوطی
27 هزار ایرپاد
و پشیم ریزون ترینش : یه نوزاد شیرخوار
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/70117" target="_blank">📅 08:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70116">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/70116" target="_blank">📅 01:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70115">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=ZnPIYbDWamdeBpGifp8JdyLQt6Gf5rkDa9HAnG7w7uY5VOn-eZIDnD6BjetBUM06uOUmJgy5GhOSqS6DFrXQjNHCFTKpAKev-Co_zCxasj2lgCN3oOLAZiwInv2H_NpN7ckkVW3w7PQrDOuI0GioE0ERFQvB1ZhL4X4VlT7uZE1tTzONkNByLcCitaiXhNEXy9PZgfGLvhfVcvszcIFgb4n0WCwVghajFpUAbMyqwt_jFwYHd-V2OaW1Y_GdlQweYAVjgPOs2quXcABCJJGoKSYZAod3YWR3v595PG4TjzZcdv903mSDNEt-gsdxLKzu-IRgF_C1kZVOuLsRwkms4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=ZnPIYbDWamdeBpGifp8JdyLQt6Gf5rkDa9HAnG7w7uY5VOn-eZIDnD6BjetBUM06uOUmJgy5GhOSqS6DFrXQjNHCFTKpAKev-Co_zCxasj2lgCN3oOLAZiwInv2H_NpN7ckkVW3w7PQrDOuI0GioE0ERFQvB1ZhL4X4VlT7uZE1tTzONkNByLcCitaiXhNEXy9PZgfGLvhfVcvszcIFgb4n0WCwVghajFpUAbMyqwt_jFwYHd-V2OaW1Y_GdlQweYAVjgPOs2quXcABCJJGoKSYZAod3YWR3v595PG4TjzZcdv903mSDNEt-gsdxLKzu-IRgF_C1kZVOuLsRwkms4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
a24
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/70115" target="_blank">📅 01:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70114">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_nCdyHRjIOfN3JMR3dhkKjLVAYFv88yqBlrpWGgzKWDfw0LKyUUwHEAR8-ABRBmppXG609UFNVvyRVEgh8iH_nNM9MsPqvifAMw-eiJtO5fiNj33gvIRkfol3Q6NFuAQRzVC13XQyE3pnfRu4iCvuv1mdE8iPcZ_QibxKdkwwuRqzL6RsnOU7A-SlAZBYLpTfywc1i7boH4tnCGfH6qxCyVXN65L8YMm6cqpSvlvcXuN3HDmFwB-L8jANr2y23qYQlyIVZv5AH41PVOKEuP_r5gutW9EW-5FFva8Z0q_rRo0m6W4ONgjkQUehrVa1X1HfF30XlrvcIcDQWOSW_cEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
〰️
فرماندهی مرکزی ایالات متحده (سنتکام):
در تاریخ ۱۵ اوت سفر ۱۰ روزه خود به خاورمیانه را به پایان رساند؛ سفری که شامل بازدید از شش کشور و همچنین یک ناو هواپیمابر نیروی دریایی آمریکا در حال عملیات در دریای عرب بود.
دریاسالار برد کوپر با مقامات ارشد غیرنظامی و نظامی در بحرین، عراق، اسرائیل، اردن، عربستان سعودی و امارات متحده عربی دیدار کرد و با نیروهای نظامی مستقر آمریکایی وقت گذراند. بیش از ۵۰ هزار نیروی نظامی آمریکایی در سراسر خاورمیانه مشغول انجام مأموریت‌های مختلف هستند.
کوپر در جریان حضور خود در خشکی، از نیروهای دارای عملکرد ممتاز و کسانی که قرارداد خدمت خود را تمدید کرده بودند تقدیر کرد و بر مراسم انتقال فرماندهی «نیروی ضربت مشترک ترکیبی - عملیات عزم راسخ» (CJTF-OIR) نظارت داشت. در تاریخ ۱۱ اوت، طی مراسمی در مقر این نیرو در اردن، سرلشکر کوین لمبرت فرماندهی CJTF-OIR را به دریادار دوم لیام هولین واگذار کرد.
کوپر در زمان حضور در دریا، برای دومین بار در سال جاری با ملوانان و تفنگداران دریایی مستقر در ناو «یو‌اس‌اس آبراهام لینکلن» (CVN 72) دیدار کرد. او پیش‌تر در ماه فوریه به همراه استیو ویتکاف (فرستاده ویژه آمریکا برای مأموریت‌های صلح) و جرد کوشنر از این ناو هواپیمابر بازدید کرده بود.
در جریان آخرین سفر کوپر، او برای تمامی اعضای تیم ناو لینکلن سخنرانی کرد و از فداکاری و شجاعت فوق‌العاده آن‌ها تشکر نمود. او همچنین با نیروهای رده‌های پایین‌تر دیدار کرد و به افراد شایسته نشان و تقدیرنامه اعطا کرد.
کوپر گفت: «گروه ضربت ناو هواپیمابر لینکلن تیمی قدرتمند از آمریکایی‌های موفق است که با افتخاری عظیم و بجا، به دستاوردهای خود می‌بالند. تاریخ، این مأموریت را به عنوان یکی از فشرده‌ترین و تأثیرگذارترین عملیات‌های دوران مدرن ثبت خواهد کرد.»
ناو آبراهام لینکلن که پایگاه اصلی آن در سن‌دیگو قرار دارد، در ماه نوامبر برای انجام مأموریت اعزام شد و در ماه ژانویه به خاورمیانه رسید. این گروه ضربت با موفقیت هزاران پرواز رزمی را در حمایت از «عملیات خشم حماسی» (Epic Fury)، مأموریت‌های امنیت منطقه‌ای و محاصره دریایی جاری آمریکا علیه ایران انجام داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70114" target="_blank">📅 01:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70113">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2DzBzEVar112OLKCnW3QWT3sOADYN4vqtt_fmS4aCRVKC36HAd0NUaNkgTnsyd1Er4w9QJbUsXS1rF-pHTNASkue4XYpj1oMUo8AgiCOIDMoutRQXpjXiS3EP04EXxJlk2gfFJtnO7DZvEo3aQEBEkZlmgnTcBNh1xLXSzhwKbnEBfCJCT5sL42HEKYgmA9N9A1cacU0inLhkc_LmtYWocySAaWIs4YPnBxIm5eIwAlQKG4FhDR5_6FIWXPxlzWh8-rUzlLWWknypce04_Sj7v9-iD-fowvYci99IlHOorYgyxsmcicTizWUcTAwbWIYXXUiiY2aGhbmfvDx-ObtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست جدید ترامپ با تصویری از خودش با کلاهی که شعار «ترامپ ۲۰۲۸» به سر دارد:
«ما پیروز خواهیم شد».
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70113" target="_blank">📅 01:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70111">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1Y4I5BOURZEpMXTuUIGxDbttbnuVqTG6JInRi_S-0_mNicpPT7kBTI07X-7t5wt0XCJt2Id1hGZ0K1pcvL9ftgU8fuzWkYk6C7oBF0SkBJoP_7dIigX0TQown98EY-UudyYB1Cd9hxVpS6e7eV_p6SWpmLWXcAHtKyEal3g5athc7hMCqBLBSMjLl_qA_cfMC7QI1hT0iZ75RbvIRAEBVmHiHJLatTVpdrMWEKGavawJCWeV_TZ2isvUWhiQBZcoy-FopO8Jm6f6AxDALKIoLL7UgDMdwmjFNWH5coq-UT-K5mWrn-yhJL1XMfV5NY8C88p1Hyg6sMHvgibjwXXuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0a274391.mp4?token=p15j85H-GeUj59Bj07aJZz4MIUgboc6vQziwQYVOfX2zE0uWVg8qHPVlPPnNMERFHhzixW6x_NHVGiSUibgg3HcjRH83pjR1QDg6wlpJcnA3jyOH5R9XTxuqlcPzxDa7bxJvUg7XI-vLVQ4sxT-39SivjFJJll5Zv3-Lbyy4t1QEAMNXPUK54pNf7ob9GQHsVaxLYfGz-UcWuROQC8fSzSWbRc-y2rDByHdYEJ_AjYyf9n5IUKVe13OlV0ZOOSmk-gl-hauuqwzt9fs6ZHg3jtxgHy331mxviI77iYDz1h9Xd4E0iH7AQXZsH_iTjJMnuVsIxea_Lift21hd-lVtgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0a274391.mp4?token=p15j85H-GeUj59Bj07aJZz4MIUgboc6vQziwQYVOfX2zE0uWVg8qHPVlPPnNMERFHhzixW6x_NHVGiSUibgg3HcjRH83pjR1QDg6wlpJcnA3jyOH5R9XTxuqlcPzxDa7bxJvUg7XI-vLVQ4sxT-39SivjFJJll5Zv3-Lbyy4t1QEAMNXPUK54pNf7ob9GQHsVaxLYfGz-UcWuROQC8fSzSWbRc-y2rDByHdYEJ_AjYyf9n5IUKVe13OlV0ZOOSmk-gl-hauuqwzt9fs6ZHg3jtxgHy331mxviI77iYDz1h9Xd4E0iH7AQXZsH_iTjJMnuVsIxea_Lift21hd-lVtgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇱
حملات ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70111" target="_blank">📅 00:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70110">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
رئیس سازمان بهینه سازی:
🔴
طرح اول پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
در این روش قیمت بنزین تغییر نمی‌کند اما بنزین تا میزان تولید ۱۲۱ میلیون لیتری در پمپ‌بنزین‌ها توزیع شود و وقتی تمام شد، نازل‌ها خاموش می‌شود.
🔴
دومین طرح پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
در این روش ۱۲۱ میلیون لیتر تولیدی روز بین خودروهای موجود تقسیم شود و هرکس بیش از سهمیه بخواهد باید بنزینش را با نرخ آزاد بخرد؛ تقریبا مشابه روشی که قرار بود در کرمان اجرا شود.
🔴
سومین طرح پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
در این روش سهمیۀ بنزین به‌جای خودروها به مردم اختصاص داده می‌شود؛ چه خودرو داشته باشند چه نداشته باشند.
روزانه حدود ۳۰ میلیون لیتر به حمل‌ونقل عمومی و تاکسی‌های آنلاین و غیرآنلاین اختصاص داشته می‌شود تا قیمت آن‌ها تغییر نکند.
تقریبا ماهی ۳۰ لیتر به هر فرد می‌رسد و امکان انتقال و خرید و فروش آن وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70110" target="_blank">📅 00:24 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70109">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3808337972.mp4?token=DA2C5IgKhbYHfvpF8mehpV4DW2k2O8NE7v9Wup2-ZrRfHVR0rQSU0xWNqHBEHUd5DWSz_c7d07xoQdNahrX-fc7NdfOfxFVKjFj2wC8p5kdiKUtZIlIguyGDCeVArBHd9ipH3MdyBNpG1V_-mf3pt_HsQ7Dbo88w3rBdB4xUcfuzBoMRhSudEBw_hr44IVGirLulRkyYDiFHErEG1NsUUZs6K3uYigFfxbRIT25w-6cl0TvRiswn8cGkenTOvXoKEDPsZ4FTwIyfkNuPdWB1NUvJEUwMM0BsTQ3HfdymAyesN_amWSXMtWP_qLj0LUvVDVLR7TfaV4lsvTqtpukBBW-VNFWwwnmvbXORfBkmWJl3w4fokoX7AZLQOuRNsChHmSM18Pr4ECmahYHBTZaA3hIO-fKgt9QcjIcecbr6wVQ6HHiyIzy5_ovHWlRwWi4zGZT5n3uMNxmijoeRK7ygH7my2zf9vkWnRioPy5ZG9hp4eTOUmzrd0dWpFkrAdRSL32upW3y5UUjjqfcUP2UB1bxnLqQJ0ChjLogH5C9m6OpnGPGUT_4BN0M0ekF4Gx1ID7haeduRFlAr1dx_mX4A2RZiHZ6zw3RQ4opBkioEsBY9TzCMntQlRNDuY4127n-3B4eneR2412LcccQgSHOeP8I288zEOayuej_XCXWDbu4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3808337972.mp4?token=DA2C5IgKhbYHfvpF8mehpV4DW2k2O8NE7v9Wup2-ZrRfHVR0rQSU0xWNqHBEHUd5DWSz_c7d07xoQdNahrX-fc7NdfOfxFVKjFj2wC8p5kdiKUtZIlIguyGDCeVArBHd9ipH3MdyBNpG1V_-mf3pt_HsQ7Dbo88w3rBdB4xUcfuzBoMRhSudEBw_hr44IVGirLulRkyYDiFHErEG1NsUUZs6K3uYigFfxbRIT25w-6cl0TvRiswn8cGkenTOvXoKEDPsZ4FTwIyfkNuPdWB1NUvJEUwMM0BsTQ3HfdymAyesN_amWSXMtWP_qLj0LUvVDVLR7TfaV4lsvTqtpukBBW-VNFWwwnmvbXORfBkmWJl3w4fokoX7AZLQOuRNsChHmSM18Pr4ECmahYHBTZaA3hIO-fKgt9QcjIcecbr6wVQ6HHiyIzy5_ovHWlRwWi4zGZT5n3uMNxmijoeRK7ygH7my2zf9vkWnRioPy5ZG9hp4eTOUmzrd0dWpFkrAdRSL32upW3y5UUjjqfcUP2UB1bxnLqQJ0ChjLogH5C9m6OpnGPGUT_4BN0M0ekF4Gx1ID7haeduRFlAr1dx_mX4A2RZiHZ6zw3RQ4opBkioEsBY9TzCMntQlRNDuY4127n-3B4eneR2412LcccQgSHOeP8I288zEOayuej_XCXWDbu4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📚
وضعیت کنکوری های امسال
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70109" target="_blank">📅 23:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70108">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
❌
طبق گزارش های غیررسمی سپاه لحظاتی قبل از سیریک به طرف تنگه هرمز چند موشک/پهباد شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70108" target="_blank">📅 22:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70107">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0p1rapkIq3Td-lpwJ_1EMHJOs-BwTp_k2IMl98xv8YGhAoa9UEgRo7wVJp1yNvhtC3xAAqOkBdPhu0kNeUdGi7RKpZXLLmC5BsRljWiA2OtynLqNwI30qM07xGwVJ8bQ2Skwiw65v0xv7f9CKsQfLRsHX840zz0xOrpajyQwU01KHrhXMt9T1DivizQXhbxfN_pM2czLkK7kaI1aGGcZyFKvgOS-4mU6AmDlnkDaaWecpA-00hHY5i_PaG5Nqpl-4gUS1JIq4u4WqZO3ZlsNChNgr1wrK4QfrNpn__VzP2oXjx9yT0IKuq3RgzTNlmSliul0Pw9B0Z4o20YxSjt3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ در تروث:
با وجود آن چهره‌ی غیردوستانه در این عکس خاص، عکس‌های بسیاری هم وجود دارد که در آن‌ها لبخند بر لب داریم؛ من و کیم جونگ‌اون رابطه‌ی بسیار خوبی با هم داریم!
رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/70107" target="_blank">📅 22:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70106">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c505095a40.mp4?token=NmhyC_VWW50R_Nq4k9DRizEL0b-bI3hAgjlEAo-h4zHAO3Xqoi7B9OGjKKGTJMHyJ3Srzstd1e1J5SVFO2Y9UqsNZCKdr8_-WUcwqKi7nISVuk9ELiDj9sKBd9WEFi75v_SrXWjLHesJkfhJzp5W1HI0uxnTwHqaOKF5sX5Fmx163n31u5QdKIYCyN3plhW4pw0dWiDV6PpfUp7t2y8jfrcyEwP5uA3nphvVdNqFAoXMjqllz5mWfyuRQLCh6StFp4F5ISZLTfCU97IKKP_QLWKbd2V61V2VI8BDhAwSvxfUNKC71upzysT40ZLZ_QFKjhNS4ut-pAABM0fIpqcd6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c505095a40.mp4?token=NmhyC_VWW50R_Nq4k9DRizEL0b-bI3hAgjlEAo-h4zHAO3Xqoi7B9OGjKKGTJMHyJ3Srzstd1e1J5SVFO2Y9UqsNZCKdr8_-WUcwqKi7nISVuk9ELiDj9sKBd9WEFi75v_SrXWjLHesJkfhJzp5W1HI0uxnTwHqaOKF5sX5Fmx163n31u5QdKIYCyN3plhW4pw0dWiDV6PpfUp7t2y8jfrcyEwP5uA3nphvVdNqFAoXMjqllz5mWfyuRQLCh6StFp4F5ISZLTfCU97IKKP_QLWKbd2V61V2VI8BDhAwSvxfUNKC71upzysT40ZLZ_QFKjhNS4ut-pAABM0fIpqcd6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب یکی از هوادارای استقلال داشت شاد و خندون از تیمش تو مصاحبه تعریف می‌کرد؛
که یهو رفیقش تصمیم گرفت این شاهکار رو پیاده کنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/70106" target="_blank">📅 21:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70103">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q-ulP3FLxhg8sFG1pTG3X27t8Tecb35JR9mlbn9nYutVhL-4I2zf2lzFtJjHnn6ILiBjpFU9BSKAel5psZAdEYDf2SnkHw2LEfP8XF0mlNPvVaJibmUFXD6bWMbJPmDdZFulgpzrKawSoBnsRO1Pq5Y80AuCahFGoXCnzlZHXeLxSYqoxNRETxFicVC7F06dgKmFtPWqn3PoRxhsOKY5IBOabV8kOAV3zdo3_b-X1CB7Lu6jdpsL3fXZDMcmrXJM05PB0hCo6fblrpou4oyk_vrl1xpgNkourj_OVMDbaK3Ov8RkEMAqzegA1CtvUtdbYans1ClQ4utg7fzi03wm4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A58YCDQ6G4-ZENHiK1zCnpSFJ7CjdNgXAJJvfI9GlQLu1knRkddYOcW9fHBwQsUUzlZqOsAQIC7OL2ZpSGBvrT0A0i7Yh8PhVkKYZIo9hAgwwmkZQ8WH7VBy73VWwNd-ETTvM3pe-JinxKf4b8NOc5RwbAc1-imdWVrNkyz-ZjLdwfzheMsNJnUFGX0o2lUBH9uQwCdzLPu1g6-6Ahu1eoX5fx-otnyKatu968D17V57aN_iZr5VxWwLoqV108MUf8UMJD0pXaGVxQ45Di_isc9JZyg-CHHHu25T5rPdqNWWJDsFPPwbz6Qc9jrT3ZRaz4OKOxzl-Je8RH9IFuNJXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rKhzomJh27uwXxI3nXp2wA67IDtQE3cqfpqxMT6WMif8gtG3yMpd0RhKfePp1l4fTQFxLAFDLqQX6urjmVMdq3VTQ5YBw_IYt820wF0wJwq9lcWUeO6iak99Vjh8KekzIl4v8OQNyF3spVhPfFeP1quj7p0lKhEHGhhUAYcNmCRAa4O80olhaHDwbArgF923NZqjOkhJTzO7u0-Fm3gZVQtlr9oAE6cyXL1kpNG0-h6be5NjtHxJmcEMoIAKl7jtAHDH4XAy5LdJrARcP7kqNoBo5g8_kFyg-OIkNlhVH9t_B8QwFlW5h9itud_SgBoblxTWvaK3Ks2md8VaULbP-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست و استوری نوید محمدزاده و حمایت از فلسطین
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70103" target="_blank">📅 20:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70102">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
🇮🇷
🇺🇸
میدل‌ایست:
به گفته منابع، ایران معتقد است که دور جدیدی از درگیری با ایالات متحده اجتناب‌ناپذیر است و تصمیم گرفته است تا به‌جای دیپلماسی، تمام تلاش خود را بر آمادگی برای نبرد متمرکز کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70102" target="_blank">📅 20:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70101">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f39fe384fd.mp4?token=WkNWb8bEfjbm4Z0pG0hjXd4CgmJIHu99JK8kA6jND06jfpdgga9Mh6tGRnn7kAp3OoSe00SlAt6BB2MSUZ3A9y87lDjCob8zDReQcJ8h2ymnezbvbOfMBfyuvlZ5HpPf2dXiEfWfuAwrZilwo1PGDSZg8b70N1mQ-OcOK_oN0g0eSM6sFoSeG8hqCk9OPwdSz9tb0PjTevnRwnLMIEZ3vlX6XXS3ZkIenwD7JUJQxrn64nBE9iwbRsc8-GuMRuVlN3-n4TREQEDP5stlGkQvSECJeV1_AfuECWBqZeiKHthvXQo_ceRB3jFW5mA6t4V-kHceqdxytxxNoAsHGgLBcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f39fe384fd.mp4?token=WkNWb8bEfjbm4Z0pG0hjXd4CgmJIHu99JK8kA6jND06jfpdgga9Mh6tGRnn7kAp3OoSe00SlAt6BB2MSUZ3A9y87lDjCob8zDReQcJ8h2ymnezbvbOfMBfyuvlZ5HpPf2dXiEfWfuAwrZilwo1PGDSZg8b70N1mQ-OcOK_oN0g0eSM6sFoSeG8hqCk9OPwdSz9tb0PjTevnRwnLMIEZ3vlX6XXS3ZkIenwD7JUJQxrn64nBE9iwbRsc8-GuMRuVlN3-n4TREQEDP5stlGkQvSECJeV1_AfuECWBqZeiKHthvXQo_ceRB3jFW5mA6t4V-kHceqdxytxxNoAsHGgLBcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوتا گربه داشتن دعوا میکردن که یهو یکیشون تصمیم گرفت گرفت خارکصده بازی در بیاره و تا موتوری نزدیک شد رفت جلو موتور و باعث زمین خوردنش شد:
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70101" target="_blank">📅 20:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70100">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTwADcOa2IE2UxMMzYDcZym8j5waC2fXuSWqDaeCLYMpOmfdSfxVNOmhSy7ZUmeOTLobdq7WtAr9cha5x_ILUDKJezjb34mx_tEPGfgZSmJhco66nZCg7vU_PjW50sSEUs8rsL-Y675HGi18gaiX56kgbgfe3FU1M18U7sWs_2izh_U-85Vq1pZRBokioLuyCfpkPSE0tY88NgQM5MmvovAaLAPdHRmZCXH5K1z5sG-Zh3jjeH1P6GGfa7yf0Nd-n7XMpVKX2mYX9r7tcrOQZsHna6eejphcHoc1fuUxmHiwcBWQS6LBk3c3BP68b-kvnB0l2Va9NfXhUUHRSCHIGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
تصویری جدید از سردار عظمایی فرمانده نیرو دریایی سپاه که توی اتیکت اسمشو نوشتن عظمابی
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70100" target="_blank">📅 19:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70099">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4e3b71c01.mp4?token=C6KrXpG8PDoLxgSlT3q1dTXwKLOsjf-uFYhga6E7-SMTMI1c5f_GKHJJYuHreDApvC5CNaGoBXqRVDdIB-QbcEG5DsEkuJ70V9IPT0ER9qEJrr45JymDu1SziIrYrUV1y78yIlFsQr9ZjDRKhMxdRyXH61UwE5QYiRx3X93VJiI4c3Xr6dianQcEwhuvOceK-LFrtAJeTI5Ge5VRnNxb3i6NRu9tuQaCsAypezkvb8OtOSRy0TdBeTXnGvvUZY0rZY_pmppQQyHaYAMNGkWXIoE3I1a_zSRGZP-zJGSmErostdlQAyz8BhG87uMBtmveSy8-IC-KjbTkl0bXP-iMYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4e3b71c01.mp4?token=C6KrXpG8PDoLxgSlT3q1dTXwKLOsjf-uFYhga6E7-SMTMI1c5f_GKHJJYuHreDApvC5CNaGoBXqRVDdIB-QbcEG5DsEkuJ70V9IPT0ER9qEJrr45JymDu1SziIrYrUV1y78yIlFsQr9ZjDRKhMxdRyXH61UwE5QYiRx3X93VJiI4c3Xr6dianQcEwhuvOceK-LFrtAJeTI5Ge5VRnNxb3i6NRu9tuQaCsAypezkvb8OtOSRy0TdBeTXnGvvUZY0rZY_pmppQQyHaYAMNGkWXIoE3I1a_zSRGZP-zJGSmErostdlQAyz8BhG87uMBtmveSy8-IC-KjbTkl0bXP-iMYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کص‌مغز بازی واسه ویو یا پیک‌نیکی بودنِ خایه؟ مسئله این است
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70099" target="_blank">📅 18:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70098">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5505f54825.mp4?token=NyHuCg_-xbzAN5aFInu4AinazRXOz1DRJa0mznp_yHxxfB9VPQdTShDQQ6ecnUpQaRAaY4aGmhy6m_Oti0PC1EMhTs05_lcmd9yFFaaD5RH5jbiPhujyel7D2FkFdZKtd3s6eOzTgXKr-mLI36ybbUhStrZ8uFrEtvz5UeGL4DEW9DIv5DTTIYtj0XTvY5sTQJsi2iB_XFI6tL_yJNPR0uXvr7Jl4taXKCNIRTTdkr-s5R1BeOD_kQC4yDnsMVbn9iuLfhMZWdTsuUBTrUU4gDDmBPno-HOAI90mIX0Ll7Y1v0BDjAUTqIfj8BBmOvTuOwrZInKvT0BUR04bbpQvtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5505f54825.mp4?token=NyHuCg_-xbzAN5aFInu4AinazRXOz1DRJa0mznp_yHxxfB9VPQdTShDQQ6ecnUpQaRAaY4aGmhy6m_Oti0PC1EMhTs05_lcmd9yFFaaD5RH5jbiPhujyel7D2FkFdZKtd3s6eOzTgXKr-mLI36ybbUhStrZ8uFrEtvz5UeGL4DEW9DIv5DTTIYtj0XTvY5sTQJsi2iB_XFI6tL_yJNPR0uXvr7Jl4taXKCNIRTTdkr-s5R1BeOD_kQC4yDnsMVbn9iuLfhMZWdTsuUBTrUU4gDDmBPno-HOAI90mIX0Ll7Y1v0BDjAUTqIfj8BBmOvTuOwrZInKvT0BUR04bbpQvtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
بعد از این صحبتای پزشکیان موجی از انتقادها از طرف تندرو ها به سمتش در حال روانه شدن هست.
دلیلشم اینه، میگن چرا مسعود داره اطلاعات محرمانه کشور رو لو میده، باید باهاش برخورد قضایی بشه و...
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70098" target="_blank">📅 18:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70097">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">معتبرترین سایت بین المللی شرط بندی که به ایرانیا خدمات میده
✅
وقتش رسیده قید سایتا ایرانی بزنی و توی سایت بین المللی فعالیت کنی
⚠️
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70097" target="_blank">📅 18:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70096">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSC6yY-iAUKW2xmu9y-pzEk7VWntT7eD01U1nYYto5mqfca8j5hDr-FVI8rLVMzUH9mMjVXmDVsxhjmVFqsapVLNQsobCPby21i91hCz59U-L5FbkQgOldOPEnSYwXz1MDoeoiQkR476ulU3YK9jJJj1p7GMSBEeGk2opLo0MLwIhr8IICtWw3k7trdzzKJZCqBP6F6R0N5EncYSJiRWJBkUTHA2b21MLOGuEc4IeuqWDpQ5Lh-AgzuBZCzNZXmDloyAX7nQP65cc91d60Oywqy-MbkB5Cg9tyIMEPV6zyGiHPEnTRtDKDNXhLeaPFNfX8CNBeweqVGJUK17mkO0Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g24
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70096" target="_blank">📅 18:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70095">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2573e39307.mp4?token=PjHrW4d6ha-4mhVF1lb5Ba-l9Y9uVXdfcWGXMw6AH-eZN9LZSvh-idLhpqhBlWIsGnkAuCK1zhLYxkSayQ3lD9_73XBsYGJ1IswpCDqlRtOMWUhFcds29RFTgY4GCCs_R9Ix4-NA6t7lieKLjwuewvCsOW7t1XyQsfGo0NXNCfm9taYTMT-_V1vZo4RsntZ7TgGvRUKnL_EJoiDAjyv0zso7psTOY1MGDojjsNOWoRtvTGWkwy5NDfPYlbQDbyBhs6m7nIJ1ETlo9LRJfuS_cuo-r3fBtHerEW4dQqsWh-mnNWZEqYDVVxy4NwxSe8Ab0hVUCkEOhhJ914rUpYNmQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2573e39307.mp4?token=PjHrW4d6ha-4mhVF1lb5Ba-l9Y9uVXdfcWGXMw6AH-eZN9LZSvh-idLhpqhBlWIsGnkAuCK1zhLYxkSayQ3lD9_73XBsYGJ1IswpCDqlRtOMWUhFcds29RFTgY4GCCs_R9Ix4-NA6t7lieKLjwuewvCsOW7t1XyQsfGo0NXNCfm9taYTMT-_V1vZo4RsntZ7TgGvRUKnL_EJoiDAjyv0zso7psTOY1MGDojjsNOWoRtvTGWkwy5NDfPYlbQDbyBhs6m7nIJ1ETlo9LRJfuS_cuo-r3fBtHerEW4dQqsWh-mnNWZEqYDVVxy4NwxSe8Ab0hVUCkEOhhJ914rUpYNmQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند شب پیش چند تا جوون مست کرده بودن و توی ویلا همچین کاری رو کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70095" target="_blank">📅 18:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70094">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/532b4ed793.mp4?token=WHKaFs0VAaGK42xHTiszitWJRVedzZTIgNL0JwqFMhAumQp1fmTPN_cMkQH62eLOqgCm9ue2WOQWQVUBsS1F6Ld9sEzyXYytaHY3JtE_EG8o5K2WFD4wRDCHFMkhPgKMxzxd6Z5GPTPjoakpYeioRFhRdnqnQqaVjbP3wLHJChTZpulSuqRy9k01ywBiioqPUyObTDDRLeq9XS7aEjBeXcW1yuhhtyFpwu7CwlTeseDdVJOX9nMrEquNZqxBHGRFjw6YvfIo57kKoq-Di7LOXZN0F_9iWgw5A_Gl8wtXaR56-_ee6QkP2xqUvovg6JcOr2PCQrEMwoO4Tma0hfx5Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/532b4ed793.mp4?token=WHKaFs0VAaGK42xHTiszitWJRVedzZTIgNL0JwqFMhAumQp1fmTPN_cMkQH62eLOqgCm9ue2WOQWQVUBsS1F6Ld9sEzyXYytaHY3JtE_EG8o5K2WFD4wRDCHFMkhPgKMxzxd6Z5GPTPjoakpYeioRFhRdnqnQqaVjbP3wLHJChTZpulSuqRy9k01ywBiioqPUyObTDDRLeq9XS7aEjBeXcW1yuhhtyFpwu7CwlTeseDdVJOX9nMrEquNZqxBHGRFjw6YvfIo57kKoq-Di7LOXZN0F_9iWgw5A_Gl8wtXaR56-_ee6QkP2xqUvovg6JcOr2PCQrEMwoO4Tma0hfx5Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
صداوسیما: پنج هزار قبر برای آمریکایی‌ها در اطراف تهران آماده کردیم
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70094" target="_blank">📅 17:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70093">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b05CXH5jDCX60czC_4Ud8N0H1VOJLrjyRre_zahTWkRB-cgA4xtMzpyFPBWG3wxDvUujI7v5eIK46j3W0V9J5IarzATyJkZmUTI5P4Hp-8-wZN0knxHa1g-xhwkIn5aoO9DKdO4PV-HT87VuAqfQS0EhThZQ818BN_2PAfqCdMjIW4ikyqwV0i3-DH1TZ4hWpWJv2DNTjQpDu0kmxPRwSHhuqj_i2tUk1uO6Qm48Lyhcqug1ZE2WKlppFk27yN8kF23i6rvxY4fKDVFRo_esG85uMrCS1m-AtCBUkBHQKcwjFD9R435jKpVGlRCTFcSKu4AQS-HbBqDcHEUQ9T4Heg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
🇺🇸
کراسنشتاین خبرنگار آمریکایی:
دلیل استعفای لیویت این بود که فهمید ترامپ اونو به عنوان طعمه مرگ توی هواپیمای اصلی سوار نکرده و با خودش نبرده(ماجرای هواپیمای ترکیه)
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70093" target="_blank">📅 16:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70092">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/st6Ef1oN7QY6jGmaG3DZlpObwsJfawPUe5THMywqtoQAZoob1NkkGqwmW6K9RqjYaqnlsTeBx6Vf-jpbkgllk9UC7bcMsUDyvl3O99KBhn_RnyChHQKJuJ7yJdeOu5HKaYJkRWizjwXK55wUvGg3SD6qe91wMSIiYw7eS324KD4Ng7uint2DTEVrM8YpbOTzXHNUxFlDllAhgajcQUao-xfJvd8TW4-1jJzk8lOmqKL-uBYBil3BT_7RjWPl2aX3xSwsQJcKl1IY5ch7c24_PvslIldtfg_FSgADwkEV9vmTlD40i97BYuunjwlO4GGdkjPNqKpSJHeyR9Gr-xJW6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۰۰‌هزار تومن تخفیف خرید با اسنپ‌پی در شبکه‌های اجتماعی!
دیگه با اسنپ‌پی می‌تونی از بیشتر از ۴هزار فروشگاه و برند محبوب در شبکه‌های اجتماعی مثل اینستاگرام، بله و تلگرام، خرید کنی
و با درگاه پرداخت امن اسنپ‌پی هزینه‌ش رو در
۴قسط، بدون سود و کارمزد
پرداخت کنی.
با وارد کردن این کد تخفیف توی درگاه اسنپ‌پی، خریدت رو نهایی کن:
✨
کد تخفیف:PAY5SCMD
از طریق لینک زیر، لیست برندها رو ببین و با تخفیف و قسطی خرید کن:
https://l.snpy.ir/br9ej
https://l.snpy.ir/br9ej
https://l.snpy.ir/br9ej</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70092" target="_blank">📅 16:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70091">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6444186749.mp4?token=jcFrp7AXDe4nViAWHtvZEdShrJQ_sazK1QilCEcD_rjLE9Wp7KYiL3_HjllWGWVFJPtyM_qGO4ijE0UvQ53moj5veG0Y7vokVyW4agVZ2wbICBlSlxRwnbJHjYex8ogSK1CB9zdVDd2kiATn0YZbAbbhsgYTbRA3wsMSvn7ZYdkEXpY5l-LcsRLLy5-V2PYCeR1eVA5M67HmQoxl0V7lkwMpOQExb4SkOyBdtlxo_mDBNKcty_Y0pXtFEbC4NW2J3gtto8evr2B0Bwx7BwfqPAFjjUI8OjxoH4Js9l74-vzeva8tEC05UhuxCvboy8IP_D0gXnK-JbhWxAmC2lPYNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6444186749.mp4?token=jcFrp7AXDe4nViAWHtvZEdShrJQ_sazK1QilCEcD_rjLE9Wp7KYiL3_HjllWGWVFJPtyM_qGO4ijE0UvQ53moj5veG0Y7vokVyW4agVZ2wbICBlSlxRwnbJHjYex8ogSK1CB9zdVDd2kiATn0YZbAbbhsgYTbRA3wsMSvn7ZYdkEXpY5l-LcsRLLy5-V2PYCeR1eVA5M67HmQoxl0V7lkwMpOQExb4SkOyBdtlxo_mDBNKcty_Y0pXtFEbC4NW2J3gtto8evr2B0Bwx7BwfqPAFjjUI8OjxoH4Js9l74-vzeva8tEC05UhuxCvboy8IP_D0gXnK-JbhWxAmC2lPYNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
رسانه های اسرائیلی با انتشار این فیلم‌ نوشتن:
خیلیا فکر میکنن پرواز جنگنده‌های اسرائیلی بر فراز ایران خیلی سخت و طولانی و پرتنشه ولی کاملا برعکسه و زمان زیادیش شبیه پرواز هواپیماهای مسافربریه.
چون مراکز اطلاعاتی اسرائیل همواره مختصات پدافندها رو به اطلاع خلبانا میرسونن.
فیلمی از پرواز جنگنده های اسرائیل بر فراز آسمان تهران در زمان جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70091" target="_blank">📅 16:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70090">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnEewLlyZrK-AQS6ZGOs67ueOBBkgmaSkEV2LneA5Eqso9D3nw9OzDeSqgG1O7ksIBJHk3s8uTwVAl5Vrr_obf7Pq8o5FPKsw7yD6TcdkF7MPSzMkuWjeTQoJxasHVwA7mnseHlsG_6bFHnqk2z8ZnWwDVCLaH0me31VUwR7musJ5P9oLmib9nwqSG3r5GFWqKfi8VBmPKvRkUc4ZpYJ4BRS3QMnRTWo_r6cUlVGi1vWLMMkaIEdoAd126n21fSxDUC1r0YV7vlZpu6K8rGWahfNrYtt9tFxSeOwOMZCzsYr9KSQViETAlIG7TVCgwlT_CbvuLT1rFAvDy5EqG6veQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سردار باقرزاده: سه خلبان ایرانی توسط قطر به اسارت درآمده‌اند؛
فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح: ۳ خلبان ایرانی پس از سقوط جنگنده‌های سوخو-۲۴ در جریان حملات اسفندماه، زنده توسط نیروهای قطری اسیر شده‌اند.
«جواد صالحی»، «عبدالمجید دشتیان» و «عمران به‌روشیان» از ۶ ماه پیش در اسارت نیروهای قطری هستند و دولت قطر تاکنون اجازه دیدار، مصاحبه یا تماس این افراد با خانواده‌هایشان و مسئولان پیگیری‌کننده را نداده است.
طبق کنوانسیون سوم ژنو، صلیب سرخ جهانی باید هرچه سریع‌تر با خلبانان ایرانی در قطر دیدار و درباره وضعیت سلامت آنان تحقیق کند و شرایط آزادی آن‌ها را فراهم آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70090" target="_blank">📅 15:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70088">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a18fbcabf.mp4?token=o4KEg8X697NtZzb8oLyHd9H9UWL8YAfSE6To6lOEf1G9TLiNc9DlTHsjgsFOVgY9ndM9UhlJG3iyE97VsAUkqMEaJdGA8HgHcxax0HAyQz3p_YeADlXM-x-vNXXVidtVkFN_IQj9OiNOt1HQKEHTJeMso6BJmw3LRUyqdgo0Ai5w0ItqzumG9vdlimn4OlBPgm7o24yl6ZDR9AckqJsIY9gRTMdvXkPEYc1o1TWEfhwOtMDpSMzHG1eI7q1IFc2V58h_k50YWby0W1CzsIzBG2ath1bpG0-ZAF9CfdWhkuoXOlYIXq2NzB1lRH_vixhXyz5XOJoCupAlVQcVqsMVdiP_-ZiDeLpNTNwHyontbTY7oWT8Sl9t98agDWyJ3JIeduwVPClEg2aP4TuwBrWqlSeqrbIKqvA19G05rfMjZ1JW0n6CgYpUq4IvDyRGtMrUONDNKPelYZPRLg1CIaf35Ucw3zY4D-KN3FKFonZnhruE0RXWz6xP3Fll0HbPoCABi1OiCGM39N4BD-2A8kJVVPv-apsOLGuf1uw-40E2oDDZ31pctILbsmw-wEpNn4YjdGFMqrVYmtjHiG-v0K8IYXGo6zyCsegbL7FJzTQwbGGRETq6Ry-bW-DXRSD6DaegGShfTv4ubK2eR7MCbYjg4rNIL_i3x3bzHxD75MQGvhM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a18fbcabf.mp4?token=o4KEg8X697NtZzb8oLyHd9H9UWL8YAfSE6To6lOEf1G9TLiNc9DlTHsjgsFOVgY9ndM9UhlJG3iyE97VsAUkqMEaJdGA8HgHcxax0HAyQz3p_YeADlXM-x-vNXXVidtVkFN_IQj9OiNOt1HQKEHTJeMso6BJmw3LRUyqdgo0Ai5w0ItqzumG9vdlimn4OlBPgm7o24yl6ZDR9AckqJsIY9gRTMdvXkPEYc1o1TWEfhwOtMDpSMzHG1eI7q1IFc2V58h_k50YWby0W1CzsIzBG2ath1bpG0-ZAF9CfdWhkuoXOlYIXq2NzB1lRH_vixhXyz5XOJoCupAlVQcVqsMVdiP_-ZiDeLpNTNwHyontbTY7oWT8Sl9t98agDWyJ3JIeduwVPClEg2aP4TuwBrWqlSeqrbIKqvA19G05rfMjZ1JW0n6CgYpUq4IvDyRGtMrUONDNKPelYZPRLg1CIaf35Ucw3zY4D-KN3FKFonZnhruE0RXWz6xP3Fll0HbPoCABi1OiCGM39N4BD-2A8kJVVPv-apsOLGuf1uw-40E2oDDZ31pctILbsmw-wEpNn4YjdGFMqrVYmtjHiG-v0K8IYXGo6zyCsegbL7FJzTQwbGGRETq6Ry-bW-DXRSD6DaegGShfTv4ubK2eR7MCbYjg4rNIL_i3x3bzHxD75MQGvhM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اجرای یه پسربچه ۱۲ ساله ایرانی از آهنگ ترکی «NAPIYOSUN MESELA» حسابی وایرال شد!
اجرای این پسربچه تو رسانه‌های خارجی، مخصوصاً ترکیه، کلی سر و صدا کرده و خیلی‌ها معتقدن حتی از نسخه اصلی آهنگ هم بهتر خونده
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70088" target="_blank">📅 15:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70084">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhrQ8GpBU-gAoizJhQJfowj2_fo5f8JMnBcXhOkLu8IrEVym3xOA9C1FnRaie_YRvmTmByd3ittAJEhnZ0FIa0CHTlIGcZZi39h2geGPKGmhCbUK0PCDLiMu4FWl3GK7bWMNnqFv3l4f-naSo_i6-ElP1IITU1pB9epIQOaqLt4vPMilFzWww1KV3QMhrIOo2PCpXag27u1KaUMrdp1MYuUNvhfja39bQrtsJCPD5MsYxx_iEsnlYl6PW3DkbgS6LAc9Gb2yYnQYC7r2R0vFjAs3crx7n9qbYXUN8vLwwJKAYLZfEVp5UEfPt8kIhXlZN5B2oUf8lxG4LFpIbjnT-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/596d386743.mp4?token=EMSuEszDaF3tk06YdTzZkAhB9qFtrKzsYimTB3wRJLT7HvlSQMfZKe1Q2ByyDQm0mjn8OO3W1SCpuynI12Vz7uzr1nvciwvfSyPl-SoQFvKd-I3vwEyj-zemUEQiqpHVUiCrE_Fw5JPYhDmx158P1275Chd3KyOj7j_6O-_w5Moz2-xXbCPygN7M8XqdzGoqn9XQ99QcQv3E-AOzAdIgN6F1FWlod0y4p3a6Xfk4yqPtvpaAEg63y2Qr1bH9FKzzTzGY8OO7CpW_9jQsuZuE0ddx0RM3CUfF4ewplqLF5b0Octl6Csz37_bwvlMeMNW60vTAN1UWTkGaGY5ryPNMWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/596d386743.mp4?token=EMSuEszDaF3tk06YdTzZkAhB9qFtrKzsYimTB3wRJLT7HvlSQMfZKe1Q2ByyDQm0mjn8OO3W1SCpuynI12Vz7uzr1nvciwvfSyPl-SoQFvKd-I3vwEyj-zemUEQiqpHVUiCrE_Fw5JPYhDmx158P1275Chd3KyOj7j_6O-_w5Moz2-xXbCPygN7M8XqdzGoqn9XQ99QcQv3E-AOzAdIgN6F1FWlod0y4p3a6Xfk4yqPtvpaAEg63y2Qr1bH9FKzzTzGY8OO7CpW_9jQsuZuE0ddx0RM3CUfF4ewplqLF5b0Octl6Csz37_bwvlMeMNW60vTAN1UWTkGaGY5ryPNMWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
حملات سنگین ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70084" target="_blank">📅 14:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70083">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fbd8e1f85.mp4?token=LtCJjwJ66h_sZr80q8WdHU8wIbNSZzZf3PdTXX-azHlHDYTZ_cn8QoA3VBZhQZZllTVMpi3TVIYeu3yk9VhGv24Ko6F3gShcBChNr02xrPWpIP3LwEyGMSzqYu6cyMpK3iZ8_ap5glokLdKzWRXTFIGSRaAtSDAbWrQRqojVmmd1bneFLVmSlclQ1h2n2B2NN0tVg0LV9kTtdKlgb1rCetxV6rS3g4Epp9QvdYXKPOQF7yPYYUQ6Olxeu_ZjP5A-ZhJ19QBjif5AmdE2UGYURdmeQIUSDDJZ-xI5cdpTsscc1ClXk4a9WGPgG0h4x2gvvB8Zw0H8xCBGsQuySWMZrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fbd8e1f85.mp4?token=LtCJjwJ66h_sZr80q8WdHU8wIbNSZzZf3PdTXX-azHlHDYTZ_cn8QoA3VBZhQZZllTVMpi3TVIYeu3yk9VhGv24Ko6F3gShcBChNr02xrPWpIP3LwEyGMSzqYu6cyMpK3iZ8_ap5glokLdKzWRXTFIGSRaAtSDAbWrQRqojVmmd1bneFLVmSlclQ1h2n2B2NN0tVg0LV9kTtdKlgb1rCetxV6rS3g4Epp9QvdYXKPOQF7yPYYUQ6Olxeu_ZjP5A-ZhJ19QBjif5AmdE2UGYURdmeQIUSDDJZ-xI5cdpTsscc1ClXk4a9WGPgG0h4x2gvvB8Zw0H8xCBGsQuySWMZrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مم‌باقر قالیباف:
همون روز که به ضاحیه بیروت حمله شد همه چی لغو شد حتی مذاکرات
گفتم امشب اینطوری اینطوری اینطوری رژیم صهیونیستی رو خواهیم زد
اگه اونا جواب حمله مون رو بدن کل منطقه رو آتیش میکشیم
ترامپ اومد سریعا توییت زد محاصره لغو شد چرا چون ترسیده بود ولی دیدم زیرش نوشته تنگه هرمز باید باز بشه
به میانجی ها گفتم چنین چیزی نداریم‌اگه ترامپ این توییت رو پس نگیره دستور شلیک موشک ها رو میدم
درست بعد ۵۸ دقیقه ترامپ توییت رو ویرایش زد گفت تنگه طبق تفاهم نامه باز میشه نه بی قید و شرط
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70083" target="_blank">📅 13:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70081">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/98817f7767.mp4?token=jdxwih8QOc0osyJOuzzFTTf4Q_w4LIoaJxc-Stw0yCeo8iSqZ450KXQkAGx2BaU9ne2eWmG61fZLYIvMYVJJDb7jUG3WRW-RPRq3QHUrfXbrni4s9rlyKsm2UgwbCBdAdFM-opULE3mOznSiLFXFLy1br9C1eDOejxbgWvJB2mwTEv7-z4v-uPcWMvs6RR9_DKLI4HngOkMVj35QIfF9qEV2gRUsnN-AVQ6czMQ3dQ3Gp-yDiTL6Twp5UwM8kV58ZLAOwBcwuDV38NORIU_gDjpeT7WoK9izHc-OUZS-EGSOXCdMXMSYbDXvg9h22zAjGfk51Mb9A3y6yM2if7bdyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/98817f7767.mp4?token=jdxwih8QOc0osyJOuzzFTTf4Q_w4LIoaJxc-Stw0yCeo8iSqZ450KXQkAGx2BaU9ne2eWmG61fZLYIvMYVJJDb7jUG3WRW-RPRq3QHUrfXbrni4s9rlyKsm2UgwbCBdAdFM-opULE3mOznSiLFXFLy1br9C1eDOejxbgWvJB2mwTEv7-z4v-uPcWMvs6RR9_DKLI4HngOkMVj35QIfF9qEV2gRUsnN-AVQ6czMQ3dQ3Gp-yDiTL6Twp5UwM8kV58ZLAOwBcwuDV38NORIU_gDjpeT7WoK9izHc-OUZS-EGSOXCdMXMSYbDXvg9h22zAjGfk51Mb9A3y6yM2if7bdyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عزرائیل این روزا تبدیل به کراش دخترا شده!
یه انیمه ساختن، عزرائیل میاد جون یه دختر کوچولو رو بگیره، اما تصمیم میگیره ببره پیش خودش و بزرگش کنه.
همه جوره ازش مراقبت میکنه، مثل یه ملکه بزرگش میکنه و میفرسته مدرسه و...
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70081" target="_blank">📅 13:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70080">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e1ed49791.mp4?token=jl_Byxz2hmOWVlALSo6EEe8WYyYfxBdWD3OcCy5htbgphD9pxhxk7eOxjKQGBq0hKwuI7bG7IGC6S_S_ml09tntCGnfRyXWPf4e1lmyOdppOiPTZK2VanyPG2D-Fs8LqgU8ewYCWycYVPI3KXR4rYT9hCX7dEY3AtYBYj_CIljaGMSNmLuGIGQD1hedFrlHStBn6goa_6JPdpbT2QbCXik1G-OJ6dQLxNlD9TzN7wiSTXnZShvUt503nyDPDMTG3JhhSJYLvEtGaCIAPextPr1qwWWfOv66rWSb2oKvpS5v6RSnDMRfKbkUtCx9-PgSZo4fp0O5nWUJAUzsixIXxLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e1ed49791.mp4?token=jl_Byxz2hmOWVlALSo6EEe8WYyYfxBdWD3OcCy5htbgphD9pxhxk7eOxjKQGBq0hKwuI7bG7IGC6S_S_ml09tntCGnfRyXWPf4e1lmyOdppOiPTZK2VanyPG2D-Fs8LqgU8ewYCWycYVPI3KXR4rYT9hCX7dEY3AtYBYj_CIljaGMSNmLuGIGQD1hedFrlHStBn6goa_6JPdpbT2QbCXik1G-OJ6dQLxNlD9TzN7wiSTXnZShvUt503nyDPDMTG3JhhSJYLvEtGaCIAPextPr1qwWWfOv66rWSb2oKvpS5v6RSnDMRfKbkUtCx9-PgSZo4fp0O5nWUJAUzsixIXxLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف:
با همه وجودم می‌گویم که برای من هیچ فرقی بین امام شهید و رهبر معظم انقلاب نیست؛ حکم، حکم ولایت و رهبری است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70080" target="_blank">📅 12:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70077">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nqcS4t2-jJqMpYKMv-QR2AgCBGgzogoQuoTojmK3xiyPbbjNsvOdQ-4tn-I7T4KrX-udn8X56SuFdBSVHhuSEDHGkzjjQ_wSNBrfuhucGMej_tLueTq2PgYgX6S8ZypSzDnsU6SJ4UHLwd5SwNkKHbJ9D1_hWb-RPWs_vMcCk06pS4As3mkx9CwFexWBVGUcBwDDQEVzCGb7NGU6cRE92FykybMUshTG08ng4_v0MQ6emDpU9rtCtLmYHE4B25DtZwwFv2URnV-qIcysApt-oNW_J6-JjQ8X6ijIRnY3EjhHr3dEkGC0U10v-ov3x8Hi4BIyBhmh_wngeYH0fIDQzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tzzURinBG5FR2ibmKz26dUCgUaUT1Q_XL358sYLOfR4rzBRDrQ9E3EAMeSgst1_I9vIMjGyjdZM4guLjDvmz69GdduguAqu46tmDbzzbBwA5DFX7j62YNZ4aFYOuXZY0MSZuR7tMMMzdzYdp8KOhff6eA0r1iGjRtVSPqY68bJ8j5wBVtk3yRuSakfwbf_V7ZYZE6rcWGRcljytlab7zmazKzMPjUYmmfvwNADmIIEK_RkpJgyOn7m8HH_tPj3L9vcTkrdwSlr6o4WtxbnT1hiH9rexU9NqF1tq7io1LSxKF9Y9WxhzsVlBGHZ5hsHtWNhwMtA2O0Vpau2K5b5FMlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tl69qgBFnEt2v9MNL9wOuCmnycftowg3rfWA5s9hFynvyxvPjeeTkyPUf41n92pUG5ZjTTZWb6HwSRvrTPPvTj_OR4WmEtbkRQ9Irm5cTqHekn0rEjjFaX4ujFPRYh7dxorFHoaebMwRGEpnjNxnyyCckoaraaFBz2yPAlkXgeitNfDRPKkx6uNi_6nYD0-tECf5XS-lcmz2Qtm4Fmj1N7c5nsLrxxzsLCzbRqwTtOjFx3vGQNOVZfGkyM_azhTRNfLuNzTPtIFkx29uP0lz6k9F7S2Wwu3RNkzqD7Si7cpgePqlCODo417SmBq2wiHoO-fugs9P0RG2KyZOHeKkYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💢
〰️
❌
ناو هواپیمابر USS George Washington (CVN-73)
یو‌اس‌اس جورج واشنگتن یکی از ناوهای هواپیمابر هسته‌ای کلاس Nimitz نیروی دریایی آمریکا است و ششمین ناو این کلاس محسوب می‌شود. این ناو به نام اولین رئیس‌جمهور آمریکا، جورج واشنگتن، نام‌گذاری شده است.
🔴
مشخصات اصلی؛
کلاس: نیمیتز (Nimitz-class)
شماره بدنه: CVN-73
ورود به خدمت: ۴ ژوئیه ۱۹۹۲ �
طول: حدود ۳۳۳ متر
وزن جابه‌جایی: حدود ۱۰۰ هزار تن
پیشرانه: ۲ رآکتور هسته‌ای
سرعت: بیش از ۳۰ گره دریایی (حدود ۵۵ کیلومتر بر ساعت)
خدمه: حدود ۵۰۰۰ تا ۶۰۰۰ نفر
توان حمل هواگرد: معمولاً حدود ۷۰ تا ۹۰ هواپیما و بالگرد (بسته به مأموریت)
این ناو در عمل یک پایگاه هوایی متحرک روی دریا است؛ یعنی می‌تواند هزاران کیلومتر دور از خاک آمریکا، عملیات هوایی انجام دهد.
🔴
جنگنده‌ها و هواگردهای روی ناو
هواگردهای جورج واشنگتن توسط یک بال هوایی ناو (Carrier Air Wing) اداره می‌شوند. در سال‌های مختلف ترکیب این بال تغییر کرده است؛
جنگنده‌های ضربتی
1) F/A-18E/F Super Hornet
جنگنده اصلی تهاجمی ناو
توانایی حمل موشک‌های هوا‌به‌هوا و هوا‌به‌سطح
سرعت بالا و مناسب نبرد دریایی
اسکادران‌های معروفی که با جورج واشنگتن پرواز کرده‌اند:
VFA-102 "Diamondbacks"
VFA-27 "Royal Maces"
VFA-195 "Dambusters"
VFA-115 "Eagles"
2) F-35C Lightning II
در سال‌های اخیر، بال هوایی مرتبط با جورج واشنگتن به سمت استفاده از جنگنده نسل پنجم F-35C حرکت کرده است.
نیروی دریایی
ویژگی‌ها:
رادارگریزی
سنسورهای پیشرفته
توان حمله دقیق
3) EA-18G Growler
هواپیمای جنگ الکترونیک:
ایجاد اختلال در رادار دشمن
پشتیبانی از حملات هوایی
اسکادران:
VAQ-141 "Shadowhawks"
4) E-2D Hawkeye
هواپیمای هشدار زودهنگام:
دارای رادار بزرگ روی بدنه
کشف هواپیماها و موشک‌های دشمن از فاصله زیاد
اسکادران:
VAW-115 "Liberty Bells" (در دوره‌های مرتبط با CVW-5)
5) بالگردها
برای عملیات‌هایی مثل:
ضدزیردریایی
نجات خلبان
حمل تجهیزات
مدل‌ها:
MH-60R Seahawk
MH-60S Seahawk
اسکادران‌ها:
HSM-77
HSC-12
اسکادران‌های نمونه بال هوایی CVW-5 روی جورج واشنگتن
(ترکیب ممکن است با توجه به دوره زمانی تغییر کند)
VFA-102 — F/A-18F Super Hornet
VFA-115 — F/A-18E Super Hornet
VFA-27 — F/A-18E/F
VFA-195 — F/A-18E/F
VAQ-141 — EA-18G Growler
VAW-115 — E-2D Hawkeye
HSM-77 — MH-60R Seahawk
HSC-12 — MH-60S Seahawk
🔴
دو رآکتور هسته‌ای؛ بدون نیاز به سوخت‌گیری معمولی برای سال‌های طولانی
.
⚠️
این ناو به احتمال قوی جایگزین ناو (CVN-72)USS Abraham Lincolnخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70077" target="_blank">📅 12:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70076">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdQbDIMk10SjLRQslmgWSj8P63HN92KsHMTu3elrjre-wDKokJG6t33Csu66d9ImPui6hY2lAdpx5QUhf1uHbJBw_U3llR6rNIA2mekc9VXFXt4FdwcIC1k4HVd3KVi4yXwUpQIQMD5cN7vq1WR33tP9iMTHii8uwfANppdGKj_WZoIYuZx56vvHyyJuH8I5pnvi62-MQ44_EMSRLz5OSUzzPEGl3-IsormAJm9VGGPOHU8EmBTZNQ1PmCnNX4OrMXeBnaJhDKG7LgDBWmnV_rR0vKiozWYl6R9SHCY6Oyf2ywz19eujVSemjO-Vcsf9FPjxSoJ-OPe7khYuDzu7-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا UKMTO:
گزارش تأیید شده‌ای مبنی بر برخورد یک پرتابه ناشناخته به بدنه یک کشتی فله‌بر دریافت کرده است. خدمه در سلامت گزارش شده‌اند، هیچ ارزیابی خسارتی گزارش نشده است و در حال حاضر تأثیر زیست‌محیطی آن مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70076" target="_blank">📅 11:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70075">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnDBGR7A21eIwwKSXDfHX2Wl2tvJDjmcGx36x4AEDJza_W8Hu1uRDHo9gBKfPqHaSdvvCp2kctfb2HtsbEQf0L2qX3XNGyoAppuNn9qLh2PAWT-6vjc0UMzF96h_h7n0Eaf3cuNe0MMfd0q5RR6t5YvFDEYil_J_MVNpgQiQNte2yrZeTSbgrEFVohPsXR0NHQyKyRGt3GCmueZOPI8hNjBbH4s5ULmNZCTPHNxwcvMOxkJkY8vaFrCE5HF6-m-ROBh8jcYFj6xd6CwclHCtgUhvMgv3DDcpDR2-yI2KwFC3ATjmznT16_wdXXs0RlnsHRn5m6FnJNj0zBToLTvQdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
اکسیوس:دونالد ترامپ، رئیس‌جمهور آمریکا، در آستانه انتخابات ۲۷ اکتبر اسرائیل، بارها از اعلام حمایت صریح از بنیامین نتانیاهو، نخست‌وزیر اسرائیل، خودداری کرده است؛ این در حالی است که ائتلاف نتانیاهو در نظرسنجی‌ها از جناح مخالف عقب‌تر است و تنش‌ها میان این دو رهبر رو به افزایش است.
پیش‌بینی می‌شود ائتلاف نتانیاهو حدود ۴۹ تا ۵۳ کرسی به دست آورد که بسیار کمتر از ۶۱ کرسیِ مورد نیاز برای کسب اکثریت است، حال آنکه مجموع کرسی‌های احزاب مخالف بین ۶۷ تا ۷۰ کرسی برآورد می‌شود. همچنین در اکثر نظرسنجی‌ها، گادی آیزنکوت، رئیس پیشین ستاد کل ارتش اسرائیل، از نظر میزان محبوبیت از نتانیاهو پیشی گرفته است.
اختلاف‌نظر میان ترامپ و نتانیاهو بر سر مسائلی همچون ایران، غزه و لبنان افزایش یافته است. ترامپ از رهبر اسرائیل دل‌چرکین شده و در محافل خصوصی او را «بزرگ‌ترین دشمن خودش» توصیف کرده است.
آخرین مورد اختلاف آن‌ها مربوط به مخالفت علنی نتانیاهو با طرح ترامپ برای غزه و خلع سلاح حماس بود؛ هرچند نتانیاهو متعاقباً پذیرفت که به این طرح فرصتی بدهد و از شدت حملات اسرائیل بکاهد.
در همین حال، رقبای نتانیاهو از جمله آیزنکوت، نفتالی بنت و یائیر لاپید، از طریق کانال‌های غیررسمی پیام‌هایی به اطرافیان ترامپ ارسال کرده و از او خواسته‌اند که در انتخابات بی‌طرف بماند. ترامپ در هفته‌های اخیر چهار بار با این پرسش مواجه شده که آیا از نتانیاهو حمایت می‌کند یا خیر، اما هر بار از اعلام چنین حمایتی خودداری کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70075" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70074">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70074" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/70074" target="_blank">📅 11:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70073">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbGmkPxY7_hdDTdE5axQS6X9A4sRwXi1Y_Ig-bNZ7h6MqfEfdri8YRvD9D44TfjQCgK8Fgub3Jvi1FtRpIRFjVvZbO0ipsydn0jy-SNzTVs5nQFXV9dCjGyqdkAFNw2Wu_ZJAP1Lx8JvYOUE9eM9vq0q9wpcKh3jHt2lrRw8l45xa8eurizErpB72WeB_laWB5wrtBnHbjUe9rfVTX8uI8aA7RDeQ65_Iq_YwlHlUzxgeZ8CzcgCIxUXh_rCfKvmlLNa6PyUHKH1GJUQaJJifwTPANFuy9XzSAveeh7tbrVR2rXwPfZlvhNkp4VBw-3Ee720gBZy8CV2V1SNzk8igg.jpg" alt="photo" loading="lazy"/></div>
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
r24
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/70073" target="_blank">📅 11:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70072">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f783bdf6d2.mp4?token=hQCGpDYNrakPa5w5hz8-kvacKLSVJs7cxQn-UeSDowodxNqylNwLZgteRpEr2_ug4F2802Rs--w1_xtK40qRsjDT7YPEPs69YrrEix6vebfXm051rMnwRK-QFSDVSU4gqUyFsOa0AyEnh0kWYcSh-AP84dOoMztU_WurYFsb-OtPH5owm2ZAeDmud4OXrqXgtSAJTqV-lObSevAIu63qxOTHSgicby3E0KO5j-94eGakziA6j1mG1E31zF6oKbb8WRMd3UkGG2yQ_kI_P9erN14tQcJ9i22CoDQG31vDiG7hIsnqQ11pNZg1FjR8t_OZxfji7vgc7qRHkjsZini9zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f783bdf6d2.mp4?token=hQCGpDYNrakPa5w5hz8-kvacKLSVJs7cxQn-UeSDowodxNqylNwLZgteRpEr2_ug4F2802Rs--w1_xtK40qRsjDT7YPEPs69YrrEix6vebfXm051rMnwRK-QFSDVSU4gqUyFsOa0AyEnh0kWYcSh-AP84dOoMztU_WurYFsb-OtPH5owm2ZAeDmud4OXrqXgtSAJTqV-lObSevAIu63qxOTHSgicby3E0KO5j-94eGakziA6j1mG1E31zF6oKbb8WRMd3UkGG2yQ_kI_P9erN14tQcJ9i22CoDQG31vDiG7hIsnqQ11pNZg1FjR8t_OZxfji7vgc7qRHkjsZini9zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دیروز تو محل دفن خامنه‌ای یکی اومد به ترامپ فحش بده، حراست زد دهنشو بست:
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70072" target="_blank">📅 11:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70071">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/59dbb77b21.mp4?token=YJO3_K0kbAz0Yn7zh7KT2TFSwK2USPe6-X0ly2MPan5lnHutxMHqEihWgTl1v9d10H0kGCOg1Mg9WkLr0fhNeTcn7x-uyOjXdM7b-bl8T2UN-2cQOsI4HYmzFtDjbplaAztOFHvZGOpOcUQmd3de0KtK3LUVWDQ6b4ZluRKzL9BnSjhQKfG18xP6irLgV-COIsYiYkGaRDJT0v1w4Vny-NpnNG9g4aHc_VbSMMu8i4uk3ddpaePf4YPZeELBh2qBrTkg5mf68KEK9mI2bfnjVQEawn0GcsqljASxdi9_QwZaO0GYAL0eQFjwCWob2RuWjeymDH7-YkIc8d49oSj_UA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/59dbb77b21.mp4?token=YJO3_K0kbAz0Yn7zh7KT2TFSwK2USPe6-X0ly2MPan5lnHutxMHqEihWgTl1v9d10H0kGCOg1Mg9WkLr0fhNeTcn7x-uyOjXdM7b-bl8T2UN-2cQOsI4HYmzFtDjbplaAztOFHvZGOpOcUQmd3de0KtK3LUVWDQ6b4ZluRKzL9BnSjhQKfG18xP6irLgV-COIsYiYkGaRDJT0v1w4Vny-NpnNG9g4aHc_VbSMMu8i4uk3ddpaePf4YPZeELBh2qBrTkg5mf68KEK9mI2bfnjVQEawn0GcsqljASxdi9_QwZaO0GYAL0eQFjwCWob2RuWjeymDH7-YkIc8d49oSj_UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چهارتا دختر یه سفره سه روزه رفتن شمال، حالا چقدر خرج کرده باشن خوبه؟
۵۸ میلیون تومن ناقابل
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70071" target="_blank">📅 10:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70070">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">💢
🎙
صحبتای اشکان خطیبی درباره بازداشتش :
در حال حاضر پناهنده سیاسی هستم، از ۲ سالگی کتاب خوندن رو شروع کردم و وقتی ۱۷ سالم بود وارد دانشگاه شدم و کوچکترین دانشجوی دانشگاه بودم
من رو از جلوی در خونه گرفتن و بازجویی خیلی خشنی داشتم؛ ضرب‌وشتم، تهدید و فحش‌های رکیک و جنسی به خودم و خانوادم
۷ اتهام مختلف هم بهم تفهیم کردن؛ از توهین به ائمه و پیامبر و رهبری گرفته تا دعوت به اغتشاش، برهم زدن امنیت ملی و ضدانقلاب بودن
😳
حداقل ۵ بار دیگه توسط ارگان‌های مختلف بازجویی شدم؛ حتی یه کارشناس مسائل تروریستی خاورمیانه در وزارت ارشاد ازم بازجویی کرد
به‌خاطر استوری و فعالیت تو فضای مجازی این کارا رو با من کردن، ولی میدونستم دارم چیکار می‌کنم چون دیگه تحمل نداشتم.
تنها چیزی که خوشحالم می‌کنه اینه که بدونم یه قدم به آزادی نزدیک‌تر شدیم
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70070" target="_blank">📅 09:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70069">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‼️
این خونه فوق لاکچری که تو سعادت آباد میبینید ویلا نیست!
اپارتمانه که شبیه ویلا ساختن
واقعا اگه اینایی ک این خونه هارو میخرن زندگی میکنن
پس ما چیکار میکنیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70069" target="_blank">📅 09:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70068">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94046ec789.mp4?token=enVYsc6KM90SHnVnBASXHsbp1LDf8YWlficicOrBrIejSaOJQnAtfT-gsnALlrWkKJAEvYugZ5CpI9Dht5nsVv7EPuXyl69oHAvKuMMCO3w3eGVzfL0vzpsttesrNKBPGzdXVaIVLdwDtvBw3dZNPGrlHtroudHJsZ1n3It5QmY3oAMnGJ8FtAxfBjTp-cxbqi0QfI5SejuqzGrSRmCqPadY6DS8V_q6QjuWNV5dQ1UjY9bXUj-FBZGwwmKH0N7m6PL94BXEZrjPO1p20r-y--PfqFNpvHM9Ba9GHMalMo_WQHo_jCVUFoMTNoohXgph9cOhfIEWyjG-z45-QkSNcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94046ec789.mp4?token=enVYsc6KM90SHnVnBASXHsbp1LDf8YWlficicOrBrIejSaOJQnAtfT-gsnALlrWkKJAEvYugZ5CpI9Dht5nsVv7EPuXyl69oHAvKuMMCO3w3eGVzfL0vzpsttesrNKBPGzdXVaIVLdwDtvBw3dZNPGrlHtroudHJsZ1n3It5QmY3oAMnGJ8FtAxfBjTp-cxbqi0QfI5SejuqzGrSRmCqPadY6DS8V_q6QjuWNV5dQ1UjY9bXUj-FBZGwwmKH0N7m6PL94BXEZrjPO1p20r-y--PfqFNpvHM9Ba9GHMalMo_WQHo_jCVUFoMTNoohXgph9cOhfIEWyjG-z45-QkSNcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان:مشکلات ما چندین برابر شده، در حالی که درآمدمان کاهش یافته است.
هزینه‌ها چند برابر شده، مسیر واردات طولانی‌تر و درآمدهای ما کمتر شده است.
نفت را نمی‌توانیم مثل گذشته بفروشیم و با تخریب برخی کارخانه‌ها، درآمد مالیاتی هم کاهش یافته؛
با این حال مجبوریم برای ادامه فعالیت اقتصادی به آن‌ها کمک مالی کنیم.
مشکلات ما چندین برابر شده، در حالی که درآمدمان کاهش یافته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70068" target="_blank">📅 09:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70067">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70067" target="_blank">📅 01:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70066">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=Cvo2DbtdQlMZ1t5RQmsTzyWHeMKnPa9SQY8l1kkHWtSDrrhpQGh0gaLvgXZdrIyPB93bw_DoYQ_iOf4yVT0OfDP7IUFfDyRYWzaH5-Nx-DcUu6Jq97l67QWfTU_xjjeuHcLLHv3f7LuqlpaJtlnch9B-C1P_l1pw_466B9tNYA2q99jfFuuE9ov78JMZueJzZ0wO7Y_7Mlt8eG9vojGoB2-Pvts-UqkSmxraFLF2xFGuKbFZUN5_eAP-OCdzbg-_dTYzmRmMLqAUyOceJZy0MUaEvo9uDWIk93PDTTaRvExJPS8LysfdJtpRkwA36QcS9ZkYpzOw4rCRVmwrNcddbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=Cvo2DbtdQlMZ1t5RQmsTzyWHeMKnPa9SQY8l1kkHWtSDrrhpQGh0gaLvgXZdrIyPB93bw_DoYQ_iOf4yVT0OfDP7IUFfDyRYWzaH5-Nx-DcUu6Jq97l67QWfTU_xjjeuHcLLHv3f7LuqlpaJtlnch9B-C1P_l1pw_466B9tNYA2q99jfFuuE9ov78JMZueJzZ0wO7Y_7Mlt8eG9vojGoB2-Pvts-UqkSmxraFLF2xFGuKbFZUN5_eAP-OCdzbg-_dTYzmRmMLqAUyOceJZy0MUaEvo9uDWIk93PDTTaRvExJPS8LysfdJtpRkwA36QcS9ZkYpzOw4rCRVmwrNcddbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
a23
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70066" target="_blank">📅 01:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70065">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86a20a8bef.mp4?token=lMUc_YSwnxlkrSj2CsyK5ZM1zyGn72n8L048OnNYZW5nborfMq0wZhNUTdqs27P9pR6NSfiPsZqPxb2BvVQdJ6YHfVSh5lcqK_qbH-rYVsqVSPH-P2wNhBM6eDWLlf8ev47FZReksxtgKbGf1JD7Nq9i3v7wSMyp-Ud3AR-tk9VT-exOTlVhuEff7VPZR-_6chY--FAfGmyKiYs791-FBKrneDoCRr1WIMfBXJqqDZdAIhRqpBsb5M-QY8YEg3JgXq8GNJv7q_tDneyfP4PVkHS3oDBsPe-D77UUlNrYNjgyOw_c_Xtnm3GGoSNV9VrTPZSNoUaeo0QFTE0N7qUG1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86a20a8bef.mp4?token=lMUc_YSwnxlkrSj2CsyK5ZM1zyGn72n8L048OnNYZW5nborfMq0wZhNUTdqs27P9pR6NSfiPsZqPxb2BvVQdJ6YHfVSh5lcqK_qbH-rYVsqVSPH-P2wNhBM6eDWLlf8ev47FZReksxtgKbGf1JD7Nq9i3v7wSMyp-Ud3AR-tk9VT-exOTlVhuEff7VPZR-_6chY--FAfGmyKiYs791-FBKrneDoCRr1WIMfBXJqqDZdAIhRqpBsb5M-QY8YEg3JgXq8GNJv7q_tDneyfP4PVkHS3oDBsPe-D77UUlNrYNjgyOw_c_Xtnm3GGoSNV9VrTPZSNoUaeo0QFTE0N7qUG1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🇺🇸
ترامپ:
ما قادریم تمام آنجا را نابود کنیم؛ اما نمی‌خواهیم چنین کاری انجام دهیم.
ما تحریم‌های اقتصادی بی‌سابقه‌ای را علیه آن‌ها اعمال کرده‌ایم.
اگر آن‌ها دست به حمله بزنند، ما صد برابر شدیدتر پاسخ خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70065" target="_blank">📅 00:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70064">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e71c06ff85.mp4?token=IS07Il2k54SE30CY_b2J-uez44kDzFlkC0HAHLX-EIOfcouHqZ8yRiLfjU-LoSWoTjaJ4hJgEedavtrZZDFptJTw4AQCJh1a-6W2FcWkn6_aKOYxbRzYqpl1KPhdKNSWnwjjpXwgsjYRqyCSwcKmHijm0rkzmkz2Ix1z65U2gdnt2x6-3bhawbf6DLjlpgu7_tvLxgdzidUarDGkzhDt4vJQiEMEuF1nghH-QECsDCm8N1k9La-RjilE9OoZxEbqSNTnJrCvAyVv67ORZU_aKwSrQk8PiC_2y4VV0isuSeH_YjRrDoj43fopqgDTCGC6yV1jqC1h9PkmevyJGSfskQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e71c06ff85.mp4?token=IS07Il2k54SE30CY_b2J-uez44kDzFlkC0HAHLX-EIOfcouHqZ8yRiLfjU-LoSWoTjaJ4hJgEedavtrZZDFptJTw4AQCJh1a-6W2FcWkn6_aKOYxbRzYqpl1KPhdKNSWnwjjpXwgsjYRqyCSwcKmHijm0rkzmkz2Ix1z65U2gdnt2x6-3bhawbf6DLjlpgu7_tvLxgdzidUarDGkzhDt4vJQiEMEuF1nghH-QECsDCm8N1k9La-RjilE9OoZxEbqSNTnJrCvAyVv67ORZU_aKwSrQk8PiC_2y4VV0isuSeH_YjRrDoj43fopqgDTCGC6yV1jqC1h9PkmevyJGSfskQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:ایران تنها کشوریه که کسی نمیخواد رئیس جمهورش باشه.
«آن‌ها هیچ رهبری‌ای ندارند.
رهبری‌شان از بین رفته است؛ رده اولشان رفته، رده دومشان رفته و نیمی از رده سومشان هم از دست رفته است.
این یکی از مشکلات من است؛ کسی نیست که با او مذاکره کنم. این یک مشکل است.
من گفتم: "آیا مطمئنید حال این آدم خوب است؟"
اینجا تنها کشور دنیاست که هیچ‌کس نمی‌خواهد رئیس‌جمهورش باشد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70064" target="_blank">📅 00:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70063">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55686a2794.mp4?token=o1um3jOVgI-0wvePthc1S6DsZJ-XYBOgiOJevmws2t2HlT4t_0gCJcuMOp8AIx_114zLcgPsdfI22gwQPFRdDLuAKrgxTVuTtpY0sSqby5c17l0SWVD1XnMkt-uhEqN9wzrbdSwt7d9vlC7AEcCpLNBtEj25u5PuiVf9c1MqaKhFPEyRm9VjevbfvAnPdmd-jYPOzYR7HGbfWHQvsSKb1vrJMzhFx7rjfO44TucQdZ8sH3QGP9nRw4AC0BR00aR45zHIb6KeLS7n88ZFBlnOGhkMUUeEj2VGW4BDcZ8xZH5w8ftO907K4C4Sm5Ct-A_SxnkuFQ_fwrzXq81TxHlNYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55686a2794.mp4?token=o1um3jOVgI-0wvePthc1S6DsZJ-XYBOgiOJevmws2t2HlT4t_0gCJcuMOp8AIx_114zLcgPsdfI22gwQPFRdDLuAKrgxTVuTtpY0sSqby5c17l0SWVD1XnMkt-uhEqN9wzrbdSwt7d9vlC7AEcCpLNBtEj25u5PuiVf9c1MqaKhFPEyRm9VjevbfvAnPdmd-jYPOzYR7HGbfWHQvsSKb1vrJMzhFx7rjfO44TucQdZ8sH3QGP9nRw4AC0BR00aR45zHIb6KeLS7n88ZFBlnOGhkMUUeEj2VGW4BDcZ8xZH5w8ftO907K4C4Sm5Ct-A_SxnkuFQ_fwrzXq81TxHlNYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
«آن‌ها ۲۱۲ هواپیمای بسیار خوب داشتند—برخی را به برکت اوباما، باراک حسین اوباما، به زیبایی از ایالات متحده خریده بودند.
از او شنیده‌اید؟ باراک حسین اوباما. و هر کدام از هواپیماهایشان ساقط شده، از بین رفته.
آن‌ها هیچ رهبری ندارند.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70063" target="_blank">📅 00:07 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70062">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28ccab4d33.mp4?token=bcB3nOQ4seldt4Y5935lP4y-j3IFgb49NggLa423OuYeLM2CATj-cJeCKARp7dU6fhl6QSbSEC1iWl-uJ0Djp55U1MhjNUnqsWO3Hb0eH4MBtfOfPTjg6lIWcH7qPSh8fkNvGDSLqOhnX4ipdyhFKW5qf0I_IUTwnqzYh-0axjHPzq3DQw1O6KbAo0ZcEh8Hj6XSPFjLm5F4GhzqTx-9IXRY6mMjSKHBP3tFG-M2nsjbUsLYv1wIRUskG2oGGpZPJCv-RuUf3syS3uESwVR9RKGn-qxyPHOqxSvdAk7Y_FYBoyqUhc-4Plv8_vY3YrV-QrKiP10fU15aLALXvDngYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28ccab4d33.mp4?token=bcB3nOQ4seldt4Y5935lP4y-j3IFgb49NggLa423OuYeLM2CATj-cJeCKARp7dU6fhl6QSbSEC1iWl-uJ0Djp55U1MhjNUnqsWO3Hb0eH4MBtfOfPTjg6lIWcH7qPSh8fkNvGDSLqOhnX4ipdyhFKW5qf0I_IUTwnqzYh-0axjHPzq3DQw1O6KbAo0ZcEh8Hj6XSPFjLm5F4GhzqTx-9IXRY6mMjSKHBP3tFG-M2nsjbUsLYv1wIRUskG2oGGpZPJCv-RuUf3syS3uESwVR9RKGn-qxyPHOqxSvdAk7Y_FYBoyqUhc-4Plv8_vY3YrV-QrKiP10fU15aLALXvDngYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
«و ما در مورد جمهوری اسلامی ایران هم داریم به موفقیت‌های بزرگی دست می‌یابیم. هیچ‌کس نمی‌داند چقدر موفق عمل کرده‌ایم؛ آن‌ها نمی‌خواهند این را بنویسند، اما خودشان می‌دانند.
می‌دانید چه کسی می‌داند که ما چقدر خوب پیش می‌رویم؟ خودِ ایران. به این فکر کنید: آن‌ها نیروی دریایی ندارند؛ وضعیت کاملاً یک‌طرفه است.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70062" target="_blank">📅 00:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70061">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b256a73ac8.mp4?token=Srfr6iHobs1Lt0IyjMDWhSVxu7btmb_lX2RhdSEwKasiBrfQ-U_VKQz-ilScq91rz-uEUlMIPIZ7g0fT3uyVEd6jnsM9wD2GtAQ6aR4nXD8TM4Iv5sfhdLMDKRPRjToT8y-nfu-kNwgyqJ1KNdiRefX2inUsGQa5m976JdnNVHkf36o0RTdfyia0ktTAUvRbCih4P7E48H_Vh5SITM1p3mVk64aAfx-7GSE7NbiYXqI4A8itBilTZWgTGpqhLATpnoaXttM5vVbnap9qwLlHPcMCYrwqLUzxYnxxajAw-VpYwKM0lfNnkcv85MTxdUkmweD8Jeca3FscJ_gPT86JXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b256a73ac8.mp4?token=Srfr6iHobs1Lt0IyjMDWhSVxu7btmb_lX2RhdSEwKasiBrfQ-U_VKQz-ilScq91rz-uEUlMIPIZ7g0fT3uyVEd6jnsM9wD2GtAQ6aR4nXD8TM4Iv5sfhdLMDKRPRjToT8y-nfu-kNwgyqJ1KNdiRefX2inUsGQa5m976JdnNVHkf36o0RTdfyia0ktTAUvRbCih4P7E48H_Vh5SITM1p3mVk64aAfx-7GSE7NbiYXqI4A8itBilTZWgTGpqhLATpnoaXttM5vVbnap9qwLlHPcMCYrwqLUzxYnxxajAw-VpYwKM0lfNnkcv85MTxdUkmweD8Jeca3FscJ_gPT86JXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
«پس فقط این را می‌گویم. اینکه کمی بیشتر برای بنزین خود پول پرداخت کنید، فقط به یاد داشته باشید که این کار را می‌کنید تا یک کشور بسیار شرور نتواند سلاح هسته‌ای داشته باشد، کشوری که واقعاً حامی شماره یک تروریسم دولتی در جهان است. ما نمی‌خواهیم آن‌ها سلاح هسته‌ای داشته باشند.
پس وقتی مجبور شدید کمی بیشتر پرداخت کنید، حتی اگر به چهار دلار برسد، اشکالی ندارد. من هرگز عذرخواهی نخواهم کرد، کار درستی انجام دادم. اگر این نبود، منظورم این است، من در بسیاری از ایالت‌ها قیمت را به زیر دو دلار رسانده بودم، اما کالیفرنیا را نمی‌توان شامل شد چون آن‌ها مدام مالیات وضع می‌کنند و وضع می‌کنند. شما قیمت نفت را پایین می‌آورید و آن‌ها در نهایت بیشتر از آنچه پایین آوردید، از شما مالیات می‌گیرند.
فقط باید به یاد داشته باشید که کاری که ما انجام می‌دهیم، خدمتی بزرگ به جهان است، نه تنها برای خودمان، بلکه برای جهان، و ما واقعاً کار بزرگی انجام می‌دهیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70061" target="_blank">📅 00:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70060">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40c189273f.mp4?token=VMfsM3Sv7JSZgbHbyxRGeWg5dLe4q-ecz2ahtRCC92xIoFS4kwjL1v2Nrf5lHZFlj5dtrzLtaVkhIF4to4NCCZ_PXD2CHUgGKa24u82yGledOo-NobMRyuFmUD7uVGmYXeKbBGotO9ngeD3NnF7dVTzlxtU2GZv4vpoD36hnAV8hW1M4cdpWh3EG4euWfTayaRLmwBftf3i12sF4f7mo3p8T-4CkLZMNY2NWZ8g4YxByqncJQRAowgMwZmrS8pt88LlaCVEfJA7q-_S13P6qARgvoU-hKirpMc4s3ULIcX0CN7MRZMXKlo7IQIQZPsiihtCQKcc2TjTieSUJYC-hPLEki6znWQfSs8lk6TOp4Y8qSATLLPlV9LtRNLZdWpSvfMVyxfOFteWFJU1xIoqEGLpt60vxuk5m3p5OWcq6xAF_PWNp4vnhNZV7n_SjhBoQTL-eIP8YXH9xP3alToh8GIA6HR7S0-HcI-0-yv9pMyfk1RMIu8hbBWss2taSzviKdlmQMcr_Xp5w8HJkbuvLsdv44IaN1ufl2ReXs9R6pBZRcooyGzF67wfs88RjZaA5EBinOBiWcT6ff-zVfIf_e_RrE_LPQPjP-_I9XZb16NNeR_k1L9vOslyVW0TrotfkHsxeMC85udxAiUOd43H1m0FRD7vTaVXHWCVcBFOpVs0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40c189273f.mp4?token=VMfsM3Sv7JSZgbHbyxRGeWg5dLe4q-ecz2ahtRCC92xIoFS4kwjL1v2Nrf5lHZFlj5dtrzLtaVkhIF4to4NCCZ_PXD2CHUgGKa24u82yGledOo-NobMRyuFmUD7uVGmYXeKbBGotO9ngeD3NnF7dVTzlxtU2GZv4vpoD36hnAV8hW1M4cdpWh3EG4euWfTayaRLmwBftf3i12sF4f7mo3p8T-4CkLZMNY2NWZ8g4YxByqncJQRAowgMwZmrS8pt88LlaCVEfJA7q-_S13P6qARgvoU-hKirpMc4s3ULIcX0CN7MRZMXKlo7IQIQZPsiihtCQKcc2TjTieSUJYC-hPLEki6znWQfSs8lk6TOp4Y8qSATLLPlV9LtRNLZdWpSvfMVyxfOFteWFJU1xIoqEGLpt60vxuk5m3p5OWcq6xAF_PWNp4vnhNZV7n_SjhBoQTL-eIP8YXH9xP3alToh8GIA6HR7S0-HcI-0-yv9pMyfk1RMIu8hbBWss2taSzviKdlmQMcr_Xp5w8HJkbuvLsdv44IaN1ufl2ReXs9R6pBZRcooyGzF67wfs88RjZaA5EBinOBiWcT6ff-zVfIf_e_RrE_LPQPjP-_I9XZb16NNeR_k1L9vOslyVW0TrotfkHsxeMC85udxAiUOd43H1m0FRD7vTaVXHWCVcBFOpVs0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ایران به‌شدت در حال شکست خوردنه.
به‌زودی اعلام می‌کنم که تنگه هرمز به قلمرو ایالات متحده تبدیل شده.
به افرادم گفتم: «باید یه سفر کوچیک به خاورمیانه داشته باشیم، چون باید جلوی یه فاجعه احتمالی رو بگیریم؛ یه آتش خیلی بزرگ، چیزی که تا حالا مثلش رو ندیدید.»
وقتی مجبور بشید برای بنزین یه مقدار بیشتر پول بدید، من هیچ‌وقت بابتش عذرخواهی نمی‌کنم. من کار درست رو انجام دادم.
یک کشور خیلی شرور نباید سلاح هسته‌ای داشته باشه.
کاری که ما داریم انجام میدیم، خدمت بزرگی به دنیاست؛ نه فقط برای خودمون، بلکه برای کل دنیا.
ما واقعاً داریم کار بزرگی انجام میدیم. محاصره مثل یک دیوار فولادیه.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70060" target="_blank">📅 23:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70059">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjvXBTj_Z1LyZ3MA2FRjNmcLEmz7TNab89Ix3Xh4LWYnJgbK1a_6M9FqmsxTqVVpGlAvL5_021H3sBUryhKAUy0YdTYfvUphqWguIqttuVOVTDZUZ_BGGI3QpjKAbr65pYGS1XkBKahmmxjJO4RopPUGo6PTj5C9urin9ws3N9WKHOmEdjqaUVh6FmmFu1FtKwrxa1JT9J12LznKNPbDFAyr5YmxMosFUK32QqFxouVYGu1T8Z-DLAjLM7cPWRPU1ybE1IQf2oceGu_8vWRJoBixlfCWOyKdaRzlMlDOYWSeVPhZunBZcCSEQj5JbWCZk_bGi9NPY_Id-gcNcUxg3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70059" target="_blank">📅 23:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70058">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d105db041c.mp4?token=IpOELqdgg8rjhMvTgkC0Iu4tbLNqS5YeDIKy6SvTVtOdA6Dq9K40UZ_1WgZyKZ4Q7KTrOes7jIBRjZMyfxDt3VQO6TeTx8pCGODcRGPF-vTYt5iTOYVT5M1PJO5cMHtc8lqXXZL9FE6zybUS8pOtlZDHWIhtRgIP5fab4hEWR7YDEHTaBunVABE01TUrcS6eHXt9jb91mSU66WBXfoAlfJbMGMgkepRqfr3eMl34sAMv9XVYJH6B0TgxALPN4JT6xXF4p2LTFxRQh7fK99Gyp-pAzrHDEguwoUN_erVUdrT1P2QFHlVbSzf6UM7AAYYhwU2xqEnQIz9uEhIsvOY4sxH7HlZ1hOdYm9_B7rm4oFCm-xpHZ9qhtNuIokK9tHgQN0iu_ePlZI4yDJOcOe2mkMyO8uhgbpLphyiJMZ312j8Nwxg08vnQwxXTZxlnZ38smSRzVPZi7WMtWkbLNQJbCcIY-egekuhvWqlrVp3ZQmEax_psu_jJgs4QWGcFduUPdlbgkUnLV07pWjIrW7LeF7LLt77kU33Fl0LumRaQwiiJ2Osoe3P0Gnq58uICf7dyU2IbRe72yoQGRg9VuZhpgwSavI7OmH_mAKNJsPJpIho7ubHvW_OwK7gtlMAsuHfQINi-2mtDbEx6BEbVbZsfWjZpFWuAns0aJwkyS78rTjc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d105db041c.mp4?token=IpOELqdgg8rjhMvTgkC0Iu4tbLNqS5YeDIKy6SvTVtOdA6Dq9K40UZ_1WgZyKZ4Q7KTrOes7jIBRjZMyfxDt3VQO6TeTx8pCGODcRGPF-vTYt5iTOYVT5M1PJO5cMHtc8lqXXZL9FE6zybUS8pOtlZDHWIhtRgIP5fab4hEWR7YDEHTaBunVABE01TUrcS6eHXt9jb91mSU66WBXfoAlfJbMGMgkepRqfr3eMl34sAMv9XVYJH6B0TgxALPN4JT6xXF4p2LTFxRQh7fK99Gyp-pAzrHDEguwoUN_erVUdrT1P2QFHlVbSzf6UM7AAYYhwU2xqEnQIz9uEhIsvOY4sxH7HlZ1hOdYm9_B7rm4oFCm-xpHZ9qhtNuIokK9tHgQN0iu_ePlZI4yDJOcOe2mkMyO8uhgbpLphyiJMZ312j8Nwxg08vnQwxXTZxlnZ38smSRzVPZi7WMtWkbLNQJbCcIY-egekuhvWqlrVp3ZQmEax_psu_jJgs4QWGcFduUPdlbgkUnLV07pWjIrW7LeF7LLt77kU33Fl0LumRaQwiiJ2Osoe3P0Gnq58uICf7dyU2IbRe72yoQGRg9VuZhpgwSavI7OmH_mAKNJsPJpIho7ubHvW_OwK7gtlMAsuHfQINi-2mtDbEx6BEbVbZsfWjZpFWuAns0aJwkyS78rTjc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار
: اعضای خانواده نظامیان درباره شرایط داخل ناو «آبراهام لینکلن» نگران هستند.
🇺🇸
ترامپ
: نه، آنها نگران نیستند. این ناو همین حالا یا خیلی زود حرکت خواهد کرد و یک ناو بسیار مشابه جایگزین آن خواهد شد.
🔴
خبرنگار
: آیا مأموریت این ناو بیش از حد طولانی شده است؟
🇺🇸
ترامپ
: نه. نه. نه. اصلاً به اندازه کافی طولانی نبوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70058" target="_blank">📅 22:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70056">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c20969ce7.mp4?token=fzA2wUVdjJygX4WwaS1eHEHCtIYdsZsU2ErAeQ06NFQfE4wG1rk7snv8P7R0AbiwDe-MKAKMOjUx3_cs_rCRnLpjGhGffY7M2crvlMhw2kC3PR-VF6wDHIZwD_sn3SDinP_4r-plpL7CFRA5mMmKLLvPkOQwPNKWzxdzQy0OmWqqJadiq9o7_if746aLUYUeW0VmieWEOgRn3AoESDe8LBX_3T3XGAgzFChQ15ZT2NwrXJD5kXqX71v5Ce4q7rXKtoNwk5bS5Q9ZTgy-b9S0layQLxrRCCNavRUKqzDl6ITDeiPaRj6ARtIWYPw3G3713oZsyj8gwQ8CeI792TqgxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c20969ce7.mp4?token=fzA2wUVdjJygX4WwaS1eHEHCtIYdsZsU2ErAeQ06NFQfE4wG1rk7snv8P7R0AbiwDe-MKAKMOjUx3_cs_rCRnLpjGhGffY7M2crvlMhw2kC3PR-VF6wDHIZwD_sn3SDinP_4r-plpL7CFRA5mMmKLLvPkOQwPNKWzxdzQy0OmWqqJadiq9o7_if746aLUYUeW0VmieWEOgRn3AoESDe8LBX_3T3XGAgzFChQ15ZT2NwrXJD5kXqX71v5Ce4q7rXKtoNwk5bS5Q9ZTgy-b9S0layQLxrRCCNavRUKqzDl6ITDeiPaRj6ARtIWYPw3G3713oZsyj8gwQ8CeI792TqgxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک جت جنگنده اوکراینی مدل میگ-29، امروز صبح در حین تعقیب یک پهپاد روسی مدل "گران" بر فراز منطقه اودسا، موفق به سرنگون کردن آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70056" target="_blank">📅 21:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70052">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CTlMRyCr_9NNnM1oTIxiMDwIVfAUdzeAPNE5Ki632qlyPu4MpdANwtYdDVCRd2ppB1vLva5BdsGiqqEONYGrvIKPRsJPz543jsDLdchMjVVx7RprHcFV-Fn4_Fpihwn6uSkCb7ugu8slr4uqKwBLDf2zJtjCkvscSKIPFhF88XlgQeceExwUd1gjdC_uraFP8Q_ZdCvMb7XnDMpRvFifBALNExrXoOCWN3VVapjCa8xHvvbQ1b1oTRd4-usySjiEQ-sGYanzRUc6xYXKHH5gbUbTyFjYR9OJ3E8aOFY0U3z8CrZiLTIZ5GbTtKC6IDJLQSt9B1fos_MD-WrTgb6TFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZO2QVLfzUAxe93u39E-Z5uW0Svkt-hSoJOx7dVGfALTd83b3wcvndWEQhMjoCw3RRqg3zmkHy_uZKvatOuQNQ5avqj4_0E_X2a4qFdarlxhwA_cSI_XCTFKuKXwpsoIrdkiZNTYcjQ2tVSkohGw-CmbaFyZBaJhgy-eB_-B-lU5fQ4Z-zaCsaYk1z6LZ5HMag6UaS2DjMokMrepJ5a2Ku5oCnCKkLKteFki2UPcmuWsVEW3LVIRF7_Os8_5a_rvescwYdw4ZZY_ou5WyVr7z6NAyu2nDl2ddmLiBa11pz5txL5krnpDCQ95EZJx8xnAqDZgpCcQ8zl10vRMFd1ohFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tKhZtR_CLT3OVnsZFWB59HRNIaHVg3P2vK6Lb1DxC1kOcOI3SZmJCmYsrF1aKp4EJtJ77-ZNS_JfOcIYxUoMJDNnA3rTxoldRVbGjOFvq9dFpKXvSoVQfZsjdUFsZd9r5YcQqC0KDeObgbSUQf9LnTPgd8gZChe92Z_c3_lz6KyXGcXNpw6qWSjBZ0XHWO7YaTrz64fZ6sX_zuG552DX48BSqQduWuvuUIFPqWpMEy8MxAUCEbhtCIKFttiV3HfNepckPwQlsvOL-Vmn2zjiI4pfpZTQxSV7ivkkixoE5oUFx9Mwjlj0MWYwn6_r25CuNxI1h0sR3qCFBFAHiaqSSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5cd1ffaaa.mp4?token=ca3_gwERKzI5YVIC9QcSC_0wIzjQECGtVpSO3xdBUxKubJxRLzbtKjzEnnCqmN4ALq8xzMU9qssXYTycbh1Htmmp_DinIHGpZVL63dWZy9F1dI_eLhCZ2Ur7bcqnd9G4QAPqihe5zFrah9U4NWTPNhwcsPr491nSFkMzDmgGyLkhvd5JthqHJkk9QTfD5WXs3-TI1kpcwHTi2PDIjLOQMeRpKk5XNEn-iiL4m-Sbw5hP0cgfKh_Wwa-1nXNoWZsQ1QGKp1snnMFzDd5hj4E1yrxl7Fv9PAZJ3frNfz5gWDTnXWxBturaNI8qDPnXkxj2jq7pWeadrlQFtPKGadFJMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5cd1ffaaa.mp4?token=ca3_gwERKzI5YVIC9QcSC_0wIzjQECGtVpSO3xdBUxKubJxRLzbtKjzEnnCqmN4ALq8xzMU9qssXYTycbh1Htmmp_DinIHGpZVL63dWZy9F1dI_eLhCZ2Ur7bcqnd9G4QAPqihe5zFrah9U4NWTPNhwcsPr491nSFkMzDmgGyLkhvd5JthqHJkk9QTfD5WXs3-TI1kpcwHTi2PDIjLOQMeRpKk5XNEn-iiL4m-Sbw5hP0cgfKh_Wwa-1nXNoWZsQ1QGKp1snnMFzDd5hj4E1yrxl7Fv9PAZJ3frNfz5gWDTnXWxBturaNI8qDPnXkxj2jq7pWeadrlQFtPKGadFJMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
〰️
صفحه اسرائیل به فارسی در پلتفرم ایکس:دو مهمون خوشگل از ایران
🦌
امروز صبح جنگلبان پارک ملی برعام در منطقه گالیل شمال اسرائیل با یک منظره زیبا روبرو شد. دو گوزن زرد ایرانی که احتمالا از اندوخته‌گاه طبیعی که در مجاورت پارک است به آنجا آمده بودند.
گوزن زرد ایرانی زیرگونه‌ای از گوزن زرد است که در آستانه انقراض قرار داشت. اما با تمهیدات دولت ایران در دوران پادشاهی پهلوی، موفق به حفظ این نسل شدند.
سازمان طبعیت و پارک‌های اسرائیل در سال‌های پیش از انقلاب وارد گفتگوهایی با دولت شاهنشاهی شد تا چند راس از آن‌ها را برای حفاظت به اسرائیل بیاورند. به موازات آن، اسرائیل دو راس گوزن نر از آلمان گرفت که پیشتر از ایران برای حفاظت به آنجا انتقال یافته بودند.
لحظاتی پیش از آمدن خمینی و در آخرین پرواز تهران - تل‌آویو ۴ راس ماده گوزن زرد آنطور که دولت شاهنشاهی وعده داده بود، با کمک تیمسار منوچهر خسروداد به اسرائیل انتقال داده شدند. اکنون چند گله از گوزن زرد ایرانی در کوه کارمل در اسرائیل زندگی می‌کنند و تحت حفاظت قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70052" target="_blank">📅 20:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70051">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8pl3-d1qihd2iXd9ygzRBq_sBoXv8PGyW7HK-ryiasSCTXo6gopYYn9V3ljttdiM48G1hIT3RRVFsRKObwljU2HBqsvapKWIrbHytYh0OTcsSf4TZ0rfXyAVGc1M1bwLv0A9ivs-RGlFpFEkPHvhypUyipX5DdjwIms19qDkPbmrS_r7qlladi6WXFIs708Cf4R_J2-Wjo9LY1ovvq12m_N2cEPkepvxPjZ9YSsPviyJCzhOD9ijEgzfWb8cyFt3xNEwVkuMYPyt8-o89McjuC0zv7d_hSZl1E7jADJW5lBRbv19XshdZ6w3P6LYMbm01JP5b5gbiFMFAU_sRLNhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
〰️
فرماندهی
CENTCOM: اقدامات آمریکا علیه کشتی‌های مرتبط با بنادر ایران
:
🔴
فرماندهی مرکزی آمریکا (CENTCOM) اعلام کرد نیروهای آمریکایی از زمان تشدید محاصره بنادر ایران:
🔹
۶۲ کشتی تجاری
را تغییر مسیر داده‌اند؛
🔹
۳ کشتی
را از کار انداخته‌اند؛
🔹
و
۲ کشتی
را برای اطمینان از رعایت مقررات، بازرسی و توقیف موقت کرده‌اند.
به گفته CENTCOM، این اقدامات در چارچوب اجرای محاصره بنادر ایران انجام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70051" target="_blank">📅 20:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70050">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1768f156c.mp4?token=XRqFQhWeEPFxxHEgrWTZEdKy6q3goYPujQkAZRYmwPER_xknLgc3s8mPGzbASfxInk7flkLchqQdUdRVfHKGpTIdJQRPlFQLJO4GI0jjjNHDfuucdmFVbT-hLhppyOO-w_QCUSbhqY6DzqVatN3FI-hhvV7t7h1brN9VDzomBSwkgwL3Idi0j0p_4A8WgQ-qRZhVEeLlC5Hh_7qHIGOlDjrJoS30e71n4HVahvjeEOgPymmVXMnrW9iQK_QvpW_Ii50OjV_rnjluOjYWZ1utJgQgBP51SFUb9_EZdk5WH6RT2UJLlUQWDbR2qU1H7tytwlyDQCTsgiZWRO9AUtciig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1768f156c.mp4?token=XRqFQhWeEPFxxHEgrWTZEdKy6q3goYPujQkAZRYmwPER_xknLgc3s8mPGzbASfxInk7flkLchqQdUdRVfHKGpTIdJQRPlFQLJO4GI0jjjNHDfuucdmFVbT-hLhppyOO-w_QCUSbhqY6DzqVatN3FI-hhvV7t7h1brN9VDzomBSwkgwL3Idi0j0p_4A8WgQ-qRZhVEeLlC5Hh_7qHIGOlDjrJoS30e71n4HVahvjeEOgPymmVXMnrW9iQK_QvpW_Ii50OjV_rnjluOjYWZ1utJgQgBP51SFUb9_EZdk5WH6RT2UJLlUQWDbR2qU1H7tytwlyDQCTsgiZWRO9AUtciig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پسرا وقتی حوصله‌شون سر میره بالاخره یجوری خودشون رو باید سرگرم کنن دیگه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70050" target="_blank">📅 19:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70046">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c9b730cb.mp4?token=EzbKgwnGJlFjWlthMSFL8AFcwi505XxflJOECdlsRgOlBnjUoBGL-VIQzYkJXUuDtxyV1jBEOGN5bguCXOc5iE0ZYpm4gNQTfpI9MlYTC6Nthcwv6DBQFCdu1YYmEwuRwnYSFDwuaIHo30bjdl_HmI_AXG6GBeyei_GUWPT9JJOsybLpWDFEJjOcVGlvV3uvE7YtHSz1o1lq_WKQx6S4ZNsfDyTsUpQ4eqamL1TBrJqWMXucj5jVKE0dvWvMGLl6N3LLCzNlfMk0rXxY_mLJnEDqLcJfLcp9lVDuZO3T8XAkaNqv-CAJwrkRC0QLXzIri7uOgwZ8Mx5wp93h1pCOQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c9b730cb.mp4?token=EzbKgwnGJlFjWlthMSFL8AFcwi505XxflJOECdlsRgOlBnjUoBGL-VIQzYkJXUuDtxyV1jBEOGN5bguCXOc5iE0ZYpm4gNQTfpI9MlYTC6Nthcwv6DBQFCdu1YYmEwuRwnYSFDwuaIHo30bjdl_HmI_AXG6GBeyei_GUWPT9JJOsybLpWDFEJjOcVGlvV3uvE7YtHSz1o1lq_WKQx6S4ZNsfDyTsUpQ4eqamL1TBrJqWMXucj5jVKE0dvWvMGLl6N3LLCzNlfMk0rXxY_mLJnEDqLcJfLcp9lVDuZO3T8XAkaNqv-CAJwrkRC0QLXzIri7uOgwZ8Mx5wp93h1pCOQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
رسانه‌های دولتی: ایران لاشه جنگنده F-15E Strike Eagle نیروی هوایی آمریکا (با شماره دم 00-3000) را به نمایش گذاشتند؛ هواپیمایی که اوایل ماه آوریل در جریان جنگ، با استفاده از یک سامانه پدافند هوایی جدید و تاکتیک‌های ایرانی سرنگون شده بود.
این تصاویر همچنین پهپادهای سرنگون‌شده یا توقیف‌شده آمریکایی و اسرائیلی، از جمله MQ-9 Reaper، Hermes 900 و Hermes 450 را نشان می‌داد که علی‌رغم قابلیت‌های پنهان‌کاری (گریز از رادار)، رهگیری و ساقط شده بودند.
ایران علاوه بر این، پایانه‌های «استارلینک» (Starlink) را به نمایش گذاشت که به گفته مقامات ایرانی، برای هدایت پهپادهای آمریکایی و اسرائیلی و برقراری ارتباط با عوامل و همدستان داخلی در ایران مورد استفاده قرار می‌گرفتند.
در جریان این جنگ، ۱۷۰ فروند هواپیمای آمریکایی و اسرائیلی توسط یگان‌های پدافند هوایی سپاه پاسداران سرنگون شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70046" target="_blank">📅 18:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70045">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/488afe5f03.mp4?token=LMKQIe-ae-nc-gjTCkYfKOigDNNJJp4PgOxDJnF3siqr5_WY9nknr6TkYDAs4b5TSUSUGeblAVCHRJqqzHhk88jhN0nwCnID9xJv0qvVlM58XqzicBQzRu8kv_HD0I0TDbgQBaOyNQ1Q9S_FYO9WI4XdHlpzLZBnuAkLrxrLLF0oBh5XssUd8GzykfBf4gXxr6x2lH2yIRS7jFu9ZOsE9aZHpenQziJwvf0xX2RjgJ1xwpmYMyWG7CJlSRIB3eaA5kVZpBF9BCjpOFZ6fCC8ArTB-4cgUV-jOmbUs1Q1zEK6LyoIeFD1e5ukjr7uvn7iWiUSlgv6oJuF0Yq3Q4s2Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/488afe5f03.mp4?token=LMKQIe-ae-nc-gjTCkYfKOigDNNJJp4PgOxDJnF3siqr5_WY9nknr6TkYDAs4b5TSUSUGeblAVCHRJqqzHhk88jhN0nwCnID9xJv0qvVlM58XqzicBQzRu8kv_HD0I0TDbgQBaOyNQ1Q9S_FYO9WI4XdHlpzLZBnuAkLrxrLLF0oBh5XssUd8GzykfBf4gXxr6x2lH2yIRS7jFu9ZOsE9aZHpenQziJwvf0xX2RjgJ1xwpmYMyWG7CJlSRIB3eaA5kVZpBF9BCjpOFZ6fCC8ArTB-4cgUV-jOmbUs1Q1zEK6LyoIeFD1e5ukjr7uvn7iWiUSlgv6oJuF0Yq3Q4s2Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو تبریک تولد این چند تا دختر و پسر بچه، از هزار تا سکانس فیلم ترسناک بدتره!!
😶
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70045" target="_blank">📅 18:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70044">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">معتبرترین سایت بین المللی شرط بندی که به ایرانیا خدمات میده
✅
وقتش رسیده قید سایتا ایرانی بزنی و توی سایت بین المللی فعالیت کنی
⚠️
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/70044" target="_blank">📅 18:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70043">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kz4nSbLpricxluyypdWdycZx38D4cOh3I2OF-lg7cjnETNtgjp0okGuisley3eynmLfN9IG7EbEjdQeKUweELHiiCrvj4kZzaiqoo09hlp7KLsTjt1Y3f-FASeSvobUWBMWKYL-10OTcU3Pb0XJjh5MHPe0IkDmvHdoCJpwOehrksMBeUrGCHcnXEQeKM4nzLkvPYC1vhvCNSr-SRSy0h2WksID5-QvaUkXTqhH90ULzChmZDbr8UvXZV_xd2exDZpinPCo0knLrrdWR6HV3Cg9kkleRgStib5Ad5-T7BU1Tqe9F31dQRhxFZj_NbCgYz2yMyqegAGrsvlIY9oxvZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g23
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/70043" target="_blank">📅 18:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70042">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a464071683.mp4?token=oHXD8_aYggEJnQtBEMcEYM3Aq_C3_06LfSOI2lqYs7pER2Qt4Yvhx9Ebvx4oklIkgtKis83JbRFVoD1_nf333Rx8qwgOevj_WQlQY4ykef6uUE3xWi5S5NG8bMX-nIEloUcgJyD01pn38iOCgc2oUDAVcfl9TUe7PdMuzKuy-WPpErjFmg0iSmN_hyxOWqYI43NB5oRAYXL0XiGZ9DDmsSm5DKIsP2to9ycR-LWLZ8ZTzaev9_k_e-xfQW_gRGzVFOy6vUmxXc_BSwDAGgQuDg04DPo6l648D1RLjgc_WuvY0d1L95mAgZ8cMfmhjt7YhViv2zojmgLEXNxU082GKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a464071683.mp4?token=oHXD8_aYggEJnQtBEMcEYM3Aq_C3_06LfSOI2lqYs7pER2Qt4Yvhx9Ebvx4oklIkgtKis83JbRFVoD1_nf333Rx8qwgOevj_WQlQY4ykef6uUE3xWi5S5NG8bMX-nIEloUcgJyD01pn38iOCgc2oUDAVcfl9TUe7PdMuzKuy-WPpErjFmg0iSmN_hyxOWqYI43NB5oRAYXL0XiGZ9DDmsSm5DKIsP2to9ycR-LWLZ8ZTzaev9_k_e-xfQW_gRGzVFOy6vUmxXc_BSwDAGgQuDg04DPo6l648D1RLjgc_WuvY0d1L95mAgZ8cMfmhjt7YhViv2zojmgLEXNxU082GKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
یک خورشیدگرفتگی از فضا چطور به نظر میرسه؟تماشا کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70042" target="_blank">📅 18:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70041">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/36594ef37b.mp4?token=XfA8EbF_gDRTZHd0ILWmyaA3NiPBXRcc_BZLJWCv4o2cVlbuNNgLkG-1szKE46M3YsMNkbtcdwmfvS7gD43gufR9tA0H49ktfvEkWl7Jx2NQm3Ej1C7MfU2x6VGm8Ux73jN2G-7PaLPpYy3fqIugddd--pFNsOKYM8xEgS2tysVpOeAhMinNDmCi_0xmjM-AnK-euYaENsmBxCFHs5u2uJExZFal-XlfXp-n8zaJAVD1uMJOxWZxJbl5Oj_Ke7nLnjMvl2lNCQyIOyaZm7eUpALsfSKTvrHzJb7M11CX0TLjbQSXhwfcXUKJAEyLwsB4xHA6HaAnUPgvy7kqILEEyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/36594ef37b.mp4?token=XfA8EbF_gDRTZHd0ILWmyaA3NiPBXRcc_BZLJWCv4o2cVlbuNNgLkG-1szKE46M3YsMNkbtcdwmfvS7gD43gufR9tA0H49ktfvEkWl7Jx2NQm3Ej1C7MfU2x6VGm8Ux73jN2G-7PaLPpYy3fqIugddd--pFNsOKYM8xEgS2tysVpOeAhMinNDmCi_0xmjM-AnK-euYaENsmBxCFHs5u2uJExZFal-XlfXp-n8zaJAVD1uMJOxWZxJbl5Oj_Ke7nLnjMvl2lNCQyIOyaZm7eUpALsfSKTvrHzJb7M11CX0TLjbQSXhwfcXUKJAEyLwsB4xHA6HaAnUPgvy7kqILEEyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این برنامه‌نویس یه شلاق ساخته و باهاش هوش مصنوعیو میزنه که باعث میشه هوش مصنوعی خیلی سریع‌تر کارکنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70041" target="_blank">📅 17:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70040">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4ee0155b21.mp4?token=Pu_3eKYvpXRtfnQzcDAnFTka_gSa7m0tDAZo2ubRRSyMpqUoWc-R266xDSzq0FqZYfVaX-lwDDO-Zt_lR5JQBJREA1uQyMsuhn9PSVt48sHQqaFalCwrRLpMubeWaMgH4Fsbm0bcVAOa3pYpksMdz5jdAtB27V8Forl4zSymP5yqQ8Hp4SjywrtLyPYBzIph4giTWSJ0WPaWnfTV4GL7rb5r32j8B4RvI8_wLiafeH0WCvLEH1IdlAPZ5R9WVAPt7Xq3jxthr1gze-seJcezMj0kxCAZFlxnOw0nGYW4-il-pso1DEsvAA6Wi7lKM0vAbfv0YBfWMBVZSMWJOawjEw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4ee0155b21.mp4?token=Pu_3eKYvpXRtfnQzcDAnFTka_gSa7m0tDAZo2ubRRSyMpqUoWc-R266xDSzq0FqZYfVaX-lwDDO-Zt_lR5JQBJREA1uQyMsuhn9PSVt48sHQqaFalCwrRLpMubeWaMgH4Fsbm0bcVAOa3pYpksMdz5jdAtB27V8Forl4zSymP5yqQ8Hp4SjywrtLyPYBzIph4giTWSJ0WPaWnfTV4GL7rb5r32j8B4RvI8_wLiafeH0WCvLEH1IdlAPZ5R9WVAPt7Xq3jxthr1gze-seJcezMj0kxCAZFlxnOw0nGYW4-il-pso1DEsvAA6Wi7lKM0vAbfv0YBfWMBVZSMWJOawjEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این چند تا پسر برنامه گذاشتن که مسافرت برن اردبیل رفیقشون میگه من چک دارم نمیتونم بیام ولی دوستاش هم از بس عاشقش بودن اینجوری بردنش:
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70040" target="_blank">📅 16:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70039">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WARko-IZJKpLXfuXc9cEtscS1NuwjYhQizIiLI3L9wUu3A161sywqtYuZDX2MdnON603TgMAbIjNgO5ZeCbg-MoVgxATWR8zsBFmKe-Z2vMICtzNhbr1onfgVUQ5OxaGSykQXK61uE-Yrq4a3jiRialhw49uvdSwGd_FqPLZyCCnrS6XFRrHwb96zWP9_Bq_wfhbfjN0aUxDNli7c38TI6oKlBVJ6Nuf53UOaGMaX6IyfO38rowMY2AKq7NbKSlWvcNcGDLkg85SxwMKnT_DXYuLKTNietbq7EFqRRVxlL8aq5p71vj1yQlZy02UV7uR_3m-xNhpbyXytokQ1EHBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
اسکات بسنت، وزیر خزانه‌داری آمریکا، از اقدامات «بی‌سابقه» برای منزوی‌سازی اقتصادی ایران خبر می‌دهد:  «یک سال پیش، در ماه مارس (مارس ۲۰۲۵)، رئیس‌جمهور به من دستور داد تا سیاست "فشار حداکثری" را علیه حکومت ایران اعمال کنم و وزارت خزانه‌داری نیز چنین کرد.…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70039" target="_blank">📅 16:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70038">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‼️
هوش‌مصنوعیِ لاس زن دیده بودید؟
🟡
از دوتا هوش‌مصنوعی‌ میخواد که این نقش‌هارو بازی کنن؛
یکی باید نقش انسان رو بازی کنه که 3 روزه نرفته سرکار و مریضه و جواب تلفن هم نداده.
اون‌یکی باید نقش رئیسِ اون شخص رو بازی کنه.
جالبه که تهش نه‌تنها قضیه ختم به‌خیر شد، بلکه داشتن "لاسِ مصنوعی" هم میزدن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70038" target="_blank">📅 15:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70037">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⏺
🇮🇷
سپاه پاسداران:انهدام پهپاد MQ9 در آسمان هرمزگان
یک پهپاد MQ9 توسط سامانه نوین پدافند پیشرفته سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور امروز صبح در آسمان هرمزگان منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70037" target="_blank">📅 15:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70036">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/93a5f3f1ba.mp4?token=j7blXDgcTLteQPJtKwDqzqYGolwRoW6mQh9g-o_w4WyNoZbfSwgSneioazCKODGHYfqsIvoY3rz8Mk10YLBtTJXG7jitb6goeiTqqgZ2_ufutAZYE1YqJUfFV3XnEfrNmMllNH8UaTOoaIEpAqA4N6hXVLCGxPzjfhrvlfoIB9XongjeZ8M7V9AzDjd9Cd34iTxn03CehpvP5ILEjAjig6v8zYTVY_wjTRnnyPmGevEfb7jp6mWOVtBtzhv-EFrwHmk3mKlh4d_neyx91DtsLw7RweBFkuGiJkahOLH48IvrcuVdwdGWaA8o3unwcxcunutCTabd4-80G9S-49mnKg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/93a5f3f1ba.mp4?token=j7blXDgcTLteQPJtKwDqzqYGolwRoW6mQh9g-o_w4WyNoZbfSwgSneioazCKODGHYfqsIvoY3rz8Mk10YLBtTJXG7jitb6goeiTqqgZ2_ufutAZYE1YqJUfFV3XnEfrNmMllNH8UaTOoaIEpAqA4N6hXVLCGxPzjfhrvlfoIB9XongjeZ8M7V9AzDjd9Cd34iTxn03CehpvP5ILEjAjig6v8zYTVY_wjTRnnyPmGevEfb7jp6mWOVtBtzhv-EFrwHmk3mKlh4d_neyx91DtsLw7RweBFkuGiJkahOLH48IvrcuVdwdGWaA8o3unwcxcunutCTabd4-80G9S-49mnKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ایشون خیلی زیبا، دقیق و کامل توضیح میده که سکس فقط همون چند دقیقه رابطه جنسی نیست، یه پروسه کامله!
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/70036" target="_blank">📅 15:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70035">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/075e2967ac.mp4?token=lJgQuTDUFDVpGxl4Sv6K5SDIe6DK-9gUVj9z_cW5LcIFtiAXR2bVLUE7nRyd0b_7YD70mcejHAk2XQKFn8kG6zHIylIU0eZiKoYTUFqFs1E_flGR00PwFY5LUTSoGyd3uYrf6O9l9GnrszyZ8T17cEMQmQVNQ2HWa1R4ayVfTSDxQ2HbR4WyDbzXquU9YFlJJoHbuJz1rx8UDPmPjU5d8Zks99rrxjmOERxNnZPk3Td1nuDF31Zw-7qEvcZASj-nVgiylAk46d9FJORNzG41a40ymtCQcP2mZGAIGjajZEfMoPBfmz3QvYHHTzgljNezq2lXUBuhgSje87p403TEKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/075e2967ac.mp4?token=lJgQuTDUFDVpGxl4Sv6K5SDIe6DK-9gUVj9z_cW5LcIFtiAXR2bVLUE7nRyd0b_7YD70mcejHAk2XQKFn8kG6zHIylIU0eZiKoYTUFqFs1E_flGR00PwFY5LUTSoGyd3uYrf6O9l9GnrszyZ8T17cEMQmQVNQ2HWa1R4ayVfTSDxQ2HbR4WyDbzXquU9YFlJJoHbuJz1rx8UDPmPjU5d8Zks99rrxjmOERxNnZPk3Td1nuDF31Zw-7qEvcZASj-nVgiylAk46d9FJORNzG41a40ymtCQcP2mZGAIGjajZEfMoPBfmz3QvYHHTzgljNezq2lXUBuhgSje87p403TEKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سومین رهبر ولایت فقیه رونمایی شد.
این زن بلند شده میگه من رهبر سوم جمهوری اسلامی هستم
😶
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/70035" target="_blank">📅 14:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70033">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfEcpiIrv9rfTJlB683NdWnyNjcmr594UKsb3LRS9KIuaZofeWs2NhAi8XYPMNg23nYYo82tt3_iYqb2YQ2q0nBFKOxM3E6S8B1MOLdrmmO4kyTjFgcYoOTwlX9XeJ-yKQS81c-FIm94x_Xeb2v00p03y43F2yhOdLsB3YeKkaDsTZDb-Kfw8hIW1HCLyAYweGyqANkpXU402FvQ4tDeE7nAm8mCz16_YSl3URAvZRayKz9ydB2l7SIby29AtQnMdl8jWBKNgfe-Xt6A2Txk9GgHxuoeiRbAt0HObfR7GtDO1HO_D4c3H0qqrSuozKa54oqnj8VAiqf6RFbt9RsJGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bba5655f5.mp4?token=S3kCJu9meim0lhAnKGslinBCtSLlF-ruVrLlN5omvQTh_xoW2d-nwdU8Up7X9QPa9GkLTX6GeQwIJh7npW085ome6cNa28yHXGoWnuyN7TqhL9vdNEAcZJP96gVxo30YIQAbDPdsTNjK-jvufyjhNW8-dzrzxbv4G9lagli1f2QZiEAd8UD4FfmkLkEfhc4wHqoLZK8n0E8SoFjfuvb0AVbvP4_i3IEjJDBo1rfB18qY7HCz-FYH-qBSx8frTEOcklee7Abdlj1HrLs_hYyo2PaR277PuU9Nsxqb9T6sh4jTh0gVKWxX9j7UBFxt1z_v96gW5nKqt_szXybzC2Z5iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bba5655f5.mp4?token=S3kCJu9meim0lhAnKGslinBCtSLlF-ruVrLlN5omvQTh_xoW2d-nwdU8Up7X9QPa9GkLTX6GeQwIJh7npW085ome6cNa28yHXGoWnuyN7TqhL9vdNEAcZJP96gVxo30YIQAbDPdsTNjK-jvufyjhNW8-dzrzxbv4G9lagli1f2QZiEAd8UD4FfmkLkEfhc4wHqoLZK8n0E8SoFjfuvb0AVbvP4_i3IEjJDBo1rfB18qY7HCz-FYH-qBSx8frTEOcklee7Abdlj1HrLs_hYyo2PaR277PuU9Nsxqb9T6sh4jTh0gVKWxX9j7UBFxt1z_v96gW5nKqt_szXybzC2Z5iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پیام‌رسان عجیب ساخته شده که کارش مثل کبوتر نامه‌بره! فاصله‌ی تو و دوستت رو اندازه می‌گیره و هر پیامی که می‌فرستی، با سرعت یه کبوتر واقعی راه می‌افته سمتش.
یعنی هرچی فاصله بیشتر باشه، باید بیشتر منتظر بمونی؛ تازه ممکنه کبوتر وسط راه گم بشه و پیامت هیچ‌وقت به مقصد نرسه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70033" target="_blank">📅 13:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70032">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇺🇸
ناو آبی‌خاکی از رده خارج‌شده USS Peleliu (LHA-5) با وزنی نزدیک به ۴۰ هزار تن در جریان رزمایش RIMPAC 2026 و در آب‌های هاوایی، در یک تمرین نظامی به‌عنوان هدف مورد اصابت تسلیحات مختلف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/70032" target="_blank">📅 12:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70030">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T5NIkGLWXGo3ZM9jHDMA0mfKg0QTzOH3Ed41QWJG-KXSgXZKNzcZzbaPQkvlYiwfqRd_doDGBcqjcc1k0N0BIPLnDi8ZR8MWdvxc_9nQ1suor3TwLbBK2WbqDXFZA50gFHfUHNhgiDS0NWlP2IconwpFjm57qjavh__U-AiB2McuEMccRoTJeA51xqSYGWNPuGF_oHIuHJMke_tExcS5sOImxgVt7Y1L_EcZ8flZaJYsSgapRPUSt5n43PucXrv5CykTif2DnGm5jqqhrFrDu0MfaDHhgRF_IGFmjNMYSEu06FCW-QWLn9DR1iMbDMtyuUMnKaPkrKw1A4KN_1U-9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uRH9Zu7lazWr-_eDImak96oeZmIMl3H3wTtWrzzGjXTkFmQXFpNuuSnEcAQ5kXvCPKtO2UZ8TmNZ_YyCezVvNapCnRXqb3QDNW3Pfezd8rgl3uLCvRUntjoRjAjODFukZdBOjgcORdQDZLTyDCs5vqqh6NthJjYHS67M-Xff_kdXcFn2o3B4MUgs5WNJMVb4C1nJVkCljtpR_5_ju1r95MCGnQOcW3MERXToLPW8LKURtXVrFYvefNBoqbc7pthG1LD3Fs2BmvXPVXAhLWSAUE73TVHnv3JElamEj8nwHFJAecQUQMsch4pGp9huQZ7ut-P_2GW8QmOJI_CaevA4wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇮🇷
شبکه خبر صداوسیما رژیم، عراقچی را خوارج نامید:
خوارج ابتدا از یاران امام علی بودن که بعدا به خاطر افراطی گری از مسیر خارج شدن و به بقیه میگفتن منحرف.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/70030" target="_blank">📅 12:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70029">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WALxYB_Xb-VzcYm0l2IFpIhrybX01IjsjXXuifmZTGwJNajCCatYbTM2x7mGiGH1ROhNQdRZr6etnBjx2b1TwgChzTBhn_j97gv8qhBnrvE7BiscywqDZO8D7JSBDDrGe4jwfw1fd1SEWweorHIEmVD3qsRi0eOFw1s4rzx5yqbxHvIYACjpTN6kVy9tg2Gcr9hXk4tSl-5BVv5t0OEKMJ_0wZbua42TtX82h6k7uCgUVwh-4kUb_UlaNv7n4F9jDwtUfEXsjKfJFYgL2WELLTnE5z7QI0-pLWDlE-UVyRvP6MxndPOizaY1DMIa7rxKYUFntooG5eCrV_0tgK5cZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا:
یک نفتکش حین عبور از تنگه هرمز هدف حملهٔ پهپادی قرار گرفت.نفتکشی که در تنگه هرمز مورد حمله قرار گرفته بود، آسیب جزئی دیده و خدمه آن سالم هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70029" target="_blank">📅 11:53 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70028">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc0cc5ccd.mp4?token=TyXL-VjyhXw59fzDE4YszEYaaDaSvEnQqdKtiXcKbM2kKUn0QB-MXwpBazkjCNeZwDUUOu2HaIthmn4wtkZfdmeTC7Xq5Va9auAfZtwG_UFokamSEUfdKOqZySZkuz7wgAMdQgEiCIvuoxEHmLJaDMCfOVv_a0gzVQswRaiF4936CkyHqLrkvLIDOBBsfftiqOyTHL8irYshtJTqCqcpv3pvBerh2sjKs3-3aMX19Yk6lPYMY7OjZ_nPa_z34YirB2dZoDbLZWkd1V6c3dp-9HyP3OKn9S4-KjZi21wZnpq4uz_ozd5p8WnSj2isxWkeS_JkISpMubyVmF7Ueaaw1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc0cc5ccd.mp4?token=TyXL-VjyhXw59fzDE4YszEYaaDaSvEnQqdKtiXcKbM2kKUn0QB-MXwpBazkjCNeZwDUUOu2HaIthmn4wtkZfdmeTC7Xq5Va9auAfZtwG_UFokamSEUfdKOqZySZkuz7wgAMdQgEiCIvuoxEHmLJaDMCfOVv_a0gzVQswRaiF4936CkyHqLrkvLIDOBBsfftiqOyTHL8irYshtJTqCqcpv3pvBerh2sjKs3-3aMX19Yk6lPYMY7OjZ_nPa_z34YirB2dZoDbLZWkd1V6c3dp-9HyP3OKn9S4-KjZi21wZnpq4uz_ozd5p8WnSj2isxWkeS_JkISpMubyVmF7Ueaaw1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تهدید نماینده مجلس به کسایی که اعتراض کرده بودن:
پدر ها مادرها بهتون میگم دخترتون پسرتون کشته بشه تقصیر ما نیست ها
هرکسی نغمه ای بزنه بیرون که به نفع دشمن هست اون کله اش نتانیاهو هستش و زیرپاش تل آویو و حکم تیرش صادر شده
تابحال با چنین صراحتی کسی باهاتون سخن نگفته بود
دوس نداریم فرزندتون کشته بشه چون جاهل و غافله و هم میهن ما هستش ولی مجبور بشیم میکشیم
🎙
📺
حالا سحر امامی مجری صداوسیما:
نه شکر خدا این تجمعات نشون داد خونواده ها فرزندانشون رو با هر رده سنی طرفدار این نظام مقدس کردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70028" target="_blank">📅 11:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70027">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
رئیس سازمان بهینه سازی:دولت برای بنزین چه برنامه‌ای دارد؟
🔴
روش اول: با قیمت فعلی تا میزان ۱۲۱ میلیون لیتر بنزین در پمپ‌بنزین‌ها توزیع شود و وقتی تمام شد، نازل‌ها خاموش شود.
🟡
روش دوم: ۱۲۱ میلیون لیتر موجود با سهمیه و بدون افزایش قیمت بین خودروها تقسیم شود و رقم مازاد بر آن با قیمت آزاد فروخته شود؛ درست همان چیزی که قرار بود در کرمان اجرا شود.
🔴
روش سوم: از ۱۲۱ میلیون‌لیتر، ۳۰ میلیون به حمل‌ونقل عمومی تخصیص داده شود و ۹۱ میلیون لیتر باقی‌مانده به‌جای خودروها به همهٔ مردم اختصاص داده شود.
🔴
از مردم هم میخوایم که نظرشونو بگن که کدومو اجرا کنیم
.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70027" target="_blank">📅 11:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70026">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مصاحبه عادل فردوسی‌پور و امیر‌ قلعه‌نویی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70026" target="_blank">📅 10:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70025">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzjAGxzD4Q1ntlj41AlSbGD9WBJwTCzGg95TjfR5tKUGmMsoSsE47zsmOR9jLRxYnW3kjfSCFjsgWX0Qs_0xe3GaOiAygA4VICb-PAYcZx3-CYBjYE5X0SAoSRzyce_SrvcQUwKT40xXWllGO931y-7IWH_NrrpXV7TqhLPorKcNBokjW-HPZ9MoW0OGTdemtUUife9XExdo9ySITLWHXhpOK_JhBfbvr0qmENdDZ6FFb5yDuSfi5yd0Zhmqhd68MOJHRoT88YFEJDlmeiEBK2EyImXIjm5XICxY72ilZmgjHvr0B-bHUqboKvoe5zTfxBiwHUcuJtok4AZ4_mTwdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
📰
وال استریت ژورنال:ایالات متحده در حال آماده‌سازی برای استقرار ناو هواپیمابر جورج واشنگتن در خاورمیانه برای جایگزینی ناو هواپیمابر آبراهام لینکلن به عنوان بخشی از برنامه قبلی جابجایی ناو هواپیمابر است.
ناو لینکلن بیش از ۲۵۰ روز است که مستقر است و ۲۰۰ روز است که در بندر پهلو نگرفته و رکورد روزهای متوالی در دریا را ثبت کرده است. استقرار غیرمعمول و طولانی مدت آن با تعداد کم پهلوگیری در بندر، قانونگذاران را بر آن داشته است تا نگرانی‌هایی را در مورد وخامت شرایط زندگی و رفاه خدمه مطرح کنند.
مقامات تأکید کردند که جابجایی ناو هواپیمابر جورج واشنگتن قبل از بروز این نگرانی‌ها برنامه‌ریزی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70025" target="_blank">📅 10:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70024">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70024" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/70024" target="_blank">📅 10:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70023">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekQINj79GHpiApPv-iMOmJyvGzFzQ2OoIuDVTNMOX7ISmOM_vRTMxW5Oyvt1LKm4Mlr7ULT47p0IoWUkYFMHqPVTD3ob_JoflQ_PWdMmZcfmj8k88dWlfLD2YgXsWEGjwtT8fzKXYMGJV_ZFMplnfk06gUZdWSEJK5GlIGlmh8IYsIeStEsZfRIVRprq2hX2ieCGGY9Svam5oPy4RmGxCJKb8JrhZ76pWXqacfCf3-H1o5SW4qerr0AoYPdKo6wVda2Up4e-uvbXu2P9XMBB5oAVu24ZJ_CEh6krJ1AY8CxEHmyTLoGWCU5RlpoloEQQBmztfJQeFnBQvJqYD9YOLA.jpg" alt="photo" loading="lazy"/></div>
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
r23
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70023" target="_blank">📅 10:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70022">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aefb92b64.mp4?token=idKtUrejV0yVfo-wXUfioBugAgg4eJQ74LM1KYxwsKlvEqMAUBnE7gL3qm0qWgSZdSuqpaa_eubYrxRaYm2QfcsqxCjsYYXV882eRxhizOpLSfLutZdnZhyWDGdz-OWAvDPzbssjhQcD79QTlpyfzA4r25lR_PxdrwcKRt8ESmak1U0YXE5i0Gg8miyuy1gPJshgriD8V6aV95OpcQT3d1Y-nGscvv0_xlJ-mVfd-0VfwdKv55hofC0JBPQprZnS_Habpl63_2RsO9L-b0wtqFZKWu3ff4lAtM9pX0XByfDZFPC5CayVeq7PpVd3TU35_k_JgsXdddHtJejeveM6qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aefb92b64.mp4?token=idKtUrejV0yVfo-wXUfioBugAgg4eJQ74LM1KYxwsKlvEqMAUBnE7gL3qm0qWgSZdSuqpaa_eubYrxRaYm2QfcsqxCjsYYXV882eRxhizOpLSfLutZdnZhyWDGdz-OWAvDPzbssjhQcD79QTlpyfzA4r25lR_PxdrwcKRt8ESmak1U0YXE5i0Gg8miyuy1gPJshgriD8V6aV95OpcQT3d1Y-nGscvv0_xlJ-mVfd-0VfwdKv55hofC0JBPQprZnS_Habpl63_2RsO9L-b0wtqFZKWu3ff4lAtM9pX0XByfDZFPC5CayVeq7PpVd3TU35_k_JgsXdddHtJejeveM6qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
اسکات بسنت، وزیر خزانه‌داری آمریکا، از اقدامات «بی‌سابقه» برای منزوی‌سازی اقتصادی ایران خبر می‌دهد:
«یک سال پیش، در ماه مارس (مارس ۲۰۲۵)، رئیس‌جمهور به من دستور داد تا سیاست "فشار حداکثری" را علیه حکومت ایران اعمال کنم و وزارت خزانه‌داری نیز چنین کرد.
همان‌طور که گفتید، ما حساب‌های بانکی، کیف پول‌های رمزارز و دارایی‌های آن‌ها در سراسر جهان را هدف قرار دادیم و جریان‌های مالی و پرداخت‌ها به رهبری، حکومت و خودِ دولت را قطع کردیم.
در نتیجه، در دسامبر سال گذشته (دسامبر ۲۰۲۵)، یکی از بزرگ‌ترین بانک‌های ایران — یا به عبارتی بزرگ‌ترین بانک آن — فروپاشید.
بانک مرکزی ناچار به چاپ پول شد و تورم عظیمی ایجاد کرد. سپس در ماه مارس یا فوریه امسال، ما جنگ نظامی (کینتیک) را آغاز کردیم. آن جنگ پس از چند هفته پایان یافت و ما از مرحله خشم و غضبِ تمام‌عیار نظامی، به سمت خشم و فشار اقتصادی حرکت کردیم.
🔴
بسنت وزیر خزانه‌داری آمریکا:
اکنون نیز به دستور رئیس‌جمهور، سطح این اقدامات را باز هم بالاتر برده‌ایم.
منتظر اعلامیه‌های بیشتر در هفته آینده باشید؛
چرا که ما قصد داریم اقداماتی را علیه این کشور به اجرا بگذاریم که در تاریخِ اعمال انزوای اقتصادی، بی‌سابقه بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70022" target="_blank">📅 10:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70021">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d5c4dd610.mp4?token=gPktNgwaJ3WjfulW-dsxVP5qgE598YF7W3HbFfI4WKGoQXP-lxyg6Av6qwx2op8liuAnTvDwqEbP5FaOkc1mJLlByW5Htde8Gzb3DGXfl9gEfx496NR_wXDF8_Os5Me5ddNRZKL98izZQGskKEKAB9VpftHOEwWkJBT_mP-t52hy50WQHwRRf6OMQyUcTRVUSugklvlJUzmext5Z-BB_JyGcTrhtY00adsw3zFW1f7ZHtlhIFIHf5ZUgdLEcZ5nsQGRXgKpDnzjuyRttcLsFtST2p165ZPJuAYrFVvIPg-jh9oGFycNjsHRsvkLbaOI8sKZKAD-IVfzail6HanOW3XUidqsqAu4CRHqLk3stcTAjCAc52HZSOy6FXJrTIzIVU6TaRq4BYQLLblfS_Lr0JFcqxylkI-2FNeSP86l0JRUp3gkkrb2H0eNC27yYkqIeuV6DzDsj5XicM95eP4uaPuxztovAIeHulct54-qmQp5XEZvKP6TW-FGcAyYowc34SLL-zBIxV8zw4LR58wLUgbXJemee0LOllTQM0njfo_2z-oigtPOOEro0_RMuge5HEtv6W69cHhidkW_DTdYo4InolZGLtN7JhIXwVaQiQG2YBQXmHWVIC6wdpWQEDHjKF1rZ4OUz5L-fqxjjlf_ef81F2am3Mks1fUa6snXcZiI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d5c4dd610.mp4?token=gPktNgwaJ3WjfulW-dsxVP5qgE598YF7W3HbFfI4WKGoQXP-lxyg6Av6qwx2op8liuAnTvDwqEbP5FaOkc1mJLlByW5Htde8Gzb3DGXfl9gEfx496NR_wXDF8_Os5Me5ddNRZKL98izZQGskKEKAB9VpftHOEwWkJBT_mP-t52hy50WQHwRRf6OMQyUcTRVUSugklvlJUzmext5Z-BB_JyGcTrhtY00adsw3zFW1f7ZHtlhIFIHf5ZUgdLEcZ5nsQGRXgKpDnzjuyRttcLsFtST2p165ZPJuAYrFVvIPg-jh9oGFycNjsHRsvkLbaOI8sKZKAD-IVfzail6HanOW3XUidqsqAu4CRHqLk3stcTAjCAc52HZSOy6FXJrTIzIVU6TaRq4BYQLLblfS_Lr0JFcqxylkI-2FNeSP86l0JRUp3gkkrb2H0eNC27yYkqIeuV6DzDsj5XicM95eP4uaPuxztovAIeHulct54-qmQp5XEZvKP6TW-FGcAyYowc34SLL-zBIxV8zw4LR58wLUgbXJemee0LOllTQM0njfo_2z-oigtPOOEro0_RMuge5HEtv6W69cHhidkW_DTdYo4InolZGLtN7JhIXwVaQiQG2YBQXmHWVIC6wdpWQEDHjKF1rZ4OUz5L-fqxjjlf_ef81F2am3Mks1fUa6snXcZiI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حرفای مجری صداوسیما درباره حکومت پهلوی:
ما از دوران پهلوی اطلاعاتی نداریم اجازه دسترسی به آرشیو هم نمیدن
چون تو اون زمان بچه بودیم تصوراتی از پهلوی داشتیم که شخص محمدرضا پهلوی فردی خنگ و ابله و دست پاچلفتی هستش
خیلی از پهلوی صحنه های اغراق شده و کاریکاتوری تو ذهن ما ساخته شده بود
این بازخوانی تاریخ نبود بلکه فحش نامه هایی بود که علیه پهلوی نوشته بودن چون ساده تر و راحت تر بود
الان وقتی ما می‌بینیم که انقد روان انگلیسی فرانسوی حرف می‌زد محمدرضا پهلوی میگیم اینی ک میگفتین خنگول این بود؟؟
اون کشورای غرب رو تهدید می‌کرد با سواد و محصل بود و روزای کاری سختی داشت
میگفتن رضا پهلوی یا همون رضا پالانی شخصی نا لایقه ولی اون هیبت داشت ابهت داشت و از کف جامعه اومده بود مردم رو می‌شناخت
کسی که دروغ مینویسه یعنی از حقیقت میترسه و متاسفانه آرشیو از پهلوی نداریم ساختن برنامه با حقیقت خیلی سخته.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70021" target="_blank">📅 09:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70020">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzWpl50c5VjtexCq79-yA2-wLeag0E2FSDoifZupF9zaUXZ2LzH3QhdpFHZgR3Qj_5DGV0Xb-iQzQfP9tIV5RCvD2RTY8EvPYnxEbB7Kb16Sirl_XAKBiSArYULFQ9fk0Me2QWAY1aKOGvXQLAEimD86LYsWPSubG0f683VFwV49mUwHSh-n1VaBaiPJulT76GvMeGFjpLeCBpoQvI1DXbM-wzmMGzCGQYMTltHf2C672wVmslKRtbaR8Vi_5czByt1VR9GFT70n5Zq5BCq_qy-4NNtlHKDNc-mso-yp3vj7nR6wK4fHnc8HC4lCszTFtzEY-q13965kq5oqerM4Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇱
شبکه ۱۳ اسرائیل: دریاسالار برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، به مقامات ارشد اسرائیلی گفته است که او پیگیر انجام حملات مجدد علیه ایران است؛ چرا که معتقد است افزایش فشار نظامی می‌تواند تهران را وادار به تغییر موضع در مذاکرات کند.
کوپر در جریان سفر آخر هفته خود به اسرائیل، خواستار حملات دوباره به زیرساخت‌های ملی ایران — از جمله تأسیسات نفت، گاز و برق — شد و اظهار داشت که ایالات متحده ممکن است در نهایت چاره‌ای جز ازسرگیری نبرد در کنار اسرائیل نداشته باشد.
موضع کوپر به ژنرال دن کین، رئیس ستاد مشترک ارتش، و همچنین دونالد ترامپ، رئیس‌جمهور، نیز منتقل شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70020" target="_blank">📅 09:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70017">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXwT3Q0J50oWN5qrvIilm9LiDC91sGJyl5GE6QVRREDn4znGvHR_1LvUdnOl2DsULWnTyzbAH9rhzq3Vw-ydvs_tgB2VGIv6hlLFUnzqmVgyba1JV5RSl3BRUBbghGQfRaBzDORNIu7-fN0I9Q9ayerRq9vQzZ2i7bBZAlzUEsIb5Q17ES4kF0DhlzECWcrJJaT8Ltnv3-jja2H-RG8RY_a9b_wm9EEOWQGSmpgqB1zpexLwAelOcKVueINk_9ECIstQTAtUcTg5djhfIuazvxs9m4eEamvC8tj0FnXeohAloEUYtNTR_dERmf7-83dSYodJweN8rJq885r6sQy9_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
محمد مخبر، دستیار رهبر و عضو مجمع تشخیص مصلحت نظام:
راهبرد قطعی رهبری مبنی بر تغییر وضعیت به حالت تهاجمی در صورت عدم تحقق شروط ایران، بی‌تردید موازنه قدرت جهانی را دگرگون خواهد کرد.
با توجه به اینکه ایالات متحده ناتوانی خود را در حفاظت از متحدانش در خلیج فارس به اثبات رسانده است، پایدارترین مسیر برای دستیابی به نظمی منطقه‌ای و جدید، پیاده‌سازی سازوکاری اقتصادی-امنیتی برای تنگه هرمز است که مستقل از تضمین‌های نظامی واشنگتن باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/70017" target="_blank">📅 01:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70016">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ed6d62f0e.mp4?token=QmPOEHaiPhoH5BIQ_8kJcBecl5mD3zrqt28mBrCSj-zE4XfwetWB-jSb7pLdJ6xEGlvAF-NJ3I-3LJBqvwC27ZBZnGWAQxsEm8XD7tkzsvJE_CCpsSMqaIIAF0yizasD5iCFN0wLW27JCDVZDLX1FS8QMc2oUf8plxLjmv3ExhUJAFrRsT7RarmyysN-mheLydeWPVKH0Nn4OG3fbGV30RnTpweHWvbB30BvXDsM455Hdawhu1LGkTp4VZh981bBRWFwyroDZT2_2ER9uKxW_oCG4NVlg6P6TFVbm5aNx7W13COx62vFz9PWX5oLJiciWkSk_KTPbzlrc-2iXue9yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ed6d62f0e.mp4?token=QmPOEHaiPhoH5BIQ_8kJcBecl5mD3zrqt28mBrCSj-zE4XfwetWB-jSb7pLdJ6xEGlvAF-NJ3I-3LJBqvwC27ZBZnGWAQxsEm8XD7tkzsvJE_CCpsSMqaIIAF0yizasD5iCFN0wLW27JCDVZDLX1FS8QMc2oUf8plxLjmv3ExhUJAFrRsT7RarmyysN-mheLydeWPVKH0Nn4OG3fbGV30RnTpweHWvbB30BvXDsM455Hdawhu1LGkTp4VZh981bBRWFwyroDZT2_2ER9uKxW_oCG4NVlg6P6TFVbm5aNx7W13COx62vFz9PWX5oLJiciWkSk_KTPbzlrc-2iXue9yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
📰
آیت‌الله ونس در گفت و گو با فاکس نیوز:
قیمت نفت امروز به شکل چشم گیری نسبت به روزهای ابتدای درگیری کاهش یافت.
ایرانی ها غیرقابل پیش بینی هستن و گاهی به تعهداتی ک میدن عمل نمیکنن.
این بحران با تقویت موضع آمریکا و با جلوگیری از دستیابی ایران به سلاح هسته ای پایان میرسه.
ثبات تنگه هرمز یعنی ثبات قیمت نفت و گاز شهروند آمریکایی.
ابزار هایی داریم که ایران رو وادار به قدم های بعدی بکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/70016" target="_blank">📅 00:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70015">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23ef24fbad.mp4?token=F1gjvOb1PBqWqeuf0ORYSI-kiINnVO0dVU-lLBNZYI0al3AqWZfZmeAtJDbhxDqhwoJR0fD_J9OuYbOv30cMkSQQgz_sfxIT-ckE_aJ1qCPUdaxc4xr79E7JXUfv1ti6sA8lH3HKYsu9zaVyCbqgSU3sbwebh7ZQV0JbtF9phEuM_UgvR9DNRk8npwsxqfV0B_CnWJLjaXsTJTDjNW0fD3HA87kwAyv0YGKNda_xPZL2UgOLW8FQJQdcYAJIGGnoQEQYusDbrkBw7506JRmrDWeNk-8jwotX13GDwPO_yEH6OACwzOSMkjE0UdwbOQKC0M_8VRpRHyXF72GHoSIy9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23ef24fbad.mp4?token=F1gjvOb1PBqWqeuf0ORYSI-kiINnVO0dVU-lLBNZYI0al3AqWZfZmeAtJDbhxDqhwoJR0fD_J9OuYbOv30cMkSQQgz_sfxIT-ckE_aJ1qCPUdaxc4xr79E7JXUfv1ti6sA8lH3HKYsu9zaVyCbqgSU3sbwebh7ZQV0JbtF9phEuM_UgvR9DNRk8npwsxqfV0B_CnWJLjaXsTJTDjNW0fD3HA87kwAyv0YGKNda_xPZL2UgOLW8FQJQdcYAJIGGnoQEQYusDbrkBw7506JRmrDWeNk-8jwotX13GDwPO_yEH6OACwzOSMkjE0UdwbOQKC0M_8VRpRHyXF72GHoSIy9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خورشیدگرفتگی دیروز از نمای کابین خلبان هواپیمای A320:
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70015" target="_blank">📅 23:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70014">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c94cf4401c.mp4?token=Lz2ETupsmhEGO6xF9ekOEuieYX0aogqlz7BFAYO_BAtVwwWAQ6BI7xsALnls22qgNt8C3i3N5qw1QZCW9WVbZnwskRZCT-negjUr3xjNzvRXKclUluSyQiObuZOBovlBAf83mZGUkxHOKYJgdWQIH1Snc1hNSvQKKxpk-7Jc5XisN2kAwWLVRxKHMYlNZKh9IxQjKiTT-AJoVrEEiYTKI5U2SHYRrE3yNG-WydVQ0qtN_moUd0hI5lGCmybgFRedfsOYk-5GD8emf74df_wZ_IxQ4Yb2d0E3tYUGKrBHgQdXsW2Bm-8qSNZMB8UcDCwC6QnjD20m-C3ooGUw2pbzEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c94cf4401c.mp4?token=Lz2ETupsmhEGO6xF9ekOEuieYX0aogqlz7BFAYO_BAtVwwWAQ6BI7xsALnls22qgNt8C3i3N5qw1QZCW9WVbZnwskRZCT-negjUr3xjNzvRXKclUluSyQiObuZOBovlBAf83mZGUkxHOKYJgdWQIH1Snc1hNSvQKKxpk-7Jc5XisN2kAwWLVRxKHMYlNZKh9IxQjKiTT-AJoVrEEiYTKI5U2SHYRrE3yNG-WydVQ0qtN_moUd0hI5lGCmybgFRedfsOYk-5GD8emf74df_wZ_IxQ4Yb2d0E3tYUGKrBHgQdXsW2Bm-8qSNZMB8UcDCwC6QnjD20m-C3ooGUw2pbzEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه وایرال شده یه زن باحجاب با یه دختر بی حجاب توی میدان علیخانی اصفهان:
زن محجبه: اینجا همون جاییه که معترضین، مامورای بدون سلاح رو به قتل رسوندن، نظرت چیه؟
دختر بی حجاب: من خودم ۱۸ و ۱۹ دی کف خیابون بودم، ولی اصلا این کارای وحشیانه رو انجام ندادم.
پهلوی مردم رو تحریک کرد بیان تو خیابون، خودش جرعت نداره تا ترکیه بیاد، چرا باید طرفدارش باشم؟
مشکل ما داخلیه، اصلا ترامپ کیه که بخواد دخالت کنه؟ اگه یه اسلحه به من بدن، با اسرائیل میجنگم.
آخرشم یه دفعه متحول شد و اشکش در اومد و باحجاب شد
🥹
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/70014" target="_blank">📅 23:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70010">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e9Kg8-TOyciDsDdH3WJf_LyPAXQvEhGD-ldvOuCvSLJmi9bvwdi2S8C-QChYOhAHCwuZTNE3_ZthUT2BDDqIo_5gX6VUmLaXqVZ-eC0tEpc-8yhlpdBQR75d4r4g-hbWqv9_2mzeTOh6l0Kaxq79HppcLv6326oZqMjOIGbePw8h5RGVyv6RJAid7J2utofgBcOPxhTz5wc7VldFSioCWOnYda9QlMVUH7pDfdjuBfSSVLPVFrM2K29F52L0NjeUj0T_4Mx_hXHJAD06ajXILdintRihWZKFgGPE3G0k_XGitCVbInqsQPBOCBcy5CZ4VHY9fNvV457y6lzY0sJKiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQ6HlSCR9xcy3AuisnO6wQgefffar51xXhQtH0uCOc4Wum8jNJSrzP7Ln2psMhF5QYQDvHt_0aC7oADPp11y1bT1KEdlL5b8ZubEIlsNr4-A_X8-L1B8covuyLB_-sP8wiZXVPAP_k4Z1nIb7i9TrISDcqxqfCaixMMn9GDTRHiNZcYcDSn5jN3p2RbPtXcmLYkC_bQzqgwPmb-kR3aB2jq1yLq8vbhPUSK6_XKbg_S1KT4oQBmk08eWavoqLU9VkBNUbNHC1j-auudtl_0oqUJrRri-kPxIQnVEAKlZ87bq_PnpZloo_jiXVXRFsZX89fMR7tSsON9wcDxMPIOpcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bzg-pkk3FHi1Y_jAtwESG0Gsj2gRUO36P6KApDd-rtWF8LtTk1J3JPz6N0OnJIho4kszTSu1ssOXRvD3Z7RaKwMC4T1Yl-gPZkk83k8hmjJAbba4xQle-LSg2q71o1Uu0IB8INUOXRcPNPOaIt8fDuYO-JFZqnojKRUGrWPTVHBhFxWd6m7LvHt714RSVQrj_LnFmGrbStJB9B4F4E1oqUrfmN-ZGUHbf-YEPon5CHLuC1VVl37NUZmck0eW-I00aivD9mwYJwtWhoCHgDT6RI4ASJS8NSzrJg7ur8TCTFuErUX35F28VPBd71OC2rWyKU7Azero91anj2w3rHc9dQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f63b04c02.mp4?token=X9L49cql34arwsE-sAE4KqHAWTDz0vjxG_8N4jpXQfwvb0_5cTfG8h4YI2kkURSTDEkcJb-Aavc9Vqxwd45dycqNTg0VshXZ9Qg1JYiFwCxMhleza_7UcXqns9quwj7zMSnk1oKYrk-IxIn_ofs7LzftJT8QC74v7-8u_tGWXFY4ET5WmVbxsl5oFXmeHxKJRq0TjpykGITdTMrKTKEPHKB0WPeaLJO2djSWXaJCi7xtL7EZY28ZHhx7wB2PjqNfLKBBOx6grbn8Fv1qomHqTpMWSh8-TOgkvKxFfCPrB_s7KrXcacPWiqzd5eJw48n3CAfHd-Tp-ix308u-2x_5Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f63b04c02.mp4?token=X9L49cql34arwsE-sAE4KqHAWTDz0vjxG_8N4jpXQfwvb0_5cTfG8h4YI2kkURSTDEkcJb-Aavc9Vqxwd45dycqNTg0VshXZ9Qg1JYiFwCxMhleza_7UcXqns9quwj7zMSnk1oKYrk-IxIn_ofs7LzftJT8QC74v7-8u_tGWXFY4ET5WmVbxsl5oFXmeHxKJRq0TjpykGITdTMrKTKEPHKB0WPeaLJO2djSWXaJCi7xtL7EZY28ZHhx7wB2PjqNfLKBBOx6grbn8Fv1qomHqTpMWSh8-TOgkvKxFfCPrB_s7KrXcacPWiqzd5eJw48n3CAfHd-Tp-ix308u-2x_5Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🔥
🔥
🔞
با انتخاب کاربران کوماتزه یا همون Comatozze اهل کشور روسیه به عنوان بهترین پورن استار برتر سال 2026 از نگاه طرفداران انتخاب شد
ویدیو های کوماتزه بر خلاف دیگر پورن استارها، فقط با همسرش ضبط می‌شه و بقولی به همه نمی‌ده!
بخشی از ویدیو های معروف کوماتزه:
🔗
پارت یک ویدیو ها
🔞
🔗
پارت دو  ویدیو ها
🔞
🔗
پارت سه ویدیو ها
🔞
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70010" target="_blank">📅 23:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70009">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e68930a72.mp4?token=hit2nC9jqx9mMSHkezDod0eVQKdDs-2BTpRO27qWMS7lel3wuZE4mDdEp4e33Zo9eAulzwdILVe2vYvIDK5VMVv-X-mUluT-7F3EJw98LZueG_G1cdJmmvzxRmYirzzIrzLpjn_KE2ZS_MP_B3Y6FkAk_B-PKaT9I1PES5i2RoJP70PaPs8jXmcavoJ1dV7RAG5ioc491ApS4IheAS2EEF1NOvH2TcK6urU8zmWXcm9OLk7IYhmAEPRe2gMhO1MV6nPx3lXWyAJn5Z5gXyNkvKex9on8vfR0RveaBbVdNYkhPmUs9WzSyXYcjTHROyCxOrAJLQ4TNE8GGur2pl0B9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e68930a72.mp4?token=hit2nC9jqx9mMSHkezDod0eVQKdDs-2BTpRO27qWMS7lel3wuZE4mDdEp4e33Zo9eAulzwdILVe2vYvIDK5VMVv-X-mUluT-7F3EJw98LZueG_G1cdJmmvzxRmYirzzIrzLpjn_KE2ZS_MP_B3Y6FkAk_B-PKaT9I1PES5i2RoJP70PaPs8jXmcavoJ1dV7RAG5ioc491ApS4IheAS2EEF1NOvH2TcK6urU8zmWXcm9OLk7IYhmAEPRe2gMhO1MV6nPx3lXWyAJn5Z5gXyNkvKex9on8vfR0RveaBbVdNYkhPmUs9WzSyXYcjTHROyCxOrAJLQ4TNE8GGur2pl0B9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه مرد روستایی در چین با استفاده از تکه‌های ضایعات فولادی و فقط با کار دست، یه بازوی مکانیکی غول‌پیکر ساخته.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70009" target="_blank">📅 22:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70008">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⏺
🇺🇸
پیت هگست، وزیر جنگ آمریکا، گزارش‌ها درباره وخامت شرایط و بروز بحران سلامت روان در ناو هواپیمابر USS Abraham Lincoln را رد کرد و گفت وضعیت موجود «کاملاً نادرست بازنمایی شده است.»
او تأکید کرد که در این ناو، «هر چیزی را که در توان داریم در اختیار خدمه قرار داده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70008" target="_blank">📅 21:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70007">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
کانال13 عبری:
برد کوپر، فرمانده سنتکام، به مقامات اسرائیلی گفته است که برای انجام حملات مجدد در داخل ایران تلاش می‌کند و معتقد است که ازسرگیری جنگ می‌تواند موضع تهران را در مذاکرات تغییر دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70007" target="_blank">📅 21:29 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
