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
<img src="https://cdn4.telesco.pe/file/U5RxoE1iJEI-7fuDf2Nu3CUZgIY21fSNpUzBk3d7MsUOesjVB_JTLs1WrH0iSJ6TQ58el6lburtmLbi_ji3nIjJmCcouh--SjaOMlD9uJ7zs10IxhaoPn_mKQAIsX7NPbfS67bDOqeIkXPqG5DshmCe2Xl88gkzsCAEVDDb5pXm5cIBbDuMFS1nI2hk0Uu27FO63WGbQkd_hBQGQEH9JNOk1OUJXfJ2tNXHolytDMwauVwOA69O0OPpTjNB7FNfIDptGTkKltf54R4kZkultVfFaJrHTyRXdZfpVjKiUnYQPF5hxQ5fa0wob56sHdKQP5x_zL691FNsqiRnu4y_nUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 487K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 03:30:25</div>
<hr>

<div class="tg-post" id="msg-31350">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1KzKlBUCaWcLi_RqYRmB9V4ILL4lovaR_QtrULVOpjkcVtxfCYa6pX88b6zAx35VeaAEufl4LS0IM6Lrgk6Vh6VHAsh31jiqFScWVgxL29XPSD3On3imjaxGdGrNYnvungB1KLitCpV413nZCCDnRnsFIWgfp7363QoQoYpY8SsSPjMLViktOGdP3KLIsrGfRXM0wwLmHTY1_t1aZxsON939YScC2UzZiZ7Y5FCn42zztJ4vtNvRbSrJ7oYE_zVYjhbWaAJ6_CqLjzAdxpOZE3Zd65B6VBET095pQtk2fbPQAOLreS7l87E1L0Ho050OYX_NnOQVe2KqhRWNIvkOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌بازیکن آدم بشو نیست؟! اخراج وینیسیوس به دلیل‌کشیدن مو سر بازیکن حریف؛ وینیسیوس که توانسته‌بود دروازه ویارئال رابازکنه با بازبینی صحنه به‌ثمررسیدن گل، ستاره رئال مادرید به‌دلیل کشیدن موی بازیکن حریف از زمین مسابقه اخراج شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/persiana_Soccer/31350" target="_blank">📅 01:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31349">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2B_LIbMtgiMIDdLM4DBOXWB4eJ3vrnYZX2yS7d0Eqh55ii08X7GlGnzZXlgEk9IFTBifLDGnFNUV1Cc4sMLlli24uvyMhBgJ4aEsoQFm5HMUyx73Ym-_ZMmrGRWsvp9uzjbkCeWwCp2mWZKIIwyGqP9UwETQzLO9-MKD1PWzqFCxejj_Zi9DCPMGsyySv371wOo8D-AOV9afFX10iyiE7L3xehc06SJLQKqJpz6wSE19bUZGrsfV4qtwN7XMdFde72zJsfT13zxaMuyfcPSupaMA1R6Wdw-__9ckvmEL2tvkL9-UpytJTQEyVnK8LIVQLTzGRaAy4avGDfcxfh2ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ پیروزی سخت شاگردان مورینیو در برنابئو با تک گل دیومانده؛ اختلااف 6 امتیازی با صدر حفظ شد. وینیسیوس ممکنه به خاطر کشیدن موی بازیکن ویارئال دو جلسه محروم بشه و الکلاسیکو رو از دست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/31349" target="_blank">📅 00:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31347">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mEyp7TP50v1m6cikBHno_wvn-tChoYA21nxkQ1T9T63ebEYOpoT_IPP_ULmAIYinZNmvtOrb6_DoHbhlAb6NLi6D2eKr69CLUjNvWzIoWo5C14c3dylW4iHJznmqpQ3k16JDJe8UGdYU_MRHAp-djGEh9jjCXOpdFqYTltq9-l61BFzn4kU9dSQJxsbzqsyWmnOdQNVsQ0vFcOUemjNoY3QEDi4-JNCpw8cvvyejUdcoj54gtQ9JdGxWiHtSv6VYlpJdX9LiVIzTGBZYcueu6TC0oy3H8hrctHPoa47klsvW7rfltQFN-njQPFyt7UQoNRUlrLh8iGlQjeI5f0AQdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GEW-F1teniccTQIalmSv8yC0vYyTis3LBV_MOst-veO1pp7pio5p5XUheLVywL-XadFOTxyPRZOFUtG9aeQc1h_0QVIuKQmfvRlwiJiLdqMQOCFmnD2loEPzxjymYmgOyhGuegsKrhxD6avALF6_3bDcCYqUrs42BfCtEUf32PePNsmiRgBUX2SSx_kYVnvB0xlLXDhidQDbXTCE5jKf1pJMWBMsTiZyt0y-vp5eGMmCk_sxhAnWYzHaxD77egoM7X7hC4sO7tf3S-UZ572TMI9_RXfRUkdD9ck45z9MW2g5T-4gHBwE8GdEqlkIUQi8-7nbQ-uEaG8kphIjbQeThQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
این‌بازیکن آدم بشو نیست؟! اخراج وینیسیوس به دلیل‌کشیدن مو سر بازیکن حریف؛ وینیسیوس که توانسته‌بود دروازه ویارئال رابازکنه با بازبینی صحنه به‌ثمررسیدن گل، ستاره رئال مادرید به‌دلیل کشیدن موی بازیکن حریف از زمین مسابقه اخراج شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/persiana_Soccer/31347" target="_blank">📅 00:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31346">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFCYTc1fZNuoXanWVlLpgRg8atF3t786yUj3B77E8Zh9yenBtWzq7UofDvfov6ZMHBnHnFN9lOHU7w3X6sFrdhRX1TrhNl2vQNzAW3sB-45V79pNej8udqjJ3-sRM9YBoYgH5uCtdFgtjcVoVH0RLucmj8aF39lXxwzyPJAZgsDC3cJsrpGQfMKB7otz0oNEOg1m1pBVauCgzWaXN7u2EaA8JEgd7qC3mUZ-bmUnVY_WiJIJf6eF7Ftaf-pczolRMsD1wXkMqWeDo8sftuG1W9TRzTOMNR-Xryj8dQyJ5HrKOWFHrwq8IdsU-t6EY6bUikYvHoXtJJehmlbJJa1fNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ شماتیک ترکیب رئال مادرید برای دیدار مقابل ویارئال؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/31346" target="_blank">📅 00:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31345">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crL9JSAT2SzRYiWF4hR1GzxQNmCM4YJf2o8sIutnvLqzlk-pvUTLh_pqNpIEJy6uWe-DuC88bbUb9t_jjVyaPt3Z_FhgUGQ7tWEPIoIMC20qNKJF822MCvBbCUzbNAMBhiQCd4u_XnCWgS5_aBTvcTJK2eD5JImdD2VnUwcB9UF0p_EUpNhghEzJJ5LtGTUPQp6EheLUQDLSTtxNvyZ6uWlSTzffpkn2EiovyUMxYATXVtDl3uqdmqm7DJ0N1GUpp4nDPwd2IBx6lIlRi5QUVFZEUJm8EWQG2ElhxfbeVD0TmZPsAk9W40N2wxeSXyfUm2HAzYYr4EfkvKi8M7rTPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برسی عملکرد پرسپولیسِ مهدی تارتار بعد از انجام هفت مسابقه در فصل جدید: پنج پیروزی، یک مساوی، یک‌شکست، پانزده گل‌زده، چهار گل‌خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/31345" target="_blank">📅 00:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31344">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRbrVTbZbCVywcvVmY0vNq3zz1xlrDYbR9szMt6fIXRKTXN0P98-rrlhoQWGIF8aOWMX53yfKVI3aN5cQ_nmgsAVng6OymE17ntPycPE-Eu1WOZYcuwUpn1q4cqTl6T3KwbloDpml4rINA5TS7OOfAXjWIOM-Y3wh24s0SslnYnoDF31sUOu8QP_KcbwWhlq5LjT-YGWnaBJTGE-uUXlNdgqLtBi8VZdvfK9wAMlEuwFpVXat401iMtPM44JWJx1ueoGe0wbsAqopcwoS-nQT6cUQ9Gkmt3NU_Iv-3cv9lSzzr_06YaMEXT7m6pKEgo822d46uG0spHHLELSZ12s-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ یاسر آسانی ستاره آلبانیایی‌استقلال دیدار روزدوشنبه مقابل تیم الغرافه قطر رو از دست داد. این بازیکن ممکن‌ست با کاروان این تیم به قطر برود اما قطعا بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/31344" target="_blank">📅 23:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31343">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
👤
برسی عملکرد پرسپولیسِ مهدی تارتار بعد از انجام هفت مسابقه در فصل جدید: پنج پیروزی، یک مساوی، یک‌شکست، پانزده گل‌زده، چهار گل‌خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/31343" target="_blank">📅 23:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31342">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTC24tUxzaNVYF1ARNgVJ-ZkneRHHer4tRVN-0g9Bd4s44YKwNy9-vspDwo8OeM1o5h1dHKkK_Qmx9Cej3jKXxG7Z33Nbb31qwjlQLyzzrLpbBTThRwDDXT7r_n96cpwbCRW9uBaG72_fzOo2XNH8miJkHF9XA61QrnuYcCM46UzfrdMgiz7zkt0NkfQXFAtZaUxpGuQNEAZRvY4FfGNNIGiN68h4ZRR7oG-KuJpqn9wyBacR2B_9-4TN5tgXMj9RjRAuwjSOvbbOBJM-FO7AbAS0aoeWyKhXKvWiypUWvwRS5eBUmW7XGeH7US8p_oWua1YEujwDQsWblUGTDzTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گلشیفته فراهانی با جان سینا فیلم بازی کردهه؛ چه لبیم گرفت ازش. الان دارم میفهمم چرا حکومت داره تلاش میکنه گلشیفته رو به ایران برگردونده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/31342" target="_blank">📅 22:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31341">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/31341" target="_blank">📅 22:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31340">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇪🇸
👤
نتیجه دو مسابقه مهم امشب؛ هشتمین پیروزی پیاپی و ارزشمند شاگردان هانسی فلیک در لالیگا و تثبیت صدر نشینی و توقف شیاطین سرخ مقابل شاگردان دی‌زربی. مایکل کریک در آستانه برکناری از هدایت منچستر یونایتد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/31340" target="_blank">📅 22:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31338">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXK0jGiHbTqhSCMUm_LJ4U5ip5uGW5NsaNyS207xUwPWP7d1CPcuAfFYcAbiv4GclRV2DIUgHpeQ1pbl1HvfjiFus60_FE-w-lgziO2YmVuT7d_nDFj-1qq5tfxuv5bour8zSiObPvg41XnWsmUTlEeKFTCk9wzP2PZHYnsiSjEqJbPhCbHuBpmpp7V_R9SPqJuYoIQkIH9QmhWEutFDdSc3E5GPqX4RoNasouEaJg0aoiKeSxlr3S_7alifyqtWQlFSwXdXTB6RfLgHsLh0sgk7ccl2fuqZSB1J0CshLdyFDrkSRrLXttYJ07-tsPuTtNna0E8UxNHr0VN1c7VjbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/baFcdfkpW6PDV093A60nkHIRwgJQNKXnCSiF1tcjaC5-c7s3paU9P2NTQcIhYQWR6CuQQpcXlNxGeENYLqCxxGujr8czzL2WhZYQ_PQsJYpIbk_pRFTRByXZ0Q3hZXFrqmOrIxySO6nzc7dF56zdirjUsg3G295SWzhDS5br7I_LjalOVZpDrrxfXyDIdkf_dbieokRu4iSrsNqUnrYGGqmn7VVxUR7r-TfeeCpnb-oL3kEY2ljVk3nTVjdaBsZq2uKcUQ-IV6kmO662WWjDswaoD_vBd4H7skh4OtbEy6k6v1AJFRfJNS7Q0CLUtUswyiaCQseFCVXXGA4QKMpSIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته هشتم لالیگا|شماتیک ترکیب بارسلونا برای دیدار امشب مقابل ختافه؛ ساعت 20:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/31338" target="_blank">📅 22:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31334">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m4x6ymjr5xDw1ye1_4VvZFXiB1sJoi3tiravP2ozZLI9ppaXBZlkiLmnUW1DqQkJY2VmBadxpd4-1-mjrOhBXh_GI7gJXeWw2eApXhrYN0wNAYcRaHnpad1ReWExS-SQhSSqgIz30QvAoyG2VhJMpCYt186AOdqtdWqsyaveUTeXy_-Rd__Kx12LJeTK1N240oVzaahC8S86wsvSa1lu8-NLv8HbsxuOEVg-t2SGNizD-kvC5fk-88k8YxHkOaeIPsvqbvNMXnrHO080tsKra-dvX2DS3wflyWUcoEdle60gNM6IRv0zFyBYlIPsO0JeiFNE8R22FyVg4In6gkemkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bz7snkM16oxFKKLj5yM3J0UvDzEx_JDyV1f864uTofuXjyKS3B0IzQFHvpg_2gp2Lqy2XhzlYbCVIyoePTb9HDHHAWtkdqaabW8-zEnJ03BEnT75u-sk15wzfjTR8zcQEjMkHdC2HWtV4sorzcfQNY900yaOYBR_cKJsUdcTIgT7DRiXe7yfgkgPHcs8hH513R8no4_0MeKZYhFRV1biQcHH-JGILIuvR29pJeNBMZ9fSc_d-wQgsZDr9Fom_AD7AfyrRqHUcsg1cEY2XAWX1LjR5x5XA-HhWc0NZL6r4h2uevp4_T6v5nKl3X61BRyHsHn6cVoNUwKMNEFu2fA2dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ شماتیک ترکیب رئال مادرید برای دیدار مقابل ویارئال؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/31334" target="_blank">📅 21:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31333">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXDCZ01sc624yA39l-9NqYM6z7Wbb4DJ0u9m4Nv8OcStSdSX5JSZQxyhZMNaiThEytMgEb-09GyTU2K-FzRcP275e0ERC1kJlJ_oLClmDWaJgVcLEYJdEJcLLvprn1y9D4K2cs-0POg0eThDCwNhKy2PPRypD21--p_eRG0uSHwU8pmAL2g4ZKMc2xOKxhZ2Hp8hDyk-H_nvgIu-VR1MbmP60BdICKsfrkAHQML6FSm0V8tC6Nm1Ny9ZaK6VjJ5iEyinasLRHoJqt5A2Ou6cNRuj-lrZBgh9D81JBIuLbwWIFpfrK-XwG6vE2yu5wpz0On-XqrHAda_J3AXFQBVRAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
رسول‌خطیبی‌سومین‌سرمربی اخراجی فصل جدید؛ بعدِ شکست‌سنگین فجر مقابل سپاهان مدیران این باشگاه با رسول خطیبی قطع همکاری کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/31333" target="_blank">📅 21:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31332">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsjCExMJYr1uVZl9xzscOd3A-KCyfCg9w1GLDmN1tHAoIsCtfG7qreWk6bPRVE0mQCLFtQAFy7PzfkveYRUouT8AaNbq191_peFCETqZdD8eEUcynoG9ohFmK18T_O10MkatVBd8ovAnnxPRf3gQUyBHHlP_h5xg7p5Fnr9zk1VDq_ROnLfJ-7XIRsfsUlaJT0tQvvQlVJNxqVJVbguuTE7Dso-AdLslB3RRJLMPoF4rJayhrBlLq7_guelbFO-7HkZkWNUTz3ueKbUYRJvNvsjcWV4Fj0lhPjD0YPs95O8nrWa8hglviHLL1S9AVHj98q5ryJDGZSM9p0peYg16jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هشتم لالیگا؛
شماتیک ترکیب رئال مادرید برای دیدار مقابل ویارئال؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/31332" target="_blank">📅 21:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31331">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/31331" target="_blank">📅 21:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31330">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1NLVIGL0J-uF8h3n6NoH6zH6fIAPfy26PvKz_cXxSBzplw5eOkBKn9qtThbJ-6r-ia5-JL7fe66mJNFWOX_0kboauM2kgjMa4uM0H80ahsmpROhd4EmlScJ9cfnDmkj1ONptNPdcWDMsAUrP8Iv45Bk8NycmkH4pck2LD_SCsBwvWzAAQ5HE5QSqQrD61gFBfz-UruY3th318g7RujX_zQuz8yF7nU_7g7mcm8D3tRx-nhTVCrN64M0JJGqqCpfFk0mqSQIB1WDGjjI6mYsO3q-InPxT-sak4fck8DCPXnI9K0Mf-m67wYUlr9Edq2kAUOKW6NkoON-pvbNJBntwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
فدراسیون‌فوتبال‌پرتغال موقتا کریس رونالدو رو بابت ترک اردوی تیم ملی این کشور محروم کرده. گفتنی‌ست که کریس رونالدو بین یک الی شش ماه از همراهی تیم ملی فوتبال پرتغال محروم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/31330" target="_blank">📅 20:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31328">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QQWz_k9qEn9tZzLogDoiYmu0eWzwBrK7-aXA1stt9RQoqqq-363S6Xvhg_bhcWnFX2KGXQJl9s55Fy1iqZ02RQwkpQdzAfjTzzCQX_aC9ez3DiAJoFeTueN6IixK2vMyN1XfoUBevORe4raeiaV_-CAfBT-fKRO9vwKFq5C6m7YZAX0JZlDAhO5S0V82eGtC6s6ZNGFUTbtj_p-ic2EMw527OWCuT7aAevuF3u711bDqncaDJtlT9Idd-uL4OsNQDikmfnBvxTdPF5cdjy_dVh7SZipkqgG9qWHf_mndVWECRlJFOOouqwnRi6ZsM3Lsud6PWfIijsiOJ-3uUJR1-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Alb00lRfurTh_WojyE6bXMfofZ8Z5AHCVXcjH8KL2Zkacp1GM6H-VJz3GVuUWj_BO4VQkCVMisUIu7-Y54q6QzDnZIt91rpsSpBMqdN7kZ2zUxF4ubH7DmgNNaC8Aa6XxvtlWIIuqkx5-NOhJvnzUNiPlhPhO3wPjXmpwBMufQAMA8UVWdU3xcBc_Yczqz2tVXVTvoAvJs-tKrCca-4yI4LZUY9Gg4iJtqvLgUbZ7A5G71fCAsTZGi1UY94bhESiRLieiYOjKzZT6ybMFVgPKixCvMznTgGcIF86VxDfv9puiWkxna8XsPTBks3jIy0n55ii7Y7Pjwc6YpQ-_dMb6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سیلی دوم در انتظار مهاجم سابق پرسپولیس؛ درنیمه اول دوم بازی امروز با شمس آذر رضا شکاری به این شکل پنالتی خود را بیرون زد تا در پایان بازی پذیرای یک چک آبدار از سوی ساکت الهامی باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/31328" target="_blank">📅 19:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31327">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🟣
درهفته‌ششم‌لیگ‌جزیره؛ آرسنالِ آرتتا با درخشش دکلان رایس و گلزنی برونو گیمارش دو بر یک از سد لیدزیونایتد گذشت و در رتبه دوم جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/31327" target="_blank">📅 19:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31326">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzcv_La8rzp1kk74PMjvrCWXIUu2_PxUqQ1bRPW3HzyQKO2wlDPnsVOar9xh2E4BvvuDofp9otoGBMx4CMB_R7XIJeIQ2Y1WYaNbLZUZlKd65M0fE7Erpa6bcCvSzbgs9gQo23jay9-jmdfpza8IY1VvZqmSqYZuT2upFOwSQXgLwfLoSNKO-2SAJ8NlKO94rfbrAmjCDsvpfJJCwDOoxXglMloOV_11bKDsgOKUfOktwIh4RRLUEMFnw3W5MeOGTHMK4ZV04rIyHDENqxmHRdkbizSRziySwUy5ltLigBsQgvjxdTnG4Or4rhrO6IFbjJs43A6FEMooKbrYmFeHZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلهائر زننده‌سریع‌ترین گل تاریخ بوندسلیگا؛ گل ثانیه ۸ رابین فلهائر به بایرن مونیخ با عبور از رکورد کوین فولاند، تبدیل به سریع‌ترین گل تاریخ مسابقات شد. فلهائر، ثانیه ۸، فولاند ثانیه ۹؛  هر دو گل سریع تاریخ، مقابل بایرن و مانوئل نویر به ثمر رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/31326" target="_blank">📅 19:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31325">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oz2iTteWPAexzV5bepEUM2e8a3FKgl3mQjt5xxiTkqhOy47Wm-cW_55LHH6ArHpJ7Idps3VUIgjyw5p1C7H4TnwhM7IFT45E65sLrgL8IbYhsIa_QK_mwRdkAk5jSIH5MYcn72tDWh8kAv1df0Tbgf6pucK7wnysNcmzFa0KQBZwB4Q71HMjAUpoAtOdCKrSM46_jJAweRcG5tk3G5dFWmFFH-2JHkGZ8XETFIORnF-shB1Ng3BEav4ILtt_QN3bor5bbuVVDRHPp3pc8Gkzt0N3Zpr0SbOEGLRfvAFmm4zGdecWzn0Zv66TPazs7HMRc3-m5sZuYdMJvB5xhH7muw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
خبرنگار و گزارشگر شبکه اسپورت که از فن های شدید بارسلونا هانسی فلیکه و معتقده که فلیک امسال بارسلونا رو قهرمان چمپیونزلیگ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/31325" target="_blank">📅 19:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31324">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSJ9FxsDOXDl2iUgPmJAgpXC3nP-Zc6oiLibAy7Fh99h-_PC3wGp8ZpFdZi-vgGtTtrEunL-Ks8fY81CS74NODv_vqXGvSv0lMfTHmePhkIykMFBP1sva3RW9w6DZJa77p9zvEBLy2rnFg5Om_CKy-hzy6G1DZxkH709iY6RQhKo4WWNjcU4uQB_VtqKHuPfluBfbUqV3zZi-i-9SKJySy0p_-KT6KPEPyCqn2XXHNSEASkf20Vv0RbMJlVj1eyNG-g0jqZ_9QCzvf9dsGUGanANY6A4jAfMO9sRBNPJWRj5vUf292y66zjga_b2mJnXXOkUflUQtPNVAi99Oqsj7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
خبرنگار و گزارشگر شبکه اسپورت که از فن های شدید بارسلونا هانسی فلیکه و معتقده که فلیک امسال بارسلونا رو قهرمان چمپیونزلیگ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/31324" target="_blank">📅 18:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31323">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/31323" target="_blank">📅 18:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31322">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfyJ7j51FAJLJJItlQKxDuh0_wPWTuHdCETN0EugtNlnOrt358FXbUCgnvLmi4df4koqawa9nm1EVQSF6YykaxX0UyfwQsKUze5o4eTLAZIbDW-T54_7ENcnsx5jerP6jN1SfPn_hkWdw5eQcr-wK2PucsqzSw3WDC7ird8ByTTkczWqTJVF2PYRXJFeooLFCt12AkKoQkerFJvSMxgGo-YawxBlsXBZU_bSxvXtS2nksUqTBZujTRbDRPz37M_UcXn6yaHPOzdTN08Y31q0iRBVNYG53iSoFS1pThAAdjgu6vRYnG8aRoxRX6BWLZRUv_EA1-yrSeelQzL-QXaqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اولین گل‌ستاره‌ ازبک سرخ‌ها درفصل جدید؛ گل سوم پرسپولیس به نفت توسط اورونوف دقیقه 85
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/31322" target="_blank">📅 18:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31321">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/31321" target="_blank">📅 18:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31320">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGtGVUZI8BOugdslUYaXN1hkuIfcdikzrUghVx-7aQgWJBUJJjqyvxz5gLbSwVqHRNGTi1hsbGojKcQaAOfZ_hHKAvLpwZxr4lZKP8_Daowx7_uW01LoGJmQ03MEhuj1Af6hDceFecEshwzzSTF2Zc-Wlu5hhL0G4SHEccxGdGsbKKH0SfyjCf65kYj1Cd9-bPV0uMojJFLx-GxNm5CKkkUZlcsl-F3_c0MOcBhsITntdWU5S45CB1lZO5aE9UW_7XIKvXh_5cnH7L8hpFfoSD6s6D-Zo_eyWgWvOznx9FDpeQUkcGUnB-iAVJRR34zioatsr_upx0xUMqjnEY9dHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال:
به‌مامانم‌گفتم تو هرمحله‌ای که دوست داره براش‌خونه‌میخرم و اینکارو انجام دادم، قبلا تو خونمون آشپزخانه و اتاق خواب یه جا بودن و زندگی سختی داشتیم، ولی الان خیلی خوشحالم که برادرم اون زندگی‌مرفهی روداره که من آرزوشو داشتم.
تو زندگیم یه ملکه دارم و اونم مادرمه
.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/31320" target="_blank">📅 18:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31319">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/31319" target="_blank">📅 18:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31318">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/31318" target="_blank">📅 17:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31317">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/He2EK6W_eYLfXR_dGAyUxg4U6dq_bHaYQHHry7kTm-HUnIXThX01WcO9ltu33TXiBEhWtw0cl3qqOjsecAsHKjgDvMpP_5fKq_GIMlOEwQ1go6aAs-E-tuzhInf-1gHssuNCOCRI9fJxsBdPvke342gydzV6YIC_j27c403TVSiY9JQInYDq7m4rEmiikxt17x3w-jnpL6xotJNKHH7fRtXxxN_vgtz26HcdOuprq5fQVK8U-ZMOO6a6NosRw2J-taIiI_Yrd8qxBsPuWAuPadM9QJaGAtnLIdqEjkRzxu78rYb_U5FpnrV9qiSxgSRzS4oU6v5QeDjWEeVsmiMwSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ همانطور که‌چندهفته پیش اعلام کردیم که جدایی دنیل‌گرا و باکیچ ازپرسپولیس در نیم فصل قطعی شده؛ مهدی تارتار نام این دو بازیکن خارجی رو از لیست سرخ‌ها برای دیدارفردا باصنعت‌نفت خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/31317" target="_blank">📅 17:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31316">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmTzqMpsXCrvWiLUnwAKQEC64Htt_EFwXEL8RpuvoY2RI9iKzMhU5hE-woHSVC3XdQEl52wqjWhTDvKz0yEgRiWnUKlc__DZH1pXMOEd0BJfoZrTkCfWgwQaVoc5Ch_JSpImkGiwd8DyiOJzCs27HX6kJwgJTGUf23o7mS4aU_rOoeNFwTLL18qJRznN5qA-1NwRfrh_0AIpiTZ8PoFlEzLO5mUuf1MiE7yx8kGjcYDtP7dUzrC54Q1KGQHpgnFeGBbhJ3o4XRPipj1hzaRGG1LoqN37EUG-3zmkx_1KroBpuLZSow76uZ98kBXOXKDHDMOicCdQYfkR1azzpIHU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
دبل نیمار دربازی‌بامدادامروز سانتوس در لیگ برزیل؛ جفت گل‌های نیمار از روی نقطه پنالتی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/31316" target="_blank">📅 17:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31315">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛از تقابل شیاطین‌سرخ برابر تاتنهام تا مسابقات رئال مادرید و بارسلونا در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/31315" target="_blank">📅 17:08 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31314">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmmNMIgVSxGIMd2VnqBCPD55xh73a5LMkYcaahGZjiAfHoHTHfrA-q0WTlsDMkDwRe56xaGfRfKSvZAwCmJa4NlzwWxI09L1yGcHsgEdWe1ggHc3pA304TfqJfCqNvWIP8DXQdXOqzu4osNHDpqGLPIkgA1hV_1Na_NOGf9lo_TbMA4XQY8Cp3tVYPKA-34IU1lwUb72ic9rCQcSVOtd2SMGT-mdCmzw8BGOMLmjhN0orQGQGgDF4M7YpPN128f2skkFAjWJPDrGNsYkKvL4S9vPL-dyc_ZBP0xb56lD0yvoUOmpdlSvMV-UNj7ISzIZhlKAHMAaxkGF7DxRltIyLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو: به هوادارانم قول میدم در آینده چند بازی مهم یا یک بازی خداحافظی با پیراهن تیم ملی فوتبال پرتغال انجام خواهم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/31314" target="_blank">📅 15:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31313">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRdq-Zj8eAkqrfcgV206J8Lo_c4YTFiBmGuddQsTBDdbfND1trCiLPr-hV14H9nmXwnt1LLs_ADSP9Z6rfuSZeTMJazUmAN3glwObkbsI7r8DjoYlKh0B9O2Kh1MLtEjhGdw_xYtYgn0jtEcoPaE5aonMDOwuUDL9maYW9M3aY_Kwm0eWsLUhEK1HxBVMZprNYtiJMx3970eH8lliAKRojEmGM7Xf0S9072_Cc2A5ivDtY5ZgqWpNgg4FDNDGJOF9Gok-nfsVfQs0SM3pTYDgwEudNuFQSkUvNaqlUacr40GwcAkDNNAoAdT81K7OnKXRwvAhBMvMhU8ucS6nVZoSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باگلزنی دربازی امشب با ملوان؛ علیپور با گلزنی در بازی ملوان به رکورد تاریخی علی پروین رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/31313" target="_blank">📅 15:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31312">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cldavU2EBl8EFmp7ZP3vUu0kvZsIAodDP9ZARTpJGLPxzz-FmX00P_5jtctr7cK5bqiSwK-yrniO6onKd8kA7ySj4v7A1CxLKeO8n6Gk-DsZHyyyjJKC5F1V_DQ0hu4A_qhrCzQv44DwIUxfSvY5mB0EfYLEQ5vsQbNn2LDHM4M2pGeZF6fNRTlKiuYTjFPwoTN69-i1C3nZPCjixW80RVTCKdb4IV7T1rD-v1ErFcV7KR9CoFUK2bRTGCOfsLVJw6jPVVHb9IiMTpbiGM2BRkvFiagddaJQcw25ADyfVCGsWBJjSiI6cUcWfteArfzv1hqgdKSdTfxiY8xQJ_DqfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه‌های پرشیانا؛ علیرضا بیرانوند ساعتی‌دیگر باحضور درسازمان لیگ قراردادش رو با باشگاه تراکتور فسخ خواهد کرد و راهی سربازی خواهد شد. او از اول آبان سربازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/31312" target="_blank">📅 15:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31311">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IY-92YCHK81HXWDZg2LDs33-trlHwW-hEHNGoJRzjXR1dDTgfH6cu5EIbUoCCVauLqAbw2teLl1tHLTSC5qJFripwDBw1f6axvJhVWqTZCdkB9R7oVORqurGh19KU89Xxmrde9RgzUHxF0qQpnaxnLCTnXMsnDndvhQtS4PmOEWSw4l_hGGsItKiCZH_CDSwUj0Xq3O6sM4z1s0IJBIOFwYLcgqxquIE-mklhDbwjShzyUvvk_iX-r8ftSwWoLsb6w8JwG5FO5dmL7QuZes_8ou3o8kx_a5jBUCP77Y3I4jDZWr5HT9VvaVRIaNSYI8qB_Tupp-_A64IS2gTrJGkfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام‌باشگاه چلسی؛
کول پالمر فوق ستاره انگلیسی آبی‌ها قراردادش روتاسال 2034 با این تیم تمدید کرد. یکی از دلایلی که پالمر در چلسی موندنی شد علاقه شدید دوست دخترش به چلسیه. پالمر از منچستریونایتد نیز آفر رسمی دریافت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/31311" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31310">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAgEy4syLZAFjEGiaTmyFJsLtuwmYW_IftXE7adEHA5_MkphsnuEBTZHzRo44XhGguQpjpime8UUvmW1J-15Vtli6cBbCPZnmLMQIL1PSGvI34E6g0lXqGT0Gv9HP7k1Uf9ptOTS9sYQYKwZ1yTDD61AHbFi_qY-j6viU9XpS3009cGMb8PS1bONlfdQsANTTihXtJ2SXMP0PKHllaaxwqukObtw55ofkCDpn47kKb2DE23VSZmg_5EBrPeX1_MIv0VSgzsh-IM07rMBgar4Nd3dnh50vCZzem8Yg-ta_ZMk5dUI_r0-O8Fw4dxdi2ByVbKBE57CtdxshQ6x2wJqDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیگ سرمربیان تیم‌های لیگ برتر در فصل بیست و ششم؛ محمد نوری دومین اخراجی فصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/31310" target="_blank">📅 14:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31309">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYacp2TAz-TYzzP6-AwYiTE1xpQUK6fChc-eMRx5OhoENvZxLP0v1dyHxCzF1OfImbdwfqUlslmurluFqr_7TG7altAHV91-i0nHMS5zesp1xdfsfEi_AM45L3NHzGiLhQO9VnVoAapTJdfxyA_dODxwYshxm9uf9_XhEqj7tEApKbf6X_hsY1eclInmFvG6PV0tKVZ9wv9yUjj4hFkhH1Qc37HRYVBr3oxy0lk-ej-8IF3LFh52KHrzSD6hKRAL7GxToRSRknLIB00YLu_1KPQmzDRMSIA1GCdu2uASix6DgVnE2kbYKeLwq9CpcjmiRIRkd8b6ing33_eE4LIZUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
گل‌ پلی‌استیشنی‌وتماشایی پاری‌سن ژرمن در بازی شب گذشته روی همکاری دیدنی عثمان دمبله و فران تورس دو بازیکن دیپورتی و سابق بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/31309" target="_blank">📅 14:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31308">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrqTIK82KexzZO0Jco4EO7VPZvd0ItB_P1aPwpVApEslQt_IiesfgzrhhC4hh9pzCpAl_eE-JX88MrWtg6ze4g93u6j8Lwy1N_bunP_pJs1UCygrvSvLC2ofnIDji9c_HKHscdkfFxCjeu52T4zY1eE_HqNWp601uPdACyzV-jWOVqQDWfO8KMGJDnBkvjaRDdz5bDnvy4A8vhs4ooV8cw_GzXyXzjavcsGptHzcNilE7xGMVN0OiH2bX2o4-49lZXJy1Xhkti3o9Z5NOynHB9Ejxbkut4o8EUJ-2JqBm6lVF2iom-6p_YZIEXSkoY1bV6SYtguhf5m2G-M7KUI1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ یاسر آسانی ستاره آلبانیایی‌استقلال دیدار روزدوشنبه مقابل تیم الغرافه قطر رو از دست داد. این بازیکن ممکن‌ست با کاروان این تیم به قطر برود اما قطعا بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/31308" target="_blank">📅 14:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31307">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXKQar7oBw-rbYwwUznOkuYkjdRZ4MyV_1DEh9Pm4_xIu1nouk-CdU6QbFHy5ylgQ1KdbSlxpEsHLMnrtGKmYh3vA9bAJCT_dVXtl5xbHiNcqXqKYwVNLhG-LSWODp2pYpr4iVtNRRxGSS8WKqHRAnHVjZ2o4XS7K2e1WLpxbLBEwB2nQ3-5lXB6dvmA88q6q8h6itRjEUcKaTipdmtL-FzLjeSDGafQg5pgNwO1tIeeIuSffTJQqyGCFsCesBvVgCM1RTAXygeKg9iZmPLTaEuYkHcmkhIivTyCTTxjGkAMhsWpavid_sPY6BvPZFkyEXMQOldGYHfq-DgbIE0_8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تاج رئیس فدراسیون فوتبال: هیات رئیسه مخالف دادن جام‌قهرمانی به باشگاه استقلال بود ولی این مورد مجددا در حال بررسیه. اگه بخوایم‌جام هم اهدا کنیم توی مراسم برترین‌های فصل اعلام میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31307" target="_blank">📅 13:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31305">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NEQbDSOGoRpNukuFxd8roMHJmSqCLfouX-fzjhIBExp_sY8XhcyS7A4aQth7xhNGQMg5d0LJbLKW4PAs4XvPCgIwWZxHL8exB99VpND8bV8cJlJr_MarIszUyHVnDJXhdt9FeSWZ8DKp7fsHAOb5ns3Nj9Ub9kO-VwaNXV97Nsf7yNFawuxYGHsXR9rZqrKxkxHmAaujcN7z8txWlXCsGsYoazHlhQFUyQW16UCjtZkUsh-TeSzY4GAeegRXOA44qBJAS9X-YkMVw4ubsUtSbRJDV9wCQQWQ76qmW4igSXp3no4Aq9zNOiN9Ir4F8GIAkkNhtUVewiJX-zYWdlma0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jxh5zCUnPNmeNUs3FIiRFounIBNmjiIDsWV8kIWP4cbOBwoxFO-Cj4WsiiYvkJUciuTzuIA96tlLiQySeXrLz6X4UPpeYOLlybc6tKLHj7rpD2ltO36u4lJHzn5Bfw6GJE-uq_uSb5jo7g8EuFFamrQfOEzopS0VcnzyVcpqYEwKIA83RAtQ_oVLn_217ZjIzJVj0TDD847nFRgfj6RNsBo2kvAZROlma3jfrD1svVXhipGB7NAmCB87d1b5yCXWxXqhsKXvCpmj1LmPxsaS29ZPJbejtNbHoaRvRUcK6UQIo6JEXilNcuRxuO11wpjo0tazt7sEmKw3SdjWqYNsOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛از تقابل شیاطین‌سرخ برابر تاتنهام تا مسابقات رئال مادرید و بارسلونا در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/31305" target="_blank">📅 12:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31304">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4eXTAFVWS30YvXPEjOcsJ7P7gygmKqX07Vrx88zy9y8795reVUfoMftLsTUCBtQ2NFcl0FtQEFh44L7NEu_KBskL29QlL1W8QO9SgJxuW6P2xBIcvBYxZUoLkvwft4p2cRmeP7yQFiFr0PYE8JAqcf8BQikPoFRuNKTida89z-VHB-Zv6KF0LShNfL4c1I-N4MmZL_Waui5VpBxqKF_1GZKgwYYmfCrzrliDGZ-X0QB08y4NoFa7PmtxenaaEWCV2Vdb2C_s4NadaPGG_SZxSGB0wMqCaGCgOlr-V6IQoE-eg_7GPAKUjAxOOTLyevCbqkJB6SIRLHO6wKKNuYEAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گلشیفته فراهانی با جان سینا فیلم بازی کردهه؛ چه لبیم گرفت ازش. الان دارم میفهمم چرا حکومت داره تلاش میکنه گلشیفته رو به ایران برگردونده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/31304" target="_blank">📅 12:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31303">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otbWwKiqWV6k6lVM7jRO2-fUmVLRVl5FCBL5PShOw5ZecsWrogNhHjQbT5rOATVypxXSt6wm2IpCpCbJ0k2xKgPGxswA-hgoWSwlACaz4N1CTiZdr-1-w3mSA_OwhrdbJVJ-9HaWiJyizVqoMcJiCNptjMv8xdsdG2FQ0w4zSJMSXSRZX1EL08AOI0DN3DF_iDdpCIe0ISp1D9BNwlW4sxRJS78V530BpKKUC_jCn374vfMhKsPDTTVosIb-MRxWwE2wpLkmCz9W3lQ7WmQ8X2Zd3smjJ4wY5nJF9gjfqOFG-LlpxW9Xrk9qGooHokHCYp6XItpGa5pE8Znr65VdOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
گزارشگربازی‌دیشب‌النصرلحظه گلزنی کریس رونالدو: دردوبلات‌بخوره توفرق سر سرمربی پرتغال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31303" target="_blank">📅 12:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31302">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlIpIIOHCEjeFKADoEOWuhDCFvWoNjInhU8Wc2QEdO_7J3mxEtBm4uQ2Zf5chObLcPVvl2bKnxyk7qKFG8nxouEV-61sJsR9JU2geBHwQsmkZnBuMUwnrZ_C_-m0y9rCMjYHgHNs0VDnEhiZdZikR42qTr9cOZNMSN_GKfQWP5Y9PBjTCGRPnilQeDMxr_niBAr5rN56r5xLmCbf_IOINLaubXAttTX9awMeFcBu5oIRj00EkjqWqURcH3awpHLQ0MGtgFmnbTgdLq3BUuOgVQ8N1KTN_rVFCgX1IxviXgOGTdU6sqMqTlCaJ02f7D0ns6naFdfK4CWjQgnjOl92Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگااام! مگه میشه؟! صدا و سیما: مرغداری ها برای افزایش وزن‌مرغ‌ها توی‌غذاشون تریاک میریزن، برای همینه اکثر مردم بعد مصرف مرغ بی حال میشن!  نمیدونم چرا حس میکنم هرروز از این چیزا میگن که مثلا مردم از گرونی مواد غذایی غر نزنند
🥸
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/31302" target="_blank">📅 11:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31301">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgzwYzQh0aDCYyR00Z6QTJheb-PqFjJYI8Oy8IM4UQYDyJpQYJhTKa4tC0cyIXcNYXpyyxuXXbGffHW5n0NOYZMLY9-NmdEgNTfK6utBpNYT_JjqxlhDL3JoD7zcx6rrSo44OUOHdMRBRmThjZR0C3F3eOF_bbxy_aWnhqfVD_5grw5WVz7iUkfuLS4WivpPOqQXDsjzX6ZAw7H8MaslLX12syZQNmyOKprvn1e_F37f0DFQ9LoNYTiO7lZCw6bY8sN2UZD6qgSUfrhjyZVosSYzwMJfxhjwIMz81utprFNP7HmwIDjlVYf-cGRXUsEfAyBwcVqbV2p76hEXltXtmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ایکاردی‌بالاخره از وندا جدا شد؛ درخواست واندا نارا برای دریافت 250 هزار یورو نفقه ماهانه رد شد.
‼️
ادعای‌واندا نارا مبنی براینکه اون «شغل خودشو فدای زندگی‌خانوادگیش‌کرده» ردشد.  مشخص شده که دلیل‌افزایش‌شهرت‌واندا نارا ازدواجش با ایکاردی بوده‌که توی‌ایتالیاخیلی معروف بوده. همچنین واندا باید دو سوم هزینه‌های دادگاه رو هم پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31301" target="_blank">📅 10:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31299">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3341162dbb.mp4?token=hervEbgGeWuSQ8ybHf5g8glqsD65j80dsT7NoXi6rFJZuGVHg-Xn6k7HAwhkU4lt5cs_2fUFHVt03V9Vxc3z5qDpVSzVHjA5dw_wo7pZ2xMqH_tic3CsOPAD28qjRFuMGKjjU-V_jJQYB7g62JiKC-jIVSP8H_2cQbAH7myif9FqXk6ETVxxuj01sC0neYEnjlCOEIwJhKfogyVQ0uagMGGDXeLdNydlXi9Bnqk7QpI0DN0oNCiRXpEPIRjez_YU3eomY3gRIa-7TkX47TVn6BTMQGx5dwDcxCzauoW1lNnngoIbvT671Kq9bNTZuCahsvxCxQ_m8Oe1-Bm5RDK6mhcf0zOetz7rusZfXLIbtYAerJHqy-ypQO-TEfREIHWaTkQScrxyihCqMLT1f_EkG7yO6HLK4kpLwXZWqpZ3qYVKTCwtfmrAIzh7CEdoeX7DDk7NzO6ZgBVGbfiwUe1KOiv5eiBw00NO3ck70PtxrjtSESUPb7O8nfe8S4M9wBDBWJF3p4JY6ZPWNAPC3NDZmezrcTtjAYhLV5oR7knRSIenWLiVGJBoNZrT5wm2eKCP10ZNH0ImN9f2tcXK8NJnvfTIPXxTKwqDGVSECaLrJYpteaLDyL9yJhbBmKpkfM0EbcrdyrTQx4HGhJFrGkZMMWQvLHTdFCFLAhP4U8ityYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3341162dbb.mp4?token=hervEbgGeWuSQ8ybHf5g8glqsD65j80dsT7NoXi6rFJZuGVHg-Xn6k7HAwhkU4lt5cs_2fUFHVt03V9Vxc3z5qDpVSzVHjA5dw_wo7pZ2xMqH_tic3CsOPAD28qjRFuMGKjjU-V_jJQYB7g62JiKC-jIVSP8H_2cQbAH7myif9FqXk6ETVxxuj01sC0neYEnjlCOEIwJhKfogyVQ0uagMGGDXeLdNydlXi9Bnqk7QpI0DN0oNCiRXpEPIRjez_YU3eomY3gRIa-7TkX47TVn6BTMQGx5dwDcxCzauoW1lNnngoIbvT671Kq9bNTZuCahsvxCxQ_m8Oe1-Bm5RDK6mhcf0zOetz7rusZfXLIbtYAerJHqy-ypQO-TEfREIHWaTkQScrxyihCqMLT1f_EkG7yO6HLK4kpLwXZWqpZ3qYVKTCwtfmrAIzh7CEdoeX7DDk7NzO6ZgBVGbfiwUe1KOiv5eiBw00NO3ck70PtxrjtSESUPb7O8nfe8S4M9wBDBWJF3p4JY6ZPWNAPC3NDZmezrcTtjAYhLV5oR7knRSIenWLiVGJBoNZrT5wm2eKCP10ZNH0ImN9f2tcXK8NJnvfTIPXxTKwqDGVSECaLrJYpteaLDyL9yJhbBmKpkfM0EbcrdyrTQx4HGhJFrGkZMMWQvLHTdFCFLAhP4U8ityYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
تفکیک 980 گل کریس رونالدو در کل دوران حرفه‌ای این بازیکن؛ CR7 تنها 20 گل نیاز داره تا به رکورد فوق العاده و تاریخی 1000 گل زده برسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31299" target="_blank">📅 10:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31298">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3l2a8N3rZmtaE3E6jmR-B1gfy_56lg0Dxe5gz1pUtnc3VGYm7MsMXGdxAL9P247q2bB9mZOD44MvAmaB11D6hOGxtvdsNSLWOI5I8SjJrHIPkTapONNfofhkoXDTeit3-tpX216JTnHmqKFntzvI2Qm6xHUpvcdfr-inrhs6xNDO7ZWw2X8S2FPZSh0hbUoA-VjQTEhGfZSdCgRuztTVLwr4w6zcahBVd_5z1-7QcSdrkloVVLDdI5I1W3sf69O7_cJMVWYWih11DLA0g27DUvWDJi-uj201p3vA_OBi-kEuZQ6b7Mf5uHsbGi7US-tLAvXw3nx34CWCf6vFevXnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جدایی محمد نوری از نفت آبادان؛ با اعلام باشگاه صنعت‌ نفت آبادان، محمد نوری پس از شکست مقابل تیم پرسپولیس از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31298" target="_blank">📅 10:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31297">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiAY-TlHrtfwSG1JqT_KtQN7QeE4-jgELUmZRiI-Z7pIXY_VB2eph4Chhd9hkfQ-us7pzuD76E1U6WQm_96AvzqBQkYVEFqN-XsjyH6eEM_1rs4nln7USVsqwifG3z0nlgDynw92XDSoTVSLQ22xBXBn85WDL2l4x9RdaYfe7MtBsQ155R-EbMWKxRTYAMaN6FusPAx37wY1OXcuouPXuDkigDgg99XN5Kd0-8iQ4DzexFx-3bCnYUOIVTc-BehAiGNHTOmJyedNo_LOHBN3iGVrkn3gOWi8VrO8uJKMKxYqQlt6tufrVoVUqf_YfcOVrKOqBYvtooU9vx9H_uOiAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان‌نظام‌وظیفه‌به‌علیرضابیرانونداعلام کرده تا زمان مشخص‌شدن‌وضعیت کمیسیون پزشکی‌اش حق خروج از کشورو ندارد. از طرفیم نکونام به مدیریت باشگاه نامه زده و گفته بیرو رو دیگه نمیخوام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31297" target="_blank">📅 09:41 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31295">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoxdOkLbXPfmI4lpQC5SRPaCdzKRHbfH14jiP7mltyNhs2kaPASMqcZ5hsuggJ3sKHKdABohkQ9Pjn1FL7ilYLOm86C_dmkHiqkRCmSG3pqmNfM-H3zbEcuQErfTH2xO_4c6eOYJIqH98q9wFKrAhYZ8QOicmg4zBMofnhBNxX2EFPBemfw-KFlxXYnW54cnmaCGDcq6UCosHqGzfIWyYvt5CqY9V4BC_OClwv2BAB-l1s1Y1D6oRXAshGRUadUZx68liqCTBu07i4Nf8gv0M_ufOvFnDbYVd8OB_igbTbwvfhIi1bXY9Xslgph7XV6-E1UXAPsCP0tIEUBbcamTfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛از تقابل شیاطین‌سرخ برابر تاتنهام تا مسابقات رئال مادرید و بارسلونا در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31295" target="_blank">📅 01:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31294">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIPBlei-u6hrqq3WtBqO4tqJFxNp2gRxvtlqZnFb1eV4IcI53PZjZH9ZCjtFeGmtDFxnMOjpURw9sdk2pXvRalgCT9fALf-jjRKtuAvFtZWXN78FC8Hveg2dyTgZQCO8Ze0t3Z--uk9k-qIzYHkvfHj0OSHaEwpoNJkg84f8bA64oKYYHfOYprDzcdEUV6D_Ov7sOJ2gGtGJ0dWkzzXLOJnS-mgJnq9PPM-prgfzP9nqeIY9keUzlE8MtUJYraMjEjGigTThlOfBsfNVvt1vh-ip_1jcR1CjNduDP7BtgYnEj2jv5LIIr9NVNHW3N_2Ds08O0VNPjj0CUdoUschLtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
نزدیک‌شدن پرسپولیسی‌ها به‌صدرجدول‌لیگ و برد النصر در شب گلزنی رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31294" target="_blank">📅 01:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31293">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plvsTCgBtjWd5Lqml1Dlbm4OgWQp6lPCQ_M7cr92n7EtGmlBmtQlA-FrRcpHYQmmcJCYX5zzVdztTLmV7aPElQ7Pv5fGPnuBOfZS1vZOduM83gTsloRAFf9v_aKHywa7JDxUd5Dk-UFleMxGNaJVuuRwxTGEDcrwLqSuxtOC-do6Xzkwn0F3IFXJtaHbYclD00RkQmbVkr3Eny2UQfgiSYSJIdQ-_LAIqtFQVLMIUq72TibDdvIQ_fYHg8QzewhsSrXL-8x2hwEYhdmuJhIiaLMZFlSAxEc9X4fRj4ZCNEAgk6lJDqyDAdJB8DtrxvK0tcefx1IMHjqCSLgItLt_Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛برنامه بازیای معوقه هفته هفتم رقابت های لیگ که روز سه شنبه و چهارشنبه برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31293" target="_blank">📅 01:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31292">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKG5jwF2QgXb_W25LFGO2Yn1U59cvhx6obqwNZLVOyC29-kvubLHkXlITiCSG6XeGZUxzpCpwCwyPhytR3Ph-_asNJrR5lD0GdDwYmM1XMKNUGe7qmdWFGa0UTpLOVZLjsbI50VYZuKuUkYNNfIN1wMKJx4gwrgAUyk10bk-S49x-PjTRf6PlfBxpJx9zpB5EnEbFNO97a1cx-9DfwbjS9pmYbt6khi_m4M9NwWtX74Uef6aLs3mG_rWrOMAFQPk6Lpn8C7n9lsL7CG2mXGrnOPfnRqbyjFZCJBEErYc2XbPxmIlsIocbWmv2nVjHJBz0x0MKa6CzaTzM2DALXAOfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ نبرد شاگردان تارتار با صنعت نفت و دیدار زنبورهای وستفالن مقابل وردربرمن برای حفظ صدرنشینی در بوندسلیگا   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31292" target="_blank">📅 01:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31290">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpCQla9VNcFXaU3Xc2zPF_McSGbsHAFluuafWJDmYGzfBdWXvo5fiqcBvxCocIzLhA3dPk7CMDH2X9j8wnTt-IpWWqJ7mIVSuRjb_nNVxTX7Y0NfzEFcF0ymtiS3fiz5Lf-xKCSrV2pBJH-CPHQOhY_L3poQy-KpYxAl21Gxk-aHlt5bmb7ri3kbT5OqHTfNoVuVLH4vxP4e0K7pkuPyrCVQQKhX2VHAcLISny86SKxbypBG29V9cp7rfX_lyXBig8HKa679S3bnpy5DIVBp6nmH2c4exA-txm990Luj7hE1dW2qww5U3ym14G_Ds50r5QwNJlQDy2uJWGPf4ITPVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
گلزنی کریس رونالدو دربازی‌امشب النصر با الدرعیه؛ این 980 امین گل کل دوران حرفه‌ای CR7 بود. همچنین رونالدو به اولین بازیکن‌تاریخ‌تبدیل شد که مقابل 160 باشگاه مختلف موفق به گلزنی شده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31290" target="_blank">📅 00:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31289">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQ9rsLQu6Qqh8CG8Htvytu3o2-GZp-SdjT0N2O7glLh6OzbYWFiEHRVT5rA-g331vdbWvZz6-3WUKxpw51dhE8zfFhYQ_dnAkZVJX6D0zOvP8Op6eIzPnWhMErbsfRaTeq56YolLsgvKROIZovdG1PDvw80wxUFNwsKbW6MQbMwarP0JnsKa7E97f40bVWTYgsPe091JRYttqYK71pGVLf9i2zYq2yGeD1H49k9LP37sFNz8ewdKabPr_MrVsp5q7OXDjf4FcCqSbkLDYIO3uLzmv7MRlo2YC0DQGrT4rBDvHJwV0Ml09p7gpbTO2UxJS7Mm3eUmsABg2Nyjz1g_0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دختر خانوم پا اسکولز اسطوره باشگاه منچستر یونایتد: جود بلینگهام بازیکن مورد علاقه منه. بنظر من او در حال حاضر بهتریت بازیکن فوتبال جهانه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31289" target="_blank">📅 00:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31288">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2RYzfCue-XhHj7b9FW8Sx78ZIS8MsmGXuLJW3eByqs13sxyJjWM9-2FEwUAmis3iishSytzszbo-ZFml_fdlvXjwz9PzAuIaJ1PgjZfroyNqOPuxZpucXP_JPXg6h3ceikfmRRKenk73mceJFpp6cginQtUn6hNlRkJpaFc5rrKmH9XA7UI41YCWSxF-CxSDEa3O9DyYnjy6X-JlVBFv_Pm1SWl47WnzCb3lox21csJKn70V0OsbPQlIJbnzKZLywON9Oj0Jepo8scfTU2zGvNkonDAWnZeBAZDAMQ25kpiZg_CfWX9sIjdPdk6myMEjLesn8MK0VkP48BqSMnQkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان هفته هشتم؛ البته بازی‌شمس‌آذر با پیکان و بازی‌های معوقه هفته هفتم بازی مونده تا جدول رقابت‌ها تکمیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31288" target="_blank">📅 00:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31287">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‼️
سازمان‌نظام‌وظیفه‌به‌علیرضابیرانونداعلام کرده تا زمان مشخص‌شدن‌وضعیت کمیسیون پزشکی‌اش حق خروج از کشورو ندارد. از طرفیم نکونام به مدیریت باشگاه نامه زده و گفته بیرو رو دیگه نمیخوام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/31287" target="_blank">📅 00:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31286">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sH017DXcZDVqnciDzZvBEZ5voP7mJ0C9-sJYJM0vCZ4yA2zQ7txfzFSd-0X7LUFDmUhyVgEFpFKLhlHnfU6u20GDYvZCqF6qXmBPUOHkLfvD_7GraSOyUKp1EkVRZZTgoYwtcwYQ6LPOU_hLOkms4og95JYpt0VH37gYM8VXJ0Rx5AnL3ufIKzVpcoPbKiXB6cvimi5hYuyYEzr23OVMvaX39fowen1L2y6hNCdkipwlLgYAmW-Vp0qeo3cVBJAyU1esnJ_poVk1JBlovJnpxiTLNg4Rc3l3FF7PZq0ypucCn3rt9_RJx-i_9FYFTmqIzR6DTXRsifiJ4t5aMpdKEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تایید شد؛ علی رضا بیرانوند از هتل و اردوی باشگاه تراکتور تبریز اخراج شد و با صلاح دید جواد نکونام برای همیشه از این تیم کنار گذاشته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/31286" target="_blank">📅 23:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31285">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZkIWtEqHtjsA9j3davevRl98n3e63fsJ_5N0baFkFig0jwcFkC5V3vqyJSuNNgekxV02CGvTvBDreArXKCiVGuYvrIzw9FCk-jYWXThMd7WrWUz8InUFlOJ3Kvt6PALHJN-8XAojiVpCKizQXPHNdAtCaStvglXGY-zAdCBvh_GE9zb9G5rlTiXEqsyl8GIH984kd8okzzjeZxm3qTbhDYwkVlB_t_aIzFlTB8rsrskSDkswqCodmldMW5Uymo_NQoOQ_OrepfSc_F4AGLiKxayXI_Spmj3vyGQmVfBZ-sk6YGbqIWR8a4Dzh8l9cr8mZsdHPamw8druy2yUrubCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جوانگرایی‌بسبک‌تارتار؛ حضور پویا اسمی بازیکن 16 ساله به جای ابرقویی نژاد در ترکیب پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/31285" target="_blank">📅 23:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31284">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SokGxhSvzyVQbQ2lwgzmpVWeTTD6vJk_-_OJSFwrq5JvrEqEJ_mqEo1Tdo1MBAMYW29z3w-qXFJzz2oTIbM5B07iTEt3v8J9wkLoiumNfrFtpLdOw3jeZz4J0CJconDmy3CKaRxPeYJ4ylNbuLENXqutu9EsaZAZyDOmOuRTX9-LbSUER9GFqCf2MZsoXAYwDEuS0zMK-lsqXXqXEzkw2e3UnifGVLPqugpQsECWTm_xA9ZwA737fUCqVdJNdrDJoVTl05XlMxS6zc9_qWUpK3KbkDHSupSr3mW3gsQhGA9_vtB_kbYP0XZCyk62xqceA-kZCLRhgxzKaxayn7WiOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تاج رئیس فدراسیون فوتبال: هیات رئیسه مخالف دادن جام‌قهرمانی به باشگاه استقلال بود ولی این مورد مجددا در حال بررسیه. اگه بخوایم‌جام هم اهدا کنیم توی مراسم برترین‌های فصل اعلام میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/31284" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31282">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZKQHTBjiZH23hsbovGxb1b_4xV-9LhCiQPVWFXJK5P9_HdWeS8HGRdKPaeiy-T6wPZGpD82FkNlgiKbr285wXSFL8V9FNunDq88R7EioJju1ddsV-_mNuFKIEJd3PjHYsIpioKkOFEhtNJLXxNqJHX-mYGyqAvAct83NDPfEDIJJk76Mo4w9jQmJCcu9OhlKPKqq1643IVb5pgjK897PYqQqZlPfmVFDYNFCvmr8DuVgYmIENSCAQSotX7wrLlyg0kwXeAXWWkZg7QGsP9NDsUwS_f9JZCRQmbs4ADiKorszsEcpVb2yjHVpGPVb8xPhGdP9o9_U4SKihDHzI6lXsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fvgdfb2LJv69F1AeOXkBtmcFBpGtXRJYvTfgeJZ8tBwAe_x_jPX0kVtTlfTdjT4mCH7ItHenk8Cq8IPbsGryw4_jAZp9l_XPTXOOO5XMIO9DgA4BQt6kqOSot_pbNfnT7PjUbzBfDbr8ThVsljZbAIcjAnIp1grSGqqnQATjG695gGPok1YO4YrBXclY3s4Gkuv6ltn9nVSdjGzpoaKbfE2DbGkoVY574MsdtZPSQmWYFo_A9ZrOSAw9Q9GyLcEF6M-xJg46g6j3rL9DRNt0ruFMafkEezU0z4lZuDfQPKK-yl5--0rhpCDq9hHl6NEJiG8GzKNjqIuHrjFLuPg08w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
قدمت باشگاه‌های فوتبال ایران از ابتدا تا کنون؛ آبی پوشان پایتخت قدیمی ترین باشگاه ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/31282" target="_blank">📅 22:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31281">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTzLs8wuqnXslBEq2tONvQ5I0qMkD3vQyJYySyOitv7DcUpJi7IsnkMhPhYtqdGs9SmUFJ3A_742zbTNYxEcTkgTLaYGwXZW5qyYMMdZ28GnMrkwQssvbjdz9MG4vkNIrWcZztUizKJFp8xCJo3g0O9w2aRlfcTQSmeh8UYbB0WmxYGqjYb928Gb-wMy2qbzvp82R1vZQ-ThXDb-KuK4GGTIAidnLf0hcUSz3gMj8jY-AX1xI7so1LtmhVN9mOyeMXoaiFfLPXuLOuxUgzt_zvtxelQA3Cs3FcvHJ4fUAH210M4YrBCbYEmXvIaDgoUM74bs9DFyoCkiW9FCEpoGmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/31281" target="_blank">📅 22:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31280">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejRBAqdqLfxkW4frfNsdIVFaTe3H0LAFErMZDbEL-Y7qQ7IE0qGENm9Zk0ormoThSS-Bu7zLjadH4S3F8tbm-DXz0b4qrVQbARlW2GNaHbXEBemqfhhRl5qlFIdR-1PMV4g74m2BqIIjiITTKhQFCRFCQ8sppUZP9dEtmBncK-5yVdqg-WoDyoOdLz1iffF8yTLIYBKc_EPk2hsdnk_YSWCfXc--bvlAz3ecOJlh_j3tqDkAamo0uJ8TfQzwEa8uqHVXBA9b4ccnrXs9pDKTRs5Yc-JRxMc5_BnC5fZBpzQTuaAH6TZnGlDMbNRWm65aroUS_2KOik0I3DosOJqkfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دستور واتساپی‌شجاع‌خلیل‌زاده کاپیتان تراکتور به‌بازیکنان‌تیم‌تراکتور:همتون علیرضا بیرانوند رو آنفالو کنید. او دیگر جایگاهی در تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/31280" target="_blank">📅 22:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31279">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🟡
👤
#فکت؛ کریستیانو رونالدو در طول کریرش مقابل 159 باشگاه مختلف‌گلزنی کرده است. اگر فردا مقابل باشگاه‌الدرعیه گلزنی کنه اولین بازیکنی خواهد بود که مقابل 160 باشگاه مختلف گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/31279" target="_blank">📅 22:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31278">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ فکر کنم تنها کانالی بودیم که بارها گفتیم که رئیس فدراسیون فوتبال به باشگاه استقلال وعده اهدای جام قهرمانی فصل گذشته لییگ برتر رو داده. حالا هم طبق شنیده‌های رسانه پرشیانا تا اوایل هفته اینده فدراسیون رسما در بیانیه‌ای استقلال رو قهرمان فصل قبل لیگ…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/31278" target="_blank">📅 21:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31277">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTA6Tv5uefE_ne6UNeNIW1807aB9gdxa5IX_zuwQ9VUH3xzhq0BELSsk_1y9P6V52NbhjXkLdgo0OKnTiicHsRJY5lBUc3_LuR7LSRWZaMNOdv1E6ITZhvLCQCFkKf85cYHO5NJ0b9RrPKcOwd8l0XoLe5qTqR8ccxF8F-qNPKYfQSgH6XsrAYHvLM5uXFb09SVmdexeykNeZ7C1J287OCNdrAHjmR8AFINtC1wPW2SHb9lkIxcDyhbVGyiCS46kQjRhKiPrmizUEVNbRjsSMMpJeJkoircmPBpvXvz5b25osticoqPrZZIS8ihDJC4ns8QMLs8IzgeZ_m623R5KVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدمت باشگاه‌های فوتبال ایران از ابتدا تا کنون؛ آبی پوشان پایتخت قدیمی ترین باشگاه ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/31277" target="_blank">📅 21:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31276">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-ZpJ6aEcL-WzsR2FQ2yjXAVz9UeJrVhLCXhtRv8wAyWUU2_i3Ybw9NQjXDFaLzYDvS1gmaqob7VSBKuNTYTHC7JeIVu9YcOlgZ-vMUchsL8abGVQKlw76S_uR0PwhP_e22nCUCUJDaOUCvg6BdPZaha2ZDTObp_3MQbYHxr5pIcojdHApSuRtOkhPJroHddikrq1S7egC1lQ701nvzJY5XfHV2zUmC7j3QrSYCKWdzR7f2YgP0wmFx9CZWGITa_-iSXxCzZBTY7h5WrOQLcKIxUNTbC_cQWsE5jumlMKQCg49JQBvs1t2Z5MdyCDz6gkqlf3Q0OqIw6rEb8d6UoDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام وزیر آموزش و پروش؛ به احتمال زیاد مدارس بزودی و در روزهای آتی تعطیل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/31276" target="_blank">📅 20:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31275">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqAZPHCaFtNDFVIeai0dI1-EoFhYE_PuPfCDHUsFAndQc5XOkC7OeqN6ixgalINd0XJyBrWgczmNRjw6KUDhE9KobiDs5Zs1Uz995fmTbMOhXpJJCPTeOMS_AHnmoySJSYK_R-g2Ha-japeRRjKGPCoskjXwthwqZp65iTvlX-RTuDOaXe4YQ6EY1GNwHCMMnaXaUTAwMREUhTUZ6SGKOKhrVEt3tllDazWOyUUVaSedTv-ypnnKcAJ9IgScvgWytSQgigaLsLlJFaCirZTKuIHo1L9QEyEgwQXoZC_N34tqAn6bgtXldsXWT8Q6d18bJE8mflxXfIP8HGi0aVuE4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ ادعای بن جیکوبز: خطر این سناریوی فاجعه‌‌بار وجود داره که باشگاه بزرگ منچسترسیتی به‌طور کامل از دنیای فوتبال کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/31275" target="_blank">📅 20:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31273">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vEcGxkMOEXqIdPD8tFyZMbiyvn01CyD7Z45MWefJXQ-tp7_qVcoAIVhSWTf7Iv3g_yqQg9LLcSLQopgD59_BdKfmB6OvzrnY14EMTbSeVKUAgwMN9sftLdEk3fdGctOMjErbe1_9B6pWCkEj_k-rjBhkF06Vd9LjXtZk-Wv_rn_vEeOiV3jLzeDAZYiQitvE2ByaL_YisueM34PIGXzhFcEu97XWSnPJSKkV3LvZNFgY4dq2uTcyOm9HwUhNEi2IvApfc3xn3yiUUyycD8h3XUynFqdqp11PTA5HX7qP4sKbGUhyxjgWq7BSse00IHukBtuY61jx6BwUc0smDBdF9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HOmBnsfqT18EOQIhXuVv3FvVaktbjLy2hP80s3W6d8zdm-OYClWYeMnPxNrnTPgwEgoD6fo7KZG9JRaKx2YzTq9C4-No8HAnDLN88JXt6KWpCI0MxoKVNYw3GruDEv8Wihm3EpSoB6oQMcQB7kMRPvlD9RAEQomDe7_caNVxBhI06I4FpjIvfE44JFj6M5gjW9DlXqeEj6ni83ugS9rqzcUVdoWEUuDXUln3o7IMKkc7eyPM8XQnYO76pxBCUAzhCXrYIzisLeujlVeLQ1twI2PwAh1YO9amzc4LlfXPyGJFo74lQAzpB_xMzZk5oAKf-OKaBKTaOczqUwEaLJhoFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
تفکیک‌ گل‌های کریس رونالدو و لیونل مسی در مسابقات ملی؛ رونالدو 146 گل در کل دوران حرفه ای خود با پیراهن پرتغال به ثمر رسانده و مسی 126 گل برای آرژانتین به ثبت رسانده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/31273" target="_blank">📅 20:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31272">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e9e6b867.mp4?token=far6gyjB8SJk2x5g2gqIaQJRsZQhI-iN2VXQOnywEVzJOUgknlmSKBIDOz-cnarjyudzy-dtKO1m5E8doSYsebHQ74Ct1N5BxivTzfOJArVuvDK66AAf99Or_A5gWUpc4yN-WRecoFhXW9bygwu9cnz5SAgPtWBK5OW9UwExNnQiwcLzgHiBPN8e7CPtZpu_phB5vKDh4lg5x1vyYTc-8D4AzKkSZgUyMHc4VrEz_KGtQsnAYE2xhatx9fZlJo0Io5D0CDE0oLkS8IWRMc4ScJIisyTquQCfYkZ03nlxMuA_V32xEBs3rP_eNsx1hGR9D_SjZbNEzE48xORsm2slsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e9e6b867.mp4?token=far6gyjB8SJk2x5g2gqIaQJRsZQhI-iN2VXQOnywEVzJOUgknlmSKBIDOz-cnarjyudzy-dtKO1m5E8doSYsebHQ74Ct1N5BxivTzfOJArVuvDK66AAf99Or_A5gWUpc4yN-WRecoFhXW9bygwu9cnz5SAgPtWBK5OW9UwExNnQiwcLzgHiBPN8e7CPtZpu_phB5vKDh4lg5x1vyYTc-8D4AzKkSZgUyMHc4VrEz_KGtQsnAYE2xhatx9fZlJo0Io5D0CDE0oLkS8IWRMc4ScJIisyTquQCfYkZ03nlxMuA_V32xEBs3rP_eNsx1hGR9D_SjZbNEzE48xORsm2slsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی‌های عجیب و غریب دروازه‌بانان باشگاه‌ها درهفته هشتم رقابت‌ها بعد از اتمام فیفادی مهر ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/31272" target="_blank">📅 20:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31271">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MN9L4XLmydm3hStA4-YS3wtykJkurlVghEvdC2rGL70b3zJSIML0TGqDlVt82RePIQCT9OtYUu9NmQuaR7-4OypuIurhtNaWMmbsXlTayl_ylfbJxWOjX3U_yKmPPBiNEQr67TkkSNZ4huj-gHryRjZWVK0d0k1J9Rm6qqM9J_uMh3XgJ2yvpc-9GC73xvC3gKUKfEP9uphrPFIHcHvgwV5RQllJN8tnXA7T--HNmPXcmCueWF3xPaPBRaygwO350E0l3X-BZBQgtj4WYLEy5WNGY2uF8R6I_A6YHCvVXDW1qccKp4eWZs1uJkPBEvCGcrb0F2rSxouhtvQnTVy4cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی رسانه پرشیانا؛ کادر پزشکی باشگاه‌استقلال به‌سهراب‌بختیاری‌زاده سرمربی آبی‌ها توصیه‌کرده دربازی‌روزدوشنبه استقلال مقابل الغرافه ازآسانی استفاده‌‌نکنه‌ تا مصدومیت امروز او از ناحیه ساق پا کامل برطرف شود. بدین‌ترتیب‌به‌احتمال زیاد آسانی در…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31271" target="_blank">📅 19:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31270">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان هفته هشتم؛ البته بازی‌شمس‌آذر با پیکان و بازی‌های معوقه هفته هفتم بازی مونده تا جدول رقابت‌ها تکمیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31270" target="_blank">📅 19:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31268">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtpyt373sgjJOm3A8xAzfz1HN0I3XKQeasVEmLy566uf2Iv0FL0VUZ7vYohaNzJIuIoRtlG3FnWZ43ST1jloAam9nrTI4xv_6bowc3O9QCTQUx4jqpriOdUMUa2SbN_Ekj8ETd6rs8S3WWF7oiXdH0cEYQXJa3A8vGaEn1gQpV1mjJ6sRrqm-r6T2T2CMMh-A59oDgGrzWxAFBULU1FuV0fQEd2pYf8bqTo2qg20D5f070vY3Q75Vqg75PJn3xkLwaxMNHi4tJec5D-4YX-aihDSTQAfboCLs6n3P3vaWhhF7hwVFXqkCM3qGA11nGIVQbX9qeNpNVSXAyK-TH-PNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ وزیر آموزش و پرورش رسما از تعطیلی احتمالی مدارس به دلیل تهدیدات جنگی خبر داد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/31268" target="_blank">📅 19:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31266">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/byDIVul3zSFNT9RgPcJso7WKT8rZvcAcP6RASOVuJY6CLuZApbOWBdpeFjxhOpOHNGdKRAO2ER55IOZ4wVKrgVQMMKXo447vDkslTbX-Jlvn6vumxQSQEVzb8G9O3bMNevI87b6sLcyva53E5IROG-pFEnD8fz5bMeEOHVtdccGbjcPQ4GAop4D79LXDE--M8mpvCTflpXrC9GwC2Te6F4KMPjplzu-GdZ3WKNCvRjLtdR8kl3m7bbu2WzfQ3nPRtOI8Z3dSCekpHOEcG5fMvkvPNEZTakCwNmlqB9FrvdP203-h2_TNSBpAgW4uSTHFWHjM-FvJ74NhamlgajzWiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GBum5I9fcvYgJq7ddnAikqx7Jyb31O21majvtPOYhnwaSDFBxdLIDJs3-qgIjzcm6clMBz7aCJwF6QJsvJP2TwP6seZvP5wg09xMf2LdWmhFQafFDNV0a11ktRuOS7e6AKri26KT2_qlL_fwrsC8rKlsjTaup1VxYhDQXNIpeGauYpld3ooqWgkEwQx8BUuhYmvujQi5fDQwyvdxHvGrY0sXRWC_vTEtv22OB4vzA2qL7jF-OjUwcx14NxHzmfbhtkjz63FTHwhUQk-siATdLct3yLn76VaeOS_lJbxJhHzxeNfelwW5fMVFm_fz894osnqkZNCc-nErGPyKgxX6fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بانوان هوادار پرسپولیس درقلعه‌حسن خان.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/31266" target="_blank">📅 19:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31265">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eab1GxUozmDj3EAsi0zcnrA8MdZRRrQrNGCza82tKwWebcysdooFT9ypOqcB-eKZ6Zyqu_AxuS1vB1wzdmE7GfpV4pi4EkhbLyY5lpPI7_O0kOYkl0_JALy6YTxjI6_FbWdLdaa_Khv6A9rH-L7UEmIY6AbOVsh8zm8gI-c7wW2EjbvJRMBAR_YV_FqDSr9JBLs059XZ5lhGtFOL9p4p0wppZUwQKsKyw6c7pvWPRVdYO1CV8BZk3P0V3Hy2Xhmuhy6zkGlRZ53wIQRaql3cRn4DyNrdZo-m7xvtkkaV5thExjaH8ysN5gb42M3syN4-_3LBjjuOMb4CI9fCvI3SaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/31265" target="_blank">📅 19:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31264">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYvs9-joQ8MNSawrhKMiXqTyZtC2h-TUarmdBdlzdtJa89t5V0nQPs03JVpfJmsDPXkR-oSqDCh0i2w1JpjCRRtKOvrH_UiQsw8WNEfJ8t3r2OpH0Scu08EslVLLXxhuQGtXfJQkh47pKo55YfNKXxpCf0BBxPj5ks0hZMW0lUHUhgBdkZDbbgQ_c9LhELcp9rUPorK8Seh8uNAWJu7BaXlLjGHh9MlVtDUKDXLhxU9z9Ixznhro_iNJzh14YMWafbp6rFwT3tP8JiE4TfWmOkan_lUax2eBR4iLbZD_RzKEaS-CZEUJEZz3bqUY4f-0Zf9y4pLPF37ymV4701IB9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31264" target="_blank">📅 19:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31263">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cabaGZKNsqZ7eYXbXUb8s3xsGEnwvjvC3Oug91yxx6j34s4qNaqfM-5mnRtFTcavRjocNHUudN2xotoUMdmjVoeKgNW3ccXG9LUviIGC2C9YENRsYnkOYElMIypXJb3Dsp-bM9fqh98GO0nlwOIX7f0P39_8NFxRlUT7awj24oZXh1A3xG7qndlLQPEMhUBY1BwavMMygI4Rpzd801ssCEJytrD0o4M2XtB8O42seTdrbCQ7YBxrf8KIP6iklFcF7EJw9fYbsjae2CzqupHK9wpzfyDudzqv9Rs7RDGPKLxNni9kLDTgnstZl_xGOKfhnPsp8r5LfX5lxPJyN-hb1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
سرخ‌ها روی‌کرنربازم گل خوردند! گل اول صنعت نفت آبادان به پرسپولیس توسط باصری در دقیقه 66
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/31263" target="_blank">📅 18:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31262">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/866119f609.mp4?token=oJpZApM8BfnrGOFIYEW_nyjdpFZqaX3udIqwKom7uaoT9GquwrwP5kxki6ds9HNb_mK4N9O2QCZUvcJeMcZfVJvV2oenPIuX3LPpDD6SWEYldRC-eKVYkHaYq-dDP8azKou-N2q3q8FD5NshNecGVxyum2HLorD295d0cacRHjKCD6y1uMImZ3CBRNFhNrv6xhcjEI2RKqbem9Lkv-tf_1deuD1--cj5X2k3ozn3j_fELtEgQBhY-8UVS6KCQSZkYt4Vn1DoCVbk-iQr2eEo4KfYRVmj7lULky8fUzuXxIgnaHPAHY1jNGuZgkSmVV12eFfWoSq7bYdGt2WcTj2qtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/866119f609.mp4?token=oJpZApM8BfnrGOFIYEW_nyjdpFZqaX3udIqwKom7uaoT9GquwrwP5kxki6ds9HNb_mK4N9O2QCZUvcJeMcZfVJvV2oenPIuX3LPpDD6SWEYldRC-eKVYkHaYq-dDP8azKou-N2q3q8FD5NshNecGVxyum2HLorD295d0cacRHjKCD6y1uMImZ3CBRNFhNrv6xhcjEI2RKqbem9Lkv-tf_1deuD1--cj5X2k3ozn3j_fELtEgQBhY-8UVS6KCQSZkYt4Vn1DoCVbk-iQr2eEo4KfYRVmj7lULky8fUzuXxIgnaHPAHY1jNGuZgkSmVV12eFfWoSq7bYdGt2WcTj2qtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اولین گل‌ستاره‌ ازبک سرخ‌ها درفصل جدید؛ گل سوم پرسپولیس به نفت توسط اورونوف دقیقه 85
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/31262" target="_blank">📅 18:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31261">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aaaacac90.mp4?token=DHONu9v08bz4dsU-nz1haBsBXNBNkTw_124e-sE3E5rM5YqhFfolDUtp2MT-6wOGlrxG7xdh1HikszwgktvLAbQ2PZ322nAnpwB4ymaIGIIopR1R5uNhd5_ed8ACbZLtuAAZ1iA-SjZH0LlN7q6dwM2uUqIh6ZBwYpeV5Sn47sOHXzzfRULWB5eNiAxHnFFUbqK2x9B95IkDBYfPEZxS8UlFas0AIeNXSQqpGu04t2VVEFhWcnJFzXsiQJZcUQHN6HQFqubt2JnWSooR_-QYhh7BCQoGtfBpZoOvLsT4DopHDhK-7EZ0p-FKrDk4V7Za4F31qvlotA4Fd1byFgu-3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aaaacac90.mp4?token=DHONu9v08bz4dsU-nz1haBsBXNBNkTw_124e-sE3E5rM5YqhFfolDUtp2MT-6wOGlrxG7xdh1HikszwgktvLAbQ2PZ322nAnpwB4ymaIGIIopR1R5uNhd5_ed8ACbZLtuAAZ1iA-SjZH0LlN7q6dwM2uUqIh6ZBwYpeV5Sn47sOHXzzfRULWB5eNiAxHnFFUbqK2x9B95IkDBYfPEZxS8UlFas0AIeNXSQqpGu04t2VVEFhWcnJFzXsiQJZcUQHN6HQFqubt2JnWSooR_-QYhh7BCQoGtfBpZoOvLsT4DopHDhK-7EZ0p-FKrDk4V7Za4F31qvlotA4Fd1byFgu-3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
سرخ‌ها روی‌کرنربازم گل خوردند! گل اول صنعت نفت آبادان به پرسپولیس توسط باصری در دقیقه 66
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/31261" target="_blank">📅 18:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31260">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd9e6967b.mp4?token=Uoar3mmMQbozYzAv8SqADTaWYOHAwpryLV2OoiwwRYYfnCW0g19zPKHYzeFs4PpYIn_r0_hdRd0K_vJXxoIgE4BZyEYnhXSi3UBBppr9sOaa0jYH2Iw5jHwiIeg72rABzDYhu0c3gOY2WYHufQa04c0ZG4eIDxSHtK3OOlYsjaLjIAPeoLjm9NG4gdRIoE6J5Oz-Agbqol2si7TNY3OaNlTT9_nsM712A-QVS4WtSGoXmNsNwSItNZdWTsmgC4E1OWYPR-AZwHdKJeLiwK-gsnsEx5a05SNYOgpwpsEklON3EYq_AyW86ViUMFtAIOWr7nkm2dPmCQiri-QP7fq51w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd9e6967b.mp4?token=Uoar3mmMQbozYzAv8SqADTaWYOHAwpryLV2OoiwwRYYfnCW0g19zPKHYzeFs4PpYIn_r0_hdRd0K_vJXxoIgE4BZyEYnhXSi3UBBppr9sOaa0jYH2Iw5jHwiIeg72rABzDYhu0c3gOY2WYHufQa04c0ZG4eIDxSHtK3OOlYsjaLjIAPeoLjm9NG4gdRIoE6J5Oz-Agbqol2si7TNY3OaNlTT9_nsM712A-QVS4WtSGoXmNsNwSItNZdWTsmgC4E1OWYPR-AZwHdKJeLiwK-gsnsEx5a05SNYOgpwpsEklON3EYq_AyW86ViUMFtAIOWr7nkm2dPmCQiri-QP7fq51w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تثبیت‌پیروزی‌خانگی سرخ‌ها؛ گل دوم پرسپولیس به صنعت نفت توسط علی علیپور در دقیقه 50
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/31260" target="_blank">📅 18:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31259">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db73f92ec5.mp4?token=pronTonW9azUR3mX19AQiw81W7DKUHrV9-55eLiSFRZ3iFXtQebXaJZVpaQYVZiCE6NeMHs1b-GG5OWCERIntJzcceq3A9LEC7TNvbBQyWL9rPPGNgMWhNutvu-ohsvji4Fd9Sy3OwmCIt9Zn36eHSEg5NXbohb0ITmVGOm-1xIR7RnTpwiPE9zrGhj4NtbxYpZ-Fa1f7P94Lmi7qmmlpSLtwzemMjtDd8dzPMJ2UeP8w0yr0adaFROAFFEQPFhACMKEizweoytnfowhTLsFyqQeuAk4cCxCcO4Pb91fY0kNQoi4TRqCexUEB5Sl29fm4U9MxIpcQ6AN15GkZT6SGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db73f92ec5.mp4?token=pronTonW9azUR3mX19AQiw81W7DKUHrV9-55eLiSFRZ3iFXtQebXaJZVpaQYVZiCE6NeMHs1b-GG5OWCERIntJzcceq3A9LEC7TNvbBQyWL9rPPGNgMWhNutvu-ohsvji4Fd9Sy3OwmCIt9Zn36eHSEg5NXbohb0ITmVGOm-1xIR7RnTpwiPE9zrGhj4NtbxYpZ-Fa1f7P94Lmi7qmmlpSLtwzemMjtDd8dzPMJ2UeP8w0yr0adaFROAFFEQPFhACMKEizweoytnfowhTLsFyqQeuAk4cCxCcO4Pb91fY0kNQoi4TRqCexUEB5Sl29fm4U9MxIpcQ6AN15GkZT6SGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شروع‌طوفانی‌شاگردان‌تارتار؛گل اول پرسپولیس به صنعت نفت آبادان توسط تیوی بیفوما در دقیقه 5
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/31259" target="_blank">📅 18:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31258">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOfpXsddPZnMp-VrOdNdYaHaFPLJJ4CXbMr7BFklxdaGqv43eu2jTmRW7RnGnwv7farCjY2dvF1bfoCNk0rtUCAfPfAEy0z2Ryss0Xw69bFdX7bfUO5Hgsvq4WmoXy4Hj977bjH8acgXcfthkfeyyzgREl6w4TtO5X5E-2tL8d_vtOO_xPH1c_hWwzjUq0albJIeZ7uZUH1FP1Y3_3rFsWVvijMk78A0LvHq3a4Et5vdFlM_xyMxPvAPpuh6LrYeC4CR-9VI9o14qMAmmg_HjmOPH7wkaZw3iPPUAHi5E_-Ph-mFbzOj_5zaJE_PRrDL8eeOJ7ZFwIAG_9SK3-iSxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
تصاویر جدیدی از بازی GTA VI؛ این تصاویر در بخش موسیقی وب‌سایت بازی قرار گرفته‌اند و نگاه تازه‌ای به فضای جهان GTA VI ارائه می‌دهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/31258" target="_blank">📅 17:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31257">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0462dcd97.mp4?token=WeKU6-P4PZJPTVa7HZGhj0cHcl3xj5Hr0ZEydNYKfFq8Lk90wPYkJF4_2r1vZfJecAfEhgzKtTcuXSAk7qEVfDGk40OzPS3BL6KVq8vC87ImveccIzowCoooXg4E9amuYXHmUkxii5nD0RbrBIYINZRah9kkCs7zRnDqRCls7cCL8zdg6l6A-RHZvu3ohIFfWYHT3oucMUfH2I1mLF64k6v6NKZVmpbL1vPWj7C9FtTiYJEF4FqRlf5EOtlzmRKRCQ3bJZgv3YWowu3IjXzEQdbBH1D8kuCnaAhrTHjn96hbQ1B2VzaegpWw4JgBLfqM99yxJ66RB8KDKi8kshgVdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0462dcd97.mp4?token=WeKU6-P4PZJPTVa7HZGhj0cHcl3xj5Hr0ZEydNYKfFq8Lk90wPYkJF4_2r1vZfJecAfEhgzKtTcuXSAk7qEVfDGk40OzPS3BL6KVq8vC87ImveccIzowCoooXg4E9amuYXHmUkxii5nD0RbrBIYINZRah9kkCs7zRnDqRCls7cCL8zdg6l6A-RHZvu3ohIFfWYHT3oucMUfH2I1mLF64k6v6NKZVmpbL1vPWj7C9FtTiYJEF4FqRlf5EOtlzmRKRCQ3bJZgv3YWowu3IjXzEQdbBH1D8kuCnaAhrTHjn96hbQ1B2VzaegpWw4JgBLfqM99yxJ66RB8KDKi8kshgVdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از وقتی که مسعود محبی مدافع تیم خیبر توسط رسانه‌ها بولدشد و باشگاه استقلال نیز به دنبال جذب او افتاد هر هفتههه داره سوتی میده لامصب. این چه اشتباهی بود که تو بازی امروز کردی پسر خوب!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/31257" target="_blank">📅 17:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31256">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/499a1fc96c.mp4?token=UMrbhvRi0T4cF5Ew3PR0hPvdeC7dzi3JLqXjaLJnodQgDOTMZqIYw9SZ2EIM_ppGnLMvOIFkTEGXanmM_s5diSrPsvgq20bglXo9s1lZC01W2Bq2_qIcrnPoRjJe7wE8-HkfvGI6Q9GBw5A1Qja0UPSLJlhGhWuKO7CZMpv14IcL9AU1fYVZ6Tm5Fu4Jg8keVZKe7mtrZ5DtqwtR0q0PZPna7gbw6IGATNzxZUxBZLKaWXb-MfGlg4MXEkvE-YX1z70qF0n1L0illZDeT5jtc4bINPDt8OCHNjRWIuiH0j1YU1AykUhGJT2J42Wjzs_ALDT6vDGImzRNTqU5UKImUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/499a1fc96c.mp4?token=UMrbhvRi0T4cF5Ew3PR0hPvdeC7dzi3JLqXjaLJnodQgDOTMZqIYw9SZ2EIM_ppGnLMvOIFkTEGXanmM_s5diSrPsvgq20bglXo9s1lZC01W2Bq2_qIcrnPoRjJe7wE8-HkfvGI6Q9GBw5A1Qja0UPSLJlhGhWuKO7CZMpv14IcL9AU1fYVZ6Tm5Fu4Jg8keVZKe7mtrZ5DtqwtR0q0PZPna7gbw6IGATNzxZUxBZLKaWXb-MfGlg4MXEkvE-YX1z70qF0n1L0illZDeT5jtc4bINPDt8OCHNjRWIuiH0j1YU1AykUhGJT2J42Wjzs_ALDT6vDGImzRNTqU5UKImUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
شماتیک‌ترکیب پرسپولیس برای دیدار امروز مقابل صنعت‌نفت آبادان؛ علی علیپور، کنعانی زادگان و ایری بدلیل‌مصدومیت این بازی رو از دست دادند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/31256" target="_blank">📅 17:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31255">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7613725c1a.mp4?token=OZFA87BjKE2Vg_S6zg9AUECN7zTVmwBCu1_TpYsHvRQ2y_htqQaQ54xT0QwRTV--q_DXOLpvDcB59tEW5tZFHGqFRqZDUbqgR_3PzNC_YUfRI7rhqfjZvAgUTq5Nnwggos1TnY0944a2REC6i3U13-Gx2Do1-2EAGp3D8KWooHxV9Nsgnoh0Cz6z1RG1GJ3jMSlCBX22jHzij9YIRG0KYolq-ndYPoidqm6biAmBnxzDrXN91SJU2OnWEMIAql7IouvdgwWYAz4qrvkR1ovMCU9cOs1x1u9BHU2UlWv4822H4O2hqjRd6t0iR2ff49ScS5HM2DFOJmR8KNj4eoL3bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7613725c1a.mp4?token=OZFA87BjKE2Vg_S6zg9AUECN7zTVmwBCu1_TpYsHvRQ2y_htqQaQ54xT0QwRTV--q_DXOLpvDcB59tEW5tZFHGqFRqZDUbqgR_3PzNC_YUfRI7rhqfjZvAgUTq5Nnwggos1TnY0944a2REC6i3U13-Gx2Do1-2EAGp3D8KWooHxV9Nsgnoh0Cz6z1RG1GJ3jMSlCBX22jHzij9YIRG0KYolq-ndYPoidqm6biAmBnxzDrXN91SJU2OnWEMIAql7IouvdgwWYAz4qrvkR1ovMCU9cOs1x1u9BHU2UlWv4822H4O2hqjRd6t0iR2ff49ScS5HM2DFOJmR8KNj4eoL3bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بخش رسانه‌ای باشگاه خیبر خرم آباد در اقدامی جالب شماتیک ترکیب این تیم مقابل چادر ملو رو به این شکل "یه نوع شیرینی محلی" منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/31255" target="_blank">📅 17:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31254">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcVE8z93mfW9ANJccE0PLVjeovcsiJz09bs4NIH1LXocysN-jwQXdyBBmF7DwtWmLbT0a_ceztRzbZLvF4oRG7-kVPtvr4VsZH5nQMRag_aJ4r8j6xeICcvlJZY-0Di2WCDF6gECP7fxUrNb82cd_U87J--wQFqHeok820QUA_qf4Ctb9vNG9ICBBxFCCdXQhjZ_7CE2iinhE2OKUHJwfvVNLCxcuzKCg_vEHcWp8Y8pplKJ-xdJyreuC7ojg5f-0BLTSyqPOOI1q_z7GFnejMu24bVzBEjljFXKes4RQyyvLkVpCw2BmzqEkYh0LEYEFALQO8ETKfCG3S8xRz0WXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل بازیکنان دو تیم پرسپولیس و صنعت نفت درهفته‌هشتم لیگ برتر؛ مارکو باکیچ و دنیل گرا از لیست سرخپوشان برای این بازی خط خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/31254" target="_blank">📅 16:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31253">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‼️
#تکمیلی؛دستور واتساپی‌شجاع‌خلیل‌زاده کاپیتان تراکتور به‌بازیکنان‌تیم‌تراکتور:همتون علیرضا بیرانوند رو آنفالو کنید. او دیگر جایگاهی در تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/31253" target="_blank">📅 16:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31252">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDinh_XUK85_yFOhIblU-yotAradGnmSWgDX3zBep-zevQcae9XQRKw_f4htFQEXTlxY6X1F9uqMf_sxm35mi_OHa1lxXlBvXHXHuuh3PI1qPmzjHTcaftC3CAnjaCpWKPlZ3zEC8ugrjqSMJjgBm_ThzN8BQsb2NCckGd_fHim0vIk_TVgom2DqUW3UZDB9tT_kQzMJitRDfBspLhBlu7uIZkbGmcSM6dYHMTtCG-Brf0NVuwA292vUqLzVlGmcnDz_HBd2-CHSLvtmUu1YIvt3qiXfXK7UZcKa4y5q9ETglxr7GS-cu1LujKGVrUx53oblFWr4Jlz-VlyfYj0Wkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛ ترکیب تیم پرسپولیس برای دیدار امروز مقابل صنعت‌نفت آبادان؛ ساعت 17:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/31252" target="_blank">📅 16:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31251">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h52J-uh2xAGnEvzy3wd9C-W6HeMBNb8-rmUeFPUXUcAiamZKFQp3i3MEC8SNxcTPE3R0K-1lurvGoMAtWc3n_xfNUZIbikyzzDCN6OHRYgg80wfdAsZBRzEpx1LpOf4yp-uLz1gpdzmwaAZ5SE77KCPQK_2_VRVuInlx34S-2GuTt8wNzJmcK5sp0TESGRXCwfkSeTJE-XiYKqIfdOpGB84Wny0N0Ji0gpYh41pQqFblMQt49WYjaww5lcMaz64bsYx7lp1hTDHvT6i6pBfbXjQ47ykGky5b3WaIuzZaT14QpHnV5NFqxM7cXg461JCoW3o-x43UjZfK5LQ5udiDoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ همانطور که‌چندهفته پیش اعلام کردیم که جدایی دنیل‌گرا و باکیچ ازپرسپولیس در نیم فصل قطعی شده؛ مهدی تارتار نام این دو بازیکن خارجی رو از لیست سرخ‌ها برای دیدارفردا باصنعت‌نفت خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/31251" target="_blank">📅 16:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31250">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoCM8Yd32uD5EuT7h9En7QxVZkUaYoTcy_bnn8WbQnM9M2Z0vM_h0i3lSJ_pF56HF_cRiP7ENyP6sTDc9opXa8TmbQiAMws7xUJYeLCvELIx0VG1u2kc8RB31dQopvAl3UHf79uhYzKORC5Cw0gvP9NoSLEzUpnUR0iw9mfEnuu6lRsXFvI2qnkSwb1M2C-rssgqfyC_nxB8jv_XyAF9vr1T4JAalopWE0g6qxirwggj96mryW-dzZR9aWW1YrJrbOC5wHp8H3BJB6MK3mR98LRQVK1_DBBf5IzpK3VwZ5EckmOMg3eEDjZIbuHmvQ_qILmOtwIiUAFD0p3Q3Tue2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
به احتمال زیاد پرسپولیس امروز عصر با این ارنج به مصاف صنعت نفت آبادان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/31250" target="_blank">📅 16:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31248">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cW3pLJoh6JH3T5Fqdi2bjWEPKPdIuDDhxqNY0V7nW1uKHqXGJnwl3q71-ObHJqtsmHqIibzMx59S76-P5Dkv85-jf4VrsX5Ve79xTQn5h5qyCMk6qeHMRSjPqVU0hgC5wQmkFfZMWQ8zX1dpA2Ja70qY1CiegcQW8ObHVl9Beeq1Jp7WP2FvoQ2r_2zm8rCUsdW554Gm0G9BDAO5RgubqSSgq1TP_C_abTbSaz-YXOj4AaYhdoSev1xE3b7p2V-1AWpZKac42TanLnvV3fr_8u49nbB1cQooAEmiiSJnl3QumpIVaWJQ7vJJ94xA7xcVLzKHrC9afnX0kPNsTVPxbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OZZApHTBPr1xOYBtLD7ULAE3qYJvSbibtfrDeZHpdZWdhU6IC2SdrZXAlpSrmqzScKDGYWlna1TO0SidIu7nNTdMLQD1tAxq0sguMwMbRPG-67HdfyUELqaSIQcZ8LC3G6vZnEeEXhU2vfaRXW_9U41W_9nIrEdnkfa6yF9aneoLnmBWR69X-yqY0EmG1o_lW7NzvP5Jp_aoU5FvFS50qhczvwMVIgL50FNEyqOyn9PufKF4OH2idh9MXk394OkoCEiSJINTTFy3IyzduGpOqqAxYoXJOYUMHwAqX2irODH5oWciXC-jUpvB--iX6yINYCGvT1zXLM7DSprtF9OwfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تشویق‌ده‌ثانیه‌ای‌لیونل‌مسی شماره 10 آرژانتین و ایستادن به افتخار او در برنامه ورزش و مردم بخاطر خداحافظی او از تیم ملی فوتبال آرژانتین در اوج.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/31248" target="_blank">📅 16:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31246">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAwClJGNDexz0RN_qQGKGeFtABMs_ir1KSUIgJZvrC1IB-BrLKcN0gIm22xrpfvNhOyOOTrnZNwyurA4ddpOSX5W67Z5JUH1iC-Xfg7aVZf5mLxD2lA8imnvoaSHVvasEp4QiKpuYTLryhDf1bllG1x8muFR8R_RHnOACDWGUTIvYlsajDh7f59TT7t5yFA1KFBEXgUv3W6DgY8WP1CTuxgcIZmz3IbBXmupJLxuNdXEEFqynUHonLw7pgnJymdsMIMz1q1YhC1FGb_K9HFBINKZai46ULjT6MoR4qMjHS2tN3DrDwQ8SOmRCsjaZ_NQvcvunWbw-VNnW58qoMGpgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیمار جونیور، گرت بیل، محمد صلاح و ادن هازارد درکل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/31246" target="_blank">📅 15:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31244">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2089087958.mp4?token=mOEGK8kDQUbS_vMlTQw1B7mhtjR69BZ_GcHb5bfPwmjnvMHh1HB42ccZcbBZPdfovoM2U9xqYjU6kyaSNT09SIiB3izDFsLcueQcqMGaMOR58Kc2t-fnXuIZ1zW4PYDC_a_7iPcJOwsLPpDmQkZrhv0nXsM3cSCP11CC2E5WyviAoSEps8ytpD1BPNwLIoPtpOHK4yTgQV0WSTRIiD9vLKMKF58CfAV87t8QOB-XXBNEb8WWeKyeuT3gTE4kfz5jtDBCcb54jlMHnfo3Z4Kv5gnciw50swwRex5PTTtqus9D10SXiQkDWTeXhMEnP6ymfVKafA84xLu5_bwP_wawVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2089087958.mp4?token=mOEGK8kDQUbS_vMlTQw1B7mhtjR69BZ_GcHb5bfPwmjnvMHh1HB42ccZcbBZPdfovoM2U9xqYjU6kyaSNT09SIiB3izDFsLcueQcqMGaMOR58Kc2t-fnXuIZ1zW4PYDC_a_7iPcJOwsLPpDmQkZrhv0nXsM3cSCP11CC2E5WyviAoSEps8ytpD1BPNwLIoPtpOHK4yTgQV0WSTRIiD9vLKMKF58CfAV87t8QOB-XXBNEb8WWeKyeuT3gTE4kfz5jtDBCcb54jlMHnfo3Z4Kv5gnciw50swwRex5PTTtqus9D10SXiQkDWTeXhMEnP6ymfVKafA84xLu5_bwP_wawVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
شعرخوندن‌بازیکنان تیم ارژانتین تو اتوبوس برای مسی : "لئو تو مثل اونشب تو قطر جاودانه ای. مارو ترک نکن همه میخوان تو بمونی و..."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/31244" target="_blank">📅 15:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31243">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9DkbCJ0gplDaVzfEnbswQ1rsWviK8ZuAQ1tsPiAyKP_PwJmMajaVkHp4ebYjjbWJfYKPrXb3U2Hq8jT7mx6-c4uq_rR-kFu1ETnofiB4JpHFTNSdMGI1-oDJbLgMo6arBh6YMx6jdh_xk4DoYNpsVsgHEQ6911Tiib0uke-5ln3a0iAOVnwwrS1-EWt8vidQfpDtcN3-MlUNpfqkTWWj_cDvX2Poo-tTx-VGZnTL_meXM5OVHsVxt5iruNbYXdr99K2XBNy_w6RyP6_gMaXd7ahD2IBFT4Gq8CxTfcyBS-ESW_FBmmP6pRck44yz2OM8VRAGRa0XyKUikFxRGzIEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
🇧🇷
#تکمیلی؛ با تاییدیه کادرپزشکی باشگاه بارسلونا؛ مصدومیت جزئی رافینیا دیاز برطرف شده و او مشکلی برای همراهی آبی اناری‌ها در بازی مقابل ختافه در هفته هشتم رقابتای لالیگا نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/31243" target="_blank">📅 14:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31242">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33992a38c0.mp4?token=XO33_-UF5RO3ZRdZmkgko4QMWozE9CloAst5j59LnQa3gq4-UjwbRZ7BbXPvs_Hc_1XMIG0I7Qj_UQTEs7S5pOWDV_7yHTYrL1BunBrRUPOe94PZohaDwvVHlEl4jgxc6mA9LwE4HAe_lKIgQyO02cQspCfMAFHAmPubT5LkVHf74wB11OYXDgo6-BcesfOnJJs6_w7yXldvEdwZvuu2JHmKJwPFaviF1XgpNR02_aFljGr26b-u82HppKli65RDH5dSnbey9z69ReZWhmlSm7PXVy8s6j5q_Ob_ujZWkow_ZYyBqNlyVRbxWTe55b8SL7lGX4ZIOo7GUAvcxGUaKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33992a38c0.mp4?token=XO33_-UF5RO3ZRdZmkgko4QMWozE9CloAst5j59LnQa3gq4-UjwbRZ7BbXPvs_Hc_1XMIG0I7Qj_UQTEs7S5pOWDV_7yHTYrL1BunBrRUPOe94PZohaDwvVHlEl4jgxc6mA9LwE4HAe_lKIgQyO02cQspCfMAFHAmPubT5LkVHf74wB11OYXDgo6-BcesfOnJJs6_w7yXldvEdwZvuu2JHmKJwPFaviF1XgpNR02_aFljGr26b-u82HppKli65RDH5dSnbey9z69ReZWhmlSm7PXVy8s6j5q_Ob_ujZWkow_ZYyBqNlyVRbxWTe55b8SL7lGX4ZIOo7GUAvcxGUaKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهترین‌نمایشی‌که‌یه‌مهاجم مقابل ایران از خودش نشون داد. استپ سینه‌ هاش آدم رو یاد پرایم زلاتان مینداخت. همون استپ سینه‌اش رفت تو گل ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/31242" target="_blank">📅 14:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31240">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cbHH7PqZquFoNHjXWkWRj0Oa9AULfp23a52kEYkDK7i_pkAvXhfKi5xsd8feWm7HQPtNkKxcQOwGu62Dy4au0LN892BL-nmU4RDWTJdf8PfQsVyvU8KAOw8t9CYgwr625KlVSfuPqH2cot-AVdSPUtmoZ9DTxbREX1xuI_iVOFLEnnq_aUYZQBCg1K8ei7KlLHrwlwtih9wradGGl0nDqpLfEia9zsfWsAQoqzzTMcTsJyM45hM0YKvXMigQviHP2eG9eAT3lKI6onpMPWE7fQ9spHk3RK-jaWkx3ohalTuDQiiolawUIisBDGQ8OwKIChtBil_YOxJHYiSTWlAVKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CfAiaYtm2hS_C3B9amu6dwNFugz9n6IJY_PcObQlb9F9Rl0DYrwKCfn5uiMr9Vy10aqo3zRa8jLctwZzptIckeTQZ0ex0uTzw7RKNUxHlqnJt1iLO2dg7DOt3C_gyaj16P44BNhxC5ZjUsVpT_MfN6cO_FM7inhQc3wV6ufKg_l12f2UYq9F5Hce0E5XZq6ctA3KB9_BeLslLrRzD3mLlRVV2JOR41t3R0y7iduKuugYt1dMAblyE873QkAyeaE5CISJbhDPSOTbzaFm398m8aB6AbTrtIn5EbSsjr2LTayYn_B_10EWBvrDcb2bqV80Rf7f2TKsTGOU1iGCai0iDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
حضور بانوان هوادار تراکتور در ورزشگاه یادگار در جریان مسابقه روز گذشته پرشورها با استقلال.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/31240" target="_blank">📅 14:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31239">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-eLBvfRexZFblqfA4jHzcg28rn1zxArfJWTRTk0nzly8vI9AtbUouV8znwdYS7IwFTZ-rL6nB1wRRd6aE64XErqLkv_5hpv0FXy4Y1MMo-rmLr9f4LrfsVtcwGwxRn6vHp22ttvA_gSME5bB6NhuLC8jArd5kywixDBIYZVUfDfNNvK7788kNTsXTp45eiLQrghF8kZaw9F-_ch-wxh48RHWLB2tnzmu7bZMaiF0kSpcM2rWMeJu19xhD0QL2AKGNHi4vn8GdbZc43vY-2VaafBME3zY1soLoawCkNPsoKlXF-1TKIbjX0Lct27_Twrsyy6U-fzzq962JojQWcPBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های دو تیم پرسپولیس
🆚
صنعت نفت آبادان درتمام مسابقات: 48 مسابقه، 31 پیروزی پرسپولیس، 6 برد صنعت نفت و 11 بازی مساوی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/31239" target="_blank">📅 14:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31238">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dq2XlsTi9Nsc64OE7BVELAa6AIVh9pbZzCxDmAg5mTWIIKaZ3Lslz72N2Cz2l7jO_CksouGPJCbY4jMNwkf_o1s1WAEhKSS7jkf6Qiy6d6uG8WVRjzpKgL8fQIaHjhOK6gWonY7pTWJ_xF5WtCMb-Rzf2DgXR7GOhRHioQ0nuQ0D8AMOiKmODSGVopKqCljvUCiqZn94v3E7oKbyo8EIMNlU5KWzpc1lba3_LzvNaEAxBxvemlexn0QdljFtgPlUxFhz5xF2OtzRMxkm5KRFmbyzib_NHeH3i3AzVPWzLXRXQDIGAx07ZV51JCkB6-2_YYKUTh1xVmWH2I_FHMwwlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
دبل نیمار دربازی‌بامدادامروز سانتوس در لیگ برزیل؛ جفت گل‌های نیمار از روی نقطه پنالتی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/31238" target="_blank">📅 13:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31236">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DsjNL38xJ3tVPXRru5TWT8ER33cNIUZGUnUecDC2BbVk8ZyB5acHx0B3nvDS1P1xnH2nGfi0JY0mis9gbGVFTDM-LqQh2fvlbQatRDMd-raXeDLeVnsUXn-4c-Rmgs7G_OnEePVES1zg95zVPlZ4wygmvL6HJT6E-a0IrAgYX1cOzab-Tc3BpUVZlxwDxHfmAv-Fo_2ulo_YO2kJnf7tlItcnugfZow_Rk-I9fKoks094SDNkkRHhYTK6HbsHu8xwCKTxu-ub56Tgvt9niWMOkKYBDzO3enlPzsbq74f_r1RAAn4eIm7RYoxv6NiVJVpEZ5adIeGD1OnOmmpyf_VpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lrJ8lD6oLUexq_EyL6mADJwCByWqy3Mdk9l4B_NNoPIImDZPT1fa1NRZatx08RvDH9qwHS6JuBxBglgUQQmp-kEeSnz_pJqlihMV8zJjX3S7Tx2R0iQfBryJK2tRHQPWCLefgshCIpNL0pO2KkVIZjgjQyQgI49z8IsLn_SoAQ3c8r-5KRHJdUVr7ZNt7MFwujX9OSFZFObKBt42RjV6H9mdviqktixHktTRDboWsOGywfmke4IH18idjAE4V-hhzfV_ipaat6ASnVY1WHQZPm4H0Vwu8ht9Sme52soCaIo-yI4x6Ryqm6Jd6yop4pjASIsANpbhzaESNL8v-8FuxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صحبت‌های تلخ همسر خدا بیامرز هادی نوروزی اسطوره باشگاه پرسپولیس که با گذشت 12 سال از فوت هادی هنوز لباس مشکی‌اش رو در نیاورده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/31236" target="_blank">📅 12:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31235">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FY1lAx73AwHGyBPg3OyzvQQrj-598u9b5ODKJ_6dBJXvC7zj21TLStmVKg-3TDL-tenL2EW5B4N_12sfxmxOiNL5u1Kr7BtMW3tHW0YoMogjQkH50KcjwV3M34Yl5LrlNSJYC0oQ83NVVtHs9cD9ZbINefVixaMkFlJnaG_vHp1EaEAUUdOzJVMdQjCPxSAVWK0KupLrky6ay6PVIkFcBr-2huzjqcmDX2SUtyhWQ8anTrM7XKKVgqlu_bFU37NMqrhysoK4s0RRCSG5bGsbGTiiX81nKWr_aSTf8MlmEILPwsDUs9TWNEQ4Pxc8tzmMP76-nDs37EH04l-woHEVxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تعدادجام‌های‌معتبر کریس‌رونالدو و لیونل مسی دو اسطوره تاریخ فوتبال در کل دوران‌حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/31235" target="_blank">📅 11:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31234">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSp2cFSv9c-dpjz3aXLCvRHoi65zrd8JFvIwmSkA6kp3JkP6GI0K1g8CI_3XWHFqXcvUswbFNRSNz5L_Shotb3V2sZ79JOOkgVf5Va3965-ZQAQ4wdqRIfOmSPO-UELtl5zvZ1Rj-zheiDwfcVA4pE6RPrmdE5XcVKrpJW08j_GfnX3pxBAxOIIth-pGiFMXC1UKwRCXYTLqcMZPr5L90D1uFSRCwu7ag2ClRzG-7ckb7L2smtuT6z9YkXy7C3bUlsH_Fe-VzFJM4exQzCRqPZmpCvE0EG-fbHkvP93v5YiwCo17ZWpdk6wL83lLsoV0_UWNyTzmveYcmgbgpMRd8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
باگذشت‌دو روز ازبیانیه کریس رونالدو هنوز هیییچ بازیکنی از پرتغال این پست رو لایک نکرده!
‼️
این‌ویویو روببینید تامتوجه بشید که چرا کریس رونالدو اردوی تیم‌ملی پرتغال رو اون شب ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/31234" target="_blank">📅 11:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31233">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
این هفته هرکسی برنامه داشت امیر قلعه نویی رو تیکه پاره کرد؛ این بار نوبت به تیکه های سنگینن ابوطالبه که اینجوری زنرال رو چپ و راست کرد.
‼️
ویدیو کامل قسمت سوم برنامه ابوطالب رو هم میتونید از طریق پست ریپلای شده مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/31233" target="_blank">📅 11:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31231">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVqRkpYI7qyhGN4RTllLmH96TaOFHHqTYsktumteYXdLnpzi_-EbJyyue9abClybIOcCgFJSbwCN2ixk-ESxFBXaL2K_KPGLJMOd_WlAr6NW5Wp6DWOTBrhljd3sUe8L_R7pVBeheG_N9nxTLhgJ7AUqUnXeMgCtpi0AroK7t3hEhcFKKsRxjIo6QiAdJtq3zLTlaRNSx3ta63xT9K5fkY0CzbOKjEWLpX-FwCMbaRR1smQkix35O_9Px8i-dmQhdk8zpI6ct_AzY8uS5hSXfJMCpn_klT4TYVi5bm7t4XpB7mWXcCfabgcqC0N1b1DxcnjTAabcb71fVOPcAV8Q3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
به احتمال زیاد پرسپولیس امروز عصر با این ارنج به مصاف صنعت نفت آبادان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/31231" target="_blank">📅 11:04 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
