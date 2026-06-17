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
<img src="https://cdn4.telesco.pe/file/hIuGvJSyWv7e0pfT0duJG5ZKbWz1UJ47rSzSkhdTTafNlcq2NCdhPlaoyoqxJiAXGfzuKj1hBWkBhNkPAshTSIJ-OJG8Gb_zWzKs3RGUXoOaeZGpugzuAECazilHsIaZN0GKqFWD2pSKdib8O_p9_7aNnJ_iaQg_YvoeOnqGjd91c4ixQEzSzZ5SO4n9YOlUolfJmODdHo-Xn1eJ-lCO5l-FfI9SCp4QCLdvSMKM4DQJCQoVY49wPhYm8cXRqqdj4THEGDCMOUATxBeu3EwZpE3zj5OsVUI5s6la5TwL_iATw302ssiPoY-wUwYjfxmnzp0deFimXp43qg3IQVsXfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 223K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 20:57:42</div>
<hr>

<div class="tg-post" id="msg-66378">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533e14dcfc.mp4?token=T0HIX0gmJr21MV4_6bUrnwTwqoB0o2bo6xG-zP3UkFJuA-r_Va8h7NLXRrcycgJaPld5Ub4Qb3v03wmISNSSCQKeG2pQrp0JMlFDVvUIVvgteq4U_FaZiJaR5UW1Q3DZY7pDN9kZ9gPM7BycO1dczIgkp4kVl-nkeXY-R3KXDFqxbfc6SgAd2rpvHvDCpM-laZXgukPyRV_6DYyk9UxovOBmT6rEoxUahCj2qRQlUr8VCbI72lA2vynz0d_h8TLXCR9FgqQoxpVgzChf8kJoyjfukHjo69pOel060_xu1EerrpdNN70vyJCa2MF2fRIVwkEEgwhqxfdhKXoNfB-epA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533e14dcfc.mp4?token=T0HIX0gmJr21MV4_6bUrnwTwqoB0o2bo6xG-zP3UkFJuA-r_Va8h7NLXRrcycgJaPld5Ub4Qb3v03wmISNSSCQKeG2pQrp0JMlFDVvUIVvgteq4U_FaZiJaR5UW1Q3DZY7pDN9kZ9gPM7BycO1dczIgkp4kVl-nkeXY-R3KXDFqxbfc6SgAd2rpvHvDCpM-laZXgukPyRV_6DYyk9UxovOBmT6rEoxUahCj2qRQlUr8VCbI72lA2vynz0d_h8TLXCR9FgqQoxpVgzChf8kJoyjfukHjo69pOel060_xu1EerrpdNN70vyJCa2MF2fRIVwkEEgwhqxfdhKXoNfB-epA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
مردم از من می‌خواهند پل‌ها را بمباران کنم.
من قبلاً این کار را کردم، چون می‌دانید، آنها به یکی از وعده‌هایشان عمل نکردند و من بزرگترین پل آنها را بمباران کردم، معادل پل جورج واشنگتن ایران.
اما ما آن پل را بمباران کردیم، دیدید که
@News_Hut</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/news_hut/66378" target="_blank">📅 20:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66377">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea27fd13ab.mp4?token=DTCvR-nl1uBKAi2o5PgNMn1oVGG-_GeLarTZ0I6FQhn-NUQ7_GjxJYFd6DsFtczlvY356URfGQLWzZ7gYNiYmfv9H59oPZUbxW2KYZoIGH4eD-1vTyhZe-X4G7gdGLxVOxh9NS-fTvZ92Bg5o1Vt-dgbjlIwYgiIILV8eD_R1qHiBYu9WQK6JEzd0pwnMMUlIZLA9G6NYwcr9nedotDhgSllLaKbpPsfSFyUKPrNu9y2gt_Eq_k3kkAgpFJDFFh0rEk6QCibYbF3zU7-IhC4xz9IAxKKRvu-Ee9j7B-dl6v5qgy1J2Iq3S348bcs5vRxyXKonhlXLU6Dkg49pnlIZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea27fd13ab.mp4?token=DTCvR-nl1uBKAi2o5PgNMn1oVGG-_GeLarTZ0I6FQhn-NUQ7_GjxJYFd6DsFtczlvY356URfGQLWzZ7gYNiYmfv9H59oPZUbxW2KYZoIGH4eD-1vTyhZe-X4G7gdGLxVOxh9NS-fTvZ92Bg5o1Vt-dgbjlIwYgiIILV8eD_R1qHiBYu9WQK6JEzd0pwnMMUlIZLA9G6NYwcr9nedotDhgSllLaKbpPsfSFyUKPrNu9y2gt_Eq_k3kkAgpFJDFFh0rEk6QCibYbF3zU7-IhC4xz9IAxKKRvu-Ee9j7B-dl6v5qgy1J2Iq3S348bcs5vRxyXKonhlXLU6Dkg49pnlIZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
گسترش توافق‌نامه‌های ابراهیم چیز دیگری است که امیدواریم به آن دست یابیم.
و من فکر می‌کنم اگر عربستان سعودی پیشگام شود، لطف بزرگی به خودش می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/news_hut/66377" target="_blank">📅 20:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66376">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0cf6ba4c.mp4?token=g9v5qE0lufVhTVtOtYh4A0Ctsm85pjP88fuH1jjVy_hB3acExX8ntc9bQNnn3OgsroI6yqTS63_g-4J8uOik3ogZMb6Elts31BgOk2K-Jw0UqwEMKaQBudukBPkS7KYXMwW-UnpBX6m6KUGDFizfnmvVoQxmaMXZYlhdDMj4EJJ0T802D0GzB9YY8o5iBpmFkR-mV3yHOQeZknItwJZxeC0ou8RKHRAH1TJ71N19DthAEdykANl5SVMwEx8UsZbDkSZrEMKf4hSz1OMnV5yXXIM7na7elORXnWDQ0O5qgEmU_cOfNej2pMVXf6gTIEhTGTCvSsHebjD9hPBiPIYDUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0cf6ba4c.mp4?token=g9v5qE0lufVhTVtOtYh4A0Ctsm85pjP88fuH1jjVy_hB3acExX8ntc9bQNnn3OgsroI6yqTS63_g-4J8uOik3ogZMb6Elts31BgOk2K-Jw0UqwEMKaQBudukBPkS7KYXMwW-UnpBX6m6KUGDFizfnmvVoQxmaMXZYlhdDMj4EJJ0T802D0GzB9YY8o5iBpmFkR-mV3yHOQeZknItwJZxeC0ou8RKHRAH1TJ71N19DthAEdykANl5SVMwEx8UsZbDkSZrEMKf4hSz1OMnV5yXXIM7na7elORXnWDQ0O5qgEmU_cOfNej2pMVXf6gTIEhTGTCvSsHebjD9hPBiPIYDUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد اورانیوم:
هیچ‌کس نمی‌تواند به آن دست یابد، بنابراین مهم نیست که ما این کار را به سرعت انجام دهیم، اما می‌توانیم آن را نسبتاً سریع انجام دهیم. هیچ‌کس نمی‌تواند این کار را انجام دهد. و اگر آنها این کار را انجام دهند، ما با موشک‌های پاتریوت به آنها ضربه خواهیم زد.
@News_Hut</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/news_hut/66376" target="_blank">📅 20:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66375">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07c3e1404.mp4?token=aC7Y-tbJ242BSeEzHqATneotmJGMhFnO5KzZSGUutn9C6lzrf-R0zB5s0uyXZ9RmCqTLDgGp8fugtCUK2GeRHvpjlVUcgWQ4caHLVTtUHYHBHXp91cil7CJbZtFcph4krN6CHZNC7USVLh1ZJiCejaUfR9iW_7BIZSzzUI1786nKIgyqeM8erKlaamd_BFvHvPKOfIYBKue7Obw_ANdQpkMwhVBKaV1XX270LgGuzuauhOAEZqvvZwlyUFXGbOMqZ5Nyn2vqOefWPlVMrrAY-4YdmLMNyN0H7XARtnVe8js3nefinHsrPsF3GUwkEXBc5StMgP-LCRr0fGZeoz24YQZm3-5oN1jLCw0RaAXbJMhFfqOPv30k4uq0yLmSJ-wzXLkr8JiCZ6zWGqgix0sGpKPAZrD5WKS4ZHml1S2jnNj3KQL9aAaGerWZ3yzT_ERook4-e7zDUUj8PC8MLLzPzRv_fQ37sEJMEOWVRoK7PvmrJrwplIbJ5GWqpc0QWxtr6n1vwU_TNRb4XqsNG6cPIPP9Qmc5cc6LHRIlfhULCqE_SXIfTb09p0skcwmvnXCr7etS29Gkf_H8fNxnQbzZewGT-Hhyttv4m4XTf0due3cD8tl7hAmavAAySB61Dm3fHNvmFhgva8F-l8Vui7NSqYy0C_9OTA9UaPXGX6ybALg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07c3e1404.mp4?token=aC7Y-tbJ242BSeEzHqATneotmJGMhFnO5KzZSGUutn9C6lzrf-R0zB5s0uyXZ9RmCqTLDgGp8fugtCUK2GeRHvpjlVUcgWQ4caHLVTtUHYHBHXp91cil7CJbZtFcph4krN6CHZNC7USVLh1ZJiCejaUfR9iW_7BIZSzzUI1786nKIgyqeM8erKlaamd_BFvHvPKOfIYBKue7Obw_ANdQpkMwhVBKaV1XX270LgGuzuauhOAEZqvvZwlyUFXGbOMqZ5Nyn2vqOefWPlVMrrAY-4YdmLMNyN0H7XARtnVe8js3nefinHsrPsF3GUwkEXBc5StMgP-LCRr0fGZeoz24YQZm3-5oN1jLCw0RaAXbJMhFfqOPv30k4uq0yLmSJ-wzXLkr8JiCZ6zWGqgix0sGpKPAZrD5WKS4ZHml1S2jnNj3KQL9aAaGerWZ3yzT_ERook4-e7zDUUj8PC8MLLzPzRv_fQ37sEJMEOWVRoK7PvmrJrwplIbJ5GWqpc0QWxtr6n1vwU_TNRb4XqsNG6cPIPP9Qmc5cc6LHRIlfhULCqE_SXIfTb09p0skcwmvnXCr7etS29Gkf_H8fNxnQbzZewGT-Hhyttv4m4XTf0due3cD8tl7hAmavAAySB61Dm3fHNvmFhgva8F-l8Vui7NSqYy0C_9OTA9UaPXGX6ybALg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
💥
پرزیدنت ترامپ:
هیچ‌کس سخت‌گیرتر از من نبود. هیچ‌کس سلیمانی را نشانه نرفت.
می‌دانید، وقتی من سلیمانی را هدف قرار دادم، مردم فکر می‌کردند این بزرگترین اتفاقی است که در خاورمیانه در ۵۰ سال گذشته رخ داده است. این بزرگترین رویداد بود.
او رئیس ایران بود و مورد احترام، اما او یک نابغه دیوانه بود.
@News_Hut</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/news_hut/66375" target="_blank">📅 19:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66374">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9392768ed3.mp4?token=g6X7saQ1vEbJw6iBXbgW6h3hWKwG2grXfrNW0UbQxpkel7z859dyERraUJMNeYkw1QtjJDi-xeA5NE8tzYRbbzbuxv29Xx_GR0ygjSNlliAua5UCLZBNAWIxQA3QsqffBhmq9G4QzdoqVyX8knD75I7wGMIP50SBE5fkFgiS5zNJNZRQRgW_kZqR4RsWVRCl9HyxWMm-7BZ0loL1CqT8n8xcof8g9SDB-bENsKyn4h4o3canFjD5Wq38xe5HE1ME2ItsdJeTt-Zi1ZfnRcod-gw2CfyYS2iAplN2Eqy6zXgRJ9-Yc2sjpBi6atCFqM8ATXazDOW2e0dPDl1htVn1IjIN0rz5QVqY_IphPgfLwdPzZVSpRuqvrFURmo-6UeMq36IifbFNpFAjhNVHozm23JKJtnCFo0CdVlJ9WVjk4_gvREvLGl5nPqsUWUAcJR4M1B3h6axIC0qkGEXvcT1QtmNpsQyUDhH6PXxK_Mqp5u7yNxYqeMKKKzhf1nqJ492MU-ETE35cMqvwJp6AArVPihH_5trFNY-JSfrwk5Ok9FEJx3X5BrFQOtyg201rXQRLpyRAy1wwsYohKrIcSWvJ1DEORykX_lfmPHROtLSIFFGn6g1XBYkP7G3_tO3KjXuYhbb4c6TLmvTyQs8lD-ktLWwwJntl5nxMrshwpMxcUmY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9392768ed3.mp4?token=g6X7saQ1vEbJw6iBXbgW6h3hWKwG2grXfrNW0UbQxpkel7z859dyERraUJMNeYkw1QtjJDi-xeA5NE8tzYRbbzbuxv29Xx_GR0ygjSNlliAua5UCLZBNAWIxQA3QsqffBhmq9G4QzdoqVyX8knD75I7wGMIP50SBE5fkFgiS5zNJNZRQRgW_kZqR4RsWVRCl9HyxWMm-7BZ0loL1CqT8n8xcof8g9SDB-bENsKyn4h4o3canFjD5Wq38xe5HE1ME2ItsdJeTt-Zi1ZfnRcod-gw2CfyYS2iAplN2Eqy6zXgRJ9-Yc2sjpBi6atCFqM8ATXazDOW2e0dPDl1htVn1IjIN0rz5QVqY_IphPgfLwdPzZVSpRuqvrFURmo-6UeMq36IifbFNpFAjhNVHozm23JKJtnCFo0CdVlJ9WVjk4_gvREvLGl5nPqsUWUAcJR4M1B3h6axIC0qkGEXvcT1QtmNpsQyUDhH6PXxK_Mqp5u7yNxYqeMKKKzhf1nqJ492MU-ETE35cMqvwJp6AArVPihH_5trFNY-JSfrwk5Ok9FEJx3X5BrFQOtyg201rXQRLpyRAy1wwsYohKrIcSWvJ1DEORykX_lfmPHROtLSIFFGn6g1XBYkP7G3_tO3KjXuYhbb4c6TLmvTyQs8lD-ktLWwwJntl5nxMrshwpMxcUmY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ :
رهبران جدید ایران باهوش هستند، بسیار باهوش.
آن‌ها بسیار کمتر تندرو شده‌اند. فکر می‌کنم آن‌ها خوب هستند و واقعاً کشورشان را دوست دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/news_hut/66374" target="_blank">📅 19:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66373">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885ecefd64.mp4?token=uwZ5M2MYmVVd-z49B8IF9wzTwaCwcddtDmqfkpYqUw3AB5sHkHP1W6xvb2zUcQaQ1tv8_i3IoC09axhFquR0k36CvKh83dPAS0wbudvttIqn6Y79Enx1T0MmIH4BLW8O6OPO57yA4m4uMroUbvgZhiCoXGWd9IBTiP3DniNApMkcvZjfaTbKwG7s1CHF3mMtXPNZ12k5_nJGFXhMmGcMzWFpVI95btoCJRXqPUrlbfGa4_7CuDCeOI39Mmk0CuO60HzfQVpNu0RAijPTBAjHtEgVIruEn8a9vvST3JHFKXjmHfiwp_oe6ZndK7X_VFa57NjO80n7Ygpo4a4ld-aTRX5jpbK1gxQZ_oTrOGYzu_X8YAYOj31SeCJPwG59moLb_dsv2OOFNAXd3gg2ezz_xB8zviAcbeigzors-Cg_ZVy_EPlTgP4AlCcHowisHAnE6SPYSLzLAcRR8f7SIpN7SxLZIQTxAu7YoZcarNRXvw1UkOYQYMbvYysX5KgFsXPzvmINb21E9G93MSaQECf6bOvx0YQl-xhBXbiUf4qQ0_KtVEv_m3mz3yGIhZ3HUKxKtXJ559Jp5WNIqC3cokgYl9zz76nAepHufSEo3qQ-ecE0ElajHSirBOQjaWdfO7bDAv5TqBnTlWsGxSOxid_xofOCw4NTPAI33q2-GA2dp9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885ecefd64.mp4?token=uwZ5M2MYmVVd-z49B8IF9wzTwaCwcddtDmqfkpYqUw3AB5sHkHP1W6xvb2zUcQaQ1tv8_i3IoC09axhFquR0k36CvKh83dPAS0wbudvttIqn6Y79Enx1T0MmIH4BLW8O6OPO57yA4m4uMroUbvgZhiCoXGWd9IBTiP3DniNApMkcvZjfaTbKwG7s1CHF3mMtXPNZ12k5_nJGFXhMmGcMzWFpVI95btoCJRXqPUrlbfGa4_7CuDCeOI39Mmk0CuO60HzfQVpNu0RAijPTBAjHtEgVIruEn8a9vvST3JHFKXjmHfiwp_oe6ZndK7X_VFa57NjO80n7Ygpo4a4ld-aTRX5jpbK1gxQZ_oTrOGYzu_X8YAYOj31SeCJPwG59moLb_dsv2OOFNAXd3gg2ezz_xB8zviAcbeigzors-Cg_ZVy_EPlTgP4AlCcHowisHAnE6SPYSLzLAcRR8f7SIpN7SxLZIQTxAu7YoZcarNRXvw1UkOYQYMbvYysX5KgFsXPzvmINb21E9G93MSaQECf6bOvx0YQl-xhBXbiUf4qQ0_KtVEv_m3mz3yGIhZ3HUKxKtXJ559Jp5WNIqC3cokgYl9zz76nAepHufSEo3qQ-ecE0ElajHSirBOQjaWdfO7bDAv5TqBnTlWsGxSOxid_xofOCw4NTPAI33q2-GA2dp9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پرزیدنت ترامپ:
روز یکشنبه، ما به توافقی با ایران دست یافتیم که به همه چیزهایی که در نظر داشتیم دست پیدا می کند - همه چیز و خیلی بیشتر. جلوگیری از دستیابی ایران به سلاح هسته ای همه چیز در مورد همین بود. این حدود 99 درصد بود. آنها نمی توانند آن را توسعه دهند یا بخرند. آنها هرگز نمی توانند سلاح هسته ای داشته باشند
@News_Hut</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/news_hut/66373" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66372">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/66372" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/news_hut/66372" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66371">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rezbhXflGnYGZIGlMWpczoc8CsfIw9EUz6uxUQiebe53ShhCrDo87loeNL5cut5IjQ-kbkviTpm1KwYabEiZJoi9RVZuLZxr7j71kHQ8a4QSglexa1gI4JBtyLFF-WvGOCeh9Sem981FyP5BKmfHRe4Ecznqd4v4RDkmYoOV0ISay-1iuCeZE5enSgaSYN8mh0W5EqS2KP9qNltqP1BNKaWzUoUcgsHdRu0uRSljcb6TcIWAih1xFRHhL8HIsD6OHXZgBww1pbMafXdouJhiZH3niUuxEJio-dIRuLglcbwVyIfP3NFEtGkyXCvRsjKd5aWcOl7-ULti1ZQKS2m8Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/news_hut/66371" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66369">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbJaO9sdIEW_mFr2xQ3F66-EbIFvoWFxmW4FSmRoUnTwy5zz9fEVAPjmqool1lzjlleMR4x-aXwFQRWoaqDO_RL95TOnS_s7HKdliYTRkRZ2VlWLDipiTgIptRDkCTTggxPIrahfxdWBjL7VfDKGb9aSWw0uaz5jna3qknAjQVhPBzTvKGlJmudJPkxaA6T6uMcvk71ngRH86N6-U20dU4G0hvezN8vzNaMv9RrfmbtvKx0o_BESCkyYr1QvA9jeZqOM5h5EJSub1vvSDSMRZLmvshk-kYdF-tyIIxE4yRoRKXdPbA-1MCQqBekntR6xfv5DjXsstfWwqaoYF_q40w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
توییت قالیباف:
تعهد ایران به همکاری برد-برد که بر پایه مشارکت استراتژیک جامع با چین بنا شده، قاطع است.
در جلسه‌ام با اتاق بازرگانی ایران تأکید کردم: ما مصمم هستیم که اجماع استراتژیک خود را تحت GDI به نتایج عملی تبدیل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/news_hut/66369" target="_blank">📅 19:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66368">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53224e4497.mp4?token=dPqGNq36F_QB5mNPKZZmjo-ySbU5Dh-jCOuUcanP3oUOBOHjEjw5gCaYSCAsqJhRZ-kJC_dcd_dN4UghR9peDNGWMTp4gFTYGd8A4Ao5U7CIeQvaU6KsPkuIOmTY3M_0nlE6n4lYmmMV6ApsYgXWc4zmTqNSFAUfeHoJyTl3fC6GLYgBgmot9qOaptsqXUlOjFcAMl3KnvQypRW3_IF3JvPlm9s9HCp2fYYZnpLBMv6kGgPkp_I_UC94YMa6ZF1p5NPcZEm85fG2zw-tvCkRN6mOQR5O6pLjgAW4URj96WVGniI8cWWLsLSa6A317LCVxnJYmXag9S-bUaksIv3CJ6sb2D-7JnHErVQIuixLu2pVpGVcg8L0CYa5wUsj5AzcSA-8NXWeB1QR2B8BwVSuRIfLD5iQIzTBaxNgXCeOz0LmHXNSkvy6IOLiCqmWW4edvFEL5tng-TV1ZvY_euEj4L55tyKbtSWHUhzW3oJHjHV4-N09e34VISvUynDjx_YXnr76KDwPHNKQ1_xE3IUCMq5BA3HVUUkvOEzTPlRsLuUdV_odEMf00f7PW_vAzKWqq_q1rqm9dkH-ccPEDJzy0p1n4cAUfKZBumzYNPJBeJ_19AjaepXULuCNDJKYMtbxQHphdYXLI03UbQnnrJQg_semHru51g87UtxxZ3my-sU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53224e4497.mp4?token=dPqGNq36F_QB5mNPKZZmjo-ySbU5Dh-jCOuUcanP3oUOBOHjEjw5gCaYSCAsqJhRZ-kJC_dcd_dN4UghR9peDNGWMTp4gFTYGd8A4Ao5U7CIeQvaU6KsPkuIOmTY3M_0nlE6n4lYmmMV6ApsYgXWc4zmTqNSFAUfeHoJyTl3fC6GLYgBgmot9qOaptsqXUlOjFcAMl3KnvQypRW3_IF3JvPlm9s9HCp2fYYZnpLBMv6kGgPkp_I_UC94YMa6ZF1p5NPcZEm85fG2zw-tvCkRN6mOQR5O6pLjgAW4URj96WVGniI8cWWLsLSa6A317LCVxnJYmXag9S-bUaksIv3CJ6sb2D-7JnHErVQIuixLu2pVpGVcg8L0CYa5wUsj5AzcSA-8NXWeB1QR2B8BwVSuRIfLD5iQIzTBaxNgXCeOz0LmHXNSkvy6IOLiCqmWW4edvFEL5tng-TV1ZvY_euEj4L55tyKbtSWHUhzW3oJHjHV4-N09e34VISvUynDjx_YXnr76KDwPHNKQ1_xE3IUCMq5BA3HVUUkvOEzTPlRsLuUdV_odEMf00f7PW_vAzKWqq_q1rqm9dkH-ccPEDJzy0p1n4cAUfKZBumzYNPJBeJ_19AjaepXULuCNDJKYMtbxQHphdYXLI03UbQnnrJQg_semHru51g87UtxxZ3my-sU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ درباره ایران:
معامله‌ها شگفت‌انگیزند. من تمام عمرم معامله کرده‌ام. وارد معامله‌هایی شده‌ام که صد درصد قطعی بودند، اما اتفاق نیفتادند. وارد معامله‌هایی شده‌ام که هیچ شانسی برای انجام‌شان نبود، اما انجام شدند و به آسانی انجام شدند.
پس هرگز نمی‌توانی درباره معامله‌ها مطمئن باشی. اما خیلی زود متوجه خواهی شد. فکر می‌کنم انجام خواهد شد.
آنها می‌خواهند امضا کنند  می‌خواهند به زندگی عادی بازگردند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/66368" target="_blank">📅 19:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66367">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ca2e02c1.mp4?token=iO48jucu2FKkK1l7RuL2N6hJ4k7--pW3bbmp2PN9w1XQQLIotF2KL3Ji7YSvJEQCB_6ZcVQHT0H11ARw2GYb_ovWy1rD1DmMSPL8voYoE1AIYylEfg50NoNRgqdtBUHXTnA5BuHeqJo2ve1C5HnO3M7hJ9vSIMF_nKAOb7l0Ullza0B3KN4gDuv60wDcabY7Nm5cLq0lFxYPc45yif0GUw_k8Cdpa3A_einsAFJJb3oBrxqfDfI2uaac8v4CeKZsnQjj8MLxdrjySGFiD9GSGbtehhiHcQrENXqoxxYU8njtvqVzxraV0cc2UTx9xNrShjfRiM5k-Rz14i_kpvpXSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ca2e02c1.mp4?token=iO48jucu2FKkK1l7RuL2N6hJ4k7--pW3bbmp2PN9w1XQQLIotF2KL3Ji7YSvJEQCB_6ZcVQHT0H11ARw2GYb_ovWy1rD1DmMSPL8voYoE1AIYylEfg50NoNRgqdtBUHXTnA5BuHeqJo2ve1C5HnO3M7hJ9vSIMF_nKAOb7l0Ullza0B3KN4gDuv60wDcabY7Nm5cLq0lFxYPc45yif0GUw_k8Cdpa3A_einsAFJJb3oBrxqfDfI2uaac8v4CeKZsnQjj8MLxdrjySGFiD9GSGbtehhiHcQrENXqoxxYU8njtvqVzxraV0cc2UTx9xNrShjfRiM5k-Rz14i_kpvpXSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار: آیا می‌خواهید اروپایی‌ها مین‌روب‌ها را به هرمز بفرستند؟
ترامپ: ما به آن نیاز نداریم، اما اگر بخواهند بفرستند، خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/66367" target="_blank">📅 18:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66366">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06239668e.mp4?token=v3QoGQJG8pEE1jQ7k1sK5p19RpM-3kAbnEBUxZZZHKgNvCwXhn-K_SVY6_ADmhaGj4VxbXbHvZ6T2NKDNpFcHYFLRr00V0uB5mTpYtTD9TT3JzFAq8cRIwtYd9vSublFHo4sPa25ENzPSgMBfG5ogttHeDmNuDKbKir0TIrmWt5W49nJdwOdNzyIJTRYDeyA3RqA4iyw-kMUvIF8ZOvzEdxCUxDsAZ8jJKJ_UxwRIoL67HZVXN_BMa_dOZcCpP5-X20sZTymaOfI2GcGV9604qq1Wl96YGbS8hYxsDyaI7ojTX3-2BVNt8xRD7G3OiyIHSxDMYpVuZiZ5yyJXwn5Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06239668e.mp4?token=v3QoGQJG8pEE1jQ7k1sK5p19RpM-3kAbnEBUxZZZHKgNvCwXhn-K_SVY6_ADmhaGj4VxbXbHvZ6T2NKDNpFcHYFLRr00V0uB5mTpYtTD9TT3JzFAq8cRIwtYd9vSublFHo4sPa25ENzPSgMBfG5ogttHeDmNuDKbKir0TIrmWt5W49nJdwOdNzyIJTRYDeyA3RqA4iyw-kMUvIF8ZOvzEdxCUxDsAZ8jJKJ_UxwRIoL67HZVXN_BMa_dOZcCpP5-X20sZTymaOfI2GcGV9604qq1Wl96YGbS8hYxsDyaI7ojTX3-2BVNt8xRD7G3OiyIHSxDMYpVuZiZ5yyJXwn5Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: آیا می‌خواهید اسرائیل عملیات نظامی خود را متوقف کند؟
ترامپ: من می‌خواهم اسرائیل بتواند از خود دفاع کند، اما همچنین می‌خواهم از تصمیم درست استفاده کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/66366" target="_blank">📅 18:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66365">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oj9SYhI3i7VJ6FVGHUJUDOBsPJ7U7lEBJCku3t3Vkt4kbH7usXLOkRCTr6NnVM2p9sotgVzXjcd8x_5FYZF4EI44dm6VuILlbFgAr96I0YqwevDvTvU-fiSTeDj7aB0e52gd7S9L-jrjLbyzLHSKRoV6DJTn9bC9h5EaixqvmyIggxbx2KSpMA0MIIsizdZQ4MENATLhi6vGjCpe2Ox8FN0JovvpvTsU-fIsXMDrwrB19bImNtbM7Bza5rL5OpcorzlB8xZZMsCEn4zKrOjPkrFR6JBd6CxIDc6PD_TWliP6RrCdZq5jxsE4zUdtaJDgYQcqWoq2Qec5J40VG_L8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دولت سوئیس:
بیش از ۲۰۰۰ سرباز امنیت محل امضای توافق ایران و آمریکا را تأمین خواهند کرد و منطقه پرواز ممنوع برای تضمین امنیت اعمال خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/66365" target="_blank">📅 18:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66364">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6LHxBpe8Bi29WyyqkvlfKaC02hXsQvAXBvxocC2f5VEBM6LaEmoa89on6HvZ7Go6QXJlsvzQqgc8yVvwLG21U66Y0fnQmKAH6HQ_pO7upATplw6eIbQ6Nro7O7vkqqTrEO1wmXhIDuZmfF3oLQelEG-WoV8osOsHMRWNu1YSUyfYutms8P6y2twdpJZaHFf1Eh8JEka6jRJlu1bMqn7FiGiTXDZvOrPkLex--Zfdo8y8yeGw-TbtGEXbqrwWqGnLXvJA7_dE2l_Yrj6BanbeNG5LWvLl8j2syOs45ziNbPscL5aLQ1FgT8SJS53WgsH4ZCyugUUDNKeQdympUBJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزی ۹۰ میلیون سود از جام جهانی
⚽️
برای پولدار شدن تو ایران چنل زیر فالو کنید
⭐
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
1 دقیقه لینک برمیدارم
❌
❌
❌
سریع بپیوندید
🖱
سایت های شرطبندی به دنبال ترورش هستن ، به عشق مردم داره میگادشون
💀
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/66364" target="_blank">📅 18:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66363">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gi5XWlgd6KINmmtQvE2WmTYhEVJ97xlzlkHZ_a5PyqWE6gLJHcv1iDYZUuJzxr4UpaTR26bX3Koav6KmMC8dLvLsqtpmlbuvuljkMg19N4oAJI_tqZGJ-lzgV57W2PhLeDhkRsrSx6vup8-GeC4MTDQJEIPVtziqF9qxKpR9I0mSyqR91Pen8QNQA-ladZBhezczAejxSCE-heVJSH-jKhfyRWhQFNPeXP5O9eS99_3Q5P_EylL667X8Ap_Qy0ZT3y8PqYdPBE4rftdsQ9b3XDm2ChkCqqLrNhDp8fQIASxOymccCqr-Euvf1IN59ZE_2XlxQu09AqOihM04eSqdsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ در تروث سوشال:
۴۵ دقیقه دیگر از فرانسه یک کنفرانس مطبوعاتی خواهم داشت. سپس برای شام با رهبران فرانسه و دیگر رهبران اروپایی به ورسای می‌روم و امشب به خانه برمی‌گردم! این سفر موفقیت بزرگی بود، اما چیزی که بیشتر مردم می‌خواستند در مورد آن صحبت کنند این واقعیت بود که ایران سلاح هسته‌ای نخواهد داشت و تنگه هرمز فوراً باز خواهد شد! اعداد و ارقام بزرگی در همه دسته‌بندی‌ها برای اقتصاد ایالات متحده با تعداد افراد شاغل بیشتر از هر زمان دیگری در گذشته. بیش از ۱۹.۱ تریلیون دلار در ایالات متحده سرمایه‌گذاری شده است، کارخانه‌ها و هر چیز دیگری در حال وقوع است، اما مهمتر از همه، اعداد و ارقام اخیر بازار سهام به دلیل توافق بسیار بالا هستند و به همین ترتیب، قیمت نفت در حال سقوط است!
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/66363" target="_blank">📅 18:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66362">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a882497b26.mp4?token=jTi5Dcg_KV376eYzw-OaTM8pziN_DDBspo_PHBJCFFYzQadMekJkE2uE3ONTX8-y2qrjMukWlelF1LBb4IyKL4ZwGG5f2hTnbB-QMYqvxtW6eqdzolarJY3SlgawTYPGagVDwK_RW-Kmt3VT3E4nms4-D04V1JYT9X-nBqPkJ_UGym6CnILo2NsTBavZC56ZvmCr-uSkMsGFXyEpPm17j3TMpSsFE2EuxwDHQgFgk00t6QCcuMiV22DawKkgvSQuBi5yXb9-Vts6Eq_56MKo5FGFoVXIyxGmnTrS_OYpVGESai6H1dC7moLjCVqyC-x319LGgkrJpY6RAYeoTihrWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a882497b26.mp4?token=jTi5Dcg_KV376eYzw-OaTM8pziN_DDBspo_PHBJCFFYzQadMekJkE2uE3ONTX8-y2qrjMukWlelF1LBb4IyKL4ZwGG5f2hTnbB-QMYqvxtW6eqdzolarJY3SlgawTYPGagVDwK_RW-Kmt3VT3E4nms4-D04V1JYT9X-nBqPkJ_UGym6CnILo2NsTBavZC56ZvmCr-uSkMsGFXyEpPm17j3TMpSsFE2EuxwDHQgFgk00t6QCcuMiV22DawKkgvSQuBi5yXb9-Vts6Eq_56MKo5FGFoVXIyxGmnTrS_OYpVGESai6H1dC7moLjCVqyC-x319LGgkrJpY6RAYeoTihrWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نه از دوست شانس آوردیم نه از دوژمن
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/66362" target="_blank">📅 17:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66361">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7f967b0a.mp4?token=Hsx3YVBtI1ZSXmezG9MRu7KyEzx1j171epQcd6BxtH9fyN_rJs6p1YQXTbSRn7wHUR0ZzK73zceTZd1HtcoOPaj6zNkL9H7hG4LlNh5HWvmhVGt3SDyYGDHuZthqrvD1q8vQQSGX6wRTLPU9lWr3WPeIcPGqK5nnVBHaIBJZ0BNN1i9-G0dF2XyadhnaQ2WlkkxxCbg6MFfnrxWtQTD93zSL0EKYsPuz00L1oUKVpipCF0MjaTs5kobe71qonUOls2-RabxAcpV0knNooaXQvsdbbkAy3tY8ZWAfPZlu3hFJOg0410KBsvBdWvsc18ls1pR794Uz7AOYTwmSK8_AUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7f967b0a.mp4?token=Hsx3YVBtI1ZSXmezG9MRu7KyEzx1j171epQcd6BxtH9fyN_rJs6p1YQXTbSRn7wHUR0ZzK73zceTZd1HtcoOPaj6zNkL9H7hG4LlNh5HWvmhVGt3SDyYGDHuZthqrvD1q8vQQSGX6wRTLPU9lWr3WPeIcPGqK5nnVBHaIBJZ0BNN1i9-G0dF2XyadhnaQ2WlkkxxCbg6MFfnrxWtQTD93zSL0EKYsPuz00L1oUKVpipCF0MjaTs5kobe71qonUOls2-RabxAcpV0knNooaXQvsdbbkAy3tY8ZWAfPZlu3hFJOg0410KBsvBdWvsc18ls1pR794Uz7AOYTwmSK8_AUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده رضا پهلوی: «صرف‌نظر از نتیجه این به اصطلاح مذاکرات، این توافق پایدار نخواهد بود»
شاهزاده با رد مشروعیت هرگونه توافقی که بقای رژیم تروریستی جمهوری اسلامی را تضمین کند، تأکید کردند: «صرف نظر از نتیجه این به اصطلاح مذاکرات، این توافق پایدار نخواهد بود... بقایای این رژیم هرگز در نظر مردم ایران قابل قبول یا مشروع نخواهند بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/66361" target="_blank">📅 17:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66359">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e17877e6a5.mp4?token=K-qYkvRhgsjMfPVtJDGMnUfp_VMLWZnVzWEeQUh-cBndx7kahsQXsYXMyaEtlwOrGfZK59TkvXVL9viomOcqCeXJCk7sHAdNDHoOmnH10JCVju_E6jxoAN5FWRZJ_dXpv5g5c5alNx0IqEnE24PXSN88qq0Aqt6BpSSzqHvi1-dXfrEmzyOXpJV7gXwBqrkb80SjcAeez0jH_k_ytwTVTjUbfhh1h_UY56JV2eF2HKlxNkXTWHZ9t7T6jEbZY65IcUChgW4KdjUPO573RTYQzE5lhRUeq2QW9jRf0XdVs5ThNo28D76S5cMBuRXf1r7ZUlyHSLXIew_MxWC9kafEaFMS3jExAOHMJhsvvXY3tM2sOMA26MTfnDSwYr9J5_saFVgA27NjDHXVl88kMCeH9ZUve9pwiPIZB9H34fnW5HkEPRUA9vxYxD_LC9flt80s-4D2v_8ACD2TuiWtjzc_YCi3SBt9BWAxTQI9mphjZJ3iRfvo4zdU2c5iOTlv-8XztecKvt4xXoZo1P2svlIAJyHOgA5xJTX_gr9_5zbgcF01yUIo6TlMvVpJZ4NvjFO4O8hdrzB1woWgZo4ENODGurQr4iHl4Pbt147qWWcfJ5Da4a8I5oMfCz2b9b6949DH4oHml9mgDBl7SLUt7HS0XcJllPAvs4ndfe6bde1lzaY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e17877e6a5.mp4?token=K-qYkvRhgsjMfPVtJDGMnUfp_VMLWZnVzWEeQUh-cBndx7kahsQXsYXMyaEtlwOrGfZK59TkvXVL9viomOcqCeXJCk7sHAdNDHoOmnH10JCVju_E6jxoAN5FWRZJ_dXpv5g5c5alNx0IqEnE24PXSN88qq0Aqt6BpSSzqHvi1-dXfrEmzyOXpJV7gXwBqrkb80SjcAeez0jH_k_ytwTVTjUbfhh1h_UY56JV2eF2HKlxNkXTWHZ9t7T6jEbZY65IcUChgW4KdjUPO573RTYQzE5lhRUeq2QW9jRf0XdVs5ThNo28D76S5cMBuRXf1r7ZUlyHSLXIew_MxWC9kafEaFMS3jExAOHMJhsvvXY3tM2sOMA26MTfnDSwYr9J5_saFVgA27NjDHXVl88kMCeH9ZUve9pwiPIZB9H34fnW5HkEPRUA9vxYxD_LC9flt80s-4D2v_8ACD2TuiWtjzc_YCi3SBt9BWAxTQI9mphjZJ3iRfvo4zdU2c5iOTlv-8XztecKvt4xXoZo1P2svlIAJyHOgA5xJTX_gr9_5zbgcF01yUIo6TlMvVpJZ4NvjFO4O8hdrzB1woWgZo4ENODGurQr4iHl4Pbt147qWWcfJ5Da4a8I5oMfCz2b9b6949DH4oHml9mgDBl7SLUt7HS0XcJllPAvs4ndfe6bde1lzaY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای وایرال شده از ایونت های شبانه تهران
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66359" target="_blank">📅 16:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66357">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sl3uSPtskXzNgUsIvsQjgC-J7KgnGN83yiVHewGMfJ6LwPuIJDgo6q5A-vNalccuhMMmXEhHd4SNcb_TSAFeZ83LsCVA4Ff4f__lYfTNTdcNOb9keG5G_L1lezPLXN1FdXNB5Zb8gR1q5su1GrE7Nm8hv5MS2HWD6IV9zt7jg5BBpHEPBI8JercZDV6Nwli2beTIXG4aA4twrYHtlQV0PfVfUQSHHSCwnVu33f36oUj9J1mwWbNks8sWSKo20UjXeMlux7qqTvXY0H_GAGOZJwU9U_m2KEkJRlvOpH0de8xr8wWQPCgKJAU8isJI8P7KL_Tho9G_ThxeltUrOeJTkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/145629d21c.mp4?token=Yvud_BAQjTTMUiiFI_emQbzFd-QjDYSMrLGwiokDnxRpFhKJ5GwjLk7AEm6TTm3JwswcQTv5VJgxWQYS6MxI0dWSM5tp_rWrscLsxxi89OdXagc83_SFalyIQkM3ZNPZ03T02xfWmfy_x6gWb86DrbRAs-SAyuIr-SYOPxrKUoZkfOZ4hQT_cbtdAmI3ci0CdC65YIKyEy-SdOtUPWW9voRac0x7QpyHfFUz2HRiVqKi5_-VRkHOCbTida4C753ZCWUg7BdAwp50Gk-IOUwba3jDqeTuU30GHFMGZAvUfwKSrGjmdbgPSqTlFfJIdAmGDWhEuvRK74FJeYFOZaHGoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/145629d21c.mp4?token=Yvud_BAQjTTMUiiFI_emQbzFd-QjDYSMrLGwiokDnxRpFhKJ5GwjLk7AEm6TTm3JwswcQTv5VJgxWQYS6MxI0dWSM5tp_rWrscLsxxi89OdXagc83_SFalyIQkM3ZNPZ03T02xfWmfy_x6gWb86DrbRAs-SAyuIr-SYOPxrKUoZkfOZ4hQT_cbtdAmI3ci0CdC65YIKyEy-SdOtUPWW9voRac0x7QpyHfFUz2HRiVqKi5_-VRkHOCbTida4C753ZCWUg7BdAwp50Gk-IOUwba3jDqeTuU30GHFMGZAvUfwKSrGjmdbgPSqTlFfJIdAmGDWhEuvRK74FJeYFOZaHGoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جنگنده‌های اسرائیلی مناطقی در نزدیکی کفر تبنیت در جنوب لبنان را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66357" target="_blank">📅 15:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66356">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2f9733be.mp4?token=nA_pUY5seoJ7GHFJFcjpUjGgd16hqiKcPZMMU_AbDSPEL1eYL5SR2Lc3yHKXcwgJ1O4zQEHhx0GfYPPFw8ygf4aLeDAXCUS2x4qOy8ZKL26njVn4pR_Fqn03S9Mn989tXirWaSprZSrXg_TWp4gTLS3aGVHcEnIQ0wB79A-ejLBDQYykr-SrlHrkGPPpV-vdegI7UPaCNwAi83IudeYRfesIL9zjdDO8ZGhyU_kmTGpjqliieG3funN5iDs2lX8sTy2urUcueTkh7tWkXR0NaHsg1Arw-I1cTVB8o61oc_t4FBEHBSWZRF4MIWh7iwK1lN11SyYOCmVDfZ0n6Yitcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2f9733be.mp4?token=nA_pUY5seoJ7GHFJFcjpUjGgd16hqiKcPZMMU_AbDSPEL1eYL5SR2Lc3yHKXcwgJ1O4zQEHhx0GfYPPFw8ygf4aLeDAXCUS2x4qOy8ZKL26njVn4pR_Fqn03S9Mn989tXirWaSprZSrXg_TWp4gTLS3aGVHcEnIQ0wB79A-ejLBDQYykr-SrlHrkGPPpV-vdegI7UPaCNwAi83IudeYRfesIL9zjdDO8ZGhyU_kmTGpjqliieG3funN5iDs2lX8sTy2urUcueTkh7tWkXR0NaHsg1Arw-I1cTVB8o61oc_t4FBEHBSWZRF4MIWh7iwK1lN11SyYOCmVDfZ0n6Yitcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
فراموش نکنید، هیچ‌کس تا این حد در مورد ایران سخت‌گیر نبوده است.
این کار باید توسط کلینتون و باراک حسین اوباما انجام می‌شد. این کار باید توسط بایدن، بوش و بسیاری دیگر از افراد انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66356" target="_blank">📅 15:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66355">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048f0eb68f.mp4?token=Rhmu5f7-tCnpzu-izB787TijPfxYyoinkdB50ioRG6gEPE7vrOgYHrYBpARg2S6W8xrmg3UwpVi9svvj5SCbFynLlOBwYxt7UppjXK_HCe5PwlAdKd7wmw_7LvW-Mc4TvjtVnMw7RupT4LktbObWO5Aj_jwI0Bl6yQJM5fKpzTshT2C9EEv37TnxMTIwP80Zm-SNvGA_U4Bu3DZC49kfJqy3aHWpptqiX4cnff-KQ3_ttt1MkHFfJASmut0G2LFvMY_2Tdord0e8WgfxNxpHleS58W7Lv59ZsyDQC5cUbQjV6d1_zln3mK6Y-W-P8LbhyUrhO7i_aXYveEb_OFT2jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048f0eb68f.mp4?token=Rhmu5f7-tCnpzu-izB787TijPfxYyoinkdB50ioRG6gEPE7vrOgYHrYBpARg2S6W8xrmg3UwpVi9svvj5SCbFynLlOBwYxt7UppjXK_HCe5PwlAdKd7wmw_7LvW-Mc4TvjtVnMw7RupT4LktbObWO5Aj_jwI0Bl6yQJM5fKpzTshT2C9EEv37TnxMTIwP80Zm-SNvGA_U4Bu3DZC49kfJqy3aHWpptqiX4cnff-KQ3_ttt1MkHFfJASmut0G2LFvMY_2Tdord0e8WgfxNxpHleS58W7Lv59ZsyDQC5cUbQjV6d1_zln3mK6Y-W-P8LbhyUrhO7i_aXYveEb_OFT2jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: نیروی دریایی آمریکا هر شب بین ۱۵ تا ۲۵ کشتی را متوقف می‌کرد
دلیل پایین ماندن قیمت نفت این است که ما هر شب کشتی‌هایی را که شما حتی از آن‌ها خبر نداشتید، خارج میکردیم. دو روز پیش، سه روز پیش و حتی یک ماه پیش، ما ۲۲ کشتی را خارج کردیم. به طور متوسط هر شب بین ۱۵ تا ۲۵ کشتی داشتیم و هیچ‌کس از این موضوع خبر نداشت. نیروی دریایی ما کار بزرگی انجام داد و به همین دلیل قیمت نفت به ۳۰۰ دلار در هر بشکه نرسید. قیمت‌ها به ۱۲۵ تا ۱۵۰ دلار رسید و اکنون حدود ۷۲ تا ۷۳ دلار است و حتی شنیده‌ام از این هم پایین‌تر آمده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66355" target="_blank">📅 14:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66354">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7384906c.mp4?token=CMLyp7-i9p8NUczICg6FC5RZk183dVsF5zcgxeoWDUsbeVoyKIjyWZH_Rq0X82tTsJjU2ufjakbsrgkpta5NaSfjdZoHXvOm_weeF2jdG02WSOpvgE-LQ_-nicRP8qbjjN895qZ3WlNFug1g2DpT5Rmk85kGuyyDVltyud2ihFKlPtiadzf1qw9HZccCsaU7aHioC9wjLeNZoHMqBqd-bDkvTygG0wAVi6r4VodfkEoPM5cOwL9GMNGOmzJ8fFD20IKaVMP7uRdlXAM-7dAFNUHwi_p25dBHMuQl0z9toUyqIHtJS0cg3gqhA3VqmbrnfDeqiJgGQ9Th5b8d0IUBbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7384906c.mp4?token=CMLyp7-i9p8NUczICg6FC5RZk183dVsF5zcgxeoWDUsbeVoyKIjyWZH_Rq0X82tTsJjU2ufjakbsrgkpta5NaSfjdZoHXvOm_weeF2jdG02WSOpvgE-LQ_-nicRP8qbjjN895qZ3WlNFug1g2DpT5Rmk85kGuyyDVltyud2ihFKlPtiadzf1qw9HZccCsaU7aHioC9wjLeNZoHMqBqd-bDkvTygG0wAVi6r4VodfkEoPM5cOwL9GMNGOmzJ8fFD20IKaVMP7uRdlXAM-7dAFNUHwi_p25dBHMuQl0z9toUyqIHtJS0cg3gqhA3VqmbrnfDeqiJgGQ9Th5b8d0IUBbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: «می‌دانید ایرانی‌ها چه کار کردند؟ آن‌ها به اوباما خندیدند و به او گفتند احمقِ مادرجنده.»
پرزیدنت ترامپ با اشاره به نحوه برخورد رژیم جمهوری اسلامی با دولت باراک اوباما، گفت که مقامات این رژیم به اوباما خندیدند و او را «احمقِ مادرجنده» خطاب کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66354" target="_blank">📅 14:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66353">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bba81d7fe.mp4?token=e2YCkTGrcGXkbH_6SA8K4x_uP3glLRVzoSqH78JKHbIqJDKYoToPthakiW6gdpXsko65UhR88JnBbO6lLOWf5T3Cd9DJEpyqa1qSsantY6szZfRDOso_uOtcJVLMCz02nPFltARhfy4cYOmw7dz_clOYGSOGtOR13XMCbmOPUwGEM83irMhRs1FNfSY9xOQMoCo2sok9JEl5N2WGDS8WiUFJ4dbW6zCnDEaOoUHEeDgKJbDJ9QC0ESP3_ZADAUbycfr_w_aeR61vJSOIlCKrOxI902m-v7ZazUFnisGM5CGghj3yFXRR0AeL6KG1biIV_H_lhsz88E1nY17Khp3zsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bba81d7fe.mp4?token=e2YCkTGrcGXkbH_6SA8K4x_uP3glLRVzoSqH78JKHbIqJDKYoToPthakiW6gdpXsko65UhR88JnBbO6lLOWf5T3Cd9DJEpyqa1qSsantY6szZfRDOso_uOtcJVLMCz02nPFltARhfy4cYOmw7dz_clOYGSOGtOR13XMCbmOPUwGEM83irMhRs1FNfSY9xOQMoCo2sok9JEl5N2WGDS8WiUFJ4dbW6zCnDEaOoUHEeDgKJbDJ9QC0ESP3_ZADAUbycfr_w_aeR61vJSOIlCKrOxI902m-v7ZazUFnisGM5CGghj3yFXRR0AeL6KG1biIV_H_lhsz88E1nY17Khp3zsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
ما مردی به نام سلیمانی را از بین بردیم. فکر می‌کنید اگر او زنده بود، این اتفاق می‌افتاد؟او یک نابغه شیطانی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66353" target="_blank">📅 14:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66352">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff72e5160c.mp4?token=X51tyiab_TZM2rs1wL5dYeTE4oaBg8Zhq4oeClmWzUJToIVMRgp7T4l2_EEreDXhv_OTAWgD-QfFKmasbYHaaI2VyGS10a2_Qgw1vYunqMrbyLdzf30NK91A8TcxgzSNnY8P6_9SHqiBV46U2JIbyTu7Q1ArncMbNDiH5gMIIjfj_a22ThG7I1ZSg2MpS10biYF1o37mfgNNrdNBUqJP4kCd4YHf73A-9t3LiudN86tL1jDUenBRNig0d6s8rv0jb7FyIOi1z16qL54GrJnycz_NtiS1TrzcspDZ5e6AuzDQLfd_lSRfB0wbqLa-FKhXxEwAmTFZSXkvJ_-fX7Yfxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff72e5160c.mp4?token=X51tyiab_TZM2rs1wL5dYeTE4oaBg8Zhq4oeClmWzUJToIVMRgp7T4l2_EEreDXhv_OTAWgD-QfFKmasbYHaaI2VyGS10a2_Qgw1vYunqMrbyLdzf30NK91A8TcxgzSNnY8P6_9SHqiBV46U2JIbyTu7Q1ArncMbNDiH5gMIIjfj_a22ThG7I1ZSg2MpS10biYF1o37mfgNNrdNBUqJP4kCd4YHf73A-9t3LiudN86tL1jDUenBRNig0d6s8rv0jb7FyIOi1z16qL54GrJnycz_NtiS1TrzcspDZ5e6AuzDQLfd_lSRfB0wbqLa-FKhXxEwAmTFZSXkvJ_-fX7Yfxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: بازار از توافق با رژیم جمهوری اسلامی خوشحال است
«چه کسی واقعاً خوشحال است؟ بازار... بازار در حال نوسان است و قیمت نفت سقوط کرده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66352" target="_blank">📅 14:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66351">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a231223e.mp4?token=b0aASqVQqLnoZrYqsZVF0a4VDIGhIQh3aIZUG2wJMbTbwl20PJtnpCWp3cMBjN54FFmEjOjupWmg_M6IPByMmwp9_6BtzgLY51dBzl9DhBaVMgZTOkdCahDJ0g2f6Ch1H-R2vtMVoUMeMuS9CtVmOErZbhZylc8WWUD8fspBlnL3ipdyhmcmL41ys-xW02m89Ljl_-TrZeojDHbcx3NV39FjQd4I3cI-XtAT-dB5xbiT_RqWNmLsgGTrkPT-deDG2PMEfcfkBa0kRVLqCdrNuREVMYLNr_eQ33fj4qFUUiL5Lah_BFi2QU0fNDzG-4mvBesJDQf5haZAbA8KqXm7Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a231223e.mp4?token=b0aASqVQqLnoZrYqsZVF0a4VDIGhIQh3aIZUG2wJMbTbwl20PJtnpCWp3cMBjN54FFmEjOjupWmg_M6IPByMmwp9_6BtzgLY51dBzl9DhBaVMgZTOkdCahDJ0g2f6Ch1H-R2vtMVoUMeMuS9CtVmOErZbhZylc8WWUD8fspBlnL3ipdyhmcmL41ys-xW02m89Ljl_-TrZeojDHbcx3NV39FjQd4I3cI-XtAT-dB5xbiT_RqWNmLsgGTrkPT-deDG2PMEfcfkBa0kRVLqCdrNuREVMYLNr_eQ33fj4qFUUiL5Lah_BFi2QU0fNDzG-4mvBesJDQf5haZAbA8KqXm7Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد توافق ایران:متن نهایی نیست؛ این یک یادداشت تفاهم است.
اگر من آن را دوست نداشته باشم، ما به پرتاب بمب روی سرشان برمی‌گردیم.اگر آنها رفتار مناسبی نداشته باشند، ما دوباره به پرتاب بمب برمی‌گردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66351" target="_blank">📅 14:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66350">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7653e74d56.mp4?token=Yg2382s4D_ieH7UGaHFtKN4AbhuGbzLK8rPE-1FBMd6VKY8pcXuHws87sN_EhsTvL_Hyr2aLCnLMXWCBd8PRhbIbFiwOgTJuV89FKnUGJu39Gm-6s1tDJHhUhG1TgyWGEa4BbP_ChmzIkrJYTKggLPcbeFrWw5YZu62fV2fLuj0PibKD5BDj_VHVmqu8XkvS6oqr1_RJWkK6nwk2ATwXS5eE-i8pi2KACoN6ZlrKk9nGsJFBzeYeN5PfP4Z4DhEZbXlchYVuwwNVeBPa1j2YUMB_k0nxTE7gcrsCl9EhU0piKW9Xme6wVW0gy9qL5z8iZVBKe4Ae2nusExlThbsZPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7653e74d56.mp4?token=Yg2382s4D_ieH7UGaHFtKN4AbhuGbzLK8rPE-1FBMd6VKY8pcXuHws87sN_EhsTvL_Hyr2aLCnLMXWCBd8PRhbIbFiwOgTJuV89FKnUGJu39Gm-6s1tDJHhUhG1TgyWGEa4BbP_ChmzIkrJYTKggLPcbeFrWw5YZu62fV2fLuj0PibKD5BDj_VHVmqu8XkvS6oqr1_RJWkK6nwk2ATwXS5eE-i8pi2KACoN6ZlrKk9nGsJFBzeYeN5PfP4Z4DhEZbXlchYVuwwNVeBPa1j2YUMB_k0nxTE7gcrsCl9EhU0piKW9Xme6wVW0gy9qL5z8iZVBKe4Ae2nusExlThbsZPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد توافق ایران:
هیچ‌کس نمی‌داند این چیست، اما توافق بسیار قوی‌ای است.
به نظر می‌رسد اکثر مردم بسیار خوشحال هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66350" target="_blank">📅 14:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66349">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8de3b6155.mp4?token=uOYfCd4QH66qLIfW3d12ezrjtJG8osdsEqSPIjhwweXDkn4czDNgcobmxRxFow9o0hc6FCVVu4WWByQ_XFHyBtA4-PlU0vED1txa1yVIu9EWMCymMHvt23wOEPk5bbVqtdx7xWyxZyfKKlqGltlSHOnRTiiXno_wBDVkHfkT9AxD5hALtMyyKo-K1OVwJM1H7_bQU7rkzC8sO8tOjazgctwQkwVzkQT3YdCwT4Cv-iW-cb6mC15QbST23h4hTtqP1VJkkET_DUlLvW8RbfC7WD41ZnqFVzCn02CAwPSY9kmMOYLVl4RFHUmeTvcDWk2t2cAH5QiVJaqI0WPINJ9rbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8de3b6155.mp4?token=uOYfCd4QH66qLIfW3d12ezrjtJG8osdsEqSPIjhwweXDkn4czDNgcobmxRxFow9o0hc6FCVVu4WWByQ_XFHyBtA4-PlU0vED1txa1yVIu9EWMCymMHvt23wOEPk5bbVqtdx7xWyxZyfKKlqGltlSHOnRTiiXno_wBDVkHfkT9AxD5hALtMyyKo-K1OVwJM1H7_bQU7rkzC8sO8tOjazgctwQkwVzkQT3YdCwT4Cv-iW-cb6mC15QbST23h4hTtqP1VJkkET_DUlLvW8RbfC7WD41ZnqFVzCn02CAwPSY9kmMOYLVl4RFHUmeTvcDWk2t2cAH5QiVJaqI0WPINJ9rbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یسرائیل کاتز: هر کسی علیه اسرائیل اقدام کند، بهای سنگینی خواهد پرداخت
🔴
وزیر جنگ اسرائیل هشدار داد: «هر کسی که علیه دولت اسرائیل انگشت و دست بلند کند، چه در غزه، چه در لبنان، چه در سوریه و یا هر نقطه دیگری، می‌داند که باید بهای آن را بپردازد. اول از همه، آنها زمین خود را از دست می‌دهند و خانه‌های خود را از دست می‌دهند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66349" target="_blank">📅 14:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66348">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/831548d977.mp4?token=GqRAw5eUyNdCUL1LHWS3gSk4XFS2LWpiHykAES30MQ8Vqo7YAOfv0KmuwKbRDYqQfwB603MAFLhTG8OAj1td5FBA1SpxKVigJUxqb_4OZU9YVxq0f-7-YRaeja-IugrAnedchFgRAZ06euNWyJIjF-enghsLo2TRGh1K0YGgQ8DOVMotEGKt2N3gs2ucM9XQcqG8kpV138iqvpHYsL7Zd0ox2M7XmkOBVGzSRHRGznndcYFIf8RhGaR9SczlXwuUR4cis7GRMAFthEvD5rlhyM3LVv7TbqTqXHMJLR5mUJHICP6aT1JbSoUOv57Jbz-IX2g-DEyJqzN8jR2aa94JEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/831548d977.mp4?token=GqRAw5eUyNdCUL1LHWS3gSk4XFS2LWpiHykAES30MQ8Vqo7YAOfv0KmuwKbRDYqQfwB603MAFLhTG8OAj1td5FBA1SpxKVigJUxqb_4OZU9YVxq0f-7-YRaeja-IugrAnedchFgRAZ06euNWyJIjF-enghsLo2TRGh1K0YGgQ8DOVMotEGKt2N3gs2ucM9XQcqG8kpV138iqvpHYsL7Zd0ox2M7XmkOBVGzSRHRGznndcYFIf8RhGaR9SczlXwuUR4cis7GRMAFthEvD5rlhyM3LVv7TbqTqXHMJLR5mUJHICP6aT1JbSoUOv57Jbz-IX2g-DEyJqzN8jR2aa94JEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس و دیسبک بازی مسعود با خودش
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66348" target="_blank">📅 13:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66347">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51823a43bc.mp4?token=T2tnRbtGnb9wAS4asFqaNQw9fOiUPA6ppGB8F5q0oYuElL5jM069sZ1jqY7bTN1vw3ho5M1ss3DwxGUOHD8567O4inj9AB5GOp7gKFSwp9zVjPuqtkHzWlZ9OL9QDno06UYtwxA0_DttCWTzldbHrqwflup-GEP9DFLWwXfXj95pMhQgZ6TyAgf2kKl7NEdl0bE23KxP6Y5ik5kAE-O54tvvMq5DK71sdt36mz8gn6MBX-w5DgOXfEBou32Fv-rctyehg7nVfAg6k-tdsF5V9nNHcD6z_66mNTbOXAxMyNWIglhHNMm-puDqz6m4yPX2fmjoO64Br1wY8IryJOnmbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51823a43bc.mp4?token=T2tnRbtGnb9wAS4asFqaNQw9fOiUPA6ppGB8F5q0oYuElL5jM069sZ1jqY7bTN1vw3ho5M1ss3DwxGUOHD8567O4inj9AB5GOp7gKFSwp9zVjPuqtkHzWlZ9OL9QDno06UYtwxA0_DttCWTzldbHrqwflup-GEP9DFLWwXfXj95pMhQgZ6TyAgf2kKl7NEdl0bE23KxP6Y5ik5kAE-O54tvvMq5DK71sdt36mz8gn6MBX-w5DgOXfEBou32Fv-rctyehg7nVfAg6k-tdsF5V9nNHcD6z_66mNTbOXAxMyNWIglhHNMm-puDqz6m4yPX2fmjoO64Br1wY8IryJOnmbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاوره اخذ مدارک دانشگاه آزاد
واحدهای معتبر تهران
کارشناسی، کارشناسی ارشد، دکترا
با استعلام
💥
(
بدون پیش پرداخت
)
💥
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
Telegram :
👇
👇
👇
👇
@irantahsilat_iau
Instagram :
👇
👇
👇
👇
Https://instagram.com/uni.irantahsilat
جهت ارتباط با ادمین
👇
:
@madrakuni</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/66347" target="_blank">📅 13:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66346">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1725e10790.mp4?token=mbiFLrvKoGNrXzpCnZZv7sQnu2GLOhIqQrNxbqciuOm6efV1FT5YkclzPv7_OTzTf-UPkcrkfNnBV1NPze0sRqd96kFBcSzCAxcH05xp_0Z25BDNk7UkwNYC1uepgxn11P9D3C06t8CqZ8VOtDQqe6S05kxSJXgoId794E6CPJ8vjFuYA9tAaQ5DA1fMOXN08dGqJGzL_3sVQcnkUrNPd4oSY-KcapiCbDG880n5Mbq_jTdkCkkD3sSGJmKDsiKkAEsYe2t71Iypc-FWsSm2Ae8dKRnBWiHBAT5veCKdVCz8We9zaLEMH1x_Sr-6AzKHmhBrbcOCG8C114kNgT9AjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1725e10790.mp4?token=mbiFLrvKoGNrXzpCnZZv7sQnu2GLOhIqQrNxbqciuOm6efV1FT5YkclzPv7_OTzTf-UPkcrkfNnBV1NPze0sRqd96kFBcSzCAxcH05xp_0Z25BDNk7UkwNYC1uepgxn11P9D3C06t8CqZ8VOtDQqe6S05kxSJXgoId794E6CPJ8vjFuYA9tAaQ5DA1fMOXN08dGqJGzL_3sVQcnkUrNPd4oSY-KcapiCbDG880n5Mbq_jTdkCkkD3sSGJmKDsiKkAEsYe2t71Iypc-FWsSm2Ae8dKRnBWiHBAT5veCKdVCz8We9zaLEMH1x_Sr-6AzKHmhBrbcOCG8C114kNgT9AjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
بالگرد کاموف ۵۲ روسیه برای رهگیری پهپاد انتحاری اوکراین بر فراز مسکو به پرواز درآمد:
در جریان موج حملات پهپادی صبح امروز اوکراین به سمت مسکو، یک بالگرد تهاجمی کاموف ۵۲ روسیه تلاش کرد یک پهپاد انتحاری اوکراینی را در آسمان رهگیری و منهدم کند. این تصاویر بار دیگر نشان می‌دهد که جنگ پهپادها تا قلب پایتخت روسیه کشیده شده و مسکو بیش از گذشته برای مقابله با تهدیدهای هوایی به ابزارهای غیرمتعارف و واحدهای هوانیروز متکی شده است. حملات پهپادی اوکراین در ماه‌های اخیر به زیرساخت‌ها و مناطق اطراف مسکو شدت گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66346" target="_blank">📅 13:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66345">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyEOvORZ7kzjBWTeMHCl8U402kBpR5pfyj0CUCphDkIT1Xdtn-90uEOyxibYkUNW45tb2M1qxZSs03yu8A5OLHSwMtTIV078-ZB8Hxii4U4DfyaH_GvJWntoysiyJO0KIgW78qxvo0JVDts9H7-bqJ3WPzxxVYa15P0HuNpfnBqYu9waSQ8zW_R7QHP5DeY09cxlwDyDhiqTx_4RktbgPeoomRE5wB2VgD8ZGd57hn7HfjDq59_2LyuAQvvSKHQfn0V8r80u6nYqCKRBmJmxJq5ARNnoy53R1OtiebGBa4MIPpCq6yeepWBdJj-FkcImZN3iFATcLPZ7L9IifzePRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت مارکو روبیو بعد از شنیدن خبر توافق
😔
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66345" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66344">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66344" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66344" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66343">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puEhE-MVSWiPLAsoi7a6Qmru5jUrIJXQmJ4FjucSiIhS3pMxKlip0qQ6MUkmVN834S5aklnqmznjkF2V9rqUklh78TNJ8gF4VM5Fz2nvKuTNHyrcwW4GVai7sWnKVeQfK00GAKno4fAquJfoYBPL0HESnYWveBcyOvih71ly4fYG9WhTzKQezJjHwbtW6eZ4DDIzuEfZy41ahrUAblvXciPg_aTgnqZFlva7wNmBKENtwkV6nY-iDWer0hMbJ5qXVh7l29DQSPkYkaF4JFsQvcVYoGzCjBTEaSsjlBEqcj0lejOk1OYYIeOK4jYW3C79bYT16mUE5XrZdRRaJf_QRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66343" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66342">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5hoF35iOmMKQBOWN7QLzd_220VOVCJp0aT155lp9Ey-bYjMX_vCL1yUQS0TePAEP24CUJLApFQBjfNW1q1lpxNc34bB7O8mDitTasY5jmWZmYN4BH5JQAg93ZrCxneciuNLCeikPJecB4JRgbg2DAiUN0GE3_-n0IftKeFsjEYpazcXJPWwmT8k48vUAe1qc30aFl70RreP1mjxKsyEsHmk8JFCQCD0aJcdNO9KVtRbriH09FONf8Wi0CpXo6MWoIwAsVvdJt61AFeretLUuV3mlw69YAUXzJ2npmHp3lLf0nrN7JpThpss8vIn4PIHdBp91m8nH4yBrfGyk7q9qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
شبکه ان‌بی‌سی به نقل از یک مقام آمریکایی:
رژیم تروریستی جمهوری اسلامی با وجود اعلام یادداشت تفاهم با ایالات متحده، همچنان تعداد زیادی پهپاد به سمت شناورهای تجاری در تنگه هرمز پرتاب کرده است. بر اساس این گزارش، سپاه پاسداران از زمان امضای الکترونیکی این تفاهم‌نامه در روز یکشنبه، هر شب اقدام به پرتاب پهپاد کرده اما نیروهای آمریکایی موفق شده‌اند آن‌ها را پیش از تبدیل شدن به تهدیدی برای کشتی‌های تجاری، شناورهای نظامی و خدمه حاضر در منطقه رهگیری کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66342" target="_blank">📅 12:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66341">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qf0t6ZcOL7MI_-14AIoFDuwFRKti1TJdBGRB0NQe_dsux9h67nVvED004Vss--xXneGxvpgygIoGuu2Yd9g7acZ9q3Vqb1D2_wSoqUi4YUptpnzxF8fTMU41jj7m4ODVmXjsyKZ3eKoz7grir0_cj8NhTM8TEwKJPC6h_dRVrkTKvpg9Fu95d9nvg4qeTbJGatSooCsHH-JrJvQrK12cH8pZpWjtTe5QIqvdzr9gDOO5IXgOElRiyvdw7wxeX9CUJXMp73fBC4XCBFDghDxLkUCvMbKeU2atHNDuiVfUdbsPlQHgFNE9lwK4Vdg3b8WaJj9EZODk1nZF2VNPK1cMog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تغییر چهره پسر ترامپ طی یکسال
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66341" target="_blank">📅 12:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66340">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d976a7f361.mp4?token=ETTLu-s7QlIjSUBFTcMbyzDvC1wQy-meOmsZz7JqTOjV2s_2daNJVtm0cTlxbHKCtMu9jLWlC3cYW8-TpzCdKh3Kl7bTUN3EmRo4JgwvE1PRwkj8VOOIBxwRWoV9-u1TXD0-7KMc4A8Qht-HGvfQqzBysx-N84meWv-bqgzROMN2g1G4pKqKA8Zk014FcfG-ZUtA1LX8zLhD1eEqogyu6dGrP6Cdc0t3dC-9_7Y3KqrR8DnPzf83elFmc_Lo4uldrZXqz4rwIMsmi-uSTiPSNGdMIQ3gmNEucZsZwHZhO6I17wXhWrqHEITogZqjmQyf1-OcCyTb7L5y8B7a2CuuXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d976a7f361.mp4?token=ETTLu-s7QlIjSUBFTcMbyzDvC1wQy-meOmsZz7JqTOjV2s_2daNJVtm0cTlxbHKCtMu9jLWlC3cYW8-TpzCdKh3Kl7bTUN3EmRo4JgwvE1PRwkj8VOOIBxwRWoV9-u1TXD0-7KMc4A8Qht-HGvfQqzBysx-N84meWv-bqgzROMN2g1G4pKqKA8Zk014FcfG-ZUtA1LX8zLhD1eEqogyu6dGrP6Cdc0t3dC-9_7Y3KqrR8DnPzf83elFmc_Lo4uldrZXqz4rwIMsmi-uSTiPSNGdMIQ3gmNEucZsZwHZhO6I17wXhWrqHEITogZqjmQyf1-OcCyTb7L5y8B7a2CuuXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تداوم حملات ارتش اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66340" target="_blank">📅 11:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66339">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac69a7be8e.mp4?token=Og5vg2rX1jYrhCiN4e1JUxng3YdRVU7Rdp8ronljbae0AJDgRGU-tLfB3M0EfP07R-YEKRKNPY7nYCvMuRHXYwI6VVB5MasSdkDjlPAHlo-MspwxbxUfEYQWVcbmgRvseR_CeHmojK0PrMnnIMxuad6IcYqRQCI336oc1a6PdLw9GCWcS0XumK3-TrTQMHAun7mfTBxIKXk1lSjvpc5RuhFETrtWLVXde9PGESjQUhbT6y9U3T7d43s2ajd7wiG9sIyiEFpSnCtumzXmvKkHMy4z7yNs2bgvAiQJzAKBQ0gQcGUIDel6mf9G5mPAoQs4zASkQtTEfL7lmjrrB1DdYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac69a7be8e.mp4?token=Og5vg2rX1jYrhCiN4e1JUxng3YdRVU7Rdp8ronljbae0AJDgRGU-tLfB3M0EfP07R-YEKRKNPY7nYCvMuRHXYwI6VVB5MasSdkDjlPAHlo-MspwxbxUfEYQWVcbmgRvseR_CeHmojK0PrMnnIMxuad6IcYqRQCI336oc1a6PdLw9GCWcS0XumK3-TrTQMHAun7mfTBxIKXk1lSjvpc5RuhFETrtWLVXde9PGESjQUhbT6y9U3T7d43s2ajd7wiG9sIyiEFpSnCtumzXmvKkHMy4z7yNs2bgvAiQJzAKBQ0gQcGUIDel6mf9G5mPAoQs4zASkQtTEfL7lmjrrB1DdYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
مایک پنس، معاون سابق ترامپ:
به جای توافق، باید اجازه داد نیروهای آمریکایی کار را یکسره کنند، تنگه هرمز را باز کنند، توان نظامی تهاجمی رژیم ایران را از بین ببرند و به مردم ایران یک فرصت واقعی برای آزادی بدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66339" target="_blank">📅 11:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66338">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ba759cb9.mp4?token=YFvOP_EqvhdFXYBuMQJhnEzygadcThz35uWLra-tryjiYgNlltbSKy1z4gjqKkJAy0_sNeHk7r-7GXqpJNbIPx2gU2F4Uwn7dSgqUg6tPt6Zy-AU_34j3samCR1g4Odycauvi5DdYj8AIgW5AcRKXilBQ5E5pH4ahu_koDxEvHppJxGWTJVe9t4p6LYuudjlar3lMa2BQzLgvZA83YkhkvRLSHEDdtgVbYFaE8yYSCNAWQ2bs-ZYZKoOjefKZgvqvAyvrFNhWNS6-jp-FevYGMB5SkJImX6SfI7H7Qe14CcVJ2pwAQ8YlgihLZ8vuXmmgEON2oAuTDTNCqBuP2ktzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ba759cb9.mp4?token=YFvOP_EqvhdFXYBuMQJhnEzygadcThz35uWLra-tryjiYgNlltbSKy1z4gjqKkJAy0_sNeHk7r-7GXqpJNbIPx2gU2F4Uwn7dSgqUg6tPt6Zy-AU_34j3samCR1g4Odycauvi5DdYj8AIgW5AcRKXilBQ5E5pH4ahu_koDxEvHppJxGWTJVe9t4p6LYuudjlar3lMa2BQzLgvZA83YkhkvRLSHEDdtgVbYFaE8yYSCNAWQ2bs-ZYZKoOjefKZgvqvAyvrFNhWNS6-jp-FevYGMB5SkJImX6SfI7H7Qe14CcVJ2pwAQ8YlgihLZ8vuXmmgEON2oAuTDTNCqBuP2ktzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسایی نماینده مجلس:
اگه کسی ذره ای عقل داشته باشه به جانشین شدن فرزند رهبری میخنده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66338" target="_blank">📅 10:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66337">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzZDQTSInafJqwuuaLNtWK_F4rwW4xBz0jNckMhhLhqVRtbjDLJNooqwqSIYYuZPPpA562uaFP0pJwfYQ9SmYk9kyUUIa-04cfVvBJiEMHMYUfATJH0NBoPW6FOHXg7eZge8IPx_NDvg0dJKqW5l7w0qp2RWU_txVt2YVVTlB-VmdVpjJvomKW4q7aPDO9Gdgo8lEQ32-Y9p94dVhjRNz7Y89-1yfsLa6TeO5_jTN7HtUv_IxeZT3Ql5yiemTgt8p0phlMp3-xO76xF-MSS4QbKBHPjSz46DEoXKsRZuJ9T2gCpE_0qfF2LfZoWKhQGd5dn-jHkAkKjcqAUys-PdYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
مجلس سنای آمریکا طرح محدود شدن اختیارات ترامپ در جنگ با ایران را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66337" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66336">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0d9bfbe9c.mp4?token=qanFjH-7LD0LGfFpxd-lLX5YnNS1_2mkA3cccNbpdresrVpaxyC1nkHyTAUOA1WFS1qw60i4MlT4JWAl5vgJliqFLa0CW9Z1JuGkiFeA68ljIUyRi8JNAL7zMHSII9k3GM4spmQjGaTUBZwiw7gY14AKz6PeggdNuDUhtjtZMZ3_zf1aCaDxVmVNa8d6NW0egOYhaKWlcSL4kjntSHTdkWgtWctT0MwPMS2UL4zotYPWjlQPrs7-wCBhZSjs8D_HrAnsz5lEk_ZQEKsHMyWgaUoETgl1sWbqTb2F_duOn-6ALU9kN8YxplJKNnUznnDL2OTL0UOw5gtKRYPm0tS2qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0d9bfbe9c.mp4?token=qanFjH-7LD0LGfFpxd-lLX5YnNS1_2mkA3cccNbpdresrVpaxyC1nkHyTAUOA1WFS1qw60i4MlT4JWAl5vgJliqFLa0CW9Z1JuGkiFeA68ljIUyRi8JNAL7zMHSII9k3GM4spmQjGaTUBZwiw7gY14AKz6PeggdNuDUhtjtZMZ3_zf1aCaDxVmVNa8d6NW0egOYhaKWlcSL4kjntSHTdkWgtWctT0MwPMS2UL4zotYPWjlQPrs7-wCBhZSjs8D_HrAnsz5lEk_ZQEKsHMyWgaUoETgl1sWbqTb2F_duOn-6ALU9kN8YxplJKNnUznnDL2OTL0UOw5gtKRYPm0tS2qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس درباره ایران:
اگر دونالد ترامپ به عنوان رهبر ایران انتخاب می‌شد، دموکرات‌ها همچنان می‌گفتند که ایالات متحده باخته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66336" target="_blank">📅 09:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66335">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/555366529c.mp4?token=pqHZ3FaM5T8YOFykq47MAZZwKTvaXewheYR_dyE8INhvk4h1oDU3zCgkVLLqmnNvPaGK2JHsGmojctAFFwthbH6nqM4b9kTHi6GPKegAA4VL7JXF69GCtehNvKNtuC5wZ_sN-AbLcI7tb9z3lS39vno4rb_EMCjUX1hwBEfDUbherApbnb7ESI_HfoXj_QmAPcwtiQ4hJfRqtMa9ZLxlPsOurftkgi1ZWbHMH5drvmmPiZgAOhLSSfQqQNNuj2ehr2Vm7mgwGXowfG-u3HJr6ABfJ2Bh5gEWZhu6c0t0AgXHkVtK0c_G2H0i5pMCSGPRj57_HEnoUN2fNUY0CHQyEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/555366529c.mp4?token=pqHZ3FaM5T8YOFykq47MAZZwKTvaXewheYR_dyE8INhvk4h1oDU3zCgkVLLqmnNvPaGK2JHsGmojctAFFwthbH6nqM4b9kTHi6GPKegAA4VL7JXF69GCtehNvKNtuC5wZ_sN-AbLcI7tb9z3lS39vno4rb_EMCjUX1hwBEfDUbherApbnb7ESI_HfoXj_QmAPcwtiQ4hJfRqtMa9ZLxlPsOurftkgi1ZWbHMH5drvmmPiZgAOhLSSfQqQNNuj2ehr2Vm7mgwGXowfG-u3HJr6ABfJ2Bh5gEWZhu6c0t0AgXHkVtK0c_G2H0i5pMCSGPRj57_HEnoUN2fNUY0CHQyEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وقتی نماینده میخواد ثابت کنه زندگی ساده ای داره و اونجور که همه فکر میکنن نیست
😂
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66335" target="_blank">📅 09:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66334">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66334" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66333">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u_2stG8SUYx1GUDKt_3vK9DOMEpSwyhakejwHYeOl9ArFBbVXFJUK5A4plQ8WrD23-KawSdRTUB_rf2TKRgyc2J6ITvydsLU8onwzpHfwKUbsrDXCJyUvr2UBBquXPMAt6H82ye95o5ibaYDEJ9LWN9ppx3Ae8ydL_eHq9Uzkpbbzn5cPfQln3KnwfkQ37ABji3P9GYZp9Ln6mT6TvVTY5LSmzbdWUKy1_U8_tzgp-lNVzeOloGrPv0L_hAsotbh0eCO1nTtOisqTFJUFq95xFpmOyzOap_h4_sKI5whegm7CubtFwUZGZ4j-h_CLxg3lIN5mjWosZJLvwDv_lN2IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66333" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66331">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
به ادعای باراک راوید مفاد توافق ایران و آمریکا به شکل زیر است:
ایران، ایالات متحده و متحدانشان خصومت‌ها را متوقف خواهند کرد، از جمله در لبنان.
ایران تعهد خود را به عدم توسعه یا دستیابی به سلاح‌های هسته‌ای مجدداً تأکید می‌کند
ایالات متحده و ایران متعهد می‌شوند مسئله دفع ذخایر اورانیوم غنی‌شده ایران را حل کنند.
ایالات متحده و ایران درباره غنی‌سازی اورانیوم و نیازهای انرژی هسته‌ای غیرنظامی ایران گفتگو خواهند کرد.
ایران وضعیت موجود برنامه هسته‌ای خود را در طول مدت مذاکرات حفظ خواهد کرد.
ایالات متحده محاصره دریایی را برمی‌دارد، از تحمیل تحریم‌های جدید خودداری می‌کند و در طول مذاکرات حضور نظامی خود در منطقه را افزایش نخواهد داد.
ایران ترتیبات لازم را برای تضمین عبور ایمن کشتی‌های تجاری از تنگه هرمز، بدون هزینه، به مدت ۶۰ روز فراهم خواهد کرد.
ایالات متحده متعهد می‌شود دارایی‌های منجمد شده ایران را پس از اجرای تفاهم‌نامه در دسترس قرار دهد.
اگر توافق نهایی حاصل شود، ایالات متحده نیروهای خود را ظرف ۳۰ روز خارج کرده و تمام تحریم‌ها علیه ایران را لغو خواهد کرد
.
هر توافق نهایی شامل برنامه‌ای برای ایجاد صندوق ۳۰۰ میلیارد دلاری برای بازسازی ایران خواهد بود
ایالات متحده به ایران معافیت‌های موقتی تحریمی برای اجازه فروش نفت در دوره مذاکرات اعطا خواهد کرد
مذاکرات بین ایران و عمان با مشارکت کشورهای خلیج فارس برگزار خواهد شد تا ترتیبات مربوط به حمل و نقل و خدمات دریایی تعیین شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66331" target="_blank">📅 00:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66330">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9122af9759.mp4?token=o5hPFuqB2qm_9TsQwUlL1R4qQs67Nejd0mZrwvQq2_7iTugNMoRdqcUammoKvhX7oRs22hyK3_veSB90O_QPdzPKP3xzfecbVQnSOSaJsA_8urr_jCp-Z0xSc-k3GtPUyYGQdksYGT9XHH_HJwtKYVkcO5BBiDz3wX_EQSHEusoG49GAwQBaCrbsnEkf3QTkeLVgFB0EIJnmyt7hUkNcQTVhieeoMpndWSTmXGzizJiRRJQtLaNTC7xVqdagamI2FDsu21TUOxCbzOGhsxtP6WWXXSQtHzbGxt3rppeHhtXAyyfM_xdtJkMqqRKGAfjPVb01tDsYjo0wrkcvajTeNj1hD5cR-NlqeIixZIbXFJRtQdJlGxu7WcjWdggYfKki5AvxnvoOXoa_4fWgals3T_BV3VzCRlrZtQL-2lwO16fzcwNHfPMDCvdofwawQ7RixUIyWr23HiFh7capgF5wge6wGAKbR3_kg6DPvt4MUjZd-WNOQimvV1Qib1pyGw5eC8_0nlMRCfAWIfqlJPLwSlprceXAco2IXAGHQMj4qJvls1Pa5OnszU6c7NIBJDy5BgQ5Yh2GeAONYfJGQDmFNkZrMpBPM3n1Umz4zKwI2tUJblP99xALjAgP_ZtiTJWpM-Udj32Nc0qMdZ1xzvlZa2wBDH2uHGvc3TTP8ww29Ts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9122af9759.mp4?token=o5hPFuqB2qm_9TsQwUlL1R4qQs67Nejd0mZrwvQq2_7iTugNMoRdqcUammoKvhX7oRs22hyK3_veSB90O_QPdzPKP3xzfecbVQnSOSaJsA_8urr_jCp-Z0xSc-k3GtPUyYGQdksYGT9XHH_HJwtKYVkcO5BBiDz3wX_EQSHEusoG49GAwQBaCrbsnEkf3QTkeLVgFB0EIJnmyt7hUkNcQTVhieeoMpndWSTmXGzizJiRRJQtLaNTC7xVqdagamI2FDsu21TUOxCbzOGhsxtP6WWXXSQtHzbGxt3rppeHhtXAyyfM_xdtJkMqqRKGAfjPVb01tDsYjo0wrkcvajTeNj1hD5cR-NlqeIixZIbXFJRtQdJlGxu7WcjWdggYfKki5AvxnvoOXoa_4fWgals3T_BV3VzCRlrZtQL-2lwO16fzcwNHfPMDCvdofwawQ7RixUIyWr23HiFh7capgF5wge6wGAKbR3_kg6DPvt4MUjZd-WNOQimvV1Qib1pyGw5eC8_0nlMRCfAWIfqlJPLwSlprceXAco2IXAGHQMj4qJvls1Pa5OnszU6c7NIBJDy5BgQ5Yh2GeAONYfJGQDmFNkZrMpBPM3n1Umz4zKwI2tUJblP99xALjAgP_ZtiTJWpM-Udj32Nc0qMdZ1xzvlZa2wBDH2uHGvc3TTP8ww29Ts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
جی‌دی ونس درباره ایران:
🔻
ترامپ هیچ‌وقت نگفته که هدفش این است که رضا پهلوی را به عنوان رهبر جدید ایران منصوب کند. چیزی که او گفته این است که اگر مردم ایران بخواهند قیام کنند، عالی است. این کار خودشان است. این موضوع بین آنها و دولتشان است.
چیزی که ما می‌خواهیم، توقف برنامه هسته‌ای ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66330" target="_blank">📅 00:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66329">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
جی‌دی ونس:
🔻
فرض کنید امارات متحده عربی که یکی از بهترین متحدان ما در منطقه است، بخواهد در یک نیروگاه هسته‌ای در ایران سرمایه‌گذاری کند. عملاً بدون اینکه ما بعضی از تحریم‌های موجود در سیستم مالی جهانی را برداریم، این کار ممکن نیست.
🔴
حالا سؤال این است: آیا اماراتی‌ها در ایران سرمایه‌گذاری می‌کنند؟ یا آمریکا اجازه می‌دهد اماراتی‌ها در ایران سرمایه‌گذاری کنند؟ نه.
🔴
برخی می‌گویند خب، شما به ایران پول می‌دهید. نه، نه، نه. ما می‌گوییم فقط اجازه می‌دهیم برخی از این کشورهای دیگر در بازسازی کشورشان سرمایه‌گذاری کنند و برای مردمشان رفاه ایجاد کنند. این چیز خوبی است، مگر نه؟
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66329" target="_blank">📅 00:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66328">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400d2a3a78.mp4?token=uD9waT5ohG5mfoD8mGkjTf4NxKvgZAK4owy1ot9rXQdnp3B_kITM4Tjb-3mv50-0-YombqjH3dcKGbSG4ouL3niUYMoMcTRMkx2naMaRPlUz1kUwCzwsI5PhDV1wI4JuPbkYoOn9UK7ZwUJM4yxg5tR4G4E97EqWmq_bUucRuOLw4u8c45AIeQ6A4Aeo0D1mcAlCQAlx05Aa7Hyc8M_8kMFyV1pfqNmyFmYXW5dJ19tEdUe_W1lFSjHJdGGtgYt9CcRgEnvh6vplhnclkCjfgpTDXhMHHdeZNjjj1BUn29DX8KRrocQ5ASQ01RkIA9poLeA6vo2-gDDa4diwcLKvdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400d2a3a78.mp4?token=uD9waT5ohG5mfoD8mGkjTf4NxKvgZAK4owy1ot9rXQdnp3B_kITM4Tjb-3mv50-0-YombqjH3dcKGbSG4ouL3niUYMoMcTRMkx2naMaRPlUz1kUwCzwsI5PhDV1wI4JuPbkYoOn9UK7ZwUJM4yxg5tR4G4E97EqWmq_bUucRuOLw4u8c45AIeQ6A4Aeo0D1mcAlCQAlx05Aa7Hyc8M_8kMFyV1pfqNmyFmYXW5dJ19tEdUe_W1lFSjHJdGGtgYt9CcRgEnvh6vplhnclkCjfgpTDXhMHHdeZNjjj1BUn29DX8KRrocQ5ASQ01RkIA9poLeA6vo2-gDDa4diwcLKvdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🎙
جی‌دی ونس:
🔻
یک نفر گفت - یادم نیست کی - که این توافق مثل اجرای طرح مارشال وقتی نازی‌ها هنوز سر کار هستند، می‌ماند. این حرف از چند جهت غلط است.
🔴
اول اینکه طرح مارشال با پول مالیات مردم آمریکا انجام شد، اما اینجا قرار نیست پول آمریکا خرج شود.
🔴
دوم اینکه ما می‌گوییم فقط وقتی از مزایای این توافق بهره‌مند می‌شوید که رفتارتان را عوض کنید.
🔻
(البته کسی که این حرف را زد، سناتور لیندسی گراهام بود.)
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66328" target="_blank">📅 00:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66327">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7276198054.mp4?token=aqi1lmQcjxrQkNmuqg8FjH4z4is504zZkDmTaynTpJGCMSXNdRhf8FwEeWrtdZmO8BZVJgxx_I1Cw-6pyePVoXlwAB2TPmSIl3MRsjpgcX8SUQGb1jeC3uLWE1TUpHwRU9j7A-z6QrbiD6LLL5YZfIjbskpy-65xxHJVZpfoOqw2-N5IkDLEif8I_axod75G5DoNWQ4jmb-mhFH4KnS0vxtHcMdiCrXirEG7cvVHr4su075fVmZRrwFTwBrNMwGmxpZLDvInpqwb6hVogwUu_3M5lmf6ZRPg8cJNmq8rhetlOUwoaIJrpSlfbG56wgYnYx9lD6mEnvxEuD9ubUL1d0xH2b9ARx-oOwDFf-7etP9IAr6fsQ2-rabh27iqwP0onPGH8mVZh4AaZebr2nMivHe1rf7tljeYCJM0ynwZja2kyvxp5K7rWzoXltO-7hM0om2WumyfROm8k8liBbd8lsZqYbQiP3NdFAyrc-lsaSsYnq6zpcH2v1xOAweZuvBfvsZFdyb9VwbKxQCe1-DQ58WmUBRKxqWSMq-UwhSo0AXJUvKYwXeE31fc-Nn8K3ArrU6jWZW7KFxFq4y_AkSQbJjeMzF8huksJPsdwgsLZ1Ubhr7a34dtAjYAXbfwl97dg1bAQELtPyJW6qcSXUAPKEagtx01BzJSuVwNWjBGfF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7276198054.mp4?token=aqi1lmQcjxrQkNmuqg8FjH4z4is504zZkDmTaynTpJGCMSXNdRhf8FwEeWrtdZmO8BZVJgxx_I1Cw-6pyePVoXlwAB2TPmSIl3MRsjpgcX8SUQGb1jeC3uLWE1TUpHwRU9j7A-z6QrbiD6LLL5YZfIjbskpy-65xxHJVZpfoOqw2-N5IkDLEif8I_axod75G5DoNWQ4jmb-mhFH4KnS0vxtHcMdiCrXirEG7cvVHr4su075fVmZRrwFTwBrNMwGmxpZLDvInpqwb6hVogwUu_3M5lmf6ZRPg8cJNmq8rhetlOUwoaIJrpSlfbG56wgYnYx9lD6mEnvxEuD9ubUL1d0xH2b9ARx-oOwDFf-7etP9IAr6fsQ2-rabh27iqwP0onPGH8mVZh4AaZebr2nMivHe1rf7tljeYCJM0ynwZja2kyvxp5K7rWzoXltO-7hM0om2WumyfROm8k8liBbd8lsZqYbQiP3NdFAyrc-lsaSsYnq6zpcH2v1xOAweZuvBfvsZFdyb9VwbKxQCe1-DQ58WmUBRKxqWSMq-UwhSo0AXJUvKYwXeE31fc-Nn8K3ArrU6jWZW7KFxFq4y_AkSQbJjeMzF8huksJPsdwgsLZ1Ubhr7a34dtAjYAXbfwl97dg1bAQELtPyJW6qcSXUAPKEagtx01BzJSuVwNWjBGfF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇱🇧
جی‌دی ونس
:
🔻
اگر ایران حزب‌الله را تامین مالی می‌کند، ما اجازه نخواهیم داد که مجموعه‌ای از دارایی‌های بلوکه شده به ایرانی‌ها منتقل شود
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66327" target="_blank">📅 00:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66326">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8b2573c92.mp4?token=aKBEYnSWEfoGTQcWXkOo1VLIDZERmWvXg38Tin-bvC1Iuuces81tF6CVqfRlNh3BLcf0IGuAt4w1IFPT2O53MKfh4BCGRVQ_W2IKv8dqnXGWhKWCfrz3Hi8F4vYTW8ETvfmRVUEtIga4FuPYxohFtD3fX6_xM13nLpGVQmwfn1uf_Pn1IAgG62okIFn_R9go9LWQq_sWbMxiU6_3v9OhFPIKgA1rRZ5SQVIzWrHT1L1gJhreEjCvdGWL2ozhl2tThhSk6Rj23B2XR6qjf__GijpaDTPd36cu81iQca0pkvW6gW-qSGL61mlajEllpXp4y59zZJNEkW8wbPWE3yf6Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8b2573c92.mp4?token=aKBEYnSWEfoGTQcWXkOo1VLIDZERmWvXg38Tin-bvC1Iuuces81tF6CVqfRlNh3BLcf0IGuAt4w1IFPT2O53MKfh4BCGRVQ_W2IKv8dqnXGWhKWCfrz3Hi8F4vYTW8ETvfmRVUEtIga4FuPYxohFtD3fX6_xM13nLpGVQmwfn1uf_Pn1IAgG62okIFn_R9go9LWQq_sWbMxiU6_3v9OhFPIKgA1rRZ5SQVIzWrHT1L1gJhreEjCvdGWL2ozhl2tThhSk6Rj23B2XR6qjf__GijpaDTPd36cu81iQca0pkvW6gW-qSGL61mlajEllpXp4y59zZJNEkW8wbPWE3yf6Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوند و تعریف و تمجید از ترامپ
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66326" target="_blank">📅 00:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66325">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1190f45b0e.mp4?token=mN-K8KBjOJnlvKEK5kjHpQXNfpr326lDyy-VjKXa2miSeqJ5_AlXCcfvbstLpcWoqa0fP2dce0OEnvtN7yEzwquABH89l3Y1LO4cgmyjZOBs4B6o9HU8CeVu7b9rXL9CVYDdM_oXKtP0n5DSRgee-wCbwjVt4GEvcNd6YUwVp__NDkopbik6ZE1KcQL68QQO4WzDAkSVuLeLmjx4_h2AsO-VlhlroCEXjEmHWQTb9N8FyjcpwrS9EREqImpu4ZB4Ygro5AitNKvT2DmskzElMIk2Eb6SYvuMzmaz4s-nWvTCChqm8rt1hDxFKVgHLMalcrwhoRf6wk8fIFObYsH2HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1190f45b0e.mp4?token=mN-K8KBjOJnlvKEK5kjHpQXNfpr326lDyy-VjKXa2miSeqJ5_AlXCcfvbstLpcWoqa0fP2dce0OEnvtN7yEzwquABH89l3Y1LO4cgmyjZOBs4B6o9HU8CeVu7b9rXL9CVYDdM_oXKtP0n5DSRgee-wCbwjVt4GEvcNd6YUwVp__NDkopbik6ZE1KcQL68QQO4WzDAkSVuLeLmjx4_h2AsO-VlhlroCEXjEmHWQTb9N8FyjcpwrS9EREqImpu4ZB4Ygro5AitNKvT2DmskzElMIk2Eb6SYvuMzmaz4s-nWvTCChqm8rt1hDxFKVgHLMalcrwhoRf6wk8fIFObYsH2HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان بازیکن تیم جمهوری اسلامی به خبرنگار خارجی:
مسائل داخلی ایران به شما ربطی ندارد؛ مسائل خارج از فوتبال، بین خود ماست و خودمان آن را حل خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66325" target="_blank">📅 23:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66324">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcce5ba4b.mp4?token=GMgg5VdzjxbO72OZGmGzw_gD-eWZsmFGv8pTGkf__231wfiW75ISATUjxXFjnM0_kdX7LdqqmGbsQX1j7IlyC_skeH6kQqH-zCq5gvTRQhSy39zqhuSDb7Pzr6VX2WKgfinRpMAV_gaT5pEmBRq10mKNrmuJ41m5UqsYaM2Q8O-swpa3HBzXUEQP0eza5EIzKYkrApQubSPrMRK1IAj136IdN8tqWaERJJ1LcDVJRhv7O1zMWnaJyPfAWcFI7EJCZfEKskYiczXOjkRSyCJvoHR6WRmwH86ytFhOYcT-RpIEeMN3wfdn1steFCdMuUmXV0oCIhLOeidibdGIujZxIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcce5ba4b.mp4?token=GMgg5VdzjxbO72OZGmGzw_gD-eWZsmFGv8pTGkf__231wfiW75ISATUjxXFjnM0_kdX7LdqqmGbsQX1j7IlyC_skeH6kQqH-zCq5gvTRQhSy39zqhuSDb7Pzr6VX2WKgfinRpMAV_gaT5pEmBRq10mKNrmuJ41m5UqsYaM2Q8O-swpa3HBzXUEQP0eza5EIzKYkrApQubSPrMRK1IAj136IdN8tqWaERJJ1LcDVJRhv7O1zMWnaJyPfAWcFI7EJCZfEKskYiczXOjkRSyCJvoHR6WRmwH86ytFhOYcT-RpIEeMN3wfdn1steFCdMuUmXV0oCIhLOeidibdGIujZxIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرزیدنت پزشکیان:
مشکلات خودتون رو خودتون حل کنید، من سیاستمدار نیستم من دکترم، برا سلامت مردم اومدم
😔
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66324" target="_blank">📅 23:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66323">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9ab7bce46.mp4?token=S9PWtXi8j3G82m036x1OXtwqY8-nJRZHiW0mR7Un6YMBpMeDvB2bRew8FBgjvfFwRFL9Xt9uApyUcrKOP7RpLeNlW_VN0BnqginVlNJvD5c2SZoLqGw1H8JLbT-gg-vkMh8Zn6vMRtWlsEvlmVCBKTAHAdLdTvgXM-dXXV8-3rDZ4BieO91Xi2MwXrX_Xt2DYyNMQBiQVmrQKhdserVsNcM0KoLxix6vnmKMpyDERPHKvcjWMgZnz4crq7NLaw2M8cHnpayVvTVBFLmnh44aMJ_2512Idm1DaPUtHdrxiBwx5c5xu7tbhyvuF6ny078VYbuVd9FnPdUmGSrLMgsAJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9ab7bce46.mp4?token=S9PWtXi8j3G82m036x1OXtwqY8-nJRZHiW0mR7Un6YMBpMeDvB2bRew8FBgjvfFwRFL9Xt9uApyUcrKOP7RpLeNlW_VN0BnqginVlNJvD5c2SZoLqGw1H8JLbT-gg-vkMh8Zn6vMRtWlsEvlmVCBKTAHAdLdTvgXM-dXXV8-3rDZ4BieO91Xi2MwXrX_Xt2DYyNMQBiQVmrQKhdserVsNcM0KoLxix6vnmKMpyDERPHKvcjWMgZnz4crq7NLaw2M8cHnpayVvTVBFLmnh44aMJ_2512Idm1DaPUtHdrxiBwx5c5xu7tbhyvuF6ny078VYbuVd9FnPdUmGSrLMgsAJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عرزشی:
چرا با کسی که به رهبر عزیزمون اتهام جنسی میزنه مذاکره میکنید
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66323" target="_blank">📅 22:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66322">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
ارتش اسرائیل، طی دو روز گذشته پس از اعلام پایان جنگ از سوی ترامپ، «۸۴ بار آتش‌بس در جنوب لبنان را نقض کرده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66322" target="_blank">📅 22:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66321">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
#فورییی
؛قرارگاه مرکزی خاتم الانبیاء:
اگر ارتش رژیم صهیونیستی حملات خود را در جنوب لبنان متوقف نکند، باید منتظر پاسخ سختی از سوی ما باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66321" target="_blank">📅 22:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66320">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e376d329d7.mp4?token=jOsMKmWkT_qCvfuj-K7y6aXFBRzFvC5DRXrZ8tdzMOnQrwARzcW_3oNiRBTRAzvClFeb92zwWF69qdywC4LkS6P-O4sr9G7dcpaJRWapEg3JDGoQ2Fnta4gUPiYhuaZLN0arWVaM_tXyYdO_aNuqm5qimF88Y96a18_mCjkab9aUNPSIJCHoJKHDBWUvfgH0AvCuqit94fVW7z4PjFpPHofwbZIc3wJHKMT_co8upTwE-CQjJiSKUgB8hxENyQoj85sAbdo6VNZQ0v8Xn2DjhMLYuVEL-UE1pOinZMzluboDpeReuUazT2DMHX4Mk9ahZUTU5_2VaHoQ0KoMJPJryQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e376d329d7.mp4?token=jOsMKmWkT_qCvfuj-K7y6aXFBRzFvC5DRXrZ8tdzMOnQrwARzcW_3oNiRBTRAzvClFeb92zwWF69qdywC4LkS6P-O4sr9G7dcpaJRWapEg3JDGoQ2Fnta4gUPiYhuaZLN0arWVaM_tXyYdO_aNuqm5qimF88Y96a18_mCjkab9aUNPSIJCHoJKHDBWUvfgH0AvCuqit94fVW7z4PjFpPHofwbZIc3wJHKMT_co8upTwE-CQjJiSKUgB8hxENyQoj85sAbdo6VNZQ0v8Xn2DjhMLYuVEL-UE1pOinZMzluboDpeReuUazT2DMHX4Mk9ahZUTU5_2VaHoQ0KoMJPJryQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنوز سواله برام؛چرا خارج شد؟
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66320" target="_blank">📅 22:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66319">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8ZHdayqpPDCHTkFSJZDN1F1VYkSiv1k8-7ANiud7Wf2iwRQ2SulT4F1X71xYLJA22G9qdFsc78013YeHlhThvaM0P1Ov8PQiRekm9XIGeUSCrll5uvo0AHg8AwvLKROhE7OXSCuRL5jOyofpQqAGpnZG87KFQCRL8LI3ZjoHnwHzbXSXTEygiTIeYvuOuEgt37p1H1XwdOLb0lBKLw6XZIqiptSNgfjGhfoQvUocNbhaOmlZW1aNwsQAB2TTb-6WxK5_pxspwD0gkecOOxcmizFWvQzKI1A0A6DfBjNlUU8eIXALFnl1snNzwaa9xQmJbbS20skGd6_qkABhpneQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نفتالی بنت یکی از نامزد های نخست وزیری اسرائیل در انتخابات آینده:
توافق فعلی بین رژیم جمهوری اسلامی و آمریکا فقط یک توافق موقت است.به ملت شریف ایران می‌گویم که امیدتان را از دست ندهید، جمهوری اسلامی رژیم فاسدی است که سقوط خواهد کرد. نوبت بعد که مردم ایران قیام کنند ما ابزارهای لازم را در اختیارشان قرار می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66319" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66318">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/837293596a.mp4?token=jerIxpNv6uqc4mBcjxHr0kR_4IKZ3l6lp_A6p9gI9lOEw00-VNxurBTpZVd0rz-t6UQtVcM986FOwQNb6VRi5YEKmheS7umGktTVohGWH4zmQO79BGHXI8P-yIGcaNtGj7I_3jCczL9hDk4N_-hGjwSuxsGUK0PrmTUID9mIrl8ZpgNph2wuXBWhYLhGdp8xzefavLsnapUGIcjU6hAZa3IlNI1_qviolS2-2nhYQPaLsCwGaqYgIiWROlDaMVFk3zHQ1QNtZFkCxnt5jeuHEodNNdcfOKP1CqWjMJv_XNeI4Vq-aS2SVlcyBgn5tGVZyYwp8bPr5vxlMpFbbitQDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/837293596a.mp4?token=jerIxpNv6uqc4mBcjxHr0kR_4IKZ3l6lp_A6p9gI9lOEw00-VNxurBTpZVd0rz-t6UQtVcM986FOwQNb6VRi5YEKmheS7umGktTVohGWH4zmQO79BGHXI8P-yIGcaNtGj7I_3jCczL9hDk4N_-hGjwSuxsGUK0PrmTUID9mIrl8ZpgNph2wuXBWhYLhGdp8xzefavLsnapUGIcjU6hAZa3IlNI1_qviolS2-2nhYQPaLsCwGaqYgIiWROlDaMVFk3zHQ1QNtZFkCxnt5jeuHEodNNdcfOKP1CqWjMJv_XNeI4Vq-aS2SVlcyBgn5tGVZyYwp8bPr5vxlMpFbbitQDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی‌دی ونس:
اگر مردم ایران خواهان رفاه بیشتر هستند، رهبرانشان باید پیشقدم شوند و رفتار خود را تغییر دهند اگر این کار را انجام دهند، عالی است. اگر ندهند، ایالات متحده قبلاً چیزهای زیادی به دست آورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66318" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66313">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k11PTSqOFvpxb0RmvDNTBkHJqLUHkcJ78mMMI2s1luzI7CutoV_3YHEVTF5lqYN3rcUfRGjj3yQe2DI3Fb_tR8LvLpJhQuMjTv32VXp2kSFH_NqIwZlDNUwlwnfSbXwreKckZ14NfqNiUYxVsWZD9nNr-R8JH_tWwcVPvl71HtCgDUmOsbPil-ZJDy8tkUV7HVwTni0M1F8DCUrHVaT5zv2svoC1owKHpfHOKZgYNzljdyjqAR5X0O_usVgUfeARs7AmRW26wZcV1fHzCbsld0FTum9IDK_VmczjysEINouigf6ftPVFdflI-KLH2XjpEq1XxIRhQThdci-BGkfhGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
زیر نویس شبکه خبر:
حمله پهبادی اسرائیل به دو روستا در نبطیه در جنوب لبنان ۴کشته و تعدادی زخمی برجا گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66313" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66312">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxBKZJWbG7JbpjKbasAjJjxlfswhrHBW5fTa4OARLL1vG1pWXCJgkIMNZxk_LfLDc6p8X8l-8r6nXNX94m9zaMJ-i6J2zdlZgosGNs1fdGIN_KR3IY2kREKe7IOaw_i2oDGYYTXwM3AOGkwyG6DLFpKH37qv80D1F-x5IfppWtvo2mT9zP-q10dE8U_o0YWYHBVd0dMJLPg46kMb7ZIodvkqhTGV33L9ET930KaRiKy2GpGTAaVDBwGBr6e3N0-jNctPqh9JNurtZl09dYgZZG2Fz70gmeHNkDjpqSQjgvxmlXdSE7wD7QsK5YI0qAy5_5KnU5dnh87L0Pewf7I6Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتاق جنگ اسرائیل:
لانچری که به سمتمون موشک شلیک کرد رو هدف قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66312" target="_blank">📅 20:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66311">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c47f7533b.mp4?token=ZUXV93mgLaPTK5GprjFd3ZDk8eo7arbYhipqC6_uSx9vLxw14Eopo5CmqSxsoc7gm6m3APmnWED0G91NbOLnwd8xsqLG1Ww-op0mkHCEj14DHsDbz6q_eYKwmP_3mWuU8W9SbMqgQ8ljOKt5SveTEchrrjOju7yUtqeqao02hIOXs2Ao_LeqIaYvEq6NPfi_W3lO4edmEBYEAUAgNQjzHgja7YjWT1SaeaMzj2Uvj28daW3v8zKFuXIMOf88LyWSxUsHhKkrWTaGJa33bfca0-s5i5zLO3vaefgxWFMr36vnH-v1uyAynLLiYWOwArmZaW6RcYt2UbzMd9DdyovyqH8jW-uEl1cq-PFjmNO5dSXm8cKRvkGMi_Qh935CMULyYii2kIWhIE9AXn_6Oge6X3zkYgblA0mvz46_nsZdc1ImzSd0t2y7tlw0mJTvWUxOOU8Hvq6woMSOQsEToNOtETfdhnQoXu9ILwZuSaQGZagntJYerroGU1_DEzsS8p218LRr2cLdktklzymO9Fi0UEVWWSSAGdkWrZFxgslyEdtSX6EWZrN7jB5eeKdu-yOV69GhsG1_4RBy9-lEAUFiTCgWFqp93QSYYyPjESA95QCu7dahEZay0wJpDVNmmoFkjT3kAJcPhk6u0omaC63WY80o4pJYZvPK_e3qDI6LxXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c47f7533b.mp4?token=ZUXV93mgLaPTK5GprjFd3ZDk8eo7arbYhipqC6_uSx9vLxw14Eopo5CmqSxsoc7gm6m3APmnWED0G91NbOLnwd8xsqLG1Ww-op0mkHCEj14DHsDbz6q_eYKwmP_3mWuU8W9SbMqgQ8ljOKt5SveTEchrrjOju7yUtqeqao02hIOXs2Ao_LeqIaYvEq6NPfi_W3lO4edmEBYEAUAgNQjzHgja7YjWT1SaeaMzj2Uvj28daW3v8zKFuXIMOf88LyWSxUsHhKkrWTaGJa33bfca0-s5i5zLO3vaefgxWFMr36vnH-v1uyAynLLiYWOwArmZaW6RcYt2UbzMd9DdyovyqH8jW-uEl1cq-PFjmNO5dSXm8cKRvkGMi_Qh935CMULyYii2kIWhIE9AXn_6Oge6X3zkYgblA0mvz46_nsZdc1ImzSd0t2y7tlw0mJTvWUxOOU8Hvq6woMSOQsEToNOtETfdhnQoXu9ILwZuSaQGZagntJYerroGU1_DEzsS8p218LRr2cLdktklzymO9Fi0UEVWWSSAGdkWrZFxgslyEdtSX6EWZrN7jB5eeKdu-yOV69GhsG1_4RBy9-lEAUFiTCgWFqp93QSYYyPjESA95QCu7dahEZay0wJpDVNmmoFkjT3kAJcPhk6u0omaC63WY80o4pJYZvPK_e3qDI6LxXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه ای که سپاه داره لانچرو برا شلیک موشک آماده میکنه و ایشون هم شروع میکنه به فیلم گرفتن.
واکنش سپاه:
😡
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66311" target="_blank">📅 19:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66308">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTkYzZ2lYhXvW5PgMD925zfHakTBITdcq_bEMyOirw8xyyXODPx5mv9wCcenZiTOPvjNVKpna478k7NsmENlKtVHLgWIVoi-wL1Di3qxJkiAdaRJiyfHh28Ze_5l-Y4z4Cs1GHnzjmLFVzOflsNV2NVpi5io1Mpn4Vs6T3quT2mmBwCwpdTwO28dPbfTzPAqZJ2tLVvy5dhHkCgNsM8Kk7b10cbSXbSv-OokdZEu9OUOOTDanwyvRZkWIev2W_ls9MGDNs2f95pkwM2qp09h_vNwDZgQ0hf_MA-nZWaOhXOHjz7TNsBn62Lh-9uBocZxYZIwDPnuaOGafi6yduPTHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فاکس نیوز:
اف‌بی‌آی یک توطئه تروریستی گسترده و چند مرحله‌ای را که قصد داشت رویداد UFC Freedom 250 روز یکشنبه را در چمن جنوبی کاخ سفید هدف قرار دهد، خنثی کرد.
به گفته مقامات فدرال، این نقشه وحشتناک برای "ایجاد حداکثر تلفات" طراحی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66308" target="_blank">📅 19:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66307">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpIepbZwPabxvUUIXZ4Eyt35-O93CKwKvPnbai-KKqPMaoLiDc5V7WravjxGaQXYn2Ma-pj4qVyYaDU6yvG2gVFlAQL3xoYvKja4pZ2C6urI746xb91LgoBGQ1DrKQ6Kt5bTpx_8B89vJYrf2YbAwiFMgyL-fGmqU2A-4UPcQdhY-GZMYZzSMG-l1MdOT1xu7wp_EHumeER0baiTOtGbwRTw5tLHH84LY-PhFM60q2QuyexYQPeeKRSi1mYt73f-md1Xm0ntrX4nMMlA-SJGhs8RbdofgIj3jlQhgn_XjsUfQeGylGBwlQ4KrGbWRWPqQwfzwuTS8QdTKwdXXDUdLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارتش اسرائیل، منطقه میفدون در جنوب لبنان را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66307" target="_blank">📅 18:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66306">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecc0108dd2.mp4?token=uopEloqL91vYqNZZjAPVUKXM7B2J8pifAacl9K_ftNkZhx5oP1ZKftfBz8fPcr1nVokwNOWcJ9gJHBaQJmG8MlyQK7TWfWLUhLZ9fmdFIAL6EODOJczWNGd6hAJRlVjrf3jErUXPy2dSClzpBeQvETlzqTQQlM4EOHhE1e9s1hNcnWjMc3F-P8ndOSXOxealEk4UcLh0yfJ3QNxS9pNFoWWThoq_apYAR9KEMZ_XbhZY7AhIFfH1Qgwtc38eDFRxMfHmSyvYK22fZs1x4hYZdsIBdDahFgbyx5i0_k7_VenFoCVsz9Vj3CEejLMDHmhUAYD0gfVYsX9C-49rO9c3pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecc0108dd2.mp4?token=uopEloqL91vYqNZZjAPVUKXM7B2J8pifAacl9K_ftNkZhx5oP1ZKftfBz8fPcr1nVokwNOWcJ9gJHBaQJmG8MlyQK7TWfWLUhLZ9fmdFIAL6EODOJczWNGd6hAJRlVjrf3jErUXPy2dSClzpBeQvETlzqTQQlM4EOHhE1e9s1hNcnWjMc3F-P8ndOSXOxealEk4UcLh0yfJ3QNxS9pNFoWWThoq_apYAR9KEMZ_XbhZY7AhIFfH1Qgwtc38eDFRxMfHmSyvYK22fZs1x4hYZdsIBdDahFgbyx5i0_k7_VenFoCVsz9Vj3CEejLMDHmhUAYD0gfVYsX9C-49rO9c3pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ:
ممکن است شخصاً یک کنفرانس خبری برگزار کنم و متن یادداشت تفاهم میان آمریکا و جمهوری اسلامی را با صدای بلند بخوانم تا رسانه‌ها آن را به درستی پوشش دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66306" target="_blank">📅 18:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66304">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLoVgv0HVtE1DWwZ-djngEedjLlJajMI5p-3RAr_C__-DSbW_hwERaCSzoRMkjBNrqCJWa3frpPXLfzwkPzHcSowPboLwrkkUcNcItYHpsRMXN2AoLLYuXRcEXcudZ1k-aH8_1bnRBlzaua3eH-hypTqZJlrw3VElcvlOJiH9z0lesYM8lnpAQ-EkITkAJj5TlbQkwhbQkoUGTf7WI5uz7IxwKK-1oxwEiTgX2ylN3LWEQJ0W1ya6Ndl7dt2h5Gefb53oMcw5S2mvz-NiZNFMCvtzcxHWHQJsPlyNmnp1u6RYU95sLj3aIGR36sslxbQs5xZ8IcAVIvV7CgtzjqxKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وزارت امور خارجه سوئیس:
قرار است یادداشت تفاهم ایران و آمریکا روز جمعه در بورگنشتوک، در مرکز این کشور، امضا شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66304" target="_blank">📅 17:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66303">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miLWGm0eXbP0i5zP_Cq5WymsSIR7470LiM6LSCI4mUt7_IdqWyjPniQXAfmYnAw0wBVm2amx9J0_kgCzCwhBKBlAGzAy3G5XBPP2WXDfeEBENWyfpjGyAXGhq7rLFeX4FfLADH7Z39hs6IKxHgSAKG7Fmr3ii4zVdfQiF7IJYlU2jxQjr-YNnuJQQWwlcWs85Fk0FJ26A0HxHIHSMcanAM9grzYlzA75Vbmvqf34MSxzr72wLefMaKvE4r_yBbloJZGTLbheaCbe-ms_tcV5QlvzMDb3vzlTonwb0kevMgma6YZuAh2uWggE6O8wv50ezSbSGb0urNLyNSgB7cme3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر تیم جمهوری اسلامی که آمریکا و اسرائیل ویزای جهنمشون رو اوکی کرد.
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66303" target="_blank">📅 17:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66300">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d1538e700.mp4?token=q05b_JiGenz-9FJU0uReMStF93Ob0ifqR-hrpPmMKvnhzgKsY9DXBDJISwKw0uLotI5p6BlBwAvBpwNJovVGTLv4WIOCNnFQl6NKySAQBXCMYPi2Vtr3cLe72z8JWleytiOIgfgR7zgfFYJpYr4sedTTinNd0uFnMnScVM_2NYnNHSc15rkxxjA_YxVcONTglhMhJwUwxNLfCTcPmaFoSAGQ0MrcK6BtTbWiz-cI9fmvOXoTizVDSyyCVQbJeYuaAZ3MSlAneCemfn0gnE9RWZUVtqU8GEL5fthvKJHOC9jn928-KzLR-BA3Bmd5pvTevwOcIvyNRHX686BW1h4Qzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d1538e700.mp4?token=q05b_JiGenz-9FJU0uReMStF93Ob0ifqR-hrpPmMKvnhzgKsY9DXBDJISwKw0uLotI5p6BlBwAvBpwNJovVGTLv4WIOCNnFQl6NKySAQBXCMYPi2Vtr3cLe72z8JWleytiOIgfgR7zgfFYJpYr4sedTTinNd0uFnMnScVM_2NYnNHSc15rkxxjA_YxVcONTglhMhJwUwxNLfCTcPmaFoSAGQ0MrcK6BtTbWiz-cI9fmvOXoTizVDSyyCVQbJeYuaAZ3MSlAneCemfn0gnE9RWZUVtqU8GEL5fthvKJHOC9jn928-KzLR-BA3Bmd5pvTevwOcIvyNRHX686BW1h4Qzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنگام بمباران بیت رهبری هرکسی که اونجا بوده کشته شده جز مجتبی.
مجتبی همون لحظه:
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66300" target="_blank">📅 17:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66296">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TBftsF6wvgK5yDMQV4Ic6qSb2gOk5rCQoA9y4myNXx-NWafrW2QI2KMExzfMSCfiyBPG1VUebGxSxvMtodQvmKlyyndI0zdXYQCr4ShETlj_hK8WIhVYicyrr0AkCc6RPSRkvQAXQKTnptdMvG8cctE2h1opD3RvAO7eSOU7OZKeiOfmfWdqtN0udavKEF2xzhfuTjUxTgQcU-RVKYDuc3yHCNe0yWtY2Kw1LG5ka4ppr8HF-NsVggJ_W5CstZ_deBlwChjv7IE5JyOTia8UfRgyq2W6qZKbPEk-bYrdPyAbIdgOHo2qhkOEi7ReUn9trcrBCIAac0TFsmD6V2GmlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U98MDY5CU92BSt2w8h1EACrLHeCsO4rJvSRTpGF1sZ-yGA4BUOfaKqC7STLQBnAB0XZvRHro6WUqGVuJFlQ8QGwBMUkIuNmtcK5voo5ReMcATofrizV88b3uC6kOWzL8TLHk52cW-BO5qXnfIl9iy3Dld_FCMk2Q_6oVchPAkgKPAN1k4aBzM70rsP3I5wNtyPQcxAH4m7CMT39pN6DFUSLKKLeTMasEHXoFVyVj4ROI4dHFBNtuySZHEqJadVRz3Qe4_aCS69dpOFo6ty8S9aOO0FDCzBjFQ2lu9iGhks_KsI5yVm0Xntp6u5DasgNHsjTM8xHIgbHh4CcvM8ulsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tnCk3-SE9HMTiho2xTvOjcKpVMrcPnfVy9UmBJQuiMnNXyX_f5ppm9sm4Y_yQvCsv-Jw0Jq9mGw7RHCM6Z91zTVh29ULA6qzLp7Tyc7Z5zghhiDMUVKi6Vwq8Pwb337PnEtSoNTa6ar2QOj8twXYnpZnRVxO8PZfMRqkN2aqkoVtsidq5TYCPpuAhKmrzv92pAYIwFT8Q1_LJYEaRB-cQUnFkl6A2PpWArltavLKUTCjfYtkz8lYf1goEViDzuciWwnwXrf9AmFB17imUGlcllwwsjHKWVtz6azitqaoNJAzBw7fx3wAJt7E_NeUlT5hV-DrZCxq1_zozNqiH7vrVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aUndeL7sGXnJqWJP8umMHQWcjrWlV6t0gFOpAR97G-fQNw0EgNPWVT1IX_R-6Wzg9bMlC4NEFBXQfb7VigfiX41FuFeHE42c2Ha1x2uGvvXS7YYhJeHFRMlRYE3Yjh0PLcyyVezBzjpa9HKGbD2lswHTF-y5oZbjnUECFNH-HcqLRTaw9kHwxAPsHfyVEi3_Q4_xiVsTosfgcGTezMVI-GrWurM7arJsDmXf1zKthibCK6MIw73Btj6bellSex8qwCszSTLu7ih_WAedgH1o1Y9Oi0ePxYQ-zafdi80vY1El0DFguGDhSenPp61EDOqgvwqZCTpEJH1idM7HUqgPMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ویتنی رایت پورن استار مشهور آمریکایی دیشب در استادیوم حضور داشته و از تیم جمهوری اسلامی حمایت کرده
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66296" target="_blank">📅 16:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66295">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c34b0ffff.mp4?token=tXEa5TAMdKOgx07-F_RaiiCaXu5G2THLGTarCEMxB6p_zr1A82jbX7C_qXCyAl9QvfxvXQ_Lhh97C4zAE-dzr_ul02iBdLbQsJ4ShcMgPq5FwkUaTEKa2sReVqberS6c9UQEsYT5q_dD2KD41oMhQpIBuQlrgxsT8W_Hhhkk1uZ-LhjvHJQ42wflA8_RB5bATVjiBCa68m6oKUIKDzTpp1hDpeYljqMUrjtjz6koboexbOZ4SxS1wjMttW_INt9v5bv4ne3OcqXmGJ9WpS6931FhP19AtXsWpOC_kl3Hu4nr1GKXR3BwdrI1-kSN-cFDgWojU2TsCqHTM26Ns3iM7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c34b0ffff.mp4?token=tXEa5TAMdKOgx07-F_RaiiCaXu5G2THLGTarCEMxB6p_zr1A82jbX7C_qXCyAl9QvfxvXQ_Lhh97C4zAE-dzr_ul02iBdLbQsJ4ShcMgPq5FwkUaTEKa2sReVqberS6c9UQEsYT5q_dD2KD41oMhQpIBuQlrgxsT8W_Hhhkk1uZ-LhjvHJQ42wflA8_RB5bATVjiBCa68m6oKUIKDzTpp1hDpeYljqMUrjtjz6koboexbOZ4SxS1wjMttW_INt9v5bv4ne3OcqXmGJ9WpS6931FhP19AtXsWpOC_kl3Hu4nr1GKXR3BwdrI1-kSN-cFDgWojU2TsCqHTM26Ns3iM7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استادیوم فوق‌العاده زیبای مرسدس بنز در شهر آتلانتا در آمریکا میزبان بازی های جام جهانی
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66295" target="_blank">📅 16:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66293">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pseE5vKB2BiamLEj6WIj3G-YGkJmamaTszmGTFed79i6NYRqY2AP-LitqMsKR9lVz4reqjE1pn21vHTqAqU6dafiSd3TXvTsrTeutHfA1LRgzDA4lb6Wk44J4q7l5ffaY6oUo2KTutWCCbaAwEuFiTeXea3fgDX1uEGHJMRpcAYD7gFjH8BA8CN6VHXyideLZjlhwGIUT1yaCP7ulST68G4p58G1anQC2lBRjbsM96-gSvRiA44uPaVFQct_OU8W6-hKH3suWTvUQnq1IehzamcwjnMgjdpalaiJQuTA1On7UjVvlrnewRfeCySH6C88PBMyIQV-nUDuJOpHa1L7Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
جمهوری اسلامی هم‌زمان با امضای تفاهم‌نامه‌ «صلح»، دو تن دیگر از معترضان ۱۸ و ۱۹ دی‌ به نام‌های جواد زمانی و ابوالفضل ساعدی را اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66293" target="_blank">📅 15:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66292">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52f8c1feb4.mp4?token=lOLyHcwSlrfvloaq8vuUUxKjV4CywN0KdmSwOI_V75axiBIX84TySfx7cwL2KgVLd2A-29r4HhZ_gw3vs3sS9hYN1Zbe2GMuvpq1STavzHglMMbpbvkhOAdLuPpSlv-C_I78VDC7cM1maTTzV_bRe3g5B7UeefOHMHhtuplr4YreFrxqgiYHOhqvYq5-q1-07-coDFGtpaF3G47hQIW97YROrCGVI0zNAjKnNm5ccD8lLOv0I_8CzyeLIYzQVuRc0UXC6jLj7uDoJgHeX7jWRt7tOpbhdZe_qXA0RrUf5NcNr2Wd_VZ3yzjWihxwK2-DwXWu5HZg6QRBrc_l0BSOtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52f8c1feb4.mp4?token=lOLyHcwSlrfvloaq8vuUUxKjV4CywN0KdmSwOI_V75axiBIX84TySfx7cwL2KgVLd2A-29r4HhZ_gw3vs3sS9hYN1Zbe2GMuvpq1STavzHglMMbpbvkhOAdLuPpSlv-C_I78VDC7cM1maTTzV_bRe3g5B7UeefOHMHhtuplr4YreFrxqgiYHOhqvYq5-q1-07-coDFGtpaF3G47hQIW97YROrCGVI0zNAjKnNm5ccD8lLOv0I_8CzyeLIYzQVuRc0UXC6jLj7uDoJgHeX7jWRt7tOpbhdZe_qXA0RrUf5NcNr2Wd_VZ3yzjWihxwK2-DwXWu5HZg6QRBrc_l0BSOtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
انتقاد ترامپ از روشی که اسرائیل در لبنان به کار گرفته است:
لازم نیست هر بار که دنبال کسی می‌گردید، یک آپارتمان را خراب کنید.افراد زیادی در آن خانه‌ها هستند و می‌توانم به شما بگویم که همه آنها حزب‌الله نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66292" target="_blank">📅 14:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66291">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db26cc81b.mp4?token=SCxoxAoPtgLfjGF0FiC557stusNANo38-3XClkthpD2lsUSHi3x2zjG8CXGjKW1v3OlHDepK7RJjgGkcD3Z2ZiK1QUMue6h9RuxRbvTXuPNAebFSdxxW8gbPcpq7VoLsoqA4hfCL5fIhHayf4y_C4-IieDsuHSJQH-mlqx42FZdKaru1Dlh-ImLi8rFjABDsZYpX3dD9TLz4r79G1oWSYtcDUHSzo8ETH-WAhr2xwY8CmeVd_r-A7F4nkD5HCDta4vVXoeJRzpsdXX1wRhTNzJP0PWqFSG9_5aOapigmqLpCZeQE-C8twpfhjuDCc1J8jIb0keNW517hM7N1LYMXrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db26cc81b.mp4?token=SCxoxAoPtgLfjGF0FiC557stusNANo38-3XClkthpD2lsUSHi3x2zjG8CXGjKW1v3OlHDepK7RJjgGkcD3Z2ZiK1QUMue6h9RuxRbvTXuPNAebFSdxxW8gbPcpq7VoLsoqA4hfCL5fIhHayf4y_C4-IieDsuHSJQH-mlqx42FZdKaru1Dlh-ImLi8rFjABDsZYpX3dD9TLz4r79G1oWSYtcDUHSzo8ETH-WAhr2xwY8CmeVd_r-A7F4nkD5HCDta4vVXoeJRzpsdXX1wRhTNzJP0PWqFSG9_5aOapigmqLpCZeQE-C8twpfhjuDCc1J8jIb0keNW517hM7N1LYMXrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
در توافق من، اگر ایران به سلاح هسته‌ای دست یابد، منفجر می‌شود.
در توافق اوباما، به آنها اجازه داده شد که سلاح هسته‌ای داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66291" target="_blank">📅 14:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66290">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaeee1ba07.mp4?token=Mv0NOENn6CKRp_dhkczJiITy8Z9qDDK43RzvqpG0cDno8JI0AI_G4f023r-TKvJ6d2UNgBKJ7vlrYAWHXx0BhjZ5XEiozay7MCAfLpTCOwvvz7tN3YE2_RSdycsSeFpI6ef3FTrz82C3iQ06psq5i0kwBYP-6OLyehn8-liWHa2WbAI1kpgHx2_zatzi2A_FIXNkXX514VJpEMIXyVFzRV-DRaRgMjg3IoWwQUa3ZqNcoCZdXoiK3UTG2mNqHfDihKQfoA0jyKG5sc8MnjhWZzJqEJ87YyUk3oeTf7VznGXhuiImLbIyGZTsUHAjNPtbdlJxh8yi1Dl3R41egaCwDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaeee1ba07.mp4?token=Mv0NOENn6CKRp_dhkczJiITy8Z9qDDK43RzvqpG0cDno8JI0AI_G4f023r-TKvJ6d2UNgBKJ7vlrYAWHXx0BhjZ5XEiozay7MCAfLpTCOwvvz7tN3YE2_RSdycsSeFpI6ef3FTrz82C3iQ06psq5i0kwBYP-6OLyehn8-liWHa2WbAI1kpgHx2_zatzi2A_FIXNkXX514VJpEMIXyVFzRV-DRaRgMjg3IoWwQUa3ZqNcoCZdXoiK3UTG2mNqHfDihKQfoA0jyKG5sc8MnjhWZzJqEJ87YyUk3oeTf7VznGXhuiImLbIyGZTsUHAjNPtbdlJxh8yi1Dl3R41egaCwDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
گروه اول و دوم رهبران همگی مرده اند.
رهبری فعلی ایران افراد بسیار منطقی هستند. تعامل با آنها خوب است؛ آنها افرادی قوی و باهوش هستند.آنها رادیکال نشده‌اند و به دنبال کمک به کشورشان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66290" target="_blank">📅 14:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66289">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/059a9cad8e.mp4?token=SUPboFWq5izbUMpuncbns4D10QFL-N3jMe5EYT6v9dkDVrOeLNXeBtwfRcvRTrSHoGEFqENXYeYO7vVFWBgbBK7QpuvkdJZsCKcKXRK2eFeuU07kXlBjKSomt7Ew1o3cVuAXcSetZifWfa7UAHQsNEehf1uXtpg-0XoUFFJJ5nugh2ikKAWytpOQzmkHmswtSreQCt8M_CJaguIx6isq9GsyWwaOThBX2yxtsrSGT4X1Kw0SSkPFHcUeFh6sUs825ikjg3va-EHJWRqL2HRk93FURZ9h0pnLqe8DBlY4XDs2Lkp6n6zHdRd5v0o4eC1cIOyq-HomSJ959woobuKbSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/059a9cad8e.mp4?token=SUPboFWq5izbUMpuncbns4D10QFL-N3jMe5EYT6v9dkDVrOeLNXeBtwfRcvRTrSHoGEFqENXYeYO7vVFWBgbBK7QpuvkdJZsCKcKXRK2eFeuU07kXlBjKSomt7Ew1o3cVuAXcSetZifWfa7UAHQsNEehf1uXtpg-0XoUFFJJ5nugh2ikKAWytpOQzmkHmswtSreQCt8M_CJaguIx6isq9GsyWwaOThBX2yxtsrSGT4X1Kw0SSkPFHcUeFh6sUs825ikjg3va-EHJWRqL2HRk93FURZ9h0pnLqe8DBlY4XDs2Lkp6n6zHdRd5v0o4eC1cIOyq-HomSJ959woobuKbSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: رژیم ایران همچنان به کشتن مردم خود ادامه می‌دهد.
ترامپ: بیشتر این اتفاقات در دوران رژیم اول و دوم رخ داده است، خیلی بیشتر از الان.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66289" target="_blank">📅 14:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66288">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b6ac4ffe1.mp4?token=KBjpGT7_bpcrbARbsmKyhs8TXAIB5esmvbKfFtsGwc3c4HWiFsN-GzlxmNJEu9zjXPePp4R8kLoZcImHTw2h5natrYsYId1es4Q9CdVvh1nJJqwrvCT-w2Q9Z1NOSQ-FMcP-XQhvCDCf2Q1s_MwYhUC5Dn5qRP8OGYbG4PC1pUnkC7wVca5zv9SkLTCnlh8HSX3kgTazQ2fGEOCSSQozmG3rXV-Zxgd0uUQbImmmgN2xaCarMSYU6H14cPg0fe7Lq6Hr8Vu0n8pvHYgnRAXyPFmplUupkUC8PvJrZC5HEyJ3H1i4fayrRcK96GTLIs86oLz4Dz7tPB9lP3OSRcgdDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b6ac4ffe1.mp4?token=KBjpGT7_bpcrbARbsmKyhs8TXAIB5esmvbKfFtsGwc3c4HWiFsN-GzlxmNJEu9zjXPePp4R8kLoZcImHTw2h5natrYsYId1es4Q9CdVvh1nJJqwrvCT-w2Q9Z1NOSQ-FMcP-XQhvCDCf2Q1s_MwYhUC5Dn5qRP8OGYbG4PC1pUnkC7wVca5zv9SkLTCnlh8HSX3kgTazQ2fGEOCSSQozmG3rXV-Zxgd0uUQbImmmgN2xaCarMSYU6H14cPg0fe7Lq6Hr8Vu0n8pvHYgnRAXyPFmplUupkUC8PvJrZC5HEyJ3H1i4fayrRcK96GTLIs86oLz4Dz7tPB9lP3OSRcgdDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد گرد و غبار هسته‌ای:
شما می‌توانید این استدلال را مطرح کنید: چرا اصلاً خودتان را به زحمت می‌اندازید؟ چون واقعاً ارزشمند نیست.اما فکر می‌کنم از نظر روانی، ما می‌خواهیم آن را به دست آوریم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66288" target="_blank">📅 14:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66287">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77169efe09.mp4?token=LwxykaCJJlbXeZTHyKLXYKqOw6LR0KBDo_pVUIQt9YVZOU_TMrqZinpAAtcCJDagJksyyGLfyhdnqH-kuT4Iy1xUaoz9rmdRboBjMoT-7d2cySq2xVudDNHBSj9JJEWuOf9VkTFIAwHU2568iMBCYXw7HKO2wLisZBVGId20bNWj1WUoF8WRFpAZ6daqXQIvTaY88BbczBXzdof2WcAJPwFpBjKTyq_hZhwlws7Ep2qY_o0534kBXxTtWWlX2SEgwq5Jdf0ZIzNSLZYthXwLwbPVxbq4hrlkQW4lkn8VSCI9jAa8UOcLUR-BHy-8VtRbbjRM4GALrZAbR3bfUWdGVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77169efe09.mp4?token=LwxykaCJJlbXeZTHyKLXYKqOw6LR0KBDo_pVUIQt9YVZOU_TMrqZinpAAtcCJDagJksyyGLfyhdnqH-kuT4Iy1xUaoz9rmdRboBjMoT-7d2cySq2xVudDNHBSj9JJEWuOf9VkTFIAwHU2568iMBCYXw7HKO2wLisZBVGId20bNWj1WUoF8WRFpAZ6daqXQIvTaY88BbczBXzdof2WcAJPwFpBjKTyq_hZhwlws7Ep2qY_o0534kBXxTtWWlX2SEgwq5Jdf0ZIzNSLZYthXwLwbPVxbq4hrlkQW4lkn8VSCI9jAa8UOcLUR-BHy-8VtRbbjRM4GALrZAbR3bfUWdGVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
ایران حتی یک بار هم به ترکیه حمله کرد. من هرگز نفهمیدم. هیچ کس قرار نیست بفهمد.
مشکل این است. آنها افرادی کاملاً غیرمنطقی هستند و این افراد اکنون رفته‌اند.
من فکر می‌کنم ایران اکنون رهبری منطقی دارد
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66287" target="_blank">📅 14:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66286">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5225dce7ab.mp4?token=qnuNtGh6Xr1ZZ5jjUdXNDDMBfX4dh6GxcNC04cQhRTJ8zb1rF8IhgkwOeylJ1XyoSLMXSP1avEL5rDKfsryRwsYU5jP4W1AzxRkuXEKiojLm36mIfDgu7n6ply22ZgAR6ejhvhovxwBkPr8aSvXXshak-ZZycMjX3lQYeb-gc6gjektwV4iK-O4s6VR2MOE5Tvbxk5W54b3ryhRZnUK2DM-Q-ywK_oQ4xhTbpiBOj-z3Z75O6P14oq8LkHHJ9wey6Iht2YrdThohNWTR3urD2fZsKbROutLARVeVXUXVYw2_6S1QT0_EwBk00KWZdMkAzfNYE_2STPE8rFhmju4zrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5225dce7ab.mp4?token=qnuNtGh6Xr1ZZ5jjUdXNDDMBfX4dh6GxcNC04cQhRTJ8zb1rF8IhgkwOeylJ1XyoSLMXSP1avEL5rDKfsryRwsYU5jP4W1AzxRkuXEKiojLm36mIfDgu7n6ply22ZgAR6ejhvhovxwBkPr8aSvXXshak-ZZycMjX3lQYeb-gc6gjektwV4iK-O4s6VR2MOE5Tvbxk5W54b3ryhRZnUK2DM-Q-ywK_oQ4xhTbpiBOj-z3Z75O6P14oq8LkHHJ9wey6Iht2YrdThohNWTR3urD2fZsKbROutLARVeVXUXVYw2_6S1QT0_EwBk00KWZdMkAzfNYE_2STPE8rFhmju4zrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگن مجتبی تو LA رویت شده
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66286" target="_blank">📅 14:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66284">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rLT-AdiLGMpJDwjfjvfg5fZRtdjDE3dd1ymRIYHCeFeR_7p6zHbwizF3EIKc6aU2tWVIfQKYaucNsA7ibeJ9dJZemsHfGHSCT45iejADBwXm-_14y-HSMf3CbZWC3NKPls4YvqO2KYky2eVr2SohvNRUdq24hOhpo3l6ph3gd1gFw9uHiRBWq-Ym1eaJM7LkpsEDDcno1YgW8oa54fRpMI3zs9NKttOSaHVTWRtf1gaj3BbD-Ur6ETTnKJl_bUbtUxWBFttc8RGCZCoxqMSYdby5QhC3cmEIEIgQ888l9fkVBg8v2H5nz5ejbQhQtw5qNwJLkZxxIsL84lOXkBZZFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uEsjtFSN6qMAJcImOoTjK4eXOi5hNK8ffJD_WkJ1WVP-yJAvMHF2ctv4vrfvfufdHKE_EkxsraMz7EH--xxxu56cGjk9dexPTChARCwZio_25x8KQgIw0vrA0tNZqtvh5vdWxKMsJXOQS5lbMvnL91HhCOSsxiyc-_ZWXIWZWnP9welRbDXCzxT_m9QJyoZqXAQM7cah6sS2zuTwZSRbc51pMgv1wW9sty8iPHM5UFI9Dm1CIA-HRjh_3ZaRwAUgXM_oBijy5AqUo4mXd-elC-39Z3oy57HhF0xPj6357WgVsFt5HnnjUHdxCV-1tXbIW2vm2-QmJAkDN67eHs44ZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
برنامه جدید امتحانات نهایی پایه های یازدهم و دوازدهم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66284" target="_blank">📅 13:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66283">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
ترامپ:
من به اسرائیل پیشنهاد دادم که سوریه مسئولیت حزب‌الله را بر عهده بگیرد.
جنگ لبنان مسئله‌ی فرعی است و توافق هسته‌ای با ایران می‌تواند پابرجا بماند.
به اسرائیل گفتم حمله اش به بیروت برایم خوشایند نیست.
نتانیاهو اکنون باید در قبال لبنان مسئولیت‌پذیرتر باشد.من از نحوه برخورد اسرائیل با لبنان و حزب‌الله راضی نیستم.بدون من اسرائیل وجود نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66283" target="_blank">📅 13:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66282">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
ترامپ:تلاش هایی برای تغییر رژیم در ایران وجود داشت اما موفق نشدند.
اگر ما برنامه جامع اقدام مشترک اوباما با ایران را لغو نمی‌کردیم، ممکن بود این کشور به سلاح هسته‌ای دست یابد.
ما می‌خواستیم برای گرفتن اورانیوم غنی‌شده به ایران برویم، اما این اتفاق نیفتاد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66282" target="_blank">📅 13:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66281">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
ترامپ:
توافق با ایران به مرحله دوم منتقل میشود.ما یک توافق منصفانه و خوب با ایران داریم، اما هیچ پولی در آنجا سرمایه‌گذاری نمی‌کنیم.
چیزی که مرا به امضای این یادداشت تفاهم ترغیب کرد، تضمین این بود که ایران سلاح هسته‌ای نخواهد داشت.
چیزی که برای من مهم است این است که ایران به هیچ شکلی سلاح هسته‌ای نداشته باشد.
اگر ایران به دنبال سلاح هسته ای برود جهنم به روی او گشوده خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66281" target="_blank">📅 13:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66280">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b4a7171c.mp4?token=p2bO6-EfRwQ8vZikVZh7mEvVgUimlC1uFOoMqA4XUn6H-cbxCzim3MFyL7SaO-8y1YWkzHa6U4-4DmVyRevpJsxkRz2Ez0o1V4OSlQ85fajZJOZ-MS3sNvjEvyEugx5F0OfL2WUam_SgMw7ZxHK_ADz16ZepomyDRSJrT0prbrXHuM8R449fac2gIiJdqYgHZBXt3j3Kxtn9OzUvqgnAiqXa2_iJfos4giIGKHz3wCgr4iI7BwYxnGlz-HZ8MmIDeAfu1KOWoClCb2br1q8K_XS05WhhCx61H2U6KVIk73u2kTvCb6v76x9McJ-v_8wPFAlvxphUm_WeJvkfGTkLOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b4a7171c.mp4?token=p2bO6-EfRwQ8vZikVZh7mEvVgUimlC1uFOoMqA4XUn6H-cbxCzim3MFyL7SaO-8y1YWkzHa6U4-4DmVyRevpJsxkRz2Ez0o1V4OSlQ85fajZJOZ-MS3sNvjEvyEugx5F0OfL2WUam_SgMw7ZxHK_ADz16ZepomyDRSJrT0prbrXHuM8R449fac2gIiJdqYgHZBXt3j3Kxtn9OzUvqgnAiqXa2_iJfos4giIGKHz3wCgr4iI7BwYxnGlz-HZ8MmIDeAfu1KOWoClCb2br1q8K_XS05WhhCx61H2U6KVIk73u2kTvCb6v76x9McJ-v_8wPFAlvxphUm_WeJvkfGTkLOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
هادی هوتیت، خبرنگار  پرس تی‌وی، وارد منطقه‌ای در جنوب لبنان شد که نیروهای ارتش اسرائیل هنوز در آنجا مشغول عملیات هستند. فیلم نشان می‌دهد که او در جریان این حادثه مورد اصابت ترکش قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66280" target="_blank">📅 13:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66279">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b685347f.mp4?token=p9xY8eigRWrlAPPc7Jago8iBRT_3UAg_dABMlaFCd5Qrrfn21l5BaNub1Z3aBoMNkcy4LqA-Vr31xvSFoe_CQtORbay_qm8GRsi2hIdENDJX0MMDJT63AyRE3w--BAc3D-pikSsIf5Y_FbnZ9H5k7PT833JurFgTcpUGJai2aG2H3o2rlPspbZFodBaWu3jGKE7d40P9cap2SZFnFFhj0FJ3oHKmN5FGWKsvHRYxG8IHkHD4G94jKbuKD8qtbm_s5gLqj-w3qx9Ux41G2VD57kdwTxT4leJ8PPosGq89dHBBWfePay8w-TTn5o8ZY3fWITcDwIrQYr8kZ-CpH8aQ1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b685347f.mp4?token=p9xY8eigRWrlAPPc7Jago8iBRT_3UAg_dABMlaFCd5Qrrfn21l5BaNub1Z3aBoMNkcy4LqA-Vr31xvSFoe_CQtORbay_qm8GRsi2hIdENDJX0MMDJT63AyRE3w--BAc3D-pikSsIf5Y_FbnZ9H5k7PT833JurFgTcpUGJai2aG2H3o2rlPspbZFodBaWu3jGKE7d40P9cap2SZFnFFhj0FJ3oHKmN5FGWKsvHRYxG8IHkHD4G94jKbuKD8qtbm_s5gLqj-w3qx9Ux41G2VD57kdwTxT4leJ8PPosGq89dHBBWfePay8w-TTn5o8ZY3fWITcDwIrQYr8kZ-CpH8aQ1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمدرضا شاه پهلوی مردی بود که دستش نمک نداشت
👑
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66279" target="_blank">📅 12:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66278">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
عراقچی:
ما واشنگتن و اسرائیل را یک طرف این یادداشت تفاهم می‌دانیم، در حالی که ایران و حزب‌الله طرف دیگر را نمایندگی می‌کنند.
پایان جنگ در لبنان بخش جدایی‌ناپذیر پایان جنگ در ایران است و شامل خروج اسرائیل از خاک لبنان نیز می‌شود.
هرگونه حمله نظامی اسرائیل به لبنان و ادامه اشغال، نقض تفاهم‌نامه است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66278" target="_blank">📅 12:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66277">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d988cc6faa.mp4?token=afO-56ahvI6oR3uHjKVYGJu-5tp_U0eGFQvwDDlQovknDNRCyEHdpv0zNhvvRasmJzdYmqdX8WLaL6CtVMtw4xF_NatVt6SMZlSOiQTWq89oL30Jp7JRFZ3UzoA0DQwC6dE2GPr6I1x1QDwmz6iFqfpd7IDfT8DJ0sJ_qnwkq1wP730gcGjAf252QlJ8J9Rszf2B31k0VH2RFXckDNdzcWzt4Taw2-xlf1kkRn0scZLrrTT-Cwm2luaygbR6AT9r_3RWbbPTQQ0OtaEmV_mjgNhM_yCbGcITFl2wuZoKbDXq_3yl7U49V_sazTJD-eyDtaIufRGNwqfNeiq0Br1QXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d988cc6faa.mp4?token=afO-56ahvI6oR3uHjKVYGJu-5tp_U0eGFQvwDDlQovknDNRCyEHdpv0zNhvvRasmJzdYmqdX8WLaL6CtVMtw4xF_NatVt6SMZlSOiQTWq89oL30Jp7JRFZ3UzoA0DQwC6dE2GPr6I1x1QDwmz6iFqfpd7IDfT8DJ0sJ_qnwkq1wP730gcGjAf252QlJ8J9Rszf2B31k0VH2RFXckDNdzcWzt4Taw2-xlf1kkRn0scZLrrTT-Cwm2luaygbR6AT9r_3RWbbPTQQ0OtaEmV_mjgNhM_yCbGcITFl2wuZoKbDXq_3yl7U49V_sazTJD-eyDtaIufRGNwqfNeiq0Br1QXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایرانیان وطن پرست سنگ تموم گذاشتن و اینقد پرچم شیروخورشید زیاد بوده که میساکی فشاری شده و پرچم جمهوری اسلامی نشون میده میگه این پرچم ایرانه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66277" target="_blank">📅 11:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66276">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944350c2ea.mp4?token=F8UHo_YxcuCIAX-UE_Gu8a-wv3DjVno4a723Nm5dxm9HPs_JkuKpzZZyMVi0e2f2HAhcZBWLphEskpXNgaJ2pmruzTBTdexeefUbAnZ0OGzK_F3jPws0MHAIAom_bchr-jW8Cqnlb1B62SXDFcyJsFydNrXZPHeADruGDGzivivb3GSs5RfrcaD9nGpC9IgLnaqcT5K7NXdfUs4lT1Wf_kQDyYF5vok5Y18Y6cpp9yTrB1OHsV-JUcIfkvVh8IQVybCv0AGQJDvH-IQ2J8Se3exY1O5tmkVUf_el6IN7eXFsbDiRUy3LHgFLDE38xdOAVnriFSSSpK5w_DAjiCT4VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944350c2ea.mp4?token=F8UHo_YxcuCIAX-UE_Gu8a-wv3DjVno4a723Nm5dxm9HPs_JkuKpzZZyMVi0e2f2HAhcZBWLphEskpXNgaJ2pmruzTBTdexeefUbAnZ0OGzK_F3jPws0MHAIAom_bchr-jW8Cqnlb1B62SXDFcyJsFydNrXZPHeADruGDGzivivb3GSs5RfrcaD9nGpC9IgLnaqcT5K7NXdfUs4lT1Wf_kQDyYF5vok5Y18Y6cpp9yTrB1OHsV-JUcIfkvVh8IQVybCv0AGQJDvH-IQ2J8Se3exY1O5tmkVUf_el6IN7eXFsbDiRUy3LHgFLDE38xdOAVnriFSSSpK5w_DAjiCT4VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دلیل سود نکردن من تو بازار بعد چندسال
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66276" target="_blank">📅 10:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66275">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78c971246f.mp4?token=BtqY6orb0QpCbPAOseOveC2_Qfuyecvy-9kO0QujS4dBqk5woLefUDbvbnI-JwP4GXa80oFcuQU6WjL6uiGSNj3TLVxwNqyvc7IoXZdCaVqQIJCfKHH4dyp1vbamP_sJZW-Z378DU_znB1n0KMKYI4pzbIr31DCMHQU-5NuLNaHsOh3f3TaZa7-DCVwJ7hswAjcVTZmpWPiOdaddCq9reBz7k53LL6T9VLTDn_UlDxRQdZ52mQZyOGkDmYgfhVIQ-QqXhKHOx8Jk3xOS5Paapjc6g6Bzuk2zA8OeaEpsLChFnPjfWVq4UE1m1jqZC6ColiU-IAWy-EibPg6jUDuj3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78c971246f.mp4?token=BtqY6orb0QpCbPAOseOveC2_Qfuyecvy-9kO0QujS4dBqk5woLefUDbvbnI-JwP4GXa80oFcuQU6WjL6uiGSNj3TLVxwNqyvc7IoXZdCaVqQIJCfKHH4dyp1vbamP_sJZW-Z378DU_znB1n0KMKYI4pzbIr31DCMHQU-5NuLNaHsOh3f3TaZa7-DCVwJ7hswAjcVTZmpWPiOdaddCq9reBz7k53LL6T9VLTDn_UlDxRQdZ52mQZyOGkDmYgfhVIQ-QqXhKHOx8Jk3xOS5Paapjc6g6Bzuk2zA8OeaEpsLChFnPjfWVq4UE1m1jqZC6ColiU-IAWy-EibPg6jUDuj3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تصاویری از پالایشگاهی در حومه مسکو که در اثر حمله پهبادی اوکراین دچار آتش سوزی شده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66275" target="_blank">📅 10:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66274">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696afa1a70.mp4?token=uw6Q-Vs4SuvPj3okBEDbLMzXr8-VHQtLnIM-FXqg5EgkInyoWLocM693rf5aWStPnGwLGKg3f1Clnu47B56cUEFbHOPBNBK5lSy40sh5C_dh1JB0cC0bPhOH1gJkgA1M-mNKR-SlDjGYyFf3pcEyqDT4cY8QSNec30UktW4VzlaN0GNNfpyEuEc7Nz4XrIVekXle7hwQkM5EwtHTGVXcWkN5oeLTlkgHjs8j5hZ7cUhPxIknSPhjV4ajW9NLJGDijhQNk8T6BBFWCM8zX7CQMpK2YjouqbtF8u07MsSyZcdzQ592H6SfFJjUedkEVIDvvuDWaH2w76TqidcZx97u8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696afa1a70.mp4?token=uw6Q-Vs4SuvPj3okBEDbLMzXr8-VHQtLnIM-FXqg5EgkInyoWLocM693rf5aWStPnGwLGKg3f1Clnu47B56cUEFbHOPBNBK5lSy40sh5C_dh1JB0cC0bPhOH1gJkgA1M-mNKR-SlDjGYyFf3pcEyqDT4cY8QSNec30UktW4VzlaN0GNNfpyEuEc7Nz4XrIVekXle7hwQkM5EwtHTGVXcWkN5oeLTlkgHjs8j5hZ7cUhPxIknSPhjV4ajW9NLJGDijhQNk8T6BBFWCM8zX7CQMpK2YjouqbtF8u07MsSyZcdzQ592H6SfFJjUedkEVIDvvuDWaH2w76TqidcZx97u8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هو کردن هوادارن حاضر در ورزشگاه هنگام پخش شدن سرود تیم جمهوری اسلامی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66274" target="_blank">📅 09:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66273">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f96ea995.mp4?token=cEhsauaOf4KYAwAO2iuniIlHU_rYnBz7odlOjM_NLRfhDMlzA6N0aXO4pLtJZGbQQtS9PnlHQUGiQ1jpN6uYxKWLhvoFae4Xl01WJK4gOE-pGZaZ8nxiN5WY_byeJrN0bd6Am7yDyYS0saZ-zIoSuqVWAAT-PbT9743k0kkmM7GFKRTPAEB-jqWtANwl43xNJb3-gLC-_KNVvDvxB31VS52KjmhJzDDtu7B4Ppn_BJWx_AEtmlACVh12ymm_mLltklg30N-fsWfNOu-o3iSDNHNdxf1gYqk858uHUSpwujYU85nfmaz7W8_7q4UFBlRC7xBoUH35c4I_eFbi1H2P4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f96ea995.mp4?token=cEhsauaOf4KYAwAO2iuniIlHU_rYnBz7odlOjM_NLRfhDMlzA6N0aXO4pLtJZGbQQtS9PnlHQUGiQ1jpN6uYxKWLhvoFae4Xl01WJK4gOE-pGZaZ8nxiN5WY_byeJrN0bd6Am7yDyYS0saZ-zIoSuqVWAAT-PbT9743k0kkmM7GFKRTPAEB-jqWtANwl43xNJb3-gLC-_KNVvDvxB31VS52KjmhJzDDtu7B4Ppn_BJWx_AEtmlACVh12ymm_mLltklg30N-fsWfNOu-o3iSDNHNdxf1gYqk858uHUSpwujYU85nfmaz7W8_7q4UFBlRC7xBoUH35c4I_eFbi1H2P4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ثابتی نماینده مجلس:
عراقچی نوچه و اراذل اوباش آمریکا در کشور است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66273" target="_blank">📅 09:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66272">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSMAaLuz1R2p_dKxt2Wm08nRudH1kI4_Of_69gpVAYDl8jCwh_Hwg11P4cRnRbupO5WUTxQ83Xe7SB8WhlypRHc_DcUFVFpsjvLxe-sIOX8Gax6CmxdJvXq0p3x8BDc6pBjMVnZZxm4ZJ386tsXtAw9ye_9HkIt_mp6pNhmH8HsHp02s7E5x-LGA86Rx4SbjN79PaAD73N8Prw2II44EwnTcgJNeP90TJ840uvig11MniqDZX0GNmsIcUmDoXHGA1vSvPYnizNQw_t3JKDmtbPftj-gWXHpZ9mHWtXebSaxGYl0B22lSmvLqQypauXevXSo5Vs1x7aUmhViVae8uTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏆
پایان‌بازی
🇳🇿
نیوزیلند
😀
-
😀
ایران
🇮🇷
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/66272" target="_blank">📅 06:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66266">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گل دوم محبی
#hjAly‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66266" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66263">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🇳🇿
گل‌دوم نیوزیلند به منتخب ایران دقیقه ۵۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/66263" target="_blank">📅 05:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66258">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
سخنگوی قرارگاه خاتم‌الانبیا: گل زدن نیوزلند به ایران قطعا بی پاسخ نخواهد ماند
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/66258" target="_blank">📅 05:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66257">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پایان نیمه اول
فرزندان برحق وینتون روفرو ۱
کاکولد های گروهبان قندلی ۱
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/66257" target="_blank">📅 05:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66255">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یه حسی بم‌ می‌گه بازی مساوی تموم می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66255" target="_blank">📅 05:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66254">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🏆
گل‌تساوی توسط رامین‌رضاییان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66254" target="_blank">📅 05:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66251">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQoOZVnpA-JFaA8d7mr77XpFtvfQ8XCRjiQ05XE6iaeH6C_9sJtOvRQDzQDN-ZbQFwT7YpytkjYqyU864_Km4cHRjpwmJsR03YIVZxVqQSpPfpwHRoPSGbFoTz6p08fdbXtIcwLH2otZ6VhnH5xLc5iV7L_mIdJuA7YqYHT4qU2jeCfG7zK6eZ8g2ePwIORNzEcomVmYHTfue69m5cZUSJFDSPFEkK5DCQLJVN5pr5AcDeov_XHMAmjOAD0mcXhQaYe2KdMHp09n2VKsIdlr8fo4LcWleMzMce_jEeHmr8nTSaQYJmRlM-MLniz9xzSNoH-xy4v7C4XlTZ775rd-Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظه بازگشایی تنگه بیرانوند
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66251" target="_blank">📅 05:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66248">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🇳🇿
گل‌اول نیوزیلند به منتخب قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66248" target="_blank">📅 04:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66244">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-poll">
<h4>📊 دوست دارین کدوم تیم ببره؟</h4>
<ul>
<li>✓ تیم منتخب امیرقلعه‌نویی🇮🇷</li>
<li>✓ تیم ملی نیوزلند🇳🇿</li>
</ul>
</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66244" target="_blank">📅 04:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66243">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSpJfRnDlS_4Mu_YfaPZbMIC6GcnRsiaEcsi3wKDG9uHMhlAriSi40vNuAtuwGpQK6ZlGjrgMe5h8qtw-UsB_z4ntDk1pprsW69MLvobNGTDwcBLXAFVraW6TymWB3fAMRrpuHLrq0y6N5uDx-O58dz4HBVcK-_IjTpVsTwfUfSSsXu-kg9EnHySbwAg7NVTYYcuoCCK9e6_TUOMJIb37kOc-TIJXqtxjZJ85lNs-ZBWFSP6WYMtAex-1wRQ-iDj8eFNNjy2OI3ou5NBk5fIC4v4iQx_bHLakCs0VnxN-HOOyamjqFit2GFEHz2ayR29xG0r2Rwbk1yffyQBZAJc6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبل بازی
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66243" target="_blank">📅 03:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66242">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حاج علی یکمی تحلیل کن</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66242" target="_blank">📅 03:45 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
