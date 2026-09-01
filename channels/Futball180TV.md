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
<img src="https://cdn5.telesco.pe/file/fIG_5VExzUQQAmoxnmEfo8a0FUp6HI_KBf7L3h6-IpMBO_EynZip0hItmUlUcSmUsLtPicqcxg1ZYcgfpu42bs-Sh50OGPnrA8gY46AoCpdetsw2dtULYun7D8BQzh1CtQ022xcn3FyzP66BuaJDtkE2IyXNgo0_ahKOxh8NHJvKdTs1nT21xDnoV1hx-CxprK9T-tA_sce86jwN46MKO-uvhqoqGz87DXYGWXe5jBEP3Yxg5ZHlgr3HgjbVJG9WFnbc0B3ezCwPuiawcCkPI79c4oMRT9G8rS6PmXMrHL6Wiaw9iTgUZBJPZ_md-QKUKC7s4ASB2msdi33YhQYYfw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 432K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 19:17:59</div>
<hr>

<div class="tg-post" id="msg-105281">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ep68WtputvOLQKNgMleraEHooJ0GVEL7DBD6VHhGv1zD0ympnnadbmcvQRoVhRPCV0rfwvVl2c8gCds-zzyTIBKHMQMoee74nVC3ftQUBxMeRaSWHmkF4okbE9jNLAHjrtMzol0MqpfE4ZMUfKi_7cfpoNTqglEmmSHE3JS-lQtpCG7xCQ5OCXrLy0ZTm6lG70Z_0CCM3279WGHxLL1XMMtyvrAp1Qyh9VObJLpWgOw2aDGpG3baqxpSkdHiBnfKjSAkRirvAZPE7voW6UCGgCQuM3xLMOJnZximrpyLNlCbenTO6yWo5hhTFvhheiDGj-ku-x8p9wY215XqbgoFow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از دیمارزیو: منچسترسیتی و چلسی به توافق نهایی برای انزو فرناندز دست یافتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/105281" target="_blank">📅 19:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105280">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33c4f0d2a1.mp4?token=Ck_lC1AnkTeegvyYrlbhAxL4nJNa9ywGunk66NRGIwUKHUW1v1sxnpjsrQ4gvoV4V-YYx2V7hbAHWA3REXHUwYSVigR2zGGNJwiA7GVdB5fbl1JrHZiyN1QlKCpueYQce9MHsX4TnigmnIlRxbUZkbIHYGm1ztnbCXxVkSLoyK3EadNvndrLVTzphoyXEzYK6cDE6eFuuhXz4OfH2nudajBMfP_CR254WlP3eMbbaV6Vl0IV_A-DS_rDL2DTKbLq6FBDdZ5yYY4SJ61AiP4FMQNQ14PwfOgz9idw0hGPJq0v5lGJvX1qmet52wp7CxExegHRN3YHnjRmr-MYSJmcOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33c4f0d2a1.mp4?token=Ck_lC1AnkTeegvyYrlbhAxL4nJNa9ywGunk66NRGIwUKHUW1v1sxnpjsrQ4gvoV4V-YYx2V7hbAHWA3REXHUwYSVigR2zGGNJwiA7GVdB5fbl1JrHZiyN1QlKCpueYQce9MHsX4TnigmnIlRxbUZkbIHYGm1ztnbCXxVkSLoyK3EadNvndrLVTzphoyXEzYK6cDE6eFuuhXz4OfH2nudajBMfP_CR254WlP3eMbbaV6Vl0IV_A-DS_rDL2DTKbLq6FBDdZ5yYY4SJ61AiP4FMQNQ14PwfOgz9idw0hGPJq0v5lGJvX1qmet52wp7CxExegHRN3YHnjRmr-MYSJmcOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
🇮🇷
هوادار پرسپولیس در آستانه دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/Futball180TV/105280" target="_blank">📅 19:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105279">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ei-co9DRurwACPPZLvz5I4JIdJdmp-Aoc2TlSt69tB_YIu45aojRjplEkiVkRT3S8_UcUcCKb1M13EID286qWUhdiNERKlCwpE0Ex65ExDKjgdOPJLe2dbgxr_XY8j8Cvac8C053gMmkfMK6kCWHA2t32heE3tc1pNXB5PkjRIWUgLFs_ZrNh4WC4kB6COi65rBNJ19AcxHJS4zyv2q0mXPWoZNn-OFy0rKOriM0gSDtGwJLyKT8kzAuVUnS9PL58S-jN2Zuy4425gl0THkbjwqUDwyykviVq8drS3mbVKMbFyEyWY6m7twTWgao2-kfTBaaz4CWFfkCJdieRAW61A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
پوستر باشگاه‌استقلال برای دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/Futball180TV/105279" target="_blank">📅 18:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105278">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07cf132574.mp4?token=G3bpoDAPE7nbUJYmWfsqPjvrrZsnGRY0z1jTbelG3AWmPzShmxkDBWkG28FBmhxr6ghjbEc-Iqwm7P0d5u0oH1kfL04BMZwh7A2nlzddeZGLV5qBavmIvuMIzvM9WlpJ8Z-m9lwxcaCw2Y0MmzMmi__qtY9ibR0x3QNJ6XI5djkeGq84dxPIVt0_dVeNcHyeL9p88-FR6asJaByN0dfCiv8dkssPfrbN9mlGxO_rr6kC0W3qAmHYb8fwJ3Nh0QPapOiHLc7RGsBIi9jMkpo3EMlwfxO69yZEcWp7oXfywtD6FgULdBYoWKu9_6eHRtJx89S3UB_V-HX6sYJDCsBo-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07cf132574.mp4?token=G3bpoDAPE7nbUJYmWfsqPjvrrZsnGRY0z1jTbelG3AWmPzShmxkDBWkG28FBmhxr6ghjbEc-Iqwm7P0d5u0oH1kfL04BMZwh7A2nlzddeZGLV5qBavmIvuMIzvM9WlpJ8Z-m9lwxcaCw2Y0MmzMmi__qtY9ibR0x3QNJ6XI5djkeGq84dxPIVt0_dVeNcHyeL9p88-FR6asJaByN0dfCiv8dkssPfrbN9mlGxO_rr6kC0W3qAmHYb8fwJ3Nh0QPapOiHLc7RGsBIi9jMkpo3EMlwfxO69yZEcWp7oXfywtD6FgULdBYoWKu9_6eHRtJx89S3UB_V-HX6sYJDCsBo-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
⚽️
تحلیل‌گر شبکه‌‌ورزش کشور عراق: یحیی‌گل‌محمدی تمرکزی روی تیمش دهوک نداره و معتقدم میخواد به لیگ‌ایران و سپاهان اصفهان بره!
📊
یحیی در چهار بازی ابتدایی فصل لیگ‌عراق موفق به کسب برد نشده و هر ۴ بازی رو مساوی گرفته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/Futball180TV/105278" target="_blank">📅 18:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105277">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guPZup19PF0Zwh8ryaUIQ9984gYgjsWIorWCFtunM335sUmAR5CbGJ3Hjf7_apsGGIg7xvtVbi-iQjZT7Zcaf_40a6vGxG6MlyvTuxnpv-rHZ911DpiuGmKJo0oO0xXmpj5zk5ss-lMEnQEy4jz_RgNKNB2ywZnc2bXuVdHuBVWcSHjQTHXDzfPK3B3OimO3wFLph6lthuaPOeo3yXgcGo2Ptq9syXl4jQaxOgSh6ZrOTpmI6_JHjIBJCsOR7wNwSs2OkILIzuApvgT65pvTiFDQPfN-R1Orbp9F-YosFLP2gJxuvLRMLTPhU3fqRNw0oH2VMVMC8ugRFp01cmLAVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیب تراکتور تبریز مقابل شمس‌آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/Futball180TV/105277" target="_blank">📅 18:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105276">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7b5a30f12.mp4?token=XHk3_408Imdbun2KdhuF68dShHRoG5bZs7TRBVdwy0AIuBU-Kz9zBxyxHfyr2A9QLrPrQ-IxX6QkpQVsdIfbBS3r-AvMCOLKVv_8_9XcCc3IjudWp9YLfHt-7BM2EBlqYSlKalKreLbkizLtvzI9o6-XI8udRG49rs89SqsA1mW9bqbi3njoQDwkcT00UMssR_wApI7COnRRqI4bTY8NlgILIP8Ss4hom-L6FmZrrL2OXMM9SonvxpQo2skdUw-GfrwjypRrMXuHCK_5ipSMwkfAavuuAOy8cKGSPzS1zaDRV3Kd92P8_ExHb3m7cvIuKEAiTL9Ay1W8_VpvNqxKHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7b5a30f12.mp4?token=XHk3_408Imdbun2KdhuF68dShHRoG5bZs7TRBVdwy0AIuBU-Kz9zBxyxHfyr2A9QLrPrQ-IxX6QkpQVsdIfbBS3r-AvMCOLKVv_8_9XcCc3IjudWp9YLfHt-7BM2EBlqYSlKalKreLbkizLtvzI9o6-XI8udRG49rs89SqsA1mW9bqbi3njoQDwkcT00UMssR_wApI7COnRRqI4bTY8NlgILIP8Ss4hom-L6FmZrrL2OXMM9SonvxpQo2skdUw-GfrwjypRrMXuHCK_5ipSMwkfAavuuAOy8cKGSPzS1zaDRV3Kd92P8_ExHb3m7cvIuKEAiTL9Ay1W8_VpvNqxKHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان‌چالش ترند این‌روزهای فضای‌مجازی
😂
❤️‍🩹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/Futball180TV/105276" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105275">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105275" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/Futball180TV/105275" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105274">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRp58W9o8CtofwGTSMvAnhu1boa8YoNKl06f3hWODBw-l6k_96JQY2hAyzSD2U2o3apSaReKTy0vlFk2FcUpBxbn9PAMeSeiYrQFpm512X_GwPp3qnDX5xPfGvpRGApl2TcI3KoYDB-aFYSBy4qu789T6E3wF7jJc8nwKd11vq3tLZBMjDAVMllNkOnpCXJyvswDHgVAeCfWxiOCUTo3xFUCJNQqJlJCvZv96tkNOiJluj_ay7pP8ivI7t50SwHzHJGBFHbMRUIArr8gWNbOr1u00JPuwMOmuHo93v6EV-9E0M7GVVQIHtMiPL12o8c51fiGPZQejOc6k7Wl-wfCtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/Futball180TV/105274" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105273">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9737ed01b1.mp4?token=oaf4q2WeIRRf96mvCabdZKyE5bAcAdh3ydrzIU_RciNxYFp0rBgYlEseGVy4YLVC9jrrTxcOOQnkuT5pKntbYgRhhfp3IqSC4yPfLYg7wyucJQTd_zxR1CPyotvUxPAwZ8h4SCpO726QOcyNw3zJ6eChhmVfGo8CEP39KXO-jF4e76_9effm3KMBXz2o_q9zOJ1furEMQ569vDOUp1-ogSYE8ikntkCxMl7aG4-KcgG8jEECIZhyAWipq7kiYknddEU_VmX49ASNRYBwX_V5KOAH9zWDf546JWtBQdI6M4942H5oFRT_qYYdqDgpxhbfbb8o1npMF3BJPPSMX8Xp9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9737ed01b1.mp4?token=oaf4q2WeIRRf96mvCabdZKyE5bAcAdh3ydrzIU_RciNxYFp0rBgYlEseGVy4YLVC9jrrTxcOOQnkuT5pKntbYgRhhfp3IqSC4yPfLYg7wyucJQTd_zxR1CPyotvUxPAwZ8h4SCpO726QOcyNw3zJ6eChhmVfGo8CEP39KXO-jF4e76_9effm3KMBXz2o_q9zOJ1furEMQ569vDOUp1-ogSYE8ikntkCxMl7aG4-KcgG8jEECIZhyAWipq7kiYknddEU_VmX49ASNRYBwX_V5KOAH9zWDf546JWtBQdI6M4942H5oFRT_qYYdqDgpxhbfbb8o1npMF3BJPPSMX8Xp9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⭕️
پلیس‌فتا در واکنش به صحبت‌های دیشب: به پرونده پیام صادقیان قطعا رسیدگی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/105273" target="_blank">📅 17:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105272">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/273bbacf0c.mp4?token=QBohqEPMlhZxn3LXsrH7-zfr1OpY6rO_cF0F_qNQwUdRco-m4F0zN3PTvI9ZxtTlq4sRvkdUguCuXvAgZCT3DX96Iq25W9Vyo4igCnDHLXQOHIqdIkFDLAMDnineNCB90jGs-45BjrjZs8dtbF7efmNA4r_jk5lcsqyHw0Fj4Vm2HvzjU0JM02c4A2iBj9ChYbtpq5e1U_46xEYaGEWCuM0MdDjlrp-2vNi554ffdqoB0dbAExfT7kK4UMqR0qM72mJC_fVzo7mE1avNTBbwouVhpbc87hOQlDP5YnsndlXrsVCO2aeT1RWf-uD5niQEDS3twFdXXEVRyrWpNfo-Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/273bbacf0c.mp4?token=QBohqEPMlhZxn3LXsrH7-zfr1OpY6rO_cF0F_qNQwUdRco-m4F0zN3PTvI9ZxtTlq4sRvkdUguCuXvAgZCT3DX96Iq25W9Vyo4igCnDHLXQOHIqdIkFDLAMDnineNCB90jGs-45BjrjZs8dtbF7efmNA4r_jk5lcsqyHw0Fj4Vm2HvzjU0JM02c4A2iBj9ChYbtpq5e1U_46xEYaGEWCuM0MdDjlrp-2vNi554ffdqoB0dbAExfT7kK4UMqR0qM72mJC_fVzo7mE1avNTBbwouVhpbc87hOQlDP5YnsndlXrsVCO2aeT1RWf-uD5niQEDS3twFdXXEVRyrWpNfo-Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
تیم‌نروژ با قرار گرفتن در رده ۱۲ فیفا، بهترین رتبه سالیان اخیر خودشو کسب کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/Futball180TV/105272" target="_blank">📅 17:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105271">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb1b930efe.mp4?token=hqEeACaU2M2pwoUb51T-UjA0_8rk2Kf08RS10cfTp9m_X6i4ostCTUTQnHB7-p5MeG5aXrgCfsUkesVNbJD_1pOxf8VrP7KDVfUhTkXWPdk0HbLAHTQOeeoubeKO_kkiGiV0Gemrz96TFjuCgDjJ3D7dG3mp-H-Tbaov5xmnOUl2HB3jTRUelfJ4xkQ2u9LEOflEfmBdZg6J3flIXJklBoe8vowx4AcnECL0pT7T8KsxKOPgxBX10mPdrw8UJvB9joJ4ZYzFjXaCkoJaAWkoM4h8YvgLaPE8igvePOd_l53T9cmHV_ZHi2xbD7xZETGc-xDPps_nnf6OST6tul4kXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb1b930efe.mp4?token=hqEeACaU2M2pwoUb51T-UjA0_8rk2Kf08RS10cfTp9m_X6i4ostCTUTQnHB7-p5MeG5aXrgCfsUkesVNbJD_1pOxf8VrP7KDVfUhTkXWPdk0HbLAHTQOeeoubeKO_kkiGiV0Gemrz96TFjuCgDjJ3D7dG3mp-H-Tbaov5xmnOUl2HB3jTRUelfJ4xkQ2u9LEOflEfmBdZg6J3flIXJklBoe8vowx4AcnECL0pT7T8KsxKOPgxBX10mPdrw8UJvB9joJ4ZYzFjXaCkoJaAWkoM4h8YvgLaPE8igvePOd_l53T9cmHV_ZHi2xbD7xZETGc-xDPps_nnf6OST6tul4kXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
صحبت‌های هوادار تراکتور پیش از بازی با شمس‌آذر: ممنون از نیازمند و ایری برای گل و پاس‌گل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/Futball180TV/105271" target="_blank">📅 17:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105270">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOV8ROzXCdoV9w6reBmLFv_BHyE8T51Wd44GN8RPtsf1IwisMSN5JXpy8uocECHPSOihP_QpoJ1d_Tm6c1qjOEbwBgjOKs5voTSOGdlxP_JvJQJQLTidCfB3ogKIMOyZ60qcMbkMJbzJXxQ5GBF_XtqFrU9qY9s4ZetyNh24zSJCXt9LbbamHNh7qWwfRQxv-Dc2vXsVCD91fP378oO4VUEhcjRyIMnp9eiCjraWtoyCAGuPGFgd1oxSfys7niV9f9A6Ru_Xkn4q2Nr3kW4cCoPWioY9dnQGeabohuwfG0J1qUiH6V0ssxGvcOt-TvLr4XuY9QELEgkpLFQkwuCnLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تاریخ اولین ال‌کلاسیکو فصل مشخص شد:
‏
📆
• یکشنبه 3 آبان‌ماه
‏
⏰
• ساعت 23:30 به وقت تهران.
‏
⚽️
• ورزشگاه اسپاتیفای نیوکمپ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/Futball180TV/105270" target="_blank">📅 17:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105269">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx6DTASKio92OEZ6Txd4w6o_7Gtxjg3rgVwvnkog01f36F1LBktBn84BuTrcy9Ruxm5U5V9EeIJS3BKyCCPUHuqQXIiViE_KfAt7RHtQJsTRPlB_eocUE7dR7368Xi5t5WNsGERdUqy0az5U6SbeNI2J6SMhGgTKF5Z828jf66XgqYNiDiZ4t2keKF6cK3Zwumc0E8kQyBe2ursF71IzFuqaY03CDZHozO5X1re_J6NFCzGL-MU0v1cWRAIjr_pHxi8-EZRNM4dP6evNreBeHWNyNhcPsB3S_AG8woRNE5PP78oZDlgWhIVQn3dHZRX1Bzr5swG2DPw0EU2Dsk1v6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
🇪🇸
🇪🇸
مقایسه عملکرد هانسی‌فلیک و مورینیو در تاریخ الکلاسیکو فوتبال اسپانیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/105269" target="_blank">📅 16:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105268">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHZlpwwXx7EXlnRmN92erbuxTgExf4gr-CjOoLBhQKr3VS82EVGNa9N8YWQKvlYIxLZOFchZkx_FFIM8nuXAKokj45gqju5gt1r_2_k3YQ0xcmHgH2VHbuYI3VWR9Gbuvvh-jlShfGE8pLxc7Ac7yGcizdo_uwsfzz12wFNK_j0PokSoujlHdli9Gk50znXV9sWXV7yqQIdep3eI4xYd3cb8_eKhaBcjzYjnyvounaBd_sjYsrlAhm055dv1x-0O3ZjqaRpmxi6e4uUBwMN20EtT4_V-B1xGNIFnnPDAQAJUFvdeMtgAaSiwr5auDMy5sUyw1vttgAOpgKRR5JuOUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
💥
در آخرین ماه از تابستون یه نگاهی بندازیم به بهترین فیلم‌ها از سال 2000 تا به الان که اگر فرصت دارید در این اوضاع شخمی مملکت نگاه کنید. سیو کنید بدردتون میخوره
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/105268" target="_blank">📅 16:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105267">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dfdcc87e9.mp4?token=n1eKTd0KqE47ZGFHhKm-trM7N0j8BqPJNqdR6qnmBs8hcppojdGO8wDgAjtmN_lm7RHOqZ0ZA5Gi0cyg2uyVtUalpBvMgccRwAyWbhrBYjknIokYqpMd0ECsbzMAcKhpXLN0S1YPJehxKRSGEm8vfOZ9DsvYdIeyNTZmERQr7oRZ8eiaaGYhwWvWJidVDO8ikqdJP5eivLOQ4JgQp_bxKD2S-xVSgTmNExVQ6Vn5vj8GgGtT2XvNGBRuy0Utd-gK8pWkEyPtJrjobA2vtkwl0AkTlfPTCjCPlDYmeXPCHKOpShP12AeT40z2Fq8ANhNQOxJ38PaWjYiH1JJ4lRK6cRtdDNkCiaHP2UcPdnRLCv5rNBq9VKNuawFsLwndXD7-ZRy9d97nsRALwxpUrqmn6eYbCrbrp-D3w87caqJ22xOnlziMxSRqSklGkoeYDXXa2kRlzJH6wbsJtiZqEmHxwWTMPmn7ltLQANSQv_OZAG1NPLMHn0f1nPON83IGEG7rNkDSiYNvTXC5N_j1Z6opiZGYpz6NzNWoQAE_rspnxpQp0gxMOc7uinK6U_dMWfHkpURBsLGws8_vC2tcrH_xY-heqEAk-Q1TaTlKBxtoljyUmviZmCxWPz2E5bbXrjnhV7PDinBEDUP8_eglli7DVZYz0sLyjW1ly4SJ9EhlXb4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dfdcc87e9.mp4?token=n1eKTd0KqE47ZGFHhKm-trM7N0j8BqPJNqdR6qnmBs8hcppojdGO8wDgAjtmN_lm7RHOqZ0ZA5Gi0cyg2uyVtUalpBvMgccRwAyWbhrBYjknIokYqpMd0ECsbzMAcKhpXLN0S1YPJehxKRSGEm8vfOZ9DsvYdIeyNTZmERQr7oRZ8eiaaGYhwWvWJidVDO8ikqdJP5eivLOQ4JgQp_bxKD2S-xVSgTmNExVQ6Vn5vj8GgGtT2XvNGBRuy0Utd-gK8pWkEyPtJrjobA2vtkwl0AkTlfPTCjCPlDYmeXPCHKOpShP12AeT40z2Fq8ANhNQOxJ38PaWjYiH1JJ4lRK6cRtdDNkCiaHP2UcPdnRLCv5rNBq9VKNuawFsLwndXD7-ZRy9d97nsRALwxpUrqmn6eYbCrbrp-D3w87caqJ22xOnlziMxSRqSklGkoeYDXXa2kRlzJH6wbsJtiZqEmHxwWTMPmn7ltLQANSQv_OZAG1NPLMHn0f1nPON83IGEG7rNkDSiYNvTXC5N_j1Z6opiZGYpz6NzNWoQAE_rspnxpQp0gxMOc7uinK6U_dMWfHkpURBsLGws8_vC2tcrH_xY-heqEAk-Q1TaTlKBxtoljyUmviZmCxWPz2E5bbXrjnhV7PDinBEDUP8_eglli7DVZYz0sLyjW1ly4SJ9EhlXb4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ربات وزنه‌بردار چینی وسط مسابقات جهانی وزنه‌ خودشو رو میز داور ول داد
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/105267" target="_blank">📅 16:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105266">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b94f1ee2b.mp4?token=fBS8SMeBWcDCE6THSpMUeBpJkDRqlTkiKoOvBKyTY0cQ-kTy490n6mpHk8vBSCj1kGXRQMwD6PCTFB8gUJM32IyWttMh5H18XiwOJurydO3DzjvUsR83hRmpcf3LvsNxd-LkR_TlIj-51TV5y1czHKDhKSGBLIbI6hAqHa0x2ANw5rP4JCl-5vQSbDVoiBt_K3cPoWaOm4FXJeWVmSqmwcwDW2zWs2iCYAQ1oGybBvQvJih_V-9ggxtpgotQHWh63MTJJjJx3XKd08w7I2tx30LBPzYysFv8zLHkFGfDFt4oFrUwoWTxgdGrv2vQEhsS5MLK4ZnUguAcK7pt98EG5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b94f1ee2b.mp4?token=fBS8SMeBWcDCE6THSpMUeBpJkDRqlTkiKoOvBKyTY0cQ-kTy490n6mpHk8vBSCj1kGXRQMwD6PCTFB8gUJM32IyWttMh5H18XiwOJurydO3DzjvUsR83hRmpcf3LvsNxd-LkR_TlIj-51TV5y1czHKDhKSGBLIbI6hAqHa0x2ANw5rP4JCl-5vQSbDVoiBt_K3cPoWaOm4FXJeWVmSqmwcwDW2zWs2iCYAQ1oGybBvQvJih_V-9ggxtpgotQHWh63MTJJjJx3XKd08w7I2tx30LBPzYysFv8zLHkFGfDFt4oFrUwoWTxgdGrv2vQEhsS5MLK4ZnUguAcK7pt98EG5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
پیتر کراوچ در سال ۲۰۰۵ فکر می‌کرد بالاخره مخ یک دختر اسپانیایی زیبا در هتل را زده؛ اما جیمی کاراگر خیلی زود فهمید این «دختر اسپانیایی» کیست!
🗣️
کاراگر همه‌چیز را جلوی هم‌تیمی‌ها تعریف کرد و کراوچ تازه فهمید دختری که به او علاقه‌مند شده، همسر ژابی آلونسو بوده!
🙂
کراوچ سال‌ها بعد در پادکست گری نویل این ماجرا را تأیید کرد: «فکر می‌کردم به خاطر جذابیتم از من خوشش اومده!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/105266" target="_blank">📅 15:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105264">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38daf6a490.mp4?token=Zt8xZbLC6TrlgdYgBKIIwYG5ZERQl3BbU0OMlYuNeLmzua-H26z1Jz17eb3x2431vxuruIjLMD4DbN1GSvWJ-KfcCVRqD0a_UTbOHJ6TK20YVzO17HU9nwbNFLLauqamhKGJ71GMWEWwvdq7V58o-y3WfgT73tY5C6BnOIhY7rLefYGWds8nP4ilKKMZlYOcs1MRQNV0cDPWkE-9K4VtN1dQ7ebx5LDAvnTyvG9FTTmWMVhbjGeFI4pT-PSQc6YSy3-ZEZsEDdEwYgqOTnL5yhSPX_s7UMxHbf7M-rsfLipoJMFS86aUMs1cOeIOzQCjB7T0WRgVIfjdF90mUunfRYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38daf6a490.mp4?token=Zt8xZbLC6TrlgdYgBKIIwYG5ZERQl3BbU0OMlYuNeLmzua-H26z1Jz17eb3x2431vxuruIjLMD4DbN1GSvWJ-KfcCVRqD0a_UTbOHJ6TK20YVzO17HU9nwbNFLLauqamhKGJ71GMWEWwvdq7V58o-y3WfgT73tY5C6BnOIhY7rLefYGWds8nP4ilKKMZlYOcs1MRQNV0cDPWkE-9K4VtN1dQ7ebx5LDAvnTyvG9FTTmWMVhbjGeFI4pT-PSQc6YSy3-ZEZsEDdEwYgqOTnL5yhSPX_s7UMxHbf7M-rsfLipoJMFS86aUMs1cOeIOzQCjB7T0WRgVIfjdF90mUunfRYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
⚠️
واکنش عادل‌فردوسی‌پور به حرکات منشوری شجاع خلیل‌زاده و عارف حاجی‌عیدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/105264" target="_blank">📅 15:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105263">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e1a906213.mp4?token=cFo54OXtBSx4xZuVo_XzfJEBdcWQiYTmGc4UycDhwPVxoX2F_gAZV1DkuQNmxoTSmzXF2j6KXN_tNin4XJ1yCMuo9pzDjmk2X55ux_tZjTqzg6SxfXA_2S78jktF7YrT91WW-e4pDRv-EyFodx21TeJlO4YbdRF40iZm0ly4Ndf7dc6TW9univBgLRP5lQsxj4UDM_K_7YLg1T-cMkKNd-SfZ0x7SBWeoRBkUjj69OTeFbXadx7YswhvFPk_yHhGz_IbLLUYc0aHbN0VT0IGCpT4hqfr8lXJJz3ZN7YPjlpOkiBkRGpqJWxvEfJ__RrxGrWrCHC-zNT10QPBbEdrlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e1a906213.mp4?token=cFo54OXtBSx4xZuVo_XzfJEBdcWQiYTmGc4UycDhwPVxoX2F_gAZV1DkuQNmxoTSmzXF2j6KXN_tNin4XJ1yCMuo9pzDjmk2X55ux_tZjTqzg6SxfXA_2S78jktF7YrT91WW-e4pDRv-EyFodx21TeJlO4YbdRF40iZm0ly4Ndf7dc6TW9univBgLRP5lQsxj4UDM_K_7YLg1T-cMkKNd-SfZ0x7SBWeoRBkUjj69OTeFbXadx7YswhvFPk_yHhGz_IbLLUYc0aHbN0VT0IGCpT4hqfr8lXJJz3ZN7YPjlpOkiBkRGpqJWxvEfJ__RrxGrWrCHC-zNT10QPBbEdrlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای دخترای جنوبِ ایران
🫶🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/105263" target="_blank">📅 15:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105262">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7EF8RGYBG539V4ZDMhcofGPxUeRoKK0A3cEXqctF989f-xxt2XXNqusb69o_HYLUjkXQIIt7t2cd5_GNvjbFYXYNjG5vbfUTuOy1rjf-B_4vZSOswH9GnZejMfnrDGdVJigOv-MbzRsHP4B7nEXTnvgmOMFOExkha9Obb2dzvMkA8b901py-cwIOlW2qtXykEbw6YinTcFmzGpqW0Brf-NhjPmpAN2WtEWPZ4TfAyy55meCizxgDv4xyC5jyPrngV9RPWjEAQQ2J7WK7ubrRmypbEvIjU8EH-TnPYGOGbmSiQGO-cTSuZUO-74NdcCtvzASayJbdf2bKEAGL8MfOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇮🇷
هوادار بانوی تیم‌فوتبال تراکتور تبریز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/105262" target="_blank">📅 14:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105261">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93b254714.mp4?token=qlRrRulvqfLTwHw6xorT4XFvQDlYrco4SO_jCjBL7fsyrZAYzT2YRfvhSDKrYLZyCEXc9J5h8pnESAYcQvWToOtDjtxkxalruV7-8_qOjJ7-W7g9LvF30VYHITNLLcm-ESqc6qWaEhgU1vZB9jjz8ZEAXGwYPDhQmrKNhh7Mm3OOqQzdvTX9rHp0-cCtsxAjWh17C-chJSfrU_OX7uR3PfSizDhjzQt59GItqjmNYwiUfE7UrVhws1FmQsSOfIictZzBR276reMeSlqPpOP1IfUnscdgNoNXj1Tbe_fQDB5S8nJBiriTRcAWL7l8RxSszGNifGqI1qydHuvGCGuTNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93b254714.mp4?token=qlRrRulvqfLTwHw6xorT4XFvQDlYrco4SO_jCjBL7fsyrZAYzT2YRfvhSDKrYLZyCEXc9J5h8pnESAYcQvWToOtDjtxkxalruV7-8_qOjJ7-W7g9LvF30VYHITNLLcm-ESqc6qWaEhgU1vZB9jjz8ZEAXGwYPDhQmrKNhh7Mm3OOqQzdvTX9rHp0-cCtsxAjWh17C-chJSfrU_OX7uR3PfSizDhjzQt59GItqjmNYwiUfE7UrVhws1FmQsSOfIictZzBR276reMeSlqPpOP1IfUnscdgNoNXj1Tbe_fQDB5S8nJBiriTRcAWL7l8RxSszGNifGqI1qydHuvGCGuTNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
بدون‌شرح‌ترین‌ویدیو امروز...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/105261" target="_blank">📅 14:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105260">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411e9bcdcb.mp4?token=NQFFdVXcQqZDeeYUYKS0Pel4fZUuL2pUpynQ9ERhY0GgHciQNMxAz0clePKCOKFdYXnJ7Cg_vuSRJFFJQLNHw_ru3sC7JWPqkPxv1cxx1ZVIVIXQoD1Tkp0tZp1oYQ3XNpqddztMl57-KmpA12bXXGNKmoJ6GOiu_mEqy45W8LS5BZ6JE3wcRkzMxitHSe6SKcYDYm_G4o6DphNWuJQD-IYF-YHCZnyBNyQMhTC8uTbPW8nVxlCr9Piiq-EllexwERqyYJ1mEz-4gMEILDmZV-V5Jj38H5z4Jq10z0CHyEn16C2Y8zj8f41SjOlB8Do7LXhp4gyOh68Rr0yY95_cvbgJt0VSH9ZQTjhE41ZDkM7YkDYTefjOYB0C33EuJCPcPHqyeGsSV7l4hgodVIbUKJWO442RaCJO7cSiFWp-tBOJ5eg0_CzqBjzK1wAek1recfMuiJz2uvcSmtIXXX5EFQwRx972wbq5LELNL0_I69Yt4ZJ45vRoN7Xi7ru-pG0yMjFYSzBIWoyRe414C-dWodqgSzd71S3REboZfyrkh2XK6FBcLkReykQ3MEj-53c9Z_kg3AZs9gEtIJ7mY_w0rlgTptlvwPynccbx5bOH7wvJb49WhRvcFB1lSrt43AXx8q29-ZJNVJhka4kfW6zlK6QiWI10qW44CEHncYUj_v8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411e9bcdcb.mp4?token=NQFFdVXcQqZDeeYUYKS0Pel4fZUuL2pUpynQ9ERhY0GgHciQNMxAz0clePKCOKFdYXnJ7Cg_vuSRJFFJQLNHw_ru3sC7JWPqkPxv1cxx1ZVIVIXQoD1Tkp0tZp1oYQ3XNpqddztMl57-KmpA12bXXGNKmoJ6GOiu_mEqy45W8LS5BZ6JE3wcRkzMxitHSe6SKcYDYm_G4o6DphNWuJQD-IYF-YHCZnyBNyQMhTC8uTbPW8nVxlCr9Piiq-EllexwERqyYJ1mEz-4gMEILDmZV-V5Jj38H5z4Jq10z0CHyEn16C2Y8zj8f41SjOlB8Do7LXhp4gyOh68Rr0yY95_cvbgJt0VSH9ZQTjhE41ZDkM7YkDYTefjOYB0C33EuJCPcPHqyeGsSV7l4hgodVIbUKJWO442RaCJO7cSiFWp-tBOJ5eg0_CzqBjzK1wAek1recfMuiJz2uvcSmtIXXX5EFQwRx972wbq5LELNL0_I69Yt4ZJ45vRoN7Xi7ru-pG0yMjFYSzBIWoyRe414C-dWodqgSzd71S3REboZfyrkh2XK6FBcLkReykQ3MEj-53c9Z_kg3AZs9gEtIJ7mY_w0rlgTptlvwPynccbx5bOH7wvJb49WhRvcFB1lSrt43AXx8q29-ZJNVJhka4kfW6zlK6QiWI10qW44CEHncYUj_v8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇪🇸
دیشب‌کریم‌آدیمی بنده‌خدا فکر کرد چون ۱۰ دقیقه تو زمین بازی کرده دیگه بعد بازی نباید تمرین کنه که دستیار فلیک این‌شکلی کاسه‌کوزشو میشکنه و دور تا دور نیوکمپ کنار نفرات ذخیره تمرینش میده
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105260" target="_blank">📅 14:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105259">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c284d93a.mp4?token=lTzcNW0RLaL7KGyy31c0cQ-YskdQ14X4Nu-GG7lMtvYJdHvN-6OV0aTpf6CyD0FlruH0S7atxdfQ9pto1gzzGKNI-DHPokvhVvcWT8QvMxuCFyK8oNjg7j-hfTNR89WNlf2-vQ1QzlsYVfnIp7x33z-YaEZ9V3cIWD62kgOXP-96-W3YnV0-WDMBBO9xbArwNz155yG5lVlfIVFeodgFF1Yaqeo_xI8THNesjqNVLlH0es-kjgy8P0YOhRaDMIq_InmmXxDgHzp-60cnwNyMPHV_y6dTZgDulGHcKoWRuT55MIRQZDCsTVImJx0-7ENW6T_Npji8YQK0UPlH5O31SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c284d93a.mp4?token=lTzcNW0RLaL7KGyy31c0cQ-YskdQ14X4Nu-GG7lMtvYJdHvN-6OV0aTpf6CyD0FlruH0S7atxdfQ9pto1gzzGKNI-DHPokvhVvcWT8QvMxuCFyK8oNjg7j-hfTNR89WNlf2-vQ1QzlsYVfnIp7x33z-YaEZ9V3cIWD62kgOXP-96-W3YnV0-WDMBBO9xbArwNz155yG5lVlfIVFeodgFF1Yaqeo_xI8THNesjqNVLlH0es-kjgy8P0YOhRaDMIq_InmmXxDgHzp-60cnwNyMPHV_y6dTZgDulGHcKoWRuT55MIRQZDCsTVImJx0-7ENW6T_Npji8YQK0UPlH5O31SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
عملکرد پشم‌ریزون دیشب لامین‌یامال برای بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105259" target="_blank">📅 13:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105258">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4862134a1c.mp4?token=BcyMTYFotNJc5B8KInKakHPahpEZv7azpNKip1JCI4m5c92mF4NC0yJ_SxJ3-KYNYU_XcWPWLkBoXTKrKEyNgbkl7D14IblYTG7zVEr-gLNxj5euBVEXEisZOnOJt67jnSIFVpy7NkSQTqYum_dWjVdjs0f5U0l0kfiquttE8A0L_oLpLbktWUlB3Y6vzBz7NrmCiByfP8cmslD_M0MCx0vjEIioLiumDDVoLXR1FvpQO1iP5MT2NDgBuW8Yd5Zxk4ut5ygz92fV8rn0atbCooOEjV0Aq4ieVMKsUcfVLK67cF8_ZZaS5TvgMAX5pPPbCunhC-lxcnCRMlAflVczIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4862134a1c.mp4?token=BcyMTYFotNJc5B8KInKakHPahpEZv7azpNKip1JCI4m5c92mF4NC0yJ_SxJ3-KYNYU_XcWPWLkBoXTKrKEyNgbkl7D14IblYTG7zVEr-gLNxj5euBVEXEisZOnOJt67jnSIFVpy7NkSQTqYum_dWjVdjs0f5U0l0kfiquttE8A0L_oLpLbktWUlB3Y6vzBz7NrmCiByfP8cmslD_M0MCx0vjEIioLiumDDVoLXR1FvpQO1iP5MT2NDgBuW8Yd5Zxk4ut5ygz92fV8rn0atbCooOEjV0Aq4ieVMKsUcfVLK67cF8_ZZaS5TvgMAX5pPPbCunhC-lxcnCRMlAflVczIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
محسن نامجو مرتیکه دلقک در کنسرت نیویورک، شانزده شهریور سال ۱۳۹۲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105258" target="_blank">📅 12:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105257">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از دیمارزیو: منچسترسیتی و چلسی به توافق نهایی برای انزو فرناندز دست یافتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105257" target="_blank">📅 12:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105256">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/950b2c8673.mp4?token=Ud7fBZuPkbwvfiqQ3Cfw4XbHiV4icC9GsKua8_lH1CY8M_BjcSqQP7in2JFdhwaRQYmukYHmYnBm-U0mDT0rE7hrSKIl9lO0NZyZ1b_xNVIvlnEbjTdnMjHGu6eABTW0NjN18Xw6EJj4ppOL7vrTCR5yyz356l8UY5ra4VGv2_R0Z9TLlrr1ZPHD9pJSK5HjzanbHraUTqBLc-ZYZ-VE215lkAnzMHNbgYYnVHDqge49b_P_6NVG-rUymWgazIxTTYcMDZSNtTWFUwgKog_3L2wEP7MfmUwBnHESPrCt9ZA4iswcFXUyybb2fWLbxhmuVYpfqGqJTpFNq3v6AJm1KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/950b2c8673.mp4?token=Ud7fBZuPkbwvfiqQ3Cfw4XbHiV4icC9GsKua8_lH1CY8M_BjcSqQP7in2JFdhwaRQYmukYHmYnBm-U0mDT0rE7hrSKIl9lO0NZyZ1b_xNVIvlnEbjTdnMjHGu6eABTW0NjN18Xw6EJj4ppOL7vrTCR5yyz356l8UY5ra4VGv2_R0Z9TLlrr1ZPHD9pJSK5HjzanbHraUTqBLc-ZYZ-VE215lkAnzMHNbgYYnVHDqge49b_P_6NVG-rUymWgazIxTTYcMDZSNtTWFUwgKog_3L2wEP7MfmUwBnHESPrCt9ZA4iswcFXUyybb2fWLbxhmuVYpfqGqJTpFNq3v6AJm1KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
مجتبی‌پوربخش: تا جایی که اطلاع دارم، وضعیت جسمی علی‌کریمی خوب است، فشاری بر او وجود ندارد و صفحه شخصی‌اش نیز در اختیار خودش است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105256" target="_blank">📅 12:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105255">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FO5lvoocKsaOWTMW4BlPVzaQp--lfW3AUEAsz4zrT_jkXyPtQl--Uv-EKAqMCJtVl7ONivow1ppLo8XOoAHOmtkIyUKdfcbnspWeMqDgm761Riuz_bc4_IGvI00VkBbw5pOwiYqc_JaVbYiGUSm90fNa3mDBGs6bTQyjXnYFQCeEPmc1I7D27gH3ecR-ftlGMx9fQVETtZw0E_UFInirGATuTaCLOlWOvAQvYQVJ6RaNMagmrx1VxYTTbvneLXVbj0kvv-8emQi4JobQ56lkY1GQGEzdtPf-0JFaNgdFaXm6OKj2Mf5XRuaZdXFTt8OVnn8tvBBVnCsu0RC4AfB1Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
نتایج سه‌بازی ابتدایی بارسا و رئال در لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105255" target="_blank">📅 12:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105254">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f53a6fd8f.mp4?token=QLhNuwLz0A1woN9A5zGDjm8jG7o8GbQAUYz0yyZVBdEemi6GKZlurhYpQEUe4lxbXF5iH9NNpxJVPXW81zQVp-1LZqvhoeo584vA8Pu9sgacBo9JxvomPOJaGXSHfFW5STbT6AS03dIrzSzSOp7hEEgZVYgxZtJGoMOS8r-wU8NRti6SlfLIxtAeCkYLPo0UGQfJRpJIxVOcjpVYsI-GX93xgTC28mgBw_CbO0BTozfVOifQRpGvvgHqNs5tmygvpVESReuRbN5Ta-msILi3NcSVFvcd4NBAdV-3gO3194mqfX0hSL6GNo2vqGoxqCpIJUg2AqE6fodCMipxzCy-dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f53a6fd8f.mp4?token=QLhNuwLz0A1woN9A5zGDjm8jG7o8GbQAUYz0yyZVBdEemi6GKZlurhYpQEUe4lxbXF5iH9NNpxJVPXW81zQVp-1LZqvhoeo584vA8Pu9sgacBo9JxvomPOJaGXSHfFW5STbT6AS03dIrzSzSOp7hEEgZVYgxZtJGoMOS8r-wU8NRti6SlfLIxtAeCkYLPo0UGQfJRpJIxVOcjpVYsI-GX93xgTC28mgBw_CbO0BTozfVOifQRpGvvgHqNs5tmygvpVESReuRbN5Ta-msILi3NcSVFvcd4NBAdV-3gO3194mqfX0hSL6GNo2vqGoxqCpIJUg2AqE6fodCMipxzCy-dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
ویدیو زیبای و دیدنی حمید سحری پس از اعلام خبر خداحافظی اسطوره لیونل‌مسی از تیم‌ آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105254" target="_blank">📅 11:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105253">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105253" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105253" target="_blank">📅 11:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105252">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWOGMLd9UDiPZGjz96-gGIAz8Jf4Wt3Yw5alThThtcCpDzeeyuBuzXSDcLx2TvJPnrKgoorxYrrpGwjgzTwBx3rYuSlY2KepXVrQtHTG879bQCKxf6vV_N2qeoAI8k0S2yFGL2svsuyZHrSNBgdzSfcWn8WPGLCFVDdTBBos2FLVwOwFT2VGawCu-9PpuVbITV9dZPhXsU_3jNfEs6fkfUsKwCm8XygTrnj9KvV7XPTuF3P3kn-TWp8rCVEpF3rCUXS4TIRY7EEoM9IscfR-6_YKwWxcFN0Bf4GSNeYtmnp4_0v6G_2ECuXNcVb6be7KAzedi6n_fEyiv-ce0FaCSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش بینی کنید.
مونزا
🆚
تورینو
دورتموند
🆚
هامبورگ
کرمونزه
🆚
پارما
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105252" target="_blank">📅 11:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105251">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f62060bab.mp4?token=vndbNLIWpfOBJLSi6PSPFcQ5HjVx3Q6KCkFcNNTCLCvLShX8Bg9Qakf2QMZxYZnN5wkyVMgXFjhdz1VGV6OtcNnuWqiNKnB2AWIOqe8F7UDAhLJMXgcXxcIXG-gYcjzejM5rjRWpMa_FB_CwPc5I6rccshC02Lo1yK5YAK7-VI5sAvAcL9q5hWfpOo7_lenO-eXuWqvJkb3xpl5HuhKQ1UsY1N16hwGoP-t0jvnHhOX6bx3YcsFdMA7sdY9s6zrOE-v2u42aRnOv47AHKhC1dPlDms2lctk_eOPzQ-ICbGAw_6T2PCvYVXfV5i2MlScuQNkanU9BNNxeiqRUDPz0Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f62060bab.mp4?token=vndbNLIWpfOBJLSi6PSPFcQ5HjVx3Q6KCkFcNNTCLCvLShX8Bg9Qakf2QMZxYZnN5wkyVMgXFjhdz1VGV6OtcNnuWqiNKnB2AWIOqe8F7UDAhLJMXgcXxcIXG-gYcjzejM5rjRWpMa_FB_CwPc5I6rccshC02Lo1yK5YAK7-VI5sAvAcL9q5hWfpOo7_lenO-eXuWqvJkb3xpl5HuhKQ1UsY1N16hwGoP-t0jvnHhOX6bx3YcsFdMA7sdY9s6zrOE-v2u42aRnOv47AHKhC1dPlDms2lctk_eOPzQ-ICbGAw_6T2PCvYVXfV5i2MlScuQNkanU9BNNxeiqRUDPz0Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
🇮🇷
فرشید باقری: خداروشکر به پرسپولیس نرفتم؛ آبم با آنها تو یک جوی نمی‌رود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105251" target="_blank">📅 11:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105250">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbad291eb3.mp4?token=cvan_DkkGY0mcTxe709n95ZIcWN34fV5MRbDBFDsC2TTaR9JQSmrEzjwFpSFYY6oitclb_A2uk5u_ogHfF7VKL6VMY3WlJb5uY_AZzasHalmbSCTnRwqr7s-PUyxVxnTXkwpfnMjR1PgESjjgNyw5C03zmlh8DPvTWunBq8wrcJybSaPmMjRPYyesILlQ2PfzZQ_0E0rF8EaSqWxOaO6sC7JloDxxLMANI_5qiJwCPcTJh9Yt0PeCnl53W3xOn1wKnAq8yqwZmrQbmqIkfgYpQrTZHqlmOJy1RlMtnBXrn7iKQuYEpgaRs_aklZDWe9tox8nz8bg07oq0IF2Q7CT3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbad291eb3.mp4?token=cvan_DkkGY0mcTxe709n95ZIcWN34fV5MRbDBFDsC2TTaR9JQSmrEzjwFpSFYY6oitclb_A2uk5u_ogHfF7VKL6VMY3WlJb5uY_AZzasHalmbSCTnRwqr7s-PUyxVxnTXkwpfnMjR1PgESjjgNyw5C03zmlh8DPvTWunBq8wrcJybSaPmMjRPYyesILlQ2PfzZQ_0E0rF8EaSqWxOaO6sC7JloDxxLMANI_5qiJwCPcTJh9Yt0PeCnl53W3xOn1wKnAq8yqwZmrQbmqIkfgYpQrTZHqlmOJy1RlMtnBXrn7iKQuYEpgaRs_aklZDWe9tox8nz8bg07oq0IF2Q7CT3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
🏴󠁧󠁢󠁥󠁮󠁧󠁿
وضعیت سخت‌افزاری ورزشگاه اولدترافورد که وسط بازی از سقف ورزشگاه آب میچکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105250" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105249">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtfeWEUrJJnzvNR5q3S9ET88mwzSt-YzULrf5W5P7cmIKmhlQ45kKsz8skxzzVMI9d_MgQeIevgGnpXxnBzHrJB5U64lxsEf_545MyENjrRQipSYUL-_B8YNlCDvDemK1BN17PIZUg4DJNInnRwSFlvbKRNVDtP3YTxSQ5mYFIRvq1mnXkVPIEZrKA3EoN9Q5pwx-jlcEMfkEJ14H46um9-hYhoBb2dcLL9s_LpxCV1DCko_xcnQeyNwzIAz11HeFwyoF--tjWSLyfX9qOCSLYOA6kkyA7kZD8jKsPsyWqjcoK7vvudCxFYvSp_qjPyieGm_ol1ZiJgmzuOmK-_pGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
پوستر باشگاه‌استقلال برای دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105249" target="_blank">📅 10:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105248">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a276b65ea.mp4?token=VyfXx0USHqt_ElmT2MRryV1NY03AWFBd6B9TPCJzBQwxdANTWAYOc9nneGnzYNcOc3erU6RfFVylA4PxKZHs9YxECKsW4T82pC3QLC2K0JFIrg6-dw5-rM_dXqzyLkihHqYp9ASjI8qFIoCInGc_OBKxIP1hRMtlXrTIFraoIh3lfCI_7T5feBir9Lnsp37ca4tvPDazU2V0ET2SWgKa97j9XRL9AF8KY56KZds96JE5jl4tXSd4_RQp_xx6c2OnfZXg-jW1S5CgdcXj_vC1pHbwq1se2BfuOfwGp9Z9DP-wqzHp9nID27v5t_DFeGRMExVJhuQsvRVAxukJxRWVtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a276b65ea.mp4?token=VyfXx0USHqt_ElmT2MRryV1NY03AWFBd6B9TPCJzBQwxdANTWAYOc9nneGnzYNcOc3erU6RfFVylA4PxKZHs9YxECKsW4T82pC3QLC2K0JFIrg6-dw5-rM_dXqzyLkihHqYp9ASjI8qFIoCInGc_OBKxIP1hRMtlXrTIFraoIh3lfCI_7T5feBir9Lnsp37ca4tvPDazU2V0ET2SWgKa97j9XRL9AF8KY56KZds96JE5jl4tXSd4_RQp_xx6c2OnfZXg-jW1S5CgdcXj_vC1pHbwq1se2BfuOfwGp9Z9DP-wqzHp9nID27v5t_DFeGRMExVJhuQsvRVAxukJxRWVtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
افشاگری شب‌گذشته داشعلی‌منصوریان از فساد شدید در ساختار فوتبال عراق
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105248" target="_blank">📅 10:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105247">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2QzBB3BDRcVen-rONxt_dDOx5vZA0JTrQsTShvea55D4sC5K3l90_5lQfQZkli_WNYu39Liwj4jS6tDcVcmiR3iHD4FkUXhH71frrq8oHCkBhy5E429XgBVR0mQ1CZCN_S3Q2utwlVqbgzjzdHWNJP23_bBz0c3ul1Ymusk-anp2Ze5wFqDjKzN-In1h1rqXS_lTZEX4NBARX6s_TDtNTqpAmjgUYVcVvOMcRRDEDtfuAcx-o6N_aQNv0c9U5uHnRYgbfEsDalKzJaEfWuJznu74LHHNlkX18oWaYI0Tf89vh8yrvdbr4YTS6-nMekW16elqfs1WjjfZWbbHGRQTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
با حکم کمیته انضباطی، شکایت دو تیم سپاهان و مس‌شهربابک از استقلال بابت بازی غیرقانونی یاسر‌آسانی مردود شد و این بازیکن مشکلی برای همراهی استقلال ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105247" target="_blank">📅 10:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105246">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1b1a2663.mp4?token=PWfqKnKQPH9NAyaE0d_rCUaBTFcQps2i8s84vG40TQ9N7K1Lg5EePpG2riMdSLwvC7e-OYx7wejMs8bdWl7yw_XNImEdsrvS9JEinHZMclU7-xfDODTERaYpdodDqYpdUo_Bp79_-rD8uoY0P-8QZ1WpQK59-wQUhUQn8Z8wIeQcFaid92hYzpB1zOBVDzTrXRIPztFxMTcTu5w232x8lxBIhsi3ljJwZOObKnXdapUlfPmQQfxN8PRdJNyFpS1A3WNdjdyhkpkolfQscbc-wNdebGW_1QTOIc17NOnb6wXISIUBln3-L8rjxYKAol5YEPSSxUQFjxZzDMgNGO7cjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1b1a2663.mp4?token=PWfqKnKQPH9NAyaE0d_rCUaBTFcQps2i8s84vG40TQ9N7K1Lg5EePpG2riMdSLwvC7e-OYx7wejMs8bdWl7yw_XNImEdsrvS9JEinHZMclU7-xfDODTERaYpdodDqYpdUo_Bp79_-rD8uoY0P-8QZ1WpQK59-wQUhUQn8Z8wIeQcFaid92hYzpB1zOBVDzTrXRIPztFxMTcTu5w232x8lxBIhsi3ljJwZOObKnXdapUlfPmQQfxN8PRdJNyFpS1A3WNdjdyhkpkolfQscbc-wNdebGW_1QTOIc17NOnb6wXISIUBln3-L8rjxYKAol5YEPSSxUQFjxZzDMgNGO7cjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🙂
‼️
عمو رشید دهن سرویس درکی از دیدن برنامه با خانواده نداره
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105246" target="_blank">📅 09:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105245">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31f95056c4.mp4?token=Kf5rmhcw-3paetwTCIjAXotP3D8vNb2GH06UelpWIwL8VhNoTjcCX-fKxpjbBrrBfCFAa50i9tN1IIyS5iWKcxJNmrHc0Fv7DQW_YaVieei4kcfAOpm1VMfLvUHQXhNxUAm5JwFfgpOBQTaq9azdaougW-ch68KpG6t8wRhuuDGCoI3cHOm0TiA-j738IhMbv_hRJuP1NVUugAR44MGTfSyFeBf7G290TqRNAM6bqOxkqGSbCK0bZ0Um_XcfB6NxqrAKl5wtuwpixENg2-qGrmn1W7gW-PxZlL9OmZUyM8emR4L01CXw-k5FK_x6o1xxVwafJaUsbsdoXzl6ccAjAUnM1y4PE9dmICx5SqK_qv5RRCEezVWD1dYDOyh_qbWNFCNtQ_mrmMeyfyO9DbSxwRYYZ2uD3hQ5Pxj8DUDdfE8FvgYH0G_9bBa4WscEKomQuDXxBIvNDpSyYuwUj0Dh-E-fHSpJB_Kt3oi-2xE33G6ziXyUBuXygyz3f8THM-OttUn-79lgIy9-QWqjESkMrNuhVk6imBd_fF9yOPZdABMB7xMaY3ReJz2WsW6qLaqOMydQ34gHcVuhhZANT1SWlesdZ-2RFEi0a3THd_IaAFBU0wjR22WbcZVbvmkWrp_s4OdV7QeP_teU97IvWlUBVQiLlPfAeGSvsXQFMrAySIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31f95056c4.mp4?token=Kf5rmhcw-3paetwTCIjAXotP3D8vNb2GH06UelpWIwL8VhNoTjcCX-fKxpjbBrrBfCFAa50i9tN1IIyS5iWKcxJNmrHc0Fv7DQW_YaVieei4kcfAOpm1VMfLvUHQXhNxUAm5JwFfgpOBQTaq9azdaougW-ch68KpG6t8wRhuuDGCoI3cHOm0TiA-j738IhMbv_hRJuP1NVUugAR44MGTfSyFeBf7G290TqRNAM6bqOxkqGSbCK0bZ0Um_XcfB6NxqrAKl5wtuwpixENg2-qGrmn1W7gW-PxZlL9OmZUyM8emR4L01CXw-k5FK_x6o1xxVwafJaUsbsdoXzl6ccAjAUnM1y4PE9dmICx5SqK_qv5RRCEezVWD1dYDOyh_qbWNFCNtQ_mrmMeyfyO9DbSxwRYYZ2uD3hQ5Pxj8DUDdfE8FvgYH0G_9bBa4WscEKomQuDXxBIvNDpSyYuwUj0Dh-E-fHSpJB_Kt3oi-2xE33G6ziXyUBuXygyz3f8THM-OttUn-79lgIy9-QWqjESkMrNuhVk6imBd_fF9yOPZdABMB7xMaY3ReJz2WsW6qLaqOMydQ34gHcVuhhZANT1SWlesdZ-2RFEi0a3THd_IaAFBU0wjR22WbcZVbvmkWrp_s4OdV7QeP_teU97IvWlUBVQiLlPfAeGSvsXQFMrAySIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚪️
افشاگری پشم‌ریزون عادل فردوسی‌پور از ریخت و پاش چند صد هزار یورویی مسئولان تیم‌ملی جوانان و امید در اردوی ترکیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105245" target="_blank">📅 09:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105244">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b5c71afe0.mp4?token=aNEK7cDOmWn3maJtzE2sxbdWO17nWYxLmhll9QnRSypvczYKw1TIqnj8HYH9eXEuOSiqfUXR8vW0F4zQMg1HrwMPEO7aBwZjVMGECNRsEyUxls5GjGPpkhQNAhEYoZP8W9Z6F4vUg9IfqssKnCgtSExzXli7YCJ-vnmXNA8SUWEE_XrT4ewAy9tKp5d5McbX61-E2MHbcJfEbikS5lxABUCpjI2iYzTjVLftcbNKeGDR81QNUQhPjF8HCQFyHzxNOv1n17abcPa1MC-qV90tm5ZY_oBhrRR4egZM_mWgM33dHKi2r83TRtO0jEe-cmfelb5UrT1x7HFOiSoKllPcTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b5c71afe0.mp4?token=aNEK7cDOmWn3maJtzE2sxbdWO17nWYxLmhll9QnRSypvczYKw1TIqnj8HYH9eXEuOSiqfUXR8vW0F4zQMg1HrwMPEO7aBwZjVMGECNRsEyUxls5GjGPpkhQNAhEYoZP8W9Z6F4vUg9IfqssKnCgtSExzXli7YCJ-vnmXNA8SUWEE_XrT4ewAy9tKp5d5McbX61-E2MHbcJfEbikS5lxABUCpjI2iYzTjVLftcbNKeGDR81QNUQhPjF8HCQFyHzxNOv1n17abcPa1MC-qV90tm5ZY_oBhrRR4egZM_mWgM33dHKi2r83TRtO0jEe-cmfelb5UrT1x7HFOiSoKllPcTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو خواهر پژمان‌جمشیدی از برادرش در بدو ورود به کشور کانادا پس از رفع مشکل ممنوع‌الخروج بودنش بابت پرونده اتهام به تجاوز !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105244" target="_blank">📅 09:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105242">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fa9c53173.mp4?token=AhWRPtyw2AjTssIvreqSGiIurAmgFtmm6_c2gbWP0INkbHMFe7350LFW56kd_ysiLCttT_BtwBGUIk-Ii1Y81pUncr6uK5yXzcpu61W5crG3YmwQKOZ8guY71LVwxn5dD9QLRgVg6x8HT3fDdAI4AFe9OnPxTkUd87p5LL1Go46WFUvXwlH_dw_C92XxlAvpZvJlHFoq8X93JXuv9_DvVAeFp6M2h82llH5CbT6m6L7KWEzSuiY9X5ZWhEURIgVfosLxvbYbkkTVhSpwaQ-NYrLTWgWFkFfIcDXsG2kHlBxfy6hgl57r-uR_9f3MJhvCgLy3sNCgtdtWCbMZ_qc2eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fa9c53173.mp4?token=AhWRPtyw2AjTssIvreqSGiIurAmgFtmm6_c2gbWP0INkbHMFe7350LFW56kd_ysiLCttT_BtwBGUIk-Ii1Y81pUncr6uK5yXzcpu61W5crG3YmwQKOZ8guY71LVwxn5dD9QLRgVg6x8HT3fDdAI4AFe9OnPxTkUd87p5LL1Go46WFUvXwlH_dw_C92XxlAvpZvJlHFoq8X93JXuv9_DvVAeFp6M2h82llH5CbT6m6L7KWEzSuiY9X5ZWhEURIgVfosLxvbYbkkTVhSpwaQ-NYrLTWgWFkFfIcDXsG2kHlBxfy6hgl57r-uR_9f3MJhvCgLy3sNCgtdtWCbMZ_qc2eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های عادل فردوسی‌پور در اولین برنامه فصل‌جدیدش پس از حواشی فیلتر شدن سایتش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105242" target="_blank">📅 08:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105238">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Apejr14WE6f-GVvDba63IpVKvN2eEeo4wbqwU6Y_L085vy_99bwZMZYKLhwhXsGUfQLmfnbnOTSHwYrxJTobsEXidAcgtaWF4Ag3mfjC6L27bqW1s-IOLAzQg-Emcw6VLcFm2HSyN8ZoX9rRcr0PffubpO16nUAgf0R7PZE4Digjvzyn2DbAhhzGNQ1ogCMOXenlInfxZotfXuIVwuKfC8LY8xjRheFUCzXM7Hazg6Bh1ngm51_zgyJugZS5-2cHee4UwQX86qoNtwbT723-1W5RLjOv3qMg9pMNRq2mZfDoRMGmIc_sU4pP_KBMB539LxwjEN_Xe56gi8rsLRRiBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلیك: 91 پیروزی در 120 مسابقه با بارسا.
🥶
ژاوی: 91 پیروزی در 143 مسابقه
با بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105238" target="_blank">📅 01:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105237">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dn3Haqrc7rfQmf3S_fdEUZjUeIMSdLM38pTzgrrQX6W37lHqKUWCdAwwuKhKTqHzmJ-Mq8wTjeDYXRQrkNybIuf6KwB0dLKeCtmOTchLkWPahkqttiMShv3ZxQtapsHaRzhK_XdyqTtvz5j8RJZZPH0zj4eJIpRG4U63XBpMs6NBW3QL5BJDUm6PorS5i7L6IRVfzJM-JhU1pCeAM3A4CZvwQLsBA0_AP_XuHb1ykYBDM6C7hE-2q8ccyZD-Rzuzvo0bHVn1_mN-ziA19MprZS2TKzFgW2entfFDE8ODAcjjH981uYZ2Pty-96wVB6bu-Jvc9ESDWujJF6Po9708ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: مودریک از چلسی به تاتنهام با قراردادی قرضی HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105237" target="_blank">📅 01:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105236">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKxkKGzA9lDdeo0_aFCVqcDjts8qcXvj1N5A5_p0JmToxyPWwE9loAtOUmf3lz8E1hG4H8nr7r7l72fpLoT4agnLvUh4emtp9v9Skj8dRH8SXegcoNkqNtPbetuQMVNfa86s8OXvx-evLDBvQtgyUZjIf03XgiDZdpXAS2nYe0El3zeHbqrO-Gt6vQ4-efmxSI_X1B6pW-UpcHmvAY2VWC4im486S7stLDxuYdYUZ6zmqETi-X7Z8fUjN1y6-jjsXv7UWI-j4w2nbTUEEH5zWYnadiqJjhFfdQmR_9_kWn9oNfJGo9apWVHDnG4wOlJiboZckqQuu1lYyy_VZe9QHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌سوم لالیگا؛ بلوگرانا روی نوار برد؛ پیروزی پرگل در شب بریس رافینیا و‌ یامال
🇪🇸
بارسلونا
😄
-
😀
رایووایکانو
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105236" target="_blank">📅 01:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105235">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">لامین‌یامال دبل کرددددد</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105235" target="_blank">📅 00:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105234">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بارسا پنجمییییی</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105234" target="_blank">📅 00:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105233">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گگگگگگگگگل</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105233" target="_blank">📅 00:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105232">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شنیده شدن صدای انفجار متعدد در سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105232" target="_blank">📅 00:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105231">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی استون ویلا 0-1 آرسنال با گزارش هوتن خداپرست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105231" target="_blank">📅 00:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105229">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گلگگلگلگل چهارم بارسلونا با دبل رافینیا</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105229" target="_blank">📅 00:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105228">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
‼️
🇮🇷
🎙
توضیحات پیام صادقیان درباره جنجال سایت شرطبندی؛ من اصلا نمی دانستم این سایت چیست و فقط تبلیغ می کردم، تا الان یک بار هم وارد این سایت‌ها نشدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105228" target="_blank">📅 00:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105225">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گلگلگلگلگلگل دوم رایووایکانو</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105225" target="_blank">📅 00:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105224">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گلگلگگلگلگلگ سوم بارسلوناااااا</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105224" target="_blank">📅 00:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105223">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گلگلگگلگلگلگ سوم بارسلوناااااا</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105223" target="_blank">📅 00:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105222">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd706ab6a6.mp4?token=A3EueqBlnKpPbC2oFKpqn6n7sE9x7lxnE8QGtKQZkVBmBmz6aZ4sIgdcisJEFYGtf7CJDfS3ppAK7-FawQrNQjToWlFwvaEe-k3HQLaSqmt8zXdRjJm9grdYZMJesXVpP28PdN1fR3XuoLiwdr8PgALvAr3LUr-wKI4Lx6o_5__np_uwAoNuD95xQ6ljvzuGfiOYY45jMjVbp7E_G3Y25Ytx7QCLNrehA6jxQAtDQDherl0nDZvbNsbtqjcMFHsTDaOXHzm1i_xlClbO4tgKo_6O_0iUyd7_ZeZ7RiBBOXuSu5WpKH0zvUGi7zLzrqfSyZ53J5rhk46GJlPLobKKs2pAxLRoEZasSSFg0Uvbf3OFSvYIhkqCveRlI1gm-WojytMcDP0g0P_LZqeA99BxLEdE8wwtTTBwgiex5mCL3ucefA3RDbpkfFAd3WTpQndNV0Og1FZTRWcSrCxXKkfenmKMlnu_qzVjQFg07ykIMAxA-UWWtYGxnnfVQMX6NaIq7EK2_lKbyQ47ouFgqXQN00RI2NkwzWbjrxmmFxmOC3bwNff3khWYW7k0SQfQbRCFnha6V-uSDvMlZ6jCih7leXHTdP-5senBtGpPSV3SRW46vPpCK0h2HVLZOhX6XNQTDtPVV0X15CYpkXo9vKKAqfPiTq2-LlWDaX5FY_fOT-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd706ab6a6.mp4?token=A3EueqBlnKpPbC2oFKpqn6n7sE9x7lxnE8QGtKQZkVBmBmz6aZ4sIgdcisJEFYGtf7CJDfS3ppAK7-FawQrNQjToWlFwvaEe-k3HQLaSqmt8zXdRjJm9grdYZMJesXVpP28PdN1fR3XuoLiwdr8PgALvAr3LUr-wKI4Lx6o_5__np_uwAoNuD95xQ6ljvzuGfiOYY45jMjVbp7E_G3Y25Ytx7QCLNrehA6jxQAtDQDherl0nDZvbNsbtqjcMFHsTDaOXHzm1i_xlClbO4tgKo_6O_0iUyd7_ZeZ7RiBBOXuSu5WpKH0zvUGi7zLzrqfSyZ53J5rhk46GJlPLobKKs2pAxLRoEZasSSFg0Uvbf3OFSvYIhkqCveRlI1gm-WojytMcDP0g0P_LZqeA99BxLEdE8wwtTTBwgiex5mCL3ucefA3RDbpkfFAd3WTpQndNV0Og1FZTRWcSrCxXKkfenmKMlnu_qzVjQFg07ykIMAxA-UWWtYGxnnfVQMX6NaIq7EK2_lKbyQ47ouFgqXQN00RI2NkwzWbjrxmmFxmOC3bwNff3khWYW7k0SQfQbRCFnha6V-uSDvMlZ6jCih7leXHTdP-5senBtGpPSV3SRW46vPpCK0h2HVLZOhX6XNQTDtPVV0X15CYpkXo9vKKAqfPiTq2-LlWDaX5FY_fOT-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
ادعای بابایی مدیرعامل چادرملو: سه‌جانبه را برگزار کردند تا پرسپولیس آسیایی شود
❌
صحبت‌های علیرضا بابایی، مدیرعامل چادرملو، درباره پرونده جنجالی معرفی نماینده به آسیا/ رانت اطلاعاتی، دلیل گله از گل‌گهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105222" target="_blank">📅 00:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105221">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ou2Gnap5o_xxWojkaqF6DvQRRSImHd3bIa37Zv9gXNFvEcvNsfAFObtnV17k1uuggQO2vyUCx2xXVNJXADuVREg4f31WJQeVTKCsfZQFnnFW726qHP-pc6-teJXOoNvcNJuzjnN-G7YGqJqLaetUr80UHfzWG-bSJJx0oS62zeU1VfCsp5i0IeTjqNzZXMNPoBcR3VG2HhWlekx1UwshF6kZwSliexpS1GAQ53Y01aZ-NvTJPblHIcCJO1FBiYzvwIdo17IFUBWkgqUUenoeDh_c1qVlFxsvQ0TCT-tfpH7WfWIVg5FQpzo0U7G85oiowyuBjtQIBujbevWWVJsTuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
🇮🇷
در نشست امروز کمیته داوران، موعود بنیادی‌فر نظر منتخب اعضای این کمیته بدلیل تجربه بالاتر نسبت به کوپال‌ناظمی بوده و قرار شده قضاوت بازی روز چهارشنبه که حواشی بسیاری خواهد داشت، به بنیادی‌فر واگذار شود تا بازی به درستی مدیریت شود. هنوز تیم داوری رسما…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105221" target="_blank">📅 23:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105218">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گلگگلگلگل دوم بارسلونا لامین‌یامال</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105218" target="_blank">📅 23:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105217">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گلگلگگلگلگلگلگ تساوی بارسلونا</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105217" target="_blank">📅 23:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105215">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گلگلگلگگلگلگلگلگل اول رایووایکانو
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105215" target="_blank">📅 23:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105214">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f1302c5c0.mp4?token=ir32IfUSv3VqlC3qWyR3WCEw96GeHf07cUPwRIc_bkU8fmq8KQBaPVyDuBsgXHStkWq2uDGcHupkf3V-LdW3yZfyAAUZU0jxagUgEku_glKbsc-FLdo-GpCwa0juF3C_3_TNxw78Qm7hLOg43Cm4bSuusL71mfpEB0KLiow18j-2BTwzBLhJUaIu2oUe46TARdVWR5XD6s1n-TMGoLbTCOQUDrn6FsQYz6rMnq5F13HnTCRRXkRSo5pUu16z1ZnXWap5kisLrwt8ukMdB3GKJaML53C_G6QNjzfL3D7CUIuf5SyjmdgqnRA8JF91U7uKkMUE3J8KA_UpzKc0OQkxJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f1302c5c0.mp4?token=ir32IfUSv3VqlC3qWyR3WCEw96GeHf07cUPwRIc_bkU8fmq8KQBaPVyDuBsgXHStkWq2uDGcHupkf3V-LdW3yZfyAAUZU0jxagUgEku_glKbsc-FLdo-GpCwa0juF3C_3_TNxw78Qm7hLOg43Cm4bSuusL71mfpEB0KLiow18j-2BTwzBLhJUaIu2oUe46TARdVWR5XD6s1n-TMGoLbTCOQUDrn6FsQYz6rMnq5F13HnTCRRXkRSo5pUu16z1ZnXWap5kisLrwt8ukMdB3GKJaML53C_G6QNjzfL3D7CUIuf5SyjmdgqnRA8JF91U7uKkMUE3J8KA_UpzKc0OQkxJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
در اولین معاینات پزشکی از مهدی ترابی مشخص شده که این بازیکن دچار پارگی رباط صلیبی شده است! معاینات تکمیلی قرار است امروز انجام شود و نتایج آن اعلام‌خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105214" target="_blank">📅 22:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105213">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇷
مصاحبه‌های منتخب هفته چهارم لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105213" target="_blank">📅 22:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105212">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/782a933b7c.mp4?token=GDWgmUT4kOMCoR7-QCiEctsj0dvbxb7CU2KEez_hD5BZC_mTXkihvNpR4dOg5Cvrrsk7DSbXFISYzfkTF47-rU8Dy29UnFTXaLis89DU_jVSkL_7DFoJlF8tZnB6sao1_8TSg-nTnqimk4_6Wks9wwFvpv8Pfoq4FT3mGVYylZAKmXPd8hM33Zyc84hi7Lp1t2xzeC0BzAYCjKPYii27w3W-VrPC4jUehznyU_rgHYh3iKbm2NBx1Uf0KtJuYQbxHCrru4K5lNstgzxXnOCyWPSqJP8em0lzvJqLp7HthKBWzZOXAF2LW3lQI_29rDPg-WZ_o5FB3S6opt3NOjJ-FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/782a933b7c.mp4?token=GDWgmUT4kOMCoR7-QCiEctsj0dvbxb7CU2KEez_hD5BZC_mTXkihvNpR4dOg5Cvrrsk7DSbXFISYzfkTF47-rU8Dy29UnFTXaLis89DU_jVSkL_7DFoJlF8tZnB6sao1_8TSg-nTnqimk4_6Wks9wwFvpv8Pfoq4FT3mGVYylZAKmXPd8hM33Zyc84hi7Lp1t2xzeC0BzAYCjKPYii27w3W-VrPC4jUehznyU_rgHYh3iKbm2NBx1Uf0KtJuYQbxHCrru4K5lNstgzxXnOCyWPSqJP8em0lzvJqLp7HthKBWzZOXAF2LW3lQI_29rDPg-WZ_o5FB3S6opt3NOjJ-FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لحظاتی با گابریل‌ژسوس خرید جدید بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105212" target="_blank">📅 22:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105211">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XutUiz0TmhuYjLCYjzS6vRHL8UB08yjxGI0Zc9m_Qu8nsIJRQC4XlPcGSeUo2f6JuGZGoBZ9UXLhIukr8aGbNhtLPYNY6nK71B9slQdYGfITKWgfQ9kwK7ngob0rhBmcmSKzqOiVHRim9P9wEIJJY6emRxeIic_1RrOgUVi1brnEAUYKGD5v7FxZMbBNwiPf3C16xf9-84PKq3POh57PWupn1SCWr-Bl0UitPr2-zJ0F3C4jTYPhYxcUEUZPvt1emds2lmTPFCpgk6nOYveKXGnBoaxGtuf41lOapj6jKoGpJChl332zeblX8VYm839YBPTpcuz3m_U6E8VqDM8XmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: ایلمان اندیایه از اورتون به منچسترسیتی؛ HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105211" target="_blank">📅 21:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105210">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-1ZlBy2_K9DefT-Eu9rbg22HBwh0kqJfzEkD4jbMTZ2tjVd3Q_cxvJC7a1otZemJAH8ccn4Azz4oulvWxKi2cDETGtgJ_BJo6B9c280a3Er80qUhNhV4h2KMX1RKSwxeY8d5wncanjZkPC8oNiUothRZfgavyC0ek5dYbOAMlNqbsifc5BnZM7708DV9_mwpKcMWNdfkbrrnaGMMB9jQX1Vgr5IYvINdcJ25-tmxpvDgkcax-eSFEqNHEgg678asUh0rsLxGBjCV8VtnamTBILw77WmVuu9y9vempyXKfCtqGA7JgxBKGgxT3zSBv7-MTXxIr-9NUkkX8NOaArJwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
هفته‌سوم لالیگا؛ شماتیک ترکیب بارسلونا مقابل رایووایکانو؛ ساعت 23
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105210" target="_blank">📅 21:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105209">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4bw-oeva9lNUDvi7y-cGOkg40f8ZvpOc8GZ3o4zvpb0WAR54wKhepF_b1UBIjDPxNn26jkATuYJwKxhaDjHGEKFGFXHWfaRqvcF5ELTqDMfJCx0o3-OjcqPF0-mCcZeBUVoCgWjQbzD2gZoDtSs4AYmpYG8n_Kq9JD1_w8BsyZ6irdtxgnmzutR0jCu6Tct_jR_Vq97wB3WmXfsUx084xkTujjGOtHtyAmZFdMXuWgh_DpkW6g7QFJCKN2ZCHz_CNMkGdshFNal8xEwagmBowkiGxv5bUBdVnDIE7jHDlajmWl6IDRAnAcUHEHtb2PgkkkjJJkuCBU9LpcBrtxIJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
💋
با این ویدیو فوق‌العاده و غم‌انگیز رسانه 433 میتونیم ساعت‌ها گریه کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105209" target="_blank">📅 21:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105208">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGTybvVgcAqFamuxIQuHSG9Fup-lXHgYxNHbgMVRPlZ612bQ-LDDfCNXdVBcIo0TkRUJQqMIGBSwsr6JjKelA0BPun1ab7sz-a0NS9j-zwQYFE5uVs77kb74t8it3CkKMG86rY_EYiJMUL4EWzWtD-Gy34kUkeKQauzcRO6ziFQwb7NmQJyGWEA0R9tPB7VX4mpY7INrgajkVoWGBPq-lLRmhQTZ3Ah6OK_XlXiyW9CXTvVgTaAM5KDX4Oh-FnGnW9Xs5JY_MuM8ytPu0WNM1IXbOy67ozBHRuvb9HpId_ag3Vx3oSTkBSY0SFjp6NPvNrxY9VU-fVwS51gSSel4Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: اولین پیشنهاد تیم منچسترسیتی برای جذب انزو فرناندز به دست‌ چلسی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105208" target="_blank">📅 21:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105207">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJ2H0l76GA6xkCVd9LE_kbNO06M3iUgUVBCjSco-C2hIxzAF3GkWryb0nNylcNMVSC2VUAjthCTxO9nKEyLVu24djOncQGUJIxato9xEG-D76EUkTQ5oHkb8igzAS1OPZspc9oJDuefzp3_aFYUo7ounxFRO8AhSUi-IKGIItgacWar7Lm14jyf4WD1QA4Lj-nA08okG_naFGAdDqbGODYQeJPEiE18GIMHniDalJp8RxjT7VEEZIoULum6GsXn4D-MFpL2X-hiIYl4By9e0cdMQ1jGnMPdFW7S1ThjXNdifVpVlhSLrjy048frgKgniXhU9RNKh_ITEwQQOcdIA2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم پریمیرلیگ؛ ترکیب آرسنال برای بازی امشب مقابل استون‌ویلا؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105207" target="_blank">📅 21:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105206">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ut9Q1iCLi-FWMTSUeyjTlotRngrNbuSWhBLWT8AKgkm5ecsGbfZhIZYsYb8PvupVVkGRYXxioMUz2YV-SsAzcaB-iwpiDC_u7Cqlq71yWzuK4t5OGUIj2rcRCNXlDn9fF2ncyeIAm40ukj8evpl9mnnDXPaRfeXN9Hlxj7qMGJg2NA3dZ8FcgA2qNRCSe-xEmmXzZOW89FsqJUmxMWrgvnKoOFiBSoOtUe7TKZG6Ctgss7bZZUH-Jt48j8Hj4EHzAHZIscd9lc7DqaGQ5gHVDpNwLJQR6euxUiomuXAkfMMPvSHLmetuuxqyqpDioIqYdH2r5JL8a7eK0cqGZQ92vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
فلوریان پلتنبرگ: آینتراخت فرانکفورت درحال بررسی جذب خوسلو در ساعات آینده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105206" target="_blank">📅 21:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105205">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m81ULfKttggnWhTchuKXM25-q8QHpICMQgvehhaFI6-sG1knpiNBBHNIgzDxCMxCOAnnPK_7iwn30ykyshnOvhpfo7Q9IulIYfUk--7UXZDPtMt0ZmvA4fxViQY8Vo7YblFUzVVHg_OvLsGbvSEc06lZwOl7KLxRNnBb7n39V8DfDuJnX2Bk_JtrSaN_ZYYKP_-8Jqbhj6qs8NTR_dCnOuCIn5kHgEDHMrfjTd7M3nVW8G8sQrfPU_gCqjmfrgVN0qYXp4p9lg6lPHXWD_24ysg9y6KnkOaFG1WPvPe1ywDdyfplXcjjWs-W2kR9WV5ilPdT6OBYxdHd-WURNM8QCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
💋
با این ویدیو فوق‌العاده و غم‌انگیز رسانه 433 میتونیم ساعت‌ها گریه کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105205" target="_blank">📅 20:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105204">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooFYUEC78k_W65a141PJHrv7pBGp18i0CxjWy4g85j3sQuGE-jEGwoOeWCz2OVdAvumPA8G2L69HK4r8hvMqlEA_48SuwOT9N9VhMO-KDOOLWhSq8dQkv-eWFszKshLJ8tzAC4ZkMc13LH-5u7bUjgGnVp-Qa3IOQcOshoArzOBZ5YQG6f-BPaocQB_XxtNu6HJ1Ghvxz0KH34NgwKpI-GUmyNNIRd4OhLcSBrqGuHC8rRHYiC97__J073t1q86zP9YkfdjYvbSzoWzQW08hJs-zxnT202xPQHSkS6gZMo8ePpknlAj9t6g8peOaUaEDhW4cbMu_PvgGUFXQopVdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت بلیت‌فروشی دربی طبق معمول ریده به خودش  زیر ساخت در ایران 0 گنده‌گوزی 1000</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105204" target="_blank">📅 20:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105203">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
⭕️
#فوووووری؛ بلیت‌فروشی دربی آغاز شد. برای خرید بلیت از لینک زیر اقدام کنید  https://ticket.sepahansc.com
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105203" target="_blank">📅 20:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105202">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
اعلام جزئیات بلیت‌فروشی دربی ۱۰۷
🇮🇷
🇮🇷
بلیت‌فروشی دربی از امشب آغاز می‌شود و سهمیه هواداران استقلال و پرسپولیس ۵۰-۵۰ خواهد بود.
🎟️
ظرفیت در نظر گرفته‌شده برای هواداران: ۳۵ هزار نفر. سامانه بلیت‌فروشی که فروش از شب شروع میشه:   https://ticket.sepahansc.com…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105202" target="_blank">📅 20:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105201">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEw4bZb-4-D0Oxq0s4mMzGAlaSVy8M0BctEIR_BvG6WK_dzpPnha2eqqLUPBY_2EsmrYRHIg1cWN1wYqtj3e_bl3hJo9YQg-IjoixjB2rHydOTpcWSjpOPhAYON7eo4lgVNxp21GeDmyesATxn3nQUO-m3cHx9PZz-SYCvThBHG8qfvBJBaYwASxU6pjxwSUjixxbxaq1uiy9JTBQwSwS22okchrqmnN0ElHmUKTzORZx0cgIaKCMB5PO5ELeloNJ-63rCPmX4W_wt5iHrllbhSXDK_LUucLj6jdV-YwLb_YFWbbIqqCse4fPsO9dEXeE_jyafuwOE-JA24CNV_1hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
🇮🇷
در نشست امروز کمیته داوران، موعود بنیادی‌فر نظر منتخب اعضای این کمیته بدلیل تجربه بالاتر نسبت به کوپال‌ناظمی بوده و قرار شده قضاوت بازی روز چهارشنبه که حواشی بسیاری خواهد داشت، به بنیادی‌فر واگذار شود تا بازی به درستی مدیریت شود. هنوز تیم داوری رسما…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105201" target="_blank">📅 20:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105200">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5DVUKJc7UkPdZg2nvIoZyhkZEJ-bwqQXwcEedWuGmYakCGXFt-oOyy1SK2QTHtUru9U_gDW3RtYzTtuVXzvbTWkdtVjJwrIgL7rOjc3F2A0Vh_QYoa10DvrAKTIU4VwNgJvtnkpA-Wyf3MM8bShqHjoQILN9CZvIqVcSpxZ1HW5E2gjhJ4cuSCDAI-bMLwgT_Ipewxb9XU3lu037z0EfWcOl_GQfL48j_RAzK9CkqyCuJMLPAr2TqhrVW-sfgU6ienAKDBJqzDBTN1wl1GhRJmqzJkpvYKzKMspGrz6mV2eLyMCKlrlusGBkPotHrsfXh3KPoz8FYmzxcW-lz5QNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😃
قدرت دوس‌دختر در بازی دیشب رئال‌مادرید:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105200" target="_blank">📅 20:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105199">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8cb7444c7.mp4?token=OfcST5zLXEGDNbgvEN9M3eaKzbt3UCdUX9eL60wUv_53LQXcxkH7zzFxP2s77PxFrqnvSMoEak_Yzh_oVedveaCr-E0otm7rcLdjcHJ8R7N62z8VH_6CmT0DCALw00gQhPPy3pUKBF6G1lPvuEj5WYfJbAnTbQzDn6gPsgzaHkOgzvLVYARSevWVSob1rOctYpf8OyHRV6Ls_o5AIexUY_uxUzCmAOXqsZ5yMWwWNe3IG6xt6-9Bk_9CeY6_u5ur7MpdsZVTCQt8ED84W6BUH8GwnfyeRvJXXLd6S1CK5GRdiPOkpVzuAJSMM2V97nrdKWZdT-T9R2P0hHmj389icky3hMF7IhdmnLN6fsUBJRK3TWeA-IOEsWqu68pIKmOSs4Z9vU26HECVqG4qaAWZlVza93yPD0LgVNhsabPGl_av-8sSoaWGssOKdX8vAL4kxY2gZrZlpd16VU2_lktrYYU_gBDe-vtAR8_WCaDQJmEB_0-065Fj0qE-9fi3vsbGdcVL4ePw4F5xzUpo1e6jOQ2Rdbg5qlfCgI4Q-cEAcOGw0ing1T3URLCdwpkk6WsSieGZH2-lOX2TA5uqMl_6qAGvdz_AATfsTto7eDcwvGPW4TE7IVlcYg4MNYa-cZy3ikLejNCQrjZXgreL-83peJHfTLBZalv6yyyjIJFs0E8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8cb7444c7.mp4?token=OfcST5zLXEGDNbgvEN9M3eaKzbt3UCdUX9eL60wUv_53LQXcxkH7zzFxP2s77PxFrqnvSMoEak_Yzh_oVedveaCr-E0otm7rcLdjcHJ8R7N62z8VH_6CmT0DCALw00gQhPPy3pUKBF6G1lPvuEj5WYfJbAnTbQzDn6gPsgzaHkOgzvLVYARSevWVSob1rOctYpf8OyHRV6Ls_o5AIexUY_uxUzCmAOXqsZ5yMWwWNe3IG6xt6-9Bk_9CeY6_u5ur7MpdsZVTCQt8ED84W6BUH8GwnfyeRvJXXLd6S1CK5GRdiPOkpVzuAJSMM2V97nrdKWZdT-T9R2P0hHmj389icky3hMF7IhdmnLN6fsUBJRK3TWeA-IOEsWqu68pIKmOSs4Z9vU26HECVqG4qaAWZlVza93yPD0LgVNhsabPGl_av-8sSoaWGssOKdX8vAL4kxY2gZrZlpd16VU2_lktrYYU_gBDe-vtAR8_WCaDQJmEB_0-065Fj0qE-9fi3vsbGdcVL4ePw4F5xzUpo1e6jOQ2Rdbg5qlfCgI4Q-cEAcOGw0ing1T3URLCdwpkk6WsSieGZH2-lOX2TA5uqMl_6qAGvdz_AATfsTto7eDcwvGPW4TE7IVlcYg4MNYa-cZy3ikLejNCQrjZXgreL-83peJHfTLBZalv6yyyjIJFs0E8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخرین وضعیت زنده‌یاد ورزشگاه آزادی تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105199" target="_blank">📅 20:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105198">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2396WXkGD7rE8O4f4jr0YGXd3F9nAfrVaq0TAXNPlBMy3v-ASJoV56Vy9vRqkDZAo_a4vQJabE2MivLJBexAVqN0NC1PKiGR3UFE910VU7uvaecvQauM3HrftZ2rW58K9p9d-Kl_y8pIdPw1qXkbRXYOXUQvJXIMT01I57tzeUSVXX3RMQYAa4ypoJzrn3EcLoD9Ng3rAf6Cpxu0azmOH9qDUUpZz8RZ-9ryASZGklvT11lexqAfB_kN2ig1icJPfGA_ZrXWlb0fGxVyWLIy0qxCDzHndI_C5QZVFVm-_ggTCn5ltYK22c2BeHkpz_m-g7NdyRnF1MWxOgRv-j74Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
آنتونیو آدان: به باشگاه استقلال گفتم که نه پول فصل قبلمو میخوام و نه دیگه حاضرم به کشور جنگی ایران برگردم. قرار نیست به استقلال برگردم بخاطر همین طلبمو بخشیدم چون وضعیت ایران خوب نبود و مشکلات این کشور رو درک کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105198" target="_blank">📅 19:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105197">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpJkWpCRxTylfw8pLHZ8B4m1x7HHHorOedVhWafWIFQQ_x1VIR7PXJahE7ojiJfEVaQO4MlaWPejzU34S3ZoaBREqSy-tr9aU1s40VaxmrubPzAl_rajF2AWUiR-B7uhEemTNy-1uDj_z2C7TeIb0MfV50Ai8CZxolOKNg6RKGJD6GGfp6yjqU3KO4eCQ1bxgEEEFNWi7Fm8YL5WXb8rY0ZdHa6oUfS_9Ew_yDpZUf8-cPbVoN3JWu0vINsfTOjEa0FTrk-M652x3F3yvNGpesCDVq3ifSjdiC4n2slJkQh2wSTbrB70Tyu7Eig46uF3eWTRpPDWxbgBYVPlbACYGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
نامزدهای نهایی جایزه توپ‌طلا روز ۸ سپتامبر رسما معرفی خواهند شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105197" target="_blank">📅 19:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105196">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCx9AhwlC5IM2g4eITtrGs1nssuTezSpFS3lstP5ugZFRILEbxXkgrtlng2UeHQIftFHyiT46lRMh3eJsWWulEsgmaZ1M-6e5nCUjThBFPjup6NbrtXpMrPR24uvGYnYASbC8lYoDftkitB3gjFztXErYz7vcJkX_r-tslCzEKik_dDBKZ2YBrn-3sMPY7RnpHUAfpmJxnkfQUPpquOqteUBWsRhaSXAWQFkRnS1zz8JFQFeFDXMaipXEhEPhLyNp8hZzuZ6CRKjOFW-4ruzkYI3NImCU1SaiZ3UDso6tiIOK1WTISxBhC8u3Jkl5pAnQzwFgsMRnOmqJ8aYFn5jwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
🇮🇷
🇮🇷
دربی با نصف ظرفیت نقش جهان؛ این اسمش مدیریت کردن فوتبال و مردم نیست
❌
ظرفیت ورزشگاه نقش‌جهان برای دربی از ۷۰ هزار نفر به ۳۵ هزار نفر کاهش پیدا کرده؛ یعنی عملاً نیمی از سکوها خالی می‌ماند.
✔️
در دنیا برای حضور بیشتر هواداران راهکار می‌سازند؛ اینجا اما یا تماشاگر حذف می‌شود یا بخشی از ورزشگاه را خالی نگه می‌دارند و اسمش را «مدیریت» می‌گذارند.
❗️
مدیریت واقعی یعنی فراهم‌کردن حضور بیشتر و ایمن‌تر هواداران، نه ساده‌ترین راه یعنی بستن سکوها.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105196" target="_blank">📅 19:39 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105195">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjKflzTS1WFxL2MqdhbzMbX1PcFc6SHuDY2im_z9V92cVutZ1EClIWP-Irk5Vjjfrw7Fx5bdyvzUdd65ruiiQVqgCsXWScxLlwJJPAM5D07nk4wHCfiGbiOC47EwNWT9UNXu3RyiEWl-1nOJthmn1kheUjXZUViSLvgMDTr8Nt6YZXGdwhmOE96opUSyU2da6MHtDLf9Sa3N6jXwg41qR9E3APyV6qnuZu14b6y4uDvOjoJfS1IbgJEQyoFDAqLWpaMgXLsvLseadpEPP7hJBpRmXeUQpYkPCjT-s_pTo3OLGJvfwLFeND6rEs9QeJ7NL5JFq8cThaUtd3U0ec_5og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اورنشتین و رومانو: لیورپول پیشنهاد ۷۵ میلیون پوندی سیتی برای جذب گاکپو رو رد کرد و این بازیکن در آنفیلد موندگار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105195" target="_blank">📅 19:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105193">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddcd857187.mp4?token=Z5N5KCoXct7pW-Pnt0PXiL86pnvD8hN2PWYpszLv0g2ar_2WJ3yATxCBt9c3y2TaOMWIzOVms1TxzXkMR5I8sEoTuP-LPJ36bXEbGU3XTZI1fFBJAHDLx7rV3ZMrUFkZnBiCbhJwUom2meodAWII32Su7O3kOHp-Qc4T6mhcPMPRYe2XpBDHYgZEQ7TyPFsfgSy1j7Y4pyw6Zzx1wzS86L1AbP7NqZDcCab05IsVhw-DfOF5KIB3OEKsQcRyL-PM6QWkYz2H42Ekp-U-F6BDDcgcUuegkFYld2OcSAlQaLLIBiVzLdTZpdluUFlWH9peDFQvlJ-xCxKd8NcLNZib-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddcd857187.mp4?token=Z5N5KCoXct7pW-Pnt0PXiL86pnvD8hN2PWYpszLv0g2ar_2WJ3yATxCBt9c3y2TaOMWIzOVms1TxzXkMR5I8sEoTuP-LPJ36bXEbGU3XTZI1fFBJAHDLx7rV3ZMrUFkZnBiCbhJwUom2meodAWII32Su7O3kOHp-Qc4T6mhcPMPRYe2XpBDHYgZEQ7TyPFsfgSy1j7Y4pyw6Zzx1wzS86L1AbP7NqZDcCab05IsVhw-DfOF5KIB3OEKsQcRyL-PM6QWkYz2H42Ekp-U-F6BDDcgcUuegkFYld2OcSAlQaLLIBiVzLdTZpdluUFlWH9peDFQvlJ-xCxKd8NcLNZib-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
💋
با این ویدیو فوق‌العاده و غم‌انگیز رسانه 433 میتونیم ساعت‌ها گریه کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105193" target="_blank">📅 19:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105192">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
▶️
🇦🇷
ویدیو جدید اسطوره لیونل‌مسی از دوران حضور درخشانش در تیم‌ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105192" target="_blank">📅 18:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105191">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Htuu9_uABgfeNjHsIrn7yp06YvrHgpi-lkkDupDobixYUoQ14R-dNRPfwYEa5zhvPIcciP_fSZXG92Yq1AjlaSmDjbDj6FgrpYQr46OifRpya1BrmjD4rXKsL9hB_CB5y04hHZZpDk6Qql2wPg9tXOtuKwaEg1bhUYQHKRqvxvmasmFMxVlAKMX3dlYEzy1R1Z670Le-YuGq8G5bpBo-Xdhzm7A9vvhdHb04gl6Yj87rmIfS1rrqcNjduShe-_kAEkFLmxy9YL0T3vL_VTbtDdpHLTNmI2lRGqA4-v9OrTKUwWpbBFKHTUevEOuzcOFhn60oh2TkpZ2-AyxLYcAkTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🐐
عملکرد اسطوره لیونل‌مسی بهترین بازیکن تاریخ در تیم‌ملی آرژانتین:
🏆
1 قهرمانی جام جهانی
🏆
2 قهرمانی کوپا آمریکا
🏆
1 قهرمانی فینالیسیما
🏆
1 مدال طلا المپیک
🏆
1 قهرمانی جام جهانی زیر 20 سال
❤️‍🩹
207 مسابقه؛ 125 گل؛ 68 پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105191" target="_blank">📅 18:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105190">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTaYaiX-Z8r_jPdLWqxx6m0_caWWzDeTbadY1uUj3dAXPcRVfJyo_dFFhSWZaKHtJiLJO4rxGUzMt5ZuoHHR2cU35hAKLCJ9JQf-2gXtPKflpjRLKkIMq8iUdgItSdnToMfkZu3UH24haRNFcr1jNSGHlo7U1cuKwh7P-pU7BAqh3D6KQEsh7iROrZ990w15XklpLs46CXgu1F6OHGe8yqawSOvUpCd30pDI_BZvUqTNlW4X_8v4lzSY0svh9LV5Pg1JMPWI2RVPyhzvBTUligTNQKhVicfQgFQ3af9h6Wy0tIcnv0WBjgLG7T43YERAlbjkWoJ7lhZHpyGx_C5aFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🐐
📱
پست اینستاگرامی اسطوره لیونل‌مسی و اعلام خداحافظی از مسابقات‌ملی:
🔻
دوست دارم، و دوست خواهم داشت، و همیشه عاشق این هستم که بخشی از تیم ملی باشم. تمام تلاشم را کردم و دیگر چیزی برای ارائه ندارم.
🔻
همچنین، بازیکنان جوان فوق‌العاده‌ای هستند که در حال ظهور…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105190" target="_blank">📅 18:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105189">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6y8ddjhADEMOHyG2f7ACHseTlHKParRTiHdHTXBZ_-CypW6lCAopOf-Cm5_jjKURPPEIm1fg3Vmjym2wRKplrF3BMNBF_KU3nQ8DKD-jEb7Yg7CgVaviSggzYc5qzLegCST-EVIF_5dMi-JK64deYUvZ3FEUfvhHBV7SLx8nuCHYllHKOih23FOOrvcMy1easydjPRq6ouEBQTmjq4oYYDc8A_oaygeAEJFJucWFjbrHx3rPyRqgcIkv86wYGa8Z60xZSmlHhJaKLYNRvTX_oLipQ4I3pQ4wYwHedYFjES9kDStYOpDfMmBHXovs1wC2UsEhZo8XYBk0J65E6phXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇦🇷
❌
#فوووووری #رسمیییییی؛ لیونل‌مسی از تیم‌ملی آرژانتین خداحافظی کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105189" target="_blank">📅 18:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105188">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmveJyY1h6-m_U8jPVHfXsIS3pMXpoLhdrZ87A_dJfxqHqhsrVLUmGWYq8nYNDYj4swsAU1qi2F7AF9J4TzNbT8JqHRifph2nbS5O9fy6KaBLchPM9qhjbcBPJLe6VK5UiFrZajHUDLKOPJh2_JQgWIQ5BrmICLos7VAJ23GH2EJ7LaiQv5HI6cg3FP-0_TawNNnFx345zH6uNy-xM_pP5jqAEjt0PI5DdIggdt6Yiw1XK0h-GXDL0rzuiezP9HIsLMROHdxEecAeweoAn6KBWxnoD9OD2NdnRocJbrNwjktjMNdmOKOC9cVerRNs84r90F8NwuBplob9k9hKvTL_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇦🇷
❌
#فوووووری
#رسمیییییی
؛ لیونل‌مسی از تیم‌ملی آرژانتین خداحافظی کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105188" target="_blank">📅 18:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105187">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI3vksfCo9eEcg12uSSOQoSLHnqoM--BXxENR52kW6Hs3r-y2Jf7V_pwFv5znwnZEjCB7EVvcHyFnqjE8kaKFJ0TAp2E-05-pGTScojsqUjF3gNFkMatWI8222quS-Mvy7t-awKWh0dOsYLcwby11dvdZWhq65iJ0FGTcJ4a6MjQfScfWxyyWO22NO6NELI2mP6gfbRwPp0OniE7BzYvXlEns2FnFO5TY-3Tj2VSOdPRoOoXgg9mVLH9kmq_I8NwPNc6OaNjgwEX-oGRFAc7zteoJUe1ydjfUbQudQSxzdljKuwcGi5e4zR_daabBdA63EMV3mFuvft2oMRo6bBWAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🐐
مقایسه عملکرد مسی و رونالدو در میامی و النصر؛ کدومشون بهتر بودن با ریکشن بگید
لیونل‌مسی
🔥
کریس‌رونالدو
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105187" target="_blank">📅 18:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105185">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f80bffe56.mp4?token=Kapa0evaCse11zHKpmWQSaRBthEkMR4-i3QuBFenGH6s5KeFPHD7GSfQEWL--f7PVJfXDDY3yUNfyG6dA1RKRYdS7ute6y2ftTUrFAkRKhzeus01W62LWs2vZ-eWTMakrXbXGsd_7gnqx5QDF5-IacIYyvKNYPEstf1hULOWj_ICYFhpQkUxVgzIMGKn226bxUzk9dukZ3tR8UYZM4DhzDd8vouhL00SkVxKdcGlXcoaDsLq7Wj9Gm5p8p3k1qjmxHxPxgUKujlfdJv_zVhXr8V6CCwSZnmmM4EFHxPhFN0ZVFBgelnQ8O7BB3IHzZt6nsdKLPX452rfYAVUewLqYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f80bffe56.mp4?token=Kapa0evaCse11zHKpmWQSaRBthEkMR4-i3QuBFenGH6s5KeFPHD7GSfQEWL--f7PVJfXDDY3yUNfyG6dA1RKRYdS7ute6y2ftTUrFAkRKhzeus01W62LWs2vZ-eWTMakrXbXGsd_7gnqx5QDF5-IacIYyvKNYPEstf1hULOWj_ICYFhpQkUxVgzIMGKn226bxUzk9dukZ3tR8UYZM4DhzDd8vouhL00SkVxKdcGlXcoaDsLq7Wj9Gm5p8p3k1qjmxHxPxgUKujlfdJv_zVhXr8V6CCwSZnmmM4EFHxPhFN0ZVFBgelnQ8O7BB3IHzZt6nsdKLPX452rfYAVUewLqYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
استادیومی که تاجیکستان در کمتر از دو سال ساخته؛ امام‌علی رحمان چه رئیس جمهور شاهکاری براش این کشور آریایی و متمدن هست واقعا
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105185" target="_blank">📅 18:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105184">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aP36cYEqHvE3SfjptL6m2-tI-iJack0M_qCDg3ttFkTRSxkNF6Yeqv1irFmaq88R6d90tDxXRGzfbUGXFjaziTOUx5LCtju9tBF-J1JRoI0Cj3-LiT0kKvZZbsPQBq1K2Vk4I-YmNkdw611SOs_zJon22DTBepskbunRKS7jroYyEN5-OhpFwXEtJ5wanjlgqJybjDWuw7FZRXKUW4mJuNKQmXWE5qVfW1rZ9iqJr_glIHw6e-_mZ1Gjd8pFyJ3KNhh17pcK0yNzsSQTPl3cOZ2Dx15D-fmMknC3duc1AaQugiQlhZOTXRromN6PrUYuxgv8hWehNP8hW6Wf1yKRXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
رومانو: بارسلونا هرگز از تلاش برای جذب آلوارز دست برنمیداره. اگر در ژانویه موفق به جذبش نشن، در تابستان ۲۰۲۷ تمام تلاششون رو انجام میدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105184" target="_blank">📅 18:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105181">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Co6wAAv4tPUV_ZYvE72fsnzWppiiE-qlYkOnwlVnYIpwVQfq6EZEP20NYxSMqKwfVe4_F7aIUBDG-jcKpLHEHJd9vQ0KEGI6pE9q3Y6zm2clNyll3batzw2j0XkWpOFlOUc2ysxDM_ics6ASodoaKF_iLt2QbzBTXkEZLI_fjH1iSw4zZqjiWsImqMYVZeNORpVEOlFAf004_QWTvwIbxxoWOsONSmkQSeH5QcBd7KmDSFNmYuq-O8k0BbKBJN3DoIHH9LEF5cFMjLiUo8tpsG0exYcoTS6fCmLEWeUkzlUapVtjU6izJczYrSB3nHkMGTclRNj3PBMclRdSgiyG8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇸🇦
وضعیت خوب نیوکاسل پس از جذب یایسله سرمربی الاهلی عربستان؛ در مقابل الاهلی حسابی فصل رو به ریدمان شروع کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105181" target="_blank">📅 17:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105180">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⭕️
⭕️
با توجه به نزدیکی به دربی پایتخت و بازدهی فوق‌العاده تبلیغات تا پایان هفته، اگر تمایل به همکاری و انجام تبلیغات مدنظر خود داشته باشید، با ×
تخفیف ویژه
× در مجموعه تبلیغاتی تیوا با بیش از ۱۵ کانال مختلف ورزشی و غیر ورزشی در خدمت شما عزیزان هستیم
برای هماهنگی و‌ کسب اطلاعات بیشتر به آیدی زیر پیام دهید. سپاسگزاریم
❤️
@Tiivaadss</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105180" target="_blank">📅 17:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105179">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Otb1kUb0BUcsx_NvkyrXw_hlMnH5QAN9h5dL-YOc2dJdpU6iWtVRhIh1Xrg0HYmKTAWli-YbJkxA1OQxfmE1ZKY1Ji6tqmiomPTfdHDxrhv5tw4H7ruNA-dM49mBSOg8-01mx9unUm7YSaBBc7hne6_JVNXuByWSufVdGK28-ozZotrdli_4DeYOwSk1dYSkMhFa_IKcc7dJmu93FgC5L9cHGocmOAStjCFJAnuj5PlLA7yQBla77QxnKcNuO3bJZ2SB3P-4vd_xDzor9Nvxf27kHYc2TgFJW0wAHwgXC_ggwf8XLAFGn8BN8obyNNRqlxuG_WWnsZpFYLLZfNsDtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔵
🗞
#فوووووری رومانو: کریم‌بنزما از الهلال عربستان جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105179" target="_blank">📅 17:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105177">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UNCqCUMH_YCo3aVYd4zR7bI4DTlPQaO32UMMb0jVOHLBYHfoN_QrWn0GMvhPEOpY_ksz2QoxapGxoJM5xb-3h4SPPb4MEwQeXlO_pcfH6Ca4mTj5_-GiEiDTNUN4aAv7iIFigvb1M1-5lnuisSWqqW0bGXQ8yvt3CxCpp5wLlsobKxkdJvHeKWC90xfT6EHIqeuKxFMCURx-WaqGDexq6Ura37LU9vWJmG5NfWEs9j61ViE1s6T_iLPqLEXnjXe8On3BbtwRlge9l9W_v-MOXRxI-dcC11hw4MjXhqyzW9HnRBUAKh4zoTHG9PjZKIBog-JlgZKAEr-vPGBM_nuLXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WOfv3aSFHmTtkkuDPj6dzPjoHxj1KYhM59gJIyb7veLeHLJmneIqOGv7KjqOlh1qFA2K7R2ftjKFMG8tCvL5bhkHw1nKX3HzM1rZm86LZDbZ8dXU_10wp5aUBtCIQd-E7ynMycsI50zhA2s1j2UiyTjpoDOaWp84nw2SbTdulObosEssAIsK0yOCFMWUTBO5mg2Hr5Rin6Fbp2m6RzQSsp4fiZI0dO34L-ntWu_jlvOjGnt_wycPp46iY6c9QhK1VMSmnsmvPAoHI3CPWiv57_jwmIv7oI2ZUpzda1eeW7pFgme2XiUUtwqk5VlEwxJ1aFRCrtbueb0EqgUZMYLdQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇪🇺
اوا موراتی، مجری ایتالیایی چمپیونزلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105177" target="_blank">📅 17:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105176">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚑
🇮🇷
#فوووووری؛ ابوالفضل جلالی بدلیل مصدومیت از ناحیه کشاله‌ران دو دیدار آینده پرسپولیس مقابل تراکتور و ملوان رو از دست داده و وضعیت نامشخصی برای دربی داره. پزشکان حداقل ۱۴ روز استراحت رو برای این بازیکن در نظر گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105176" target="_blank">📅 17:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105175">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
بلیت‌فروشی دربی پایتخت تا ساعاتی دیگر از طریق سایت فعال خواهد شد. ظرفیت این مسابقه به شکل برابر تقسیم شده است. ۲۹ هزار بلیت برای آقایان و ۶ هزار بلیت برای بانوان به فروش خواهد رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105175" target="_blank">📅 16:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105174">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15501a2dd1.mp4?token=Yp7C_ex5MVMgzxMmGcXDIYeZFXZuOWLJN921gzGs5j629QzFSEbv2m76HXe58oxDYaCsS2Qx2xJLkffIgTQe2DRjvrFwwmcWZwDG05aiTgka_pwft3gHw3fKkOWjwSwYkdWBHEtbDqHYl9BVyCqh5isjmXnbD4K15ReV-XZYpBEHZS4_P5vcUTPF9vyQ_oVc5_cdvYrufvYXyqmyuiu2u8lBVQ5yHKz-5Wvab6TdEvw_thoAQuiiZ4OB_fFf-UTO4-5uWowEmMXnTcVybp6_ynQMYWHo-cHTIpHF3LCRr-mAt2LidG1ENzzifmr0nzgeHyGyLz-o3OioEO2NEeDVng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15501a2dd1.mp4?token=Yp7C_ex5MVMgzxMmGcXDIYeZFXZuOWLJN921gzGs5j629QzFSEbv2m76HXe58oxDYaCsS2Qx2xJLkffIgTQe2DRjvrFwwmcWZwDG05aiTgka_pwft3gHw3fKkOWjwSwYkdWBHEtbDqHYl9BVyCqh5isjmXnbD4K15ReV-XZYpBEHZS4_P5vcUTPF9vyQ_oVc5_cdvYrufvYXyqmyuiu2u8lBVQ5yHKz-5Wvab6TdEvw_thoAQuiiZ4OB_fFf-UTO4-5uWowEmMXnTcVybp6_ynQMYWHo-cHTIpHF3LCRr-mAt2LidG1ENzzifmr0nzgeHyGyLz-o3OioEO2NEeDVng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
وقتی صحبت‌از دربی میشه؛ خاطره ورزشگاه آزادی با جمعیت ۱۰۰ هزار نفری و صدای عادل فردوسی‌پور زنده میشه؛ چه دورانی بود واقعا!
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105174" target="_blank">📅 16:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105173">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">▶️
🤯
برخی از سوپرگل‌های چیپ از راه‌دور ببینیم؛ حقیقتا گل توتی به اینتر یه چیز دیگه‌بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105173" target="_blank">📅 16:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105172">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCPslrgfIU-bgPqW6sk47d9FUirwR9lIpmoMcBQntfXMISyOYWjhreZEd5jVyadfGVLL8Zp1vFOqRtdpIQfuQVVcF3E908_1lkQrEGAQRGO1enuHB6yHPfyfUBgrEMNn_amftIlYQv02abFykmFwak44s3et93n4dC67XJBvDZ2FHL7M2JqFycTxwaeguSWEAsji2qDDgIzW79Y68gfoajeMYmLj-hSpWyXhmyzo7lEOR1o8i1rI1fQIsvEmtAO_g7ID05s1CmJV-39SIGJ6dudmQUByluIoIAVoHJmhn3XHrgAt6E1Q3Kka1JPdmrLIgnynE4MP7Msk70hLM3QgSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
عملکرد اسطوره رونالدو‌ در ۲۵ سال حضورش در لیگ‌های مختلف فوتبال اروپا و آسیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105172" target="_blank">📅 15:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105171">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVtrZVaOffYST6YvNDRE15KlfQRmjJzS-sx7vBIoWrtWZZ1Uo6A0shdNzJGhJ0tHHPwjph_dfPwF99ykRcEXeTuGj35rFvq-0bdB3Cjg379uY5YHL7f30Chr0PLa0yEgQ7PBVQmcs7x2k6UQex0vhaXn4B6R9CFGaCCsiXbrqxrylOq2yKZlGHSiDPM5GADQ-RBw7Anp_bW8dDynAGTmvY3D1B30iy_godypOxRzGN33J_cpB2rupRAsr_a9q15ueumA20DfJXBa6CTSouS7RMHzGVDir1iBQX3wahWjC2AZ1ntoNYSDIDlG_8QNy1gWpeaD2YIM5d7JRSt8KefYKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😢
⚠️
دختره ول‌کن رامین‌رضاییان نیست و یه ویدیو پر کرده حسابی ریده به سرتاپای اسطوره اخلاق و مردم‌دار نسل فوتبال فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105171" target="_blank">📅 15:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105170">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPITHmwMc4S9EryLiZTEbQVSm_u0JLy9rRFNhkYcQQ5-rJsZduoSKVv4mJacy8ew4j2rezamQgSBO-gH2PpBXF_TPrsMpLEPT-VNFaIlem46RZ6qMz_bekEgjwMcmrzplOqJ16aO225Z-Qfd0bHzHY1mRAjYCpRMskfMCZS-78RLO91rsgO7LJRbjCHLi8OhbqKrDuEUWqEsZ4NmhRMVkBqerdPkyAlFBjhzNr92xJ7DIlO070iVPcTcSxp-oLIsv_GHa8BHaRISfw2gzfhyit88AJC1at6brRjISq0fAe6ClgJ50nM7TTS6kELUE76hdV94lNzhQu6kgb5s4c47Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
😱
❤️
💵
با رسیدن قیمت دلار به 210 هزار تومن ارزش حقوق یک نیروی ساده در ایران به
75 دلار
رسید. حقوقی که
یک ماه
باید با اون زندگی کنه! معادل یک
دیسک بازی کنسول
که در کشور های دیگر کودکان با پول تو جیبی می‌خرند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105170" target="_blank">📅 15:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105169">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWQ9D4lcN612iNn1zPXFvng3S6EccmzOGs4QMMW5cGVxJsjOVeWnlKu5C7UuLhNS2_IIZkwGbJ4TzRQYVx3ExYuFA8NuJVsLBEVuxDZ1G8CnNBrMGCjc2ogWZD9lV_4ouCADb1juFSlm5AHjNNx2oIGw_HTB3Y7ZYTWYaoSFxiktf6DQMY_56yJ7fLUvVAzVGGwykdgDG29dIY1Zhu0VrQZ2GrjZZiz6vJBM8kQZ9rSZbQ0GNEiElEHwPgURj0QlM6NGi-yVQe8RozcGQ5Sgii3dT08veXEsaDJ43SFceaUP0unynJ2MQLzTu8CZrruen0lz_kraCKPf-93pLqnmjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست بارسا برای بازی امشب مقابل رایووایکانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105169" target="_blank">📅 15:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105168">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32a916d757.mp4?token=ZJPrvMHhotY2N80Y2Gj01hHJ_52DVLfShNmpQkut6PmwLyD1WYXw8tm9QXozJXq2i5mFsFmc-Osyuy0MsF0MGtUlx0v2_FOr4PHuAIP9KtEumvTnKiXdABptRAO9wXBkXJwg0S_ccG4rsYNZUviLvMkBqlXotUhT-WLfdQ5B-LIUBOskZyhuwFdkZ7VThSq-RHyebQ9c7j0HvuCJmCD_HzQQ2NV4t5dbfETgYWm3RqLJqqisSWtXxRGcfnI8oqE5D0NZZokfUJlQ8PFbxxNkfF--xbyD7ZVqZnCc26L5oZMPJ9Coya6RkwTARQHzEfi8IfHV9xq4S95tJGwsz_M_5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32a916d757.mp4?token=ZJPrvMHhotY2N80Y2Gj01hHJ_52DVLfShNmpQkut6PmwLyD1WYXw8tm9QXozJXq2i5mFsFmc-Osyuy0MsF0MGtUlx0v2_FOr4PHuAIP9KtEumvTnKiXdABptRAO9wXBkXJwg0S_ccG4rsYNZUviLvMkBqlXotUhT-WLfdQ5B-LIUBOskZyhuwFdkZ7VThSq-RHyebQ9c7j0HvuCJmCD_HzQQ2NV4t5dbfETgYWm3RqLJqqisSWtXxRGcfnI8oqE5D0NZZokfUJlQ8PFbxxNkfF--xbyD7ZVqZnCc26L5oZMPJ9Coya6RkwTARQHzEfi8IfHV9xq4S95tJGwsz_M_5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی دو سال پیش این ویدیو از نامجو رو دیدم که میخواد کوکو رو تو ماهیتابه برگردونه، شما اگه این ویدیو رو میدیدی از هیچ کار این ادم تعجب نمیکردی دیگه حالا فکر کنید همین آدم بعد کلی فوش دادن به جمهوری اسلامی دوباره برگشته مملکت تازه ازش استقبال کردن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105168" target="_blank">📅 14:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105167">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fea9db172.mp4?token=W-x5O4IcQUcgFcg3lrCy9EzYsJoRNZZT4OhdHKE50pPyRjX5eRR3DMGg8lwcfFDKOPOL9jxG5fsYzB0bjzmJqRw8pIcZwZdGvc8y39dPypLUqP7BHFVb_QFfVtZXZCj-BF2fQzGGN51KWadjXFLI76u8r6OSIZlDgsQG_TqdQJEq2SMWE22goP8RLy1KQO6nvzc_bmc9N0FRSrfOGxO1i37Ex9heIkvhU_UTCEBsUSVfFKjVoUamFXMgzbU2TCi7LBkss5NM1Q-MbGZcQsQE-gAVPiSlUqoAD5TdNPA204hDXh6Li8ooXIAt2C6Bxmj0QpSRNzJPUdX2--hKeZMDNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fea9db172.mp4?token=W-x5O4IcQUcgFcg3lrCy9EzYsJoRNZZT4OhdHKE50pPyRjX5eRR3DMGg8lwcfFDKOPOL9jxG5fsYzB0bjzmJqRw8pIcZwZdGvc8y39dPypLUqP7BHFVb_QFfVtZXZCj-BF2fQzGGN51KWadjXFLI76u8r6OSIZlDgsQG_TqdQJEq2SMWE22goP8RLy1KQO6nvzc_bmc9N0FRSrfOGxO1i37Ex9heIkvhU_UTCEBsUSVfFKjVoUamFXMgzbU2TCi7LBkss5NM1Q-MbGZcQsQE-gAVPiSlUqoAD5TdNPA204hDXh6Li8ooXIAt2C6Bxmj0QpSRNzJPUdX2--hKeZMDNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇮🇷
🇮🇷
هواداران خانم خوزستانی در بازی اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105167" target="_blank">📅 14:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105166">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c2e01cdc.mp4?token=KJxSZLIXh4HPDpmiLHsbSaxfGpXampvYfk5FCnlBu6RLROebhm1VGNkIequ8ecLRQgUyH61KC5saISE6ZExu3LEuxpGmWsjhQVXgXNUQfYvf3HLaqLZXEKsDaOpwO_FPUXqX2q8xJtGGxsJC26svgALjlbxUSXtJxOTPU4XxuD_-vPTM0gpII3Il7AYCOhe-XsFTo3hI9Yj49jIq3x5M9es8Nw4zWQUsGR90KMlP2JCpB98cvgbVDwvcNzs1Q3G9int1reUZ3stEKW3kyCpotuCPuUI2RNAA8wO9VmJrlXlYPUFa4IOT-2UIZwm727QozN81SAnGHsSs6QKx7o5fKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c2e01cdc.mp4?token=KJxSZLIXh4HPDpmiLHsbSaxfGpXampvYfk5FCnlBu6RLROebhm1VGNkIequ8ecLRQgUyH61KC5saISE6ZExu3LEuxpGmWsjhQVXgXNUQfYvf3HLaqLZXEKsDaOpwO_FPUXqX2q8xJtGGxsJC26svgALjlbxUSXtJxOTPU4XxuD_-vPTM0gpII3Il7AYCOhe-XsFTo3hI9Yj49jIq3x5M9es8Nw4zWQUsGR90KMlP2JCpB98cvgbVDwvcNzs1Q3G9int1reUZ3stEKW3kyCpotuCPuUI2RNAA8wO9VmJrlXlYPUFa4IOT-2UIZwm727QozN81SAnGHsSs6QKx7o5fKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها‌ ایرانی که میتونیم بگیم خوشبخت شده همین همسر جان‌سینا بزرگوار هست. چه عشق و حالی میکنه ناموسا
😢
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105166" target="_blank">📅 14:02 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
