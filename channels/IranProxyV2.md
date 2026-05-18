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
<p>@IranProxyV2 • 👥 38.4K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 20:13:28</div>
<hr>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 318 · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 889 · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8424">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8420">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4wzQRtiM1mcIGTC05WkQYki3TVQZZVY-_46hfqlvTmwg3wOJFodjj1Uk6ukLSBKjywZO810yqNYohbJIHqFYo-djqL8neNZ2P7PsCdQ_ja_XY-X6-O2LLgjLwdNjdtuzKzUXM3nLmhrFCLZFO4Fnum7DmgQfbrzGPPhIUCLAj-y7bpykb2Ftg_sNPrxOHe99YUjkwOoBwLsMt5BUpVZxvSMAFpQNiVcuCJCGSEQLu1jC97QqSMMcUubiMPZHwyOp83mzt21AMTD4DNEN7hShE0WWsjs7PS0bfwi0Bb56Bdg5sxLk7mZKMPOkYnq2ZHUjKA2iELjHsExyOXT5Cb2KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8406">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2261382e-40ad-4259-9564-33734d96cf5c@varzesh3.com:80?path=%2Fws&security=none&encryption=none&host=nobody.fasterspeed.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjYPubZoYH6y1SlhjzVs6lMivIYu_nGpF_OKguWD3t5ZQgYhjX3i7rJtO-k290URFH-klWbS4_oqLuh2M2pC9WMgOLRkuM65s3E2NNx2iOP7p9e2Dnx-Dv7IOMeS2aj6_9o9QKXnvak1fRal3PxZme1suoviR8PI0gKcLMS7fcyd-6_1duSDJN3nHBY6auGkBpRRuKeJMTvrOWOZiOdMsbS55sTXuFTURXZ2IBEtTc0vVejPkpGLbsbSj1Xol8ws2RXM6fAUh2KwqFGUiR8akJnpeNJ-LfoEkHIyQcsbqMtDMJ4mq7iqhtSH2bi3jaGv-9ef4sW71evWsTWfg0h7pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8403">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8399">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrrSnDGNOnrvjAj0iVTktwq-KraSvXlxKvuE1i8vaAVJ0MrCs9hpXpFq3jA8u6uCeup0GOSPUS0XlcjORnzraKpDwhQnhYU9sWVKWACLaK3eH17zaXD43futDg9L89KcJHBLbz7EI2xaUUr1VzUR9MQqiJO3--Z0uTdGZXeJ3EBJqx0QcLqmPNhaCuRZCdjfXIEGbsU84ImL0nsOX0gZySVnekcwjp0ZFm7Z3yILCaziUI4rpWTtHEDzlhfiEeJB7VP4enDB2lpN3Q1Kp60NGjRPxnEgq1KYq7lhGfA-fKNdgaWhQR2CFdfVBe2-5WAXW7bWpOefrit8Ehh9FnC0DQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://36326231-3138-4166-b834-303439306131@185.143.234.96:80?encryption=none&security=none&type=ws&host=dl.tgmovie.bond&path=%2Fl%2Fw%2FaXD2QyDdS6vRQpxs%3Fed%3D2047#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=VYKqY31w3P-G9u6AkmJ3e8CLlXnhB7QikZ2DJbFrSmQtGsgdYhv6YxrMRInAwKfacgY1QYGOiW-qgueSPPSPBiKQjU4AFutXz1tLIuIimRD5ZfdQex8eF7P87i32VsqT7hPN4_o-xK31DKGU1TeD1UfXm4tneqh7SRURrY0l41H5JKlS_t1qH_oUHxCI4tOduA5zxibuZqOYxQRNfaPo8qNpMzaOM6ZYH8VcJVmvPkfTW6WZ10jfdphoQJzIL9L7R0JtaQ_h_2m7fWffNEa0QSOqGPXwt2JYxzNhCP6RhWd5Gk28Jp2NbIrm5DTpskJXN4kbcYOfK18VFY05m64Ecw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=VYKqY31w3P-G9u6AkmJ3e8CLlXnhB7QikZ2DJbFrSmQtGsgdYhv6YxrMRInAwKfacgY1QYGOiW-qgueSPPSPBiKQjU4AFutXz1tLIuIimRD5ZfdQex8eF7P87i32VsqT7hPN4_o-xK31DKGU1TeD1UfXm4tneqh7SRURrY0l41H5JKlS_t1qH_oUHxCI4tOduA5zxibuZqOYxQRNfaPo8qNpMzaOM6ZYH8VcJVmvPkfTW6WZ10jfdphoQJzIL9L7R0JtaQ_h_2m7fWffNEa0QSOqGPXwt2JYxzNhCP6RhWd5Gk28Jp2NbIrm5DTpskJXN4kbcYOfK18VFY05m64Ecw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=nWrUgsobdAR9uq8eSiHKRMRagWLizEalo1otsW7pXxP4x20NXyCx2_ZNb1LVLZYE8tfQ7wtlAIm-flJL4ApLzim9NKvEqRbQxlh6zNR0M-UOg09s8moIJ8P6GrLdqxRT6L2bKv_aeyvNBXY2UBMYvESmsSoT6Is-C8V5XqrekM6gVTAXYfGoRu48SFF8ypmdXn_BQKF5IaCSqdmlTHoNbdWdKWNidjDBVccWWomWGgFPP-EFZ0jc8k_YIp4R1pWQFnyAelCU-hTuHetYQOilCPSMdOUNv3zKXMfTNpAARAMb6R7jw9iNt96uQGsTjwdTbRGA_oUNb67w0a50ei_f8Y-829Pg5mCh0llpeZ0s_JngyN8aUyMkyeCHphkJ0SqaOF9of6oQgV784a51ehQDXCS_BPF2e4R1NIVVOr2wYRFEM7gheKEHlBTYQOiXkfNN4n1fwx1MGYE2VvpHSfVXWug9aesy4si0y56Q_1e-Vz-0tVchc__IugwfCAV7i5Axn4loePXGbROUszoAmlScHAza-AcAaAZRf_N4dD91T1RvgMq3Pnn1ema_mXuNL_TtEX5eaf1EynE5mte-yv5bYvPA3EITBoenSOMxcbtqhLBSuNjvZFWNQLz3fZnmmXBPh9q5pFdk4qoY1MGQlFt9b4qi1sJoF8Jffma9CdHkKCU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=nWrUgsobdAR9uq8eSiHKRMRagWLizEalo1otsW7pXxP4x20NXyCx2_ZNb1LVLZYE8tfQ7wtlAIm-flJL4ApLzim9NKvEqRbQxlh6zNR0M-UOg09s8moIJ8P6GrLdqxRT6L2bKv_aeyvNBXY2UBMYvESmsSoT6Is-C8V5XqrekM6gVTAXYfGoRu48SFF8ypmdXn_BQKF5IaCSqdmlTHoNbdWdKWNidjDBVccWWomWGgFPP-EFZ0jc8k_YIp4R1pWQFnyAelCU-hTuHetYQOilCPSMdOUNv3zKXMfTNpAARAMb6R7jw9iNt96uQGsTjwdTbRGA_oUNb67w0a50ei_f8Y-829Pg5mCh0llpeZ0s_JngyN8aUyMkyeCHphkJ0SqaOF9of6oQgV784a51ehQDXCS_BPF2e4R1NIVVOr2wYRFEM7gheKEHlBTYQOiXkfNN4n1fwx1MGYE2VvpHSfVXWug9aesy4si0y56Q_1e-Vz-0tVchc__IugwfCAV7i5Axn4loePXGbROUszoAmlScHAza-AcAaAZRf_N4dD91T1RvgMq3Pnn1ema_mXuNL_TtEX5eaf1EynE5mte-yv5bYvPA3EITBoenSOMxcbtqhLBSuNjvZFWNQLz3fZnmmXBPh9q5pFdk4qoY1MGQlFt9b4qi1sJoF8Jffma9CdHkKCU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5cy7cKHeDUjFxjLqjHIMetNt3h3bX6ZpFMrrwdEJTJyaG4MkGRB92HFw83_486YhUiIFelkMVS6XTbKVbAMk-270jFUr2iSFU_oaiBbPfhcwYCGhS6KTAm1qoLNF97gESgEdyJkrH90RxT7GDonWEGtKUSWcuoTBVnPhc_3OzTQJfX_-VsRxi2oGIKVyc7KHPCLxz7Q7glJIcKFOjBLErMYL_masTb8rLZGzu4Xp2LFpElJS54btfOyZJEe67dbsMPUNljA5pqrFqMKJFdMNeAHq8UeGe0Jdb7ETpLCQOxxR9BCMR5xO6Q8R_tqlHR_qaBCBrQ6jm05W2PsobIbxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8B604wGnOX1z2PxCui872H1lpu9jdwihEdCKzC11PzWcBTmtp8RS0r2jU0OX_7cNgpVNHdIkJiOGcfFCUh8FGSuOzQFKV_5_ZpBDeA-1LaZttsIT0eOSSFNtuBPaKmCfZYn_jcicEl58ZBLtPuFNx6rjEQbWVjy-cHpD8-ciRLPHWKy-KZh5z-XX2HdYm96p_IfsgAexotPuq8eY5MCJOSSKJ3195Ut8LrOEjiHXvjx0govDDKebChnYxQIcj-cxabITTjzVBPEpY1I1LMbZaNM7RYhegZE5qRlrp2l3cTuKqD1f7hqTshKHUPtU8uBbnOX0Vn7F60zE7sWleo4UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8373">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/koBTtTqSZgzlMEvmn7FP5FapmzeutJrFxo3hSKLh0I6-sbcMG3_njzPZEtBLvcBDuFC5U1TMemgqmD4LIiElUPmIkAUU3fs8g_fosGB43LPnqOzZR3HwKJm65zE96Iv8fL_Ig6YzPPW6_z4Ulwr1pcTpBGOKlXisJp6ih2kshZBSdE82UoLtJoTFnGUcFHH2qdVJh8SuBiDSUid6JeYncUdc_QsXz9LJiR0PD4Du3CV6dfgkxcuVmTrjKgEu4AMiMGxVwwoK8pt2sWicRPmvCZrmjntiVi124kkxtDj9CdEBIvGHHhL2DYEz8uhW7Y7siVSEOVqzdvp5XfmsPEYB8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/IranProxyV2/8369" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8368">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=Zwx-L1lylLpnKmWK1r0wE_JTMl1StwoRord_0fxleaH04jIZlevNCczhABlcFxyF1ynPXGVTf8e_70dT7_HTb-zvBCGI9KSYavv8uskeLe8Hu4iO_9CZZcXSRZxwL7-EfMtHB8m2m0DP9BgcU0D_IbbqHneiipGJQ4XDeUOQi3leNkjwYo3B3uNgD6vsoJtYaJ-wDLxEr_H6lfDBL04j4MZweZIi-BCvztvH5qo0MJhYAu4nqr2E_xEl88AHmVcYgH9anjwz7VhJ4kkONhcIXHoSaMJWE62Y3zTdybLPVJFvKz0wvajdSPeQEuyvLw9LxCsXgxL32PQ1K6-nDGBNLzamr8ePtXj-9qknf8oX4miEZtgdhw0uhbwv5poposmgepo2oYkcZfv7vv2etz4oOsWsuRlNWk119EuuOkdmWEEuY-UAhGun4P414CJto_IMSxJZ6YQoMBs1pYMUoOEetz4lS8TxW3K8OYTfaZmbAf2jhYwBGGj-k6VS9aAjRRnXChSLJl09evwgZ8kNmkvqq4ISOzyQfwKH7ZBa_VJ91XDnt4ipEYWV9isPMe1ij_uQXjS8km6Qvb3T351vc0NwXMCrwHt8S9Ct2nIjDHc0gsOa7qgoQwpB-KFi0SOjJJi8g8psbv2iAspgrDQheQyGLX2DOrOXc3nVZFfv1iQE6tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=Zwx-L1lylLpnKmWK1r0wE_JTMl1StwoRord_0fxleaH04jIZlevNCczhABlcFxyF1ynPXGVTf8e_70dT7_HTb-zvBCGI9KSYavv8uskeLe8Hu4iO_9CZZcXSRZxwL7-EfMtHB8m2m0DP9BgcU0D_IbbqHneiipGJQ4XDeUOQi3leNkjwYo3B3uNgD6vsoJtYaJ-wDLxEr_H6lfDBL04j4MZweZIi-BCvztvH5qo0MJhYAu4nqr2E_xEl88AHmVcYgH9anjwz7VhJ4kkONhcIXHoSaMJWE62Y3zTdybLPVJFvKz0wvajdSPeQEuyvLw9LxCsXgxL32PQ1K6-nDGBNLzamr8ePtXj-9qknf8oX4miEZtgdhw0uhbwv5poposmgepo2oYkcZfv7vv2etz4oOsWsuRlNWk119EuuOkdmWEEuY-UAhGun4P414CJto_IMSxJZ6YQoMBs1pYMUoOEetz4lS8TxW3K8OYTfaZmbAf2jhYwBGGj-k6VS9aAjRRnXChSLJl09evwgZ8kNmkvqq4ISOzyQfwKH7ZBa_VJ91XDnt4ipEYWV9isPMe1ij_uQXjS8km6Qvb3T351vc0NwXMCrwHt8S9Ct2nIjDHc0gsOa7qgoQwpB-KFi0SOjJJi8g8psbv2iAspgrDQheQyGLX2DOrOXc3nVZFfv1iQE6tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8365">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBgA005b3dTZXQ2P-HBn0Pa09_YxpIuUbm0yejmbGKCFH_DOjfabaS6w9UrYZ3SZ-kOpoexcbY1j5yeL4zrenGsZn835LHJAGzz733IGLvVMDrzFRDTwSbHJlAavi-gIayuCoazBscoGbFhIRd9IFwYeKeerytUl1xD43tbN-aM0XgzQVUX8Jv6ta7tyMLd2cXFNW11hX2fLrHMKIZsO_Xi4kjD6FEy1dtSb5zQnWHSQ5rQbA7PSm8b7-_Wwa-vh3rDlNyQKV7CGtqxX-87XQ3FI1CqoPs08-0Y0l8-B71Tlt5glxahCqRMoXxWR4Wc9FeyG4gTJGBZpMPmTbC7E_sTM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBgA005b3dTZXQ2P-HBn0Pa09_YxpIuUbm0yejmbGKCFH_DOjfabaS6w9UrYZ3SZ-kOpoexcbY1j5yeL4zrenGsZn835LHJAGzz733IGLvVMDrzFRDTwSbHJlAavi-gIayuCoazBscoGbFhIRd9IFwYeKeerytUl1xD43tbN-aM0XgzQVUX8Jv6ta7tyMLd2cXFNW11hX2fLrHMKIZsO_Xi4kjD6FEy1dtSb5zQnWHSQ5rQbA7PSm8b7-_Wwa-vh3rDlNyQKV7CGtqxX-87XQ3FI1CqoPs08-0Y0l8-B71Tlt5glxahCqRMoXxWR4Wc9FeyG4gTJGBZpMPmTbC7E_sTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8363">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uUUZXiy6o1SUJ4EfL9oc25EAdJUZfdQDeOW2QS8BgKdk8ofAEfKHwExTvu4JdAUuSvEBF-lLAnLI497lo-ofVoleNznRAK0A_C4KaCV6PP0kdn5x5luDW0ZYPlmK6gxOy2z-ySCaGPHEvCCP6410NiDIw3JNlJ0ASfaFs-Q28-bk2ZZKOAWasp7wpBy7UjHnPTDgjcnd2v4NtLmwUN_7LIF-X_h5FoxYvdOv6pIX6oYzGYnJol24fpbF65zP5m0QRxW5SKnyZ9n1jyTTl5D7x02pqi9UXvbABBFSFpe3m73eH7bz4twwnOuk8QqvLzACQrGL56nB_uhEAp9zDTymPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
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
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8358">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8357">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/IranProxyV2/8357" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8354">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ms6KIxCsvq0XGpUAAF52xGIU_03gIm2OiticnIzXCrnKdX2ec2KRsVl5A2V1g-Ha3_OUIkTunm7Wft645hJT6OTTTn4WETKPxhLx1Lq0CE4oWwAF6mmoOPsw98QL8V-bJf_EGJebuoZ2IUzCUYWAzRKiWgdeTzj2ZtyO7pkbmo7DtQxACtN2wNxE3-pH0VfzuPcldwJlnlWx9g5WYGlLwfZXenE2MdFIkvsv2J44OCJ1_VR0E7zZi0jvSg_02qE6bBK1uuDqQMg5zMpgJ8GSh0CgKdbKVgrwnNJgRHR7Yw4xJZ3sCVaBOCHKTfHpb54r4V7wHOyRhQcz3N1NQMVdQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8350">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8346">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">slipnet-enc://AQskvHpoSr0z/luIGDACbhKreNDTKyhhMA3DYlYmmHhr6T/THqqypSEZIR2ROKHLR6XP/iribGUsJGd/wwwh1ZLFTrR6kKY78tIX6XmbL6eLIwT2+Az997HmcivFgJpEtgDTqAQVkonbDemLykPWC/L86oUN+Bfoqg7S+FVTAWD2NIQa/11CwodDdSWh8KTKoVIV80wPNJXSS2qi4THuGu5jEoTVOenuOImriz65wsm4ASSgo750zT/dZvGGj0ynpjQVa+y9hxbby3u0Lu0qbp27pnXaUHzmoEh3jQVIQi5OAcX4VvcUetwhOtV6DXHU+vsZPWDcQUOpd/7/0wZW+EUN24SqPt9fGMIsFsKpHXPoJpUs2BB1PkC8TZymVkqwmjeO0Cey8oj1g+DCiR5r1jtWijUAv4yehzdzbDuU++T1J6Sj0nP7ADo9wGFllaneHyrpoGHXRSCiQtztJKw7qwEWTLBo0jLT1Lt76HyJ0xGn6lPM+evyYA4Pd3E1bwcaa9kh6kJ0BTIjfT2UBa+zd2L+UejzTjqrKrYW6whN792AmDFdS9CHY7Ho7F2PZf+wQx4E0BjdJ7MFpNfblxmmgD2SsxRqH/7IpWpb+mr48+kqlveInlB9RKTxdzdfufoY5s82opLQBhAsuyXEhcqMYgRLIUsUXiILutNRoc/vBq41mI4B02bmpcZR6JmcYTcU1pjWop1QQPNvo89WaaJWZxYBCjO+TtbhLFsN9VTXdVe6fMSNo524sRPA3Kk04YuQk3cugUbywKo/BUXCnss9G7ffIJgmxd6UK5GIunGf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/IranProxyV2/8346" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8345">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=EGr7iwwCVhl3JqVsuVypHr3X3he5yqZsC2RoCqyUMEzTf8CPdTlRiPcK-D63nOn3iIndnFt935V2O-ANUXWrljzcFhDoF9IRfFUIm4e38svuteUwfgVcNZCQDwmYUOmqx7XsNVQkm6kvXovptrzQkelw3rYUIGuokQ0Vy72zExwpCMfo8LLSZZb7-5f7WJgp0NOggt7eIWjFvKeKkGt3Pdyci48PZTvfAX-xnhDpigHGX3OXtrfSlIjaTMIdx4Qgb-KbLzIVRsk6a5fyEEWTL1OsCFWdG3UozS6_h-yxRJtoqLdnWgrpFtd0710ul2auZ9Q8H-DCmu30hEfTtlOgSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=EGr7iwwCVhl3JqVsuVypHr3X3he5yqZsC2RoCqyUMEzTf8CPdTlRiPcK-D63nOn3iIndnFt935V2O-ANUXWrljzcFhDoF9IRfFUIm4e38svuteUwfgVcNZCQDwmYUOmqx7XsNVQkm6kvXovptrzQkelw3rYUIGuokQ0Vy72zExwpCMfo8LLSZZb7-5f7WJgp0NOggt7eIWjFvKeKkGt3Pdyci48PZTvfAX-xnhDpigHGX3OXtrfSlIjaTMIdx4Qgb-KbLzIVRsk6a5fyEEWTL1OsCFWdG3UozS6_h-yxRJtoqLdnWgrpFtd0710ul2auZ9Q8H-DCmu30hEfTtlOgSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینک از وضعیت سرعت کانفیگ ها که بخاین تبدیل کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/IranProxyV2/8345" target="_blank">📅 19:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8344">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن   ایدی ادمین…</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/IranProxyV2/8344" target="_blank">📅 19:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8343">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">محمدرضا عارف از سوی مسعود پزشکیان به‌عنوان رییس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/IranProxyV2/8343" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8342">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن
ایدی ادمین
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/IranProxyV2/8342" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8341">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کانفیگ های پروکسیو یه تست بزنید مستقیم وصل بشید بدونه هیچ پروکسی بیایید تل ببنید بالا میاره و اینکه احتمالا ۲.۳ روز دیگ کانفیگ هاتون کلا عوض کنیم  یه تست بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8341" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8339">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eF_k1BiQff1a6r00kChVn14pwKsTbjdIHarU-9UaWAKemyKSN5qGjHnMFvN7Q2YdiNCWcHZpl_lcb3NZr1hVe7IcmgfuYmigK1RYr0B7BqIo1KU58Y5JaV_ME9Y_5A3IzVO9UdGDQMAzzSacJaF_ZpTNzS-X8bPZow5XX4wmx-5iEdoGK171qR0vIARlhSgI8DeMV-oJcSpIPCVEcmSnWVrCHwQciurvN0lWEokhFDssFswz1Va6SX2WOtqWhNnQ1O7xrY8c2vJUbzPN5QDSc1U_NApO7rIifdgsdoSUtTEtRsqHA0kpAepv9LFvvqsELZ8FDApYMprQ-dFbnaOZ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خدایا شکرت؛ دیروز اپل به صورت رسمی اولین نمایندگی خودشو در افغانستان افتتاح کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/IranProxyV2/8339" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8338">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">معاون ارتباطات شرکت مخابرات ایران: اینترنت بین‌الملل نباید با همان قیمت اینترنت ملی عرضه شود!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/IranProxyV2/8338" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8337">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/IranProxyV2/8337" target="_blank">📅 13:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8336">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/IranProxyV2/8336" target="_blank">📅 11:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8334">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mz4g0I-85XQAypmzYrUxw_1ysvZzbI46s_lNHMPDHKl0GCCb6LIO4XpXq1B33a5zxZM4sENlQ0XA4Vgo2A2OcJcOnV3xFxqKoIaTUhIlIl9VhE35959xx6uDpTwMZsTVVDp1YpFbJGGMdtOF-O8_uGByTwbGbvfa0W6KTW0uCSYcJG4B13fuIU2QcGGtZ33LhsOnvT34FJZIax5_6-llwikIglbKsqVrHClaoprTdqaaAVnjoaeP-cxXlHqcG9caheBnTGQJjbDNohrNfWCBF-iOaXfIFcupHiaF4FKW-x8IvELuUhCyfXAJ4GAKda6qpvpS_3RJuTK16yc5JV4kRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EzHcVmGgBPuJE-CDKwTFLvBMBneruzNpSIet82FF294LdbwTpEzE91Z-VS98wL08nJHbFF3DYKjXnk7Dqu6eIQ4P9SSN9MO4S3flUeH3d0YNVzr84foNaMHGI2j69635Bu_DleNwl_8fWeHbDOGJwOKEbVBkX2raHaIUuR7mXmGS6Qj5lYgZBqd8qfyoHW8SNOfTS0x8U9N4dk-r8CtgnPUJiTelVdIlUmyPB2KucIboDGQLsrfOQV7Z4rHgKPmdqCx--P5QByoARKOSmRn-Yms8ux68F0phMi_-Rq7vzAgiGV5dBJKSHtwzywcHR7XXPeJk1HDCbLgfCkmIYi8hEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صنف کفاشان و اغذیه فروشان هم شامل دریافت اینترنت پرو شدن.
به‌زودی کل مردم ایران شامل اینترنت پرو میشن که دقیقا همون اینترنت قبل از جنگه فقط به جای گیگی ۵ هزار تومن باید گیگی ۴۰ هزار تومن پول بدید.
و فقط اونایی که توانشو دارن میتونن از این کالای لوکس بهره‌مند بشن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/IranProxyV2/8334" target="_blank">📅 11:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8333">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/IranProxyV2/8333" target="_blank">📅 10:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8332">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://45cd71df-7b23-4568-8677-fdc4a0daa76e@protectnet.cloudinohost.com:443?security=tls&sni=protectnet.cloudinohost.com&alpn=h2,http/1.1&fp=chrome&type=ws&path=/&host=protectnet.cloudinohost.com&encryption=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/IranProxyV2/8332" target="_blank">📅 03:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8331">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✈️
Slipnet
slipnet-enc://AcwwsvYl4r7DajFRU6wa12enHS94jGWcw63dYwNxwSzZZDO03mNtFG6vROd+UO8opWIgDZkjjnUHlVvSaj/HvKW+p2HLBc4ETWvUWsMZpCwiUmAeEORd+qfA089iU7PBEHuvMqTIeRqwCA6OyylmfHRyIlB+dS4avIQQAJLxeW6G0ZMnp8HZ4VPpuiN2Vs3U7StRqxSwEP7f8wUXQy1DHgcCE9WD74CKd5RxaHADsaaT4Qj56xDB+DTB8l41JtvrbtjUVSNCS349vS8XyPhXi12t/YaAupzBKzSkPCXi8UjM8Ft2AyUuvLKTPgSMjJgI+vBT+16sztR9Q5n88GbrLNNWKD31CXYgjS4YNk8tLooUjYBgOKWmoBPVWCHej1RPyjs3lg64enMfTyX+WKjZ/fxrqH/8uGQZGj7qLjcGhGaohjHujN+ODCfxxAlK+6Y6eQFfld7UtXfyz9cTmhkk7mebn5exSrIv9o1auX6VVjUQ8xLMvhf6wwsD6vwQsblA6QeIvDoD8NUOfeKZFKrraoPjEdJexjOxcn9gbWSEM/QeqZB/lQ4LnfH6zHtP8PmH63PRZJTZUv6VlAovbrtWUp0ziB5fgISZTC4akBfBPTO32WXUTj+Wo1sSSeCH1rfVQAYoMqoQusLWWSHLm5Llfz5jW8qGwROFKxCq6HYzt4gLRZixvL44Dluxo+oyG14jHwsAmPVh05xydwjCI2XcpiJgX5De91xk+x39xMt7AwApPsraUbzuBscA/TU90Ehahp5NbRa0nr1Z44yGL0dC78sWZrPT5XtXbIE+Ydpd5qq3F1Y=
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/IranProxyV2/8331" target="_blank">📅 03:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8330">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
اطلاعیه سرویس سرور های تلگرام
⚠️
به دلیل شرایط پیش امده و قطع سرویس های تلگرام توسط دیتاسنتر خارج سه راه برای برطرف کردن مشکلتون وجود داره، دقت داشته باشین که این مشکل فقط رو سرویس های تلگرام هست و سرویس های تانل تو ربات هیچگونه مشکلی ندارند.
1⃣
- روش اول…</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/IranProxyV2/8330" target="_blank">📅 03:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8329">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/IranProxyV2/8329" target="_blank">📅 23:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8328">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/IranProxyV2/8328" target="_blank">📅 23:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8327">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سوال اینجاس اینا از بازی ها هم میترسن باز نمیکنن حداقل مردم حوصلشون سر نره
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/IranProxyV2/8327" target="_blank">📅 23:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8326">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✈️
علی قلهکی، خبرنگار:
🔻
تا امروز بیش از ۴۹۰ هزار سیمکارت پرو فعال شده است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/IranProxyV2/8326" target="_blank">📅 22:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8325">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">💎
𝗩𝟮𝗿𝗮𝘆𝗡𝗚 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻 or MahsaNG ( Psiphon)
vless://799f939b-964b-4416-84ac-18a6ace7fe70@camp.nahidapp.com:443?path=%2FIF_VPN_Bot&security=tls&encryption=none&insecure=0&host=camp.nahidapp.com&type=ws&allowInsecure=0&sni=camp.nahidapp.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/IranProxyV2/8325" target="_blank">📅 21:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8322">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iW5jBkZhUKHypX8nmMReJDT76N6doD-KOmf4ZnMOHqKctxNjLd-Rksjh8lh0mAhLPykVmmOAZHUaxzcN9Bofv0gTJe73Op1j5Ttc4zoKbfoXwQfTGF-J66AGtd2poPeAV1ZdDwiNtATn9NPqpYJ4fQE69giUUz_0o1AucnzW8cGtwLdUKSjqq7nEeydqDeQTb_7pqZ3p3P-SpE2KYorsyD_tfiLUzZihpLImE1ekRdPp6fdUdf2ckU0d4WaCHcHT_vOnW7ARXAcKofrR1ukd7J7UDKGhv9zp39hMYDE6ZEJGLWRw_Aj77vuzgljEHY7oPLDZXe3YEEO3V9AslP0bVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
وعده پزشکیان بالاخره درباره اینترنت :
◀️
ارتباطات و اینترنت به بخش جدانشدنی زندگی مردم تبدیل شده
‼️
به آقای عارف ماموریت دادم با لحاظ حساسیت‌های حکمرانی، نظر رهبری و وعده‌ای که به مردم داده بودم، در قالب ساختاری چابک موجبات خدمت‌رسانی بهتر دولت و تحقق انتظارات عمومی رو فراهم کنه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/IranProxyV2/8322" target="_blank">📅 21:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8321">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/IranProxyV2/8321" target="_blank">📅 20:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8320">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G982juDcAauCIvLvpy_bbrVw8ZsIB4Xbu0xcYfoPmt2XQP77bbOOr7BkPuO8M41PjdFOke3RbdYVgVzr30SVTrV5w1LlHZyiRjoZcbn81qLVCpAN4sbmM_KyJOkUV7hrr1zEgcV7AiOjk3qCh-iJkrqCjrAiv9KQIYV3vMzlD6qtLloa54MBRpCi3kRVKfBbmR5xKk9uEAl7sPDvS7RVZu8n-Ev8H2KA66KkouYubpUehHszi2SVoT2R0efVFODOTWwFvLSCv5ssKY-qu_HsJJvM6PE9rirTm_tD5G6fd8Ca1K0y69I7kfWwKNpqoWv62gNnpPYASIbpquAhGSfJAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت اینترنت پرو
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/IranProxyV2/8320" target="_blank">📅 20:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8319">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/8319" target="_blank">📅 18:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8318">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de826422e1.mp4?token=k8quFTGU_WSEGef4FpzR-JwmUt2QG0KglQ0iUtj6kdGe_w_a1lrBGUVehs5h4GBi6YRDo8MrJKW4qTS67IIorWTiwvID0RNeVoe2P2xI3R3HFwuAQhjMMpIu19_ezkziGsRBLu6M_tvGbR1fLVP6zg4EYePQblSHn1wgVHhevl-vuO3CZ5X_P7woayqCbpD0u5UDQ_r0GB7lSLAmQp49kUkBzoTZZLYglJ7j92fh9adfe6x9c3lNs66gXN9BD4quBQ0QQGQQSKHyV0oCYwkGo5a20W_vnMc3wCWbLikecIZhI8wKN1OrHss5v9HGvUlYJYCtkqJa8eZ8yAi0MMg-PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de826422e1.mp4?token=k8quFTGU_WSEGef4FpzR-JwmUt2QG0KglQ0iUtj6kdGe_w_a1lrBGUVehs5h4GBi6YRDo8MrJKW4qTS67IIorWTiwvID0RNeVoe2P2xI3R3HFwuAQhjMMpIu19_ezkziGsRBLu6M_tvGbR1fLVP6zg4EYePQblSHn1wgVHhevl-vuO3CZ5X_P7woayqCbpD0u5UDQ_r0GB7lSLAmQp49kUkBzoTZZLYglJ7j92fh9adfe6x9c3lNs66gXN9BD4quBQ0QQGQQSKHyV0oCYwkGo5a20W_vnMc3wCWbLikecIZhI8wKN1OrHss5v9HGvUlYJYCtkqJa8eZ8yAi0MMg-PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شهبازی مجری صداوسیما خطاب به مردم ایران:
اگه اینترنت 5G که افغانستان داره و مسترکارت که سوریه داره اینقد براتون مهمه؛ خب برین همون افغانستان و سوریه زندگی کنین!
﻿
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/IranProxyV2/8318" target="_blank">📅 16:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8317">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ایران اینترنت ندارد، روز هفتاد و چهارم …
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/IranProxyV2/8317" target="_blank">📅 13:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8316">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⭕️
اطلاعیه:
وزیر ارتباطات گفت در تلاش برای برقراری اینترنت بین‌الملل در اسرع وقت هستیم.
همچنین طی پیگیری‌ از ISP اعلام کردند که اینترنت بین المللی شبکه خانگی متصل شده است اما هنوز زمان مشخصی در مورد اتصال دیتاسنترها به اینترنت بین المللی وجود ندارد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/IranProxyV2/8316" target="_blank">📅 12:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8315">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde1d5a77d.mp4?token=mNZkaEt5oYyMzkp5zO_3CkgXRL6-kUoFkiQUztP3dXYQVXwGFkwFZxh6_QPSiDPDlh8kLuhDPZb_s7zvrsUh2u8vxWZfwq_QjsF7ABOP0J4nx4yfivSbhTDjB8O-qYQahQhOq7r5njU9oDORC79XqVB1s786O6ap7X46IuuhoKAc83VweezhHQL8iunOQS1YX1cNkfNbORn6dXlJobbxzPPX3RjrCRu6S41GhwFXpKBKA4MAhgbTbdwzeljqggSlMtBt4kdWpncydlHQJ1rGH5HGwBeGeLTwOcnPCKTVcKSho7OYtF79totZPZUmpWO-mEFmGJPwgAIV3goEWbClCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde1d5a77d.mp4?token=mNZkaEt5oYyMzkp5zO_3CkgXRL6-kUoFkiQUztP3dXYQVXwGFkwFZxh6_QPSiDPDlh8kLuhDPZb_s7zvrsUh2u8vxWZfwq_QjsF7ABOP0J4nx4yfivSbhTDjB8O-qYQahQhOq7r5njU9oDORC79XqVB1s786O6ap7X46IuuhoKAc83VweezhHQL8iunOQS1YX1cNkfNbORn6dXlJobbxzPPX3RjrCRu6S41GhwFXpKBKA4MAhgbTbdwzeljqggSlMtBt4kdWpncydlHQJ1rGH5HGwBeGeLTwOcnPCKTVcKSho7OYtF79totZPZUmpWO-mEFmGJPwgAIV3goEWbClCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهاجرانی:
اینترنت حق مردم است؛ عصبانیت مردم کاملا درست است/ عامل این عصبانیت دشمنانی هستند که باعث می‌شوند فضای امنیتی ما مخدوش شود
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8315" target="_blank">📅 11:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8314">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اژه‌ای: اینترنت پرو و سفید مثل پتک در ذهن مردم شده است
🔹
رئیس قوه قضاییه در جلسه با وزیر ارتباطات: مسئله‌ اینترنت پرو و سفید مثل پتک در ذهن مردم شده و باید با موارد خلاف قانون در این موضوع برخورد شود.
🔹
در این جلسه دادستان کل کشور و وزیر ارتباطات به رئیس قوه‌قضائیه گفتند با بررسی‌های صورت‌گرفته، احراز تخلف در قضیهٔ موسوم به «خط‌های سفید و اینترنت‌پرو»، قطعی و حتمی است./جماران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/IranProxyV2/8314" target="_blank">📅 11:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8313">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">vless://8b7dbddf-fe0a-4405-b8e9-bfac4d9439ef@185.143.233.235:8080?path=%2F&security=none&encryption=none&host=MHI.ARTARONA.IR&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/IranProxyV2/8313" target="_blank">📅 11:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8312">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">V2ray + Psiphon:
vless://3728fc28-910c-4a9c-888c-c08c3e2f4a06@snapp.ir:2052?encryption=none&type=ws&path=%2Freq2&host=snapp1.gptpersian.ir#musiclovers85
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8312" target="_blank">📅 10:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8311">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">احتمالا اکه پروکسیا درست نشه با کانفیگ های ثابت جاشو براتون عوض کنیم اطلاع میدیم خدمتتون بابت صبوریتون متشکریم</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/IranProxyV2/8311" target="_blank">📅 00:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8310">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حجم سفارشات ربات بسیار بالاست موجودیش تموم شده بود مجدد شارژ شد، صبور باشین، دارم یکی یکی رسیدارو صحت سنجی و تایید میکنم با تشکر
❤️
💲
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/IranProxyV2/8310" target="_blank">📅 23:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8309">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqVSnJ-SRec-NyetgB4ZYMcLyAK_AGoseUjONXp76l0_2rx62i9A1JUgTHZeWYihBAZBp9b5OfXVvfE2lIUy--HgZowtK15o-LmE81QIce6SUvgPuLxB8WlqEHC7tMj8Bi3gCvU7zS9Ks3GpBqdPOUOY3MQ7sujIduNR-ficWaKYvx1hG1GyWp_1CNCXhZkR1De4HRRNNwwiLu5eHhVeR5kdvGFA9N_I9dJA6MJpa3BsaBWXV0vYpnAeCukaqud7uqyP6l7BZ6vyybUvFeFIhq-sULTeWmhuj79WlyaLd0dQWAtRNL1HFaBDhyOJNrrCAEyGGXQ7t2txDgvURVQQeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایزه چالش دیشب، برد 2-0 بارسا درست پیش بینی کرده بود
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/IranProxyV2/8309" target="_blank">📅 23:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8308">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
معاون علمی پزشکیان:
حتی در شرایط جنگی هم بستن اینترنت راهکار نیست، زیرا وقتی کامل بسته بود هم ترورها ادامه داشت.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/IranProxyV2/8308" target="_blank">📅 21:00 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8306">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⚠️
ترامپ به فاکس نیوز:
‼️
در حال بررسی از سرگیری عملیات «پروژه آزادی» هستم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/IranProxyV2/8306" target="_blank">📅 18:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8305">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f5f6fd683.mp4?token=IttL8QA2g3pQ2XnFh50dNTXnTNxbg5E45DzDndBpaVRqPLyKMbQ5pR38PBenWWLWX9bvHp6UM6qeQWdASHHvSsjD9LpUXUHg4HWYVNwnv1ng-phb2dSN6qEmBeYnKrw5RA2EwvUekcwp0MEPANxC-Ws_mBJ_nySQpJUVN0QrtfQ0EdCBsw8o6bixVJRR3DO9TiwvXoS_aRGZ_CGXliKRbzeQrgY5b3pr3UXPogh2JH_VVJmINkJ4Mmw7YRq3EdZn2h6WxXC_SHdXIMCCOQhZN9sKhIbuux0bsLKCbEaTxrcJ8RBHe5EvxsNWQ3EIo5C_YfjJwKKbFsSCEy0d2UMQXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f5f6fd683.mp4?token=IttL8QA2g3pQ2XnFh50dNTXnTNxbg5E45DzDndBpaVRqPLyKMbQ5pR38PBenWWLWX9bvHp6UM6qeQWdASHHvSsjD9LpUXUHg4HWYVNwnv1ng-phb2dSN6qEmBeYnKrw5RA2EwvUekcwp0MEPANxC-Ws_mBJ_nySQpJUVN0QrtfQ0EdCBsw8o6bixVJRR3DO9TiwvXoS_aRGZ_CGXliKRbzeQrgY5b3pr3UXPogh2JH_VVJmINkJ4Mmw7YRq3EdZn2h6WxXC_SHdXIMCCOQhZN9sKhIbuux0bsLKCbEaTxrcJ8RBHe5EvxsNWQ3EIo5C_YfjJwKKbFsSCEy0d2UMQXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت زندگی مغازه دارا و آنلاین شاپا بعداز ۷۴ روز بسته بودن اینترنت!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/IranProxyV2/8305" target="_blank">📅 16:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8304">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
تصمیم‌گیری درباره بازگشت اینترنت به وضعیت عادی در دستور کار دولت
افشین، معاون علمی رئیس‌جمهور:
🔹
در دولت یک کارگروه زیر نظر معاونت اول رئیس جمهور برای تعیین تکلیف اینترنت در حال شکل‌گیری است. احتمالاً در این کارگروه تصمیمات قاطع خواهیم گرفت.
🔹
وضعیت اینترنت در دولت در حال پیگیری است. نظر دولت بازگشت اینترنت به وضعیت عادی است. قطعی اینترنت قطعاً به رتبه علمی ما ضربه می‌زند. در زمان قطعی اینترنت رتبه علمی ما پایین می‌آید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/IranProxyV2/8304" target="_blank">📅 16:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8303">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/IranProxyV2/8303" target="_blank">📅 15:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8302">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">داریم بروز رسانی هایی میکنیم که  سرور های مخصوص تلگرام مستقیم وصل بشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/IranProxyV2/8302" target="_blank">📅 13:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8301">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKwTfbvsQYCwoogXUIHaHJU93wOcl3k5BcOUiwDXcZf7EJpmWDJ5wZzaA00PUtoMBJqB1pZf3RFII1n2jNoLmjG9Rpr65HMWNUJx9fG1V251YbqjmxubarKh6sEHr7c3huKAZZyt1KkNcY20RqdlIytBNQDPJxsi7B7j2ttNMGud8-SQrqBfSvlSw1ompW4-RED1UtKxbk359zAjtCuc5eeQn5B1HzuO9aCWvADAIhTBqeqmTz4IW5qWhLpKGUleCLT0Pg0qpBEXugl9HOfqz5Y6EYEZJK6SiWVJf8Es4fvda9NwfiTrlonbOXg4ol0H2I0pEHXYhT6ELlfsOLXKAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/IranProxyV2/8301" target="_blank">📅 03:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8300">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
صدا و سیما:
ایران آخرین پیشنهاد آمریکا را رد کرد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/IranProxyV2/8300" target="_blank">📅 01:43 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8299">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رفقا پروکسیا مشکل خوردن مدیر فنیم داره هر جور شده مشکل حل میکنه از صبوریتون متشکریم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/IranProxyV2/8298" target="_blank">📅 00:50 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
