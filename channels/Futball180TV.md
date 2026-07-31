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
<img src="https://cdn5.telesco.pe/file/Z94rPtLCt9ntGAgePpfzjchZ_JqVA6gFLKnzwPb3nDFBUWn-8CFcOZ_hGqrI7v92SHOaH-haX17CN7KzjNTijwlSs4YdsIVsMgf2g0igPslQW_M0LlyX129bxZSZBVK2Yht-qWqOss4w-810z4Poit7_Z_wMMk4kJG-_09YypHEYvGDsV7x0wUZRe7zAMPcSiPWSpw4IsTgx9XLrUnZ8AB4XLL4Yovm9GtZ96PABwTcU509d4HPAGs4ff9FSofaVf-33dgWpiEtMG8HA_sbRNFCediNf8beyW7P1W1OoHqb_pnxrWvwv7yQGyGw0VTc-gMmiDhXA52vyY6FOzIDu-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 509K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 12:12:47</div>
<hr>

<div class="tg-post" id="msg-102410">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b5a4f433a.mp4?token=aeCm49yvCWSiL77lQU-lI0JqQz61z-hMB8_QgN9cl_zOIFPX-DfFIy_6nemxPliq2dZTyEIA5Fb6Cv2quKZOArZZjYvF12_ykZ--5eA1nar4bVszh2i2aT8apdZIJaHQg4uVfQGPcuQXijYV7VKTd7jKeUhA7WM-3AyicZ9Ou5i1LLCtQcIn9UiObem6ExSxtrDWUxInZ6oeLjDw2jpZP7WK59wi3FQ7F--zNya88YHlIazTwam0_hUpwH9FKmPHHYRwLpa2chbqBVq8IgWX8lWj9Bj5Qw5ROlkM7XnL3vHFAnjqGJMDD93a72RHQ0TzeF5yOX_Y3lQMNepVJKcFWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b5a4f433a.mp4?token=aeCm49yvCWSiL77lQU-lI0JqQz61z-hMB8_QgN9cl_zOIFPX-DfFIy_6nemxPliq2dZTyEIA5Fb6Cv2quKZOArZZjYvF12_ykZ--5eA1nar4bVszh2i2aT8apdZIJaHQg4uVfQGPcuQXijYV7VKTd7jKeUhA7WM-3AyicZ9Ou5i1LLCtQcIn9UiObem6ExSxtrDWUxInZ6oeLjDw2jpZP7WK59wi3FQ7F--zNya88YHlIazTwam0_hUpwH9FKmPHHYRwLpa2chbqBVq8IgWX8lWj9Bj5Qw5ROlkM7XnL3vHFAnjqGJMDD93a72RHQ0TzeF5yOX_Y3lQMNepVJKcFWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
🔴
‼️
علیرضا بابایی مدیرعامل چادرملو: تورنمنت سه جانبه به دلیل کمک به پرسپولیس برگزار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/Futball180TV/102410" target="_blank">📅 12:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102409">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=RzCkqd1wndnwMQgUAB0b7tNjMm1N0Z-jLV6ij4NsvAWp4EKK3xcnLtHzj4iR6q80hxWwmbXKyXPux0We230jTzkej0muGtN0wenNU9T57Yns3vmcNWPbcWnfabHA2HSdWjeIYPE-x4XnawTfkgh8WQ9mtBejIBWa0UUb1KcLeQQfyTngoCqmrYzEo_uXquvDW7WmQjTDTDQHsfcwrei3TxjAyZ6GHEmpa3kXtYNMJjPUFv_EOThasMwhvPg52C1amhl95cfof7bbCEWYauRD0SQ8d71Y27Dt0Fg1Pu959gu-mOo80IusxhJ57-BYouEb_JVqTBs0eLoIsLmGze9dAF4f5aplsbngjmtaIV_V9DNhsbyqjPiMO7AUyR1lUmiXTZFPwreoPH9cPoGCuQooDtPiHryHQ7Es9XXDTaTS9uVwRXqn_JWPN1KsoEKN7-w6kRY4sc6GIjYEZ3JQKFjyRqArKBA6Y7MQIrHEeYgw6L22iwBqGANrWncraMlfkIG0BLUxv3lu8yvRss5OmF8rSaXpSTardjH-ywplPDoOWsYEWVOGNrlKfgKLfCGUHslaJk3j3N1ICtu14vq1X1rPnkHCo0uN7U13CapnWUtW7bltKNNfmmMCDdpnWKwtp8h_rNE0-l_jXNHxn-Uc4v6K55nhEIsnU3baVjbpDyMijPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=RzCkqd1wndnwMQgUAB0b7tNjMm1N0Z-jLV6ij4NsvAWp4EKK3xcnLtHzj4iR6q80hxWwmbXKyXPux0We230jTzkej0muGtN0wenNU9T57Yns3vmcNWPbcWnfabHA2HSdWjeIYPE-x4XnawTfkgh8WQ9mtBejIBWa0UUb1KcLeQQfyTngoCqmrYzEo_uXquvDW7WmQjTDTDQHsfcwrei3TxjAyZ6GHEmpa3kXtYNMJjPUFv_EOThasMwhvPg52C1amhl95cfof7bbCEWYauRD0SQ8d71Y27Dt0Fg1Pu959gu-mOo80IusxhJ57-BYouEb_JVqTBs0eLoIsLmGze9dAF4f5aplsbngjmtaIV_V9DNhsbyqjPiMO7AUyR1lUmiXTZFPwreoPH9cPoGCuQooDtPiHryHQ7Es9XXDTaTS9uVwRXqn_JWPN1KsoEKN7-w6kRY4sc6GIjYEZ3JQKFjyRqArKBA6Y7MQIrHEeYgw6L22iwBqGANrWncraMlfkIG0BLUxv3lu8yvRss5OmF8rSaXpSTardjH-ywplPDoOWsYEWVOGNrlKfgKLfCGUHslaJk3j3N1ICtu14vq1X1rPnkHCo0uN7U13CapnWUtW7bltKNNfmmMCDdpnWKwtp8h_rNE0-l_jXNHxn-Uc4v6K55nhEIsnU3baVjbpDyMijPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
علیرضا بابایی مدیرعامل چادرملو: بازیکنان را از پای دیگ نذری آوردیم و با خواست خدا پرسپولیس را شکست دادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/Futball180TV/102409" target="_blank">📅 12:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102408">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=hTfDp_W3Qa--rmRTY5hUPsEqYi0632tXR0DNmRz4hEVZcH-BsPUMi5m0satUgTJu8agFfe_FjxYc2NxWLLXTbG7ddPg4TMwxMZ-OaTBtEdsUxoT884FQqfzwlRpZWMNZZmHmvXZUEpb9ykLb9Gu-N3IFiH-_5GfEdnQdPHXTUaoSO5OaHCbishizOMaT1oZ9_eCwrxJJLcoRhJ5pO-E_y5pNg0kJsAsX3VBDX6t9QRyPtN-jIULsx7SiFLB7LIw9LrGNm-JYe6YSLoQoz0FqmQrSYBvqhlpyxfJpeYYK5NQ5R822CtidJheFTBrzk6rDu-teCWjKukRgtKX5knvXvXVoYiqY9nTVpzEQqCiHeC_jwIuv5iiRTF7P4dunYfuXsTVNGdQujlQL3MvEMRukirn238SlZULPoBP466JMCwYY6XaDOy4SdVjJqr_2RhI-4l6EvfHzRWlqb-3J2kLbBssy0L22mCY6PTxX64Z5IQ-FZL7syZbW_GN6JaByBm1dDArvlX_ErfFJiVXtKTcFMBzuC_5DQh-03wS_HRcs2IKpF4G6vud7MhisQ_1s1r8vgbVP6n3EwsVl8K7tnFqXbKkk0q18OzR-dGXqqQFCffxXGL1PcfYrJphor4-_AWBii8z_qEKtMF0br2Qjsldt4g1TmqwQFggGfenOPmQVvNU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=hTfDp_W3Qa--rmRTY5hUPsEqYi0632tXR0DNmRz4hEVZcH-BsPUMi5m0satUgTJu8agFfe_FjxYc2NxWLLXTbG7ddPg4TMwxMZ-OaTBtEdsUxoT884FQqfzwlRpZWMNZZmHmvXZUEpb9ykLb9Gu-N3IFiH-_5GfEdnQdPHXTUaoSO5OaHCbishizOMaT1oZ9_eCwrxJJLcoRhJ5pO-E_y5pNg0kJsAsX3VBDX6t9QRyPtN-jIULsx7SiFLB7LIw9LrGNm-JYe6YSLoQoz0FqmQrSYBvqhlpyxfJpeYYK5NQ5R822CtidJheFTBrzk6rDu-teCWjKukRgtKX5knvXvXVoYiqY9nTVpzEQqCiHeC_jwIuv5iiRTF7P4dunYfuXsTVNGdQujlQL3MvEMRukirn238SlZULPoBP466JMCwYY6XaDOy4SdVjJqr_2RhI-4l6EvfHzRWlqb-3J2kLbBssy0L22mCY6PTxX64Z5IQ-FZL7syZbW_GN6JaByBm1dDArvlX_ErfFJiVXtKTcFMBzuC_5DQh-03wS_HRcs2IKpF4G6vud7MhisQ_1s1r8vgbVP6n3EwsVl8K7tnFqXbKkk0q18OzR-dGXqqQFCffxXGL1PcfYrJphor4-_AWBii8z_qEKtMF0br2Qjsldt4g1TmqwQFggGfenOPmQVvNU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇪🇸
مشکل ایمنی ورزشگاه‌ها به لالیگا هم رسیده‌ و تیم رایووایه‌کانو نمیتونه از استادیوم خانگی خودش در فصل‌آینده استفاده کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/Futball180TV/102408" target="_blank">📅 12:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102407">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a01fbf75.mp4?token=XzEt7Y7hISi-cDjUUgKb6k75w9H0-AfgB5Ey-Khfky_R8TkncnLhZF_3ygZuwHZBfu7IRemZV1gniDuGFpuMDhNh84gqwTbo7Ga_DxOc6mc0LemHlxDmFTIWqiy1WPxXHsjOAMsj28qEKe4PkHxkguKS3G5NqzXdzrWdqZ5zehqUDEkXa-jEM_qPUYoohFI591QM_P2qkvyekEpv5gqbY_Nqt4SSQYHok2OXgtIFETF7LlIZlWZX5YoPytcH2XZfrzMYedfVoHk2F-xdDyQTScytQZY2HQeMztPAoE6qQU46EyBLrphxONzDqRlqTaztfaONTigENqK_JWH9Gv-stg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a01fbf75.mp4?token=XzEt7Y7hISi-cDjUUgKb6k75w9H0-AfgB5Ey-Khfky_R8TkncnLhZF_3ygZuwHZBfu7IRemZV1gniDuGFpuMDhNh84gqwTbo7Ga_DxOc6mc0LemHlxDmFTIWqiy1WPxXHsjOAMsj28qEKe4PkHxkguKS3G5NqzXdzrWdqZ5zehqUDEkXa-jEM_qPUYoohFI591QM_P2qkvyekEpv5gqbY_Nqt4SSQYHok2OXgtIFETF7LlIZlWZX5YoPytcH2XZfrzMYedfVoHk2F-xdDyQTScytQZY2HQeMztPAoE6qQU46EyBLrphxONzDqRlqTaztfaONTigENqK_JWH9Gv-stg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو وایرال شده از صحبت‌های تلخ و بامزه یک ایرانی حین ورود به‌تونلی در بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/Futball180TV/102407" target="_blank">📅 11:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102406">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262957043c.mp4?token=n0_YmwG4LIqx_NN_zOTqfcuSU-qvKHy_3Ti_VGOnH0uvu-LNjTLrjypURbmEK4ebHvQT148GAd-ibqtXyq_FFdGPnLWSX1ct3gUVrKRy_TcHNqeGnSaMLzvM0kI_kYRyisbCEVrMf6qOFtXXXeK5PkFJ0qGHfGlNQClWUZwFoJPVPey05SOZ9Epnbg8rxrRQ8PP037U9nKW3yiyor2aPuMOyGrdXv7mQ-ovO0zDvjlZaC8k1kMJDDwOZfjDxsD9dBl39AGnZpM9pE5V8wNyY4DEStJPxW8OCcbfJfVYoV5slVbvwGSg-Mm3vSEUW3QXnzBPehNE8oqISUllAtKTNgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262957043c.mp4?token=n0_YmwG4LIqx_NN_zOTqfcuSU-qvKHy_3Ti_VGOnH0uvu-LNjTLrjypURbmEK4ebHvQT148GAd-ibqtXyq_FFdGPnLWSX1ct3gUVrKRy_TcHNqeGnSaMLzvM0kI_kYRyisbCEVrMf6qOFtXXXeK5PkFJ0qGHfGlNQClWUZwFoJPVPey05SOZ9Epnbg8rxrRQ8PP037U9nKW3yiyor2aPuMOyGrdXv7mQ-ovO0zDvjlZaC8k1kMJDDwOZfjDxsD9dBl39AGnZpM9pE5V8wNyY4DEStJPxW8OCcbfJfVYoV5slVbvwGSg-Mm3vSEUW3QXnzBPehNE8oqISUllAtKTNgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپرایز خاص‌ ژابی‌آلونسو برای فصل‌آینده؛ رونمایی از ستاره ۱۷ ساله قزاقستانی چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/Futball180TV/102406" target="_blank">📅 11:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102405">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2180d890.mp4?token=UnPIE_XkIgYljwrt_Qj6FsE0FaCB4AWzN2ZlSZYRSDiKTvKJKOXYE2_JJPLctjZOXqornLZayscHCJgehbsjurnCZIepvwfHdO6cf2TMpiSwgvx5GitND_U6hQU8Ztf34ML0fnW8sdAsiF4GB7g_eqfPdpaZXZ7ZasummX7hRwmbu_okuTBDQUdE4DeoJ0OP-RizUtn39Ez2GI_trdR3qRK8La_k55ZamIcUaNxoI4DqkV9wQbuNim5T1oIB2-_XzUIRuizEwG6DqJq9zUDYulgPyUnUF5FAPoOLT82XuyRcju_2jlkrvW9w4MyAGIKO2rJrsdWQONr89MM_AckU-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2180d890.mp4?token=UnPIE_XkIgYljwrt_Qj6FsE0FaCB4AWzN2ZlSZYRSDiKTvKJKOXYE2_JJPLctjZOXqornLZayscHCJgehbsjurnCZIepvwfHdO6cf2TMpiSwgvx5GitND_U6hQU8Ztf34ML0fnW8sdAsiF4GB7g_eqfPdpaZXZ7ZasummX7hRwmbu_okuTBDQUdE4DeoJ0OP-RizUtn39Ez2GI_trdR3qRK8La_k55ZamIcUaNxoI4DqkV9wQbuNim5T1oIB2-_XzUIRuizEwG6DqJq9zUDYulgPyUnUF5FAPoOLT82XuyRcju_2jlkrvW9w4MyAGIKO2rJrsdWQONr89MM_AckU-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
آماده‌سازی استادیوم نیوکمپ برای فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/Futball180TV/102405" target="_blank">📅 11:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102404">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31c9897d6.mp4?token=rzj-GnaW7Lkc8Tg1sJ3IYsxpEkmiXuSvkwUrlCjZmxUOncah77CKcs20mCENV4AjjXXZQRv5bqWQZbE2jILCz4R55VlaoyZ-GfUUvF2Z3EWgP947zZiI9wJYHQPwOI0FKF-KnaC9A_74JICXbRd0ityaxglmyJuX1ztyeOB-0Fv6Cn10nlymt_YdWa-MlUy5B5OFgROiErs9SdsbWMfb7AaGN9ixA1wap7LFpHBqmCWrnDUC9QyOU9D-zlwEszthd2gmRpC1lka2LCAhzfg9aTeJYXTgK0vJsV4QdXiMc0TRD6vlQI4RImfBAIK1PEQmUF_jao2kjek6no_PW2h10g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31c9897d6.mp4?token=rzj-GnaW7Lkc8Tg1sJ3IYsxpEkmiXuSvkwUrlCjZmxUOncah77CKcs20mCENV4AjjXXZQRv5bqWQZbE2jILCz4R55VlaoyZ-GfUUvF2Z3EWgP947zZiI9wJYHQPwOI0FKF-KnaC9A_74JICXbRd0ityaxglmyJuX1ztyeOB-0Fv6Cn10nlymt_YdWa-MlUy5B5OFgROiErs9SdsbWMfb7AaGN9ixA1wap7LFpHBqmCWrnDUC9QyOU9D-zlwEszthd2gmRpC1lka2LCAhzfg9aTeJYXTgK0vJsV4QdXiMc0TRD6vlQI4RImfBAIK1PEQmUF_jao2kjek6no_PW2h10g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
پاسخ‌تند و کنایه‌آمیز مهدی‌رحمتی به صحبت اخیر معدی‌قایدی: بذارید تو‌ توهم خودش بمونه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/102404" target="_blank">📅 10:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102403">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
کیت‌دوم فصل‌آینده منچسترسیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/102403" target="_blank">📅 10:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102402">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/869e38d1a5.mp4?token=JE3oXaQIcJl5VMC6RWko3urdr4xDXT02GQ5hx7muWpmzih-MkrOCrOPtx9wa7jNh_swhSG1kSI1eNrzG2RELxmTMs1vO0iooQ0dbQmtv8VzwUwkonG67Jd6E9T2z23-_a0MdhbwN_1F_o9pIbfJdZXH5DMfQYO5VR0fonlnXwXRpk-aY9RFPxMT6V22OjzLm3ABYGW8KNkS3gETDwDQfoN5NuvI421cRUqz3r2eJlsyjfg3FHZNv6La6O3IJNwCYFUhnhi-IgNPJ4If2YCjt6OWt-PJT8QfuF61Puu12mpB4nzV1LCbNiXFrKc1LLBPa25IcS31kVXAM5tuaOC2r_zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/869e38d1a5.mp4?token=JE3oXaQIcJl5VMC6RWko3urdr4xDXT02GQ5hx7muWpmzih-MkrOCrOPtx9wa7jNh_swhSG1kSI1eNrzG2RELxmTMs1vO0iooQ0dbQmtv8VzwUwkonG67Jd6E9T2z23-_a0MdhbwN_1F_o9pIbfJdZXH5DMfQYO5VR0fonlnXwXRpk-aY9RFPxMT6V22OjzLm3ABYGW8KNkS3gETDwDQfoN5NuvI421cRUqz3r2eJlsyjfg3FHZNv6La6O3IJNwCYFUhnhi-IgNPJ4If2YCjt6OWt-PJT8QfuF61Puu12mpB4nzV1LCbNiXFrKc1LLBPa25IcS31kVXAM5tuaOC2r_zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
درگیری شدید فیل‌فودن ستاره سیتی به همراه مادرش با چنتا از مردم در یکی از کلاب‌های شهر منچستر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/102402" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102401">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0266060c.mp4?token=iwHU_DiJ3CDNCdfOPVnUpMUhOCJYio-kL1skJZaGTIivjI59KuLhroDF62FO2w9proYLQjBFHvCHsl6kSj_TdqRjr8Q1jBEE41klFL32jUd_yirKV7VwZRXb8CXI9UHjNzQdZ3dAR_-HRyYfdR1Lm7hf2GsLSWmZaYaVQhar8H2Gq-a8A1ZHsOLbDBW6KioQpB-68_87QckKOoxt2vfXfuMbrJOHoKThFvqgPeNV73Znx5qUS5111p_2gNDl5DgJ-_IPvJFEpQ1Bsnabma0gPpTk7E9OJJnUglx-hDD-_e2B1fWMItoe8l4am5r_3UajgomEWLXDUsyOnLRLbnyeCw8umgJAco50OwEs_PolyUjBgX7jOQfLAMEmVvMqkflin5GpKq44GNqL38g9MDabQKLsdZzjVqaNnQkcL1RREUOlBgM9m0_R3_3fB8gCBq78k0cKiJDfSxUjQe5SO96Ur9BzNoLCMqCaHYvFiOfq0XaZevLaq6Bd-TuDQekJNSNiy4Bxqu0WUi9dfcymRNKjcaVe_oFsBGrs1LXXQsz0e6nbtI6yrExP1U3IKObZldREfhxzNy9YJUsyEd8PIJ8L2cf70pypupYjvK23G6SpYMbHFAa1zDqfhY6yqxiuiL7QW5tLyjBfTmx-HJSI1v6-dG5HZjkEeIf71Tl1Lc1Rgtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0266060c.mp4?token=iwHU_DiJ3CDNCdfOPVnUpMUhOCJYio-kL1skJZaGTIivjI59KuLhroDF62FO2w9proYLQjBFHvCHsl6kSj_TdqRjr8Q1jBEE41klFL32jUd_yirKV7VwZRXb8CXI9UHjNzQdZ3dAR_-HRyYfdR1Lm7hf2GsLSWmZaYaVQhar8H2Gq-a8A1ZHsOLbDBW6KioQpB-68_87QckKOoxt2vfXfuMbrJOHoKThFvqgPeNV73Znx5qUS5111p_2gNDl5DgJ-_IPvJFEpQ1Bsnabma0gPpTk7E9OJJnUglx-hDD-_e2B1fWMItoe8l4am5r_3UajgomEWLXDUsyOnLRLbnyeCw8umgJAco50OwEs_PolyUjBgX7jOQfLAMEmVvMqkflin5GpKq44GNqL38g9MDabQKLsdZzjVqaNnQkcL1RREUOlBgM9m0_R3_3fB8gCBq78k0cKiJDfSxUjQe5SO96Ur9BzNoLCMqCaHYvFiOfq0XaZevLaq6Bd-TuDQekJNSNiy4Bxqu0WUi9dfcymRNKjcaVe_oFsBGrs1LXXQsz0e6nbtI6yrExP1U3IKObZldREfhxzNy9YJUsyEd8PIJ8L2cf70pypupYjvK23G6SpYMbHFAa1zDqfhY6yqxiuiL7QW5tLyjBfTmx-HJSI1v6-dG5HZjkEeIf71Tl1Lc1Rgtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁳󠁣󠁴󠁿
نظر سرالکس فرگوسن درباره‌مثلث جادویی بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/102401" target="_blank">📅 10:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102400">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f864b5c9ce.mp4?token=rxolQvcPvP-QkV43_bZ3QM4-_ncyZv98JPFsBnLP5lii8iXyADuctzoKfA-Qq-Q72ySpDmZxZaUMNGFO5TSAeOQcpkgnOFJYO-J7StB91XZwKB3OGqMaeILtv6_S5jHIG8l-bgzn724szV9diJpfXYhfC7hLjAFhb8Fg5m0iS1R7Yg-2pb0XPCr_HwBYm3b4oSYEsbj5-KJQQ8rrmn8AxoVYw5ltI3a4LM2OY6kRtdq0ltrSgvUmXNRdssnRGKE_Yz37mc8E-k9-mNkw7SLVivTbmm4ecxn1bHGhFEXJHpHQ5PNkRjCI-b9ztrwXee2gm3BKgD7IHo_NafEdhcYVDGh0GR06OZpNKnKdyYllSyLIuKeMvKQfpioL1SLgAvIlwlqpWbbAEpwZYzDLo-zPptib6fODaOwns7M7CwEt4acqC_6tCYdH9jrQgAf1JfbqlxFPVffXx4RBg85C9yokjGL4iD1iXI1FdE5fv393JYXH-gEH5j3RXAxs4rVzOqSVPt7GV2aEQ7C18AKR-KDJiwDCTq1JX-NbUHz3xyBgLNgc_Q-FMHPsye20WdXhtxIX9Xa2XQRyhMxetXQe7WvjKxgvzK-ZBO2_VlkHYqnl4pfpIytZHrsb54u0-iKVqRC6AwG55w4HCaUJ1cfL2Q-eik-Ye8-QWiD6LAt9bWuyc2U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f864b5c9ce.mp4?token=rxolQvcPvP-QkV43_bZ3QM4-_ncyZv98JPFsBnLP5lii8iXyADuctzoKfA-Qq-Q72ySpDmZxZaUMNGFO5TSAeOQcpkgnOFJYO-J7StB91XZwKB3OGqMaeILtv6_S5jHIG8l-bgzn724szV9diJpfXYhfC7hLjAFhb8Fg5m0iS1R7Yg-2pb0XPCr_HwBYm3b4oSYEsbj5-KJQQ8rrmn8AxoVYw5ltI3a4LM2OY6kRtdq0ltrSgvUmXNRdssnRGKE_Yz37mc8E-k9-mNkw7SLVivTbmm4ecxn1bHGhFEXJHpHQ5PNkRjCI-b9ztrwXee2gm3BKgD7IHo_NafEdhcYVDGh0GR06OZpNKnKdyYllSyLIuKeMvKQfpioL1SLgAvIlwlqpWbbAEpwZYzDLo-zPptib6fODaOwns7M7CwEt4acqC_6tCYdH9jrQgAf1JfbqlxFPVffXx4RBg85C9yokjGL4iD1iXI1FdE5fv393JYXH-gEH5j3RXAxs4rVzOqSVPt7GV2aEQ7C18AKR-KDJiwDCTq1JX-NbUHz3xyBgLNgc_Q-FMHPsye20WdXhtxIX9Xa2XQRyhMxetXQe7WvjKxgvzK-ZBO2_VlkHYqnl4pfpIytZHrsb54u0-iKVqRC6AwG55w4HCaUJ1cfL2Q-eik-Ye8-QWiD6LAt9bWuyc2U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
شباهت حرکت‌های یامال و اولیسه
🔥
😮‍💨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/102400" target="_blank">📅 09:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102399">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5630cebcb5.mp4?token=BjjyH5byYJu7parSGbVxgEYPG96Rz6B8P2rOojU0bJN4w6BDsfKJbRil-93fHSqfF09fbh5UNJSV-nLDLjP8nS5RhtbM1Gpw-Ss-9JpnmzDZ19wl-XDquTncj2_G0oWLDaJBd-yMEUpFvZTadHMgZPnxDrfRSc6yAOrvy7hI4MZnB4hil_0V4cvKTIwDMsIhLwXDioBaHkWyZacB3pn57A3XhgYYSzKUMxTxOTHCPDdkQ_zoWm9iEO0mrEgHZgv2zXUVMR65SdRurhpG0FqJfnnzXGwhr_k4mdKvbxVn_1MfYdN_QQc0cLEJXetjkXqbj5pd754ge6Jzs2ZiFBicYWN8khDNA171IifoPf_jF8RVsQcrSllvExIaO7i2BWv3vBwkK5xwFukTwhs44BHFf4qCOUEd3AZp8NvFmN0SMS4-Gfu9cAyjWWs47uOi33jSpESNi3kNaPdNYYS5X9mGk6AWZ6hDWyuojZU2Nr8rIleEA2xaLdS06DEaKOOkhkE5iiEjjMW63jJo6s8Rj_ZsJaaT3yCzg-r8lzM13QmK1CK_gXQPvjZuFlpNJmORSV82hkrfgFiXPPc5W_p_JuGsahuw4Z7h49QQQTfbk6meSETHnSZUUQYRfVghGALuG5YYkCsMdP0XHtDU0yy1FjWHQ4fRHc2nlYq8rLihDSG1CXY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5630cebcb5.mp4?token=BjjyH5byYJu7parSGbVxgEYPG96Rz6B8P2rOojU0bJN4w6BDsfKJbRil-93fHSqfF09fbh5UNJSV-nLDLjP8nS5RhtbM1Gpw-Ss-9JpnmzDZ19wl-XDquTncj2_G0oWLDaJBd-yMEUpFvZTadHMgZPnxDrfRSc6yAOrvy7hI4MZnB4hil_0V4cvKTIwDMsIhLwXDioBaHkWyZacB3pn57A3XhgYYSzKUMxTxOTHCPDdkQ_zoWm9iEO0mrEgHZgv2zXUVMR65SdRurhpG0FqJfnnzXGwhr_k4mdKvbxVn_1MfYdN_QQc0cLEJXetjkXqbj5pd754ge6Jzs2ZiFBicYWN8khDNA171IifoPf_jF8RVsQcrSllvExIaO7i2BWv3vBwkK5xwFukTwhs44BHFf4qCOUEd3AZp8NvFmN0SMS4-Gfu9cAyjWWs47uOi33jSpESNi3kNaPdNYYS5X9mGk6AWZ6hDWyuojZU2Nr8rIleEA2xaLdS06DEaKOOkhkE5iiEjjMW63jJo6s8Rj_ZsJaaT3yCzg-r8lzM13QmK1CK_gXQPvjZuFlpNJmORSV82hkrfgFiXPPc5W_p_JuGsahuw4Z7h49QQQTfbk6meSETHnSZUUQYRfVghGALuG5YYkCsMdP0XHtDU0yy1FjWHQ4fRHc2nlYq8rLihDSG1CXY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شیرجه زد، گرفتش، زد زمین، شوتش کرد!⁣ جوک خنده‌دار بیلی مک‌کالاک ماساژور سابق چلسی درباره‌ی پتر چک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/102399" target="_blank">📅 09:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102398">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SF1-yhk5ZPwncMpxE04gU0qNSxjDG9sTLNYsr8WxQ4IUNzL4QudpdxwwjMy0yd1ykz8lwv6B3XDLMzKwM084nKxxr4w2ShjdBp6_5HtWTn-LkiH6FGV05EL51b490xEg7Ai-ptp6UhKvAXYynnRcQZ5XoC-GwLCTC9TG70_WSokqkfONd_LvgC3VRIe0qOtMtJd5XiTMKZcyuppel_s6jUKx-Qye9olhm-nnDa5C3kUI1WXgNbVNYl0hjc3xHV2cUkPdGqylVkfAbYBMPuqNJWzHUKvmNqqA98k8O4B0nrcGxzNh7sktKE-LcYiXMvuRnhd_V8V8tiFaVSaw6Hb1Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
🇮🇹
لحظاتی پیش، فرانکو بارسی، اسطوره فوتبال ایتالیا، در سن ۶۶ سالگی درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/102398" target="_blank">📅 09:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102397">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d54a6dc02d.mp4?token=KBghbBdkTbEnqPsWphy71_vTIdjJ8EJR_VeXPmQlr83Tctralg87rMC5YDDe9VBLgPYIivaWZ_9-UwI_MfKo9gPJ5_pNAnNwq1mlEi4C_OsanVFlVtByu12WnlU6gzrhVj6u5CaETGKdY8lHsEbFoG_XXvz--n29ZKDRyPGe7oN5yUDfpe1CtET_4NJnuVDOTjqAqwTCb3ZVoMLAZ2oFRSXqGwy7zbftsayst5tNkPXimwT3r1exPqu_sRcEsEmFMF0LEVESpG9Karkcf1XxBE7aKdqmZqY4Ok-DInUILB7fAzg2Wbm5XMeRTJ6NWCUmec1tmm1lkD1yvW8wHH3b0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d54a6dc02d.mp4?token=KBghbBdkTbEnqPsWphy71_vTIdjJ8EJR_VeXPmQlr83Tctralg87rMC5YDDe9VBLgPYIivaWZ_9-UwI_MfKo9gPJ5_pNAnNwq1mlEi4C_OsanVFlVtByu12WnlU6gzrhVj6u5CaETGKdY8lHsEbFoG_XXvz--n29ZKDRyPGe7oN5yUDfpe1CtET_4NJnuVDOTjqAqwTCb3ZVoMLAZ2oFRSXqGwy7zbftsayst5tNkPXimwT3r1exPqu_sRcEsEmFMF0LEVESpG9Karkcf1XxBE7aKdqmZqY4Ok-DInUILB7fAzg2Wbm5XMeRTJ6NWCUmec1tmm1lkD1yvW8wHH3b0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت فوتبالیا اوایل هر فصل
🤧
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/102397" target="_blank">📅 09:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102396">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e396ec62ed.mp4?token=gfGuOc2NowV-pHHaSYDbTJvD2oOeLezU77YcIGE57HMlBiRiLMZ8jbuknAxcAIBMB3xVJ7RiudH-qEDDXSFD8evvzVSU7bhKFKWJz8l8qHoJrY1JU7U3ErNVIpDW-G81Z79-LnpyyYybKtY4IbUQRaD5nFs_XgpdnF-6J9vxiZO0RgFZjtFI-o8IVQ3jsjslhZ5nhxi0Rj-gE15MnrSXWSHk17NvUE27wxq9mXF3MbEB6Ik6fUjd5MV6v2nifDUgYYjV-V0YEgDKvIrGLk8EQr0OSwzaPjR8kuiL5ZHTpnKJSWb6gbvX_3omqWqyuh-WReB-Oprzz64n9lbRvN_GSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e396ec62ed.mp4?token=gfGuOc2NowV-pHHaSYDbTJvD2oOeLezU77YcIGE57HMlBiRiLMZ8jbuknAxcAIBMB3xVJ7RiudH-qEDDXSFD8evvzVSU7bhKFKWJz8l8qHoJrY1JU7U3ErNVIpDW-G81Z79-LnpyyYybKtY4IbUQRaD5nFs_XgpdnF-6J9vxiZO0RgFZjtFI-o8IVQ3jsjslhZ5nhxi0Rj-gE15MnrSXWSHk17NvUE27wxq9mXF3MbEB6Ik6fUjd5MV6v2nifDUgYYjV-V0YEgDKvIrGLk8EQr0OSwzaPjR8kuiL5ZHTpnKJSWb6gbvX_3omqWqyuh-WReB-Oprzz64n9lbRvN_GSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
نظر پرز وقتی مورینیو میگه وینیسیوس رو بدیم به تیم‌های دیگه تو این پنجره نقل و انتقالاتی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/102396" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102395">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6u-DIIpODXzM2PIULJFifFpAyMcfodoiieKgM1OGuCzSipPzWBIb7_Dw9utAtrq0ZtWSOSthOSJSIoNj4nn6Xwx8baJwWnfwyrVRlWMJxK9_p1RnX3no3Wu-jeuLCv5Oh7wm0vNLap6m4jZ0TtHUMK71AAeM2GEiibVNtBavbJyUmq07EeQSoh8NV_I_VDgEDtP3PK06giZ3wxDlAcSXffWssNGmMVzvFDvDWJrOkmYx9_1l6jZU8J6asUzfN5iyLaaDKUsqNlMb5pXusH21mGpWC5bWKZb6BelmQVjmPQvUcYKKsNe_mmTI1Y-Rq4Ney7B2E5wGh-tPiqqHQVt3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
رومانو: حاضرم قسم‌بخورم که دیومانده بازیکن رئال‌مادرید شده و فقط تا وقتی لایپزیگ بازیکن جدیدی نگیره قراره رونمایی رسمی انجام نشه. اگر این اتفاق نیفتاده باشه از حرفه‌ خبرنگاری خودم کنار میرم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102395" target="_blank">📅 03:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102394">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfVj1U7IiPlU25S1ytVEL69YgSdgPQqZY_0ZzcluOBiAscTTLP-RCJ_Xg2Tr5mAabH9U1knGLeOu9pnoqIb_KCHtjHb9pYaFWEg2L4rniK0aPg7Zm1lfCqqaQ4CcUB4DJdiQ3I-SozhL6kcB3-Eb8xGo03PTxTiEC_Sv4yidB64W4AdhHEb-s8rJN7DRa-h4_SyVjCvuAX2JSSS9H5WfvnsF70MhlaxmvGHwKzM3rggr1E5GkUwE5-z-8P7yWxYaRS5pFM18GVCJhRN2-bCUmwrvak_8TGvS8Yel4PoTktwJi3YIUrpkgjzPalD8qtBAhM2IpPRzFT5PdLcIRbG21A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کاسمیرو:
خوشحالم که اینجا هستم و به لئو مسی کمک میکنم، او پادشاه فوتبال است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102394" target="_blank">📅 03:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102390">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HmCSEQLeRfu0FgFvxGyGXzhuS0GUuNrAPXwk1TTjloW302wnH1WZ2C8mN6hAm78L5frqQfDj81ZX5FGLSMeTl7mQT8YlsW3_Cag7gdKuz6SotkrlrmEgnkdcUSM5ardpsVQs6yeY2RZMgneGz9F-zB95c79WsawyMG63hFmVn9gZHfETqsUQuJcvuA2aSwDRWHk3kqEm-jenzjayqKHm5431NTdt1tA9SR0iMJHyYpqNcHOc15J2KxNVkACn5EJFXx6RoyKjDmNEhNCs6bCI5LdVaGL3v0od2qB6igr24P_2W53Jt3iD-qiUH4xRSGj3QJ4s6jllaPSz9TwMxm9vRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vrk6kDWvQOyCb2LYAmoL4JqpfkDBsyMKfhsZEouFH2zqCxaI_3WON4myvKhyhPM5TS5SjIR7_wQlv5GrWff6Ypjl4NFb_l_8q31kvj6XbiD58Mjt6t-Ktxmf8ZsjGP5UV2r8-0AxFymJC9imTwOwWKBAQqRBMc1-TiNa0I7L_C9HiLUMqy6PmA_gZCgf7jDvlEMMoYI89u7ZeQjZ12OOA2IKrm6Fgy5B-ZvHVIyxMJCo2CeuZPWooeUSHooIA5W2sdVV3QoSV1Q6czDSoH0l12MaFjNjEOychfKHVlKF1-kiwztlc8D7K6eJ3lEGB01kYrnZFrZNA7-jcydOG4Lhdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sz7Aqp19dumCuBJt9BhiTlKBQmwjMCHeZJ8kqtMEjzwDVPCOy6KhvNyZvZPLFZdtQvJZN33lmqxC3Ont2w2FhDfSbdEDbNTQ1fLXDv3hjvW5PWlUR-VkzRJaI5myswMtn-U046yskNjIPxKiCDuMfFAHRdVzy0cUjCLoT2RwaiLbs-38CO4luplGlSTT2ixc_kI12SzITOqBu8CwJxmRpxt6s-E2yHCPwQxGomnd93gh88ZvsvbKBbPhWzZ-rRhSuBKNYGUq5cm0UF9Zt3N0wAfswxTP1X7EjgW1DSWszDetKEMkQ-3PawO1VgD2pwjJfvefCghH2KdZ5Oc8NtlyZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NghHiHD6utRz5aMlzmeUhDzU0GeN7be9BSUClcOxMjrGdjpUR5e35Ej2Hhg1wwF3OgcvKuByF_nUB3dZjymfRa6mgj5g2dKqhr99y0zW-kBrpfiJ8eClyCPTrIoV5WccK3Cu67HznBdpvPc6vulLCJbey2_K0zbCDLLtMmnAe32S_w4gvOM4yW4MAdWOS1D_qqe4uQY9R_hiy9GnTnKsgvdCxNTt_u5t0UJdmzNT_5AP-pQqA7uaoz6B20njEO8BVTfOXnaAEkaR1H3jO4rQyNZdQ4ZuF6kUbDriIVA2UhOURTL0bTFILeQvvogm6OuOQv-6VUOvwiMHKaD4YRX8Yg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریس و جونیور و جورجینا رفتن عشق و حال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102390" target="_blank">📅 00:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102389">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/511459b235.mp4?token=BpZGaIWpLHDTKRC6pQkzw_O81aPZlDfCTGwr1TaVS2pASv_DSsX0Q6DWoHo3qazV-VuPSGgcEziDYtw2EUuvsvBy_MCyj-_hxYM3A8TVUgYZJnP0L9x0jhBgnBtXlCqRyeoRkA2f8Zx0MyAwYG19wC8LQDUnvFtv09hDnv6VdBWgOtRuh-l4QCpUm_m1-8yCLwI0F3Qt3ZKKx1_0lOM8AExao3C_PBFwtd_3cfMQdS9kTm2wOoj5_niZd3Qt11W222YyzzMOMRphefMenOlaGdj66sO90CbRzLzz_mvtC0-JNkd1NHw3qvR9sOjG5XGbcxa2qSzkdLzWfXiqHhAdUIZzvBSx22mef0TZCkWue5sCA_SFu4SP4iWYj6mdhEtZu_8mKVr1qpDsK-xzF9HLglmD6mG7W-BFp6TZa9Lu5eVtJkw-GK-CJwJhYchvHU2ZwXo7hy08QzdF6DP1YqbMuIc5AgRFuVUd6c5hgISy8xXwVLjcxsRu4g_axVAncEPa2PWwdKIQQhdIDiIIdBKg27sMPyEE2aAFvPLmvTgsok5FVSXVZBFbMbvceC4KcDRhicMUyZt2_7cqUwQSXPO0Z_B0LlPvjUXE4o-ADqM43pc76ZDFl6MFeZ6dlZcSmMoF_KUP6uhztrp-oeOTnxy6nM5zx_ejB_tpjIAaJ2ctSO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/511459b235.mp4?token=BpZGaIWpLHDTKRC6pQkzw_O81aPZlDfCTGwr1TaVS2pASv_DSsX0Q6DWoHo3qazV-VuPSGgcEziDYtw2EUuvsvBy_MCyj-_hxYM3A8TVUgYZJnP0L9x0jhBgnBtXlCqRyeoRkA2f8Zx0MyAwYG19wC8LQDUnvFtv09hDnv6VdBWgOtRuh-l4QCpUm_m1-8yCLwI0F3Qt3ZKKx1_0lOM8AExao3C_PBFwtd_3cfMQdS9kTm2wOoj5_niZd3Qt11W222YyzzMOMRphefMenOlaGdj66sO90CbRzLzz_mvtC0-JNkd1NHw3qvR9sOjG5XGbcxa2qSzkdLzWfXiqHhAdUIZzvBSx22mef0TZCkWue5sCA_SFu4SP4iWYj6mdhEtZu_8mKVr1qpDsK-xzF9HLglmD6mG7W-BFp6TZa9Lu5eVtJkw-GK-CJwJhYchvHU2ZwXo7hy08QzdF6DP1YqbMuIc5AgRFuVUd6c5hgISy8xXwVLjcxsRu4g_axVAncEPa2PWwdKIQQhdIDiIIdBKg27sMPyEE2aAFvPLmvTgsok5FVSXVZBFbMbvceC4KcDRhicMUyZt2_7cqUwQSXPO0Z_B0LlPvjUXE4o-ADqM43pc76ZDFl6MFeZ6dlZcSmMoF_KUP6uhztrp-oeOTnxy6nM5zx_ejB_tpjIAaJ2ctSO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل فردوسی‌پور بعد از کلیپ دست‌بوسی که ازش منتشر شد یه کلیپ گرفته و میگه ویدیوهایی از گذشته من رو گزینشی منتشر کردن. هجمه عجیبی علیه من اومده! من اگه قرار بود چاپلوسی کنم الان تو صداوسیما کار میکردم و نَود رو داشتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102389" target="_blank">📅 00:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102388">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlHZ1OzHkfq7VPCtZq2RmLVm7a60BAffpkdRQNYWuPZSvfRe_lzRnZbpbJMrItH1o8tmj3zCQtrAfeYQ1TCZDUJjN8TyovWTX_zCWD23M0VKDkSHZ-IlothpOKr16osaqx9-2_7mPVsWNC6Ap7WsOkyLdbKWtW6fCR6lytGXP1qYV-bsI82qvS6KC8LVt8Ni7DzLLg5Sa0NemsngFN4AuopxyMXtwf1gw2Ip9aD7Me5tms0wo-X8t6JjD4pjswQZsKGrzoYSAk2HifBaeTx6tcIwIiPdLsTytWg8xUz98hnO4oCcQzClMb8LIciEM3KatUORyI14mJwkidmjre6WKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری: کارلوس اسپی شده با بند فسخ به مبلغ 25 میلیون یورو به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102388" target="_blank">📅 00:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102387">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBSWY7uIqWKgOHOQ-SxjnqIlDObQpFB3boezBvLEsq1ntfRrtJZOn0py0imVSUQ-tRCp8Drv7xuLcpKLRgegej5hgvv4w6NdwoXvOIwDxWwtyRl1tUG-EXDuVEsfoy8jhN3NTBXmUwb8mJO1bwap2FTYhjFQUD6fIsBIvmJe55746piQA1BgDeDrij4HiHgBEnlqVT7-F-NEIB5nI5RLHAgWxIFUnNwYvWe_MXLiNSBBV8O0z8tDDvMIvfZxPxGwZbx6qx7MksRrGjpiY1PoDx1cDW9RXXA5JaltnxJOqgvghrLSiRoop6_kUZkm-al_FVebFoaEhdNyQPUDiZ3buA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری بلینگهام که رو دستای زیدش خوابش برده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102387" target="_blank">📅 23:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102386">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae65f1051a.mp4?token=L9coTCBKLqnWofIFP8HDhD2MCjFa1mwTkPaRwZUbZjES-X0M1Oa7CJE_nGyYN-GcrUNhN4_NAA0SLGsshpJiOp-Q9q11rI_hK_WyyljIiFXtYUMqaiXLzBkFDBXZE0r4YvwgTjWAVURnXjMts7a6EoE1-Wu_buiLERg3j6fh-jP7I75BjBniOVCSDVy4EP0_HmlbOuwMhfHDIXl6X6WVRWXNHPysp0KoMKafgBlNEtq_cFWh_6gQDYvJBjGpkaj9w3sWHHjeqAZ1SNJiyQIzQu8SQMPRY_KSdxjeaPirWgWlAoy5Pj-GN7nCsLPubBzBypZtWoYkfLg65kvndjiJOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae65f1051a.mp4?token=L9coTCBKLqnWofIFP8HDhD2MCjFa1mwTkPaRwZUbZjES-X0M1Oa7CJE_nGyYN-GcrUNhN4_NAA0SLGsshpJiOp-Q9q11rI_hK_WyyljIiFXtYUMqaiXLzBkFDBXZE0r4YvwgTjWAVURnXjMts7a6EoE1-Wu_buiLERg3j6fh-jP7I75BjBniOVCSDVy4EP0_HmlbOuwMhfHDIXl6X6WVRWXNHPysp0KoMKafgBlNEtq_cFWh_6gQDYvJBjGpkaj9w3sWHHjeqAZ1SNJiyQIzQu8SQMPRY_KSdxjeaPirWgWlAoy5Pj-GN7nCsLPubBzBypZtWoYkfLg65kvndjiJOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
روایتی جالب از تمرین‌های پاری‌سن‌ژرمن؛ جایی که حتی امباپه هم از دقت باورنکردنی مسی شگفت‌زده شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102386" target="_blank">📅 23:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102385">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvAX6t0C0AP-Noawa3OFS9ontZOCrW1tg9e-WGI88gwG6AQ3rCZzCKgwNoe4pmuqIXSACBOnV0pVNN_1M5WfxFz1MDWqvLtvXTm6uOGSNFynf7toZcz-bp4x6qMiZ0TuftDEh3E4pTlIvpdFxlBc__a_VtTR-AfSIlMX37wBjpQ9ewDIFj5DUMwrlsiALaDBrciFSnpGcRxpTHaAIW7xc7wIKdkcJbg1YQRVZMmuB8SVlfpkAIyHW9keXCYdJPj78dmQZx7dRzcGtj7XIC5L38BPyDr_9E7wXpdvFSO-14gDkorVXdB6dw3GalGgIznQYQC2BWjzrKd5YGtqD8V6vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اولی هوینس:
ما حتی به امپراطور چین هم اولیسه رو نمی‌فروشیم چه برسه به رئال مادرید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102385" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102384">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYlFjJbZxttLH3nKIF9rMW-1Eaaxz3-8JiZQcbbPxjjwAjTNSsy9Z_ok7ZfOROjVuW4GPKqm30h808ugOIHrV8H7p6KqqWjc2zCc0WcvoDGrYQm4vGSl9rL_fKFZz9aF06Pw45X3TY7af4DVLvF_r32UZFA8_PiNKOgY7ZTyHE6Kk6TEEjtxXd3X3gDnY3apnnKl-jiWiv6ZNsyZBYapUNRFO17dAXBJUOyaVDb6boNDq-e7eZ2hFX_ldqbEexqKjcUA53msNYxQZzgeRjB7IAThO5v9fE4SA0Fqsn7_U0ILpUU1MlRSOEEEC8QVxcBxGe6ceMzYFCeDtXETxloB-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
رئال تو این تابستون شاهکار کرده و همه اینارو فروخته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102384" target="_blank">📅 22:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102382">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AGfTVLdNnnKIiMqf7nFtG_3Yf_UbnfkOH4vEx96TCT9e7wtZq3EjdaBfB69mL-Ze4zeog5JxsrudhGlFEiC-YCakGa1bk4jJdFiuvuqfF-VL5gsDZLJRANnRfNipsJeLUL0M0_oXLneSmLPKmawZvFsgFSNX3RDBLAYpY5bcTU10YpsaPpADvY4c4m4MlONxEiRGivvAI_dK1bHrEoD0KNIl_r93Iom2yclN-D89M33AVqLgcUt5liWfHtsVbolY7litfX6K67bj9RjYLZlsAXigtqOjMcpOvY5q5Y5RphufyxwI_tIAZnrzTtyvqVNippDYO0zWwPro2TNLTXaNfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WZ0OCFb2p0xoEf3VRSDV4omsFvuYe-WIJXEc08uHmrpeTOUt-xWaoHmoW1QlIEPESD2DDTCdtQekAOA_DC8PsPIqt5HGwd7ZxvW5E-xdzLrfi6ONvvJCRQBG3VVF4UC6SdPccX_2sC1-bHV15J5uqiWFC55i95SWgFrNq1Daxvou-H2Hz686HQybARryeWbvlCJ27nO2hGyyUF2linOh0ey7xhYATlO8_81edrCYPm4McIzBAlacsDyfOSGSR7Xiz0WNjObrGh0a44LbDGDtC-YnJD1rBAoUuykNIdrebu8Sw5r9hO9miopoG7f75OfTeasz4Ti78V1eitY5RsqVHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو در 2003
🆚
رونالدو در 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102382" target="_blank">📅 22:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102381">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-text">▶️
زودتر حرکت کن؛ راحت‌تر زیارت کن
🔹
همه راه‌ها به عشق حسین(ع) ختم می‌شود؛ اما زمان سفر می‌تواند تجربه زیارت را متفاوت کند.
🔹
اگر سفر خود را به روزهای اوج تردد موکول نکنید، هم مسیرتان آرام‌تر خواهد بود، هم زمان انتظار کمتر و هم خدمات بهتر.
🎥
این ویدئو را ببینید و بدانید چرا
«سفر با برنامه»
، بهترین همراه زائران اربعین است.
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102381" target="_blank">📅 22:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102380">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epKUuna1OW5bNk7Ce4m0Jet_-up7kgJe3Zb1BQUup4on8imrQ3NBBgCIHGLw2vxlkluINnbnZMZKBQdqT-iXM_eINOw1XcdM62p0JQlIvbZAyCWUpReSqqD8zWJrkLpxPhfxTR1D9tFZQGROXE93qM4De5gOtixbPNRuenPUqz-I4nS_5AyfAlfS_NWpCxfqfQCE5WNVl55VF8_fWPIwHJT3bBR7hre8x__R7cR21sMdXxUKVCapmQzwzrcuvelazBfvzGEbq_o_zaN0dcZUbEgfDJJXkdZ8XQ471_sKrvIBvwsGL8tTuihzWZiYwYCa6jfT-5fGScveYK31AcUEyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری: کارلوس اسپی شده با بند فسخ به مبلغ 25 میلیون یورو به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102380" target="_blank">📅 22:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102379">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQVgUtqQN3-UJAAvuh5VwmltILgU-pjcyUI8i7_wU1BXxFDD_opCgYemCZTTBPMgFWfyxxuEvg9AxlXMFmsDXO6ZD469Nx0kgQ-gcKt29bNYFAgwK9uqCgdyKMqQiZvYgBqVvvmdZrTyXh7Oq5oZP2ZRGvJnhii31EvDDOFqnpgNXvA4w1zccbepKpj_GOYKsySWWg4AOCn5kO0LyDFy9_NmHaO0aCVspsphtVb-JJxSp51NSkO5US93vMVo55tHkXMCv35zpfzbigb6LgvqYnuzMLzVgyoLCwPpEVs6m-QLTnodHSLsVUq0JgoANXSHlzbJbPZF3Fkv08fL90V1gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییرات وینی تو  فیفا اعمال شد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102379" target="_blank">📅 22:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102378">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjpVXpuOYIImt_2NtSjFJQ8jB93UWb3_bXsIuUtdSAGPZu_bEIbYU0_1UJFj7HHi5tN4n666mpuhFWOYv9EEwEqd10WQIoIrjNnGklb58fUVF3g75ZBTwgSNJYKqfnf-WshtuqR8unJCUNsTI6-elYllgb9mHyD39A4879J7U5yVIrNLlXFRGC4pPISjpDyc8Il6TS8ggZyC-9xEipDnGnBhLX2KCHwHmGycucnT0Ij-Db99NmYNr0owFQcOxyLg5dUlZzjColHjf10apPWzQDpBj53_niZLEdid4QJtUUnKQk6t5ogNLrmRx0xE1EuwKSurL58nNMqi--ypeHwukg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بایرن طبق معمول به این تیمه تجاوز کرد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102378" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102377">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4MmRsl9_eVxkPaoUF9_H1qPmgI_BY8ZQoS2YcDp5tN6dW2HAS7AhUfi13VqHRAaIBG1VFxm-pfL8RP3AVd5MFX_z1a7sQZ3Njk-w4ki-wniqa4Nu-PZ3bYPN8joQ2i_m_BK7RXAibf1v4956cRUi4qiGQ2SGAcOUpFjcD37uZURU2N8FFpTXGatO25-V8fedtLdYhbjjvZVTw_nPNtkyrI9VvrLfMRMfnR5AZuKzP8d9Bj9AxtYrJSJVRlTiArBHeeW9vm0qZxFqR94mYzQ5SoQLuapTb1fRb_kZkc2iFdkIf_5c_UduegvBILHwnb6Sa3MEKmVXq37UTeVdo2n3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه فدراسیون انگلیس:
ما در کنار همکاران اروپایی خود ایستاده‌ایم و بطور کامل از موضع مشترک آن‌ها حمایت میکنیم، ما با برنامه‌های فیفا مخالفیم، جام جهانی متعلق به فوتبال است و همیشه همین‌طور خواهد ماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102377" target="_blank">📅 21:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102375">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhE9JsW1G3TXEq8r9oj8qhZ1RZTY9TWze9NqExerkloiwRO-OWMTxLXyBO5YLoNSWPv4WtPtt8FzL5uQ1xZmUrg4rmD439tn8k__nBwjuoeV0HKcxTGdWBj1KOv4Ns5RUAxg_QozVJVbufOqKPjkquUb2h6sMHLafC_2bWjIdmDJlipzwNzekmEf4FVpDmhF7Xr93gObbock6iJ65OI_YK2VDWwR6ez3r7UFrewUaQa3urbtEj4gPzVFMxgMUjIsUT78J9milmpolgz-Qa0Ic9UrI3hdPH2ctp2FuFRrk5YwK7ZFaTUxYDableKj3JifSEtEQHo2ZPyh_6t3Wk0KsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
اسکای‌اسپورت: منچسترسیتی برای فروش رودری حداقل ۷۵ میلیون یورو میخواد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102375" target="_blank">📅 20:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102373">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlGUMCXF4I7ZeQAvKAdtFUPQ8roV1Z2rZOSooIv5gWYGeThCmdowVJpm884P_07Lxnde1wQtxrC_TFHXhgfqHJzSJCeWbm_Fx3DvFoPt6546ybeeDJyMyIVYl3xQGpslQ0nDtjOP1ICpbMY1Qb_QcQcORa5fICfiXywOoJDea9qCb4M-LjmF6XbeDvtORithY3By_w8r1xe3nkExrGIcizW5_to4oGzkLul4YiTfZJSQcK0P5Rfc8VIJE1l8OKBvFI6jpDUwkRSR_3IOLeghZ3dkT1jAlIGGa1fY5Dm18qGqVbtJoolMH5SwNzrhZw6WO-SK7xzgkil5Ge-cxHKwPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d9c0f441.mp4?token=vtRVVx8daHKLNbJcL1jzvZvYJ5naLnuYu6DEdXNt8lN-uWqE0r0EYf1jHh8yPg9vJPNtQrgaM8PztmXE763OlgB48QMxDWfRHB8a3KVicod2V93AYyjpvXVXJTRwackBtqKJf8MBvtpFe6Ynlkdeztwc8n2htiJAQ2w0e7eKCE7dCTT8kkvnkQ2cXqlcxuwVYu3zrW3w5Fy8_SIRk6ZaHZdUTKsGgQbuske8NVmqmf_3ZVQI_mlg03bt7woOX5CFuPabFbuk4or29HcsDaSOGUneLkWFNuQaNRcSvf2xZB5O0WmZDat6zF1VA5n36Yrh8DVpy8ivpFc07P0JbZXIlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d9c0f441.mp4?token=vtRVVx8daHKLNbJcL1jzvZvYJ5naLnuYu6DEdXNt8lN-uWqE0r0EYf1jHh8yPg9vJPNtQrgaM8PztmXE763OlgB48QMxDWfRHB8a3KVicod2V93AYyjpvXVXJTRwackBtqKJf8MBvtpFe6Ynlkdeztwc8n2htiJAQ2w0e7eKCE7dCTT8kkvnkQ2cXqlcxuwVYu3zrW3w5Fy8_SIRk6ZaHZdUTKsGgQbuske8NVmqmf_3ZVQI_mlg03bt7woOX5CFuPabFbuk4or29HcsDaSOGUneLkWFNuQaNRcSvf2xZB5O0WmZDat6zF1VA5n36Yrh8DVpy8ivpFc07P0JbZXIlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
استر اکسپوزیتو درباره آشنایی‌اش با کیلیان امباپه:
ما در مادرید با هم آشنا شدیم. حکیمی به من گفت که کیلیان خجالتیه و خودش نتونسته شماره‌ام رو بخواد، برای همین حکیمی شماره‌ام رو از طرف اون گرفت. چند روز بعد همدیگه رو دیدیم و بقیه‌اش تبدیل به تاریخ شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102373" target="_blank">📅 20:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102369">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OPA7wLvp2bq3XiurIHYyJDW07F_DGFe9eF9REhHfgJQztCqS2MUOFinTcMbUcZAPVtbZfbTwEFhKNkZn9eTZN2AX-BmIfcXuSwDUUbzo-GUsTP4azZQ9CS1gqCrxiaEGVTsD30iCB8T4T4hO_jdho15K4K-oRUYo0i6AIbR25FOE7if88so0jjc-mnY_EoA9Wv2mhQB7NEdd2fI0XHHm7ajV93UU_tEiCYQc8Cr_2uIGbDxIh0XXhqQ1csN53swsikP84omhg054FRbHTK5aeCxlDOT5i81uEtlT1ldrDqC8PCsoZk6CqXxoyheyAD0QqV9qTwsdYnAV6QrKS1lpQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WXVHVYNwpyk7fpz6qPIEVWZPR7dcFHmhuW1oJUsS77yxVhSKM_cEDeEoHZcRn5cmTwfku3qECnNFvjg7aDqYwi4UHAjc8LguZgbOiG7Jvk6i3NNPmBBisTPc9b4ejBsc1-ZeDvlQMbMVlwu4ZbRsJR74uOJQCGlkh7cJkpKJN7XAABjJZ--dQw7WYs2UpNgTmG_rHmCh3Q_m2H0pwzDvw3abLWm-YGSgU-NKfGZevSqP8p6CLBNd70PM66V7enJCm9awVZ3IZtqJ5Vak729ZIhA0UVBxoaq98aiAWroQXMWWl_fPVnIvA0Lw0lCjIhWTXtk5IMGciq2l5bNjR54XQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuZ_0REUKf83r5lpHWUycWEu6zLIZcNUhg8YiUYjAfPUe9uW45zhwiZdK0-oCjpSLNpaBCQTI1o_UeBuNxbnAg5NM38rEC5xzd_yBsmwvESbnJ8YRcmJKssu_XLrjsowGVlYzTIjwCHHkEnN-iLSFOKdp1KPfjZPCgqHqPCyaNPg1xfL_x98WMuWcPDzctx5kwtuDSqkplx3uWcYF8PH1Cl-262zn5LGKIAKBvkRyI9GA3HNvxd3kE3EqooMD_ZqCKzp_SQjL5VbN6yR5fbPnQgpoyrrV2wbJX5OR5_si4wzdWfCOiCBv3FWmBrur3_TPyx6YG28-KMvJNMySmmMoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJxGCebcsDEAYxo5K6inySUBchtxzF2rNwHD60VUMfcoTduaNyNLV1KHz8mChAZpC164cowps-jmHaNMpiIJqDLoVZkAoFm30WM9brBjCGyiKd5Y5-t-mU52qmtaCXumteis_kdwkZVnOeJqlQ97xZJ9XjD-90N5S719XIn28BvTZWjVEqr5V_mdNk_z2fsUHOnDjSEOGIph9CRkbAJQYmEg50vVTbhpVQcxJoHI6Bw4DS1__XabM_pS52cM4-cR8ePbFzsudUHeeoZq_wU-MPvtzjTEnS7EniRl5qxFmuwiD1HFxMpH-K7KTW16KgqVHI4nbnwPC_1UoZ2QkNn8sQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
چلسی در همین پنجره نقل‌وانتقالاتی حدود ۳۴۲ میلیون یورو هزینه کرده!
💰
💸
خریدهای آبی‌ها:
🔺
مورگان راجرز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
— ۱۳۸ میلیون یورو
🔺
مکسنس لاکروآ
🇫🇷
— ۶۰ میلیون یورو
🔺
مارکو پالسترا
🇮🇹
— ۵۷ میلیون یورو
🔺
ژئووانی کوئندا
🇵🇹
— ۵۰ میلیون یورو
🔺
امانوئل امه‌گا
🇳🇱
— ۲۵ میلیون یورو
🔺
آلوز دنر
🇧🇷
— ۱۰ میلیون یورو
🔺
دستان ساتپایف
🇰🇿
— ۲.۴ میلیون یورو
⏳
بزودی رسمی میشن:
🔺
والنتین بارکو
🇦🇷
🔺
جردن هندرسون
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔺
دنی ولبک
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102369" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102368">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b486c4e528.mp4?token=gvlmaKNTLkRBBqNqZPuDsGyA8qcN19O3_2Y43lbZt4hcOBsnZn7hpexLyCXTZ-yMUnRvvGrwC1kqHMu3QXBD9OXjtv2geIB40zCNDr5OYkJ_u4Of0pCN0Pg8ByyDGJQRm6GAr_QhByeRCVa5suaoEXtZaT2msc9R8ZR-GkXerGPPZwyTg6kHzKkwd6vZLltRW2RGG-z9uT75sELpPj4rtVYUlwCTridEz8Zb2CAD7w_vK43QOd5MKGWdH2zv2_A1TRt77MY1zCl5wKSiRpGi89y7aUjmzOr5A7UyX3yCph9b3HrV1i41uUYPWk0tpZTxcTttbA6-AxoXo6a-er-HgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b486c4e528.mp4?token=gvlmaKNTLkRBBqNqZPuDsGyA8qcN19O3_2Y43lbZt4hcOBsnZn7hpexLyCXTZ-yMUnRvvGrwC1kqHMu3QXBD9OXjtv2geIB40zCNDr5OYkJ_u4Of0pCN0Pg8ByyDGJQRm6GAr_QhByeRCVa5suaoEXtZaT2msc9R8ZR-GkXerGPPZwyTg6kHzKkwd6vZLltRW2RGG-z9uT75sELpPj4rtVYUlwCTridEz8Zb2CAD7w_vK43QOd5MKGWdH2zv2_A1TRt77MY1zCl5wKSiRpGi89y7aUjmzOr5A7UyX3yCph9b3HrV1i41uUYPWk0tpZTxcTttbA6-AxoXo6a-er-HgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🔴
🔵
تاجرنیا: «ما و تراکتور، بصره را به خاطر نزدیک بودن به مرز، به عنوان ورزشگاه میزبان انتخاب کرده‌ایم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102368" target="_blank">📅 19:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102366">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twbj8Qcno1G2h7myFH18lTgtNI49cgS0Kh3q4lpFYYYp-RwU2lLS2M_rwj8TjW018v1OQ6OOLNiTzM7zVD3N7GbZP4cnB_g7IL8vvv2MaG-yu_afN7PnclQOHP7EblP4NCDLBNgXIsk5C6wDBUIpDc2ZYnNqGUbBKmlL6LgoJ_3_RnMf387CQW4bI8nY2lbUAb7SfpLRrB17ZVD15WYrI6cAKpzotIs8lX_hiRlv-yfPejOM5ffaU593hktoZAT0H1LJjdN1-6lZd5Urrgq8SiKddsic1JbPPwP2Q6fDzu3hv6rCez9xybJ10BFZDpqb98A1J-j8J6IDmZ4G_S5wTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
✅
تیم‌فوتبال پرسپولیس در دومین بازی تدارکاتی در اردوی ترکیه مقابل آلانیا اسپور این کشور با تک‌گل علی‌علیپور به برتری دست‌یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102366" target="_blank">📅 19:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102364">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4TNSLgZLMJqFQfW6s5X0CHdq9e-MkeiCuTga013jUPdjz49rb2q42CgbuuLvIYEAX6n4Cm5p8jj8tOtD3l7jaT0rl-WBXXFN62GJKCJGCiyGGeOUkDGu_z0GWcK6N9Vzc8nw3MX2Q6Eo5ZT70Opom_nKj7Lspm_jha_hjO70hS1AU8u4ix5LeRvgtJR3wetlXrFP5bZ-D9TXqemx_SNp2GhNzWbQ_SsyjnNOaRmNAhGA7xsv2FJQGa_Ns_ctKufORQRYKOOpOvX9VloiLhepPCVVansIi6ERkfxas7WHlhfuIgaXECL13K2POf8HBw6t4TortjeMKjz6nm5g_2FBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08c0c36c9e.mp4?token=pALmXJsoFhQJm7nPNJXFinh1cmmLK2Me1yzTba-Bm9Cw7pJvOxcS7JaLVhwBFrWMJNK5STsIU06T9CySUdbuf9Md3hTj4MQvjz9wn3dOWx6lKv1F-YaC_uNjiV8BwGw2xmYhRZTsnX0353bcNgJ74rlgwEk6Ol_PJCEPc3x0r0IOaKCSVr8LCw0CY8GuLq0PYRfnBEJ4OsNezm96QpMFO-jKHOxHM2L30mAtqfqcEuveGtZnt7CEyRsJoElZP35m4Iy4uaN-cjtyY1SEtAqyDxFiW0c6yEz5oGI42GXFtbLTxqeo59dlxZ5H-SP4dKBFQLBoXJIS0SB1je2OIhEFPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08c0c36c9e.mp4?token=pALmXJsoFhQJm7nPNJXFinh1cmmLK2Me1yzTba-Bm9Cw7pJvOxcS7JaLVhwBFrWMJNK5STsIU06T9CySUdbuf9Md3hTj4MQvjz9wn3dOWx6lKv1F-YaC_uNjiV8BwGw2xmYhRZTsnX0353bcNgJ74rlgwEk6Ol_PJCEPc3x0r0IOaKCSVr8LCw0CY8GuLq0PYRfnBEJ4OsNezm96QpMFO-jKHOxHM2L30mAtqfqcEuveGtZnt7CEyRsJoElZP35m4Iy4uaN-cjtyY1SEtAqyDxFiW0c6yEz5oGI42GXFtbLTxqeo59dlxZ5H-SP4dKBFQLBoXJIS0SB1je2OIhEFPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اولیسه درحال لذت بردن از تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102364" target="_blank">📅 19:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102362">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gagme2H7hTgl3E2ggSxCwWH3RF4AVzY3okebM5ZOs4ZAhSjd8Ef5NPrMDeS4fQcIx-kISBe4VvWocjS-fF2b7DIEKSwmvgL94JaWxF-Udo6eS2q7dKdxdIVFahw8oqoEBqx2SXzp2302DfMWPztgp6J24kQSj_O3fmNE8JO9UyGPS_KnmnSLNGoUCbrspQJ2835WtQrdyh2owUtN6c2BIkda0-cJB6tQTwCyk1BJewqpVKnfkTl7fonE3yZ6LkWcfx0LO0JWY06pyTn9CcUll2go-BP71CA5mMVNgpvf-pN2pGbbOuMVQxDw0_1AcgISU4dIiULWP7nSIq9up-q1wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3645ae0183.mp4?token=OPiv-i5Y5NV-muenntYb31u-uAqE5tQ9RLKLg_pDPNWlioSQtnW3WXFkIVRFEVQV7GGYlPnabvsGB0gb4eNLAjxWXAKhDliokc-DmJJfafaYaD4dq47h_SkfGIKdC60Bs3XHwRBqbJCZSu6krH3IPYxOa53KBKq_-H8oAP4i9VHtg3KFIB4Xmcdz8hiqyGo8MTFGfjA9JBv8qeREmC2s2D1E0HW-wcCJEqta1yaPyS1PhhGqUtTO8LaT_WAz_4OK-tapJ_X9tUp9wqjWbJb56DHeeLu1QfEGO0KwBCN5rY579k17CDI6TmCcPXFdSXR8cU5ZQwRaDKN66bch6NDDMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3645ae0183.mp4?token=OPiv-i5Y5NV-muenntYb31u-uAqE5tQ9RLKLg_pDPNWlioSQtnW3WXFkIVRFEVQV7GGYlPnabvsGB0gb4eNLAjxWXAKhDliokc-DmJJfafaYaD4dq47h_SkfGIKdC60Bs3XHwRBqbJCZSu6krH3IPYxOa53KBKq_-H8oAP4i9VHtg3KFIB4Xmcdz8hiqyGo8MTFGfjA9JBv8qeREmC2s2D1E0HW-wcCJEqta1yaPyS1PhhGqUtTO8LaT_WAz_4OK-tapJ_X9tUp9wqjWbJb56DHeeLu1QfEGO0KwBCN5rY579k17CDI6TmCcPXFdSXR8cU5ZQwRaDKN66bch6NDDMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نیکی نیکول، رپر آرژانتینی و دوست‌دختر سابق لامین یامال، در مصاحبه‌ای مدعی شد که رابطه‌اش با ستاره بارسلونا فقط برای بیشتر دیده شدن بوده:
راستش باید اینو اعتراف کنم. مهم نیست وایرال بشه یا با واکنش منفی روبه‌رو بشم؛ من سال گذشته فقط با لامین وارد رابطه شدم چون می‌خواستم اسمم بیشتر دیده بشه و به کار موسیقی‌ام کمک کنه. با این حال برای اون خوشحالم و امیدوارم اینس مثل من ازش استفاده نکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102362" target="_blank">📅 19:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102360">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iWKcWuTK7gWQg_xOJLdDYZQ9ePXK47f8y9F3gqy_whm4qzatqYY-cR9aFo_tiWaIGHkfpDBeZ3oYskv-Bsq-V-b63iqMBEXApPpiuFwir5M1YszA-wYi9EULBg7FtrbTUtdyspPIJoji949JQMSbq1IjhDmXw3kQLKfGcu0CPg0yBv4XorVeqAwrcDaVyb8JAvj0_TKIYRNBC5Zcwo_4_aAwHHoGsyHP9qY6i8PamqnJTfSreWs_Bjeyg59eWr1cywWJYpRkPAPQFyvgdfvh2uY-SoLVgm_HrP5akddf06ZmbWVcCSUSvsmL2VyQDD40BQg12S1BbSkD6rojnIkrgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K3n08NyWoM-OVm-GyY6GXceUM5Yo5FY1piUTo7msMytnw_Gr-Ex4OsoDLsF1S0LZBs50QtfEfqScBnH9LZ7zg_C5DSsUYbdM0cU6Ok0DTAujJs2s8cMYSBfOi2FSLxY0z34PFrwbMvvuJe2xaaDfavH-0sq8_Wgm3xs7T1EAc6pB9o6tkwYjyBfp8GBNBybyZ3eyDvazyvF5BwBiYG4XTY1orDz4o1ATNrDHFYFObr2Rf5A6yn7HMRSyCq_B093vHX2t-0a6IxalW4CILMAUQ_sDBhBOueC_FCsik9lhJ8A2vqqeyD5CG3s3vzuMtwoXcizlLjU-Vm-T_n6onFpA3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇦🇷
طبق گزارش‌ها، لیساندرو مارتینز و الکسیس مک‌آلیستر بعد از پیروزی آرژانتین مقابل انگلیس در جام جهانی، برای خانه‌هایشان در انگلیس نیروی امنیتی خصوصی گرفتن. گفته میشه بعد از حواشی جشن پیروزی و نمایش یک بنر جنجالی درباره جزایر فالکلند، به خاطر بالا بودن احساسات و احتمال واکنش هواداران انگلیسی، برای چند روز مراقبت امنیتی در نظر گرفتند. البته گزارشی از حمله یا خرابکاری علیه خانه‌های آنها منتشر نشده و این فقط یک اقدام احتیاطی بوده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102360" target="_blank">📅 18:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102358">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vKTud26CyurWyRg1m8lG_FSF39lHb_qAcLPVSLiqKfLZx-M42Fk9RO9nSxuWs9YahThUVPZSEGpErgpXQLWRq-vA6p5HQ6EW3k6LUs3TnznklzOx_ikwiISKA7BIJN9sfH2aESjfW16ps0WA9tKbok--Vnu6aWdbv8HgYw0xbWv5g0Kr33fWPeow6gJwhXQbmw8yi_0LO1VB51CxMslHBpa2hE27y4qI2RPcBrCk4cJmXti08sPI8ECBJDeAqJns6C3SKMSXUMO2XopuwZ1BG7Yt9zfzMA0V2ZKm5r4NCjHDbfcbZB-j3ngPDTDQf7sowEldPWGV_oK3wcZuMvyZJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q96ayThaZcs2oplrU4z91ioqfNkJfDZDobXaaXm1drYIISqwcGflzsC46SPaRLO42cLhTfnVhnBmPUap-0j0pGnWLJVpx8ZB51RYrprrxreD8kKe6oIJgHZf_KEO64yjOhAqf4l-ah66oeC_96icXeDqxX2o631e-eJLAS5kVyhUSsn-UX0V_FCogq6pepByDGNz27R34WWknEA9nuGAMpfZOSe1cE-BF_mHnehpb6E8C8OkPvzTYVmwK8NxL4ypvgPJCmYBfe9PnjjuMhPulkypM4TSaEfoDtNUM4T97-0P9n1Wx3Cmn2LaB79G0cL_eZ3j2NMgHiKgEj2FbR9TnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
نیکو ویلیامز و دوست‌دخترش آینهی گارسیا جدایی‌شون رو اعلام کردن. طبق ادعاهای منتشرشده، گفته میشه آینهی نیکو رو در ایبیزا و روی یک قایق در حالی دیده که مست بوده و کنار سه دختر دیگه حضور داشته. بعد از این اتفاق هم وسایلش رو جمع کرده و جزیره رو ترک کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102358" target="_blank">📅 18:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102357">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e33cfddb.mp4?token=Smvy5vB1v7uWOzyrlPWNOEt5AGKT5MAyIkkLby-XCsS-P8Gz_kFULeIl4niV8TmUtwTO9uDk0IImBbawNChbF0igBx3Lp2W2exwyJx3WrZgdzOFw6yG3xd6wdqCFdgafACEFUf8yuf9eExdYkVTRNs0mCOHH0-HZHVzBOkWwRZJpZXuVw7YGtmsXxecc89R3u3yi4ztRk_7Ip_-3svqRIqAZkYRIF64p8Yl4I4WRgQuPPqWFcBarybkYuPxaXOwOdEJOVEOsh9efWG5XerYLgL0OamgpedhgH6NzlIm4U-a9Au-tRgLvRKvCM97ZEdDsLhNR1zZ3vMnmdnjXOkRWSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e33cfddb.mp4?token=Smvy5vB1v7uWOzyrlPWNOEt5AGKT5MAyIkkLby-XCsS-P8Gz_kFULeIl4niV8TmUtwTO9uDk0IImBbawNChbF0igBx3Lp2W2exwyJx3WrZgdzOFw6yG3xd6wdqCFdgafACEFUf8yuf9eExdYkVTRNs0mCOHH0-HZHVzBOkWwRZJpZXuVw7YGtmsXxecc89R3u3yi4ztRk_7Ip_-3svqRIqAZkYRIF64p8Yl4I4WRgQuPPqWFcBarybkYuPxaXOwOdEJOVEOsh9efWG5XerYLgL0OamgpedhgH6NzlIm4U-a9Au-tRgLvRKvCM97ZEdDsLhNR1zZ3vMnmdnjXOkRWSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی ترامپ‌نادان با بازیکن غول‌پیگر فوتبال آمریکایی؛ بعدش که مزه میریزه از اتاقش بیرونشون میکنه
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102357" target="_blank">📅 18:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102356">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5a8032cf.mp4?token=V4wZm7Uy_AVuE8X1FcED46K3YtCiQJA9mxx1RLwa9VSDOoOHRd5S3LcAZQWZPiQDZENjor9Pz7mF-_b5BeaX3wlqBRPAi2j88ZuWyCgsgfqyOpNim3HiA0G9X3_udsJl1jVld-2CYRZ4hNZGMjLHDgiJ4DlIolNswokxH_Mnw2nmtM4lwR20MTJXG7QIgOyw8v57s31zJO1sy396kC3aQbnlkbXPPucqPHPisW06D3z7dPcF2Z35UjqE8XqMqCBWXBwZ5zhsmXeqf9_uUqC4ZLqkvwaeHOrh3PqB1azGs6CtpZIjAfMwaB7MzmdzUfII4zPJNbkQqu18M3zsMO_wMXXpjwoC6eOu1eSIXbNi36Vm2zLIBUX4wRSBcEo8IyXyf5bS3PSTKI3gtnw60_M9wCPxzTLF7ij7uIEw-tWtq4tUrALheRn1X_16Ow-0FFH6ftbCIi-xMG51XZKXZ5XXWs-FcSjgnHzvYc-GUoypnpATCqHhzQbZ2ohc3So08id--M8ZcpGSaQNCE9Zfd2lsgzIzDojF5SCOH9rPZGOmYft_daJUuQ-saW9HKEl5WwDOx453Mf0yqRH4ubq7BxoPfw5G4KeMrVXKsfQJf0j4QFBAPsumU32w8mT_-0Xs7O2H2lzfQCTsdz9DAs_7pQDhxEZg3CK_gjQjE0GAUr8DUec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5a8032cf.mp4?token=V4wZm7Uy_AVuE8X1FcED46K3YtCiQJA9mxx1RLwa9VSDOoOHRd5S3LcAZQWZPiQDZENjor9Pz7mF-_b5BeaX3wlqBRPAi2j88ZuWyCgsgfqyOpNim3HiA0G9X3_udsJl1jVld-2CYRZ4hNZGMjLHDgiJ4DlIolNswokxH_Mnw2nmtM4lwR20MTJXG7QIgOyw8v57s31zJO1sy396kC3aQbnlkbXPPucqPHPisW06D3z7dPcF2Z35UjqE8XqMqCBWXBwZ5zhsmXeqf9_uUqC4ZLqkvwaeHOrh3PqB1azGs6CtpZIjAfMwaB7MzmdzUfII4zPJNbkQqu18M3zsMO_wMXXpjwoC6eOu1eSIXbNi36Vm2zLIBUX4wRSBcEo8IyXyf5bS3PSTKI3gtnw60_M9wCPxzTLF7ij7uIEw-tWtq4tUrALheRn1X_16Ow-0FFH6ftbCIi-xMG51XZKXZ5XXWs-FcSjgnHzvYc-GUoypnpATCqHhzQbZ2ohc3So08id--M8ZcpGSaQNCE9Zfd2lsgzIzDojF5SCOH9rPZGOmYft_daJUuQ-saW9HKEl5WwDOx453Mf0yqRH4ubq7BxoPfw5G4KeMrVXKsfQJf0j4QFBAPsumU32w8mT_-0Xs7O2H2lzfQCTsdz9DAs_7pQDhxEZg3CK_gjQjE0GAUr8DUec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
یادی‌کنیم از کینگ‌کمالی از اساطیر بدنسازی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102356" target="_blank">📅 17:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102355">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a15854e8.mp4?token=LbItQK7bb4HW9rw31vp-Fo_4h_YlPPCYE2UUXUTVNLH2WAIH-5e1s1GlwTRNnIkZF-3lOe6horXImT4I_MGNyk-qHLG6i1n-skJeyLzPaZLcYkEn1_2YbodRBQB-zp5stc6WcLoSUkA3yZt98CM9FqbR4tI1zJlvX7AUZvNjW2e0IDfd5W_g5c3GznPF8FsH2K8XcnoaK0YtFx28fP3HLD5eRueNLcovI5VVrLYUiFz6tm-_PTSBYIXMXcR-E01F_S0HvHTOKM3CDPGe6R89lORZGluAG9TFG_y03ssd2r4gXjfu5xXxKll3JyvmBRqWF9Apcp_8JlF7U5cJqeVW9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a15854e8.mp4?token=LbItQK7bb4HW9rw31vp-Fo_4h_YlPPCYE2UUXUTVNLH2WAIH-5e1s1GlwTRNnIkZF-3lOe6horXImT4I_MGNyk-qHLG6i1n-skJeyLzPaZLcYkEn1_2YbodRBQB-zp5stc6WcLoSUkA3yZt98CM9FqbR4tI1zJlvX7AUZvNjW2e0IDfd5W_g5c3GznPF8FsH2K8XcnoaK0YtFx28fP3HLD5eRueNLcovI5VVrLYUiFz6tm-_PTSBYIXMXcR-E01F_S0HvHTOKM3CDPGe6R89lORZGluAG9TFG_y03ssd2r4gXjfu5xXxKll3JyvmBRqWF9Apcp_8JlF7U5cJqeVW9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
وضعیت این‌روزهای هانسی‌فلیک در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102355" target="_blank">📅 17:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102354">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=XqJ5MHlLIJnsE1WnTPxoebGm5jE-sNj4Mo14LueE1tuwwNUuDawpQz_pv_2clBNVo0v-27AYED4p5g2MSH1gNPRQAK3Nkye__iZj9OmSex2YX24l-4aSzK7eZgCAwdWQiT5W3MvqIkBntKZVYyh9DZsXF4zkMbnZmq5YA42fDwlO09mUr1lpNyMKg0Y5FYdnyV0A3NK8FR2wWO9mgEfGsW_IqeoyOoZHUBZQ6Z4kETiPt4Bmdc8rv3Ceq1xk12YfjKML-0onGtzmI9fsgozs72bQc0cENNYv4KXm95gx40M5eP72-5t2Ctad7nT3YObJ_h2LmFCt44h1sFUMJc5EJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=XqJ5MHlLIJnsE1WnTPxoebGm5jE-sNj4Mo14LueE1tuwwNUuDawpQz_pv_2clBNVo0v-27AYED4p5g2MSH1gNPRQAK3Nkye__iZj9OmSex2YX24l-4aSzK7eZgCAwdWQiT5W3MvqIkBntKZVYyh9DZsXF4zkMbnZmq5YA42fDwlO09mUr1lpNyMKg0Y5FYdnyV0A3NK8FR2wWO9mgEfGsW_IqeoyOoZHUBZQ6Z4kETiPt4Bmdc8rv3Ceq1xk12YfjKML-0onGtzmI9fsgozs72bQc0cENNYv4KXm95gx40M5eP72-5t2Ctad7nT3YObJ_h2LmFCt44h1sFUMJc5EJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
‌‌ ‌ ‌ یه ویدیوی وحشتناک ۱۰ دقیقه‌ای از
این حرومزاده منتشر شده
🔗
🔞
مشاهده ویدیوی کامل</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102354" target="_blank">📅 17:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102353">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMWBGPiLiLn0q0m0KPRVORJPqu-rI3XpePYt23SnTuSTx1f-7f-ky7Cpuyw_bpzj-RA2t5nyYzC9GUl8SPsiFppSNWq33bwnzmVDtBOvJT2pccFCfbJd7ZxfjeGfb6e1HiXjaQlzw8gDCXKLfN9dIEX77NBIRIBzIdvNSPu2ZYGOp7GOqmU6r9j_Cube1Xc1Dlxmk6p3aWpryID86xpWeiRAREg6dyN0K3NqW1oU0IVhrBQGXggtAqFk_fbe4OocXtRWTETUBhrlVx57IFBHpxIvnVAIGy-fy7-eR3sKGE8RV3kVFAWqPvJsvgr9blctzmqyWzL54gFRSKBrN6SAoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🗞
رئال مادرید، پیشنهاد رسمی ۵۱ میلیون پوند برای جذب رودری از منچسترسیتی ارائه کرده است.
❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی قصد فروش او را ندارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102353" target="_blank">📅 16:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102352">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f25fd06c.mp4?token=kVjvZDGcRRIio7PcrUPFsaJDi4UpxJm2Fr68eI3j3KYWcZaB70R0143OdOsS5aSXXsjGr2tbbiLUgaERDvcTI5TT0v4TdNTe9NfD-hnoiyitIu8O4Ln5RPO16uGnxKsVwIOFzimLWLy3XwB_VRfgHcmEZ0wkzow4J_gjhHOGS7jwGG4m4mPdPcARMLMwiamTESzXwZYVLpM4P-HrHWPrBTYNQSsNEO3uK1s_80-gU8zsJIpv-kaU6KsEn57KPTCOruLzgSghiERvvLGPCtphQnU1WCH0DGlYCVSzdv2650zFGymd45VM0_d2oJF4K2wcL8wRIowyNsYBFGaeEQ_3YJhKCJzMe60T26Zxdc4E9d8sEB98rXUN08D_q4dcZf3e9kcLizN3YrIfC4oxVh4l641qf-kZ7Laghmf2_EdkGrp6ccPXKy19aBBcv7VmegWVhOpDwmJDsWATPNWpSYNflcRN3B01UOwGFRWGBRglb952KLa26l4By4CSjo4Hdb9w5Y9CGxyyL4IB82KIGe03PWzDv9iS9meWegj175Qp1CFAVukql_j5XJNXWUVHi3rN1HnUOjc04m1GFD52tsxJeDtus9LbGLTiQLmk_ojOvYxb1hTmTKQd6xb8lIbBjG9NQcAhmsnsQvWCOlshEtPqbwnoqgCF3su0qNbpD_gQzCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f25fd06c.mp4?token=kVjvZDGcRRIio7PcrUPFsaJDi4UpxJm2Fr68eI3j3KYWcZaB70R0143OdOsS5aSXXsjGr2tbbiLUgaERDvcTI5TT0v4TdNTe9NfD-hnoiyitIu8O4Ln5RPO16uGnxKsVwIOFzimLWLy3XwB_VRfgHcmEZ0wkzow4J_gjhHOGS7jwGG4m4mPdPcARMLMwiamTESzXwZYVLpM4P-HrHWPrBTYNQSsNEO3uK1s_80-gU8zsJIpv-kaU6KsEn57KPTCOruLzgSghiERvvLGPCtphQnU1WCH0DGlYCVSzdv2650zFGymd45VM0_d2oJF4K2wcL8wRIowyNsYBFGaeEQ_3YJhKCJzMe60T26Zxdc4E9d8sEB98rXUN08D_q4dcZf3e9kcLizN3YrIfC4oxVh4l641qf-kZ7Laghmf2_EdkGrp6ccPXKy19aBBcv7VmegWVhOpDwmJDsWATPNWpSYNflcRN3B01UOwGFRWGBRglb952KLa26l4By4CSjo4Hdb9w5Y9CGxyyL4IB82KIGe03PWzDv9iS9meWegj175Qp1CFAVukql_j5XJNXWUVHi3rN1HnUOjc04m1GFD52tsxJeDtus9LbGLTiQLmk_ojOvYxb1hTmTKQd6xb8lIbBjG9NQcAhmsnsQvWCOlshEtPqbwnoqgCF3su0qNbpD_gQzCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مملکت به شدت عجیب و غریبی داریم
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102352" target="_blank">📅 16:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102351">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/138f735fee.mp4?token=AuE8VN38dXkIZLGpsQkjuEh9KU0dy34kN3LNFBV3EnNaKLgMxTu5YrHwLC0WJGLKNweBdAe4-ijcHAk_TEHSRPk9W8b2AcjZZPTIt4oGcvwKDy93HTDAnroD3Opz_gC5gCul6vdwixYyPsIWit3fbY0YTmVrCd---kTdkn64mc0EWFQpPCYsQE13yMHWwuPoAqwWetJUAOMYKEnzY57_brynIdKC6lWsET0Cz8_UD-0fI2Q6xQBiEn5x-oXjGx0Pv_50MeEGFFD6Y1Xke8ePbD_9x6d0nmKIpUyGLZi-mkubCsn_Hq4ClvNAKeMu6SnEBTvspaJqz0E_UP3t9nMNfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/138f735fee.mp4?token=AuE8VN38dXkIZLGpsQkjuEh9KU0dy34kN3LNFBV3EnNaKLgMxTu5YrHwLC0WJGLKNweBdAe4-ijcHAk_TEHSRPk9W8b2AcjZZPTIt4oGcvwKDy93HTDAnroD3Opz_gC5gCul6vdwixYyPsIWit3fbY0YTmVrCd---kTdkn64mc0EWFQpPCYsQE13yMHWwuPoAqwWetJUAOMYKEnzY57_brynIdKC6lWsET0Cz8_UD-0fI2Q6xQBiEn5x-oXjGx0Pv_50MeEGFFD6Y1Xke8ePbD_9x6d0nmKIpUyGLZi-mkubCsn_Hq4ClvNAKeMu6SnEBTvspaJqz0E_UP3t9nMNfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
برترین‌های تاریخ از زبان رودری ستاره اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102351" target="_blank">📅 16:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102350">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇪🇺
🇪🇸
یادی‌کنیم از آخرین قهرمانی بارسلونا در اروپا با مثلث تاریخی کاتالان‌ها در خط‌حمله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102350" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102349">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6gxUuFcEP5pKFnTELjXXXv8RQPgVcYfdnZg-HABU-GotDZGqptvBA8eVbNeSIe7saAjwT38IOESG4vKpKRGrBFFYwWHdFak2ELB_S3mDGmKtC_ObSld3iyPb_OLEsM3ouqSaLqKySqIVkMhdh1SJY0FA_rTWDOULonjWszF7G7isRNCIpPBDrB9nRm9i_BoEvFDnu7yGjIKtfuF4hjaKhlk-uzEUGvXPA8R9OgO3Jtfpwxx1dcHux6diiKgeEmBGOIdZ2cw7TtzIkTnP37LsYUDL4PtgVWGIf8tmtlzoKTP1QKRZhVwPU_79455LPt6wPU82_DFe78SKvxyh-GLhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گونزالو گارسیا به فولام پیوست
۴۰ میلیون یورو
۲ میلیون بند پاداشی
۳۰٪ از فروش بعدی به رئال مادرید میرسد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102349" target="_blank">📅 15:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102348">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d88e7b9804.mp4?token=lRdpGmBX7zh1bZV37WISPSYw42ihrLxkvUF34ZGdr2SN3NCcoMbe2nJHZZgb0Ce6LwDVRv2u_j3OcAA44k7nC6xp2Ck0vQdNWJxAXjbN7j7onnRNVFWl3kDtG1q344DK1DhYbqKVpkLHqSFkkvriMmNJDzgfYvZb1KCS01Ja_X88wiqx3wjVuPergGzNv00Db2U4DJfxw-JYt6M09dCqAMhWCs2da5eknaUzK63XqdkPhEKsKnOpHYchH2b42jY_jG0pJTGxj-11MOu8QZS73BCn10NEgmHry0dfD1tpvEFLTSyGkMAaBDcbh1Uueah4n4HxUbUBtG-qGULyz9JMoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d88e7b9804.mp4?token=lRdpGmBX7zh1bZV37WISPSYw42ihrLxkvUF34ZGdr2SN3NCcoMbe2nJHZZgb0Ce6LwDVRv2u_j3OcAA44k7nC6xp2Ck0vQdNWJxAXjbN7j7onnRNVFWl3kDtG1q344DK1DhYbqKVpkLHqSFkkvriMmNJDzgfYvZb1KCS01Ja_X88wiqx3wjVuPergGzNv00Db2U4DJfxw-JYt6M09dCqAMhWCs2da5eknaUzK63XqdkPhEKsKnOpHYchH2b42jY_jG0pJTGxj-11MOu8QZS73BCn10NEgmHry0dfD1tpvEFLTSyGkMAaBDcbh1Uueah4n4HxUbUBtG-qGULyz9JMoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
💥
حالا که بحث تیم‌ملی داغ شده، این تیم‌ملی و بازیکنانش بنظر از همه سر تر بودن :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102348" target="_blank">📅 15:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102347">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0063915b2d.mp4?token=ZV_b05kLlvdtBGJZmPMfAuiabWT2Ba18wdCZ4dU5nmOcfYa2MR_IuROws8yME9PaRl7D4iiFxrK0HSCwbCkCQtFV1CQdXo7t6LzO9KKMrfIInwGr-2uaYUH98jV3_Pb86uQe9v5c14BhJ4rrWya4SZQEXOV1AP386NGKFtsVEHCllANcZMuDKnwqgNGZ6Ya9ul8wEp1At2S7Pwrr7KV8B8LPaktpQ1YaG8iuYfyfp7P28xxNViEY_P6LAUZ_67lO37mwIbBQQJgDgzDR2C2FdtsLlF76jDa9tJrlcCkeGGU51rRUM6CE3Om5y3koKRA9CVwBdQkxvJ2Sib7gUxYVRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0063915b2d.mp4?token=ZV_b05kLlvdtBGJZmPMfAuiabWT2Ba18wdCZ4dU5nmOcfYa2MR_IuROws8yME9PaRl7D4iiFxrK0HSCwbCkCQtFV1CQdXo7t6LzO9KKMrfIInwGr-2uaYUH98jV3_Pb86uQe9v5c14BhJ4rrWya4SZQEXOV1AP386NGKFtsVEHCllANcZMuDKnwqgNGZ6Ya9ul8wEp1At2S7Pwrr7KV8B8LPaktpQ1YaG8iuYfyfp7P28xxNViEY_P6LAUZ_67lO37mwIbBQQJgDgzDR2C2FdtsLlF76jDa9tJrlcCkeGGU51rRUM6CE3Om5y3koKRA9CVwBdQkxvJ2Sib7gUxYVRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره‌بامزه از زبان فیروز کریمی
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102347" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102346">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2314f18179.mp4?token=UDICOke8g3xL_4I5h7TssCkW1BRGbaITAS9qOFK7B_cEZsEFK79AxW4er-wvVHa18ZrsOgSYb-fUkIguzkCNHYkClqwLECM8EyKFamz3FtTb5kw8PcHZ6HCGUufGIgs3gYV5NIqyn6GqhKaD9sudtU4RnLzp_k4IgGIWZMDcTPHZEG3xNPbGvpelgu27kO6S_drIuj5wXHlvZ3myBRdY32RMH49D8bItKKOuSnrZSMUaBEVRJYNEz5wrVJnc0vxnnKwUlxRX0LSwCnBCwvvW4CsuaPLTm0-CsGcEVzodL6FMXmvSCF6q51Tyi2kIGtqqMPh9kf8NsLUgB4d3dGwZHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2314f18179.mp4?token=UDICOke8g3xL_4I5h7TssCkW1BRGbaITAS9qOFK7B_cEZsEFK79AxW4er-wvVHa18ZrsOgSYb-fUkIguzkCNHYkClqwLECM8EyKFamz3FtTb5kw8PcHZ6HCGUufGIgs3gYV5NIqyn6GqhKaD9sudtU4RnLzp_k4IgGIWZMDcTPHZEG3xNPbGvpelgu27kO6S_drIuj5wXHlvZ3myBRdY32RMH49D8bItKKOuSnrZSMUaBEVRJYNEz5wrVJnc0vxnnKwUlxRX0LSwCnBCwvvW4CsuaPLTm0-CsGcEVzodL6FMXmvSCF6q51Tyi2kIGtqqMPh9kf8NsLUgB4d3dGwZHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
تمرینات پیش‌فصل بادیگارد لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102346" target="_blank">📅 15:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102345">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇪🇸
🔥
۵ گل زیبا در تاریخ باشگاه بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102345" target="_blank">📅 14:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102344">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e80cceff6.mp4?token=KBvy4T4iPkApObtGei6reEhX8J-P0KarruRIWA2-kv7xwCXWnF1GjDu4_B6gt9X9FyQ9uMccyEWPYdVrDLBeRNZYZe9p8t2LmqXGZRZMTzTbi9l3g3HG8uJDjdQDrtrOcOA272_ccAWD-DGU9eAHcQOORsvw8Aq3tGLLc3ydl2mw-3dk_MzKnAkcy1mpnyGHidC_MfhIqnSnPcTO2KT6gdxC99NWFkBh79jF1A3PxAqxQTZFk-Cjv_BzdLobVohOnPXYcOtbSNYSCB-7NEa7P3QaKkcX2-QHTOjeU4G2x4l-9IfoeldxURi1_2joOQimcZfCro8AYanXp9-aw5dhCYxYCwe4L0ap6hedZ5zHEObwGSg9MblpXLFFN6DG68mNnWdIfec1s0jTc3D8O74U4-Spt0N0smxvZGDlJreS1dJZWepmY38EOGjeXJF1YeSf4vm1JOqDoIEGfCVuroW7FucsyfCzRuMQPjF2372-0GgMghyCPRI8X4PIjf9c29RoevhShpAnlt1-DF1G50dOEawM1f0iU6-GAwBi2MD4Y9wMq5O-vIgZcurFckI9_ngBvb8Gdn2ADZLfIAzleP7kzD3rskvwYLXtoittqbn3BjD_ZYO9V7jOtaydNKOqEgAXQqQ5HAZO5YSWeEkxyI8NS2WhuPXqQLdTLpgdgs1nJ-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e80cceff6.mp4?token=KBvy4T4iPkApObtGei6reEhX8J-P0KarruRIWA2-kv7xwCXWnF1GjDu4_B6gt9X9FyQ9uMccyEWPYdVrDLBeRNZYZe9p8t2LmqXGZRZMTzTbi9l3g3HG8uJDjdQDrtrOcOA272_ccAWD-DGU9eAHcQOORsvw8Aq3tGLLc3ydl2mw-3dk_MzKnAkcy1mpnyGHidC_MfhIqnSnPcTO2KT6gdxC99NWFkBh79jF1A3PxAqxQTZFk-Cjv_BzdLobVohOnPXYcOtbSNYSCB-7NEa7P3QaKkcX2-QHTOjeU4G2x4l-9IfoeldxURi1_2joOQimcZfCro8AYanXp9-aw5dhCYxYCwe4L0ap6hedZ5zHEObwGSg9MblpXLFFN6DG68mNnWdIfec1s0jTc3D8O74U4-Spt0N0smxvZGDlJreS1dJZWepmY38EOGjeXJF1YeSf4vm1JOqDoIEGfCVuroW7FucsyfCzRuMQPjF2372-0GgMghyCPRI8X4PIjf9c29RoevhShpAnlt1-DF1G50dOEawM1f0iU6-GAwBi2MD4Y9wMq5O-vIgZcurFckI9_ngBvb8Gdn2ADZLfIAzleP7kzD3rskvwYLXtoittqbn3BjD_ZYO9V7jOtaydNKOqEgAXQqQ5HAZO5YSWeEkxyI8NS2WhuPXqQLdTLpgdgs1nJ-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فرشاد محمدی‌مرام درتست گزارشگری سال ۱۳۹۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102344" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102343">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfucp_lCFrROBITEL5Slvs3WK1gNlpKm0KHvsRQgaAW8lMevrLmgsUtar6Lrkb5-2a9uIDYD5Ccfbg92h466HBw-Ak-2XdRab9h6Se8tBX-BlL4qiE9OKAEUxtkfkmJBeE_cNZ_ITNmPtq_z5ekPN5FD4wkMGk1nFEJKt6gRbvWOlWVelziWEDdPoms4IkY0fr1wnA5EIH-MkU40ZA3_m4rBXjPKlzY0Si2wwLRqpMZqJQd0g2xZhLMxXwgmOasSgOG_5NkWcNoe6yIuB97901n4mlBDgEoIBixEckvxN1kclZU2H-NOE29vSduA24s0GYG4Ac53RKoYlTpfyjWyeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔹
رسمی؛ نیو راموس مصدوم شد و حدودا یه ماه و نیم از میادین دوره‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102343" target="_blank">📅 14:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102342">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3336c43202.mp4?token=pVoU76YqH5XZpiFzl9RHa7J3lIX8sg3G3QDlNz3d3JIj4hfTASyPfBIbyg9sQ3oLC85mz3YFn5QTm-GwAKn7b4dERRZAxWm5PLK8TxbNT-7BGU3YytqeORrYuK6zbPEVEnbJmZnnqNvJuMPx_eUXc6Jwp7BWtVnaCo9QK1nIw9qGI3oviu0igEK-52szpiay0NEQABvGc8QgyQlcl6QqR4VHVIjHXlk0T3AHScS5K2Nyw-RWoCYrKwVnYocZRgqSAwHMawmxlsBrbwbD_1eI3smD3g_YgnLv-2KZHI-VL_fAh63j3m5gvpvE8mHCX9_tyhP2PJbweRDh17AkRgRT9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3336c43202.mp4?token=pVoU76YqH5XZpiFzl9RHa7J3lIX8sg3G3QDlNz3d3JIj4hfTASyPfBIbyg9sQ3oLC85mz3YFn5QTm-GwAKn7b4dERRZAxWm5PLK8TxbNT-7BGU3YytqeORrYuK6zbPEVEnbJmZnnqNvJuMPx_eUXc6Jwp7BWtVnaCo9QK1nIw9qGI3oviu0igEK-52szpiay0NEQABvGc8QgyQlcl6QqR4VHVIjHXlk0T3AHScS5K2Nyw-RWoCYrKwVnYocZRgqSAwHMawmxlsBrbwbD_1eI3smD3g_YgnLv-2KZHI-VL_fAh63j3m5gvpvE8mHCX9_tyhP2PJbweRDh17AkRgRT9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
رتبه بندی سوپر گل های فرناندو تورس ستاره سابق باشگاه لیورپول و تیم ملی اسپانیا، توسط خودش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102342" target="_blank">📅 14:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102341">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6cUX7pz7dGz10k-pLeOjF6sqqwY7KVMx68LixqHlsqhYkBbuJ5ymaFrxoCJhSUX8G1QICbJgxPgxdIDrhXGOupEuzdZZ9biV3QqTw8_DvE-PDHpfp12VRH2_pPTJMeJs21v52sE9bUr4qI8eAJGSrzgsdTHWLImFUyfcb1AueFk_36j9CiNGuHrm0rgU86rww9VH10kTP2DpFV7UMsPhRm-GOtQAe24GQCLzvACFBRlVFsZFuC39Nhiy8aT7TAYXY2xUpSQprg73teFhQpZucwD1ib4PHQ1nXjexxLbxyKAmlCsKWo8HaDGjEhn99RD1wnEAsgdDg_AsH4NAW55gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از کوپه: رئال‌مادرید و فولام بر سر انتقال گونزالو گارسیا به مبلغ ۷۰ میلیون یورو به توافق نهایی دست‌یافتند تا این بازیکن شاگرد آربلوآ شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102341" target="_blank">📅 13:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102336">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W1cU3P5xAjRm_lRC9TjCxU4zXdLlFsYMNPf-2PmZFXH7aD7vKV5v65GJ-I2mUQdtk-QTu6CVWXSNGs_nDB8sRm743rjVhiluI4V8AbPVwZFGl78rnf_A3mIFU1f2uX5XYL0rwcsRYuWetxSlEPOVDIpPFvd2uSO1paj_AtHoWxAg-MrS_aCCQejtCzsMz7AW4yH88oHM8ledXloLPT4zbBk4XO52urRP1wPNFyPTbgnVZSW2VHP8BN2L-4TtIirI1JqS_j93x0jQY6OeJbaZdJB56NyG9k6f9HfbaP089FVwYgYwHayXak4U0bKPJHvJyb_JlMl_2r3iKFnycohZ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cdnfUplsYcKXfDazRlnaNhGk-gw9xYPwVuz-TVE8zSg49BTWf9svTCCBfMTr2vKDVVcHElQlCdsEulw_Vu_C-N8AhchVrbrzMj6EbS73Z556WpubVI4tfS2QeXt-04livJ_LCJIfqnfy5yssRyXqMrZ_SPfGZn3Rib9nRCceYt9vuQTjRMNeOC2b4OVgY9c-YHNMd22KbE-PHsPKOYsroVAlCmR-o1TC0rbrDIOcc-yCVngeosiSblaAw6Uml6QVbBOYxql76sVQWlVcNjx6YLiQqhNWfDMxhr5RCqL-kfxGV_m256LmhSHWhnHeCHuZH20C0z60sE9nahP_h9_5zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ep1UebPVUbqszU1nFBUtA0JFoysVorSqLKDT54KvdSxijl6sOUNR7NEuzHc6PtXGuW-XH8GXsWU3oA4p4fFz6xPfdlqWyoyzIiskIdBq659lFBVdx4Vo_0D3KDzirl1tYLX1aWcM_jB0rkuo4pqorX11RDG54GKHiqwUvRkcjZLoPLlq0kGeOhj8pIkL6VfVa0HtZ1ZzpNE96IPfSBf3yz14KnkhBgMxtBng5Yi0yRdRHH7JexXI4rHydJ0uBM54UGQom53Lj7wMIj0JJy-UXGKfo_ggFLzX0pR-0AqijWc9-SDmoYJXFt4QFd9l4Ss3C8FaudroipjE0h0UmLdGtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a8ZNGzvfSKaYGlSTWSk_ePIlYkdfSdD_5axKbo_DeMSxgID5rjxUJKO3l7OS0vP1NowntA3p5hg7TKPFBkH_lFjgJo4FiosqqBUqIWZ17v-cUmAdFDAycaSdQkm0yi7BqFhoGaiF85kUhRHYAouaYTUvDFujmyo8Qv0vNJpFCyWg5D4pJs1r46fJ1a1khQMpx6B5DNwf_SnCk3Y_bQIiRVAzkUxNHhX8t6548s-avktUKN48AyTxoVYMEbRfXvwrhEBkpt_l5Xo8cO7gKF226InXRNG8z2IdLbu21g6_qCEkyI1Ngc_VbKhXZS3B1yTpEeClOieR_vpGAdo_vx-96w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FVoucVxgejkz9qS29q0IkIo-oyMJ649i9xeERTkFKyFb2944cujyTlcNo7Z53xfdR_m016JzhJg7UrEi_GkycH6_gomD5G3tz8_W0XTygf4Aig0kVnmyn53mubFgYhWdv5kPpjpPo2KDuR1khXdZx4ugDWCrPZ4P22F3gQ3C-5mIU7m5VZ5QwuhsOirRIZxyKZJ19i0QtlcusV1dBPckPCgS8O1Qi4XdaK-28OwJH7B8R2mxIRfxz7H7NhhFLkFPB6WxJt5O5bGVIg4TfjAZFQJf1WP9UDb8agIg_JQLpU5RzXfik87QdFGBw1ItfUhj0mXC7Kj4PvTrQ4rIgF0pWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">+ قدرت تورم :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102336" target="_blank">📅 13:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102335">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cd1mur7g0Bu7OfUVfLr_ItgkSwhf6jW1Jio6-UsynhfqpXK2L8snwr_cMXRVOA4dpziR3BYYzcgxfgvesqu8mRBj9USRm-tYXj-sHqO4o8jrqcv-XlrrlnLV_wihJrJcc6ielBYXspo0RiWVVgycBTTIU85h5ImcktT18i1nFlhEF8OzuNZwzOpXeKH4ya1n-vXwg3OOzUpusDmcoZPdMPVO9krTZQWWM2E7bxGqtoAGU8IFaLwqZ_kvG_pNKXeUfDIPVawQiA-ygDrJW34Q0U-YkqUnL5CPmXioe568Vrx2cbVS-J8_uZafCFSWMEijeE_g65H-RYKBSIdCqMJMKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
💙
#رسمیییییی
؛ روزبه چشمی قراردادش را برای یک فصل دیگر با استقلال تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102335" target="_blank">📅 13:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102334">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkchMRsvDZ4KE5edD_rkPfeYgw_8EQrpzRyXjALb5PrjyCE0D6_dBH5n2hYVKBzJqjm4maCZV5fj3r0aCpYpPxFB_Ppjep8KLjE6q5igeq7AKWidseEjOGhtUrkxsK9bXq4wwlqCCU5C_wkP85mBZK7fcoP4CFc6wChsgfC_2ofJA18bI3Ypq6oyV-KwDY96r4eoD7TxA2gcmCa2jOXatz4hRWSgwh0rAo3LPxePfJRe6NAFJ_ueYpIVfVjQz2GwLvKWA-dmtWQbyIX9soExP9BSEySr2IlzPvVwX3oxG1sag_9W8r5yOe48YM4D5htvMOxFumFVQ200ZTp9HX_iYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
⭐
فوری از فابریزیو رومانو:
⚽️
ماکسین لاکرو از کریستال پالاس به چلسی پیوست. 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102334" target="_blank">📅 13:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102331">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W26kWG2jWbk2lbzRDWbc-Ya9ljq2zjBF1F_fug8yjHRJNgxw3LeVQLLsSIe16-8jzj7PKcASLaVjFyTkFZopnf6_ZAIvQdW6YnLha3-RaFkxX5iO_9UH94iqs5Xery4nTfr_7E-WhuIqhH9BOkZaI2tjeIw4jhupnw5OMieoFedrR9UpV9_NVSSA53KPplMmLL3h0orob4Z3p3Axi0WfR6V8suflM_RMVcy6ezHZlZ65A7V69XifTEsNY-L_uGk2xTHZn4pOkBO1k56SBwKEf1ghlUC8wxtN6B_ifCfEOuaV_wJGTTCl-jBPsNI4ZP5O_VzHZvK5yteiQdTVnTxWKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RE7cQdYD4ral2d4b1Ow2-ARaimubT6SuujH97F5aUSHsT-4mwkel4PGBStSkt3Wqk1TyUyiUg5RjmzqMraSgoDcydrxVHi67ylv8BwyhHSJ0Rk5WXo22Op6MiWOTnTsgZAy6RXZOuh5u_fJ6UjYB7yag96aeHqOp_SOw5EBpTPSDYu6PWWJcKlH3fOTCWH_1vW039yDBtIVouNlI7aHFpta08blT9hcEMOF4vWOJvcD3WzY-3EnN6A9BZD9Q1tmQTBkON1IKRNcIT0NQEvsyS1M62Rx4EttUqWsGfpRLGpJ1Ik2dRckQki2bwslmwfSjt1xriBhHMyrOdASBvtxAmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PD3ekLVl2vHrxbvJkLZQEqV69lOhYpEvyV_W5waGoCKqsBuMUPVajuGsdN1xUPNl8AnyQaqiWNBjXMr4cbOHRWP53qu5Sxx2RlkZCHMAadpK4bcW0RfcJIAwMtqXbh0o4_JBEbN4fYXvAZyxMyRBugOeCwen_-hBtjWdrV5kwGbuWuh0Y3WF_0w4XQfTFM7oWFnDc023wCiQmvZSrjeyCHfgfSdXswExxD1JOMbROfvv2CS3SRf1-hQLSnxbtmByd_fiJzcS7a3i2oKokfps9ZhSmMWuO6Wm3Ji9kJNl3vUFBUQSy3lmFSWjL31wsKpK2g31L-wHxsujqrqcB1x73A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🗓
🔹
اعلام برنامه مسابقات سه هفته ابتدایی پریمیر لیگ ایران
⚪️
هفته‌اول لیگ‌برتر
🔵
استقلال - مس‌شهربابک جمعه ۲۳ مرداد
🔴
شمس‌آذر - پرسپولیس شنبه ۲۴ مرداد
⚪️
هفته‌دوم لیگ‌برتر
🔵
استقلال - نساجی سه‌شنبه ۲۷ مرداد
🔴
پرسپولیس - اس‌خوزستان چهارشنبه ۲۸ مرداد
⚪️
هفته‌سوم لیگ‌برتر
🔵
استقلال - سپاهان یکشنبه ۱ شهریور
🔴
پرسپولیس - تراکتور دوشنبه ۲ شهریور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102331" target="_blank">📅 13:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102330">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N76WQI1-RtmhF2KvJoObCk4VkPiX4ZZUh326U9gylX4fM1PqCAwcuiBSSoWgJkYQwYi3skiPCRIxPfDpldt_EiDu9OA4zJMWU92eukzxh5YXaqJa8RNAmz4dp_ETbNh_vbbLcSzNxknXqZONC46AU3lli6MVL8Y1vFO-_QilneioAfYLwpBImFbBNw-kXq1mCSsswPAAfmrb3Po2bTIA-stxhFWdlNp4svUwcqKUgJIeEbDKqou5LubWpQUTwWa_5GgUEmzH8jEGNuy_nzI_2iIjdzdhEf72h9yaIQgPQ6lfiwKEejCbU4uGedxRFgdWg_OB4rYMyP1TfU6HonM8tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از کوپه: رئال‌مادرید و فولام بر سر انتقال گونزالو گارسیا به مبلغ ۷۰ میلیون یورو به توافق نهایی دست‌یافتند تا این بازیکن شاگرد آربلوآ شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102330" target="_blank">📅 13:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102329">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZT1fjONgIFf7bi5Ib1rsu6P_Wzd3a0JlDTyjSILQxQic9V8we2ayvhlY_ybq1-3V2jtJAmG2Z1kU6y9bBP_xXtj5en9HIX-R5cfX-1tU3QR4Y9ntuhptNyx9Oq9P3ZiyEbK1vk5WwPpsc1AG8HsckQLja80IuEf9R3yHBwJYms9FMmV_DMcAUTxx89KM9HTmdl4XqAtOu3aLP8lRXbdfJTqhVJE8X5CdSrCqef_POE2z88Dop6lsYz_NnOAsCdlw2FlsX8ip9AH-dosF_Rr9Qn0TnFT8ms3wz0Zv1PJBaM0d1GUEz-78ROLsI71X6vlaN-gm-_C1k9_Jsfq6Jcpcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
✅
توییت مجتبی پوربخش مجری سابق صداوسیما علیه عادل فردوسی‌پور.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102329" target="_blank">📅 13:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102328">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee8b739e27.mp4?token=F0T3CO26vg1p2sj_tSLWzjklYPjfVJUY4QpJmqy-dZkLKVb7vz_88NJHIAnPtMllYjxWnZmhY2ekjZaGY5JED_IiVIKDgNvCEGn4xZ1nXI0NbIHvfs3vxesJjng30DazyiWLBAq6JVnEaVI9Lt8XU2wupXvx_2u6XZFIXESvniS-VrSfKGVlgglqWU0zw-hUGMf5mTwmlH3Qn_wKe6BK0a420ljHmobsTFzWTKW5NdbJMgzRkZ9zUDIlhoBsfm4S_YaN1loNQc7n9oXrd9WFd0TovlhLz5MNBw9UL8jr8z3f8d_kJkXIIjw1QrCVT2r47gIDpVV9wJ01UeAYW8fmIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee8b739e27.mp4?token=F0T3CO26vg1p2sj_tSLWzjklYPjfVJUY4QpJmqy-dZkLKVb7vz_88NJHIAnPtMllYjxWnZmhY2ekjZaGY5JED_IiVIKDgNvCEGn4xZ1nXI0NbIHvfs3vxesJjng30DazyiWLBAq6JVnEaVI9Lt8XU2wupXvx_2u6XZFIXESvniS-VrSfKGVlgglqWU0zw-hUGMf5mTwmlH3Qn_wKe6BK0a420ljHmobsTFzWTKW5NdbJMgzRkZ9zUDIlhoBsfm4S_YaN1loNQc7n9oXrd9WFd0TovlhLz5MNBw9UL8jr8z3f8d_kJkXIIjw1QrCVT2r47gIDpVV9wJ01UeAYW8fmIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
روزی که مسی به برونو فرناندز درس فوتبال داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102328" target="_blank">📅 13:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102327">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHbbDkT7x6ED3EbMyaINKD0xaTjmYN9gNesbrXrqTxgfQuW0kFxrmAQ44uazH8RuVWnGiwb0j8SRdibuzrhWznVr6sGQj46FHbOLaM1Z-ADDH6jKdvQk-D_exrP9gezfTwpkn_21O9NxjJGrI0YkWUuSBvqTRB3atKmjiKyX05pQsEBe7S6earUjuEWQTbm6mZ70ggRTOqzy5FgqwOHqJ-AJr1s6v3d3IAz0GEspB5z6vpzNkroc9bDNAalMXSE0D9PQ_uguQTZHK_waOnWqPUr5bRJ7Nxw6xU68xHSeGjoHaRed2nyC4oy63qh-5JICGN-a5vv8cOhGX40as3gFVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🟢
صندوق سرمایه‌گذاری عربستان سعودی ضمن تقدیر از یاسیله پس از کسب دو عنوان قهرمانی متوالی در آسیا برای الاهلی، با جدایی این سرمربی به مقصد نیوکاسل موافقت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102327" target="_blank">📅 12:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102326">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa8a1ce74f.mp4?token=jlR_9y6wEhMv7VPR3CZ1WdDOfrPslRylJc_3CLXel5F27BF1xhT2qF-PedqxsUoaKddAmuUwGnoUKdEkOVPX10pbqnfciZYGkzd5J_48YwU_smwjYuLd_vZUgX4UnIGaQjV7wF4jN2J8Z_LVVVQg94uOXSZ4qA9TPPq1xFkmIbI8uWlfdLZ4jtvHqxkFh0-kSLLPdzXlYtmOcGNqgBKlDsdE3rXELuT69xG8KrT3ttYYACHpZm5g_hJ305gCG9hKqOFCufHzV_eMfb6S87ziCPTrgzYicOocibES9NDWSvnc0-Ai0zhoJKmnZBayZrvMOQz4b0F_YcfI0iZx-skOdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa8a1ce74f.mp4?token=jlR_9y6wEhMv7VPR3CZ1WdDOfrPslRylJc_3CLXel5F27BF1xhT2qF-PedqxsUoaKddAmuUwGnoUKdEkOVPX10pbqnfciZYGkzd5J_48YwU_smwjYuLd_vZUgX4UnIGaQjV7wF4jN2J8Z_LVVVQg94uOXSZ4qA9TPPq1xFkmIbI8uWlfdLZ4jtvHqxkFh0-kSLLPdzXlYtmOcGNqgBKlDsdE3rXELuT69xG8KrT3ttYYACHpZm5g_hJ305gCG9hKqOFCufHzV_eMfb6S87ziCPTrgzYicOocibES9NDWSvnc0-Ai0zhoJKmnZBayZrvMOQz4b0F_YcfI0iZx-skOdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
یه فلش بک بزنیم به زمانیکه داور زن بازی رو متوقف کرد تا به کاکا کارت زرد بده و باهاش سلفی بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102326" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102325">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49420aa7fc.mp4?token=g1ym-n_oqLscTlAc6YTdfojqtgpoWcQFbPt9IH1DqHetFSShzf0QlErXAnpsxR8_JGIHOKjsoefIQPI53HeXehBHATMaptMAy1yAXJr3EY-bwVTrRAr73hi0DUfgPzBoi-vvkqWm-5F8Ogm3nGrXedAZHgYCA3Hq0IuZD3oj8v3dtarCXfUtc2x_ePkpFP0hPWVHluI0gJcKDi1Pg85Bweo-6Qc-X8Rq1yGIHKTwN9TpRFihc_wJ9LZ6gEfm5C3VxlrTFlr6ionajD2Wi9fG6kpZhwGWeOxIjdfEz7KPx8sBoloT0uN0WxuYmKuSTMtOIH1nchCjGmVkqaDvYvsp8YAfKE2xeDSJ7iaCAsIaIFjN3-KN8W5v-mzgX1q754lgdqW59onzAeFIn09fNUiWIJWq1Jr4YVEG2wTXD-B_gpmkOlRsOahcQ8yokEuJgE1i0NH1ccDSD_oBK3xBSeoRBt_dVXklYRdxnKvITU2Xh_-0gW1m8dq7Fyv8wr-HpIEUyzWyBH-EI32CU_JO7z2hYrwCEzofmfsuLep-4Aum_ybSE7Z3BfTEHzeH9hvcS6p-jCU1hjJp7wQ8O_QUc_-E-zfNpd1-1x5ixqw2nOoRqzjLxBX6HAmmSX55AwjoRl96P5DKdzXLQoauzhNmGjOPibjLHv2w9qwhlGIMGoqL6Fk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49420aa7fc.mp4?token=g1ym-n_oqLscTlAc6YTdfojqtgpoWcQFbPt9IH1DqHetFSShzf0QlErXAnpsxR8_JGIHOKjsoefIQPI53HeXehBHATMaptMAy1yAXJr3EY-bwVTrRAr73hi0DUfgPzBoi-vvkqWm-5F8Ogm3nGrXedAZHgYCA3Hq0IuZD3oj8v3dtarCXfUtc2x_ePkpFP0hPWVHluI0gJcKDi1Pg85Bweo-6Qc-X8Rq1yGIHKTwN9TpRFihc_wJ9LZ6gEfm5C3VxlrTFlr6ionajD2Wi9fG6kpZhwGWeOxIjdfEz7KPx8sBoloT0uN0WxuYmKuSTMtOIH1nchCjGmVkqaDvYvsp8YAfKE2xeDSJ7iaCAsIaIFjN3-KN8W5v-mzgX1q754lgdqW59onzAeFIn09fNUiWIJWq1Jr4YVEG2wTXD-B_gpmkOlRsOahcQ8yokEuJgE1i0NH1ccDSD_oBK3xBSeoRBt_dVXklYRdxnKvITU2Xh_-0gW1m8dq7Fyv8wr-HpIEUyzWyBH-EI32CU_JO7z2hYrwCEzofmfsuLep-4Aum_ybSE7Z3BfTEHzeH9hvcS6p-jCU1hjJp7wQ8O_QUc_-E-zfNpd1-1x5ixqw2nOoRqzjLxBX6HAmmSX55AwjoRl96P5DKdzXLQoauzhNmGjOPibjLHv2w9qwhlGIMGoqL6Fk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در هرجای دنیا همواره فوتبال آبستن حوادث است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102325" target="_blank">📅 12:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102324">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbvZA3bySDKWPaR1Jd6uYSQeiNgvrWCgmse8nlS7hCymSs_08HJN-9ksOngeDkvbpS5c0Mbl4TLlKWphHH_HVeJjf12oourbNY2Ygx_RYuXdADCNP--Akex3EkMMdhUe8iF9fltxb0vnDmQcQO-1ahLN-sZL8KfIzHqQXgZiGO9UamUI-8FLpUrZrg6N12r34OjMxGFyZxIyhDyzYzT0FNiy8iX_zjHF_ZBDTvE4-oXNiu7XOIuY0eJrwaXbcCccQX4VMNUqffvK3tSL0qM32X01i2T8vvGieHt4Mfm_dntNsP_EkguIW8wOBYVtqRRsWhU-uU12GUcpehLmGTZfRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتیاس‌یاسیله سرمربی الاهلی عربستان در آستانه هدایت نیوکاسل قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102324" target="_blank">📅 12:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102323">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9305c345ee.mp4?token=cgZeBpBPfE3HDWgXKWF2Bj0AYxaQ5QDLx9NlFCc77Ejs4S-gPbjZbGNcOwDanBYhd4AsHN0F8tSCQO49V62GxKqEdJsSNwuvrVVAs_pDVMoREx3Wf4FY1Vku6dLQU4AWuIzPVaVq9jxFb9nyP6lnFLZr9eBYQgLnPQdIiij06Zo4rtGw3vUgO-kSPg2sT0ShDwsO4RMUX3j2KRDJwHLHWItLpjejdfdTN5OJGdfjzXnbo2nQba000LJgZ81RkBg_z2r36rDTPsDcJt99P4oVQLwN7gK3lvI9L8EEEBZTQI6JMN0PLvyiIwAz0z9hjwoerBNR7MbWpoZDAqjEf0inCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9305c345ee.mp4?token=cgZeBpBPfE3HDWgXKWF2Bj0AYxaQ5QDLx9NlFCc77Ejs4S-gPbjZbGNcOwDanBYhd4AsHN0F8tSCQO49V62GxKqEdJsSNwuvrVVAs_pDVMoREx3Wf4FY1Vku6dLQU4AWuIzPVaVq9jxFb9nyP6lnFLZr9eBYQgLnPQdIiij06Zo4rtGw3vUgO-kSPg2sT0ShDwsO4RMUX3j2KRDJwHLHWItLpjejdfdTN5OJGdfjzXnbo2nQba000LJgZ81RkBg_z2r36rDTPsDcJt99P4oVQLwN7gK3lvI9L8EEEBZTQI6JMN0PLvyiIwAz0z9hjwoerBNR7MbWpoZDAqjEf0inCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇧🇷
فالکائو برزیلی بهترین فوتسالیست تاریخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102323" target="_blank">📅 12:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102322">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1c528fcb.mp4?token=demVLvaVG-yUKFZkoCwE0wGUeLtjPO9MOBBBJsBVVorHfqa4jQM6ulvzl1bxiV5B4UfdVGidRUxqARQieBPRwBg8y_2CfmTdxQMUks3YiYQ02TasmCGMea3AptL6lQ0_waJbQlOy5TQZHqAPHBuatDZfVtHaFHBpSNvuvoqHljSLMxAVdQLgD0-56F7iCmizYnNaFZRiPO3pONvMQFUrO16feFlk80E20MQ3g_ChYTd7VLTdKog7DV_yfneN-BO05ik_xRLy0p3-Eaj4BVn3iQvbJvvsSCueINi1cU2e7C1EKLpC-E0p-nYVVP-i9Driu1g1lCyPD3sUCIuz1CNzQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1c528fcb.mp4?token=demVLvaVG-yUKFZkoCwE0wGUeLtjPO9MOBBBJsBVVorHfqa4jQM6ulvzl1bxiV5B4UfdVGidRUxqARQieBPRwBg8y_2CfmTdxQMUks3YiYQ02TasmCGMea3AptL6lQ0_waJbQlOy5TQZHqAPHBuatDZfVtHaFHBpSNvuvoqHljSLMxAVdQLgD0-56F7iCmizYnNaFZRiPO3pONvMQFUrO16feFlk80E20MQ3g_ChYTd7VLTdKog7DV_yfneN-BO05ik_xRLy0p3-Eaj4BVn3iQvbJvvsSCueINi1cU2e7C1EKLpC-E0p-nYVVP-i9Driu1g1lCyPD3sUCIuz1CNzQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
❌
الکساندر پاتو؛ ستاره‌ای که قدر خودشو ندونست و خیلی زود از فوتبال محو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102322" target="_blank">📅 11:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102321">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKVEJBVUSVZFSTIXIUhhjLTbsoqBVjMvIsEEtbuuaYH937HeiA6nDkhVNsNh-ygAWYEfggygT6XxiwEwK5qiGcUPMBlO_N9tI44NJB_Q0-u806bsBSeJxUzPIkYIcL8isP15ia2FVu33CCqMcOdt-tGawkYyNbpHC2OgwzRLlswMUoGvtNfGUV-b4vWdCxZ72tBJFuJv-DF32CyqWboeeKMk8MzuMpkCWcqhlx_udtohoS-mRx7zL9L9QUzC82cs3YttPU62dHaUFChJGiP0ILWR_2fWkiv5Rt909ToXhDRcPmmXEQ5cfTY_4a0CFptvO8emlz7SY9YdABd7aXQWQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
⚽️
رونمایی از کیت اصلی النصر برای فصل بعد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102321" target="_blank">📅 11:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102320">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
🔹
بازیکنان خارجی ، 4 مدعی لیگ برتر
:
🔵
استقلال:
🔵
آشورماتوف، ماشاریپوف، آسانی
🔴
تراکتور:
🟠
خامروبکوف، هلیلوویچ، ایگور پوستونسکی، اشترکالی
🟡
سپاهان:
🟡
ریکاردو آلوز
🔴
پرسپولیس:
🔴
دنیل گرا، اوستون اورونوف، مارکو باکیچ، ایگور سرگیف، تیوی بیفوما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102320" target="_blank">📅 11:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102319">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGQeWK0c40-r2qUhbbIeULxxtBbNPzqmwq4JORMcn0C36pFJLcVVngaVG6XQwBwlFs5VfXWk8GxmfT-0UCWPAjzUzm9XwasyYmcg5caglseTwyF0Vcv61nx9XUA_XRii3fOLXy7ccmaOMED8sZygcKILNRkrfAFFkEjx3VnlZ2OhwW4gRMywjCyNkcYS7qnd0Jdw8lrwWVVt5p52uN-m6Yar5fiWX_SC0g0_tBtSZ37-obSkXVL10s2TadrDaGIxr0gwWBHerWS0VxGgW0LKbismlIB4jKo47NpTT6vaoprkOLrzqABDzhK8mk_uA5YK_HEv5Di0GnXpK_q9YGyOlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتیاس‌یاسیله سرمربی الاهلی عربستان در آستانه هدایت نیوکاسل قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102319" target="_blank">📅 11:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102318">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=sWm2bKFDoXwwrkN2QF-ErIM2XiBCJ1HYxGrkNZHJ8XQQ6LO6eBUHSPwMAHq2B5AWwWyOLlGKAVx62aMoBMDLS9yBRTLNGIiSkJqQBvWyKp3mFteh4xSRPJY0Ye4aLUCygJMfkzZT-c2c-xuBvukDbsENGB7Ld2T_pZMHDYm2xKW7kea3zMYU-uYPzuOK6vqnvKEiVDLmVP-VoQe0O6GvJrcAHIdrocjIf9yALCCN2r9odaaRR6cA4hd23CqDTMN-Elo5udDne_cjWgYG2hTWBdwUEUN-vpLMKQ8g-ZSDXTH1tqlWdrq7wgM1y6jIvKD4x4GR8EtqCl_Nzjqp3TFjcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=sWm2bKFDoXwwrkN2QF-ErIM2XiBCJ1HYxGrkNZHJ8XQQ6LO6eBUHSPwMAHq2B5AWwWyOLlGKAVx62aMoBMDLS9yBRTLNGIiSkJqQBvWyKp3mFteh4xSRPJY0Ye4aLUCygJMfkzZT-c2c-xuBvukDbsENGB7Ld2T_pZMHDYm2xKW7kea3zMYU-uYPzuOK6vqnvKEiVDLmVP-VoQe0O6GvJrcAHIdrocjIf9yALCCN2r9odaaRR6cA4hd23CqDTMN-Elo5udDne_cjWgYG2hTWBdwUEUN-vpLMKQ8g-ZSDXTH1tqlWdrq7wgM1y6jIvKD4x4GR8EtqCl_Nzjqp3TFjcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
با اعلام خبرگزاری رکنا، نوید زیادخان قره‌داغی همون حیوون کثیفی که دخترارو تو خونش کتک می‌زد و لایو می‌ذاشت، بازداشت شده
⚠️
‌‌ ‌ ‌
یه ویدیوی وحشتناک ۱۰ دقیقه‌ای از
این حرومزاده منتشر شده
🔗
🔞
مشاهده ویدیوی کامل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102318" target="_blank">📅 11:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102317">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
‼️
🗞
🇪🇸
رومانو: رئال‌مادرید و لایپزیگ بر سر انتقال دیومانده به توافق نهایی رسیدن اما دلیل اعلام نشدن خبر اینه که لایپزیگ ابتدا باید بازیکن جایگزین جذب کنه و سپس خبر رسمی اعلام میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102317" target="_blank">📅 11:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102316">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a432ebcf02.mp4?token=pMBipM37Mp47pe2qPOwbLOBaYw7e_il5hGf8o73ESFXq1GnB620BACVdRoBHdyYKjoabU1-jpg5l9zJLObtFLr8jo9v5_C-ZlDJdsh2HX_M7XELG1sJcMo2ispByjjSSLrkeHQT2mopHjDm9w1pjIlf8w0lFfTJIVOJA0d_wnAWuNljOrA0YMgKPYFRbxaQwYh2G6FHdgR6xmtgdIw5GsSOZGzIyinXqKuK-xDhiffX3JTDQNv9HxcTl4IduJnCrBYBqIs09YR4v386lXoJ8yNJ3BVqempkFfkMPWx52zbLa7p8buQ5ZkH-qdx1jvfS-2ZiODJ2WxGLgKj9wwUR7vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a432ebcf02.mp4?token=pMBipM37Mp47pe2qPOwbLOBaYw7e_il5hGf8o73ESFXq1GnB620BACVdRoBHdyYKjoabU1-jpg5l9zJLObtFLr8jo9v5_C-ZlDJdsh2HX_M7XELG1sJcMo2ispByjjSSLrkeHQT2mopHjDm9w1pjIlf8w0lFfTJIVOJA0d_wnAWuNljOrA0YMgKPYFRbxaQwYh2G6FHdgR6xmtgdIw5GsSOZGzIyinXqKuK-xDhiffX3JTDQNv9HxcTl4IduJnCrBYBqIs09YR4v386lXoJ8yNJ3BVqempkFfkMPWx52zbLa7p8buQ5ZkH-qdx1jvfS-2ZiODJ2WxGLgKj9wwUR7vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
از دعا کردن تا بزرگ کردن لامین؛ چند کلمه درباره یامال از زبون مادربزرگش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102316" target="_blank">📅 11:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102315">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/areyUSx6HVi3-WK8kfnLBTRHl9NBxkgMaH3oXO0t_7xy9xVRF2K2mRXRmb5GHsuGETT_UVDESiT2FyF8kUTTce1DNyxGIAOQiGSaeGyCH8WopkflBP0-EhVO4vBkq1yl8jRZ1tw9OIk7BCCk-VhiT8Pp3tehexmRr7Vtb-zProTzKZUtsaLDL5M4RLGJ-lxLasexvvt74vK6PScctqb8dZ5telYkssFI0USovG9v6gq2HkzTkq0l2b9fOcPhQqjg_Rwno29PyMAJAxy3G63kSdZufsR6aU8-QiwLTPPz6O2O84hQrRMzbyq6yM6Kio37Zgsy0Y_IyQDceFP6FA4ydw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇦
🔵
با اعلام رسمی AFC، مراحل حذفی سه فصل‌آینده لیگ‌نخبگان آسیا به صورت متمرکز در کشور عربستان‌سعودی برگزار میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102315" target="_blank">📅 10:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102313">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCjs-HmQg0gaaGr2AR_WwZ_uUqcHeq0I8aBZ-8VHDid-uVEJ5KY2H6m1R4t1AeOuw7AqQVQKIKhMvFt-mtQ4SdrX5uEXEzl7IIou3mZOnMO2uEU3Xi1l6vOrStwCfofVZBrEAvJg8dYLbdRCUVcgX5YJfJgWqIiRRTOK6fz1qVGaUvN6qOS25KOAOhFU8A1xOVdemZeSl33sp0X5G59g0M_4k-RIHLDpn-1X4Qr3Kvm4IQ0U7xGcoNakvkVMebjEFr3FJh1mCld1HnfKEn1XteMcmKVWcJouiSl2jv14-i3cYoYd3s_lsSdqc1yI2yxAA_cHOgrr3DdLYOt6sF2uBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ایوب‌بوعدی ستاره جوان و مراکشی باشگاه لیل در آستانه عقد قرارداد با منچسترسیتی قرار داره و بزودی جانشین رودری میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102313" target="_blank">📅 10:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102312">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac4341594.mp4?token=IzE2UGaQnRPml_qlj_b4w-ATHDrdMb8R1tX5R-YWL01Q2YDVDtSQveqMbTkpXMbUr3Vp-g3eFMzrihdu7sUkRKdHA714r5WFJwTojl8vPREF0D-Q5U86e5BfsGavgmKNGd3foYQhJz7xG95EW5dJ2J7nodWYyPZAcwJymNnhe29t4eRbYYMYBpiJDrVVCcnBVVb5p0o4cKyVkxnm-niV07U3APcOOonp0h9UFxZaU-RzuiWUXTO13z9G8bJ0y3-qcNpyswR2TNqiy85DBdK8ZRkAxY2oAjXU3HraaygQSYWgYMBJ0wUS5jS7KfPV3vqQ2lsCENwdPcWSg2I_i1eYog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac4341594.mp4?token=IzE2UGaQnRPml_qlj_b4w-ATHDrdMb8R1tX5R-YWL01Q2YDVDtSQveqMbTkpXMbUr3Vp-g3eFMzrihdu7sUkRKdHA714r5WFJwTojl8vPREF0D-Q5U86e5BfsGavgmKNGd3foYQhJz7xG95EW5dJ2J7nodWYyPZAcwJymNnhe29t4eRbYYMYBpiJDrVVCcnBVVb5p0o4cKyVkxnm-niV07U3APcOOonp0h9UFxZaU-RzuiWUXTO13z9G8bJ0y3-qcNpyswR2TNqiy85DBdK8ZRkAxY2oAjXU3HraaygQSYWgYMBJ0wUS5jS7KfPV3vqQ2lsCENwdPcWSg2I_i1eYog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Auraboat kids
💀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102312" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102311">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZfUQMiq2I185i0g-kq3l2NLU-xLm84lN4-76511NvD8XeREdJyR0fvGqNG--UTfQSLB1EWDBIz_oBG6FCMW4FILMf6N9FjeY4NS8UX-WSISxSBUFBFIoO4mldZEcXNE9Nxeuo9u7sZ9mIYRb_O6HTz8HnnSf327D-ekOWo47c7257Kw75X-cpHHE6s1rla6frR-VKND4LE1Z4ZlFRfDTNlHGld_fqVZIFyd_yxfsNX7gWo6Y9_5hk5sxnbPzN1Y32Pqd4WaEinn7kR0YdBkz9psp4dGWQHQaGAto7cpOPR0_n6JFUoxSEpC3d4Rzxpp2uSpEuOY6KfViU5M1UsyBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
تمام‌نیازمندی پسران فوتبالی سرزمینم :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102311" target="_blank">📅 10:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102310">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jq3gUhoFLJEE42U12tBzXOdnFzQbQ44XYSDnHKp4uu8h09E6RS8eBIYy7pCiuHN72XWgv__YwsSAkeeF6weHbCpeRpU86PBZWQiuQnsUB73Wh4FojJl5HRhiKPiPrm_EKAZwYCwoHAffsoIeR1uMyYZgD7tswWmEF5vVbbLjiFIa536aUNNt1MwGSqwTo62HpY_mlTEXBAqFeY3-kEu-hcsxqtKumEgm7EoptsOZWZ6WiFM5w0YFehOntU4EM-TNriTLZnHzZWph80HTKdru3fLQVyuX5YCM5DCZvcXDlKsHMSfaWu9NhDUspAvii-v19l_ZeUOx7q3WmnB5jboQDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🔵
فابریزیو رومانو:
پاریسن ژرمن و موناکو برای انتقال مگنس آکلیوش پیشرفت زیادی داشتن و معامله در قسنت نهایی خودش قرار داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102310" target="_blank">📅 09:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102309">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjRBLyXjc6bqJyOlKTuK8D843oBKF-AN6nnC96kcwBfEA3rjKBVGgHwUgdXGy49ojABhLL_ydlwEqDC5YKRh7e6GIUsnIsCX5X6JJcKZ6IwpX7BKoax-7DTRPyviqdJOwkirjQ46ImGx-P91QI3GTq6AjcsHFfx04kr0E8KIcwMIvWUbl-ic2M14zUhJWFQUO4H587s2QqijaMEyOWA1NDv1__SUikdYmBm32SC1A34pfULHeS6iXodl2wEAognhFCFRoXf5By62I9xJVhskRoRtGfVeg3WNH7VEei1evOZ8bqI5M6IrugCQGv3kmZMUTPCxIw5Z8f1hR0j2FKULgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بلینگهام برا زیدش تو تعطیلات عجب پایی میخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102309" target="_blank">📅 09:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102308">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTCZJTfLTq6mY3y3mgXU1d4ZHS3kInlJl3Oo_pT_JAhlUlMY6vwwE4_c44S3HGNc1wjKrMys4FNDW7iSyDt3_j6-5tgvMhLDww2-ZAGYMODIA_6I9oY9Wb7gx9e_XVMRjYz7IpuX6sJ_XtJffPno7kgnQFNLJVpzo7EgWonBm3U5JsXYNkQ3J_vVLEimoG9FOvw2ai0VHKemivex8hOZo5rfDr0vHjmBf6TeiarQJceC2M9iDz7siNuJcf_cTQ6SSjy4yfR3q-Kwf2DbH8Ao3adZ5IthvoQxKJUVcaTVa1tfjF29M5fOh3exg5v0twCWAYgp9JGEt6mPB0sz-2fYmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
عکس پروفایل فرمین لوپز، در حالی که تمام هم‌تیمی‌هایش در تیم ملی اسپانیا عکس‌هایی با جام جهانی دارند.
😭
🇪🇸
لوپز در بازی آخر بارسلونا قبل از مسابقات جام‌جهانی، دچار آسیب‌دیدگی در پا شد، که عملاً شانس او را برای حضور در جام جهانی از بین برد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102308" target="_blank">📅 09:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102307">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31f0971b6a.mp4?token=kwFG5q0I0UFA3m5bGLTQzZQKSIedHjrNhwp8b6nuRseEUTGwP8aDrGNizeekpBZ762fFfN-3etLQHEYBFwT-5SUbW-cEhS80TjMNnXjuWQfGnD50UHxMDijIvQaF-nkPWse_ysbKDPmtGYMxSckx2TkRXZ-7WtsisBDfoVsOhV9CLaxjGyiWDUJsuWp5fhjKlzc9YHlVsDSUuHy4-TiZcH4hMYEtOPXJKTychdnkNmnpwR_g9L559OsnNpacHZTbc4nEqZMLxj61nDfM9QrlYOm52K_ItxLiBxti-02Wh8ihJM7vhQL_qowsYr2AHf-9U6KJzf2Z5Lj6FH-_sYVWUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31f0971b6a.mp4?token=kwFG5q0I0UFA3m5bGLTQzZQKSIedHjrNhwp8b6nuRseEUTGwP8aDrGNizeekpBZ762fFfN-3etLQHEYBFwT-5SUbW-cEhS80TjMNnXjuWQfGnD50UHxMDijIvQaF-nkPWse_ysbKDPmtGYMxSckx2TkRXZ-7WtsisBDfoVsOhV9CLaxjGyiWDUJsuWp5fhjKlzc9YHlVsDSUuHy4-TiZcH4hMYEtOPXJKTychdnkNmnpwR_g9L559OsnNpacHZTbc4nEqZMLxj61nDfM9QrlYOm52K_ItxLiBxti-02Wh8ihJM7vhQL_qowsYr2AHf-9U6KJzf2Z5Lj6FH-_sYVWUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیوی سنتکام از حملات بامداد به ایران
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102307" target="_blank">📅 08:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102306">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‼️
👀
اسطوره‌علی‌دایی امروز رفته بود مراسم ختم اکبر عبدی که مردم این‌شکلی ولش نمیدادن و دنبال سلفی گرفتن بودن!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/102306" target="_blank">📅 02:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102305">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7xGV62-UMEeTKu72lr39dNR_5gEN7Gk8_RD--quTQOWb8ozm8yyTEfNoHhYzwXoJxKGlxQSN3NGkwiw3aVk6WkJYtL_90iKS_fYTkueyPFciMXG_KATif5-tP2pDtFFUg0ygulySOyX805ap6kv4pJCq2H3msDUEubfGxjIYky5M6ONUoZgQYtrFHNlvALWVCtCCmF-68m888t3KppTJDwH2qXMKmYlFVgX8E49a_5u6eqtvOyx04KtwMCqoq0FeBiNzSjOmsc_VhIeDb3G04NZcYIJXSwLeACpzneXbIJzLibMqcGh9iTtVewX1Nh0yBjl6Xvb6PwsY5-xgIv85w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از Cope: اولین پیشنهاد رئال‌مادرید برای جذب رودری به ارزش ۵۰ میلیون یورو تقدیم منچسترسیتی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/102305" target="_blank">📅 02:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102304">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwOZ01dD63KYF53ouXQCWj7ECVssDb4n1_D8LCr1d8mlDIanvqBB82Kjc1QRYr6Eo031AjrBJuXnvAplQMIXoIdRKhR7efBpiV2Fe5VPhl3w2mXeiecgkIO2L4YiT5DzVZyXczcsVRBl82QQGiNiMy9NfHrMovZApDj5u-sBozjkjZbKtHGTvsHpYB1M_Yuy6nuCPvWl6CAM9F__62zbducF-r7ffXWTESSmrA_fQteF04KYSjeIiA_g8NHExzEMZuxjhtUcQ3HQYYs2xC6iaDFxaCwL6rW5nVK2ZHP5EQCadulKo5f7Flv3kVsN9qZ3L4qKOb14Yi8h55ai-ytwtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
🇮🇷
وال استریت ژورنال گزارش می‌دهد که دریاسالار برد کوپر، فرمانده سنتکام، طرح‌هایی را برای یک کمپین هوایی ۱۰ تا ۱۴ روزه با هدف قرار دادن زرادخانه موشکی ایران به ترامپ ارائه کرده است. ترامپ هنوز تصمیم نگرفته است که آیا مجوز عملیات کامل را صادر کند یا حمله محدودتری را انتخاب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/102304" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102303">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6afbb43876.mp4?token=q9AJsTCv2P6eFrjzXzz7BU1AAzRCkZqdkfIS7eueAiyJSCihJ-7FyIcOSv6TX3feUXESCDAmAXDJtF-BAuOB55EC29HXFnVtTRRwj4SG87H3786vI4CyWJxbFRc4In2d242R9eagyTlEPGYEFQT6d1KBU_JlIyW33zqwE6C1BrwHOjYApGEjTdUn540TDYoDiDTGPgbkmRlbZHMlCXrRPYAfke7pTSRjLh-f8aMO9D-7Q16-f-_Wt4cyUZXaqM-_Ymq91c9Gb3K095ZdfJZAHQTaVrbUNAstrcwVklxH0tCXXqRJbCb35nAjw0LdIq4LBZQ2H6wzm5YvRxe4fm6AQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6afbb43876.mp4?token=q9AJsTCv2P6eFrjzXzz7BU1AAzRCkZqdkfIS7eueAiyJSCihJ-7FyIcOSv6TX3feUXESCDAmAXDJtF-BAuOB55EC29HXFnVtTRRwj4SG87H3786vI4CyWJxbFRc4In2d242R9eagyTlEPGYEFQT6d1KBU_JlIyW33zqwE6C1BrwHOjYApGEjTdUn540TDYoDiDTGPgbkmRlbZHMlCXrRPYAfke7pTSRjLh-f8aMO9D-7Q16-f-_Wt4cyUZXaqM-_Ymq91c9Gb3K095ZdfJZAHQTaVrbUNAstrcwVklxH0tCXXqRJbCb35nAjw0LdIq4LBZQ2H6wzm5YvRxe4fm6AQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
عصبانیت شدید آزیتا حاجیان خطاب به مردم در حاشیه مراسم ختم اکبر عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/102303" target="_blank">📅 01:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102302">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3gAKvddXfJ2okjMH_sCwq1XRWJ_VDqmswmoDLJ61a0Qf0niaGe3mpDSvAj2rLIS4GOmMhEarb356L18KCM72qdnPrmce7V_dHXJhz_0pzPsTPCwX9yKSR_M7xD87EkEU2R0xiQyYxQQIa86_fzEJCkI0WjH7xy2icrwr2DNw9PAHTi5oo3dVj9fVhY_cBGJzduiAMGdMcRSuourkVyguOz4faHHSgxSngfjFAdudHTaGQ-UFtQr8K7KCyco2-ob_zDR7cckyneBYkSJrMWhPSS5YK2akfBwRUUECzhIjzSzTvE63I2RFjpBFPb_27_Fq-dO_q5JTcYeh_Tss3oygw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🟣
بازگشت لیونل‌مسی به تمرینات اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/102302" target="_blank">📅 01:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102301">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4e2122bef.mp4?token=vMrAXgOWbdSKrGKrnqRtBP4flXL_3W0fnx-QaTTMQMViDQqP_RCSIJmydN3keaHu87Vofzoer2v0ltIVdFny1mBtTV_YmTIMxGwkx2fKQZeOPvzP80WbJNFSZHFPkN7Vgz-HmCsAgMwH1pafAweVlPD1XREHaY5aCseWIBgo6jUkhz7fwYhpm5SpeTO3JMSyhqZ9IdXWY-rfoRlbvaEhYiKtWFOFz2oNhtfd4ZtHWv3EdhA_C9QwIAE-E_k3BXMCIscZexMgLWipgqLyIh02DXQVg47aeYSN-B3TLvvdD66K7lMTX8HczWz9M_lrsf8oEMo0HwEjCrQ9R9T7RGX8jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4e2122bef.mp4?token=vMrAXgOWbdSKrGKrnqRtBP4flXL_3W0fnx-QaTTMQMViDQqP_RCSIJmydN3keaHu87Vofzoer2v0ltIVdFny1mBtTV_YmTIMxGwkx2fKQZeOPvzP80WbJNFSZHFPkN7Vgz-HmCsAgMwH1pafAweVlPD1XREHaY5aCseWIBgo6jUkhz7fwYhpm5SpeTO3JMSyhqZ9IdXWY-rfoRlbvaEhYiKtWFOFz2oNhtfd4ZtHWv3EdhA_C9QwIAE-E_k3BXMCIscZexMgLWipgqLyIh02DXQVg47aeYSN-B3TLvvdD66K7lMTX8HczWz9M_lrsf8oEMo0HwEjCrQ9R9T7RGX8jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🟡
افشاگری مدیرعامل کارخانه فولاد مبارکه: دشمن با بیش از ۵۰ موشک مارا هدف قرار دارد و بزرگترین دستاوردش در جنگ همین بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/102301" target="_blank">📅 01:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102300">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uc_NYP9SZ3kvy87PLZpzm8h8z3rm-IabnCmjSbIkHQjW7MjaPbBpdarHtOkcZV4EQI4BpB8z8QaILILXR1BYLRzDuryax9ANT0EaAAT2tgzBnK0XVPAMFbyLmmSQaq7KWzuxGPYyLrPamXcmzdJZ-Fl2nbMrOzyVRDcBJucS9alY901NLkoXPgfDydI2zkTmp-iONEQO3wJZfaOoklcay1vdJ7zdUuu3Zai4HISOeDRs6t-16lnCxKIuaRSssQbwDigaqrTBWUUuCK2UhkAQvyt9OajO_IRz5o8C4p0bAC7ttl8cqkHIfSqTX47hlKyVxuNayY1hDSf2RvKGgb00OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
📰
به دستور ایلان‌ماسک، صفحه خبرگزاری تسنیم در اپلیکیشن ایکس(توییتر) مسدود شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/102300" target="_blank">📅 00:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102299">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fe21feda.mp4?token=Pxy0iaGELAKZRJMckN-Mm4Wms1Dux16NlJmHNuMCKe-Zo0-Ast6uGfZdIcYcPyGE_nJvt1xyXVKP0owfxzB-5BTA990tNyhtcjvRgSY4xEcLau4uQp_0Kj4Dvix1kBI8HNDVppuCZlrgllO5GGUjdfK6jeLtWbKvPLSua06zfGmbtJbOrvn5Vn0fNCyV6O0AdYaPoTlkn5mWsIIwr9Xq2Hc8JUnQzTyY2lIHDXSmtM7zLxP5QdqUPEJ27C7u55aJLF3KSUyz2g_gXfVRhKeIYlJkvSqwKBsmpGRL3ZbxNMqcWYIV7V3G3GQQmDEdA5BD-g0h31sOF8WnOVKTyvoFaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fe21feda.mp4?token=Pxy0iaGELAKZRJMckN-Mm4Wms1Dux16NlJmHNuMCKe-Zo0-Ast6uGfZdIcYcPyGE_nJvt1xyXVKP0owfxzB-5BTA990tNyhtcjvRgSY4xEcLau4uQp_0Kj4Dvix1kBI8HNDVppuCZlrgllO5GGUjdfK6jeLtWbKvPLSua06zfGmbtJbOrvn5Vn0fNCyV6O0AdYaPoTlkn5mWsIIwr9Xq2Hc8JUnQzTyY2lIHDXSmtM7zLxP5QdqUPEJ27C7u55aJLF3KSUyz2g_gXfVRhKeIYlJkvSqwKBsmpGRL3ZbxNMqcWYIV7V3G3GQQmDEdA5BD-g0h31sOF8WnOVKTyvoFaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
پلن آخر بارسا استفاده از ترشتگن تو خط حمله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/102299" target="_blank">📅 00:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102298">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqsXnpnrpAhZJjLCvSnYEBBLw69oe0Au228jBo5u2ouW25eaygYnKqmbZ6sHjr7wFjtrOPcLNAncUpAaqrzPeYqZv_4Jg8iRln7CyeLYc6cW-UCW5DOrpZ6oC-LxXhN6KJukawOSpJmuedK2-TObzjjj8hepXmk65xe2ClpmcD74oJM2SboYzIEFxEk7oOlqbNGeBCedcFKNaq8bgSeQek-zO1kidFdBXOh-CDoCZb9mUcP_7Hi0lbqfk-Ly-GoemsnT1t3nUxcq2G3dvQZhDrZh3Bm2oGlP2z30f2SBanEKd4pcs1_rx3_u-X0uf22hC4MGYxhdNAo9G_cfH9-nxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
په‌په‌آلوارز
:
🔻
مورینیو، وینیسیوس را به عنوان یک عنصر ضروری در رئال مادرید نمی‌داند.
🔻
باشگاه، این بازیکن را مجبور به ترک نخواهد کرد، اما در عین حال، درهای خود را به روی یک پیشنهاد "مناسب" بسته نخواهد کرد.
🔻
همچنین، باشگاه قادر به پرداخت پاداش قرارداد به مبلغ 80 میلیون یورو یا اعطای 80 درصد از حقوق تصویر (حقوق بهره‌برداری تجاری از تصویر) به او نیست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
از طرفی نمایندگان آرسنال پیشنهاد خود را به‌وکیل وینیسیوس ارائه کرده‌اند و حالا همه‌چیز تحت نظر وینیسیوس برای پذیرش یا رد قرارداد با تیم لندنی است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102298" target="_blank">📅 00:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102297">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pg630osUnipgPpRZCSgSyD6UV7G22WWqFCMht3vnU8SCVjFwnzagtfh2y8Ar0Tw6KOmvD6KScz2Zw_PVBZU3twmQ30Ocn8YRe5Sxy4q8GSWrAt7mQ1zHHSg8pj7VfrZT2P4XgY_visGGCVBTQqcQSDhRhSHMUI7eBBpAPdv6Mqsh9w_YkBox92Wfpw_aFIZyX6jocttJqX0pcVFYuCz_k9h3_8OsuTpz2plOpueHqiyBvZQxzJZBF8pcnWKs0ntdkKjxkGOAxPJnF8zM0IQgPh2Qa3DdkXYYaUaLl0Kp1GZ9mwmqDGTA4EB7dDkug5GJahq55Qc8LuYn_zwGFRx4-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇪🇸
🇩🇪
فلوریان پلتنبرگ: امروز هم توافق میان رئال‌مادرید و لایپزیگ بر سر دیومانده حاصل نشد و مذاکرات به فردا موکول شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/102297" target="_blank">📅 00:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102296">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a93d51cbc.mp4?token=M95FfgbiZg69cRN25DDo04v2xHaWwL68rifWHD_idUfFXUOF30N_pbYJtARGMJMoR5Ve6gthXuqw9Lx4LF613X9CZ7twVx-VtwdygRp8tHuqdFIBTGJf_RNAb4bsQtdHnaaDlIH-0gqHWOtM8WENCnEjNufo0WQkN7RfCgOqV2udJD6NHQALHO9iGm0mtqJxMz_SyuE4NXCNrfsNa1qP9eMQ3Ii1O5CACr446hAUl80yLXGvwElnV-w6U2GWoVvbzK1AeQijbCGzf_2snewgKXFMyZGtuiWZ6ubwoAq12Fu-NAPuT9v8RzLg1wncMoEn4P5dKb79dslfd05QHO-CuTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a93d51cbc.mp4?token=M95FfgbiZg69cRN25DDo04v2xHaWwL68rifWHD_idUfFXUOF30N_pbYJtARGMJMoR5Ve6gthXuqw9Lx4LF613X9CZ7twVx-VtwdygRp8tHuqdFIBTGJf_RNAb4bsQtdHnaaDlIH-0gqHWOtM8WENCnEjNufo0WQkN7RfCgOqV2udJD6NHQALHO9iGm0mtqJxMz_SyuE4NXCNrfsNa1qP9eMQ3Ii1O5CACr446hAUl80yLXGvwElnV-w6U2GWoVvbzK1AeQijbCGzf_2snewgKXFMyZGtuiWZ6ubwoAq12Fu-NAPuT9v8RzLg1wncMoEn4P5dKb79dslfd05QHO-CuTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمای اورانگوتان از بدن کوارشما ریخته
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102296" target="_blank">📅 00:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102295">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4b353d1e.mp4?token=C2geYBjnOmF2NztNgGys_zV7MnIKtd7LPsWtCZsiaw6nw5YwQzpUX941xNa1IqDBdQyd8Hb_ZrdlCJDIqSBUL0TKhfSst-zT3wsjQ9KORl2Tjrz689fWUsEit-c2Gu5ZcJdgQ0JKK268RT9msrzLs8yUpvbejD5bfme0oDK_NZj_s5LqKyHImz1b7shFk0eC4fYDgXNOZu1can43PARg5FmipWcz3uC7lS9yKn5KrLnUNRt6cks8Wpq1qcahOhRYHBgi81AeBoHhwmhb_463DWkXbLxgETWdrrT6WS5XQ2ez1ZafC_ZlvXhjNGInBWjQeLC9aA9qSYKq8KWZPZ6b4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4b353d1e.mp4?token=C2geYBjnOmF2NztNgGys_zV7MnIKtd7LPsWtCZsiaw6nw5YwQzpUX941xNa1IqDBdQyd8Hb_ZrdlCJDIqSBUL0TKhfSst-zT3wsjQ9KORl2Tjrz689fWUsEit-c2Gu5ZcJdgQ0JKK268RT9msrzLs8yUpvbejD5bfme0oDK_NZj_s5LqKyHImz1b7shFk0eC4fYDgXNOZu1can43PARg5FmipWcz3uC7lS9yKn5KrLnUNRt6cks8Wpq1qcahOhRYHBgi81AeBoHhwmhb_463DWkXbLxgETWdrrT6WS5XQ2ez1ZafC_ZlvXhjNGInBWjQeLC9aA9qSYKq8KWZPZ6b4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال تو تیک تاک : دوست دخترم خوشگل ترین دختر دنیا با من آماده میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102295" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102294">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102294" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102293">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=q6TTckZyvg2wAbnTPvMDrNAKisG31ajKmxHIwyr2d27JhGBCM1tpraJFPSwd6eCIo4aS3OaD-yHS8p5QNANz_UIMyzXJcDenSFIiIe_Dyc5x6gbsWLHoocF7RxxzViZ76PLLrjQDe6bc-bo4NVVSbXch02awq6jduGFnDYW4_BRSM9Vi6CtKh26iunYbxCOJZ5qImPiJDLOYlZ3SqRTUsEaLIhn6OIXwG8CUQlt3nd6lYZOjsyQOl_FrpQPsgjwhZZj2r6nBcAPRcG5wTYPS3_vHtvB2R2G8LvM1iC0jXwGdOwBM8G0trD0mNb2Z5mIpLOQcU_mybq7p9QLHruCjog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=q6TTckZyvg2wAbnTPvMDrNAKisG31ajKmxHIwyr2d27JhGBCM1tpraJFPSwd6eCIo4aS3OaD-yHS8p5QNANz_UIMyzXJcDenSFIiIe_Dyc5x6gbsWLHoocF7RxxzViZ76PLLrjQDe6bc-bo4NVVSbXch02awq6jduGFnDYW4_BRSM9Vi6CtKh26iunYbxCOJZ5qImPiJDLOYlZ3SqRTUsEaLIhn6OIXwG8CUQlt3nd6lYZOjsyQOl_FrpQPsgjwhZZj2r6nBcAPRcG5wTYPS3_vHtvB2R2G8LvM1iC0jXwGdOwBM8G0trD0mNb2Z5mIpLOQcU_mybq7p9QLHruCjog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/102293" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102292">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdCWIlTB4XQY9jExEOaiSi_fUxAPj4I9gjDET0naZL2hsQbqeesyvxAxWsfnqPoqU1kkmakr3FNBpP_-Z5HimkGz56Prz8Vo7IHi-UX1eF3i2xpGpIrOthkRGZ3tinubDQQLI-0-AByQBxIPC8ygHp3hMhnFtfsxs8dzqOC7llzmanHi4yaDRW1CWUtHqto-MWatbouex5YsWhO7hR9N7Es_7PAka9xnqoEKw0xV0a-_yd7LY9XIKbvHljWaMSMbm-mVYlK3nvUWzcFB6PVs9fuxoQ6LlfmZHRxTrNNKLkj5jfZdfrLNZ9UqmYrJ0LPRZEfys-hr24XAyGavfPAeBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری از پپه آلوارز: مارک بلینگهام (پدر جود بلینگهام) در پایان فصل گذشته با باشگاه رئال مادرید در مورد جدایی پسرش صحبت کرد او دلیل این صحبت رو اختلاف نظر در مسائل ورزشی اعلام کرده بود.
باشگاه اعلام کرده است که جدایی او امکان‌پذیر نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102292" target="_blank">📅 00:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102291">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCP-4Bdw4WjKlFF789tWYonCquK724PUVSVnQ9X7oLzQZ4zci_CUCpeXt71mZpYIN_tRXrqbwjd6YSYXrnjgBq4E1TUVZn3GLGzwaxqKgMaQ0aRX9J26wC0FmzifJ-cbg4TMEtI4MN4QzVxFazfQdUGx5EuZxZhGhhgn0ojBefG27vsGqRkph62TsAf26lLFKfUAlCN7kmLlFs3so8gglYysun0ynAQTIU7yX-cr0CvY0-nwD2tEamKM3-NGgyg9Qpfsk1suQbIs-0kcYn5IdGw3pz8gYoFJGDqTNNyQW0FkZzhpnAZzyZuL69z_FRdpLI2LB2nD3A7BzArrFgDayA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇹
فوری از شبکه DAZN ایتالیا:
استراماچونی از ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی ۲۰۳۰ پیشنهاد رسمی دریافت کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/102291" target="_blank">📅 23:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102290">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocfEwMW4TqlUaVezXH4e3E-AICYh0LCfk9AC-Y5Xkj0ZEbEZiHY2Rbm_R0GUS4qed_PNUmqlBwSiIzo2WppVBjLVcPs_fX1eY3YjxIyBuHCmi2ZBPSQBT9Y-4y_rV6DZR60elHXFZIlqNH70ViVz10e-RDJgZ3SE0qMszE3JCVh4aYGpT4zzTccxT1VDbFnX5IyGRHeBszFWVoWC-f7pVVx9ZQpzsS1WpfVww_0KId_mfQU1tDsJaoQjEMHkL5xPZoBgDhxdQcyu0pJTIJIRuxS2yrawy7XjmGdDNNPX6inOpqqSqCtORNgNHaEJvPU7BB0af3nvfxf0IG7DCPvfaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فرمین:
این بدترین تابستون زندگیم بود! همه چیز داشت خوب پیش میرفت که مصدوم شدم، اوایل جام جهانی نمیتونستم بازی هارو ببینم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/102290" target="_blank">📅 23:01 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
