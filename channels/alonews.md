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
<img src="https://cdn4.telesco.pe/file/AaR_R3pyhxNfD3ghknxpT2U8LFFWby_SQ1f2GX3_xxWjldS57E8pUpaGSzg8aGnihA1B1PWm890nvrThqB2ZFZnCpib3KJuqRuYqWsiFU4D-fCCl2qUdp2f-dEBMBUBsaoCWxoEP_R38Cq6YI4rN-ewFx0g01ShEgOCMSiZ2x8PG8EUIhngLt0bsyugPkaSJx6LtYEE-RdPtowJDKZrdWsbf_JeGsdzGbBEUQB2_2QuMCiY4Xc4duyQgbRZfBqvlj3HtUA1wAJKpPZD9cfhBIbUY3Gh8HxfAn_P-VmyIPHjZ5fp-H4wId6AFlydG_yfwmxJnJLbdza2m971LSESZCQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 921K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 18:01:13</div>
<hr>

<div class="tg-post" id="msg-123313">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ادعای اکسیوس: به گفته مقامات، آمریکا و ایران به توافق رسیده‌اند اما تأیید نهایی ترامپ باقی مانده
🔴
مقامات آمریکایی گفتند که مفاد توافق تا روز سه‌شنبه تقریباً توافق شده بود، اما هر دو طرف نیازمند دریافت تأییدیه از مقامات عالیه خود خود بودند
🔴
مذاکره‌کنندگان…</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/alonews/123313" target="_blank">📅 18:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123312">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ادعای اکسیوس: به گفته مقامات، آمریکا و ایران به توافق رسیده‌اند اما تأیید نهایی ترامپ باقی مانده
🔴
مقامات آمریکایی گفتند که مفاد توافق تا روز سه‌شنبه تقریباً توافق شده بود، اما هر دو طرف نیازمند دریافت تأییدیه از مقامات عالیه خود خود بودند
🔴
مذاکره‌کنندگان آمریکایی جزییات توافق نهایی را به ترامپ گزارش دادند، اما او فوراً آن را تأیید نکرد.
🔴
«رئیس‌جمهور به میانجی‌گران اعلام کرد که چند روز برای فکر کردن در این مورد فرصت می‌خواهد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/alonews/123312" target="_blank">📅 17:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123311">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10b0b9d0c8.mp4?token=Kdd63oqkz4cS08LppE_g0d6D_ma57eMm6re_AoofqWgCrDldLlErxFuIVYLbyX7Y563clvjNO4TQSXTo04tLk5FxKPeaq5BHgcgqAgNu8LdWicg5hXRUiEkw9oHoUoaK0MjXqABBUzEw2jnFU_U1wUSROaj6wsvPHiDTjqTdq9ig-_1DGQrSU5DStKmyEijZsMPVLu0TciJf7Iv_iuVIFAz97OsiEXlg2R4pUqw3mGOLMitghtDme4dqm8G8oQVhMVdce_Y9n5bKEifro79B8p9sfmiaCUZVOMaasj8inCf-hf2XGpHJxaFaVa7Ns2SravwzBX1O83vDP6fL_b0fEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10b0b9d0c8.mp4?token=Kdd63oqkz4cS08LppE_g0d6D_ma57eMm6re_AoofqWgCrDldLlErxFuIVYLbyX7Y563clvjNO4TQSXTo04tLk5FxKPeaq5BHgcgqAgNu8LdWicg5hXRUiEkw9oHoUoaK0MjXqABBUzEw2jnFU_U1wUSROaj6wsvPHiDTjqTdq9ig-_1DGQrSU5DStKmyEijZsMPVLu0TciJf7Iv_iuVIFAz97OsiEXlg2R4pUqw3mGOLMitghtDme4dqm8G8oQVhMVdce_Y9n5bKEifro79B8p9sfmiaCUZVOMaasj8inCf-hf2XGpHJxaFaVa7Ns2SravwzBX1O83vDP6fL_b0fEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو:
اسرائیل کنترل ۶۰٪ از نوار غزه را در دست دارد، دستور من حرکت به سمت ۷۰٪ است. با این شروع خواهیم کرد.
ما در فرایندی هستیم که می‌توانیم قدرت خود را در جهات مختلف به کار بگیریم.
ما همچنان باید بر حزب‌الله فشار وارد کنیم؛ در حال حاضر با حماس درگیر هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/123311" target="_blank">📅 17:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123310">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgiDqfdNRJduZota8llWLig0v-OmZfHM1ZaBzdPpEm4IJI5RJYkTDHnc7uDEEtvhMZcJsBR5uTkHfWg03h-C7plNdcd0Zh_ZmambP8dqpljbVn9AHWhtEiiBYn8R9rLyJJtxJdCd1isLUGYUGoZbUT6DCdmHy3a720yTaKIzA7OJojG19zC8COEnTw-sMqy2ymUVMmmTQtr_1oOU6AFTDovOr1Y7hES8yn21zqOlHqlLs2nzavEJly23mTBrARMtALZ6h5fPZonU_AP_pf3u9EIst1SEZB5MPrZWyTS0c8_WMI_lvWL0GnDlw7swPigFlXlHGMyLMk8jD5YWpbaBtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
ماجرای نماز خواندن کریستیانو رونالدو
سعد السبیعی، مدیر پیشین اداره حقوقی باشگاه النصر:
🔴
پیش از آخرین بازی مقابل ضمک، دون (رونالدو) با بازیکنان نماز خواند و سعی کرد در رکوع و سجود از آن‌ها تقلید کند.
@AloSport</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/123310" target="_blank">📅 17:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123309">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
روسیه:
ترامپ با انتقال اورانیوم غنی‌شده ایران به مسکو موافقت نکرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/123309" target="_blank">📅 17:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123305">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac373359e1.mp4?token=ax2kKjLBG8JMFfPdf90jzXUXqLW2yHRciO1uIt8QAoqeMFFt5fgh9ZR-d527RPYTxxAdmorfk8m2eTfqlVL_y40Xly-ef8ZIE7oLRk0jVBFj7VryMbjaXxnyyJwirOaeT8U6dUtpLJ9cYSmsPc18eVB2u6M1FKZWQyLZKYV9amwjxfNWqWJzYQxZNPHRUQ9RgYuoet3zADicOLwR6nUA7-vzE_0DMdL9s9ztQ4P3PKAoLY6UbFTRYUe0rv-lSVmGQtgTDhSJE1ZkFbtP6A17oV1z1om0K4xYS9xVVU-J11sN3RZeYVxC17zVqV8enrX-z_29suXBFI9XUjhEz7KoOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac373359e1.mp4?token=ax2kKjLBG8JMFfPdf90jzXUXqLW2yHRciO1uIt8QAoqeMFFt5fgh9ZR-d527RPYTxxAdmorfk8m2eTfqlVL_y40Xly-ef8ZIE7oLRk0jVBFj7VryMbjaXxnyyJwirOaeT8U6dUtpLJ9cYSmsPc18eVB2u6M1FKZWQyLZKYV9amwjxfNWqWJzYQxZNPHRUQ9RgYuoet3zADicOLwR6nUA7-vzE_0DMdL9s9ztQ4P3PKAoLY6UbFTRYUe0rv-lSVmGQtgTDhSJE1ZkFbtP6A17oV1z1om0K4xYS9xVVU-J11sN3RZeYVxC17zVqV8enrX-z_29suXBFI9XUjhEz7KoOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت وخیم لبنان بعد بمباران امروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/123305" target="_blank">📅 17:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123304">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده درباره محاصره:
نیروهای آمریکایی اکنون ۱۱۱ کشتی تجاری را برای اطمینان از رعایت قوانین هدایت کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/123304" target="_blank">📅 17:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123303">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74fef6c239.mp4?token=l4f8v_UAAV_8ST1jyXwHUjdfNQyeg9qmc6fBcN8VaVixwrK3FLGqp0BthY2oL4KfqtCXehN2y8J8UG0r50CIZ4s0rQqgglsxuP5h4WViLrEusX-rNTybqqrpBat5pfOcAkSY1grXkfKcgsMsKLU4ngjnwwt6969XHM4CQiwS4wHfLYZOl7azNkIH2LPCvL9LqsTw8mfI_KVj06dMfdSpYGQppCj-IfxMu1v239dzGCjbLTnpOnbzqEc1ky9zKrjcTTE3xUoNkw9sdzX0WjMiDFbI40FH2hAIV2MF2PXDTjnGFHFQa8Hs50oqH3ogY3aSYkypWNbBT2i9GYETmJtg5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74fef6c239.mp4?token=l4f8v_UAAV_8ST1jyXwHUjdfNQyeg9qmc6fBcN8VaVixwrK3FLGqp0BthY2oL4KfqtCXehN2y8J8UG0r50CIZ4s0rQqgglsxuP5h4WViLrEusX-rNTybqqrpBat5pfOcAkSY1grXkfKcgsMsKLU4ngjnwwt6969XHM4CQiwS4wHfLYZOl7azNkIH2LPCvL9LqsTw8mfI_KVj06dMfdSpYGQppCj-IfxMu1v239dzGCjbLTnpOnbzqEc1ky9zKrjcTTE3xUoNkw9sdzX0WjMiDFbI40FH2hAIV2MF2PXDTjnGFHFQa8Hs50oqH3ogY3aSYkypWNbBT2i9GYETmJtg5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: الان ما تو بیروت حمله کردیم، دیروز در صور هم حمله کردیم
- نیروهای ما از رود لیتانی عبور کردن،ما اونا رو می‌زنیم و خیلی شدیدتر هم خواهیم زد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/123303" target="_blank">📅 16:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123301">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCbHOppYD_sCg2-5ZU9zWzpXjoSREezHaj_T4wsLtOi4SP3tdrXXxHkn2BRNwiWnHSdx28s5AycpkUb1hVfrSIcOrnpgWfv9TYX9BXe8klVXbOHBkFIpe9LOHv5txqSdJi-YACZF9_m9uA-gssbVYFxLFsWmh_DK5fP9HIbHnnWH0ndt38rMdizSWK1fcplKSnysrpzuvnspU7jGoNPLthTW2PN1nyKO7n9H8E-EkNgTAlQl3GGe5tcyVBtP2C-Gya8XT8sTTdTQU7TvvpeqJgD0GXcukzd1HlzLBnTT81T5dwt0LF5gygsM73TZ_6JmRU3UkWAqxoV4SJmvg_wl-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دولت ترامپ و وزارت خزانه‌داری ایالات متحده در حال طراحی اسکناس ۲۵۰ دلاری با تصویر رئیس‌جمهور ترامپ هستند
🔴
اگر این اسکناس منتشر شود، رئیس‌جمهور ترامپ اولین فرد زنده‌ای خواهد بود که از سال ۱۸۶۶ روی پول ایالات متحده ظاهر می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/alonews/123301" target="_blank">📅 16:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123300">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
دولت عراق حملات ایران به کویت را بی‌شرمانه خواند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/123300" target="_blank">📅 16:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123299">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVCrsn_5ziYDwKYGqyZqjD3nIQe0UAcQOZqfZ_gbtQuPPlxbPCGCD4yTsHxiy6DqYKtFpBXV3oWqIWCDE-_Jgreho-V7BHIF9q-2XV8kYuamvXp0EP_9KIwByVyT5OBMOrOdRBTOrleHtyQtqr-6QiggW3Xnvr2THW8yUua_62JNWQfGMEyhx57HpmCtHoxY8_mZ1zkABi36dWeydPY8WZyByAveFT8ESISxE_2dzKL2cX7MXHksJAZjQpolUfiQ7m9y1opNDvf1qHarWX-WoXR7qfubCZaiy58WCC3oaPzfa8wCQH1AzEs-vqFDC82CfuYzXIvVdlGHhiXnhxpUNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوش چشم، کارشناس ارشد صدا و سیما: ایندفعه دیگه جنگی نمیشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/123299" target="_blank">📅 16:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123298">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
هواشناسی: تا چند روز آینده خیلی گرم میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/123298" target="_blank">📅 16:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123297">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KY7u-6QngzIiXAGK_1ynGEfINa1Wem_vQ2TT74-gdbmz8FeElK8BwsQvoxGmVMks5aZ9ZiM0AGFtjxK3skGSQ4I5Qa-qHmXkB4UC3aed9z1R2WUhLg9SSarSXI46LCgsgIolnbRjhIL1y9MqFhdSI9yxMohpk8TjHc2PzSMcF158czTU9ROGoUoNTGFvZyOMFVCUCpnAhkXiKHo93WFPJdwKsJXgf-6jweLmYHgTLf0tbf4u72nVdZFFSEuaDG09I63v8oFCuWtk-GW0oadIK-K9kW15QWj0DUXoL8e3cSmUT1OuDW_4q3-veFFxt1da14UQ11pJiuthrWayWwqF8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابوالفضل ابوترابی، نماینده مجلس: آمریکا بعد از جام جهانی و انتخابات کنگره دوباره حمله می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/123297" target="_blank">📅 16:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123296">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFIyavwqNFTh4OGbInC_ULPPdLLY89RbbR5VTgr9fmmPDuBu4yHPSbDh1kZkzjGN06ZvCFfbZEk_orVXV77sIJOBep-RF1emwtq0w1ibuiHwTXNGWvuC0201S7IFM5ogL1G7kEOKUvaG2xXnsp2S0doMNFzmlLiEDX5sFlAYGa7vcy1VD1bv0Qja2SiZJPpLgLXkgtArBclUqgHLlb_f4koeC7g5Ua3cvOL8Dbj2c5SvkVO4QcQ-jzPd5293x2hOdAmSykg_te0Iva7LgkHmPpYULDWt2BjhXxTDL-_avtVGm-FiWLd7P8I0H5p-d_mZZWVxOi7erKcHYq_6THfObw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه سنتکام درباره اتفاقات دیشب :
🔴
دیشب ایران یه موشک بالستیک به سمت کویت شلیک کرد که توسط پدافند کویت رهگیری و منهدم شد.
این اقدام، نقض جدی آتش‌بس بود؛ اونم فقط چند ساعت بعد از اینکه نیروهای ایرانی 5 پهپاد انتحاری رو اطراف تنگه هرمز به پرواز درآوردن که تهدید محسوب میشدن.
البته که همه این پهپادا توسط نیروهای آمریکایی ساقط شدن و حتی جلوی پرتاب ششمین پهپاد هم از یه سایت کنترل زمینی تو بندرعباس گرفته شد.
🔴
نیروهای آمریکا و متحداش تو منطقه همچنان آماده‌باش هستن و واسه دفاع از نیروها و منافعشون مقابل «اقدامات تهاجمی و غیرموجه ایران» هوشیار باقی میمونن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/123296" target="_blank">📅 15:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123295">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سه نفتکش با پرچم‌های پالائو و سیرالئون در دریای سیاه هدف حمله پهپادی قرار گرفتند، اما این حادثه تلفات جانی یا آسیب به خدمه در پی نداشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/123295" target="_blank">📅 15:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123294">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزیرخارجه پاکستان جمعه ۸ خرداد به واشنگتن خواهد رفت تا با مارکو روبیو دیدار کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/123294" target="_blank">📅 15:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123293">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgENMPzABHkf79AVALnUst9upWaJjr1hHY1M4m6r5aM9-UhUecqVXdNdZ8kp5V5bTzZ3qr2uPz0mIGwaU50ZQjFD3zLQV6HEaJiWkDsOS0D32ABkTowmVH3jbOEMSCBr2NiLU_2WJZMsOZv5-QOrpuS5OjCJ_FkhwDksDQD4JvykFJwE4hF06HhXo1Zr-_40zcV0gCINd5YB6cl-mX5lIz_Of3-M60cKmymPjYBJOJIZqLVWsUXrgg7RukEoAihCdBHwHZ4J1SEf0kbuYQHG08pHQMl3-cAaH8RoGI-BOxDZoZZCgxRbIF2AvkeKwwGVWEQGuE7dMZG6q5BPrgRJtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سیتنا، پایگاه اختصاصی اخبار اینترنت:   تمرکز ۹۱ درصدی ترافیک اینترنت در تهران است و بازگشت توزیع عادی پهنای باند زمان‌بر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123293" target="_blank">📅 15:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123292">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJps_Gv7b8BBJwlfPQd8K78qFHJLP08JkQlvU4h3a2PZSiKDRUgnNniD0zIpVIZ5EbbI1ZiRjJPdqtd4LXOSrbUkwYswQ35H5Cs3rG4JYHXRdgWUeK7mFsE9EXatKY0V24WF4UMfrridGvHjfVrbi8GkIDaYBCUxrupqd8-JvUxdyUqUm0W7PphJ0zMUoJugl2sPdkADroQA0_m_GA-nFnpr-7PXPVOSPxqyfOnxl9x3jol7qKDQtJPN6LYDLDHgMUoalH4sEXQrO2CwmTudxkFnHM_nlxsz65Z_ALWyLT0BY7USo7r3f-R71cf-W8WtxSl8O9jqMwVvbMyIIIZziw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واشنگتن پست
:
مقامات دولت ترامپ، اداره حکاکی و چاپ را تحت فشار قرار داده‌اند تا یک اسکناس ۲۵۰ دلاری با تصویر رئیس‌جمهور طراحی کند، که این اولین بار در بیش از ۱۵۰ سال گذشته است که تصویر یک فرد زنده روی پول رایج آمریکا چاپ می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/123292" target="_blank">📅 15:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123291">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚀
مصرف بالا؟ حجم‌خوری زیاد؟ اینو ببین
👇
💎
همراه با ساب یعنی مصرف بهینه‌تر و تجربه بهتر
⚡️
🚀
سرعت عالی پایدار برای استفاده روزانه و بلند مدت
😍
😍
@NetAazaadBot @NetAazaadBot
😍
آف فقط برای امشب
😍
❌
گیگی 50T
❌
✅
فقط گیگی 25T
✅
@NetAazaadBot  @NetAazaadBot
🔥
یه…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/alonews/123291" target="_blank">📅 15:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123290">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c3UrtH5XWzZgU2bz3pkt2aTUlLOofxP-cYKqFs93CSqpOCGeG5RoMwsTTU0wCOal8cl2Gz96qkXa0ABRE6QINI2yKcag2lOaidaVipEmVK0oep7hnRae3xN3EefOGDdHShuCwHiQGWBK-4uaNWKReocRkIuKFenoC_ii2q8s5zHBxeOHsIofM09w6EWto3c_UB_2JgKuhFrHBkAc8jFu1CN-_B7EdpUI0e3KmVYN_B-4EkNiFY84q_2luVXm-IGQg8F7HK8nyl8q75D3uzACx0xHnCtY9xQgvkY28F9ui7UVmhTqRWSHoPiSC-duiCoongpF-tc0iMWQJZ6Fc1bjJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مصرف بالا؟ حجم‌خوری زیاد؟ اینو ببین
👇
💎
همراه با ساب
یعنی مصرف بهینه‌تر و تجربه بهتر
⚡️
🚀
سرعت عالی پایدار برای استفاده روزانه و بلند مدت
😍
😍
@NetAazaadBot
@NetAazaadBot
😍
آف فقط برای امشب
😍
❌
گیگی 50T
❌
✅
فقط
گیگی 25T
✅
@NetAazaadBot
@NetAazaadBot
🔥
یه بار امتحان کن، خودت تفاوتشو حس می‌کنی
✅</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/123290" target="_blank">📅 15:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123289">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5ec1c3aa88.mp4?token=dWMDk6y5xG_oUUkPVZWrwxyNTrrFTkiuDgNPZspuNQEB7W8oEoSNX5R3Y5gyHUB5loPiqjuGoKz9K-oFWoCG6dSTH490xdxwexnLCdFqhbDVZsg6w7OBVC_r0ptzOe3l7S8xJz3-mNf5xPQEfnavKLtDLKm4NEpp32CvgbcNZ7jSveucGoNZCcTcTf6F1d-v5Zb64vjrPmvjap2avBO6kqzUWJnI0EiaR05wfhos4hY29npvRN7XKUaf2ep2YUmShU4stofGTjVPBf0-31B9CPeBD0Fe2Q7q_-rVbatFDf1Fbewgtl9FPvrTooA0Eeg-cUKMc3nEagkMKYFdlISG_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5ec1c3aa88.mp4?token=dWMDk6y5xG_oUUkPVZWrwxyNTrrFTkiuDgNPZspuNQEB7W8oEoSNX5R3Y5gyHUB5loPiqjuGoKz9K-oFWoCG6dSTH490xdxwexnLCdFqhbDVZsg6w7OBVC_r0ptzOe3l7S8xJz3-mNf5xPQEfnavKLtDLKm4NEpp32CvgbcNZ7jSveucGoNZCcTcTf6F1d-v5Zb64vjrPmvjap2avBO6kqzUWJnI0EiaR05wfhos4hY29npvRN7XKUaf2ep2YUmShU4stofGTjVPBf0-31B9CPeBD0Fe2Q7q_-rVbatFDf1Fbewgtl9FPvrTooA0Eeg-cUKMc3nEagkMKYFdlISG_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف تازه اینترنت پرو خریده، بعد پسرش بهش خبر میده اینترنتا وصل شده.
واکنش باباهه خداست
😂
😂
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/123289" target="_blank">📅 15:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123288">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
سه ماهه حامیان جمهوری اسلامی با خیال راحت توی خیابون جمع می‌شن؛ نه خبری از حمله‌ست، نه «ناامنی»، نه تروریستی که پیداش بشه.
🔴
اما همین که مردم معترض می‌آن توی خیابون، لباس‌شخصی، چماق‌دار، موتور‌سوار و تروریست ها با هم فعال می‌شن!
🔴
چرا؟ چون این تروریست‌ها از بیرون نیومدن؛ همون بازوی خیابونی رژیم هستن. همون‌هایی که وقتی نوبت مردم می‌رسه، مأموریت‌شون می‌شه ترس، سرکوب و خون‌ریزی و کشتار مردم بیگناه.
🤔
تروریست حکومتیه که برای حفظ خودش، خیابون رو به میدان وحشت تبدیل می‌کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123288" target="_blank">📅 15:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123287">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
تصویری از محل حمله ترور هدفمند
🔴
هدف ترور به نقل از منابع اسرائیلی: علی حصنی،فرمانده یگان موشکی لشکر امام حسین
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123287" target="_blank">📅 15:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123286">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
تسنیم نوشت: برخی مدارس با لغو امتحانات مجازی، نمرات دانش‌آموزان را بر اساس ارزشیابی کیفی ثبت می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123286" target="_blank">📅 15:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123285">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
اکسیوس: در حالی که دولت آمریکا فشار اقتصادی بر کوبا را افزایش می‌دهد، احتمال روبه‌رو شدن با بی‌ثباتی بزرگ در این کشور وجود دارد
🔴
این رویکرد شتاب‌گرایی تدریجی است؛ یعنی فشار افزایش می‌یابد، اما از مداخله مستقیم خودداری می‌شود
🔴
دولت ترامپ معتقد است که بدتر شدن کمبود مواد غذایی، برق و سوخت می‌تواند تظاهرات ضد دولتی در هاوانا را برانگیزد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123285" target="_blank">📅 15:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123283">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
پروازهای رامسر به مشهد و اصفهان پس از ماه ها وقفه برقرار می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/123283" target="_blank">📅 15:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123282">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وزارت خارجه قطر: نخست‌وزیر قطر در تماس با وزیر خارجه ژاپن تأکید کرد که همۀ طرف‌ها باید به میانجی‌گری برای حل بحران [آمریکا و ایران] پاسخ مثبت دهند.
🔴
نخست‌وزیر قطر بر ضرورت حل مسالمت‌آمیز ریشه‌های بحران برای دستیابی به توافقی پایدار تأکید کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/123282" target="_blank">📅 15:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123281">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
تصویری از محل حمله ترور هدفمند
🔴
هدف ترور به نقل از منابع اسرائیلی: علی حصنی،فرمانده یگان موشکی لشکر امام حسین
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123281" target="_blank">📅 15:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123280">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c84bd29044.mp4?token=vTK_AdAcAjRq1yXmtlnynVHUC8M-b3dyyo9UEHfTAJZd5sq6VLrv014R0doS-iWahc3Bxk7STRwxcXb0eQG0NwZvtHrt2ZXYLC1-tdnS1Y6aVPMc9T2brVJZspPUeEBoXDuuXNO_wBvAHjqNJaFiYR2FuxRkbaR2dyy5m2kQHeUxn8j6Shv0PoWGK7kVGpxMCECTe3sjnLQ7ws_RylWqlHvDyI-d4k2Ml161_GAo1bAK4qYC08iAc7ICMkBt2I9u8ToVmLnW5UK1L2d_vCEeC0Iy0EcOpDzKIf5kiz8gjhJ04r12TuKnqij5KFvy0SC-uzH9rvp42hhj-6enza2DEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c84bd29044.mp4?token=vTK_AdAcAjRq1yXmtlnynVHUC8M-b3dyyo9UEHfTAJZd5sq6VLrv014R0doS-iWahc3Bxk7STRwxcXb0eQG0NwZvtHrt2ZXYLC1-tdnS1Y6aVPMc9T2brVJZspPUeEBoXDuuXNO_wBvAHjqNJaFiYR2FuxRkbaR2dyy5m2kQHeUxn8j6Shv0PoWGK7kVGpxMCECTe3sjnLQ7ws_RylWqlHvDyI-d4k2Ml161_GAo1bAK4qYC08iAc7ICMkBt2I9u8ToVmLnW5UK1L2d_vCEeC0Iy0EcOpDzKIf5kiz8gjhJ04r12TuKnqij5KFvy0SC-uzH9rvp42hhj-6enza2DEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نیروهای تروریستی که ایران رو اشغال کردن در 18 و 19 دی در حال شلیک مستقیم به مردم معترض بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123280" target="_blank">📅 15:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123279">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mQZ48e-FAlhQ5E7ecn5wo2yS3oWiU1f5uKwBqlYIxavbnwN0PmUGbGUJfmmoMPEF6hTTMqlhYVrjvRnWxzCnN370v8AWRGzIgXNV_LMkbxRMYc4r8Cpf7cf8YwfvdZ6zVtGm_uciRp4rmM4Mcq4CP3S_VpcVfKbV5Xbw71_F1Skkp01t6W2-S8eNvGNKAPwy1Td0O5la5-HpjLU-QUCrHmpzQ_RSJCYcnhe1ikmy-FqSVEMNmfNJCkpWDG_vvwqFn2DksjCzyENVR2IMC4lZFPs_9N47oAOolTTkVLl5mslei_wp9-Ei8czDE-xNdYT2HDYvngux88lQzWNEyen4Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از محل حمله ترور هدفمند
🔴
هدف ترور به نقل از منابع اسرائیلی:
علی حصنی،فرمانده یگان موشکی لشکر امام حسین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123279" target="_blank">📅 15:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123278">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f656bb517c.mp4?token=KTMlKfXuhURJY9eoaCdr4xmPUdOG60OWf3nhnNUXJWP_wOAAWcLKtnnx87d6DmbQ_OZe7LpFw03PYxiQuARDZn_t7RL7MNgXNZhBCw97h8i1KqpsW4ROS6b8v1f1FZewvR7M7-M8wHin9moJj_e0Eo81bxnlcgKHWagLaNOTPopHe9IIEup7R5n7ko-6QCV-6qguncvhGVdy9evHeDz4jqc8HepJRn0CSlskUxclpA8Upo0gljzD7qrywFCN_Bew6ws8xZIg4wYbpiuSPELIqo1MElhrXkxc-RuD8Dt0Zp2kotyuCe1rJChe3ixMcxCeS7arZqyCCai8yZQLkZL5GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f656bb517c.mp4?token=KTMlKfXuhURJY9eoaCdr4xmPUdOG60OWf3nhnNUXJWP_wOAAWcLKtnnx87d6DmbQ_OZe7LpFw03PYxiQuARDZn_t7RL7MNgXNZhBCw97h8i1KqpsW4ROS6b8v1f1FZewvR7M7-M8wHin9moJj_e0Eo81bxnlcgKHWagLaNOTPopHe9IIEup7R5n7ko-6QCV-6qguncvhGVdy9evHeDz4jqc8HepJRn0CSlskUxclpA8Upo0gljzD7qrywFCN_Bew6ws8xZIg4wYbpiuSPELIqo1MElhrXkxc-RuD8Dt0Zp2kotyuCe1rJChe3ixMcxCeS7arZqyCCai8yZQLkZL5GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: اروپا ابزارهای خاص خود را برای دفاع در برابر موشک‌های کروز دارد، اما وقتی صحبت از تهدیدات بالستیک می‌شود، وضعیت بسیار دشوارتر است.
🔴
ما مجبوریم عمدتاً به ایالات متحده تکیه کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/123278" target="_blank">📅 15:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123277">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
سپاه: شب گذشته چندین کشتی با دستکاری و خاموش کردن سیستم‌های ناوبری، قصد ورود به خلیج فارس را داشتند که نیروی دریایی سپاه دو فروند از آن‌ها را متوقف کرد؛ مابقی نیز مجبور به بازگشت شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/123277" target="_blank">📅 15:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123275">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uKcOqaD3Rnkpj3LNx7WH2Ncnf0GGGhz70TeGu4pFy3xfV30qqGyrQTUE_dNX1ZjYkTE33ZT_dOL_bk7BX6aZzx3xMEvN9uwXVpQyCOxFd2N-ISRBLYHNIdEhj1-j5GnKUbO6RAJm_DwkrIeHETobkaF-tlExrBXW4-ihDg0U5lz3tgGDmkYuk-oUiWaGsv5IwtgPUmFpZYPbCgqFE3Qp9yXKis26VCEVfyfl3CAOgdnXSi0D2q56M_PkVDbtzMo-msTJm0i5_6ULpLCKOnvAuqfVxWuytZuHLf_o-2tQYUu2lHfCG9axat4J7fHJJ3Ur1t8EhxN7cjY7O83o8v1-fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oXO8bylDPOZeHmPrvoKKuhUOUD8GqNG7CmhWmHIFmD4eb5Fb9mghtF-fvmeWVb5k27MY8rxaZAX2I6RcfcmADkXv-JpkRNB5qf-hMq04-Lt0aPFCB7FqUR-6uovOjze4_z16xdJBWcn1XsgF3Zox4PNfxYhb3Ns_EqGrT3TR09lpZn0tDOtBKGPUpH2DuymXL-SqnWjyqJ0pr0UCdYwfps5E-vuNUF117QyV9Lhg0rgyqcH43_saVK1tqfPHa6VompQLz4-hO2rclSz8BYXYOQ3-0dMOh1-_7HmUbJGkrx5iOT5fnkNcvRl-Mwa5QxCut9pjAIMBSptXKBXB_D2OnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات هوایی به شهر النبطیه در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/123275" target="_blank">📅 15:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123274">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
آکسیوس: افزایش فشار واشنگتن بر کوبا؛ برنامه‌ریزی واشنگتن برای بحران احتمالی در تابستان
🔴
طبق گزارش آکسیوس، دولت ترامپ در بحبوحه نگرانی‌ها از بی‌ثباتی بزرگ در کوبا طی تابستان امسال، فشارها بر این کشور را از طریق تحریم‌های شدیدتر افزایش داده است.
🔴
مقامات آمریکایی اعلام کرده‌اند که در صورت تشدید ناآرامی‌ها، گزینه‌های نظامی احتمالی را بررسی کرده‌اند، هرچند تهاجم مستقیمی برنامه‌ریزی نشده است.
🔴
این استراتژی بر فلج کردن اقتصادی کوبا از طریق هدف قرار دادن منابع اصلی درآمد و شرکت‌های وابسته به ارتش این کشور تمرکز دارد.
🔴
مقامات این رویکرد را یک «شتاب‌گرایی تدریجی» توصیف می‌کنند؛ یعنی افزایش حداکثری فشارها در عین اجتناب از مداخله مستقیم در شرایط فعلی.
🔴
واشنگتن بر این باور است که تشدید کمبود مواد غذایی، برق و سوخت در کوبا می‌تواند جرقه اعتراضاتی مشابه تظاهرات ضد دولتی گذشته را بزند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123274" target="_blank">📅 15:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123273">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: «علی الحسینی»، مسئول موشکی حزب‌الله در یگان امام حسین ترور شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/123273" target="_blank">📅 14:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123270">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQh9i9Zkr65cOZrMy6M4Vo6A2TD11vpEwmYotl6lQ57ttB-JtCybPYRSTt-B9iA0h8h5AqHeqEakW0i2wuzVYHs_bmTrSCAIkqu6hxD953vmto14KKIPG1Imdq0Se3cs4QjYQLz5i3PbQGPpkCDqgImg2schFugwFdYV_lPD_52S6CUtyKIXcOy2NIDdj0y-1sQTuOW8RJDzPJGDcr0gNqDL2ncef5BytVagXwGaDFSrQWMpXhT99laqj3KAbj2zsgV5v3tzSupAHe1eckYDFZnY4ATOoACSuOhy1zmmsUiUR-b2--UU7UG4UgSdpi_RblESFXKnSjhcX5TGMO8C6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kOQxSFU_zK96gUSD_DH8_umBiePLwN2Am0QGoY3RoogJGPto5HudqqH_0t1DeOuqjhmJlSBKz9YaSMZc6fzd1oViYFaKhe6IWgpV3iNDszRIxezn_GWB2tZ7HmdZ4b6tbJAexqE-gtIpWDhwmumcyuvhufd4IAYKmd9biua4QRGjSaiFEbzFERr_Dk82B2VmY6nL_5jfYtuGMB2QB9kua2UGB6banzW-C5vOafn2836HiHMqpkMtzlRuFSDn4MJU5aXgS1LVuSr5I5Ha18ngn4sTzMMS2xhS3tYqhcbKb7m39Q2W9cDH4RZxTcLQTnG3s_f4Z96tednAw_LvH5IMng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b60d30259c.mp4?token=LesVCvoOaPo5leY9hQE1Cq-0_1aVUbWZBaqbFv39E82XmWkVdq0e8hkw2LMvP_CzP6pZMEZtfu_VJLgxewv2dAryOsqvWF57mdi_ZHDV3hyzo9arNkZnPGO2k3h6iiiWydw8-PofxGUtpg56vrT9mvVwIB1BwX1r0WT8wYUy8RpyUqYBSqMHA1w9pSi6QTmx731Gc91GfR6mqPXicQh75uCJzcEDJSsZfm-Cv5pzV2XCmX30pf_II9iPvFkE3yrfiE1MdpD4zgYvE992IjD7nq-8I17DpIte4x6vu0NRBIGhF8-8EhjQAmelUu-SluXuEw-RGpCJR4ONLqTh0evkaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b60d30259c.mp4?token=LesVCvoOaPo5leY9hQE1Cq-0_1aVUbWZBaqbFv39E82XmWkVdq0e8hkw2LMvP_CzP6pZMEZtfu_VJLgxewv2dAryOsqvWF57mdi_ZHDV3hyzo9arNkZnPGO2k3h6iiiWydw8-PofxGUtpg56vrT9mvVwIB1BwX1r0WT8wYUy8RpyUqYBSqMHA1w9pSi6QTmx731Gc91GfR6mqPXicQh75uCJzcEDJSsZfm-Cv5pzV2XCmX30pf_II9iPvFkE3yrfiE1MdpD4zgYvE992IjD7nq-8I17DpIte4x6vu0NRBIGhF8-8EhjQAmelUu-SluXuEw-RGpCJR4ONLqTh0evkaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / کانال دوازده اسرائیل: پس از هفته ها ارتش به طور مستقیم به بیروت حمله کرد
🔴
برآورد می‌شود این حمله برای ترور یک مقام ارشد حزب‌الله باشد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123270" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123269">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
قطر و امارات، حمله ایران به پایگاه آمریکایی در خاک کویت را محکوم کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123269" target="_blank">📅 14:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123268">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MP6VZNCr6LpABxGvWbg2vDOHVoDrGXIunIlpn-lyGQHpmXqtrH0o4z5bIbSRfCFzPhBkv0fWptIYrPVQySrjDSgVQD65ZPrd6EGfHi2DsvMGQ2jE4A59FXHuPmWJOEkdbCHPJzL37kdXO6MEa2KoDSrlSk_cztqQKLjcoFyKniNlOPw6y0NIceuw0Zs9Ag_nK8pR19nEfTPaGY9J_rOguF0QQU_GqfBrYbDAjujsyqqeq512swQrFThbcOBxiQrDEtdptO7bD1eBWIWzx6AwlMM9CScv8aTjJxVpxNnTygnujF63xvI2Ky0DE4URctCi2ODrh2w7wv4CqVs4TJpe0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منصور هادی رئیس‌جمهور فراری یمن، در ریاض درگذشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/123268" target="_blank">📅 14:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123267">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری/سنتکام حمله ایران با یک عدد موشک بالستیک به کویت را نقض فاحش آتش‌بس خواند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123267" target="_blank">📅 14:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123266">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBEsql1Ko_jUIft97Rtxh0dsPfvazDUkJfWkclYiqkpg4L4Cx7V51x5EIRA6tJ3Mfr0JUGLqRoWx_J3PhrxZCw-SXRGs6npt3V7xjQ_578hjttlaEuXywxALp55ZujFz9lgAKp_tQl6nYVEc1W0XIOE6DoNshAuZsBpvQ75VVN9itrxH9jrSuAoQGKYOKB2bUuiyy8UD12i6-J9bdqucznYEVXkQd0NHGimnlLFdS74BYU6wzclVlMEZzcHIwfoCvPyAFNjRUmSSnC0L-ktljJ46Km-el23mJcLvWNNTQbmHpUgUXx1PXuqfzu-vExmD7lvTd6Stk_D7hnlc0nSKRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جروزالم پست: کشورهای حوزه خلیج فارس احتمالاً درخواست ترامپ برای پیوستن به توافق‌نامه ابراهیم را جدی نمی‌گیرند و آن را «زودهنگام» می‌دانند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/123266" target="_blank">📅 14:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123262">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QuQRNrzU3kY5fGtdn8228-BmtoCD4T2EpIy648E9IPos45NZMoJ8jA-8LAj-iRGqevLLPmeYxGUrOUZsShgJvPXcTPTS8s22kNZkKcY_idl2YppPZp5RgbCKrQ4HW1LP-MuwWHBDh48D-hsp8rNjdBRLYOAQDDAvyAl427zHgC0qFOVjr0qQP23TUZOEDaTmxeMtclBoJGkZawtyQjfthI3bfJblWmSUnLtyIIfj9q77YJ7UHQhZcrjcdh-a0sVU5gSK6J5TaEWo2HdE0uI0eU0bfGBaSnwvY-dRMPbYAfcq1bFjx6JLIAMvuepDICZXgOhQk0skL5z4XQPYOJVqVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ddpzrwDgPcVVG0i6chlhmxGaTmcWvSDYKWvWf_Uax9RS1SBBZEgH3wGVyNvvX1Kh8h-DUlw0ENew7iGOJM9G7O62ADno-R8Y2RP-aZFfNAFNj2BAg4fu01rnRpNhpAdtWtjsdfiVb_Pb16wHTk1tZ5wsNbb49CUfNHxDINO1Qah3kXUUQaxrmEvr_Ht6uOlbccqJD_8XI1-tIpBTOKJ4K9Mgyrxq_el8FY5ZBqpU4XN_Fvp3Nk1iTOlmWAJd8NVhg37WeYB5XNtuHRWI0zlgLdQNKSyMXCSYhHXLMYzwtUEme3-LqfOZVx_JKcpOnwFLSMuW7X0G4WFi9R2lBbq2Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E0GFtGInmboginVqFb2dkfYH0OZsWUZcSC9XZih2SoZcztlle7qtibHZS5p9lhAzG5AOcvZWDlGjo10Q-uS70OBSszcThGkgapRnaS9n6bY96pF4hcbh__PDTHi1h-dU_FJwEeW9hQj9Y9iwV_CKAFjNiGlUlzK62o43A1BnUW5lFjLSxgqj_OvxFDCBfXtJwEAykl7f381egqJi_2k_RVxsqsgGMkObr4uleRfy8YpHxAyi_hV5hvCw_l-PoT8Zcuyfc75o_TMiOWwV2jaDur-KIX0rUG3QPPpuwauTzftLcA9jj_dADXVqIUS0_0EhuiJV_nXNuktK7otw5Pf39w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c4Kwj-eQuxSfaMBKafUtilPQjPxpRkp5_D2s8zlhtzKWxF0OKFSisIdKbF8MOMo9fuJSpaz4Lyo-qYZaJUQ13jFK6d3t2ekn0DP79aXzeLHh5cKPPGEN-cLQDr5QgzdUd-CMJop9LJMv_tn-AdlXqD5P7Wa_t0qJfeT3alC_ENrjUhQ5a8MxJgp2oOyNp6FR8EgPJ8pp82y3d1sBVrWtcU-tK-LXvWrGvWJbEAokCZpdiw8jkUYOP_kOj87RdF6114fKv290x6mTO35Q-pzwQ1JG-2eA3Kgmnx3jvzJgo79Z1w7-ucfH1RrYh_-t3AJcz9Ve2nYoHWsy8F0Auzr5DQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای که سی‌ان‌ان منتشر کرده نشون میده که تا حالا حداقل ۵۰ تا از نقاط دسترسی به ۱۸ سایت موشکی پاکسازی شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123262" target="_blank">📅 14:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123261">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da27079b92.mp4?token=ul-OSBpDM23_bG60ZZgB5dKy49iGdZhsik6rBV70LKN6EzhfLYPE0WMc5ap5Zxet3SG50uz7H00DPOv8aJNnFfVVPwqw0InQH5d3lp-HTMBLqtNvRcP6sHZct72QGnKw3wGABiOMYup1aPVyfCk2EJC08m0eUk9fmlLFN05YgJ37uH2SRUWdvEVCFLDgvenqMMjUE4RXDeasm1wBKFD5C8fUMD4XqGZJ31nONHcPnEXKJz_hXHYaFwP73_mZK-0-16_afig4a7umiOtTiwyRWMNZVm1wcmBrXA7S5If7pKcQCfJRKpNLC27TpWNC8t2mNWvsiEa3NK071g-u-7jqGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da27079b92.mp4?token=ul-OSBpDM23_bG60ZZgB5dKy49iGdZhsik6rBV70LKN6EzhfLYPE0WMc5ap5Zxet3SG50uz7H00DPOv8aJNnFfVVPwqw0InQH5d3lp-HTMBLqtNvRcP6sHZct72QGnKw3wGABiOMYup1aPVyfCk2EJC08m0eUk9fmlLFN05YgJ37uH2SRUWdvEVCFLDgvenqMMjUE4RXDeasm1wBKFD5C8fUMD4XqGZJ31nONHcPnEXKJz_hXHYaFwP73_mZK-0-16_afig4a7umiOtTiwyRWMNZVm1wcmBrXA7S5If7pKcQCfJRKpNLC27TpWNC8t2mNWvsiEa3NK071g-u-7jqGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل : تو ۲۴ ساعت گذشته بیشتر از
۱۳۵
هدف حزب‌الله رو تو صور، بقاع و جنوب لبنان، زدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123261" target="_blank">📅 14:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123260">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52efb03882.mp4?token=peT2o5B_TlOnUkvV-V8E-CphOhiqkMA3LpuLK26KeDWrqPFQ-5U82W6dE7tk3UIcCQCpLjTvr7Ro9g1T95qyPXOamV3YMVdrvQrRK_pvyEwbyEYt-KNcwhJuQRUU1oXBv1MbbhYEVTxZqydKweHCOkSTwYQ3NzRQTTUmhLOIOYpTKJCBQG5zHj_eKoRmrSQTFMPs5pxzlllMAm8Y9xy07TedAiHu_VwpV-vopdSzkNXeeK67vfmBkXuiTNl81PJ146FpTG2d1nhzIKWNoGaXV-umMBpYpYrBh9IvhryhmSx2VxOabUSz3Fr-061T6F_tlpBRwO35L6e8EfzCnzIDYlBA0KxAmNpbdSH0vDH57D4K69DHaMZTlkVFHw1psIWtFYrqyBWYU7nGYbWPfnTMafVR2PpXf9cxnHUZQd3gId-Wv2zV_cOE7srdiQXo-WC3ke-QeMaMP465ghD0FvlE-f2SZgdnN0YfFsIXgh2wwTLi0s4wQNtimy60_hLFGmZjA2D_RSeE-8d5jLe0yse9IKqMQ9kPqEuvQpx3ZSE9lBvh1uGRuL24apGKzJa1PUF9y1cGAIPMXHbhu_lbVQ0Cyfm9l2z-gQ5e6wwXxxstUNZCXbZ6hcxyxy6uYZw3kENKVF33C_0fAGeZUin2xX9M3q6o8vNUBm9lShUhx1jqTjI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52efb03882.mp4?token=peT2o5B_TlOnUkvV-V8E-CphOhiqkMA3LpuLK26KeDWrqPFQ-5U82W6dE7tk3UIcCQCpLjTvr7Ro9g1T95qyPXOamV3YMVdrvQrRK_pvyEwbyEYt-KNcwhJuQRUU1oXBv1MbbhYEVTxZqydKweHCOkSTwYQ3NzRQTTUmhLOIOYpTKJCBQG5zHj_eKoRmrSQTFMPs5pxzlllMAm8Y9xy07TedAiHu_VwpV-vopdSzkNXeeK67vfmBkXuiTNl81PJ146FpTG2d1nhzIKWNoGaXV-umMBpYpYrBh9IvhryhmSx2VxOabUSz3Fr-061T6F_tlpBRwO35L6e8EfzCnzIDYlBA0KxAmNpbdSH0vDH57D4K69DHaMZTlkVFHw1psIWtFYrqyBWYU7nGYbWPfnTMafVR2PpXf9cxnHUZQd3gId-Wv2zV_cOE7srdiQXo-WC3ke-QeMaMP465ghD0FvlE-f2SZgdnN0YfFsIXgh2wwTLi0s4wQNtimy60_hLFGmZjA2D_RSeE-8d5jLe0yse9IKqMQ9kPqEuvQpx3ZSE9lBvh1uGRuL24apGKzJa1PUF9y1cGAIPMXHbhu_lbVQ0Cyfm9l2z-gQ5e6wwXxxstUNZCXbZ6hcxyxy6uYZw3kENKVF33C_0fAGeZUin2xX9M3q6o8vNUBm9lShUhx1jqTjI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: امروز در سوئد به‌صورت کاری حضور دارم.
🔴
ما در حال آماده‌سازی یک بسته دفاعی بزرگ برای اوکراین و یک گام قوی در خصوص جنگنده‌های گریفن هستیم که قطعاً نیروی هوایی رزمی ما را مؤثرتر خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123260" target="_blank">📅 14:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123259">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50b5ff794a.mp4?token=sHguo7khiXA8CJwmc4qvjOBgRMljWBX1VDloAhkNWjk0qOqv8-VStyTi2CiXKk75D_KDm9klJ5ox_RuLnMC9ifueGkYS60s3ggFUZOh-K8fBtPvmYhcQrPB6I3zp6iN1bBf_QRMX1ULVHsurGKujdzkzqHNi3M04DOp710KuL1DceBQN34ca4NSQWdLrMESAsO5N-rxvR5OFq2whRbyJq8PnMYMc9foMsXNSUIP7z6rV15NiXM5_k6pNpZqw9tlww8MfsRc6rSJMn_r6YolC5IE9tLo9RhaQH5wrrA88p1SNK3Wv5DAYyG-PZcy2L5L7AsfOEcBVicBl7dzGlONErA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50b5ff794a.mp4?token=sHguo7khiXA8CJwmc4qvjOBgRMljWBX1VDloAhkNWjk0qOqv8-VStyTi2CiXKk75D_KDm9klJ5ox_RuLnMC9ifueGkYS60s3ggFUZOh-K8fBtPvmYhcQrPB6I3zp6iN1bBf_QRMX1ULVHsurGKujdzkzqHNi3M04DOp710KuL1DceBQN34ca4NSQWdLrMESAsO5N-rxvR5OFq2whRbyJq8PnMYMc9foMsXNSUIP7z6rV15NiXM5_k6pNpZqw9tlww8MfsRc6rSJMn_r6YolC5IE9tLo9RhaQH5wrrA88p1SNK3Wv5DAYyG-PZcy2L5L7AsfOEcBVicBl7dzGlONErA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین از ساخت نیروگاه هسته‌ای در قزاقستان خبر داد
🔴
در جریان سفر رئیس‌جمهور روسیه به قزاقستان، توافقنامه ساخت نیروگاه هسته‌ای توسط شرکت روس‌اتم روسیه در قزاقستان، به امضای طرفین رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123259" target="_blank">📅 14:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123258">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaff230743.mp4?token=qMycbzjR_msASkj8rEhXoEm2TPlGO4CukNmpF7mpJCVHtMTDBSkJMO2KjMf6PcFYb76s8IJD5773oS0xy9LViZUOSzwlvFMW_a9Q0GTg4a4IRRLa9aUPeRe6HFj8E2ubV3mjPgQBoIPtO90hOqi33t8BOr4rISDymtCjmD0B_RCMGdXcHB_j-aDEPysgOcdKL-tRoTEnpn97wbzclEizVNfoTZ0qtW3mh2NcQgG47QynebXMsLCdqX0jewELPEOLiwN1XxyDo1x4MjouIb-QJepr_zTaF_1jhof6YzvTBeaDnq3I6g2d0te5pDx0VMHJb-1LwA2L862Kmu1dHSV9KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaff230743.mp4?token=qMycbzjR_msASkj8rEhXoEm2TPlGO4CukNmpF7mpJCVHtMTDBSkJMO2KjMf6PcFYb76s8IJD5773oS0xy9LViZUOSzwlvFMW_a9Q0GTg4a4IRRLa9aUPeRe6HFj8E2ubV3mjPgQBoIPtO90hOqi33t8BOr4rISDymtCjmD0B_RCMGdXcHB_j-aDEPysgOcdKL-tRoTEnpn97wbzclEizVNfoTZ0qtW3mh2NcQgG47QynebXMsLCdqX0jewELPEOLiwN1XxyDo1x4MjouIb-QJepr_zTaF_1jhof6YzvTBeaDnq3I6g2d0te5pDx0VMHJb-1LwA2L862Kmu1dHSV9KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوی عجیبی که توسط کاخ سفید به جهت ۶.۷ میلیونی شدن فالوورهای اکانت کاخ سفید در تیک‌تاک منتشر شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123258" target="_blank">📅 14:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123257">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
کویت : ما حمله‌ی دیشبِ سپاه رو محکوم میکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123257" target="_blank">📅 14:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123256">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: منابع دخیل در میانجیگری آمریکا و ایران می‌گویند در ساعات اخیر پیشرفت قابل توجهی حاصل شده است و شکاف‌ها بین طرفین در حال کاهش است، اگرچه چندین اختلاف هنوز باقی مانده است
🔴
یکی از مسائل اصلی حل نشده، درخواست ایران برای تعهد واضحی است که امضای توافق به معنای پایان دائمی جنگ باشد، از جمله درگیری‌های مربوط به اسرائیل، ایران و لبنان، و اینکه پس از امضای توافق امکان بازگشت به جنگ وجود نداشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/123256" target="_blank">📅 14:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123255">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
الجزیره: سقوط سهام آسیا از بالاترین حد تاریخی خود پس از حملات آمریکا به ایران
🔴
ارزهای آسیایی با فشار مواجه شدند، زیرا شاخص دلار با کاهش امیدها برای حل سریع جنگ، به بالاترین حد یک‌ هفته‌ای خود رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123255" target="_blank">📅 14:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123254">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1sVivQ-QEYLn_qaWTQw4jJoIiDrS_7QcREa5r8PeSXh_4n-T9STY75wrKj_Wsv1OeccDXgLSYU_fSfyf8R1J5mo2G13T5vXmsAuIadg_Q2UgSMnbLhaFucC8OCg5bdr8MUdy6KHFXDD9XOfbmUZkyPkXY1Q5itM5tk0oFJq167dEVX9uFblJh5j-V62d2XQsO4wBMl4SNKSsOLgVHn07DQG2dq4pzXpxSC-Lj2SS1MlKRcEHkEEhRXi8w7WRIBhf9SDrA6e9VueOvL0wX9TWwj2KTiVRtj-Y5l8OE0a6UNrzMyeuPe4B5UJ8xbgaXRzJYIWBIQXyuP-XYgVUJickA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/123254" target="_blank">📅 13:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123253">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
کامران غضنفری، نماینده مجلس:
آمریکایی‌ها هر روز ما را تهدید و مقام‌های رسمی ما را تحقیر می‌کنند، نباید با چنین دولتی مذاکره کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123253" target="_blank">📅 13:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123252">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24b3059c39.mp4?token=W4nVaB0i9XCXqrKQaZPu2RxRDgxvn77RPQXc81cIOtTZyCZzYtLLS5m477tkwigxsUQ7e5o0nLPWRZJdC-eaGS5c8pFFI0w52pK-EC790xbXMrl59dnWTM7uIP4jHqcyHv5F7mW9lOf2Edbu7GvALN2pNgtQNcywzVpMMCsMbmek-gECjnHdHflm_vFBA_Goltj9E_-PG7HvdUkhxqJ6mv0gTOfkOniNzl4Cqv4iYv7qrUaW_s_aq8wxVMzeoir3PZ-TU97RQbF6kE8YOsSaJH8He11sAM0xO7wl-a-JTVsOjnFMcRtIiDWqJIDcPkIbBDk0sfDdn-iRrFw6WlU5Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24b3059c39.mp4?token=W4nVaB0i9XCXqrKQaZPu2RxRDgxvn77RPQXc81cIOtTZyCZzYtLLS5m477tkwigxsUQ7e5o0nLPWRZJdC-eaGS5c8pFFI0w52pK-EC790xbXMrl59dnWTM7uIP4jHqcyHv5F7mW9lOf2Edbu7GvALN2pNgtQNcywzVpMMCsMbmek-gECjnHdHflm_vFBA_Goltj9E_-PG7HvdUkhxqJ6mv0gTOfkOniNzl4Cqv4iYv7qrUaW_s_aq8wxVMzeoir3PZ-TU97RQbF6kE8YOsSaJH8He11sAM0xO7wl-a-JTVsOjnFMcRtIiDWqJIDcPkIbBDk0sfDdn-iRrFw6WlU5Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین : حجم تجارت بین روسیه و قزاقستان به‌زودی از ۳۰ میلیارد دلار عبور می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123252" target="_blank">📅 13:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123251">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
امواج مدیا: قطع روابط سومالی و امارات؛ افشای شکاف استراتژیک عمیق میان ابوظبی و ریاض
🔴
قطع روابط دیپلماتیک میان سومالی و امارات متحده عربی، نشان‌دهنده یک شکاف استراتژیک و گسترده‌تر میان ابوظبی و ریاض است.
🔴
عامل اصلی شکل‌گیری این بحران، سوءظن شدید موگادیشو به دولت امارات است؛ چرا که سومالی معتقد است ابوظبی توافق به رسمیت شناختن متقابل میان اسرائیل و سومالی‌لند را تسهیل و هدایت کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123251" target="_blank">📅 13:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123250">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-m6RybAsgRgLZV7EKWgTOl0mCyP5jxHIwZ0zxhlWPIlrWFyFth4jhG661nYBSiUjxDfJj75j6KwHaJP3091HF-LbVeyQbl_qXP0jaoBnK-7uJHdfz8aJwXu2BkjjhbR5gVQL-wmcfvml5Ku8l0qmo2vnbsdmTDNEYx-tna8J4WbX3WoVfBwDVxVJw5tw7Xw7IIvjpSG2toQ2N9LRxa01wuEgqagYYE40xJigeVw7V5abYLWEmUkh3clbTD3Mi4FSUTsRws-VEVEpYl9qtjClEosYqodictC7JdyE_RlYqAwjdRAW8RwgOx6MzCP5AQcC89jj9nlfzgk-oqRLSDkDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۶.۰۴ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/123250" target="_blank">📅 13:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123249">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOR_s6k1pokX-vVCHxN41d4pittavsBtfwImiReWrtV5QLTYC6ZYTNMaRnEyCd8l749Pz-zNlV3BlupR3cVpBAuT3cFOgvsx2DPcHDfmAyCiAri0p6aJq1v14-CW00tEeLR9d5bGTa91XOvmwPKQUYLKmu7N6J5Q67jdkN1lBqbd65KXJWhwChI-sQTv7jNKHgmRtVrVDNABCi6ND_843HXEiLy5fDkbIcnwDbLdRC6OyEpCBQ11vV8XQtYsnj_7p9SuiF3PqYN8kKatAuAUtfxCfO7qg5k3K97XH2EwZ4IyDxWbYOAgl7gK1CoVjb0CV6ePSdwAAYQEoEg-yJ58ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نمودار جدید نت بلاکس نشان می دهد همچنان بخشی از محدودیت های اینترنت باقی مانده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123249" target="_blank">📅 13:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123248">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وزیر علوم، تحقیقات و فناوری درباره زمان برگزاری کنکور سراسری ۱۴۰۵، اعلام کرد که پیش‌بینی ما این است که کنکور در دهه سوم مرداد برگزار شود و رئیس سازمان سنجش به‌زودی جزئیات آن را اعلام خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123248" target="_blank">📅 13:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123247">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzcvxootPQbFQAOKE7FsgB7-xwx9_CM_kj9eRpHV7pQ72LPhtywHz1rDS4xQ4JYmNkzXX3O_lv-h8sJfPaBJATwPgZ6LWTvEWQuEl_VDC2svp3vLm7uTpZSzEcXu25KstrMXqeB7YAbCj2Wjmy6Y3OFhX6HrBHEUPBJ6BMWSdzZYjj3MH7_4XB6vfVNbxP-tclQr8pvyXLT0nM-Cc4oX-eaaOL1zi-RKZUbFKkmT2-8dkEeFN9pYziIyPW00zyWFyJFGXgSxJeVARDITVPQh_x3czZWTPzylhUIwUYxN9nl_z6mgnFWNl25_oLAeXIcZmgUNZUQsnsmuFyroBIXIxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیوارنگاره جدید میدان فلسطین تهران: اسرائیل ۱۵ سال آینده را نخواهد دید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/123247" target="_blank">📅 12:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123246">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClcE_yuJR7xl4ogGSjPIr9SDAjBpSisP2SMgm8jmUJl7wPHaOAFLjEzydN0EUzUVXfmvlREzg8yorC2_VUrIA8yHk0wWxVb5MQqzaR9Y1GRjN__c98_pHsWm7LNXCWyJLPKTaCbzZIGzygYLew-RNpdR8-eRFd_RLbV1PX8pdC1CALhfWxzET52GhdSPM7z4qVwevuW7mmYW-LC862BsXW2cnbxatNx6aIA7gTIlNvSl1kZtd9zGSqhuWrrZVuDLLOjdtdNH7XSP3ycYy19v4Ead0DmjB0tzYMYwHoVqhkvCUZyk4tMOnbdgWWmhIVmuOhlF5yUITm5XjSsYjcAKtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
«روزنامه وال‌استریت ژورنال دیروز گزارش داد که ایران برای دور زدن تحریم‌ها و محاصره آمریکا، از سازوکاری موسوم به انتقال کشتی‌به‌کشتی استفاده می‌کند؛ به این صورت که کشتی‌های تحریم‌شده حامل نفت ایران، پیش از ارسال محموله به چین، بار خود را در دریا به کشتی دیگری منتقل می‌کنند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/123246" target="_blank">📅 12:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123245">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f949a64946.mp4?token=WU0Kc9MQ-OsxlpJHSqrB5w5UYJO7cZv11chj5bLxQ68-zvD3LJSQxoZheUfbv47CIdK0b4ZyI6-WOXOMwa_O-IdTAMKuO-IhvyQt7yzYVVnyiWPPMfITb13swuEXAtbaNtlyYCFEr3b_IRmhxNiiex3iXAizpDVFakLshIZyY2mwiB5v0hMMPezYIiUtj7iaB0Q_u-OxrfK7v63xNFQf-IP6W8iBjxF8iojRi-iUfHpWuvv4J9H0spBJ4P5xsgGFW37JXyaPo_1eTAC5yUZDCaWGbeJQkMr-_QaUX_7m-PH0H7CnVJP1izVH2s1A7LXapIReivqoy5cYpmayJ7vIgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f949a64946.mp4?token=WU0Kc9MQ-OsxlpJHSqrB5w5UYJO7cZv11chj5bLxQ68-zvD3LJSQxoZheUfbv47CIdK0b4ZyI6-WOXOMwa_O-IdTAMKuO-IhvyQt7yzYVVnyiWPPMfITb13swuEXAtbaNtlyYCFEr3b_IRmhxNiiex3iXAizpDVFakLshIZyY2mwiB5v0hMMPezYIiUtj7iaB0Q_u-OxrfK7v63xNFQf-IP6W8iBjxF8iojRi-iUfHpWuvv4J9H0spBJ4P5xsgGFW37JXyaPo_1eTAC5yUZDCaWGbeJQkMr-_QaUX_7m-PH0H7CnVJP1izVH2s1A7LXapIReivqoy5cYpmayJ7vIgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سپاه ویدیو حمله دیشب رو منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/123245" target="_blank">📅 12:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123244">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
تعداد مبتلایان به هانتاویروس مرتبط با یک کشتی کروز به ۱۳ نفر افزایش یافت که از این میان سه نفر جان باخته‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123244" target="_blank">📅 12:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123243">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
مراد ویسی: یا توافق میشه یا جنگ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/123243" target="_blank">📅 12:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123242">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
کرملین: روسیه به کارکنان سفارت‌‌خانه‌ها هشدار داده است که باید کی‌یف را ترک کنند و پس از آن، هر کس تصمیم خود را خواهد گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/123242" target="_blank">📅 12:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123241">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKKH1E-iNCCIyBD_6_rJBdguJJk85bqXjHLs-iAQtxfWhdvhxbRxG0ulHILW7rTNdHH1aP4yHpzlwER_bPv5cTM7JPZEzkbEnIYo6-pXjgOIkWQbDz8F6Xat_kkfGb86Rpw084dBmLlS78pGC5xTLoTfOKh03cievbBSsfnRMV5nR06JM8hWfiRzwgKjFO6N4uJ-B2hsZZt5A_8cbxTZbu42D74tHjeJ7VXwirMELYPycDwK0h1Xh55PWaxTKo-WTi7AHtOUsyUbBRy-6eoJVP4223QwBBDXuOKuW-lWNpLSfoXN3z7i6-dJACDeaSlqhbtyOuVcZOq41_HznP3dzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در یک پست در Truth Social از نخست‌وزیر ارمنستان، پاشینیان، برای انتخاب مجدد حمایت می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/123241" target="_blank">📅 12:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123240">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ایر ایندیا، پروازها به اسرائیل رو تا ۳۱ ژوئیه لغو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123240" target="_blank">📅 12:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123239">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ان‌بی‌سی: پنتاگون فهرست جدیدی از اهداف نظامی ایران تهیه کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123239" target="_blank">📅 12:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123238">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/850994c0bf.mp4?token=u8bmEJjiitx14dssbDbKlhj6HaeQpl3xJRTFUzj2o97jE8xVa9zWZH5Vfr1LpTTVaunjTwTm3n4dfWrZHTYa0wy3zhPDaRs9PecYqPnkJP0Lav653wNGmOUTMHtnDopl92D83yXUUCbM7fZQhh-4lRj9s4IaUu45n8eRX4NiE2mBGf-xj3skKpVs8Plh-5FwsmQ8Amn-NFdVaV2xsK3ktvM6SCgXjJT8Gox51av3jLnskOhNZ7m28pPVJOWsxvgcNdEbfmCrJAq9pOGROBWhBB2S3o0Islt-yP1w6CrMF77cbc96n0KAVgW2JxMih-J2GtptwHrMZNNDn66Zzis2rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/850994c0bf.mp4?token=u8bmEJjiitx14dssbDbKlhj6HaeQpl3xJRTFUzj2o97jE8xVa9zWZH5Vfr1LpTTVaunjTwTm3n4dfWrZHTYa0wy3zhPDaRs9PecYqPnkJP0Lav653wNGmOUTMHtnDopl92D83yXUUCbM7fZQhh-4lRj9s4IaUu45n8eRX4NiE2mBGf-xj3skKpVs8Plh-5FwsmQ8Amn-NFdVaV2xsK3ktvM6SCgXjJT8Gox51av3jLnskOhNZ7m28pPVJOWsxvgcNdEbfmCrJAq9pOGROBWhBB2S3o0Islt-yP1w6CrMF77cbc96n0KAVgW2JxMih-J2GtptwHrMZNNDn66Zzis2rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از شدت خسارات وارده بر تاسیسات فولاد در اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/123238" target="_blank">📅 12:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123237">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
کره شمالی درخواست آمریکا برای خلع سلاح‌ هسته‌ای را رد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123237" target="_blank">📅 12:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123236">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وزیر دفاع طالبان : ما ثابت کردیم که خاک ما تهدیدی برای ایران نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/123236" target="_blank">📅 12:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123235">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8c7JMSHIVZABcbJAuFu07RNqAzlW7GUiPFEI55Z42pbYQqyyYEVD2NI8CnGeGVTTYBOynEoV67q3CWI8eSlsloyoi7x3OApdAkDde-x_9YgZxutKXHENeFjblyChRLm5PvXmEug9v_z-xL4j2OK-H7MrtdfaqKztj3ZWTpwsVoSQJmpCtKNSWOThxpf753BNPsYuyj9htYzU9b7ulGmCy6icL4AjRVBmfLL3pukIxI01o6dvc0Egw9ldHW58IW7JBsNiCu2YndJr5WQOSt4kdwsBnW3iZbq0FVGZJq9B023etiSgqdRMYwJ2rR9NptLLsizUuhoysboxuCbXX4esA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل بار دیگر دستور تخلیه کل جنوب لبنان، شامل تمام مناطق جنوب رودخانه زهرانی، را صادر کرده است.
🔴
(نقشه پیوست توسط ارتش اسرائیل طی دستور قبلی در گذشته ارائه شده است)
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123235" target="_blank">📅 12:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123234">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/943583b8c8.mp4?token=GjIsd_oJqYbbH7r1Xxn72iabt8veXEXPxaz0Y3N7i9gK9zhvwf3DDBzB8oVwYLErCNpWn6-Gq5g4WWp5Aa7tACqTez-clwbjHh68hcq_i3C8oDD_NtAWH5Kg-0Qa-kP2PY_Jpl_WRj1AqRXHtXQFQLQwkveoB5ZtiVzL712jTHSYDfiZgBz91JrvHmEEg60K_iD18v4JUk5H4S7WK_zoI6Idt5Y22m_zf1M8XqlGxEb9-fWjQfG9Qh-x84t3M_uW9wIXdrNEVf7ZTzK1uV7zrJGUcNjxJl9G1brZE44l3EYa5-WQD5UW5Fx7_4ZfEYksnkDuzpP5C1bxP8D23cKs8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/943583b8c8.mp4?token=GjIsd_oJqYbbH7r1Xxn72iabt8veXEXPxaz0Y3N7i9gK9zhvwf3DDBzB8oVwYLErCNpWn6-Gq5g4WWp5Aa7tACqTez-clwbjHh68hcq_i3C8oDD_NtAWH5Kg-0Qa-kP2PY_Jpl_WRj1AqRXHtXQFQLQwkveoB5ZtiVzL712jTHSYDfiZgBz91JrvHmEEg60K_iD18v4JUk5H4S7WK_zoI6Idt5Y22m_zf1M8XqlGxEb9-fWjQfG9Qh-x84t3M_uW9wIXdrNEVf7ZTzK1uV7zrJGUcNjxJl9G1brZE44l3EYa5-WQD5UW5Fx7_4ZfEYksnkDuzpP5C1bxP8D23cKs8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از شهر صور پس از حملات هوایی اسرائیل در طول شب
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123234" target="_blank">📅 12:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123233">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRyPB-D9bhov33-_oFoqd31hC8cIJyBvlwBJZd3slulSBF6BRG3s3J25CnRYdRvm2SnRQ643KZi9tH0x6ZkI5AU6LLGuatDLvO1NLpjfX2t30__3ruOe9KlmwE5Te-uxYuyRWxpcYsJ8nE-9QNjMlsPn2JdhamJAn3B1awYKhLanKN6TYmxxiKjz2qmXrwFsWJ1MLoOC9-EblUTpX_QPkODXWjOmMsBbgHwAvq6L3-gvyfPvLRcnWkrJY-n-7rYCLTMmwrtN-bZvGYnnqulHjUlssKfP1xGmDdi8eA0kDWM3JGR-MAR6stgnT3W-v_wU-LCHGpp732o6-3MqgVRqQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابوترابی، نماینده مجلس: دارند با آبنبات چوبی صندوق ۳۰۰ میلیارد دلاری فریبمان می‌دهند، آمریکا بعد از جام جهانی و انتخابات میان‌دوره‌ای به ما حمله می‌کند
‌
🔴
باز کردن تنگه هرمز با ۱۲ میلیارد دلار پول خفت و خواری است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123233" target="_blank">📅 12:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123232">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b2993715e.mp4?token=rTYP223oHx8LDI7Zev9Aq28AJ9PKBiAn5DtFDsm-JynT8DZsO1bEKAwf81J7m6IyCgJEh3DJqTtUgr3UsOkKvD44JSXRRRggKvZc45yuoMnCHKUuogRVdzcanv9-8ej1pd1iafA1_wz_IWk2kFhc1i7sTW-5cXZ5F60FksnxUF_2e1H2aoHndRsTu0rHCLey5I3JGItcJUi3oaH2FQLu-2sFecOAnZRvEiKDDybGZLe6psDcRH_OJC-SE3NZdk-VNXFjjzBlENtYofdrS5cVnpbVJw9lB-OPQ7lsM_D1ASlAxwYGISOso2gbqn8wQrrJJzSW8d5BTHVx9cGuRLu4oUR9Kzk6xvKxnUiE9K6brlxA0-0bczowaqNxilVV1J-7xv1QAOmYYEdDDpPOEJzLBiKPK0DGWMkOYPsB64ZUQFTzWWBT8gLb1YyPwnA6Jcnhh46cN82tFyqBLAYUfswCE-uTRvvA-Zvkcc6pVHhTKkjx3OkqK9VBVYh_AiOdBKv_aYWGbpVINoKUuayvgmn_mpOF9_gGDFnPlPUK_N--J3blG-Xy7-lWVnSyC_PwXfZdIUlEV-wkZwwNChIC20q-xQ4bX9-I6aqbgm_GY2TB7uma7o1ObkSBLhwXAmRhqiFzmpgKN_r3VVGNVKHrcEq9e8v5ZsooeuRzGicCbASrJeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b2993715e.mp4?token=rTYP223oHx8LDI7Zev9Aq28AJ9PKBiAn5DtFDsm-JynT8DZsO1bEKAwf81J7m6IyCgJEh3DJqTtUgr3UsOkKvD44JSXRRRggKvZc45yuoMnCHKUuogRVdzcanv9-8ej1pd1iafA1_wz_IWk2kFhc1i7sTW-5cXZ5F60FksnxUF_2e1H2aoHndRsTu0rHCLey5I3JGItcJUi3oaH2FQLu-2sFecOAnZRvEiKDDybGZLe6psDcRH_OJC-SE3NZdk-VNXFjjzBlENtYofdrS5cVnpbVJw9lB-OPQ7lsM_D1ASlAxwYGISOso2gbqn8wQrrJJzSW8d5BTHVx9cGuRLu4oUR9Kzk6xvKxnUiE9K6brlxA0-0bczowaqNxilVV1J-7xv1QAOmYYEdDDpPOEJzLBiKPK0DGWMkOYPsB64ZUQFTzWWBT8gLb1YyPwnA6Jcnhh46cN82tFyqBLAYUfswCE-uTRvvA-Zvkcc6pVHhTKkjx3OkqK9VBVYh_AiOdBKv_aYWGbpVINoKUuayvgmn_mpOF9_gGDFnPlPUK_N--J3blG-Xy7-lWVnSyC_PwXfZdIUlEV-wkZwwNChIC20q-xQ4bX9-I6aqbgm_GY2TB7uma7o1ObkSBLhwXAmRhqiFzmpgKN_r3VVGNVKHrcEq9e8v5ZsooeuRzGicCbASrJeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور گراهام : به متحدان عرب ما می‌گم، باید به ترامپ کمک کنید
🔴
اگر هم بهش نه بگید، مسئولیت و خطرش با خودتونه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123232" target="_blank">📅 12:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123231">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
خبرگزاری روسی اینترفاکس روز چهارشنبه مدعی شد که روسیه و طالبان در جریان نشست بین‌المللی امنیتی در مسکو توافقنامه‌ای برای همکاری‌های نظامی و فنی امضا کردند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123231" target="_blank">📅 11:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123230">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وزارت دفاع چین درباره وضعیت خاورمیانه: گفتگو و مذاکره تنها راه حل بحران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/123230" target="_blank">📅 11:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123229">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
کایا کالاس، مسئول سیاست خارجی اتحادیه اروپا: بازگشت به جنگ به نفع هیچکس نیست!
🔴
«آنها [آمریکا و ایران] در حال حاضر در این منطقه بسیار خطرناک بین جنگ و صلح قرار دارند، و ادامه این جنگ به نفع هیچکس نیست.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/123229" target="_blank">📅 11:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123228">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
آکسیوس به نقل از مقام ارشد امریکایی مدعی شد: ایران چهار پهپاد حمله‌ای یک‌طرفه را به سمت یک ناو نیروی دریایی آمریکا و یک کشتی تجاری پرتاب کرد
🔴
نیروهای آمریکایی این پهپادها را رهگیری کردند و همچنین یک واحد پرتاب پهپاد ایرانی دیگر را روی زمین قبل از اینکه بتواند شلیک کند، هدف قرار دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/123228" target="_blank">📅 11:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123227">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDmorTdUnt3K_f5b6bUn8vDX95fa0tnGyiiqKC6I80zv3Y1uPoOdCFwpWfVZ67pSn5rC5pD03GQqkFTwPXLm2CFEhHuA06pzqmF2BAK9bpNnE4kNuz5jF9lloPeYQ804c92LB1qQkKhKsCNammdpd2Vvzo-On5tOV-wD8HK8fD0Ak6i4Zd2qlyH1rd65Y9QYf_6YPxJYyNW1w2qWWvv2vzJ6IvVtr4kBDI8NNWoSj11c1BlSOdzimcmERqQYXsqIf2rnQp-OPWMTm15FQWzaCRQGcyQvr-4CvW4s53KWewjCPRum_wQhZ2uanwt_7_pwX5gOloh9T0eDXHPn-wmn_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
املت هم لاکچری شد
!
🔴
قیمت یه «املت» به ۵۰۰ هزار تومن رسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/123227" target="_blank">📅 11:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123226">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
قیمت بیت‌کوین امروز با کاهش ۳.۵۳ درصدی به ۷۳,۳۰۸ دلار و اتریوم با کاهش ۴.۴۴ درصدی به ۱,۹۹۱ دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/123226" target="_blank">📅 11:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123225">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
قیمت دلار آزاد امروز با کاهش، به ۱۷۲ هزار و ۵۰۰ تومان رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/123225" target="_blank">📅 11:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123224">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrvYmlWtVVqIQn3wQhUoWFjyXRVQJDu6DJycNp_F2ukhxhTtvvbIV_PhcLKMN861MGMrl_gjhOa1ti-vWWk3Uxj84nZpMC7gCmvJcrtG1mtX1fEt_JeC-XIEaDszSd0T83iC7osgYR0OBIbk0qTbMaYiFXSkIXJcxoGcqx_JSZaQi8Tm6kr4yig4QUWqLtIdD1u9q_luhDmzbEZReJ7f9YspsKlScVI9sMlOLiuNl2ZEhdE9bAkI9fFbAgFJdPs6YW2BDKmL1jusoTxQ2ZG__VNRGxc-WRP-vVhDNoLoDd_dhXOGh3e6fSxBOWeZ0Y5vw7tH-n7OeJf9gYEEHuaQfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتور جمهوری‌خواه لیندسی گراهام:
اگر ترامپ به عادی‌سازی روابط بین اسرائیل و عربستان سعودی دست یابد، باید جایزه نوبل را به جایزه ترامپ تغییر دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/123224" target="_blank">📅 11:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123223">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
پوتین در جریان وضعیت نیروگاه هسته‌ای بوشهر قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/123223" target="_blank">📅 10:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123222">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
علی باقری کنی، معاون دبیر شورای عالی امنیت ملی: پیگیر آزادسازی تمام دارایی‌های مسدودشده ایران در آمریکا هستیم؛ این دارایی‌ها باید بدون قید و شرط به کشور بازگردانده شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/123222" target="_blank">📅 10:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123221">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgNMBauOBmyBubMnVvzzQAah_B6dBYnU4C-3HuNBisF7zjKtFVshsKcRNYmxJ7bjIYgr0Cg6_29erl0oL82r7V_jExdaeNEwg4THeN7jJn7e2fA5QO6K-gyAGHlNdOR9wNbsdxgiuaNBDqvRjs4yA1m6bWtPy8BZhUjPv_y4UITtQxTF0wmEGf0J2h-6nFFnKHpVDeBtTDqriSF3UUhc2bShyH7SgG9ZHhpOPiEEd6r_Kq7pu7ehwmaNy5qjLjGhKe3-a1AzbEOauLR8uB9CbO22FP2ktRYjBfSbLbQQyGK2q9WvcxXQh5GxVqeZT9BngTbgrcvQCLTBULIm0_0dEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازار عجیب معاوضه گوسفند و سیم کارت با خودرو در ایران / مبادله کالا با کالا راه افتاد!
🔴
بازار خودرو ایران حالا وارد فاز عجیب و جدیدی شده است
🔴
اگر سری به فضای مجازی بزنید با تبلیغات مختلف معاوضه سیم کارت و یا حتی گوسفند با خودرو مواجه می‌شوید.
🔴
به عنوان مثال فردی یک سیم کارت ۹۱۲ کد یک را با خودرویی تا ۱.۵ میلیارد تومان برای معاوضه آگهی کرده است.
🔴
از طرفی معاوضه گوسفند با خودرو هم به شدت مشاهده می‌شود و به عنوان نمونه فردی ۱۰ تا ۱۵ گوسفند را برای معاوضه با خودرو گذاشته است.
🔴
آنطور که به نظر می‌رسد حالا با افزایش قیمت‌ها شاهد مبادله‌های کالا با کالا به خصوص در زمینه خودرو هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/123221" target="_blank">📅 10:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123220">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی: جنگ خاورمیانه، استراتژی‌های ملی انرژی را تغییر داده است
🔴
آژانس بین‌المللی انرژی اعلام کرد: جنگ خاورمیانه، کشورها را به سمت باز کردن مسیرهای جدید تأمین و روی آوردن به منابع داخلی برای غلبه بر بزرگترین بحران انرژی جهان سوق می‌دهد.
🔴
فاتح بیرول، مدیر اجرایی آژانس بین‌المللی انرژی، گفت: «ما در بحبوحه بزرگترین بحران امنیت انرژی هستیم که جهان تاکنون با آن روبرو بوده است – و من معتقدم که این امر، استراتژی‌های سرمایه‌گذاری در سطح جهان را تغییر خواهد داد، که مشابه تغییرات عمده‌ای است که جهان انرژی پس از شوک‌های نفتی دهه ۱۹۷۰ شاهد آن بود.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/123220" target="_blank">📅 10:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123219">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
فردا آخرین مهلت ثبت نام کنکور
🔴
مهلت ثبت‌نام داوطلبان آزمون سراسری سال ۱۴۰۵ دانشگاه‌ها و موسسات آموزش عالی و همچنین آزمون پذیرش دانشجو معلم در دانشگاه‌های فرهنگیان و تربیت دبیر شهید رجایی فردا هشتم خرداد پایان می‌یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123219" target="_blank">📅 10:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123218">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b34e26c9.mp4?token=RDGFXVjVnfnho4b7xsyNCZhaU2kmcqZxKfCSsUeTR-KXKAPp7a1DBVxsf4LSHOVxW1xaZm2q_bUOwjcJD3_sFU7VT759lJIfuybvI4bp5YJOtEzlKiWb3763SE3RLszqT1lTDeq1fR6hGOO6uQ7i6KadhUcBYnKJ5Fja9gF8bVTrDWQNSGPBqr-CstnrqKLFsj5XSSGez27w58Uh31qTyO0YhkyKbSDJqZdApjDzVpWnIQ0P_n3RZ8qLw4EqotM_7sMIc_K0wtFn65XlqEzHvwSuxUt0OmROcj0P5gcED43dkNseE6TH06BV_CmLtaVzcUv02tnh3Tmq8Mgdeoc8qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b34e26c9.mp4?token=RDGFXVjVnfnho4b7xsyNCZhaU2kmcqZxKfCSsUeTR-KXKAPp7a1DBVxsf4LSHOVxW1xaZm2q_bUOwjcJD3_sFU7VT759lJIfuybvI4bp5YJOtEzlKiWb3763SE3RLszqT1lTDeq1fR6hGOO6uQ7i6KadhUcBYnKJ5Fja9gF8bVTrDWQNSGPBqr-CstnrqKLFsj5XSSGez27w58Uh31qTyO0YhkyKbSDJqZdApjDzVpWnIQ0P_n3RZ8qLw4EqotM_7sMIc_K0wtFn65XlqEzHvwSuxUt0OmROcj0P5gcED43dkNseE6TH06BV_CmLtaVzcUv02tnh3Tmq8Mgdeoc8qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت شهر صور بعد از حملات سنگین اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/123218" target="_blank">📅 10:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123217">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚀
مصرف بالا؟ حجم‌خوری زیاد؟ اینو ببین
👇
💎
همراه با ساب یعنی مصرف بهینه‌تر و تجربه بهتر
⚡️
🚀
سرعت عالی پایدار برای استفاده روزانه و بلند مدت
😍
😍
@NetAazaadBot @NetAazaadBot
😍
آف فقط برای امشب
😍
❌
گیگی 50T
❌
✅
فقط گیگی 25T
✅
@NetAazaadBot  @NetAazaadBot
🔥
یه…</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/123217" target="_blank">📅 10:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123216">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cNF_b-345_nTcILlf46WY3G-OVnrJ7roYd7fVsYjnMS1nuJVI80OgTnPFZxmpHrM6ysMFmPWN_6LA8miNeR9povaYI0qhMkjXZ7IM-Hcyi08ZjYcWgrf23Qw894gf3DWDftHIXp__tfYpkaX4-FN5SJF9NqKTyqJVn8vBtK7_OlJRuittiBZXsgqSaeY5Hku8q-uXYTqNWQYyueReMu2GOxervFz4L1iDYTIOcSbdoerWXEd4YyvsZxupqr6r_3HTJNfzRy0GDN_QNnK1rOhid1JvwaPmLmhURFpB9iokv23X0gkNulwbhWi7cf_E4At8-7_7j8OfoRJa34IQV9XPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مصرف بالا؟ حجم‌خوری زیاد؟ اینو ببین
👇
💎
همراه با ساب
یعنی مصرف بهینه‌تر و تجربه بهتر
⚡️
🚀
سرعت عالی پایدار برای استفاده روزانه و بلند مدت
😍
😍
@NetAazaadBot
@NetAazaadBot
😍
آف فقط برای امشب
😍
❌
گیگی 50T
❌
✅
فقط
گیگی 25T
✅
@NetAazaadBot
@NetAazaadBot
🔥
یه بار امتحان کن، خودت تفاوتشو حس می‌کنی
✅</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/123216" target="_blank">📅 10:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123215">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mTTXI-kf6_ehP2yzimcoywC0MUpPUdAnReRhuNb94udoxHmiR8z6FCQPMsBNva16ARwBKSSivvvcOY8emNjzlAe5VKArBKrBEPlmTRoe_o0Us-CPZlq4n5U4yL7xpuEk3mRQHi6pXNOll_dEI0-fGRRJeE4770mqRb50ev6vSQOa_SQ8nNNnqlfJzh8BMVRodXyMYuNczyMcsEEsHawkdxB9o_Fu2Dj_yYkZ_RzcbERSCutqUp5xqEOm1l6rNfLsAohftHaDGknM-hO3pIGO0kE8jeQGRJhqEtkcN8UjqeKbnP8bz5Sy2oUAGOwi0LzNpdobd8g59H7bJT8f7mFlGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان ملل متحد اسرائیل را به فهرست سیاه مرتکبان خشونت جنسی در جنگ اضافه کرد
🔴
این لیست اکنون شامل اسرائیل، حماس و داعش است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/123215" target="_blank">📅 10:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123214">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
اتحادیه اروپا: همه به دلیل بسته شدن تنگه هرمز هزینه سنگینی می‌پردازند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/123214" target="_blank">📅 10:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123213">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
افزایش دما در کل کشور
🔴
هواشناسی اعلام کرد: امروز و فردا دما در تمام نقاط کشور افزایش پیدا خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/123213" target="_blank">📅 09:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123212">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-_zETzzft3SysGrvZJnHpxLzfx_y28P3AI8f8Gy0T-lJV5_eWymKasQEqPXgQ6xzFVJ3KbM0O8-YU79nIOLpWxfIQuCVqV0QNmzBuKMABizMUhniafoF_YSsvvEwsUfI5fxgKE1EnSXnAIc7SywUxABy0KFFwfguJJ-uj9NFg1X246lLSwhQd0RK4Ody_iPvDMBJtkbCKNAYyl4GsgJn4_EuIE7TKorGP0t59cO7gXkzx_t7N_IwxJUwLmD5aA4gsfeR9Rvg2vtueAG12wjE62IbIQLkNpxoEnHMcen_qzvU0SbYQ8dn21u_oSt7_GTv88ygp-10hRcJl5y8H87NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی دقایقی پیش حملات هوایی در شهر نبطیه، جنوب لبنان انجام دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/123212" target="_blank">📅 09:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123211">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
رویترز: قطعی اینترنت ایران، طولانی‌ترین قطعی اینترنت در تاریخ معاصر جهان بود و زندگی میلیون‌ها نفر را تحت تأثیر قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/123211" target="_blank">📅 09:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123210">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل گزارش می‌دهد که فردا دور جدیدی از مذاکرات بین سفیران اسرائیل و لبنان در آمریکا آغاز خواهد شد و این بار در ساختمان پنتاگون خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/123210" target="_blank">📅 09:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123209">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad5a7a9116.mp4?token=RQk82VJk9Yy3oo_JnbOYUuI_6qiY1xMWPK35fVCWScP4ycB0KTnqUEcALm9IbKcDXkbLoXksrOPirMpKJkiCwhWFpjmtO4k3Bdin50Lv4A5cpBsu7LaynHSdtw9i-qtv1kwc9njSQ9_U_nQ4Cp2aAnKl1focQbsSSJ4B3KGQ_Bhv2D9wRbRdYTatBdbnCyv0s1mrh7K7LLKP6sZFiR6dWxtPGrBe9BNOwiI6qc8r1UXNCTmuup4bNFmBKM73y4yNlROXGlnnSovQlcPNOlail1FRAa6QVmKnBNHHh3q_9o0aO9lCIjgdcb8GfBTsI3BfYrtqNXBQMwQ4kTYDErix2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad5a7a9116.mp4?token=RQk82VJk9Yy3oo_JnbOYUuI_6qiY1xMWPK35fVCWScP4ycB0KTnqUEcALm9IbKcDXkbLoXksrOPirMpKJkiCwhWFpjmtO4k3Bdin50Lv4A5cpBsu7LaynHSdtw9i-qtv1kwc9njSQ9_U_nQ4Cp2aAnKl1focQbsSSJ4B3KGQ_Bhv2D9wRbRdYTatBdbnCyv0s1mrh7K7LLKP6sZFiR6dWxtPGrBe9BNOwiI6qc8r1UXNCTmuup4bNFmBKM73y4yNlROXGlnnSovQlcPNOlail1FRAa6QVmKnBNHHh3q_9o0aO9lCIjgdcb8GfBTsI3BfYrtqNXBQMwQ4kTYDErix2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم‌اکنون - وضعیت تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/123209" target="_blank">📅 09:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123208">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
فوری / پولیتیکو: تجهیزات لازم برای حمله نظامی به کوبا تکمیل شده و تنها چیز باقی‌مانده دستور ترامپ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/123208" target="_blank">📅 09:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123207">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
رویترز از عبور سه تانکر نفت از تنگه هرمز بعد از خاموش کردن ردیاب خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/123207" target="_blank">📅 09:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123206">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل گزارش داد که ۱۵ فروند پهپاد انتحاری از لبنان در ۲۴ ساعت گذشته به شمال اسرائیل نفوذ کرده و تأکید کرد که ۵ فروند از آنها در نزدیکی مواضع نظامی اسرائیل منفجر شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/123206" target="_blank">📅 09:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123205">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c882b2806.mp4?token=JAuDjk1vNxaZ29jUMhUjy0Srq7fDQXQ6GH2lBsNYkcyOVa8oCDtSjI6ya7ga9M4i-77jTUlgB6_K7P2Z9bBk6zjR89HS1XY217EI86np2EIy-rYrymM0lHSTvxGNFOy8Z62wuKCMtyiY_h1_NHZhQD8SdkDqqY6lYTIi9sau_Td1hK-cxApwOsZhCzPJplZYasV9iTCJvI0SHvn77xk6kHlUS-BH654n6_2EEQE7CmKk6kBD3FjdmVC-IS_z4Dr85e6CyPUhCuWrKgeJT9nptOZdIuMgOiL1IEgSsxlFBgL88An2WopZ5_-80Bqt6uDEIgdB_ngjbsG1-e286H_Hmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c882b2806.mp4?token=JAuDjk1vNxaZ29jUMhUjy0Srq7fDQXQ6GH2lBsNYkcyOVa8oCDtSjI6ya7ga9M4i-77jTUlgB6_K7P2Z9bBk6zjR89HS1XY217EI86np2EIy-rYrymM0lHSTvxGNFOy8Z62wuKCMtyiY_h1_NHZhQD8SdkDqqY6lYTIi9sau_Td1hK-cxApwOsZhCzPJplZYasV9iTCJvI0SHvn77xk6kHlUS-BH654n6_2EEQE7CmKk6kBD3FjdmVC-IS_z4Dr85e6CyPUhCuWrKgeJT9nptOZdIuMgOiL1IEgSsxlFBgL88An2WopZ5_-80Bqt6uDEIgdB_ngjbsG1-e286H_Hmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جیل بایدن گفت که نگران بود جو بایدن در حین مناظره پربحث ۲۰۲۴ خود علیه ترامپ «در حال سکته کردن» باشد.
🔴
در مصاحبه‌ای با سی‌بی‌اس نیوز، او گفت که «هرگز جو را پیش از این یا پس از آن به این شکل ندیده است» و از عملکرد او «ترسیده بود».
‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/123205" target="_blank">📅 09:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123204">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
اورسولا فون درلاین رئیس کمیسیون اروپا ضمن تاکید بر حمایت کامل اتحادیه اروپا از اوکراین، از کمک نظامی ۲۸ میلیارد و ۳۰۰ میلیون یورویی این اتحادیه به کی‌یف خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/123204" target="_blank">📅 08:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123203">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رسانه‌های لبنانی از تداوم حملات اسرائیل به لبنان و حمله به شهرک «الغسانیه» در جنوب این کشور خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/123203" target="_blank">📅 08:55 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
