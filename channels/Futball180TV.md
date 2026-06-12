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
<img src="https://cdn5.telesco.pe/file/P2ymGHLTTkdP_Bi-MM9NL9MDiT5EHM2bwmhdYCkHi1VH-DXdnrojM9IKr4N0J9mcNRxNVkqCwxO77hn2X451mj735ZS9uA_FXYZhBDm2I3InKo6Kb4jOUk9lv-dfkV5FpqH0TftS6vJc-MSn1tDSjdFbm0_-h-DAgJpVwcUbzb7YYj0zs0XoNvabOt4qcDl9lHWVxsX2MLSvMuELz1iSQcgXGtbz2iDt-8Z4wr8OGKgmXlPEyAf71JbLyZjTjm5rMWB8Y2e6MQj-Yv7kS2ORvRcQyJJ4kAdl3c0q6NiwAD56Qj_-4OE5sbtyf0hbQZ4leu9V-Kv083BSrsmO3qqRog.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 393K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 05:12:38</div>
<hr>

<div class="tg-post" id="msg-92233">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wBE6WAMx7rdxOoJcJFE2rpT9M0xJwtEHfLuYI-p8wo0k8ws2rDgoixyLU8wKypyxGNUxtpLPvReGHZH_ZyUX0bW6obmKVCm_-_18A0Uave1M0VGwLiV0U-dB4fzbvd6Jwwqaxly3Y_m5fPp9ZUD2HqN4B7bAUHAtgLQZyhEQpX83Klkcjp9halhmXy7sSIpp3N2gUXVI1RUrgnB2u5ZHYrb1qbWfXPG8DeOk9MSAFiH0LIW9pEN74XgkaTmKdSbA5NBaw_7-bQ4y2lExfhKc5K_AhvACJHYL9JL_Y2ZgcyXld5TWg72mChRuoePIwPTZLBjDNCqbIzceWhIBd0cI7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DjzL3rsgmvP1ctkL2hjdbVN-UpQNA7AAUtnR1Eo7gLiWpWNX881yIhtaydGTiXqqbrQW9apEmxibW1Eq_-1FcZiZXMqWxEzYK7tHHtWJXXqPe15pUGDRsQbPAX4Rmv-jv0RGl4gjKhyptbVH7eHtQSzCMUis0umS7D9Jq-QsuYXOAQA8KYOUkEDxxP7kU4MzU1tygeqj2eyDKO66eUnDX7FwXj0kfCTbcI_Q9O3kawfQd46sNl5aYJsY2QKlq6T4y_LrKjbQ-bbZCwBLVKsHv2BB2a23DkRbaORMVG1YAku1VXA7aDT2zGDUiJXEsVIYJanbKv_RV5hxXJax7I_59w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مجری محبوب ما
حاجی خانوم دلیتا
😘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/Futball180TV/92233" target="_blank">📅 04:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92232">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVdCid73L-qAGl1IOHX89HTUDe7myD_TimM-O2QuMLnv-IJotkP8Y2hpFLqsM-VKsX1GNfIErjbuwMrGs51NUxudx8VYKhzSWYyxwBxcV4qHuePJE2h5urfpnBpTmbUrCdzXi456t07gDcsAqgX2QFuuVlDeeOvmQ_8IZLk6rvVzxEwT4iSeZhHIDZprbyxGrmXRh2ZSxz1HuPySTDcdiATYZ-xJD_atlSANZJ7cXZ1WVIP9Wa5Hsgt2wVUr5JWXcksPUJ6pOfPjUvr6SoEyn4O2TB03prAxknZ1NYn_CWUqjw9QkzXx5Egt_kC0BiVxikQUcHvBmsXwQtMj0iJMiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇨🇿
🇰🇷
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|ترکیب جمهوری‌چک و کره‌جنوبی؛ ساعت 05:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/92232" target="_blank">📅 04:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92231">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdStXgIDvwKbu3eIpxc8fENY0GTFNRFBIfEETMIdYGcUUppp4meP0cw0Y47EvuHsmMBUJ0j7Hayk0gyEfya0h8BAad0Kc-kMOIzDalhEZb1SsdnpIIiVkQuvJCZcn04b4VR9TcK4XGl94Xy9O2uVSZXP0H0hS3lvpvpYGg-bNyBqNtDpowZX0Woqniij4ql4kSN2TT-_bso4tk5poPvuMF0k1tM7DcSqOt589jV5rpba4I_jqAfLc9KKzyRUReYvgIWCXzrbGHQl0D9XK3xGKL-lcseGS2O0tZGwVbycvkuc3mNnp5IFyI3p5J7FFdCm0KXKSFlLm0a7QOZ9-jfByA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
🏆
🇫🇷
شات‌رسمی جام‌جهانی دیکتاتور فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/Futball180TV/92231" target="_blank">📅 04:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92230">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kp8A3lUs6hdRb9ton3fCpxRYrqJ4Qohe2PKphvHOAuRzmc1zKtOsTu3C5I--w3e6C8wRmFzX1gYZV8WCcxC-UHuLxVZ0r3q_Yo6SFWX3YWEcf-kVCMeRKe8urLESE5XAT6tW5XVQ2-fT7J7A4amaBw0Pzfemd62VPRiTI-j4LuTt8cS8qn3fBsVD2oPSUdt6P-2QEVRHmEOvj7VEWuPxs4bnT9CSa1WAyTDLfjQI3DIP2E8nvgoMl01Bwnn7VINPQR7238i9i6wM1S20LfePg9XWIKgiT_Fgkr9PzSMJxKb63H2LQ50khOtFwqDMB4w2i8dCKdqSCTMKzmKhqO8ITg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🙈
🇳🇱
وضعیت شکم عرق خوری ممفیس‌ دیپای‌ در تمرین امروز تیم‌ملی هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/Futball180TV/92230" target="_blank">📅 03:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92229">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVmlS76AooojL8RCUIIty5WI17cE7Qn05Ftetgbw7uMv8C9iw5ChJEPr-8miFNRmVURAvvox3VEphAXPfx1h-SYPYuRUh9pLLimNJTjbOXkMdV4SJKbHr1FubRCdl3spL2Bb8uCnQMpACJ5-r2O5hPLiGhF8U7P9zE7vwl9iknLXozLGUJ5oy-IN_Cb0U9tzcnN7y8H0bEt6fsc0sZrLsg9BezoWVWHMh8mGfQYX5wmdvQYyLz_QJub0gJPtZc2DKKwgLIHLMrgr7RyjDj2SVftuygaikBHHqZmyj1TgQnUSlGL7Z-Tx8GYPstPoMMaWAnr2gWY6i2pCC0a_deeW1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇯🇵
واتارو اندو کاپیتان تیم‌ملی ژاپن که بدلیل مصدومیت امروز از لیست سامورایی‌ها برای جام‌جهانی خط خورد، از دنیای فوتبال خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/Futball180TV/92229" target="_blank">📅 03:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92227">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q2h4GBEHNS0Qx2CYGS0R6AuxwWu4Q8lDeo7mLDMncdKCHbZ_XxDiv-cUNh8nelgCTXcHFKOrLcP0iYozrJ8Be1SUqqETiJH-CB-muYlHlRd-88vD5pg8U39oEfD4NsFqb93Ttbk0Y1GC_AjbP-9IkM6WD3AtXN7nDc0fFSIIBPCdld8HI_RUSfPOoEH6JdkkwCU3O2Kd0sLgn6Dg847IWAvAnnaaLJZiIB5odYNCanll0O0jyKLf62A87wwntF-1pK8X9x6hDHZU3YbteH7y0hoJYL-QA8WvvZyLlGem2EyDTiKQ2VMtOXZ7jVRM5sLGBACf6ZaDGiOkAT9KnzKC9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JP-fo_0Djz3F37yaDwehrzdbIQ223XODIRlTm3qaPX2DSanC5zxMUZuwAMviMOSIAEzfNGBqgH-RS_1fUKnKyozmNDrJ6lQQi1WdX7ECfJ7BqYo7NIZBc6Nj1PmVVwDuaMKc5_WzOxYf6h7XLbQ8K10CmrCOu7-wKwtTk9juzyqBprSi30CKmDLtiRO0PplsPmreVgvEPTPoLl4S-gGHOjIZa0quooZ_fKPjO3rUwYhov0i-vmOnbf6pXirQDWKdowAl9iY7e1ZVudzTcEnQoZZjR8X_1xbuMSrV-y2L58q8z5lglvi94BE0ixlaBu86MSALN1aMydOZNLCN1HZsxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇿
🇰🇷
استادیوم گوادالاخارا آماده میزبانی از بازی کره‌جنوبی و جمهوری چک.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/Futball180TV/92227" target="_blank">📅 03:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92226">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/09e8c7b7d0.mp4?token=Bxha4NBcwex4Sf3NAQnli0KVY8f1RLlFqrOAjm_eipJ9HFuyJMYSIkPRGhWLJuV8oZwMXD_5KBqwtYj8DbohgbTiKebGldM5UlsaMTRS36Ir8yw70BA52JKSl6XiG1tgQO3UldEDZ-ZucQYd5sOsnGIu3lXvdqlTBnZUAswoyrF9xzV_ua0MNGxgMPV3vnW_IDMZ1tHaLngbbTdX9OzmMCT4IPWFcEbWUQIh8NQjtqW6L8vUQG0xWA6vf3Wf8jTxwVgSmCiKn5LFMBYNq1rADzsHK5dPpTBcDP0Qx88M8kGCPI0g0RvgL4IpUFHaC44Vnv_4x0N1WKLQEwQ4bQOyIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/09e8c7b7d0.mp4?token=Bxha4NBcwex4Sf3NAQnli0KVY8f1RLlFqrOAjm_eipJ9HFuyJMYSIkPRGhWLJuV8oZwMXD_5KBqwtYj8DbohgbTiKebGldM5UlsaMTRS36Ir8yw70BA52JKSl6XiG1tgQO3UldEDZ-ZucQYd5sOsnGIu3lXvdqlTBnZUAswoyrF9xzV_ua0MNGxgMPV3vnW_IDMZ1tHaLngbbTdX9OzmMCT4IPWFcEbWUQIh8NQjtqW6L8vUQG0xWA6vf3Wf8jTxwVgSmCiKn5LFMBYNq1rADzsHK5dPpTBcDP0Qx88M8kGCPI0g0RvgL4IpUFHaC44Vnv_4x0N1WKLQEwQ4bQOyIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
ترامپ:
امروز جنگ با ایران را پایان دادیم. و آن‌ها موافقت کرده‌اند که هرگز سلاح هسته‌ای نداشته باشند. چیزی که ما روی آن اصرار داشتیم. این کل هدف بود. این ۹۵٪ ماجرا بود و آن‌ها این کار را به قدرتمندترین شکل ممکن انجام دادند.  پس فقط می‌خواهم از همه تشکر کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/Futball180TV/92226" target="_blank">📅 03:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92225">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59c15527fd.mp4?token=qG4yo3CmlGTniIM8YeKuXBYhGLXnwrnavU9-rFq5xQ1BUBlOvzyfNUKxHCpNkctOMoHw-FwukDPYMe5GGKPNlh00wnSzkdeElo9NfH9cpcjoNRlJgnIK-BTM2ka0gD4BlATcRTVkOZPaEQMy97pCdfZ6TV_npRONCKVU5_005mO6B2u-B-9Tzsb6PCM8Tm5LIZlaJD-LQQ7pNzoY_8DzxMsTxT1qVohSqGr4m1znScBcoZsCAoc9qh5fXSLY1aSPhohxBIinoN0hxeOB6Z-NydK-vWGRwfwc8Avbz7uT1BGJS3UVz8sRpkzjPcoQ5ozRq4XRQMshZWmcq6G3PGvVPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59c15527fd.mp4?token=qG4yo3CmlGTniIM8YeKuXBYhGLXnwrnavU9-rFq5xQ1BUBlOvzyfNUKxHCpNkctOMoHw-FwukDPYMe5GGKPNlh00wnSzkdeElo9NfH9cpcjoNRlJgnIK-BTM2ka0gD4BlATcRTVkOZPaEQMy97pCdfZ6TV_npRONCKVU5_005mO6B2u-B-9Tzsb6PCM8Tm5LIZlaJD-LQQ7pNzoY_8DzxMsTxT1qVohSqGr4m1znScBcoZsCAoc9qh5fXSLY1aSPhohxBIinoN0hxeOB6Z-NydK-vWGRwfwc8Avbz7uT1BGJS3UVz8sRpkzjPcoQ5ozRq4XRQMshZWmcq6G3PGvVPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
🏆
پشماممممم؛ این یارو که می‌بینید حدود ۱۷ ساعت قبل ینی قبل شروع جام‌جهانی از نتایج بازی‌های هفته‌اول گروهی جام‌جهانی پیش‌بینی‌ کرده و ادعا کرده همش درست از آب در میاد. نتیجه بازی اولش که مکزیک بوده درست از آب دراومده. ببینیم در ادامه چی میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/92225" target="_blank">📅 03:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92224">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pceNL_URfSTDAdQPPiaEwF_HJwVY2nC8emazV94qCEn-rtiQgiAp5LllGLsqfWIDcosOeuotgbPPpZb4knaGgWKWSiRDcEOtyWOmjqShXztuD1Em9hU_pgE1b1E5zTZN9Uu7zJCDD4ZzMYMc-y8sJwMlIrJEkHK39DLyv3916XkKS4qDkBRlqJ6Q92dTEjb47HTbMQ54DRizoWpCyjiZsnVcBTQpfAznxWf3XzRluxfpv0v6gd2Yvg63blFDXE7TS87WkNo-RcRx8It9HmxRXv_rfImMEBvq615x_SVCwa6vxaD5SUcEo7KKUKokSKCcypDMHQd9FioEo0ryXtGAcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
❌
#فووووری
؛ تالیافیکو مدافع چپ تیم‌ملی آرژانتین بدلیل مصدومیت حداقل ۳ بازی اول جام‌جهانی رو‌ از دست داد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/92224" target="_blank">📅 02:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92223">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnNyhEUUwxPY4XqY6CvjG-PhBM3_ZP4YPOeTnIXcvJuDXW_Hq4nv5abfYpAxFOr0Ya3wXQkIICjOolcAl6vMQsTu-FhQyX1pPVctylfi58Sn095d591LXT1jPD3lXip1r5nYwj074cIZHqYLXRxPEiH-nfsOnbPcoN5whBDw_Sfmx-9i_lS4m-MlZQQxjX9haqJRZrR89jSi4rDrl5GBuyonAgke8LYQ1g14hS3OueYXGzNPzCZzSBBRDbhenjmVObjUvJ0B_QanqY_hU0UxLHfuMJfTuGpTBlFFyOTndBDZmbq3gXZY0L_UJrpA6pNzWCTVKoGQWBY3wvCG0HCnsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🙂
🏆
نواک جوکوویچ: بنظرم فینال بین پرتغال و مکزیک برگزار میشه و جام برای پرتغاله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/92223" target="_blank">📅 02:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92222">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35ed8d7a65.mp4?token=UZHHlzStKgiJ9Vp2u9SBtKwWI1nAtv317kOmnJSABtZl4hSGE9_mBaailBW5srC0ALONQLVf0aMckogGtYCb8QzAbdIRVfjINsitwvD1k79srn7BO79AtBdp-Nb6YLUh-1eher2RzLP5nwrmhTpl3mfmtXgaO3-4f9LQy_gLkVPY3ZYljK3FL5L4qdbV1nxzIAvuU7Y6UUetATyBMRwSUeFmtjnLLfucrwkhe0GXDhYjVGQwWeR2Dw_QIp5aLeyvWMMzoZ1cR1T2Oy4bGfIiGdDxX6GbXSDv5s1M58aiyDpZrrpGrzIrVvppST3IvzgtrnrjsjRhc63IqCXZrZR14TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35ed8d7a65.mp4?token=UZHHlzStKgiJ9Vp2u9SBtKwWI1nAtv317kOmnJSABtZl4hSGE9_mBaailBW5srC0ALONQLVf0aMckogGtYCb8QzAbdIRVfjINsitwvD1k79srn7BO79AtBdp-Nb6YLUh-1eher2RzLP5nwrmhTpl3mfmtXgaO3-4f9LQy_gLkVPY3ZYljK3FL5L4qdbV1nxzIAvuU7Y6UUetATyBMRwSUeFmtjnLLfucrwkhe0GXDhYjVGQwWeR2Dw_QIp5aLeyvWMMzoZ1cR1T2Oy4bGfIiGdDxX6GbXSDv5s1M58aiyDpZrrpGrzIrVvppST3IvzgtrnrjsjRhc63IqCXZrZR14TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مصاحبه ابوطالب‌حسینی با طرفدار معروف پرسپولیس. عالی تعریف میکنه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/92222" target="_blank">📅 02:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92221">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/92221" target="_blank">📅 02:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92220">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HA_HhoRAG7yxvOyy1q00K7zXbh2j41GZPN8fLhtSzdY9KDMujZ23ETnZ1Di4cj2PuERRC9Jo3qak2iT3tQNgRGz2zCdS4nC399IEduunstmHQyDxZ7zFQy1v3NdUmVY64X2KnoiYOgFk8XpSaw_h67PxfjGIqkEUp_fMHEYt2wEmB8Ihgy7HH3UJszk0tp7fFu51KvxGi3IoLMWhuAZLYrPIEVSGs2PtHCeWXdi6mOd_FHoFNg11je8RZiyNVCxeEucrOzBR3p0svlNEX9xHNB-MeTEY75990seChBF-dhPLnJdvSgJDC1t0LMqspdmUZyvwT5_B-EC3dwsmuhgl9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/92220" target="_blank">📅 02:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92219">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgonilGx9XOFlZ8Kkch7tlSMHXXaxgtdpvclVT0w_-aQwqcjjzkTl7tVWigfeSxl9MPZpGg1WgCj-zWf-4fvtTwx4429MMLkeY05Dwry1dh0Y75N78zfW7hF9KC2x3Ei-7ERsnN69QKCYHT0Ze6SDDDK-hXpbJiDNxVUAl80CpM5zawzqU5HDoCJOdVNOcoJzK1z4SjyGWgp8A0aqvxmZ8Gp2oj1LiTpGKyv3WfaXft9zNuFVsBaYXXSSRC5vEjm9kfuIhSkFjmJ5sQYdqOF1cObE-LKJHzQZiY9fAoGWsoxfCObJ6-4o4sp0P8nMMKO8gU6Xcl4GODjeIM-hKv4vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اوچوا دروازبان مکزیک:
امیدوارم در فینال با اسپانیا روبرو شویم
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/92219" target="_blank">📅 01:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92218">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
فوووریی فارس :
دقایقی قبل ارتش ایران اجازه عبور یک نفتکش متخلف که بدون هماهنگی وارد محدوده تنگه هرمز شده بود رو نداد و همزمان سه انفجار هم در سیریک رخ داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/92218" target="_blank">📅 01:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92217">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-rhsPOE5XlWfGw7q8GgE5m9E7ToMZIihb1ii01RggilttBI8uZ7Ub6qwHbol_XtVirQmiBzXfyOW_qgRA9GIf3C2Dmoa-RQr24acc8v2RjMKPbdgEsp0r35nJg2l5DtnIohm-AWOS21oOPonKw2ejHPDfjYTFuRiOTSUW4XA4CVpCTGPDZNcocqE2UTl2Vr3O-xtR_WCkcLsSjYIOAZkhwMvv2LWzB95ihekyg3UZJC8FZ9nE_rhZEu12wUEG6d3v6nVFEXdP66oOCCITvojSSuJOs1Bj0X8FTo298QuecN6FIV6metTgzieTWKObNah1VhL2eVgBx_IVN_uNep1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سه انتقال برای رئال مادرید در این تابستان تا این لحظه به همراه انتصاب ژوزه مورینیو:
✅
دنزل دومفریز
✅
ابراهیما کوناته
✅
برناردو سیلوا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/92217" target="_blank">📅 01:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92215">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJ52jvxU2E2Y7MWiNqjvsCGZvSa9JSzpjJuGN7WchZgGGZ4NcJSBOnwno27B_SSj9rB_JrmtVGKoXlSlW7WM2WCAsjhSQ1XLgh8CmFU31C4hXUIsJQJrQSCtJgj7AOefQriG7RcaS0nBntHn4RvlZgiLvoTeMipVt46X6Wp7bSNzftDfcs7p6Q3g6oxPeZ_wupHB6izIA-DC9WBWJ0chJh6ui_pqJaBLHWz6DoRWCdtUnD-XYxXbjGAPjaJA-oDjSJk7mDtkvfB57Oig44W_duwvwWh3_AnKSneFwTDkxveabanK6raHsHmC9rE_ZYxKgpg83JuH56ohodltMPnBnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/diHxLmrm17S4hkQr9x5-kYWYFE6YyAMpKCA0aCy4HsCLPWjMQREAIAetg8WvUD5pWHLvM19iJ8D6x-4UcYwIiCiZEqv2nkcPGz9X1BDhUlOrFzSGlHSaJzUNS231ZckfdKAgyEiBrX_A8B6rM3cmBBIMU12MQ3VcTV1uNg8SF1rarzU5uNFJu9Zmu2zyz_kmfIzHyu1CZWqjdBxgT0hgEQY4081-WshWpzLGFVL-i26HP4FZxOa9SZKWJabwR1oNwpxvyzHnn7pcUZKvWnS4pT9vpKg5XFxvHKUjkEu32KVUvBN-1d1-hr2CktgIiIcuASoTQ2KyUqDDtfuMvuMAsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
آبولای پرتغال:
🔻
در محل تمرینات پرتغال در میامی سه تمساح دیده شده. زمین تمرین پرتغال در کنار یک دریاچه قرار دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/92215" target="_blank">📅 01:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92211">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rGzpS0xM7MOE5sFhAIVJ9zJUJPkxEiJ875pqtkdBWdEeq--gk8XGC_TQQypEI-NWObvP_YuWHiCarCJKSp9iLqfEucKMv4DHPQSGAACoTpGufRy-eMuO4-O0lfv4FxtW8Fa1YxZ7WLyYtZpvk96a_sNSJs7he_JabNcFy72os-Y4rhcMkJ7P6hbv9aLhcNaIhKtcEJ2DiARa388x4HEOOoDLNgh6NFyd5X5iKOVMDY7P4DgTpCyosvPgiB_iQHJJbfAj6JgKN6gy5J3dbsC1RnQjQEPG5LE2aKDz8hpaegCmfReq0I4LqYOjYnHCkcwedQvuPseHbCNZpC_5NET5Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jNKZC9auM9WgLBR8wDpqRmoGJC4Ldo3N4nowyu-8LG43ueLYiQOyoAetF8t8zzW0GF31sSKWGKb2cI0GoXICnwfOL6DYgNYk7uUWkMPmYj72_FbW7Us6SSVXV7TIS2a2XKwR3yNEnaV70zjdSu_hwHGe5RHIpCrUX3HmtP4j7fHuLAoq1-SfDzqw90e0utw1jgw93GHyCWDNQRJ4PDkUhDErpNkCoLmyZVPi0XFgwN2vDRGYYluTBkHVCV3NLt6W_d_oVFJXSNDTKVjebY9LNIMf3KydJ3qVf7mxpx9sfsEjdGdr8Wcc7fcAToakzpsRo0xtCHFMlKQ5BzJA1ykMUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tzuq_oj0FvZcBilpOkFCT9GZVR-YQuRZgDQMqAarEb3MkxTPz9FkIzc24LTJtwpcgjsrau6mCnrq1RJ0-UI-_A-626UDr9PbKHIvOWLe1jruLlwqM7p7Zf8mwmBD5yU5ZdlqjrLyTYuORl9xUsNEPB61fdlmarqdBinxJhaYajHV8W7WGA_aGm72-DgEadiFI3M_ubfNDELG4OYYtEfHJdk7QqRcny7bjMREq2fTFTlnqv8DjHKZMy-FeJ6_C_m-vybYldZsN0LWe3Oj-vMY0_pag4d1zp3-rnsykvwzpKrRTgYRDBtKf2L8KJqqJgGyDsyMSSEJ8FnLx2uEwLmZkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/itEzUcDDGPv379oTnlScRlGKLYVWPujQyuTem70oozhq1fzgaWNZ5N64foT77qXLNPkX-IoT_jaHssfUo1ZzKbDHbFzYECjDx_SRzySwfaPOyd_vu4NG4Mmuh51Tjrln8hhC1avOJ8M6Dn9FBdzCKwodksK0GVf-KFDog3TpwksDU3oYqMyP8odWhe4BGrsIs3ogStorCpiMAaRxU1Ni7sBZQDLbyGts8QPzXYVC0VsUSgqGEnFwyVkyo3nig82NCcCLfEjX1ufFM7qGY3bAAUwAXCFCYgSvEGTf33GMQDXw_NyXGgzLmDTbwtpVaNLk8d51-iBrMW__Ugv2or0mGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تیم ملی فقط مکزیک
😘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/92211" target="_blank">📅 01:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92210">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfeIIFmFPiUkn3t2EXwcU3jP2VxL9EOs-0gVtjDi5guuGqvapR5HqMCgft331a92ea6DV_x5XFuUY5jPOB8hcz-6yOwjlecTCVGu16D90ObO12Spl99u2i5jyrx-OCEpB3_Jmc7NnZeyjRuPwY2N-AVCvqgTbQWX3iJ-xFqrz2eb7c55lpaASTj2BndVjR0hA20sGetEt6xtN9UrjEWd-SITM_DHwVHImUD6DypPT8qnmCKoAFitzoD8RhAPj-QJxIKbNMFL9YzNxrwhHzUioTbSypIiFHL0768noZTYt90-NvBbBMp3n1lmKKeesHJIpp_O4Cw6Rwf5Fc0KLuZceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فووورییی رومانو: برناردو سیلوا به رئال مادرید به عنوان بازیکن آزاد، 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/92210" target="_blank">📅 01:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92209">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XF8aYfjQay2xRmicYdU9bNdYqARnmP-RSIiZIB7h25xSJ80z_8CsJln01Z9CJivEJjTPTnmT6oJ8miQTyd6iayyHywpgmaoe3ceTfni1lriorUXCWW7fyeAxMYbKZ0ag5yNr0Wsx3nuQxo-qyYcq-087xbpycz8a9PW9XsX5BTwayiLssQNRrIFAabiuKwrP_gC1ekvFYoJQkal-6Bk5dUou21pUY11gsYqz_Z4o70LBmkjWyfIjntT_VEyBCx5eXin-2TbBdHw3bvdN8zbu8Gib5_H82RwaVFi3NMtt_w0g6TqJ7zSvZFnHuQZNf5IDzm7baFDo_4HTIl4RNHexcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه:
اگر قرار باشد بدون اینکه هیچ گلی بزنم قهرمان جهان شویم؟ من فوراً و بدون تردید موافقت میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/92209" target="_blank">📅 01:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92208">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
فووورییی رومانو: برناردو سیلوا به رئال مادرید به عنوان بازیکن آزاد، 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/92208" target="_blank">📅 01:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92207">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qenc6AhSK_x0FiQcgddVbStoA9lt3UjbbX6ryAiVGVuNf4bZLwLfrGDVJD1RKW3MqHliimlTpbckZfnp2MHM_0cQ-OPV-ivMJcZnp6aK4PCTHv9MdxzYcbBfllTpnMuCcg4nvF3rYNa9reK0OyG0IU2DHH50iqurAeuzh60j9hufBZDn8why3Hb_lf-VhTK1Zyy4RJCh8IeLmhxIUHTAwIUTNbs5y8VyFvUZFlTndSMg46I7FTJ1A6ixuhdphcTMx9HtkzoxNGNFh1Xbi218tE9537PG9U3sa0n_iT3Bs2YOyKGwB2Sv6W06o_D57Iedh6FpqaQ-HPxyTlxfdbDLlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📔
رومانو:
🏆
برناردو سیلوا به رئال؛ 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊 بزودی!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/92207" target="_blank">📅 01:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92206">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
هم اکنون؛ شنیده شدن صدای امضای توافق در سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/92206" target="_blank">📅 01:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92205">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkPllEK2w5EvWQipuRJOjVdtuCMFL97AwnFvuf1yqrUdkoQJnlSfXiWwPBVO5MVLlb3PivnTZqmGNDltF7fV6t-IpQDSmP1abUMmJ4kZai98rGi7HbufB3OVIJsAc7Q86-eluuBMxnACeAIXT1GYI2guH7o6BzSoTAFYlLKRl8g58-SrCF-Y2GgX2d355rNWryHQjNDGT0U6PBqlADTpmTekgaxr3GoaIgIXFf6x7Ag8zqwUd4YBx4lVv4_hYM9eYhMBwEUYAF3X5CLXt3A3ijMEcqACflkeBKR62KiT3bDsS-qF3xBslQ3FBhSeTCDdZxJtytM4uoqhzQvd_w5Kaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🏆
بهترین بازیکن دیدار افتتاحیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/92205" target="_blank">📅 01:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92204">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dbae198e1.mp4?token=Tqj05kY1q7dKNHAM0K-fIiKOgc_AB1eb_7S2u0ks9hBd5bpHPoA20Ol-JnAiGuTlJyaAN5fQytPEljgoD4nv37arpjgh6xqKR4oA1GAO6LVX_4fMZqrD1moOYPcdFqQzMyNRNEUJxj2uNAj7tcBrnaLd6OTSolvKglw8J3Ccym2MvaFQ90s4r31D2j7LDv4PMbod6cuu71FZFNyojbEqLS95DWzKafhhRK0O59PHRszNO-Cpn4iiIx5d5FBAbZF2GfN4ncWf6THKuc3SmWvCP9kZ0BZU5Bj_SVcWU_rAE3kwP1U1OqhFUTShoK9dcCQzNCrSQ6ldlKX6dZwDHYP66g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dbae198e1.mp4?token=Tqj05kY1q7dKNHAM0K-fIiKOgc_AB1eb_7S2u0ks9hBd5bpHPoA20Ol-JnAiGuTlJyaAN5fQytPEljgoD4nv37arpjgh6xqKR4oA1GAO6LVX_4fMZqrD1moOYPcdFqQzMyNRNEUJxj2uNAj7tcBrnaLd6OTSolvKglw8J3Ccym2MvaFQ90s4r31D2j7LDv4PMbod6cuu71FZFNyojbEqLS95DWzKafhhRK0O59PHRszNO-Cpn4iiIx5d5FBAbZF2GfN4ncWf6THKuc3SmWvCP9kZ0BZU5Bj_SVcWU_rAE3kwP1U1OqhFUTShoK9dcCQzNCrSQ6ldlKX6dZwDHYP66g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بارساییا وقتی میفهمن تو یه بازی داور ۳ تا کارت قرمز داده ولی اون بازیکنا اسمشون آرائوخو کوبارسی گارسیا نبود
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/92204" target="_blank">📅 01:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92203">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
هم اکنون؛
شنیده شدن صدای امضای توافق در سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/92203" target="_blank">📅 01:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92201">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efd5005212.mp4?token=u8eh2h6Yoo92CgjeyDhYNQK-9TLajL3crEkx1twxdMa5I3yla9kjFR61y4JSUrM4vDAKX5D0LEgs5ffQ6y2Wt7ZnaNxMN_y23Rungo1QiDq2ssbe55ovwCP435KlCcjzvefWGK3UYHGGZWTIDJb0_hlr78dIKpdH2saOMqbdRdCCmMc1b_ZwqxR2gpQr7ru9tbQq4lVHMiGKqX2TRVtsFFWGW0HX4STlTDCzEwZCOm_j8BfsdRvHb31igSyUfaVUaCEPWcVce-kKAGOgfcTJ8Vfg0dmOLhhB-vF9evLXSEF4wLbrWLpha5zgsmFeuOLe-ErOTylJ3AuM-0wXFYw74A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efd5005212.mp4?token=u8eh2h6Yoo92CgjeyDhYNQK-9TLajL3crEkx1twxdMa5I3yla9kjFR61y4JSUrM4vDAKX5D0LEgs5ffQ6y2Wt7ZnaNxMN_y23Rungo1QiDq2ssbe55ovwCP435KlCcjzvefWGK3UYHGGZWTIDJb0_hlr78dIKpdH2saOMqbdRdCCmMc1b_ZwqxR2gpQr7ru9tbQq4lVHMiGKqX2TRVtsFFWGW0HX4STlTDCzEwZCOm_j8BfsdRvHb31igSyUfaVUaCEPWcVce-kKAGOgfcTJ8Vfg0dmOLhhB-vF9evLXSEF4wLbrWLpha5zgsmFeuOLe-ErOTylJ3AuM-0wXFYw74A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇦🇷
لحظه دعوت سنسی به تیم ملی آرژانتین درحالی که توی تعطیلات بود. سنسی بعد از مصدومیت بلاردی به تیم ملی دعوت شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/92201" target="_blank">📅 00:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92200">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2O6v962ARZ_ybde_JPf_NIZDk83R1Mey4fGCvPNiedPNulYfMEWpUxd8SPMzHqVznQE4KyA9V1N64z1RO69JKePmffvbn2qQWXYK4mgMUVeHEBXL6nEo_W-hVG6COMTN09IHmUUGClX1JxBejQ_SVkMyT5HfzN6D4UEYYw-0BwvodPfJmseJqyWDfC8DIvgOybQhQwe0ywu1IX5Y2XIebVYKg2rIL52ifKII3CdgRsHzBT-fmcw6WF9bJPFee9UPLyJBjEsrBr7rBd6HzpEa_hYfGsHDP9X0f_RE9oDMXozk1ye_elpXLiV5GDL3hTV6ve81g99i13hI_7bFbuFCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع قدرتمند مستر شت‌هول در دیدار افتتاحیه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/92200" target="_blank">📅 00:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92199">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFrsulMHT4tCESe5snNEbv9B4srSocZFI5JnOA5AKcHzgfO_Z93ZjnpFQI7u0go04T1SzTRo3BLzoVXwmlEmxXCpnAdabTNy54vyuELri62YwyUnuyrS0C2kaAqwe007PbRkUdf6_195RYc8s1Ktw0a3XtLbQD6lex6gtJK_zLKLQCROyp8elsqgs-IJ7uzC6ZVCK1Z0-uwi7bciufyMHx-po1Z11sjvrWMAsUZvghHFBSWgLpJV3CAVsI7pfY5uakwmEP5G7ABgXfoP9jQT7IbVPY1vtlBmvn-usTiwsW1I1JxY_dmSE13_Ngs02RQVuSwgfNrbWmzGw81V29M4qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری:
رودرا خبرنگار پرتغالی: برناردو سیلوا تست‌های پزشکی رئال مادرید رو با موفقیت پشت سر گذاشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/92199" target="_blank">📅 00:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92198">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lgfc2q6HJIJ2QDaQIXOPeVGqTtM_e5zfLYghFdAQo7yQIc3sRwHcFEjDYe8F0JA31nb-GWZMHtz9RQ5d8QkDYOwm_mXA6toF1TLUDJ5VRj6yd8UVZ7WJYXG7pNxmQB316KoBM7dsfNb4VG9zBtNqOKamUTi1h0O7ShzgjMQt461CXnfn5la0m3Qt1vEZhUJpJGCJ7tvxr1NluSe--jBXif4PCkAZyjSpSNcN5aa-shn1QzAwv5czEe_ASgniv-Cm75pSf9gSm1gv3RPviqqA-HGMuNuFLF88xp2gbsilRDATpzMDL133UtYAHcrAXog2uWCeRj_EPYyQEQ8ryGbISA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
مکزیکی‌ها بعد بازی بیرون ورزشگاه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/92198" target="_blank">📅 00:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92197">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vp2tWVDHgwi2vebcXrgaaaXwckgsTr-rfLXi9PnK5niEKEQPNSJxYwBiUSiWhkxJs3i2x-lUoEEWcqk48yrlgBs1kRHfHug5Vqy4R6-_EREjg5yofy3UeU1a7NE0DB3fjHT1pZVah5bp-qAU5bRG5UkiaXnB93Lld6GfBI1EzBP_1lrG0uVb5hO_ahF_hTZjGSj08LS97R00vY0A36OVYcQf2GciX3yrxHFw4ksZ91Uq2Z_dslk7C34EmYKKAzSTUHGHXWsR1mUn2Fa8PXgTjgzvnH--_832ANGjcMAwMH8mLvBCO0psTqd-PhhNk4oXTnmivaYDQxQJWjIsuZcx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
جوانترین بازیکنان تاریخ جام‌جهانی:
۱۷ سال و ۴۱ روز —
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نورمن وایتساید
۱۷ سال و ۹۹ روز —
🇨🇲
ساموئل اتوئو
۱۷ سال و ۱۰۱ روز —
🇳🇬
فیمی اوبابونمی
۱۷ سال و ۱۸۵ روز —
🇨🇲
سالومون اولمپی
۱۷ سال و ۲۳۵ روز —
🇧🇷
ادیسون پله
💥
۱۷ سال و ۲۴۰ روز —
🇲🇽
گیلبرتو مورا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/92197" target="_blank">📅 00:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92196">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXvD3u2SRoQaWjVwEnLYNH-xLcT-xpxAdLaKNjrY49RY0vyEr6yW1X5wvDTM6J0zpgrKsFGxWkFYBEvP9S_ROBuVP_8iK7-jej-Ym9-84NngE5TjZjuFnZ6AmR_gitVJfw4cmmTycRGW1iD_ttbGUOQLTdZV_O9LURxo08iB-Zc87rz5E6SNXSfM2lRFBM6IHmQ_h4c0-C6BOAwMK0fLAEeWlYwXCA1kyCSgribrFje1Zc8WUIaqakNu6rUL8jlhtnBTa5BmvEnWYdt-wfjbjm3mGt78Xb6LnRmF8FWFLmunemxZRGuFeumxMS-fC7RwfstitPbvS0fNYR8faXWQkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇽
بهترین گلزنان تاریخ تیم ملی مکزیک :
۵۲ گل — خاویر هرناندز
۴۶ گل — خارید بورگتی
۴۶ گل — رائول خیمنز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/92196" target="_blank">📅 00:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92194">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dbae198e1.mp4?token=vpR_2Nw0s0-zluPn3Df4IHzxmkXQUHl82qt34md4fkNLYkB8B6z0bQAw_B8ICi8HhYtcNMCfrhHqcaG93ffDtRXKxUKH1lDU2qPPGGIrfyEwaR9pYbaCZNTcuOB-D9jN8me4Zb-djObPS4E5wpEx3XBPCuqUWxTQs1lc4O6_bNsT0FgCBlL7YQz_SND9z13CMiajP87kHWywUcQU6zpiI8lCDUn2MKI8apWNwjKeahILzvydHY2ekJU6X5TTAFyU6YweHX8igkAJPCWZba1zsOH27-bXjtAkO9c3rTMsMqSvnhfPTLrMoRlECitXODvuqu7WuVfzWiE1yVcKJnnvaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dbae198e1.mp4?token=vpR_2Nw0s0-zluPn3Df4IHzxmkXQUHl82qt34md4fkNLYkB8B6z0bQAw_B8ICi8HhYtcNMCfrhHqcaG93ffDtRXKxUKH1lDU2qPPGGIrfyEwaR9pYbaCZNTcuOB-D9jN8me4Zb-djObPS4E5wpEx3XBPCuqUWxTQs1lc4O6_bNsT0FgCBlL7YQz_SND9z13CMiajP87kHWywUcQU6zpiI8lCDUn2MKI8apWNwjKeahILzvydHY2ekJU6X5TTAFyU6YweHX8igkAJPCWZba1zsOH27-bXjtAkO9c3rTMsMqSvnhfPTLrMoRlECitXODvuqu7WuVfzWiE1yVcKJnnvaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میم جدید
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/92194" target="_blank">📅 00:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92193">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-DWFc_SEg9Dp4PwR3V5Iu0uGvOj8mlZaofGMvYkJJzTXgbPknYoKsBpeQoHYrCJzJd04y4UqPeNQYQDlUuHZ1mNUhd1SEqOyK04nZ8byevB_zn46nHmzlPcZ-XJ26Y-ou_pKNtPXJJK6znOwWbN2dmAW3BJRZoBIaMBcshZNcGAWftSgaPUhrnKw1m171KAz1S1Dth3zgdZ7ba0ah1Vk79lBxYtSCKeekJYlSqNHDpYz_dUqJXX7clgLE9DY0JQPhDd4HMtoOEvq8fAxrSmGmoi98-Eg37FhV53duwLnrc5sbRyZub6NDSql8uo3yWTT7NoST8CMOMi4XfMvC6z4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رده بندی گروه A جام‌جهانی پس از پایان بازی افتتاحیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/92193" target="_blank">📅 00:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92192">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3DL6bdRk-tCu6tIQp2RD7_GDOGG0rPdIB1UfwBakTjAPWnU5puThQ4HSmuTPc6inNGye3Krqx8G-AgVo_9bBs6V1ydppSazXfezAZPHjSW6PQjcmdtr3tAc6eqOrhvaMS5PHWDLKH35WcHpyB1tmWRO49-XU3JzMayItUdyouKPAgMbMVHE7COV3mqjnkRXFSF3nrBYiEnrP4PLZvJjGXg1LFA9t4hI5Yb_kZW8wxj25UUrOuLCNbQ7tTx2WnB2EvoyaQWRLmOVWzGIq05bUK1yt5KIPXCYgJGmajMomeMRdBJcpM4zTNFCEkMFwo1vY3gCmjzTeckWAEEKYKao1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بیشترین تعداد کارت قرمز در تاریخ جام جهانی:
‏۴ — پرتغال مقابل هلند (۲۰۰۶)
‏۳ — آفریقای جنوبی مقابل مکزیک (۲۰۲۶)
‏۳ — استرالیا مقابل کرواسی (۲۰۰۶)
‏۳ — آفریقای جنوبی مقابل دانمارک (۱۹۹۸)
‏۳ — ایتالیا مقابل آمریکا (۲۰۰۶)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/92192" target="_blank">📅 00:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92191">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
تیم ملی والیبال هم با نتیجه 3-0 مقابل بلغارستان شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/92191" target="_blank">📅 00:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92190">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnDxRcR53S-ilL-036nJWmAMEDFhIYi1y1jeyii6HzAVC-iDZgpWiIYmXDJamDVb6cXx8pHQ60bz43Dg64kNpGfdZDSkgjeFilc7clzqn4vwiQfItDUy6s5LGb2m9jRYJUWPGO3ykKwmYEkcXPbxgzwqNRalKOYkmHWYRL0_I_8fgY84zeT3TF1ypljSJI3uulr9TRnr67-0ipjA10AwfxeSIH_h1MXvJn9pJa3MuCIui5fGbCrt7Me3h38In4Y7neDDp4aiF539CGeCaDJEBipgdjDeTMF5iVpXO3I4tTPLEq-lcb8eUvRVSqpLoHdOQo-_lZdKJkP7XgD3AdJGxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌اول مرحله‌گروهی جام‌جهانی|با سه اخراج و چندین کارت زرد؛ میزبان افتتاحیه را مقتدرانه شروع کرد؛ حریف آفریقایی چیزی برای ارائه نداشت!
🇲🇽
مکزیک
😀
-
😏
آفریقای‌جنوبی
🇿🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/92190" target="_blank">📅 00:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92189">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇲🇽
صحنه اخراج بازیکن مکزیک در دقایق‌پایانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/92189" target="_blank">📅 00:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92188">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">عجب افتتاحیه شاهکاری بود همه چی داشت</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/92188" target="_blank">📅 00:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92187">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بازیکن مکزیک اخرااااج شدددد</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/92187" target="_blank">📅 00:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92186">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🇿🇦
صحنه دومین اخراج بازیکن آفریقای جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/92186" target="_blank">📅 00:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92184">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🇿🇦
صحنه دومین اخراج بازیکن آفریقای جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/92184" target="_blank">📅 00:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92183">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLiM7ipB0892GZCOiFDViOzNI0McEwAl9HK_iUKTn3BBhlT6QKzJrZ-Ckn3Ay5P5FgTOKeBeT-kCrcakYw9-317jwGusZfNE0u9jRpEBfAeEPVIV74Q5uzoN8gzc_Z44J15vtPyZFcZbFg5zSJp1Y3ObbhgBTfmMu2-4Hdch-WVt3YF_GSJB2gX4dZN7PvIxP8cMOMW4b4beYNRm0RTShJEUSjzqViRK0KMlRNzklkA9QmyAnELpmC3TCNhrgew6HWZOy0tYgKCnaGo0ZK5DtiPzInZSZJ3xdxwh7aI4oLZ74yLvW9pn79khdtNwOuUPE1evxfDz0Ib5u8tBUcrp5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمعیت تماشاگران حاضر در افتتاحیه جام جهانی ۲۰۲۶ هم مشخص شد: 80 هزار و 824 نفر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/92183" target="_blank">📅 00:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92182">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
دومین اخراجججحج آفریقای جنوبییییی</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/92182" target="_blank">📅 00:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92181">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28a031a16a.mp4?token=OSfLTFxEpr7ZBShIUktGhIUHa4eHQbIgNw95bGTKOIg5492HnTFkWRV-Mxp_XM443F2xNbt05fYj6IRDYD3BAtFVUQx640qlDR3OfbCD8vRyLhvcrNHXLf6j334jTsumPflYfnMhBLtHLN9HAOeNaTEaMcvT009r8BDb4dWqUsq6j9weE1kscGPlUJl5PxmMSCBiAmzPhf_5Lm4302ULSUZv9ebVZsQ7JYECH6B_jlyPJFAg0QTbzE0-vj8PRQ1aKYPssMmF8VQqGP7PmEGvVMxHC_6NhrMZ8ESEfFfZGbmuF035Q2nSWIU2P5ifyUz-YvuG3V7L9uVS9JmXdxXQwCaIl0j6LPAhJ7O4UwCpaLVLXt5iaD-6ij5R8A9sfSupVVy_o_UVCWuRO9YG9h3r2amVziELTFupbrP1xqdvRjuGMRn2YmpddlB5yPY8JTXxrm1JkwWXC7X4hn-Q0P_xkO6qbvTImMyr9egxbnxnzH45plGvxRJcZFaAdp1fE9wRpT-Ura2HwKQlxRMJlbCwDLwJZGswHyiiM20ZVBwBb-lSOZPba8pfupt5L8mocyxgg_LLaRqc31kbL777e-zXN-fKd2HvNcQUwcz7_tSxB5HBXckI13UuqXnDTKtEJnx2HiBiSePEvWAewMPsDwe6Cu9opUMdn-7Fgj4aaQ5CQeI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28a031a16a.mp4?token=OSfLTFxEpr7ZBShIUktGhIUHa4eHQbIgNw95bGTKOIg5492HnTFkWRV-Mxp_XM443F2xNbt05fYj6IRDYD3BAtFVUQx640qlDR3OfbCD8vRyLhvcrNHXLf6j334jTsumPflYfnMhBLtHLN9HAOeNaTEaMcvT009r8BDb4dWqUsq6j9weE1kscGPlUJl5PxmMSCBiAmzPhf_5Lm4302ULSUZv9ebVZsQ7JYECH6B_jlyPJFAg0QTbzE0-vj8PRQ1aKYPssMmF8VQqGP7PmEGvVMxHC_6NhrMZ8ESEfFfZGbmuF035Q2nSWIU2P5ifyUz-YvuG3V7L9uVS9JmXdxXQwCaIl0j6LPAhJ7O4UwCpaLVLXt5iaD-6ij5R8A9sfSupVVy_o_UVCWuRO9YG9h3r2amVziELTFupbrP1xqdvRjuGMRn2YmpddlB5yPY8JTXxrm1JkwWXC7X4hn-Q0P_xkO6qbvTImMyr9egxbnxnzH45plGvxRJcZFaAdp1fE9wRpT-Ura2HwKQlxRMJlbCwDLwJZGswHyiiM20ZVBwBb-lSOZPba8pfupt5L8mocyxgg_LLaRqc31kbL777e-zXN-fKd2HvNcQUwcz7_tSxB5HBXckI13UuqXnDTKtEJnx2HiBiSePEvWAewMPsDwe6Cu9opUMdn-7Fgj4aaQ5CQeI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇲🇽
خوشحالی عجیب هوادار مکزیکی از گل اول این تیم در جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/92181" target="_blank">📅 00:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92180">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">احتمال پنالتی برا مکزیکککککک</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/92180" target="_blank">📅 00:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92179">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">احتمال پنالتی برا مکزیکککککک</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/92179" target="_blank">📅 00:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92178">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/961d7b1b38.mp4?token=mglohma4_2wf1gLghTgaKcg1OygVrx9QzfZFyNIeP5qsxqd5l7dyO9Iu0VNLhCdsHvCfD3aTzKZKyo0OsFFy9Ef3JUAUl1zHRBNmmPmB2TozJoiT10cEaptxyXRPsYrC9GalpC1SkUmfB_a7iUkkz1Z7zimGGL_WaMlz6zVbnXaKLYni6pkhKyi7aRBPikyr-RXHOsK9nAsKbDE6UCY2zzjug80Zfcn7MspPrDIofDHf1rD0lY2fGD_531n_NvdITlSndk-nasJHdDsz3waYg5WR1Uk0gzsFaMpRIaPjGBr-dwVbX4AjeERyK2MsQ2czxoZPetY8cdcriRRYMNanV3m8O-YaJEhp93W8Cn0MWms9s_FMfPuT9XOYOf1aJ2aC6NWwv6RBmqyhO-6_9kfo3YqzFn12BIjbkIBs0jBGtInN-dSC1jWNOxKtwq522x9F2WXpcjHwIkcM4diQU8lWDS4HJLSx0g1Fu2G4iwNoxGBxAjj9fqUuNBoA3u3LVf6l4sivlLVVUKi5SqjYWFdmgbSDFaNN8w7AXqenPh5DVLKDjiLMPiqcczjCTnoVr8GvZpnVZZL71JbDTFLVMT0TGtLH2F4MrASgGo0o337lJ10BUTwyJJEHjGvAN1XIU-cUjg2AmCwZl3RkpMLbsy1xG0OVw095uWYCiUkqyH_-vdY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/961d7b1b38.mp4?token=mglohma4_2wf1gLghTgaKcg1OygVrx9QzfZFyNIeP5qsxqd5l7dyO9Iu0VNLhCdsHvCfD3aTzKZKyo0OsFFy9Ef3JUAUl1zHRBNmmPmB2TozJoiT10cEaptxyXRPsYrC9GalpC1SkUmfB_a7iUkkz1Z7zimGGL_WaMlz6zVbnXaKLYni6pkhKyi7aRBPikyr-RXHOsK9nAsKbDE6UCY2zzjug80Zfcn7MspPrDIofDHf1rD0lY2fGD_531n_NvdITlSndk-nasJHdDsz3waYg5WR1Uk0gzsFaMpRIaPjGBr-dwVbX4AjeERyK2MsQ2czxoZPetY8cdcriRRYMNanV3m8O-YaJEhp93W8Cn0MWms9s_FMfPuT9XOYOf1aJ2aC6NWwv6RBmqyhO-6_9kfo3YqzFn12BIjbkIBs0jBGtInN-dSC1jWNOxKtwq522x9F2WXpcjHwIkcM4diQU8lWDS4HJLSx0g1Fu2G4iwNoxGBxAjj9fqUuNBoA3u3LVf6l4sivlLVVUKi5SqjYWFdmgbSDFaNN8w7AXqenPh5DVLKDjiLMPiqcczjCTnoVr8GvZpnVZZL71JbDTFLVMT0TGtLH2F4MrASgGo0o337lJ10BUTwyJJEHjGvAN1XIU-cUjg2AmCwZl3RkpMLbsy1xG0OVw095uWYCiUkqyH_-vdY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
گل‌دوم مکزیک به آفریقای جنوبی توسط خیمنز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/92178" target="_blank">📅 00:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92177">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خیمنززززززز
🔥
🔥
🔥
🇲🇽
🇲🇽
🇲🇽
🇲🇽</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/92177" target="_blank">📅 00:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92176">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مکزیککککککک دومییییییی</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/92176" target="_blank">📅 00:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92175">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گلگگلگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/92175" target="_blank">📅 00:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92174">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6fb369fd25.mp4?token=BCrXTxmq5XDnaxzgzaHTP9Z3HPW0owesiqwuc6bcsPrzCDnPzu1B2WaG50dl-MyTZV6_X-RR_bTtLm-OFfEW2BBv553ZXgxunVG_Ndp1AeHdHdkkqNEqVFt7RvNOscDESk2YrxJ1sEQBdeo0XR7rrJhAcTXI00v0dmxXp5UR7gC4cxfot2eYRV_NTi_tA0XWaXW5zrfqEm0B852UR3hzed-edokLLZe-A3uLiTDh48rEYnip7b0dqdTBlVD1vhnSuo3WdR8h4eyexHrMSnkUPvLwqSlhhHmRqYDaS5Lg4F1Rg19WihuYnb-Kp0JPBG525SQme-aJZM5v3tvhGkGLW6BrAVsqi3-Iu7OPtJlUZGKV4cvhLb39XxCn3QIq-RZpSeoTM7jD9ml1LGpR6NZM8Qta9lnzAmb_1yhgKlqEapxGP_unndHuxNoSTiNN5XcyClDiwQLHZ9b7NBcSq7mW85rfbvpOBvADGSCf9-xeq2YSqztvSLP5ljt8rwJsMhLn2bHcTY9FK6_d7Fwi16z_AMuho8owFcKwcU5vgePuNq9y13js_XmYV6yPzRQV2j1gRrMmXgP8Cf1o8W59cvVVH3M2OBX12hsCZW7LI0vnFlq_fdLjwxN2IbpCZ6NaKH6gYSR6YWhEXxjhNsBXWCm-Xr2uEtax8fcPdXjA88_Jo_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6fb369fd25.mp4?token=BCrXTxmq5XDnaxzgzaHTP9Z3HPW0owesiqwuc6bcsPrzCDnPzu1B2WaG50dl-MyTZV6_X-RR_bTtLm-OFfEW2BBv553ZXgxunVG_Ndp1AeHdHdkkqNEqVFt7RvNOscDESk2YrxJ1sEQBdeo0XR7rrJhAcTXI00v0dmxXp5UR7gC4cxfot2eYRV_NTi_tA0XWaXW5zrfqEm0B852UR3hzed-edokLLZe-A3uLiTDh48rEYnip7b0dqdTBlVD1vhnSuo3WdR8h4eyexHrMSnkUPvLwqSlhhHmRqYDaS5Lg4F1Rg19WihuYnb-Kp0JPBG525SQme-aJZM5v3tvhGkGLW6BrAVsqi3-Iu7OPtJlUZGKV4cvhLb39XxCn3QIq-RZpSeoTM7jD9ml1LGpR6NZM8Qta9lnzAmb_1yhgKlqEapxGP_unndHuxNoSTiNN5XcyClDiwQLHZ9b7NBcSq7mW85rfbvpOBvADGSCf9-xeq2YSqztvSLP5ljt8rwJsMhLn2bHcTY9FK6_d7Fwi16z_AMuho8owFcKwcU5vgePuNq9y13js_XmYV6yPzRQV2j1gRrMmXgP8Cf1o8W59cvVVH3M2OBX12hsCZW7LI0vnFlq_fdLjwxN2IbpCZ6NaKH6gYSR6YWhEXxjhNsBXWCm-Xr2uEtax8fcPdXjA88_Jo_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🏆
صحنه اخراج بازیکن آفریقای جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/92174" target="_blank">📅 23:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92173">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">چرا آفریقای جنوبی داریم ولی آفریقای شمالی نه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/92173" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92172">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇷
#فوووری: ترامپ: به من اطلاع داده‌اند که رهبر ایران توافق صلح را تایید کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/92172" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92170">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/irxe8fpIcDPOju8NjhdK0xcfZ4mKO_tm7dyxtpM0CBJhGCLxPaLa-sXkGI_nFDs6cn1AJi9iUbzBk0zoOgNNx-UlrYuZ8JM444F1_G8hZcq_yW4W2AEn56KSXqnL3Jy5ucH99OawUQU8-bAnC5qRkPAZjqa_SPeA4XE-mSiR9oF60L4j0JYJcvSMlI696E2QLdeb34qpfDSza7xgFsjjVhzlv86a_MH5okrjtTvAMWYO7-CkM4QdSDW0TGKnK1glH89W3nkEVZz7h-IjdpI8iuLPs7lknN6nEkn8ui0zALfuXaQO35r5sOfKofmy8bjdkN0rjXEfXzjOhKfqRtLPxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KaH-o9ZbaYsyZ9zIkP3PxwM5rhBl5-iMMpUfF8TlrZIAVUVCWLw3WXgBposQJBk7FexfosWmEUdQe1QGjp88wA1PHF6C1phj3MOc8wbQTyleuhKbdiJq2NKPdcXw1XurfeAnBBDgTtusxMx_UoD10WbAEZXiHF2KgnnKrvO_2D1dt49ikD3e98sH8xy5r63eIKOxHbco-zwSFoB6bABx5-Tkg2HrCjDtu_NpvztbEG5l4zVVzORcFcZQVkIW5SdSGXPn8ceSGbuftMzyh05PH7i0bQ-2Mx45sahsd3HvHquVUc_rlGUJbmfdsxnGlf9mBpxEMP9flwWC6PtiZ4AvVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فن مکزیک باشه
🇲🇽
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/92170" target="_blank">📅 23:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92169">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آفریقا از کجا پیداش شد اومد تو جام اخه</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/92169" target="_blank">📅 23:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92168">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بازیکن افریقا اخراج شدددد</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/92168" target="_blank">📅 23:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92166">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇷
#فوووری: ترامپ: به من اطلاع داده‌اند که رهبر ایران توافق صلح را تایید کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/92166" target="_blank">📅 23:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92165">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/352ca9d87d.mp4?token=r7780jnwPEJK4m4gZedzEJlI1Al-ASIS6U8awMq4Mky6ZBjFNZ3zXkGwOG2GdP5MflmPS-mfoCJ-kle7EkL44cWyMMnY62js-rLVsc90UhbahD58dB3_wM427JHdBEo-oxxg03kuD__gBcS8965Dy5joAMlcvMWE0vyg_-oXyFuBzXOu0eJirbHk3qrIai7FuQy4W_S74Z1BirJni3NPW_Ev7UzWosmzQ19RQ8XmIScvs7wfZPY8EnmxvwiY-PHir9WhBy42LJCgXn5XGnl0dHlvzrH--xowJhn7zWkhdIKnDKPNmTmPPSQ92hxE1BdY2mJSpyaK9WiSSOYse5WrHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/352ca9d87d.mp4?token=r7780jnwPEJK4m4gZedzEJlI1Al-ASIS6U8awMq4Mky6ZBjFNZ3zXkGwOG2GdP5MflmPS-mfoCJ-kle7EkL44cWyMMnY62js-rLVsc90UhbahD58dB3_wM427JHdBEo-oxxg03kuD__gBcS8965Dy5joAMlcvMWE0vyg_-oXyFuBzXOu0eJirbHk3qrIai7FuQy4W_S74Z1BirJni3NPW_Ev7UzWosmzQ19RQ8XmIScvs7wfZPY8EnmxvwiY-PHir9WhBy42LJCgXn5XGnl0dHlvzrH--xowJhn7zWkhdIKnDKPNmTmPPSQ92hxE1BdY2mJSpyaK9WiSSOYse5WrHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇷
#فوووری
: ترامپ: به من اطلاع داده‌اند که رهبر ایران توافق صلح را تایید کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/92165" target="_blank">📅 23:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92164">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ریدمان عجیبببب مکزیکککمکک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/92164" target="_blank">📅 23:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92163">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ریدمان عجیبببب مکزیکککمکک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/92163" target="_blank">📅 23:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92162">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
آغاز نیمه دوم</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/92162" target="_blank">📅 23:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92161">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyzX4YtSdNgrwv8hNjuG5XBb5lb4hlRJqqMzvtLtTPBi-ChZSg8V2pzI0oYyGrt-2ZReiInSiSj04IGf8eo935cN5QkQ1L-X_jSuiuVrmkwFcXqcHceqpjfZxmW6GGuxiPGL7HUx6d1ycsAAVqYygweR6vLSvw8ovAWw8WOWKwssYv0LqTH-0hM6SWkIZHhxIy4qhk7LXWcR3HMEbhYZsZ9cGEzyBAMff67qFQBDIdBvQx86liAZhUwwWCNq1qhaTGwSuB3qNtaeK-YsIZ6TMUwIijHr0q3-tNO0ol2Eenvvoq2W5GnSjWMt9kVDYYkbSYsvWqGXGdWDqoZa2u-Row.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏این استادیوم ازتکا مکزیک سومین باره که افتتاحیه جام‌جهانی رو برگزار میکنه
اولیش سال 1970 که مکزیک و شوروی 0-0 شدن
سال 1986 هم بین ایتالیا و بلغارستان بود که 1-1 شد...
پس امشب هم مساوی میشه طبق فرمول بالا...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/92161" target="_blank">📅 23:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92160">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D63HltmRUl9cmS08C6RrWUOCFfVzN-CjOcZWNAROotQNxDyblwxo1ftiPoMKqBVdQRxDUFhM580tKM6QhHkOlZ4MPAv-CGBZkSmtospSHRFPkQo8OzyAh0pE7hz0e3-vSnAK7Q34Yvgrl0bLBYFaaajeV8qpYh4BdCc2iJJKlV4-ioXQSOPddy-b7vXLhP6gJgqNefhfo4tKFDZzZApwcmcYe-PAKTBw1gV87SCHRpOCTzLFatd22X0uxJgmWssZWsXcAH9q-9dlXCK1v54-gegY8346ywwmj8RW7mzvyFJfznP6dHxVrC_mjBj3QGHTwWZMLv7nyZI24Er7y3qgCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇲🇽
🇿🇦
آمار نیمه‌اول بازی افتتاحیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/92160" target="_blank">📅 23:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92159">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1vRDhf0Xqk9JWj3RB8Z2e8-JFpJZPta9scmIYDNzFwoQFJMgfTYHDQ0FrbJTJwlfkAuACD1yHKWSHrvN2kiyiFp88tucON24BDkCeIP_m0LBVFtmSvJL7ilPPRW4WkRkHtpc_UgNwRr7k2kvxrBHz4xDNIYFXgBJKKMI_FFRj8LrpkPSWeoQStA039iSfw6mLHt3jDBX4SVaEGmCOmwlCznj02YclQTkffbKBLAx4ZwAYoQ08krVdW4psIOh1iHzykdTMHQN6kYEE9qyhJ5OKQmkGPmQw9dF3eOMSdxuG_yJiB12mHQnxX4oZfcCnQ5lkF0A-8UJ3KvJc2oATUGVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇲🇽
• برای اولین بار در تاریخ بازیکنی از لیگ عربستان گل افتتاحیه در جام جهانی را به ثمر رساند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/92159" target="_blank">📅 23:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92158">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پایان ست اول
🇮🇷
ایران 23
🇧🇬
بلغارستان 25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/92158" target="_blank">📅 23:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92157">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f357b6ae8.mp4?token=GBl6lInDQLLB2GDnNs2uo-uQ8jAjUZDRrPll9qroAvW9yrJZeGSUFEERutM3oSPcPfsPjl2OVAfACh6BEHXb3t1m2sm7jaqgj1Huw_536OBLMRHDRzcvh_gs3tNyTPDu0lezbyDBIZgvytmPRXVbvIengLXJAVldlFZPG8FYYTs5dsEZXI22_HvDuxrQ54e7kL7m-P4hIF2WM7HtqHCz0PE1yMW1CztGD6HmGqTmGKP-hsRI61l2WDu-UOiQTGqdqIThcZLO4sKp4PM25TuaEtscXEyca0uvSolOmJIIvWL6eke3wiw06M6ZF-ycnYkM7RsfaAuBeBdWy-pN_AnRSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f357b6ae8.mp4?token=GBl6lInDQLLB2GDnNs2uo-uQ8jAjUZDRrPll9qroAvW9yrJZeGSUFEERutM3oSPcPfsPjl2OVAfACh6BEHXb3t1m2sm7jaqgj1Huw_536OBLMRHDRzcvh_gs3tNyTPDu0lezbyDBIZgvytmPRXVbvIengLXJAVldlFZPG8FYYTs5dsEZXI22_HvDuxrQ54e7kL7m-P4hIF2WM7HtqHCz0PE1yMW1CztGD6HmGqTmGKP-hsRI61l2WDu-UOiQTGqdqIThcZLO4sKp4PM25TuaEtscXEyca0uvSolOmJIIvWL6eke3wiw06M6ZF-ycnYkM7RsfaAuBeBdWy-pN_AnRSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
اشتباه عجیب در دریافت تیم ایران باعث شد تا بازیکن بلغارستان با ساعد و در ضرب دوم امتیاز کسب کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/92157" target="_blank">📅 23:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92156">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">من از این کانفیگ V2Ray گرفتم، سرعتش واقعاً عالیه
🔥
حجمش نامحدود واقعیه
، بدون قطعی و روی همه گوشی‌ها کار می‌کنه.
تست رایگان هم داره با ضمانت بازگشت وجه.
تک‌کاربره حجم نامحدود: ۲۴۹ هزار تومان
دوکاربره حجم نامحدود : ۳۴۹ هزار تومان
پشتیبانی
👇🏻
@khadamatsup
کانال
👇🏻
@apkdownload_sup</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/92156" target="_blank">📅 23:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92155">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⚽️
پایان نیمه اول
🇲🇽
مکزیک
1️⃣
➖
0️⃣
آفریقای جنوبی
🇿🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/92155" target="_blank">📅 23:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92153">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مکزیک بازمممم ریدددد</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/92153" target="_blank">📅 23:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92152">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بازی شدیدا کیری دنبال میشه
😐</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/92152" target="_blank">📅 23:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92147">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مکزییکککککک تیررررر زددددد</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/92147" target="_blank">📅 23:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92146">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/92146" target="_blank">📅 23:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92145">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بازممممم سوپر سیووووو گلر آفریقا</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/92145" target="_blank">📅 23:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92144">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
وسط این بازی کله زرد هم گفته قراره توافق بین امریکا و ایران تو اروپا امضا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/92144" target="_blank">📅 23:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92143">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بازی دوم تیم ملی والیبال ایران مقابل بلغارستان هم شروع شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/92143" target="_blank">📅 23:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92142">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ولی دلم به حال اون پسرای میسوزه که فوتبالی نیستن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/92142" target="_blank">📅 23:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92141">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وسط نیمه یه وقت استراحت دادن</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/92141" target="_blank">📅 23:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92140">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBh-5sDm34FXUXusXi_8Dtqb2O4ksV4CtZFSoTaE0r2fEQFziBCgVnnUPXxj4yaA7IiEMQRYV0cTQUAS-1JdAoCu36_mF-CNRYOaqzfO3IzGCC1UUakDMjSfWXLX7Xzrbl037vv7n7ZD9sGR6G1GBY8THoV-5HZq8VhQptozuMdqSq3ckydLc3wcKva1BdLmjQG68rkUaL7OqsuY5OfB0t-FYcah_cXusJ7aDjJDSItOCqYwHH19ILYLd5HcNVZurlzxzoWNDk9Z7749rhXtVo9QhzZuvthjnYWJWv6z6lMkry8W5PdAFgZ99Cr-s8suHNugfEOmAMEs5hImI6T3cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلزن مکزیک این آمارو تو القادسیه ثبت کرده🫪🫪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/92140" target="_blank">📅 23:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92138">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دومین کارت زرد بازی در دقیقه ۲۲ داده شد</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/92138" target="_blank">📅 22:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92137">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گلر مکزیک کسخل شد یه لحظه
😐
😐</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/92137" target="_blank">📅 22:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92136">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fMi_lKhXr8kUdJFWSFD4TRpoRm91LVkF76v7bFvQYv8mMmSi-1XJ3W4flyv88aAsELUbB0tgVTnggkL6QU9HsEMKty8qQ1jxpT0MhOXcoCA5YF_V2yPWvFsFdCnscb17yRv0d6BlQsYfRnly13whQdc8gtyEY-BDlT2Y7P6DEMdc60MdWGDwxydkr--P9-yiQ9EcfzC7XUoUG55dSuxOq01RCuuepFrg9c52eUPHVurZPPHNzrpSiDRKgOvbcS-5xWU1qr1dmfXbbstN_PUwnjTNQpQ0pOEZoWxfkBBLLCEB_xAHu_-xZqysCtcUzBNfPzWoZujH0mp6hYjzmF92zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکوربورد پنج دوره قبلی جام جهانی
فک کنم امسال ازهمه دوره ها خفن تر و بهتره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/92136" target="_blank">📅 22:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92135">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بازیکنای آفریقای جنوبی وحشی بازی میکنن</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/92135" target="_blank">📅 22:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92134">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🏆
🇲🇽
گل‌اول مکزیک به آفریقای‌جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/Futball180TV/92134" target="_blank">📅 22:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92133">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مکزییکککککککک‌زددددددد
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/92133" target="_blank">📅 22:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92132">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گلگلگلگگلگلگلگلگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/92132" target="_blank">📅 22:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92131">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مکزیکککک گل اولو زددددد</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/92131" target="_blank">📅 22:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92130">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/92130" target="_blank">📅 22:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92129">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🏆
سوپر سیو تماشایی گلر آفریقای جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/92129" target="_blank">📅 22:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92128">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گلررررر آفریقا چی‌ گرفتنتتتت</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/92128" target="_blank">📅 22:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92127">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مکزیکککک داشت میزدددددد</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/92127" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92126">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🏆
آغاز بازی اول جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/92126" target="_blank">📅 22:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92125">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dv3BH2dHZBdVNjRKEzTLi20JnGCMWqRpY85lIHkjOwEGX85llsAmPpl6v-OWZbSJpGuRKVVYiiZYKjBgLFC-hGv7HoVRlnLNSvNjgp29i3WkVtUuRlY-W-NXUdR3oZVY8YXGrbM58d_spKCvkz2oLL8lrcIHgveV2XnPvzAtgU54TVyz0uvaz6iidiR-z3ErA2jRC8Bo6IwqZ1HSL1FiPXzLL1v1UJECMDWUct_Y-evnfoocSV6m0TAnMPlSEfEP6WjubotXM3hQM9LI6K3gadJcri9PaWB7QXjSCJI90WYr9rvWTl9K_6CKZlp91lLkVeIOHwfOdaNm9D8J4fcXmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت ادمینا که مجبورن وسط جام جهانی تو همچین شرایطیم پست بزنن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/92125" target="_blank">📅 22:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92124">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3fd70679e.mp4?token=KbXDHiTk0ukhgmtsxX4tGkOrKPfkrPFxQeOxu9QT2aeP2mkCM5dCGJEwuDeOzdNfOocuMPacmGcom9cvw9N1tz6k_bPkMpbMH3sPHou58T7RT5DIdOKXyPBvLfyQRLPKYzsb9DN6HSk4K6W57yu4Z_VH59LOcZG7qmabRRiHGm8fJF2c3H_CKQvqIWjDZY1KQ6o8qZsvJuBRz6E7WjP7GpxZmupuEQD4iLxrtuooVDExmYst0NCw0yipbWUQ6Jz-7SSw9L4lOCx3W4v21-Bx6cXrbH8gLgtUshB-gbXReplxN_E_8oYJO4Zlo8ywlnss3nGVy5QHYmc2jWV-cshQHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3fd70679e.mp4?token=KbXDHiTk0ukhgmtsxX4tGkOrKPfkrPFxQeOxu9QT2aeP2mkCM5dCGJEwuDeOzdNfOocuMPacmGcom9cvw9N1tz6k_bPkMpbMH3sPHou58T7RT5DIdOKXyPBvLfyQRLPKYzsb9DN6HSk4K6W57yu4Z_VH59LOcZG7qmabRRiHGm8fJF2c3H_CKQvqIWjDZY1KQ6o8qZsvJuBRz6E7WjP7GpxZmupuEQD4iLxrtuooVDExmYst0NCw0yipbWUQ6Jz-7SSw9L4lOCx3W4v21-Bx6cXrbH8gLgtUshB-gbXReplxN_E_8oYJO4Zlo8ywlnss3nGVy5QHYmc2jWV-cshQHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدمممم
😀
😀
ابوطالب اومده یه برنامه ساخته واسه جام جهانی با حضور حاج بهروز که علی پروین رو مورد عنایت قرار داد:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/92124" target="_blank">📅 22:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92123">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yez3AjedMfDa866rtgQWaCgB9viBEw0I17dSGdNNsZuDaqhtFnCaPHUIb3ehnlaE8zcQ7QxvYY0ChvZ66jZVkupuq7-WSpMmmEt9T76rH7yrPWDLkZyECsCxcPp_7xGd8tmhbkbJ-z-194xHT1dnkT3uLhIV9e_1xji2SCl56_sKxlPMdWGNkrZ1OMUcj8iFXpli9aBb_8T9SzCfUzCQYOAXW72CVCPdm8eYQmSW9CWw5J5SOJL_PD-bRmP2B1DHOqin4arq752vQOZrfwjFxxDYaMBEDZM8quzH2RxEqnlma-F0cg_1Q8KY4QcUA4qESfd5ynTZtUreWB1C0AQg0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بادوم زمینی همراه با جام‌ وارد زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/92123" target="_blank">📅 22:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92122">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAVf_f-ykWDAKLYiUupOivxy0nuUgfpqqsxELtPw9jKLxjFzp3-MuZXjHmz30y_BkE_KOAU5n-b5rcj8bvpfhqi2NTBgzET7QyjGDaJiOD5vOXAGCu2msZ_U4Kzk05aelp14EHSpRLxubiYOABtS7ILgwY2CmNAfFUnbAEvAeNIDNihrft3hrrHoj7gfgVnKbBgdRzbzz9LV7K2LDtwYe58yZJFstO2DF2AuiKtIUkhB94Yn5gx2E3LQCKfdJdKxSaT_UZjfgMrjxbkWQ_Fk3UTW5ZvfOk0kJzW74YzFy3cD3QmNU3DcLXNodiFje98oyXzC1SZGq0tw09IBy6cTtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📔
رومانو:
🏆
برناردو سیلوا به رئال؛ 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊 بزودی!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/92122" target="_blank">📅 22:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92121">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15e74f9b5.mp4?token=Z6qRgH2ycjnMoeLcKXROliBai2KAKJpvs0OZrT2E3TyTyrEmT2E51Km7Jo3Zb7pnsJZLUp_OLnrj34cIiGu_YiT4CcYALx96W3jy-_kYXXY-hxynisg4L8twoVtA2kUhtUcotph6rTZ4IE-3z1ENW5psgLcheVaSrObOXOXmBEXq1ftylgI3laVLjFzCJb8HSUtFv3bvX7Tqs277So3groZFLURql_mXKbLGANm2ZU_EXVeTwMMx-g7mwwryS3PHXEOzU5qfzhi5uXeTavzjut_YWzZQs1Tf0Q655Qc3fGK7AdpUl9NIYRM3SKc1otwkKQtpybplBpJZhrE3FoCRPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15e74f9b5.mp4?token=Z6qRgH2ycjnMoeLcKXROliBai2KAKJpvs0OZrT2E3TyTyrEmT2E51Km7Jo3Zb7pnsJZLUp_OLnrj34cIiGu_YiT4CcYALx96W3jy-_kYXXY-hxynisg4L8twoVtA2kUhtUcotph6rTZ4IE-3z1ENW5psgLcheVaSrObOXOXmBEXq1ftylgI3laVLjFzCJb8HSUtFv3bvX7Tqs277So3groZFLURql_mXKbLGANm2ZU_EXVeTwMMx-g7mwwryS3PHXEOzU5qfzhi5uXeTavzjut_YWzZQs1Tf0Q655Qc3fGK7AdpUl9NIYRM3SKc1otwkKQtpybplBpJZhrE3FoCRPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فردوسی‌پور و نکونام نشستن دور هم راجب خوشگلی دیبالا حرف میزنن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/92121" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92120">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇷
معرفی تیم ملی جمهوری اسلامی در مراسم افتتاحیه جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/92120" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92118">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjGdXuNK5H-AFYHmN41UxcB5frHZOC2VDVl81UYOF_etwGxOWHUOigvAXUui4Bk-j0Zu_Chrr10yJqnhndpDhf0WCKVVc5vDAAQ6vCMaCACUuMWKaZce-FCXhcSvFzL236vRxqJ98z-FT7ehFZF34ZEg9k8PjAXw7buya5RevDbVe7K3vuxyyCPgDJbngo7K0XvVJd4DiW6QT_U9PXOovMGPhLCJHkuISlEODf9IKApbZWNKP9J0IaDeDRM-Hqi7Ep7MF6SsqQPChlvhJZo1YjQeVfY2a0UrJcveDIq_lKxRoO-e-3hKINyOixz_s-DHf20eqDBGxqaWJ8jfaQS_ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا 30,000 تتر جایزه ببر
🎁
💸
فقط با
پیش‌پینی
بازی‌های جام جهانی در
صرافی‌بیت‌پین
😍
بزن رو لینک و شروع کن</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/92118" target="_blank">📅 22:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92117">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIRMHXIgyGKhlFiZQuKnuUXyDH3aGEPLvCip3nbQ0ynQTdwoip14nzNoeCxOTA4Svz0BckypQ4-m29nHG67G8kFeZWITDDP3XVeExxpOdrbgiLL4E7RM1tmmB58j_b6eAel6At59xiNpMU_7ZslgkqkwdIbYb81as19-e-WX7wCZl-QxrowXrDpDWPge1xNkYD0EH_uv5RbVWnI-VVdJ3H_jz-iDYBhIgXcLSstnbk42Z0wmP4qU1pVRp6BuEfMMpoCviGPQYnNvt6Q6BZKlkI9C2mQrwLCgxN7Wvz4LIqs0R9OXL80PVM_KAF-_8f9P-OwkrIVxKPUh55AGApFQqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جیانو اینفانتینو:
بیایید واقع‌بین باشیم، بهترین کشوری که تاکنون میزبان جام جهانی بوده است، کشور قطر است.
🇶🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/92117" target="_blank">📅 22:00 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
