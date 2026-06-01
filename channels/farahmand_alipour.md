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
<img src="https://cdn4.telesco.pe/file/FGjqPcU8YOWPvUzC2BW673iYimNRvn0NOiupHOmJ0VpygdazpHf1X-CNjmVvhp29kZ6UhZAqNI4EGTLMYNoFg3CxRmE02N6yPWXbX7GNHUSNs5EAnd9IScbpvstDp5DMjqjGIQ6d0N0bYNSMBt5l7ShhXiTYrcK3O090dWM8Jc6mu67GT__Uzh4V81wAqMcNRiJyXp17GyChvYyzRWLkPVeneeC99Zha4hcjmUoK4N9x7bVFtO0eLozhpZR9nwfFrwethXCDjO_-Dw1P4i8ZQugeRf1iaD9DPe7pp-1kJAqzqfi7oXoMwu3sPefIMacQf4NzA3ky-2h1Gax_s_o1Qw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 19:19:40</div>
<hr>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRxQ3GL7Rr_iQ31_xBU6WKXq77WPnD2KVBpPWidBnZ3-_bZ0BCutmvCjfcTPcDa0sn17yredtD8LOLYs86bjnNGcnnqToFZQjQdG79tqZMzF5kblA9e9BUZPSSMnXEFruUTXI9WPOoE3-lMXmWNviSXAWIdCaa3v4MkvkIacEEohf9GcUBp7WoWUhsrkfZIwV2oeewA1IrXjloYlEnv1bDw0n-2Z9Lj1syRJSRSREomGAzukEOamqWpwbKpj2CkCoGE0YYL9wO6UGBlg0buxVYj2B7t1ko814onRaf-Ae6xeOTd4m5k6nwzwl0C_8xb3MN4tW_kmMjxXqOL28N47uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRDISfWdhFTcQ6zutISdPGBmHwvYeyOEil6XtRQL1PXdOnI_-ftnJZCCd9aZihz0TsG71O8CtTUKbr_SJQnympxndG5pmCybMQUVw8kn8GlYayJ4Rf9eeQcK1bSHDF50jUzp7L4jKYhKks86BS7TqTfi4KCUp1o0mxpKWHZT0CTvNQubVnXPUtvdWmznTwfTPXobGtF16zPsxawC4kdCRtk6bDtu3EAmk7uaSY83gXwVbbbKhbggu3y8x3FE6-dZUOrEsfWn8uZBuA7IEqXMHvgxz_b0NDIjV6lJi8HFg7JA9a13_xkfx64rGsvrY2F-w3gVRIiUS6NPgwLv09ffCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو دستور حمله به ضاحیه (بخش شیعه‌نشینِ بیروت) را صادر کرد.
🚨
بلافاصله پس از انتشار بیانیه نتانیاهو، پهپادهای اسرائیلی در ارتفاع پایین بر فراز ضاحیه به پرواز درآمدند و خیابان‌های خروجی این منطقه بند آمد؛ هزاران تن از ساکنان ضاحیه که پس از آتش‌بس نسبی به خانه‌های خود بازگشته بودند، دوباره در حال فرار از منطقه هستند.
🔺
نتانیاهو دیشب نیز در دستوری به ارتش اسرائیل خواستار  عمیق‌تر شدن و گسترده‌تر شدن عملیات زمینی ارتش اسرائیل شده بود.
باید دید واکنش جمهوری اسلامی چه خواهد بود.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5236" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WmoBdfJ3Eps7x7Up04Dk98WrE6w24RofCeMmBpfN_mLWfCSBOI2S34keQkt7jmKx85mjChOdDhSnfe-GYhaCpdOc8z1VcKBjyKEhFJjWLlEllrs7veRRMEiY-dv-a0vU4XaMpKDR0rmaPiAM1-jof2TL_IkwxdfLdZF7pd9TSzcWL3t893EZ2r6Z_JmmibfspU02tOKehoWqpeRm4i4ObLOYAzjS-0zJj05tiKmv-oLLt_wwrTb1rk2xYanTvC5jDPVTlycaUoS17QcJvuKM1x1BemauNP0h3am225WlxLUn4mJC-zlfVaCrxKnZOpC33OJ31O3sV5gLyM5ZJdiZXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jdo3C-aUBNy2EQh2ybAzt69PdBhsCa3piHHPiO2kHMTTUDWT2k50xVHoksZ5Qvp51BtWDFUTgnRS_jI1sB74NHwIgpX0UVvX0_55jfHBXomi_frzujIxvW-ZUN76GVsTfbOPq5AZTt9CX2EznxiBjNY1RS0Lm5YoAPCwRaDL6Ay7GG8aRAb9HMOOAEVQLU8l33a1Zsu2t8ncONXu5PJE81RyPWYkFULnzZb7SmPhZZqK1Jo9rqYrUYbIL7pjf3l9xE-L8M11d3wEuAqo793cFyY2jKX54g1JcwyPvlv5Vj0x-cYPyKcnOkDwsigFwVMj8fEmxIlvSqYaWpJQkItAXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=ofRC9OrhP8lB_2HR-rgwYj4qpv1CD4SMoNa4SdJYCRQ7CEbqrZ0A8Gq6vn7MJzEuYATVevKd7yT-hvfsBIMtetWllF_7YNtw2Ppx7cFWQ8y2uKXR_JxCoBNda7SkV_QAHGueA1-zyZXxPvqVtULruIghOBPrMSLf9qFcLBLxfxYVrQxBGj_NKNZix2CbIpvhZisKuDkgpF2-3x9VFOUEqQNp-4ZZ4N8LWFDCGbXPbLjuCATAaPut6lDeadHjn59qrGI47UfBwSDk9DMxQoXkNx8PU3FNwkRsP3f5qx4dqCGGSirBRCvosCHjhhBx2IuxGIlN7m6yo8zCNVkC7uNv_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=ofRC9OrhP8lB_2HR-rgwYj4qpv1CD4SMoNa4SdJYCRQ7CEbqrZ0A8Gq6vn7MJzEuYATVevKd7yT-hvfsBIMtetWllF_7YNtw2Ppx7cFWQ8y2uKXR_JxCoBNda7SkV_QAHGueA1-zyZXxPvqVtULruIghOBPrMSLf9qFcLBLxfxYVrQxBGj_NKNZix2CbIpvhZisKuDkgpF2-3x9VFOUEqQNp-4ZZ4N8LWFDCGbXPbLjuCATAaPut6lDeadHjn59qrGI47UfBwSDk9DMxQoXkNx8PU3FNwkRsP3f5qx4dqCGGSirBRCvosCHjhhBx2IuxGIlN7m6yo8zCNVkC7uNv_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tu828bLFPXf7z-tcJe449HY559hg0RUwyXlDRmQ-BKy45KaQaUk6EBQr_W5eW9NtALOUsWc69dnBpQe0UiYTUQQOirzA3kn6fm_il65NeldEDSViolkUc3gJgJFX3cYDbnqvJVCe1sX2Oww1JOGdktPYzxnCVwABUXmO33q9BVKMLZwMdNfl0m2gDoFL9PauExbCuUt17gFfOukqoQwBNPyZ--3mcpdvW_vx_9K5-N-OFrF985HPARJ_jXaC8Yt5Yynb31ORw4EsnXwLVMZYDA0TO4iaJCo2_xV5MGvJzv03A2x096ukvjTe-K_0UCJBjipnlkyEE0HZqr57STgkUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=YgbzeGn1qQ0o1qYU-Ke_qh4EOQXvlspelG8atwPESOS8o67qvVOwmXbjivXyNWuQ8q5S6mrbKS96DBKfKaZR9xC2161GZ1T46amFISPZfCZAeDK2AzoPrC9tXWfacPZ5mqYVq1AJe0CTGTnyPZRlJbJjFo0OvmbBwR6J35BipZBwNfi-Y7-haLpmnBjLuLSXMjSocZZotJjnu4TdyHzw1xx2t_YcdcCiLybIAWYcrdvGYX04F47u6YQDB8y4gNQ08X-s2de4P_2Wr8xNe0M7V8aCvZDEZmpObPtknHhTzxWjq3goCfwURvjA-3kD10tILarM3fC2rFzBvG24cLRQQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=YgbzeGn1qQ0o1qYU-Ke_qh4EOQXvlspelG8atwPESOS8o67qvVOwmXbjivXyNWuQ8q5S6mrbKS96DBKfKaZR9xC2161GZ1T46amFISPZfCZAeDK2AzoPrC9tXWfacPZ5mqYVq1AJe0CTGTnyPZRlJbJjFo0OvmbBwR6J35BipZBwNfi-Y7-haLpmnBjLuLSXMjSocZZotJjnu4TdyHzw1xx2t_YcdcCiLybIAWYcrdvGYX04F47u6YQDB8y4gNQ08X-s2de4P_2Wr8xNe0M7V8aCvZDEZmpObPtknHhTzxWjq3goCfwURvjA-3kD10tILarM3fC2rFzBvG24cLRQQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=LBNE1BoqZfrUT4bq7nDoHO6YuzfS5HOSqkXqiXzuFoNqoQSEpy96gP8VSJ8R-_OxbQ2ghl8POA83h1KK2e_5IssyIOP3obpDYbt8qfY289ucsd81xFOD0gyv8VHshy_-_ARZGLir3yJ-6uLWPlHK1aMH-XGNO3F7MmE7pPn3adZBU52FFQPO26P2upsjQ-OcLtj43IhVFsLKghGhXgCn7Pn3B0sBa_P0pHQUTW4MpF546a59x0svhkmCbym70axKAalBAF3TITYH6UHR-_ycs_gNZKIcI7O11nmWg_oOgHstQOHJ5pk9B41zkdf8Gn7ElfwylzssLqS79QMDstRB4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=LBNE1BoqZfrUT4bq7nDoHO6YuzfS5HOSqkXqiXzuFoNqoQSEpy96gP8VSJ8R-_OxbQ2ghl8POA83h1KK2e_5IssyIOP3obpDYbt8qfY289ucsd81xFOD0gyv8VHshy_-_ARZGLir3yJ-6uLWPlHK1aMH-XGNO3F7MmE7pPn3adZBU52FFQPO26P2upsjQ-OcLtj43IhVFsLKghGhXgCn7Pn3B0sBa_P0pHQUTW4MpF546a59x0svhkmCbym70axKAalBAF3TITYH6UHR-_ycs_gNZKIcI7O11nmWg_oOgHstQOHJ5pk9B41zkdf8Gn7ElfwylzssLqS79QMDstRB4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDt9Xz2ojJd3VEd6382cXrw2FqZdtGCX23CDSmAWq-pyVrvQ5gc0Z9P0u6gybZ2pf3vjurC-Pd7B5Yp0VdA2Bza0JzHfrJM5H_HeFxf7Ls3KrKimQkl-v5XcQaIqtMWon9C3HiTVREL6_OsD4CNovy7Gz2ycduzHJf-RrRsLEsfn6hhAO6ULlAvsSOXpfc3IJMsFfi_kP8AN-32oXggerhaQUR0Yld1Ezq-lz_OIZKADPNfrijJP7GzIUPNNEvXm9x3s5ORGYlrR62SneUdPRC57Y8w2SElnDcNJevLjldk92qgeMNrhbFN47iYoTbnygSdYdx2iAM1hJu7Ta5LE5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما
از دولت لبنان خواسته بودن
که برای آتش‌بس، مذاکره نکنه و…..!
به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره
(که بعد بگن دیدید، همون کشوری که به ما پول و اسلحه و….. میده، آتش‌بس رو هم آورد؟)
ولی الان می‌بینن جمهوری اسلامی توان چنین کاری رو نداره!
ترامپ اساسا داره لفتش میده و سرزمین‌های تحت کنترل حزب‌الله هم داره می‌افته دست اسرائیل پ یک میلیون نفرشون هم آواره شدن!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5227" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=urkoZdd6dU0ywLypBHalpTb1juRd5oefXk50CE7pJ4JHrFvqJxoQeEwWcFc7jv0kfcUUj-mnjh0f3BC07za7ZUZSW_shegh_Zm7hHKxkCRRUxyPdZv50l6NwC1uxAZ0O3O1--NzatBL97kVeY8NRkzgS8jAPS-QLOuJ6gRpmCQCfKbEn1LdO6kpjixQ7NgT3JzuD1w6FRrxxtI7NTQZRed58emJjQQAh2pJDPz5vcVWS5BjuGD8JktFjExQCCw6UFUwFm8TbOikzvugytNiLBw0Eu7tHxVI1nmPKwe5l-h8oLS1VHS-PkgDL947zuXsrHnDEORod1H-a8I-2WKtWuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=urkoZdd6dU0ywLypBHalpTb1juRd5oefXk50CE7pJ4JHrFvqJxoQeEwWcFc7jv0kfcUUj-mnjh0f3BC07za7ZUZSW_shegh_Zm7hHKxkCRRUxyPdZv50l6NwC1uxAZ0O3O1--NzatBL97kVeY8NRkzgS8jAPS-QLOuJ6gRpmCQCfKbEn1LdO6kpjixQ7NgT3JzuD1w6FRrxxtI7NTQZRed58emJjQQAh2pJDPz5vcVWS5BjuGD8JktFjExQCCw6UFUwFm8TbOikzvugytNiLBw0Eu7tHxVI1nmPKwe5l-h8oLS1VHS-PkgDL947zuXsrHnDEORod1H-a8I-2WKtWuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.
به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.،
مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!
یا شهر‌ نجف!
برخی از شهرها را اساسا به صورت شهرهای پادگانی عربی در وسط مناطق فارسی زبان و ایرانی ساختند،
پادگان شهرهایی چون : بصره و کوفه!
در قم اینقدر عرب ساکن کردند (از قبایل یمنی اشعری و از کوفه)  که برای چند قرن یک شهر با هویت عربی بود!
اصفهان اغلب یهودی بودند، یک شهر تجاری، عربها حتی بهش میگفتن دارالیهود
عربها شهر «جی» رو کنارش ساختند و اعراب رو ساکن اون کردن. تا نیمی از منطقه شهری اصفهان عرب باشه.
نیمی از قزوین، محلات عربی بود.
این حجم از استقرار قبایل عرب در قم، مرو، قزوین، اصفهان و… اغلب به خاطر قیام مردم در این شهرها علیه حکومت عربها و مسلمین بود. قیام های قم بسیار معروفه، اما اینقدر عرب ساکن قم کردند. که شهر برای قرن‌ها هویت عربی گرفت!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI9CYUUbwLxx9LWIdoESF2vBjoDmQtNLiZIpccSjtP-YF5eGfUa3rX6W6G8tLmIAOUGREBArNTF5pYyDW-KKMnedia21jvt5EI5sZZZ51YKmFGutbYL1g4kthmxgVN7zQoyvTX2-qKwFucwANiqTMWd-KTcmivj9YiRChJuemsgql1_Tt70YBt32OIKYsJjlL-B-iP6NHGz4RG_frJw3_dg2HFWQR6uow5VqWf4c03DdMxsaVCMtzKQlLOHE_k9th7YmTDzt1vjb3AlWvBA3oVuSRkQrkuBCdI4tOLgGs7f1dIasw9eFgqU7UxAc8U0-FLcDJB7F1B6hEeNomMga6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqA0YJraytWtV6rAzmAWG58GdXEVQx1-Nr8ruktgtnljgq0zzjmJiffUgb7-gwV8yUZ9FH75MEneitnhqZ7sOQWlgyl5f8981oyifM8_dk_35Ww2Mk5IvNFsuuM6RgFvIeBSkEGHxkQXXZwQy7UCaXjtUtELMTvekkSNphqZ2CzxbndOP5przQERwjLT16alrZhV4yTcJEQtcaP2NSxEgmnF8X9uTMDSIwUIFrGT7XN1TcF-Ke1R6YP9HUd2ozpus_WjwEPnfz6_lTN5j0TVnKoDWWWdrMEtcjCYMgz0OaVdxWeWU4HF0LvC7iqPVXhFNE9IvdPNtoPYbrTxwghpyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vICGXuPUDPh8JQMFBtsUus_dvTluoXs8WbtUfenIIotlOWAD0vhQ7YW6b-db-J9QqKGQxd_WdTIE7nvBYq22E5c7PVXhfob19H1DicyVhVagl1d2a5fkcJuJjIwcvxD8_6JZitBfQ5ARhlzIKbYpRIaF5wBgyzoy5L07hHB2CqnKQQa3EpTBZMf5OY5-z0RWYfkPTRs7B02msp_ebDbIxzvRVT9p9QAN7_UBkyq5hRclrke0TOSq_XYCab1D32HuJ4HQf7AySgBrvzQ5amu_vZDUqnUHK44byvYZcArjZBNt6eWTCqEHCIeg0owUr3zub8-taDn620yjGn-AaWZ6aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZPLt6UQQgh_ONMtnveA6lz-ZobNv4L6o9Gxww1JoZW3ReqeBiWY8OWBngkNXMCAUVSPggL4q7YZ1_h-wH8cUx2zkgYE0yrvUiJ2DsDbGUVvNXdcrbOS4ym-tBzQ2lYy9UotvNAHSMcqDX2hzbSS_Mo1dLSvN4ZfCq0DmW7aip6IB9BCwE3ROW0S49lpirT0UmBIa-RnSA9alomhkMdyfXNg4NkLnfPooDuiuKVgQ_-0PFJfUArqAkm94YWPW3Mx7rXxmBA_NdPEfIuh3I7qDNbV4aRkTwFRCL4G5Usu0A9jKW1F192n1C_t2kzTukfvtdwfiPoBLgn966-vsObuPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I_wzD3-T4oMKT84Y1RKZxSCHORmajjTGwOCx9eHwJSYefl8Sunzg-xEccxFOkqkv-XcuL2mkfc553JKU0AMWxgPiwhUcEfUC6vySqDaLJ5N0bkBen2i57eHOaqFkTzRYU9BK9EM7hcizaBiLEaEwosl8oCc-NbgcT59B3h_HeG3mJ54S5pczBdknVc9FziaMPUgkgCPB039fHZ6ZlRLhUcTBqd0oqS4vPwPJsrJqs8E95NrsYc7iatIvLtrP9IYtZnLvu690MUdWeLB2VzrS3GVrsoI2WuwpYoUJYQIJoZG-sAQv-Ry6JwJ9CA6qOE-0JsGCZpv7e6Jel9T6yLkkOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتون رفته میخواستید برید
پشت سر خامنه‌ای در قدس نماز بخونید؟
که شما تاریخ خوندید نه؟
تاریخ جمال عبدالناصر و صدام و قذافی و بشار اسد رو لابد خونده بودید
که همین هوس‌ها رو داشتن!!!
و به همین نتایج هم رسیدن!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5219" target="_blank">📅 18:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5216">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SI3kEH3S8hJZ5SYxqzCS4nbaaI0rybWdbEevw-o2qdTx1fgXoH-2gPyBsFVjT5NGvqoPUu_Y0D69GjLMeT-n6yWXji84i1o_Ki-aZmFuteYcOkwcV3-U8fZtbAqYqsvWTLnkfPrSfglhkV9OTTBhZf2HGEU_DRrnaZEDGKr7Qa938MJw-Eb6BXZqOOVh_zjo_4hJW3cFQo24riLvEZW5tyPaF2x05coHeOh-bDimCeTUoHP2Uh0z60ncXJ3JPWIbddjdukeh3Nn6lPkuYuc0g3GkpvEpFkqFKYuBboFVSEzm8O0R_m3JLLf_GWylCaXhb1xFEgUvP7UpMoHpkcsrqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/soq9EtRD13cswEbDtqa18dP1UQvOYoUo1KnW-QfzYNDO5jTtT-0AfQdYEdyNImoGkPLB6WUtR_3ZLoAQGy8WIwpKWYUfsvhaIx-Amgh1Dge8bTuFgys-jFi2QihRw51I8qWK9L_rAKqxiwecV0QsDtcrMGblTNSddqtafdvpLMGw2-e8ak72BvjbyheutfxEr6YcOuPJoJqIqkw_MY8K0DaZa_MURRfqjacNmbtVB3YrhGyXv9ajxbv1a5ky9RPn22nht6ZTUrXHpXigVXLFHPscQ3c3wApEkjUK6tRMUaN_oGbty_P4Hax6vOL4uc29xdwUbY7CJEBNI6QjjGd1Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v8rCGVrOo_JQwNVvQRr1NNH1How6i4mqq3EBBp5Owt2JC-zhyuS4UNj0w7E-BITmjjXWpaHjaGkf5MLLU40QOS9rHmhiSP0b76zcVSfXVXgqnK-WJktizSus02TtoJyMaZsqCdzO34pR027jVcn1a9eYnGji9zAXU1r8IDwimRVv1ucns90hBFMTPE3emYknHp-YjBcFIWnBHD6pp3o-Mp18s_gIj8pFmcxXEw9BfpnF_OXJtN6B-io8EQMA_0m7LbxPf7cMcAnL0fX03Hr73Nv9cz1-asepsvcfWqtHZwHxlBKTMic-hDBBfIRVX7JZ4-Akp1dDw6Jygd2H4JR_CQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=h-3NzOtb4s2igzzuVuz3xnLUpVz1eu1vbX0uF7ObSKOVoii9YVftJHy7uOXUzf8xjDq3Z0kQXFWMeXjARMQE_tj1-kIgXfipDePmulVgx6s0fgdqR3oQYRimKe2zWw0NmODUIFSEm9_C7LRF_x9fXEZ2VpDFcwhRr7TrNkckzjSCM7nXNOVtJH6-g13XEyIEi0Idp6QjG2RkGIsWvEe-1_qSN45irTjh_wJ8nAsh1Va7yLc41gJ2ilpwKHuVwi8b_UIiTKQ1HXBvhRycHAvEUaZyJJrQnfIsOphjJlyo5g7abqiUpZUtr-veIlKmAewqT2rQ0MKmuSPuyYuFJPQ_KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=h-3NzOtb4s2igzzuVuz3xnLUpVz1eu1vbX0uF7ObSKOVoii9YVftJHy7uOXUzf8xjDq3Z0kQXFWMeXjARMQE_tj1-kIgXfipDePmulVgx6s0fgdqR3oQYRimKe2zWw0NmODUIFSEm9_C7LRF_x9fXEZ2VpDFcwhRr7TrNkckzjSCM7nXNOVtJH6-g13XEyIEi0Idp6QjG2RkGIsWvEe-1_qSN45irTjh_wJ8nAsh1Va7yLc41gJ2ilpwKHuVwi8b_UIiTKQ1HXBvhRycHAvEUaZyJJrQnfIsOphjJlyo5g7abqiUpZUtr-veIlKmAewqT2rQ0MKmuSPuyYuFJPQ_KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=fXKOarnhkLCpDAAy3ohH-2fJ8UjATW6fq9zJT_GXusQG-Dem95UAmICBNDGugdELZMkSHUymde98MhPJsKgjWiaiawdWqUugws1GKb-vht5sBaFIy1j2Ay_HJgQw7rg9-jpJDwKWXsI2sQptA-1Lz1dRYYrU354WeORqsWZ9O0W-RZFqAEMJOTjPbBwss-Q-vPOHLK9RtSAZO6F5nuhNpC6kHXQCcF_1VXnUwoAFMkBNy650gviIeo7-AKkul9zHVVk4DcmoLncU1yDvYm6P0FO3SUk8HaxictM0kni6XzbGJB9X9SaT5f3gXl7LQ5RySUWrLuObf-t8r0upy2pOyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=fXKOarnhkLCpDAAy3ohH-2fJ8UjATW6fq9zJT_GXusQG-Dem95UAmICBNDGugdELZMkSHUymde98MhPJsKgjWiaiawdWqUugws1GKb-vht5sBaFIy1j2Ay_HJgQw7rg9-jpJDwKWXsI2sQptA-1Lz1dRYYrU354WeORqsWZ9O0W-RZFqAEMJOTjPbBwss-Q-vPOHLK9RtSAZO6F5nuhNpC6kHXQCcF_1VXnUwoAFMkBNy650gviIeo7-AKkul9zHVVk4DcmoLncU1yDvYm6P0FO3SUk8HaxictM0kni6XzbGJB9X9SaT5f3gXl7LQ5RySUWrLuObf-t8r0upy2pOyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=AfHtHxu3T24ChPCzzwbxlCH00jNxwv2D8B0UEj-pahqgq3QaGlWbPxHEjmbtivgncsWp7xcUuwt3Rna8d5HJ-olyzt3SneovGg3a3Wbh9wFWar5gNVGHn-v_NI2huW1Rcit6vB0SyT_AbuY_aYCrcca3JwXf8tobGOpHVkTOxnPj_DHhw_enwFqHdUKNE573MUrylyYjOoj_uujDLAbVQNdQR3QCCAnRSSr3od6k7PFttYnC6Aq89VDv3-NxPRrjdWMO_7Zaz1Dd0kj392zobECmuqzcEZ2eMxvpifLV6rI7BSv78bVPV0A7lLwrGGdRDFUjWW7d1PM1rO06vzu0BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=AfHtHxu3T24ChPCzzwbxlCH00jNxwv2D8B0UEj-pahqgq3QaGlWbPxHEjmbtivgncsWp7xcUuwt3Rna8d5HJ-olyzt3SneovGg3a3Wbh9wFWar5gNVGHn-v_NI2huW1Rcit6vB0SyT_AbuY_aYCrcca3JwXf8tobGOpHVkTOxnPj_DHhw_enwFqHdUKNE573MUrylyYjOoj_uujDLAbVQNdQR3QCCAnRSSr3od6k7PFttYnC6Aq89VDv3-NxPRrjdWMO_7Zaz1Dd0kj392zobECmuqzcEZ2eMxvpifLV6rI7BSv78bVPV0A7lLwrGGdRDFUjWW7d1PM1rO06vzu0BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z88j3K5gOTcZ506bzd-f4E0hEdJHq2_N_68pjEjLsCVtKRYwI9L3ODpxaxpr0U1z0m9aB85kDPzqk4qWsAYtLTcvEW7r0_1xYSWSZgW-SnUKTwOJlOW_RVM9VCpppfpmAqzi8yF9yr_s_vuJ58fsCD0SawltRuMtlQLIHLkZG-7x_LskMDZoJ7KyhKEjuYQXoaI4QA0yvbL_vfdgQnCa3Euxmjy_Ad7oLnGGpow37MyDbNz4Up4EUgJ0cae9IKU55o1-VmQ3qGP2yOdyZ8Udr0RBc4SwSXjjGIxLgILtvTqKNmq8iKOGrZUqQ6jolT7gBt4NgDwhnSdgVdvMWLHQtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات و دعوا سر اینهاست!
خوش به حال آخوند که چون شمایانی رو داره! هر بلایی که سرتون ببره، آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی و کره‌شمالی رو نمی‌رفتید! راه
صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5212" target="_blank">📅 17:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbvOxD0S_7zcE622_yOvnjx56xOhWUx0o45GYl1DZrVquUcYwImx51b2yI3vDn60v9bPMqxGn3bRh8l886dQ5EkdiF3e_pArjFf-aN9JUv-PeFdRDlBitN4M_0Mv2Xz7KSNm-R7vLGvRAdU1fnCXoK40MGbMdJOnUhrMbGHOA4JyG8zdQwgXZPGpFAeVd6-xugyDAU8uXmhaDl8nuyWjZ-o-IIogTrQ8eYPR33-aB00Vv0bkeBvyuuhmH6jH3ZiL98a7i50gbjzXDKFy3us_kdzidCwZxwXJzQhD0XHytvFmWbPSqMhu6MXy7wNxPrWnkHY_7vCO7VmpudVayETk6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ  ۴۰ روزه به خاطر ایران اینترنشال بود و‌ دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های
ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های
جمهوری اسلامی  و ۴۷ سال آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات
هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات سر اینهاست!
خوش به حال  آخوند که چون شمایانی رو داره!
هر بلایی که سرتون ببره،
آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی
و کره شمالی رو نمی‌رفتید! راه صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5211" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5zNH-49TMxm2PZhgpAIpI75nTsQd_bBvhI23Pp8oUnkP20lWBSnjy022OqdTvO_Kl-rHR607PSW-bSC51srF5kgTRUMkS283Edm0AtR1WBUBG-Ec5lOcShapyF351MEtcZ65a5HJVfomo89SxU3uNd8-bEcLAv-6dkCXquVo2_tIOK-7hFTa5udG23bmc6AGUgi5u65CnqcmfDyVJIP3WEhaVUW1H1rLMX3DCZ8Gn8MEuzB9EZ_rdEeel8uG8JvVatFvV3FcBqdH6iOk1zeH3T6Ax8gPgZQv1zmZOqWjfqe63o_Zg-SHJkaSzsUWfvLiqqDRhCYIKzVIMq1QU-jiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAyO-CZlrDRcHpQWSbX6AJrRf76X-9EWEn56voYvKnyw5pNXV66wJg1Dz_UQCX5SP4_H-ZfbVCRd_h-n0ertgYKhhj2E25QzdphiEhoLWUnWiyHPTxsXlRRr5TaqgVV3ox7ZjiaS2oa6negYEOX_FVo4l4BNhIr04oWNvuqLkpfYHobQdvW7GBsQGQs1d62kgNo1OkmmKWNhpzelBndhWCg0XpAMbLgQxrNl9RFmFWWNE290KuGKdr_AEcG9j_cbaBKHWwUG2FX3asJP29STPWIJLWFbQfay2WQc0RxiGNgHoy_eMrMU69jsQ40l_EIo0-L5clfP3H6g-e_Az2MewA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=lDypGIAsrQNSuBxq3N5rdUpF-yzu_Yama9czCrhMCR4rZRKA4GZ2ZL1x09ayu6Ic3AsZKlZEHp45raOuJyRCRQjlYKf6p1e-lnU44qaSYuGrc6AMnKWPtjVTcxDoPvV-D6o-irr8DaAj4HbptLR4WxvuI0f_0RIpoSrdmLilCSvE0GhlVdavQiDXtfV7Eng7QYOC_mAbELdqDAZ2ML72WZTS58pdcRlE342Mjqd0Qm1MvSEKHmd-iTbg36t_6-kA5U0Aq7onZpTfLoAFLanezvyHL2SkQbtSEWmRIaKs6UqM1jH7t2G9GC-9PLjKmewoQoNQFK56DLSuR6vp8ECSHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=lDypGIAsrQNSuBxq3N5rdUpF-yzu_Yama9czCrhMCR4rZRKA4GZ2ZL1x09ayu6Ic3AsZKlZEHp45raOuJyRCRQjlYKf6p1e-lnU44qaSYuGrc6AMnKWPtjVTcxDoPvV-D6o-irr8DaAj4HbptLR4WxvuI0f_0RIpoSrdmLilCSvE0GhlVdavQiDXtfV7Eng7QYOC_mAbELdqDAZ2ML72WZTS58pdcRlE342Mjqd0Qm1MvSEKHmd-iTbg36t_6-kA5U0Aq7onZpTfLoAFLanezvyHL2SkQbtSEWmRIaKs6UqM1jH7t2G9GC-9PLjKmewoQoNQFK56DLSuR6vp8ECSHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=XQShMfDo8qhMTMxxu7EB5j2ZKSn34HsEI0SPBEf6fNgMgCgbyj2lF2183iGkJPx1NbeMzQP1A-wLMxCCSjVB4u4fCynuBH9xAJzfPXpvgeN3y8oNGN4U3OmiaU47TElG8s6I_bxDo9yOy9vo79qWrLLe2ykigt5QNf_lLX2T87ZncX5h4hm5TrVvP4xDwkVT6nQ_wXGvIOpo7JL2sKsXT7pfnS3nmTk4WHvaVxBCTFuywk-wpJvghXfZVa1WNoaEXaodNOIWQ-eEi9mxFELrT9fyMpeVuGFfmHVZAO2ON0_h3TjEpLBveYjqk1ss6TIpOrvMDdiY0h9QaDij0LSkiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=XQShMfDo8qhMTMxxu7EB5j2ZKSn34HsEI0SPBEf6fNgMgCgbyj2lF2183iGkJPx1NbeMzQP1A-wLMxCCSjVB4u4fCynuBH9xAJzfPXpvgeN3y8oNGN4U3OmiaU47TElG8s6I_bxDo9yOy9vo79qWrLLe2ykigt5QNf_lLX2T87ZncX5h4hm5TrVvP4xDwkVT6nQ_wXGvIOpo7JL2sKsXT7pfnS3nmTk4WHvaVxBCTFuywk-wpJvghXfZVa1WNoaEXaodNOIWQ-eEi9mxFELrT9fyMpeVuGFfmHVZAO2ON0_h3TjEpLBveYjqk1ss6TIpOrvMDdiY0h9QaDij0LSkiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQRej4qoLfnQAp3UFW33qas3bVybYZfhveovCc1wxS494IzkcT1JgNEDnnBIyITWEtHHF6TKFiMVmzv5frGWDgNWoEYy_Fvo5AwPF6OgXIKZrS55r1Bltt8Qvt-8h7K4-YTTqWfwMZbv7o3m81VHLihOBRaRiGO31xlEk4O81ezxJHENFQBlxBlRfFwTRyhP-mSc6d5zEmLDVsPBVMQzd8zOb1t3wZ-b0dJ7cQ4ApXO50UZtCpNcCUHMkFKxOJ3f5ohf9zCYgC4M0PnQxQJ77hrQsw85rEd8YxWAZkYjQFd5i3_R-zezAsbBpEYpr_oFNifRcKi5u1LWM9a4gm5b1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی با آب و تاب می‌گفت
به امارات حمله موشکی و پهپادی کرده،
حملاتی که ۹۵ درصدشون توسط
سیستم دفاعی امارات خنثی میشدن!
اما امارات در عوض پنهانی با جنگنده‌هاش
حمله می‌کرد و جمهوری اسلامی هیچ سیستم تدافعی نداشت!
یعنی اگه به ایران ۱۰۰ جنگنده، یا ۱۰۰ موشک حمله می‌کرد، میشه با اطمینان گفت ۹۹٪ ماموریتشون
رو انجام میدادن و اهدافشون رو میزدن!
کما اینکه اسرائیل ۸۵۰۰ سورتی پرواز در آسمان ایران انجام داد حتی یک هواپیماش آسیبی ندید.
آمریکا هم ۱۳ هزار سورتی پرواز انجام داد.
آمریکا همچنین ۱۰۰۰ موشک تاهاماک به ایران شلیک کرد، جمهوری اسلامی قادر نبود حتی جلوی یکی از اونها رو بگیره! یک در هزار رو هم‌ نتونست!
جنگ با امارات رو جمهوری اسلامی کلید زد
و هنوز هم کامل مشخص نشده چه آسیب‌هایی
ایران در این جنگ متحمل شده!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sc2xlBXC5sUbkmRo1cgL6mgcFQ-r1AqeaAEXmVKvnyeQ5rcxI6r4fu-LAXvZGnU0N7vPm24GMSdo_aW4PmnQwPF9V75BgC2GU8JCFbYIyfJKOiZQG80VSCq98H_R_SBPpZTK7TeMsPbrDHRRWlJi1T5U7m6bMvr8jpPccvSJWliPt19RD-55R6xJhIV7_s2kirjgEUW-YmMsRDq9xsu5wO9MdP_0BlenJ-hBYwggECKoFY6tvRFgdDx-n5U8vFdXGBMX9WQDENBsIHeiFhza4EjnyDpRIRlHzVAHpFTKOB5MD4mytkvCCeVt7-AGNm147E5UxIK1UVzJkR3Q4VSICg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MERWGW4Efr1CwMe4428SigL4GhR_gkrf00lEJ_vzGeAzThSfFctGlua1n4orK8gs9094OzoI5-YR5TMhAh0R_Ailyw0jzfacyN5hmUaYaMWGI4mUhoZS4rs0Spl43J2g7PoA2iYRPs7VKqDqP_ca5upHu0QyZ7L8NJHGUJLIld2S24zaO-tgVOXEi1bdsL9Q6TRJfGbEkd8XoBDcVL-BX4TFS9NmyM01jkMcC4BViQR4JlDauWzESwX7Yov7j91HzZ5HeZQuFvhA3zMNuvNwDiWp-SyjM0mnjItHpgKJvrMUhSqhizLQyyUFox5qjjLF4bcds_UVNGkQJ5uJ9IZ2XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBYtTHmjlqjzABCG-txDMTAZjAmwM-z87imEsRlgR18bUGIjA3bzh9IjiR-JjXoDZwkalfBcOXZwONax3TD4bN_u-CsTiAe6G4sc8k3EbytE0Zimtj-D0DWXzDJx2jRsacu5cxk4ChS3q7ZYXR4wrbF_gZMr6lioakXNaUtczYej_AgNif8MwO0Ps7-j3gmVo-1fZqVpRDHKHVfbJ2yHbbOLeNyBddeUEOe6WRC16qdlirVJlI-NlkD8hDI_6v8guDtZ-fJphlJ51juW3-Jx1Qw7h0XjVZOTv8x8SPEVUGalqBpRqk0RbCyduW3P8nnGt4P_3ilN7GPD2PyBjZSL-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : برای اتخاذ تصمیم نهایی اکنون به اتاق وضعیت می‌روم.
«ایران باید موافقت کند که هرگز به سلاح یا بمب هسته‌ای دست نخواهد یافت.
تنگه هرمز باید فوراً باز شود؛ بدون دریافت هیچ‌گونه عوارض یا هزینه‌ای، و رفت‌وآمد کشتی‌ها در هر دو جهت به‌صورت آزاد و بدون محدودیت انجام گیرد.
تمام مین‌های دریایی (بمب‌ها)، در صورت وجود، باید از بین برده شوند. ما با استفاده از تجهیزات پیشرفته مین‌روب زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز باید فوراً هر مین باقی‌مانده را جمع‌آوری یا منفجر کند؛ البته تعداد آن‌ها زیاد نخواهد بود.
کشتی‌هایی که به دلیل محاصره دریایی بی‌سابقه و فوق‌العاده ما در تنگه متوقف شده‌اند ــ محاصره‌ای که اکنون لغو خواهد شد ــ می‌توانند روند بازگشت به خانه را آغاز کنند!
از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین دفن شده‌اند ــ زیر کوه‌هایی که تقریباً در نتیجه حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند ــ توسط ایالات متحده از زیر زمین بیرون آورده خواهند شد. (طبق توافق، تنها آمریکا و چین توانایی فنی انجام چنین کاری را دارند.)
این عملیات با هماهنگی نزدیک جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام خواهد شد و این مواد به طور کامل نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی میان طرف‌ها رد و بدل نخواهد شد.
در مورد سایر موضوعات ــ که اهمیت بسیار کمتری دارند ــ نیز توافق حاصل شده است.
اکنون برای اتخاذ تصمیم نهایی به اتاق وضعیت می‌روم.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UjfjkcKoKjyTxj_rvCSrYgHtoWXgOdTDReCny4fXREbpDHu50zSOZ44x9bhtx6lsBhrpBvngHP4TofvqYNNbGe4s-xq6I27UwR_TJvqHCpu6NM6nCxnUpT08uAf5ScocKOBRAOXZSugOuUy0iLVrWcTewuv7tzxJIViQE78gJCkMOeIZhFR2uVfq7--tA5DA7XJBGy-slKJ1SF-JIuEeQYZ6iI4ZV8UsM7Lzx7g7AI9lymrVfG4LKBYf6oTmS_5hD5my1v3eXnDGQ-0NiI8lsGDndvNuob5bodApjGgCtTBSP1deLuosiqcXSZEMm0c_bXoBdwFVDRzY2HRFTcTxUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AMQJnPy3WXk7Vw-_dXsrEh61Glfg25Mj0zadrbnxmd5F9U3MqP5E00z3OC4O33JVFTXxMNNSEnykPDadesNxZ0-xaZJsAthfU844ehDWKkb0KUzrZ6T-rHBomtjzOnRtzA_NdZa3tzGJ89L2xKtFe4cQyp4ZcPXhHWcYkin_M77yv4bWpDhag7Hlhcbp_HCU0xDM6aT_A9xxqljpwP3eBfC4ISKOrw1sTc8cqx2t8ImdRf52ke0yyKQ7_uMn1WiqP64csMnkFTY3hYNNBb4kwTjxq0YPIjh0SzFg38JeOVaq6u2CPC1a1VgSqJHndTLj0c_3y01un8OVP8u0_bTCeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gf-rp6lFBhGjoX9rnr7trS3BqMwSH9Vw5ldtAFB9TDRJ_7kTUwfDnO1GcOS4FII0OJDekDyXJlwx5UoCM_pnfj5PH_wVEGyOtMKGnMXoSJbvZPqlQwmWNy01aY6GtzXvMsd2g3CyiTo_I9jvl_lFFDMgR-SPDMHF71wAfhVPzBmUhXtEXq-rffm7E70jFkQm2DKSjXNegtBByytOA5NZ9Wun20rWmaiK8HBoI_mxVvVlexkEkkjoTo89-SLWjBdG0GZHvu724HUq1mYkvc2zUfGe9lNLvcwpjui0htyAumtiSy2rFB4RDjN1PO2OPhd0ab-zR7qoVD0CuG3qSucaEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W_JT2efbvFM_tWAX0ag686p0Km5oOZLEDd65rn5aNWe_Uv5EXBRX9AfQPLEgCIL6FicT3fdp9LgcauYET9KPXDIMKU_U6UF8fgl-6PLEJuTQcdMZJmF0ROdic-JJy6aJOZHg1bmGjfMhQtPjE6UzXb_N14rgexLLQjiXi91-TxbHd17YM_059wVlGO5UF0ZmXkC0FAa-Rz62cYvcsKjuLrUDfGpFI-D96szx7dR1jXxIhZ14LiU8__5aBvamdZ5BRG2IcewHSdp_qkDRBgoS-l336mTAAE8PKIb2ixL8M_AdTZ8QbylxXD5rfihXitKkt6fCORXQyKGZy7ODlsrOvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=ZV69s5MzZomxbiCiYW8wLyK1gO03STiwkxsupFMvxdqtnKFJWDi6VCxDknQrXqELpuCZYPwjx3FuTHDQINiqkR6FwaH_Pg-YWOC-7B8LdxUp1APsgsmfz7CXw7zrU63ogceDDThvM7SzJMfQO3Bdafdz_RUZFlwp48BdE8k2fjfVMeDkKKJJA-f3TBIzmT6NoDiq_JM-3_bVqLbfI6h9AcClCwu2Wb-fH66jttSH0AW8JKRA9f_wqjtNTBfHHYlN_UOsNcKJs_yoPLG3tDomiwXTxBZ5awhXh__sCD9BwP-PtyPIyAjg4UwEpbF9zgXrCGo7Wv_ZvAzlHI1erhTM7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=ZV69s5MzZomxbiCiYW8wLyK1gO03STiwkxsupFMvxdqtnKFJWDi6VCxDknQrXqELpuCZYPwjx3FuTHDQINiqkR6FwaH_Pg-YWOC-7B8LdxUp1APsgsmfz7CXw7zrU63ogceDDThvM7SzJMfQO3Bdafdz_RUZFlwp48BdE8k2fjfVMeDkKKJJA-f3TBIzmT6NoDiq_JM-3_bVqLbfI6h9AcClCwu2Wb-fH66jttSH0AW8JKRA9f_wqjtNTBfHHYlN_UOsNcKJs_yoPLG3tDomiwXTxBZ5awhXh__sCD9BwP-PtyPIyAjg4UwEpbF9zgXrCGo7Wv_ZvAzlHI1erhTM7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=dRON9ztnPPHUI65irRG2YB66Iwo74cCjwQ67Zp7ZcI7hUlwqoaPqN8ulFxywHprN8cKyUKaCIw6w4eZkWqhRM5yYiTI68fQqa79NRJ55Xf0dXuGyp6RevW79S3QwSe6Qk1Ch1ieTrmMA0UKH2UFNtWGoyG7azSZUtL52qt2uCeYBIgzfW3WUoyLbFgRVmsCC5d-AmyoRK30ZYMsAt2TJ7ttEKlQZyfvml_MxwtgDeojGR4uUQEY1xc-zNZIfJjOUIwdPR_xvE6kxm4pxM6DZv2jxevfcPxJaSTOpNve9FNE_lgePEsJSKNus7AHy3kQ7SH8SCKOPyL3n5pAVc0t9kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=dRON9ztnPPHUI65irRG2YB66Iwo74cCjwQ67Zp7ZcI7hUlwqoaPqN8ulFxywHprN8cKyUKaCIw6w4eZkWqhRM5yYiTI68fQqa79NRJ55Xf0dXuGyp6RevW79S3QwSe6Qk1Ch1ieTrmMA0UKH2UFNtWGoyG7azSZUtL52qt2uCeYBIgzfW3WUoyLbFgRVmsCC5d-AmyoRK30ZYMsAt2TJ7ttEKlQZyfvml_MxwtgDeojGR4uUQEY1xc-zNZIfJjOUIwdPR_xvE6kxm4pxM6DZv2jxevfcPxJaSTOpNve9FNE_lgePEsJSKNus7AHy3kQ7SH8SCKOPyL3n5pAVc0t9kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d1NVoF9AIZ3ttZsMJ3xRaabfegSgiRB9y5G9vTv0rOxKRQPr8RBiIVM93h4Hi82Dy2AwWJxju5569R4oz6u3kjKZD4Gz8urWiO3eYfFejw3dN75uGzxQAI3KgamUKFgKmEb9mhUsbH5P92DvO49KYEcgn49vslhv_z1mqtnGaDJpUSRspA9rLNz1U9QX_3al2sRbbT93R-0UQm1kWzt0QYNYsoqSEhnrpQ9LgepzCBeGScLA9A0rNs1NLinE7OW7rfZD79jbE59savSyW1TZvvIdWh8s3WpFMFiUSPJizJwaM4sKaEF_fuoyNzR0ndlk_z75drefE1SnKIIehHqlEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKirSxHhhIrSCbd2yc1xIxKxlb9dnfqz4ARnCx46zs5GHcWGTrLk1dB7P9_draOu38vvPrbNpkhhCH7dSdC75-KiFBhU5ZZYaOg-TapKe3Kn5caS70-gltDl23st94iruNgpQPNC9uripCimTRnvb0B9QGvV0vNHrIG97kc4qlxVZ76vubyGv3_OHZojzNqu85rsIAMN9GZaZ0cEDjHfLPMtQlj8jU2CrYqyrl9t86UCytUk0KyMObK99158Rn5mxJ-X_5CKuMS7x6AnlYJuLITlp1fIxL46r_LZNUzXbfRMUVe4i3pGrtwXFEv_i4QtCGag6tFtoO7ASNr2zySVZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،
پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!
حتی زودتر از پیام‌ شهردار تهران!
حتی زودتر از پیام جوادی آملی :)
پوتین در پیامش نوشته بود :
«اطمینان دارم شما راه پدرتان
را با افتخار ادامه خواهید داد.»
پوتین راه پدر مجتبی خامنه‌ای رو دوست داره :)</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=hRzqwfLL-J7QPrh4ADgx7CYWR4ly4xCkRbwEM1z5K5Pmwcp5TfeymXKdqGyuI89cjgFqUqcUrvLpauojBjXrCVJSvFtss7hbXwnxxQK5b4xBYDK_fFb1lH9ZU2VcFcPy_0YEgOplMpizWr6sQOL2rUirHGBIapr8bFS71nczR8YXuEZdn4C68JZt_tThBs_lQFqjfWqPd_CBLAyvBDSO83MotzwGCijsQJaoC_udTL-loPg_hVU5HwCTOJN-ewp2Enn8tpLMDNu-037Rsnyor0AKU7T8wfA_BWkEfP-GSG4OereyT66LQxkwyq_m-8NOyyoHtJeOjr4ltRbV3JPAdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=hRzqwfLL-J7QPrh4ADgx7CYWR4ly4xCkRbwEM1z5K5Pmwcp5TfeymXKdqGyuI89cjgFqUqcUrvLpauojBjXrCVJSvFtss7hbXwnxxQK5b4xBYDK_fFb1lH9ZU2VcFcPy_0YEgOplMpizWr6sQOL2rUirHGBIapr8bFS71nczR8YXuEZdn4C68JZt_tThBs_lQFqjfWqPd_CBLAyvBDSO83MotzwGCijsQJaoC_udTL-loPg_hVU5HwCTOJN-ewp2Enn8tpLMDNu-037Rsnyor0AKU7T8wfA_BWkEfP-GSG4OereyT66LQxkwyq_m-8NOyyoHtJeOjr4ltRbV3JPAdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTJ7bMUsegLYxjYKiTyrKKi5FtXWmM2xAdJQdaAHOlats5r9UKf2I6WLxlZN0JqJ8vqB3GkRQd58gAgU2ASq2trjIX5e0GZsjbdbD9EDjELDprBDaJRsRsZqTeIb_3SqS84MF6quGAb3ZAfbwRsDpJXZ09nomT4cgAhOM1Hn-_q8nAauOwuE3n_VnYTjmK3NqGhjb6Vu8-FJosKkK5-ydWNKenxlMHuAp7gEwvenK4XbciXfAEHzrthnAUveKwIZ_teg7SJlAdeXjhhn2gqkEqyr61Z7dknWVLGxt0aqFbE5dZpnQb97FsqBlrWWD_ZyAyMAKdz12ILojrL9QEpBTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏حالا که تشریف آوردید:
‏از ۵۷ کشور اسلامی، فقط ۸ دولت کشته شدن «ولی امر مسلمین» رو تسلیت گفتن و ۴۹ کشور سکوت کردن!
‏عراق، آذربایجان، تاجیکستان، پاکستان، لبنان، الجزایر، عمان و قطر تنها کشورهایی بودند که تسلیت گفتند.
‏بزرگان جهان اسلام چون‌: ترکیه، عربستان، اندونزی، مصر، مالزی،ازبکستان و… سکوت کردن!
‏تروریست‌های طالبان هم حمله رو محکوم کردن اما تسلیت نگفتن!
دولت فلسطین حتی حمله رو هم‌ محکوم نکرد! سکوت کامل!
فقط تروریست‌های حماس محکوم کردن و تسلیت گفتن!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5187">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های جمهوری اسلامی  از بستن تنگه هرمز خبر می‌دهند.
🚨
🚨
🚨
سخنگوی قرارگاه خاتم : به ۱۴ پایگاه نظامی آمریکا حمله کردیم و «صدها» ‌تن آمریکایی و اسرائیلی را کشته‌ایم.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5186">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔺
شادی مردم ایران از شنیدن  خبر مرگ خامنه‌ای
🔺
بیانیه رسمی دولت اسرائیل تا دقایقی دیگر</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5185" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حمله به بحرین
😅</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شاهکار جدید صدا و سیما  اینها رو باید تلوزیون‌های جهان در بخش سرگرمی نشون بدن</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5183" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">«دیشب مردم تهران در کوچه و خیابان  کل می‌کشیدن» مرسی از بابت این اعتراف و این مستند سازی از وضعیت تهران پس از انتشار خبر مرگ خامنه‌ای</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5182" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5181">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=NYVlimnz1-a0fcckx58CD6q2LmYqzLRNvlaQD6ion24Q5k4r8ZyZ8NrE-_Z0yU-_DWALYtM9Cnq7gKz7d7pZ5QxBlml_KqZEd4BXNE1Looh0OpbbjPESpplFxc01zhPksVDPIdjKw6JB5B4ly3aSGFz4GBuaXa_XpMNtMCyyPHA_0w7wIifhfmAlZkX3ap3hq6F5Issd-0mzxN4CwGVaYdvXNnw9eCtXUi0o97uqiggpKpoMCEFOGrBfNk4nYsernUYqrZ4o7RsgYId3y6FmiDfW1xFmwhSd9p_oQFfx9_mU47rrzhAeNne953520pflrdIbxCdqneDnJSC5O-0CGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=NYVlimnz1-a0fcckx58CD6q2LmYqzLRNvlaQD6ion24Q5k4r8ZyZ8NrE-_Z0yU-_DWALYtM9Cnq7gKz7d7pZ5QxBlml_KqZEd4BXNE1Looh0OpbbjPESpplFxc01zhPksVDPIdjKw6JB5B4ly3aSGFz4GBuaXa_XpMNtMCyyPHA_0w7wIifhfmAlZkX3ap3hq6F5Issd-0mzxN4CwGVaYdvXNnw9eCtXUi0o97uqiggpKpoMCEFOGrBfNk4nYsernUYqrZ4o7RsgYId3y6FmiDfW1xFmwhSd9p_oQFfx9_mU47rrzhAeNne953520pflrdIbxCdqneDnJSC5O-0CGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس پاکستان داره عزاداران خامنه‌ای رو با چوب میزنه  دیروز هم پلیس پاکستان ۶ تاشون رو کشت.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5181" target="_blank">📅 09:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بخش خبری ساعت ۱۴ شبکه یک و تکرار ادعای زدن ۳ جنگنده آمریکایی  در آسمان کویت و تکرار این سوال که چطور در آسمان ایران به این پهناوری نمی‌تونید ‌، در آسمان کویت تونستید؟؟</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5180" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فرماندار جم در استان بوشهر، می‌گوید که یک «پهپاد متخاصم» منهدم شده و وضعیت شهر به حالت عادی بازگشته است.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5179" target="_blank">📅 00:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از شلیک موشک از منطقه جم بوشهر به سمت چند کشتی که در تلاش برای عبور از تنگه هرمز بودند.
گفته می‌شود در جریان این حملات موشکی که از سوی سپاه صورت گرفته، به سوی یک کشتی آمریکایی نیز شلیک شده.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5178" target="_blank">📅 23:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=ubC1QI3iPltml3JQbchtrMg5xmMpQXKqhskUe5GvPBGXamTu-B30bjYRndT3R-5DUhS49Iwoacuipnf8cRX_-n8EM3BewNzaGEoeeOABAIByj5HLm0yRJ-RtcnB4wH9bFAHpE2wl3qeKuJ0hMjWz8jHnxpDZpv-H6hCwrP9DPsoNBD6pIswr7mOuG8uMxqbSGU8KsSC1LYKFJ324WKF3iwwwOKDOshbWmBl8fS9bbdlK08k_Q9T7NcsCORC0nS9abOJOouLH143BfLEr1KJREsRqOx7CbAAEmyscqWzmjsAK6sroINX4TwxtRls8xq_qT5lk07xt06JwTdCFwXWzaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=ubC1QI3iPltml3JQbchtrMg5xmMpQXKqhskUe5GvPBGXamTu-B30bjYRndT3R-5DUhS49Iwoacuipnf8cRX_-n8EM3BewNzaGEoeeOABAIByj5HLm0yRJ-RtcnB4wH9bFAHpE2wl3qeKuJ0hMjWz8jHnxpDZpv-H6hCwrP9DPsoNBD6pIswr7mOuG8uMxqbSGU8KsSC1LYKFJ324WKF3iwwwOKDOshbWmBl8fS9bbdlK08k_Q9T7NcsCORC0nS9abOJOouLH143BfLEr1KJREsRqOx7CbAAEmyscqWzmjsAK6sroINX4TwxtRls8xq_qT5lk07xt06JwTdCFwXWzaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=DVIW_RM4Y_MUssgWDNqb1ELo6UCnlNhnbnO03At1S-MjjeLk7lVzJiOD9tep5h7LPANBKyWJ0wkNR376IJduUaN9VqD4mq-IWVSCd_k-qs54JwDBxUGBBJBM9wO9FkCRzHk-IxSgRjBSOQuZJ8Zy7yvTC85bp1g-ZrzJz9-3gPwqx1_0sPBIw9W4j4-rCvI3TW7CN8ZeLJ8iaSP6hXOKeQhR1hl1Hx1R4rhYgKb4HvnIM-jrh5ObPVv5P9DTBxqKJPVYEgezOa0BBsuNSkexMJhgTObFtB90fpfg_IvW2Cm5N9GQ9JeAKkUamQmY5nIit_zX7QNN3BahBfM0gaRC_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=DVIW_RM4Y_MUssgWDNqb1ELo6UCnlNhnbnO03At1S-MjjeLk7lVzJiOD9tep5h7LPANBKyWJ0wkNR376IJduUaN9VqD4mq-IWVSCd_k-qs54JwDBxUGBBJBM9wO9FkCRzHk-IxSgRjBSOQuZJ8Zy7yvTC85bp1g-ZrzJz9-3gPwqx1_0sPBIw9W4j4-rCvI3TW7CN8ZeLJ8iaSP6hXOKeQhR1hl1Hx1R4rhYgKb4HvnIM-jrh5ObPVv5P9DTBxqKJPVYEgezOa0BBsuNSkexMJhgTObFtB90fpfg_IvW2Cm5N9GQ9JeAKkUamQmY5nIit_zX7QNN3BahBfM0gaRC_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از ۹۰ روز صدا و‌سیمای جمهوری اسلامی می‌پرسه در حمله به بیت کیا کشته شدن؟
کمیل خجسته، برادرزاده منصوره خجسته باقرزاده، همسر علی خامنه‌ای، میگه  افراد خانواده خامنه‌ای که کشته شدند، همه در یک نقطه نبودن! در جاهای متفاوتی از منطقه بیت رهبری بودن که به همه اون جاها حمله شده.
این همون حمله‌ای است که پسر عبدالرحیم موسوی ،
رئیس ستاد کل نیروهای مسلح میگه ؛ ۳۰ روز گشتم و جسد رو پیدا نکردیم!
عجیبه در این حمله فقط مجتبی سالم مونده باشه!!
چرا خامنه‌ای در پناهگاه نبود
!؟</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5176" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
آمریکا و جمهوری اسلامی به یک توافق ۶۰ روزه رسیده‌اند تا آتش‌بس را تمدید کنند و مذاکرات درباره برنامه هسته‌ای را آغاز کنند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5175" target="_blank">📅 19:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208f980645.mp4?token=VkYDQwSR3oPg50QnQ6twHmbQe731W1nldEalTrFeIV5zjF_xAEVgAQU_Zr-a6NpkxVNrzePjTG2T-C-21D1BypujdVwq1uSrIZ_MDbzGFNtKEGpk9sWhZYukI9I7koEgM4k3P4N3RdnbiYRr4oZacopi1V-4bVjclIIjjhCuA_qTU70TT-YwD3R5AVQI0OihIOnKh3Lx4kZkl9q5MEYdpneTDRn7AVch588U3Z9Q9j4_bc34avupxBiiMR-WP3SGbsY9RiWvKKl60zMBWPJt3VU9si-YLBjNF7-tS04qLTKKGZsFNe9sMg6WwJKHVblISHAk6rzA9ZsHeeA9WY5FVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f980645.mp4?token=VkYDQwSR3oPg50QnQ6twHmbQe731W1nldEalTrFeIV5zjF_xAEVgAQU_Zr-a6NpkxVNrzePjTG2T-C-21D1BypujdVwq1uSrIZ_MDbzGFNtKEGpk9sWhZYukI9I7koEgM4k3P4N3RdnbiYRr4oZacopi1V-4bVjclIIjjhCuA_qTU70TT-YwD3R5AVQI0OihIOnKh3Lx4kZkl9q5MEYdpneTDRn7AVch588U3Z9Q9j4_bc34avupxBiiMR-WP3SGbsY9RiWvKKl60zMBWPJt3VU9si-YLBjNF7-tS04qLTKKGZsFNe9sMg6WwJKHVblISHAk6rzA9ZsHeeA9WY5FVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش زدن ظریف :)
نوبت عراقچی هم میرسه!
این مسیر رو خیلی‌ها رفتن!
از منتظری و بنی‌صدر، تا موسوی،
خاتمی و روحانی، احمدی‌نژاد و…..</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5174" target="_blank">📅 19:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=DsSQrvsjXC9AYpQe5CT0DWFVF3K-8j5PbhRmDNqK2d4vizQO35PD4AKhXxLCACfaO0GIX0ePF2WD-8lusLwdUquOvSSrVzGaMvx8GO8m4drMChgHbn7miP--IQifvPj1ecVvwGjZkKM-wN3_UDv5XiQNxMv2eTwhkjwQJq5EHpJCRMRi-qN4_ok7j52HnXjKzP2OXmPeBqeah1A-iWxt6v7I_AfHI9kCAwbIfRfk2iSRGltxPUnJ3U5wGvnTWeHG_jNJlGmo_Y0TCdL5wiUA0fvoG_C6rGYTYjf3NBsX26-tqsYdO0b27aGwXeE_Kdi2Ov0PJ6CCMJILKNO1WDGOyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=DsSQrvsjXC9AYpQe5CT0DWFVF3K-8j5PbhRmDNqK2d4vizQO35PD4AKhXxLCACfaO0GIX0ePF2WD-8lusLwdUquOvSSrVzGaMvx8GO8m4drMChgHbn7miP--IQifvPj1ecVvwGjZkKM-wN3_UDv5XiQNxMv2eTwhkjwQJq5EHpJCRMRi-qN4_ok7j52HnXjKzP2OXmPeBqeah1A-iWxt6v7I_AfHI9kCAwbIfRfk2iSRGltxPUnJ3U5wGvnTWeHG_jNJlGmo_Y0TCdL5wiUA0fvoG_C6rGYTYjf3NBsX26-tqsYdO0b27aGwXeE_Kdi2Ov0PJ6CCMJILKNO1WDGOyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=RY2QQeTTDhUcaNmprj1oEOFZ_4gKzEm_5hbsVcRE6ZlL1kiWDguQc1rELGPqKfBhW4fJ6m0JwsY5VqRIvx8x4SjiT2XsRDig-zSllxrJOeNU4Q72AFybTbycLwD6YxehdR7VGl85A3xYqxg5Wu4LFYeQJ6CxsXRdRWYqIqK-AGXsc7Pi5PCoHZfeSHsK9jdejaD2NGcHTWaGXPVLaz5eyeImGcEC3jc4rCSr96TUapGSxE9YIpGc5S9MIKZyHegqp-Gr0efdmoIl3YOyMQAalAvtwaRhV0J-0xFwfdQiXCB2kfs9ZFgciASHxqRIyBoAaMT82pDSe9T-j_-85zAHsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=RY2QQeTTDhUcaNmprj1oEOFZ_4gKzEm_5hbsVcRE6ZlL1kiWDguQc1rELGPqKfBhW4fJ6m0JwsY5VqRIvx8x4SjiT2XsRDig-zSllxrJOeNU4Q72AFybTbycLwD6YxehdR7VGl85A3xYqxg5Wu4LFYeQJ6CxsXRdRWYqIqK-AGXsc7Pi5PCoHZfeSHsK9jdejaD2NGcHTWaGXPVLaz5eyeImGcEC3jc4rCSr96TUapGSxE9YIpGc5S9MIKZyHegqp-Gr0efdmoIl3YOyMQAalAvtwaRhV0J-0xFwfdQiXCB2kfs9ZFgciASHxqRIyBoAaMT82pDSe9T-j_-85zAHsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله هوایی اسرائیل به بیروت
🔺
آمریکا از دولت اسرائیل خواسته بود تا به بیروت حمله نکند
🔺
گفته می‌شود که در جریان این حمله، «علی الحسینی» مسئول ارشد موشکی حزب‌الله لبنان، که در واقع یک عراقی است از «فرقه الامام حسین» از گروه‌های نیابتی جمهوری اسلامی در عراق، کشته شد.
🔺
اسرائیل دیروز هم در حمله‌ای به غزه، فرمانده تازه منصوب شده برای «گردان‌های قسام» (نیروهای نظامی گروه تروریستی حماس) را حذف کرد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5172" target="_blank">📅 14:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">علی الحسینی‌ از فرماندهان ارشد و مسئول واحد موشکی «فرقة الإمام الحسین» حز‌ب‌الله عراق در حملات امروز اسراییل به لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5171" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJvxKZhmkp8tEq6SyYj7fiGa2hi1tS1qF_HCWSyP4gLo9PVkB7Lq3i1-qKSQUoo1nEgCZVj_5libz_9hhxltc_EMtNwt6VHUAEOGXqcFhsHgvYI1bnNfi950qf7U_o3eTwFWi8I0dTgVXI7v1Suu9Fy8EgJ0rn2EQIIZxHIXWYK1hIcbbWN5242j71g28cjO4pgXdXfJ6NUL-I5p9lDPwpeIjcKsCE2kpVsLcTQc_vxf2scyYqQQAsePZQYAkKACQOVNV_zQGKbNErsz5ATKIpkHBqyDdWHROO8j9Z8h9wW-74fQCSIWOZxJcCoPbA_gm3ZfQLI4eaS6dWWcxrRemQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام:
ساعت ۱۰:۱۷ شب به وقت شرقی آمریکا [۵:۴۷ صبح ایران] روز ۲۷ مه،
ایران یک موشک بالستیک به سمت کویت شلیک کرد که توسط نیروهای کویتی با موفقیت رهگیری و منهدم شد. این
نقض فاحش آتش‌بس
توسط رژیم ایران، چند ساعت پس از آن رخ داد که نیروهای ایرانی پنج پهپاد انتحاری را به پرواز درآوردند که تهدیدی جدی در تنگه هرمز و اطراف آن ایجاد کرده بودند.
همه پهپادها توسط نیروهای آمریکایی با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنین از شلیک پهپاد ششم از یک مرکز کنترل زمینی ایرانی در بندرعباس جلوگیری کردند.
فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای همچنان هوشیار و با تدبیر عمل می‌کنند و به دفاع از نیروهای خود و منافع‌مان در برابر تجاوزات بی‌توجیه ایران ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5170" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=ijLZyxoEI1kah5IhQHMZUfirLjQGkbsva_ZXbtZuOYfLzjbe_a1lOWdTjd3YHvfHM9m7WlfzaeQxQrmq45LhCWf7pkyDCCdyVkC1bCuRWMOWUU_1w-wgi5mMzmUqiLGAbvoBGIaxaTsILH1Q8D8xB81KKGuJnDIqf3x1k_7F7sWUtAjSe3WnX8_IWjeFO5h7m1DQADGJR9JLMFbhaGoJL9RQZAc2_1vUbI3r40rkDWQgWZ6CjBTPbJ3uC18oLBkKZpfz7RE3cCi0WkduJmFG2eIyxsWtlV--qAOHiv4SbS-13IdEgpOx09oX8qwoa4rCAZvvUvq0qy3kIodrVZ1CJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=ijLZyxoEI1kah5IhQHMZUfirLjQGkbsva_ZXbtZuOYfLzjbe_a1lOWdTjd3YHvfHM9m7WlfzaeQxQrmq45LhCWf7pkyDCCdyVkC1bCuRWMOWUU_1w-wgi5mMzmUqiLGAbvoBGIaxaTsILH1Q8D8xB81KKGuJnDIqf3x1k_7F7sWUtAjSe3WnX8_IWjeFO5h7m1DQADGJR9JLMFbhaGoJL9RQZAc2_1vUbI3r40rkDWQgWZ6CjBTPbJ3uC18oLBkKZpfz7RE3cCi0WkduJmFG2eIyxsWtlV--qAOHiv4SbS-13IdEgpOx09oX8qwoa4rCAZvvUvq0qy3kIodrVZ1CJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kz_fQKhuk_VaC7ZZnamA5mwcE4OuPNZFJpu8TZvU_gQbXx0iCm0r9h6uIkYv0uTOHdxi63Y0ZGkcq8RA9yaRqlQyj_P0lyT9E-NceQTmarVt_crwuQYoGBW2BJLGu11d5ABvMClIIotaTW57EQI9IyqWEwV4oLpD-Xi1I31A2eWKYpggHYQqTxvy1beLmHYpx73VuJLCHUAjilGNUZEzDMkSeV_ybxvQ14VWlWmWyeWL4tKKhgK-toOgRpqfqQ1ab9oc41Vma1Ko-Q3JCBcNwsOgslbiKnDgWaMf3G1c3NgnvnIf__vzTtTP7Wqfzg5S-oLS2I5G-g2L8AjiXbWdXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=UGWkecGMLH8R-gWXaHUhXzvlOuFcs1xgR6GVriiVi6f4f6eHRRaYhJFcxbyYO5BBuv9lDRLdrVhgH7tDsLGxcFjoTdnVctDest0df8LvsieCdVPw9ViTonQbMT2sILy2sn7cx1NZYA7qEELi1gIt2vPe-hZs2EVy3vpdJQBRtdkdp27DB7_MEBXhF9qa5P50MggHYGSKIfFrTpRAaBJy5xXkXaLaWSReh0cZ9Tw_2oii6ADeBFfCCmVtIUSGHRSdN2Z7nlR1yknBAXBvT_tWLZ04eSguCR58htUl4U0AQAlSaSlLJjOoFC4bzLInvoEibvk86lZvIU-b3Lh90Pwbxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=UGWkecGMLH8R-gWXaHUhXzvlOuFcs1xgR6GVriiVi6f4f6eHRRaYhJFcxbyYO5BBuv9lDRLdrVhgH7tDsLGxcFjoTdnVctDest0df8LvsieCdVPw9ViTonQbMT2sILy2sn7cx1NZYA7qEELi1gIt2vPe-hZs2EVy3vpdJQBRtdkdp27DB7_MEBXhF9qa5P50MggHYGSKIfFrTpRAaBJy5xXkXaLaWSReh0cZ9Tw_2oii6ADeBFfCCmVtIUSGHRSdN2Z7nlR1yknBAXBvT_tWLZ04eSguCR58htUl4U0AQAlSaSlLJjOoFC4bzLInvoEibvk86lZvIU-b3Lh90Pwbxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !
جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،
انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره و مفهوم «شهروند»، دادگاه و وکیل و حقوق مدنی، پزشکی و بیمارستان مدرن، بروکراسی اداری، مفهوم حقوق فردی، مفهوم و ارزش آزادی بیان، مفهوم دولت و ملت، سرشماری و شناسنامه و داشتن فامیلی و..
صد مورد دیگه!
مسلمان‌ها در دنیای جدید چی داشتن؟ هیچی!
هیچی!! لباس سنتی بپوشیم بریم توی خیابون هاشون نماز بخونیم و بگیم خدای ما از خدای شما بزرگ‌تره!
با نخوت بگیم ما خیلی از شما بهتریم!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5167" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5166">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
سحرگاه امروز ارتش آمریکا به ‌منطقه‌ای در اطراف فرودگاه بندرعباس حمله کرد.
سپاه نیز در اطلاعیه‌ای اعلام کرده که در پاسخ به حمله آمریکا ، پایگاه هوایی مبدا این حمله را مورد هدف و حمله ‌قرار داده.
بیانیه سپاه اشاره‌ای به محل این پایگاه هوایی آمریکایی نکرده.
اما خبرهایی از فعالیت مقابله پدافند هوایی کویت در برابر حمله پهپادی منتشر شده.
🔺
برخی رسانه های حکومتی نوشته‌اند که یک نفتکش آمریکایی قصد عبور از تنگه هرمز داشت که مورد حمله سپاه قرار گرفت و در واکنش ارتش آمریکا دست به حمله‌ به اطراف فرودگاه بندرعباس زد که ظاهرا مبدا حملات بود،</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5166" target="_blank">📅 08:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWvHYFgCvPHt-_Eq_N9ExdOx3JzH1LzAACfvUd9HV8uHV38ZSZJz32a0_hUhU0IHzuUBdf4s-atXbiyxHONKEZm_exfO0dAt1Oa0nEJ7pBklPf_IIUn38f9cgp5hb1GXIlUtpj-GD5q6I9ihySSNfK14FeYHGYowme3GvrRPbTeD_gnc3sWIgonUFs3RNmruQuEWXT9xExNGs7kTWPfrwUIdVUm4IbA6xAajRQl6_e5T34EpnIu65HXTHCMRP3M7GjRlDS1PVJIPV8yFLlBcfq4QZJNz9Izny74Hc37P2LTphjv-kF4SmtA9X_lFESZUkrIKiIGIE19w9GIZVdofCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3w0ENpqaL7_4Z40U5G54GAFWegi6rD9q-yzmjRAYsahaiEjm7dpfVUfu2PfGyRwVklVLHkwi3e0nnwdGWRuUhG_ykktbzgdW42rjn7doGf7swaCITIR2K-YwD6EIyFoW_OuBXc8N_dSjO41gtvZAxnSgMnGv0Tx5jirgKXJJbzvKTsjFzUPQdk72T9uiziAMO15dwoNX59JczlFyZHgE-rfprESOnpJEtFfmSDtZm0qha7Ee1AY0zY7mclgagqDlztfW4AEaJEZlEODBAMnacwA8eCZtV2Qmpc53PMQ8XA-XZlu0o_2RaLe07Sj6WT1O3X9CMU32hguJmefpC0n2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9_i60JcdRIvRApIW7evb4V_0uET5J1QNhodYllJI33Z-XH07quSFN1f-INtWT74n2Tx1sdOPtXB6g4FRXuPwN8l3ir8NqVsGOx4-QqAGEshZgNN8EnOgoBRqMK8as9yGLvZi5u2C2NJ5phxH2c_2c6qZ9v_vyeN8ZJBiZsrxTwa9x4plPltkuVMBAArdOUx1pxtE9ZSaWsPgHPILk-FpjN79CSG6HkbTvSHfz--ou3TW28SWvrSrK6_AV2sBa1_erD0Uue2CSJL-U4Dk7eUTuxwlJQXWqhwN3-etsGFWT9-rVKXjfKTL9uxkl3NJz8s-LeB00oar0rx2_ahby13jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfpqOKEspRxi7GLmtLMgLvo6GQo-eAjhGAcLVv00dhgXKPhXVj-ITpQ7FGDN4FcW6uBDTKfz5u0tn9bzyQrsq73KLNXmK_KnHpEpo2abfvW_qu552Xis4XxmEDvIOg-3ssciKqWlZ9P1SaGGTjuRDATOKlPF2GrpUaOaBnbmsv-RYF0TSTVAWv_ktY2Iccw9CLatxU6rqP6jvz9vyaxQov1fsCyfMSIxWSlBjSFJoTJAFYuvN0XVBuEmCHe-EQM8dLKVS1jZaJTfsB7sQesE5fHLgqhh5WuUaxsDtj1dM_VwbPe3VmSPoGjq_PVjMsDcYRG5PORoFya0SQh8HWMCdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rME1LQWfV3eCJNUJBLbrtxRxjXzBD0fr8ohn11rpCPWyBXBpk_pEd_WRUVh84G_r_5a-SGNRIMTHDgAGPSPa6JRjI32idNGT-QOV06e4sgpB7lKP7AlGIgJjjrTYk6LJ7LlC2y33U90wNniXgbhGoOWhGlkXlqK6VXIrcvufkUrMzvbonYIu0NOGFVtvizwoLj43JrdS_0dxE7I-PpBF8dvdwJpycwCdikX-K4CBx_wpWh-5Mx3Z6PQO6YGKFk6oXMitju84NI37K-IQeROxoadH-Sx2JoxVp44Bd6xsQqlhxPyVVPwkj7O5R2IgHJphSfSEnLbWoEG7iC9awSII7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnIXRoSk8sdi-67hQ_bcML_cTJzEkQXabGCFTbazMf3tH7VgPRiuRidPzIv96MHSdcGpx7F2Jczkvb5iYSyWp4-GekTBksIuPAGPvflXzTr1YsBK0JFDEZzHtKIADB98HsjwTxdf47j2N4i-rNgdhDZLCRYp2ZQNJz-IpE7UrepSnV4tsOuiKTyYBaT0x-dTk4hkTVdf9pedaQE0gQQZF2j3TxKi8cxraOqW0c0r_I8iHFT23jbgErWOvBtey9-a7rACmMAnAKTHmeNqxzV5LgnKnDpxKg_TJmR9FkSvtSKvs6EEaOcRWfl2O0cZFFOSoBRNrKKBtpmhP_iZzaunuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnBXp6rq4fOx2Cq-Hsj_faoUc7yFNkn4NrRytosZ-OGVwDyXNCHHT40W6eTiYB_hRV4hAl_YZ9fxbKaz2vkJ4cJTfrIeGXBDBMnPEdajBDpebhnbQCWzDitjOINUWAgE89EfjorUCyt9xNdVjg277T-xphhslld4MdR7N9p6tM0K1ZPJ6mW-78QBB2YG7sq7_x8EI36zQGwqL8BybPc-UevbaTMerV4X76bypNWShcExiGriEn9Hq54NagfSHxcBR5LfU9f1vNeyOXPxzWqf35DZO5IAucR4Y0hfeSe5jNg3Pu8qw0h5mKwnqlaRj1Lm08b_pP7zE58gd3sDKkEPIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvIzooARK49WOamDOLXDzHxbqZdjjwJOGhbrY5xjeigSes-O60pB-sJ6ojWPmwftWfHPPJyWrcwQ0yfQBbX1i6vPkraBTJxdA_iaRYmhpFT6AqhoZ1l1sZZCN1e8OOLLoT5ty8G1IuRVlQtN31xNg1-QLy20p22hOQyzCV5pDdZu9FuVQVTE4lnducKqUWA3Pv99cg3s4Fq2_6OXojTHSjO3HKTbSV8xSMKRM5rjtdJo5J66LTnJi72QMgdYT5igh6yrQlsOWfh2wBoLyN55omek4HqXyjDWbQPuJ0MtyhNIqTHJaYxoLUEMm7gTXOajFDP58VP3ffxDNjJiavVVKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=NmS-g0rMDKPB8LbJzWFqV5XU15p57HhocqoxR3H-lbOVkS58XvSDce1wXOuo88bc3qkX8KEf-cuhUfJw4U41zXeYhZcenlUJMgz1y6ML1eDZfqCqLgblYde0rwpQsvbkKXzwSrVd4gjhfkd2QV6fVmV51CeN-c7C3mPR-FfoGwhS1OVwHORTpe6-BibvcwWD2M50wDMLEnNg3K94wzav_cBQrQPIZh96WhVm-yNqsQOSWOcSRYCa0M5zvDCFa6LFmutAxxS1IBVhbic3ppcfWP5nfYMs5tCtyKvcbvq4bx6xdgD9nJTUsVstrKSJHA_pzsyNnA49IcIKpk9MajjWFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=NmS-g0rMDKPB8LbJzWFqV5XU15p57HhocqoxR3H-lbOVkS58XvSDce1wXOuo88bc3qkX8KEf-cuhUfJw4U41zXeYhZcenlUJMgz1y6ML1eDZfqCqLgblYde0rwpQsvbkKXzwSrVd4gjhfkd2QV6fVmV51CeN-c7C3mPR-FfoGwhS1OVwHORTpe6-BibvcwWD2M50wDMLEnNg3K94wzav_cBQrQPIZh96WhVm-yNqsQOSWOcSRYCa0M5zvDCFa6LFmutAxxS1IBVhbic3ppcfWP5nfYMs5tCtyKvcbvq4bx6xdgD9nJTUsVstrKSJHA_pzsyNnA49IcIKpk9MajjWFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا دبیر: کارمندان بهایی من‌وتو می‌تونن
در صورت بیکاری، تو پارک دانشجو مشغول کار بشن
مدیرِ تراز جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHi54I1vy5Ms3Ep2eXC3CSAXjvlVtfXfw6khXf1uWJTmfYWq5ZwGyenYaVO-amwX9Td1GGsJNG4r4GWc5dL-v_hlHfBUozu4iYqMzRRvJon25xQnvkzSCeWIt0UmF-t3QEC0YINZ6LbwF6BvBhlsDme6xoC9XWtVa_C8zvA4h0s1O_PHk5_0Z-GijdtJL9kYHfc2XfupoyWKD8x6BH9fCW9IjJZW67uH1tUAas77t6buIJLWBjjL9iRDRyorkSZ-C9t2sD7-l_rAowhyS9X1j_Ono2Ta5PTejLtNHBBlyJMSUphLVpxiROEsPZJzwYyqQDsJB5A4std2KWGBsNlqkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاریکاتور شارلی ابدو
از قصد جمهوری اسلامی برای گرفتن پول برای عبور کشتی‌ها از تنگه هرمز.
آخوندی که میگه : به نظرت
چقدر کاغذ توالت بهمون میرسه؟
اشاره به پول ایران و بی‌ارزش بودن
ریال ایران که ارزشش در حد کاغذ توالته.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjBT1zlSdX59ywLJ8Zs26G_Z3PjuRz5Iw_crdDvr73IJsAZk4VwpioVlASRDksMG9_p6XfB97WdP-MLR9rwNRH3npiA2XypmcUF9Jfu08xhVcVX57f5Gf-VTihiGDrf_O9ErHq61z_RBBv3B5r2y_-mYh3v69l0NIBtNJjgLbsHl7AwmwW_YrLnODFswqOwQcSwBLYL-JiZ8M4sRZ3nolqOY5JvoqNJx7NxqurMH-0bFkMaXQoIe5Hq8kgn_WAfybDD0DHDw8BTPh2w8IqucVD2ta2CU6bGOJeiBdlCzHm4yhi-cfLJ9QE4vZPqq04lrJRO0BcR6lOr_4fv8959_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Erwj-T82Pd7sWvXoa91XQQTSHUegcQ_uQxAvYvmrSL_wQ0GODEQeJj_isnpk-MCptAE5E5sWOcGK0GcZRgEK7M1XO_Bu53y_hO9SpcTAnrwyQ8-XuTSwuz06U3u0tUXWWl1TYKoaVcntol3zCAMjdCqKZsbvx3g7sY8_NQMLcQlg8yMPraNOdT5QaUAZLAMdksM0Pgi7YnElQMU99IchMQFrn5otYdaTQnqmR_WUufrbcLOXxO8ZSb1rXzsDzsjnPPQSb-w1WUpEzQ1tm_S-1hS7ObqiMszhDhQPGKouq1x_hAxgQhxyf2VaM3cmnXQPEnccknufI20RrcqswY8t6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fv2EnVgi1Ux5p_4RAArwKitOAQjqBwoKR_CTtX2OuBNzpoPFM1_qh5vb_OFwzfvQSz3GgYlFwHHYfVXW28M7V_1IijK3xMlHsQT5pkXHzy_lENZu_1iTglhUj3lp5YsfOrK4LGLKc-_ifnY9dvKwTj-fokINuLlDzYwgoHpAr8U50q3HidV0iFFgI2Nh1JSlm01s0PaFVHiz2KJusnY-_rhOIvM5P22AFjNAgr8uQRKWsEU79paNDPJqZ42UBs4z90TfF7GgJ9M3bz8ujOWTlwe_KX2szxLRof68DJfj7MkVczeggdqmWN-K8zod9TyJQcNPTX8MB-UMbHH0Kk8bqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sesPcB2XfPnzV5UezFxtu-05cZPyj6xfk3MuLrHv3dV9K-XBUY6FoP1R7Fp_QTWSHmCR4k8hrIGV7b5Zf6Bb_GbDfbWjoLG7cl8gTOmFlLS13lAmtixpUEUzLby0te1XUUY0MmFlITV7agbl6iTF_UhPoiR9n1FgBxSNxO2IKlUzRB-fa2-MMGkBlFtsyIPHHjV63ySKKG7koZV54GyXgN49jtMlpyk66fznd3awg0VajT-R5KMBjtq_jmWKMEFwfjNj6No5jm5SN8xR441UypSu11jXbatVwrFF9UfAsnmwH6pMwAFlFAqqTmL4gnA0osepqwET-biVlvUekxlwWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=rrZE1MyvnlIEyrOHxkSIqC90GbuhkiXO8L4Idpu1-6KZbWhfOo2zPVz7eDNtAh6L0FlAU2-pnCL3S1Lmx4AJgSb6vaSrMk3mM8KrlRhlG9_GYjHEKjudaeMRc6d-YPz3md1GbtBfWteYhTGimU34yFZMFr3Rylsp5mRdsXgxB-NkegNsSdKAN4pp2bUT4-NQhakRhMWVgYDw2ejhx75Q0klXcb5XtAQWLmbaI93cza-0ez2N8jiRyfe_ldhR0Cdb989E2_P1n8Zby1XiYxJUOnQg_lH3IVv-01SQ5np07u3MqfCVkZ-fMso82kOLM-29Vy7Q3doN_gkXuvQaPMQP0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=rrZE1MyvnlIEyrOHxkSIqC90GbuhkiXO8L4Idpu1-6KZbWhfOo2zPVz7eDNtAh6L0FlAU2-pnCL3S1Lmx4AJgSb6vaSrMk3mM8KrlRhlG9_GYjHEKjudaeMRc6d-YPz3md1GbtBfWteYhTGimU34yFZMFr3Rylsp5mRdsXgxB-NkegNsSdKAN4pp2bUT4-NQhakRhMWVgYDw2ejhx75Q0klXcb5XtAQWLmbaI93cza-0ez2N8jiRyfe_ldhR0Cdb989E2_P1n8Zby1XiYxJUOnQg_lH3IVv-01SQ5np07u3MqfCVkZ-fMso82kOLM-29Vy7Q3doN_gkXuvQaPMQP0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixO5Bb5sxEQOqT0x5kyk73RnUbSOpdfTndVOCOz7v1XO04rpmk1lyNeKgKd-0G3wXZqlrkrflqrSrc0y5fgyc8X-QS6Xo6DRr2B3VabchiKJw8YUmTkOfywVSkvG47yVIy8kIgkeyXjWNPp9nNUA6yf_RyQZAT9smIT6iiOApZmUwJgtH6GwHgYZ1eSgDiIrMWSAilmShXeCLjT6Y4wEICRj9VRFuraYk1IT_YeNINzNuTIK1i3s7A8QKQxgh8uHORoKNpcKhcwHGJUXdDrR0qYEvueT868ur6uakWx2DgEROTW1om8rLfJhTA1Rjlmz43HDiMiIHWBILbMPTTIgDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=AJmEAQ0mlkSPL5cXxHgmotq0-6H5TwItiAU_-FZ4m5t0pcBECVykh_GvmjqrUMIzWNjgHPi0uCAhUF6wiPau0CTk1KKUFwA_mgbvIWBJcNoxaipCjVVihq_89gNkPtT2k3cOjY4tRT67SMOONmIgeu2nR2BGGiEXCW8Hznjp4LGBOCORCf7RlUuzh0h995f6Sagm8p7Z0dwnkuLrtArD0sThPho3qYShaE1GClTihnE8ITjHxK4k25uyiH9aJ0OcxMmuoNOYKv48eA4tN_hN17zkh6nIuQjR0e6mvKUf6clV7qK7Eg4zPZFycRK6DQ61wJTkLF2aNXobj4qL-jkhAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=AJmEAQ0mlkSPL5cXxHgmotq0-6H5TwItiAU_-FZ4m5t0pcBECVykh_GvmjqrUMIzWNjgHPi0uCAhUF6wiPau0CTk1KKUFwA_mgbvIWBJcNoxaipCjVVihq_89gNkPtT2k3cOjY4tRT67SMOONmIgeu2nR2BGGiEXCW8Hznjp4LGBOCORCf7RlUuzh0h995f6Sagm8p7Z0dwnkuLrtArD0sThPho3qYShaE1GClTihnE8ITjHxK4k25uyiH9aJ0OcxMmuoNOYKv48eA4tN_hN17zkh6nIuQjR0e6mvKUf6clV7qK7Eg4zPZFycRK6DQ61wJTkLF2aNXobj4qL-jkhAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخلاف
گزارش صدا و سیما
۱- بسیار بعیده آمریکا و اسرائیل
به جمهوری اسلامی حق غنی سازی رو بدن،
۲- غیر قابل تصوره که آمریکا
کنترل تنگه هرمز رو در دست سپاه بگذاره و چندین کشور ثروتمند عربی
رو بگذارن گروگان اینها باشن.
مسئله بزرگ‌تر از جمهوری اسلامی است
مسئله سرنوشت منطقه است.
۳- غیر قابل تصوره آمریکا تحریم‌های اولیه
و ثانویه و….. رو برداره و دارایی‌های
مسدود شده رو بهشون بده!
🔺
اما اگه این حرف‌ها ۱٪ درست باشه :
۴- فاصله میان جنگ ۱۲ روزه
تا جنگ ۴۰ روزه حدود ۲۵۰ روز بود.
ترامپ بعد از جنگ ۱۲ روزه گفت بود :
« جنگ تمام شد، ما پیروز شدیم و تهدید
را خنثی کردیم! »
۵- ۱۶۲ روز دیگه در آمریکا انتخابات میان‌دوره‌ای است.
ولی شاید حتی پیش از ۱۶۲ روز دیگر،
جنگ سومی در راه باشد! و شاید پس از انتخابات.(با فرض اینکه حرفهای صدا و سیما درست باشه!)</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=V2_J-5T0u6gHOB-jG0nH6xFCsc2m4AUBceg1N6pmrrhKpG6XlvESX6R8xPakG5-7Fp8Z2OuMLOyM_W25jGYrd-zyhF8zrQhvEDp9G_b1EjXUcdVGDSl6J5t-ss_uh5iWh-t6IGGKqQadMP_X6TljsKf24Z8b2p31OBeHnLndljC7JxpOJ7bNIFA541ddd8gHCYcn0dyot74qRd4XruzEOIS5l2G-Ye8yMwY-QsirxAa1S8N6EG8NGHhbe3lediTSkDzq3ZjPwwIEXVcN0x2eacw8AkwQIIuaiBHfK4Ld2oTalaAMVcTnt4_WuVtwSliuBFTschJVuyr2WcHI5-o9RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=V2_J-5T0u6gHOB-jG0nH6xFCsc2m4AUBceg1N6pmrrhKpG6XlvESX6R8xPakG5-7Fp8Z2OuMLOyM_W25jGYrd-zyhF8zrQhvEDp9G_b1EjXUcdVGDSl6J5t-ss_uh5iWh-t6IGGKqQadMP_X6TljsKf24Z8b2p31OBeHnLndljC7JxpOJ7bNIFA541ddd8gHCYcn0dyot74qRd4XruzEOIS5l2G-Ye8yMwY-QsirxAa1S8N6EG8NGHhbe3lediTSkDzq3ZjPwwIEXVcN0x2eacw8AkwQIIuaiBHfK4Ld2oTalaAMVcTnt4_WuVtwSliuBFTschJVuyr2WcHI5-o9RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما:
آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده
‏۱. آمریکا متعهد به عدم تجاوز به ایران شده
‏۲. استمرار کنترل ایران بر تنگه هرمز
‏۳.پذیرش غنی سازی
‏۴.رفع همه تحریم های اولیه
‏۵.رفع همه تحریم های ثانویه
‏۶.خاتمه تمامی قطعنامه های شورای امنیت
‏۷.خاتمه تمامی قطعنامه های شورای حکام
‏۸.پرداخت خسارت به ایران
‏۹.خروج تمام نیروی آمریکایی از منطقه
‏ ۱۰. توقف جنگ در همه جبهه ها از جمله لبنان</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSJgbYLtKUpBfMKW8seas0QcLxAFmT3rJAO7uX3-MxQofkgou9pQFlO7inVC9W0GH2ZjN8cfPSKvu62VjvcGr68Nf_VWA7RvZ6RzICsxXOV1ENX66jl8T18_Tn8Nz9mjeJyai0JEgjD11v7ojbYvIhopyT-Ala9doVECrP4hnpsUo_5pEW_wafWFOJjoJxv4iRQIFTmGZ1c9vhg3_phpdqaiG3dZfdsd33KIiNHKaHw4ff1GVF0SNXfvqR5VCNiwohdcmxa6bn-90VU0EVvtGOoclwDOwBVWYuIU6sTh2DGSLmUiYdJ5rvSh0WzWq1ylQcyqHYmbI6Y-ZA6zI_0Obg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">️
🚨
🚨
آکسیوس: یک مقام آمریکایی گفت که پیش‌نویس یادداشت تفاهم شامل تعهدات ایران برای هرگز نرفتن به‌سوی ساخت سلاح هسته‌ای، و همچنین مذاکره درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالا از کشور است.
☢️
به گفته دو منبع آگاه، ایران از طریق میانجی‌ها به‌صورت شفاهی به آمریکا درباره میزان امتیازاتی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، تعهداتی ارائه کرده است.
- ببینیم چی میشه. بعید می‌دونم جمهوری اسلامی اورانیوم غنی سازی شدهاش رو تحویل بده،
خبر هم میگه ج‌ا به یک میانجی (پاکستان / قطر) شفاهی گفته!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏
🚨
🚨
ترامپ :«من اکنون در کاخ سفید هستم؛ جایی که همین لحظات تماس بسیار خوبی با محمد بن سلمان آل سعود، ولیعهد عربستان سعودی؛
محمد بن زاید آل نهیان، رئیس امارات متحده عربی؛
امیر تمیم بن حمد بن خلیفه آل ثانی، امیر قطر؛
نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی و وزیر علی الثوادی از قطر؛
فیلدمارشال سید عاصم منیر احمد شاه از پاکستان؛
رجب طیب اردوغان، رئیس‌جمهور ترکیه؛ عبدالفتاح السیسی، رئیس‌جمهور مصر؛ ملک عبدالله دوم، پادشاه اردن؛
و همچنین ملک حمد بن عیسی آل خلیفه، پادشاه بحرین داشتیم.
موضوع این گفت‌وگوها جمهوری اسلامی ایران و تمامی مسائل مرتبط با یک “یادداشت تفاهم” در ارتباط با صلح بود.
یک توافق تا حد زیادی مورد مذاکره قرار گرفته و تنها نهایی‌سازی آن میان ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلفی که نام برده شد باقی مانده است.
به‌طور جداگانه، من همچنین با نخست‌وزیر اسرائیل،بی‌بی نتانیاهو، تماس داشتم که آن هم به همان اندازه بسیار خوب پیش رفت.
در حال حاضر، جنبه‌ها و جزئیات نهایی این توافق در حال بررسی و گفت‌وگو است و به‌زودی اعلام خواهد شد.
علاوه بر بسیاری از بندهای دیگر توافق، تنگه هرمز نیز باز خواهد شد.»</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOEZYkFP0P6mgvfniJYpZuHH-nB0aQc7v4-3RV-2_xpy-73C1DxSZCHWK_r45IkVthx2xRaiVgDY-B026AP-ZggUjtc3W4OcMnUqiA6ItggmjjD2dYQkxR6vhURnABCZysrl8hgFCPe3px-kNZweWdPPP4FCwx84mxM_4ZPVUGKQWw_S6xJFc5J0nctW-Vn1o9kdpByalGsBz2afB5r_oJsn713nOFHqb41kwrNIUrrpUf9Uc6ZJmppOjxAXQBX5wU16P2WF4flmNN9IV5BLYThaflPukD8-2moO4kRJ1V9zajKg_JG_fLTh_eU0Y2L9Vm3bxp-G_igOa6HjZpBCXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
آکسیوس :
ترامپ ساعت هشت شب امشب ،
در یک تماس کنفرانسی
با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5130" target="_blank">📅 20:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=QhpKr-XlhZkGgmWFIwlon9B1sQkoJe_t45_7prNtGcjgMZoS50DDps4MCQTTWK8E3tMrD1ecnyyprP3Wo7C16gHnfiHL9SvRnVcjF0wm6IKvdmEpD1wGzi6SWJa-Dj_qz1s2X5gSJTyRPZFXJvs-4vEoPnIIj0ig_y8JBXU_hlw9g47CrpUSlT3Mhn_cqWkSwipy4ybLX90FsY1MvDj4g78hjQzcJt3PvJHVHy0vHownIldd_g1kZ3aXFYjJiDcYCPkqwQydK5xqFikJZ4IZzGly8AiDfmRCPfLU9dOzdFmxbS6DS8qfzCTTppTVj18RHiiHGPTr4QGpNQ--48Io2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=QhpKr-XlhZkGgmWFIwlon9B1sQkoJe_t45_7prNtGcjgMZoS50DDps4MCQTTWK8E3tMrD1ecnyyprP3Wo7C16gHnfiHL9SvRnVcjF0wm6IKvdmEpD1wGzi6SWJa-Dj_qz1s2X5gSJTyRPZFXJvs-4vEoPnIIj0ig_y8JBXU_hlw9g47CrpUSlT3Mhn_cqWkSwipy4ybLX90FsY1MvDj4g78hjQzcJt3PvJHVHy0vHownIldd_g1kZ3aXFYjJiDcYCPkqwQydK5xqFikJZ4IZzGly8AiDfmRCPfLU9dOzdFmxbS6DS8qfzCTTppTVj18RHiiHGPTr4QGpNQ--48Io2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد از صدها سال
مردم شمال مدیترانه و جنوب مدیترانه بهم رسیدند
الجزایر سال ۱۹۵۲  (۷۴ سال پیش
مناطق اروپایی نشین
و مناطق مسلمان نشین</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4Z-N4piRHEUnmqWxGlH9lXhGUxKZU4ymx_IjtTw6mEJ7xGMzwFalTvZanhvdF7J5YZlX_aiYV73T0j_c6ubPLuU2OnfY61r8S694zx276jwY76dLAKgYV3ps18sffbfLo4nNsacK4KlMb6wLbmbXbKVKi_BeLz5QLT50KlAfSxwrkkUfVD_Rar8SPtTWuEzP6zkfimoe1E1Pu3UENsdGTetEwZiOCgVkVQ8jraiCIniyxu8-leV_GierY_iy1Fz9JXUZS6Eq0Zj25qu1Yrp3q7GgpoMf-AMRpbFTT5DfEvqqmPwI_6WUDVxxuhxG2ZRep5z_YfIz1EvXVNoM9ZR5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمال دریای مدیترانه، اروپا، نماد پیشرفت
آرامش، ثروت، هنر و معماری و….. است.
جنوب مدیترانه، نماد فقر و بی‌ثباتی
و جنگ و سیل مهاجرانی که
از این سرزمین‌ها می‌گریزند و …..
مصر، در جنوب مدیترانه، برای ۹۷۰ سال بخشی از جهان یونانی - رومی بود.
لبنان و فلسطین هزار سال، لیبی ۱۲۰۰ سال،
تونس و الجزایر و مراکش حدود ۹۰۰ سال.
تا اینکه اسلام از راه رسید
و تفاوت میان شمال مدیترانه
و جنوب مدیترانه شکل گرفت.
و دو سرنوشت متفاوت، دو چهره متفاوت گرفت.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
