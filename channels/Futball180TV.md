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
<img src="https://cdn5.telesco.pe/file/JkBV9mzjV0n9C3fXO9niaoF-EThvUJAf-izogvPo62qWN5ACUwmvBQruXYpdaXvU2uWGQWjZD9_-l1GqLP6ULrwej-KlEmAC9UPWWtB32t-HhSvrm7klRVE8ZVo3Svi5UFzUxioQqiWcfaP7pVYAiKPYVQJS1NUDzB16TpoW4t-X0yPHSmN0CLfucMUz5SvV6fR0kyA4D9SmOuzuqPLa7I20jmx0XQP4CDpGybqKns4kHDbK_AR2xW0ANSsBGRpBUDXq645M2Setl_KAijGaoErbpHX0LXuD6yUpWdyUGGxptAgW2PCSZ_BPPl_0x_qCkza3qpQlnCFCigQEmgK19Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 395K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 03:46:48</div>
<hr>

<div class="tg-post" id="msg-107578">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/Futball180TV/107578" target="_blank">📅 01:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107577">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 611 · <a href="https://t.me/Futball180TV/107577" target="_blank">📅 01:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107576">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/107576" target="_blank">📅 01:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107575">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j8n-sEx5oYHQWLjVnfV7HlMbqGZeYRu5varFC8N4GsvpRfac6-KjTYzKL15Krd3SnbnlhodF8mmZ37FkXFx7bEu5b0H79pXCqcZcjv4KKVYAIUrIHgjRSIWB3z7nRmJCxZO7rywzYkD331QtCiUTZLK4XcneE-KjXWFB3EMYQShKCn9AS3X7oufB0bmqUQJZk4xmcBEGD6FUMwHyoxF6-xJu43BUTPOre-FrDs6Hs5G5_ON8YHL0cN1FWmZqZH-rF9JZcrViRV047lrh0vUAf0-yXUBdm9j5id41W_xCWCevonNZYn78ccfyc9rj0OXsBFS8ZJDpiihSv1gXKWiLKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇦🇷
ترکیب تیم‌ملی آرژانتین مقابل بولیوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/Futball180TV/107575" target="_blank">📅 01:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107574">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc7236f39a.mp4?token=QqrpJwYzq9zS6j-mHTZUHaGanzyHur8blqDwoVrhEJrMiSPg7oRHdhmfE8pm9OMUrGw2WO1obZeXszdGiejx4eAvOiQhsDqjeC6ySuyKtQvuKXe7nZA9QUcABE4OtmFAosqE4zxZtziBY6sVh7oc_uOapWtML60yYMaTFIgGo3GxTmwnijH69CgFZfCuIZtyCMGQkfubTlW31NCEfR0W30bvKvEc6fKOcJWLuNYPhXvJrb9Rw5xx8gprlJgu2iOrxbeQd0T4MUj12M4mI30E3SnEcqGwsnINkqUJzcJwEdw_iBQmMjpE7wLx29PJkxAIOJB4W1EkcATXu5mFyZib5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc7236f39a.mp4?token=QqrpJwYzq9zS6j-mHTZUHaGanzyHur8blqDwoVrhEJrMiSPg7oRHdhmfE8pm9OMUrGw2WO1obZeXszdGiejx4eAvOiQhsDqjeC6ySuyKtQvuKXe7nZA9QUcABE4OtmFAosqE4zxZtziBY6sVh7oc_uOapWtML60yYMaTFIgGo3GxTmwnijH69CgFZfCuIZtyCMGQkfubTlW31NCEfR0W30bvKvEc6fKOcJWLuNYPhXvJrb9Rw5xx8gprlJgu2iOrxbeQd0T4MUj12M4mI30E3SnEcqGwsnINkqUJzcJwEdw_iBQmMjpE7wLx29PJkxAIOJB4W1EkcATXu5mFyZib5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✔️
🇮🇷
محمد خلیفه گلر فعلی آلومینیوم: قراردادم با استقلال امضا شده و نیم فصل به این تیم می‌روم. خودم هم دوست دارم در استقلال بازی کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/Futball180TV/107574" target="_blank">📅 00:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107573">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a45c62d9ed.mp4?token=CS1T3gVjSEIm3g4s0rnlRcgi3NThmEAs25gHHDtFTRfBUguCw5UIVxCUNIQ4Vcjc5iEPfld73KTp4xh0uHLSqYzx1byp0kFfKxR_bxXW_mFSuD98310W9jpEery5bYI1WGHZdIFGpee4pqlEB274Z_5n8qs98DsAhrzRly45fmoffAg4tLxI0EARfi_LTNMi0Us1Lpw7X8skZfoMGa_ijT_WzF50xswtg0n9HL4lJWM4xRc8RflITbpRxzivsZZkzpizw-23eREnVR9vWHR3LSCZ29EwuWVoJcQeyP2ySTLVc7TWrB1gZGHTiT8L4FIyn6-fde457Y3vncZuOGLJwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a45c62d9ed.mp4?token=CS1T3gVjSEIm3g4s0rnlRcgi3NThmEAs25gHHDtFTRfBUguCw5UIVxCUNIQ4Vcjc5iEPfld73KTp4xh0uHLSqYzx1byp0kFfKxR_bxXW_mFSuD98310W9jpEery5bYI1WGHZdIFGpee4pqlEB274Z_5n8qs98DsAhrzRly45fmoffAg4tLxI0EARfi_LTNMi0Us1Lpw7X8skZfoMGa_ijT_WzF50xswtg0n9HL4lJWM4xRc8RflITbpRxzivsZZkzpizw-23eREnVR9vWHR3LSCZ29EwuWVoJcQeyP2ySTLVc7TWrB1gZGHTiT8L4FIyn6-fde457Y3vncZuOGLJwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرکت‌جالب بیژن‌مرتضوی در بدو‌ ورود به ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/Futball180TV/107573" target="_blank">📅 00:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107572">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCiKYC66vYSE_rq_ucRqUZAyE4XWC73gRD4h8Z_n-CCXO7JFU-09GyvJc29-oypQsJVpKrcUq02LBwIPl-fiVuE6y8FlcQpOVSyimyfY9eaMZ8kJe8LB0I-6eOSkBTYrgno5w1j0DM4-E8aluRShcBtpRZ6nOi9QaEdz8IZLFBcX5PGwPdiRyz6FCY_-sX7VmsSdvYQHgaHTGW7kVqIay4no7PAVUQGxsr2dYAXoAmOsi3zHST2gGIcJ0BTQ3Pg7tlloqmjTHVTVnG6CcxxrXS0Rr1otrNjXnHygQwFKbaxwxqmkqOyCgKCbDARKI7A-pRZwdQaa61H4N6gUr11PYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
👤
رامین‌رضاییان از ناحیه عضله زیر شکم دچار مصدومیت شده و احتمالا برای مدتی از میادین دور خواهد بود.‌ وضعیت نهایی این بازیکن تا فردا مشخص می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/Futball180TV/107572" target="_blank">📅 00:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107571">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db10a352e4.mp4?token=vdnb7zDUOaykO9CNqWHaEBO0182TfhmCZFV9lT9LmvhI3Kt8Wa4XpXEQhR_wOhgD47mIhaopIoCfs2fW8ZNoF95CuCSddpDxxRb8w4m5poiEtuFpQVs17BqFYExxhfgKi0w5-STMXuHt8TwmuoI2BIq5gk4knJquF2i7aSUkjQUcBw6cYOGOzwUblL7gL_zZba5MF7nv6ahFUSAbuDSqz13KqZcYnUw88d7PcNuLerAuwBobU-gDypSqTBsxB15R_ZCG9HVVPpOkl-WjrgUGtoBdSZ8Z4d8LtdkwzwWVANXWiDrpgrguWAFOJmWmBe5tIqBInpx3byPRQT2QNK5zxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db10a352e4.mp4?token=vdnb7zDUOaykO9CNqWHaEBO0182TfhmCZFV9lT9LmvhI3Kt8Wa4XpXEQhR_wOhgD47mIhaopIoCfs2fW8ZNoF95CuCSddpDxxRb8w4m5poiEtuFpQVs17BqFYExxhfgKi0w5-STMXuHt8TwmuoI2BIq5gk4knJquF2i7aSUkjQUcBw6cYOGOzwUblL7gL_zZba5MF7nv6ahFUSAbuDSqz13KqZcYnUw88d7PcNuLerAuwBobU-gDypSqTBsxB15R_ZCG9HVVPpOkl-WjrgUGtoBdSZ8Z4d8LtdkwzwWVANXWiDrpgrguWAFOJmWmBe5tIqBInpx3byPRQT2QNK5zxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
آهنگ جدید محمدرضا گلزار منتشر شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/107571" target="_blank">📅 00:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107570">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8hiCoUOdxAeQ01I40qLHBdvWMAl7-30raDhymzkcOXuDnGC6NMBTnmNbq-dhaORwCDlLK-i5LOUmI4jZnjy8evGTO29CR4Ax5DjxMIHErjYG0Mu9vJZIhSROvyKMcvKoXH44ElBOY7FvxoF0XxPyrMKQRxNuKjCxN3StZfdxo0A6SLBYgldi9ilZ6cHrGqCvOnq2kdLtbfCYx1AGhAoyiZ_b1wzWSbE72whAZEqSy3wUAeketDeHpnZHiO_Vbbqen-cI5bSWl0EYVQqP-y5oNGO0ec1RA5lJ-ukb_vFEv3KGJkCE6P12EEj03nMezlKooBfFF7PbEm-sjxExmj0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇵🇹
#فوری از آبولا پرتغال: تا زمان حضور ژسوس روی نیمکت، بازگشت رونالدو به تیم‌ملی غیرممکنه و باید بزودی شاهد مراسم خداحافظی برای این اسطوره باشیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/107570" target="_blank">📅 23:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107569">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ba-q87WCTd-lahFPW1xPnlDNqW4IkIwRM-_8XGgZ8_haA_qUl8QwJWUz__YB7_y9MuipjP8LHEydr_KJOGyjR2ZwKKJmo3YkED0bRwir2ONmyt9p7r-5GNKF3jM4MgWhUXzay9e1qK2bgnKzBonpYm-x_epAn--yS3T8jCa3aXmovaPUTZd9FEKRK9hZzxOd_kRdhlk77o7KoU31482HdBpU200vk4Ujd7ifyuucw-6VFEtXEBtFCHCAJLFoUiQdnlTGTQNofeG7RN4VBWTU5TLHvSILrhGVhYXRp3fULDpimxcSSiyyG1c3Xq5OA2aTxYFCfk-f8TFR899_zMdSHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚽️
امیر قلعه‌نویی: اشتباهات اخیر خود را میپذیرم اما از مردم میخواهم فرصت بدهند و مطمئن باشید که تیم‌ملی را دوباره پرقدرت خواهم ساخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107569" target="_blank">📅 23:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107568">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBOQMgSrI1F1XN3CB0imc2ZLju_tt2gJFLvYbXgwkrTnhR7y5H3EDUOOTpYn5GzJm_3dh2JNB4ZlphqIU3VuHr-d0HYfTZOrUsFq6xeZ_v8ac91hPjygDyTkJ-1DMZngSXvjO1dIms2OLsyOn4BcgA8GSBB9-eMcJSv969hFoSzMtyKY-jOKRzbsWtAGfgblu2eUDXKPIPcYa_7SYNAff5H2vZAIta375kMFlqcvsRV1XKOMTvcdCLGO74vKOrgiDxTiByvX634Yi5RQYkht6Uu24cSm72OOOMRnUG1yxhYaIi7FqCBf5WCnFGGveNjOKv98TISECbgYKL8AvA4-kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇵🇹
#فوری از آبولا پرتغال: تا زمان حضور ژسوس روی نیمکت، بازگشت رونالدو به تیم‌ملی غیرممکنه و باید بزودی شاهد مراسم خداحافظی برای این اسطوره باشیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107568" target="_blank">📅 22:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107567">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O202PReY2bOzW3RQZSpj3xoP8ArCoIZ_qkX_7zWonqLWYPgkmWedwX66bzDCOFk7dXPyoYMvmF3ujdEvwtMpYygEDNssR9afoZu8G1fKDVUOcV6R1r7RdcU3KTsfl_COhlhTwkVO7_8AA6n7l4jnphCxtd5BifCrq_n0KGRyBazOGEpqq-Cz7D7b5xYldPyihvvPyzu-hP0kwaIS_ZMPEyO1bNF1n6nVw1wFrTH3mExZA7HSmBwlSBd1xIG-axkuJ1SjDGa5aGlkOELz1HcjoKJhe1iSXTmVpUtXZ2AB0AYOfR5Dm7bPgzaa31EIJAA2rsmA4WKwxUC-V3LhBv7eww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
💣
رونالدو اعلام کرد که کمپ تیم ملی پرتغال رو ترک کرده:  بعد از کنفرانس مطبوعاتی سرمربی تیم ملی و متعاقب گفتگو با رئیس فدراسیون فوتبال پرتغال، تصمیم گرفتم کمپ تمرینی تیم ملی رو ترک کنم.  در زمان مقتضی، حقیقت رو درباره دلایلی که منجر به جدایی من از تیم ملی…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107567" target="_blank">📅 22:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107566">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuadZvIyLhanzlTjLsDQITvasQZbpdNHssRyYwzhocXlIveW9qOqajLMRtMK2qzJ2JOn9sWDk_SJBqAnA_iHl9yxDN1N36DJnTHEjFDYfbOhpf4FRU4V3MWX0ZZ5FRNOfcwYhBSWzeXHEQy5IjtFgAST4iJoQUzKP3kFOPuGJLuPxfC47ZoNRUGvZeR7wPNSHvcxiapgzJ4mLVNe9VsPudEj5173_0rwMQ8GCSeEITSRc6iIpw5x91Yzah0T96FHyusxpTqK2udbRqBWx1xahjX0RZpqCQKNJT1lBAhbxU11nAmTCEYFl6AmfIZ1uqy0BzQ5JJnaGdytGnfyWsMPhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
💣
رونالدو اعلام کرد که کمپ تیم ملی پرتغال رو ترک کرده:
بعد از کنفرانس مطبوعاتی سرمربی تیم ملی و متعاقب گفتگو با رئیس فدراسیون فوتبال پرتغال، تصمیم گرفتم کمپ تمرینی تیم ملی رو ترک کنم.
در زمان مقتضی، حقیقت رو درباره دلایلی که منجر به جدایی من از تیم ملی شد، تیمی که همیشه خودم رو وقف اون کرده بودم به همه مردم پرتغال خواهم گفت.
اکنون زمان اینه که برای پرتغال و تمام هم‌تیمی‌هام آرزوی موفقیت کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107566" target="_blank">📅 22:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107565">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpu7PZZA-vxxB0Z63gf8AkTtEqtE3BbvlYJltWg0Ei6vWpxnF9M9QISzM5MBt_aV9xh4IcJuNVhTb8AtlndhGrJd7FPcpAExvFdD0mCBcn0mxW3w4shSgGDNUlNOX_rB2t9TQeZ2rdyiX8H_xjeTnNmfB7mef3ueQlzklXdz6T2IM6rQeFQ7Cfom80-uHi9xZ7eOnRH0hZdl1QLRbBOqyDRHFPq166b02-Z2PukJNjDhfJ3gpd0em2kKRiWENzh5W86Q_kIuWaJ6KTfWOUhxcD8wwey4aXE-O2QAUO1ITewPnrUoSUZvBGqgzqHka_Kmbo1ONdLkdpy01i998uP4bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🏆
فرانس فوتبال اعلام کرد که عملکرد ابتدای این فصل در ارزیابی توپ طلا  محاسبه نخواهد شد:
🔸
دوره ارزیابی رسمی از 3 آگوست 2025 تا 19 جولای 2026 است.
🔻
هرگونه عملکردی پس از 19 جولای 2026 خارج از دوره رای‌گیری خواهد بود و برای ۲۰۲۷ اثر گذار است
👀
به عبارتی درخشش‌های ابتدای فصل یامال و هری‌کین و ... تاثیری در نتایج امسال نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107565" target="_blank">📅 21:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107564">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcE84GyTGh7bWF_nESBFBbrnnNnCZhwH-I5q_K33ngxkbhZu0lCKSGzkOqZ1AcHYLy-6TNagbSIHDsD3GsW2GWxVa79UITm5z9WWOlp95HTvkoan5xzZ9csn9d4-qERBf61eeX_kk97Bt5jwyErq_uW36z1vtf_T5ZtcdgFWvG--ttR76z4gvaylr3K49uSgLavV6LJq1Dl-THsUMHMnOYM6XIQvzYzqOz2AJt0O5zMbWezN15dgatH0uGBJs6opJuFq7GAyemulaf2X8fsoDy-ws36xQmZaReVsEFT8_ToW4yEW_OegyC4ryFplpr15YA5bp2SlKkvdRPCf3WcQ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇵🇹
ژرژ ژسوس سرمربی پرتغال: رونالدو در بازی فرداشب مقابل دانمارک بازی نخواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107564" target="_blank">📅 21:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107563">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81558f0c75.mp4?token=rA5iwnjo-Uvb1JQA7wC4Z2fvKPldU3RsIRs9_RI63tTcYMCRMgPzRIowhNarq728tJNc2DRd6wcKiCiLGfOPRQIl2-MTsJjPcpwTxL5nywIBuvWQwIiWFKkSWnOUfAVBjuEsfqa-M0ZbQDOuP91usfACQhgIV4fRdnb9FsbYw1C9fS2DSowpf4X52h9UMV9BLrmMTXNTiuFaAkTWLqHr3dglDZvyYg1D0As4A09dvB-03eSemijsPN0iFWW_cq0n5F2Q-wx6sSnwxbzeXCpn4Up8vvenWApXIHbfYSbwLY0wvp5Sk8mTTdL3Nq_RtoVa7aeYkoWWUupOGQPzxGZh0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81558f0c75.mp4?token=rA5iwnjo-Uvb1JQA7wC4Z2fvKPldU3RsIRs9_RI63tTcYMCRMgPzRIowhNarq728tJNc2DRd6wcKiCiLGfOPRQIl2-MTsJjPcpwTxL5nywIBuvWQwIiWFKkSWnOUfAVBjuEsfqa-M0ZbQDOuP91usfACQhgIV4fRdnb9FsbYw1C9fS2DSowpf4X52h9UMV9BLrmMTXNTiuFaAkTWLqHr3dglDZvyYg1D0As4A09dvB-03eSemijsPN0iFWW_cq0n5F2Q-wx6sSnwxbzeXCpn4Up8vvenWApXIHbfYSbwLY0wvp5Sk8mTTdL3Nq_RtoVa7aeYkoWWUupOGQPzxGZh0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رنگ عوض کردن سردار آزمون؛ حین جام‌جهانی خایه‌مالی عادل رو می‌کرد و الان...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107563" target="_blank">📅 20:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107562">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a3b8520f3.mp4?token=G27Y32x6QbcvqT-SjyZf86ZBAIi5bKCfUYUly5ghsvX_Tyi4Hu43GC4kECWrc8rEXEvjeyAplQFEA7sK9kwFrloezNvfk1y5-TVZLe7IsY9NBKAj9NQhHNLMUhPJj3um5twFBzm7qrXfa30yXnASRMUaxtWYYDUhD9J6BLG2-vNG04422fjYl81PdpsLoM0aSDSJB0yYd444x1Mtjv_prI0hDi01hyP46gTatQyD7dyeWPKj7b6Nm8D-9ctDMH82SZyHnsWYXLvVSLVdvGECIbBQoW_30cGYm1PqDqhF2MzT2P7P_4uhJ2xLbZVMYVLluCkuY-dtXj4fKJ2MS8ZTPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a3b8520f3.mp4?token=G27Y32x6QbcvqT-SjyZf86ZBAIi5bKCfUYUly5ghsvX_Tyi4Hu43GC4kECWrc8rEXEvjeyAplQFEA7sK9kwFrloezNvfk1y5-TVZLe7IsY9NBKAj9NQhHNLMUhPJj3um5twFBzm7qrXfa30yXnASRMUaxtWYYDUhD9J6BLG2-vNG04422fjYl81PdpsLoM0aSDSJB0yYd444x1Mtjv_prI0hDi01hyP46gTatQyD7dyeWPKj7b6Nm8D-9ctDMH82SZyHnsWYXLvVSLVdvGECIbBQoW_30cGYm1PqDqhF2MzT2P7P_4uhJ2xLbZVMYVLluCkuY-dtXj4fKJ2MS8ZTPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
دیس ژوله به قائدی و قیاسی؛ ژوله وسط برنامه زنگ زد به قیاسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107562" target="_blank">📅 19:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107561">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvaI2WKINaW2L4un51WnMaBUA_2bn8duQPyWYEy20K6H2Ay_tBDv_ip5YefpJ8Q-zbSDh050-KxvOYHiUneDl8oOVE8ci5hm4gBFBGxj-JZTuGRChE_EYQWf9VQhdEbNO8nMLZ7D5zq-xAIsfE0rZxLwrzNczkzSrNMifiFOwyOF15I-jumNNel8lGw6t0LmYsld2VWQSwgaBXNsJdR2B56upIxjI00FFeorUx_O_SS9TXN_jhhDrgXsma1APBRL7UbiyD0_dmz7fv_A4Yv3lIK8Cz4gLmpc8KBSzUmOpMWhXN440rqaA1uWsWvN9w-zpYvzqijVEs1rOF3REmpKXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇵🇹
ژرژ ژسوس سرمربی پرتغال: رونالدو در بازی فرداشب مقابل دانمارک بازی نخواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107561" target="_blank">📅 19:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107560">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d3104ad6.mp4?token=urHcw09aZGjwONGeLRcttK-qs3k5qwTWnIAens8qQrTG4vivf9oNbRuh8F_u69U6cav1lV-Nis-TQZZm5rTkGhO2jbPTEPxhBHDKvg-OGVLtSODUqWdA2bQwxBHTSHhJ972QdEMwUIWe4zFmB1cAu7PFO7OD7mpNXGgd3xm-ir1_asPObEtNHFK__E-7eBhEQ_ycPyZRbv6rgn8RliEeucjD4zvLZ_m4_1VFPRxDH-sCmC8JMfecaMOai6RMgmsuZCHvWHEbQiUers66OpSYXUIfWs_Dsy5nHlLTbVWXZz_tdOqluZ2BOPKTdepBKCfc2AmejYAEK7m_IcC1WQgSiYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d3104ad6.mp4?token=urHcw09aZGjwONGeLRcttK-qs3k5qwTWnIAens8qQrTG4vivf9oNbRuh8F_u69U6cav1lV-Nis-TQZZm5rTkGhO2jbPTEPxhBHDKvg-OGVLtSODUqWdA2bQwxBHTSHhJ972QdEMwUIWe4zFmB1cAu7PFO7OD7mpNXGgd3xm-ir1_asPObEtNHFK__E-7eBhEQ_ycPyZRbv6rgn8RliEeucjD4zvLZ_m4_1VFPRxDH-sCmC8JMfecaMOai6RMgmsuZCHvWHEbQiUers66OpSYXUIfWs_Dsy5nHlLTbVWXZz_tdOqluZ2BOPKTdepBKCfc2AmejYAEK7m_IcC1WQgSiYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های ژوله‌درباره جنجالی هوش‌مصنوعی در ارتباط با سربازی علیرضا بیرانوند
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107560" target="_blank">📅 19:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107559">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80e7cfe3bf.mp4?token=J5O2KgHwk_UJdfQB-y3oI0YhV25si0xnMbUt5leguxBd6isZQUlyXdDXRfKhPeQXFHqJJZ-J7o37NoCO0kalPecpIv6SBWqBtkpyn_zJx9Ow2yw32p_-0nrc5sSWUIpdCWMJQjfbxINTmGHtm3VNie0GOyY9DRGwe97ExwTmhDSn2M84u6NFeOh1UAwF254AvXj4g3rSqPYJ5jSOpylh5NM4w9m0SbF9LUT9dMMlztf12gxWWIrnjZVx7wa58iqeZbIlDeCe9mN6FVuXJQXuynIZL05Io1XOu53Z7t8AtCut0FyJrVfoHeDKzHlI5N5Ng1RWyM4kq7ImTpFMAk4qUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80e7cfe3bf.mp4?token=J5O2KgHwk_UJdfQB-y3oI0YhV25si0xnMbUt5leguxBd6isZQUlyXdDXRfKhPeQXFHqJJZ-J7o37NoCO0kalPecpIv6SBWqBtkpyn_zJx9Ow2yw32p_-0nrc5sSWUIpdCWMJQjfbxINTmGHtm3VNie0GOyY9DRGwe97ExwTmhDSn2M84u6NFeOh1UAwF254AvXj4g3rSqPYJ5jSOpylh5NM4w9m0SbF9LUT9dMMlztf12gxWWIrnjZVx7wa58iqeZbIlDeCe9mN6FVuXJQXuynIZL05Io1XOu53Z7t8AtCut0FyJrVfoHeDKzHlI5N5Ng1RWyM4kq7ImTpFMAk4qUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🇮🇷
شهریار مغانلو بازیکن تراکتور: زندگی کردن خیلی سخته؛ مردم نمی‌تونن خرید کنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107559" target="_blank">📅 17:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107558">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107558" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107558" target="_blank">📅 17:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107557">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugEbri3wXs9opFf_32OLeF7cLtciq-7ZBuVFWYYz6tBSWt7lCTq36rJ9wwfa5PXSBmlxt5tKiWIu8wkTQQVb1bbpu75QYBKCn5nByBaosQCswCgW5m1CBhMhI_MsC10J66MVb6RRSYG-A8CgnE9HSFwyxNBGLcpe_bSZlO-ondP6w_Z53TpViSCDKgSOOtFr8_Zlp5aMTdwqz0T2PmRPJoenW9AjsTEoVYhJKAu89iq2cNgUR3lz4uBaeDk2CMzlwSE90CXc90rZsxYf0YUTLLWqZ46ImFdgZonk8sG-WSS8-8fa3oP4qifNGsR4GfAemm1eTDDY-KfKgluiJ9bqjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107557" target="_blank">📅 17:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107556">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‼️
آخرین وضعیت ورزشگاه مخروبه آزادی تهران!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107556" target="_blank">📅 17:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107555">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2b8aa84ba.mp4?token=LtmYLoDFXnFfNyN9unfkp4uiG5NzUz2dscn6v1qk-WXIKA7ZFDiqrcHLzEcqqQvYFJUEZ8luENMmWHqRTBF04rQ_be7vYaCtE0ur_Y8Wn3ylHV5vN07BBTdRdWOrTjn_vLBseLLqxNMiKS-f54dL8ndQxdcUdHUGLCvUq7ny1lY1vJ6pB0bBfzGo9Sx3hdkUc6itLGNZgf9g1vRfPwm37JAyQvbFeINmg8ohiBYkjnV0RI-cV3S1l0bVeIA6c6o1yRkGxWFMLLBgZt6Dm1-MSE1tZtsN9mB7oeGJergbJnZD7ZOtChxWpEOp0CctwzH24rfKLVmPH_DoIEWTJ_Kf8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2b8aa84ba.mp4?token=LtmYLoDFXnFfNyN9unfkp4uiG5NzUz2dscn6v1qk-WXIKA7ZFDiqrcHLzEcqqQvYFJUEZ8luENMmWHqRTBF04rQ_be7vYaCtE0ur_Y8Wn3ylHV5vN07BBTdRdWOrTjn_vLBseLLqxNMiKS-f54dL8ndQxdcUdHUGLCvUq7ny1lY1vJ6pB0bBfzGo9Sx3hdkUc6itLGNZgf9g1vRfPwm37JAyQvbFeINmg8ohiBYkjnV0RI-cV3S1l0bVeIA6c6o1yRkGxWFMLLBgZt6Dm1-MSE1tZtsN9mB7oeGJergbJnZD7ZOtChxWpEOp0CctwzH24rfKLVmPH_DoIEWTJ_Kf8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
دیس‌سنگین ژوله به حرکت کنعانی‌زادگان روی گردن عارف‌آقاسی در بازی دربی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107555" target="_blank">📅 17:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107554">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71c4e91ce5.mp4?token=Bh9gt6kUfnh-El4rSsB0U_NvvvdpNqjz6uHMpLKXlw9L_HkcEgLJ9uy8WyLjO6It1KaVC4eA0tcPTUl7-uvYvPw_ar7pV_BhPpIYUZdZ0JWts6ElMTo6sGlnqoB2k-6T-DobKlug1qnI570lRdy78hC1UdvmoWXKprzI05e2UF3vIajo88D90TFv6BOqt2-02mYfAmgf5cSDaLZ1png5UZMSJ919Xmn3I7fmReMO64pWeckfdNn0oiUB6IeaPopF1-3vYz2SyG7XE9hry7bwtpg5Fm0U55frdiztCSw085QfDjYiC2rDTdeUXkvbqqhr0H77jckSZepGp-zR-QRlUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71c4e91ce5.mp4?token=Bh9gt6kUfnh-El4rSsB0U_NvvvdpNqjz6uHMpLKXlw9L_HkcEgLJ9uy8WyLjO6It1KaVC4eA0tcPTUl7-uvYvPw_ar7pV_BhPpIYUZdZ0JWts6ElMTo6sGlnqoB2k-6T-DobKlug1qnI570lRdy78hC1UdvmoWXKprzI05e2UF3vIajo88D90TFv6BOqt2-02mYfAmgf5cSDaLZ1png5UZMSJ919Xmn3I7fmReMO64pWeckfdNn0oiUB6IeaPopF1-3vYz2SyG7XE9hry7bwtpg5Fm0U55frdiztCSw085QfDjYiC2rDTdeUXkvbqqhr0H77jckSZepGp-zR-QRlUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
واکنش‌ ابوطالب به صحبت‌های مسخره حسین عبدی پس از شکست ایران مقابل کره‌شمالی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107554" target="_blank">📅 16:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107553">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d381cb7a98.mp4?token=Ew5VT77OUNgncY5OHEmTJvK-ykLKRwzsS4IrjLnC0DFoV1vBKqUcvk3TKN3Q_RKE4MdJmXESVo0CJ8COTzbVOSKJ4vbFLssDdVwcmn_WEUgAGmCF3gLQWUNBwkrb35qWUbgHE4UQfNG0ovFtofQYwpv0GZSzEGV5I3MJCJ6ktdboKXIkz0_FHbSI4dnEVpo_DT9y4bPzbLX88f00_WeZpqSAmxia0Q3HOSTkdWPmhOYm54BsdH2mpOIRF7uq0BVxh1D5-lm4ApgtHbK01to587S0dHxqyvqfVxf_cB7P1a-e7b2Twf9FO5PI4WbTjqCXJVjm3WTLPCZYxGVzda8BUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d381cb7a98.mp4?token=Ew5VT77OUNgncY5OHEmTJvK-ykLKRwzsS4IrjLnC0DFoV1vBKqUcvk3TKN3Q_RKE4MdJmXESVo0CJ8COTzbVOSKJ4vbFLssDdVwcmn_WEUgAGmCF3gLQWUNBwkrb35qWUbgHE4UQfNG0ovFtofQYwpv0GZSzEGV5I3MJCJ6ktdboKXIkz0_FHbSI4dnEVpo_DT9y4bPzbLX88f00_WeZpqSAmxia0Q3HOSTkdWPmhOYm54BsdH2mpOIRF7uq0BVxh1D5-lm4ApgtHbK01to587S0dHxqyvqfVxf_cB7P1a-e7b2Twf9FO5PI4WbTjqCXJVjm3WTLPCZYxGVzda8BUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
همسر بیژن مرتضوی خبر از بازگشت این شخص به ایران را دقایقی‌پیش اعلام کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107553" target="_blank">📅 16:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107552">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a63edbd38.mp4?token=mp21hRhfOFYgbXEzPOo1lfe9pcRncyMiOD4BoEwnFEOlWdYSapjzhbMzRkrsYlQFv8B54MCtFdgVRAOvvkr567uX_lGxGSN2iYPAx6t_If4y7UloDtIj_2ExOPOltdtKQu71QJSPhMfRImsn34tX_kt0g9PB3XgkE2KWdKO0aYYhXHWDGoHMFFiL7RMfid-grVHpx7ZFNehGBSY6QLP96eMnxvWr8LpPJJNvwVnmaRps8Hcxz_WnaumQjG918nftVJ1Sts7nv4n1yqG7K4R-LcQGDxPXpliQY1emgfMGQ97robykakTJ2fNwBiA0RDptZ5iJiW50qdwc8Coo2GwDhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a63edbd38.mp4?token=mp21hRhfOFYgbXEzPOo1lfe9pcRncyMiOD4BoEwnFEOlWdYSapjzhbMzRkrsYlQFv8B54MCtFdgVRAOvvkr567uX_lGxGSN2iYPAx6t_If4y7UloDtIj_2ExOPOltdtKQu71QJSPhMfRImsn34tX_kt0g9PB3XgkE2KWdKO0aYYhXHWDGoHMFFiL7RMfid-grVHpx7ZFNehGBSY6QLP96eMnxvWr8LpPJJNvwVnmaRps8Hcxz_WnaumQjG918nftVJ1Sts7nv4n1yqG7K4R-LcQGDxPXpliQY1emgfMGQ97robykakTJ2fNwBiA0RDptZ5iJiW50qdwc8Coo2GwDhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
قلعه‌نویی میدونه ترند چیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107552" target="_blank">📅 16:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107551">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlQA2MEE2TuktWdZ-T8fpvI0J_6UxWt4OKSpsDI_qbqY1_mNlvhTlqTuV60X3wxTgnTcGqTbwuPHnSvJULv1CJY5or5IIaeHVDXA7Qg9Z0aaSNCgnMS_Ivs3yrzfPLzlsbWQecOQ6lf1o6kUGLCAxJ9LOxgVVFnpOdyCmXIbGYxL5mbjhRQZZVAtyPNGiVntz1w9OnOaNI9RgskfqzVDtLVTo0QN0_ne3rP6fRIJ7a04QvKsx09-DYhnPvnhEaVSnRXshIpojRjCFAx6cu2WdJc8smIZYwBwtDwUuxenzTwZs16DWDhU0DpUkOZKTTe4z3RxPzf5vS1BAPsl0ot88Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
⚽️
برای اولین بار از زمان رقابت‌های یورو 2008، کریستیانو رونالدو در تمام طول یک مسابقه، نیمکت نشین بود و حتی یک دقیقه هم برای پرتغال بازی نکرد.
🇵🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107551" target="_blank">📅 15:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107550">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0610e8bf78.mp4?token=W299f2woqk-JuW8xK-IWuez5PbcHpUwTDtFq_x-6sYrxu2603owmZF3nteJgIRK7mbYCwVw5npu8UGIdmAQQpK9XN873eSmlV5U1TGQqP2mkDLciOynWEJueYkwuwi5VOGMKzP0lZXzwd8FUzQqApVHYeU9iP5JDHlhch8wiop3SzM3uIeLyRBCQ6BLCOJUL0ivG_y15Lc5t4qq5BmyVbJhN0tsqv5tMS_2Qj_H5jQT9IlMnNawgSmV8HIFzAcNqEi4fSdBZ3qKD2f6OCOXTqsau2cf3hRtHCe7Yj_5_essrCE7pvPK7WpPF-GOpM0g9-XtqAr3TP4zqdTzonGptzYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0610e8bf78.mp4?token=W299f2woqk-JuW8xK-IWuez5PbcHpUwTDtFq_x-6sYrxu2603owmZF3nteJgIRK7mbYCwVw5npu8UGIdmAQQpK9XN873eSmlV5U1TGQqP2mkDLciOynWEJueYkwuwi5VOGMKzP0lZXzwd8FUzQqApVHYeU9iP5JDHlhch8wiop3SzM3uIeLyRBCQ6BLCOJUL0ivG_y15Lc5t4qq5BmyVbJhN0tsqv5tMS_2Qj_H5jQT9IlMnNawgSmV8HIFzAcNqEi4fSdBZ3qKD2f6OCOXTqsau2cf3hRtHCe7Yj_5_essrCE7pvPK7WpPF-GOpM0g9-XtqAr3TP4zqdTzonGptzYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🙂
دیس امیرمهدی ژوله به جنجال خداداد عزیزی نسبت به پاهای پرانتزی امید عالیشاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107550" target="_blank">📅 15:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107549">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a12598c8c6.mp4?token=o3o3lPKreoRlgn313s1JXWB06w1x9KwJZ6RCVqLrvQQPV0DTq_vMxbsqMnkzwQ-JeNjo_yr4zW3A9bjz6ThS-i4kLPFWTM-6piuEBSLqf5QjZB8hgGvjTaUwi_SL2BIsTMURFtPGE4JqIdBrhOvhYSz2fMJxbCXvKqMYgOqQcFYb6g_sbhvsZwLp_s30aAsufkEo71vCQm_jw-ClzexL3UkI3xtFyThm4QVRxKB6LTdhAkq5EcvhNyaiBJgrXOOnIpFMoHEXfaJuuFaVez-DmFb3wylW9hbZd2QAAV6x-LvSHy4_0gp3CgyM_I8rZ5vofWoR557Rfpz4M1xUyQ9OBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a12598c8c6.mp4?token=o3o3lPKreoRlgn313s1JXWB06w1x9KwJZ6RCVqLrvQQPV0DTq_vMxbsqMnkzwQ-JeNjo_yr4zW3A9bjz6ThS-i4kLPFWTM-6piuEBSLqf5QjZB8hgGvjTaUwi_SL2BIsTMURFtPGE4JqIdBrhOvhYSz2fMJxbCXvKqMYgOqQcFYb6g_sbhvsZwLp_s30aAsufkEo71vCQm_jw-ClzexL3UkI3xtFyThm4QVRxKB6LTdhAkq5EcvhNyaiBJgrXOOnIpFMoHEXfaJuuFaVez-DmFb3wylW9hbZd2QAAV6x-LvSHy4_0gp3CgyM_I8rZ5vofWoR557Rfpz4M1xUyQ9OBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
‼️
جام جهانیه یا مسابقه‌ی انتخاب کراش جهانی؟ کنایه ابوطالب به لیست نفرات قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107549" target="_blank">📅 14:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107548">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c539f4e6f.mp4?token=FnNPJ0CEb9iIQRAEiC5o7qjUjt7SaBc8yrdN0ywrVB8h7CKFr-rGT6eFMlrwGRFxShzP-WoD5ysIgOCCX6W_iA0sjvi9SNF63sI9ie4ru83wARU0ma069du5nb8RNA10KeWGhGzg6-01wlPw2Uy6lsodwa2EXr9wIPlZIjnNqevIehOCkI4O-gQA8qlUvNVOGAJDyZ8MyKaKUx_yN2X1DVL8afrVBVKPl9O4Mb21DxTojsAps901tyWciJyL8NFtsbA-JUsQf87e5cJ7CtwIfmMV8M8M2oJuy8leWWHO1nr2qNtMB0AiSIpOq1bgepTbT6-WG-2rpRP7sZfcvpWzGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c539f4e6f.mp4?token=FnNPJ0CEb9iIQRAEiC5o7qjUjt7SaBc8yrdN0ywrVB8h7CKFr-rGT6eFMlrwGRFxShzP-WoD5ysIgOCCX6W_iA0sjvi9SNF63sI9ie4ru83wARU0ma069du5nb8RNA10KeWGhGzg6-01wlPw2Uy6lsodwa2EXr9wIPlZIjnNqevIehOCkI4O-gQA8qlUvNVOGAJDyZ8MyKaKUx_yN2X1DVL8afrVBVKPl9O4Mb21DxTojsAps901tyWciJyL8NFtsbA-JUsQf87e5cJ7CtwIfmMV8M8M2oJuy8leWWHO1nr2qNtMB0AiSIpOq1bgepTbT6-WG-2rpRP7sZfcvpWzGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
پاسخ ابوطالب به انتقادها از برنامه‌فان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107548" target="_blank">📅 14:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107547">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc4546c8d.mp4?token=BKMOXOQcmdpBAxN42gsWAUOUySCXbRHZpzxxe08Uo-y94-uXl2DFz0igQ6_UHxsF1PQHnjh7gI0Gnt9C8WlAIc-A5hlejheVCh32tywctQWusxpYQSf9aVFqynz-4RC_frIjQPUosWtGeSH2jaH0GCUf55P-KJWGPgbt_UQGkNxkHd3ysT6DhSdPjvvQlsqU-6jasFWRAeEQGSFWLEpZH1MOdkrOcJBDlIoYfIG3PbQQZWWA44uGhvROotG4R5AqAiMPzN1ru49oEwVOzeAp5yHqMPoO8AEjnauC18svrCzweVYy2vQM-R3Q71MRrjMMw5O2Xiu2hWNssPXr9Inhh038qTZMwf6pR4n8aIjZHOxnxZ1TANXSqZ3nH3UC_SaavDar2Kam9BHmn8PwDI0MnmdGeUDcuggKgye_M56F-2dkQDoERhpL-Kce3gDQG5XMzTKBraQ3o6lAL9mGcYvdDp61P3o92PDGm2FI3eEwbM-b58PtWG11xnfsnC5CP0ApHnUCtCeAz4Yu-1LI9D73_nb1OgPX3mdIW86_OO5A4eWaWhryzuhEozM7qkWAbUeTE6UIX5DgqBTgwfEGYcevi9euWGQEa5FEIlaWxlasafKrdVe5VrCRDbZ6KTg-3qwMvgm_jFqaORsljH6nJ_XDHWF59J2biUt_q2MpCRZPmgE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc4546c8d.mp4?token=BKMOXOQcmdpBAxN42gsWAUOUySCXbRHZpzxxe08Uo-y94-uXl2DFz0igQ6_UHxsF1PQHnjh7gI0Gnt9C8WlAIc-A5hlejheVCh32tywctQWusxpYQSf9aVFqynz-4RC_frIjQPUosWtGeSH2jaH0GCUf55P-KJWGPgbt_UQGkNxkHd3ysT6DhSdPjvvQlsqU-6jasFWRAeEQGSFWLEpZH1MOdkrOcJBDlIoYfIG3PbQQZWWA44uGhvROotG4R5AqAiMPzN1ru49oEwVOzeAp5yHqMPoO8AEjnauC18svrCzweVYy2vQM-R3Q71MRrjMMw5O2Xiu2hWNssPXr9Inhh038qTZMwf6pR4n8aIjZHOxnxZ1TANXSqZ3nH3UC_SaavDar2Kam9BHmn8PwDI0MnmdGeUDcuggKgye_M56F-2dkQDoERhpL-Kce3gDQG5XMzTKBraQ3o6lAL9mGcYvdDp61P3o92PDGm2FI3eEwbM-b58PtWG11xnfsnC5CP0ApHnUCtCeAz4Yu-1LI9D73_nb1OgPX3mdIW86_OO5A4eWaWhryzuhEozM7qkWAbUeTE6UIX5DgqBTgwfEGYcevi9euWGQEa5FEIlaWxlasafKrdVe5VrCRDbZ6KTg-3qwMvgm_jFqaORsljH6nJ_XDHWF59J2biUt_q2MpCRZPmgE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آنالیز بازی انگلیس مقابل اسپانیا که حاوی نکات بسیار دیدنی برای علاقه‌مندان به فوتباله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107547" target="_blank">📅 14:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107546">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
رونمایی فدراسیون از معیارهای تعیین رده‌بندی و قهرمان در صورت لغو فصل:
🔻
۱-در صورت برگزاری حداقل 75 درصد مسابقات رده بندی بر اساس جدول موجود.
🔻
۲- در صورت برگزاری کمتر از 75 درصد رده بندی بر اساس میانگین امتیاز در هر مسابقه.
🔻
۳- در صورت اختلاف فاحش تعداد بازی‌ها استفاده از میانگین امتیاز به همراه تفاضل گل و نتایج رودررو.
🔹
تبصره: سازمان لیگ می‌تواند با تصویب هیئت رئیسه روش عادلانه‌تری را جایگزین کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107546" target="_blank">📅 13:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107545">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95a2f6b70b.mp4?token=Gl43g-iu7I7EVZbEeewxHfKJ8d_30UYkSxf8Jxz4yfHrAJuz0pConFNEoCAi4pqVRjy_5BRpBZrKvpq4_BFMC5PCLMMR8JYGtNQCwoDBIfvv1MubcyEj2RnAU20BdJ_AsG2E1kt58SbUdJJk5giBt3lCYxhvxsaxmA9BAuDhZQYOhTH694440C75KfWBej5x1ZZC-QgmjGPKC_6BMIUTIPmXtunHeNQybDPYiI18Kz8D0o3q_iCkeLn0ei3ncU_MVMD2Te02IcPq_hcjE97HEH0BAAjVZcEWBAo07eMUt3YWDgMqWnuGSgaylWOmvZZ6FAVwjJl4SDEaKqPkxQ8ZFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95a2f6b70b.mp4?token=Gl43g-iu7I7EVZbEeewxHfKJ8d_30UYkSxf8Jxz4yfHrAJuz0pConFNEoCAi4pqVRjy_5BRpBZrKvpq4_BFMC5PCLMMR8JYGtNQCwoDBIfvv1MubcyEj2RnAU20BdJ_AsG2E1kt58SbUdJJk5giBt3lCYxhvxsaxmA9BAuDhZQYOhTH694440C75KfWBej5x1ZZC-QgmjGPKC_6BMIUTIPmXtunHeNQybDPYiI18Kz8D0o3q_iCkeLn0ei3ncU_MVMD2Te02IcPq_hcjE97HEH0BAAjVZcEWBAo07eMUt3YWDgMqWnuGSgaylWOmvZZ6FAVwjJl4SDEaKqPkxQ8ZFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
تصاویری از علیرضا بیرانوند با لباس سربازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107545" target="_blank">📅 13:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107544">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6d3e68068.mp4?token=iGv_pdPokiNJ5cW7r01OHsL1EoahTpozRvyD7uxGDTeCcnHGLZLD7eI0GdTyfMpYuta3hdwB0ou5DVtH8kWJ8tJisCafAOqxnlQG1hGYEL8Z9XdAaRf99SQMqC8ZQGy6jDrVNTW9QqC_t1eopoLNERQQotNd-qvroyTkpAMpoLfdTeiB4RajijIi0rMR1x-kVW-KYTmaD9ayrBTbFp0D-ZqDE309PlSY5ub-e78L8o85Ol2R7MoMBSScoQ4JtWhdxya1uweLpsPbzO4CTvmtbfgE9Cec8b8TOE7c4dq5kBY2p9_UwtqoHOF2_0RptH46hjSXwak_BUEaxqGPiwdM7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6d3e68068.mp4?token=iGv_pdPokiNJ5cW7r01OHsL1EoahTpozRvyD7uxGDTeCcnHGLZLD7eI0GdTyfMpYuta3hdwB0ou5DVtH8kWJ8tJisCafAOqxnlQG1hGYEL8Z9XdAaRf99SQMqC8ZQGy6jDrVNTW9QqC_t1eopoLNERQQotNd-qvroyTkpAMpoLfdTeiB4RajijIi0rMR1x-kVW-KYTmaD9ayrBTbFp0D-ZqDE309PlSY5ub-e78L8o85Ol2R7MoMBSScoQ4JtWhdxya1uweLpsPbzO4CTvmtbfgE9Cec8b8TOE7c4dq5kBY2p9_UwtqoHOF2_0RptH46hjSXwak_BUEaxqGPiwdM7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚽️
توصیف امیرحسین قیاسی از امیر قلعه‌نویی: جوان‌گرایی و تاکتیک مناسب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107544" target="_blank">📅 13:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107543">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2b061cd6.mp4?token=blD_D_RqjXBBQozPivZEAPgTkGkCfiaDSfADFegOFQMWYwMuzjLvi3aHsLbn8q0Yq5o0aCArrouzAtt4UvKu-8zdPuUdpPgLyOIYZMF0EZkIEIqiVMvF5XpCWtDIB8C8KoY3otfPgJBdgnCFHNh6k41tdd0b3rec-HeZQC5U5JanldvZCYhC5FD6nMAoociXBi51zkK5LadC-67ymzxsl74DcdQhQsNXfKy5EafMGG-LgpVg0VsMIlts0nhEpzNdztmqf9WX6ZCR0qXqTOWi8bCedl-oaNDfRANKnqgWDpS9vBrTd7GB2vq1k3jQKQJ9thQeula5lCAd6vhbFx0-IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2b061cd6.mp4?token=blD_D_RqjXBBQozPivZEAPgTkGkCfiaDSfADFegOFQMWYwMuzjLvi3aHsLbn8q0Yq5o0aCArrouzAtt4UvKu-8zdPuUdpPgLyOIYZMF0EZkIEIqiVMvF5XpCWtDIB8C8KoY3otfPgJBdgnCFHNh6k41tdd0b3rec-HeZQC5U5JanldvZCYhC5FD6nMAoociXBi51zkK5LadC-67ymzxsl74DcdQhQsNXfKy5EafMGG-LgpVg0VsMIlts0nhEpzNdztmqf9WX6ZCR0qXqTOWi8bCedl-oaNDfRANKnqgWDpS9vBrTd7GB2vq1k3jQKQJ9thQeula5lCAd6vhbFx0-IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های امیرحسین‌قیاسی درباره سفارش غذا ۶۰ میلیون تومانی برای مهران‌مدیری!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107543" target="_blank">📅 13:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107542">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9a4a5cb83.mp4?token=MKjCUK-Ky7Qsj0P3VZqgnMTs0Vo9727tDGKtwlMHEJnHMhOT8tP_VZpy2P9OHBN3LZAX7Vj-tWnjhdukp7OFe3qLNDCfOGOHSMtyt64yCuJSMY2piiezcIOtI2Z0MoKZMHxze49IpOkcOkeKTD1qkr3ljwU9U69SW8v2tfHus5W-npRBqGlbvSM8xhE6L2BVJFbEII6DH5-8Q0gbLwZ73zakAw5xcYvwHBHthl9nSN7BQ3DW3sDOzAJVHnxffKTquq5n83LkZUjSYwjAnS1uXGn6NfbPa7mvzUJ2LetT4WOKngtSGDd6Y1sLRs0WpLs5JlzmHukNyobdtPrABidmAYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9a4a5cb83.mp4?token=MKjCUK-Ky7Qsj0P3VZqgnMTs0Vo9727tDGKtwlMHEJnHMhOT8tP_VZpy2P9OHBN3LZAX7Vj-tWnjhdukp7OFe3qLNDCfOGOHSMtyt64yCuJSMY2piiezcIOtI2Z0MoKZMHxze49IpOkcOkeKTD1qkr3ljwU9U69SW8v2tfHus5W-npRBqGlbvSM8xhE6L2BVJFbEII6DH5-8Q0gbLwZ73zakAw5xcYvwHBHthl9nSN7BQ3DW3sDOzAJVHnxffKTquq5n83LkZUjSYwjAnS1uXGn6NfbPa7mvzUJ2LetT4WOKngtSGDd6Y1sLRs0WpLs5JlzmHukNyobdtPrABidmAYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
مارادونا: ۴۰ تا بازیکن از تیمای مختلف ایتالیا روی هم،  به اندازه یه توتی نمیشن!⁣
اسطوره رم ۵۰ ساله شد.
🐺
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107542" target="_blank">📅 12:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107541">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4869197932.mp4?token=DE_R-9MPfRD7z8x94Tvo3ExL49nYOeXQSfF6Zl6HvW3wGD-us04OSkX5Ks8_NgTd3Rg7JgZ5A9vR1Qb26pakUEeK_1wa-EZlozothVGusLzNvYPvf2hfhnuFEiC9tkDZIyDlhOjLnqmHN-P8pF3kHfXYH4QefEj0iMDHVso--YE0qRiGVJgNm4etlbjrUm84KHpkaFmc3lWKNFpNIxzMU8W5rTli1XZTHvCNua1GdKEO1_MxwgESDKjG6QKcmLyCkQlu6KB7nM-s4gc2Ze2fMRD8vtP-6PIOtVxRNwxYL7PZvv-NTUAG7DhD3tkRYdkb_r1SHZYsvCk6tz4Yl-yVhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4869197932.mp4?token=DE_R-9MPfRD7z8x94Tvo3ExL49nYOeXQSfF6Zl6HvW3wGD-us04OSkX5Ks8_NgTd3Rg7JgZ5A9vR1Qb26pakUEeK_1wa-EZlozothVGusLzNvYPvf2hfhnuFEiC9tkDZIyDlhOjLnqmHN-P8pF3kHfXYH4QefEj0iMDHVso--YE0qRiGVJgNm4etlbjrUm84KHpkaFmc3lWKNFpNIxzMU8W5rTli1XZTHvCNua1GdKEO1_MxwgESDKjG6QKcmLyCkQlu6KB7nM-s4gc2Ze2fMRD8vtP-6PIOtVxRNwxYL7PZvv-NTUAG7DhD3tkRYdkb_r1SHZYsvCk6tz4Yl-yVhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
🇳🇱
یک‌ماجرای جالب از فوتبال هلندی - بلژیکی!
خانواده آقای فن‌بومل، خودش، پسراش، زنش و البته پدرزنش⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107541" target="_blank">📅 12:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107540">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/621d1efcf6.mp4?token=E2Egsu5HmLkAneRcIo_n0pjIkEQ2nj0vnKjksrR2ZK0Ua-UUP0GtkvDw3GwN96CsBGNeE8nmmq-a3aOJdmnARpT_EYlj9gZlyZwx2_Q0sOhkwLKNbGuj5LxV2ZwNJalEDiAecbs3Tc--fxb3mwfZtGTyHMHhLJnOlHe_f78yCmfSYQas1kx6JrU2atVnjzGk_S8YWq6SoZhW8uwscLV02NZdp7-w1PfTGIoJgxXJF_lmJrLpqfFj5Yf2WO8xcm83wOw-S2KKwUpiOL2OL87PDQEDUB0TLkpcUBKJVvgn7cD9qSe1P9Ys31vV2YDdVD39XDtqlRY7wNyqWxK3CRtClleI_9IXgzgiGaCKS7r_ZROCiWI6wPPIuOSZRIkOASiO6ABp6CFau5b8gtUIsm0q8oqML6tLgs4tXp9Di91aSTmXrmQ-l1IcGbQjVFoAeaMNKG_--1iLUfXX5zAbHeeWdBM5RuxpM-zq3q3qkPuV1y-PvxN-aQeMNagGYRInAk-xbDRl4at5N-c2R8JHX-MVQKm6AsdjgcUwABK_CgliefZpoYWGsrBFU5XQZ_ta7jjym2fNVvNVL4twr2w1lvB4QOB-vKq-JFenKmEwioyRUn2_Y2iQCBjpJo5N-Rl657MwsCompFNdIpHxdb8aQy8QvXvLI89PI_VL21xm4uypmnE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/621d1efcf6.mp4?token=E2Egsu5HmLkAneRcIo_n0pjIkEQ2nj0vnKjksrR2ZK0Ua-UUP0GtkvDw3GwN96CsBGNeE8nmmq-a3aOJdmnARpT_EYlj9gZlyZwx2_Q0sOhkwLKNbGuj5LxV2ZwNJalEDiAecbs3Tc--fxb3mwfZtGTyHMHhLJnOlHe_f78yCmfSYQas1kx6JrU2atVnjzGk_S8YWq6SoZhW8uwscLV02NZdp7-w1PfTGIoJgxXJF_lmJrLpqfFj5Yf2WO8xcm83wOw-S2KKwUpiOL2OL87PDQEDUB0TLkpcUBKJVvgn7cD9qSe1P9Ys31vV2YDdVD39XDtqlRY7wNyqWxK3CRtClleI_9IXgzgiGaCKS7r_ZROCiWI6wPPIuOSZRIkOASiO6ABp6CFau5b8gtUIsm0q8oqML6tLgs4tXp9Di91aSTmXrmQ-l1IcGbQjVFoAeaMNKG_--1iLUfXX5zAbHeeWdBM5RuxpM-zq3q3qkPuV1y-PvxN-aQeMNagGYRInAk-xbDRl4at5N-c2R8JHX-MVQKm6AsdjgcUwABK_CgliefZpoYWGsrBFU5XQZ_ta7jjym2fNVvNVL4twr2w1lvB4QOB-vKq-JFenKmEwioyRUn2_Y2iQCBjpJo5N-Rl657MwsCompFNdIpHxdb8aQy8QvXvLI89PI_VL21xm4uypmnE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
روایت عجیب و غریب میثاقی از معافیت پزشکی برخی از فوتبالیست‌های مشهور!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107540" target="_blank">📅 11:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107539">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884ca354f5.mp4?token=Nut6BgwiG4rxH-LDhY_M24AJyNa-wXli1X18czXRVYCTOPuysOls6SyBQj2cWg6kxsxwmZgENB0I8OvlKS1hEueHT193XZauGUONsdRKyfdbeNjBvYiFOkoDT3ootY7ALygKfA6H3OpAFpDzwECVTuelhN_Z2l4nCheiv9PPzvP_Wv6NSeiNBUio2vRDKv1C53wsbwZ13MpS2mLrvN4VsjG6nmPsuHia13P66Iv_-TJrRslA_IidVeaUSzGXTNwgBN2cTaYV_1PBI3oxiOGbrLp5OBM9LjlB_KEToMvmRT3dljRkQSQoj075eSFSt3FY35geYCZY_LDzyQofMMR_vAjsKfOcKex7YjVAnMIPcmel8fibX_9Xi1sr07nDmOE2Mzvfsp9KGBevFh9Gsp_8QVVjY0emhjz1kG8I1EEJEHNznCEbfwnupTViMA9_yat9i3eImkBf-30t3EG_dJdeofpI-IyWc-zKH_2eO3x2ttYMN_K4D7bMSABz6xe312yyvSD5rquSiaIHFj0S4rvqUWdB3gYD3ZvKl07Am4lK9AGRQLir4wJyWTtmbXSGPCNYZLb5jO3uWqYHSxNuCeWbtFweJ8QyP16t_dZ5OIYqTtyG6JeRdJsdvqtFGtRq-yr06RCSP6tvZN7j-aMqOFwzdcC_zwwKSpAhFbOfXdRrEQ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884ca354f5.mp4?token=Nut6BgwiG4rxH-LDhY_M24AJyNa-wXli1X18czXRVYCTOPuysOls6SyBQj2cWg6kxsxwmZgENB0I8OvlKS1hEueHT193XZauGUONsdRKyfdbeNjBvYiFOkoDT3ootY7ALygKfA6H3OpAFpDzwECVTuelhN_Z2l4nCheiv9PPzvP_Wv6NSeiNBUio2vRDKv1C53wsbwZ13MpS2mLrvN4VsjG6nmPsuHia13P66Iv_-TJrRslA_IidVeaUSzGXTNwgBN2cTaYV_1PBI3oxiOGbrLp5OBM9LjlB_KEToMvmRT3dljRkQSQoj075eSFSt3FY35geYCZY_LDzyQofMMR_vAjsKfOcKex7YjVAnMIPcmel8fibX_9Xi1sr07nDmOE2Mzvfsp9KGBevFh9Gsp_8QVVjY0emhjz1kG8I1EEJEHNznCEbfwnupTViMA9_yat9i3eImkBf-30t3EG_dJdeofpI-IyWc-zKH_2eO3x2ttYMN_K4D7bMSABz6xe312yyvSD5rquSiaIHFj0S4rvqUWdB3gYD3ZvKl07Am4lK9AGRQLir4wJyWTtmbXSGPCNYZLb5jO3uWqYHSxNuCeWbtFweJ8QyP16t_dZ5OIYqTtyG6JeRdJsdvqtFGtRq-yr06RCSP6tvZN7j-aMqOFwzdcC_zwwKSpAhFbOfXdRrEQ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
‼️
سه‌ سال و نیم بدون رشد و تغییر در ترکیب نفرات دعوت شده توسط قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107539" target="_blank">📅 11:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107538">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4v1flw0HMJuFCj1_xrEiWi2hexRKGGDoPFChYRUCMFA7o6T-IjgCuadSs5f010FEI0OgFVmKcszS0r-ifE2mi5-ZAcqvuqtHqmvcAdTGfiWHi-8ChyPGgWNRRlctxL988jwux5b3dBx0WYRNN5yKsS9bgreS2sMrdYW4v5l7gHo3VqOG9hQzQ-0d1qT1CT7930MAjxuDosLtO1L0yKzuASzkIOTT9FbQfQuVy9HvGmfscXQmMkFxGCkqe9yGKCW8igtxuXcSZS9TCzCwyhsbt28onYaJeT_aRUXMn1ggVE66IYKal6FhTLshjt0pOQMJnWrihuFGJEe0nXrfG95Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
📊
ترکیب منتخب دور‌دوم لیگ‌ملت‌های اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107538" target="_blank">📅 11:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107537">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✔️
🎙
صحبت‌های شنیدنی رسول‌مجیدی درباره کیفیت آکادمی‌های فوتبال اسپانیا که زمینه‌ساز نسل‌سازی‌و قهرمانی در جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107537" target="_blank">📅 11:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107536">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107536" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107536" target="_blank">📅 11:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107535">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5Do6VBTnG9AIRhScEbIFGseMq7o5TlrrMIkGtMtzFLqZf6bINd4VSIexjAax1Sm2u_vVQUNydO3XKr7oEp5NERKqbXMDSqVwxHo3D3sBY-VB3KmtHhY91IU5e0326eZCcJqtm6QF-9OACRDhYz5bZT5Ly5hhDHgL9lYQaX3s7oqPsf87LbHgVbdCNb3s6xCl2CzzkQvAvdgs-QBPR9FSL7S8-71LAXFkprktzf7NiVDbJ8dipuy2JiYDvEIu1pRPTEbKrkmLq7maWFjly0LyyJhAKxaZImEg4F0AuvgJkIaBxS044U5pjyWRoL9bNZy_6ZKhmV3O-AezAmGioSSgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط ۴ روز تا انفجار در قفس
🦖
​ناتالیا سیلویا در مقابل وانگ کونگ
جنگ سرعت و تکنیک؛ چه کسی قهرمان جدید
UFC
می‌شود؟
🦖
​شانس‌ات را در
TrexBet
امتحان کن و روی قهرمانت شرط ببند!
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107535" target="_blank">📅 11:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107534">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4KJMRg4ANxC1T-ELxsle8pBuY2Of6AGnapsfsETItM84wN7PIRvsq7W2Gz7wJItLODK0vrmKTVK4e5x0kz4DKoWwsxnvRcRBdwU-NbAGPSSPUotBpQlPLwRQ6NdL_TLQvpfErPjQIL14Bk0aC5vDkUdrWz09pAgCXFq30GEpRj6zeEnyi7sZsvBRRjDoIm6XnDLB3vAH26U9BamGNivjsKDRh2CprjVZ6umrrSBCP0PqwirgVp92w4IIrM2MlT4lJItgMtnXZoKu6XWQckzjgKu7y0W9cxzeBWsk3_fZIsl6h90tlfKAqHlGuIb0APU_nuFBY3ERqINI5dWHs6Xbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇸
رومانو: رافینیا اردوی برزیل رو ترک میکنه و برای مراقبت بیشتر به بارسلونا برمیگرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107534" target="_blank">📅 10:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107533">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvU7mHQujIP-RAp66NrttRuy4_OfECvkuV4kOIdZEdliM6HQ_j718XyEisdrBSYBiLqne4eUMyan-JpQiUHbf3FRDH3j65EQq55u4bq4bpwKN0HIdYahn0wPgUVn3ryjwia9DPq2Dhoa5hJHiRhy0rtHpVDgs5AJwBL0yXYqQojtfbkWW_nu8iQV_Fb9axiCXWsWeAzZZJ1QvJ7yw0OFVI0A_AL21zKP6CweDILn_xeUdS-57NSuTWBLoIk6zeLxGI1iTnfQEWl7ewNeDjRP_PJUGyJo2bhFL6suCwx9mB5Chzc5ml_WZl2DBHl9nEvcF1PSQSpp1_cseF0HhQ7LQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
🇪🇸
اسکاتلند تنها تیمی که توانسته اسپانیا تحت هدایت دلافوئنته را در یک بازی رسمی طول ۹۰ دقیقه شکست دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107533" target="_blank">📅 10:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107532">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78614739b9.mp4?token=M4r_WRthLys_Emyp13BeMqhHIgZ9tWZZqvR7TwTFxESogv9CgWos37PbZjv3RQnc3lHa7uM2vYL91Swx4wM1W4_b9_ij0I6oS5OVRVwvp961ifgj-7pGgSpWoY_IFy_Rm1HJcaOZga26I9noCWjT3T3LJfOVDSuNyYZCXPwobQhxrij0UL2grh985ebYvS-Du2PvmLRT7g6hKM5q5cPTOWOTVzag9FDdArvfTTGYtNvuFYVHctJI-x-TXIal3AX2E1lOclq5pvkHn7aSN3pE2q0fRV9amQkrJv2v651mUFdRiSKdkzH0ehLFmjMCa72jZZzb4y8oynyn2PozwDQuQGE9CC658q4KinvzZYP4xYG2d4DYjJ5vtlhViBedOyIEYgOCxPY5GpKP2TY8Qo5lx4xo4MZ7yZ3qyNcqDR6KpEO01oJGKOGC6TYW9lkwDp_YguiO1pxhWWKZdkMPSf_e4mVG_Jep_XaT1czC2flcgXgBzcFBPw_nGhkbSeIJjV2gjeKmN22cT4y_0v5smSWWTUKeLYYAPKXEGDH-0JGSdw2DiCo4E74nd0P-oAtNuleYE0b_CeAIJL_JpxWi0D4zjWSG1krJNSKqitS6iQoYbWBCJYnno4ePlJZTz3vRPfRbNgJi2O8e46Yrr2v2mbZmpmWFgT-6YcpikpJkSfp4OH0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78614739b9.mp4?token=M4r_WRthLys_Emyp13BeMqhHIgZ9tWZZqvR7TwTFxESogv9CgWos37PbZjv3RQnc3lHa7uM2vYL91Swx4wM1W4_b9_ij0I6oS5OVRVwvp961ifgj-7pGgSpWoY_IFy_Rm1HJcaOZga26I9noCWjT3T3LJfOVDSuNyYZCXPwobQhxrij0UL2grh985ebYvS-Du2PvmLRT7g6hKM5q5cPTOWOTVzag9FDdArvfTTGYtNvuFYVHctJI-x-TXIal3AX2E1lOclq5pvkHn7aSN3pE2q0fRV9amQkrJv2v651mUFdRiSKdkzH0ehLFmjMCa72jZZzb4y8oynyn2PozwDQuQGE9CC658q4KinvzZYP4xYG2d4DYjJ5vtlhViBedOyIEYgOCxPY5GpKP2TY8Qo5lx4xo4MZ7yZ3qyNcqDR6KpEO01oJGKOGC6TYW9lkwDp_YguiO1pxhWWKZdkMPSf_e4mVG_Jep_XaT1czC2flcgXgBzcFBPw_nGhkbSeIJjV2gjeKmN22cT4y_0v5smSWWTUKeLYYAPKXEGDH-0JGSdw2DiCo4E74nd0P-oAtNuleYE0b_CeAIJL_JpxWi0D4zjWSG1krJNSKqitS6iQoYbWBCJYnno4ePlJZTz3vRPfRbNgJi2O8e46Yrr2v2mbZmpmWFgT-6YcpikpJkSfp4OH0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚪️
واکنش فردوسی‌پور به مصاحبه‌های فرمایشی و سفارشی ملی‌پوشان: سردار آزمون، با سابقه بازی برای مورینیو، وادار به گفتن چه حرف‌هایی شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107532" target="_blank">📅 10:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107531">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4481359e02.mp4?token=GKuMIfHfRqodm98K2qq_2d_CiVW0K2IG3_0MKY1tvFaFT4Nfh3Yvr9mdNYhCqV6ctVW3c9ZemTu-MiRhmFI4HAJAaZxBL3u1icG_Aeib8vqd4LEvzRGjCh8Bm6m7HZAE0tDLjTY9xUVeXwnHi4nBtNs7_GBmxSXW5HAqosqReAFxV4uCJYkYYASjISsbMxdLul_Ifi6LEl-XFCK2pV2HqKsjCMMneUsqRXqL1GIQX87_6uK2I4cPA9nDjaEL_rrIEvbrpZVRN87CieADUGgpaUlCYQfxo5jkiM2UBH-duygPa1Zbo2NLEDlCIlCfG71H5qyQSq745F9HvtCoaxHIxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4481359e02.mp4?token=GKuMIfHfRqodm98K2qq_2d_CiVW0K2IG3_0MKY1tvFaFT4Nfh3Yvr9mdNYhCqV6ctVW3c9ZemTu-MiRhmFI4HAJAaZxBL3u1icG_Aeib8vqd4LEvzRGjCh8Bm6m7HZAE0tDLjTY9xUVeXwnHi4nBtNs7_GBmxSXW5HAqosqReAFxV4uCJYkYYASjISsbMxdLul_Ifi6LEl-XFCK2pV2HqKsjCMMneUsqRXqL1GIQX87_6uK2I4cPA9nDjaEL_rrIEvbrpZVRN87CieADUGgpaUlCYQfxo5jkiM2UBH-duygPa1Zbo2NLEDlCIlCfG71H5qyQSq745F9HvtCoaxHIxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
شهریار مغانلو و دانیال‌ اسماعیلی‌فر:
🔹
چند روز پیش بیرون بودیم رفتیم یچیزی بخریم، یه نفر دیگه هم اونجا بود و خواست خرید انجام بده و پولش نرسید و رفت؛ بنده‌خدا اینقدر عزت‌نفس داشت نموند که ما واسش حساب کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107531" target="_blank">📅 09:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107530">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5234add2e9.mp4?token=umnyXm3zB7jf26HCpvNbLo9H97l0wpZmhwlE_DbRTEKwU2QSwpOA6QOo5cmLCv5YThlW0U3VQFL4ZEC2TnvUEJSBR-2TWBM_KZ5T_cESauxbjucsQLGSRedc3r4YuCZcsqbfN2pxMQA3VkqarQZEbZ3APR1KnVWtytChYJoiuFEoyALfRHPglnCz__p099mowtz1IB-21mGk0hFb_oeol4vRZ04xzUTRx7fWPTakWV8VKCvjugzVoZMIHVIt3bxO2U2lvRGDwtNF-70MDyzu7Uu2emtPv_urCenPov4ETUzxf-aqWhVL47Be2CV9rhsCiYk6bY1bUpU_UEbCl2QyAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5234add2e9.mp4?token=umnyXm3zB7jf26HCpvNbLo9H97l0wpZmhwlE_DbRTEKwU2QSwpOA6QOo5cmLCv5YThlW0U3VQFL4ZEC2TnvUEJSBR-2TWBM_KZ5T_cESauxbjucsQLGSRedc3r4YuCZcsqbfN2pxMQA3VkqarQZEbZ3APR1KnVWtytChYJoiuFEoyALfRHPglnCz__p099mowtz1IB-21mGk0hFb_oeol4vRZ04xzUTRx7fWPTakWV8VKCvjugzVoZMIHVIt3bxO2U2lvRGDwtNF-70MDyzu7Uu2emtPv_urCenPov4ETUzxf-aqWhVL47Be2CV9rhsCiYk6bY1bUpU_UEbCl2QyAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🎙
میثاقی: سردار تو وضعیت سربازیت چطوره؟ معافیت تحصیلی داری؟
‼️
سردار آزمون: نمیدونم ولی میدونم دکترای فیزیولوژی ندارم، اصلا چرا باید بتو جواب بدم به نظام وظیفه جواب میدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107530" target="_blank">📅 09:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107529">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c02612ddc0.mp4?token=icBzWfywV8vpOXt6cCyeRYRWCYDHOkTBCrqdnb3HNkL0Cp3yQYXERu9gqIvf7WGEmG9qu6B8PhQzJ6FU8TtdlMNlrQNY_N55LlM4QJKqnZefgl5Ic3kBFV760SBg6K95er2nWIQZ9pyR5ufy079-yy5j0AMR4KKUCXzuPNYkSYlO-JVRvxRW9ka_Jw-E9phkbH-yDOTBIxobVOnEecx7fWNSWDR2O3gq5pVQifM2Ak1RoAcM0LXkPwr9MnaO08W8kKH0t2yzfSSLlV1kc6rxMeC0MBYNc4oob5ibCeXiU50oME-L7bGxPizHJOsGlU94O76cD5RLUxd7UHSuVsuNZj34ip96DACarbsE_i9FcCphPzBtArOFu7g1PtOSavI_DHugs8NdneAUAxSEGApKKY3scSG89nph-k4sGf9Q-4Tvj6OH9YE9NdeAFsuCdgm4qn8JnqvGZ2_dsQ70T0M4_c1eVtOtaMj-YnjymW3deWp_AoMqp-yeKe1V-FglqHbXpp3OCb_SCObWkCu4btQ4VCeYbXOCmsXzELXHDlNGmvjD08oEe2f4c_a9pOmW_7rDoXV8yRYo_lqdai7I_5BsqnGS7_i9WeS41DZBPEOQHKnIPptEoShYEKJq14RPFVk4jxq4YPJmyoxZTDdbYxojMpY0hSeUCdZeN5Q8u7PLOTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c02612ddc0.mp4?token=icBzWfywV8vpOXt6cCyeRYRWCYDHOkTBCrqdnb3HNkL0Cp3yQYXERu9gqIvf7WGEmG9qu6B8PhQzJ6FU8TtdlMNlrQNY_N55LlM4QJKqnZefgl5Ic3kBFV760SBg6K95er2nWIQZ9pyR5ufy079-yy5j0AMR4KKUCXzuPNYkSYlO-JVRvxRW9ka_Jw-E9phkbH-yDOTBIxobVOnEecx7fWNSWDR2O3gq5pVQifM2Ak1RoAcM0LXkPwr9MnaO08W8kKH0t2yzfSSLlV1kc6rxMeC0MBYNc4oob5ibCeXiU50oME-L7bGxPizHJOsGlU94O76cD5RLUxd7UHSuVsuNZj34ip96DACarbsE_i9FcCphPzBtArOFu7g1PtOSavI_DHugs8NdneAUAxSEGApKKY3scSG89nph-k4sGf9Q-4Tvj6OH9YE9NdeAFsuCdgm4qn8JnqvGZ2_dsQ70T0M4_c1eVtOtaMj-YnjymW3deWp_AoMqp-yeKe1V-FglqHbXpp3OCb_SCObWkCu4btQ4VCeYbXOCmsXzELXHDlNGmvjD08oEe2f4c_a9pOmW_7rDoXV8yRYo_lqdai7I_5BsqnGS7_i9WeS41DZBPEOQHKnIPptEoShYEKJq14RPFVk4jxq4YPJmyoxZTDdbYxojMpY0hSeUCdZeN5Q8u7PLOTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇫🇷
آنالیز تیم‌ملی فرانسه تحت‌هدایت زیدان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107529" target="_blank">📅 09:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107528">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107528" target="_blank">📅 01:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107527">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107527" target="_blank">📅 01:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107526">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57b621a66f.mp4?token=rwkTas0rkARARXxGBNRCzyaNglGS5I20v-bTqqs3wmrVWPv71xHEwP87U3I9bXkSL9tj0EkrDETAHnXjx7K056ETTh7olcblRHvvNj_asoyWHYIQoa9sqI4WsLJ7DlaA9oVY30Pm_XhGI_WqpXteRNfLN3d_Tzs9_Eefga-RHXAM_44ug1YgFQCtNd92TEDvoJFPQtgHrQTyIHBUZ-vqhWmj0SuSYEXycaPKnuLRSfJ_HbjgPao0buV3TYzgWH4RKXRCjRQuTL1zuutjZywZzRHVL4lyKZSWkeM-_PIdB3rNRxmkq9KPnxQ1LfQkb5GrOicCZdX_sq4SPR3MuDT4mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57b621a66f.mp4?token=rwkTas0rkARARXxGBNRCzyaNglGS5I20v-bTqqs3wmrVWPv71xHEwP87U3I9bXkSL9tj0EkrDETAHnXjx7K056ETTh7olcblRHvvNj_asoyWHYIQoa9sqI4WsLJ7DlaA9oVY30Pm_XhGI_WqpXteRNfLN3d_Tzs9_Eefga-RHXAM_44ug1YgFQCtNd92TEDvoJFPQtgHrQTyIHBUZ-vqhWmj0SuSYEXycaPKnuLRSfJ_HbjgPao0buV3TYzgWH4RKXRCjRQuTL1zuutjZywZzRHVL4lyKZSWkeM-_PIdB3rNRxmkq9KPnxQ1LfQkb5GrOicCZdX_sq4SPR3MuDT4mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🙂
کنایه‌های سنگین ژوله به امیر قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107526" target="_blank">📅 00:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107525">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tI7FLluLQe5fph6TVBcVPx-L83-XDgubd_3ohLGiPHgjuHLwaC7zuU2ZgkWhS6LOUdChv5BaD0KK-sReHJ0-r-SbSinPI6eLtWuh4QzNIbi0nRNgMlf5kCDK5hyBppL8KU6p7HaLGr0Ni3dPkt4p320w8FVJgmlW4yPhtiHMzV8Os-sw0UfsaVqncmd0uMDFzMEJO-Kz_V7ZgpnxG8_QaXKH2eg29VGp6JTdTOq9N7xhovL0x_uSd8sjEbuxmeoRNKA3kywTgGEIKP6gxjztjeH6-QrWdPDdD9DK_JCO8t1E9Xg5r7Jo8bwQorZeD58oSKLio6ycLfama5OHcvoNTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعتراض میثاقی به باخت امشب تیم قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107525" target="_blank">📅 00:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107524">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqY40jl9SzNoX9AimQMfl33LvRUc4tJ8quQ54Dn7jqIffjz9xrEcNe_EJA3AmZoPJikqpaGtobRYtvNntrYsMycMgMjzkcrHlgEKekaI4D088cqltqbkraSX2W-URNKRjh3Xtnmh3DrJ37NcZK7lKm0gBBR8onFdV4e_-hjHjSdPpRZ0ewv4FX4rnyJ3qKRErhxPEnXb8a6GsVh7RwFqUsNUSo97QHR_VjYvekRhJG3KCDrRVgzo06yB9j5cgmJbKzzh4mZiXbvgkrkYzXWrc3ANRWtEeCrx1ldLKjGFSxOQyG2BA3DiuFtZk5P1Du3drYfxoEG5CgPB_3THnw63gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
پایان بازی؛
🇪🇸
اسپانیا ۴ - ۱ کرواسی
🇭🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107524" target="_blank">📅 00:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107523">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5febf615d8.mp4?token=iobkedkTuCeg8-uI_2jVT14Lp-a8WNz2xfxawABn8tbwRCSFUKW4AzxPjVqN_ZCkZxX1MfDOSyZ7b8s8iC29ZoqgONdrB9475KzPA4SyEFGDPHvRnx1iz8eLOMq-gLIFGf1ZCnaoeYrnv55wijBxvYE_Ic5nC1xev2Eq_h-8boIdMj9eXz_qquFZ7BcecqkqKwKnGyzRQ4bLTcFTCeOzmEu5XLtTpZxUdGqUKw5NRtkwV7UZGFMm0wgg5Jty4uqUs1HJgv4OqnYY6M_RVs9NoXxuee4D1aSkuxPWEpC627uTOupmGf-VROqUfSX1hLWvbH72SIhw1ExUCqwbbQy1ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5febf615d8.mp4?token=iobkedkTuCeg8-uI_2jVT14Lp-a8WNz2xfxawABn8tbwRCSFUKW4AzxPjVqN_ZCkZxX1MfDOSyZ7b8s8iC29ZoqgONdrB9475KzPA4SyEFGDPHvRnx1iz8eLOMq-gLIFGf1ZCnaoeYrnv55wijBxvYE_Ic5nC1xev2Eq_h-8boIdMj9eXz_qquFZ7BcecqkqKwKnGyzRQ4bLTcFTCeOzmEu5XLtTpZxUdGqUKw5NRtkwV7UZGFMm0wgg5Jty4uqUs1HJgv4OqnYY6M_RVs9NoXxuee4D1aSkuxPWEpC627uTOupmGf-VROqUfSX1hLWvbH72SIhw1ExUCqwbbQy1ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل‌سوم اسپانیا به کرواسی توسط لامین یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107523" target="_blank">📅 23:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107522">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گلگلگگل سوم اسپانیا به کرواسی بازم یامال
😐
🔥</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/107522" target="_blank">📅 23:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107521">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/713c4da9c1.mp4?token=ZeDi1vLTNaqzb3BOfcmZ_1qI8QjFh14tppdjf2vceBBHykcri_YfSQ4asnsFcYGrWYb_QxBBTqp5uLKFBDfitfGxMzI6Ts9UjXCtwniFxuhyuMckHOrpcEWJN_0aYjmjfURXGS_C6o7ado74knM52HCMTdjS7pZrcG1emLXkfLpzMs8bIcJxZkQO39JHyfvI4Z68SclDX_jOgibBUB37PPJMLhP6BE79gzU4xFW1PAd5BkAdU54yOLahAzS4nZIbabDWKbC5LjnQr54P6Oi0ZMaavGHPNFBytRRySnLBS_M3Ts4CMmP95QQM6EWhFL9w5VmmDhStzOtPZTEf9XEVQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/713c4da9c1.mp4?token=ZeDi1vLTNaqzb3BOfcmZ_1qI8QjFh14tppdjf2vceBBHykcri_YfSQ4asnsFcYGrWYb_QxBBTqp5uLKFBDfitfGxMzI6Ts9UjXCtwniFxuhyuMckHOrpcEWJN_0aYjmjfURXGS_C6o7ado74knM52HCMTdjS7pZrcG1emLXkfLpzMs8bIcJxZkQO39JHyfvI4Z68SclDX_jOgibBUB37PPJMLhP6BE79gzU4xFW1PAd5BkAdU54yOLahAzS4nZIbabDWKbC5LjnQr54P6Oi0ZMaavGHPNFBytRRySnLBS_M3Ts4CMmP95QQM6EWhFL9w5VmmDhStzOtPZTEf9XEVQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
قلعه‌نویی بعد از باخت به روسیه: از برخی بازیکنان در اردوهای بعدی استفاده نمی‌کنیم
ای کاش از خودت هم در اردوهای بعدی استفاده نمی‌شد، آقای قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/107521" target="_blank">📅 23:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107520">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
‼️
⚽️
امیر قلعه‌نویی: دو بازی اخیر ایران بسیار مفید بود و توانستیم پلن‌های تاکتیکی خود را به نحو احسن اجرا کنیم. انشالله در جام ملت‌ها دل مردم عزیز ایران را شاد خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/107520" target="_blank">📅 23:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107519">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86c5f06ad.mp4?token=hC8fWeKMOVpAGJKYt5Nd5PqxYMGIZPCa9SDG2ftc3MQTTvGX60UuYimDQy7Qrnqvr0tlaLlB6YSGm8MEBaOgebIA3ktzXGruMBuPb5NLdD4ZXK1vJ3YVLVhPJSiAg1_DM3QWjfZR0Et7HApg4xx69mqvd7Lkn5zlcYcKN0R6eapnYPjB_x-VbK8wQxKNYWIpVQHvHVlZDCbFPqPedtL3psC56ha-9QfND0tsbAYtqRl8rSuJ9h1Thqf6ZbHnazZ3GJM9xIuHgczk2nJuOegH9c1m8iOIxnefcE9-e6yd3lsLzG-eGMDhUmnT2xQicBlGT7lC3E56U2FPiOO2-xqcnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86c5f06ad.mp4?token=hC8fWeKMOVpAGJKYt5Nd5PqxYMGIZPCa9SDG2ftc3MQTTvGX60UuYimDQy7Qrnqvr0tlaLlB6YSGm8MEBaOgebIA3ktzXGruMBuPb5NLdD4ZXK1vJ3YVLVhPJSiAg1_DM3QWjfZR0Et7HApg4xx69mqvd7Lkn5zlcYcKN0R6eapnYPjB_x-VbK8wQxKNYWIpVQHvHVlZDCbFPqPedtL3psC56ha-9QfND0tsbAYtqRl8rSuJ9h1Thqf6ZbHnazZ3GJM9xIuHgczk2nJuOegH9c1m8iOIxnefcE9-e6yd3lsLzG-eGMDhUmnT2xQicBlGT7lC3E56U2FPiOO2-xqcnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
پاس‌گل لامین‌یامال روی گل دوم اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/107519" target="_blank">📅 22:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107518">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2651377ca2.mp4?token=e7rktdGR-t7f2dZWpJkp4-S5OM_jtz2H1goj-21MdCt9hVKMXgWTdRWXzMPI5dpONH72KGMCSsumyXUahXWVEfwmcDge5dBQ3b-6_FPFHQyPUAoFWaqdOZy8B-lkGZnMgRXlceDeSiHgGwvyQLUEb3IXV-MdUycX_P4CQtg4LGCQIXYySgKNdYf2DnOpzN8pY3PAjvIXMg2sHkDkseJVFr3xeoDgHJGAsiUG-Je9kcvMe97ykPJstD-SO3ORbbpr4kO0OgXJjK4jkLGI2TqMvdBjaPBjT9Ncxq41kQ8RP0JUD2xlTNHif7nbdWEzUdnSXYe5QL0DYTyRTws3phZqvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2651377ca2.mp4?token=e7rktdGR-t7f2dZWpJkp4-S5OM_jtz2H1goj-21MdCt9hVKMXgWTdRWXzMPI5dpONH72KGMCSsumyXUahXWVEfwmcDge5dBQ3b-6_FPFHQyPUAoFWaqdOZy8B-lkGZnMgRXlceDeSiHgGwvyQLUEb3IXV-MdUycX_P4CQtg4LGCQIXYySgKNdYf2DnOpzN8pY3PAjvIXMg2sHkDkseJVFr3xeoDgHJGAsiUG-Je9kcvMe97ykPJstD-SO3ORbbpr4kO0OgXJjK4jkLGI2TqMvdBjaPBjT9Ncxq41kQ8RP0JUD2xlTNHif7nbdWEzUdnSXYe5QL0DYTyRTws3phZqvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول اسپانیا به کرواسی توسط لامین یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/107518" target="_blank">📅 22:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107517">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گلگگلگلگلگ یامال بازم گل زد برا اسپانیا</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/107517" target="_blank">📅 22:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107516">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38f859d863.mp4?token=ms695dxh73CKyrgz0_FsOLCMZtjQ0fwakbYzKA771gf5I5jT3wz8txq77FaU3t6RZnxEfE2d_DA3MmHRdB_WtxsOtdQWmfa6MdBSDhWu0U8dOxUXf12Fc6alzykj9w1IvMz0fVF49DdCNcGOgYAbF0RYQxEt1oFU8z-RLDRqNJhqKLgR7skTe8nhp2mQ8AEHhOu9Yt8pWddvb1yloJBtxFn19KB0dbRhUOyPgPy27P6Em0fEPrm3hXXzyMW0RG77cBMEmL1PdLEUW-sFOsfB8j42uBJVqMXyokdt20iFeM5Hpx_BPOEB1ktK9NIzQRbMi3W5SeTTWzF867rglhjc6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38f859d863.mp4?token=ms695dxh73CKyrgz0_FsOLCMZtjQ0fwakbYzKA771gf5I5jT3wz8txq77FaU3t6RZnxEfE2d_DA3MmHRdB_WtxsOtdQWmfa6MdBSDhWu0U8dOxUXf12Fc6alzykj9w1IvMz0fVF49DdCNcGOgYAbF0RYQxEt1oFU8z-RLDRqNJhqKLgR7skTe8nhp2mQ8AEHhOu9Yt8pWddvb1yloJBtxFn19KB0dbRhUOyPgPy27P6Em0fEPrm3hXXzyMW0RG77cBMEmL1PdLEUW-sFOsfB8j42uBJVqMXyokdt20iFeM5Hpx_BPOEB1ktK9NIzQRbMi3W5SeTTWzF867rglhjc6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
دیس ابوطالب به فان 360 فردوسی‌پور: فان واقعی اینجاست و هیچ شعبه‌دیگری نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/107516" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107515">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhchKlrteVfDGDpJ0h4QhWVt9mOMAWc0aPUy1SVRgOLeLMszDVOM-H9u4Pwpg1biCqtVyxu05PEdxYhe9Kb-VnMXNDqVKAItLZ4hZk7QGce5p-UqgYS4ujBGUEl_kWE49jTrMiKMfFCuglevv3rP0t4IgioBtC0di6cjvy2Gqq2pbI5EHlGNpokUPXtWitjLOx6MckRSSi747ge2Q0QlDFVY2ETR9StgjbBJTH7a-52ycIDn04lWTaH5FgGKu2RNwlA5jo7oM66ZKXgK19ov6WNSAryuTWRK6auGX55YEA_nsol4pdKdpQy9xraTj2mgEO7CbBzbdbA2f1t_qAsfKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پایان بازی؛ روسیه 2 - 0 تیم امیر قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/107515" target="_blank">📅 21:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107514">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
پنالتی برای روسیه</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/107514" target="_blank">📅 21:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107513">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mwb7pQyhOO_pZPeygKtMr5LGqnk6iHF4kVAfSnapRl_aJkWeBRXKbxqJ-ejUknXesD7H15DZyJJUsmmhbw94raf1CQk-rFCb52Mkf_6iW4EDasaDJAiQlRbqkEvH0gNOMuW12aNFjHXiF19d9K4x_EsF5ca5Jz7Wd_I56b-0g6_1BqN_kgx76FJpq4p901BFpDQtjiH4BqBMcp2ZpsOKvW3aX2tD1MYmNVprDxk_R8lDhMxz0srM8b03a84kFUhfIDLtCQnp4ylGW7ij839s8lso8naYJIP6I7ewiEk9XQ9SWqfNjsQRSttPYP8j07u9DAjnj8M5hUbO4sYhZewaNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
وضعیت پات چطوره؟ ران پای راستت خوبه؟ همه‌چیز مرتبه؟
🚨
🚨
رافینیا: «خوبه.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/107513" target="_blank">📅 21:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107512">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c98093c1e.mp4?token=Vt8b3KrfMuRqjzM6LA64ake0mVjokcz0W_PYXWPvgpKP-HbH601z0uOiFkE7KzLT93utJxYFijspNixLRmg5WqTiuSVAmcLTqAXCqOIZmmQdF-Oz48KTan4WB5G8Vdsd7sKQEKU0-XiytF71xtvc4kflDCwZjsWyE1IAdy_y6PDM5uVoOvA3DeYjN4-SbUdYHl9b5C3p-DDhFilDgQXiPkakHnnIJF9Gt5oUz33erlkutekEeWdBnRJ4EcLPOlokCzUnujqjc0C3aeuagn9aFLGaFLx948juImoqQ6yA8Jn8fbkc2-uIFYH4oHmpwsox_ovpvOTGg66JJzczkZR_pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c98093c1e.mp4?token=Vt8b3KrfMuRqjzM6LA64ake0mVjokcz0W_PYXWPvgpKP-HbH601z0uOiFkE7KzLT93utJxYFijspNixLRmg5WqTiuSVAmcLTqAXCqOIZmmQdF-Oz48KTan4WB5G8Vdsd7sKQEKU0-XiytF71xtvc4kflDCwZjsWyE1IAdy_y6PDM5uVoOvA3DeYjN4-SbUdYHl9b5C3p-DDhFilDgQXiPkakHnnIJF9Gt5oUz33erlkutekEeWdBnRJ4EcLPOlokCzUnujqjc0C3aeuagn9aFLGaFLx948juImoqQ6yA8Jn8fbkc2-uIFYH4oHmpwsox_ovpvOTGg66JJzczkZR_pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤍
‼️
چهره درهم قلعه نویی روی نیمکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/107512" target="_blank">📅 20:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107511">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYQZd9N0C0LR0MZYra-fPN_l6qor5nX4a7jXh2x76iA5b2kjKJKmXfFJ_PWl0ALxhasvYrVC-41Fx1FRTG1deRSHIG_l6FVCdCW2F5h-6DGoYNMPwdFpL4Ky30WrPICqloFBd7I1z0C1zUgp1-jx4nCiS77xJVt3U4J9Mf5HPvJSevEy-d5LozKkO5mQiMv0eBCgOCEAfvPr3_I6AbDi-j5bR0ZBn2NIhBmpenaWHpQVlWjz1gAVebeWAkfleSH8hcS295IhtvX-74cAXf6qAB9ch9smEU6XIbmRMcYURhMgcBRmhz9-M4Es4836Ch1X0maH6wLgphe6XyYV6XpaIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇪🇸
اعلام ترکیب تیم‌ملی اسپانیا مقابل کرواسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/107511" target="_blank">📅 20:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107510">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWU2Wjvvr6KtrLtP_SVSCiZOdQGYVgpREY7Pbkf5pBVObpXBNEfg_WTDJ5__no9BV9PnvcsG3SjHAX0tHZmZbtxdSjOPyFSQFBN_ik5rNHMez82q-MYc1e7GGgi8GlbKLrZ3UeIjOX_04TBfGYe00TDPszKRVG2Ykhau-c9bLJqK-JYXYHPkA-CpqmZTtnVWwYrwPtl9tM_8ah4Lw0mTFVeFP82-cNCH-cvjrn4-riwI5jcr2SHvLIaZOuxu4II7LsEHNROsjsWgFfldIuZqVIxoZC_Xauj0FxiCJS672sJAf3EUgAWF343W1xAUg4mphkkXDV_G8fCfuBmGvjkjUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال ایران حالا بهتر درک‌ میکنه که این‌ مرد چه نعمتی برای بازیکنان داخلی و لژیونر بود و فوتبال ایران رو از حالت کیری الان نجات داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/107510" target="_blank">📅 20:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107509">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41fa93705.mp4?token=sYaMi-hF1eLompvoMBYP9kRoLTGt615FP_nQC8A-ZhwdO1iUltxW4l83xv2QlkiC61znE81LnFWv4RlFOViaSB3WY_U2JNUKcrHsp4uEbxgZAq9sXvVydSHq1KRu-3qPMNh7ex_0Wm--bf4gRJ0Hh8gXzCDVScPi1G5W_uCdnWZusgRoZYNl4Hqv5TcbPWpb4jvQgvLogTYx5WDFCbYzH1IM4LUZSo5qpDe1IKkNCccbi7mcFGUHOGeMSV_ovRoZVYokUKIkpu93XQr8wC1m4X2K3n2q-w-EFwVEWStuNQeuOjtWeIHhjY9kt778UDH1ckgNtWVIVljfL8lZZEcw_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41fa93705.mp4?token=sYaMi-hF1eLompvoMBYP9kRoLTGt615FP_nQC8A-ZhwdO1iUltxW4l83xv2QlkiC61znE81LnFWv4RlFOViaSB3WY_U2JNUKcrHsp4uEbxgZAq9sXvVydSHq1KRu-3qPMNh7ex_0Wm--bf4gRJ0Hh8gXzCDVScPi1G5W_uCdnWZusgRoZYNl4Hqv5TcbPWpb4jvQgvLogTYx5WDFCbYzH1IM4LUZSo5qpDe1IKkNCccbi7mcFGUHOGeMSV_ovRoZVYokUKIkpu93XQr8wC1m4X2K3n2q-w-EFwVEWStuNQeuOjtWeIHhjY9kt778UDH1ckgNtWVIVljfL8lZZEcw_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل دوم روسیه به ایران توسط گلوین (35)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/107509" target="_blank">📅 20:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107508">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‼️
گل‌دوم روسیه روی سوپر کاشته حریف!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107508" target="_blank">📅 20:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107507">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/117f9ab643.mp4?token=Xx3q7G4ocPMONkWEeeHmMhQteQzKfqb8h2777vhmnkVWTTJ36LxeD0Z1FKhTL3nXSCn8yi0rJFhGqcJ-zgEO4DaYPr7F1TnMxzHO4pjQgQSE5UiQuAwkdYsIeaEgyBnWZFcSpeo5LLyzlGYjy9Eaa8qoV_1VpGTlkzUTiVsWMAybtSs-bPdA1XHnoLueSw3tyBJlzNaNpDwUlzWvSh4zKEN63_KoL_mRK_cXG7jiJ5VDY56ldKVSp0VF9wETji-JDBMyFb7on-YcMojMB0tDQtyUsOwDKu3_BCs5-p8zJpTdFSuBHcDETVKYyVQhmOyjXMCjEO_LkJgxbyQfw0OemQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/117f9ab643.mp4?token=Xx3q7G4ocPMONkWEeeHmMhQteQzKfqb8h2777vhmnkVWTTJ36LxeD0Z1FKhTL3nXSCn8yi0rJFhGqcJ-zgEO4DaYPr7F1TnMxzHO4pjQgQSE5UiQuAwkdYsIeaEgyBnWZFcSpeo5LLyzlGYjy9Eaa8qoV_1VpGTlkzUTiVsWMAybtSs-bPdA1XHnoLueSw3tyBJlzNaNpDwUlzWvSh4zKEN63_KoL_mRK_cXG7jiJ5VDY56ldKVSp0VF9wETji-JDBMyFb7on-YcMojMB0tDQtyUsOwDKu3_BCs5-p8zJpTdFSuBHcDETVKYyVQhmOyjXMCjEO_LkJgxbyQfw0OemQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇷🇺
گل اول روسیه به ایران توسط گلوین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/107507" target="_blank">📅 20:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107506">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">روسیه یکی به تیم قلعه‌نویی زد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107506" target="_blank">📅 19:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107504">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9Y2YZz5Qu7HLT2YDKnGUu-hZh320gnQqf2fkKYj7eE4B7lur_pdxWKE8rkzfL726_MFLKzma675fQ115L0q-U-CRLLBuTQovzV-nxfNYtRiIuFAms07KuW2TeCZp38BKUuiFw4UErbkwM1h_Mv12EHhDtGic44SrA4Lp1ohQDSns0Ydmz_D_l03RKyn_XIBTsdfJ_bwj2LnfXJj_1cqX1e82Syu6Fy-2i8DDrnr4PVtXYmZQXoidYFwu9sEZlNWoJJj5vLmEBX6oTvVd7yo5Gmm1ifNoOSoKqPd52gNLqu-ReNDOtvZKqXdxibYjmkFuvlV1aGpVIHGCxsiSG2hDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیگ برتر تو یه بیانیه جزئیات تخلفات منچسترسیتی تو فاصله فصل‌های ۱۰-۲۰۰۹ تا ۱۸-۲۰۱۷ رو تأیید کرد  این جزئیات تخلفاتیه که تو بیانیه لیگ برتر تأیید شده:  منچسترسیتی با تعدادی از شرکای تجاری خودش قراردادهای جعلی‌ای تنظیم کرده بود که توافق واقعی میان دو…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107504" target="_blank">📅 19:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107503">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pefLkqTbFWJp5emStPXKX6d6svdXCgkdbI9Ak9BeJavUZonGwMH5_ENsxufDoiNzH3KyJAa0vo9hX0XsCUNG0ok1722D55oJiOsuHt1u-dApZTGhXcUBN4-shJbMSsvLiRQ1f5jcNxp_TBEd3oFy-c9iqE55tZOb4LAb8hE-8cqLQM5Eg6RjK1q9ni2HxyUBUUmlQvFSRpCKghXv9Sl5rBgl26rM87YBtNysJUgvRPbi8dx6BNlH3N4o_E3DE8Lu7LCK74otf0yWkLlrGMItbLrC4SkHycNBHvdwxfneezvc6qP2N81KddvcHIPrANVDVzZ2IH7eYyvCZUpT7lNhYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیگ برتر تو یه بیانیه جزئیات تخلفات منچسترسیتی تو فاصله فصل‌های ۱۰-۲۰۰۹ تا ۱۸-۲۰۱۷ رو تأیید کرد
این جزئیات تخلفاتیه که تو بیانیه لیگ برتر تأیید شده:
منچسترسیتی با تعدادی از شرکای تجاری خودش قراردادهای جعلی‌ای تنظیم کرده بود که توافق واقعی میان دو طرف را به‌درستی منعکس نمی‌کردند. این باشگاه همچنین به توافق‌های «صوری» دیگری نیز اتکا کرده بود تا درآمدهای خود را به‌صورت مصنوعی افزایش و هزینه‌هایش را کاهش دهد.
این باشگاه صورت‌های مالی نادرست ارائه کرده و وضعیت واقعی مالی خود را از حسابرسان و نهادهای نظارتی فوتبال پنهان کرده بود.
منچسترسیتی به‌طور قابل‌توجهی محدودیت‌های هزینه‌کرد مالی لیگ برتر و یوفا را نقض کرده بود. در جریان تحقیقات لیگ برتر، منچسترسیتی چندین مورد از وظایف خود در زمینه همکاری با لیگ و رعایت حسن نیت کامل را نقض کرد که از میان چهار مورد ادعاشده، سه مورد تأیید شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107503" target="_blank">📅 19:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107502">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a09194b9.mp4?token=pAR6lnaKKxvDi0D8SC9aXtP02XDkIQsL1tUPIenOdab7_89ZMkOZvBbh2hRWr04QGpQ2ujpisjmivhr-I5cc_w132M4WfSCgvsc2vy36nOaiVPX9J4MGANAgG8WUYdtQxJGFHjn_-Wb4XJ7hbxayGcQ3ZE_1oE9ZJRE2gxs5HxyYE3E_m6Yu1lKfHYK-Xm5QUCLTUAWi70JxcpvXvTatoCxRm59gG-g9Ldybx0MqSW0dEs9CYxTAqcRIamwJWzVEIefnK-qUNb0OPhwXjbs6_pXMLrEZQ2iEo7V4yzHK4jxQPTqg0khHZaSp4NwiVK7yrhnF0WwSVuvbpFYiykf_Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a09194b9.mp4?token=pAR6lnaKKxvDi0D8SC9aXtP02XDkIQsL1tUPIenOdab7_89ZMkOZvBbh2hRWr04QGpQ2ujpisjmivhr-I5cc_w132M4WfSCgvsc2vy36nOaiVPX9J4MGANAgG8WUYdtQxJGFHjn_-Wb4XJ7hbxayGcQ3ZE_1oE9ZJRE2gxs5HxyYE3E_m6Yu1lKfHYK-Xm5QUCLTUAWi70JxcpvXvTatoCxRm59gG-g9Ldybx0MqSW0dEs9CYxTAqcRIamwJWzVEIefnK-qUNb0OPhwXjbs6_pXMLrEZQ2iEo7V4yzHK4jxQPTqg0khHZaSp4NwiVK7yrhnF0WwSVuvbpFYiykf_Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باهم ببینیم قطعه ی زیبایی که استاد جواد خیابانی برای گلر تیم ملی، علیرضا بیرانوند تو مترو خوندن
🗿
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107502" target="_blank">📅 19:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107501">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107501" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107501" target="_blank">📅 19:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107500">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_FzU_wMkjiqJpihOKpOVf3PJuJ-rq29PnGabtPilFuqLE9KCZr_DTOAw4ek-78iaBCpCVjFuMKpW4OQgNNT-l-iKWpB29S1NFvXqz3wJfuVeatxHFJoWUS9ZBvlgjIwx-1Qn_90RwO4u1FKqiTe_jG-vs4GXmtQd3jNXAnviLgDWja0iJCV9I07LbLc4ITen9jSvdFzlNr1Mq7CwPJbGcN1lERJuP7ByDwUcsRQB0frmS4GgiiCT1L75oIL8YA1M3_rLgx9mnexKsD-MEH4SWPMFghLJzJBTvIkGCg7gdBKEIJrvjKUPRFB4gmOtqxGclVhuEFncH_JtWpzeKHQ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز کرواسی
🆚
اسپانیا را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
کرواسی: ۳ برد، ۲ شکست و ۸ گل زده
اسپانیا: ۵ برد و ۹ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107500" target="_blank">📅 19:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107499">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfL1nY9rf1sGqBycaiFNPSQZlyfcQxOocYq6JsCfbE6J9xZbFwaFtC_1C8_wt6JRvLBjDYADF7jJq7rchMiQY1ZVIrT_J-M9dSK4o__DZuvPyfM3BaaUwrVKG_iLWniMXYCE4auz-iAlyLeql6soT6Hce__AYwRKr4zLLGyUCJJju0lx_LYFyKDWKUDLDKPopNYW5sVEJLSlCZPAkxwLtw6ijzehLMbQpIvEc8yCCTB1cbql1gI7WsO-qpq-CbCDK1LkKAXoHspFxkvN0JZj1ADr-O9ekMcwSft6FXWaq2wV5ALtISjTisxjGU3hRfSORJ4d9rzq16IfO5hwucCIbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇵🇹
رونالدو بدلایل نامشخص در تمرین امروز پرتغال حاضر نشده. تیم ژسوس قراره فرداشب با دانمارک بازی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107499" target="_blank">📅 19:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107498">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68583cf71d.mp4?token=kb4hjUzEG8GLF2zkBtq5hqPIE6SYJo_LvQKkfneXTeJuaqExm97yXOEgOqwHbXHw4iiLJXIqVgCzf0sbTLI6X11omS4FGFuRAWyGeQO1-MHCZZO2UuLvcKXIQgllqg9MaFo_APNOemFbsAOVTKE_ygPWTo1wwnGc-HiR_IoSwGbo3gcUW74ay5lvPpYe5ukDq2M3nrDFVwxVsi5nNfZNmRMy5fEYg-80EF3NsahsgiwYT_a_JEwVMDpoascGFNP8o91UqMWWxcWny8g5IINI1OZruyvKoMGkNF-T5JrJAwFTS1TVf6xXpvBUE2qgSQmI4GFBr5DKmqiOHwww5BRKXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68583cf71d.mp4?token=kb4hjUzEG8GLF2zkBtq5hqPIE6SYJo_LvQKkfneXTeJuaqExm97yXOEgOqwHbXHw4iiLJXIqVgCzf0sbTLI6X11omS4FGFuRAWyGeQO1-MHCZZO2UuLvcKXIQgllqg9MaFo_APNOemFbsAOVTKE_ygPWTo1wwnGc-HiR_IoSwGbo3gcUW74ay5lvPpYe5ukDq2M3nrDFVwxVsi5nNfZNmRMy5fEYg-80EF3NsahsgiwYT_a_JEwVMDpoascGFNP8o91UqMWWxcWny8g5IINI1OZruyvKoMGkNF-T5JrJAwFTS1TVf6xXpvBUE2qgSQmI4GFBr5DKmqiOHwww5BRKXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
صداوسیما والیبال را هم از روی آپارات پخش کرد/ بودجه ۴۰ همتی برای مخفی‌کردن لوگو!
📺
سازمان صداوسیما که به‌خاطر پخش قسمتی از یک سریال تلویزیونی در کانال آپارات کاربری عادی به نام نفیسه‌جون، از این سایت شکایت کرده و دنبال جریمه ۳٫۵ همتی است، بازهم برای پخش مسابقات ناگویا تصویر زنده آپارات را بدون رعایت حقوق ناشر تحویل مردم داد.
🤯
جالب این‌که همچنان سانسورچی به‌دنبال محو لوگوی آپارات است و مجری تلویزیون قطع پخش را به ارتباط با مرکز(!) مربوط می‌داند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107498" target="_blank">📅 18:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107497">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3TKcI06xrdNBCOA2r_F9XwAOnxCG8o-s1yz7Ypy4AieQv6bBcHw6Ob7L5H4ekF1IsYmluIHrc8sirrKzdp624lCNT2pyTPsmk_DSG-k96FARQG60Ju0dM3cDaDx3aZ2QN184lRT2M7t3CEC1JjUyK4R_OCotOh6kHYx_nYlJG-U9sYhpfABNQlRe5dNAM99JZ9gS5dxpx5zgWIb7gdNtO1GNSkAzmz_WkZoVtcleJ_U1wr58XA-zd2HGQLcdvEeFN_3fv5mRIr90UflunrHK-5BrMqWuTK_2G47ZxGYX22xWIErfasMcPyUUcylFLjly9QQI-q1RA6vWyM3QfKgEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب تیم ملی ایران مقابل روسیه
سید حسین حسینی، شجاع خلیل‌زاده، علی نعمتی، صالح حردانی، آریا یوسفی، رامین رضاییان، سعید عزت‌اللهی، محمد قربانی، محمد مهدی محبی، سردار آزمون و مهدی طارمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107497" target="_blank">📅 18:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107496">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cb0JTEQpp7oq0JQNuCmsT-r9wClj1DnxLlJh7uKBXE0o0lO2Wt6CJWv2TJ7mFkQsMKU5EK3cqC1u8Xv4jbFbg10at85xx8pVaqSfuKnwoIjhS8IMVFEk-xQmBovqIV4MYuCYPk051wQM3VC6j-LzWMrw32KTgwFfcRE-DUjG1vLrgqx7ZT0-fG3bvO9GcldDhpcYPVc4c02wN7aX8FCn3WOTxWqaaJ30soKL-1JpxU5lFrhIX1GlH87RL0Jl5hzERWAmnzM4QnPGs30Njjn5cEGGlbk-IU5zVMFgnyfPnrNojXjOaC_ivf0dQ4iSkOK31nkRgkNCguV_bCojT0MWgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
مصدومیت های کریر رافینیا
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107496" target="_blank">📅 17:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107495">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30660fe341.mp4?token=n0MZjcjm4HStTr-DjTrVeAQdnj6jp2zQMSKj2BtxGcxWIwyhZ1OtfvesCr1o2i656quR7oJyEuQ6u809IzQe8A4UPUNRzfjJaH4P-K_tvo2XjlnnUuCTuCgEruq5f8-_vTZgNyHS24gSmB9VAtgLLLFrpd4TDsk2D5YtD8Ec94HPCHadOFS87ujTm4hzbGLsIUcdqrtXKXUb4f_-NmtMFFHhBg_KDn4xnwq6_oj8PT6tcKE4Eb5oDO9Wui32YP5eV8AYzdiNfNNhgTdEVepOhNWfX83pz5-maoFyqrZ1rn_S-6Hu7FIMYzlslX6qqXgthYffOLECejhZ_rLvgC8-qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30660fe341.mp4?token=n0MZjcjm4HStTr-DjTrVeAQdnj6jp2zQMSKj2BtxGcxWIwyhZ1OtfvesCr1o2i656quR7oJyEuQ6u809IzQe8A4UPUNRzfjJaH4P-K_tvo2XjlnnUuCTuCgEruq5f8-_vTZgNyHS24gSmB9VAtgLLLFrpd4TDsk2D5YtD8Ec94HPCHadOFS87ujTm4hzbGLsIUcdqrtXKXUb4f_-NmtMFFHhBg_KDn4xnwq6_oj8PT6tcKE4Eb5oDO9Wui32YP5eV8AYzdiNfNNhgTdEVepOhNWfX83pz5-maoFyqrZ1rn_S-6Hu7FIMYzlslX6qqXgthYffOLECejhZ_rLvgC8-qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
على تاجرنيا: با والتر ماتزاری به دُمش رسیده بودیم اما پیام های داخلی برخی هواداران پرسپولیس باعث شد قراردادمان امضا نشود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107495" target="_blank">📅 16:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107494">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa385d1d9b.mp4?token=mTWXcMg7QyE4LlxWc95cCenRHo4HMUtdDp_M-8zwXEtjngg8vjZ0JT0qoMj3_8yNa3-gNIZe5ZAXWYbHfVw2N8DC0r89kJ0kxAQZ8OLT862wxdJVNLwcdYoPa07YfXoUYE5A-yDazBDZVpCaReF9tSRnLFRUV8RyFZuedz-c7qXyd0E3cQPsjR7OKzayDfnMbzsOfeLTe3ihuFAE-lpL30cxgyvtstTehC9qB9XXRzqbxEN3vlye7WK68xkBHCLmyktgNd7bhAeRTwiD2_GU4A0DGwEVa8_C0L-fyb6Xf3rzm8_JBgCN3iP62otHQ1qn4yNhwhlAZMU14-B56fh1wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa385d1d9b.mp4?token=mTWXcMg7QyE4LlxWc95cCenRHo4HMUtdDp_M-8zwXEtjngg8vjZ0JT0qoMj3_8yNa3-gNIZe5ZAXWYbHfVw2N8DC0r89kJ0kxAQZ8OLT862wxdJVNLwcdYoPa07YfXoUYE5A-yDazBDZVpCaReF9tSRnLFRUV8RyFZuedz-c7qXyd0E3cQPsjR7OKzayDfnMbzsOfeLTe3ihuFAE-lpL30cxgyvtstTehC9qB9XXRzqbxEN3vlye7WK68xkBHCLmyktgNd7bhAeRTwiD2_GU4A0DGwEVa8_C0L-fyb6Xf3rzm8_JBgCN3iP62otHQ1qn4yNhwhlAZMU14-B56fh1wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
وقتی امیرحسین‌قیاسی با چندین یوتیوبر مصاحبه و از درآمد عجیبشون سوال میپرسه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107494" target="_blank">📅 16:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107493">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39b949da6c.mp4?token=pN755rUWM3zr3SlOTmoL5MJ4owzGJoeQWpIBQ6zVuNxbhb-w8lG5aHI25LGKkrgN1R-le2JKpEHJeUPLLOlb3mAG9DdtXVtY54V2IEdfg9jwFnc_W2xYxG0Vl_uzfk8fVmp0KWmSnuyR_LqvqwGR_CHw-zc4yD28H28E0xDRkFiDqTa3Ocm3fVMXoT-_MLm6-W3plP7LaTvb2bJ49-w_3iQLPhogHWMaHY2aGctOdRzf533USekwLVCTVrD_H8v0O0PEmrThPS30L3gcNzBonU5IzXsYWrHkWTVUMKzKE6HDZ-zW3FpAFR5VWpV8X69Vw58fCAKnHk6_UKOuJJLBJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39b949da6c.mp4?token=pN755rUWM3zr3SlOTmoL5MJ4owzGJoeQWpIBQ6zVuNxbhb-w8lG5aHI25LGKkrgN1R-le2JKpEHJeUPLLOlb3mAG9DdtXVtY54V2IEdfg9jwFnc_W2xYxG0Vl_uzfk8fVmp0KWmSnuyR_LqvqwGR_CHw-zc4yD28H28E0xDRkFiDqTa3Ocm3fVMXoT-_MLm6-W3plP7LaTvb2bJ49-w_3iQLPhogHWMaHY2aGctOdRzf533USekwLVCTVrD_H8v0O0PEmrThPS30L3gcNzBonU5IzXsYWrHkWTVUMKzKE6HDZ-zW3FpAFR5VWpV8X69Vw58fCAKnHk6_UKOuJJLBJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
#
نوستالژی
؛ درگیری تاریخی علی‌دایی و محمود فکری درباره تیم‌ملی در دهه هشتاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107493" target="_blank">📅 16:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107492">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dG1VcsBdr-yHlM4ymdJMP3oZZnv-kE8iHvzfGPvQ8HT35vD6td8KhRzcO-5F_46qhoSIZYyIHd2NSsFBrV8MIjolzM7JbsbGVPOCuZql_lyJtBuGymYxN5NYc2XDSkjl80t2hoqGnvYXNC84y2rL8z6HtdkJhSgZKQaXdKGxcEhokSOpysTX3nVYqrk3Hi78hxVjSbAZoLenIP9nuDHuSBzufONEdzwm4iForVw-5HGJy9EodLlZa-ZqJndtbT244NWBpSkDGnW9ZGTPwk5EtnxQvaYONaM6cVGP9bvXR9mPVCOQmgxgrzjFL2aIVW6j0OrmzQSmDOFq4h_JycKF5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇪🇸
میزان دوندگی تیم‌های لالیگایی با رتبه فعلی آنها در جدول مسابقات این‌فصل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107492" target="_blank">📅 15:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107491">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بررسی پرونده فساد مالی منچسترسیتی به روایت دقیق رسول‌مجیدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107491" target="_blank">📅 15:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107490">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚑
#فوووووری
؛ رافینیا در بازی امروز برزیل از ناحیه ران دچار مصدومیت شده و از زمین خارج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107490" target="_blank">📅 15:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107489">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11af8c0994.mp4?token=evKrC7TVYothc9wKOCmO0Go7U3noprOCRTdqBB9SLZFf20sKMf8twEo68eWW-cJ0uWf74YvQ988vYW2xNnLwkA8MuLWQ43FMW-mjOlBU7QvgJC6mj3AEhOip7FrIN81EA01cMLZKzZUtj7t_uumbdCO394b4dS7qfy7IvwHroKMhkhPvLuMytDyOL3kTnkCTf7BC0bob5Q96kYLWpXSi3TRlt2IXxDTABhzPacWDdHimtkvgY_LlJN6HUOsY9FGfc4RXb8BSNAw6hHlYVRqofqGTp3SZOqeWQqwyOgXIq5IfWwh2dH_DYuoDOd5p-HzejDH_-9WV7v3wYliUpwlfo5UWIC4ypkFFCirVURQV6noN5lAts_YOp1Ug-bljNJunwlL4xYnaBc_5KYUVHre6i2FBI7rxx5S-zuiUpo1mjoWvc-UJjY02STgTFv4nCyWzk-r7snYDan2uCa6Vu3gLE4FxaZibdhL8b3XP3EXCbcGwjtIxo1S1-AK8wqPHEXW2e0RnzZIrHYFSKYr1VZIqRp2W4dv3Em_s0ZEzBU0Gj368P09T6Nn6l0qy87I3T9tuCHgjNdyj-BpmjOq7e_DeWeWPA-ZRiHBxd6RLLY9waeiEB92gqo02s11T5W31sCcAW4Ck9E8-1CGlC6Q2i8BROF974R-UHd-JdXUkUxBkl-I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11af8c0994.mp4?token=evKrC7TVYothc9wKOCmO0Go7U3noprOCRTdqBB9SLZFf20sKMf8twEo68eWW-cJ0uWf74YvQ988vYW2xNnLwkA8MuLWQ43FMW-mjOlBU7QvgJC6mj3AEhOip7FrIN81EA01cMLZKzZUtj7t_uumbdCO394b4dS7qfy7IvwHroKMhkhPvLuMytDyOL3kTnkCTf7BC0bob5Q96kYLWpXSi3TRlt2IXxDTABhzPacWDdHimtkvgY_LlJN6HUOsY9FGfc4RXb8BSNAw6hHlYVRqofqGTp3SZOqeWQqwyOgXIq5IfWwh2dH_DYuoDOd5p-HzejDH_-9WV7v3wYliUpwlfo5UWIC4ypkFFCirVURQV6noN5lAts_YOp1Ug-bljNJunwlL4xYnaBc_5KYUVHre6i2FBI7rxx5S-zuiUpo1mjoWvc-UJjY02STgTFv4nCyWzk-r7snYDan2uCa6Vu3gLE4FxaZibdhL8b3XP3EXCbcGwjtIxo1S1-AK8wqPHEXW2e0RnzZIrHYFSKYr1VZIqRp2W4dv3Em_s0ZEzBU0Gj368P09T6Nn6l0qy87I3T9tuCHgjNdyj-BpmjOq7e_DeWeWPA-ZRiHBxd6RLLY9waeiEB92gqo02s11T5W31sCcAW4Ck9E8-1CGlC6Q2i8BROF974R-UHd-JdXUkUxBkl-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
اگه‌یه فرد سیگاری هستی حتما این ویدیو رو ببین و برای دوستات بفرست؛ تاثیر مخرب سیگار روی سلامتی از زبان دکتر رهبری...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107489" target="_blank">📅 14:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107488">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd91aee857.mp4?token=Cx2Mnq-IjcqsmsTCJk-QhJd0CtqNGRPxnefW3E7F-fyA1bJvPjbwsFq8EMOLrS96N4uJQmNGQYJ86xCxBdt3auRHJm0vpC24YrB9SEWYKrInW9ttpo180SrsLkVgrgngb7jTXcu0dBcd_eM9nMtMC9c69LE94-cntvcVyyYE-3Vf8WtHmXGiAiYkMU40WTm2MHDhAGZ0x9lkrOmoJRaVD40BpZ-amH0p8DZGR3LyyzzPP6KR7XdpuxY0i4s_9QkOB2rpphee51pw_4Z5W4g5B7gHYuS-_b_yF_DTSzd80OywUmeiOBfT__BHI4WKePUSdLZTIlxILLCEgQPD4AnlxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd91aee857.mp4?token=Cx2Mnq-IjcqsmsTCJk-QhJd0CtqNGRPxnefW3E7F-fyA1bJvPjbwsFq8EMOLrS96N4uJQmNGQYJ86xCxBdt3auRHJm0vpC24YrB9SEWYKrInW9ttpo180SrsLkVgrgngb7jTXcu0dBcd_eM9nMtMC9c69LE94-cntvcVyyYE-3Vf8WtHmXGiAiYkMU40WTm2MHDhAGZ0x9lkrOmoJRaVD40BpZ-amH0p8DZGR3LyyzzPP6KR7XdpuxY0i4s_9QkOB2rpphee51pw_4Z5W4g5B7gHYuS-_b_yF_DTSzd80OywUmeiOBfT__BHI4WKePUSdLZTIlxILLCEgQPD4AnlxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇵🇹
پیام‌واضح ژسوس به رونالدو پس از نیمکت‌ نشینی در آخرین بازی پرتغال مقابل نروژ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107488" target="_blank">📅 14:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107487">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf450995b.mp4?token=qaY-9Bkkm2oYSHZ9Fvo-djF1qBb4tDxXn_HnOgqacyUFdNtC-teOuVERDUIPa6b09rS3JBRBB0HqxTwwHe25D8p00YROSBxzO5ZQzeju749z9cdM4jAELZlK5H9r7sBggDvp3JVG76NrlOHB4ycCt-7E6c-X7-g4J0bewtIzku8YuAr_Pjcdt54q3chatbmfzjZl9t1Md9-95FmxADkdT3yj-HHpe8P6nLXf0lx4yklspH2V_uX9xuVVu_mWkzkFMTmqq5SAnIkZQyiznDaq_u6AIpafAIXIltyMEnkeR619PPaw75mwJTh55tSJVm13xaloX_-UD-g8wMSz7an--bgtx1Plm8WLBBpXnVOYL8P68I2Tuc4XdcATBmb17CxVnNeffXHATHlNPBxfkTO86WTZuSKWbocQzIWmjeeoSz2FV-Sa_CHY6h8Y9rEgR0Ig6jdbg5CFGy5OP2D9jZFDpRJuLXld_9yoxZG2UEbSH3Neoa63BcE9Q2447tali0IkkN-qvQor2EGoDVFyKq1hkXhrn0TNuroQ01UGcy8NUqJS2x8RKvLgsXzD4dd_v2RH-lwyhRt8g9-7GE77H_Wy92zZlIuWluaI2hVZIQTcFLigVtuE8VpHOkOI_TdDY901LEOnvPSWDSSazLU6xlcmIbka5eT53G25Bq8ju4PAHiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf450995b.mp4?token=qaY-9Bkkm2oYSHZ9Fvo-djF1qBb4tDxXn_HnOgqacyUFdNtC-teOuVERDUIPa6b09rS3JBRBB0HqxTwwHe25D8p00YROSBxzO5ZQzeju749z9cdM4jAELZlK5H9r7sBggDvp3JVG76NrlOHB4ycCt-7E6c-X7-g4J0bewtIzku8YuAr_Pjcdt54q3chatbmfzjZl9t1Md9-95FmxADkdT3yj-HHpe8P6nLXf0lx4yklspH2V_uX9xuVVu_mWkzkFMTmqq5SAnIkZQyiznDaq_u6AIpafAIXIltyMEnkeR619PPaw75mwJTh55tSJVm13xaloX_-UD-g8wMSz7an--bgtx1Plm8WLBBpXnVOYL8P68I2Tuc4XdcATBmb17CxVnNeffXHATHlNPBxfkTO86WTZuSKWbocQzIWmjeeoSz2FV-Sa_CHY6h8Y9rEgR0Ig6jdbg5CFGy5OP2D9jZFDpRJuLXld_9yoxZG2UEbSH3Neoa63BcE9Q2447tali0IkkN-qvQor2EGoDVFyKq1hkXhrn0TNuroQ01UGcy8NUqJS2x8RKvLgsXzD4dd_v2RH-lwyhRt8g9-7GE77H_Wy92zZlIuWluaI2hVZIQTcFLigVtuE8VpHOkOI_TdDY901LEOnvPSWDSSazLU6xlcmIbka5eT53G25Bq8ju4PAHiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
دیس دکتر ابوطالب‌حسینی به دکتر بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107487" target="_blank">📅 14:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107486">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09a02722eb.mp4?token=LRX456MOyuLqXbGGyJkt_vdS5FGFQq2bzstcPBH75XUd2h--BGog_JxtySi0SD1fPQ3XKFr4PsJKlNTrcv_xMuO4aT6pZo_YKSqgj0uWTOn2v4nUUWBg_OhDAUwpDaMuwrmX9ZwObIB9D7mq5k8pdDjjAut9Vn9VVbbjh-iowT99QOwl2zzlirxKooMm3a3s2Mz_s-yL69_-K446JQ67BqZgA3CGm791-3FKxJcmxArg6gtdlFDZz-cdrZK5zuYZmZwU3nhUkg6J0GQQNjiT9xrrbN6wvmTEGC_Ga0eJhwPAcTQB9xvFVeAOmJB8v-3TB8hzK8Z49nKuMrMVZnXUxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09a02722eb.mp4?token=LRX456MOyuLqXbGGyJkt_vdS5FGFQq2bzstcPBH75XUd2h--BGog_JxtySi0SD1fPQ3XKFr4PsJKlNTrcv_xMuO4aT6pZo_YKSqgj0uWTOn2v4nUUWBg_OhDAUwpDaMuwrmX9ZwObIB9D7mq5k8pdDjjAut9Vn9VVbbjh-iowT99QOwl2zzlirxKooMm3a3s2Mz_s-yL69_-K446JQ67BqZgA3CGm791-3FKxJcmxArg6gtdlFDZz-cdrZK5zuYZmZwU3nhUkg6J0GQQNjiT9xrrbN6wvmTEGC_Ga0eJhwPAcTQB9xvFVeAOmJB8v-3TB8hzK8Z49nKuMrMVZnXUxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
عادل: ناکامی تیم ملی مثل داستان تورم شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107486" target="_blank">📅 13:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107485">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ee940a4.mp4?token=nPRZAJBDRqS_hzMkgeGYWP2vSoBJIDdb-DR8OMa5T2TKPnl0DW7qLkZeYvuelItNuO1rxIOz3xo_4oGM3dpa7wGh7bHxXvUa5BfLj3fC-40VElgonPvlV3tCRy14W5katjRYJ6H-3kuu8waJ1eRUXrQ88j0WxDOb2kU-CVH_j3rc9XJrwPZHQUWcgJ5dKZB7Czn8C_jxOFM4HTnD1TZ7cnwfU8H8NQt2GxqNPA9uQ1f-qKcKP9i1EDlenuRs_1DoVq4O9vjIatyhqRMkCfJX9S88J_D2daAqK-xbX4rqSfPluyz84hr3HP06KUaBOMJ51RrYVvNDjk8W8JPjVmyjNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ee940a4.mp4?token=nPRZAJBDRqS_hzMkgeGYWP2vSoBJIDdb-DR8OMa5T2TKPnl0DW7qLkZeYvuelItNuO1rxIOz3xo_4oGM3dpa7wGh7bHxXvUa5BfLj3fC-40VElgonPvlV3tCRy14W5katjRYJ6H-3kuu8waJ1eRUXrQ88j0WxDOb2kU-CVH_j3rc9XJrwPZHQUWcgJ5dKZB7Czn8C_jxOFM4HTnD1TZ7cnwfU8H8NQt2GxqNPA9uQ1f-qKcKP9i1EDlenuRs_1DoVq4O9vjIatyhqRMkCfJX9S88J_D2daAqK-xbX4rqSfPluyz84hr3HP06KUaBOMJ51RrYVvNDjk8W8JPjVmyjNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
📱
پست‌جدید سعید صادقی بازیکن سابق پرسپولیس که خبر از ازدواج‌خود می‌دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107485" target="_blank">📅 13:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107484">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‼️
نیکولاس‌سوله مدافع سابق بایرن و دورتمند این روزها مشغول دروازه‌بانی در لیگ‌های پایین آلمانه
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107484" target="_blank">📅 13:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107483">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0bf7aaba1.mp4?token=knhKDfq3xUJxfvj0XN9i9p85One9OksnhOvf1zTYeylOQyaOMlQTiaG0rUKO_d-X43QPv93pP9eAYqz4EiKvinBfOQAEdkmInuCVHRIgJFzkuNTy3pgNlCBrUrxD4usO58swSUxp4tl2rNo7i5SAgRaTH2k6Ot_grGtJWt__k7Tl6GhbPE7OaeOfjDpFHwL8V4Bux7iXslvF10jElMaVza7OttpYOsRCKQGjxqvl9tL4dpdgKBi0iLnIHA-VOSLutpzpa_gMmmEDHvY4b7sixoeOBpF4Hwsk8SmuUXsIl9o8ccHBn_nV7BEegtMDfMjqt2kPw9ceUme8qGaX8AAtNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0bf7aaba1.mp4?token=knhKDfq3xUJxfvj0XN9i9p85One9OksnhOvf1zTYeylOQyaOMlQTiaG0rUKO_d-X43QPv93pP9eAYqz4EiKvinBfOQAEdkmInuCVHRIgJFzkuNTy3pgNlCBrUrxD4usO58swSUxp4tl2rNo7i5SAgRaTH2k6Ot_grGtJWt__k7Tl6GhbPE7OaeOfjDpFHwL8V4Bux7iXslvF10jElMaVza7OttpYOsRCKQGjxqvl9tL4dpdgKBi0iLnIHA-VOSLutpzpa_gMmmEDHvY4b7sixoeOBpF4Hwsk8SmuUXsIl9o8ccHBn_nV7BEegtMDfMjqt2kPw9ceUme8qGaX8AAtNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
وضعیت وینیسیوس در بازی با استرالیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107483" target="_blank">📅 12:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107482">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgAn9DJ7LOqNCGOYCfRxVLlL66zsniJ4EdoV1xAOArVzFlygsBqkQ00NfRj98Ke1MZvXbEMzEvp_Ue2aDqo42SC6elo2uORH1moQYsyyHhlx4e3v8NAvk2BytY-OL2dfZdaUsT5lD2iCoSH9_5mivx6X_PRV8IsIYdCdECr8c6V3bu003qIKQHz1yCFe3V4Y2NxL12x1oF8w2hsLTZoq_0K8Z0BbBeVhT_Jz_NOUqk91evdA0yc0WC9yu2kFq2ZsHSJN5eS92-l04cfV8fwjkokFfgYyF6qOJ7YXUEj4VFoLTyo8VmRPYVBsAOoAUcTcK2SSBuvdm5XaiG0bd2YFYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
علیرضا بیرانوند به دلیل تاهل، داشتن دو فرزند و شش سال فعالیت مستمر در بسیج، ۱۵ ماه کسر از خدمت دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107482" target="_blank">📅 12:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107481">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2592f7770.mp4?token=BFBhdyyrn97eyAHHeszev-uvmTi3qNjPMD3M6K5arFbd0I7rOhp2zF-pdSgr-7-Uk0gT2fjKjwpnbzXFRj-O8afqSHcV4UBsjPVQkKx8ysLFRqCm18h_BiG_e10Rs6I9oxWnfBwIou7Y17FNyQIAV5vNqm6MH5M82UfCXHGnMzCj7RllupG0nxfz5BqfqF2pYEv7R1brV1jlf7JWVYWTd9xUssBvnb3r4unTc1sautfjH-VKbv2x4Akw2tRdOjnMtZJf-XVWYE3LcsKclXX5Dkozn0lm9zsWGz8_FVonCEmiDPhKQ8bmsqYfCroAhoOM--XCr0LMHjkxUlhiqG98ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2592f7770.mp4?token=BFBhdyyrn97eyAHHeszev-uvmTi3qNjPMD3M6K5arFbd0I7rOhp2zF-pdSgr-7-Uk0gT2fjKjwpnbzXFRj-O8afqSHcV4UBsjPVQkKx8ysLFRqCm18h_BiG_e10Rs6I9oxWnfBwIou7Y17FNyQIAV5vNqm6MH5M82UfCXHGnMzCj7RllupG0nxfz5BqfqF2pYEv7R1brV1jlf7JWVYWTd9xUssBvnb3r4unTc1sautfjH-VKbv2x4Akw2tRdOjnMtZJf-XVWYE3LcsKclXX5Dkozn0lm9zsWGz8_FVonCEmiDPhKQ8bmsqYfCroAhoOM--XCr0LMHjkxUlhiqG98ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
خاطره خنده‌دار امیرحسین صادقی از سوتی وحشتناک حنیف عمران‌زاده مدافع سابق استقلال وسط مکه
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107481" target="_blank">📅 12:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107480">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvSKzp5x3g3yrv8AmQch6wGJP1rgFJDBzDw7jAXf7PdTFRUiPQI0-luzo39j1Kiyfjfm_9XWfgwZ895uADQD28NDh1493HY2rpl3w5sKLSkXUu7EMQyM5fhLlqq0rSkG6W-lAPuQCErjR9qMAH2jh71n-pg1VTwTsOIq2MWmIXuwgb2EV8bR2v-3nNq4Wy5cbGjKvTG6DoXm2gwVBLn16ZYMASrCbMErYVpRDfLKzinkjE2SqKxkF39gcX41LJL8pLeNzsPGRIraFn_IzuQjNf36MHZ2zWXToyKu-QF1dSnD6JtezqZr4lh_SEaHgY3JqNoOxGvKn-ctw4KI5HA1Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
ترکیب‌رسمی برزیل مقابل استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107480" target="_blank">📅 12:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107479">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e6f4de836.mp4?token=Y_QsoZx0vQv2ATbLDPb98BoOZqRJQdmxfNLw1juGc_2o72h6dHpx7DpXe92NGY4n4lrPXgl2uLzGSdJujTJPxBF3Vfsw63pg2PulpvDm9ZcNBBA0NQ_6AymdiVfDBAqcbYU25EhOB1nkoJRvqvupoc6NQ2r_wMu5l7ZsmixVx_QC41VRC5gOAnC3DQdmxp2DxrQADYAOf3_4U10vGllXjPv9aaFVcPlRUeCsxVG5UzVxj2GtE1xVTvtRLxDOaM_6oB0F7UEoVAkvBlsG2B1B7FQnCgHrADRo2aeGjK1hjH2GlV9Mypv5J6gkpjjRGO9qdf8F323PsW8uhYQiFyhtzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e6f4de836.mp4?token=Y_QsoZx0vQv2ATbLDPb98BoOZqRJQdmxfNLw1juGc_2o72h6dHpx7DpXe92NGY4n4lrPXgl2uLzGSdJujTJPxBF3Vfsw63pg2PulpvDm9ZcNBBA0NQ_6AymdiVfDBAqcbYU25EhOB1nkoJRvqvupoc6NQ2r_wMu5l7ZsmixVx_QC41VRC5gOAnC3DQdmxp2DxrQADYAOf3_4U10vGllXjPv9aaFVcPlRUeCsxVG5UzVxj2GtE1xVTvtRLxDOaM_6oB0F7UEoVAkvBlsG2B1B7FQnCgHrADRo2aeGjK1hjH2GlV9Mypv5J6gkpjjRGO9qdf8F323PsW8uhYQiFyhtzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
تشکر عادل فردوسی‌پور از ابوطالب‌حسینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107479" target="_blank">📅 11:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107478">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4uSavX2C1fAgCgXEWozvmKZdw2BAVWYdzzWv0X5ZvvWrBQUk67EYo8_RpdYtzNdf9e2qKb-366JtXolC--YmbRi78MfFqe5aETAez11mpgGO4zW7Wk_j60v8rj2dtoGBovcFmZ940sCuIpaFtGbRHsQL5R6mQQUZAiyrjsK2p6Umav-qFDdDvKIgFxGmnvvDjTEAm3eea6i7NSzteLSN0vXp55Pi3hFMi6RxAVibV98esIoT_yLyVjQOM2Hb3hte9wijQkTKJbV_PB22tBYMiczcQXQjQVKgP3NLgCyJrSIkdc7BkZGMUvMB09etJJG4BcmMHTKBxHFXPX_dGOAiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💵
وضعیت دلار تا این لحظه: ۲۵۰ هزار تومان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107478" target="_blank">📅 11:43 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
