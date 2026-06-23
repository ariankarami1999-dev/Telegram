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
<img src="https://cdn4.telesco.pe/file/L5tMIbqpAf5dILxJnuZbLcyH7kLhyr1ZyyUiwPPDo8TVS8jOP9Fd7QqIhpDd7cgpI5GE0W9IFolxedC2etQYpLP4hBSgiUwJMZeBBmnz9kh02n_xFXtH-XpiRG9cND4ZBGkqYYwx3VOrEJ7h48RwJ-dqkC9T3Yf-vWnjaY2OVk3SwuPXMnte0bAcCL0zgiOucJFA5L2WUI-lV6rc2ikgshCnhAcseRUO0WxY3I-U2HjwUg0CqvI6d2oeQ68s3Wla5l-b0hy-oeNy3qEyBHt_-cpvbSIoYir9yNe66wlM5BfD5i84gEOv2XHcWMUba8FErYV_2N2iW3BCOTnOLS-meA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 11:54:03</div>
<hr>

<div class="tg-post" id="msg-444237">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a13e62494.mp4?token=ql3qY5MfYvGZ668AzCBYUc5L8XnNQ0uOUzgfcNPXGS_h1GKlvqN4oPKK85fPxlnfC1JbaXSoDjeFbE05GDhfptoYI44_Wk0F8Ik1bOcmavWncAk89ytStVf03-WbpUiUO74V2FkpnrY-OOpk6HpfnJkrxURQfYZpPucFhupp7Ffy8a8aTYa4y1C69K7gTaPEGmHGOJb18xK5Su_TVvpFt3cF-ZhfuzuFirq5od4eAwYVd8kPQd_tuJT4fKGsbOuXgXypbmXHLKaNOV9rUNlwqj-346P1eOfQ6pzA-OyWLadu0mpJhsrxPatFfLjWHXXVLNTVji6wJRR0hcVF3OZnaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a13e62494.mp4?token=ql3qY5MfYvGZ668AzCBYUc5L8XnNQ0uOUzgfcNPXGS_h1GKlvqN4oPKK85fPxlnfC1JbaXSoDjeFbE05GDhfptoYI44_Wk0F8Ik1bOcmavWncAk89ytStVf03-WbpUiUO74V2FkpnrY-OOpk6HpfnJkrxURQfYZpPucFhupp7Ffy8a8aTYa4y1C69K7gTaPEGmHGOJb18xK5Su_TVvpFt3cF-ZhfuzuFirq5od4eAwYVd8kPQd_tuJT4fKGsbOuXgXypbmXHLKaNOV9rUNlwqj-346P1eOfQ6pzA-OyWLadu0mpJhsrxPatFfLjWHXXVLNTVji6wJRR0hcVF3OZnaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: برای ما مهم این است که به دارایی‌های مسدودشدهٔ ایرانیان دسترسی داشته باشیم؛ جزئیات آن به ما مربوط نیست و این جزو تعهدات آمریکاست.
🔹
خروج خبرنگاران از محل مذاکرات سوئیس به این دلیل بود که ما برای کار رسانه‌ای نرفته بودیم؛ ما برای مطالبهٔ حقوق‌مان رفته بودیم.
@Farsna</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/farsna/444237" target="_blank">📅 11:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444236">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74d4781cf4.mp4?token=FTQnYZQjSGDAiTp4PAv9-FEZwqRVBumFJVi4P-arJuQl6j2kc82KiTY0ewHhvXzavoitCf1KzEvn06-EO8Mix-u0RZVQI0MEhnITYFBoVqO8mOQpHwWw8Y5sEcplXZsMcmUAHgK10V9MTAY45Y_de4gpgQ1Ig2CNr3O1IxLUrFKipCzrlgtT0GIX_DX6vMxM1r254sylMgenf-5_4A9o0gizzQRG-JiopTK0xOPt15U6sa4M3t3c4oj4-gCMNNPGIT9tjETIiyUv8zj6BEoPZgiaHs4_jcUr3qtdFM8evzw3dJH84M66b7TybTJDlR2FFfVnw2JTMsXZxYKLBvTYKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74d4781cf4.mp4?token=FTQnYZQjSGDAiTp4PAv9-FEZwqRVBumFJVi4P-arJuQl6j2kc82KiTY0ewHhvXzavoitCf1KzEvn06-EO8Mix-u0RZVQI0MEhnITYFBoVqO8mOQpHwWw8Y5sEcplXZsMcmUAHgK10V9MTAY45Y_de4gpgQ1Ig2CNr3O1IxLUrFKipCzrlgtT0GIX_DX6vMxM1r254sylMgenf-5_4A9o0gizzQRG-JiopTK0xOPt15U6sa4M3t3c4oj4-gCMNNPGIT9tjETIiyUv8zj6BEoPZgiaHs4_jcUr3qtdFM8evzw3dJH84M66b7TybTJDlR2FFfVnw2JTMsXZxYKLBvTYKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: توانمندی دفاعی ایران مطلقاً موضوع هیچ گفت‌وگویی نبوده و نخواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/farsna/444236" target="_blank">📅 11:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444235">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502e49ac2f.mp4?token=qWr-KtCZ7NLFoEUWYlUkuHnBgm0z8fJNY4urssMjx_Lauxl1z1473CXPiiDBtWFGamzldilz9QtVfPGHSXSK6gANZdszZkxadfXCELrVXFDFLtl4mFhRmNKaOGmNLim0so4cWxOmyIrR4UfhvTcSmMpa_oKJHsuBDP1fMppptBER5biNYjOwdm9-u-TEIH-g3L4oERXisMq1UxV0WjeuaA4iGcICjAV1SUflpWNBTsZeFoFX43rTDEE8AQTAcYC5o9MXeFApFpiZBBgQmsvrPfnfZuZ2_NIma0CbSt6IfvYI3b2uVBcljaMg7g1__dWhF9tWBN7tk-hNURV18t88ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502e49ac2f.mp4?token=qWr-KtCZ7NLFoEUWYlUkuHnBgm0z8fJNY4urssMjx_Lauxl1z1473CXPiiDBtWFGamzldilz9QtVfPGHSXSK6gANZdszZkxadfXCELrVXFDFLtl4mFhRmNKaOGmNLim0so4cWxOmyIrR4UfhvTcSmMpa_oKJHsuBDP1fMppptBER5biNYjOwdm9-u-TEIH-g3L4oERXisMq1UxV0WjeuaA4iGcICjAV1SUflpWNBTsZeFoFX43rTDEE8AQTAcYC5o9MXeFApFpiZBBgQmsvrPfnfZuZ2_NIma0CbSt6IfvYI3b2uVBcljaMg7g1__dWhF9tWBN7tk-hNURV18t88ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
کمی تهدید وجود داشت، کمی هم گله و شکایت، اما در نهایت، مذاکرات ادامه پیدا کرد و ما به پیشرفت‌های بزرگی رسیدیم.</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/farsna/444235" target="_blank">📅 11:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444234">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9d4619ca.mp4?token=Wtx-_GhGa9TkTN37cH9TaN3V9CgqHid5ozLDZwipAPK0d32NXqvuLw9p7_LWg0zxwjxb_Zv2ZQHHkiTLMeymuiagF8WBisE2L9HK2WIIXbwPpXqdLiqeVfCMwSNz9mwRcTqhCS0ZENjlcYOOM7bZcjg32kPhGUZBJYpeNb_fZj7B0URBOD7vNQV3ZcRAQLRatshcIpHSX8CSL2l4w7LJVHIystkxEqtE2j012QjnAfIOaL_DzMl7BQmtR5A3YBqxQeEGhpUpwKeaIH-n6t8Uu5GprU4G1L344tUgO7IbGgl2d3FzWFUev874yBuKtHUFBdACbXrjXBGkqlfTsXOoqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9d4619ca.mp4?token=Wtx-_GhGa9TkTN37cH9TaN3V9CgqHid5ozLDZwipAPK0d32NXqvuLw9p7_LWg0zxwjxb_Zv2ZQHHkiTLMeymuiagF8WBisE2L9HK2WIIXbwPpXqdLiqeVfCMwSNz9mwRcTqhCS0ZENjlcYOOM7bZcjg32kPhGUZBJYpeNb_fZj7B0URBOD7vNQV3ZcRAQLRatshcIpHSX8CSL2l4w7LJVHIystkxEqtE2j012QjnAfIOaL_DzMl7BQmtR5A3YBqxQeEGhpUpwKeaIH-n6t8Uu5GprU4G1L344tUgO7IbGgl2d3FzWFUev874yBuKtHUFBdACbXrjXBGkqlfTsXOoqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند
🔹
سپس آن پول عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد.
🔹
آنچه به آن دست یافتیم، از نظر من یک توافق کلاسیکِ به سبک ترامپ…</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/farsna/444234" target="_blank">📅 11:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444233">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dfbfbc0c5.mp4?token=JKFLyYtLscPj6w776uJw0ES0R3C9PMKfJimH2vnmyNwZT9i3BtutZLW1bNh6DATX_zOM8nUkfEjtkmduqxZ9psSeQG8c4uT0l9af03msCnHuxd9lE_8dQNL5P3-hGk--HJcdf_xrChqZWwkDeMYuc-FWGlxqCCB-UpWIrrq9gCq3-7WJ9A7wCtVclKF68tsbiVa0rGCq29ZdyzNU9iFgkKQM91StH-8gfuVn5IaaxVuqsO4oPW2YaZRZ5vCm8Uk00ww3_ZAzLg7dSL8NFek2X2UnRWClClsnc0S_1Rp2pctZD3RK2QWJVrS89JuwXM9ZDB9hqDLgW9-nxKYVAb3mkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dfbfbc0c5.mp4?token=JKFLyYtLscPj6w776uJw0ES0R3C9PMKfJimH2vnmyNwZT9i3BtutZLW1bNh6DATX_zOM8nUkfEjtkmduqxZ9psSeQG8c4uT0l9af03msCnHuxd9lE_8dQNL5P3-hGk--HJcdf_xrChqZWwkDeMYuc-FWGlxqCCB-UpWIrrq9gCq3-7WJ9A7wCtVclKF68tsbiVa0rGCq29ZdyzNU9iFgkKQM91StH-8gfuVn5IaaxVuqsO4oPW2YaZRZ5vCm8Uk00ww3_ZAzLg7dSL8NFek2X2UnRWClClsnc0S_1Rp2pctZD3RK2QWJVrS89JuwXM9ZDB9hqDLgW9-nxKYVAb3mkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ونس مدعی شد که «ایران بازگشت بازرسان آژانس بین‌المللی انرژی اتمی به این کشور را پذیرفته است».  @Farsna</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/farsna/444233" target="_blank">📅 11:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444232">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yh58wGa82UZZ0VHzd-T9_AmyNFbSiqM1LqD6YHXdhq0gvOuLVQ1eQY-MB-t_M4QnU22bsNXtTdJIec6pGUOlGcZkpDK77ry4vAWgyzwkE94RW6qmQuFBpz0hSaiQp54vzJ6BqJ_tR5-VDVof2cukkHszxKvgLIBVT4EYohbiz4uFzwg4_fxgEIIwLHEJ3N3ndHVgB8WegWypOb8fVhDfRMz58UxJD-NmA2QsskmMWmcaR6zvBMElKXaMWQGdkvjpC_WqSlHU8ja0-9KjrAIRMUbmHbuPi3w-ZqZvnUQN572LjCGLOAaO1k_DL_3u0MOsaHD5mXa4pd2hyw31WWjL3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یک مرزبان در مریوان
🔹
دانیال نوریان از پرسنل مرزبانی مریوان، در حین پاسداری از مرزهای کشور در پاسگاه انجیران به درجهٔ رفیع شهادت نائل آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/farsna/444232" target="_blank">📅 11:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444231">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ia48Ch0681atVxRFbK48zVDRTS-aCyiFtlOFyRDAgOLoU3Rfn9psLj45QWqVMZsR9EqORXl9SM7OibSlsW4pSgi8F8HqoB439L9LBUjsq62s27ZAnLbBJkdRXmZ18btFMxGb65WYDDkHYMQ81vOeuLXLM3000t2wj9zSV7RJ3yCW-UjpzyiFsxX6PIOsnOSeteksBf6vU44yYgyxJIphacqGrTzmQWs3ZUT6KGkCBr0iLGoptjaHAs3UnjTf_1tgiLizVVoeSnfzKUfwYA0O4t6nolVXiQe5_50rram7vGET0rF6PqYUxbPho8q2tdjZNFzgkYAI91u3E4nJK_I4Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزادراه تهران-شمال یک‌طرفه شد
🔹
پلیس‌راه البرز: با توجه به شرایط ترافیک سنگین، تردد وسیلهٔ نقلیه از کرج و آزادراه تهران-شمال به‌سمت مازندران یک‌طرفه شده و تردد از مرزن‌آباد به‌سمت کرج و تهران ممنوع است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/farsna/444231" target="_blank">📅 11:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444230">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cibgsncNn9AdNNixL4x5rR6on9vVedY7V9W-4AT5EEeiFzgVtY6yD5NXBv57ArxCFWFpv80YmrfGQ3GRqpkMs1J1TjycBPrZYhlYiHP-TKNUfN8Whew3YGx07BAc4NdvJPVmYd8yZknA9pWyagvYK8ofSaRONXakAzBfXw_kMIMMbRM06TtknAyRIKlgUNCUFIoe872BMw7mjPU7cZG-0I86ZxBA7KSOvWnSMdJmL7LLULjWE8e0rxs7l2iFUnAuwXe9M5jumyjAkAMhEq98R5y5mtrkShHUzAfmzPMg1fvdkvzdEQYaErgBzcX31sCjPi6E3UqA9D5tit4ho1qAxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز جلسات ایران و عمان دربارۀ مدیریت جدید تنگۀ هرمز
🔹
هیئت مذاکره‌کنندۀ ایران پس از پایان مذاکرات سوئیس راهی عمان شد و گفت‌وگوها دربارۀ ترتیبات جدید تنگۀ هرمز را در مسقط آغاز کرد.
🔹
قالیباف، عراقچی و اعضای هیئت ایرانی همزمان با سلطان عمان دیدار کردند. تنگۀ هرمز و شرایط جدید حاکم بر این آبراه بین‌المللی از محورهای اصلی این رایزنی‌ها بود.
🔹
آنچه از روند مذاکرات برمی‌آید، تأکید طرف ایرانی بر این موضوع است که مدیریت تنگۀ هرمز و شرایط عبورومرور در آن به وضعیت پیش از تجاوز آمریکا و رژیم صهیونیستی بازنخواهد گشت و ترتیبات جدید در این زمینه در حال بررسی است.
🔹
تنها جمهوری اسلامی ایران و عمان به‌عنوان دو کشور دارای سواحل تنگۀ هرمز، مسئول تعیین و اجرای ترتیبات مربوط به عبور‌ومرور در این آبراه هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/farsna/444230" target="_blank">📅 11:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444229">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">چادرملو در آستانۀ انصراف از بازی با پرسپولیس
🔹
باشگاه چادرملو هنوز تمرینات آماده‌سازی خود را آغاز نکرده و همین موضوع باعث شده تردیدهای جدی دربارۀ حضور این تیم در دیدار با پرسپولیس به‌وجود بیاید.
🔹
گمانه‌زنی‌ها از آن حکایت دارد که چادرملو تمایلی به حضور در…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farsna/444229" target="_blank">📅 10:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444222">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BTmQvSfatbnVLRlhG6NMVaa5JNXXuokbx4Udi_WNfk35vS0SrsRbLm3SuXcJyIg5x6Y4oOlMT0DUqrELo9Ee2-hmDt8nlEGV6JyEl4fCXRfWP2HCmlnio5iYg_jucFCDUDpaRQtQPYZTiWxTn2d2qkWvwmvNGabDBsOZt0mLXWJ0GiSs5bLMWPDZGOdIyFeUHWWXbOHMzJYn4_voAB3HOlqW49rWZsCWgLWOEamtDxzHER8FpK3h8Ayp8FE1EuDE8buU-5oVnCkP-nUSuPnDeo_tF6Wt6IlbcDr341s-Yrs2H3cEqR2XTmFuesvBrfh8Z_GQO_SV5bBirA_vyssNVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAN7uYBc4ueYObuZtyF4SW5JK9265w1_-K8cygizfB4fQ07nKCN71hvt3rOwpPRsTQO_vbNjBS0XnZwB8erR8g6WK9mTHczAblihXC2KguGncYrhWNwtmN8qbb780Ynv-9Yg8gsnKCGm1rJoz6BZWMIP62uDggt97NHGeIk-kfX7yRK3nFOKMNDK3NMPLFDO1eCPu7vVMF7rAcjJUdkPjcgjywbtq92HsIY5TqwVPY1NU5ogGHsRVhhCTFaK20n-yq7ENKdygfOvUSpQdqJV6B49GEdGlHOTsq4-9s1F-3maZBPLcxBruYYIX2Ce64sS8z6fx5pTcb6HjbxLzWAfPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hMx1UDY8LT_F-8w7GYjbFTTGpXAc69YmtbxTgD5lokzU_Kb6pVr6odDWrGNsUwtiCP7_UR_KQnIh87l0TN01rCx4nX5DpP4xVgDfGhDRRVGI8ulGovqsJ4fH7CF9e8kaYhdjx_LtHuAfBXB8WdX3m24L8U2d72--RprvziHZ5ncLxIcRzCX0XQd9Et7JCSVtgjEAfpctX4k5RBeGCqQURKaEDrV6JBhJJg5EJkT2VnyMfakX2AatKtzJtLG5d9R3pb8iCYox3O2gSpZCcjnYfS05WfH-YA-DWQ1UD45M6rxcANeUnQ42ohvp3_WFYODFHKFH0ovP2QabtM4eUkbXvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJLujWf5QMpoID3onU17fa5V-ChZEftT7f21dVtFqd2Url06VTql6a1Ft1yf3dfrZl_UxViuW4C04fOs2i-UsT3OPy56gIaH22k03f-TjFUtK_OY6QpMj0takzvXHl_WbIvC7JDuedgzVm_xr_Pwvg3eMEn1YSZPE5B0DUPMPQgEGJGjoqi2dueJZ5Fb8LDh2PVm7ZBfBgoPbAFx9W92lC2XBcQ_ZtVPCaHeIX1_d7o6rPF9T7ru6g1RB9LghfUlc7hyaCJDwS-c5zmY3Hi8TJMIR7RYXsPcWxoEKXpKxhbThc78H-VYtVUdWf5k7AlLqKWZNljFUD9J9N3xFFzlwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lb_l_84ZBYhLWnbmPTv9a5vqkXzlh3WLuKEb89Zx4xRkcyUg0nfk3TlTtgj-LozgIKzoIejVT8CJwRZm8JA4skvj076aK6JO9Dp2XFG0GYslc-Mms4G77gjYez96v3JezgGgCs58z8TLsTaGL15GNeuVEcecZ-83gaanMQq5jl3nw9dlLtIT5vc7nyQ-2AQyGkKsMcOyPcbWSxY06Jh1ZwIwR_HDmqwfDOOF8jGXjgLwX2hn3XT-vKYGDG4Wm1fyvWrsowtMmBj16zKpGCDay9RFGgfOAwfK5VjYK0ngGgtKO7C3eRjp4Upt1MiPNvADL_2qFXn64rGSHuYpLQRCrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CRCJFmOlzQteNt-o6obbFPfFVSH7D0kJoGNOHHOrR5WxrE8FiyFQFLklpZnmRT4eVRBcT7ixKo6xoFSLLl5vSMZj3QA3JcdwhdN6OvZeeh_UKtmuggRALyW_yZE0oa0W_n10LK9vIM2XuxqAWlm-YO-2vspzAo1APeNWbdUKAipmHdfaEMNZN1wi-dkPag3Ts13PM-cPrRGtORKwMMf0QqktVuxahRfysG3e3VE9RbSi2P3AKReZFsJTyO5xESx3Ihi6_fcgBCYKTQf8UlIZZ6z3ESU9bKO-S0MQXOEOdOkMp3utVp-DcyVkQ_RGh7HD376538aBOJHpxsNpFF-tcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YeC49fujz5q-P7Q1kp6QBO76yxCkCZD3JOPPHY0Ljl6B2lk03knsLgbiCvtj9KeV4TwK8Cq93w-U35ouskKyhdyjanK2DtNbx7eAxMv-tu4UhxSx6bIforbPayyEmNGO5kX7X5NUkKm_mnC_KRMV9LTG6fY2Jdo1YQpGqIkck_C-IxGulG5QuOex0P5uVAiTnaiH7FW03c_G0lQUzx8LDoygmctvDPhsalPzWFZMJbKjkKAE6seKLfr90HbkoUZvKLMlaHUwzvvz3XzMUvSz5o60HrIONyjadTkcQCvvd2Tm6D2fDMXokArWHPP7eKbEozswukbwJ_acVhQENeH5NQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین «شاه حسین‌گویان» در باغ رضوان ارومیه
عکس:
محمدمهدی فتحی
@Farsna</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/farsna/444222" target="_blank">📅 10:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444221">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sr-JLgkzMTylkd6DJjTem3PEW89-wiK4l9p5XuSkkzxhX8qOCzElJqsAXQ1WhgEt8k4F8YFdMY18IVprsjEM-WMlfglCkvfhTkydZRS9re-wD9Ia04PB9-bGY2mZl1ROD0oitOff7RoZsX-HlncSX_klJxoYDHd8ClpvmTUOApq_9bMIesJ2Jo-QF6lERlUDf8l3ri-dVNTuyrI-zUcdFQbFv7NNWjjJ0fWs6muk5G_CWIqBemfgqzgd2H3D9hjbHx7jWdVHjGyeZcnIT-dZ4_4nfxVHFlAVn5QPcAWJHLO3YYJach_3V9oLcEeonuNNEgN1_L-1PcGaPwVtyu_i5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ مدیرکل روابط عمومی دفتر ریاست‌جمهوری در گفت‌وگو با فارس: رئیس‌جمهور فردا به پاکستان سفر می‌کند.  @Farsna</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/444221" target="_blank">📅 10:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444220">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKYagInETz0oLE5l3_8e8qgLqdtgbOsZzYzxHCQhMoE2E9Cn31FKH-wleSwxqsO-PBgdCLgpNLMQ3f58NTABkeWS8zUvKyZumztsuaeFLgR0KRFdJsIRBCSHcTkDAzpFxX5TIpVocQz2zuTOXJoJdWbvKi29JAfFX_i5C3F8Sxj0HtDLGOJO5tReILAnWDIaHAnViAHA_bqwAPteb2SIj9KXf8VSAnQDjzhZFUu78ei7FYcu6_aA8Og1_SWf8Z-Mj57R0nTB_ep92NrolpcmXyO3an7Vn63q8ZdLrHza4RO-U36_wmpHutZWztWRKpcdw9l60sirIyp2OevITZKRQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز نام‌نویسی در سی‌وسومین دورۀ آموزش‌های رسانه‌ای باشگاه توانا
🔹
زمان ثبت‌نام: یک تا ۲۰ تیر
🔹
هزینۀ دوره: با حمایت تشویقی و فرهنگی خبرگزاری فارس فقط ۵۰۰ هزار تومان
🔹
سامانۀ ثبت‌نام:
tavana.news
🔹
پشتیبانی و مشاوره کارشناس باشگاه توانا: ۰۲۱۴۲۰۸۲۹۴۳
@Farsna</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/farsna/444220" target="_blank">📅 10:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444218">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GqaEkkOgPcAVlfDFyNJh_cOYfpN-5HlgK2Wa5iPO6lI6Lp2pyQqBC9Ndh83OYuvny4eUnJY2kdltnNCK1Y4YtH_5vUH3NHkr_hsGqySsI8Xw0NrlWE0xsx4SnzjRFyN3GJ5RcKgceMfOt2gHHqLOXg_EkyzU0oUI5MfYtRpYusUCZA8cEK4cLep77IqeI2HaL88IcMoJY7Ezc4VcZexZqhDHtUFqop-asr1Jd09YGi893bYZSl5E1mKEHR-V04KHtum7g4EnTuxot6Cnl8ovW6CYMiW9T_nKx6nu_RjMhwQ8S4VBzVIbKWUpaEthjOt_rvJC0Fq1eLyVI0qhQ2Wbsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/efNh5mgoQQ_E0v8HGXNVTl9x5whuF2ohVzWxUZbSRcegLEidDEWF-HYcUbXWT-TpfEqpIiB6oIJ90rJnUl9Z2BTNX-okBxF7KMmEHTA0Uh5hJmsH7ZST6rzFooojOLBoel9Gy-oQR5qdDSMzmD2eUFh-q0FbtW88DoqBrQU4F__C1o5RlAgSOaE9HtpNVHJfEW6mQ4WVdDiOVSYxNdQKBs2ev8uL5L-oBncaqIVT-BVALLh-gtjJQYiGa2GpoSqizhDv3kwuW_kA21VKcL9fQLQqiSLatwZQyHYviIZirmjtsPYqQqqjjvPDGNQRIChyOpt5hekHrDgdnVZWoFCGMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">۷ هزار دانش‌آموز خواستار تعویق امتحانات نهایی به بعد از اربعین شدند
🔹
کاربران فارس‌من در پویشی خواستار تعویق امتحانات نهایی به پس از ایام اربعین شده‌اند و گفتند: با توجه به حضور گسترده خانواده‌ها و دانش‌آموزان در مراسمات و پیاده‌روی اربعین، همزمانی امتحانات…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/farsna/444218" target="_blank">📅 10:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444217">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5CvYzFDhXxi2WbQhMWUkpPreKOKr_glIemak7DDycfma3h3Gq9JziH5yu9s6f_8FyJ7X2Dk3FI07hBhIZLB8OqPDLV4UiA8ocnnONCjdWtk_iKGTzk3pIIlc7-qNgxCzON95K69zx6yrnhoaWANW2FzzA5_0i8JBimLAfIpntOFhnHQPq1uApxKuWiFimr04kmASGs38efOfNPtdtavQ-IkMozE-wIjFZwuMbDUkj3MHOcmg7WBu5oq1Jlb4iI1puXbWFIVc77M3CcE_oLNYfgFAzYHSkeMXhbq3MTcNsGQSggKUlc6o8MdB1xYVfzrpCqpsPZeUjeE-hNJoyursw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشت‌پردۀ کلاهبرداری با اراضی جنگلی به‌نام ایثارگران و جانبازان
🔹
در روزهای گذشته انتشار اخباری مبنی‌بر فروش غیرقانونی اراضی ملی در منطقۀ تکیش تنکابن موجی از نگرانی را در میان شهروندان ایجاد کرده.
🔹
این پرونده که به گفتۀ مسئولان توسط یک شبکۀ سازمان‌یافته در چندین استان کشور هدایت می‌شد با ورود قاطعانۀ دستگاه قضایی و ادارات منابع طبیعی وارد فاز تازه‌ای از رسیدگی شده است.
🔹
ماجرا از سال گذشته و با انتشار تبلیغات گسترده در فضای مجازی آغاز شد؛ جایی که افراد سودجو با سوءاستفاده از نام موقوفات (موقوفه آیت‌الله مرشدی) اقدام به فروش قطعاتی از اراضی جنگلی با قیمت‌های بسیار پایین کردند.
🔹
مدیرکل منابع طبیعی مازندران-نوشهر گفته این عرصه‌ها جزو طرح‌های جنگل‌کاری بوده و به‌هیچ‌وجه قابلیت وقف یا فروش ندارند، به محض اطلاع از این موضوع، پیگیری‌های قانونی را آغاز کردیم.
🔹
با ورود دادستان کل کشور و همکاری دستگاه‌های نظامی و انتظامی، دفاتر خرید و فروش این اراضی که با عناوین جعلی مانند ایثارگران و جانبازان در مازندران و سایر استان‌ها دایر شده بودند پلمب شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/farsna/444217" target="_blank">📅 10:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444216">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رئیس شورای‌شهر تهران: تصمیم داریم رایگان‌بودن بلیت مترو و اتوبوس تا بعد از تشییع رهبر شهید ادامه داشته باشد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farsna/444216" target="_blank">📅 10:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444215">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f1b8581e9.mp4?token=k520yZfCVaGhvcPkPWZQkjLkMjr0dax5zEmosI6m4SIkOXKD87Vj6sG6eHHdAFlYJn49fQDlIjJzUI82wMioz4Ta7C6Fso2xB1ClaPsGZgtfeZlNVv9fM8Mg_wNmbOBTd1ExxsW9SDjVfGdFLjodUg9nqgCJVHUqDlkA1y8YB34NvClMBcC_kDKEAtcql_pxzF7DXfgYqgzBCk8qQaGq8-pj87LLdPO_kYCyAYI_sUBIekRRiuFtArjdqlyfCa9RPV7df-fECS1tdT6gspkB7va0dUmxCIb8P2JRAx6q852bcGVVJfk8fC9ituKghoZpOYgg6EXDUAbSldXvypTeIGkAAe2hF5dDSL9K4lF_cbdcS7KYp4esmAbTt49YydbEmKH45WkK5fIhOuYelxLOxojcEmc1oEq9GFrtnpJRgxEm9zZJl5TT4i5OBwcKNYO1hqHYF_VggWSKUSGloCnsS9bDvRzadwgAnAdSXXU0ZJy2OYGsZPLpZZb6nLSxS-PlcvvD6lW4S_am2586wsMzabeERebuRhscfOiI6B7NyQQJnhGa8JTAWVIMMi6uaxCQAnY-72wx5v4fqL27Mpb2cKVbnxSdGmKw3ho5uebCHRzDBoMBPJWiGQ0LRoOQs2Z7wMi3iswVh5S_VnKUbYZ_0_lQlgJ0-cY30r5FdICSsAE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f1b8581e9.mp4?token=k520yZfCVaGhvcPkPWZQkjLkMjr0dax5zEmosI6m4SIkOXKD87Vj6sG6eHHdAFlYJn49fQDlIjJzUI82wMioz4Ta7C6Fso2xB1ClaPsGZgtfeZlNVv9fM8Mg_wNmbOBTd1ExxsW9SDjVfGdFLjodUg9nqgCJVHUqDlkA1y8YB34NvClMBcC_kDKEAtcql_pxzF7DXfgYqgzBCk8qQaGq8-pj87LLdPO_kYCyAYI_sUBIekRRiuFtArjdqlyfCa9RPV7df-fECS1tdT6gspkB7va0dUmxCIb8P2JRAx6q852bcGVVJfk8fC9ituKghoZpOYgg6EXDUAbSldXvypTeIGkAAe2hF5dDSL9K4lF_cbdcS7KYp4esmAbTt49YydbEmKH45WkK5fIhOuYelxLOxojcEmc1oEq9GFrtnpJRgxEm9zZJl5TT4i5OBwcKNYO1hqHYF_VggWSKUSGloCnsS9bDvRzadwgAnAdSXXU0ZJy2OYGsZPLpZZb6nLSxS-PlcvvD6lW4S_am2586wsMzabeERebuRhscfOiI6B7NyQQJnhGa8JTAWVIMMi6uaxCQAnY-72wx5v4fqL27Mpb2cKVbnxSdGmKw3ho5uebCHRzDBoMBPJWiGQ0LRoOQs2Z7wMi3iswVh5S_VnKUbYZ_0_lQlgJ0-cY30r5FdICSsAE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ستون‌های عظیم دود آسمان هیوستون آمریکا را فرا گرفت
🔹
آتش‌سوزی در شهر هیوستون ایالت تگزاس موجب برخاستن ستون‌های بزرگ دود بر فراز این شهر شد. هنوز جزئیاتی دربارهٔ دلیل آغاز آتش‌سوزی، میزان خسارت احتمالی یا تلفات انسانی منتشر نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/444215" target="_blank">📅 09:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444214">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تست سامانه‌های پدافندی در بوشهر
🔹
فرماندار شهرستان بوشهر: امروز از ساعت ۹ تا ۱۰ صبح در رأستای تست سامانه‌های پدافندی و دفاعی در محدودۀ نیروگاه اتمی بوشهر صداهایی شنیده خواهد شد و جای نگرانی وجود ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/444214" target="_blank">📅 09:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444213">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPtLbxm2fqEFffym7aLSIv7LmTmLcBtN-4kp3XN3ImGGb1oORI3in5-dBjylogyQ9yp66UEo8Bl4PysxeND1mMUZDmXufwoHfmJXSeB1L_mDdkNUcK4WZelUnPFRVpkpwJUhhUSHgy4ZKA_hHeXi-xKAZOr6ujd8oryuEOp1Yk4oY1XVMc6Xi_1K_tMBG1qcjGTHZs3DL5KHbpQ3VNPfTqL_5ospseeD3OeyFTbRwNzhSAMq0xSRF57oEG4pBfT-5ysFWIBvfv-YkK3HqQ1-oYiXHW98QdQBR7H-i01imF7CXpU2FUMzlkdv2iaiMC0gSyBP2g-xr_gWZweKK8jkcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرژانتین با ۲ گل مسی از سد اتریش گذشت
⚽️
آرژانتین ۲ - ۰ اتریش @Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/444213" target="_blank">📅 08:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444212">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzYRTHGspq-o5KhkPHAHP0NG49JsnV8kI03FU-U_dHD6cWWeBr--ZI9x1oMjlDXzc3uLaB9C6W6aIHF7864gVReVGNCxoRRAl1TQ-ymwSrGlHF4lHfSsDiKLKM7KmV5l7rOkda7yrHDbGhFB7dzAj3iJCgo6Z7F5_3AQ_KC4F7xIezNnSLC9odiXv7UUnhc2_jBQKPuV_bD6VaFxrksocvFV07BW1RxwmQWlwaySZGxmbbeQp-TV-hxCIqDkqacyyJJJL6AT59bSOLhCobtq1A0O64DEdz5x2xS0m_j50W4W_DAEXtT1poBJuSKCbHe9WkjOrYEpFLc3D1NZRY9ZGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروسی پشت در بی‌اعتباری ماند
🔹
در حالی که برخی مقام‌های آمریکایی در روزهای اخیر مدعی شده‌اند ایران تعهداتی تازه دربارۀ همکاری با آژانس بین‌المللی انرژی اتمی پذیرفته است، مقامات ایرانی این ادعاها را صراحتاً رد کرده و بر تداوم رویکرد مستقل و مبتنی‌بر خطوط قرمز کشور تأکید کرده‌اند.
🔸
محمد مرندی کارشناس امور بین‌الملل طی توییتی نوشت: ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید.
🔹
اسماعیل بقائی، سخنگوی وزارت امور خارجه نیز این ادعا را تکذیب کرد و گفت: تعامل ایران با آژانس بین‌المللی انرژی اتمی طبق روال جاری و منطبق با مصوبات قانونی ادامه می‌یابد.
🔸
ابراهیم رضایی، سخنگوی کمیسیون امنیت ملی مجلس هم در پیامی صراحتا نوشت: گروسی را به مذاکرات راه ندهید؛ او از سنتکام نیز وقیح‌تر است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/444212" target="_blank">📅 08:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444211">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaY9DGnsODutXkVmVmbtByi9BrcRoAzuGknbRlpXq5bH6Ph5OM50_pllhG3NJWm8qdlIbYEedQy0s1c9lH9dWxaHVu4fgi5i74b8Aysm6cUaxChmrSUZrO8NG8QWGGcDHpNC56qQm-UVePhigwRY6iJgQfQdhu9ATsjJyBr8tPN2-BrUfgC7ofJcGG8Uzwd0HvIrICLhU93vewE-103WXf8JdUvwDNMNw2YVu1TN2qDd8oB2Zesuk7zY5Nh1aNJDotSe1rSP_tIihUSUgBnxiEPXVgOs84OS5jn3lQbKndvy10_ofI2uC3Odr-09-pHODgbWEMOsH4SPww6tSFk7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نان در تهران گران شد
🔹
طبق اعلام کارگروه آردونان اتاق اصناف ایران، قیمت جدید انواع نان در استان تهران به شرح زیر است:
🔸
نان لواش: ۲ هزار و ۷۰۰ تومان
🔹
نان بربری: ۱۰ هزار تومان
🔸
نان سنگک: ۱۵ هزار و ۵۰۰ تومان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/444211" target="_blank">📅 07:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444210">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e0c191c12.mp4?token=o1um1AYpIFqMXsn31Gr9bB-5Mzj4s17BYfWUidex3zcmm30Ut1HHCwLpivC3_uuLIQw1nT0BzuKWguAMkXOFeyss_rMhEf_7cBYCxQ_TnI7JY_DV5GZrjMkfqf87KVrO5-L_QTG1oLe8f57YnxUMxYAKmdgWbrokjPzdt85XEzGM26UJ2b8PUV6EXP_vuxR1RaNAgCl48gTaQuIwZ7jECPDUeTlcUOUvWVmTBu83P9MuBLTCyoDmAppoOiXesHtmmP3FOsBuE6Px9uWv6aNbyEAP__vpu201PoNNL90eKCUMc5SbK9_Y-UhGirAXy7tEGneQ8emkS0x-5wD59GRAUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e0c191c12.mp4?token=o1um1AYpIFqMXsn31Gr9bB-5Mzj4s17BYfWUidex3zcmm30Ut1HHCwLpivC3_uuLIQw1nT0BzuKWguAMkXOFeyss_rMhEf_7cBYCxQ_TnI7JY_DV5GZrjMkfqf87KVrO5-L_QTG1oLe8f57YnxUMxYAKmdgWbrokjPzdt85XEzGM26UJ2b8PUV6EXP_vuxR1RaNAgCl48gTaQuIwZ7jECPDUeTlcUOUvWVmTBu83P9MuBLTCyoDmAppoOiXesHtmmP3FOsBuE6Px9uWv6aNbyEAP__vpu201PoNNL90eKCUMc5SbK9_Y-UhGirAXy7tEGneQ8emkS0x-5wD59GRAUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گردباد هولناک در روسیه برق ۵ هزار خانه را قطع، و ۱۵ نفر را زخمی کرد
🔹
بر اثر وقوع یک گردباد عظیم در منطقۀ سوردلوفسک روسیه، ۱۵ نفر مصدوم شدند.
🔹
همچنین این حادثه قطع برق حدود ۵ هزار خانه را به‌همراه داشته است.
@Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/444210" target="_blank">📅 07:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444209">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNhDDwDYgBp0C1bIr64QH9Ck9nMSuYJwRqJG2y4vhKt9fcUzALyhpk6YOZNSynlPbmpTZVC_fAR9hP-OP7QlNu7fbzITSu5CsY8gCBtHKcIxy33zFsMm2BHvgOHA0uhiI-sDfiGm5i645y6F8krHoLAJB3vTN5EkfFqHZqBOK6sAdG5dvclSCEpzf5WpZNPxh712mBM9hO72-QsMmjzoHRFJHcAofj-WhmU7DMHYMbsVhqcd1ppXY15MdT3sxjEAn06YjEJuMY7aGhtsgolaMqp0VI8DEdTCADH1ESVSb0biI2CWcZixfrRbZazEob-jfGDyB_8XcEAC5irxCLlo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو هیئت‌رئیسۀ مجلس: صحن به زودی بازگشایی می‌شود
🔹
سلیمی، نمایندۀ تهران: با توجه به تغییر شرایط، آن دلیل ابتدایی که موجب می‌شد صحن تعطیل باشد، دیگر منتفی شده و ان‌شاءالله به زودی شاهد بازگشایی صحن خواهیم بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/444209" target="_blank">📅 07:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444207">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMPoE6WuZwHMQeFsKMxvs6_T5F8kxqEK3V7k1EB-W6CpVGH1DQGQnJE2N5syvnFMstmyiCk7t3RDYuv-IZ9NgWhrZ95GqF-LvS7VJ5QLEn2kdJ3KxR9a5vB-291jzZffsudhUTrILw5MRl-F3TWkQxgmkCZ21KvqwpgMwo6yumLeg0GFNG3QshdUw5ErX81nZCMFWiqZknTKMJo9vzkfOPP2ma1MRbxW3MPJqkPHeSa7a_TcE6GXfkq8vfXpyawxjRmewtlrxH4eR5KCdcHNABri-nqhAUbRYgC-FFTBWvsxzQJONkpSNk_-nw1rRBNfCI35WflDib_jR2JVCj2y4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تشنگی آغاز شد
🔹
روز هفتم محرم سال ۶۱ هجری، یکی از تلخ‌ترین مراحل واقعه کربلا آغاز شد؛ مرحله‌ای که آثار آن تا روز عاشورا بر اردوگاه امام حسین باقی ماند.
🔹
تا پیش از این روز، با وجود محاصره نظامی، یاران امام هنوز به آب فرات دسترسی داشتند. اما در کوفه، عبیدالله…</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/444207" target="_blank">📅 07:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444206">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOdAdDZCUCLtAiTeX-mLkWbFIo_80I1lOFRugtBOW1A70SvvgxNGlNdtC7I7DXHQk6KUNYkEkidCy6gsbswzz1uP-6uvm3p-EnWwKFxS0415EDeiHJ2xxLfbZg1gnuFswfNfM1hfkC7I_poIcoTTLcZLMPJYd_HmxqvVGZ2LBj8vrHH0oGaMLo8wHBygKjlS3APfC8ldQT65pxhRHg49TC5tJFN2n5OEEI9B5qW_XZv5ba0BZE2_fR7-SBi9n5lr8aqs3OJrlJMUxIvRjhVW95kPQjodRHa3w9gEMdyuGNtzKp5Ur_0_9LPgV8bGVU02Y0sUYkCAvIo_0qoESiWkuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جدول‌تیم‌هایی که تاکنون صعودشان به مرحلۀ حذفی قطعی شده است.
@Sportfars</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/444206" target="_blank">📅 07:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444205">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyTn0Et2_V_49yIRM0osdO3z32s8qIcdtbEIK10Zzr_bdNnsClkQlwGJ0OKLgPfApQiOpS3VDN6SlPAJg5tNA_Vj-ulJiyXHV0RQ5_72uwmwmvfcpmIPAi300utZ39J_9dpKEWHXQmOZo-L4Z90MoOJg3xQU6bXEp2q2DyYtNfRq_6BKT5-qUia5__TdlFoPzS7nsPtqRKVWE8BfAWBnAVf8TpjyyRjL4crqE5ncBO7XOb5dx0nsmqp_aIxK0Jm_ya1H0orYlItg_7K4KE1QeUYi2FCwedjTYopqvdQlfkg_0rSqZjr2mHPPJ-fBfx5-ZuV1PWNA2Z_N5pLTxZYGGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چادرملو در آستانۀ انصراف از بازی با پرسپولیس
🔹
باشگاه چادرملو هنوز تمرینات آماده‌سازی خود را آغاز نکرده و همین موضوع باعث شده تردیدهای جدی دربارۀ حضور این تیم در دیدار با پرسپولیس به‌وجود بیاید.
🔹
گمانه‌زنی‌ها از آن حکایت دارد که چادرملو تمایلی به حضور در این مسابقه ندارد و احتمال انصراف این تیم از بازی مقابل پرسپولیس دور از ذهن نیست. هرچند تاکنون هیچ مقام رسمی این موضوع را تأیید نکرده است.
🔸
این بازی برای تعیین حریف گل‌گهر سیرجان در مسیر انتخاب نمایندۀ سوم ایران در رقابت‌های آسیایی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/444205" target="_blank">📅 06:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444204">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee8416b335.mp4?token=MEmxI2hX94QvYqGJh0WvdhUIzPwDP13QPvymXhSWbAaPlqtivbuSui6AXvC4F5sSTFcAq2krG0kzuqggcp0ZleBQ2oAkGn4yijxdutAY1JyGsF4-izX7f7zfPdudNeliGxmnyTbH1uOzv9ZOm-0LBsE5l9T4Sphk4ZRFpnz69fFZAFFiiKbZg-VlxTBt-6HzUZeUmnsNyjKUntMnM42J8YybOc1uREnLDKHjSVbJowhkrwLB8-UmpUwXY-Asi0-46i5aV9jYtu8hWSMix12BGQIX8eyemVNs9dhpIQMXIJqWDm7UgSROmJShBdPuaJIR4zjbPNR_zOuXfq2OfrgU-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee8416b335.mp4?token=MEmxI2hX94QvYqGJh0WvdhUIzPwDP13QPvymXhSWbAaPlqtivbuSui6AXvC4F5sSTFcAq2krG0kzuqggcp0ZleBQ2oAkGn4yijxdutAY1JyGsF4-izX7f7zfPdudNeliGxmnyTbH1uOzv9ZOm-0LBsE5l9T4Sphk4ZRFpnz69fFZAFFiiKbZg-VlxTBt-6HzUZeUmnsNyjKUntMnM42J8YybOc1uREnLDKHjSVbJowhkrwLB8-UmpUwXY-Asi0-46i5aV9jYtu8hWSMix12BGQIX8eyemVNs9dhpIQMXIJqWDm7UgSROmJShBdPuaJIR4zjbPNR_zOuXfq2OfrgU-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شادی وایکینگی بازیکنان و هواداران نروژ پس از پیروزی ۳ بر ۲ مقابل سنگال، و صعود
@Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/444204" target="_blank">📅 06:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444197">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FqPltEaefDyyhRQ0a2kWPtmBA_Fg9uDSQAEHjk2gfwDMBWmnby68OthhAkBIH1DZhor7AI2gxpwaQc2HXm-jLhgrNe3dqLAoylZGLFRp89choZtvzlvvXKFzd7I8lXihmcfYkw9Eb5U6FKCegI1ylhG96qLxsPB7ti7zYaqvKnXGrYF00qfSa-OSxpkfRojR9_1d0tR5zbY0ZUPrGTfc2go0pT3uYnzW911Ab-5xwP4RVY01oZhsLXxcuhyLkTBmRF2OHsiRxEvfzyghO24kHTckzNhxflbciyMhfFlh00NN9etm9nX3dQmPifk5bWQKKqBDWft2X9e5fnWbdCgiqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k9LhT1JGUFPxORnFCkGN-A9qgEFFYyiGgHYdcxmPIDlg0B6OavLUEcPgJRTak_Vse327lWDViTlExXK5hGa0R6mMK_96ruESctitjUHXUEaTLo2bVjOO22RkiL7Tp31hQQtT01sKzfeGKoX7c8lRsvn-17ebyqhnaGE8SdqdlYiHkVC1O7iQEI7V6m7Yk5tTDwbaC6DBwZNOX_A3rL5b0KMEAsNDBVZGBHzXaEdYOBzUeNV7pzFD1t21UdOHQDqZ08SD9MqDhwBOTGgeC3LYlDrrUxPi2oVELYGh2Dpir8GS3NLFA7HevrKKZ3J-wkLaVFKnrJZOBmLNPZP970gI_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QsjORPd5aiUudovyvwoQ9adEbrRED7_0VrajRk04YasFpUnGSuRC1Q9kelTXb1JWJLgfGN-ZUEEqHb3_RZ81l_7MVoPpZDzFmOV1x1SD2GSI54zptwlIb5k8lmOjngjVJ32rSstBDA8_KMBkpOT6s9BUkqP6N2b3mAS62944pzCa77UpsG66jxVv9PDspz7VzryWz72ayh_JPLlfuIb5mWxANUEVzrXjNNa89VGdv2BNIR3bpCyYm0cU_V99uZtn3shUsfug1ZCwVVfF4JJW3byb4-kWJ6rs4hUdLHqOMSfqwiaevpH9gcD3WxUifi_mzNgZqA5di-uvK9lli9aFuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/seY6eu0clI4DmYR4QdMABOph8Y0swDpDJ5N9BzXpDYzxWkMgACQrOlbdWzSTvKE5CRLMPDP922lyhi7YEdkgjxAp-qmCj4EsVQQ127U8jFRHdRR1BAqLRjfCDSPkkCfclWSaYBJ70-OF5Ohwl2F58fO23S2p7nN5JSpa9wen-NTmbuXwMTFv2PQY3S7-aQAAFQhxFBpyMeQnMe2K05S3lZGwEVtpQj5C13xLE5fBHLGWwF1P9F1KtAXRVAYH4KJXTvFCDbTKFQwn1P8_jExEvF5TpbP823NSE9qL9K9bDfg-WBQ-j3L0hT6QMqa--lCXOW4x_y6kCGHBB5Da4cL8gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uiCbAS7QKLfXoQJOPe1yUulrYcG3cWmLdJISPYM6pL7TJCOh7OFk-XGuXxxiFhQXJOCHkBxLu9tVKO5kqJR6hYivhPzwaCsJfbLeVvu7wnmsOINxxEO8yfYzcoTgGqgdT5swkwVfcNcQk4dvYT2i6U9enCEIdokHiNVFcliO98k16Ycjp5iRCEId8cRpnXiMDT7mDuYBk7-0YnHT1aQB-iUtow4fthZCJnXN4uMjFRV2pfXyuTVKmPNPR6fJcvk8soNGolQZvQk_wyydPAGoMMINdp-4KeKeS3wNEnt9gHnIEdQbIYq5yjw6URRmBYS1ZyhC6aRg93gchpyErysHbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SU3dkHFm1pQn88pLxyPGvTkOJMJyaZ5yxSR0kcX4K2r6IqsWeaTvp2Jtfpkc-OG8-XASt-m5KKAJV3mzyrwfR_FIsf_G4fcg4RAfPl96hj71tEWReT6WE5TzTuxQbswnqawUR1gZurO1R3TmupTjrYKjWjsZ0QDZP2HaBv9s9S0FxfaVFk1MM1xEfQ72ZdsbRCp61DK48sgRijggJBPQsx8sq_GW1fNAJOzR4oh_CzQB6xOQtdAlKypyO--4p5KMKhyJ1FvMxTfoVXJiZs7tGVfTsHc5dYQTeB6aw44EfVWj5z71UX4DRvstErhkIJT-s_r6Yu9k1jWOleHzOaD0dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CjBPrnSUdCCR35dvEmxJiwITSVdqVOe3IT5sXwEh8yHfCcDYEK7H9NKV4hmTijZEUz50By-qRT8_wmqIBcjryB15YDih8exo123c9J5hAPEHZydOzpOxLKukAVRNGBFbMQRZ8HxWBu001favXGFVM9aROOuEQyX47MQdZD-dXBPXTWumLB59oJRl6Fsk61EMRImXb9NbZlZzCdm3S_InibAz7Qp1GZ9iVmh7nG4A72l0UQDE0szRs2QTbpWcsRQhSJ2fxPmFwdTyJh99aj50YN9avjeg9VWpjRWKUjESWZejfns82mej8LmaLAwmFF3a1wXFWnjVMpt3r5ys_oLQ1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نذر حلیم خمره‌سفالی در بندرعباس
🔹
پخت حلیم در خُمره‌های سفالی سنتی، آیین اهالی فین بندرعباس است که محرم هرسال نذر امام حسین(ع) می‌کنند.
عکاس:
رهبر امامدادی
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/444197" target="_blank">📅 06:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444196">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خبر خوش برای دانشجویان دانشگاه آزاد
🔹
دانشگاه آزاد برای کاهش هزینه‌ها و جلوگیری از سفرهای بین‌شهری دانشجویان، امکان برگزاری امتحانات پایان‌ترم دانشجویان غیرپزشکی در واحدهای دانشگاهی محل سکونت را فراهم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/444196" target="_blank">📅 05:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444195">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBC85v-B2XUijtpkk4-MGkhVazya4uZONDndeyjYjAyexRIlXGM82ziwMt6PcAwhbs_bbESe32KL7OBcjy2UVXWl6kHmlat37jWuhPnXgl46xqfzBeWXNpjsE5e9jyF7bWmkbLlhvP8vuPRu60K8aYF_E0mWzczuzJhfclZdoq1x5t7oncC71HFeqLsrKllp7IbZ04i0mLgSIfpcgcfbR0jIZcp2shSmgT2x0PREsMUVjrN12mn66nyZ29zbhgtOwVpeksb0NsNOXTSIhuCp7a0f708y41DS_2Rfkz-kb3xIMrxMsZaEEL-XWQHuY1GztFfgM1jM7ZaCjd6CVM234g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهارمحال‌وبختیاری؛ بدون دریا، اما در صدر فهرست غرق‌شدگی!
🔹
در دو ماه ابتدایی سال ۱۴۰۵، ۱۱ نفر در آب‌های این استان جان باختند؛ رقمی که از کل آمار غرق‌شدگی سال گذشته بیشتر است. استانی که دریا ندارد، اما رودخانه‌ها و استخرهای کشاورزی‌اش قربانی می‌گیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/444195" target="_blank">📅 04:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444194">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ha7pKrR7WKZMRS9nZswL4l4TjRriqNBYVf9fkWQJ4fRnPU1ADILn4SulwsDEcr9G_zt5wFSfzV3-T_X5PIvQPx9QjvIhB78aDzqB0ELcsu6kQOsf2FkGcxikKmZCERLA6_FKY_yT0OqrmvDlEr9G8Prs16b-Q2tRUgUCSR-nXOQgKjPWifQ7GcPh9_tO-0uYtnXvhuqnl6bo7eTpOJ1TfGok5kUZSTZYbkfoxmi3kwhcGrphwEDGZFQNpzCQ1pR-nNGfkPlBrqu_UmyUGjyFNC8evMGoks5Tbd-lERSzOMw6G0Vtf0EhdE0Ye7AxzK9unK6w1yIKWeXLcCjtIRVfQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسوی‌ها با سه گل از سد عراق گذشتند
⚽️
فرانسه ۳ - ۰ عراق
@Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/444194" target="_blank">📅 04:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444193">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7652da31.mp4?token=Me5p7zLK6y_k1h6YcvKW8jDtZhly36oPhW3DmL1GKzi9UZZBsEQJdAFOHJhCS0PKD-zSh4BvQpqCR2c55JjLCHjp9gmh_oQIumatzsc5Z_67T2r5c3HQqN48wgMHclWWtcicBACH4K_AHKZiWNNipv1MtOR7mJYwh7dUI_2l1vQBgm3qqyF6Z6-C8gCmZYdq4cP5aicpJVYu8bkIRvAJYUjFNFkgn0ltUkOCCnV03tkjj2m_nfiS_nPUnfMRfs6Qz4AbABj8BBVL8w1cD-_4uRGsSllIbtrXKRiHITal_RPUYPozX2Ahv0syW825H98R9WNGWG66SbGxOzt3Hen4xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7652da31.mp4?token=Me5p7zLK6y_k1h6YcvKW8jDtZhly36oPhW3DmL1GKzi9UZZBsEQJdAFOHJhCS0PKD-zSh4BvQpqCR2c55JjLCHjp9gmh_oQIumatzsc5Z_67T2r5c3HQqN48wgMHclWWtcicBACH4K_AHKZiWNNipv1MtOR7mJYwh7dUI_2l1vQBgm3qqyF6Z6-C8gCmZYdq4cP5aicpJVYu8bkIRvAJYUjFNFkgn0ltUkOCCnV03tkjj2m_nfiS_nPUnfMRfs6Qz4AbABj8BBVL8w1cD-_4uRGsSllIbtrXKRiHITal_RPUYPozX2Ahv0syW825H98R9WNGWG66SbGxOzt3Hen4xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوت‌ها را چه کسی خواهد نواخت؟
🔹
هوش مصنوعی، شگفتی بی‌نظیر تکنولوژی، حالا رسماً قدم به مستطیل سبز فوتبال گذاشته است. آیا سوت پایان داوریِ انسان‌ها به‌زودی توسط ربات‌ها نواخته خواهد شد؟
@FarsnaTech</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/444193" target="_blank">📅 04:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444192">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4df6f5ff3d.mp4?token=JdAUYmd1ZKD_ws0gzTPkMjf9Yz9RQX2XjBIY8kRp8k6OrxTz4DDO4oybQcsaWjym3aHuBIXc2hVrnTDTRzjpWpD-pjs_vgR8FkrLVUfunO5CfOFEFAx1TrN-ZwAkkvcZEmwRWPWcIYHlMQkUliU007jx2C9Q7ZHo0-NfD9DpZSPnEY9_W6v5uKmyGb3jGO--IgYZJAnB5JlIMrdS8cAyryhNR9axeCrqvio8-CVrOxj-0WXCCIItEuHupcaobuTeL7jrg-CJWFlO_z4_BHrQvGAoMo25JySplxuDmK2TS_wnvZVgePSRBHKfwk7TmaxfZohLGJtMBg3BRv9qcPIYoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4df6f5ff3d.mp4?token=JdAUYmd1ZKD_ws0gzTPkMjf9Yz9RQX2XjBIY8kRp8k6OrxTz4DDO4oybQcsaWjym3aHuBIXc2hVrnTDTRzjpWpD-pjs_vgR8FkrLVUfunO5CfOFEFAx1TrN-ZwAkkvcZEmwRWPWcIYHlMQkUliU007jx2C9Q7ZHo0-NfD9DpZSPnEY9_W6v5uKmyGb3jGO--IgYZJAnB5JlIMrdS8cAyryhNR9axeCrqvio8-CVrOxj-0WXCCIItEuHupcaobuTeL7jrg-CJWFlO_z4_BHrQvGAoMo25JySplxuDmK2TS_wnvZVgePSRBHKfwk7TmaxfZohLGJtMBg3BRv9qcPIYoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موتورشان روشن شد
⚽️
دمبله دقیقه ۶۶
فرانسه ۳ - ۰ عراق
@Sportfars</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/444192" target="_blank">📅 03:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444191">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3578b64959.mp4?token=AnRuHH9Xxx3T-MmRtMCNkOZq6WCVVZDX08f1oZC8CnRgWKIZX1PaU2QBk6IiKcTSn9giGThvSkhCUeLJZg7eOiqJBz9q7kMDSu1c8sztg4TjV9pJG0JwrNP6UTbHTtZG2dS7FcX8_B6ppD3DIZ_QUDBOJQYKUt60CCbNJkmPr-k2bmsXMqspN6zGXQzDvbhRopsXotLN7ZwGnwxGZrVjW1ZLYFCWAbC8OuG6YZxN80N5EfI8JN7BsdUoXNqa4ogoeGrh8Qazn_-m1-swzfF7KyHJ5ccO1ZBqLW6Zv2N4kJAlYR0sUm_eaGj1uu60x9g46bvzXwov65rXmwXn0tYO5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3578b64959.mp4?token=AnRuHH9Xxx3T-MmRtMCNkOZq6WCVVZDX08f1oZC8CnRgWKIZX1PaU2QBk6IiKcTSn9giGThvSkhCUeLJZg7eOiqJBz9q7kMDSu1c8sztg4TjV9pJG0JwrNP6UTbHTtZG2dS7FcX8_B6ppD3DIZ_QUDBOJQYKUt60CCbNJkmPr-k2bmsXMqspN6zGXQzDvbhRopsXotLN7ZwGnwxGZrVjW1ZLYFCWAbC8OuG6YZxN80N5EfI8JN7BsdUoXNqa4ogoeGrh8Qazn_-m1-swzfF7KyHJ5ccO1ZBqLW6Zv2N4kJAlYR0sUm_eaGj1uu60x9g46bvzXwov65rXmwXn0tYO5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رابیو، بازیکن فرانسه دروازۀ خالی را به بیرون زد.
@Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/444191" target="_blank">📅 03:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444190">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73b0f3a5bb.mp4?token=WRGPKWVoE0jIsjgkYd_3eHhakr_oDXmo2pdMKJapH8lpPwCCcmyWB4Lt7tR4Q7dpiqXYlLqI9tlekx5jwVX-f1DDI4QlpWKlQIHjOT-fGceaAVE5K3DNso-gJNxVGyGeEVte3pU7n5_yMq_aQqR-ZqJM51HOqDelG0n2j209uZR7SnNPmxywr-xuqq1T1CEo1CvF8IbQlD70aCsaY4xibf1oNGF3KOllsUM_mRghSQgidRhLktubnMOs73oOOjKASkfsnT7s4h7rWJvlaCj1iSexmiA6HtEhamXrx9yZu1cp9Fhuon-4u2vbekAeepy9_hMCXLFYFBo31OqAsmls3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73b0f3a5bb.mp4?token=WRGPKWVoE0jIsjgkYd_3eHhakr_oDXmo2pdMKJapH8lpPwCCcmyWB4Lt7tR4Q7dpiqXYlLqI9tlekx5jwVX-f1DDI4QlpWKlQIHjOT-fGceaAVE5K3DNso-gJNxVGyGeEVte3pU7n5_yMq_aQqR-ZqJM51HOqDelG0n2j209uZR7SnNPmxywr-xuqq1T1CEo1CvF8IbQlD70aCsaY4xibf1oNGF3KOllsUM_mRghSQgidRhLktubnMOs73oOOjKASkfsnT7s4h7rWJvlaCj1iSexmiA6HtEhamXrx9yZu1cp9Fhuon-4u2vbekAeepy9_hMCXLFYFBo31OqAsmls3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اشتباه عجیب مدافع عراق، گل دوم فرانسه را رقم زد.
⚽️
فرانسه ۲ - ۰ عراق
@Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/444190" target="_blank">📅 03:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444189">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfNyloQPv2Ompm6VtfAUB9iZO4SzYf2ZmcLsyt4ZD52V8rxB5X3pirEPPm2HgvQ52HHssDfZCUyzHJVtyY8fST9qcbG0h2JnGWJx3KK1c0CTI8xHqLv6XNOErjzL69SiCwpgHxIksxZJpA3VkTYW2ufNFfVSNtUhwooya9SGAwyRIe-ciPOYBiQd8Ek7IpUVHw3UoL6mWZDvyd7mQxyBQHDQwINiH6WoIrV0SRCjPjZjES8j0tC3VbE-jkb1YhpV47YJqdijpktqZlJ9hBxfFOThT-9wW7LwMIurMJAG1fO42BNp3SERYocdbTme8WqB4k6fZ0xrzvy53yK4fALhTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از تأخیرهای به‌وجود آمده
⚽️
نیمه دوم بازی عراق و فرانسه آغاز شد
@Sportfars</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/444189" target="_blank">📅 03:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444187">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
منابع خبری از بمباران و تیراندازی ارتش رژیم صهیونیستی به مناطقی از شهر خان‌یونس در جنوب نوار غزه گزارش دادند.
@Farsna</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/444187" target="_blank">📅 03:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444186">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMNaJTX8B-J3bTwxsUra7hAXjg08oZCRffyrg_-kRYEHGlfzZGzN2nUXLmnFO3-5FvM1Vr0zfrOU8O0LYWAiYHryh9pt_wAbFxAWJ_4yVMC6Xg_qLIgrZOxT_MQXHTp4JlBU16alNdUJn7t8OWghjqwXeoKT7zgQUfYCEhnaBEM0VGebtejTlVmu-_q3n81mylQzkf8tqoeCTu9mclPuh7UqdjEXZvOqUl13g9eeOopdHwtO6kpzvek0TuPPyq31VcA0S0c6uJrCSCufr1ZSuhIL6laXanW3kZFQz0Z2b_riM1aWdDgi3vMBPY-L24QhXWg3dGtETTWJPcN12dHCIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آغاز نیمۀدوم بازی فرانسه و عراق به ۵۰ دقیقۀ دیگر موکول شد. @Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/444186" target="_blank">📅 03:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444185">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYsHtpzH0M7KiRf-V7U3FyCK1sv-QLmqt5xa6wSqc18UI4pycdlKhATMiSe8SXvSF3KIAdtFooAMKBDVVuS9t5lH8kLGBdluq71OIJhI2Zpt6mR3rLrgrzwN89hUQRPozG-i1ukG8GyDR-9SZ1kH4ZdCj8K-6THI-5WNbPIwt-wfFXqRAcKB8g-THjm3Ym4daKSp8cfBLSDb62pZ-yrxirhPtqlyYOnsxeVzBnm9KfqUnzC8TbFtElttz9joQVyW1vU_vKq9sxwKuMbJQR0H7MPwwS0RSpCId7PzCRQC_u_GawsoCIXbHo3OoDCC73-Q_LPOGwAjs-dIacGbTTZVhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
با اعلام داور، بازی عراق و فرانسه ساعت ۳:۲۰ دقیقه از سر گرفته می‌شود
@Sportfars</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/444185" target="_blank">📅 03:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444184">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⚽️
آغاز نیمۀدوم بازی فرانسه و عراق به ۵۰ دقیقۀ دیگر موکول شد. @Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/444184" target="_blank">📅 02:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444183">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f49b38b9b2.mp4?token=eIe1m5fODk1tr-Bd6nO5Yx0yPpNwCB7v6rZlfCHtpz_oYizMlOw3MSN62pa3oMaG1CJ23v9tPYujr5ogWYGtAicLVn_5vGBB6EZVCucBr8lnI2O4sr1P434nL8ECsoFz-Lu2yWnpRkIU7upnBP7HbbaZOKsdPT9YXxEqk2ntJD0O_TodiCOmVEHLE8xRutCIaLQXZs3oRVKx2IpTSIaUp_9FDg52ACY1pnnHc5pyPTaqsSeapAWrDjCO0uimGczZzKJjHICxomlT1wVkMSP0WDd6A335Q5UbrPDtPeb_OxVIqlndU3GyqYZYJ6k75DQgAvTCICI6TFemeu-cCA2owqkaxUz98hqpdx8lBvmkTlz_m8AcVUoa6b9REFJd7i-KI_V7EAGZfYn87enp5sGuM0ie-GVA3vnPFe3y-DKjoydnnqA7OTP4rsFnpWTM1JX2udYiiZ480VRF7XS93HcCiyFeNdskDkLzVZ_OatedmkcpniINaL9bir6WtBMjdnIi-1ByK1uQqcvsO7o7jqL8qou5_lJnmriwtLV8Me-rif0OkNAWw-7ZtgJ2C4Us76jUptcYc7xJ5Lu1o490Dtv1av47Xo2ejBA0XR88TD2zIUFscbn027--qA1Ep-IXqB-GM7q6YbXkclEOEKlVaRu6Du87h7T3sOAJjssznmqf7XU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f49b38b9b2.mp4?token=eIe1m5fODk1tr-Bd6nO5Yx0yPpNwCB7v6rZlfCHtpz_oYizMlOw3MSN62pa3oMaG1CJ23v9tPYujr5ogWYGtAicLVn_5vGBB6EZVCucBr8lnI2O4sr1P434nL8ECsoFz-Lu2yWnpRkIU7upnBP7HbbaZOKsdPT9YXxEqk2ntJD0O_TodiCOmVEHLE8xRutCIaLQXZs3oRVKx2IpTSIaUp_9FDg52ACY1pnnHc5pyPTaqsSeapAWrDjCO0uimGczZzKJjHICxomlT1wVkMSP0WDd6A335Q5UbrPDtPeb_OxVIqlndU3GyqYZYJ6k75DQgAvTCICI6TFemeu-cCA2owqkaxUz98hqpdx8lBvmkTlz_m8AcVUoa6b9REFJd7i-KI_V7EAGZfYn87enp5sGuM0ie-GVA3vnPFe3y-DKjoydnnqA7OTP4rsFnpWTM1JX2udYiiZ480VRF7XS93HcCiyFeNdskDkLzVZ_OatedmkcpniINaL9bir6WtBMjdnIi-1ByK1uQqcvsO7o7jqL8qou5_lJnmriwtLV8Me-rif0OkNAWw-7ZtgJ2C4Us76jUptcYc7xJ5Lu1o490Dtv1av47Xo2ejBA0XR88TD2zIUFscbn027--qA1Ep-IXqB-GM7q6YbXkclEOEKlVaRu6Du87h7T3sOAJjssznmqf7XU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی جدید محمود کریمی برای رهبر شهید انقلاب
مثل جد تشنه لب به آسمون رفت
روز عاشورای ماه رمضون رفت
یک جهان به مکتبت پناه آورده
خیلی‌ها رو خون تو به راه آورده
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/444183" target="_blank">📅 02:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444173">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qUZ3rIMAZ6R6uMG8gOtyvUFk18L2DYqN8d4dcNzhAG3FnSluy9wtTnQaSgDEhxpW5j0mhoKXHKV8QvEyn9wRBVW42zpJJo9D8E_szH01yc6LlVpALLK1sNP4Fk3Hcu9G3uet9EEJMhKQqZ51za764ar7wOZJTR6MG8YpWgkE0e51R1kBHgrJOBwYlfk-cCMESCPqCbWa22oy6911x-G-D-yQYFQ4kITV43V5S1WkIYZ7U6DNri3oxra6eHy8cbDMhi1RldTrfYBG4PhIFbLL-mqWFq9mgFvhguoMhRdIDU6ib6nxLZ5MKKVHX4J6vE-vew1LHpmSv7GeiHA2MFNCNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSPgUVJiJCacUN3evbU8fUKcG7BiCLCqHVXxaf869VdOHeh0KtC0NVfdr4p0UruNGYbidMYOpw6FD0IMRkfkwo8-LQJpRzvqXJMBxC3CzITYfGyPVL3tsw6Jcebiy3_928B8pA2q60S51WttjODpYCNOIdUxY-4Pz5UDDoEzJTrL3fdi2NXYpXhWGOsfBKitbKoKgiia3qn_Xo81bsdbj51Fc2pfYR0O6XAo-2o-IYATtl6uiRjhOFjga67kteVaIJirNqKMrVKHyPtiPYv2Ocuav-jclkVeB61KEN_vE4gby3Bz37fQdFDQZ5jI5fJz_rWoDb_nST8P--i2M2MwqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bgbn6R7XbTORsTGegYyh6PHmJquXK1Vw6rNKC3JjZmmmnqgv-Ix9LFRomg1Cfvo7xtWfqd7L7f4xAnD1srVkQJRlznaZJNlYZdZhHtak7jaKm2-0cXKK3GGUXFe7TXoQ7pcla-vUBM5MuI1Xk-EHPb_o1_jMBoG7V46WIsZZemUu6ohAVHWIe-0jo3qM1Z3ajnvGGWxgjXSJw6QBk-5nxygyJpo6gWNuyHv0aJTw1u-u42Ch7gJncCpnn70wTkV6RXwoSMkDP0JwCnP1CJszmIShTpaxt0LNBRaSWxJ3nU024_nBOmxEAHanaXjiLfZFuSfH6oGI51T0YfzKox-aAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O3g3o3ACtcgdLJd_K3FIcCH9qcSuNXLT6xUbca-VbIsiC6kGQaQMv3VV0Bk54CI7PV5bdBaiH_VBo3Mh8y5tyKnf-Xk6lCGf9lGgdrjdl5-dNktmT1JZm7R5DpO7uaVpiBhVRN5piu5PpKtG6SDgatgkN3C4DbOYX6bb5TzrxJqcGdBCfWKffuIgbYH8vCeYvuR7tDe3Q8bkQBAmLq5Zr0_M6Oj1bXk8bkD0QrDdRTX7oNWiKvKfG9RL62asO5caM31pVJzokMaiqKG5GC5Pqj2tLEx1DQq7Z494Th9eP5_E8Yvjszm5JDcQ3UNOQeg5KVWy7uiVOzHZtoQ2rIFgHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d8emCcJcdrQrV7YSqRgd6mQgDFxSXXogkD33J8XlCbP6hddLoEtb2aVv2OHPfsNrlSkNLu0O0X72R8qmwOx7kqJevINVXwleknPRExeEIMP9ZPgFqHlW2zqaIcC7z0b9Dq4Y1OZaGeThDLltySWU3q0C1_QhMcAjYvc7vFvW7rphDEIH3CjSjXIXFgNfGuBVdT4kwjrNYUmn4dwLoqASSuNtyimwfZIITbA1-PXjuNoKVdcrynYJcumncy0gtO_IIyb3G5aKVnvDL2tY-tYYaZD2oKCPVTeU6Kgxv239BujU0ASyd3kBeOSgz5kF14Ue8KK6Fh-EgxDhpQOZH5DUkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CvoZJC7yk2v_3MZoIVTGhRzblV45kqhEAX7P8Aw3ZS_SK4mwr9KiDDXEhvoxDn7S9I5assv4S91eJIXgroJcEM-vmgqTWsTo6l-EhpIngxWadJYVYpq1WQK0RY_ZpDbIkb6AajKORDY1f_vy9eFcIAZakL5slLI0cLzVyxlR94U22wy69CFLRHcTtHgewU2_kiSf5xcD7-hbbdYK5af5lgApokNynd3fCsIyfWe7WQ9Ant6O9WDPhNx5ZIDp6roP82tjS-AIgiDl5pE5wkVp7Dlw1Ar00TwKSJP9QUJ6Ewm3QDeqUKDtcQUXYipLcP7F-zfpOD69etSh1H6Pzyg5cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HjNKlMIokKo8aPEguaFxAwPMX1ce6GVYdkRjPlXslkV4Lz6amRFrN1dY2W_VAoe6Pz1yE30oJ0DMyAK_H1kaMj0QFs7p4KHN8HaIyKNpQRKay7ZCUl7jVvz5QFbRyUM0XRIhgUYnvgDTIoZeWL6f9E_WIvzc0I4G1hS2e8ywXpqzteeMYAvl1ay1-vDFxPM-RAXcr_B1Rnlb9WuLuultohRO6osma4_4Vj3S96YT4_MQmtd1kqv9-NKTuee61_MrnKsObNtQBNmtGZ8Rkn3mGfm3oEKeBKjQRldDfLA8MvRSLBlkwGMzx90gt_75BQ86MWp0GkjkGxwrzcp9ZhV98Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IhYLZ0R8BWIToGUeoIfvIX96J75MCqRyuPIoW4ykp01XqiAuUHQvSOPMpc1gHNj7caHwUmxq6EOq_EKn3dGJtecmFg36r40WdIue1lurkhLVUY9dik3USLTqPQls-SE27EdZLn9uTHip5RSOCWXJSgpF01NMvCtvMXAHT3FQJqFITUbZlwp4XjSLeDQm9tKHHxsCZTglJ7W5Fv2LG83iOAFWNSj3s-XNaEVUOvSN_2wLsoVPPHadfGeC-5u-hxbFRaX85tWXCoHqj3Zm5opQIxmK3KAJjjqQOJMVatIHqrDDgCzDvegmRUGFhdaikX6MNY0d5fId_XYolZTkkPvDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J2fzQFG-9nmEpr5y9TmJWLgvI71czsKgkhlvKpvU402vZiAU1sFFTzezFSi4h68sxRX8pwIvxCXVNcSs7FwlLzU-DqpKxqUIQOKIEUH1HUpfUK-VJVwNick3X56CC_Xxq5Sctl4Ad2zyYpcdpXrQD4kqCayyx4FCDvM2J-ChNcz3uYEaXNiF5NFt_bbJzpr24V86u4JT7k812MQthv06KdHBSzIjSpiIveS4K9JR5Y0mUfwbELv11de1EdG4B7wJeBgipIkBIgDKR8AAYxQUKOwhGHFDGaSxYD17yb2y0pQQbOfZfg4IcYdTuq4qruLJ0Ud9PclttV-AaXlU9d-sIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W5dLaPFrEbSRc1ls8_qKdz4LHYR3XMrpTGG4sm2Qhi1vTRgMTLV_Wr_h8kFfcJxi47rllRzYYOSyfqk4833GD3joUEJOIzFdV_Zq7I5FT6WtMtu0VfDaggyaC9ddPY83kRYcGxkVFxqZjzhUhQ9QXp1HfQPvAiK8CcCQeIeMAvWc2IIhO3U4Rq6pjD9Hs2og1tqBlyf2bW-PE2hKGGdomGbJYOkiftfNwTXXKNzv5Y37-IcEjztjZHg3pXf0EvZNzQvdIze2ipplzD1mwqJ-k3zyUh4TEExa5c03YDMScuOixJRiWHTmvGGgH9eMW9MOGcV2lDEqD6z3DlIGr4PvEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین مشعل‌گردانی نجفی‌های مقیم قم
عکاس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/444173" target="_blank">📅 02:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444168">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oux9xJtxxworpRKOqkO0IGH7h8aTCSkp0-V_wXtagI4O1wig8Zji00C10CG3M7NoCL-xPD51MVxnaviboM0iMb0AdhW9ievGM695fneAJwm0h48_IDDW6Q1QJ9SKhYiTvN0iQv_CYYUMHelTB9ldX5z5Cy-ktOg3-d4oevJNo4YzZnPX07Gd_LjyT3XcxwRJ_iarZYKtQXT93IxciPc5izRj3LZQ1ebZ6SB51-i2zaq3hzu0ZXRKClD12ZBbPbiTsSCLyIlGzaBC_MVrcndkOm2XOgJbeHNZvu_PCog-qGu-t4ybbTL38XpZH1X-m2B3Gbw93ag1UGRMBl0QznxQBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XnbL1_HvO8isuVuVs76Q7uljkArUMAhD6X204X_4ifNlhqU0a3hTjUAGc2LLPMrnOJBShYlEnrxo3o-IsRFowixd65Ro0VwPzADHMldW_2HN8xnNpRuK3MnZNM1UoLz8QNCRLEiKLRxi0uMDy6X3qa97cb-8bJToTV-y1cmX5TwdLVWnJ1cmtDsGNuz4b0XCdMPEPntp8q2u2UNvUxTvNYYTMVVpHqDK1jVqobEtHH-tCrljxAKM22D5aasHjDAu4bAK-8h6L3NOnw44kpU2KkfiTc0oP6PU_nJs4omr4u7q2W8-FI7XM-w6eKnHo_uNrvj1WkqKQw439PGHgim53Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y-xLgYPvBBqUtj3vZBYURpW7v9U1M7_W9v0VF2NX5AVCO2TupAGCavHu0ZHMbwqZzNLGcXKfYq9IH6phquSR_wbDafJHFPNHSYdN8tYM6GGwM9tfcFJXzzuzgUf7i6s-4R2Aou0fRootBjk5bvBODA-MLQ3GG5iRlM0F1pM1ubfS_QB4sZvMOYGTu3BdCyi1m_fLQ5Vn7le34U43xR0o_EBLoq4gl_ICCxqmBSxgvVpVebG0lWdSu5heOuKAjLwu1MELO8UDzLd1zgvTGV_Rmf6L_HIx3x8LXx3HosIWHyi8cFqgaO1yBu8RNaRkaZdIIb-KiLjoDq9CmRpqb-jONg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K4sj2lJFLjDLDALIqjH8lHaPsLlZ_fSrC7uMI4jyIABDXT6tNejJEe_ETCCCRWHiUF4tizIKUE9tk7w7zCPv8lB5mEdFZUkVSLbtltEY4toB8K_9673vCxu84MlrqgzUlDDcP_MzGEI6B_JmRL0Tpu1HGVQPx7lqjXy57aZTnQefrz8IXUz-bbwtx8ut0j3gCen1nS6pHVF_tEZfOX99BhbnTGR5ZaiUVErHMCOfuRFSRJd01sOODLrahOSksOFSMNFPofE9pugIU3XiYU7aEtYCD6sKpbZJByI2kEGqPnhvnrzCt5H7UEyQdn-hv7RSp3BkSAW_zBcja38oPYAZ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nVPJ2PqQHfuCVyzTv5xWlea6EwSqKmCZJ_74v6fInNICbiHd3qDhNwUh7RumEDw8LBR6apa1HNp-Hh3XbZ3StVCHF7CjVnV7X2zfnMzntyzWbvHZgV3JO3srw3AJQwY_fnTQaVxVyf4GONizASyROgTSposSaQZCaSWCbbgWjcld6wFG3HQOZ1pAyu8tJXLLC4Q8bboLu1S8WrZPwuc-72ZC9VzTd7i_dKmiNXf-GI_FFoWmVcdrBIWQpXSjly92Pzya82bJjafn_kakW0lerGZYFiaxgfJNKzD4KF-2u_XmIOW_5FpadMDpc12Efla15w8fKe7pggN6Zh-0q4s3Yg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۲ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/444168" target="_blank">📅 02:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444158">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fr7C-3ooeudx2Zg9WSAwNTF6_r0nS4Sp8_nDv_rp347l8vJPs94A-lC43Sf731UsrOLwOQjluB0w4pac1GC_3AiWqRxsSKyBo5zaZ8Z_bNN349HtGzOX-wx4KJ8umhcGLKcN-2VL9usEyzSdte6YpxWmNdVatrLqOEnebESJ3w2KkqDTirZx1SGvltfCLz9EW9-SyYdZgl5ccpBjQ23S5PqrZ-p0co3bc8j45b6FQ_dhinWfCBPBAGi87fLrQnSmHOs9epuhSeZxRDKt48-RdsLXRj-aMrwkIE-pcSo3SQAinJw1hOh0bQ0tDT-SLBNmPsIhKJsKJu2bWaFdW-bYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MlZhb-j7dKQLoZOmcU9lLl9ldvH-Fv_j_g_aJh2jJJymzPutmpG0LdWmaZBBqK2y3Q7yKE4EfHEU8CIjBdjoW3gxn4j1l34g7r67Yvskr_b5NdHHzT-8jH-mpz-BLaKnyA45QaoV-8_JphFODaGVGFAr3_2x7azBh1xXTvzU_TFFqYe1dPCOTiOPMaC1aE5HGMdMfDkaqSMQLUJf01kJFuZTDrcD7-tXsy4Y1jnomVcyL-TpqxJ8LbqbatSt3biX8Xy6fuFIMgplMWf5u8b1F1wEa9EtRfjw3bAsXq-M275-8Zh-oOiWkda2oSKEcdOVDp4oiKyitpjuh19JB6J0wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ohuy3xOLWPL_f2dDO1trCKJ6NIZAWUl0wc0ZL4mEEooqoZ2Da2wIjmjEqKXuDMBW7EEgJbH6xMJLLTmIq34Dv4GXVuUSIe7ptu8pFTuJLDzJn9KS6jhky94fignT8QOvxKgbS8DuArnFA-BKk-MZFC191Cxy6VKNW0poYOWVSFRU9IHaNHu0dFZmsdnAZvhqtKJAlTKotm_FFv94yqOjn9wrfDC0w4cHTRtmf5wP9piuFNbbI68-zUt4vPylIuSMl45tJZpeX27fQhapbdiAR9mWloZh7IvqzSQIjcovKUw-f8G2-igc2PYr94RajJSoQv4GBk4hc76JUSML_Sz9zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knuZKTED0OtG4NiJzDJNBUzcK-pGuopude2Vx2GAIo9U129cs39RfUDi4cZBtKJi05RbDaoIQZfjCXyUlQPpI4R3Nj6Pb7LOe1aMLLdplzzSVTZsDHY0GyXBLMjPx3cCPDR1wNn5ZkKShVlghsvgYokBSrNw_j3DQhLKrDzM3aFZWZaFwXIwwIIl413fCH9YHmbc6_r3BWOQNRiuu5JtaxZp00bPTS5-Z5p4NcVx7DkVWp_Bj9F4_KanwCDFJ0urn2x2NDNdC3GMI2i_7D7Y6Ldzn8pFsPkx7JC9Hvkv3ZpJxgSgb32kSKae2x7k7e5pTIftBkJRd_S1vI_Zma_NPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T8dAbTlCcBaggRqNA86hZ2bySbOHpz4m9Nk8lQYnhMvRTaPWCx1b7DHhvgPW-BlpjlI387a2jSL-Z2aXTm1Dx__081Saaqktkqqlw2b0m4Fmi4HUypVmA_gIAQvrhwigh-6GbD6bvJ70JRFrMu9nbNZYKv7i6D4GxP_IbGyprj8Y-MJzHysLBBxl5ssRdsxOZlxENtZfG-Ppw2eyErT0nzrsFpSqb8ONBRwqb8L64Xe02I7cJy3BpmCVqxPwMnHkWYw_592P7ASyoURhNs_rNEp_-8DaxZ2s63pEEamvTsjrCiefLR7TsiuTVpn85d1S-0bS1FOpZZHOvxkVRRulbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n8uKcGXSryejsvgQ62yS_-nZodbSj1NMVqGxLjz4v5BZ9VbmAki5nCfWYybOMmJvRlB0QjGXHWsqcRlkPbhdJU3xdgpFwn8RZEwhkiOq_7TzfnIvbGO9xQPaOFVizvGtDYbxmIfInMz3hZrZ72-oxdG_A1ghz48ney7YCbTx8wkXMK1GmgbWoMI63x5A2W0sScPZBO75QuyA7CeWdY8cF7a8NU5l3_5MVEGNgl1gX_JE6nUJ2-RVJsBE4JowZ_eHhfpg6VMW2P2_df4ok8u8FC4fzFOoDa3nNSvxgG49ftI_OKv-B7FYZa2bsoEyeXc5MdwlLnFCYdE6dJRPugIoPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cw_P9adgdbIuYFcS4PNiwUaAk2Z-u85gGY7PmlSDwg5wWXKjC-9t1ZzxVVoN7fs7Kx5C2Emcu51h0JaNSmHpnJo_THYcVDHOZE439HivO6_HtRiwEJA1wqWEhs9mYWhrqqOLYYQ4DVp9xfAG0pSAXfOssh_HrgrXs3cX5k8GBG4L-rW9odAS6PddwxdN9z7RaiaJ9vmycNdjCJgjFOnStiEvpBz7Ee-7uCAsNQLEh6sc5DVZzXQcTRy0xvGAdPLvSh0_ZJV-LgHe7kti5IHctLL-lUZXpcsICH8fjeLTSrovo9oVXUX93mAizab3SCNLs9hIbxWOPaYPhrunXxeUAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SdOTemeDyr0vaeJkKVlrK9IvtL5PEfcKIDiKzBNSrONOy5TBwMkmD8IKT5pezuie4WgkfbSPfG1jFtPtGT36OJ88mLe2YhASWHFlg_AnHK5mOv4bEUamac1-s9Ww2Pyn5Qu5mLIXC0jK2foXsGB0GETbBMuJooyAasyi6mWldPNwZPE6y1RjFVV6O4LKjlqUS8HWcHcNoqZWN80p_GgEYqzm_vOhLriOr6TL2NxI-8uRRwHaoDlZQkZ5lvfEGDWQgmDiMwNn8b8jXngr_0obDI1STgt9rkUL-EBMg8Lap2l7CVT1yN_PByW4L63xAx3Ccd-61fwMlO2nEtwHofF1Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iMrXkmADi33FQMsf_VE67rA3c5vOURRU3hJXD8her_TFohuskHNZsxQ7my6XE43pyXancjbNs9-zmktDQnVAz-78DiYZ_AZYH-4UK9TKh3MJ8CdwhIo4Ut4k6W9JQ58FU1r2n_AMncfLJhHj6CYXpaEaFRfkvpr_-No1rn7CZyOYiaDtlf2RWoCODRmRxV0hWe8Su-FU_3COhGVExhrDLMGxrxdrtku9zJfcO9IGVpHw7rQrMAxqvrrnJguQvLzmjl1MX2xWnt8i4HStwsbi8T6VPxa-7euxYWPU4Q0KYSZoV1oCHUKzQ7SGYoPBIXJ3sfazbhVXMruGBrI4pSw81g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDlUS8QNjA6LFuXfTBGOJurFFIcdu-vWlIuoP_jVugTD-B_xHcTOcZnzWnlSgyCin3soFtrfjaV1IYI-1ybSRe_tImKzrjVo7y28qX1EyHKPfaWPFylinSbrCS1StRwycoUMp20xP436-mJLWFwAN7-qgWA7pSm4NMVJiuADKHwSmgAxs_xmObYzSszsY1VvouTkzhyP2yKEVyO93nLkAyx7zqbxmeLLj-lrl3iygThr9QjQilcVWrcJYerCzbLWwbM93Esc2PmgJoUGayD3U3icepAqccRgE-66HFyU78PMFJ9TXiDqqhMDFzTQqjQLI3lyXF5qjOX6hlWNAsNdUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/444158" target="_blank">📅 02:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444157">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
وزارت خارجه از توافق دربارۀ ترتیبات مذاکرات آتی با آمریکا خبر داد
🔹
غریب‌آبادی، معاون وزارت خارجه و رئیس هیئت مذاکرات فنی ایران: قرار شد تفاهمات امضا شده درخصوص آزادی وجوه مسدود شده به مبلغ ۱۲ میلیارد دلار (دو مبلغ ۶ میلیارد دلاری)، بلافاصله وارد مرحلۀ اجرایی…</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/444157" target="_blank">📅 02:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444156">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZCZbMQLnDEK11XlJOr7_HhUDZobqC6mWfw6qh0joG9JZVzHTQjdgPA6YzoKhoNliyEXoLEGEP5t1894RrCK5KBSygyVUPRgdJO-Qw2je4K7hoi4f126ERCWX33I2k1ksVt4q5oE0PjsmRcHmnV31zKsvxmy0aO5rgyEyR1AaKzFd9GjM-y_2BKzq2KJUPtPVMXSystrmQYjFK8v84ZWTulE4Y-K743zqQEOrC04FBR7hebC3lb4dlN2Q750COlVIheqcNuKLpfIlOf18mHCDrm-TWgsE9QNgv1ZdlnGR84TnKfUMTPrmh1MtDxWHLLocp9LSoZ1f0b6wUCNai7Z_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وزارت خارجه از توافق دربارۀ ترتیبات مذاکرات آتی با آمریکا خبر داد
🔹
غریب‌آبادی، معاون وزارت خارجه و رئیس هیئت مذاکرات فنی ایران: قرار شد تفاهمات امضا شده درخصوص آزادی وجوه مسدود شده به مبلغ ۱۲ میلیارد دلار (دو مبلغ ۶ میلیارد دلاری)، بلافاصله وارد مرحلۀ اجرایی شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/444156" target="_blank">📅 02:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444151">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RvGNsYqBeqyLvfQvUH5yv7S_twESpvE5kadQCAERZXn3HR0wa_ZbFxlYbTRKyCsDhBdgH-naIw1b1ZOirxTh6J85BR-3AiYu6MNba4eZRgVJXPFd35QnPs3FXvMZ47uCO22P7r0iOnsGYHhNYVy55K9PfK7qLmbBz0ECQ7Ply8EaWRIsdyHfu-ZAk9MZ5COCD9wK17CsRo9CUPUzI-SsADLb0_12lI7D5QdwWDNpHZLPrhSXEg98KMx7w74PnXe2hQfWaPkwr3UtG-g4QQveA8qfd84_zSJXOHURhp8PRWyv5UGlo89eW72zP7YMIZaK0cbDdNk179lmcKnUfsYapw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uylvHx8ouL1sDOm6gHtMRTQeFNjTdK7p9emLoypf3tV0XH-lfGUMax-6AiavbDzEdg81nuoMh69MVNqKadjZoFHyoiDvlPMeJ46GUFJ0E5cwVrHJQCbjjF3J1zK2kEJa9KoDwy1WtQJwBz7tlbMH0aMYQKM4pDGKueaAfj3kg3VHwHwlx7WAAsmN38Pgjig2mSj4Lf8SUn6sQVPVR9f3BoEgPWxN9gueNCvnU-h2u8K0ZUEZx__STo_D5v7xuQYNurO7i6VoDkj2ooLQ7s2BxoKbtJCdNUv93dWpPu_EzPPpUaizwugT3QOh9xCwH-kwYDbMOiOvp9QkXADhlz4VtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d5bvTRbmjAPWgSOIkeEx8fcILcFibCNTF1gXbdiToGI4qop8NunAjwsxMl1IBfvrOmB5Sefi3cLMHxfRC4wm4eZkzlbjFADPq_3wUbS6HJ0nyD62RxzCNGkTt4i6fH_H4cvI9Lfo2-bQAwVw7ZvRsEZ9HQ4_psOXvH73NDd-4vZ_-exnLmSylFNOZ69OEr68dKOHWdklvBlqTS_5v8RdDsNEdMAEjTM4X80oyLegetEeE-eCLc4ukNG_KTBy8MCPC4NEz8PKMld4T21ugqkamaHK01AV_aiX7dMiHicaQOipJYxUhqA7yRvS1PT7WZ_-yPwhwLtvplTO7CD7UTcVIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LHDe7LTjTJmgWfwxeu4bMz94B8-89LbLrtDTR26u9MIhByUUWoPrPFgNTAX4_MjHt9uqf8IwzB9me91ZlJSRG0PN3l7D5C8-JJvx9TIL3BMxN4-Nxt8x0GI3558A_2c2TgcmzmMEelzaTZN01oinBGmUgVn4OarBUwuFmm9IXCqfvhiWKk2HZFBmJcHylbmy0U8A5guzZWAriT9rJt9IdN0jkUAzaQSdugTpACQ67_nTIUbMBWbU3FssiVlOhGLShMMKW1AkbmvyX9UpAJHlCsq-q5eAjI1dsNtISd2aC232E4gOBbaZLJyrbQumoFshO04FZFu7nHkq9PZXf5GXtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZlV7hV3rEvxSJH_KBo5kWDHYX1l1k_Rb2BeHV7SpJ54vOUWrLROwnMVR22N-9SIrYF5Kt1xOLntsYx7ch5sw6egGwlxhx2jLwmwyk_2H1f8CLng0srA7slRd2MbQX0hTzP2j3B4mo84P7EirY5yZli2WscTdu8549bcFSZ_wbQOQMK3qlCQeab-k5yxi26-RtTcCx3mCiF9muVWS_7zmsi6iah0nAS832rD20XHGBaxRMKhNVlDVrR7-9-4imY05YfooBmc-61TbecV6RRLQkXhT1S124muhFR4xMUVMDTXd81Abot8dfsz3HOSymJYBGO0EvFsWtZbu1p85Sgb6hA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
استقبال وزیر خارجهٔ عمان از قالیباف در بدو ورود به مسقط  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/444151" target="_blank">📅 01:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444150">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4b8757089.mp4?token=iPJg397P15_aaLZuJBeZTLXjRf3aTg0mM3j96ZmYcRcwLuZLV1v5QGT7oLFaEOfizePHcYmap6-u6ZYdTJ9YvrmBKSPRZpNHGL_De5qmteavSjJyM_kxkOGvGwNNnosBZgd2bW_uF2p6_69XAUqedyENoJsccKlfxDk_DWsIIK8tRaL_TdkXSRN7h3D3p-gmYm9DTJNOknVc4S1cbXLYJsiJnaQyGcA0hLb4v5iv2CHup5OxdlsxCQm_1BR54BglyJ3IFqZVfl-6_Aza4es3LqwazKrOPygvt_lCNmXxe-0M_BAGCiiMo87BLXxMC0QSdcKtMVn6g5cx5swUrxjuiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4b8757089.mp4?token=iPJg397P15_aaLZuJBeZTLXjRf3aTg0mM3j96ZmYcRcwLuZLV1v5QGT7oLFaEOfizePHcYmap6-u6ZYdTJ9YvrmBKSPRZpNHGL_De5qmteavSjJyM_kxkOGvGwNNnosBZgd2bW_uF2p6_69XAUqedyENoJsccKlfxDk_DWsIIK8tRaL_TdkXSRN7h3D3p-gmYm9DTJNOknVc4S1cbXLYJsiJnaQyGcA0hLb4v5iv2CHup5OxdlsxCQm_1BR54BglyJ3IFqZVfl-6_Aza4es3LqwazKrOPygvt_lCNmXxe-0M_BAGCiiMo87BLXxMC0QSdcKtMVn6g5cx5swUrxjuiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
شرایط بد جوی و خطر رعدوبرق، شروع نیمۀ دوم دیدار فرانسه و عراق را حداقل ۱۵ دقیقه به تعویق انداخت.
🔹
از هواداران خواسته شده ورزشگاه را فعلا ترک کنند. @Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/444150" target="_blank">📅 01:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444149">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۸</div>
</div>
<a href="https://t.me/farsna/444149" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۷ – کتاب آه</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/444149" target="_blank">📅 01:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444148">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJDazWypxhsNQ1VFgNU7WYWOywd_wTCgpV8oW23KP9iTtXKl5XDB6_ovu908j1P7Riq4KygDTyqt-E_DD6vWz08hqh9yAJXDDP71xvyF0-RUwBws3pm-d3UuJtb-Qg1bjq0KPwBiqJ4oPF-4un8YWFMGwxfd9MvbATaCI109-loQVN4AfI8XkQONX-kv3w_Gbb11VWM5C5hdAKr0nAUdeyIVL9Ju0u727hzoYwaXh0jPgUH7yMY4dtmt85nkaL1ds3WoTUPh6sIV4_O4pbGGxXmm7GOM_1hhugu-duJB6ydAsPp-B7A9ZvV0He1h7uo2BJEFRF7PBatSB7pgvSbqOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شرایط بد جوی و خطر رعدوبرق، شروع نیمۀ دوم دیدار فرانسه و عراق را حداقل ۱۵ دقیقه به تعویق انداخت
.
🔹
از هواداران خواسته شده ورزشگاه را فعلا ترک کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/444148" target="_blank">📅 01:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444147">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b8d941003.mp4?token=JJ9hP2nzJC4HKgnlMZEj6kxGUNkIf-GiZcPZNb1tFJrbXJ5dh4HRTn4aqlEIqyf6Wt28aSOs2kPNtYup99DRIXcfRpLpFNATpwWruT_0Ddhwm5TCUSjQgnaGelXWgR2B5wRqgC5JhBi7KzoAyfT3x9WZtKSFVZ_7IIbKnchp0xpUM48bnuhWRq3WJUkX7inCH9d6MaGDP4MudZr-d0o75F-nocid2EdXSZpcagzg4Ngjxb8okdCCOMjUEmKCAIY1gVE7N5NcZ4Ajr7N1m9fSK9Zn30naRnffuT4E3XwwfT40EXmjnTecYbFuyHIeKjzmHURLh3s2FTNXjym3FvLzjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b8d941003.mp4?token=JJ9hP2nzJC4HKgnlMZEj6kxGUNkIf-GiZcPZNb1tFJrbXJ5dh4HRTn4aqlEIqyf6Wt28aSOs2kPNtYup99DRIXcfRpLpFNATpwWruT_0Ddhwm5TCUSjQgnaGelXWgR2B5wRqgC5JhBi7KzoAyfT3x9WZtKSFVZ_7IIbKnchp0xpUM48bnuhWRq3WJUkX7inCH9d6MaGDP4MudZr-d0o75F-nocid2EdXSZpcagzg4Ngjxb8okdCCOMjUEmKCAIY1gVE7N5NcZ4Ajr7N1m9fSK9Zn30naRnffuT4E3XwwfT40EXmjnTecYbFuyHIeKjzmHURLh3s2FTNXjym3FvLzjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ مبهم ترامپ به سوالی در مورد اشغالگری اسرائیل
🔸
خبرنگار: نتانیاهو امروز اعلام کرد که نیروهایش لبنان را ترک نخواهند کرد. این موضوع یکی از گره‌های اصلی و نقاط بن‌بست در مذاکرات است.
🔹
ترامپ: این حرف را به چه کسی گفت؟ به شما؟
🔸
خبرنگار: او این مسئله را به‌طور عمومی در اسرائیل مطرح کرد.
🔹
ترامپ: خب، ما قرار است نگاهی به این قضیه بیندازیم.
🔸
خبرنگار: خب، چه اقدامی انجام می‌کنید تا مطمئن شوید نتانیاهو اوضاع را بدتر نمی‌کند؟
🔹
ترامپ: قرار نیست به شما بگویم اما این موضوع حل می‌شود. من آدم حل‌کردن مشکلاتم؛ مسائل را خیلی سریع حل‌وفصل می‌کنم، از جمله مسائل مربوط به نتانیاهو را.
@Farsna</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/444147" target="_blank">📅 01:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444146">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">بدر البوسعیدی: با قالیباف و عراقچی درباره تنگه هرمز صحبت کردم
🔹
وزیر خارجه عمان بامداد سه‌شنبه گفت که در دیدار با رئیس مجلس و وزیر خارجه جمهوری اسلامی ایران، بر تعهد به قوانین بین‌المللی و عبور بدون عوارض از تنگه هرمز تأکید کرده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/444146" target="_blank">📅 01:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444145">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3761e2cf7a.mp4?token=tVaTw1DaDji9XU-9nD8dSACpCWK0CWJJN9tJAmOul54eERs48qISszu9fCHVFVNaeFcIAVbMvQzqIjarWWktyr0lBfj3IrSsR7Lae2u_1TFdh4xMzRsMVG49anJkWYWGSQn0SIgmj32-sacZfBtTrdzNtVZZFndZTzjIAxs9q4mgt49Ad4-vfKU5nXpaUGe4U3-WUhF-1P4Pk6VEQbzfKcFZyiqFTyofP1ylpAbaTgSsiEgUryjLeDC59QL5n6RNEaGeBhP-DH7-EnC1W3pRlsIjLacq-vRl99tL8auX-m79vEAj9sppXi5m1qUjXeLLPAbPvOZ4kh37j8Kf1qpITYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3761e2cf7a.mp4?token=tVaTw1DaDji9XU-9nD8dSACpCWK0CWJJN9tJAmOul54eERs48qISszu9fCHVFVNaeFcIAVbMvQzqIjarWWktyr0lBfj3IrSsR7Lae2u_1TFdh4xMzRsMVG49anJkWYWGSQn0SIgmj32-sacZfBtTrdzNtVZZFndZTzjIAxs9q4mgt49Ad4-vfKU5nXpaUGe4U3-WUhF-1P4Pk6VEQbzfKcFZyiqFTyofP1ylpAbaTgSsiEgUryjLeDC59QL5n6RNEaGeBhP-DH7-EnC1W3pRlsIjLacq-vRl99tL8auX-m79vEAj9sppXi5m1qUjXeLLPAbPvOZ4kh37j8Kf1qpITYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: بیش از ۱۰ میلیون رأی قضایی در معرض عموم قرار گرفت
🔹
اذعان می‌کنیم که هنوز به شفافیت مطلوب و مدنظر خود در قوۀقضاییه دست پیدا نکرده‌ایم، اما اقدامات قابل توجهی را در این زمینه انجام داده‌ایم.   @Farsna</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/444145" target="_blank">📅 01:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444144">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎥
اژه‌ای: دیوان عدالت اداری حدود ۲۵ مصوبۀ دولت و شوراهای عالی که خلاف قانون تشخیص داده شده بود را ابطال کرد.
🔹
همچنین بیش از ۱۲۰ مورد از مصوبات شوراهای شهر و روستا که خلاف قانون بودند نیز باطل شدند.  @Farsna</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/444144" target="_blank">📅 01:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444143">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce9296f446.mp4?token=WAx02Fn3r2Sda6LtYr9rsmI4ZUo354MSx8Fkte6ghvZFEifu0YmbIV_CAHL4OAoPeVmotfH_klr-1a-jOgXVQtDqV9he6vhpgwfTRBAt2N_M1D2nC0yHuQwlHS22Pj_dWMMPXANWNcN4d587hAUMkOL2l2bbnNBez178tNsD4fodls2GKHVX5yjh7TT4OO3YWFeje6zcu38fe7tArIIelmZ_cof6Savhd_Uk51fCMhUgd_5HJTrpr-57alFD_rxXrgcfVjZP65AzUXT6rdFqKCgLQlBgZuSPqO7HTB8jlOc9UBG4a2Bh-r9_6tggMExae34HngjvkARBmPIw_qlafWRMeveHAEvd88cOoqXFXf8FWqlZbKBKCI3MpjICbhdHj32vsHMSZHYT6A6ZTBzJe3XIg9CJcSiffcl_rc5ZMz0peIOCxUcyZr5nW_VZINj-1ApWOBlbVtgRxxdO68K2KzCssU8HbSPZvCPIhsvzpfFzHI_sHrDtzJ07TpX3cyh6Lzp0R08P2hWflyHOW4uwLUDkOQKi8T5R1CTvJ1vAHhGWbiuJROL8KTcR7PdJ7IyG1_hQQE8SVXk73BmyI395kmD3a4Sy73ZwV1jb23O5dq2b30VLrljLXS8HpWKuXcO2YXvsbNg2Gz3y3OkBHjlGN_riFRVQaGaE6wSk2yemb9o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce9296f446.mp4?token=WAx02Fn3r2Sda6LtYr9rsmI4ZUo354MSx8Fkte6ghvZFEifu0YmbIV_CAHL4OAoPeVmotfH_klr-1a-jOgXVQtDqV9he6vhpgwfTRBAt2N_M1D2nC0yHuQwlHS22Pj_dWMMPXANWNcN4d587hAUMkOL2l2bbnNBez178tNsD4fodls2GKHVX5yjh7TT4OO3YWFeje6zcu38fe7tArIIelmZ_cof6Savhd_Uk51fCMhUgd_5HJTrpr-57alFD_rxXrgcfVjZP65AzUXT6rdFqKCgLQlBgZuSPqO7HTB8jlOc9UBG4a2Bh-r9_6tggMExae34HngjvkARBmPIw_qlafWRMeveHAEvd88cOoqXFXf8FWqlZbKBKCI3MpjICbhdHj32vsHMSZHYT6A6ZTBzJe3XIg9CJcSiffcl_rc5ZMz0peIOCxUcyZr5nW_VZINj-1ApWOBlbVtgRxxdO68K2KzCssU8HbSPZvCPIhsvzpfFzHI_sHrDtzJ07TpX3cyh6Lzp0R08P2hWflyHOW4uwLUDkOQKi8T5R1CTvJ1vAHhGWbiuJROL8KTcR7PdJ7IyG1_hQQE8SVXk73BmyI395kmD3a4Sy73ZwV1jb23O5dq2b30VLrljLXS8HpWKuXcO2YXvsbNg2Gz3y3OkBHjlGN_riFRVQaGaE6wSk2yemb9o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: معضلات ۴۰ تا ۱۰۰ ساله حوزه اسناد و اراضی حل شد.  @Farsna</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/444143" target="_blank">📅 01:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444141">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3198d874de.mp4?token=Nb3unjZaCf8oqWumAksXhX2UVHd0sf5GXIKLn4ghmyojqHHZOwKf7u7gf16ZL9wBPZEgCrWm6I8ySZvdhH5RfKn7JuEdTXdCvjbvLdDPM6n3n3fjzlAjt2oZqiUZxl28lixkWnth90QAewe2ZS7cO5pVAOr5MjXXQabORKiiYPQL8x3y4KJNR47m3kbmumPif65JrxjC8bAXWTiUPJ0XnYaBd5SqVktSKqnPosAnP3iQgJoUFex-YWDiycNZbYjIIBhnSVWEeIBRgy-UHW-3VcuaFo05Z0RDXvmMCNwnmZpGibFNmc4g5IdY3KOXXrpS_jj0a0BeSvp_eqiOMjHz9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3198d874de.mp4?token=Nb3unjZaCf8oqWumAksXhX2UVHd0sf5GXIKLn4ghmyojqHHZOwKf7u7gf16ZL9wBPZEgCrWm6I8ySZvdhH5RfKn7JuEdTXdCvjbvLdDPM6n3n3fjzlAjt2oZqiUZxl28lixkWnth90QAewe2ZS7cO5pVAOr5MjXXQabORKiiYPQL8x3y4KJNR47m3kbmumPif65JrxjC8bAXWTiUPJ0XnYaBd5SqVktSKqnPosAnP3iQgJoUFex-YWDiycNZbYjIIBhnSVWEeIBRgy-UHW-3VcuaFo05Z0RDXvmMCNwnmZpGibFNmc4g5IdY3KOXXrpS_jj0a0BeSvp_eqiOMjHz9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: برخورد با محتکران متناسب با شرایط جنگی تشدید شده است.  @Farsna</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/444141" target="_blank">📅 01:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444140">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🎥
اژه‌ای: دشمن با جنگ ترکیبی به‌دنبال ضربه به ایران است.
@Farsna</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/444140" target="_blank">📅 01:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444139">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a7a3f7b60.mp4?token=oF8TYim_jQr3SgJ_6an5tmsF4VbhwclsWDdOtAv8-xbG_6nQl3qGmA9cwYW5GmNT80mBNMNHWrZs6XXmloNmoz0IUy5SCvPZmsc7yR8cj4M6QIUVbxGbUSHlLPkWebEl2jwSLQxRYvk-sf7L8NNuoxMi7aqTuguje8njxpeyu_9almp5FOJYBL7FQHUBrhaE8EhJlUojTv2eOFAfGBi6qYJeQc2ikY3F4HQ-nMzrYmH0tSgS9oRhSui9sY9vDMMHLdOr5um2JqImD7DiC1ZHaPZeZEoMQbFM6oNIoZKA4POj2wKTh0SydevlKoMPq67_fK4lwL4-IIbL74CcyXMNUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a7a3f7b60.mp4?token=oF8TYim_jQr3SgJ_6an5tmsF4VbhwclsWDdOtAv8-xbG_6nQl3qGmA9cwYW5GmNT80mBNMNHWrZs6XXmloNmoz0IUy5SCvPZmsc7yR8cj4M6QIUVbxGbUSHlLPkWebEl2jwSLQxRYvk-sf7L8NNuoxMi7aqTuguje8njxpeyu_9almp5FOJYBL7FQHUBrhaE8EhJlUojTv2eOFAfGBi6qYJeQc2ikY3F4HQ-nMzrYmH0tSgS9oRhSui9sY9vDMMHLdOr5um2JqImD7DiC1ZHaPZeZEoMQbFM6oNIoZKA4POj2wKTh0SydevlKoMPq67_fK4lwL4-IIbL74CcyXMNUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: با ورود قوه‌قضاییه به موضوع ارزهای صادراتی و تراستی‌ها  ۶.۵ میلیارد دلار سرمایه ملی به کشور بازگشت.  @Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/444139" target="_blank">📅 01:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444138">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdf51c89ef.mp4?token=vJ5fj85tALjjNuhsgh5b_Rg3vo8R3Kdp--6ymDq4ItkV2_HetmtBKjkA9tmx4JJp72ylP44WImQfQPVo1RQK2py4gTarAY3AjviWkvlMo0XySEWHtFdlEhG_zmLnrJMFdjnWtbBHhd239Gf7hwrIjhkJEcHfVho_QMQhg8qJe-8SXwhvld1aCpFag9P8PTEraq0Wx6RVYq_moh9OtWTEOHzdliEJXI8ZnY1-au9y7gETw3H_21MROVybriy3ik-50HZluIw3Ba84ktAjhwRM2ASqRB4LPZmifl8ZJiR3WdMz0KbRFQCa8S5OhGn3i9wlgjQrUbi_lBOh9YHQ_CEZKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdf51c89ef.mp4?token=vJ5fj85tALjjNuhsgh5b_Rg3vo8R3Kdp--6ymDq4ItkV2_HetmtBKjkA9tmx4JJp72ylP44WImQfQPVo1RQK2py4gTarAY3AjviWkvlMo0XySEWHtFdlEhG_zmLnrJMFdjnWtbBHhd239Gf7hwrIjhkJEcHfVho_QMQhg8qJe-8SXwhvld1aCpFag9P8PTEraq0Wx6RVYq_moh9OtWTEOHzdliEJXI8ZnY1-au9y7gETw3H_21MROVybriy3ik-50HZluIw3Ba84ktAjhwRM2ASqRB4LPZmifl8ZJiR3WdMz0KbRFQCa8S5OhGn3i9wlgjQrUbi_lBOh9YHQ_CEZKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رئیس قوه‌قضائیه از تخریب بنای متعلق به دستگاه قضا برای آزادسازی حریم رودخانه  @Farsna</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/444138" target="_blank">📅 01:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444137">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vv5E4JXGnyvIqie01dGQN3qpQxdvMQNWbMaxUumNMvcdaRhOKgURRfI0l4TOInpr9g9S6vVlHbShEdmRc6QSANfMWzUrCLRxYR7OB4Djh7GG2YgqKJXT357TY-4ssjHhW4weXy18-dhZoTgTCziERdOEPLYKu1aPDbK6Kns6_YW1BaMKlZIkJ4QOpGd45fR50NZxbdrFutm3WwE6QhL6iQY8fBerkbfldky9cLVgutdomNBL1lbAB-HZ6z3E4-GpwUid6rg1XRq0aT35UtTO2v8SC1KDkTLjlPeX4-rqKvrqUCoFI-cdYzNCY5EC1S3Vd2bx2tdTRRwtPmsTSkmvFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله: با هرگونه نقض آتش‌بس اسرائیل مقابله‌به‌مثل می‌کنیم
🔹
محمود قماطی، نائب‌رئیس شورای سیاسی حزب‌الله: مقاومت در برابر هرگونه نقض آتش‌بس از سوی رژیم صهیونیستی، متقابلاً پاسخ خواهد داد و به شرایط پیش از جنگ جاری بازنخواهد گشت.
🔹
چشم مقاومت باز است و انگشت آن روی ماشه قرار دارد تا در برابر هرگونه نقض از سوی رژیم صهیونیستی مقابله کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/444137" target="_blank">📅 01:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444136">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb884a97d5.mp4?token=pmpdlspKxq6CnNIrv9wD-LhfzF6UY8fGbhaV0Dtfx2JWFbWYAZ_P_wO04NeqEGxrro5mPNwnh1SBfU5jfEqNwMWwfW3Iv4BpNp8XTizznbX4sZIxP5XoMVkuppFwc9onUvfo3tuP5Ym-1ayef4VJO6u04Yry5QCzK4EdsQs4MLFxVLNHOqGMvV-U-AhTBEy7tW_6nBTMexKg1-UcdLGvaB9a-yMuMTJldAynJXIHYNFASyvq0Ypsnkgp5R5024mZH5Z5fI1gFw_EusA9AC61QwKhVdbdhz0g-XD782KskFahtapq81AOOfZiwhDbAAVS7iGn-XTZQFm_jTNzun82qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb884a97d5.mp4?token=pmpdlspKxq6CnNIrv9wD-LhfzF6UY8fGbhaV0Dtfx2JWFbWYAZ_P_wO04NeqEGxrro5mPNwnh1SBfU5jfEqNwMWwfW3Iv4BpNp8XTizznbX4sZIxP5XoMVkuppFwc9onUvfo3tuP5Ym-1ayef4VJO6u04Yry5QCzK4EdsQs4MLFxVLNHOqGMvV-U-AhTBEy7tW_6nBTMexKg1-UcdLGvaB9a-yMuMTJldAynJXIHYNFASyvq0Ypsnkgp5R5024mZH5Z5fI1gFw_EusA9AC61QwKhVdbdhz0g-XD782KskFahtapq81AOOfZiwhDbAAVS7iGn-XTZQFm_jTNzun82qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: بیش از ۸۰ هزار پرونده مربوط به اغتشاشات ۱۴۰۱ مختومه شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/444136" target="_blank">📅 01:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444135">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1834a9bbae.mp4?token=tRIQqV66y0hUmQnW6hrvO7cBRxJMHGdLKE6W6GGX9loSmj0kj4kJMM2LYJfYwLpWvQILapHIeKbzOrzJuJO7L6Xsrh5RyTrB7AZCGjgQgX6e2mjsQdae6mp40nafXjPEvUsRn_fx5_jvJLMQR0gNkjdawEuS2DQFTi5DlEdeXREuEZEvW8bpqybKABl9DDYH90aKGoHWozN4a-zdT4Z_EW8CJ1WegLVZRkpzP5bUuL4-51jJ-QcOTimzIW7jdbi-zPm3D0lL8O_Ncyk09ppKHKu9A3a_Q2eMjBGy0PL5_lVF2Jd9kZ_nllt4920lSQ7mlS5K4H8h7iF2RNjwiMSuDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1834a9bbae.mp4?token=tRIQqV66y0hUmQnW6hrvO7cBRxJMHGdLKE6W6GGX9loSmj0kj4kJMM2LYJfYwLpWvQILapHIeKbzOrzJuJO7L6Xsrh5RyTrB7AZCGjgQgX6e2mjsQdae6mp40nafXjPEvUsRn_fx5_jvJLMQR0gNkjdawEuS2DQFTi5DlEdeXREuEZEvW8bpqybKABl9DDYH90aKGoHWozN4a-zdT4Z_EW8CJ1WegLVZRkpzP5bUuL4-51jJ-QcOTimzIW7jdbi-zPm3D0lL8O_Ncyk09ppKHKu9A3a_Q2eMjBGy0PL5_lVF2Jd9kZ_nllt4920lSQ7mlS5K4H8h7iF2RNjwiMSuDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپرگل دیدنی
⚽️
امباپه دقیقه ۱۴
فرانسه ۱ - ۰ عراق
@Sportfars</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/444135" target="_blank">📅 00:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444134">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171b81be2e.mp4?token=B4Wjrjq5huRsQbeugPejCD5rC5C8JTLVNek-0DGPkhwixq3kiupasex3jUt4teeKnDRV6iTV0wc7lXXUXViHvf2boeiaMRMXbskJHshrtnLCy-hENtCw8fFMBzVCWTnnGfivgr8lcnX2GaMfCqgK-CxTlZzldawAgxDVpQ-a-MhNF8gtRJcbriwTsgccOk6JTBDVbrb3AlBA-F-7UymY_R_aF_sxSfQ5vNnDt5LzVOLLghgLkCGkfSZm8_QsmcZ2DhZJ-BACzrW-j3EoSJekv9rBp0_e2Tw5gyvDC1sFP6VmBFaPsFgoiJiKk56feDZuGITahqxck9HXJsT2pss7Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171b81be2e.mp4?token=B4Wjrjq5huRsQbeugPejCD5rC5C8JTLVNek-0DGPkhwixq3kiupasex3jUt4teeKnDRV6iTV0wc7lXXUXViHvf2boeiaMRMXbskJHshrtnLCy-hENtCw8fFMBzVCWTnnGfivgr8lcnX2GaMfCqgK-CxTlZzldawAgxDVpQ-a-MhNF8gtRJcbriwTsgccOk6JTBDVbrb3AlBA-F-7UymY_R_aF_sxSfQ5vNnDt5LzVOLLghgLkCGkfSZm8_QsmcZ2DhZJ-BACzrW-j3EoSJekv9rBp0_e2Tw5gyvDC1sFP6VmBFaPsFgoiJiKk56feDZuGITahqxck9HXJsT2pss7Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: ۵۸ هزار میلیارد تومان تنها در یک فقره مبارزه با فساد به بیت‌المال بازگشت داده شد.  @Farsna</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/444134" target="_blank">📅 00:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444132">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09f208a55a.mp4?token=cE0BHblVAIikEB4fM_EeG6NF3pKCDY9_k0W3DRkphYZfiQeRTS_B-irjzJKmXchhgdu-VGhCBOXKRW7n1iki0y5Eg3REyfGqQJN8-dOZIStHrUM9jwNGonCKrXg4wemMZYVOB22CTOLevmLlcLBsP6QuEhXAAtQ1f3SCvAxhZ08d7FuAKMuGKy_-vxa31uJiifUHftq6fMBXELQhprtamTnePAcMA42NkOyeFc-IWeVJym220T9uc1yZcULGzTWdXuGb1XH5GSMUfMDDVaeEf7bUiSU11llhT6KQaPFJ7ZtdDeu_MKmyNAk72hEhk8u5-ZykuPEpprqO717JkJdzFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09f208a55a.mp4?token=cE0BHblVAIikEB4fM_EeG6NF3pKCDY9_k0W3DRkphYZfiQeRTS_B-irjzJKmXchhgdu-VGhCBOXKRW7n1iki0y5Eg3REyfGqQJN8-dOZIStHrUM9jwNGonCKrXg4wemMZYVOB22CTOLevmLlcLBsP6QuEhXAAtQ1f3SCvAxhZ08d7FuAKMuGKy_-vxa31uJiifUHftq6fMBXELQhprtamTnePAcMA42NkOyeFc-IWeVJym220T9uc1yZcULGzTWdXuGb1XH5GSMUfMDDVaeEf7bUiSU11llhT6KQaPFJ7ZtdDeu_MKmyNAk72hEhk8u5-ZykuPEpprqO717JkJdzFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: قوه‌قضاییه زیر بمباران حتی یک روز هم کار مردم را زمین نگذاشت.  @Farsna</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/444132" target="_blank">📅 00:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444131">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/946b7c5e0a.mp4?token=M5KPDgQrM_RJLlHwX1uk2NifrKNj__mVILA6U1TgxLsSPkhVtiEs4YA-I8AjvpQFTHPnbQ2jqkaoBNJ57ZU2P_RHuO7Y0npIwsyGqJzLp9q4d-VXVSr8H7iKtmlUjw27rxcN9kPfx3I1AvzyEuwY48n0h0q3f6fcheBzAtmH1q4kIVHnBDZAPUAVknspCMkQs6y3XqgO0RN-h3xtC4ohlMXMtVwQCZV1N0thsyOE0D3CVF781c2XmbXCswc2UtuKu-HZq-r81KKN3rBQZAJuLmb4wUOeaxauDX1V67fx9oHqOQy8n5Z24KIPO9L4ODSoAlhhn6mYqNx4Zqx5BdX7Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/946b7c5e0a.mp4?token=M5KPDgQrM_RJLlHwX1uk2NifrKNj__mVILA6U1TgxLsSPkhVtiEs4YA-I8AjvpQFTHPnbQ2jqkaoBNJ57ZU2P_RHuO7Y0npIwsyGqJzLp9q4d-VXVSr8H7iKtmlUjw27rxcN9kPfx3I1AvzyEuwY48n0h0q3f6fcheBzAtmH1q4kIVHnBDZAPUAVknspCMkQs6y3XqgO0RN-h3xtC4ohlMXMtVwQCZV1N0thsyOE0D3CVF781c2XmbXCswc2UtuKu-HZq-r81KKN3rBQZAJuLmb4wUOeaxauDX1V67fx9oHqOQy8n5Z24KIPO9L4ODSoAlhhn6mYqNx4Zqx5BdX7Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: قوه‌قضاییه زیر بمباران حتی یک روز هم کار مردم را زمین نگذاشت.
@Farsna</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/444131" target="_blank">📅 00:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444130">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EylUmwucBwZlpjft4G2w-Sce-QHxZXQze6i655tfp95K1eyFGnqUMgrY5DUiPz0krw_XKfXYzyggSnVWdaNItkKEbor4c7PIDB2qDAhbVeflepg3HHgBZ9er2Q388HDkfx0-GGQoB4IH6jLe8iVPlB82TY71TUcHeforaBIMA3JK8dvphgzfw0Obk57kKqjDP-3LUYQlFhz3nVMU72G629ftVd81Ej0Kgrv7V8w0qTm1R6XGqDh2F7r_4oepk_y2pAufX04sW_58bUdzOLJHkl25CoGwVmy4avd6_e2NR41W4kP_Xp_KwqHoCtQqcaAcIsTrAQygUHhd4jrBOi2obQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنده است یا آزاد؟
🔹
روزی بِشر حافی که مردی لاابالی و غرق در خوش‌گذرانی بود در خانه‌اش مجلسی پر از عیش و نوش و صدای ساز و آواز برپا کرده بود. در همین حین، امام موسی کاظم(ع) از مقابل خانهٔ او عبور می‌کردند.
🔹
دَرِ خانه باز شد و کنیزی برای ریختن خاکروبه به بیرون آمد. امام از کنیز پرسیدند: «صاحب این خانه بنده است یا آزاد؟»
🔹
کنیز با تعجب پاسخ داد: «معلوم است که آزاد است؛ او مردی شریف و ثروتمند است.»
🔹
امام فرمودند: «راست گفتی؛ اگر بنده [و فرمان‌بردار خدا] بود، از صاحب‌اختیار خود شرم می‌کرد و این بساط گناه را پهن نمی‌کرد.»
🔹
کنیز با سطل خالی به خانه برگشت. بشر که منتظر او بود، پرسید: «چرا این‌قدر طول کشید؟» کنیز ماجرای گفت‌وگوی خود با مرد ناشناس و جمله‌ای که او گفته بود را تعریف کرد.
🔹
سخنان امام مانند جرقه بر روح بشر نشست. او سراسیمه، پابرهنه و بدون کفش به دنبال امام دوید تا به ایشان رسید. بشر در مقابل امام توبه کرد، بساط گناه را برچید و از آن پس به یکی از زاهدان و مردان پاک روزگار تبدیل شد.
🔸
و چون آن روز پابرهنه دویده بود، تا پایان عمر به «بِشر حافی» یعنی بشرِ پابرهنه معروف شد.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/444130" target="_blank">📅 00:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444129">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16c61cd58c.mp4?token=v8KztQSgbSCk6WQX0PgYgRwfIimp_A1_G5CKR7A3Z3_LZx7GY4b7y3svXliWl8zODhDmJroZ6-ZmDZDZyDGbEunO4RkWE5EqTbDDD-IkxnIRZF1MBeWkPeaR5W1O2N3C64vjtgNv0a2l7gJv0hDYvKjaznvyFdJ-eyOBDJcTe3z4Xz-w5I8COU7P30KZzfweDmKm3GCDs1GCjmHsSxUoyUt-z1onDpmcce2XDsw9TvchUkHtUq1oV2HabKph-xX8sn8_YV6fkKamaJ6qL47mPMeotbpJDYIez68bZ67Eoof2krXm5Vl87HE1NEeHGmqHlwxTCTwJT3U9mkGNGhHEOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16c61cd58c.mp4?token=v8KztQSgbSCk6WQX0PgYgRwfIimp_A1_G5CKR7A3Z3_LZx7GY4b7y3svXliWl8zODhDmJroZ6-ZmDZDZyDGbEunO4RkWE5EqTbDDD-IkxnIRZF1MBeWkPeaR5W1O2N3C64vjtgNv0a2l7gJv0hDYvKjaznvyFdJ-eyOBDJcTe3z4Xz-w5I8COU7P30KZzfweDmKm3GCDs1GCjmHsSxUoyUt-z1onDpmcce2XDsw9TvchUkHtUq1oV2HabKph-xX8sn8_YV6fkKamaJ6qL47mPMeotbpJDYIez68bZ67Eoof2krXm5Vl87HE1NEeHGmqHlwxTCTwJT3U9mkGNGhHEOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از شعرخوانی سیدمجید بنی‌فاطمه در دومین شب مراسم عزاداری حضرت اباعبدالله الحسین(ع) در جوار حسینیهٔ امام خمینی(ره)  @Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/444129" target="_blank">📅 00:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444128">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2866ec25ae.mp4?token=lhj3aZxNQymsabBpj2zzSySxp0Q47p9QC9NzMYEZo-Ch6EEzHVKumip6DU2esupWj_xuSQ3bq8OOHQa80uGqWQrchzGj5ZNdtfaHZ4zGp1zjTSUVXrtqPKDzsr6bLA8qOJg6akHoA3Y6LhTO2Hqcd6qvl8WuRsvKzVF378y8mb2dGyS5QZLKnzXTr9rXkGhIYr99505lNLz8zH-DTQPFnV_Tf2NMOpCg8p1Q4gjKCxQxqSq-QUEoQXe-bwrCYYHeg5aMr2JVwMeRnLYiLdUt4VMjwJ5RVW8T-AttP2nc8oWGbWfgq9hvPn0knlONVP2BYBNLgBfAuRD0kvRLi8V34w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2866ec25ae.mp4?token=lhj3aZxNQymsabBpj2zzSySxp0Q47p9QC9NzMYEZo-Ch6EEzHVKumip6DU2esupWj_xuSQ3bq8OOHQa80uGqWQrchzGj5ZNdtfaHZ4zGp1zjTSUVXrtqPKDzsr6bLA8qOJg6akHoA3Y6LhTO2Hqcd6qvl8WuRsvKzVF378y8mb2dGyS5QZLKnzXTr9rXkGhIYr99505lNLz8zH-DTQPFnV_Tf2NMOpCg8p1Q4gjKCxQxqSq-QUEoQXe-bwrCYYHeg5aMr2JVwMeRnLYiLdUt4VMjwJ5RVW8T-AttP2nc8oWGbWfgq9hvPn0knlONVP2BYBNLgBfAuRD0kvRLi8V34w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیرانوند با واکنشی تماشایی بلژیک را در حسرت گل گذاشت  @Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/444128" target="_blank">📅 00:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444127">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ccbc7c95b.mp4?token=WLlXeNqWVtzV5kWCSlan3CDdSB6cFNm1YmnphbPwVGl-UWtSRz7iVEeinwnjlPvrKSoXVRoWpDS2VvVw_VSvhqk46fHqKeZYENZfXgpRPtDOQG90Tv1DdXSWeJnITGrRMESzY4IcbxmNYiKpwOkRU7HR3D7qgWK2lYM2wV8hPTB9UM7XHducLPqZyfQyMhG4JrWund9NOtfEwY3FZFM63X4JTyJb5uHn9D4yEWqU2IeMpK40Jal1fBHlC5fSWiqH1pppBxLluoqXyFDXgStkBY0w7QCURXHixH84xT607AnFdduam0VgqauFCWvmTixEKY3sUiVRi3Pn1LmYoPAN_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ccbc7c95b.mp4?token=WLlXeNqWVtzV5kWCSlan3CDdSB6cFNm1YmnphbPwVGl-UWtSRz7iVEeinwnjlPvrKSoXVRoWpDS2VvVw_VSvhqk46fHqKeZYENZfXgpRPtDOQG90Tv1DdXSWeJnITGrRMESzY4IcbxmNYiKpwOkRU7HR3D7qgWK2lYM2wV8hPTB9UM7XHducLPqZyfQyMhG4JrWund9NOtfEwY3FZFM63X4JTyJb5uHn9D4yEWqU2IeMpK40Jal1fBHlC5fSWiqH1pppBxLluoqXyFDXgStkBY0w7QCURXHixH84xT607AnFdduam0VgqauFCWvmTixEKY3sUiVRi3Pn1LmYoPAN_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: در انتهای دور اول مذاکرات وقتی متوجه شدم ترامپ هیئت مذاکره‌کننده و رئیس‌جمهور ما را تهدید کرده و از حمله به ایران گفته، به ونس گفتم بند اول مذاکرات این است که تهدید و زور نباشد و همان لحظه مذاکره را تمام کردیم و از جلسه بیرون آمدیم و دیگر برنگشتیم…</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/444127" target="_blank">📅 00:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444126">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0bd5d167b.mp4?token=g0tnHyb-r8Fm2aU-gyswXPW6ApMk87D7sNC1bOiIm8Aur3QKwU9jk4e-GSiy4EdDWIvF4F6zNSt6bcrsfVSyKgDRTapyXVmLtFkWFPlh-28cowmrqZNaf42xSnR3DoOwpJu5-5d7AQdb3np04P90_alB2MyF7XYi1YXSJWDcgdJAwXVvwUL69kXm8zJt4aew0tmYMMdiqtcEqOZSzT29QTMAwaIJ2d01UXJ32PnYcBssLd0ggnO3ZntyndZfOUSpNBEHTgV5DHB0HNvUFy_IoPJrrHbcuMDk-_osK1GVxZiB4QBzyJMLSEmpZ4ubb8Uq0v9pewQxR1CF_2gcOHan6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0bd5d167b.mp4?token=g0tnHyb-r8Fm2aU-gyswXPW6ApMk87D7sNC1bOiIm8Aur3QKwU9jk4e-GSiy4EdDWIvF4F6zNSt6bcrsfVSyKgDRTapyXVmLtFkWFPlh-28cowmrqZNaf42xSnR3DoOwpJu5-5d7AQdb3np04P90_alB2MyF7XYi1YXSJWDcgdJAwXVvwUL69kXm8zJt4aew0tmYMMdiqtcEqOZSzT29QTMAwaIJ2d01UXJ32PnYcBssLd0ggnO3ZntyndZfOUSpNBEHTgV5DHB0HNvUFy_IoPJrrHbcuMDk-_osK1GVxZiB4QBzyJMLSEmpZ4ubb8Uq0v9pewQxR1CF_2gcOHan6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: ما هرگز نمی‌خواهیم با آمریکایی‌ها در یک قاب باشیم
🔹
میانجی‌ها خیلی اصرار داشتند و ماهم گفتیم در آن قاب حاضر نمی‌شویم و ما فقط برای مذاکره می‌آییم. @Farsna</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/444126" target="_blank">📅 00:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444125">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/524582de93.mp4?token=dv5fkQbi_r5WfmzGOG8tsid3IJCZbC5IekIzsMXZu3BFMECR8rokxTSLpTWHiJaW81S-CGXMmUXQc_rKAUCeoGysyqq2zslrnZZS0z0b4kknITU-Dl_K231biIJgRtbDCGQ1FFBNL9iXSEFv5G8MB9I--oDBSa5JAgPaT3BudMcBptCvx3BucoXVcUARij1QxfGCmHj7dWzRS9zIjNfPQ-E0lZ2h3fZvPue_vAyZJ60Dri8K9Q1i0UkwgsGXQSEmMaoXSPzMBWrmb73xMxLTpeT0wSvSdttvmWIIlXvvX2HabaZjWr0wxqTzit_Q6tQhIBKEDXPgx8_Sk6yZ20hIqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/524582de93.mp4?token=dv5fkQbi_r5WfmzGOG8tsid3IJCZbC5IekIzsMXZu3BFMECR8rokxTSLpTWHiJaW81S-CGXMmUXQc_rKAUCeoGysyqq2zslrnZZS0z0b4kknITU-Dl_K231biIJgRtbDCGQ1FFBNL9iXSEFv5G8MB9I--oDBSa5JAgPaT3BudMcBptCvx3BucoXVcUARij1QxfGCmHj7dWzRS9zIjNfPQ-E0lZ2h3fZvPue_vAyZJ60Dri8K9Q1i0UkwgsGXQSEmMaoXSPzMBWrmb73xMxLTpeT0wSvSdttvmWIIlXvvX2HabaZjWr0wxqTzit_Q6tQhIBKEDXPgx8_Sk6yZ20hIqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: با رعایت قوانین بین‌المللی تنگهٔ هرمز با ترتیبات ایرانی اداره خواهد شد
🔹
هماهنگی کردیم که خط تلفنی وجود داشته باشد که در دورهٔ تفاهم، کشتی‌ها با امنیت بیشتر پیش بروند. آن‌هایی که احساس نگرانی دارند با این خط تماس بگیرند ما به‌عنوان مدیر تنگه مشکل…</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/444125" target="_blank">📅 00:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444123">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d56dae973.mp4?token=bG-NDrqMit8kS5AAXtD54iX1yOV4GggJmVEAxOmTlq4i8Sxsf9DlqQE2sDlrP-CfqEPt8Ss0Q4G2uCfvv1tshg6u6_3C9xj5Ovbn2bM8opSiRvj3LzFEy_DBu50KKC4FQ-gXLJv1iQfwIR1z5edeUJD7fIgEFbh6-eIUIR_K4c3p-NUpj3CDt2iCVTfNxOdaoJRMbCPy0o5gkAye8FA7LDFIxs5mnoS5C0XdvjAMrYfjMk66oyr0npWwRptUfQSSWOK-nJiI7yGAWRFQ9C5biC_cspk23V3xC34LCZiH3Rb7d2gN-CZxVmFIohHGhsJh2rB0vBb3opN74537f_TRHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d56dae973.mp4?token=bG-NDrqMit8kS5AAXtD54iX1yOV4GggJmVEAxOmTlq4i8Sxsf9DlqQE2sDlrP-CfqEPt8Ss0Q4G2uCfvv1tshg6u6_3C9xj5Ovbn2bM8opSiRvj3LzFEy_DBu50KKC4FQ-gXLJv1iQfwIR1z5edeUJD7fIgEFbh6-eIUIR_K4c3p-NUpj3CDt2iCVTfNxOdaoJRMbCPy0o5gkAye8FA7LDFIxs5mnoS5C0XdvjAMrYfjMk66oyr0npWwRptUfQSSWOK-nJiI7yGAWRFQ9C5biC_cspk23V3xC34LCZiH3Rb7d2gN-CZxVmFIohHGhsJh2rB0vBb3opN74537f_TRHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: با سفر به عمان مدیریت ایرانی تنگهٔ هرمز را مستحکم می‌کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/444123" target="_blank">📅 00:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444122">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12bdb04e6b.mp4?token=JA29Lu4gea2xwyt0rPKswfd6ihl4WP8xpBhjjSvUGLRcmCzpUfnn5PcJ3S12xvto9q6ysKgc6D9IaQ0Ot0v1CMGPULToQq16ekeSwfL0jfz6cA8YolppNcUTjdIUmTB8xAdTCQhcTrsYgObB7BnPlfS40LU9xYxvq6FCbiGkySLBYMpxrUHRw3RrFfjB-A6BamU5H9AM8Gye99drSehZnGHr7SJF5TVAThVFd8ub1vxFBZkxtJnArjTBSvoBfsWG8nZBy3uWPJF00BmeJpQfrVFCIkKQuXcDVioeS8vLWGSD9XRDQyjCqz6R-hM0PmNaDNQ_DfGTXF2kwMCCrYrfXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12bdb04e6b.mp4?token=JA29Lu4gea2xwyt0rPKswfd6ihl4WP8xpBhjjSvUGLRcmCzpUfnn5PcJ3S12xvto9q6ysKgc6D9IaQ0Ot0v1CMGPULToQq16ekeSwfL0jfz6cA8YolppNcUTjdIUmTB8xAdTCQhcTrsYgObB7BnPlfS40LU9xYxvq6FCbiGkySLBYMpxrUHRw3RrFfjB-A6BamU5H9AM8Gye99drSehZnGHr7SJF5TVAThVFd8ub1vxFBZkxtJnArjTBSvoBfsWG8nZBy3uWPJF00BmeJpQfrVFCIkKQuXcDVioeS8vLWGSD9XRDQyjCqz6R-hM0PmNaDNQ_DfGTXF2kwMCCrYrfXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: ما اگر به سوئیس نمی‌رفتیم هر لحظه خون بیشتری از شیعیان ریخته می‌شد.  @Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/444122" target="_blank">📅 23:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444121">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477b8b8251.mp4?token=jQ3mVyLztDRZyhPtydBRge2KW82oh99uROJfk3bJ-5xt_PKRuWRfzQPtRxU-0odsqXr7DAywbzyUajXRNqHD_g1pZOyUR7ys2yfDI1vC-BtqAnzk4vJcfmMQ8oCeEWPOMowh4BMZVt73WKpssFj30JN0r_odqTIWxFEizzYrv3FrIxrigCD-aEDvY_wCXsyjSmGAvKTfb0o_hx6_bOgXWDIMUuDovo39ZwNm2UwXInE72_EwLb4BjeS8BHrFRXIWAfeGHBegm76wTAneOrGIsRP224FsIc6wz3-11zJB1Bdj4VA4ulIjGZP-FPUNEHc1uN0dwTR2k-TO6WL-rrw1sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477b8b8251.mp4?token=jQ3mVyLztDRZyhPtydBRge2KW82oh99uROJfk3bJ-5xt_PKRuWRfzQPtRxU-0odsqXr7DAywbzyUajXRNqHD_g1pZOyUR7ys2yfDI1vC-BtqAnzk4vJcfmMQ8oCeEWPOMowh4BMZVt73WKpssFj30JN0r_odqTIWxFEizzYrv3FrIxrigCD-aEDvY_wCXsyjSmGAvKTfb0o_hx6_bOgXWDIMUuDovo39ZwNm2UwXInE72_EwLb4BjeS8BHrFRXIWAfeGHBegm76wTAneOrGIsRP224FsIc6wz3-11zJB1Bdj4VA4ulIjGZP-FPUNEHc1uN0dwTR2k-TO6WL-rrw1sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: در مذاکرات سازوکاری درست کردیم که ایران و آمریکا هردو باید تمامیت ارضی و حاکمیت ملی لبنان را ضمانت کنند
🔹
توافق کردیم مرکزی باشد در حد هماهنگی‌ها که [از درگیری] پیشگیری شود. @Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/444121" target="_blank">📅 23:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444120">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a821d59d.mp4?token=F1_bYL0hDIy555mEg8Fm2il87P_1GJpmfx-LrwUnfEegU3GGKZIs0enEYH7Fn69ZG4DAyAJmcjMrvyQmX-Eiso59I3sO-69nE-BxFWM7e1Ma1pD3zyTRFd1Q71BUfL-jverpBoNn5OOvPIYPMg45bNGLhNYmNmIAKAfhq0Alp82ThOVADLv1IFWZgeYtqi0xz3ZMjv151ufR3FUUEQGNvvRWawIhOhDca4-AdfQ4ShMtkGZMZHTli6jSzP_moGgQVwWHT8p_9isYnozEI9uEgEGVaVKD0UAOLgjuXGiFSk5KC2URUoiIZ9G86k4tH_Grn_el18hTFb97aqEtPfYoXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a821d59d.mp4?token=F1_bYL0hDIy555mEg8Fm2il87P_1GJpmfx-LrwUnfEegU3GGKZIs0enEYH7Fn69ZG4DAyAJmcjMrvyQmX-Eiso59I3sO-69nE-BxFWM7e1Ma1pD3zyTRFd1Q71BUfL-jverpBoNn5OOvPIYPMg45bNGLhNYmNmIAKAfhq0Alp82ThOVADLv1IFWZgeYtqi0xz3ZMjv151ufR3FUUEQGNvvRWawIhOhDca4-AdfQ4ShMtkGZMZHTli6jSzP_moGgQVwWHT8p_9isYnozEI9uEgEGVaVKD0UAOLgjuXGiFSk5KC2URUoiIZ9G86k4tH_Grn_el18hTFb97aqEtPfYoXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: ما به آمریکایی‌ها بی‌اعتماد بودیم و بی‌اعتماد هستیم
🔹
اگر می‌خواستیم از طریق نظامی محاصره را برداریم متحمل خسارات سنگین مالی می‌شدیم اما با مذاکره محاصره را یک‌شبه برداشتیم.
🔹
تا توافق نهایی نشود تحریم‌ها هنوز هستند؛ پس ما باید معافیت تحریمی فروش…</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/444120" target="_blank">📅 23:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444119">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed9726683.mp4?token=rr_DvuWch2AnTCu0xzeAxYcwFqW8NyWJuw8n6Q1yBJxGjiTiQHJ_uhMKwBYVvsZRtZRv0IuNl8DHmi6SxxRRWR9dYM2MXh6e0aulfOGiZBS2kZpuV-uQo8_RCFEl5nmRc_UThYMFpcdo4ZdeOKZx3wV4aL7jITmoQAX8bMNVXs61Vw5CNn6AwX380h7ofxcr2rJDIAEBWbsCPrXp9n67dL1iQKRz1WtB2mk7Gecs-1M50-Ii8I1qfFO80RqAOOWKFyV6TDTwOpvJCqdpOlbJ4t379mvRdxw-DX0BsqCxU2WCAd7Wo_rXYuvnjZbvt0ZXlrBHgQFYX7r1-4BZPXlqQJIJgiI_zjWSjkA3SKIjfFAtUIN7t3My3bbr0lyAD0UiLjIG6kgw7WjemMH6hZCD73YAE4FtuUATtsSwh7ZUbPsaPvA_yXIuWSdvQxRNEELQK2d6H0TIbyPIhf6HV5IB9RheHdW2bFyH2o-9CUSBtHXnC-R0wNGBSvPA4bLRyqI9yyXUH9TjVPVZNxqEqKuupKNVTuosb9NaZ_d8REVS-knFfCCVpv1EaRwgGV06WpYOiekggcOx7wJQ58tG348ljuA2mKdQglrtcmTB6yau5GcKpTrvpfnKszXsUKAA-g9nF6oy1eduPf-IawXRWymQP8YmY8UBtdtBGgtHJUwxebM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed9726683.mp4?token=rr_DvuWch2AnTCu0xzeAxYcwFqW8NyWJuw8n6Q1yBJxGjiTiQHJ_uhMKwBYVvsZRtZRv0IuNl8DHmi6SxxRRWR9dYM2MXh6e0aulfOGiZBS2kZpuV-uQo8_RCFEl5nmRc_UThYMFpcdo4ZdeOKZx3wV4aL7jITmoQAX8bMNVXs61Vw5CNn6AwX380h7ofxcr2rJDIAEBWbsCPrXp9n67dL1iQKRz1WtB2mk7Gecs-1M50-Ii8I1qfFO80RqAOOWKFyV6TDTwOpvJCqdpOlbJ4t379mvRdxw-DX0BsqCxU2WCAd7Wo_rXYuvnjZbvt0ZXlrBHgQFYX7r1-4BZPXlqQJIJgiI_zjWSjkA3SKIjfFAtUIN7t3My3bbr0lyAD0UiLjIG6kgw7WjemMH6hZCD73YAE4FtuUATtsSwh7ZUbPsaPvA_yXIuWSdvQxRNEELQK2d6H0TIbyPIhf6HV5IB9RheHdW2bFyH2o-9CUSBtHXnC-R0wNGBSvPA4bLRyqI9yyXUH9TjVPVZNxqEqKuupKNVTuosb9NaZ_d8REVS-knFfCCVpv1EaRwgGV06WpYOiekggcOx7wJQ58tG348ljuA2mKdQglrtcmTB6yau5GcKpTrvpfnKszXsUKAA-g9nF6oy1eduPf-IawXRWymQP8YmY8UBtdtBGgtHJUwxebM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: وقتی پیاده‌سازی آتش‌بس و پایان جنگ مشکل پیداکند ما می‌توانیم این را هم با موشک حل کنیم هم با مذاکره.  مذاکره و‌ میدان مکمل یکدیگرند. @Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/444119" target="_blank">📅 23:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444118">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e88fe3f217.mp4?token=Oih1DsRyv4po73w1KpkKU7r2TM-HNPD4vyr6XM954nzCzbViru0x8k35e6ZQu9urvDACCK62YJb7TGkJASj7E0orFDdJM6wZr3mSxsh5-PdrEemjToDuHCp-DXbh7l6B8O3lI_PIpfhcWyJRnPBkHzryS1MPyGv7OsB3JZBzL8fqjMah8p6CnXnwV5xBajwBZeI9OdTLrDzDvIzVDCSR62pl_Nu-Avrtn7VvfTq3gNRddThC47EZj7iPyoIehvm1FDQKlRBxrdlLg6PNOmFEVpKRGHY-Ea6NNTjw024F0VH239wqCdlRmAZuRLHBV-9cX7_VjtL8RknY0lIxTaV52Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e88fe3f217.mp4?token=Oih1DsRyv4po73w1KpkKU7r2TM-HNPD4vyr6XM954nzCzbViru0x8k35e6ZQu9urvDACCK62YJb7TGkJASj7E0orFDdJM6wZr3mSxsh5-PdrEemjToDuHCp-DXbh7l6B8O3lI_PIpfhcWyJRnPBkHzryS1MPyGv7OsB3JZBzL8fqjMah8p6CnXnwV5xBajwBZeI9OdTLrDzDvIzVDCSR62pl_Nu-Avrtn7VvfTq3gNRddThC47EZj7iPyoIehvm1FDQKlRBxrdlLg6PNOmFEVpKRGHY-Ea6NNTjw024F0VH239wqCdlRmAZuRLHBV-9cX7_VjtL8RknY0lIxTaV52Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: در گفت‌وگوها موضوع [حفظ] تمامیت ارضی لبنان را تا به نتیجه‌رساندن رها نخواهیم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/444118" target="_blank">📅 23:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444117">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e8285d04.mp4?token=JhSTdgQrlsL-rxPjeOX95DpN4BxY9AT9K7zZScspl9iNtbYJxsQhOvVilSASQufPW_7tbCH_NImKPqzaG10sFPIeErQXAV7Nfncj89V2xZDsK80DivMu4NLiaGpTb9IwnscuqVv1VIsIuEe_ZvGk5gbQdqVD083OwFG7fJUCMgDokDitff5IfIFSY2oYyjyeHMYuLd8gou9DxOewWWFaZynZpyfe-ArgwOKDFCxxAtzYTonBue4SUIh3Z9bw0HJPQlJ-MarWO3pkBQjR2up_r7IvXBVUkqythi0onVc3KqS6F9aYCK2L2i7JeupWNx87a6-lIN_P0sSoXbO86GeWzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e8285d04.mp4?token=JhSTdgQrlsL-rxPjeOX95DpN4BxY9AT9K7zZScspl9iNtbYJxsQhOvVilSASQufPW_7tbCH_NImKPqzaG10sFPIeErQXAV7Nfncj89V2xZDsK80DivMu4NLiaGpTb9IwnscuqVv1VIsIuEe_ZvGk5gbQdqVD083OwFG7fJUCMgDokDitff5IfIFSY2oYyjyeHMYuLd8gou9DxOewWWFaZynZpyfe-ArgwOKDFCxxAtzYTonBue4SUIh3Z9bw0HJPQlJ-MarWO3pkBQjR2up_r7IvXBVUkqythi0onVc3KqS6F9aYCK2L2i7JeupWNx87a6-lIN_P0sSoXbO86GeWzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیرانوند: مردم ما ۴ ماه سخت را سپری کردند و ما همه تلاش خود را کردیم تا دل آن‌ها را شاد کنیم و شرمنده آن‌ها نشویم.  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/444117" target="_blank">📅 23:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444116">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45811675c3.mp4?token=W14kZGRn85hroQRGiDoHKIooc3ADWg6LtGHvaHNqvB9ZPz6UG9L4zNuNWfSX2Bty_L7-Y-i-pZB1Jjt1WFVBDI_QmeDwAPWBBzoQdJUJ--5gHXaoFP3rMOde4TnM_-hI_yzc84wv44_f8j2aLIt4F7dcQO1fq19fJ7bgGx8pmBi7dVV2vP0eICepZcJR4-eIH7F69-eqTOx2XABqn18q_JYl7SuC8PQf-LYPx8TiRAJ0tfb1zES-FzjTOr0RqKpuUIpCY8fa7YFI_fXbBb2aW9xvCdywAGtG2q5AHH3_zehATdcSKrWCgPMvVQNMTekhS62lSn9SSBLEqJu8RjuJAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45811675c3.mp4?token=W14kZGRn85hroQRGiDoHKIooc3ADWg6LtGHvaHNqvB9ZPz6UG9L4zNuNWfSX2Bty_L7-Y-i-pZB1Jjt1WFVBDI_QmeDwAPWBBzoQdJUJ--5gHXaoFP3rMOde4TnM_-hI_yzc84wv44_f8j2aLIt4F7dcQO1fq19fJ7bgGx8pmBi7dVV2vP0eICepZcJR4-eIH7F69-eqTOx2XABqn18q_JYl7SuC8PQf-LYPx8TiRAJ0tfb1zES-FzjTOr0RqKpuUIpCY8fa7YFI_fXbBb2aW9xvCdywAGtG2q5AHH3_zehATdcSKrWCgPMvVQNMTekhS62lSn9SSBLEqJu8RjuJAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیرانوند: مهدی طارمی قبل از بازی یک سخنرانی حماسی کرد و به بازیکنان گفت اگر سر خود را در مقابل بازیکنان بلژیک پایین بندازید، بلژیکی‌ها ما را له می‌کنند و آبروی ما را می‌برند و باید در تمام لحظات سر خود را بالا بگیرید.  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/444116" target="_blank">📅 23:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444115">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001a8c75c3.mp4?token=WFrRx_GO_owJ0R8Yc2VTa1pScBuye3xk1lWR1XPRWAAHBzxJT3ok4zc7CRutU4uvwUuSuACuWu038123aAuZhhsW_uerrDgtBNvJn_NOITP-vX7gg_Qel5ZLGX7jUJeSFuJK1oOVheZ1xPK7rNlXq3w12OvBNm29ySLYVcBOdeMP3-KTqMqoxGdk6sLX9eWfES599PcSwZPLVcFNrKOfWccyuBJCgh-3RIscZ3hfduQUczUd89R6MTLaifZMq5HQZqyW1Ttv7Ckn0XmT88vfJDiymd-LDX9-Fp21V42KzColqtLbWZ-MggVuZORYBeFTIV0VFRR6VVsrZkPD23A3uakLnE8T6JD2uTTK87UQwSPiSEStrOOmKbymzOtMHq4fPvU9tdo3mGDCNfc6aLaGUgzH6lCv8StY6B_s_-IQzw-it9WDiLeD8KC5J_3dRfS65awqGswhogEMTVudtwJW7peFO7lTlCpW-VIPSKiXTu9duILW_GgTjG4hQ6XSZilq0eZBw4iN5Jvt8LwIhEW5U2TW3ZEl4W4puKgaOO24EAtZx7TrJwCY1xtZUj-bWxEBouiaiwfcGH4m-1g2H6iTIt171Y8WCOfvycRBdexT3ZJBlAzCaEVCfXK9wnhD7IbB3sLTvEyUR-JcZYyvonDv3dmmwEVM5ySAgcr1HuBroJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001a8c75c3.mp4?token=WFrRx_GO_owJ0R8Yc2VTa1pScBuye3xk1lWR1XPRWAAHBzxJT3ok4zc7CRutU4uvwUuSuACuWu038123aAuZhhsW_uerrDgtBNvJn_NOITP-vX7gg_Qel5ZLGX7jUJeSFuJK1oOVheZ1xPK7rNlXq3w12OvBNm29ySLYVcBOdeMP3-KTqMqoxGdk6sLX9eWfES599PcSwZPLVcFNrKOfWccyuBJCgh-3RIscZ3hfduQUczUd89R6MTLaifZMq5HQZqyW1Ttv7Ckn0XmT88vfJDiymd-LDX9-Fp21V42KzColqtLbWZ-MggVuZORYBeFTIV0VFRR6VVsrZkPD23A3uakLnE8T6JD2uTTK87UQwSPiSEStrOOmKbymzOtMHq4fPvU9tdo3mGDCNfc6aLaGUgzH6lCv8StY6B_s_-IQzw-it9WDiLeD8KC5J_3dRfS65awqGswhogEMTVudtwJW7peFO7lTlCpW-VIPSKiXTu9duILW_GgTjG4hQ6XSZilq0eZBw4iN5Jvt8LwIhEW5U2TW3ZEl4W4puKgaOO24EAtZx7TrJwCY1xtZUj-bWxEBouiaiwfcGH4m-1g2H6iTIt171Y8WCOfvycRBdexT3ZJBlAzCaEVCfXK9wnhD7IbB3sLTvEyUR-JcZYyvonDv3dmmwEVM5ySAgcr1HuBroJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیوند ۱۱۴ شب دلتنگی با شور ۸ محرم در یاسوج
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/444115" target="_blank">📅 23:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444114">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39f08f7b5c.mp4?token=LktU5bXPV2qYzRj8UlT5y610Kj6IG8JZIaFQ5JvWZdEqxCFWjRNyFjQAMA2kdFla-UrBOHY9KBGxguO7mJbUPuJmZTjfH1Li4TU1nCJcbFUUcwx1bsdv4VehBa-iQSS4EU04NhKhxDV0RT6qpq-ZwoJuBqfZU7lt2MTIk6hNADcdHCO4P4FmSoTMtNU0Uhe2HrnQAiUb_g_u1HZeXGMLz5MLNDytIoD7g_S_Qp8urhiNhPd-K7uXm6GVDmBjsaXHOOL4yFXpIBZOg-Ix99agffymrL2zSCnpHIqhRF3lh-q3mqqgb0glhsGghKYvABLeOs4hsSiNtwrqBEBLXeHQqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39f08f7b5c.mp4?token=LktU5bXPV2qYzRj8UlT5y610Kj6IG8JZIaFQ5JvWZdEqxCFWjRNyFjQAMA2kdFla-UrBOHY9KBGxguO7mJbUPuJmZTjfH1Li4TU1nCJcbFUUcwx1bsdv4VehBa-iQSS4EU04NhKhxDV0RT6qpq-ZwoJuBqfZU7lt2MTIk6hNADcdHCO4P4FmSoTMtNU0Uhe2HrnQAiUb_g_u1HZeXGMLz5MLNDytIoD7g_S_Qp8urhiNhPd-K7uXm6GVDmBjsaXHOOL4yFXpIBZOg-Ix99agffymrL2zSCnpHIqhRF3lh-q3mqqgb0glhsGghKYvABLeOs4hsSiNtwrqBEBLXeHQqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علیرضا بیرانوند: بعد از برخورد با لوکاکو، تمام زمان مسابقه را با درد خیلی زیادی بازی کردم.  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/444114" target="_blank">📅 23:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444113">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef10148d95.mp4?token=iR2V5wxQoC01n6JH7nDO8QEdLdWMChCogmbucxtMSJanT7BBmG_m0zDMlQfgGmpOqghI_12eh8K0Cu4ns-t1i60fUq56DLVBvdstXNvad03sZktJhDOiS6mogYfeELC2gubYqnGT-XZ2L7D6sK6CPWGcI-1hm9Ff3PULY0wFcJSy2uc8XaDvJZlIoEj1Do8WL-yvg0nkLBON7Izwy4TFYkSCwcNa4txCszEtJzNnpV1X-OEfVk48PItAG6ERrHDNMsmPkNI44a0C3QINFq9VOhq0mfbPxNH0F3GvmPSReR4j9X96q7VtbDPi3vw96qGo_JqtareiAxSNh2Ev7cysyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef10148d95.mp4?token=iR2V5wxQoC01n6JH7nDO8QEdLdWMChCogmbucxtMSJanT7BBmG_m0zDMlQfgGmpOqghI_12eh8K0Cu4ns-t1i60fUq56DLVBvdstXNvad03sZktJhDOiS6mogYfeELC2gubYqnGT-XZ2L7D6sK6CPWGcI-1hm9Ff3PULY0wFcJSy2uc8XaDvJZlIoEj1Do8WL-yvg0nkLBON7Izwy4TFYkSCwcNa4txCszEtJzNnpV1X-OEfVk48PItAG6ERrHDNMsmPkNI44a0C3QINFq9VOhq0mfbPxNH0F3GvmPSReR4j9X96q7VtbDPi3vw96qGo_JqtareiAxSNh2Ev7cysyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لوکاکو به‌خاطر خطا روی بیرانوند کارت زرد گرفت   @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/444113" target="_blank">📅 23:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444112">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5540a0a5eb.mp4?token=fiiRUFBFLSnXq45cjP-o2KTR-453P6G5VI-4b5r16OwFhV6tvc9-eJ2LcP15aq9ASJzxpAxWNv7STRJ3mypKBcVQ2yGQsN8Zwyn7R4hMbCyBttxrlO0m3-5EKhlJ1HKk9soS2G1pGiAyocjkoqrHmHehZZKHiz51gJOTlfxxfX0nOwhSdHUrKnw-N3eYCut_TPfpe1e6-78Fe9GIzOUkDuFgIoaEpvM6FpwKcpJ4GswaQ729is4IsfhkXXIDb-jxk0OSBWz72vt5iDLQPJzR54_QisQIZ9xQh1PxwGXlwHCiihxTF363F0dGoLKFZpZAXf_o7w5d43H941_yl38Vhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5540a0a5eb.mp4?token=fiiRUFBFLSnXq45cjP-o2KTR-453P6G5VI-4b5r16OwFhV6tvc9-eJ2LcP15aq9ASJzxpAxWNv7STRJ3mypKBcVQ2yGQsN8Zwyn7R4hMbCyBttxrlO0m3-5EKhlJ1HKk9soS2G1pGiAyocjkoqrHmHehZZKHiz51gJOTlfxxfX0nOwhSdHUrKnw-N3eYCut_TPfpe1e6-78Fe9GIzOUkDuFgIoaEpvM6FpwKcpJ4GswaQ729is4IsfhkXXIDb-jxk0OSBWz72vt5iDLQPJzR54_QisQIZ9xQh1PxwGXlwHCiihxTF363F0dGoLKFZpZAXf_o7w5d43H941_yl38Vhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال وزیر خارجهٔ عمان از قالیباف در بدو ورود به مسقط
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/444112" target="_blank">📅 23:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444111">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‌
🔴
یک ‌منبع آگاه نزدیک به هیئت مذاکره‌کننده ایران در گفت‌وگو با خبرنگار فارس: ادعای معاون رئیس‌جمهور آمریکا دربارۀ بازگشت بازرسان آژانس به ایران کذب است
🔹
این منبع آگاه ادامه داد: در مذاکرات سوئیس هیچ صحبتی درباره حضور بازرسان در کشور نشده است. @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/444111" target="_blank">📅 22:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444110">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNNMHQA7e3Bf_mKja5jNZkPueHYEKjqKpaWZNGM9z5o4EAeNejGOvqidPrHSmq_Cb7i6I-TPR8BTxbzIFupIZfKWY_uibn8vpCRT3CkJ78mFeeV8tehJemBDIJ6gUAPOHy264lqCPZS4J0-PT3YXSSfBxbWoJSIvqXXE2jhxoqs2s_Pid5lQvvJ_3cIN9QT0pIIxmXoXugzGzF82orOA9g83IEM7pFgTCrlXOHeO749x1-EopP5U1SnArIYsvJ1eDZLUqyN5Rylr_Y7OYX9xBY3OEP4-OCW_C5q6shPB0ncga9M9hiakruBjILOaifYw4jGqWQPJB-VDf8xOcfnVMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از کلوزه عبور کرد
👑
لیونل مسی با گلزنی مقابل اتریش، با ۱۷ گل به بهترین گلزن تاریخ جام جهانی تبدیل شد.
@Sportfars</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/444110" target="_blank">📅 22:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444109">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCH4q5bxjVmuDnNPZdXtWmHiO6n6NKoIHiM8s3JTyB4FZXIOj3D8NkJjpjqGegMLu3yZ-heN2kkRjDKXt9Fy2dqQc2gJt1vYiftN-BVcBI_A09MSaMS22g3FoCoKvZFcbOC0AGgxiFHwD3ET2NgpQoaqHhoCsGNczYlHyt8FFavi7M82tNa1K5m7BdtV24C8ShQJMCo98P_viTzixxXeATwb7UsL9XFWhMnk2pJ4h2UhL97ZYTBgxmOQ09KyW8Tkwf3XPE9Mrk13DKNrxFEb5QIrH-WdCAUwPjxNQnB8x56uVKNfxWpwTemrHjL29ULbHuSQdmDEZ84Mojx5G8uVng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرژانتین با ۲ گل مسی از سد اتریش گذشت
⚽️
آرژانتین ۲ - ۰ اتریش
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/444109" target="_blank">📅 22:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444108">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc13f57280.mp4?token=NjzduOByfdg2mOIoTef9je9_8ExpmtST_fySiW5VRlOfqTViYsLTW1aajS9eS5z1rIlUwC5HfbwJy6vzp4rUhALft2PqONnfcPJT39VoJOtMdZ-9eK_nwLp9xElT9k8HmX68ALrvOkrCc9zDFw7xP7NARPnepgDjyE3jSRRxA2XJt4UWayR8tLFUZc6t6xnVeXoFJftZIfxIUhD4gH1QBZIpBqnG8E0_I9lWem2dbSdkYTizBvRKTcEBnmT1Q9iYQIT1fIEU1C_tI_pIPDYWYrqxjGk2dpSyF9FxFnNr_q8KAjWDRrbUneeZJwJN0JWqZMMscPQmRz2cTHxEuf_UMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc13f57280.mp4?token=NjzduOByfdg2mOIoTef9je9_8ExpmtST_fySiW5VRlOfqTViYsLTW1aajS9eS5z1rIlUwC5HfbwJy6vzp4rUhALft2PqONnfcPJT39VoJOtMdZ-9eK_nwLp9xElT9k8HmX68ALrvOkrCc9zDFw7xP7NARPnepgDjyE3jSRRxA2XJt4UWayR8tLFUZc6t6xnVeXoFJftZIfxIUhD4gH1QBZIpBqnG8E0_I9lWem2dbSdkYTizBvRKTcEBnmT1Q9iYQIT1fIEU1C_tI_pIPDYWYrqxjGk2dpSyF9FxFnNr_q8KAjWDRrbUneeZJwJN0JWqZMMscPQmRz2cTHxEuf_UMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار خطاب به معاون ترامپ: بی‌توجهی و سلام‌ندادن وزیرخارجهٔ ایران به شما، توهین‌آمیز بود؟ این کار عمدی بود؟
🔹
ونس: باور کنید در این چند ماه گذشته زمان زیادی رو صرف سروکله‌زدن با ایرانی‌ها کردم. بعضی وقت‌ها به‌عنوان مذاکره‌کننده واقعاً رفتار پیچیده و گیج‌کننده‌ای دارند.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/444108" target="_blank">📅 22:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444107">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a722f491.mp4?token=MkeeymbQNvM0VkhwC8Hca17IT717oKWnge26SZp8hov6YDor4rxs0SCQOB_-bREzimQJowXAphTCajj1AyvsE3TX-PHg4FhEL72vL1hx6G5J8vKARCjlZgD6MprWx710IuOuSCVBwA8-N3sTmi3wyu0Y8gst3cn-yIqlgPLTqAbzooOfeHV53z5SwBb-7x11Jfoo5pD91iPr2J7oJnk3Pwxlb63wi4eIEtya1pxwBF72kVqF_o7YQEV07rdUMeZu9nUkwtnJI6yDmHL5hk79AhvA-uQ35zAOhQgN79lgJQKxaX_h1qRfp17fusZQB2BTzt6hpydtMWjqd7dCYpjCCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a722f491.mp4?token=MkeeymbQNvM0VkhwC8Hca17IT717oKWnge26SZp8hov6YDor4rxs0SCQOB_-bREzimQJowXAphTCajj1AyvsE3TX-PHg4FhEL72vL1hx6G5J8vKARCjlZgD6MprWx710IuOuSCVBwA8-N3sTmi3wyu0Y8gst3cn-yIqlgPLTqAbzooOfeHV53z5SwBb-7x11Jfoo5pD91iPr2J7oJnk3Pwxlb63wi4eIEtya1pxwBF72kVqF_o7YQEV07rdUMeZu9nUkwtnJI6yDmHL5hk79AhvA-uQ35zAOhQgN79lgJQKxaX_h1qRfp17fusZQB2BTzt6hpydtMWjqd7dCYpjCCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موشک‌های ایران  دست‌نخورده ماندند!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/444107" target="_blank">📅 22:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444106">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🎥
دهلران ایلام در محاصره پرچم‌ها و نوحه‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/444106" target="_blank">📅 22:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444105">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRj3kHSZDezmzhs7ulsSEfrV7ZBip-LdBBd3Y2eS6ZV4fioacC0N2kCTmVMkZFglK75zI3vxNh99dzJGudi14PWOPPHEMFVw4Ii0e-3HpGoLk-3B5VDFUNKkk0PS1AWZc7BL4JiNxHC_D3airfxvKkZI72QA1txJ5-o2B1-nYEWTndA6WtZxIEqeE7qecu6jBJPf2AVpp9g2dVzCu23bIP-KBDxIdOjGfwuVfdd4O5JoB_KXChiU7OB64TC6Vj70OadnePwzQn7tNd4FLLPoiIx6x7uWB35tr4EHXpccnkk71rzPwh3nC5OKqkKy0G3Jh7LI7pBIkPyLad93HVkN4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانداری محور مدیریت حریم تهران شد
🔹
شورای‌عالی شهرسازی محوریت مدیریت حریم تهران را برعهده استانداری تهران قرار داد.
🔹
براساس مصوبه این شورا باتوجه به افزایش ساخت‌وسازهای غیرقانونی مقرر شد شهرداری ظرف مدت ۳ ماه حریم مشخص و قانونی برای تهران را معین کند و پس از آن صدور مجوزها در حریم شهر را استانداری انجام دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/444105" target="_blank">📅 22:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444104">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔸
خواهش می‌کنم دستور رئیس‌جمهور رو مبنی بر حذف پیمانکاران در استان هرمزگان را پیگیری کنید. چرا این دستور در استان هرمزگان اجرا نمی‌شه؟
🔹
حالا که دارن بعضی جاها برق رو قطع می‌کنند کاش مثل پارسال اطلاع‌رسانی کنند که بتوانیم برنامه‌ریزی کنیم.
🔸
الان یک هفته است خونه فروختم و پولم تو بانک ملی گیر افتاده. چرا کسی فکری برای این مشکل این بانک نمی‌کنه؟
🔹
با وجود مصوب کردن مجلس دوره قبل مبنی بر اختصاص کد استخدامی به معلمان پیمانی مهرآفرین، چرا وزارت آموزش‌وپرورش این کدهای استخدامی را در احکام معلمان پیمانی مهرآفرین اعمال نمی‌کند و هیچ‌کس هم پاسخگو نیست؟
🔸
وزیر آموزش‌وپرورش گفتن مدارس شهریه نباید بگیرند پس چرا در شهرستان میناب هر مدرسه‌ای سرخود یه رقم وحشتناک می‌گیره؟
🔹
میشه به گوش وزیر اقتصاد برسونید مددجوی کمیته امداد چی داره که دهکش شده ۸؟
🔸
امکان داره پاداش‌ها و حقوق‌های بی‌حساب‌وکتاب و امکانات عجیب‌و‌غریبی رو که به شرکت‌های نفتی‌ می‌دن رو پیگیری کنید. مثلا بهشون پاداش می‌دن که بتونن جنگ رو تحمل کنن یا حتی حق مقاومت می‌گیرن!
🔹
تو رو خدا شما که رسانه دارین لطفاً به مسئولان بگین مردم واقعا از فشار و تحقیری که از طرف خودروسازها با قیمت و شرایط و نحوه تحویل خودروها بهشون تحمیل می‌شه خسته شدن.
🔸
ای کاش یه نظارتی هم روی اجاره‌ها می‌شد یا طوری بود که صاحب‌خونه نتونه هرچی دلش خواست به اجاره اضافه کنه. آخه مستاجر چه گناهی کرده که هرچی درمیاره باید تقدیم مالک کنه؟
🔹
۳۰۰۰ نفر از هیئت علمی‌های پذیرفته‌شده فراخوان‌های  ۹۹ تا ۱۴۰۳ که همگی پروسه جذب هیئت علمی را با موفقیت گذرانده‌اند، بیشتر از ۳ سال هست که درگیر مسئله صدور کد و حکم برای واریز حقوق هستند و به‌صورت تقریبا رایگان درحال تدریس در دانشگاه‌های کشور هستند.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/444104" target="_blank">📅 22:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444102">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbea764f62.mp4?token=SLJQs4WwPqVaIaWPJU-Wuwd9ve0c0froBVacOU3831z0b1JUFQTuwhMzH6t59o8ZLzWa98SI5_7Bp-3j8e4mD65zrAEiimAC9VmX0V163EO4-29mnjbudhVpRVARuIucgKoMoSm0BTGCt8q7MC3E1ouaIjq4rFXHTKVmWboqWr1K6eqsjsnKOyYbcW-jmVJUN7bwxXmcNn3g14k8EATG_s6zuYxm6UKanyI2un8rgKjk9jKRfeY8A3Lq9mOSMbkF_94hnYLZcr0ugKXiaKjyH_J9HgrnEGaMlWnpKAVn43ewuLwJxAPowdp1j8WdTh0MgaNXJEVbDMxfQmBb2Xxr3oVZE9xBqYFSu5uwUQ1B5XBcvr8fbCo88nJooCbia-Fzb51zQc38lFbmCh-IlcSIHXWFnCt_6FidGDAJ1p_IRtsKf1E9eNyypnC77HhT0SXLbV01YGmwA9e790SmLOdarsee34L6AT2sP6-9HVTh8waeGI0x8gP_HJ1yxD-ejsMUZfIsgj19_8d6MXsVUQT-QSd62aSghY9rHEk1eDoS21o3NGnp4GeX2n-t2_SwaBK7Msm4Jh9O69qFBzZJAnK4VMqbcLeYn6RJs7-_43Lq4pAjMq7tKcZIlz-UkShP_qIjo1-hV1ukP6h0KJxiqUzztwKhPVxBBlSiMx3iEThZjpY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbea764f62.mp4?token=SLJQs4WwPqVaIaWPJU-Wuwd9ve0c0froBVacOU3831z0b1JUFQTuwhMzH6t59o8ZLzWa98SI5_7Bp-3j8e4mD65zrAEiimAC9VmX0V163EO4-29mnjbudhVpRVARuIucgKoMoSm0BTGCt8q7MC3E1ouaIjq4rFXHTKVmWboqWr1K6eqsjsnKOyYbcW-jmVJUN7bwxXmcNn3g14k8EATG_s6zuYxm6UKanyI2un8rgKjk9jKRfeY8A3Lq9mOSMbkF_94hnYLZcr0ugKXiaKjyH_J9HgrnEGaMlWnpKAVn43ewuLwJxAPowdp1j8WdTh0MgaNXJEVbDMxfQmBb2Xxr3oVZE9xBqYFSu5uwUQ1B5XBcvr8fbCo88nJooCbia-Fzb51zQc38lFbmCh-IlcSIHXWFnCt_6FidGDAJ1p_IRtsKf1E9eNyypnC77HhT0SXLbV01YGmwA9e790SmLOdarsee34L6AT2sP6-9HVTh8waeGI0x8gP_HJ1yxD-ejsMUZfIsgj19_8d6MXsVUQT-QSd62aSghY9rHEk1eDoS21o3NGnp4GeX2n-t2_SwaBK7Msm4Jh9O69qFBzZJAnK4VMqbcLeYn6RJs7-_43Lq4pAjMq7tKcZIlz-UkShP_qIjo1-hV1ukP6h0KJxiqUzztwKhPVxBBlSiMx3iEThZjpY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمایتِ گنابادی‌ها از انقلاب در شب حضرت علی اکبر(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/444102" target="_blank">📅 21:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444101">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‌
🔴
یک ‌منبع آگاه نزدیک به هیئت مذاکره‌کننده ایران در گفت‌وگو با خبرنگار فارس: ادعای معاون رئیس‌جمهور آمریکا دربارۀ بازگشت بازرسان آژانس به ایران کذب است
🔹
این منبع آگاه ادامه داد: در مذاکرات سوئیس هیچ صحبتی درباره حضور بازرسان در کشور نشده است. @Farsna</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/444101" target="_blank">📅 21:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444100">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y89kJrr8g3C3ZMbu7sL0Yv4LzCBnTtvLqSi_2be9HwuIeAnVbyj_I_f2rFxbH6muku3uUA4sGNrEqWNTUPx2-K27BESf8wX7zu2QwXvzxx6hHVHtvdh49vqJPf_S70w9CYj_Ro6a8IixBbGEm8K8BXO7CeY1YeWKgNGQ_6y83CQUyj1L4_crZujhhytQUcvg5PhMntKOJwi9A9elxW4_CcR897Mug-mYGF2l6I8kB2k2g28GCbDULdMAqgurTq_hRXFXwfL3VDjYyjijzYbppQYWMQ0NgXi13AxswXdeAgaw4ylaeBJlBBjBL1cXhdCttPVy8s6bj-jor_hDqcBSKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گام مشترک بانک شهر و ساتبا برای جهش سرمایه‌گذاری در انرژی‌های تجدیدپذیر
🟢
به منظور توسعه سرمایه‌گذاری و تسهیل تامین مالی پروژه‌های انرژی‌های تجدیدپذیر، تفاهم‌نامه همکاری مشترک میان سازمان انرژی‌های تجدیدپذیر و بهره‌وری انرژی برق (ساتبا) و بانک شهر به امضا رسید.
🟢
به گزارش روابط عمومی بانک شهر، بر اساس این تفاهم‌نامه، دو طرف در زمینه‌های مورد توافق همکاری خواهند کرد که اولویت اصلی آن مشارکت در تامین مالی طرح‌های احداث نیروگاه‌های تجدیدپذیر شامل نیروگاه‌های خورشیدی و بادی است. این همکاری در راستای حمایت از توسعه ظرفیت تولید برق تجدیدپذیر کشور، جذب سرمایه‌گذاری و تسریع در اجرای پروژه‌های نیروگاهی انجام شده است.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/444100" target="_blank">📅 21:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444099">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه مالی فیروزه | Firouzeh</strong></div>
<div class="tg-text">💎
«
مسگون
»
سه‌شنبه ۲ تیر
در تمام کارگزاری‎‌ها
«مسگون» صندوق بخشی در صنعت «فلزات اساسی» با تمرکز بر مس و نماد
#مسگون
در روز سه‌شنبه ۲ تیرماه ۱۴۰۵ پذیره‌نویسی خواهد شد.
تحولات قیمتی صنعت «فلزات اساسی»
در کنار آینده ممتاز «مس» این صندوق بخشی جدید گروه فیروزه را به یکی از گزینه‌های جذاب بازار سرمایه تبدیل کرده است.
💎
تخفیف ویژه معاملات و خدمات اعتباری اختصاصی در کارگزاری فیروزه آسیا:
https://in.firouzeh.com/kargozari
https://in.firouzeh.com/kargozari
🔙
👨‍💻
واحد پذیرش و پشتیبانی کارگزاری فیروزه آسیا: ‍
🔜
+982152461000
💎
@firouzeh</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/444099" target="_blank">📅 21:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444098">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/444098" target="_blank">📅 21:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444097">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09908d161b.mp4?token=JOGo0ZvQxODkpfMIYbisRJl557Jj6dS8GmBEiCOKaum3wdARu0mGa4kFvHtAA6AfBhVnkXYS87O7CYprIx5wxUSMjLKPlO_yHLZzX7sTBPud1ZIsAL5Ugm14aqv5L1KHQ-P8H4uPTgO72hIgRNGdoyVkAUXw9aTyivPPPZKWEwdJGC5DVPfTZ_LMmbP5-ezNLbiJTANSjKlNWq9afPAgfJVSniPTRf2WU0J9sVYIt0G-4-jb2h8veF_bZ-5SonaxBtMwvczHePeZZj5HsZ2gA8Sgqr_74LrjcaLqyCnUbhJ3PHQseAaX34YslTdH6pinO2y9Ttl-WGVhbWmq1jcQcinfUDSNWz7_qrCTTIwT0qiIy66UrJ_m_4ImzKgjBFBZcyGdzSab147HLzq77QNcrcl83M9fCw07y7WaVCNoxEpCprBfFMrJ9ELYi4GTvm8jAxYjb5NiA15_1Cfx4Ze9yfBcb7pZqeBIfHF8BUn9T3nE73SALeV97w9j1z1rvOgIhgoiDemYhmYdS8EmWZoS2X1s1TLDELwy0Bf4H9lHqJAwfHj35zkiXZA3P5lcxPqjveWEfIVJt-_ER3t9_Q6QfvkQQ1tlsnomxk6Fv4s27SkHMRvIBnfx3_xarSY8htFEWIObpnBCP99grl--Iuhw46W76CGOPJwNkFf02vTNTEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09908d161b.mp4?token=JOGo0ZvQxODkpfMIYbisRJl557Jj6dS8GmBEiCOKaum3wdARu0mGa4kFvHtAA6AfBhVnkXYS87O7CYprIx5wxUSMjLKPlO_yHLZzX7sTBPud1ZIsAL5Ugm14aqv5L1KHQ-P8H4uPTgO72hIgRNGdoyVkAUXw9aTyivPPPZKWEwdJGC5DVPfTZ_LMmbP5-ezNLbiJTANSjKlNWq9afPAgfJVSniPTRf2WU0J9sVYIt0G-4-jb2h8veF_bZ-5SonaxBtMwvczHePeZZj5HsZ2gA8Sgqr_74LrjcaLqyCnUbhJ3PHQseAaX34YslTdH6pinO2y9Ttl-WGVhbWmq1jcQcinfUDSNWz7_qrCTTIwT0qiIy66UrJ_m_4ImzKgjBFBZcyGdzSab147HLzq77QNcrcl83M9fCw07y7WaVCNoxEpCprBfFMrJ9ELYi4GTvm8jAxYjb5NiA15_1Cfx4Ze9yfBcb7pZqeBIfHF8BUn9T3nE73SALeV97w9j1z1rvOgIhgoiDemYhmYdS8EmWZoS2X1s1TLDELwy0Bf4H9lHqJAwfHj35zkiXZA3P5lcxPqjveWEfIVJt-_ER3t9_Q6QfvkQQ1tlsnomxk6Fv4s27SkHMRvIBnfx3_xarSY8htFEWIObpnBCP99grl--Iuhw46W76CGOPJwNkFf02vTNTEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از شعرخوانی سیدمجید بنی‌فاطمه در دومین شب مراسم عزاداری حضرت اباعبدالله الحسین(ع) در جوار حسینیهٔ امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/444097" target="_blank">📅 21:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444092">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی</div>
  <div class="tg-doc-extra">حجت‌الاسلام کاشانی</div>
</div>
<a href="https://t.me/farsna/444092" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
#حسینیه_فارس
|
شب هشتم محرم
🔗
سایر مداحی‌های امشب را
اینجا
گوش کنید
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/444092" target="_blank">📅 21:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444091">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/444091" target="_blank">📅 21:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444090">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">هدف آمریکا از «رفع تحریم نفتی» چیست؟ ونس پاسخ می‌دهد
🔸
وزارت خزانه‌داری آمریکا امروز با صدور یک اطلاعیه مدعی شد که یک مجوز عمومی برای معاف کردن صادرات نفت ایران از تحریم‌ها برای یک بازه زمانی ۶۰ روزه کرده است.
🔹
پیش از این جی دی ونس، معاون دونالد ترامپ، رئیس‌جمهور آمریکا درباره انگیزه‌های واشنگتن از صدور چنین معافیتی برای خبرنگاران توضیح داده بود.
🔹
او چند روز پیش در جمع خبرنگاران تصریح کرد که تحریم‌های ایالات متحده علیه ایران در سال‌های گذشته بی‌اثر شده بود و واشنگتن به دنبال راهی برای رصد شبکه فروش نفت ایران بوده است.
🔹
وی روز پنجشنبه گفت: «صراحتاً بگویم، ما این اقدام را امتیاز بزرگی به ایرانی‌ها نمی‌دانستیم؛ ایران هم... آن را امتیازی برای خود تلقی نمی‌کرد، چرا که عامل بازدارنده آن‌ها از فروش نفت، تحریم‌ها نبود.»
🔹
ونس اضافه کرد: «آن‌ها بدون هیچ تخفیفی، نفت زیادی می‌فروختند، زیرا تحریم‌ها اساساً ناکارآمد بودند. در آن مقطع، کاری که تحریم‌ها انجام دادند این بود که سیستم مالی ایران را به سمت چیزی شبیه به سیستم بانکداری سایه سوق دادند.»
🔹
معاون رئیس‌جمهور آمریکا اضافه کرد: با لغو محاصره ما در واقع قادر خواهیم بود تا حدی ببینیم که سیستم مالی آن‌ها پول را به کجا می‌فرستد و از کجا دریافت می‌کند. این یک منفعت واقعی است.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/444090" target="_blank">📅 21:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444089">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🎥
دیشب سربازان ایران در ۳ جبهه جنگیدند
@Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/444089" target="_blank">📅 21:23 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
