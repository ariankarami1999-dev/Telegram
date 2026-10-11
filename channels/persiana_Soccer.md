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
<img src="https://cdn4.telesco.pe/file/K0qX30OC7phT48fjn7687RXAAkWzZ5LKuOEqJIEpCmAfdIUlc4TihmqTWyXaq2zxDKMtgiysQVxvbv3GY0TNS8lTU048qiWxy3APzN0ASFkr8vN8u9FO9xqNifZzTpT4sB410sFEQ5L27rP4z1Wu9VV__hikT3MInoTZp0vxQPFcEG69L_W2rJmzMAHrUyUa1YtXeAFPDdXeaGhTjZbLq5ZIdSQmGshYjwykIMBfCQnHhVZGRJIT8CI8leXoUffyYAmPwpGfoGvwM555n1HMHBIKks51_g9nDWMLlrUErFwaTdFlyDibr30ka3uSTGz_i1hQFp_6pRdDD5Yrr5MlkQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 486K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 09:34:16</div>
<hr>

<div class="tg-post" id="msg-31355">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNrkb6BuHVNcrao1bdFVB5uWj-gF30bsOhIHJcqHimrMLr6oi9kIua75tvgenCy-sZnbVZDEK-DPQlA5KrasVsNErinYgGgyqUYwSLUHnzz3aJXB4aHGnr5-rDpvx81OoJwOidCwhzKKRN0mK8j3sPHXp3qRzMO5tXXdwCrP5eQonqs6RMmE_-iMvUAG5j77jMuxyQrDEVUrK1GKcHh6WpKrXkrnEYPP1B2hRjzvVH7drehXoyZeyXtiLqMbryKN_lyC3OsRlS0jN68sywGnfD_FaQ3mYhoDUuHrWE1ZG3ATVyFXcpnK3AJDXCcJqxOi5nstAO_Nog0hgT-FDJQcNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
بارسا فلیک تو این‌فصل: 9 بازی. 0 مساوی. 0 باخت. 9 برد. 39 گل زده. میانگین 4.3 گل در هر بازی. بهترین خط حمله دنیا. صدر جدول لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/persiana_Soccer/31355" target="_blank">📅 09:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31353">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa22c27bfb.mp4?token=aDr2jm2U-Gqg8Eu5GLPYGsGWgWXJXWtgM7HMhZ0gBTSjiWOx_vEbsNZwH1csLHc88X6Scp7SeEkcVCp3dTlgCbEpEBznsPiX4VWODH-d9h8bI-b7Ixog36IkjV6LUK3TB1IN-oPEoC3T-3Qe5pu8VmByyVXywEiCy40VoSIuNUovakMVYZMlixnqTJYrGrYgAPV_75RU0YfeqNCxxzAWKpMvqkWIa2Cmc4rJpICMhMoFp21ycynzlwoGolijT-hODbdpvCBkoSP9K0zJxtpPbEysgDJvWhSTBjGqmMyyVN8WC3UP4kmk64vaTA7mszG5n0BtyXMOUPKR_nPxSe1dUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa22c27bfb.mp4?token=aDr2jm2U-Gqg8Eu5GLPYGsGWgWXJXWtgM7HMhZ0gBTSjiWOx_vEbsNZwH1csLHc88X6Scp7SeEkcVCp3dTlgCbEpEBznsPiX4VWODH-d9h8bI-b7Ixog36IkjV6LUK3TB1IN-oPEoC3T-3Qe5pu8VmByyVXywEiCy40VoSIuNUovakMVYZMlixnqTJYrGrYgAPV_75RU0YfeqNCxxzAWKpMvqkWIa2Cmc4rJpICMhMoFp21ycynzlwoGolijT-hODbdpvCBkoSP9K0zJxtpPbEysgDJvWhSTBjGqmMyyVN8WC3UP4kmk64vaTA7mszG5n0BtyXMOUPKR_nPxSe1dUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
تفکیک‌ گل‌های کریس رونالدو و لیونل مسی در مسابقات ملی؛ رونالدو 146 گل در کل دوران حرفه ای خود با پیراهن پرتغال به ثمر رسانده و مسی 126 گل برای آرژانتین به ثبت رسانده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/persiana_Soccer/31353" target="_blank">📅 09:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31352">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDk-OMtMilRZRO98zzEHrSvafG375sZ8fUji665fDPWTe9wTI24IIyRrhBj-u9GqpUPIrkua9rG6RxFNpii2KH6YbYnkO0g1sDHds2U54xB2mrWgCQ9hjZb-fAaNpf6-JNsA1MiW4QNK9Oy4WCNQ9ZoScDcJCtsKStVQSAqPUVfcM7ETrkWx8yQ2I78lSx3yc8pKXNbTeFAdZkETvAFwrvqmoVAuKq-41i1f-GHUfxfub1WTiI8KUmRCQSBT1C8fobECUQLtDqtKHbdf3KLETuXdDGtXahhpGtRzsmwSEFve3aFV_lzdj70WEjB9gEyDTDKAnOzkQumA-1dtDaZK-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛ دوئل حساس لیورپول vs من‌سیتی در استادیوم آنفیلد بدون حضور پپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/31352" target="_blank">📅 08:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31351">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8zj70A_6nWf_2HyZzCpOuwZv6ZJhYJWOln2gK_Q1Y8UgqWalr_ytOHCHNihqQVQjNipaQqgkD7Vj6VyX-VxhC6Sw5grfmuaSPzLSiNgbhROI3_A69zp4JHbTpNsMYxMXdSLyWBGBJrpprbVwv3ICC2dU3U0q9JnnehEsmtmyXL3ItvLMDmNMzSaBhMkCCdfLUV-IcewLEQf1QGO9jPI3Ru4bVVHk8OhphEK6vwWPexrWDfIqHJJM-0CQGrcCJG5Lm5ktB00btf4pBGWzwFWRsxczWcmJVuHkZShkyR5FjChT23AnElguMc7ZlnQmck1KClk3OA9a80f_GLvnsYD1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
از برد خانگی بارسلونا و رئال مادرید تا دومین تساوی بایرنی‌ها در این فصل
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/31351" target="_blank">📅 08:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31350">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1KzKlBUCaWcLi_RqYRmB9V4ILL4lovaR_QtrULVOpjkcVtxfCYa6pX88b6zAx35VeaAEufl4LS0IM6Lrgk6Vh6VHAsh31jiqFScWVgxL29XPSD3On3imjaxGdGrNYnvungB1KLitCpV413nZCCDnRnsFIWgfp7363QoQoYpY8SsSPjMLViktOGdP3KLIsrGfRXM0wwLmHTY1_t1aZxsON939YScC2UzZiZ7Y5FCn42zztJ4vtNvRbSrJ7oYE_zVYjhbWaAJ6_CqLjzAdxpOZE3Zd65B6VBET095pQtk2fbPQAOLreS7l87E1L0Ho050OYX_NnOQVe2KqhRWNIvkOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌بازیکن آدم بشو نیست؟! اخراج وینیسیوس به دلیل‌کشیدن مو سر بازیکن حریف؛ وینیسیوس که توانسته‌بود دروازه ویارئال رابازکنه با بازبینی صحنه به‌ثمررسیدن گل، ستاره رئال مادرید به‌دلیل کشیدن موی بازیکن حریف از زمین مسابقه اخراج شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/31350" target="_blank">📅 01:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31349">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2B_LIbMtgiMIDdLM4DBOXWB4eJ3vrnYZX2yS7d0Eqh55ii08X7GlGnzZXlgEk9IFTBifLDGnFNUV1Cc4sMLlli24uvyMhBgJ4aEsoQFm5HMUyx73Ym-_ZMmrGRWsvp9uzjbkCeWwCp2mWZKIIwyGqP9UwETQzLO9-MKD1PWzqFCxejj_Zi9DCPMGsyySv371wOo8D-AOV9afFX10iyiE7L3xehc06SJLQKqJpz6wSE19bUZGrsfV4qtwN7XMdFde72zJsfT13zxaMuyfcPSupaMA1R6Wdw-__9ckvmEL2tvkL9-UpytJTQEyVnK8LIVQLTzGRaAy4avGDfcxfh2ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ پیروزی سخت شاگردان مورینیو در برنابئو با تک گل دیومانده؛ اختلااف 6 امتیازی با صدر حفظ شد. وینیسیوس ممکنه به خاطر کشیدن موی بازیکن ویارئال دو جلسه محروم بشه و الکلاسیکو رو از دست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/31349" target="_blank">📅 00:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31347">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mEyp7TP50v1m6cikBHno_wvn-tChoYA21nxkQ1T9T63ebEYOpoT_IPP_ULmAIYinZNmvtOrb6_DoHbhlAb6NLi6D2eKr69CLUjNvWzIoWo5C14c3dylW4iHJznmqpQ3k16JDJe8UGdYU_MRHAp-djGEh9jjCXOpdFqYTltq9-l61BFzn4kU9dSQJxsbzqsyWmnOdQNVsQ0vFcOUemjNoY3QEDi4-JNCpw8cvvyejUdcoj54gtQ9JdGxWiHtSv6VYlpJdX9LiVIzTGBZYcueu6TC0oy3H8hrctHPoa47klsvW7rfltQFN-njQPFyt7UQoNRUlrLh8iGlQjeI5f0AQdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GEW-F1teniccTQIalmSv8yC0vYyTis3LBV_MOst-veO1pp7pio5p5XUheLVywL-XadFOTxyPRZOFUtG9aeQc1h_0QVIuKQmfvRlwiJiLdqMQOCFmnD2loEPzxjymYmgOyhGuegsKrhxD6avALF6_3bDcCYqUrs42BfCtEUf32PePNsmiRgBUX2SSx_kYVnvB0xlLXDhidQDbXTCE5jKf1pJMWBMsTiZyt0y-vp5eGMmCk_sxhAnWYzHaxD77egoM7X7hC4sO7tf3S-UZ572TMI9_RXfRUkdD9ck45z9MW2g5T-4gHBwE8GdEqlkIUQi8-7nbQ-uEaG8kphIjbQeThQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
این‌بازیکن آدم بشو نیست؟! اخراج وینیسیوس به دلیل‌کشیدن مو سر بازیکن حریف؛ وینیسیوس که توانسته‌بود دروازه ویارئال رابازکنه با بازبینی صحنه به‌ثمررسیدن گل، ستاره رئال مادرید به‌دلیل کشیدن موی بازیکن حریف از زمین مسابقه اخراج شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/31347" target="_blank">📅 00:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31346">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFCYTc1fZNuoXanWVlLpgRg8atF3t786yUj3B77E8Zh9yenBtWzq7UofDvfov6ZMHBnHnFN9lOHU7w3X6sFrdhRX1TrhNl2vQNzAW3sB-45V79pNej8udqjJ3-sRM9YBoYgH5uCtdFgtjcVoVH0RLucmj8aF39lXxwzyPJAZgsDC3cJsrpGQfMKB7otz0oNEOg1m1pBVauCgzWaXN7u2EaA8JEgd7qC3mUZ-bmUnVY_WiJIJf6eF7Ftaf-pczolRMsD1wXkMqWeDo8sftuG1W9TRzTOMNR-Xryj8dQyJ5HrKOWFHrwq8IdsU-t6EY6bUikYvHoXtJJehmlbJJa1fNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ شماتیک ترکیب رئال مادرید برای دیدار مقابل ویارئال؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/31346" target="_blank">📅 00:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31345">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crL9JSAT2SzRYiWF4hR1GzxQNmCM4YJf2o8sIutnvLqzlk-pvUTLh_pqNpIEJy6uWe-DuC88bbUb9t_jjVyaPt3Z_FhgUGQ7tWEPIoIMC20qNKJF822MCvBbCUzbNAMBhiQCd4u_XnCWgS5_aBTvcTJK2eD5JImdD2VnUwcB9UF0p_EUpNhghEzJJ5LtGTUPQp6EheLUQDLSTtxNvyZ6uWlSTzffpkn2EiovyUMxYATXVtDl3uqdmqm7DJ0N1GUpp4nDPwd2IBx6lIlRi5QUVFZEUJm8EWQG2ElhxfbeVD0TmZPsAk9W40N2wxeSXyfUm2HAzYYr4EfkvKi8M7rTPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برسی عملکرد پرسپولیسِ مهدی تارتار بعد از انجام هفت مسابقه در فصل جدید: پنج پیروزی، یک مساوی، یک‌شکست، پانزده گل‌زده، چهار گل‌خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/31345" target="_blank">📅 00:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31344">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRbrVTbZbCVywcvVmY0vNq3zz1xlrDYbR9szMt6fIXRKTXN0P98-rrlhoQWGIF8aOWMX53yfKVI3aN5cQ_nmgsAVng6OymE17ntPycPE-Eu1WOZYcuwUpn1q4cqTl6T3KwbloDpml4rINA5TS7OOfAXjWIOM-Y3wh24s0SslnYnoDF31sUOu8QP_KcbwWhlq5LjT-YGWnaBJTGE-uUXlNdgqLtBi8VZdvfK9wAMlEuwFpVXat401iMtPM44JWJx1ueoGe0wbsAqopcwoS-nQT6cUQ9Gkmt3NU_Iv-3cv9lSzzr_06YaMEXT7m6pKEgo822d46uG0spHHLELSZ12s-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ یاسر آسانی ستاره آلبانیایی‌استقلال دیدار روزدوشنبه مقابل تیم الغرافه قطر رو از دست داد. این بازیکن ممکن‌ست با کاروان این تیم به قطر برود اما قطعا بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/31344" target="_blank">📅 23:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31343">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
👤
برسی عملکرد پرسپولیسِ مهدی تارتار بعد از انجام هفت مسابقه در فصل جدید: پنج پیروزی، یک مساوی، یک‌شکست، پانزده گل‌زده، چهار گل‌خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/31343" target="_blank">📅 23:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31342">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTC24tUxzaNVYF1ARNgVJ-ZkneRHHer4tRVN-0g9Bd4s44YKwNy9-vspDwo8OeM1o5h1dHKkK_Qmx9Cej3jKXxG7Z33Nbb31qwjlQLyzzrLpbBTThRwDDXT7r_n96cpwbCRW9uBaG72_fzOo2XNH8miJkHF9XA61QrnuYcCM46UzfrdMgiz7zkt0NkfQXFAtZaUxpGuQNEAZRvY4FfGNNIGiN68h4ZRR7oG-KuJpqn9wyBacR2B_9-4TN5tgXMj9RjRAuwjSOvbbOBJM-FO7AbAS0aoeWyKhXKvWiypUWvwRS5eBUmW7XGeH7US8p_oWua1YEujwDQsWblUGTDzTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گلشیفته فراهانی با جان سینا فیلم بازی کردهه؛ چه لبیم گرفت ازش. الان دارم میفهمم چرا حکومت داره تلاش میکنه گلشیفته رو به ایران برگردونده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/31342" target="_blank">📅 22:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31341">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ece2dc9b.mp4?token=nON7j77pH13fW4td4UQ01M7U7Cja96Y2sofG8XZAD5s3Z1KegKiGXbhQBbxOJrHObNuRa3dx8kOVFCUscRWHl2g2v35DL9C7a8Zq03Sd6VFVFq2uigTv6xkUXurc7O54cKu8gcdDmZKB8uXLcH3xxrtzShxYg41ErrmOlu_rc5tm5MYq8GmbM_G968nIjIuJXcGGgGqwJ2I4eEVOQfOFKkF1gdXn6Qjh_OL7kPHeInVnAjSJlwj7OreJ43_LnN2uw8fW-VA7EtzuZFR39yj1T3xLskzrdYO7B8baEVwZH4zCa-_u-BE-4LqC-gyYYyv9J6ZWS_usHU6dTpERg-P2EK4CUR7w5ua0H73leoYwk2iodZe5gA30Ngz3-Fa3qu9TOZF9lwqm3BiYfn1RRFwpj_oLb1dudSkALg90ZZOcZdqtSTkhZCrzXDJSKmO2fzeaUgptcZXJ5klXUk9FjR8nbVTLHDKEN20bK1RnuXNkY3bABvxgOdNlxsvvqGlEaFXYEpQ4XVW9yNtoJFwt-K_58Gl_FFexg65oczL-DBNdbdWbcwQOqy3uD7aNuIgD7j4T54a-dxswmbULkChq3C7orFyLO0oaITxEOWYVgaqpO9JXK92bwRaTtCloKz8oEmkzZD0a0sZQ0sWHl0cRv6ZuB230Ihl6MEPd6R-pk8FaON0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ece2dc9b.mp4?token=nON7j77pH13fW4td4UQ01M7U7Cja96Y2sofG8XZAD5s3Z1KegKiGXbhQBbxOJrHObNuRa3dx8kOVFCUscRWHl2g2v35DL9C7a8Zq03Sd6VFVFq2uigTv6xkUXurc7O54cKu8gcdDmZKB8uXLcH3xxrtzShxYg41ErrmOlu_rc5tm5MYq8GmbM_G968nIjIuJXcGGgGqwJ2I4eEVOQfOFKkF1gdXn6Qjh_OL7kPHeInVnAjSJlwj7OreJ43_LnN2uw8fW-VA7EtzuZFR39yj1T3xLskzrdYO7B8baEVwZH4zCa-_u-BE-4LqC-gyYYyv9J6ZWS_usHU6dTpERg-P2EK4CUR7w5ua0H73leoYwk2iodZe5gA30Ngz3-Fa3qu9TOZF9lwqm3BiYfn1RRFwpj_oLb1dudSkALg90ZZOcZdqtSTkhZCrzXDJSKmO2fzeaUgptcZXJ5klXUk9FjR8nbVTLHDKEN20bK1RnuXNkY3bABvxgOdNlxsvvqGlEaFXYEpQ4XVW9yNtoJFwt-K_58Gl_FFexg65oczL-DBNdbdWbcwQOqy3uD7aNuIgD7j4T54a-dxswmbULkChq3C7orFyLO0oaITxEOWYVgaqpO9JXK92bwRaTtCloKz8oEmkzZD0a0sZQ0sWHl0cRv6ZuB230Ihl6MEPd6R-pk8FaON0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
نتیجه دو مسابقه مهم امشب؛ هشتمین پیروزی پیاپی و ارزشمند شاگردان هانسی فلیک در لالیگا و تثبیت صدر نشینی و توقف شیاطین سرخ مقابل شاگردان دی‌زربی. مایکل کریک در آستانه برکناری از هدایت منچستر یونایتد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/31341" target="_blank">📅 22:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31340">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇪🇸
👤
نتیجه دو مسابقه مهم امشب؛ هشتمین پیروزی پیاپی و ارزشمند شاگردان هانسی فلیک در لالیگا و تثبیت صدر نشینی و توقف شیاطین سرخ مقابل شاگردان دی‌زربی. مایکل کریک در آستانه برکناری از هدایت منچستر یونایتد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/31340" target="_blank">📅 22:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31338">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXK0jGiHbTqhSCMUm_LJ4U5ip5uGW5NsaNyS207xUwPWP7d1CPcuAfFYcAbiv4GclRV2DIUgHpeQ1pbl1HvfjiFus60_FE-w-lgziO2YmVuT7d_nDFj-1qq5tfxuv5bour8zSiObPvg41XnWsmUTlEeKFTCk9wzP2PZHYnsiSjEqJbPhCbHuBpmpp7V_R9SPqJuYoIQkIH9QmhWEutFDdSc3E5GPqX4RoNasouEaJg0aoiKeSxlr3S_7alifyqtWQlFSwXdXTB6RfLgHsLh0sgk7ccl2fuqZSB1J0CshLdyFDrkSRrLXttYJ07-tsPuTtNna0E8UxNHr0VN1c7VjbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/baFcdfkpW6PDV093A60nkHIRwgJQNKXnCSiF1tcjaC5-c7s3paU9P2NTQcIhYQWR6CuQQpcXlNxGeENYLqCxxGujr8czzL2WhZYQ_PQsJYpIbk_pRFTRByXZ0Q3hZXFrqmOrIxySO6nzc7dF56zdirjUsg3G295SWzhDS5br7I_LjalOVZpDrrxfXyDIdkf_dbieokRu4iSrsNqUnrYGGqmn7VVxUR7r-TfeeCpnb-oL3kEY2ljVk3nTVjdaBsZq2uKcUQ-IV6kmO662WWjDswaoD_vBd4H7skh4OtbEy6k6v1AJFRfJNS7Q0CLUtUswyiaCQseFCVXXGA4QKMpSIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته هشتم لالیگا|شماتیک ترکیب بارسلونا برای دیدار امشب مقابل ختافه؛ ساعت 20:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/31338" target="_blank">📅 22:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31334">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m4x6ymjr5xDw1ye1_4VvZFXiB1sJoi3tiravP2ozZLI9ppaXBZlkiLmnUW1DqQkJY2VmBadxpd4-1-mjrOhBXh_GI7gJXeWw2eApXhrYN0wNAYcRaHnpad1ReWExS-SQhSSqgIz30QvAoyG2VhJMpCYt186AOdqtdWqsyaveUTeXy_-Rd__Kx12LJeTK1N240oVzaahC8S86wsvSa1lu8-NLv8HbsxuOEVg-t2SGNizD-kvC5fk-88k8YxHkOaeIPsvqbvNMXnrHO080tsKra-dvX2DS3wflyWUcoEdle60gNM6IRv0zFyBYlIPsO0JeiFNE8R22FyVg4In6gkemkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bz7snkM16oxFKKLj5yM3J0UvDzEx_JDyV1f864uTofuXjyKS3B0IzQFHvpg_2gp2Lqy2XhzlYbCVIyoePTb9HDHHAWtkdqaabW8-zEnJ03BEnT75u-sk15wzfjTR8zcQEjMkHdC2HWtV4sorzcfQNY900yaOYBR_cKJsUdcTIgT7DRiXe7yfgkgPHcs8hH513R8no4_0MeKZYhFRV1biQcHH-JGILIuvR29pJeNBMZ9fSc_d-wQgsZDr9Fom_AD7AfyrRqHUcsg1cEY2XAWX1LjR5x5XA-HhWc0NZL6r4h2uevp4_T6v5nKl3X61BRyHsHn6cVoNUwKMNEFu2fA2dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ شماتیک ترکیب رئال مادرید برای دیدار مقابل ویارئال؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/31334" target="_blank">📅 21:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31333">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXDCZ01sc624yA39l-9NqYM6z7Wbb4DJ0u9m4Nv8OcStSdSX5JSZQxyhZMNaiThEytMgEb-09GyTU2K-FzRcP275e0ERC1kJlJ_oLClmDWaJgVcLEYJdEJcLLvprn1y9D4K2cs-0POg0eThDCwNhKy2PPRypD21--p_eRG0uSHwU8pmAL2g4ZKMc2xOKxhZ2Hp8hDyk-H_nvgIu-VR1MbmP60BdICKsfrkAHQML6FSm0V8tC6Nm1Ny9ZaK6VjJ5iEyinasLRHoJqt5A2Ou6cNRuj-lrZBgh9D81JBIuLbwWIFpfrK-XwG6vE2yu5wpz0On-XqrHAda_J3AXFQBVRAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
رسول‌خطیبی‌سومین‌سرمربی اخراجی فصل جدید؛ بعدِ شکست‌سنگین فجر مقابل سپاهان مدیران این باشگاه با رسول خطیبی قطع همکاری کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/31333" target="_blank">📅 21:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31332">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsjCExMJYr1uVZl9xzscOd3A-KCyfCg9w1GLDmN1tHAoIsCtfG7qreWk6bPRVE0mQCLFtQAFy7PzfkveYRUouT8AaNbq191_peFCETqZdD8eEUcynoG9ohFmK18T_O10MkatVBd8ovAnnxPRf3gQUyBHHlP_h5xg7p5Fnr9zk1VDq_ROnLfJ-7XIRsfsUlaJT0tQvvQlVJNxqVJVbguuTE7Dso-AdLslB3RRJLMPoF4rJayhrBlLq7_guelbFO-7HkZkWNUTz3ueKbUYRJvNvsjcWV4Fj0lhPjD0YPs95O8nrWa8hglviHLL1S9AVHj98q5ryJDGZSM9p0peYg16jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هشتم لالیگا؛
شماتیک ترکیب رئال مادرید برای دیدار مقابل ویارئال؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/31332" target="_blank">📅 21:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31331">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd28a51cb.mp4?token=gXL95scwHfuUj3E860Fc-scmsmsgz73vN2nWzeoruuNvWQ3qDtDvSwtIIR17qumJHeYIgmL5cZKS8P-IE50zJ-Vk1WIuE4e0--5tswBOF_cPTpLcgG9EFzPLKnE-0td0_aHQ8QX2lSiuNqdMw7DAK8lbXaXvRMSj7a3lcizO0auLI_6yEeRCae5BpeUqEYZAwHhB9TnRhQskwdJbVvD1p5gV4nvpexIsfa282p65bN06etX6FGPCq5yD1HMn3a2cI5j3OTXqnabGf_S3mEr8RzMFQt-qeWSWw__mSIMfnMLu8Pf683X0-RKWADnBHjYodrVJunPUaCN1QxY8dDyTUEDGLfpAAgL9k2zGAoWYQF8v66N-5TsGErEW1rBPeRU0pM3K_RsY0GM9neS2ng0yr8-IYcAufUyMduvW823euXtFi4vM6geNrPMnquwc3qa-HqPE3w553UehFGlnQQngFw2zlFhioK1lSdFoCwsQm3ddWa5p08amCGW758cQvsHfZEaez0BJweXvqYCMO908iVDHNiNMiCr5bRw9eEzmayy1-IMenOqqCY1ZI1Hx1mVjkxjRkV25ZpRa9im7znJ_tnGIoxF8_45fWw9Lt9NOAtPQSLupLckqKvpt9wMWvBLa2zQdZp1Rau-1zql1-XrBkylqp7-HNHU9xD-m1hrCJ28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd28a51cb.mp4?token=gXL95scwHfuUj3E860Fc-scmsmsgz73vN2nWzeoruuNvWQ3qDtDvSwtIIR17qumJHeYIgmL5cZKS8P-IE50zJ-Vk1WIuE4e0--5tswBOF_cPTpLcgG9EFzPLKnE-0td0_aHQ8QX2lSiuNqdMw7DAK8lbXaXvRMSj7a3lcizO0auLI_6yEeRCae5BpeUqEYZAwHhB9TnRhQskwdJbVvD1p5gV4nvpexIsfa282p65bN06etX6FGPCq5yD1HMn3a2cI5j3OTXqnabGf_S3mEr8RzMFQt-qeWSWw__mSIMfnMLu8Pf683X0-RKWADnBHjYodrVJunPUaCN1QxY8dDyTUEDGLfpAAgL9k2zGAoWYQF8v66N-5TsGErEW1rBPeRU0pM3K_RsY0GM9neS2ng0yr8-IYcAufUyMduvW823euXtFi4vM6geNrPMnquwc3qa-HqPE3w553UehFGlnQQngFw2zlFhioK1lSdFoCwsQm3ddWa5p08amCGW758cQvsHfZEaez0BJweXvqYCMO908iVDHNiNMiCr5bRw9eEzmayy1-IMenOqqCY1ZI1Hx1mVjkxjRkV25ZpRa9im7znJ_tnGIoxF8_45fWw9Lt9NOAtPQSLupLckqKvpt9wMWvBLa2zQdZp1Rau-1zql1-XrBkylqp7-HNHU9xD-m1hrCJ28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت مؤدب‌ترین و باشخصیت ترین مرد تاریخ فوتبال ایران ازسفر۱۸ساعته کاروان تراکتور از تبریز به عمان به دلیل محاصره هوایی ایران: پنج بار فقط سگ ما رو گشته. اینجا هم فک کنم صف روغنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/31331" target="_blank">📅 21:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31330">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1NLVIGL0J-uF8h3n6NoH6zH6fIAPfy26PvKz_cXxSBzplw5eOkBKn9qtThbJ-6r-ia5-JL7fe66mJNFWOX_0kboauM2kgjMa4uM0H80ahsmpROhd4EmlScJ9cfnDmkj1ONptNPdcWDMsAUrP8Iv45Bk8NycmkH4pck2LD_SCsBwvWzAAQ5HE5QSqQrD61gFBfz-UruY3th318g7RujX_zQuz8yF7nU_7g7mcm8D3tRx-nhTVCrN64M0JJGqqCpfFk0mqSQIB1WDGjjI6mYsO3q-InPxT-sak4fck8DCPXnI9K0Mf-m67wYUlr9Edq2kAUOKW6NkoON-pvbNJBntwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
فدراسیون‌فوتبال‌پرتغال موقتا کریس رونالدو رو بابت ترک اردوی تیم ملی این کشور محروم کرده. گفتنی‌ست که کریس رونالدو بین یک الی شش ماه از همراهی تیم ملی فوتبال پرتغال محروم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/31330" target="_blank">📅 20:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31328">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QQWz_k9qEn9tZzLogDoiYmu0eWzwBrK7-aXA1stt9RQoqqq-363S6Xvhg_bhcWnFX2KGXQJl9s55Fy1iqZ02RQwkpQdzAfjTzzCQX_aC9ez3DiAJoFeTueN6IixK2vMyN1XfoUBevORe4raeiaV_-CAfBT-fKRO9vwKFq5C6m7YZAX0JZlDAhO5S0V82eGtC6s6ZNGFUTbtj_p-ic2EMw527OWCuT7aAevuF3u711bDqncaDJtlT9Idd-uL4OsNQDikmfnBvxTdPF5cdjy_dVh7SZipkqgG9qWHf_mndVWECRlJFOOouqwnRi6ZsM3Lsud6PWfIijsiOJ-3uUJR1-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Alb00lRfurTh_WojyE6bXMfofZ8Z5AHCVXcjH8KL2Zkacp1GM6H-VJz3GVuUWj_BO4VQkCVMisUIu7-Y54q6QzDnZIt91rpsSpBMqdN7kZ2zUxF4ubH7DmgNNaC8Aa6XxvtlWIIuqkx5-NOhJvnzUNiPlhPhO3wPjXmpwBMufQAMA8UVWdU3xcBc_Yczqz2tVXVTvoAvJs-tKrCca-4yI4LZUY9Gg4iJtqvLgUbZ7A5G71fCAsTZGi1UY94bhESiRLieiYOjKzZT6ybMFVgPKixCvMznTgGcIF86VxDfv9puiWkxna8XsPTBks3jIy0n55ii7Y7Pjwc6YpQ-_dMb6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سیلی دوم در انتظار مهاجم سابق پرسپولیس؛ درنیمه اول دوم بازی امروز با شمس آذر رضا شکاری به این شکل پنالتی خود را بیرون زد تا در پایان بازی پذیرای یک چک آبدار از سوی ساکت الهامی باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/31328" target="_blank">📅 19:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31327">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🟣
درهفته‌ششم‌لیگ‌جزیره؛ آرسنالِ آرتتا با درخشش دکلان رایس و گلزنی برونو گیمارش دو بر یک از سد لیدزیونایتد گذشت و در رتبه دوم جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/31327" target="_blank">📅 19:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31326">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzcv_La8rzp1kk74PMjvrCWXIUu2_PxUqQ1bRPW3HzyQKO2wlDPnsVOar9xh2E4BvvuDofp9otoGBMx4CMB_R7XIJeIQ2Y1WYaNbLZUZlKd65M0fE7Erpa6bcCvSzbgs9gQo23jay9-jmdfpza8IY1VvZqmSqYZuT2upFOwSQXgLwfLoSNKO-2SAJ8NlKO94rfbrAmjCDsvpfJJCwDOoxXglMloOV_11bKDsgOKUfOktwIh4RRLUEMFnw3W5MeOGTHMK4ZV04rIyHDENqxmHRdkbizSRziySwUy5ltLigBsQgvjxdTnG4Or4rhrO6IFbjJs43A6FEMooKbrYmFeHZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلهائر زننده‌سریع‌ترین گل تاریخ بوندسلیگا؛ گل ثانیه ۸ رابین فلهائر به بایرن مونیخ با عبور از رکورد کوین فولاند، تبدیل به سریع‌ترین گل تاریخ مسابقات شد. فلهائر، ثانیه ۸، فولاند ثانیه ۹؛  هر دو گل سریع تاریخ، مقابل بایرن و مانوئل نویر به ثمر رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/31326" target="_blank">📅 19:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31325">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oz2iTteWPAexzV5bepEUM2e8a3FKgl3mQjt5xxiTkqhOy47Wm-cW_55LHH6ArHpJ7Idps3VUIgjyw5p1C7H4TnwhM7IFT45E65sLrgL8IbYhsIa_QK_mwRdkAk5jSIH5MYcn72tDWh8kAv1df0Tbgf6pucK7wnysNcmzFa0KQBZwB4Q71HMjAUpoAtOdCKrSM46_jJAweRcG5tk3G5dFWmFFH-2JHkGZ8XETFIORnF-shB1Ng3BEav4ILtt_QN3bor5bbuVVDRHPp3pc8Gkzt0N3Zpr0SbOEGLRfvAFmm4zGdecWzn0Zv66TPazs7HMRc3-m5sZuYdMJvB5xhH7muw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
خبرنگار و گزارشگر شبکه اسپورت که از فن های شدید بارسلونا هانسی فلیکه و معتقده که فلیک امسال بارسلونا رو قهرمان چمپیونزلیگ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/31325" target="_blank">📅 19:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31324">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSJ9FxsDOXDl2iUgPmJAgpXC3nP-Zc6oiLibAy7Fh99h-_PC3wGp8ZpFdZi-vgGtTtrEunL-Ks8fY81CS74NODv_vqXGvSv0lMfTHmePhkIykMFBP1sva3RW9w6DZJa77p9zvEBLy2rnFg5Om_CKy-hzy6G1DZxkH709iY6RQhKo4WWNjcU4uQB_VtqKHuPfluBfbUqV3zZi-i-9SKJySy0p_-KT6KPEPyCqn2XXHNSEASkf20Vv0RbMJlVj1eyNG-g0jqZ_9QCzvf9dsGUGanANY6A4jAfMO9sRBNPJWRj5vUf292y66zjga_b2mJnXXOkUflUQtPNVAi99Oqsj7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
خبرنگار و گزارشگر شبکه اسپورت که از فن های شدید بارسلونا هانسی فلیکه و معتقده که فلیک امسال بارسلونا رو قهرمان چمپیونزلیگ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/31324" target="_blank">📅 18:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31323">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5837e5cdb.mp4?token=pAQPOxXHSrpptnKNW_NyTZyuWkiX_F4xVSG1sEoyzq_jLP4TZdLHbgbLFIFHvNTxy3fXVUmJyuBTUaYTKMB18p6KanuOaa7uiuSjxArBxgNin9bLyZkUGFvTqMWS68Z49lJ_53rTQ8ttUckj2Plt5UImakgCqN9cL7vM7znC4o-mfkKGbdMGQTTB57XQcSKWkgczLGSnihV5Z2U6QAHOYZbqKQvWAC7CYHFQVT8T63P90Ggq5DE0Fe7U1HwJ1NNW-f3DqbeWvEi_3EbLa1Ukc6NL_Cw8kj4UhyD-NkIN-x_K1ycydwFopCrZA0XfOtOPkTtTjwL_d0_cRVwBrh4rrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5837e5cdb.mp4?token=pAQPOxXHSrpptnKNW_NyTZyuWkiX_F4xVSG1sEoyzq_jLP4TZdLHbgbLFIFHvNTxy3fXVUmJyuBTUaYTKMB18p6KanuOaa7uiuSjxArBxgNin9bLyZkUGFvTqMWS68Z49lJ_53rTQ8ttUckj2Plt5UImakgCqN9cL7vM7znC4o-mfkKGbdMGQTTB57XQcSKWkgczLGSnihV5Z2U6QAHOYZbqKQvWAC7CYHFQVT8T63P90Ggq5DE0Fe7U1HwJ1NNW-f3DqbeWvEi_3EbLa1Ukc6NL_Cw8kj4UhyD-NkIN-x_K1ycydwFopCrZA0XfOtOPkTtTjwL_d0_cRVwBrh4rrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ساکت‌الهامی‌سرمربی‌پیکان درپایان نیمه اول بازی باشمس‌آذر اینجوری رفت سمت حجت احمدی و یکی خوابوند زیرگوشش بابت اعتراض به کادرفنی حریف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/31323" target="_blank">📅 18:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31322">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfyJ7j51FAJLJJItlQKxDuh0_wPWTuHdCETN0EugtNlnOrt358FXbUCgnvLmi4df4koqawa9nm1EVQSF6YykaxX0UyfwQsKUze5o4eTLAZIbDW-T54_7ENcnsx5jerP6jN1SfPn_hkWdw5eQcr-wK2PucsqzSw3WDC7ird8ByTTkczWqTJVF2PYRXJFeooLFCt12AkKoQkerFJvSMxgGo-YawxBlsXBZU_bSxvXtS2nksUqTBZujTRbDRPz37M_UcXn6yaHPOzdTN08Y31q0iRBVNYG53iSoFS1pThAAdjgu6vRYnG8aRoxRX6BWLZRUv_EA1-yrSeelQzL-QXaqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اولین گل‌ستاره‌ ازبک سرخ‌ها درفصل جدید؛ گل سوم پرسپولیس به نفت توسط اورونوف دقیقه 85
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/31322" target="_blank">📅 18:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31321">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpzvvBGpAvUZ-47mM-q35kS33qTNhlSxyQt_QV0v9rNthHkGAZe62yz9okjEKzP3OT2o7dNQE8Qyr37c70u7_SESGEFIuNvAURdl19w_kMFR0OwxYV9kI53ldSz3piQYpCAS-P9gGEDn3i2H5200Ydqgqa1wmQIWZCASYf527FmbboRDm-ZciKsF3t5glsfSaYMT9gM4dXqrf_hXQ-fR2sBQI733w_k1a-jFIO-z-eYbr9ewNBvqxO7KhiwDExUVDTtNMQsL9t2Us6WbiHH0gte4L_bAMHlu761lKU4D3iQeYKTN1e4rlz2EFjMVsxXThDXw37eCwcDCyPFHLxcvSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G18
🅰
🛒
ورود به سایت
👇
✅
https://ieoruyxtsud.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/31321" target="_blank">📅 18:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31320">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGtGVUZI8BOugdslUYaXN1hkuIfcdikzrUghVx-7aQgWJBUJJjqyvxz5gLbSwVqHRNGTi1hsbGojKcQaAOfZ_hHKAvLpwZxr4lZKP8_Daowx7_uW01LoGJmQ03MEhuj1Af6hDceFecEshwzzSTF2Zc-Wlu5hhL0G4SHEccxGdGsbKKH0SfyjCf65kYj1Cd9-bPV0uMojJFLx-GxNm5CKkkUZlcsl-F3_c0MOcBhsITntdWU5S45CB1lZO5aE9UW_7XIKvXh_5cnH7L8hpFfoSD6s6D-Zo_eyWgWvOznx9FDpeQUkcGUnB-iAVJRR34zioatsr_upx0xUMqjnEY9dHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال:
به‌مامانم‌گفتم تو هرمحله‌ای که دوست داره براش‌خونه‌میخرم و اینکارو انجام دادم، قبلا تو خونمون آشپزخانه و اتاق خواب یه جا بودن و زندگی سختی داشتیم، ولی الان خیلی خوشحالم که برادرم اون زندگی‌مرفهی روداره که من آرزوشو داشتم.
تو زندگیم یه ملکه دارم و اونم مادرمه
.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/31320" target="_blank">📅 18:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31319">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17a54f38df.mp4?token=IRuAoQ-riCFv0YqHJhcL9Bopf9IYihxuvp9Zml_bTeFpAt0Qkw_emBlZks6L6XvdtecnNiPtVyawraMaZ5jfABxgPIKURb1TeeANuPYRoUUe2ZoJY5MWfYYjv9JsAuHYWDf9u4hW5JxQzyH6Zb_Mf3NRLTL5n6X6c7jCUOlhIsHDFc55jmfOqVz4iX2xGuB189D6O8iuTWv-kvSk6k27O38rnWl3G9i5w46LDNCyhuesomtyHFRPeT-ffcgULre8ppudO4neAd1CcvjHl5BticZHEwaGoRmBBmwDb0hrJIUAKOUlIIpL6RUKW_gboLoFD63vW4KHgz9xeoiJ1dGFSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17a54f38df.mp4?token=IRuAoQ-riCFv0YqHJhcL9Bopf9IYihxuvp9Zml_bTeFpAt0Qkw_emBlZks6L6XvdtecnNiPtVyawraMaZ5jfABxgPIKURb1TeeANuPYRoUUe2ZoJY5MWfYYjv9JsAuHYWDf9u4hW5JxQzyH6Zb_Mf3NRLTL5n6X6c7jCUOlhIsHDFc55jmfOqVz4iX2xGuB189D6O8iuTWv-kvSk6k27O38rnWl3G9i5w46LDNCyhuesomtyHFRPeT-ffcgULre8ppudO4neAd1CcvjHl5BticZHEwaGoRmBBmwDb0hrJIUAKOUlIIpL6RUKW_gboLoFD63vW4KHgz9xeoiJ1dGFSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
واکنش‌ابوطالب‌حسینی به صحبت‌های اخیر ساکت الهامی سرمربی سابق نساجی که گفته بود در زمان حضور دراین‌تیم در رقابت‌های لیگ برتر حدود 10 روز در زندان‌های ساری تمرین میکردند.
🤯
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/31319" target="_blank">📅 18:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31318">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e05ef0c40.mp4?token=t2pwqjEoKp6Bwu7rd-oDPK11xQOZBGkM4OW5Z0HqsjewbIsSj8ej91-ohZc1EulD__wEL9e7Snry_2CxiDU4BOq12giOQ-74tEniqtSBU5T9tZ4ggG7CF_ShfEqtuks4mWbJ0_fvOmXlYdDhFXGHj7_2yv0nttXYM0MBBdpXSg9BIl1A03FzrMZAu50ze1ySn8_CgPwkIlBRyIztEzRsyhAifVX1WNL35a94xmnETJgWjWBds3lur8CjriZZVb7vM193TuMVRDo7JeGd2j6xfVsAxh9jJ83DrlSoPD_cRWkjQ-yGO7woKBwdE6uvk_2zvHmP3OTn3cerf3cLVNB4TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e05ef0c40.mp4?token=t2pwqjEoKp6Bwu7rd-oDPK11xQOZBGkM4OW5Z0HqsjewbIsSj8ej91-ohZc1EulD__wEL9e7Snry_2CxiDU4BOq12giOQ-74tEniqtSBU5T9tZ4ggG7CF_ShfEqtuks4mWbJ0_fvOmXlYdDhFXGHj7_2yv0nttXYM0MBBdpXSg9BIl1A03FzrMZAu50ze1ySn8_CgPwkIlBRyIztEzRsyhAifVX1WNL35a94xmnETJgWjWBds3lur8CjriZZVb7vM193TuMVRDo7JeGd2j6xfVsAxh9jJ83DrlSoPD_cRWkjQ-yGO7woKBwdE6uvk_2zvHmP3OTn3cerf3cLVNB4TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
درهفته‌ششم‌لیگ‌جزیره؛ آرسنالِ آرتتا با درخشش دکلان رایس و گلزنی برونو گیمارش دو بر یک از سد لیدزیونایتد گذشت و در رتبه دوم جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/31318" target="_blank">📅 17:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31317">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/He2EK6W_eYLfXR_dGAyUxg4U6dq_bHaYQHHry7kTm-HUnIXThX01WcO9ltu33TXiBEhWtw0cl3qqOjsecAsHKjgDvMpP_5fKq_GIMlOEwQ1go6aAs-E-tuzhInf-1gHssuNCOCRI9fJxsBdPvke342gydzV6YIC_j27c403TVSiY9JQInYDq7m4rEmiikxt17x3w-jnpL6xotJNKHH7fRtXxxN_vgtz26HcdOuprq5fQVK8U-ZMOO6a6NosRw2J-taIiI_Yrd8qxBsPuWAuPadM9QJaGAtnLIdqEjkRzxu78rYb_U5FpnrV9qiSxgSRzS4oU6v5QeDjWEeVsmiMwSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ همانطور که‌چندهفته پیش اعلام کردیم که جدایی دنیل‌گرا و باکیچ ازپرسپولیس در نیم فصل قطعی شده؛ مهدی تارتار نام این دو بازیکن خارجی رو از لیست سرخ‌ها برای دیدارفردا باصنعت‌نفت خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/31317" target="_blank">📅 17:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31316">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmTzqMpsXCrvWiLUnwAKQEC64Htt_EFwXEL8RpuvoY2RI9iKzMhU5hE-woHSVC3XdQEl52wqjWhTDvKz0yEgRiWnUKlc__DZH1pXMOEd0BJfoZrTkCfWgwQaVoc5Ch_JSpImkGiwd8DyiOJzCs27HX6kJwgJTGUf23o7mS4aU_rOoeNFwTLL18qJRznN5qA-1NwRfrh_0AIpiTZ8PoFlEzLO5mUuf1MiE7yx8kGjcYDtP7dUzrC54Q1KGQHpgnFeGBbhJ3o4XRPipj1hzaRGG1LoqN37EUG-3zmkx_1KroBpuLZSow76uZ98kBXOXKDHDMOicCdQYfkR1azzpIHU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
دبل نیمار دربازی‌بامدادامروز سانتوس در لیگ برزیل؛ جفت گل‌های نیمار از روی نقطه پنالتی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/31316" target="_blank">📅 17:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31315">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛از تقابل شیاطین‌سرخ برابر تاتنهام تا مسابقات رئال مادرید و بارسلونا در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/31315" target="_blank">📅 17:08 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31314">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmmNMIgVSxGIMd2VnqBCPD55xh73a5LMkYcaahGZjiAfHoHTHfrA-q0WTlsDMkDwRe56xaGfRfKSvZAwCmJa4NlzwWxI09L1yGcHsgEdWe1ggHc3pA304TfqJfCqNvWIP8DXQdXOqzu4osNHDpqGLPIkgA1hV_1Na_NOGf9lo_TbMA4XQY8Cp3tVYPKA-34IU1lwUb72ic9rCQcSVOtd2SMGT-mdCmzw8BGOMLmjhN0orQGQGgDF4M7YpPN128f2skkFAjWJPDrGNsYkKvL4S9vPL-dyc_ZBP0xb56lD0yvoUOmpdlSvMV-UNj7ISzIZhlKAHMAaxkGF7DxRltIyLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو: به هوادارانم قول میدم در آینده چند بازی مهم یا یک بازی خداحافظی با پیراهن تیم ملی فوتبال پرتغال انجام خواهم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/31314" target="_blank">📅 15:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31313">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRdq-Zj8eAkqrfcgV206J8Lo_c4YTFiBmGuddQsTBDdbfND1trCiLPr-hV14H9nmXwnt1LLs_ADSP9Z6rfuSZeTMJazUmAN3glwObkbsI7r8DjoYlKh0B9O2Kh1MLtEjhGdw_xYtYgn0jtEcoPaE5aonMDOwuUDL9maYW9M3aY_Kwm0eWsLUhEK1HxBVMZprNYtiJMx3970eH8lliAKRojEmGM7Xf0S9072_Cc2A5ivDtY5ZgqWpNgg4FDNDGJOF9Gok-nfsVfQs0SM3pTYDgwEudNuFQSkUvNaqlUacr40GwcAkDNNAoAdT81K7OnKXRwvAhBMvMhU8ucS6nVZoSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باگلزنی دربازی امشب با ملوان؛ علیپور با گلزنی در بازی ملوان به رکورد تاریخی علی پروین رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/31313" target="_blank">📅 15:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31312">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cldavU2EBl8EFmp7ZP3vUu0kvZsIAodDP9ZARTpJGLPxzz-FmX00P_5jtctr7cK5bqiSwK-yrniO6onKd8kA7ySj4v7A1CxLKeO8n6Gk-DsZHyyyjJKC5F1V_DQ0hu4A_qhrCzQv44DwIUxfSvY5mB0EfYLEQ5vsQbNn2LDHM4M2pGeZF6fNRTlKiuYTjFPwoTN69-i1C3nZPCjixW80RVTCKdb4IV7T1rD-v1ErFcV7KR9CoFUK2bRTGCOfsLVJw6jPVVHb9IiMTpbiGM2BRkvFiagddaJQcw25ADyfVCGsWBJjSiI6cUcWfteArfzv1hqgdKSdTfxiY8xQJ_DqfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه‌های پرشیانا؛ علیرضا بیرانوند ساعتی‌دیگر باحضور درسازمان لیگ قراردادش رو با باشگاه تراکتور فسخ خواهد کرد و راهی سربازی خواهد شد. او از اول آبان سربازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/31312" target="_blank">📅 15:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31311">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IY-92YCHK81HXWDZg2LDs33-trlHwW-hEHNGoJRzjXR1dDTgfH6cu5EIbUoCCVauLqAbw2teLl1tHLTSC5qJFripwDBw1f6axvJhVWqTZCdkB9R7oVORqurGh19KU89Xxmrde9RgzUHxF0qQpnaxnLCTnXMsnDndvhQtS4PmOEWSw4l_hGGsItKiCZH_CDSwUj0Xq3O6sM4z1s0IJBIOFwYLcgqxquIE-mklhDbwjShzyUvvk_iX-r8ftSwWoLsb6w8JwG5FO5dmL7QuZes_8ou3o8kx_a5jBUCP77Y3I4jDZWr5HT9VvaVRIaNSYI8qB_Tupp-_A64IS2gTrJGkfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام‌باشگاه چلسی؛
کول پالمر فوق ستاره انگلیسی آبی‌ها قراردادش روتاسال 2034 با این تیم تمدید کرد. یکی از دلایلی که پالمر در چلسی موندنی شد علاقه شدید دوست دخترش به چلسیه. پالمر از منچستریونایتد نیز آفر رسمی دریافت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/31311" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31310">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAgEy4syLZAFjEGiaTmyFJsLtuwmYW_IftXE7adEHA5_MkphsnuEBTZHzRo44XhGguQpjpime8UUvmW1J-15Vtli6cBbCPZnmLMQIL1PSGvI34E6g0lXqGT0Gv9HP7k1Uf9ptOTS9sYQYKwZ1yTDD61AHbFi_qY-j6viU9XpS3009cGMb8PS1bONlfdQsANTTihXtJ2SXMP0PKHllaaxwqukObtw55ofkCDpn47kKb2DE23VSZmg_5EBrPeX1_MIv0VSgzsh-IM07rMBgar4Nd3dnh50vCZzem8Yg-ta_ZMk5dUI_r0-O8Fw4dxdi2ByVbKBE57CtdxshQ6x2wJqDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیگ سرمربیان تیم‌های لیگ برتر در فصل بیست و ششم؛ محمد نوری دومین اخراجی فصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/31310" target="_blank">📅 14:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31309">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnt6XKsPsbBjKiUFaCUVU91gzMGtOhMOfNzRm8QiMooFrbei7j9D31QqhHd83X1XFPdY9RCMwXTwsU1rqvVI-zZMY6IWzZ_w0TOr_5JgaYoA9HabJGngr25sQtbaXjs2Bb-UbsVgrRMRmMgwZW7CsHjVOMhu2hx-7bQsAM5siZmmvrSRYBr4XTq7f-yQu-4nxT79ZdxNNeJYPrC2mrx2tYktkL7pw6wsz8tMmAnV3WrX7drc_-ia_qPy5_oTLzD2FD7wLmiVhCeqR9KvztvNMU6NrANA9vMY-UfCLEOj6PHH0-2cdonE6-BRikTBvkUwGdQqpbtJu5j4EsLtCiTKUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
گل‌ پلی‌استیشنی‌وتماشایی پاری‌سن ژرمن در بازی شب گذشته روی همکاری دیدنی عثمان دمبله و فران تورس دو بازیکن دیپورتی و سابق بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/31309" target="_blank">📅 14:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31308">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrqTIK82KexzZO0Jco4EO7VPZvd0ItB_P1aPwpVApEslQt_IiesfgzrhhC4hh9pzCpAl_eE-JX88MrWtg6ze4g93u6j8Lwy1N_bunP_pJs1UCygrvSvLC2ofnIDji9c_HKHscdkfFxCjeu52T4zY1eE_HqNWp601uPdACyzV-jWOVqQDWfO8KMGJDnBkvjaRDdz5bDnvy4A8vhs4ooV8cw_GzXyXzjavcsGptHzcNilE7xGMVN0OiH2bX2o4-49lZXJy1Xhkti3o9Z5NOynHB9Ejxbkut4o8EUJ-2JqBm6lVF2iom-6p_YZIEXSkoY1bV6SYtguhf5m2G-M7KUI1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ یاسر آسانی ستاره آلبانیایی‌استقلال دیدار روزدوشنبه مقابل تیم الغرافه قطر رو از دست داد. این بازیکن ممکن‌ست با کاروان این تیم به قطر برود اما قطعا بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/31308" target="_blank">📅 14:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31307">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msuA0Tq6rEaWcQ7Z81zEbS8YLWN8ZNROyRryy5uWxj7TKNYj4bxIkSjBOpzJIAx68kavh_9nDi5i4roajvxeUJGoj3LEWcbzysUtbdZmtoTv0tuwR1f9LBabeeYtFiptJS3WWYIRqT8EBgiPhKLSs1GPrLqM2XcZAjfQ2dtr-CFkL4X-0uSj50O9152pGGmX3mRHtbXaMuiF7XYk4mKBhhh-EoC2pq21owEVNJro3wCs13RXM96YpI1-Ami2RQLzKBk8M14Pnr7718FCT_kSLznMrh5FOZN0J65-7YSRFmoCgNYXncA5jSqTRpB-JK1t3ZdhEbeKBWQZKiNaPli1YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تاج رئیس فدراسیون فوتبال: هیات رئیسه مخالف دادن جام‌قهرمانی به باشگاه استقلال بود ولی این مورد مجددا در حال بررسیه. اگه بخوایم‌جام هم اهدا کنیم توی مراسم برترین‌های فصل اعلام میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31307" target="_blank">📅 13:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31305">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ioaRcFwfljgsfhaoqCCJu79wrRcOHEZbgNRiJBZNZBOfsGJKUKcTTqKbcrAkc6_oW4tx06yjUbN1NkNGomN7KPbf1hEcU0pueuzigyRYEqW67swzFsnHpT7LpzFUNIINwgvU_rzdaRk0XDv3qOsylzBa5QEZYNZEd88KAqOwlzQLt4Qc1lepT0QPI28cYZEMkijRNX_wmL-ANJo9BwfSxhepTe8zAMpfJCJ6nUmLTOM6GQHfPy3ImTUBmVgD5CAObPLXD8S0so24a-YPMHW6s7mTG6V0_TRRKWyWIinsW87X0i3fm87BhuKHej8yJv6VYqmmgOjkMosDfazMuADSdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zxhi1TOU7qA_gJHznfD7ElyAs-z8e13GcswnNbqMXIbtlnuUAVhINczs28IHnVZvfXiX9R443T7F9co2ydYgHQc6o_sf4jOw7Di2a0_Sz_OH0c1fP0S7DqJO6E8Al-lwBWrr-5Ez-gh7l6P8WsX3fbCR-X3GPguTRnkzJ4tM-XjUXQ756XfBXCtwUJwT6DbwWg6tVHlLevoMCmjoW3opnzvRTE_Wfr0lNbzUQzKs7Mf4VDWApeZamZfIpZcSgqQZISSiVRhzLJu1zvBVXrAycUR29Rsdh1jOBuALO1PvfQK5wx-Sb0wzxyYc208YxmyGnmGpAD5Y_jAmgkVvA5QyTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛از تقابل شیاطین‌سرخ برابر تاتنهام تا مسابقات رئال مادرید و بارسلونا در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31305" target="_blank">📅 12:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31304">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmI00RIS5SEgHCm1TgQMZeh-E3rUFBSW29ELhmOm7qRBuWPmnwy5gXxernpC8luQHTCoIhzIXxXkPfWM1vpPraAOw5MI9KvtTKu7XIkx4gtciLFY2A2gD5ZS3X0WyJwICYBaNNdGuXAvLBbWjQuP0y7xwVwGMK_UYpF8cMbOeudlKMUOq8DdIeu49LxuhZjhl7adSZ3LQpN9GgEDo09va-Bb4JcIjrXiXstZuIgyF3Hbc0UL0vk4VZ21Vj0labpvzHvj5WgHtWC3wkFK4pTo1D8_El2XCv3PLObomGzDCxvyszRVgNtFISr6RIaESaBBy4TcpUsZBUtpL1IvSYYrSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گلشیفته فراهانی با جان سینا فیلم بازی کردهه؛ چه لبیم گرفت ازش. الان دارم میفهمم چرا حکومت داره تلاش میکنه گلشیفته رو به ایران برگردونده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31304" target="_blank">📅 12:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31303">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_tzGcb4NZDX2mjk-zjusJx5uIBTeW0k2swTyTPw6CBmyGXbAwMg4IoRdYCMZ9Cxasu7uu0rNZUCHUiazOU8_vEojxKR4QMCz5Zx-5mKH31-o0TphzAjeFTxB5LMNslA5YKsCoEpd0RHre2f1w7tyHcBLQgFQqKCwRCNwaI7CtSa1YbtD-iRRd11Mk1ecIkjR7pOo7BJYneDDM4NvIA2EZx7hPpU17bxGlrr6rnV7no0E7NSWWcsGf9BxjW9cYv8wfEYVRiN9Kf0dy8lhHTsdmbtGmGApnnKs-y-dUdIGb5XJ9WbzvpxDeTck-HCGBuUawfx-lopOhPeYGyQOJAMrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
گزارشگربازی‌دیشب‌النصرلحظه گلزنی کریس رونالدو: دردوبلات‌بخوره توفرق سر سرمربی پرتغال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31303" target="_blank">📅 12:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31302">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAhqvWSCKUIAR7Vw8eWMkw4IdvrRuxYRqy9dgTBCWBHBHPry8OqFI_1_gZNEjQsCtKY-4D4UvUiuJKXwIwhI5S5lfS5fvmF3myUc9G6hNWbV6sayCZTnW9AvhS3FC8z74bTu0BMTPEWxnHOjjXUvY1DgtimeX9RzfLVy1cpKwyR49P1BHmK6r8tP1WyDQJELN5v1CyApjyIDtlHMXFnlnrHG0fLPaLg5Ak5S_jynpURjVpi-DpI_RvCTa-3GCToIcanH-nfI0VxdFbPH_JxuF5Ec5t4wRy9UNJRmb25KjM0THsHdDN9mtxTbCNEcEy9BqJy8w8ai_zTNSoVN51os6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگااام! مگه میشه؟! صدا و سیما: مرغداری ها برای افزایش وزن‌مرغ‌ها توی‌غذاشون تریاک میریزن، برای همینه اکثر مردم بعد مصرف مرغ بی حال میشن!  نمیدونم چرا حس میکنم هرروز از این چیزا میگن که مثلا مردم از گرونی مواد غذایی غر نزنند
🥸
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/31302" target="_blank">📅 11:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31301">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loSxGHiMu4mTfRk9rRSepXngZIBKKoCRc1LIkutVuomZdR8HRO0EmTT6nroBt0easnp39cHkf0wuuG7r0AnCZMv72UK2GiVc5aE4IntiE1VxOhz9OBlmgJYASjx0gs-0kadTwtu1Wo6P8MEXSQSAuNarS6z-Oh2g5E3Pbd2barWokOFN15TKRFGGMgvZ5zxJkQk8S8msz-6DjKDkBCeumGfgnE8U_HZ9fkXnkTqI2CjJcEyLBEY0eqcE_wE-ZAW2Q2Nn40X_AU5MigWyL_fKuKJOjaREfgIOZnlxAEI-2TiauJRxkG7Nhu4EqwxPpVRlxY1ujA_iVjsHVVR9aPDxqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ایکاردی‌بالاخره از وندا جدا شد؛ درخواست واندا نارا برای دریافت 250 هزار یورو نفقه ماهانه رد شد.
‼️
ادعای‌واندا نارا مبنی براینکه اون «شغل خودشو فدای زندگی‌خانوادگیش‌کرده» ردشد.  مشخص شده که دلیل‌افزایش‌شهرت‌واندا نارا ازدواجش با ایکاردی بوده‌که توی‌ایتالیاخیلی معروف بوده. همچنین واندا باید دو سوم هزینه‌های دادگاه رو هم پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31301" target="_blank">📅 10:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31299">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3341162dbb.mp4?token=dU_aoT9nLG-Aek0Ate5Dtf1eu2wWW5agPORl3Qw7KkrCFXBMM6PU57mcbtFLgmlBQT5aU_aMDMJn_vSrlXV3XS_8PeRwqqPMjY6TPlH_Ni1sMAt0_iehNvQdQWlw9RroUh4QEMAEkP6tYtd0NL8zLSmx7PfLE7RB72aUC3vYCOlybqo2R5oyUEG2OL5MAfiY4WKK397PB5NK27WNqhEQjOxcubIHbbFQzLWYfVN9RX4fuvA6c-2-esasJJQgY7ppAtmGWtmPFHsNQLLRrgKtpped9xEd9B-CUNd9nEysT1UqIa-96aSISvbIMC4AW5Dn7la5zF5hJdfGdh17T1-PAkGGbS0G7yAV3PdUuWMdfrNJGPLC1kQwZjGqLReqUN17M-gnZQae1wr52DllpPCd6IZNThsmGDJwDgqU3VcbU0lsp_X6-yJVCG6v38T1K9a76TsXsTHNPx-vogHmgOM9D6JMXhWiJ0OA2AVBhH8FbJXHc605OzVcvntpHAGBW3umWqHX1FWHKv3ZpIiAfPEvWl36fAy7VDTdnfnkIURReUO6hJHPo-6xHfLrag44EY_eWkMfzAOMZ75hFFcpQlIZ9y1ztGW6XvU7qGEkOpz8eaBL7NoBU2AZ4wB9eJKYcms96H-TfiOHFCcTfWOaUqfozLOoViR7n7pGeTBBKQilwW4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3341162dbb.mp4?token=dU_aoT9nLG-Aek0Ate5Dtf1eu2wWW5agPORl3Qw7KkrCFXBMM6PU57mcbtFLgmlBQT5aU_aMDMJn_vSrlXV3XS_8PeRwqqPMjY6TPlH_Ni1sMAt0_iehNvQdQWlw9RroUh4QEMAEkP6tYtd0NL8zLSmx7PfLE7RB72aUC3vYCOlybqo2R5oyUEG2OL5MAfiY4WKK397PB5NK27WNqhEQjOxcubIHbbFQzLWYfVN9RX4fuvA6c-2-esasJJQgY7ppAtmGWtmPFHsNQLLRrgKtpped9xEd9B-CUNd9nEysT1UqIa-96aSISvbIMC4AW5Dn7la5zF5hJdfGdh17T1-PAkGGbS0G7yAV3PdUuWMdfrNJGPLC1kQwZjGqLReqUN17M-gnZQae1wr52DllpPCd6IZNThsmGDJwDgqU3VcbU0lsp_X6-yJVCG6v38T1K9a76TsXsTHNPx-vogHmgOM9D6JMXhWiJ0OA2AVBhH8FbJXHc605OzVcvntpHAGBW3umWqHX1FWHKv3ZpIiAfPEvWl36fAy7VDTdnfnkIURReUO6hJHPo-6xHfLrag44EY_eWkMfzAOMZ75hFFcpQlIZ9y1ztGW6XvU7qGEkOpz8eaBL7NoBU2AZ4wB9eJKYcms96H-TfiOHFCcTfWOaUqfozLOoViR7n7pGeTBBKQilwW4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
تفکیک 980 گل کریس رونالدو در کل دوران حرفه‌ای این بازیکن؛ CR7 تنها 20 گل نیاز داره تا به رکورد فوق العاده و تاریخی 1000 گل زده برسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31299" target="_blank">📅 10:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31298">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSAZ0zZnOT9Mc3_O2i-Js6P1zMq8_DmBBhupGaJX6nk1IRi5EVJNC99ZtLk15gGugr8uBZ_8ptrHkHJ-XrfgP2DUr8O5kLcmFrVbRQ2enTSAOKWGVZRvokgiLD7p0jX9VU54Oy_1Q2VGekFca67pMTlf5yHGvu3b7deH1sposXWEZIabasXOLGI4ooWYlZWYxdUeKKFteD602-E62gXtul9iLh7FkqmbiDOjnNcRW_Jpa2gaX8waYpKkQ-g2B4WysnlOTOXIa6nUyQXrhSZhL3JZET5kBdxHWLADtOHCwXc5IdExcy_t6gQi5aAlxGpQfTJ6F6AWypmo1DR_3x_ZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جدایی محمد نوری از نفت آبادان؛ با اعلام باشگاه صنعت‌ نفت آبادان، محمد نوری پس از شکست مقابل تیم پرسپولیس از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31298" target="_blank">📅 10:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31297">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtGEtQQkAcbPCh2xeYPhznx5gdzAtnUnGHa8GOowacgtR_8LQc7PBVKSLh-XBWp_v35jtZLqv0q8UqSev_KO15jNYna82SpXJBdcEJ5LkEM8FSnZs0DhaAzupRBFy58ebVCuRjjBNKj7Qx3G-2ksEh6hkj50yjFetHK_jTjghe0x6h6nkB4_XMGlpmfq49KRGfj0w5kMaWnmwJ0AUTptEjEdVCLv4LwJUoOhCVE_S_j_gABS4zdsQ8mEZsWMktvw3JSFamQNrEUviYnT5-2z6_W8zAuiy_2GJqa9wwZfk-Mx7WUkbBMreHGI5nY9iIn6JgI0J2QIXI7EUkwrTnaRCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان‌نظام‌وظیفه‌به‌علیرضابیرانونداعلام کرده تا زمان مشخص‌شدن‌وضعیت کمیسیون پزشکی‌اش حق خروج از کشورو ندارد. از طرفیم نکونام به مدیریت باشگاه نامه زده و گفته بیرو رو دیگه نمیخوام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31297" target="_blank">📅 09:41 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31295">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdn0LyzMuZF5AqyVz6L_M_8GwSI8kY_uGUo9n6pMPP9wcte9R9GPPOCXf9e0ujPW6-g1V-bTMPJWNfbyi9gr1BAgsuIa_k7NflMfoyMdu4a-5atUHROViIQ_MmhlEd-HKGruyFEvb3mQbDfbsoExkbwcc-8IjSzu9hVArUh2L159DHnG0U5rzupt2WiNkYfGXbb4Xx5fiC0YdbAbqON1neKlh2zB6_-TWBDCVJPiXrdF_dBWML51s9km5uzIxo15YoAKf03Ez6pU73P-RpVSq-t8fJ-0vDpA38DA5g9ZlaOawI8GadAVsBLgaUozE46MyXRcJ_dk79k5SZAOMgtixQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛از تقابل شیاطین‌سرخ برابر تاتنهام تا مسابقات رئال مادرید و بارسلونا در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/31295" target="_blank">📅 01:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31294">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukLsV1ptVsyH4x0G8AFTKS7EP9TmQaalmUiw_gSHnROI_w6dIhAAE1P54hgb9DB5nsbxcrqj5me_JiJw4AhoWg4eH494t_zELusgg7MrOaOnKFHzJAacqTbm7aOm4zHgIuYElPUfpSr0gx5MFsyfFeemcBeMeNE2oE3oAPztfoP-PONKZelJAdq-oQjm9JpLfVDrAU0yCBtXz9HABEVEwWigfLA5fcgp4bn3tmgmP7ywp6h4VypoVdwf7p_knRSEQoc7yAlSRdQ0QzmRHl02qwlb9yBUxJkmaOinqFsJyzItvVHhZ4lz5I4fEKNHbEJZfKTnoSvxx8G30CxunKc_sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
نزدیک‌شدن پرسپولیسی‌ها به‌صدرجدول‌لیگ و برد النصر در شب گلزنی رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/31294" target="_blank">📅 01:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31293">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYU6VqSUcXnORPhmYSxjp0pWFgZ7t_4kwzIQFJ8wujmgMOzNIiDnlRBBXsD4snt8gotcM8JIDBFDdkNHr5ocG2ks1GykCFUanJOJAhR8kBeUvZN5AMu5jfhw9aRkXV8tFVdPbQDoVZZZF0PY6nSYrlWJ8lDS0cl_FUw83fHYbDe99BSou0AXSxrtGiZvT4PIsSYwHsNOQzRS1PJpGmNqn_yvOJu8Y63pAm8UH1H9uinv21Nw7DkAnrIW5kgA-xtEkSD06LnLd2Xxq4kX40aqh8tJYXn9PMpbC8BsK7jiotjyA1hnPGggTxzgOwvaiAlPTC2WYW0R7ztU8B6bq8qTNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛برنامه بازیای معوقه هفته هفتم رقابت های لیگ که روز سه شنبه و چهارشنبه برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31293" target="_blank">📅 01:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31292">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8Tq32-UKM9zBX2S9XGLZm1iWKHg1ktCQawoBIzg7tNNHMbzTFK4kVSssCqTWSmuGW6iSHxGzk3fCcBEHnGXcDgmPwH-I92MiJO4r566eKhwNgUO3-PDulvGMAi_l02ABRZRO6JjDbg7GkPmyzoHie8ny83W2Ne_h7RRneV_FXcwukVigL4iNi_FcXdpuwV-BAYWnW3QPS9pyDYUsAL5s8HBM_5hgd3o3djsqe8QBwMo8ZLWYV6nNogsehH8_DHDHkEE83phqeFYCqM-uBskmAz-dS5h5ART6awwikZaacsxCWm4ddcdVjzMQV1WNafCNi2zifJaRHIuDq00gulJAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ نبرد شاگردان تارتار با صنعت نفت و دیدار زنبورهای وستفالن مقابل وردربرمن برای حفظ صدرنشینی در بوندسلیگا   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31292" target="_blank">📅 01:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31290">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBgUjezrkxXVGcUz3JgfjKGiunhhTJot_8SZp8J-gWyNmiNKeU60xUZec7tIW4q8GZ2v3JKa2mgjucEzotdVgG7mo9UCx8HJDbUywSx293x4SGvt0OdeOUHdKMR0mMhJ6I_E-uJDN8U_LeenVPTBcUHDe4BAPqzAAHYAwq6Kg_JXbq3QeBEeRoBBgavncItkyCnEnjzvWmFEKpsEUAruNtF3AGmk0MeRFDvMPRTnXmaLliE6KHXGDRq5KqCWGXwULLlMVk9by2zWneWeoiK75ZoNkmlvt0EYi4_F0WeeWWzXPi06UaDZHpF34gB7GzdNOyf9p5PCqFEZJpaVgYetMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
گلزنی کریس رونالدو دربازی‌امشب النصر با الدرعیه؛ این 980 امین گل کل دوران حرفه‌ای CR7 بود. همچنین رونالدو به اولین بازیکن‌تاریخ‌تبدیل شد که مقابل 160 باشگاه مختلف موفق به گلزنی شده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31290" target="_blank">📅 00:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31289">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nb7J5IdrdeE-5W8xNWT7UJxB5Q0zoV2wbmFHckCw23O62qeLHllPewMPo0SVq1lFeXxGroJe_i6dAGaVTeu0Khjz8W1re-pOLWVQ7FFAWRqOSlzifkzhsqYLZHrLKJWsnKT9EHiHBvGttAK7hw0srpSkfe3gAq8eLk1lCj5DoWrazGNcoF_Mju9Z0koJHegG4nr0DLwAmVz4kEfEkr2-nD89xx4gTN5ZG9Dq4qcPtzps3IGY_pOFNBRuiQUlzzUJpv0PHIKdcYVBneDM-C_9AHTU7izDwXHwE1Fkw0oD39EKhcObmYT0IKinE-sgXbCqtzwb61GpRvTjB2f6_SbdXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دختر خانوم پا اسکولز اسطوره باشگاه منچستر یونایتد: جود بلینگهام بازیکن مورد علاقه منه. بنظر من او در حال حاضر بهتریت بازیکن فوتبال جهانه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31289" target="_blank">📅 00:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31288">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6Mkv0KMme6j31Jkc1NHexw9vlib09SGuDwd88xF2mJuLaNv-tnMhgk4LaQeQiFl1FuolzGoYm8M7aRWF44CnsDMBEF13FgkHnlMLHXNQwOySWXliwrnYhijWVB1g1FRED-zdTIiCabXHUGJ3W5Mi9Q5B-n8TQFG7BGi81smFrdpQx_AU3lB02tZ0fIzYent_g47iL9fFa-aYaV29Y7gwPpANhX-2uBgI1ttiv3A_O_o-T9gN2zbJFgBygkX4dcl0iFWg_J8uc7AREjPrKkyW3LzeUZxgXw7PER0YW35ufNvCns0jaaiSNhfMcQhO1NukXt-xMHDxm6GmSTNBGy7Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان هفته هشتم؛ البته بازی‌شمس‌آذر با پیکان و بازی‌های معوقه هفته هفتم بازی مونده تا جدول رقابت‌ها تکمیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/31288" target="_blank">📅 00:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31287">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‼️
سازمان‌نظام‌وظیفه‌به‌علیرضابیرانونداعلام کرده تا زمان مشخص‌شدن‌وضعیت کمیسیون پزشکی‌اش حق خروج از کشورو ندارد. از طرفیم نکونام به مدیریت باشگاه نامه زده و گفته بیرو رو دیگه نمیخوام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/31287" target="_blank">📅 00:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31286">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo5nHGEdz6MrzSNoYwzcH4iwipyF4REByHI5aa-QiqLdaPFuD9MSg8RvknK8j0xq7H6uegjmHs5tPTitIL7RBv8Rtm0Z88yuQp4LHsDJ3Nb1W-M1h85ziVFaH-5_YdZjdSyOdRJTLjf6VG4wLV645cSZw6H9XqEWqE_pK5opm5l7kVGs2laeLDPuQkSaKeIl4xO-FClDnpSOlejezoC6TOUezF_zPT41zB_Dkjrn5kmRWWezVMwyYATUx4OVQBc7OwZ0oHc1d6IX3MFO9M88cUcJHbAN3gmM8O_J3_BZJcEjYaeQJgt1B6vtspW0ik86uvsIOOCLpfFv-2nZeWTFSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تایید شد؛ علی رضا بیرانوند از هتل و اردوی باشگاه تراکتور تبریز اخراج شد و با صلاح دید جواد نکونام برای همیشه از این تیم کنار گذاشته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/31286" target="_blank">📅 23:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31285">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhW437t_Cv_2aX1SsffqidLe4Cc9aWg-lV8zmNaJO1AM_DowVa5uHwDFa54_6PNmK4HW1zz_JhgZ5UIZjr3GQkyCaYzsNC97e7_PIWIKbj0z3gysjM4wpNNPK39HDCYERb1pNEtcvlmLlzhM2KP4Mvl1I5Gf9YVxQVsaAftqQOuR1wxrUB1DZ-YqRM3tzNsOmOGQkTX-QmPgND4gk2OQSY7rp8v1KU1IzKQ4GEGN4A67zR2WoZSaToE9rCytDUcaNmpkpd9G5kjpM6zW8ytb_JVKAEwWiBK3hzRGDdeWN6KtivEYcXV0WdMATXZR2AEz_dXOdvpzaiZGnb4IzXWuLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جوانگرایی‌بسبک‌تارتار؛ حضور پویا اسمی بازیکن 16 ساله به جای ابرقویی نژاد در ترکیب پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/31285" target="_blank">📅 23:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31284">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H40xAqT_Cxli4VeTwCPLPcQuTWN-5VS-4xlHP-1rxhka9Ex6gnhCHP5-s-qEV4KbkV7AC0Q6pZwGfNoIZV1cVi6rOONqefPuMEzlZdvP831XgDtwdWLK8cqJGZp5IAtMQWy0HqQwg_hq45RQ6kxw-pkjWVIxnlorqwsgTks0gRaoeSWPOWskTop9xKNWvGjnvMGLZmbaHvieHrTSo-lHLZNK2J25a8nWnpfS3AvtECdbXukleiyfflOArxwA3UEcsEg2sB3zt1jjUrAMkCUCUL8FybpFzyEpu2T4SPxYqavx1ZXdX3TNzaXr5pRQZ7Jk6vJpcx45qcKndFaQZf1tAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تاج رئیس فدراسیون فوتبال: هیات رئیسه مخالف دادن جام‌قهرمانی به باشگاه استقلال بود ولی این مورد مجددا در حال بررسیه. اگه بخوایم‌جام هم اهدا کنیم توی مراسم برترین‌های فصل اعلام میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/31284" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31282">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QRdKwxTFmfYNr-nFQ5PwIlj7KI0_Hc_zAfuhduu4iWKakiaaeGtueSCgRNTItSIAmY9ZdRKrfbaOidyQAyNZLPLH8tVI9IMlKzMkl7tu2K5BEWNzpLcU5qRXykWff9_topo2Rq0tHoVS39FDgWjIEJKIUtn5Hv49QVO86Qtf5bGU4q5Juttt6P7ZtXSkgUzjsCpAOAmn-GAFCfoLZQVeerVCUJly_f4F2Zw1HhZT09Q5IpG1lwODh3whb4_Y2f3XgMM_0CJpaRI-KHMsm9Pi71_UXH0GshYc5WTRk3OqxOHMJ4ytheJD3gY9eQ2vNdhQlAMslPs-6cfhER6mjCoaCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UVnZWCVkBdopFbXNyTwnfVzYc0hXGb5P8V8yzvsirAlNshN7PtnuUZ55bd7cwnY01tOR9PlqlnklK4rE9RdCMj9HhwxulMYEbr8i3pRFUPo5TqC_pbI-MrXRiVwyb9pLccuQdLon4E1VCx-o-YtZ_eq2eh5p59R-GN2SM2QL2DQwF840fC_430boGw2rMHOxaG729Ssqa2wqp1w8VKkM7t0If2YKKk3eNn7OnAlt1857Dek_8z0Ro6fpprofY6Ugct2-TKDbSUzdGAH2PtlvwUlk2DikbQaPC9fOFEZnj4y0E7v4u55w-4lp5CJH7KyLRzw_biuw3CGdyOdS0idWMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
قدمت باشگاه‌های فوتبال ایران از ابتدا تا کنون؛ آبی پوشان پایتخت قدیمی ترین باشگاه ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/31282" target="_blank">📅 22:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31281">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRwnQ9HjKyhvb0WmjqKVb3PBA8dG4uwQ7UBWwZ5-JOMrtoSc0V7i2RiOA0vbEdxZgCztwsTKK7tqmEjdZ0DT3gicDhDBaWrilr3pqNxezu1wKNmw2-QNpYnpuxMyxZTEATMkSGYSRGvDEIDx-n4HMyWTbT5S_5KKnIIuoc_EJGlLjWlp2dxvsk-aq1SaXYhLCe3NR3Z4bigi--x4UZtGvEdbbZg9oqi-7yt3Yv2tmbpqCpX5Xx2X1RN9cY-gvpRhmL5xfcCVgDbQhz4fqDurfX68oI8Yv_qgWzsswzkaSpk9UQ1uFPSLIDU8pIZfe0YiQ7hkaJQICIwP7SE4kub20A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم لیگ برتر؛ دشت 3 امتیازی و ارزشمند شاگردان مهدی تارتار درتهران مقابل برزیلی‌های ایران.
🔴
پرسپولیس
3️⃣
-
1️⃣
صنعت نفت آبادان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/31281" target="_blank">📅 22:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31280">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpKGlQudOHQtjXS1fz2_du5LlD56EOVi3LxLbj1MBK7sQl26EBsdqRaHDiQ895t8IM-loyQ4XME_DsaDhEFh5OYvQAWvkhpgZ_1JEUsO6yWaP1SG3tx3oaxRfLOyKOXHxX1bEtThGo-EcpQJLsAoygiKRSkPOE7mC5FKXLfAw_BK0QYftKjWRIzg4gpxeZDdlMxiphRIConjhSLf8xBNTo_OZDv9j1XbEHRHCyQ9f-sQSPuPOjQIjaubrgOVbVgm5y7cb7VyVhZaXActNrNDSXB8Y9J531SpkxIh5mySfu6PW2azniblnCPPNWmIsGf0jxrsV_eudtOb_utBXYDSrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دستور واتساپی‌شجاع‌خلیل‌زاده کاپیتان تراکتور به‌بازیکنان‌تیم‌تراکتور:همتون علیرضا بیرانوند رو آنفالو کنید. او دیگر جایگاهی در تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/31280" target="_blank">📅 22:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31279">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🟡
👤
#فکت؛ کریستیانو رونالدو در طول کریرش مقابل 159 باشگاه مختلف‌گلزنی کرده است. اگر فردا مقابل باشگاه‌الدرعیه گلزنی کنه اولین بازیکنی خواهد بود که مقابل 160 باشگاه مختلف گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/31279" target="_blank">📅 22:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31278">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ فکر کنم تنها کانالی بودیم که بارها گفتیم که رئیس فدراسیون فوتبال به باشگاه استقلال وعده اهدای جام قهرمانی فصل گذشته لییگ برتر رو داده. حالا هم طبق شنیده‌های رسانه پرشیانا تا اوایل هفته اینده فدراسیون رسما در بیانیه‌ای استقلال رو قهرمان فصل قبل لیگ…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/31278" target="_blank">📅 21:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31277">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icKR2OIhy75s_RrCcO1hGN8DBVtbppqbTMAGtk6jEsosCl3gSNN49UzBmNPz5-9vX1_I58cc-znx6d9H9zPFCxIOPzGVJfQsr6K1UhfY5GLavDc9TFw-D2ULVEwHIoBa-cYeWa-uEHd4hH0y9GBFyr57olTGVP22By9TxnGqPhN9a9GDhhIWNQmRKAgViMMuR7SJWlvD-CTo1dles41DWIo1mWIA9JzGnvBE_hNkLYiwbcY-3IgEJKk_zUrWtDj7tQ7ZnPAqBQq4ItQSWFAg3XmBi5s07XcrzFSS0HQOpVgifjYDEVlKGjJbiGeZKsC_M7Zs8QF3ZZ5ZzOM1ed5vYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدمت باشگاه‌های فوتبال ایران از ابتدا تا کنون؛ آبی پوشان پایتخت قدیمی ترین باشگاه ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/31277" target="_blank">📅 21:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31276">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axjLExr0EHgZT6Ip3BDcH-rtx0PHE3d0S0AOWqrsFCWE3O_fbh76L4ugjscayN7-nhqhb1WZpg16jI2DrHp7BhsW0YEFc1glaCB51XA3GGjhI9JyV17RGOcJgXVruMADFUuUgBjHXDhfJVVh6WRh8QYjnzwisZa3-wneHl9Bw1QQrr4zBvgzUmG6QNWuUPMYTe4aSc4z7YquHoK2mzWTYmIBPEAfr9T1XxCACHxLqQSXT1LwpsyjX_8wneLWG9FL3MYermZdLYWhIKcif0I6kpanmuKkETYYQSBNCDUca2rv-OAoR2Is0CyvDg_SJIsocX2BQNb8Vruh8hHwqm9kWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام وزیر آموزش و پروش؛ به احتمال زیاد مدارس بزودی و در روزهای آتی تعطیل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/31276" target="_blank">📅 20:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31275">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VU64pw5Zirv67THdKDyjmN0k9mAzbmJBmf-jWJBsMwJDeM99HsVGHQMu4N_4Ao1Bi4p7TIwBoKge8L-_BfFCIqThuW27URCuEizBcJWigGQstDOYVA8xgqGEwYWcn4IHKyp2qsgIR3768S9psF93yVLbPuQMCYza04y5KdJ2beVe9ByHLZXGt5pwdmcru3Hv5p-WOC8mprBesH_OoadTsbJ1QXYYR8a_JPa3tgyfvYRLSN8TkRrsEVXwRuOmk41ZIQ3Sf6n5PQWEFrSK4WWZCfwDvgMNQX4i91eBUXS073Oui1IjhFxhuQRux6sJJTsVmozJoHPR5uuFhIjm-tPmiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ ادعای بن جیکوبز: خطر این سناریوی فاجعه‌‌بار وجود داره که باشگاه بزرگ منچسترسیتی به‌طور کامل از دنیای فوتبال کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/31275" target="_blank">📅 20:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31273">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OAzrlNw-doJlt6xmt1S9760gas4Zv-XMu2gUD9ATqYjvK7e-39TUMZFLy1reZVWdrQQDI4KjsoNTdNhtJ4SWU29pPYfsW9Stkrq79aIJY7RdHS_pM57pujTCT-ng0QokR4oeT7kRVA4dbGsKf-BiWHiW4pcjmhRgD4hBmvD3P-2QVcFFM5xuf2LPeNQ0f74Nii-NXgo2jae-ZuqGP86CA_Y_ui4RWQp2fsUkpxNtKJTSiRp-7f5gTW3AbipUk5ZzxEY9-F8wzsgMaxU8v_2VNKfeIIxcDJVYH8HPiUJ2GSDBkMgGdt6p12Hq9pk809Pr8K8bh8A3fW4REprbagWrWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v7duTlhSpEeUzed-dXUIEw6OTr1yJ9xN_QhVsNErycG514X59O6bYTp8yv-Aysjh2TCKIeCnvni03VdyW7RJnbmvLXcA_XSKj8yoy1bRDuEx2Io0ndUUHV_8a47SpN6HG0-zDeM-rwWYxg5E7E3BCyZ3s2IUt2TPe_m_9yVfZcaTKsF9qZ6nx12AqS9uoE1yajm5vr6bvksUwrkzLKS4lpFhFd3jfPJAFMcBmsb0LVPKtwP01CBeRsgU5ueKidRLSyMGEPk4G2OvyRQeAP4GiEHtxPl5ZI4kF2SwvonUeqVo0q-d3sQW06LQDZLqf1TjxIhz4LvcUjInQbAbvnMIjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
تفکیک‌ گل‌های کریس رونالدو و لیونل مسی در مسابقات ملی؛ رونالدو 146 گل در کل دوران حرفه ای خود با پیراهن پرتغال به ثمر رسانده و مسی 126 گل برای آرژانتین به ثبت رسانده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31273" target="_blank">📅 20:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31272">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e9e6b867.mp4?token=NS62KHdvlA72aSwBYAZOqPwvToN0vonAyuFM8So5-R2NjJyOah9bTCRu-73NH9IObDHIY7NH2Wcpcy7cdxiALlNtKNZNkDESWOzLgGPRV_d0qp8dKxZkp-h03Uyu5l7U9S-AfN-52g0URsso9Qe3oVG0-qydsXd1fo6eW4yVA-0FUhs9yumt1aj6RoxZwC7PiAqYtUDsP0ChKGSzHpXVG_HVZcwoanNPEbHRXR43OSwQ60z2nUaWHnTqs8hFoAPiKVl1loPgIpTOHLKAmP1TkYdy5ngznMrzABR5iYCauSl9F_iGvA0N-o3xSl23qVaert97WC-TgnSCBsIdnurjvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e9e6b867.mp4?token=NS62KHdvlA72aSwBYAZOqPwvToN0vonAyuFM8So5-R2NjJyOah9bTCRu-73NH9IObDHIY7NH2Wcpcy7cdxiALlNtKNZNkDESWOzLgGPRV_d0qp8dKxZkp-h03Uyu5l7U9S-AfN-52g0URsso9Qe3oVG0-qydsXd1fo6eW4yVA-0FUhs9yumt1aj6RoxZwC7PiAqYtUDsP0ChKGSzHpXVG_HVZcwoanNPEbHRXR43OSwQ60z2nUaWHnTqs8hFoAPiKVl1loPgIpTOHLKAmP1TkYdy5ngznMrzABR5iYCauSl9F_iGvA0N-o3xSl23qVaert97WC-TgnSCBsIdnurjvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی‌های عجیب و غریب دروازه‌بانان باشگاه‌ها درهفته هشتم رقابت‌ها بعد از اتمام فیفادی مهر ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31272" target="_blank">📅 20:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31271">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1gPO-OvLnOwoZiUcrxjmzttqm1Lzy-vE1pBndPmve2qtB6_CziC779oHNMvyfcfFf9v11D8gKI2jTguGB2tiuHd5bxX4zQ9ZKNRdMnltrJYbu8hwakqx1FRPmr0O_3rYP5JQYf4G0Or4CMF6HuVI8MwRwDjhEqSnIK0m8JaKKxAQkWYS9o3bRv1OnXY1Fej1yrftOd_12Q7zTP5V3pikl2tlHC50lGrF6clYdQOHSiQ5cM4OQ_3sgMXdI6IjtrA5PdHxhak7lABrHKqqQQ13B786vwoUXmp_3aUmijNFwPFK1ReFTiFX0Q92z1zQoxjEsLODVLNqSwlAPolXoS-Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی رسانه پرشیانا؛ کادر پزشکی باشگاه‌استقلال به‌سهراب‌بختیاری‌زاده سرمربی آبی‌ها توصیه‌کرده دربازی‌روزدوشنبه استقلال مقابل الغرافه ازآسانی استفاده‌‌نکنه‌ تا مصدومیت امروز او از ناحیه ساق پا کامل برطرف شود. بدین‌ترتیب‌به‌احتمال زیاد آسانی در…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31271" target="_blank">📅 19:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31270">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان هفته هشتم؛ البته بازی‌شمس‌آذر با پیکان و بازی‌های معوقه هفته هفتم بازی مونده تا جدول رقابت‌ها تکمیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31270" target="_blank">📅 19:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31268">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzJbd_eaoIZGDPomz9yx1jnCFpOY-ukaOV9pC7sPHajsJXVsRXgSNNyQjAmTh018z1M9bmuRHNO8ZzTFA1wx0osDAt75o9W0lPwLPWsn_i98BIOxEWT9fx0GeWl2Gh9CqAO03NHz3KnlquxuCezDzfHJeONCjz95n5BNYkHZC2hpgNsJGJJabu_BjZQ3qzRT_qBnmBZCqjBRnQM4d2_hg1vbtuvX9hrekWlilmMabIo7w_h5jzbzeMdAZh20NF4bZNnYZBC1FmBHD8WRKkNII8Upp7gB7C6aR2kohHdhT5vlLtnB-FCC_Z3ILAGAFMQn3hwrEOqBs-7vR-1R8AZzIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ وزیر آموزش و پرورش رسما از تعطیلی احتمالی مدارس به دلیل تهدیدات جنگی خبر داد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/31268" target="_blank">📅 19:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31266">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCoCWDvnnG2Vcf1-gzw54sFCeOYhRdsAzRu7IW22Y2zohTUbYrfkhIOJcXW1Lcy253dUHBB8TRe_FAzU7ZZ0sPR3A47f-gw-FNUUHbXXFGTpEZqcrutZLbIpVhJSSkozQnXMjx-wcARTDLxKLLqNFo_LP-YBZnsUTynY4XL8zfpUM59wB6WqPY9egFOL-otaIxHsNMltoEJFyI6D-lXib3NioGaoa3-ypHXV31NbzkRJCLhvYsMlDmiZ34-x-T53BidJVeu0bLjPgQ7YqulwAYGPwYaJMsIAFHY1hvGFjHJ8ViwwFl_1Z-IWVUMkLTc9QDDIpGSnOMljtSXQojmClA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mj5l45uQ_6OHnBYay6E0NoeUYjDnAfM71YRmTP_FS5oQk2MkpR2QYOxeOmXFz4Mp3njYLjE2O2544wqkh2SXtnkfV1TRwR0RGLWEBiXRRRfY6tx-N8Ze2gIRclU_gUZc5bULODU8eOFoAqdl4GC29rHuMCxshNYx3Xsjal5g89JntR4fUehPz9Sdcwxv8D3hkuIvBLbZP25DexAg57TXI3qqN8mpnsCpNu7SCRihOKdmC8bAxosWtTD_QAsyUnhKiaumoDQtIfMyB8QOCcyU1eFcIEE_SRfAw3r2CqsXKohmBYJmYSsFcsCuauw0ziE_E-89_k-A8kc1gHYL5gbWpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بانوان هوادار پرسپولیس درقلعه‌حسن خان.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/31266" target="_blank">📅 19:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31265">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWNbrnIWe61YsfKr0IEoKRul0_PeRjbC1EPF3ufKy5dl8aMTpcPDUHh4BTQFSRz9gMk3xnAvWcqEKyTuKX3kb_Bq9vMP9fhXBtOspAL1jp__NfPkEJMfLySlNNPIjXohkOSTU6PKgmdvoXrV5x33gG9_mv7CKOA-T1Z7ilBS36-fLtxNsuN3KPaABkk5O9hlEt-B58ndR6ugvyubaTsA-J_SxjpcNraWLS6R5L7gcTyUMsBr0SjC07m43L1fsk-Cj8ppyXRsbEloTp-azCXJN-JDmml4pmXGSmuqe2-_L-zWNtXrAwRPbWFOfOpAweQcbeJMtJoNDdXtp4HUG-ZtcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم لیگ برتر؛ دشت 3 امتیازی و ارزشمند شاگردان مهدی تارتار درتهران مقابل برزیلی‌های ایران.
🔴
پرسپولیس
3️⃣
-
1️⃣
صنعت نفت آبادان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/31265" target="_blank">📅 19:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31264">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_i9Mb0OLiFb42kOXZTcqu4ZHtqTQIv_AhtiA8AD2leXVttzgTjISvdYJCKPLVvp1B47uflA3Q4npq8Q0trGFCk6inRH35kNTW0wR37s2QtktK-89UnJn7YdJElpEcIdfjoeVKu9jwVe37CUDhu65XEcB3OdDQkGWruwaRGhaYCZJ1Ospy2XIHXCMFRUHpgIkTPJQyXpuzYgymhByT_epcV226S7HDrUnB4Js6TyCE8P6Hhq1tIgR6MzTnl9RTnYZF5Qb9e-ouiD1bcIlyXKVF-0W6ml1O1jxFGWQlEeQkIsQ2nxspEz-0Koa-0eyr9jKCbvD0F82Ie5sY-KvUP43w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم لیگ برتر؛ دشت 3 امتیازی و ارزشمند شاگردان مهدی تارتار درتهران مقابل برزیلی‌های ایران.
🔴
پرسپولیس
3️⃣
-
1️⃣
صنعت نفت آبادان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31264" target="_blank">📅 19:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31263">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gml2TZm8DMBKetBqTwnxFpepzg2YHymiMbDEt9uUrLnTVy9xmwYXvsvqCVCMcnhUPr7-yo4-oJhV8fnD4kEasnSykd-sNeMEgeBU2sKuoUKRKzElwlE55tMeDwLF1SFf7c1NpahquOLIF0JACzdFkWW21W9ccaIRvnz0wK39_Ek7eKaExS7pifyroQQI3wmTSJIv0guXGDEToD2PL-SOVAmrxzTHcl8QVhNMXwBP8ttjQrVYqVaeC0hm9DZT5qOk0u9yPQnHuxDaS529L8-x30aDuVtUmbWC5c3H0KU48gXLxuXTDorPJKAytMA8Qw_HuYCWGwKKHnsQo-sHYHF12A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
سرخ‌ها روی‌کرنربازم گل خوردند! گل اول صنعت نفت آبادان به پرسپولیس توسط باصری در دقیقه 66
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31263" target="_blank">📅 18:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31262">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/866119f609.mp4?token=Eu7lZSOcy4mb2Jezc1xVF-7F_UMSGlA-s4QbvDf5I09QW-f0Qshuu1Vh-9nOqjD5NV2O8X-tVDYQ3uCN1LQBX-7E0xrzripE6PIADtpZ1CUY-H7On60nv2gV2aTsAc7wA6e6qXpdGxZT-B-ODctrY_y_KJmysrKxxUlCoMfz4y1k1HuUoriH1ctN2XSqNhzeOzPIrRvDvvhgRP6bJC1DKMCYsTtyo6U10Jkw9e1gqAEtdlY7FgJWv6K80IHL5i4qwzSJTMxi1C8Zol2PECkP-IJ_BiRnHHB5FQ43Tz3_L04zjNM0s_qXX5qlUMAzR2E9GvjI7BzC2tuyWaGh6z2QhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/866119f609.mp4?token=Eu7lZSOcy4mb2Jezc1xVF-7F_UMSGlA-s4QbvDf5I09QW-f0Qshuu1Vh-9nOqjD5NV2O8X-tVDYQ3uCN1LQBX-7E0xrzripE6PIADtpZ1CUY-H7On60nv2gV2aTsAc7wA6e6qXpdGxZT-B-ODctrY_y_KJmysrKxxUlCoMfz4y1k1HuUoriH1ctN2XSqNhzeOzPIrRvDvvhgRP6bJC1DKMCYsTtyo6U10Jkw9e1gqAEtdlY7FgJWv6K80IHL5i4qwzSJTMxi1C8Zol2PECkP-IJ_BiRnHHB5FQ43Tz3_L04zjNM0s_qXX5qlUMAzR2E9GvjI7BzC2tuyWaGh6z2QhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اولین گل‌ستاره‌ ازبک سرخ‌ها درفصل جدید؛ گل سوم پرسپولیس به نفت توسط اورونوف دقیقه 85
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/31262" target="_blank">📅 18:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31261">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aaaacac90.mp4?token=BxuSQav0NOcjCSwWMaDLw-i7L7H2wctFzXpSqj8AQAHMv4jxf26jfmnSy9a955ZVX1Sub-Pnt7ehWJNu_w6yyWldllZFCyvYrr35BE1e_cf_PsxMeWm27k_Dhza3_8mL_iYEBhUNZoaTqwy7yArjBAxbz5iLr2cx00CzpUTlWNuMCkqz9DkgwSKAxRMyY4YF9CawqE31g25LfHyRO6qG1iU7d_AXyPRtSBwFKZKAgQWuG4fJVaaWYpQ6qnOB9tmGMEa_cJMzwmZb2svcPKH_0K8SwEdjsNnJkIHaCKqunVESudrQCweIYoOaeg1RAuzjkFYj0uD2wOgX57IlHkBRTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aaaacac90.mp4?token=BxuSQav0NOcjCSwWMaDLw-i7L7H2wctFzXpSqj8AQAHMv4jxf26jfmnSy9a955ZVX1Sub-Pnt7ehWJNu_w6yyWldllZFCyvYrr35BE1e_cf_PsxMeWm27k_Dhza3_8mL_iYEBhUNZoaTqwy7yArjBAxbz5iLr2cx00CzpUTlWNuMCkqz9DkgwSKAxRMyY4YF9CawqE31g25LfHyRO6qG1iU7d_AXyPRtSBwFKZKAgQWuG4fJVaaWYpQ6qnOB9tmGMEa_cJMzwmZb2svcPKH_0K8SwEdjsNnJkIHaCKqunVESudrQCweIYoOaeg1RAuzjkFYj0uD2wOgX57IlHkBRTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
سرخ‌ها روی‌کرنربازم گل خوردند! گل اول صنعت نفت آبادان به پرسپولیس توسط باصری در دقیقه 66
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/31261" target="_blank">📅 18:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31260">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd9e6967b.mp4?token=SXGtqIZdTP1W5lA5dFaSzzdURueQ-KXmHvZNCpK8jZ7qTcsziR2aEMGZTZUdeYVVn5gXpq1MX_vSn7itVVJ8rjGiGyP-diYPz8kJHMov1mpqOCm8xSLvfPdnU_iLC5vT0n4IlG0engPg9oxEkjKFF5MBe2oRQ3M5KkJF0dC7Sy1wgnamMR5KWDM6Akk8JcyJQ-guT1q_ySq_ymiGewcwZVUaKNZuWq9AFOWZ5fgP01Eostd6YyRfisw7gma0iUVAeVxCAdS1_PszmY3HB4prKQxwV2dVq1p1yOns4CjTzakZAOhzQEyNLlz8zpZgHK1W7X59MsbFJHW6xulaeprgwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd9e6967b.mp4?token=SXGtqIZdTP1W5lA5dFaSzzdURueQ-KXmHvZNCpK8jZ7qTcsziR2aEMGZTZUdeYVVn5gXpq1MX_vSn7itVVJ8rjGiGyP-diYPz8kJHMov1mpqOCm8xSLvfPdnU_iLC5vT0n4IlG0engPg9oxEkjKFF5MBe2oRQ3M5KkJF0dC7Sy1wgnamMR5KWDM6Akk8JcyJQ-guT1q_ySq_ymiGewcwZVUaKNZuWq9AFOWZ5fgP01Eostd6YyRfisw7gma0iUVAeVxCAdS1_PszmY3HB4prKQxwV2dVq1p1yOns4CjTzakZAOhzQEyNLlz8zpZgHK1W7X59MsbFJHW6xulaeprgwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تثبیت‌پیروزی‌خانگی سرخ‌ها؛ گل دوم پرسپولیس به صنعت نفت توسط علی علیپور در دقیقه 50
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/31260" target="_blank">📅 18:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31259">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db73f92ec5.mp4?token=X1GJqsxLcFXSlFp27zCRi6R0Hg1xnk1sq8lsblI43-D2pxzRF02-DQHS6d6RoSXsC0w_ypOJMvbtzqUb4ShrepJ0Iqjh4nmBRhUgcPtT5YGPPD3WhD2EeDkBLWLpq9XdRZOiB5bs6DQPsgS7v2VQQDFsaYlyB8dpXm-zZtmJrubqYDWOL96nxQP0uH_1vT-WiblwH87Tb1mOIKFnSPgZPwTz444ob0DHI1C3Atc9FOEVaVZn6m5TTEwvVpKKYritv4ukXvAplPc4XrcdZAqlwOlzTlZ5r_5tK0pXDbMRA6Nby-ezXRTvqbDGMlVEzGS1b23CkKDNxP28ak0lk7Gwhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db73f92ec5.mp4?token=X1GJqsxLcFXSlFp27zCRi6R0Hg1xnk1sq8lsblI43-D2pxzRF02-DQHS6d6RoSXsC0w_ypOJMvbtzqUb4ShrepJ0Iqjh4nmBRhUgcPtT5YGPPD3WhD2EeDkBLWLpq9XdRZOiB5bs6DQPsgS7v2VQQDFsaYlyB8dpXm-zZtmJrubqYDWOL96nxQP0uH_1vT-WiblwH87Tb1mOIKFnSPgZPwTz444ob0DHI1C3Atc9FOEVaVZn6m5TTEwvVpKKYritv4ukXvAplPc4XrcdZAqlwOlzTlZ5r_5tK0pXDbMRA6Nby-ezXRTvqbDGMlVEzGS1b23CkKDNxP28ak0lk7Gwhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شروع‌طوفانی‌شاگردان‌تارتار؛گل اول پرسپولیس به صنعت نفت آبادان توسط تیوی بیفوما در دقیقه 5
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/31259" target="_blank">📅 18:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31258">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kODaRK0Q2g9mPOcLUrSpR2iTqDmq0nENNGQj5gEi8BepbfIPYJWFAzKbEWUua0DMeL27nPPQo5P9oOe2Y2AmtG1TVopRm91WIvIeNUsFZLfjRQ3auoNWgWB92YUg76U1UHIL2CAcEi_IECaUIlDa7e3aE-5lMfnOPrFE2w5-iCFxxTLdw7oRvPk5b2u2Xr4I3OojYWcQph--aVRQJP4xc3X7cTd5LyrN6REzhHrh7fmb8R4j-STOcR3hahqvMjc8CpZslP1Fb4gMsCdZ1_x49_iy9zC0vLS18hFzKWRJwC7ke5NmngnXwuRXYUJqGNloeOZSttHznJRrixBUK-dEQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
تصاویر جدیدی از بازی GTA VI؛ این تصاویر در بخش موسیقی وب‌سایت بازی قرار گرفته‌اند و نگاه تازه‌ای به فضای جهان GTA VI ارائه می‌دهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/31258" target="_blank">📅 17:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31257">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0462dcd97.mp4?token=FSlbpR2_D8xF-_6GDh3HD_7PxdYv9i6bXk4YAdCZRh4-ws02hhVy9fJ2_yKtYtztjo67T0sNrf7ISOCI2p3Gn5qTWe2AvtwPcBQXTwXt11qwB4OEtt-aelD_y4jbqEfMbTDMvIS4KmLUhLN4trXIl1MO0nKKfBLQJq0-ztTeYvPw6oLu4AkJM9dwP-OZvvnXOt52bCT76myAv6RynIn2f0nv6pcMrPDQR_sFJ6ekHwwLgpVAKm9bbXsNnCt_RhKOP2uUW3ynjZCISIslaWrziOgzUKD9kgOVoS27NNfKYS0IyRGPnz37k8LXW8_2YePOigKNn33kUEtq78h8ZH4wVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0462dcd97.mp4?token=FSlbpR2_D8xF-_6GDh3HD_7PxdYv9i6bXk4YAdCZRh4-ws02hhVy9fJ2_yKtYtztjo67T0sNrf7ISOCI2p3Gn5qTWe2AvtwPcBQXTwXt11qwB4OEtt-aelD_y4jbqEfMbTDMvIS4KmLUhLN4trXIl1MO0nKKfBLQJq0-ztTeYvPw6oLu4AkJM9dwP-OZvvnXOt52bCT76myAv6RynIn2f0nv6pcMrPDQR_sFJ6ekHwwLgpVAKm9bbXsNnCt_RhKOP2uUW3ynjZCISIslaWrziOgzUKD9kgOVoS27NNfKYS0IyRGPnz37k8LXW8_2YePOigKNn33kUEtq78h8ZH4wVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از وقتی که مسعود محبی مدافع تیم خیبر توسط رسانه‌ها بولدشد و باشگاه استقلال نیز به دنبال جذب او افتاد هر هفتههه داره سوتی میده لامصب. این چه اشتباهی بود که تو بازی امروز کردی پسر خوب!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/31257" target="_blank">📅 17:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31256">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/499a1fc96c.mp4?token=VXax-CDn-t7qbDL8mRn1ImJJlE40QokUh2Nkwif4bc9fUW_AZH4vkwAOVhCVr2gmxnJEckQUR78VZIp0JjYq_Nu2sxEeLkulNJU_IzuwFDCOn7AT3FUi6NN8zxxwhIf3UJlBgbjiiSUsweBSbz4ex7Fwl274XyFQoLYRQ3Jv4aGUV6wyy49k2ErEwiWiZ7Ei8K6RMDeTSNGxo_ueyUwGQX-gUX8eRaf9fOEVrMtBd5JJYskvH87BDxG0Hi8VajTfwO2xWvYCiRr0NrF2FsQ7fk-zFpTcaeWOBY2hzf-ZGR2k4zju8lv20UxI7dcHd6aLRKIsqUI1_cevwZJ51DHVSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/499a1fc96c.mp4?token=VXax-CDn-t7qbDL8mRn1ImJJlE40QokUh2Nkwif4bc9fUW_AZH4vkwAOVhCVr2gmxnJEckQUR78VZIp0JjYq_Nu2sxEeLkulNJU_IzuwFDCOn7AT3FUi6NN8zxxwhIf3UJlBgbjiiSUsweBSbz4ex7Fwl274XyFQoLYRQ3Jv4aGUV6wyy49k2ErEwiWiZ7Ei8K6RMDeTSNGxo_ueyUwGQX-gUX8eRaf9fOEVrMtBd5JJYskvH87BDxG0Hi8VajTfwO2xWvYCiRr0NrF2FsQ7fk-zFpTcaeWOBY2hzf-ZGR2k4zju8lv20UxI7dcHd6aLRKIsqUI1_cevwZJ51DHVSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
شماتیک‌ترکیب پرسپولیس برای دیدار امروز مقابل صنعت‌نفت آبادان؛ علی علیپور، کنعانی زادگان و ایری بدلیل‌مصدومیت این بازی رو از دست دادند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31256" target="_blank">📅 17:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31255">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7613725c1a.mp4?token=qirtB-FpztuOIMMpzgBmnGwNk_kGaubC0FDlaccigCjF3RRwMlrUrOxz90BFuAwi--nixr8NVgwmyXdM5OjB_alUcLWVC39zmUy8nIcCEucdEf0GySGCLfcluFKUmNV6cv0pCrvUZoY_w5DsrFvJoTavy7R-OiU68GFNYf6pCyDRZZOChynorqssVY4EV-C6ypiVfwSQ1oayB-7H_TxrCOFZ1sOBygySpizk_uq_85edc7alS5CuNIiapZGsNWDtJqY_5l80LjT3IgSTAz1lsiqqBhh-cWdBqrpVNV4riuZfOwEN8gRsq7B6ELXBsB4ghFce3WV6CVmREGreocCWCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7613725c1a.mp4?token=qirtB-FpztuOIMMpzgBmnGwNk_kGaubC0FDlaccigCjF3RRwMlrUrOxz90BFuAwi--nixr8NVgwmyXdM5OjB_alUcLWVC39zmUy8nIcCEucdEf0GySGCLfcluFKUmNV6cv0pCrvUZoY_w5DsrFvJoTavy7R-OiU68GFNYf6pCyDRZZOChynorqssVY4EV-C6ypiVfwSQ1oayB-7H_TxrCOFZ1sOBygySpizk_uq_85edc7alS5CuNIiapZGsNWDtJqY_5l80LjT3IgSTAz1lsiqqBhh-cWdBqrpVNV4riuZfOwEN8gRsq7B6ELXBsB4ghFce3WV6CVmREGreocCWCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بخش رسانه‌ای باشگاه خیبر خرم آباد در اقدامی جالب شماتیک ترکیب این تیم مقابل چادر ملو رو به این شکل "یه نوع شیرینی محلی" منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/31255" target="_blank">📅 17:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31254">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAPKOlyd5xe9nZlYsD5e-hICNPqwSvmB7-fhehSkc_RdJZIOm07HmErhnfpFQKlMSpWDLvWGgV_Vm4sDD8O_4HC9CDl6Ier4tXfpu8JRU_teXijQFd27KMNcMpgCf9LrLo5i8k5EukWeSKZtnZoLpzgaukfrP7e7eWw_p-2DbhPf6-yknYhZI2-hHetvBbgjgGnXs8idkHf5ktP9bWFEuFxUZ5ah11mJDEz7s56Tn4w0y1-rpsURv4_SILqlKckLGLVtCTBP13ILr0OGedGRk-f6REttXZyjdo5agazZGOkFC2R-cNH109aKWrWvb9ml2dt0SwkrO_ZYCpPZnmxDSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل بازیکنان دو تیم پرسپولیس و صنعت نفت درهفته‌هشتم لیگ برتر؛ مارکو باکیچ و دنیل گرا از لیست سرخپوشان برای این بازی خط خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/31254" target="_blank">📅 16:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31253">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‼️
#تکمیلی؛دستور واتساپی‌شجاع‌خلیل‌زاده کاپیتان تراکتور به‌بازیکنان‌تیم‌تراکتور:همتون علیرضا بیرانوند رو آنفالو کنید. او دیگر جایگاهی در تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/31253" target="_blank">📅 16:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31252">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMKoLe8-VA0m_fw5M_OKPiTCUIiNmG0G64WMflLzKARn4C5gVVQX9SPvzrVKv15Zbi6MItK4XsEhK4cPw3YMuajlRTBZvTQbQgSaFIAlBpPAL1BJDBmgTFQYPo6LMiecZkDB5VAuqvmdryYJbA3Q2gkW2KIoajy2nbgyllPaeOFiKOIrTCE8dv4-ZV8NQ4_O4YIu1qMjuRVE000plP1i5AhMpWvdytcefDNpmrI8EvZNp4KCrksdps-PMv5a1Cor0jqTMsx0upo7CP0tXKt6PqtN8nFl8f96SDbR-v30zgs_8-WoFZvfa5GHHlnSxEF-mXu5ULTFTrzH0Jl5Pcfc-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛ ترکیب تیم پرسپولیس برای دیدار امروز مقابل صنعت‌نفت آبادان؛ ساعت 17:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/31252" target="_blank">📅 16:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31251">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJdQbb4PxZdcHn--Kc-XHbrVtmvmmUjtKPNAzahj3NQ5wJ9VI1B3I1hMJn-xhEa-OYJ3hEEO-SPCSSE6j6dNFaiMTAYd_ZP9vb6gyho9VoVMDYzIB69fYZQH3Jb5G7dclg5SPmd__awcP3zbaHh9af4ouRgnxjRbovejlwGhfeQVQScMWV-R8dD7QZ2D-NO0_Vj8DwfX-W_o0WX9JeGxZBiz9tjKFVum3duKSOm52Mj8EmN-MhUwUBNjwzYgazzkg0RPzV1iknhN4zbKbDN1wJb0MZ9O_VaDGyHV971VU4ZnOK5pnJeUamnhT2ywZEspVrTHSpycBudQbG0p9flIGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ همانطور که‌چندهفته پیش اعلام کردیم که جدایی دنیل‌گرا و باکیچ ازپرسپولیس در نیم فصل قطعی شده؛ مهدی تارتار نام این دو بازیکن خارجی رو از لیست سرخ‌ها برای دیدارفردا باصنعت‌نفت خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/31251" target="_blank">📅 16:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31250">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yx7eTZDfIyRDOjN4h4zj2_e8vD7aooP6HQq4CFeMikdUmSdCw7e4ZNdvwAJj3Ixb-IpztPfbrTyD-PpDeNxxppywxBcHgPLGcwQjDfI4nUJQksHoVKCWWIPTJux9geu56HTU95DbzXA7NNu7txSxKR09wllntOHFa9JgcwufwMjbTF6nQWVrlzGBnE4d3GxOILtEbHfgNz5f8qCfgS1FxUNdLCyNolmpSbkltlztUtirGKROxQ1aZ-el0gXLQbz7TBHnHTESH_p32fwTLpbfAQNzXksC5e69zhp-GG6g7t0AuvK6fvV7VpsXhas3gh_h1SoTPUu6b51FkRM8SIfYaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
به احتمال زیاد پرسپولیس امروز عصر با این ارنج به مصاف صنعت نفت آبادان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/31250" target="_blank">📅 16:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31248">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MmdjYFxHIGKCJXTWI2N4civbyqY8MQd5et94Mrr5y7QB2_SbJ10D_Jky9GK7rHRIMVgBIOcF0Iu6n9vfqhOOzJmwbyG9nc9HYMW-9oGFqk7tzFj3PgtH4uUcxrTA7KaZ2MM8Q-8Qq1uGkdCZrn1IthrG5mOFXZyH1EsMDJmWVQuCSuJRHlw_qwV-YVuxz8ajfAXlHxwMEEIFK2wVS8KXnGozyao0z0eLr6ndqouh8Y6tv668F2qngfcI-R_FlxZwFR1xDUHhpHiLrh-XfwkV7BswoXv87bP2l1iCBV-s28L3DQUUaq106uhJlYkes_TwDJj6V_wD4hoz_aZ3crKA7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GIdcUoSFuComafbAeag0Tti3dPjWqEM0NmaoxvJ8TAL4stFuNcWafdvmDbfTMOyrnlSrrXKABZar8AOctQx8Tm61PtDksT74nZpcNwjDIVNzR9EEMG8pT6LW1iNFqw_JCUpHCUai9tJ6hYkyVuSYlmA7ZvFkABMLcnCMZWQvxIkiSYSt_v6OEEdtZmEXnieq-9uXzbkftp_KPqU-7zIxlXJlQ7hc87WC9-CEqgQsXdf5pwJLeQlKwCtW5XPxIy01W7IzcCc6q-_UEwxWBZbB4lBs8VZOkmCr6987oeKAmV0ss7iFKFp3QNijeUR89M5CqB0gNDPv3cOZLex3CcEjdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تشویق‌ده‌ثانیه‌ای‌لیونل‌مسی شماره 10 آرژانتین و ایستادن به افتخار او در برنامه ورزش و مردم بخاطر خداحافظی او از تیم ملی فوتبال آرژانتین در اوج.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/31248" target="_blank">📅 16:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31246">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6kTVpEwWjkj0Nd8P1ry4ztcDGpuQke9z6ayc4d-IsYma_Fg9rL4QvvSdsw_qrrZ4xRNRxbPga3kklpG59EfnpYaGltUqOReRYshO8YqJSwEIx4D0s9oGuttumU9HpC-XmL-AEpcuEsNDLN84K8oAs_W7zWK43LWe9CvTblfVjC6OkGLnyC9rUh6qwkMhw-isPnivCvJxJ3_YvgOqBipwlMKmV19i43GFiFNtEQN0kP9tVgm7YSQye_7LgHyplZRgWL5uBM8-D_jYyn3jq9gDJwNieZ5EpbO0yWQ6H8SWi49KaIJoprSJ_PWc20LfbcuAVpjj8iMlHGwREzqCtR8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیمار جونیور، گرت بیل، محمد صلاح و ادن هازارد درکل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/31246" target="_blank">📅 15:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31244">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2089087958.mp4?token=p3ln3KuFI22HXoLco5VmIbdx671p_G1_V79C7Uhtu3NkZmdWjv_UdHo3SexEbKGoXhsp3sg6_rovg7dK0haXq4wozSzAriGTETuOXUf77Iv4YG3wnyVAh1Eocgw7s5nwSdiE7jNppFRh6eBAqmnZjPFPs6ckFRgB1gewbWmp_0iee7UFzg6NW8JPlGshW1AD3-RbgeF4k6z352Kfxl1_-o_KeRq11TIil2lY3NLm4ym42z0zyely0zN_m__m5rgCoU4TVpYKImYbWH3BLlK6y2KsXK3Xi0PqsrNOw4prls4C7gRQpeW8xoHoPa3a-2FQDquJPiCYJstIBotvBE0WEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2089087958.mp4?token=p3ln3KuFI22HXoLco5VmIbdx671p_G1_V79C7Uhtu3NkZmdWjv_UdHo3SexEbKGoXhsp3sg6_rovg7dK0haXq4wozSzAriGTETuOXUf77Iv4YG3wnyVAh1Eocgw7s5nwSdiE7jNppFRh6eBAqmnZjPFPs6ckFRgB1gewbWmp_0iee7UFzg6NW8JPlGshW1AD3-RbgeF4k6z352Kfxl1_-o_KeRq11TIil2lY3NLm4ym42z0zyely0zN_m__m5rgCoU4TVpYKImYbWH3BLlK6y2KsXK3Xi0PqsrNOw4prls4C7gRQpeW8xoHoPa3a-2FQDquJPiCYJstIBotvBE0WEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
شعرخوندن‌بازیکنان تیم ارژانتین تو اتوبوس برای مسی : "لئو تو مثل اونشب تو قطر جاودانه ای. مارو ترک نکن همه میخوان تو بمونی و..."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/31244" target="_blank">📅 15:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31243">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sz8qgv8Fg2jTMvPiM__N1_AK2Risv8TTicnnVZ14Sa8PLwmxg9yUCDHShZsMHrzUFNxK8nVL9S2HQrSIK8DR166vbT0IN9CdLxPsSrV34kkYtIsKHvhfx2BzT0PtKdqd3dOg8-z5rZ1bg9IlvkclGIDoDne7bnLVnD9QC7fzC0rgYtpdzNTbE_aBc1ZIrOfCvZ3WQiP41GGXP_BLdyADFudG2HtPVKM8ixWJ7GVaJ1SZcOfwa7B6WGEh0_xOTWKu5HuNZ5J7uxlWZtLEMWLLjI9Qs_SE14xkSnqjB_Y0zYX7vyJzzDV1tdm_xMIlhBumGr3Ut69XWSix_pQ3ZcTP4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
🇧🇷
#تکمیلی؛ با تاییدیه کادرپزشکی باشگاه بارسلونا؛ مصدومیت جزئی رافینیا دیاز برطرف شده و او مشکلی برای همراهی آبی اناری‌ها در بازی مقابل ختافه در هفته هشتم رقابتای لالیگا نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/31243" target="_blank">📅 14:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31242">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33992a38c0.mp4?token=E51ONHG3TxXqEECmNblRaBWOMZvqcnyO16Uj-LGX_y8wwPn9PXXyf5sfNo2sThojrN5TPgcaPg8T3xv97_k6GDZR0XLSTLjSBmBg2rVeYbxxodROM4a7wtMx36Y8_09Kj_Wxi2nEVAcPEFRLbmtyYoT7YwedWylRgnp2uLEJ1zqE7nIc_GU9MXfk-OyLa-EpTkYUBX_Br8QPoOXENDIEfq2tcH3orr2flAP87sDEXbtq0jm6-BnknmnW4ipyPpNTU7NSQ6OmOE8btMf5p-Gk8Tptj4zAaoDysY_9p8LRA4Gij3iH6EpRzh7hBe2RJvTR3G3_9iMf7KwRr_kuUHofRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33992a38c0.mp4?token=E51ONHG3TxXqEECmNblRaBWOMZvqcnyO16Uj-LGX_y8wwPn9PXXyf5sfNo2sThojrN5TPgcaPg8T3xv97_k6GDZR0XLSTLjSBmBg2rVeYbxxodROM4a7wtMx36Y8_09Kj_Wxi2nEVAcPEFRLbmtyYoT7YwedWylRgnp2uLEJ1zqE7nIc_GU9MXfk-OyLa-EpTkYUBX_Br8QPoOXENDIEfq2tcH3orr2flAP87sDEXbtq0jm6-BnknmnW4ipyPpNTU7NSQ6OmOE8btMf5p-Gk8Tptj4zAaoDysY_9p8LRA4Gij3iH6EpRzh7hBe2RJvTR3G3_9iMf7KwRr_kuUHofRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهترین‌نمایشی‌که‌یه‌مهاجم مقابل ایران از خودش نشون داد. استپ سینه‌ هاش آدم رو یاد پرایم زلاتان مینداخت. همون استپ سینه‌اش رفت تو گل ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/31242" target="_blank">📅 14:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31240">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/go2WeAPtKpLHsSsFaKUJEXNUbThvUPMsGwCPWqLsyAxvW_aTMIEn3XZsm7R_x-hSi_YVfb2vgWV5ZJ1Og3JlqKIfyYO71Ln-wYckoK4XgfM9k-8JHWt0IxsONGW1JQdBp928d5R7q88gIDgSQzog0fyRZNh0FW-YUSvj897VJ9Ndn7XVcokvAx74W_hu_Uz9TaALRHY7y_hqCOf1Tqx42kSnZ8kOnUENAD7IssoNSaM39YnPv3ZOi3RtDf--BZQBjiMgf-gAcnEHczXpfqt78zl9TkuTGA0rdDu2jKUxALD8wivABHLrov-f_Ki6ASZVrBIaBa60myxh-rarPSpl5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i8V6elOibJkq_alwR-B3rfYtxCVM4e3T1miX0RoOuE_1S3PwChcuWS1phSE5QcIkGSIsH2t3dpKjFSMMf0zMidcffxXxRr2vDNyN8G-MBpy02Ee8Mc9Ab-ztQBwBQV6sgeuJIZsU6WXgbCarX1QL65ZSHxttU7crisAT8RbqLF3wzF8OgULJpp3Mpc3DH8q6tnj1KjbI3oS13aM8vrECpJeVtOfZ1zPYLYeHpXnmgNo7ZOVddySTZ97nypxQqviFNOteHWuAf8HNJ0mVQUdawa86jS_uaCi2-8x0Jl-0qtq-NeS0d7pKfurBMFC8Cd3JWaJXhY23MM1MWN9p3pJi9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
حضور بانوان هوادار تراکتور در ورزشگاه یادگار در جریان مسابقه روز گذشته پرشورها با استقلال.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/31240" target="_blank">📅 14:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31239">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLiInc117zHU-dbkdRNzY4qWk6QPQh2SwQI4Iy1CxNVLRDT9OlP1ZdU7g95TFvNpk0o7wPXodzMiaycxrH7golXQW7zj6XELcu-Wk5r6I2-Egbt9Qd9K-Jy4bREg1orR4DHn8QmQwQ40y00VW44FGm19t3ZVvl9kqapbSkOyWAFdd-qFHDxXGu8O8OKpgUh6lmvNFr7Ga1BGw5iJlJYr_gm12KW-qw0PcKhf87VScacq27yxVZ3nFqS2YWJqPcdkYXATNqvJKuWp6vGIkqVyY-4IAOybiYfXLIqrRx_mzNeKBw0BTq3RNDjFanJVmb7bAfyR4QAJ5wtvzyGECRan8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های دو تیم پرسپولیس
🆚
صنعت نفت آبادان درتمام مسابقات: 48 مسابقه، 31 پیروزی پرسپولیس، 6 برد صنعت نفت و 11 بازی مساوی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/31239" target="_blank">📅 14:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31238">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRTJc7QIILtQc41CylkUGBDBHY1xT_-kMKAamtVz3UYaz0DdNpH-t0BXY62blkSTm9oEITdsSxu6Zf2vGZMAUnZYMqmGL3uNViwtBJ72iBn3fb72yO1N6g4ye8zrYLvyF3lWBwGFlLpbMBkNLvG_vXjZW79YWvt1AH7wMcjEM-iWW_dQN3enTEBaRr-N61yVamL7mhsotK25znAua2p2DpllQzbB48sSpZk0uicyg_yTdpfcwQ_5eWiZhHZgbKrSqF3SZIJ5WuMxp468nhYreCno3FPRq5-OB4OTOFKuHMMTG-VzGNIFqR4SNeetcwiWrVQcVZ1weEHQSszFnH2lUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
دبل نیمار دربازی‌بامدادامروز سانتوس در لیگ برزیل؛ جفت گل‌های نیمار از روی نقطه پنالتی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/31238" target="_blank">📅 13:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31236">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vJep8CMvhfAvjA7sPZJs8IhsUv5hROYNYH0fvrJDE6VhG5HMaOU7nijOPITY2qFnu1ogmZZXNWZb6Daw0XVex53uS_m3LkhsU6GjRgyhe4SPo6OT97XYIdPP1jXj-ifICoS3kOjsCW2AVKCnj-EisQ7Wh7m082xnSuMiO6FPPrTs1NQuGm-ULQGVXpRHUbuWOac4c6rFrrVG7uQ9FdOc2QnbVdp5YkBONqlWq7-8hr10uFdBd5-qsLpbAXiDu6Wu7zMAjpq2A11udlzDlG5ldfvbugjwVS5lf0Mwi1G8iuCx-tGnQchkeQzA_kvR5DpB1b5Nv9wY1UFoTSgLsVEDnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aiODyI4aR6f_at46NRfRBv0o5oJOJXBQUEg87xplHi_g1sP9GT84gL4CXytmrsprsEOYuD8M0vlblVhbVA5soASRG18DMcwJLjBPXeYWvVC3BHPwvV3l_W986cUVP5acxDelkeO5BNbhOWaY37xFxal6Wz8YAMUwqQAPEHbNZ5ySgiFxE_xneQuLjT-_Wti7INPnRfWgWygewbyrCpClkCNWumsU12-ilGupI20zncRl12bUYDP_2V7iwRJ9Ja-2TljHbenNpppUKW_3nBjU3tEhoJFPj9FHwPmwa2W14QHe4gTjNlvX26swLbgPywlnTQ_lskXHYpQ1qq1QmBDYGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صحبت‌های تلخ همسر خدا بیامرز هادی نوروزی اسطوره باشگاه پرسپولیس که با گذشت 12 سال از فوت هادی هنوز لباس مشکی‌اش رو در نیاورده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31236" target="_blank">📅 12:13 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
