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
<img src="https://cdn4.telesco.pe/file/WACgA0NVTX6Y2xPkHc8dvNkHSGsVMvasC42NwsgQjelCDCu3OdvJFXwNv4MuYcbxmEX8GzeyZz-V5g_sEKh5t-yAhV5EgccDmUl74wcSmdnWUi2K816-S3UIN3NeEGD8kaElKBHm9r3O70oAzF6BXJE3REOYlL6Uhw0KDNKk-kU3V9Il42oxqEcrmZ20ZLJGfVpEvK-6wZ7wtccDv43M6V5liTyzFTQnpRduKoMKeBW_DOihwfUkpKkjFyDRsvX9ptFDaFNYYHuZvCLOD-wquYhAsymnji_tTgrA2pXAv_nRGkmvcSyJA1b2A9m_f20pJUO5HIqZLEKz1Pv5p7ulIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 38.3K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 13:12:49</div>
<hr>

<div class="tg-post" id="msg-8427">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دوستان ربات جهت آپدیت و انجام سفارشات لحظاتی خاموش میشه
❤
✨
🙏🏻
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 366 · <a href="https://t.me/IranProxyV2/8427" target="_blank">📅 12:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9OStAZL43UssOZ7AsLbPNmpkD0ZUV6HQjI7YagMR3bNOzAW4DGuqIhZOl97tvRX5jvpWNM1NjoNfTWl16Bfokw3nuile_paN-3NVd_Nuxrs6hKQf9ruSmfxXg7xGA9YJJKr02xN25jwMQ80o65k3n6p7b1xh_SCbDOxxswXBZ4L1FyfMpZtpF7itBvD__REDjY43rc02rjupMOJ5aHai6hPew3igDUiI-Rp00CJW8J4xX_peJdDnK4rULlz2mCKWwsR7gL3nhotNalRoOcclT-rX1pu3R7n0eup47ZV_MuNyGpVOwQrhz5C3Hc_9UdXW0SqjXHwiGWdD_BW3bJzHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 97 · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=G9CiRQdRrf_z270tKeb_1nhCI4CC7DJ0Ra7a1e0RXkkHlZW8PxSeVnNizm-UbAv5qplbfpIaiRg7thVypmDAiSpdqd7X90qBFywvLxNnvJfTNjUX87t0MlkqFIi4hXYI1GSZpT06DtcWtiQIw7cY3gbLd1RpsU12VvmsLe7hHbKg4ExEZyPLEUtilDJpFlIls0SqCnNhXQIffMZHtyqsd6TezlBHzaGz5ahW2G1-iP-az1wQDTRWYVDNbGRd7-ffqdFPnYOSV0f85iuauimuE60SdkzYpLWEAER1xLLpEqcgm3mN42_kTg-VmDUAF8RZRcvNRIdxggceXB6UQZ8upUod0oDdUyJrhwQFA_-3uUQLBC-_ZJr8jyyw6qyRD_YkXHnBbOQhXUx4e7p6sSpMoiz1xTbja0sqrr_WBXtya2tnq8CmMkrgPZPW8lByAAcuFdFRFUA6lfUv0Sf1tElriYNAuvALmaNLprrF41Feykn074jZbgvklRLPOPvbMQFevajiIB0Wh7d3j-yRGwqWhzonS3daVfH_I3qa1AhdwtCTD7AOCUM2oMGDQuUhXyaDzUZpIEc6R_gCM68YZV448pONDRcMPg3llESM39AquAZuC_qsB9KoY_ZVYxgRdenAtOsqMmtrxJKsua0OmNZ7w-p69qjEuSvTb9bdxmIYn-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=G9CiRQdRrf_z270tKeb_1nhCI4CC7DJ0Ra7a1e0RXkkHlZW8PxSeVnNizm-UbAv5qplbfpIaiRg7thVypmDAiSpdqd7X90qBFywvLxNnvJfTNjUX87t0MlkqFIi4hXYI1GSZpT06DtcWtiQIw7cY3gbLd1RpsU12VvmsLe7hHbKg4ExEZyPLEUtilDJpFlIls0SqCnNhXQIffMZHtyqsd6TezlBHzaGz5ahW2G1-iP-az1wQDTRWYVDNbGRd7-ffqdFPnYOSV0f85iuauimuE60SdkzYpLWEAER1xLLpEqcgm3mN42_kTg-VmDUAF8RZRcvNRIdxggceXB6UQZ8upUod0oDdUyJrhwQFA_-3uUQLBC-_ZJr8jyyw6qyRD_YkXHnBbOQhXUx4e7p6sSpMoiz1xTbja0sqrr_WBXtya2tnq8CmMkrgPZPW8lByAAcuFdFRFUA6lfUv0Sf1tElriYNAuvALmaNLprrF41Feykn074jZbgvklRLPOPvbMQFevajiIB0Wh7d3j-yRGwqWhzonS3daVfH_I3qa1AhdwtCTD7AOCUM2oMGDQuUhXyaDzUZpIEc6R_gCM68YZV448pONDRcMPg3llESM39AquAZuC_qsB9KoY_ZVYxgRdenAtOsqMmtrxJKsua0OmNZ7w-p69qjEuSvTb9bdxmIYn-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 807 · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8424">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 776 · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=IhtntVWSJvvty0jc2e7VSsEl5h7XB4EKZ0xSoqIc9hE-z9EidVGOnsfGRQbkMhl4a7LylY7XAs-p5HmtPmOaVzAySHWoEB7Wk9mcC08Jy40JRrCKFrYuU2v3UjA5usHwu7zSzHTZBfgLSZegWA4yGW4meC-o-qES7nXwVrUxKzIrDr4DPQKvWyHXaKjPi1FpzOAZ0G7nU3Jh43BXl1NLAuQY38wClA4OO97X91mBjsUj5qe24PDd7lnusBJK8e-ppl72Lu-rTFr-Yh9gEnEugi2Jy6MYSOfAzwhfvmDTWKxJTdGRQg-Rqh69pLWAA6JUxyG0_mokg2VlnslNlV7LgCsME2Xmk-dnF_TvyS6KxrC0mdBjlZ9Zme_KfucBoDCRMte5aQKzkTfjHBGE0BQMStAmNc_sjmVsbhmKltjOUDIZwe9sA1iGHYvchpOBLkQi2dlL7iZasEPHIDcaypKY4D60T8ATmbLod4if9Pv_zTb6fNgki9EzWReLjJ7NKxgG1uDb4x8h4WgbL0LKvM298lWR1kunuLN6teIgUx7kiv0_eixhgw8WVNs2fbqT3YlKObt7W-e_gg1fsTlUKzVtdW-9Z2JCw3M_vdIAwj-3KQHDIRTr_N46u7qaxbsAdokAFA0QGFt00PcY9Ru_a9vcyCo8Zj4PAcRhEzgbm9Yjq_o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=IhtntVWSJvvty0jc2e7VSsEl5h7XB4EKZ0xSoqIc9hE-z9EidVGOnsfGRQbkMhl4a7LylY7XAs-p5HmtPmOaVzAySHWoEB7Wk9mcC08Jy40JRrCKFrYuU2v3UjA5usHwu7zSzHTZBfgLSZegWA4yGW4meC-o-qES7nXwVrUxKzIrDr4DPQKvWyHXaKjPi1FpzOAZ0G7nU3Jh43BXl1NLAuQY38wClA4OO97X91mBjsUj5qe24PDd7lnusBJK8e-ppl72Lu-rTFr-Yh9gEnEugi2Jy6MYSOfAzwhfvmDTWKxJTdGRQg-Rqh69pLWAA6JUxyG0_mokg2VlnslNlV7LgCsME2Xmk-dnF_TvyS6KxrC0mdBjlZ9Zme_KfucBoDCRMte5aQKzkTfjHBGE0BQMStAmNc_sjmVsbhmKltjOUDIZwe9sA1iGHYvchpOBLkQi2dlL7iZasEPHIDcaypKY4D60T8ATmbLod4if9Pv_zTb6fNgki9EzWReLjJ7NKxgG1uDb4x8h4WgbL0LKvM298lWR1kunuLN6teIgUx7kiv0_eixhgw8WVNs2fbqT3YlKObt7W-e_gg1fsTlUKzVtdW-9Z2JCw3M_vdIAwj-3KQHDIRTr_N46u7qaxbsAdokAFA0QGFt00PcY9Ru_a9vcyCo8Zj4PAcRhEzgbm9Yjq_o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 922 · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8420">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWx-Y7aWHisDRTmCLrzMwLEmyD1DoxOtOfRUANo2G1KuGJn9YhJmWa-h9l4_upt2hsy5ftMl9jF70yN6QrBD6t8kmXqXMKDlmqP28bAHWHg0L44hBtmcz_dnh0oKMAUHIkMLJqKrUtCh16yE4ZwmYb-S4DTDk4lf5F0dHpHqUEJ8bbTNHtzUQm-VtHn6PwKQkFSLYhRElKuInKRKD5l6VdlnQKjVgAGbNy6JMfePwWYNtaPtzjA9D9cUMPNMNqsBsc2vsBjrUNddX4zwJYZaXxz7skVAhDFgmXByLKHYpZHzDdouxGG7Ws-3t6ZHGtrukN4361ZcLAVjRSqbPaxnQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=qoOjrqQz37z5zedvs7nCeHgoq_iY87AN-IviTVT5rBW0vPRylt57Djh2nGd0JdzRr7uP9T4d_p4AwC8ZEuYAPIgym2DpeV45WEQPPyhTt7s1ZaHySNDcuViM3bZk7cLFagzcNgqmQv6J0n7DiIuMtPUQ2Dc9rj57426oO8qEXsSEd20bi1DWJDV404a6CKUBi4crxtqCCTPRESn5xVwhHUmxc1qLofN4jz9H7gAa7OazVw-KqCF6ojOa3VRqSqoBkm531U7e7VX6zyv-EGWd_NDxjbBsQlxX28sITivqbQ2pjhMoov7s4sKk1PwtjW40q0yeOd48Ou_s-AxqigLxFrWZk-oNJMXzgt4g8Vwkmx2cni341Rg_EsG__DTihw3_hsFui5DO_rr-MPnJkNLDCWWRNrxafVOCCqINq39FKU203auAJWz4b2Bg07uc3Dqy1T8_i0D28-8uli08bELjTsJYu66n3UxbUZzaMAnTPy1oRuNc_pv8UhlloO4tE_aZONPNK7PorYPbe0Uux6AgAhlVn5dqY3Z5vrXPZQPU8kyMWrnBXxaqF7aXcCIT6JTOn0cEgvHKeDnrdl6R2vGTYmHqt-Ncv384ND5LaFVaomKanQ8SdcNLv2tijzAY6OqgTdQtog89bFSK64n5pWLIWIlIuwaS7nl6f-C1ZXIkGY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=qoOjrqQz37z5zedvs7nCeHgoq_iY87AN-IviTVT5rBW0vPRylt57Djh2nGd0JdzRr7uP9T4d_p4AwC8ZEuYAPIgym2DpeV45WEQPPyhTt7s1ZaHySNDcuViM3bZk7cLFagzcNgqmQv6J0n7DiIuMtPUQ2Dc9rj57426oO8qEXsSEd20bi1DWJDV404a6CKUBi4crxtqCCTPRESn5xVwhHUmxc1qLofN4jz9H7gAa7OazVw-KqCF6ojOa3VRqSqoBkm531U7e7VX6zyv-EGWd_NDxjbBsQlxX28sITivqbQ2pjhMoov7s4sKk1PwtjW40q0yeOd48Ou_s-AxqigLxFrWZk-oNJMXzgt4g8Vwkmx2cni341Rg_EsG__DTihw3_hsFui5DO_rr-MPnJkNLDCWWRNrxafVOCCqINq39FKU203auAJWz4b2Bg07uc3Dqy1T8_i0D28-8uli08bELjTsJYu66n3UxbUZzaMAnTPy1oRuNc_pv8UhlloO4tE_aZONPNK7PorYPbe0Uux6AgAhlVn5dqY3Z5vrXPZQPU8kyMWrnBXxaqF7aXcCIT6JTOn0cEgvHKeDnrdl6R2vGTYmHqt-Ncv384ND5LaFVaomKanQ8SdcNLv2tijzAY6OqgTdQtog89bFSK64n5pWLIWIlIuwaS7nl6f-C1ZXIkGY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرعت سرور های همین الان
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBlumzh9Exsa8IxMFh9F-hfwJUF3vogGKif6yENuZJjG7SsMYxN7TFxUaruXSVy67Yrkw5VLWXPChU2_Xr9-oyRGmYf5zWiqPdYSn1MPDf3e14h9SmVAGl6qM_6ubHpbGBdyrcVj-3yO_bv4juEV242K-CPC2pCYatJyLzmLK7QpLVKVIsqBBVgx1Msqt0QaUwEKmwB3NW2E-DzGYIQh4Ejn0BQ4CvaqOYOseMHELL18WoOSfxjfk7Y5GmhgQyG53wP3vuzSaexfZbkEFzY2w8rO6rkDM4LfinGKrvceE5bfKpnRT_1eJSpVmBpKctgO7gYPpkcS-cbpWfEmoJ9s_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkX-r2MhN9uc8KOT500f0f3YJxumiEdw0bOrwH5Sgc9LHn-ZdUJ6NbTwWfB0Phuy_xIerfL5zW_tRt2gt5drm6mWBkzfojV4YLUKEPNFCi61GmMCpijxV_WVeBM0XOCXRWsSFK8DC2HGRASEukaaAp4TukJJvVhRq2yvAveumoxIeD3X8a4eIUsQyKVegYRBPSxaeL1-ZJp0CDprgJIOPBcMUXsw13Z9SF4NbpTqeJh7LucNTRjmtv9vQdqmMXGE4Si-2HIDrovQsBJsPhRkoAbFXWbUipc7Yxrro4gWyQjtaXETEmuu8kgRFLEv37rfVjwAPNo4STzJx0uFYtPiEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=180T
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=MLjpDPySDvi7NWqj7I1Z61RI5FE8T3aYPiTTPKlAgYcNXZ0R5T0YMPt6OiwQRTGC-qlBy98LfwrTYQ-OcvmPd8dG9OU2tx0F6cQ_IncsUCdWMdm1pYW0VVRAnTqaNRd2jfBXBjLk3VNenlg1dyvAwb9tKzE7HX1EBvxz1BqJRqWo273HILsXONFroLteIa9dSA_zL6XpS-m34zT-rg0ok0-Jky4Mf2Gvyx-MIF5ax35TiBxLtgw1E_VrGV0oe1F6LxWSYTZBfC0uB1rfMb-_etiNPi-mK3WvMeEyIPWsJJ7oU4ag7VS85XwI5_YVufm-TGMmDT4sy8aMoc8F5rPd8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=MLjpDPySDvi7NWqj7I1Z61RI5FE8T3aYPiTTPKlAgYcNXZ0R5T0YMPt6OiwQRTGC-qlBy98LfwrTYQ-OcvmPd8dG9OU2tx0F6cQ_IncsUCdWMdm1pYW0VVRAnTqaNRd2jfBXBjLk3VNenlg1dyvAwb9tKzE7HX1EBvxz1BqJRqWo273HILsXONFroLteIa9dSA_zL6XpS-m34zT-rg0ok0-Jky4Mf2Gvyx-MIF5ax35TiBxLtgw1E_VrGV0oe1F6LxWSYTZBfC0uB1rfMb-_etiNPi-mK3WvMeEyIPWsJJ7oU4ag7VS85XwI5_YVufm-TGMmDT4sy8aMoc8F5rPd8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمامی باگ ها و.. برطرف شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMT7xdiyI5I_QkWz0mUhyR034Jx3EubqhBzB9Pu2w6Gn6ZzNwWrEJn88i-AY3gzcUg2WgAARQtJnwiPhaK3vf2lfD-RC74FZY1MVBiKEu9zarlH4a0pDfZ2H8zR77qHFf8FWCaC_DZTBuleCi-SBcQw44Kvw5KqNUglod8M94Rl8NY-vG4VSiW6rb66OwIoKCT820nRZ1C3H2k9BYlFY6Eh1Tv7WDV_sulaUUy-4dUyGdWvRdgyfIEuv-vpxrbWnJiIIrgGXhLzwb-HYgrumYjzl_D4v22gGSSWv5qzsJxQiJxOYChJ1-_6vNKOzogNjKB8hlRcqQwEi5YngF_6whg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=180T
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8406">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2261382e-40ad-4259-9564-33734d96cf5c@varzesh3.com:80?path=%2Fws&security=none&encryption=none&host=nobody.fasterspeed.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYQAi4NK01Ur8o868TWVrD0HpM3WCecUw_ZGgruAwzelibmUOQ4kqfSpeuy65q6Zd1Efvvqu78V3-cA3xXyH3zf7APf_y_RubQkb95TEdUMqzSV6d3-70RjcEVWpyWCsGU-CC7b9qyDpG8BsDN-U-o-V48sAsWMmRxuWYk_BcSdRKMkO_EM1wybzxoJ84kLDXH3M4v5wuVkg6X-SfbfPRD9eI9n71tCm164BymiPDIlt5A5ADmpCdI-9wY2cpvCYwqPm5P-1tKyv6xKXBd92peinKpmD3FT0Lem8qIkW2hAbdzNjZEg322tKkSB-DMWqCNt1Kakzi75Rr4tLG7m_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8403">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏چالش دو گزینه ای با موضوع  اطلاعات عمومی
📚️
‏
🥇
🥷
Sara: ‏(۱۶۵
❣
)  ‏
⚪
❌
⚪
⚪
✅
✅
❌
⚪
✅
✅
✅
✅
✅
✅
✅
❌
✅
✅
✅
⚪
‏
🥈
🥷
Freya: ‏(۱۳۸
❣
)  ‏
⚪
⚪
✅
❌
✅
⚪
✅
⚪
⚪
✅
✅
✅
✅
✅
❌
✅
✅
❌
❌
⚪
‏
🥉
🥷
hossein: ‏(۱۳۶
❣
)  ‏
⚪
❌
✅
✅
❌
✅
⚪
✅
⚪
✅
✅
✅
✅
✅
⚪
✅
✅
✅
⚪
❌
‏۴ )
🥷
Dystychiphobia: ‏(۱۳۴
❣
)  ‏
✅
❌
❌
✅
✅
❌
✅
✅
❌
✅
✅
❌
❌
✅
❌
❌
✅
✅
❌
✅
‏۵ )
🥷
- Amin -: ‏(۱۲۹
❣
)  ‏
✅
…</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8399">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏چالش دو گزینه ای با موضوع  اطلاعات عمومی
📚️
‏
🥇
🥷
Sara: ‏(۱۶۵
❣
)
‏
⚪
❌
⚪
⚪
✅
✅
❌
⚪
✅
✅
✅
✅
✅
✅
✅
❌
✅
✅
✅
⚪
‏
🥈
🥷
Freya: ‏(۱۳۸
❣
)
‏
⚪
⚪
✅
❌
✅
⚪
✅
⚪
⚪
✅
✅
✅
✅
✅
❌
✅
✅
❌
❌
⚪
‏
🥉
🥷
hossein: ‏(۱۳۶
❣
)
‏
⚪
❌
✅
✅
❌
✅
⚪
✅
⚪
✅
✅
✅
✅
✅
⚪
✅
✅
✅
⚪
❌
‏۴ )
🥷
Dystychiphobia: ‏(۱۳۴
❣
)
‏
✅
❌
❌
✅
✅
❌
✅
✅
❌
✅
✅
❌
❌
✅
❌
❌
✅
✅
❌
✅
‏۵ )
🥷
- Amin -: ‏(۱۲۹
❣
)
‏
✅
✅
❌
❌
✅
✅
❌
❌
❌
✅
❌
✅
❌
✅
❌
❌
❌
✅
✅
✅
‏۶ )
🥷
𝐑𝐚𝐝𝐢𝐧.𝐳𝟐𝟎𝟎𝟕: ‏(۱۲۳
❣
)
‏
✅
❌
✅
❌
❌
⚪
✅
✅
❌
❌
❌
✅
✅
✅
✅
✅
❌
⚪
✅
⚪
‏۷ )
🥷
Matin: ‏(۱۱۸
❣
)
‏
⚪
❌
⚪
✅
⚪
✅
⚪
✅
❌
✅
✅
✅
✅
✅
✅
❌
✅
❌
❌
❌
‏۸ )
🥷
𝘿 𝙀 𝙑 𝙄 𝙇: ‏(۱۱۵
❣
)
‏
⚪
❌
❌
❌
❌
❌
❌
✅
❌
✅
✅
✅
✅
❌
✅
✅
✅
⚪
✅
❌
‏۹ )
🥷
Paranoid: ‏(۱۰۸
❣
)
‏
✅
✅
✅
⚪
✅
⚪
❌
❌
❌
✅
❌
⚪
✅
❌
✅
✅
⚪
⚪
✅
⚪
‏۱۰ )
🥷
Robert: ‏(۱۰۲
❣
)
‏
⚪
⚪
✅
✅
⚪
✅
✅
⚪
❌
⚪
❌
❌
❌
❌
✅
✅
⚪
✅
❌
✅
‏۱۱ )
🥷
♧: ‏(۹۹
❣
)
‏
⚪
⚪
❌
✅
❌
⚪
❌
✅
✅
✅
❌
⚪
✅
✅
❌
❌
❌
❌
❌
✅
‏۱۲ )
🥷
Zaker: ‏(۹۷
❣
)
‏
✅
✅
✅
❌
⚪
✅
⚪
✅
⚪
✅
✅
❌
⚪
✅
⚪
❌
⚪
✅
⚪
❌
‏۱۳ )
🥷
✗ᏦℕiႺℍᎢ✗: ‏(۹۵
❣
)
‏
⚪
❌
✅
❌
⚪
✅
❌
❌
⚪
✅
❌
✅
✅
✅
✅
✅
❌
❌
❌
❌
‏۱۴ )
🥷
❥sheyda☙: ‏(۹۴
❣
)
‏
✅
⚪
❌
⚪
❌
⚪
❌
✅
⚪
⚪
✅
✅
⚪
✅
❌
✅
⚪
✅
⚪
✅
‏۱۵ )
🥷
Ахмед: ‏(۹۰
❣
)
‏
⚪
✅
❌
⚪
❌
✅
⚪
✅
❌
⚪
⚪
⚪
❌
✅
✅
✅
⚪
✅
✅
⚪
‏۱۶ )
🥷
Ali Moheb: ‏(۸۹
❣
)
‏
⚪
⚪
❌
✅
✅
❌
⚪
❌
❌
✅
✅
❌
❌
❌
❌
✅
✅
✅
⚪
❌
‏۱۷ )
🥷
Vista: ‏(۸۴
❣
)
‏
⚪
⚪
⚪
✅
⚪
⚪
✅
❌
⚪
❌
❌
✅
✅
❌
⚪
✅
⚪
✅
⚪
⚪
‏۱۸ )
🥷
ㅤ: ‏(۷۵
❣
)
‏
✅
⚪
✅
❌
❌
✅
❌
⚪
❌
⚪
✅
❌
⚪
❌
❌
❌
✅
❌
✅
⚪
‏۱۹ )
🥷
Mohammad: ‏(۷۴
❣
)
‏
⚪
⚪
⚪
❌
✅
⚪
✅
✅
⚪
✅
⚪
✅
⚪
✅
⚪
⚪
❌
⚪
✅
⚪
‏۲۰ )
🥷
✨
𝒫𝒶𝓇𝓂𝒾𝓈
✨
: ‏(۷۲
❣
)
‏
⚪
⚪
⚪
❌
⚪
✅
⚪
❌
❌
❌
⚪
❌
✅
⚪
✅
✅
⚪
✅
❌
⚪
‏
👥
و ۶۳ بازیکن دیگر با امتیاز (
❣
) کمتر از ۷۲
❤
خسته نباشید
❤
‏</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkCINZeAWaz2fVAMfRt4LWGSpMZWDsKcnlwInPqVp-aCU4DvFZ0PsDLkBIdO2neLWnSnT9AnvZQJaL0Y7uQi3GbpimECanBM7hF8wvth7SY30CLg5lF8GO_Dn9AgSSOaIWyZ7uwroq1_ArGWPt4B_2g61FuQgplni_eyyCKEaWGWsJP01I06bYX9DCRrCkJWk9ee5n_8gDtGa9wJRvHCRxusbVo8wlticLtiia6UP5lF3MFzBfbuI_83_bgV18upSlM63l1MHRKxYYYFjrfsYtI7-1a4SN19RHRCLAGoAFJIx0c8uOP5_sURe-CKxBKgbj8R5KFGqMNzG02Zbrgz4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://36326231-3138-4166-b834-303439306131@185.143.234.96:80?encryption=none&security=none&type=ws&host=dl.tgmovie.bond&path=%2Fl%2Fw%2FaXD2QyDdS6vRQpxs%3Fed%3D2047#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=CaGt2xuteraStGHQ5m93nSjJBFBX8e5uobDrzpPuR3xi1eHQpcUgSQEzhbJCPpE8Hr7bGjPieAT3Jym8vQXvG4IzM7gO_QT_Tst7_aY0x86gbBxFYQ8gOK0RN4fKU2CTLAlbcRcFYCPdctR1cIRKFdchvMzFWhFBGqYLXpmayFF4pwzrX_dN1LJ2Qs-JHaPswpKQZYij1A6oE471jtm2TakZBRGiwu1-3XvdJzstkWAjZ8WkdZ9BoNYJWy7DEju9Xpp3SAL75Rb7NuxQ4nfkbTYWefZcDcL47szR3bTkrPQKlX5Mh29lkr9stqLVGwenl4rREpP3qFJTj8KUgC7tBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=CaGt2xuteraStGHQ5m93nSjJBFBX8e5uobDrzpPuR3xi1eHQpcUgSQEzhbJCPpE8Hr7bGjPieAT3Jym8vQXvG4IzM7gO_QT_Tst7_aY0x86gbBxFYQ8gOK0RN4fKU2CTLAlbcRcFYCPdctR1cIRKFdchvMzFWhFBGqYLXpmayFF4pwzrX_dN1LJ2Qs-JHaPswpKQZYij1A6oE471jtm2TakZBRGiwu1-3XvdJzstkWAjZ8WkdZ9BoNYJWy7DEju9Xpp3SAL75Rb7NuxQ4nfkbTYWefZcDcL47szR3bTkrPQKlX5Mh29lkr9stqLVGwenl4rREpP3qFJTj8KUgC7tBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=Y43gf8IERBHwLq10_-vKE439EPuSPBAUF-ZTAOm4wOA4v14dZ0iUVssaqzzYWaVdputn3jHg8yDmHL_nJ_-PhCntX9cGqJcr9c_hIJLmXRaEagRXlqeoREeB9Fc-NUT3c6CH9KaVp7tuBY51UjFDidOUchnVGk3ufXw2y0vzdf7c-mfHCpaMBFJfhGwgcROHOgML9cHb-iIV5s18PI6aItmiYeCE8yT6X0gsOMbKtlRlESfzIKdv8dW8PDgr9eTck6Vlv1Zzl9IOtF-fWMe3YDZajcVw1qPmh0B9hOYrQpa7ZYpZNX12Qyq8lTAIE78bwX0QqG0vcZTF1J361ePa0kfViVF0-1aWpN0Yf_h1FKQyd3ybulhs6T6ykYCxQh5XjLvx9Es6LwL7JSlcvsg_aK6HhLp8yO7GdtON6EWKPttqGYySfoXFGqrsqbrliCpzhp-vTXyk9YAGTGhKF_xNnwEWoZj0fUfIHL8zxOKndQ1zDgWu6t4zQPggOvdalOg7k_PLM5lwDLN16OePjn7TpEk3B4tJNzkLbgUW8JOpmse6UCIsqtCkZClQ6D2yOTCmprgq-s2Q-BNNUAtaGL2rLGhBjQixQfYEyLctsBHZfjQyKQlgK8u9-2vtz6ba1o1ZtQX3fnr4EZpZfifszSNQ5xTnLKgSgkaF_36gRctUMVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=Y43gf8IERBHwLq10_-vKE439EPuSPBAUF-ZTAOm4wOA4v14dZ0iUVssaqzzYWaVdputn3jHg8yDmHL_nJ_-PhCntX9cGqJcr9c_hIJLmXRaEagRXlqeoREeB9Fc-NUT3c6CH9KaVp7tuBY51UjFDidOUchnVGk3ufXw2y0vzdf7c-mfHCpaMBFJfhGwgcROHOgML9cHb-iIV5s18PI6aItmiYeCE8yT6X0gsOMbKtlRlESfzIKdv8dW8PDgr9eTck6Vlv1Zzl9IOtF-fWMe3YDZajcVw1qPmh0B9hOYrQpa7ZYpZNX12Qyq8lTAIE78bwX0QqG0vcZTF1J361ePa0kfViVF0-1aWpN0Yf_h1FKQyd3ybulhs6T6ykYCxQh5XjLvx9Es6LwL7JSlcvsg_aK6HhLp8yO7GdtON6EWKPttqGYySfoXFGqrsqbrliCpzhp-vTXyk9YAGTGhKF_xNnwEWoZj0fUfIHL8zxOKndQ1zDgWu6t4zQPggOvdalOg7k_PLM5lwDLN16OePjn7TpEk3B4tJNzkLbgUW8JOpmse6UCIsqtCkZClQ6D2yOTCmprgq-s2Q-BNNUAtaGL2rLGhBjQixQfYEyLctsBHZfjQyKQlgK8u9-2vtz6ba1o1ZtQX3fnr4EZpZfifszSNQ5xTnLKgSgkaF_36gRctUMVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-44Vuf65Dv1-dpoHlavZdBsqrG4nlV4WOytYS9hAA1iMyPoMfwfOLREAbLvlhkEXFqvghe6LMzDD7gvJz_FUowZDdp68zBDBSZ50esNJedTeSvEKOITPb5g1SKX9RRZvyF8ELLyVCnTvWlD8d4MS3PZK_80fDDzRx0tBljf0CRfGbKsEqPKcux5qkoh5bBkOZP-u3yAEzX1t6EwKBURB_fzfQJVeg98qIUGOdXMwYM9BKcfqsVQ7T6L_Y9rSkxFztoy-XDu_sJguAdTaLbpo8fvweRwjBlPyjcjAe7R_kZPfTmFxiW8AjOReBeUHHwsaKRfZPSgJKT0zfyparNXmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLjO-J5QJDXqUp-hG390uWC4sWoBwo3jISKGGqphv1K3IBN9FtWKHvh4OaztvAcFqOcVW5_g7mVZ32RnyYlZyjvb6m5EvHkfOxjQPYtpn0ClF5lPbGaor0ylt3OmgsCpmI2kQdfordfhI8zgK-1X5H9Eb0n2nfGDrtB4zDkyA7ULu_liJ0esXk1zLHDEnayhiqgH1BWOeRaCLXhWiFx0QfuPTinNPrDb5yB9okG1R20x1yJp9THj1dcFu51q6UaSDT69_dJSzsQUUsxOzEcq-WUcWIk1AnoQZ_44bJ-QcTq1-Nqr6XlV-IabYoP8fLPmxeHoFo6-kbHQeHR3piWRSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8373">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
کد تخفیف حذف شد برای راحتی قیمت هارو آوردم پایین راحتر بتونید خرید بزنید
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gjKa9TCHssTgVTY7zOiOnRKsvlmzj59_0t6Y_6OHZkVFCaHK7FFXVSrxlZCuf0OYxiDGUJ1ND7PCX9qDkv6Q8tpu_wlau7WIRIRaVPQ1V_a4GpQkeSJGR9TVNzm-pyJaYtOsodzt_cY7wHvDQGeBVDXoQwzeHO98IKz5p-bvqrG2br9UcSe80b4WuvRhCbsmz1NZGisvORYcxBmfJGuDDgJSolzeRSKRcj6vPW8ugcSUKCxhtXIS0_XlTkWTaXKk18pW6hIFo2MUOlzT7eXHULX77II7jqbbwzpoliL5vvZ0LOj4UWLrMIngVxWBSgTKlQ9o-j6xqrr4cvKEgXrTDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/IranProxyV2/8369" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8368">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=LAfaIYMCN-WbY9Quo5RosCY4uNebSu3eqqnqjK9qcJBaUZM9Lc7xM4PjiTUAEsK1c61yLx2YOoTnu3fCO0BJ2HM5aL0UY-hYYfANw1lEiGI2kJdEmT2j7QaEbX-rRjoQuHyTF1B40jaTovgSHxlflDHbPV9Jx3AeH1WLN5k8ZfW2wVTz0OvwsNcbOOjeHfsxs_FfZlZfWnNCzaVNKM0kER5PexLUNkMK_JlQu2Vymtr6teWgnZ1-4DPLo3a-UfPfiEQi9WLguWnroxxIAcAEWlbl9CUPVOKeSrNZ4J6JZUJvu7bYxyfIsDv38_2AqR3IiHJMCMdTVb11McuXOXtOkH6mmWvqkhB5DTZaIb_Mfnv9HGpZ9Cu59AiMEtMpM5cXbQidCChJImH_N91wg2NmCpVaVXymV8sSmQRWd3iywXN3pOsEUMzwdwzu1ePHPQjnPc2xA69IUNrO1SgbvbvKO1wtgFLq_cq-Na2kxqVuex9Uk2d-u8qLfcqBkZx2YSzFMtorg8NFB_Lr3PqPBcEa1D94VJKThLjfwkpREJ3NvrG5QwfI-UU3obmiAGrDPLbTEULcq33vPfMlhnHCkZzl3sLuwSglB-4hGxZHGyPWlw8hXFnvOCZv8Ifa18Kpzmh23loxLloVktrVLwdxXD8JzgqNfPzVVDsnTamcJ-mWDII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=LAfaIYMCN-WbY9Quo5RosCY4uNebSu3eqqnqjK9qcJBaUZM9Lc7xM4PjiTUAEsK1c61yLx2YOoTnu3fCO0BJ2HM5aL0UY-hYYfANw1lEiGI2kJdEmT2j7QaEbX-rRjoQuHyTF1B40jaTovgSHxlflDHbPV9Jx3AeH1WLN5k8ZfW2wVTz0OvwsNcbOOjeHfsxs_FfZlZfWnNCzaVNKM0kER5PexLUNkMK_JlQu2Vymtr6teWgnZ1-4DPLo3a-UfPfiEQi9WLguWnroxxIAcAEWlbl9CUPVOKeSrNZ4J6JZUJvu7bYxyfIsDv38_2AqR3IiHJMCMdTVb11McuXOXtOkH6mmWvqkhB5DTZaIb_Mfnv9HGpZ9Cu59AiMEtMpM5cXbQidCChJImH_N91wg2NmCpVaVXymV8sSmQRWd3iywXN3pOsEUMzwdwzu1ePHPQjnPc2xA69IUNrO1SgbvbvKO1wtgFLq_cq-Na2kxqVuex9Uk2d-u8qLfcqBkZx2YSzFMtorg8NFB_Lr3PqPBcEa1D94VJKThLjfwkpREJ3NvrG5QwfI-UU3obmiAGrDPLbTEULcq33vPfMlhnHCkZzl3sLuwSglB-4hGxZHGyPWlw8hXFnvOCZv8Ifa18Kpzmh23loxLloVktrVLwdxXD8JzgqNfPzVVDsnTamcJ-mWDII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8365">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBkXwVG6G_VSLKO2RYY2mPzZfD20RUvq-Ctq0CSHNx5YOFh2vkadSbIv9wo3I4eTp2NIQdoxtyJ7acb4HoJXspY9Z4ly_PgRjchXtd2nUc-tioLeZ02i2NrVptIhm3BASSC57FO29N42RtUm-8M66aDC2HP1LKRmKDBeJJ1IG-cRMqWvujehHr2Rp8wa0vxouTu_kofVLr9p6qMkYRigMEzfccw99iDQ8WGW-43_jGdRmRVg-jCe6p3cnshfaMRBM_ADt-GhoPmxX0tnz0d66hN_TDTgbgJl7SJIQYfTfg1fupHxohmiKh3hsYor1NkQijQfL_Q32BLpayKLwAG7ce0M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBkXwVG6G_VSLKO2RYY2mPzZfD20RUvq-Ctq0CSHNx5YOFh2vkadSbIv9wo3I4eTp2NIQdoxtyJ7acb4HoJXspY9Z4ly_PgRjchXtd2nUc-tioLeZ02i2NrVptIhm3BASSC57FO29N42RtUm-8M66aDC2HP1LKRmKDBeJJ1IG-cRMqWvujehHr2Rp8wa0vxouTu_kofVLr9p6qMkYRigMEzfccw99iDQ8WGW-43_jGdRmRVg-jCe6p3cnshfaMRBM_ADt-GhoPmxX0tnz0d66hN_TDTgbgJl7SJIQYfTfg1fupHxohmiKh3hsYor1NkQijQfL_Q32BLpayKLwAG7ce0M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
وضعیت سرعت سرورها
@RUSSIAPROXYY
🇷🇺
📌
آیدی ربات جهت ثبت سفارش
👇🏻
✉
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8363">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gKi5BESguAxK3kbAl2mpE-zCfcSfFOVXDmvHwSeCANGzJCvtO4epCFcFrV_Jm72ylF6OZRGqyMMcqscqweSt5YsdKHpXIXSuBU3SjJT2ZBLcDtikMt2mstTdJvo_g2N7CtAm2mH4VhwkK_kdotQNnn7SNNQZtA8RtMiAz7HP5ajqozwtTJgcxmnKVbhf7moG2XQjshIUpjc_nJ6vZ17w5yy4IdEHQRMBOF_mRuEhWNROuOC6cviv-E3udI5p7f6O12o6K3-O4JBqIYcR215i163KCZgRit1_yd-ixplo034a4-UApUoas_3PEpWtsN9dE0dmRgyr-at_OgrsD1rQUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8358">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8357">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=
250
T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/IranProxyV2/8357" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8354">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lACY4jCrTFDk50BkmbrKSyejaZlT8RcLUFtAKjxQtcSeJWQOqtktt2CNE_5mTTJFQyW66bsqHAR8U0b3THmtiQGv0kSNTXX_8swTLSGxUZsTIQVMNaug4FE6ysugEu4GoBT2ilaCnRWXGBIGbuaDmzhNUio6ON0EGsnz0rBDtGAbVSFY5RNk1l1u6AaAhYibX94nJl_YU_5XJ7--1DNOLZt9D_getAI8fdzWfGN2-V34PxE9YhuoN74fXnLepxodisXVrKQUqqhjIRc6WioOkQ5mGLaIXHfdk-YEfh-zzULjiiHtY4XUKCbF929NQWeEIMtzFiF6yhohC_-qNW4ocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8350">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=
250
T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8346">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">slipnet-enc://AQskvHpoSr0z/luIGDACbhKreNDTKyhhMA3DYlYmmHhr6T/THqqypSEZIR2ROKHLR6XP/iribGUsJGd/wwwh1ZLFTrR6kKY78tIX6XmbL6eLIwT2+Az997HmcivFgJpEtgDTqAQVkonbDemLykPWC/L86oUN+Bfoqg7S+FVTAWD2NIQa/11CwodDdSWh8KTKoVIV80wPNJXSS2qi4THuGu5jEoTVOenuOImriz65wsm4ASSgo750zT/dZvGGj0ynpjQVa+y9hxbby3u0Lu0qbp27pnXaUHzmoEh3jQVIQi5OAcX4VvcUetwhOtV6DXHU+vsZPWDcQUOpd/7/0wZW+EUN24SqPt9fGMIsFsKpHXPoJpUs2BB1PkC8TZymVkqwmjeO0Cey8oj1g+DCiR5r1jtWijUAv4yehzdzbDuU++T1J6Sj0nP7ADo9wGFllaneHyrpoGHXRSCiQtztJKw7qwEWTLBo0jLT1Lt76HyJ0xGn6lPM+evyYA4Pd3E1bwcaa9kh6kJ0BTIjfT2UBa+zd2L+UejzTjqrKrYW6whN792AmDFdS9CHY7Ho7F2PZf+wQx4E0BjdJ7MFpNfblxmmgD2SsxRqH/7IpWpb+mr48+kqlveInlB9RKTxdzdfufoY5s82opLQBhAsuyXEhcqMYgRLIUsUXiILutNRoc/vBq41mI4B02bmpcZR6JmcYTcU1pjWop1QQPNvo89WaaJWZxYBCjO+TtbhLFsN9VTXdVe6fMSNo524sRPA3Kk04YuQk3cugUbywKo/BUXCnss9G7ffIJgmxd6UK5GIunGf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/IranProxyV2/8346" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8345">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=K1ccJD-YSQqycxinllzLfisVZUBnQpftfmPVX_u5RxdbRCaSrmK2Gs-wRu5wKeh8D9iaK5yfHId5y4_nZ9h7027SDGT3euLL6EknyWWWSZXRmplAFD-pqdhzHC3_AVXYHc_en4kdYqgutRu7i8gVwMasYzqIFOda-SXVAfOmJK9zQOgcgdfecBux_bfmvM2FLsmy6_1JxmRQ-RyJDd_OwTGyOiaz7bKb4oR5r4J1XcSNQb_bxm1y44qOWQYlbJOqG7rKFrdwIbV0zRec1RryGNNVt5Iu9e23nwSCV61SSNpj5mhoQjnBXbX3PI_cj6xV5EgzTSXdQCwnYQ4ysSO_5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=K1ccJD-YSQqycxinllzLfisVZUBnQpftfmPVX_u5RxdbRCaSrmK2Gs-wRu5wKeh8D9iaK5yfHId5y4_nZ9h7027SDGT3euLL6EknyWWWSZXRmplAFD-pqdhzHC3_AVXYHc_en4kdYqgutRu7i8gVwMasYzqIFOda-SXVAfOmJK9zQOgcgdfecBux_bfmvM2FLsmy6_1JxmRQ-RyJDd_OwTGyOiaz7bKb4oR5r4J1XcSNQb_bxm1y44qOWQYlbJOqG7rKFrdwIbV0zRec1RryGNNVt5Iu9e23nwSCV61SSNpj5mhoQjnBXbX3PI_cj6xV5EgzTSXdQCwnYQ4ysSO_5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینک از وضعیت سرعت کانفیگ ها که بخاین تبدیل کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/IranProxyV2/8345" target="_blank">📅 19:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8344">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن   ایدی ادمین…</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/IranProxyV2/8344" target="_blank">📅 19:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8343">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">محمدرضا عارف از سوی مسعود پزشکیان به‌عنوان رییس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/IranProxyV2/8343" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8342">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن
ایدی ادمین
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/IranProxyV2/8342" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8341">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کانفیگ های پروکسیو یه تست بزنید مستقیم وصل بشید بدونه هیچ پروکسی بیایید تل ببنید بالا میاره و اینکه احتمالا ۲.۳ روز دیگ کانفیگ هاتون کلا عوض کنیم  یه تست بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/IranProxyV2/8341" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8339">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YsOFghog1f33Fol4e2GNDJiy5CV7VqB83glWsxziwkYgXu8H0HXkA-L_IOUW5K5KOA8vj4AauwqEG3PmmR3sw31kBlkPpRLALjnubnH6_d41WcmxW5MYYOj3mffTw8_Pp2JCsRkTJlMsQVqa22s3rXe3mfy51D8IpE27HGNmkrOKptKHaD2G7SV5dMHUDC6ZxcQCtIW3EADNR5ZlcTDWd1Ew9yAz_NmJqKYHk675YkEh5Nd2Dd7v8Kyw-FK7qrAx6ER6x6NeE66rIpJSw3qlUBaU3mFALvVUY9TfIrtQ0FZ4NW4uJjiirGX0B68QcWwCPWd98kBM9aiEcePfIMK-SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خدایا شکرت؛ دیروز اپل به صورت رسمی اولین نمایندگی خودشو در افغانستان افتتاح کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/IranProxyV2/8339" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8338">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">معاون ارتباطات شرکت مخابرات ایران: اینترنت بین‌الملل نباید با همان قیمت اینترنت ملی عرضه شود!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/IranProxyV2/8338" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8337">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/IranProxyV2/8337" target="_blank">📅 13:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8336">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/IranProxyV2/8336" target="_blank">📅 11:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8334">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LSNARg8VBPXOHr4PFKyzbXlsQLe8J7Nv_fJxRiG1K_Ih9EUPzvWyACzjVVqJJwiySDn3NQdqi7293GY_OjEx9LdLEr4srDvyIrOrz7wZQ8V97K800pyOLTQKpKIAZc79_cPwE8iuit2Gt-OkM0e4-HUgmnsjjdAXnBlAwURggnv0fokyxNOqTkxHXiaiOz5MBVBOl5zK7ErA4ZckF4wUxFiMLqu54S2qi-VE79sYEWFCgje6OGW0c7WO2feDqfsjqCecL174DQgfqL-17EG5UsiXsuWPPaNgjN2m5eQiSqcuqwnGrB6DJoqeAPiWhAV6gChaiAx-3cgKNfG2TqwuvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eIjh81r7ef4dp_DgvtnsFAQqfK_I2gYnnmpUE6MCmwFo0WmTy-yGkeyPd2z2SVmkm0W7NQb0pD0ZGsDFmSYXODK8sXa5GT4cACwfE9UtXPn3yg8OfiSJU_6sZVQnjy4teLLO2rOCJGI6wGXd8alCVw7R_-HUWIi5rcP_s52l_2SmRxKOcZCyjAUTt_7YPDBwBAOItdlNBoT6M4ZzBl1FoqczPtxysrSkaMBk-Jy82DMz10MZQXca0x2kRUMWF650aLlsce719Bqlpl_vcgHDNV7Ck6KEcVYnetQIE1YM2RtbuB_7QJsPR3nKK4j6k-RAV3TgjuFeJS1f5pXLV1Vn-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صنف کفاشان و اغذیه فروشان هم شامل دریافت اینترنت پرو شدن.
به‌زودی کل مردم ایران شامل اینترنت پرو میشن که دقیقا همون اینترنت قبل از جنگه فقط به جای گیگی ۵ هزار تومن باید گیگی ۴۰ هزار تومن پول بدید.
و فقط اونایی که توانشو دارن میتونن از این کالای لوکس بهره‌مند بشن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/IranProxyV2/8334" target="_blank">📅 11:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8333">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">قیمت‌ «سیمکارت سفید» و «اینترنت پرو» در بازار سیاه چقدر است؟
🔹
اینترنت پرو و دسترسی بدون فیلتر از طریق کانال‌های غیررسمی و بازار سیاه فروخته می‌شود.
🔹
قیمت ۵۰ گیگ اینترنت پرو در بازار سیاه تا حدود ۱۲ میلیون تومان اعلام شده است.
🔹
سیمکارت‌های سفید با وعده اینترنت بدون فیلتر با قیمت‌هایی بین ۴۴ تا ۱۲۰ میلیون تومان فروخته می‌شوند.
🔹
فقط اقشار مرفه توان دسترسی به اینترنت بدون محدودیت را دارند و این مسئله شکاف دیجیتالی را تشدید کرده است.
🔹
کسب‌و کارهای آنلاین و دیجیتال از محدودیت اینترنت و هزینه‌های دسترسی آسیب جدی دیده‌اند /اقتصادنیوز
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/IranProxyV2/8333" target="_blank">📅 10:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8332">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://45cd71df-7b23-4568-8677-fdc4a0daa76e@protectnet.cloudinohost.com:443?security=tls&sni=protectnet.cloudinohost.com&alpn=h2,http/1.1&fp=chrome&type=ws&path=/&host=protectnet.cloudinohost.com&encryption=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/IranProxyV2/8332" target="_blank">📅 03:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8331">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✈️
Slipnet
slipnet-enc://AcwwsvYl4r7DajFRU6wa12enHS94jGWcw63dYwNxwSzZZDO03mNtFG6vROd+UO8opWIgDZkjjnUHlVvSaj/HvKW+p2HLBc4ETWvUWsMZpCwiUmAeEORd+qfA089iU7PBEHuvMqTIeRqwCA6OyylmfHRyIlB+dS4avIQQAJLxeW6G0ZMnp8HZ4VPpuiN2Vs3U7StRqxSwEP7f8wUXQy1DHgcCE9WD74CKd5RxaHADsaaT4Qj56xDB+DTB8l41JtvrbtjUVSNCS349vS8XyPhXi12t/YaAupzBKzSkPCXi8UjM8Ft2AyUuvLKTPgSMjJgI+vBT+16sztR9Q5n88GbrLNNWKD31CXYgjS4YNk8tLooUjYBgOKWmoBPVWCHej1RPyjs3lg64enMfTyX+WKjZ/fxrqH/8uGQZGj7qLjcGhGaohjHujN+ODCfxxAlK+6Y6eQFfld7UtXfyz9cTmhkk7mebn5exSrIv9o1auX6VVjUQ8xLMvhf6wwsD6vwQsblA6QeIvDoD8NUOfeKZFKrraoPjEdJexjOxcn9gbWSEM/QeqZB/lQ4LnfH6zHtP8PmH63PRZJTZUv6VlAovbrtWUp0ziB5fgISZTC4akBfBPTO32WXUTj+Wo1sSSeCH1rfVQAYoMqoQusLWWSHLm5Llfz5jW8qGwROFKxCq6HYzt4gLRZixvL44Dluxo+oyG14jHwsAmPVh05xydwjCI2XcpiJgX5De91xk+x39xMt7AwApPsraUbzuBscA/TU90Ehahp5NbRa0nr1Z44yGL0dC78sWZrPT5XtXbIE+Ydpd5qq3F1Y=
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/IranProxyV2/8331" target="_blank">📅 03:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8330">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
اطلاعیه سرویس سرور های تلگرام
⚠️
به دلیل شرایط پیش امده و قطع سرویس های تلگرام توسط دیتاسنتر خارج سه راه برای برطرف کردن مشکلتون وجود داره، دقت داشته باشین که این مشکل فقط رو سرویس های تلگرام هست و سرویس های تانل تو ربات هیچگونه مشکلی ندارند.
1⃣
- روش اول…</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/IranProxyV2/8330" target="_blank">📅 03:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8329">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/IranProxyV2/8329" target="_blank">📅 23:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8328">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/IranProxyV2/8328" target="_blank">📅 23:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8327">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سوال اینجاس اینا از بازی ها هم میترسن باز نمیکنن حداقل مردم حوصلشون سر نره
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/IranProxyV2/8327" target="_blank">📅 23:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8326">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✈️
علی قلهکی، خبرنگار:
🔻
تا امروز بیش از ۴۹۰ هزار سیمکارت پرو فعال شده است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/IranProxyV2/8326" target="_blank">📅 22:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8325">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">💎
𝗩𝟮𝗿𝗮𝘆𝗡𝗚 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻 or MahsaNG ( Psiphon)
vless://799f939b-964b-4416-84ac-18a6ace7fe70@camp.nahidapp.com:443?path=%2FIF_VPN_Bot&security=tls&encryption=none&insecure=0&host=camp.nahidapp.com&type=ws&allowInsecure=0&sni=camp.nahidapp.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/IranProxyV2/8325" target="_blank">📅 21:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8322">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6QMxF7XjiR5EgMMf75w-CKUY-qc0uxTWZ8zQhGRZwTgJbsVLEXPJqE-AvEbs-VA5PbxNfCvMh7LqM0ARJeXO6i3PwVCLIYz5n8rHzbuTBX07bTSlzRup4P62rzmrhrLkMO1xaXVOmGb204WhGWsGXWHT7zil_lDqFDIQ6z8me6tfqauwUs0s22JvkoB7r7V5ZSD00tbK5dWHjlAO_pMEVy4zaF6ixgek-a5MXwSiWB9v1AgV95QwlPuckp1KOtlXN2K3mJWkHXIjX2yKWv5O0EN48FMoSYAqWJwe0crVTjiyu4Q3hssaRcWIglw4XqxZoeBiMS7pO53znWHP3kuYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
وعده پزشکیان بالاخره درباره اینترنت :
◀️
ارتباطات و اینترنت به بخش جدانشدنی زندگی مردم تبدیل شده
‼️
به آقای عارف ماموریت دادم با لحاظ حساسیت‌های حکمرانی، نظر رهبری و وعده‌ای که به مردم داده بودم، در قالب ساختاری چابک موجبات خدمت‌رسانی بهتر دولت و تحقق انتظارات عمومی رو فراهم کنه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/IranProxyV2/8322" target="_blank">📅 21:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8321">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
اطلاعیه سرویس سرور های تلگرام
⚠️
به دلیل شرایط پیش امده و قطع سرویس های تلگرام توسط دیتاسنتر خارج سه راه برای برطرف کردن مشکلتون وجود داره،
دقت داشته باشین که این مشکل فقط رو سرویس های تلگرام هست و سرویس های تانل تو ربات هیچگونه مشکلی ندارند.
1⃣
- روش اول بدین صورته که شما کانفیگتون رو برای پشتیبانی ارسال میکنید و همون حجم باقی مانده براتون با ضریب دیگ چنج میشه به سرور ثابت البته با سرعت کمتری
2⃣
- روش دوم سرورتون تبدیل میشه به سرور تانل با سرعت بالا مث سرویس هایی که درحال حاضر در ربات هستند ولی، ما به تفاوتی باید پرداخت کنید بلا عوض
3⃣
- روش سومم اینه که کانفیگ هاتونو نگه دارین بعد از این شرایط نت از حالت ملی به حالت بین المللی تغییر کرد به ازای هرگیگ، ده برابر اضافه تر حجم دریافت خواهد کرد
🔻
@RUSSIAPROXYY_Admin
📌
به این آیدی جهت رفع مشکل پیام بدین
👆🏻</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/IranProxyV2/8321" target="_blank">📅 20:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8320">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJryDHfPrt7Sv7YiaB2EmJok6t_2JluCvjMQG3ddBGi00sqytNLy5C18B2QLZ0fCHTrHaISmH6gYKChzSBsVde0IPj1L-J_ahPs46s5_xRk2MlxtL0a6A7SnBhI4JC0JuiUUTnjP4PPYSVqgX5aT8BOOP98B3-9gtzf6nMwbphDrIh5AOBLlYgAazZVguHfkxaHXhVJOHwq7mUkr43MGW5sUVJKjiPazLdRST-fVe5Lp8HSk4j21xqAyhdrEk7qDYI-PdO8-csR9VgQHWD-RnAPoMvMVfY1sasn-gDRopc5s0GnjGmdVA4CPQth8g8B6wuiJUAmpihqq9THDUcEfeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت اینترنت پرو
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8320" target="_blank">📅 20:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8319">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✈️
دوستان نهایت تا امشب سعی میکنیم سرویس سرور تلگرامو اوکی کنیم، هواتونو داریم همونطور که وقتی هیچکس وصل نبود تو دوران جنگ با کمترین قیمت ممکن و کمترین سود ممکن بهتون بهترین سرویس ارائه میدادیم، سعی میکنم از جیب خودم هزینه کنم تا مشکلتونو برطرف کنم نگران نباشید
✈️
سرورای ثابت برای نت بین المللی و کلیه اپلیکیشن ها و سایت ها و... براتون تو ربات با کمترین قیمت ممکنه قرار دادم بازم امروز
قیمت هارو کاهش
دادم که دوستانی که شرایط مالی مناسبی ندارن هم بتونن کانفیگ تهیه کنند.
✈️
🎥
📸
💬
👾
📞
🤖
🔍
🕹
📱
⚡️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/IranProxyV2/8319" target="_blank">📅 18:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8318">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de826422e1.mp4?token=Vh53aa9BbnnK4p5kHla4qRAvALliQOrzTpYqpc0GjidSb5-xrSot3_1liBjZF9aOMZDvkLdeHWDjsmDsEziYLUrQupHqBTE3ixzwGF0tAlwzrZXlxpKr9CRZqYI3ywJzbJqi_O4pBw_IYlCrphN535QPx-frBglvUnqZG9F6P-JYADKe6Hy1uqh1ncgrL3hkYYFDz1ltdCdKSX2GpNV5L0AwzCEbiZI2Sn0xqsGDcnrOvQaEFjRQJSb8G5vCl6ZYJYHxfXCjl0FSCSjrLB_ZpQNp-kVIrDbSYMpchpPGmOPHXUsFCzXCEkogJGYoDLWOQ9sgAcAEnJrpdHP6TbUdhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de826422e1.mp4?token=Vh53aa9BbnnK4p5kHla4qRAvALliQOrzTpYqpc0GjidSb5-xrSot3_1liBjZF9aOMZDvkLdeHWDjsmDsEziYLUrQupHqBTE3ixzwGF0tAlwzrZXlxpKr9CRZqYI3ywJzbJqi_O4pBw_IYlCrphN535QPx-frBglvUnqZG9F6P-JYADKe6Hy1uqh1ncgrL3hkYYFDz1ltdCdKSX2GpNV5L0AwzCEbiZI2Sn0xqsGDcnrOvQaEFjRQJSb8G5vCl6ZYJYHxfXCjl0FSCSjrLB_ZpQNp-kVIrDbSYMpchpPGmOPHXUsFCzXCEkogJGYoDLWOQ9sgAcAEnJrpdHP6TbUdhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شهبازی مجری صداوسیما خطاب به مردم ایران:
اگه اینترنت 5G که افغانستان داره و مسترکارت که سوریه داره اینقد براتون مهمه؛ خب برین همون افغانستان و سوریه زندگی کنین!
﻿
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/IranProxyV2/8318" target="_blank">📅 16:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8317">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ایران اینترنت ندارد، روز هفتاد و چهارم …
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/IranProxyV2/8317" target="_blank">📅 13:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8316">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⭕️
اطلاعیه:
وزیر ارتباطات گفت در تلاش برای برقراری اینترنت بین‌الملل در اسرع وقت هستیم.
همچنین طی پیگیری‌ از ISP اعلام کردند که اینترنت بین المللی شبکه خانگی متصل شده است اما هنوز زمان مشخصی در مورد اتصال دیتاسنترها به اینترنت بین المللی وجود ندارد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/IranProxyV2/8316" target="_blank">📅 12:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8315">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde1d5a77d.mp4?token=DxXYTzeSUmeqQPf2y09CTPeAAnt7XgVuPGqk9sFH1KibWEyvqyrHCC7HW4uzO69-tG-F5yNrxBhhf9L5gLt64L4uoHmxqCiUSPNPw94dzFTzw5jVPvVg5IefHko-dMC5wMiDTvVCQHU8Jk8mqU1J4fwg2JrSjg1wnfn9ZFv6mqhjSEJSQl-x-LeynbCafIzgYZiYPPSMOccul1UXY69iswk8V_3wWulE9S_atC6q7Zk19v459tzVa9qjS7EtOYjNnX0AcVpKJTrVXl0KdmlLDlWocfAYElkvJ-N4haMWw2ARDmg7bxHvhbEk9mbMIN6-x8w9mhHzNBYNc3F_XsM_rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde1d5a77d.mp4?token=DxXYTzeSUmeqQPf2y09CTPeAAnt7XgVuPGqk9sFH1KibWEyvqyrHCC7HW4uzO69-tG-F5yNrxBhhf9L5gLt64L4uoHmxqCiUSPNPw94dzFTzw5jVPvVg5IefHko-dMC5wMiDTvVCQHU8Jk8mqU1J4fwg2JrSjg1wnfn9ZFv6mqhjSEJSQl-x-LeynbCafIzgYZiYPPSMOccul1UXY69iswk8V_3wWulE9S_atC6q7Zk19v459tzVa9qjS7EtOYjNnX0AcVpKJTrVXl0KdmlLDlWocfAYElkvJ-N4haMWw2ARDmg7bxHvhbEk9mbMIN6-x8w9mhHzNBYNc3F_XsM_rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهاجرانی:
اینترنت حق مردم است؛ عصبانیت مردم کاملا درست است/ عامل این عصبانیت دشمنانی هستند که باعث می‌شوند فضای امنیتی ما مخدوش شود
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/IranProxyV2/8315" target="_blank">📅 11:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8314">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اژه‌ای: اینترنت پرو و سفید مثل پتک در ذهن مردم شده است
🔹
رئیس قوه قضاییه در جلسه با وزیر ارتباطات: مسئله‌ اینترنت پرو و سفید مثل پتک در ذهن مردم شده و باید با موارد خلاف قانون در این موضوع برخورد شود.
🔹
در این جلسه دادستان کل کشور و وزیر ارتباطات به رئیس قوه‌قضائیه گفتند با بررسی‌های صورت‌گرفته، احراز تخلف در قضیهٔ موسوم به «خط‌های سفید و اینترنت‌پرو»، قطعی و حتمی است./جماران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/IranProxyV2/8314" target="_blank">📅 11:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8313">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">vless://8b7dbddf-fe0a-4405-b8e9-bfac4d9439ef@185.143.233.235:8080?path=%2F&security=none&encryption=none&host=MHI.ARTARONA.IR&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/IranProxyV2/8313" target="_blank">📅 11:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8312">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">V2ray + Psiphon:
vless://3728fc28-910c-4a9c-888c-c08c3e2f4a06@snapp.ir:2052?encryption=none&type=ws&path=%2Freq2&host=snapp1.gptpersian.ir#musiclovers85
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8312" target="_blank">📅 10:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8311">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">احتمالا اکه پروکسیا درست نشه با کانفیگ های ثابت جاشو براتون عوض کنیم اطلاع میدیم خدمتتون بابت صبوریتون متشکریم</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/IranProxyV2/8311" target="_blank">📅 00:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8310">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حجم سفارشات ربات بسیار بالاست موجودیش تموم شده بود مجدد شارژ شد، صبور باشین، دارم یکی یکی رسیدارو صحت سنجی و تایید میکنم با تشکر
❤️
💲
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/IranProxyV2/8310" target="_blank">📅 23:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8309">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRNZaScZVFza3-gJWEz2G1CeCdoaoFGdXQ47RKea39JkfmuWQT3tXBVZIEUtmk01SU4MFUAAY2SImxOyjquoWHc-ClZovyJEpR4-G4QI7YOxoVyhS8NHxtv-BC0SE9mUxfcM7L3YGL3M6_scF8H5ZOhXh-3jl1IujrANBaRrLkYjuKeMw8QXk4vvi1vNx-naEGHSAVoeaAr43HAwBnnC6ldyyHgq6n-ZhEDUjgsWoZ9sfX6M0UUQvvVJYLAcSNXyvyOywN2HC0Oog2LS1Bt8b5_pGWgxSVmvD-xofosVPe0sLMubo4L22WqamdSok5K7dArynJ5Qf_60wZiItZgMDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایزه چالش دیشب، برد 2-0 بارسا درست پیش بینی کرده بود
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/IranProxyV2/8309" target="_blank">📅 23:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8308">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
معاون علمی پزشکیان:
حتی در شرایط جنگی هم بستن اینترنت راهکار نیست، زیرا وقتی کامل بسته بود هم ترورها ادامه داشت.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/IranProxyV2/8308" target="_blank">📅 21:00 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8306">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⚠️
ترامپ به فاکس نیوز:
‼️
در حال بررسی از سرگیری عملیات «پروژه آزادی» هستم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/IranProxyV2/8306" target="_blank">📅 18:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8305">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f5f6fd683.mp4?token=UnMS6cF5vD2GaxIVgzIVWwlrNsHsFKHIwjHHK2M8B9RyBRSkDUWIhHc2GlPg-d2jgAW1P64lbrklIL4PxCQUumwZS_xDmY1v9OfHr6kFe-cEAHMFXPF85SICbe_Pc5ZF8cvGiwIIkIsx2ON4EhbOzjg-AL9ZbX18Buy_yBzdPn6VJpFw3Th60-HB-7jOSmAzHVaQvkjxyZI9kWU5L_En1xsGTnHygx1JbnrN2XZ7Itc1-pSWl2uIojVE8-vJzJXQtKT2dk1Rb8pBUkGlu5uUkso0DB7evcl4nd30Qq8u6JssPrdAkhH7Jc_TdlAPes8mxj7Y-IU1qNhxrtD3eEzacA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f5f6fd683.mp4?token=UnMS6cF5vD2GaxIVgzIVWwlrNsHsFKHIwjHHK2M8B9RyBRSkDUWIhHc2GlPg-d2jgAW1P64lbrklIL4PxCQUumwZS_xDmY1v9OfHr6kFe-cEAHMFXPF85SICbe_Pc5ZF8cvGiwIIkIsx2ON4EhbOzjg-AL9ZbX18Buy_yBzdPn6VJpFw3Th60-HB-7jOSmAzHVaQvkjxyZI9kWU5L_En1xsGTnHygx1JbnrN2XZ7Itc1-pSWl2uIojVE8-vJzJXQtKT2dk1Rb8pBUkGlu5uUkso0DB7evcl4nd30Qq8u6JssPrdAkhH7Jc_TdlAPes8mxj7Y-IU1qNhxrtD3eEzacA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت زندگی مغازه دارا و آنلاین شاپا بعداز ۷۴ روز بسته بودن اینترنت!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/IranProxyV2/8305" target="_blank">📅 16:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8304">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
تصمیم‌گیری درباره بازگشت اینترنت به وضعیت عادی در دستور کار دولت
افشین، معاون علمی رئیس‌جمهور:
🔹
در دولت یک کارگروه زیر نظر معاونت اول رئیس جمهور برای تعیین تکلیف اینترنت در حال شکل‌گیری است. احتمالاً در این کارگروه تصمیمات قاطع خواهیم گرفت.
🔹
وضعیت اینترنت در دولت در حال پیگیری است. نظر دولت بازگشت اینترنت به وضعیت عادی است. قطعی اینترنت قطعاً به رتبه علمی ما ضربه می‌زند. در زمان قطعی اینترنت رتبه علمی ما پایین می‌آید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/IranProxyV2/8304" target="_blank">📅 16:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8303">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">dalage pezeshkian 2.npvt</div>
  <div class="tg-doc-extra">1.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8303" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/IranProxyV2/8303" target="_blank">📅 15:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8302">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">داریم بروز رسانی هایی میکنیم که  سرور های مخصوص تلگرام مستقیم وصل بشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/IranProxyV2/8302" target="_blank">📅 13:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8301">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoXfBfhmTeaRmATTgf_WdegqvzhTNpTw_vcjOeAJKAMUSVHHkhyzPodGGlwi8AnnA4kObPOAfrvJDq0-Rr5L9bqMRAFYjoEAyY9x-1o_tltnjJS5kdsZcXDwRaZweQi65rmj-NAfr4WTEdCT4aZb7u-M9qo2CrCIW_O99C5dpJIuxdRSaK3zUH1GZ6XLvM58_oehgddbMHcJg0_9imZ81giatib5xnR3-j24DXlSungUQ1ZfKBkIgIEk0GW9d6CV4xQmLINWs6uIuTIeE6Q52YxJ9oZ579Jde0G0hJLKbemU4r1YOfQHePQ7zSo98vqtmOxSO5TUi3QaGmtPwiKzfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
جهت اطلاع رسانی مجدد همچنان در تلاشم، که مشکل دیتاسنتر خارجمون رو برطرف کنم برای سرویس سرورای تلگرام، درحال حاضر همچنان فروش سرورای تلگرام از دیروز تو ربات غیرفعال شده، نگران نباشید برطرف خواهد شد
✔️
فعلا درحال حاضر سرویس های تانل با بهترین کیفیت و سرعت ، تنها سرویسمون که روی تمامی اپلیکیشن های
🎥
📸
✈️
💬
📞
🤖
🕹
📱
🔍
قابل استفاده میباشد و برای تمامی دیوایس ها واپلیکیشن ها اوکی هست، در پلن های (1 گیگ، 2 گیگ،3 گیگ و 5 گیگ) تو ربات موجود میباشد برای ثبت سفارش
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/IranProxyV2/8301" target="_blank">📅 03:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8300">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
صدا و سیما:
ایران آخرین پیشنهاد آمریکا را رد کرد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/IranProxyV2/8300" target="_blank">📅 01:43 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8299">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اختلال شدید در اینترنت داخلی
🔵
متاسفانه از دقایق گذشته اختلال بسیار شدیدی در اینترنت ملی ایران رخ داده به طوری که cdn آروان ؛ سیستم شاپرک ؛ سیستم همراه بانک برخی از بانک ها همچون بلو(سامان) و... قطع شدند یا دچار اختلال شدند.
🔵
بسیاری از سایت های ملی و داخلی نیز باز نمیشوند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/8299" target="_blank">📅 00:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8298">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رفقا پروکسیا مشکل خوردن مدیر فنیم داره هر جور شده مشکل حل میکنه از صبوریتون متشکریم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/IranProxyV2/8298" target="_blank">📅 00:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8297">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نتیجه رو زیر این پست پیش بینی کنید   @RUSSIAPROXYY
🇷🇺
پیامتون ادیت بخوره، قابل قبول نیست
❤</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8297" target="_blank">📅 00:49 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
