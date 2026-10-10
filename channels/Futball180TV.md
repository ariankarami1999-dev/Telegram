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
<img src="https://cdn5.telesco.pe/file/Acj64csvQBsys5TPezw2zR-1z6Ym67dejw6csrfrtdSTkL7LbKVLqLJHbhB_d76-q3469NcD4dmozNsvAPcFuAQFsn7a4QR3MJ0AzSiN-QMms3scuE5hAliNPkV2YmObXk-x2cfK8XONgm2X7k4UxdezN7ChkXL8D81YTDMA1sVRcT3uBnzqhLLXrzTszt5EhJ5-vbQ5XTg7GLSP5sUAWrVIWBG1lXZH7yByewbtmWAdwRPnAFNq56eb-YOxNAWAWar2MRisVK1KhYpeKS9Biz0L0kvmmXKwj1m8gD2uUxbVX4nresCXBGerj29azs6Na55TBNu5J9FxYR4FtniLSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 386K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 21:02:44</div>
<hr>

<div class="tg-post" id="msg-108285">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8kwp5HVRirLaxCNmDeRW9oS-s8B0pD4Y0EECCBarTh9VMoMK-GtsbXUJnT89W9JZ_89OEsTNn1x1jo2d1myCmq95oKC9NVAm5BThN5nv8hVj9OdAjS8dUk9OMXw74W6xBav416JBE11lQbUtQ72if44p6LM8x-db-4cEa1ZMPMYtqdH8rQJo0h_zY0nLeIa8t4kiV6s7ZBBw_wC2xsHMKi-jiagk-mGUcEwXvxrsB7C1K-DemSWKP7llq2uAXmHGjYqi7Whbf0Ne_U8qCQtu5LCbac2tsl6wq_dsc3QAcZNaWK6PJXR-8dmKWhG92RUB-VEGlTtgjFSt593tMg1Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇵🇹
فدراسیون فوتبال پرتغال از بازگشت رونالدو به تیم‌ملی در فیفادی نوامبر خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/Futball180TV/108285" target="_blank">📅 20:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108284">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9c23307a24.mp4?token=MKXuwreS0uYSEWaBI8w5KJ4sv6RSr7IbRA2tMYA8cRClqyxmXUXehbYq7UdUYK2HbjFaKJh34UyFvIqntg4lwqf4CT4faTTxSsvWZYgQj0T0njkwmvda1cFHYqr2oH--Sv1eBIaLcdSYkwG0rfypevkZuwEs6bzR4HvSG3e5WoT9wyvCEAyhdk4pHlIJPESCHqTuTm6AbqKbVdqHoYOxO_ppgw6gQ3YjE5HgQBAWlr2zlhmCLTSSNjm7VePhrQFRugxM-CplN_8ZrvB6ZzVgKOTP73moXRzz1t83xzZPnnL9b5Pcy9OTcqHuX-LMwixsYuIHHqju0PTwxMdEIQGFHiRS-i7k_VOMCVADCHYk9YbIi0ehrFxonDr6HP80sZdQWyWBKXJUF-hH-_33KpnB4ikEbwh3fRLgvcrRMzN9brB2ack_eG_Rz2YrF7MEliXxbOP82Ok5qNLebqa3yPXmh28MIL0oKgAWibOU3nqzF8nWkr9P_ZQjXowc6azYRg613SJoeePcWx5MZrB-wrUdHS1dokznXb-zu-snb7qb-dqpKS2xySVusvGSGI6UmmMnMmfzY_n7aSXKXeeXX02RWl-A9auj1sbeztPgUyaE4l60tqDhWXF-9JxiDuTofGKBLhXQggKpcB_bcpMs1a_GXHs8GGzujgGpXIejr6SrUIs" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9c23307a24.mp4?token=MKXuwreS0uYSEWaBI8w5KJ4sv6RSr7IbRA2tMYA8cRClqyxmXUXehbYq7UdUYK2HbjFaKJh34UyFvIqntg4lwqf4CT4faTTxSsvWZYgQj0T0njkwmvda1cFHYqr2oH--Sv1eBIaLcdSYkwG0rfypevkZuwEs6bzR4HvSG3e5WoT9wyvCEAyhdk4pHlIJPESCHqTuTm6AbqKbVdqHoYOxO_ppgw6gQ3YjE5HgQBAWlr2zlhmCLTSSNjm7VePhrQFRugxM-CplN_8ZrvB6ZzVgKOTP73moXRzz1t83xzZPnnL9b5Pcy9OTcqHuX-LMwixsYuIHHqju0PTwxMdEIQGFHiRS-i7k_VOMCVADCHYk9YbIi0ehrFxonDr6HP80sZdQWyWBKXJUF-hH-_33KpnB4ikEbwh3fRLgvcrRMzN9brB2ack_eG_Rz2YrF7MEliXxbOP82Ok5qNLebqa3yPXmh28MIL0oKgAWibOU3nqzF8nWkr9P_ZQjXowc6azYRg613SJoeePcWx5MZrB-wrUdHS1dokznXb-zu-snb7qb-dqpKS2xySVusvGSGI6UmmMnMmfzY_n7aSXKXeeXX02RWl-A9auj1sbeztPgUyaE4l60tqDhWXF-9JxiDuTofGKBLhXQggKpcB_bcpMs1a_GXHs8GGzujgGpXIejr6SrUIs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم بارسلونا به ختافه توسط گابریل ژسوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/108284" target="_blank">📅 20:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108283">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔥
🔥
🔥
🔥
گابریل ژسووووووووووووس</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/108283" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108282">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بارساااااا دومیووووو زدددددد</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/108282" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108281">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/108281" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108280">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9dcb84758.mp4?token=Ewqy9RoDywp4RFF-GSjNKXXr6IHGQMPKOer0xFE1H2kDz0tk20kPWOLtg6nFpXhLSIaSHjK7VA-vP8ZIiopO7aGAFLHFxBcV2B-kGv7E1wibWa-V4EGoY4u3CVh89-mFQJL7RFTRqIVnhpgyg6gcQ3TjryS7FvqUZnnG66JYMyhynX8O1agxt7S63SwZEIUCWFT11YYcyCQXHBqAoPlFKI_M3Wc-7wApBegpDdGqNMOcbiKBZntNoMfBpwEE-wn2Q1P5d0AaZK4Kyy2YuYrs5QT9quZO2bjrFxixueb46rX7x_inhYxh2uaz6oIvDuKlXMIOpPjT2r50sL3oZviZoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9dcb84758.mp4?token=Ewqy9RoDywp4RFF-GSjNKXXr6IHGQMPKOer0xFE1H2kDz0tk20kPWOLtg6nFpXhLSIaSHjK7VA-vP8ZIiopO7aGAFLHFxBcV2B-kGv7E1wibWa-V4EGoY4u3CVh89-mFQJL7RFTRqIVnhpgyg6gcQ3TjryS7FvqUZnnG66JYMyhynX8O1agxt7S63SwZEIUCWFT11YYcyCQXHBqAoPlFKI_M3Wc-7wApBegpDdGqNMOcbiKBZntNoMfBpwEE-wn2Q1P5d0AaZK4Kyy2YuYrs5QT9quZO2bjrFxixueb46rX7x_inhYxh2uaz6oIvDuKlXMIOpPjT2r50sL3oZviZoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
حجت احمدی: سیلی نبود، آقا ساکت بهم خسته نباشید گفت؛ پیشنهاد استقلال؟ خبری ندارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/108280" target="_blank">📅 20:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108279">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/faa2aa1c08.mp4?token=OnQBDeyrLoBR-03dVDwfJiGFjtp8IJW7FnEjrE40Ywt2KnwOBE_l8Sk6iAwYenzHgo-e8HwfjvQRKdI7fzO2OrhHzxbrRlv-UY3r8qjugnIvZ92TMMyzjB4MoqYRlux3EUr8mCNIY-yYnb6KbMMO39swMW2ziJ47f2RI5gkc5D-LE_eEKp6G-EKvnPuj1neaWN76PtRdxNNybA9FFSjomP8bHlhAB6-y7mYLjUwdJ5FSKkHU3tPVkFvWkZ-Dxr9v9ss68_ZTKYak0YJLo7xc0oxOFwTTHZIKayJsfSg6Z8IWx3FI4z3SJO1aS74WZAE4e7hbQV4sDBltdoQHhBx7qz-LHhiQTdlyy-6kIyYYoHHf56uvSi13wZH4Ag8ksOIjY-ozqUUMY5AFaajTxYWv9FqGtaTWQ-6JNJvXgFURUiK2xsvuqJYvwJgb8p5fR4mWTuY5wR-KBUVf9o6GGHVIjUrNoA3KC3FkYGWDO1KTWlglrQElSNAMTIkZt9wC9dXSimHFLHWHSsBMQ0LrOLxJl3ZH2jhNtp7ivgdYLrRP29b86C2AMwAr271e9QJbLVOcV8LLD1yOc-LpU7L8uTzfnrcPWRs99RCO4k4Q3sOhB3rkxbLmz_CJNGxd7-kYz7QVtFUiP05brPglPAFi2ej99XXdOFY_zlwOsK-W2zTdNG4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/faa2aa1c08.mp4?token=OnQBDeyrLoBR-03dVDwfJiGFjtp8IJW7FnEjrE40Ywt2KnwOBE_l8Sk6iAwYenzHgo-e8HwfjvQRKdI7fzO2OrhHzxbrRlv-UY3r8qjugnIvZ92TMMyzjB4MoqYRlux3EUr8mCNIY-yYnb6KbMMO39swMW2ziJ47f2RI5gkc5D-LE_eEKp6G-EKvnPuj1neaWN76PtRdxNNybA9FFSjomP8bHlhAB6-y7mYLjUwdJ5FSKkHU3tPVkFvWkZ-Dxr9v9ss68_ZTKYak0YJLo7xc0oxOFwTTHZIKayJsfSg6Z8IWx3FI4z3SJO1aS74WZAE4e7hbQV4sDBltdoQHhBx7qz-LHhiQTdlyy-6kIyYYoHHf56uvSi13wZH4Ag8ksOIjY-ozqUUMY5AFaajTxYWv9FqGtaTWQ-6JNJvXgFURUiK2xsvuqJYvwJgb8p5fR4mWTuY5wR-KBUVf9o6GGHVIjUrNoA3KC3FkYGWDO1KTWlglrQElSNAMTIkZt9wC9dXSimHFLHWHSsBMQ0LrOLxJl3ZH2jhNtp7ivgdYLrRP29b86C2AMwAr271e9QJbLVOcV8LLD1yOc-LpU7L8uTzfnrcPWRs99RCO4k4Q3sOhB3rkxbLmz_CJNGxd7-kYz7QVtFUiP05brPglPAFi2ej99XXdOFY_zlwOsK-W2zTdNG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول بارسلونا به ختافه توسط آنتونی گوردون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/Futball180TV/108279" target="_blank">📅 20:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108278">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">آنتونی گوردون</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/Futball180TV/108278" target="_blank">📅 20:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108277">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بارسلونا دقیقه ۲ گل زددددددد</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/Futball180TV/108277" target="_blank">📅 20:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108276">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گلگلگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/108276" target="_blank">📅 20:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108275">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/326220841f.mp4?token=sB007Ytu50fxEPWA024gh8bk_bn-eVoQYYKHSVcpZOOWyvjZDsg0sNEIcaQhqDexDCowxWPShrUP3jkp9c3FVYMQ1T6EX-3wbBCKCq9AI-E6D-DAXOZ_3ovMf4LY7Iyet1yJeyTWiS9Mt1K6rnpXH4nxOjlt2kSoLvW-sm4bY_2jzOwRWdKPIFZElIKuJkrOmkPZhYSqzhJj9lZW_0Eg3KyRInZIVOi98C4_sLXzl-U7QSKr7Yt56petGc015o1RIcsF7xjIbCVZgkUvm0q1abaLdZzM97eAXaYKZaoGuT4D87VhE8ipsXMjfWYGpfDI5reFOhx2dcYWBi8F0zS89UqrDYqB0Oz2FJ05gIcYkuLeP0eKoIqyoKydje__82V2Pz5TeBCFZCU-OUAxtRaxuRdMKoZK-udSnByB_ZHMcoF2JLdi5TOearOPfHKqsLFwW11TyyagQC3F5eKx16xDTwH2g3TCXH-nsG6Qf61-4bQ5h8Pkn2TEbjVLSJbNRMbWBShvsLjeYbVCJ-Vf9VIb30E1I0dtKUVAILOw-mRe-NtJr4SqSod8tgZBzTIfkcl10UF9R404vERgKnuDXIJoPwFQ6BMVSqQbbQhTbm9kz4WExa2ONx6A6XOToJ72S7wxX9JGTMDdMUba4I8KWSch2kBEmUqnnw87wsZFb1UlA6U" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/326220841f.mp4?token=sB007Ytu50fxEPWA024gh8bk_bn-eVoQYYKHSVcpZOOWyvjZDsg0sNEIcaQhqDexDCowxWPShrUP3jkp9c3FVYMQ1T6EX-3wbBCKCq9AI-E6D-DAXOZ_3ovMf4LY7Iyet1yJeyTWiS9Mt1K6rnpXH4nxOjlt2kSoLvW-sm4bY_2jzOwRWdKPIFZElIKuJkrOmkPZhYSqzhJj9lZW_0Eg3KyRInZIVOi98C4_sLXzl-U7QSKr7Yt56petGc015o1RIcsF7xjIbCVZgkUvm0q1abaLdZzM97eAXaYKZaoGuT4D87VhE8ipsXMjfWYGpfDI5reFOhx2dcYWBi8F0zS89UqrDYqB0Oz2FJ05gIcYkuLeP0eKoIqyoKydje__82V2Pz5TeBCFZCU-OUAxtRaxuRdMKoZK-udSnByB_ZHMcoF2JLdi5TOearOPfHKqsLFwW11TyyagQC3F5eKx16xDTwH2g3TCXH-nsG6Qf61-4bQ5h8Pkn2TEbjVLSJbNRMbWBShvsLjeYbVCJ-Vf9VIb30E1I0dtKUVAILOw-mRe-NtJr4SqSod8tgZBzTIfkcl10UF9R404vERgKnuDXIJoPwFQ6BMVSqQbbQhTbm9kz4WExa2ONx6A6XOToJ72S7wxX9JGTMDdMUba4I8KWSch2kBEmUqnnw87wsZFb1UlA6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇪🇸
اتلتیکومادرید با این گل دقایق پایانی کوتی رومرو مقابل آلاوس دو بر یک برنده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/Futball180TV/108275" target="_blank">📅 19:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108274">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی چلسی پنج - یک بورنموث
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/Futball180TV/108274" target="_blank">📅 19:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108273">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec5d3b26d2.mp4?token=T_51HZnROKpNLXHDGjbaoyd7HtehnKXxGoPCy9AuBQMZz7ju5JY27jaPdbTnhGK1ItGoQn3hY3gF-BcARqIgWO1BKrZamQp21jXEWJHRVMlCJ8qBcfLCJ5iiWurc9qVb007gn3CyzGGbvXeKNFg1Xqu7BbDlz_H9b98QsDrY0l7EV3HxyPm8upsJs---AIhZvuFI_tlS7wM0J1ctqynjGFXwX8mvLMyfmc-wBkKBLWvmh1Pe1dpZsZsXEPAU_RyMZRUqxKocLvWK-XuU7Q__welAcsw1cQxmDS0oqFPBQmh5r672GNkgr2MCqAW09D1zBYhbOKwlL93cgQPJbOKpRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec5d3b26d2.mp4?token=T_51HZnROKpNLXHDGjbaoyd7HtehnKXxGoPCy9AuBQMZz7ju5JY27jaPdbTnhGK1ItGoQn3hY3gF-BcARqIgWO1BKrZamQp21jXEWJHRVMlCJ8qBcfLCJ5iiWurc9qVb007gn3CyzGGbvXeKNFg1Xqu7BbDlz_H9b98QsDrY0l7EV3HxyPm8upsJs---AIhZvuFI_tlS7wM0J1ctqynjGFXwX8mvLMyfmc-wBkKBLWvmh1Pe1dpZsZsXEPAU_RyMZRUqxKocLvWK-XuU7Q__welAcsw1cQxmDS0oqFPBQmh5r672GNkgr2MCqAW09D1zBYhbOKwlL93cgQPJbOKpRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپرگل دیدنی و کاشته هندرسون بازیکن چلسی مقابل بورنموث
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/Futball180TV/108273" target="_blank">📅 19:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108272">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b95f1bafa.mp4?token=iKaeT05mKPzXyMrPxx4WL21figOt8e5UMejwJBA9QifyUdJa_7bANpcG4J208Rexoe3XpWmvksxdm7vPWtuvzhe1IbsZDeVgHrrQcs9jJdW0TAu9WEY1snEMqVXpEkXpBvVKhcbeQNfaOuaXEDhiJ8RUFsGaDJFOvlI3vASZ56Hy4lwxBR58OIGxQBWS935c6kGd8_T0ggj3KD5mtMsVmGfyWD2jbudhzQvfyNoasWHOvClwDOE09ZPUdy3l0SMEKdBNK1kGy7V48-es8L8ATVzF_DL_fw8RXlezraU-csavXrQ_CvYhZULukUFZ3Zo8Cw6B_VZp_FrfP3F3_LFYSiFsN0oUQXREpvnTmQLyNQnnNSvktzLWfbLDIxxZ8KzVA3Iqm2u78_aEvjhb390ENl5hzS6TZUyCazVfT2uZz0nekFBXsKbEwQRwQpNXPmLwVqQacJb7xjcudcx5lSXcCbO1f-iCABoKmmU0agHrqCjDDROuogvGGsx_EMCs2Im6fi0IHk-_GL82HFt6bJxgaLgdxD3z6moJgN4vFUBR0GXBVXrThab3HUu4bZF0Sv_ArBU84Y9fdmy5PQ3X7tW-nbus42WsErls0dNXeG1sTVDvT1JJSeHIWyGwqaXX_PzBuQJS2UKHQ9N-kg-35c3y-1ivm6GDzzGIekfSMd_jywY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b95f1bafa.mp4?token=iKaeT05mKPzXyMrPxx4WL21figOt8e5UMejwJBA9QifyUdJa_7bANpcG4J208Rexoe3XpWmvksxdm7vPWtuvzhe1IbsZDeVgHrrQcs9jJdW0TAu9WEY1snEMqVXpEkXpBvVKhcbeQNfaOuaXEDhiJ8RUFsGaDJFOvlI3vASZ56Hy4lwxBR58OIGxQBWS935c6kGd8_T0ggj3KD5mtMsVmGfyWD2jbudhzQvfyNoasWHOvClwDOE09ZPUdy3l0SMEKdBNK1kGy7V48-es8L8ATVzF_DL_fw8RXlezraU-csavXrQ_CvYhZULukUFZ3Zo8Cw6B_VZp_FrfP3F3_LFYSiFsN0oUQXREpvnTmQLyNQnnNSvktzLWfbLDIxxZ8KzVA3Iqm2u78_aEvjhb390ENl5hzS6TZUyCazVfT2uZz0nekFBXsKbEwQRwQpNXPmLwVqQacJb7xjcudcx5lSXcCbO1f-iCABoKmmU0agHrqCjDDROuogvGGsx_EMCs2Im6fi0IHk-_GL82HFt6bJxgaLgdxD3z6moJgN4vFUBR0GXBVXrThab3HUu4bZF0Sv_ArBU84Y9fdmy5PQ3X7tW-nbus42WsErls0dNXeG1sTVDvT1JJSeHIWyGwqaXX_PzBuQJS2UKHQ9N-kg-35c3y-1ivm6GDzzGIekfSMd_jywY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گل های دیدار آگزبورگ دو - دو بایرن مونیخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/Futball180TV/108272" target="_blank">📅 19:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108271">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6MosIM3P0aXm-PVY-RrypSueB2ZaTjM7eLl87KgdzgkaKvNGON72bB1il3uWCN1De-5aI-7Dqvxn_z-OUO5dC7OmW3IcJ4r-LTFtRT1HK7qLJ-CUYzSWnaTapSD43dz_HfDvJdhI_PSfx-6nL-7zlev3qW88sRkJTv5alTqu0HG3NVF24-yVrx_WTnz3JRMa-vQ8icA67sOgQtsqdkfm5_L1XCkN9hMKhMri5hYc1rBiX0cHPEepoP16OEm5cDg4et_4H-yMVTPvrq62NzaRSvHVQ62OjDupwVieY9UHy51IecfRLsFnZFI1qlEbztAada5XASunT-nDigO-dDRqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
پایان بازی هفته پنجم بوندسلیگا
⚽️
بايرن مونیخ 2 - 2 آگزبورگ
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/Futball180TV/108271" target="_blank">📅 19:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108270">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7l8mb74pNRUwtXlpMkqVP4peCr2fUSi87STB6Muh4SMMnzOaxZTCvRcWwOysUwJGavaqlH8NGscMxwjHvlbt7yhaISRmL42ouO3ARgYoHXKoLJM5qNrxQfslAPJ-M8giAZKygQGeRRa-bsBaGNuQ_Z6Eagm8ebX54AKleFw1MccpDPNlL12XYB-EcMZKil0njWqyq18LgI5QKOVLQG5O9hB3VdOLWObGSiArXcgdpaPHqhgToqADXmUcIo-EvCkWCzuA3ILh3ayt0B9hTg83Ooi-RYHJHwNKh5HnW_ZuvYhDvSDn84ZD2QLi0jB2pvm3lM0-6VpZ71q5bX8ue2b-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب بارسلونا مقابل ختافه؛ ساعت ۲۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/Futball180TV/108270" target="_blank">📅 18:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108268">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eMhwff7fAMwk_8ozwIQJIKxUighm1ItN-63sCnDCE_nYc-6nZKycwSCPK-7Yd9N9Aw7QlCuJHynppNA_rCyNqcrOgVr6p5hbduXfOuXY50dS_rNChd3KIX-FkvbRYlLcAC-uaCjWmGiKZbqPp__1bRCP977WXK0NbEztmD7192DYtocpq-OQZZhirT9Oew1ydCZkiZfW1iOxUknFtPPH7dVM-XGCTILkP-T2fiiiceJw3gi43ZjcUxYyxMdYeG7pn424khqG5LvItz10m5FFjZYwjsW1TVmz5dU5xdBNAUiZSMjrf0hF9vq6cDRxHVR0GeaFuDQi5sWP9IWxMtU8Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N7CI9nX5iW7J_eMEPjtRUTTi7yKqragiK9qbCxFtDxDJsugYXmQc_yJAIgXWpEuFymWr52vuGsAp-OFQZyyOVUShKOTkDkHafL3TTmJ9GeljtbGFNVhLnC3j52ag8a6OZTqQ1zi7eEmZlqbXBug8cfyqs4tFXRCl3d6XkiMMcXMmTgjUiAhijuTYiZrhBCQpQjrpkRWz-6ktaLyecbE6QGasVK1j_8TB46ivTtbDI4-GXGfEOaq9fip6Fki-5nwJjAGVEaHFf5vVeAjL6IiMPZBRcCMePddF3lTw0yZGmQ0TC8qzdd_J8ago9so5ZrUSz8DZxWFYDyqwz32sqiGClw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب تاتنهام و منچستریونایتد؛
⏰
ساعت ۲۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/Futball180TV/108268" target="_blank">📅 18:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108267">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZOLAwclsfrYDKVdIy7aNeLU-HYupKpQyTVc-4M4IA26cbMGw4ZoEFSvdoXMR7zL-1zyXXy6aFxplAA8IxWrh8yai8UP3EK7eULVTQMY7kCpVvqc_qDjK14eupVKYMqOHQB8hOy-sm8h_pyXAGKONQc0qGAgZ8OdsgHO-gKbrAKcrZEuqhnvNx1U8sLheWVrr0l5AyUDLm4-zHCew1yyv6-3e8E16G5OIWS8lyeq7Gaq0YIOR4eVR2PlpLtvYu6Bv0kXPeuloC25LP2yF2jEXsf8OfWaVg-eL4U4cJTjuNfji1xnP4OH8mkSld3TCBVAc2W3NjA1Cyrq41BhZP_kEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب بارسلونا مقابل ختافه؛ ساعت ۲۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/Futball180TV/108267" target="_blank">📅 18:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108266">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1wJD6mIK8QhXpbGktpStxQb-hKDUbWY1kOU_fw-VDXO7o6_3LPnyGRjs7tDfaftBZUi2A97pe4cwKL2P7mkUmP2yIn9gJvmBui13dbHFXUzEV13ilXBEp_Dgysq3s_jb33fwC3NZ8rTesS_rWOZ_hCS8oe2Xq-n6p_YW2-OUNhR40bS0lBQJdvdpN-jUM7H2TjWXiDKyr9RHlC7sMi3gZoG18ItxOAgsEi9jO7f9bYU7kiWjvsAWubniBm4EnKXiZA4WXhGcC979ONyuUEEPdyDyzOM-qgT-e0n6bhyN8mxGg-NdXjjgIk_zn9cMf23zsBKzwnGxJ6f6QQwKq8A1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
‼️
با تصمیم محمدرضا زنوزی، علیرضا بیرانوند تا اطلاع ثانوی و پیش از سربازی خود در هتل تیم امید تراکتور مستقر خواهد شد و حق حضور در کنار تیم اصلی را نخواهد داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/Futball180TV/108266" target="_blank">📅 18:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108265">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33630db290.mp4?token=fshvZMTALHSF-76J7OtDv3a5KrYVgUw-Ccotj1wI6rBaEezzroPsgJen5QZQ8qS447vRSBXXWmhYHD2XSOzn0k3YHWGzn9Jd7p8RNvdgck5jnyj1rXFXb8pxW9qsEUbE8RkOUv9G2-PIm-1TEwDdwYrtk0p6FjvIrJhCpcVfy04cMupBdhndrkuG9OdXJp35OT0jFZX0nomlVqZoJ-M51T_fyWTyTg5eARywyU4Ohn18tprz7zmwCe6PORWO0R-sJcs8w9UpvtoDMZI5qflahCa4aZ05JRlLNXLUomFk0MM1prK72ZT6j22XwSo5szpyyKJTlZieJfROcEZAE6a0aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33630db290.mp4?token=fshvZMTALHSF-76J7OtDv3a5KrYVgUw-Ccotj1wI6rBaEezzroPsgJen5QZQ8qS447vRSBXXWmhYHD2XSOzn0k3YHWGzn9Jd7p8RNvdgck5jnyj1rXFXb8pxW9qsEUbE8RkOUv9G2-PIm-1TEwDdwYrtk0p6FjvIrJhCpcVfy04cMupBdhndrkuG9OdXJp35OT0jFZX0nomlVqZoJ-M51T_fyWTyTg5eARywyU4Ohn18tprz7zmwCe6PORWO0R-sJcs8w9UpvtoDMZI5qflahCa4aZ05JRlLNXLUomFk0MM1prK72ZT6j22XwSo5szpyyKJTlZieJfROcEZAE6a0aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🇮🇷
سیلی ساکت‌الهامی سرمربی پیکان به بازیکن تیمش پس از سوت پایان نیمه‌اول با شمس‌آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/108265" target="_blank">📅 18:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108264">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRL0CAsmq6uZWmH419_zPJDbO3B8H69SycZsHglyqNXOLqqr7c-8D8KHaJyFgFVifw3iExrndG2eh0owPj6dFbnkGmTK_aSvpcj6m-LXM2wjrZU053D55iCCpJ9i2WDM_0xaNWWq5jaS2RqkmJ1aLZV6_bGr9TomNUZhHLuAQ5eoRYhK4EWxy0Y_4Ff-Ti4nq_8PGULkB9KNwQLl67RN5-28puDqAnBpxN4RHOq5PShkIaSGsglY4vv80dfE6vuV9iNsM5dyYBxKq8xsQqOdHEh9EVLANO_a3UgMsDY0943i1iYoLDnStgxOFVNemjxMYYNPBgB-2jP96u72lNgYtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی های بارسا و رئال تا قبل الکلاسیکو
⚽️
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/108264" target="_blank">📅 18:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108263">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/974d9df6d8.mp4?token=BgLsGoTtw5fA-eb3gK_tNROdw6dptWlCjmsEhmr6Lw3LxMnIqChX51a-BFQYsgYkGzwchNL9MG3yVh66LhfXEcxM3N-r4_bmVyT8ZFIh_FSCcAQj7EF97Ohv2rGwlMWieZzHcaDz0-Rn7-S0a-n9ob3IvgpbteQilf5ZmUqlXk_zWB54ptRUlBX9eEkZBbYXg1-z4bbm6NWqpBTyKn4ImqbEkzBaEdJ30xesCQSOpav2Qm8HQZSzAacYaffqtCCK1U1RKGpyVXUF0Wx10phuPxXz0QAkygFfVidil7Z8ALeYZYVt30HfSATra2SS7de869B5NEyST9Oa81fmx3B6Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/974d9df6d8.mp4?token=BgLsGoTtw5fA-eb3gK_tNROdw6dptWlCjmsEhmr6Lw3LxMnIqChX51a-BFQYsgYkGzwchNL9MG3yVh66LhfXEcxM3N-r4_bmVyT8ZFIh_FSCcAQj7EF97Ohv2rGwlMWieZzHcaDz0-Rn7-S0a-n9ob3IvgpbteQilf5ZmUqlXk_zWB54ptRUlBX9eEkZBbYXg1-z4bbm6NWqpBTyKn4ImqbEkzBaEdJ30xesCQSOpav2Qm8HQZSzAacYaffqtCCK1U1RKGpyVXUF0Wx10phuPxXz0QAkygFfVidil7Z8ALeYZYVt30HfSATra2SS7de869B5NEyST9Oa81fmx3B6Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
یامال نسخه ایرانی هم خوب داف میزنه زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/108263" target="_blank">📅 17:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108262">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/108262" target="_blank">📅 17:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108261">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kk6E4WPd0K0YiYC7iK8Y9EgXYJvQ8T8jwEyU2_90t85xv_4-zUofyhZanYnvddG-mF-3oYuFAxOC0J4N56j3EI24PPEkG1QX5Ubd_EItkGnbY4nXHWXiRAqvCVHqckA5jlbi4QlmQ0wdO65CRcrTA6AYzGQEsuE-TUL0lrzaXS-WYfgIgpt4lVihf_uvTkHDuH17aDTR-V0QvAEjCLfv-dmA3GoChIG1gmoBXm0hvqLV5Wm6rgUtEI0_RedG2hOVkIKGpXOOB6yRSAcp8GyjD0FibNbbBBJ5L1KLGPb4ptZxKEvN2BpPT9pOSOSNeFioRuGRviTqEbuuxKrl1Iv8Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز ویارئال
🆚
رئال مادرید رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم در ۵ رویارویی اخیر:
ویارئال: ۲ برد، ۳ شکست و ۱۱ گل زده
رئال مادرید: ۳ برد، ۲ شکست و ۱۰ گل زده
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
https://TrexBet.com</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/108261" target="_blank">📅 17:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108260">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d61d77833.mp4?token=P-wAm1G0oDc1Mg3t_5hEC8IbAsIas_N1UtevJn4ybkpStt_8pLBsHULLk9gqVLlf9OH3iFgqWq3bkZrr0xM0Rz0BLKZgGNXZvWFWgiIAskm5fn-7-phbx6aLBkqYvcsBO_ZNrs9LtPKiJ9TMIxT_cCvpyZxtXk0wUHdxBZxDgp6MSIj9y0HbrxsgmMxOJR9Ix-HpX0eHjLTM7s1YTE76diZf5XMPmZ20fFJ5A5zqskxNN-ojsJoeO6xDQVoRyhPKIni3aPQiAgmN9zPC6bekXHFaMxXyQAW_zASCdBQEQSCSOmTOeYIJu6NavorghPgsPC7VNrQtS-PP1BCAt55IUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d61d77833.mp4?token=P-wAm1G0oDc1Mg3t_5hEC8IbAsIas_N1UtevJn4ybkpStt_8pLBsHULLk9gqVLlf9OH3iFgqWq3bkZrr0xM0Rz0BLKZgGNXZvWFWgiIAskm5fn-7-phbx6aLBkqYvcsBO_ZNrs9LtPKiJ9TMIxT_cCvpyZxtXk0wUHdxBZxDgp6MSIj9y0HbrxsgmMxOJR9Ix-HpX0eHjLTM7s1YTE76diZf5XMPmZ20fFJ5A5zqskxNN-ojsJoeO6xDQVoRyhPKIni3aPQiAgmN9zPC6bekXHFaMxXyQAW_zASCdBQEQSCSOmTOeYIJu6NavorghPgsPC7VNrQtS-PP1BCAt55IUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
بخشی از دادگاه انقلابی امیرعباس هویدا که وایرال شده است :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/108260" target="_blank">📅 17:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108259">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6680dee71.mp4?token=DYyll4lmE5U1jtkN-IpFKXmAyHh_sG9R7_1t2m6JruUFzC23IQe4x9FxaeeQHJFxBPkS1jYQQQWqXwplR7jYIg82_VDpT7yAbSy0UU4eWa7zMEvqw1W2yRBCjcbk4QUK8C8z3w1diCJsz0eBwR_Y1b9smAwDNFwOj5tHUu8cNDDTV4g9mesGHDwlNG1QeKN3Z8XYyFQODz_M5gUcny22ysBLZhvoJdXIWW02CqKFHqRY2R4C0ZSJczyQuglN2tM-cRLXpSj1KTSCOx6_JEDrTD3bjPaKdbBq39ctdScsTm9Sv2KC7AiJ6ZAsv5KmFObVxMMipb4-a8UfLtI_b2Pz6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6680dee71.mp4?token=DYyll4lmE5U1jtkN-IpFKXmAyHh_sG9R7_1t2m6JruUFzC23IQe4x9FxaeeQHJFxBPkS1jYQQQWqXwplR7jYIg82_VDpT7yAbSy0UU4eWa7zMEvqw1W2yRBCjcbk4QUK8C8z3w1diCJsz0eBwR_Y1b9smAwDNFwOj5tHUu8cNDDTV4g9mesGHDwlNG1QeKN3Z8XYyFQODz_M5gUcny22ysBLZhvoJdXIWW02CqKFHqRY2R4C0ZSJczyQuglN2tM-cRLXpSj1KTSCOx6_JEDrTD3bjPaKdbBq39ctdScsTm9Sv2KC7AiJ6ZAsv5KmFObVxMMipb4-a8UfLtI_b2Pz6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشتباه عجیب مانوئل نویر؛
گل آگزبورگ به بایرن مونیخ در ثانیه 5 بازی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/108259" target="_blank">📅 17:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108258">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‼️
⚠️
‼️
‼️
⚠️
میرسلیم: مردم باید بنزین را لیتری ۲۵ هزار تومان بخرند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/108258" target="_blank">📅 17:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108257">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bead49b429.mp4?token=JQHp6bKwu5BOvxUm7gAQHaX4askgF7tHM5-_2yR94ISkQvE7u-xI_Xaj2cp1hHWaHwRJhmwztAsQjg_Zi7RjT-hi-GBAQNXlEfoUPYQ5OBAiPuycpgLd9efjo9RHwevPcby25ptK6ZVnk80pWhK5Z1lGDLkdVkUUep3tXkWRweUzC6ykrMJAepElGBFOCnJZNc7n9jZwG1DuJTBh4BE8xbTo1ZrigZDa_pVIFv6YVBOHVnN87m97aKrNcOR6JYUX-_kKK7xbRGqZuCmGvGTVthx64MFxf-dg_avzuzIq9gapSBGEpxS8ObWAXenBwM3dZIsqSc6zJo0I9r68koi_rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bead49b429.mp4?token=JQHp6bKwu5BOvxUm7gAQHaX4askgF7tHM5-_2yR94ISkQvE7u-xI_Xaj2cp1hHWaHwRJhmwztAsQjg_Zi7RjT-hi-GBAQNXlEfoUPYQ5OBAiPuycpgLd9efjo9RHwevPcby25ptK6ZVnk80pWhK5Z1lGDLkdVkUUep3tXkWRweUzC6ykrMJAepElGBFOCnJZNc7n9jZwG1DuJTBh4BE8xbTo1ZrigZDa_pVIFv6YVBOHVnN87m97aKrNcOR6JYUX-_kKK7xbRGqZuCmGvGTVthx64MFxf-dg_avzuzIq9gapSBGEpxS8ObWAXenBwM3dZIsqSc6zJo0I9r68koi_rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
امیرحسین صادقی پیشکسوت استقلال: علیرضا بیرانوند به استقلال برود، من دیگر هوادار این باشگاه نخواهم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/108257" target="_blank">📅 16:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108256">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpCkc9nowBirfgICw8AQsgFkGSFaF1LyPDGc6suoIdEkQIt6EzEN-5pFfKQAGokTAifSyAimDiKydwWeSAxZTn_n8cloWnv-3KdlDZXw9CAzc8aOfyt-LgoZzDQThfm7WUP-z76terbtkmUpg9yg4iObTpHnNHIF8Lqj9VEcIcl4qtZm0WTUmjkdiT6o2N-5SceSLiVCEkHtYaRNBjgm-JrfWDrMSDwSx1wZN8nf9PWPn309OBa3j45rHY8DS0m-CTRK5aEF0FwmvawVn_BM6FEAMpYrz3idoK30m1N0YdFu8fES68GSl_-2gp3mSYA6gcFM1V4XTGuN_uBk1G5wMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل دوم آرسنال به لیدز توسط برونو گیمارش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/108256" target="_blank">📅 16:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108255">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYU7rr0EPKTuI2jRUQP1MVw6DOxOZe8Z3_KUWZq00ns540leES7fAp7-RzIW8GIyAXVJej05OikcUAydhxrumnb5VgvM8RTn5DtWo9WvQ3dkJDAK2a3Cexv-V4VrViUTw9htHJRqmLiP6zAEMMfQ01kXXtCoNS4iCbIUd7IdOoC3iTHrDIkCwdNd-G3FWSzmetEC8p27a-RFN1ImpFlt5bo40xWHvlLndXQO-EX02U0RKdH53Zk-ZBGDEWSY1x1EVfo9xsAua-4uSQESoIS--zyKmOXwLK0L-WbXKhYEEC-R50q0l3a2kcrgLNgOlxXWb1dt7vtEfS_fxx6dHOUWxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇮🇷
کاروان استقلال لحظاتی‌پیش با پروازی مستقیم از تهران راهی دوحه شد. مدیران آبی‌ها در ساعات گذشته توانستند محاصره هوایی ایران را موقتا دور زده و مجوز مستقیم حضور در دوحه رو کسب کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/108255" target="_blank">📅 16:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108254">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64417ab8f.mp4?token=abdd_Nwg1aIYjD9t4N1akB-5aNDSIhkkqyiVuzWzNCQLjrxsRRR3tmUJZZb0MIO6dg-_1kxiJBEYVB5oL0jTaZpmc69UmAWN0p_aMolXoxOocYlfnZ1_FG6N9e2qd8F1LGhmeYXbuIMYv54NkAcpG36fV8pymdSjq-TMc5RwaK7QI5oMy31XVAbUPe4eiyaqa4ENIES3nv-vnGxl-W2hZTvvb0lwzn6mabZrh-tbl1E_quBWt-blTjSk7rKC0mZyLD9yIJyOg02Prj7Ee848r9PnCu_j6_fC6ly0bhJACkjwE-98NM-PGWj-Ncuj6IphiK-BEbAyAS3oh3VRC3K3aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64417ab8f.mp4?token=abdd_Nwg1aIYjD9t4N1akB-5aNDSIhkkqyiVuzWzNCQLjrxsRRR3tmUJZZb0MIO6dg-_1kxiJBEYVB5oL0jTaZpmc69UmAWN0p_aMolXoxOocYlfnZ1_FG6N9e2qd8F1LGhmeYXbuIMYv54NkAcpG36fV8pymdSjq-TMc5RwaK7QI5oMy31XVAbUPe4eiyaqa4ENIES3nv-vnGxl-W2hZTvvb0lwzn6mabZrh-tbl1E_quBWt-blTjSk7rKC0mZyLD9yIJyOg02Prj7Ee848r9PnCu_j6_fC6ly0bhJACkjwE-98NM-PGWj-Ncuj6IphiK-BEbAyAS3oh3VRC3K3aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل دوم آرسنال به لیدز توسط برونو گیمارش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/108254" target="_blank">📅 16:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108253">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb6a1e8ef.mp4?token=cgLmpasjGZXz6sijBsvckUzE_zzBXZlgmn7t08NCSY1glh8d3lQuyD40Kv2eCceUkvI2305pZiP5FYEqvNLggxNXhnmDMVahbRXHP-Tarnvt-BpDaNGChodwfkT9irtP1IlSbaZwdqSd9IuRuRxxb2tVLK5mM6Bra8TY7fwNCnsmPe902gXY8t9t7zeJ3K7cDt6cYNA2x6dH9zeIxsmNKYj42w-hLT0q96Au_wKzR3lmSm8xjxIoxxvQpxgXPezRpbpN-QLId7RILdV11QLkxEDHosb4q0jxrd3geTSYYO8cdYhxZj7qPS34WxI7BhrfaaGrTaHKi9cJfeqVyJwY-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb6a1e8ef.mp4?token=cgLmpasjGZXz6sijBsvckUzE_zzBXZlgmn7t08NCSY1glh8d3lQuyD40Kv2eCceUkvI2305pZiP5FYEqvNLggxNXhnmDMVahbRXHP-Tarnvt-BpDaNGChodwfkT9irtP1IlSbaZwdqSd9IuRuRxxb2tVLK5mM6Bra8TY7fwNCnsmPe902gXY8t9t7zeJ3K7cDt6cYNA2x6dH9zeIxsmNKYj42w-hLT0q96Au_wKzR3lmSm8xjxIoxxvQpxgXPezRpbpN-QLId7RILdV11QLkxEDHosb4q0jxrd3geTSYYO8cdYhxZj7qPS34WxI7BhrfaaGrTaHKi9cJfeqVyJwY-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول آرسنال به لیدز یونایتد توسط کالافیوری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/108253" target="_blank">📅 16:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108252">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13447d981f.mp4?token=OsjYncW09tVi5hTgDQqjTi57OSIYZqoNgZ48V13E6Vaws8mANLF7ha4Rw-Cd8aA6VcCCheGrJWV2D1bD9vjVF4sPeApQm23XNL145TRNtceuZ8wzJmTp71Yq9FT2KArO-i_erBlQvGlMreVkBSg57Xd8PbL0_HriwUQ0iyH75PVNZObOMzmj3Px76pM_67Cw9mD-TAFuZFxtC97ct4v9O2m6cq_dj_SICRFgM41gD6cYbp2JiiT7WhLceqqHbNvrxdJqr2DrOJwyAa8khXsYuu99vWuAta4dsiVZ8HBHzMHotuopnEuLjGupNWWQ2QdP_zazVjejWSTlVCOGl_5eEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13447d981f.mp4?token=OsjYncW09tVi5hTgDQqjTi57OSIYZqoNgZ48V13E6Vaws8mANLF7ha4Rw-Cd8aA6VcCCheGrJWV2D1bD9vjVF4sPeApQm23XNL145TRNtceuZ8wzJmTp71Yq9FT2KArO-i_erBlQvGlMreVkBSg57Xd8PbL0_HriwUQ0iyH75PVNZObOMzmj3Px76pM_67Cw9mD-TAFuZFxtC97ct4v9O2m6cq_dj_SICRFgM41gD6cYbp2JiiT7WhLceqqHbNvrxdJqr2DrOJwyAa8khXsYuu99vWuAta4dsiVZ8HBHzMHotuopnEuLjGupNWWQ2QdP_zazVjejWSTlVCOGl_5eEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول لیدزیونایتد یونایتد به آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/108252" target="_blank">📅 16:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108251">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYVpmeYv1gjQUShnpsYMHnn1bgq_lnOV6I6JitP4xkRRWbTngowsz7qbRz87WDaeeLdpMSW_IKLrgLDoUwSf0L5Gcn3fGklTNsfH9FidQS34fzo1s-RoxSMmH-fqkPFLD9BB4YbmnrKFWjUt0odmHs_1VXuAyToJjxSQJThIQeKJ1cmMK_lZGi7JGQ440xwuSBPBxza9DOhEEciEXskU5_eHL6mtb--XheILMN0ST6SpQcrjwGLiqjqaq9D3q9v8mOM_JtmelMfiXjUYOUY-hpN5_7dSMPhl-X37IU0TpL8ZBvgYVXa7C9C4iinB_MItFP_8M5mzEh_e0wIqUsY3SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
در فاصله دو روز مانده به بازی استقلال و الغرافه قطر، هواداران پرسپولیس درحال کامنت گذاری زیر پیج این تیم قطری درباره یاسر‌آسانی هستند. این درحالیست که آسانی بدلیل مصدومیت مقابل الغرافه به میدان نخواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/108251" target="_blank">📅 16:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108250">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5lTCisoILdU4sSbpn3qGXR0wcisKc7ObhVDlDQ_Mnh5ccx0zBzBmPOY3pcI-vDbEGt3FrL_YKlfCDCyubkTWpETME48tGk-2ShbOQ2KnN231ur_srYTR7P1J-N5ICKe2UqsdvRZJ8hGz5d0OCOxd_gAE88alnLqy5DR9xtislfD-hziAQjW8Z3OHVPvTgisOor8HtYA-Vh79e57apeLkBkIhIUThJVDY9g2KzFyI3-CafU-f4UQxVEFnlWtlQeur0CpxTzL97IZcorIO6y6bRUD9FNOEYTtf1iKpH5Q31XwxImhUKkI3IGXKGLGybCGbAM7I4yU9aGQSxYXLYsd5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇩🇪
شماتیک ترکیب بایرن‌مونیخ مقابل آکزبورگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/108250" target="_blank">📅 16:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108249">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85108132e1.mp4?token=EOsViv1oDj39Dw4WEnuGUQKoHdAzMGPt94N2ZRM6V8hIKShqYraqlXBRMpCycUCO3ec2k0CtaE2y8v8sM8IEnuZwXvdtxmrgC5K4vPy-WKdN-OJTYnOyDTm-5jAVeKU52kyyUlFG33sXfmTiiqTwHjzrDPi2x6UQeRpg-7Jz-wWoQFIe_MbFcxECylY8X2IJbq9PgPmOK3EQ6_H0sI6K3xA-zrZXF_pBuFISSTp0C9wypx_wM_X5lKNcANhBU-fvWyXMWJ8kLeSByV3G09x9kn_W2v9Kxpi05rCxh3Wz8TP40A-h6jYtDJ5FJti8e0BIW6kXovHkjltV0aya_FmkMGxiRqdCObvHKRhYOlqQycoJASBCHYqiaco8VeiIfDMlqNBKkxu4jLvFlRg3k0MP8YrSh4PDBW5735nxgGncr08VQ-T-32RLTurCXOEP-C73wgQFDZa2_VObhx5V0TuGFNOgyfxHo8sAMWD4UJXBcZsf4fMzfKKr4CLwrmlZBSO7SOJWVp9sP6jR-oGpjjrImh8R-aCAV4tElQcvs68KN9snP9VTiSZg1NI-1g01jK5VCgc9_oXO2AhlB1xY05m3LdolvF1soyBccgQnDHODJcRytGhoA50ngx2HKVYu6ICimD4gXmrwgwCQUd_aWs3IV1X19fcW8XgyYr0-qg3jhAo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85108132e1.mp4?token=EOsViv1oDj39Dw4WEnuGUQKoHdAzMGPt94N2ZRM6V8hIKShqYraqlXBRMpCycUCO3ec2k0CtaE2y8v8sM8IEnuZwXvdtxmrgC5K4vPy-WKdN-OJTYnOyDTm-5jAVeKU52kyyUlFG33sXfmTiiqTwHjzrDPi2x6UQeRpg-7Jz-wWoQFIe_MbFcxECylY8X2IJbq9PgPmOK3EQ6_H0sI6K3xA-zrZXF_pBuFISSTp0C9wypx_wM_X5lKNcANhBU-fvWyXMWJ8kLeSByV3G09x9kn_W2v9Kxpi05rCxh3Wz8TP40A-h6jYtDJ5FJti8e0BIW6kXovHkjltV0aya_FmkMGxiRqdCObvHKRhYOlqQycoJASBCHYqiaco8VeiIfDMlqNBKkxu4jLvFlRg3k0MP8YrSh4PDBW5735nxgGncr08VQ-T-32RLTurCXOEP-C73wgQFDZa2_VObhx5V0TuGFNOgyfxHo8sAMWD4UJXBcZsf4fMzfKKr4CLwrmlZBSO7SOJWVp9sP6jR-oGpjjrImh8R-aCAV4tElQcvs68KN9snP9VTiSZg1NI-1g01jK5VCgc9_oXO2AhlB1xY05m3LdolvF1soyBccgQnDHODJcRytGhoA50ngx2HKVYu6ICimD4gXmrwgwCQUd_aWs3IV1X19fcW8XgyYr0-qg3jhAo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
ماجرای خرید تراکتور توسط زنوزی به زبان نماینده مجلس سابق(عای هیمتی)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/108249" target="_blank">📅 16:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108248">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yg1hE2XiHD3SNcUT_6702q7cymjxmwRvpGOvDpr0UYExxehQrKz5OYSYBmzTUJ_LI-WpciUjK8_PoDus7v7gBrAfVsyP4yQRdZsOMpXcvPX4fXh56xjhgyWzgvHLXwWB7Ew7Ii7H2XMw4tdSDqNDhgjw0KKePiypr_eiko5fFusavMelmPY1MRhy-3Y-Zc6iRuA7nyj7QlnfHwznPLvhKLEftQ2EQ0oijkphPbQV7aCEcPJlb-eev9r0Wee4YMnNEQi_fs-79lvX72AuRlmByPcCl6OIGub1CZ4VOBmMsBGahvk67MCkj-P_Jtg38CZr9p_rSBp7giKmtO4aQU__og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
😳
مصطفی میرسلیم، عضو کسخل مجمع تشخیص مصلحت نظام: تیبا با خودروهای خارجی قابلیت رقابت دارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/108248" target="_blank">📅 15:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108247">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d024a83d11.mp4?token=XkseNjrgGEGt7yCz2ZYemwYthbYvnK9f8nR--IQirY786aDPcZV7zz6U6A8yxPk37b0qCC_adcbSbkz9vww0kBy2vcgATsKF1V-tPDk-nCGqJ7cQM_iAcw78JwG8uLf2aLA8DcYWDwBjQKix29RQfyLzejph03fhy_DfTlwbNAmVY_4e7BEqXTtM2EP3Bxef1nOx4s-4scLBT5b2uPlqzabWoTBpjyg7nNV0dCpVqm3G89Hyvuv3Y8ABdlM813ApCz73ycdwnC7na7XvO9TgmMFnRJ_YRmY8h5J7Xey2xCtvQ7evd4fkxfb61hYq1D-0ivS35FjOFfjlJDoJvt0EspOdkXYsCgijnr9nygtE4wjTg3am6vsmRLfclKRrtCAHuihbuouRP7x9kaudmr6ZirMmKs2YA0A-YaZjGJZp0IoWsvDy0RFrBpbpoy5BctnRsKBjK64P0hiCYy0HjNZeNXq3BskLwJPxHfpYsnrmbnLrNzZCR2k0Pl7zFYvPifHfraTFGGrlPGFDYeakfTFYbjTDEsTEeOLSpeZW_8veggGTuf9L5HZt5mw99svu2ADQhAcEluAI0Cm7n6zJ9l0UhdXGQu_62mLu9z5DtBeq8uhNr4XeoJzBJd7pVjgCnAg4Fe9dsXJBCuYpbqIxGpRupwWpg9o0AG7GvJ16vZjCpgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d024a83d11.mp4?token=XkseNjrgGEGt7yCz2ZYemwYthbYvnK9f8nR--IQirY786aDPcZV7zz6U6A8yxPk37b0qCC_adcbSbkz9vww0kBy2vcgATsKF1V-tPDk-nCGqJ7cQM_iAcw78JwG8uLf2aLA8DcYWDwBjQKix29RQfyLzejph03fhy_DfTlwbNAmVY_4e7BEqXTtM2EP3Bxef1nOx4s-4scLBT5b2uPlqzabWoTBpjyg7nNV0dCpVqm3G89Hyvuv3Y8ABdlM813ApCz73ycdwnC7na7XvO9TgmMFnRJ_YRmY8h5J7Xey2xCtvQ7evd4fkxfb61hYq1D-0ivS35FjOFfjlJDoJvt0EspOdkXYsCgijnr9nygtE4wjTg3am6vsmRLfclKRrtCAHuihbuouRP7x9kaudmr6ZirMmKs2YA0A-YaZjGJZp0IoWsvDy0RFrBpbpoy5BctnRsKBjK64P0hiCYy0HjNZeNXq3BskLwJPxHfpYsnrmbnLrNzZCR2k0Pl7zFYvPifHfraTFGGrlPGFDYeakfTFYbjTDEsTEeOLSpeZW_8veggGTuf9L5HZt5mw99svu2ADQhAcEluAI0Cm7n6zJ9l0UhdXGQu_62mLu9z5DtBeq8uhNr4XeoJzBJd7pVjgCnAg4Fe9dsXJBCuYpbqIxGpRupwWpg9o0AG7GvJ16vZjCpgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🚨
‼️
عزیزی در فرودگاه بغداد: فقط ۲ تا سگ دنبال مهدی شیری و اعضای تیم افتاده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/108247" target="_blank">📅 15:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108246">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1ba40b7cc.mp4?token=sOduAAGBsB94-jejbFQCxwMnQZReXNfOksSig1xrLCxK0_E_Z64sCsBHuP6uyRVFDf4rfBd71PpKyTXTBTa490y1nbo31lqt69k2Qnueg_sJGGMHFm_cSxULCo4DvoM81NXnbdiGRTe9_zqlsDzMMGR7gRuYuDQ9zBDR0P18XoBD3tQDf_k7Cgg87HuIFpEDk5LszGEbmGuArB1s_ussgEHFoLDuG_Zld4XeW5bYjmkFTEigUdz4_ZQbrPiqRN1mmNOlvCuaMC-l3XmWNReNzasjFnepq_O5bBhp3bdoAlMkAbc77vgGH68pWFZivJcedqnwX5YuE0Ho9yr2JR6gCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1ba40b7cc.mp4?token=sOduAAGBsB94-jejbFQCxwMnQZReXNfOksSig1xrLCxK0_E_Z64sCsBHuP6uyRVFDf4rfBd71PpKyTXTBTa490y1nbo31lqt69k2Qnueg_sJGGMHFm_cSxULCo4DvoM81NXnbdiGRTe9_zqlsDzMMGR7gRuYuDQ9zBDR0P18XoBD3tQDf_k7Cgg87HuIFpEDk5LszGEbmGuArB1s_ussgEHFoLDuG_Zld4XeW5bYjmkFTEigUdz4_ZQbrPiqRN1mmNOlvCuaMC-l3XmWNReNzasjFnepq_O5bBhp3bdoAlMkAbc77vgGH68pWFZivJcedqnwX5YuE0Ho9yr2JR6gCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد مدت‌ها فردوسی پور و میثاقی رودرو شدن
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/108246" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108245">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a5e7db4ee.mp4?token=K-zbQzXkdyCQozFreW3KdQImEgqABSqJmCJ8UpTjarllveX91I0UYgaJ8aYPCEuhXjXh4GqRR15FPMJl7CqJMNIxVoVS4ezXjR-AOlpjNMsCE8L8iRHNs29fs01YKknYfoooPnlb4x04EROBFN0LEeOdwnHFJZa1U645hPevKsH9pezF_1gnIOp0KOJEcB7xM6cS5QqHN-i07zoWU_qmyc2Yfab9UWEOqLiXWSDquN_pc4pIYZiWGurUUXD3I9yreA4yfC5-uA91fLfmZEEwMXfPaAhOnS_epQcYHHCfFO-O99FvWH60t6OYs-criqjHtT3WAnKYbTUdNuD0hDtRBSRpxJrKmXJXIL_Wjp5tJLBoIpvWr1o3WkFBm165eVs4iRPALbfpblMFhKB7_osnVPvGzWGELNw6Q3Uwy4Xs7WISrmV4z16JXJIAriQgAhM6IP0Ipbe6E1K4BcMcxp9HxX8XVr1m6jaOgbS3O2LB265LCU2DKmDIMlQeuqPHsewvsczeFGYdlJE3NUokJmh1jJQA4nZmx7jLqsU33P98n-RoPJrM_ufXdemE3_u1Ut4rQ49xNEw0Mpy_TCyoyn5yWOl6SQ85-xIMRrXKhY1IpVMQ1LcmV9p46bv9DgZxxikNGClDr6KijdOCKF1tOygVkH4WUH2pD86ybMr4iVXM7aE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a5e7db4ee.mp4?token=K-zbQzXkdyCQozFreW3KdQImEgqABSqJmCJ8UpTjarllveX91I0UYgaJ8aYPCEuhXjXh4GqRR15FPMJl7CqJMNIxVoVS4ezXjR-AOlpjNMsCE8L8iRHNs29fs01YKknYfoooPnlb4x04EROBFN0LEeOdwnHFJZa1U645hPevKsH9pezF_1gnIOp0KOJEcB7xM6cS5QqHN-i07zoWU_qmyc2Yfab9UWEOqLiXWSDquN_pc4pIYZiWGurUUXD3I9yreA4yfC5-uA91fLfmZEEwMXfPaAhOnS_epQcYHHCfFO-O99FvWH60t6OYs-criqjHtT3WAnKYbTUdNuD0hDtRBSRpxJrKmXJXIL_Wjp5tJLBoIpvWr1o3WkFBm165eVs4iRPALbfpblMFhKB7_osnVPvGzWGELNw6Q3Uwy4Xs7WISrmV4z16JXJIAriQgAhM6IP0Ipbe6E1K4BcMcxp9HxX8XVr1m6jaOgbS3O2LB265LCU2DKmDIMlQeuqPHsewvsczeFGYdlJE3NUokJmh1jJQA4nZmx7jLqsU33P98n-RoPJrM_ufXdemE3_u1Ut4rQ49xNEw0Mpy_TCyoyn5yWOl6SQ85-xIMRrXKhY1IpVMQ1LcmV9p46bv9DgZxxikNGClDr6KijdOCKF1tOygVkH4WUH2pD86ybMr4iVXM7aE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇷
آنالیز ساختار دفاعی استقلال در این‌فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/108245" target="_blank">📅 14:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108244">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bed940014.mp4?token=UlGpL8jN4KllYf-ta2qQKFnS_ii2GQNGDF-BiJtWW39fJ29ECqdBJmWc4zYx-eaNuaWDmaM9pziOx0k1bU75LoEZLo5qMv3FctqOCm2gThPy5Xzac4tPMFkAhjjDabCc6_l7VF0AP7hGlqysZomXIW-5r1AvkwEk2qAhExNVuEKNcN3BBmFbT_QrYbrUqUToeZW3C3_6DZJEPlR0eRgdafe9mnSdp4vz0QNuCkKSea5hnYmYTHTpwT_RzwMKSU40a6kUd5ZrGjrYou_HvwqdwSLe_BJxyIrvUGCn9EcH5RAkrw9zaftMuFuIUu1ShVEcWSeiU2RVWDGKL8ORHGHIm7CsmiNLXPfGm0VUpISe4XE96jnGdaRmTK1AMsntuxa7y8bpolmRet46nm3KegXp0b1uRhu5mrSXax8okrJZWPwlocjBZCwrH6qbQsmsV8WXRe86S7TMQABfSF-POgShwtyfcfDgMvqu161CdRT_AqsutegpQ24Chma2L3oodfjM1J8bcOGuCF5hucLW5FtzFjw891Qeu-rh6FAYfY52X7D4_FivOllON_CzIJsqubeIsr6mD_qsyBwtMzHvQVqVpwwaRfhcidPI77LLY3Ko3yeptrg-RzSa66Tuyt5IzARpTLkv72jNcSlM1lISO0PGXr1KuKc8req9g2SOmq992tI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bed940014.mp4?token=UlGpL8jN4KllYf-ta2qQKFnS_ii2GQNGDF-BiJtWW39fJ29ECqdBJmWc4zYx-eaNuaWDmaM9pziOx0k1bU75LoEZLo5qMv3FctqOCm2gThPy5Xzac4tPMFkAhjjDabCc6_l7VF0AP7hGlqysZomXIW-5r1AvkwEk2qAhExNVuEKNcN3BBmFbT_QrYbrUqUToeZW3C3_6DZJEPlR0eRgdafe9mnSdp4vz0QNuCkKSea5hnYmYTHTpwT_RzwMKSU40a6kUd5ZrGjrYou_HvwqdwSLe_BJxyIrvUGCn9EcH5RAkrw9zaftMuFuIUu1ShVEcWSeiU2RVWDGKL8ORHGHIm7CsmiNLXPfGm0VUpISe4XE96jnGdaRmTK1AMsntuxa7y8bpolmRet46nm3KegXp0b1uRhu5mrSXax8okrJZWPwlocjBZCwrH6qbQsmsV8WXRe86S7TMQABfSF-POgShwtyfcfDgMvqu161CdRT_AqsutegpQ24Chma2L3oodfjM1J8bcOGuCF5hucLW5FtzFjw891Qeu-rh6FAYfY52X7D4_FivOllON_CzIJsqubeIsr6mD_qsyBwtMzHvQVqVpwwaRfhcidPI77LLY3Ko3yeptrg-RzSa66Tuyt5IzARpTLkv72jNcSlM1lISO0PGXr1KuKc8req9g2SOmq992tI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🇮🇷
على تاجرنيا رئیس هیئت‌مدیره استقلال: از فحاشى هواداران به مادرم خيلى ناراحتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108244" target="_blank">📅 14:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108243">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879a0a76f5.mp4?token=Ef_4vxtK_t77cRPGc70ahM6QW_fHy8FXerIozjpCxq1gZbAo-SUmMGQ5Vgre5NumgYck2-EVE2XGYuRegssbUyYor03-7pRW21orN2w8MjIgFbLF8bMqqkkVwWttBqfznv3eae1oVzAh5pHzEZYUGFN3C8mrLAyFLPIkRPYqEnH-lznd6vH8VVYG8Ozu0ZRcemSUjbcZcHhwJgqNTA7JRcgvTYzznVvWdTT-_GW9HHb2BtjjJswQI72z-IvBgqXTjIfCyidQsZXg4OPj1DGlJ_GTF5oklccLhc3TWWACx_-Kdj1U5I3rFwsJYQPlN1I8lCQYGFPSmx0SvJH9D1o5Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879a0a76f5.mp4?token=Ef_4vxtK_t77cRPGc70ahM6QW_fHy8FXerIozjpCxq1gZbAo-SUmMGQ5Vgre5NumgYck2-EVE2XGYuRegssbUyYor03-7pRW21orN2w8MjIgFbLF8bMqqkkVwWttBqfznv3eae1oVzAh5pHzEZYUGFN3C8mrLAyFLPIkRPYqEnH-lznd6vH8VVYG8Ozu0ZRcemSUjbcZcHhwJgqNTA7JRcgvTYzznVvWdTT-_GW9HHb2BtjjJswQI72z-IvBgqXTjIfCyidQsZXg4OPj1DGlJ_GTF5oklccLhc3TWWACx_-Kdj1U5I3rFwsJYQPlN1I8lCQYGFPSmx0SvJH9D1o5Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادر چالش را پر قدرت ادامه می‌دهد
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108243" target="_blank">📅 14:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108242">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_wa1-6sLqhecWP60HgU2STdpcg7BUQ_lfXtpcJiyzEYLoDGy61yAvzjXrv0JXeyjDIlG5-jpPXLpdHaCrQWB8K37DRZY-xXZh1qYnl8s-HapbYmA7p_-9YgxCN4P7p75GygJAFodYUIBeI4afccd8mvZn0xih139nEj4cyVR1-fiBp3VZCWSbZiDEKW5XQiQSwi1L8W09SPWrEPRgzf9jZG-YtqQL1b61R8HldWDHml7lEi8ZEXUJnYcGMJ23B9Zw137D-Hl24ORSzeZYGvFM3MWQENBUab5fh6mWGkiah3JkOV_2U05QOTpG8Yy3neMeJ5LY-AWCuyFvOno60Iqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
لیست بارسلونا برای بازی با ختافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/108242" target="_blank">📅 13:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108241">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgU__yV3Aeyx0pmjERFpvqEcyJu9wsmRTebnW9Tp3jo4-wrnq3LmZL0uAHndQVx8a7TaQKQDm9iD5kIj-9qkZ47bcz3GF1Z0bh5oSQw8ACsGVdfQCZAqPrLZ45cccbbcbtPus6MSo4zCA688re_kn7Wtpagi0Di_80ZtoZKMP5sKUAfcMd7eELiote5adPHeyFo5AmwOVwQQ-cwn5uTcRTq6kMJ6ymnlaw-QdLSciN6e_EyYJon7ACIXycmgcg4JAKgUz9E8ZEM5a3bujPpeWmrMK_nIn_bFCjPYTnpLCUDDShV919XHXLWMVoNU8zc2PWftqcy5YPyIkkO3uPISug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب آرسنال برای بازی مقابل لیدز؛ ساعت ۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/108241" target="_blank">📅 13:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108240">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kM5VkCswOz3TQqZ-jEzqaPf4fV9dYYpAO_jq_wBGf-O7qd-IBmEbRimFlessvAx3lAUdzc_J6MUJFKI71nw4gjWU0JlJtnAdFjpIIVTA5sSZ9NJTDykQ5-SGptTsZHxPxFHNXfJgmhMOVQKZtBDexQOGEs5ZCkwn8vFtRJYbg5sGuD6Si-cRwL04ApEQL-6vk2OWPxA7EYUpNSVAKKyK0KMJaHqdnejqZRlgEPy1DgAOGUCr90BXH0BWyviN8UbGZ-jIE04YR7LBznkSk4-43KDINU3Z16lpFF6OMSF92_abhLIzXyYzwhOagFDIHxEJj228aFeQHh5vcXz4SwrntQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚔️
🔥
بازی‌های باشگاهی بالاخره برگشتن و قراره طی ۴۸ ساعت آینده این بازی‌هارو داشته باشیم:
😍
🇪🇸
بارسلونا
🆚
ختافه
🇪🇸
🇪🇸
رئال‌مادرید
🆚
ویارئال
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستریونایتد
🆚
تاتنهام
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🆚
منچسترسیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/108240" target="_blank">📅 13:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108239">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90ee39992.mp4?token=k7iVvouLNlgKaIoRwcoFD_1i5dgtUH6IedZk3lA0io3J0aL978CR4E5NlRRp5-3Q_w5C-Gm3-bMAUbVOeFoyaZ7AklQpAbVTifQqVSAg5asmGbgdmd67LhRWwMoMLad4HX3nWf-6nojTM0tPG7MXRFeJaZ7OgPDtC0qT1r1u1-Tdu5HSqXqrwIkfXj2my5QPNc3g-NKQEmnEkRO4RHwqLNoI71F4hSx55rjYwoRUwhBOJ8k4lom_amHV6XHXzWbZbK1AYrIdr1KlpicroXmsy4IkQqjY2kTJon8fv1w2SDGy_UNzHG_EXndm1Z-0yEgX1eVpsfjx2lcLLHhjhh99sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90ee39992.mp4?token=k7iVvouLNlgKaIoRwcoFD_1i5dgtUH6IedZk3lA0io3J0aL978CR4E5NlRRp5-3Q_w5C-Gm3-bMAUbVOeFoyaZ7AklQpAbVTifQqVSAg5asmGbgdmd67LhRWwMoMLad4HX3nWf-6nojTM0tPG7MXRFeJaZ7OgPDtC0qT1r1u1-Tdu5HSqXqrwIkfXj2my5QPNc3g-NKQEmnEkRO4RHwqLNoI71F4hSx55rjYwoRUwhBOJ8k4lom_amHV6XHXzWbZbK1AYrIdr1KlpicroXmsy4IkQqjY2kTJon8fv1w2SDGy_UNzHG_EXndm1Z-0yEgX1eVpsfjx2lcLLHhjhh99sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
باهنر: ایرانی که صداوسیما نشان می‌دهد کجاست که ما به آن پناهنده شویم؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108239" target="_blank">📅 13:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108238">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qjt7DMVWWMqPPf-Hl7nYWVqnEbF29iy_80hFE0WwLaLVHZ3_hQnwD_6HOPUSEsHeOdFSXdGXZkGRkZOLzD6bqTYnfx8cZGALLzaL3_oDYyECzJMwuUWxaR2VRVoWPVGhGOlR4ck5LG5YDGyJMppcxUq3XDC1NFUhrVkvZot6Qn-D90vLq7z2DRJMo18RZh43ltF-awRnHdbCELp3r3QaVWaf7BAZm1MPiRUU4Wnxh6yOVNIc7aWBOiT3eKBaHmiNdy8p1IP34JhK20R_ERB_6gqo6t2KuyJzOfzBYmPMELS9uuj2hTRPiJtZZ1Yy8djeWAYUSDh6V2FDYEd45iFpnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
قرارداد کول‌پالمر با چلسی تا سال 2034 میلادی تمدید شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/108238" target="_blank">📅 13:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108237">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3554e4463e.mp4?token=Hetej7uGJA_QNuEULAHiqEJmgHW5WPxRDFGlmpWqToIe4iOdaBvvTW3kkgk1sh44OuhA2QfAioH0H744RUEdGdTv1cxYx5dc4khs5xBCJ5vLWh3ortPioLC6qbg84j4p7Eoz0USG4IIR2FUh0VSIktT6V9acI60O-ky5FtEoZILnBj1flw1POs_ziHOwFon1dbveoVssn6D8HqkyuIqTsBrZrq22lgAllxJzg9Ohow4D62X3iu7A6v5N2qMr8maqKv75Dmq6pnIViBwLrsQUv5ZSC2pNxi0Fjl0JMhc-vukZBH83R1vOdqWhdY19fwqG-Ra1gq4Z_23_gZ5MzvZdeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3554e4463e.mp4?token=Hetej7uGJA_QNuEULAHiqEJmgHW5WPxRDFGlmpWqToIe4iOdaBvvTW3kkgk1sh44OuhA2QfAioH0H744RUEdGdTv1cxYx5dc4khs5xBCJ5vLWh3ortPioLC6qbg84j4p7Eoz0USG4IIR2FUh0VSIktT6V9acI60O-ky5FtEoZILnBj1flw1POs_ziHOwFon1dbveoVssn6D8HqkyuIqTsBrZrq22lgAllxJzg9Ohow4D62X3iu7A6v5N2qMr8maqKv75Dmq6pnIViBwLrsQUv5ZSC2pNxi0Fjl0JMhc-vukZBH83R1vOdqWhdY19fwqG-Ra1gq4Z_23_gZ5MzvZdeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله جدید هادی‌چوپان به منتقدانش در ایران!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108237" target="_blank">📅 13:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108236">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62f9b3658c.mp4?token=TFWJrSXdKn7bEIRNSjboqrk2t1lPTw2ipalbm32M0hoMp03TMQGxnfQ-I9H6WszLOcvVKzrUSVqGVMZUXKY-VKZmrHJZhtbZNcLOnJZ8lpLd2gvjpJnpKNcd8qr9-dP0bQcjJlIyQG9E7WaFF9t92Lro7oLU2V_UXK904yYB20qI2-1bpxKgW98w4MoYfvp1h0C5QVfhQ0-MtDC1-y-THGIVNCq74xcHiDlEPAsizPE10CiKgFbC8GFnTI6dCVIOYixNZhzMu82hPM_HeKi1dgSfACkYkJCCRW4-2wFMNBdLxSn-6Jk5jD7d2Q3NPQmiXWBK1mtD6PENW58wkSE8gZDixHnY5OmLmitR9eMcWRFHmI74-tan2brYYIa0tcT6ZUgRnh_tAvb0Zm_8O1ExxBpVKsEEEczJCKp_XlEh-0UMio3jOFwNbRRRK5Ghn-M7lRdsue-MF9Uu4SfZVkpSr4QpIWYrUReDXh3Ti16J8QnDDZtrMx0eyExZFGfw-ByY-bPQs-hbAMyfUov7sBBO-b9KDyRMROJmiA0qMw6v-K143oBwhA0yuOacl5g7OqvrbUV8hX68htigQjDaukSU6yRHgj53dxON0UTvlOahJGaHekIboxud8CN-p1z0O3rxoxH2rlmr28rHdvs8AwZJn6j8bdTHU1i-NXk3W3hyZxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62f9b3658c.mp4?token=TFWJrSXdKn7bEIRNSjboqrk2t1lPTw2ipalbm32M0hoMp03TMQGxnfQ-I9H6WszLOcvVKzrUSVqGVMZUXKY-VKZmrHJZhtbZNcLOnJZ8lpLd2gvjpJnpKNcd8qr9-dP0bQcjJlIyQG9E7WaFF9t92Lro7oLU2V_UXK904yYB20qI2-1bpxKgW98w4MoYfvp1h0C5QVfhQ0-MtDC1-y-THGIVNCq74xcHiDlEPAsizPE10CiKgFbC8GFnTI6dCVIOYixNZhzMu82hPM_HeKi1dgSfACkYkJCCRW4-2wFMNBdLxSn-6Jk5jD7d2Q3NPQmiXWBK1mtD6PENW58wkSE8gZDixHnY5OmLmitR9eMcWRFHmI74-tan2brYYIa0tcT6ZUgRnh_tAvb0Zm_8O1ExxBpVKsEEEczJCKp_XlEh-0UMio3jOFwNbRRRK5Ghn-M7lRdsue-MF9Uu4SfZVkpSr4QpIWYrUReDXh3Ti16J8QnDDZtrMx0eyExZFGfw-ByY-bPQs-hbAMyfUov7sBBO-b9KDyRMROJmiA0qMw6v-K143oBwhA0yuOacl5g7OqvrbUV8hX68htigQjDaukSU6yRHgj53dxON0UTvlOahJGaHekIboxud8CN-p1z0O3rxoxH2rlmr28rHdvs8AwZJn6j8bdTHU1i-NXk3W3hyZxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇪🇸
آنالیز دیدنی از سبک پرس فوق‌العاده بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108236" target="_blank">📅 12:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108235">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ae47b4ef9.mp4?token=ZXjkMM3JfHdSjjsj1wYrmHdQhuWEEXwwwx71ircAQhWjLpsTA7fo7E4CcGR_soi-sEB41UNqJjHgSidjXmXA7ZUjhzNOdRJLEQSBGQ8DACLQZTo4UcXIgnH2zEq-vqpU4ModXGvsdtWj9Hyx0pNOLZpBgnlt4bg28RqsyrWtW-jC7DtSRBPjWkbysqMyfOkYXyBWmcaWhRyInhr-t4BwA1doaT_2SCJD_3dfH3FJ_wgVs29JimQDj0NSBrqixCLc_-KWo7KQJAdO0uhXKC7U1nMAkg0Hhgl8hpkfXev_KxapbwVTbeH7Otx6TBzY7fhGr7CJmFOdrUelvXLfg1FJXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ae47b4ef9.mp4?token=ZXjkMM3JfHdSjjsj1wYrmHdQhuWEEXwwwx71ircAQhWjLpsTA7fo7E4CcGR_soi-sEB41UNqJjHgSidjXmXA7ZUjhzNOdRJLEQSBGQ8DACLQZTo4UcXIgnH2zEq-vqpU4ModXGvsdtWj9Hyx0pNOLZpBgnlt4bg28RqsyrWtW-jC7DtSRBPjWkbysqMyfOkYXyBWmcaWhRyInhr-t4BwA1doaT_2SCJD_3dfH3FJ_wgVs29JimQDj0NSBrqixCLc_-KWo7KQJAdO0uhXKC7U1nMAkg0Hhgl8hpkfXev_KxapbwVTbeH7Otx6TBzY7fhGr7CJmFOdrUelvXLfg1FJXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
دیس شنیدنی قیاسی به قیمت کالابرگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108235" target="_blank">📅 12:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108234">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec43246d0.mp4?token=r_Rq415374rK-tvP98IpgT5mqiK8S2KxzqIMYHu3XeHclyQNnKJqf6nyPKOg0HGt6hR0nl9tTh_RCzXjsCVkZiMrqna-AGURf2K-dx5fc9pcc6Sj-hf1oSrM_CLx9hFJY_NmVPzyvdE-1_10weJbMjuUE4sFWTE1NAWhq8x4OvszNUcUdHpvF2bLhCuY2Ua0jRNEmOgBXHr9PZGtwhUSpa1C5xlh1-Qbv-i6zSQD9XrJRZFFvPas6pGj17x7ho6qhuO4LXk7mbINiNClmhMCYF4iaBLqoT959HHZGdzRzzy4NJU3kPRXSofoQanbgTP7Sf3dOhfBNDdgO3GaeVLWUgXAfr3xA8w3zMgmxJFZZR1oan64Yvp78O1G3Pajp0lPUM5vOJcdyNeBmvrjXWbFTn4AsTuibUO21XW7ofj33lWWuYd6ctY-1Dg5Tp0Uv023MMBNluZK4QbgLQFphCMCD7zSBEHhuf6NrY11e0NZuKrcAWSkq13nPDvEI5_YyWn_Tg_BaSwO4GELyYSqdqvL5T7obIHz6mg-C9Y98h5bYm0kfyeKLPfTOfZ1E9wEppwR9P4exiQyFIC9Ivi4Nr2fpItPFgP0dfZvVGzDslnsymwMADL4652F22iDmkfFZGofR-xMS90VTTLi_lfss2PK8_XYAOhMcRGPG7kb4Yy6q1I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec43246d0.mp4?token=r_Rq415374rK-tvP98IpgT5mqiK8S2KxzqIMYHu3XeHclyQNnKJqf6nyPKOg0HGt6hR0nl9tTh_RCzXjsCVkZiMrqna-AGURf2K-dx5fc9pcc6Sj-hf1oSrM_CLx9hFJY_NmVPzyvdE-1_10weJbMjuUE4sFWTE1NAWhq8x4OvszNUcUdHpvF2bLhCuY2Ua0jRNEmOgBXHr9PZGtwhUSpa1C5xlh1-Qbv-i6zSQD9XrJRZFFvPas6pGj17x7ho6qhuO4LXk7mbINiNClmhMCYF4iaBLqoT959HHZGdzRzzy4NJU3kPRXSofoQanbgTP7Sf3dOhfBNDdgO3GaeVLWUgXAfr3xA8w3zMgmxJFZZR1oan64Yvp78O1G3Pajp0lPUM5vOJcdyNeBmvrjXWbFTn4AsTuibUO21XW7ofj33lWWuYd6ctY-1Dg5Tp0Uv023MMBNluZK4QbgLQFphCMCD7zSBEHhuf6NrY11e0NZuKrcAWSkq13nPDvEI5_YyWn_Tg_BaSwO4GELyYSqdqvL5T7obIHz6mg-C9Y98h5bYm0kfyeKLPfTOfZ1E9wEppwR9P4exiQyFIC9Ivi4Nr2fpItPFgP0dfZvVGzDslnsymwMADL4652F22iDmkfFZGofR-xMS90VTTLi_lfss2PK8_XYAOhMcRGPG7kb4Yy6q1I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😳
مصطفی میرسلیم، عضو کسخل مجمع تشخیص مصلحت نظام: تیبا با خودروهای خارجی قابلیت رقابت دارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/108234" target="_blank">📅 12:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108233">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108233" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/108233" target="_blank">📅 12:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108232">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqR1_SgT4b1VtgHwWcZz-B_Z3aEj3lFEDt5BZpa-_wyrl2leyxRpiaN7geJFFGignLQoDLBqBsp7CXeA5mruqW0DeqXLs_wdzJzwgl5qx0c-e1FGgGezZTekVnPeM5f9wH-dGtvvClKGWHOCAtZ_pYbZSc4RtFJF_i4LROpczsJ_FNztuFQndAGGeFu896nX4DwEADbMeMlXJarE2o4HL9T8RcAcQpQ9oR3wJNbG6xzxKDEGDZuUmSwzZSPa4AgQzF8czcgn-HQcEcLX2oVtAKDrFSnepVLEoKbyBVxelIBazPPUW_mRZtiCyGjEOsrOXFQT6CQ-Jtnm9RISmED8NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
لیدز
🆚
آرسنال
بورنموث
🆚
چلسی
تاتنهام
🆚
منچستر یونایتد
ختافه
🆚
بارسلونا
ویارئال
🆚
رئال مادرید
بایرن مونیخ
🆚
آگزبورگ
پارما
🆚
اینتر
فروزینونه
🆚
ناپولی
لومان
🆚
پاریسن‌ژرمن
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
https://TrexBet.com</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108232" target="_blank">📅 12:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108231">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46a6a1545e.mp4?token=GT5KJLKckoJMmcIqfmqVSx-USGRUoVQIqRFNCfcx4rQSyUB5fN01pT4o8Q7pv0_RfpdKcMCdhjSNEocMEr5CWdORvXdb5zRelIr1jY4VT9dOqpSAXdY6mEqlQd98liUUQCMSzsp52R1hYNSET3kKwU3NdVFu02gRD3G5fuOUDEx59mXBl0rEf3H9O62pUL6JvBPzhKRUIrI6yjyokqk-9VoVsuzt8_dznElXs1UQQ6bE2UF0qK_E3SjKDDzq2ARPYrlAyzqPn-PsiXRzQl68_fMEUOfeqNNasnoajGxCSuvuxWmQ0CWsZx5o6yDlkIqRukrIUZiyCdhLzhL3bMtM7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46a6a1545e.mp4?token=GT5KJLKckoJMmcIqfmqVSx-USGRUoVQIqRFNCfcx4rQSyUB5fN01pT4o8Q7pv0_RfpdKcMCdhjSNEocMEr5CWdORvXdb5zRelIr1jY4VT9dOqpSAXdY6mEqlQd98liUUQCMSzsp52R1hYNSET3kKwU3NdVFu02gRD3G5fuOUDEx59mXBl0rEf3H9O62pUL6JvBPzhKRUIrI6yjyokqk-9VoVsuzt8_dznElXs1UQQ6bE2UF0qK_E3SjKDDzq2ARPYrlAyzqPn-PsiXRzQl68_fMEUOfeqNNasnoajGxCSuvuxWmQ0CWsZx5o6yDlkIqRukrIUZiyCdhLzhL3bMtM7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
امیرحسین قیاسی: گلشیفته میخواد برگرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108231" target="_blank">📅 11:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108230">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28909a001b.mp4?token=m4Dgj4Qg5wzkZLx7oal_G7zDai7QIurFctgKwtcxeyV-oKLCJ4u5O41Zhxtyii56jqzDokYvylDB_s-mrqnLF-dm1O7sBpcL6HFahYbtThEyENkl5Qk1dLUd_5VWsliFd-3RdACN_sZYpYIraWAdHBzA900ComwN_yJCSDA0JgcqmN9MtZhht2AdDDgT1XcCGyTeP-nPGBPe0JNCsSdL8obI3Zxtk5rLkI1yYBYs22rqBDoz4tmtIg4YoS7zjYB5cDl40W7dj9d-_D8hVN56oPywlQ9fkEgTTfelm67vy_lnMBv6MqabcI5NhNb7Ftmuv-waAbWrln9mbD_WAaPLUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28909a001b.mp4?token=m4Dgj4Qg5wzkZLx7oal_G7zDai7QIurFctgKwtcxeyV-oKLCJ4u5O41Zhxtyii56jqzDokYvylDB_s-mrqnLF-dm1O7sBpcL6HFahYbtThEyENkl5Qk1dLUd_5VWsliFd-3RdACN_sZYpYIraWAdHBzA900ComwN_yJCSDA0JgcqmN9MtZhht2AdDDgT1XcCGyTeP-nPGBPe0JNCsSdL8obI3Zxtk5rLkI1yYBYs22rqBDoz4tmtIg4YoS7zjYB5cDl40W7dj9d-_D8hVN56oPywlQ9fkEgTTfelm67vy_lnMBv6MqabcI5NhNb7Ftmuv-waAbWrln9mbD_WAaPLUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇳🇱
نوادگان یوهان‌کرایوف در آکادمی آژاکس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108230" target="_blank">📅 11:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108229">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15d66cbfc.mp4?token=LYIoVOr6RNDxPsN5FuOiFijvvcB3UyYhKImgMj1sY-DX_R8vkf1tC5a-lfBXCLsTurl0oxBUOrx5uGuUakejoIJYT8SNGx6Gc9qe422rLhIDQ34ILy9JLiAXXM6ORq79Z1BL0oaxJ7IuTP1CZo65vRHLSYOUtVzRGIhtJzoMVaQpa6IfmAtnCzyP-PNswffbrCf_VfG6CFbLYDuoR_MA_Kl2hkNqs2nYP99dF_uaiHPNl5WeRWnf6mDZEpgqoQwJOtOZyi7z4Vqu8eSoiJrRhvd3__tRnV0nl6gWqqcuPSaO5kGMDUPZA2mguA6t3vsMiGSdYpyAjPG7VhRVv3hLHTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15d66cbfc.mp4?token=LYIoVOr6RNDxPsN5FuOiFijvvcB3UyYhKImgMj1sY-DX_R8vkf1tC5a-lfBXCLsTurl0oxBUOrx5uGuUakejoIJYT8SNGx6Gc9qe422rLhIDQ34ILy9JLiAXXM6ORq79Z1BL0oaxJ7IuTP1CZo65vRHLSYOUtVzRGIhtJzoMVaQpa6IfmAtnCzyP-PNswffbrCf_VfG6CFbLYDuoR_MA_Kl2hkNqs2nYP99dF_uaiHPNl5WeRWnf6mDZEpgqoQwJOtOZyi7z4Vqu8eSoiJrRhvd3__tRnV0nl6gWqqcuPSaO5kGMDUPZA2mguA6t3vsMiGSdYpyAjPG7VhRVv3hLHTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🎙
ماجرای خواستگار عجیب رضا گلزار: دختره بهم گفت نمیخوای تکلیفم رو روشن کنید آقای گلزار!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108229" target="_blank">📅 11:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108228">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f9b62a8b.mp4?token=DnFp8ES1vPDRio6-WCtTswfcOrvKuqnCduGxbgxGz3qRVzvpiOE5_KwKQBIHdw-NX33YGmBxQrulYyDCjNTG1Edt8pOrSWXLFLGev1RrpMrI7pX0aI6OerqM1ipRg1aThcDetrM7HPYhVZpRN5WtbEi4miyLZ1o0oQ-2MAlHW7RvzETZsjrStxlDQzZSmDfJZnmSm8RzREXkoge2tG_H8h9fF9X5UHv6mMiGebrEzW2XvNxBgYm7vQxM5rRZbTv5ZSp03nDMvmU4yWOgGRZ555trNRedLcswxc4DdTq8IoHxHFfc1GOM21afNIEOFAYM2imLQFg2rx8BWvqVcqAWhTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f9b62a8b.mp4?token=DnFp8ES1vPDRio6-WCtTswfcOrvKuqnCduGxbgxGz3qRVzvpiOE5_KwKQBIHdw-NX33YGmBxQrulYyDCjNTG1Edt8pOrSWXLFLGev1RrpMrI7pX0aI6OerqM1ipRg1aThcDetrM7HPYhVZpRN5WtbEi4miyLZ1o0oQ-2MAlHW7RvzETZsjrStxlDQzZSmDfJZnmSm8RzREXkoge2tG_H8h9fF9X5UHv6mMiGebrEzW2XvNxBgYm7vQxM5rRZbTv5ZSp03nDMvmU4yWOgGRZ555trNRedLcswxc4DdTq8IoHxHFfc1GOM21afNIEOFAYM2imLQFg2rx8BWvqVcqAWhTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تاج ادعای کریمی را تکذیب کرد: نه تنها ۳۵۰ هزار یورو ندادیم، از مربی تیم ملی جریمه هم گرفتیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/108228" target="_blank">📅 10:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108227">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حسین‌کنعانی جلو این اسطوره سندورم‌داون داشت خودشو به فنا میداد که شانس آورد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108227" target="_blank">📅 10:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108226">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db6a9148c.mp4?token=udgv_Pcgkg2XPwxu3cLNs-iRuP9J97qQkpQfcreiDZiW5yElzD6KwRF9AIgAEIFhwN_fHZZ_W9H4TZIO8hE2QhAc0ZOBy9bACkf9PUMd1dIOxLWYJtNWstlKP23f9ofBLOM3JPNJc47uap681SOQEfcIRcTABtIYukzFBmAJLc_DXyNfTUmNQ3E7V1L3KR9V3X6m3t44C1o4zLC2yHuigFmvIDO0q4liYq0LYCd1pbo8cmwYvHm1s3sp8gzYSdP89Qsvpj7T-K-mnjXPOcq9CgjSOpKi18DetxGmdhGgp3KTkHez4MIjA7CvwTGUYe_emXRrqBZe8LhvSZqv6dD6tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db6a9148c.mp4?token=udgv_Pcgkg2XPwxu3cLNs-iRuP9J97qQkpQfcreiDZiW5yElzD6KwRF9AIgAEIFhwN_fHZZ_W9H4TZIO8hE2QhAc0ZOBy9bACkf9PUMd1dIOxLWYJtNWstlKP23f9ofBLOM3JPNJc47uap681SOQEfcIRcTABtIYukzFBmAJLc_DXyNfTUmNQ3E7V1L3KR9V3X6m3t44C1o4zLC2yHuigFmvIDO0q4liYq0LYCd1pbo8cmwYvHm1s3sp8gzYSdP89Qsvpj7T-K-mnjXPOcq9CgjSOpKi18DetxGmdhGgp3KTkHez4MIjA7CvwTGUYe_emXRrqBZe8LhvSZqv6dD6tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
گلرها بعد از تعطیلات فیفادی
🫨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/108226" target="_blank">📅 09:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108225">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e462fbf72a.mp4?token=X3FuWCVD1TDSHuMFHyIzy1vZZgJvgs-0DjcwmbpVBiXTimVHOkh5bdkZUxO7lLSSVMZgKKffKD3QVzJ8Th-ujdI0dpf_Kt-FCxJJkv6vQ_iQA1us8ZEdgdPR3-2mEAZrjgPCw_-m4rs2UMUO45cuOrTvMyBO7XvgZ7-rUCHTwdnhIxEmhfawm4PFLmZTj4Sia5mYfWW1iCpvVws2FxBxbg4a_2HMsXIRArrnZpKRCT7NSbSXHunWTuY9yzNTITCogvmCtX1X1WWo4qkHREvAjo7axxnZBJcTSwqg2dLW78Z4h4V5bn3hbzlQ_t9lWdFHhk0RJgEzvcHCS4HsdqOTuDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e462fbf72a.mp4?token=X3FuWCVD1TDSHuMFHyIzy1vZZgJvgs-0DjcwmbpVBiXTimVHOkh5bdkZUxO7lLSSVMZgKKffKD3QVzJ8Th-ujdI0dpf_Kt-FCxJJkv6vQ_iQA1us8ZEdgdPR3-2mEAZrjgPCw_-m4rs2UMUO45cuOrTvMyBO7XvgZ7-rUCHTwdnhIxEmhfawm4PFLmZTj4Sia5mYfWW1iCpvVws2FxBxbg4a_2HMsXIRArrnZpKRCT7NSbSXHunWTuY9yzNTITCogvmCtX1X1WWo4qkHREvAjo7axxnZBJcTSwqg2dLW78Z4h4V5bn3hbzlQ_t9lWdFHhk0RJgEzvcHCS4HsdqOTuDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
حمله علی‌علیپور به میثاقی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108225" target="_blank">📅 09:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108224">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8286fc429.mp4?token=RLs3XBx_vsQVCVpGdwW-SM1Im-QKW5YPTYtKSPMkZCDuwBwifFiEbJXm-LEc1jZustzQ-qjVCKgcVuNT-2uMVVsJFEiELLZurDXYWQoFMzGhhdGVhs8I8HOJeLtGTxJwcV1Nqirz1jTLObfMnIxFOWT_2AMYVY0m3kFG6pJsBKATVZ0-txcoaKMxSe_Ean7yFpJOnog5VgX-hutEyC7v9ujR4sqLgzY0RjIgJUed2678hpy50BKn6iGjqJQOo_SGkxCzOxDpNphlpt7rM1WnT29YPHo8D9enffOtwRY_gWQ6E7zVEl-Q6cQ593A7zZFGH8y-iQghCq6TzQJTpwQrqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8286fc429.mp4?token=RLs3XBx_vsQVCVpGdwW-SM1Im-QKW5YPTYtKSPMkZCDuwBwifFiEbJXm-LEc1jZustzQ-qjVCKgcVuNT-2uMVVsJFEiELLZurDXYWQoFMzGhhdGVhs8I8HOJeLtGTxJwcV1Nqirz1jTLObfMnIxFOWT_2AMYVY0m3kFG6pJsBKATVZ0-txcoaKMxSe_Ean7yFpJOnog5VgX-hutEyC7v9ujR4sqLgzY0RjIgJUed2678hpy50BKn6iGjqJQOo_SGkxCzOxDpNphlpt7rM1WnT29YPHo8D9enffOtwRY_gWQ6E7zVEl-Q6cQ593A7zZFGH8y-iQghCq6TzQJTpwQrqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
میرسلیم: چه کسی گفته نفت ایران متعلق به مردم ایران است؟ نفت ایران مال مردم نیست و متعلق به خدا و پیامبر است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/108224" target="_blank">📅 09:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108223">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdfc01a1a5.mp4?token=g89V8AXOLH04-oUalRhvlSWNxRH5SbPbAtoIzQj3lay0u5X9JBtYf6MnJNGWvLe5fK97rTu_fBZxsIYg-IMBYPvhBqGz9TUcYA4aU7rzSQGRNPIFIZCtw_5gGHaf43PZSreluzs003cWX4m-U_rrIuGRwC_Wu0ZczZLj7gf_2mRXTQM5mWr_MyZ0KHPqpC5GV0_T0qyr-5-GycJhoAxDJtcx_xzoVeext4_S5Am7W1cNLX8Ux3uMGs12ZAQrfRMLnylbibmT50DegRQ61uF1v36_0L9wLy1nRqNUylea6Mdp5htDDkpLPhoie0Z7vqiMpgc-cfWiGXrGanhUvicwog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdfc01a1a5.mp4?token=g89V8AXOLH04-oUalRhvlSWNxRH5SbPbAtoIzQj3lay0u5X9JBtYf6MnJNGWvLe5fK97rTu_fBZxsIYg-IMBYPvhBqGz9TUcYA4aU7rzSQGRNPIFIZCtw_5gGHaf43PZSreluzs003cWX4m-U_rrIuGRwC_Wu0ZczZLj7gf_2mRXTQM5mWr_MyZ0KHPqpC5GV0_T0qyr-5-GycJhoAxDJtcx_xzoVeext4_S5Am7W1cNLX8Ux3uMGs12ZAQrfRMLnylbibmT50DegRQ61uF1v36_0L9wLy1nRqNUylea6Mdp5htDDkpLPhoie0Z7vqiMpgc-cfWiGXrGanhUvicwog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇷
🇮🇷
محمد تقوی، در برنامه هت‌تریک با آنالیز بازی پرسپولیس-صنعت نفت آبادان گفت: «سه بازیکن نقش پررنگی در پیروزی پرسپولیس داشتند؛ محمدمهدی محبی، بیفوما و ارونوف. صنعت نفت توان رودررویی با پرسپولیس را نداشت.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/108223" target="_blank">📅 08:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108222">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ffece8e7c.mp4?token=cFgOdGvPsMLWIjoatufd96WKwGZV_9tDRByWPI_DBZUDzwwifg4NOU2hJ7Y4JxiTq8azlpnuPJVOeNLRgA8If-wDd-uTg8tJ8vcH8IAPdUxBYmB_gqCOcMwZITicTAEfcWajMToYCeHPRInTfdJom0m6AWP0164Dfnm_JDTnipG7l9sonhihSFnGHzbFBX48N3ep_f2k2TljqWiWm_kkrV18-mTxDc7t1yOzXBy913hc1iqgTWhvImWwdvUyQ5TqtLev2ZfnNKxIZRNHG95e70a0SBfBTNEqU0rS-5QWV0_I6ewCUUsLdwQR6Rz5zqPrWsrsfhDmURj-DTO3sA-W9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ffece8e7c.mp4?token=cFgOdGvPsMLWIjoatufd96WKwGZV_9tDRByWPI_DBZUDzwwifg4NOU2hJ7Y4JxiTq8azlpnuPJVOeNLRgA8If-wDd-uTg8tJ8vcH8IAPdUxBYmB_gqCOcMwZITicTAEfcWajMToYCeHPRInTfdJom0m6AWP0164Dfnm_JDTnipG7l9sonhihSFnGHzbFBX48N3ep_f2k2TljqWiWm_kkrV18-mTxDc7t1yOzXBy913hc1iqgTWhvImWwdvUyQ5TqtLev2ZfnNKxIZRNHG95e70a0SBfBTNEqU0rS-5QWV0_I6ewCUUsLdwQR6Rz5zqPrWsrsfhDmURj-DTO3sA-W9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇷
🇮🇷
محمد تقوی با آنالیز بازی تراکتور و استقلال گفت: «من بازی را به دو بخش مجزا تقسیم می‌کنم؛ نیمه اول به طور کامل در اختیار استقلال و نیمه دوم تراکتور بازی را در اختیار داشت؛ استقلال شانس آورد که بازی را نباخت. اما مساوی، شایسته هر دو تیم بود.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/108222" target="_blank">📅 08:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108221">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c27c71fd.mp4?token=avjFV21BHUhoIpD9AcQxomgREGKfPvmSjNF3BuKaUnOD8_nuGKVWhNru1G2yL4Qjp8P6L_4ZkAE--yc0y0lgp9ot1_cRteFCcH6GhQvyJ0aMjKNa-D1RUO1QRm7QVdA_SidVlKBYJEygam9VZ_qQ-wVMmJ-pljWK3xqxZCWp1RTQSPNHZwE-Hv004dX8CBnUWlCMQ6h_XpiINxyumpbYQG9pBN0-bOJR7ERyqIgBGZDYLqzPsildV7yH4nz5HEYtT1fIlD--yBtIoMvj9x2kByH0K9AwVsR4ebxTEgjqcWi2rRItijREfb3RNHVoSSxMtaxYSCjDoXp4R4rGHQcwYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c27c71fd.mp4?token=avjFV21BHUhoIpD9AcQxomgREGKfPvmSjNF3BuKaUnOD8_nuGKVWhNru1G2yL4Qjp8P6L_4ZkAE--yc0y0lgp9ot1_cRteFCcH6GhQvyJ0aMjKNa-D1RUO1QRm7QVdA_SidVlKBYJEygam9VZ_qQ-wVMmJ-pljWK3xqxZCWp1RTQSPNHZwE-Hv004dX8CBnUWlCMQ6h_XpiINxyumpbYQG9pBN0-bOJR7ERyqIgBGZDYLqzPsildV7yH4nz5HEYtT1fIlD--yBtIoMvj9x2kByH0K9AwVsR4ebxTEgjqcWi2rRItijREfb3RNHVoSSxMtaxYSCjDoXp4R4rGHQcwYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انتقام بیرو از حجت؟ دیس‌بک بعد از ۲۸ ماه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/108221" target="_blank">📅 08:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108218">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sI_L4G82P8-kI_iU7x75gZY_dlrn37Z5EYKdpLoArfKUOuNdqLj3zJ9j3Kw8UjEbGTHoI-nYZM7FF35lmw-u5YkM_p9aB0GrotS24mQrmASVCFyf_WrLlAoL1-Ad9a3oO9A-nj8k_9-MwrB9ckcfSH41DrcYS3t_1MyOxameqPz8ZCiA6iGrz-xsuzl5SQBJZ5t48qIfY6nr_VI1n1YGNQMs-5DvA4BHbgm7f69xj7-l4-XQNqZj3O_Wia_t3iYpxmslIoM9YBH6ESfd9J1_n_DgUZ6UlzjzqkM_Kytl4-UPLu-g1dywyj1GUs9NKd-7I5dYlGwuv_yU6nZvbPUhoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
❌
#اختصاصی_فوتبال‌180
؛
🔴
در گفتگویی کوتاه با مدیران پرسپولیس این باشگاه اعلام کرد که در نیم‌فصل هیچ قصدی برای مذاکره و جذب بشار رسن یا بازیکن خارجی دیگر ندارد چون ظرفیت بازیکنان خارجی این تیم پر است و محدودیت‌های نقل‌وانتقالاتی فصل‌جدید مانع از جذب نفرات دیگر خارجی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/108218" target="_blank">📅 01:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108217">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbXj1CoDfYwjPUqQYXuF_Ak_Pn137NkP93mLIiCz2zKSD_4-eYdQLW8mGbXXHruDoDuji36DWYHiqv8shwpLu9r6BKOCIAFL8JL4cWcvVR97deT9Vw-SHbMi4SJVNFI5aAYOdIDouBfPdV51TO6x-0hGzhy5P1nGoihIoZASTaOZvUh4FXOVdUxwHY4BS9pehe-5hLC13sIy396iRs1oRmwmn0dqG4bBMtEIw0e5HIGf1A9euVPhuOJGS7L38mhk30JncXqzWsHffz1u2sRCFy9unntM_eIhc4c-Xkj8KZSqiqtH7tFUAEfJSMwVr1jXntHodwZcIeeJjrs9DOPOUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
❌
🚨
وزارت امور خارجه آمریکا در توییتر: به هیچ دلیلی به ایران سفر نکنید. شهروندان آمریکایی باید همین حالا ایران را ترک کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/108217" target="_blank">📅 00:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108216">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2M2DJV2JCswaphnpgDJMpjnk7Q1iiBB2N_LBgcyrt9FyuHDulsYESmr9WwZLESmK7WAKnRF0Gf_MoPLXg3WnudN1iSQMDZwcT4p9AKTZG941wHLsHQqNkePD2PxQikaFZOU3TgXEbesqqd6HOCSI20qHpX9Q8zkrqs24hUa0Ygut7JJ0mHLK51IBybtO-x6B6AcHmSNcfFSGFARTHomL8zWiboA0KvSOjRyW_8O0ssFZJC70i6aIaE6RAFqWhJn8VBRSGvtRm4D4bZsTHhDAO_0CzvkirMydRZBi_rWhaPJkawtPH21kgYdEep61y1ZT2mgsUqGX_uwXSCmTefitA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🚨
ظاهراً سازمان نظام وظیفه به بیرانوند اعلام کرده تا زمان مشخص شدن وضعیت کمیسیون پزشکیش حق خروج از کشور رو نداره و حتی اگه بیرو با مدیران باشگاه به این اختلاف نمی‌خورد هم نمی‌تونست شاگردان نکونام رو در سفر به مسقط برای بازی با الشمال همراهی کنه مگه اینکه مشکل خروج از کشورش رو حل کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/108216" target="_blank">📅 00:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108215">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab16b6ba1.mp4?token=obzKdYSDlt911c2dTUUDX7YDkqSnZZ83XaRnxbf1E2_-ZE943R5o-kRbOGFX-wpkTKJXENeuFvfRtMENKAXuFxgcICiTwWdTUPK8aMppj6UM7r-pyPcAlDhAUSBKBAwMcu55eyPAbP7hdPCAk77l4h-9KCaifHje6GXlkwH2MZyDrH8-32HvojgAy5GEj3NSXQaC5Hw2G-tsd4wCbXm3I-VkUyJx2HUzwOK_rGb14cdrXnNfLERPVNmOzHfOG_9ujlTyEGsyOHdyWmZr4uRx0GrbpEKlu7GSQjdiPEEjSBPuUi0JPo4ElN2x7zDEDVClAlpO2LjittK55XD_K1cBxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab16b6ba1.mp4?token=obzKdYSDlt911c2dTUUDX7YDkqSnZZ83XaRnxbf1E2_-ZE943R5o-kRbOGFX-wpkTKJXENeuFvfRtMENKAXuFxgcICiTwWdTUPK8aMppj6UM7r-pyPcAlDhAUSBKBAwMcu55eyPAbP7hdPCAk77l4h-9KCaifHje6GXlkwH2MZyDrH8-32HvojgAy5GEj3NSXQaC5Hw2G-tsd4wCbXm3I-VkUyJx2HUzwOK_rGb14cdrXnNfLERPVNmOzHfOG_9ujlTyEGsyOHdyWmZr4uRx0GrbpEKlu7GSQjdiPEEjSBPuUi0JPo4ElN2x7zDEDVClAlpO2LjittK55XD_K1cBxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
آخرین وضعیت شکایت باشگاه ها از آسانی از زبان رئیس فدراسیون فوتبال: هر تیمی دلش میخواد میتونه به CAS شکایت کنه و مانعی نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/108215" target="_blank">📅 23:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108214">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsYaWpg9NyWzpYeXl8OWdWthl8RU42JMDIMy3k1IWNTJ6su383W5v1LXtvDceep_Vb8Zx6ETvR3FRMNRkYSaW8NMYbdNSCjcOztkuLZTqtNXx8iOj6hVFqGW9ZFoIp_geWxgWmOoHJfaGv0hsXtMDlKcwFaM5A7pSmPL_8dE7lJ2ev7Aa4FCABOn-RHvl78BJePpWC5pz4qBvbfZRnuOQMJqq0F52Xq-e1N3V2AdM8n6HsQrPDjP-otqNZjhTey3OPUBrUvXgGiOw5dGbRVV7gYzjTc96znLEIrD2udOuoakLnsnOEDxtAa5I01BuyngBeM0xhlB6wOysw4CoPCwoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
فوری؛ بیرانوند از هتل اخراج شد!
علیرضا بیرانوند پس از درگیری لفظی با مدیران تراکتور و در آستانه سفر آسیایی این تیم، از حضور در اردوی تراکتور منع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/108214" target="_blank">📅 22:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108213">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6phDc1jvKkJTdMsSbvHviC6vdc9H3D33CD2wat9VWVl1T1nBFfml-oNHHVhgOZwteoEqbLF7ZzkkngvNWStQgXo_nh7gJdOOhOtDpXwB8DKy0lnTwecwXTKVoKvJaKrODQyy6O0Wwrq-iI-98s9ra6wyTCmbFExwIMIXHVleOol2fgujxkY72QFuN2zsM2CoYf5wyRSH67-WVD-bz1FbXFqdbmKvYOCR1IwBOVfIQFmiOCoOBNa1rEeh47M6jPHeoTMP2BsBfsriLr250e2X4-ZWfwJVWhcP8Vtif4d2MqTfhVjUku8v4JclnHTykegezNKNl7yeE01uycOxaEP8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
❌
محمد نوری پس از شکست مقابل پرسپولیس از هدایت نفت‌آبادان اخراج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/108213" target="_blank">📅 22:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108212">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b78fb174d.mp4?token=GI9Wo9EUSNn-4t3KoYWT4wVC2qN1c5egMkou2YW3IYV5atN4aVklxem-q2lnxPqcAH2-1ZVhwPTsuTPIe8XGcomru4EEEVaChTe6Ni5--mnGM3IlZ3u-osTwqi-JzLOF-Yf5EE34JGFh6aDdUxfSrvJvXf24VHsSD8CbFxqxDo-RC0NrhNltMQe5smiUtV1eC_Y_nvWmx4mVKPYSpmC-AiQNIaeSxCRBN4Ww37T86bmIZj9OpwRwzARSVpfPZeM_khc25nBZRYb8KyTVeh9g38YlDBM1oc4CaikJyi5adwvDttXU9Q4N_SMwqcenIsYyc31vwwqiDNVPIUAshfsFew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b78fb174d.mp4?token=GI9Wo9EUSNn-4t3KoYWT4wVC2qN1c5egMkou2YW3IYV5atN4aVklxem-q2lnxPqcAH2-1ZVhwPTsuTPIe8XGcomru4EEEVaChTe6Ni5--mnGM3IlZ3u-osTwqi-JzLOF-Yf5EE34JGFh6aDdUxfSrvJvXf24VHsSD8CbFxqxDo-RC0NrhNltMQe5smiUtV1eC_Y_nvWmx4mVKPYSpmC-AiQNIaeSxCRBN4Ww37T86bmIZj9OpwRwzARSVpfPZeM_khc25nBZRYb8KyTVeh9g38YlDBM1oc4CaikJyi5adwvDttXU9Q4N_SMwqcenIsYyc31vwwqiDNVPIUAshfsFew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
گل‌شماره ۹۸۰ کریس‌رونالدو در بازی امشب النصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/108212" target="_blank">📅 22:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108211">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🔴
طبق شنیده‌ها؛ باشگاه پرسپولیس مذاکرات خود را با مدیربرنامه‌های بشار رسن عراقی آغاز کرده تابرای جذب این بازیکن در نیم فصل به توافق برسد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/108211" target="_blank">📅 22:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108210">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
⭕️
🇮🇷
مهدی تاج: هیئت‌رئیسه مخالف دادن جام قهرمانی به استقلال بود، ولی این مورد مجدداً در حال بررسی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/108210" target="_blank">📅 21:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108209">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
‼️
🇮🇷
محسن خلیلی، سرپرست پرسپولیس:
یاسر آسانی؟ باشگاه تمام مسائل را از صفر تا صد پیگیری می کند. داخل کشور به نتیجه نرسیم صددرصد در دادگاه عالی ورزش دنبال می کنیم. ما نگفتیم این پرونده پایان یافته است. مندیت آسانی به پرسپولیس؟ بله او مندیت را داشت اما زمان همه چیز را در این زمینه نشان می دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/108209" target="_blank">📅 20:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108208">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hr3aQlGENwUxvWnCF2Mk5uWJxO21GYmT0Dnd5XUaYrDQHj9aIDX3SRxa1xr6R5k7ct2ZVWK6wci_omglKfneWAPqM6c0l1t-PPIDyqjyNVwCnJZpCCh9xhYyQsBB3odYAKK72VLXQqljWkDuiCJQFbwl2QNdq6oGnIK2KAt7tizzvOI7GhXB6YaeRqndphAPX0leepKyw_KzKlg6DbQ8nkDloOI11Y3jGk4zWzzbRNNuCRdQ25wJBESfocHuOkJfShn4HUE5Wx96kZ8BopYW-scJH67MIHbzkxXNMfZJLTybKISZq_wmxgD_b7QyX_xIuNKNV0H6C-zgaO4r_3m_1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رونالدو در ترکیب فیکس النصر بازی بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/108208" target="_blank">📅 19:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108207">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e597b9b54.mp4?token=lQKasl8RjI9gKazpWPFI81qbk4QHug6s60EBXjmvaEFRNWspr8EqzHvB829Ju0WgTjE31atNPBu41hEo75-PYjEp7QZpoWVx__vjvDZaURmUDtAZsH5ysVpEEgYZM6044icDIyzdQCBpbYFTvzHjJh7qyZVONgMAJ7a6g80n4NEqeHNPkHtQPi4rjnNuTS_31fPGU3Mv8ag5fme69bAq8fFrc7ykGFYwy0dg-5_VBi14pOkZr2MW1eLI2cT7HOaksO2i55RMyApCA7QZsRLKhWtPuVqS-71yuXL7neiGx62oKQJWaPYvEmbM__CWsi5byZmYXnoI6Twm33O3e4SHRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e597b9b54.mp4?token=lQKasl8RjI9gKazpWPFI81qbk4QHug6s60EBXjmvaEFRNWspr8EqzHvB829Ju0WgTjE31atNPBu41hEo75-PYjEp7QZpoWVx__vjvDZaURmUDtAZsH5ysVpEEgYZM6044icDIyzdQCBpbYFTvzHjJh7qyZVONgMAJ7a6g80n4NEqeHNPkHtQPi4rjnNuTS_31fPGU3Mv8ag5fme69bAq8fFrc7ykGFYwy0dg-5_VBi14pOkZr2MW1eLI2cT7HOaksO2i55RMyApCA7QZsRLKhWtPuVqS-71yuXL7neiGx62oKQJWaPYvEmbM__CWsi5byZmYXnoI6Twm33O3e4SHRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
‼️
🎙
پیام نیازمند: گل صنعت نفت؟ من را ساندویچ کردند و گل زدند؛ مثل روش آرسنال/ از گلزنی اورونوف خوشحال شدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/108207" target="_blank">📅 19:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108206">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1c0466c5f.mp4?token=G594CL8ZS4HYNMVR94bH3rnRfMHKGkePzKLlXtGVYED0mKwvTh5O3iQWecv42IhvfBqlBUDa6X6S3Ga6918ywCu0Dl-Y3We4b7vBLAWX1PZF0GuXzUQAUTyc62nDuFR1XSWqtJW0TnpzbH4vi6qDZYKVTdpAknLZj7iFB_1juszSJJKqESmD1ys6z0AKxqtocRsmUtzJBBQXmniPT6x3j8uhryX-5QOVgo6FpAQVZWLq9WlG-9SbABbEYNaC9xlNAfYt5xYhinf977phfgkHRyNQJFMjRnoQ6xvLm3JSUEW8ULjgBW_kw0qL-YoO1e4-zHyKmRZI7oS0wAlTOFW7_Qc4YVyuB2o2Syp0W5F8m8auh_9NygtUyGp3PIcMv7bDHKvmxGjIYPRyeNjj_p3RCQPTu2PRVzKCJVpTAR_DxwIXrlLAdm1qHPTy_096gMhTz2uc3qu3zsdM2cTpA3cHTdhyG3u3AiGv4P50w0KPDm3ePwdANe3kyPfj_mga9aV4cg5M8i-pimVkRK7VtoTEy82T-e1TxkMnpEKpGChIrHmKEB6_rGlvs9vLOCpA4Q-yKMfKS8DNyNGWiHQEm3dEYDFvG3AA-NgA7Mgj5UByefpVQ2E--9uRzY1P8AcXROSzZoHLiE0CZgIexm2JqE9lTMMFGz0g2uRl6jxfUEHJt_c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1c0466c5f.mp4?token=G594CL8ZS4HYNMVR94bH3rnRfMHKGkePzKLlXtGVYED0mKwvTh5O3iQWecv42IhvfBqlBUDa6X6S3Ga6918ywCu0Dl-Y3We4b7vBLAWX1PZF0GuXzUQAUTyc62nDuFR1XSWqtJW0TnpzbH4vi6qDZYKVTdpAknLZj7iFB_1juszSJJKqESmD1ys6z0AKxqtocRsmUtzJBBQXmniPT6x3j8uhryX-5QOVgo6FpAQVZWLq9WlG-9SbABbEYNaC9xlNAfYt5xYhinf977phfgkHRyNQJFMjRnoQ6xvLm3JSUEW8ULjgBW_kw0qL-YoO1e4-zHyKmRZI7oS0wAlTOFW7_Qc4YVyuB2o2Syp0W5F8m8auh_9NygtUyGp3PIcMv7bDHKvmxGjIYPRyeNjj_p3RCQPTu2PRVzKCJVpTAR_DxwIXrlLAdm1qHPTy_096gMhTz2uc3qu3zsdM2cTpA3cHTdhyG3u3AiGv4P50w0KPDm3ePwdANe3kyPfj_mga9aV4cg5M8i-pimVkRK7VtoTEy82T-e1TxkMnpEKpGChIrHmKEB6_rGlvs9vLOCpA4Q-yKMfKS8DNyNGWiHQEm3dEYDFvG3AA-NgA7Mgj5UByefpVQ2E--9uRzY1P8AcXROSzZoHLiE0CZgIexm2JqE9lTMMFGz0g2uRl6jxfUEHJt_c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
واکنش جنجالی گوهری به جدایی از پیکان: تیم می‌باخت، سرمربی می‌گفت ما جادو شدیم و فقط دنبال این مسائل بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/108206" target="_blank">📅 19:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108205">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4ed7f5cfd.mp4?token=SEP_1JG62IoElIpgRDsZHjBt-K8cviVs7vtzqvaeN7LxZ0QrANadozazc6-e4--6rzMJykk-KjKebKWjhUKO8RqGNS_XaOegpnQUkzN2AQD3YM-jKDQ9kNjmzXARDIR1Vd99FPkAbGRHvUpKeQG9fmrYa8uqWLyRyMKwCkcoHOkpu4wlr3nLvhz5h27E1tZIEoQmgFJBDv275dk4OvM9mQnK0tL6YSPuY9qurd8akJ_qwBqkKLnHt5WUeeI4dTSjrIpsfyte02O7lrkHmG6OIUOp_fAvLW3zIhW_dSggILPLxkq9HjEeQ2RVbgA37SEnBY62_Dk3RUVzjcfIGUQifZ3pcpAbfo4MRFNIbq6DcFpTh-6KlAuZBQoHx43aHzvbUmXEOjOjtq7jKIK6nbat17KwhGD3zf6y9XhnVgmBO1X57CDroR9_CQIfyTkhO7VJE01uri6yxbC-lwbS1vRWNSkmhC713AExZ_B-yeYSeOWUMZ4iq4br0ClbJPs75ykCynLPxGiJFdkaJ4h_Pwr1t3m6X_jr1ylxm9BTVxNQBo1RR-PAJKReVEtLchvTbZk5fGSDcOVPaoxpek6oscSLuNlAZ4LKXeluFewCKUG7eb0N1LH2leJQRdsODHvNDsQnCzIU4NbVTMvV7O7WjYnog818heOYSMmxFgVOzBog5eU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4ed7f5cfd.mp4?token=SEP_1JG62IoElIpgRDsZHjBt-K8cviVs7vtzqvaeN7LxZ0QrANadozazc6-e4--6rzMJykk-KjKebKWjhUKO8RqGNS_XaOegpnQUkzN2AQD3YM-jKDQ9kNjmzXARDIR1Vd99FPkAbGRHvUpKeQG9fmrYa8uqWLyRyMKwCkcoHOkpu4wlr3nLvhz5h27E1tZIEoQmgFJBDv275dk4OvM9mQnK0tL6YSPuY9qurd8akJ_qwBqkKLnHt5WUeeI4dTSjrIpsfyte02O7lrkHmG6OIUOp_fAvLW3zIhW_dSggILPLxkq9HjEeQ2RVbgA37SEnBY62_Dk3RUVzjcfIGUQifZ3pcpAbfo4MRFNIbq6DcFpTh-6KlAuZBQoHx43aHzvbUmXEOjOjtq7jKIK6nbat17KwhGD3zf6y9XhnVgmBO1X57CDroR9_CQIfyTkhO7VJE01uri6yxbC-lwbS1vRWNSkmhC713AExZ_B-yeYSeOWUMZ4iq4br0ClbJPs75ykCynLPxGiJFdkaJ4h_Pwr1t3m6X_jr1ylxm9BTVxNQBo1RR-PAJKReVEtLchvTbZk5fGSDcOVPaoxpek6oscSLuNlAZ4LKXeluFewCKUG7eb0N1LH2leJQRdsODHvNDsQnCzIU4NbVTMvV7O7WjYnog818heOYSMmxFgVOzBog5eU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⭕️
🇮🇷
بازگشا، سخنگوی باشگاه پرسپولیس: مدارک کامل و جدید خود را در مورد آسانی به کمیته استیناف ارائه کردیم
🔴
همه تلاشمان این است که موضوع در داخل کشور حل شود. حل شدن در داخل کشور احترام به ارکان قضایی کشور خودمان است. درخواست از پرسپولیس برای پیگیری نکردن شکایت؟ ما دیروز نامه ای به فدراسیون زدیم که قانون محل مصلحت نباشد. یک بازیکن می تواند نظم جدول را به دلیل تاثیرگذاری اش بهم بزند. فدراسیون درخواستی برای عدم پیگیری به ما نداشته است. تا آخرین مسیر از حق باشگاه دفاع می کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/108205" target="_blank">📅 19:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108204">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad5142fc9.mp4?token=oxzIEsLAPCij7h723KOxVcZts0Jey75z0-LzhnL-Dt4sUGPGrTOKHAl2-OGhD5qUO3mS6KUuS2uNvTALwgHg-e2cKLSgBi9yMDTVcpTn4Cv_PrTNlgklFgynx-3Mv_JIwJd5kMhm6ITp0z0KTGjFq-Czwf_HHBs4XdmCxOWbS8oeYpAikZEh0twnDe2bdK7B7k-i1x8X21ksKuWkTBtJDCP6vl7T1VvuL4-f-2sn6WSM6T6uNs4vj7__ocldvi3HVh6Ol2GK7zJUEOWGLhM1w0QmTvK4BJjoc6S0TgYPQCXSdsAlzygE_kBmrhmKyy4mV8ecd3OC-X-12o1FE0EsCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad5142fc9.mp4?token=oxzIEsLAPCij7h723KOxVcZts0Jey75z0-LzhnL-Dt4sUGPGrTOKHAl2-OGhD5qUO3mS6KUuS2uNvTALwgHg-e2cKLSgBi9yMDTVcpTn4Cv_PrTNlgklFgynx-3Mv_JIwJd5kMhm6ITp0z0KTGjFq-Czwf_HHBs4XdmCxOWbS8oeYpAikZEh0twnDe2bdK7B7k-i1x8X21ksKuWkTBtJDCP6vl7T1VvuL4-f-2sn6WSM6T6uNs4vj7__ocldvi3HVh6Ol2GK7zJUEOWGLhM1w0QmTvK4BJjoc6S0TgYPQCXSdsAlzygE_kBmrhmKyy4mV8ecd3OC-X-12o1FE0EsCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🚨
‼️
🇮🇷
هوادار پرسپولیس: کامنت در پیج السد؟ ماجرای آل کثیر را یادتان رفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/108204" target="_blank">📅 19:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108203">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tB9pKIpEP8V4cJ8LnH_02_tOYBz5rFkzXFAGLgeRaBPrdgv5NOqloIvCa3PulKk6UfpPFaG2IdHiiqw8mYEA3e-KNjkdEVSJxA_fvtj2bFjj8MoApdIpkDBOHx4OjNrcBMcCbNy5qHezto-U2-gmCwTl3izAI5CmB7FmF21Su-pVyRRGTEyJZvp18JcHPp0Y1-qj4tjuxrGsJNJnktZ06VHxyZKdz6jVGHJJTRAe8LIkZ31cJQxMC7fuRHrjsdt3dBnQ_tb7NUorHWjdhFSVOR5-IROATXTGCN4N66mLmwPbSRGzkLEiMYrxNtKbbsUEiURot4VqqF3uRlENd5Wb6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌هشتم لیگ‌برتر؛ بهتر از این نمیشد؛ برتری خانگی با گلزنی اورونوف و بیفوما؛ علیپور هم طبق معمول گلزنی کرد؛ پرسپولیس در آستانه گرفتن صدرجدول از تراکتور
🇮🇷
پرسپولیس
3️⃣
-
1️⃣
نفت‌آبادان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/108203" target="_blank">📅 19:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108202">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VR9Hfft6Rtlvi-gSxY9lg0FbwZK8o2moIxMuoaVZXHUEFPxKm4EoA7Z-aDpdDkStkEcMKI1Qzir5gJ6QvgqJY6YUXTmIrIE42s8xASq3RvHBpuJj74-zuY4_2QumHEusVBCX9yL7_a_drNl4tVO-GBSn8HRrIypijNL_E22plCO8vrvCFeSG3aQaKegH1_RWiWaLcg21O4hCTLPl1Yo3MOZaIPzJywyqIcpijUoJ_qH8VZmAtsZ2RyEdXCYrG0isEuP5_8M9KVBm4HHcdOtVr6yQ8sIVl3xHi3yi2Rt0-h0gRsIFHyFUx-Jp99MAkVaGKOi9__j2OnkbxG0hSP6W0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌هشتم لیگ‌برتر؛ بهتر از این نمیشد؛ برتری خانگی با گلزنی اورونوف و بیفوما؛ علیپور هم طبق معمول گلزنی کرد؛ پرسپولیس در آستانه گرفتن صدرجدول از تراکتور
🇮🇷
پرسپولیس
3️⃣
-
1️⃣
نفت‌آبادان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/108202" target="_blank">📅 18:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108201">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19c9ae46fc.mp4?token=Vuz6PJkvQxcLeDiIO6zuHmWuNrn7lZOGiH9lM9jnfc6dqZUg6-hSn20QfnD98oNJt2NfZV2B60VQiEtj0CLBDPatkx439vBLGQBN4zAz-nqApYLcdMx9NEzG4mrgZDZF67hfIOifi9QQ7qefxoRg_YSKEMosnjcqPlOvsfdfaSLlruWFVz_Lo23pQFgrw-DP3Qqy4Y32857mEJPmPJmrrSa9iAyv2KLazRM_kmp37H1z_DAzisrQwSzi3J0IUdflRdBEEZ8cH79impv8noE5komyIouSiaFn8OdBXzn2ADetdZDqg-yaYWHTGu7Q4ySCPoKaRAZ0BmT8s-FDbvbtDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19c9ae46fc.mp4?token=Vuz6PJkvQxcLeDiIO6zuHmWuNrn7lZOGiH9lM9jnfc6dqZUg6-hSn20QfnD98oNJt2NfZV2B60VQiEtj0CLBDPatkx439vBLGQBN4zAz-nqApYLcdMx9NEzG4mrgZDZF67hfIOifi9QQ7qefxoRg_YSKEMosnjcqPlOvsfdfaSLlruWFVz_Lo23pQFgrw-DP3Qqy4Y32857mEJPmPJmrrSa9iAyv2KLazRM_kmp37H1z_DAzisrQwSzi3J0IUdflRdBEEZ8cH79impv8noE5komyIouSiaFn8OdBXzn2ADetdZDqg-yaYWHTGu7Q4ySCPoKaRAZ0BmT8s-FDbvbtDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل سوم پرسپولیس به نفت آبادان توسط اورنوف (84)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/108201" target="_blank">📅 18:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108200">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4da4e50a3.mp4?token=rIyL6R-DRk7S8DH6byGHw19np-4J6lqUlUAI7j1-zA3o7HcJN1AE8VOQsKkKAB8udV-thXlRhJkmR2_NWuudtn9r9_oUqmZo1Ywz-dm_lgGuJxDv2GP3d6xnoLek3CVY_nRxwBF9bJofTF7lTC_mH_x_MNHsW651LoNoy1sKTzbIKN5xYvcjAPZK8uKBAXqecQ-VnmkCWz64_ezkWL_YgiVoG_0k3LZXRgW9fMvqhZqtLWcDi2qvCZFNyIIh_beu-4Z2sk9Ps4Ypscp3OJ4jghGJfLxj11IywXW2skif9P0jZh80gC9AOrvIszPXX8MmvNpxdy_tVqZ_tWT0XtXfAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4da4e50a3.mp4?token=rIyL6R-DRk7S8DH6byGHw19np-4J6lqUlUAI7j1-zA3o7HcJN1AE8VOQsKkKAB8udV-thXlRhJkmR2_NWuudtn9r9_oUqmZo1Ywz-dm_lgGuJxDv2GP3d6xnoLek3CVY_nRxwBF9bJofTF7lTC_mH_x_MNHsW651LoNoy1sKTzbIKN5xYvcjAPZK8uKBAXqecQ-VnmkCWz64_ezkWL_YgiVoG_0k3LZXRgW9fMvqhZqtLWcDi2qvCZFNyIIh_beu-4Z2sk9Ps4Ypscp3OJ4jghGJfLxj11IywXW2skif9P0jZh80gC9AOrvIszPXX8MmvNpxdy_tVqZ_tWT0XtXfAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل اول صنعت نفت به پرشپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/108200" target="_blank">📅 18:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108199">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aa65c912b.mp4?token=iV3zk6XcbA7zbW_FE7TG3GCl6tnToddRXGfx3Quzvs-Qrb2Ry6jjWre403iKuWXVmH4rKlbp8o05uQ_zO1T2-fwIXFZrLgfzmQoSAz1PdKL-YmwD4-tIB_Tg5_vTBIvhcKPmjY1Zt-VDExclsLu5qOc_RtnxgOZULGZMPxt--pHJi9owBfTPwfRVOJ8qDMSR7uZlvbvUcGPQiFeUsL6XYHLIC8ebPOAQUyszg_z1ewcCsAMyBZ-PHGoYAc2OsYdcl4vuZgF8ePiKZr9AMd3JzEM4sRNjmKg0WGLRviA0MGxn0JkWJtjvWBFnhpFNTTwW0iCZcMWGaEs0p43ezBbZLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aa65c912b.mp4?token=iV3zk6XcbA7zbW_FE7TG3GCl6tnToddRXGfx3Quzvs-Qrb2Ry6jjWre403iKuWXVmH4rKlbp8o05uQ_zO1T2-fwIXFZrLgfzmQoSAz1PdKL-YmwD4-tIB_Tg5_vTBIvhcKPmjY1Zt-VDExclsLu5qOc_RtnxgOZULGZMPxt--pHJi9owBfTPwfRVOJ8qDMSR7uZlvbvUcGPQiFeUsL6XYHLIC8ebPOAQUyszg_z1ewcCsAMyBZ-PHGoYAc2OsYdcl4vuZgF8ePiKZr9AMd3JzEM4sRNjmKg0WGLRviA0MGxn0JkWJtjvWBFnhpFNTTwW0iCZcMWGaEs0p43ezBbZLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل دوم پرسپولیس به صنعت نفت توسط علی علیپور
P53
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/108199" target="_blank">📅 18:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108198">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4b20c129.mp4?token=PUsRWG-c2oHsFFoXPtoseqBM4JqkI212he8ilOvMgt-knpi1dvcFWOVA_FJZBc8fxZiEHX6kbKRmeqYDtzmMir4_zs1RD-LsGlNSsl1clshLSNHI1sSDFaS3_g6d65AW4-hG_CqTkzsSbeRaOOopZ41LleOxbtQH0cQbo3hf3boHSRRoTSCBi25XAkAYXWXV34zd1BjggWkg3UHF0lC2LrzHjHt__ObwdNoJsmEfNRG12mzh2wViLcDht_xnw7TEo8ChopFQ0ePrEEQcNATApKmHeuh1lCuOlM1WngJlfkNje96AoyRm-VLNOHwwIyFIA4bWSLSxGor55bZ41ZcWQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4b20c129.mp4?token=PUsRWG-c2oHsFFoXPtoseqBM4JqkI212he8ilOvMgt-knpi1dvcFWOVA_FJZBc8fxZiEHX6kbKRmeqYDtzmMir4_zs1RD-LsGlNSsl1clshLSNHI1sSDFaS3_g6d65AW4-hG_CqTkzsSbeRaOOopZ41LleOxbtQH0cQbo3hf3boHSRRoTSCBi25XAkAYXWXV34zd1BjggWkg3UHF0lC2LrzHjHt__ObwdNoJsmEfNRG12mzh2wViLcDht_xnw7TEo8ChopFQ0ePrEEQcNATApKmHeuh1lCuOlM1WngJlfkNje96AoyRm-VLNOHwwIyFIA4bWSLSxGor55bZ41ZcWQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اعتراض شدید تارتار به پنالتی مشکوک صنعت نفت
🔴
@Perspolis
@RedStarFc</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/108198" target="_blank">📅 17:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108197">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3013266bc8.mp4?token=fxE9lItGbVasXWt5SDva9QDPw2gUufxio-KrN_rRaIcWDVBz6efmrALezoLsyM1iS-bQV7ZM5YuMuYoIngNq3eLs1cdJk8mHf8Mqn3S91WkWNnhmBWTUxgvgCNxCqnKx8uMvLj92hvVzNiffl92NEInIcjtXw1orh2d_dW3_fWbgwqTdYTQqnl9pis7f3UhV7iY0qiY0i94Mps6HhkseB0oDrZ74EG4CJIGFpR7Xq-VVHUKMlpx5DXsu9GPZvMUfCl02UKcfOs80a6snHaflqAhPkANBf7mFpHuskThbJHGUvAd22KN4xdYaHkcUUIUgM9_S-PrHClolfTIIwmRSZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3013266bc8.mp4?token=fxE9lItGbVasXWt5SDva9QDPw2gUufxio-KrN_rRaIcWDVBz6efmrALezoLsyM1iS-bQV7ZM5YuMuYoIngNq3eLs1cdJk8mHf8Mqn3S91WkWNnhmBWTUxgvgCNxCqnKx8uMvLj92hvVzNiffl92NEInIcjtXw1orh2d_dW3_fWbgwqTdYTQqnl9pis7f3UhV7iY0qiY0i94Mps6HhkseB0oDrZ74EG4CJIGFpR7Xq-VVHUKMlpx5DXsu9GPZvMUfCl02UKcfOs80a6snHaflqAhPkANBf7mFpHuskThbJHGUvAd22KN4xdYaHkcUUIUgM9_S-PrHClolfTIIwmRSZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتباه عجیب سیروس صادقیان!
⚽️
⚪️
گل اول خیبر | امیرحسین فارسی '35
چادرملو 0 - خیبر 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/108197" target="_blank">📅 17:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108194">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‼️
اعلام پنالتی به سود صنعت نفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108194" target="_blank">📅 17:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108193">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef96e5b249.mp4?token=WxiMknWzP-1NzSFDIB_8DQwjqLN-Vbk15sxANJgtDPBdnIsddWCmSpknAwM2YpCLqlaqSEKcS7HKArGclGmVCJd9PWYPOq_qerUIDA_9TOQrFDqmMc3gW1m9re9L2BIGYmTnKUYogJ-6vfrA7Fho1MUclSOeqsprWxQ14ATaOSsVwYGH7BfJte1jPBdh3wD2KOpEnICZ7a0kBEvKUSolDkqktrHfqIentFSJHSFdStZJuboXZ0SHjl2TeJSJk87s9MgmGGLkXBNXNcdsQW9uzmGoGytvwqNZI-HQmBO9xj65_lvET6nKXjXP1TBFPiYLF3Dn8ruvAtc_dM1lTYI3jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef96e5b249.mp4?token=WxiMknWzP-1NzSFDIB_8DQwjqLN-Vbk15sxANJgtDPBdnIsddWCmSpknAwM2YpCLqlaqSEKcS7HKArGclGmVCJd9PWYPOq_qerUIDA_9TOQrFDqmMc3gW1m9re9L2BIGYmTnKUYogJ-6vfrA7Fho1MUclSOeqsprWxQ14ATaOSsVwYGH7BfJte1jPBdh3wD2KOpEnICZ7a0kBEvKUSolDkqktrHfqIentFSJHSFdStZJuboXZ0SHjl2TeJSJk87s9MgmGGLkXBNXNcdsQW9uzmGoGytvwqNZI-HQmBO9xj65_lvET6nKXjXP1TBFPiYLF3Dn8ruvAtc_dM1lTYI3jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعلام پنالتی به سود صنعت نفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/108193" target="_blank">📅 17:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108192">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60684bf96a.mp4?token=JKVn7QN0FnmqhvpE7HiTAiN_EkXEMWXDyhWDbHNejUVaVDEYjAFbFoPI2IaBeeLBsxVF41Pv2tfUtrwu4evNt4h6t81dINA7JJnQXK3iy8GzItbFb46X8mmug6zhvkFYsoja7R84aByh-KboNb8sl2DTc6pOBfE4WvA9vkQXpwXpO6CIDIsisfGdVDP22DWaodbGqeLLjFnXHSvvtxhXCXvqslqQieYCMg1FuhUmB-Mt28usLqPUN-aDTFtIwO7oNj6f8Lcdl_-60ludIliahWOho1YxXP_8Rxxy8kvjk4haN9xFe1ATS_fgHtrXJmtz828VujDGTs2JsvOeFIwtzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60684bf96a.mp4?token=JKVn7QN0FnmqhvpE7HiTAiN_EkXEMWXDyhWDbHNejUVaVDEYjAFbFoPI2IaBeeLBsxVF41Pv2tfUtrwu4evNt4h6t81dINA7JJnQXK3iy8GzItbFb46X8mmug6zhvkFYsoja7R84aByh-KboNb8sl2DTc6pOBfE4WvA9vkQXpwXpO6CIDIsisfGdVDP22DWaodbGqeLLjFnXHSvvtxhXCXvqslqQieYCMg1FuhUmB-Mt28usLqPUN-aDTFtIwO7oNj6f8Lcdl_-60ludIliahWOho1YxXP_8Rxxy8kvjk4haN9xFe1ATS_fgHtrXJmtz828VujDGTs2JsvOeFIwtzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل اول پرسپولیس به صنعت نفت توسط تیوی بیفوما در دقیقه 5
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/108192" target="_blank">📅 17:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108191">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b705c5cdea.mp4?token=SKhM2DBZuQjvefSr2zz4gG4As5xLJyIRC0g5jCjwOA_l7jBd-zgQXfKpc1mNvNpH6hCS1TODAAMRFnxp4xMose9x28AGMblYIxly4imqQHGJKUdte34XKee-7F1BFxceYhbk4EY-_qZ8pZqt2IJu5puXqUBgxukayEF_uN2y_O5tELREDrYw91XcA4pXtZQhB4tgRsvLMspIcg3tm5huP_bHe5Y-unR4G-4NFzKWC0kmWeUItcw32JzsXKYGCK7SbaSiCyVEF9i8w9XPlr3QBY2let8BYCY8K2kpfetcaNLZvDYWdNrfY_SB_W21-jI-pXm1Zkm8nWEUr4-oCyNV3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b705c5cdea.mp4?token=SKhM2DBZuQjvefSr2zz4gG4As5xLJyIRC0g5jCjwOA_l7jBd-zgQXfKpc1mNvNpH6hCS1TODAAMRFnxp4xMose9x28AGMblYIxly4imqQHGJKUdte34XKee-7F1BFxceYhbk4EY-_qZ8pZqt2IJu5puXqUBgxukayEF_uN2y_O5tELREDrYw91XcA4pXtZQhB4tgRsvLMspIcg3tm5huP_bHe5Y-unR4G-4NFzKWC0kmWeUItcw32JzsXKYGCK7SbaSiCyVEF9i8w9XPlr3QBY2let8BYCY8K2kpfetcaNLZvDYWdNrfY_SB_W21-jI-pXm1Zkm8nWEUr4-oCyNV3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
هوادار پرسپولیس: به عنوان یک لر بختیاری از بیرانوند متنفرم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/108191" target="_blank">📅 16:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108190">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74fffee2ce.mp4?token=uBjNghlWDcrAAr_V_7fTDfHdT3jywcjBwZa2mLW1oI5LGgDVXBlVjCpTlkMnLulJ5eW2RDmjL8WJW2VZkSZ886unmdYM2vM8XkeXrPocGRBeIv_L8qsUKIm0l4AjUeUG8zUW9YDQGfz0GOjEvwDQiB7G5zQt0zYu1o23CfjWJIsPdsykugKcaG-lTs9ThvuqQ2TBJ9mofFWAt3SFKIzj7qkR67cwcu5HYXu3mHlnNvmfmInrPf8Dr4HxySYhL8nJthZthH7Zr1HbaZX0NSrKGmsity6Jl99m--boIN6BDiN4X-NXNgTeOazlxflHMRsWCC0OI_YswG7QFljhdcn3OWNKE9ihiOk_UqXedNnZuvkRb_i6uZAb41MIEvTA9r0vMthrP5PcU-5gA-TsG0rPBd94lZuqAz6PqP3UwRvuYZd3lHAPu0jFAbPYtSVv_x2ffO-JKJaeNe4nUP_hRX6EFGyV0Ad0xeXhVRkv6liefdsH-Zo5gmcZ9a1wqfRtZL0qE5Izvv4MxaK9DJPltgeBB0JF-ThOHc1EQ-FgdZ3nVPt2-jHvY_BBrNBCBCOsd-_JMkMVpfGfg3TKM0wI6cbdwgfEEVTY_ciRwNue-ALM11XXi81lwd67RTtKv3Jzys3oiTIN3v4NlG8BjEXo5HSLZVKVaVEdAhhXD8ENMaJS67M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74fffee2ce.mp4?token=uBjNghlWDcrAAr_V_7fTDfHdT3jywcjBwZa2mLW1oI5LGgDVXBlVjCpTlkMnLulJ5eW2RDmjL8WJW2VZkSZ886unmdYM2vM8XkeXrPocGRBeIv_L8qsUKIm0l4AjUeUG8zUW9YDQGfz0GOjEvwDQiB7G5zQt0zYu1o23CfjWJIsPdsykugKcaG-lTs9ThvuqQ2TBJ9mofFWAt3SFKIzj7qkR67cwcu5HYXu3mHlnNvmfmInrPf8Dr4HxySYhL8nJthZthH7Zr1HbaZX0NSrKGmsity6Jl99m--boIN6BDiN4X-NXNgTeOazlxflHMRsWCC0OI_YswG7QFljhdcn3OWNKE9ihiOk_UqXedNnZuvkRb_i6uZAb41MIEvTA9r0vMthrP5PcU-5gA-TsG0rPBd94lZuqAz6PqP3UwRvuYZd3lHAPu0jFAbPYtSVv_x2ffO-JKJaeNe4nUP_hRX6EFGyV0Ad0xeXhVRkv6liefdsH-Zo5gmcZ9a1wqfRtZL0qE5Izvv4MxaK9DJPltgeBB0JF-ThOHc1EQ-FgdZ3nVPt2-jHvY_BBrNBCBCOsd-_JMkMVpfGfg3TKM0wI6cbdwgfEEVTY_ciRwNue-ALM11XXi81lwd67RTtKv3Jzys3oiTIN3v4NlG8BjEXo5HSLZVKVaVEdAhhXD8ENMaJS67M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
صحبت‌های هوادار خردسال پرسپولیس: اگر یک بلیت داشتم که یک بازیکن را پرسپولیس برگردانم، آن کریم باقری بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/108190" target="_blank">📅 16:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108189">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0df85fa87.mp4?token=BVlVlbs1Jk1u2P4aSQYteHRt9Idngzj_byIjVZ0v2KbvajFTWorneqp35CGUe-TZJ5YE9aq7Tv7fyX4-DgHfIa6o_SRAWiYnhk0okEIjX7fRpXpU6BpGNU9zfaNNoxqWT21Cs9JZVj1VKvBsOK6iLgwRHNKaMGym2jPz-bUHN-5E4baUynubGOU4uUK3vO-KSTvmU0AxtOCToPm5aRNAFuYwxGbh0mJpUwqey_OaxzUX-1YO-T1wUMP1F-RL3olzkc9r9Io8r8kXXPsrHWSFHH9Ryw6tWAMPGI9kXhGRrbYefiwfCC2L9TYgx_3Gcj7_qMZmBNVczlDyQkS8bGOTyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0df85fa87.mp4?token=BVlVlbs1Jk1u2P4aSQYteHRt9Idngzj_byIjVZ0v2KbvajFTWorneqp35CGUe-TZJ5YE9aq7Tv7fyX4-DgHfIa6o_SRAWiYnhk0okEIjX7fRpXpU6BpGNU9zfaNNoxqWT21Cs9JZVj1VKvBsOK6iLgwRHNKaMGym2jPz-bUHN-5E4baUynubGOU4uUK3vO-KSTvmU0AxtOCToPm5aRNAFuYwxGbh0mJpUwqey_OaxzUX-1YO-T1wUMP1F-RL3olzkc9r9Io8r8kXXPsrHWSFHH9Ryw6tWAMPGI9kXhGRrbYefiwfCC2L9TYgx_3Gcj7_qMZmBNVczlDyQkS8bGOTyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بانوی پرسپولیسی: به خاطر پدرم استقلالی بودم اما زود متوجه بزرگی‌ پرسپولیس شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/108189" target="_blank">📅 16:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108188">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1D-5-HWuzrOjwwpHpcowc710Sscf2IaHx7eZI_PtB_oV-6b_JPQB651Csn63vpWP3XsMVllKsiY204yeLtmf5Tui8vSzhwrUPX5EE85pBCClon6jC-Lpqg1l5L5R-4U57e5Y8uxfd7iw0rFmaJU5ypri1AcCPhIR4DiJ7yddp-qdH05zXJP_40_FBEHfnWgopohHdLPYVsZwg2kJDS0PQhDwTdCvMwrZTVHzhSDUIuuZgUGi9vBvNxb8VCPwrhlxUruNj9vlYiQFYTKYfGVadcLgMn-qJlBgrodtrNadSbV4vkWmbo2s7KxTV8pUwrPSBVpdeYXoZam3_OEY27X1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
لیست رئال‌مادرید برای بازی با ویارئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/108188" target="_blank">📅 16:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108187">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c488f1154.mp4?token=qysuH-V55IJ9sMI04sRsL3RL0fJeuY2nGIWrLUM6z74rj64GYfQZMt8ZvFAAKWZbVqzS2Qyis-8X-0nGGfbUK8WThAgYMpUmcIkQPyHFOdYadRqnz-CoBC2QE0r71EXKhRALmkORVVQYVl81x5mOZlXcO9CKbMbQtWHpU2ESp9A5BqeSdfSatgNpGENxlAMkW7lVtyTLymNZHzZWllJyToHFMZDQHq-LchMVzxPdSbqz7XdUoJgD83Cqdda8Y6Nan9xTrpgWylzmZC9lFu8BznZTvL6RnnFpI8P7VVFI4eC9o2-LayDk4vbysUwG0UMo43OiG7iyMKQWnfJJHTZyAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c488f1154.mp4?token=qysuH-V55IJ9sMI04sRsL3RL0fJeuY2nGIWrLUM6z74rj64GYfQZMt8ZvFAAKWZbVqzS2Qyis-8X-0nGGfbUK8WThAgYMpUmcIkQPyHFOdYadRqnz-CoBC2QE0r71EXKhRALmkORVVQYVl81x5mOZlXcO9CKbMbQtWHpU2ESp9A5BqeSdfSatgNpGENxlAMkW7lVtyTLymNZHzZWllJyToHFMZDQHq-LchMVzxPdSbqz7XdUoJgD83Cqdda8Y6Nan9xTrpgWylzmZC9lFu8BznZTvL6RnnFpI8P7VVFI4eC9o2-LayDk4vbysUwG0UMo43OiG7iyMKQWnfJJHTZyAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
هوادار اصفهانی پرسپولیس: تیم دسته سومی هم پول زیاد بدهد، بیرانوند قبول می کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108187" target="_blank">📅 16:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108186">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f38bccfd90.mp4?token=o-9TmafPIyRAjJRxKM3EBmki0YcvioYW6pc1d0CblUimm2zSup0AH80szfw6IhrfN3Ht1RES1X3wUv21FHuI-RveXq_IvzDb9V3QYRuE_TU64nQhR9crq_auhunb6CbjSpsSw_G7pRH04QtoN5_KyDpBkmgj_hHuLK133NPNmbiWQABm56sLoR_xKSS9ETuF6Nkj4rbapYnR48oSKYMB97Nc-L0KRgE-1OMoI1kWJMNT5mBzCXcR_HYP4aCI1FzB4h7vquKEqwb_jLq6rnDCO9jE8_T6NMFu-pWtfoKfKYy2hlJI7D18IkyYSpZ9ODUR7H-GDQxSvzCmKyLHGtkn-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f38bccfd90.mp4?token=o-9TmafPIyRAjJRxKM3EBmki0YcvioYW6pc1d0CblUimm2zSup0AH80szfw6IhrfN3Ht1RES1X3wUv21FHuI-RveXq_IvzDb9V3QYRuE_TU64nQhR9crq_auhunb6CbjSpsSw_G7pRH04QtoN5_KyDpBkmgj_hHuLK133NPNmbiWQABm56sLoR_xKSS9ETuF6Nkj4rbapYnR48oSKYMB97Nc-L0KRgE-1OMoI1kWJMNT5mBzCXcR_HYP4aCI1FzB4h7vquKEqwb_jLq6rnDCO9jE8_T6NMFu-pWtfoKfKYy2hlJI7D18IkyYSpZ9ODUR7H-GDQxSvzCmKyLHGtkn-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
هوادار پرسپولیس: جام فصل قبل؟ هیچ کدام لیاقتش را ندارند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/108186" target="_blank">📅 16:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108185">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
⭕️
🇮🇷
براساس گزارشات اولیه، مصدومیت یاسر‌آسانی جدی نیست با این حال سهراب بختیاری‌زاده هیچ ریسکی روی این بازیکن نخواهد کرد و زمان بازگشت این بازیکن حداقل مقابل گل‌گهر است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/108185" target="_blank">📅 16:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108184">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f4416442e.mp4?token=cVdugGkYJVE3Q50-Vli325em4a-gmWcHcvayvXUMhT7HVgfjMW6lV_OoQg-dQJrgGr0ZzekVMds6g6rLJLDeRU9Qu6bRighmucA9v6nBDQYu1Rc1AWMeAnaYf2fRpvgOqwwvpVR1EmS4WOvagDo8rj725bU7rT_Pr2rnDS9JQj31PyUaEPcXn-jFLsGpaxVjBY1QgUkaJoX-_ibtD7Bu8DGv_vdTxvisbh6iUdoUuP1ry85INCGSgWap3-H2dvyiwvXOPGEtzynEM5guC6l7lgcDHgMGoTyZgzfDy5kc8nM2k0KfAyz4T21g-9sCVKBsN0kriFDbgHGTsbgU9rnDyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f4416442e.mp4?token=cVdugGkYJVE3Q50-Vli325em4a-gmWcHcvayvXUMhT7HVgfjMW6lV_OoQg-dQJrgGr0ZzekVMds6g6rLJLDeRU9Qu6bRighmucA9v6nBDQYu1Rc1AWMeAnaYf2fRpvgOqwwvpVR1EmS4WOvagDo8rj725bU7rT_Pr2rnDS9JQj31PyUaEPcXn-jFLsGpaxVjBY1QgUkaJoX-_ibtD7Bu8DGv_vdTxvisbh6iUdoUuP1ry85INCGSgWap3-H2dvyiwvXOPGEtzynEM5guC6l7lgcDHgMGoTyZgzfDy5kc8nM2k0KfAyz4T21g-9sCVKBsN0kriFDbgHGTsbgU9rnDyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
کنایه هوادار پرسپولیس به گلر سابق: وجه اشتراک ما با تراکتوری‌ها اینه که بعد از 3 سال می‌فهمن بیرانوند چه کاره بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/108184" target="_blank">📅 16:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108183">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TynkvTNT-0EtP8RVTZudnUIOoBRklG-xP48mTIVFSMl9SANbYR-wSnYgGAduQrIy4GouaQe_EVMK_PcIOQbLzauGRuOWwri5wu79xN-26aXn5Y0qC37GT7gO4FW27E-jCGpjeRGlO4gWuGUW-1BrUKgMGUKFIkiP-jiR_O4NPUuJKbBgfAS5ij2SMMta30li69NA0tmbLEuYGfv66dF9qmhc77m0PjNIwiuq3YF_ioHBrpwXYaBKmq0vFE7b_ckTMEwzWqojlZhB5CBkNw6jIUc_Fc2VT0IisoPQjn6xtbwU47K1M77XLyk-UHFMvTPBieAefavPdgIr4fDF1_uMxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
اعلام ترکیب پرسپولیس مقابل صنعت‌نفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/108183" target="_blank">📅 16:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108182">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a8dae1c8a.mp4?token=snEmlQysn_BpXEW-hRbtCgcW0r-qaK80B80-fVavO2daFNqwc7ENW-vr6RBM-JHyfyyiOvbI-X-vEvd0eaZpmGl2XoNIQJ7L3QUTAXmpgPB_wNRhS4vZ7CP4XhGOb8tP9TaNCBtlEFH5z3AG9o_-NkwBlrbFpt-4heTbLj7eVr1GsQCALhBa3b5lO44YZS8QmmdGuJCbeqVtPqASUww-AGw2ZgHaD5vuLL2mEIT5xsbVE-0mnnkTKymLQegT-J7vPPzkvGgw74npVxft0aWNN5_lyzDBwwooFKN4-Jzu_7KpyV4ofqAw-tx8WxofkcBA_mAkxMHYot6YwLbH_RgfWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a8dae1c8a.mp4?token=snEmlQysn_BpXEW-hRbtCgcW0r-qaK80B80-fVavO2daFNqwc7ENW-vr6RBM-JHyfyyiOvbI-X-vEvd0eaZpmGl2XoNIQJ7L3QUTAXmpgPB_wNRhS4vZ7CP4XhGOb8tP9TaNCBtlEFH5z3AG9o_-NkwBlrbFpt-4heTbLj7eVr1GsQCALhBa3b5lO44YZS8QmmdGuJCbeqVtPqASUww-AGw2ZgHaD5vuLL2mEIT5xsbVE-0mnnkTKymLQegT-J7vPPzkvGgw74npVxft0aWNN5_lyzDBwwooFKN4-Jzu_7KpyV4ofqAw-tx8WxofkcBA_mAkxMHYot6YwLbH_RgfWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
کنایه تند پهلوان پنبه هادی‌چوپان به منتقدان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/108182" target="_blank">📅 15:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108181">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa24f6046.mp4?token=uG2npFCqHAzhDY2AeTIsl-9e7z2U2JkDpiatX3-X9cRqEjvSBt8oLecv3wEMymm1T1xRci4Z7cji27NVzlRrFWhSu9x5njQbwrHV68cLeUdSVFrHiU1HZvKNuqvlAqbbNeFbMixMGD2VNJGZUkj_RPszBrDJcEgS86tzFXtPCfKEHo6DQbrEh0XYmSfeN_JH_wau6abh4Y1j_YHFf14EjZIcH3V-hbA0vu0_Qfc74_R_ijZZR99qa-HHBgITsmDplGQreZsTkrdZveSdDPz2B-CsvDIq-2EAgspmG-RcQ_KTcDoyDwSIVF8EISfiM03MPRKYshklHZy8-qgHBzLfxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa24f6046.mp4?token=uG2npFCqHAzhDY2AeTIsl-9e7z2U2JkDpiatX3-X9cRqEjvSBt8oLecv3wEMymm1T1xRci4Z7cji27NVzlRrFWhSu9x5njQbwrHV68cLeUdSVFrHiU1HZvKNuqvlAqbbNeFbMixMGD2VNJGZUkj_RPszBrDJcEgS86tzFXtPCfKEHo6DQbrEh0XYmSfeN_JH_wau6abh4Y1j_YHFf14EjZIcH3V-hbA0vu0_Qfc74_R_ijZZR99qa-HHBgITsmDplGQreZsTkrdZveSdDPz2B-CsvDIq-2EAgspmG-RcQ_KTcDoyDwSIVF8EISfiM03MPRKYshklHZy8-qgHBzLfxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
همچین ذهنیتی برای همه آرزومندم...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/108181" target="_blank">📅 15:15 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
