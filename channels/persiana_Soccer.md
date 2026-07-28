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
<img src="https://cdn4.telesco.pe/file/jCc3YSp78ZdyqfgEwgwUqx3oysH0qgR4aqjTXuxjv9rC_VvuMzlbkvWOG964vD6lBWkWZ_fEoADPwcj9ke883BDTfjYYHVT9VQWGWUyF6wYfRJ9M9BIHkwVyEkkUCH3O-_4UWsfmgB8_N8132nxEw0llXMc-8fBmvt_NMYcSLUL8rA_1x1UnZC2NLZETScQJ_gC4G9bdLdwW7nB4BR4za8uWd9TSYGCvDGBeTcrW7iCGvdaA4pkdJYQRnPjaY4n66_acKQO69OWRaT5M-MlMJRGL7nbOgoSYU4feJ9lK_3mrMDpIS2EAWCGKOy0Pj1QooCk-aYb5WKHtRnH_FdMMDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 609K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 11:27:23</div>
<hr>

<div class="tg-post" id="msg-26668">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4SczvTLZnQPB--UaMZFUaAuferm5AYK2OkQRDBumtSdPGkOfCrV6duR8U0fKE4f9_qKOFbhrt2umNGtw1ZUZ87jpmyLzjkkpSEkciHdT4AeG6SYP9D2MpHq84LpPWZOJJUjqZToyQY8g-MzpXaGc2XYURm2RV1_AwMWbBK-ckF1sAOImVj-JBT_3YC10bH0BqUxcEUs3_sdSXgqOL62Wm0KohkMunxFFhX5GLyVWlv8IniBQkLHZ2ZI-J0A6lbYmkuK8AdcqXQOMMY5O2_YnXa21atjrkxIWYXBehgjCfQT0lt8dqXUwvLP72HINb6aD342txNSFjNUDcF1iA6T6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس رونالدو قراره وارد دنیای سریال‌ها بشه!
طبق‌گزارش‌ها رونالدو توی‌سریال‌فوتبالی Day 1s که با همکاری متیو وان، کارگردان فیلم‌های Kingsman ساخته میشه حضور داره. جالب‌تر اینکه رونالدو فقط بازیگر این‌پروژه نیست؛ خودش یکی از تهیه‌کننده‌های سریال هم هست و در کنار دیمین لوئیس، تیری آنری و رپر معروف Dave ایفای نقش می‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/persiana_Soccer/26668" target="_blank">📅 11:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26667">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1z5Sz391KUDJ--Opal7FfC_6HUB5enBYnzmVi-_o6GAbnuO7-_3x0ZErdDco00SaWf1861lDG0vr-QzbT9h3GKXFyMSzHPRCiD-xenip88L0lH5rBvwihUoIRvpY3PGOFr3sqJPsxx5jNgUWvVMRxHvDAIt-ckdsqtkHvVprorcEg5ZbEQdUux65HTUroZBlDlDdm-RsZLnEPJeRHfHRTHMwNRU4xny_MD9plI7QGUKYpZf16Ryti2ARPFG0jVA2sw0Lneafn8TAzc16WSH4zi3Q0WErewItJNK52OKBf2hxCquJU6t5zVu5QuojiYQ9cz7wvcK5DWt63uelXAXqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/26667" target="_blank">📅 11:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26666">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKmKYSihFxcb5BcRdtx6UwtoLWV2FczP5P9iuHA-erVAbtK5_MDlSUlcjCjLvSLMrY6wTGQlQqxy2ZPzfi5_eH8ULmwA8Higwa1GTekGBhix80AVCrYU4VZG8IoIIIF1FHtjPGf2UIIgZ1QFj6ilYXylHhWoH7inLeRpPJPiZ1pUR9Gm8brCmcWIO5aDDTJhjL6Pn1R8meFpDDE7trWWGBACM6Nik--Hr7UkHGNHXEScBEDeTyIhAxion5W4Q2Km1lpFPhC33HaHu3r6KnMXqf_w3BEjlGBjHxFtIWpFtSEDqafup5nDDE_E3I2rlFms7fb56ycMz5kY9bQupNQl2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/26666" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26665">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWouwpLlvUekbUK4KDUPuZ6-YdX0WylQV288me3TktQW_8GHy5K_S_Bzo1HSyTghcYtYqRba-0bSfv1UVEHPrU2OirjqlQTroueqpmoKDomJnEep3Y-U7YKxhEEvt0QugR1-ycIdwdCeESwc-PwwZjRNxDk_KKpTHKuqxY9TdJ_wyYsU0wvoOFS7wXpYeuzX3vPLF8BJEXcX-kzEISCnIoyUqYQ4WPIrUKnDhFxswGKIjzkqDouxBhysdjV664_dsvgvj3ycXQyOyQxkIMS7R20_s-IqsvOtSga7uQIDHRVq-gc9tFO99sMyEkmY3vas4dcKKH7Z_oEyPmS1FfQd7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/26665" target="_blank">📅 10:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26664">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHbJGP557MJn6kXmshVxbkwpuA--j2UkdKrvtyE30uQxZG_VW71mElKGgQdjlUbZXPVzMUJ2Yj_J8daiAv6VssJCIoPSAJFRWQzsXl2-BJlBVHx4K2l2EgCTjFsgwpOXkK8D9qmqw37WZVIsDhEuCg1YEk4VizdmC_bgMTtDmFt-Nek0wXygf3tMbxDqYc8xmb7ho402WrfPgj2MXcL0Bw7Szyb-Jv6tjILYMXfCgMVENfj3qWdLqrpFJK1hQgtSumQOplKK2D7_aPzxt68cktxXLkNncogeCmYV9FyC7_aWIWy2IhTrfa_Tpol32boexYevOvanYtio1GJpLXFJNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام رومانو؛ پائولو مالدینی اسطوره دوست داستنی باشگاه آث‌میلان از مدیرفنی تیم ملی ایتالیا استعفا داد! گویا قراره از بین مانچینی و کونته یکی بیاد بشه سرمربی و مالدینی باهاشون مشکل داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/26664" target="_blank">📅 10:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26663">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b74f72d96e.mp4?token=m2B3rK7vPnaR7Z3Gq_TCZK0jeVSBYcRmxALBxJt8VbMjO1_eFkG99whsJkxoWEMkUobUogLgKFopA0PHoxzTffXfdop6eL86UXa_2TV9kbGNikVM8BC_A7zxnRXdnMpdxVE_uhJfU5-EIZnBLeLHdlGVADGfWMCTSS-xgcG0xXulXOyIPAp-xokIcGgx6ish8Zo5IAAuFifTOYwt2koflkBh_8X0upf8B59m1xWq3qdhlV-i0tkmFjDR-0ZIV3NfU553nN3tR-JoQrAtBjz3W444eJ407pxikyiTtapLgj7oHz2JGCA4We8bgPjTJX9Y8KI1md9abyLl1KdCyi6pT6p-uAq44q272NCW-imKHUy9WW9EN_Hxb17h6fLrFTofDCJ82ZJkHL8TXwL6w8v2zZvGBkiNvtdDHm5yH5_HLRP_DG1xWuWKnUor3hqn9oSlW1oIL_MVNbUO4SkfnA3_-msIESB8WHb9gY4UYebzsvIht3355znR5TkxW7lX34x2g4MxgWnnfJwxF84FLU2QdF12uThnTX6xTvO8amycsYo87l7-hisSaan5pic7Y6si0Ws0Fnd6HZVJeOMvcCu4s0qMMda69z8MiJlcsqPE4i853p_5jXYA57T9XsjiIqx_NQ-rhqn76xwPIyKQBre79wgQqAjVFaFECk5bOCjJFuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b74f72d96e.mp4?token=m2B3rK7vPnaR7Z3Gq_TCZK0jeVSBYcRmxALBxJt8VbMjO1_eFkG99whsJkxoWEMkUobUogLgKFopA0PHoxzTffXfdop6eL86UXa_2TV9kbGNikVM8BC_A7zxnRXdnMpdxVE_uhJfU5-EIZnBLeLHdlGVADGfWMCTSS-xgcG0xXulXOyIPAp-xokIcGgx6ish8Zo5IAAuFifTOYwt2koflkBh_8X0upf8B59m1xWq3qdhlV-i0tkmFjDR-0ZIV3NfU553nN3tR-JoQrAtBjz3W444eJ407pxikyiTtapLgj7oHz2JGCA4We8bgPjTJX9Y8KI1md9abyLl1KdCyi6pT6p-uAq44q272NCW-imKHUy9WW9EN_Hxb17h6fLrFTofDCJ82ZJkHL8TXwL6w8v2zZvGBkiNvtdDHm5yH5_HLRP_DG1xWuWKnUor3hqn9oSlW1oIL_MVNbUO4SkfnA3_-msIESB8WHb9gY4UYebzsvIht3355znR5TkxW7lX34x2g4MxgWnnfJwxF84FLU2QdF12uThnTX6xTvO8amycsYo87l7-hisSaan5pic7Y6si0Ws0Fnd6HZVJeOMvcCu4s0qMMda69z8MiJlcsqPE4i853p_5jXYA57T9XsjiIqx_NQ-rhqn76xwPIyKQBre79wgQqAjVFaFECk5bOCjJFuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/26663" target="_blank">📅 10:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26662">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6oOFR8yV_T_PQMM0kzLnGjOuwFK8opU9d_C0DBhEzeLnmDF8tQIkg01nOPTwYLT3AkIZ1YUQpvj1Qr6ErkW9dHa16REiDpHnYHp6bI24XTPvmTBwn3REYmHqUoBncuRO93Ojt2lBDe6YfRdHvdXafJwzNFGpDUFk3sizQZd1BhMIpEr2ErHkopmxpiMjKFeP59w45GQ8ckCuxL2WH8OaZAFsqJa9zZfIhTP6ysyXkeQ9MxozLR5c-JaLq0WnE_qVQsUS364BLEoz3l8QqechHYzjJpDTmSYLTztijhcMUvWIDxGVTCQYkRCeGQWVlwCr19Zn5Cg3lVYu_Do0H1cAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
یان دیومانده؛ از دزدی سیب‌زمینی تا تحقق وعده خواهر مرحوم و پیوستن به رئال مادرید.
❌
یان‌دیومانده‌وینگر ۱۹ ساله‌‌ساحل‌عاج پس از ثبت ۱۳گل و ۹پاس‌گل در ۳۶ بازی برای تیم لایپزیگ، راهی رئال مادرید شد. او در دوران کودکی شرایط سختی را پشت سر گذاشت و برای رفع…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/26662" target="_blank">📅 09:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26661">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgnDPLr0n5pjHlsTEH1ZL9EAELHbaXYFtGRGzD5GDNFBbg-UQ3TJ5gmVvkppbrbAwDUMUEq7c-7Xai7t1EKhkb8E_4L887U9naSiN3EKqL2xdac8GhSXvnhweti9xUQkoDTHDyIFa_EMbpnmG7o-XdQlLyjV6AlVoeZXIpkQ5T0h-Pbx-azgFS5QWKSALZm5k2U3YlM79bWVUefKvx9O2nfWAQV08_D9dpsqDY7pXC00bmp24tjufBO0ymnafLDEf6thGDukdv8QmbJERKsdtTczDdwroT3xZOXYXqJ3hfYK6tBFKPovf0V8QKo0gIJiTybis6m-q5s7X8RTzZJ82g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/26661" target="_blank">📅 09:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26659">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNznNpa-xE3SbvknZpDbBLdYMa8v1Qn7iQqDGAAhta3E98_tgiXXbQqC5TmXJIMUoFwUEb-BCgYVq1nWxQc6bA1UHtQejeHwieMLVTH0H6F1-AdnCjHvXNFH25Z0u9XW3wrc85TGrZ2p1fG-lC8EpwhaFtJKii7DHWurRZp0686lw3Kvift1Rbo_iEqWgIYCEso87QRACaCojcHveLk2v9fS6FiqFITOhvSodlds2ClkMdZ1pXD2klWLbnhtLhTdHLVAQpfi97_I3TQclmJASzEdGttIDTTTPveI2W8etpT68u9W59r97YrVqldMqJiIOlZgbZ52gYnqO5yOZL25cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/26659" target="_blank">📅 09:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26658">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8feaae9b61.mp4?token=vH3c-Y5qtBisXryZrkX4VuqoV4MA4f0X6atApAUWKE6CyzpfT63mQWxnRDBIXxXGxQRQtDU6FvcelqIYojHvGuVA1f-BXdOud8V19E3YKcWJzsO7PU_WZfajPtMHpg3Y1l2zjROlCtttz3Ej-VKp9vYewFHVeXNtPgoZMG8In2TNadeg__Eg1XtuCU8vLvsKgKj7vxXl-JN43noxq5SM8BsB24RCfk0y5hfn6M-xZGTchytLkpclCRvvsd13fGso1acgi6hQRi23Uw2hwfc1RpQna8FwT10Wxmu68sWEptrPJyvTESvyOu0EN7PLdcBz-NVGXH5Gj0soEGdehR0kvWECXFsd7Eag_q4ITNLwRPs2YuZWQWDbvgJBnXs_h3IrVIsKXMdoWP17TunVDVi-S7nON-5BswEWugkTotcBUIjz-uwRENjczZgj615EHI4o7qzwDiAgq7Mn7kcJOjRqsmUFoUaKk2Mkur41FWyTbq-CiYJ_T3_EC-790c7885baj1eJzTQiTqFa-K628Mw1csmhgZLIHxOOE-JxuMBTcZkPtx6XRkkfDAbqSjfxRg3PgnQreODX1GUdLHVVQ8S-esoHr17tB5CSvH5ChmBZXj95aLeZd1dscwMwNHczcnrAyMtfw3TDusT2-BcwI8FjTDLE9Ix7z0UMPhVgtSqUtIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8feaae9b61.mp4?token=vH3c-Y5qtBisXryZrkX4VuqoV4MA4f0X6atApAUWKE6CyzpfT63mQWxnRDBIXxXGxQRQtDU6FvcelqIYojHvGuVA1f-BXdOud8V19E3YKcWJzsO7PU_WZfajPtMHpg3Y1l2zjROlCtttz3Ej-VKp9vYewFHVeXNtPgoZMG8In2TNadeg__Eg1XtuCU8vLvsKgKj7vxXl-JN43noxq5SM8BsB24RCfk0y5hfn6M-xZGTchytLkpclCRvvsd13fGso1acgi6hQRi23Uw2hwfc1RpQna8FwT10Wxmu68sWEptrPJyvTESvyOu0EN7PLdcBz-NVGXH5Gj0soEGdehR0kvWECXFsd7Eag_q4ITNLwRPs2YuZWQWDbvgJBnXs_h3IrVIsKXMdoWP17TunVDVi-S7nON-5BswEWugkTotcBUIjz-uwRENjczZgj615EHI4o7qzwDiAgq7Mn7kcJOjRqsmUFoUaKk2Mkur41FWyTbq-CiYJ_T3_EC-790c7885baj1eJzTQiTqFa-K628Mw1csmhgZLIHxOOE-JxuMBTcZkPtx6XRkkfDAbqSjfxRg3PgnQreODX1GUdLHVVQ8S-esoHr17tB5CSvH5ChmBZXj95aLeZd1dscwMwNHczcnrAyMtfw3TDusT2-BcwI8FjTDLE9Ix7z0UMPhVgtSqUtIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🇪🇸
دقیقا
20 سال پیش درچنین روزی؛
رود فن نیستلروی ستاره‌تیم‌ملی‌هلند با عقد قراردادی به رئال مادرید پیوست. این سوپرگل دیدنی او رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/26658" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26657">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rER--NWGUX0NRonOBiXegtSYZeJYmZcfrY4hZzlXpspeNyvrC30oNAH7hcBe_jpakmEugofcWAciWV46A5BH1Y5U1gZL_7afT2ciVfYKEl-IdRmxz8PArUt_viT7LnpLVgjo8BpQNLES_HcB7M19m9P_Wk6rm3jcWC9jjnAyvsFZJXYvBocZUVqkX5pRYpGX9VooAgCKrNZQ7E94Al-cXHnRkeKOxTvwfkG6Yw8V4Kb1eSgQsTxz9_cuoT790ipnV6wsT4nFjlexZOu_5y-mvlppXjrpkuDdwXwE5-rwfJSClpTrg_CKj_wesZZBIrWILFbe2ham5tRNMyq7_28WjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛
بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/26657" target="_blank">📅 02:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26656">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPN5tJ_UuyR2BN5AW5sRrR53-JEGDk0hmA82kn585ETeI-acSFR5Ll_PN-wCEyFahdno2CHPEQwlaHvvHrkx7jIvU5Pttu-NAeUrTpTsyDEjgpJoVXOHHKPNubPNbqTpICE31kXePEGSukl-x3VmSyDhtODsDhrBJ65X3qWb5kOCSmOiq9ioAS2-XbUW0PPyVnZhTaQ60M1DaC1kV6unwEOef_rgpMuA6O3Qo5tttVJUTSxXNnf0GhoVAulPDw48lwTwISNrUDa4Wm7FdMnU4f0_iVLaIvF4iVBiotvoLiXjIHwPCj0KUlg7qvNSh1eyA1nuAk-N-Ktx39MQby49jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/26656" target="_blank">📅 01:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26655">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=vtLYzh0ZpADdg5EAfxzb0G6662ABs66BqLoEHAzUr5xdZx6bWvBz7PuOWo-_O5iIKHKRXwg7PRbHwTo7SOQp19giL8TkVYVEr-UiNbDuIOqI6aKaQAsmiYU8M_5FjLDuVRgH2w3OB7kihy3TsmqhpLoD08EmCD1Hi9eFBawPbvBtzQPx-HdWheUyjLE1pOA416xG1yckD5YXZqMZpvjOj0XQA_YVesz0nul-ykC0uJipGkpptfv1nLzyvcbjZZ4uvx-EFSysjAUuf5BviYIwkd0WIldPETAfNXWLLEnN_CSu2QSCtBS4_q7UbLYPDtQEGRCjG-GRTYdu8YtnHrsI4wyjKLF7Nh55Z_TSc3bsXRKTJd7M9l_0N2Bi2JmBCU04-aq15zlplz-ZM7vplBtSU-ofQjS6tT7XSgO85vV3CN5kb5igPqOyhSeqZ6PbsXRZhFAhdzlum-2m51UvnIAHbjaAcMlojUygM5gDojUUO_pEG3wmANhCPrQC1CDDV95F_M64EHQbbZ-V7yDNZWhk6-V076WzpVH5UchrJeVVk_Vw3-KAEgVUgxrfk7s1OAaQuh0-uOeWooEXQvwiYBRFcV5cZpEQZ042nKqZUO6NKCS3d3O9nc0nJw7vu_rdmOoL9TmAfXnisA-JL_bX45DLqfnmWL8PF_PRfaiAyVr6OZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=vtLYzh0ZpADdg5EAfxzb0G6662ABs66BqLoEHAzUr5xdZx6bWvBz7PuOWo-_O5iIKHKRXwg7PRbHwTo7SOQp19giL8TkVYVEr-UiNbDuIOqI6aKaQAsmiYU8M_5FjLDuVRgH2w3OB7kihy3TsmqhpLoD08EmCD1Hi9eFBawPbvBtzQPx-HdWheUyjLE1pOA416xG1yckD5YXZqMZpvjOj0XQA_YVesz0nul-ykC0uJipGkpptfv1nLzyvcbjZZ4uvx-EFSysjAUuf5BviYIwkd0WIldPETAfNXWLLEnN_CSu2QSCtBS4_q7UbLYPDtQEGRCjG-GRTYdu8YtnHrsI4wyjKLF7Nh55Z_TSc3bsXRKTJd7M9l_0N2Bi2JmBCU04-aq15zlplz-ZM7vplBtSU-ofQjS6tT7XSgO85vV3CN5kb5igPqOyhSeqZ6PbsXRZhFAhdzlum-2m51UvnIAHbjaAcMlojUygM5gDojUUO_pEG3wmANhCPrQC1CDDV95F_M64EHQbbZ-V7yDNZWhk6-V076WzpVH5UchrJeVVk_Vw3-KAEgVUgxrfk7s1OAaQuh0-uOeWooEXQvwiYBRFcV5cZpEQZ042nKqZUO6NKCS3d3O9nc0nJw7vu_rdmOoL9TmAfXnisA-JL_bX45DLqfnmWL8PF_PRfaiAyVr6OZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اوایل‌لیگ‌برتر
؛ یه‌باشگاه‌‌ایرانی‌یه‌بازیکن خارجی اورده بود "روزی صد تومن بهش میدادن میگفتن برو سر کوچه فلافل بخور… نوشابه هم نخور!"‌با نوشابه میشد ۱۵۰ صبح‌هم بهش یه بربری میدادن با چای! تو یه بازی گل زد یا تعویض شد، یهو فاک نشون داد بعد اوردنش نود که ماجرا چیه، اینارو تعریف کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/26655" target="_blank">📅 01:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26654">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAbiX5d0oPsJ4e3feuIFIW9otfx3im_aXH6WAi4KF2JxMPL05f2o3pb_zowbGjemDTvdHaZroWmSYvcx7Y505oQ2uk403QPx-D1Vkr1EJTAk6KGmYbicZdF4fy91IzVxfK2vOaVcTcLckjyH_3HTHfIDqaCaq88WjsvKBgvnrohPrPmHZhJ1hSRWsHNmh8_7Z1poTtbdy0B9c23wGFCS24NkXXgM4NH5290zSzjW0l-BwkKEugRLWUvRAPFxSR913ehEvyvFGpLtC4lulbjgZ5DJM6HWtnSBH87gybBR7M2PvW78pKayR0ojs3wmbO9jVIHhK6XWAggeph1Zyiv4lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلورین‌پلتنبرگ: رئال‌مادرید رسما آفرخود را برای تمدیدقرارداد به وینیسیوس جونیور داده. آرسنال هم بلافاصله اولین‌پیشنهادخود رابرای وینیسیوس و رئال مادرید فرستاده. حالا تصمیم نهایی به وینیسیوسه که کدوم باشگاه رو برای ادامه فوتبالش انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/26654" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26653">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4PXTMTVNOJwQ6qqHtbqic6_hQYMmwJv9A6R911Ir8Dsy6diuHzn-kt36DXdBQSrgn-u4h-oPrkzsJwyaV9ObMT9L5PMW9YIqWNVNX93GbPIKyIt4G-iK_i8W__SL22H3XSOAvlvSoCo58v_hEfr7H5arUjGi2lex3dKMK73rSaXxBAmqi7DvVeoYRvtf-CvHWR_lRB9dUu-VWGp802RhcQUzHloXntTcR0N4A51vd4kGLgcIO9gsEwm8A57a7_2yez8mRj9crOjR-0BcEM7xfff9yqPni79aS4IwdrDUtZdZT8LMYkC2D3i9si3rLKDTmcaqPkdWVqnIGnlhfJvMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
حضور کوین یامگا درتمرینات تیم مغرب الفارسی مراکش بدون استفاده از عینک؛ معجزه خدا تکمیل شد. بینایی او صدرصد برگشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/26653" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26652">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F51-CvvEswJRQDLAPfIvZwru75m01zUqA4cx_Jtfy_PfRYwim_ZgMKQ_kvNttDe-7Ep8SdTS9GFJS87PKBmUe8uDCXc2lD6SHmv52T3_YbhcACMa7p4Q0sKI6s5l9koxOT6AjOswC2rR1tuI72Gjbw_GAGEPRNTxRmc3Db6zsED9cATrO-Xzr2V1Aga7pIv_-jQh6gHqo13R2BGx46_slVWfr7fKX9iuFlA-ovAnj0Mb4VEdsnP3B9YkVciqAQ_anpn4XSFI8VaArQ5YZoOrZREV_81sI-or5ekNzuKxTzPC9TB74MycqTkUw6akYzopRGbcZe2c8uW8dMNdMokeyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/26652" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26651">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCIVAxoeTRRCl6ybBc5SDr_Pwoz5qK58keffpq6KvmW6xyc7oD71sru-gpDLIIS-qodNFpdNZ5M444F6e11bA7oOTfIa8Sl8xnQSYEPksr51lCA22nlA97O8htYvpc3PkRUKjkb12e1lgjZXcTZuTwSKdA0tK_W1QI6DGKsnChrFR7LE8yLCs8orTwoq5quwbHA1t9zzk7DtbUU5fzwxgGo821KRa1yyy6TY1njuQ4VZwSoODuNx01T658pmtCHcQxvckjjIjIkTdEQoMVqITgyQXwrwWMBOm4Z8iDYnlK5YPC_CD2lbVUrvFwBO_vxhaei5evVaZpjJVyFnC0bVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/26651" target="_blank">📅 00:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26650">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/185f669e03.mp4?token=GSEDUwNeI66DZeLDgTcAMJ6oLCDvROQcMmvO9beRcLPwInOypR7Oo-ahtKuUMyYvvtCJ1c-heyD45iDwokKMXvkzDgWplNOUpa8rCeyvzKq-q8_65u2FW9wZCo6hh17m1BUW__q7evUHwkAjifiHlUNyxhbhBNKLLgZ2PTK6nzLQWZSa9RVkty0xqWRTUNBld95UMoo6WO9nSjpqhi4iLby2geyUFNt2fqsUoOZjbZgIZGe3iC2CepwnlMnmuOiZ-q0rghbJyvKcRI79HP4emS9iyhiJEy9xKvrwYGvQSZmotU5zQZv0dwxFq3xeVGap0NE2Mlg96P_7hSo5ipACGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/185f669e03.mp4?token=GSEDUwNeI66DZeLDgTcAMJ6oLCDvROQcMmvO9beRcLPwInOypR7Oo-ahtKuUMyYvvtCJ1c-heyD45iDwokKMXvkzDgWplNOUpa8rCeyvzKq-q8_65u2FW9wZCo6hh17m1BUW__q7evUHwkAjifiHlUNyxhbhBNKLLgZ2PTK6nzLQWZSa9RVkty0xqWRTUNBld95UMoo6WO9nSjpqhi4iLby2geyUFNt2fqsUoOZjbZgIZGe3iC2CepwnlMnmuOiZ-q0rghbJyvKcRI79HP4emS9iyhiJEy9xKvrwYGvQSZmotU5zQZv0dwxFq3xeVGap0NE2Mlg96P_7hSo5ipACGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب بلینگهام از زمان‌ بعداز پیوستن به رئال مادرید: کارلو آنجلوتی گفت فکر کنم بلینگامِ اشتباهی رو خریدیم. باید برادرش رو می‌آوردیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/26650" target="_blank">📅 00:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26649">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRmbnMUF8DPMWoTkrf76s3vLRImJehQp4l9pRQIpDkpwxIsv_VWLBs_yL5uY9Bb76JtstDslRq25BX5s-Z6lq4WLQrCWne9mN56XQo5jehRxW4xsPeZqis3cxVOt30T1cRUuku0edBGhT3bu4TKvvb4y8DV2uxym5kn8x0W2RE68c7YYfe8djDZ_XTQ5x91Qsidgqoun6eZg9vQAqXaAcJVAMyAEXGQ4GSFB3nB4IcIuQS-tTRkePy8ltT2kNiK2cCIOYbpSxDU2mLm05bxwr4qOExOAaw4PSzzeLzlJGypnUbvj0We1Y_3uPnfr0yZl74dWbBMq3ZZvUXGXlSwqyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛ تمام خبرنگاران معتبر خبر از عقد قرارداد رودری با رئال در آینده بسیار نزدیک میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/26649" target="_blank">📅 00:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26648">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJtij5Os5MmJHbgg7X0rElfPZGpLhEkRREFKrCbE5mG0wzMdB0NjWfNM7uUF0DtY-x1TWiZKbuImpHfHyT_eqE13LPQVd78FgsSMxaXariL7_J37ftNEKX5sOdzvEb0M4z-nWkhsGo8PRKuSKN3EWgW2KVNDPPWUvWJR75z8AowP7nFCwPPH566fXLmfob1CrDqNloEu0RTm3CiTIZSZzDcyQZShoMwD7-0uCaJVWZBBWE991BkmZVmfeyFyYrW61KgEXqLwM6f5tdna8a3AiR0cLqC6rbxtQDRWLDikjV5wG3MM18oBGhe7vksLlE9mN2vEfKd3YJ1OcqIdrGMV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/26648" target="_blank">📅 00:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26647">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAp9dgw9ADY1kPODgp_SS8PHLUYQbdqlNjEnMI0-a8DaLQJg2nUcHOYLadtrEKaTfGTcRgLMoQG_yA5UX0pBx9flLgLqelRGI5qqb7TboyqwCdV-PVeSnG97NIZ-DssPu3w0ByfCvOG219UFAEol4hPKg-8WsoiGNXipLfNSzT2XmDZMAicJiDH6nkZsXxbT2G60U_LYxiEvYqQigyYarVDHp29hCthJCdBG3WIdKkxbaraAxDwZ-yE_uI8WUGiNNsH0bnfq6pFqo6YPadyRS4XGqZCuF6n-JQMmiJdGtMgUBLu6ThcOo2uUREHf5O_FIB7YEcOUN07k_kAnKbzyKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/26647" target="_blank">📅 23:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26645">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=SHfSWz2DXuC1JwXZXBB8U271-sj4Zt1_6QXNcaQWqJZ0WNMS9xEwjDLwcC-FnzgoWGWAjrexrJcj9tsDSOvrnh8t7D5qwT6QFSjyY7J6ZoYBUIRp6BDY_HzlK0KbI0_fh6igHTc8GsFkyZBOMrm-lGI6Ms4dnXpFGhiMFr6FP8itF3XzN8iYxzWkyrTX-EiDDkNmPGBFajEGRRH7mUBrL4egopZXcPsfz9O4VKLxYL8DdvzqpEKV8PQwjuPHaW7_uvwWtrueHhFS4hFM0gwHMMW5V1yyJn-cYNH6Rfpu85GYEtF3Nzy58EazCGUlza6Lk-AdYDSby-dzdSlJ6Obs8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=SHfSWz2DXuC1JwXZXBB8U271-sj4Zt1_6QXNcaQWqJZ0WNMS9xEwjDLwcC-FnzgoWGWAjrexrJcj9tsDSOvrnh8t7D5qwT6QFSjyY7J6ZoYBUIRp6BDY_HzlK0KbI0_fh6igHTc8GsFkyZBOMrm-lGI6Ms4dnXpFGhiMFr6FP8itF3XzN8iYxzWkyrTX-EiDDkNmPGBFajEGRRH7mUBrL4egopZXcPsfz9O4VKLxYL8DdvzqpEKV8PQwjuPHaW7_uvwWtrueHhFS4hFM0gwHMMW5V1yyJn-cYNH6Rfpu85GYEtF3Nzy58EazCGUlza6Lk-AdYDSby-dzdSlJ6Obs8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26645" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26644">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_KyClrn_Wej310DtgBg7bZAjOQKpLAk_DK2ySA_EbA3E0HRUPQHT1YPwNAefK7AHAW6kSMnonMP0Wiz9xod3-MJldtn6LLTuJs3N30CHxABKVczBaeLKWgfpWhlOz63TkubaddItHB1IoF5OWGo-mdgnTiEXAqqqfKa4lIxNbT4mMK56tfbgkOxTK2qKJc20-pcD8ZNgb0wYt-Mlzks5z2yp4Cc4rcx0_MCNLZa2n4n5gtf8TiCWpGYNoZS4pEj1qjQaCWlPsJgMvkHFOxJ3WFFI1O6teGk2wFG6RMCF4Mqq-ohe4GLDYKR1a09C9X_C1WapO7Gt1iGDOmZpc1UPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26644" target="_blank">📅 23:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26643">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgJMqdMbuaW-x9ui-rKKWuBBk593yX71wXNn9MtDX34g6SNBrmDAzOI021smqjFGbnjjvWID3TSQ-CnmNoplj-F4FmE_ubYMI3J95LGgMj3loRjB1l0enuvjGYPfDAqbsWAdF8_-nM8ylfZiF4hVczHwKJMQddLWbgoQvGeslmy0dvK3zNxLyG80U-ilPO4V6lp-7EWLoVvHMnKTIaJ0AOMmWwttLBDQcpi6i9f5nfBRkpvHkV-4piLpGfNynDboEC2sPPgjTSI0Mv6dGpnjHO-DPs2ASiquS7ZTjMIQTwdnQMAIOjGEncGva-jY2tW3642rmY0ixeR3vt1A72RBFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یکی از مدیران باشگاه استقلال درباره آسانی:
🔵
با توجه به اینکه فسخ قرارداد آسانی در سازمان لیگ و فدراسیون‌فوتبال به‌ثبت نرسیده و باشگاه هم اسم آسانی را ازلیست‌تیم‌خارج نکرده‌ونیازی به ثبت دوباره (new registration) ندارد بالغو فسخش و توافق نهایی، طرفین به قرارداد…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26643" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26642">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRxZYymahxCnNUXSNaPcZNGVYdmutff1R_xkaO2fmUBVVTTuJX4wX-04wSYk2slJD0q12Cr6Lu545g0MMDGcouaJQdtLytIjl9vB33ZycY4g8jT2gSjVLgoAAnjX05Fm4SfXrQfYYxMsxdYpYH4rBIrq65bFDouBB62fF7WSkRNrGw0uRa2L5okWNdpHR9dYVBHr7kXVsYeD-ehR6oxOSfk5bJUFuhT43HBWxE2SSC8FV3hl6qSgkA-v_CIySIltG6KlmtyqBFdCMsxn-PIb7Y6rmhlA11Ka53P_PyRX0Z8nzMfgjwiOIW01QIqJDnYpzu004cxOJNWTjk4wgzgVmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرنسس لئونور شاهزاده اسپانیا امروز درحال شنا کردند که ناگهان با شش تا پسر شکار شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26642" target="_blank">📅 23:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26641">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpM4_oONkl7285N16_CwukXXTawHwUu9XpOVrht_2JgOKhnEX2mH7mt9iytTZXocaF0NmxsCCkOvse3Mp3NlavHT2cxp-2_zEeR6rv1Jej7XL_rjxLzngGLFXK5nbhljIBkvEwY3WbNrk_qzkLC6Y1CEpPz0eEMtJvYzy7oEUBcon2Dw6UGeTMTkJDcL4ZTtLxQ0KNDxVTxifWfnfqnOneQ9k1jARMv5et47cpBZNoCzpXfMCHd5S2aH1i5q7UQZfpnyWTHVwi0QwRfqskXhboAbozXvqxSFF05iJfeKxhyfUD16WD86_65OWabLpzbolrMQu1Jy_uJRIbejTi4ULA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26641" target="_blank">📅 22:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26640">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bh8ZrS03wW_OGY21Q6A_i_wfQlY-XMPwYyx4vJhAblzAg1QpnYJWErPrgfMjnfQfB3nwCxnAYqRtMHHT_uX9fvoJiMf1aDzz6CFQ8ARNupuM_xM_Dhy6MkWpJt5c6kUNwYlsaCHcpUTshz6tm-9Hhc9vVq2qEgubOxYcSKUVClNm7jlZXRzeqNRWTjQ0kPiu7MeZxUSIWlxNb-hv0KF2K3SdTcHqKzv0XIPvdjaOOvxDxfcpgh8UOPxNjKpiiFQxEqhtSNSPpSRIivNIDtBgbCVol5vVy_czqBwR1dvv3IOUCUeNlLg3NinRpyEWtwBrZhezlhzMutzDvqH8ZUrUuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#نقل‌وانتقالات|جیمز ترافورد دروازه‌بان 22 ساله انگلیسی برنلی باقراردادی‌بلندمدت به منچستر سیتی پیوست. احتمال جدایی ادرسون بالا گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26640" target="_blank">📅 22:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26639">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWG7zQne2TXr6K8oPo3GgxVmQWTgIPKaO5hP1Xf2utPRL7FT6PMz8er-iroLvgQeQWS0dkt4XvBCHXCBarDrEGfWyijJFxvupS4RlRQOvJQxHKX6BZMdci7uKPkQFzb8nxRGCq8-nA-FxGMZRlbX8DUUsDydIYoKFLQg4vIGPbbo3shDqUpMDtjOE53BwOcwcmIfx-MUf_To4WuiwWk8_nA_dCnVEItgtx87iBdsls-xTgXebvqdSh0uGqtjuZ8SL8NdyPCW7H-jn9e_Kddfd56veyRwbmtaUsHJUUCxJRoBJ4qj0IhJoTQZqxF29LFbc-6GFlHfUZefiudmVABrYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26639" target="_blank">📅 22:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26638">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWTjKH0ews5z3dQj7QMfhvoQP9Vf9BCoO3785wgvWzG0i2ggTGDBQ1GgGAps4kun1l_8uiEcDyQWKdZIMEEdoLzIJS1JMwLajEorKUaPG38L_-JNIa8Vc_4ArIQfOc5KBD0Be3XTo5_HdUwWuTB5KAGFL0zP1Q9NbuAOaGX03TvUeytXr5ua7ObKKWycU7gvtG-vgSRbR58X-QdyMn3RQZhimTjQUQ8exqjJtwM5u9DwUU-KUeaqGLa33m-t6J8gGXwYZinwsxmwepsI_H5FHGecWJRdUocAAgLkQkhzVDk3Rg06isjep_eMV67HOFh07JKvONFDyHh1XdrDvKopmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26638" target="_blank">📅 21:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26637">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMIFOfH4Ummqqud_YBRfq0AiFDlGbA7RzWqA2MxFlK-5jDie6gokfT3VgxxLWFGyo-Hu3NZym_co3yKzoSEJa0ETLeAuEVThhCh25NpkYR85No9-v_-ycjQsmfP253qcJEtx4ytcgX9Yt-k9bfO1yM-Q09OyOH5bi7QZg2H8g0YEvMQm9Jh5dyOPO26990RzT9IGXfhokbC7rEiyZwLzkamh5HiMUr3pfcDvZxpuC6t29yJtfMbwTVLEHz9g3WZxUP9GcTeIEMWpavkOYTXUscTBmFJ8tahWrWHiYFyTyntQ0eqmIqfza2f-rMv-UE9aArM4TrCfIf_7V1tu_dQVVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی: باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26637" target="_blank">📅 21:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26636">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhrSL4OT7akFezOOV20GpJWTOFYBa3Lsrd1PrtOOYNqTmqvksoxcreEoUPLp81lFkesoQnZiLxIpKyhv01unkIldYtRFIYi_CreErjDVgetEARo94OVb5QD2geOxAkBumhYxA7Gl-53_9xFNoDlYocnk0EJPznETJn-PtnKqXBZqxCxPJExXzNJ9XdN2E3BaWK_uQkzHWlwd-4MMGT44WLVVe2fMwdy6mUyP4UfONuNEPeX3uKrwCeiAq_oUVdaTBAaefzfzBtSOiKyMMkpCmxEg20Nym4QgH2QASvpvcMltuedn4p2mkee0WTjN2X9tRn1ngCWtC4yrEjRr6BIdyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26636" target="_blank">📅 21:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26635">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_ku-_dxBuhLq5DvlllfNNeARH_2Ar_-CLfZnL97Cg5GZlRiL_fE7-m-yuVe_q6c6_5lT_9N2yx8x8WfYJCfRI4MF18scL3qu67wLKoRQ_W0cNvbfwsS7cJel7NjdeGKQb9ihTEQCIZxuXByTsaup5gjqfoDyW32DzAaPv1vFiqNlm0HhwFp7FHzrBI_ZCwWFKeozFXAcCSCeJeShGgODFA7jmXUNSILioBD3pCMr6JBPls63JBseMMzSVnI6F4pzm_jf14_EJpjne_7-l3X-CFMwX_S85VgSwXqk9yZZPaJIXdX0oa_MfgpcleydbNh4NHmP2L1oSIaP_QJTYY-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26635" target="_blank">📅 20:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26634">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUvVEWFuLH8InWb6Nk7Dg2xLyqqBDz--E3jYsLff1HfDtilUdne6QfG6u2eNe0MvIYnVN0AsCOPDUQuPH_U31Tov8EZCbRRBA4nZ_jwI5d6B1y7y5AV4vST_HDNPatzTR_iya-cOlOEe1Y4tORUZKTLuZ1wDff8ck7cQu7QVY4A3jehfCVw0BjmUsQZaMCWImyXaLEQK_vCLdQqX9cQ0M9Va-jjKxENYws5day0rtGEAFzrtXsckq2FxaocMJG6ln52_qoEFiL-CIHTPxpjxItmVi8fiLjgh1WE9KyHlfeYWK6KQ3-Va7VBtU3w0hGS9FGopSPI9rlltqzmyrZUGOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه اتلتیکو دالاس که درسطح 2 آمریکاس و سال 2024 تاسیس‌شدامروز به عنوان نخستین قرار داد تاریخ‌باشگاهشون با چیچاریتوی مهاجم ۳۸ ساله سابق منچستر یونایتد و رئال مادرید امضا کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26634" target="_blank">📅 20:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26633">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ae0WFtqXEQH8ATlgGVZTyYg8kRXyVg5paG46yY98OBTM_EHUq8RILux8Ax5YlEqKzAREJjMeOYeUgjt4JL0A8FaTL462X3DxGSksW9TZvvJQlwdbkLyV1gvld7TLVqM699tSWDhXqcVXqty95LN4id0wfbaNknecUBqutuC92IvCpWq5IeGENJjR5-fG9vSijPhkrqA9bAe7KDyDvrJ4ECwfHYFD7mqp6zS7vK49eBav7jJ28AH54WK0fgGEsS5zIuTZqeCIgIVUnh2oXg2DT9Nl8cGXCgBFq8VT-YW_a137x5FxQDCk4bluc3SxLw1SvpTy61QN_PArXO_TsGXiBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد کرمی دهن سرویس بلاگر محبوب ایلامی تواین‌وضعیت‌که‌میبینید داره شیر آلات تبلیغ میکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26633" target="_blank">📅 20:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26632">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPyRZufGAQ44--VbUdq4OPOpAfxOpU6pdClqMFvGTcaotLH3zZSiPOs6BmCKwMdffoBHItbsFASvoB0k9Z9BbkxPbkrX5TUYl_uU_K8tMLW0bbPVICEmZZIcyvIrpPOu8h9YOayJI9wy-yJdQkB21mNdWZonY30xWynBq7qfCqkHy8JQaHr0CYHOpJYBCmjDAbQWQXNPYXKv9jsDjC7Dyt8eGOJHgzWHfoAlQdsb0keWPj6zh5xTeeKwCGHEK2W3xLBcuYsF5JnQHhG6gDevC109gJ-LLvd4_zKkoYKAbf-OyQFlIYRN6izlA3ELIXQAHWH_jXJhTdIys2Dkcf57iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ روزبه چشمی کاپیتان33ساله استقلال ظرف فردا یا نهایتا پس فردا با حضور در ساختمان باشگاه استقلال قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26632" target="_blank">📅 19:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26631">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-GLPzv8_gz6rSNYMkOmLRZWtsKCR-xtdvVitMldx4XUCE20eCGLVXsSysqBXwKY7QW2fawOw0xW6bGuc5S9kpWgiJ98dKI9pXm7yDsPftDVhT9XzXVqnCKXyuO7YPNKnBjLOrfKa7RjTBjK8i5q8U6tZvbQpwKRVtXYboVldb3a9dXPgpM3WsHxg773XfFitCC8GBtF6Vzjwb8Zm1gX_etvGDjVt4mOcf7VoIS3uFpI1UN8MxehnqoutUZcKXquPDTCgf5Qr9sWAB5TBWbZ06ltXwk_wx-VhhhIMt1UZwTjtCAzvPoOuj5qJmWuaQYhMkGlvgITwHdbQAAWGoYv8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ:
ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26631" target="_blank">📅 19:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26630">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDlXIfJ9gTGYPMWtironeBJwKWP3kCkybBaO359uOPT0VJ8uIWVTR1alrzlZz2HJ2a4Bsli778K5YfizIk6-ziQbX30JKpcoRiT2nJqQ6A74i2s9zctSg_zT6LD3gCyh5hv2xBEahoZZWL9duE7SMokBXCmmN9J0PLh_LQjnXMlD9hdN56FQIiezRR4S1cvqhjY4MhVSzuiVvXH24-NarzoaD_2HeosWhJqkE3_h9JGEGwJM7WSKcqxOUFf_hVx8qnjrBeGXcblOrsAaCacpEAWijEpQaRFkWr2pRtdh-mmWVJvQ-GEAmSd_0w0Oe-9R9Q67sy9cwmuren2lHKKMbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه چوروم اسپور برای جذب مامه تیام 150 هزار دلار به به باشگاه‌ایوپ‌اسپور پرداخت کرده بود و 750 هزاردلارهم به تیام برای 1.5 فصل؛ روی هم جذب این ستاره زیر یک میلیون دلار هزینه داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26630" target="_blank">📅 19:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26629">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAIdXMpUjL6n7tNmo4v8P0gGeNQDDOcLWzB1U_OSQHfvBlMTznQEdEQwAJU4VZdsJdid3fCYHbSyaFPh6j79f7jgomYmD8IooibckuT5QAbbIO323LpPI5KfzBzR1aFCoLJ9LfBp2dMKptcasQIGoPSTnC0ZtiIoPIC5sqJyCFPkq2Hs82nmuZQ6GSMZJWQAiYO4Txyi-LcZkuKyqCsbYQ_zIyqzK-nxO5rewECz72y2XOcaTKFvspoWB3b4USHYtVOlD0IQGAySYlYk9dETMrZEIDDslS1kOo70NMevm6g3emt_fcVM8Y6s0c1upIJg3MaK6X5VU1SWlg2BHm0gUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26629" target="_blank">📅 18:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26628">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLM9S5hfFn4kwgZX8q-HqfunCNipfJTmcJfglabm6GD1fBMqXxTrOUXJDrIZajM-EosJ9rMYWN84VTHQIOJbSTZIqI7zwsVdx8v2i5bsZ90_E1r5wl6p9JdhFHMyArVaPeEmO3dHBUaCVzu4rl_IewxKYxFn6jNpyZ6lvBk3E4jDaGLmJ5hdG-_Np5V1_rgQjp7OB2mzBoGcyB5j9k913I1xBGJ9J4-krXUd1SuHb3m8MuSDdcxWa4VDbmlvrmIbZiPl4Y-ugDfztie2vM4rkjPCde9t3L7_qEhP1kdsAMHElbvjD47D4CG1B9YhJv0Mx5WawdX0kvFewq9dLkAtjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26628" target="_blank">📅 18:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26627">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=JBA5LDoC4fiwEtf5IF1L-bn7clhC7Kja7Xev2Ayz_9kZ7F5PsqIsTvcH4tRfI39864Oe_q3XTSjZVVSVvCBhqrJzPJw9GBYtaOoCS2vGK8nWwkBlQa1ij68MT-UDo3LYmYlw-P4xfNpvqE3-Pox5sZO2EUy9cQthjBldNavqZBFkknO3Xkm3sfO6Ywt8IOtLGRGSyvaYyBnclZ_7z1uXYLdMGTa_G8k1dFpaiEeBt4ukey5hMgZwcCtY4FgZJMI5S3Z9ObfmpMT0dz6LBlahGHMMQitqvZVxA4W5evtTvprEWYybMWonPENobAE5KgGSB6iHZUkDBsopnlOyZHMkbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=JBA5LDoC4fiwEtf5IF1L-bn7clhC7Kja7Xev2Ayz_9kZ7F5PsqIsTvcH4tRfI39864Oe_q3XTSjZVVSVvCBhqrJzPJw9GBYtaOoCS2vGK8nWwkBlQa1ij68MT-UDo3LYmYlw-P4xfNpvqE3-Pox5sZO2EUy9cQthjBldNavqZBFkknO3Xkm3sfO6Ywt8IOtLGRGSyvaYyBnclZ_7z1uXYLdMGTa_G8k1dFpaiEeBt4ukey5hMgZwcCtY4FgZJMI5S3Z9ObfmpMT0dz6LBlahGHMMQitqvZVxA4W5evtTvprEWYybMWonPENobAE5KgGSB6iHZUkDBsopnlOyZHMkbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26627" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26626">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=jHiZE577-1Q5elnLOoj7bhVj5MZ0FVc39UE8ysgTIsdeTXARepj-8R0G5Q6Srgxv2MFnBNq3kqC2NapDVXylJwhU2KzWTqvUshvB9Wxph1xWMB-AcLXYUOlX_NrHieK4qFRImM2WBbDLdwwBYVGSpk8VJiRMR7x1IexOr4_4jORE4MzJ9-oXke0lzrkykZLxuuZXBaJB-9VvtXu3qjwn2KW-zCV41qHveL35Nt9TXFPZrIm5bIq6KOLCxFQGBwFez0BjMc5tSjkLfYDdNuoEk9SbIBbCE7-2Tor4BQJIE0TPqg_TZY3nOFOkHt0rfDPeTQ0awtwwmZ_mBHLQXvhTPCxGbFIopvWfGJVfOZjT2WTfQA5fCb6YkGa_i3YSf1sLJXz-3tvOjOtJF5DztiWZ6cCOuiaWlSaYJL46AY6vqp3oXHK7Nz_5kLTu6TXQnS1dkHDaABM6mYB1OACiCa0fwWlsL90Hu5dFYhqYhvi4LMFaccmwOkVy6KxJDFBdqxWpY8HkXphMcrjidHXk2PVUIlpGzvh78571I-9BnoGTxg0f-bC7NaG6hhcg7TnFKYfGRRYFFJWdjWDVmRyCWYtoomChW28Me7OOnwgICl52FbBEpByloPmJy-wcGPc5IhD4eKv6CXDdYMruspohN7j2ocp5KTtkCFynn5LbK-zdLHM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=jHiZE577-1Q5elnLOoj7bhVj5MZ0FVc39UE8ysgTIsdeTXARepj-8R0G5Q6Srgxv2MFnBNq3kqC2NapDVXylJwhU2KzWTqvUshvB9Wxph1xWMB-AcLXYUOlX_NrHieK4qFRImM2WBbDLdwwBYVGSpk8VJiRMR7x1IexOr4_4jORE4MzJ9-oXke0lzrkykZLxuuZXBaJB-9VvtXu3qjwn2KW-zCV41qHveL35Nt9TXFPZrIm5bIq6KOLCxFQGBwFez0BjMc5tSjkLfYDdNuoEk9SbIBbCE7-2Tor4BQJIE0TPqg_TZY3nOFOkHt0rfDPeTQ0awtwwmZ_mBHLQXvhTPCxGbFIopvWfGJVfOZjT2WTfQA5fCb6YkGa_i3YSf1sLJXz-3tvOjOtJF5DztiWZ6cCOuiaWlSaYJL46AY6vqp3oXHK7Nz_5kLTu6TXQnS1dkHDaABM6mYB1OACiCa0fwWlsL90Hu5dFYhqYhvi4LMFaccmwOkVy6KxJDFBdqxWpY8HkXphMcrjidHXk2PVUIlpGzvh78571I-9BnoGTxg0f-bC7NaG6hhcg7TnFKYfGRRYFFJWdjWDVmRyCWYtoomChW28Me7OOnwgICl52FbBEpByloPmJy-wcGPc5IhD4eKv6CXDdYMruspohN7j2ocp5KTtkCFynn5LbK-zdLHM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26626" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26624">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWy_O59b_3K9xV7109V9nRTheDXV9d5KeH02TKceh_B4BnCpom5TUtHxPxAqy0YnSqD2wnmwOXTGIOLf9KDFAnU71MMk06yJcBsa4IiH1_RRi8RNlbtWmIGBWNUAW_nK5VQfsL9QbMOF2iqBgc-08_vayzme-k_sMWAkAOiCXb7AcV-0qVVf5C_HjGKElDTOMU9V_Gb0kE7COLB3bltpfR6vnc8ud0KdhjJ7G1x-befsfiTbJfB5pQTvjFzAI9UI4OZEoPVRLMR4rttMFg9srShB_OCOrPMf9HE4zwNzBcas1kWwQABV3390fU-7c2EDT7e3quUzqaAkiQcCev5Jow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#مهم؛ اینکه‌بعضی‌کانال‌ها میگن زندی مدیر عامل باشگاه نساجی‌پول‌پاشی کرده که با قیمت بالا تری دانیال‌ایری‌وکسری‌طاهری‌رو به پرسپولیس بده واقعاصحت‌نداره. زندی‌بارها تو جلسات با مدیرعامل پرسپولیس حاضر شد و گفت حتی حاضره با همون رقمی‌که طاهری رو از روس‌ها گرفت…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26624" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26623">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYRktDD5v9578o5e4KqpvG1zqb0WESRzLEkRO1z7gjaFrjiYMftqDONLhKwSLYvJepNTqNRSDP2x0iVYwB86_-P90lt3Ksj_p3qUABkAC0qOoFrVK8gtFY9LBN1LbdHgffPFcs4udCpDIWtm7e5XUEQ0K7f4Hum3VF1jH2BoBAkmDIUFrMgG7JCiYBFRbUA-2iHPMgx6Goe8qWxllL5SLxufSlf7NDLizaZfUxxwO50uO2Gep8KJ49QjnfGd7WbHH8JZLd0K3jLLLroAqG1IE14zKlpgQEYX9zwJSVqoWVtpVtbzXGnon-Jqj60RyrE5-T9rR3lPROp3wF0Sk3u5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26623" target="_blank">📅 17:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26622">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLfFnr1ZcEE7avFwro0yA0AD2XwpEHz0Wq7qkxfAg3YUwPSzRJTkeImR9PZylTgfvvqTLikVljaJ5Pybe5gNnQjpGeXUuOztxyxBDvrqjvqLDg7nFtIC2jQGKV-oTBAlgwKhwHGCNsYUxZcyv_t0XFwb3YySJsbiiGFAe8ULof4R4G59c2xWIKIbhH9YwDi3cvZMOtIhnStLxIS9c3i-KN_69WfnawX5v4W3nSGg4g3OtVo9HCg3eN9uMZQpu63KLy9p8eKCx2QyGBcXNJWUqOZKnMaAqTdl9anoUif89Xzk0WLGc8eTdPQYqS0LV8HqsyZgWHtC9rm6Ieg5MsfQNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26622" target="_blank">📅 17:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26621">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiZ9z9nPPhq2cZKImRFZQxeN0GwT_F3i1xg0rWEa1XpPO64XlUdBBbPcllcs82lcuteCy4IvlA8omTiPiL-XKHHinM9aabRMXcNuwQ9MzCmRp03xlJ5f6DMWp9T-0jk2zaEUOLbzkLqEgVKZNI7eTaK98QOuvzU8tmD12TdpRMpjlGQlL1MxHZAdFbajmDxkPObnahDZT_D_yCc6mkdgMVdfssS0qWQbzLopOoE-AUW8gC50HE-YYdsAzStx3wPJPfbckg1jnm5gFV31Fp1Aanutv7jzDza-J4VaAGnArRPtAWf3DaVeRCO-_Q7T28kaEpBi1vbk62IIMYdxwSZCcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
فرناندو سانتوس‌سرمربی‌سابق تیم ملی پرتغال:
حقیقتا من هنوز از این‌که رونالدو رو در جام جهانی 2022نیمکت‌نشین‌کردم پشیمونم. ازاون زمان تاالان‌باکریس صحبت نکردم و رابطه‌خوبی نداشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26621" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26619">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=U1CtHB2rzlvbXv6haPVyjetWFOKZcAt9EmyOXiYeRWrgFgFodxvdKchnRlS7QjAAoQvDhEQoOV3F7oK-QRTxGj2t-qwKy62UhS000whKVTiETSK8Y9FF7duu-joA3pszUPSYpLg7WU-cQ4_xUm9ByIG0KljrBSvAZTFCIj5Lf4XyBBHOKnOuipFypKYX_og4o1k_FeLjG0mgOlZk0FqbEpcMnBj5uVD_NH23qgS1QGHixhSUHfwKUqBHgHm8P0Bc1LFM0a1cJyPLqF-JGE2sDwHzbc6tySGgEdqspdC6dG0PmfXMVi6v9kX-k1YhWVs17D3fj7CS4ZCmjCjeeuSt9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=U1CtHB2rzlvbXv6haPVyjetWFOKZcAt9EmyOXiYeRWrgFgFodxvdKchnRlS7QjAAoQvDhEQoOV3F7oK-QRTxGj2t-qwKy62UhS000whKVTiETSK8Y9FF7duu-joA3pszUPSYpLg7WU-cQ4_xUm9ByIG0KljrBSvAZTFCIj5Lf4XyBBHOKnOuipFypKYX_og4o1k_FeLjG0mgOlZk0FqbEpcMnBj5uVD_NH23qgS1QGHixhSUHfwKUqBHgHm8P0Bc1LFM0a1cJyPLqF-JGE2sDwHzbc6tySGgEdqspdC6dG0PmfXMVi6v9kX-k1YhWVs17D3fj7CS4ZCmjCjeeuSt9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
تاتیانا دوس‌ دختر هکتور فورت ستاره جوان بارسلونا و حامی تیم ملی اسپانیا در جام‌ جهانی 2026؛ گفته چه آرژانتین چه انگلیس بیان فینال قطعا اسپانیایی‌ها توان‌شکست دادنش رو دارند.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26619" target="_blank">📅 16:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26618">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bT1o0hkAGDlKcjGAjm4TJQcHCS9hR92cbuCECoJOJf1t7vhO8DnCh2Jm1CJap7ZLihllT3Jqdz_8kKtD-jcOo4my1pCjeUASuV7KpFALFnOE0h3f3n5BvecH6haxmv21yZtiI0qpaz8NIW2S0PXWgn6GEwkvepLobI2K-Su--upDXZalSn8OWSO2c4NlMLh2WKWRpwULNT7aZtZcnrhg1gjYG0wGq7DZZX86hKxDTDLEbfImZB5JfTOx9KIHnwaoXGy5eVu4hkF0lknYl8-2I5AQdYDqMx5BDSCMVcLOhdJP167qM35MJFS6liSET2PMrU0feRDBMXhk-ld_dvS6bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26618" target="_blank">📅 16:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26617">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7JkPWEQNBbaSqlBUPHD17VnaczY4XWzoP2YbWqc_MXzDp1J5pWY07yfzId7CEdbbCUilqIktXNY2DIZJbbrpP74qA47VJKOR3ohLukKs4UC0OSCGYbtpAhjkFDQOL0Q406djUOjkQBM8WgyMq9fWXi6zRDbxfpc3IQ3uzPf5uvMgWSqyUmdv3ewmdIKUDaZiVVBcONkhg6Xv9_hPR3R7bHXdtckLDZ4pxwIj1hkkFaDyqqLsfJb9OQZWEBu62FQNoYMF6-UynMa5Mn5YmmkRlsb14vKbNjCKLrg10SZuvkYCyfxYqPBg1jhm3QRnML6KtvvgxbMXSwGJM2aohII4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26617" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26616">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7YbzQJa88ZpYM_8N-msfDwKqHpT9wsaa-kW__vLCJytTYsEHHF97cN0ka-ZyT7TYpfqO7X-yqdoV9rtT2C3w4SAo8XsCcgIfOJmbwBZJy9FnM_yM0dxi-pIU0BsLon5jZZEWqbso-tY3VVB0Fp7eVNzgp3CgDWsFemr2N1ZahJ3mu2MAg-VfloalZZHmzP-ZtknzOWOQ8NUWkPEAedWc-dCk9Y1ZaNTuSlcnN0_5ReeLOneal3lFjb1bp_5tOkXBhqXDN1Xuj_KixAHVXgbEfpJpCYZcGHWqlihTs1FymTe37QEUZAEH5D9Mn--JCYV44wMSOoYlfgVozlQe_f-3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پاختاکور ساعاتی‌قبل با مدیریت تراکتور برای جذب خامروبکوف‌به‌ارزش 800 هزار دلار به توافق رسید.
‼️
درحالیکه مدیریت تیم تراکتور با پرداخت رقم 2 میلیون دلار برای رضایت نامه محمد قربانی مخالفت کرده‌بودحالا بافروش خامروبکوف…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26616" target="_blank">📅 16:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26615">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kId3KWKG8AHgFyB-C10UruTGGYwFxIEBuBAXmKUXJ_VqjEr2r0oB00Czs5uoZawZ2oLTGOGPGgnr25wyEVU7NQHVebanRsPqLKd-sqnR2htq5lZgqqYIOLCc5nKAykZVV5duauPuxCIJs1G_G7QsDkxQc4XVKK0aqC4BcKhWGM9or0zzjk9W7PMz2tea2pD-FE35Mn7T5_Wtl847eU73nFTR96Ew1MJeYRsb2EYv3C544Ph_qrEzOL_5nMIzTmJQZcp1_dWvCgv4-OaaGk8CjSNbnzzmyxDpIIYPw509F1i9LWEkgU6bXeEDDTqXpJ3m6ACjXGc1GP1vOR1hPtqJ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
طبق اخبار دریافتی رسانه پرشیانا
؛ باشگاه پاختاکور ساعاتی‌قبل با مدیریت تراکتور برای جذب خامروبکوف‌به‌ارزش 800 هزار دلار به توافق رسید.
‼️
درحالیکه مدیریت تیم تراکتور با پرداخت رقم 2 میلیون دلار برای رضایت نامه محمد قربانی مخالفت کرده‌بودحالا بافروش خامروبکوف بزودی برای جذب ستاره 23 ساله باشگاه الوحده اقدام خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26615" target="_blank">📅 16:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26614">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmlPUtD6opl8dioWO-jewefokaxpost_TFb1dGZZ-Bx8ZXUHqtiHt4JqF9LeD5dFYFIOFf-F9ORdvi8s4PMP5MdX34Dw6G7g9iLAKsgE3v3U70qthS_vv0HcrXdk9iG8tte5oZJ9jE5y1CjalnnifhmX5kxiPhksoabnxwNOG2XBoX36HZ8CZ9PrKC1Tf9wFCyitcBHHLDjPw1U8j1-saBzw-bjgm7quY2WZJaE2LWaGG6pYizVxem25dVo-TXAD8xzoV8doJ5XX0b_QtBEOgX-f0kLpfwfdGn5I1ok9xihM7kj5HzIYO7k3Nnl0g4RLozMo3w1EusuoPLdwxslX1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26614" target="_blank">📅 16:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26613">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtPeD925KG1CzpVHHshnVxp7dWaaI_chw2tcQbP9cRB68mORzyELVwhPRSzeB-Eb9JVylsHEG0oF1kPNcqpCf0rQXT27x_5fFKS0y3jhICcfMvGl_mjzYBk-5r4IWMd9OemTvt1MqjDKgq0Upe5147XNC9QfB0t_QfY0VM9tL-4LUkr6oAAOAfOuG-ZZDY6baYYwMSnf8rcx1q36Lvv40jzYTAu1wWJOauF7cT79H0y1X__yAwIHvVUaYveiWpu7K_QHa_xPFCjlX8fKyObrBao3RLxhSh4EdezMRaIRMycz3TZzeKdCdnxyPfNfAmb_tqS1l45dZPu5RaaWgg9EQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا
؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26613" target="_blank">📅 15:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26612">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJVrQVb9Lz3C8oeLhT3tIX7rGhUwdLdwQglAufMPvmt8EPcUnF-u0xqW6vqfIXS8VaMXY-UIoYxRUxAykHmpiGn0dPZFBmB00KGJDZtHNh1zqfniu04-nh_6-Ke566WN6U0HdCKdPmqOdvuYaUQceozeG0dE5PGVpRFZpqA-X0Ji5EfbEWo5qLYDHhQ1HtXUz3s2_mvwS5_6CCt-6J6a5_16kgSLd56INs3WReYIMPjOkQFYL3jT4wsqyMNLcVHvlgcn6rYxKwR6zmPkUPGMa8bUHuz6wRJDwWYKPQQOv6weX5vc8xMMxCY5gRp90IXTGoUiQCRR7ULFWAEeSigHQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
یان دیومانده ستاره جدید رئال مادرید بعد از پیوستن به این تیم این تصاویر رو منتشر کرد تا نشون بده از بچگی فن رئال و رونالدو بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26612" target="_blank">📅 15:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26611">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGhM6RyhMrP_Gm8BUv4b0mxtWaxAb-UrzlEsJSr-G7lT0FF8LE5lpXwC0ronCifpys-JqY_LmbWfT3IIGFCyat6owxASFwhaFOkA0tL1gGyUOrmRc17DGEQGAIL-YB3igeBVkjIHU3vnbCSpKQUh0d3c3kn_C6LErj3Rt_0OS1F2jO9ukLMo7_0BbEtQmwYD718JWizDPawlNe73GrHEsrsPMVvepWnIzs314S31uQkSe6zXQcDgULvhVtLz49zN9rvpltPMS0C8bexKKPhFcODLavj7opFJuuxiXDQbXvFsYOhrdNg4zFKKdYpLRlnxxhSrahYH2GJEHyckWugJVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 14 روز پیش پرشیانا؛ با اعلام‌باشگاه‌پرسپولیس قرارداد محمد امین کاظمیان توافقی‌ فسخ‌شد. امین کاظمیان پارسال در شرایطی به پرسپولیس اومد که لقب فوق ستاره به او دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26611" target="_blank">📅 14:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26610">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mU1d26vz4PIvI2j28BTm6qT1ZcM5RaGu4WqnfeymiCVjDraSJYgEmCP4AEA6QaERSqY0gtZUV9-trxjwNcWMCGr9gP7n37FdXG6zZgfYf8Zg4QoG82svmHbAaT2OmPBJ0uq2OBaDekDY2VIrUjeGB2l6hBe6EYAa4dn35CuaBoOZ6O_a4sAcp-plCdMTgXPevVC_T7wEXIne5OyszmNFezCPL5rh5vMXLzHxS-GUnprWq1-suVaVR8lLjrYl182ThanxNDX-bXeMMK-8FBo2LaSH9HE1piLB7Hdwybuss8dT3aEMv6y9pEocBQGaR9rHFS2GCemoAsntqXffFtMEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26610" target="_blank">📅 14:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26609">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b74811f44.mp4?token=iKJw47fdu6cuehD80d-hovOLruPU5GNZp9ODoZPI0BwkKFSW2BAVWsEk-65Er3bK8QG5WsnL6LpKqQwcslngyrqrJcnCxcik_hYARNtX8HuDCEoJjTN9O9l4afGd74qR5VXmODUZW3w4Sa17EsbLMxJSBQaMegXmozrn4HUFXwzokSIbDAMzaYYk1XkpotNyVTwsF_uKDSX8ITwZzWybzaIMqOKWmqNAFLsIfJN_TpGlAjJXGGmNk_5RmZCM5k9iHf_5rbU5Chiphwr-uwV4nixT_l0N8BB2z-4n8cIh-Pj4m4dSqVtZbFdDrqy7UmmG8WVCD-ym49w7vrtvGRnYzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b74811f44.mp4?token=iKJw47fdu6cuehD80d-hovOLruPU5GNZp9ODoZPI0BwkKFSW2BAVWsEk-65Er3bK8QG5WsnL6LpKqQwcslngyrqrJcnCxcik_hYARNtX8HuDCEoJjTN9O9l4afGd74qR5VXmODUZW3w4Sa17EsbLMxJSBQaMegXmozrn4HUFXwzokSIbDAMzaYYk1XkpotNyVTwsF_uKDSX8ITwZzWybzaIMqOKWmqNAFLsIfJN_TpGlAjJXGGmNk_5RmZCM5k9iHf_5rbU5Chiphwr-uwV4nixT_l0N8BB2z-4n8cIh-Pj4m4dSqVtZbFdDrqy7UmmG8WVCD-ym49w7vrtvGRnYzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
پوستر باشگاه آث میلان برای روبن آموریم سر مربی جدید روسونری؛ قرارداد سه ساله امضا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26609" target="_blank">📅 14:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26608">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLQrEjAVzM9R8LBugfv_YAJiv-bE8LgpWKZX1QCBz8yAM2VQxtxGUtXqGXkrsq907VVxLxZZ_obToDWYwSNzDuiLDRJLabYYODCxXBfnd5uj9qSQUAmwDKdtJf7t6ku7Z1Q4uQut8r840nkuAQtp3MWESfXX4GWisUqMPadpE9agxXQs6R9d5fQkc4-fWK5sItcqE1RoHBo9lDq5BbVc8MGSAiKwbNWN10kMrglI17EOlX49SnUwxCm6Q4_u9rpnpcdaAfoFXeLNh83_UzLfXGM8dVbyUPktb3gAptDL_1PNZolY0Ft0stalybiDn06KxdJNZupIZVhI8wiDyl8eiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26608" target="_blank">📅 14:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26607">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQJxyI-uzPk2EwofNxMewrIn02CGtHL47QijAHDR-KzI24vDSZEWWS1xhTONNxJBxmenCcBCgkDv5T4SbS_w73BiQAvU36tl9ZUfVhMLigq19eQ_4bNYdgv68TJYdM9naRZXzxNBvSshTfJf-tBBzkLS1lCkzx5FhbhFY6k6fYN1w4xZXZmLDeMJxIKrif-RMJtZ71AkX2I45avAUMfwP2C0HaF8AXp8rlU0t1k_zrSpRRhmV4IUq8k_xu3u03EKFuWeRMuC5ngb_KqVp15Eb_OHwDAtoxG42za74USyOud_ABCvXFCA6QNOyxrEdaxRjGBU645Oz47t94a14QvoRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه لیگ‌ های آسیایی از نگاه Opta Power Rankings؛لیگ‌برتر جام خلیج فارس ایران در رتبه پنجم قاره آسیا و 61 ام جهان قرار گرفت.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26607" target="_blank">📅 14:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26606">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vv2CupGpIG47smoO4daoKJfYHTsbVdb567TL6K_GapFXKZqXA1ax6yyHplgFVRdmqxCU4KNNUPgDe5w2HSbUQ2JtE1_hLpdeFQVZMTHfmMqvsNGx9vwbEyS8Di4RyjNv8fJ3gdtTeWyi8Njkmfx3vdZwc9R5NIgnompf4p8Y5wKQ2jQ6kWJxMBsI7AzSUcnNXjA1P1VDeo3_-CHcxWIEqlXFN1I9Zl5vwQZ-F4KIYDbnPrPBznw_jq_tmM8VI2CN32OsByMeGbbCBjq5ALkj0Nypg6ZcvjXU_s_bssMSgi2vXergpe3FueoW6TBjSV0GZ_W47tZyvotWw3qTUHQehQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه نساجی مازندران با هومن ربیع زاده مدافع‌میانی 27 ساله‌تیم شمس‌آذر به توافق رسیده و این بازیکن‌جانشین دانیال ایری در این‌تیم خواهد شد. جالبه‌بدونید که ربیع زاده با اینکه مدافع آخره پارسال در لیگ برتر شش گل زده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26606" target="_blank">📅 13:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26605">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crTTtWV442KiCb46rjFncZgK_Emi-GueMV6FYVT-jUEMHpOl6zr-yfrsG8Pg3Rbh7zwVxWeom6fSTWyoFgULrUfnY7bTAkODGeAcyDkVD0LiWEZYHQvpNyhzCpHW6hoYY7OtJbPi4pqF86E7NjeP-keDMmcC4Kp2EHz_tnhL1Ge7oDQF2nc5TroCLWeT12vf-RMDNpogMwtVaVnqk29YJ1DnF96RPAe6n4E_i07pzCafKDug8i3f4nQMQjFP4M5Ddfvo8QozPzqS2NnoevflK-EIXwd35HamWuC6x9xmtIl8zTx35hSK44EpGiqifNfN4hYStWw4ChuD616jE78ACw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🟠
فوتبال ایران فوق العاده‌ست
؛ داوود نوشی صوفیانی پری روز رفت باشگاه مس شهر بانک پیش پرداختی گرفت و رونمایی شد. دیشب پول رو پس داد و امروز با ذوب آهن اصفهان تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26605" target="_blank">📅 13:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26604">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzReZMA70PWsuVaFpbSayvOuR6ZYetq2muUwPsKkSYUNZ9sROzWR7Iub-d2_6xjXH8vi8d-dnWRePEAz26C03eLW99l9sXJofit2vsgKpp1sulLq_-kKM9wX5gDBxsCwRppmCpgTtsXtEDtWGOsWSX8L84sgCz29PEG2fYta4m5Thgr1ZOoF7usRjEgLVmv12qckYKSP2IAGEm4ajr98MfLTOKcHeb8hO8Df2WP0h-EuKVhUPwnepEHQx-gdv_XzYNeIaicsJTrc_gSbWcXhP-zOvBqFmNXD_fr38g4zTUDfSL8vzaNYjeZWul_l4Dd346H0GD_sMCkRps9XWY-y8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26604" target="_blank">📅 13:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26603">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0cb160c99.mp4?token=PIKdmMBeONFuiq1EBedZnRjfNL2CodDKaty44t0IQEp-0QweFHfnkzyCr2ueWNbTPAMdzYLsnbzYvNFZ5uVz5L9dY876yZTc9bAZZ91Ks0CiHmi88lYlmMZ8aZqJ8Z8v13grsImg3iy6ObZNm8iWCV_KoTbbqJZKFa-LxZUJxSIymed6oSVRL_7NTvLqrYFjG_fgqozzzO3Ba_nt7yDs9deXJgxbLTtkyaEWKEFaElinTJa6Xhx45EonhKLH2Xb2ZTnpcixMwu2w3gRT9g_vpaszTHf99eo2cYajmIF1a83hbVfE-CWuifH4uHotn0eUQKhV6nWYTd1FKqFlQJZtUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0cb160c99.mp4?token=PIKdmMBeONFuiq1EBedZnRjfNL2CodDKaty44t0IQEp-0QweFHfnkzyCr2ueWNbTPAMdzYLsnbzYvNFZ5uVz5L9dY876yZTc9bAZZ91Ks0CiHmi88lYlmMZ8aZqJ8Z8v13grsImg3iy6ObZNm8iWCV_KoTbbqJZKFa-LxZUJxSIymed6oSVRL_7NTvLqrYFjG_fgqozzzO3Ba_nt7yDs9deXJgxbLTtkyaEWKEFaElinTJa6Xhx45EonhKLH2Xb2ZTnpcixMwu2w3gRT9g_vpaszTHf99eo2cYajmIF1a83hbVfE-CWuifH4uHotn0eUQKhV6nWYTd1FKqFlQJZtUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26603" target="_blank">📅 12:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26602">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIZ15bqX7FEDGAOit1e9qlMRta_-lUwS47gb7pxsmvvN10N4-uW-rx3XMFRXOhDPz8cnt-5k3tLOL-9FHmmXSwaXh8h8QWI0cvRCCNgbbX94BWcmKTxcIVKYshhVoNf4Nv40jsklj8nFQnFj4S-isjQswTCVezxLChK5F597d2V1S1VmlninzJ7zaP6Wvte3rFYxP09HXn30jjbFGrPmSg_aRJ-QFnuTWNkL-yVLuiyS8_jxcKfR-Eq7dgt-QK_18S25x9Wgdh4DzPyQjIP6ADTuGk3JK3JttpvOv5tLVz10MIeATBfG7LUyOpb14dvKzGSmqI9Cxm4pD-VfrYx0KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26602" target="_blank">📅 12:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26601">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXHOAaPQ2Jk0DgtNDCQys_gE3IH-EZNg-gQNpTGQG9xX4Lw7ynmGmN79pMVJSKcZ5EakbDO2aYUjCCMYZiekwYh7vuqW-XRUImG_6fvkMEPQQlOgZFYDQVCy7wPmcQxV8xBWfMoMKFdU4-zKkvy0ib1KFvuGi82eMzBKjcFrC0778E3AzbnQ2xEsoLBWT31EpyBbruIfyDzvj_eJcWrJEsFIDQqaMfK8rgpT9hHPcGXlAFjNAo0TitZNYQR1k9eb-HPY0-PC0K1YU9mkbCSKnm5Q6HHcUN8MtdCrsTaCqnBB3NLiWoWrwLJwCc3NehhGQF3I0AhlJD_bOkrO8sbBIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26601" target="_blank">📅 12:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26600">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsBiAScJETdsyX2CShBKV_hCRAJjaYo9_tUVEMUWEmzOHUG2Zs1NtPTNYH3L9HZwX9YdA8J9L2vZ3UO-Bu5SqlHOshybcyWLc1JDqMjnIkC7uUFVCaa0-QbHf4J1y1l_JeljrU2BSSmj49KGF-JwVUacu3QH2L36b21CFo7UbE9_UKr2cC9hDzoeh5-OPjSjgF4gWnIUXrZjNg6A6MxMLuLwBmOAs1PziufJKOJ8IH76Jjn02m0Ndg3ThY_69AFTuDkDittHBUKsbuiBku5E0aGTMeGZWsjtdD6Y7fpDbaUbgGW0yJ83nKpWouBiXnbZc3PH7Y2aQk0uaQiFoCibcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رئیس جمهور چک در اقدامی جالب و در حمایت ازتمام عکاسان به عکاسی مسابقات فرمول یک رفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26600" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26599">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSv5hyRShoi9SLeLAE4o9iBdAquzqImfMOuAWErBjqz3MCeg7g22ef8Ior-GN1SkeyJmwtpl2xRsmNJCNVdFeb3qgAHtzhKiY5ADBAlOimX9rf0DGJV0_GZVmkQCPDdhhS0-NHL52gBtj-5Qy_hoWK1pB-E_GpRGFutkkqDQwKA1dFyVrss_HmeiHIRSndTsmtEWoPLv6TlF6qYrAEA1uhjnzsmkBMxQ_gqJ5DueZNIuwPunBCV_vTxj9L-u7meVD9lTPntGr3IUM-XUGreAxTFcMjX98d0OpBALrRzvQULMb2YTNAmmm9ARgEbIacc-WPpJ5ZfXGidMulHGY-2PRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه پرسپولیس صبح امروز به درخواست مهدی تارتار؛ باارسال‌نامه‌ای رسمی به باشگاه تراکتور خواستار جذب صادق محرمی مدافع پرشورها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26599" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26597">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v18lESdK5nKgT843LFrBu23FlG6T8lkMV4BHK3GoSuL2yOra4oY4ysXClagCyPPDoX_czJ48QQmS-VyynN6dMT1gEOTb5aNw5KlcTD4ic0SE_m9yG9n2dN-iUmUKWesopnPAacM8ddYAUC6Jc6DZkkTR1ptbaPufs4mkNBwrGpwqV5AsD-Gj6_N1LQdIc2P52B3ehNeCMMUiY8AzPCkyobsS4Rl7Iri1ekXtFRTBH4PeHIv7VdivHLzH6QpAz7UQecMDdv-s54PRnc0QYB_tBF0tE7msMSFFaHdoAC_otmPj_SNf5VyygHiLMTawZr1AKxUq-pOROH7eb6W6Mn2jlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه‌گاتزتامدعی‌شده که آندره‌آ پیرلو درگیر یک پرونده شرط‌بندی درروسیه‌شده و به احتمال فراوان فدراسیون فوتبال ایتالیا قید توافق با او رو میزنه و روبرتو مانچینی پرافتخار سرمربی آتزوزی میشود.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26597" target="_blank">📅 12:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26596">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a36a095cf.mp4?token=tQAhBafINtsP_pDeb-qE-klzib3eBDJFUyjvnrvhhSRPx_-uFXUJSD0En9uZ9lxEf3UO3KsGQjVY1t6xh5DzHQgSnz8XbRS_mOkOxk2Bc-l5dgoWUPfFyh-amLruop2XlWhRqZe2rURRqYW58TU84av4vkShJmnliHL4wv2AonPhv3cPcYYB12lYh6emWriZ4licU7TlzFWOi12TSZOOLiMsxlgGDu0-080iP7_9gvnMCicYzLoq1-OKAtUY_zoAJzA4IpDldB4uHiKZcPg_X9qg6U8U7iTjTzAZQLwb-8-NMJlaHlW68ahsBW25tN_RtI8nWYph0ZCOinbWpt7uUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a36a095cf.mp4?token=tQAhBafINtsP_pDeb-qE-klzib3eBDJFUyjvnrvhhSRPx_-uFXUJSD0En9uZ9lxEf3UO3KsGQjVY1t6xh5DzHQgSnz8XbRS_mOkOxk2Bc-l5dgoWUPfFyh-amLruop2XlWhRqZe2rURRqYW58TU84av4vkShJmnliHL4wv2AonPhv3cPcYYB12lYh6emWriZ4licU7TlzFWOi12TSZOOLiMsxlgGDu0-080iP7_9gvnMCicYzLoq1-OKAtUY_zoAJzA4IpDldB4uHiKZcPg_X9qg6U8U7iTjTzAZQLwb-8-NMJlaHlW68ahsBW25tN_RtI8nWYph0ZCOinbWpt7uUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی از تمام‌کنندگی محشر لوئیز سوارز فوق ستاره سابق بارسا؛ یکی از بهترین مهاجم‌های تاریخ‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26596" target="_blank">📅 11:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26595">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gV2250xEUm_U7gNVOFlIrVx4YRELLQJDPTzlB8I-sdOIh4NHBIwm4LuASelgndlnam_EAlM37tHbq-OHF_RgXfANJooRxy0V7I2M1Uucjnrf3HcnoTme2eWjclASUJ6VVHh2mCMKg7NGwdNnf1aZrhy-bI-0OU1yI-ieWYagZooftjyQUooyzqC-yuTEkqxQxpUwzkpLX1A5j2F2SKIDPl01FHcekbEbvpeBy2KUEbbof2qdDoWn9HCXcncwWuTX_g3m9c85Y6155rXXKw8wSiBJXVW4URsw8fT8IQbIaC6ieUkdGVH307E-lYJSVCpKiEWcFhDCVhvtcHnN_xAVUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رودری اگه به رئال‌مادریدبپیونده؛ احوال‌پرسش با وینیسیوس جونیور در اولین جلسه تمرینی این تیم:
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26595" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26594">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilpIHmhr6f-oRsY0DFYSafmnGq2GnkpYP1DbbNfPPyyMsGO8tS0mNrUMKbE0lpa1KHj6I3SR5Wf1j72ZvM1MW2no6qmBjoMjYWerl_AAuLC4sZtHkOhsQYbpB32pGczfoGIHMMr21cK8QyG9fkmwyxrEP0twtsyw-i1MJB-YF-rClgy127TjQ03nGDhfyy9lQrChVxSVAYFcRgZvSiJ9C01VSHvLk1TX-pM1GhEqjIm7novuD9-vx2fo1ck7U6NYt9H82DNZogoGFH6qUejYqanzQJzl92vCP_nKDusK-MFMrlVMnpNW-_UP3YQaBKT0pKz7HI1rFVT1knuuIhc-2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه پرسپولیس صبح امروز به درخواست مهدی تارتار؛ باارسال‌نامه‌ای رسمی به باشگاه تراکتور خواستار جذب صادق محرمی مدافع پرشورها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26594" target="_blank">📅 10:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26593">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFIr-_G1HKjyHabJnlc4DKmVb06eTyXGsb6RTH0roASYCxH_SI1fbwWAyMyDd5qKg4iMtu0_urEKcDTt8TCqewOuD1_3KfOsv-KmoP_kOXiNMwCAs7XIfoS3f3qJ3Pgz4ZOl_jTS-lmA12b523qHYcYNHSnoaMgeijF3hVKGVaBzO6MwjpbjEybn2F-ttwP99PivuRF7-ype91qU35lEDux7UjC6cvYXu684Wa3_rlfpq42LYPDHselWA8Sod-ydjfBYAKVyt_bMMGvrjaHnLkWXOPm_SroBmKKApo8CIgWCGSa075CiQlG-ihiK3rZXYqbO1i9-CoDDjMT0CICx3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ دقایقی قبل سیدمهدی رحمتی شخصا با محمدرضا اخباری دروازه بان فصل‌قبل سپاهان تماس گرفته و از او خواسته به گل گهر برود و قید حضور در تیم پرسپولیس رو بزند. قرار بود امشب محمدرضا اخباری پرسپولیسی شود ولی به احتمال زیاد راهی گل گهر سیرجان…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26593" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26592">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5E-9Q7gTcXzQbPz8v69jNkF-9Qw8wVPfcKUkBNzc1PdZqfF6tsmUjGRUONK_6-feOBAUMagjrGvQuG4HWyDfoCyBn-_Qui1qk__eDIGZeHg0xiWzSE1OLAeUADIkZpaMx44e3mAfECcR2qYF6ovFeRxDvYtH8xCecA_Su2ZVSRnAWDQCB5Cy8Vr7woN2K2s2O5N4pqr5yoxlBI818bqivwYPLtVpF0cy5K7o0ATdaNugjxULEXp62Aq3FLLWohWvc2UbTSIKnjCR6wqs8XXyKfD-28zNpiiaaFVC294GPDvyrmcRRh_JxUSVdrg--f3gGcz7Q8gn8WyvwIp3JeAKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
چیواله وکیل ایتالیایی‌باشگاه استقلال: روز دوشنبه یا سه‌شنبه هفته‌آینده دادگاه عالی ورزش رای نهایی‌خود را درباره پرونده‌باشگاه‌استقلال میدهد. ما مستندات رو کامل‌به‌فیفا و CAS ارائه‌کردیم و بسیار امیدوار هستیم که پنجره باشگاه استقلال باز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26592" target="_blank">📅 10:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26591">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btP1dsDBolQtAQhVvC7TT30c9lIdcYFxcr4_j2QJyxEwVobf3faguPYnBYbepcfXl_RDMAOpUYJRY2oZNfVGeWR0JO9aOYSj4TN10aIM16fmJAxtSVnHYTbVbEJ_4mHj4gB0f4rc9HIJnySgmmCTshzjUDY7Hmg-wqP-y8zTuVwn_ClSEq_B7Ytm55GEaT6KiKj7c-L5C7PVfXWeNbBr9iOKo5Rx4t1jxzoDWkjv4NIjmDipc2ycjLAq66GbApUJZ59HNM3OvQfPM8rObCeAc5F_pd2Q61-A1fFhPma-a3-RED4RPcez7oVjxZzJ8YMiVEBzbOSiIIUrwxSqb69U9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#نقل‌وانتقالات|باشگاه آث‌میلان با پرداخت 50 میلیون‌یورو به‌PSGگونزالو راموس مهاجم 25 ساله این تیم رو به خدمت گرفت. قرارداد ستاره پرتغالی باروسونری تا سال 2031 اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26591" target="_blank">📅 10:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26590">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4SRbeROi1X8xckFGCbNzUqsKZ6HnPwwk8kDpuqT00VoJiSRf6IHpAihbKwjN2EpVAMTNZw6ejLgzhHx-nfLY9K-RNroLq4_gboJ1_2S-Lp2bhHo9Z2SpBz7QSrVbf4kNgaiHd23bhab898_NhxW5_PtsIwmO9rzauHIY1pYex-SGrXUXvYFB2kzcpX7iJWZUxelfEECKVfWdVUZNhIKpayly8dmaTohBlArodLTN5Ea8E6mKv7RRaPVvht3Fq7AcaqGy8Wj3EnQkH0dOhwYb49m6bCnqKqVuEQiJi9YLeOX3JWRZhmkw810NUhYd7FGXD0dYhymxreVp055ppZX7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26590" target="_blank">📅 09:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26589">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkOFUbDk7c6--QX2E_FpuTC0Ashpw9d_BlEnPFftkRWze5_b35-3AkqJ1fessVahh0Y4LVA51hPKSYm9dfPxwAGz34aDbVPHBBVIXrm6ru6AE5tXilkjOpg6znGSmnv4AEylYLs6j3rQKM-Xm4D2Jfn_EoYB9eMyw945Vl9kgjF0gkr-OLiUl2o94482glG2_vvI60BSeMtVU-V-__gafd7ZDsngIOz43l5Fr_7LInVkDBJWGSoyI1Vm78fLzRfB__0WCmJavJIG5kE6aNk-mIcrncVW8GxhmCzkeAGCy8BkrCbaNzA-WFhlubPvbTcHvf-9bTs2VhgVdWj3QrCz4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام جوینده در ادامه‌ مصاحبه‌اش گفته که سپهر حیدری تو روابط‌جنسی کم‌کاری کرده و اونجوری که من میخواستم هیچوقت نتونسته من رو ارضا کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26589" target="_blank">📅 09:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26588">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c7b549a0c.mp4?token=tIh93KU3rwRDHuUa3BDjuG88P7MDF9KFcJtmj9KWQ3rd9dmBf6vo83VvTvmZrvVOThiUQr6-3UiUxiGoVuekmOhvPe9Aog721A8dndpATE78ijAXcMWf7Tpzdwg7-bXMA7Mo8NKz-bDvQEtPhUd4zDuVRWoi93UtGIYvOBqJiRhjKkKfQZR4Ewb2gUOTNydxxgV776woDz-99mZcacFQxT-A2LbDOZMBiMkb63uwZeLzyFawN-kGMh7gGBz_sQaqgilovM4vj_irc_3Zo7nqgF3v1rauhJA-Fyg9oHl5lJtb7pL2CYrF04hJwZhhdYD-iThQJRlfBKSUqCDXjlni1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c7b549a0c.mp4?token=tIh93KU3rwRDHuUa3BDjuG88P7MDF9KFcJtmj9KWQ3rd9dmBf6vo83VvTvmZrvVOThiUQr6-3UiUxiGoVuekmOhvPe9Aog721A8dndpATE78ijAXcMWf7Tpzdwg7-bXMA7Mo8NKz-bDvQEtPhUd4zDuVRWoi93UtGIYvOBqJiRhjKkKfQZR4Ewb2gUOTNydxxgV776woDz-99mZcacFQxT-A2LbDOZMBiMkb63uwZeLzyFawN-kGMh7gGBz_sQaqgilovM4vj_irc_3Zo7nqgF3v1rauhJA-Fyg9oHl5lJtb7pL2CYrF04hJwZhhdYD-iThQJRlfBKSUqCDXjlni1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26588" target="_blank">📅 09:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26587">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8NCZvWWevPtRS3C_8psFT6YkOPFvk6R2tn8dDPnHY2yJ7e8j0JKyIW6xvM84mUAvGtAl1H-I2mXAVnEKDBKpZytoH0F3M_bP9lhZ-G5efhnJ8j1XHQlJ20j7RLFiF6BLgRbv2XCEaiVmiiHlCM5UvnPqZMouvalBUuddEp2O0SSdkVwAy-fMngoz4d5OCWp_TBTsmN4VBhfRn0h-CRDW2G4NyUBc6PbdibCsX0cdxzeBs0n5YR0GbxflXE5UcK16iJMKMWiS91IGWFVqugHequsvY2x9TVUvIMSO_3LUA0Gkg3fjMZY1nIzhKGEuI4JtinIJ6VGaRmgYGWuqhhTJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه جالب عملکرد رامین رضاییان و یکی از مدعیان توپ طلا درکنار کین و دمبله در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26587" target="_blank">📅 09:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26585">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cqkalr3H4dJWY-VhgTwGo7EUBDZG0iuoK1rSUBPQpciSY8YJLoICv85Zg-mp7itxptrkBy-Zjzf-uRxGtmSVBxBya3SV7aG9HD_hHaYGT8hk4qxZOf9Sn0y4AFzr2GICokIXp_uraep__rk2shrE8FV86xTPTmYWfhqgPrOz5bJ4KLpF2xjwocna-W5v8W8X6_AHO2rTfVNmpxQpl3kXCPa7LQmYDGJ-Im_zI17h43ZkVzLov1MsWUbqjDEmmInXrvem0J9qvTgkB08hdI0E3uQ0bCorOudL6ffln5tCLmmvVMFptk_DBTsPEmvggBLeMvJpFdkkEans-CO4zQ6Jqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b0pPWnHEO2RFyR9sN359UKF4dY5_ZulJAI9IB97akjSS8E7iYA2fzUvH91VMdRsavHLrHx7FyLX56ONiN8Le5e_eN7Zjccd7EwDhJqdFXfPom6JuDxrL9KYUJnzVbeN8T-2gCyhVCnhMNPRKZiUZAZM2NjHSbvHfT7yZEl33QLaUqzmLdyALzIbCCnloHS3CTZ4vsd_0fczKIeNGeyZFLUjMTn2rGTM2KnqYzzYXL3Nqg0m013L9ekfWPt5Oee4LrwGpR22ZMaC9A1vE2ahUej1eoZ5VQ2EEdEH2eLqcpncSHomWo1ldxMYtLoCwidhOQyLREysEtDXvTEp24gE0LQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
آقای دیومانده بازیکن جدید رئال‌ مادرید هم مثل عثمان دمبله قبلا یه مصاحبه اسیدی کرده: الگوی من رونالدو عه؛ خبرنگار: مسی یا رونالدو؟ قطعا مسی!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26585" target="_blank">📅 08:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26584">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7iH6TnN78Pa57XCICyQL8RKbfS2QicfYISBe4_uqiiABAmYmwJqA4_ojRsN-0uEapIIY09qhMQVBwNH1AExoqrBk-lxsHvQ29Wssm_lnRllMLCnI1LJ6o9JyT0-cpvL68bS6gc9uxYvHBeW6WeonhBlJba6FX_1a6pJpKLXLjq3LEBD_sWxXD0-EfnmgSkVL4DcnXv-q4qTJjQuSIU6_DCpl3t-WwVEtQtTzIdXy0TsTRI684a8oAvEN6tKpUEI9YvBqpz9dFJFmiRhDhbb-JrqlS_pbH3i0Oc5MAIDKBua5Ppew7n0Jh10BAd_YFvtflm7SxzYKL6b_2nukSeLWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26584" target="_blank">📅 00:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26583">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwca1YRzvelUq4BhPfD1kzOk4mMTDdk4G6aEUwXPJQ3otnUDFTTPf9F4qWSmFZncxmNN3A-XfflYe8_YobbiTQVDqVuaJ8KojoYTg9W4qMpzRDy7v9V3c9AycYtQeDuLA5c__cLiAf9Gp49NyMOF_JVYbUcsCZHFpqx2AUyZN2QdU3OlaB04PjkfoWDFFnHGR_t1qKNjOOUaNVM0PkpGLSipQ1NaA5xBVLvBg90F2TOkJNf0rHJkA7SB5adgl7BuVp4QPPvbUaR223k1Wpi9ig6VRRqVg40YX6PS0tdu76uMWNfXKNQRK0RGIHTZWFwiBaGHy4L_2e-Mo7Q0WD435g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26583" target="_blank">📅 00:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26582">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfwVlpko8f9Dpmx5N3h5w8pdqCUP--8uuT0G6n6YQUhWrqgmadpO5i-ygmR1r3-_daom4ls4tSti_3M4rlgqfdD6rO4oRDQxKyhHS3gfT6Z8O9zEby4PraYffzoiLsBLmo3JdU3ZvNpFT6JLbx74ZzdDE4oFfCfabDafrun6EeaXndO3k1C-1x8hujZzXZ4GcJ6miWx4XjygIZAlHyDoHXsqMeCPUQtPfFx0W6aEwcJ8uHAxCfFC0rbC3l2T8j3E9ff5XVno5UsmWw_g7aAAqgBvjC8wpOVC5C8oZ193LAGLppoYIXv2WHUYgnVURwuuhbYaaKy8Zldo9q5X68AS-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇹
اقدام ایرانی طور فدراسیون ایتالیا؛ از پپ گواردیولا، کارلو آنجلوتی و روبرتو مانچینی رسید به آندره‌آ پیرلو! پیرلو با عقدقراردادی‌تاپایان جام جهانی 2030 به‌عنوان سرمربی تیم ملی ایتالیا انتخاب شد. البته در صورت ناکامی در یورو برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26582" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26581">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8UxkI6-OmxfKz96-FKfAAS8L1DDTlxMbNO109r84s2rvWa3FVwuRyUDlzO05l9dQV-OocRaPSnwYF84EuC1l3UjFznEub8I2-bpuGB6Rx-2VE70pWgut-U-80jEbZnwWAr7R-OhT0DNu3kzljVywaRipRHT0490qhdthu3MO9dlab5Il_GV5ktA6-14oV_OeFqC_vANfiTVNkcSd9pKea4qniXtlGKZBZZ2kdT-Hdm-vX0Ho1q5Wscvc-7QmopzlHFVMu1jijOnwQOsZ3anA__VMaRQGXHAe2bYCNdaTXrce_00bCEe0F8KVVmRDys9GQlDk4EzGd3ApR2pLnR66Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
برتری لک‌لک‌ها با درخشش سوبوسلای و برداقتصادی‌اینترمیامی با تک‌گل سوارز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26581" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26579">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYUzw77IEXsW7Vi1rRX2JOaHUgBjw5Thzlhatca_dyeDyINxGj0q3ynUN0Z0hHkYsi3Pm1CbC4olxLlwYPJagyDxQw8NKIogU2BxVBjE9a5qGl5EaJaeLb9E6EJDPLEm-4TRB0Hd-UHp5GQIerR4yCdIlH7_PgRGHXQIjKnSfqvgfgNr0lp7RYTs1UnlVYjZn5Ynib-527xuo6eh3Jrwv26hMCnRjf7oao391CYF6ojJGh74TRXSCBbHKJRqP6jk_sP1ds1QU5D4n6mD2KLvpGn2XFBVL2lGeUWugc8Do_PhxYvyvPSA2lmexjllIzTDKAwvta_6-1pwI8XkSRM3JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26579" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26578">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwOd4nIoY5lFlEWhjTPT6pU8VdTY15r7S31qJ1dezHzXOw1ZtsTws9yzsthWninbYmMArsx3IwOX4X4852LfKajmiTfr0DoeGjIT6VAV5KWVOif6_kb-ubujrXD07fkm6dH_TFN53Ok7RNc4JEzylZ9ASVJMgQg2FiE2QRlJZa1SHeSUzE0rPX8Xwe7bdNLlGM5jsmdj_ia1QxjXjFPklTB4sV0tk8tFby8oWB5uvziXWo29V7hnAJUL0dcEwV2BmXITVPc7u1McTCnG_y3FiHxUHEgKsswQBk80ar5nArT80j42s68Kbo1ja3kG0dEvVfNBE83diMQRHGgOubxmqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ پیروخبر ریپلای‌شده؛ رفقامون تو کانال میگن عثمان دمبله، کاکا، پائولو روسی‌ و بابی‌‌ چارلتون از قلم افتاده و این چهار نفر هم خلاصه موفق‌ به‌کسب‌ سه گانه‌ارزشمند گرفتن توپ طلا، قهرمانی رقابت های جام جهانی و لیگ قهرمانان اروپا نیز شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26578" target="_blank">📅 00:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26576">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d08e79ca3.mp4?token=H0GrkjcuAwaV4ozUOIw10SybILfaWocNjchtzxX4ShPZZvFxuj-ccywvF78XQWVRKmzmkGp5TKasjanmyjGSU936ixyREQmcFtmKGBNX8m6GYT8hFVwOYztJOkdd1qyDSUeKLXdvJZSeifkkKn2gBqRzr7WlNchEnc1uolGyNE_DGONB6yiUXCHXBB3YARpQX7STtPpiR6_7eRyuR71nCgFZjSmRPJp7XWAcbXdg5CupxKgA6vVsyo058EznBBEs7a6aLwFI81mc5Zl5nd6hoBCvCcgP6hEQuJGaJ5AvXUxUlNazYG6caer-ns4cvDamf5ROzx7LNKn4rafY-su6xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d08e79ca3.mp4?token=H0GrkjcuAwaV4ozUOIw10SybILfaWocNjchtzxX4ShPZZvFxuj-ccywvF78XQWVRKmzmkGp5TKasjanmyjGSU936ixyREQmcFtmKGBNX8m6GYT8hFVwOYztJOkdd1qyDSUeKLXdvJZSeifkkKn2gBqRzr7WlNchEnc1uolGyNE_DGONB6yiUXCHXBB3YARpQX7STtPpiR6_7eRyuR71nCgFZjSmRPJp7XWAcbXdg5CupxKgA6vVsyo058EznBBEs7a6aLwFI81mc5Zl5nd6hoBCvCcgP6hEQuJGaJ5AvXUxUlNazYG6caer-ns4cvDamf5ROzx7LNKn4rafY-su6xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه نزنی ما احمد گوهری رو میاریم به جات!</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26576" target="_blank">📅 23:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26575">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiU2P21o28gSilLTErfoANG1S73_3Vl7kthGEDIFp3CrS6eOVnbAiJ20CJM_TLn5lPa0iO5tc4EZrjo1RWF1GRvoN_053mpLU59vhoQFSmhrsNrRYaB78uEmvTua36xWUBweXsUoHcZ1vwTGgIuAxPoXVH73mWK1DT4dtaOuw3GahYj8c2PsNayed6kbleARC1U42xGhLtCvFBkVfprGmjScIyQfJ_TLAR5YWTmKGeq56IfHqmWVqHnoGlUQViaacSMz_mnpyKyNb3S084VhH1B-amC67mgpOM3pMEYGip4Ibic5bOVHvevW-Vs9kysKLC1bLzJoD-ihuc8SAiaOyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حالا که تموم رسانه‌ها خبر از پیوستن اخباری به گلگهرمیدن لازمه بدونید قضیه چی بوده. مدیر عامل تیم پرسپولیس ساعت یک ظهر با اخباری تماس‌میگیره و میگه قرارداد رومیفرستیم امضا بزن اگه نزنی ما احمد گوهری رو میاریم به جات! اخباری هم میگه اوکیه امضا میزنم.…</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26575" target="_blank">📅 23:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26573">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b08Y1souRuYLJhX5BnhEgaeM1r75iXq7Tjx7d0k2Vg7fUyN-bkMVP3P0xeRt59FnGkSoXX5B6anORZDjK5a2m3JRv9Vuv3d59gpyC3KxKdTqRmnzKfFBuEepzNMMGIQ_4xjNBlvSrzfHm31exPLEyfbF1UIEkWks97dQzI52_dmBXqFBMqtqo1dvlzYn9MvWQBnPLJjUHKD-WX9jpmYUEMQU1AEcPm4qLbeiIZUvSfFj6ayA8MczimZwkTWBId2yf8WASluvPeLF_F222pnxP3GJ2h_TJhlI2asyFUrmuqqeX5zxjxbcMeKSVBUWGhmxw-hQD9iD-XRb9GmmkTrpZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ دقایقی قبل سیدمهدی رحمتی شخصا با محمدرضا اخباری دروازه بان فصل‌قبل سپاهان تماس گرفته و از او خواسته به گل گهر برود و قید حضور در تیم پرسپولیس رو بزند. قرار بود امشب محمدرضا اخباری پرسپولیسی شود ولی به احتمال زیاد راهی گل گهر سیرجان…</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26573" target="_blank">📅 22:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26572">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzVzf2IAcp2EOYCy22tVx6TxqYrHF7xOoqN3HSNUBN4VQC0Cw1RW-VOYB7Yv615FoqIRIUgikIZsqpMHbmYGglpRHBmeRTriDFgNNqWXEAle9l3VTzLbhNH17rB7WwCtZk6j8kg-lTtvoQ01trGG_ZsUjoEWF8g9pem0MPupSvlVh8a9BB3dP-QLfxlqycuxH0KfujWo1lgikE-GJNTG191IwcX9YQ1RCLs-5aTi0LETnLiLAfEnbZSGUYAtbcID1QUCjWnCd2sYcZNrsYf9Fncz4iNk8ZSnxDXFOgf0ep4_q_-AYEO7CCHwKWurxoU-25qSTYzExaBxKYDTYfC3Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26572" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26571">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxfzKjelemIxTu1drp1o7tSxHqv20oO_cEq9_gCX1pDWQVOCqwZ_h-0woz2Ks-lPrOCUVLBxgcQxQDo9oToDiHKrqzgE5fLohk-BdggVtYlPYi3SlwEq3T916DOLhPxvL6OObB1UR-xlkZ6Efqsl8ciPa5r5xWHPAJdJxTnEMlexEoP-MgYbd5rJ6-G6GfWTDNhUlJKLKyoV2E1uMAc8uKM7LJw_Zkj9aJCofad_tHz29bchbM8w2Z-IPQyju4MuzU2oaZsK2Kil2apat5nLtrFLZuidiuIoccu4FPD1gejmRYVZNrCXFx6F6NsI9KuKnITjpHFpmKXhhG0iamJDHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
مهدی عبدی مهاجم سابق تیم پرسپولیس که در فینال‌لیگ‌قهرمانان‌آسیا هم برای این تیم گل زده بود باعقد قراردادی یک ساله به خیبر خرم‌آباد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26571" target="_blank">📅 22:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26570">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZXRkrFB72tc-5C3kMWHq_cdYSoFMHu1wbfgV23BQMGXO4_Ry6BbCoorFX7ZaRhnuDUESs1sj7ci0T5iYUSy5KHTU2FD9y0sKgWEVUXcB9hpNH6C3x-gi0VIWpkC6n2ZPhKy7wHUeA5lT51w6Ns39cOVlZl_zAzRIOwZHpYi1NjwcpwWdE_b9uf3oQh9buFG-KGpWRIcHyl1PT9-kb4AdSog-Gt0iwDpA3mjqLItJ5xbHfbFt2n66JdsVyQC8xxP4aveqc19Y3-E0xXieS6Wpd_1ySF9EkMXewbbPYytAcT7x_dBKUIurT8v2AdE0HLjorI-g2pJDHVjjuhsS5M8KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروقت فکر کردید بدشانسید یاد آرائوخو مدافع میانی بارسلونا بیفتید که بعداز گلی که به تیم بنفیکا زد اینجوری خوشحالی‌کرد و به خاطر خوشحالی‌اش مصدوم شد، گلش مردود شد و تیمش هم حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26570" target="_blank">📅 21:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26569">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEeyEp6QgJdt6-2gSZtbibTJPWP4wIUju3_SPxIF3RszVd5RrHx5CeF8u-Fa7Ua1aYi6GZuU5Kq8PrZf7chqcxIi5HOQiHTY1K5Qhp921RNsyS8f7zaKZIlVG60VnBAv0cL3pWNQkEX_Pm_dDfKP--wuVnxXaPT93YTtRCvandpfwJWORG4vfI4cGB3IQvgXmqX1zfxVAkZCdqGrPm8poModBZnX9USCnQA9krTiO0GyT8wpyz58tIeVkepwHU6_2SmB1RTyKmO7pUMRifsPAVpewebNUoAKvN-TxnaMSErGt-aTcWn1BCTocq7Zkf4kJCvGm_r7hXIJ3uS-oWHWaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26569" target="_blank">📅 21:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26568">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOS0v-y7Nwix3hoZTbjo36f4tAEfyOBGigL-RqN1RmH2WTmFUuqOYaCLJ6IGk_AjUMhYoqXlU2BtaKc8q1oiH9gpQMIyUF1OR4u_pCZsceB65S_UqrIwlKQxNvBck4uI3Xda3bx5gdnYNRFkHbakyz_s56huapn4Hh8g0hDRD8OeqEWe5t7BYien695DoG_tWT2BUnI3PyWsN8NGAM0ka48Yn3U5PwNsBTE5rmlIZlES0QfR7K0jfX1zZEMY5US1HE_Nvbliei-T-_XzZRaxbtMUnXmVqJAGjqqcI_2VJg-lnlqNvEi1m9KARF-7Jg3Ga30WSGiE22MT4M8neK7hZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#تکمیلی؛ تلگراف: خبر مذاکره آرسنالی‌ها با وینیسیوس جونیور کذب محضه. این بازیکن بزودی قراردادش رو با رئال مادرید تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26568" target="_blank">📅 21:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26567">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6-6v-Eg7lM_kd2ARFEnxishzudfCEAaLSUMRg2aRMyz4E3la_QgY0FRPoCBqz4NR2Luv-46GO3dpqKetp7uvdyV8ZR3HtKGfGcHq3bQqCd2Qend_4cAf0lgTScm_RNjWBRO2dlEC1asueUhJcLrJfO3C1VaURJ293iknZ-HPuiqw_D4P0o1F4hzR1ntQlGX9CTfIY4azwc985R-UzDGc_13-DvDPaIUdVaad5CUMWj5LBgs7mQUqSrcH4Eeycux3WtlE_xy3ux17CZF_bAikcC0yAI2MRJUOtLACizRZRFm1B0oGqrR_emP2Luwv9EBmdt1EMqA6nc8vFnriUjz5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام رومانو؛
بایرن مونیخ بارا ساپوکو اندیه پدیده 18 ساله فوتبال سنگال رو با قراردادی 6 ساله به‌خدمت گرفت. پست این بازیکن هافبک میانیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26567" target="_blank">📅 21:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26566">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEN5y72de-VPBLHeF2RoigcF8gJ8QVsAb4cw6XziepvtXkh2KbO7n8NmoYHuuhGsXHg5UryLh4wvszjfQ2lKHOnZWK578MIhucrTHwryz7Gj6Ht6qLX56lYIjPDrpZDL_qqUU2A9glXPTBEgvwd1B7irRNhXGtvTg5nLUm1i9LMT3-Ncsmn-bDErHt_RTXdZZ23Z3yUQLfgsabc-IBzU0zN9iMoLYZILmsW03P77FSYmONuEsgLtwPluZT67BkkaFclHkOqQEZO-65jVKtwnHR09p8R-FXIP0kw6q-irSkk9ICRCgrZerUZP_GshmuDQBxmTkKFmgE2P5JdQzOXTzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه میخواین بدونین کیفیت زندگی، اضطراب، فشار، چقدر روی زندگی‌تاثیرداره، باید بگم تام کروز و اکبر عبدی همسن‌بودن. تام‌کروزهمچنین بهترین تفریحات، بهترین بدن رو داره ولی متاسفانه‌اکبرعبدی‌فوت کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26566" target="_blank">📅 20:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26564">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYbt1C0u1d2BuYznqDY0faSD-qPfeO4Z6V-wI7CaWMT0L-9efaWfNTZy0BC0bGh24i-TtF95ab_VY744SgryqD-vbNNaOg9BtNnxK5Rd6bBlvvufrYDpJrOFjIjHraPARhQjhY3Ortat4iUvPM27hxwPcblIGblwzFjuqndsnUIru5UUACZ_vNyqY78hS2Tk17ATRcv_A6ZKni9gfkwjIdMGumUjN5fJpiBRbOI7rF7g5J3-lf8TrJ8yqQdq8ki0GQ5WqPd-uGY_pCufKOp7KUCFt-sNAj23f60J-m0tGd5KHxXZmgYZjpcULgdYWcgbK-wJtepciRxr5j4GVWB2MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26564" target="_blank">📅 20:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26563">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2409944d0.mp4?token=CsxeBvJDYxqOIaa-adxfOXxtz_P1g2ym7VYUwFt-mK7jPDRSJZSJUKh8AilR82rbkrtMZmehY56Pc3oSNvbJplPECeub_YrjKGYm8AqIy1L43h7tBc9cIT0IbBSe3Ba1xQJAbnc6bYTIawVbO0SRujFwDCnCdmRCQYhAeFEtNL8SnjyDSUtDuv6HpeHDzs-DN5Vlkf5GXzGlm4sD9MucY7QFeqY0FFCI68nK_5nXv84m_YnBsdRBbQIR2JyydA-WK1xQNt4YUqsG9IGGJIkGXSy0ph5g1duu5f8HcbZdA69ayYMvVwN6nk3BCDJOhQyjx3ObPbKicMhWWznEXofPvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2409944d0.mp4?token=CsxeBvJDYxqOIaa-adxfOXxtz_P1g2ym7VYUwFt-mK7jPDRSJZSJUKh8AilR82rbkrtMZmehY56Pc3oSNvbJplPECeub_YrjKGYm8AqIy1L43h7tBc9cIT0IbBSe3Ba1xQJAbnc6bYTIawVbO0SRujFwDCnCdmRCQYhAeFEtNL8SnjyDSUtDuv6HpeHDzs-DN5Vlkf5GXzGlm4sD9MucY7QFeqY0FFCI68nK_5nXv84m_YnBsdRBbQIR2JyydA-WK1xQNt4YUqsG9IGGJIkGXSy0ph5g1duu5f8HcbZdA69ayYMvVwN6nk3BCDJOhQyjx3ObPbKicMhWWznEXofPvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26563" target="_blank">📅 19:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26562">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uc2ZI-TxJT12-YSq5Yd7jQpDt9SIsEAsZF785Q9SgoMatqZEeTb0dJxzyqmhAT9vEyzqiZXChpRPwnX4ZUv5vL1EvZsH-rcU9qXTFCcez1bL9IrdiGFqjP3iuc1320fEeOVp9nSw4nn7dsnIC4ExKQmllfZSRHUg6gEMcpKOOxm5i8aa_loLU4jLMNDaTFxzLf3fviAd03XUb0JpYXUWhVeAbwClPoubvsPeC0Nm6Yu1XM569_YDMABFe_9eQP7uX2lXfmaJHRQ4tCcAbjpukJ4QuZCFkiwmpDCJZuAwbvBsRSneWChqFeGForS2rxJk52aN1H_OSBf5szlzSe_fiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ طبق پیگیری‌ های رسانه پرشیانا؛ باشگاه استقلال پیش از شروع‌فصل‌جدیدقرارداد یاسر آسانی رورسما تا سال 2029 تمدید خواهدکرد. امروز توافقات حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26562" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26561">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66921272ff.mp4?token=NgSFK-P0Yx98AxLRBhk_H4KkabNpyWMBETavoi211W2JmMiMIKd4BHDCmfawOx6VjTZ-V67ZXuKkTbbo-7WZEZ9S4kJMOKVxC1YHPX5AUNOEhJKpKIoAerptMRdmh0VCHEHeC4i8-yY6_3lE3jmPcjXU7uruu1km6RtYWfw6xmRozUqp0LaNoG8ZawHqLrcM6kZocuj15Dg6rjht-2T2HRpAmb0sLQzA2ge6ztX_vJqvwP0MNt_ELXfS5QQCVZ5jPuVRSkuAbg0GaxHBWBuf7rGW9uFwgRKZBFyAwg-UO3OyZ-UrbMM7X-NT-Rkjthx_zSx8WRLDd9lxRQOKlcXMxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66921272ff.mp4?token=NgSFK-P0Yx98AxLRBhk_H4KkabNpyWMBETavoi211W2JmMiMIKd4BHDCmfawOx6VjTZ-V67ZXuKkTbbo-7WZEZ9S4kJMOKVxC1YHPX5AUNOEhJKpKIoAerptMRdmh0VCHEHeC4i8-yY6_3lE3jmPcjXU7uruu1km6RtYWfw6xmRozUqp0LaNoG8ZawHqLrcM6kZocuj15Dg6rjht-2T2HRpAmb0sLQzA2ge6ztX_vJqvwP0MNt_ELXfS5QQCVZ5jPuVRSkuAbg0GaxHBWBuf7rGW9uFwgRKZBFyAwg-UO3OyZ-UrbMM7X-NT-Rkjthx_zSx8WRLDd9lxRQOKlcXMxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
حضور جمعی‌ از بازیگران سینما و تلویزیون در مراسم خاکسپاری خدا بیامرز اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26561" target="_blank">📅 18:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26560">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhS3qVj568dEyzXp5GUXdpGOGFOU-FK9Lc9qG-xqQg6y-fUbWIWFEuLGdLw8cg2be_8Zffx9i4qwH2sS2rF3_tfzbFlx14nljlkBrexS8GWiK0NKif5Q22uCYqiKsKiegCjFirQ82kCtpu7t7_KbFloHd-NhFFTowss9pfbisFDd6xPanVk9acg2ehTgLEVTSJLSgNLHg_7R9kfHyGRVdrzi5mmOV9VnP-8xZR1cF40t3PrKxwmKMmTXNTa-bT8869jxpJHCCkPMQ3NXX-bJ6lYqgVA7L44fSvhPXXb947YUQdowLCjVG34kd6dUf9m-mRAFFvxsf4A7W1Jxvt3h7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از دوس‌دختر لامین یامال پرسیدن‌چرا نامزدت رو بعد از پنج سال ترک کردی گفته فهمیدم لیاقتم بهتر از اونه و منم حق انتخاب دارم و انتخابم هم یاماله:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26560" target="_blank">📅 18:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26559">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSKibnln_iPrF6QAOKJxtnjKVQV5lxnHfJdQg-ywK-TFWpU3oYFRkfz2gVs4B3LtDPW9CWWNthnAR-IpKy9IkVz8Pm1B4HsOTlNSqm5AdIxdeYLnLnGNKr9hYrauFnPkFUteB9yU6WFL2OdkcNxEoEzDDcoWCYhgH3RozE6kdAT4PCkurmKE4JjNCDE4-wEHeRMkxT10VM161q_3yrnVpnRsxxQx1xUizBdiWH0Jsdc6SUC3d39tVeGMCp_OHL1Hbj0S2rpAsrM7CWGz8rx5_zjYYDC24nL5aK8eqOJyypq__UGbDcXX8ewyqg4L9qUa0nxl6kOci6CvsnoJCRZjyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26559" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
