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
<img src="https://cdn4.telesco.pe/file/VWEoZD662VwS5MFA_hdjxbyFzA64jvPeUQxmYjezodCWXIgnK3yNoMpnXAIXsS-USRWlql7-8xSr_EO5TOX9UDLMv8KznbrryFCSHsP_8RBAN3x_KU43GhVufbvbmD6UkSZa6VvTWEYlEZ4QrCZe5NJsVhaoAN7XEvcHsbDpwPZPKXkdMFuUGu0vSxc7pZRtj11SvZiMP-KjfXM7Dm6viNc60YJ3IQAnfwDd_ecO3YdaANLFgvGQ7Ih_3RY3WGsLIdFvWvG5VjdJuywk48_6TJy8rLRKqePBmYJUl9dWa-CWWeFMajSg8COlY1NaGuRlG1Gk21Ef9lUgVzgvqz51rA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 112K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 17:26:02</div>
<hr>

<div class="tg-post" id="msg-71145">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/100451e13a.mp4?token=D-gVyVuEIAa5F6hxO109KZUXmali5OiwemjuyJ458y0vUa9wU9us8h9F00pLiX-u5yKuDjkqIZUMhYDrUlN_LTlStsaufXf0wkxlXyn-emzD6WbYaAHBPlBh1UrMPlI6jBCKnXsj63L_iGUd1D9y_F_Ed-ZdLoDq2a0q78s5N3KH-ER8xYP5Q-9DyE-OTYK8c4jnJ5exEaPGygS2S-CFldnWwWD-dM3c8HjIZei06S2Mihw-CjmIWwPJCqXg_lSKQzD-6AMkSjjeVLEZG5rVUIVthcHHO3U0zJd3lKljWsisHQ7dH482CnXm7cbPC1-GOUwpFsOYO8iZXHLeOOaRgTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/100451e13a.mp4?token=D-gVyVuEIAa5F6hxO109KZUXmali5OiwemjuyJ458y0vUa9wU9us8h9F00pLiX-u5yKuDjkqIZUMhYDrUlN_LTlStsaufXf0wkxlXyn-emzD6WbYaAHBPlBh1UrMPlI6jBCKnXsj63L_iGUd1D9y_F_Ed-ZdLoDq2a0q78s5N3KH-ER8xYP5Q-9DyE-OTYK8c4jnJ5exEaPGygS2S-CFldnWwWD-dM3c8HjIZei06S2Mihw-CjmIWwPJCqXg_lSKQzD-6AMkSjjeVLEZG5rVUIVthcHHO3U0zJd3lKljWsisHQ7dH482CnXm7cbPC1-GOUwpFsOYO8iZXHLeOOaRgTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بابک زنجانی: سایپا را ۱ میلیارد دلار می‌فروختند، ۲ میلیارد پیشنهاد دادم، نفروختند
@News_Hut</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/news_hut/71145" target="_blank">📅 17:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71144">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b09e3df411.mp4?token=W7gmX_WraWsi_7lWnFHAuKJQXKXyT8ZudjnwFj_Xrtd_GgyBTu9e2PBwWgAf9JfH_FZRXW2K023fxUYrbFmIvB208hnzvIlfV6R_PtAvySpi2yyF5qT9_SoX167L_-_-SPCAFLz4qwxfe2gmme6LrztpAnDdFV-IQAxvauaWWlEyXmFF9AuDKTQGGf9U0uWZpHkSWvL0Flmovpmo7_bdEC_Jbgn76Y8uZUlTbq_xEN6m7QWtBOmNv6emD3IWIfA8OEIhUGKszQV0FptxZaWAEZIjYuZT6dKemyxvd8oj6vGwN1nCE_9ZHmwt7KY4OROhlzm92LWmov7WcEa8869fZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b09e3df411.mp4?token=W7gmX_WraWsi_7lWnFHAuKJQXKXyT8ZudjnwFj_Xrtd_GgyBTu9e2PBwWgAf9JfH_FZRXW2K023fxUYrbFmIvB208hnzvIlfV6R_PtAvySpi2yyF5qT9_SoX167L_-_-SPCAFLz4qwxfe2gmme6LrztpAnDdFV-IQAxvauaWWlEyXmFF9AuDKTQGGf9U0uWZpHkSWvL0Flmovpmo7_bdEC_Jbgn76Y8uZUlTbq_xEN6m7QWtBOmNv6emD3IWIfA8OEIhUGKszQV0FptxZaWAEZIjYuZT6dKemyxvd8oj6vGwN1nCE_9ZHmwt7KY4OROhlzm92LWmov7WcEa8869fZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه سری ایرانیا هم انگار توی یه ایران دیگن و رفتن توی جنگلای شمال پستونک پارتی گرفتن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/news_hut/71144" target="_blank">📅 16:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71143">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc463ce6f9.mp4?token=FOvcrYKZLJafR_q_9EqLD9_CIzZ0t_XDupnS363Py5RiZ3yotW4arP0t0VDEn9ogo45wmQqT_amcb8oJEx3odwEU6duf25IbLp5OB4zNGsiXb06JlbolQU1rOhuYxBch5-an8wQXe9QiRvoYuh_-mtZlzX05Bd0pmxya-ShRey7uvbLPgsT_C2ddrDZzeowP8py7nNeyuue24Hled5ynEZ8-B71ARjiuWHX0bxyeIGWs1JENeBLjRXhYtxbqeOOjuByaOHqtrFge6WGrC8bUCiAFvJeulV6XaJqpQvG8rrVG0oiruJqkYWXE6wVB7NzvQhyPPYEzzJEnVcyX-4teiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc463ce6f9.mp4?token=FOvcrYKZLJafR_q_9EqLD9_CIzZ0t_XDupnS363Py5RiZ3yotW4arP0t0VDEn9ogo45wmQqT_amcb8oJEx3odwEU6duf25IbLp5OB4zNGsiXb06JlbolQU1rOhuYxBch5-an8wQXe9QiRvoYuh_-mtZlzX05Bd0pmxya-ShRey7uvbLPgsT_C2ddrDZzeowP8py7nNeyuue24Hled5ynEZ8-B71ARjiuWHX0bxyeIGWs1JENeBLjRXhYtxbqeOOjuByaOHqtrFge6WGrC8bUCiAFvJeulV6XaJqpQvG8rrVG0oiruJqkYWXE6wVB7NzvQhyPPYEzzJEnVcyX-4teiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
تو چین یه نفر بعد ورود به مغازه‌ش که به علت نشتی پر از گاز بوده، کلید برق رو میزنه و کل مغازه میترکه ولی خوشبختانه زنده میمونه و بعد از اینکه به بیرون پرت میشه کون لختی فرار میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/news_hut/71143" target="_blank">📅 16:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71142">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9c6b59588.mp4?token=JK044tiChGbwtEGNNjEnUb3jysMwUjP9xXyGkb4gsJUDcfNVCASn1XhklqQO6DuMFAtCtiJP4Uc7UKQSOxNBUqnXrKDCmadTerxrePHPfDySeVQcawjjH5klB6BAs-IXrX_RXEVf_gOsA3PCkYwpSE7ODzuwT_g7-x5Smygf2_ja9pvn58YzW2PGpVFo55i2ltPKefPMoRWDOXq5Yv3-lWFgH3Tfh67ZBxKvSnntgHjEHcSpkN1xr_2P_ydlRypuRBYsK_3zqZrQihLk5G68IeWufCt46mlnFb3RTS5OcPff5uei5DWYN6Eh9kWi4OR_g4RUz-4FtiJnP6_Ob_14QoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9c6b59588.mp4?token=JK044tiChGbwtEGNNjEnUb3jysMwUjP9xXyGkb4gsJUDcfNVCASn1XhklqQO6DuMFAtCtiJP4Uc7UKQSOxNBUqnXrKDCmadTerxrePHPfDySeVQcawjjH5klB6BAs-IXrX_RXEVf_gOsA3PCkYwpSE7ODzuwT_g7-x5Smygf2_ja9pvn58YzW2PGpVFo55i2ltPKefPMoRWDOXq5Yv3-lWFgH3Tfh67ZBxKvSnntgHjEHcSpkN1xr_2P_ydlRypuRBYsK_3zqZrQihLk5G68IeWufCt46mlnFb3RTS5OcPff5uei5DWYN6Eh9kWi4OR_g4RUz-4FtiJnP6_Ob_14QoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇺🇦
🇷🇺
یک مزدور برزیلی که در درگیری‌های روسیه و اوکراین می‌جنگید، لحظه حیرت‌انگیز عبور یک تانک از روی خود را — در حالی که میان علف‌ها پنهان شده بود — ضبط و در حساب اینستاگرامش منتشر کرد
😟
@News_Hut</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/news_hut/71142" target="_blank">📅 15:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71141">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07a24e005.mp4?token=gVBTmx78HCaZevvjWaDjUAHU_Y_pPLFWbBTtclkGHRHgOIX0WYFcvEg0kUt4C08GhvwtLyGTc0PqS0iEvFPkJ1rpzSKXTYoPIJTOK4kbDoQb1a7sryDfapt_oOIDn481b2PnBAeVDurNQASWVSn6fgLtDR9Mc92d6-O-zrI_uVv1qQeIZsZ9KTgwDUUe0SyWsWNp3XckdAxJszGSYXj6zTLM6G2gR-xzNwExzHfSu3wW5kw_J-uT2hZw4A-Xd_YmvhZAHcK4fk440ztBdwTVf6lWLxyVIimblSLxWMK6YjC9aFbN2cv4-L8JmMsG8u0VV1u7k-Z5-uXMopOTrB_Pqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07a24e005.mp4?token=gVBTmx78HCaZevvjWaDjUAHU_Y_pPLFWbBTtclkGHRHgOIX0WYFcvEg0kUt4C08GhvwtLyGTc0PqS0iEvFPkJ1rpzSKXTYoPIJTOK4kbDoQb1a7sryDfapt_oOIDn481b2PnBAeVDurNQASWVSn6fgLtDR9Mc92d6-O-zrI_uVv1qQeIZsZ9KTgwDUUe0SyWsWNp3XckdAxJszGSYXj6zTLM6G2gR-xzNwExzHfSu3wW5kw_J-uT2hZw4A-Xd_YmvhZAHcK4fk440ztBdwTVf6lWLxyVIimblSLxWMK6YjC9aFbN2cv4-L8JmMsG8u0VV1u7k-Z5-uXMopOTrB_Pqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه آخوند درباره شعار«تا آخوند کفن نشود این وطن وطن نشود»
؛
همونطور که رهبرمون رو شهید کردن یه آخوند دیگه جاشو گرفت
به ترامپ و نتانیاهو و منافقین داخلی میگم این حرفمو
تا آخوند شماهارو کفن نکنه ول نخواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/71141" target="_blank">📅 15:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71140">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⛔️
این قبیله ای که میبینید اسمشون موکو موکو هست
؛
این قبلیه در افریقا که مثل سرخپوست ها هستن برای اینکه زنان قبیله خودشون دعوت کنن به سبک رقص های به خصوص خودشون انجام میدن
هر زنی در قبیله شون مجذوب رقص مردی بشه میره بهش میده و اصلا اینطوری نیست که کسی حتما باید زن شخص خاصی بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/71140" target="_blank">📅 14:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71137">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca83f4e683.mp4?token=gh_vgEleK9PDhlIPePwuNVg1sFNEx60K0zP75WKMGW9BU7CCOIs-WQFmlsoLYWGRKaYmnAfc6dppjZmK2H_md_Bth9B3xMH-LaTfL2tsl-ViWGglpXL-Fhgn8JtNJhVX33ZSKSBQX8n-niSgjgbwRxx6mgM_Qz2A-u8fGOftxpgLu-abtqLo4a1CgRtJMRvu0n8IzjPRqZMmaV-b-fcKVEmV6cBM-zF1MTYp40fuX6ipaxl5uwp_KS3EpwkFyc2-t6CsBrutVqR0pHLh0QYYYmZvHQxdKtYtMyM1bk86DQkj_PANS3or8wdax8dBCdiOqnuW2ykHgHMX93gdcB3yXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca83f4e683.mp4?token=gh_vgEleK9PDhlIPePwuNVg1sFNEx60K0zP75WKMGW9BU7CCOIs-WQFmlsoLYWGRKaYmnAfc6dppjZmK2H_md_Bth9B3xMH-LaTfL2tsl-ViWGglpXL-Fhgn8JtNJhVX33ZSKSBQX8n-niSgjgbwRxx6mgM_Qz2A-u8fGOftxpgLu-abtqLo4a1CgRtJMRvu0n8IzjPRqZMmaV-b-fcKVEmV6cBM-zF1MTYp40fuX6ipaxl5uwp_KS3EpwkFyc2-t6CsBrutVqR0pHLh0QYYYmZvHQxdKtYtMyM1bk86DQkj_PANS3or8wdax8dBCdiOqnuW2ykHgHMX93gdcB3yXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
تصاویری از تورنتو کانادا بعد از بارش باران و طوفان
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/71137" target="_blank">📅 13:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71136">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fec01afbd.mp4?token=IxeGcJTwyLE3h_5tlr91t26CA78q9okw4T4k9YNM5XBF8Wqnc-EsHqDDnr3DR9k4pdWy5Mpu3na5VXZ5yW0nWfR-9MHthBW3oIJMGUOY_qz4rcT6MV0pnFRI3eFdKd_zV5ywqMDdEo6mgk4NTnz4GCuWOLeN_p5xGRNa7VSm1DwlkevO9bcwK8pO_XUJ1D6oKh3u34K_J3RZMkfOFEwjCGUe_q3AtQFJ5cVQCb7z1sxsHdWPHJW3euOzl-0kCPupYBWXohygE8yY6dHxAob7LFK5L5LNanCc80kABd3qChpO_teJLBXyFNZIum4Ncd5Q8YP7-obfwC006h2rDxeHig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fec01afbd.mp4?token=IxeGcJTwyLE3h_5tlr91t26CA78q9okw4T4k9YNM5XBF8Wqnc-EsHqDDnr3DR9k4pdWy5Mpu3na5VXZ5yW0nWfR-9MHthBW3oIJMGUOY_qz4rcT6MV0pnFRI3eFdKd_zV5ywqMDdEo6mgk4NTnz4GCuWOLeN_p5xGRNa7VSm1DwlkevO9bcwK8pO_XUJ1D6oKh3u34K_J3RZMkfOFEwjCGUe_q3AtQFJ5cVQCb7z1sxsHdWPHJW3euOzl-0kCPupYBWXohygE8yY6dHxAob7LFK5L5LNanCc80kABd3qChpO_teJLBXyFNZIum4Ncd5Q8YP7-obfwC006h2rDxeHig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پیرزن طرفدار حکومت که میگه:
نه پول میخایم نه چیزی دیگه گرونی هم تحمل میکنیم مسئله حجاب رو حل بکنید خیلی مسئله مهم تر و واجبی هستش
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/71136" target="_blank">📅 13:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71135">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af49e9554.mp4?token=FoCh1zPsQvHDErfkYdkoIdlR_Xg8WAq_a4vPbHpPGk-1KCtuQjGXf2iqdCRd6h5l1Se3aT-7UkIseqpryC8-fcfg4nGsf4ktGyT-lSP85L5nxNLVCd4strlbEuUrgIVQ4_EGUvdW0-flShC1tHu0Fhyljb6gTnqORQZWcaMv5S6aa7EwAYii0qVnvH7ZAoy7Oo2olbnuTZaeM2psrUjSz5sm3MN4i28AkGoMQy85Q-xfaJAVuclC8Y2sNIle4hE7H1vbtmPUh6QdF2Sbo09N1_07fk7C-968f3-jy6lHVLMYcpBaAvV4fjc2Vc3CfoCteerf2tueDbHs5sK61xiIDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af49e9554.mp4?token=FoCh1zPsQvHDErfkYdkoIdlR_Xg8WAq_a4vPbHpPGk-1KCtuQjGXf2iqdCRd6h5l1Se3aT-7UkIseqpryC8-fcfg4nGsf4ktGyT-lSP85L5nxNLVCd4strlbEuUrgIVQ4_EGUvdW0-flShC1tHu0Fhyljb6gTnqORQZWcaMv5S6aa7EwAYii0qVnvH7ZAoy7Oo2olbnuTZaeM2psrUjSz5sm3MN4i28AkGoMQy85Q-xfaJAVuclC8Y2sNIle4hE7H1vbtmPUh6QdF2Sbo09N1_07fk7C-968f3-jy6lHVLMYcpBaAvV4fjc2Vc3CfoCteerf2tueDbHs5sK61xiIDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
تصاویری از نفتکش ایرانی که چند ساعت قبل هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/71135" target="_blank">📅 12:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71131">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bb2e861ad.mp4?token=R3UdkNKxNnNO16vrueJ2HTlUvF5skl0f3hJRqD0nFjCbLgzAinVYwqqDDZTpM0cf8y2GPpja3mc1xnKT69enBtq3qdLMOot_HABeBuuRpi0h5TFsI7yXnxbEaKacFk9AN6nrw9bBUphylyITxy_GN4TWLYvN6HO7dgRyilt8c0IkHu4kjqIqpqQR0yasSg3GgIBF_ZwBtInt9pWpwRuqwbADU9onyv7DeU9mcsHJbiar9mIesljKtgb0D730QgiIavGF8wU3-23SAKKJdscGZ4qyH1GQ8rwZz76axQwxf0T5DR7SJfI9DTgDDNjlD1SQ_qBE2CGvrAW9zs4lgahOag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bb2e861ad.mp4?token=R3UdkNKxNnNO16vrueJ2HTlUvF5skl0f3hJRqD0nFjCbLgzAinVYwqqDDZTpM0cf8y2GPpja3mc1xnKT69enBtq3qdLMOot_HABeBuuRpi0h5TFsI7yXnxbEaKacFk9AN6nrw9bBUphylyITxy_GN4TWLYvN6HO7dgRyilt8c0IkHu4kjqIqpqQR0yasSg3GgIBF_ZwBtInt9pWpwRuqwbADU9onyv7DeU9mcsHJbiar9mIesljKtgb0D730QgiIavGF8wU3-23SAKKJdscGZ4qyH1GQ8rwZz76axQwxf0T5DR7SJfI9DTgDDNjlD1SQ_qBE2CGvrAW9zs4lgahOag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇱🇧
خبرنگار اعزامی صداوسیما به لبنان سقوط تپه علی الطاهر در جنوب لبنان رو تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71131" target="_blank">📅 12:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71130">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
خبرگزاری فارس:ساعتی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارگ شنیده شد  خبرنگار فارس در جزیره خارگ می‌گوید صدای انفجار از محدودهٔ خلیج فارس به گوش رسیده است اما نشانه‌ای از دود و آتش در خلیج فارس مشاهده نمی‌شود. تاکنون اطلاعات رسمی و دقیقی درباره…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71130" target="_blank">📅 11:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71128">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gXevtbUCZLup8ddudij9gyfwcF83RhbGYJrDPg3rrlPImG3Cz1EWfVS-BZkzZRG39Mb2GwzDnlfLA-s3AvEuAx_QiWqmd-pxRxvCBQKZc0770x1WfoXebA3fms5kbv_qnaGYKX-8ZODDrWrPh7y5C9IYQZeZNmKsl5KRNqbX-qC9kuIUsjv-vlI76eZ9cokOuGfhS4WHRdgETzt7wcUOO0hkzBOUZZ7bdf2rXMS_HW61bbq8pbSPehDN49qoSwbSY4aefhWcIROdx9Af2B-Kmb3nHv8Yi-xGtxT_8NMuRy5R1AFSBUmKadvsvaqktsrXKDwZf0nJB-kZ3JJgl5cYOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/924e97ac3c.mp4?token=iiBpzuFc5u88hVvbNcFEotyMfemY5DiZzS5fYV-NIoKnRHu_Q0LjNdy3s1jkhRKSpoEBdN95qvftNA6QU9kCM5UD5V7W8W3gCgIWgjMFic4a86arATx_lj9E_PKmX1zpQTI6Oodfhi64S9w2Ggr2vpexA9alfj_gPZuGZPBFUTbVOqbSv9sNpEPR-EY4CKMDh_xJ1Rjy2gGLOeNjYeBkUd2LbKPkgCx30IjDdfPWB1KidWyxOwTmBhwBhHkiOpPagWZfKv3jYbypbfMtir0-zjVvRdVF-d_G4dNcKOIOCGT-kbZSD-wn9hv33yFVldrKtumzcEqezZ7t8ddCMzv_0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/924e97ac3c.mp4?token=iiBpzuFc5u88hVvbNcFEotyMfemY5DiZzS5fYV-NIoKnRHu_Q0LjNdy3s1jkhRKSpoEBdN95qvftNA6QU9kCM5UD5V7W8W3gCgIWgjMFic4a86arATx_lj9E_PKmX1zpQTI6Oodfhi64S9w2Ggr2vpexA9alfj_gPZuGZPBFUTbVOqbSv9sNpEPR-EY4CKMDh_xJ1Rjy2gGLOeNjYeBkUd2LbKPkgCx30IjDdfPWB1KidWyxOwTmBhwBhHkiOpPagWZfKv3jYbypbfMtir0-zjVvRdVF-d_G4dNcKOIOCGT-kbZSD-wn9hv33yFVldrKtumzcEqezZ7t8ddCMzv_0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه پسر بدبخت پست گذاشته که اگه این پست ۵ هزار تا لایک بخوره، صاحبکارم منو میکنه! تورو خدا لایکش نکنین.
و حالا واکنش مردم دلسوز ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71128" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71127">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
خبرگزاری فارس:ساعتی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارگ شنیده شد
خبرنگار فارس در جزیره خارگ می‌گوید صدای انفجار از محدودهٔ خلیج فارس به گوش رسیده است اما نشانه‌ای از دود و آتش در خلیج فارس مشاهده نمی‌شود.
تاکنون اطلاعات رسمی و دقیقی درباره علت و منشأ این صداها منتشر نشده و جزئیات تکمیلی متعاقباً اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/71127" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71126">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71126" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/71126" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71125">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMy3bGXOQNAwVS0M4Sjg1o44SeR17hsSO7Dac63Nb02m3t1E63kOkIdmgw64KMTipyEqDD0qCt2uw0RDqHr8eznrt-GMMjYAWMMtTH2L5skpcw925vXHjjt_kfV4i2gdIR3YhhlTjLhsApkzSVANbXKRr3uglPLXnNIY2u8NQwYp6PPLvaPtbqay_xFEjINkd2dmOjG5LVZeePTfMshP2Vx65QgI9GMfp6TLwnynLtxfdscqhK1IaEZhNIWiH9a--_CI80QAXQ8tcJ5NzCn5DxpaOoF634Ca4R334rXUdN0FZduylxhnbhIRa8Qvhy3JlSMQ9HR9RCWQz2t_VdRodw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
بورنموث
🆚
نیوکاسل
کاونتری
🆚
منچستر سیتی
تاتنهام
🆚
ناتینگهام فارست
اتلتیکو مادرید
🆚
اتلتیکو بیلبائو
ناپولی
🆚
اینتر
آتالانتا
🆚
رم
دورتموند
🆚
هوفنهایم
بایرن مونیخ
🆚
شالکه
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
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/71125" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71124">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0380bdceab.mp4?token=nGyAO2axLPWIzsUdUvB41CnD7FeaYxXbNeFY1X2CG-MvEi8VnfSzyY3xLtI7psUXqnx5ZKuokbc42JCnIygz6K1gdcptIzlq4MynQdD3YCItN6FjWwbfNSjjMcwkv_KoUtVfMaOOyuPU3vQcBvhnWCH46ktnzDCIAVVW1kGZVlDa0nfZ3rM7uv6-eXrWXz4UGYMFM8e7qfx8MohK_VuKk7Uq8kSjeamgd_ToaSjsdeG_djlzjhtANAngCxp8VhXqEDuMqr0ntu0sxmMqxEIkrX6eG3Kifvuc75vOAZNq-NHXpiDPSQdZn8zh6JDqCX3Bj-CTqykBfnc5vC-r6I5C1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0380bdceab.mp4?token=nGyAO2axLPWIzsUdUvB41CnD7FeaYxXbNeFY1X2CG-MvEi8VnfSzyY3xLtI7psUXqnx5ZKuokbc42JCnIygz6K1gdcptIzlq4MynQdD3YCItN6FjWwbfNSjjMcwkv_KoUtVfMaOOyuPU3vQcBvhnWCH46ktnzDCIAVVW1kGZVlDa0nfZ3rM7uv6-eXrWXz4UGYMFM8e7qfx8MohK_VuKk7Uq8kSjeamgd_ToaSjsdeG_djlzjhtANAngCxp8VhXqEDuMqr0ntu0sxmMqxEIkrX6eG3Kifvuc75vOAZNq-NHXpiDPSQdZn8zh6JDqCX3Bj-CTqykBfnc5vC-r6I5C1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📚
معرفی لاکچری‌ترین مدارس ایران !
برای اینکه به علم برسی هم باید اول ثروت داشته باشی!
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/71124" target="_blank">📅 11:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71123">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a478b3c9a9.mp4?token=O_0x5fqpbTmwC28imlEKbicFNHxcaJMFYikh-KEUK08jsGXy2FLdlMOrJV-DPnXhlh0Ky_Dj0ed_Enn2hlXR_HhlDbm8WKxakxQkeK-hOvRwnRHWwI6_8o5dvcMbxadZ2VbQZ_W4OECxd9mThmLQxYsg4lsMq-wsvFWXhLl2De0xKxsOCOiDaejXPMRGX0_iMJFmOAHH3Bkz6ZYVgTPR_dKCNQjmuwEV6ROrE8gEQzohWL4iJSLyOAabJhUExLPHCXKAAu7D_4BDD5GYV8JJyZWTifNH0BzMjCQsqSO44JYyZ3D0Vjbf-_v0p1-xPoNNsvAWU-fprwRYFWr34PveYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a478b3c9a9.mp4?token=O_0x5fqpbTmwC28imlEKbicFNHxcaJMFYikh-KEUK08jsGXy2FLdlMOrJV-DPnXhlh0Ky_Dj0ed_Enn2hlXR_HhlDbm8WKxakxQkeK-hOvRwnRHWwI6_8o5dvcMbxadZ2VbQZ_W4OECxd9mThmLQxYsg4lsMq-wsvFWXhLl2De0xKxsOCOiDaejXPMRGX0_iMJFmOAHH3Bkz6ZYVgTPR_dKCNQjmuwEV6ROrE8gEQzohWL4iJSLyOAabJhUExLPHCXKAAu7D_4BDD5GYV8JJyZWTifNH0BzMjCQsqSO44JYyZ3D0Vjbf-_v0p1-xPoNNsvAWU-fprwRYFWr34PveYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تسلا، سفر با تاکسی‌های خودران Cybercab رو تو تگزاس آغاز کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/71123" target="_blank">📅 10:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71122">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a09a3f19ee.mp4?token=aMwwZBJKzYQjbiqfSRRhx4duHTjWlLTsTnoNXozo1kZWgx4ydnbh774WbSSXvIAkrdzKjs1dyx_XstzdIDUIJ_nbCzqzFIjxgDePQXoxYmm99C_XzcvPZfB09ecaCF2Xnz9zyLbjPpd3QKseo26gGTEn-cODgdgHqyQ3ji0ud1JOkJlvJqMvbWT5vSCf3vUo522o-E0wLt5XaMlyyQ0kVZEBZlS1RsIU68B1QGjLgrxyLtKIoubCo5MhpjJK18j0Vu2sQKbEQRluGiX-jgEq_DhT-EJWim1DoaWtVuFKqIjNFv2EBuE6DYfv35wS8oUBecrH84ndX2B0nt-RkzlGvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a09a3f19ee.mp4?token=aMwwZBJKzYQjbiqfSRRhx4duHTjWlLTsTnoNXozo1kZWgx4ydnbh774WbSSXvIAkrdzKjs1dyx_XstzdIDUIJ_nbCzqzFIjxgDePQXoxYmm99C_XzcvPZfB09ecaCF2Xnz9zyLbjPpd3QKseo26gGTEn-cODgdgHqyQ3ji0ud1JOkJlvJqMvbWT5vSCf3vUo522o-E0wLt5XaMlyyQ0kVZEBZlS1RsIU68B1QGjLgrxyLtKIoubCo5MhpjJK18j0Vu2sQKbEQRluGiX-jgEq_DhT-EJWim1DoaWtVuFKqIjNFv2EBuE6DYfv35wS8oUBecrH84ndX2B0nt-RkzlGvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
〰️
🇹🇭
کامیون‌های سوخت‌رسان مشغول انتقال سوخت هواپیما به ناو هواپیمابری «یو‌اس‌اس آبراهام لینکلن» (CVN-72) در بندر «لائم چابانگ» تایلند هستند؛ به‌طوری که از زمان پهلو گرفتن این ناو، روزانه ورود و خروج ۲۰ تا ۳۰ دستگاه کامیون مشاهده شده است.
این سوخت برای تأمین نیازهای «بال هوایی نهم ناو» (CVW-9) در داخل ناو ذخیره می‌شود؛
یگانی شامل جنگنده‌های رادارگریز F-35C Lightning II، جنگنده‌های تهاجمی F/A-18E/F Super Hornet، جت‌های جنگ الکترونیک EA-18G Growler، هواپیماهای هشدار زودهنگام E-2D Advanced Hawkeye و بالگردهای MH-60 Seahawk.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/71122" target="_blank">📅 10:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71121">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deba41468f.mp4?token=XG-3OnWOpt9kc0R6Ax2ayWPU3hKJlBLRep6r7kAHewa4kFico3wWiA1QqeIw-VHpL468OrDehVSbxp57rLPjDrJxcR3ClZgdpqoLoOJE2bIrAvBUIUBG2tewiE4LafoUncIdNiqS-ixJ-XZGwKOsfRT7xGbrpTf1I_9kx-s00IGzmwdNbvVwjc4tKVSqnEjZ8QzgkY7ZDvlLJiv1wrd6nW3Az_b9J76plUzA-Me11KpbBqpNnaEBr-8D1KcwJqQG0et4BV4maMuQ7-0hcdoeVaMo-uSjvkLyqdq2zL8H6OBxdJxdwIPUb0WaXkOoPrr2l1ywWuu8QQpODnQDXxZGFrlUn9NhDhkIZx681qJqBiIp8G2DO9kHLAHJIIyiDZnhLbMV5p8Ku64fYEQ2B1mrHui3wUjg3JmginW1PV0cXFtLFV-r8-oZcS8CLx4XEBN-TCWrymUTscVrCeDiPV0cAR-PiVzEbPFW2SYnRJ94Mw4gHv_6h_h5T7441Jtk4hjgV6a4vvK9VE7vLdez8ORQWuSSU_jx8pZKctUNuKL4ZnX88YTdQWkXqmajy_GgrKGyYF8YBnWDvw6-ZmMDBQS0qapjQYE0NwRGwQqpyC2gbOuDQyxDUpmLIngosAxD_NpFDXD55IhYPdGmaAfpsqgZFCCCu9HlseuFHMi32batOhk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deba41468f.mp4?token=XG-3OnWOpt9kc0R6Ax2ayWPU3hKJlBLRep6r7kAHewa4kFico3wWiA1QqeIw-VHpL468OrDehVSbxp57rLPjDrJxcR3ClZgdpqoLoOJE2bIrAvBUIUBG2tewiE4LafoUncIdNiqS-ixJ-XZGwKOsfRT7xGbrpTf1I_9kx-s00IGzmwdNbvVwjc4tKVSqnEjZ8QzgkY7ZDvlLJiv1wrd6nW3Az_b9J76plUzA-Me11KpbBqpNnaEBr-8D1KcwJqQG0et4BV4maMuQ7-0hcdoeVaMo-uSjvkLyqdq2zL8H6OBxdJxdwIPUb0WaXkOoPrr2l1ywWuu8QQpODnQDXxZGFrlUn9NhDhkIZx681qJqBiIp8G2DO9kHLAHJIIyiDZnhLbMV5p8Ku64fYEQ2B1mrHui3wUjg3JmginW1PV0cXFtLFV-r8-oZcS8CLx4XEBN-TCWrymUTscVrCeDiPV0cAR-PiVzEbPFW2SYnRJ94Mw4gHv_6h_h5T7441Jtk4hjgV6a4vvK9VE7vLdez8ORQWuSSU_jx8pZKctUNuKL4ZnX88YTdQWkXqmajy_GgrKGyYF8YBnWDvw6-ZmMDBQS0qapjQYE0NwRGwQqpyC2gbOuDQyxDUpmLIngosAxD_NpFDXD55IhYPdGmaAfpsqgZFCCCu9HlseuFHMi32batOhk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بابک زنجانی:
الان کافه‌های مردم را می‌بندید بعد شب آدم می‌فرستید که بیاید تعامل کند.
می‌خواهم فیلم و مستند درباره این موضوع تهیه کنم... آن شخص هم فکر می‌کند که با ۱۰، ۲۰ سکه زندگی‌اش را گذرانده
بیکار کردن ۸۰ نفر در منِ بابک زنجانی چه اثری دارد؟! اصلاً فردا بیایید آتشَش بزنید.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71121" target="_blank">📅 09:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71120">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWABbhDsaGTni_MTDHJ59CaOtNJ3Y_IVNEzPAvLjRwIZowaZPKhK3yE7wNLNRvEmRBt-xUJ4YlXa5dkWAGj197IL5jZ11UaxZZaaGC_o7Ws5NRo3EYXtOAufgnDhf6Sp77Z1w60UxrVZTaSDHqxCSy8cnA0WxNEMDH_zhWL5gJ-FaEg4Bqv-OgukqttZfA7axVjFw-a80zr-sV0rXfCTT4IThy4YQ5oi0DsT3oJVaNvcJ-ruKxccapoO4KV-ezbqIdoOVr87Uy5IJ6s5Jd_cqa42ZXRn9WHwHYBIfemp6MZWyfNImQhIImDUn19hPTBYBqC-_HkFKxuKg9IIdPRuHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
🇴🇲
نیویورک پست:عمان بی‌سروصدا پیشنهاد ایران برای دریافت مشترک عوارض از کشتی‌های عبوری از تنگه هرمز — حتی به‌صورت داوطلبانه — را رد کرده است.
این اقدام، ادعای هفته گذشته سپاه پاسداران مبنی بر توافق دو کشور بر سر تقسیم درآمدهای این آبراه را تضعیف می‌کند.
عمان معتقد است که دریافت عوارض از کشتی‌های عبوری ناقض قوانین بین‌المللی است و تحت فشار آمریکا و کشورهای حوزه خلیج فارس، از این طرح عقب‌نشینی کرده است.
ترامپ دو بار تهدید کرده است که در صورت موافقت عمان با دریافت عوارض، این کشور را بمباران خواهد کرد.
ایران در دوران جنگ، نهادی برای مدیریت تنگه ایجاد کرده بود و از هر نفتکش مبلغی بین ۱ تا ۲ میلیون دلار عوارض می‌گرفت؛ اما بدون همکاری عمان، هرگونه سازوکار دریافت عوارض در دوران پس از جنگ، فاقد وجاهت قانونی خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71120" target="_blank">📅 09:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71119">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71119" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71119" target="_blank">📅 01:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71118">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLuXNtH3SxQKdK4xMw9Qus0bXok5Z21iEoyMTRz9wpFNZvc4tHOo7EMrrMOClkAIOle7FXLXasgy0LVLgSo4QoK22g89XAZ_psy5KG4lawjtPLCPBIxgHp2gcQNzby98jrmYrxZXk86cIclMgdCssMWD_XTFQ1SeyaQG_me_Xh5gFFIU3SXIAUo0uSV8ne7FReIeKH8bGSUTQ9sT-c4J-BN4GUVjAuVeQBy77miyOlEhmJx4mzE_Eesfzb-UidoEsCW1ncZmhB6yy0nIcBldAiDx-CwGL0Utu7UPeBnJ8SekGfC_l0KuO4uWgVJi82dtQJ6z_HRrCGpTTIpSB2iccA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71118" target="_blank">📅 01:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71117">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59487b6d80.mp4?token=ZH-eWDhOoYBnrTa6vKr_Es06CihAy9Y6ZVW7sM9i_WAfPap5MO7KEbKYw8hePLStInb4ZHfN-z1NUu2FwJNPCDRsixZHtzvI2Y6IrlyU0Ot3IqGUXU27S7ezesbt1W1RVy7NV02ftgN7dIQ6AJUbn-PrBIMOVVvia8_tCylJiEsx023zGAFjS8pcA37_SRN0ro2y3K5sR7xXgmg1hLYPE2i8RiMgWvEwD5a65ArZeXQor3xUvuRQPhGVihfUaYeri_1ihwuksdbljRuZg-4lW60hLPBCiv4GEvwH6vZj2zE0s_QRoOaYZueRJAnJ-o229CfT2cqIraqWtlos7Jt2dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59487b6d80.mp4?token=ZH-eWDhOoYBnrTa6vKr_Es06CihAy9Y6ZVW7sM9i_WAfPap5MO7KEbKYw8hePLStInb4ZHfN-z1NUu2FwJNPCDRsixZHtzvI2Y6IrlyU0Ot3IqGUXU27S7ezesbt1W1RVy7NV02ftgN7dIQ6AJUbn-PrBIMOVVvia8_tCylJiEsx023zGAFjS8pcA37_SRN0ro2y3K5sR7xXgmg1hLYPE2i8RiMgWvEwD5a65ArZeXQor3xUvuRQPhGVihfUaYeri_1ihwuksdbljRuZg-4lW60hLPBCiv4GEvwH6vZj2zE0s_QRoOaYZueRJAnJ-o229CfT2cqIraqWtlos7Jt2dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
مردم آمریکا چه زمانی باید انتظار تعیین تکلیف (resolution) در مورد ایران را داشته باشند؟
🇺🇸
ترامپ:
انقلاب(Revolution)؟
🎙
خبرنگار:
تعیین تکلیف(Resolution).
🇺🇸
ترامپ:
تفاوت بزرگی است. فکر کردم انقلاب(Revolution) جالب‌تر بود.
⭕️
🗒️
به دلیل تلفظ نزدیک دو کلمه راه حل/تعیین‌وتکلیف(Resolution) و انقلاب(Revolution) ممکنه ترامپ اینجا به عمد کلمه انقلاب رو انتخاب کرده باشه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71117" target="_blank">📅 01:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71116">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ef0c44cf.mp4?token=Sjbo6WJ6Rw8hiFjZCjd5EjgF_cgvitDDSV4bYj2Plcbdh6G10E9N5jkFsQp4Z7xzt-2TL61GMyvCdp7xw2uxd35jYX8LGnZetlXQ49uM2abgHWqm7kJkUiC_d9h5lKZpem2pdHiGXG1HVT_2d34iGCFk9KfG6m8VB1LC4JoXgYg-KpU3ZVqriCNkA8B2DIbSAyZ6wzSfgYCV1mR8IhEP1db-0iWIDuPbFR7SAw4j4idy7v2gEeYmIzUWROvElP5lKMzRl1we0eDPrdtt6qDKVH9r-8b2YNuUeU3jTql_ml3RjPSLdBzpsb0xOueUZ2iLuywp2oQL2KX1TDqVcNDTGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ef0c44cf.mp4?token=Sjbo6WJ6Rw8hiFjZCjd5EjgF_cgvitDDSV4bYj2Plcbdh6G10E9N5jkFsQp4Z7xzt-2TL61GMyvCdp7xw2uxd35jYX8LGnZetlXQ49uM2abgHWqm7kJkUiC_d9h5lKZpem2pdHiGXG1HVT_2d34iGCFk9KfG6m8VB1LC4JoXgYg-KpU3ZVqriCNkA8B2DIbSAyZ6wzSfgYCV1mR8IhEP1db-0iWIDuPbFR7SAw4j4idy7v2gEeYmIzUWROvElP5lKMzRl1we0eDPrdtt6qDKVH9r-8b2YNuUeU3jTql_ml3RjPSLdBzpsb0xOueUZ2iLuywp2oQL2KX1TDqVcNDTGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو ایتا و روبیکا از یچیزی رونمایی کردن که حتی خودشون هم نمیدونن چیه
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71116" target="_blank">📅 23:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71115">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1e4d7b78.mp4?token=NW1HGq1uHDrCFu5-usfpivvdx7qlV12H5GPlQtzeiYO7K7a6dbVVGoDXrc7ZbotVMNld8Xf8SypKcVSB12yRxLejKVt9iGExDjvwF-R62dBRfYXbJ28ucF-uNECizJriwFUPjDAVl8T3uEKZjAWA74P-VniZHJAQqijAHycQxb1tUan0hl0nF_jybosfWxt2480lrCT4omHAr2tvH6Ht9Aa5B35OdgTIRzI4d3H7WJ1DTk03h46jgb-QD6Sx_Ra_bqloH9ufD8z6J6J1Rrb9gveHc3btnkL7EmM87FwTDALzGcJl3J0R4NyrV6ptkSHjFaSMB-eRibw_9KEViIdndQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1e4d7b78.mp4?token=NW1HGq1uHDrCFu5-usfpivvdx7qlV12H5GPlQtzeiYO7K7a6dbVVGoDXrc7ZbotVMNld8Xf8SypKcVSB12yRxLejKVt9iGExDjvwF-R62dBRfYXbJ28ucF-uNECizJriwFUPjDAVl8T3uEKZjAWA74P-VniZHJAQqijAHycQxb1tUan0hl0nF_jybosfWxt2480lrCT4omHAr2tvH6Ht9Aa5B35OdgTIRzI4d3H7WJ1DTk03h46jgb-QD6Sx_Ra_bqloH9ufD8z6J6J1Rrb9gveHc3btnkL7EmM87FwTDALzGcJl3J0R4NyrV6ptkSHjFaSMB-eRibw_9KEViIdndQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
طرف اندازه یه گاری پول جمع کرده و الان آورده تبدیل به دلارش کنه، کل این همه پول نقد شد فقط ۳۰۰ دلار
!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71115" target="_blank">📅 22:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71114">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/05f93dafa7.mp4?token=hiwRwwhq3Om7IiFHWeH0HH2Ov6xsf4SbVmpYV_nK1gkhINBWHn6_3K32MThN1mdPuHrEIM1rVwjSdUOj_RekC3Y2ZpTWEM_7QgIWFjwQU4OEGYqls-Is6sMPPlO8bH3NUMv4307FaH6Ps2gSwsVDBw_59MjBFMUODOoDW3c4VCUye3yInYRinbF3tozawxgwA-4Oqg1bD9gBpX2gtizgBuBrdtMhhT0PXqAqq5OGM55m6yKpnBgrFj6BiQGPlb3OdEPtUtUWVlDAl_JCBxRy0T07tKKtGjzKOaj7xkrYMEQ1V-ZZYM3M6ahz3SacbrqijmgL3hHRSa0AqGE78NGxC1xLvULcNZQNfSNt8dtG134uvzgUcCsku7ERyvL5jldw4ya5ak6WZX7mkqmpcpLzsrRBPflm4vhlvkJh1U6sPHFkAZl_86jT-mr1EGh6mFTTkh-tF9k_ylyN_eB9ZeI8FrnN4pejvRJpLZqdq0PgufsYLAKDRFbBWmdE-vvx4V2MAUmmY-5RSs9Cy2Wai7_toSAR2FYvj7kootMa4MQewE3zV2TLj6ypG5E3o14SIf26AvO4rBvxSB4FvFCXFCIt3Lat8TdZUYhAypG-hAiwq2qp4UnbxzLIuULPtEcEi9RYX-Q78ojb89dz_oW-f7KMCtBLHHqelIDlZSaxRGOfpV0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/05f93dafa7.mp4?token=hiwRwwhq3Om7IiFHWeH0HH2Ov6xsf4SbVmpYV_nK1gkhINBWHn6_3K32MThN1mdPuHrEIM1rVwjSdUOj_RekC3Y2ZpTWEM_7QgIWFjwQU4OEGYqls-Is6sMPPlO8bH3NUMv4307FaH6Ps2gSwsVDBw_59MjBFMUODOoDW3c4VCUye3yInYRinbF3tozawxgwA-4Oqg1bD9gBpX2gtizgBuBrdtMhhT0PXqAqq5OGM55m6yKpnBgrFj6BiQGPlb3OdEPtUtUWVlDAl_JCBxRy0T07tKKtGjzKOaj7xkrYMEQ1V-ZZYM3M6ahz3SacbrqijmgL3hHRSa0AqGE78NGxC1xLvULcNZQNfSNt8dtG134uvzgUcCsku7ERyvL5jldw4ya5ak6WZX7mkqmpcpLzsrRBPflm4vhlvkJh1U6sPHFkAZl_86jT-mr1EGh6mFTTkh-tF9k_ylyN_eB9ZeI8FrnN4pejvRJpLZqdq0PgufsYLAKDRFbBWmdE-vvx4V2MAUmmY-5RSs9Cy2Wai7_toSAR2FYvj7kootMa4MQewE3zV2TLj6ypG5E3o14SIf26AvO4rBvxSB4FvFCXFCIt3Lat8TdZUYhAypG-hAiwq2qp4UnbxzLIuULPtEcEi9RYX-Q78ojb89dz_oW-f7KMCtBLHHqelIDlZSaxRGOfpV0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
یه بلاگر ایرانی رفته چین و ربات انسان نمای چینی رو به مبارزه طلبیده؛
حرکات ربات به قدری تمیزه که انسان واقعا از آینده جهان خایه میکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71114" target="_blank">📅 22:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71113">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66a864cef.mp4?token=CxdFB43ay-SGPw1JWB382d-xLrIVENNUXO3JRU4s7bL3nV0LLkRaeXHGmracmDGaCmtHBra0x2yvzr7Egfel2ycheMDQEqUzJabUy0tpvn4py4ctPXtf3_2HG8eu014rznO9dA4lGhBIDWUjqoSZDaFeAuu7C6EotX56h9AW3zpTf1ugHf6-hF31Jz-w0lS1SrapcbZNrpalpeepGw5jNKQ8uqHAYeHhAbXKVnv4Yu4RXlAzp_LWV5WpeiTXAkZGuvR9fn6_CGGomz0KXQPQjS5qVc0QM49yzRFJ1qDPmnBmNIOrRMeGjn95jECnzgHXeWUxg5t5Yyht9fti37Kxig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66a864cef.mp4?token=CxdFB43ay-SGPw1JWB382d-xLrIVENNUXO3JRU4s7bL3nV0LLkRaeXHGmracmDGaCmtHBra0x2yvzr7Egfel2ycheMDQEqUzJabUy0tpvn4py4ctPXtf3_2HG8eu014rznO9dA4lGhBIDWUjqoSZDaFeAuu7C6EotX56h9AW3zpTf1ugHf6-hF31Jz-w0lS1SrapcbZNrpalpeepGw5jNKQ8uqHAYeHhAbXKVnv4Yu4RXlAzp_LWV5WpeiTXAkZGuvR9fn6_CGGomz0KXQPQjS5qVc0QM49yzRFJ1qDPmnBmNIOrRMeGjn95jECnzgHXeWUxg5t5Yyht9fti37Kxig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخیرا بعضی دخترا طی یه حرکت فوق‌العاده و زیبا، دارن هرچی ژل و بوتاکس تو صورتشون بوده رو خارج میکنن تا نچرال به نظر بیان
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71113" target="_blank">📅 21:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71112">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEj7oGqDsriQVIOS7bnZ8sC2xLccwoKf0FYZRvf7MIczUi3tqmky-_nb5QqUf1-fx5uJDF1R3fYWbJk2GnuDQIvxMlyyvNvw2PejR7DI1trnMS_Rem8gcBKX4eyDsATFrI2-UiaAlz4HHY3pj7qgfEP7OvXF3mKpkhIKyDKu6_3oH9EdynVu19SBCKz_K4qdNKymmhvjLQ6ZK9Aj8uUvAsmAHqskvwfBOp50rC7QPX617Mpe2fsVAOLIO5GT74vvo9VMd_3-Z2nUb-Z5d67tBQufwwpzKHhGtnBDXLF0LYZ3pSHgQwiCZe4xS29iJ8xYz7Ju00Cnb9FJsBGv6ytdJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👎
قرارگاه خاتم الانبیا: حملات پیش دستانه علیه پایگاه آمریکا در اردن که در حال آماده سازی برای حملاتی علیه کشور بودند را انجام دادیم!
❌
خبر بالا که بطور گسترده در حال انتشار در رسانه هاست فیک و نادرسته، همونطور که می‌بینید سپاه پاسداران و قرارگاه خاتم‌الانبیا هیچ اطلاعیه‌ای مبنی بر حملات پیش‌دستانه منتشر نکرده
@HutNewsPlus</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71112" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71111">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcZcph6ic5KNvZ1NjU1--krUOSHdLfuuc8R_KgDiZlNUc5_CYv41yfFLmGWZmOkLIS5YEyhQcM7tWdY4gYX4YZgcAhAIVmxwKDwm7sNqic0feLwxw617lv7vvqr6siXHNsBrdYC56j1FoE8xV2pRD8amVsvCOm64BGZY_644iXfHSryDnHUQL2FThoFocwVy8tOnCseK-5w-SErZC7JGy8VftQSyzoFbyl7VbErEYSZX2NF4OJJsnMuG5-UkC8yd3LgDLhuyuinTShHTL9Z_PREcIRWwv67Q8uSJYcX6ICaWsmYtgDNc-L6SP-K9zVkksxL1rpsj7VuToGoE_4W-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام ارشد آمریکایی به کانال 12: در حال حاضر هیچ اطلاعی از وقوع آتش‌سوزی در پایگاه‌های آمریکا در اردن وجود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71111" target="_blank">📅 21:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71110">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c74f1d2d4f.mp4?token=iat0vwfu4gqFJv2-gHCyJlWZq7e91NlNJxljrnBNIrreuTw6WYOtc0FU2rBsqb0Qz-_r-6zhlGcRgYom8YdDftqOjA_pgHpjtXOsf0rMApX1vzOMjFc7LlpqgAGR7lhywAA_OgV_nymE4n7uKmgJgR5xz9UCxybzhByNk6-mAgS4hhofVRR70Hn_37PxPBifGTORHcFpU3L2NZJumBJuoIcbS1JqTXLIfUAPogKigUTOFO-9lwwWcJeLH6MIA3AHJUaXin9GeUovGpWQV5jPI--wlthuStbHiJktBmoaQgVdbhmvsOgwbyPRtjm8mWflkLLmYvT66fadFSYtKaEzFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c74f1d2d4f.mp4?token=iat0vwfu4gqFJv2-gHCyJlWZq7e91NlNJxljrnBNIrreuTw6WYOtc0FU2rBsqb0Qz-_r-6zhlGcRgYom8YdDftqOjA_pgHpjtXOsf0rMApX1vzOMjFc7LlpqgAGR7lhywAA_OgV_nymE4n7uKmgJgR5xz9UCxybzhByNk6-mAgS4hhofVRR70Hn_37PxPBifGTORHcFpU3L2NZJumBJuoIcbS1JqTXLIfUAPogKigUTOFO-9lwwWcJeLH6MIA3AHJUaXin9GeUovGpWQV5jPI--wlthuStbHiJktBmoaQgVdbhmvsOgwbyPRtjm8mWflkLLmYvT66fadFSYtKaEzFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک ها از ایران به سمت اردن
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71110" target="_blank">📅 20:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71109">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
منابع عربی:چندین انفجار در اردن رخ داد
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71109" target="_blank">📅 20:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71108">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbf8f1e1a9.mp4?token=VucblGlJFk2Kw3-qtym2oWkaxWsnnby5Mj_F7fBcP_dkXMAhXBKbxqo2O7n0Si9M-yTN_cHUHmn-TfMFf0dvP8cPqeTNP2RmN-8sGQYyyM_B1y2osdD8sus_UHOnJuC7R-Slznu-IVz8H7noUueoYBKlXXbZnn5AwNClGX1QJZs2W9JI7pLTbZ84_pXxSLixoRhRpXRGkTs7zI8ftR5fBt8IHc5c_z_uy-XFUNmb8theQHnfdD3TTAGvXECKjCRYoxUj87_9tOKP1Lfnkj7EYEcVtoUolJ0H08lkmUn0oS4n5wYklXgNQe6JlJFxGF0auxzZpD4hDJPIo1KcdlZvzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbf8f1e1a9.mp4?token=VucblGlJFk2Kw3-qtym2oWkaxWsnnby5Mj_F7fBcP_dkXMAhXBKbxqo2O7n0Si9M-yTN_cHUHmn-TfMFf0dvP8cPqeTNP2RmN-8sGQYyyM_B1y2osdD8sus_UHOnJuC7R-Slznu-IVz8H7noUueoYBKlXXbZnn5AwNClGX1QJZs2W9JI7pLTbZ84_pXxSLixoRhRpXRGkTs7zI8ftR5fBt8IHc5c_z_uy-XFUNmb8theQHnfdD3TTAGvXECKjCRYoxUj87_9tOKP1Lfnkj7EYEcVtoUolJ0H08lkmUn0oS4n5wYklXgNQe6JlJFxGF0auxzZpD4hDJPIo1KcdlZvzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇨🇳
بِسِنت درباره ایران:
آن‌ها محموله‌های نفت را به سمت چین روانه کردند. منتظر اقدامات مربوط به این موضوع در روز سه‌شنبه باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71108" target="_blank">📅 20:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71105">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64aa07a7bb.mp4?token=lv2x5XDiPFDruyyleUCPr0d1LSoafX4XyNq6DtMFWJcPGFctpk7NGstIu9IfKHR5N0rdFFLy68ZNf3mppbAoR9PEHIhsbHnW4-ruargved9u6a_2pItNEzucmBjLtgmB4sD0MqGnqthqm4I9cObYjnTTdIrCxO2vCt7VBvyKYqhTfMdOeIUQYNg5UMUJjrXAjJe9BbW-MicUSPa9l3ttVcrCs_IaWCTL-6WUNClDVHBdZuP8OsKQRghd4JaLqYzmI8AwKr9xynVQpCUS3xHIOKxQjJ-yscxBkRxGBG0BhxPpmY-ckzn88HqQNIOW46D8HBCQUuE_WnwMj_JBX2EpjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64aa07a7bb.mp4?token=lv2x5XDiPFDruyyleUCPr0d1LSoafX4XyNq6DtMFWJcPGFctpk7NGstIu9IfKHR5N0rdFFLy68ZNf3mppbAoR9PEHIhsbHnW4-ruargved9u6a_2pItNEzucmBjLtgmB4sD0MqGnqthqm4I9cObYjnTTdIrCxO2vCt7VBvyKYqhTfMdOeIUQYNg5UMUJjrXAjJe9BbW-MicUSPa9l3ttVcrCs_IaWCTL-6WUNClDVHBdZuP8OsKQRghd4JaLqYzmI8AwKr9xynVQpCUS3xHIOKxQjJ-yscxBkRxGBG0BhxPpmY-ckzn88HqQNIOW46D8HBCQUuE_WnwMj_JBX2EpjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بابک زنجانی: دلار رو بدید دست من تا یک سال رو همین قیمت نگهش میدارم وگرنه با همین فرمون کشور تا یک سال دیگه نابود میشه.
من رو ۷ سال بدون بدهی انداختن زندان و همشم تو انفرادی بودم. همه اموالمم ازم گرفتن. وقتی آزاد شدم حتی ۱ دلار نداشتم.
با چند تا تلفن ۱ میلیارد دلار پول جور کردم و چندتا شرکت تاسیس کردم.
من میخواستم سایپا رو به قیمت ۲ میلیارد دلار بخرم که نشد ولی خودم میخوام کارخونه تولید خودرو تاسیس کنم
من توی خارج کشور بانک داشتم پولای وزارت نفت تو اون حساب بود. اونا تحریم شدن پولاشون اونجا گیر کرد گفتن تقصیر توعه و حکم اعـدام بهم دادن
تمام بانکای ایران بیان جلوی من بشینن ببینیم من بیشتر میتونم سرمایه جذب کنم یا اونا. فقط با چندتا تلفن. تا معلوم بشه کی اعتبار داره
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71105" target="_blank">📅 19:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71104">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf31ca2a30.mp4?token=D0Z2iX-zqX6EHNgQzUUM-l0sFO6hbiaUkgaLKD-yDXQIGUfDizknrnYIA8SsdwGo_RFT5UShwkLGyVQ8A7zPvhbGRw--mwThlM0WSVZS5WEd3sLNZDNCt4VSCj8QJ8RTqxKwfspasqy4RwhmBFw5RRRWUzp4djzpOAV-5NF-RLdUbwN9bksG3eyRMUczhBClm3wr7jOvkZLUWN4PsLo9UyUauuc1dX78NWX1wg2BJBrDoitakASrK_Vrs-LnfkorWedKCH8ZcTn3OY3ndvTIV_BpTi_1pMqmdbGPHr687DfLB9D-NBeUjb4JxSZy9SZ_3Gt-A-3N42X9OJZGruf7fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf31ca2a30.mp4?token=D0Z2iX-zqX6EHNgQzUUM-l0sFO6hbiaUkgaLKD-yDXQIGUfDizknrnYIA8SsdwGo_RFT5UShwkLGyVQ8A7zPvhbGRw--mwThlM0WSVZS5WEd3sLNZDNCt4VSCj8QJ8RTqxKwfspasqy4RwhmBFw5RRRWUzp4djzpOAV-5NF-RLdUbwN9bksG3eyRMUczhBClm3wr7jOvkZLUWN4PsLo9UyUauuc1dX78NWX1wg2BJBrDoitakASrK_Vrs-LnfkorWedKCH8ZcTn3OY3ndvTIV_BpTi_1pMqmdbGPHr687DfLB9D-NBeUjb4JxSZy9SZ_3Gt-A-3N42X9OJZGruf7fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت درباره ایران:
متحدان ما در امارات متحده عربی در خصوص این بانک مستقر در دبی همکاری بسیار مؤثری داشتند. اکنون ما برای متوقف کردن تمامی این جریان‌های مالی غیرقانونی، با آن‌ها وارد همکاری شده‌ایم.
ما برای رفع این مشکل با آن‌ها همکاری خواهیم کرد، چرا که بانک‌های متعددی در سیستم مالی آن‌ها فعالیت می‌کنند.
ما نمی‌خواهیم این بانک‌ها را نابود کنیم — هرچند اگر لازم باشد چنین خواهیم کرد — اما اکنون همه کشورها در این مسیر با ما همراه شده‌اند.
این پایان کار برای این رژیم است؛ آن‌ها یا باید [رفتار خود را] عادی‌سازی کنند و یا با عواقب آن روبرو شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71104" target="_blank">📅 18:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71103">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e7eb93ff.mp4?token=S92OCLHwMxB6R2tnTg8Q49YulMAAVZl8vw2bnBzAOJNXu0mkrl6uA67fW9po1YTrqV51hLh2slszWMv0rNlAZoMxUtM9wKb7SyPWK8Fnv3v7NUABcBj2Ofjrv4Eny_9RvZCDGs_-YoXyAhznVOl2JTUFKPpD1c19IFKax5gCqR8WP1cXW6GIPfu4_g-EqrZBQZOUp6-lvvnO6wxVvecpZ5wyfwsy7aAV5TKEmdcmYsT-OPdOsDHTVVIKgUZI6cDLujRBZnrf8QISDr6b718jP0bVOwloFm7dfvd2FJdPWqCS0PNJ-scE1Uqp2sQtxS53a4u3qO86_br2T-5_sWtjVWDOswl4r6BVIKI-6IZ_BWPZBhUMuk5i9URVftKxoyuNm0ttyYj9XLIpR94jm2zQ-CrKLiLk5FPi-EQ2oLHr5_QH5U-jLyJ9fvJdqW9JFVTyJVcoUWewrO0FAnCbQn6HCxFDgw-HxIZ1K0Spho5AmXCxn3zrryqYpFAhO0YZ_Ab4aPjcrQxA-ctO-YhE9VkrmgPHA4yyndZVrTCUbLS7clJRzCvDfTlQ46gJAfpCUTWU7MgEgMrdevUUPLbwB1zZLXZfjrCO3CEVA2H1MhavYeSzPmc0byRgtUC0TB42nwZnwDfnlkF6BUQbi0w-Sk4C3GZjrv_aySSILahIIRJcj-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e7eb93ff.mp4?token=S92OCLHwMxB6R2tnTg8Q49YulMAAVZl8vw2bnBzAOJNXu0mkrl6uA67fW9po1YTrqV51hLh2slszWMv0rNlAZoMxUtM9wKb7SyPWK8Fnv3v7NUABcBj2Ofjrv4Eny_9RvZCDGs_-YoXyAhznVOl2JTUFKPpD1c19IFKax5gCqR8WP1cXW6GIPfu4_g-EqrZBQZOUp6-lvvnO6wxVvecpZ5wyfwsy7aAV5TKEmdcmYsT-OPdOsDHTVVIKgUZI6cDLujRBZnrf8QISDr6b718jP0bVOwloFm7dfvd2FJdPWqCS0PNJ-scE1Uqp2sQtxS53a4u3qO86_br2T-5_sWtjVWDOswl4r6BVIKI-6IZ_BWPZBhUMuk5i9URVftKxoyuNm0ttyYj9XLIpR94jm2zQ-CrKLiLk5FPi-EQ2oLHr5_QH5U-jLyJ9fvJdqW9JFVTyJVcoUWewrO0FAnCbQn6HCxFDgw-HxIZ1K0Spho5AmXCxn3zrryqYpFAhO0YZ_Ab4aPjcrQxA-ctO-YhE9VkrmgPHA4yyndZVrTCUbLS7clJRzCvDfTlQ46gJAfpCUTWU7MgEgMrdevUUPLbwB1zZLXZfjrCO3CEVA2H1MhavYeSzPmc0byRgtUC0TB42nwZnwDfnlkF6BUQbi0w-Sk4C3GZjrv_aySSILahIIRJcj-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
همه خواهان پایان یافتن این وضعیت هستند. ۴۷ سال از عمر این رژیم شرور می‌گذرد و دنیا دیگر از دست آن‌ها به ستوه آمده است.
مردم ایران مردمی عالی هستند؛ اما رژیمی سرکوبگر بر آن‌ها حاکم است.
یا رژیم از درون تغییر خواهد کرد، یا مردم قیام خواهند کرد، و یا باید دید چه پیش می‌آید.
ما آن‌ها را از نظر اقتصادی خفه خواهیم کرد. آن‌ها در وضعیتی قرار دارند که من آن را «آرواره‌های مرگ اقتصادی» می‌نامم.
ارزش پول ملی‌شان در حال فروپاشی است و صادرات نفت آن‌ها به صفر رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71103" target="_blank">📅 18:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71102">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13cf8fb01d.mp4?token=nUtOFnnqsd82k9GWaeL71sdo8xZsJNW2h-tz_wZgNUZuHH52aiK50Z-tySnHpCEBn5OJxCrXBejfNxSNRjaUYnL_BDrsSgRCdjNdUeJvxQvfi6nf4mqWL8GuYEw5WYz47saopmAG9QkOHEhEdmpxztxJ2k8rvdu-g5nx9swwdmgWCjJ3l4O9ikBUdFQvv8bK5vRBINsHnyFbrC3yY9i-R4krmsDwOO25wPvgLK3k5oWm7EO2mudKjR9SRQNfMv5r9FP6vML9l7M518W0ioQlGx5KdcI7X7yMG3nf6D6o_VZU312APuDxUtD_LQs29JYHYKdZz7tjBULXbXRWYVUKeYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13cf8fb01d.mp4?token=nUtOFnnqsd82k9GWaeL71sdo8xZsJNW2h-tz_wZgNUZuHH52aiK50Z-tySnHpCEBn5OJxCrXBejfNxSNRjaUYnL_BDrsSgRCdjNdUeJvxQvfi6nf4mqWL8GuYEw5WYz47saopmAG9QkOHEhEdmpxztxJ2k8rvdu-g5nx9swwdmgWCjJ3l4O9ikBUdFQvv8bK5vRBINsHnyFbrC3yY9i-R4krmsDwOO25wPvgLK3k5oWm7EO2mudKjR9SRQNfMv5r9FP6vML9l7M518W0ioQlGx5KdcI7X7yMG3nf6D6o_VZU312APuDxUtD_LQs29JYHYKdZz7tjBULXbXRWYVUKeYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
ما بانک دیگری را که با ایران مرتبط است، تحریم کردیم. هفته گذشته، یک بانک مصری را که پنج شعبه در دبی داشت و ۱.۸ میلیارد دلار در اختیار این رژیم قرار داده بود، تحریم کردیم.
امروز بانک دیگری را تحریم خواهیم کرد و احتمالاً هفته آینده نیز بانک دیگری را تحریم می‌کنیم.
ما به سیستم مالی می‌گوییم:
ای عوامل مخرب، ما می‌دانیم شما چه کسانی هستید. خودتان هم می‌دانید چه کسانی هستید. کارتان تمام است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71102" target="_blank">📅 18:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71101">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
⭕️
🇹🇷
🇮🇷
وزارت خزانه‌داری آمریکا سه نهاد مستقر در ترکیه را به‌دلیل ارتباطات مالی و فعالیت‌های مرتبط با ایران تحریم کرده است:  Golden Global Portföy Yönetimi Golden Global Varlık Kiralama Golden Global Yatırım Bankası
⏺
هم‌زمان یک مجوز عمومی برای دوره جمع‌کردن…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71101" target="_blank">📅 18:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71100">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
⭕️
🇹🇷
🇮🇷
وزارت خزانه‌داری آمریکا سه نهاد مستقر در ترکیه را به‌دلیل ارتباطات مالی و فعالیت‌های مرتبط با ایران تحریم کرده است:
Golden Global Portföy Yönetimi
Golden Global Varlık Kiralama
Golden Global Yatırım Bankası
⏺
هم‌زمان یک مجوز عمومی برای دوره جمع‌کردن معاملات (wind-down) با این نهادها صادر شده است
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71100" target="_blank">📅 18:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71099">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372294672d.mp4?token=q8iHCu-d_vu-gvVakUAfSBqIwpZPdIauKN0EXozp9gCFr5IcSNiDS8hgoFOvV9K6OHNVZpD1Sa356P282dEUw4uekkQjih_ocPVNggsyQcH831jlh4ISc38zlUkm10Q3u_-gZ94dog-5e-9MjPeZAABeKLUtaehR_L5mfOSpdCKB-X1FDaVHeecT2cEjQTM-n7kF_cT5UAo-NPI_gO5lo_yTKZIEauA6Kj5DOrJ6wmJuIzToidq8e_vEOmLQK9z_B5qX3XPOW2nKHZmVj5MpaGMdiul6lBQLNx58nQRmoDlroP1ki0glhWiEJnuxb6nYZCdpicMsQMQIIqp7OaXSuJqGWNTycsrUjbS0wJLzzsHPe-tbpTXTkJghGNTweeZF6SoUKi1B6OzRoRh5O7eBeFAiJBPzSBJuUMgwmvx6gKP0EUwdWbbBD8W4UBFY7b8vJ_YJxagB-pv5UoaQ5_rYu_GxHfBrSinwr3bsu2Kz3V0Y054dOm_KxDtzcR27X-SjNq4kTAJH20KtX3dVrHPw5NB8mfppOr-n3RSHgEIdcnOqsJ_-lCMks6zCTn1LKPSxiNlWb97MsArClvW2w_Hzk-iHyn-D69gIQD8Pm4LaUP4GQ6zntJl3RjZ2WDmh1PBh3GoilWLlx7l5kC58taNBn9nbWNZZA-IeCFAmEEuDKNk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372294672d.mp4?token=q8iHCu-d_vu-gvVakUAfSBqIwpZPdIauKN0EXozp9gCFr5IcSNiDS8hgoFOvV9K6OHNVZpD1Sa356P282dEUw4uekkQjih_ocPVNggsyQcH831jlh4ISc38zlUkm10Q3u_-gZ94dog-5e-9MjPeZAABeKLUtaehR_L5mfOSpdCKB-X1FDaVHeecT2cEjQTM-n7kF_cT5UAo-NPI_gO5lo_yTKZIEauA6Kj5DOrJ6wmJuIzToidq8e_vEOmLQK9z_B5qX3XPOW2nKHZmVj5MpaGMdiul6lBQLNx58nQRmoDlroP1ki0glhWiEJnuxb6nYZCdpicMsQMQIIqp7OaXSuJqGWNTycsrUjbS0wJLzzsHPe-tbpTXTkJghGNTweeZF6SoUKi1B6OzRoRh5O7eBeFAiJBPzSBJuUMgwmvx6gKP0EUwdWbbBD8W4UBFY7b8vJ_YJxagB-pv5UoaQ5_rYu_GxHfBrSinwr3bsu2Kz3V0Y054dOm_KxDtzcR27X-SjNq4kTAJH20KtX3dVrHPw5NB8mfppOr-n3RSHgEIdcnOqsJ_-lCMks6zCTn1LKPSxiNlWb97MsArClvW2w_Hzk-iHyn-D69gIQD8Pm4LaUP4GQ6zntJl3RjZ2WDmh1PBh3GoilWLlx7l5kC58taNBn9nbWNZZA-IeCFAmEEuDKNk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تیزر دوم فصل اول سریال هری پاتر که از کریسمس 2027 قراره پخش بشه
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71099" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71098">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71098" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71098" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71097">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZqilgoajvKjiirGEY6U78aZos-DgwmK2Lr9LWNHUHqeR2MS3H_0htjPlNGEa3cOEAQasl0OlytNQXptRF_mSn165UT1gIQZdpV_FBOezduvWT0JqoGKUK_J0SIZikostHsvuLKYl4fjF5HkcqFua9jgGXjBSW5RXPKQ5Apcpz96oNDBFdZMVkYj0j15HUD7nnaGpr9eVehmM67yFO3ussgCW_WA8u5-xAVYfyVdEP9W-bO5n1sr1iTr3TSqXQXGLA-G5oUsAXioYon4MlMus9871lf-uNAqD_dmC4vgvC18sdWRO5MrjN0aK2aVDyv-PdL5fN67CihExXV-M1adeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
پاری‌سن‌ژرمن
🆚
موناکو
⚽️
را در سایت بین‌المللی
TrexBet
پیش بینی کنید.
📊
مونامو ۲ برد | ۱ تساوی | ۲ شکست | ۹ گل زده
پاریس ۲ برد | ۱ تساوی | ۲ شکست | ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71097" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71096">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">〰️
سنت‌کام:
بیش از ۲۶۰۰ تفنگدار دریایی و سرباز نیروی دریایی آمریکا، بر روی ناو جنگی USS Boxer (LHD 4) مستقر هستند و این ناو جنگی در حال حاضر در خاورمیانه در حال انجام ماموریت است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71096" target="_blank">📅 17:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71095">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcc841fe5.mp4?token=Q5zy1b8tE6kr5UTcc6oe_xTqJjNNrTRuvdynbkmzqNq0CRru8SFO8A8nNsBAI2jw88x01ADbjlW_BZfQxp5NN16cPLuEnu0FxBZZd7FlxZ-k3LY0N5G_zy7mZyRug7qjOXBiaZ94Nu5rJnFGldW_XVWQ-oNBgR5Fq7qLemUU8137E5cNy20VVbxGmMlkn_hjJu2wUXXWBRU1VEwcrsuXnNdtkJxGqnr1FPn_mocTUfv6C7kYVrSgVA3ISo28AuWQ3aHw61enJjYBaPWGskpdVdF5a5LqrTKTWOF3iq04GuC_JjYHvdXjbK5_DYL7CyrpP3-MbV1EsNJ_8oLnuK7bdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcc841fe5.mp4?token=Q5zy1b8tE6kr5UTcc6oe_xTqJjNNrTRuvdynbkmzqNq0CRru8SFO8A8nNsBAI2jw88x01ADbjlW_BZfQxp5NN16cPLuEnu0FxBZZd7FlxZ-k3LY0N5G_zy7mZyRug7qjOXBiaZ94Nu5rJnFGldW_XVWQ-oNBgR5Fq7qLemUU8137E5cNy20VVbxGmMlkn_hjJu2wUXXWBRU1VEwcrsuXnNdtkJxGqnr1FPn_mocTUfv6C7kYVrSgVA3ISo28AuWQ3aHw61enJjYBaPWGskpdVdF5a5LqrTKTWOF3iq04GuC_JjYHvdXjbK5_DYL7CyrpP3-MbV1EsNJ_8oLnuK7bdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ببینید از خانمی که داره از تجربیات رفتن خودش به تور کویر میگه...
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71095" target="_blank">📅 17:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71094">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf229661bf.mp4?token=PGUN016zkyHYb7AazTLhc8QjXwI2ho52jXu6jcWr0kjszxe9r0wYqVE10rGBfeJANRIJRhABDPgTMpx3nQn23sX_gNnv90AHvAZhc63GtdThOJPtVkPdyGPzx1qnSwFehryXkutSrYurKFpn1jbP17rZTma0n8vljKYOfzqbpfY_HO9JnuRvRWNzq1vUQvwqYcPvPYQZo6zOSy1Ku3P-w5NDT6vuuA69_taFVxuvez8tqBBD9zZzf3T6yUwcbNGf0vkN2p8beM2G0pjc-G9g7_xcCllY3JIm8pWAkDWrTx2er8jJVeKZprMtmFHEQY7QVOVzCiEl6bv2fBVK1aamww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf229661bf.mp4?token=PGUN016zkyHYb7AazTLhc8QjXwI2ho52jXu6jcWr0kjszxe9r0wYqVE10rGBfeJANRIJRhABDPgTMpx3nQn23sX_gNnv90AHvAZhc63GtdThOJPtVkPdyGPzx1qnSwFehryXkutSrYurKFpn1jbP17rZTma0n8vljKYOfzqbpfY_HO9JnuRvRWNzq1vUQvwqYcPvPYQZo6zOSy1Ku3P-w5NDT6vuuA69_taFVxuvez8tqBBD9zZzf3T6yUwcbNGf0vkN2p8beM2G0pjc-G9g7_xcCllY3JIm8pWAkDWrTx2er8jJVeKZprMtmFHEQY7QVOVzCiEl6bv2fBVK1aamww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
سامسونگ A17 که یکی از ضعیف‌ترین و تخمی‌ترین‌ گوشی‌های بازار به حساب میاد، قیمتش به 100 میلیون تومن رسیده.
البته این قیمت واسه دیروزه و امروز احتمالا گرونتر شده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71094" target="_blank">📅 16:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71093">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc7b61838f.mp4?token=rGzos_7xVNXQHoaX2Obpyq1qvOSm059ojHPy18xlu-qs0XitAqOas_68G_ZkGP5JzV9LgCJezYV5tMV5WF7ljtnYud93TrLcI_mK221FScOqm6-yjNLpTOxEf95rtSdptsGNMSE_RcPFyYIH65CjhxPu4ulKO85oFFqjSYnqGNCirZ5mm6HRQGwb1EsAZ_XQUP0_9m8rEhqTqrTW4UDHrFpMS4QaMNg0k_jN4bUl_kqIx1bxQjhly0B25-yE5q8hwaW89eFSEZOr61IbmTLOQu_w5YLGlaKLhFJjBHZKt0iqVwPh_UZntOvxw3V7DJYwxhAHSZnsy6xdbAFCUYrsLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc7b61838f.mp4?token=rGzos_7xVNXQHoaX2Obpyq1qvOSm059ojHPy18xlu-qs0XitAqOas_68G_ZkGP5JzV9LgCJezYV5tMV5WF7ljtnYud93TrLcI_mK221FScOqm6-yjNLpTOxEf95rtSdptsGNMSE_RcPFyYIH65CjhxPu4ulKO85oFFqjSYnqGNCirZ5mm6HRQGwb1EsAZ_XQUP0_9m8rEhqTqrTW4UDHrFpMS4QaMNg0k_jN4bUl_kqIx1bxQjhly0B25-yE5q8hwaW89eFSEZOr61IbmTLOQu_w5YLGlaKLhFJjBHZKt0iqVwPh_UZntOvxw3V7DJYwxhAHSZnsy6xdbAFCUYrsLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یک راننده کامیون:
الان کنار مرز پاکستان هستیم میخوایم رد بشیم اجازه نمیدن.
رفتیم پیش رئیس گمرک میگه طرف پاکستانی اجازه ورود نمیده.
پاکستان گفته به ازای هر ماشین باید دو میلیارد تعرفه بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71093" target="_blank">📅 16:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71092">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45bdb5a184.mp4?token=emTUTX-mZD-lKzRRcPu94y52W_-HvBN9SBFqaRgnfQhufz6wUGfmbgjhRmxiB0oZvSkJvznjSIrrN4ysDJO67A_RrtTocxSFq53maU-AGb3YO_z4TpSHeML-5c0cAH1_enpeQaEV7DMeg266DrszsQGstVUuIaqWWnScp8CNzkHEcWm0dUcGEXe_cYsdnRBtxbJ0jf0vmvDVKflFe_M6sY2Mkf0DfHJYAW6DnPtJHWCy3HE1utCDqame9gBCs0pxKqjMRGQUIRm5UIMxeiB6NAyXBh87efLtnOHwy2bisNKhahc72HM1Vlu4bqShNfAVrrtbk-n4PkfxNs271WBHWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45bdb5a184.mp4?token=emTUTX-mZD-lKzRRcPu94y52W_-HvBN9SBFqaRgnfQhufz6wUGfmbgjhRmxiB0oZvSkJvznjSIrrN4ysDJO67A_RrtTocxSFq53maU-AGb3YO_z4TpSHeML-5c0cAH1_enpeQaEV7DMeg266DrszsQGstVUuIaqWWnScp8CNzkHEcWm0dUcGEXe_cYsdnRBtxbJ0jf0vmvDVKflFe_M6sY2Mkf0DfHJYAW6DnPtJHWCy3HE1utCDqame9gBCs0pxKqjMRGQUIRm5UIMxeiB6NAyXBh87efLtnOHwy2bisNKhahc72HM1Vlu4bqShNfAVrrtbk-n4PkfxNs271WBHWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه دختر حامی حکومت:
فک کردین اومدم از قیمت دلار آه و ناله کنم؟ نه اومدم پاره‌اش کنم!
رزق و روزی دست خداست نه آمریکا، دلار قیمتش عوض شده، خدای ما که عوض نشده.
قیمت دلار هر چقدرم بشه، باز روزی مارو خدا می‌رسونه، منم اعتراض دارم ولی ناامیدی تزریق نمی کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71092" target="_blank">📅 15:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71091">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2be4c50b6.mp4?token=mjHplpywo0GQv3NMC1gkIdEXeIxcxeuHBrN1Qwz5rLLxyHgc-ETssgc4c482hdlYzWaVxxhLdgkAg1VLomMJybmqw8eeRXriCV3aZlgSMNlWXZuvSILfNCeO5MvekzgrP9qucSoUWtlVZN5vzn-_FFNkoVeTTcCt6uqJ40TzpCmH2bx_VrdGOWs9hn8UfAHx1jIYWj1yj6l9uyRMhUF56eT8IVDZLRMVm38A1vX1VsYdg9LPpUFKNE8H-ygu1IAagC8ABWaWTWhGUz0ojPL3LnH9PKbxbly2OSJNa34TsjU7v-VHCFQrQdOAvVEVaYfjzTQdRr962phVKEl42faYVoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2be4c50b6.mp4?token=mjHplpywo0GQv3NMC1gkIdEXeIxcxeuHBrN1Qwz5rLLxyHgc-ETssgc4c482hdlYzWaVxxhLdgkAg1VLomMJybmqw8eeRXriCV3aZlgSMNlWXZuvSILfNCeO5MvekzgrP9qucSoUWtlVZN5vzn-_FFNkoVeTTcCt6uqJ40TzpCmH2bx_VrdGOWs9hn8UfAHx1jIYWj1yj6l9uyRMhUF56eT8IVDZLRMVm38A1vX1VsYdg9LPpUFKNE8H-ygu1IAagC8ABWaWTWhGUz0ojPL3LnH9PKbxbly2OSJNa34TsjU7v-VHCFQrQdOAvVEVaYfjzTQdRr962phVKEl42faYVoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚀
🇰🇼
روز گذشته، یک پهپاد انتحاری که توسط ارتش جمهوری اسلامی پرتاب شده بود، یکی از واحدهای برج مسکونی الدیره در شهر کویت را هدف قرار داد. این اصابت باعث آتش‌ سوزی و تخریب کامل آن واحد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71091" target="_blank">📅 14:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71090">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0b6b730d.mp4?token=Pko5eDBHvVMLyNxHBP_oVBuxcuVG_fgTccNynInsIHjMASS4NUK6SOUvlt6WYBP2x_okxPWZp1KAp_2eDU_9cHlN73lOgVi8ad28agvj5pv3r_6koM5paqed0kBZF2rBGapH8fRUdFc3UuY_qGqBpIin71JG2CRfVeVLYPRRxZzcEXrlQSeGXkXn87eV6dJSKaH9fnvSg0VrAucbrZxmsgPjxdir1zg4rTBLin187LxDLNyGarvXlSggmq6gAOF-ztoKtq8ThP5y5ACzUvpD3AgQd21PNqSfoa7ySRFQ6LqWZL4NV789b-IpgO5N-1O1WjtI8C8HixHwlCdadLrtog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0b6b730d.mp4?token=Pko5eDBHvVMLyNxHBP_oVBuxcuVG_fgTccNynInsIHjMASS4NUK6SOUvlt6WYBP2x_okxPWZp1KAp_2eDU_9cHlN73lOgVi8ad28agvj5pv3r_6koM5paqed0kBZF2rBGapH8fRUdFc3UuY_qGqBpIin71JG2CRfVeVLYPRRxZzcEXrlQSeGXkXn87eV6dJSKaH9fnvSg0VrAucbrZxmsgPjxdir1zg4rTBLin187LxDLNyGarvXlSggmq6gAOF-ztoKtq8ThP5y5ACzUvpD3AgQd21PNqSfoa7ySRFQ6LqWZL4NV789b-IpgO5N-1O1WjtI8C8HixHwlCdadLrtog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
❌
🇦🇪
با افزایش تحریم‌های آمریکا تجار و بازرگانان می‌گویند امارات از بارگیری لنج‌های ایرانی خودداری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71090" target="_blank">📅 14:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71089">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28ac9cc9fe.mp4?token=SMU-T-CK68QGSVxlMfFRLwq8c_NG6CtJLGP1u7tYm3dXNyrmMZqJFEchHt3B7bvpoQPZiui0A2oc2dPO0dgLaf1Qp2HEoEU_6nNP8iebVEmdQAy7KnX5Jb9i6XSqjOK2lYF8YBEWn0sT1dGL9eBYd0wcCO0AEvJmfxnOkUoJCqWF9IELp9IaD-wQIoBJ6FiPeh0qnsbVSweM3GrL5OWTtdAkCsZ8zZlzPvA8XBX_io5NSI51H_rBSfFqrzt2Ccf7ok_jjoe2-F6kmKeiL3LCVBvzn-1s1hCf8NUtwS6jj0NaWG45acfUKNFtG1T1C-nrj75ZDOVNbo2WQzbUv84Eqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28ac9cc9fe.mp4?token=SMU-T-CK68QGSVxlMfFRLwq8c_NG6CtJLGP1u7tYm3dXNyrmMZqJFEchHt3B7bvpoQPZiui0A2oc2dPO0dgLaf1Qp2HEoEU_6nNP8iebVEmdQAy7KnX5Jb9i6XSqjOK2lYF8YBEWn0sT1dGL9eBYd0wcCO0AEvJmfxnOkUoJCqWF9IELp9IaD-wQIoBJ6FiPeh0qnsbVSweM3GrL5OWTtdAkCsZ8zZlzPvA8XBX_io5NSI51H_rBSfFqrzt2Ccf7ok_jjoe2-F6kmKeiL3LCVBvzn-1s1hCf8NUtwS6jj0NaWG45acfUKNFtG1T1C-nrj75ZDOVNbo2WQzbUv84Eqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇱
🚂
برخورد قطار با یک کامیون در گذرگاه راه‌آهن در گدانسک لهستان.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71089" target="_blank">📅 13:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71088">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b60a6b68b8.mp4?token=l6_2cS8vfGLsrgZW5_1DZptxVthvPhOU0yYimgdgoLn-KoDnF27x-QwdRqx1vh1dAOmn4jytwzoZGyWtobzRIumbWz3tDGKJK0jnh--zTSbxeucRWlQOF0m5YL_Gokjs35tZqHfj0STUSn9Qi2e79rdDQaJm1QZiyz934wd8kZ6HZNp_3frfk5Dk2KKTCiL27VSR1SrvWl52E_tX0876dbv9jKammW6uuR7UH6TUfyCtaXZQ3ia_GTv-sZHNrVXe3Wgpsj29J_FUW1JSw00dSAgB1HT4pAno2ON8u7ejKxmZlRgk7wfo-rUlm4pRLsnUbDc-n4hjaQnuAsVI985hSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b60a6b68b8.mp4?token=l6_2cS8vfGLsrgZW5_1DZptxVthvPhOU0yYimgdgoLn-KoDnF27x-QwdRqx1vh1dAOmn4jytwzoZGyWtobzRIumbWz3tDGKJK0jnh--zTSbxeucRWlQOF0m5YL_Gokjs35tZqHfj0STUSn9Qi2e79rdDQaJm1QZiyz934wd8kZ6HZNp_3frfk5Dk2KKTCiL27VSR1SrvWl52E_tX0876dbv9jKammW6uuR7UH6TUfyCtaXZQ3ia_GTv-sZHNrVXe3Wgpsj29J_FUW1JSw00dSAgB1HT4pAno2ON8u7ejKxmZlRgk7wfo-rUlm4pRLsnUbDc-n4hjaQnuAsVI985hSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف با رفیقش رفته دور دور الهیه و به یه دختره شماره دادن،
و حالا اولین پیامی که دختره براشون فرستاده
😟
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71088" target="_blank">📅 13:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71087">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71087" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71087" target="_blank">📅 13:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71086">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZjIKPoM4TQxAbvtwyIrDtI0GnvURY47rODXJ0fRfCW4ZXtOciTWdmuIZiht5Sdq1xQNz_7FazTxDm4ulpGP9LhZzRNbXjCDo8nNE04iO7GuXBexNJKsrVquJsDXgNj0ddnblJjggGaB_0X2KPLEHc1ViQpfLVYk9ykfjWfUc6xRsZeVReYGUmzMTOAGz-dhLOsyGBo6IuIN5yb7dh2DOW889rPb9RPYFkcfD8wjCx4hXap6cFO5p9nCtZkL3aMed59TVC-10ldXIfkMbykey_lsVY8p3n22u0gA3zDnDxgywJ_8cZ39bCs-C-KADHO4wlxQa-hVJYARAD2Eh8sUPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب رئال بتیس
🆚
رئال مادرید را در سایت بین المللی
TrexBet
پیش بینی کنید
📊
نگاهی به آمار دو تیم در ۵ بازی اخیر
رئال بتیس: ۲ برد، ۱ تساوی، ۲ شکست در ۵ بازی
رئال مادرید: ۵ برد در ۵ بازی اخیر
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71086" target="_blank">📅 13:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71085">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4843999275.mp4?token=JfDkTrPNcu_mlwppPjzvWljokT44Q4RGnhrTamWw2dSTxMY1kf_WIxUg9zg_O9Po5tguGaDyTeNc6a7GdH00gbW-6UyWcq68CjNe9AiwwdXMrMR3SKsOsHvKgTrKo9CMjwfJ-OdHSkBgQG0zNSF2DlsYQbmw3Qec-szQCbVbQdToA86CMSbEFE8hoCL4Ah3w0Yds3sVzo5SZ6Fc10131I5nWqZJgPh296vMRAdPCGve5lVpznLFxUdQ86EN06DPiq0cqDhZrMlSKjBWJh1nUIxw5-qBLk_cGItFzKiCor039E7cGJPYkKUI8bkxfVbwfQse7EZMQ9TO0cZkVMQs56g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4843999275.mp4?token=JfDkTrPNcu_mlwppPjzvWljokT44Q4RGnhrTamWw2dSTxMY1kf_WIxUg9zg_O9Po5tguGaDyTeNc6a7GdH00gbW-6UyWcq68CjNe9AiwwdXMrMR3SKsOsHvKgTrKo9CMjwfJ-OdHSkBgQG0zNSF2DlsYQbmw3Qec-szQCbVbQdToA86CMSbEFE8hoCL4Ah3w0Yds3sVzo5SZ6Fc10131I5nWqZJgPh296vMRAdPCGve5lVpznLFxUdQ86EN06DPiq0cqDhZrMlSKjBWJh1nUIxw5-qBLk_cGItFzKiCor039E7cGJPYkKUI8bkxfVbwfQse7EZMQ9TO0cZkVMQs56g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
پرزیدنت ترامپ در رسانه‌های اجتماعی پرسید: «مردم ایران کی قیام می‌کنند و می‌جنگند؟» آیا دولت در حال بررسی مسلح کردن یا ارائه، سایر حمایت‌های مستقیم از مخالفان ایرانی است؟
🇺🇸
ونس:
ها ها ها... مگر پیتر دوسی امروز صبح این سوال را در فاکس نیوز نپرسید؟
سوال خیلی خوبی است.
و چیزی که رئیس جمهور گفت(درجواب به این سوال) دقیقاً همان چیزی است که من می‌خواهم بگویم.
قرار نیست درمورد این سوال صحبت کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71085" target="_blank">📅 13:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71084">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VLhwJBQIr0327kBfStWzdR5Tgjz5NaBQpjys0swugVfJBM6smbIIUHEGGNNGtjvg7I3P-BxrQsd3fU59Xscp_RJtN5IEsiyOWwQEFQA-kyWD_mXiLQSMkXl1uFWJsVc-ME6YrvX9-7bf3PpxXAitXLO7_33eAZ8mLTfZkREeasmriXUUaIV-yHHS7YBjLkxo5oEh3ppQqgAr76W8ONxLSO7FLom-gPEAjxaW_0a38mLjCFrpZe1BE9eyJTVaM86agLeZB1pFPD5gYyAIgWVQNY2S7RlTOVI9T4tixNObdwAyau6eG-qz0jUfiJQhlGl-KvKbu_zDUm534zoo4VVv8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی با این پست به شدت میسوزه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71084" target="_blank">📅 12:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71083">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0edd50344.mp4?token=sSywWnFI1YhjEhZh9tdl0Ht-CMuyRQcvyHZFAC7VZvU5pwDDxSg5m6b_caS233oQa-l48CoNWJJSuO23CuXe6g7H7Yh_OM1sBnbZDHd8ZlopXyl0RjuHJ1HZ3FTriDuatTWaqWdsrBvie1oIi2sadhlnPJ1yh9DmawcWSqe1G9vPVIIY2UdOS3mmzEETtQo1mnbIPzs0ZTFiVrrXVC-Wbw4iVFbrHYPnNNXp5C9hUtIfyrdUuGTuJyoXC0h0hL0sWM7ZB703Vuj-R5v3SXtDKL2gGEggbAh9rVtVikBtWuLjEdKJiUQezvr5WywaSO-3CGgmKNE9bz0MzgFCM7PkAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0edd50344.mp4?token=sSywWnFI1YhjEhZh9tdl0Ht-CMuyRQcvyHZFAC7VZvU5pwDDxSg5m6b_caS233oQa-l48CoNWJJSuO23CuXe6g7H7Yh_OM1sBnbZDHd8ZlopXyl0RjuHJ1HZ3FTriDuatTWaqWdsrBvie1oIi2sadhlnPJ1yh9DmawcWSqe1G9vPVIIY2UdOS3mmzEETtQo1mnbIPzs0ZTFiVrrXVC-Wbw4iVFbrHYPnNNXp5C9hUtIfyrdUuGTuJyoXC0h0hL0sWM7ZB703Vuj-R5v3SXtDKL2gGEggbAh9rVtVikBtWuLjEdKJiUQezvr5WywaSO-3CGgmKNE9bz0MzgFCM7PkAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال شده از طرفدار حکومت
🎙
خبرنگار:
از قیمت دلار خبر داری ؟
🇮🇷
طرفدار حکومت:
بله شده 200 و خورده ای
🎙
خبرنگار:
با این قیمت پس چرا اومدی اجتماعات ؟
🇮🇷
طرفدار حکومت:
دیگه باید قدرت تفکیک داشته باشید تو ذهنتون و قیمت دلار یه چیزه و بیرون اومدن یه چیز
اصلا اگه امنیت ما نباشه شما میتونید راجب قیمت دلار فکر بکنید؟ نه نمیتونید!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71083" target="_blank">📅 12:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71082">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⏺
ویدیو وایرال شده از اعتراض یه زن کارتون خواب:
به عنوان یک کارتون خواب که 20 ساله دارم این زندگی تجربه میکنم!
شما مسئولین که مردان خدا هستید شما دیگه چرا؟
تو دانشگاه رشته حقوق خوندم
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71082" target="_blank">📅 11:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71081">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18ffbfe89.mp4?token=cgChCPOz8b-mY1LjT7w5sSa76JgYrQp4k0xU1Gnh7tbtyYOXF_N5EamsYBHumliEt8DTOPVyrv8WARNEbprQEkxS8lcDcLcJsr4bVGuFUd1YPapLvmr-fpmb0JREMkEKaHapkRPeXXE57JQk5blagMKI39_FJld4wer-QbljLEvTYXhhGAFXiR6EBrcA3j0nvp8Y_0uQunMmicdRnrlhlYcmcab1D2TFiGuFtYR_sZ-UoF3Rh-G9YgsOTplkubgOZHsJvA3-6DPsKwKUBRqg7I7ksGJ7Zf3fv14WErv0nRjFuBHuo8aw78sTUI-fTypuzDrhti8ruUeCvt-F-Do9Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18ffbfe89.mp4?token=cgChCPOz8b-mY1LjT7w5sSa76JgYrQp4k0xU1Gnh7tbtyYOXF_N5EamsYBHumliEt8DTOPVyrv8WARNEbprQEkxS8lcDcLcJsr4bVGuFUd1YPapLvmr-fpmb0JREMkEKaHapkRPeXXE57JQk5blagMKI39_FJld4wer-QbljLEvTYXhhGAFXiR6EBrcA3j0nvp8Y_0uQunMmicdRnrlhlYcmcab1D2TFiGuFtYR_sZ-UoF3Rh-G9YgsOTplkubgOZHsJvA3-6DPsKwKUBRqg7I7ksGJ7Zf3fv14WErv0nRjFuBHuo8aw78sTUI-fTypuzDrhti8ruUeCvt-F-Do9Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسره دوست دخترشو برده تو کوچه پس کوچه ها بهش رانندگی یاد بده
آخرش هردو غافلگیر شدن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71081" target="_blank">📅 11:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71078">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bc34fe3de.mp4?token=U1_GrpQyyBY3H8pKmXqucEeqkzWF2MB3Bkj05UShtS_DjNNn1-5zqiXW73AzoiRtLhpM_bZ4m844t9VFWG-6y-LvalRBD2IsEflXfL2yt2-56QE3yIcuHXZ7xbY1Z2zTmJYQlotO2JSUAYvMDlpenacF1T12jpMvgiaKuxN7fCu8m_8J3sksFOw3Cgxl8Ny_gLRZDMAb4oAJhIgS-5aM-Y2TygJDSz-f08vVk_OGnuagldjdwl4gN1m4uFknUnOIg0LHCisTIa95-UHa8xbzuD46IxEDbJZAbrhYtq7-gBxxcXdfFjApX3xmWTs8yvWj3vXSkftg-sEeB4uVIatSOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bc34fe3de.mp4?token=U1_GrpQyyBY3H8pKmXqucEeqkzWF2MB3Bkj05UShtS_DjNNn1-5zqiXW73AzoiRtLhpM_bZ4m844t9VFWG-6y-LvalRBD2IsEflXfL2yt2-56QE3yIcuHXZ7xbY1Z2zTmJYQlotO2JSUAYvMDlpenacF1T12jpMvgiaKuxN7fCu8m_8J3sksFOw3Cgxl8Ny_gLRZDMAb4oAJhIgS-5aM-Y2TygJDSz-f08vVk_OGnuagldjdwl4gN1m4uFknUnOIg0LHCisTIa95-UHa8xbzuD46IxEDbJZAbrhYtq7-gBxxcXdfFjApX3xmWTs8yvWj3vXSkftg-sEeB4uVIatSOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی دزفول چند تا دزد میرن توی یه خونه مجهز به وسایل ضد سرقت و 3 کیلو طلایی که توی اون خونه بوده و قاحب‌خونه قصد داشته باهاش طلا فروشی بزنه رو میدزدن!
صاحب خونه شب قبلش توی اینستاگرام گفته بوده که میخواد طلا فروشی راه بندازه که این حرفا رسیده به گوش دزدا ؛
فردای همون روزی که این حرف رو زده وقتی صاحب خونه خانومش که باردار بوده رو وقتی میبره بیرون یه هوایی بخوره دزدا میریزن تو خونه و طلا ها رو میبرن.
حالا صاحب خونه گفته که هرکسی هر سرنخی از این دزدا داشته باشه و بهم بده ، 10 میلیارد تومن بهش پاداش میدم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71078" target="_blank">📅 10:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71077">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0def551e36.mp4?token=NT94C0pX42DmXWVBhWFzbt8GFTb2b0B-J1HthB0uv0MG8kch7pOxUFG02IEvpMLqdT-lROl5e3VldlIKHjUHAAkpGDVNqGpQ3TXYW33BuftkJ14vdF1Ub7zcBFQxZ17rp14b33_UNBItomFDkjlbZ1tO7n_ov1gPIi8rCSz0KCOrKrm4lMqNgRddWxHWvzxcB49XZBEfX_UqLluL0Cb2UEaeupaHvFXCyg_pBk1EmTE80r9eaaTve-cpVuxVU4raC-kde6nPuGTcRW_ATWIKiOXLFiUxHkUvYkew7MHKQstkMhi0wwStuHct1iOOkEIQMiiD6CDyhPZx3a0fUsYgVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0def551e36.mp4?token=NT94C0pX42DmXWVBhWFzbt8GFTb2b0B-J1HthB0uv0MG8kch7pOxUFG02IEvpMLqdT-lROl5e3VldlIKHjUHAAkpGDVNqGpQ3TXYW33BuftkJ14vdF1Ub7zcBFQxZ17rp14b33_UNBItomFDkjlbZ1tO7n_ov1gPIi8rCSz0KCOrKrm4lMqNgRddWxHWvzxcB49XZBEfX_UqLluL0Cb2UEaeupaHvFXCyg_pBk1EmTE80r9eaaTve-cpVuxVU4raC-kde6nPuGTcRW_ATWIKiOXLFiUxHkUvYkew7MHKQstkMhi0wwStuHct1iOOkEIQMiiD6CDyhPZx3a0fUsYgVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه دختره داشت تو قزوين واسه خودش قدم میزد؛
که یهو یه پیرمرده خواست مزاحمش بشه ولی بعد که فهمید طرف پسر نیست، عذرخواهی کرد و رفت
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71077" target="_blank">📅 10:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71076">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4ba13b0e17.mp4?token=lB6wC25nNbKEM0qPflMKplHwQWWP6t-DpYgZMBIxuBPtURJMcQzVyNVOun2sI2juMzzdqslDrf6xCGACYydNEE8getbRvjEb1UDdI9Y-ijHbe-QsTjPNPw-1b8o0iyrSLOPvmxfADMWWnaK2IVTI5U3o5Fjl0BwOkKvucaDHlZ6IYPmV68ABc1k6D7bC2WEzeh7HmQK7f7f4Hi2f3Xcie53Iruu6WzLC0dkHSKg-aoV1jmVuq3CAk4HIEwjaKlUT2qbJsBg1GupqbinQjDeFiQMN7bj3ENH3n989IJ6naziIqVQ08QfRRo3w3z0RGtKdf1jREVRW4l97AJZ_-1R60Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4ba13b0e17.mp4?token=lB6wC25nNbKEM0qPflMKplHwQWWP6t-DpYgZMBIxuBPtURJMcQzVyNVOun2sI2juMzzdqslDrf6xCGACYydNEE8getbRvjEb1UDdI9Y-ijHbe-QsTjPNPw-1b8o0iyrSLOPvmxfADMWWnaK2IVTI5U3o5Fjl0BwOkKvucaDHlZ6IYPmV68ABc1k6D7bC2WEzeh7HmQK7f7f4Hi2f3Xcie53Iruu6WzLC0dkHSKg-aoV1jmVuq3CAk4HIEwjaKlUT2qbJsBg1GupqbinQjDeFiQMN7bj3ENH3n989IJ6naziIqVQ08QfRRo3w3z0RGtKdf1jREVRW4l97AJZ_-1R60Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه دستگیری یه قاتل فراری در ایرانه
:
قاتل با چاقو مامورا رو میزنه و داشت فرار میکرد که یکی از مامورا عین راموس تکل زد و طرف افتاد.
بعدش یکی دیگه از مامورا ویلچر برداشت و میکوبید تو سر و بدن قاتل تا بیفته زمین، هر لحظه این فیلم عجیب‌تر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71076" target="_blank">📅 09:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71075">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uviL1Appr9Zo9vCep2giF63zEmKW9F1SWRQ9zQVmqUufjdLYeprGE0OUUpyuEt0JzBs7QUX9-cbM8HP4rfwukV60RCAdwCSQpWpe6KpF-yMucypFXsH9SbMo0sWXzhRX_saiQnhyV5JN3if_ROejIA4sBPytqK2MWvhqHb9c-OYTSFjXPZPe_zs9uDs2ku6xyWJAF5N_mvomN7XsTYpdJh2fYWQ2OE0pZj2QuHwrccn1K_XJsZcn-krAefyz5TpEhUBBVcA74GIrL0J1LljyKRrWOTri9XyC0eh52bf8LoQJPSP5x4L4qoovRGKHfATVZ5_xTc-CEHB8CT9Ozuss_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
⭕️
#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا:
اتحادیه اروپا رسماً به «عملیات طرد اقتصادی» (Operation Economic Outcast) پیوسته است و ما از موضع قاطع و زودهنگام آن‌ها قدردانی می‌کنیم.
ایالات متحده در کنار متحدان خود قاطعانه ایستاده است تا اطمینان حاصل کند که رژیم جنایتکار ایران نمی‌تواند از سیستم مالی جهانی برای تأمین مالی جاه‌طلبی‌های هسته‌ای، برنامه‌های تسلیحاتی و نیروهای نیابتی تروریستی خود بهره‌برداری کند.
جهان پیام روشنی به رژیم ایران می‌فرستد: ما تا زمانی که آخرین شریان حیاتی مالی باقی‌مانده قطع نشود، از تلاش دست نخواهیم کشید.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71075" target="_blank">📅 09:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71074">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71074" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71074" target="_blank">📅 01:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71073">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0uBjoyU_yH88afBsots2syoxPMQtCVsKVjnqgiQWlks9xnZHcGB9lS6pfnlr6-m7GKnGZcmR74HC3kBG2HgTaJlL6QuOFlz2VBbzlK_CcPgEdyRh2ndDka95QEgi4lYaYZugPP72KJ3oKJFpHQZQzRQkote_o-PLW5NJ5lOvO5V1kLa6jteOZmHJpZnlJUchGjr5GiSpCs4-gjdKH4nSj05B-TlJ7VfM7GecT90dkP44W3yga_VQwO5VrtEFy5Xn4lHdb64rwDcu2MFTDD2uFYJNei_EixVg8SF1__g8XYweNqyM_F2aPt4-vUJgIzAxMoyEvYEeXiMuLGUJYVtVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71073" target="_blank">📅 01:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71072">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🇮🇷
نایا:ایران چندین موشک به سمت کشتی ها در تنگه هرمز شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71072" target="_blank">📅 01:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71071">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c46c090035.mp4?token=Qb-4bY9NSCsACfEPJ_doRfq5C8ICWNmqLwCRpSlHAuVTHpSf9SBg5R4IXe-8aRzAnjBKpRGv4_vcCC6NRkjdvTMacMRgVPw6NVVGreNhCYxD3qQ0QPsu6_BC7IM9srPniWtKGkh_o2pXYsv00PlqXWdcEpIfxI25NFRFYFCC1gvWuNbYJfMyZhiug1ZD-xCRIGpr6q-Jbps8gdCDPL8y4g9eb73JcI920LTse9c-m0CLGq0CXuAFV2Y8slV_F70tNdnGA28wDR6csfa3Hl7RAOAVy7TXocRQa5PnvIL2dz5lbUdaRf8G8ZFQlCFKRU70YiOyHvOU3O9a_xXlV889jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c46c090035.mp4?token=Qb-4bY9NSCsACfEPJ_doRfq5C8ICWNmqLwCRpSlHAuVTHpSf9SBg5R4IXe-8aRzAnjBKpRGv4_vcCC6NRkjdvTMacMRgVPw6NVVGreNhCYxD3qQ0QPsu6_BC7IM9srPniWtKGkh_o2pXYsv00PlqXWdcEpIfxI25NFRFYFCC1gvWuNbYJfMyZhiug1ZD-xCRIGpr6q-Jbps8gdCDPL8y4g9eb73JcI920LTse9c-m0CLGq0CXuAFV2Y8slV_F70tNdnGA28wDR6csfa3Hl7RAOAVy7TXocRQa5PnvIL2dz5lbUdaRf8G8ZFQlCFKRU70YiOyHvOU3O9a_xXlV889jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پورمحمدی:
انسداد تنگه هرمز، برنامه‌ریزی شهید پاکپور بود.
شهید پاکپور پیش‌بینی کرده بود که جنگ با ترور او شروع می‌شود.
شهید پاکپور برنامه‌ریزی کرده بود که اگر جنگ آغاز شد و او دستوری صادر نکرد، فرماندهان ۲۰ دقیقه بعد شلیک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71071" target="_blank">📅 00:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71070">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46300e7107.mp4?token=BtN5H3tPX3mwYi2VIWI071Bxwj4b4rLA5XYRAuvm2d7TYSJtnPxGYSuhIZXtL9qt8eXm6bvS3laHEYl_Xi1t6P32PPZqZgZlQTgMv8gbdR6caprKbMoeQPLkCt7YiNE_y5QamLBBj5pD1XJmTNeB5ADOYPcf0wwlt4Q0U1Nkgfg45n__C40jfx1c04cFUJZLA0GfBm1y2C2XmJksiBVT7INQgrEc7WL-3o7iBJ_iotjY16CZrUUBAeKy_MHOsYV5zdn1dWqddU0tq1MDCcEHB2e9mvNK7shUaoA9VNhWOaN7UDsDy2BHJJSbAIqky9rUluQimQaXmpnD1YGr-tBgXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46300e7107.mp4?token=BtN5H3tPX3mwYi2VIWI071Bxwj4b4rLA5XYRAuvm2d7TYSJtnPxGYSuhIZXtL9qt8eXm6bvS3laHEYl_Xi1t6P32PPZqZgZlQTgMv8gbdR6caprKbMoeQPLkCt7YiNE_y5QamLBBj5pD1XJmTNeB5ADOYPcf0wwlt4Q0U1Nkgfg45n__C40jfx1c04cFUJZLA0GfBm1y2C2XmJksiBVT7INQgrEc7WL-3o7iBJ_iotjY16CZrUUBAeKy_MHOsYV5zdn1dWqddU0tq1MDCcEHB2e9mvNK7shUaoA9VNhWOaN7UDsDy2BHJJSbAIqky9rUluQimQaXmpnD1YGr-tBgXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
چندشب پیش تو شیراز یه دعوای عجیب رخ داد؛
دوتا دختر با ماشین میزنن به ماشینِ دوتا پسر؛ بعد گفتن ما مقصر نيستيم و داشتن فرار میکردن!
پسرها هم گفتن چون بی‌ادبی کردی، باید بمونی خسارت بدی، بخاطر همین پریدن رو کاپوت ماشینِ دختره که فرار نکنه!
این وسط یه پیرمرده هم خیلی بی‌دلیل از دختره کتک خورد...
تهشم دختره گفت دیگه این موضوع واسم مهم نیست چون زنگ زدم شوهرم سروان شهریزی، الان میاد کون همه‌تون رو پاره میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71070" target="_blank">📅 23:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71069">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876466a913.mp4?token=Irj5zPQIUEsEWNHOswnkbOrpA-6WOgczgWPECHGvXF--nNb9WotPi7RJ8E9ec3-qrfciIvD2zC9XejB-ut3MXkrOLpDWTFbrIjHTGHmppee-MG9Vwj5Y7p6Ga26mLdYS_LCHCwtPGC00dK__PAx9Lw00CDsgwpHTkjNIhovPNjw_V4EIxG40_Og0uEZf7y68xjKrQBasonKE-CU5seBvB-RtB5dGdPXwEn5IMSSg8mpCLsXH-QtNdBS-_o2-dZDY9pyNzVigwIrv1rS_j3sR9V8vaXbIQ0Sd2P9_k7-3O5dylapMjheBHlo-FQ8cjRRoOzdoZD2YFW5yoo01UQ40Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876466a913.mp4?token=Irj5zPQIUEsEWNHOswnkbOrpA-6WOgczgWPECHGvXF--nNb9WotPi7RJ8E9ec3-qrfciIvD2zC9XejB-ut3MXkrOLpDWTFbrIjHTGHmppee-MG9Vwj5Y7p6Ga26mLdYS_LCHCwtPGC00dK__PAx9Lw00CDsgwpHTkjNIhovPNjw_V4EIxG40_Og0uEZf7y68xjKrQBasonKE-CU5seBvB-RtB5dGdPXwEn5IMSSg8mpCLsXH-QtNdBS-_o2-dZDY9pyNzVigwIrv1rS_j3sR9V8vaXbIQ0Sd2P9_k7-3O5dylapMjheBHlo-FQ8cjRRoOzdoZD2YFW5yoo01UQ40Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق گفته خانم دکتر؛ دیگه خوردن واژن خانم‌ها نه تنها دیگه نباید باعث خجالت شما بشه بلکه پر ازخاصیت و فواید زیادیه که تاحالا درجریان نبودیم!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71069" target="_blank">📅 23:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71068">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6EKq2VPItX73ES-1cn5J8nk1M2ISPmoiouxWixYRugxG6cJ3xaBFsZ3_7U5MQkJl7AXtW_9Dxi15154zM8tKzV3vKbr3DKn6avb4OLiFOd3MTVLsSf_wXcQZpQgvgUfji_Bt0B1EwbOM1wqIhCoWgZSBJFN1Zuif_z1nzo-yCTEy7YKgKRPgNjzJtnsysJLMPaR-a9TG1-c7esd8F7893HQ3-yH4eu0QwHUO4dT4xBf_ednr6SowaGNFDTFjLeETf4ixMhgYGHduiOJ4xVq5Yl1BgEALToCMpOvW3NEHiqmN12hT4Yn3h2ILePfWwJMgvt9Gs3fxkbNLjk_VRN_eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیبافِ:
قهرمان، محکم‌تر «شورت» (Short) کن؛ طوری که انگار آینده‌ی شغلی‌ات به آن بستگی دارد (چون واقعاً هم همین‌طور است).
یا اینکه سطح ذخایر را به زیر «منطقه خطر» برسان و فرو ریختنِ آن حفره‌های عظیم (و البته نابودیِ شغل خودت) را تماشا کن.
یا هم به درگاه خدایانِ نمکِ «برایان ماوند» (Bryan Mound) دعا کن.
دنیا که از همین حالا بساط پاپ‌کورنش را آماده کرده است :)
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71068" target="_blank">📅 22:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71067">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f701b5944.mp4?token=Zi9x-9vcyeXgU8LaxNvgnYIU_PEWDiEwLqN22QZvH2Zh8dLdibIJqZZ4VkpVnPi40-aVPsyWWbHx_pEUiWyCrsk10EqZDi3Faox44SdpKqgHcZKJVK9a7Xr7Qf6QqNpug-Alg2aOfF7KBsYK0c1LKMwU5hyjY0AFI1DEsYkMpWLK7uRpr0NMq-o8xlvMupXqz7lXr2oLkWMzyg-J0O_S9wtTrx50yayRm95xh-GVFWKixImrnYkMiyvZrUNgOhNPGIeSRml3y0m1LAkwqUfIkeDbg8FLFyj0685bRPHD4Tl52cqqjVFaYiqsbXrSyRBwEYvsmJaoOaxw9v9jVn11Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f701b5944.mp4?token=Zi9x-9vcyeXgU8LaxNvgnYIU_PEWDiEwLqN22QZvH2Zh8dLdibIJqZZ4VkpVnPi40-aVPsyWWbHx_pEUiWyCrsk10EqZDi3Faox44SdpKqgHcZKJVK9a7Xr7Qf6QqNpug-Alg2aOfF7KBsYK0c1LKMwU5hyjY0AFI1DEsYkMpWLK7uRpr0NMq-o8xlvMupXqz7lXr2oLkWMzyg-J0O_S9wtTrx50yayRm95xh-GVFWKixImrnYkMiyvZrUNgOhNPGIeSRml3y0m1LAkwqUfIkeDbg8FLFyj0685bRPHD4Tl52cqqjVFaYiqsbXrSyRBwEYvsmJaoOaxw9v9jVn11Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
ارتش اسرائیل تپه علی طاهر در جنوب لبنان را فتح کرد و کنترل آن را در دست گرفت.
ارتش اسرائیل پاکسازی دو مسیر تونل زیرزمینی حزب‌الله در رشته‌کوه علی طاهر در جنوب لبنان را به پایان رسانده و در تلاش برای خنثی‌سازی آنهاست.
لشکر ۳۶ کنترل عملیاتی رشته‌کوه را در بالا و پایین زمین به دست گرفت و آن را از وجود شبه‌نظامیان پاکسازی کرد. برخی کشته و برخی دیگر فرار کردند. خنثی‌سازی زیرساخت‌های پاکسازی‌شده در حال انجام است.
در داخل، نیروها مراکز فرماندهی، اتاق‌های تسلیحات، اتاق‌های ژنراتور، محل‌های زندگی، دوش‌ها و یک آشپزخانه را یافتند -- که به شبه‌نظامیان اجازه می‌داد عملیات جنگی را انجام دهند و برای مدت طولانی در زیر زمین بمانند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71067" target="_blank">📅 22:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71066">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jD5mTq23NrS3N1QATvyhHWUUKA2x8wtF18C7UzjnPxNBS1l0krkYV0W7JZPzcIdPgoi5a4mkhMkfNHoT-d55OTh4k7ekAK_6-SnkhftZrb2Dlii4IaGhKgdKpPOCwehSYRs6f9I13j2D6kBc4bv2wMoHDWkMFw8rkMUAOqoacvWKON9orPI-ab4KFts7dSeM68kMVh7-_845XlB7yclnzrdyWTSYBAcUNUCWgPtFz0q7Kg1Adjfwx9Podtx8yIQr0AA7nHVmBn2aAtRwhSL69P_tU8QgSL6W5uvxsFr_I1WRP3e1mgb-sC3eVpEG7Ok8rrv45BYWk2WkkEFd-A0tpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرید حضوری با اسنپ‌پی، یه خرید معمولی نیست؛ شانس بردن BMW داره!
😎
🚗
با اسنپ‌پی می‌تونی از بیش از ۲۰ هزار فروشگاه حضوری خرید کنی و هزینه‌اش رو ۴ قسطه و بدون سود و کارمزد پرداخت کنی.
🎉
🥳
همه‌اش همین نیست؛
۵ هفته، ۵ برنده، ۵ جایزه در هر هفته هم در انتظارته:
🏆
۵ گرم طلا
📱
گوشی Galaxy S25FE
📱
گوشی iPhone 17
💻
لپ‌تاپ MacBook Air M4
🎮
کنسول PS5
این شهریور، حضوری خرید کن و شانس بردنت رو بیشتر کن:
👇
👇
👇
https://l.snpy.ir/iozfb
https://l.snpy.ir/iozfb
https://l.snpy.ir/iozfb</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71066" target="_blank">📅 22:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71065">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af33ae7319.mp4?token=thHqyNxX_uioUg1bhj7SVTmKdWpO59zuHeiqf0_ecM2nAyYf5EdHCi-cjbB_6brs90Ax9l1utU83tObUUVpKTBMuFv2NvKwDpOp1A_A1xOE4xZ8PZT_efct4Ed3BRyBTyWnci1EQSrEtk9d2bKuwE19l7DmNINYQZw5X9kz8_4CHY7Y2zlS7mVdkkHw6RJjLwGAyqX5wuk_diyziQcqxM9eCEJt-DP7J7iYUWnQBBRP6M3utcMdIchtbWSdyVBDrPAI2GidLoPrAlbdHUdpjBpS3NXyrDFoKJ2Ui5fKxD8fEiWy4q56soT6znSCDS61NcAi32-r0NUVrnagYxme4LLF_4HuF4lj6UoBm7l5duNc-TpzwQHza0QytMRZmKyB9POezdTfeRTK8aEDVkT0tER8OxRtK_IjPDgMoPFXdAXZTmtJCYJQXYCApOF9Tzt24xHQZADBcEqRIMN0OhZ3k4iBJ7CHZZL6EDneRKffhU_iEkspl1NGA2udMDLv79Nh0t4do4zNua8WxYvZEEXdjvIGXbnFGwtmLOdzWE6zbYPzrODr68oOfKcn2UNUyWfm9xUk2cXGNMBSiHC7_LAXrhK32CVP-6ElPYRx0olBqWAxpuNwNawOYqhhm1xJ4WMB10Xy320R-4ieS3zI_Jyz2Cm3RjmSf2HdKRevFoIEym7E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af33ae7319.mp4?token=thHqyNxX_uioUg1bhj7SVTmKdWpO59zuHeiqf0_ecM2nAyYf5EdHCi-cjbB_6brs90Ax9l1utU83tObUUVpKTBMuFv2NvKwDpOp1A_A1xOE4xZ8PZT_efct4Ed3BRyBTyWnci1EQSrEtk9d2bKuwE19l7DmNINYQZw5X9kz8_4CHY7Y2zlS7mVdkkHw6RJjLwGAyqX5wuk_diyziQcqxM9eCEJt-DP7J7iYUWnQBBRP6M3utcMdIchtbWSdyVBDrPAI2GidLoPrAlbdHUdpjBpS3NXyrDFoKJ2Ui5fKxD8fEiWy4q56soT6znSCDS61NcAi32-r0NUVrnagYxme4LLF_4HuF4lj6UoBm7l5duNc-TpzwQHza0QytMRZmKyB9POezdTfeRTK8aEDVkT0tER8OxRtK_IjPDgMoPFXdAXZTmtJCYJQXYCApOF9Tzt24xHQZADBcEqRIMN0OhZ3k4iBJ7CHZZL6EDneRKffhU_iEkspl1NGA2udMDLv79Nh0t4do4zNua8WxYvZEEXdjvIGXbnFGwtmLOdzWE6zbYPzrODr68oOfKcn2UNUyWfm9xUk2cXGNMBSiHC7_LAXrhK32CVP-6ElPYRx0olBqWAxpuNwNawOYqhhm1xJ4WMB10Xy320R-4ieS3zI_Jyz2Cm3RjmSf2HdKRevFoIEym7E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر ترامپ هم اومد به بازار
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71065" target="_blank">📅 21:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71064">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40c15e0881.mp4?token=SBiMiqr-dbGE3H2xnb3llFCYdG5CG-pK8Y8pcco7HF8j_eYBzoZgraOYsVmz9A9lI1eJq5c6iFP87Xg_wdAZ1DAC_9c9n8AI240PELiRx9_ctpH3lXwmzoynxJ01XMlB3bLe0-tdUByLAIlSpoDfZyqiwEpA-a6myy2Y1X1xIIM5fpeBwq0x9Rnq6ZwJFwD1dKpiV0Z2H3Osae9C-ZqG5iEdi2UA90r1WKKQ02K6nKtjVS9HuzcH2SXwPFAYH6YJcMDXeZRpYmnUK6ZRi1_SG3gkT0d7Ca1AdjaUrppzKgRqEEuiskt-SBUwsYkYeJrC7N9XOi1xzV1V3IK8HKqj3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40c15e0881.mp4?token=SBiMiqr-dbGE3H2xnb3llFCYdG5CG-pK8Y8pcco7HF8j_eYBzoZgraOYsVmz9A9lI1eJq5c6iFP87Xg_wdAZ1DAC_9c9n8AI240PELiRx9_ctpH3lXwmzoynxJ01XMlB3bLe0-tdUByLAIlSpoDfZyqiwEpA-a6myy2Y1X1xIIM5fpeBwq0x9Rnq6ZwJFwD1dKpiV0Z2H3Osae9C-ZqG5iEdi2UA90r1WKKQ02K6nKtjVS9HuzcH2SXwPFAYH6YJcMDXeZRpYmnUK6ZRi1_SG3gkT0d7Ca1AdjaUrppzKgRqEEuiskt-SBUwsYkYeJrC7N9XOi1xzV1V3IK8HKqj3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
رقص عجیب «حسن حسین خانی» مداح نزدیک به حکومت  در حالی عجیب  و  با شلوارک! تو یک  ویلا با آهنگ شماعی زاده
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71064" target="_blank">📅 20:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71063">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0392122fc9.mp4?token=l2elL4U62i_IR2u9quADusLrQt-t5ObQYeQigX9cJ6T7iNMF0SQbzbdHQmUJRMlcosJ3iW_fgTHoSsZmPoCOI1uamZm2Sgqssx2wEho_SWtIwrII3BBIIhVhUnuMD4jDPkKebUAbI6Xk8vk5SIM1UPpm2vBpuoLEr9d_ODYmHp8Yoq9gZGEH6956pW1oPMo0-08UvrL0dKp_yLdieKwhGu9tL5C6W_0bsacHq9WthozQHmdyrd0cdhyDdr3JCzVbHhfNURinzG4cZnOamqO4fk-Cug0WvWTxSDwBmuaZPp-n4EWGnfItyRtAqqwhQ-8RWLqIiCl70k3N9nNUxbwyAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0392122fc9.mp4?token=l2elL4U62i_IR2u9quADusLrQt-t5ObQYeQigX9cJ6T7iNMF0SQbzbdHQmUJRMlcosJ3iW_fgTHoSsZmPoCOI1uamZm2Sgqssx2wEho_SWtIwrII3BBIIhVhUnuMD4jDPkKebUAbI6Xk8vk5SIM1UPpm2vBpuoLEr9d_ODYmHp8Yoq9gZGEH6956pW1oPMo0-08UvrL0dKp_yLdieKwhGu9tL5C6W_0bsacHq9WthozQHmdyrd0cdhyDdr3JCzVbHhfNURinzG4cZnOamqO4fk-Cug0WvWTxSDwBmuaZPp-n4EWGnfItyRtAqqwhQ-8RWLqIiCl70k3N9nNUxbwyAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
#فوری
؛نخست‌وزیر نتانیاهو درباره ایران:
من به توانایی‌مان برای از میان برداشتنِ یک‌بار برای همیشهٔ این تهدید ــ یعنی سرنگونی این رژیم ــ اطمینان کامل دارم.
این همان مأموریت اصلی است که همچنان پیشِ رو داریم، اما به تحقق آن نزدیک شده‌ایم. این کار غیرممکن نیست؛ بلکه کاملاً دست‌یافتنی است.
آن‌ها بی‌دلیل از حمله به ما پرهیز نمی‌کنند؛ آن‌ها به همه حمله می‌کنند، جز ما. آن‌ها از قدرت ما، توان بازوی ما و عزم راسخ ما آگاهند.
من خطاب به دشمنانمان به‌طور کلی می‌گویم: با ما درنیفتید. اگر درسی گرفته‌اید، بدانید که نباید با ما دربیفتید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71063" target="_blank">📅 19:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71062">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
شلیک موشک/پهباد از سیریک به سمت کشتی ها در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71062" target="_blank">📅 19:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71061">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veV9sDt2yUwv79728uZFt_i-gSfXw-8UP-pvglmjeaUjZJqThEBZwZM_ijorsq2nR8-DdpRhqTXrUOEI2tRYx-2u-tn15QMbRiJ6OdDxi8wK07-U2Au5X6jPPEQgnctJrlU6OacYX0IiJe_eeA4M9rw4MKa_CwWdbd240KHV96FS9LB0VAYBLZ2SoUAwabE736kgAm0qnFNwmaP_RptFUZAZkWviVvrH5n7Hq3e8TBD0SA22vKnp2pFV6jJpwz2vvz0E-vkKgamzwHQZ7xwJ-5zwxjAEq3SLzUq67H_EYRcbrCBfzGip-A3TMZ4mcInSre1w2DSFRUCWHapHMqsRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
برای آن مشتی خائنِ پست‌فطرت که از گزارش دقیق عملیات نظامی ما در ایران خودداری می‌کنند، باید بگویم که ما ذخایر تقریباً نامحدودی از مهمات با کیفیت متوسط تا عالی در اختیار داریم؛ بسیار فراتر از آنچه ممکن است برای این عملیات یا هر جنگ احتمالی دیگری (که وقوع آن بسیار بعید است!) نیاز داشته باشیم.
علاوه بر این، ما در حال تولید مهمات با حجمی بی‌سابقه هستیم. ما در حال انباشت و آماده‌سازی برای مقابله با هرگونه وضعیت پیش‌بینی‌نشده‌ای هستیم که ممکن است رخ دهد.
ما این مهمات را برای خودمان — یعنی ایالات متحده — نگه می‌داریم و فعلاً به دیگران نمی‌فروشیم، هرچند فروش به متحدان به‌زودی از سر گرفته خواهد شد.
همچنین، لازم است بدانید که دولت بایدن حجم بسیار بیشتری از مهمات را — بدون دریافت هیچ‌گونه هزینه‌ای — به اوکراین واگذار کرد، که این مقدار بسیار فراتر از مهماتی است که ما در ایران به کار گرفته‌ایم.
صدها میلیارد دلار کمک رایگان به اوکراین و ناتو اعطا شد؛ هزینه‌هایی که اگر از اروپایی‌ها خواسته می‌شد، خودشان آن را می‌پرداختند.
با این حال، ما آن پول را مطالبه خواهیم کرد، هرچند با کمی تأخیر!
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71061" target="_blank">📅 18:52 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71060">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21cce2e5e.mp4?token=knDV3Etp_Yq8nzl9Q-ztLPN8atzpXoWJV262sB73AokKOmZ4LwDDKOWKTW4nmV_R2bvsPrvFmzrRVfacjmGYIx4-71pbxv3JvCmolvL632kKGWIGK7Vkq3KYBhbJPVty77ryplO_7oDw_Su4oHy6r1gSv6d1old9mfF9h9M6KQdSNqSgF0e61gsC6OAGfw-EevoSPqmUHVKkItxAxvfadu63-CDUpOy8BobhT1De6WqZYpforL0KbMdI6_pfDpLHMog2f3NvP67_zYQtyGWEaHYYwBTB-w9vlvsOqRBln59D3MoaNfEp78eY4J78sSL0-qItJ6_rJNcbYe-RxDSE9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21cce2e5e.mp4?token=knDV3Etp_Yq8nzl9Q-ztLPN8atzpXoWJV262sB73AokKOmZ4LwDDKOWKTW4nmV_R2bvsPrvFmzrRVfacjmGYIx4-71pbxv3JvCmolvL632kKGWIGK7Vkq3KYBhbJPVty77ryplO_7oDw_Su4oHy6r1gSv6d1old9mfF9h9M6KQdSNqSgF0e61gsC6OAGfw-EevoSPqmUHVKkItxAxvfadu63-CDUpOy8BobhT1De6WqZYpforL0KbMdI6_pfDpLHMog2f3NvP67_zYQtyGWEaHYYwBTB-w9vlvsOqRBln59D3MoaNfEp78eY4J78sSL0-qItJ6_rJNcbYe-RxDSE9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
کسانی که دوستتان دارند، شما را فردی خوش‌برخورد، شوخ‌طبع، سخاوتمند و بذله‌گو می‌دانند؛ اما دیگران می‌گویند که شما سخت‌گیر، متکبر، مغرور و حتی بی‌رحم هستید. به نظر شما، کدام‌یک از این توصیفات درست است و کدام نادرست؟
❤️
شاهنشاه آریامهر:
بی‌رحم؟ گمان نمی‌کنم.
متکبر؟ قطعاً نه.
مغرور؟ شاید کمی. اما در مورد کشورم—و آنچه به دست آمده است
نمی‌توانم شخصاً دچار غرور شوم، چرا که انسانی مؤمن هستم. من عمیقاً به خدا ایمان دارم و اهل عرفانم؛ پس چگونه ممکن است مغرور باشم؟
انسان در پیشگاه ذات ازلی، هیچ است؛ مطلقاً هیچ؛ گویی اصلاً وجود ندارد.
البته با نگاهی به دستاوردهای این کشور، قطعاً دلیلی برای احساس غرور و سربلندی وجود دارد.
اما بی‌رحمی؟ این ویژگی من نیست؛ این نهادهای حکومتی هستند که باید عمل کنند.
وظیفه آن‌هاست که کسانی را که قصد آسیب رساندن به این کشور را دارند شناسایی و خنثی کنند. اگر نام این کار بی‌رحمی است... خب، در آن صورت باید بپذیریم که در این مورد با هم اختلاف‌نظر داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71060" target="_blank">📅 18:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71059">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/259e330a05.mp4?token=rDwMLiwbaMgoDLAvTOX4JRCgrdDbtW5xwPndpQIzw3EOGrGfTNQLiJeYndqNn4ivuSG6XVlwQyeCDLHtXRUfhmtGBlfGGpPAfhwuwpPWD4pEGfRzhDK-9zptAPh7riCf2_75xz0wtPHSbwUE0xWs42iRp_jMAKlg-eJ9i6FzwVw_LYJfpBWkUlnsTkHVKXrgLdnE-4RiTZsxAUCuyAfPYy-mr957HjWCci6iAjj5cOwJgPvQVKaofB3qNfqtndPxfmk_V0aBC_vB_LTlGP3BOE0NsvGNF3021hEp7kGqicpeILetygS8H3_LnO7vK5AoamYDCPRn0Q-foklFqR-7aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/259e330a05.mp4?token=rDwMLiwbaMgoDLAvTOX4JRCgrdDbtW5xwPndpQIzw3EOGrGfTNQLiJeYndqNn4ivuSG6XVlwQyeCDLHtXRUfhmtGBlfGGpPAfhwuwpPWD4pEGfRzhDK-9zptAPh7riCf2_75xz0wtPHSbwUE0xWs42iRp_jMAKlg-eJ9i6FzwVw_LYJfpBWkUlnsTkHVKXrgLdnE-4RiTZsxAUCuyAfPYy-mr957HjWCci6iAjj5cOwJgPvQVKaofB3qNfqtndPxfmk_V0aBC_vB_LTlGP3BOE0NsvGNF3021hEp7kGqicpeILetygS8H3_LnO7vK5AoamYDCPRn0Q-foklFqR-7aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های این پسر درباره‌ی اونایی که میگن کسایی که ریش ندارن کونی هستن رو با هم ببینیم:
کدوم مادرجنده‌ای اینو باب کرده که هر کی که ریش‌وسیبیل نمیذاره، کونه؟
شما برو فیلم سوپرا رو نگاه کن، عمو جانی کونش هم یدونه مو نداره، چه برسه به صورتش.
ریشو کسایی میذارن که ترس از کون‌شون دارن، اونایی که عقده دارن و بچگی کون‌شون گذاشن، ریش میذارن.
خیلیا ریش دارن ولی صد مرتبه از کونیا بدتر هستن
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71059" target="_blank">📅 18:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71058">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71058" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71058" target="_blank">📅 18:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71057">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehEe6Tqqv5QWakTNhOwATGkYoYO1aqccgXAls3WVw9_hz1zjFxjBjicWXZGioo8AeLlCxohZ8SqCsk6mEA_59lQdg24uqTd0JAsrgGZg69MNJQRAzH0gmIgto5IAY6ushnCerCGi7AxiMllrDuos8RPPDjsyF_-Gx3qp-UZF8vAGGxhLqux1HCw76rRwtCNrFaqSKa5oZZCEWH7dPn__PujaLOO4GVhMpJ9iNwQsM4VZV4bDrY3SOmm-9SIWF66hUBo6B3jNpEHklvdKjSgt3IuL9t7Kkve551Jny8ZKQnbJp0M0xHXSlkjRrgmNjo5_BWQDfNXeV25E87Ph8eyBhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان
US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71057" target="_blank">📅 18:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71055">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQ3SPsaCZPmTrvYQBmg0XiYVF58QVZOn6i8DNZjNqsaDKEERno1SJ1dn6Py9_f2t9qfCOJUqcyP1ms3SOxKzKhbGFDg9WzMbjMS6WBNfnKSSXL26fvxwzeAZTFNSqFWREada7fC4Yy6yYJ5ZfxiCTQ1WDYvoTngdciMTf4YQJPwIwWCmSI0Um5lFy135yfejysbcThaVcDwwSQuzxCtMy9A5u8dVG_iseptnSXgkhvYKO9zHezsoYijW9SiBs9OjaGyZSoYggoRbRWryHeCrkkCE9i5MgMfFTdqrXs2SLNv4dDrUCSXvqCX4MCFv43GdfSdVXBrRtPE-0P60IT4XLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
💬
🙂
پست جدید تلگرام در پلتفرم ایکس:
حس و حال بامزه‌ای دارم، شاید بعداً عکس‌های نودم رو منتشر کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71055" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71054">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_1ooZmXihuImHOJFFqOUCzotaZ3l5nw01LqA51Ux_vpjBwa-PguLPtr0nnyMQqbCQuII-7hcJxSIM4Hsbk6Zgg2U658oMQmCM7CkwumWKnYwTIyqg-A8ogv8I9WqsiZPiQhR3rl_5xmPxu4cvIi4BURfLDDO9JnTqu6qh7YEwJg9K5rP2wmRnPuHZY0efIiemi0T3FcYv79Pa-sorvAR07AimAfLZjU7YhsIjXfssLfIqwikA6Y_RR9wq5OOXweCLQvoaUNf5DHzNm_Mu2ZTWEUgSnmsNpA0SqHx-ZyNO1FmCrBpDO70Q_OpatmvxrNY27YW9ZQXzCCn-xloTOQ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
جمهوری اسلامی کشته شدن سه خلبان نظامی در حملات آمریکا در دو شب گذشته را تأیید کرد.
اسامی: مجتبی باقری و حامد اوکاتی (خلبانان هوانیروز/هواپیمایی نیروی دریایی) و حسین مهدویان (خلبان نیروی هوایی).
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71054" target="_blank">📅 16:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71053">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03924aeb44.mp4?token=AFtuNV-11RyA9Mm3HxOGPg4-ROC8ZedLyWwTJ6QmbuLd9USA60KoGt57gbsZwlK2a3_iqQ_5sB2ywP1yGj3qRhpTtzUavIn_L7bPFO5j8Ib2hMrJkEOLtHm0sq8dUV6ORZcZ-ovDkR0XSEy-esDR7-HI-eLXSQf_D9LmK0dnNY7J4HTin3rbp20SDQ2g-90S1yXWmuQdI38KVYeGOsjYBTkJUQmtmi7Znrp1j0RPVFV53fVklAhZuhj2RSOvtoyRqhSJgTXCJVMRitRZG90El_6KDDABBTFUzr0sG-vnqmaeZ4pf2lvP_aDp9z70vWnWdkt6nfQJA-_6nCmDizviaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03924aeb44.mp4?token=AFtuNV-11RyA9Mm3HxOGPg4-ROC8ZedLyWwTJ6QmbuLd9USA60KoGt57gbsZwlK2a3_iqQ_5sB2ywP1yGj3qRhpTtzUavIn_L7bPFO5j8Ib2hMrJkEOLtHm0sq8dUV6ORZcZ-ovDkR0XSEy-esDR7-HI-eLXSQf_D9LmK0dnNY7J4HTin3rbp20SDQ2g-90S1yXWmuQdI38KVYeGOsjYBTkJUQmtmi7Znrp1j0RPVFV53fVklAhZuhj2RSOvtoyRqhSJgTXCJVMRitRZG90El_6KDDABBTFUzr0sG-vnqmaeZ4pf2lvP_aDp9z70vWnWdkt6nfQJA-_6nCmDizviaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تو ایتا و روبیکا با انتشار این فیلم نوشتن سامانه پدافند لیزری جدید اومده و همه موشکا و پهپادای آمریکا رو با لیزر زده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71053" target="_blank">📅 16:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71051">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94edb900f7.mp4?token=MCusr5771wzyxVik0tyUz1pxlqo3vOxbuPFP3j29JYhe11loT4P4UAPivThgF3zvj2pL6Uc_wjG9pAcM-smGYl0XY326VCs6Ik4NUzTZMEpZMWFumVim1VYEGMJtvbfvqVTX3E1z8tS-znzthoXoslrfwTlCv1nW92DKA9T683ecGFeA0eetYI4iYPIAvRiWR7-505xG3pQ6GYwKFYO8vDEpuCk_N9Lpctnnv3bfKpey08DYAV1q7ZOga35TWZSnBFwkQhGRSkonin3Fa7kez-05wErS7h6v9pGthOejfR3R7TgjTLairiLr1vJ8fqIP3tDT1LXeELr_MIHGeS_zGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94edb900f7.mp4?token=MCusr5771wzyxVik0tyUz1pxlqo3vOxbuPFP3j29JYhe11loT4P4UAPivThgF3zvj2pL6Uc_wjG9pAcM-smGYl0XY326VCs6Ik4NUzTZMEpZMWFumVim1VYEGMJtvbfvqVTX3E1z8tS-znzthoXoslrfwTlCv1nW92DKA9T683ecGFeA0eetYI4iYPIAvRiWR7-505xG3pQ6GYwKFYO8vDEpuCk_N9Lpctnnv3bfKpey08DYAV1q7ZOga35TWZSnBFwkQhGRSkonin3Fa7kez-05wErS7h6v9pGthOejfR3R7TgjTLairiLr1vJ8fqIP3tDT1LXeELr_MIHGeS_zGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کلیپ از یه دختره که سر سفره عقد، آقای داماد رو سورپرایز کرد و گفت من مهریه نمی‌خوام و فقط 14 شاخه گل بنویسید
؛
هیچی دیگه پسره دیروز طلاقش داد و اونم با 14 شاخه گل رز طبیعی قرمز  یک جلد قرآن برگشت خونه باباش...
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71051" target="_blank">📅 16:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71049">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/01429c982d.mp4?token=OP9IC53eZjPRwrlmFFC_7ZJuVlcz2QqUp3blcns8HuWjmLLikW6BY4AedrHkkG1gV5qoC-5AvvTdr9PdEP-Z69LuVSSfyV02oOO_a6Q8J-ZX3LxhoVPgDxjNJJNdC88fwYZjEWJLIq54jPcGXzk30-LSrtquzMsVA65zB7R0HkKiGhRC1QbI4zrV9lc-jomY6jcNG7wAcT0FivI5KfTs10HP70_JL3Z264PpnxUYvtnILjQOjF6i-CXTcaWYEqBQylid8Vfisikcv15VAsezneO-ItqRo8jeZAlf3uOV3dZdTQH-dgV9QtoEHWAU2xb4ZtE1U32U7r6GDZRpt3L9hA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/01429c982d.mp4?token=OP9IC53eZjPRwrlmFFC_7ZJuVlcz2QqUp3blcns8HuWjmLLikW6BY4AedrHkkG1gV5qoC-5AvvTdr9PdEP-Z69LuVSSfyV02oOO_a6Q8J-ZX3LxhoVPgDxjNJJNdC88fwYZjEWJLIq54jPcGXzk30-LSrtquzMsVA65zB7R0HkKiGhRC1QbI4zrV9lc-jomY6jcNG7wAcT0FivI5KfTs10HP70_JL3Z264PpnxUYvtnILjQOjF6i-CXTcaWYEqBQylid8Vfisikcv15VAsezneO-ItqRo8jeZAlf3uOV3dZdTQH-dgV9QtoEHWAU2xb4ZtE1U32U7r6GDZRpt3L9hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز، اولین ایونت مد و فشن توی تبریز برگزار شد و حسابی غوغا کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71049" target="_blank">📅 15:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71048">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7913d873f1.mp4?token=r8yWJweK3kBbsFtfuad_Ag2YOMORA2UG5TGZHmOSxtn1Sixccg9cud3HaeQrOM8vlak0wXgsJJlK2S9CMvRhkPzGEMhoGJH0RJVAIt15iOsqgWq_iMPjB1zFEr-dky3ykOgyzJlSqkfR-qajlZahl1HTMk30efmQmpTcl9Nhehj1NWpsODPlugoYGkbSKxbCQaPBovbrAqd77ekIOz4CCAo3taQkAOlCKM9lz-NKasr0zz_LjVIHatamZ0p3p1pBLIBOKCL-ApKoDzjCyzgUgM8DFewYMt-zPBZQ7nmtbEAygpqk1f8D_fDQrSKg4xCizZ7x87UYgKE-ad3MVBae4g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7913d873f1.mp4?token=r8yWJweK3kBbsFtfuad_Ag2YOMORA2UG5TGZHmOSxtn1Sixccg9cud3HaeQrOM8vlak0wXgsJJlK2S9CMvRhkPzGEMhoGJH0RJVAIt15iOsqgWq_iMPjB1zFEr-dky3ykOgyzJlSqkfR-qajlZahl1HTMk30efmQmpTcl9Nhehj1NWpsODPlugoYGkbSKxbCQaPBovbrAqd77ekIOz4CCAo3taQkAOlCKM9lz-NKasr0zz_LjVIHatamZ0p3p1pBLIBOKCL-ApKoDzjCyzgUgM8DFewYMt-zPBZQ7nmtbEAygpqk1f8D_fDQrSKg4xCizZ7x87UYgKE-ad3MVBae4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کلیپ در مورد پسرای زیر ۳۵ سال که موهاشون سفید شده، در حال وایرال شدنه
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71048" target="_blank">📅 15:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71047">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0BxDC9qUH_zQYswua0vK6I33Az6BjoyRpv2XanIYpcXw1Pz-HfuVElL1fb4W1d7VK6q6F66_8Qzh-KTgvd9iU7s-WP-1wv-or9P5RmJ0vEUnWE46XMmwudQpQkbRQMGYX6v5ZvQQW2Jt3Tn43ad6u9C9YYnP-VbKFzOijhJ-Bp_lAXhwG-O2lgzCj2TbRV4Ls14avMTob2a373bcduNapJ_G7RqW2TYp9i4J_HiAs5J8COftsAGn3tQGTldlyL9tK3dM8V1xGRWsgiAaBKvMcNKD5ufYUcHBoMp7GrG8fC8qc-CbsRZMjPqvrWwLe5Dj3WsbsV3awzuI2C3aIYJ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
خبرگزاری میزان وابسته به قوه قضاییه، روز پنجشنبه ۱۲ شهریور ماه اعلام کرد حکم پرونده صادق ساعدی‌نیا، فرزند محمدعلی ساعدی‌نیا، در دیوان عالی کشور تایید شده و او به ۱۲ سال و ۶ ماه و یک روز حبس تعزیری، مصادره کلیه اموال منقول و غیرمنقول و محرومیت از اشتغال به شغل کافه‌داری محکوم شده است.
مرکز رسانه قوه قضاییه این پرونده را مرتبط با اعتراضات سراسری ۱۸ و ۱۹ دی سال گذشته دانسته و مدعی شده است که متهم در «تحریک اعتراضات و ورود خسارت به اماکن و اموال عمومی در استان قم» نقش داشته است.
صادق ساعدی‌نیا، فرزند محمدعلی ساعدی‌نیا، کارآفرین و نیکوکار ایرانی است. محمدعلی و صادق ساعدی‌نیا در جریان انقلاب ملی ایرانیان در دی ماه گذشته دستگیر و اموال هزاران میلیاردی آنان مصادره شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71047" target="_blank">📅 14:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71046">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:  اگر ایران به دولت اسرائیل حمله کند، این اقدام اسرائیل را از هرگونه محدودیتِ موجود برای حمله به ایران رها خواهد ساخت. ما به تمامی زیرساخت‌های ملی، نظامی و غیرنظامی ایران - از جمله زیرساخت‌های انرژی - حمله خواهیم کرد و ایران…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71046" target="_blank">📅 13:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71045">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7750e2ea67.mp4?token=l4UOb9kA_sXw30ZDMmtCGgaYquxvBiRPScO8tb-_EVQylRByMJtTmaAzNNEwUbtTupNb7cKSMfGiKAGVqElxvFkO32mx6GHGCFD99NLIAsM1AewZ_PCWDHAxEL8Nw2G4cQCq39IhwJETBWQzFG1NBpdW6IRl_3aJxb7daRZJo_o7fxoPveZQWRnyzl7s4lE7KsfLYwOlmFr_YPPx-DIGfpM0jjwmhSIVd066W0K854XHoA7bc9ECMojha3-J6NW79wM8g6XEbzO-0IDlt3KacJsbD_-vV_Wz7L580l5Tq1QyvKFHLxUf6k0L8rY-DnjUr7mAOG9pvRbJfme6oz2Z1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7750e2ea67.mp4?token=l4UOb9kA_sXw30ZDMmtCGgaYquxvBiRPScO8tb-_EVQylRByMJtTmaAzNNEwUbtTupNb7cKSMfGiKAGVqElxvFkO32mx6GHGCFD99NLIAsM1AewZ_PCWDHAxEL8Nw2G4cQCq39IhwJETBWQzFG1NBpdW6IRl_3aJxb7daRZJo_o7fxoPveZQWRnyzl7s4lE7KsfLYwOlmFr_YPPx-DIGfpM0jjwmhSIVd066W0K854XHoA7bc9ECMojha3-J6NW79wM8g6XEbzO-0IDlt3KacJsbD_-vV_Wz7L580l5Tq1QyvKFHLxUf6k0L8rY-DnjUr7mAOG9pvRbJfme6oz2Z1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
اگر ایران به دولت اسرائیل حمله کند، این اقدام اسرائیل را از هرگونه محدودیتِ موجود برای حمله به ایران رها خواهد ساخت.
ما به تمامی زیرساخت‌های ملی، نظامی و غیرنظامی ایران - از جمله زیرساخت‌های انرژی - حمله خواهیم کرد و ایران را به اعماق دوران حجر و تاریکی بازخواهیم گرداند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71045" target="_blank">📅 13:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71044">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b05262cb.mp4?token=gszz-6sNFe9p2txxiFOilbwzda8J_WD6z8Hq8DXdPrvyRAoFMfqYIRKu5ukj9zLFzC3xIPG03oVg1wdXtASf5rrN7bHqu7nUduv0wI25vdOnDf9xw5YNgAeHZADLeB2HMw_btQHaIHCOCLPV5SUfJT2oCBHpyLZSFxZwEQN7Wz7MAIH0ieZisd-it5cb5B4y0FlQN_xranX7NmHm-ls2w20U51mcl5MqhATcDBChwhJp7Ny98KVB9rEfvP2YNeHyhq3kbpCgzfrGlnG6fCwrWYmWVpNd6pU5wJQOKXczDuB42LUyrHcdu2O1SuhzJcgitWMr8VkHmJ9RCPC26OQYRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b05262cb.mp4?token=gszz-6sNFe9p2txxiFOilbwzda8J_WD6z8Hq8DXdPrvyRAoFMfqYIRKu5ukj9zLFzC3xIPG03oVg1wdXtASf5rrN7bHqu7nUduv0wI25vdOnDf9xw5YNgAeHZADLeB2HMw_btQHaIHCOCLPV5SUfJT2oCBHpyLZSFxZwEQN7Wz7MAIH0ieZisd-it5cb5B4y0FlQN_xranX7NmHm-ls2w20U51mcl5MqhATcDBChwhJp7Ny98KVB9rEfvP2YNeHyhq3kbpCgzfrGlnG6fCwrWYmWVpNd6pU5wJQOKXczDuB42LUyrHcdu2O1SuhzJcgitWMr8VkHmJ9RCPC26OQYRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
جنگنده میگ-۲۹ام‌یو۱ اوکراینی یک موشک اس۸۰۰۰ «باندرول» روسی را در ارتفاع پایین با یک موشک آر-۶۰ منهدم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71044" target="_blank">📅 13:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71043">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162568634d.mp4?token=ubwuT4UPNmDaeMx1LtX-8RxLiZ6dHwF0PK_VBnsZ9Jo3xTrjqk6-DDkjjoWQnXJ3Q3xPrmDJD03F_ZNwpnqlwR8q2uqszzxnvJcyMJn181CrL_MnFR4RdgfaIEiP4SRMB-SF5xTF58hdcWxzJFtBPX16DdqFjM5LsD3CoW8OrJXSFYFItuqF9fR18btwRvKsr1WpTSxS9YHFF0UWB34wTixScX4jd8OdsrI5tpQnss9qs90OOnWQS5nfk_fN_xdNufF2TpHTUsfp58x3-y3EWGthW12GJqP-wMiv_tuO7h0ACnsvd8vcI-Ekn3gPrBezDuvpenkMU2lOAgj8t-j5Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162568634d.mp4?token=ubwuT4UPNmDaeMx1LtX-8RxLiZ6dHwF0PK_VBnsZ9Jo3xTrjqk6-DDkjjoWQnXJ3Q3xPrmDJD03F_ZNwpnqlwR8q2uqszzxnvJcyMJn181CrL_MnFR4RdgfaIEiP4SRMB-SF5xTF58hdcWxzJFtBPX16DdqFjM5LsD3CoW8OrJXSFYFItuqF9fR18btwRvKsr1WpTSxS9YHFF0UWB34wTixScX4jd8OdsrI5tpQnss9qs90OOnWQS5nfk_fN_xdNufF2TpHTUsfp58x3-y3EWGthW12GJqP-wMiv_tuO7h0ACnsvd8vcI-Ekn3gPrBezDuvpenkMU2lOAgj8t-j5Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
روابط عمومی ارتش:
در ادامه سلسله عملیات‌های صاعقه و در مرحله سی و یکم،  در انتقام خون پاک مردم بی‌گناه و دلاورمردان نیروهای مسلح، بامداد امروز، ارتش جمهوری اسلامی ایران، «سامانه‌های ارتباطات ماهواره‌ای»، «انبارهای تجهیزات» و «آشیانه هواپیماهای جنگنده» ارتش تروریستی آمریکا در پایگاه احمد الجابر کویت را با موشک‌ها‌ و پهپادهای انهدامی، مورد اصابت قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71043" target="_blank">📅 13:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71042">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71042" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71042" target="_blank">📅 13:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71041">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ks0I6GdDd5ZqeyrFBciIKksoKATtAzyZPp1idg1Ulg2PdZTwaiXUcVmBsWOknOvi0E1C5vGB8JOhDS56ZmUoYwfr25mU9lP-yRfj03OrAsV9gGGr36AtI8C4oSkJiqyMXkEZyyO2_XzEC_rwDxXWWfvR4R6FWMVVlgy8s1F8Uoyg8MrfZbLZvkCR86LAh5uZR_m3E3bCDk0mY8VyZ-bKyhjraOpKIeHlYIv25M4E0duWZETGrBBMy4I-Tw3PvrV6z2CzWf7YRQCLpsbQOKaWNelWbV_Kd8CMmEBuVkDMJiJ8LxMrQffs71noaXnzwVO0A7PTBoRlG6Z8f2d_PZ3ATA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71041" target="_blank">📅 13:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71040">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2218c2694e.mp4?token=uZ5RrKpcyUgV6tw97CZfPPWEqYLNYM6cr74jaLuxdK8BfL6eE9hAFensoGuQfc3mJha5j9nvxevaXZ8JZZvAlNrRGNMOJbGeTiNwTqhrdpQe2kmF07EXY3Dd92tFw1JrqR1JnM8KMRV1LJp2wydbLnM4EhfS855xjTZRrGk4VsgE0HBblxVnwPC_71TwW_Y_2THrJMLrZ2UlPFHrYqQZNsrQhMLDqIJB1qWyvjUL2tkQdKY5wzm0idv5QhjAno-_L5pmaDVpN6qgFc0pgvX184G-TYrLVPuAhtOyOABv2jgB5WoxR1w2yBFDDMOGv5PW6960alefmhqwaUy9NlLZug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2218c2694e.mp4?token=uZ5RrKpcyUgV6tw97CZfPPWEqYLNYM6cr74jaLuxdK8BfL6eE9hAFensoGuQfc3mJha5j9nvxevaXZ8JZZvAlNrRGNMOJbGeTiNwTqhrdpQe2kmF07EXY3Dd92tFw1JrqR1JnM8KMRV1LJp2wydbLnM4EhfS855xjTZRrGk4VsgE0HBblxVnwPC_71TwW_Y_2THrJMLrZ2UlPFHrYqQZNsrQhMLDqIJB1qWyvjUL2tkQdKY5wzm0idv5QhjAno-_L5pmaDVpN6qgFc0pgvX184G-TYrLVPuAhtOyOABv2jgB5WoxR1w2yBFDDMOGv5PW6960alefmhqwaUy9NlLZug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تو میدون تایمز نیویورکِ آمریکا، یه خانمِ چاقو بدست بعد از اینکه یه مرد و یه زن رو از ناحیه شکم زخمی کرد، بعد از اخطارِ پلیس‌ها به سمتشون حمله‌ور شد و به این شکل بهش شلیک کردن و کشتنش.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71040" target="_blank">📅 12:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71039">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f52d28bc.mp4?token=bUT1rr69-Z7KemBfDdNiBSgTDdHiVYUwwlXPRKKWGi66yXmXpJgtbbyv3YozvRExJnVkHpkzjNm3X0Jpi1W3Q-5DDe83H4CcmsVHLDWNqRjrzj2JGXM6q0fsJiC_vvlSSwRqpLqefUGKysFIYCRECStWVoWK4htyMd_7eGPe7dhNXJAh9teFg5b2p7NDScEyDAUIUwJvCb0dtE_xlW4_x1hx4GPKzWdZ_tm2Ws-qSV7WYiSJKWPpERvZohVdWqv5nNBj6RMG_5j9rtfRsjVSalcRcfhGsw5pgf-hBB5x5awQKWDTIxW-XrcqfZBDuYU3_REoBtG8833eSyaOnpOuog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f52d28bc.mp4?token=bUT1rr69-Z7KemBfDdNiBSgTDdHiVYUwwlXPRKKWGi66yXmXpJgtbbyv3YozvRExJnVkHpkzjNm3X0Jpi1W3Q-5DDe83H4CcmsVHLDWNqRjrzj2JGXM6q0fsJiC_vvlSSwRqpLqefUGKysFIYCRECStWVoWK4htyMd_7eGPe7dhNXJAh9teFg5b2p7NDScEyDAUIUwJvCb0dtE_xlW4_x1hx4GPKzWdZ_tm2Ws-qSV7WYiSJKWPpERvZohVdWqv5nNBj6RMG_5j9rtfRsjVSalcRcfhGsw5pgf-hBB5x5awQKWDTIxW-XrcqfZBDuYU3_REoBtG8833eSyaOnpOuog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سایپا تو ماشینی جدیدی که زده ماشین با اینکه راه نمیره ولی براش کیلومتر حساب میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71039" target="_blank">📅 12:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71038">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tm-IwuhCI74P6xvQIPZS8_oo22GwQ0YQHY7bb4AL5ZSh8tHDZDhZ7QzXT9VzrEBvFtQ5ljnMAwKjg3IA9RxavV5UCp_RgM2YEuEPetDMDTa2wXu9kabTYKRjIbDoXQULGp9v8hfCg6pLW6aJ-FUtbXFej6B-4bssGA_D74YTL27K7H8WOiM15tQaIkuUPpKjVdocC3iwwJeyjNKxZy0vDwWHrJ4nx_-8ieoiwSf4tmS8g-rHPos8wqgnlk69oNUueDVIl86J1oRwKhLPJ9QJv8lPY4pMS2v7fyxQUr6Vj2IwCqlJLG7_WMd3uFcBhArWty4scD7sYuaWqKe5yxAy8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
اکسیوس:استیو ویتکاف، فرستاده کاخ سفید، آخر هفته گذشته در ساردینیا با شیخ طحنون بن زاید آل نهیان، مشاور امنیت ملی امارات متحده عربی، درباره ایران دیدار و گفتگو کرد.
این دو مقام درباره گام‌های احتمالی آتی بحث و تبادل نظر کردند؛ چرا که دولت ترامپ در پی بازگشایی تنگه هرمز و هم‌زمان افزایش فشار اقتصادی بر تهران است.
امارات نقش کلیدی در تلاش‌های تحت رهبری آمریکا برای عبور نفت‌کش‌ها از این تنگه ایفا کرده و در راهبرد تحریمی واشنگتن، کشوری مهم محسوب می‌شود.
مقامات اماراتی به دولت آمریکا اعلام کرده‌اند که هرگونه کارزار مؤثر فشار اقتصادی باید شامل تمامی کشورهای عمده‌ای باشد که همچنان به تجارت با ایران ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71038" target="_blank">📅 11:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71037">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به بندر سوچی در روسیه حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71037" target="_blank">📅 10:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71036">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef77017317.mp4?token=SG3SLWCqUVA8M1wBwvcHY80qL8Xtw2_rt3Z6QM63XBDGKFGBJJGSNv6zU68W22Bw_QLCRNl8YshWrUUGknzx3T_M0chHEfZmBxNtV-URzNBhbyB_KBtW3sPiwNGyEn5zUd5UmyY_dmUrNYBM4XzLUvKkhMpWxCef0jWwL7iHUSjmWFj9I9qeKqpPf6-1tposiqMK4wqA4VZbwPK_hp0vkXhvXotM5W7hGfjWGDGaNWsDCcrSbw9vQ39RFq5UqWo6zBEqtNnZvZjEy9bc_V_AKgpYdf4O4PsrfhX2h06Ca0zD4s16Vrz28cKHNY4vCCK_Z82Uvljwrivj1cs0EVq06A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef77017317.mp4?token=SG3SLWCqUVA8M1wBwvcHY80qL8Xtw2_rt3Z6QM63XBDGKFGBJJGSNv6zU68W22Bw_QLCRNl8YshWrUUGknzx3T_M0chHEfZmBxNtV-URzNBhbyB_KBtW3sPiwNGyEn5zUd5UmyY_dmUrNYBM4XzLUvKkhMpWxCef0jWwL7iHUSjmWFj9I9qeKqpPf6-1tposiqMK4wqA4VZbwPK_hp0vkXhvXotM5W7hGfjWGDGaNWsDCcrSbw9vQ39RFq5UqWo6zBEqtNnZvZjEy9bc_V_AKgpYdf4O4PsrfhX2h06Ca0zD4s16Vrz28cKHNY4vCCK_Z82Uvljwrivj1cs0EVq06A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی وایرال شده از پسری که چالش گرفت که تو خیابونای شهر از مردم درخواست پول کنه(نفری ۱۰۰تومن) و اکثرا قبول کردن و در آخر هم پولی که جمع شد رو رفت به نیازمندا کمک کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71036" target="_blank">📅 10:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71035">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7de7f7edfa.mp4?token=Bqpm4BuPLe-Fx7VKl1lV6JipXo7kmKkSgRL0rm-0SBX9yyYkkT5W_1p3NoxADILfDcmOZz0p6Lu7KZHyfmddk_4uWsZ3ynsE9zjqq_GOvT93G4T0WBIxNcCgIHek7YqNxCPoj9dcLSq9rOP3fmgCUM_EmffzoCWHQdEbN6hgFDsi2OQmTGzJk6PqmdE4nW6bDr3LVTEbSG260dK7cQKfc3ABCq75Bjf76ERMYatjPlAq0rrRJ9YrSxOs-O4tOTpiGruy8iRgBDmyy8EpU8xCfaRtGWglaf1Ou3sNKnTZNM4zT3zChymLVg8a4yKGS3YH67Y6Hq7Pog0G-Xta6qwDUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7de7f7edfa.mp4?token=Bqpm4BuPLe-Fx7VKl1lV6JipXo7kmKkSgRL0rm-0SBX9yyYkkT5W_1p3NoxADILfDcmOZz0p6Lu7KZHyfmddk_4uWsZ3ynsE9zjqq_GOvT93G4T0WBIxNcCgIHek7YqNxCPoj9dcLSq9rOP3fmgCUM_EmffzoCWHQdEbN6hgFDsi2OQmTGzJk6PqmdE4nW6bDr3LVTEbSG260dK7cQKfc3ABCq75Bjf76ERMYatjPlAq0rrRJ9YrSxOs-O4tOTpiGruy8iRgBDmyy8EpU8xCfaRtGWglaf1Ou3sNKnTZNM4zT3zChymLVg8a4yKGS3YH67Y6Hq7Pog0G-Xta6qwDUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ویدئو جدید از پرواز هواپیمای HC-130 Combat King II آمریکا در ارتفاع پایین در عمق کشور به دنبال خلبان آمریکایی جنگنده F-15E
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71035" target="_blank">📅 10:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71034">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad58d044a.mp4?token=bn0D3tCp3SXOiVolTUpcmqUVdStnYi-PUEk8AswcbDLvC3lN_emGg2fY35BfUvxi0eEqFBT4CcGXST6tFkPTyLEIAyRkp12S45u0pQbGzcbquAw2yAE9E1tG4sgpM63lYfQOdD6SZVpYxcy8Y1qXDONJEZagF75kZfAHW8QBF0f3TwMugfZcoIgLsiL5ocJP7KbhoccoxjKQqAQE1DcdyuZhCrcVMJJqZ-XhQuPAS8xXA0vYx8KnqNOLohwhRyfYFZ9EdDSF09i_U1INKau1vli1hnlieRDuN1Dk1qbHmqoCuYSdnXwPpTF9qWB5NdjFYBhh4yScDbbQj5m2FKO_Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad58d044a.mp4?token=bn0D3tCp3SXOiVolTUpcmqUVdStnYi-PUEk8AswcbDLvC3lN_emGg2fY35BfUvxi0eEqFBT4CcGXST6tFkPTyLEIAyRkp12S45u0pQbGzcbquAw2yAE9E1tG4sgpM63lYfQOdD6SZVpYxcy8Y1qXDONJEZagF75kZfAHW8QBF0f3TwMugfZcoIgLsiL5ocJP7KbhoccoxjKQqAQE1DcdyuZhCrcVMJJqZ-XhQuPAS8xXA0vYx8KnqNOLohwhRyfYFZ9EdDSF09i_U1INKau1vli1hnlieRDuN1Dk1qbHmqoCuYSdnXwPpTF9qWB5NdjFYBhh4yScDbbQj5m2FKO_Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
تو یه فروشگاه تکنولوژی تو روسیه، یه ربات بعد از اینکه مشتری هلش داد، شروع به دعوا با مشتری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71034" target="_blank">📅 09:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71033">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e73b2179fb.mp4?token=frwC6afaqO_vqBgnFYJeF5FlHf0eg96dqa-fUvmXRAjY2yk-zzIa6eX3iScPsbNRe3t9wg8eeRQihiHthbIyQxMyIO4SMBE7LNJbocbdicxnhx6pZcEB4k76o7apKkOV5qHJlnsKRDwa2mEUQou9dnMcRaTzGk5XWy9f_meoTUQyQFpMkeIq_55inGSgSF9fViEpYmcDjP_39VMDQnKONFUTKZ3NboBy34swcumqXT80S9KWulr2MRRcZYoF4aqncXGTTGNBS1c9e82rWm6f-dp62JYRNaSarcIfoD0DIUwOcIdY6bFnd__xBtdJvA-WKhbu9HyL0Ja4snfEzXk0Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e73b2179fb.mp4?token=frwC6afaqO_vqBgnFYJeF5FlHf0eg96dqa-fUvmXRAjY2yk-zzIa6eX3iScPsbNRe3t9wg8eeRQihiHthbIyQxMyIO4SMBE7LNJbocbdicxnhx6pZcEB4k76o7apKkOV5qHJlnsKRDwa2mEUQou9dnMcRaTzGk5XWy9f_meoTUQyQFpMkeIq_55inGSgSF9fViEpYmcDjP_39VMDQnKONFUTKZ3NboBy34swcumqXT80S9KWulr2MRRcZYoF4aqncXGTTGNBS1c9e82rWm6f-dp62JYRNaSarcIfoD0DIUwOcIdY6bFnd__xBtdJvA-WKhbu9HyL0Ja4snfEzXk0Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیح عباس حیدرزاده مداح درباره‌ی وضعیت مجتبی خامنه‌ای :
تولیت آستان قدس رضوی گفت که شب دفن رهبر؛ مجتبی خامنه ای ساعت ۱۲ شب اومد حرم برای دفن پدرش و تا ۷ صبح اونجا بوده.
وضعیت جسمانی ایشون هم عالیه، هم از لحاظ ظاهری و هم از لحاظ جسمی؛ حتی مسئولین هم پشت سر ایشون نماز خوندن.
همچنین ایشون نیم ساعت کنار قبر پدرش دو زانو نشسته بودن و گریه میکردن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71033" target="_blank">📅 09:03 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
