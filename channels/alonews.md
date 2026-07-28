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
<img src="https://cdn4.telesco.pe/file/NN4HfmiDHW0sqdnzSg7OUi4qHOzjbIdiVVC_KKl3ycV5uKohRGQ9O2m4FnlHP_x8PWY6wNz1m2xFs3IiwlRVrazdN256QAxqVpP2VhLgLoBZ9YehYMVfNFp8_EYGjNmrSzO0fXN6e7pQUr4D_GMvoAtrpNQ_jNhKr3T7oBlDA3QHzGqLgoRU9zwH45RKTlopK5AlbRE_trmUvGH-zD39t1eHNTjKGBLhUTH3KyFCjCVm8yIwJNQZ0TAY6P2TLVc7qZ0ZtZvQk1lnMeaGXod6v7XfOIruruDk3REBXePd5iSLyRAzWqXSJLDwB_L0zz3XrEHbn3iK2OQK3TxYG5RIxg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 971K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 05:27:46</div>
<hr>

<div class="tg-post" id="msg-138045">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2b428aa9.mp4?token=TorzfqWx6u7zKnUvP3RXY86ULk-D4omvgFFfZ08Y6kY_vch7DgknM0-PmHD1mgDzIOc1--4Ue9TjeHAUuGOZoS7yoUJK3vXJrGnWcwLw9i_kZQjW9-bkk2DGy9tacOg4aawn-Nl3LqJ05GeEGvbqNKxums1AIRTyZmygkTGknt4YAIQbwZpgste16LqfG333-WcgHs-DyJ218IBwdMtPsPfPDyPYzYEipgqdwqKN41AvdFvnjQIplAlRqeLgVEgOOw2kP10xhGrBtlP7nYHkdk9RRSw7qyu-GDDodfl_5t-YjFp5xqw6ddvhBxjSFU64yE5FOVakW8uHbVE89ahtEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2b428aa9.mp4?token=TorzfqWx6u7zKnUvP3RXY86ULk-D4omvgFFfZ08Y6kY_vch7DgknM0-PmHD1mgDzIOc1--4Ue9TjeHAUuGOZoS7yoUJK3vXJrGnWcwLw9i_kZQjW9-bkk2DGy9tacOg4aawn-Nl3LqJ05GeEGvbqNKxums1AIRTyZmygkTGknt4YAIQbwZpgste16LqfG333-WcgHs-DyJ218IBwdMtPsPfPDyPYzYEipgqdwqKN41AvdFvnjQIplAlRqeLgVEgOOw2kP10xhGrBtlP7nYHkdk9RRSw7qyu-GDDodfl_5t-YjFp5xqw6ddvhBxjSFU64yE5FOVakW8uHbVE89ahtEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه ورود نتانیاهو در واشنگتن دی‌سی
🔴
نخست‌وزیر اسرائیل امروز با ترامپ دیدار می‌کند تا درباره ایران و اهداف احتمالی «تأسیسات هسته‌ای» گفتگو کند.
🔴
گزارش‌ها حاکی از آن است که نتانیاهو «اطلاعات محرمانه‌ای» درباره تأسیسات هسته‌ای کوه کلنگ ایران آورده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/138045" target="_blank">📅 03:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138044">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb91a1151e.mp4?token=HvUVRh-MX8LfmPMRiiPLBeL2zODm2_m8iJq8SNZsUOzQPMyH97V46RVlJExRegulBqV4DkoQG-uqguKvFAqmI3ZStByQGpmDowjsdde8gaAXTCgkM073LxLmGH7KMxIkflb1fBTviAT2jFgWYcpzMeo_-g7AD_mybXINoFMYD6YVsCWaw5Mm-sGv_ZkBZx1PiqnVeYQPJdjvy9yjqZ_BLNPnVi4tyhjVy0PRFrMfohvW89SPuKqJnGMiqTw41VTFOGohdtUlGMIY7IPv6Ni1Dc9DRN1_KRa-jsvgDQaxRdidqyfDk6J5NaA4gjvgUP4dt5ENAAUh2nfdWO3JR72_ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb91a1151e.mp4?token=HvUVRh-MX8LfmPMRiiPLBeL2zODm2_m8iJq8SNZsUOzQPMyH97V46RVlJExRegulBqV4DkoQG-uqguKvFAqmI3ZStByQGpmDowjsdde8gaAXTCgkM073LxLmGH7KMxIkflb1fBTviAT2jFgWYcpzMeo_-g7AD_mybXINoFMYD6YVsCWaw5Mm-sGv_ZkBZx1PiqnVeYQPJdjvy9yjqZ_BLNPnVi4tyhjVy0PRFrMfohvW89SPuKqJnGMiqTw41VTFOGohdtUlGMIY7IPv6Ni1Dc9DRN1_KRa-jsvgDQaxRdidqyfDk6J5NaA4gjvgUP4dt5ENAAUh2nfdWO3JR72_ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گریه خانواده اعدامی‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/138044" target="_blank">📅 03:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138043">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOgI9zBzXaS9-1dY-cQiNagLhGQ7nhKUX4Djes6KEsEEshV-TUHKNF9F11qIEms574Shn25gloA3GSMfnvfCS2ohL9phTnrtqKj3OjMqswLKNISh0CKBfAcA2fmqEeFXvE6WVnvXQjd3_sMq1Gxwpvs2RDLnX1CNw8MhIAjYZEsbiQ3_Y65oTAnQkmvqtvUtDSB7AYSoDgB6kXOvsU0N3eRt4T7jJS3s_NXsScB2i3lrXXyx1ygFSZq7IOGj8u2easdGgC4shdMA1iCTdQCxDklrIZ4JC7W8IkRHgX4jfU_6osntT5H924K16K2H4HNGtFXygcAOLnMfGoIxL99PdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آزاده آل ایوب(خاله نرگس): نباید به بازداشتی‌های اعتراضات عفو داد و باید همشون رو اعدام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/alonews/138043" target="_blank">📅 03:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138042">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c96ac69ef8.mp4?token=MA5ZAOwwteXKSN7izVG8wa-uQ5vi5j8nMtE3d5TkSWKLxKtPscFKwxXQ_QTQMYmpcjkAN-8U9El-MxjnXnOqZtr0UEf0cFqJc8W4NYriiLO1ggAdvik9pWhqvt8qgNnSYNkp89K6fSs2psPQtl-afOWtZlDiaU-ajcz6CVuaaKNWYnW0pLOZRv12TUa-nlT3xL7u3Envfgjm4N-spjrenjiqScMpQNcrNpQAw3HS6kjfRd8CuWBwImkMvOWn8cyEQUQ5ibo9h73P98eHPdp1yKjxsOgQqP9ODtGbdecBdx6CqzUgmUa-pgL1FEzg2mdDqLW94GZM2GHHO4-HG1ClD3wFuwr4PIdtm6tCiYFGIU-tn29KpCCtnFAEZxnKQeXythoSr8lBKKHu5WCvoDWQX0rSGdPkGWBk-Gifz62ItX7keAsFKMTV8WonOWH0b94Jumd426HoQ9vYvg5i0aY2cLDvk4NysbWf5LkCx9xvAilt0fQlbDbicVJe1pI3apWKoCU-SKncnkN3xUq2Dc3QYF3TfpiTWXMU9Mzky5XPPWVBgMZiCS50Kc10lAtV2MDBMqnLIlZ-P_nl0Cumom58rvvERS_epl-rpWVlOOpWqdycNE6SVfBIMaYK2qkXWNu4soR5tu-dQnVpPnjGYWGCd6YnZnv07i4hYEgNhAaTd7U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c96ac69ef8.mp4?token=MA5ZAOwwteXKSN7izVG8wa-uQ5vi5j8nMtE3d5TkSWKLxKtPscFKwxXQ_QTQMYmpcjkAN-8U9El-MxjnXnOqZtr0UEf0cFqJc8W4NYriiLO1ggAdvik9pWhqvt8qgNnSYNkp89K6fSs2psPQtl-afOWtZlDiaU-ajcz6CVuaaKNWYnW0pLOZRv12TUa-nlT3xL7u3Envfgjm4N-spjrenjiqScMpQNcrNpQAw3HS6kjfRd8CuWBwImkMvOWn8cyEQUQ5ibo9h73P98eHPdp1yKjxsOgQqP9ODtGbdecBdx6CqzUgmUa-pgL1FEzg2mdDqLW94GZM2GHHO4-HG1ClD3wFuwr4PIdtm6tCiYFGIU-tn29KpCCtnFAEZxnKQeXythoSr8lBKKHu5WCvoDWQX0rSGdPkGWBk-Gifz62ItX7keAsFKMTV8WonOWH0b94Jumd426HoQ9vYvg5i0aY2cLDvk4NysbWf5LkCx9xvAilt0fQlbDbicVJe1pI3apWKoCU-SKncnkN3xUq2Dc3QYF3TfpiTWXMU9Mzky5XPPWVBgMZiCS50Kc10lAtV2MDBMqnLIlZ-P_nl0Cumom58rvvERS_epl-rpWVlOOpWqdycNE6SVfBIMaYK2qkXWNu4soR5tu-dQnVpPnjGYWGCd6YnZnv07i4hYEgNhAaTd7U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جو شدید امنیتی در میدان علیخانی اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/138042" target="_blank">📅 03:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138041">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ترامپ به سی بی اس: مایل به توافق هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/alonews/138041" target="_blank">📅 03:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138040">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
یه سری کانال خبری هم که فاز مردمی برداشتن دیدن ویو خوبه بین خبر اعدام تبلیغ شرطبندی گذاشتن تا پول بیشتر گیرشون بیاد
🔴
یه حقیقت تلخی هست تو این مملکت هیچکس دلش به کسی نمیسوزه و همه منفعت طلب شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/138040" target="_blank">📅 02:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138039">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIEV_1gKVwIexNskcaImjZjdVou_7QaMhA95zQLH_HT-6vOBCI0czX32rZEAbVI1W2vgqXgQQZsIlHX60mS-_vyAQTSihClaeJP4rnZ07gbmk_RW7H6Umao4jfswKqHfqaDd_ojXTyrGTpgEMPEg7E5dKepnsunoR-q57ybqT-LPupSFxIKw6GB8wk7ultZme0k9Wr59_ZG8eNcyCnfP1prHa7AbdcvUI9DK7QWfu5OaEPvEqtRKD5Fdg70a9cl-0LNV9PeTaKm4kVFtbKka7OEsbJPkbP--x-9OXMb-OoxN13-8DO7DUiwgQsGsOREoDGZdzzWAHbVNNFDeIESfPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اعدامی‌ها رو آوردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/alonews/138039" target="_blank">📅 02:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138038">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5c5d18645.mp4?token=CU33XwNoQuCOGqxAGEhxNbjGNgLaoLO5tbXOrgDwlWOkM2uhKB2XJlU-qRF3cjL47nHbmTAyfNi30IJx7rrxL25iYOaYNH3RPkfvIrHgrnRkOkY1_Gy_jxoRJTav6H6Gj4P1-vFB0cXAo-UFbZCCKMExfw-H3TCM4Bd0NWJz0QMnc2I0LhnGQEGH3zwHR-gdbVZcxDxe8dTvXOSps6-Wq944JBvPAB_LPtXlq8afdvNi4pvLs0GxjAdO9uHlLkbWk1HJ1jic9nCfsqde1qamWQcDGdIcfo3-WHg3iGVtBaK0KUQBlY5ni7QufGcJcMe7uStKThfSf6VnuQAjjuVZXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5c5d18645.mp4?token=CU33XwNoQuCOGqxAGEhxNbjGNgLaoLO5tbXOrgDwlWOkM2uhKB2XJlU-qRF3cjL47nHbmTAyfNi30IJx7rrxL25iYOaYNH3RPkfvIrHgrnRkOkY1_Gy_jxoRJTav6H6Gj4P1-vFB0cXAo-UFbZCCKMExfw-H3TCM4Bd0NWJz0QMnc2I0LhnGQEGH3zwHR-gdbVZcxDxe8dTvXOSps6-Wq944JBvPAB_LPtXlq8afdvNi4pvLs0GxjAdO9uHlLkbWk1HJ1jic9nCfsqde1qamWQcDGdIcfo3-WHg3iGVtBaK0KUQBlY5ni7QufGcJcMe7uStKThfSf6VnuQAjjuVZXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعدامی‌ها رو آوردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/alonews/138038" target="_blank">📅 02:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138037">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
طبق گزارش‌ها، دقایقی پیش چند دستگاه آمبولانس و ون انتظامی وارد میدان علیخانی شدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/alonews/138037" target="_blank">📅 02:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138036">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/710f6ceb7e.mp4?token=EKUuW8RPyhErBHriILQw-TzE6Vy40Kt_pEZu5tqGj4pcsyAE8U83pWGdMv9hy3Sqd85bj93cSpbF_EOJH4jS5yPyQmJoi5H0Fi6ncCBRUcOiCmeHb9E8_hJXU1b9LurLi5oS2d3S37mFr6DCQCRr5aCTVjAhq6iupkwtSYBor4FI9ILGUHd-X_WuKqmN0CsPqapapt0fsDJJoFWgWxzE5D-_JPe0C55cm2JyrabzhOc5BD-yolyufR_lODGtV8brVq9XowqayoJtZTPTDAz07pzNFC0YUgI1Tvtq2cpRwcch5bQXTJmpCmWjy5jkvqkODwOkx0RCfyNPNijrt-LDmrMZq9NyomKZzvM5XA4Jxf_Pp0Sq30uH9YlAWp6umocIGUNfCkj4iNkp7RUpDa7bzzaJ8WLdgC6RfcKtMULJXR2iXMOMtnjRxLLt_N_vg8Axp7d23VVAy9gb3zKoqgh9rLeAH7hL4VSCkQGTMoKdl2sPSibqOFfrZkSnQLBq9LSOa-tw1xtvISOYGSTzQAC_j1uJnpfU_hk5Ha6sV52qgjGOe0TEtefHAT2liWX61Mka9OQCQ1xugXpIeGo1uVezOo3OBkaSZF9RDqJ79buIwGZ1EQ53wscv2gEK5VK-szkZSOiJpR_uwOXG1z29Pd4vuqYokOEzOOnsOpz_pMpKhK0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/710f6ceb7e.mp4?token=EKUuW8RPyhErBHriILQw-TzE6Vy40Kt_pEZu5tqGj4pcsyAE8U83pWGdMv9hy3Sqd85bj93cSpbF_EOJH4jS5yPyQmJoi5H0Fi6ncCBRUcOiCmeHb9E8_hJXU1b9LurLi5oS2d3S37mFr6DCQCRr5aCTVjAhq6iupkwtSYBor4FI9ILGUHd-X_WuKqmN0CsPqapapt0fsDJJoFWgWxzE5D-_JPe0C55cm2JyrabzhOc5BD-yolyufR_lODGtV8brVq9XowqayoJtZTPTDAz07pzNFC0YUgI1Tvtq2cpRwcch5bQXTJmpCmWjy5jkvqkODwOkx0RCfyNPNijrt-LDmrMZq9NyomKZzvM5XA4Jxf_Pp0Sq30uH9YlAWp6umocIGUNfCkj4iNkp7RUpDa7bzzaJ8WLdgC6RfcKtMULJXR2iXMOMtnjRxLLt_N_vg8Axp7d23VVAy9gb3zKoqgh9rLeAH7hL4VSCkQGTMoKdl2sPSibqOFfrZkSnQLBq9LSOa-tw1xtvISOYGSTzQAC_j1uJnpfU_hk5Ha6sV52qgjGOe0TEtefHAT2liWX61Mka9OQCQ1xugXpIeGo1uVezOo3OBkaSZF9RDqJ79buIwGZ1EQ53wscv2gEK5VK-szkZSOiJpR_uwOXG1z29Pd4vuqYokOEzOOnsOpz_pMpKhK0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قوه قضاییه:
علت حکم اعدام متهمین میدون علیخانی اصفهان اینه که این افراد در 18 دی ماه تو میدان علیخانی، مامورها رو با طناب به تابلو بسته بودن و بعد از اینکه با سنگ زخمیشون کرده بودن روشون بنزین ریختن و آتیش‌شون زدن و درحالی که مامورا زنده بودن اونا رو روی زمین میکشیدن و با چاقو تیکه تیکه‌شون کردن و فیلمش رو برای رسانه‌های معاند فرستادن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/alonews/138036" target="_blank">📅 02:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138035">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jIautNwdWHjtVTi4XVLJTpNKLBkO2d9N9MOEdn3M_s8vVjGBITYL5ma_1P_l8xx4g8tKK7DwXDcJQdXrMEvF2m-vg_Cxl-XD2-G2HI1_EoXH1ze4fSh0UCF5yslsxhsVjfdf6xg_w_6nwO93ZlQFkpBo12IyWhQYAoWKD2GD3SPKLf77B9OLcpwEA-EQPNvoU65HbGROzrjhKtoW0kgrEPf-6o-_LVkOeCbEY9owOyd0b_p5KDTnEHVk-crsuVb66Bto2LEDvNpZZMnR5i91Tuz8qPsc5XDxQnKyHCkPZ0dh74NC_Crvew21u2-DGt0avmziztpyflY4DCwx-e4TNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا همزمان با اذان صبح، مهدی ظریف 23 ساله هم بخاطر شرکت در اعتراضات دی ماه، در مشهد قراره اعدام بشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/alonews/138035" target="_blank">📅 02:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138034">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ql2ISSGRfkWmL5zsWx1byQkrsSr8dKQWNmN5jvai-Kf3DTHTHmTt9xVnt1XZbT48_s1AUWmHME9AqmhJ87HkSETslNIEeytRZKSFoT2fDlihniI4WxbgrNRQqyHxCivs-fOW5cv6vD95pNgD-oVNPSI0ewj2g3QNTntwcBHTBhqMDGx8mwTxEI_zthn-Hw-vYY6u_7zYzsghuWO0gqx-kKzzBEpbEXInRN2oyD2rYObzJyMC3ihvVmkX2UGUXdPwFMFroxQIh9HmC9c2LZ2UyxPtbsp7Hz4KRw_wRVSro5vxEDD3SSYZLnU2iBROf48SMBqVWY2fCIYcUCxD4YGv2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بنر نصب شده در میدان علیخانی اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/alonews/138034" target="_blank">📅 02:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138033">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/780d746559.mp4?token=JlBoLUQv2WQ0gfPdBhecRnCtHkj5StkSLHl24d1O8wim0MWwHWelkF36DPPF9jPHf-hMETifVdiqNmEoWJYptAZFUIL6lV4I6IrBj9vYZ09-kAbnq3l36hdYCjhhFtukmyCNGydaaLPO9nkPw0fdDA6GTkHdn0kmFaFi1GhkHVFiLJ3FJF7B0HOqh-m5CQGV2dpckz630uxj_WOxknMdDyPdzwRpx-L0JkfWDkcBYbmdzYdV_8tTzhJ-xrcpvcWq_bRX55hXbTtnHaQpZgrQjy-uGXlsSN3GBE8qJBO1vSKFAUmii68_3KIpxElLfRHanZmSxfwMAoLoBeA7QLRIAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/780d746559.mp4?token=JlBoLUQv2WQ0gfPdBhecRnCtHkj5StkSLHl24d1O8wim0MWwHWelkF36DPPF9jPHf-hMETifVdiqNmEoWJYptAZFUIL6lV4I6IrBj9vYZ09-kAbnq3l36hdYCjhhFtukmyCNGydaaLPO9nkPw0fdDA6GTkHdn0kmFaFi1GhkHVFiLJ3FJF7B0HOqh-m5CQGV2dpckz630uxj_WOxknMdDyPdzwRpx-L0JkfWDkcBYbmdzYdV_8tTzhJ-xrcpvcWq_bRX55hXbTtnHaQpZgrQjy-uGXlsSN3GBE8qJBO1vSKFAUmii68_3KIpxElLfRHanZmSxfwMAoLoBeA7QLRIAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون میدان علیخانی اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/138033" target="_blank">📅 02:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138032">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">#نه_به_اعدام</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/alonews/138032" target="_blank">📅 02:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138031">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1dfac21ffc.mp4?token=oeSCvKnmPWVw2XiZkeSW9XuAf_3XXjgRwHCNU4PcaJYtVX5etkF2eVY5FTTDiwa5ctgkZLR0J5VLshb57BC8_WuYARu3scSD3ypfhr-_DWvs19-x5DjLX5tlr-p5mgr75loQ5UIhRn3F9AhKSlggQMNxjgZKISX16R0hNPVUN8N8krH4OHEEYHC_Nhf3SxS7UGYSqVVFHA4IOrJlKOqacl0deluyvchXtTSwgKwsD6CQ4YweFugOjbqfkhX7gWhRvs-objhrMvkrOgZGbE51I56TQ3vgQoojgX7rit5PXtdaV-5mGtZteb0mFV5GWBgNj-AeXZGx74_QG0WS4hoNQg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1dfac21ffc.mp4?token=oeSCvKnmPWVw2XiZkeSW9XuAf_3XXjgRwHCNU4PcaJYtVX5etkF2eVY5FTTDiwa5ctgkZLR0J5VLshb57BC8_WuYARu3scSD3ypfhr-_DWvs19-x5DjLX5tlr-p5mgr75loQ5UIhRn3F9AhKSlggQMNxjgZKISX16R0hNPVUN8N8krH4OHEEYHC_Nhf3SxS7UGYSqVVFHA4IOrJlKOqacl0deluyvchXtTSwgKwsD6CQ4YweFugOjbqfkhX7gWhRvs-objhrMvkrOgZGbE51I56TQ3vgQoojgX7rit5PXtdaV-5mGtZteb0mFV5GWBgNj-AeXZGx74_QG0WS4hoNQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون میدان علیخانی اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/138031" target="_blank">📅 02:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138030">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YTkRszIQl170K4bLAU1nmGi-wjZ6RbObrW5oNXCWJ-KesDG06cyICRXLh6s4RrcvmvdjeeYHctR1t9EfDzaS5fmduXS_9t6gnAgQ1eAXNDOVZbt4W_uX7NEQ67zG4565wyxB1HWG9y_NQLGdZB4uto8L3pcS1ht6n6jTuKwRivsSUayRfbGCKALqF4Ng2ISm5DI8Sd9bZH5VCDIicmqJgoqovnSy2FqCrRHDs0DYsMyYuJ8GL4gnLTKnyOVweksmfKxfnt-Sh3imwuzDUlIMQD1oDmPswYIVeQ1gQIR8U4mUg0yp3S6F4q_NLGma3UAV1oxYdnIX8yVYscmryOP-UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه نگاه به دستای امیرحسین صفری بندازین!
🔴
این طفلی اصلا معلوله! آخه چطوری میتونه یه مأمور رو کشته باشه! چطوری دلتون میاد اعدامش کنین
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/alonews/138030" target="_blank">📅 02:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138029">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d0967f8fa4.mp4?token=r5CLJx0XnOoJOV5sXE_x7_9fC_oVOdUJsSrsVf-zSoRxnHz1Kt3KYXN8SN85m6I84DFVxNL-m8_HC1YrYwZq2iEreyDl4BCLVEJrRGZkMask16Ll2hJ1bqGhMj6YLUtM3MigsiqfteLzAQ9L3usFsQ9CpQ3Himxwy5fo7VA2jozgI7LqfwFNqtd74B_a3JiBvEXBDyA_7T4O8cDKnr1WpFZMLHiPxI-NPmhKBoV1rNawQjRoq_dWMZL14eyEldsydQJOVGiS4FWi4hRdGbjbFkZddduOu_NdW5hzi82FUSwfLb4jwLPPrQtIjko7B-oyCPU3qSaR6zAyMiwseUi9-g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d0967f8fa4.mp4?token=r5CLJx0XnOoJOV5sXE_x7_9fC_oVOdUJsSrsVf-zSoRxnHz1Kt3KYXN8SN85m6I84DFVxNL-m8_HC1YrYwZq2iEreyDl4BCLVEJrRGZkMask16Ll2hJ1bqGhMj6YLUtM3MigsiqfteLzAQ9L3usFsQ9CpQ3Himxwy5fo7VA2jozgI7LqfwFNqtd74B_a3JiBvEXBDyA_7T4O8cDKnr1WpFZMLHiPxI-NPmhKBoV1rNawQjRoq_dWMZL14eyEldsydQJOVGiS4FWi4hRdGbjbFkZddduOu_NdW5hzi82FUSwfLb4jwLPPrQtIjko7B-oyCPU3qSaR6zAyMiwseUi9-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون میدان علیخانی اصفهان که قراره ۳تا جوان رو اعدام‌ کنن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/138029" target="_blank">📅 01:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138028">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
هواپیما بی‌بی نتانیاهو دقایقی پیش در واشینگتن به زمین نشست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/alonews/138028" target="_blank">📅 01:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138027">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
به صدا درآمدند آژیرهای خطر در کنسولگری آمریکا در استان اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/alonews/138027" target="_blank">📅 01:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138026">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501833108d.mp4?token=KYsd6BmUE_nRtQ7rjJ9CwZzgm84dG9xy3VD8pEA6S04vLxsPq0rE4jIM_80Xg8sBdZjQQJy6QEiG34gqhk0Xjrq7Q6QnLuT-b_Tvt2xW48jxFK5jHgk0PS9JeDlcT7_zrf5aexAV88AJRvQKaYyuChdIHW-5hnl1oNIyaJzDzvG1T-Nts7YfsyXbTIbT1WigqC21mwzgJNQI9w9ngK1PyMiKfcn3OnfE_YHsIUvyaBpXoG__SRkRYMShhBgazbHRa14hc5aZ_GJ-pFlC9xsQuc80jBQaT0mv15tFPQp0TeoGkk7eZE3mUJCQs2fjy07Ce-8RIFPg5Umeu_C5VkVnxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501833108d.mp4?token=KYsd6BmUE_nRtQ7rjJ9CwZzgm84dG9xy3VD8pEA6S04vLxsPq0rE4jIM_80Xg8sBdZjQQJy6QEiG34gqhk0Xjrq7Q6QnLuT-b_Tvt2xW48jxFK5jHgk0PS9JeDlcT7_zrf5aexAV88AJRvQKaYyuChdIHW-5hnl1oNIyaJzDzvG1T-Nts7YfsyXbTIbT1WigqC21mwzgJNQI9w9ngK1PyMiKfcn3OnfE_YHsIUvyaBpXoG__SRkRYMShhBgazbHRa14hc5aZ_GJ-pFlC9xsQuc80jBQaT0mv15tFPQp0TeoGkk7eZE3mUJCQs2fjy07Ce-8RIFPg5Umeu_C5VkVnxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش حمله و انفجار در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/alonews/138026" target="_blank">📅 01:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138025">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=ArsVlj8hWbxzXA75H5UExUNoYqkL7qtcMuBE0xKgVUS7Eq2pD9uG2zIBveKI6_agqU3KRdbEBAY2A0CvlmI94A8e7rpijKKs2UUltkU3q5gXxzWuNyn_Ji1ssB5PHGiIcUI64zOHOGd2ArcbTXDMrTPIout6tLevMeCqsJV5lvJm3MdZUQP1NO8a7hvPqboUJCsX-t9_qTiXXBR9f5PF5_LAJW1VCK-KANkLmx_vn70GMHWFLaBAFqlUCxDW5qZJ9Q5aJpV_hqgNeYzcENtRjC7xPU6unUdf9tma9SiYXsXjKPmjeEAoYUBPB4gBw3jpo7huAA6GXVhZjs463aCzDIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=ArsVlj8hWbxzXA75H5UExUNoYqkL7qtcMuBE0xKgVUS7Eq2pD9uG2zIBveKI6_agqU3KRdbEBAY2A0CvlmI94A8e7rpijKKs2UUltkU3q5gXxzWuNyn_Ji1ssB5PHGiIcUI64zOHOGd2ArcbTXDMrTPIout6tLevMeCqsJV5lvJm3MdZUQP1NO8a7hvPqboUJCsX-t9_qTiXXBR9f5PF5_LAJW1VCK-KANkLmx_vn70GMHWFLaBAFqlUCxDW5qZJ9Q5aJpV_hqgNeYzcENtRjC7xPU6unUdf9tma9SiYXsXjKPmjeEAoYUBPB4gBw3jpo7huAA6GXVhZjs463aCzDIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بخش‌هایی از سخنرانی ترامپ در میشیگان:
🔴
آن‌ها ۴۷ سال است ــ که در واقع نزدیک به ۵۰ سال می‌شود، چون دست‌کم سه سال است همه می‌گویند ۴۷ سال ــ مذاکره می‌کنند و تنها کاری که انجام می‌دهند این است که همه را معطل نگه می‌دارند.
🔴
همچنین نمی‌توانیم اجازه دهیم آنچه در ایران اتفاق می‌افتاد و هنوز هم اتفاق می‌افتد ادامه پیدا کند. آن‌ها در یک دورهٔ چهارماهه ۵۲ هزار معترض را کشتند؛ تصورش را بکنید، ۵۲ هزار نفر در ایران.
ترامپ: ... ونزوئلا.. پس از آنکه تقریباً ظرف ۴۸ دقیقه پیروز شدیم، گفتند: «اوه، حرکت خوبی بود.» خب، همین اتفاق اکنون در ایران در حال رخ‌دادن است.
مردم هنوز متوجه نمی‌شوند. ما نیروی دریایی‌شان را نابود کرده‌ایم. نیروی هوایی‌شان را نابود کرده‌ایم. رهبری‌شان را نابود کرده‌ایم. تسلیحات ضدهوایی‌شان را نابود کرده‌ایم.
پهپادهایشان اکنون با حدود هفت درصد ظرفیت قبلی تولید می‌شوند. بخش عمدهٔ توانایی تولید پهپاد و توانایی تولید موشکشان را نابود کرده‌ایم.
اکنون با ما دربارهٔ دستیابی به یک توافق صحبت می‌کنند؛ اما اگر ما این کار را انجام نداده بودیم، هیچ مذاکره‌ای در کار نبود.
آن‌ها ۴۷ سال است ــ که در واقع نزدیک به ۵۰ سال می‌شود، چون دست‌کم سه سال است همه می‌گویند ۴۷ سال ــ مذاکره می‌کنند و تنها کاری که انجام می‌دهند این است که همه را معطل نگه می‌دارند.
آن‌ها قلدر خاورمیانه و قلدر ما بودند. اوباما ۱٫۷ میلیارد دلار پول نقد سبز به آن‌ها داد. یادتان هست؟ پول‌ها را داخل یک بوئینگ ۷۵۷ گذاشتند و به تهران فرستادند؛ ۱٫۷ میلیارد دلار پول نقد.
او تصور می‌کرد می‌تواند به آن‌ها رشوه بدهد؛ اما آن‌ها در عوض با خودشان گفتند: «این کشور چقدر احمق است.»
نه، نمی‌توانید به آن‌ها رشوه بدهید. باید شکستشان بدهید و ما داریم حسابی شکستشان می‌دهیم. اما خواهیم دید نتیجه چه می‌شود.
اکنون مذاکراتی بسیار دوستانه در جریان است.
نیروی دریایی ما در اجرای محاصره چقدر خوب عمل کرده است؟ حتی یک قایق [نتوانسته عبور کند]. آن‌ها می‌گویند: «دیگر محاصره را نمی‌خواهیم. لطفاً، لطفاً، محاصره نکنید.»
---
ترامپ:
اکنون قیمت تخم‌مرغ بسیار پایین‌تر از زمانی است که کار را آغاز کردیم. خواهید دید پس از آنکه تهدید هسته‌ای ایران را از میان برداریم ــ که بسیار زود اتفاق خواهد افتاد ــ اوضاع چگونه خواهد شد.
اما افزایش قیمت‌ها ربطی به من نداشت.
---
یکی از سخنرانان همراه ترامپ:
۴۷ سال طول کشید تا کسی بایستد و بگوید دیوانه‌ها نباید سلاح هسته‌ای داشته باشند.
همچنین چندین دهه طول کشید تا مشاغل را دوباره به داخل کشور بازگردانیم.
---
ترامپ:
نمی‌توانستیم اجازه دهیم آنچه در ونزوئلا اتفاق می‌افتاد ادامه پیدا کند و اقدامی که انجام شد بسیار قاطع بود.
همچنین نمی‌توانیم اجازه دهیم آنچه در ایران اتفاق می‌افتاد و هنوز هم اتفاق می‌افتد ادامه پیدا کند. آن‌ها در یک دورهٔ چهارماهه ۵۲ هزار معترض را کشتند؛ تصورش را بکنید، ۵۲ هزار نفر در ایران.
اما هزینهٔ عملیات ونزوئلا، همان‌طور که گفتند، تاکنون جبران شده است. به همین ترتیب، در برابر جمهوری اسلامی ایران نیز با اختلاف زیادی در حال پیروزی هستیم و تضمین می‌کنیم که آن‌ها هرگز به سلاح هسته‌ای دست پیدا نکنند.
وقتی کسی می‌پرسد: «چرا این کار را انجام می‌دهیم؟» پاسخ این است که نمی‌توانیم اجازه دهیم شما سلاح هسته‌ای داشته باشید. همین تنها چیزی است که لازم است بگوییم.
اگر قدرت سلاح‌های هسته‌ای را درک می‌کردید، دقیقاً متوجه می‌شدید که چه می‌گویم.
---
بار دیگر می‌گویم: ایران هرگز سلاح هسته‌ای نخواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/alonews/138025" target="_blank">📅 01:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138023">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JB07cU6JlHuHJYSjpc-EF88M6tYrFz4dQ9S262DwnF7hVT1IfOhhQdl5fNNek0OtlZ8-7xA1mzgjEBCO0Da5S6SasEtMsrX_xg10HY-CF6aitY9CIBVTIwogRvbHTnhZPvh1zAQ8EAQXvNmKPVuZLB4x1-JX7ZYizdEC1ATxlU1xIZL8xGJK4s3PFrjJ2jPFF3NPYDcfTVXR7tvX_4bh5UX3VQp5kvcNXdRGPAn-dQ3fQfKWgTZXp6IQVlibTJafiTL16CRNLB0qBu1kIY0h85_XpBstWqsC8PC0QEaHhuF6spCcsfUpfhbFojDUeCWkudIMoUN-5Aqx8W5WKFV6LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ryopj8XH0Q_uH_uNJih8ze6dU9PMHKhxNKYcSZPEFudWXLaIPly7FKRtq-F_5_ZT53JWEScMAyZaQJcYaDJ1v5xmcWWd11sfb_PyrY2DHrVgg3lqvu328yq9k-xVpaZngrC-VVGXlO9Z2CdXiz5a8NvdvpgcI7R2ZWH9k6w7eDZDN-6q90hLtQhMEiiu-qhtC4dvMuXCChO-XB4baY9lG6-ENiGFjmCRUfgWROYz4ySCgZ6aA0JEpZLMRlwwMm6DKok0P6CJe-aSe_fXPUGR0laauV_D0dwJlvpStS0YdvcYMZQucRIKKfECjWy6Iw0bTVvx82SEO81f5jQVfJhUjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یه پسر ۱۱ ساله داشته بازی می‌کرده که از ارتفاع ۱۰ متری سقوط میکنه و از شانس بدش، میله آهنی مستقیم فرو میره توی باسنش!
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/138023" target="_blank">📅 01:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138022">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9b8525811.mp4?token=PNURjdQGOCELme_TxIDa-Y03oCqu49QLQY6ctw0nCz9X8UmOeFqFuPooNz9lJZqeQvGp99jWyDR7zQz32Y-K-24Tr0kB-HTkbNfF9e58OUgrbTFCX1hJnE8LwrxIhmEKiqU29_lP6hof7k7s95L_51iw6iQSwUW_ZcNKoeLASn-757GSrmY2q5-BgmACiv28LHSqsQVpeFGF9D9RvRbe5oUEK3AdstXs6ExfAP0_O-KdBkT-f9K8-KdNoxqCsRwYF8vrEOybndLdpuh_4e4joKm8UTeSepnPgC9l6LqzuFKHyFH5eS3Mkrv-326PPvRWNQ5WuHnYOqTLruAbV4BzhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9b8525811.mp4?token=PNURjdQGOCELme_TxIDa-Y03oCqu49QLQY6ctw0nCz9X8UmOeFqFuPooNz9lJZqeQvGp99jWyDR7zQz32Y-K-24Tr0kB-HTkbNfF9e58OUgrbTFCX1hJnE8LwrxIhmEKiqU29_lP6hof7k7s95L_51iw6iQSwUW_ZcNKoeLASn-757GSrmY2q5-BgmACiv28LHSqsQVpeFGF9D9RvRbe5oUEK3AdstXs6ExfAP0_O-KdBkT-f9K8-KdNoxqCsRwYF8vrEOybndLdpuh_4e4joKm8UTeSepnPgC9l6LqzuFKHyFH5eS3Mkrv-326PPvRWNQ5WuHnYOqTLruAbV4BzhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مصاحبه زنده یاد کیانوش سنجری با شبکه (آیت الله) بی بی سی که حرفاش به مذاق این شبکه خوش نیومد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138022" target="_blank">📅 01:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138021">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
گزارش‌های تائید نشده از حمله به کنسولگری آمریکا در اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/138021" target="_blank">📅 01:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138020">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b4fa9f23e.mp4?token=j-hHdBKMUiR9S2dVnNQQF_mORs4A0aXXObOHZKDX1RzvSSH1w9xVe0mQIeViofKaMVpe-euxihqMCHkqP1NsiLcUuXkXdgR-EBsLMvFvGkZ35U1rkafg_xj0Hwii122WFqsfCnYrihAPbsLNH9uMDh98y3HVWFBoVYbsYvvHpDmDmZ6QEO4pF0gFnQCPSzjC2E4rYeyjRzPg-fkK5usiQW9Rg9O8OJXgajvxkMbC_41wVYNZRZcxpjRmIR7v5-i70qsotPDgCiPHMSctgMovl9VoLZi44dleiOyaTcbGn8T1MzQLO1wKe89u1fzZ9HyRBp7i0OOtagtM-T-0DJ1YwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b4fa9f23e.mp4?token=j-hHdBKMUiR9S2dVnNQQF_mORs4A0aXXObOHZKDX1RzvSSH1w9xVe0mQIeViofKaMVpe-euxihqMCHkqP1NsiLcUuXkXdgR-EBsLMvFvGkZ35U1rkafg_xj0Hwii122WFqsfCnYrihAPbsLNH9uMDh98y3HVWFBoVYbsYvvHpDmDmZ6QEO4pF0gFnQCPSzjC2E4rYeyjRzPg-fkK5usiQW9Rg9O8OJXgajvxkMbC_41wVYNZRZcxpjRmIR7v5-i70qsotPDgCiPHMSctgMovl9VoLZi44dleiOyaTcbGn8T1MzQLO1wKe89u1fzZ9HyRBp7i0OOtagtM-T-0DJ1YwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حکم جلب این بلاگر طرفدار حکومت بخاطر نوع انبه خوردنش صادر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/138020" target="_blank">📅 00:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138019">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
رئیس صداوسیما : اعتماد مردم به صداوسیما از اعتماد مردم به دولت بیشتر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/138019" target="_blank">📅 00:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138018">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سپاه: نسبت به دوران جنگ خیلی قوی شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/138018" target="_blank">📅 00:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138017">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
تو میدان علیخانی اصفهان داربست نصب کردن و جو به شدت امنیتی شده  طبق آخرین اخبار ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری به انفرادی منتقل شدن و قراره تو ملاعام اعدام بشن #نه_به_اعدام #زیرساخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/138017" target="_blank">📅 00:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138016">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2x1xyzeXT03QRxjwUQM3zivH0uYzpdn-0mU0s5Xkg7Oh4RKTmGk5iq5kTD6IpFvM_OhdsZuMOVVcbSev23GCOkmdMeSmN36_-3ieXxc7IqbF2tWrp67vyGCDmiVCq2zVPUoVYT8KYVoiSdKFl7ps-0xtd4wvNjgUH-nMpKcANg4QIW4B-0EviV_rAMo9aHqmOnFn5lkvfNDFEza-AwHT0baVqxhmLgaktC6XkQa1-V1CwCsLb04i9kw-P68IJtgek8p5dP_7-bcX1zs4NKJ0CxK4zkcHbUlsSWBpPmGQ-JBqy_8Y99w_-14vvwnocXptGyeLZ1n7mjkMVkwc8mmZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو میدان علیخانی اصفهان داربست نصب کردن و جو به شدت امنیتی شده
طبق آخرین اخبار ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری به انفرادی منتقل شدن و قراره تو ملاعام اعدام بشن
#نه_به_اعدام
#زیرساخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138016" target="_blank">📅 00:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138014">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G1lgmQ3nM8vXvn9QXJQDUTEmRhwvuEy66qaSs3IqPvt6d9qDbkfJDH43DbSYEkIEo-g7ZK11X4WkI4Y_RS4ew_c7FUHg2fGB_FXjy-GIR7R7qJx3-xn0QH7a3hJV_pbR_NahC5c_uRs4671W4c1YemKD-rAJeA4aPezOArrA_5FNDC1Dd02OU9RwEqJO-DspRwZ7LCkrSNZZdFiIJOvHrpQ-loyTeGv59M8d8CRFPtjDqPrwF-PC2do3TgP65lqcyOrx3q-mHqPqw2fdQDVD_v1e4FdFFcN1MHjYFy-3GdyJZR5oEqXc9m6pVtZciBNBKb6p2-CogfQFh915dT7_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/caSUO2AIhwcl2w2dOz9MuAMeIVzndFDjEvB3Cg1qLgOwrgFpC7B4fkgBXcwqSumzLYx6TblnFHeGLa6yw8mZfaF1jmFcmnztHoTbiyyEWfNO-AQuKa7YX1plCFlGjI8s3hxlikd_aFYV5K4x_b1g6lYPiBT3RMUVOz1-HyyITlfAhsNCSSEZPLgWU4Dp6b2skhuxExxxsDMQQKs_3yimL_l1dg6xTMj1FP5pG410GC54QcXmzPzr6Uh2pPu5-xTmcJ4xgM63FCr7hYadKsIrHkUFlLBb1SNnBLOrxlZiIZsF9AEBGh55usd3ougEo-T6vSRbBgjQ8b-4uH-ghWF5HQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امباپه با بازیگر معروف، کوماتوزه رل زد
@AloSport</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/138014" target="_blank">📅 00:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138013">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
این وسط از دقایقی قبل یه گروه هکری عکس ترامپ تو جزیره اپستین همراه دخترها رو منتشر کرد
◀️
مشاهده فوری
به شدت داره ویرال میشه
🔖</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/138013" target="_blank">📅 00:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138011">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترامپ سه‌شنبه میزبان زلنسکی و نتانیاهو در کاخ سفید؛ ایران و اوکراین محور گفت وگوها
‏
🔴
یک رسانه آمریکایی اعلام کرد: دونالد ترامپ رئیس‌جمهور آمریکا روز سه‌شنبه در کاخ سفید میزبان زلنسکی رئیس‌جمهوری اوکراین و بنیامین نتانیاهو نخست‌وزیر اسرائیل می‌ شود و ایران و جنگ اوکراین و روسیه محور گفت وگوها خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/138011" target="_blank">📅 23:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138010">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6dd15287.mp4?token=meckTjmaslaJuhe-qoxcVMbFaWKF09xbqkg3710ZczI2Jf5qJfj2UzE-1DIQikV-p4CvmwhIRtQsPMrvtQeBJKWNycck8gFyO04HliIkiYN7Chod_sFFVD13JuFxAIJBeR608F2OLXHJ6tV88AonoOKlmXSvLKuR41tKwK9tewN6uT5OFRQDhJuj7LF8FoFiPP_oQdUk5bO4OdszNmE4A0BqLz-Y44wjFEdNkwV2nZBMsRY_J6VEeX2MyNEo1DRJccOph3k9YAPPyKn_vlfYte6C_DKBSeUv6bVuVIR-B0Bet7qEiiAqjVHRgL3c7yPmjnyM9cSRzGhd1vPwFFDpXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6dd15287.mp4?token=meckTjmaslaJuhe-qoxcVMbFaWKF09xbqkg3710ZczI2Jf5qJfj2UzE-1DIQikV-p4CvmwhIRtQsPMrvtQeBJKWNycck8gFyO04HliIkiYN7Chod_sFFVD13JuFxAIJBeR608F2OLXHJ6tV88AonoOKlmXSvLKuR41tKwK9tewN6uT5OFRQDhJuj7LF8FoFiPP_oQdUk5bO4OdszNmE4A0BqLz-Y44wjFEdNkwV2nZBMsRY_J6VEeX2MyNEo1DRJccOph3k9YAPPyKn_vlfYte6C_DKBSeUv6bVuVIR-B0Bet7qEiiAqjVHRgL3c7yPmjnyM9cSRzGhd1vPwFFDpXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما به پاکسازی کشورمان از مجرمان خطرناک، قاچاقچیان مواد مخدر، قاچاقچیان انسان و افرادی که از کودکان سوء استفاده می‌کنند، ادامه خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/138010" target="_blank">📅 23:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138009">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73846f9e59.mp4?token=KDOvdzqbds7AKyHf5eLkdZsBWmtNcAXJWe9qOIyYtAufiFGLvDk17SS-azugjMSvUjyamS7Z2kL1JVe-P-YkEY9HGufVvFtS3tUUy9v2x1CNN6EZkbazkYWmXvs2kSdHYq_E5dGNHIBN5GI3y6LtEOV6WA2LqicygHlJC7pQepwY8DoDeDfwQUw4DXyuzxA_68PkwViD7-Jsy_epOLmRxLGRulKhV2d8FQScE5aGY7MjGn7TBGwF2151XyXeRu3o342rIu9jCgeFu0qPpKZDwswZTqbg0-AgxsxUxUteJV8-ta-0c6zlz6EBJPJuUcziu0Guag4x3etbByXFsr2PfzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73846f9e59.mp4?token=KDOvdzqbds7AKyHf5eLkdZsBWmtNcAXJWe9qOIyYtAufiFGLvDk17SS-azugjMSvUjyamS7Z2kL1JVe-P-YkEY9HGufVvFtS3tUUy9v2x1CNN6EZkbazkYWmXvs2kSdHYq_E5dGNHIBN5GI3y6LtEOV6WA2LqicygHlJC7pQepwY8DoDeDfwQUw4DXyuzxA_68PkwViD7-Jsy_epOLmRxLGRulKhV2d8FQScE5aGY7MjGn7TBGwF2151XyXeRu3o342rIu9jCgeFu0qPpKZDwswZTqbg0-AgxsxUxUteJV8-ta-0c6zlz6EBJPJuUcziu0Guag4x3etbByXFsr2PfzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما در روابط با جمهوری اسلامی ایران به موفقیت‌های بزرگی دست یافته‌ایم و ما اطمینان حاصل می‌کنیم که آن‌ها هرگز سلاح هسته‌ای نخواهند داشت.
🔴
وقتی کسی می‌پرسد: «چرا ما این کار را انجام می‌دهیم؟»، به سادگی بگویید: «چون ما نمی‌توانیم اجازه دهیم آن‌ها سلاح هسته‌ای داشته باشند.»
🔴
این موضوع بسیار ساده است. این تمام چیزی است که باید بگویید. نیازی به گفتن چیز دیگری نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/138009" target="_blank">📅 23:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138008">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترکیه فروش سامانه S-400 به مصر را بررسی می‌کند.
🔴
بر اساس گزارش Defence Arabic، آنکارا در حال بررسی فروش سامانه‌های S-400 به مصر است؛ اقدامی که می‌تواند یکی از موانع اصلی بازگشت ترکیه به برنامه جنگنده F-35 را برطرف کند.
🔴
گفته می‌شود این موضوع در جریان سفر اخیر وزیر دفاع مصر به ترکیه مطرح شده است.
🔴
مصر هم‌اکنون سامانه S-300VM روسی را در اختیار دارد و در صورت نهایی شدن این معامله، توان پدافند هوایی خود را بیش از پیش تقویت خواهد کرد.
🔴
به گزارش منابع، ترکیه این معامله را بخشی از یک بسته گسترده‌تر همکاری‌های نظامی و فنی با مصر می‌داند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/138008" target="_blank">📅 23:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138007">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b21566da8a.mp4?token=B6LcAt3h9l2XC66buZJzW3jaO7fnkkiZumWElU6HB9ctbR_enBSZgR_Aa2gIZiH2nsru73oNVNT-TyuisQvyoNAcWs5XXBCm_PVyHI3GDH6gR69W51Wk8MWMpSwXlJLh5aNU8y4iDmuW5jr-lcXx0SV3Ws1Z7OgEcge-FxlMwOHhSkiBDeEtZfVGi7P5Vo7rWThXdBsGAKucfTQXxAgEoos_YG651TQHp_ZbO-Q6Vzn9zoK9o0WJGoX_BRPtCX6otP_-Mce7NpX20B5NjKJ8cDc-ArU8KEnTZZPPmAm9IpzbBeL-8wX-UZaSlnG0968XiGsjmPPRxKoFyo6ghhQAwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b21566da8a.mp4?token=B6LcAt3h9l2XC66buZJzW3jaO7fnkkiZumWElU6HB9ctbR_enBSZgR_Aa2gIZiH2nsru73oNVNT-TyuisQvyoNAcWs5XXBCm_PVyHI3GDH6gR69W51Wk8MWMpSwXlJLh5aNU8y4iDmuW5jr-lcXx0SV3Ws1Z7OgEcge-FxlMwOHhSkiBDeEtZfVGi7P5Vo7rWThXdBsGAKucfTQXxAgEoos_YG651TQHp_ZbO-Q6Vzn9zoK9o0WJGoX_BRPtCX6otP_-Mce7NpX20B5NjKJ8cDc-ArU8KEnTZZPPmAm9IpzbBeL-8wX-UZaSlnG0968XiGsjmPPRxKoFyo6ghhQAwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
در ١٨ دی مردم رشت شهر رو بصورت کامل در کنترل خودشون داشتن بدون اینکه خون از دماغ کسی بیاد.
🔴
ولی در ١٩ دی حرام زاده های حکومتی با آتیش کشیدن بازار باستانی رشت برای به قتل رسوندن مردمی که به اونجا پناه برده بودن و به گلوله بستن مردمی که سلاحی نداشتن، جنایتی راه انداختن که هیچوقت از ذهن این مردم شاد فراموش نمیشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/138007" target="_blank">📅 23:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138006">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
نایب رئیس مجلس: همه راه‌ها را با آمریکا رفتیم و جواب نگرفتیم
🔴
آن‌ها فقط زور می‌فهمد، پس چاره‌ای جز ایستادگی عالمانه و هوشمندانه نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/138006" target="_blank">📅 23:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138005">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0413f576f8.mp4?token=TPIqzM2RdooiA-DiEr5p2yFR-LGPw3nJT7CzDmvemjHfFzbOTDse-LuinSkbS_3je9gkQsqe3NfsMCJtAfCX4orbzOAPejwcaQAsUk2jE9gqnx7xHlMY2c0ODdQpJXhzsFbykZcQD-JBoChbOODA0DNcYaNCtmh1ApJRLzD-eghfN1avFrz8pWhmpkF2wVGHomr_r-8UtT1umdAHBWt6WilF2mGa-5qNn8aztbCnpYC2fYI6GBfrv6vjREtpt0Gt_le96PQV8gK2oiG_azkYYE93fwWisizjjOGNjTJ8i9kYNiPFEvVXAQhnTI4TPizNdrr630JjMfw81xauusGHAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0413f576f8.mp4?token=TPIqzM2RdooiA-DiEr5p2yFR-LGPw3nJT7CzDmvemjHfFzbOTDse-LuinSkbS_3je9gkQsqe3NfsMCJtAfCX4orbzOAPejwcaQAsUk2jE9gqnx7xHlMY2c0ODdQpJXhzsFbykZcQD-JBoChbOODA0DNcYaNCtmh1ApJRLzD-eghfN1avFrz8pWhmpkF2wVGHomr_r-8UtT1umdAHBWt6WilF2mGa-5qNn8aztbCnpYC2fYI6GBfrv6vjREtpt0Gt_le96PQV8gK2oiG_azkYYE93fwWisizjjOGNjTJ8i9kYNiPFEvVXAQhnTI4TPizNdrr630JjMfw81xauusGHAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ گفت: خیلی از جمهوری‌خواهان آدم‌های خوبی هستند. ما حزب بسیار مهربانی هستیم. اما اگر بخواهم صادق باشم،
🔴
شاید نباید این‌قدر مهربان باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/138005" target="_blank">📅 23:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138004">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ترامپ : اون حوضِ زیبای کنار کاخ سفید... یکی اومد با چاقو خرابش کرد. مریضن
🔴
الان داره تعمیر می‌شه و خیلی زود دوباره درست می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/138004" target="_blank">📅 23:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138003">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/190b4a0822.mp4?token=r6VIkZ3ttQd1HRVScb0h_1vltgQ4A-tddOvK2Dxw4mphmfZD0BIX35Yx_RVbom9_Z5vXcVJByhqtLrL7PNvT4sBwOR__GqnqCPM1XI5hpI5eL0Fj79TrfHqdsFtrjJSG-Khl8XoJ6x3CeSdquOk-A_IIgLGzY8ElgMKmPxwoXc9MkHfUlD4iVPW_JSfls6BSZJ_6_Lyh6DAUBG9Z07l1jZt1D1nvrJgOrqkJWBLmq3X9aixTOGtr0YS1Jazmw236Z8g5W8GxzDPdM6r2W3X2XDtkO3dOt0sBCfmw1qKp6f_T8PgDZCsG7w0Pu4ge1FAcz7lhWgQZHfssZNSPaM-t8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/190b4a0822.mp4?token=r6VIkZ3ttQd1HRVScb0h_1vltgQ4A-tddOvK2Dxw4mphmfZD0BIX35Yx_RVbom9_Z5vXcVJByhqtLrL7PNvT4sBwOR__GqnqCPM1XI5hpI5eL0Fj79TrfHqdsFtrjJSG-Khl8XoJ6x3CeSdquOk-A_IIgLGzY8ElgMKmPxwoXc9MkHfUlD4iVPW_JSfls6BSZJ_6_Lyh6DAUBG9Z07l1jZt1D1nvrJgOrqkJWBLmq3X9aixTOGtr0YS1Jazmw236Z8g5W8GxzDPdM6r2W3X2XDtkO3dOt0sBCfmw1qKp6f_T8PgDZCsG7w0Pu4ge1FAcz7lhWgQZHfssZNSPaM-t8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: به طور موقت، تنش‌ها کاهش یافت. اما آن‌ها رفتار مناسبی نداشتند و مجبور شدم دوباره وارد عمل شوم.
🔴
اکنون آن‌ها دوباره رفتار مناسبی دارند. این شبیه به نواختن یک ساز بانجو است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138003" target="_blank">📅 23:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138002">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ترامپ : یه کم ناراحتم چون شاید تا دو سال و نیم دیگه رئیس‌جمهور دیگه‌ای داشته باشید. شاید
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/138002" target="_blank">📅 23:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138001">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/006cb45ccc.mp4?token=AdCfUHPQkuTC77gcro0HGAoGZ6sypcYF0Nogs_PjsLqxESxkhhIhD9iEgnuhkFdOKAqYchNknbybDi0kxwz8l6wVwFOmq0amdH3u_qL96EJ4n-FXbppndkIUCKZyl9XPASh_AwpL1MjnQJWMZ3cysbp_CKf6cUmbN0CgG_bklBqLB2J3hNxdZ3V2FtrKZ6-a3xCBWRBU7CYlOq_FIWlcmvtaMKqVYPqvqxaIoBqxTDIgSW-t8p8Yq1NKSsLat4pYYQx1WPE9JZIjDTDie2PR5AgXZMoIP7W_cSWjbk_byWQCtiur9ujYQu8LcPk-FzN3vsO5BVnHljz02VOIpRHj7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/006cb45ccc.mp4?token=AdCfUHPQkuTC77gcro0HGAoGZ6sypcYF0Nogs_PjsLqxESxkhhIhD9iEgnuhkFdOKAqYchNknbybDi0kxwz8l6wVwFOmq0amdH3u_qL96EJ4n-FXbppndkIUCKZyl9XPASh_AwpL1MjnQJWMZ3cysbp_CKf6cUmbN0CgG_bklBqLB2J3hNxdZ3V2FtrKZ6-a3xCBWRBU7CYlOq_FIWlcmvtaMKqVYPqvqxaIoBqxTDIgSW-t8p8Yq1NKSsLat4pYYQx1WPE9JZIjDTDie2PR5AgXZMoIP7W_cSWjbk_byWQCtiur9ujYQu8LcPk-FzN3vsO5BVnHljz02VOIpRHj7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران گفت:
نمی‌توان آن‌ها را با پول یا امتیاز خرید. باید آن‌ها را شکست داد.
🔴
و ما داریم حسابی آن‌ها را در هم می‌کوبیم. باید ببینیم در نهایت چه پیش می‌آید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/138001" target="_blank">📅 23:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138000">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ترامپ : الان مذاکرات سازنده‌ای در جریانه. ایران می‌گه : لطفاً، لطفاً محاصره‌مون نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/138000" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137999">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1be3db46cf.mp4?token=q96XCCewOVyvD-yXovWl-VRAs4tSwgvCKxAUTN8jnAgAWl8ORyUksClkIeL1mWNugW5jf9LvI3Lq1V3SpjTtBAmFUTlCYUXuC28LuYC_7IkSFJ6vaRlN75j4XbpIZcUZ-YVLniaEUFz5qQ9qqAHl6wxTwObNo3kL_AE732i0JhV7VEIj1C3d6_wnispb9qX2seXvVHsugIonDbtD5937fbMfrO1dx9zVHgPsp8rLiLzMBEy8DNXyoTdJgJ0RLMSwQUjWBqkAWyeBsKk-BXBE92_PGGyTuiKk9zvKvFrHM_WIo57KWm1HHRR-2cvNLqj3swMlYltflE3EHmxxM5BpXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1be3db46cf.mp4?token=q96XCCewOVyvD-yXovWl-VRAs4tSwgvCKxAUTN8jnAgAWl8ORyUksClkIeL1mWNugW5jf9LvI3Lq1V3SpjTtBAmFUTlCYUXuC28LuYC_7IkSFJ6vaRlN75j4XbpIZcUZ-YVLniaEUFz5qQ9qqAHl6wxTwObNo3kL_AE732i0JhV7VEIj1C3d6_wnispb9qX2seXvVHsugIonDbtD5937fbMfrO1dx9zVHgPsp8rLiLzMBEy8DNXyoTdJgJ0RLMSwQUjWBqkAWyeBsKk-BXBE92_PGGyTuiKk9zvKvFrHM_WIo57KWm1HHRR-2cvNLqj3swMlYltflE3EHmxxM5BpXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: مدتی بود که اوضاع کمی آرام شده بود. اما آن‌ها دوباره رفتار مناسبی از خود نشان ندادند، و من مجبور شدم دوباره وارد عمل شوم.
🔴
اکنون، به نظر می‌رسد آن‌ها دوباره رفتار مناسبی از خود نشان می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/137999" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137998">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38d9a0a947.mp4?token=uGnQ6kC5FSIYd3pB-tKTGxCltolyyp44sXzGE4sa2bhZPqwy7NfgaKBHRXy_mLT1ilSiNfhKJ88kOOtQnNtf4SX1BbD4CzV38vLXsI7QvZfFqnoocT81PVf29GcPsZa7dezBnLFnUTgomgWH-9MoB1dky97rkpi64yvlVq0rB2ci0aoyfMmKhbENqLb4DCvB_oM6xNATOkssZqD9CUSm1LfEF9jFmn7Q0ps1KPUvMm8v6PN_9yBcWUUImSlZwChynM2xfeKrsntwo96L0TTMM92_I0xzJFPkRU4gNXJ4MAQQ622cVtiAwy2K5zGCxe3Dmze-RAr3ox8IlQVgR57atg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38d9a0a947.mp4?token=uGnQ6kC5FSIYd3pB-tKTGxCltolyyp44sXzGE4sa2bhZPqwy7NfgaKBHRXy_mLT1ilSiNfhKJ88kOOtQnNtf4SX1BbD4CzV38vLXsI7QvZfFqnoocT81PVf29GcPsZa7dezBnLFnUTgomgWH-9MoB1dky97rkpi64yvlVq0rB2ci0aoyfMmKhbENqLb4DCvB_oM6xNATOkssZqD9CUSm1LfEF9jFmn7Q0ps1KPUvMm8v6PN_9yBcWUUImSlZwChynM2xfeKrsntwo96L0TTMM92_I0xzJFPkRU4gNXJ4MAQQ622cVtiAwy2K5zGCxe3Dmze-RAr3ox8IlQVgR57atg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس جمهور آمریکا:
با وجود علاقه‌ام به رونالد ریگان، او اجازه داد صنعت خودروسازی آمریکا به ژاپن و کشورهای دیگر منتقل شود.
🔴
من در زمینه تجارت، از ریگان بسیار بهتر عمل می‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/137998" target="_blank">📅 23:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137997">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ : همون اتفاقی که توی ونزوئلا افتاد، داره توی ایران هم می‌افته  فقط مردم متوجهش نمی‌شن
🔴
اینا رو نمی‌شه با پول و امتیاز خرید
باید شکستشون داد، و الان هم داریم حسابی شکستشون می‌دیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/137997" target="_blank">📅 23:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137996">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bed1c3e10.mp4?token=AyBUV8eEFBkNRknPxt15LVoBbGg2ab8n3NfEPWhXRc1Gs8OYS-jnfuvCJLz7iIqSYd7CIWChTGVGCZ3HB3A5Pfkx1TaKnRU9Ie6gbYqUKi9e45zUEMXj81G9cowGg3yQwsDLc_XAN6nilTwx4B3Uv6v7znKHfmlMFRf06NCEBvhcc1XMc827Om0CH4WHK6eKsOQTjXmB-2e8h8Pfo42i5AERghKAUIC57Xe8DwDbdMVynI6qfUsos7DEnOFrnQq5XRmf7pTSVhwX7K06B8vplGeERYCGarF8kPTBQSR2_ZceJ5ywlWBMu4jJegUY3RRNovYoA_DJgoS9vbnjmmCVsoOvVCeuQ_vmwnwkdZvZctOV6pK5VWnrPMMyUvvf87IpvTv-q1OayQ22noSalZnX8o1I73PN53MdNMnpa6lyP71Y2p4Tturea1Hi9IiIXZL2x3AyfLaPnIT5dtIXAsRJo0rXDZNYZWSItsPFT1orPBdnG1ZxTtJ_5KTPlH-XeITRghAeGsCe2ORdEO3aDSCrgniR0hIdyCFkpmEz6Tq0ErLzEWV7VAdYxRsn_URq6fyoFyZIkCxb-N1YY8cWnvfBx-bX-qduEGbSbcpeJM-2ISEiBSW4jmB6pZAcYVtFkvn1Pr96v_9TY_ecYe_dO2wlQcyFVaHMjc9il9HItmoISfs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bed1c3e10.mp4?token=AyBUV8eEFBkNRknPxt15LVoBbGg2ab8n3NfEPWhXRc1Gs8OYS-jnfuvCJLz7iIqSYd7CIWChTGVGCZ3HB3A5Pfkx1TaKnRU9Ie6gbYqUKi9e45zUEMXj81G9cowGg3yQwsDLc_XAN6nilTwx4B3Uv6v7znKHfmlMFRf06NCEBvhcc1XMc827Om0CH4WHK6eKsOQTjXmB-2e8h8Pfo42i5AERghKAUIC57Xe8DwDbdMVynI6qfUsos7DEnOFrnQq5XRmf7pTSVhwX7K06B8vplGeERYCGarF8kPTBQSR2_ZceJ5ywlWBMu4jJegUY3RRNovYoA_DJgoS9vbnjmmCVsoOvVCeuQ_vmwnwkdZvZctOV6pK5VWnrPMMyUvvf87IpvTv-q1OayQ22noSalZnX8o1I73PN53MdNMnpa6lyP71Y2p4Tturea1Hi9IiIXZL2x3AyfLaPnIT5dtIXAsRJo0rXDZNYZWSItsPFT1orPBdnG1ZxTtJ_5KTPlH-XeITRghAeGsCe2ORdEO3aDSCrgniR0hIdyCFkpmEz6Tq0ErLzEWV7VAdYxRsn_URq6fyoFyZIkCxb-N1YY8cWnvfBx-bX-qduEGbSbcpeJM-2ISEiBSW4jmB6pZAcYVtFkvn1Pr96v_9TY_ecYe_dO2wlQcyFVaHMjc9il9HItmoISfs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :
مه‌هی‌او!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/137996" target="_blank">📅 23:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137995">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0eae498d1.mp4?token=JoMI777w2TIuUulEWqlFs2n6meI8jihl1uNYU0GdHUXsXOD8tiAUUztNX1kLZowBRQnH0F4VbSzLveLiO7Y8OIob18QaA9AFyX8j_GBEHnPQe46EMMNpKZ0fboN4QU0CJdbVS64TSjhshsmhUWQynv_wfAJaurxBPGn3bFDqeTQLtLjJTc_TZd9dIxa-jmkkDpn63UFtWjPwhfTeBQmFwIx-4vv-dznFA8FIG6T4zu83h-FThNoRStQ-p0R1-8Vk04xTvaRm3Rylz9eERmvaXz-dFDAWMMOU3ZWXVtGjkqlE8xNaeh5OFxA3WOLL65b16dM4qFPQIwpk7sIiVPB1zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0eae498d1.mp4?token=JoMI777w2TIuUulEWqlFs2n6meI8jihl1uNYU0GdHUXsXOD8tiAUUztNX1kLZowBRQnH0F4VbSzLveLiO7Y8OIob18QaA9AFyX8j_GBEHnPQe46EMMNpKZ0fboN4QU0CJdbVS64TSjhshsmhUWQynv_wfAJaurxBPGn3bFDqeTQLtLjJTc_TZd9dIxa-jmkkDpn63UFtWjPwhfTeBQmFwIx-4vv-dznFA8FIG6T4zu83h-FThNoRStQ-p0R1-8Vk04xTvaRm3Rylz9eERmvaXz-dFDAWMMOU3ZWXVtGjkqlE8xNaeh5OFxA3WOLL65b16dM4qFPQIwpk7sIiVPB1zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:دولت دیوانهٔ بایدن کمونیستی بود.
خودِ بایدن نه. آن‌ها به جو گفتند:
"جو، بیا کمونیست شو."
او هم گفت:
"اصلاً کمونیست یعنی چه؟"
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/137995" target="_blank">📅 23:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137994">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ خطاب به یکی از معترضان در میشیگان گفت
:
او یک کمونیست است. ما در حال رقابت با کمونیست‌ها هستیم.
ما با اختلاف زیادی پیروز خواهیم شد.
می‌بینید آن‌ها چه می‌خواهند بکنند؟
آن‌ها می‌خواهند خانه‌هایتان را بگیرند.
آن‌ها می‌خواهند پولتان را بگیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/137994" target="_blank">📅 23:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137993">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8546f48c6c.mp4?token=jCx9CR15TYhBTe35mYgbYBJKwd3gLJcyUvZ6al3r4pGZTvbez1ZSSSjOiB01MyXfLzX4nYoSFL3t8ra5Aa6vaEULVI7su9QS7RvvSqr4tq8XUDNgvo9wyvlA78Ge7Xc0Zrx8yOoH2-YjcScjHpQ1Q3bymkvyw-nd82cnFAZmrQFYV9jCDctWVFOBxMCzVzEi1TEtbiyIyn0oeHJm7VFwwGCbRpqtmgxpsYJ-xadj2y06oIPY5ZTO0_PeoVhxhCfeGv2A0u05OX4EFRSS72UubtcL3lPayBR1beCVmpNkeBzJ-TXMUYhg9sfAhHsJBZcnffERwJjwrtMwU9lKGYq9HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8546f48c6c.mp4?token=jCx9CR15TYhBTe35mYgbYBJKwd3gLJcyUvZ6al3r4pGZTvbez1ZSSSjOiB01MyXfLzX4nYoSFL3t8ra5Aa6vaEULVI7su9QS7RvvSqr4tq8XUDNgvo9wyvlA78Ge7Xc0Zrx8yOoH2-YjcScjHpQ1Q3bymkvyw-nd82cnFAZmrQFYV9jCDctWVFOBxMCzVzEi1TEtbiyIyn0oeHJm7VFwwGCbRpqtmgxpsYJ-xadj2y06oIPY5ZTO0_PeoVhxhCfeGv2A0u05OX4EFRSS72UubtcL3lPayBR1beCVmpNkeBzJ-TXMUYhg9sfAhHsJBZcnffERwJjwrtMwU9lKGYq9HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ گفت:
من بیشتر از پدر و مادرتان برای شما کار کرده‌ام.
من بهتر از پدر و مادرتان با شما رفتار کرده‌ام.
و خودِ آن‌ها هم با من موافق خواهند بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/137993" target="_blank">📅 22:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137992">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c3ad23df.mp4?token=oE9HHHoMUojc8C_qIaSKxhxi0jpbCUFqAdtwjRXiIQsy8-jDbVOHY8qxfP5bWMNPf00TtRTsiyjO5CTKUR5lRhUSNLdiiWA2hMby7SIKLVC7O-KGc09RROKqduwKiaarv1jX_KTRHVRggCTif-0UWUuNfimAzDAPobMKsYCY3IJparWi_qDIn_4yryWeXrfJgKIrvREAxRHwRhPHbwMt37IFFZ344w9aJ67j8zB8QhfF6ucSuUnFWCtZ_qH5jCTWlqoce6GwZpSM8zfMekfCdumi_EohQPGEhMkrmzhQ90-wpX8SGLUbDtDH7xtykrCtV8Fa6N8mIPycvCuu2pIy_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c3ad23df.mp4?token=oE9HHHoMUojc8C_qIaSKxhxi0jpbCUFqAdtwjRXiIQsy8-jDbVOHY8qxfP5bWMNPf00TtRTsiyjO5CTKUR5lRhUSNLdiiWA2hMby7SIKLVC7O-KGc09RROKqduwKiaarv1jX_KTRHVRggCTif-0UWUuNfimAzDAPobMKsYCY3IJparWi_qDIn_4yryWeXrfJgKIrvREAxRHwRhPHbwMt37IFFZ344w9aJ67j8zB8QhfF6ucSuUnFWCtZ_qH5jCTWlqoce6GwZpSM8zfMekfCdumi_EohQPGEhMkrmzhQ90-wpX8SGLUbDtDH7xtykrCtV8Fa6N8mIPycvCuu2pIy_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ
:
من رونالد ریگان را دوست داشتم، اما او اجازه داد صنعت خودروسازی ما به ژاپن و کشورهای دیگر منتقل شود.
ما ریگان را دوست داریم، اما در زمینه تجارت، ترامپ خیلی بهتر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/137992" target="_blank">📅 22:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137991">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/137991" target="_blank">📅 22:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137990">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/137990" target="_blank">📅 22:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137989">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
قرارگاه مرکزی خاتم‌الانبیا:
آمریکا در تداوم شرارت و ناامنی در منطقه و به دنبال اجرای محاصره غیرقانونی دریایی ایران، طی سه روز گذشته اقدام به تهدید شناورها و کشتی های تجاری و نفتکش ایران در آب های ساحلی و سرزمینی کشور ما نموده است.
🔴
هشدار می‌دهیم این اقدام آمریکا به منزله توسعه جنگ در منطقه تلقی می گردد و همانطور که نیروهای مسلح جمهوری اسلامی ایران در میدان عمل ثابت نمودند هرگونه تهدید و شرارت ارتش تروریست آن کشور را بی پاسخ نمی گذارند و با آن برخورد خواهند نمود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/137989" target="_blank">📅 22:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137988">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41d2424e0d.mp4?token=MVf0gUC131muOdezlWJjeQHheTD5aXaq_qx0S6a-8q7Yk54pnwNAPFloz4PMjZLIK9XLfrJA6wyNDHjn_zPfCZKyJyuHdCnggm-Oj3btqeJrmDWnRApwgRytgRMdAZcCqmST-Io-aPWtOYfulIMNgPBiG8lsfe78-Yhel5ggu3HevwHnQbZ-V57p5EoH7Xs5U5PRz9o22AtSGoZKsHfD7lUxFY5hIchlKhyD3mlu--kLLxPm8HKahQDU6YceYqDoqKuX9yRqNRjwvSJp0eb5VXG_ZZIdEYvA8GQSAUk1JfJo09TdTnavLxlsyWNL6k_hne2eCdqSISnZ-abDk6pCYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41d2424e0d.mp4?token=MVf0gUC131muOdezlWJjeQHheTD5aXaq_qx0S6a-8q7Yk54pnwNAPFloz4PMjZLIK9XLfrJA6wyNDHjn_zPfCZKyJyuHdCnggm-Oj3btqeJrmDWnRApwgRytgRMdAZcCqmST-Io-aPWtOYfulIMNgPBiG8lsfe78-Yhel5ggu3HevwHnQbZ-V57p5EoH7Xs5U5PRz9o22AtSGoZKsHfD7lUxFY5hIchlKhyD3mlu--kLLxPm8HKahQDU6YceYqDoqKuX9yRqNRjwvSJp0eb5VXG_ZZIdEYvA8GQSAUk1JfJo09TdTnavLxlsyWNL6k_hne2eCdqSISnZ-abDk6pCYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرگزاری عبری زبان
: ارتش اسرائیل با احتمال بالا ارزیابی می‌کند که پهپادهایی که صبح امروز در نزدیکی بحر المیت و هفته گذشته در کوه هرمون سرنگون شدند، توسط گروه‌های شیعه در عراق شلیک شده بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/137988" target="_blank">📅 22:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137987">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHh3tBYvWCi3p5zq9c75mwn8r6h5G16IMpHwQSWJLalfrkX4qrphYOwiFE73rSIk-6B0oX2otnPW3JiUhKeLBXfPLypBNIkqPmgTby1jsG4HNfyV9u2H0QbygERr9CLVLqzw0JKbVDRwTWAnE4NZMpj7Hloxnmv_5a72y9kdFZ3uKis5sPH3Sxjr1HMpisoDse7pgT_3vo_guNzhogrjFfl-C_8RoOhmuetrq7XWt1s7jIlnSdmVu5kUSZIjsAZ5R3a5OFquA9oplivMxw4jbVkMJVHeISqnDBrT8LSDwO3wCKpMQz3ywtxmqbj7fp26ZnJMsrPXSdLntcx-E1MIEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی:
مراقب باشید پاسخِ احتمالی به اوکراین، کل اروپا را همراه با آمریکا علیه ایران بسیج نکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/137987" target="_blank">📅 22:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137986">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAZZXs2sN3UoIAadw4HjtJCPyZgzLjjfxM7bY9uk2b61YM62UhHI-Jm2B1lYLwNMT-6FS1UQUQ6-60JPijtWpoeGpKKXEdaKM_5rO02XASJupUa49QC10_2UJqeFP_3y1Rq9dSgBBuvMdiy7R3-4M7r9Jo9LcBKgjR_a3Fi1uVEX862YrjpWGgf1IwCS-_nmxlzjECuSLltyKDic4wSflSPfOJR1AyIu_i7RAiu77MR5kPSATXK4TAUpLtgFOn8XaWrBkplsSx3FwUinYOKwCUEN5tpu6vtbZll2jQFtUUgRa9cFpDrJuMIYhnIJKXdwfEsX7uisSwJXSBd0lIsZrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقام آمریکایی به الحدث:
مذاکرات با ایران جدی است و ممکن است امروز شاهد پیشرفتی باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/137986" target="_blank">📅 22:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137985">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
مقامات آمریکایی: مذاکرات ترامپ و نتانیاهو به موضوع ایران و توافقنامه ابراهیم اختصاص دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/137985" target="_blank">📅 22:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137984">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
کانال ۱۲ عبری: نتانیاهو در دیدار با ترامپ اطلاعات حساسی را در رابطه با ایران به او ارائه خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/137984" target="_blank">📅 21:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137983">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2-lM9gal3hJWUnrlHT9gSBxKA1XWFlLeN8kLYzn--G4M8H5Mq6vqGPBYhU31LpvTORfs8xvfPxwDrttESYQAI8aEemMky5VnlnuTOomR3I7JJnhmmgrAl6NwX6vr7qv_BNMkyX7yQl9Z9_sPY9Eoo0PTKNEzEepG3q67H1p1WkGtpmhXwFtvNwI5l9he4U45Hapa6V6pkPlbJeaKbTUzP40lUkLM6-z3J2oTciEwGdnJk_vC3h0niEZWLt-EpW66XHVbTi3hhtkpnoAtZkn4dVDK-jYyVwJO7XdR23MJts1GWMT5Rlf4CZezr9d4Mvu4feAdduzsjri4m92s85uUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعاتی پیش نفت به قیمت ۸۸ دلار کاهش پیدا کرد
🔴
۱۲ درصد کاهش قیمت در ۲۴ ساعت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/137983" target="_blank">📅 21:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137982">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
رویترز ،مقام آمریکایی : ترامپ با نتانیاهو درباره ایران و توافق‌های ابراهیم صبحت میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/137982" target="_blank">📅 21:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137981">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
مکرون: اسرائیل فورا باید از تمام مناطق لبنان عقب نشینی کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/137981" target="_blank">📅 21:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137980">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fa2zCv-P7Gpf1rVhuNqXUqr9xB_qYP-UVmgpO7cm1TZ24RG-j9jk1VW8MPEk6WDy6i26clQfH1OAXMt3LdNMC5q5lPULsaRUhqSGrQtUeJY75VTEGWWdfTN4muZQPYcGj9rqg0GO5gKiiS_UhaaYzjUwhSvXRyj7jlHMV4Jtd-MrPudbPTwDjx2FuuOPCdFNCATaAWTfSb4bBEGcMSv2JjfYAgWExzzz8TVcfWowl1W70mzs9zpon-4AkG7D6PHClVjrsTkvB-00gijsKfIe9dv3i_yWDVKSeE4Rzq8gFEYz7SGoM2fYv9kT0fWWv0y0OtXjaQGKFjdk5_8_h3pZ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقام آمریکایی به الحدث: مذاکرات با ایران جدی است و ممکن است امروز شاهد پیشرفتی باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/137980" target="_blank">📅 21:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137979">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
دفتر نخست وزیر عراق: الزیدی دستور تحقیقات امنیتی در مورد آنچه در بیانیه عربستان سعودی در مورد هدف قرار دادن آن با پهپاد از خاک عراق آمده است را صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/137979" target="_blank">📅 21:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137978">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
شبکه i24 اسرائیل : نتانیاهو در دیدار با ترامپ با فشارهای قابل توجهی در مورد چندین موضوع از جمله سوریه، غزه و لبنان روبرو خواهد شد. این دیدار بسیار مهم است و ما امیدواریم که راه را برای عملیات مشترک اسرائیل و آمریکا علیه ایران هموار کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/137978" target="_blank">📅 21:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137977">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
استقرار نیروی هوایی آمریکا در قطر و عربستان دوباره تغییر کرد!
🔴
در پایگاه العدید قطر، تمامی هواپیماهای سوخت‌رسان و ترابری بار دیگر از پایگاه خارج شده‌اند.
🔴
در پایگاه پرنس سلطان عربستان، هواپیماها به آرایش زمان جنگ بازگشته‌اند و سه فروند هواپیمای آواکس E-3 نیز دوباره در این پایگاه مستقر شده‌اند.
🔴
به نظر می‌رسد ایالات متحده در حال جابجا کردن هواپیماهای بزرگ و راهبردی خود از پایگاه‌های آسیب‌پذیرتر نسبت به حملات ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/137977" target="_blank">📅 21:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137976">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd0b82ccc7.mp4?token=EH9X4HxnwaI_D8EE7sPpCOjeo697j4EFOiTnSMDp9l5WuVpUw51zciTk2a1bzX1Y6q-lk-5jY5A2B0dyf_5_bSfhbJ140BtDSUNxsmmXmMa72P1LQbNW5uuz3omDlJhgvvBkFVqfcYxZ0GoCIiFsUtf3Vp5uM4fHeP1NxInrFqH_CRIzXN1Zdp17_NFAgNB5CzOkC1yEhEAZIyCbyYZBjNytBY7UzsUHAoJYUQFai7IIKy9av5Y-QtISe1UZCoCcV23LKBMi6gWEkbxoz72_dtP_O-ZRX_5nHBZ7D6FC65L_UMSllm3MQx92l1gPpC49MWYIrM4PAtk9l6gUy0KHuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd0b82ccc7.mp4?token=EH9X4HxnwaI_D8EE7sPpCOjeo697j4EFOiTnSMDp9l5WuVpUw51zciTk2a1bzX1Y6q-lk-5jY5A2B0dyf_5_bSfhbJ140BtDSUNxsmmXmMa72P1LQbNW5uuz3omDlJhgvvBkFVqfcYxZ0GoCIiFsUtf3Vp5uM4fHeP1NxInrFqH_CRIzXN1Zdp17_NFAgNB5CzOkC1yEhEAZIyCbyYZBjNytBY7UzsUHAoJYUQFai7IIKy9av5Y-QtISe1UZCoCcV23LKBMi6gWEkbxoz72_dtP_O-ZRX_5nHBZ7D6FC65L_UMSllm3MQx92l1gPpC49MWYIrM4PAtk9l6gUy0KHuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از کشتی ایرانی که مورد حمله اوکراین قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/137976" target="_blank">📅 21:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137975">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
بلومبرگ: ایران و عمان درباره راه حلی برای مسئله تنگه هرمز گفتگو می‌کنند. یکی از پیشنهاداتی که مطرح شده، باز کردن مسیر میانی تنگه، در آب‌های بین‌المللی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/137975" target="_blank">📅 21:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137974">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afba5829f9.mp4?token=tJq_aeNZBRAHYeZufqtF_fawZv_KVj6CVew33fV1bNOZacfa0aUSFHos9_9MqCXZ58LMDgEjseJrFobpOUUCPImtmAOxR4W0aKPmxMeGp6assKqZEEtsnSn09jPfEpDtrC7pSa4qvWJC2ASfl3eS4IhgFrZNCTtL1MwHfjc7LINpk7uNRxRvVTbxmCqAr2WKOjqLakSdw7zb6aUI7ILDOVSg7olY3_um9NnkhDUldGQ-cwv2BXtWH2uwL0EjqAZKjw5_Dt3FcVNOpvq-bG2fxVQVlv0XB4VI-J8XwRQ42rSxDDesDZDGhgKBuguG8PjvDmcVpO79gXPksymRQp79rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afba5829f9.mp4?token=tJq_aeNZBRAHYeZufqtF_fawZv_KVj6CVew33fV1bNOZacfa0aUSFHos9_9MqCXZ58LMDgEjseJrFobpOUUCPImtmAOxR4W0aKPmxMeGp6assKqZEEtsnSn09jPfEpDtrC7pSa4qvWJC2ASfl3eS4IhgFrZNCTtL1MwHfjc7LINpk7uNRxRvVTbxmCqAr2WKOjqLakSdw7zb6aUI7ILDOVSg7olY3_um9NnkhDUldGQ-cwv2BXtWH2uwL0EjqAZKjw5_Dt3FcVNOpvq-bG2fxVQVlv0XB4VI-J8XwRQ42rSxDDesDZDGhgKBuguG8PjvDmcVpO79gXPksymRQp79rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
: روسیه تجهیزات نظامی زیادی به ونزوئلا داد.
🔴
ونزوئلا تقریباً تمام تجهیزاتش روسی بود.
🔴
ولی تهش چی‌شد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/137974" target="_blank">📅 20:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137973">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا اعلام کرد در چارچوب برنامه نوسازی نظام تحریم‌ها، نام ۸۴ فرد و نهاد را از فهرست‌های تحریمی حذف کرده است./همچنین چند کشتی با پرچم پاناما و ایران نیز از فهرست حذف شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/137973" target="_blank">📅 20:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137972">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ : اوباما مهمات نخرید
ما مقدار کمی داشتیم و من دستور ساختش رو دادم
🔴
وقتی من رفتم، بایدن مقدار زیادی از اون رو به اوکراین داد؛ اعدادی که قبلاً کسی ندیده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/137972" target="_blank">📅 20:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137971">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dca0922d5.mp4?token=pGq8SW448-yJoocLiPWJsqTajuAtU-nRZuMzaywYnqfJ5S2uXHgehjunpvaoZmX18Bu3KRvHoLt83J4Ax559c39BXLTO3g0aia_cBbgmfsBBZhLYGr2Yiv6ZWLi7hwFlTNYysLe9peFbe2B11oDrzTvfRHNz6IoIfDfVGeVRYP-hrbx6S1m81ezmoSMdCSBIOdXj_ZU53Si89_UeqB0i6LPnt8YcioJBX8TlTyGVPxpd0dLBcCAwcsZV-elDMLAiMVowEZ6DxSkNPgqwAGJCbzvdY8b5QdhBpWF6wtVBFLugRPdEdRAqUuKufAX2Pn1416t4vz7s9R9wSu4NfSk_sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dca0922d5.mp4?token=pGq8SW448-yJoocLiPWJsqTajuAtU-nRZuMzaywYnqfJ5S2uXHgehjunpvaoZmX18Bu3KRvHoLt83J4Ax559c39BXLTO3g0aia_cBbgmfsBBZhLYGr2Yiv6ZWLi7hwFlTNYysLe9peFbe2B11oDrzTvfRHNz6IoIfDfVGeVRYP-hrbx6S1m81ezmoSMdCSBIOdXj_ZU53Si89_UeqB0i6LPnt8YcioJBX8TlTyGVPxpd0dLBcCAwcsZV-elDMLAiMVowEZ6DxSkNPgqwAGJCbzvdY8b5QdhBpWF6wtVBFLugRPdEdRAqUuKufAX2Pn1416t4vz7s9R9wSu4NfSk_sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پولی که از ونزوئلا به دست می‌آید، صرف چه چیزی می‌شود؟
🔴
ترامپ: صرف اداره کشور می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/137971" target="_blank">📅 20:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137970">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f19b14e9.mp4?token=r-bTSsN2COOCs1eDfRs-XAlQLMC2rcQDNkW-cUnvt3SVeszjGTJ8Y4tzB7q53bPjrtIoZf7couDAN7vKR-0drEYyfHDijH6NWXk3M4rmwwQFQMcFtt9_3IQPqNV6Yiij3P_mEnv2A2KWN4b77StQ8FHlwSnaIuyJpvzcjI611tSU0bWy_enEcDXx4AdshssioRX6Ukr-xL4SfpwTwDHZntWF3ZPxT_jRkgEyDfb7PgRzyKUPX5KCHWBpaC2h5DJFASRqLW5TdcXrHTr8H-bBOUZcxqbY1Xm1AKrX8lSDEKn42MiJq9p9fnMqksYQ8uisq4p-H8TnTW_ST1EkdvzxtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f19b14e9.mp4?token=r-bTSsN2COOCs1eDfRs-XAlQLMC2rcQDNkW-cUnvt3SVeszjGTJ8Y4tzB7q53bPjrtIoZf7couDAN7vKR-0drEYyfHDijH6NWXk3M4rmwwQFQMcFtt9_3IQPqNV6Yiij3P_mEnv2A2KWN4b77StQ8FHlwSnaIuyJpvzcjI611tSU0bWy_enEcDXx4AdshssioRX6Ukr-xL4SfpwTwDHZntWF3ZPxT_jRkgEyDfb7PgRzyKUPX5KCHWBpaC2h5DJFASRqLW5TdcXrHTr8H-bBOUZcxqbY1Xm1AKrX8lSDEKn42MiJq9p9fnMqksYQ8uisq4p-H8TnTW_ST1EkdvzxtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چرا می‌خواهید سناتورهای آمریکا در واشنگتن بمانند؟ نباید بروند برای تبلیغات انتخاباتی؟
🔴
ترامپ: چه سؤال احمقانه‌ای!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/137970" target="_blank">📅 20:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137969">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f5ceb040.mp4?token=UGPa1M8FSkMHugDXGsG4bLrQS4GoVuSRT1qThLcDVSdk9GCQWZpyAiHjkQ10E4IDKrLLkDX7JPUm4KDgg85-hsqSUPNPQNP_ICAe2fjumpXEcgjvoQCoOhw_bMVCibppbj9166pyAmnrMQ51FZn9XEtVfllQ90blVUTL0_H6icep_jGoIIo8TOhv9RIliwPTnBmb4IxJuKYBsfY8t569j6XVtvM2AgOYEp-kGi2s-UiLV3b4xMv7G4AAzwvUcfXl1Pt2FQ6RQ7slVMLHtiBWDK9AZDM1yPyHt8-rstSHrx298hSTUWxrzKAzho774oSpTK3JbUVJKIihki8cipCAiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f5ceb040.mp4?token=UGPa1M8FSkMHugDXGsG4bLrQS4GoVuSRT1qThLcDVSdk9GCQWZpyAiHjkQ10E4IDKrLLkDX7JPUm4KDgg85-hsqSUPNPQNP_ICAe2fjumpXEcgjvoQCoOhw_bMVCibppbj9166pyAmnrMQ51FZn9XEtVfllQ90blVUTL0_H6icep_jGoIIo8TOhv9RIliwPTnBmb4IxJuKYBsfY8t569j6XVtvM2AgOYEp-kGi2s-UiLV3b4xMv7G4AAzwvUcfXl1Pt2FQ6RQ7slVMLHtiBWDK9AZDM1yPyHt8-rstSHrx298hSTUWxrzKAzho774oSpTK3JbUVJKIihki8cipCAiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آیا چین در حال دزدی از آمریکا است؟
🔴
پرزیدنت ترامپ: آن‌ها ما را زیر نظر دارند، و ما هم آن‌ها را زیر نظر داریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/137969" target="_blank">📅 20:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137968">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bea6d733a8.mp4?token=m4swiawRaaUJ7CGDsssXUifR5uFpBAgISKdU-PEBeA51uBBe6zOvggqrgatI-6STpViQEvZxVkzI5dfPD2qZCVutPemRkZ0jjg2zDKLI8ZKWdAmBgq6EEkzBT5C2Lpif_j1YG00Bv1l-b6ALQS5a4OoPA5wf6bZ2wdUZc24X7ZIWSEs0iNOEzwtZqDfjMrYd5ovpt3e6HMzlc4GYvlQ3NkSQq2lqcV6U8fhsboNG8ZUYPFuXAnXmaWZOH_iVOvBVxi-5QiigbClxkzmqymaa-fdf5NF0CoBC6AawW92jJV7MYuwfrx1U4mwllS_A-3lszH5-LnYAGWbCxwsWgbmo9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bea6d733a8.mp4?token=m4swiawRaaUJ7CGDsssXUifR5uFpBAgISKdU-PEBeA51uBBe6zOvggqrgatI-6STpViQEvZxVkzI5dfPD2qZCVutPemRkZ0jjg2zDKLI8ZKWdAmBgq6EEkzBT5C2Lpif_j1YG00Bv1l-b6ALQS5a4OoPA5wf6bZ2wdUZc24X7ZIWSEs0iNOEzwtZqDfjMrYd5ovpt3e6HMzlc4GYvlQ3NkSQq2lqcV6U8fhsboNG8ZUYPFuXAnXmaWZOH_iVOvBVxi-5QiigbClxkzmqymaa-fdf5NF0CoBC6AawW92jJV7MYuwfrx1U4mwllS_A-3lszH5-LnYAGWbCxwsWgbmo9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : چقدر دیگه به ایران فرصت می‌دید؟
🔴
ترامپ : من زمان زیادی دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/137968" target="_blank">📅 20:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137967">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff0e22e8d.mp4?token=QVsl9Rc4r-pAS3CfYrPBQiKBMcSKuW1V7UQJmpDJ47NK2IytCCGb2uhWGvd65qNQziPzx-Q5uQ_-u29bDScUbH0hgHEmw0AFO0Vcr8yHffHFL5QIAwrI-t9NJo4vsMDQI1vzGq4ceUu1_prK_0tEpYdgeyiON49-AHAKFX4RyIu0B76vyBDtAycN9fLH7FKTzFalUPqYjjYKu1X1jbbSeJRTFbEgvZrOEPhSTrntKi1gEBCATqV5Se8WE8NVF7BNJrkjgdMinz5l6OzBgKPSgSzyE9dXb4fBoYLyKCS2_j7S_vvcVqNiSv1xkNUWLTfbNCZn8HHTyz2n8oETfgIy0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff0e22e8d.mp4?token=QVsl9Rc4r-pAS3CfYrPBQiKBMcSKuW1V7UQJmpDJ47NK2IytCCGb2uhWGvd65qNQziPzx-Q5uQ_-u29bDScUbH0hgHEmw0AFO0Vcr8yHffHFL5QIAwrI-t9NJo4vsMDQI1vzGq4ceUu1_prK_0tEpYdgeyiON49-AHAKFX4RyIu0B76vyBDtAycN9fLH7FKTzFalUPqYjjYKu1X1jbbSeJRTFbEgvZrOEPhSTrntKi1gEBCATqV5Se8WE8NVF7BNJrkjgdMinz5l6OzBgKPSgSzyE9dXb4fBoYLyKCS2_j7S_vvcVqNiSv1xkNUWLTfbNCZn8HHTyz2n8oETfgIy0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : اونا درخواست دیدار کردن اگه ما خوب عمل نکرده بودیم، اونا درخواست ملاقات نمی‌کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/137967" target="_blank">📅 20:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137966">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ترامپ درباره ترکیه : ترکیه یه کشور خیلی قدرتمنده؛
🔴
فوق‌العاده‌ست و یه ارتش خیلی بزرگ داره، ارتشش هم تجهیزات خیلی پیشرفته‌ای داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/137966" target="_blank">📅 20:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137965">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6384fa75fc.mp4?token=M5sZa95D983ft3cxd8aIi0pEQ0AOHsY2WZhSwE724s2ZogC9KrYjFCOA5l-d8cX__U_Q0pKQ8ib8pw8PeLxUUvJqa77chqBTg_QwdU6FrqapnFTaZHZu5f425QynikHn0agU3cT1y_KZD8DAtQfh-7wPW4CQ6Co7EI0Mdy-73K1xrQvcWLIGP5-3ZVvoZquP7mc4Q_cCdWak2BrNK7MWMBBHsg7IbbthtHYl58Fi-RpJLxdcmy2SiW8pXL7puuxzfDf2Vgnu9xgP__vTUGUwNKT5ujOTYN6VTSTOIY10YLUTA_8aM7VODo7JeuHtrS_XOF-GSyNc6RK1uUy1QTCmBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6384fa75fc.mp4?token=M5sZa95D983ft3cxd8aIi0pEQ0AOHsY2WZhSwE724s2ZogC9KrYjFCOA5l-d8cX__U_Q0pKQ8ib8pw8PeLxUUvJqa77chqBTg_QwdU6FrqapnFTaZHZu5f425QynikHn0agU3cT1y_KZD8DAtQfh-7wPW4CQ6Co7EI0Mdy-73K1xrQvcWLIGP5-3ZVvoZquP7mc4Q_cCdWak2BrNK7MWMBBHsg7IbbthtHYl58Fi-RpJLxdcmy2SiW8pXL7puuxzfDf2Vgnu9xgP__vTUGUwNKT5ujOTYN6VTSTOIY10YLUTA_8aM7VODo7JeuHtrS_XOF-GSyNc6RK1uUy1QTCmBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما توی همه زمینه‌ها و در همه چیز، از همه جلوتر هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/137965" target="_blank">📅 20:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137964">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec41e14555.mp4?token=IrVsqkaVoFSBG85hwW8S1XHf1TgmKlqjgo-083NF6gltOMQmcmZdEtfrFDp3VxLXiZL2jLY6O-dQMWJnrYU0TsLWWd9h3GCtj_Kjj5ZhBrnqRU4h2c9vb-LiEGxCEqueUIOlLbofvs0C9lwW2WTtinanFVshW9DcGl51-Ina5NrufkcuW9p6CgZkoMdmc634jMfjrj7L-kDHehJeRGVQMuNRxw3yo7t72CVKeuWie2-0yiMhbZXrd2GPQQtVx-elujf-do58pu1OQ6IDNAbfKWxKroYlyh6my1OXJhElUMDZEF4XKw259ZxOfNguktrRSTWlyovrI56FAKN8EoeP5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec41e14555.mp4?token=IrVsqkaVoFSBG85hwW8S1XHf1TgmKlqjgo-083NF6gltOMQmcmZdEtfrFDp3VxLXiZL2jLY6O-dQMWJnrYU0TsLWWd9h3GCtj_Kjj5ZhBrnqRU4h2c9vb-LiEGxCEqueUIOlLbofvs0C9lwW2WTtinanFVshW9DcGl51-Ina5NrufkcuW9p6CgZkoMdmc634jMfjrj7L-kDHehJeRGVQMuNRxw3yo7t72CVKeuWie2-0yiMhbZXrd2GPQQtVx-elujf-do58pu1OQ6IDNAbfKWxKroYlyh6my1OXJhElUMDZEF4XKw259ZxOfNguktrRSTWlyovrI56FAKN8EoeP5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : آیا نتانیاهو می‌خواد شما با ایران به توافق برسید یا می‌خواد حملات ادامه پیدا کنه؟
🔴
ترامپ : نتانیاهو آدم خیلی خوبیه. ایران الان فقط ۸ درصد از قدرت قبلی خودش رو داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/137964" target="_blank">📅 20:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137963">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ترامپ: ما هزینه جنگ ونزوئلا را چندین برابر پس گرفتیم.
🔴
همین اتفاق برای ایران هم خواهد افتاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/137963" target="_blank">📅 20:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137962">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ دوباره اعلام کرد: اگه من نبودم اسرائیل وجود نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/137962" target="_blank">📅 20:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137961">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ترامپ: ما مهمات زیادی از انواع مختلف داریم. بایدن مقدار زیادی از آن‌ها را به اوکراین داد، و ما الآن در حال جبران و افزایش دوباره ذخایر هستیم.
ما به قدری مهمات داریم که تحت هیچ شرایطی نمیتونیم تمومش کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/137961" target="_blank">📅 20:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137960">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/794142c13b.mp4?token=FsF__0J-urO1z3_BC6dTCxWpo6C0tg0_l2AFJ7aiwoU8oXOrTprWpKLLYnlaDe8Q6lMwtnbbdL_tGebaT9H-eP4RD7YgKEgXm6OKTXACiEVY8Aj3mHXRVD92bkXbL4lJgcrd3u9vxQlhWMKJ-Fv_kfKpCExe1n6HpUbPdCgiLry3-6JPAzd5iDxLtOc3MIOoDJixJSuZelaPkRRZG5m38B8-OMBqA2fH0AUdNiFSFCmQjEkZoBMSH9nDiADnhnQz_ruu4PZjx3nAXlzgV5we6SXmRhierNNlKpyB7afghK26xn0hRla6kYCg3bsZVHhsSAtbPLDhM9XSVuEFmBblHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/794142c13b.mp4?token=FsF__0J-urO1z3_BC6dTCxWpo6C0tg0_l2AFJ7aiwoU8oXOrTprWpKLLYnlaDe8Q6lMwtnbbdL_tGebaT9H-eP4RD7YgKEgXm6OKTXACiEVY8Aj3mHXRVD92bkXbL4lJgcrd3u9vxQlhWMKJ-Fv_kfKpCExe1n6HpUbPdCgiLry3-6JPAzd5iDxLtOc3MIOoDJixJSuZelaPkRRZG5m38B8-OMBqA2fH0AUdNiFSFCmQjEkZoBMSH9nDiADnhnQz_ruu4PZjx3nAXlzgV5we6SXmRhierNNlKpyB7afghK26xn0hRla6kYCg3bsZVHhsSAtbPLDhM9XSVuEFmBblHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آیا شما و نتانیاهو درباره ایران هم‌نظر هستید؟
🔴
دونالد ترامپ: یک اختلاف‌نظر کوچک بین ما وجود دارد، اما در کل تقریباً هم‌نظر هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/137960" target="_blank">📅 20:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137959">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
خبرنگار: نتانیاهو با ارسال جنگنده‌های اف‑۳۵ به ترکیه مخالفت می‌کند.
🔴
ترامپ: هیچ‌کس به من نمی‌گوید که چه بفروشیم و چه نفروشیم. ترکیه متحد بزرگی بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/137959" target="_blank">📅 20:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137958">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
خبرنگار: آیا نشانه‌ای از عربستان سعودی در مورد پیوستن به پیمان ابراهیم وجود دارد؟
🔴
ترامپ: ما در مورد آن صحبت نکرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/137958" target="_blank">📅 20:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137957">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ
:
ما از پول ایران برای جبران خسارت‌های وارد شده به کشتی‌ها استفاده خواهیم کرد
🔴
از پولی که ما از ایران در اختیار داریم، برای این منظور استفاده خواهد شد.
🔴
به نظر شما هم خوب نیست؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/137957" target="_blank">📅 20:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137956">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما در حال انجام مذاکرات خوبی هستیم. احتمال اینکه اتفاقات خوبی رخ دهد، وجود دارد
🔴
اگر این اتفاق نیفتد، ما به همان کاری که دو روز پیش انجام می‌دادیم، باز خواهیم گشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/137956" target="_blank">📅 20:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137955">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc61b4ad75.mp4?token=E-VxHEklpfFyn9qnl0bgPqL2RQiPV0gjh2q71qYaUlEJvJ1aJKJXdciDqHrM8PTXVL7gi4ls68pKXTEC9KueSpjCbfyw0JAdtMsIPLk-ieYYGTeS_M0AcW5qA4fgMBUoisnHkSvhBVXq01lXDJ33qaTCXihuYmLEHhQfOi0cpWn10yz_PdjlMKi-IpJAjfX3nb59ziVy18cQhvltC5yqFlDgAVyJlO9Bpgr4y6cM8lBA31EpIvzuOrOxluX6ioHO8_wpa9TAKqH-L7LNO2FYqzmlluxSbiMqVBPZ_EFiw0elLo6POqmXuTWmX-Dycoohngf2JgLHDsn-5NZ9ZqPT1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc61b4ad75.mp4?token=E-VxHEklpfFyn9qnl0bgPqL2RQiPV0gjh2q71qYaUlEJvJ1aJKJXdciDqHrM8PTXVL7gi4ls68pKXTEC9KueSpjCbfyw0JAdtMsIPLk-ieYYGTeS_M0AcW5qA4fgMBUoisnHkSvhBVXq01lXDJ33qaTCXihuYmLEHhQfOi0cpWn10yz_PdjlMKi-IpJAjfX3nb59ziVy18cQhvltC5yqFlDgAVyJlO9Bpgr4y6cM8lBA31EpIvzuOrOxluX6ioHO8_wpa9TAKqH-L7LNO2FYqzmlluxSbiMqVBPZ_EFiw0elLo6POqmXuTWmX-Dycoohngf2JgLHDsn-5NZ9ZqPT1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ایران در طول ۱۴ روز گذشته، ضربات سختی متحمل شد.
🔴
آنها به ما درخواست بسیار مؤدبانه دادند و گفتند: "لطفاً دست از این کارها بردارید. بیایید ملاقات کنیم."
🔴
در حال حاضر، ما در این مرحله قرار داریم. باید ببینیم چه اتفاقی می‌افتد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/137955" target="_blank">📅 20:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137954">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ترامپ: از پوتین درباره ارائه تصاویر ماهواره‌ای از ایران سوال خواهم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/137954" target="_blank">📅 20:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137953">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ترامپ: حوثی ها اگر مزاحمت ایجاد کنند به آنها حمله میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/137953" target="_blank">📅 20:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137952">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بنزین راهی ندارن گرون کنن شک نکنید …  فعلاً تو موضع رسمی می‌گن هنوز هیچ تصمیم نهایی اعلام نشده، ولی وقتی چند تا سناریو هم‌زمان روی میز بررسیه، یعنی اصل ماجرای تغییرات جدیه و فقط دارن روی مدل اجرا و زمانش تصمیم می‌گیرن. گزینه‌هایی مثل گرون شدن بنزین آزاد، تغییر…</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/137952" target="_blank">📅 20:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137951">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ : اونا می‌خوان با ما دیدار کنن و ما هم داریم باهاشون مذاکره می‌کنیم
این شانس وجود داره که به توافق برسیم.
🔴
اگه اون کاری که ما انجام دادیم نبود، الان حاضر نبودن با ما مذاکره کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/137951" target="_blank">📅 20:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137950">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07935bf061.mp4?token=nxDMRb45oP1bqG-SooxlKiZgKrDQMeaPJr6-ln4_YrbrYHpYVDSwy4q6SraFfVp_tIVQ2_gsgXVZUvtKKquNOzjE1zc3KkXh4aX7RWSGheSYap_kXY7aR9n3xun_0jf2rapSSzkntP9XKvwJOKYPtgyGTHE0BqB_L0mRQT0kjcKne20VfSQdSyagRlQaWizMyvC3YYMjmwpyZLG3Hxr2mmA_gxIif9cQDOBBO7TyJoJgnYnWZFjY3NAeALOoWBcSHUGN4Z4oWHGcCHWd6lbbOVAKm_ue5SDIHMHjpiGi1CpNo4jARl4YO4FErwI5Sd80zGsBGqC49ylLyBkd8iG_Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07935bf061.mp4?token=nxDMRb45oP1bqG-SooxlKiZgKrDQMeaPJr6-ln4_YrbrYHpYVDSwy4q6SraFfVp_tIVQ2_gsgXVZUvtKKquNOzjE1zc3KkXh4aX7RWSGheSYap_kXY7aR9n3xun_0jf2rapSSzkntP9XKvwJOKYPtgyGTHE0BqB_L0mRQT0kjcKne20VfSQdSyagRlQaWizMyvC3YYMjmwpyZLG3Hxr2mmA_gxIif9cQDOBBO7TyJoJgnYnWZFjY3NAeALOoWBcSHUGN4Z4oWHGcCHWd6lbbOVAKm_ue5SDIHMHjpiGi1CpNo4jARl4YO4FErwI5Sd80zGsBGqC49ylLyBkd8iG_Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: در مورد جنگ ایران، آیا به دلیل توصیه‌هایی که هگستث در ابتدا ارائه داد و نتیجه‌ای که گرفت، از او ناامید شده‌اید؟
🔴
ترامپ: خیر، او کار بزرگی انجام داده است. ما ارتش آن‌ها را نابود کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/137950" target="_blank">📅 20:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137949">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
نیویورک تایمز : ترامپ در حال بررسی سه گزینه اصلی در مورد ایران است: تشدید اقدامات نظامی، تشدید تحریم‌های اقتصادی، یا اعلام پیروزی و عقب‌نشینی نیروها.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/137949" target="_blank">📅 19:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137948">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
فوری / هم اکنون تیراندازی نزدیک کنسولگری آمریکا در تورنتوی کانادا
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/137948" target="_blank">📅 19:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137947">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016013f411.mp4?token=N3T4PFMJzr3t4SO_bDmNMbHHTFZMdxTvWDqf5Bke4NmFsz6drg3-IvKFAR26h75ag6cd2ZBVSVdpr_m5V79Eu7CMqVveUdZmtZAUHjq1Z4GrXQr5U_T_LX_keOCeVZDRVOOn3cYWFC2cMcWT14OneuzoqBxmYBghPI6RjyvyPI_ReXueetZ3zIHcmqjfqG3NOQmU-krPuu7MUfYD8qE15zpEqy937_PIirxxUYdlB6V69B0ZJhAj6alYl-a0WbHwTeWszRQpzZQ35U04d422bXBZj2oV2WDqwSRnA1Gb5KkFGDY9LrCRpSa7wKQeg89mvrDQTsl9wOxNM2UQKyR45APlH3kZf1y4LDCTYhLJ7d9g2o4NAd44GOmSzhkPNtK9QZEm7w5bvTpoKMKfEpYZuT9F5zbQTiYSsT4XHsiLqAqbWQNiCCIkJE9t1jCdkfeWHNo6vAYvYwMw9Pl8A13867MJ2iXfeuG5B_5LmlsI_gnFAe4jzgxDXv62xiVsKZVNexreQsyZfjdsJA5IGg3_zkKOHEE66CEye5nPY8TdTqtuXGAnfK75bngHubNdvDqM9W3DK-jcx8TWdgwSgA84UcZJdyyjUt5pVWgtj5wSaJ4rIoJJIy6VIDwZ8syS6rqj7-uToiPLxULh3aO814-XGxuV9pHmAHlu_z5OpW4hViY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016013f411.mp4?token=N3T4PFMJzr3t4SO_bDmNMbHHTFZMdxTvWDqf5Bke4NmFsz6drg3-IvKFAR26h75ag6cd2ZBVSVdpr_m5V79Eu7CMqVveUdZmtZAUHjq1Z4GrXQr5U_T_LX_keOCeVZDRVOOn3cYWFC2cMcWT14OneuzoqBxmYBghPI6RjyvyPI_ReXueetZ3zIHcmqjfqG3NOQmU-krPuu7MUfYD8qE15zpEqy937_PIirxxUYdlB6V69B0ZJhAj6alYl-a0WbHwTeWszRQpzZQ35U04d422bXBZj2oV2WDqwSRnA1Gb5KkFGDY9LrCRpSa7wKQeg89mvrDQTsl9wOxNM2UQKyR45APlH3kZf1y4LDCTYhLJ7d9g2o4NAd44GOmSzhkPNtK9QZEm7w5bvTpoKMKfEpYZuT9F5zbQTiYSsT4XHsiLqAqbWQNiCCIkJE9t1jCdkfeWHNo6vAYvYwMw9Pl8A13867MJ2iXfeuG5B_5LmlsI_gnFAe4jzgxDXv62xiVsKZVNexreQsyZfjdsJA5IGg3_zkKOHEE66CEye5nPY8TdTqtuXGAnfK75bngHubNdvDqM9W3DK-jcx8TWdgwSgA84UcZJdyyjUt5pVWgtj5wSaJ4rIoJJIy6VIDwZ8syS6rqj7-uToiPLxULh3aO814-XGxuV9pHmAHlu_z5OpW4hViY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زوهران مامدانی، شهردار نیویورک:
من علاقه‌ای به وارد شدن در یک بحث و جدال با نخست‌وزیر نتانیاهو ندارم.
🔴
آنچه می‌خواهم بگویم این است که در شهر نیویورک، یکی از اولویت‌های اصلی من، حفظ امنیت شهروندان یهودی نیویورک و حفظ امنیت هر یک از شهروندان این شهر است.
🔴
ما می‌دانیم که در حالی که شهروندان یهودی نیویورک، اقلیت کوچکی از کل شهروندان این شهر را تشکیل می‌دهند، اکثریت قربانیان جرایم ناشی از نفرت، از همین گروه هستند. این غیرقابل قبول است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/137947" target="_blank">📅 19:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137946">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سنتکام : کشتی تجاری تغییر مسیر دادیم؛
۲ کشتی از کار انداختیم و ۲ کشتی هم بازرسی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/137946" target="_blank">📅 19:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137945">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
سخنگوی کمیسیون انرژی مجلس:
حدود ۴ هزار مگاوات برق به دلیل جنگ از مدار تولید خارج شد؛ قطعی‌های برق جنوب به همین خاطر است؛ همچنان به ترکیه گاز صادر خواهیم کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/137945" target="_blank">📅 19:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137944">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aL7vu6cwufErZvHuWc7hC7zo-9ykQGPy0OUKTFNB3ZvT_pbsSNxruckTzYJMQ9uRLRIP1Ji8MWTYlEVw94-2fVsQUfJlPxp_4ANgBjZ4jiFUTf_v_xIPdcyA1oiGa8NQJi8PjvulPcqyqquOk7JDq4QXZ3sfZNw2Eh1Ikt9SIqSnMV3Y1oC036uN1agLylwe9LpryD-f5am6RU40s9OYKqxzZQs3f_15lfpa6vuj02vlNpfUGehHZFgzWQBY2mCCXbXHgR23dAYSJDJ_qsqpnwVwoY6etg7eamiO8aA0082-3K_gadNkLd7Lm69Bv5hYsC5a6sS7cXIyCF4G_DFL2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کرملین دیمیتری پسکوف:
پوتین بر هر موضوعی از الف تا ی مسلط است؛ او قادر به درگیر شدن در مناظرات آگاهانه با متخصصانی است که تمام عمر خود را در زمینه‌های کاری خود کار کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/137944" target="_blank">📅 19:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137943">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رئیس‌جمهور اوکراین، زلنسکی، برای اولین بار با نخست‌وزیر جدید بریتانیا، اندی برنهام، در کشتی اچ.ام.اس کوئین الیزابت در پورتسموث دیدار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/137943" target="_blank">📅 19:10 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
