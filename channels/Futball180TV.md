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
<img src="https://cdn5.telesco.pe/file/kVPcs8LmLfkXZhz0w2Rhq5r88gGNGhPVrfCaghVghIPdy4_ff_xCDpmWDmMC0ok7cHb5E6nA9kIE3kjSmwko865LzX-QcVtKzZ37yNp12sF_pU_noeJBh-rKqVf-kNyh3dPA5T5gL2A5vG372j9iQ8T35m2u2hGWybXHDimd-Bh1SHequrgRqmrcwVXhIG1yEy4I7rRpfXUHBq3JB-pW8da0ktfsABrlmn8y1R1LLfzkM2qdOr9OT7CLRg5bs8R409YmMao7Ur0ppIF09PYpcah353HadHwE5B4OttV2PJhw0svhDGn3jgdKammbAajyW1rX8aguS-yi4myA38prnw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 431K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 15:40:45</div>
<hr>

<div class="tg-post" id="msg-105342">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91b6a8d69.mp4?token=E7jW2gnEgMq2eJTjS9JMHhCW5fwp3gd4NeBMju1BW_5VATx2oE9QKtzuUuQUOfYQQ4rWNYO_bIHSBObVA7UF4uSz5BKNeAbiCepzt1_Ova33cQm-79Ua6_LKjeF8oBPpZWxRUz6BwMRPTKBywA2ConPBr2h-28pZzPnKbzXdX-CwmHMe6ZwM-TNqtb99dWwDyygnHoagPOn2rWeNRj2uVzh1boz0tFugr7SdjgefTVYgZpymbqV5mGIX9E7NwucL8bYK-qriyA8G88U-ebo7o7GI2G6OQhHrJGHYkFYHQxLmpESfJeYrZCtS5ubQGm1tbEQ68by6UHOoM-sg9ruJBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91b6a8d69.mp4?token=E7jW2gnEgMq2eJTjS9JMHhCW5fwp3gd4NeBMju1BW_5VATx2oE9QKtzuUuQUOfYQQ4rWNYO_bIHSBObVA7UF4uSz5BKNeAbiCepzt1_Ova33cQm-79Ua6_LKjeF8oBPpZWxRUz6BwMRPTKBywA2ConPBr2h-28pZzPnKbzXdX-CwmHMe6ZwM-TNqtb99dWwDyygnHoagPOn2rWeNRj2uVzh1boz0tFugr7SdjgefTVYgZpymbqV5mGIX9E7NwucL8bYK-qriyA8G88U-ebo7o7GI2G6OQhHrJGHYkFYHQxLmpESfJeYrZCtS5ubQGm1tbEQ68by6UHOoM-sg9ruJBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظ لئو. خداحافظ تا تولد یک اعجوبه دیگر در آرژانتین.
🩵
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 605 · <a href="https://t.me/Futball180TV/105342" target="_blank">📅 15:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105341">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9af28d1f54.mp4?token=o5YiHAqfvXjtNhCfPWyTzijVwJYGckT6facBIf77RpPoGTvAw2oFyfg1W-6iJJ4koZavmpqgqS1cp3bYvj6m_UpFuVxg5xMM7ZKJVAJ2cCOiR1prj-_f9ur4SI6agJUW6mzFgcmpsZSk7jx8iUvgq-CHYCr54qKy5b64iZLD3pX408piNPebNjo3xssB0kJCGMxQc_FSlg1RH3OCv2e_QG2oaZX7l9PkF8qelru2KFH8mz6gmAolgXohG8vOYCHy43SzTbRx7XKmR8Zch8Pijn3FxO67f3ijcUvhewrUHL9Juuom1DXGVlQ3Qe7VJuQ2F29HDSAUfzSQ2SwZ_FcdoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9af28d1f54.mp4?token=o5YiHAqfvXjtNhCfPWyTzijVwJYGckT6facBIf77RpPoGTvAw2oFyfg1W-6iJJ4koZavmpqgqS1cp3bYvj6m_UpFuVxg5xMM7ZKJVAJ2cCOiR1prj-_f9ur4SI6agJUW6mzFgcmpsZSk7jx8iUvgq-CHYCr54qKy5b64iZLD3pX408piNPebNjo3xssB0kJCGMxQc_FSlg1RH3OCv2e_QG2oaZX7l9PkF8qelru2KFH8mz6gmAolgXohG8vOYCHy43SzTbRx7XKmR8Zch8Pijn3FxO67f3ijcUvhewrUHL9Juuom1DXGVlQ3Qe7VJuQ2F29HDSAUfzSQ2SwZ_FcdoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇮🇷
🇮🇷
دربی فقط یک بازی نیست…
⚔️
یه حسه، یه خاطره‌ست، یه جنگ برای افتخاره.
🔥
۹۰ دقیقه‌ای که هیچ‌کس نمی‌تونه نسبت بهش بی‌تفاوت باشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/Futball180TV/105341" target="_blank">📅 15:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105340">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3a4e2ac35.mp4?token=U9RpxwCgR0pAdyx008LJyhEiqxvowpx06FbqmyZVlnbB5VJZbBvZ-syazBY8oTNSEVf5wHj8-sC2Zb1c9_1uG7oIY3afv-4Y7K2TVHZniACJflfdf2TFkcqJzV7P0iJ8qOjZZXx0GuGnNuBHQjsx9cXjGHkwTJy67rCWXd8diOKaPQIjYvgexnwHBjZCQvXwXs4PIZH20PZy4RCZTCJ36LaNH_ccJ_xFyFcOolqexi5ckIGvD5hNhz5FnKWFd4MOu9UL2xCz0Jx-Zpo8_VPzIs_9e5CBT71cICI044_fkQHVtcqgzjnXddFkDrXOT1SbIaAJnk2wiH5VsbYtDA9OqW2kDTeY0Q3jHnNoXwcmm-36HluCbvidUzs91wdVxvNbmuyxtB2ffpRPuZUg1lQs4_ru4W8A6eRPyU5gzD8d17ZYwczOBfZP4REQqJriO0Tg6IM7L2fU-ihy2fUpGzwUdmsqiF3854gtPGDmqftumwz533LSP-r3nYKNO5FvYJ89IirhU0HLVUqqpQSBk8fQ6x5irL616MFyTIGI4RgETHqdnyYkNr87Dkh-kqYxSmVq1MAoAHpK44qZXrz1VH7xHqlSRehQ-GPuTgCRAbSoe0-uA0eKU1_gh3Zj8Tl9YcATQdFYnH2m97y0rEB5A73dQgA4Gk7K5Am2MqooyD_eKak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3a4e2ac35.mp4?token=U9RpxwCgR0pAdyx008LJyhEiqxvowpx06FbqmyZVlnbB5VJZbBvZ-syazBY8oTNSEVf5wHj8-sC2Zb1c9_1uG7oIY3afv-4Y7K2TVHZniACJflfdf2TFkcqJzV7P0iJ8qOjZZXx0GuGnNuBHQjsx9cXjGHkwTJy67rCWXd8diOKaPQIjYvgexnwHBjZCQvXwXs4PIZH20PZy4RCZTCJ36LaNH_ccJ_xFyFcOolqexi5ckIGvD5hNhz5FnKWFd4MOu9UL2xCz0Jx-Zpo8_VPzIs_9e5CBT71cICI044_fkQHVtcqgzjnXddFkDrXOT1SbIaAJnk2wiH5VsbYtDA9OqW2kDTeY0Q3jHnNoXwcmm-36HluCbvidUzs91wdVxvNbmuyxtB2ffpRPuZUg1lQs4_ru4W8A6eRPyU5gzD8d17ZYwczOBfZP4REQqJriO0Tg6IM7L2fU-ihy2fUpGzwUdmsqiF3854gtPGDmqftumwz533LSP-r3nYKNO5FvYJ89IirhU0HLVUqqpQSBk8fQ6x5irL616MFyTIGI4RgETHqdnyYkNr87Dkh-kqYxSmVq1MAoAHpK44qZXrz1VH7xHqlSRehQ-GPuTgCRAbSoe0-uA0eKU1_gh3Zj8Tl9YcATQdFYnH2m97y0rEB5A73dQgA4Gk7K5Am2MqooyD_eKak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
▶️
🇮🇷
🇮🇷
سریع‌‌ترین گل‌های تاریخ دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/Futball180TV/105340" target="_blank">📅 14:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105339">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_rCrZjuT_EpmI16Ea24LYj0bsmuwJEardjXHtILbKJI8bJdx1nTwazzP9NhvExhL1FONlxpkQ5xdGGcZ1pT_O-tYnXrJuw5_swwhUW7fi8i2NeL8xDEHhcU2eJdUdmNktXeIaf70X0a4K4MS0ZPcOwzYoL0mUWc7s8b23sFZj_lSQsjwY-e-RS6JYV3TIQlpIxd7sl2SN_qAN9y2ORrXUQ5L-GtL8WJamVSJH7w-FwCm50D_kcWa-OSy-dNQ4_pOaI1wT9ikkT_hfwLmx1eZ36m9KaeszxfXNgnwkZzt7rrJBuGvFbdaymWFfZ_MUz3MgnAUoaQ1j0yVH30FKdWzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
💵
قیمت دلار تو دربی قبلی ۱۲۰ بود و الان در کمتر از یک سال رسید ۲۲۰؛ قدرت گنده‌گوز منطقه
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/Futball180TV/105339" target="_blank">📅 14:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105338">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d7c8fe82.mp4?token=T0NB2t9KM8lBqFIvuilTH-0iUbgnYQS65ro0q7c0hHH-giptMqcrFZAxanDGlju-47Dj_q8rOrOi7VO8bukxPCJrmullnKpv82DuoKLCdkE557WwHnVozE_A6-G3F43pJer3mGtAUnALTd9cmnn_-4Itaj3hIiDZatsevg3se19tmYQ5684RwHEl3pvanxKuOpRmzbCnDxor_UwM6oCAMncKR1xzQcUU0b0MHyhQI_y2uVi-PkrhViY2LSzIJfq25V7kGtbwCXLaKiCc5OTgdpdfFkj1Im7MNbapA5AfrT8AfG1VJGNOUGrskvYi5bw_hT4w5U2hSpJjcE1-jfvROjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d7c8fe82.mp4?token=T0NB2t9KM8lBqFIvuilTH-0iUbgnYQS65ro0q7c0hHH-giptMqcrFZAxanDGlju-47Dj_q8rOrOi7VO8bukxPCJrmullnKpv82DuoKLCdkE557WwHnVozE_A6-G3F43pJer3mGtAUnALTd9cmnn_-4Itaj3hIiDZatsevg3se19tmYQ5684RwHEl3pvanxKuOpRmzbCnDxor_UwM6oCAMncKR1xzQcUU0b0MHyhQI_y2uVi-PkrhViY2LSzIJfq25V7kGtbwCXLaKiCc5OTgdpdfFkj1Im7MNbapA5AfrT8AfG1VJGNOUGrskvYi5bw_hT4w5U2hSpJjcE1-jfvROjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
زنده از ورزشگاه نقش‌جهان در فاصله ۵ ساعت تا دربی حساس پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/Futball180TV/105338" target="_blank">📅 14:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105337">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇷
بهترین گلهای استقلال در دربی‌های لیگ برتری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/Futball180TV/105337" target="_blank">📅 14:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105336">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇷
بهترین گلهای پرسپولیس در دربی‌های لیگ برتری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/105336" target="_blank">📅 14:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105335">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfQWGdEnbMmO5oAQezBukKV80n9Ko00SkslClWQiEBRPJmrPRiJ9MNW_GeCdWhZafIhJ_wlBDx3KGJ2fB-XqD9OXN_KICM62QbbxwugBNdkfObMZJ1uSmk00BHSN9Iwa5VQQE9Y-TtunlVQ-bVUgH6TEBOmz0BLwcwMv36gIQYhXWHL6rjZxrBW34AOpBiuXZaK6Iu2IwMHnrmKrlycMVvrxrTN2D3eKs4P6eMy3O7k-QSyLUSIiOWUlwtXtSNG6st4nb4kcFJ62BYqRxHGILM7HIrEkeViMpRYMZXVlVLxEJrl843ypHwO8-wB6KKTNKFQ62p4q9yH0dviJp3Kwbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😳
💵
خارکسده
افسار پاره کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/105335" target="_blank">📅 13:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105334">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhO39cyp02I62mDm7Y1H4JXN8tOjBsTFJrNGgFENbBIKpxDRuaqrcyvfNV6pQHIIkSmc_sXdxpP6pGlaO45UdNkDjqiwC4LUN1yW5I3l6NH4njlNnGKEyNvoMTe12Pf5PLV4ygL4x3lntFAG1Miz7O_MiATCHSrVemEEKPrNwLPv0-YM-Blu_P8awMIpv3sS9sDmFgpNH6tYG5QugtN8miH6DK1omEO8nGBf_ZeV37wF8rTMRXCSQ8FLdh-18QKAwjom28WNFsVjrLU3TU64foAj6W7iE8ZtgXWaVHLc3N47UVKpKOj0v958twmWOHO99k3Eqp2rFulhd6YGlsN00w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
مسیر‌ فوتبالی عجیب‌وغریب آلوارو موراتا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/105334" target="_blank">📅 13:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105333">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40825ae46d.mp4?token=XhDMmXQitcjhsZenCdnfZi0kpNGYhLDmDiAJs1PhExCMSbzBDCH7UjeIGNd81_mR3GyRws-fF9G0ia69vIlpkQiBe_Qm0KuIR3X9pU7A0VnZ8ny0Zf9g2fbqkTJtiRM0O2_TUYgxuYSkk6eVIqR_jy6ykTYV1H8d5TX4z1RYBwhlrjScWq8aE_h7EkU-7aNeFrPcKKyvLhhneRLPo8AM7PWnNM3rdqZjZfX8HTBw2LNGUUl41OmJG9WLr8DWHpQ_40W9OOmhNdazbuZBvFs-FmT7fqVXXHLTRKtDz1hdJy6D8ca5sOWeyGva21G0rWdXTgBl6mK1czgjpXPlETrIag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40825ae46d.mp4?token=XhDMmXQitcjhsZenCdnfZi0kpNGYhLDmDiAJs1PhExCMSbzBDCH7UjeIGNd81_mR3GyRws-fF9G0ia69vIlpkQiBe_Qm0KuIR3X9pU7A0VnZ8ny0Zf9g2fbqkTJtiRM0O2_TUYgxuYSkk6eVIqR_jy6ykTYV1H8d5TX4z1RYBwhlrjScWq8aE_h7EkU-7aNeFrPcKKyvLhhneRLPo8AM7PWnNM3rdqZjZfX8HTBw2LNGUUl41OmJG9WLr8DWHpQ_40W9OOmhNdazbuZBvFs-FmT7fqVXXHLTRKtDz1hdJy6D8ca5sOWeyGva21G0rWdXTgBl6mK1czgjpXPlETrIag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
امیرحسین‌صادقی: اگر همین‌الان میخواستم در دربی و فوتبال بازی کنیم، دستمزدی که باید میگرفتم بیشتر از ۱۵۰ میلیارد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/105333" target="_blank">📅 13:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105332">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc8f3b366.mp4?token=lL8N-UjM1L1YJS0busozqQae52m7fhyJFP6PvLxQUG5CNdpe7wuQC6SE-QmqBjjb68HydLyxttmxt1a4HsPw7fZ1mD3ZFGio_HmWKydz7a9mbR7OngP2LK9r2Zh7asrRVfRRQE6BA3YW-6ppHy7CfYqPW6GiS2o_nzX6gzQPQdOHn0m4qfkHF_E1BaRshl0D0lQ2ivAWn75IBIM9vlWuZ030L7cKSRu8aNGiUEH7SIJEiqQMOS2Mrriz36-LL_V3ccWMMreO-VWOhzCcF9io08muoLd3Hc6axhk-JpPCutotj7syJak4KS45VRQtS6NQ1Zkn9FDesq8asAFpU8lCug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc8f3b366.mp4?token=lL8N-UjM1L1YJS0busozqQae52m7fhyJFP6PvLxQUG5CNdpe7wuQC6SE-QmqBjjb68HydLyxttmxt1a4HsPw7fZ1mD3ZFGio_HmWKydz7a9mbR7OngP2LK9r2Zh7asrRVfRRQE6BA3YW-6ppHy7CfYqPW6GiS2o_nzX6gzQPQdOHn0m4qfkHF_E1BaRshl0D0lQ2ivAWn75IBIM9vlWuZ030L7cKSRu8aNGiUEH7SIJEiqQMOS2Mrriz36-LL_V3ccWMMreO-VWOhzCcF9io08muoLd3Hc6axhk-JpPCutotj7syJak4KS45VRQtS6NQ1Zkn9FDesq8asAFpU8lCug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
حمله مهدی‌فنونی‌زاده در آستانه دربی به بازیکنان سرخابی: عارف آقاسی ١۴٠ میلیارد از استقلال گرفت؛ قیمت بازیکنان فعلی ١٠٠ میلیون است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105332" target="_blank">📅 12:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105331">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105331" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/105331" target="_blank">📅 12:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105330">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGbRGuPmqLiA_JdqsOVZTFxWSHdt-l20tN2L6LybN_o7zVBNDq_Sb6oWTi2X8dkLemgKl3hGjVVQw2UmiCoC0cdg1ZvYxCnhcKxdZlqwDToT1m12XnTFcscQ3UNaKWGzbLzOayfzv4wdFwNmX2LIUIlLme5YT7bMRUAccqrfkbiCbOpOsE1_RKJBzguoueUhvhVElemYEAUvSxPj8cGbirAg5VcYsOoTmyRTvmALzRzLo2AK4CAKcvIPK-KYMFPqd3c6ilacmTildP48HgkFTE_LdmJbd5-Dp18lSXZ45U2n3T63EEHBX-vKnxjmOqBSPY8K8wCk5ggguY-LoQr4rQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/105330" target="_blank">📅 12:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105329">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1137b6f537.mp4?token=hB7pCjIlLA8_8bwIucSQQJxClQz9nBzVHYBD-r47GAFx9q7Jh_8UuEME7b2B2GkZeyB4bal-v9L7r-ANNbVr5LYKlI9FfdPVDUipNIRaPbZlH-2XvuNViUMV5hsP_ZiBxgSzttfX5VEkKRNEWkoFd0mOx8VbyGoTHzYRcCnCiFF5tiPL_rlQi_jgtSAmnRn-4TAlu5zknOH4c6jzEYWr6rvfqszL1I2fkTsILf1oi4VdDIlLMjGRHldtsSOPVOimER_3RcUK4v7d-lKkmGnswhUoWcHbTJLz6oiy-J119XtWYbbEQiVhwpvzmDjdUT9qsfbsoZ3_NleM8exINLJExye8378wC-aGANV4_b_LkE2pmvjt23D4sEW1hWp2QF-7UmcwFsdE1cxhkPswiK4ebKU0zfuG7wJj5j9c8xvURBcAWTlB6tq8aVluUr3Q2Uq3EylYAOVbEP0hRz1JD--W0A880-yKWM0h0gUh_IIn5dtTN6TggbYV62SPWXB9tcIEDV4HZG63cK1dzn4SP6k-F_9Bga5jFe9QpuTaJ-fXivsaXN-wBSjlKxpck_-OBwNVFe5kti8CqhEB-pbg4bxaZbJywqX5sJ4Z7wpzt1hkHIvP-51PuzB31-oKljAKvboJMk-YW4mki19qJxZrnLPniR2npCyNVcMicQRGfKQ6LqY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1137b6f537.mp4?token=hB7pCjIlLA8_8bwIucSQQJxClQz9nBzVHYBD-r47GAFx9q7Jh_8UuEME7b2B2GkZeyB4bal-v9L7r-ANNbVr5LYKlI9FfdPVDUipNIRaPbZlH-2XvuNViUMV5hsP_ZiBxgSzttfX5VEkKRNEWkoFd0mOx8VbyGoTHzYRcCnCiFF5tiPL_rlQi_jgtSAmnRn-4TAlu5zknOH4c6jzEYWr6rvfqszL1I2fkTsILf1oi4VdDIlLMjGRHldtsSOPVOimER_3RcUK4v7d-lKkmGnswhUoWcHbTJLz6oiy-J119XtWYbbEQiVhwpvzmDjdUT9qsfbsoZ3_NleM8exINLJExye8378wC-aGANV4_b_LkE2pmvjt23D4sEW1hWp2QF-7UmcwFsdE1cxhkPswiK4ebKU0zfuG7wJj5j9c8xvURBcAWTlB6tq8aVluUr3Q2Uq3EylYAOVbEP0hRz1JD--W0A880-yKWM0h0gUh_IIn5dtTN6TggbYV62SPWXB9tcIEDV4HZG63cK1dzn4SP6k-F_9Bga5jFe9QpuTaJ-fXivsaXN-wBSjlKxpck_-OBwNVFe5kti8CqhEB-pbg4bxaZbJywqX5sJ4Z7wpzt1hkHIvP-51PuzB31-oKljAKvboJMk-YW4mki19qJxZrnLPniR2npCyNVcMicQRGfKQ6LqY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
چرا محمودفکری مانند کریم باقری در تیم ملی فوتبال ایران موفق نشد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105329" target="_blank">📅 12:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105328">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7p1kAJJgJHmeIT_Q0862ftWFXR11fCApKSeii7i9NvZ8N71RTGNyo40Lx5-P3STQv1kbfwOrrmtp_BFOd7ifLPub_PxBiOQrryTMECzYTjgiFFEglOGZP6kG_KqSh2uYx5JeuLSeJ4kmrddonhLheykoHMej9CymF3RgIuY21egJfSe7kjhlwnxcoD_u4sW3YmGk8cye7NGh8pF6GwOlxaILoksSBq2RkcTPk02VjJ4qnG7_6tI_TwuZOZ6eLrPC22EHmtBVKjeZ_yhOug4IPqUaimg0mr5SO_j_Hpd5n80-OwmBY1TH_lu3mF4NaQV2TrZXu0ClWZr7Hv3H4-xFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💸
🇮🇷
🇮🇷
ارزشمندترین بازیکنان فعلی سرخابی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105328" target="_blank">📅 11:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105327">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f75defa90.mp4?token=ONEicbSkrF6nY55XHZ9aXBruTxJRr4J-JHzyiEP7qSOPSlw14EQfG2asbut75mnhRAFYciayrogGfg6i8IFP-0L_0-OJw_9BpfNRAvFYHMQD_-vxVUJN0Km1s32pjRv5Q_hYMb49PoWZW6IJyiFfbBnXlfD2Ctm98fjQABvO64qai_ZKpG5G39hRUMw5nOtfDJdg4ft-l83Lrs-TAxWBO5uN7_yE7n4pFBV4OPKONTy9BysXLIOlCJDEBoYXHe_tK8queXNVjUMLwHZzxd2tHTJGYndJi2jc68bj1Xx7kOYh4ZAOpJ6z3R2zeQyYkgEHLF5CFBEIx7yvGOFelO7K231lMFgEhSDe5zKCf7HKlHYakNcZGoN6O1IAuVOmTxpQ5Xp0KOpxNe7TBvK_f7ZloFZMktqU4R-6IHaJAvPHM4EbxSPIvNF2ZoehBHisvBx3c_nC2bC57V3Zx5Fd4YpDedEJ8X2wpOoSUYdqHdkh8TN94s68Xl-5PRdHnN1o7jDqbchnRbSxAP4CVrQGSxK8JNkNiwMjcorGI8R05ieJHy3q9UuIq8WSgCRGdV9u1i8pejR1w5NGAEaUdQB8_2jEgLp7ic2ndq4ktzQ2qrO-836C_MFppfu9LxFWac-ywMdtzMz77hoNDmszzhA-om1-OOuicy7-u8Q6sn98i8Bn1go" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f75defa90.mp4?token=ONEicbSkrF6nY55XHZ9aXBruTxJRr4J-JHzyiEP7qSOPSlw14EQfG2asbut75mnhRAFYciayrogGfg6i8IFP-0L_0-OJw_9BpfNRAvFYHMQD_-vxVUJN0Km1s32pjRv5Q_hYMb49PoWZW6IJyiFfbBnXlfD2Ctm98fjQABvO64qai_ZKpG5G39hRUMw5nOtfDJdg4ft-l83Lrs-TAxWBO5uN7_yE7n4pFBV4OPKONTy9BysXLIOlCJDEBoYXHe_tK8queXNVjUMLwHZzxd2tHTJGYndJi2jc68bj1Xx7kOYh4ZAOpJ6z3R2zeQyYkgEHLF5CFBEIx7yvGOFelO7K231lMFgEhSDe5zKCf7HKlHYakNcZGoN6O1IAuVOmTxpQ5Xp0KOpxNe7TBvK_f7ZloFZMktqU4R-6IHaJAvPHM4EbxSPIvNF2ZoehBHisvBx3c_nC2bC57V3Zx5Fd4YpDedEJ8X2wpOoSUYdqHdkh8TN94s68Xl-5PRdHnN1o7jDqbchnRbSxAP4CVrQGSxK8JNkNiwMjcorGI8R05ieJHy3q9UuIq8WSgCRGdV9u1i8pejR1w5NGAEaUdQB8_2jEgLp7ic2ndq4ktzQ2qrO-836C_MFppfu9LxFWac-ywMdtzMz77hoNDmszzhA-om1-OOuicy7-u8Q6sn98i8Bn1go" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
مارک‌کلاتنبرگ: پنالتی تراکتور در بازی مقابل شمس‌آذر گرفته نشد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105327" target="_blank">📅 11:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105325">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZCCwLpGQ-D_75hRTnxVdYqCqzQ9ENFC_nODzgHdGyPmkvHy-u6RHE2EtoZyJTIjsBawZm8w5Eo22HWBfSQ4l__fQg3nu9SV4Q4vSLl2rGJJ99jgTzjV8LoEj46sG8xgk8D_w-UJtdIk5ZYfT-TaFAovnT6KWzd0-lt1MQjrXkzQ_MHT6Ln9kHKqZH5wGIep1JZIygrXqk8rPgKk9ZZs0z-QYhqYBhlTNwiKAXPpgg5gTCBiIJ95dhkPl_OzILkaNw-vmoq5cu7ACedxkgz81lTqr0gbLjFWhbTklFEMefUvPzz41xAkflWfLkQCryWyQ1q2qgCVfNOxe_WK5EfReUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VKuBkaSB__DDa72YDEUUkiFNzVRly3bPjQ8QWndZOj_NxzE_SaKvTatIkjlgaQYx3rsQXKj6qt8BhVp9VeeJljyvEyUGLG14Mrawh_gqR7GX2Kj8bpDH0V1e4IXaeLHm2Mazlg3XscerXC3kCOY_cNGOR37cEpzZ2yx9X45ce8GvZ3W5eunmSPEt92niXv89VVHkCij0k7X7LYH2XIf5L0IGMBnY9H0XFD2MftvOJY_zvZ0Bn8ZUNMevpjt4xe6m8W4txN88Vyc0SuHL6IiosDN1ubi7hBte0tqsa9zS50LxGes-Csfc2gUNcKuLYgOik2VoIKMejdy8vWzczOz2CQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
پوستر سرخابی‌ها برای دربی امروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105325" target="_blank">📅 11:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105324">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">▶️
👀
🇮🇷
🇮🇷
مروری بر دیرهنگام‌ترین‌گل‌های دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105324" target="_blank">📅 11:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105323">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XutpHViR1j6Gqj4cT16QOS5xky8PUxzuC-iR4Y3oQ8VvBbwkleSyWopCyAQdakVxRRrgOmxDsp2yk-tH_Yty9HnsEUqlwLNn6Yv2-xIR5oraP_i9-B4RHPm9Z9X-S6SikOQoAOHCnzQRHoMQAA3DKa8zhufYmNaxkrnl6GVT6jKqnH44iQQQ27Wm8rxLCgdMND3aG9ep7ztuuw_dpay1kyl04V_ex2Np57i5M83_Ritq_OeP5AjbMzutdfxBr6JQUu1FsJQyUcOCvImuWGogjdPspICkNmImdt9CMV3xFMUyqNPjh0FGHYBS8rSfgiJYr6Ij6Q6zCAvsPDo87tV2Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✅
🇮🇷
🇮🇷
مقایسه افتخارات رسمی سرخابی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105323" target="_blank">📅 10:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105322">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a3bce317a.mp4?token=r5wTg7pS8otEohByJVldztFm6IFGwlKqQszoT50ps2JW7WR5rPfo1VdGCKn-iDJcUGGVzb6183jy639gRRpnwCLeOY1_1YIcg9sq28bDA-F58zpsRFTyoXNKPSbZXCPbKPvW7T2bWmJwwbrbu5fmbwN1AFK9yIse_YRopaWK0SOBfeup1iK359Kb8z4kKYidJsGf2-FGQ8N8McSiqRu7eFdiFbWH253B7OsiY6gCjNZ183zfh0euIRtn-FtuyzzaC6nAu3VmWIzivvfHCRoY1O2bPxIR8MGWsIoRL2ez98VCYm1j68lUbN8_BA3y4J0yLNreNAPqAx4A0C57_Kec1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a3bce317a.mp4?token=r5wTg7pS8otEohByJVldztFm6IFGwlKqQszoT50ps2JW7WR5rPfo1VdGCKn-iDJcUGGVzb6183jy639gRRpnwCLeOY1_1YIcg9sq28bDA-F58zpsRFTyoXNKPSbZXCPbKPvW7T2bWmJwwbrbu5fmbwN1AFK9yIse_YRopaWK0SOBfeup1iK359Kb8z4kKYidJsGf2-FGQ8N8McSiqRu7eFdiFbWH253B7OsiY6gCjNZ183zfh0euIRtn-FtuyzzaC6nAu3VmWIzivvfHCRoY1O2bPxIR8MGWsIoRL2ez98VCYm1j68lUbN8_BA3y4J0yLNreNAPqAx4A0C57_Kec1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😂
🇮🇷
محمد نوری سرمربی صنعت‌نفت در کنفرانس خبری دیروز تیمش بازهم شاهکار خلق کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105322" target="_blank">📅 10:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105321">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
🇮🇷
🇮🇷
سه‌دقیقه فوق‌العاده شنیدنی و دیدنی با نوید استادرحیمی از دربی‌های جنجالی و خاطره‌انگیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105321" target="_blank">📅 09:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105320">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca6813881.mp4?token=K4ZLEuaOLBDf7qTom71NNz8G_xlPmziDme87LvuCm7WRlyRqfehjKNgUrfJryMWAAgh4ufhhpRQlX2kNB_uK_aIf_CIpbJ_ekjynmKW_e9tEW21LjFLYjhgR-KRHkhsXOL1XljQr6yetaRPD9znaZMSllzJrQml4CAobpNKRAUleIZNk3tGO_Ssl6jqNwWJ5tde_UmAPZe2jeyVsgt-A1luvFAdAIiqUfPE-XR534aGAtnRWl1ZZT6LXIajW-d5AITFYojZik_OU4-syVvhUndWGuisRYptXlfOWudw00hqu4nKUfbGlO5MUdRus_4nNRKu6IW0X5-LplWJ4A_X9Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca6813881.mp4?token=K4ZLEuaOLBDf7qTom71NNz8G_xlPmziDme87LvuCm7WRlyRqfehjKNgUrfJryMWAAgh4ufhhpRQlX2kNB_uK_aIf_CIpbJ_ekjynmKW_e9tEW21LjFLYjhgR-KRHkhsXOL1XljQr6yetaRPD9znaZMSllzJrQml4CAobpNKRAUleIZNk3tGO_Ssl6jqNwWJ5tde_UmAPZe2jeyVsgt-A1luvFAdAIiqUfPE-XR534aGAtnRWl1ZZT6LXIajW-d5AITFYojZik_OU4-syVvhUndWGuisRYptXlfOWudw00hqu4nKUfbGlO5MUdRus_4nNRKu6IW0X5-LplWJ4A_X9Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
🇮🇷
فقط اونجایی که صداسیما زیر نویس میکرد دیگه نیاین ظرفیت تکمیله
🥲
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105320" target="_blank">📅 09:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105319">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇷
🇮🇷
یه ایرانی رفتی از دربی کشور زیمباوه برامون ویدیو گرفته؛ به دربی سرخابی‌های خودمون تشبیه‌ش کرده
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105319" target="_blank">📅 09:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105318">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوووووری
❌
شورای تامین استان اصفهان در صورت تشدید حملات و درگیری‌ها تا ساعات آینده صبح فردا جلسه‌فوری تشکیل خواهد داد و در صورت ملتهب بودن شرایط قرار است بازی دربی را بدون تماشاگر اعلام کنند. هرچند تا این لحظه سطح درگیری‌ها به نواحی…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105318" target="_blank">📅 08:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105317">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ebf67c803.mp4?token=XT3P2MrCyTNH7wKPceh9A3BydlO53RyQ-A5ElGO6E0E0Cazmf1v8w8r00Ql_KQl466V6rPVF30nWwR71N6Wlrq50h_I2p-bC0qVxQ-rCN0Ikm5OLVZzAX7aMfHz1dO414afENXLVZXfcd3ROpX3rvbvtdP_ONzAqQ8ewMmFmVlc_hkZVjaDVR7uY4zaGh3pZ3U4ODXX9fcLqkJoYS1erLUcipOuQSDTP25waDuAWTSrvSY_ikDr48sugEBof5zlDOgwjQzybs2qCMBZA0WZ3cI5_VyM6J1kQo3R3bjH63uq-39mZLPKZJVIqr3Pvn-E5v4eAPcQ7cQtCoETp8fGHlTgoOyRd0BlYEU7sLfJXHtqD8y4Tzfyey51MR3iwsf3JmrX4Mk_dJLVN9Ezl_l-2ZS7J7fKpOMcSU3tbhjJdIyiHPNfTpa13zZ9uXCSlpT30XwBv2a2XLk3l7ymUqM8i6cdAasYmouHuPEHUmnhePKCrZPfm3vlHDIZYwSYhgfwkxv4pjycXzRQtL1R4i6ZR3IjpQ-OFArt_r7EdjJNXQPtjIyjm8LDdn31Xfu878F2whcrph-XTtIYkUt_rUYKr6hSm7a42n_Nq9LrN_2uLOSYL8m-YwX1_5Rrx6Kaker3OsC00rNLP0DrARP4i_HTWinuJaeUxSokO3_uTpOYbrIc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ebf67c803.mp4?token=XT3P2MrCyTNH7wKPceh9A3BydlO53RyQ-A5ElGO6E0E0Cazmf1v8w8r00Ql_KQl466V6rPVF30nWwR71N6Wlrq50h_I2p-bC0qVxQ-rCN0Ikm5OLVZzAX7aMfHz1dO414afENXLVZXfcd3ROpX3rvbvtdP_ONzAqQ8ewMmFmVlc_hkZVjaDVR7uY4zaGh3pZ3U4ODXX9fcLqkJoYS1erLUcipOuQSDTP25waDuAWTSrvSY_ikDr48sugEBof5zlDOgwjQzybs2qCMBZA0WZ3cI5_VyM6J1kQo3R3bjH63uq-39mZLPKZJVIqr3Pvn-E5v4eAPcQ7cQtCoETp8fGHlTgoOyRd0BlYEU7sLfJXHtqD8y4Tzfyey51MR3iwsf3JmrX4Mk_dJLVN9Ezl_l-2ZS7J7fKpOMcSU3tbhjJdIyiHPNfTpa13zZ9uXCSlpT30XwBv2a2XLk3l7ymUqM8i6cdAasYmouHuPEHUmnhePKCrZPfm3vlHDIZYwSYhgfwkxv4pjycXzRQtL1R4i6ZR3IjpQ-OFArt_r7EdjJNXQPtjIyjm8LDdn31Xfu878F2whcrph-XTtIYkUt_rUYKr6hSm7a42n_Nq9LrN_2uLOSYL8m-YwX1_5Rrx6Kaker3OsC00rNLP0DrARP4i_HTWinuJaeUxSokO3_uTpOYbrIc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
روایت فرشید باقری از درگیری عجیب سیدجلال و مهدی رحمتی در دربی ۸۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105317" target="_blank">📅 08:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105314">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
اگه استقلالی هستی، به هیچ وجه این کانال رو از دست نده!
⭐️
💙
📸
پوشش کامل بازی‌ها با عکس و فیلم‌های اختصاصی توسط خبرنگاران و عکاسان ما
📰
اخبار و حواشی داغ آبی‌ها
🎁
🎁
و قسمت جذاب کار: هر هفته قرعه‌کشی به همراه کلی جایزه
🔥
🔥
اینجا فقط یک عضو ساده نباش، محتواتو بفرست…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/105314" target="_blank">📅 01:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105313">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbwzC9XFp4k2mSfu9-w8192ZG2T-B830MTFrmX541-eYzVQFsnp1YVgyPDtHTbbgJ2rp5NsjuFRuhHIEi0_fA3aEkLAK4vpqF2qN9Hun6WUq1b2UpGMTx_gdes0vNYhzV8-LDoBQaGMvNY1b8_HEenENewFWFLBlDbiHsdKUjOtR3cAtcijNoH4L89VR32GoB9hh_riP7P8RjbRqKEz23V1gyOXBwpUGXvjwpdOMAmC5FCzjjKW5BZ7CcP7g4SWPVv_IgpbEBq-AbRvtjtPYhQnmaGTG20pMi7o3U5GNyQiz8BvRET21XLz07SCJ3Q8yeZ16a-RGSbJNNT6ZjHAc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگه استقلالی هستی، به هیچ وجه این کانال رو از دست نده!
⭐️
💙
📸
پوشش کامل بازی‌ها با عکس و فیلم‌های اختصاصی توسط خبرنگاران و عکاسان ما
📰
اخبار و حواشی داغ آبی‌ها
🎁
🎁
و قسمت جذاب کار: هر هفته قرعه‌کشی به همراه کلی جایزه
🔥
🔥
اینجا فقط یک عضو ساده نباش، محتواتو بفرست و منتشرش کن
🔥
با استقلال... برای استقلال
👇
💙
@Esteghlaal_twitter
@Esteghlaal_twitter</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/105313" target="_blank">📅 01:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105312">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/105312" target="_blank">📅 01:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105311">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⭕️
⭕️
با توجه به نزدیکی به دربی پایتخت و بازدهی فوق‌العاده تبلیغات تا پایان هفته، اگر تمایل به همکاری و انجام تبلیغات مدنظر خود داشته باشید، با ×تخفیف ویژه× در مجموعه تبلیغاتی تیوا با بیش از ۱۵ کانال مختلف ورزشی و غیر ورزشی در خدمت شما عزیزان هستیم   برای هماهنگی…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/105311" target="_blank">📅 01:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105310">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
⚠️
یک فرد ناشناس در مشهد با خودرو به تجمعات جانفدایان ولایت حمله کرده و تعدادی کشته شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/105310" target="_blank">📅 01:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105309">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f42b196ef1.mp4?token=czWeYcGuHu_CPc3U8Z2hf7AS6tUl4coJlKUvq20UF_hCEIVeLjUwyBZXFjv-XpER2HLm6GV1Lx-IuW80hs08VI9DBNJ8KZF_EEZGBSmIbA230Swx_Gg8_niybH8LmPV9fCgvYgKWOR7Z2om4nz2n3gztq43dWCMUSzPoZheJ2SSM8mIi28H1RTBPYec2H3rMo8cFZAAX45BgrGaiCYdMDmt-BcTL5LQzBLM48iEJXeJeQiEFukV3JdcwONpPSicV44i-llbx8CNhjTvC3qn4eobSdedOuEG1XMlu12SCnH9bDMfGkt-c2D_GUDYJ1wVlqET1_NnpHvCb0EWmvQiRjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f42b196ef1.mp4?token=czWeYcGuHu_CPc3U8Z2hf7AS6tUl4coJlKUvq20UF_hCEIVeLjUwyBZXFjv-XpER2HLm6GV1Lx-IuW80hs08VI9DBNJ8KZF_EEZGBSmIbA230Swx_Gg8_niybH8LmPV9fCgvYgKWOR7Z2om4nz2n3gztq43dWCMUSzPoZheJ2SSM8mIi28H1RTBPYec2H3rMo8cFZAAX45BgrGaiCYdMDmt-BcTL5LQzBLM48iEJXeJeQiEFukV3JdcwONpPSicV44i-llbx8CNhjTvC3qn4eobSdedOuEG1XMlu12SCnH9bDMfGkt-c2D_GUDYJ1wVlqET1_NnpHvCb0EWmvQiRjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚠️
تصاویر دوربین مداربسته از حملات پیاپی به نزدیکی یک مراسم عروسی سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/105309" target="_blank">📅 00:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105308">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAMjrewbGufGPB0qyWzC6k4uBblf56I8Csk3nVMXofGVx0aX_O58jby84L16o4yVLZAdooo4R_N1u8xbp5J4xq0GWqejV37uIyzChxA7Tyg8KoU-xPFxXTve5rvAfgGyJaWz8fEoDh-IkbRYBSjLVUHcA61gx3j7Iw-HawW4b0LybL0JMWEieCSqpguL4PY8NErcJTWkSWDMEwu9Pra_Nmcmn6mw4c2bUhfdIb7hvC6nQfZSS8hZoKT8mqzUDuBabM9JVgmo3EaSSdHbh76Ld4kNz6A4HRAM-oulQIBJYmmQbD2V7C5V0XfU_iTQ9oCKLpUmYQlT0yMtAMCcoGNquA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوووووری
❌
شورای تامین استان اصفهان در صورت تشدید حملات و درگیری‌ها تا ساعات آینده صبح فردا جلسه‌فوری تشکیل خواهد داد و در صورت ملتهب بودن شرایط قرار است بازی دربی را بدون تماشاگر اعلام کنند. هرچند تا این لحظه سطح درگیری‌ها به نواحی…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/105308" target="_blank">📅 00:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105307">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوووووری
❌
شورای تامین استان اصفهان در صورت تشدید حملات و درگیری‌ها تا ساعات آینده صبح فردا جلسه‌فوری تشکیل خواهد داد و در صورت ملتهب بودن شرایط قرار است بازی دربی را بدون تماشاگر اعلام کنند. هرچند تا این لحظه سطح درگیری‌ها به نواحی…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/105307" target="_blank">📅 00:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105306">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180
#فوووووری
❌
شورای تامین استان اصفهان در صورت تشدید حملات و درگیری‌ها تا ساعات آینده صبح فردا جلسه‌فوری تشکیل خواهد داد و در صورت ملتهب بودن شرایط قرار است بازی دربی را بدون تماشاگر اعلام کنند. هرچند تا این لحظه سطح درگیری‌ها به نواحی اطراف استان اصفهان نرسیده و این اتفاق تقریبا بعید است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/105306" target="_blank">📅 00:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105305">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cf9805271.mp4?token=bXOnqYBsbgI6LIJEQ4ruK_YP4NHvhC5Vv-KExsrFfbmgEKyulWonUrN89Q8kuKeetLkKfLT2_KdmSlXui2JFNdRVFSMmASmf07FUBqYMFdkNOV_2lVQBg-1zZBcvUlBGXn9KWjzuL-GLUWul8_CdobfaXhFEccfEFWJksPrHCmwj7pZFmGYb7pTFqmAH3gpugUMEzzmSclnZvX9jaoOPl7VA3hZhvRQwbZ1RFKsH0gylRloBRMLwWlX356eKKCrqxDGLjJkNFrtK2SqkUKmfEYaycE8C49Phdoqv2fQySRZWQ2ElvQq9Z88W6oX-Qtq7r6_eqfdB7rtZP0vw1RrE7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cf9805271.mp4?token=bXOnqYBsbgI6LIJEQ4ruK_YP4NHvhC5Vv-KExsrFfbmgEKyulWonUrN89Q8kuKeetLkKfLT2_KdmSlXui2JFNdRVFSMmASmf07FUBqYMFdkNOV_2lVQBg-1zZBcvUlBGXn9KWjzuL-GLUWul8_CdobfaXhFEccfEFWJksPrHCmwj7pZFmGYb7pTFqmAH3gpugUMEzzmSclnZvX9jaoOPl7VA3hZhvRQwbZ1RFKsH0gylRloBRMLwWlX356eKKCrqxDGLjJkNFrtK2SqkUKmfEYaycE8C49Phdoqv2fQySRZWQ2ElvQq9Z88W6oX-Qtq7r6_eqfdB7rtZP0vw1RrE7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
⚠️
یک فرد ناشناس در مشهد با خودرو به تجمعات جانفدایان ولایت حمله کرده و تعدادی کشته شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/105305" target="_blank">📅 00:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105304">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcaf59f19.mp4?token=fG7zsvtibOTJ6Xgf7J-cZTtlXPcxgBmI7vZfpk1ll3HbyU4eGck1FxBt3yjgsZ6kfah8Ikd639Nxx5iOIlY7ZFj1_OZpzID6_uUPs2hhVNl1KpDSffA9iZnOEVoOUMgBjuxzkMfUKIVE1IbscdZ2fAnzUi3JSEX21FK5fQ-7vITsqigYoPdE_THtpq0bnP17LSZ_jNfbvx7YVWg6QSIQASCEGMVgzuSe2VeK7OWPLxzYtdJoemTp26IOqdUm5t6dEv8mz6m5eWFFKX3ntEVB-LhY6PO4kjj4lqLTwBPsgMTmhmyPZalCfQonuMf7Ryj4XgEnSsrvfzLVDz5tqTVdbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcaf59f19.mp4?token=fG7zsvtibOTJ6Xgf7J-cZTtlXPcxgBmI7vZfpk1ll3HbyU4eGck1FxBt3yjgsZ6kfah8Ikd639Nxx5iOIlY7ZFj1_OZpzID6_uUPs2hhVNl1KpDSffA9iZnOEVoOUMgBjuxzkMfUKIVE1IbscdZ2fAnzUi3JSEX21FK5fQ-7vITsqigYoPdE_THtpq0bnP17LSZ_jNfbvx7YVWg6QSIQASCEGMVgzuSe2VeK7OWPLxzYtdJoemTp26IOqdUm5t6dEv8mz6m5eWFFKX3ntEVB-LhY6PO4kjj4lqLTwBPsgMTmhmyPZalCfQonuMf7Ryj4XgEnSsrvfzLVDz5tqTVdbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
جملات قصار و واکنش منصوریان به حکم انضباطی علیه الطلبه؛ از جیب خودم خرج می‌کنم رای برگردد! مستقیم می‌ریم CAS؛ یونس محمود ١۵ سالش بود من بوندسلیگا بازی می‌کردم
❌
⚠️
در شرایطی که دیدار الطلبه و نوروز در هفته سوم لیگ عراق با برتری ۱-۰ شاگردان علیرضا منصوریان به پایان رسیده بود، کمیته انضباطی فدراسیون فوتبال عراق حکم به شکست ۳-۰ الطلبه داده است.
😀
دلیل این تصمیم حضور همزمان ۲ بازیکن الطلبه با پیراهن شماره ۷۷ اعلام شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/105304" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105303">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6jNj0153gp1TpkvWA4GqpI1Wz6cLmk7p8o6cczuwMUUzWKvt3Yg9j9cnKyNxKvJulFzXEnL1vAktJ4j3JhIMsV9jUA-SrZILZAH0epoMs5Yq2S_Eq8Uwo-BePXn25-DmQRNVa-jqdIIpFK2cc4Ut8XgKALfq44Fuw7GNYuAxDKcTNiTisVPd9SItpt00gqTm0hjdjjEi7NlEBIzZVnVTnoN06hiZn6lBluqis7DCdi2svnSpAb4dfw94zax5tBwdr2R3Oe56sBbMiRKAl-RrZDVbBazMLG3MtSOo_CwozkXvWUvjUyoF_Hh1zQxl9SgtVVjMKsWUiNoi_JIkA-RoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رسمی؛ اندیایه با قراردادی پنج ساله به ارزش 65 میلیون پوند از اورتون به سیتی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/105303" target="_blank">📅 23:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105302">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
گزارشات فعالیت شدید پدافندی در شرق تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/105302" target="_blank">📅 23:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105301">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👍
🇮🇷
بانوان جذاب ملوانی در بازی با پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/105301" target="_blank">📅 23:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105300">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f706e532c0.mp4?token=h236NRUo6NE9asCMoWNXjv6GrxnY-yg5_RRd6Ml9W95xMk98jjQWRo5h9P2j0PRCkExQapjcW18OKKAZY336Ren0I9Fk07UjKkjWjDnjaj9re2KV8idvMl4Gn31xfnmUf7v2ZwSYSgs3UUqopY10x6tZU9JgBsZn9ULy6fRV7iYpWGUygP0HoqkIuKllTgoIe4it118DlTbbWv1ZxMEt-waQEsC-1OaDaBIXkwNSbZmZl_HMqgz3JX4md2dqNJ3bgjxQLphu2hm00PVMGNmzwk8kpw_bvvsde9mwhwfsczfaYdM69Prhsh9tPd84c2nz_WNEHcIR5eRTjPB2-YMT9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f706e532c0.mp4?token=h236NRUo6NE9asCMoWNXjv6GrxnY-yg5_RRd6Ml9W95xMk98jjQWRo5h9P2j0PRCkExQapjcW18OKKAZY336Ren0I9Fk07UjKkjWjDnjaj9re2KV8idvMl4Gn31xfnmUf7v2ZwSYSgs3UUqopY10x6tZU9JgBsZn9ULy6fRV7iYpWGUygP0HoqkIuKllTgoIe4it118DlTbbWv1ZxMEt-waQEsC-1OaDaBIXkwNSbZmZl_HMqgz3JX4md2dqNJ3bgjxQLphu2hm00PVMGNmzwk8kpw_bvvsde9mwhwfsczfaYdM69Prhsh9tPd84c2nz_WNEHcIR5eRTjPB2-YMT9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🔴
خداداد عزیزی: داور عجله داشت بازی تمام شود
. چجوری 2 دقیقه اعلام کردید؟ وقت اضافه را کی می‌گیره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/105300" target="_blank">📅 22:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105299">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f17ff9c0b.mp4?token=aymtm9CrGXUHizv2_OTEfwLKhOU4pEDZacdsT5K7o8dMiqMW1AdM1yq_s1VuIuyH4hfWXlr--O20wRvVcMq0a67C4ugpIq8mz4Qx2K-LOhn0Ddef8tfO_R3W047BE-UP3GCZjWXvu-yth6jwNau4gYJXgEb5QhtJCO3uJZimet2yhIhhWGso0Km9wowbk7iodMAoAiNMTI94uOvi_ZBa4wiy00RTtZPaL6L0zPxzVlE6j_eOUqk_35VCeMKsh2vHUcXn33Bz_JYXMV337s7rVi4Q9aEf21VtCZ6n9w6Iww56QNZ3Nt32Z7sKw_F2_8n5ixypEfGCjgapHTIlBf1aKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f17ff9c0b.mp4?token=aymtm9CrGXUHizv2_OTEfwLKhOU4pEDZacdsT5K7o8dMiqMW1AdM1yq_s1VuIuyH4hfWXlr--O20wRvVcMq0a67C4ugpIq8mz4Qx2K-LOhn0Ddef8tfO_R3W047BE-UP3GCZjWXvu-yth6jwNau4gYJXgEb5QhtJCO3uJZimet2yhIhhWGso0Km9wowbk7iodMAoAiNMTI94uOvi_ZBa4wiy00RTtZPaL6L0zPxzVlE6j_eOUqk_35VCeMKsh2vHUcXn33Bz_JYXMV337s7rVi4Q9aEf21VtCZ6n9w6Iww56QNZ3Nt32Z7sKw_F2_8n5ixypEfGCjgapHTIlBf1aKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇮🇷
🇮🇷
همچنان از بانوان پرشور اهوازی در حاشیه بازی استقلال و فولاد خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/105299" target="_blank">📅 22:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105298">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344f252bb4.mp4?token=frZ5gOD8rFSi2J5YMgrh7zoxPDjwyHvtWqICIVH0lAHoEqnSbtvJHll9S_4wIA-8dcfkoEq6oaArSpnTXq-TNgGD61H_FUo4A-u2hPKn7yLgkKwdRlrah5z5AdKjrfIFpsKJ9QHAsZOnh-rMby1bLbsRyzXjTm5k84u5ATSV6x0Wcc3gIH0Cj2a9VmqTd-vFESKEmU72XJyuCJSWUmVNju7eToCQNTi42YCgGYeDk8nteRFYrOOz-AhJWZTkfDTKgxEcMNKEaCEs57Nb-b9D34B7D4kYygLFKLL6pnjZ0xbRy-ycpzNcncB1-_pwy21K9oAiFlHVh1jFc2M-HFtU6izFRmKNztIolc52bXUFxDoyxZ7kMECvZAJl5341UPWlK9YMkCgl63VX61kyslSqB433fXz2KrOO08UJ4Ux6EqDUhHlk0MsI_kyhP_jvMTSp7FbZjvleQ_DLSZDXxXANa6uzZpgGxag3GqftSKTf0z8eKW-xWCEXnyAerfwoGn11AC1eS_hOw4RmfnDYtiMeM9-tPmjJX3NP57QlGpZwo9tF_2fV23pEb9FRjF-9f-1-gWJQ_UrqcvIM6hFQibpLdyXqo3t7TtG7Fk2OXL6UMwAlouL9smwP-EOnw1Cz-5lthjhkduB1BgnsQnPxxsi03st6I8n4J4WRYnwwO9Y8A0s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344f252bb4.mp4?token=frZ5gOD8rFSi2J5YMgrh7zoxPDjwyHvtWqICIVH0lAHoEqnSbtvJHll9S_4wIA-8dcfkoEq6oaArSpnTXq-TNgGD61H_FUo4A-u2hPKn7yLgkKwdRlrah5z5AdKjrfIFpsKJ9QHAsZOnh-rMby1bLbsRyzXjTm5k84u5ATSV6x0Wcc3gIH0Cj2a9VmqTd-vFESKEmU72XJyuCJSWUmVNju7eToCQNTi42YCgGYeDk8nteRFYrOOz-AhJWZTkfDTKgxEcMNKEaCEs57Nb-b9D34B7D4kYygLFKLL6pnjZ0xbRy-ycpzNcncB1-_pwy21K9oAiFlHVh1jFc2M-HFtU6izFRmKNztIolc52bXUFxDoyxZ7kMECvZAJl5341UPWlK9YMkCgl63VX61kyslSqB433fXz2KrOO08UJ4Ux6EqDUhHlk0MsI_kyhP_jvMTSp7FbZjvleQ_DLSZDXxXANa6uzZpgGxag3GqftSKTf0z8eKW-xWCEXnyAerfwoGn11AC1eS_hOw4RmfnDYtiMeM9-tPmjJX3NP57QlGpZwo9tF_2fV23pEb9FRjF-9f-1-gWJQ_UrqcvIM6hFQibpLdyXqo3t7TtG7Fk2OXL6UMwAlouL9smwP-EOnw1Cz-5lthjhkduB1BgnsQnPxxsi03st6I8n4J4WRYnwwO9Y8A0s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
حمله شدید اللحن شجاع خلیل زاده به عادل فردوسی پور: همه می دانند فردوسی پور با تراکتور مشکل دارد!
💬
شجاع خلیل زاده: من دو سال است که فحش می‌خورم اما خم به ابرو نیاوردم/ فشارهای زیادی روی من است و خدا را شاهد می‌گیرم که در مقطعی می‌خواستم از فوتبال خداحافظی کنم اما این کار را انجام ندادم/ دو سال فحاشی به من شد. تمامی این فحش‌ها تقدیم به عادل فردوسی‌پور/ همه مردم تبریز می‌دانند عادل فردوسی‌پور با تراکتور مشکل دارد/ از زمان برنامه 90 همین بود، الان هم همین است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/105298" target="_blank">📅 22:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105297">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1acbc66f12.mp4?token=nVr9qQPitRX_pH1LS1d3_7t8e6oxRP36GGNMyZLoqlVyedIxkhVK5QNRp1LqOVJ-mJ4Lj0WDdCclBskZ-uxn4EksoGmowSr9ObubZ6YeOSVImoSgB_1O5e9suOU68t2pYkQC0leqwfyuA9zobT70OfvpSkethFmMh9uID-2kO69IPRdS0gPjw7xuOTMSqtFvvqSTxGuS2-lSfjl-vh0-LEcodlpgxEdHmdtbnITB4V4X7S2dOFglESRL-2nLm6VgAYX1N26w_hiPq-OsHvtB--7sW9wkPXJBuzpbj2ZKbz61QX4cLJOcvNnR9LAlc11LCq91hFNjqoiw8nubKqCrzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1acbc66f12.mp4?token=nVr9qQPitRX_pH1LS1d3_7t8e6oxRP36GGNMyZLoqlVyedIxkhVK5QNRp1LqOVJ-mJ4Lj0WDdCclBskZ-uxn4EksoGmowSr9ObubZ6YeOSVImoSgB_1O5e9suOU68t2pYkQC0leqwfyuA9zobT70OfvpSkethFmMh9uID-2kO69IPRdS0gPjw7xuOTMSqtFvvqSTxGuS2-lSfjl-vh0-LEcodlpgxEdHmdtbnITB4V4X7S2dOFglESRL-2nLm6VgAYX1N26w_hiPq-OsHvtB--7sW9wkPXJBuzpbj2ZKbz61QX4cLJOcvNnR9LAlc11LCq91hFNjqoiw8nubKqCrzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
تناقض عجیب در صحبت‌های پیام‌صادقیان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/105297" target="_blank">📅 22:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105296">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
آغاز حملات موشکی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/105296" target="_blank">📅 21:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105295">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2a82a31c.mp4?token=dgxLNUANp-z0UHo4KHxGPlKK92U_C1B11fqj3alCXrcHqI4GbJPI1w4_USwuEdShGrQKHlXBv3bXfL9G5oKyV26yQ20SsZI3w6nskuqgaad28hnulUC0ovBFl1mJFHEw2gK1gXXnMwCcXb2dBkvPPtj5MXvevUp2SoOLll1EuVWK8d0k7PH2uLFOANN3JxokdGEU2yV9tG4khY4fmwpdNmbIZnhIM3I69feyHSWNbtm7Wk5aN_rgt8NL3rOGaCIbyB1WvvbUnQLOnEc006ushDQwC3XAQq1jiiMYfvIZ-LQJTrMKTGu8O_JFLLaCmPTOzlxbpXGnb_BIPMN-E3c7rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2a82a31c.mp4?token=dgxLNUANp-z0UHo4KHxGPlKK92U_C1B11fqj3alCXrcHqI4GbJPI1w4_USwuEdShGrQKHlXBv3bXfL9G5oKyV26yQ20SsZI3w6nskuqgaad28hnulUC0ovBFl1mJFHEw2gK1gXXnMwCcXb2dBkvPPtj5MXvevUp2SoOLll1EuVWK8d0k7PH2uLFOANN3JxokdGEU2yV9tG4khY4fmwpdNmbIZnhIM3I69feyHSWNbtm7Wk5aN_rgt8NL3rOGaCIbyB1WvvbUnQLOnEc006ushDQwC3XAQq1jiiMYfvIZ-LQJTrMKTGu8O_JFLLaCmPTOzlxbpXGnb_BIPMN-E3c7rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
افشاگری فرشید باقری بازیکن اسبق استقلال: پاتوسی سر پنالتی چیپ دربی با فرشید اسماعیلی درگیر شد و ما جداشون کردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/105295" target="_blank">📅 21:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105294">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e8d66f699.mp4?token=q8BASTIjoj_XaMFlkgRgM9Y8tJ4He3IiVo0V4bp5qkBgVtoaAhopfBpYfZBOZudaGNOo6nbdA3a5G5jHvb1GS6sdRexxnTCo9f53DyFrn1cmWIasnIbFKz5zbZSWDzatuKVqt0ck7QIpQI5MQZVkdBqMeWjH4vyEUGL2AHjLrIV6fE14Wj5fX_K1S0sL-r172EKEySTj0fr2cdwdaTXy28FmsAos4gGSZDOnjb_MnkvsuOeIoh2NjNwNClnt7KMYYpu89bYKymjZROmDHek6wDYbMHfTlJ1Wnc-FR18045JBpH_g6YOpYnn-2bvyWJdxsYjeFyqURMFwUFrO-BRe-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e8d66f699.mp4?token=q8BASTIjoj_XaMFlkgRgM9Y8tJ4He3IiVo0V4bp5qkBgVtoaAhopfBpYfZBOZudaGNOo6nbdA3a5G5jHvb1GS6sdRexxnTCo9f53DyFrn1cmWIasnIbFKz5zbZSWDzatuKVqt0ck7QIpQI5MQZVkdBqMeWjH4vyEUGL2AHjLrIV6fE14Wj5fX_K1S0sL-r172EKEySTj0fr2cdwdaTXy28FmsAos4gGSZDOnjb_MnkvsuOeIoh2NjNwNClnt7KMYYpu89bYKymjZROmDHek6wDYbMHfTlJ1Wnc-FR18045JBpH_g6YOpYnn-2bvyWJdxsYjeFyqURMFwUFrO-BRe-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇮🇷
💥
خانم‌مریم‌یکتایی هستن مجری تلویزیون جم‌اسپورت و گلر جدید تیم‌بانوان باشگاه استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/105294" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105293">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFdSsDuEIWUGDFAE7bwjbAqvtiGACCNCiJQP2aZ7sK62VwGnFm9mQEQBFUEaTFG4vdZ8fnhvvNyyT1lz3sQmKPY_pL2rN3HH0X2FkSfxRVHCPLLIi9V1_SXWCDo1Wkq-8MzjloisE5DZOHCettJU1r2lJ7RlAC8YuKnonE9eXC6OsP-Tc7i8z6P8fM1c4TH_cV0vJsOrFiRNCFC3rGA0TFvP7MecPAdSab81feb4qJETO78Kq34eDcShWfUi_LMyQDzGI-mJCubiedDrOjaqcIT7guG7Doku_NTmsbTWTgY8t634BU9Efn67se8BdVeO3YITobEm0z9VxTmMjLLT9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
#فوووووری
از ترامپ:
🔻
‏"در حال حاضر، ایالات متحده حملات هوایی را علیه اهداف ایرانی در نزدیکی تنگه هرمز انجام می‌دهد. این حملات گسترده و قدرتمند هستند و در پاسخ به تلاش ناموفق ایران برای کارگذاری مین‌های دریایی در این تنگه (که در حال حاضر عاری از مین است، زیرا مین‌ها یا به طور کامل جمع‌آوری شده‌اند یا منفجر شده‌اند) و همچنین شلیک هشت موشک توسط ایران به پایگاه نظامی ما در اردن انجام شده است.
🔻
اگر ایران به این حمله توجیه‌پذیر پاسخ دهد، مجدداً و با قدرت بیشتری و در سطحی بالاتر مورد حمله قرار خواهد گرفت، اما این بزرگترین حمله نخواهد بود. بزرگترین حمله هنوز در انتظار ایران است و وقتی به پایان برسد، از جمهوری اسلامی ایران تقریباً هیچ چیز باقی نخواهد ماند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/105293" target="_blank">📅 21:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105292">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/649b5fb52a.mp4?token=mmXAyf7M5UkVVU9yEpnlI-w6FYmWpRm_0iKxeN85UMX8tRKrAqCRL5BN7okw0QZoHt--_VnCuRV0ZI4mlO4SHpy3u8RXwNJSBUtI4-LorwaWnb0ZZlbceqIpVJZPd8fcY5rgT2DP67MKuVy8lPl_8ZXNX2kyQ7xHbl-a0zrHcaDNWE62R0CsIpYZlwPfeU6_LlEeGsWUSKRCJzRVe_zpHC73CrOG1TcFwPktkI8351-jQMdYJxocbLdJYKrobXErEPuKeyjwvL2HKlX-ouv94bs9y5RBBYm6NzYet2XmXgUbJTw0WoZJAs78PatJprkekDymvJrM1mMCB68THWXrjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/649b5fb52a.mp4?token=mmXAyf7M5UkVVU9yEpnlI-w6FYmWpRm_0iKxeN85UMX8tRKrAqCRL5BN7okw0QZoHt--_VnCuRV0ZI4mlO4SHpy3u8RXwNJSBUtI4-LorwaWnb0ZZlbceqIpVJZPd8fcY5rgT2DP67MKuVy8lPl_8ZXNX2kyQ7xHbl-a0zrHcaDNWE62R0CsIpYZlwPfeU6_LlEeGsWUSKRCJzRVe_zpHC73CrOG1TcFwPktkI8351-jQMdYJxocbLdJYKrobXErEPuKeyjwvL2HKlX-ouv94bs9y5RBBYm6NzYet2XmXgUbJTw0WoZJAs78PatJprkekDymvJrM1mMCB68THWXrjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🍷
تلاش خداداد عزیزی‌ برای یاد دادن اصطلاحات پیک زدن در زبان فارسی به اشترکالی
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/105292" target="_blank">📅 20:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105291">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0375b01ecb.mp4?token=VrAYUiE52usIWec68CYm7Wjf9y-Vl93Ln0FHieKFuzsfkqBfAFOwr9D2LnebVBSfvTbrT1c-tCTrjlDj9lZfBMB60bi7mvUMhIR8lHXjuPw2WBhlcjCH2Yg1JR-_yf-q0OSh50m35Dg5LkBisEEt13bVXNxISE4dPFrVhAhwDPEIBMTuzvyxMrI9vIAwH8ghLFjtXX3AK5nsg6RYZFy_-Iamnn-6dB7UcZA1dpeOo46uNTzaH4ensZWBIDomhDhlKYLs-1XOvckm68CzP5nDYkI8nhXQeV6uXjfh1u31s9N2MKTGnJoeI1O1YL8B63pLeEodoEAGLPIJDXjbOlzWnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0375b01ecb.mp4?token=VrAYUiE52usIWec68CYm7Wjf9y-Vl93Ln0FHieKFuzsfkqBfAFOwr9D2LnebVBSfvTbrT1c-tCTrjlDj9lZfBMB60bi7mvUMhIR8lHXjuPw2WBhlcjCH2Yg1JR-_yf-q0OSh50m35Dg5LkBisEEt13bVXNxISE4dPFrVhAhwDPEIBMTuzvyxMrI9vIAwH8ghLFjtXX3AK5nsg6RYZFy_-Iamnn-6dB7UcZA1dpeOo46uNTzaH4ensZWBIDomhDhlKYLs-1XOvckm68CzP5nDYkI8nhXQeV6uXjfh1u31s9N2MKTGnJoeI1O1YL8B63pLeEodoEAGLPIJDXjbOlzWnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به جمع بزرگان تاریخ منچستریونایتد خوش اومدی، برونو فرناندز
👏🏻
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/105291" target="_blank">📅 20:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105290">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGziOb_f9oGB0jSy5eMIAh96vQ549g9vQQvdXhGWI7RVzIIsbMFea4GqDm6iqRaasVEcqbu6ryGGvInp2pHUnCbJvVfBmF7MkI5PoeIsW2Bs_Phyt5_R8f4SOrR3-0s1zU7IjDrb3xYms1Da-sceSQSdfpEXE_wbBq5yGpNKuB93nlnXZ95NKqBVK8yV0wq1LoVOM_IdY8AOPYh0Jroo1VLXtqnWd7klaKmL5Vqyl-TgabcUftHuuwP-XaBxxjLoKK4-ET0YYq91ytbWrvfwJIfdPv5KD3mP9EVrkH-_HkHIvG2luyx7sxHzbSHED6m6E09_alMX1Dlv1B3H3YTVXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
ترکیب الهلال برای دیدار با الاهلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/105290" target="_blank">📅 20:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105289">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
موج جدید حملات ارتش آمریکا به مناطقی از بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/105289" target="_blank">📅 20:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105288">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Anh3tXaS-i3vEhqmfxIOmXSseGPW2x-Bp_tUvAgqnyZUobDvEheXtK9W_-kqa1ZGwCaZFITMy2oQZdknildiHJ3qROsOXsXvYg9_9wYhvOHQYH1R3r4uk2t3w6Rk2spJPW9CcqlSfV5BcC5hWq9jeE6iOzmKwkXtEOScAm5hMmTDutP67xrH3pTBOXstIw1QjGkTR9zxoJRD9sHYxXm5JrdOvcHUAJCtC7YzemdXMmhx44pjX1gQ2cY2awrkgOHuXmrOxtY3fPr4tV0_SRi6MJrxfqHLGSMlc70uwDD-xvZtVpJyNsn92C6jbRzzDzepng1VPIk1G9RF5ghGQDzXxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
ترکیب
الهلال برای دیدار با الاهلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/105288" target="_blank">📅 19:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105287">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
موج جدید حملات ارتش آمریکا به مناطقی از بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/105287" target="_blank">📅 19:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105286">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
آغاز حملات آمریکا به نواحی جنوبی ایران از جمله میناب، کنارک، چابهار، قشم و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/105286" target="_blank">📅 19:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105285">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
متئو مورتو: مارک کاسادو با قراردادی قرضی به لاکرونیا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/105285" target="_blank">📅 19:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105284">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBF5AVsH9X6hayPYyE3OdHyc0iAfthyjLU6yB2F0GMOH_Ai78UdN-Amxlgi7KSiyOUlrQJyKAfbabaUC7CdvzZNK5TRZ5TF6s3L2dhw5HCNs6pW52TO6BSrwCT3YppouR72IS4GpYjSX6pef_ViUv63XaaesgBgBsWakqQvIA70dB7JlgnM3_pjhqx8Hsn5xyJvy3TEvstuw2h3uR403AwPRug5vTOFLTLBFUHmNW-j6cMrMPeOKNUh6AgPm4BGudJ_02VekVGyjRyBIySlFLGk6m7_Va5-RSau8AF8u0spxZe5t9GxGqUJvc-OtcatNA8gNZZDczwlN-kxQKalbug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
متئو مورتو: مارک کاسادو با قراردادی قرضی به لاکرونیا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/105284" target="_blank">📅 19:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105283">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
آغاز حملات آمریکا به نواحی جنوبی ایران از جمله میناب، کنارک، چابهار، قشم و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105283" target="_blank">📅 19:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105282">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🎙
🇮🇷
صحبت‌های سهراب بختیاری‌زاده سرمربی استقلال در نشست خبری پیش از دربی:
🔵
دربی همیشه خاطره‌انگیز است و بازی‌ای است که در تاریخ برای بازیکنان ثبت می‌شود. ما شاید موقعیت‌های بیشتر و بهتری نسبت به فولاد داشتیم ولی استفاده نکردیم ولی از بازیکنانم با توجه به شرایط هوایی اهواز راضی هستم. امیدوارم بی دقتی هفته قبل را فردا جبران کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105282" target="_blank">📅 19:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105281">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ao4CFgxGUgQJc3g53yo4PwtMPbIi1JpOaVU-fxcvcpx1gRq4x1m4ZAWZXfY1VB3Vi4nLB9GxCEs3oOM9mrGI13vhxfCCq4EZRNJ1E5Fjj8E3ItCesZyq1mjWzBdizUAw09X0PlVF19g87UfLrjxnXl5Zod_CiOccOMccvLoMCtO13dEtP-RdO7RU5DpbWqUItU3zRjg8z4stqoc0WryWKxOEMC7RBH5q-uFCGQ6Gil0PoRMdU0AwT0xHOvVoU76zw2pG7og24JdDGLWwXnT1zGgkRPF8-zFJBUdDWLXBbNh3o8MB3ULb5AmjRIQg4LxgQVTBtDpILsz4eiZBUmwVQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از دیمارزیو: منچسترسیتی و چلسی به توافق نهایی برای انزو فرناندز دست یافتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105281" target="_blank">📅 19:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105280">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33c4f0d2a1.mp4?token=aZfu8oNY2Q5jvh9WKPde4u8C0ggyQUpQfMktc8J7m19paIEhfx0mEZV0J7YcXGyY8z1YYerj3g_UaRlUwCapN7IaL8Du5dkxOIX0Br9MQJ8GZi8hsWaaPyKR5r9Ix0-u6J7J8V9lT7kiJanW5XcDvJdrkJ9Pz2SX_wPz8qX158NuW4k6ZDBUzCt8vNFOphYZY8Q7IV5S2YZFQMaAAmpbUfO7CT7nxft029nt4wz7s_HMDjc0zaeLhwsYNSLTIYxhQCrmW0GwQP8FqCHxgUXBWZeiL1q2tnJkrzaA9TIFFg28_1Um6ztL7Sk-McWcBe24yYAbEFBK5qkwKmMxCRJ20Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33c4f0d2a1.mp4?token=aZfu8oNY2Q5jvh9WKPde4u8C0ggyQUpQfMktc8J7m19paIEhfx0mEZV0J7YcXGyY8z1YYerj3g_UaRlUwCapN7IaL8Du5dkxOIX0Br9MQJ8GZi8hsWaaPyKR5r9Ix0-u6J7J8V9lT7kiJanW5XcDvJdrkJ9Pz2SX_wPz8qX158NuW4k6ZDBUzCt8vNFOphYZY8Q7IV5S2YZFQMaAAmpbUfO7CT7nxft029nt4wz7s_HMDjc0zaeLhwsYNSLTIYxhQCrmW0GwQP8FqCHxgUXBWZeiL1q2tnJkrzaA9TIFFg28_1Um6ztL7Sk-McWcBe24yYAbEFBK5qkwKmMxCRJ20Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
🇮🇷
هوادار پرسپولیس در آستانه دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105280" target="_blank">📅 19:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105279">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKMGSYnYCHalvE4hWc4B3KOm3R6svXTgWn0OP1Kmfwu3EL5BbmuKrS_BVYsM7S5ezxzZybJyeA1uTdoihHZfdWawJSbZ4-14a8AOMhaEIaJMqFhqLFJVHQRz6wKvx7RxzWMai1mnzVjS3I12JSAOsBv9D_vFrMcBjoUze9SQkvMhmp4qYE5UTwbv9C0Mg90SBqqlGif2WaQaZExVdsBLYtJkPpRMe2sUP2kzuE_gUmosSn2c0vxLlHqDFNIXMcoEVNQfeO3NOtGFBypYKhHtPBYSQERaYnLWJpLctFqG3E12EGEfPqIWG0S15HpLSZgbUV7xr28gfv05-uOPizuJpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
پوستر باشگاه‌استقلال برای دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105279" target="_blank">📅 18:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105278">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07cf132574.mp4?token=QQfX-iZZJs6TE8XPlZG0YyBH1jwvZr8GIYwvOBXM4phfhuohhqVtzrkOZyaqIJLZ6QWzau_IB6CTcJu5-sqXSCg_24ZW4ygOY6rkEqee-L7YM0kQhORjE718IZUmT0-jJ08_2qKfSDHXWPcISvTK6rl4k9tYAd7L7kz7PAo_ULMmrerayPTYNKAfQkXzGS2WtxFD5peZnuKn5PLrSSfhkLVqCs7dP-mdOtXtSxtCE6rZ5HqE9SccQK_GHzzzge03Tyq-E73YNkCHwEFlPtgaowCO7CXAWF2BHlCdQzR8tAyPSBpNtoqQjjOdVWljpT4_deiIflhEX79_sCMeZRIl1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07cf132574.mp4?token=QQfX-iZZJs6TE8XPlZG0YyBH1jwvZr8GIYwvOBXM4phfhuohhqVtzrkOZyaqIJLZ6QWzau_IB6CTcJu5-sqXSCg_24ZW4ygOY6rkEqee-L7YM0kQhORjE718IZUmT0-jJ08_2qKfSDHXWPcISvTK6rl4k9tYAd7L7kz7PAo_ULMmrerayPTYNKAfQkXzGS2WtxFD5peZnuKn5PLrSSfhkLVqCs7dP-mdOtXtSxtCE6rZ5HqE9SccQK_GHzzzge03Tyq-E73YNkCHwEFlPtgaowCO7CXAWF2BHlCdQzR8tAyPSBpNtoqQjjOdVWljpT4_deiIflhEX79_sCMeZRIl1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105278" target="_blank">📅 18:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105277">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Khp3pq_VKrfwRO5dU17rzcQl0GSiKWFwFdH_AkRiaDBdscrKF7jhWoEaj9_TIY62iq2xYpuhLXNd9K9BBL3RCq1wn40XrKBMZvdf4TMSoAXz6miZlP18DCnUzGUj5OZhCMBaEDgXbcV0kjh29QSyI1EmcBxWxNvNHuNPwfvRsR4IYbu3aam_XpgHNYfJaZVXLMALNhRrD3gXWMVRPiZLEnyO3bX48U1KmyYfAo0107ormAnANX-eLf49yDpiCdtUL090t4W6KJZOpXeJ38mif7Nd1_rA0o_iCYkmbEGCV_KlW5wooTfFzx86Ew6kLcTMrehF-gy_x2Keq28Ov_jurg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیب تراکتور تبریز مقابل شمس‌آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105277" target="_blank">📅 18:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105276">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7b5a30f12.mp4?token=W0fRXpdAcmVOGSiYkywXGqqJW460tkp4mkZ4kiGia0xqnsBY0N3Tl333w6HFus__rz9pbXaAuQb5YCqSIgzdTPrkK_N3n6ALlUELMW3jN4ZHrLb61Tb7bYYAyRCYVF5GVeYWsk4L1Lr7Duv8x6UrYk_POingmMMtW8kQo_AkYVvoj-JJFHfUZDmf-nO-fK1guS-LsTT4QN943M6fzvdKiyIe2RmM0mu2aG1qye45zsyyPVpwbM2ts2f92DKHG8tF9VJuARaQyRv0RKXOcYXtRhHaqmjjnz1d-XUkUctymUJ5WknOR5ohqWps7kafN66F7g6vLsK5hUCsNXLTJBi35A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7b5a30f12.mp4?token=W0fRXpdAcmVOGSiYkywXGqqJW460tkp4mkZ4kiGia0xqnsBY0N3Tl333w6HFus__rz9pbXaAuQb5YCqSIgzdTPrkK_N3n6ALlUELMW3jN4ZHrLb61Tb7bYYAyRCYVF5GVeYWsk4L1Lr7Duv8x6UrYk_POingmMMtW8kQo_AkYVvoj-JJFHfUZDmf-nO-fK1guS-LsTT4QN943M6fzvdKiyIe2RmM0mu2aG1qye45zsyyPVpwbM2ts2f92DKHG8tF9VJuARaQyRv0RKXOcYXtRhHaqmjjnz1d-XUkUctymUJ5WknOR5ohqWps7kafN66F7g6vLsK5hUCsNXLTJBi35A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان‌چالش ترند این‌روزهای فضای‌مجازی
😂
❤️‍🩹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105276" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105275">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105275" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105274">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UildT_tptPHzW2Gi_2uPYx16zOEYXr6FPXo83Svbu9PkrsshHIddsbFiLU0lbhxJKPjUVZNTsHauvRz7xxHHeEk0neJ-TM8J8_B7uQ0ipyQYhwqoTNZiLum2iSE_Ze7AYe4FqTjRYc6I3auZHNQtiUuMQAXFcO5KFIVNqg2Itf-W_B1cTO315PTyBu4uoYvV1wkKAJnD4Qwv6DNtcNrV4zEUzYvG1wlCaKtXnKJ1K9o6lS9-wTufJxoKLCmSRa5UbgTW4a66SC36CdDBlsiKav9WTDw2h030QiD-2kddeVf2-x2CSwJHKmXsLYykBl9iJv6EUneTpOCsYZ3n-g1fog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105274" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105273">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9737ed01b1.mp4?token=nIrXUe95vOkCPkfY3rf3l6GvIr8pTioVZRaD8SzKcmolhFCXlTiE2Q74hc-TvLh5CYF2zG-lr8UUPpd7Tk8UKE7Y6Io4XmIvezsLgAF452cvtiL8I-_volKiYei4KaHsKFTLS52GW95xCly0A1lJWdtlirRDuPpPaOh52OpAEiYWkdNGw559V22wM5_JpIO72LRom9pDolEDrSq1iyM9ZX-bBJveFteGqg6AtvzgtEg7lsFvyN-OL1mL_anDFbjtGGB9AVRXnaZWkFpgP7R6cFGJgapmPGwLrT6CTHOE5iLKSuiqTkdPHSKPp1wdkWRsILXblZRxFcJBzO--SPRVaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9737ed01b1.mp4?token=nIrXUe95vOkCPkfY3rf3l6GvIr8pTioVZRaD8SzKcmolhFCXlTiE2Q74hc-TvLh5CYF2zG-lr8UUPpd7Tk8UKE7Y6Io4XmIvezsLgAF452cvtiL8I-_volKiYei4KaHsKFTLS52GW95xCly0A1lJWdtlirRDuPpPaOh52OpAEiYWkdNGw559V22wM5_JpIO72LRom9pDolEDrSq1iyM9ZX-bBJveFteGqg6AtvzgtEg7lsFvyN-OL1mL_anDFbjtGGB9AVRXnaZWkFpgP7R6cFGJgapmPGwLrT6CTHOE5iLKSuiqTkdPHSKPp1wdkWRsILXblZRxFcJBzO--SPRVaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⭕️
پلیس‌فتا در واکنش به صحبت‌های دیشب: به پرونده پیام صادقیان قطعا رسیدگی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105273" target="_blank">📅 17:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105272">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/273bbacf0c.mp4?token=HSXCyIKEXhW93R8QGDROSmoU-OcAnuCqjB4-VBuH_aHuG3NBgj4qH119p7roZHksn59VPKtPyl7PAWhB8rRlUR_WE_4Ts_wh5yDMZH8MOLmBre5DwL-NrMDZY_76kxsTG00RlR9QiKiBwXvGM_TeZvARydyu7RnUBPl5IY0Gezj9G77P6YVFG_ql5Zdre28lsupMOx5GCaR-GKrWUufPvhWMgIEWQervo_EiSZKMP-KwW20U44Qlxbway5DNSyXGy1UsPsU6fekGsM-nSmhBaAkwWo6GaADClTNV9nbkIJLYFBamGqOex1CQG2CvBwME4w-rlC5pxgESctCHipcOsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/273bbacf0c.mp4?token=HSXCyIKEXhW93R8QGDROSmoU-OcAnuCqjB4-VBuH_aHuG3NBgj4qH119p7roZHksn59VPKtPyl7PAWhB8rRlUR_WE_4Ts_wh5yDMZH8MOLmBre5DwL-NrMDZY_76kxsTG00RlR9QiKiBwXvGM_TeZvARydyu7RnUBPl5IY0Gezj9G77P6YVFG_ql5Zdre28lsupMOx5GCaR-GKrWUufPvhWMgIEWQervo_EiSZKMP-KwW20U44Qlxbway5DNSyXGy1UsPsU6fekGsM-nSmhBaAkwWo6GaADClTNV9nbkIJLYFBamGqOex1CQG2CvBwME4w-rlC5pxgESctCHipcOsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
تیم‌نروژ با قرار گرفتن در رده ۱۲ فیفا، بهترین رتبه سالیان اخیر خودشو کسب کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105272" target="_blank">📅 17:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105271">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb1b930efe.mp4?token=oQ6JwVyo_yf5wFgXI1-dG-96nOoCf8UT6id6BWi11JOwkcQLyAZmrGxpt3oEk5hQX8QtlrMsuwfzhtUyrc8NGjtqDcp-JeFjptF_bBwfOCAjYpVgdm6KUtYXikzu8UwPlldhidonumJ75fG3PLDD-GSd0NqACfvSOfwrkesz1tQmhUaLWcw26PExgrc9U82yfI8Wnkox-hQ7q83U6K0q0Sz80f9xpVHl3mgrFU48Cc6C2C5qCmGx7HUTu1xESv1wHidryjnH1ywiu9vqbYiIkvfwH3bNUPVWjbzSdVx7ULDK7Eo-X2KVIkixtf8nJBLYl7TfniWHqbDtWNZFUI50Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb1b930efe.mp4?token=oQ6JwVyo_yf5wFgXI1-dG-96nOoCf8UT6id6BWi11JOwkcQLyAZmrGxpt3oEk5hQX8QtlrMsuwfzhtUyrc8NGjtqDcp-JeFjptF_bBwfOCAjYpVgdm6KUtYXikzu8UwPlldhidonumJ75fG3PLDD-GSd0NqACfvSOfwrkesz1tQmhUaLWcw26PExgrc9U82yfI8Wnkox-hQ7q83U6K0q0Sz80f9xpVHl3mgrFU48Cc6C2C5qCmGx7HUTu1xESv1wHidryjnH1ywiu9vqbYiIkvfwH3bNUPVWjbzSdVx7ULDK7Eo-X2KVIkixtf8nJBLYl7TfniWHqbDtWNZFUI50Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
صحبت‌های هوادار تراکتور پیش از بازی با شمس‌آذر: ممنون از نیازمند و ایری برای گل و پاس‌گل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105271" target="_blank">📅 17:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105270">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJeBf3XPeIW5BD27QU4vALVrgHJxHwy8wdlfj2_sjbLAnBPCja3ByCDibChZeb1DRnD5D2BdmSqgB--J7ph9zbd7oGyAPvwjAyli5SZt-4rlAqFWf7SyLN7XIhgXMSq2S8OaqH5syUiZi6I43iZPC6hUeKtq7H-RXwdDFPhDpqnRFL052OMfebKNoQZwxhE7G8w46b3MUVjN4j0W7hIQffBHSs4JlgIADrXtDTVo6th4Jklgdhyfpd72y5vZOLgSWv45Jrh480WaYvq3v-4UAgw2_P-XXLZESWbAAX4tHc7rSDFmeV3mcGnvWmdAVIGyqmKT8F0a65hn8-GyxmDHIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105270" target="_blank">📅 17:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105269">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-pRGodwWKVSNTnRvPSQy4mdefE9KNv7HLqEWshHxRpsvG2uBrC5tuw2Vd-FIgEZuM3TKyr4Ej9HlYY3J8ELD25BXVW7WAd2jw-wzujm8_rQd-wQ95AaDp8jg0lv9PIE8tsChC5UBDhVLpYPmYVmDq0_hvFec_eiOi2OpWyZPmJmf37RLauPFnPkRYvKADuu-FNUzn6ah5A6Xd0InN-WiJrs9RaMe8Qd54N4mxCI8h0NB4lL3tcqsg08amo9wIcGzD6x7kLiElej12co2ooga7um92CDcX5KSm2naLrC6UFS3-COCmO3xT0FmCQRktsN8UZ-aqNOC_xc08b1k3pvdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
🇪🇸
🇪🇸
مقایسه عملکرد هانسی‌فلیک و مورینیو در تاریخ الکلاسیکو فوتبال اسپانیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105269" target="_blank">📅 16:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105268">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k--ZLYCHOQfZqmrBvzG9XWaZ2f4su35mEP53ky9zFI1PR5mGL9uxvpAc2u_8vkYcbvhDLJao-FdQc28ErnTvoA5P6y4KxP1N1k4yUM_mQWcptX_osuT2NbhBGiXfNVeC-eCaBDeaAw9t6p0EAX16wT-pwzrRen8cGsEJtn-VqewRV1f8lrqMm60IzZL3WfZTA1wQ4HUJzvmZeuL606QVQe_yJW0ljJO-mJahZyrwZvZaD7375IyNNSvRrM97WoRBEyhuV9ogcr4xB_46aohuTU_cpiSZLYzUw1oBNW5DRgKQyAIy0yWwEor-3rMJEK7Ejis1S6-YVA4evpuWUUvhxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
💥
در آخرین ماه از تابستون یه نگاهی بندازیم به بهترین فیلم‌ها از سال 2000 تا به الان که اگر فرصت دارید در این اوضاع شخمی مملکت نگاه کنید. سیو کنید بدردتون میخوره
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105268" target="_blank">📅 16:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105267">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dfdcc87e9.mp4?token=KFfYN7WlBudoba6FNWF85T8FXo8-Izhg0GjBvOLbW3GuRArzqolSoV0qlcxe-WHHQ3YpTojizWUTCsNrFB0mgopQbQBCJmpjQnr_EmL-c5hXMhoCYrZmVa0TynovJijpXJLAgxFdXHhd27DL0ofhr7JgXNDYUBRDMhDIuo_kK-U2FREQpDZVke4W5a6YHfoi1OtNc5gyx1ScsGJUthEMwoqV9oTFnestWeeyLj_9aSTEey5lKlFOqzrawzgYtY-8ddRHxRXJ1ahIdaMQWoj5nLbHAgyCbfrRz6gdj9Jw-_1RA5CRikt_fbr9VnGmf5VTvt0pnCrJT1uiO1V1_ISIqR3BdjD4dG_P55NQ6a-mGh8WZVckrOtnqC0mxx0vG2M49y6UK3rEV6b7v58j9ZInGuGV-iQiG3FVqyY46JK4btPKYxEaTIT_fjL58_dFbfxI3MPjdDBLu_smkZIoVSttY-tx5hFqyyZOupEVIpLustffLfUmwTadlUAnIOO1JuHkAXnKvt2ZeRDGEJuMcPyQqog0i-HMnaQThzRcxHNVnu_dZSI7Vi7FVVhL3aTUKjJcEj4apX4Jh1hXRQCg89DU92kGR_dKJ1YTyCZb2Iz1OHFXXQEVTYB9a604VxwSUKxhEQtiDXzglTgqmzq2Dx9xLKapFa_avERYoWYwDPVk7h4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dfdcc87e9.mp4?token=KFfYN7WlBudoba6FNWF85T8FXo8-Izhg0GjBvOLbW3GuRArzqolSoV0qlcxe-WHHQ3YpTojizWUTCsNrFB0mgopQbQBCJmpjQnr_EmL-c5hXMhoCYrZmVa0TynovJijpXJLAgxFdXHhd27DL0ofhr7JgXNDYUBRDMhDIuo_kK-U2FREQpDZVke4W5a6YHfoi1OtNc5gyx1ScsGJUthEMwoqV9oTFnestWeeyLj_9aSTEey5lKlFOqzrawzgYtY-8ddRHxRXJ1ahIdaMQWoj5nLbHAgyCbfrRz6gdj9Jw-_1RA5CRikt_fbr9VnGmf5VTvt0pnCrJT1uiO1V1_ISIqR3BdjD4dG_P55NQ6a-mGh8WZVckrOtnqC0mxx0vG2M49y6UK3rEV6b7v58j9ZInGuGV-iQiG3FVqyY46JK4btPKYxEaTIT_fjL58_dFbfxI3MPjdDBLu_smkZIoVSttY-tx5hFqyyZOupEVIpLustffLfUmwTadlUAnIOO1JuHkAXnKvt2ZeRDGEJuMcPyQqog0i-HMnaQThzRcxHNVnu_dZSI7Vi7FVVhL3aTUKjJcEj4apX4Jh1hXRQCg89DU92kGR_dKJ1YTyCZb2Iz1OHFXXQEVTYB9a604VxwSUKxhEQtiDXzglTgqmzq2Dx9xLKapFa_avERYoWYwDPVk7h4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ربات وزنه‌بردار چینی وسط مسابقات جهانی وزنه‌ خودشو رو میز داور ول داد
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105267" target="_blank">📅 16:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105266">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b94f1ee2b.mp4?token=M3ClyOzJeftskBONFlbIf-sprEBp_VQjuYnZGQPbJIFjoojb7bHER0BRctIopO0c648q7fxWFT-KicFg8dRjtE9-ZrSOmfpLe3dEm3V5oybjrw7TUCMlgxIogKAP5_vA9KfDemXF6YkU-0219j3NaLFdoGspNNe8QojtEQWKdZ22zJbInyE9c3JAjQfimXj04THU2owyLK_4Zzl52exmMMcxYf2uzg0l2pWnE2T4NJE0YG3eHoqB3R8KGzWb2csa_nTJd5Qsux22eIh0RRiu4-xAPAQEDlmG0C4CUDckqgIZCGFtnkefXg2ktRk58tF64Z0eWPIG6eRSsZqI-lDCDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b94f1ee2b.mp4?token=M3ClyOzJeftskBONFlbIf-sprEBp_VQjuYnZGQPbJIFjoojb7bHER0BRctIopO0c648q7fxWFT-KicFg8dRjtE9-ZrSOmfpLe3dEm3V5oybjrw7TUCMlgxIogKAP5_vA9KfDemXF6YkU-0219j3NaLFdoGspNNe8QojtEQWKdZ22zJbInyE9c3JAjQfimXj04THU2owyLK_4Zzl52exmMMcxYf2uzg0l2pWnE2T4NJE0YG3eHoqB3R8KGzWb2csa_nTJd5Qsux22eIh0RRiu4-xAPAQEDlmG0C4CUDckqgIZCGFtnkefXg2ktRk58tF64Z0eWPIG6eRSsZqI-lDCDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105266" target="_blank">📅 15:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105264">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38daf6a490.mp4?token=F1e3YQmQvsrnpwHIhJHvgakFzWFF5HKxM3MeDlGUwvyZZ8ktUaFjVLgyNys3hLUJk9VHPqSqL3FzqBkCadb8IfV1-lc08ejzv7GiyibSlgbA1HnE9t6W_BuwPPUJNBk6BiZN4_ae6WMMOtnUsvjQGkI5x6X0-j5qBwTzrARSg9TH_55x2ECd43RlJ8aCEL9lpt250E6n8jcDpyhSyXUM_RVhoJgzBDTF5NZJKk2yRK-HtzUnPOCEL0yjOgywDwq-kHmRMOKrc53vhElEsQ2K-bE_MADK216XVVx-YjNIN_4TXhJI8OsfL0hzBFUWmMLaux_grGAf6dUw0A-KyxIXWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38daf6a490.mp4?token=F1e3YQmQvsrnpwHIhJHvgakFzWFF5HKxM3MeDlGUwvyZZ8ktUaFjVLgyNys3hLUJk9VHPqSqL3FzqBkCadb8IfV1-lc08ejzv7GiyibSlgbA1HnE9t6W_BuwPPUJNBk6BiZN4_ae6WMMOtnUsvjQGkI5x6X0-j5qBwTzrARSg9TH_55x2ECd43RlJ8aCEL9lpt250E6n8jcDpyhSyXUM_RVhoJgzBDTF5NZJKk2yRK-HtzUnPOCEL0yjOgywDwq-kHmRMOKrc53vhElEsQ2K-bE_MADK216XVVx-YjNIN_4TXhJI8OsfL0hzBFUWmMLaux_grGAf6dUw0A-KyxIXWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
⚠️
واکنش عادل‌فردوسی‌پور به حرکات منشوری شجاع خلیل‌زاده و عارف حاجی‌عیدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105264" target="_blank">📅 15:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105263">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e1a906213.mp4?token=gi2T2BwxkFv2vsxibAvWiQhVx40iENQZZRiK9XjvlinS-W7K1c25Gv9LABpNL3d6dfsLHmWEBA9FzJDn4giMbz-75KBJMIGd-zwlQyBscmXY7vzmeQ2i4TmzMf1R0QAfgfTefxO9m5htJN6irgHzhgl_nCNJuTd0AlZSjDUX0Ly7OdRvHjZMFTZ2CPyeMCEGGCMxeMoKjYr2PJNFBc13r9oAspACwmMZoHZJZnzHLeH99gmJDSHGkx2Nf0Hz-j-fR4o-D067LQ_HQ5entSKDQXrHCndcYDsKg73Btke483tkE1FKe21bQRYMUV6KRQlGzYJutKpAMu5vNR-RsJ8DQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e1a906213.mp4?token=gi2T2BwxkFv2vsxibAvWiQhVx40iENQZZRiK9XjvlinS-W7K1c25Gv9LABpNL3d6dfsLHmWEBA9FzJDn4giMbz-75KBJMIGd-zwlQyBscmXY7vzmeQ2i4TmzMf1R0QAfgfTefxO9m5htJN6irgHzhgl_nCNJuTd0AlZSjDUX0Ly7OdRvHjZMFTZ2CPyeMCEGGCMxeMoKjYr2PJNFBc13r9oAspACwmMZoHZJZnzHLeH99gmJDSHGkx2Nf0Hz-j-fR4o-D067LQ_HQ5entSKDQXrHCndcYDsKg73Btke483tkE1FKe21bQRYMUV6KRQlGzYJutKpAMu5vNR-RsJ8DQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای دخترای جنوبِ ایران
🫶🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105263" target="_blank">📅 15:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105262">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQaoRauVo4K0j-NW-rYdC8oEYj5wUw2ROIIZQxbOS5DoiA0dDsjpGHhvswjJDSPe2wued3eVB-CcYRGPsgkfXyJDHP621MrVyx84T--Kp0CbebJolCIblF07lAqAK_ickcX2Tke5RYnQEGtIRaAT45PDUkoFA0UDthomyn86bvc7cdHwvqZz7qajdtK6ynJo4UoDrfepKCAIBsTUTLUKcUq-g3McdSM-ZbPZxMr21SAuVxmJjm6YZqovGRnsQDW8Eqb9aoYYbddc2SSwKwPp26bHOMlnvlfF8i3mXUSa_RiVXoUknGXYLljYyRwzWlQWjemorPaaWgOkMz_C__gY5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇮🇷
هوادار بانوی تیم‌فوتبال تراکتور تبریز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105262" target="_blank">📅 14:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105261">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93b254714.mp4?token=qJY06dum20Q9EXFwJWOTdraTnOMn95GKf39bGZqmj6pOInUfl051o5jpVUMh6H8nHizoxAtMicgBClo9p88sHaiJFQgRnS3sEjS7eViFz4akjb8vSrrUeq0UqfKGKhkWfTkmuhhbixA4R23nYEQSRxTa1hhutOHALn5ioY3fQ0fC-5F0KabG10XnEA7nsCpgCMtvK4R9AwA0pcEzKdinHSVa4O4D3-d-ioeC_iikkrHnLuJHj9P0rn7EARZtEyAAy8by_bfkzT2Zze9U57WNBI5l1M4UgHmtxZA45hPIKRE6fWLkZDSwc93ENE2SFLhlNfLF5vVEDQMKKB_Cpra3Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93b254714.mp4?token=qJY06dum20Q9EXFwJWOTdraTnOMn95GKf39bGZqmj6pOInUfl051o5jpVUMh6H8nHizoxAtMicgBClo9p88sHaiJFQgRnS3sEjS7eViFz4akjb8vSrrUeq0UqfKGKhkWfTkmuhhbixA4R23nYEQSRxTa1hhutOHALn5ioY3fQ0fC-5F0KabG10XnEA7nsCpgCMtvK4R9AwA0pcEzKdinHSVa4O4D3-d-ioeC_iikkrHnLuJHj9P0rn7EARZtEyAAy8by_bfkzT2Zze9U57WNBI5l1M4UgHmtxZA45hPIKRE6fWLkZDSwc93ENE2SFLhlNfLF5vVEDQMKKB_Cpra3Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
بدون‌شرح‌ترین‌ویدیو امروز...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105261" target="_blank">📅 14:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105260">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411e9bcdcb.mp4?token=QqegKNDC4LahwtaOTqDkt6CuB9rEKaw8DzXWpSZaoTr-hPKx7fMFAupVS7eMcNXn0fempq-3BYjy3Kwvkk1vXDjLL2-GxUeM-By-k0B2YEaRdlJE2q44aZvsctFyd3nRtKIh4Eu6atIsMswN7ri7RJfcD1Is-qfqadqVC4AB4w7yAjKrIgHBa0F-IheBWbukeHdi-l9yUHrCWtz9Y1W2FYEZOxbMOjEF_1wZ1kP6g4NM0c2KKCfdqODQvv3nP8hdJYgXOjgyYqmb3YrXX7l4NAdjzRocg_zS4Gq7S37r4-CYlKwUZA5A3Yo3PFC5zaKlPoRsYPZmPZ-nrEelZrQIhHXnXERrRIgPTwg_DdNzHdMKt5RRVZ8URFpGJc7Ka8LsdNC6VUwzmHUdD4jAqZrrwyjeJsay6SLkArrtzuRiEqzUD0jOKkwtPUlvHk9c5aWVDoFcQEJcFvotzWnWvzLpIFhkDRYvHMwfz59G0W9WFy5oYHYhRS38I6DeYmWF-yHlvFwmtWyyh2RycLlwdvw5Pk4NLMPJksa21aWzIfC8pYbM8rkarch4Z1vtXYeNIEsfXOqkpZQ8npcP7zIlcNRyitgRffoyK2S3Ae9PJgj2l5kzz5perNXyf0m-Ol8lJkaJXgQw6EmNqlEcVU99QG245Vl1wZ3419K2_v987hxymME" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411e9bcdcb.mp4?token=QqegKNDC4LahwtaOTqDkt6CuB9rEKaw8DzXWpSZaoTr-hPKx7fMFAupVS7eMcNXn0fempq-3BYjy3Kwvkk1vXDjLL2-GxUeM-By-k0B2YEaRdlJE2q44aZvsctFyd3nRtKIh4Eu6atIsMswN7ri7RJfcD1Is-qfqadqVC4AB4w7yAjKrIgHBa0F-IheBWbukeHdi-l9yUHrCWtz9Y1W2FYEZOxbMOjEF_1wZ1kP6g4NM0c2KKCfdqODQvv3nP8hdJYgXOjgyYqmb3YrXX7l4NAdjzRocg_zS4Gq7S37r4-CYlKwUZA5A3Yo3PFC5zaKlPoRsYPZmPZ-nrEelZrQIhHXnXERrRIgPTwg_DdNzHdMKt5RRVZ8URFpGJc7Ka8LsdNC6VUwzmHUdD4jAqZrrwyjeJsay6SLkArrtzuRiEqzUD0jOKkwtPUlvHk9c5aWVDoFcQEJcFvotzWnWvzLpIFhkDRYvHMwfz59G0W9WFy5oYHYhRS38I6DeYmWF-yHlvFwmtWyyh2RycLlwdvw5Pk4NLMPJksa21aWzIfC8pYbM8rkarch4Z1vtXYeNIEsfXOqkpZQ8npcP7zIlcNRyitgRffoyK2S3Ae9PJgj2l5kzz5perNXyf0m-Ol8lJkaJXgQw6EmNqlEcVU99QG245Vl1wZ3419K2_v987hxymME" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇪🇸
دیشب‌کریم‌آدیمی بنده‌خدا فکر کرد چون ۱۰ دقیقه تو زمین بازی کرده دیگه بعد بازی نباید تمرین کنه که دستیار فلیک این‌شکلی کاسه‌کوزشو میشکنه و دور تا دور نیوکمپ کنار نفرات ذخیره تمرینش میده
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105260" target="_blank">📅 14:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105259">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c284d93a.mp4?token=gAT5zIymHvinBM6ab6AUCagUT1FP5wl6Lc3MNZHqez7goFvJ989-q-zJjfx-RnfnCktL1qEpcZCbhlRh25vR37H7OdsGqDvbHVspxBBOYBhPRcqBlgU8WCEGMrx90IikwqgfV90TzerHT-somTmKAgxdoKsPr1lZvXswj6LgazjMoMDEU2uneEAMky3r0ciJsYOgugyRk81O7k8T6YTcGKHbFBKc-Hd7gymwnc1QnlHC9oOBZ_oXA8v1XQI48wF92lsE0FSa82I-eS_gczRAkACaJsjSENm0CtZycQmXyWh3i9nGExGU14gFNKry_7esUGOft-Kv4TxZ-ROMa4ptrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c284d93a.mp4?token=gAT5zIymHvinBM6ab6AUCagUT1FP5wl6Lc3MNZHqez7goFvJ989-q-zJjfx-RnfnCktL1qEpcZCbhlRh25vR37H7OdsGqDvbHVspxBBOYBhPRcqBlgU8WCEGMrx90IikwqgfV90TzerHT-somTmKAgxdoKsPr1lZvXswj6LgazjMoMDEU2uneEAMky3r0ciJsYOgugyRk81O7k8T6YTcGKHbFBKc-Hd7gymwnc1QnlHC9oOBZ_oXA8v1XQI48wF92lsE0FSa82I-eS_gczRAkACaJsjSENm0CtZycQmXyWh3i9nGExGU14gFNKry_7esUGOft-Kv4TxZ-ROMa4ptrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
عملکرد پشم‌ریزون دیشب لامین‌یامال برای بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105259" target="_blank">📅 13:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105258">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4862134a1c.mp4?token=a2I255fUoOsU8Qn8l34AeKCwWJ-TM_p21IKEbxEvenRaLevBpig2ncMjXhEMJLrPrjqdRgF5qByymPyuRLwA2AbND0PANuT85QlOGicUSUqbnv005SBb_G53_TN7KMQny9jUazc1219uxfXNISwj0_hkBZVPNZw9mTb1xVrfb5Vk7VzpaDtISZyx_OJQlN3ODbeApNDXsj8Ih35NwKCe9rmPx7k-WRyIAhVUofcgezgPwOI7uLNbUuKMFXdXK_Mdc5RLBOYmLhqg1Xr2935YpSiAnUQjKJlpDqmm_yydoxJh5bIN0tW9iyYxp-_e0ReFXpquRohcyM0-0MHVLkE0MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4862134a1c.mp4?token=a2I255fUoOsU8Qn8l34AeKCwWJ-TM_p21IKEbxEvenRaLevBpig2ncMjXhEMJLrPrjqdRgF5qByymPyuRLwA2AbND0PANuT85QlOGicUSUqbnv005SBb_G53_TN7KMQny9jUazc1219uxfXNISwj0_hkBZVPNZw9mTb1xVrfb5Vk7VzpaDtISZyx_OJQlN3ODbeApNDXsj8Ih35NwKCe9rmPx7k-WRyIAhVUofcgezgPwOI7uLNbUuKMFXdXK_Mdc5RLBOYmLhqg1Xr2935YpSiAnUQjKJlpDqmm_yydoxJh5bIN0tW9iyYxp-_e0ReFXpquRohcyM0-0MHVLkE0MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
محسن نامجو مرتیکه دلقک در کنسرت نیویورک، شانزده شهریور سال ۱۳۹۲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105258" target="_blank">📅 12:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105257">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از دیمارزیو: منچسترسیتی و چلسی به توافق نهایی برای انزو فرناندز دست یافتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/105257" target="_blank">📅 12:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105256">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/950b2c8673.mp4?token=JkmdURWKEvLr3JedaVUGZKxzp-gvRfrZtCCDVrcfeY8NVI5_Vo4AkDccVA4_Oa2wox-f1uFvM-IG6m39lJZ-JVAFXgsta0N13VUqoVw3ljDCn_A8HusrTF77jB14d8Fsa8v2wE07RAEYfN3pI2XBoTK5BmrpuKPNhhxFyncInWrcbKTRUaQyrpNi2y2CRBLrObQWZLcGnjKAHrSJTwg23t6OAtkqIJyk2tTLgiZrReiwboL7DXegGjveWs3U2HMIHJManOr_IJJEvfD7AA9jH6Uw4_h-jUPlrk1_lwib6QzDaOyHsC0XbxMDkzdBVna3H04kCeO48xDR5aFGuy_s1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/950b2c8673.mp4?token=JkmdURWKEvLr3JedaVUGZKxzp-gvRfrZtCCDVrcfeY8NVI5_Vo4AkDccVA4_Oa2wox-f1uFvM-IG6m39lJZ-JVAFXgsta0N13VUqoVw3ljDCn_A8HusrTF77jB14d8Fsa8v2wE07RAEYfN3pI2XBoTK5BmrpuKPNhhxFyncInWrcbKTRUaQyrpNi2y2CRBLrObQWZLcGnjKAHrSJTwg23t6OAtkqIJyk2tTLgiZrReiwboL7DXegGjveWs3U2HMIHJManOr_IJJEvfD7AA9jH6Uw4_h-jUPlrk1_lwib6QzDaOyHsC0XbxMDkzdBVna3H04kCeO48xDR5aFGuy_s1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
مجتبی‌پوربخش: تا جایی که اطلاع دارم، وضعیت جسمی علی‌کریمی خوب است، فشاری بر او وجود ندارد و صفحه شخصی‌اش نیز در اختیار خودش است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105256" target="_blank">📅 12:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105255">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A75H27qThID5b6jI7w2vyo0UC3k51aziyApaCiQLmr5VI8Rhro4zHl_KMnW1-PdgM7u22CYCfqXY5C4I5UOzdciIhwZwV9nP5Ccy6IxOgmuu0qlqfs0wN8PnCMckwkeMnfvXCltn6Qum2fcndRfXHEPYspBMlA3NYIvjMvgPtbuxaiyCoHmUjkvwjaPie48oYPhL4XlUZ3jYKVE_4kKNjfhnrWnHzFS15WR25eqt_kZkWiwKSc_a9MmcIYQ05djSUvsfjD21Knxb3AUqp25LZhEUiCzqtaY_ezre42r7gIhfsrmESPkZVRa9dMFU_yXwjg7Y4a3bsDXd81QopH2How.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
نتایج سه‌بازی ابتدایی بارسا و رئال در لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105255" target="_blank">📅 12:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105254">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f53a6fd8f.mp4?token=a_PtEMLeZEGfx1oR5eqi4qlaeKZyvP_EUl6sFFcae0teJzpkhdFCcpHEnv09xQyeLgpLRdQ0EC7npgJEyjFYNy_uZorX1VfyNnDsFowe7r0fqaYgHD0D9RBtwFq3mPzaKlOCzE3VaFWoYgFLKQJF7PHB3U0oPxaQjaRn7MB1eoDJqXEuWxbGpjvPf1A0aNIc-WVO8uA1ApXOF1K9GfM0Qaw-kHroKQeI8IP8VgFvdoNYObG1i_TyM7m1O23XOZpcc2KSR07wb8nzD1v_Hud5xzbqc4t0AZdiXl77t-mZUccmtW9r-MnPc2Joem6w0dOIhrer-9wGDeHkQRUBYaaLsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f53a6fd8f.mp4?token=a_PtEMLeZEGfx1oR5eqi4qlaeKZyvP_EUl6sFFcae0teJzpkhdFCcpHEnv09xQyeLgpLRdQ0EC7npgJEyjFYNy_uZorX1VfyNnDsFowe7r0fqaYgHD0D9RBtwFq3mPzaKlOCzE3VaFWoYgFLKQJF7PHB3U0oPxaQjaRn7MB1eoDJqXEuWxbGpjvPf1A0aNIc-WVO8uA1ApXOF1K9GfM0Qaw-kHroKQeI8IP8VgFvdoNYObG1i_TyM7m1O23XOZpcc2KSR07wb8nzD1v_Hud5xzbqc4t0AZdiXl77t-mZUccmtW9r-MnPc2Joem6w0dOIhrer-9wGDeHkQRUBYaaLsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
ویدیو زیبای و دیدنی حمید سحری پس از اعلام خبر خداحافظی اسطوره لیونل‌مسی از تیم‌ آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105254" target="_blank">📅 11:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105253">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105253" target="_blank">📅 11:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105252">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoH8zuCmZV4by9_YSG-YNgoKB8zl1IBVxHEtIU6LbMrwQHhjFwkLvmKW0ch2eLMvkQpqdlW-CWPdGFMlriwbe8ij3E7Jfhjd4SBMRv_qxRc4xkc24jEd_q1vPcOLsFcsjciURctm8QgcDC_Yc09Fi_RtJ7o4phbbbEWeoGGoBU-Uycai_HbLLCw7m-LF_2gTkQgePyj4FVzyfaWe28H4hwU2_a1RIzQjHMK4jdCzjhnQ5RI8yOndJpf5RbqprxnNSb6MThCD1eBJg7eLhnEF7NjF0f2JquvlX9W5QBLbWF3ABpev4Uujpf0qnPBTM3OMuImHyroA807K9RiYQ7apIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105252" target="_blank">📅 11:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105251">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f62060bab.mp4?token=mInF3jRyBXAqZrnSeiEi25qry539Ju6cakJlBcc7JP30iUJiaXMVSl95kEo9jKT13Yr-f3phv8sIGalb-pvPInxHmNXFlt_sjiz9RJaHFXMyW-ydopx0fPhfDdzajszVaF8hxig9pFiN4yviFKZuZv-JcLaL_Efl6tYofBRrGYqnmXcRfKbiwvkOufJfDshQlqKwnyrGhH4x8skwX908LnzMrOC4xnHakjRmiufWXL5it1jukuMt_sKJs7Zyykj8IMEjecWSXNqOtMZ-NubG2-xdYO_qdLqCv9oFRMnsFYyjrbV6xtY2jfrsrpO0yrTaAzQxZyTbVFtVusQYHSLvHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f62060bab.mp4?token=mInF3jRyBXAqZrnSeiEi25qry539Ju6cakJlBcc7JP30iUJiaXMVSl95kEo9jKT13Yr-f3phv8sIGalb-pvPInxHmNXFlt_sjiz9RJaHFXMyW-ydopx0fPhfDdzajszVaF8hxig9pFiN4yviFKZuZv-JcLaL_Efl6tYofBRrGYqnmXcRfKbiwvkOufJfDshQlqKwnyrGhH4x8skwX908LnzMrOC4xnHakjRmiufWXL5it1jukuMt_sKJs7Zyykj8IMEjecWSXNqOtMZ-NubG2-xdYO_qdLqCv9oFRMnsFYyjrbV6xtY2jfrsrpO0yrTaAzQxZyTbVFtVusQYHSLvHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
🇮🇷
فرشید باقری: خداروشکر به پرسپولیس نرفتم؛ آبم با آنها تو یک جوی نمی‌رود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105251" target="_blank">📅 11:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105250">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbad291eb3.mp4?token=PyCKhcOGKQnEJdrGAHT2pQLSU4z26iXOl6VUf25RKMyjNtp_32PaTWTB2bYVPNZhhgOFTQRikpW4B7EhgQRfRyx_iX76juuBBw-nfl6shfWqwQF-oc5-IXF2hef5L5qsmXpJYKL2Hze6slTqQsCoyew2gErOc-28ZBzxIGHQCfqDVIWkBLKuPp5ly4RVxMyab82hDkQl4VGuw5KBNAkXuwNXDACEAFKCXby96hVSZJHuZORE8MIgto30mFk8uhRroXfNjRJFDOulE1TKEJgPbQQcD3wEwkDTrJ6t7VNytbPl1gRPK4I2bJ3viwozqfRoo3CYXFQbP7eaKFyC-2zeLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbad291eb3.mp4?token=PyCKhcOGKQnEJdrGAHT2pQLSU4z26iXOl6VUf25RKMyjNtp_32PaTWTB2bYVPNZhhgOFTQRikpW4B7EhgQRfRyx_iX76juuBBw-nfl6shfWqwQF-oc5-IXF2hef5L5qsmXpJYKL2Hze6slTqQsCoyew2gErOc-28ZBzxIGHQCfqDVIWkBLKuPp5ly4RVxMyab82hDkQl4VGuw5KBNAkXuwNXDACEAFKCXby96hVSZJHuZORE8MIgto30mFk8uhRroXfNjRJFDOulE1TKEJgPbQQcD3wEwkDTrJ6t7VNytbPl1gRPK4I2bJ3viwozqfRoo3CYXFQbP7eaKFyC-2zeLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
🏴󠁧󠁢󠁥󠁮󠁧󠁿
وضعیت سخت‌افزاری ورزشگاه اولدترافورد که وسط بازی از سقف ورزشگاه آب میچکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105250" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105249">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWj9QnMvhqh5kqOfLgunyD2SnyKg9S9UhIRhEW4Ekv-wkzcUwJZuH3opXWKyrakANI5JoVwybkGDqU4EUDLsHDFFQi2NzWYbknAULH5jxiFV0aA4xUY64Y6ax4imJzf_46_CeddX4Y7BWK6KC_BhClR0tzHfmaZocOclJdnS8So8kmKt3v4Xbo12J031cxxUOKK2sUWO_Q1TnZIiMmS1UvxKM3UOXWR3scIMBc6Ae4bXsyXyC7lvphSUPgUkLacPUIsyxa8OuG_lk6QhB7CLHHcEX-cTIn2h85_OHOyo0XilYScLf-3sQpgUtU25u6KKFaMAmoy9m5aox3ut4fvpWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
پوستر باشگاه‌استقلال برای دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105249" target="_blank">📅 10:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105248">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a276b65ea.mp4?token=B9Zhef5ZXKFttJGwcsD318tvLvgllDy1RoiS8ylh4rvaqabS8lhiDzjaV7qpWh1vdc9Ns06-6lOfzw1bbztSM5qRbN32EMK9Q2e9ZI1-T3NwKXRa5ceF7AEDAL7dBWD5fUc9VH5cQUO0t6k7jm-MZTwXDWsm1FJX5wxA4uC8oe_vFC9jNOjKukU7JNv6ThtiAdnsLXl4qyCTOYtttfWi4TyiOlfs0MqSsVGZObNj3ybntLAC35Zt3kZMZ5iH7SU3fP3sJP5MBiiCqeEIbIkM6q-VemDYOE6cjdOgAiGJKRF-m6ExOK1JhRiEQopJOsciXccUOf7d54SPruUWqUH62A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a276b65ea.mp4?token=B9Zhef5ZXKFttJGwcsD318tvLvgllDy1RoiS8ylh4rvaqabS8lhiDzjaV7qpWh1vdc9Ns06-6lOfzw1bbztSM5qRbN32EMK9Q2e9ZI1-T3NwKXRa5ceF7AEDAL7dBWD5fUc9VH5cQUO0t6k7jm-MZTwXDWsm1FJX5wxA4uC8oe_vFC9jNOjKukU7JNv6ThtiAdnsLXl4qyCTOYtttfWi4TyiOlfs0MqSsVGZObNj3ybntLAC35Zt3kZMZ5iH7SU3fP3sJP5MBiiCqeEIbIkM6q-VemDYOE6cjdOgAiGJKRF-m6ExOK1JhRiEQopJOsciXccUOf7d54SPruUWqUH62A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
افشاگری شب‌گذشته داشعلی‌منصوریان از فساد شدید در ساختار فوتبال عراق
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105248" target="_blank">📅 10:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105247">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5E2P3sxPzX5WOX7txyfmLmOd92ZfpnijenHdDqiHsjaqt5hhvFQfuJuiAfSj9MoamWJdbPStpaRnttuZHDLIz6ngasO0tpHE-S8YkorUYojXx47BInLZmccwL4_miuel2bT8SwYRH-3sWMK4VSoZljnCMFs3G3Rd5GFVLDXp7UzV1yl7NnQM6Xqhi4ajhoZvyEHZikhKiqASinG7XtD7x1yUxmXRiWdBHIZSW8XldbFOW_VIZKHbr4kjmbLzu1lBP1cjmvcioU4q6CmRdr8T-ObBlKg4DHpq6iclUx8LSsIGg2J-mHQROTxrAhCFTysx2_3eZ7NsTpaldCJG90UXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
با حکم کمیته انضباطی، شکایت دو تیم سپاهان و مس‌شهربابک از استقلال بابت بازی غیرقانونی یاسر‌آسانی مردود شد و این بازیکن مشکلی برای همراهی استقلال ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/105247" target="_blank">📅 10:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105246">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1b1a2663.mp4?token=lL4OVQJCKKhPMYfHWAUF4tWilvjSjhMyTyj7LiPPJm6dqvH9WziOLDwNEoo-P8cTVzgt0dCBUV51Gy_SKRX3s3_TZqw6vEbZC-SMgO8qeiA7vUnZoeuRfQUpGnNIlwG4ADyfEHyMZUvdm0lgFgUSPG3azsF8i13jQTbSMzTH-xNElbSNKcQkZOS5THavRXa94r1Q1kyYDub-OGm1WUpsBI-SNXCB87YB8zbfE7YteSkxq3Jg6QOqIZmDQtPo_E6vDr8rS-R8_GEC7AgTtjPjVPfUPpPh2SzIpsnXRgjakFoIx6i6-BiWjnm8u5cLXYyBihLTyxk66uJ96p-da9P0MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1b1a2663.mp4?token=lL4OVQJCKKhPMYfHWAUF4tWilvjSjhMyTyj7LiPPJm6dqvH9WziOLDwNEoo-P8cTVzgt0dCBUV51Gy_SKRX3s3_TZqw6vEbZC-SMgO8qeiA7vUnZoeuRfQUpGnNIlwG4ADyfEHyMZUvdm0lgFgUSPG3azsF8i13jQTbSMzTH-xNElbSNKcQkZOS5THavRXa94r1Q1kyYDub-OGm1WUpsBI-SNXCB87YB8zbfE7YteSkxq3Jg6QOqIZmDQtPo_E6vDr8rS-R8_GEC7AgTtjPjVPfUPpPh2SzIpsnXRgjakFoIx6i6-BiWjnm8u5cLXYyBihLTyxk66uJ96p-da9P0MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/105246" target="_blank">📅 09:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105245">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31f95056c4.mp4?token=upTN0nfG4NSs_bZqMvnbiGGbvT1CjyQlgDSc6n2N8izE6T8KPb7S8D8-x1L9bdqcNa49B6Km9aCjHc9r1J4iCgKjA2TgzujadBbWD_3_jH_6qb_gR3t8_KCQF1MWwvYp9cEIsS9PyKs3CrO6bvLoyV--8kJ-QtES6e9oAx4EiRTA5bjeYGoIMEnm_H9pitc7-3MdLoy8Znh2Fv1dyfoUqwUZ4KRulonVQOab3GWA0oGMOX30jukCMUfgoc6hDbaAEiLcfpVs0u9QKyMyOutKUgIph9zApEPL--SPUTAVk5e4Gv96ufc358z9A-jzTW9gZq-xHC0KXWKxWCPMn-PN6Zcrph7Y-d19-OUgUmRI0XzvjVyZBh-7hB6OiRNrUvA6050WAdv-89Fd8oKZCfn6h2Q4kSnEsg8QRFelZNiLB2UMXLeKDoFyEj3UR5AogZWqPeQDrSlegFCpOvttAf4T6nDvi5xEsg3V8rG5oIENJy42bXRPCa0zFJPR3Ku68zj-V0nMhbv-q022OWtJZizU-KI9VOCp0Nx7dA-7XhziuEuaKY7vlbCfTKVbZk-rHQxYR0krgHwOGK9j-muCoF4KwoyeHIzR815Rn0To42sGEXe9ImOn2sjwlWYXHz8ghAVX7zy_q20e4ZX9KliirjKDEEAkU-Q1tFCIqM_HEJUqKVI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31f95056c4.mp4?token=upTN0nfG4NSs_bZqMvnbiGGbvT1CjyQlgDSc6n2N8izE6T8KPb7S8D8-x1L9bdqcNa49B6Km9aCjHc9r1J4iCgKjA2TgzujadBbWD_3_jH_6qb_gR3t8_KCQF1MWwvYp9cEIsS9PyKs3CrO6bvLoyV--8kJ-QtES6e9oAx4EiRTA5bjeYGoIMEnm_H9pitc7-3MdLoy8Znh2Fv1dyfoUqwUZ4KRulonVQOab3GWA0oGMOX30jukCMUfgoc6hDbaAEiLcfpVs0u9QKyMyOutKUgIph9zApEPL--SPUTAVk5e4Gv96ufc358z9A-jzTW9gZq-xHC0KXWKxWCPMn-PN6Zcrph7Y-d19-OUgUmRI0XzvjVyZBh-7hB6OiRNrUvA6050WAdv-89Fd8oKZCfn6h2Q4kSnEsg8QRFelZNiLB2UMXLeKDoFyEj3UR5AogZWqPeQDrSlegFCpOvttAf4T6nDvi5xEsg3V8rG5oIENJy42bXRPCa0zFJPR3Ku68zj-V0nMhbv-q022OWtJZizU-KI9VOCp0Nx7dA-7XhziuEuaKY7vlbCfTKVbZk-rHQxYR0krgHwOGK9j-muCoF4KwoyeHIzR815Rn0To42sGEXe9ImOn2sjwlWYXHz8ghAVX7zy_q20e4ZX9KliirjKDEEAkU-Q1tFCIqM_HEJUqKVI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚪️
افشاگری پشم‌ریزون عادل فردوسی‌پور از ریخت و پاش چند صد هزار یورویی مسئولان تیم‌ملی جوانان و امید در اردوی ترکیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/105245" target="_blank">📅 09:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105244">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b5c71afe0.mp4?token=HGnqHQX-ws7poQC5l7zciV1xhomex6cbG83PpCtsZmVAMoVFY0YtJdGyIunbmRdoqcSMVYFjlnqrhaA16bEy2SM-6SUhhjBG_ROq6ycrB5VZGZ-10lMAVDOs2lIR9Rqgb5VJpw3xbJ8FXCPPt9uhsTatFjO0o3EYpTz4JZHzwzxb86gQqQp8KPT33DngGLZVOpSpEjDX6TmKRADY2XadsBdDfuPiWkizfKIJnRBaT0T6sW4TCFXCI5QjLLlarg9wfSR67udEOBNDDLSEgyPWK-cpzxWIvY3LcQsREA5IVfhDafRPRWdq5k1Gu5jX5mYzXeVD9gD1OMR3wcR_Hg1CHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b5c71afe0.mp4?token=HGnqHQX-ws7poQC5l7zciV1xhomex6cbG83PpCtsZmVAMoVFY0YtJdGyIunbmRdoqcSMVYFjlnqrhaA16bEy2SM-6SUhhjBG_ROq6ycrB5VZGZ-10lMAVDOs2lIR9Rqgb5VJpw3xbJ8FXCPPt9uhsTatFjO0o3EYpTz4JZHzwzxb86gQqQp8KPT33DngGLZVOpSpEjDX6TmKRADY2XadsBdDfuPiWkizfKIJnRBaT0T6sW4TCFXCI5QjLLlarg9wfSR67udEOBNDDLSEgyPWK-cpzxWIvY3LcQsREA5IVfhDafRPRWdq5k1Gu5jX5mYzXeVD9gD1OMR3wcR_Hg1CHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو خواهر پژمان‌جمشیدی از برادرش در بدو ورود به کشور کانادا پس از رفع مشکل ممنوع‌الخروج بودنش بابت پرونده اتهام به تجاوز !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/105244" target="_blank">📅 09:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105242">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fa9c53173.mp4?token=gUnsNEfiqnTsLP9ttKgoCv4QxQideVUpXQzXC7DCC7xvesGFxKYS5o5yz4lsWIYWNurq7Wg4qlZq2EIyk2tuqRkIr6ezQ6yD-ES-5SVC_zMNn7bxLWw9yKmb5ObAQ7EtCB3bzB46w_j-p3RT27891Gm5ATv0wv1878xRYFrEX_ytytU1_Lr66tPqWvnqHK81T8WppnMksCBZFtf6LH0Zt2NWSZiW_mUUD9gyCWiUO9R_xXjEXvbzqICQcHDn8pM0O2-duFq3ewgjXI9XxUI-6cDctJINT9kWiNIeV_uU0rbm3rV7n3-Ss6onAT5cBRAdm2AirQ5vbXCxsiDEBB2DAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fa9c53173.mp4?token=gUnsNEfiqnTsLP9ttKgoCv4QxQideVUpXQzXC7DCC7xvesGFxKYS5o5yz4lsWIYWNurq7Wg4qlZq2EIyk2tuqRkIr6ezQ6yD-ES-5SVC_zMNn7bxLWw9yKmb5ObAQ7EtCB3bzB46w_j-p3RT27891Gm5ATv0wv1878xRYFrEX_ytytU1_Lr66tPqWvnqHK81T8WppnMksCBZFtf6LH0Zt2NWSZiW_mUUD9gyCWiUO9R_xXjEXvbzqICQcHDn8pM0O2-duFq3ewgjXI9XxUI-6cDctJINT9kWiNIeV_uU0rbm3rV7n3-Ss6onAT5cBRAdm2AirQ5vbXCxsiDEBB2DAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های عادل فردوسی‌پور در اولین برنامه فصل‌جدیدش پس از حواشی فیلتر شدن سایتش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/105242" target="_blank">📅 08:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105238">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKz_5XqpDCjIJJUKGPKJz4ADpsiUx2_AET_YEwP6EIXT_Jk6XWx1Zs89xgKt9PVjmZ0kqrVVbvYday4hNxwsxdWXafMpEZQ3nT5TA36nnyMo_8mm53cYSxpZjHY_kiZfbGz1rqDV_Gs_sup44SCo88vw0QioOLV73ABHuUaJMTh9d6cIKTZNuDh0Hl5GOfs8Ny5-I5ixprdJh8OanurNkBp3T43sb-C8Efpx4JTWmPAW2GTF89sEsJNmmerKxtCPj-mJ7p-6JORD4I4EenOUIT7RgBUovPo6_pYXYtQIumZqsIdPwdbha6niMHSiiH7upEs7NxYqfwyPb4JSfcJaQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلیك: 91 پیروزی در 120 مسابقه با بارسا.
🥶
ژاوی: 91 پیروزی در 143 مسابقه
با بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/105238" target="_blank">📅 01:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105237">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCH6BAaGV49CHrFD_9crH0DcO0QXl5BvNEJYWX7hi3kZunVy289i2915lHuHukFjfefQUA-f8KTHNtQOHfh0UGulF6NWvUmeAJlIaU5BZ0XydEEkr39d3icJpjN1NzfgMP6u-4Jrs5pp2mOvpdGYf4SzbkPB5snosCdaXn6oVuAa8IQTEjMLImlbxFrpHoCKjjgV8K1AWJrpxDqIgr_EsKVIvpq8R6uEsx0RLhOf_3r_B-XrTnXiP1YwhNLEBPoiEN34tqJJOlbLsNoPrtEWOkSK1Tj3p83J0lcvJDJP0qi4tsXhS8CUo1V6OH2iHCcVdDtK4LcJzfvTQZmhSI53HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: مودریک از چلسی به تاتنهام با قراردادی قرضی HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105237" target="_blank">📅 01:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105236">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkTsYUHePVXz3nS5Q5VM-pOSNuxW_ncQGHlQTT2YF7ZRHn-N14WvBTtfz_rh-DBqA9953elCXMrNRVqqplPEXN2275ZesRF0GSl86WbhPB_aTyP_BhyUwc5TUuKTerh_YnS31QaH724444mC4AEguD8qP3hpi-rpOajkAwhZO9EMtBEpXh_SzrLwH0MTa0bXGXQDGW3GFlNYzZP81pSMILxzkbxiLzNVDu1-wZ4oVJ861sqvPlsSSJ4ub-wHlM3pdHmAcs8BbrEjSiGk6XdIkcSwkQkUctlxb67lPhNrvjdVmDcSjgpViqV4gMgkuNVZDAFAwN23VI4N0E5s7_NQiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105236" target="_blank">📅 01:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105235">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">لامین‌یامال دبل کرددددد</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105235" target="_blank">📅 00:55 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
