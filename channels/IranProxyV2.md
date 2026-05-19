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
<img src="https://cdn4.telesco.pe/file/bIxvR_Ldr-GnFhlKeRWWWbhtUoHLAHylvHpDJONiCn2uXm6lHfUzY3RhHIzazWUy3rbpDj9f6xhEYVbYotBULEhOqASMc1gbTnOdfvzTrgOXEhYBmalfagDvySPORsu42ZyAvwuQrj2dS0x_uVv3V-vujp5CTlQwZclo1lGnvn8IbmcI991N0gG0GGzjkPE9FtkYS98Le6fkw0MUpZ2nX5wUvkXIZR1M8ikJuRBvhUdZGpXNeSB-Bv2-uGP-RA4787nkVHY7xbg1tH02AGX1Nye346tbeCm-88oHCJVJnzmo5SnaZil6n0d9eT0LR6DVuwGHw61jhKpqcFhzVb4ZDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 38.5K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 10:30:24</div>
<hr>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMvCN4tYaF4tBkn6IqtM8V9K8yPwWPE9OhweWFHQvZuR6yOS7gUGU1LOZr9PbDYL_h3eSfFeCXcP6FaGv697LzX523KmuCNxDEZoEOiUNDziZ8xRoUyq-XDI9ML4_slVg36POruvVnDXVBF5-WA58NgADFe_yU7H_gbgA5r2eqikPdkWUapuMR-mhdpIV8VuDk8NzgcN7MoIdnyumQwa_1Lr29008-Kl_ZTFpFdYqHIIRcI_KH8WnN4PgVh4pcvaX5mB-e8jtn8qGrSposX3MBVkKAvqC9AH8KyXyGNTXpRSypf3Oi6DyIGR-HeBjrDkaNjZYhYZwzhkDXhETpMXvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 324 · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8437">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2c72062a-a542-4b9b-97ac-0b636930d7c7@65.109.112.38:30366?security=none&allowInsecure=0&encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRuN34C1OAZXd4Grt49NvU6fdIfIwDLHkPbXHwKXcTZW3PXE7N775PI07dzL-YCZniT690mypVdTv6ppmGrbdyU3hAw-gCERkR4a7T2vE-p5yzG7ko9kzWSFvntmP8-tT8OKTQhx6Soh-Y3cG0K5TZ7b44_T2LMPOj5TRKASVuVF0Png7G-_j6IezVHbtZjvd9ZsPwFFGfs4Yx_lAPTYKdYJEP7puwxWytFikEqovyB5vqEMg7g4jTsuvWog5npFh3IjUm2fEC6b17SHzUb_ODDEoivNV6J4LXyQe0GUqFV-VpiYyguvD-Zk8D1dhukwOHv8UgQLIUM4BRPFk0jvOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8424">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8420">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpSISVgveqRXYjiC0GuQVgjHVll8Vo9MnmgTDgTVY5erSc8lTJhUuSj_Gbv16BYIzz7bJHUVfzUVkqqC4omve_pM89_VnrNsCuTI1VBQP_4oJinwaB0U65gY60QeQ-MVwxwkDlwaT8F0AiFsW3UE720XKU2wU_9875jWkGsuZaP2TnbZyyAs6fmnarmW_gs4JFTysZyiv-ihIdWnVPfF0H3in3kBMd6lEvg1m1aMkb3qgN9BKzB-DzTFZKmAEx-BidUH9h-EPwscuZUJO3XVUzgudKdfp-3ZGUeUiHEqhuy3U-ecIf9ZU7lpGiUMq1bt--p3WRi9oBZTMTGp15qzLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=mcWvvn9JnfL7ZEnweFn3rpnPsQalPBgoR9_blpBk9rQWWdc4Cr5UL_x7ZxGrjVTCg_VcOXnfUz1UUi6OZTrgia7UYAxD_lvg0c52eoay4Hp9MS6WFsvZkdX5rDg78mkzD_8__-MNeE1x2uM2SYEydxo4NrxLOm0TS1LuUsMq8jC0dlEu8QeTQGdLHTKqTZoTyrnGvRQwzMXKxVXjJ68dnXtY4QxKVppF2QbTWwOVKD-3hAdff2BHyFGVKB0OrWfMwcLzYlgVGbfxJDOadD663G1CwOa0L_6Mwa55vC2D3KowLSpxronln7yUKcJLqP8tD3mbAUra--AYcyQ1Q2DWZh-rrLUJBC_Hc8Z4P4eY1RgrhDGFAEwPK_SoTOYetr_ZskdyETp762btSsYdMMxMvKPffL9tt2nWkd99z5uisjviTBpfVrTapEr2sVinWN8SN18aUBAw2ZiDpr0uyrmencFMF1N9IGX1w605zfHebsotJToS_BjY4PxPUEZr9ZQE1aCJtsgD5NpYin6q57bxa4x6wnWOXxfdywDsymzhJnv31VGJcfQzqGFvo6NWIw17PP8FQZPZ2JgCPQQiAXqfhXk6G2WsKFtLsq1HKnKJdlt3cWjWjBY82v3GkxtbxyHHWgOVj3_McjhIgpNeXyHLNUOyPTrCe0eVWBqjuRs6CTk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=mcWvvn9JnfL7ZEnweFn3rpnPsQalPBgoR9_blpBk9rQWWdc4Cr5UL_x7ZxGrjVTCg_VcOXnfUz1UUi6OZTrgia7UYAxD_lvg0c52eoay4Hp9MS6WFsvZkdX5rDg78mkzD_8__-MNeE1x2uM2SYEydxo4NrxLOm0TS1LuUsMq8jC0dlEu8QeTQGdLHTKqTZoTyrnGvRQwzMXKxVXjJ68dnXtY4QxKVppF2QbTWwOVKD-3hAdff2BHyFGVKB0OrWfMwcLzYlgVGbfxJDOadD663G1CwOa0L_6Mwa55vC2D3KowLSpxronln7yUKcJLqP8tD3mbAUra--AYcyQ1Q2DWZh-rrLUJBC_Hc8Z4P4eY1RgrhDGFAEwPK_SoTOYetr_ZskdyETp762btSsYdMMxMvKPffL9tt2nWkd99z5uisjviTBpfVrTapEr2sVinWN8SN18aUBAw2ZiDpr0uyrmencFMF1N9IGX1w605zfHebsotJToS_BjY4PxPUEZr9ZQE1aCJtsgD5NpYin6q57bxa4x6wnWOXxfdywDsymzhJnv31VGJcfQzqGFvo6NWIw17PP8FQZPZ2JgCPQQiAXqfhXk6G2WsKFtLsq1HKnKJdlt3cWjWjBY82v3GkxtbxyHHWgOVj3_McjhIgpNeXyHLNUOyPTrCe0eVWBqjuRs6CTk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرعت سرور های همین الان
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnMokMJT4lPFJKqcSS8glXtkUYo-LzEhMSLLi8pVgiU31c8oDmhJy73m3oRYyaUQDJdm9k8hNnhxCQ4e2SDXMMCjc268k2Wz7pTNkbagxWHbboBxLIsuhBjffXQTiDDR3POrxPa4MSyQrQr69DFXoRXM0fOx6odfOvP-fvvUapwg7yUR5lh7zZvxrohIZxQ_yLJq51pCB-EKs_Ls1kUSjmzAHzpVP4llUftKXut9EYQajoleZC7aVeKbnfIFQDCaZ413wG6pBISDW86TIRt9luHRxxe1F_jwI3UN8bpdAwOtRD2VPeuSz5__Tlw0E5QFQV3JI9Rx4hfCIi4dajRYsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vi9FPPZfQWYMuTY0WG-vCHy1nWb1v4lW4NYdBds46xpt7UloTqEl2UCH9bMilw2DSzaHT-5gbftkxbrT8m5RALu3ILA8z3UdkysVefnXZ_GLmX259Pihm1cqPEUj6A3Mv8T3KS_CHtGuokVa7-nFiCTGU9La_Jo1rFMub_CVn2WHxFjQc7D1NxECjrYALoEvpDhpi7bIVxTXQ4ttKo6raAt0pZ7mBNZojA4uLB5RT-goDhK2tBaKwS8GBBELV2eRorNS6JCFUkH_R5W2XV9s3rp7v5SqU-daQEa3xJenu42T_lOu6LHo8-ql9k-WMlxVlrZnwXGgTiZo6vgEuhnRhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8406">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2261382e-40ad-4259-9564-33734d96cf5c@varzesh3.com:80?path=%2Fws&security=none&encryption=none&host=nobody.fasterspeed.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/St2hCj2Tsdo_akFU_wQOhzVdCqvVfQ84wqQhzJFZQnA98FudHhh3KPfV5iS6TZGZCsTRPT14-KsMfglFu1dP-WsK7Ld6ZFzRjYNhonjtCJJn0rI0ljf-IKycdsBk6OW2t3KkbZsuWqk-E5fNX-HWgzsbTbpk1Jh6ARY5wwVRODPL-j2bhT8LA2Qa_CiN4dRGgcxOKa-qItwibDPtg2rvw0sflvICgg08nESlzhu93jlcYHi8xHuUUgWfZUfLyNY65QlJLTB4FxWEh-g6M4ndMOoDWKdsXkYZ2_dAPT5MqX5fRsm8Xx4Hp_K46V7dv8A26RYt2d5zcj0o0xmvemvteQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8403">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8399">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://36326231-3138-4166-b834-303439306131@185.143.234.96:80?encryption=none&security=none&type=ws&host=dl.tgmovie.bond&path=%2Fl%2Fw%2FaXD2QyDdS6vRQpxs%3Fed%3D2047#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=PZm7Vjn3MQ_E6jryF5AQ30ghJJYkDYKZ2_E-ag7ORIVOR8PQ8LXwvIpB8VYpCywu4I_tgHL2csDO1fC-Q-T1BPh4Q3ejAInhNubOaB8CHzc4Zv9uPDb2NO8eLfzJYZuuE8Su69CSZOy5YVclg4SI3DEu06O-7iEuKmg9tmkTK0ING3IWCaPZi7o-BbCa11cqQiN4tZt7wTsiv7b69DLKUtEZVuP0rfVVDqhN0gTUe5tDcw_T3tn_K_bw8aJKJm9gvfRX0r7JVR95AVoXelYPATBTrYSRq7bzH4jyADTwTUZ5aAurp431Gz65WWl0wCQImA2duUI72V1uTtZggv2OJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=PZm7Vjn3MQ_E6jryF5AQ30ghJJYkDYKZ2_E-ag7ORIVOR8PQ8LXwvIpB8VYpCywu4I_tgHL2csDO1fC-Q-T1BPh4Q3ejAInhNubOaB8CHzc4Zv9uPDb2NO8eLfzJYZuuE8Su69CSZOy5YVclg4SI3DEu06O-7iEuKmg9tmkTK0ING3IWCaPZi7o-BbCa11cqQiN4tZt7wTsiv7b69DLKUtEZVuP0rfVVDqhN0gTUe5tDcw_T3tn_K_bw8aJKJm9gvfRX0r7JVR95AVoXelYPATBTrYSRq7bzH4jyADTwTUZ5aAurp431Gz65WWl0wCQImA2duUI72V1uTtZggv2OJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=Vpx5Fs1sfR1Oe62T3fDBTRFuLFMqoe8CJqOO3IpG6ijWYLzPGoDdb_OCyljHnWHbwlw-dA0HddtDIgZN4iGR-XBAcVqJqE2-OiI0Z2Bh4HfyoRXEc6QEEOWcSTkvmGwat4jsi6ch4jrQshUZ2GT_kwFtWRVF0dfy_Jf2LJ_u-4VbKKHecuemIanS3BeHdwEBreL5ollaHT9VBR45fwvx6i5Rx_ZX4GKcfhrGorYhCLTHrlqfhUUmjPOYimUqWvtIfWOIrweMpCH9krY9hbfSK78tqavQTBX9uoG05H8VYT52mVzGHcT4BByzYzRjgzBGjF052XWPicmz03yiY7HhmYURiXYUrMb9zB0bz4KOlro3VbFYRr8wHs2Bx1wp8ikVgnmBFTHq5bndNip51Io2U0lZY364YQYOo-Gs2pdCiGHrGYT6QjsOBbpxfmO6u9y4DpH0lf_yCKmDUJ7dcZ5hJTFGe6FcncbflqEO5qCQ1xT4Np4JELe7T5ImIFFl4-Kg_5EyfCWub8MQVDs7w2Ri3ZoLL0k5TNsIRODLH9UmdSquRlRewhLShOxpLz6dyBiVo8djYDC7FzyiniOtOpJ2BkOYs2Dv9Axysm1mRW4QN--0Exaq_ufYkKrOPl1OcXTezLwgqW_bmW3ub9FoiiQSYB1nv943Oy_Tym85Roh3_TM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=Vpx5Fs1sfR1Oe62T3fDBTRFuLFMqoe8CJqOO3IpG6ijWYLzPGoDdb_OCyljHnWHbwlw-dA0HddtDIgZN4iGR-XBAcVqJqE2-OiI0Z2Bh4HfyoRXEc6QEEOWcSTkvmGwat4jsi6ch4jrQshUZ2GT_kwFtWRVF0dfy_Jf2LJ_u-4VbKKHecuemIanS3BeHdwEBreL5ollaHT9VBR45fwvx6i5Rx_ZX4GKcfhrGorYhCLTHrlqfhUUmjPOYimUqWvtIfWOIrweMpCH9krY9hbfSK78tqavQTBX9uoG05H8VYT52mVzGHcT4BByzYzRjgzBGjF052XWPicmz03yiY7HhmYURiXYUrMb9zB0bz4KOlro3VbFYRr8wHs2Bx1wp8ikVgnmBFTHq5bndNip51Io2U0lZY364YQYOo-Gs2pdCiGHrGYT6QjsOBbpxfmO6u9y4DpH0lf_yCKmDUJ7dcZ5hJTFGe6FcncbflqEO5qCQ1xT4Np4JELe7T5ImIFFl4-Kg_5EyfCWub8MQVDs7w2Ri3ZoLL0k5TNsIRODLH9UmdSquRlRewhLShOxpLz6dyBiVo8djYDC7FzyiniOtOpJ2BkOYs2Dv9Axysm1mRW4QN--0Exaq_ufYkKrOPl1OcXTezLwgqW_bmW3ub9FoiiQSYB1nv943Oy_Tym85Roh3_TM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMt8nsbmnPp4u-9gfkNZRYAqt6Cp6Ja61EDKOAIXHlRMavuThXmhb-a4arsi2rFofPaisSEM-7c9hEbLpS7D-3CivMPf3y8byF2wkLPdMHqeY3cMApgXpKbdgh71iWm3Y5ZwURIGnjzEut5e0BgOlQ6rsrPz4hKE6QF5TV7PzmntlcpnltvHRE1tFLywe77wD1QiG1nYSRDk4Mp2_2DxdC72swjyN_GsBxF_rZrmAIZrgFGZ4qTZyfncGUmOf5M8wDziYy8Dtq_lvPMypGsb4qXBD_g8tXxfA-gwGJ-MP30sukZ-uPKzb_c_kZJfm8Zh6po7Iv3J2zLCV1E7zHZcTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZG7BeS_4j78a-xmQGgt-s5xFZdImErfpUlBGPSPXExiC5JPpgM1ySeYk8c3PeXosa_onFNtluMb7qMqpsxR3WeYRAXcfYkadCmnfpkbG659QTix50HHFBYitQ-823gjTm8LDW7vEOPBX2hfQ3QmQZ90Vn_JxHqGOXNZTIu-iYGVUVAzYgExpXhErRJcIVE6V0PblfiP0O7qvn-iI-RGi1mEJVyjQue0DFMRJmckFDJqxp25R5FwBL_ocYUu_tCvMD1FNh6Sls71E6pESYryJjqBKimddClzHt9kA5WSnLh3PVdmhTO3kK7RkFcAzggYX9XIqId2O1XkZyuPQE1nQ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8373">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uq3M1-2UiTCf4F23N8wxgI1URSghbxDnf6oJ8MaKQ1SWXEqN4P1Q2CQADjwyxNdGdh2AWbWSwTzQBHYf-wd8-UrSnqXOqlnn6FT-K9y-UC9kW_FQ51DFhh07cSWhHH02XF8xr2LHN2sDzVOLhZMlI9nHpAuXdXh602q8zTaBBjBNrbZ4TBX8mg40EB4hk3_fNOz-T8sz6vR5odK0BV4CbCySyfjRfb8YFbXfalJECdYYIzOkGn7jl-bGMaxW7izjOcjlgULieOj_5Nn1RoSkSvNpmChrxVNqkGKSuPq75f19Q1ydpcIKZawPxV2Ee_E227AfWvHrKSKG5gf2_ydjAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/IranProxyV2/8369" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8368">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=EDU6eY-3HCk3EiZAwoqyJ79Oy1GfPL3DBf0dT1E3o6cnX4sBFmaLtcpAIjvq3y_MILzntWt3rA0vS0S1vJ6P3F0_l6R1D9p7P-zAQx4fVZ5-yPurlIRIjIc6OSkq2PbFNVi1VJWx0XXHb1YLp5C6Z5vH-Sloq5PJY1mZIPasvYbRrEhJiX1wkFcJqBOMf1shwnunUJy61bW-Xht5uKT5nwKXU6P2a-yL3qYOjEI4DNyrFp7J6fiEyhG74bB1IKDg-lBIv8IT_qrjKEmFFdAyZXqjXmfFUCE2T6DOsxllKvfHLK4Lt61o6uiz6fyylSCuHJrwgC1GEFvyqghTdfsSCmbY45XvqD0KCxzh8T2EuIaX1E2FB0a-o1n0TQxHFZ91D2gF1VZhlN2jVd3zMbLx8hSgkjGXn1Co-LH2YCZj0ot4lc1iNBm1N0jSwgdDi1H19JIWyrU_qRj-ZgejJJe7JKbGChuNyoFsacdfaDiahGTdq1tUMXHc1jRLv5xxJ87FTHCJP_uttnMBISY80PbB2EHxY93Al3KIwoundv35tnN8_-h2s6GEJLrFP7h5VsrNPDeta5hZI9RR5G6xxecXTwtEaTovVhkQz_n5wGK6u9IFCG3ng6kmawslE28THGN2jWj8HvNDdCEVClpQPJLtKr6v6oFdy5A5HqsNc4s2kko" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=EDU6eY-3HCk3EiZAwoqyJ79Oy1GfPL3DBf0dT1E3o6cnX4sBFmaLtcpAIjvq3y_MILzntWt3rA0vS0S1vJ6P3F0_l6R1D9p7P-zAQx4fVZ5-yPurlIRIjIc6OSkq2PbFNVi1VJWx0XXHb1YLp5C6Z5vH-Sloq5PJY1mZIPasvYbRrEhJiX1wkFcJqBOMf1shwnunUJy61bW-Xht5uKT5nwKXU6P2a-yL3qYOjEI4DNyrFp7J6fiEyhG74bB1IKDg-lBIv8IT_qrjKEmFFdAyZXqjXmfFUCE2T6DOsxllKvfHLK4Lt61o6uiz6fyylSCuHJrwgC1GEFvyqghTdfsSCmbY45XvqD0KCxzh8T2EuIaX1E2FB0a-o1n0TQxHFZ91D2gF1VZhlN2jVd3zMbLx8hSgkjGXn1Co-LH2YCZj0ot4lc1iNBm1N0jSwgdDi1H19JIWyrU_qRj-ZgejJJe7JKbGChuNyoFsacdfaDiahGTdq1tUMXHc1jRLv5xxJ87FTHCJP_uttnMBISY80PbB2EHxY93Al3KIwoundv35tnN8_-h2s6GEJLrFP7h5VsrNPDeta5hZI9RR5G6xxecXTwtEaTovVhkQz_n5wGK6u9IFCG3ng6kmawslE28THGN2jWj8HvNDdCEVClpQPJLtKr6v6oFdy5A5HqsNc4s2kko" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8365">
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
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBlizHnisyVtj-EsdhEBXdXcDQAYjmwmK1U_Mx3YATY9K8WmoLacxnkEUM3mUJOS7Jx6nPPrXV2gSpPxeVC_4x1MyEwNH-gokoVDrL1PHdQUiQzo4DSK5kx3RNxOH8P6zFwnZCBIt76IW0x-psGpbVAzPrfzwqMnE8U3XZjcZQ9Ir_IlpwN8Iri31UtaKzXjbLIRwsIRwAXCWMDGpllrGTotQ6XH7Asqgw_Qvvf4S8GBlqYlACh5h6FkomFHCBp00Ou78tp-24F9dmt4p8UAExNpuHnFyqrSIWYIqqsGpMcwOdu4t1UkZcS-yLAT9TXH0PMVZGsd4dB0QYvcQNbpe0lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBlizHnisyVtj-EsdhEBXdXcDQAYjmwmK1U_Mx3YATY9K8WmoLacxnkEUM3mUJOS7Jx6nPPrXV2gSpPxeVC_4x1MyEwNH-gokoVDrL1PHdQUiQzo4DSK5kx3RNxOH8P6zFwnZCBIt76IW0x-psGpbVAzPrfzwqMnE8U3XZjcZQ9Ir_IlpwN8Iri31UtaKzXjbLIRwsIRwAXCWMDGpllrGTotQ6XH7Asqgw_Qvvf4S8GBlqYlACh5h6FkomFHCBp00Ou78tp-24F9dmt4p8UAExNpuHnFyqrSIWYIqqsGpMcwOdu4t1UkZcS-yLAT9TXH0PMVZGsd4dB0QYvcQNbpe0lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8363">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ji-aLlQtQz6eg3ojzVkuaHG1y-ewm74ngR0DXw1QCsO-FzcOx2wIdcGHlGITb5paAI8eQQq3SruYQ2lgfvgwV91Uh_zcjyMH7xUXeRjXXYw1Ei54_IEEmGFCCC7meP3Og_03yDYkIcpGeRzPaXo81apD5tqQxu6cmsYTxyqcfikHDNwVLadNOgzSku7djrH4BhcPxWM9ZC5jXQWqA9CbZ_PR-v6-mgdyVIkFIK9Z_6cPHpzVYLYrhHdRz_all-3EzQtpANBbB7WdpkoMFvu1mK-D8WCj2gpg7Nc4XIkAweqHJzkRhk4YsayAsyRiAJUJNI4RNI_AXjTkGXMbvTWBBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8358">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8357">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/IranProxyV2/8357" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8354">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pagSTR9TnZHfuWWaWrcK6FvIu2DS6_A2DJmssq_rSoxyVGRoW6J0wi9KCNsBJ6soJTCl_dKWfqnTir3STQsmSLVDreS-meT598PPm4Pyl8HDktYM49PmV9l66zy7bTXn8zwl1VgOywO_Yq4s7md92HkeJxbY287Ffxwzq5BvcTxS1QhIjvCKSDjEJj-kVFXX9bl_pq9VnYYuY-hotbGz39s-SWcH1F6oi3GK03t_jXWYJpkOJKwRTGPe2NpN4k-6f2irp0VM-zRhxmlKpKi3a-runBzr83wD4NSsHNuNea4OMhwjFn7MRSGN-KgPy4VTYZ4aznGjf8j-16pt1OKlnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8350">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8346">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">slipnet-enc://AQskvHpoSr0z/luIGDACbhKreNDTKyhhMA3DYlYmmHhr6T/THqqypSEZIR2ROKHLR6XP/iribGUsJGd/wwwh1ZLFTrR6kKY78tIX6XmbL6eLIwT2+Az997HmcivFgJpEtgDTqAQVkonbDemLykPWC/L86oUN+Bfoqg7S+FVTAWD2NIQa/11CwodDdSWh8KTKoVIV80wPNJXSS2qi4THuGu5jEoTVOenuOImriz65wsm4ASSgo750zT/dZvGGj0ynpjQVa+y9hxbby3u0Lu0qbp27pnXaUHzmoEh3jQVIQi5OAcX4VvcUetwhOtV6DXHU+vsZPWDcQUOpd/7/0wZW+EUN24SqPt9fGMIsFsKpHXPoJpUs2BB1PkC8TZymVkqwmjeO0Cey8oj1g+DCiR5r1jtWijUAv4yehzdzbDuU++T1J6Sj0nP7ADo9wGFllaneHyrpoGHXRSCiQtztJKw7qwEWTLBo0jLT1Lt76HyJ0xGn6lPM+evyYA4Pd3E1bwcaa9kh6kJ0BTIjfT2UBa+zd2L+UejzTjqrKrYW6whN792AmDFdS9CHY7Ho7F2PZf+wQx4E0BjdJ7MFpNfblxmmgD2SsxRqH/7IpWpb+mr48+kqlveInlB9RKTxdzdfufoY5s82opLQBhAsuyXEhcqMYgRLIUsUXiILutNRoc/vBq41mI4B02bmpcZR6JmcYTcU1pjWop1QQPNvo89WaaJWZxYBCjO+TtbhLFsN9VTXdVe6fMSNo524sRPA3Kk04YuQk3cugUbywKo/BUXCnss9G7ffIJgmxd6UK5GIunGf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/8346" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8345">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/IranProxyV2/8345" target="_blank">📅 19:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8344">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن   ایدی ادمین…</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/IranProxyV2/8344" target="_blank">📅 19:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8343">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">محمدرضا عارف از سوی مسعود پزشکیان به‌عنوان رییس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/IranProxyV2/8343" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8342">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن
ایدی ادمین
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8342" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8341">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کانفیگ های پروکسیو یه تست بزنید مستقیم وصل بشید بدونه هیچ پروکسی بیایید تل ببنید بالا میاره و اینکه احتمالا ۲.۳ روز دیگ کانفیگ هاتون کلا عوض کنیم  یه تست بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/IranProxyV2/8341" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8339">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ggHmCpFEyAMUah4EdTGxtoFmPPWOiG3nbi6bWZ7uwH4i_bJABgBHKtEwE3b_KWfPa9Qmx601Y5U9-1xKoI-q8iL81v_h1s61r7iPP6Nh6ORX-EVeKr3mQugUH53stMP-LPBwlBy3dFCSjmuJa670bprgF6sC1hGxdVvnAGfDFzEvSs5cvokmB0r5lR3jqGfCRe7BEZ_qLImcy6461WyfGN1C1Dali4yHIvZY-AvfIiFbiO2BSDt-041EhcQvxQ3BVzZUcUt-zOqIs0kpUtk4etgtxTsnAhNKGe8_E_IjG852leawUYhJYWrGKAhiuLeXhE3a2zZAAr4tf4ooTvZpTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خدایا شکرت؛ دیروز اپل به صورت رسمی اولین نمایندگی خودشو در افغانستان افتتاح کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/IranProxyV2/8339" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8338">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">معاون ارتباطات شرکت مخابرات ایران: اینترنت بین‌الملل نباید با همان قیمت اینترنت ملی عرضه شود!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/IranProxyV2/8338" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8337">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8337" target="_blank">📅 13:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8336">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/IranProxyV2/8336" target="_blank">📅 11:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8334">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rA5UF3zetl8frzcoknETX55ppwU8RyR9sK2fZ91Nxq2nhvgtVq2AeF2ExFX1mD3hyjjbL2zs0DAHlJVso5faI6z59QaAdkmUr4X3Mot4qWYXawTEHoDg82WwCbv97TQwpqM4sq34qGL5NjMkM1lO_2JJfwQXOu2Ac4MDHAnUHFEqXwn2Y8c2vctjmOZARhKl745EU4Yi_2Xn3QcoS9ViOOLuDe9QUHFfNWAV8CfEzObuklIyLD86Q--2p-Vq5C1wzdVat8UuWkKeLZzAuur41TxJe59oAC3GRkyzYu872XWi37jPYYq0li-YZSi6-yXmomIKypaXGNYH5whhRfMQQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZ8PRx9y_yxX4JwgRwchqVt9704YKwVLVe5uy0aW8DEEWwVMbNW5eyGfqezw-WOp3BjbMk6Wc6GVEcADURJF8G7CtwOcUGv9Pl0I7hoc1NwK-gqBy5-KLecvYsrgzWwiRyn3FaQlUOiNexF68Gtht1MHpcm2iJz_37Abn8kygJM8DmWy9gD6NgSShpivn9J7MgUrI7Rgj-KPDuLfN99sOhfZwOdMERmBBZyu4Cr4cIQd29jan_DpGtf5Rfg70W_KY5z4kFdnmTVomnG0s0P6-KKcGnd0CPMEjS2_pLiRlI9C1FS8o-3ERRo1Kq3v2hZdnVVDuY1goOA2auCZEkcz9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صنف کفاشان و اغذیه فروشان هم شامل دریافت اینترنت پرو شدن.
به‌زودی کل مردم ایران شامل اینترنت پرو میشن که دقیقا همون اینترنت قبل از جنگه فقط به جای گیگی ۵ هزار تومن باید گیگی ۴۰ هزار تومن پول بدید.
و فقط اونایی که توانشو دارن میتونن از این کالای لوکس بهره‌مند بشن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/8334" target="_blank">📅 11:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8333">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/IranProxyV2/8333" target="_blank">📅 10:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8332">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://45cd71df-7b23-4568-8677-fdc4a0daa76e@protectnet.cloudinohost.com:443?security=tls&sni=protectnet.cloudinohost.com&alpn=h2,http/1.1&fp=chrome&type=ws&path=/&host=protectnet.cloudinohost.com&encryption=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/IranProxyV2/8332" target="_blank">📅 03:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8331">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✈️
Slipnet
slipnet-enc://AcwwsvYl4r7DajFRU6wa12enHS94jGWcw63dYwNxwSzZZDO03mNtFG6vROd+UO8opWIgDZkjjnUHlVvSaj/HvKW+p2HLBc4ETWvUWsMZpCwiUmAeEORd+qfA089iU7PBEHuvMqTIeRqwCA6OyylmfHRyIlB+dS4avIQQAJLxeW6G0ZMnp8HZ4VPpuiN2Vs3U7StRqxSwEP7f8wUXQy1DHgcCE9WD74CKd5RxaHADsaaT4Qj56xDB+DTB8l41JtvrbtjUVSNCS349vS8XyPhXi12t/YaAupzBKzSkPCXi8UjM8Ft2AyUuvLKTPgSMjJgI+vBT+16sztR9Q5n88GbrLNNWKD31CXYgjS4YNk8tLooUjYBgOKWmoBPVWCHej1RPyjs3lg64enMfTyX+WKjZ/fxrqH/8uGQZGj7qLjcGhGaohjHujN+ODCfxxAlK+6Y6eQFfld7UtXfyz9cTmhkk7mebn5exSrIv9o1auX6VVjUQ8xLMvhf6wwsD6vwQsblA6QeIvDoD8NUOfeKZFKrraoPjEdJexjOxcn9gbWSEM/QeqZB/lQ4LnfH6zHtP8PmH63PRZJTZUv6VlAovbrtWUp0ziB5fgISZTC4akBfBPTO32WXUTj+Wo1sSSeCH1rfVQAYoMqoQusLWWSHLm5Llfz5jW8qGwROFKxCq6HYzt4gLRZixvL44Dluxo+oyG14jHwsAmPVh05xydwjCI2XcpiJgX5De91xk+x39xMt7AwApPsraUbzuBscA/TU90Ehahp5NbRa0nr1Z44yGL0dC78sWZrPT5XtXbIE+Ydpd5qq3F1Y=
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/IranProxyV2/8331" target="_blank">📅 03:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8330">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
اطلاعیه سرویس سرور های تلگرام
⚠️
به دلیل شرایط پیش امده و قطع سرویس های تلگرام توسط دیتاسنتر خارج سه راه برای برطرف کردن مشکلتون وجود داره، دقت داشته باشین که این مشکل فقط رو سرویس های تلگرام هست و سرویس های تانل تو ربات هیچگونه مشکلی ندارند.
1⃣
- روش اول…</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/IranProxyV2/8330" target="_blank">📅 03:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8329">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/IranProxyV2/8329" target="_blank">📅 23:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8328">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/IranProxyV2/8328" target="_blank">📅 23:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8327">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سوال اینجاس اینا از بازی ها هم میترسن باز نمیکنن حداقل مردم حوصلشون سر نره
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/IranProxyV2/8327" target="_blank">📅 23:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8326">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✈️
علی قلهکی، خبرنگار:
🔻
تا امروز بیش از ۴۹۰ هزار سیمکارت پرو فعال شده است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/IranProxyV2/8326" target="_blank">📅 22:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8325">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">💎
𝗩𝟮𝗿𝗮𝘆𝗡𝗚 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻 or MahsaNG ( Psiphon)
vless://799f939b-964b-4416-84ac-18a6ace7fe70@camp.nahidapp.com:443?path=%2FIF_VPN_Bot&security=tls&encryption=none&insecure=0&host=camp.nahidapp.com&type=ws&allowInsecure=0&sni=camp.nahidapp.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8325" target="_blank">📅 21:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8322">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEZ1xbVNiZkoMcrHZM4DDm8N7xYJfr3imwHxt1CjKovfaK5xAY-fQb8zyf5-AZ7czoCI7MAn-tLvkjfT9yzZXi6KkBQh37CpyNlFzBWsGOGtN4IRqz4hUFcoPU6DXjESI4vfKcKp10U6ZVykVDWAfAyGY8vhKCfjrRd5ScNwTUvKNJkzYTtP45CQCL54l9rpzEcwOo4yfl-k1M6zzDsiNqTr3QXWDuGzP6enJUa2vtpUq-YxAlhT-Q17TOTPzXkqlk3P2HtH_I7tg6nNuEDr3j06Ub_jdAb07ZtPwOsymQB9-yOJpMYTeOMUZsry4jO27Rm-nL70ZhOyTs853d_wGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
وعده پزشکیان بالاخره درباره اینترنت :
◀️
ارتباطات و اینترنت به بخش جدانشدنی زندگی مردم تبدیل شده
‼️
به آقای عارف ماموریت دادم با لحاظ حساسیت‌های حکمرانی، نظر رهبری و وعده‌ای که به مردم داده بودم، در قالب ساختاری چابک موجبات خدمت‌رسانی بهتر دولت و تحقق انتظارات عمومی رو فراهم کنه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/IranProxyV2/8322" target="_blank">📅 21:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8321">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/IranProxyV2/8321" target="_blank">📅 20:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8320">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzDczmcxPN7ArQN5EQLs25Eg5_Edzhc0oDo7x-pWfJaUZoNlRoqiz-KLIwCONt64HzLjDwtwD9qbpZelQceGgt3LN5dtfp4nzylRmY0JrIiIDw3H-d1DEVkECKwj224Adn0K1nNeeUIuL7fkyJ6glInnPjSIqgVtyNK1OzVveVcq0bTxjyuCo4N1IgHkcL6gn03tn72OPBt0dLAEwW2hbU6FmbWwmTCCckOQ0mFUN8-3SsousGcI35PqOpTDFaf6KknAV--QPdyv-l_eFcM2Tr5EndON0sEexf6JDR5kUsUeYKToNKoL-2cRKqOCQWDPSZDYGcmBFiwXOax8lmClJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت اینترنت پرو
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/IranProxyV2/8320" target="_blank">📅 20:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8319">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8319" target="_blank">📅 18:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8318">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de826422e1.mp4?token=EsJADr6yK2mM4jAkkNA-y-XVm3J52CNdIw47F74phjlhoZInFa5hgvFTrLKWze4bfrWyYruzHOeJMWhVKRGYFx5zwwSs-tsjiA4WUPmiXubkjLgsvuOyP5xJlc3l9ONUGvK-XhBU7cU-AgVMXmL68vSEvp7qrfwyhRW3P6x8rcPmHWe9UXCYpzHXf6PDo17JqCGh3IJIm4JWlJ8XFHVwiIKIPkcnUuUxT5vk34DGmUOu0fuNYFjRKmGR8v4lUmq8Zpcseg_u-UjBam1z-Df01PmfGuqlT8m-iUIV0L5Z_49fHGspDtEshcLXQ336W5DPCrChErqqWu1yUel2XiDzOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de826422e1.mp4?token=EsJADr6yK2mM4jAkkNA-y-XVm3J52CNdIw47F74phjlhoZInFa5hgvFTrLKWze4bfrWyYruzHOeJMWhVKRGYFx5zwwSs-tsjiA4WUPmiXubkjLgsvuOyP5xJlc3l9ONUGvK-XhBU7cU-AgVMXmL68vSEvp7qrfwyhRW3P6x8rcPmHWe9UXCYpzHXf6PDo17JqCGh3IJIm4JWlJ8XFHVwiIKIPkcnUuUxT5vk34DGmUOu0fuNYFjRKmGR8v4lUmq8Zpcseg_u-UjBam1z-Df01PmfGuqlT8m-iUIV0L5Z_49fHGspDtEshcLXQ336W5DPCrChErqqWu1yUel2XiDzOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شهبازی مجری صداوسیما خطاب به مردم ایران:
اگه اینترنت 5G که افغانستان داره و مسترکارت که سوریه داره اینقد براتون مهمه؛ خب برین همون افغانستان و سوریه زندگی کنین!
﻿
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/IranProxyV2/8318" target="_blank">📅 16:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8317">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ایران اینترنت ندارد، روز هفتاد و چهارم …
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/IranProxyV2/8317" target="_blank">📅 13:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8316">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⭕️
اطلاعیه:
وزیر ارتباطات گفت در تلاش برای برقراری اینترنت بین‌الملل در اسرع وقت هستیم.
همچنین طی پیگیری‌ از ISP اعلام کردند که اینترنت بین المللی شبکه خانگی متصل شده است اما هنوز زمان مشخصی در مورد اتصال دیتاسنترها به اینترنت بین المللی وجود ندارد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/IranProxyV2/8316" target="_blank">📅 12:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8315">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde1d5a77d.mp4?token=mbs-bHORWxPJC83SqbH1Q-U_tmEXYRBJelTHO2_IBZzqqScLJjjepOfWYypSjKWexmKCszCDExLUzv2DUPwVFfvkuf-3kOn2b3Blm7PhIE3RJNCHcJYdC6oU75f0HZ957j8UXFtTi_M9CHeIMzWgGv4OCkF_zMaAIkQpDemM0dV5kV9CW2FYMUQePhcOkn53f5undkcj7Qele-gIVTmUppsWhDSQM8tg7PjgV_6HA0c1lYtP0ZLJw0StuDNwfqubwhGwiRko0x3ivG-qFQoY2emw-N28asbToMbCl4OY7hzCcqvwR0kZ5gjHo_MyEt7iOjoNB6TeZ6nTJeDUhI-I-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde1d5a77d.mp4?token=mbs-bHORWxPJC83SqbH1Q-U_tmEXYRBJelTHO2_IBZzqqScLJjjepOfWYypSjKWexmKCszCDExLUzv2DUPwVFfvkuf-3kOn2b3Blm7PhIE3RJNCHcJYdC6oU75f0HZ957j8UXFtTi_M9CHeIMzWgGv4OCkF_zMaAIkQpDemM0dV5kV9CW2FYMUQePhcOkn53f5undkcj7Qele-gIVTmUppsWhDSQM8tg7PjgV_6HA0c1lYtP0ZLJw0StuDNwfqubwhGwiRko0x3ivG-qFQoY2emw-N28asbToMbCl4OY7hzCcqvwR0kZ5gjHo_MyEt7iOjoNB6TeZ6nTJeDUhI-I-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهاجرانی:
اینترنت حق مردم است؛ عصبانیت مردم کاملا درست است/ عامل این عصبانیت دشمنانی هستند که باعث می‌شوند فضای امنیتی ما مخدوش شود
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/IranProxyV2/8315" target="_blank">📅 11:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8314">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اژه‌ای: اینترنت پرو و سفید مثل پتک در ذهن مردم شده است
🔹
رئیس قوه قضاییه در جلسه با وزیر ارتباطات: مسئله‌ اینترنت پرو و سفید مثل پتک در ذهن مردم شده و باید با موارد خلاف قانون در این موضوع برخورد شود.
🔹
در این جلسه دادستان کل کشور و وزیر ارتباطات به رئیس قوه‌قضائیه گفتند با بررسی‌های صورت‌گرفته، احراز تخلف در قضیهٔ موسوم به «خط‌های سفید و اینترنت‌پرو»، قطعی و حتمی است./جماران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/IranProxyV2/8314" target="_blank">📅 11:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8313">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">vless://8b7dbddf-fe0a-4405-b8e9-bfac4d9439ef@185.143.233.235:8080?path=%2F&security=none&encryption=none&host=MHI.ARTARONA.IR&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/IranProxyV2/8313" target="_blank">📅 11:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8312">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">V2ray + Psiphon:
vless://3728fc28-910c-4a9c-888c-c08c3e2f4a06@snapp.ir:2052?encryption=none&type=ws&path=%2Freq2&host=snapp1.gptpersian.ir#musiclovers85
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8312" target="_blank">📅 10:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8311">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">احتمالا اکه پروکسیا درست نشه با کانفیگ های ثابت جاشو براتون عوض کنیم اطلاع میدیم خدمتتون بابت صبوریتون متشکریم</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/IranProxyV2/8311" target="_blank">📅 00:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8310">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حجم سفارشات ربات بسیار بالاست موجودیش تموم شده بود مجدد شارژ شد، صبور باشین، دارم یکی یکی رسیدارو صحت سنجی و تایید میکنم با تشکر
❤️
💲
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/IranProxyV2/8310" target="_blank">📅 23:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8309">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJPYSLpa_wP4o3Qsb9GS5L83I7DKjXo4QellumLdHJSf4ZaWWEhdn4fhtjNY-yAFJnv6Uiz4Qm2vxqmEo5sAPgANTCmOExfeDNTvyf9yYmuAcHCjFjq2BliNlch6zZ_vxZOSnMKKs4uNxsh7F6Xu2dI9aCCNWe0esXweGB99gD-wjhOgnF5V1NF2XkBaIpIJ87_WfeEzxscyJDakpr7Hx6Qmv5v05b29CcIcqn_mr_LNVGB1zYkrmMzaHnbHju-P_oV66Y43CqExFPdb7v29kHcvN8SDwJOP62HVztaJV_mc2ZgFwE2J_c-xAJGWhiNmzUZV4kK9HkkpC5Bq1ZjRYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایزه چالش دیشب، برد 2-0 بارسا درست پیش بینی کرده بود
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/IranProxyV2/8309" target="_blank">📅 23:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8308">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
معاون علمی پزشکیان:
حتی در شرایط جنگی هم بستن اینترنت راهکار نیست، زیرا وقتی کامل بسته بود هم ترورها ادامه داشت.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/IranProxyV2/8308" target="_blank">📅 21:00 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8306">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⚠️
ترامپ به فاکس نیوز:
‼️
در حال بررسی از سرگیری عملیات «پروژه آزادی» هستم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/IranProxyV2/8306" target="_blank">📅 18:30 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
