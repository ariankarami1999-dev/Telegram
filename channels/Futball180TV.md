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
<img src="https://cdn5.telesco.pe/file/tRDeUf4nd-Hd2dQli_4ieI5g3K2y7QIDthao4l0wpJEiRhAPgQmfqD0tQpclN2B8KMteoXTmcIFCWwQ3rYFWJX7kBPaSpOyUIuWt1xLsSkYi6DTpx1W6gLgcJbY5Y314h_tjhRgvrwLW8mdkmYD2gChVXAN0XDwEWnH7NgMQ9HeNCnwwsAw3xWG6f1jBCyCtu37CDRltWicqak5h0aLXisJdgJ-C8jLcOAaOUyd0kYAONl5x354HcM6ejViEfo-jH3w9Wz4Xi8IGvmySLS-aZobiSoomXW_wlsTVkTK8pIvarPN2p7so0LG1kkgZrnAJamWvjI8gTaRJUvlreJ7mXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 526K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 17:54:16</div>
<hr>

<div class="tg-post" id="msg-102005">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8T0-m3-l_47fWziFMWHtMvtcAR6O7hoOSBXkZqsUJfEjHipSMULu-hRUMdy19PgiiqPxKlPwNk_uUsOnrV7sXbdoZwWbv7jimu2BP7D4_SVEhZWZA3hlk5sSx29udpBVfZX9xvCXrt3cxCxS0p9f1dCRLIl5X-MoV5OjcmN3XwOqdLZ1-TULp9oHgVN9jZD3ZFLDTMGoVvzzHigzVoEP6wGHh7x0HOnUqQ4PYNYPjpj3l-5D6iBq7DlQ2E00IBLTGrDvQTspHCjkL7urO1-yON78CyJwPrYlNrqLKoLZOYGUMV1JJgzQB5TrrsawBSigDzvbKhNTQPcfTgo5YYCLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🇪🇸
رقبای احتمالی رئال‌مادرید در سید یک UCL که با دو تیم از این تیم‌های در تصویر بازی میکنه
🇮🇹
اینتر
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🇩🇪
بایرن‌مونیخ
🇫🇷
پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/102005" target="_blank">📅 17:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102004">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aeu3x3LqecIwWT5CJHUg1J-s-O0Z_08mobO6ZZM7BhAj0zefduRprtXOccwn-plaR8zEw8ubMX8VH61-_8MJm_vyAWCnC2QBpTNxPkbKGmTa8UIzoD4_bwPKRM7NLMeZfZ4EbKK9T5C75dNvwzYkKEtf5F1Wv9n64YFZ0Eh3bzX83VqR6dtmtJ7UshprpkyFuXGEuuCXvITRQbIO-GD6SbRpGEOwYDo9WhymSxvM8lrk_PSTB3jhFXAztOS7VY3kmOfDTRDJ7TiovZ6aU1caShm76FWXmfvMV8YEQKjEmM94DHt54nuZN4oNcs2nrbMON9UhW05ZJYmKAppLUPRITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
متئو مورتو:
فولام قصد دارد یک پیشنهاد بزرگ به رئال مادرید برای جذب گونزالو گارسیا ارائه دهد. آربلوا می‌خواهد او را به تیم خود بیاورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/102004" target="_blank">📅 17:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102003">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYTjPaOmIPquHLUJGz5qNnMC5n-y5mUOjOzdUBNFSc8arN9gmBi2mfoFgnh84ocRgUoW16D3LCyBkDIcX-ox-bGNcyjZnaTBYIrZlaagEmdMAIxXKPS7boHiZKYzemVyFU6tDtVieARS2v-uB_TZ2JXOsG9NQjQqIWwu41t1IMXbaxpnC_8bqsU4kdLd5hix8Ham7vVqD3-D7NCrPguaPhUU4SwfUzGHZPT45geQR59vge3YuISUsY2PYhEErYg1rllHNV2YrfwmYl7_4RBJgDfQIJqsLh0QG4Mpc0-2nylt679yiRGNdCEG7emy6L7dVPVNcTLnEEAq5ezEOz_ulg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سانتی اونا:
باشگاه الریان قطر پیشنهاد خود برای جذب جیدون سانچو ارائه کرد
باشگاه قطری در تلاش است تا وینگر انگلیسی را متقاعد کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/Futball180TV/102003" target="_blank">📅 17:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102001">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🏅
فوری؛ لینک پخش زنده بازی پرسپولیس و پیرامیدز مصر گذاشته شد
💬
@squadify_ir</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/Futball180TV/102001" target="_blank">📅 17:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102000">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=rcAVThDAyXT1yIy4rjoackv0hfVqOAWKpDbDEdg4dgqsh1sOWrZxcStyBUPH3O7ODSuq20-k_Z0h9qhtwujZwtWOcRhc8zIAyTcuL4lrt0BEUvEzA64SHTl0nu6DQDoicTSE5Pfat-px_iJIcIzwsTyY2Jb7l3GAJwv7ANXub2ionw0YpdhwEa3SyY6TKaJI1VjgcHYeFdZayL_3fhHI0V68GYnqXdkerlm-bI4YBs50Zm5V1alAqnXXGlScNOa38ZA2p5bXoQ1k8BN9ghe4PmmCMRQjAi17g07u8jOfvDqTN6ghOzbZRloGjiPP0Fr3T3BKdH1aj2LEB5Tvecz5eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=rcAVThDAyXT1yIy4rjoackv0hfVqOAWKpDbDEdg4dgqsh1sOWrZxcStyBUPH3O7ODSuq20-k_Z0h9qhtwujZwtWOcRhc8zIAyTcuL4lrt0BEUvEzA64SHTl0nu6DQDoicTSE5Pfat-px_iJIcIzwsTyY2Jb7l3GAJwv7ANXub2ionw0YpdhwEa3SyY6TKaJI1VjgcHYeFdZayL_3fhHI0V68GYnqXdkerlm-bI4YBs50Zm5V1alAqnXXGlScNOa38ZA2p5bXoQ1k8BN9ghe4PmmCMRQjAi17g07u8jOfvDqTN6ghOzbZRloGjiPP0Fr3T3BKdH1aj2LEB5Tvecz5eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
آنتونی جاشوا، قهرمان سابق بوکس سنگین وزن جهان، از آهنگ سیاوش قمیشی برای آهنگ ورود خودش استفاده کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/Futball180TV/102000" target="_blank">📅 17:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101999">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=Ha5UTnkC93OXRQ-DqbtW1aMn3qvpwxXAo1NY1sNg8sqZg3Pz4yW4UsTpFtEC8AwmpH0yEy6G9ZFvhOeVYIjcDK6bxBhwzVor0qzco8CWLWRhBEyDOIo185Kb4dKxQpH2GT0xUF-f6zXGZKb1M5iUvf6v3YCC66oltJdDk6eVof1dP6g869gxdM_5koSVwuR36zI6MGJkYZ8L4Oaj7XpgXJgTwHYi2Jxb5wwnOMY633_jWbUeBP7JBE7gmDk9o1G0eVn7aenlNMQaniD5aUYzbyYJBDD_y3lawC29JveOlU3DVGYyb0a0vrRvdICHBaNNNtsgcUt5Iaj-6T-1EIcsAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=Ha5UTnkC93OXRQ-DqbtW1aMn3qvpwxXAo1NY1sNg8sqZg3Pz4yW4UsTpFtEC8AwmpH0yEy6G9ZFvhOeVYIjcDK6bxBhwzVor0qzco8CWLWRhBEyDOIo185Kb4dKxQpH2GT0xUF-f6zXGZKb1M5iUvf6v3YCC66oltJdDk6eVof1dP6g869gxdM_5koSVwuR36zI6MGJkYZ8L4Oaj7XpgXJgTwHYi2Jxb5wwnOMY633_jWbUeBP7JBE7gmDk9o1G0eVn7aenlNMQaniD5aUYzbyYJBDD_y3lawC29JveOlU3DVGYyb0a0vrRvdICHBaNNNtsgcUt5Iaj-6T-1EIcsAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
قلنج‌گیر معروف ایرانی که با درودافای مملکت ویدیو میگرفت توسط پلیس بازداشت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101999" target="_blank">📅 16:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101998">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a860d22dd.mp4?token=YTFs1ga8mOOWX2hR-qtbHiQaoL2m-MoNb97gR4e5aXRoHpq1UyvTxV8N9Mx_WGSb2OuQPd_7DzQ_Eks3LrjoGD_QHBN3fRIbU-RN9pMtYS7yTLjV2YGKblqqhAZmm01PCvl5vQARYSg0OBpwNCbjCcsKHzb4Ot-ai8Jl-kBFhgTImNZKqDQPYPlyay7NSZ7OSeYMNxZ757b_jrt3LTjB_CWRxzmqEhf13ucue-S4im8o68XVDxIu0IOyyQ3wTaTbi3wtaSVxVhxp7Sv7z9cGsaknL7FQ6hNStdJm5LpeiKP34X0KwDCyF9bofZ-WSlskXwWctPl2E4ufaaEVrZIUaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a860d22dd.mp4?token=YTFs1ga8mOOWX2hR-qtbHiQaoL2m-MoNb97gR4e5aXRoHpq1UyvTxV8N9Mx_WGSb2OuQPd_7DzQ_Eks3LrjoGD_QHBN3fRIbU-RN9pMtYS7yTLjV2YGKblqqhAZmm01PCvl5vQARYSg0OBpwNCbjCcsKHzb4Ot-ai8Jl-kBFhgTImNZKqDQPYPlyay7NSZ7OSeYMNxZ757b_jrt3LTjB_CWRxzmqEhf13ucue-S4im8o68XVDxIu0IOyyQ3wTaTbi3wtaSVxVhxp7Sv7z9cGsaknL7FQ6hNStdJm5LpeiKP34X0KwDCyF9bofZ-WSlskXwWctPl2E4ufaaEVrZIUaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
اسلحه به دست منتظر آمریکایی‌ها
صداوسیما: مردم بندر جاسک به صورت خودش با اسلحه در ساحل قدم میزنند و در انتظار ورود نیروهای آمریکایی هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/101998" target="_blank">📅 16:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101997">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABp-pRvAxC9MfXrpuRZ_Yoo3p3FXoRok4mP0oGP7kKFdT7CrmRNqdzyVwZongLv95toTghQWfAPXPUW8uIVdenzZR1WeU0fI64THI-zA-rvyh9L_sexaqKKQ0fNS0SR8TgDVtb7CWLvEESFP4bstqnDz3KAwNUNRK60lcfYq6xzATUOq53CClkwXn4wYOVRdy0dZ1lDrC03HF1VH4ro-2o-PPf4VPAIF8rGnC43hBwSw8DsbU8E4HsAc9dKbSxi8MzSZDRD0JdR4WpkbsLo2fZ_dUw5bVfeVBXRCnDI8Spu0qpVPGQ7G-bahO4n2AHyqzSChBvzhIJNzG3uhxbtUQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنانی که با همسر یا پارتنر هم‌تیمی‌هاشون وارد رابطه شدن:
🇦🇷
مائورو ایکاردی و همسر مکسی لوپز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان تری و دوست‌دختر وین بریج
🇩🇪
مسوت اوزیل و دوست‌دختر کریستیان لِل
😀
تیبو کورتوا و دوست‌دختر کوین دی‌بروینه
👀
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/101997" target="_blank">📅 16:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101996">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58250e2a71.mp4?token=GBshSmjeV4PYubMCaplOfvWid7iNU-N_B9iFMqXKVGb8dPDA43Ks5CSF6PlMc4g7909P4tMA3CGAbwF6x4QP-PKM3S4hJKMEfsA3YXgjqRQnxUf4hjWHh0_rwfHmQm-8eSRszH0LfB1RU-imSWwoEjmTdt0Q70jabG482CSCUryQOfgACFUd5v1Z6ppF4BHhBGQCrJ1xQ_Vti4CYxvua8kLf9rRvtKwwnUpkRukGFmyqB1qhkGjOeYozBcbFahW_NHa0GvFuBalZcKKp6Blm8TnD3xc8zpRyfi6dagOL5LDvVdY-n6eUe6-QXdhsZfL6gKno-hCgkvKgQWmW14o0jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58250e2a71.mp4?token=GBshSmjeV4PYubMCaplOfvWid7iNU-N_B9iFMqXKVGb8dPDA43Ks5CSF6PlMc4g7909P4tMA3CGAbwF6x4QP-PKM3S4hJKMEfsA3YXgjqRQnxUf4hjWHh0_rwfHmQm-8eSRszH0LfB1RU-imSWwoEjmTdt0Q70jabG482CSCUryQOfgACFUd5v1Z6ppF4BHhBGQCrJ1xQ_Vti4CYxvua8kLf9rRvtKwwnUpkRukGFmyqB1qhkGjOeYozBcbFahW_NHa0GvFuBalZcKKp6Blm8TnD3xc8zpRyfi6dagOL5LDvVdY-n6eUe6-QXdhsZfL6gKno-hCgkvKgQWmW14o0jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🎙
علی علیپور: حتی خود پرتغالی‌ها هم کیروش رو گردن نمی‌گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/101996" target="_blank">📅 15:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101995">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4Qi7qBDCosFh9mQDSgLEVG46ZPfLyniBSxV65GvYdqKrYVlZodmwuGgBeTPXiJVCn0ri9EOoi5K-k--esPw92VlU9sc2CiuV_3GDSW5AkPhapy6lUHDnjiASwz54vi72m3gfyjQmt90JLF11ZCpcFBjjkiUtIIJo-VpqohctZjzUzq-apegTfuZ-9YuDYDfscbX4BFPx0b5-6kXtQuKx8y4oJiCyrP0eG7svtAHx1ffWXJ3iXDOZPm60_zlHElIj-n8PlnP3XW6jdjSj2DKzOcojZ3wMN0tUfwPa5RvoMg_kU4jGiPNHlYdE_6goDRFC994heCZnff43_0wB6ItGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📉
می‌دونستید؟ فقط چند هفته قبل از جام جهانی، اینس گارسیا، دوست‌دختر لامین یامال، حدود
۲۵ هزار
فالوور در اینستاگرام داشت. از زمانی که با لامین وارد رابطه شده، تعداد دنبال‌کننده‌هایش به
۴ میلیون نفر
رسیده است. فقط در روز فینال جام جهانی هم حدود
۱.۵ میلیون
فالوور به دست آورد. همین رشد انفجاری باعث شده چندین برند بزرگ برای همکاری تبلیغاتی سراغش بروند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/101995" target="_blank">📅 15:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101994">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🔴
فوری از رومانو: لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/101994" target="_blank">📅 15:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101993">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZnE2pk8xWfK8kaX1EUhJxXjaFdzzCvaXZhWlo7UrULxUEoPd3XMxlMYXw7DPjqH0yryv1HPIsJY8DTbzJ4eH4VLz8tSZVjIbcFFswFIEW5ngY_44KuS45pz9qkPCPjfiU-V292VaxQL_qqT5yP7WnjONzyJWtqlaH0o_Emtf5Hk-wXGYj__oTVbdq3ufOzBm8r_mFsOvEtSvgsexVmoRFEBi2EW-f-NNIzQqRSwRkV751EQsDG_cZK9aIWD2sY-jI_BQNmxzqxmmEMmV4qoFnRK_Mo8IOiLS-TaHV9-BnqlGWa2PmShTBULP-ruFNiGkBE-dSesgKnLQ3I6k7jLqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فوری از رومانو:
لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/101993" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101992">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45e9d378eb.mp4?token=Zx4z_I_QaQRpEqemvT-zEO7CIpyT6oHuQk3i3105fRggopLN6tXN_D0LNdRCAJsTPLaFjVbLPEr3u3n7uVlCjl9KxC0dUlVTsg0ZS-zB3CHMEvKL65Wxl-7p6Ne6D2sYOWSM3muW_onSZwOXEvsNv4m-FA0HZuJgCA9_VorQOwV_r6k1qIsRs2qNPKhif2JnUsLWptvf2v5ygXyx7wpMv5Q0wLDwF-TKUPX_aP8IjgJ-9QASPpmjd-RWN1lGtvijpmbq_tCFjkjMuj3vVrmV1zlkTWTAHx61EF49hoDL0rzwM9DsEfjkGhfkrN2L8xyjEteb3k7YBOZU1OiNTzV1YC4r8kea-dzDDUtMe3GhVg4ANqxlZBh9qLsBetfNkuapLiQkVh7q2_RnKprPDEbxZeFSMomceF8kwlBOT6lIVfVzAL0R5ES7yM8Y6sR4DLxe3XIA2lx7byqW0IoWSHpMVYfjwVbZY_pS3Fy-6WuQ5Xqm0nfQrytqgf9lDHNwMwgcy50oJSCSZtwDxNT5wVc-XmfhIS2y7FQOjmk59tNMsREkU5m6EUP-K5gQMuAv83gGa1_psYdtr8kv4EeIlNmzHNDM6tR_LczZOfjQysQ5DcnnSpltjZKQvfMgX70JahX_PE5DrIjaTdGvibbSt7alL5m6xnXA2SFSbR1Z_awDX-U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45e9d378eb.mp4?token=Zx4z_I_QaQRpEqemvT-zEO7CIpyT6oHuQk3i3105fRggopLN6tXN_D0LNdRCAJsTPLaFjVbLPEr3u3n7uVlCjl9KxC0dUlVTsg0ZS-zB3CHMEvKL65Wxl-7p6Ne6D2sYOWSM3muW_onSZwOXEvsNv4m-FA0HZuJgCA9_VorQOwV_r6k1qIsRs2qNPKhif2JnUsLWptvf2v5ygXyx7wpMv5Q0wLDwF-TKUPX_aP8IjgJ-9QASPpmjd-RWN1lGtvijpmbq_tCFjkjMuj3vVrmV1zlkTWTAHx61EF49hoDL0rzwM9DsEfjkGhfkrN2L8xyjEteb3k7YBOZU1OiNTzV1YC4r8kea-dzDDUtMe3GhVg4ANqxlZBh9qLsBetfNkuapLiQkVh7q2_RnKprPDEbxZeFSMomceF8kwlBOT6lIVfVzAL0R5ES7yM8Y6sR4DLxe3XIA2lx7byqW0IoWSHpMVYfjwVbZY_pS3Fy-6WuQ5Xqm0nfQrytqgf9lDHNwMwgcy50oJSCSZtwDxNT5wVc-XmfhIS2y7FQOjmk59tNMsREkU5m6EUP-K5gQMuAv83gGa1_psYdtr8kv4EeIlNmzHNDM6tR_LczZOfjQysQ5DcnnSpltjZKQvfMgX70JahX_PE5DrIjaTdGvibbSt7alL5m6xnXA2SFSbR1Z_awDX-U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظات خنده‌دار از زنده‌یاد اکبر عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/101992" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101991">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d63baf35c4.mp4?token=fqowHwKHJzDdSFMuW2DST2-RWwL-lbAhOicYnBiwYML6fJnEn-aDLi_JkmPiu5N2eATO3-1nQ_5dyHwq7V8F0y2SaeXvL_7w9oCTnMtjxObF_UX7YkyirmZZ38moMS-8OsrfYxPnwqMjumAKyFaRDXME2evT_eSQK3IZ2yPl1UiY4H3i7p3N4LJ_wP8FN0WeOZi8cv2E2-QibXVFCcMMXES9_JDgDdskPjyLU3--HJFqU7gFgZyMR4Feuoi7oFeAhP8jJN8BL1HXXw3xhj3OxBMhIPCoKlGAH88oRVF-F0WU2qFprhDW58hx-8pEXYGAOXAEXJ7Fx26S9vOfugjJTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d63baf35c4.mp4?token=fqowHwKHJzDdSFMuW2DST2-RWwL-lbAhOicYnBiwYML6fJnEn-aDLi_JkmPiu5N2eATO3-1nQ_5dyHwq7V8F0y2SaeXvL_7w9oCTnMtjxObF_UX7YkyirmZZ38moMS-8OsrfYxPnwqMjumAKyFaRDXME2evT_eSQK3IZ2yPl1UiY4H3i7p3N4LJ_wP8FN0WeOZi8cv2E2-QibXVFCcMMXES9_JDgDdskPjyLU3--HJFqU7gFgZyMR4Feuoi7oFeAhP8jJN8BL1HXXw3xhj3OxBMhIPCoKlGAH88oRVF-F0WU2qFprhDW58hx-8pEXYGAOXAEXJ7Fx26S9vOfugjJTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
دستاورد دیگه تیم‌ملی در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/101991" target="_blank">📅 14:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101989">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmD6Qk8V2gG-pD0ClVilVwV04PY7XZ7wE1iV5aOOckLY_MPwOa3tvyNbYYGlGZrHkHaPiJ7Bn8PF3w2bcKYyaf-zdYMd03mANFJStqY2Di_kmvBSV34H46274NXbPSq3-twu4c5vdGHF-8geU3dyyNNdJrLInKup05srcL8T3jGdTRHZUqjy2_ip94u_EnzdjmRtdBA86ydOe35B56STmwZQJdFPJBPJpPOAjYba8oVJkOiEtkUBFV6vrL8Tgn2y4FsMSVLSqO77P_b0iSg4Kz7G3s73nidvA2hjbFY_FmOzwMv9vobgN_OsVjjFNGNzp12s4UDb5cYYUn1YPyHYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGA_jezv4vipmckUzCKPoZPRMIlaggerESym9tsewcirkp-pxL4-YIkkcD2aFl2vNDFniF_owAa9IjRMXSr6NTQlDc5T2tXc7-9tDTcn6cmoy3QRnWBUmsVJ1fKnCjUsm7xUIY5rBboN6UFhoLrRT5FUD3QjnGb7rvBRHwU2zg5A6_njwO0vWdX7QQ-ut9-TMMKGNOmWvIW5hyRXF_pxRpmNz6PWaV5k-j94i382AKiHq4N8Le9JdHPe728ZC4MgGISEMSJKYlN46-nxXTy_oka208JhUzitHbGoiJAJY1nukIcEAOn1h6j8SMWp7ne8-KUdW61kfc2wixO_VfpUBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اینس گارسیا، دوست‌دختر جدید لامین یامال به این موضوع که گفته میشد باعث جدایی او و نیکی نیکول شده، واکنش نشون داد:
من به کسی آسیب نمیزنم، چیزی رو از دست کسی نگرفته‌ام؛ فقط دارم زندگی خودمو میکنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101989" target="_blank">📅 14:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101988">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310ebc00ec.mp4?token=H_HMFxGVqIXEFlNoye9rX7UIW2rSD4pNtvkjXqBjzpHLKqf23VMBhvTdXtnnItdy3VMIEeeokNaEx0VS3Abc_fFPF3PuTZ7ri2-j9LIhMtAxGpmfxwiSBCneFxO9XK-jnSh3gKfHveN69jhPUoRaeXGmut1lc5H0JZgCko_cW-LNy2kpf4Wop5cNvxRAHC7rShKexIemSpDxnGye0LkzZYFT4naxiZQgFj0cH1chTa4vnyl-Y2pQL2ftDK1yGpfVAEYVxrQl7lTxzPssUNfq9_F6k6aNhR42p1nU-gnbeeRShbE9vJpLCrlXF6C6LMB2UhCPYNJAsIJVJITLe8Dt3SI1EdBlPVRXrARGrxKNzgeZ3LmJipO04veYfjavJONFCW4sztI-JGUPCfhOpEm1tAr7duOfpNRWG3dbKibQaCydebLU0SF6smoD6z9VVBIEiLWHqj_i2PtHxnQDCV7f2YBvG_LM-hz686xITJnaAysJnrKZnCiCogcN7sRbKSN4oUuemaiTs0KZiQ-nwIPcydkZqI6cBPFAP3jxH60Dt0YkESggoviU7hUcrewHcIqsSM9iBXrR-0W0jvb_7V72c9J-DUMhTeL8SCPniJnTTNx5m8V8Cpr0vPUyKqlWTCaMANn2QGI56dG3wNgutLAC3Bug9MHTqp3oMPKW3MgFR38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310ebc00ec.mp4?token=H_HMFxGVqIXEFlNoye9rX7UIW2rSD4pNtvkjXqBjzpHLKqf23VMBhvTdXtnnItdy3VMIEeeokNaEx0VS3Abc_fFPF3PuTZ7ri2-j9LIhMtAxGpmfxwiSBCneFxO9XK-jnSh3gKfHveN69jhPUoRaeXGmut1lc5H0JZgCko_cW-LNy2kpf4Wop5cNvxRAHC7rShKexIemSpDxnGye0LkzZYFT4naxiZQgFj0cH1chTa4vnyl-Y2pQL2ftDK1yGpfVAEYVxrQl7lTxzPssUNfq9_F6k6aNhR42p1nU-gnbeeRShbE9vJpLCrlXF6C6LMB2UhCPYNJAsIJVJITLe8Dt3SI1EdBlPVRXrARGrxKNzgeZ3LmJipO04veYfjavJONFCW4sztI-JGUPCfhOpEm1tAr7duOfpNRWG3dbKibQaCydebLU0SF6smoD6z9VVBIEiLWHqj_i2PtHxnQDCV7f2YBvG_LM-hz686xITJnaAysJnrKZnCiCogcN7sRbKSN4oUuemaiTs0KZiQ-nwIPcydkZqI6cBPFAP3jxH60Dt0YkESggoviU7hUcrewHcIqsSM9iBXrR-0W0jvb_7V72c9J-DUMhTeL8SCPniJnTTNx5m8V8Cpr0vPUyKqlWTCaMANn2QGI56dG3wNgutLAC3Bug9MHTqp3oMPKW3MgFR38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
چنتا سوپرگل نامزد پوشکاش ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101988" target="_blank">📅 14:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101986">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KrHqV0Tg68Un3shsf_WJkWdaM9zgKeJrcGgWQggleuV6pSWHZc4yFHBnSSEIlVAuNawgRCXCRxjb89MkcJhf0qdqdQxDtJ-gLZLNK4E0GISkD-yMmwYgYRxQiwabAPAEOc3kO99VFfa-A76XenDHTfIUGHBf5ZjOtJWAYUXvNrFaSi8ToPOwHMq3uz9fBkprwoGGeM4SQZluWMe03pLWfmsEgJCwsiggBnjYV1gG11W5GznhRnmRJ6JmBEgVu5HgtHHUvaxoUg2F27TpdI8BIZNSbp13Lm_Y1p6MSwUm67urw9ddU5hGJpMkekm466aNl_GFzv1Ytv3F5mgaCfH5yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uialL1mv6dUXR2_hWVGJEUci8y2wRm-b78GTXyUKSn6MFmNsJQ_asxsqkIFPYmGIJeb5eY5wqznPf-ZXrOYhzlpi9dDxGp3xNoCNyXFFHLydeb7PdPwQegxVOmdUkALgvnX4icJDQnR1r91loefS6qfk0C9_cnhzTrGDWhgxhfxEYJsrsN08lKSGUFU7iypbZRmKJaaUzPFWXOmZF1hn7wq6bBO0HbO-samXmMyGUcbNQz3vw9ZC4MocIq-EDftk-RRhabKCCsRLqkjTna2R6BU7LuwIOEW-YdeY4lRmKupTach-lhoZ5OhevkCXtVdqpExCjorTL6VO3TwhaMA01w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تاریخچه رابطه‌‌های لامین یامال:
• 2022 — سینگل
• 2023 — آلیسا
🇷🇺
• 2024 — الکس پادیلا
🇪🇸
• 2025 — فاطی واسکز
🇪🇸
• 2025 — کلاودیا باول
🇪🇸
• 2025 — نیکی نیکول
🇦🇷
• 2026 — اینس گارسیا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101986" target="_blank">📅 13:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101984">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CjzplorUJdOOeL3o-seugnWW1WsTP83233W5YuDO2P43MSRE_n1r_r-0tAou42RE2m0KRLtX4N1HPeGF-vMls6RBP_qETS_nrpJ0lTqbtTdQOlEjYNE086Gbsfs5zzmd_ylaG3MqPIvSR9hXC6xoD7XDf9a4d6QgvRYNb5vqIENEJV3BQzg9gx2QoO5GyoeRgr2CXyToIWy5kWZqG5wFyyiVgCv_qrEUbrBwFQdPPhLqBJRFgfl0eZ6YLhybA5PM8hh2eR0D1a6VnDTRcyPKqkta7wniK1zx-dhqIyzSKZmtWrs3xN8daN_YARHyq7JQYk5M4eTNnKKfjBZTkgGFGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QEo4Q1luxdVPcb1LBbhh2AJPmDr5DYt_M_kGELCvhnff8dKPlPXA42bXw31WRwT175gGLBiGEyXYzVvU1ymW7V5RdHPrum32Va6B5RrKZa-j_65vntPhPL3lfC8w-XN3RUd7hX0vNJ8uhsLRaUzx2q5WzS1DgR6I-JoKPwoHgqNa-DnN_3bRPJO2uqHvrKP2uYt6MVtddCiIj7NONfgA44gWjAXV7ZDS1LwGpWP7V6KC7zKm_eNqzd469bP4lWtJyvI8tnZVg8a0XizHcdKCkwBwBiWGm_0sGLTrwXcufAaui85ok62CKAHimfdpYQ5LpbqCrGbGy1TN9ioDYo9TPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
جسیکا توگا دوست‌دختر سابق وینیسیوس جونیور:
این فوتبالیست‌های سیاه‌پوست فقط از نژادپرستی شکایت میکنن ولی همیشه با زنان سفیدپوست و بلوند وارد رابطه میشن. اونا هیچ‌وقت با یک زن سیاه‌پوست وارد رابطه نمیشن یا چنین رابطه‌ای رو علنی نمیکنن دلیلش چیه؟ جوابش واضح و مشخصه! خواهشا این سیاه‌پوستا فاز آدمای اخلاق‌مدار رو برندارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101984" target="_blank">📅 13:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101983">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
په‌په‌آلوارز: دیومانده به رئال‌مادرید تا 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101983" target="_blank">📅 13:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101982">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgAGmWD0E5qLy7cmqgUfVKo3ukMbsBO1PWvpyI-0xTSQSPqho_J2GGdJ1DAvFTXUGGVurpFrpMbyHFsbR922xugLrZH1Q9U7EdOIsPaKtEFSw9BluxOl2TCnhIRR4NQ7mn4s0I9LAB-tlWxix1ZJ7qNcGw5VBOG3KU9PZX4_sOPLcJl3Lvolvd5o7Df2GXsNLxh35XmLBJIX_vaHBX9_bUuCVdwpPKs4Zw98WxSahd0V8gvTp0e0GNtp3uvJFweLYHrP3P5ZIti1oReliKRfnSUwJMF6cnZjCyTTQ-_-ZcDvHP9zkU4hWPS5rz4-P9cbeZ914xEvSIObipNkagBQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
په‌په‌آلوارز: دیومانده به رئال‌مادرید تا 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101982" target="_blank">📅 13:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101980">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBfnNlwfE45wA3FmY5xxLhY4kJuAGMsg5niM6c6cFbLZRMKxhQuBr_JGi0OVB4J4urfwLsH7GodsGZqIwgJflBl8q86VjCVvkoDIKMZ1Zq3VD9TW67Do6f15VT1ZpEDRrUCeLzrFm6IwADQ1FwxcMebfjIdP8J6VEULadY3UlLRcT8t7okyBPu9vVFpAyPoLjr_8TllnR6Ow4tD_JUhDtRHAs61vvv04U8DQzienVnVZGBK5WB2JWIGlhS2sOudtfD2qjET19p9U7_rdHGAICJETFxwaaHsPILOhLmVmfgp2XIdylDi6ShRbnyo4tWRv4JTlw2_pBm1hM6UO6oIl9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/huL3Q6923qsMMBJ8BicWid2P_O1AtKEFPzf_B_K3VYYMhM0qJPa4hg7BCf9zm-BNON2pywNQcsp1OH6n-i7Jqbxe_HPWa4TyjKBjsFF0pnL_BWVZS8lqiBvVJY0cZTzb8Xr63ryOyLXKNgUVpd5kXvOujvJmyf4MINUSDUNDi46Uk3QQXa05j_I67toVzZONEwd8P6L6_MxyT_4N_WfGVSkp8BRpYKG2juaqO73JwUbfW7pDaKSRyVjH8itkxG2l-BNbXl1PiQEPavPP6jyi_fNxUQsxmKSm51is0yx73nlpgtrZlomDYnjLyKTryldHX9tBeK5dg7oHLMIVtKIFoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📅
🔵
17 سال پیش توی همچین روزی بارسلونا 46 میلیون یورو + اتوئو رو به اینتر داد تا زلاتان رو از اینتر جذب کنه.
🔵
🔺
فصل بعد اینتر تونست با حضور اتوئو یکی از موفق ترین فصلای فوتبالی تاریخشو رقم بزنه:
🏆
سری‌آ
🏆
لیگ قهرمانان اروپا
🏆
کوپا ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101980" target="_blank">📅 13:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101978">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5VImra185rPqPT8zjEXlew8NlKZQVtG79R_gbWqyXDwggSRlLl7IeyB4WNRtcrmd25pSjwrJJMnteWTqQwplkIprxmlv2pJeU056w6ftma254Q8foBAnYJMI82scJnqT-jlZHZv1mGLZZcSmnkHRxcRZgmmrfem8Plo6kbw2fNaXP7Y3jdJFvnmSBdLd6nApznu9X6bnV10_Ty4DUqb3bnK2TtmGu4vsHMFwdty3JF4wWQiUZQkfVtLYZXoq6H2VVuqMap0n7YHuObrIMdSzT-S-cDjVu3jBiR6VNIMXpAFGaRIjjS-NUYw8E4Sv4A44gTftVWVSahLwAirJCQsgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OgHMHm5LcXif8AyQaL9reNii9RvURDneJB4xKdkJqsGdjkcuC5Y3FTydkDs89_i-sJW_SR8VOMBLzEHnQhRY0W8JP1RM5l5ap6xPxDGoKpgbKJfukRJAxUAGGmHuDOf60euRoRK0-nPrqu8T5PWIJjmg3_U0P91MFR-Oa7B7VaTmyeeV7wDdwzHEeEK12iFNp6ltAU7wFScEy_agQoCI6PdiPzdOrR7ZEg-dnx56-NvSf9mTpH1qvFujF0P_K4aHHE3-dEXIvUaf-P70SdZMtauwxhTiys4-S5P_BKCOT59ZN3m-_9m5Q2hvTNSzglNuJJyB0thzDEHnCari_aJHVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
الساندرو نستا درباره غیبت ایتالیا در سه جام جهانی متوالی:
باورنکردنیه! پسرم تقریبا ۱۸ سالشه و هیچ‌وقت ندیده ایتالیا توی جام جهانی بازی کنه. وقتی بهش میگم ما واقعا جام جهانی رو بردیم، تقریبا باورش نمیشه. میگه: واقعا؟ برای نسل بچه‌های امروز، دیدن ایتالیا در جام جهانی انگار داستانی از یک دوران خیلی دور و گذشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101978" target="_blank">📅 12:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101977">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LONdZmcpaEUPLsyGAY0wJOAzDwnlcYauBuTo8_4JQlCFr9pAt1SLCkTTuXV5Z5kxB7OPobTtJmHVsbE8kwE2MCROY1EciC_gG-hkMU9J8bKG7uCqjcBN3SI-ngmt4q8nUzGPg1vDJ2VKgbKMamUlyepms0QVjWBwD0wxov4gbxQwktiA9YEcShBt0oRILzfxXT1qVcoZqK6MkIYMTBZFqLkApgVwHp5q6K-xSnD0JxRyKjriPSJmt5aEwfqVYWqRwkxOwaKMGcGvhsOgQwgVnPQH1TfHZ9FVb1-ka-JYHWkzQmrZvNsyGBCk2No96n4mL2eAntRMPG4Yek5OiCky6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
ترکیب آرسنال اگه همه شایعات نقل و انتقالاتی به واقعیت تبدیل بشن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101977" target="_blank">📅 12:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101976">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKgkDaKvEYeRHrCTmvFXpUUakjUge5VkcxevSTvVoZmvYJTgCb9Bu7Hs2XpN3UKldu5TTYfHRuhM4bjpmVl4hZ_zwpHKmGMm6JHNw8pjmb60iMdQU2WrNkFFgvOuNFHNLmlUceuPxiiOJ6S8bc-8yNDqCGbS_qD51uFRvRPWRLIEIJkVv_qFSw9JbksFDCg5jIgz8h6viISWVgoW-vkt8rz1kbBidI1vY3VE1SAWXwPMaoStR9NnI6yOz68ulG8xTQbJT4s-Q4kQ0UJXHg9G49HVLEGQdK2R6WI4vs92pMaR4smSpwsnqk1Rn0c-fAki2m0M8AQf_g6S8WlxsGKp7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
طبق گزارش‌ها، بدهی‌های النصر عربستان به حدود ۱ میلیارد دلار نزدیک شده و همین موضوع توانایی این باشگاه برای جذب بازیکنان جدید را محدود کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101976" target="_blank">📅 12:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101975">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ddfc2f853.mp4?token=SibjIRTN1zTqTxZOlZBe_jiSUUmjfO3dKbh5F8PZLlSiGNbEJqUkpPcPj3Y_zIh4nbjknVXMYof3aTuUvfUCfyR1X9PSaQPXyiNav4m8_eOhSdXdRXu452bWc1SuaQl9g3ETGJHh1p3FrGJk1ce8PbQhmnNaEglM0x3N8CvP3iaAPK9q_LxMYBgM7nxg8kieeRzRSVjQTDrPW7bxDYiAhlLjom__GPA172x0VExJFhZF-SjfMj4hJdlM5bskravgB1HFHOoCkrwSbAM9sy2PgrC2HoIo-exncuuooyPqxDLuDt06f8Wu9FL0Ag2qiK8839pVvYjRjh9Rx9VzKGJdEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ddfc2f853.mp4?token=SibjIRTN1zTqTxZOlZBe_jiSUUmjfO3dKbh5F8PZLlSiGNbEJqUkpPcPj3Y_zIh4nbjknVXMYof3aTuUvfUCfyR1X9PSaQPXyiNav4m8_eOhSdXdRXu452bWc1SuaQl9g3ETGJHh1p3FrGJk1ce8PbQhmnNaEglM0x3N8CvP3iaAPK9q_LxMYBgM7nxg8kieeRzRSVjQTDrPW7bxDYiAhlLjom__GPA172x0VExJFhZF-SjfMj4hJdlM5bskravgB1HFHOoCkrwSbAM9sy2PgrC2HoIo-exncuuooyPqxDLuDt06f8Wu9FL0Ag2qiK8839pVvYjRjh9Rx9VzKGJdEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خارکسده جزیره برا ایرانه
✔️
خارک و سه‌جزیره برا ایرانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101975" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101974">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQKOf5FU7lefFbkO7zNLX9gLwl5kSLymyloe1D8ic-URvtjmtM_0eygfjLcQZ2ZHF_J-0X4FTTAFjtFYrynUzEkvVpLP8A41y3m04QtQESC6atQN6uFDmaZAEotyjWfj7tD5DUFmzX-cM_VwiVL9lDN5pndxolmxBCMRnpMNQuZ4ZzVnpBGpoGvQrv6Kn1WUHlM6BkIG6208qT84owZOZ4w3t6_P3EDq0I2tQi4xwGEQDfyTd50TSj6mfTsF0xmti0tBiUuUVvZGA3PkCbimBt-S6zxEuMwuJ98RG7HZtu2crMSelw_h3LVnD_hTInxHItaY9gO2eW_9wPh76hkSTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انزو و خانواده تو تعطیلات
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101974" target="_blank">📅 11:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101973">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjTmAyITjBqGQ50_WlM1hmLZMDU0oluGOGn4Nva7nJetVUCkZmCQe-ZNUF3lKLSNsWs3J0B6X5GIVU-Qj9kD0s4uoUBPHOYP2ZXg5pm_t4oKMi3Sf1Umuzk4wwrL_9XiFXrJoPOAS1dLZZkDXcPojRJVJzhS1p2uEzrQozQYufgsEGPAjm0g9XYZYrxOyyoAuLZwZ0PlR6uomVMY0NyNd6hLdrr3Bj1onJsHKgTzhY-xXugz7zqxAiaMJYnnaIsOaOxGdkyH6ZbGhxRIj2puXmfbS_pUVSbi04_I8xHyMp5yVmkM3RsCiNGr4SuMWtO2MUXAbpTEHcNOHCsxCF9x6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
‼️
مانوئل نویر:
🔺
هرگز آن لحظه را فراموش نمی‌کنم. مسی بواتنگ رو رد کرد و درست جلوی من گل زد.
🔺
بعد از مسابقه، بواتنگ شوکه شده بود و گواردیولا به او گفت: «احساس گناه نکن، این کاری است که مسی با همه می‌کند.» سپس به ما گفت: «حتی اگر صد سال هم مربیگری کنم، دیگر هرگز مربی بازیکنی مثل او نخواهم شد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101973" target="_blank">📅 11:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101972">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c941f7e49.mp4?token=Las1kMFL2aWkWml6xKSP2Z70HFhJtYmJN9OpMCBjCPrvnS_h1qQHLX78gZvaWCUeB7zoN-5ddTFYH6MXRfOt6geJWZVc7wk0PzlXscQVPRKApgTHZjos5r7waD_4Ba38sial1pIy5LgZoCsJ7mcDHICFRuzGfX0FNqojQ9WHy6nAAD8WctCOPVX0IDlkvEYeqfq-A8V3t0iKoPUUsxJ3AYT0lp6lhEULonKjbW7ORFDlU-G1N9ERRchFJgqXIqP18QkfQqzpeTatrpy1dko_Ux7Z20P4FwrOJsMNDb1VQ0z1hygs1TQbNGBVSBTI4QOiKe6RlzcYtaysotn4BZPgIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c941f7e49.mp4?token=Las1kMFL2aWkWml6xKSP2Z70HFhJtYmJN9OpMCBjCPrvnS_h1qQHLX78gZvaWCUeB7zoN-5ddTFYH6MXRfOt6geJWZVc7wk0PzlXscQVPRKApgTHZjos5r7waD_4Ba38sial1pIy5LgZoCsJ7mcDHICFRuzGfX0FNqojQ9WHy6nAAD8WctCOPVX0IDlkvEYeqfq-A8V3t0iKoPUUsxJ3AYT0lp6lhEULonKjbW7ORFDlU-G1N9ERRchFJgqXIqP18QkfQqzpeTatrpy1dko_Ux7Z20P4FwrOJsMNDb1VQ0z1hygs1TQbNGBVSBTI4QOiKe6RlzcYtaysotn4BZPgIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیوزلندیا اینطوری از بازیکنای تاتنهام استقبال کردن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101972" target="_blank">📅 10:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101970">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dk3ZjxUHvNjavd6GhPggt80-vtwP5gX6by-zs-LkGteoKDcm7LDhVtTgE2SGj-Zg7etqKeRVjXMSV7FDgeNabXK0gucnFUzU6cEn9mGSgb25ziiDK_gTiidh-YuZJC9Bbmxwf2yx6u3gK0mBOSXFMJYTuM0Bgtc1qVawEJZz9N-T3M-3BqHZUycWHypLCWUYKEyW04UjeZpOMISTU1edGoriFlsh5qs22F6L5CUmKgIRpbKTfYjPI7Ek9DNaGT7WkthdsNUj3fNDn9cPsgjaZwLCn8e4dIwyagKDq1uIRqgM44ywdfobOu5HJi7bHE-DoZtEv6Um7P8fFv5V_uTkwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/viXOTRu5jdHJnqiGEJQPt9gBFcH1u4d7t1AEIF-C1VIJvfln3x9gUn2_oIaI1frnc8XovIX7GzOQvTr4Pn6e1W6LiutNwt2_7DZrqMnVx1WX0LSRu_omEA7mKDhjGkw1wz8hdnmVZb2T5uMZiRfD5iFDm6qn7re5pcn2w1kIsst8pXcXcyVTqQcaE5kDpUHzVM-2PZ0KCdnIwu536guCApgtZY8-3mnqjwIspPLD1CVR5V_tB_o2u5VwNWYlzO9fkSSSdx8V8XC5mW8JFTqTObtEHCOJRThrh11yS9HjZn3btP90vuOP4Eg_fV2uxCtxQ3qnvloFf1a0uJD6jrxXoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پدری داره تعطیلاتش رو اینجوری تو اسنپ چت میگذرونه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101970" target="_blank">📅 10:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101968">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ifSpFeQDi6vyX_7SDenGFukBXcZCUbD7lI5PyXhFPUI9_I1b13ZQxEKAlLgzmTDatqXnn9fTCX3iTQHWCdWzSttreO_gQJhsvqMgRGp_PbxGHEAJU5WMEsXG5LoTyWcTFRFxOCdYTKsqAfINqFsDqZrB4i5MYwZOPbtF0fVwH_UloIrlwIXgIAcz6BCk6YRyNMnYgY9F2qq8-wmgw_g5PYXqkzVDd5Enfuwgme6XEj3MOhb5HJDVRYUCOIWCdm8Wr4N-IP8nyQmB7yECYqKnPed3pONWnHgMRfJcXGgDzp1_kBDFJDJ9KcE44CzL5Gok30RuNigDCqs4V3SoCW_1bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTPi-38ol_8TAoVc8BKQQf6Mk7VL-C3Rj33Mbzg3YcIv9lbrbHaIBtUuwInSSIndpPBPmDrd6TjZUM6EFmTxphqSll7gDqnZ6z367wW83adDtXx739JwDRa-4PXZ1v_1esOs919SezwyiNFhqDwzREGgylV24Liopstdg1Kr2J2flBSBgA2cmPvM7-tS9GgYH4sXJpGv2Zhn0n88yfOJc1cxHyd-hHhKccip-v9l7kzKKnF7Zgmexc6mQfDsS_MjcbM6ln89rSbsiwAULlinepYoiV3nAs8qxJHE1XETJCxxHrhAxLJ6-3tsf-eTS40wf64BN0eqsjpJUKLvqgpy7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
😞
میگن نیکولاس پپه بعد کات کردن با اکسش تیانا ترامپ ( پ.ورن استار ) الانم داره با لانا رودز وارد رابطه میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101968" target="_blank">📅 10:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101967">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMiCH2TCtkoApRf6gQSDvwbjBO9sIuUa__wLqOZtjPbtW2RnhDFTcpY6bHBk61bo7pShdNMldmKWyjkk_9fp_KDDBqOGC9kYKt4twI1ypZUX2SWTsN3ZgPG_QLLerVHmtgL65USiWnaEGhvYU6srCK8qaCpTYl6SETuYwzXauCCSvuXgedSrEtRdrMFuaJ-LbMfXuf294Nav20pI_ZopvK0peTfYJoM5uOwZivCZrs0hnPj19DWGwebTk9DF7B3n_GRtV6bRkHjr1FvrSd8Y4MuqEYcRI_f9WwmXq4u4z39t3j5Rbk4ekYjHv0mgoZByNcIFSqUm5QCfsoBBmOo9fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
موندودپورتیوو:
اگر بارسلونا نتواند خولیان آلوارز را جذب کند، دیگر هیچ مهاجم نوکی هم نخواهد خرید. بعد از جذب آنتونی گوردون و کریم آدیمی، مدیران باشگاه احساس نمیکنند نیازی فوری به خرید مهاجم داشته باشند و معتقدند فصل آینده فران تورس، دنی اولمو و رافینیا هم می‌توانند در نوک خط حمله بازی کنند.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101967" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101966">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaauBu-VB59IrA-yODnrgRgj6hWtTvJF8TEGwSNBwcblLHlI1h65pjD147liXmVumIf6ViLyEE2xYj9GArwFZRcaQ1ATUC8SxtjEq802zOJiWX5LkE9JDDqcT1FO5opsLO4t42-cSH2-tMWkVOKTwOdo4uuM7o_kmg_ICavHpDbhMx3tVTpL3o7t7bq4GXrcdR31Y4eq3ueBN6WdYgxawXphwrB82p6eYFEH2wokcYKhkBIm1WWmarnc4zqQrTzW0aLyfnZpDEx-6KtQoRJk-g83wkeCoau9BKqQMiXrisRvZ36hoA-WbIFRP3KFSXfqYaEeIHTJNVyHrDFia0K62g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
–
فابریزو رومانو:
⚪️
در ساعات آینده، باشگاه رئال مادرید یک پیشنهاد جدید به باشگاه لایپزیگ برای جذب دیومانده ارسال خواهد کرد.
🔻
این پیشنهاد از 100 میلیون یورو بیشتر خواهد بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101966" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101964">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RBapGYXbH3I-dsqEOi_9zGQZk_AIgjOeJB_Q9nTqE27BEwbUinwigQixw6dJPdEpmS46jFTrVPa5RSzovmX3pxZxUiO5R6MeBNC-WGmmFxBMAZjccF9n6fnLP66GanDJgdnF7H5Sqw8x0TG69_TUr_2cv03v6NjOrM_CzUWWpb6ly1lWQXrdwIpExv-QuvNc6uMK6KutyZIHXDNcA2WYpebJhwb8WCKUpqQA92R1oAmUSFnBwfHAOfQoijiUML-dUdCB5T2kuLtBWKK5bydB_EmP_zlqJAbNrFCYC3TL-0oMyzkLiA0Hj8_kslb-D8oqUVGtIrTv5VS0bVNHWFWeIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DZq5ss6RAvY8I878NDcSzXh4prlVzZRQw_Yf4nWqomCobrSoGqY_CxsrpE9QOs0hjci50XMp5zyVJ9-iWHrPQXKrUywrL8V70YKDEmCo-vaaNAxP1DuJQk9_OZBand6HxiMT474TD7Y8J1A1QN7CijJAR-civhKtugene-VxUC1Tj7RjK4xoYZtzZN-1aNa4fO8zivDGs5ERhJ85NeGmh3p6vak45ewUcscfauR6MqbhrRivIO0VkM8uwRr10yN4eEjYPvRUSBYhP_s0mNn11PxhLoOMzVHBe1kXTG4aEcLNAgaJzcAvI9tgaa3iRGFpty0LYQ0SQ5BLl0qc9pPclA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
سوفیا رین شایعه‌ای مبنی بر اینکه حاضره شبی رو با کیلیان امباپه، آقای گل جام جهانی، بگذرونه رد کرد: من هیچ‌وقت با امباپه شب رو نمی‌گذرونم. هنوز باکره‌ام و خودم رو برای همسر آینده‌ام نگه داشته‌ام!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101964" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101963">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7DDqU2xJxNjGS0c2jA80ItM7_CuJ84JDM98rwwhMRkZA_MKjzqtxLI9WLyoQYb78lEtUP7VhvLxHSNV12mwVNU2m1ggs-hjoR9rmFNZNMp56gK_AIt7vbG-r8WrRvmnIwXSQr1PJ2GNOIV5d_8ji-0pJVciqzcdGqKb7jEqKU99bJuEC7WZUP6MXGTzSRrt9Pmzgg8LbSbvk5svlbwMO_jTJFp5bXCQfrVAMLbbHBERPTJa8QyyZNnuxTv1reXJ6vd7tUxBVlOye_jy-6a6i3udDKDbEXIdKQiOnyFLrNrQEDhlUQsf5lvoyQJmrOjOWtiuXDo0kB-6ZXJ0JZjKSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رونالدوی برزیلی درباره کریستیانو رونالدو:
فکر میکنم بازیکن‌های خیلی کمی مثل او از بدنشان مراقبت می‌کنند و این‌قدر اشتیاق پیشرفت دارند. من تمرین میکردم چون مجبور بودم، اما او تمرین میکند چون عاشقش است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101963" target="_blank">📅 09:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101962">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0d0985c7.mp4?token=oH2kDm212imOZF9d5dz6ZyssFTHAkHdSmmcK306XCnudY8DIy7zupr-yXn9RJZvAX8-JsHx2fAOVwj_dqoTYxUyIAlLgzAX49aJUpF_ZcWnw9azTi-JPG_BNrL-Z-z6QgF1_zNs2mal99KjnXN3DMXJZ_Msl6LfmcRXHqMcxaG7y2-hpTra_mJjzCIM7N0RW2tdd94m_DToKOvR_fHTG3DRsMIdog00qXBZsikW1vG6XzlX7aWBlSI-MOx8FTX9OFEz_bbkgn-kVk5GS4ikPpqRM27eG3OIm6xCXUddlrlVUykL2zrYy9dykeAO_eWBaElKGgBofOp9hraPXVkSDPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0d0985c7.mp4?token=oH2kDm212imOZF9d5dz6ZyssFTHAkHdSmmcK306XCnudY8DIy7zupr-yXn9RJZvAX8-JsHx2fAOVwj_dqoTYxUyIAlLgzAX49aJUpF_ZcWnw9azTi-JPG_BNrL-Z-z6QgF1_zNs2mal99KjnXN3DMXJZ_Msl6LfmcRXHqMcxaG7y2-hpTra_mJjzCIM7N0RW2tdd94m_DToKOvR_fHTG3DRsMIdog00qXBZsikW1vG6XzlX7aWBlSI-MOx8FTX9OFEz_bbkgn-kVk5GS4ikPpqRM27eG3OIm6xCXUddlrlVUykL2zrYy9dykeAO_eWBaElKGgBofOp9hraPXVkSDPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚡️
بخشی از گفتگوی جذاب بکهام، زیدان و زلاتان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101962" target="_blank">📅 09:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101960">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tyU3KIie7xPDL-jrw5kb5oDplwi2TpRgnJNJ9WUIckTsgsTz0Il07L6vMB6VpzRsVYbpZh069iCtc9v_u6Zu-c5vvH9Ij3vqfLnLMDEBdgqr67-MwsaW9c1gpyDbgc1GnrTcQ4b2XE3zJ9NiectDZdQHk2AV-I8TYQE6vejgB8B9_vQjNLiR_E9ebZWwECAIY9FoNJE83o08XPZC0tDo3q9kaJcBRvjkwVWbsubWcus362wm9C4Qas5WOD_0h-0lsVrGOQXSKeJNCXEH-VlSmKPW58IKRkBl75FT7QLyvLv-R_PP5jFihlRaz3Ra32hbOvPaU2EDE7PTmlzR6ub83w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WzCp1Ch7sRMiuvGlPj32fUL75U5uD8t9UW_1ZPRNI40SFYJGBONhiKvsyFABe0RslF_zGW4WDHrrhdBHwzrDtXaYEL9r3KNpHFZEMtI6iTI0yktjFylmMMGxaVatf0NonY61zwkK6XfZk0iZpg8XUd_lq_yo17WUwhclKWGTDBHq-4XkIcxPe2ZkRnea51FAj5mdk-jB63eELXKEUGn0kT3Ax3-ruGK87ZwWMBdZTc7WlBYhl-5eSE0EvzM9xDM-wgZFXxmJc-M81cK16VJJG2n_5XJNPzHIMgFClcyRDumCuC754DDEo_cThi_KwEer1U4n_2EzVB-qLrkJgG_rjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریستیانو و جورجینا قراره ۱ آگوست با هم ازدواج کنن بالاخره. تبریک به این دو نوگل دیرشکفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101960" target="_blank">📅 07:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101959">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YETGVfDKMHUbLeD6v14pkrLVol1ZwRM6s53daTHLdyv8hZkkxdx3ZFQ3UaLU9ERDTlkOuO4Qzd6keQ9iuOJ_9M-EYADdyOmAOde7H2glE3ITsYGUYPGAyAoEoWNSgzLyVI12vINl54L1qfaXuEgrD2tsOpsSzajl0eZgFLl4y-Ts-bF0-bOfsmOjQyXLLSGZSNcPdTWv07Pg38xmgq6zbGOhhuoLLHjGw8trKZ0TggTSfUXdaBCzqBw8yyNlLZla2ZR1B7pMnPShNnapljJggopPRZ8tlX3xxT8QFRx__xsXn9sPLaejW4wb_ZyPUHAHxxSzEO-EojxT8O52dCMWCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👑
موندو:
تعجب نکنید ولی احتمالش زیاده که لاپورتا پرونده نقل و انتقالات بارسلونا رو بدون جذب مهاجم ببنده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101959" target="_blank">📅 06:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101958">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85d2fa751b.mp4?token=hvHeS5-YhcZXmGeUtSoTOq_54kv4S0hW7DfKURIrSIIRgH0OJTwvRisewzjeQ7nyYs_E8ZOgjWskYSZ_P9ZMdXPzh-W_1-BeZYde4pUPLkdaH-9hI3Z_kJ_Oo7P8-6j4UkemzHVsychLVogV2mvBklwrPjhOx7ezOlXVEKfroj28xjBNJR9ObFozsHx-SCUaTGEZ7tffKy3oLKOF9hJhH3-IeRZZ_gySa0ZYcRgjyNdVWSc80dwgqU-7pTrd-1E--32j_sEPuYUKvdDkLfBvIASOlZx9vt-Tm55MHLFq7-X0m58n6Fwh6lum8iG7C9mq7ltC7oy-trHiq8eCMS9BuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85d2fa751b.mp4?token=hvHeS5-YhcZXmGeUtSoTOq_54kv4S0hW7DfKURIrSIIRgH0OJTwvRisewzjeQ7nyYs_E8ZOgjWskYSZ_P9ZMdXPzh-W_1-BeZYde4pUPLkdaH-9hI3Z_kJ_Oo7P8-6j4UkemzHVsychLVogV2mvBklwrPjhOx7ezOlXVEKfroj28xjBNJR9ObFozsHx-SCUaTGEZ7tffKy3oLKOF9hJhH3-IeRZZ_gySa0ZYcRgjyNdVWSc80dwgqU-7pTrd-1E--32j_sEPuYUKvdDkLfBvIASOlZx9vt-Tm55MHLFq7-X0m58n6Fwh6lum8iG7C9mq7ltC7oy-trHiq8eCMS9BuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
نیمار تو اولین بازیش بعد از جام‌جهانی با دبلش کون سانتوس رو مجددا نجات داد و با نمره 9.4 بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101958" target="_blank">📅 06:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101955">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXWVcXEb78TGA7H7S_jc5_A6l1yM0gLFGLQC3qz89WbaQE0AqjZ7pxR_F8iU6mCOB-0QE4h-_Tw4D0_GXVp04LohVHTCG3BwTXmA0AFXmZ5ujUSAeXZtfDME87sANrAYl0MwMjGZaaVLLVj9MCctdEBo82pVgWO-xF-B4eyaYbPGEz58keZg3uhW2otqzh1yDQJfhsyn_3eBD2_hfbIF8U68KLcg7cy3q1mPV9eokvejZN9OHk6EWALfE8Ian2NYQSqTuYe0UGZr3EukwNofU1kAjdGyFcNSbpLB36k0rxp-FtfV0yNXt8uZ1RxlDGJZUJJBapcusS2EC3zdmmGXkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gx_oDIsBQt9_u8qwqTSITnGqCctAlQ8-nI-YnlRPaahp6cHRLOddhOZKmerM7MFcf7uFZ_QixPK0xEpQ9ZdfRnYjnk-Yan_huy0Aod1HN4y1AJOb7Qrv7_YZ3OHJmxhBydMyugm5nwiLNMoEyPVqXyF7pbAwEbDwqX9SugmLoAdNP3nORvo_quD783vwLMZeN4HDJ0FKfIdRBOK1JQlW0qnU4LaupkcvbB4bVPY94e4N9QF3HFyyTMyq8NTnunk49Y7yPodyNnd0stnrzdOlU17HIJU97uqOceVxsI_YBWCZ44wUZtFQm9kfBNaQ8wyHCFH-tHnEhFXTSauFpZcMXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953a60dfac.mp4?token=Q-leYCd1fSawmTRGJRKoWlwtIgxy8A3KdxMf557yFRVly_He8y4rrQkTSatxUXMr9lBxrtmciPI_uloAhbl3h-euo7N_oiHJKaBpGs-v4TtfMs4G1P__q1quJX5gzm-LiEHFnrdHRna_KRaoY9ZSJLRNj2j1AwXis31np5xSIVFpDehwjOHPXt3_qa_r8dgO2HZoIxA1R1ptLe7QlatcApwlvKl_0xsrDi_1KuWiJ9n_brFZInKkOAL3xC7FQ8zDt1LkGFo9vg9i4S-dR6tdKhKbACZhcsPhQ31i_5HRckRphCBeUy0Se4rQbOkNdRv7v1ejwiLtgtGvvdH9yABuqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953a60dfac.mp4?token=Q-leYCd1fSawmTRGJRKoWlwtIgxy8A3KdxMf557yFRVly_He8y4rrQkTSatxUXMr9lBxrtmciPI_uloAhbl3h-euo7N_oiHJKaBpGs-v4TtfMs4G1P__q1quJX5gzm-LiEHFnrdHRna_KRaoY9ZSJLRNj2j1AwXis31np5xSIVFpDehwjOHPXt3_qa_r8dgO2HZoIxA1R1ptLe7QlatcApwlvKl_0xsrDi_1KuWiJ9n_brFZInKkOAL3xC7FQ8zDt1LkGFo9vg9i4S-dR6tdKhKbACZhcsPhQ31i_5HRckRphCBeUy0Se4rQbOkNdRv7v1ejwiLtgtGvvdH9yABuqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
نیمار تو اولین بازیش بعد از جام‌جهانی با دبلش کون سانتوس رو مجددا نجات داد و با نمره 9.4 بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101955" target="_blank">📅 06:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101954">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMhu3IvJZ6TL2vLgS6xdQGJVR-o5qYkrtYPsCz9K-Qwqkk7CNQloQpuY_7c68xYMZLuGVgFAFmhyppp_D8lNvYWrU_xY0B2DZA3jgVWHAIAw8yVoQXgdnd7bvfJKSZ-fsyeQdyzdNYuG0VCzNxYUvQ8KX-Tf223amYE9gf0t3dmm1IzCjuM_2-TZEbkSmQbQwPrXnXFi2v3qlbPEDYlDPdYCXfSNu_A5skOTPgec-gfTwrlhnjuXVB9WfJjZTx7xuB8QRDkUE34RJ1E5bmuQMHvoAbg2TiHJjFCvlFs_T1wqj6yquZtv5rQk-OAh2ffj8g6jzMAMT1FwAsf-AAAwyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
مسی امروز اینجوری تو روزاریو شکار شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/101954" target="_blank">📅 01:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101953">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44643cb150.mp4?token=SpQoi2w9TpKb-pSuqkyb9CEJ-3LpC2dZg6-sH11m6vwW6IvXKp2YmC3jo_2RmioeMyndh9dLxJleaGj2Sn90KRF8UTDbjmicXRuinFDl6xtyRh9ydpo9r8uc2TpH04H5unqBzGbfkI5TWO_LdJaCoyw_M-wGYP39cun4sfq_KHnQjmF3lnqrwdV86B-diC9BsBAe_Iwjf6M7Wj54Lwm-e1hmoKBDI2gYaADtJaI1qy1xWws6OIeTF4wmt7o18bRzz0BsPU_QlES9rNbSSvK8Nw9QG67RBxLVc1HdwwdLsOmW_GVwySv9UV_AbGS8tCeibe_eyXT7VUARGse78zyu31rwu6K38vJ3loaDD8eyK2QWerOnDdmWPVSvc6w7tCihVOtzOGmh-8dskW1Qevw3lCXGbAITTO28hS1VncLYwDabyIlDcBp5lvrrvUMw0w-_D7MFboSQfjvqKT9uxzH0BGDbzQ5G-rNaFtV85ds68tiKOQdGVazm5yhD_8shp6HyrJLeWpPn-7UYP7mbARKKlniQIipjJsYCAjpDnk37_9K_srbMxJlKsD__RU7ahNI1bfsdlgRcYf-aPZReq3j61IujOvwO90vhvRFFX62_z1b_VauIBUbOtjjopH_jZOW7L9qt46rj-YPbNK_5lYgKZqM-l_IAk_f62zM2B8JcmF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44643cb150.mp4?token=SpQoi2w9TpKb-pSuqkyb9CEJ-3LpC2dZg6-sH11m6vwW6IvXKp2YmC3jo_2RmioeMyndh9dLxJleaGj2Sn90KRF8UTDbjmicXRuinFDl6xtyRh9ydpo9r8uc2TpH04H5unqBzGbfkI5TWO_LdJaCoyw_M-wGYP39cun4sfq_KHnQjmF3lnqrwdV86B-diC9BsBAe_Iwjf6M7Wj54Lwm-e1hmoKBDI2gYaADtJaI1qy1xWws6OIeTF4wmt7o18bRzz0BsPU_QlES9rNbSSvK8Nw9QG67RBxLVc1HdwwdLsOmW_GVwySv9UV_AbGS8tCeibe_eyXT7VUARGse78zyu31rwu6K38vJ3loaDD8eyK2QWerOnDdmWPVSvc6w7tCihVOtzOGmh-8dskW1Qevw3lCXGbAITTO28hS1VncLYwDabyIlDcBp5lvrrvUMw0w-_D7MFboSQfjvqKT9uxzH0BGDbzQ5G-rNaFtV85ds68tiKOQdGVazm5yhD_8shp6HyrJLeWpPn-7UYP7mbARKKlniQIipjJsYCAjpDnk37_9K_srbMxJlKsD__RU7ahNI1bfsdlgRcYf-aPZReq3j61IujOvwO90vhvRFFX62_z1b_VauIBUbOtjjopH_jZOW7L9qt46rj-YPbNK_5lYgKZqM-l_IAk_f62zM2B8JcmF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لوکاس هرناندز: «کیلیان، اگه قرار بود یه تتو بزنی، چی انتخاب می‌کردی؟
🔺
کیلیان امباپه:
فکر نمیکنم هیچ‌وقت تتو بزنم. دوست دارم مردم من رو به خاطر کاری که توی زمین انجام دادم به یاد بیارن، نه به خاطر تتوهایی که روی بدنم دارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101953" target="_blank">📅 01:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101952">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRXZmpqtEDS3ZloMdGXANJh29Yvtuvu2Nb6Tybr_sDS-MFRqLfcs_Lqhb4EcGxaZLcnxZrkI8kVeaCFsLCaMTdep8FX4UckN3bmDMznDOlYw2WD-U1paK_JT5qVLkYHSj9YOq7PUkbrGtRB5oELO62hVm3YwNLjkCn-AtBrE_M_e1Tyx6kXng26USr9AaZlIymKOWam2Br0IOsUOAyjZmomerKfX3mEIYGp67oXsNFZi2bd_ks8Se--6Avt5spbHqyjglWoFJ7gYTFE6xa4FVQ-A0ly5FlTl2wsksBcZ--yg5bRRpnw75lfdi8ctthPP5L2zcIejY3rHKkGVMnpwPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
امباپه و پارتنرش بانو اکسپوزیتو‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101952" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101951">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmyADtsAfEsQvxnbT0eEj5LxhHoLzslbggAPq-3fecjNEeQaXKdzQLSgZiGLBSO744z8f7edyu9KcKa6wGtyAvCpPjX8JP8XlK8_YpRqFK56ac5oKQLRPxS33r8EBvRDY53hYeSYMTI45z0pBe7toLs8etXCoYmoTcz5Otruw0pelNIrWvGKpEqdyE57NzdcPp7EBq7SVx9YETX1LqBiigMINLGhdvweJW_MYHagOye7c3c897pdNZtgODPSnX-qFP2Tt2HiFc1ADI-dw9h103BL6dg5g78P56Qc7vxSsgUmTV-MAnMoznuvQJewNutWNfAW9ti4vN1xIFOdGtqQKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینی خوشتیپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101951" target="_blank">📅 00:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101950">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63dd42dc4d.mp4?token=Z4p0SpqqzCIxtsyXxypOVel9BjDLJ5u3PlIWD7JhNGEtUo-3q-6FIUAmqheGyS3GLBrYo6ehYovPntsTwW6oIYqKjnZVVaMK5KdMQ-YphE669SdgAFNEpw2zo6LuNbWc2fjXVjdO_NLndM_s_Lj8WAoGNjKk_vEYeesIzcPvHkI1vgZKUjD8u6F7vWCo7W8yEZM0XUWcjstGwGqwnFdypgoHhCl6HnBJIjN1NpDyCbGDyRI8l-8G8ANTVQ1D4SnTEsfngB2sW_8kkrYjNXQufL0y5IgR9_yyo_v9GU5WTvsjhx40HkB3DVwr17Hxyg9hZ_NLFnZx8VwkQoBjFACGiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63dd42dc4d.mp4?token=Z4p0SpqqzCIxtsyXxypOVel9BjDLJ5u3PlIWD7JhNGEtUo-3q-6FIUAmqheGyS3GLBrYo6ehYovPntsTwW6oIYqKjnZVVaMK5KdMQ-YphE669SdgAFNEpw2zo6LuNbWc2fjXVjdO_NLndM_s_Lj8WAoGNjKk_vEYeesIzcPvHkI1vgZKUjD8u6F7vWCo7W8yEZM0XUWcjstGwGqwnFdypgoHhCl6HnBJIjN1NpDyCbGDyRI8l-8G8ANTVQ1D4SnTEsfngB2sW_8kkrYjNXQufL0y5IgR9_yyo_v9GU5WTvsjhx40HkB3DVwr17Hxyg9hZ_NLFnZx8VwkQoBjFACGiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ری‌اکشن هالند به میم هایی که ازش ساختن.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/101950" target="_blank">📅 00:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101949">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8PqW72NY3VBer5XpgINkS0OGIqKSIoVrUYgAECOsGaofGMaSctMjYjadGlgLHaZJ-azmk7zigGzX9seVN0eUodJwhBd_SjyXUr2Ldr890VEK4JtquI8KFedTlj0onWTph8IkGHmSNor_iF_FPSoQ-HyminnVbGrHB_LhGXJaQBxUci7A5UZuO6ts2MBstCLGuZLavJJngHDkNbQyGSh8nPfU99pfACBonz3Ej33K8uzOjMgHo4qXDgzE5HsGtCoEVnSXtixVNwSAYuRNI8aoZpF8tQehl4AUz4-51DopWVIS8MUghsq12KtBpiY_FEtjzhVAq6kE-J8zqL3SR_n9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو: رئال مادرید و دیومانده بر سر قرارداد 5 ساله تا سال 2031 به توافق رسیدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101949" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101948">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iase3SUsnKF9pZK9CAR4mKw_WjXGXUqZfqs4NgEtpIga0eNdR-E7hRC2icmNbIhijB0sOZ6owOb1J9tkdSse_fQeIpIMIhAxCnS-nAAvVUSVAJCPoUmUtFmC-hVP78U9TanAMoFFzRHL5STJH5KzQX-QiWJeNww-M8yTyaJUP84DcFbR7bbwu9-KPfCx1OmQhu2KJK1oMtdjahrBRmLf5iuVfIiSVBRjTxlnjMngd73Ly89VTkQWdRhhy52Q8o1m1sHANTUK-Muf4Av9ONVtRNaVmwz7LkHsmPi-exwU5QeQGACMyuLUBrmKd9lXp7HrrOqRD_PZUI4_7Au03taVWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔹
ساشا تاوليری: باشگاه الهلال میخواد مبلغی در حدود 120 الی 150 میلیون دلار برای جذب لوئیز دیاز هزینه کنه! اونا بودجه 350 میلیون دلاری برای نقل و انتقالات کنار گذاشتن و این تازه آغاز کار اوناست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101948" target="_blank">📅 23:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101946">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fj2jLjQTB8BAbMknf3BnvQ1HwnN4wFmcVTz7FQHvfszlArE0fE0O4MyETzoRCRbFoyV7lS4ScDv2XezmAXNYkByTmjo_OxCmpN6R8WxWV1VnCwG8IW9m_A8B0Zp3wvVld_btEpE8ovtbznRErSvLXZUzCoor0BQJvec1ytAs1_pH71ZMGakOnydz7YPNtpsjuyqkpp_9PDclBYiTRp_yiG_LEcgAiXfGXuMCm0M_MyHmVEQacrKheFD3VW3LKp9TQfEJmNMaRifISpZxcdA2HtbL13W2U-Cq72pVERMVqd2-jemfx3Q_xtj1j-WWxSaRrVusNBTE5GKEAuLvvjnBjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GIKUiVkg-nBAtrOrl-xkkim1iYVli_jEg1CDqO4P2cFe8ion9jZJPGK0xCUYE_q94EgWMvlsBY6TBVv1mefWDVetYhK2OI8EnflmyrM2bAlSPZBzeCWI6uirS5xSD64vefwA68u-SIApCg_FBcc6oxA2skDAwJuWCnCZ8N6hfEP53Ewp0WHz61MioOE6gRA3puQ9hTWt-gD3rlMOHoe7z9sPJiL18uPjIYoMFEriaxPLsmW9lZc4TuUen9RnnMfQEx4RPWdoSOr9-98uGBLiuu_M2m6PPfDfiLByLz9o73AbToGAC4djfrlWsi77K4FEcStz0UYL2UF2GgE5jfXsHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
سرخیو راموس درباره اینکه بین کریستیانو رونالدو و لیونل مسی کدام را انتخاب میکند:
برای من جواب این بحث خیلی ساده است؛ اگر فردا فینال داشته باشم و فقط بتوانم یکی را انتخاب کنم، کریستیانو رونالدو را برمی‌دارم. مسی لحظات جادویی خلق میکند که کمتر کسی قادر به انجامش است، اما کریستیانو این حس را به تو می‌دهد که فرقی نمیکند بازی چطور پیش برود، بالاخره راهی برای بردن پیدا میکند. چیزی که بیشتر از همه تحسینش می‌کنم همین است. استعداد یک چیز است، اما در اوج فشار درخشیدن چیز دیگری. وقتی کریستیانو در تیم تو باشد، همه تا سوت آخر به برد ایمان دارند، چون او بارها این را ثابت کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101946" target="_blank">📅 23:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101945">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdSRXUeHFLHfSm42UAeEfXi_pixIRQz_HiVBja2x4g5QIpCTZsGNKPTQteS92dn3M8-ijQVKOS5GUj3Ov--X6lmzxCaInOmQzyVqMvcgoG1KjN75iXjyP556qlIVZl-p8IHKionGTX4mr-V2wu-IvOPtZSyCWwu0-NXnhW4Wf1Cjaejb4aTfeO-IXoaAy8iWUKJNg-mmn93hspcb-8RSGl_gBFMc0s-u8Nj5xLwvXYoHJA9uRgdcrVRav2R9VZBIaRlC5_IaHUE1eEMrmytSnU9sqPyMg9PMZjk4UrZAJb7WpzMKrqyhGlN49maj0vY9gin2fQqjy77oQMmK0C3I7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
به نقل از فابریس هاوکینز:
مایکل اولیسه تمایل دارد به رئال مادرید بپیوندد، اما بایرن مونیخ درخواست او را رد کرده است. رئال مادرید تمایلی به درگیری با بایرن ندارد، زیرا رابطه بسیار خوبی بین این دو باشگاه وجود دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101945" target="_blank">📅 23:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101944">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMEzxtJKITcaoaUwMjtBOl91qyEV_w_RPAnZacKMQcpQa0pyq2-021JnB9iu3c0p8HWLp_nZ0hzwleGY2GsfEF8gU91BufcG2MOT6PiwEElVLFrQ0Ta5OrFWD6Iol2w7fa5l0sMRS0OFqlIOsOh2qHCHtsxSB2FV8A8_6X_wwX8wbhyYlbnztcH5rbKghDJfIn_R5B4BvjN_hyo3MH29MncWYSae8cBLExORG2tgs6axQIaYxpQih12x8FAUBSMQUgMLwyxUiG7xFHviQF92g16Z3GLwdFBlSB5tU3gohpyL4k9GZXLYTJ9I0bMo7R9-EVKmeOdXfXxV6NQIL0b8QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو: رئال مادرید و دیومانده بر سر قرارداد 5 ساله تا سال 2031 به توافق رسیدن
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101944" target="_blank">📅 22:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101943">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFLvfnMp_ZzSb-ksco28JdTzobhN1Qm_Uw2qBUCO1u9LqwvTYMRjRGClGHZW1hw4LrxJFZcoE_pv0TV7D9y3vuI6ZAQIGt9yjmt3qBWVWrEy1TeOPF_IoGk2-vQk2bqmVnYdya1PWTVo10EaBTjVKgKN1ObpZvEfzFHBPmVAtnFqCD5PM8_GswFfkColsx56ZWtqs8QvurnHF7XoqydNcPk4MiRGtltFFLFGNXOoW8_zyJwpLBDMKyDS2j_ti1pB2V9giVlV713Le7KmYKM60lVhnEyIdJILSAJ1qOTjXLtusMF5hPiTE4O3p1qPFY_pGwB3UtSvpleJVswW18dcbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فابریزیو رومانو:
رئال مادرید و یان دیومانده به‌ صورت رسمی بر سر شرایط شخصی قرارداد به توافق رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101943" target="_blank">📅 22:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101942">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qxl-Nd2vb8Ya9fphejAUbJIRRWnlcyemCHtQ1mvAsvvo55Mj_gIMvouIortVMLuDh5V8Ui4aOVjeD7YAOJEJYvBRU7TJe1UdKQW6LPxmOBZ0MsMjw3oCJhcf-DujOaxWO7MZ1NT6VbJyuW-GWpzSMuyUqpDVFgC7-iy2TUqN2aeQhwZzCJuAG57wnvy-E46oB2cDN270z-OPQ2it3AoY7Tuorbp17nAvJZ4OdOdZSbFvLv9CqNFAHtTuqfLtHR_SnFC6fgBtWjCTJmoGyKTi11G2P5Gfh6KXWjpW46173K6hegdyeCCWnFNaTyDnjL4coNwM6XObjT2Zq74Q5-_clw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👀
ترکیب احتمالی رئال مادرید برای فصل بعد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101942" target="_blank">📅 22:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101941">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5LZk2Pv-3vOaPlDHCOxoCfc1ZuAh-B7K5FR3f5Eg_jZzk5mGbKNXWYtQ-39AI5CO18DzTtdfvqAbcR2TWwoxRS7aFtskyMOxJ3dY8ES8GkK20tpTwlajmp2xoMmEMuFxEZPPB2sCNT3zKQZuX05mgRCqGOOaIpERuAxhfyRhN5T_LHj59mpZbkX_gMT5rruPfLRPyiPVeqSKAeBSAJRZW3UCxBtBorhZlVmmThiUZIX4Ib0majMtuTVqD8fn9vPiEzYq8vok4ujFZLTcddPhRtLGA8flKy8b1uLKIT3tbwjCE3yB24TL0zcHJ7lRdz5xY_MOxfRXFivmNVyP4Cqag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از قشنگترین تصاویر جام جهانی؛ مارک کوکوریا قهرمانی رو در کنار پسرش متئو که مبتلا به اوتیسمه جشن میگیره.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101941" target="_blank">📅 22:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101938">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cn2J9k4jI3P2DiRZ_pBfTxHEbarS7XX6jaMiyTok9RWI3LNyccvCwUIxRuPGo7Gy1DOme9SdcOJTccpxMI4Q7HGfRIOmksEWlfLkk5DLUi3Jd958GfFOxeCnhTiE9dimSk0iG1iiYLpPbmAFkSLXhbMi7xICKttgJTJ28QJ5UwuYgIJMhLjIz9ugYS4HdwMZZAlc8CnBjTD8wHNlRjUbmfYfA0wcvoxunauQimCh-GGmBRqs8eRp4jvKe4wPSRca-fYwLkZYg9JUXY2ImtxZy_dUhInXckXil2UX1BR9aQFqoUEDedi1Ueih_mF_qrdHTfig9Xx6cZlw8M6BkHNxHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CEFIbW1dzXG7bvaHrLKp9fngt810nimXwJHWwprOyaqs1czJPBuFmbHMhQZx6liSLAOewdyUb600dE_TbX9TC2OndvIVXM5Wvax52Ts1VTfd8MmiuNGaNW4DVIEwv2OzIDjUSqjnmxZTDFq0c-I__1SjpY9dwAwsUO214ZRrbukVoFNg1SVlR8COcsoJUNBl_xdVbGwlw_oDEn8nPuO0RrbNvH_lYkcs-hY5kbbZzGgbZZuNJ3ajI7-9yNYVVa8B9KvV4_t5qoY122hP3DkahHW5okVxjPJ6_I5eV0784UneNl_7FO6iBgrfw-HFv02TOnbrjQDE0qfIzOlBqr0ggQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NR_nKxPxitn9lSfyVGglH2AQquAdl2SS3EcQxhNIG4SxT_k3sh470Jw6ygGze9dMQViDuMjWi_VGL1TwaCyPz-RqkkRI1bWUQlE2vBT6LGe2PSmulZek6AffSX_ug7iruCzARs0RqWmX6DCED42fPewYQic4gsKiSpE5xWZ0IK7mWgCT4v4p-sgBFHYBSOoqg5nbX0hWwExnJdT5C49TNd99PLQlHM9s0RwN9i1D2sqjcqw7gpRrzfX1OVtI9SqOEm4n-cM_u031Z_Wf5gFeglTkSB9RP5m_0o_NoUuM6e-tlZehYWt59YjMy3fu3s5mNHEnHX6ethiJfKuDCLVSWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇳
😆
امروز تو یه حرکت پشم‌ریزون دانشجوهای هندی تو اعتراضاتشون ضد نخست‌وزیر هند، عکس امباپه رو هم آوردن و محتوای بنراشون هم اینا بوده:
«دیکتاتور امباپه شکستِ سیستماتیک را تحمل نمی‌کند. همین حالا استعفا بده!»
«۱۲ سال در قدرت، و تمام چیزی که از مودی(نخست‌وزیر هند) نصیبمان شد، نسخهٔ پرمیوم امباپه بود.»
«دیکتاتور را پیدا کن.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101938" target="_blank">📅 21:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101937">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9GXzX9F1B3MNI_emfeHlLFA3f9rWWM6iWN56P9x0OdyB3GFnn5d-_IUrTU3carSNADSC5AFrsb7_lTiYp6sdjBGZJb2FXZKrYfZHCvYlnMJcSmfXLeCyfRCTZ5jIqh-JFyvYmqDHltJOFwwyiW8KaQhrQNrUkWCTyDabcHkk8JzGqirrx232pzVbN_937Mz41c_cVS5ay3UkS-63u_O9ykM9EXl0IQc7QMNNkZDkFvuQJR6WXa2PDXJfdH07jNnB3bfJadX8GzrwF8UPyjNqurDpfHRpLjFINpFMta2jObJzh9MrgdZge99yrLV4mo3KnPxI5dAUlukrvX5gV7pkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلاتان ابراهیموویچ: "بین این دو باشگاه، این سوال پیش میاد که کدوم یکی احمق‌تره؟ لایپزیگ که پیشنهاد 100 میلیون پوندی رو رد کرد، یا رئال مادرید که 100 میلیون پوند برای این بازیکن معمولی پیشنهاد داد؟"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101937" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101936">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_jtC1GXcYX4M6H0qqh1TSETW-A1ltPE0-epqGkWB7IzLWkieARMFb5NKB2LvAoTFLQlkBh8_QgaBgmq_zkCMAJJJKEe5AEFI5z5VHq6iYeUA9yVyBsPKzdpJampWpcWilTUFmZ4jffQtZWBP_vF2z9Exob1CewzGpfojflw1EJWYz8XF6OhBNp1Lfd_xYaZvtubIc2fsKdOFRNXKkPJVeZqXJLGJzPsBmLgFl26hn2vkSZM0UU9zkQdQ6AlCz59_IY3gFp2Za7rIj_CfnvjG3ENajXYIkWCI4N4jncV7EY-faEAF4QR8CwWXE-8-z-V44yRZ0S93hWEtSlQLGLGuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
محمد خلیفه، گلر جوان و ملی‌پوش آلومینیوم به استقلال
پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101936" target="_blank">📅 21:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101935">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxSx9VtmI9jIiDOr7jH8m3-fWYzbssKsYgFGd07azmtxhu10KV2gK1VMprD6_lfzsmygoVaHePs-VGs_jmT8N8oIUzSpNdIk59Io4Aq8O2fIPgtDCpNfHNSdtgC8ULkUGDyVO3bxWA6xB7Qr-Lyuge0Pco0kMU2M5MhJfybbtKkjMf6bTemU9FhBa9dXAMh0SUMVKoyNMYf2QTO7QauuW72cLRNTvvrlQYirFJQeocKQO_5rRjjWV7_qgHCblcDNUzTSUoCR7ibWBaSw1d1NEG8_Y33psSzrd_sAt68CprkgMZUlFrR2VoWfwwzg018jLhhFM5sfq2NTkCDVLFagRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ماریو بالوتلی:
یه بار زلاتان ابراهیموویچ منو با رافائل لیائو مقایسه کرد، ولی جوری حرف زد که انگار می‌خواست بگه بالوتلی بازیکن خوبی نیست.! منم فقط یه عکس از جام قهرمانی لیگ قهرمانان اروپا استوری کردم و زلاتان رو تگ کردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101935" target="_blank">📅 21:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101934">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMVhVKnO81BicsSWssXttBrH9lyTzKxiKEgl_FzKuseM42f4hSYgSYJeFvVwHwxOcuY8NjydQznhP5u_j0PC-izagptamLH7GJH2UC6hGdjRgMw3Qq4afHcYsU6U7Pc2EUwgjHy3K966Cnchc4Yz3IPAISDd9BquSFEEOkzBc-0ncY9LZPPHJAL55_OuK0G4XlfSnoWAbAjUs6SVJ4CjpU5kgjc0QWnMU42FQ_UfTi_AME4S0ntFizEIN2z9GoxrCnwPvHhShJlBdE84wlcEgE_Rar_sPZ8MvL75R_7CmGPGQD-fJdvp1NhhBMZSxQehrVegENfkeDFg_4afkshwpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
کریستوف فرویند مدیر ورزشی بایرن مونیخ:
اولیسه به رئال مادرید؟ این موضوع اصلا برای ما مطرح نیست. او این فصل هم نقش مهمی در بایرن مونیخ ایفا خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101934" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101932">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UT_BgA12uPkUDGirWhJ0tiUS-BXQA3fvQKHkMwwOY2DcCirWv9IB7lc34lPQ25-sZuRI8WmoFMLtsYvqbXzRVIwOIK-uHAbriUDbLev8ucSctbRye80J5bdRu0YQKbRx3cY4sM887O1S6h-ax51i8WWuBz2b7qUMNdqwl3lKoOfZa9NgvaiHSfSIt5wDMetI5Su97snhIjzAj_5h_GorM8hcJEtQ0L6lczY1a7AUSJplbCNtljbJ91AE4mww36XB55XW5eVKvje_uKGIoeioRjsCn3gc_HYWFUcygqp7FsEG7xGt6FG71ScJoNLSOfcImHKngKw5eWv4Uix3IUytjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rUSIKcnip5oqNL11kXfPXoCRNakbM7vw01hfKN08YrK4HQzE08YyJIa57qp-MO-bLFM2mRmiKY1Tj8Iu3yE9QqU7TH8XrxEbAmE20k5M2UnGbRbK4VKpBHmHPzBfp0xDwwzmwgVWWb6uWm9CcpAHrd6JtNpyUbBwQVIitjKfrrjqpDtTsDCug9qg-3rINPYKAN_EclfQLRSYhQWtUcD_czqHqPFe-3Iv1QXDQk0R5v5KcglzRgzzqG5-Q7qzWwLGZoJQIbOGS5aydWJ6mjBlqeEE3YwenVjdpcoSfeOu-cB6rGy5GhJQo-dYkb167gnw_-72xmfoQHTBNWNEN0Umcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
براهیم دیاز هم از پارتنرش لوز مندز خواستگاری کرد و رفت قاطی مرغا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101932" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101930">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtBXKS9IE7zNSb6qE0xlj1srfsVfoERb7KM7u5lIYm_nFaUy80rAE3Lp6WH4sMEjhd18tehXfrMCz-1hS0iSCclw1WtsHdM_baayWZJ6ZJ4-0PQJnQEdPCodVwL6eZRdHfJkauo_goBqnkURqJyCK-S9RBOzTPQNoTTQ91bviBLcjugu2xSeK0sGD55_01a1Tc6Aq9OhATvnz94mK6rrE3qC9eNONHsBpMSP9TstkLms0PpZjXyrelxv-17zFGcqjgAUIX_vlEehJ_8ogu60CPSTanHRztx3qYjAKAPeTrOmCviwzvt9BoK80BsKWqLYQERIERi9Xaii_202wwxE6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2c2dac8e5.mp4?token=CJ33U0_29VfT2Ib4QKeCiYYj-AdRUVwoGb28vS5kgLCjWV_7ja1TGd-eukuvP23lVG--dIVe-Rn9kCmqDb7PgT5avrbOVn3liVwqRvY8bG9Fo2ozfEJU_dR7K2DDYhHmM47xK0Se1Ly38WoszC5PV87mJIqrR6BCFNSISFh0X-OaXkfgbDzRqAx_0rd2Z9IhFsMCuI0XoWgZAREpUYlhbvR9BY50AtVDCtRUsybhdOh4lSHDejXNIvgnWg3VPQK1CDktAx7o1GmYBhjtUC41jlR62Q8KklMh0sm4wW5ohE_-wqPk0m7ziYc8DEg0MjWyg2iZbSo0M4kZy1e9QjrZHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2c2dac8e5.mp4?token=CJ33U0_29VfT2Ib4QKeCiYYj-AdRUVwoGb28vS5kgLCjWV_7ja1TGd-eukuvP23lVG--dIVe-Rn9kCmqDb7PgT5avrbOVn3liVwqRvY8bG9Fo2ozfEJU_dR7K2DDYhHmM47xK0Se1Ly38WoszC5PV87mJIqrR6BCFNSISFh0X-OaXkfgbDzRqAx_0rd2Z9IhFsMCuI0XoWgZAREpUYlhbvR9BY50AtVDCtRUsybhdOh4lSHDejXNIvgnWg3VPQK1CDktAx7o1GmYBhjtUC41jlR62Q8KklMh0sm4wW5ohE_-wqPk0m7ziYc8DEg0MjWyg2iZbSo0M4kZy1e9QjrZHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
برگام عجب سلیطه‌ایه این! اینس گارسیا دوست‌دختر یامال، بعد از موج انتقادهایی که به خاطر جدایی از دوست‌پسر سابقش گرفت، یه ویدیو منتشر کرد و گفت:
من به خاطر پول یا شهرت لامین باهاش وارد رابطه نشدم. خودم درآمد دارم. از وقتی با لامین وارد رابطه شدم، بیشتر از چیزی که اون برای من خریده، براش هدیه گرفتم. کلی وسیله گرون‌قیمت براش خریدم، ولی اون فقط یه جفت دمپایی برام گرفته که حتی ۷۵ دلار هم ارزش نداره! بعد هم برای اثبات حرفش، کتونی‌های گرونی که برای لامین خریده بود رو نشون داد و در کنارش دمپایی‌ای که لامین براش خریده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101930" target="_blank">📅 20:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101929">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pzq4CVdTAgOxCVGKrjf9bZU7psr-wgJGDbU2xj8gRRw6rT-R8I2B8lq5bXWRumdAH8Mrn87u7rS5FYNDEx3D31Z5oXWbuScEbgAiltm7_-ixp1aBOK_mvetasEx_XK4CYVRmjEFckQkr76U7G45R0-tCialVHTEbw0HCiOo1ySPcUIjoreR5ZfHMaV6M6XA1x3njc47GvRdKjXM6CkBYUC5QkYC9xklH4Or2WpJ74R5-2RQTkf2dwKkSxlFh16zqFxiL3bJmwbH6npr0plvTlx0dvvPKZVaCA5wzQy0ZYD2nte1WqilqDygbFFYZe5rdySehb_Hnqr34Pd02s12WxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پوریا لطیفی‌فر هافبک گل‌گهر با قراردادی ۴ ساله به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101929" target="_blank">📅 20:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101928">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62941770b7.mp4?token=Jj8t1Lgjk2s4p9PFnVz_zLGSVkWJ0dwwRbfH8UVNBGCVjLh6FJtSBE0fOe6nwSUp_jvwHw-k3fuRGLNkCjT8QW4XIiSCXN8Ay4ghnmdKgUwLerIhmAn3kE-EL5n66nQA_VNWgm1FPZvyOBpnB4qclL92eaYGa1heC8KwbU_GQPDb2db5oJHev_DL84ZK7bj_sGWFCPp6uSzgrJSH07yLWi6UoY8nJxxeq-7xNsmyAUq-sJsYwpRI9WgGo9XgJwgqQmRSpLW3syeC9gYcMIsaJjUwmsqYyb6PuDnAz8Jhmv3IRbvHmBqgzPwx61-LrnWNhjp5zBXFqkItjArcdqojbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62941770b7.mp4?token=Jj8t1Lgjk2s4p9PFnVz_zLGSVkWJ0dwwRbfH8UVNBGCVjLh6FJtSBE0fOe6nwSUp_jvwHw-k3fuRGLNkCjT8QW4XIiSCXN8Ay4ghnmdKgUwLerIhmAn3kE-EL5n66nQA_VNWgm1FPZvyOBpnB4qclL92eaYGa1heC8KwbU_GQPDb2db5oJHev_DL84ZK7bj_sGWFCPp6uSzgrJSH07yLWi6UoY8nJxxeq-7xNsmyAUq-sJsYwpRI9WgGo9XgJwgqQmRSpLW3syeC9gYcMIsaJjUwmsqYyb6PuDnAz8Jhmv3IRbvHmBqgzPwx61-LrnWNhjp5zBXFqkItjArcdqojbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💎
استمرار، استمرار، استمرار تا رسیدن به هدف
این ذهنیت منحصربفرد ترین بازیکنیه که دنیای فوتبال به خودش دیده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101928" target="_blank">📅 20:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101923">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SpYH2J4PkPp0hsH9MiRLzd0MgGhXhs7vePBw31LA52PWucAJuq2_98T4z3DALOpDiD6wQ77Ei_Gvbf7y4Hqf2VQNQ6XXr3jZWyayeC2ECl2ESCOfYuk0i1CTmS3G5vyFZ4wkiCuSrR4xftqVbDM99rdhn_kbheuh7s8qT1bmYt97nhJsEeAg7pgPc2SRasQ48PBeueqBe7Q9y6cq6es4-h38z2MOK9LyjfcD-A7MS81X9OoFcI5pp9rFQUF5owdq2LWgim7T7e6c6kHzQtu-y0ufjO4tcB64ciBW-YaxUbhjQIal5YMbwZKi7X-cT5KNgYuz5rSxdbiEY2lb2_9YyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hq9VPoazIXM9k8ZLY_mYQhGu4Ou3USv1c2-c8CbX7VkkLZx6hVdIny_HhHOaFDobCYVvsGQfhiuDrM5RXa3y2VgNiSnRKCp4xCB63v_sqdPjYAKJeiM3MDZy8-wdtT0Nt0lGfKY84clpQj27x66c8iQoBqXP_a9qnzd7Q6sF2aqZoUjXR4SkFx0T_ivE_3b_VxBp1ZC8l0m8R5hr4eAC0Saf_sOUsKS9EDdGGCxlxehs3vHw30oBK3r3GQfgYHbzN5Av72GUHC-3Men6HMqEJqLrIhGuxVAtddiKTFYG0fKaMgUCz_OEpxVmYo1N3OMnWPinyFBAqGiw9ZyFLP47Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fjp8yDyEhPl8rnHKknv-2M1lelt6FTJgE9XHv94h5pbewUwEbWH8o9Z52qvDrrStDl4Ii8xT-ErA78tnvTKuBmQtsTAxrqij-lKdR1TvuP-incUfWPRsyysf7nVFaNbkVoQTMn_Wasb3oNxTmL1g7ETX-2yarW6np8oLyWPS7CfD97RSNYkXId1JRQY58mH7ZnpyqpAEL6_7XKZ8nAHaZbV0n1YuVYKxLVTNdvsdSPr64LOUFv_s6MWNe7DhNV5FUhlBzQ71NtCxf_ZXYYEWmmykEshBPfVhgFgXrPgjXjTdqRUviXD6P_zZahtHa0GHAeUIvKzwGwGJ1t7yDrZwsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91c7199c9e.mp4?token=Rb40ir2rFN1_BbKRAbI9yXQA9PVeczNmIZWRnCng8b7foQ_guRlpit84NNOU6TacgpJ0i80hWB0Drdw4GXLKEIzbgM57jchOIqOfozvvt8dfidG0gLtE6u2p-CTMSFHfGb-ducdpxXdFnRNn0jNeuXisL-SWKxoPOOGpbbnwSC77ggwkI9GvXrhc05QF12DVHaT1fGs19MrqSTT9-MKJUtk552DivMCqTkzp6myoVJ1hEiwXm_enb6W4CBs-JVQoS95QPiKdzQjqujbCQJ67-hBn8zi-bxQIjELLvgXCHVV7gvxR_sOLwCFyKIIlzmrmsSbXT6KrtemjPRvxf2p6hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91c7199c9e.mp4?token=Rb40ir2rFN1_BbKRAbI9yXQA9PVeczNmIZWRnCng8b7foQ_guRlpit84NNOU6TacgpJ0i80hWB0Drdw4GXLKEIzbgM57jchOIqOfozvvt8dfidG0gLtE6u2p-CTMSFHfGb-ducdpxXdFnRNn0jNeuXisL-SWKxoPOOGpbbnwSC77ggwkI9GvXrhc05QF12DVHaT1fGs19MrqSTT9-MKJUtk552DivMCqTkzp6myoVJ1hEiwXm_enb6W4CBs-JVQoS95QPiKdzQjqujbCQJ67-hBn8zi-bxQIjELLvgXCHVV7gvxR_sOLwCFyKIIlzmrmsSbXT6KrtemjPRvxf2p6hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدری تو تعطیلات در چین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101923" target="_blank">📅 20:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101922">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F73P__oXtoa7RBPmXGxwK52nVeUObtJKuP5WyzlcLyhqYDzMpgtdlDvQuaop-mwlTJPHnzWtpZL0ppsnYJvs6OXcUFcWfKJ3x0cx_W4U_Yc3dtG0TCyYSC9aox5bNa2sFjPqGuHikfYds1c0AQNEaoFuEQVFsJL3tQ20ThlYW4ZudpuZ_TfqEIVWA8Oec6oMNBkIryQz7NafYu6drUsiC7--cbowg-w-wuzqVGSmxlo4LRcedBUFKq10FXSZyf0p3N-96opkm79DGaL3qH_OGrwkM15pPnTqmUy-SFEBFXv8TXzstqL8EGQ0tzXCfRuFqsPDnBUvOBYnggHI1l1mlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔥
همه مدل کیت فوتبالی فقط 570 تومن!
🔥
⚽️
از کلاسیک‌ترین کیت‌های نوستالژی تا جدیدترین کیت‌های باشگاهی و ملی دنیا با قیمتی که هیچ جا پیدا نمی‌کنی!
😮‍💨
❤️‍🔥
👕
کیفیت بالا
💰
قیمت مستقیم از تولیدکننده
🔥
تنوع فوق‌العاده از تیم‌های محبوب دنیا
✅
دارای نماد الکترونیک
✅
امکان خرید حضوری
🚚
ارسال سریع به سراسر کشور با کمترین هزینه
اگر عاشق فوتبال و استایل فوتبالی هستی، این فرصت رو از دست نده
👊
⚽️
💚
کانال تلگرام برای دیدن مدل‌ها و سفارش:
تخفیف  ویژه  برای سفارش از طرف ما
👇
👇
👇
عضورت در کانال
https://t.me/esportsofficiall</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101922" target="_blank">📅 20:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101921">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fac07199b.mp4?token=VG9Oyn_h_0_lUTsPFUG6qdh5RoG4DTUJdhTythSlmu7UM2XGwTyrE-LdSTyo3OmSQklMuOvimRy87DPRxR2Z-58BiPqYCo26wdwObp6i6b7ZtuMeMI2L-w4utsvZgv5ffxNE4PbvvQm19-OY9MWh2zjCF8RwbexV80JgVPsqlUdmkzACTS186HJSxsLTGSyh4yhCeboldSZnzpDWyTM6Gnb_CW4muYVUL7niev9zcQJJ33jb9Cdzqw1QQQWDjI4ygy6LneHzTVuZ9cJb0fRedwVxvQFLcFRY22s0zZ7caAQwVJPxBppyKL8VJcU8uCjMxiMeXfVDP53SAO6eNoiHVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fac07199b.mp4?token=VG9Oyn_h_0_lUTsPFUG6qdh5RoG4DTUJdhTythSlmu7UM2XGwTyrE-LdSTyo3OmSQklMuOvimRy87DPRxR2Z-58BiPqYCo26wdwObp6i6b7ZtuMeMI2L-w4utsvZgv5ffxNE4PbvvQm19-OY9MWh2zjCF8RwbexV80JgVPsqlUdmkzACTS186HJSxsLTGSyh4yhCeboldSZnzpDWyTM6Gnb_CW4muYVUL7niev9zcQJJ33jb9Cdzqw1QQQWDjI4ygy6LneHzTVuZ9cJb0fRedwVxvQFLcFRY22s0zZ7caAQwVJPxBppyKL8VJcU8uCjMxiMeXfVDP53SAO6eNoiHVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😐
تو شیراز یه ایونت ورزشی برگزار کرده بودن که چهارتا کم عقل سر دختر دعواشون میشه و طوری همو میزننن که کم مونده بود بمیرن‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101921" target="_blank">📅 20:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101919">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HXz5ZwtahFG-pQxbnpJSIMX_SGoav8VWxKagOLYx4hyBeWdqwYfg4TDIpsEdM_pmlEGwDy9g9sHFhEGCfKYwPovDQuNFbbUQFN4XBxZKGO_p2RI7RqwuOowIj1pZAIALBocvqRWWwwLupg9Hb_nd6FlX-5pzoemt56rGuc4UyxbSDnAdV2jeBKSF0CvlnzuvDgsXruofWiLALLSM4gpilk1rAe9qgMo6MuWINT8EJvi9saY9n-Y9YP7R70l0qul6tsuZCRbvqOB5vGRAZrw-eJp1UkxzC9mPJyJnbHGRvqjGvhr0KJz6w4OriAHOMmtNKlpag849SB9uPV0vig2h4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Awvkvobv2jURpaIXRD2g2mE5h_6YTq1D3x1EzmPMpwzguoULEfO4Yw4Z0yc7ZYCujm__dM5UhyG2ZzfIJttDMX1s3KnalcD7sSNXyEdbE-lXd3PoN4nswoVHamBUOprgpRSRTVqhIfP0-8TX9zm7XRhwOCmv34MdlRoqXsE1CV_CbbPVkATnIJz4d50LMVpOwI8prDUUQ9b1uRsO6JzvIXLQqfE083QlT4HpVRtR_PLA5ZW04_KMY7WOV6q8EoXZUueWRr0bnkEXAAOnQ4EMGbEa4VVlBpy8kRHlqPH1cQVGz_KD_PdHpa2zIwSZb9UohZfSkftyZHwuUv0ePvULzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇪🇸
فرناندو تورس یکی از آندرریتدترین فوتبالیست‌های تاریخه.
افتخاراتش شامل:
🏆
جام جهانی ۲۰۱۰
🇪🇺
یورو ۲۰۰۸
🇪🇺
یورو ۲۰۱۲
🇪🇺
لیگ قهرمانان اروپا ۲۰۱۲
🇪🇺
لیگ اروپا ۲۰۱۳
🇪🇺
لیگ اروپا ۲۰۱۸
🇬🇧
جام حذفی انگلیس ۲۰۱۲
خیلی‌ها دوران سخت اواخر دوران حرفه‌ای تورس رو به یاد میارن و تمام چیزهایی که به دست آورده بود رو فراموش می‌کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101919" target="_blank">📅 20:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101918">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OE4XxTtppLnnbIG_LtTl2oWEBMKfQCWsCMw7eiPQjMNn18mbc-i8jNoaEjrFtnofBt7lsibnVvQb-uDElMY4OKlirXLBuPyoyLGzJWmQ0N4xsUQB6n71PGdpdEB1KU15fi4wVi0ol7uWcIXRvK4BITZ2VqGk3--cdJV4_T8wsBfPBuWA0H5B_xGHOq0O1KiZNYPxY-3BfR5Cg3aLOV9CLY-dBwwABIkDS-jXutFFgXkAZyB8CmgOMP9UEG3080Sudm-9wV_9cKfTfWYNb7S9UcBZEVIPnCz-upEIQQQIUz1ZCVOI-yqpfchK00aIMpPIfZ11NZzUriGsgnnXmMKkoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اسکای اسپورت:
هری کین بلافاصله پس از پایان تعطیلات تابستانی خود مذاکرات را برای تمدید قرارداد با بایرن مونیخ آغاز خواهد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101918" target="_blank">📅 19:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101917">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/779a683584.mp4?token=txmvfkBA6PG8fd5TRKpTVV5CRJlrZcUckvKwvKZLM4x-wKKJ-DlkO86BVoxFRFLpu_chi_P2zk8E3eBxZ1PgrvItj7MaXQAemgsHXvt0UDDz8rQKUz8Q6TqzXcWnmQ9NIVEBiNo0eG4affSOlH-08mesy740y6yNpuXT1O4iWr0VcQCMp6BOaSprhW-99b1lCNJqvjTPCq2NQ8-2sh_qPS1usMI8Zw1MyBORw_lbfp825Wc75ymux8ECMsZWdqsEnQdeY1eDyq62SY1G_uR5Yo-ahx4MhpDic9gTNRB2R1Y_NDuMKKWVPTjQ9f-_Fr9ZIziz6OFlyxm850RE1Cs2wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/779a683584.mp4?token=txmvfkBA6PG8fd5TRKpTVV5CRJlrZcUckvKwvKZLM4x-wKKJ-DlkO86BVoxFRFLpu_chi_P2zk8E3eBxZ1PgrvItj7MaXQAemgsHXvt0UDDz8rQKUz8Q6TqzXcWnmQ9NIVEBiNo0eG4affSOlH-08mesy740y6yNpuXT1O4iWr0VcQCMp6BOaSprhW-99b1lCNJqvjTPCq2NQ8-2sh_qPS1usMI8Zw1MyBORw_lbfp825Wc75ymux8ECMsZWdqsEnQdeY1eDyq62SY1G_uR5Yo-ahx4MhpDic9gTNRB2R1Y_NDuMKKWVPTjQ9f-_Fr9ZIziz6OFlyxm850RE1Cs2wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
رونالدوی برزیلی سرعت یک وینگر، قدرت یک شماره ۹ و تکنیک یک بازی‌ساز رو همزمان داشت.
🇧🇷
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101917" target="_blank">📅 19:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101916">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3ffe3c02.mp4?token=h6gsLC-A9NIzwDTgY9Pm3FTvX3Thw76gd8QAeLmlEVZP_NuXTeciXk1Bw1h-zCstSidz8hLHtF17SorhyUQwCJR10kUVeQW0e7aZ3hz-2IjeTb756o1sIQWDurBq8b73We2n7VKe8swuuMFQQj5cH78mXfrlZGIfhRQz0ToPuiHGFjWtqrg6QiihrwHf3Ae4Cnj_F7czDy9yXVGvWCx79jUhSz3sS-tQnWQSzA58D-0Rc2GJNJl5pZhT5hxJtQLnRo8v5GmwxP-AR1whRsMsBSDAXYV6UM2P5NO9f9sAPKDGxivTioqRyKaYUugXEf5SoiyPFj0V5XVlofIzdSTprCKpIiQzjHOtwHDR3Vkv9i-i8_sfZwjnmiEY6HdnAIDw6b0TYCtuEJh43IZXNK5Z25HNIoW-_q7V_XyDejAQBzyHvyUj1Nb0S25hRI0xtN9QadYOK9fL16jnvms8XwUp4AcBHNWEl3Q1_a7LoCT0xF4f7J4xcYhcn1iHEw5SLKDAquiOeU8Uf9UNmwyagOi_ULl4FozzTQZsxKGG7MWu9VeUqtN9O-t9CaFO8IU1F4kBUNmhDKNa3KAck5WCDtlDwHIiO7ZUG4lEN0n3omCfyEFU72dz2gOVYkIDfkvrXVqBAZCAMwwFPkeNfStxTUujfmvmeaRMMsHXedP3g1iAJDs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3ffe3c02.mp4?token=h6gsLC-A9NIzwDTgY9Pm3FTvX3Thw76gd8QAeLmlEVZP_NuXTeciXk1Bw1h-zCstSidz8hLHtF17SorhyUQwCJR10kUVeQW0e7aZ3hz-2IjeTb756o1sIQWDurBq8b73We2n7VKe8swuuMFQQj5cH78mXfrlZGIfhRQz0ToPuiHGFjWtqrg6QiihrwHf3Ae4Cnj_F7czDy9yXVGvWCx79jUhSz3sS-tQnWQSzA58D-0Rc2GJNJl5pZhT5hxJtQLnRo8v5GmwxP-AR1whRsMsBSDAXYV6UM2P5NO9f9sAPKDGxivTioqRyKaYUugXEf5SoiyPFj0V5XVlofIzdSTprCKpIiQzjHOtwHDR3Vkv9i-i8_sfZwjnmiEY6HdnAIDw6b0TYCtuEJh43IZXNK5Z25HNIoW-_q7V_XyDejAQBzyHvyUj1Nb0S25hRI0xtN9QadYOK9fL16jnvms8XwUp4AcBHNWEl3Q1_a7LoCT0xF4f7J4xcYhcn1iHEw5SLKDAquiOeU8Uf9UNmwyagOi_ULl4FozzTQZsxKGG7MWu9VeUqtN9O-t9CaFO8IU1F4kBUNmhDKNa3KAck5WCDtlDwHIiO7ZUG4lEN0n3omCfyEFU72dz2gOVYkIDfkvrXVqBAZCAMwwFPkeNfStxTUujfmvmeaRMMsHXedP3g1iAJDs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یکی از مصاحبه‌های چندوقت پیش کریستیانو رونالدو که اون گفت او قصد نداره یک‌ روزی مربی بشه و بیشتر به مالکیت یک باشگاه فکر میکنه. او همچنین درباره اهمیت مراقبت از ستاره‌های جوانی مثل جود بلینگام و لامین یامال صحبت کرد و گفت باشگاه‌ها باید به رشد و آینده این بازیکنان توجه ویژه‌ای داشته باشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101916" target="_blank">📅 19:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101914">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUQKzIDQf7lPVIXubFRSIRcqbKjglInxIhLvzTjP3Mfys0Hsmfj81lwcESK2cRYQsFd-58iJYvio4b_KnOBrNjy_1m9mPqgDLfgLUurfmT5AkhUxce6wBVpQgN64PrXZF6th0iaGqDK7OrF4mz-ehdzr1uaRUFGprw6hYSts0hy4vu_dWEddIfTNGfmqMTNuTFmozo1R-5-vLTRVsmQkzkYmQPH_3bpoTuEG0AjLdJmAItTlkP1XxF8q63tU07zfwqZfdTlrwg0kK7euPE6V3u7MkfW3Hcx4ZaNWOBIPCP1qOvszTaOmIpLE1DRb1iZ-Q0dJBGqYDERCxOxPunOBYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9c742e9e0.mp4?token=lHHxFBlecdTGZIHZfyaVShk0lSHecalhQxyqbuDvN2Flrr5WUe3kWxLzecnxyc9SoCCL7N8KIp93EXqMWZa96L_GJnyREPzYtkvM3f19fs9EA9akici-ZKmeRcSWN8J5EnhlafOOkmhK0-Fv-FdhZdNdwCHMLNmMYFrZNPEuEx70maLP4yeZrhQ_MafbcQXmXFr4FXyHvfKCsSko_dU4xmusS3tCMvrGMQu9kGGrtMLNvlD-C52-BP5U1zs7o-np0txJnWaGXFqJhqqfZMT1LzObNglpo6rDTbQxvXc95cbH5aDRXaXc8ylO1OXcvF1FyL2QVlrFMRUaedOd1i2QXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9c742e9e0.mp4?token=lHHxFBlecdTGZIHZfyaVShk0lSHecalhQxyqbuDvN2Flrr5WUe3kWxLzecnxyc9SoCCL7N8KIp93EXqMWZa96L_GJnyREPzYtkvM3f19fs9EA9akici-ZKmeRcSWN8J5EnhlafOOkmhK0-Fv-FdhZdNdwCHMLNmMYFrZNPEuEx70maLP4yeZrhQ_MafbcQXmXFr4FXyHvfKCsSko_dU4xmusS3tCMvrGMQu9kGGrtMLNvlD-C52-BP5U1zs7o-np0txJnWaGXFqJhqqfZMT1LzObNglpo6rDTbQxvXc95cbH5aDRXaXc8ylO1OXcvF1FyL2QVlrFMRUaedOd1i2QXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
طبق گزارش‌ها، لائورا ایگلسیاس، دوست‌دختر رودریگو دی‌پائول، گفته او حتی ۱۰ درصد توجهی که به لیونل مسی دارد را به او نمیدهد. او مدعی شده بعد از شکست در فینال جام جهانی، دی‌پائول دیگر حتی کنار او نخوابیده و رابطه‌شان به جایی رسیده که به فکر پایان دادن به آن است. گفته می‌شود او معتقد است دیگر بازگشتی در کار نخواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101914" target="_blank">📅 19:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101913">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRLg9fNoyNE_L6XgsUEElucOBfvxxFw5KrtLpmaTR6d-5x4NIEAjSqMMApcWPIqVk85vazLnoja9sMHxIobyeqt4ifqvsDz4xZeLl0l82j07DNl4TF8nSl21pgk_BbmXD2qIq4JAQdMTekGAYSriZO-3yXPtWmlfgLbFUnlyLtgKFnxtrpsyk3b3TQnTN8QJMa12n7fL9Z-qn6USJKOLa3dumsr60Vtnufghk8xVtaTmqgvKyimQtGbS7msJJXlDKDEyJLrWfh4oWCmoKZxBJfDqAmTPDYZECQCHq5a6m12n1GeX0BWeqt4A979ZElZnBgc4BNj9mWxCUwcVL_2Ojg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
تلگراف: ژوزه مورینیو با انتقال وینیسیوس جونیور به آرسنال در این تابستون مخالفه.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101913" target="_blank">📅 18:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101911">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eXkz3tTpmuwGGT6bGiB-5ICTijXWfhZcrSmEuB0Nw4cAepBgvKFp_Iku-b1q72untSdclrcCy6yix_l52_5F7ka6am8ojOKMTb9mFGEWupDWlEZ4KBYXa5X8jFoNyIM-eosCW3gdzkdHefAMiANGPNcyVFQxQGQ4xXxEb5lmrabUVdGkB9_FzchJOur6ilnkMr2jrx6uReMaxRz3ohXJppFV74o7ozQWT08nTzmShubNmBAC4FCLE6XtVx8ycFZD77lSVHuQNNc2UvdbKgWazMyY3TkvMJNSGczcOWPCfpNpcIWbenEWDjJAEcXo24rWET903zEl0LDJnaqHFYjAfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AjQRfO30rs8ysNHD8u-KUwR5mgdAq-N4AArnemFHYHMxSO6j4tt9EpSOvuUgQ769Cimbz8mB0Z8FMJVh1wGC7zRkeAEVt2w49k-vDhZ3vYeJ-CIr1oYVkQKjfbqBVVp9bE5cDdt71kHqI7UXH5LIdwJPP6OqLPuG1i9XBGOAu74fB4l79eWCt32E0mkn3eGVHrdLA9nCqkI7UBknT5LkQHt3I86E0yfYz9zDEXKACB6QeGj4QRQS3P0iuwS_q4JQfU-T1AgFUMT5zd-BC5kYC1UCPi6YqLwjsUgtea8AVfrgCq6JAD7jTbadbUkh9HVBnNzLK9lqJl13lxgYFXVWYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
رامون آلوارز:
اگر انتقال رودری و دیومانده نهایی شود، رئال مادرید ۲۶ بازیکن در فهرست خود خواهد داشت. در این صورت، باشگاه مجبور خواهد شد حداقل یک بازیکن را از فهرست خود حذف کند تا با محدودیت تعداد بازیکنان مطابقت داشته باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101911" target="_blank">📅 18:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101910">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrbnbPFNV6w5CFaGezOjHhUxOSIbueWl4wByfGIFZdLfjdekibvE5BgRJyJ3sSrFj7lVlykB3H28k4dZMj1ZbxniFih1VQQZ7D07UCa6myj60DP6d69PZAXrKD1BahW4NGDYiEgUyU1nxPPZo41k9HgwZiOZNHLYzjbJhdYwBiwLpPXEtYPE9U7hlQUhj8rnzjk66e8iaJYhvPawdf7PccZbtk1hPRgZIkEiWKvjLWgoFrQu78NmOyOJR4TjaznbTbD7pMcRExQw3JUrmFH4rBxSA0RooPsQScOzkfPdWvg7CIhBxBsd3neFTSf9TroSNEL8kD3MS3H4s0TZrKBW5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ربات هوشمند تهران پی تو ۳۰ ثانیه خرید کن
😍
فروش یووچر، استارز و تلگرام پریمیوم بدون احراز هویت و ثبت نام.
تحویل فوری زیر ۳۰ ثانیه.
درگاه رسمی بانکی و مجوز فعالیت
✅
@Tehranpay_bot
@Tehranpay_bot
همین الان استارت بزن و راحت خرید کن
تلگرام استارز با ۴۰ درصد تخفیف
😍
یا داخل سایت رسمی بخر
🔽
https://tehranpay.net/utopia/</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101910" target="_blank">📅 18:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101907">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p7dTCsq929Jd0UvSrrWtQZB0nbHzn-ZmJOhLNT9FOwdElkqvI0nA0TIxLELLdmHCg3SdfJtNsuHpkNqX8ugChozvmmMZU4fvGmmwoOX2HukzbD6rp7dKaZjgrs5HgJvWZgJR_uiYyxgtX1Q5PFmpx4iCF0L1TnzcYaPmgU5n67yUhOj_be6YNstS5x-UwFUtqi0BwFRczs3_UHwm4J3suX9ZbOWoKvT1j0EEuH2IJSOD0VeGu4lYgxv_iUxeANSXZDiJ0SlNq7ANA_qPaTGbDN9I_spEPu5PvhbGPNGApcYpTR3YXRE07j3aXHNo-ILlQkiH46XhW68MRS_Ghznqzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iwwx_9x1tdDC3b0HS36s0ZWgUPZZ7yDF3FxpW9PIIOAsH6iCz_P0tcdA3rWRVdJGY3JKSsvDSw436eRbMzXl8px8dbjs9BCutqOFhHaM5t0FX7zHPBVmD100EuZZNHURPD7VKYLwBdWFQJK5u1SFboiDs1B8v_q3GUeuI8Gz-i7_ULwAD-W20aPZ0-fkdnra0WKWF65JqvwbBZjUDdMxt1SGhJMDGY5XMilDXkDBy_F0xRQ_9KOqjMuLyWXSZP30oao-IMQUOHTBDWantufb1puwEFVR2oDPvTJzCRiV-RH5gdhEm1MdYKafe9wxCPIzoc2ZprlQxV9CQ5_06rIh6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d05827d11.mp4?token=h0NMpj4cxsZFPa2fcZ5Ypr9H_EFXrI_ZCPsJAeg3yPeDiF_TEQlwooVYtvXV-BE_2JrsJwskK-fWTq3SXh8okK36hkIppFGyiqGVJ1gIv4nwAf3JTg1_LLyF04XwYjQ7UG4YtqKhtnA3dU06gWUMfF72JavYpx5gRb8KXOQShwj8CSlGLB-d9OKbPWa5iuSCaDJpQCUY5rRRYUrfcb5RnVj5-FWV6eWSr4JEX3Ih_lsG1I5EOmg7kazBgNFJVKzUyk0SwBfPZuHWIfQzEAcMSQX6D2PKXaXRukhqeTzCbKOYno6Ml4kIdpX9ToOru06G0g-VgjkJcy2SSrXny7Q9dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d05827d11.mp4?token=h0NMpj4cxsZFPa2fcZ5Ypr9H_EFXrI_ZCPsJAeg3yPeDiF_TEQlwooVYtvXV-BE_2JrsJwskK-fWTq3SXh8okK36hkIppFGyiqGVJ1gIv4nwAf3JTg1_LLyF04XwYjQ7UG4YtqKhtnA3dU06gWUMfF72JavYpx5gRb8KXOQShwj8CSlGLB-d9OKbPWa5iuSCaDJpQCUY5rRRYUrfcb5RnVj5-FWV6eWSr4JEX3Ih_lsG1I5EOmg7kazBgNFJVKzUyk0SwBfPZuHWIfQzEAcMSQX6D2PKXaXRukhqeTzCbKOYno6Ml4kIdpX9ToOru06G0g-VgjkJcy2SSrXny7Q9dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
رودری درباره جنجال‌های جوایز فردی‌اش:
فهمیدم مهم نیست چه چیزی به دست بیارم، همیشه یه عده هستن که میگن بازیکن دیگه‌ای شایسته‌تر بوده. وقتی توپ طلا رو بردم گفتن وینیسیوس باید می‌برد، حالا که توپ طلای جام جهانی رو گرفتم میگن باید به مسی می‌رسید. این بخشی از فوتباله. به نظرات مردم احترام میذارم؛ مسی و وینیسیوس بازیکنان بزرگی هستن و مقایسه شدن با اون‌ها خودش افتخاره. اما بابت جوایزی که با سال‌ها تلاش، فداکاری و ثبات به دست آوردم عذرخواهی نمیکنم. هیچ‌کس نمیتونه ارزش زحماتی که کشیدم رو زیر سوال ببره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101907" target="_blank">📅 18:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101906">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cbd3d9241.mp4?token=eiWALpCdtFgChnX7RBgpqjpHcG71lBaa3zts8OcZLxTKpazVWANuqNwnJUhvlxgTEz5TJwJylJ_MEwW2Rg3ejlQYyBcyHh4sWN4KIrJF1S_S2YkzRUnLE_J95QhO_it2t69eBr3Z5Gv-8h3gN6-fmZ06sIW2ATPsnQS3eGRepzqo5on3mVMCdf5ExPZlQRZuPqetxLhZjcAIRtfohq3WSThOtYo6LXAhrePSrd8FvVFjZQNdIdfhsZGnT_pdJvAu9NrctgvioNLlyzRetmrYiLpOVTQIHzmC74w60o_QAMQ1I55oKF8LogXHtCSeu_x65kxv_nwQugHtGHhMhUa0Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cbd3d9241.mp4?token=eiWALpCdtFgChnX7RBgpqjpHcG71lBaa3zts8OcZLxTKpazVWANuqNwnJUhvlxgTEz5TJwJylJ_MEwW2Rg3ejlQYyBcyHh4sWN4KIrJF1S_S2YkzRUnLE_J95QhO_it2t69eBr3Z5Gv-8h3gN6-fmZ06sIW2ATPsnQS3eGRepzqo5on3mVMCdf5ExPZlQRZuPqetxLhZjcAIRtfohq3WSThOtYo6LXAhrePSrd8FvVFjZQNdIdfhsZGnT_pdJvAu9NrctgvioNLlyzRetmrYiLpOVTQIHzmC74w60o_QAMQ1I55oKF8LogXHtCSeu_x65kxv_nwQugHtGHhMhUa0Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
حالا که اینقدر امروز دربارش صحبت شده یه کم یان دیومانده ببینیم.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101906" target="_blank">📅 18:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101905">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6a2da2fb.mp4?token=NyTMr-i2GGegTAHPq14bjfltURQwnD3i3dyVm_fQB3I7UiAxFx4bJGNxnDSscf0giypBIbc7iUApgisj34643b0Aqtd1v3vT-zb1uC0j9rJzdDWg9dXGPdX2ekYhsCTHuw18G075tOBXCEmaWfkDpPFpuZCd8b8fYzGtpFD_NXWszhKqr4pQIwfkNqCp5UtYVNPAvGYDQjCgYCwbotK_ly7iOgtdtcpmedxukhBPRLMlJcBguO6ls8XxONAoSRiKKJroJqkRR2ylCez_63OGCo9mudb38YITbWjw24iGVbWaAXrTDcNk85mc2Zl2xXrUuVEEp0mKKYqNZq9fbKy21JJFhJDjEOOTBevb6pQtyb46co_ISml3Lu-V9W6Bn0GxiVK1C6y_ZGtZEJ70_DTgR02nPkOjdPqgVqesgjX8Vbaa5VEaLNTEHzANZStgjYw0NM2XzUatcwp7bPC5qghOgkfA0yfLPUXapNQFL_zQLyu5-DsUcajIM52dwJ_ohXhi-zdsAzbxCSH8d28i6uNyAVZAesy1Y_0ofyntHd5N5RDGoV93eM9ZmqHYRChActZEVeh41rmpqVQyiL6cu2kIE2QH4-Jo4l-VJvYIlQcI3SFgNm3JxDGrc5K2640bviqCJJO0hqQr8moYSPlJDIboWDE2kbGlNd3WvargmCLyMNs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6a2da2fb.mp4?token=NyTMr-i2GGegTAHPq14bjfltURQwnD3i3dyVm_fQB3I7UiAxFx4bJGNxnDSscf0giypBIbc7iUApgisj34643b0Aqtd1v3vT-zb1uC0j9rJzdDWg9dXGPdX2ekYhsCTHuw18G075tOBXCEmaWfkDpPFpuZCd8b8fYzGtpFD_NXWszhKqr4pQIwfkNqCp5UtYVNPAvGYDQjCgYCwbotK_ly7iOgtdtcpmedxukhBPRLMlJcBguO6ls8XxONAoSRiKKJroJqkRR2ylCez_63OGCo9mudb38YITbWjw24iGVbWaAXrTDcNk85mc2Zl2xXrUuVEEp0mKKYqNZq9fbKy21JJFhJDjEOOTBevb6pQtyb46co_ISml3Lu-V9W6Bn0GxiVK1C6y_ZGtZEJ70_DTgR02nPkOjdPqgVqesgjX8Vbaa5VEaLNTEHzANZStgjYw0NM2XzUatcwp7bPC5qghOgkfA0yfLPUXapNQFL_zQLyu5-DsUcajIM52dwJ_ohXhi-zdsAzbxCSH8d28i6uNyAVZAesy1Y_0ofyntHd5N5RDGoV93eM9ZmqHYRChActZEVeh41rmpqVQyiL6cu2kIE2QH4-Jo4l-VJvYIlQcI3SFgNm3JxDGrc5K2640bviqCJJO0hqQr8moYSPlJDIboWDE2kbGlNd3WvargmCLyMNs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
تیم رئال مادرید در دوران پرایم خودش یه شاهکار واقعی بود؛ به طوری که تقریبا هر بازیکنی، کاپیتان تیم ملی خود بود.
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101905" target="_blank">📅 18:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101903">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/virCfL5coZz3MGNB6eZSpszrjsvuU2pxswnyATfscf3sRlvBEEDNbKJaWWIecc7jMXye6iigsowu0rdVWgS93_v6ql4k6Z9IPu2kCstxSlE8bE9DSW4Hj2p_2JtxL-T6EPPL8pfNWNQwe8Kg7hvFMu_f2b-sFLdknM9_Daf3U21dmVbnAYmlhRgfGVOjn94Emi_J-L-SlMqBrbI1zkL3qzTgBEAIVNXyI5odLvGBOEmx2l9H0kA18oFR_Rzeyu8GWDYMKVq2XLeuRiqVXbXcItnXB7tOMiyNchQaSXP4BZKlE4oNjKYiFwdIFY-WKuTITpIvXX8FpuYRdTpQByYRig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
کاکا درباره دوران سختش در رئال مادرید:
من از میلان آمدم تا بهترین بازیکن جهان شوم، اما مصدومیت‌ها و رقابت با بازیکنانی مثل کریستیانو، بنزما، اوزیل و دی‌ماریا باعث شد کمتر بازی کنم. حتی امروز بعضی‌ها من را یکی از بدترین خریدهای رئال می‌دانند. اما آن دوران باعث شد خود واقعی‌ام را بشناسم. کاکا می‌گوید نه بهترین بازیکن جهان است و نه بدترین خرید؛ بلکه همان سختی‌ها او را به انسانی که امروز هست تبدیل کرد. فلورنتینو پرز هم هنگام جدایی از حرفه‌ای‌گری و شخصیت او تمجید کرد.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101903" target="_blank">📅 18:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101901">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nAHy9SswW0Xfj_Wv79lCcxr9aB_eflSE9VAsdwbRT2f7R1SwAysDzVfr6S37pqcjqV6QD1Aoor_huRlM_2Dn1336IM7da9zMgzkmly0YsvcgukIGxDMgv46xN6kaNBOhWGrq6y_ldOX2WB4hzi3PmQyUjkiQfS2ttfVmXjVxsdUi5cw_wDTGSQo2cQ6vu986inp4u9d2mJ2DxVfDHScYw8_MDlLwThOSP81MqEa8HsTn1k7fc7htrv4nk0chTLw8lifEDro8jL7dPlOMynCzebepomuCvpqR3omAD014g7qcpgNKmgxRYond0FwNjcRmmwH_ImdwxyeIGYzXYidrmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X8b4zRd_xRLiDSg1XLVfPcbwdJOpETb4NPNMNa7cd95jzCSjEVMNu0IVF-basXScOc22L26G-L2FkIJtaKXiUpM-CbgHxtL5SZ-kGXONFfocc_AuKYofmGAVM73EKbCf8ofvfZTzRh7wCtCBDXBEX-Scnx6waU-SOhyvHR2AaNAu3Q5f5Thyr1sxYhdS1ooBiJIvpmeO3kj-bWzKJZXLY3JREbC-R74tdKtt5lJX7GkFzcRHv_vxqWsDXc_1Pc8yqTVSZEhmI48-r94aJADXLqys7C7Jn-UREygpSghcHAyWGDZqTakX9SUoM75IkhZivjdJo3HD5WiggjV2l0HBnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
یان دیومانده درباره گرفتن یک پیراهن تقلبی کریستیانو رونالدو در منچستریونایتد به عنوان اولین هدیه تولدش:
اولین هدیه تولدم یک پیراهن منچستریونایتد بود. توان خرید پیراهنی با اسم بازیکن را نداشتیم، برای همین کاملا ساده بود. خودم با ماژیک مشکی پشتش نوشتم "کریستیانو رونالدو" و شماره ۷ را هم اضافه کردم، چون می‌خواستم به خودم انگیزه بدهم. هر بار آن پیراهن را می‌پوشیدم، تصور می‌کردم خود رونالدو هستم. فقط می‌خواستم از همه بازیکنان دریبل بزنم و تا جای ممکن گل بزنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101901" target="_blank">📅 17:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101900">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b492c31a81.mp4?token=XAR8TdCMy8ak5fsgzkBdAjZGiQduG2KHMnTt50a7T1DVi9izYTzw2VhIkRe4JtnT0N7ZuOSAGFoJRWqnKLQUJ734Hd2x49oW63-ld5nkgGz0i73w5w9N44hm8NtNH-qvY2ZxaGU5wrSTsqLREvqlf-ZmExapUXAFd4OJrGMqkYWIogwS4fHMh58_gYxLw-UJw-iUWlCUMYgeV5swMyeAm_Ni1_spBNiP3XkgVDCJdzhBIzKfMZFwX8gCMQsj3YDTN32YKX8WkcJW1tydpLTM3mqotffTL-aHd1WoaYYD0vB356uQHScIN1-2hNACbiNjtNfL112689y_F_fxssFYoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b492c31a81.mp4?token=XAR8TdCMy8ak5fsgzkBdAjZGiQduG2KHMnTt50a7T1DVi9izYTzw2VhIkRe4JtnT0N7ZuOSAGFoJRWqnKLQUJ734Hd2x49oW63-ld5nkgGz0i73w5w9N44hm8NtNH-qvY2ZxaGU5wrSTsqLREvqlf-ZmExapUXAFd4OJrGMqkYWIogwS4fHMh58_gYxLw-UJw-iUWlCUMYgeV5swMyeAm_Ni1_spBNiP3XkgVDCJdzhBIzKfMZFwX8gCMQsj3YDTN32YKX8WkcJW1tydpLTM3mqotffTL-aHd1WoaYYD0vB356uQHScIN1-2hNACbiNjtNfL112689y_F_fxssFYoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فران تورس تو تعطیلات در کنار بکهام و مایکل جردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101900" target="_blank">📅 17:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101899">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f2886d75.mp4?token=bEoTc-ou1hz4cnbnLOzVNntdTAkHoQsDYIdBakJOJdCkPF1i5hNKSSjSeeFcfVDVg-gQrxCO70i7gqQGTZMZA2WXL9Ca7orQvOaYFC8aIZUcg1SF6iYjN00bB8tEWQAN7Kxka7gAxCWcpN3zXQ66jt8nqea2Ju17aFPSSmsex_rB1rpEjF46bylewspg7L39B3wtkIFk6TNJ9ZI7kqvdDJ6pz46T4fHaW_hDT_CVk4VIZiJXo0eTgsu6JYq-OVFh1XjxDSWq_s7ikVcFcJzFzpg2EYS-OvrttwLDdepg3OGz7FLhlxKcGD8c_amDC2HkT1HetQC-_fzBlzk_wH0MdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f2886d75.mp4?token=bEoTc-ou1hz4cnbnLOzVNntdTAkHoQsDYIdBakJOJdCkPF1i5hNKSSjSeeFcfVDVg-gQrxCO70i7gqQGTZMZA2WXL9Ca7orQvOaYFC8aIZUcg1SF6iYjN00bB8tEWQAN7Kxka7gAxCWcpN3zXQ66jt8nqea2Ju17aFPSSmsex_rB1rpEjF46bylewspg7L39B3wtkIFk6TNJ9ZI7kqvdDJ6pz46T4fHaW_hDT_CVk4VIZiJXo0eTgsu6JYq-OVFh1XjxDSWq_s7ikVcFcJzFzpg2EYS-OvrttwLDdepg3OGz7FLhlxKcGD8c_amDC2HkT1HetQC-_fzBlzk_wH0MdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر شاهکاری یه کپی بی ارزش داره
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101899" target="_blank">📅 17:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101898">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe82274ba.mp4?token=ABaWCVO7uM7ry8hQ_GS9mHkERoywfnXWZosesPt3wj2IM47vee7KbmYSHTVZeFkW36LLWC5H681gjoqH7hVqqJuVv1DsXRdSyFbiwyWkuBPbRPw8WQGhp-T2EIF2TGUATIp5DsPsAe6Y5TQf52I86P9GCjdW9rDTd7IXeKuHbZilKTsn3-qXz7vxZZoA40EXaMIF9_nE69CYcCPKH7qmG3dOKsm8BPSmVwhmKKHVZZLOS1L7OQs8W1Wxk6I1mSa1cyh_hQnrj8jc9JbogKgOhIAt_7ahN7jJ8dUJ8JdfWsuEedQRZOaOzK48bDKY8_FXbDIegWB7wpF5zPh2TtID3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe82274ba.mp4?token=ABaWCVO7uM7ry8hQ_GS9mHkERoywfnXWZosesPt3wj2IM47vee7KbmYSHTVZeFkW36LLWC5H681gjoqH7hVqqJuVv1DsXRdSyFbiwyWkuBPbRPw8WQGhp-T2EIF2TGUATIp5DsPsAe6Y5TQf52I86P9GCjdW9rDTd7IXeKuHbZilKTsn3-qXz7vxZZoA40EXaMIF9_nE69CYcCPKH7qmG3dOKsm8BPSmVwhmKKHVZZLOS1L7OQs8W1Wxk6I1mSa1cyh_hQnrj8jc9JbogKgOhIAt_7ahN7jJ8dUJ8JdfWsuEedQRZOaOzK48bDKY8_FXbDIegWB7wpF5zPh2TtID3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زیر ۲۹۹ هزار تومان با ارسال رایگان!
🥳
با سرویس سفارش
یک نفره اسنپ‌فود
غذای مورد علاقه‌ات رو با
همون کیفیت
ولی ارزون و به
صرفه‌تر
نوش جان کن.
😋
🔥
از اینجا سفارش بده
👇
👇
https://i.snpf.ir/wopv1
https://i.snpf.ir/wopv1
https://i.snpf.ir/wopv1</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101898" target="_blank">📅 17:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101897">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5e82a980.mp4?token=iJQ7tB_6YVj0yKqBu7VaKnXXzmo2qbjPBRYL6CAb_enGnE2bMl5WK8IBPXekjM903eybPwZhIPxmhxytWgj8-nWZDwrlhomN6PnSWaUudX6WQL359NTf2Xv_uH0J0Ko2rzp2BQFjIhvJximQlSAzioZCZ6F3UXlYV3gHbDFEBSGRrhOOgxyRTaIWSX_C6m6NFI_zZXHzSDV9vwd6dwSdDxyXkRuB3eOcPEe3kBbfMqear0kJkSq6faE6ZdFsM7aU5qKfjzEF2dSAfyuLR1zXV-cuZFM10UPUGe30_ciT8m0cFrdTt5qjApeprkaohjFvqBc2cBgZHUm7uZ2VpQjr8IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5e82a980.mp4?token=iJQ7tB_6YVj0yKqBu7VaKnXXzmo2qbjPBRYL6CAb_enGnE2bMl5WK8IBPXekjM903eybPwZhIPxmhxytWgj8-nWZDwrlhomN6PnSWaUudX6WQL359NTf2Xv_uH0J0Ko2rzp2BQFjIhvJximQlSAzioZCZ6F3UXlYV3gHbDFEBSGRrhOOgxyRTaIWSX_C6m6NFI_zZXHzSDV9vwd6dwSdDxyXkRuB3eOcPEe3kBbfMqear0kJkSq6faE6ZdFsM7aU5qKfjzEF2dSAfyuLR1zXV-cuZFM10UPUGe30_ciT8m0cFrdTt5qjApeprkaohjFvqBc2cBgZHUm7uZ2VpQjr8IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارلینگ هالند از مزرعه یه پیرزن استیک، عسل و شیر تازه خرید و بعد رفت خونه تا خودش دست‌به‌کار بشه و غذاشو درست کنه. فک کنم هالند بعضی وقتا یادش میره که یه فوتبالیسته با میلیون‌ها دلار ثروت.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101897" target="_blank">📅 17:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101896">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjEw2MLhZUNFs_rz_pUwEMEFGelDmlki7sevCM4fCkkGiiM0lxDVNRiBH6UaDWC20k7AQjNu9kj3NitGwptkB-SyeORhDwn439XojzikDRkpYjVPyfcvVle-XZkJGRf1rY-M2B2lJN_ydQJ5NA9sE6ji0bK6V0gk96HKG-XYKeand31jPn677m_SnW1EXHZJnOThgR8XYzOPqwU6UBdPvhO0vRNQaQDeZczPlK25qzO63Z6NTEgVfV0O_eeGxaP-kwWGDcTQ6K2uaiWvw5DjX8QKKG88VueYz5NPF5Pfd99GBMtJEmfqkt9HUSFow2m15XnQ_fA6VY6RRQYkTBDpzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دیوید اورنشتاین: آرسنال در حال بررسی احتمال جذب وینیسیوس جونیور است!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101896" target="_blank">📅 17:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101895">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKmpMSPw-M-ibvikuj9V0-ulWTmvC4b_PdnbkiBRZlKuaZN5LVxtvaiVQ6hm89iocOa67U8ctzZVHwpTJ00eaJDjESSnf-K7lQxYPD3jHZ1VcibErCbKNM0D_5lAEBkUhaR6IxHtLJ-AAAk7OB86mE4XdBFe6Q4EB_z-Lt6PXzCkGGUh7-VY-hWgyD6dHDpaIEfT6wRXAG4EfE4RijSiWj4HAUepouqHzJ27pWcM3RG-e8jDwVshhwOPoDLx0PAg9PlRxWPMd-fouI5Rjyri5u7ooG3hyF-K6pG4J4dswJL7_pGyHFELV7wK8edwOqTX9EE5VY1DTNO7PkqhocU_Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
بن جیکوبز:
نمایندگان وینیسیوس جونیور، این بازیکن را به لیورپول پیشنهاد دادند، اما باشگاه به این پیشنهاد توجهی نکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/101895" target="_blank">📅 17:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101894">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36c582a64e.mp4?token=gClpTm9CQO7ewkTQw4h7eyEg0s3eAxGjz4TRfpaqY1G0oOWMFTR64OmAeSIi8DH57IBSPr4zbGLTA49WP6bV279I3ltNpgRaSYGE12-sBzHCLkv-aeIhzXAi8W_xWpcwmHiX6XV5AXXnAXZAdBI9kI5pd37v1flyegTVEo7ayjghUj_6vqDoGfMWLWEsZchRcdJiokSRpzRtLqB59-N9n_qmc8vWdnzOew_iZ4pu2GuiSKUiWoWUw34SDDCoM-G9EzktWnZ4oJ1i1zX-z_qeO9hr8g9QRFJXnZwdPqqHZj_cWu8Gjo-SqpyKRY_WMXPLZwqm8w8xMCK2va3jUnNKZTmbKqUAG4UljraPgtQZFb4rxCN9kleohIxQfvXLizajL84Qaf7Dnu1SIVag2QEQL6SFA7r4jBJwJCC5PNF-u1zNETBQOkjrucLUovCROVGz8kEin1SdW32zDLP6bGne6QdvC-JBzDxrRU4y8AxyScNzq0Vun66AQlNpoB_4uWnJjAvglBjlgHOcOQclHtT_WysKfufERcckpInpJvdESbxCPdhQDlpy0TDOFNAYkU23EsrwSfKIcLnkmC7y1NivUZMNYXzn3XMxTbbNJNCi7-WM7HFVVNzayCxuJvXhHO265lhBttD35i9a_trGlDRDSC1bvjpXWy8a1va5cFXOLg0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36c582a64e.mp4?token=gClpTm9CQO7ewkTQw4h7eyEg0s3eAxGjz4TRfpaqY1G0oOWMFTR64OmAeSIi8DH57IBSPr4zbGLTA49WP6bV279I3ltNpgRaSYGE12-sBzHCLkv-aeIhzXAi8W_xWpcwmHiX6XV5AXXnAXZAdBI9kI5pd37v1flyegTVEo7ayjghUj_6vqDoGfMWLWEsZchRcdJiokSRpzRtLqB59-N9n_qmc8vWdnzOew_iZ4pu2GuiSKUiWoWUw34SDDCoM-G9EzktWnZ4oJ1i1zX-z_qeO9hr8g9QRFJXnZwdPqqHZj_cWu8Gjo-SqpyKRY_WMXPLZwqm8w8xMCK2va3jUnNKZTmbKqUAG4UljraPgtQZFb4rxCN9kleohIxQfvXLizajL84Qaf7Dnu1SIVag2QEQL6SFA7r4jBJwJCC5PNF-u1zNETBQOkjrucLUovCROVGz8kEin1SdW32zDLP6bGne6QdvC-JBzDxrRU4y8AxyScNzq0Vun66AQlNpoB_4uWnJjAvglBjlgHOcOQclHtT_WysKfufERcckpInpJvdESbxCPdhQDlpy0TDOFNAYkU23EsrwSfKIcLnkmC7y1NivUZMNYXzn3XMxTbbNJNCi7-WM7HFVVNzayCxuJvXhHO265lhBttD35i9a_trGlDRDSC1bvjpXWy8a1va5cFXOLg0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔙
🔵
۱۲ سال پیش در چنین روزی، دیدیه دروگبا برای دومین بار به چلسی بازگشت؛ اسطوره‌ای که نامش برای همیشه با آبی‌های لندن گره خورد.
👑
📊
آمار دروگبا با چلسی:
🏟️
۳۸۱ بازی
⚽
۱۶۴ گل
🎯
حدود ۸۶ پاس گل
🔥
۱۰۴ گل در لیگ برتر انگلیس
🏆
افتخارات با چلسی:
🇬🇧
۴ قهرمانی لیگ برتر انگلیس
🇪🇺
۱ قهرمانی لیگ قهرمانان اروپا (۲۰۱۲)
🇬🇧
۴ جام حذفی انگلیس (FA Cup)
🇬🇧
۳ جام اتحادیه انگلیس
🇬🇧
۲ سوپرجام انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101894" target="_blank">📅 16:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101893">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWVHPmNgLyuB_OEDOV1kZ3h5CDBGXw7ptv9V6zkGhtmqnN9h1yn-w1yyzsmDhWldPiB9w1bJ1FIiENoy-CjyKoLYr11yZioGjYzKvAk3lptQhtiNiXU6kZroPlBo5NuRA9Jt0ZxZqLM-67KafbnQ-FLZCW8bryBKIgWDrr3bxOyuVxunKZ_bhNs9fjFPDhUlNd9R_mUvAhFw-ucE5kkPFrmajz0YsIlT2l-lPmiaKX-OvybAwsv2mN93ahcqRpGVMXNsmazp44xhW-BtDuc4slFNtCJcWtS-wWsEQnIp7raNQhNFE7t89i4o95GyCumUptJgKiIWX1jUm-KZ9YcEYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش مالی جام های مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101893" target="_blank">📅 16:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101892">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
دیوید اورنشتاین:
آرسنال در حال بررسی احتمال جذب وینیسیوس جونیور است!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101892" target="_blank">📅 16:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101891">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a105d81352.mp4?token=is3blblIlVyXQC6cTUyCb8NotU4QFUgjmVTYuVj9TpCjnGNgkWb-ECGWLeqrXnFxlF8rQEcWd0i-QsWupezRjqtIcZRsppSRYZ8LqZ-0GgAKCFtzLJM3O_C1Aw-wNyfDHjU1LnQb0V-sEIJPQuRJbITzwCGk7igNcA9jmMOCGNudsN3LRLqSn4hxFhuXj7APTa7n39kcM2bCRwwvF3gKa6vF5dkwt5Ls_H86N1j6VeZixVob9h5S7qcpJiKjn6CwMHVsoIfYJxHxJmAFbXr08mBE7vni2lNnRqF5WnputAU9YAORHTc_T1qRj863LB1Lw-IA8v267A85NNyznB0EFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a105d81352.mp4?token=is3blblIlVyXQC6cTUyCb8NotU4QFUgjmVTYuVj9TpCjnGNgkWb-ECGWLeqrXnFxlF8rQEcWd0i-QsWupezRjqtIcZRsppSRYZ8LqZ-0GgAKCFtzLJM3O_C1Aw-wNyfDHjU1LnQb0V-sEIJPQuRJbITzwCGk7igNcA9jmMOCGNudsN3LRLqSn4hxFhuXj7APTa7n39kcM2bCRwwvF3gKa6vF5dkwt5Ls_H86N1j6VeZixVob9h5S7qcpJiKjn6CwMHVsoIfYJxHxJmAFbXr08mBE7vni2lNnRqF5WnputAU9YAORHTc_T1qRj863LB1Lw-IA8v267A85NNyznB0EFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین مدافع جوان، دوست‌دخترش خوشگل
پسری خوش‌چهره و بی‌حاشیه، قهرمان جهان
یه مرد دیگه چی از این دنیا میخواد؟
😍
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101891" target="_blank">📅 15:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101889">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uP1BZVxh0LQjBo1say5dza_OQmgmp8r-3pQjEzpW9oqwhLpy4LKry_Bop6SW1eIJ-scjxdQBdSmoyy_pbzFlMa4nOVB3DAABmcjgm6y_0nRcfaGYR1E4QIAtVbHtLJjKnxcDjykepq8sWBAxW0t39z4bNwdUOJObHrTdvcq1ihcAnscOW52laiowPvyqTaIw60cJ1ivKMZ90ujBNa-6DEHGnalSG9LipYQPedU7G_BxOPUsuY1ssFMz-yCl1wiKWEArdxCwa-t_UyrLU6QvLQstsFomZqF1n5HUIF-YWiLtxqMYRuQIujW-M6ZbSTgNNi5iykBVZ8Kzzzlgx-G0q9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lAUtutn7cap7738hwxMrQz6FGo3qXk-ecbjdJeVr00fWvDPeZSEhNNkvledkCwif7x0vLl4mlAo0NPLuq8aluFwv1DWV9KbmXkPgpvFhGSLPLBdDbtRLeQpyr8_cniraK_PmvyktP_Sq1cKhZ6iI2DguDOEcc72YCIXcNKCQbZH4sl_d4Erql92kp4atmId8oERZMGQlZsQRI-NNYhFUxnVzClF63-Pd_QI0mG_YwY2KWTlko8ituTDNEx3B6pj3x5pvj16GhgkbMFkD-MK0pOkYSQtTdCjS8i92rjbfYYAaGMsz4pYbHpLk4rtnhkx6u-GcoFP_Rz1-y9sBvrvmUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚪️
رئال مادرید و ژوزه مورینیو این بازیکنان را به عنوان بازیکنان "غیرقابل فروش" در نظر می‌گیرند:
🔺
کیلیان امباپه
🔺
جود بلینگام
🔺
فدریکو والورده
🔺
آردا گولر
🔺
برناردو سیلوا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101889" target="_blank">📅 15:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101888">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtoMm1Vz051bpvBglL6QPGq_ile-I9GhDytds1oEm1KCDK2G3aUX-veu_q1XuXLGO7lghXUDxGCM6A71VPUCT5_SkRic7yLhCVRo80URzuGxetRHjgANdXOOAlEWOZfDnlIWBahuwZrNapjTXihoxuvSSJQng4WWrSRF1GfFUY81tcUeqlM_ZdlrlrMDrabWTeENELKDO9I2xm7RTPnsTEjHDW2zwWt36C9AQg63O57ZVc80Q3T1tjg8qpRxLN6EEHgVWu4btPZNdahY6me2Krr3NIv4A6bMYp2sRSbjCuWyjhIPBidPk04ZzcAmW0wyq4jcBXW7Irt6ELg_gGbsVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فوری از فلوریان بلاتنبرگ: منچسترسیتی به صورت شفاهی اعلام آمادگی کرده که پیشنهادی به ارزش 100 میلیون یورو برای جذب یان دیومانده ارائه دهد. اما تا کنون هیچ پیشنهادی به صورت رسمی ارائه نشده است. و مذاکرات با لایپزیگ همچنان ادامه دارد. منچسترسیتی به دقت وضعیت را زیر نظر دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101888" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101887">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kV3Oc9_wkkP2vVfB-pFXrve_llHteOMjuYAkeg8xxj0y55OndDZLBMkGXuAHQk6rhabzgrUy30FZVrRYK0U0MePCDseQPyWLobOHhlLAMz4V1o-2PXpZW2wJwNyUhli-u8_SMQyPXRvuaUryQ9R1yV3tQMkVWezJPJgsMJqp5pnhlLDTIT7lymHVGVW_0-M1pnrMe2Mt96zxqP1B8ehuvsh4B99Wo-QXMzCxEjehqCM0iG0zw2oJw8TBxN9zBPHZrg9a1GSgtGi1sBLtcjGWSUPAw3iKul5KVJyRJCIGNHDFZBkjBY-iEf7Uydk7Qjh-dC3J9ly6Y17qceoyDdeIYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
هزینه تیم‌های پرمیرلیگ تا اینجای نقل‌وانتقالات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101887" target="_blank">📅 15:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101886">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNRHoRQSKCZYK0LclZUJ4XhvvYUHHAC2rGGNpoLE1hHoNJmgs_4024nl9875HaxnlUjQHHzX6SH8vPEiIQ9PGjU11dBh2aCNw8jjvq8yLJTt8QzHZX-JON7o01YQxGXM72SyOhuMqnUS8CS5DSDeuEO_9MB9WVnh5qTezGCAEmcUfpUMvpVXyae_A3LJGmmT1Tu3b8LFDGSWvUBKqFx-B9R4j7SHBGCSK_fXWiss5JVL-5PdBe-ToWaFL9UNtttxgsN9tyfEYyXEDQx1jS9XloNK7aPrtVbhLZmImbj6fqTmhwJeT_LyamzRjBV_zurAPrKvJpzCm-zkq1woM2fKag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رودرا: اصلا بعید نیست که اندریک این تابستون رئال رو ترک کنه، این احتمال حالا جدیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101886" target="_blank">📅 15:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101885">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUvBccZ9eJbUlOZAukwFCKjptF5y2ToMpe7VYn0D6TDs_SKz2HJEOA5zE5uGp3nSEvMAcMSgeSvCg6s5qVVYGj-AegQrppyoILWLuVlOLDX6BgRX8WJikxx_ulwzNoAPKegqpbsoxQGJUgzJX5INh7VKhUaPDLGKmL4RjWCsSzv2UMIHyZUuJUhaXEdX2soBKSzu_sNqTwZJ9IjDhF1CH52IOWGxhlRMr3wc1nGdXnNu7HYzPSbr_tXljjLznhNMzh3sykr-zNrR3DtD3pszCj6FwhHCMRQeA9J9lRflJbkwFvM218RgnBPkBwzK4ZhBEWaqWDoOW7g_TxjTwmf4zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
سانتی اونا: رئال مادرید از شایعات مربوط به انتقال مایکل اولیسه در رسانه‌ها استفاده کرد، در حالی که به طور مخفیانه در حال مذاکره برای جذب یان دیومانده بود. حتی آن‌ها به طور پنهانی به مقر باشگاه لایپزیگ سفر کردند تا این انتقال را نهایی کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101885" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101884">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f29886b9b.mp4?token=F038SolY8qvalI-7OryYIIZQtffzlZC9jp66AtPimE49FXCzw7Wb15cuI5fTAVKOmXrHIXksQA3DvsNhrc2GktCIt2vNNOs1Z2ZwQSyEgefCaDbFidxfz5lueqVQWrT6rkUyTiNQFvbAZbdpNWHSCHqi9DPwI20DWsa0PtTTJtWsMZsQw75qIuK2P3-AALI0DOzbOIEpXe_KH5sI9zVqperXAqppXvLFc6_f7C9Gzk7eLMLqGBH3W3ouiX8K769SygTB85N8j8DCoQgWTcy_ZtfWQLt_WUo__jGuzN1WJKhOa1bJiCK4zil4tjs8c8LieQ0za4bJWe-51F3jxLdWJllcLSSeYVFfulvNFOhicQ7Us7W1F4qW5SicF7DowPqlrybrWJYZMK9zlNS_VQo4dYYZXMJ1Y3TvWRRg42LUDQ4uKuTM5UVqXRqOkGUsoZs9EIp2CN7lNuuB51GmGgNV2OmjjYZrRxbWkSJj63iityC5mT_AzSkI0Rea8-JgF8w0lYAZrm4_BTP6MmCHCQ93P8FE3AN4fIM4Rp_4Of-Fp3HQIDbnYLXjMxsWep90wLDXO5uQsBIjSPn9dN0uLm1koi9JA3h7rKyxIJ9iZmEmXRwuWql24XHEfYCOE8r0u4aORTeowZmnzLndlytjqbW0u6bF2Yd-AYmNTqrzXEtVgqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f29886b9b.mp4?token=F038SolY8qvalI-7OryYIIZQtffzlZC9jp66AtPimE49FXCzw7Wb15cuI5fTAVKOmXrHIXksQA3DvsNhrc2GktCIt2vNNOs1Z2ZwQSyEgefCaDbFidxfz5lueqVQWrT6rkUyTiNQFvbAZbdpNWHSCHqi9DPwI20DWsa0PtTTJtWsMZsQw75qIuK2P3-AALI0DOzbOIEpXe_KH5sI9zVqperXAqppXvLFc6_f7C9Gzk7eLMLqGBH3W3ouiX8K769SygTB85N8j8DCoQgWTcy_ZtfWQLt_WUo__jGuzN1WJKhOa1bJiCK4zil4tjs8c8LieQ0za4bJWe-51F3jxLdWJllcLSSeYVFfulvNFOhicQ7Us7W1F4qW5SicF7DowPqlrybrWJYZMK9zlNS_VQo4dYYZXMJ1Y3TvWRRg42LUDQ4uKuTM5UVqXRqOkGUsoZs9EIp2CN7lNuuB51GmGgNV2OmjjYZrRxbWkSJj63iityC5mT_AzSkI0Rea8-JgF8w0lYAZrm4_BTP6MmCHCQ93P8FE3AN4fIM4Rp_4Of-Fp3HQIDbnYLXjMxsWep90wLDXO5uQsBIjSPn9dN0uLm1koi9JA3h7rKyxIJ9iZmEmXRwuWql24XHEfYCOE8r0u4aORTeowZmnzLndlytjqbW0u6bF2Yd-AYmNTqrzXEtVgqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
امروز تولد هالکه و به همین مناسبت یادی کنیم از یکی از ضربات سنگین و پشم ریزونش.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101884" target="_blank">📅 14:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101882">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iT4UzbTB1s-g-lxWRbIk_j7Zvzszc6qi3Z5jDB3NMSATmGyqTKaAIe3xyWuPM3NjfjP828HDNXQ9CZqfiDpQXRdhrxAVs9Z5jdBApoNRTuR3_JcJMHgUJijF4Gkm2KMlGt2WFcjmKndgQ6KIG3K6Lcrx69F0rHNVU36FwLFbz4BSCZ1pNLc9sY7KFrFcgANabQLxIX3xLRF2N-Ev5dnMfCcDNShvM647pjWKeHkGBzMF7H-SPED9enYQgSrRjqOnzwsF6ACnfD1naSzc9bteGIif4KS9z1F6l7wT6LX9lmnIp88Yy783Dc5bD21HaJvjOTBJyAuhPEnz6jc12j26mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6342fd750.mp4?token=vvow62nFfj7vc-sIDxTF1hO3Rv8qjGG01_1LCDpJZk6kX1gBKNyGjRouKuMiqV09cVknryvPbaQmQiW8t0wKPYznhePv_qRKQYx7dTg8CM9kxkBlEVvxFLg4utQhAGxGvPjs6VX5io9Zj36xm9kD7jUANCeyuRMmCdKro2dhxHaCkGBPVzK8JXsyJM6HEiiUItfg5Fu2TgjSyY0vH7w4z286VlPNU0eaCxls6Ip8D62W0fwqaJzvTQVhqzFlllCKsphqYC3pmPbn3RtMeZSNvK2jyvmjv9XecQcnHIvcom8OD0JGGFGAHj6RyCfgYLf90Tg94YWe0QMzUeuxiCQJNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6342fd750.mp4?token=vvow62nFfj7vc-sIDxTF1hO3Rv8qjGG01_1LCDpJZk6kX1gBKNyGjRouKuMiqV09cVknryvPbaQmQiW8t0wKPYznhePv_qRKQYx7dTg8CM9kxkBlEVvxFLg4utQhAGxGvPjs6VX5io9Zj36xm9kD7jUANCeyuRMmCdKro2dhxHaCkGBPVzK8JXsyJM6HEiiUItfg5Fu2TgjSyY0vH7w4z286VlPNU0eaCxls6Ip8D62W0fwqaJzvTQVhqzFlllCKsphqYC3pmPbn3RtMeZSNvK2jyvmjv9XecQcnHIvcom8OD0JGGFGAHj6RyCfgYLf90Tg94YWe0QMzUeuxiCQJNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
هِیبا ابوک همسر سابق شرف حکیمی:
وقتی سال ۲۰۲۰ با اشرف ازدواج کردم، عاشقش بودم اما او انگار به من شک داشت و فکر میکرد دارم به او خیانت میکنم. وقتی دیدم نمیشه رابطه رو نجات داد درخواست طلاق دادم اما اشرف اصلا ناراحت به نظر نمی‌رسید! بعدا فهمیدم چرا؛ او تمام دارایی‌هاش رو به نام مادرش کرده بود و چیزی به نام خودش نداشت. این یه حرکت حساب شده بود و واقعا شوکه شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101882" target="_blank">📅 14:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101881">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/356f27159c.mp4?token=VIvdy7ZdpOIYW8ly733tgjRbuSpgj-H_OMGvzC1fqm3fCYXibq9aIcJiJ_Fk7ABJw6KebEnB-MfAFwc-R_j-kNNGpVJYaiUaaRoMGHxXOWW-AD_IKCuT0fyQ4mcgpT3Z53rz0zvy5UE98q5C55QaADxHT5Q_dLxrR1leRSjSRrv6Q2egFD6yh-x3CsbuD1RUHtocLyaPmTEOhOqJJEWrKM38-7n-SAzQcmnj24mrN8NgVGz46zKv_X65sQlHWMAKlERI-gb3jjkWzuZ8yVUJi7_X4BN75xx1ftxPHVxLV3ZFBj57t5B3ILy3NuWYlqBmcFux5bVR8cTTuEpTiaqk9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/356f27159c.mp4?token=VIvdy7ZdpOIYW8ly733tgjRbuSpgj-H_OMGvzC1fqm3fCYXibq9aIcJiJ_Fk7ABJw6KebEnB-MfAFwc-R_j-kNNGpVJYaiUaaRoMGHxXOWW-AD_IKCuT0fyQ4mcgpT3Z53rz0zvy5UE98q5C55QaADxHT5Q_dLxrR1leRSjSRrv6Q2egFD6yh-x3CsbuD1RUHtocLyaPmTEOhOqJJEWrKM38-7n-SAzQcmnj24mrN8NgVGz46zKv_X65sQlHWMAKlERI-gb3jjkWzuZ8yVUJi7_X4BN75xx1ftxPHVxLV3ZFBj57t5B3ILy3NuWYlqBmcFux5bVR8cTTuEpTiaqk9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هالند لاشی تو مراسم عروسی دوناروما هم نتونست جلوی خودشو بگیره و مهمان‌ها رو وادار کرد «حرکت پاروی وایکینگی» رو انجام بدن.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101881" target="_blank">📅 14:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101880">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMCVkbi2XiYrVugrAXx_qRcE86S7mXpDGFClctMs0utFjP8h9M-OGgcndyzlvu2voy6-_UctfQVSrofNSI25a-dCwC3Oh1KS-UqsfozI5-CcngddBOb12tK4kTDj1PC7nJDZK7pc3c4gNfKqRwzZjSWJU6g1BSklAJzl6zOe7IMLLdH6jXUW4vmJF-1e3G1j_ArOiozmTwwVlqHeDovdLsBz5t3Lg5g_XDWdiemx7Vc4AQH9Usf7bQZYTiGVf_RDXd1BHpglTJqKjnYTUR8P4PETQtQCyMoDUiyhs4PMSP_bF35_a_BebRneCIKSiQr5R9Tt4Vh96frVkqwqrP7Q8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خط‌حمله نیست که ماشالا فلیک رفته تیم دوومیدانی برا خط‌حمله ش جمع کرده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101880" target="_blank">📅 14:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101879">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff0c27865.mp4?token=r2Z9Muit_eD_5mGg8wWjFPQNw-zrQ21vpcoHI9DSQWn2x-SInNpO8nMpa1ktN1fskTEeWF0n24xL9b_nxAL_rXDVpKaPZW_EXWRBYxmLnhvxlbahx-zn-hQPHboRfbueULVLatyQKOnY7V0XtF5UEn7ARTs8LZMth32CCxSoOSUDSlOc5kKUR72kce80cUlocwn5TqVsE23ne98heqN_sKZWqAxfDEUfhFauKGSAQxeKYB1YY9QIzNGFQWgQmFJJO-4_k6nsFysdRUqtb2CmlX3Qtac3H0mOa5LiJQ36_53Y0sxsXSpFCGS2GGIgqh9vtcYsHEbW-058sc04huHmZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff0c27865.mp4?token=r2Z9Muit_eD_5mGg8wWjFPQNw-zrQ21vpcoHI9DSQWn2x-SInNpO8nMpa1ktN1fskTEeWF0n24xL9b_nxAL_rXDVpKaPZW_EXWRBYxmLnhvxlbahx-zn-hQPHboRfbueULVLatyQKOnY7V0XtF5UEn7ARTs8LZMth32CCxSoOSUDSlOc5kKUR72kce80cUlocwn5TqVsE23ne98heqN_sKZWqAxfDEUfhFauKGSAQxeKYB1YY9QIzNGFQWgQmFJJO-4_k6nsFysdRUqtb2CmlX3Qtac3H0mOa5LiJQ36_53Y0sxsXSpFCGS2GGIgqh9vtcYsHEbW-058sc04huHmZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
صدایی که این چند روز تو ذهنمون پلی میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101879" target="_blank">📅 13:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101878">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_Sz3-36qgZNfGlXTswSScqF22CCysRRTs1mB2Ux6ro8-CJvSLwSz4j8noqGUqMV0F7I-Eeovd6KZbzxJ4Cn57dbBvzACdsLx3MxZJewjyP1dj2VZnHe2msmSKdM7uI9Xsaeeh0fsEfSL56qgAi7q6XC6Sv4HO05IZYuQmL8sfdyJ1KSgBCsUjgidnS0-7VqLZFW55R22-FmU-ppOo5pjeIX0BEcUvqsotk2DWt3nnxjKrnNiNTgZAhW3k75-3y2PWs1pu7EJ6o1WTeDC1iH2SXqEeg2lQZyl8YgXO0xLPgvIWsbvVXMNINME7mGyIGgCe4qoj1a04k4AK7IYVy6bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇪🇸
ترکیب‌احتمالی فصل‌آینده بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101878" target="_blank">📅 13:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101877">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc2d82d4a6.mp4?token=I5ZsPTXulMUbxZ3eHNmicPcYwkOHkeQrjqhTRJyHwZgHq96Eqr0rya7uuQcM88vh0474DbtG8sH5K74Iu97tcoBHwftp83s4puTNC0KLOUbZlUOcVgTpxwBb0BsAdGsF9KaSvuEq5iLY3TtXoUQOjdxXx-31m6SwbAYcQnOITzHaykm9THd0B6I86JcxvUcMKd5BYyTU6Ns22DIwUGKIM2SlRtHLskn72lmkauSITKryqplML1-Z6tcaoG9cduXEyFHMdjJa92Kh40N3fiia2TFuCs6JuOJTDjhyIxBMcyxV9cdOM9PNA_5lL0XyzuboGsL4wtSy-RNKg4vKL9L8jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc2d82d4a6.mp4?token=I5ZsPTXulMUbxZ3eHNmicPcYwkOHkeQrjqhTRJyHwZgHq96Eqr0rya7uuQcM88vh0474DbtG8sH5K74Iu97tcoBHwftp83s4puTNC0KLOUbZlUOcVgTpxwBb0BsAdGsF9KaSvuEq5iLY3TtXoUQOjdxXx-31m6SwbAYcQnOITzHaykm9THd0B6I86JcxvUcMKd5BYyTU6Ns22DIwUGKIM2SlRtHLskn72lmkauSITKryqplML1-Z6tcaoG9cduXEyFHMdjJa92Kh40N3fiia2TFuCs6JuOJTDjhyIxBMcyxV9cdOM9PNA_5lL0XyzuboGsL4wtSy-RNKg4vKL9L8jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
مرور دودهه تاریخی برای فوتبال اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101877" target="_blank">📅 13:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101876">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705177dcef.mp4?token=cuyFfAEyoAXq4IQxXfo4sjLO1Ci8TRdnk_7wnHhtlHOj7v4gcxXGqIo8IknQdM6wc2ITFdKEuDJ7q6sqDrxubRrf8L7v0pJ-WKpeFyiKRY2l5nFdCRvaZQywTNg1mjvW7qNX1gKvT-Di7JygPVXR4DK-pH5M6brvdumLYfSFwF-YANYGQAKAUmZf-j_ETalTyi9mC8I4Si5Z4QNIEdTzcirA5aEArK19vDGgmuASzn2-3Yq5mWrN3LKeDfjGkvcUrt1pYgctSrcDz_4p7fgGr4_jGarxkpme55ReoUFO8EzicXALjeIc5MkvJUrFhs9WERoVJBF-VbfiwVsWqdIumg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705177dcef.mp4?token=cuyFfAEyoAXq4IQxXfo4sjLO1Ci8TRdnk_7wnHhtlHOj7v4gcxXGqIo8IknQdM6wc2ITFdKEuDJ7q6sqDrxubRrf8L7v0pJ-WKpeFyiKRY2l5nFdCRvaZQywTNg1mjvW7qNX1gKvT-Di7JygPVXR4DK-pH5M6brvdumLYfSFwF-YANYGQAKAUmZf-j_ETalTyi9mC8I4Si5Z4QNIEdTzcirA5aEArK19vDGgmuASzn2-3Yq5mWrN3LKeDfjGkvcUrt1pYgctSrcDz_4p7fgGr4_jGarxkpme55ReoUFO8EzicXALjeIc5MkvJUrFhs9WERoVJBF-VbfiwVsWqdIumg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
عشوه‌های مجری صداوسیما روی آنتن زنده که در فضای مجازی حسابی وایرال شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101876" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
