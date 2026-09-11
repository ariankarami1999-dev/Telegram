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
<img src="https://cdn5.telesco.pe/file/g_T0J-9oMiFcHbOwG-iYQulyaeUCybY1nE82xIt_tUkMj_r4eHzPazEr5xgPkYhn1JLFqjMeDo9Eh0n-sw_E8QlSzveSa2Pilm6Q3sCLlNv7CJbh6s5TkOWCOWhefuJ2nwET6MnhNfxLvikj61SWjECDsYynS1wrBcJeDCzUCTkBDsAWC3DUO3m24YubEyb3Q066zMIL2_O_n1rWI8xieTMgkIc9s44oIihAJ2Xqvp-TSWpTr-avHQsbrHoJ-832feQcRYHdUMwANZvLsIeQ6yFPRCaLEc-q68gypUo8-L1LniEHwREvxG1i2rYRoh2RkYa2FUvuHyba1_UNo-JG0A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 418K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 22:23:04</div>
<hr>

<div class="tg-post" id="msg-106242">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
با اعلام باشگاه استقلال، مشکل مصدومیت یاسر‌آسانی جدی نیست و این بازیکن برای بازی روز دوشنبه مقابل السد در دسترس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/Futball180TV/106242" target="_blank">📅 22:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106241">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3e40e30b.mp4?token=e9N57IRG-Y_8Mh0sfkfvfZC47_WuQGVOF5ef7Jowk4QIM0UFQRzks-I0pEnXi6thSS_W_xPd19A4GcA4z5y5bEN9GdM_PNWIQm_buCSLwPubXPZ6j_gVoW8DUZDt-m_jzX-xU_N4eLM_gVjAQWGEgKZL3XsW_Gyo9OhD6eF0LuIkPC7gJvj1K6G4etCJ6MfvUYG0V6YbJqTZIB0KlwK3TvF7oU5YB-o_WZOR1LDgbWh9Oo3gH5-YZX7WJmnyFtjBE6WG_uxY3Tiwsts6lxVyCAUyl3VZ48y4UhUeRxnTHKVyAIHxdNAf09d3xTQOqVfZtmXZtNNQ50wWhzw6U7ThGliFEx0Yf_rBNYLdthJILhi7lUG1JNYppXgC-RE0u5l1elwZIkD3tfYerii6X4etGGPAlA_ilRQHd2Aa0QxyQ7jDh048PtQUZl8Vv2ZtTQbLOhFMS458DcEpQbiHcaFFwXiI_to94SjkwCb6B-XdXbfKo3RrsdXYK-5QVvvbAotUvdOsMEvLB_6MFaKrVoyEote5ZUGgRYnr3ZJ2p6KggigGzxFeFDLMjse23_avhsNgC28E4RZ8SjN7MncMyuJgwMG4LDGUBhuHRwL6XIqKCZ0UmFPBkXo-y8wLKOfJz3f4C1ltCZmFtQ34Y8AYAlyqi6o0MBST0_VND23Z8dHe7Zc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3e40e30b.mp4?token=e9N57IRG-Y_8Mh0sfkfvfZC47_WuQGVOF5ef7Jowk4QIM0UFQRzks-I0pEnXi6thSS_W_xPd19A4GcA4z5y5bEN9GdM_PNWIQm_buCSLwPubXPZ6j_gVoW8DUZDt-m_jzX-xU_N4eLM_gVjAQWGEgKZL3XsW_Gyo9OhD6eF0LuIkPC7gJvj1K6G4etCJ6MfvUYG0V6YbJqTZIB0KlwK3TvF7oU5YB-o_WZOR1LDgbWh9Oo3gH5-YZX7WJmnyFtjBE6WG_uxY3Tiwsts6lxVyCAUyl3VZ48y4UhUeRxnTHKVyAIHxdNAf09d3xTQOqVfZtmXZtNNQ50wWhzw6U7ThGliFEx0Yf_rBNYLdthJILhi7lUG1JNYppXgC-RE0u5l1elwZIkD3tfYerii6X4etGGPAlA_ilRQHd2Aa0QxyQ7jDh048PtQUZl8Vv2ZtTQbLOhFMS458DcEpQbiHcaFFwXiI_to94SjkwCb6B-XdXbfKo3RrsdXYK-5QVvvbAotUvdOsMEvLB_6MFaKrVoyEote5ZUGgRYnr3ZJ2p6KggigGzxFeFDLMjse23_avhsNgC28E4RZ8SjN7MncMyuJgwMG4LDGUBhuHRwL6XIqKCZ0UmFPBkXo-y8wLKOfJz3f4C1ltCZmFtQ34Y8AYAlyqi6o0MBST0_VND23Z8dHe7Zc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
✅
🇺🇲
بررسی حادثه ۱۱ سپتامبر از این زاویه؛ برای دوستانی که اطلاعات کمی دارن دیدنش توصیه میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/Futball180TV/106241" target="_blank">📅 22:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106240">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16ebf2050a.mp4?token=VQICLhFztAjowQkj7UKIpq6aywK0g6PfHax4ZT12WMYYzYADOVJ9Pr9wVLfv2t1YYOopt4FUa_l2M0SEtw7r1yxHhXoPb-oJ0QaUzefOyYmRgla02hniPhyCoK-tUbBNmCirpPi9WavJPItbpoImCQfL2nByXFOIcOiqYpqEOVVIKBtTokoUpzlNPvEVUtLVEXShGsIhrBY6cNavqFY62SuJdwggUgVPLMzXhMg6g4hgyEVXGMI6Syc-VoORFvcfAzaQbGVLe6S7xf_se13EHh399R5ynqrroJW0f2eSmJYs4dW5jOQiBxy38d9PD-es7FskA5qSjK3Jp3mlAuPIDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16ebf2050a.mp4?token=VQICLhFztAjowQkj7UKIpq6aywK0g6PfHax4ZT12WMYYzYADOVJ9Pr9wVLfv2t1YYOopt4FUa_l2M0SEtw7r1yxHhXoPb-oJ0QaUzefOyYmRgla02hniPhyCoK-tUbBNmCirpPi9WavJPItbpoImCQfL2nByXFOIcOiqYpqEOVVIKBtTokoUpzlNPvEVUtLVEXShGsIhrBY6cNavqFY62SuJdwggUgVPLMzXhMg6g4hgyEVXGMI6Syc-VoORFvcfAzaQbGVLe6S7xf_se13EHh399R5ynqrroJW0f2eSmJYs4dW5jOQiBxy38d9PD-es7FskA5qSjK3Jp3mlAuPIDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❤️
محسن خلیلی مدیر پرسپولیس: چرا می خواهند ترمز پرسپولیس را بکشند؟ چرا می خواهند حق پرسپولیس را بخورند واقعا این شائبه برانگیز است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/Futball180TV/106240" target="_blank">📅 22:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106239">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/febf5e7a8e.mp4?token=KvG8a5am65pd2UCvYTpPlUc422jnBaG_LqYH_yO6n0beJihLmhlNTWA7MZofVGuG5LeMI2DX92j85jzE6N7EerQbP_i1i-xb5RrJl6ziSqeP14pxBb7bf0_qaIVSpDEA4OQ8KVuAWcp4jg6Nrw9tr4pGdICXx8L4srSvyHsoenV3tpUnEg9N1A8q2ESpMmD8xypXJRzvoltF75NwDM0n8VNSN37Qvza5dxFX9-U41OwRZdM5TddCnPeLdnTvaNGZmduZbb43rmqJy4ewwMVdiDdD-nAMvnegHQJsHHVp0-Qtpa3oSqDwyNdGVx3R2DqRqs-kJjLTwlbx__wMC1WHkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/febf5e7a8e.mp4?token=KvG8a5am65pd2UCvYTpPlUc422jnBaG_LqYH_yO6n0beJihLmhlNTWA7MZofVGuG5LeMI2DX92j85jzE6N7EerQbP_i1i-xb5RrJl6ziSqeP14pxBb7bf0_qaIVSpDEA4OQ8KVuAWcp4jg6Nrw9tr4pGdICXx8L4srSvyHsoenV3tpUnEg9N1A8q2ESpMmD8xypXJRzvoltF75NwDM0n8VNSN37Qvza5dxFX9-U41OwRZdM5TddCnPeLdnTvaNGZmduZbb43rmqJy4ewwMVdiDdD-nAMvnegHQJsHHVp0-Qtpa3oSqDwyNdGVx3R2DqRqs-kJjLTwlbx__wMC1WHkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❤️
محسن خلیلی مدیر پرسپولیس:  2 تیم ( استقلال و تراکتور) با تیم ملی امید همکاری نکردند و بازیکن ندادند چرا کمیته انضباطی با آنها برخورد نکرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/106239" target="_blank">📅 21:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106238">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a557a62450.mp4?token=H5yg1GtssXxTE8IRdM-JUA7Y71WTd1uhhzbvQhToahtNK07KHTdaSpVob01CIKf4VfduVZjK-4oxa9sDTrKthbUETMz8e0UzjsG554OjvhZ1hiqcHBgZYBPMPBjYrQK2Dh_3ZFOgzBafRYON_xEIJbUkvuDk7a0UDmWxUR_kh2k2vL60Arbm37XNtYIkGXRuq_WIKHg5A2LOOaJKwtxIuHeZRzThyPYIvFdgYzur22d36rEYyIuQJgexbDnMDmj6ebvuiOPWKQGMtq80G1bXMLEJXcqRlu7ACM4g5Cr4XZwnGW-LwDKu0HS3onQXavXebdV33R-DAOFYS_R5I8aYjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a557a62450.mp4?token=H5yg1GtssXxTE8IRdM-JUA7Y71WTd1uhhzbvQhToahtNK07KHTdaSpVob01CIKf4VfduVZjK-4oxa9sDTrKthbUETMz8e0UzjsG554OjvhZ1hiqcHBgZYBPMPBjYrQK2Dh_3ZFOgzBafRYON_xEIJbUkvuDk7a0UDmWxUR_kh2k2vL60Arbm37XNtYIkGXRuq_WIKHg5A2LOOaJKwtxIuHeZRzThyPYIvFdgYzur22d36rEYyIuQJgexbDnMDmj6ebvuiOPWKQGMtq80G1bXMLEJXcqRlu7ACM4g5Cr4XZwnGW-LwDKu0HS3onQXavXebdV33R-DAOFYS_R5I8aYjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینیم دیشب در لیگ قهرمانان چه خبر بوده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/Futball180TV/106238" target="_blank">📅 21:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106237">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dtq6rKVsXQGTGqE1S09Svb4-TzQNWQefROmVCkDXaboczIXHn37fvqnYgN0fD-6LmX3Ept4iPUHXqowbO1qKaS7iB9JFLV8SVKVUw2ynoD_Oz6TtzJ_zPBKE6DcDf8Wsvj_eo5-zCv3UrL2YnVaIbyVfwCIMwvt-UkN4riA_l9CA5P344n1jauGG81Z64RdnNEbXM30VPuqdeNLDDOLjFZm_xKBO6QfmdHn2CIQP1Q67we1oKwsiMbm5AkXin8Qy7VsD_bOure9MGsQJhRqjBOzj0EnVzPlYoH8el88EfTNudsnrjpe4K56Kg8YL1VwV9PZxM4C1ffSzxf_1OCRieg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇮🇹
🇪🇸
سسک فابرگاس، سرمربی کومو:
🔻
«بارسلونا ترسناک شده. سطحی که تیم در حال حاضر داره واقعا ترسناکه. بازی دیشب رو دیدم. فاینورد تیم خیلی خوبیه، ولی بارسلونا کاری می‌کنه که حریف ضعیف به نظر برسه، چون در هر لحظه راه‌حل پیدا می‌کنن.»
🔻
«می‌تونی مقابلشون نفر به نفر دفاع کنی؛ همون‌طور که فاینورد سعی کرد این کار رو مقابل رودری یا پدری انجام بده، اما بارسا از هر نقطه‌ای راه‌حل پیدا می‌کنه. فرقی نمی‌کنه چه بازیکنی وارد زمین بشه؛ سطح تیم همچنان خیلی بالاست.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/Futball180TV/106237" target="_blank">📅 21:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106236">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/525ed46310.mp4?token=BnPvImjLhsRH2wmLlBgOL-adYIQbLDF-3Ro2rFCTWc51YTeGKuaLOCzMpAiVt1K9doi42DKT0ohM7l22QbLSG6mReS1rd0UpqBpcfUPXm7mFkpQpPvU1mSxj6W7dFjSWRAil2CbJ8rCaU7Im-za-FTuBkzruNjYFHcrMl42ELU8C040ypMumekAaDr2jeLlsKGKtJ2B1VDTWCbpoiAHMd2fjJcRFYPhRXg6Z4ETubOBGhe7j0LADhj5rSWPb49FpCuQtLw-ncIeHHMOrv5gaq2WYLi2p0CM2K5AWfuxklipL3Hxza291FVZwA6xa_cUjGwYAd_PvqCH2dzSP08PQbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/525ed46310.mp4?token=BnPvImjLhsRH2wmLlBgOL-adYIQbLDF-3Ro2rFCTWc51YTeGKuaLOCzMpAiVt1K9doi42DKT0ohM7l22QbLSG6mReS1rd0UpqBpcfUPXm7mFkpQpPvU1mSxj6W7dFjSWRAil2CbJ8rCaU7Im-za-FTuBkzruNjYFHcrMl42ELU8C040ypMumekAaDr2jeLlsKGKtJ2B1VDTWCbpoiAHMd2fjJcRFYPhRXg6Z4ETubOBGhe7j0LADhj5rSWPb49FpCuQtLw-ncIeHHMOrv5gaq2WYLi2p0CM2K5AWfuxklipL3Hxza291FVZwA6xa_cUjGwYAd_PvqCH2dzSP08PQbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
😳
😳
اینارو از کجا پیدا می‌کنن
😂
- کارشناس صداوسیما می‌گوید ذخایر طلای بانک مرکزی ایران ۵۰۰ میلیون تن است!
یک ۵۰۰ میلیون تن و یک ۸۰۰ میلیون تن دیگه هم گفت تازه
😂
حالا جالبه بدونید که کل طلای کشف شده توسط بشر در طول تاریخ ۲۲۲ هزار تن بوده
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/Futball180TV/106236" target="_blank">📅 20:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106235">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e059f4f8a8.mp4?token=ZWriskzAXy_1DRrewILDzEJNqHoFo1AB3ingdbxU6FjCQrnMENm4QvZmSRH192s6hjozuJURbXsP2dEg1eD4lvgcpVfKOBD4xl3ENPX9qNlRdHe7aijQHHhbfU5gUCQWQA-UOXgWwO36HDpSTdprLq-lyUxb_hlycdyNdCGOgg6OIz9cJhnqGc5MkxyIdonMjMEaweMf6IRnJOnuv3L2pSx6CA9lg6VMoKuijONOHUA7COsjxLKnk32M8nuN-1XBA7xLODMhbdWHvCzxUOvMPmMRQB9Q3V97gNUII8j8AXqeDcLGabrzW6TUzIQR7ypL36OEgilMF8UVLXxORHptTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e059f4f8a8.mp4?token=ZWriskzAXy_1DRrewILDzEJNqHoFo1AB3ingdbxU6FjCQrnMENm4QvZmSRH192s6hjozuJURbXsP2dEg1eD4lvgcpVfKOBD4xl3ENPX9qNlRdHe7aijQHHhbfU5gUCQWQA-UOXgWwO36HDpSTdprLq-lyUxb_hlycdyNdCGOgg6OIz9cJhnqGc5MkxyIdonMjMEaweMf6IRnJOnuv3L2pSx6CA9lg6VMoKuijONOHUA7COsjxLKnk32M8nuN-1XBA7xLODMhbdWHvCzxUOvMPmMRQB9Q3V97gNUII8j8AXqeDcLGabrzW6TUzIQR7ypL36OEgilMF8UVLXxORHptTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
فراز کمالوند سرمربی خیبر: الان که پرسپولیسی‌ها مخالف هستند 3 ماه پیش هم که پرسپولیس اصرار داشت تورنمنت 3 جانبه برگزار شود همه مخالف بودند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/106235" target="_blank">📅 20:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106234">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmFtdxztLJKPir9DKFgBliy8PK7tGUEixPp8E6lUemmq3YzTQ3fFoT3tGR_4qxEx8DqBZU3apm5KpMd8TgzHQAhbVgY1YxfNp3_lgbRcNXLn0CvRolX3l-vD4fksGpeqr7-W2iEIDnHbVM7l8rYxUJ2ygCRmufu62Grj5N8q5mn6sHYjZmywbvlf1xjfO3U1NPx6VMtsL4xHJKc43OTP1O1ywWnc0R_WkpjjV9DahwCYDpDbO5ZkIOFI7b6SZ-PKo4JM-uYm6okK4HZW4k3D-GVPMR2pp-sqrZDwchoGFaA0WodTAawkC4nHSO2_kUxzuiQ3ww2VaL0w9Sr3Ny4ktA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین‌ماهینی عزیز و همسرش
✅
🔥
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/106234" target="_blank">📅 20:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106233">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d8215d3c.mp4?token=R_SBVVIsqdyUzYIfjUCL0kMBm2pIdIT-_sKbBQ72oUK5PjjH0BKw39onV_1hu44JX59ZW1OrsGXwwIMRACARXU7w6QFmvWyxmU-XeSkdOFTxJZeoZTCuG0m4U6ibtGmTeAlrjZnD81GjYNS_eQk-hkl3pwznxHKeL64CumbWtDvI9ydVQPrWUVu5qDgJ2dO_UkJpZuaH4pKDHwCYs_Y1o8fjfTNcfafJiBQ-o8vUYMZNpyIfqEMi4U00FoOzf04tjjDX9gsRF0fcxyz9J-t_u5yK2n2AClWIGzwLn99_m4iVdVR2tvC5-TL-eCUAfImwVNutiP8DvR24NtX8Y0YlGyLqPjGcX8820DM6uGwN3hCTrA2NfMx76Nihem-MDMI8ZB4j-v78mFNHXtD06Ljr9yFXpa0Mg7syfDN72cYk6vormEXeNu6nfikNZJLSofD_IeRhWf6TAf6K9Zb-uGfyrxTbFSU2HFpesUBwggN1hajpILsBSGfo7jgeVkjYRBg6Vp6lMiCUDymw8a5HjxoiLpfMygMQl3vMVwItcuWZs59IJMIxd9Xmd8wKkCFb070AEy-smMzgj_9ZCoVXm232va4rO_q99YP8W4X9qd-6ZGqZV8uMFeNT0p0-CKiboR1ulHYtao3OWNuRa8G4W2w01PgFQY0JOxXA_RT62wYD0bE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d8215d3c.mp4?token=R_SBVVIsqdyUzYIfjUCL0kMBm2pIdIT-_sKbBQ72oUK5PjjH0BKw39onV_1hu44JX59ZW1OrsGXwwIMRACARXU7w6QFmvWyxmU-XeSkdOFTxJZeoZTCuG0m4U6ibtGmTeAlrjZnD81GjYNS_eQk-hkl3pwznxHKeL64CumbWtDvI9ydVQPrWUVu5qDgJ2dO_UkJpZuaH4pKDHwCYs_Y1o8fjfTNcfafJiBQ-o8vUYMZNpyIfqEMi4U00FoOzf04tjjDX9gsRF0fcxyz9J-t_u5yK2n2AClWIGzwLn99_m4iVdVR2tvC5-TL-eCUAfImwVNutiP8DvR24NtX8Y0YlGyLqPjGcX8820DM6uGwN3hCTrA2NfMx76Nihem-MDMI8ZB4j-v78mFNHXtD06Ljr9yFXpa0Mg7syfDN72cYk6vormEXeNu6nfikNZJLSofD_IeRhWf6TAf6K9Zb-uGfyrxTbFSU2HFpesUBwggN1hajpILsBSGfo7jgeVkjYRBg6Vp6lMiCUDymw8a5HjxoiLpfMygMQl3vMVwItcuWZs59IJMIxd9Xmd8wKkCFb070AEy-smMzgj_9ZCoVXm232va4rO_q99YP8W4X9qd-6ZGqZV8uMFeNT0p0-CKiboR1ulHYtao3OWNuRa8G4W2w01PgFQY0JOxXA_RT62wYD0bE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
آشتی جالب هواداران نساجی با مجتبی حسینی سرمربی تیمشون بعد از فحاشی اخیر به وی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/106233" target="_blank">📅 19:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106232">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gp6gJhtgz1OVdwwFt22Gx7hepGogV7dM6JAGOEYyLQ5tqUChXWrXaelAMh3SMuLki_IRN8uOyZ0typ68fUCk1McKNrzLEq4wqmjromWC1CSpuuFleBJoUkShm2A86s-qiIMrHFaZxv-1KrWTecNRVWmENI-ksYC2DuECxXfM_rD5BJGWgZDZcme-2vP5pFasWxmya3qvBI96lytHRcGmLBpgNuDfx7DHwi_5IhRpyAZnijQHrcMUXa-ZPlRdwwzJwacQR7UM0wW1PGlL0stiJ-QHj7_Dmixtdkqv-ePxANFQdi2KbtN57o15NBpT0q9VyT01iRdsLqAilt2LfNtZcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🇮🇷
طبق پیش‌بینی‌ها، یکی از پربارش‌ترین پاییزها برای ایران در راه است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/106232" target="_blank">📅 19:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106231">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be84e2f3d7.mp4?token=KVjhAoV715oLQ4q85fmlMHqX9F701dZZwTD_OYH7NiCv9e6WAheAsDB2kpWP8BnwI1tMQO2YceTsAq_0JXUoSuzNvXczj19Il79_U-c3gUU2w36ljmF146yI60BpFKuezM9QqRoL-TrZDbu06BKQ6pYpkdlAKJme4ks_x6LAoqtpf20hy4tRuRArwwSwf0q_VisYKkMPGNVDiDic73Hw6m9wMnGtwtHOsLNMoSWMIAgVl_Js7bN4vutdDf2K3yIaeX4L91iqhmdYugqwN65zsRu3cjMGEERAq7aS2I8aJFs3moULk21HXXl8IfJLOJ4h4t383SnHPxmqhVLWFFOlLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be84e2f3d7.mp4?token=KVjhAoV715oLQ4q85fmlMHqX9F701dZZwTD_OYH7NiCv9e6WAheAsDB2kpWP8BnwI1tMQO2YceTsAq_0JXUoSuzNvXczj19Il79_U-c3gUU2w36ljmF146yI60BpFKuezM9QqRoL-TrZDbu06BKQ6pYpkdlAKJme4ks_x6LAoqtpf20hy4tRuRArwwSwf0q_VisYKkMPGNVDiDic73Hw6m9wMnGtwtHOsLNMoSWMIAgVl_Js7bN4vutdDf2K3yIaeX4L91iqhmdYugqwN65zsRu3cjMGEERAq7aS2I8aJFs3moULk21HXXl8IfJLOJ4h4t383SnHPxmqhVLWFFOlLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
به مناسبت سالروز واقعه ۱۱ سپتامبر یادی کنیم از همدردی مردم شریف ایران با آمریکایی‌ها؛ این درحالیه که کشورهایی نظیر عراق جشن و سرور به پا کرده بودن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/106231" target="_blank">📅 19:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106230">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URm56nhe7ooyqOZbhauxqi5Mc-cGW8Ayj9PCf1-p3w2ZSJ4m3ROj8Oa3gph1c-GMc6MK9i6hyaWiSl8__Cdl9VzzEFiha6--WkksYahMCQjjnTGlHLJfKJau-ZvlOksl9b0RcFoCoDzXaVQ_hKhD189AH0AhGWBJlEibRcd8kfGOstJfvQdn4cgKnPYbgKgfkV9gp1DDo63NrF_kQsjy51rMAKid263y-lCmE34xqc4Jg_GR_82ogwmhgHC2_Ge8n8OKGGAYgbL5wyYytZBVnDX7uOEQQIBGkyAWvCG827Y9L8UixdWI16wnV8hriYIcIEkLKeXXS5zSCNyCJZrH4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
👋
گئورگی گولسیانی مدافع سابق پرسپولیس ‌و سپاهان از فوتبال خداحافظی کرد. گولسیانی زننده گل قهرمانی پرسپولیس در لیگ بیست‌وسوم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/106230" target="_blank">📅 19:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106229">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNJEJ_5LpyraOn7FouifJ8BNnuXgHTnUyOx6gJIgk-4-wjRi20VLO3gWVVaVq-PP8_y8fur-G4VfcETC4gSRcWnGSVD8xJxg-k6ysvria9mrvGc461TOnjfxEEr4uSYewYTFHXnOQcCfYCGlcRXCPogl3pahLHeCgNRlHJEutaN0ydRjxBZskrb_tUBPoPdm1f_Jxo52O2yMGUQYQW0g613lHerba_UBJa9ST6-EqWnZa_Jcl1nYLdhMChjoFpO1VYHnVaNJ2_FUTlKiW1IZuwmI-ldIdNlc4SdqKUVWt7btQ4YsEc_z1lII_r9mx4JEERln3x1OvrP2bDPvTPguEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🔥
🔥
🔥
اکتبر خونین که در پیش‌داریم!
🗓
🇪🇸
🇫🇷
20 اکتبر/بارسلونا - پاری‌سن‌ژرمن
🗓
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
21اکتبر/آرسنال - بایرن‌مونیخ
🗓
🇪🇸
🇪🇸
25اکتبر/بارسلونا - رئال‌مادرید
🗓
🏆
26 اکتبر/اعلام رسمی برنده توپ‌طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/106229" target="_blank">📅 18:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106228">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106228" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/106228" target="_blank">📅 18:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106227">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VliDEZCNJZXcgt5wC_bpFUo72XloO4sOwIHDSq74PULqnRY1-PPeiuckX7MqBcVe4Ti-a-1CEdcjE7ECdwzXt1qwg9BcUTEteos4B6qjmDBOrnRRwsppgpKiHAWcD-7NGIrjZLxx1xGNZwP2QQ-c02aiW003wTSTOoYYuHFp8wRIgd6HeqhlTueny8R_gY1WFePNvQHsmJhCTXAuHV_GRfDaCUlWPzLd3LgDTWamp3sNEUL-YMt2ZW63ibWZx1LRKmegoF7d8-I_h_maAzOe6B5lsdFsjS0yAQaYy9kQ4iCWTh-WEN6E7dL3BRSSqmwKkUPnaNcT1VFV_UL7kkaEug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/106227" target="_blank">📅 18:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106226">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2YLmWotD85HHpPyghyeHUl2U7sRkYAevwbU4S5LG6_HZaFz2dySck2ZbjExxy8m3ol_gwaeihPywi78JSZWhtLmU7v__HbeK-Uc11H4W5Q01WGva-P-map65V4rvXpYUc5rLJzvHpvDIo605QNdR3rHQQyj1rv95x8IUeySoJkBm_k5pnMjqyiUfdc2nkM2i6K6S6B-q4zgV_SHrsFxd7Wv3_AxULVxPI69idXUgItWpCr8U3ip2r0LuHK8ANGE7cHTVlM2GnN7MUTQaC5-PR6wqSNYwyfcNoxnqUQoxqInfaDQcxaM_bVQ1VHewbNfOIy4BoKz3sRoZj3Sihnw1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇺
تیم‌منتخب هفته‌اول لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/106226" target="_blank">📅 18:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106225">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e1c6bb479.mp4?token=JNKlsV_E_reZvEglkT8wprxJkYvGXKQ68q7lW-3i7DshqyJzWHd_Rk0spzVnuR3gSkSxqupFxF8WbIHYwVt9Gf6D_XjjbGl_oUSgoPcnAaWPPZM9Zv1JPPOUKbkrycB8b0jrbMRyQ9dRapxlsCeFWK9Kdjm3MWhH3NM1zmMZe0JGsj4dO3gh15ELeq0WTmWc4ZdMZObNVSYzJt023qhZmF8tTXfYheQJnXTFQ4P8diVpZVq45Op5jlNO8V7LEx-ZeP-lRHZ8ZsArXFchXu7DwudiZRE5DC-Vj4Tho2vO3vHHI4yu-LKmD6elWjwjTw6ESgtTE2xzX1Nbb8aYaAXYaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e1c6bb479.mp4?token=JNKlsV_E_reZvEglkT8wprxJkYvGXKQ68q7lW-3i7DshqyJzWHd_Rk0spzVnuR3gSkSxqupFxF8WbIHYwVt9Gf6D_XjjbGl_oUSgoPcnAaWPPZM9Zv1JPPOUKbkrycB8b0jrbMRyQ9dRapxlsCeFWK9Kdjm3MWhH3NM1zmMZe0JGsj4dO3gh15ELeq0WTmWc4ZdMZObNVSYzJt023qhZmF8tTXfYheQJnXTFQ4P8diVpZVq45Op5jlNO8V7LEx-ZeP-lRHZ8ZsArXFchXu7DwudiZRE5DC-Vj4Tho2vO3vHHI4yu-LKmD6elWjwjTw6ESgtTE2xzX1Nbb8aYaAXYaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
پخش‌صدای بانو هایده در مراسم هفته‌مد در نیویورک آمریکا؛ روحش شاد اسطوره
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/106225" target="_blank">📅 18:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106224">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8904bfcc25.mp4?token=X7BxrVAcK9HF989Wt_cvUicgAxZRT46kGipQzpW99tqhwWrgheE0cQ1ML6NpC8IXUQ-WFHW-_8OIuRf-5auF02kFUbowYn9sgE0EzMu1QwslA952lvZeIKdL7sEimRNxgFfSFyViEIn85s8VJ8j2auHfFoF5WtW3jU6MNLG2fp3vTH_wzsSw8dxM9RsKO0s4fkiwyCHgmxYUqfEUjmC4EbxptDtueGXEOZCN61SQs_Q52UHMLdPk4GijcmnUbCz-7nZ0vfitpa-_6kmbavi3eawk3JK8WBrtriwyYaw93MEsw833HM77R_xV2Qe8tP0zv07OpvdBdmH4xxkye5jMEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8904bfcc25.mp4?token=X7BxrVAcK9HF989Wt_cvUicgAxZRT46kGipQzpW99tqhwWrgheE0cQ1ML6NpC8IXUQ-WFHW-_8OIuRf-5auF02kFUbowYn9sgE0EzMu1QwslA952lvZeIKdL7sEimRNxgFfSFyViEIn85s8VJ8j2auHfFoF5WtW3jU6MNLG2fp3vTH_wzsSw8dxM9RsKO0s4fkiwyCHgmxYUqfEUjmC4EbxptDtueGXEOZCN61SQs_Q52UHMLdPk4GijcmnUbCz-7nZ0vfitpa-_6kmbavi3eawk3JK8WBrtriwyYaw93MEsw833HM77R_xV2Qe8tP0zv07OpvdBdmH4xxkye5jMEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇺
برخی از اتفاقات هفته‌اول لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/106224" target="_blank">📅 17:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106223">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3be86e9eb1.mp4?token=pvoCg3sOJVORth8l0UNvt-ecDd770BqHobxnOkSyYjXHdrKhoTD3805gk0PRsZIJYPY0OmPo1urY8L7QMREMHsrW1JBZYu87YGEiYE-Yrxamk-E1-OO67x6slmhBLxkkGDcJIRiRtVGnwTUP3ZT9w22y57Z-kya5yF5mDi74OA9SvgPDcLFnxp-TvhUunU72M_KbHz7OPS4ql4ojSdCSzwh9t4ORudFFj-Q2zpbRwHYbIEk7ExtCX-nmPbSlNQjORTNlsowNagOwL0pVhCuyP0kgkcDub2LeZeRJ-eSZjQdDgAR_ob9p7zuWlyB5DytVXa123aScqBfwqcd-BrQA9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3be86e9eb1.mp4?token=pvoCg3sOJVORth8l0UNvt-ecDd770BqHobxnOkSyYjXHdrKhoTD3805gk0PRsZIJYPY0OmPo1urY8L7QMREMHsrW1JBZYu87YGEiYE-Yrxamk-E1-OO67x6slmhBLxkkGDcJIRiRtVGnwTUP3ZT9w22y57Z-kya5yF5mDi74OA9SvgPDcLFnxp-TvhUunU72M_KbHz7OPS4ql4ojSdCSzwh9t4ORudFFj-Q2zpbRwHYbIEk7ExtCX-nmPbSlNQjORTNlsowNagOwL0pVhCuyP0kgkcDub2LeZeRJ-eSZjQdDgAR_ob9p7zuWlyB5DytVXa123aScqBfwqcd-BrQA9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم تشیع جنازه بابای مسی با علی‌آقا دایی
😂
🚫
با صدای کم‌گوش بدید فقط
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/106223" target="_blank">📅 17:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106222">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8jduY8N4wIVfp_Co9301ycYNCYHDp0ztMsGvOxIjTl_0FLD72mCmdjtDVd0sYerhs6snw7qPetsS5iX_Ge9m3lNI3o_6hn7CR6oC2UsJA6fXGNQPnxY6C0p3aSOFeunpm915Ze9EcbLEM_y5UVKuhJp7Fl4favTwAXq51YvBx_T73m-sVCpKSLsz-lYPa2_Dz1I2PJ8izfsJ9G8b_P4r5usKwr-fwNfhAP6DwW308-7VplgHbGC21xG7fqsJJcS_zW2XhLoX9RH9jnPR77Ljs7_xYfi130OwPChKZyF0Q7it7SPjRGC9lIj4nGQWhYTaBSxe8r45xWhU8CIjuwBcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
واکنش علی تاجرنیا به بخشیده شدن صالح‌حردانی توسط بختیاری‌زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/106222" target="_blank">📅 17:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106221">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d24125c19.mp4?token=RDs_PAWMpxuu25pcW5AS5Q-MeosjQgqmltsWUo7Tx0YwC-dkHJnY6CFRDTNyFs6TuASwr6dSH0yYSbe3nqKlZUxzW61iHyGxGlC10QZAXCdZmdBOXDncMZW5ihNLDMypUMGIl8pOLxldhCMtVKFViG_ii0Gi3D9Z0aeoOqCgOTd8wJQwQHsLQgl8ir0iOgbBVyXHaD_oMK2Cjg0Bzg5U9QYkL-XfEGbMTytUIC4sRMNhVzKDIrnsTrIDVafelQUClU-0Ou-EieusO1P-OG_BNNoH1MrpgDFwzuVKSuGNKYOZWD9LngFFd2yIwcVj_jJ0qw_zjVmiTGoADcciGQ1sEHj84RPrL-omVmcQwhiL1gSgUWTXNN5WWd_HvaoeznxTKnSiAIEFCMtyZiHhl6eE3E6IrSKvGmu9bOUK4h3EdGwo-7Pe2E0tqNsjrJ3j0PjKHDMBCYmspl2Ae8NWTB8jy21-bFyhfIP5Uvvwka6lv4rVP7GOsSYVwDLzshVLmeCU27TAksYhpp6P6_LBtjcvJrsCkr3up_19Nsg7cpn7CiXc38k0PeqvuFBMBGKKhuhDZeqO4jkXE79yziGPJAvmP17fwHTpsesM88ehpCmDKf1lDawgQiIrKLcVWr-EqKEUzyySYQRxeSnm13h0TewwN9f9a2KKiZhINXlx-OCN2Kc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d24125c19.mp4?token=RDs_PAWMpxuu25pcW5AS5Q-MeosjQgqmltsWUo7Tx0YwC-dkHJnY6CFRDTNyFs6TuASwr6dSH0yYSbe3nqKlZUxzW61iHyGxGlC10QZAXCdZmdBOXDncMZW5ihNLDMypUMGIl8pOLxldhCMtVKFViG_ii0Gi3D9Z0aeoOqCgOTd8wJQwQHsLQgl8ir0iOgbBVyXHaD_oMK2Cjg0Bzg5U9QYkL-XfEGbMTytUIC4sRMNhVzKDIrnsTrIDVafelQUClU-0Ou-EieusO1P-OG_BNNoH1MrpgDFwzuVKSuGNKYOZWD9LngFFd2yIwcVj_jJ0qw_zjVmiTGoADcciGQ1sEHj84RPrL-omVmcQwhiL1gSgUWTXNN5WWd_HvaoeznxTKnSiAIEFCMtyZiHhl6eE3E6IrSKvGmu9bOUK4h3EdGwo-7Pe2E0tqNsjrJ3j0PjKHDMBCYmspl2Ae8NWTB8jy21-bFyhfIP5Uvvwka6lv4rVP7GOsSYVwDLzshVLmeCU27TAksYhpp6P6_LBtjcvJrsCkr3up_19Nsg7cpn7CiXc38k0PeqvuFBMBGKKhuhDZeqO4jkXE79yziGPJAvmP17fwHTpsesM88ehpCmDKf1lDawgQiIrKLcVWr-EqKEUzyySYQRxeSnm13h0TewwN9f9a2KKiZhINXlx-OCN2Kc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
یک‌دقیقه با کورتوا بهترین گلر فعلی اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/106221" target="_blank">📅 16:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106220">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0df98090f.mp4?token=psw00VhHxpJ_Aw0GzA3tb6ocpNDgMEcRoN3nxMI3SaueavD_KK_7lmgsRl0250sNO_NWu5yAMwyPODjGnoUYwOO1vmOtQeBh5dWE8CPJarPSuE-9rG8PxkMKl4YiXtVIcu3RgNtXJoS43_5x2jKcbEQiDD1rtttU8Bt2g_pIIg7H5zRgB3MnWnISnATIqRqq39IYAoHHmJcknKbKB2OEFLWr6ZNDkWVgAI60GS0-wbO7aAtX1uwai9QXzo-zW0uvoj3PKpHRACWY1RAvxjfjJNuTgzTGnAjh3m5mrZSo9U8EQQ8EJ56_zOMj3cg-qpsh1mIpw6CEuWEFZOy7_BJAwAGHy0bsosiYtQMRMxzGI8J0rPpPilQ3aUMCbflEg4OsG8Mx6hCqVVRe7p9VwNytzxk8CYYmrpPL8UcMPDuXA_a4P6XuyQm-yC7zZ6hWscIeuOgUoKKeaVMJIpZAW6bNmun0l70jyWcwi6FNZv3aoPMMY46G9Qju2dEALWLqzVWfywIYp1WeBl_lPObpvfQ1-m3bmAgBlpFelIyFgq1fnbD9-7LhRhbIekGKrQ5qIld4UkCgW_4Bz4mKJrMiL1Lzqu1AB89M-sry3aUL-1Z-gXqaaUzRQ9SCYiAe3hEU3OQQbv2FF_YwaKjlpwc77IsLggwBC47p4iOopxB3LOEpXTE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0df98090f.mp4?token=psw00VhHxpJ_Aw0GzA3tb6ocpNDgMEcRoN3nxMI3SaueavD_KK_7lmgsRl0250sNO_NWu5yAMwyPODjGnoUYwOO1vmOtQeBh5dWE8CPJarPSuE-9rG8PxkMKl4YiXtVIcu3RgNtXJoS43_5x2jKcbEQiDD1rtttU8Bt2g_pIIg7H5zRgB3MnWnISnATIqRqq39IYAoHHmJcknKbKB2OEFLWr6ZNDkWVgAI60GS0-wbO7aAtX1uwai9QXzo-zW0uvoj3PKpHRACWY1RAvxjfjJNuTgzTGnAjh3m5mrZSo9U8EQQ8EJ56_zOMj3cg-qpsh1mIpw6CEuWEFZOy7_BJAwAGHy0bsosiYtQMRMxzGI8J0rPpPilQ3aUMCbflEg4OsG8Mx6hCqVVRe7p9VwNytzxk8CYYmrpPL8UcMPDuXA_a4P6XuyQm-yC7zZ6hWscIeuOgUoKKeaVMJIpZAW6bNmun0l70jyWcwi6FNZv3aoPMMY46G9Qju2dEALWLqzVWfywIYp1WeBl_lPObpvfQ1-m3bmAgBlpFelIyFgq1fnbD9-7LhRhbIekGKrQ5qIld4UkCgW_4Bz4mKJrMiL1Lzqu1AB89M-sry3aUL-1Z-gXqaaUzRQ9SCYiAe3hEU3OQQbv2FF_YwaKjlpwc77IsLggwBC47p4iOopxB3LOEpXTE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
واکنش مجتبی‌پوربخش و علیرضا مرزبان به تصویر تلخ دستفروشی یک‌دختر خردسال در استادیوم اراک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106220" target="_blank">📅 16:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106219">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6ANU2-kyxp-oxUVoGEpntamnWrdqSZok76D2u92h84R8oo09qa92TSZVXDj1TfpWrl3ccTiepWGTE-tljB2Ii_Cnz0zPYvsRoxW3EZ8bqi7f4S4MSUInSdrKhLz7QfzhDxLciOOdonpenZSnJIGJus6RccERcnUU3SE3HAqrvN0lCQpx1FUoHcL8qoD_lELA-barf-pQVeYabE2vMgeW0qv_Xm5mC7S1Q8bhM_kQeQ3mrzkCeWzuV7Rh6JfhS87UkDqsG_jnC2S5Fq8bkc7t_6WRYUUR-yqMjyfi8tXTkQassd4jbdWIf_R219TTVSs6k5-povPXWiiLaIUvCqLaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
‼️
📊
🏆
سوفا اسکور: مقایسه میانگین نمره رافینیا با نامزدهای توپ طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/106219" target="_blank">📅 16:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106218">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kth7B57sV-h_kMvnKBBJ6ghtlqmcPeHc9BLQW2dZmn224572_yK0NiGol_RMVYzFal6hP3GvfHNrsubnVCtHEaT-wBJzyA3uvY5yPsundCwM-d2LW8w-bXMF1LxyP3MzievyX6bEj6Envc0ZQDQIoYH7yr1E8v6JhOvanJSmb9ecH5VAcZ6_dMvCEc7P_v7w3g_-ti8Y0n3UqC4aPFVNNccSJeIS39VpaLRzokS8I8rsKyu6t5qszLhyRk7uzH2h-eVy-Sd32Uf8SpzUAEhfKRuVIikUzad-_6Y3CMXbAiykP2YWr5z5nmV6H3EGtBkKMKWwZZu0ckc8KSKIPLnW8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
امار و ارقام لامین یامال در کریرش
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106218" target="_blank">📅 15:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106217">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e638c5ef.mp4?token=c7-ozvUJ9uR9ZmQpL07alevuQstbMoD15Juq2QooF1GfGgFO9G_4nSK20PoX0qh9t1qZA1aP5Uvw7rviTVJAT0vjAoOP9969H03gj_FSoH2bEiO4sLnohTSK4f-rtwbR9WRc1IrhxTySm2N-7KbXdwI0NPCHeYI9god8GnTlPHF9qwY4rOS-UjnufpKqmi-fW5PqiMSezzzWeZyY8vWzJGmxAmuyB6VlRu1mkDFmbxR7X3POO9NuCFekSV84XLwybksa8vsl_Kg2gKn0cx00caiCfoniPv3M2jg0JNndO8xau-OF6L1nxZgBWpEVIHLpIKyH3_ShgJaoBDXOL6rt_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e638c5ef.mp4?token=c7-ozvUJ9uR9ZmQpL07alevuQstbMoD15Juq2QooF1GfGgFO9G_4nSK20PoX0qh9t1qZA1aP5Uvw7rviTVJAT0vjAoOP9969H03gj_FSoH2bEiO4sLnohTSK4f-rtwbR9WRc1IrhxTySm2N-7KbXdwI0NPCHeYI9god8GnTlPHF9qwY4rOS-UjnufpKqmi-fW5PqiMSezzzWeZyY8vWzJGmxAmuyB6VlRu1mkDFmbxR7X3POO9NuCFekSV84XLwybksa8vsl_Kg2gKn0cx00caiCfoniPv3M2jg0JNndO8xau-OF6L1nxZgBWpEVIHLpIKyH3_ShgJaoBDXOL6rt_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
از مالیدن روی آنتن‌زنده و صحبت از قناعت تا عروسی سوپرلاکچری سامان گوران مجری صداوسیما
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106217" target="_blank">📅 15:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106216">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225d461ea8.mp4?token=AnBTAfQKYgwMxVI6rYOWJy2nfyPlXPRO5HM_gPhjZ7qf6Lbit1vzIMXyRbEGlUC9z2ADOEdx0FuIrP2JtAzJ2BXY20ycak4q9jBOzTm41M_3LEbt0CqOrR58u9oqrZ2Y0rFch2oHxcOTgDkRF8156LOtqiS_q6h__7E-xu0c49am_CWz2xA0exST7-G1kwMZRfR1H05JK-XsSPWip2saD8mKAiXp1M-jKWZc_9q4Shzp8Nkr5g-_4evUKdxJysZPA61VmiCvRhcjZmVsto8jfPt24ytSmZKpzH-ZszfWiOTieQF4Brk0-Ojx9QioJTn3rdNSTWobgTnB8yIZkGVNSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225d461ea8.mp4?token=AnBTAfQKYgwMxVI6rYOWJy2nfyPlXPRO5HM_gPhjZ7qf6Lbit1vzIMXyRbEGlUC9z2ADOEdx0FuIrP2JtAzJ2BXY20ycak4q9jBOzTm41M_3LEbt0CqOrR58u9oqrZ2Y0rFch2oHxcOTgDkRF8156LOtqiS_q6h__7E-xu0c49am_CWz2xA0exST7-G1kwMZRfR1H05JK-XsSPWip2saD8mKAiXp1M-jKWZc_9q4Shzp8Nkr5g-_4evUKdxJysZPA61VmiCvRhcjZmVsto8jfPt24ytSmZKpzH-ZszfWiOTieQF4Brk0-Ojx9QioJTn3rdNSTWobgTnB8yIZkGVNSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
▶️
حس‌واقعی هنر در ایام‌قبل از انقلاب با حضور ستارگانی نظیر بانو گوگوش...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106216" target="_blank">📅 14:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106215">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2irbqJ6dm3V7E3l8atHQxS8u3FK44Zmc6uYwm5AoAt9b89S2TWIct7pWogFSQFJ7znxvlGw5xJYe3GFyuUUs5eLr-7qSBSXLuJnJk1vKRnpQbKJyXcKHsu5Tt6P1V5M6yRn6o5S98vegCLL4vp0Yot8KS2uGUzWLo_FbuCRD1BOY4vXULoL2kRXYkVaiaV6KEqXhmjFzRct9iSa_jTQlG4o90Wl3APWsFeoL21LyIeBweg6zRMRNJef5Yt07G5eFAzloWYativaIud8qSgKQ3Iod7kfR-I6go93UNtsZaKQJDTbsYcyed9vdwsoRlBVHADJWr_dsdQELcpGgCs8ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💥
🇪🇸
عملکرد فوق‌العاده رافینیا از شروع‌فصل:
🇪🇸
الچه
⚽️
⚽️
🔴
🇪🇸
بیلبائو
⚽️
🇪🇸
رایووایکانو
⚽️
⚽️
🇪🇸
والنسیا
⚽️
🇳🇱
فاینورد
⚽️
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106215" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106214">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2cd36180.mp4?token=dwgjocTWZsMoMigas1p44snyxg8v6zgpdYXnLa6fiwAXG_nn-CT1M_GttIpLB15i-PUf9Axl-NigizARuy_mD7r9roKfV1iSDIRJH8BRUeta13toJEeNdBdoyCwJzk82i7iKl6VINOdSgZ6lwKCXryeBwdFxXx0_Ox9IxLAHxdRM3D7PdJJ_k_M3fCxVh7z_Ue4061DDbti9dnLw1tRhU7xQ_1c631s-s8ZeyXrQBwP8c5zdsAX85gz846sVCCss3jxvDNQ71L4c3U0MDi9i7W_vVBGCNaiygsubhNQ4TInDgBh_5RwGDCcvQypebIzGjANoG3elweJep0L-2A_SIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2cd36180.mp4?token=dwgjocTWZsMoMigas1p44snyxg8v6zgpdYXnLa6fiwAXG_nn-CT1M_GttIpLB15i-PUf9Axl-NigizARuy_mD7r9roKfV1iSDIRJH8BRUeta13toJEeNdBdoyCwJzk82i7iKl6VINOdSgZ6lwKCXryeBwdFxXx0_Ox9IxLAHxdRM3D7PdJJ_k_M3fCxVh7z_Ue4061DDbti9dnLw1tRhU7xQ_1c631s-s8ZeyXrQBwP8c5zdsAX85gz846sVCCss3jxvDNQ71L4c3U0MDi9i7W_vVBGCNaiygsubhNQ4TInDgBh_5RwGDCcvQypebIzGjANoG3elweJep0L-2A_SIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرمین یا بلینگام؟‌ کی بهتره؟
👀
⁉️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106214" target="_blank">📅 14:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106213">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ol_imBX8xhehwAP0lBc3jyH0i8uPicsqny9mBLQCEgolEE1ASqOCWZDFJZKBbaniaiDUrMkVcFw2PYVc-0p8c8w4yaIek6BzH15dOxLcCaoselbt6NCu_y6MrcZ5E9dkJpJMJGWj8IYSBgL4UJINAp5Be0TOzADWFiie0KcngxnJsGMKjoPW_HeZqcV0_TvVdwWaCiwC1nh4YnHIttRWm6HxEQAhDv2RXbRm4QWijzShldtR45I-m_pyCuzfI-BisuTU2n914dn_2TC52gv6hapczimcOE5YRz4VVm8afixrrT9nPSiL09iBbU7tnZm7sctY6-Uj2IFd8yQtc-8z5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد درخشان مورگان راجرز در چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106213" target="_blank">📅 13:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106212">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4258e2b29.mp4?token=ZpDi6BcNhv6m4JN8YfUOOQu8Q4Wh6GcxqQ_Pp2BBOFSQWzvpp4rLlJsabcvQs3_bQo_A_aLx6X_U45WGVFZDTwcFNrBwhpA4iGT2BdhJAh-iQ2BGJ6IxUaMqio7ChIUQtGR0YYwqaE9sY9igpaA-dftMiNq6CG9TqWVRE6sum6svTD3WNwOD7GtcYONhCQv47DbtURV5XCs9ibsHBEXplLpIYIB_XSL2Qq7kvYQZG4ZjUBJA7rtZTDAIws6dXjVBb_dikDNgX3F42bfMO2zwpF63RL6EYHQsTWf2Z9pjX-phli4qduGdfYbwjop880v4cXITv96fa8PlBinBnj4jlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4258e2b29.mp4?token=ZpDi6BcNhv6m4JN8YfUOOQu8Q4Wh6GcxqQ_Pp2BBOFSQWzvpp4rLlJsabcvQs3_bQo_A_aLx6X_U45WGVFZDTwcFNrBwhpA4iGT2BdhJAh-iQ2BGJ6IxUaMqio7ChIUQtGR0YYwqaE9sY9igpaA-dftMiNq6CG9TqWVRE6sum6svTD3WNwOD7GtcYONhCQv47DbtURV5XCs9ibsHBEXplLpIYIB_XSL2Qq7kvYQZG4ZjUBJA7rtZTDAIws6dXjVBb_dikDNgX3F42bfMO2zwpF63RL6EYHQsTWf2Z9pjX-phli4qduGdfYbwjop880v4cXITv96fa8PlBinBnj4jlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
ویدیوی وایرال شده از تجمعات شبانه:
«تو تاریکی می‌شینیم، ذلت نمی‌پذیریم
بنزین رو کم میگیریم، ذلت نمی‌پذیریم
دلاری گوشت میگیریم، ذلت نمی‌پذیریم
مهریه کم میگیریم، ذلت نمی پذیریم»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106212" target="_blank">📅 13:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106211">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62e4095a95.mp4?token=UEpOxMc-W9__mcy5xi0EHVoJjhBzxVlyC0GAM0gGRq2TY2pr7fKfHcuxwI3ClcxFxltkG-IBVuXjFL36c0VLS56t_iaRI4NRS2dP_CMVJ28qADi9Fx34BXqcxItKDmRl4NJFmp63vK55XezTVoa_mREHvieDvmv_yX_0jkd5Tg2JlonGji2pguMMUH6saIgloqUBVxsWj3zyDJskBTCI03h5JlYMCmNC48Qk0hu4Or7PWhRUzWyrdL6psU8chEeqPtGWwTgw3qu6dNqGK7AxlUFONt77q31B0YpsHG_xScZLF6coSzSuuk1QbnTXTmB-rEW6WDnLeKK4N1UnZDDr7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62e4095a95.mp4?token=UEpOxMc-W9__mcy5xi0EHVoJjhBzxVlyC0GAM0gGRq2TY2pr7fKfHcuxwI3ClcxFxltkG-IBVuXjFL36c0VLS56t_iaRI4NRS2dP_CMVJ28qADi9Fx34BXqcxItKDmRl4NJFmp63vK55XezTVoa_mREHvieDvmv_yX_0jkd5Tg2JlonGji2pguMMUH6saIgloqUBVxsWj3zyDJskBTCI03h5JlYMCmNC48Qk0hu4Or7PWhRUzWyrdL6psU8chEeqPtGWwTgw3qu6dNqGK7AxlUFONt77q31B0YpsHG_xScZLF6coSzSuuk1QbnTXTmB-rEW6WDnLeKK4N1UnZDDr7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🙂
🇮🇷
نحوه برخورد شجاع خلیل‌زاده با مدافعان تراکتور: حمال‌های بی‌خاصیت
❗️
❗️
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106211" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106210">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106210" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106210" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106209">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vss3qEKxMZ10tHJFlc3a4q0PSEMrZd8iUL2G5tajARj5hpq-0C11xG_8yzd6GawvnSpSjgWJ6bi5WqGoHL-1Qy9R0pHwjNnZjOLldGDbFqfLpu881Z6R9_PgR3ROIDtTuMu_59ah1Jx22wcKYssmMigVPvCZ4fFNHxQbadpFvMI7ClHX4itRLrymfcr2bIeV9v9LroNQ79puCM6QAhc3O9lzrwoV6-JIb3u52FlfOA-n2QHxt9034a_foKQJ0e3uySiUaa-BXziMdzcHzJMxHcgN66sHjbLaLRtRcTd6ov9DZ0xObpQWh0G0nvEX6p58vRyJpJ9pDtlo7G_fCFn-Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
والنسیا
🆚
سویا
فیورنتینا
🆚
ونزیا
شالکه
🆚
انیون برلین
مارسی
🆚
رن
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106209" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106207">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👀
🎙
🇹🇷
اسماعیل کارتال: بمولا از ۵ تا بازی اخیر تنها یکی باختم اونم جلو بشیکتاش بوده. تو پلی‌آف اروپا هم لیون رو بردم و به مرحله گروهی رسیدیم. نمیدونم مردم دیگه از یه سرمربی چی میخوان. دهنم سرویس شده و قصد استعفا دارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106207" target="_blank">📅 12:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106206">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46400b9012.mp4?token=TwA5iCpMvTb6tYCp7F_0C-FeU0HzN_L1x7ri-18Dgf-eImdy6iTOyaS3lMXanZj3wDf8iTbrCuFBUCY-QziNKWnpVFA8CI1GZMHjDBgeYkB2WTgSI55We53IxTE6DFBCfy5i7pqk1PT6XH3kkHy5l_h6d4EJkTcuA066tuRde7_API8-IgQoOTFLFJAjbydd2OAT8u6rV0Gov1KiGmSEbKjr6z-zkaV9zjAmyoHg0SvKf-SforA02BtPwlKn8XGDkpbyGH1teFOjvs3CWaVji4ybaACzb-UfU5M6tLTrZvx8v5IWWUX4SJZyi4CnCf3Fqir6pMKTv0ITXoGdUIUq3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46400b9012.mp4?token=TwA5iCpMvTb6tYCp7F_0C-FeU0HzN_L1x7ri-18Dgf-eImdy6iTOyaS3lMXanZj3wDf8iTbrCuFBUCY-QziNKWnpVFA8CI1GZMHjDBgeYkB2WTgSI55We53IxTE6DFBCfy5i7pqk1PT6XH3kkHy5l_h6d4EJkTcuA066tuRde7_API8-IgQoOTFLFJAjbydd2OAT8u6rV0Gov1KiGmSEbKjr6z-zkaV9zjAmyoHg0SvKf-SforA02BtPwlKn8XGDkpbyGH1teFOjvs3CWaVji4ybaACzb-UfU5M6tLTrZvx8v5IWWUX4SJZyi4CnCf3Fqir6pMKTv0ITXoGdUIUq3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
محسن افشانی: اون شورت و کرستی که استوری کردم برای خریدن آبروی یک بازیکن فوتبال بود!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106206" target="_blank">📅 12:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106205">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abdf4b56cc.mp4?token=IIhWBVmeaxKyO8J1MejPwNsxiZCVjZEUc-D07Q_40h4WbhuJi5sFeP1JP3T1DgFd4l0RbospVdYOUVYtrjMEDKo0W0oiWSoIqg3BEDwlv57U04mnKjYZMY3pEfYGS51TrmRMwUsIaF5bsg2a9F1wFcLleqXl9G7r13PhaaeUhqFEFWY0vm3URPL619Z1WvEyMc5q1Cv5dNnFWw64_pvc454qhZThICpyGUzfkkTZ8ENHFlfD9rprPr9pB8axujDPOjbc4T8gypiMplLhlMUVLuMRdvBxOkuJMWXuCYv9M9BD4eu0VGZn_PRrSFQNerQG1kna9wpw4xOxZ2AEj8ayrlkJRW3gPEMjJVfJTrrcGP2UI1mO57sVwIMi0XTrVVSrpEkb4VqPhpRZahDwXodx9-u7DuN_9GVCcpndqBZGNA5V8bZYrVNW1LCl9ycUW5mJ-4PJcWlKaztZJDIYv0ekE8ZCRb_YLK9ak4jG0573VpaAmf4sCo7crGsTp2aRFQPhrwTpBOWYjTh9xqk7HvHRImqedquJsITPuTBOgqk_SxIjSjtxot3IFzi5Fh1UHUPWUBjUq2f0IXQRjj-hN5ST3UGbx1F5KXj9RI86K5MJTi9yb8faf0emw_jYtmFWMkbDaNvAVBq5EBm1q_CZgjwBA_dX8kCiX3WcwYbjtEuT3nI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abdf4b56cc.mp4?token=IIhWBVmeaxKyO8J1MejPwNsxiZCVjZEUc-D07Q_40h4WbhuJi5sFeP1JP3T1DgFd4l0RbospVdYOUVYtrjMEDKo0W0oiWSoIqg3BEDwlv57U04mnKjYZMY3pEfYGS51TrmRMwUsIaF5bsg2a9F1wFcLleqXl9G7r13PhaaeUhqFEFWY0vm3URPL619Z1WvEyMc5q1Cv5dNnFWw64_pvc454qhZThICpyGUzfkkTZ8ENHFlfD9rprPr9pB8axujDPOjbc4T8gypiMplLhlMUVLuMRdvBxOkuJMWXuCYv9M9BD4eu0VGZn_PRrSFQNerQG1kna9wpw4xOxZ2AEj8ayrlkJRW3gPEMjJVfJTrrcGP2UI1mO57sVwIMi0XTrVVSrpEkb4VqPhpRZahDwXodx9-u7DuN_9GVCcpndqBZGNA5V8bZYrVNW1LCl9ycUW5mJ-4PJcWlKaztZJDIYv0ekE8ZCRb_YLK9ak4jG0573VpaAmf4sCo7crGsTp2aRFQPhrwTpBOWYjTh9xqk7HvHRImqedquJsITPuTBOgqk_SxIjSjtxot3IFzi5Fh1UHUPWUBjUq2f0IXQRjj-hN5ST3UGbx1F5KXj9RI86K5MJTi9yb8faf0emw_jYtmFWMkbDaNvAVBq5EBm1q_CZgjwBA_dX8kCiX3WcwYbjtEuT3nI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
روش‌های نوین تیم‌ساکت‌الهامی برای وقت‌کشی! الحق که رو دستش کارکشته‌باز نیومده
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106205" target="_blank">📅 11:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106204">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249d50f161.mp4?token=VFW4Yuxkc9jr0RSW_uum_bpQHalbYOjeyOmVabPfqtrQ1OS1BVYXra_1ML8_OpfQ3VH1eslytV2gCuKkiNx7hLBPYRKefWsqOntJUyADGa5aXE74w_N94Ig2okI8Vh2qzisEqNvDok1vY9FaogtUOzQHDHNTpyLhSNBN6LHL5-9J-ZES_wafvlEdVnSNIIX28-32dCQ7NAWL9YsX4RU9YPz4kVghUTzb-eyDjULlXyCc2XwYDk1J6YuFBWTu0UMx73Lh-KyYfrIeN2GFSNWEu2m6YmOC4jzUq7V_6XBCASrm5WYMzqUj9eEz0syGAfFHHV66XYgx_Ejp7w34igJiww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249d50f161.mp4?token=VFW4Yuxkc9jr0RSW_uum_bpQHalbYOjeyOmVabPfqtrQ1OS1BVYXra_1ML8_OpfQ3VH1eslytV2gCuKkiNx7hLBPYRKefWsqOntJUyADGa5aXE74w_N94Ig2okI8Vh2qzisEqNvDok1vY9FaogtUOzQHDHNTpyLhSNBN6LHL5-9J-ZES_wafvlEdVnSNIIX28-32dCQ7NAWL9YsX4RU9YPz4kVghUTzb-eyDjULlXyCc2XwYDk1J6YuFBWTu0UMx73Lh-KyYfrIeN2GFSNWEu2m6YmOC4jzUq7V_6XBCASrm5WYMzqUj9eEz0syGAfFHHV66XYgx_Ejp7w34igJiww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇪🇺
پس از ۱۰ سال ایران در UCL نماینده نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106204" target="_blank">📅 11:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106203">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7627bb5d.mp4?token=UT7qyqnnJLfcpIxl2oG4lOtHy52_05Fr12CjJi66_QmTZQw6pSZE6SBna7ndReAvDVNUUA7wxS3wLrmoLyj2L5AcA2Cfyo8vdavwtJA3H5X54jj2ldUq0_pGjlkBhqshuL9UGtaHkes7-EhmEbs8Sm9oLCnzHkXobBwaDdTaDQ6DG71h4kYkCQOVc7cErn5HA2soMHdut8z918JkzL0pqbiJo92vPJJKNfLMuMm08ZUu5rvaeuWRqWn81rpcYBg-97qxq1h099y4pgEUlE7by5aSJHMEL7hv09rS_hgZGaGcB44rI9yH5XMWQbcjfCII4i-ovWTgIWot4JOnY69qSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7627bb5d.mp4?token=UT7qyqnnJLfcpIxl2oG4lOtHy52_05Fr12CjJi66_QmTZQw6pSZE6SBna7ndReAvDVNUUA7wxS3wLrmoLyj2L5AcA2Cfyo8vdavwtJA3H5X54jj2ldUq0_pGjlkBhqshuL9UGtaHkes7-EhmEbs8Sm9oLCnzHkXobBwaDdTaDQ6DG71h4kYkCQOVc7cErn5HA2soMHdut8z918JkzL0pqbiJo92vPJJKNfLMuMm08ZUu5rvaeuWRqWn81rpcYBg-97qxq1h099y4pgEUlE7by5aSJHMEL7hv09rS_hgZGaGcB44rI9yH5XMWQbcjfCII4i-ovWTgIWot4JOnY69qSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
⚠️
ادموند اختر :لويى ويتون هزار دلارى رامين رو با دو تومن تو منيريه مى تونى بخرى
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106203" target="_blank">📅 11:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106202">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/629b78a14c.mp4?token=ScI6sr2-dIE-QE_sCRahq2yWPzK6RKemT-u3Nzle9NpG6UF6ObNRHokkhgw9FQmSg7L0gLn-YoD7aOIUMrqLZM11imzk78SDkle9RUrKFGegByFtDdzScitPYyNBhr_CzjGOAMKzef8QPHH8N6veZlP9sMQYscyEXxFbWV0b3prIYh3LnJ639uda7dHmSjAnqHoUDn2Y7anEUh58b7-6CSHrjFeMkKQ873_x-HDHTR6Ut461ihwZ8eynnqMyhAdQvf06puRK4dBa18h0rWeS9NMKJ5_Wjy6_H9_ZHo1AXstbha9IraY9WdgimogXw2o7yukr6-QYPpHBDlY7xqZQIU7r2WqbzVsKFX9Qj3VyhbTHfZGxBydW1y3C7dD6BUT5woNBwn4r1hVrQqYGsjQnCq9S9G9FkCkK2DujENjJ_EU1ugRpPg_X0XMBdV9qiSTfbJseEQeJU4ociU7smmpvHyZ7K-w0mENNoOOeRW2ocjXsAQ8jzIcvLAu2SVJ3PNxIcd56F4pFT9S8XLFDidRjfrASl29WUNVuTZxJ3mq0NJaTD4ShWaUNWoa76hW18gFhNdVserYaEcDcIZpTZX5g0JRwK0kEZLfUs7w5g1pMkrVYCDXymRH-MEGUma8mYy_bdK_v5o487iGXvDVsU1wi5IADgQXDhfs_Kwg_PX__c7E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/629b78a14c.mp4?token=ScI6sr2-dIE-QE_sCRahq2yWPzK6RKemT-u3Nzle9NpG6UF6ObNRHokkhgw9FQmSg7L0gLn-YoD7aOIUMrqLZM11imzk78SDkle9RUrKFGegByFtDdzScitPYyNBhr_CzjGOAMKzef8QPHH8N6veZlP9sMQYscyEXxFbWV0b3prIYh3LnJ639uda7dHmSjAnqHoUDn2Y7anEUh58b7-6CSHrjFeMkKQ873_x-HDHTR6Ut461ihwZ8eynnqMyhAdQvf06puRK4dBa18h0rWeS9NMKJ5_Wjy6_H9_ZHo1AXstbha9IraY9WdgimogXw2o7yukr6-QYPpHBDlY7xqZQIU7r2WqbzVsKFX9Qj3VyhbTHfZGxBydW1y3C7dD6BUT5woNBwn4r1hVrQqYGsjQnCq9S9G9FkCkK2DujENjJ_EU1ugRpPg_X0XMBdV9qiSTfbJseEQeJU4ociU7smmpvHyZ7K-w0mENNoOOeRW2ocjXsAQ8jzIcvLAu2SVJ3PNxIcd56F4pFT9S8XLFDidRjfrASl29WUNVuTZxJ3mq0NJaTD4ShWaUNWoa76hW18gFhNdVserYaEcDcIZpTZX5g0JRwK0kEZLfUs7w5g1pMkrVYCDXymRH-MEGUma8mYy_bdK_v5o487iGXvDVsU1wi5IADgQXDhfs_Kwg_PX__c7E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
💥
یک‌دقیقه خاطره‌بازی با اسطوره آرین‌روبن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106202" target="_blank">📅 10:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106201">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c278d8437.mp4?token=bEDUYVC6rsG3XnAY1pSeWAhSBvtfxJ8N30FoyYQKjEAM3AOLsqU6-L7DlEpf-FS8mFD4jqjDygvagTNjUovqvKLYNB2FAvqvtA7jEcs3xp8sA77C_nbz9ZD507v2lfUxYA19ycwpCCoTVz8b6bi-PIyS4QmaI_UDpbASt3a0PCtcQAS7mpBU2OFr4RG_QcaeycQd-AhDqriyZxAHdDsQZI2clA_lRYHpD_6u_wCDAGOMKhlwbb9M7XP4oK0EejYFyx3Ptb10xcbVQGfOSyLlSWnT5QMY5Xa8LHSaWZ14Dhf_6C6nOkQQbG35oQJ4V2PxzTB9qrb_OEzm2Tn3sEy65w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c278d8437.mp4?token=bEDUYVC6rsG3XnAY1pSeWAhSBvtfxJ8N30FoyYQKjEAM3AOLsqU6-L7DlEpf-FS8mFD4jqjDygvagTNjUovqvKLYNB2FAvqvtA7jEcs3xp8sA77C_nbz9ZD507v2lfUxYA19ycwpCCoTVz8b6bi-PIyS4QmaI_UDpbASt3a0PCtcQAS7mpBU2OFr4RG_QcaeycQd-AhDqriyZxAHdDsQZI2clA_lRYHpD_6u_wCDAGOMKhlwbb9M7XP4oK0EejYFyx3Ptb10xcbVQGfOSyLlSWnT5QMY5Xa8LHSaWZ14Dhf_6C6nOkQQbG35oQJ4V2PxzTB9qrb_OEzm2Tn3sEy65w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💥
نیروی دفاعی اسرائیل (IDF) دیشب با انتشار این ویدیو از انهدام کامل تونل‌های متعلق به سپاه و حزب‌الله در منطقه استراتژیک علی‌الطاهر در جنوب لبنان خبر داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106201" target="_blank">📅 10:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106200">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsM2A3b3_Kl1LRXdp06bUqxhWB5W-Ab5Y6llQoVwLkXMjjyytEXgE73SsFBYgPLqYQ2yAgKziFM52Qs57tSANXAULx_vgBFpjKYRd6Ich1mW3GZ8w6kHGGtOQwdxSQy9R1jlJ3_hu9cvNbO09GGe7p-snYACeBn5bO42iVQv1gChFNQqynURVX5WlwzWH0ixweck_ohYaNbmkoY-DHveaTu_5C2jbJO0XDHJehXwXWVPgFUj567qaWTdn8VFJWZyPVm0SWvzyTK9XZspX81GhVWlgJSh42HXjjkiNyjgzN9ZCFkI9QQklMisgOV1_Oab0u6lCJODJsOrMQSIIk5paQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نامزدهای بهترین بازیکن هفته اول UCL
🔸
فران تورس
🔸
رافینیا
🔸
ارمدین دمیروویچ
🔸
مارک بارترا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106200" target="_blank">📅 10:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106199">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c20f0a6e3.mp4?token=c4giJN8Ikme2l-jTDOuqGer1pJXnDxmf4cd4ctcRvCyXZ6HlBVmrzIW7lZpfZbzDcwWxqrqYkdyvDp0e5Er5CP4J_MdyTsgQgfMhA9RT_Q7pwquDzbTN_2LGdd1C9MGjrtZXe5OW9ln1qPypaNYe08tEWaR0r8DMPMX_1WvrGRqpc4moK6gNtja1NBQP5zpVR5-RQMU_D_3bdBv2YvtrsiUuyDZ-qFCftu_jhnlmglBZCPJEFTc8hcJmBGNZSwqZ96Af58HtwBqnoFvtPaQFrpdyJ6_nKypC3M73fUaQwNPQpPTm8ZNHmAphu3LYpyhsS2Zl6Lb7ZzzO8drGs779uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c20f0a6e3.mp4?token=c4giJN8Ikme2l-jTDOuqGer1pJXnDxmf4cd4ctcRvCyXZ6HlBVmrzIW7lZpfZbzDcwWxqrqYkdyvDp0e5Er5CP4J_MdyTsgQgfMhA9RT_Q7pwquDzbTN_2LGdd1C9MGjrtZXe5OW9ln1qPypaNYe08tEWaR0r8DMPMX_1WvrGRqpc4moK6gNtja1NBQP5zpVR5-RQMU_D_3bdBv2YvtrsiUuyDZ-qFCftu_jhnlmglBZCPJEFTc8hcJmBGNZSwqZ96Af58HtwBqnoFvtPaQFrpdyJ6_nKypC3M73fUaQwNPQpPTm8ZNHmAphu3LYpyhsS2Zl6Lb7ZzzO8drGs779uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
ویدیو وایرال شده و دلهره آور از جنگ اوکراین ؛ سربازی که شانس میاره و از زیر تانک سالم بیرون میاد ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106199" target="_blank">📅 09:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106198">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc5454d366.mp4?token=OUUmelOj-8GlY8PLkItun6Hw2pDVQFlsI1ex06H65TbvsB1WLcNFiU35PG1yXvMfaxl8gY1pEfKz8kK2Z--pWGhd0lBBLE7f0hFSAMHibrViF0lfItpDtFlaAg1Z1chWQ65J2f9DAYSOOFIAq7AbIthb8rtGLZE-cDGza8TGgT-H9-Gt35G5vKyMlv7OAj0iuNgr6LWmpWQjIGDsvqq7lgVtVn7eWesU0_mKTYJ0_xn7V8x8aEf4ANQbGawvrkuZxfB0jE7c6shcqXbo207vwuULIIE_1RTLl7B_L8Hi8CdZ4SOgYajIfApkV_jc1w8wlLCMdHlYJDoAnTAlJeLIAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc5454d366.mp4?token=OUUmelOj-8GlY8PLkItun6Hw2pDVQFlsI1ex06H65TbvsB1WLcNFiU35PG1yXvMfaxl8gY1pEfKz8kK2Z--pWGhd0lBBLE7f0hFSAMHibrViF0lfItpDtFlaAg1Z1chWQ65J2f9DAYSOOFIAq7AbIthb8rtGLZE-cDGza8TGgT-H9-Gt35G5vKyMlv7OAj0iuNgr6LWmpWQjIGDsvqq7lgVtVn7eWesU0_mKTYJ0_xn7V8x8aEf4ANQbGawvrkuZxfB0jE7c6shcqXbo207vwuULIIE_1RTLl7B_L8Hi8CdZ4SOgYajIfApkV_jc1w8wlLCMdHlYJDoAnTAlJeLIAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🎙
🇪🇸
تعریف و‌ تمجید جالب تیری‌آنری از رودری خرید جدید بارسلونا و تشبیه‌ش به سرخیو بوسکتس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106198" target="_blank">📅 09:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106197">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf8721a346.mp4?token=Lt58hE4X7llrMQcc5KMuV1l7edomcgAZFEr_K8RIisvv__SIJszSoRgUQ7YtUpHhbpnwg1An_2wRlLxWRDdQI9CXPChQPuGLsC2bwiN9c5sSk3Qyput4PKQGo2KLLoAw9nWVBqWsWHvgIX9gjAdhNdvOPYnCEZ4pTT5oHddBmLM7JkypcZZq7DXkYcL_xaqwtYEDUD_JjK6imgaxj6wDpkFM1m86WokH2yM1ReZj9i_A1y8MJn4vx5wev1tZtzhdI3lBTf70ynha-V3XCrSll9YGO7KnW9HUkaa5tUDGufcfpdacudJAv_e8ZphqgCAZg7kJh_qZnlyDc6I-X7isfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf8721a346.mp4?token=Lt58hE4X7llrMQcc5KMuV1l7edomcgAZFEr_K8RIisvv__SIJszSoRgUQ7YtUpHhbpnwg1An_2wRlLxWRDdQI9CXPChQPuGLsC2bwiN9c5sSk3Qyput4PKQGo2KLLoAw9nWVBqWsWHvgIX9gjAdhNdvOPYnCEZ4pTT5oHddBmLM7JkypcZZq7DXkYcL_xaqwtYEDUD_JjK6imgaxj6wDpkFM1m86WokH2yM1ReZj9i_A1y8MJn4vx5wev1tZtzhdI3lBTf70ynha-V3XCrSll9YGO7KnW9HUkaa5tUDGufcfpdacudJAv_e8ZphqgCAZg7kJh_qZnlyDc6I-X7isfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
اینبار کنایه تاجرنیا به پیمان حدادی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106197" target="_blank">📅 09:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106196">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8kU9m3BGgO1-tFQJ5KxB_A1MQ5-ZQ8HXiE6c3pRiUKldFe6mlZbYyTWdyjOyA9i2CNX7AdOUB5aBi4WDZq0u3e9qLQKvSk_5gkHBJNayj35HMFhweMYpKqusb7hPo7He23PgJpuz3LRuJDVKKU_WciX7zZlOROeJg7yW9dpXMYBZBV6qU4H1wg_a3viKDl97KKno9mWZpBtvNRqcRJXKwIYwRG3iGCZgi1ph561wSGBPc86jeJmtHu37twAIf6ACgN03YhvVeaGKUpLV14TmUgd4k7c8kXqPA4cr1kVoets6D_OFhDkzn5rBEdqFcSNLTWeAahPBDngT4Od1foisA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔻
🇪🇺
کمترین تعداد بازی برای به ثمر رساندن 55 گل در لیگ قهرمانان اروپا:
◎
🥇
🥶
ارلینگ هالند — 49 بازی
⚽️
◎
🥈
رود فن نیستلروی — 70 بازی
⚽️
◉
🥉
هری کین — 71 بازی
⚽️
🆕
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106196" target="_blank">📅 08:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106192">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fcya1R4DbStm6DXtHQSSAhRvjXMrloKIhrPx1OmofoFds9dM0f0aXfpDN3XvHiDhzEI0gCjI6Ui9319hxJkE_Cb4I2y5Ay5Aw56HN7BZU5c8V97q56u5z8Ig4TCuj1-k7VczIDjbxDLcMIAADXh_T3p3pDCtwouDFqiVxnfNQGzIo2Q_wnkOPOXk1xnNXCWCG3sFoOR3hHGuE0VBQfP7rVkzVyYGOc2eqBhdngbQS0EC1cvyvwYpovosajV5cJo2zbJ2zgG6qIw-a2x0Lsunu0BevyESYutDsdX8ift2PZK7bH-8mK0sjq9INhprvoxRI-u9yafrzvkGELzPFaKORg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🥶
مقایسه آمار السد قطر و بارسلونا در لیگ:
🇪🇸
بارسلونا ۴ برد و ۱۷ گل‌زده و ۱۲ امتیاز
🇶🇦
السد ۴ برد و ۱۹ گل‌زده و ۱۲ امتیاز
❌
پ‌ن: دوشنبه هفته‌آینده ساعت ۲۱:۴۵ قراره استقلال ایران از السد قطر میزبانی کنه. ایشالا خیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106192" target="_blank">📅 01:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106191">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHd3W8nv_Iwq2cjftAr7RmBokgdA0wcz9a6NuhdRssUx4SJJczIVXrNh1PG34tqvudzfAhkV6Af4_AI1ji2AVcbsaxEvAqTYvFUBYuH-MVRzO1vQtUC1g4JkTz2kqXQq1lSG1QMchWH67NkzMh2_fuiLmmvZT8Z5Aiw31VFZSu9_AAci7UwZPqKW5bJvVUc-iVqQLkBiq-ZgvdseYk6wC0IC_76tNMeSGnpvwhH_KCJNgrYPrEe80QhxSJi0suxCTH0FZb_vfLsRmoR0S6-kWFpBVMCDrVtzjitlNFiSMLwLutHhYjalgNL3koEd8grTWKYWg6-ro3Z0GWbyf12L1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🔥
🔥
🔥
سوپرگل چهارم بایرن‌مونیخ توسط اولیسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106191" target="_blank">📅 00:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106190">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYnNCxDVoNgU28yp9-jEJ2Dp6IYqgdr0NhSTo40D2yHhVSjRh4BtqS25QwNRGQjJWbkh-4e87gC9GtRkTjYOi1fgHGJUkukC_Iwy0J_BwBSkzd-fB35AVSfXFqHqyo8o4tH5xPN0_Jsy1s8m9bTel-HjIVClVTvSwk79VL4IVnlSYSJfgB0yFOl6smNLiNAZmExa6iHHDCM6CZLTPcE6Ab7gtBQqlJgZWkTJZvqgT84hQnyDNe4Yhz62-H7ZQTzLDIZ1MP9Q9WnI6GBkAAacGt15VfbJoqwURqNs3hyJ4G7S_YophG3JwOT3_1ADPSAXo84H-gl7tw0J5vmb5-Obfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
نتایج بازی‌های امشب لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106190" target="_blank">📅 00:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106189">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇿
هایلایت بازی منچستر یونایتد 4-0 صباح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106189" target="_blank">📅 00:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106188">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSomEmoVWc5Rz7vy7YtVVVsGOARJTTE_Ri3HQC8yUbiH1qGVpj-_XnPmeRNZG3xyDCivsH4N_OG2Xzm9DRqI09ecduXlE1cKkVVE-7kqdKOH5KdjzWu-W6L2C_bopVYtwJmCFrkq79abQD9vAQ4G0Kuf86VtBSX5YZMc2ZLxVINPUqVk8HFi-Ye4I1BF_KjcBN6IXa7scWbWNwogulDmym_nyiW7FELR1Ufc10sW4nWSmLpCzaP68jdETiUc4nf0Wtcpm4n0mMzgE8r0bhuaXLk__nJ4tDert3mWNfm3e8hYr3c5SKuhOcFynkltRlLpbPo6iQ3EMfN2hEQ5PEb9Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
نتایج بازی‌های امشب لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106188" target="_blank">📅 00:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106187">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3993269f13.mp4?token=WzfDxKSUyBJcVfUjGTG96H4BTY0BqnR_NF0pYCitKy4jbIJ2oP9IruYyNlXFXJ3EAa7Ark0pc3EcP5P1tP8UKeKm6eSF1SzJVnKnJj0UmL9Z7PeiAOuZ7Ma6wmT5P3TxHtV9-OAstWtQvxrd8paLe6SNSJXOLU5E80WZ6AJIukg4DR20p8cguLtU8xAEEse7-07yTZ-1KmaNG0s-FR0LRwwx2mlZoYBUbZlWzKoXrjSLXpRh3NPvtKmQGkavo11PjzGjDgxT60I0zsRxUSFZXxWtT9geBnlcmT_t9hF5XiRP3GEft8TvUvw_gajSaatzHX0Ou0s-SGwsxMHDyFfcx7Ehvs1Dz_mrH5Pio3k6im4Gboceo4Cbkqi2GBd4a4pmSjxX4lcLyntP_lp9P8A-6j3EMvsUDIWmrlMHr3euY8JW7bJwa1CNnTBrV6v7JMYIcrh98v1QXUH1umczch-3ruPErLWcCu5-S6DonC7xgkSt3uplGXr1zluVytLYfj4ih-3mHigtG8smeCMy-BG89axw4B4HCpAhSbJ_D789nLZXVW2yaCTvOH83wPIrrCDN2Rg6cmlfesvluN8KZYT4-B1TjX1uzZ8aB3-C16MHd5cpdZ8U2_rmy5m-QyDhH6AOc8eByF5SODQRshLpx_tfOxWUTc1YxL6Mp0v7udofyO8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3993269f13.mp4?token=WzfDxKSUyBJcVfUjGTG96H4BTY0BqnR_NF0pYCitKy4jbIJ2oP9IruYyNlXFXJ3EAa7Ark0pc3EcP5P1tP8UKeKm6eSF1SzJVnKnJj0UmL9Z7PeiAOuZ7Ma6wmT5P3TxHtV9-OAstWtQvxrd8paLe6SNSJXOLU5E80WZ6AJIukg4DR20p8cguLtU8xAEEse7-07yTZ-1KmaNG0s-FR0LRwwx2mlZoYBUbZlWzKoXrjSLXpRh3NPvtKmQGkavo11PjzGjDgxT60I0zsRxUSFZXxWtT9geBnlcmT_t9hF5XiRP3GEft8TvUvw_gajSaatzHX0Ou0s-SGwsxMHDyFfcx7Ehvs1Dz_mrH5Pio3k6im4Gboceo4Cbkqi2GBd4a4pmSjxX4lcLyntP_lp9P8A-6j3EMvsUDIWmrlMHr3euY8JW7bJwa1CNnTBrV6v7JMYIcrh98v1QXUH1umczch-3ruPErLWcCu5-S6DonC7xgkSt3uplGXr1zluVytLYfj4ih-3mHigtG8smeCMy-BG89axw4B4HCpAhSbJ_D789nLZXVW2yaCTvOH83wPIrrCDN2Rg6cmlfesvluN8KZYT4-B1TjX1uzZ8aB3-C16MHd5cpdZ8U2_rmy5m-QyDhH6AOc8eByF5SODQRshLpx_tfOxWUTc1YxL6Mp0v7udofyO8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🔥
🔥
🔥
سوپرگل چهارم بایرن‌مونیخ توسط اولیسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106187" target="_blank">📅 00:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106186">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a3837ef974.mp4?token=GXv504CUYzWpqGXkAIfeDZOSDVvurjZGKGU3sdpSgw1gyui7dp3ojoZ5QBESSjsU0blXLssEGNbmE-9hVGBvfVDTu5XyxDWefVwlwFmT85QS2TFgAkuS5_3BxCXoOpS0z9z7UUfLIuwQvXrwnPHPl8fHJz4tz2Eh_vQ_tJxORbbq5OLarTfuIe2rifqF-xQZvm_8mOUq9p_xpBKonHSqZHfIAHiZcLbAHETxlq4DbSsvNE7_R4ioxf4_U_qZkmBBHthj2xeBex9axMYqj6sKPFUNVp1HzE1EGjHcj8Pl7DTiMyzNlGV0-pFeEroJaHFiA2R_AuCk3RgkCQv072rb6qH2TIQmM01HS98dQ_t0QrXOUHbvOZo0PM-AOU0MzAF4WBeeiRJe0ir7Ix_QW3bHI0KujvoE2PTTeGgPPWvr_Pz54wR60mrIOtNEiDyJWe8IAcrFO29PL-MXGIFAxly40Hkv339zXu3Yzv1R_vXWXS6Cks6x6Vd274Q0Nv4fQE0lwoZMGh69uhndrnx--vseUuBou5rUfXzxCqpO7-0YRPv_8tgiO-0aPyoGCFzqvmhC-0VIvH2SIycJ-gdgZ3GD3x4svqvEpXyVANaS9SSz_VoW5dvUdHGw57VNAHyEDZQAiHG5AgAlnmrysMRnJ5mevsIb2CFiGseInzcS-2dx0v4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a3837ef974.mp4?token=GXv504CUYzWpqGXkAIfeDZOSDVvurjZGKGU3sdpSgw1gyui7dp3ojoZ5QBESSjsU0blXLssEGNbmE-9hVGBvfVDTu5XyxDWefVwlwFmT85QS2TFgAkuS5_3BxCXoOpS0z9z7UUfLIuwQvXrwnPHPl8fHJz4tz2Eh_vQ_tJxORbbq5OLarTfuIe2rifqF-xQZvm_8mOUq9p_xpBKonHSqZHfIAHiZcLbAHETxlq4DbSsvNE7_R4ioxf4_U_qZkmBBHthj2xeBex9axMYqj6sKPFUNVp1HzE1EGjHcj8Pl7DTiMyzNlGV0-pFeEroJaHFiA2R_AuCk3RgkCQv072rb6qH2TIQmM01HS98dQ_t0QrXOUHbvOZo0PM-AOU0MzAF4WBeeiRJe0ir7Ix_QW3bHI0KujvoE2PTTeGgPPWvr_Pz54wR60mrIOtNEiDyJWe8IAcrFO29PL-MXGIFAxly40Hkv339zXu3Yzv1R_vXWXS6Cks6x6Vd274Q0Nv4fQE0lwoZMGh69uhndrnx--vseUuBou5rUfXzxCqpO7-0YRPv_8tgiO-0aPyoGCFzqvmhC-0VIvH2SIycJ-gdgZ3GD3x4svqvEpXyVANaS9SSz_VoW5dvUdHGw57VNAHyEDZQAiHG5AgAlnmrysMRnJ5mevsIb2CFiGseInzcS-2dx0v4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل‌سوم بایرن‌مونیخ توسط آلفونسو دیویس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106186" target="_blank">📅 00:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106185">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29ed472619.mp4?token=vg_G4cwXduijRwqdElIl_es9zN1ozp8iSiLOZlStQ9WB-BWzjGNJ_28j9BevJP7GMRbPS_uEb85ad9q9Oza73GAK09gB-FGy4SoeXJ5zqDC-j_IvDKG1DLKOP2O5PuPsZeL0Z_muW305jpT6epuGrq0aLy-0RhY7H0A-qscwr4drwXwR51rxKge3QU8jSuxJd-nxIpHV4FsCqamSp9oScgx6lu0SWV7wcEUkDOj4zNt8vLCVkrd5_5gR7WlfVLWytKggtfN-ncaNrs64PB9zkITWeuYgD9ZJzl5dIIJfKVWSyINMFOWz5lnCE_5yZTpf2LYqdJCKoW5oZEdkF-twEEBBWTm4V4RM_pHfs-v309CeeajKfwy9q6OW44q2tzXPZ4aBZc_MMqfJMXr0dA6XZSwb9Q_H9eBonbeszqL89ysHwAKc5jcp3axV5Wirtfei-rouviVI2JaAmkMmnATAmm9URobkPJI1g0hSeyAMw5u8hjWQGMVXD6UfTsEZdgOOYaqpzIF0e9bHMHfH-qZL9yghCW5Hgkz76YJ9wlNb7dtswxjejTZIiMkt-iD4fVYTn3zfENdpoZ-hQexZNDLqFH3PZu3_zASk5Ss6rF-S750l8l91kH9I1Epva0qTTK-TpH_MHVb6lhwTCIh7gwbazyrJxX7fDZOVMTNSza4gz-U" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29ed472619.mp4?token=vg_G4cwXduijRwqdElIl_es9zN1ozp8iSiLOZlStQ9WB-BWzjGNJ_28j9BevJP7GMRbPS_uEb85ad9q9Oza73GAK09gB-FGy4SoeXJ5zqDC-j_IvDKG1DLKOP2O5PuPsZeL0Z_muW305jpT6epuGrq0aLy-0RhY7H0A-qscwr4drwXwR51rxKge3QU8jSuxJd-nxIpHV4FsCqamSp9oScgx6lu0SWV7wcEUkDOj4zNt8vLCVkrd5_5gR7WlfVLWytKggtfN-ncaNrs64PB9zkITWeuYgD9ZJzl5dIIJfKVWSyINMFOWz5lnCE_5yZTpf2LYqdJCKoW5oZEdkF-twEEBBWTm4V4RM_pHfs-v309CeeajKfwy9q6OW44q2tzXPZ4aBZc_MMqfJMXr0dA6XZSwb9Q_H9eBonbeszqL89ysHwAKc5jcp3axV5Wirtfei-rouviVI2JaAmkMmnATAmm9URobkPJI1g0hSeyAMw5u8hjWQGMVXD6UfTsEZdgOOYaqpzIF0e9bHMHfH-qZL9yghCW5Hgkz76YJ9wlNb7dtswxjejTZIiMkt-iD4fVYTn3zfENdpoZ-hQexZNDLqFH3PZu3_zASk5Ss6rF-S750l8l91kH9I1Epva0qTTK-TpH_MHVb6lhwTCIh7gwbazyrJxX7fDZOVMTNSza4gz-U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇩🇪
گل دوم بایرن‌مونیخ توسط هری‌کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106185" target="_blank">📅 00:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106184">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/469ae1834b.mp4?token=elp1bR0xFMGAs3p6xyJOVGX4hdgI7-QcCTiKghYXjw8ypQ6nNheYBB7T_mqwm9KmKj2xdDEwfPpVKLXpfg34Z7kdg_t98sviH2kjSCUm9RWn--VsLp_1VytFPSSECR8nEBfjUHA_TYlvJi-u3rC5NihZ76ny0EgmTwcNNu2AFw2CLQLnuEmrXf8ah10f022SxskmivzULRP2X_MqtJfsZII6cy-63ZDY7lQH6i95MUkchx1N_BpSXwzSEWcqjkxVlzg0d-mOXbCYbZjfqm1YLs6B2Bwzq-dryDtLv5QLm474Cb4uV8ePC_u5bUDMHXvzfhNZyhyjTZxmLVi_Xgv8tl0GiyktpWRMfbAs5qzFUGnMx1PLMt4rZ9Qr7wDbEyP-8i1We6tplsun85Lpjpe_-QiBWHfx0DotTY_h-cljcllzYAYOtXsvWpMK07FfvrVI1kLUgDE-xwQtZrqNwlvskunWEbjerSYVxxZ6OdyXB5U4FBbkH_hPziwlpQwGL8lWcVfboVpf99SavLF_MhFm0JjPBQVoFAofeFCezABAcIFag3NlQyMG3hfD3zeZcx2bT1QRbVOGUOoISBp-xwYe3xzPqKGqQ0-0QRww0vwh8e7p-rXSUpVBSMt0KLR-ju14s_7CSxuGdHF-OJ5b-yqQV6ypqSJ1oeNEcBJu7fOwAEc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/469ae1834b.mp4?token=elp1bR0xFMGAs3p6xyJOVGX4hdgI7-QcCTiKghYXjw8ypQ6nNheYBB7T_mqwm9KmKj2xdDEwfPpVKLXpfg34Z7kdg_t98sviH2kjSCUm9RWn--VsLp_1VytFPSSECR8nEBfjUHA_TYlvJi-u3rC5NihZ76ny0EgmTwcNNu2AFw2CLQLnuEmrXf8ah10f022SxskmivzULRP2X_MqtJfsZII6cy-63ZDY7lQH6i95MUkchx1N_BpSXwzSEWcqjkxVlzg0d-mOXbCYbZjfqm1YLs6B2Bwzq-dryDtLv5QLm474Cb4uV8ePC_u5bUDMHXvzfhNZyhyjTZxmLVi_Xgv8tl0GiyktpWRMfbAs5qzFUGnMx1PLMt4rZ9Qr7wDbEyP-8i1We6tplsun85Lpjpe_-QiBWHfx0DotTY_h-cljcllzYAYOtXsvWpMK07FfvrVI1kLUgDE-xwQtZrqNwlvskunWEbjerSYVxxZ6OdyXB5U4FBbkH_hPziwlpQwGL8lWcVfboVpf99SavLF_MhFm0JjPBQVoFAofeFCezABAcIFag3NlQyMG3hfD3zeZcx2bT1QRbVOGUOoISBp-xwYe3xzPqKGqQ0-0QRww0vwh8e7p-rXSUpVBSMt0KLR-ju14s_7CSxuGdHF-OJ5b-yqQV6ypqSJ1oeNEcBJu7fOwAEc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌چهارم منچستریونایتد توسط لیساندرو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106184" target="_blank">📅 00:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106183">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a73af6ae7.mp4?token=BgrLCQE4BajnIVvWkomCCGOLCk6PaTpkkpOn9-Yxp0GFmSuSdaoZoQ5N9nDDMVr0zcRwFBddVE9fRvOInH-mMCd7V4dVW_R_wAFZvas_QmucUzZ7rESPKC7uQolx-8_Y4anQFbycOpVhHnmnPWcdbOT7kwZYMn9NfCupenfVBYi0oBgWVkhxuAtL7h0BcM6YdHsO4TAaILUwe-z2pXKib3SUjkHuOqEM2ao7GtZN6CkxX8bB2L4Iwgf83-SxCRSQF_O09nUxKhSapKbCzDtMOolg2u6rMurIhj_22J-SejmDxuF8GvZLPZsCgvDnzLtvrEYi1ZWTCktTixxA_tKLWhFVOtraclKeYr6a7amHzklyNvhe2BWWNMxp4OOlWOTaPADKbQBDvAJjxIdynHKg7M2QViudZkhGhE4kzoEBOgFroUzCkvFOyxdEUFy4L-BsTZGC3IppQn34VXY4ZUgSaNqrLQEpzjNEG0GZJzbhX-5sftGjFoxBbhSuEbPQaMq7--muJAL3v8EN7njAwQcJ2_u5x6b9E6TraiEafy7Mi4QgASMUHp7TjEl0qNJwkyxv4_I8oKsbIKBTDmszbknE3Depi8VT2Uc2-Sd1Dbm4vvUu0h5LgQz5vw-abRWi39NstHZcpMhA67-G4ZoKS_r-pNKHzz4oosr8QBC1264CepE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a73af6ae7.mp4?token=BgrLCQE4BajnIVvWkomCCGOLCk6PaTpkkpOn9-Yxp0GFmSuSdaoZoQ5N9nDDMVr0zcRwFBddVE9fRvOInH-mMCd7V4dVW_R_wAFZvas_QmucUzZ7rESPKC7uQolx-8_Y4anQFbycOpVhHnmnPWcdbOT7kwZYMn9NfCupenfVBYi0oBgWVkhxuAtL7h0BcM6YdHsO4TAaILUwe-z2pXKib3SUjkHuOqEM2ao7GtZN6CkxX8bB2L4Iwgf83-SxCRSQF_O09nUxKhSapKbCzDtMOolg2u6rMurIhj_22J-SejmDxuF8GvZLPZsCgvDnzLtvrEYi1ZWTCktTixxA_tKLWhFVOtraclKeYr6a7amHzklyNvhe2BWWNMxp4OOlWOTaPADKbQBDvAJjxIdynHKg7M2QViudZkhGhE4kzoEBOgFroUzCkvFOyxdEUFy4L-BsTZGC3IppQn34VXY4ZUgSaNqrLQEpzjNEG0GZJzbhX-5sftGjFoxBbhSuEbPQaMq7--muJAL3v8EN7njAwQcJ2_u5x6b9E6TraiEafy7Mi4QgASMUHp7TjEl0qNJwkyxv4_I8oKsbIKBTDmszbknE3Depi8VT2Uc2-Sd1Dbm4vvUu0h5LgQz5vw-abRWi39NstHZcpMhA67-G4ZoKS_r-pNKHzz4oosr8QBC1264CepE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل‌اول بایرن‌مونیخ به بودوگلیمت توسط موسیالا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106183" target="_blank">📅 23:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106182">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hugUcjo9jutQ-gS96QotdcjZqI3qeLb_Saozw69JPH1_JEC1_x1i3KA1znil4g5xCpXC-CQUeFcqUnDHn8sl3WG0TJnyfmdcAlBVqF244QkojYx8FfJKTiVtUD__Jp5bZbyjO7EzZubO58auC7Y051LlEsikQwhqpzoRGa7-aESW2JoE13glSXZDE5xl2OWoVbCKCy51GRdtzF8HA9myF2PtasQiN31E62Hdz2UJzPx0Nkzmd67ICGbHrYxxNJfDgg0i15C5IZLkUSuJsahAiWEjuFVSZlPJ-1EuElh97Wk5tKx77EznUuKRTyk13Rk00fyJb1gFXp1tCiq9lDImoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔥
🗞
رومانو: فیلیپه کوتینیو با قراردادی آزاد به سانتوس پیوست و هم‌بازی نیمار شد، هیر وی گو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106182" target="_blank">📅 23:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106181">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
‼️
🇹🇷
اسماعیل‌کارتال پس از تساوی جلو رم در لیگ‌قهرمانان اروپا از هدایت فنرباغچه استعفا داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106181" target="_blank">📅 23:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106180">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cj4gakZEMKp8vF1dy9rvsONkXdOZ3PjGBEbF5pyhE7qzum3iEOuin7BD5oVMOArTuz5l6N1VvYJTex5TVtXuNAmMjn0afZx5LDiSBeaiyr_sNm2QxaTsrtDoij0EZvXwCqTIvILfR4FG0r6WPRAWpwx-kA14-yh8wP20LQSbPeFuziVxg7ODVe8RnTT_mC-vTlfNIJ6lO-xvfdUK-XamL6K7fXaZfrav-gkf8xztNpsIclQONtNBUwCRIDWUrXmyR6vHl_0OLGqkp_yWrWgZ-5MHLhfVzCCa6BFNs6m0J7HmdTM1Qz9G1BvlKwkSLX63nORqP9aF-ntmMc00CjqCoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇹🇷
اسماعیل‌کارتال پس از تساوی جلو رم در لیگ‌قهرمانان اروپا از هدایت فنرباغچه استعفا داد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106180" target="_blank">📅 23:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106179">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f2197035aa.mp4?token=Zx3DX4d-GsI1jCA8gmvpCxPTPCL7f7IsTzk3U2bN-kgXnAjie4os6xiVudzQXAWvwMRomDb-_CJZIuWGChZ6-Tp6uLkL4iCph4ZPy10MJfHR8sIZB6p_oDpwNo7HrNjALkDrQGg3OmYWwINg9hYR0SC1ozteacsNwq1HK5P94X08wwez1Y72oI8xzlK-mb9JxFsBnVn8o8COzYsOc1WUL1F_Jh2izvgua0JbBDCOHb7oKYzLFyfAAVM_sD-1xxGicc4_W_1Gcbxr7JDvolCv6L0LbgcdKNbmyzvNakk-vyUb1afED_FaeWicPRpCJPbJTq-yRVTGVMVSZezMwSRsIDEUvH3gTJ67lPk_GlM9TWeiqKPVBpAZL8r3vz7L-MDzFCmXDFBVShSPd8_y-smkMq8Xx1W6XV8dBqDbLwGnRqf6qaY4Lc9uGUquf-3DFyAI4Yqyyrk4_fgqCnzbjZuW_70_XTazTlTpJOadQeAArVp9TkBJaq0kDGoNkh1q-Z6nnEaNlnPWfh7ZgPNBk1VK_iZZxsgPf5TLqJjyh584YW36mH3audEtzBVXJRN1dmU1tIGPsF9w49LSpIDKn8Oa8hU7ExnvMcpaZE8g-dS_Z1ZFB43NAfkdzaP5y8PDLgmGzQzPHaNYtA_xd_0QiK2jucRDwgh3c2vSdCNnT0eJPug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f2197035aa.mp4?token=Zx3DX4d-GsI1jCA8gmvpCxPTPCL7f7IsTzk3U2bN-kgXnAjie4os6xiVudzQXAWvwMRomDb-_CJZIuWGChZ6-Tp6uLkL4iCph4ZPy10MJfHR8sIZB6p_oDpwNo7HrNjALkDrQGg3OmYWwINg9hYR0SC1ozteacsNwq1HK5P94X08wwez1Y72oI8xzlK-mb9JxFsBnVn8o8COzYsOc1WUL1F_Jh2izvgua0JbBDCOHb7oKYzLFyfAAVM_sD-1xxGicc4_W_1Gcbxr7JDvolCv6L0LbgcdKNbmyzvNakk-vyUb1afED_FaeWicPRpCJPbJTq-yRVTGVMVSZezMwSRsIDEUvH3gTJ67lPk_GlM9TWeiqKPVBpAZL8r3vz7L-MDzFCmXDFBVShSPd8_y-smkMq8Xx1W6XV8dBqDbLwGnRqf6qaY4Lc9uGUquf-3DFyAI4Yqyyrk4_fgqCnzbjZuW_70_XTazTlTpJOadQeAArVp9TkBJaq0kDGoNkh1q-Z6nnEaNlnPWfh7ZgPNBk1VK_iZZxsgPf5TLqJjyh584YW36mH3audEtzBVXJRN1dmU1tIGPsF9w49LSpIDKn8Oa8hU7ExnvMcpaZE8g-dS_Z1ZFB43NAfkdzaP5y8PDLgmGzQzPHaNYtA_xd_0QiK2jucRDwgh3c2vSdCNnT0eJPug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇺
گل‌سوم منچستریونایتد توسط ششکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106179" target="_blank">📅 23:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106178">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c7c2e2ba0e.mp4?token=dvOgw4JjXzzmS1E3cYjC2ZV_2HG5qSKRPubf8oA17CBbh5aKsMFC588jlC3b13Abo7HmMIZLqe5ap9JXz-PdmYqdFnH5nv8ls1Z4AmTH0NSHHJeF2kbeo5BjEvvb4imn8hV0vF_Egmj_lyFRHyYsQtnBq3KE19SaFC8mOLnWbP9Y4yU0Mvl9fKuySf0aECrcMYsVjZey3tl7-qAzctXsMaisJi1J7lTGke8EO4Ji10klaVnOyZ9kPuADRgCQk2AbN8JkIUcRYW1b6ya4lq3YYawk4yzUYXxrVgQrEK332wWXNVxtZLron5ulHw6rxvzPXIRVZkAaK8fM2KbnJLjTBYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c7c2e2ba0e.mp4?token=dvOgw4JjXzzmS1E3cYjC2ZV_2HG5qSKRPubf8oA17CBbh5aKsMFC588jlC3b13Abo7HmMIZLqe5ap9JXz-PdmYqdFnH5nv8ls1Z4AmTH0NSHHJeF2kbeo5BjEvvb4imn8hV0vF_Egmj_lyFRHyYsQtnBq3KE19SaFC8mOLnWbP9Y4yU0Mvl9fKuySf0aECrcMYsVjZey3tl7-qAzctXsMaisJi1J7lTGke8EO4Ji10klaVnOyZ9kPuADRgCQk2AbN8JkIUcRYW1b6ya4lq3YYawk4yzUYXxrVgQrEK332wWXNVxtZLron5ulHw6rxvzPXIRVZkAaK8fM2KbnJLjTBYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم منچستریونایتد توسط برونو فرناندز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106178" target="_blank">📅 23:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106177">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7a2f3527a0.mp4?token=tnKQ05XzXb6nSkf4i5uaFLqBLBCqAcZx8YXdoxx0bdfjP6Y0k6EOG58NBghQsdwQNTmUhQ5pj4qx8VG2M55qO8JtMAoW0J4lWfJiW9ZuQW4JQM8fW5tAGn7UdRBEyYGrtv1gATTUo7QkchG-9BMSMcEyttxIFzvQ0rjbyBCIVwmN_t65hKy_QsfkgVUxfLZUoD6F2zw3XvHfeIixKs0cd0oTIYZb4A3h7CzqPb1vJ_Cfrmlo7q8Cz0vA6GZ-U-Q-5UROThme152WKbI7guUm59PAMZpvXBzFNPHdFQhrI8A8xyhR7dtv_5hK72oOPkZwIaHM3YRBxuPiMqvpXLMmMKPhS5nsMs7MAQqMQPGIeJ-5eUMs0hsvwwgdv9VhpYHcay_ezXwGNG5yXeBQy0UQ1djMXteweuvoFvCSH2lRnOzWg422QN74OamBITFdOCZ6JXPj6ROKkwwRuyhrsrK2z8-WdR8kBPvEULBiKRyvsSrPlH82qLAYCBDJ_36m231Iu5B6qTAqzEanPT8xQgwFzYml8Cq6cyURh5fjnsYFnyyUBPPcl3QVEZIp-ETWAoz--wLId2IhqtV1V1hnv7tYfQsE0DQGY_iVbBGbczS8xXipOWk_aRLX14WxzEsG5Z44Iq7y87NT7Egt5Hula2FBGdjkcH-W_U0Uw8HPB9a75jU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7a2f3527a0.mp4?token=tnKQ05XzXb6nSkf4i5uaFLqBLBCqAcZx8YXdoxx0bdfjP6Y0k6EOG58NBghQsdwQNTmUhQ5pj4qx8VG2M55qO8JtMAoW0J4lWfJiW9ZuQW4JQM8fW5tAGn7UdRBEyYGrtv1gATTUo7QkchG-9BMSMcEyttxIFzvQ0rjbyBCIVwmN_t65hKy_QsfkgVUxfLZUoD6F2zw3XvHfeIixKs0cd0oTIYZb4A3h7CzqPb1vJ_Cfrmlo7q8Cz0vA6GZ-U-Q-5UROThme152WKbI7guUm59PAMZpvXBzFNPHdFQhrI8A8xyhR7dtv_5hK72oOPkZwIaHM3YRBxuPiMqvpXLMmMKPhS5nsMs7MAQqMQPGIeJ-5eUMs0hsvwwgdv9VhpYHcay_ezXwGNG5yXeBQy0UQ1djMXteweuvoFvCSH2lRnOzWg422QN74OamBITFdOCZ6JXPj6ROKkwwRuyhrsrK2z8-WdR8kBPvEULBiKRyvsSrPlH82qLAYCBDJ_36m231Iu5B6qTAqzEanPT8xQgwFzYml8Cq6cyURh5fjnsYFnyyUBPPcl3QVEZIp-ETWAoz--wLId2IhqtV1V1hnv7tYfQsE0DQGY_iVbBGbczS8xXipOWk_aRLX14WxzEsG5Z44Iq7y87NT7Egt5Hula2FBGdjkcH-W_U0Uw8HPB9a75jU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول منچستریونایتد به صباح توسط کونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106177" target="_blank">📅 23:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106176">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8476aaa93.mp4?token=blCUnL7S-iGXnCmGl005KhsrK5JQ4Pr5IRhPaR9SMMlpKNlhpEVNhHLRSj0SbtQSsiAGfAOpJuH5oYLWufO9PWCiTINTdi3Ew-afUsaP6DQ4LKoyiyzUNGXmvTYaK3s0RKSShWKNysXs7T-bjIQ3oC8cbbV5F6YxR1R0c88D9IZifZ0mOSafarmcJ1nxyA_GzzxNKQWttlKwaksaJRPWjK_7s1OQpeLobm37wqDps63ZmbnIlUb3sPZSc2-RSewUPSkPpmmyr2C_S8gF9bpQv3kaqhGdyH-XXQyD5WxTKX034vHqdLGnM8gCE0v3BJRhbS4_eVBLR9gXhp60buLe6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8476aaa93.mp4?token=blCUnL7S-iGXnCmGl005KhsrK5JQ4Pr5IRhPaR9SMMlpKNlhpEVNhHLRSj0SbtQSsiAGfAOpJuH5oYLWufO9PWCiTINTdi3Ew-afUsaP6DQ4LKoyiyzUNGXmvTYaK3s0RKSShWKNysXs7T-bjIQ3oC8cbbV5F6YxR1R0c88D9IZifZ0mOSafarmcJ1nxyA_GzzxNKQWttlKwaksaJRPWjK_7s1OQpeLobm37wqDps63ZmbnIlUb3sPZSc2-RSewUPSkPpmmyr2C_S8gF9bpQv3kaqhGdyH-XXQyD5WxTKX034vHqdLGnM8gCE0v3BJRhbS4_eVBLR9gXhp60buLe6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
بازی استقلال ـ پیکان، داغ ذوبی‌ها در دیدار با پرسپولیس را تازه کرد؛ باشگاه ذوب‌آهن نوشت: دلیل مصونیت تیم پرسپولیس چیست؟
❌
⚠️
باشگاه ذوب آهن: دو صحنه در یک نقطه از محوطه جریمه و در یک ورزشگاه
🟢
یکی امشب، چک شدن صحنه توسط وار و اعلام پنالتی به دلیل بی احتیاطی مدافع. دیگری سه شب پیش، خاموش کردن VAR و چک نشدن صحنه به بهانه پایان بازی و اعلام نشدن پنالتی و دقیقا همان بی احتیاطی مدافع پرسپولیس و ضایع شدن حق ذوب‌آهن برای بار چندم تا هفته ششم لیگ برتر
🟢
⁉️
قضاوت با شما؛ چه کسی پاسخگوی حقوق از دست رفته ذوب‌آهن است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106176" target="_blank">📅 23:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106175">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
‼️
🇮🇷
اظهارات خداداد عزیزی علیه فدراسیون فوتبال: پول ندادند، VAR آفساید را تشخیص نمی‌دهد
🔴
فدراسیون پول شرکتی که VAR را آورده نداده و VAR اصلا آفساید لاینشون کار نمی‌کند و نمی‌توانند سر صحنه های آفساید تشخیص بدهند.
🔴
آقای فدراسیون چرا خط کشی نکردی صحنه رو؟ شما وجود ندارید اگه راست میگید بیایید خط کشی کنید و نشون بدید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106175" target="_blank">📅 22:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106174">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOKAL75v-DD5id3-VQo97E0qOoTc8rHLvzGiBird9CKpBpCWtK7_iJ99U34EWl26pknffH15PZ-l55CRGEoDIvJuMDk1H0zCxDZ-fLxCATqqolDPTt4WZEtCr1PUHXtAAhxWZJkTtcKiYQhrftRWo2GuKapmYxelEQpN2Z15EihVS_ee7XcGCRtlLuuqFo9VQHv2roKYtV32EB07NuWKwsoNLPDkJc74cSdE7ilWtoIuz_8qiEfVzkxbqKaSzJrJXSBjaNhQSEbkR95Omh9VKXe8SABVa7cppoPKEF61oIv7_Dnd_1_pok5vAjmiKgjPxLuXaCkn0neeeJTTKvDdMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇮🇷
‼️
واکنش خداداد به داوری بازی تراکتور و اس.خوزستان: تبریک به فدراسیون و کمیته داوران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/106174" target="_blank">📅 22:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106173">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‼️
❌
🇮🇷
🇮🇷
بیزاتی مربی استقلال:  دلیل لغو بازی رقبا را نمی‌دانم؛ شاید چون بازیکنان پرسپولیس قرار است بروند تیم ملی، بازی آن‌ها لغو شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106173" target="_blank">📅 22:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106172">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/588203f560.mp4?token=enak7UkkpZiuEYnlbyL6dkyembGxzKLF4Lihf3H_QMSz7xrC7wG86Mjv6CAb8c9kOTKA_Tn6CQj5HOCP0wmXuS-zxH3NwLXVKGrKWoDclx_bBvM4iwEkeiyzctIo5ckRhnk_vtqu5btIjweuntk3sB2nnz2SSQFA_Ov5PAiLbkuzo7Rpk8p7qk8HRjVeM6AaGlb68gOrgqGgXrk0eiseL8PbrOqZdl6wN-V53BDgYuAX-9gUDPyOcc-3dsycPPy6cWwDVAhBVgFfjYwfM46GzXcFmyFByync4R99V-EOmwS9M581eD4wcwv_v1SdvUJcqXoI4iZRW-qGKqbF8WOsUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/588203f560.mp4?token=enak7UkkpZiuEYnlbyL6dkyembGxzKLF4Lihf3H_QMSz7xrC7wG86Mjv6CAb8c9kOTKA_Tn6CQj5HOCP0wmXuS-zxH3NwLXVKGrKWoDclx_bBvM4iwEkeiyzctIo5ckRhnk_vtqu5btIjweuntk3sB2nnz2SSQFA_Ov5PAiLbkuzo7Rpk8p7qk8HRjVeM6AaGlb68gOrgqGgXrk0eiseL8PbrOqZdl6wN-V53BDgYuAX-9gUDPyOcc-3dsycPPy6cWwDVAhBVgFfjYwfM46GzXcFmyFByync4R99V-EOmwS9M581eD4wcwv_v1SdvUJcqXoI4iZRW-qGKqbF8WOsUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
وضعیت یاسر‌آسانی حین خروج از ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106172" target="_blank">📅 21:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106171">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBN1at9-7DD4PY1sAIHC5FflTQD4UEWpG09Hbbs3f6JR2EzKoA8_eOIMJpj8LnK9Bhz4SxHNjfzwr0OqjZz4NLjucSC2X_EXdg2h9FVjSaHja8HPpmk4_MwfL2OnTMNP4fuAmoqoAUt3QR3mQzg7wvonFpQaReM2LfLKAEhCMlQW3OuV7k6BNU056eXzezAqyiSNi1cWy1dZTzt8N8zXvFk9DBqxJa5oN14FELl1Q8wa3CS93ADsEwwsOsFl0ol0i3v0oLY8z3NKAPh_y5VCWio9y11tMSgqHQR4pL7VBR4Fb6fb_OKqdyBpLBEr26ngVwWYK9AAC9RPAH2MrA7rAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
⭕️
❌
🇮🇷
پزشک استقلال در حین خروج از ورزشگاه: یاسر‌آسانی شرایط مطلوبی نداره و حضورش مقابل السد تقریبا منتفی هست هرچند باید تا روز شنبه منتظر بمونیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/106171" target="_blank">📅 21:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106170">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
‼️
🚑
🇮🇷
مصدومیت ستاره استقلال در آستانه بازی با السد؛ آسانی لنگ‌لنگان از زمین خارج شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106170" target="_blank">📅 21:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106169">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df1846b0f6.mp4?token=YDvvSlpplKZhsoc4UlgLbjCiEAvC7QXJmcOas91zozyMj5pcWdnuifaDejddUVk5x5FVDpPbFsv64POmgbUvA1Mk0sv_o6ZVIJBMnro3xIDn0ox_muyMsyuyLZsksYggaz3TscTMQAWPoqZIHWUWeDmP-SYlPrbrzeEwZ1VyCuaAwzGtUI7CLMs4d6HaNfaNfEu1EhlXImxxqvk98lUyG3ml1nnBK7zod_-I1lnngirJrK7vb87FTfuztMRBikDYCJV_--fItfRihw2Rjv1fWGg7AEgy6sQ_p6KarVcm-OvLMXwhktOZXOgfzV6L8b4Ekdii1D5VtPTXNWCl5dzACA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df1846b0f6.mp4?token=YDvvSlpplKZhsoc4UlgLbjCiEAvC7QXJmcOas91zozyMj5pcWdnuifaDejddUVk5x5FVDpPbFsv64POmgbUvA1Mk0sv_o6ZVIJBMnro3xIDn0ox_muyMsyuyLZsksYggaz3TscTMQAWPoqZIHWUWeDmP-SYlPrbrzeEwZ1VyCuaAwzGtUI7CLMs4d6HaNfaNfEu1EhlXImxxqvk98lUyG3ml1nnBK7zod_-I1lnngirJrK7vb87FTfuztMRBikDYCJV_--fItfRihw2Rjv1fWGg7AEgy6sQ_p6KarVcm-OvLMXwhktOZXOgfzV6L8b4Ekdii1D5VtPTXNWCl5dzACA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚑
⭕️
🇮🇷
سعید سحرخیزان نیز لنگ لنگان استادیوم شهدای شهر قدس را ترک کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106169" target="_blank">📅 21:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106168">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/020d7e0eea.mp4?token=nqmhz_hycY7nNgEEwH-ceYxlEq6vYj1E0pakNcOw2531GWb7TRQNz3O-hqlOtYp7XkoD6eKCcNpKUJX17UKyt06o_L23sGpZm8VGpoycrhxOz2gcAyuVvT3svYd8k6_ZkrWMY1-0ifutHSZ4a2NcRJB7hinYcEwiMpVzUWvmo6GVuBJvzpZoi-tU4puFx0_vTx_vgX5dmFJqgA0tZvBVxP_wr6xxhHDCtSj9o6xpgfiC-E1m8Swdo6CMFV2ZCndIUSzW1qXOs7x6Hz1bDvw4ktoYQ6zo1oZ1yERb1TaN18eO_yrD5GX5DtM81zxXMf_IXmXNIhGPounhlqAbePWYXxlZbhXrvUFjGW_u-x_7weQ8Tyf6xeeL6UKOMh_gwnzUPuRcm3tRK1_78EfUwZC4TivrpttL0_rFzcG5OAA_NiGB5egQpBk_Ab655qI-aJzgAXPEUZYsV-y6prNZoc0lPD97WJAdj0WX2BqnBsZls-TcY8TyBtDFin2jZ-OPIdfUqtyDSKMjHvKQ31Yz-Z0pC-P37VJoto9OVbuquIQcowE25dtBWgqWMRO3--RwwXzGE1pghiMEcYoYOBBH-UjxsKJTBop8rF2QOK4WqFMp3tBSRg9vst5l_CyDEYv8K05rR-YWWqw44ZaewZRQQB7vSNrhn4IiRm_1URIBZCdI8EI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/020d7e0eea.mp4?token=nqmhz_hycY7nNgEEwH-ceYxlEq6vYj1E0pakNcOw2531GWb7TRQNz3O-hqlOtYp7XkoD6eKCcNpKUJX17UKyt06o_L23sGpZm8VGpoycrhxOz2gcAyuVvT3svYd8k6_ZkrWMY1-0ifutHSZ4a2NcRJB7hinYcEwiMpVzUWvmo6GVuBJvzpZoi-tU4puFx0_vTx_vgX5dmFJqgA0tZvBVxP_wr6xxhHDCtSj9o6xpgfiC-E1m8Swdo6CMFV2ZCndIUSzW1qXOs7x6Hz1bDvw4ktoYQ6zo1oZ1yERb1TaN18eO_yrD5GX5DtM81zxXMf_IXmXNIhGPounhlqAbePWYXxlZbhXrvUFjGW_u-x_7weQ8Tyf6xeeL6UKOMh_gwnzUPuRcm3tRK1_78EfUwZC4TivrpttL0_rFzcG5OAA_NiGB5egQpBk_Ab655qI-aJzgAXPEUZYsV-y6prNZoc0lPD97WJAdj0WX2BqnBsZls-TcY8TyBtDFin2jZ-OPIdfUqtyDSKMjHvKQ31Yz-Z0pC-P37VJoto9OVbuquIQcowE25dtBWgqWMRO3--RwwXzGE1pghiMEcYoYOBBH-UjxsKJTBop8rF2QOK4WqFMp3tBSRg9vst5l_CyDEYv8K05rR-YWWqw44ZaewZRQQB7vSNrhn4IiRm_1URIBZCdI8EI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
ساکت الهامی، سرمربی پیکان: این برد را به استقلال تبریک می‌گویم؛ ان‌شاءالله در آسیا موفق باشند/ در نیمه اول تیم برتر میدان ما بودیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106168" target="_blank">📅 21:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106167">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4fb8db538.mp4?token=fEwFYfb5-RU1eWOkAtWrFLG1oUnimbgMnRW9wiMFOa7tjifTDPVDDJxwuCIQvjuiGNJ20He2QEGUiPQmtMqwH1V_hV-fQgLATD1cYfBIUL1KKwepPZ09qPiByZrGIyqE8r8eBHc8fctcaPqpEfrxT13kiIqyoDzZqnJWvdJecsQ9PxgrpT4GyyRKxqOmXUX6ImNoeblwXHCC-Dh1gprC2HueuyB6SPohlkJw-gZ3r3Rfjfmb-uyiucnBgYYNS5kwKhCfayU_lPAiwVosy3B1dtXnSwgQXVR-AP2hWGAobJEJ6fQZVKG8XU6op7jvnofwyiKDSwX1O6yMmwhJE3xotQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4fb8db538.mp4?token=fEwFYfb5-RU1eWOkAtWrFLG1oUnimbgMnRW9wiMFOa7tjifTDPVDDJxwuCIQvjuiGNJ20He2QEGUiPQmtMqwH1V_hV-fQgLATD1cYfBIUL1KKwepPZ09qPiByZrGIyqE8r8eBHc8fctcaPqpEfrxT13kiIqyoDzZqnJWvdJecsQ9PxgrpT4GyyRKxqOmXUX6ImNoeblwXHCC-Dh1gprC2HueuyB6SPohlkJw-gZ3r3Rfjfmb-uyiucnBgYYNS5kwKhCfayU_lPAiwVosy3B1dtXnSwgQXVR-AP2hWGAobJEJ6fQZVKG8XU6op7jvnofwyiKDSwX1O6yMmwhJE3xotQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
هوادار تیم‌ فوتبال استقلال: تا قبل از ورود ماشاریپوف چیزی از تیم ندیدیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106167" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106166">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c788208205.mp4?token=omyCJPHIEuydDbxql2byLnN9cyQrT5TIk6SaidXdbccl0m6-0aTw96V5qs_IYxAOCB4aX0BFkaaiFJgzpB8rJdukIMExXTlrWxGo9om1-biBGqiKY6IB6QFQL5H_M752kPP8Y6FvWVTGvLKYzjYxizplbvF35M11WQARAB4252Vqk0ypjzZCdudjwpmxYguEQHYcLqdDrjjy7NUqAW0-IYVjQKlAi8Wr9aaQC62YMM2JgDOajLtOarOlbyoo3CaBkyq_UeSu14XSLFG4b_-0aVjTGnq4wFU-h-X2NsLT1-xvKFBfXwwDk226_aZUBwE8_yTlVdo2AO4vQL_7yfcWgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c788208205.mp4?token=omyCJPHIEuydDbxql2byLnN9cyQrT5TIk6SaidXdbccl0m6-0aTw96V5qs_IYxAOCB4aX0BFkaaiFJgzpB8rJdukIMExXTlrWxGo9om1-biBGqiKY6IB6QFQL5H_M752kPP8Y6FvWVTGvLKYzjYxizplbvF35M11WQARAB4252Vqk0ypjzZCdudjwpmxYguEQHYcLqdDrjjy7NUqAW0-IYVjQKlAi8Wr9aaQC62YMM2JgDOajLtOarOlbyoo3CaBkyq_UeSu14XSLFG4b_-0aVjTGnq4wFU-h-X2NsLT1-xvKFBfXwwDk226_aZUBwE8_yTlVdo2AO4vQL_7yfcWgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
‼️
هوادار استقلال: به زور بردیم؛ آقا سهراب دست از لجبازی بردار!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106166" target="_blank">📅 21:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106165">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
صالح‌حردانی مدافع استقلال: از آقای سهراب بختیاری‌زاده عزیز عذرخواهی می‌کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/106165" target="_blank">📅 21:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106164">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e33ed4a004.mp4?token=XQT6Zy_L8WThCyiPYh-3N5yYPr0fOgo3ht7qFsR7pxh39SbTSVNZrbEunbMZZE_32qDEywgFz0O6gMULVIQvhoggLyEvEjub1ZSxg-VRUb5REUgg_Hec7Xs13j3UIHmGDBl2-5mTvfTQsbR9cZMqYdx_twggJ44DTwOnFyZHB0hPR_hXbZk0uoyIY3b2yuGidBm2OCS7SNnX0W5PldzibF1DTfMHcWUj2Xz0093OjN6PIhlPvBxDvEyfYrW8d0QWJXxzFjef845QCOHVpFR0pFQD0vamCj8uRRLd_WS1jRi0otm_hYmcmd_Z80fYLEis26Da6UZDDMOgL7fKVvkmBBf4ojePkSqjEh-k3AY4NvD4ZKNcDdLxCEgbR8gMDXoZ7byJz9AByeKwkhQIseCNqwYZqlhEB5oglScIgJHOXKkIHu02o4T0eKhGOA5nHSMjQnK6geuKBh1sHLNzanDXbNkxV0qHCw68OYha3LvWYL4NJUIA0NCTE92QCK2Lv9WF-VJyAvNPx3HcNBitMu402DIGXLChiQe-pHXuJDwhsp5Anh8HX2BVvbb5Kt3HQ2DaIBGsAM3thURzG19RXsG755ydVKgiPMPgYZLmBXwgYTe_R07-PJgS46OnSpk5jIW1ejRdnsNHXckxeUCfYc2o2xdVFrdOL4vHdQXJ_sxve8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e33ed4a004.mp4?token=XQT6Zy_L8WThCyiPYh-3N5yYPr0fOgo3ht7qFsR7pxh39SbTSVNZrbEunbMZZE_32qDEywgFz0O6gMULVIQvhoggLyEvEjub1ZSxg-VRUb5REUgg_Hec7Xs13j3UIHmGDBl2-5mTvfTQsbR9cZMqYdx_twggJ44DTwOnFyZHB0hPR_hXbZk0uoyIY3b2yuGidBm2OCS7SNnX0W5PldzibF1DTfMHcWUj2Xz0093OjN6PIhlPvBxDvEyfYrW8d0QWJXxzFjef845QCOHVpFR0pFQD0vamCj8uRRLd_WS1jRi0otm_hYmcmd_Z80fYLEis26Da6UZDDMOgL7fKVvkmBBf4ojePkSqjEh-k3AY4NvD4ZKNcDdLxCEgbR8gMDXoZ7byJz9AByeKwkhQIseCNqwYZqlhEB5oglScIgJHOXKkIHu02o4T0eKhGOA5nHSMjQnK6geuKBh1sHLNzanDXbNkxV0qHCw68OYha3LvWYL4NJUIA0NCTE92QCK2Lv9WF-VJyAvNPx3HcNBitMu402DIGXLChiQe-pHXuJDwhsp5Anh8HX2BVvbb5Kt3HQ2DaIBGsAM3thURzG19RXsG755ydVKgiPMPgYZLmBXwgYTe_R07-PJgS46OnSpk5jIW1ejRdnsNHXckxeUCfYc2o2xdVFrdOL4vHdQXJ_sxve8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تاجرنیا: امیدوار به حل مشکل صالح هستیم. جام قهرمانی استقلال؟ خبر موثقی ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106164" target="_blank">📅 21:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106163">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAWD0eIt2Ba5p4mis5AWE5-N43SSadhRVB8l_wvVa_ESUVHVSfmTkA7MQ_5GA-yg1U6WQaX3FprNeTTyzlqKfGPgdC2Z6tj0wN2iyCp8JiG9tz0NYY3OxIJNzOHTXGk1ll0AQMbOYaNh8RcxuD32-c4hmGMl-RVEaVgYJv2a6Wui1AZbkxlRwqlmQjzsZYHKl2pl778usgGnH0iUMSV58dushkwUsZ86mKFQtXX7Sjg2bVK_D-bBDWJge9n77BLXjZXDZs8Ov8-FdjqQSklhyeSCqZBOKeHnSSHuPpF7zrhAX9A3wis9lICmRYpYpySRSqDWvq5KK1xb7IDWGMjQXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌هفتم لیگ‌برتر فوتبال؛ خارجی‌ها عصای دست سهراب بختیاری‌زاده شدند؛ استقلال با برتری سخت و دشوار به استقبال بازی السد رفت!
🇮🇷
استقلال
😃
-
😏
پیکان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106163" target="_blank">📅 21:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106162">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6bc94122.mp4?token=AfDLO1cYdSV4mwbVJlvjaITQKmsOjSyfl0M5G_PFbp64JwSXrvGEndFklXA24FaMg9-vvorzj_JOy-SHdBkS2hBmo8OXEII4cG6D5gbepH2iWFpNib0YDmlok3lA3XwrpjwQF67UqkMCptDm9VrG4gAlA4nZm5slKtYt1RdrQyXQhwHOMG2O875c__d52QJwPFq_zySHCi1hIcDBV98NB8MW4pFHf49i5VYNAWdXZERIJd5CenJkD-1IPmp_-8cEYjSU-uFyMcmhHd2zlVuFOr8b9qOuYH596O8l8m3Oa-7_AE_UTsgMFSCum0ferBy51CgDtHfR8PG6bB00vuuMhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6bc94122.mp4?token=AfDLO1cYdSV4mwbVJlvjaITQKmsOjSyfl0M5G_PFbp64JwSXrvGEndFklXA24FaMg9-vvorzj_JOy-SHdBkS2hBmo8OXEII4cG6D5gbepH2iWFpNib0YDmlok3lA3XwrpjwQF67UqkMCptDm9VrG4gAlA4nZm5slKtYt1RdrQyXQhwHOMG2O875c__d52QJwPFq_zySHCi1hIcDBV98NB8MW4pFHf49i5VYNAWdXZERIJd5CenJkD-1IPmp_-8cEYjSU-uFyMcmhHd2zlVuFOr8b9qOuYH596O8l8m3Oa-7_AE_UTsgMFSCum0ferBy51CgDtHfR8PG6bB00vuuMhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🚑
🇮🇷
مصدومیت ستاره استقلال در آستانه بازی با السد؛
آسانی لنگ‌لنگان از زمین خارج شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106162" target="_blank">📅 20:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106161">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇷
🇮🇷
خلاصه بازی استقلال یک پیکان صفر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106161" target="_blank">📅 20:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106160">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4H2Xr8coA4HiKSThqJBMue_K7oEdAZLihiHD0HfCZAI8hBNVmwwsp9ZEUlBlbn05YhVknipEmjievpKiLHDFjsynDW9PbkvAm98P9ehoAuQt7HGa7l3pbhAlhQcKBn14DlD6Msj4xAJ8EWoWJ5hb2gYapYgkdTwknUbiElqUDufUzPl-obysVrzw978sFSDebfKNZBaI_p6pxqw_k08IOcHirfaCjpwxqfZMTgeT5vbvII30FA_nfkYXUPSJIpQn9mIWR0KYIEpC8rIHoI54HUrIrx9oPQ_L8WZGrug9UgFtPQrSIipKpUycZz5KEgE61BkHTZCVm1IAq17n0YRYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌هفتم لیگ‌برتر فوتبال؛ خارجی‌ها عصای دست سهراب بختیاری‌زاده شدند؛ استقلال با برتری سخت و دشوار به استقبال بازی السد رفت!
🇮🇷
استقلال
😃
-
😏
پیکان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106160" target="_blank">📅 20:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106159">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33ea76eac.mp4?token=S-K6Og1C64yXTOoKVzLYXghpXLl_zFClyEureIiz0dheUSY-9Ob-daTv3SWjdb1CpmCbasm7yoIFmxO7_S-7KHIcv5rwzPg6oV4YBrvEGN_p7R1V16Zkd0So4skO4AkCDSeYwB28USlAM_e2umBJZISeZ5Np6iW7EFBJ4etPdYFXvPPeidk4ZHx_lN4_7AwyJgTq01n9CkGn8Q6Vl_j9bUz5N37vFsX8t3Hx9Ooo0js2dstDLuLYtXWvNz8fkf8JWN-KtVPjUQAZMvbNbimD2-dDDwMAs4VwDFrIpoRD9rYJfRqWJmvhpXlxrv-5vxhB-jjdwZJ11eH8OY__WosmzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33ea76eac.mp4?token=S-K6Og1C64yXTOoKVzLYXghpXLl_zFClyEureIiz0dheUSY-9Ob-daTv3SWjdb1CpmCbasm7yoIFmxO7_S-7KHIcv5rwzPg6oV4YBrvEGN_p7R1V16Zkd0So4skO4AkCDSeYwB28USlAM_e2umBJZISeZ5Np6iW7EFBJ4etPdYFXvPPeidk4ZHx_lN4_7AwyJgTq01n9CkGn8Q6Vl_j9bUz5N37vFsX8t3Hx9Ooo0js2dstDLuLYtXWvNz8fkf8JWN-KtVPjUQAZMvbNbimD2-dDDwMAs4VwDFrIpoRD9rYJfRqWJmvhpXlxrv-5vxhB-jjdwZJ11eH8OY__WosmzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آزادی چه توپایی گل نمیزنه و ۱۰۰ میلیارد پول میگیره از استقلال
🤣
🤣
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106159" target="_blank">📅 20:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106158">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c661b28aa.mp4?token=GhLJ3gIeqfx6KBvk036c54j75l6AG_lx3SKSj0Jl9wcU3hOMuD5GM53gON6Z90pNFch3g42epuj3k4Tx2QryyOFpbIBfwY0GoQYG0JFF9NOspAs1PptPiWvjhDsZC6Z4PK8ps-_XHx32s4O9-cItjtCJuE7yS1JIzv2EoTZzaBJmzulVovoP0QXXGbHgv4C8KmK3NU9mU8gsnVX-tsKI5xpu1BltigkFYvWr58NlzXSIVlmAQUAEcsAD-B07_jnn0tl0g6IR32Pu1TKbpH1qLa9UPD8jI2x1B7cEeAussXF8IKiZ5mh1uBbuKP1jaHDbgJNtSiZKA6EDR_Dys8K4Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c661b28aa.mp4?token=GhLJ3gIeqfx6KBvk036c54j75l6AG_lx3SKSj0Jl9wcU3hOMuD5GM53gON6Z90pNFch3g42epuj3k4Tx2QryyOFpbIBfwY0GoQYG0JFF9NOspAs1PptPiWvjhDsZC6Z4PK8ps-_XHx32s4O9-cItjtCJuE7yS1JIzv2EoTZzaBJmzulVovoP0QXXGbHgv4C8KmK3NU9mU8gsnVX-tsKI5xpu1BltigkFYvWr58NlzXSIVlmAQUAEcsAD-B07_jnn0tl0g6IR32Pu1TKbpH1qLa9UPD8jI2x1B7cEeAussXF8IKiZ5mh1uBbuKP1jaHDbgJNtSiZKA6EDR_Dys8K4Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل اول استقلال به پیکان توسط آسانی(76)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106158" target="_blank">📅 20:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106157">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
✅
گل اول استقلال توسط یاسر‌آسانی</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106157" target="_blank">📅 20:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106156">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d01d6e5347.mp4?token=adI9DuTEq0BuUBb0abXnXllGTP8WCb4uYoBs2GZaKagftpl6Mc6iVE05HvwQvF-hU1p1dEIRFdISVHA-3nyzU2FBP8ziWbCb2t0cNHICfyzfHrLiLCma_rAI-mE7EMWog5J-dTFp6gYtO4t_HHI_zU8rZsCSKX0W8zLK2WXAaQJGaPsFphQYrpOAsLn6P7XPXtyF8qlHQLuPaEApkxhiwXUfvmSdDvPV5nKGwF_4tGaun1vah_gk8-QgrbXAw5tVPaLxUfemZ8a9sAaL025Lz57RG0mNjsq1XxBTtQ_AQf0P1vd8bCQK3E_MXxnERcdifY0mfOYBXdjrXIB5H_ozpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d01d6e5347.mp4?token=adI9DuTEq0BuUBb0abXnXllGTP8WCb4uYoBs2GZaKagftpl6Mc6iVE05HvwQvF-hU1p1dEIRFdISVHA-3nyzU2FBP8ziWbCb2t0cNHICfyzfHrLiLCma_rAI-mE7EMWog5J-dTFp6gYtO4t_HHI_zU8rZsCSKX0W8zLK2WXAaQJGaPsFphQYrpOAsLn6P7XPXtyF8qlHQLuPaEApkxhiwXUfvmSdDvPV5nKGwF_4tGaun1vah_gk8-QgrbXAw5tVPaLxUfemZ8a9sAaL025Lz57RG0mNjsq1XxBTtQ_AQf0P1vd8bCQK3E_MXxnERcdifY0mfOYBXdjrXIB5H_ozpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✅
🇮🇷
لحظه اعلام پنالتی به سود تیم استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106156" target="_blank">📅 20:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106155">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
احتمالا پنالتی برای استقلال گرفته بشه</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106155" target="_blank">📅 20:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106154">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
احتمالا پنالتی برای استقلال گرفته بشه</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106154" target="_blank">📅 20:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106153">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
احتمالا پنالتی برای استقلال گرفته بشه</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106153" target="_blank">📅 20:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106152">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDoj1ay6KeVanMMW11-ayn83jThN5Q1DuPG-L2yAlmKR37orvr8T3Ly41sK-AI8PoCDIUWBT9s6BONWX91Kz8JCJvNztzbb1XTq6cPh7x_SXGblVoWI4AJNDR_jUlCzjVHD7aYOiQMTR_NmcidTvIZQUAw-f-vKo6jP81uI_BtUQIgHkKz1XgL4zOkkYWIWhNSBl7QccoQ4WXcP2oAIraM1KZsYdmR7E1NQB2dIzl1WSpafliEZLUov5TchwbegAU0UkRjosX32yrRgtvwV8SnN5SUg-Mics_oO4tdQiKdp2Wb03AaLj3AbkkdqNjVsKoSnorgwUf5NWuXEzmMTuhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
تیفو فوق‌العاده هواداران فنرباغچه مقابل رم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106152" target="_blank">📅 20:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106151">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac6a80c90.mp4?token=eZMhARRlEd_PNNMrvfqdETns9XpSrBpJMucg28G-tEmtqAUof00GTNNhcigXQsWitYIii9HZ_ISqY54MqIuKT3oNHgz4MxLum5Q171LUHMuUsQ-R4_-q3AC83TtWsDc2s_Aic-6XCUAw3jCJODTeBkd2yzCxXmBy6LEvO8avD2yVhKVHivu1mx0ZcchNk-ThmWbw5KEMCGhO1QFQi488gPznRNPnn4x36aKYsAWePddCUKqMPeWChudO5lDoIWMd-A_7kCAVsavCmeLTcdtn0swi3hvl7SUN_c92mcawPKkthkIivON2X-hPXjXyFc-2Ieh1AXXQhFRkFPISr0mxqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac6a80c90.mp4?token=eZMhARRlEd_PNNMrvfqdETns9XpSrBpJMucg28G-tEmtqAUof00GTNNhcigXQsWitYIii9HZ_ISqY54MqIuKT3oNHgz4MxLum5Q171LUHMuUsQ-R4_-q3AC83TtWsDc2s_Aic-6XCUAw3jCJODTeBkd2yzCxXmBy6LEvO8avD2yVhKVHivu1mx0ZcchNk-ThmWbw5KEMCGhO1QFQi488gPznRNPnn4x36aKYsAWePddCUKqMPeWChudO5lDoIWMd-A_7kCAVsavCmeLTcdtn0swi3hvl7SUN_c92mcawPKkthkIivON2X-hPXjXyFc-2Ieh1AXXQhFRkFPISr0mxqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇪
🔥
سوپرگل دیدنی العین به الوصل توسط عبدالکریم ترائوره با گزارش قائم خلیلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106151" target="_blank">📅 20:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106150">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226e1ece2c.mp4?token=MdjM8ezExOsL00E2aTzGph5HwvXq3RQLrIUL6VXKIRAS3wmLlU-keum1IwSjHGuh2dkRr5fdsXF0rzP7H9eHkR_Qq8IIMb9Dfd8OyoYM6fb0912wUQWB3wQEkMwJUMl9sOSR-2dCKtzugpCWmie4PndyRW_mXT2wHN2bLfXOb-gx__cDgHs68IxkqoiGDmyoHVQf9ig5Lke6I7jUmYq0QcS4ff-oVA6ZU85YiRy7-hKwj7oxwVvc9fmimTlJfW9rTLJ45qD40oi-wlwvx7M6rfOyrv1m0_esMO0335u8GUcDJ2HUJtqzfD50pBl_LiJD5j77AffQ9S4RKoH1tKPBBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226e1ece2c.mp4?token=MdjM8ezExOsL00E2aTzGph5HwvXq3RQLrIUL6VXKIRAS3wmLlU-keum1IwSjHGuh2dkRr5fdsXF0rzP7H9eHkR_Qq8IIMb9Dfd8OyoYM6fb0912wUQWB3wQEkMwJUMl9sOSR-2dCKtzugpCWmie4PndyRW_mXT2wHN2bLfXOb-gx__cDgHs68IxkqoiGDmyoHVQf9ig5Lke6I7jUmYq0QcS4ff-oVA6ZU85YiRy7-hKwj7oxwVvc9fmimTlJfW9rTLJ45qD40oi-wlwvx7M6rfOyrv1m0_esMO0335u8GUcDJ2HUJtqzfD50pBl_LiJD5j77AffQ9S4RKoH1tKPBBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل‌اول استقلال خوزستان به تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106150" target="_blank">📅 20:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106149">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZJ9wET1BmVfA23eDpYOh9eDlkdhl36TTkdjrJsf4q5WYaIJ_OGBO06vq_Ht9skACYlkCYh4rUtXDHp-xZOJxg-L3cSh2Um3weaaiwEfuX9iM6GRl_2MKfmgDJsOtznX_fxinGETN15laFIoe5BKNsXrdnuTUTceruZXNeEjQej3fatuHrlillEE5v7tGBjUJwb_5gjRWdpfnLlATzSEoBxSm34PuEkR6aN-r0Cr0_7UfQ53kOKnugt1KvQ5mOCjMwNW5qol4Xr94HUR4RONz2ECsRUXnU0vksIBwAp2niQmizer89FZQ2R0Yr1Itp89GRHsce62Aye4oI76UIRmbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
‼️
سقف دستمزد پرداختی تیم‌های لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106149" target="_blank">📅 20:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106148">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce42c1eb19.mp4?token=vdNSdGv8OMooIOhlhCzhFSyNlzoqFSaieEAG7gS5R7IOQlyrNylHDUIcbBpFZ5E48uup9FTn0xnjmSS8MeT165f17qrIW_cyz5WVxS9gZXGzlIE8xLTIgVkPzH0Erd9PBNfl3vFVatWWsTj6JLJ3e0Yk0CB46iQc1xe-QOgByOp3hfUfaFw4Sjba0aCk8vK4CSEJgPzIMdp7LGfGwJFFVLOAFMSf3W1ZuzUBaTjkw2cyPObkq_HyIcy8CSWYZShTFOjLpT1h7QRQFS3RQ1N90vebStesjWcv9YJ4bIKUouhWOWzDWL46fdMkzbHFyeR1STjochNe-SgJ5ndO1DUxTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce42c1eb19.mp4?token=vdNSdGv8OMooIOhlhCzhFSyNlzoqFSaieEAG7gS5R7IOQlyrNylHDUIcbBpFZ5E48uup9FTn0xnjmSS8MeT165f17qrIW_cyz5WVxS9gZXGzlIE8xLTIgVkPzH0Erd9PBNfl3vFVatWWsTj6JLJ3e0Yk0CB46iQc1xe-QOgByOp3hfUfaFw4Sjba0aCk8vK4CSEJgPzIMdp7LGfGwJFFVLOAFMSf3W1ZuzUBaTjkw2cyPObkq_HyIcy8CSWYZShTFOjLpT1h7QRQFS3RQ1N90vebStesjWcv9YJ4bIKUouhWOWzDWL46fdMkzbHFyeR1STjochNe-SgJ5ndO1DUxTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
تشویق شدید صالح‌حردانی پس از عملکرد فوق ضعیف استقلال در نیمه‌اول مقابل پیکان
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106148" target="_blank">📅 19:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106147">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/494b673a17.mp4?token=aPJScBph_izyNJGiJCDdpCb68HPxSip-2rD4EL9BymKjEp667RoiEDewkwsKHJmyoi_LgCgIGIXK1fVZa08sBRDZrpg3MxZuqeJ8vOHEWfOMeEoRlrjfBuFZqgMT_3fXRzRrIOOppbtqSiUqdmeAOgLdd7mSGPWF3BpTVDGotr6YxNQ2bLehDOlok1BKsvkikG0IGojXtW8eqx-ExPxGKhEXp-KvRktKnRrAkvN9TmgTN2cDDKSHfTZ5cO1ZPAWnMKmXEsQ9s4HcNVztmHUWAjB8BSROsooBzerc1WEutPs4DAteUsK01irY91QpLGawUYENW7yLrdSS065A8DOzQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/494b673a17.mp4?token=aPJScBph_izyNJGiJCDdpCb68HPxSip-2rD4EL9BymKjEp667RoiEDewkwsKHJmyoi_LgCgIGIXK1fVZa08sBRDZrpg3MxZuqeJ8vOHEWfOMeEoRlrjfBuFZqgMT_3fXRzRrIOOppbtqSiUqdmeAOgLdd7mSGPWF3BpTVDGotr6YxNQ2bLehDOlok1BKsvkikG0IGojXtW8eqx-ExPxGKhEXp-KvRktKnRrAkvN9TmgTN2cDDKSHfTZ5cO1ZPAWnMKmXEsQ9s4HcNVztmHUWAjB8BSROsooBzerc1WEutPs4DAteUsK01irY91QpLGawUYENW7yLrdSS065A8DOzQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
آغاز حواشی در استقلال؛ درگیری حامیان صالح حردانی با حامیان سهراب بختیاری‌زاده پس از پایان نیمه‌اول روی سکوهای شهرقدس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106147" target="_blank">📅 19:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106146">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae32d5f075.mp4?token=q5rjSqBLq9q9Tb84jbhGXT8uJQTrKobVd2Dr_Z1YYaIoA8EnIgZLtXdFMxEWRxl_KxQFhw-X_c1-ujmmNjiOl_t9Xu0zHc6dCmj52ViEsX8LRXfUiKGTKIXUXTMR80m53bywcyKduea0QZ_4QJop-285vGoJhmSSw2Cs3w3JJawvEv1cg-EUTidKgftKA2Cx_73XYOVhWwxaO0fChH_5wQE1tFyh3RLAxpZJucBNBALWIMhHCQO4dp6t3p9w5j9EpkHLiaPJg-7K7z_AavW2BXRX3cXc0OtbFfsNaoHMhtXRc1_jHXqq8dLNUzzoNWbC7gFHLEljdiLOv2FwyAdYEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae32d5f075.mp4?token=q5rjSqBLq9q9Tb84jbhGXT8uJQTrKobVd2Dr_Z1YYaIoA8EnIgZLtXdFMxEWRxl_KxQFhw-X_c1-ujmmNjiOl_t9Xu0zHc6dCmj52ViEsX8LRXfUiKGTKIXUXTMR80m53bywcyKduea0QZ_4QJop-285vGoJhmSSw2Cs3w3JJawvEv1cg-EUTidKgftKA2Cx_73XYOVhWwxaO0fChH_5wQE1tFyh3RLAxpZJucBNBALWIMhHCQO4dp6t3p9w5j9EpkHLiaPJg-7K7z_AavW2BXRX3cXc0OtbFfsNaoHMhtXRc1_jHXqq8dLNUzzoNWbC7gFHLEljdiLOv2FwyAdYEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
درگیری لفظی عوامل دو تیم روی سکوها؛ تنش و حاشیه در جریان دیدار تراکتور و اس.خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106146" target="_blank">📅 19:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106145">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRMTOVtpD3PBfGQqldShSboi-NBz7J-Qnrtf3pZ54MqG5jx8OKT6WlaG-3FfqiAMCbIZjaLm1HEmTHw1ALHeEOg2JOeQTZaklpHBT00fur9i3zB3gtYdxR0pghNDbjo_s8TdU0uuecDiyVjPSe-GIrB9S5g4Ht7lLtnPyAFPyJi7FqD4xPmJFkE5KkcUhKRr5LTcqPc63v4cN9mHvkH2d99o-0p82QxHAJWPnFW1FaZEz7ZINbU9LcpPW0YPmR2S8ti7hrby98-efHUanO-F7DAyawK34NEWM43F2NMraEfEgGFvv8oKeQ6HqmbeJlJ2hf_ccJxqV01QJoV2mTWdGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🏆
فینال جام‌جهانی ۲۰۳۰ در استادیوم الحسن دوم کشور مراکش برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106145" target="_blank">📅 19:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106144">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">استقلال با این سبک بازی جلو السد باید به آیات الهی متوسل بشه</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106144" target="_blank">📅 19:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106143">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9663dc60b7.mp4?token=l4Bl-Dl6E8Jp4670kVCIKxcGLfE9mvaCrqB9UgwYk-SzkNd-6fQcvK4iKY97PRENezFSR-oSZTaaHVDGH891UJ5neCDBIlo2UUVkjfIex1Qn_Kl910NDJvZ9dU-wKqFw4gZRFI3MRMnXhWn-uDUpurhVZksicL4q8mD6IunVOrDb6lhfPUwqfIqgNNi--QMHgfvc9dqxmhknX2FqauRGp4-G34_uPgVITdzTnlCWUOvxUKU-LNzeUocGK4nkvOhZvnENAv0L417gTqVEvU5mxXZ0HowLyjm7TcC4AWu-Vox_hLyyNnGWVdk9Im5ULGsoRObPy18oXSTXyGjRhJXJvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9663dc60b7.mp4?token=l4Bl-Dl6E8Jp4670kVCIKxcGLfE9mvaCrqB9UgwYk-SzkNd-6fQcvK4iKY97PRENezFSR-oSZTaaHVDGH891UJ5neCDBIlo2UUVkjfIex1Qn_Kl910NDJvZ9dU-wKqFw4gZRFI3MRMnXhWn-uDUpurhVZksicL4q8mD6IunVOrDb6lhfPUwqfIqgNNi--QMHgfvc9dqxmhknX2FqauRGp4-G34_uPgVITdzTnlCWUOvxUKU-LNzeUocGK4nkvOhZvnENAv0L417gTqVEvU5mxXZ0HowLyjm7TcC4AWu-Vox_hLyyNnGWVdk9Im5ULGsoRObPy18oXSTXyGjRhJXJvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعار جدید استقلالی‌ها: جامو بدید، حق ماست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106143" target="_blank">📅 19:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106142">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa632d35c.mp4?token=NB641B1Ni_nj6qvKS5FbOMCHsBUUI9dDvKabeFOVIQE9oLnvi-7_FyD0bn8Lh1JOWHZryqf5890Hcu7ieBbuGqfRvi5sZYagu4JtOABFd_dLcSU7O5kABjk5JYRXB0rsh4By8XzMTYHvZEuJ7dqEZMIWUSFjCYKRYOIK1dtfipk_ZvgCszZd82DC5JIpg8JofKDrpKmuEc-PmBncoUDc7XLeQn0GZVpwZ6rodo461fXvJkpQ1TAinTzJhYQa3nrO07ORgzzznTXAcaJ9CZrs-wFYYH0KaYrO0Xr7s8iIBRqtZBnmE25ILce9e1J3Yy7NmOlkaq9JYVBloWtfOO-iHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa632d35c.mp4?token=NB641B1Ni_nj6qvKS5FbOMCHsBUUI9dDvKabeFOVIQE9oLnvi-7_FyD0bn8Lh1JOWHZryqf5890Hcu7ieBbuGqfRvi5sZYagu4JtOABFd_dLcSU7O5kABjk5JYRXB0rsh4By8XzMTYHvZEuJ7dqEZMIWUSFjCYKRYOIK1dtfipk_ZvgCszZd82DC5JIpg8JofKDrpKmuEc-PmBncoUDc7XLeQn0GZVpwZ6rodo461fXvJkpQ1TAinTzJhYQa3nrO07ORgzzznTXAcaJ9CZrs-wFYYH0KaYrO0Xr7s8iIBRqtZBnmE25ILce9e1J3Yy7NmOlkaq9JYVBloWtfOO-iHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
🇮🇷
صالح حردانی با حضور در ورزشگاه، دیدار استقلال و پیکان را از نزدیک تماشا می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106142" target="_blank">📅 19:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106141">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d99249b1.mp4?token=tALHncvG7OYncRKdjW-KrmuU48TaOW-lbKGwlEvKTW0E3VrWJmLbDojwHybFtQ9O4p11yLa07J5rhoAIK-c_V3S8X_cvOkVIGFovzAJmKhUftQEBIfIY5acs9T1jDkKsdzY7irAUWSjbnyHsRfRaBB7SUDeg7HIyXF7zv79XdaLVu10noKxB0Js2r6RcN3VP4iCOSoqkJ9rg9V0AHPsx5OuX2af7IBGLjTNgwEjvGzBrwnw-N2xxZN9zIkd6zxpTV8hssFts1yyW_sLERwDVAqKFnHCYVaJGWxXLst7IZRO7wEULvV2nHKs0vGc62ymB4SiAjEVwHNXqXrBgfM1EWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d99249b1.mp4?token=tALHncvG7OYncRKdjW-KrmuU48TaOW-lbKGwlEvKTW0E3VrWJmLbDojwHybFtQ9O4p11yLa07J5rhoAIK-c_V3S8X_cvOkVIGFovzAJmKhUftQEBIfIY5acs9T1jDkKsdzY7irAUWSjbnyHsRfRaBB7SUDeg7HIyXF7zv79XdaLVu10noKxB0Js2r6RcN3VP4iCOSoqkJ9rg9V0AHPsx5OuX2af7IBGLjTNgwEjvGzBrwnw-N2xxZN9zIkd6zxpTV8hssFts1yyW_sLERwDVAqKFnHCYVaJGWxXLst7IZRO7wEULvV2nHKs0vGc62ymB4SiAjEVwHNXqXrBgfM1EWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
شعار خاص هواداران استقلال: بختیاری، حردانی، می‌ریم برای قهرمانی
؛ این شعار به نوعی درخواست هواداران از سهراب بختیاری‌زاده برای بخشش کاپیتان آبی‌پوشان بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106141" target="_blank">📅 19:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106140">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac6e743e8.mp4?token=ANoGDzcTK0enm7tu43UC5SF_0Au4-RQ_3bkdVBu9TgtXEEnOLsWqb8A3YXe4LMYoZ6u4H4tl6w6QdJjGN4Nx3o9ITmxDMSukqCk0gz0xSwSD-Tje8IyvOu92D4WqpW_eSpmcREogTk_DNXewF5S-DWUVysvIE3MxdeaXy_qzE6lGxsppUZ_QuqQXOFXX7Y4eeUM4FSFbGJgvqqfo279n-yQCoX_JYss7K485OSr4TNyMSsX93cc9QiNECx7QiJfuP9ImWmXQQzQ9FB0W71Bg8BZG2chtgjLfNx6Pv2oBnDM08RBQHjLCK5-kGrj6vPurC-bNsFvoCusgi00ouKsKIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac6e743e8.mp4?token=ANoGDzcTK0enm7tu43UC5SF_0Au4-RQ_3bkdVBu9TgtXEEnOLsWqb8A3YXe4LMYoZ6u4H4tl6w6QdJjGN4Nx3o9ITmxDMSukqCk0gz0xSwSD-Tje8IyvOu92D4WqpW_eSpmcREogTk_DNXewF5S-DWUVysvIE3MxdeaXy_qzE6lGxsppUZ_QuqQXOFXX7Y4eeUM4FSFbGJgvqqfo279n-yQCoX_JYss7K485OSr4TNyMSsX93cc9QiNECx7QiJfuP9ImWmXQQzQ9FB0W71Bg8BZG2chtgjLfNx6Pv2oBnDM08RBQHjLCK5-kGrj6vPurC-bNsFvoCusgi00ouKsKIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
هوادار پرسپولیس: به عشق رضا شکاری آمدم پیکان را تشویق کنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106140" target="_blank">📅 18:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106139">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99d4f3e014.mp4?token=RWSA37pC4l_FnfH3syZ040_dJEdoQvT3ajq2bM3Iq4CdJKfNnOK9OJYmYelEw3Ad76nWdBhGnEvbi6F6ntLM5CHD0onDaCIVcO78H7X9CQt77khq5bCLTxZDK2mGTe0PLSnK7pCaNIeopuhDhGykDnI2uC9quhfpz1sEEbSBAgVY2VN7046Usju99JQPbXY_AHUCH8U3HyGPLBqTRAVuiduUxbwsDleMH7FZi2ZdBlY9pRyXEmpltGUPQBRJv22mFnOdmXnWasfpaORxdhzspaHCrt1hiHwzXHNXsBibL6aorI7KmkGTTOUfJySzggtF77F0Ns32RheO_Aqx-s2Frw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99d4f3e014.mp4?token=RWSA37pC4l_FnfH3syZ040_dJEdoQvT3ajq2bM3Iq4CdJKfNnOK9OJYmYelEw3Ad76nWdBhGnEvbi6F6ntLM5CHD0onDaCIVcO78H7X9CQt77khq5bCLTxZDK2mGTe0PLSnK7pCaNIeopuhDhGykDnI2uC9quhfpz1sEEbSBAgVY2VN7046Usju99JQPbXY_AHUCH8U3HyGPLBqTRAVuiduUxbwsDleMH7FZi2ZdBlY9pRyXEmpltGUPQBRJv22mFnOdmXnWasfpaORxdhzspaHCrt1hiHwzXHNXsBibL6aorI7KmkGTTOUfJySzggtF77F0Ns32RheO_Aqx-s2Frw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
هوادار استقلال: سهراب هم مثل فرهاد بدون باخت قهرمان می‌شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106139" target="_blank">📅 18:48 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
