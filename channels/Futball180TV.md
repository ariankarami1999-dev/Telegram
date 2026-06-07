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
<img src="https://cdn5.telesco.pe/file/VgNbf-e1ZHXDCRREoYooY-RC33BOoPlCj2W1jKXwT58HOf_-KZQNoJYpHJ9IMm5zr2kIbNdWaxzh_icZ3oe3DSyZJQKuT1HYmRwWlJJUYZ03VAEyesLwB-P2ep3t-KRO3LuyYSBvwa-qXVQfzRycYn5tm1xEhuLgviO-JabNdBbNAudgvMBU6c8rzK6o0FtRPvd-v0zUziZT_YTINCDe1G1xyAEChC08UbQFaBZdaPv6PkGMfZdre3Hyx9csnyZmr9pdzXvf1GguUzfBVcmZc_oTG0Udc-Tjgs9mv2BUqX6EwG8vecQR5fY3W6MKK4K-hDClRrzedsv9n7mE67iCwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 249K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 22:38:20</div>
<hr>

<div class="tg-post" id="msg-91373">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664dea4d38.mp4?token=j8_YvJ3yhRdp6J3ZJSJV4XrfmqBhdO4uVD0pd29yD_K9i8Fwo3MizoR3Gfj7iCQHnhR4db9S67x-pZDC7_5gxHFAPoI8psHwpjchG5GHXCGuKjf3BCz0dJOBKEbM5zupvqN2B5V9qxtPDjvB1Hcyg9F8QsvLR1PamtNna3NWFOwXyYPDuKyp6r9Om4ajhnAawTcsCvXWpvaA52SH-ps614N6g-8WBeApa3ExP296952KBvJx_it6NRDJDrdt1nR2glCYtqRATu2UR-FyzsCMebnaW2fgAhitHfmB46gaXW74QD5oNZ1cGfzWvAWxGsJld5cU0ZFg2JPYPA4nUFRdWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664dea4d38.mp4?token=j8_YvJ3yhRdp6J3ZJSJV4XrfmqBhdO4uVD0pd29yD_K9i8Fwo3MizoR3Gfj7iCQHnhR4db9S67x-pZDC7_5gxHFAPoI8psHwpjchG5GHXCGuKjf3BCz0dJOBKEbM5zupvqN2B5V9qxtPDjvB1Hcyg9F8QsvLR1PamtNna3NWFOwXyYPDuKyp6r9Om4ajhnAawTcsCvXWpvaA52SH-ps614N6g-8WBeApa3ExP296952KBvJx_it6NRDJDrdt1nR2glCYtqRATu2UR-FyzsCMebnaW2fgAhitHfmB46gaXW74QD5oNZ1cGfzWvAWxGsJld5cU0ZFg2JPYPA4nUFRdWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت پیوی کانفینگ فروشا بعد از اولین موشک:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/91373" target="_blank">📅 22:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91372">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بابا من تازه ۴۰۰ ۵۰۰ تومن برای نت و کانفیگ هزینه کردم
😐
@Futball180TV</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/Futball180TV/91372" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91371">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مدارس و دانشگاه ها و مراکز دولتی برای ۳ روز تعطیل شدن!
احتمال حمله اسرائیل؟🫪🫪
@Futball180TV</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/Futball180TV/91371" target="_blank">📅 22:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91370">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">چرب کنید حداقل ۲۰۰ تومن قراره بره رو قیمت هر گیگ کانفیگ</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/91370" target="_blank">📅 22:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91369">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UITmPPJ5WdfxpPUaseqhTEysIJIlbPazDSnXGuQFVK_9Hvw8NuX5XbiH--o2-XockIsR05qFpDFr9fOVQS_MwSEii7UQ3bC_O-ycgPYhwOpX3rH2R__1kpZCgvFTDQm1Tm1zltwAF_tVqZxTFXCxURWe9h4NrjB6S-XUyVYj6oRf0aJt5kMXqZiyMc4i7kIq2Htiam5njxNLmYI7DMJwWUkc1NLdwb0xbaLaLVDM_bWaYwlYzm4j4EvyngH1_nlhr1V5a9V6JrTT20IPlZPVKPGbM9UQzs9OhQ6oh9_97WA5R5DTLQYTmd2Xls-521wPHHnSeGmbPHa3qPdMTmHaMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووورییییی</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/91369" target="_blank">📅 22:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91368">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
فووورییییی</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/91368" target="_blank">📅 22:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91367">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15acd81b3d.mp4?token=NP-9JG7cO7148z3fHwVLFiUML1Rq0rnx5ApYMyJP2sHMAhNa3OIZSCFqCk5EXAxOLxguF8URvvrk3OJ0E6_bbbC0OS4yh8uUkYH8cZmjlAHWTJB3SJ2aHeEZStunEh4dQmwemPAIoHTgIPxMa6YS5PBNZJUc2B3jEnrsrE656KbyTF2ACuKbn-I2YCRHMjNpvmzPHUhc7LAa7-2nGqYEkuQJMA_bcvB6K4DP84tbWAdkAdiXJ9dXBkWK4UZUnO8GpCsnbNC2IJFND1S2FDR241eqHVvgiKJMk7X079eYZPx_BpjnYzdK4yam9bGjX-qqhRUUc5DpqUjcmSRCJDfNNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15acd81b3d.mp4?token=NP-9JG7cO7148z3fHwVLFiUML1Rq0rnx5ApYMyJP2sHMAhNa3OIZSCFqCk5EXAxOLxguF8URvvrk3OJ0E6_bbbC0OS4yh8uUkYH8cZmjlAHWTJB3SJ2aHeEZStunEh4dQmwemPAIoHTgIPxMa6YS5PBNZJUc2B3jEnrsrE656KbyTF2ACuKbn-I2YCRHMjNpvmzPHUhc7LAa7-2nGqYEkuQJMA_bcvB6K4DP84tbWAdkAdiXJ9dXBkWK4UZUnO8GpCsnbNC2IJFND1S2FDR241eqHVvgiKJMk7X079eYZPx_BpjnYzdK4yam9bGjX-qqhRUUc5DpqUjcmSRCJDfNNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به نظرتون کدام تیم قهرمان جام جهانی میشه
☺️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/91367" target="_blank">📅 22:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91365">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SB4YW-17dXFX-vxl6BYO1X-E-VxOzC-toiuJwgrzerGQjIZcbKpvULvtFtTJvCL1qa0m4mh18oWaxbVr7X24skA7Aox_sVf6ICATOUu-fSwHjkMZ7u14WBLfW6_gcf4Vshh3GS5bTPK4p9y0z_iablsl44qHQntdB3FBnsJLtWr6HOpQBIqDJrWXNlvM4UimMoLL4tlHpxok3pgLJ1q-aGUnBHFTumkWSjxxDflaDYPiEIMEkLEP08Ci9ICWZDYR0BCOvmE6QBbjXTp0oiU_UZzs2_ah_pIhz0gXi3Ewpxy3tr8m6UzMGVoYL7SJxYp7JzHYBMBySOrxC3YaDpfVPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/475c525760.mp4?token=KOOA3A1eKJLXT2eO1P7nlK-8HGC1OLB8CDVleQ5vXxjqWauB6zVaamMe2Bc27mBCzzK46KGitJYIJliWtrH2p91u1Wx5OLg2zIS1A-q_QZCyhWpTur1weefXrRIvxFbjO8bPE9TDSTu3-AI7gIr28l_r0XDET-AMJcFO6YoSZk2jvGOantO_onGuAIbFyFDTccSAcn0q1LbyTVaeqzMdKD7Ip51BxoHxlKaPQDtpMISy2jCjl6nGJo4VPwEQNlBZjW5VBBUuKouollBCxhXRl_vTlXqHy1JP0FadjI8myaWx-zCZV9yY4fTkaBXZ_HfI9H3nwFK7QHuO6h2eQDxa8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/475c525760.mp4?token=KOOA3A1eKJLXT2eO1P7nlK-8HGC1OLB8CDVleQ5vXxjqWauB6zVaamMe2Bc27mBCzzK46KGitJYIJliWtrH2p91u1Wx5OLg2zIS1A-q_QZCyhWpTur1weefXrRIvxFbjO8bPE9TDSTu3-AI7gIr28l_r0XDET-AMJcFO6YoSZk2jvGOantO_onGuAIbFyFDTccSAcn0q1LbyTVaeqzMdKD7Ip51BxoHxlKaPQDtpMISy2jCjl6nGJo4VPwEQNlBZjW5VBBUuKouollBCxhXRl_vTlXqHy1JP0FadjI8myaWx-zCZV9yY4fTkaBXZ_HfI9H3nwFK7QHuO6h2eQDxa8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثر هنری خوشگل و ناز آدولف کروس تو جام جهانی مقابل سوئد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/91365" target="_blank">📅 22:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91364">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7uy2q4g8TQ81AU7zuScR0IFXjjgLd4N-sOsBiu6u4oiWm9Q0Paw4QMt_uTdztfF42m5M-RvYYZBSHYCzItc9cZQx7s5n9kL772ebcyTrVaG7faa5va6P3n9w_CBFB6jYaG6B2FjsDynAyFL11v35VCbehVs8OIqCB94ExugWjr-jx9_t0Zee6i0HPKAuIVj3BdgrKs7vLdjohJXY7xc7ULQDFlOruqD2uurYfUKre7k93HZHx1pR5pggRWtrjAAMSgavDksVJ3q4RGScxHZT45-mD6wpyzAej6er7QCrC32OZsoBk06j3dXnKcS5pY4cTfq-zqHSZt7P-QI81Cpdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
10 شگفتی بزرگ جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/91364" target="_blank">📅 22:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91363">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlNB1Y3qE9XNYKDLknyGP6jRvh0NvV3es-R94KL_054wUVPJGXmZfggrv_KcOyJEjXtnli0kOosimAWgF6MOgKvGQrdbsZVFB-qv-gLXfC5aSzvecozAIYWsDmNYIA1jFUIgUFQHHCrpRlG-Z-FPIcopMLRM0H1Yry_ALtLWUQ4CmKJkPdG0q04q10eENWPxzRwU9LlPCjGQIHOa4G0G72pup8dEHUoHYOSIBnH9IzQx0XvhhYqENWD8hGz0Jz74LsGzheto1BPU7Qd2wVVhFN4biv8jQtrKsbobBc4vErrGZ01FKz-pRXO3QOBX-54HfPZc-q8QjkAyMshYVNgywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰۰۶: حذف شده توسط آلمان
❌
۲۰۱۰: حذف شده توسط آلمان
❌
۲۰۱۴: حذف شده توسط آلمان
❌
۲۰۱۸: حذف شده توسط فرانسه
❌
۲۰۲۲: قهرمان
✅
۲۰۲۶ ؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91363" target="_blank">📅 22:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91362">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
#فووووووری؛ فدراسیون دانمارک اعلام کرد که خطر از سر اریکسن رفع شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/91362" target="_blank">📅 21:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91360">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پشمامممممم؛ اریکسن وسط بازی دانمارک دوباره قلبش گرفت و سکته کرده
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/91360" target="_blank">📅 21:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91359">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAKqJ30L-h6-hlHNeFbYs4AYuaLjJLibqKoDag9jM2B0FsKV_9zEmfv2y2N26AD12ekpS1JXU4TS9hV0CX6KstT216erYJkBQ-2W06yXEn5yyBbKYkKnPJtGp6ttUXyCxW8aDS5HA6w8x66fzRwEcQgKcV5Uz54JBjyqFluCRxkO4SVmNsspQR-hadJvtraSdOW8HBmARi8iGdmkZtUZ5B0BASExHGgZRfphxS5H7y28FvdzZTgms8iL0_rz4327D5kKwp7LQ6gwLAJXfW_AUu04ko0UiG1OfLB2vxaTsQmu9NWlepD5TJX6OBLE0WQ-T6eKH0IaDMnTcvggBXTOSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برند کیت تیم های حاضر تو جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/91359" target="_blank">📅 21:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91358">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
🚨
د اتلتیک: نزدیک محل اقامت تیم انگلیس درگیری مسلحانه ای رخ داده و 9 نفر زخمی شدن!  @News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/91358" target="_blank">📅 21:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91357">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thad4hD9GNXUu8J-wJwUmMJBOdFVVc8Bm_SZ7sWY3Pxb4MlNWMPLOOR6uVvBKO0WsZP7NLblhurbkm0UFw5BnLdInjEZfVmqod-GfdEfzDIWLzbf6pw0-bRuW3E0owO8P2fK1q5OwzGuP-nPrEDrrPeoo2ophIWd3yEUOFbz3xCv9bHE7bWGRYpmn-ShQVjY5SsxbmFN_jYknW2gCUgLlS2uepkl3CA7DPvrZXtqc0_wiu4Z-uEN67EgQ4pxbI9CUWCVMQKbD_oYuQl4BvEjlaQ4kIlU52k9R1aVpm7POjQWIqt9oQqG4RbUJm-Wwcwgklvi7eA3tTtHw43zY2cs3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
‼️
داور بازی رو تموم کرد و اریکسن به بیمارستان منتقل شد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/91357" target="_blank">📅 21:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91356">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5QnCN_p1ATv3lTOAhwYh5NiV8F33l-O24dBIy0aUGxF05ANxcuWZLe-MmY3B-B6jK4ITlBNZgd2e1-8J_zUMUmdeGlFbed3oyqKri8AOg_LSJK5obJ3bfLYkRp-2oMoVUvjfrJW_HML-kigh9Ja-CWLRXWNg4hTPVtrRBLOj_Nvrs9uMzPfL6NsCNMwxldCg4aY48XbXeJVAJu3yWtxVsXuf-cxsJD5lWPLa8D1OqUdOZ1sXE1_YHzFro_qVij7XmVDUIub7Abx5njCSzJa0V4DkzTzZKPN90B3Zp3ig9zdBk50C-M31oWoW0rZQdKU-SR5KBC6PgcjIylvt_PiZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
پشمامممممم؛ اریکسن وسط بازی دانمارک دوباره قلبش گرفت و سکته کرده
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/Futball180TV/91356" target="_blank">📅 21:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91355">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf69fb6576.mp4?token=Kx2W3Ti57-zxzxnEV77GHKanBpZDg0wjNdBtdmLrYXmeW0EYDed0gjvcJtuqAeWzzDDs8JQJXXuHMOgLdiv72BZZehk3RVcMx16q5ohrdjg4vAjDaEOKteZHNzWbn-KKobhl1FG8xuTKa-0H1OpVh5Lfum1LZ3Dt4w_-B8gqoemFkDvsh4xzM1_KTyYDGk4xYCgEEuhPuV8Ej-lPb7kKVvuWHB5OSF5tqIndCja5HTT398b_73vs_LAy1WSmvPd86v_wVj-3yMHLeTu4hl91gGi3wozlxoy9zI6RkeR49lLxzhRp35SUx3yAWtP2pD91XSaXtRHCRBBWVZoEeJcj5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf69fb6576.mp4?token=Kx2W3Ti57-zxzxnEV77GHKanBpZDg0wjNdBtdmLrYXmeW0EYDed0gjvcJtuqAeWzzDDs8JQJXXuHMOgLdiv72BZZehk3RVcMx16q5ohrdjg4vAjDaEOKteZHNzWbn-KKobhl1FG8xuTKa-0H1OpVh5Lfum1LZ3Dt4w_-B8gqoemFkDvsh4xzM1_KTyYDGk4xYCgEEuhPuV8Ej-lPb7kKVvuWHB5OSF5tqIndCja5HTT398b_73vs_LAy1WSmvPd86v_wVj-3yMHLeTu4hl91gGi3wozlxoy9zI6RkeR49lLxzhRp35SUx3yAWtP2pD91XSaXtRHCRBBWVZoEeJcj5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پشمامممممم؛ اریکسن وسط بازی دانمارک دوباره قلبش گرفت و سکته کرده
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/Futball180TV/91355" target="_blank">📅 21:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91354">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhi6mkVbX6GaF_lxALRkEqrD7ZNyFm_PLck57Tz6C29b_d2di3s6iOOROfa3LmMSEPw1m124ByrbNrqed6UpthkCP8axMC1LufxK9Yps0mNm9wrb3W-2QpaAaG1gnjM8MTzu83ZwYksRtTw1xjY2Qoh7X43g6nlJi0ztipbAJlxHdmdFfIIpC-p7dSxa2egyyo65Ahe_s6nhK96gyQRTApq-a6bt1DSl3-yt7IQ7ZhsUyJUhCXZgbewXtEQkp8qTzWlSDWa9uQo94mHABbV7rX51wccEenvakKrKcbtihqok2OkRUuajXBT26iMn9MrCjQANDoCXZcv7HF4iUEl1dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فلورنتینو پرز برای نقل‌وانتقالات تابستانی رئال رقم ۳۰۰ میلیون یورو بودجه تعیین کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/Futball180TV/91354" target="_blank">📅 21:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91353">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k81ubeZ-MqDOBf0kpW6UqjpK3mVGqmebMCog1CPdm1ty2ZriAOHYXNFhVNZ4rfC5dpNwe-zE7n65_UAaQTUcUlgcqgMBzaX6XbvFwIfmPU8Q6cSNKWx6DDEWtmr0uOTaRdulZtxlWo8LEzm2sUYWf-stoTHz2rfDFrtYqE0wrpB7uKK4KemmhrPNhh6in3SChhkAbNlwzUXXBDBYklLSD7CSTWxVVz329BRgEe57WFu-kHNwPR9czL7d-DiJ_PApXP9__qjtFTXHWJeFwTqdqibmPTeRQcIXHUl_DkdGot8loA1M_Jrp67FqzoUdeUu31iaBMtEpcvDNEgf22ID1RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسکتبال هم جذابیت خودشو داره
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/91353" target="_blank">📅 21:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91352">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e07c2b244.mp4?token=HK53qoDlNJsl2RE90QNkmAPasGFMIWK9cmBc8IQflJ1KSPjF41uFu49ctLOdD8EJi68WqiOF7JypMdxglKAuwIcvO7x5Li22ivZU1EJNT0Sj47bTp6LOogXwtG9Vehyp1ERE_ld1C5qvvbkTNc9DXKRRy_86IFDlYG2CP9nS_BPH4hPEC1szFgVeELPF498R6sAbI1nmKyEZOgsmucHZ9-lNEr6j232epmgw8YRqfYsCEil87Nw_DeIlS_OnUQ6YCjeSriBlA00N6DZQVf2zUwR1xjpkd68PREuwuXjO3aUtJmn4osqwEfXc-wg7ivh6KSx-CT-61F2KEm4pjQp6Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e07c2b244.mp4?token=HK53qoDlNJsl2RE90QNkmAPasGFMIWK9cmBc8IQflJ1KSPjF41uFu49ctLOdD8EJi68WqiOF7JypMdxglKAuwIcvO7x5Li22ivZU1EJNT0Sj47bTp6LOogXwtG9Vehyp1ERE_ld1C5qvvbkTNc9DXKRRy_86IFDlYG2CP9nS_BPH4hPEC1szFgVeELPF498R6sAbI1nmKyEZOgsmucHZ9-lNEr6j232epmgw8YRqfYsCEil87Nw_DeIlS_OnUQ6YCjeSriBlA00N6DZQVf2zUwR1xjpkd68PREuwuXjO3aUtJmn4osqwEfXc-wg7ivh6KSx-CT-61F2KEm4pjQp6Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح میم: لجندددددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/91352" target="_blank">📅 21:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91351">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24f9934c86.mp4?token=r9ESApHi0n6pWZ1CIOTQTtKdMkRZJRdFnOnBPDy4GhrccupNyShBkN9yqxbCzIPUdiwXyTz0VMd8U8OjIlN5tNg02R-B7rgMsWut5jJunozz72ojZqaFhf5Oo8vZqRPRcFxBNZ7hOCXlxC5U4Kvwzq2EP3D8saUxyGhYgceufQtzlNf8yQUlGLAjO9KGlxurRptoj_XowxchtDsIIQZ1w3PqLRzKTqczv0Qf9DupC_Li2yCdLrizdFAFkk_MDgI0E7_N3IH_bokWfJQVrz5h5LrVgmbaZ88O8cuRFT96SEGk_Uc0roP85wVFNH645i1IOPBI9qH4lsoeaKj6hUUQ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24f9934c86.mp4?token=r9ESApHi0n6pWZ1CIOTQTtKdMkRZJRdFnOnBPDy4GhrccupNyShBkN9yqxbCzIPUdiwXyTz0VMd8U8OjIlN5tNg02R-B7rgMsWut5jJunozz72ojZqaFhf5Oo8vZqRPRcFxBNZ7hOCXlxC5U4Kvwzq2EP3D8saUxyGhYgceufQtzlNf8yQUlGLAjO9KGlxurRptoj_XowxchtDsIIQZ1w3PqLRzKTqczv0Qf9DupC_Li2yCdLrizdFAFkk_MDgI0E7_N3IH_bokWfJQVrz5h5LrVgmbaZ88O8cuRFT96SEGk_Uc0roP85wVFNH645i1IOPBI9qH4lsoeaKj6hUUQ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانو زهرا گونش از زیباهای والیبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/91351" target="_blank">📅 20:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91350">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏
🚨
‼️
هشدار جدی پزشکیان: صدا و سیما نقدهای غیرمنصفانه کند مجبور هستیم پاسخ درخور بدهیم
🔴
@Perspolis @RedStarFc</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/91350" target="_blank">📅 20:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91347">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇩🇪
🇪🇸
#فوووووری؛ هربرت هاینر (رئیس بایرن مونیخ):  ما باشگاهی نیستیم که بازیکنانش را بفروشد. اگر فلورنتینو پرز می‌خواهد پیشنهادی برای مایکل اولیس ارسال کند، می‌تواند خودش را از این زحمت بی‌نیاز کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91347" target="_blank">📅 20:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91346">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrCQ1UYZ1XaUIQmS5lLxrDU_jjws6mLni5nAtYpZMOKqBNJrVS9qvffRG-nE_7ZriVtAw8Oqlsd9Dr5DyRMg5Bb2adKo6E98rIffKPVRWt3IxEyWL_adImRbnNrZx4hktRTDZXfobvViO-MDkipmmOMgXzYhCtf5e7mollga3RbqGDseMU0ebhh4Gb-U696KoEPGJOAsdX6hS2TpG3fkv-IdyZ3kOlKCvCsl0yxw_93dr-7_OM_nOQJOmoxOjCTf3CLqklrC4zMh7TB1r1KZka-BxTsv75b3lXBGU1QF1gMrEr8IRyj13O8EaddEAHjnWKWGQpPoFcOxnjeTBWZ0Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇩🇪
🇪🇸
#فوووووری
؛ هربرت هاینر (رئیس بایرن مونیخ):
ما باشگاهی نیستیم که بازیکنانش را بفروشد. اگر فلورنتینو پرز می‌خواهد پیشنهادی برای مایکل اولیس ارسال کند، می‌تواند خودش را از این زحمت بی‌نیاز کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/91346" target="_blank">📅 20:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91344">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6EmOmJeGhgg5PMnFESppqoNhdYi2H8QklD91EeuRf-b5ZJEdD0cIt9SZLK3puQn-U1Cp9pA4r2bxx3oi4ysV8KXI-APaETf2nOUyp16caSVI8hDz6v6cVCNyoM24-alc5OSBZsUcD5SrY3EUWk34ocBLyiufJGEQUpWYHGAHmFT5l7Mfan85O0bCyhMnUyXfUK1XKTGE1zjMZ6Pv_vhwT_5Ak-BLe1c6Mn4OmCU2YyL_9JyKsMS6xv0iogsIJIR_fUoiVQVviKpvxgoX64E_-pT1hBfvISYuL4ongEdN5tHX7UCYqOxxuwptZ_Uk-Ui5JRXJUB0zwkVc5vMv4gIqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکت؛
کریم بنزما فقط به یدونه جام جهانی دعوت شده و بازی کرده و بقیه رو غایب بوده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/91344" target="_blank">📅 20:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91343">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDRSQq7aiPiZW7iKso0IrTOxdlYPY6S-Nv4gZTw7XWp51TWCJX3lUmZIDvun1y6a2zRQeffYLaOEcHgJEPb5dj4vZrsYvGZRKE4u_9TejRf5uFZO_XcyqC9tIl59fxl3hTWlhukvYOsyUGmr6ezBwKcdPsBjWr16hyxJrPTorSZZVLWPuI7DnjRgQD4mGj-2JcmTA3QPJTLzpe1uXPnkxNTjZ9hZVBl-vUTsWuXcnUOUurEps6v7twVaopQsmljiKAUD1eZxD6klzc6vnA9-1TL1msm5LUWHlCRvIz3kui3MEg6NesZ1-vLVYst_MJQQKMhoyq4y_jPAd-rV4ZW1Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
چه کسی در جام جهانی گل‌های بیشتری خواهد زد؟
🚨
🎙
کیلیان امباپه:
⁉️
وینیسیوس جونیور یا لامین یامال؟
وینیسیوس
⁉️
وینیسیوس جونیور یا هری کین؟
وینیسیوس
⁉️
وینیسیوس جونیور یا لیونل مسی؟
مسی
⁉️
کریستیانو رونالدو یا لیونل مسی؟
کریستیانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/91343" target="_blank">📅 20:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91341">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V3PPn9Nduf7sKtveKiSUZpryQtzQD8v3jgS5yVkP2HdN8oXaq6y4srTazJZB_pMxgyKhqsJbRj9VWlDan65Kalwnvd76EHMUC5KGbcK3DFmnVGv_AH8iso8uo8m0P-TbWKwwgowbwxlAl_RG2H2eSqgkYD3rOsX5_7hsEsjIKmxOKrQ3u8TudiGNx3JzVJbDlltCAaMa8sXf47-zc1KL09RaINKihme-B-P7tR9AFvJiLmXjn_udts-158fZPIsM66I6lJqjq00CEp9384FfbLTpzm1PSSFFqwmUv4g706pLBFckvwx7DlEJ5XE5mN7yckzzYMm4-jJ-vAjWtZHDTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0XTT0uGbDsMaivWDjkN7uySKJ7u7PsK9Q11580cpRpm5LXxipyg1gncdqwVX0CZrdujA1_r0LCeUOjKFN2vg1R64CnSAA2QC01agcS3ncLPXzTpsAzPf2tnGMFU2WlHn3p9flcdqzLgclN9uIYgvpeHeoY_BtX5LwqskxziqZ7EhuzMrMhuFCpYVbKjV47gKJCheYGjfYBmB6AIMrDi_jQt_GPg79Ql6xgHk68uN6vy_cPq77V92s-q57Zgs8mHg0kIWdCLtzHZxjy1v_muqloGIDmvIeMEf2UTuMoraia_3V3nha1dpdUSIxc7QTYYuGy3DtDDEIcUXPy2nRgsdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به نظر شما مراکش قوی نیست؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/91341" target="_blank">📅 20:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91340">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1xk619KicJclLTdjarRJ8dCXngcTUSrZEt0MfPNGgqpahA-7Q9I5JSJJuus1vjvdERmjKA_lvVbOhzMQWudS5FeKIOBaOBC4xEVsRTFmFw4JO9ccSS_UWt-aSSFmJdIcJOwhASlNDJx25akCyUlx6mCIf1w40T_I4xfChKfgAkacqcypBrThGuNBTFclb4qVZyYbBQrErw2VV4ZBAl1q936_xFip5hVEZJbKB0zH0sLNseK3EHtkZaTVuBcI-S9lxaNaHJ5HXf9OhVXW4DdSKeCA-YqBRNnvTaZhQWEKJHEs7Rc83XNUImZyoDZ7OhRXUvPuJ-lbdkXcE5t35kKOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرژانتین با هدایت اسکالونی به 18 پیروزی متوالی در بازی های دوستانه دست یافت
🔥
• 5-0 مقابل استونی
• 3-0 مقابل هندوراس
• 3-0 مقابل جامائیکا
• 5-0 مقابل امارات
• 2-0 مقابل پاناما
• 7-0 مقابل کوراسائو
• 2-0 مقابل استرالیا
• 2-0 مقابل اندونزی
• 3-0 مقابل السالوادور
• 3-1 مقابل کاستاریکا
• 1-0 مقابل اکوادور
• 4-1 مقابل گواتمالا
• 1-0 مقابل ونزوئلا
• 6-0 مقابل پورتوریکو
• 2-0 مقابل آنگولا
• 2-1 مقابل موریتانی‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/91340" target="_blank">📅 20:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91339">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1pY81ViKqbe8WW3HLk1VGn0pN2rfkO7yJU_ZsR4_pDDW4xxP5SsrOuK6Uh1sflKn6f6tuHNReXg6OgwXFj7lL4vHIq7S149-ZkI8iNUU_Sl2AHF5cG0oCtuMb83vnTrc11Tl4YKCW1_uhhU5QUTDxgSeAMfoFUPfqH_Ziis1ep-zoKOg40db-2v-1iPZmBwFrjVwNeto-LRkmMnvW1CX8mlYFKPw8t796aaBxJoz2z1NHkEcWermkTlvfNpEd7EuHL40zysFCsIrl9PvzXYop8jNaA26G-ZjQU4r2_bdns7IqfrLeNOdyWfW2E6VGcXSDUrXNiwYtJjgc4hP0jobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◉ 5 توپ طلا
🏆
◉ قهرمان اروپا
🏆
◉ قهرمان لیگ ملت‌ها
🏆
◉ فقط یک جام کم داره...
🌎
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/91339" target="_blank">📅 20:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91338">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1_R9BUn6-V67F1ynY_E8s9QWxWsI3bCn1141k99uM65asS9n7ZGk6_dIh5BrEYH5n6-fXYKSUyA1azYTLRlgebjGgu0R4YWMVTLYTLoXAfB2keZ9d_Zqd0bI4bte5JhG6c0WiIqHEZzk7dSPtICwo8qjvXkcbpa2o5n5hVc9knyB1WiLW1VqD5kz3MEszTR9r8JY7lOlrMZa3Zq31Gvc9qH2GQVIAZLPj0qxiRlmlYO5oldhkJ10Vqd_B_aA15uF9zraNjzepYRtUMwPuIuOqVCYElJ6hSir9Gk6uqXLZDgoI5ILK5QQKF0NatCpoJ3cpzpOma8MydqhsR4KJXumw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وسلی به دلیل مصدومیت از لیست برزیل خط خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/91338" target="_blank">📅 19:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91337">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQY4VhJf-KoA7cqkoN5UEQjuOajtdGed7sYCLDBEQ2qvFNunVMGiJEmVEz2NmIiYxlOcaYgmayVejHraL5chbQ5PaYHgPfqF8UCHU_IPpjZPhUugc7Accen4vgZ9DB8-hyoA99W7ZuthqPqwJcWGvn5kXujI643KlbswC67pSoodsLuhPDsF04VJ5l928FV8qHeDpSDi9x05IjK3_NjQdMjOYVEorFVN8Pyhaod6nrKHL4xEPfMAfFEtoZiEeIPPCcTDkxHe8uiF5t1x3PcfCLGwj2c8p5k9X70Fq5epyIJffcS3QPN6DcNOmSim0jHEhXlPd6DF8OQNr4pELnfUgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وسلی به دلیل مصدومیت از لیست برزیل خط خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/91337" target="_blank">📅 19:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91336">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afa8f6077e.mp4?token=Q07-QwJ4YBVQ4SEAKUNn-x_DjFOIyFoc5fwjWoArP3bHsEBsacE7If0mCC1xolSDPbkqKPL5t8ytTKh6bxQWJrYEIY4liGb_ZZED-Kvjcp0wwncDBIip9LHjQ_utlDvBU2Tnegdw5W4S4gahEW7rWRuJZROKc5DqrgnoFPuZsEW9RD7MWrYQ3sP_81WRYZgPBQWhW6_hV5-iK35vgCZK9AiGHOzWvjdUv0zJ8zUDmnChb4_ByI9YbVYABcwLsegODnXpNTbAW7dI7zmbPZSrOIbyg87xjqH5CZXbNDe8AHXVE_P7y2d3ly9FBz_ULqPVO9JUPlwtVa4eAOSLPtQt9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afa8f6077e.mp4?token=Q07-QwJ4YBVQ4SEAKUNn-x_DjFOIyFoc5fwjWoArP3bHsEBsacE7If0mCC1xolSDPbkqKPL5t8ytTKh6bxQWJrYEIY4liGb_ZZED-Kvjcp0wwncDBIip9LHjQ_utlDvBU2Tnegdw5W4S4gahEW7rWRuJZROKc5DqrgnoFPuZsEW9RD7MWrYQ3sP_81WRYZgPBQWhW6_hV5-iK35vgCZK9AiGHOzWvjdUv0zJ8zUDmnChb4_ByI9YbVYABcwLsegODnXpNTbAW7dI7zmbPZSrOIbyg87xjqH5CZXbNDe8AHXVE_P7y2d3ly9FBz_ULqPVO9JUPlwtVa4eAOSLPtQt9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانو زهرا گونش ستاره درخشان والیبال ترکیه
🫶
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/91336" target="_blank">📅 19:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91334">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P1Pp_IbR7xza-FAeZ2N1ri3isokiW5Klo8YcGrhgnnmW8z7nMuu4f3fm7A4ABrdV3rYDREZEmOCZPiaSfeYoIu2CuPDpfQ-NjhRll4eIOXB2idh8sSnCDXLZPqc08mxBbQPKMyTcCQOWmSnHMJGO_FtzqcUmYedj3TAdeu1EjLinm2uTe3RsDssYhjUZNlb7hnTuu6I0zoeP-ckrS-Tq3VuBXpeFRGqTmKtcYAfV4h-dj-8EtVu6NnHYymV2tBKVvXkrK4anril5spgUkCzZanZ1HMh4nigXsCNomaPxHvJB-85vj9K0GenYVDyWSifaOPlFXLhIu4AXfGhuh_0OFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keZ0P1_-KHfjaRXXHXIGPQUs-rAgrHbnMVg7Hr-mf1JMuVXrEL6Py41i_j0LBvrJfWc0pgUQmXerPYu4YMIccl0Bokn3flMMvwismJw-uBrPcfvWaVIlypXYVnkfncSuZZnQSyG83UpXwVcLwFpbYkE0BpDRXrtWey0NySm55WDaORw_GdhXLPcSRvP42twd3dVkVbhGnUUtDdz4r-RhYjTHqjKEKTZ6GpPvDSr4MKz9Axa9R2ULp0V1h8j7dID6nNozwH1gMA8JCwEkygfIeRqKzP_n7tPhjbdLbe-31DYEcwgJpRz7VqVRKOr6AVMPJHFiedf1RoONImj--LH-qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حتی یک درصد هم نیازی به تست DNA نیست...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/91334" target="_blank">📅 19:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91333">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a6ddb8bf2.mp4?token=Tu11dcLz6wAL5arkzC-GFvrGUS5m7qfm5dWds9WZcNDq0qupx8Ja22puCmxiSHsH2O_SiwYrMuwibF-wSp6bT8cqXnSAC1Efo1HokR6otPtg04FtjtiONYkhQgGdSfPSOKQpiI77xCwAVNr23nwxrV1tFUR0xTjV6t9FKhbBBT7WCsC0nLB-14gw8RI2vq2KDRsNEAWp_yz6lVmTlzWnHDnmO4qlwzLLiVwi4skOH_FrWqpsX-321hwigQsSaNiCRFwUqXhTq6T1ezDOBNLE8YVApu8GCJnrPyW-EBDYcmKuZI7qbFzx7uXMPkaAEcEdxghgvUI7jIPmYpbRCRe77A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a6ddb8bf2.mp4?token=Tu11dcLz6wAL5arkzC-GFvrGUS5m7qfm5dWds9WZcNDq0qupx8Ja22puCmxiSHsH2O_SiwYrMuwibF-wSp6bT8cqXnSAC1Efo1HokR6otPtg04FtjtiONYkhQgGdSfPSOKQpiI77xCwAVNr23nwxrV1tFUR0xTjV6t9FKhbBBT7WCsC0nLB-14gw8RI2vq2KDRsNEAWp_yz6lVmTlzWnHDnmO4qlwzLLiVwi4skOH_FrWqpsX-321hwigQsSaNiCRFwUqXhTq6T1ezDOBNLE8YVApu8GCJnrPyW-EBDYcmKuZI7qbFzx7uXMPkaAEcEdxghgvUI7jIPmYpbRCRe77A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سیروس دین محمدی: در یک بازی وقتی گل زدم، پدرم در استادیوم بود و از شدت خوشحالی سکته کرد و فوت شد
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/91333" target="_blank">📅 19:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91332">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmOIVaDQ3wS9K_E87F2tsXrXVjS-zaFllg4riy3tksx7-ms1yf3qDZXpqOJj7OA_dFvkath1xjD_sr19ciLjuKBB4XIDn_n1CzX26MojsaOWQT0Z76GBOFnhFdTwbCYxPRcL3Tpo8y28N06tcB6mzIj613d4SZb9M8Ib_zv4KWqt3z61Axqq-xjfPRYQh9cKCiEjlSBSOqdfm9qfNBdgGYc3gSygO7ruk3w0pcJ46qJ47f1-B353TFpqTbqpHFTu0_Tf-Bt4-6BjzjwIP6eBHfkPSafN82RF4-_wh77rnuofMkSY8EIVHAuXdKwekhF6KBay7LUwHa76C05bBTQrlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال:
اگه جام جهانیو ببریم، به مدت 3 هفته ریش و سبیلمو نمیزنم و میذارم‌‌ رشد کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/91332" target="_blank">📅 19:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91331">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwCKw0GjP-bXzChqKNg6CfVI_6KBwncVSW4hawYWC6eNZReMVIQpBoBsHB7IgZf-05gz-g2fHskQfphwmBXA-dP1-dtsKYhcwLTALZbmH2qh2XdlfFtWRFu4MneewUPK9Z580JJlOtMZtxDHfGRtjSqJYPv1vSOHYQtSfyW9yqbOHi4CdyIgCDp-L4BH7w48M6gxHqhJvycfaqBj80MhPuteJjYK2nCQiMsPTTCF7u-j9KTGYsWStKn8nntT5um9F9qtAphGKXjCkPNMreVjnaIpPfohKYdNFpeQ5ZYtMmclJSEfKjng00SLYKIREgm8XzmjQz_B63o-lPfSzsFW9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزش کنید دوستان ورزش
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/91331" target="_blank">📅 19:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91330">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67083b7bc8.mp4?token=JTEqDzVU45hsuGEKRJSnmNkX00DU97jsmBUDklnPgJYxyUBv1T9PUqQBWXqNPrjZTULPwgSLvq_bGmQiULmwIF21avKjL_pCqRxctvA6lah3mFUZHREuJYUzOMvV5-l_uqNDtsO_brJ48RDf-g_7j41krKP-Xg7yyKmOwd0AqTZ4J3wkNPiIDSWQNcMOUxEabIbsVVWHUW4DAK5PAw1etu0lemcJziykERE-d1hd-Y21z6poFtxueDCIU-WFlrAwiEZJ-MtT_pV2QGoUtiKz4Ohk8JxpakqBOGZPbuiwkNcB0K_XPr3w_9SgEHCVIGk4PE3koL7-zKURZN2buNH9rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67083b7bc8.mp4?token=JTEqDzVU45hsuGEKRJSnmNkX00DU97jsmBUDklnPgJYxyUBv1T9PUqQBWXqNPrjZTULPwgSLvq_bGmQiULmwIF21avKjL_pCqRxctvA6lah3mFUZHREuJYUzOMvV5-l_uqNDtsO_brJ48RDf-g_7j41krKP-Xg7yyKmOwd0AqTZ4J3wkNPiIDSWQNcMOUxEabIbsVVWHUW4DAK5PAw1etu0lemcJziykERE-d1hd-Y21z6poFtxueDCIU-WFlrAwiEZJ-MtT_pV2QGoUtiKz4Ohk8JxpakqBOGZPbuiwkNcB0K_XPr3w_9SgEHCVIGk4PE3koL7-zKURZN2buNH9rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
از ایرانی‌های خوب هوادار ازبکستان‌
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/91330" target="_blank">📅 19:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91329">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxrWp2E9ixTOvPIG3Qyc9XjZ3Jv142ZXn3s-OKE8YMDNtWdKftmUv_kDyMbk0ib3r_J4UGRWPvsQuYufznFfFIEkZ76iIthHwUTMpD9ntkqvFbZcoqFlM9XPRBLHINhEbzOwbxJ3BMK7mW8nDTv5aj9UXxlm26Nn9p4xC-Q8Xofz_mDRc46wLz93J_le7TdrOk2589LaTneLKi_NY_TK9f0TqifxkUketlcXuuNl9nSRUh8npdVFhD1ckgX_X3HA6zmLr1xiBepNQsvE9OiNgvqvKjGDKNGEjBnZmXK2tZhDJvSE7EcFgqwkapPq2-3GZ8Vcqf8WHZa22P4D-4Mykw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال درباره توپ طلایی که دمبله برد: راستش، اون روز فکر میکردم قراره من توپ طلا رو ببرم، اینکه دمبله هم برد باعث خوشحالیم شد، من با اون خیلی خوب کنار میام و میدونم که هنوز زمانش نرسیده بود که به توپ طلا برسم، اما مطمئنم یک روزی که پخته تر شدم به این جایزه…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/91329" target="_blank">📅 19:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91328">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcYynsUpjzSPr7OTAuxaCytJ1TpP_zcOtg6X48qawEGc_GiGAXVljRu600kyEwnysVqLECLu8MsWhuvZ08j84WUVQeah0WUF-LxmwRdqPxDRyYqOALdSJlmEqVDYxknPDv5VZLCYfRYHrsz1CJW7gJcFsXG2rFGNWTFaUkiDlO1GHTuiAWhVwBQjE5kY6Qu0WYWnlRpbQYgii6PH-thnD72Pe935SNqn2xM0wGoVAoWPhDmfGgu87Fyuha7mAlgIRx5d6OolyD62SD9mLDYFYmRIf7iQLbEsfFjwx49oDKPcw7NMSWFJ8AMdnMsuPUTQh087lKyDUcrLF9eBiUruTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال درباره توپ طلایی که دمبله برد:
راستش، اون روز فکر میکردم قراره من توپ طلا رو ببرم، اینکه دمبله هم برد باعث خوشحالیم شد، من با اون خیلی خوب کنار میام و میدونم که هنوز زمانش نرسیده بود که به توپ طلا برسم، اما مطمئنم یک روزی که پخته تر شدم به این جایزه میرسم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/91328" target="_blank">📅 18:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91327">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02ef042a5.mp4?token=Oz7dn0EY5DwNwKgOuA-yuw6CL4Kmxowh7hx6FaVfM-gsatfLr-_s_UPcgHYLcIUgnSLJ0Y3SDELIJQxZfZqOsJH8PlShRttq69ns50zCYD2asv7c-qq91MssTqB3ElnJOBlOwO5jeokw-wBN-lcA8Q5klilINBe8l79Wu2NTcWYu38VBHPX9uOeTDJrV0v3_Rnd2kVhHQwJwkS055gEu_4ueINJGbk2G1C0oqiOMcECDA-DM8HF7bY44xeG4BNmSH2713rS3oC_saobyoF6Cx-1dOWZMT5MTK7Bo4Nl3zfZOJ-rW-oKKhxsPao8IuU0Ymg1BiL9WM0IGKQLwKgx0_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02ef042a5.mp4?token=Oz7dn0EY5DwNwKgOuA-yuw6CL4Kmxowh7hx6FaVfM-gsatfLr-_s_UPcgHYLcIUgnSLJ0Y3SDELIJQxZfZqOsJH8PlShRttq69ns50zCYD2asv7c-qq91MssTqB3ElnJOBlOwO5jeokw-wBN-lcA8Q5klilINBe8l79Wu2NTcWYu38VBHPX9uOeTDJrV0v3_Rnd2kVhHQwJwkS055gEu_4ueINJGbk2G1C0oqiOMcECDA-DM8HF7bY44xeG4BNmSH2713rS3oC_saobyoF6Cx-1dOWZMT5MTK7Bo4Nl3zfZOJ-rW-oKKhxsPao8IuU0Ymg1BiL9WM0IGKQLwKgx0_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
تنها باری که عمیقا از ریاضی خوشم اومد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/91327" target="_blank">📅 18:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91326">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kmn9QIzGk1Vg9rxkFhMfqWFpD4_ASe3XaqwcOWCBRSauxk97iUbyVAjIXobw2zB45DKzWyjPFgcxx81i32plVy14dJ2IJX_8oNAlwQ99fJrk5YDxteYx6sf1njjH1z8vzAnLBUY2R5PFLLwawNQLs3bwjXdC3SAesBMgE6fPyn9bTj3ayg_6IdRI0hOlpWThlvkfmY30OApksp9ie6pQlm2SkfviAXQVWxR9n6URouj5rCk1FCEv69qK_JjzlloByaj94AJi2nQ2Jxt8uTYpg2lcvZ1KXi6IG7OXxjDVbjASSOW9wuDE116jYxdSFFbgMQKSZI6pO2CQ5iMm7bLNkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگلیسیا سر آب و هوای آمریکا اصلا اوضاع خوبی ندارن و انگار قراره تو جام جهانی حسابی به مشکل بخورن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/91326" target="_blank">📅 18:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91325">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
فوری/سخنگوی کمیسیون امنیت ملی: اسرائیل باید تنبیه بشه، امشب آسمان سرزمین‌های اشغالی را نگاه کنید
🔴
@Perspolis @RedStarFc</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/91325" target="_blank">📅 18:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91324">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E26LoutdEfVJNeJtKNM-dptmmT4oFd9ydvLhoqw_T7Q6X6-5n8EII7aur7YOiLyyPJ9Hoq0-mo5mbfEsx8DWCS-Fjzd65a2JAf0uZT5PnjDXIng0CElX4tSDyoeyVBdFIn75KNKg6pUnG3RDUs9TmRLUK--BBEJjLyy9mNaWq8cnZ_L9y8VmSK4tnm2x0hHc1UEiFy-pnewGYf4lCZSW8iG2zWgIt9_rXJhv8W3YJLTCCBITes5R4_SAv80_BQMR_jfbNXi1BudRVjxDgx9_2qZKVwHsl0yj3--KfeYxr4MgqIb7GYm9u4BsmQuCzKELNt7gT8ynfSBk8HiVaQoAnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رومانو: در صورت پیروزی پرز در انتخابات، ژوزه مورینیو فردا رسما به عنوان سرمربی رئال مادرید انتخاب خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/91324" target="_blank">📅 18:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91323">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بازیکنای کوراسائو با این اتوبوس نوستالژی راهی جام جهانی شدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/91323" target="_blank">📅 18:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91320">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W9qq1MtAwF0sIRsLlV8RcvoHyWT9cXJcvmT2rSAuiPvAUlSeRDzH3y_w6enzLqxymcLgEwhNDtV8Kk0ZGA3Sd2Mc6XoROj4fDv1a0PeQaiQvUidGdzTUPLbs15jPbo9QPWSLmlEFsXd0gk_qdbaxyNVRMF-oApCdFBLUHk_KJ-SrNmXRwTx93b3nsyxM9IcnKq7SN58-h4LaM23NOhcwyqJwAziUb9eeElmZSGf0csdGnWAX-mtzl7Yvs__RwHLmqGrHRBi7kCaKft0r5xjNDQzZ_9bfFLucOkKOM9CJn9AHabpj0i2uNOQ3qWPx5tFRQ5CC96Nj_R2wXvtCGEQlOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rpjms_NZZyg9TygalCJJSC0uCxjMrzgOWxEP2QXU56sQZnhYxCjqQNlkOqUZO9yAt23kyjax_xva8MMn8FNxgqZIGTgoW_QTF19Mhmk49QREaC8QhObBVzpUyhDOpQAk0gMo91b9rvGrkXrO-1OPLJO9eZ3ZHh4tA0w81iuGsA3kCtczgOC5Nl6wOFrarmB7XgNZp19ofXeRWH6KymoIqLZiMBnqfoJjNFy_-PmjRPh3ULdj1JZY_lluKTenDDgj_QqYwWcHmV2Qr-VIcmtpBGqj9_kbMZDSIc_glc1wCmtwNm1JvF0f13XWiTxBuQkgITkAYx70RpxpNUAnJ9Y5kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RCcd0H6ruJQvk8QPczvjyCsqB05RwRGPI_GeGTLJoI8GMIQJGczH-EiXZ6UMiDt_xHQgkWflAIfM8aaTtXvYNltxUoHb0SfyqKjHtjpNAORcVQvfMfL9PT7tB_gS_qIZYIE8_wukClWZwthBiAEbR7BnOmWAg2zf8dBxdxP6XekGuukAfnWVcBLDpyoFcQshUBsYjxcxGYoww6xTAiXKq3anJbvF7dWXJjVTLSMlszS70n0fP-QgoXj17gcbLB3SeIhGMBUWgxTRBcLrq5Nf3DKQbizpElXue8w42aJJGFc2uDLEZcrem5BEosH_8mxmnGkQuLRHzYJCyrQBnxtniA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خوشبحال مکزیکیا با این مجریانشون تو جام جهانی؛ ما هم باید میثاقی و احمدی رو تحمل کنیم:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/91320" target="_blank">📅 18:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91319">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ساسی هم دیده کار و بار خوابیده اومده ادا قلعه‌نویی رو در میاره
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/91319" target="_blank">📅 18:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91318">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XORkFxWwJmLWNuMaVs-5SW5ywD0h6eReo_rSpW9CrSuQT0LL5WAe1odl-AQ93rX838FRvXR7DbuNGEddX8jejjWzj62fDPf_hhTaEjudfXbcb-Rj8N8aengGOMBQmGX4PpnwCBqbSoJZFAnWMf181_UhGDTOxCkWnGzeZqVp3IvwYsEARlwwL6R3pEzK5RUOg9D5aZy2Vew19SG1iB_sg0yUxc8pWagCbly95trwdKwgad--yRnxGVmIiE8HKR83foaaXO3jyzojPWGuP0IEV9HLJuCa5o0hzAS9SasM_nblKja76PgT5oJjvwOeOpwBJHnk9E7Vtv-jWC1ySnGUgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🗞
🇪🇸
رومانو:
ژوزه مورینیو به اندریک گفته فصل بعد یه مهره مهم خواهی بود و خیلی هیجان زده‌ست که با این بازیکن کار کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/91318" target="_blank">📅 18:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91317">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6SI7kEktAABl7MNjbzFM8WjgOxdEkWNdbQfB3mgUnSPrx7WwLNZflPdeXi_GV4cAdfGN3_IVaqOh2pDWjNU1J3qPTICfz8P9Ws928C5B50IC2tKh-TzgIaepO9_LdAZg6ktqRr5oUxYE4s3pjTpBCFEltPj_i3PTMPVFX6_-wb_36c2KSzQS5AYApO-UmTRQkC42U8O9BOyniwhSvtcTmxmxkAS_qBp9w21bXR98qHQ6csJm2I4PYVVmdtY5UETxpk4mzWiOiUT4fRH33xo7RTqO1QVTDpnXDYYHVF85Ze13HqlZeLZbHjikWD5lqx_aAiSM9PsT-SFpo7BMIzkzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇫🇷
فوری از رومانو:
پاری سن ژرمن حتی حاضر نیست برای انتقال ویتینیا یا ژائو نوس مبلغی رو مشخص کنه!
هدف ناصر و انریکه مشخصه: نگه داشتن همه ستاره‌ها و تلاش برای بردن یک لیگ قهرمانان اروپا دیگر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/91317" target="_blank">📅 18:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91316">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHOH6kKJaHcKLljicZ2WJRverYS8iDkN7GEk0m0vitFiujUBH9G1j2xRIIw1aU-5Y1SJyK7xK5_WSW4PFiTOV39Uym-E_IdiuNTk1eiiol0MRUevMRKQZTZaumvY4KCqdwgfZQaRNVbb7rd3pJlQ5UCCSpb49jH0XSWoj_AEzIf6-BpLnxtZFhIdGLx8o9JkRidP-WmPF8OVPf4c-bJ0RSvOwkaiavI0mK8j4nseura1AlhxJDN3Hq7cRRzOo9gBZL-g9_yGulOGAo349xH7QdakwOgDqzw6dNQRVMX0pdlGVDRQfkbvqyfNnqAmjEd2dhBeShJrYW8SCKmnedDUgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
رومانو: در صورت پیروزی پرز که قطعی شده، اولین پیشنهاد برای جذب اولیسه تا روز سه‌شنبه به مبلغ ۱۵۰ میلیون یورو به بایرن ارائه میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/91316" target="_blank">📅 18:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91315">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qH_9wCUtkafD4-19u5soOp8iYnZ5IE-rVulJ-utarlZPURlSR0v0SkkinvLXn0dF4Grhw3E6N8GIcEQIdLPEao4CiB1N7p09bYNx9gBdEfIlIt-ecxpfDG_oe81NWPK3PZHXdHtWVlDeFbqbR9ku6cg_MUgLWYFPyGpDNBAJwK8EnnPQW0DhbBja8sei5Gjp-5h8Lu6VQdn5Qbs05IZA2fRg_xe-ua_UmDO3ujavYoV0KzInt_Qe6RW4JZ2S4UDNn63k2LrF2oyNI0HMz6BiUTbGJnSwhAqErV5BOIT8a1kNiqNVTrTDSmUmHt6ujOdj8LcXI78hTCXMdEVRsvQsZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
رومانو: در صورت پیروزی پرز که قطعی شده، اولین پیشنهاد برای جذب اولیسه تا روز سه‌شنبه به مبلغ ۱۵۰ میلیون یورو به بایرن ارائه میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/91315" target="_blank">📅 18:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91313">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23ab97717f.mp4?token=I6lQVdKBX4qOHkOFxlJFW9v1DpZmKPSj9sW5yOWE_3Ed7zrRlhj5nYdj-kRjqLya62IAPN7SLuk3q293QSz2BDCdYsJ0WLsUSyJI82TBkxrhUxzkeLEAHqpiZBviA0-hjTww8XVbhiTN3NiwjR4qpz0vX38rB3Fx97LdMzdjBttPUs2um7Or9RKxvalxCo2X5RhtYRmYWuCMBPCoq5Icy29a33sbI5bs0b-aK9M3867ekh-FFI-YzFXmTGG0re6r0VYglB_fXFterBeA9vDYEQRAciTGK6-m0uRf1vPM1xxurVeg_2VV-G_ytqDeW7E8Jmw8G6oV9wMyrppcoJQJYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23ab97717f.mp4?token=I6lQVdKBX4qOHkOFxlJFW9v1DpZmKPSj9sW5yOWE_3Ed7zrRlhj5nYdj-kRjqLya62IAPN7SLuk3q293QSz2BDCdYsJ0WLsUSyJI82TBkxrhUxzkeLEAHqpiZBviA0-hjTww8XVbhiTN3NiwjR4qpz0vX38rB3Fx97LdMzdjBttPUs2um7Or9RKxvalxCo2X5RhtYRmYWuCMBPCoq5Icy29a33sbI5bs0b-aK9M3867ekh-FFI-YzFXmTGG0re6r0VYglB_fXFterBeA9vDYEQRAciTGK6-m0uRf1vPM1xxurVeg_2VV-G_ytqDeW7E8Jmw8G6oV9wMyrppcoJQJYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدیدترین اظهار نظر وحید قلیچ درباره یحیی‌گل‌محمدی و رفتن به لیگ‌عراق
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/91313" target="_blank">📅 18:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91312">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
سخنگوی کمیسیون امنیت ملی: ما پاسخ قاطع و دردناکی به حمله رژیم صهیونیستی به ضایحه خواهیم داد. امشب به آسمان سرزمین‌های اشغالی نگاه کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/91312" target="_blank">📅 18:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91311">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejOMmZCdtZLRWoo7spnUx5TXRSzRcFy51PhYjKSfmbG4X-x_tfwpRvP0PZ9EeQxEi82LbRqmWKW281RjiNTKVfugwrou7fT_PtOE5YySlRLuYyBSzzVH6cpr1nN0DOTpYjDYAkbRHtng12hQ1JNUsZ8JylFdMu2ZdjbCJjn6cBttlkUZRPkBw60ulB_YldPolnygomhBuKOn_iR0DhS896XjBV3lWQ_nfmrWcCPr6K7Krfzsm_Kufu4tpFRjrPxS_Z0wbTvOwDVW0A6lnetfR1fWziPZqp4SLUlmJjhK9wPXRa94LtgFHc4BkENEJ02HtqgyQ2dYZhOCE7qLt01NLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضلات مارتین اودگارد در تمرینات نروژ قبل جام جهانی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/91311" target="_blank">📅 17:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91310">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4446042f.mp4?token=HFAsqlvQFJH9yZzeASN7asE9kxY9dPWoPDyg6DFYo7Xhvj_cwV5hnOWXVFVhDvrHXGxlfbjV-AKiVOaTXI0jtA8WHtescS-qi8b5pcRXECYd8CscIihWcs16PQw2x1WtycZRLZoEZ_TSXCGSOWpCsS0o4WVfnaepJMGxm3uGvRlyhoCvKAynuhJIwC8jsl2QCoYoG6EPrRhi8VZzhzMjOnd8dCkxwEetvMGGgtF_FNSbEnlDme0WDvmYxiI987DkV53grpKDhCp1AFiwpy5JTfUzBWBm1nRQj9KGShf8vLSlu8_4Z2qZj_14AsmmtSK_f9X22hHAW2jp6537JhzCrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4446042f.mp4?token=HFAsqlvQFJH9yZzeASN7asE9kxY9dPWoPDyg6DFYo7Xhvj_cwV5hnOWXVFVhDvrHXGxlfbjV-AKiVOaTXI0jtA8WHtescS-qi8b5pcRXECYd8CscIihWcs16PQw2x1WtycZRLZoEZ_TSXCGSOWpCsS0o4WVfnaepJMGxm3uGvRlyhoCvKAynuhJIwC8jsl2QCoYoG6EPrRhi8VZzhzMjOnd8dCkxwEetvMGGgtF_FNSbEnlDme0WDvmYxiI987DkV53grpKDhCp1AFiwpy5JTfUzBWBm1nRQj9KGShf8vLSlu8_4Z2qZj_14AsmmtSK_f9X22hHAW2jp6537JhzCrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره باشگاه رفتن و معایب خاص‌خودش
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/91310" target="_blank">📅 17:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91309">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUEsi5VJzMxBL17Qwox_Q2fRjQidBVVli08p3fu41R3bjpgSQzhkFetggKDE8mItmNcLXLL3HyGr8XLtSvcQ9RKWZw3tCeQUixXZgrEK8P5YYMLaztc3y4_bVS2Tu9q_CzQwNOBl1A8VEm8ndxmciqNwtVn9FGoNYxj9HxJs3Jg_yRlNAxeqcw2Mhk42BMR0a9JWHuis_pHJByZvB1Ow5bHjAw1lMDeb2NNYUMtuNYSnOdQ643UKqyiOxjZXXWhGOFO112qeGT6WMWcOAPa78ubjiX2kBH7Iep3ce9gRSAeHk1MRC1lU78R82oDR5A-9_03etvgORKNC3S6B5z7JaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی منفورها وارد شهر تیخوانا مکزیک شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/91309" target="_blank">📅 17:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91308">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMC-4tfYi52nJnglzFjIzEZd9CH4zgezjYqUxKub0GBHrsHIXrJp_VC8rHfR0oUXQeUzkDufAAJ5huXrGSBvoY2vXCfD41ItdJDy9xRRDd3fFa64BCaeejLo1X3ZxJyfxogI0LgSFdZMH9EB9YaRuIsAVntcVUFycaQrQXTJHCnZ0KDgpTR_0RoYRe6TpQJtl7EYfBhdVby3myxqeMDZnBT_2LVizpo0TZabwFQvOXwwHkC_JNgbZeJLUnzqxlEetGa0BaohwCAI8MbBMFKAZ8AxRNd1zAXZ_0WGx-yz28unCukBvgM8r6PX7rWUnq62DnQES6mMkqnsgx3zRJY0bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره قراره این رویا به واقعیت تبدیل بشه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/91308" target="_blank">📅 17:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91307">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NJ25j2461k9egR8J8CCRCvNk3CINVVEsGyIwExFDwygo4dNnWV2bJ9boBy4onaGRHpS7YBXwjKi-FV-S3qUouUFx_mt6q-KaT4kBqhtT0QZHbtS8Ok6Y3hm_UPjjai_kL23dWsiMlNCc7_zEoFbhs90ObdHvYYGuwgp8VyQLp-mkXpfxZCjae4ZWkBLOFfYkB6m1a5cu8Gk5pVA-hAR7TsShlO1V5PH33jEqsP-dA7WF6ZJKbG4g520Mr1wkuEfuBxeMVvQKsf_WwSxyDCpo2rY7YAkRxDI94VMdl6e9rOzBru_UaFSahT5PgxNeiPHxxW38U20-bXg8AmUKp0nM-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🤯
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#غیررسمی
؛ الیوت‌اندرسون ستاره ناتینگهام‌‌فارست با قراردادی به ارزش ۱۱۵ میلیون یورو به منچسترسیتی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/91307" target="_blank">📅 17:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91306">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F24ohzT7ilKo4X7OBuRmFCftOyRzV1ySDH36bYO9cvs1Og80Y9ThS_t3XtLxdSD-kDtUPveaMv9g4wDz78t5e19X9tXgA8mSa2yobznRhuNS1MhBFQlMMQHHQaymxXAdhV-ljVRJb_xu74Id1DIhc8cZz98cjfp39_CTIhoAfAMDZAviU493cIWcN08ZBHwm3H0QWMpr5ZN89j6qtyJlEf-Z_FZvqyu0KU0nIYghHFmcebAkRr0ZVpkEcJXuj7fZZgNl6wDTW1JYbGNo6j_btR31bMogWSGZ99XYDSkWukTXlNvVqOE4x5uvqwQP5MbzJ8As3EagIPlXObH-B2hvvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
شرکت آدیداس در حال آماده‌سازی برای عرضه نسخه رسمی بازطراحی شده لباس سوم رئال مادرید برای فصل ۲۰۱۴/۱۵ است.
❤️
🖤
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91306" target="_blank">📅 17:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91305">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHi12gID9I4LBc2KhQzYtPg_e8iLYXCTirMifnsU7dycBGcZ4soPE2YXTi7l7jthM1Nt9FUoxxAr2cp3duCOqz-RXGHej-1KwOkzUTRpJ1_ozTbIF9hkAFO_J5XaokW8ZakH86_TpokxPcA47kf5OtCSQfw2Sd681BmLPGHAJXmWtEwiUenn31DyZOxb9GQ0cDo60cyPdZ8ee4O8PhRqYwvZPRo79QTJ94MVBQc_WIeG14bqpVWobfYa8azfb4Hmo4kNhUSH_9Oj5CC_J7LX-Yxo3H8KRirJrlZwBXwJc8CpzDT0xWyoY_RQTjdugD7u7zIrggBu5-Wn5cwwSD5q9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فلورنتینو پرز برای نقل‌وانتقالات تابستانی رئال رقم ۳۰۰ میلیون یورو بودجه تعیین کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/91305" target="_blank">📅 16:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91304">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgsFQzABljBOS10jZbv0RwXnVLN__Ts_m_8JQi5dcCc4-BPcrlmLz-6BIznUuHeu9IBM2yP2WUCWuIroxDruU4P5klssqRHD9Lnzfpy3uThmmZL-wiRjjO7FVuVU7LpOk1dFdZhJeQateIWoQV5M9p3QmvDQTtm3JnsBMi8WM6Y_i5vMkXCU50G8zaAe92bP6phBLZ7QsYX2GdPxzZ9fmhN_xIw_yLpxRlRtS-nGu3G48vJ2hSyZ3aXX1hl1WO31v3nl0k3i3IQ9ZFsq3rMS0M2pPtlIgRcYHeFkRi8Mdy1cLDaPx8CoQvWpAxtQ_J9guEw9i4VuvZOOXaGNZmV9Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو : پاریسن ژرمن اعلام کرده ویتینیا و ژائو نوس تحت هیچ شرایطی فروشی نیستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91304" target="_blank">📅 16:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91303">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lu5hOQW2c-Wy7bzA6VHnbxtYxf36RyCy4_mH5tGpunoSyPcO643HpE6o1EyIhvKg7eComIm32h8ggFkUcuxaiBQOn70R39Svks5ANNtuwQsgU4SqmmtYvT0-VLWIZJC2wK_jQhsQOkErJb6H23Cx5LFdQp75qdw8egAoFxICxJRthyV4XM3zkfwYlC39OGrdLWG7YeytgQ_Lu9tDx1IMWOL1m4NHCYOhdvD6CfAPJuMLam-0oUne4Oz1xPfCYAivwbFgoEfGdpdwCQoBr5DzsBbW8zKbmZdqyIuTOuiY2KJrl4RBQn1-LySnOLB-hnjJoKne1A0kIISe_bEhRPS3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
#فکت
؛ اسپانیا از فینال جام جهانی 2010 تاکنون هیچ بازی را در مرحله حذفی جام جهانی نبرده است.
· جام جهانی 2014: مرحله گروهی
❌
· جام جهانی 2018: مرحله یک‌هشتم نهایی
❌
· جام جهانی 2022: مرحله یک‌هشتم نهایی
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91303" target="_blank">📅 16:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91302">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7bOGioyTcjyA1UGJAbkwLd-Ogh_JeQFgJOx6VmGL0Urck8LmwWXIWt3kHOqV1NV_sm6qJCY8NuuoJszKg6tgG6FK2cJlDwaJ0aeYVXj9TEUkdpMvesptBgf-qoxNJ1adcceHrT2ERSWjCEcF1JLpHC6fGglpcnfu5zqWTN9Kjt4x-MtBtDrBeX5Np-DT6ssi92lm3eYHDf3WXLhL-rjglXO-oVyMtbQMV9WVl4kdjOmlFpFscXDXfqDd_Jhdr5KZ7QqIV1B0wA4efXzMSvxiyOfOuE0XHlDeAJfWApZkQCuB_PLQ2djJJL8TFNMRInsCtd8sW6XjUJSrXWnOCp_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیت‌های سکسی پرتغال مناسب برای انواع و اقسام مراسم‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91302" target="_blank">📅 16:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91301">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bcfec576e.mp4?token=XH9Q3hOUxIle_cdYy-JQbuddoX9drWTYWeDIUsU3smIvVaV4-hdzYtH8hSEjQW_7rQX9VN4Voj_N_4pVbHxgy1QWY2-OoF4SQnubKKPAfU55P0cnrcGPUiRTstWsANVqOfTU8z9sGsFKsZqGUOzhU0WdJ7wjHu8DsYe_mA4zLPYQEQ0TBRkh-JGzxtQF004-OtgT6NfsRYA4chjzhspEKY-RPcAb9znP_71JkcCIKW5MQ1zDymGXME00Hrs5DiiRzMl367dndvT5J_F6dWj8M6Wiq7GFkkeWjHilSv9pHt32LRy80w4e0kMRiJ4oRM6PIRzyNWMEQu3Lqh-Y-dZ-WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bcfec576e.mp4?token=XH9Q3hOUxIle_cdYy-JQbuddoX9drWTYWeDIUsU3smIvVaV4-hdzYtH8hSEjQW_7rQX9VN4Voj_N_4pVbHxgy1QWY2-OoF4SQnubKKPAfU55P0cnrcGPUiRTstWsANVqOfTU8z9sGsFKsZqGUOzhU0WdJ7wjHu8DsYe_mA4zLPYQEQ0TBRkh-JGzxtQF004-OtgT6NfsRYA4chjzhspEKY-RPcAb9znP_71JkcCIKW5MQ1zDymGXME00Hrs5DiiRzMl367dndvT5J_F6dWj8M6Wiq7GFkkeWjHilSv9pHt32LRy80w4e0kMRiJ4oRM6PIRzyNWMEQu3Lqh-Y-dZ-WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
شیث‌رضایی مدافع سابق پرسپولیس: در دربی معروف آی‌بدو آی‌بدو، علی‌دایی تقصیر باخت رو گردن من انداخت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91301" target="_blank">📅 16:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91300">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db9b67547.mp4?token=RI7c7mYPg0LEN32nHRYd2aWGWnhAcrqJTp9pmSrsezvplOypyTr-c9bL9jzByX4hnozTSgtppcvCd5l75Ck9I9cwChDYp0J70uxjCXyDlWPK8v_rjPRta8Wxsg0eOA5VU5KhqzdEq7LVFMzGK1Y-mNZ7CdCFu3OE1ivsgsdloBFgmFARKHVv6f3kdsq5rykrjKEYlGcwBVjo6OCt8VxgBfvWw-Ctbk-6A-7snNb1xpwcm_ugc0yN9y0zr7Nv89Fru-RaEydu_2Pe2VaXUJ1Rr-YRWLCf7YmFiWap3CWIWYqIB9prcW0INj6GCcCRqermqBaRqA_PnDz2oq5XlJzEyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db9b67547.mp4?token=RI7c7mYPg0LEN32nHRYd2aWGWnhAcrqJTp9pmSrsezvplOypyTr-c9bL9jzByX4hnozTSgtppcvCd5l75Ck9I9cwChDYp0J70uxjCXyDlWPK8v_rjPRta8Wxsg0eOA5VU5KhqzdEq7LVFMzGK1Y-mNZ7CdCFu3OE1ivsgsdloBFgmFARKHVv6f3kdsq5rykrjKEYlGcwBVjo6OCt8VxgBfvWw-Ctbk-6A-7snNb1xpwcm_ugc0yN9y0zr7Nv89Fru-RaEydu_2Pe2VaXUJ1Rr-YRWLCf7YmFiWap3CWIWYqIB9prcW0INj6GCcCRqermqBaRqA_PnDz2oq5XlJzEyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
🙂
تنها چالشی که واسه تیم‌قلعه‌نویی ساختن و پسند همه مردم ایرانه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91300" target="_blank">📅 16:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91299">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjQ9roMe7Y_66haFswV_oTy5K_cg_fw3BqNsIdrCCWLD51X8tWvxr30vqMrqcq5shI-LtkahpeY797tm55bZ-XQYMyG_sG50obPyBm09Els8exo3yyqcA8lf_Va5BKspsWdDF-mbM5HuaM1YelxM6aWChcEUT534-jQlzXTlguCi9PJbXHNjHu1DBz98WK0YAfL0VCRORlXaGsWvkRH3GbaCJsuGyMa1c-XMRqxaCtmx4hrCsO_y1vedQBBlsqr5kBh9pMkiI7wannq8K4EC3sJbQATTVwwnIQL7FoL3s9hG8Oeuu911L3TCOC52rMBaIFfZ0tvOTpC3xAoDQfV3NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای فرانسه دیگه بیخیال رایان چرکی نمیشن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91299" target="_blank">📅 15:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91298">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUctaET4cUb5ceyjKlLOXE5WmGtS-hTF0SDJwWjMbFpqDWzzWiZ8eeEu7bJhGa4TylTYBUWUV1I2ZjijAyrUviO3lXYwut5FTTGjT1Uhb41_wZxW1m6NmZE_MKtnjDssQ26QM5yDWJPGWrQSB_-jF8FQzTL3y2V6XewFax_uewd-wRx1poTmWF8MZXoVDvKOiErsB2FwqNmtMQ--61jdPPofPuZubcgrocasK9iHpiJiUzRQlq8nkerC5IFEoWHOmblklLFsG0ih6uPC6lxJ5I2QWc6UtIRfuLqeqTFweJrvHEFZifsH2dy6h24pIQxknCzznzn2WKgfs3qj3A4xiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمیز از نظر پسرا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91298" target="_blank">📅 15:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91297">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c920142fb.mp4?token=nuFsDsWZhaaILeZK2YSgBOrYwBHb1RnxztR0YCEKTl6vNKDyAxzXXK5XOc6El2BLGqK6SSb5RysN-JzTtf65z3Nuy_NrpGf8wNo5fOFpH_Wg7cYcWey1BoZ6GYA8CUtL27llKVWlxjRVa_vf6B6RoXAU7UMJgmDt-PXjm2wklvHBLj8EpaXQeJt_321mDhzLmS7JIMRygPpAW_qwRMDyq-Ava_4lY1R1n9WzZp5fFdVMnQpGNko6dGmFU0nUL5HynreMWmQxUIW7oULi31kwqOHNiyskfQL629Zguy9Gs4OwZK3Joj-opcShSZ6JKzG32LzRjS4hvK68GJ-SB-m9rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c920142fb.mp4?token=nuFsDsWZhaaILeZK2YSgBOrYwBHb1RnxztR0YCEKTl6vNKDyAxzXXK5XOc6El2BLGqK6SSb5RysN-JzTtf65z3Nuy_NrpGf8wNo5fOFpH_Wg7cYcWey1BoZ6GYA8CUtL27llKVWlxjRVa_vf6B6RoXAU7UMJgmDt-PXjm2wklvHBLj8EpaXQeJt_321mDhzLmS7JIMRygPpAW_qwRMDyq-Ava_4lY1R1n9WzZp5fFdVMnQpGNko6dGmFU0nUL5HynreMWmQxUIW7oULi31kwqOHNiyskfQL629Zguy9Gs4OwZK3Joj-opcShSZ6JKzG32LzRjS4hvK68GJ-SB-m9rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه نفر تو ایالت هرات که ادعای پیامبری میکرد، این شکلی توسط طالبان بازداشت شده
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91297" target="_blank">📅 15:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91296">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4LHVtuVqF_EK-Rfe4ToizgMxWeQ7xPY_JlRAA5TNtvNTNiwIeHTANJdFlw0YA4cwNeqFSBwKyj1MaOfmZRU-hu2zekDUe7r4Wb3GI6JVMwXFvWEV6I-djW6BCka6z4kEtKjcVUgKF9JJl30qTp3k2AGbWmDf9dJGGVokMJP-VA2nbKtAyzqHMvRdN1my7qQ2-_fa4YY34WNqV3f4XpiVGdQYQJVgkUmvTkirHJ6qPoud50aPBlmn7Gj5iCItyoaI8Fhk-13INWcfIfogz-SBN1i3rRg7qdPi6NTyLcHw7kfzCoW2ixOexwMFSQR6rhp4rMddO8oYvLkbS8fb__0zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی‌ورزشگاه‌های‌جام‌جهانی؛ شماره 7
🇺🇸
استادیوم آتلانتا (Mercedes-Benz Stadium):
🔴
موقعیت: آتلانتا، جورجیا
🔴
افتتاح: ۲۰۱۷
🔴
ظرفیت: حدود ۶۷ هزار
🔴
سقف متحرک به شکل گلبرگ‌های گل
🔴
یکی از زیباترین طراحی‌های ورزشی مدرن
🔴
صفحه نمایش دایره‌ای عظیم ۳۶۰ درجه اطراف…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91296" target="_blank">📅 15:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91295">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoi-3AM5uS0unJFCa22Lls8OJjkYOTsu781LJgUf3rffHo8c3vfDr-GjLhXcfOm_MtywdogGkApWlMlLm8Yvyek4eGwRz5ISiotOVnHW--6df7LxIHTQ2VUvUvuVQy8xT55ANnYY8iCv69dTqy-4R1yJgI3US_erLXxwaeZ7-vsq2cC4m3kn6DmBk9AJrhRUSBwrM5iZtQ8RcgKyi_O2jaxNEAgKk6LKCF3tsMpJtzWvGwrHI1qTrYum2UiUOr65Ms3G22lvcipBzC3wE0vDNJvl9NxN1LynkR2egcmqOcri4KA09myDRbUiXn-lvzFTdeVjbCG_sy6eezQ0n4lYBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی‌ورزشگاه‌های‌جام‌جهانی؛ شماره 6
🇺🇸
استادیوم منطقه خلیج سان فرانسیسکو (Levi’s Stadium):
🔴
موقعیت: سانتا کلارا، کالیفرنیا
🔴
افتتاح: ۲۰۱۴
🔴
ظرفیت: حدود ۶۹ هزار
🔴
یکی از استادیوم‌های مدرن اولیه آمریکا
🔴
استادیومی هوشمند و دوستدار محیط زیست
🔴
دارای فناوری‌های…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/91295" target="_blank">📅 15:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91294">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGJCcXYL5BaGffNxyONmzHR8hMYV3vC2YTs99HSNbzHLPP3tI2sztkuaU42-SQvEcKx-sjHjRtf4rH19E_OyXbyCv_RPZx0JoQd_QIna87cSEKQDyDkgdAon3Cysx7l6TzU5qucEECkTGw2XHCA_dMTw0sid5ITulJ7TUV-yMTdyoXvTHXgvSRZSyIA2wqBnbphGm80Qh132IGhbwiQB4i8qj-LkBGEEoU2dP0l5l6DtS5s-eW2q28lt9au2eBAe6UDftmYxWDfFbGf4ObxFGyUjtvbNFhjcq6JppufSR8p8aX0vb2wVFKSiO5SR7s3w--0waAgLXQLHNIWHvReSBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی‌ورزشگاه‌های‌جام‌جهانی؛ شماره 5
🇺🇸
ورزشگاه کانزاس سیتی (ورزشگاه اروهید):
🔴
مکان: کانزاس سیتی، میزوری
🔴
افتتاح: ۱۹۷۲
🔴
ظرفیت: حدود ۶۷ هزار
🔴
قدیمی‌ترین ورزشگاه‌های مسابقات
🔴
دارای سر و صدای بسیار زیاد و شناخته شده به عنوان یکی از پر سر و صداترین ورزشگاه‌های…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/91294" target="_blank">📅 15:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91293">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIxiSu5Ur_bbxuMhgVCHu7ubnzZvhR3vcgWylOuhxWM_sYhtX3A4KBhRTm_V57Sj0BbSMXW3onc7gixTnRuwSz4BeV-4rV_JAfwnccT0dubJZS7_tMoJ9EDx1Kx1fzEzHWU2cjuT6dmhmsaDX77qlfpH_w6RI3mlvOUZ82X5EUrT97Sp15UGgzeuNHu3qDs3vjqgcxx4lOCLx9rXUjqcudab6t7f_fIgPGlDNHNfyQEvVHVohzG8aQkih9p7zdiQd0xbyhFH5oelaQig766OLcyioH-mTuH9puuzC5lH9Jsg53su57u26O07zAt_qZzOrvmepsS1h6E5nmfDJz6ABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوناهم مجری دارن ماهم مجری داریم
😔
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91293" target="_blank">📅 15:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91292">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ss4fL-JEn77df96Atj1KseNvoIB646ovFq_swdkGEW5IK4iYIS6TGR6ltRxpgLzxnvuPOeCQEo3Q3jFtAhzQ3lhnXV1TVovOT-TP0SPahSEakZLpaYRnmS_Ji-uk6CHkeZYY13oexsrCZU6LBFugNiRxxEcEAU3tUulIA2xLJytmSZh_N6S9FYYrVDRDjMPbrfBZb5iAuIgCAqkNbtCSGQkTO55RSk3rTZ86kmE41IO8rLrPzrqiuI8aelmoWvDUDZhWop-k-xZ98oAqZCeyACi5g9c_9Twl-M3xbZqZ2T5lx1_oYxCu_Y0N22346D9cu_Xeu9O4rfJ_Bfz3xPNeZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی‌ورزشگاه‌های‌جام‌جهانی؛ شماره 4
🇺🇸
ورزشگاه فیلادلفیا (Lincoln Financial Field):
🔴
موقعیت: فیلادلفیا، پنسیلوانیا
🔴
افتتاح: ۲۰۰۳
🔴
ظرفیت: ۶۵,۸۲۷
🔴
جو بسیار پرشور و هیجان‌انگیز تماشاگران
🔴
ورزشگاهی باز با سبک سنتی آمریکایی
🔴
خانه تیم Philadelphia Eagles فوتبال…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/91292" target="_blank">📅 15:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91291">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dx_cDQZQrf66tSvABdX2INqqp0r9XJ6UQhQNyp1qPFQqlBAImhZ2EoYUine0BU3fRclCbZy8kv8gCs4CZ2Rz4Ixu0fZLdKJ64f0IENFgEEJApJR_Dnz4GhTnQZowtcPf1KmWVloupjndRSMw7WNe_eMC5jr3m-4XdaDKsqNZr_YVAnK0JXN2O7T6tPicgrp2LAm5Vl04hywTmy2wxh1gzZae-NGQc84uNzLPtjeHHCl47Bun37o8wyV8ux3iPPxifcEyHNlOJAe49KBIOhYn8Q2F6FzxJ06m1O_f5L_YceZHVfe2iFCslEJDipL_yQ_cxbdVn0vDvSMBQsiMUOopsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی‌ورزشگاه‌های‌جام‌جهانی؛ شماره 3
🇺🇸
استادیوم دالاس (AT&T Stadium):
🔴
ظرفیت: ۷۰,۱۲۲
🔴
ساخته شده در سال ۲۰۰۹
🔴
استادیوم تیم فوتبال آمریکایی Dallas Cowboys
🔴
سقف بازشو
🔴
صفحه‌نمایش‌های سه‌بعدی غول‌پیکر از بزرگ‌ترین صفحه‌نمایش‌های استادیوم‌ها
🔴
استادیومی با…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91291" target="_blank">📅 14:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91290">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEEA9IX-hTABJV9MO7RtsGMO4EgT_d_0PJOjFe_75LmNFafLMH4ME_R0JRBKB0AcKbAZ3gDlspC-RKldRrgO3TnMUp3BjGjsC7JaJVk8ZdUPhbVUKS5GlQp6lbobrm-X76oIIvmkBtgyIL9y0A-LAxNmQojEbEt5ZBPklvc6E4o1pltGtNTRlWZVFjm_YdzJfdKRKNqTUt4QQjg-HjOllA-MMcWrF0MNRkrkop0FbLXL2qz-C2OdTWwjmLzjuCcPgyAR8RK2t00ehNDBzzn1ZKlf3CefmkMAmrk4J85XkM5WrJNAztnQewesmUh7fuduHEudVM7gNFTZ7Li8q_aNQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی‌ورزشگاه‌های جام‌جهانی؛ شماره 2
🇺🇸
ورزشگاه هیوستون
🔴
مکان: هیوستون، تگزاس
🔴
افتتاح: ۲۰۰۲
🔴
ظرفیت: تقریباً ۶۸ هزار
🔴
بسیار مناسب برای هوای گرم
🔴
اولین ورزشگاه NFL با سقف باز
🟣
خانه تیم Houston Texans فوتبال آمریکایی است.
✅
میزبان ۷ بازی در جام جهانی ۲۰۲۶…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91290" target="_blank">📅 14:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91289">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tomTw2SyLOU8XSEfcGdrZZrkGZT85I0BRY2GdPCUWEX-yDrc9goFJXBJmNiYhqJcHCDYijb8hQcuUTaO1I0QZfoQJc3L6aN5vCZf_O_78dzpZup8cMNY36pzLNzE0ryLkFz2kNclG6hT5Yyb-i-Mfa8PmOK7f-vHKk4soa1YvY2ybxQ4Rp5xnYC7ODBVPM00SC0BNSRTyGbG2xp3z9y-eJkyv5L9vQRxVEA-43Yyf0J_vKPGpCZ1fO-d0ae66rpmuBE5Hdiqof_CkDzh1XhuAnXq4Q4PdpLVO5_cIz7XcMRAcGSiSLzlPbGsz1GI1FovOw6SnDGaXwYpIPYdW1uUxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی ورزشگاه‌های جام‌جهانی؛ شماره 1
🇺🇸
ورزشگاه لس آنجلس (SoFi):
🔴
ظرفیت: ۶۹,۶۵۰   /  افتتاح: ۲۰۲۰
🔴
جدیدترین ورزشگاه‌های جهان
🔴
سقف شفاف
🔴
صفحه نمایش ۳۶۰ درجه بزرگ
✅
میزبان ۸ بازی در جام جهانی ۲۰۲۶ خواهد بود. ۵ بازی در مرحله گروهی + دو بازی در مرحله ۳۲…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91289" target="_blank">📅 14:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91288">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RczhTegG46eXhXinGawa3ecuWkHKVi9AFd9lQvUpF2hhc6jHte2HbszvooW2_3EZuKn-48MNrjOnsMArdkeZIbYD6MhWuBudYlKCHgDkKS4nYBbYz1B6V1gQoDxE98o2FvuiGLbX3ONn6rOB6zvMWuU7j0g55-XBJpYFw5wQH1VrIJ1c607uHt_2ISNYVa1FeH27rTrNr87eFggbhPlYvP7WrstyHaNiptefZO0vS-Ebjft_Ox33qDIMWivepbL76dNjcc7YL5kUR0jQyxO06VronVvDusMoR6Tn4hoyjrvt96GVWWwlUKeYszjqRBGu150j-sxJbV5O3Dx7jvRSoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی ورزشگاه‌های جام‌جهانی؛ شماره 1
🇺🇸
ورزشگاه لس آنجلس (SoFi):
🔴
ظرفیت: ۶۹,۶۵۰   /  افتتاح: ۲۰۲۰
🔴
جدیدترین ورزشگاه‌های جهان
🔴
سقف شفاف
🔴
صفحه نمایش ۳۶۰ درجه بزرگ
✅
میزبان ۸ بازی در جام جهانی ۲۰۲۶ خواهد بود.
۵ بازی در مرحله گروهی + دو بازی در مرحله ۳۲ تیمی + یک بازی در مرحله یک‌چهارم نهایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/91288" target="_blank">📅 14:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91287">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arlATqqbgXREESAPDo7FyahZuJEIcOu7mMTpDqDJLJbXbuT9REHsK2BWaS6RZki6WUVM9TjekY6cthtMThV4o486GWj3bCSO3FJi46CDgviU2NXVK1OTl9YuRR0XyUd5GS9UOR55YmVr1WkcePe-PnAYMmVMFVSLE3hZot3Oiq1HSnrTMNsSeP1ocrlha_Z8daNtJH8QrQ_6ZX2ehHFSbnNY7iidjfT879g8HwcU9YZwjE9T6hxI8RPLQlQs2p72xIEeYLc6NksORSbmUDVx234VdmJpIH-RVIYp2G1OqxgxbQbP1JStUTAl8e0VdGCmbgN9yCNjW68eZgAfEf0wTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🤩
#فووووووری
؛ رسانه‌گل: الوارز پیشنهاد ارسنال رو رد کرده و اعلام کرده نمیخواد به لندن بره و دوست نداره در تیم رقیب منچسترسیتی بازی کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/91287" target="_blank">📅 14:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91286">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPY5VXDQedny5l-h1JIZSVMKvjeLgZHXDN5eMWqJLJQP5IS0qQ_dy-zMYRD1-ao9x0pZWH3VB1GTu9wU7U4J3CVySABA319E7OYUQd4OPjmt0EWl_fgpA0eaEpMsMv3qAo8-pvvXg42SoqoCQFRKHkb9TnYionQK-6CqfAEpJs0YtyLWelQmaGTNQGI1aICckvEF93mxevsCk0TuVyK7qrRNfDb8fMDa20d92zr3hXx4OL9MPzxyw1EBe5wGpVnSR49SYOz4Q6VBKyqEM8QrF7E0A0oCgzJtYeOGJuZm9ubjx4ozVPbMkl99mQYwHon0fg-q87pV5gLkjzsGO6OJ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
؛ براساس شمارش اولیه انتخابات رئال، پرز بار دیگر برنده شد
- فلورنتينو پرز 65%
- ریکلمه 35%
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91286" target="_blank">📅 14:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91285">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdeda036cd.mp4?token=sMkU94-HxZn0qLxhFcEatdaUVxU1Tq9PMtVezUGzW5DeWPzUdOqv-DtGkqVq29CucqVh0pTNx1dUYfIahV68unaNLCevd0p3laQ79IcRsZWLCNFEmpLc71Jvtig50eRVajxAhtAdDbpwIwUQqHE0HZxKTxOqNTDsT__HA31zAZBBPgZG1UAwUmRjJSsj2JH2pWYYOfh3ioCw_dC1lT61lbiAAp6EXcLnP_y2IRNoqWOpaxNiyN9c1qSYNtXgoywH8LPg3JDgObtSu52FqANwpZ8mFHrqPiAfEkHirXNCGeHNA-HZNxVRWhZhGRz7gWsDSLHjP4xnhC5Sc7gXX7eAiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdeda036cd.mp4?token=sMkU94-HxZn0qLxhFcEatdaUVxU1Tq9PMtVezUGzW5DeWPzUdOqv-DtGkqVq29CucqVh0pTNx1dUYfIahV68unaNLCevd0p3laQ79IcRsZWLCNFEmpLc71Jvtig50eRVajxAhtAdDbpwIwUQqHE0HZxKTxOqNTDsT__HA31zAZBBPgZG1UAwUmRjJSsj2JH2pWYYOfh3ioCw_dC1lT61lbiAAp6EXcLnP_y2IRNoqWOpaxNiyN9c1qSYNtXgoywH8LPg3JDgObtSu52FqANwpZ8mFHrqPiAfEkHirXNCGeHNA-HZNxVRWhZhGRz7gWsDSLHjP4xnhC5Sc7gXX7eAiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
🐸
قر دادنای شیدا مقصودلو زید مورایس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91285" target="_blank">📅 14:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91284">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21f03b77a9.mp4?token=TVJZu8LQ_5wJJkun9jCQqByJRW8VhypldBIaT64NLU2rS7qGdcpbrYIca8lsgq9Z-ASaluR0SMmlE5AVSshntaiQIyNKnCP0GS4JObhe63XkVT7YQwCIMVwnPjvqGvs6g4dltVH9nPORMWW0fCaXSGH198FthHH9p0ZhkRgiOUcv2_zxvdLrPr7d6cR4b_tOFTvUhLhPZzyYnl_S0K1qEByb1985BVGjzCuDZlk2H8CzfGwOFZb65GP8Jt2vIR4aeX-1XvCgjYOaaQU6LbjULIpDdQ45NgPjskaCGdyvAa5KsnGuM69txUBTy80MnrvWb9Q2Jd8Ahcd4x0Fa-srDwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21f03b77a9.mp4?token=TVJZu8LQ_5wJJkun9jCQqByJRW8VhypldBIaT64NLU2rS7qGdcpbrYIca8lsgq9Z-ASaluR0SMmlE5AVSshntaiQIyNKnCP0GS4JObhe63XkVT7YQwCIMVwnPjvqGvs6g4dltVH9nPORMWW0fCaXSGH198FthHH9p0ZhkRgiOUcv2_zxvdLrPr7d6cR4b_tOFTvUhLhPZzyYnl_S0K1qEByb1985BVGjzCuDZlk2H8CzfGwOFZb65GP8Jt2vIR4aeX-1XvCgjYOaaQU6LbjULIpDdQ45NgPjskaCGdyvAa5KsnGuM69txUBTy80MnrvWb9Q2Jd8Ahcd4x0Fa-srDwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زن مسی ماشالااااا چه بدنی ساخته
💪
💪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/91284" target="_blank">📅 14:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91283">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5a8cca451.mp4?token=ZWubIWUv8Y_sMVtqud9czvR-uZO8EqsTNI75DD9uGOlzOKnjTDjBB8CuSHjTKBfJFdJSUbGxPu7drh9ogoJXW10x3KFnxGTbPy7vw8wir10Pfi3lIeBtVdQSHoau69t6IHhn2t6coJ7TZ0givxCcKOAAajRNlcO2ZB2rYxxTjsIJmPLo4K0_oFWNS014C8L6PONIICAB4HZL9bcyEKB5j2eZ8sdx1byTQIDIuo5lMHJU6MAB2JahwnPnmiy8CObCfRtdhN4REPkOfOIvuO8HXGNDcTPA5Za1hHCEcqbuEXtCTyVO5iqj7xz-aGc29dmx33bITLmzt94-307BxFLKpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5a8cca451.mp4?token=ZWubIWUv8Y_sMVtqud9czvR-uZO8EqsTNI75DD9uGOlzOKnjTDjBB8CuSHjTKBfJFdJSUbGxPu7drh9ogoJXW10x3KFnxGTbPy7vw8wir10Pfi3lIeBtVdQSHoau69t6IHhn2t6coJ7TZ0givxCcKOAAajRNlcO2ZB2rYxxTjsIJmPLo4K0_oFWNS014C8L6PONIICAB4HZL9bcyEKB5j2eZ8sdx1byTQIDIuo5lMHJU6MAB2JahwnPnmiy8CObCfRtdhN4REPkOfOIvuO8HXGNDcTPA5Za1hHCEcqbuEXtCTyVO5iqj7xz-aGc29dmx33bITLmzt94-307BxFLKpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
بانوی جذاب آدریانا اولیوارز مکزیکی روند زن برزیلی رو تکرار کرد و بدن خودش رو پر از برچسبای بازیکنا کرد و از دختران سراسر جهان خواست تا قبل از جام جهانی ۲۰۲۶ به این ترند بپیوندن.
🤝
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/91283" target="_blank">📅 14:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91282">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34842d0797.mp4?token=YxhnFImZFfLurutQkEImxgQcMfatHeYGEiq1nRyymqi5QsHakuMDzIBehkdo94Vn5h7CmFSWK4syD5B-pHkvGQNlmVoAaDo_Nd6-QjPVMdcVqbBWlrARFNTOeUhHgwEureAlDolJnX-eIdf7YxrYfmOux0kcizfSmPHmvf6TVkTzVKpReYIz7h1cSF1RVCkFjaknLOJRUkBkdN-sMcMLDMBOKEhjXG5vrJrM5kIDccolRYT9i0I6ImYer-IUMDGxj5AUTQU6t_rkFIK6UIGKnsYYDu2L_Cm9xadxYrB3nrDbotgqZ4RJ6kIY2gpJ5blFANR2-l0js7P9bkDDgN2fqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34842d0797.mp4?token=YxhnFImZFfLurutQkEImxgQcMfatHeYGEiq1nRyymqi5QsHakuMDzIBehkdo94Vn5h7CmFSWK4syD5B-pHkvGQNlmVoAaDo_Nd6-QjPVMdcVqbBWlrARFNTOeUhHgwEureAlDolJnX-eIdf7YxrYfmOux0kcizfSmPHmvf6TVkTzVKpReYIz7h1cSF1RVCkFjaknLOJRUkBkdN-sMcMLDMBOKEhjXG5vrJrM5kIDccolRYT9i0I6ImYer-IUMDGxj5AUTQU6t_rkFIK6UIGKnsYYDu2L_Cm9xadxYrB3nrDbotgqZ4RJ6kIY2gpJ5blFANR2-l0js7P9bkDDgN2fqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
گاوی تو تمرینات اسپانیا اینجوری رو پای رودری تکل زد که نزدیک بود مصدوم بشه و کلش کیری شد
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91282" target="_blank">📅 13:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91280">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SK2DtBowMAb40U58YlqqA84RRNAoiFxdRQKYVxEwa0zklwJC2RP7O9bd8Nzje2Vwkkwdgw3N4GIo6TWrJw7_VE8U_ZPLZOc3JhL1kqXJUDEaeYytpNzf8-_wRbXi_rh624lwKjW65aBgj3pgEzAHqZ2WVH5BL0O0ELSEa6Silh4QQ5VdR19-mgZDhGJF2xs-mEvWmKjIxolXLoBPGXBB0t8Fx9mESWQlTFCGeDtNNF-tbvmaVmA7VmVg8H34Y85t1HbGb0vfJFFVqSJjwQZvQP1M0pY6aN0jg8pi4_BjN45Ocouv61vNvPrmjmVM6W-zGz1YNu7l-Xj1Fzxo5_Yiog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rZuvSWyA7UP_iCMQj9DwVgqDzMXW9zuDzcz2fWWw0rc233f8JjjhwaT6C9X5XwbdYYsxqNsnVJP7ogQ4hpYJHvJhGTggIqLc7pHz4C_EzT2IUBEOdkLLi_Y4V3ZWmAqJHRNJNeMEp91m0UlfGHVYV88qgzdArj48aBrae162joodb6bUW-lvP-A19iv1j3-8lRSgcObpWG9qpio-BiJJg2K6P30fnjAjHmSe5z5706N13uLw2H3uhf__CC__4y_GWPSG8-brV3GIiBSHne6KCE5LM99oila1tJQmkYqHuLYropBRh5ccmA19ijGT1VKrZ8KJrV-cwJvjSoYKLUF0Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مدل مو نیمار برای جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91280" target="_blank">📅 13:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91277">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BORH9lQuyPHgOTgzwENapsroTk9nSSN0O_3GwQNNVPFBt-gQnjdJb6hF3HtJqkgTjBBB25GXwgUd4NbIuXlPXjb6NE2u5KYc4Htkw8PhMuZxKN3Uj5ZIKT1xPAzMQ5K3zHcnO1_Y0uDcOqQwHr38eklShWDFxXBl_svDQ4yVJaGPrZxdNMu3OSsVpu1Iy9A_OLHwxvMQOPL8t27ayDNRaQaRa2S2L_zDVIvMb2NjoyggsyZlAO5amyx-Mi3xXaT3oUxLf44g29UIwlHUlobE_VFFhYUv0RSn-3SbihIge3LG7kv5lb0MYmYCdey0UoEg3q-YYi9A_tbIHDQinl-m4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N49SYGagtc_YOGO_uf6LxLPbvidxyOe4HqJKawkGf4eeiMihYYCYdPsCdVrahjChrbF5uVX0L4DCUtLcGXy5VgEePxSHyMh4pO6V_cIyDBgqbQlOR2XLHLi7-73wiXDjMqtGf2dughy0zCp_EEZSS_LWa9XtvS4aZMWT1cUYZJzWBpJMJosQuQXJBlQEgx7CoewefumqfAwtaY4tzJWKebpr10qSHuZHVZ8UkvoisOMqnYnJd-_pcel3ceBzSjUrXbHv3-af5wQySw7h6iywiI0T1xrKkCV5S0LfVVOyZPl3VUAQ4hjGG9dS3ofrOnyPvFNRSTjmFERZfy6_ZKO9Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cge3Sis94gsmLwERF8DBvl6wxn-CpS2OOwodL1m1Z8OmYDFJQaAs0oVkFu5izqdl59HBqdH3bF05rfCVRaXBEx-dFNAv3SvVD7-jImDwa3gnQANXz6cuzYb1khR_OgjTXPMGTrZvRX-pKy_fYbJu7v564tYpD6gN8IdGuHjBoz5MfYCnYNhCZjwSv5TcyeWzDGqX9Pk6I-K-EP8CyJCqbSuNmzBCf0mvRN7L_Zg5mIZEuMp7QTt93dgZCSWzTQnY7CmuKocf3T-71RbfVHg2HxM8sC0N3woZLzT-A-LHmU9rIG_qpz3us_jHSDpDr2uV0zBqgr8pyo05hqCE5lrImg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حضور پرز و ریکلمه در انتخاب ریاست باشگاه رئال مادرید.
کی رای میاره؟
❤️
فلورنتینو پرز
🔥
انریکه ریکلمه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/91277" target="_blank">📅 13:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91276">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2ffdac381.mp4?token=WRUeitC5Wm6tRLNOqOvXpxEFrdGRbX1PUTpbf9qwSt3Gx7WKTI4vrsZxc8pjzy4i5tZoNW2OgCQccRiM4qAoxmi0bEcR7dtnYYgj4xxNncP5JYHXzdYCrASD2ua6E0cIdxysGYWiYolAmv7ymIylSG2pbPgYC5W5TMirHmor8EU8dTm4A0KWgrzNUNOdOkp23z1Lvt7dyCrcxiJZJiITYKpHnphgEUQXlbCoV2CXZyQ4fg6Cpe083SxIPzcVd3b1uG9ZV19QpWSnOqFSsFynhToDxekYBhYlJR_GV6xksXtBQv2Fo_hFiUGQdgu5OSuLMqZh61OoE7LI-focZfLeKCnb8yG1BumrwDL0_E1ITdo12eRVQ46hzw0hhqBV4X9gaFGvBGBdj9DZLzX2WNt66EeznKaog5cM6p8yr6TiqIhNAWMn8W-7qP1toNnydJzQM3rDgKHhfwlqLO_D2gz8-wTxHT1oADkSw-eEiMgI1jopbUK0Ia-bW0FrpTPCyafHYlumiFTnUAjwqs7Vh1ghZhibEMHCmx-bOSEHJx5V87l5-Wi5b9VT08awHstgGRugBRz3bNLEkmts6vzFdXM1WaeV-2P5eZBA4aNkkafyXhDbq8JYGRBxtVoHkvFEci_I4vJjsbQH5khaI5kAqxNXjcRW9xzuvhDMLCXrDHpVukI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2ffdac381.mp4?token=WRUeitC5Wm6tRLNOqOvXpxEFrdGRbX1PUTpbf9qwSt3Gx7WKTI4vrsZxc8pjzy4i5tZoNW2OgCQccRiM4qAoxmi0bEcR7dtnYYgj4xxNncP5JYHXzdYCrASD2ua6E0cIdxysGYWiYolAmv7ymIylSG2pbPgYC5W5TMirHmor8EU8dTm4A0KWgrzNUNOdOkp23z1Lvt7dyCrcxiJZJiITYKpHnphgEUQXlbCoV2CXZyQ4fg6Cpe083SxIPzcVd3b1uG9ZV19QpWSnOqFSsFynhToDxekYBhYlJR_GV6xksXtBQv2Fo_hFiUGQdgu5OSuLMqZh61OoE7LI-focZfLeKCnb8yG1BumrwDL0_E1ITdo12eRVQ46hzw0hhqBV4X9gaFGvBGBdj9DZLzX2WNt66EeznKaog5cM6p8yr6TiqIhNAWMn8W-7qP1toNnydJzQM3rDgKHhfwlqLO_D2gz8-wTxHT1oADkSw-eEiMgI1jopbUK0Ia-bW0FrpTPCyafHYlumiFTnUAjwqs7Vh1ghZhibEMHCmx-bOSEHJx5V87l5-Wi5b9VT08awHstgGRugBRz3bNLEkmts6vzFdXM1WaeV-2P5eZBA4aNkkafyXhDbq8JYGRBxtVoHkvFEci_I4vJjsbQH5khaI5kAqxNXjcRW9xzuvhDMLCXrDHpVukI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دریاچه‌ارومیه که حسابی جون گرفته، این روزها میزبان پرندگانی هست که چند سالی از این مکان مهم مهاجرت کرده بودن
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91276" target="_blank">📅 13:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91275">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlZdPv7_YsJRJ39CvKbxW7imprK0taZjPwPM1Ta3QqUNl5FRqcDMK2luDoCjSUWdenXnyPSjKzxldYFsV9HzwWLOGZS7fxohU310_h7J4g4mytCoCORLAAwX3FwbyM58hch9VI6I_nuklAF7hUpKjsZurennAszU6R7iHrAjYG6OeaHzBZ_kcxY7bljeL1Kvunq44ugF_6Rs3W8jm1AUB5Gcu4vV3_H4Al2ccxCVu69-iGuXXU_sdeAGxhsSLY94eJJ1Xbflmq6bpwkF8pNLnLRHn6iras19HjDCzdHmhXHLug3fH5tsnyNHvN1z_euzkdcGGt77_RSdCPLhjqG8zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند ماهشه امیرخان؟
🫃🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91275" target="_blank">📅 13:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91274">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVi5FrHfCfDtC3GyDNq0qak6yD_-YAcUOxtscZkBUY4z9FpWifYqaAF98nB4g70JQfiaa7WpelK7OF84ASPd1Yq1TjnV4jDaxU-C7QTvcZpSl8LlcPTUZxM7BLwLGVlk2rE66ER6B79KfmEjfyViE8bdIVlY3YiTNpQpRg1SoE2Lxp-EK8S5DQAPurUHYxXQgLl_049kPOWteIJFubrIV8CeW-5yVeVr5WfN2jxK7r4PZOx9c-bmevZ2EzcaSK2UhcI9Yj3sd8tKVvSV9O-0V0yCGVM-FrXPao6hpiTsSOzW0qHgDwRA1XxKKukKXPF8Bx1iQXn_tkoUjppPmoowJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیکولو شیرا:
ساوینیو و تاتنهام برای قراردادی تا سال ۲۰۳۱ به توافق اولیه رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/91274" target="_blank">📅 12:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91273">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpWRu83BSLByGT_gmPXtN0hRJZr8WxIN4ofZdjaDcjEzbfdMrs4wtwv_GKz1eA-01Jv5C_Bmq3Q-JvhEfPZ0DFvhUSTkX9ipV13Sl1__X6kkVR8lZAK0KodJd5VMwF5o-OzSI9OFJczYWpzMw7u0raHctF9Sq3Tkme8GvlHKDyP8nl3r-92dPLFxIAmEGxUsp7R5jvz2FH1BxkFRXJNaiUOQlcYUVWROT0Uk8y8N1TQBPBME6LzG1NfFp_fOOGaqds4G3huyWaUXOXW0Yg74sA7MWkvMGseNcXeiYo8qE8lX6XCUuPJynZnjiVdxJ0zRFdfMhN3GTaksjeUVmPzvsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز جام جهانی شروع نشده دارن شاهکار خلق میکنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/91273" target="_blank">📅 12:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91272">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b9ee999ec.mp4?token=OC_BQzgr85j12TL--rJHfJG0jBb9SAMQKc7iaaRZsgwWj4WGW-OFA6kBv_ryamR4MzKsnh1hz7C4nJHp06mrHNIZVogDU3MsOBPZnVdPklGXhKLWcdxVDQZvm1KfTnwKmOhfLeeMXIwo1A_B5Xq9k9XV0-Nj13eZDDHi7wA1spw9RJVhaKtRcjzSM64h6J7HJdQDH1qpTvAFOjbpY1BMFXJfcHkpbKtabR324lMrwO7zZgTk5uccVPtylPSdgMe6yoi6ANZZqEUaZXZLXwj0Q-9Rzj0A2stm4qXEbwEKPqu2yKyXNl2f4byLERss3E3edMfHzCC9_82z8BjaA5oKVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b9ee999ec.mp4?token=OC_BQzgr85j12TL--rJHfJG0jBb9SAMQKc7iaaRZsgwWj4WGW-OFA6kBv_ryamR4MzKsnh1hz7C4nJHp06mrHNIZVogDU3MsOBPZnVdPklGXhKLWcdxVDQZvm1KfTnwKmOhfLeeMXIwo1A_B5Xq9k9XV0-Nj13eZDDHi7wA1spw9RJVhaKtRcjzSM64h6J7HJdQDH1qpTvAFOjbpY1BMFXJfcHkpbKtabR324lMrwO7zZgTk5uccVPtylPSdgMe6yoi6ANZZqEUaZXZLXwj0Q-9Rzj0A2stm4qXEbwEKPqu2yKyXNl2f4byLERss3E3edMfHzCC9_82z8BjaA5oKVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت گروه E جام‌جهانی فوتبال
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91272" target="_blank">📅 12:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91271">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">😂
جمهوری اسلامی پاکستان دسترسی به اینترنت را بدلیل اعتراضات در کشورش قطع کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91271" target="_blank">📅 12:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91269">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djkcS75_5dGNiT1h4rG7f1xL90Wi21GxjfCFO8ue83W7opbCJaKOiFxEzJvi40fO2o3BGiWm2IgjVQfdmta6cjCTPOubNwIT2kCyAGAssok2e5dig501GCTF9VFhrTWpUzG_wJgENrQrt0na5_hsQSS6hqd05aNVpJLzzIJlRx-yD7GX6rskvWGOVayGeaC1oC5WsiqHtMn3eFqA_gydPZ5gCH1iS45Xf8FmnmRRq1tqlHoVjFPxc8uKq9FXFhI1O8C62VlAC5HRLW9juGiV9OkJ9j9UvB-ol8_cvSmAwWImpvMC3BOzfmXD0ZY4UwxB1r3Xnq8Vd8UaPH1Pedex5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
‼️
🇪🇸
هفت‌سال پیش در چنین‌روزی ادن هازارد با رقم ۱۰۰ میلیون یورو به عنوان جانشین رونالدو به رئال‌مادرید اومد و‌ در ۷۶ بازی با ثبت ۷ گل این تیم‌رو‌ ترک کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/91269" target="_blank">📅 12:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91268">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d1881201.mp4?token=eQ1ahuH7V7YhztkB1crEzEu_svJZ9KbHR2Dqdz1NqmE7da5GiNYuSloERjU28FqehS0ZkqK_5NIuQBJxhamu5jB3XgC3Su-XRGOvm8C5S-bpeZL-Irr0jkd-fFQjMisK_oYx3bff4FyBL8rPterkLw-pmE3pfijTPl_1Vfaa3qJeyCT936SRR7SxnU4Lp8ZlMtBJPnMteL3pkxuniu30cIg9Zlv5v8BYtmqa8H-I75BR1VG5ABFyUYBpb2v7EDKKBKlnfoycwjVdB3BMLN8CYnM5A_5dOdIL0w233PYe2WtlHZBh59Mu-4IIJJv3Ok1I7TBXEvNjjt7XoQaa07wE3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d1881201.mp4?token=eQ1ahuH7V7YhztkB1crEzEu_svJZ9KbHR2Dqdz1NqmE7da5GiNYuSloERjU28FqehS0ZkqK_5NIuQBJxhamu5jB3XgC3Su-XRGOvm8C5S-bpeZL-Irr0jkd-fFQjMisK_oYx3bff4FyBL8rPterkLw-pmE3pfijTPl_1Vfaa3qJeyCT936SRR7SxnU4Lp8ZlMtBJPnMteL3pkxuniu30cIg9Zlv5v8BYtmqa8H-I75BR1VG5ABFyUYBpb2v7EDKKBKlnfoycwjVdB3BMLN8CYnM5A_5dOdIL0w233PYe2WtlHZBh59Mu-4IIJJv3Ok1I7TBXEvNjjt7XoQaa07wE3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
باباها جام جهانی امسال ساعت ۳ صبح:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/91268" target="_blank">📅 12:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91267">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b2e6f956c.mp4?token=js2xJm8xLlmc3cmIeI_jG3ilMrn_shxC4K3rsb71kForpU0A-YgytWdsb7LakzL094-tDbZ3GFVrd-3vo2q_QKqaBy_OYDdwbFPg4ubLzcjC_M0eFiUR4SFuUS_1-1W7-1onqTGysWgzW_UnBXnEyvm2u5eaWOyddhsOI258N2nVQ_lMCrQc6ZtH5Z7QyuQd1F4zudaaCyLtbUflBCrYujWuDvqZJ1wlWs6dWMEH31kB-P7onbHglJEl6rudlyo9ImKiFP0NBrrWPL8_g7OQSP1o1TUvlZF-5qWq9ygutTe-mUnljUpnREiRiFOIi3hd8-9RBayar363LbAfBOewSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b2e6f956c.mp4?token=js2xJm8xLlmc3cmIeI_jG3ilMrn_shxC4K3rsb71kForpU0A-YgytWdsb7LakzL094-tDbZ3GFVrd-3vo2q_QKqaBy_OYDdwbFPg4ubLzcjC_M0eFiUR4SFuUS_1-1W7-1onqTGysWgzW_UnBXnEyvm2u5eaWOyddhsOI258N2nVQ_lMCrQc6ZtH5Z7QyuQd1F4zudaaCyLtbUflBCrYujWuDvqZJ1wlWs6dWMEH31kB-P7onbHglJEl6rudlyo9ImKiFP0NBrrWPL8_g7OQSP1o1TUvlZF-5qWq9ygutTe-mUnljUpnREiRiFOIi3hd8-9RBayar363LbAfBOewSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
رأی دادن فلورنتینو پرز در انتخابات ریاست باشگاه رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/91267" target="_blank">📅 12:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91266">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwgHgl6m46lprXao5rOhK4AWorZ-YbT79h1rLdPcheb-VCxvELqie4XVaN8aCV3C-VQXAJeGsD2XDxU_pEr4UoKEkpv37u5matV5usO8LSaEOyMZqPjp2h4PaznrKSlMUzJTdSQm8wbvA3kYxnqzfX58Od6Q4PgGw7_stl5N4NZ1kqIrlqJofVgQYe7dV3RzCmWnWhWThnDuA-57QEb4yxIfNylAROZZavCMQlNJNssALALGGX_bBiht-5uNrygezVj7zIok4902bsu9A0Eo9M0VgpQW6Um9qt3pSaR49q2uB6z8WXGY5lDVVyVA8TXdRROVN_fX7cUSS9KzoqtUfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
⚽️
«سال 2003 پِرِز به خاطر سیا‌ه‌پوست بودن رونالدینیو از قرارداد با او خودداری کرد»
+ بازیکنان رئال مادرید در فصل آینده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/91266" target="_blank">📅 12:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91265">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c6904cff7.mp4?token=QYCH5AYulLTnx4C5-viOEQiE9T02xTU2VCEKEmKhcOguydICx3lfc1pvT6lmMiYUGdyevVM8G-ygvjbhy3P_AWMgbMv_tBYj3v89teTuesjudrMhHpUDEXheMvWECvG5O9BB8r6lG9ohpAj_8tJzU1n0DX7PelYrKBjH_8Mq1-HPYc7emwkxBnxMwRfWEttD5AO08EiymCtxQUCfaYBX6Q2t7W5nPvpzjT20Qm7cXUQ1EWOV9pPGi9FMp9ih8cIHgcoTt4V4_VzUiJwZX_Dylo5q7bVCrP16T3dWEfzcf9nc67pjgztpa4pkHSsGhGm1IlpH_9Dl-rKzKaljQYVfIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c6904cff7.mp4?token=QYCH5AYulLTnx4C5-viOEQiE9T02xTU2VCEKEmKhcOguydICx3lfc1pvT6lmMiYUGdyevVM8G-ygvjbhy3P_AWMgbMv_tBYj3v89teTuesjudrMhHpUDEXheMvWECvG5O9BB8r6lG9ohpAj_8tJzU1n0DX7PelYrKBjH_8Mq1-HPYc7emwkxBnxMwRfWEttD5AO08EiymCtxQUCfaYBX6Q2t7W5nPvpzjT20Qm7cXUQ1EWOV9pPGi9FMp9ih8cIHgcoTt4V4_VzUiJwZX_Dylo5q7bVCrP16T3dWEfzcf9nc67pjgztpa4pkHSsGhGm1IlpH_9Dl-rKzKaljQYVfIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
پشت‌صحنه تصویربرداری جذاب از نروژی‌ها به سبک وایکینگ‌ها؛ ایده و زیبایی 10/10
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/91265" target="_blank">📅 11:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91264">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDftn00l4PmgJW8o_2DgniZLfqUUrwVnd8t-UFhyRwwN3nLCCb04yAGLsSd7J_3qlAo3A0c0OC_ULBKiP1iLiZUmpTiGz7dZeGXxZeHTMwMAo-lwPRpXPYOlwODczjY2eESOd-GeakUxM1OJMDQ3kzzLLu4CG-IIHEhLnEWjBq606QtGSF86VG-vMtpTA6SA7bX63bbz5VAf-kUgV_XU5SvfU6pJj5iX7uy161XnbkoSQVDrGZX5N2Zn8GHpncTTekf6jGxkmVeKrhuxEbYyYPSw-nIOHYnxxIPRd8b893fd0tOOYdHZcvwjgdmAtoMPzFrrevM9V_yFL3P8e2QZ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری
؛ قرارداد جرمی‌دوکو پس از جام‌جهانی با سیتیزن‌ها تا ۲۰۳۱ تمدید میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/91264" target="_blank">📅 11:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91263">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_Fo6iCzpb3zGioS4VrxJ0uCWbjHXqJDsK_a68kV-SneT7XOF5SIVMPWUBILhkPSDs1YXr6inn7GKeYdSIsEEtmyv1YdImMqYm_II4tM2GWnyP0xsdG73yyQLQKGSNYx2U4vNZnZ-EFcByIjl1w9i4hONlSPGQKC_czpf7pBU-w6411OUZeP31paC6pLU3JAIsJYCrjYGhLfRYywDzuLw4h3-LU8tzn5TQcpBqzbahFYHTjtz9WihPMYVCR0viqslao1epG0VqXVv8F1j2qM7y6TpLK6AlUvKPh0ldCAE3s3qIrE0lio-LgMtNfc7C7ZWy-EkAaKc6dzZ6x7waZ8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Milan 2009
🙂‍↔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/91263" target="_blank">📅 11:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91262">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
❌
امیر تتلو واسه ماه محرم درخواست مرخصی داده که بیاد مداحی‌ کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/91262" target="_blank">📅 11:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91259">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gJtCuYtqkEbrql6oLEUXqZjeBR7K-EnQYRKqFE360DfHgAi3s2-GUuqpcul-ODPxGHYuT4pPRjsVGEvmx7ot7koM-Dfwn9ksNUXAbMuiiVBLRIxE64ZdX2jj2Nfcu74mhrduNetvibJWsp7yxEzevmhdLo9EQACjHzj79wpaqDLz7mKs86zIi86Avmw29jdziqca6ZDh3c6uK9OfsD2DWEyVlJ5LdXupp3antZs9iKpP3El6_ZCXztpf1qBlEc9ODhVwLTmPH-0Ue4gxW6YDuIbzXx1d5Q0luy3ddqgVqw2s5kQWvMpLdySY1SjY6fJ0YuxEYA2X_J_CSgPxoSCsww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ygr7_ilNHNW4N8FCpmh7rsn4Xcd8fTm39jX5dDnQeMHJ-tiGhIkn2Wq5SLc0wMFD55JB6Zd6HjQ3gMgr_YJu0JkmFmsdF1WancSHjiw4QHxpWSGeR5XoLhfXwoAcXgvR_H2BtRpsWy6Wyo72YyLm37D7jPvzHo0EJ887eHwOXLZHcGHNC_U5z1DCEWxyZ1cZfagmRTMM8zZWiysgWB6LPxQTnbceTjLMnDyzXg0hoVz0vDyBDy8N7gF0TlBXlPXKmtHVlaoI9ifp9lql5NR76jfggs97X3FULcl36nq8TGp0LZO4ox2mgtJl2A4PBz9kQdIkjbaexrvw00F7Wuafqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LWPJuxIz2oS8mBFMYwTHqYjQgqL2y7PR5aIZNqdLKAO0TSqUCzYmBSN7YSNmpbVBvVJNDZN-xTLQKwKFASZ4zLD9I6NmtE_Fo-IwXWQURIERiAg9EXS7eiRAsE2MJnqtiYvhGxb_gBbSl_CZ3tP7R5Il1MQb-VfPX535pjhY0RxCqHbHsK6LZeK0P0HxhxrP4uII1cSuGKP9WoIt93O0FFhZg03C4RmGV6RdojsLR46bIXo0yMNQde2HQq19XfNhOnl5APIz4aYy3mFRvJUn9h8Qd5ZYu2R9DjoAEdrEkotoIYENbtWj9toPEEFD58f7lfWGL29hFBL-4YOZY6KRyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مراسم ازدواج عمر مرموش ستاره سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91259" target="_blank">📅 11:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91258">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b13497284.mp4?token=nYtIrIr7Ue6QCG5-LEWIatYa96NCKilN5jyyLfNJ__mX2Js8S7VPReMq4Y5pyHiKfWHSQPOawVFdUvOJVfCBZ2VipOFfkRz0tcvRqZ07AKx5B78BSnLTI8xk7vBhaxE0Op3EF0wA8SM5rS1JBDxuSFBmQs6ldDr4RLFfsjZjxg_T5fx3BUr_1tEYffZOs8CTR1KmtjRxySYP2AmzEyhEs9Rxj5ug1_VxQzmvwMn3cqQZRidb0Xwgg-pYZx_DRLAAvzrBtf8POiEsuAM2d301_vfjo1KNIGq0MseH-LEB61u6-d-cmi2mfpkFNlySTbvgZBc0zF7dOCqU7wYcw3AJtoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b13497284.mp4?token=nYtIrIr7Ue6QCG5-LEWIatYa96NCKilN5jyyLfNJ__mX2Js8S7VPReMq4Y5pyHiKfWHSQPOawVFdUvOJVfCBZ2VipOFfkRz0tcvRqZ07AKx5B78BSnLTI8xk7vBhaxE0Op3EF0wA8SM5rS1JBDxuSFBmQs6ldDr4RLFfsjZjxg_T5fx3BUr_1tEYffZOs8CTR1KmtjRxySYP2AmzEyhEs9Rxj5ug1_VxQzmvwMn3cqQZRidb0Xwgg-pYZx_DRLAAvzrBtf8POiEsuAM2d301_vfjo1KNIGq0MseH-LEB61u6-d-cmi2mfpkFNlySTbvgZBc0zF7dOCqU7wYcw3AJtoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇦🇷
امی‌مارتینز دیشب حوصلش نشد بره رو نیمکت آرژانتین و شروع کرد به عکاسی از بازیکنای تیمش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91258" target="_blank">📅 10:54 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
