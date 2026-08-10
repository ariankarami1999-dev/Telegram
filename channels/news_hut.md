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
<img src="https://cdn4.telesco.pe/file/hgaNMQBLNoko9mWJVnqLLwyR8FdM8ThgUeBqvkki8BOD2SOK1A5hBY-cLbCQn6kbM16gYQqJLnChyTzOav-4mxgbfIgQuS9LSBir7lNNTdVkjGZJGubKlB2cud-vIfSljPc63J7hyw_uGzFccZdWxSoCB1xIoTQySCA3sTMJk4FGTNwQ745vHQsC48b7zi2VOHdwwvAcd2hJKokgl2a7wC6p8FPg6CTp1sM1CwGUFbpZCCroX6MkPYADInKVkIqaYRznXiGXQpexTr5lnyjI437OfUYi8_vpaISchRgMMFFR-rk5xMwYz4PK76j9yUv4X6kPIyIWq1V55DX4n1Y_VA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 129K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 11:51:28</div>
<hr>

<div class="tg-post" id="msg-69834">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53aa49426e.mp4?token=En1Z16W3ceQw1DrnI_5XYBZg52qkJgoqUWqOpwsKdVYXTRSDwvtrYQjIjBNGpAoLumBFVk5RrxazBfGEi_w9ObtIQm1gX8bOE-hhc8vFBn0znyEKqL6UXl6gk1VH8gJa7Wtb2uvzYM2iYe2McpkLsPn_3plAhwYWGVMxSvFmw8mt-XEyyafzoCXuN5-WfHf0EM-GO5u-ZQ-13iVhbRlzoAHDZJWIK9JIhXAgX93qLL0fpJt5aXIH7UaTB7wfec0tjtFeDcUVYvAm0GpCSASVQyZGj9vCQtFCKka0r0OIZliYmH38sVOm-WDEOwkbfU0nHym7ASFDnUvwpdEL8V9dWTaR5otlsSZqIqAVW3pkbJoWCvXjVvaVEY1QLIorpwURr56PJY9J0i9HKoAQpHkM4zEZP5PK9uUTiFGG9jT_voiVj42KEwmO_tX3FpPlQT0tMDUswZXMOAN-iib0ye8SBjMkYm2tvxyz53B9mDpXXwa2t-k8dZRdEVMkTGQRVVx3K_2cNVyFEbZhqPlaAsr22__EcWKpmyj61iyaiP3cDYQ41ADgZbtmZ0N__IWAZvXcOzbYAVf-NQ3hXA-SyfC4P6PKq44WxWkPPVJj-JoADfMcLeqWqA4qgIAfDhOWCN-e3HdiO4xe2SJhzP4q7fyo4Wj_ue11kKdAZSDgzSNc_HM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53aa49426e.mp4?token=En1Z16W3ceQw1DrnI_5XYBZg52qkJgoqUWqOpwsKdVYXTRSDwvtrYQjIjBNGpAoLumBFVk5RrxazBfGEi_w9ObtIQm1gX8bOE-hhc8vFBn0znyEKqL6UXl6gk1VH8gJa7Wtb2uvzYM2iYe2McpkLsPn_3plAhwYWGVMxSvFmw8mt-XEyyafzoCXuN5-WfHf0EM-GO5u-ZQ-13iVhbRlzoAHDZJWIK9JIhXAgX93qLL0fpJt5aXIH7UaTB7wfec0tjtFeDcUVYvAm0GpCSASVQyZGj9vCQtFCKka0r0OIZliYmH38sVOm-WDEOwkbfU0nHym7ASFDnUvwpdEL8V9dWTaR5otlsSZqIqAVW3pkbJoWCvXjVvaVEY1QLIorpwURr56PJY9J0i9HKoAQpHkM4zEZP5PK9uUTiFGG9jT_voiVj42KEwmO_tX3FpPlQT0tMDUswZXMOAN-iib0ye8SBjMkYm2tvxyz53B9mDpXXwa2t-k8dZRdEVMkTGQRVVx3K_2cNVyFEbZhqPlaAsr22__EcWKpmyj61iyaiP3cDYQ41ADgZbtmZ0N__IWAZvXcOzbYAVf-NQ3hXA-SyfC4P6PKq44WxWkPPVJj-JoADfMcLeqWqA4qgIAfDhOWCN-e3HdiO4xe2SJhzP4q7fyo4Wj_ue11kKdAZSDgzSNc_HM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایشون هم اینطوری انتقام قتل حمیدرضا رجب‌زاده رو گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/news_hut/69834" target="_blank">📅 11:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69833">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=gMNSLpPY5lZzOYBt8Tmes5GaczRNVGQfCsEjvuiv2pWALv0_Ph4KAgmkUO50kWF0ZKGG5uHIZdNNXJB9rROrvSU8nvZVhoujOi1Q1-KcIU0dz3pGBmTDPq5ngS3jACEuLSmlXNNq_X95SXm9RScBWyZiELRZNjKkq-Fvb5BM6AhAmrEx8jfBesRsHeVsME9NzNMK7n9t_CTcLPCHQC49xPIUUD80gpyAgB_k8Awsj2wcVE1pOr4qj0xEPBYK7_1NvMiWlp4N9AfdeLNDf0hFF3gMozm3Xvbbg0t4nACwo5s1fCsOknKr4e7sGm0dEu6uTfKhZ7Cc-L1kfs9nvi2Sfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=gMNSLpPY5lZzOYBt8Tmes5GaczRNVGQfCsEjvuiv2pWALv0_Ph4KAgmkUO50kWF0ZKGG5uHIZdNNXJB9rROrvSU8nvZVhoujOi1Q1-KcIU0dz3pGBmTDPq5ngS3jACEuLSmlXNNq_X95SXm9RScBWyZiELRZNjKkq-Fvb5BM6AhAmrEx8jfBesRsHeVsME9NzNMK7n9t_CTcLPCHQC49xPIUUD80gpyAgB_k8Awsj2wcVE1pOr4qj0xEPBYK7_1NvMiWlp4N9AfdeLNDf0hFF3gMozm3Xvbbg0t4nACwo5s1fCsOknKr4e7sGm0dEu6uTfKhZ7Cc-L1kfs9nvi2Sfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دریک، از بزرگترین خواننده‌های دنیا؛
با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]
وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد
@News_Hut</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/news_hut/69833" target="_blank">📅 11:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69831">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d3c25ee1.mp4?token=eTViVL0FvSG-oafPDDr3TZqDiarBMuH4tXJM5iHd77x_ixPNfRablcvBuXP5RJ9uEmFK4mc1WEVohaVuU61WUip03atvR5LCFt1XTEuJA6mLzVtbSzM7FZfAofdtwKUZDBupzBEif90uWmwvY7tFHkiX8VvcUty5BREj9MNwqz2vXxbWOikebFQXo-ghFtu-DIuvcb3Osqy28659NLVMXX7KB05jg8oVqBBRyXf4MylkFQFsR9abg-I41sycivQlTHxDmwkR1-YaJa9uy0C97SZS6hAd7smvOcWoRyegTK3yTo727_RasDA3Xlvm1i9aqJJzTKX7GBUKrUVDz5Ol82A-dNyZtPqc-9rHFoh02DM3H4XeosEwMyFa8SBynNySGpLFMlph3iGAAsCk98cufxHBoCWQdMuCuI8E9mUjjsVbsYydLYu1Ez3M4PTeWMZwyElYGBzmo0igytQeZCKTrFgQRRusUryWmJbjobf6MBRChLnP6d7_DBvpQaHfUS0X4DMfC-Q6l-k00V9S6TvRdv44CiWsLBCpO_lDIbJEzmdPNXy9Lgc49QjOsLPANVAM6K2xQBkBE37vZafuTGZC4JcdRacfG51dwbAGeSKwCWAq3EPoIujIcpnhGcyH1hVekMwVD9pwLr4yeBpPxCkSvgW9oYVaGkCoi-dPttqritE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d3c25ee1.mp4?token=eTViVL0FvSG-oafPDDr3TZqDiarBMuH4tXJM5iHd77x_ixPNfRablcvBuXP5RJ9uEmFK4mc1WEVohaVuU61WUip03atvR5LCFt1XTEuJA6mLzVtbSzM7FZfAofdtwKUZDBupzBEif90uWmwvY7tFHkiX8VvcUty5BREj9MNwqz2vXxbWOikebFQXo-ghFtu-DIuvcb3Osqy28659NLVMXX7KB05jg8oVqBBRyXf4MylkFQFsR9abg-I41sycivQlTHxDmwkR1-YaJa9uy0C97SZS6hAd7smvOcWoRyegTK3yTo727_RasDA3Xlvm1i9aqJJzTKX7GBUKrUVDz5Ol82A-dNyZtPqc-9rHFoh02DM3H4XeosEwMyFa8SBynNySGpLFMlph3iGAAsCk98cufxHBoCWQdMuCuI8E9mUjjsVbsYydLYu1Ez3M4PTeWMZwyElYGBzmo0igytQeZCKTrFgQRRusUryWmJbjobf6MBRChLnP6d7_DBvpQaHfUS0X4DMfC-Q6l-k00V9S6TvRdv44CiWsLBCpO_lDIbJEzmdPNXy9Lgc49QjOsLPANVAM6K2xQBkBE37vZafuTGZC4JcdRacfG51dwbAGeSKwCWAq3EPoIujIcpnhGcyH1hVekMwVD9pwLr4yeBpPxCkSvgW9oYVaGkCoi-dPttqritE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی شبانه به مجموعه‌ای از اهداف در سراسر روسیه و سرزمین‌های اشغالی حمله کردند.
پهپادها مرکز خرید گالاکتیکا در ماکی‌یوکا، که قبلاً مرکز منطقه‌ای بود و در سال ۲۰۱۴ توسط نیروهای روسی تصرف شده بود، را به آتش کشیدند.
آنها همچنین پالایشگاه نفت در نیژنکامسک، تاتارستان را هدف قرار دادند، در حالی که روسیه ادعا کرد ۱۵ پهپاد در نزدیکی مسکو سرنگون شده و عملیات فرودگاه را مختل کرده است.
طبق گزارش‌ها، حملات پهپادی باعث قطع گسترده برق در ملیتوپول، بردیانسک و دونتسک شده است، در حالی که انفجارها و آتش‌سوزی‌هایی در سواستوپول و کرچ گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/news_hut/69831" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69830">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69830" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/news_hut/69830" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69829">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=rwgRWaNaGx4XA7ZfyAOTy0V1jNGwpH4jolTzD4puVq2Kc42eKHwEi-x5eeSlIUqoZ961WDwIWG8KdTwM4NI9E0p7118NzDFlMca0-Su3FZv2d80DNAY92u-vhqpa03Xa33DPMaMOy-KR8Dmf1kenZRDSecSUnjBcwBTuBjWYJSsMgrrfytM369HCpcUdIQ0JfpOHh6QNKeWKgz0iVMPiPa53rXZ3mb5IMEixokJjCZtFOoPOaJK9BPQTimnoKrhoLK0CcVCg6GOV3BHQpJ2YgGKEDWQzm_L0Zp9Sdx9I8ovnudDrpvHMchDeukSUF74o4eFKkiqqN5_QnSXkYu4Aqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=rwgRWaNaGx4XA7ZfyAOTy0V1jNGwpH4jolTzD4puVq2Kc42eKHwEi-x5eeSlIUqoZ961WDwIWG8KdTwM4NI9E0p7118NzDFlMca0-Su3FZv2d80DNAY92u-vhqpa03Xa33DPMaMOy-KR8Dmf1kenZRDSecSUnjBcwBTuBjWYJSsMgrrfytM369HCpcUdIQ0JfpOHh6QNKeWKgz0iVMPiPa53rXZ3mb5IMEixokJjCZtFOoPOaJK9BPQTimnoKrhoLK0CcVCg6GOV3BHQpJ2YgGKEDWQzm_L0Zp9Sdx9I8ovnudDrpvHMchDeukSUF74o4eFKkiqqN5_QnSXkYu4Aqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r19
@betinjabet</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/news_hut/69829" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69827">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOrIUiCg1IO2cbdmPEolU6nYYTbKRy_ytvK9qaCKhMRULf0_wxPII4bmsWOLGRP0pTTtxdYMO_ESxJjYyzluaWng4lT63neKx4JXbznKLLQ2prYBLS1JqePUehNpt5YNcF-fES_InaEFKFm1eO6i8rEGqXKBpJRm2v0wkPe6cuaCvBTEkwLzwneP_dDON2FvrRJU9Yse-SaBbLcf3nkqyB6KgHrVKnHQj7beuvRz9XKk8WWf6E6yAlQsPSfPk7bkJSJLy8RwWu4bbXiEaOWP_vGacVaQ2jzh-yB9VEz0pBCMX_sBHo3mhCKKB7MZd09STzCdaSEj28Pm9ClUDZ3ikA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
شرکت آمریکایی BlackSea از پرتاب یک پهپاد FPV از روی قایق بدون‌سرنشین GARC خود رونمایی کرد
؛
این شرکت اعلام کرده است که با استفاده از تجربیات به‌دست‌آمده از جنگ، استفاده از پهپادهای FPV هدایت‌شونده با فیبر نوری را پیشنهاد می‌کند.
محفظه‌های پرتاب این سامانه قادر به حمل پهپادهای FPV در اندازه‌های ۵، ۷ و ۱۰ اینچی هستند؛ پهپادهایی که از نمونه‌های FPV مورد استفاده فعلی روسیه و اوکراین کوچک‌ترند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/news_hut/69827" target="_blank">📅 10:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69826">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c36a2172.mp4?token=gbg9WJT6sz1_2aixdFoa4iRrvC3lJOjc8AqYWL_NMPmecZo1UpSl1TXmjRXVxYPqfXmixKG-sMVTtIdIoNRYwBq7a1p0Ua4gpySrTZjeYEiREHw6sPXsd9B1KoZxd5TZCZxDO7Ei-orWNogq4WMjPgXmRvHZeKRwBf4R8yyTfyVwaoNThNk9Upmdl-UgTDdbtXndL3TArNZMl6ldXykD2A2JW8SEgAh3x00nqvqz_FgxSQUBGyhm2w8-g7WKChfnIpbOvXlzwZtVjYGE5cfRlHDNH6HIX3RJkB1BgZaLzDwATofiQEKkPLBHbe9luAv-FsBmyvDmgywXPTncD2VOrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c36a2172.mp4?token=gbg9WJT6sz1_2aixdFoa4iRrvC3lJOjc8AqYWL_NMPmecZo1UpSl1TXmjRXVxYPqfXmixKG-sMVTtIdIoNRYwBq7a1p0Ua4gpySrTZjeYEiREHw6sPXsd9B1KoZxd5TZCZxDO7Ei-orWNogq4WMjPgXmRvHZeKRwBf4R8yyTfyVwaoNThNk9Upmdl-UgTDdbtXndL3TArNZMl6ldXykD2A2JW8SEgAh3x00nqvqz_FgxSQUBGyhm2w8-g7WKChfnIpbOvXlzwZtVjYGE5cfRlHDNH6HIX3RJkB1BgZaLzDwATofiQEKkPLBHbe9luAv-FsBmyvDmgywXPTncD2VOrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جهانگیر، سخنگوی قوه قضائیه:
آخوند خرازی، بابت صحبتاش تحت تعقیب قرار گرفته و به دادگاه ویژه روحانیت احضار شده.
@News_Hut</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/news_hut/69826" target="_blank">📅 10:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69825">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🟡
📰
مراد ویسی تحلیلگر ارشد اینترنشنال: «جنگ بزرگ در خاورمیانه، برای سرنگونی جمهوری اسلامی است.»
⏺
پرسش این نیست که کدام زودتر می‌رسد؛ پاسخ روشن است:
جمهوری اسلامی سرنگون شود، مردم ایران به یک حکومت عادی می‌رسند.
جمهوری اسلامی سرنگون شود، نیابتی‌ها خشک می‌شوند.
صدام رفت، یک کانون تهدید در خلیج فارس از بین رفت — کانون دوم هنوز باقی است.
خلیج فارس می‌شود منطقه‌ی صلح، ثبات و توسعه؛ چون امارات، قطر و عربستان دنبال توسعه‌اند و ما هم دنبال جبران خرابی‌های جمهوری اسلامی.
ثبات منطقه از تهران آغاز می‌شود، نه از میز مذاکره.
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/69825" target="_blank">📅 09:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69824">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd241cc6.mp4?token=IDy_MP9sjUkJI2Mu9ve4Ihy1cIiKO8hymb2A9j8IaclwzkEtc_Pr9iceBv6zS4KHvEOUeQFpjTUWwgp7kQzuHLHZgp13Pqm4KeDt7tmSKr7BYNc-dlIUXihBUgeb0yrjeMOPMO5C7ZK8vEh-_-gDSeacwPgMtdGiHiCm9t2ftpUQzdL5Z3WTtLWWEVKiowWdduMtMTw2CdGb8Jmfir_gL9Yktclgr9Gs5KKjaisUNxf9cDEsK4qCmlxQevcDWDDegBd0a2cPyNs0NL3TAfLc7PqvTzNCZgTcvZSXRMT-CZ4td_CQJgcJ7x3Gq-OPYJiyJLMlRszwvjP6q4Cpd2BvVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd241cc6.mp4?token=IDy_MP9sjUkJI2Mu9ve4Ihy1cIiKO8hymb2A9j8IaclwzkEtc_Pr9iceBv6zS4KHvEOUeQFpjTUWwgp7kQzuHLHZgp13Pqm4KeDt7tmSKr7BYNc-dlIUXihBUgeb0yrjeMOPMO5C7ZK8vEh-_-gDSeacwPgMtdGiHiCm9t2ftpUQzdL5Z3WTtLWWEVKiowWdduMtMTw2CdGb8Jmfir_gL9Yktclgr9Gs5KKjaisUNxf9cDEsK4qCmlxQevcDWDDegBd0a2cPyNs0NL3TAfLc7PqvTzNCZgTcvZSXRMT-CZ4td_CQJgcJ7x3Gq-OPYJiyJLMlRszwvjP6q4Cpd2BvVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یکی از نفس‌گیرترین ویدیو های منتشر شده از جنگ؛لحظه بمباران شریعتی تهران!
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/69824" target="_blank">📅 09:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69823">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69823" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#بازی_پولساز
⚠️
🔥
بلک کارت جدید ترین بازی معروف جهانی هست که فقط کافیه یکمی باهوش باشی تا حریفات رو شکست بدی
👌🏼</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/69823" target="_blank">📅 02:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69822">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6c003ee1.mp4?token=X-4qSlha0JrFoPLquYa39K20mwOW97yyB85QAa25Lc4TmjM0gT680SUEL0SC1-DBnBTcl86huza6QWBPaIAaMqYx_FcemPd1spNW9SSKsTNz_cxKHLdx8wGA6KBOjcUjaEOaGZzrM8xezzU29xeKcYPvTnmMwqqzFAp9qFJKtDu95MNT3bAU6dEt1ed23PJ1e2Ai-B94IDbIcUKxwnRQs5LOvOnh5m2itRWBKAZ7zxLEKtQkLxmYl_X7gIyVMq1cjD-l5PHf5vE8MEUDmhmKZp48dv682KHA3Wm6PV_PhB1cabkuOxI7xEXraiMMZNKI3l9Udw00NLS-XS5aUiMA5DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6c003ee1.mp4?token=X-4qSlha0JrFoPLquYa39K20mwOW97yyB85QAa25Lc4TmjM0gT680SUEL0SC1-DBnBTcl86huza6QWBPaIAaMqYx_FcemPd1spNW9SSKsTNz_cxKHLdx8wGA6KBOjcUjaEOaGZzrM8xezzU29xeKcYPvTnmMwqqzFAp9qFJKtDu95MNT3bAU6dEt1ed23PJ1e2Ai-B94IDbIcUKxwnRQs5LOvOnh5m2itRWBKAZ7zxLEKtQkLxmYl_X7gIyVMq1cjD-l5PHf5vE8MEUDmhmKZp48dv682KHA3Wm6PV_PhB1cabkuOxI7xEXraiMMZNKI3l9Udw00NLS-XS5aUiMA5DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😯
اگر هوشت بالاست
🗼
:
❌
👍
این ‌ویدیو‌ آموزشی رو‌ ببین و با ‌استفاده از هوش بالایی که داری پول در بیار.
🟢
بازی خیلی حرفه ای و‌
#پولساز
رو‌ از این ویدیو یاد بگیر
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
a18
@betinjabet</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/69822" target="_blank">📅 02:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69821">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:  اگه ایران از این به بعد به هر کشتی‌ ای توی تنگه هرمز شلیک کنه، فرقی هم نداره با موشک، پهپاد، راکت یا هر سلاح دیگه‌ای باشه، آمریکا در جوابش یه پل یا نیروگاه برق ایران رو میزنه حتی اگه نزدیک تهران یا داخل خود تهران باشه.  @News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/69821" target="_blank">📅 01:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69819">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAalZDk8Wivp1rb54E8kcJ5VThVJ22LOTeEUOU6S6b3hnxtsvmSn_B3-2ZTka-p_FWhjDAN2Kzgdy1T-2gmjvj_nM-MD1RZ3prV_JkuDQ2LpIU7g5QK648_O1TWbn4QeQeJuKXPEqgTnd19gsyKdoDHyp8zPWZyVZ_c1VI9BKpCEfSWslM2OmHvurPdkyKBtkhcqGSbWr3OzXfTHv6LAYhX9NXR46g7266VYxYsGQ6K10fkyaey8Pv5gGYmR1K7_obWoK70-xuzLr9jdJdHeHcVxQHXwVK-cfHGRS-E0b_Aw2oG4y7Mg1v-zlKrM5QARaQ5LjU3XMdDMs8ynS0J65A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94eb35c039.mp4?token=mW-Ug_57wgUgDXLmyxDw5O-XYxVhA7S-igS2Uw8G5blNg6qF1slO0nlysQkLM1dBIBED87BiUSMu4HpQDaK93Ht1ITqiREbpCcbcWciFlpdVdpjM6Tvq6mf9bsllZOcuz3ZtEqx9ABTDUFH1WXJ40N-AlHbFSpA3f6EoOS0bson78KFXYO4vbCn6hFptWkKq60cfyhUtt5CggELQnGwvhkmpcipRbChjSjhAbgNThtP4sRmPL8Pf7p8FHV4D0xz7jcp3zj6X44dSrRItBrfUSn9MIsK1eDSLqAooeiOTLvMPWcX4nlz94x5C4bwfvxXIj0QN2ktWGIvsZJejn336FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94eb35c039.mp4?token=mW-Ug_57wgUgDXLmyxDw5O-XYxVhA7S-igS2Uw8G5blNg6qF1slO0nlysQkLM1dBIBED87BiUSMu4HpQDaK93Ht1ITqiREbpCcbcWciFlpdVdpjM6Tvq6mf9bsllZOcuz3ZtEqx9ABTDUFH1WXJ40N-AlHbFSpA3f6EoOS0bson78KFXYO4vbCn6hFptWkKq60cfyhUtt5CggELQnGwvhkmpcipRbChjSjhAbgNThtP4sRmPL8Pf7p8FHV4D0xz7jcp3zj6X44dSrRItBrfUSn9MIsK1eDSLqAooeiOTLvMPWcX4nlz94x5C4bwfvxXIj0QN2ktWGIvsZJejn336FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇨🇳
🇸🇦
یک پهباد ساخت چین متعلق به نیروی هوایی عربستان سعودی در آسمان جنوب کشور سرنگون شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69819" target="_blank">📅 01:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69818">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLT9nOrd8oXIU_faWtHmZjybtQspThvfagr1bJ6Mz7vLPjD22JbPLGvocevoaJIwo_o9_4A0LmWPRuG93DXuxQQ99b_uyNTKb27rGQU_8KszyHYoFcO0Mll5MMpWtIp_xPxHpOqVCb1oQrBrJeeixFgbTu-misf0uZHupwa7ofJHeWr5PiaWBkHkLqVs6L5V_fD6xIRSID2cO7_ls0CRWeoO3PLhGDmkiv9N5pr3R1tpXp4U6rGV8-WaT6AC88dP6WDeu79DkgaA_7b3LYPleBWoEjNCSZP9I05sUkqvzuM7navhV0YnRFDRwLKfa0CmGyGC27qBxKu0VZu5eX0QGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در تروث سوشال:
51سال رفتار نامناسب!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69818" target="_blank">📅 00:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69817">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dbf391292.mp4?token=bfCMG8yW2sTsgJURA_fWZSbxtIbSOY2gOvciXoy1ijZKWHga1b57d2qRVJj3VI1_8p3eWvUxmwyOrjGWsTi87A7BRBK4dh6HpvHDTc3VnHSLYwmajVssr3-ivGaJxmrB0-eA6UqQ7061WiycMrKXcNT8fjc8eaI-nQLs3lqIdIbKpt2eU7EkBpouU7JaVqGgX6pD1M7BnslhjhHanHuy89u_1-6ZaOARw1CbvvFLRLBLEE_7lUGE7OgTJE7qK8_l4ME44Y_mMCmhtJgzcOdm2avbXucw6Fs8PNwJnRplJcAmervmLZxNDCxoOOKmVpSSiegl7aq2KU1yIVgNGoeMiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dbf391292.mp4?token=bfCMG8yW2sTsgJURA_fWZSbxtIbSOY2gOvciXoy1ijZKWHga1b57d2qRVJj3VI1_8p3eWvUxmwyOrjGWsTi87A7BRBK4dh6HpvHDTc3VnHSLYwmajVssr3-ivGaJxmrB0-eA6UqQ7061WiycMrKXcNT8fjc8eaI-nQLs3lqIdIbKpt2eU7EkBpouU7JaVqGgX6pD1M7BnslhjhHanHuy89u_1-6ZaOARw1CbvvFLRLBLEE_7lUGE7OgTJE7qK8_l4ME44Y_mMCmhtJgzcOdm2avbXucw6Fs8PNwJnRplJcAmervmLZxNDCxoOOKmVpSSiegl7aq2KU1yIVgNGoeMiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
آتش‌سوزی یک کشتی در پی حمله سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69817" target="_blank">📅 00:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69816">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه‌پاسدارن یک کشتی را در تنگه هرمز هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69816" target="_blank">📅 00:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69815">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec1565ac0.mp4?token=jHZN-e5Ju2bc8KZ04rUEH7DfSIT_gGf1QZ9vdY_FvTsl0kPcNDBhq0SHBfJdftjclz5_wZD3t_2oR4493RGl1KbJtTCKEa8KiZkkmHY71CrtiUi-eTzkCr0h83yJY1kA1I1CCAh4q99lIUX3UgnJkx-8DRMsmCBHwAB1GYNgIijyGsLlue6CP8htGoiSUwvgiXm9FpsjHIGIEluCsaGRlzRbRoOl7ACgRBLM3xIgh9RdGRJFHRy5MbI7oaPM8QpB_g885ANHJozWhnx-RKNLfKhwhyoiVIHrMDbf0tVOwdowzvE6TVXD8t_gb7RXHnAd0jJ6wdlRfVAUCQ1QEXPJsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec1565ac0.mp4?token=jHZN-e5Ju2bc8KZ04rUEH7DfSIT_gGf1QZ9vdY_FvTsl0kPcNDBhq0SHBfJdftjclz5_wZD3t_2oR4493RGl1KbJtTCKEa8KiZkkmHY71CrtiUi-eTzkCr0h83yJY1kA1I1CCAh4q99lIUX3UgnJkx-8DRMsmCBHwAB1GYNgIijyGsLlue6CP8htGoiSUwvgiXm9FpsjHIGIEluCsaGRlzRbRoOl7ACgRBLM3xIgh9RdGRJFHRy5MbI7oaPM8QpB_g885ANHJozWhnx-RKNLfKhwhyoiVIHrMDbf0tVOwdowzvE6TVXD8t_gb7RXHnAd0jJ6wdlRfVAUCQ1QEXPJsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال شده از یه پسرِ جوون تو تجمعات شبانه:
به ابالفضل راضی‌ام جنگ زمینی‌ بشه، یه تنه 500 نفرشون رو حریفم!
ایشالا روزی بشه مکه و فلسطین رو آزاد کنیم.
ایشالا روزی برسه آمریکا رو نابود کنیم و تو کاخ سفید نماز بخونیم.
نیاز به بسیجی‌ها نیست همین بچه‌لات‌ها اسرائیل رو میگیرین داداش...
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69815" target="_blank">📅 23:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69814">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b396273688.mp4?token=jmFmCWdcFVtwtiIUSxeffNfjPqKpuZ8IA1HyfWUMtgbR1_YeY9jqMjdYcuJt6d5NZZopNzabRLY6BTdgMyCdKpf4a8wT_m_fMzVtuYiaP2OK2buxL12VkLWAX6Hz2MHpDnd1YfUjl8C3x63r_uyx_Mvl4owhkysZ_2ZrksFzAXzKOVePPcuOElCso7czis6dt3RhipEj30OsZQvJKnKwbZIKCSzNWg1VdHShvVad4oNjhLsDcr87oJTI3-vfv2PkfvKHpTJhom4bG3mTo_naQCJKvmGOdK4j0WOMcYAEaxEJbPIwnZGdQSQrb6Y14dRtkd3houmsVCPKz7YJrZAidgivB0W60gy8TW4wxsJt4QFMX0qQGpCL2vDvqJT5-fCPqCVT7qKBiblU7L465vH957DOR5QUYMVOzUYYWX2r-aczAH0N5lJKOd_GD7fnF3yEEwJ0tVSBQHNeHk7mjqWaqMm160IRVjKoHQXJeKdXgpd4WqURjoifhZDrjB-gy_ZHUKD3TN2Ov6rG9hTTC4LW5RSCsBwyRgeQcF63uIroIfltJeM3iTrHPk5kV8qYz17TH_HzFVIRHS2n5JuexwfOVBwrdDTUgv4Z33i_JD8OwbHaAeKqKB3vNYKRgLCWVEb5bkQ5u8tDpKPP_pzl94bzvxKi5isNF9R3QCoalfOGrQ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b396273688.mp4?token=jmFmCWdcFVtwtiIUSxeffNfjPqKpuZ8IA1HyfWUMtgbR1_YeY9jqMjdYcuJt6d5NZZopNzabRLY6BTdgMyCdKpf4a8wT_m_fMzVtuYiaP2OK2buxL12VkLWAX6Hz2MHpDnd1YfUjl8C3x63r_uyx_Mvl4owhkysZ_2ZrksFzAXzKOVePPcuOElCso7czis6dt3RhipEj30OsZQvJKnKwbZIKCSzNWg1VdHShvVad4oNjhLsDcr87oJTI3-vfv2PkfvKHpTJhom4bG3mTo_naQCJKvmGOdK4j0WOMcYAEaxEJbPIwnZGdQSQrb6Y14dRtkd3houmsVCPKz7YJrZAidgivB0W60gy8TW4wxsJt4QFMX0qQGpCL2vDvqJT5-fCPqCVT7qKBiblU7L465vH957DOR5QUYMVOzUYYWX2r-aczAH0N5lJKOd_GD7fnF3yEEwJ0tVSBQHNeHk7mjqWaqMm160IRVjKoHQXJeKdXgpd4WqURjoifhZDrjB-gy_ZHUKD3TN2Ov6rG9hTTC4LW5RSCsBwyRgeQcF63uIroIfltJeM3iTrHPk5kV8qYz17TH_HzFVIRHS2n5JuexwfOVBwrdDTUgv4Z33i_JD8OwbHaAeKqKB3vNYKRgLCWVEb5bkQ5u8tDpKPP_pzl94bzvxKi5isNF9R3QCoalfOGrQ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خرازی:
این کلیپ ها جعلی و هوش مصنوعی است؛
من این حرف‌ها را نزدم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69814" target="_blank">📅 23:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69812">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1fdc25902c.mp4?token=QqG_6UlDzGCbV-lHWzeJS_BycqdVSePLrPt2thJZH42ndtAleMmod2G9FEPooDHgKoki_6eaWW62EXCJeO8ax-ljxrkpe7M3YyDGTKjXP-kU6N5PYDqa_71MLCmDXNQTwZoGjBu8Kg1snPdg-3wDPYE7PZb6rjsy9IHmG768s_P_3rzLgQgdykTyYaPL3BfbTCrDYOU7o_bKVDNQ2hA6XzNmz1noBasOZGQz3I2fLoLOQ6MIYu3T_35rCP7xTMbdy_gtCuwVxSN21VKRCvsEO65occzbyx8Rzwo1ULiP48nHMDmfVaaRN8BA0ipcJ7GSv7YS1WrRze2hzTyR47cHBg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1fdc25902c.mp4?token=QqG_6UlDzGCbV-lHWzeJS_BycqdVSePLrPt2thJZH42ndtAleMmod2G9FEPooDHgKoki_6eaWW62EXCJeO8ax-ljxrkpe7M3YyDGTKjXP-kU6N5PYDqa_71MLCmDXNQTwZoGjBu8Kg1snPdg-3wDPYE7PZb6rjsy9IHmG768s_P_3rzLgQgdykTyYaPL3BfbTCrDYOU7o_bKVDNQ2hA6XzNmz1noBasOZGQz3I2fLoLOQ6MIYu3T_35rCP7xTMbdy_gtCuwVxSN21VKRCvsEO65occzbyx8Rzwo1ULiP48nHMDmfVaaRN8BA0ipcJ7GSv7YS1WrRze2hzTyR47cHBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه ماجرای عجیب و تلخ که زندگی یه ورزشکار رو زیر و رو کرده
این بنده‌خدا یه ورزشکار ۱۳۰ کیلویی بوده، پرس سینه می‌زده و از بهترین راننده‌های جرثقیل هم بوده؛ ولی یه ماجرای مهریه کل زندگیشو زیر و رو کرده...
همسرش مهریه رو می‌ذاره اجرا و حکم جلبش صادر میشه. وقتی مأمور برای دستگیریش میاد، فرار می‌کنه و مأمور هم به کمرش شلیک می‌کنه؛ گلوله باعث میشه قطع نخاع بشه.
حالا با وثیقه آزاده، ولی هنوز داستان تموم نشده؛ همسرش گفته فقط یه هفته وقت داری، وگرنه دوباره باید بری زندان!
از یه آدم سالم و ورزشکار، رسیده به این وضعیت...
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69812" target="_blank">📅 22:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69811">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🇺🇸
وقوع یک حادثه امنیتی در نزدیکی باشگاه گلف ترامپ در شهر بیدمینستر، ایالت نیوجرسی؛
فرماندهی دفاع هوافضای آمریکای شمالی (NORAD) دو فروند پهپاد را که حریم هوایی محدودشده بر فراز بد‌مینستر، نیوجرسی (Bedminster, NJ) در نزدیکی باشگاه گلف ترامپ را نقض کرده بودند، رهگیری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69811" target="_blank">📅 22:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69810">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgwFKpIHtlzeXzT82CB7DZdji1huTDYpsxxZmZBH_FGIc488NWWvwRmOLYQGa2JSs1qeGPtsg80yXolxt181SuLJBFRUdUJBtICug_7ZNr0zKa5pgwOxiHJaAFcfZ2lrxw7RZ5se6I2KKpzpGP53pd1RDq7dfx7yGTMn_QXwIDbkKqoGVVFRJdeFqaUMlVMBupAwYd7NEERM1ksjmflyATiRBjN-o79VtWccNEZ4KeA6YKOo25CzhAEcnyRej1-xftNtYewjSFK3_YdVphqdaNqj41PCQtvX6IUslsW2Fuj9TuwLfQ06TCJvXMPPLOYXuUlG_qxeNhRqRYekMugb3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
با حکم مسعود پزشکیان محسن رضایی رسما دبیرکل شورای عالی امنیت ملی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69810" target="_blank">📅 21:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69809">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
یه فلسطینی به زور بچه شو میفرسته جلو سربازای اسرائیلی، بهشون میگه شلیک کنید بهش!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69809" target="_blank">📅 21:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69808">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmncPrG5mHce104jBLxS2X2l5oIom3p0Hu7ASxwvdAAF5N4LpYFxmJSbNDafS1a64wD_Nj_VAgFKGvGBZG12ekidRLgn7YT47M25hjkDN2xliKYm9HpOtvf8BdA7wAKzsN5dQNsZdm0hhVwJ1BjjTW2Og3WscEvX5nBBrhe5PLIRR1kK9GQArFubb7dtp6XaebkCcgqQzIJ7zppMYwYnZNZdksoINnInf0ovgukQY-tZ2y3jJ4nkb4masltZ8ovKWVhshmBwXeUaYPdVydpqgWk_npExatlk6fumBfGhFaBRsGx4i8-m5y3Poy2obC6Yz8IkRfw4qL4CEApqNLnGzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
🇺🇸
اکسیوس به نقل از ترامپ:
ایالات متحده در رابطه با ایران «بی‌سروصدا» عمل می‌کند، که نشان می‌دهد واشنگتن فعلاً از اقدام نظامی عمده جدید خودداری می‌کند و در عین حال اجازه می‌دهد فشار اقتصادی افزایش یابد.
ترامپ با این استدلال که ایران از نظر اقتصادی «در وضعیت بسیار بدی» است و در حالی که محاصره دریایی ایالات متحده فشار را تشدید می‌کند، برای پرداخت حقوق سربازان خود با مشکل مواجه است، گفت: «این [مشکل] حل خواهد شد. همیشه حل می‌شود. مثل یک بازی شطرنج است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69808" target="_blank">📅 20:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69807">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🙂
لحظه کمیاب واژگونی کوه یخ غول‌پیکر در سواحل گرینلند؛
ویدئوی ثبت‌شده در ۲۵ ژوئیه ۲۰۲۶لحظه واژگونی یک کوه یخ عظیم در سواحل گرینلند رو نشون می‌ده.
با تغییر مرکز ثقل بر اثر آب شدن یا جدا شدن تیکه‌های یخ، این توده‌های عظیم برای رسیدن به تعادل جدید می‌چرخن.
در این فرآیند، بخش‌های آبی‌رنگ و شفافی که میلیون‌ها سال زیر آب فشرده شده بودن، برای لحظاتی در معرض دید قرار می‌گیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69807" target="_blank">📅 20:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69806">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=dpGM_-RvfpSWzTEUt4_t27903OkYhy_980ofaDEU8R_8hZI9mOajR_pVbv5QyUsMCsmYJQ1dntm4WdMJQAma75U80k8TmktacnVDItonvh0p5cUbJRF4AxT8nifTq9WUhNax2lb36sqmyRtxCSrrwLikqN3ZZtLAD1yREU1dV6_a18wHIpo1anIFRynqUsxDd8hubgQ_SQY3ICPPvB7sYxu07HxoEmLq4cTBDKzXd3y-VU8fKV6--9zpQ1fuAEqhw-1tOuGAu9tTFOIFezBittavKD7vQ4XLoFguD3xoYCOaOMdqDKXKiZSSRNyvolJqskde_bt9DHwQZsd5H6pVVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=dpGM_-RvfpSWzTEUt4_t27903OkYhy_980ofaDEU8R_8hZI9mOajR_pVbv5QyUsMCsmYJQ1dntm4WdMJQAma75U80k8TmktacnVDItonvh0p5cUbJRF4AxT8nifTq9WUhNax2lb36sqmyRtxCSrrwLikqN3ZZtLAD1yREU1dV6_a18wHIpo1anIFRynqUsxDd8hubgQ_SQY3ICPPvB7sYxu07HxoEmLq4cTBDKzXd3y-VU8fKV6--9zpQ1fuAEqhw-1tOuGAu9tTFOIFezBittavKD7vQ4XLoFguD3xoYCOaOMdqDKXKiZSSRNyvolJqskde_bt9DHwQZsd5H6pVVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
طرفدار حکومت در واکنش به کشته شدن حمیدرضا رجب‌زاده:
شما زدین مبارک شما ما زدیم مبارک خودمون
خدا سرشاهده جرائت دارید بریزید خیابون
یجوری تیکه تیکه تون بکنیم یجوری ریش ریش بکنیم شما رو تاریخ تو خودش ندیده
به جان امام شهید قسم به جان رهبر مجتبی قسم شما رو با کارتک از وسط خیابون جمع خواهند کرد
جنازه شماها رو میدیم سگ ها بخورن
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69806" target="_blank">📅 19:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69803">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XuYuSur8AyH9yLKVdvuk_72FCLYh9JS_P_O0TBmJpPwBowbYbB1NelLavzkqLmQl7OIk_QBLeY9gxKzb8KLvTAyTjIaGvnUqz4_m1OyF9jRB72zHJjRtrnY1O7YoMV98S3eIRb0fTtKDO116CfIaRWa6ebzimdIze9xCewrNvYD6b88esxDXilza6eJYtJbdY1Cs4HB77RdEZdh7qmWVMACSYJ3GZeL8oEzRq6zplb9FaiPTy6FmbY-clO2t-1ced8rX8wb50urc9HVhzVwjEmWueBB9hMuxVxmz5csglgYz2lMFpnVsMqaTIN7o2mujlWeMIKQJUsW3J0UIBP62GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PhO51RDwKyjJilJ9-FcugYsvlbwpG3GQVJV_x-YdQE4rpVvaGfspMjNvCKg-SI-BAOqu7a1B0kqeKKQIUO0HCZv4KgM-5sgjQD0mJ6UbFCM28CmF0EiOOvlN7WwYBN3VSdp3dSG4EXsx3tlmHhszSxtC0_gimJa42PQVYx7jjBTGxvCjyF_clL91xvtU_R9rQQsarz_UMsqmsLTaKCda7omSVPZHQQqCEg3D66kJsM6X2hqjHSmA2wpEGGtrQMZLFqTX4NVQSFuQWu21iUaKCxMpNLnvia69M6twmDcJ2KFbvy6FS4crE85P6sZDmKny2fcGq1KM67A5kwJM3ip5yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bAFUVAs7ZSIZFnEL50U6ugeESfwRNY4zdalV5Oc_BZuzezf4oYVpJln7Yiwy4PwQ7yzYNX-7KZJ9xNcqZsCvqWvgq_lizsvRqv13pTtOpxij9iBr-gr7gEZd7cOgdozSFRCMVVKZa3vfEhPCCz3G8-Dz8Hr3Ag9QJeHxmLUdYqCtgLKKkpoKkd38Kq953tu6X3Ag4mR32hEL2TLRmR5pcFv20QcWP6qeB2zXtKyLGvLYVN-KQidABMztaTIvlfRGaEcFPmH9eAyxo2GOnlV_cbfDFbaXpRy6M4dbkd1Ff0oRlpK0L4DMZx87IRlbZTiT-i03iDFbtBp66nU_hsfI1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ریورز یکی از مشهورترین فمنیست ها که زن رو برترین موجود میدونست و خودشم علنا لز اعلام کرده بود با یه پسر خوشگل و پولدار رفت قاطی مرغا
☺️
☺️
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69803" target="_blank">📅 19:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69802">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0cbb95dc3.mp4?token=jTOpibOZJDRcDdpfIRWZ9qm8IngDC4ubchT1mTSGDWASrf74zYGt2H01hyH1GVbGsAzXxEVhWkWpDJCTKBF2utphdkWAgBSgoVhc0hcGZ8JT30PVqpfChpjggOZEyn2eVNaG8Wf0lby_qr-LY_kjq_7Mm57jyzrkYqyFRkoD1i2bA1gVuuKp1VFjfTzVUtvn4OKQxACLFXE3VXQzXok_d7x7VQUHQ_0K08BiN8DrF5TM9vOlsbWvJXBn2rT3ME0GoXF_YNnf3TqQj6bgwnrrluIrpyTHbWJDNIZouOfHV78-rpQPo7IjeVCnLF9onTaWnV4DDthp0967UTa73W-UGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0cbb95dc3.mp4?token=jTOpibOZJDRcDdpfIRWZ9qm8IngDC4ubchT1mTSGDWASrf74zYGt2H01hyH1GVbGsAzXxEVhWkWpDJCTKBF2utphdkWAgBSgoVhc0hcGZ8JT30PVqpfChpjggOZEyn2eVNaG8Wf0lby_qr-LY_kjq_7Mm57jyzrkYqyFRkoD1i2bA1gVuuKp1VFjfTzVUtvn4OKQxACLFXE3VXQzXok_d7x7VQUHQ_0K08BiN8DrF5TM9vOlsbWvJXBn2rT3ME0GoXF_YNnf3TqQj6bgwnrrluIrpyTHbWJDNIZouOfHV78-rpQPo7IjeVCnLF9onTaWnV4DDthp0967UTa73W-UGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
یک فروند پهپاد بدون سرنشین جنگی (UCAV) نیروی هوایی ایالات متحده از نوع MQ-9A Reaper که از فرودگاه چابلی برخاسته بود، در نزدیکی گورستان چابلی در جیبوتی سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69802" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69801">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">پول درآوردن از بت دقیقا جاییه که فرق استراتژی داشتن و ادعا داشتن رو مشخص میکنه
👌
15 بازی 15 برد
✅
من به پول شما نیاز ندارم و چیزیم به شما نمیخوام بفروشم g18 لینک چنل https://t.me/+_btGj-rRAxs3NGVk https://t.me/+_btGj-rRAxs3NGVk</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/69801" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69800">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7tPTKa_Bidi3-7kwY9Nt7n76PUha8ZPveqm9NVnvRSnc5Qb8Pz385gEZUm2gMj6hU9jkO7FM2iOlpCsulb8MrnaTVwQGmQKsD9Ckw-KjqQeK5SC-b2ruWaTLYnoro8Tf8IuhrZ6t6if7KyegOKLS-rZ_Jmp1EXUhXf3TvQ6R1UQh7XVzn8ZwO-o93HDYSml2lxelOvRQBiKmp0eEEEKBkSxIcANz-ab0PI2sPdlLq7tdtws8-bqzKwWJDgXFckDm1tSayBtFdgipnnajxvYFwdYHyRpiYWAc4E2zCcmK-64lb6aHELgx3aCIoMKXrTpp9RzRJRzWQcw7g6JkvN3Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پول درآوردن از بت دقیقا جاییه که فرق استراتژی داشتن و ادعا داشتن رو مشخص میکنه
👌
15 بازی 15 برد
✅
من به پول شما نیاز ندارم و چیزیم به شما نمیخوام بفروشم
g18
لینک چنل
https://t.me/+_btGj-rRAxs3NGVk
https://t.me/+_btGj-rRAxs3NGVk</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/69800" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69799">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411943761d.mp4?token=jKHf1UPk-ukrTGEIcht31d9Yu4D1amAuUjpaxz9xY0BsA6wObzsSV_hn7tH9yYA5z3bwePhf1f8vhk_Ln6NwCeRHkfUpZWkwZzxZndAgBuJ6uFNjfpRk1wv1tlMddM_NDM6SaaeC4-Orq-HfRXpurvmhG-uG2qQqVEszdm4myPm_h4zixDH_6WngGJwTRh0RYQxx2sCIsvVLanrIzE2azr_RRIcMKSkzRsrKvvCsNeUk9DwWLTc1VVhdhVkm5sEbkFj7UCHJcsB8mkMdE3tVdlfGMcCFJ_S_pk7T6OS1P3b89gTWLQuf2ho8B7yy9o7SNhFBI5CAkim2rTSP87Bq2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411943761d.mp4?token=jKHf1UPk-ukrTGEIcht31d9Yu4D1amAuUjpaxz9xY0BsA6wObzsSV_hn7tH9yYA5z3bwePhf1f8vhk_Ln6NwCeRHkfUpZWkwZzxZndAgBuJ6uFNjfpRk1wv1tlMddM_NDM6SaaeC4-Orq-HfRXpurvmhG-uG2qQqVEszdm4myPm_h4zixDH_6WngGJwTRh0RYQxx2sCIsvVLanrIzE2azr_RRIcMKSkzRsrKvvCsNeUk9DwWLTc1VVhdhVkm5sEbkFj7UCHJcsB8mkMdE3tVdlfGMcCFJ_S_pk7T6OS1P3b89gTWLQuf2ho8B7yy9o7SNhFBI5CAkim2rTSP87Bq2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
آقای پزشکیان بچه‌ها یه شوخی باهاتون کردن راجب درختی که میخواستید بکارید توی پاکستان، برامون بگید قضیه چی بود؟!
🇮🇷
مسعود:
من فیلم بلد نیستم بازی کنم.
اینکه الکی یه خاکی بریزی و بگی من درخت کاشتم پس تو نکاشتی.
ما نایب رئیس بودیم توی تبریز باید ده تا درخت میکاشتیم همشو خودمون کاشتیم.
ما کشاورزی میکردیم، همین الان اگه برم مزرعه خودمون بیل رو میگیرم کار میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69799" target="_blank">📅 18:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69798">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0eb6125750.mp4?token=WMUjWT51G07CG1vsyrpmOPiNh0XuF292ms4p_P5YqTq8KFewrVEjcZFkv0wE0McSCDEjch4FnQeh6nMoek8ndn2fI3sEC6PDDAbH_tp2kSlxI2l18NFX94Y-GygBT54Q9lOaCNXkd1ogHp9_clwbnLXi4GvBC7-0Sfqkv3MguEUkwDB3lsCP6QhjRw4Npv0r9fj5Qjm4_DH-mzgcgBYuUPuhNrcBIxG96AwVXrtut1udVSxCT1JjVSbjBqlxz_VHYKZKpiYJESt8f0nxP97MlD1tvMz94FT403zmshRJccr2yfgGV9CJAoHMk-DMpYyag-cTvrUBQ7rlL2TT-ZGnhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0eb6125750.mp4?token=WMUjWT51G07CG1vsyrpmOPiNh0XuF292ms4p_P5YqTq8KFewrVEjcZFkv0wE0McSCDEjch4FnQeh6nMoek8ndn2fI3sEC6PDDAbH_tp2kSlxI2l18NFX94Y-GygBT54Q9lOaCNXkd1ogHp9_clwbnLXi4GvBC7-0Sfqkv3MguEUkwDB3lsCP6QhjRw4Npv0r9fj5Qjm4_DH-mzgcgBYuUPuhNrcBIxG96AwVXrtut1udVSxCT1JjVSbjBqlxz_VHYKZKpiYJESt8f0nxP97MlD1tvMz94FT403zmshRJccr2yfgGV9CJAoHMk-DMpYyag-cTvrUBQ7rlL2TT-ZGnhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخشی از مستند«پسرملا» روایتی از چند سال آخر زندگی روح‌الله زم:
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69798" target="_blank">📅 18:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69797">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
📰
وال‌استریت ژورنال: دونالد ترامپ، رئیس‌جمهور آمریکا، از چند هفته قبل برای اعلام پیروزی در جنگ با ایران آماده‌سازی‌هایی انجام داده است.  او به مشاوران ارشد خود گفته است که در صورت بازگشایی کامل تنگه هرمز توسط تهران، می‌تواند این درگیری را بدون دستیابی به توافق…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69797" target="_blank">📅 17:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69796">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVxno7dpNWnY3OYhdlIkvukSi-z7UDpGo1f5KYnTQsAythq0G-vw4xbNxgYhyDHadPzX2-9Ig90iPkwiKBL0Bpauf7RtXF4sPAANZ65oTCrL0xi4TK62acYAOE3o5B3-UtVfItA6Nge4w5E_rk3Tpj1Bmtv_XqLVKD5CJ0g2Yuu1xPqywXn8_Gw_KdFdE-UQWH-Z-VMjygl4dQkh3jXqpTRT4ZEwUfAnBzK8XDBznfiOc75fHPUkzvWMkobb3a-dfg5mR57w_aqwtqlqmBRW5mnJXfuMvqEDbgucnnj-jsZsrSZrWoiI4kmLF5aWkj3BsvN9zjAbIEJ8xSSNxniODA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
📰
وال‌استریت ژورنال: دونالد ترامپ، رئیس‌جمهور آمریکا، از چند هفته قبل برای اعلام پیروزی در جنگ با ایران آماده‌سازی‌هایی انجام داده است.
او به مشاوران ارشد خود گفته است که در صورت بازگشایی کامل تنگه هرمز توسط تهران، می‌تواند این درگیری را بدون دستیابی به توافق هسته‌ای به پایان برساند.
ترامپ معتقد است که ایران احتمالاً در طول دوره ریاست‌جمهوری او، برنامه هسته‌ای خود را از سر نخواهد گرفت، به ویژه پس از اینکه آمریکا سال گذشته سه مرکز هسته‌ای بزرگ را بمباران کرد. مقامات آمریکایی می‌گویند که اگر واشنگتن بتواند فعالیت‌های هسته‌ای تهران را کنترل کند و ترافیک تجاری از طریق تنگه هرمز از سر گرفته شود، ترامپ احتمالاً تمایل بیشتری به تمدید آتش‌بس فعلی به طور نامحدود و رفع محاصره بنادر ایران خواهد داشت.
مقامات آمریکایی اعلام کرده‌اند که ترامپ همچنان مایل است تا در این بن‌بست دیپلماتیک جدید صبر کند، به ویژه زمانی که قیمت بنزین نسبتاً ثابت و در حدود 4.02 دلار به ازای هر گالن باقی مانده است، در حالی که سال گذشته این قیمت 3.16 دلار بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69796" target="_blank">📅 17:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69795">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa7b5af888.mp4?token=T7hoDAsCq9Qviek2hfJVzGHmYZOlfU5NSsSebaT-ywgSHNDBxaMZTlSVifBEbI-Ivkv_FGZnlkz3_OVYxd40aGkYDpPMhVX9AJuTAOBFwg1m32-UwP41C8o0koxG-uAQ6N6keJkieaiO1FC47Wk7s68PVgQ81AHQeeb1wJpHGR5DoZ2ECZmZ6HOPefdTocyjQ6BQVouWKxQsJK53yAix_jXlYBMJCWks5pbTeYRNuUud0w_jlwKpMz3m_djo3ldJWguiyM9fO-YPz75UkEHybd2MV_6xn9MH9UpmcwTYIhuiCJ6z5ZlzVj6sHc-wjtHKhPePB_J6oF-4RSehxKYeHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa7b5af888.mp4?token=T7hoDAsCq9Qviek2hfJVzGHmYZOlfU5NSsSebaT-ywgSHNDBxaMZTlSVifBEbI-Ivkv_FGZnlkz3_OVYxd40aGkYDpPMhVX9AJuTAOBFwg1m32-UwP41C8o0koxG-uAQ6N6keJkieaiO1FC47Wk7s68PVgQ81AHQeeb1wJpHGR5DoZ2ECZmZ6HOPefdTocyjQ6BQVouWKxQsJK53yAix_jXlYBMJCWks5pbTeYRNuUud0w_jlwKpMz3m_djo3ldJWguiyM9fO-YPz75UkEHybd2MV_6xn9MH9UpmcwTYIhuiCJ6z5ZlzVj6sHc-wjtHKhPePB_J6oF-4RSehxKYeHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تصاویری از یک پهپاد تهاجمی اوکراینی که به طور موفقیت‌آمیزی سه بار متوالی، موشک‌های پدافند هوایی زمین به هوا از سیستم "پانتسیر" روسی را در دریای سیاه جاخالی داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69795" target="_blank">📅 17:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69794">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⏺
معاون برق و انرژی وزارت نیرو:
خاموشی‌ها در مناطق عادی ۲ ساعت یا کمتر است و مناطق گرمسیر به دلیل شرایط خاص، از تخفیفات ویژه برخوردار هستند.
همچنین برنامه داریم تا یک تا دو هفته آینده، محدودیت‌های برق را به حداقل برسانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69794" target="_blank">📅 16:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69793">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3f5dd815.mp4?token=HJMQKtL9aPe-S0PWDnU2AIfHNMaGbr8IJ7krIx1zt1l64_uT9Grx-1xAwq4nGgy3WeaVDxUSfCGmQHyU9oXfRTcqi775KadQsbd4HC_lLPjYiutXiJuKi9Yud2ZTq77t5E6f7lSttVW5_-628CvOew09Rro_ETy_sR1xqZYsgj9CR2GHKXP8z1nV6RpRBdA5l-SftU8DZ1j5eI50ngWMgGG2xt3wTGfvK_pcdD3mJrj-DcHcWc-VKSax0BgIf9ngLsjvG65Uy6LKtA-txaxf4-lQhSOhKQqJ6FSm_X-sFAhmCj9mm6nAKSjtjl-bVx3xhDSfOMcUtfLn6ub5xGbJL6QnA4dndPrf_qfM-86bKLwxrprY7cQzFt7mkx-KfQKh-P4nki2H0OjLh98LXo9EXL78ana3640r1lEqospMoiFUMQwfqwVduObUVSeFNEMHGIRy6-Oy20lwdDjoFxzwyAQe7OejzYFIsxP6fHHqHjE9IOVgMkuRYNCXIBVUTtJdfrCyL2gjUAymQ1d_vwq-j8MR_klKN_Eh0paEaw3KPlAttjw0h4rOgD74XbZ1rRdTrf5EaBzQ4Xl5b93InC5HHgKJbhmk0ACqC9hAgioPId2MkW9KagQM4TMDnMSJ5NaI-YM0f6sdGDUAgC4a3IjmVL2HFlGhxOEz53ss4kNcdFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3f5dd815.mp4?token=HJMQKtL9aPe-S0PWDnU2AIfHNMaGbr8IJ7krIx1zt1l64_uT9Grx-1xAwq4nGgy3WeaVDxUSfCGmQHyU9oXfRTcqi775KadQsbd4HC_lLPjYiutXiJuKi9Yud2ZTq77t5E6f7lSttVW5_-628CvOew09Rro_ETy_sR1xqZYsgj9CR2GHKXP8z1nV6RpRBdA5l-SftU8DZ1j5eI50ngWMgGG2xt3wTGfvK_pcdD3mJrj-DcHcWc-VKSax0BgIf9ngLsjvG65Uy6LKtA-txaxf4-lQhSOhKQqJ6FSm_X-sFAhmCj9mm6nAKSjtjl-bVx3xhDSfOMcUtfLn6ub5xGbJL6QnA4dndPrf_qfM-86bKLwxrprY7cQzFt7mkx-KfQKh-P4nki2H0OjLh98LXo9EXL78ana3640r1lEqospMoiFUMQwfqwVduObUVSeFNEMHGIRy6-Oy20lwdDjoFxzwyAQe7OejzYFIsxP6fHHqHjE9IOVgMkuRYNCXIBVUTtJdfrCyL2gjUAymQ1d_vwq-j8MR_klKN_Eh0paEaw3KPlAttjw0h4rOgD74XbZ1rRdTrf5EaBzQ4Xl5b93InC5HHgKJbhmk0ACqC9hAgioPId2MkW9KagQM4TMDnMSJ5NaI-YM0f6sdGDUAgC4a3IjmVL2HFlGhxOEz53ss4kNcdFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
به یک نکته جالب توجه کردید که ایران به همه منطقه حتی فرای منطقه حمله کرد جز اسرائیل؟
تا الان به ما حمله نکرده ممکنه تو آینده بکنه ولی میدونه جوابش چقد سنگین و دردناک میشه.
شایعاتی هست که اسرائیل عقب نشینی کرده و ضعیف شده.
این شایعات از کسایی به ما روانه میشن که میگفتن اصلا نباید عملیاتی توی لبنان و ایران بکنید.
لازم باشد بخاطر منافع ملی به بزرگ ترین دوستانمان نیز نه خواهیم گفت.
منفعت اسرائیل رو پایبند به هیچ توافقی نخواهیم کرد و ما مستقل هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69793" target="_blank">📅 16:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69792">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef1f7ed1d6.mp4?token=V8yYvcgfDtjjuIvyLY5FL4pPeDK1K0LLjJ6c8g7_deeBN4CBiAHbU_o0LtR4JsldSFfzsZQ_gg_4tTRMW3R_Fa6TJfk-0PvcUJeJyQL9B1fy29B6ciqL52dmUKqTXgt0rnsnXVXMTEGcCQttKHd6YEBkx5H2MagzoGl6o8iqMLHA_aFzKibTBBYF7IDXWJlEeuWFCQ2aastDbpisKDmQjKwUk8c2tMY8mu5j4R9GwF8CpNw9cpYQFty9z-EwwpfzE0ymAope-40b2LcyZ-vLtYJIWc_ejOxpq83AqyAAXYj-GUtOPl7aVtt8hOAhM-5AjueQfuuds6tdOBeZnIBppA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef1f7ed1d6.mp4?token=V8yYvcgfDtjjuIvyLY5FL4pPeDK1K0LLjJ6c8g7_deeBN4CBiAHbU_o0LtR4JsldSFfzsZQ_gg_4tTRMW3R_Fa6TJfk-0PvcUJeJyQL9B1fy29B6ciqL52dmUKqTXgt0rnsnXVXMTEGcCQttKHd6YEBkx5H2MagzoGl6o8iqMLHA_aFzKibTBBYF7IDXWJlEeuWFCQ2aastDbpisKDmQjKwUk8c2tMY8mu5j4R9GwF8CpNw9cpYQFty9z-EwwpfzE0ymAope-40b2LcyZ-vLtYJIWc_ejOxpq83AqyAAXYj-GUtOPl7aVtt8hOAhM-5AjueQfuuds6tdOBeZnIBppA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آمادگی جانفداها:
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69792" target="_blank">📅 16:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69791">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26df8fab5.mp4?token=axyGw2n32XVwL84xC9C2RTKytCZ9cQj8QuP2vpow3ajGeAJMH2TUuMRdn-9y0ywYTjDLqK75MLrynnK6qGqidN8b8dHG01y1OLr0-bUycbC0hOSUCd6IcVfkfUZYnVhC6TKyc1CZswWhRYGDzuVheFXJm2AKo4rV7nOfRGvI9lQxax6eocNPryy6p260zfZY27A2200W15VxeEsMhChXk1Hvq4Uy8vSnNXSe0fcjpll9y5zbj9taHkqieEwkxQTaH-nlDXrf_ujQ7nJWMWjM5V6j67SD5CVf-yj8uIfKeDD2q0GmHn4iM6s7JHSALhq8EdMgsScfxH48AxtLWQsP5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26df8fab5.mp4?token=axyGw2n32XVwL84xC9C2RTKytCZ9cQj8QuP2vpow3ajGeAJMH2TUuMRdn-9y0ywYTjDLqK75MLrynnK6qGqidN8b8dHG01y1OLr0-bUycbC0hOSUCd6IcVfkfUZYnVhC6TKyc1CZswWhRYGDzuVheFXJm2AKo4rV7nOfRGvI9lQxax6eocNPryy6p260zfZY27A2200W15VxeEsMhChXk1Hvq4Uy8vSnNXSe0fcjpll9y5zbj9taHkqieEwkxQTaH-nlDXrf_ujQ7nJWMWjM5V6j67SD5CVf-yj8uIfKeDD2q0GmHn4iM6s7JHSALhq8EdMgsScfxH48AxtLWQsP5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ژئوپولیتیک:
ایران سامانه‌های پدافند هوایی ساخت داخل خود را به عنوان جایگزینی کم‌هزینه‌تر برای سامانه‌های گران‌قیمت خارجی معرفی می‌کند.
طرفداران این سامانه‌ها مدعی‌اند که آن‌ها موفق به رهگیری هواپیماهای پیشرفته شده‌اند و استدلال می‌کنند که فناوری بومی می‌تواند بدون تحمیل هزینه‌های سنگینِ تجهیزات وارداتی، دفاعی کارآمد فراهم آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69791" target="_blank">📅 15:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69788">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cUlyjM0FRyW92uyLxH6DQq5f2d6m-Wdr48x0sHk2xdDdBlUoOV8nH7srqzUzbrbYoap_URstfZQ7-S2c-3ym3qRTBNUlVK3X5ADUIJbixPJ2_ftfLfFYJ_EjOlbeBfbJVafmfnLlsAOZJ9SdQ209iC16cCTrbU-DKPFAhjGpTkzPj2atVCbhfclU3se8TVqHIuExfzyTKbHBxfkL8OWNZDHxHFZu-CWixtJb8CIEs5YmV0gVA4vbVOA3tsq_dRkwXh4zq4QDTXBxAMreMyEMdrj0uuzoxXZcPPNgVXV9JSb8fI5HEwxdZdaof5dlgcSL_OG4ikBKxoUzmwyPuHO-Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hZFmxF16-FL2P4EdjInkeXQ6C6N2izWhjAnBblVBBO8n0DNVyhRifKOLI60XVaRztZYA_hG0O79IO2LZi1TlbiiIvCcffQ-3BXPKSPsg7OC9GKTx824pESKNZHlQ_Sme2DMTvH54lYjWev3w62ztaai0OEL0td8zIY2X8a98zQjidW7rvYNo-yLLa_1AHDuNGKKeuvGYUIFbdp5v-Utv5F3Leuk_tdHU_RuPIx5JEXi15tCi_LUaHiM3lKXK_8P61NkJkhgQWjWkRxU9WlMlhDjfl7gHHj_IYxp6bCE3F2OJlfDZ9R7MorpHl1ZR-euJ8feKGyl2tFYkJwadYLbROA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ADFwuNp_tyQ8I3yBajlHdEfZCFXn9uWJEKMMyXlUEysZN4HxKdNNnh4w-83niO_EcajsRDymbxskX7SXp2y0W01ySqSQkmPJQwSDgvmizRuQhnpy2OPE3Xb2QL7T_nvB8FlNDWUShuK4eTxPjCwIz5Y9Wu6zFY4Fv8cXz4taJAoK3dMb5-vFW3ans269gykq4IEG4a7gO-2NF2bQLOqtqTWmlGC--XD8uDazIzPMbjgeU531LZPfsxowtejCUnyRDX0wepkKN3AQYK-eEduu6yEPnPTKN_JMKyQ5XRmnC7gKWCPloo3buqWPHHFSasYlDsxzQHq_IWjNPpph6HAlgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
🔞
ابعاد جدید ماجرای قتل حمیدرضا رجب‌زاده توسط یک بلاگر دختر:
حمیدرضا رجب‌زاده، یه مداح جوون، بعد از خروج از خونه ناپدید می‌شه. پلیس در تحقیقات به یه بلاگر زن می‌رسه که قبلاً با حمیدرضا در ارتباط بوده و اون روز هم ازش برای یه ملاقات حضوری دعوت کرده بود؛ حمیدرضا به این دختره بارها بخاطر حجابش تذکر می‌داده و بهش می‌گفته بحث سیاسی نکنه
طبق اعتراف متهم‌ها، این زن با کمک پنج مرد، حمیدرضا رو به یه محل خلوت کشونده، بیهوشش کرده و بعد اون رو با ضربات چاقو به قتل رسوندن و قلبشو از سینش دراوردن و رو صورتش مایع منی ریختن، بعد هم جسد رو به اطراف پرند بردن و آتیش زدن و از صحنه قتل فیلم گرفتن؛ با اینکه چند نفرو گرفتن ولی متهم اصلی هنوز فراریه!
🔞
ویدیویی که قاتل منتشر کرد
⚠️
⚠️
حاوی صحنه های وحشتناک
⚠️
‼️
اعترافات بلاگر دختر:
من با مقتول در فضای مجازی آشنا شدم  او مرتب به من تذکر حجاب می داد و می خواست درباره مسائل سیاسی حرفی نزنم و زندگی مناسبی داشته باشم من این موضوع را با دوست پسرم درمیان گذاشتم که او پیشنهاد داد مداح جوان را با بهانه ای به محله خلوتی  بکشانم تا او با دوستانش دست به قتل بزنند او گفت که گروه های منافقین بابت قتل بسیجی ها پول پرداخت می کنند بخاطر همین بعد از اینکه مقتول کشته شد فیلمش را گرفت تا به آنها بفروشد
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69788" target="_blank">📅 15:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69787">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRl98yTq1Voa3ORWiCenX6ETMzfoGmgr_hSNDJvzc7YMIknkk07y5s8byAm95Y0JQpRw3BoBDS_16_IUuB6nxneJRCf0_dgtUkd7K8jF1fLmdvm2vx9iY7QD5B_i_m1tT1fsLazc8mloAEJfW9x5TwPqb5yZ3jiBIwAy-YKWoauY7l8sLfBP5-htLNUeIohFKkqJmIFByIprE-xRj24xQn8LKsDLoxEfAURKQYWj00MKmZ66puJnEVPp5MiNMbiIAmBEw5xWAbMDha_df4namIBgk3v1broYvyCCKLWvKvlULl05aRzxhDJsPYPq0p4oZem608Fb3esQJ11GgJ-rZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
فرماندهی مرکزی ایالات متحده:
ملوانان آمریکایی در حال تعمیر و نگهداری هواپیماهای F/A-18E Super Hornet در عرشه پرواز ناو هواپیمابر USS Abraham Lincoln (CVN 72) هستند تا اطمینان حاصل کنند که تجهیزات گروه ضربت ناو هواپیمابر برای اجرای محاصره ایالات متحده علیه ایران آماده ماموریت هستند.
تا 8 آگوست، CENTCOM 53 کشتی تجاری را تغییر مسیر داد، 2 کشتی را از کار انداخت و 2 کشتی دیگر را نیز توقیف کرد.
🔴
ارتش ایالات متحده همچنین به بیش از 30 کشتی اجازه عبور از محاصره برای کمک‌های بشردوستانه را داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69787" target="_blank">📅 14:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69786">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
ادعای فارس:رئیس‌جمهور با رهبر معظم انقلاب دربارهٔ مسائل اقتصادی و نظامی کشور دیدار و گفت‌وگو کرد.
پزشکیان همزمان با شروع سومین سال ریاست‌جمهوری با حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای دیدار و گفت‌وگو کرد.
در این دیدار به‌تفصیل دربارهٔ مسائل و مشکلات کشور به‌ویژه تأمین نیازهای معیشتی مردم، شرایط موجود جنگ تحمیلی سوم و آیندهٔ پیش‌رو، تحولات حوزهٔ نظامی، راهکارهای ناظر به تأمین منابع و مدیریت مصارف «ریالی، ارزی و انرژی» و همچنین تعامل اقتصادی با طرف‌های خارجی تبادل نظر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69786" target="_blank">📅 14:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69785">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‼️
صحبتای این خانم در مورد کافه رفتن و پیدا کردن پسرای پولدار، خیلی وایرال و جنجالی شده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69785" target="_blank">📅 14:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69784">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ab9ff0322.mp4?token=pFgH-0RojWgOdYgDWhcYfnX-PSRdhJPoCylYnhn_TnXtZIFmLKNze_ZyfyRTAkyF-GEuPIY3mjoMbafoftBQBUzLV2iZKkcQSbdECnulswpUyaEWEkyQAzPu1q8ZVnIaowpW9m9fKkku2GCIMlWLNmTwt23eqzO7HKYeyaTkoFxIxctGaSO9l-SKWAprFqKluJcEjDCOADhZQ4TMyIuZJpxtHlIOWPJ-PUl2nJVGbFc4DfbEecZbevCd2R2y8r0F7YSRARJfur3D-fhIzjQgtrXrFTUwpZGQSF6JLsjJUhOYUu7DiyckXDerctehSfTAfozC7U-QBmQ2rA5PRqgMUxabWCzRcraRvOESo9xI5oCgMX5Gbt4lvFCRImNTueZUjRHmMRmA6DPJxG-eoV5ly_ir4G9qCw9Hddd7QDSdzqoT1RnkNObY9XpGCZQdrYGyl4WoX4aNNQWmuHEGeA8tteP89k53ysyzDfqThcza751LIPaXK6uV0rM7HXt-MGStibo31VmCQBYuNQccWoUsWi_gp-Bqf-HyXlm710qRgm5XsQVka70EBVpR-gq5dwBi30oS8qdrXlPqtkP6Tm3Rtx1TTJz1cl8wGvgkrT26tlaMdc9GI-HK_AVMYtJyXxInSZQoDRg2EztKSGJuhbkFX3SnHcC1_6ExQlZHWeucQKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ab9ff0322.mp4?token=pFgH-0RojWgOdYgDWhcYfnX-PSRdhJPoCylYnhn_TnXtZIFmLKNze_ZyfyRTAkyF-GEuPIY3mjoMbafoftBQBUzLV2iZKkcQSbdECnulswpUyaEWEkyQAzPu1q8ZVnIaowpW9m9fKkku2GCIMlWLNmTwt23eqzO7HKYeyaTkoFxIxctGaSO9l-SKWAprFqKluJcEjDCOADhZQ4TMyIuZJpxtHlIOWPJ-PUl2nJVGbFc4DfbEecZbevCd2R2y8r0F7YSRARJfur3D-fhIzjQgtrXrFTUwpZGQSF6JLsjJUhOYUu7DiyckXDerctehSfTAfozC7U-QBmQ2rA5PRqgMUxabWCzRcraRvOESo9xI5oCgMX5Gbt4lvFCRImNTueZUjRHmMRmA6DPJxG-eoV5ly_ir4G9qCw9Hddd7QDSdzqoT1RnkNObY9XpGCZQdrYGyl4WoX4aNNQWmuHEGeA8tteP89k53ysyzDfqThcza751LIPaXK6uV0rM7HXt-MGStibo31VmCQBYuNQccWoUsWi_gp-Bqf-HyXlm710qRgm5XsQVka70EBVpR-gq5dwBi30oS8qdrXlPqtkP6Tm3Rtx1TTJz1cl8wGvgkrT26tlaMdc9GI-HK_AVMYtJyXxInSZQoDRg2EztKSGJuhbkFX3SnHcC1_6ExQlZHWeucQKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
عباس عراقچی:
اکنون هیچ مذاکره ای با آمریکا نداریم و نخواهیم داشت
شروع مذاکرات بدون پایبندی آمریکا به شروط تفاهم‌نامه غیرممکنه
ملت ما تسلیم اراده یک عده خاص نمیشه
بدون تحقق حق ملت ایران کوتاه نخواهیم آمد
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69784" target="_blank">📅 13:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69783">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34556823e0.mp4?token=h8lkU1WeHB_RoyDFGx2UDDr0VEX6g3PxPxUUfH9eJtlGGQi4ywSn5sWJL0DzWm8FYau5d0oq8tj5DKlPFZzT_7WWLAdRYXi1MGJmAbN1HUnI0xRCqoefd7Z_zaeQrxUzbhImnvyFACeVrSBjN5n24nTkBDp9w-uI336BWKefOl7nZGB8BPCYvPn8POK9QJ4yLRJzC_KY3gW7OsXCzD7o9mO-UKBx4c7jcrSribVawOFXmF-Qw2OtodVZubbrP-lmOT5QbnvZDEjhcx6Iq0Sp81f31WNuTQ571_qaHhRWrQv85fdIenXpDw-Ezz-D1590ZGX1TC7tuxT5f6RraR-ZMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34556823e0.mp4?token=h8lkU1WeHB_RoyDFGx2UDDr0VEX6g3PxPxUUfH9eJtlGGQi4ywSn5sWJL0DzWm8FYau5d0oq8tj5DKlPFZzT_7WWLAdRYXi1MGJmAbN1HUnI0xRCqoefd7Z_zaeQrxUzbhImnvyFACeVrSBjN5n24nTkBDp9w-uI336BWKefOl7nZGB8BPCYvPn8POK9QJ4yLRJzC_KY3gW7OsXCzD7o9mO-UKBx4c7jcrSribVawOFXmF-Qw2OtodVZubbrP-lmOT5QbnvZDEjhcx6Iq0Sp81f31WNuTQ571_qaHhRWrQv85fdIenXpDw-Ezz-D1590ZGX1TC7tuxT5f6RraR-ZMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا متوجه بشید با قیمت الانِ یک نوشابه، تو سال ۹۵ می‌شد چه چیزایی خرید...
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69783" target="_blank">📅 12:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69779">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MO2qIZTXAnq9I5ODez8gqY6hdvdnGrWl_YexxC2q1gcXGZdrvtF_dErU9AGc50OOHD-ATD4lSzujsAb76ubRvuLMeRAbL-KlDYdADlunc0VfX7zKPr4_AuvvchygC5A_WGCYKkzWBjoQdoRCIB1HviRLtd2V_5fv5YSzgUzWqupBnn23ZGiPQWOqQKRBQVuodWex5aE4YNxXC9Bzm1ExeVFGr41S-4UNP6lWkHNarsfgkbkzFrSYUwbC5Bw4evBeX-BQVx6mHyHnlQxhOwcixxhyve89NBHCKHkntJFviL6PE2g2wGRJgpvTwc3rfWWeG6PEALzGuKxfnOESHXhUoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5f1aeb56.mp4?token=i30fPSl_8WKe21Uh_mN2kGv7O_P44xYAp6YEdsSOADZDi1CfErpmJMfCNe7bmDl-ZRvFHLAGTI3-gCWVhhT_zOzFRUXOSWaUErjMVivs7CBe6ey_E8wo_7PMQIwJXUPKxJvXUGUGQPIj75O0aztRnjKdK2dChP5SG8Jr5sZ8jgOfHbIdwV0jKueFrz-RbbFpPiyiJYDB0F0ZJ9Bo8b06b64ePkr9DhF-3mNnxganKO9gkTKWHWdLS09AhGnvMiDrh5zEquvQ418MEx65yiaLysL1_sHBMCfU07E4CoKt-DeWKh58RISxlwGGwB64wyA-4mTjlXbs4s8qzpDAzQxItg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5f1aeb56.mp4?token=i30fPSl_8WKe21Uh_mN2kGv7O_P44xYAp6YEdsSOADZDi1CfErpmJMfCNe7bmDl-ZRvFHLAGTI3-gCWVhhT_zOzFRUXOSWaUErjMVivs7CBe6ey_E8wo_7PMQIwJXUPKxJvXUGUGQPIj75O0aztRnjKdK2dChP5SG8Jr5sZ8jgOfHbIdwV0jKueFrz-RbbFpPiyiJYDB0F0ZJ9Bo8b06b64ePkr9DhF-3mNnxganKO9gkTKWHWdLS09AhGnvMiDrh5zEquvQ418MEx65yiaLysL1_sHBMCfU07E4CoKt-DeWKh58RISxlwGGwB64wyA-4mTjlXbs4s8qzpDAzQxItg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی اوکراین به بلگورود
نیروهای اوکراینی شب گذشته حمله گسترده‌ای پهپادی به شهر بلگورود روسیه انجام دادند که در پی آن چندین ساختمان مسکونی هدف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69779" target="_blank">📅 12:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69778">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69778" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
r18
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69778" target="_blank">📅 12:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69777">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-mv3jKK5Ihi_OSM90Q4Kg4aHWWZHNlh8hn9lbOtzsrEH-KjSgGdvqyLcgjCKTdHs8mN9QjPrdFT4h9hUfpTvAbCnnmkswQP3waJ7ZoiwNSCNNrMIemPg8CSc7c_s5aVCzgT0WvC5oyu5BWa6eyck6VoyR0xgdaW4X1WmUR-Xq8xe_B5er33v3oDrCxqmlg7A_mD725TEwmC1ZUIdk1B3sl8-xepfcowOHYuYm2aTSiUiN3UlycP3X-5yvucic18a2lI4HOqbDR1CwodIwGS95aAFYirM82QZ8uPw9HZSMpLmHafZUWJaNCgZqp2pDs9MCrf7Zx-TEw-pjK8cmrWvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r18
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/69777" target="_blank">📅 12:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69775">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c93de8243.mp4?token=v3WJAi_6k8EncNrHVviABfMhI1IjZfrj6rFQLeRx_IzZQQl1riYKCDxkGtpUWd6njdlJytGd8TZTwGpYilzduvzsHJl1_JhLBAaO6zHceRJVOW4CCGPJaMlDgUfNL1lTDNjE6nvq312trDUhI325a1u_QTxTyzg2nSUvGZezxHTbF62U-_QM_vTHN_ZrDkn9V8fOftXIPyDyox7cD5f2ji_yYZ8WeGHH2VZmaeFHuxmTSnGFV1-dYJP3f1KQ5VpaxKd39A7hMegzh_XibHBkQjm0d3tMnzwrKjpQDgtjw0bgltj5LWoB_PHnZGwCb4bbKGmCmx9nslBhKnGN4n-Qtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c93de8243.mp4?token=v3WJAi_6k8EncNrHVviABfMhI1IjZfrj6rFQLeRx_IzZQQl1riYKCDxkGtpUWd6njdlJytGd8TZTwGpYilzduvzsHJl1_JhLBAaO6zHceRJVOW4CCGPJaMlDgUfNL1lTDNjE6nvq312trDUhI325a1u_QTxTyzg2nSUvGZezxHTbF62U-_QM_vTHN_ZrDkn9V8fOftXIPyDyox7cD5f2ji_yYZ8WeGHH2VZmaeFHuxmTSnGFV1-dYJP3f1KQ5VpaxKd39A7hMegzh_XibHBkQjm0d3tMnzwrKjpQDgtjw0bgltj5LWoB_PHnZGwCb4bbKGmCmx9nslBhKnGN4n-Qtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
⚡️
تصاویر جالب از لحظه برخورد رعد و برق به ساختمان مرکز تجارت جهانی «اسپیرز» در نیویورک؛
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69775" target="_blank">📅 12:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69774">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b13fec044.mp4?token=QjQsE2_gc1ObJ17GhBp8VaA5A5YWgfQ-K2RctgGmu_dy06fZuIUgHrvPz5PZkyG_W_UAiAu2Cw0mnsrHuARsv1xG3e01W5O7JRNi5MbAZ-XlcYH36sOSpiPa9S4jMXLyJk5rT3s2gdlntd2cd-UaVYkvoCtJIQROPx78f7R066EY-rFLYyI-4nOPl2Nfo93CS1fz5Lhu9m43ulxJjtRmQ8gpf-yljzlpcfQkQQIJ8IIi1UcBrHX6tKVtmVoI2Zk3kC6hjKZ2U1sGWRKZ1EOHhhirPrxYBPyKCjsr7v6G84-zxTxVGPlVtW3fdGFq1BgRGwGck025pjnXma2qa-fOnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b13fec044.mp4?token=QjQsE2_gc1ObJ17GhBp8VaA5A5YWgfQ-K2RctgGmu_dy06fZuIUgHrvPz5PZkyG_W_UAiAu2Cw0mnsrHuARsv1xG3e01W5O7JRNi5MbAZ-XlcYH36sOSpiPa9S4jMXLyJk5rT3s2gdlntd2cd-UaVYkvoCtJIQROPx78f7R066EY-rFLYyI-4nOPl2Nfo93CS1fz5Lhu9m43ulxJjtRmQ8gpf-yljzlpcfQkQQIJ8IIi1UcBrHX6tKVtmVoI2Zk3kC6hjKZ2U1sGWRKZ1EOHhhirPrxYBPyKCjsr7v6G84-zxTxVGPlVtW3fdGFq1BgRGwGck025pjnXma2qa-fOnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
گوشه‌ای از سخنان وایرال شده خرازی، برادرزن مسعود خامنه‌ای:
جمهوری اسلامی یه موشکی به اسم «رستاخیز» داره که میتونه یه دور کامل دور زمین بچرخه و به راحتی خاک آمریکا رو بزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69774" target="_blank">📅 11:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69773">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0189fef147.mp4?token=ihTDv-4BRClK6tiyoRTF72cOhe_gRoD0kqf9KqFfkhef-rmZRUIU2pZ5Cnc4aD4hQIeG6zIXf38D1hMLjP3yIG2A_3U0Um8JtLf6IRpc5UeSCKE4mNBRmDpn-rdg73vs6X-nXZG8xtVFyvdt8dPWFF98BzIb16ZmwRjJq02UXJf9FCq1UPXlLhISCxMyQXUXpSp89ori8y-UNt1NHz1xZ-qTKLElT8f2hmfXt0m9Su9UPAxinoIOSMUBXBTDKFQV7kcBi4ocJT9U6v4fUxF3MhcdlTIQigfWWpb2QzzuwKqLsYiQwxuldJq5_mHJBtOInL8Hp5ZNnhyM9PBZGsDh05hg9PH-Q-qco8joqLJxVuCgEvVKFwuCqYiXOLDWT7Hte7COxEbSIVi3HB4DYlccXS_tcyACpMWaznwHtCxiAJOfaY83vClWqZfx9dDXwzmxac5_JpqOcQ47imIsQc4jrfS2GsmJMlOoVWHzuJboMlG1FqcGJCTB6_zJAOe9P6vSFQORZiRPEtL3Ej8hDm3TkVz3Toq9h2roBLFhBfDmFNGArSEfpZ-c6ZU9FuzT0WJIrZPU8sWavaTz9Ek19Fa3b90p4BRrwNw22zySdexz2QVBR7Lu41j2haHf67kGG1vmhn4N24hh8MIHsIfbu4JGI7MfG0mTGcA9BZUtqSqrNwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0189fef147.mp4?token=ihTDv-4BRClK6tiyoRTF72cOhe_gRoD0kqf9KqFfkhef-rmZRUIU2pZ5Cnc4aD4hQIeG6zIXf38D1hMLjP3yIG2A_3U0Um8JtLf6IRpc5UeSCKE4mNBRmDpn-rdg73vs6X-nXZG8xtVFyvdt8dPWFF98BzIb16ZmwRjJq02UXJf9FCq1UPXlLhISCxMyQXUXpSp89ori8y-UNt1NHz1xZ-qTKLElT8f2hmfXt0m9Su9UPAxinoIOSMUBXBTDKFQV7kcBi4ocJT9U6v4fUxF3MhcdlTIQigfWWpb2QzzuwKqLsYiQwxuldJq5_mHJBtOInL8Hp5ZNnhyM9PBZGsDh05hg9PH-Q-qco8joqLJxVuCgEvVKFwuCqYiXOLDWT7Hte7COxEbSIVi3HB4DYlccXS_tcyACpMWaznwHtCxiAJOfaY83vClWqZfx9dDXwzmxac5_JpqOcQ47imIsQc4jrfS2GsmJMlOoVWHzuJboMlG1FqcGJCTB6_zJAOe9P6vSFQORZiRPEtL3Ej8hDm3TkVz3Toq9h2roBLFhBfDmFNGArSEfpZ-c6ZU9FuzT0WJIrZPU8sWavaTz9Ek19Fa3b90p4BRrwNw22zySdexz2QVBR7Lu41j2haHf67kGG1vmhn4N24hh8MIHsIfbu4JGI7MfG0mTGcA9BZUtqSqrNwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بابای این دختره چون دخترش توی امتحان گواهینامه قبول شده براش BMW 225 خریده ناقابل ۱۲ میلیارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69773" target="_blank">📅 11:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69772">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/973161bf95.mp4?token=vSXtuxLGbZ_g_FYlBR4sY5soCeQTkMkJtxS3pLyVu4QT3b_aDHaz8oZKTkrBifNQ3fo8Ps7hyTEj4-fMHF83rCU46x-WQ8IgDQ9fSlgXb1L-FRXGMdJ8S_Afh08gbkB7TNZTOcTwfxbmIpg7im2O2T22xsZBSiv3j6ifBqIbp1uPklQLIbNjlKzV2NeQ4RnCgKRqgMaedkbF-OSxnz7G-VSvb0VSwO98OpisrZZdKCHpe8pzQiW_E0BuKDjZLZ3f4KFyCE5I9oHEsTJqKK2mbvEPZxBfIyqMOMBLLg90nA2jdIGKzC0IKFLba6o2WzqfHghcPuOx8JtWXmORi1re8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/973161bf95.mp4?token=vSXtuxLGbZ_g_FYlBR4sY5soCeQTkMkJtxS3pLyVu4QT3b_aDHaz8oZKTkrBifNQ3fo8Ps7hyTEj4-fMHF83rCU46x-WQ8IgDQ9fSlgXb1L-FRXGMdJ8S_Afh08gbkB7TNZTOcTwfxbmIpg7im2O2T22xsZBSiv3j6ifBqIbp1uPklQLIbNjlKzV2NeQ4RnCgKRqgMaedkbF-OSxnz7G-VSvb0VSwO98OpisrZZdKCHpe8pzQiW_E0BuKDjZLZ3f4KFyCE5I9oHEsTJqKK2mbvEPZxBfIyqMOMBLLg90nA2jdIGKzC0IKFLba6o2WzqfHghcPuOx8JtWXmORi1re8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
علی مطهری، نایب‌رئیس پیشین مجلس شورای اسلامی:
از همان ابتدا، هدف ما ساخت بمب‌های هسته‌ای بود و باید تا پایان ادامه می‌دادیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69772" target="_blank">📅 10:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69768">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c32fad0f32.mp4?token=F1NA2E4qS5rt8bIOx7HdwZOYXZ7TfrpcnMqflPUvif0u_pUzuVRdZeNXy87bOX55DGbVcmQQos1oQxBKTHxL5bhDQQ9rrIhdzY_1dV3QPGD03oXldxKWNECrKmoQrYeyYvLBRPZD8NEcJhS7D7NfG916VsVtwyxZiMR4hSLjfbXd9ZcNA8TQ6HPo4EZ6tEiC15aPaV4Ijxn4eGIvNdbLUczoOgI338SqpsyNUCK8ipAkYEkb695ZZNr_XekUBCEZOBgK3LDOcdR2ZvBkDuhGtloXyxd6eERJ-4wn8prcsxnPS6SgC9PFtGVWH-4FKdRQLyhLMcdPNXO0YSBJNRzRHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c32fad0f32.mp4?token=F1NA2E4qS5rt8bIOx7HdwZOYXZ7TfrpcnMqflPUvif0u_pUzuVRdZeNXy87bOX55DGbVcmQQos1oQxBKTHxL5bhDQQ9rrIhdzY_1dV3QPGD03oXldxKWNECrKmoQrYeyYvLBRPZD8NEcJhS7D7NfG916VsVtwyxZiMR4hSLjfbXd9ZcNA8TQ6HPo4EZ6tEiC15aPaV4Ijxn4eGIvNdbLUczoOgI338SqpsyNUCK8ipAkYEkb695ZZNr_XekUBCEZOBgK3LDOcdR2ZvBkDuhGtloXyxd6eERJ-4wn8prcsxnPS6SgC9PFtGVWH-4FKdRQLyhLMcdPNXO0YSBJNRzRHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ایشون به اسم آرش، خودشو اولین:
همجنس‌بازه، شیعه، پادشاهی خواه، دو رگه تُرک و لر معرفی کرده که پشمای همه ریخته
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69768" target="_blank">📅 10:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69767">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c02b892b.mp4?token=Z0mVGTKaVEhnk0_-Ve6bqVVwhuRStV-_9Wk7muk6lSctKJahtTjpkVWk5KfpkN-Py04RDgtYXPbhaqa99JWe5MJer0XzhQ89RjJztiPdehkjFJa7MXxmZg9kALdqt1GH3ykj81iLYZBDArH_TPALrTFN6Ks4ZoOrVYgxtZisoLfXyGPLS-p-lucdtuMjDse__Evz2kneWP_-7RZMyPEZpS1MNYVqLkE5Gqg9kf1o3IhgQAceOXxLcOOx5a6Fo7Mm4fcncEcsGcqSVv4bSlKzZWm7LGzfL_NXFBddPq9FI-8hp5I36dtJaevzODBfIUWy4BpPKjTpzTMaSV38dm38Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c02b892b.mp4?token=Z0mVGTKaVEhnk0_-Ve6bqVVwhuRStV-_9Wk7muk6lSctKJahtTjpkVWk5KfpkN-Py04RDgtYXPbhaqa99JWe5MJer0XzhQ89RjJztiPdehkjFJa7MXxmZg9kALdqt1GH3ykj81iLYZBDArH_TPALrTFN6Ks4ZoOrVYgxtZisoLfXyGPLS-p-lucdtuMjDse__Evz2kneWP_-7RZMyPEZpS1MNYVqLkE5Gqg9kf1o3IhgQAceOXxLcOOx5a6Fo7Mm4fcncEcsGcqSVv4bSlKzZWm7LGzfL_NXFBddPq9FI-8hp5I36dtJaevzODBfIUWy4BpPKjTpzTMaSV38dm38Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای یه طرفدار حکومت درباره حجاب:
آقای پزشکیان واقعا مرسی که گفتی نمیتونم قانون حجاب رو رعایت بکنم
مجلسی که ناظر هستی توام دمت گرم که اصلا فکری برا حجاب نمیکنی
پزشکیان داره میگه ععععععع مگه هنوزم گشت ارشاد هست؟؟
بحث دیگه حجاب نیست بحث پوششه پوشش و اصالت ما داره از بین میره
تو خود اروپا هم قانونی برا پوشش هست نه اینکه لخت بریزن خیابون
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69767" target="_blank">📅 09:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69766">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed36a1671.mp4?token=K1sngs2-rUPJAccV-UJfM1NjZsjuX40kA1HQZ_9hR_02ZpIhxluttp8d7pyNLy9ibAQXPiVkiFe5A8PnkFP0a4KujukuZmVR-xqt5aJcYoOU4VkzyLib3BWG2YXOyC0TDhRwV8_TmTTcpbPM3jD2hs-Hp2zGJ4KltpzC1LDH9OkE44pyKSbymyqNiNS02mNU73dfhtSY1YkisponlOQXe9a9ArUmfN60TmXfLUseE_SBuTd0jBbMqPyMFblPLvVMkATSJXUg08hj4Hdd6AD-EjdkCt5ea4mlOPTQxSuZD83RoN902lhRziApbVQsut5pG3j82K1gAuDLZtUOXTWp8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed36a1671.mp4?token=K1sngs2-rUPJAccV-UJfM1NjZsjuX40kA1HQZ_9hR_02ZpIhxluttp8d7pyNLy9ibAQXPiVkiFe5A8PnkFP0a4KujukuZmVR-xqt5aJcYoOU4VkzyLib3BWG2YXOyC0TDhRwV8_TmTTcpbPM3jD2hs-Hp2zGJ4KltpzC1LDH9OkE44pyKSbymyqNiNS02mNU73dfhtSY1YkisponlOQXe9a9ArUmfN60TmXfLUseE_SBuTd0jBbMqPyMFblPLvVMkATSJXUg08hj4Hdd6AD-EjdkCt5ea4mlOPTQxSuZD83RoN902lhRziApbVQsut5pG3j82K1gAuDLZtUOXTWp8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدیو وایرال شده از فردی که در زمان رفراندوم سال 57 حضور داشته
:
وقتی من روز رفراندوم رفتم بیرون و دیدم گفتن ۲۰ میلیون نفر رای دادن زنگ زدن آدما بهم گفتن بیا ببین چخبره.
اونجا رئیس حوزه آخوند بود و این بیجک های صدتایی رو میدادن دست مردم میگفتن بنداز صندوق بگو مرگ بر شاه.
جمعیت ایران اون زمان ۳۷ میلیون و ۲۰۰ هزار نفر بود.
کل کسانی که بالای ۱۶ سال بودنو و میتونستن رای بدن ۱۸ میلیون و ۷۳۲ هزار نفر بود.
آمار رو با خنده اعلام کردن ۳۰ میلیون نفر رای دادن.
توی وزارت کشور گفتن که اینطور نمیشه پس گفتن ۲۲ میلیون و ۴۰۰ هزار نفر رای دادن و ۲۰ میلیون و ۴۰۰ هزار نفر به جمهوری اسلامی بله گفتن.
اینو حساب کنید دیگه از کل ۱۸ میلیون نفر واجد شرایط مخالف بود مریض بود زندانی بود و.... از اینجا بود که من راهمو از اینا جدا کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69766" target="_blank">📅 08:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69765">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-release.apk</div>
  <div class="tg-doc-extra">4.5 MB</div>
</div>
<a href="https://t.me/news_hut/69765" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎲
همین امشب با اولین شارژ
🤩
🤩
🤩
درصد شارژ بیشتر بگیر
همین الان شانست رو با موجودی اضافی امتحان کن حتما بزنده میشی
👌
👇🏻
👇🏻
🌐
Telegram
🎲
🌐
winro.io
🎲</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69765" target="_blank">📅 01:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69764">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCFTdeHOqlAJjomOXWq-D5zMaEeNM6l17h1Sm01eJwIgyHzyNTXXyaLGt2KEGYbDKYGik-hrlXEwyeMDyJHrzesMIHrVfMnNI1yMHbgLm0dz4iuQjMel580CCRh1-46GX25JWNC_JyP8hvN9iWQ2NL4rqLO3KfpU6W6klNP8XzTe8v5TrCooiQxx0nE9YEjcpaHuVsNNh42RSJq99871K4ZiHQ30O2n8EDD_kvMNK6C7Z2ImM6mgik05CfswirzmCcRtl_wKWfVWUnwzZnRePpFpmpVHhlfSsGWv_BSgljdlcz0BWVwzPozdedkLobtLJRlddK7BdEnUVVvUOGs6lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
همین حالا موجودیتو
🤩
برابر کن
❌
☑️
۲/۵ میلیون شارژ کن ۱۰ میلیون شارژ شو
✅
برای اولین واریز تا 15 شهریور ،
0️⃣
0️⃣
3️⃣
درصد بیشتر در وینرو شارژ شو
🎁
✅
به ازای هر واریز در وینرو به ترتیب 300 ، 150 ، 75 درصد بیشتر شارژ شوید
.
🔊
با شارژ اضافی بدون ریسک بازی کن سرمایتو چند برابر کن
⚡️
🎲
ثبت نام آسان و سریع کلیک کنید
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا a17
🌟
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69764" target="_blank">📅 01:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69763">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20cf5580ad.mp4?token=EcJuigeNiUpNc2yrhKqFxe8XqI21jjwlMBU4Vzp3OB-WI2zaknylg0hDLF4FhXbGhDdKOzQuIxptfbBbCDXU8fN1uAAgVXCa1ZFFT9zcnAU42l1vlvd_rwnlzb1pmBi__4bnhmgKKSoYbenh_Zo_wy7A21oWvrAtPH7qBpOGhnd2dEFeqadWuJuWil4kpMMndWrQ_rlj3JZ374PsdAxy-Ra36Db4MrXmVFknaBorFs3uJEpv6j2nefVmwylyKgUdTrfgHbKJdW6eph7G8g7SdbMUx_wd8y-Zk8dzqLsZ4MhzEs0GWKfBu6NRu56YOGWcTpmHZJ-8owFidXK6iNgVpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20cf5580ad.mp4?token=EcJuigeNiUpNc2yrhKqFxe8XqI21jjwlMBU4Vzp3OB-WI2zaknylg0hDLF4FhXbGhDdKOzQuIxptfbBbCDXU8fN1uAAgVXCa1ZFFT9zcnAU42l1vlvd_rwnlzb1pmBi__4bnhmgKKSoYbenh_Zo_wy7A21oWvrAtPH7qBpOGhnd2dEFeqadWuJuWil4kpMMndWrQ_rlj3JZ374PsdAxy-Ra36Db4MrXmVFknaBorFs3uJEpv6j2nefVmwylyKgUdTrfgHbKJdW6eph7G8g7SdbMUx_wd8y-Zk8dzqLsZ4MhzEs0GWKfBu6NRu56YOGWcTpmHZJ-8owFidXK6iNgVpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
سربازان روس با تفنگ موفق شدند پهباد اوکراینی رو سرنگون کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69763" target="_blank">📅 01:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69762">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
‼️
حمیدرضا رجب زاده یکی از مداح های حکومتی بوده که چند هفته پیش به قتل می‌رسه، حالا یه کانال تلگرامی مدعی شده اونا این قتل رو انجام دادن دلیلشون هم اینه بوده که این مداح تو دی‌ماه جز نیرو های سرکوبگر بوده و به سمت مردم تیر می‌زده  ویدیوی قتل که قلبشو از سینش…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69762" target="_blank">📅 00:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69760">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g066ScgQmG1a3Pxn9HUT31fey7Z5BB0CLmr1Ve4RYI4jqbGcmlpwjiaO8Z0eMCQHH7-bSPWeLckUTaA4H9f-QSUaOpcQii3SxfXI3dF3cwDjS5NGDh9VW0uxUt02NuF93bzAWYU8ln8wqUZCvabPRRSCZlVk-UY3x8hJJoXRRgR6q0pr2mWoQrkjfIWnb1pQjWxTY2k-N06Ze2q_uX3zBB_aPh2UFzUouWF1wX1yhDNs3x75C3rQQOX-q1wiFQ5SwdJ59ABaGzEJrp3ruLfYuaRcgfiuUS-qJqOwlW330R9_DezlVx7A0-sCl-S3C5AJctsu8GQIzIiHeXWzVW0PKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5e8a9ce1b.mp4?token=OXTXV8Tn_pZksKwb9MemOn4-fdsLGwcmyCbAOBhXXpMivxNeJY9JsNI5mqjwpgUi1Gy_FFVfEM3Kcph7VGm8V_ltJyTvM4lhMWgkBTdJo9CCqesfyi-Xkp52_fsxw-QZoDLE4qs79kreG_SSGwSn4OK2iMxGSNFQp-5SV0kKa0duxlBHuVGBz7kA_KZNrvi1bCYYE7nidKyM3mAizMbbiAHKp7IbDlFQd_xTE4L9XqflasUNjqmiDW2mUZcIlnwr5rW0ez2xr6LNRKjrIDxJWms0t4MjtZNimk5hFRJzBlpU-VTV-Cm-ldldzvp0yO7C61fRM-9BJ4KHhxCVmVHrkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5e8a9ce1b.mp4?token=OXTXV8Tn_pZksKwb9MemOn4-fdsLGwcmyCbAOBhXXpMivxNeJY9JsNI5mqjwpgUi1Gy_FFVfEM3Kcph7VGm8V_ltJyTvM4lhMWgkBTdJo9CCqesfyi-Xkp52_fsxw-QZoDLE4qs79kreG_SSGwSn4OK2iMxGSNFQp-5SV0kKa0duxlBHuVGBz7kA_KZNrvi1bCYYE7nidKyM3mAizMbbiAHKp7IbDlFQd_xTE4L9XqflasUNjqmiDW2mUZcIlnwr5rW0ez2xr6LNRKjrIDxJWms0t4MjtZNimk5hFRJzBlpU-VTV-Cm-ldldzvp0yO7C61fRM-9BJ4KHhxCVmVHrkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمیدرضا رجب زاده یکی از مداح های حکومتی بوده که چند هفته پیش به قتل می‌رسه، حالا یه کانال تلگرامی مدعی شده اونا این قتل رو انجام دادن دلیلشون هم اینه بوده که این مداح تو دی‌ماه جز نیرو های سرکوبگر بوده و به سمت مردم تیر می‌زده
ویدیوی قتل که قلبشو از سینش در میارن و رو صورتش خودارضایی می‌کنند رو هم منتشر کردند و بعد برای خونوادش فرستادن؛ چند ساعت پیش هم اعلام شد که قاتلین دستگیر شدند
🔞
مشاهده‌ی ویدیوی اول
⚠️
⚠️
مشاهده‌ی ویدیوی دوم
🔞
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69760" target="_blank">📅 00:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69758">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a034d8d108.mp4?token=AGxCG4fFWRxqC9n8bqw4myal8pLmxaruLtqpV2A1kH8bAXTMCSbWGI_0ROH7DX9LFkKbs_9lji5vSLtvqG7DrPeb9s1L-N92l61M8uk1IZLwq0pO6kJA5BBHp7QaqGTba3XwqnwwOXnT4U4CToqkBRLjAwYwo4MPW7__g4nNlRhqN7tN0CiaI00bHH6hz1zbwb4g_fZWkj7I0jx6eNFZpqQHlSmS9y8Qcy7fERDYNvikfD1c2ZtIKvtkTra21j2BMmQNM3M8miYwqZH-NIMCzyaDat7YKANwjt1gJKW4ddzHS7n0WeiqXcXaVGi3X-1UDXoCcVla5j4OABCtIDYDqDYKIXiOX3RAsyICRVJMhjDz8gj08cAW7QaD8BfrbxeIHcfjcjX6ucAFEg4FjRPCJCMbe-M1AEVAnLlxpBGa1aI26QrKOTZ0WSVqlBpdhzJIvRYb9LBcgoPymfGW6ZBuN284mGbam4P7PvdsYUuufWrZgwV6FCLpaUnol1-oGJkfOUGRZFVBcqP-cHc-5vbpf_KWJDNpAWRZW1O-P-pfGNMBwKnUylIwhum6x4H7kV2Ou2sBecKd-TW0waJho9KsFCzfNjznBXzkkMHcamzGe055he1-_Xk4B65iBrdtBVfmY5iG7PSs2Ds36hkTgM1I2q_zxSilHbwMp48uXdydQIk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a034d8d108.mp4?token=AGxCG4fFWRxqC9n8bqw4myal8pLmxaruLtqpV2A1kH8bAXTMCSbWGI_0ROH7DX9LFkKbs_9lji5vSLtvqG7DrPeb9s1L-N92l61M8uk1IZLwq0pO6kJA5BBHp7QaqGTba3XwqnwwOXnT4U4CToqkBRLjAwYwo4MPW7__g4nNlRhqN7tN0CiaI00bHH6hz1zbwb4g_fZWkj7I0jx6eNFZpqQHlSmS9y8Qcy7fERDYNvikfD1c2ZtIKvtkTra21j2BMmQNM3M8miYwqZH-NIMCzyaDat7YKANwjt1gJKW4ddzHS7n0WeiqXcXaVGi3X-1UDXoCcVla5j4OABCtIDYDqDYKIXiOX3RAsyICRVJMhjDz8gj08cAW7QaD8BfrbxeIHcfjcjX6ucAFEg4FjRPCJCMbe-M1AEVAnLlxpBGa1aI26QrKOTZ0WSVqlBpdhzJIvRYb9LBcgoPymfGW6ZBuN284mGbam4P7PvdsYUuufWrZgwV6FCLpaUnol1-oGJkfOUGRZFVBcqP-cHc-5vbpf_KWJDNpAWRZW1O-P-pfGNMBwKnUylIwhum6x4H7kV2Ou2sBecKd-TW0waJho9KsFCzfNjznBXzkkMHcamzGe055he1-_Xk4B65iBrdtBVfmY5iG7PSs2Ds36hkTgM1I2q_zxSilHbwMp48uXdydQIk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو این مملکت اگه پول داشته باشی، حتی کمپ ترک اعتیاد هم می‌تونه شبیه هتل چندستاره باشه!
● بعضی کمپ‌های لاکچری خدماتی مثل:
🍽️
غذای رستورانی
🏊
استخر، سونا و جکوزی
🎱
بیلیارد و پلی‌استیشن
👨‍⚕️
پزشک عمومی و روانشناس
📱
موبایل و لپ‌تاپ آزاد
🛏️
اتاق‌های VIP
ارائه میدن؛جایی که دیگه از کمپ های معمولی خیلی فاصله گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69758" target="_blank">📅 23:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69757">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a2b2f82e.mov?token=YcTlSxjjFbjLDDUP5rmC1OHw0tSfnluNJ6cdX8ssk6JdiIM_iE204NxGJt3gugsrWZE3BAAd4YFMB3HrXkzGJq5lxt9y2QP5SbCq_X_l3_6VewUhLbEiTLCXx9HjyjS_IdacHGAWqCJStkiQt9Hn2otVRGTkqC1aH5Wi8qgHmRk6nEN2rvOw8xUbN0R_gPM-HQbmycFjvbZO1-QDQdQF14MNaSrS5mMidFBUu6a7AMusEL17-MH2gA2fgUfqwjZvn0SvcCmpcYNsUKngnC-QgJhFAmpkL10tD5T0fX0PN5Ny2GDcCQdGiYyUF9GpmJ2BUpJ1b3hJtyJZFi8NPYpn-H8IJ-G0ALVCAIfx5r-xaqLacsWxGEMG00DQkSQks_GxVVptPrrELCKxHhabRinrnhnwmYjiHRHbcVjZo2YP6lOZw-lSAWM7E_OXfcFesXM2crEcU4UzkmHL2do4vK2-XS_SFZ8V-c90Yf2-WLPjfDYJstVrMohK-uDQtNGEztNGcD24xp3gRjaiOtUGw3Cx9bSl6abpB3JGxKYgf8yHTlNXZ4JxE51G_cDE5TrsgHbQMOht6Ww17H6_GL70v3HYcLOV9YrciWIQskMDMBWdkDcGpHqg9A9I5j2AWFPXAuKBj8X6qq8P7ZgIT9LpVw4nunUdX0GjaVm5biVxcvKrg3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a2b2f82e.mov?token=YcTlSxjjFbjLDDUP5rmC1OHw0tSfnluNJ6cdX8ssk6JdiIM_iE204NxGJt3gugsrWZE3BAAd4YFMB3HrXkzGJq5lxt9y2QP5SbCq_X_l3_6VewUhLbEiTLCXx9HjyjS_IdacHGAWqCJStkiQt9Hn2otVRGTkqC1aH5Wi8qgHmRk6nEN2rvOw8xUbN0R_gPM-HQbmycFjvbZO1-QDQdQF14MNaSrS5mMidFBUu6a7AMusEL17-MH2gA2fgUfqwjZvn0SvcCmpcYNsUKngnC-QgJhFAmpkL10tD5T0fX0PN5Ny2GDcCQdGiYyUF9GpmJ2BUpJ1b3hJtyJZFi8NPYpn-H8IJ-G0ALVCAIfx5r-xaqLacsWxGEMG00DQkSQks_GxVVptPrrELCKxHhabRinrnhnwmYjiHRHbcVjZo2YP6lOZw-lSAWM7E_OXfcFesXM2crEcU4UzkmHL2do4vK2-XS_SFZ8V-c90Yf2-WLPjfDYJstVrMohK-uDQtNGEztNGcD24xp3gRjaiOtUGw3Cx9bSl6abpB3JGxKYgf8yHTlNXZ4JxE51G_cDE5TrsgHbQMOht6Ww17H6_GL70v3HYcLOV9YrciWIQskMDMBWdkDcGpHqg9A9I5j2AWFPXAuKBj8X6qq8P7ZgIT9LpVw4nunUdX0GjaVm5biVxcvKrg3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
نیروهای روسی به هدف قرار دادن تدارکات اوکراین ادامه می‌دهند و یک لوکوموتیو دیگر را در نزدیکی ایستگاه راه‌آهن «لوزووا» در استان خارکیف منهدم کردند؛
منطقه‌ای که یک کانون کلیدی برای کی‌یف جهت انتقال تجهیزات نظامی و نیروهای کمکی به سمت دونباس محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69757" target="_blank">📅 22:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69756">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da63e2e1aa.mp4?token=DsdWwBW0XdDVXyfCplt9qhiNXBS3wMT_z3gHLNtIYy5akdYhVHCoeMdTgGTshJ1OpjRYfbEu8aHrJOx5EtoPbUD8lbx9n6GO0aKRmR_p4HnQdTok4ZVvknJqBokh6RHLZ7AqEO8_nN0xtGskuFSQ3asTl0mR07lfi2y43jOWein2sem6JbS5iC0mV714Mma_JF_tJyXZlQOYml7gQR_Ef-rCzC37kCDn2N6EMl7aiyI6ijr_sUAbwkTOOtATIU88X7wow-Il19XQzdgcqC9ZVyIj8WY2S04SHElJ_O3ClulV4uLLRxW6FzC8-9Vvo5M8gl7Qda9ynf9hSKhiVgLtchO0MjLgaT8Z7r9kjW2-rv6LNPLYoeZB8EgVWVFL-daOpcHUC0WBUsbmaSZLNJyWTtdl7396222D2xBp2poRV8rR2z5kvTE08azKvaZJ2FrBJfxM11BmAmDUT5x0NpYtuEjtb21ARlc8B790fAGv9B2qD7N4sc6AP2EaZG2Df41PjzIZ_Bo934ktTh3P7dazvGlPr6mZ6RnvWy1gnxtp-o08LltlITs7gtcCqs_AYwi1syN3gNu0XYGiGIof7aYF1k3xZiN129UiRE55JP93CyoX6DPOpslDsZK_xf1hKK0v2vJwehSqXuh8h5uIf1sAyzAj6-DqKCYJcDMLHduDYCU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da63e2e1aa.mp4?token=DsdWwBW0XdDVXyfCplt9qhiNXBS3wMT_z3gHLNtIYy5akdYhVHCoeMdTgGTshJ1OpjRYfbEu8aHrJOx5EtoPbUD8lbx9n6GO0aKRmR_p4HnQdTok4ZVvknJqBokh6RHLZ7AqEO8_nN0xtGskuFSQ3asTl0mR07lfi2y43jOWein2sem6JbS5iC0mV714Mma_JF_tJyXZlQOYml7gQR_Ef-rCzC37kCDn2N6EMl7aiyI6ijr_sUAbwkTOOtATIU88X7wow-Il19XQzdgcqC9ZVyIj8WY2S04SHElJ_O3ClulV4uLLRxW6FzC8-9Vvo5M8gl7Qda9ynf9hSKhiVgLtchO0MjLgaT8Z7r9kjW2-rv6LNPLYoeZB8EgVWVFL-daOpcHUC0WBUsbmaSZLNJyWTtdl7396222D2xBp2poRV8rR2z5kvTE08azKvaZJ2FrBJfxM11BmAmDUT5x0NpYtuEjtb21ARlc8B790fAGv9B2qD7N4sc6AP2EaZG2Df41PjzIZ_Bo934ktTh3P7dazvGlPr6mZ6RnvWy1gnxtp-o08LltlITs7gtcCqs_AYwi1syN3gNu0XYGiGIof7aYF1k3xZiN129UiRE55JP93CyoX6DPOpslDsZK_xf1hKK0v2vJwehSqXuh8h5uIf1sAyzAj6-DqKCYJcDMLHduDYCU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از مردم پرسیدن "چه فکریه که نمیذاره شب‌ها بخوابین؟"جواب‌هایی که دادن جالب و دردناک بود؛
میدونم پول دار شدن زمان‌بره ، ولی خب به این فکر میکنم که مامانم داره پیر میشه...
من چی کم داشتم که بهم خیانت کرد؟
برادرم که فوت شده، هنوز مراقبمه یا نه؟ دوسم داره یا اینکه واقعا ولم کرده؟
اینکه الان من بهش دارم فکر میکنم، اون داره به کی فکر میکنه؟
یه دختری هست که میخوام خوشبختش کنم، امیدوارم لیاقتشو داشته باشم..
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69756" target="_blank">📅 22:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69755">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⏺
ژنرال برد کوپر، فرمانده فرماندهی مرکزی ایالات متحده، در اسرائیل فرود آمد تا جلساتی را با ژنرال زمیر، رئیس ستاد، و مقامات ارشد نظامی اسرائیل برگزار کند. این مقام آمریکایی پس از برگزاری جلساتی در بحرین و امارات متحده عربی، به اسرائیل سفر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69755" target="_blank">📅 21:19 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69754">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11c35a859.mp4?token=H9Zm9KTeJ0rg9_L-tBTjX94tD0XbU42NAjfxhGy0th5zgT-VPTmNZk6X5ZNmXP40ppiAEdCB9RAXH57LubnOxDczs443O_Rx32jGeqTCH0VFPrAE9difSGEe-7R3ZmXGYunpg6rH3YxYpnX_cD9FhN8oFmdhEaGEjOGs2vxJg2xJN31PGQzT3Bh92fHbAhUotNpebX3inNwgj03Xf7v-3NtFWlLpvZTgAoKoMNWYOJD44KBp7qUmwMgo-u1htrcS9-sTjxObAcHdjldQrmRyh0VljZ37GjDPOiORzXhIQoECoRyfnpUB7B77l5i3cu0HeuJ4b-kylLA50b49XVvuU6ebPAjrfjTR6vS0_yzMaxrqxYTCSApjGkpIr6rQUd-aV6R1i_V5T7vP7ISnoK2CcDBoHxMeQfPngqwqeeMNZn9183iFja8hsjssG0LvblAkWfCUsjxfdtiWwCnY2cH4g5SfWMW5TE7PPIBkfkLSBCBrvSzMJ2AIditgoPovjm5dtKvE4Erle7Mw73xoab-vyTbV9LLw9I3x3G4aDulSZsMbeZN8sOscebyGpx1vDQG9EUoFCbaj6iwrfjEMFzMn9vabChBNTKP0aSKFYkXJCG28RFZhJA8o-8L6RPoDZocFV-ZTk9GYw28i4i-6i-dWUw21ly8uzVi8BMZGsytEgt8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11c35a859.mp4?token=H9Zm9KTeJ0rg9_L-tBTjX94tD0XbU42NAjfxhGy0th5zgT-VPTmNZk6X5ZNmXP40ppiAEdCB9RAXH57LubnOxDczs443O_Rx32jGeqTCH0VFPrAE9difSGEe-7R3ZmXGYunpg6rH3YxYpnX_cD9FhN8oFmdhEaGEjOGs2vxJg2xJN31PGQzT3Bh92fHbAhUotNpebX3inNwgj03Xf7v-3NtFWlLpvZTgAoKoMNWYOJD44KBp7qUmwMgo-u1htrcS9-sTjxObAcHdjldQrmRyh0VljZ37GjDPOiORzXhIQoECoRyfnpUB7B77l5i3cu0HeuJ4b-kylLA50b49XVvuU6ebPAjrfjTR6vS0_yzMaxrqxYTCSApjGkpIr6rQUd-aV6R1i_V5T7vP7ISnoK2CcDBoHxMeQfPngqwqeeMNZn9183iFja8hsjssG0LvblAkWfCUsjxfdtiWwCnY2cH4g5SfWMW5TE7PPIBkfkLSBCBrvSzMJ2AIditgoPovjm5dtKvE4Erle7Mw73xoab-vyTbV9LLw9I3x3G4aDulSZsMbeZN8sOscebyGpx1vDQG9EUoFCbaj6iwrfjEMFzMn9vabChBNTKP0aSKFYkXJCG28RFZhJA8o-8L6RPoDZocFV-ZTk9GYw28i4i-6i-dWUw21ly8uzVi8BMZGsytEgt8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
شاهنشاه آریامهر: اون روز دیگه من نیستم ولی حقیقت هست
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69754" target="_blank">📅 21:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69753">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcCQjBrph05YMpyFyKmBnkN-pBQ0khsTmMkcCCKbc-vV-E0WtPexYoThK_nFdwm8WhKNH58_Ta6YxdGXBD1MopzYyGJ2aqskQQ5Tu90UKW4PX9suFNLNomKdyTZbT4a0rtRvUkK9k8wKmTrpUwWBwCdav9MkqICQVAUAzEyivf6RmFMoMk6rUGbNEuxLSVT08eQYlI4dOI338mtBeGXZQBsbF8qRtToNfqfnKlDNVVWhTC1oOL_21dJ9G8UYq6dspH4T0-JnkddPxLw8dahII2BIrT6ngNDA9UyO5faQmhC9quNWnQHVaHUQImbzvPnlAFob_dWDZbUKnTSP4irLaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کانال ۱۳ اسرائیل:
اسرائیل خود را برای احتمال اقدام یک‌جانبه علیه ایران آماده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69753" target="_blank">📅 20:56 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69752">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1727b3200.mp4?token=nrF-MYdPvXYf1WKHMaGraKOaUW_1MlsLOnpHzuP2fEGxo6SDnXPgxmjXeA6hGvyv9vpwnDiP9GnGe-gl-yYesf5aif2Xg6uE67Aidd7fxp7DUL9q6IzAki8RBbaaK2AN50M8o1d5nG-oxX_tZC4U-6G_xrCzuDXJfGg5Xkl7xfLiPhYmbglyPvZaHTHq4zfdVNAWhkUj6K4Yxxl6P4MKcX-x6FKvMRkS2HiASWNG5ODdim19sdoxvplu3eic47NLztND5sq3uHoKpWr3GUzMi5fFn081BfVMMTEWl2KNtvdC6t5Cht7KxRTuB88xQmjCVB8YezsJI3R88tStpvMmOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1727b3200.mp4?token=nrF-MYdPvXYf1WKHMaGraKOaUW_1MlsLOnpHzuP2fEGxo6SDnXPgxmjXeA6hGvyv9vpwnDiP9GnGe-gl-yYesf5aif2Xg6uE67Aidd7fxp7DUL9q6IzAki8RBbaaK2AN50M8o1d5nG-oxX_tZC4U-6G_xrCzuDXJfGg5Xkl7xfLiPhYmbglyPvZaHTHq4zfdVNAWhkUj6K4Yxxl6P4MKcX-x6FKvMRkS2HiASWNG5ODdim19sdoxvplu3eic47NLztND5sq3uHoKpWr3GUzMi5fFn081BfVMMTEWl2KNtvdC6t5Cht7KxRTuB88xQmjCVB8YezsJI3R88tStpvMmOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حاجی‌دلیگانی، نماینده مجلس:
قدرت چهارم جهانیم و حق وتو می‌خوایم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69752" target="_blank">📅 20:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69751">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8f98a7872.mp4?token=XiO4VAyXoBCxMUJ8Xfvjd-jPanTK1jExyiyjs9ttuTYAnPfspQ1Wqv1SQf_vLrx7VBISo_g9niF9Z_Ggbb5bR0X-gQ4wF-OkrNnyI9kpwbQwmWIEwz_K_bdqQ-lDHjkwVKbeW5vzq_hjfF3VGXMCac9j6KwqLdd4YBvb8wN8q8-XGicb-OyKUXM-WZ6tT4xAmtFafIDL-8-1dLKiv_L-yY8q0dhELQzPFC3Df2CwVRydnOeQX13mr9q7XSTxGQwYtGq_Yzg3_SyWNMJvgZ1BK8OC-lp7GWeJNaXKSUp_yvZ_j99xgIP8PxIgssRBVhsMZxoUAFILM_KejqbQ7qHz5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8f98a7872.mp4?token=XiO4VAyXoBCxMUJ8Xfvjd-jPanTK1jExyiyjs9ttuTYAnPfspQ1Wqv1SQf_vLrx7VBISo_g9niF9Z_Ggbb5bR0X-gQ4wF-OkrNnyI9kpwbQwmWIEwz_K_bdqQ-lDHjkwVKbeW5vzq_hjfF3VGXMCac9j6KwqLdd4YBvb8wN8q8-XGicb-OyKUXM-WZ6tT4xAmtFafIDL-8-1dLKiv_L-yY8q0dhELQzPFC3Df2CwVRydnOeQX13mr9q7XSTxGQwYtGq_Yzg3_SyWNMJvgZ1BK8OC-lp7GWeJNaXKSUp_yvZ_j99xgIP8PxIgssRBVhsMZxoUAFILM_KejqbQ7qHz5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
معاون رئیس جمهور آمریکا آیت‌الله جی‌دی ونس:
در کنفرانسی، لحظه‌ای پیش آمد که من و یکی از دوستانم داشتیم درباره مسیحیت و مذهب کاتولیک صحبت می‌کردیم.
درست در همان حینِ گفتگو، لیوانی از روی دیوار پایین افتاد.
می‌دانید، فکر می‌کنم یک فرد خداناباور (آتئیست) احتمالاً آن را این‌طور نادیده می‌گرفت که: «خب، چه اهمیتی دارد؟ لیوانی از روی دیوار افتاده است.»
اما در آن لحظه، احساس کردم که گویی خداوند سعی دارد پیامی برایم بفرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69751" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69750">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b83cf8ea7b.mp4?token=BFKbjy7cGxlF3dthqcjZ-NmHKplz9ae725rvEjifGDfUVVFakR6iGtuOoqfwE6LDSydQOocMeOv06dPxz91AOwSrPYfFdlO4oiM53utR9Kc-iDXXor37ruh9PZ0PIccoPR6ttOv6ZgCF0rBYwkdRQKObdbkSEdmMilsohSnaLfEGfiDVN5BsKcRSaOi9BIf1MzZWPgdbPoxA18jLlHT4Clb08QCWLboARMLShjKwi9aSVH1XuK2Lg5omlna7HZ08-YQ56hfUPzlyj0MREFIWOisBGGJURmUqshRUZVpYHgDpY53cZSzFh8PSEK1mMq3YYRdAtupiFwtAlCjHMoXL1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b83cf8ea7b.mp4?token=BFKbjy7cGxlF3dthqcjZ-NmHKplz9ae725rvEjifGDfUVVFakR6iGtuOoqfwE6LDSydQOocMeOv06dPxz91AOwSrPYfFdlO4oiM53utR9Kc-iDXXor37ruh9PZ0PIccoPR6ttOv6ZgCF0rBYwkdRQKObdbkSEdmMilsohSnaLfEGfiDVN5BsKcRSaOi9BIf1MzZWPgdbPoxA18jLlHT4Clb08QCWLboARMLShjKwi9aSVH1XuK2Lg5omlna7HZ08-YQ56hfUPzlyj0MREFIWOisBGGJURmUqshRUZVpYHgDpY53cZSzFh8PSEK1mMq3YYRdAtupiFwtAlCjHMoXL1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداوسیما تصاویر مربوط به هواگرهای آمریکایی و اسرائیلی که توسط سپاه منهدم شدن رو منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69750" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69749">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69749" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
با این سایت به راحتی میتونی کل ضرر های جام جهانی رو جبران کنی
بونوس هاش واقعا عالیه
👌🏼
بدون قیدوشرط
❌
با هر 1 میلیون شارژ ،
🤩
🤩
🤩
هزارتومان شارژ اضافی بگیر
🅰️
❌
❌
طرح شارژ رایگان فقط تا پایان مرداد ماه</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69749" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69748">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0HRaVP2M_3fM6n_kNaYpf_okPyPBJxrfdqqikdtaGM0SgvchN0l8gvDrTrn1IEdxXcMTa_lIftug2UyShBmiD5T6TGVHUCAP9xHT6Q8qRv3O03XAWc0aSSUYGEOTABhHqXx5VMGdBo9qDL-cnJXPNSOaLuFjQUSuPjT8u3ru6WZSfRoZp_Nlv5SaGkbN01DprwMd2S1KJreHgkKGrS9E84bjp6hQ2SAajgxU4NOv1d1kzxO-1WHo7_yZZWfo5grUhbmjGJdpPrnCim7HV8KqIb_IKprE2hfQ8KGzw3A6PeJwlhGBVz_z6c97HtRPSs2d2XArI6UA5x2RTatU8xh8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛍
#اتلتیکو
Vs
#منچستر_سیتی
💰
🛍
#لیورپول
Vs
#موناکو
💰
زمان: یکشنبه ساعت ۱۴
🚨
تجربه پیشبینی مطمئن با
🤩
🤩
🅰️
شارژ اضافی و ریسک خیلی پایین در
#بت_اینجا
رو از دست نده
❌
🤩
🤩
درصد برگشت وجه در  صورت باخت:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g17
@betinjabet</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69748" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69747">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoG844ej1J99ph_VbGsnknkW_ApsBMj18SYGNhotpIA9-JHZSr9hk-YJ0NTe0ij3YcNYQ099E_1_RVMwMqoLakitT2byzM9JffPw1RbZwxs7Br7Cvasrrh8u33fdMVjAM3ZSMfd4zLNCpXr249s02UDCCA4567R51SiSotSMBg7l_lkS5NkrH1-0cxbiuPX_JSe2svhdBoUbC067QEwus0FogCgU-H6FlcJzHbo6JzrOe0SV4yFtAu_ebrG6WeGfsdlV9w1DqZwYk6JK0eebvCzWuJxEftZNdnn0zwSIQZgEJ1AOfbvD1uqusrdGplDefl8szoVkjgYUX01isTcYsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
بیانیه دبیرخانه شورای عالی امنیت ملی:
🔴
اگر ایالات متحده رفتار خود را اصلاح نکند، تنگه هرمز باز نخواهد شد.
اصلاح رفتار به معنای موارد زیر است:
عدم تهدید ایران به هیچ شکلی و به هیچ زبانی، و عدم توهین به مقدسات مردم ایران.
پایان دادن به جنگ و تجاوز علیه ایران و متحدان آن در لبنان، فلسطین، یمن و عراق، برای همیشه.
رفع محاصره دریایی و عقب‌نشینی نیروهای نظامی دریایی و هوایی از اطراف ایران.
پرداخت کامل غرامت خسارات وارده از دو جنگ تجاوزکارانه علیه ایران.
رفع تحریم‌های ظالمانه و غیرقانونی اعمال شده بر مردم ایران.
آزادسازی بدون قید و شرط وجوه مسدود شده و ضبط شده متعلق به مردم ایران.
🔴
اینها مطالبات مردم ایران هستند که در طول ۱۶۰ روز حضور مستمر در میدان‌های جنگ و خیابان‌ها، فریاد زده‌اند.
شورای عالی امنیت ملی هرگز عقب‌نشینی نخواهد کرد، نه در جنگ و نه در مذاکرات.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69747" target="_blank">📅 19:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69746">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CExtg6B1-AIa0jI6Mx14RkGUv9rAmCH8ZHotWaD2oRU28D0H3I5hlZfFya6syIQlQq6wCPUtbJMqEs3uA4IgdLf0YWnhGmhZgyG0Rui9dkLCR_kahKOfd982K8ctOnZJeBGsfoZmTuM3-T5yPOrhhKa1u2k2X0pBN_FBD5meaQIJgrdrbprx_yW9mxscKZeVtSit6nYM5L69VX8qBk8uogsX5b0GdOUNM-zriP96ZTZFnZ-WIWSh-jSRlGyNaoB39Hr6fAMtvBaYa2-5jLN6E-r34rNghXCROkJ0a-rcEnPOOTeZlq0HZmJvaoBwZF-XEyJ5IhtDuF87i1XGym7KCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69746" target="_blank">📅 19:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69744">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvSh9-ei-wyNstYxRsGPE0bWEb5Qj-dizQ1ZuhJt7Ur5k6xQhQImUx3bxrm4Oav2vt-LIHGxT80nLDnihnTtXFqm5gVJLyTct4ThikUxMCOIBWsPL_Ti-qahb7Zwzp0WBvh3itrlzJYb8236mOGAoOU2h8kt51znMdwCNiAquMfCPp9ms4KUwNknvJ9gMU_HO-BoXay6K9UG3nkFRYSM6V6H5PHucHkvRHyV190goHtL3qBEd6nFw0QX_bPc_4UlNPkB6v7LXCOqas4fVMNe2acxX8aKhz5MPBb6-75-RvpZOZxuHYFynW73jQFVTZxn8x6I8m_zqp67nh7L3es0ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک تایمز:
ایران فهرستی از خواسته‌ها را ارائه کرد که این موضوع، امیدها را برای بازگشایی تنگه هرمز کمرنگ‌تر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69744" target="_blank">📅 18:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69743">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhzWKiHu_nhpaR6VBlTuHTVKIgy5aoFRKYKjiOZSXnjqrRRwkCm-cHWnR_uKYHHCu6b6XPR8atsil_svDII1c5tbzjFkSYKW3uP6sU-NzTzQAyBt3zgU9koQRtDOIvItzVWpFcSGgaqRCBZnRswxTt3ugJbnFg-oDHU7VSxEDmt2zRPlkSAcImnpgppEi6JX-PuplIXDw8qgLdZaeG5StmNBAopq9BxoWWarYsmEjWeR_JcDdc1maQ-is8PMHnR_CINk3jKKSAlQm-C3x1fc3vTCVti7gOgT3rKni2FhvDe0qAIPgK5hdiHU98S2_T4W3AJIjceifqc2cmt6WZOjqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان حمل و نقل دریایی بریتانیا (UKMTO):
گزارشی از حادثه‌ای در ۱۸ مایل دریایی شرق خصب، عمان دریافت کرده است.
یک منبع موثق گزارش داده است که یک کشتی مورد اصابت یک پرتابه ناشناخته قرار گرفته که باعث آتش‌سوزی شده و آتش  خاموش شده است.
هیچ گونه آسیب زیست‌محیطی گزارش نشده است. کشتی و خدمه در سلامت گزارش شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69743" target="_blank">📅 18:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69742">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/43af7e53e1.mp4?token=c9vd6slvtRKPXlCf6Uip8ibbzbBn08mlEjr_bD6wI1BxZZJ-bzyd4MxPJxx6Bl8EcMG56pYWbgMnNakW0DYuv1UPvORNdBKZD7qaO0avCilpd73m3NrpbkJiwQfBzXOMDqwYs6INqLN3z5_xr5g6qeZiLbPusFwTskGYPxHXJ5I9xE4ejL2CYu-dx4dHsgtqR-ACt7LyTSyPS2v4Ma6feNj7oJ4FORAQMTUHFp4R0fkKy7OXBBOadFSe-ZbFj_N8JtMRyNGXl6e8jqYgBgSK8j3mKxcw2Ie5euA3pQhFuyLBTnOVQKYQX2Wh1WtjTd9eP4d7p9lm83uOnZFwjZK2lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/43af7e53e1.mp4?token=c9vd6slvtRKPXlCf6Uip8ibbzbBn08mlEjr_bD6wI1BxZZJ-bzyd4MxPJxx6Bl8EcMG56pYWbgMnNakW0DYuv1UPvORNdBKZD7qaO0avCilpd73m3NrpbkJiwQfBzXOMDqwYs6INqLN3z5_xr5g6qeZiLbPusFwTskGYPxHXJ5I9xE4ejL2CYu-dx4dHsgtqR-ACt7LyTSyPS2v4Ma6feNj7oJ4FORAQMTUHFp4R0fkKy7OXBBOadFSe-ZbFj_N8JtMRyNGXl6e8jqYgBgSK8j3mKxcw2Ie5euA3pQhFuyLBTnOVQKYQX2Wh1WtjTd9eP4d7p9lm83uOnZFwjZK2lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبتای یه وکیل مرد:
توی تمام این سال‌ها به این نتیجه رسیدم که نود، برای پسرا معجزه می‌کنه.
پسرا عاشق اینن پارتنرشون بهشون نود بده، اصلا هم براشون مهم نیست کجان، سرکار، خونه و...
من خودم یه بار وسط دادگاه بودم و دوس دخترم برام نود فرستاد، منم گفتم این واقعا محشره، مرسی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69742" target="_blank">📅 18:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69740">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RA4XGz0D4lfa88hgnlAx8cfFlot84QnEq2fYbafR7FOoQtgoL7gc2feUhHOLkq-DxUyfnh67qi9eoyGroKCkTvzdibJsnpsR6_VtBobUHKNgaFzCT7fj8nSIIzKb3tXpiMdlJG7clCBP7Qw1VE03XOJYHw90VapkiWOcIBsRz-qjtwZTcmOkV4jdcpBd7u7YtuQ7Ngbxuns6BLMCpJnk8zx6ohlimN8nJ2QDHS8fwnK6bM9D2XH8ZzXAEkzfX-UgigugnE6eDYJs1j15BaX2x1x71gflYYMg1W_SWgt8-Bn42VzVLD6wcDwiFmBRhijQSKB9p20AioXU3_fLkfD8Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c7e1449f7f.mp4?token=M3AElCJiHbDNyrjhAo0BfDFj17xifNRGwREnXpkHHTTh5WGlO0tbyKoL-NwFdR5mbGNQGc_g1ZFqd7xmF1f_rlxVLRkZF803Al63wA1gVa5M8mSmVefhnEGXRcupZafmL7Tbcd3_EkxSy9NgRj25kBtVGjHm87sP0hCHuOhp5Eg6T_GyBgZoAwdINqeMzab2JY9pQZtPOFT7mO4Tp102SmUveVc15ulCK_4QdxQvco7N2Ho5btrMu5f9MyceyKQ_J_5g3OEzxtFTSmNqTwR0z0u6wjsUSwa9Xq9UcmHpD0feJU9ldBtqSmnbtk8SZYlENkoqv99o2ZLxH4Ch4eMWRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c7e1449f7f.mp4?token=M3AElCJiHbDNyrjhAo0BfDFj17xifNRGwREnXpkHHTTh5WGlO0tbyKoL-NwFdR5mbGNQGc_g1ZFqd7xmF1f_rlxVLRkZF803Al63wA1gVa5M8mSmVefhnEGXRcupZafmL7Tbcd3_EkxSy9NgRj25kBtVGjHm87sP0hCHuOhp5Eg6T_GyBgZoAwdINqeMzab2JY9pQZtPOFT7mO4Tp102SmUveVc15ulCK_4QdxQvco7N2Ho5btrMu5f9MyceyKQ_J_5g3OEzxtFTSmNqTwR0z0u6wjsUSwa9Xq9UcmHpD0feJU9ldBtqSmnbtk8SZYlENkoqv99o2ZLxH4Ch4eMWRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی اوکراین به دو پالایشگاه نفت در روسیه
پهپادهای اوکراینی بار دیگر پالایشگاه نفت سیزران در استان سامارا را هدف قرار دادند که در پی آن، آتش‌سوزی گسترده‌ای در این پالایشگاه رخ داد.
در حمله‌ای جداگانه نیز پهپادهای اوکراینی به پالایشگاه نفت ایلسکی در منطقه کراسنودار حمله کردند که باعث وقوع آتش‌سوزی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69740" target="_blank">📅 17:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69739">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6b8444e04.mp4?token=q3y8WzwlTzzJXKXRthrO1YNzzh5LYk_PPNhAEipiUL-ebVXG-ic6-PEyAxP8Wu-P_nsoKiXv_eIOftZORZdeKYgao5OpnNCnT2Va0q-48lVVdKjXq2qO6w2Z-EZDUkngW4kfPqSZSKy6v1jFGWUZVm1PQCtwFrXWXa-XM-dTnXmVXiQwpsKdvvSJ8JIxCXhQ96tfW33uxkE_snqr_z9ElrZkzY2vx8MVkgw0y3DdUG029LtK5ANn7pXt8DxBxAGPgJ5ESWQRFfGOuX5yCuSPFzOa3gUOGhq_CL2dUy7c3i31SWxCC0i3nBtCFFN_Q7kIZltr7XqP81LRRSDMT2godS8VjOdUbC7o1yBYaESi44ileDsf_gzmoJhmuBpEPGhCnHIDcFMjLUFsNu-2busHDolJdq4fjt2vNpxxcJCHCx_H3OfWoYDLmg7sWRV6LRCqV4GbW3vawuQio8wd19Fa2_XSsappt72NxDi06FiHT9htgEXpyM_Wv-E009JKF3Nadqw0Lu5MHibcUKpdxc7v42ohbge8hiB73ElAWK2K47_v_7cpfQacpezv8LdLdXPzsnIEWCSwifvPDMxRpfKDyna35aQIhFJXPLIwDaOZrRxm0p1yDGo4x8FnrfQOdf9ilbHYVQ1QX4DVyPcedmLE0nEBKFqD6DClPXaZyN7_G9E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6b8444e04.mp4?token=q3y8WzwlTzzJXKXRthrO1YNzzh5LYk_PPNhAEipiUL-ebVXG-ic6-PEyAxP8Wu-P_nsoKiXv_eIOftZORZdeKYgao5OpnNCnT2Va0q-48lVVdKjXq2qO6w2Z-EZDUkngW4kfPqSZSKy6v1jFGWUZVm1PQCtwFrXWXa-XM-dTnXmVXiQwpsKdvvSJ8JIxCXhQ96tfW33uxkE_snqr_z9ElrZkzY2vx8MVkgw0y3DdUG029LtK5ANn7pXt8DxBxAGPgJ5ESWQRFfGOuX5yCuSPFzOa3gUOGhq_CL2dUy7c3i31SWxCC0i3nBtCFFN_Q7kIZltr7XqP81LRRSDMT2godS8VjOdUbC7o1yBYaESi44ileDsf_gzmoJhmuBpEPGhCnHIDcFMjLUFsNu-2busHDolJdq4fjt2vNpxxcJCHCx_H3OfWoYDLmg7sWRV6LRCqV4GbW3vawuQio8wd19Fa2_XSsappt72NxDi06FiHT9htgEXpyM_Wv-E009JKF3Nadqw0Lu5MHibcUKpdxc7v42ohbge8hiB73ElAWK2K47_v_7cpfQacpezv8LdLdXPzsnIEWCSwifvPDMxRpfKDyna35aQIhFJXPLIwDaOZrRxm0p1yDGo4x8FnrfQOdf9ilbHYVQ1QX4DVyPcedmLE0nEBKFqD6DClPXaZyN7_G9E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌐
تریلر اولین فیلم ساخته شده با هوش مصنوعی
!
فیلم Hell Grind
اولین فیلم بلند سینمایی است که تماماً و بدون دخالت ابزارهای دیگر توسط هوش مصنوعی ساخته شده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69739" target="_blank">📅 17:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69738">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWEAFvd9G3FGHrNMQC-3AP3wdSOPuaDHK3yX769DZta32JTzv6rgQZ0-xYemwgSbX1Lr4P4xfXU1FKkqm1UrWV7McbqhTY35rj_BRUj429e8GX4wieuWfbC_gWobniW8NSzmS84tFkTzN4eUYdc_I3FJ_uWJ719pVnwCEvUj6oqerOAy4G0_mwdk-4jsfPAHJ1flM2lVk75NP9x4pgEqi4-U7RvI9PqeK7EsyrhxLka83DhqSMdGhjBQodPNFzbe9n9POz0CkT5EKpYU1fwTmpksTd1-_9LOQgfPguuehxtun_Tcs71bONYXnSnIpbqck0vRx9FhJABe3C-qwVdGRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇦🇪
طبق گزارش الجزیره، ایران امروز صبح به یک تانکر نفتی دیگر متعلق به امارات متحده عربی حمله کرد.
این چهارمین تانکری است که متعلق به شرکت ملی نفت ابوظبی (ADNOC) است و تنها در این هفته مورد هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69738" target="_blank">📅 16:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69737">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a24c34d2da.mp4?token=LoZSritnq67ulT06u8wCi8491tS8pgX9UBsCjHrW4FZHqptkAcy9QbZ2BiUcySi2xgMmOgYiEEmPCJfT5Fu6hoSpIuM5aQARSUko91mY0oMvIwCWB8fobknNBsPKpphOHwJBjJpeOnVTgIrg5UTfwWNiy-Mlqelm4zO4q1cbR1PrmvciD4ZSU20Qdgg3PV04lQ3sXx_5Cg-0Pb_VVUBGJo1OKTdAGJ9EExC1nJVZyTRZqSrsCCeKsHQLasHDXHKnduSHHNagDsxjsy6ltYhdRC3f0Sb5T_YmVa8st1xY22ZlEvFkJrrePZ_R37Xb1naW4Lcafn7VCGSaZ0wcUK4P6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a24c34d2da.mp4?token=LoZSritnq67ulT06u8wCi8491tS8pgX9UBsCjHrW4FZHqptkAcy9QbZ2BiUcySi2xgMmOgYiEEmPCJfT5Fu6hoSpIuM5aQARSUko91mY0oMvIwCWB8fobknNBsPKpphOHwJBjJpeOnVTgIrg5UTfwWNiy-Mlqelm4zO4q1cbR1PrmvciD4ZSU20Qdgg3PV04lQ3sXx_5Cg-0Pb_VVUBGJo1OKTdAGJ9EExC1nJVZyTRZqSrsCCeKsHQLasHDXHKnduSHHNagDsxjsy6ltYhdRC3f0Sb5T_YmVa8st1xY22ZlEvFkJrrePZ_R37Xb1naW4Lcafn7VCGSaZ0wcUK4P6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های ظریف درباره سهم ایران از دریای خزر:
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69737" target="_blank">📅 16:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69736">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a9432f087c.mp4?token=Osx54qgmuQC-01J1C4xZzsJdpGk6oj1qZVfGC1GyqDTFt5ddLx0gK2E7iSCOP1Uwy5GydpE2KkFhqQIW81TYx2hdOjA_Ieatr-bEI-_HuMSYhepcXmczpNvBwSdyGT1Nvqh_7kSxwc1hnWTjV3vnYOGywx5pFL2SgasvNdcMroos_HiImWwx93bGwPR4pBIGjmsWpxBIRbfCKqp4g36pMSCln1jpzGTQluIfuU0Vfop4EUfzUCXnR9QR5HCr1RToOjsPRtQeIjPirb3ZpWjbwLV5174dmk_CisH6C5b4TWgPabro0nsNRUMNfCi2q0mFaiVxJLLiA2XM1sIma3CwTA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a9432f087c.mp4?token=Osx54qgmuQC-01J1C4xZzsJdpGk6oj1qZVfGC1GyqDTFt5ddLx0gK2E7iSCOP1Uwy5GydpE2KkFhqQIW81TYx2hdOjA_Ieatr-bEI-_HuMSYhepcXmczpNvBwSdyGT1Nvqh_7kSxwc1hnWTjV3vnYOGywx5pFL2SgasvNdcMroos_HiImWwx93bGwPR4pBIGjmsWpxBIRbfCKqp4g36pMSCln1jpzGTQluIfuU0Vfop4EUfzUCXnR9QR5HCr1RToOjsPRtQeIjPirb3ZpWjbwLV5174dmk_CisH6C5b4TWgPabro0nsNRUMNfCi2q0mFaiVxJLLiA2XM1sIma3CwTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه سکانس از فیلمای قبل انقلاب و داستانِ شب جمعه
😂
اسم فیلم: لج و لجبازی
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69736" target="_blank">📅 15:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69735">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷
🔴
⏺
‌وزارت خارجه جمهوری اسلامی : کنوانسیون خزر منافع ایران را از بین نمی‌برد
🇮🇷
معاون وزیر خارجه:
در پی تصمیم برخی کشورهای ساحلی، پای بیگانگان در حال باز شدن به منطقه خزر است.
تصویب کنوانسیون رژیم حقوقی دریای خزر به معنای از دست رفتن منافع ایران نیست.
این کنوانسیون حضور نیروهای مسلح کشورهای غیرساحلی در خزر را ممنوع می‌کند.
تعیین خط مبدأ و حدود بستر و زیر‌بستر ایران موضوعی جداگانه است و در این کنوانسیون تعیین تکلیف نشده است.
به گفته غریب‌آبادی، اجرایی شدن کنوانسیون می‌تواند چارچوب حقوقی و امنیتی خزر را تقویت کند
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69735" target="_blank">📅 14:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69734">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🇮🇷
سخنگوی سپاه پاسداران:
بازگشایی تنگه هرمز تابع سازوکارها و شرایط تعیین‌شده توسط جمهوری اسلامی ایران است و ارتباطی با مذاکرات ایران و عمان ندارد.
بازگشایی آن منوط به پذیرش کامل شرایط ما از سوی ایالات متحده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69734" target="_blank">📅 14:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69733">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
قوه قضاییه:
آیت‌الله خرازی به دلیل حرف های کذب و دروغش تحت تعقیب قرار گرفت و براش تشکیل پرونده دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69733" target="_blank">📅 13:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69732">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e778f30e9c.mp4?token=MQg27cd4hQ_cRYG-LJwXrqScNBQk_KMF6CuJBWCmneH22LYD4wl1mNNQh8NQHLSuKZ4TLpqk5UuthMCvKtiJxGnuyuSw_e-nWfC1X4Mc7WlIfu72KnVuIggO4MKUNhFid84ZiuSNkZb_56sG66ZPckCUBXO34vPbIa1v8Uon-fbTk5hgyxYDthVLwKHIr9sC0yQC1fxo-FOtIdU9cmSOM1BiJWlLZkhcU2l6DgUFuugP0HaZbxAnfeIz67SX55LdCktka0PmfDfZK2oZ8n6pjyH2KiFl2TWhAnZqWykwp8WvdEBIxj64DAav9x2w54jU_NIiImVq_HnL-Hk3vS7JrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e778f30e9c.mp4?token=MQg27cd4hQ_cRYG-LJwXrqScNBQk_KMF6CuJBWCmneH22LYD4wl1mNNQh8NQHLSuKZ4TLpqk5UuthMCvKtiJxGnuyuSw_e-nWfC1X4Mc7WlIfu72KnVuIggO4MKUNhFid84ZiuSNkZb_56sG66ZPckCUBXO34vPbIa1v8Uon-fbTk5hgyxYDthVLwKHIr9sC0yQC1fxo-FOtIdU9cmSOM1BiJWlLZkhcU2l6DgUFuugP0HaZbxAnfeIz67SX55LdCktka0PmfDfZK2oZ8n6pjyH2KiFl2TWhAnZqWykwp8WvdEBIxj64DAav9x2w54jU_NIiImVq_HnL-Hk3vS7JrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مقایسهٔ قیمت های سال 1400 با 1405:
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69732" target="_blank">📅 13:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69731">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_We2TFDX7ytShayT5Nv3QEw94LFXB1C1CuFMayZCeZeKdmrRcbhbJb8mQ4IxYsMi3dckoDi7qVfUmjRzBaRU-doguQHYz4ljrx-7VLfveGB07rLjilVKDP5SwelEmHimWULDPFfBhLMy2MUc2CVATBXoLxPWkDk2eQqnArZg2in8dZ5niytlZKQR0JMoBco5GiLW4WmfBrhSDiXEJ9mddAMU9TRjWFjtuhjg0BOLBRWAhnelPb56EA1_K2GvtiC18p5Yy9_oqgXspF-P-FbWDy_75pIZEpZWedvWa0LvxefgsZaohCPm5fQKkre22O75TNhD7Psr_GgRodFJl5v2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
تعداد زیادی از سوخت‌رسان های آمریکا از ایالات متحده و اروپا در حال حرکت به سمت خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69731" target="_blank">📅 13:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69730">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb80381b74.mp4?token=mX3N4-WMKBjUE8nyk4kYCn9xe2KWyOjFrnbGq-jkWbCJpfSHP-RmURCBpw0JgHkWCM3yNp11csCdUYLX2ijfOpq7FHA3oBmcbPXDr-UKnG0ewKsBNcMg-qiKf81iahrWl5qyWfUFF90fAOS_YS3YNQg7lmQ2g_Rde1Xh9PmZXCv4s4uZLSJG68csylAopnW834veZu6KcM6UUq2EVldA1rAH7SckAWJ902A3m_x6NR_CN4R6Z4kABkWl83ZVp1AE3xFKxBJcdpC3557zGYbL5WhULw4b65SzSLQdPiqRrmUknyZgpRyt03gmvLSELUrJBfmCjGvjXqYNnDvTAXN_ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb80381b74.mp4?token=mX3N4-WMKBjUE8nyk4kYCn9xe2KWyOjFrnbGq-jkWbCJpfSHP-RmURCBpw0JgHkWCM3yNp11csCdUYLX2ijfOpq7FHA3oBmcbPXDr-UKnG0ewKsBNcMg-qiKf81iahrWl5qyWfUFF90fAOS_YS3YNQg7lmQ2g_Rde1Xh9PmZXCv4s4uZLSJG68csylAopnW834veZu6KcM6UUq2EVldA1rAH7SckAWJ902A3m_x6NR_CN4R6Z4kABkWl83ZVp1AE3xFKxBJcdpC3557zGYbL5WhULw4b65SzSLQdPiqRrmUknyZgpRyt03gmvLSELUrJBfmCjGvjXqYNnDvTAXN_ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه آخوند
:
قبل از انقلاب باید شب و روز میدویدی تا خودتو خانوادت از گشنگی نمیرید،الان وضع مردم خوبه.
وسط جنگ با ابرقدرت ها واسه خودشون میرن تفریح و در آسایش و آرامش و کاملا شاد هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69730" target="_blank">📅 12:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69729">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce1bb2a9c.mp4?token=qg88NjHduFR4zuxEyT4sXRL7YLToQYB4WMzE-k7EFCRcT1u0drxQQ7yJgiXVRhxsWF7yGPiVTbKdMUg1UG2zMNzSx8k-MCGvScwlsP2Ys2NgWEBz4RmcoaaOAfkm0phiUSPwM09V81PVpaBrYrdr-ZvAbDp_WHFN0C231H3dc-0fwOEGztlh5RCOlcUU_6D6TF7KeRSMKMDwLvHDKJ0yfMf-HVIomAlUWHpUwxsnxSo-tkpQRRtXOvp6vsYxme6GXAxILfT0q6VWl7HYvwq3EungRc8Fc2I1xLQoLzMzt3KdvcbDVqOi1mHvnomM7pNZVFr41LY8Br5NjEDLwkUIBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce1bb2a9c.mp4?token=qg88NjHduFR4zuxEyT4sXRL7YLToQYB4WMzE-k7EFCRcT1u0drxQQ7yJgiXVRhxsWF7yGPiVTbKdMUg1UG2zMNzSx8k-MCGvScwlsP2Ys2NgWEBz4RmcoaaOAfkm0phiUSPwM09V81PVpaBrYrdr-ZvAbDp_WHFN0C231H3dc-0fwOEGztlh5RCOlcUU_6D6TF7KeRSMKMDwLvHDKJ0yfMf-HVIomAlUWHpUwxsnxSo-tkpQRRtXOvp6vsYxme6GXAxILfT0q6VWl7HYvwq3EungRc8Fc2I1xLQoLzMzt3KdvcbDVqOi1mHvnomM7pNZVFr41LY8Br5NjEDLwkUIBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📰
مراد ویسی تحلیلگر ارشداینترنشنال: جنگ جهانی سوم در راهه!
هر چقدر اتفاقات و شرایط رو بررسی میکنم، دقیقا مثلِ قبل از جنگ جهانی اول و دومه.
توافق و تفاهم نامه همش کشکه، هیچکس تو خاورمیانه حاضر نیست سلاحش رو تحویل بده، یه جنگ عظیم و جنگ جهانی سوم در راهه!
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69729" target="_blank">📅 11:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69728">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41f0d554f1.mp4?token=INzTWqWu7zbu5fnz89Fo3k4uloAeKHZA4K-Xo6DSyicmczWgk7LwQmzJyxvCyzZzawrCcZeIvgablgFluHBh_EnUsSPxoBHvx40L3jiqWC6A0U_QTBpOgx5Um-x9l-OZWSH57GYNE76e8N67c1AYiHHZGMyzwM0d8Yoit9DSFi48CluVTr7hkAHQGAG2j6_0fr-qTFrCN_opxAbUnKMJgFOobWIMZjkf6VELpR_3U_il6LEvh_tUebL2mzUe6LhQ9dPrBK7Q1KUjyG9KPPTIzAvYoT-yRFmGHhzKxulMeWmrbDxVAynXhcgzQNdFTjO4vuimMGJvO6JYqbUC9qFmfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41f0d554f1.mp4?token=INzTWqWu7zbu5fnz89Fo3k4uloAeKHZA4K-Xo6DSyicmczWgk7LwQmzJyxvCyzZzawrCcZeIvgablgFluHBh_EnUsSPxoBHvx40L3jiqWC6A0U_QTBpOgx5Um-x9l-OZWSH57GYNE76e8N67c1AYiHHZGMyzwM0d8Yoit9DSFi48CluVTr7hkAHQGAG2j6_0fr-qTFrCN_opxAbUnKMJgFOobWIMZjkf6VELpR_3U_il6LEvh_tUebL2mzUe6LhQ9dPrBK7Q1KUjyG9KPPTIzAvYoT-yRFmGHhzKxulMeWmrbDxVAynXhcgzQNdFTjO4vuimMGJvO6JYqbUC9qFmfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
نویسنده امریکایی
:
ایران مهم ترین مهره روی صفحه شطرنجه
!
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69728" target="_blank">📅 11:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69727">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
نیروهای ویژه دریایی اوکراین از تاریخ ۶ جولای تاکنون، به ۲۱۸ شناور در دریای سیاه و دریای آزوف حمله کرده‌اند. همچنین، بین ۱ تا ۸ آگوست، ۱۲ شناور دیگر از ناوگان سایه مورد هدف قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69727" target="_blank">📅 11:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69726">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69726" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69726" target="_blank">📅 11:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69725">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc7f1c8ee4.mp4?token=tuys0t58Sr7nKgwyjbtkT7TGYgxcGDEyvz6Pk37PKuBLCZn73rK3CGqbg-4PFF42p_hQdmxdpbiRAtPmojbs7SdFjYc9oI-WM238KaQBN1PZgcODkGisvfIolyStWjcjS9ylJPrwKAu4mqlxVqER7DyFU2kAKUjMpLzq0YXMJOVhUDos5zgJPO-FMSUOT7OKynD0TXTIo5DLIG5hui_umCP4pQ82yPlBqhFukJ2k90WhsZTueGPXpnCaOp_nVsA4VvMqGujz7AmDk2i7CJTZf9msOdRAbdKu9NoThwYzHrM-vkwNdJUTl6TFL-xz8WWJaURI3zwdDc9NXDhYo7MiBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc7f1c8ee4.mp4?token=tuys0t58Sr7nKgwyjbtkT7TGYgxcGDEyvz6Pk37PKuBLCZn73rK3CGqbg-4PFF42p_hQdmxdpbiRAtPmojbs7SdFjYc9oI-WM238KaQBN1PZgcODkGisvfIolyStWjcjS9ylJPrwKAu4mqlxVqER7DyFU2kAKUjMpLzq0YXMJOVhUDos5zgJPO-FMSUOT7OKynD0TXTIo5DLIG5hui_umCP4pQ82yPlBqhFukJ2k90WhsZTueGPXpnCaOp_nVsA4VvMqGujz7AmDk2i7CJTZf9msOdRAbdKu9NoThwYzHrM-vkwNdJUTl6TFL-xz8WWJaURI3zwdDc9NXDhYo7MiBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
اگر
#تندو
تیز هستی اینو ببین
💵
💰
✊
این بازی فقط سرعت عمل بالا میخواد
😍
🟢
ویدیو
#آموزش
بازی AVI رو براتون گذاشتم خیلی راحت با سرعت عمل بالا بدون ریسک کلی پول دراورد به همراه
🤩
🤩
% شارژ اضافی
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r17
@betinjabet</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69725" target="_blank">📅 11:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69721">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dab2dda1d.mp4?token=BdVszowdbaUdd1D8bkCTpSr9nNYDPynCKdkRdl4VgSL-hLsf0TowwAHGtOhLGxDZI_4CGIXlXwuN6Z4aLuo8p6HvDV_IjMvsQ-nyQ2K4vrFA5YIxhGb2M2otg2cAAjQLaFV8j-uJjRHTZ_0RdtMPhNR1GQZ6JJ_1QUbgevL5-zUztf0gbj04uIAzABlA1NMitBpPYyTGytaISPDzjr2fkJEe6PxoNL7HUaQC7AUy9IGFIGnCFHjUOopBq5Fh-YuaXO4aIQty35-kF1lfQyG3xa6JqUSzDXEHysVHzKa81sVlI8QWsaEQQaOnR0a2FlApliTun-p4BXT-_unSKw_nCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dab2dda1d.mp4?token=BdVszowdbaUdd1D8bkCTpSr9nNYDPynCKdkRdl4VgSL-hLsf0TowwAHGtOhLGxDZI_4CGIXlXwuN6Z4aLuo8p6HvDV_IjMvsQ-nyQ2K4vrFA5YIxhGb2M2otg2cAAjQLaFV8j-uJjRHTZ_0RdtMPhNR1GQZ6JJ_1QUbgevL5-zUztf0gbj04uIAzABlA1NMitBpPYyTGytaISPDzjr2fkJEe6PxoNL7HUaQC7AUy9IGFIGnCFHjUOopBq5Fh-YuaXO4aIQty35-kF1lfQyG3xa6JqUSzDXEHysVHzKa81sVlI8QWsaEQQaOnR0a2FlApliTun-p4BXT-_unSKw_nCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این روزها قبل از ورود به هر بالا پشت بومی، سعی کنید در بزنيد؛
چون قطعا یکی اونجا هست که داره سعی میکنه سیاه بشه
😔
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69721" target="_blank">📅 11:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69720">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aa229942a.mp4?token=Ix_ASiAs7FSgva_9TK8Ehm0mb5R1cuZ2sTTsbPag22xjQfZ5prCHgIYUTcwVKxELKVtkHt0QUGEEDKOo2gB7zTKAIfH3f4mtsIrI-nETCxnBTEtHLRABpKNmi0rcenkEwU0tbW_m9VTJAGYQ4vX41aKwxxzL4YR6mwOCtExtIyyfCMlqeYutdOie68jul7DRI68Ol8Wmrr0B_DEkIg5sRzgCRdzhj7CDemDraX5iA-cwPGI6Yusg7JD_wgzdSsfE3jv0CXKdPUmytDeS9iAz9k22orRXLoNtyhkYbEsToOuTaXFmyGx4Ncf77jtXWfNst9jYEf-P0nPYw7P-xIUPwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aa229942a.mp4?token=Ix_ASiAs7FSgva_9TK8Ehm0mb5R1cuZ2sTTsbPag22xjQfZ5prCHgIYUTcwVKxELKVtkHt0QUGEEDKOo2gB7zTKAIfH3f4mtsIrI-nETCxnBTEtHLRABpKNmi0rcenkEwU0tbW_m9VTJAGYQ4vX41aKwxxzL4YR6mwOCtExtIyyfCMlqeYutdOie68jul7DRI68Ol8Wmrr0B_DEkIg5sRzgCRdzhj7CDemDraX5iA-cwPGI6Yusg7JD_wgzdSsfE3jv0CXKdPUmytDeS9iAz9k22orRXLoNtyhkYbEsToOuTaXFmyGx4Ncf77jtXWfNst9jYEf-P0nPYw7P-xIUPwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، (مرداد1397):
همه ما انتظار داشتیم ایران درخواست پنجاه درصد بکند. قانونی هم بود.
اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین پنج کشور، یعنی کمتر از بیست درصد.
برای ما عجیب‌ و غریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69720" target="_blank">📅 10:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69719">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKuh81vodJhTM1Y30oMy-PDcPiuyaK-oHHPCrrOS_SZaOqRUR3fi8uAG9hiezNRaFWbWC9VrI5f6hSy-mQpwygbnPbzOAwfAK9RHyOW7oUn3IktyMYE7ODhlWOH874uAEA4vGuMbKeQPCmHpNXYa_7-78jJHfpx45uQPWIHgJ3BI_7-_uAU9uW1RPphtl8Oq69sNo6h4ncA_N93I3MLQq53deMNjvWRREnOF_2c6r9RlMvRs1CtJ0DkEHSl_fecC6YpB0ZBy9axtAv79Zd3ZPOpAx0QlcKudzwJ9YvVfxsGDXB3eWYWvSF5vFmwkGybbRBQ0PIP6Lacmfs52JYQERA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه ساعاتی قبل یک کشتی دیگه رو توی تنگه هرمز هدف قرار داده؛
گزارش‌ها حاکی از آن است که ایران به کشتی‌ای در تنگه هرمز و نزدیکی سواحل عمان که قصد عبور بدون مجوز را داشت، حمله کرد
ه
است.
یک شناور تخصصی که برای مقابله با نشت نفت و اطفای حریق طراحی شده، در منطقه‌ای که نفتکش هدف قرار گرفته، در حال فعالیت است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69719" target="_blank">📅 10:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69718">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9bc484b9d.mp4?token=PHis7DuQEa9slkCrtJZrhDN79jM_rb5VV5HmLNgw5Btv4p4jEdKRyE6fKGzgUHOX60cQY2aBxQH3RXCFmPqXt9EreZR54mh65LLcDjm0QOcx5qRnUi2ikHWqs_t9Qae22qxFxeANOr6D7sLNoQhE_HrJ9XaA4izVHJc4RGXJqjZruagYGtN_owq3mzMQDQEdLXhl82r-eBihkBoNTFPoV3Tv0u_hBE1rLhvLwa-kqwj8cPcRpObWVEe2dCY1a7oCrEaX89dMlhZ_UrNtqozIcl5RmJQkajwrMEN9UnexcbpHJlMGo5pkqWQLzuldfEzV-nQ4vPAY_ZkqRBFrp7itzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9bc484b9d.mp4?token=PHis7DuQEa9slkCrtJZrhDN79jM_rb5VV5HmLNgw5Btv4p4jEdKRyE6fKGzgUHOX60cQY2aBxQH3RXCFmPqXt9EreZR54mh65LLcDjm0QOcx5qRnUi2ikHWqs_t9Qae22qxFxeANOr6D7sLNoQhE_HrJ9XaA4izVHJc4RGXJqjZruagYGtN_owq3mzMQDQEdLXhl82r-eBihkBoNTFPoV3Tv0u_hBE1rLhvLwa-kqwj8cPcRpObWVEe2dCY1a7oCrEaX89dMlhZ_UrNtqozIcl5RmJQkajwrMEN9UnexcbpHJlMGo5pkqWQLzuldfEzV-nQ4vPAY_ZkqRBFrp7itzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شادمهر عقیلی، قطعه‌ی گل یاس از البوم مسافر رو که سال 1377 منتشر کرده بود، بعد از 28 سال دوباره بازخوانی کرد و تو اینستاگرام منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69718" target="_blank">📅 09:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69717">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0959732695.mp4?token=e23Lq6PXzqgIQPDBOZCeen3aTGQQUhKWIuM6xMrG3NZImV81J3H8ycNAdEl20rhszRDk4pxZ5EmFnw_UqNMNS4deWs83TKV75sY_5S72SaJlOACcMKuZk8-Zzvz8tPlWei6EF03Yvxo_z07InCoxRseT4enmGwXFwcnivzu3MQC8S2mFMIQl1nqQP8on1k21zJfCjsJ-qxS24nzuxMwEpvNIGQ4dAXTH7vwd2nmreRjiARx5OUj2CCpZRNxXDsW6YH_mPRMxWj7xkeoSUfYmU-DIKLzwHouGgPMgbwNuhLRmROUK0QHAIAtuxRGFnB1v2rLhxPsxaqC5tDKNUNlSbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0959732695.mp4?token=e23Lq6PXzqgIQPDBOZCeen3aTGQQUhKWIuM6xMrG3NZImV81J3H8ycNAdEl20rhszRDk4pxZ5EmFnw_UqNMNS4deWs83TKV75sY_5S72SaJlOACcMKuZk8-Zzvz8tPlWei6EF03Yvxo_z07InCoxRseT4enmGwXFwcnivzu3MQC8S2mFMIQl1nqQP8on1k21zJfCjsJ-qxS24nzuxMwEpvNIGQ4dAXTH7vwd2nmreRjiARx5OUj2CCpZRNxXDsW6YH_mPRMxWj7xkeoSUfYmU-DIKLzwHouGgPMgbwNuhLRmROUK0QHAIAtuxRGFnB1v2rLhxPsxaqC5tDKNUNlSbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مسعود پزشکیان:
تا وقتی میشه حرف زد چرا جنگ؟
ما با همین گفت و گو تونستیم جلوی جنگ لبنان رو بگیریم. (اسرائیل از همون موقع تا الان تقریبا هر روز داره لبنان رو میزنه).
تونستیم محاصره رو برداریم. (ایران درحال حاضر تحت محاصره دریاییه)
تونستیم پول‌هامون رو برگردونیم. (هیچ پولی از پول‌های بلوکه شده به کشور برنگشت)
تونستیم قسمتی از تحریم‌ها رو حذف کنیم! (درحال حاضر تحریم ها بیشتر از قبل جنگ شده)
بعضی‌ها تو داخل کشور فقط میخوان که ما بجنگیم
،
اتفاقا اسرائیل هم همین رو میخواد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69717" target="_blank">📅 09:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69716">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👑
آخرین مصاحبه شاهنشاه آریامهر محمدرضا پهلوی با دیوید فراست (پاناما1980) زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69716" target="_blank">📅 09:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69715">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69715" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#گل_با_پوچ
راحترین بازی پولساز
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید راحتو سریع برنده شو
👌🏼
💖
مرجع
بازی های روز دنیا در ‌پلتفرم جهانی بت اینجا
⭐</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69715" target="_blank">📅 02:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69714">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15f45ab1f.mp4?token=JqoTXBvolPyV-7J42hZE788ZpD6tuqtHe0V4ejJHwcjhPu7zj-0qg6gt-sZ-GYHe2-1Zzy4xMwji9I8mzcmSIPF33SCyGVDTFxn5IetKWoZ11ypwVMSpdKgAc6zNvIsaOdA9ZxgHDNjQFVkH_2se_c7EnabcKsNvPJf-mKigIhcyu9d8ac_lYy2YyVCtjAVviq53XUN_uQKbmUhEIx6ZwlVK2t9gZncQ71hrOTO-CGEOFe7OsuGmLMUfZGvgVQ_Ns4Ihl8N0ac9aiKzkk77pos7hqhh9xG2p83tKbnL1m3jaKOI15z7H5IfERHLHN2_guLqeJot_1Y0IWmv-Em1tpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15f45ab1f.mp4?token=JqoTXBvolPyV-7J42hZE788ZpD6tuqtHe0V4ejJHwcjhPu7zj-0qg6gt-sZ-GYHe2-1Zzy4xMwji9I8mzcmSIPF33SCyGVDTFxn5IetKWoZ11ypwVMSpdKgAc6zNvIsaOdA9ZxgHDNjQFVkH_2se_c7EnabcKsNvPJf-mKigIhcyu9d8ac_lYy2YyVCtjAVviq53XUN_uQKbmUhEIx6ZwlVK2t9gZncQ71hrOTO-CGEOFe7OsuGmLMUfZGvgVQ_Ns4Ihl8N0ac9aiKzkk77pos7hqhh9xG2p83tKbnL1m3jaKOI15z7H5IfERHLHN2_guLqeJot_1Y0IWmv-Em1tpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
#آموزش
گل یا پوچ آنلاین با افراد واقعی
🟢
حتما وبدیو آموزشی رو‌تا انتها ببنید راحتتربن بازی پولساز بدون ریسک و بدون پول گل یا پوچ بازی کن
با هر شارژ
2️⃣
1️⃣
🔣
موجودی خالص میگیری و با موجودی اضافیت میتونی کلی پول دربیاری
🔥
💻
آدرس سایت مورد
#‌اعتماد
ما:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
a16
@betinjabet</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69714" target="_blank">📅 02:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69713">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DyweP3pIWQT3yaRbh1Ik2jnZ5ZQmqcHLADs_dIDo8_KFO6rjf-e1eCkpmJBP8cln6wkq3qNTjrT6MX-CYugaE3ryby4Fo9S8UYVLrh2zWDugIg2m0T-hX2ggIFFD_WQD-Q1qUAfSj8Rpl1bcBtfzBMzKmstI7cH-Sc9hcLxFT4AK1DyLbdlxDyGjV9qYD5MiOoZivjeTeKhlIBF94fIF-LlC_lk3X0mP62EKxabhUTYQWAj6b2FWMKunglGeZXZ3Vej0IEs_hVgW04AcE9BVj1wbqQf3uDzQDdxD3so2UprGOSwlNKv93UKmEdMDcyAxVmD0hQst_QQR2mrc-NeapQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت لارا لومر در جواب قالیباف:
"جمهوری اسلامی رئیس جمهور ترامپ را مسخره می‌کند!"
یادآوری روزانه شما مبنی بر اینکه مسلمانان بازیگران بدذات هستند و نمیشود با آنها مذاکره کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69713" target="_blank">📅 01:40 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
