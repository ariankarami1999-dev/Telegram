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
<img src="https://cdn4.telesco.pe/file/LNf_NGgmGa68bjo5aD2m-CMOw4tjhd49sBT3fURp6kEb4yNRY1HbmU7dtVZ8o5h8vNFDBmSpDKmlfAj2SomHUmnIA3qLX3YcPTIpkvrE9ANRbqtxaQFWidahbc-hl8e6xpFqTETox49PCv4fCze1f_v_H3NE8AgWkpetv4Jiunl2UQ9iVoZe_c_9OmUIKWRlNTV8yvIKpmKBjOoF6sO1fJCYqdoASVcAaqZjUujMea9UWZb4X5A3JIwzK42_XbuvL6mULdPh93XkuIDTWvo-J3NJboIE6TqI_H7UGUeWn1v6sPtaOCJxbetA7ipVPWz1Za26yp_g3AXkOZE6R9mVyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 18:37:34</div>
<hr>

<div class="tg-post" id="msg-463940">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/492eb9cbdf.mp4?token=Mhhc4grYjovIDxZQ4LWRuISYdYLxy-x9lYxM48VSSDbu0wGNRQn-quyulCCAJCbAolBhhwMup3gWhsSNbTCcJK6NIifpN4pfW3aWOOy4PUWYpEyJQhHiMMoCCi4T2KlOaR8O3wDVHxlpDN9NRW8qJPDmOSoYVjroEKK8oql4k4atNTxv3AsAW7eaTLIeGTXqecVS1ExWbA9YKl6E3-5wXhmQmpzsTUtY8-nFGcg4JnhQU9N56gRhQ0faWqTBKZza65b5WZcZCr8JA9pk4Gx_Hen8mr1GxFJa5_lpesqc-bU2bk-Ha4rG6u6UifAbQIpLGessgJ8fwmliYt6OBuOonA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/492eb9cbdf.mp4?token=Mhhc4grYjovIDxZQ4LWRuISYdYLxy-x9lYxM48VSSDbu0wGNRQn-quyulCCAJCbAolBhhwMup3gWhsSNbTCcJK6NIifpN4pfW3aWOOy4PUWYpEyJQhHiMMoCCi4T2KlOaR8O3wDVHxlpDN9NRW8qJPDmOSoYVjroEKK8oql4k4atNTxv3AsAW7eaTLIeGTXqecVS1ExWbA9YKl6E3-5wXhmQmpzsTUtY8-nFGcg4JnhQU9N56gRhQ0faWqTBKZza65b5WZcZCr8JA9pk4Gx_Hen8mr1GxFJa5_lpesqc-bU2bk-Ha4rG6u6UifAbQIpLGessgJ8fwmliYt6OBuOonA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی: نشستن نمایندۀ ایران پای سخنرانی ترامپ مایۀ ننگ است
🔹
نایب‌رئیس کمیسیون اصل ۹۰ مجلس: درحالی‌که عامل و دستوردهنده به شهادت امام شهید ما، کودکان میناب، کودکان لامرد و دیگر ایرانیان در آنجا سخنرانی می‌کند، واقعاً جای تأسف و ننگ است که افراد ایرانی…</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/farsna/463940" target="_blank">📅 18:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463936">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VbqNtgQjmu5PYEMwtvjJvAxyeXGysyIevCa_B3ciKE3uBOyqbMmyjl6GTwKMmsi-r7aMwczyRBPb1qRSucx7leDPktyEgjJ-hTCv4jkzuUF99gM9w4YecdEtPlW_TwIJHWiRIhVZYm5WlP_yf8lvVVs0eRdPVD-90hIgBGTlwAW_YFppHq12EodZGlz5YdZwGkBBHQ3xCRSRDrgHZwOYwKhSty7H-nJmXCIfXSeChYQEoecO07KXvXaKhSZGXpt0vhebXYaCLzuQaT9Ys_Qz4qKj-kXEAkI0Q6g4-ppzFpzQKQsnNlgmW4GZRdnArv8ISwiadwNTgEO3RETpqRaFhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMYIgZbzhLmZKG8xUUq8RQ1eFC4AvjLgYgZ5GB3B-yVs8V8Z170uR_GjBE7YZKWzDwsrIn4Bud0Kmzridzwmos2-QuqzaFtYoov3cJnxcRY5EbackyA9IZ2fY7OIXs0yAsRt8kUNvF0muHj0ZGqa7iVDQygASlZmjuj13P_1xFWa_SQaMNN0_iPsCCgt5LbXfnM6OFQw66T7NEBf39_6sQ0Iis8lKJpFvBRjDTKnZHdejQXVZwlgyAWIvQnyVqSXNyEMEFWOIVzuplnJwvqd9No2P99NLNlZbuCsgEECo5-MrodUOhZXdg7LEOLkV5ZcAFpVkYtSUY5Q2IPsMxWW8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c-CjlAW7qmlwqZGw8osr5okdLpEXEnFx4IUhC8692YYVE3IrhMvvrpb1D07lUY7N9FcyE6nwhBsYGT6dCFXLYt9q1AMPO197f0zdSbqTGaIpyzZSpj0jpho1AZP1VX95jv09JSwy0QNWYjmz265kT9jJmjjh0L8XWRLpb8O9jqd7uTBthaDEJ6tSY6exnkRuNfVd2dX5ldT4Pi_Xbdeujiy52OQHFLErkrKeE8Tt-biDdJAXyqFho7GsxJoQNIHREbMsIh7x1GKY3FWrH2r4OzbLQWvVof441jTnlv-5Rbq6s--T3xk3mLa71yn4jvoIfu5wPeE2b1YdVtSaB2b4KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W6egu7zWS--FFBLQOaIsghzhC78VaW7IWzRvQgFiOdBcslWfFQDeLcSa_BpwEa2GYBgyCfkiHehk3yG1iHcXLnGW09JoZtSdNILuVMm4y6Bd9aqb9YkfUUWucxKicvYGrdg8Hp6QzDd3yd2KiQjk1IPObEu4L7TQwF-7mP8kuEMvJ0maewxl2RGxFCyJcNURyizbgFa-eSzim1WRRVL-yneJO5Padb-2gQ2E_VCjF1AN3xNyglQg5COU9dors_WIsTWcN5ZZqz7ljT0aA8oxHpry0vjmi-B8DKu9dbK-gCRuHQb4HC91-HyWXfBS3jRWojFWDKafgROaFiquZF47zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پزشکیان جنایات آمریکا در ایران را به رخ دنیا کشید  @Farsna - Link</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/farsna/463936" target="_blank">📅 18:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463934">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b74c9c59da.mp4?token=jxXWLwDZ2llx1veX-cWXFP4JaMDHwCIR9ns5pKp0dz730EZFVO2u2HenHg-3zKWI56n1-lfjsnrn7UGrky-TFjT5rr53-zirjAp_ZxUVuel4rP6p79fpBPDva-JiyImji7Us6TJgbObk_38HxsCZZrPCj5nwi7ArR2se8ZpKr3Yggwb-PjAC6xnEBJs9Tfu5a3k6obP4uDxvvB7Y9DsEX3zCEGh-5FTm_zFyUAX7ZWcbCGpRrzv9UKSG3sotHeRptng0ckxcaR4hyL1-efR6rnRuHSK9klwUuYfY-BfIwiVls-ILNnmygM53kp0n4ceaZBHuuWGrfy6r0I7OmDSuRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b74c9c59da.mp4?token=jxXWLwDZ2llx1veX-cWXFP4JaMDHwCIR9ns5pKp0dz730EZFVO2u2HenHg-3zKWI56n1-lfjsnrn7UGrky-TFjT5rr53-zirjAp_ZxUVuel4rP6p79fpBPDva-JiyImji7Us6TJgbObk_38HxsCZZrPCj5nwi7ArR2se8ZpKr3Yggwb-PjAC6xnEBJs9Tfu5a3k6obP4uDxvvB7Y9DsEX3zCEGh-5FTm_zFyUAX7ZWcbCGpRrzv9UKSG3sotHeRptng0ckxcaR4hyL1-efR6rnRuHSK9klwUuYfY-BfIwiVls-ILNnmygM53kp0n4ceaZBHuuWGrfy6r0I7OmDSuRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ایران به سوی جهان دست همکاری دراز می‌کند؛ هیچ‌کس در این منطقه به تنهایی امنیت نخواهد داشت، یا امنیت را باهم خواهیم ساخت یا ناامنی را باهم تحمل خواهیم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/463934" target="_blank">📅 18:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463930">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_5EelBrHqSOQ-B5eHhXeU6Xf9F5IveS7a5I8vg42kj3qAZg8BgjRgw72Gf1KrJ_0TTkuH5k-EbbLDrzOhxlvAPV5CBGWlXsbExQtCIy97Aub98C-26NeFFuVAD59JVylDAkbrfLc38CGI2Dw8ByN2_-XDomfrGtDNOvp8xGr4gftDh5tCtQ0WEIfAoLnCcs3u-YHt0nMdw33esl6tik2rybUnQ_nqJKnjMp6aONYVCwwb_jqdhDSwYwpi51hv4F0cQ55M0R5AyZ74TXly8AzBNHPPiWXENurG7tLqCpAL3t7De-tE60bn0wqP-G9ns5EAAzA1KjhBhgC-5IR6Ofew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4Qa2hiLcjMqdLM884Afy5BWH6g22wadiQ__OKzy7rUB6YKiNPEq2Fo3btJjfVujVpuQWsOEsowWpIh09i4zzPmmV5iZUElT_ogyzCaycwtIjyGdeGN3spbQ2xTEuJ3mtX9NyNSqws-sOuzhvF41oYvA5n3U7kyCUKGXiF0B9O4YWZyzDGXuoA05PUQuXDC5b9ORmpRb_Cxy4sm3HnXBkAHriKIrtidGMD18vY8zzr-DD_KMsUecqBTbhl5B81Qa4kRJKaiuAHASR3hJQhG3eV2DRkDUGK_-6ZDFA1nWq_-WE3sMyvU6wvSIxGXs-s7fJVScojfrop0d0r4ugdT5pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VBL3duclGyijKYdxxfWtrKgmAq_24G3NBTXrHP9JMq3NiF8BC8gcXqujws3OlvFH-e_EhoR3BRWxLUB58mU9zTz9MQ0x7aZeu25MX_6umBynhEZmazVu8cFOjDIY8n4s7uZzHIMyBV-iv7L740LOOxDuCKZiuxJMwiO-dlLwjnneJZDiPzWen5FcknTAy0bgOuENmGFxo0VoZIkk6wy67cbLdsGMWjKY00VYkmUhD2qsFmQfsukO8AIRZ98bPtpSDcFQq5pa_6qkDbqdMya6PuHFKATVVaFlIRMD_oU0mQtjZprrgOa9mJjNUJxVMpS4g9ln_m0Pjw5iAoTM64W_kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lnjlHe0rwzeQYzrLxkHLjUGWrD9-pz8G_0REDuIG5RL8F8w49xFuNHGjNrMydgUx23ZoZNEczWc2yjH95faHy4_n5gGwnegNjyN1oCkOl0WN3jBmHNgqXqgvGOhxIAZ1FDuQLZJdm4IxHY2yL5cSx04FP2P4ZU6yE6GMn3CFM_Qkr-qJsqZE0ogdLw0mHmyeX9VpOwEqF6iPlD4UN2JMre63y4T-kMhW9eFL4eS-y2QjLZENII5K7ScqUDEJcvVQB1eNl6t7g7ppwLZerOOrkkGX0_ppbyqG2ECm-jxpN5NSgjGT8jF5Qnpw3X8d_15Cw08O7SGZymV8m9XpF8A3nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پزشکیان جنایات آمریکا در ایران را به رخ دنیا کشید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/463930" target="_blank">📅 18:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463929">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdae98e643.mp4?token=NP-bw4XI2jW_sdMyaxIVH_MJlYNb5iy3Iib8ij-tYQgMQTu1N1iiCRxQzfhJh6XKWyRME8MueP_8-ZhCjWzddLxZaKgq3F5oqAOQkkDfv3WBkjFvS5e3yG_Otkw9D90DsHDzhH_G69UtNUbZelOYEw2hM0ddVrDY4MTt7RsqKwgHYyDwAPfXDaOIDWh9dglfCvxKpVVtw0I061YmnwuV8FUmxMZcqicDwJr5u2FcsvyoFVSJ-VX7zpYR9SU3kyQiGQO_O7dtO2QbHPmqynifeVHe4TXj1BKqgKru8pMcvKxOA_mmK4C0KM3S5u8vnNERUJ1_hCm1iCG6ujMdVHizAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdae98e643.mp4?token=NP-bw4XI2jW_sdMyaxIVH_MJlYNb5iy3Iib8ij-tYQgMQTu1N1iiCRxQzfhJh6XKWyRME8MueP_8-ZhCjWzddLxZaKgq3F5oqAOQkkDfv3WBkjFvS5e3yG_Otkw9D90DsHDzhH_G69UtNUbZelOYEw2hM0ddVrDY4MTt7RsqKwgHYyDwAPfXDaOIDWh9dglfCvxKpVVtw0I061YmnwuV8FUmxMZcqicDwJr5u2FcsvyoFVSJ-VX7zpYR9SU3kyQiGQO_O7dtO2QbHPmqynifeVHe4TXj1BKqgKru8pMcvKxOA_mmK4C0KM3S5u8vnNERUJ1_hCm1iCG6ujMdVHizAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: اسرائیل ترور می‌کند اما ایران تحریم می‌شود؛ این یک تراژدی است که به هرکس بگویید خنده‌اش می‌گیرد.  @Farsna</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/farsna/463929" target="_blank">📅 18:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463928">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c00116d8b.mp4?token=RVh56oXvaKKcQWbjqNdUQYSkxhSTQIoKOUKGhkNgjRauaXzrSTcHt2HI14WuyHqOFsz-x4jCBpakY0eUNu2vdNMMPIL9N3kgTX4O4CWskRjQ11a5zVjcEodRxiXiV-ldplOygYpML68gIfYxP1b10GgFbW4vi8NrR8jTw5XzHOnKKOz6ZTumYAeFYU6ob6_JENniHBd0kgH5gTP6HrfumV1EJxOXC3-DoMeKM_9-mjaTb14ucNVqtQu2l5viJ0RZJxO0VwIYjXS5IfEPFuEsdKsxqa4RzHRWh6Qub9DDnJrh0wPAEAlnJmCuGTFZ-qIX8H7X601RVV8ret6-LdPueA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c00116d8b.mp4?token=RVh56oXvaKKcQWbjqNdUQYSkxhSTQIoKOUKGhkNgjRauaXzrSTcHt2HI14WuyHqOFsz-x4jCBpakY0eUNu2vdNMMPIL9N3kgTX4O4CWskRjQ11a5zVjcEodRxiXiV-ldplOygYpML68gIfYxP1b10GgFbW4vi8NrR8jTw5XzHOnKKOz6ZTumYAeFYU6ob6_JENniHBd0kgH5gTP6HrfumV1EJxOXC3-DoMeKM_9-mjaTb14ucNVqtQu2l5viJ0RZJxO0VwIYjXS5IfEPFuEsdKsxqa4RzHRWh6Qub9DDnJrh0wPAEAlnJmCuGTFZ-qIX8H7X601RVV8ret6-LdPueA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ثابت کرده‌ایم که از جنگ نمی‌ترسیم و تا پای جان برای دفاع از ایران ایستاده‌ایم
🔹
بمب اتم در دست اسرائیل است اما آژانس از ایران بازرسی می‌کند. اسرائیل ۷۰ هزار نفر را در غزه قتل‌عام کرد اما ایران بمباران شد. @Farsna</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/463928" target="_blank">📅 18:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463927">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2180626322.mp4?token=fTgIwiOeGp7l9a1puzMo7IFFNQESo4TJFuSU-jKRs6zxGvV-ahD7NxQclRhpt3kLodrmHw25Aj6-QWJ50CBzok4PrQcrM67w0d0Oj2u8l0WbygMT5dS4wzWFtJxkkRql3KQo2f_QposCh9AjbISvQamWWo9dlLXG2yyFpTC5KcqB3e54a7s51leEIahkZx9uU4In6rPgTwI0Et-5V2AJt6GgSqRdgrmyCzsbX3UTkj_9HxuJwpkXS7ubtVWDe6sc91Ii34RrnfI6JqZCcdMQ7EXZ5kpAKl_tBe1Y8uxIb5j-e7RDBdn-G9vMvubJgtm2NCR7GHyX02iIhF-Bq_9Nwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2180626322.mp4?token=fTgIwiOeGp7l9a1puzMo7IFFNQESo4TJFuSU-jKRs6zxGvV-ahD7NxQclRhpt3kLodrmHw25Aj6-QWJ50CBzok4PrQcrM67w0d0Oj2u8l0WbygMT5dS4wzWFtJxkkRql3KQo2f_QposCh9AjbISvQamWWo9dlLXG2yyFpTC5KcqB3e54a7s51leEIahkZx9uU4In6rPgTwI0Et-5V2AJt6GgSqRdgrmyCzsbX3UTkj_9HxuJwpkXS7ubtVWDe6sc91Ii34RrnfI6JqZCcdMQ7EXZ5kpAKl_tBe1Y8uxIb5j-e7RDBdn-G9vMvubJgtm2NCR7GHyX02iIhF-Bq_9Nwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: غزه نماد شکست سازوکارهای بین‌المللی در جلوگیری از اشغال و رنج غیرنظامیان است؛ صلح پایدار در غرب آسیا بدون آزادی فلسطین شکل نخواهد گرفت
🔹
مقاومت را نمی‌توان با بمب و محاصره وادار به تسلیم کرد و از بین برد. @Farsna</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/463927" target="_blank">📅 18:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463926">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a17e29ca1.mp4?token=KqL8ArOAbDqCZ4Qee9kh6g3T4BxUKldP738gJlyKRyw5re9zprbra3I6-2hKhfqrEWnSsq9oP0R9FYhqXPPIbHNKOn6Yc_jpzxwAMGdgAuow6M8QRrW72aHqlU2fCqbkBJ7KxMp8NYRglF59IF17F0vDV8XE6arW3JRzwOofTECXioBio9mtEGZ_fbGJ3-R8hRgXrrDhbqze9aGUfJgGneYjhkdUPVa3P4_cxinfvUDBU8DzyYRYPB__szn658slmvgZh95fLw3TMLv9uitBX4-lmzYvC9MTjepbNKrzLU71AyxglYychg_qMGA_7zU0L8Gg-Y6_7jjtGVcCdcXiKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a17e29ca1.mp4?token=KqL8ArOAbDqCZ4Qee9kh6g3T4BxUKldP738gJlyKRyw5re9zprbra3I6-2hKhfqrEWnSsq9oP0R9FYhqXPPIbHNKOn6Yc_jpzxwAMGdgAuow6M8QRrW72aHqlU2fCqbkBJ7KxMp8NYRglF59IF17F0vDV8XE6arW3JRzwOofTECXioBio9mtEGZ_fbGJ3-R8hRgXrrDhbqze9aGUfJgGneYjhkdUPVa3P4_cxinfvUDBU8DzyYRYPB__szn658slmvgZh95fLw3TMLv9uitBX4-lmzYvC9MTjepbNKrzLU71AyxglYychg_qMGA_7zU0L8Gg-Y6_7jjtGVcCdcXiKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ما نمی‌توانیم بگذاریم همه از تنگۀ هرمز بهره ببرند اما ایران از آن محروم باشد
🔹
راه را بر ایران می‌بندند و سپس از تنگه اسلحه و مهمات و موشک برای نابودی کشورها از تنگه منتقل می‌کنند؛ این امکان‌پذیر نیست و ما اجازه‌اش را نخواهیم داد. @Farsna</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/463926" target="_blank">📅 18:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463925">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7b9c96ee.mp4?token=GljwKSNYBqvcIT9kBvrOshP_Vc7VQEHljPiCBWJ41NXpb_NjozNNqE-izfgm-CedAuvQhzeksbI_F8DmupdfEFoIOGNcTjO_KHq9AE6MhKyVqTfKzM0de_IlrB8Ba07gl2P97cAICfWseq2a8bL8-rJUPbiqOmEvsn4SU3a1O_7M12EzLywDRyiHeUdwmkqi_pUg109p4C5Kw83izhvs7ZH2Zd7Th-H3aJK5_pjjMvZ-yDo4zPKClqttZitWxTTi4p836-n9BWSo61J1oxLoUHSvglyMO6-_sn7lyNR1D26_Dl_3bS845uJ9d1R_bc8h4xKPCzph6MMFIdE6hq8dDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7b9c96ee.mp4?token=GljwKSNYBqvcIT9kBvrOshP_Vc7VQEHljPiCBWJ41NXpb_NjozNNqE-izfgm-CedAuvQhzeksbI_F8DmupdfEFoIOGNcTjO_KHq9AE6MhKyVqTfKzM0de_IlrB8Ba07gl2P97cAICfWseq2a8bL8-rJUPbiqOmEvsn4SU3a1O_7M12EzLywDRyiHeUdwmkqi_pUg109p4C5Kw83izhvs7ZH2Zd7Th-H3aJK5_pjjMvZ-yDo4zPKClqttZitWxTTi4p836-n9BWSo61J1oxLoUHSvglyMO6-_sn7lyNR1D26_Dl_3bS845uJ9d1R_bc8h4xKPCzph6MMFIdE6hq8dDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ایران نمی‌پذیرد دانش هسته‌ای امتیاز انحصاری چند کشور باشد
🔸
به صراحت می‌گوییم: نه سلاح هسته‌ای و نه محرومیت ایران از دانش هسته‌ای. @Farsna</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/463925" target="_blank">📅 17:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463924">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f95f7b4413.mp4?token=qUJ0qLZ0ZsvJ24LPWJsZ-aXAT5WTZ8uq-e-KdbS9ozTleYOxppvQGR9Xd_LlUEgiOzYH3Xv_B--_mYU4asTCW7NnD7AynVBIB1TX7nRIhnWFkmVnjwv0rlsSXL3CBLRjNZDXYNjLB0SZcSldHltWYhrvpNr1jKjgWqHlK02XzG-CHED3kl577gCIEkN62dDgdYUp3PE8hLnMKsb57pimdge4CqmsdbFt0PCs-vRKTrGUvmGOSsPsQUZ843hF8U6gKexigkGHmWiukFhZyiA3mf9o21uwXZWPkGHlluGo3Hy-VpCt-5HsZJ7rXU4nliP7gSNM5aNt6nb4VWyJTsu7IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f95f7b4413.mp4?token=qUJ0qLZ0ZsvJ24LPWJsZ-aXAT5WTZ8uq-e-KdbS9ozTleYOxppvQGR9Xd_LlUEgiOzYH3Xv_B--_mYU4asTCW7NnD7AynVBIB1TX7nRIhnWFkmVnjwv0rlsSXL3CBLRjNZDXYNjLB0SZcSldHltWYhrvpNr1jKjgWqHlK02XzG-CHED3kl577gCIEkN62dDgdYUp3PE8hLnMKsb57pimdge4CqmsdbFt0PCs-vRKTrGUvmGOSsPsQUZ843hF8U6gKexigkGHmWiukFhZyiA3mf9o21uwXZWPkGHlluGo3Hy-VpCt-5HsZJ7rXU4nliP7gSNM5aNt6nb4VWyJTsu7IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: سامانۀ دفاعی ما برای آن ساخته شده که هیچ‌کس تصور نکند بمباران شهرهای ایران بی‌پاسخ خواهد ماند؛ ما برای دفاع از ایران از هیچ‌کسی اجازه نمی‌گیریم.  @Farsna</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/463924" target="_blank">📅 17:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463923">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49e2387e6f.mp4?token=BUD9pnD49ys7ZTFyzk8bvtthvYyBZbY9NLATt2e-HvTKscG5JIiSSVKXGdLdHN9P7jor5Fkgv-mByTmVx354I_pokvALJmg6Yk_AQ2wOV0jzd6vgvvAblejDNXCTjmo23SBU1XLekob2KJZjKP-BULs8WZH7MW5OF8SaAft9_QX2hUzFg_6Ml237lIchj5zIf8J5dTgzYioYLHSD9Qbs7-Rzmi1dMplPEoAjusDgKYcEb7quTz51duaD9a0r_IQQ-do-IIFEV8_UP9dPhc8m0AKwz7hNpZjM92QJovUQ31QztRsrpy31_Fe4WHV-oOj0WuKFG81LtuSgVI3VotA3gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49e2387e6f.mp4?token=BUD9pnD49ys7ZTFyzk8bvtthvYyBZbY9NLATt2e-HvTKscG5JIiSSVKXGdLdHN9P7jor5Fkgv-mByTmVx354I_pokvALJmg6Yk_AQ2wOV0jzd6vgvvAblejDNXCTjmo23SBU1XLekob2KJZjKP-BULs8WZH7MW5OF8SaAft9_QX2hUzFg_6Ml237lIchj5zIf8J5dTgzYioYLHSD9Qbs7-Rzmi1dMplPEoAjusDgKYcEb7quTz51duaD9a0r_IQQ-do-IIFEV8_UP9dPhc8m0AKwz7hNpZjM92QJovUQ31QztRsrpy31_Fe4WHV-oOj0WuKFG81LtuSgVI3VotA3gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: مردم ما ۷ ماه هرشب در خیابان بودند برای اینکه کسانی‌که توسط آمریکا و اسرائیل مسلح شده بودند، نتوانند کاری کنند.   @Farsna</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/463923" target="_blank">📅 17:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463922">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0871b6d93f.mp4?token=gLZ49xGd4ee_7UFkRGH2Pm0dlK-UfpYTtd3AdEybHw4EyLSmJBwREaw4G8SBMsWFhs6vmoPptgOG3yIbplEdjZdVhSWzavvsupQ3gflzb8sr0gxW7FAkaRmyWOaOgnhkHM3mTc9RSfukqBH0-Qh7Qm4o9BEfCyZLdk0B5slLgtZWcGe_PvG6GQO4FdD1RgRShhfKyJ5rsCm3SrtxDOe6WS8q9LMBfx45SajdsHqYQGsv_n0HMimhjSy-eBFnkW3-aPFtY7ucufPZ1uG8syMUmR_A5dvrYbtwTa9snj10q41eVZnPbkDxJg8iOEgenoMnwUWXwoFGdBtMwUdHJAvRAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0871b6d93f.mp4?token=gLZ49xGd4ee_7UFkRGH2Pm0dlK-UfpYTtd3AdEybHw4EyLSmJBwREaw4G8SBMsWFhs6vmoPptgOG3yIbplEdjZdVhSWzavvsupQ3gflzb8sr0gxW7FAkaRmyWOaOgnhkHM3mTc9RSfukqBH0-Qh7Qm4o9BEfCyZLdk0B5slLgtZWcGe_PvG6GQO4FdD1RgRShhfKyJ5rsCm3SrtxDOe6WS8q9LMBfx45SajdsHqYQGsv_n0HMimhjSy-eBFnkW3-aPFtY7ucufPZ1uG8syMUmR_A5dvrYbtwTa9snj10q41eVZnPbkDxJg8iOEgenoMnwUWXwoFGdBtMwUdHJAvRAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ایران ۲۰۰ سال است به هیچ کشوری حمله نکرده اما ما را به تروریست‌بودن متهم می‌کنند؛ ما قدرت میخواهیم که از خودمان دفاع کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/463922" target="_blank">📅 17:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463921">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fbe61eec8.mp4?token=uNT0Arq39zEqjscaaJanq_60sGw1Lyn_cqZxchY5SBjOy7cbLhH1czIw4qPsi-did_WH_Z9RYnnsKm_VTj0TPHSutOwZw4zvXLSOKKLJK5tGHsKC2u0Uhnsc8Gj_JiI2FmcCpSvT-Qlg0HcyLA3h89r41GYAeBuuGOsmQgidcLXyK9OAweHw-WaI8Z4BpMkJy1dVPMaHHFDbicBMhSaJu8HWjcqOT_pc0k5MotjHRrFFexnL45XWi6MlI_FOqSM1-HXcJtkkb6DaYutgegrwQadvTKl0EyFAgXFhhS2F_kASBh4OZExCxoNWStvueL3NWI1fCIh04JzZ6gzVLg7q5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fbe61eec8.mp4?token=uNT0Arq39zEqjscaaJanq_60sGw1Lyn_cqZxchY5SBjOy7cbLhH1czIw4qPsi-did_WH_Z9RYnnsKm_VTj0TPHSutOwZw4zvXLSOKKLJK5tGHsKC2u0Uhnsc8Gj_JiI2FmcCpSvT-Qlg0HcyLA3h89r41GYAeBuuGOsmQgidcLXyK9OAweHw-WaI8Z4BpMkJy1dVPMaHHFDbicBMhSaJu8HWjcqOT_pc0k5MotjHRrFFexnL45XWi6MlI_FOqSM1-HXcJtkkb6DaYutgegrwQadvTKl0EyFAgXFhhS2F_kASBh4OZExCxoNWStvueL3NWI1fCIh04JzZ6gzVLg7q5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان در سازمان ملل: ما تروریست نیستیم، ما قربانی تروریست هستیم
🔹
من از ایرانی می‌آیم که رهبر ما را بدون هیچ دلیل و برهان و قانونی ترور کردند.
🔹
من از ایرانی می‌آیم که در آن آمریکا و اسرائیل یک مدرسه را بمباران کردند.
🔹
در لامردِ ایران آمریکا به سالن ورزشی…</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/463921" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463919">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc74a13417.mp4?token=GLAcULu5ujDGdz6CpKHx2SX4bR90sUKLAHgtdwLrKv-uKqxjunlSGmW3Q6SD-0xJ5gZuSx5UDQpYD40rP5CjdgcxXpcIXrJkCHzcCkiyErPw-JWFQOkijCnj3Bhm4CUtVK5moAW2BNXXso7Tdx0acgjUfGPhlIDgxDs9HF3xJWf5al9rWwhk7zZnffPkd0aFRIXhs0ncyeKZY4yIOa5dCKww68MjTRmo3J7lGrZilY1_JhhU9qt2BBtl6dztvjZwce9KEuQ__SDQ4iH9jMV8pJUikoJAQWYNPkGqoA-M4BWeNofxgcTEBoWb_a3jnRmHgf-QDVEA40yrTFr4qiwqRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc74a13417.mp4?token=GLAcULu5ujDGdz6CpKHx2SX4bR90sUKLAHgtdwLrKv-uKqxjunlSGmW3Q6SD-0xJ5gZuSx5UDQpYD40rP5CjdgcxXpcIXrJkCHzcCkiyErPw-JWFQOkijCnj3Bhm4CUtVK5moAW2BNXXso7Tdx0acgjUfGPhlIDgxDs9HF3xJWf5al9rWwhk7zZnffPkd0aFRIXhs0ncyeKZY4yIOa5dCKww68MjTRmo3J7lGrZilY1_JhhU9qt2BBtl6dztvjZwce9KEuQ__SDQ4iH9jMV8pJUikoJAQWYNPkGqoA-M4BWeNofxgcTEBoWb_a3jnRmHgf-QDVEA40yrTFr4qiwqRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان در سازمان ملل: ما تروریست نیستیم، ما قربانی تروریست هستیم
🔹
من از ایرانی می‌آیم که رهبر ما را بدون هیچ دلیل و برهان و قانونی ترور کردند.
🔹
من از ایرانی می‌آیم که در آن آمریکا و اسرائیل یک مدرسه را بمباران کردند.
🔹
در لامردِ ایران آمریکا به سالن ورزشی دانش‌آموزان بمب خوشه‌ای شلیک کرد.
🔹
آمریکا خودش تروریست است اما به می‌گوید تروریست.
@Farsna</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/463919" target="_blank">📅 17:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463918">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در منطقۀ جازان عربستان خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/463918" target="_blank">📅 17:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463917">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‌ هلاکت ۳ تروریست در سراوان
🔹
معاون امنیتی و انتظامی استاندار سیستان‌وبلوچستان از هلاکت ۳ نفر از اعضای یک تیم تروریستی در درگیری با نیروهای امنیتی و نظامی در شهرستان سراوان خبر داد. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/463917" target="_blank">📅 17:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463915">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gjda0uDgoE3cJiFQd3NsPvgo3BNP_bdgVj1ak65T2FgJ58oVX2X7D2mafKWvFE9LO8WP9Bb3w1bY7H3mwr-sAH-eypG7AwQ87XKNkrHxQhnx31qGBHwwuWvxoqkSU5A4rqi_F-Oy7Sme-RRqDrRTxwnsmfYCoVD_l8c5yHRZn3_HmLFlV1IQ-J3mDU9HfNBW8bg4i1r8vxWPSRVlu8OQNNGZA3NFw9ZnT3FAw6kyw3-yL0B8C8ShM26wLJxl57SOBZuec6fcF-QNt0yLQTpm0kHO9YlZbZ2n8qwCJmIQ8IYqGc_gk4HUqQTABVVA0ReOJ-uu-Tqulqom1UihdRTBSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/azrm1j1wnifnWw7Dlk5MSTiaFO47odhiGSeltSHu3tsr_gK3YtDgnGsK5KD_qedkh3M9xWmaIAA_Q4ep2LHr1R3qNMsjdBKwzCaju0Ky6yWp1aT4fwVeFoRqVJ6kOU3vOqx-bYGUu8L_LTd4H-hgLxZr-wkJ5aGEa-FcEL1-MWBjys28kTltX39Uo3uvBaCiw-zbE1r1O3zyIUXye1IdawCkHMLmGmxMSIJLkXxZRzR-coNQrBI2hO_kFLIp9V4G8zQkutjfSs26BLm3l79gzUrMwgAsRUzRaAubWZkLFq-toyh_oVPzbRgfQU2roopRawzLcDalsoye2XWNw5d-2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: پاسخ‌ رئیس‌جمهور احمق و متوهم آمریکا را رئیس‌جمهور ما طی ساعات آینده خواهد داد.  @Farsna</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/463915" target="_blank">📅 17:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463913">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316b4b36fa.mp4?token=FfT-15QyTN1F6peH4I8s99rpcTXDFSAFuitIj0C5z_m_CS5FSIV1Bc70aZ1U_ajyRIk8R2kU3wr3FCdKYmpDTXz2_jY0-c3dCoCY2tpnN6OZVw2JGRpEo6en3_b9U_4ERFWlkagl4hm4VsflnMQnu7XH9kWDTCV33Xo3KgFXrKWcCDpqV2O0CaL9rlJe6El0lRdM8VazOSsLJMyDnffFv0M_kTQv4jOBeA3sK_uogaJa_W4WjM7bVTzDSnNElf3x8GN28hZnAsg6rz4IiIUKW6ZE6DLUltgKBSYcOXc1HglmQG63AS1lkKz0xoNp6deN2qFMUnyAapnN6e_yha5lJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316b4b36fa.mp4?token=FfT-15QyTN1F6peH4I8s99rpcTXDFSAFuitIj0C5z_m_CS5FSIV1Bc70aZ1U_ajyRIk8R2kU3wr3FCdKYmpDTXz2_jY0-c3dCoCY2tpnN6OZVw2JGRpEo6en3_b9U_4ERFWlkagl4hm4VsflnMQnu7XH9kWDTCV33Xo3KgFXrKWcCDpqV2O0CaL9rlJe6El0lRdM8VazOSsLJMyDnffFv0M_kTQv4jOBeA3sK_uogaJa_W4WjM7bVTzDSnNElf3x8GN28hZnAsg6rz4IiIUKW6ZE6DLUltgKBSYcOXc1HglmQG63AS1lkKz0xoNp6deN2qFMUnyAapnN6e_yha5lJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: ترامپ ممکن است بخواهد در کوهی در ایران کاری کند یا به سایت‌های هسته‌ای ما حمله کند ولی ما همین را هم تحمل نخواهیم کرد؛ طرح نیروهای مسلح ما برای پاسخ آماده است.  @Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/463913" target="_blank">📅 17:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463912">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656e877e1e.mp4?token=uE7jv2-dIjNe-Dovimgf1JofPKqL3AjzCLKgK9A0Db0v4rJ1fWPvtfCDNbmhAZZQOXnwkcnTdDxR571UMvls_xnGHsbC2KRvDu-ELv8Memyqd7QyBN1by4H2UpJJd_Vq0uS8xWJGnDXTMw6HgHi9AxzuQD9gWxxU1pfwGquhugM6i5mVtu89hobz7NVgXrRFKTWwB8JQIMZGWjD6HimMOFsTqbUXgmyeERcHlG6-KTlCst7_nZrBxN6NHfRxsaYfYwzwJ8NmIS_T-1nrycW9utpT1lURW98XM8e8UeCjTLCQqmYLBQ8hdxv6aBde0bKKa_-Y015ZoPFDHWPxi8eOkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656e877e1e.mp4?token=uE7jv2-dIjNe-Dovimgf1JofPKqL3AjzCLKgK9A0Db0v4rJ1fWPvtfCDNbmhAZZQOXnwkcnTdDxR571UMvls_xnGHsbC2KRvDu-ELv8Memyqd7QyBN1by4H2UpJJd_Vq0uS8xWJGnDXTMw6HgHi9AxzuQD9gWxxU1pfwGquhugM6i5mVtu89hobz7NVgXrRFKTWwB8JQIMZGWjD6HimMOFsTqbUXgmyeERcHlG6-KTlCst7_nZrBxN6NHfRxsaYfYwzwJ8NmIS_T-1nrycW9utpT1lURW98XM8e8UeCjTLCQqmYLBQ8hdxv6aBde0bKKa_-Y015ZoPFDHWPxi8eOkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: در دیپلماسی جدید ما اهرمی داریم به‌نام تنگۀ هرمز که تضمین مذاکرات است
🔹
تنگۀ هرمز ابزار دستیابی ملت ایران به حقوق خودش است. @Farsna</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/463912" target="_blank">📅 17:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463911">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8337156e77.mp4?token=C89iKQ__59LMOKzHJPIoRHHe3z0SrQXSluVhUmaSOZqHGVzDR2ce2MCXj2QpZVsUiKMuaEZgiFyPEdUZC414IwqUGmoBAVOpGmUDHcliJRJBWeWyFSbJ8s0M-JQDJ1pLjMFH1JVf6BtrflnnJUB5RgpoK7379VYE0TYQBlbdJsy3i8wd-_kRvYCDZzBwrRhEtpI0K_av8EfvXIlMSq1fQepnPAQpyrUPk_x2x4mKsgeiadMG5nPjjnvWZgulqFsvvZCYOkC1wpoDTYYd1LMpGh76pbIsoQaLUzICEj5EEVRi4Z91QOxpz_FHVaEyQQFjZoadF3nDs1UJ5d8kQmZ9vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8337156e77.mp4?token=C89iKQ__59LMOKzHJPIoRHHe3z0SrQXSluVhUmaSOZqHGVzDR2ce2MCXj2QpZVsUiKMuaEZgiFyPEdUZC414IwqUGmoBAVOpGmUDHcliJRJBWeWyFSbJ8s0M-JQDJ1pLjMFH1JVf6BtrflnnJUB5RgpoK7379VYE0TYQBlbdJsy3i8wd-_kRvYCDZzBwrRhEtpI0K_av8EfvXIlMSq1fQepnPAQpyrUPk_x2x4mKsgeiadMG5nPjjnvWZgulqFsvvZCYOkC1wpoDTYYd1LMpGh76pbIsoQaLUzICEj5EEVRi4Z91QOxpz_FHVaEyQQFjZoadF3nDs1UJ5d8kQmZ9vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دبیر شورای‌عالی امنیت ملی: آمریکایی‌ها وقت را تلف نکنند و شروط ما را بپذیرند؛ دیپلماسی ما به عقب بازنخواهد گشت، برای بازشدن تنگۀ هرمز شروط باید عملی شود.  @Farsna</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/463911" target="_blank">📅 17:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463909">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e65ab9911.mp4?token=qyIDTSVdCp2X2tlSvkvaZ4KY8GD5mmXk9ooHXJcgjC_W6gQyAYaIrDiLBFPuKSapJsc-F_1gPOPe0nRGGUeJ2C3qIwmFVgf9OnUN6JdU0AooFHnNV1zFVTM0ST-wlFNkusTJ93AVgd4JuW2dBoSpfpGFX5WjJwjsow43dzjuv1m8scefBST8lFxFqt1DY2sCRSE6fraakvmGRL4yloe0tpt68zhZTHtfBzR-mxObyHDZqw_4Viw0IQt2_f5eOBBZT1O8D_XLwcOn_gYGLkk7H1VshjYhdI9yOXdHvGVTLRBid99d7Snryce0LAUOAYgXy8XcP2axrPqdgL4lHTSfsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e65ab9911.mp4?token=qyIDTSVdCp2X2tlSvkvaZ4KY8GD5mmXk9ooHXJcgjC_W6gQyAYaIrDiLBFPuKSapJsc-F_1gPOPe0nRGGUeJ2C3qIwmFVgf9OnUN6JdU0AooFHnNV1zFVTM0ST-wlFNkusTJ93AVgd4JuW2dBoSpfpGFX5WjJwjsow43dzjuv1m8scefBST8lFxFqt1DY2sCRSE6fraakvmGRL4yloe0tpt68zhZTHtfBzR-mxObyHDZqw_4Viw0IQt2_f5eOBBZT1O8D_XLwcOn_gYGLkk7H1VshjYhdI9yOXdHvGVTLRBid99d7Snryce0LAUOAYgXy8XcP2axrPqdgL4lHTSfsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: مطرح شد که ۷ شرط ایران را آقای عراقچی به واسطه‌هایی که بین مسئولان ما و آمریکا رفت‌وآمد دارند ابلاغ کند.
🔸
تا این شروط عملی نشود نه تنگه باز می‌شود و نه مذاکره‌ای درکار خواهد بود. هیچ تحولی ایجاد نشده و فقط ما شروط را ابلاغ کردیم.…</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/463909" target="_blank">📅 17:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463908">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5087f76949.mp4?token=QKuULVWVvCYWtVkFtiVV3U5W2yX_RQQuEBYHcyRwc4J95R5j0aLtHKYuMq2ieWYiB_bhI7aOxFCrnL2V0dse9aHqo2YI4PUwFclQFKiMLBcPkIdQ-kOtpjPBRUDiOE9CirHnRn_QuqpdIOCurw5K63QGXM7C655fdJlOfgo7Po1uS2ocsB9a4rN_hfv6zgLaR_bKf9TEQVdaSX8jyuqfV1ZAh-CJnQc75TrjRbimRkyxotuom6Pk--HwM4zZW25BslFeazzCXxA12CQUGIcDkTonDDgMyi31sJ1eADBwCXlJh2e7aXOro13QxHiHSt5P-hT3yTK4KTyBxGfNSfH_VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5087f76949.mp4?token=QKuULVWVvCYWtVkFtiVV3U5W2yX_RQQuEBYHcyRwc4J95R5j0aLtHKYuMq2ieWYiB_bhI7aOxFCrnL2V0dse9aHqo2YI4PUwFclQFKiMLBcPkIdQ-kOtpjPBRUDiOE9CirHnRn_QuqpdIOCurw5K63QGXM7C655fdJlOfgo7Po1uS2ocsB9a4rN_hfv6zgLaR_bKf9TEQVdaSX8jyuqfV1ZAh-CJnQc75TrjRbimRkyxotuom6Pk--HwM4zZW25BslFeazzCXxA12CQUGIcDkTonDDgMyi31sJ1eADBwCXlJh2e7aXOro13QxHiHSt5P-hT3yTK4KTyBxGfNSfH_VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: ما دیگر به دیپلماسی گذشته و اوضاع اسلام‌آباد و قبل از آن برنمی‌گردیم؛ آمریکایی‌ها اول باید ۷ شرط ایران را عملی کنند وگرنه نه تنگۀ هرمز باز می‌شود و نه مذاکراتی آغاز می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/463908" target="_blank">📅 17:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463907">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e0d56947.mp4?token=UObKgfK9BLUZt4iM3Q3BoaQaWPQepEv-VGAk5kIggUtrmoJ541NKA3ADMrQ-a0fiwaSzU5PjBvflxcQ3qFylFVGlpSqIkUw764UA9L82khHdOpMGNuPY9nR4fp-_aTsLKaXoJI7_O_ePGMsXi280y5FrMK70961K7gMonc0WioEkyDgNpNdotAe53bOFG4PuTIjw5R8qiIvBDGfuYoQPrp4SMFn-yreQEfM_hhO4brYR98iKODi1VzcmCrJd0vh-81MMWO6Zh0HZnJd2G4dJYFcMSDwx8eP4T3J_rlnRHEyaEwQsf82jLh4noxVmBTlzRIkS0WMUPqo_QEWCwqb4gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e0d56947.mp4?token=UObKgfK9BLUZt4iM3Q3BoaQaWPQepEv-VGAk5kIggUtrmoJ541NKA3ADMrQ-a0fiwaSzU5PjBvflxcQ3qFylFVGlpSqIkUw764UA9L82khHdOpMGNuPY9nR4fp-_aTsLKaXoJI7_O_ePGMsXi280y5FrMK70961K7gMonc0WioEkyDgNpNdotAe53bOFG4PuTIjw5R8qiIvBDGfuYoQPrp4SMFn-yreQEfM_hhO4brYR98iKODi1VzcmCrJd0vh-81MMWO6Zh0HZnJd2G4dJYFcMSDwx8eP4T3J_rlnRHEyaEwQsf82jLh4noxVmBTlzRIkS0WMUPqo_QEWCwqb4gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: داریم زیردریایی آمریکا را مهندسی معکوس می‌کنیم
🔹
این زیردریایی تا ۶ هزار متر در اقیانوس تجسس انجام می‌دهد و فوق‌العاده ارزشمند است.
🔹
شاید برخی کشورها در آینده به ما بگویند فناوری آن را به ما بدهید و در قبال آن چند میلیارد دلار…</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/463907" target="_blank">📅 17:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463906">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c4a673395.mp4?token=U0gHnASI2a_QUpm9gyx67q7JxYy0JLdxejGJyhi3usz7E8iDzXixMcLTmIvEsbKzHm5t8S5SYbuWnRhm2SRHZKHIbAS_F7DTnz7zGLOX0OK4NFsnqUHP2xDvQZrskM-2Qk6zfPm9bRNfkLLVABsNI5FKz3LJjDoLiYLyUtpz-1HrZRQOSF9F3nvz88dItnX_pgwicDV3nVAe9m33QA63Q7aiPFu3iGGnwBnn6uccsYxSpsPbTOWU9IDKWzO_ZsW-DzJOtQjjsoAOivyRfSxTlh_MKd1vf9oDDJJc72qE6UIFmy3hoSb4LQGNRKX8HIHiYdDlrtMcTzPTlqHtd5kzUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c4a673395.mp4?token=U0gHnASI2a_QUpm9gyx67q7JxYy0JLdxejGJyhi3usz7E8iDzXixMcLTmIvEsbKzHm5t8S5SYbuWnRhm2SRHZKHIbAS_F7DTnz7zGLOX0OK4NFsnqUHP2xDvQZrskM-2Qk6zfPm9bRNfkLLVABsNI5FKz3LJjDoLiYLyUtpz-1HrZRQOSF9F3nvz88dItnX_pgwicDV3nVAe9m33QA63Q7aiPFu3iGGnwBnn6uccsYxSpsPbTOWU9IDKWzO_ZsW-DzJOtQjjsoAOivyRfSxTlh_MKd1vf9oDDJJc72qE6UIFmy3hoSb4LQGNRKX8HIHiYdDlrtMcTzPTlqHtd5kzUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: ما برای اولین‌بار توانستیم موشک‌مان را بالای سر ناو هواپیمابر جرج واشنگتن منفجر کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/463906" target="_blank">📅 17:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463905">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d21ae2331.mp4?token=mhopG_un9LBM3bHyTH9x56gd3H6FSlbw-Usm50mzwhL_zppcLm5jk3mMiDXALH8RyFpFDK9PZtzT2gW6uHdG0UvBi9CZjhE0lXK5tK2cvuqu-G_7OLXkO8P7T5Aubczq603uVRr065vxt_zJa7E-eWVow-UL1EM8wLq_Tk5kiAHnjUOx4iU6e6EnDckitDcknccU50ZZmBlavFjJOJOwAGYYMb7AQoaDbjmMCv_c6To8GTFFA6uzm1joSLlRD5c80Ae1R_ZV-V9djXLg2GM6X2B3cPqj4Apayo42F-BgY4UnCNaJdRnIndUkR0Hj3OewGy7UAqJwhdY788hxfFJv8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d21ae2331.mp4?token=mhopG_un9LBM3bHyTH9x56gd3H6FSlbw-Usm50mzwhL_zppcLm5jk3mMiDXALH8RyFpFDK9PZtzT2gW6uHdG0UvBi9CZjhE0lXK5tK2cvuqu-G_7OLXkO8P7T5Aubczq603uVRr065vxt_zJa7E-eWVow-UL1EM8wLq_Tk5kiAHnjUOx4iU6e6EnDckitDcknccU50ZZmBlavFjJOJOwAGYYMb7AQoaDbjmMCv_c6To8GTFFA6uzm1joSLlRD5c80Ae1R_ZV-V9djXLg2GM6X2B3cPqj4Apayo42F-BgY4UnCNaJdRnIndUkR0Hj3OewGy7UAqJwhdY788hxfFJv8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: ما ثابت کردیم که آمریکا حریف ایران نشد و در آینده در جنگ با ۲ قدرت رقیبش هم با مشکلات جدی مواجه خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/463905" target="_blank">📅 17:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463904">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/945c6dd294.mp4?token=kyQnW3YY8Vfyz2PtLEk3fiNB6iYIVlxRIf0zDPznH58c6ikt23qExWkvdNEfcbPqLbs9rHNoacNa2YFYg-EyLTV2X5LmOSxDKo7K7aR7HRNpmHj1p5vXgt3VTJVH-yqGfQglnT73TZipnz4dCriASpGEnm15CYZnGEfybPoIU8QaQdB6FjAbi1h2LTd6X0qstpdxQmzLujoVASH2hDBCXdQPel7J9a07W-Xei0Jj0rRNm4m3o1NriKCau7ppCWUolYTquLo8-T69DA4Jd1YIjaBNZuBlBDNTgNOuotbeGaYhB79sROcWURln1E8N66JNzGio5oXhVLUCneejW7_Ysg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/945c6dd294.mp4?token=kyQnW3YY8Vfyz2PtLEk3fiNB6iYIVlxRIf0zDPznH58c6ikt23qExWkvdNEfcbPqLbs9rHNoacNa2YFYg-EyLTV2X5LmOSxDKo7K7aR7HRNpmHj1p5vXgt3VTJVH-yqGfQglnT73TZipnz4dCriASpGEnm15CYZnGEfybPoIU8QaQdB6FjAbi1h2LTd6X0qstpdxQmzLujoVASH2hDBCXdQPel7J9a07W-Xei0Jj0rRNm4m3o1NriKCau7ppCWUolYTquLo8-T69DA4Jd1YIjaBNZuBlBDNTgNOuotbeGaYhB79sROcWURln1E8N66JNzGio5oXhVLUCneejW7_Ysg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: ترامپ خودش متوجه شده که جنایت‌کار است و خودش و نتانیاهو جان سالم به در نخواهند برد.  @Farsna</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/463904" target="_blank">📅 16:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463903">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/254ad4c36d.mp4?token=EOoT9ORnl9CxslXFpXTZChNMvNJ-bo0xtMIpjz5APmRP_AffuYNLCHf9xLjaTN0rKyhP5ySJv0Q5FFRB5_CbtsbRTJIf9tEhZAwAiqVKklfv7bBhePWvhpGy_KNV6hN1eONUV4HzmNlPfxiP3innz3KVMH_8PCJQnwoSj9Bt1EdagCbGlJmw2YXT2_hD4pHmE1oH4cBjtf2PBtIMzqljeZRdKywtVR0wb8bIaG8cC9G6hkSVT-C1OlBJPsdrb3t5BXRm_LpWvxnYd2Z8pxDjCQBAfxW4wst1tr3VtRsFwjNC0ihxeWdO9a83jo4n7JIRxYprAtQDaICM1-f4LiiHiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/254ad4c36d.mp4?token=EOoT9ORnl9CxslXFpXTZChNMvNJ-bo0xtMIpjz5APmRP_AffuYNLCHf9xLjaTN0rKyhP5ySJv0Q5FFRB5_CbtsbRTJIf9tEhZAwAiqVKklfv7bBhePWvhpGy_KNV6hN1eONUV4HzmNlPfxiP3innz3KVMH_8PCJQnwoSj9Bt1EdagCbGlJmw2YXT2_hD4pHmE1oH4cBjtf2PBtIMzqljeZRdKywtVR0wb8bIaG8cC9G6hkSVT-C1OlBJPsdrb3t5BXRm_LpWvxnYd2Z8pxDjCQBAfxW4wst1tr3VtRsFwjNC0ihxeWdO9a83jo4n7JIRxYprAtQDaICM1-f4LiiHiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: یکی از حماقت‌های ترامپ همین سخنرانی‌اش در سازمان ملل بود؛ چون در جایگاه جنایت‌کار شکست‌خورده به دفاع از خودش پرداخت
🔹
این سخنان نشان می‌دهد که بزرگترین مشکل ترامپ و سیاست آمریکا، ایران شده است.
🔹
تمام سخنان ترامپ مثل دفاعیه از…</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/463903" target="_blank">📅 16:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463902">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyrIH1rT0etqA0TB5qpWLcKhE8uGvWvMB7pk_6F0XS5UFynq1e_VSL2ct2uw8QENClJPI4_UQAFKxiSGimpNtzHqbraaXE3H_eUM40zfbcrleG9JVOymNQyg2GB9CimkOo8hLHhk-glQzCmcw_IImAd8zXCH5-m3n0b8zNVuqFTlRmM1D-mx0vDZ6ESyuXb_jSvFuTyjWoh7AYQkFXkstx-LkVe4t79pJm_30NpR5v904RPPUD1wZOy41xIZoEgKmNnS-9ycUxBH7B1M1pSD1rmJpbBUtOtiF_sKzD3_yiXAgs_1nveDlXlBnAsBsQr3au7msZeB_QjXOYs8kwYLtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلاش نافرجام مدیر سابق برای مدیرعاملی استقلال
🔹
باتوجه‌به بررسی گزينه‌های مديرعاملی استقلال در هلدينگ خلیج‌فارس، همچنان مصطفی متدين بيشترين شانس را برای رسيدن به صندلی مديريتی آبی‌ها داراست.
⏺
كميته انتصابات هلدينگ پیش‌تر در جلسات خود گزينه‌های مختلفی را برای اين سمت بررسی كرده ولی همه آنها رد شده بودند. از جمله اين گزینه‌ها كه برای بازگشت تلاش بسیاری کرده يكی از مديران سابق بوده كه توسط شريعتمداری در هلدینگ خلیج‌فارس و علی تاجرنيا بركنار شده بود.
⏺
شنيده می‌شود در كميته انتصابات اين گزينه به دلايلی چون رد صلاحيت توسط نهادهای ذی‌ربط، انعقاد قراردادهای عجیب‌وغریب با بازيكنان داخلی و خارجی، ارتباط با ایجنت‌ها رد شده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/463902" target="_blank">📅 16:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463901">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72dbdea702.mp4?token=JrJhv6S1X2UaevmUSSXNTCzUcrTdQ72R6zWBuZ5C5Uu3RReHtth2VrdYEo3-ln9fE6XesEBpa4rnUJV8Qby653gQ6gaaPa6CN1HjWnCFSZ_79J2aobUy8EC2-xLWKvLMh4cRJo9_u818ruK9Lvgqa652jvWHxEfuQyn0clD9b_sBru3q3Ep3XEKzhJ56xEcbd0WzriuZWuIqO4bDad2ty5taiQz1_mQEL-Ct6EUdkJRf-YMghEWiZ3L_KicVn2yamTELAllhOn30dhDlAgX7Lr-tj9xr4Ms73dHQKguiQCA_RTnxci282scfS5It4i_CQQtmhAZT0F5dYrpV7JDUig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72dbdea702.mp4?token=JrJhv6S1X2UaevmUSSXNTCzUcrTdQ72R6zWBuZ5C5Uu3RReHtth2VrdYEo3-ln9fE6XesEBpa4rnUJV8Qby653gQ6gaaPa6CN1HjWnCFSZ_79J2aobUy8EC2-xLWKvLMh4cRJo9_u818ruK9Lvgqa652jvWHxEfuQyn0clD9b_sBru3q3Ep3XEKzhJ56xEcbd0WzriuZWuIqO4bDad2ty5taiQz1_mQEL-Ct6EUdkJRf-YMghEWiZ3L_KicVn2yamTELAllhOn30dhDlAgX7Lr-tj9xr4Ms73dHQKguiQCA_RTnxci282scfS5It4i_CQQtmhAZT0F5dYrpV7JDUig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: پاسخ‌ رئیس‌جمهور احمق و متوهم آمریکا را رئیس‌جمهور ما طی ساعات آینده خواهد داد.  @Farsna</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/463901" target="_blank">📅 16:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463900">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f70T0Akz4JP1-zxaOlDVUbutLhvMt_9x4OGDj_zf_vPy-curAyjOyCzCfrBiVqOvBNTAzYP5_Kxm-jGean-xVHDbx9_LSh07PeL1rZULZyIwtqR4qKQKQpG1zj1YRFUSvFjZ1kvmjW4aPQKkLOys8wlUCVjaZZfcu99_E7F6FXU_7nU6J3CzQPz9VbG7Fvhgp07foqFe79KgETiO5Y-yupfb3LdcNfJGUXmI9EqIFv5d0wXLAxbTpNN7czpDQfP2EyG6ISaFU1TRCz6KfbPtJOh003anmC513DgQghtondhnbdA7iMvgbFAbNZAEw64E3Q7DIe6hlSKOdj6HXqTOnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقایی: همه کسانی که در برابر جنایت در مدرسۀ میناب سکوت کردند و از محکوم‌کردن آن روی برتافتند در این مسئولیت شریک‌اند
🔹
مردم ایران برای همیشه این چهره‌های زیبا و فرشته‌‌گون را به خاطر خواهند داشت؛ و هرگز قاتلانشان را نخواهند بخشید.
@Farsna</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/463900" target="_blank">📅 16:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463899">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b85e9660.mp4?token=uvi_VFJ9_16zRWOYKp7Ir5lZ8F4mp9oVcXJz1R8NR8BGJgxTjgt1pqpKvjQWQkGtuf1oGYX_Yttib4cyEE8OCo5FV39piRq148S76qLxS3jYZ1FRUY2L9Fl6ucgulHU3X2QIuAh9NFqxzOwAheFUGKtn8CDzRe2MLiCG2pn-t2oXgUIKHfPVc4D2e1hqG6RHW61xSa4l5DEregQ9K4mAsoSBFG5dAm7xxdh2dQPIDOU79E4Rmp29uaiIjjNVroSd66gENUgI9A1ZEot8nComwiNGrCwplTbXAffc5XEWCi_txQ30CxAJzBHUhCF72LItRpNafroTfsKtZFgyHlke_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b85e9660.mp4?token=uvi_VFJ9_16zRWOYKp7Ir5lZ8F4mp9oVcXJz1R8NR8BGJgxTjgt1pqpKvjQWQkGtuf1oGYX_Yttib4cyEE8OCo5FV39piRq148S76qLxS3jYZ1FRUY2L9Fl6ucgulHU3X2QIuAh9NFqxzOwAheFUGKtn8CDzRe2MLiCG2pn-t2oXgUIKHfPVc4D2e1hqG6RHW61xSa4l5DEregQ9K4mAsoSBFG5dAm7xxdh2dQPIDOU79E4Rmp29uaiIjjNVroSd66gENUgI9A1ZEot8nComwiNGrCwplTbXAffc5XEWCi_txQ30CxAJzBHUhCF72LItRpNafroTfsKtZFgyHlke_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
واکنش‌ ستادکل‌ نیروهای مسلح به تهدیدهای ترامپ: آمادهٔ واردکردن ضربات شدید به آمریکا و رژیم صهیونیستی هستیم
🔹
تکرار ادعاها و تهدیدهای بی‌اساس، با توجه به فرسودگی ارتش آمریکا، نه نشانه قدرت، بلکه نشان از استیصال راهبردی آنان دارد.
🔹
لفاظی‌های رئیس‌جمهور…</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/463899" target="_blank">📅 16:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463898">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc32ea4288.mp4?token=a7VAj-Ka2hlqLGmtmdvvIYnb1kWmfT5mDSvrcwvyP8U9fZKHsEZWDAO4p-uI9YxZRX9Td4uZbuK6LXn6ESKs7xi5W8o7I9ipRDUQ8XygU5QKlUHDmoyL_tCkMNoE1RtwJW8Ewo9sgsVMWYhYFoxYktsSdLgj4oUilRYtUkGSR5KEvznBxt1gYW9UmiOYK8X_SZ18ypIVLGw7nXaOW8mpv2lS8fVnQArtiF_QCwxJdNkUEIN5l7mC0soTKL8M1mlFIWdp2DLigrUmuDleBMUj3elkmt-weaucYGC2fzW9KLJMn4-_Nt9WrcOR81XJisIPFWrbfthcufsXu4kzi0hvLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc32ea4288.mp4?token=a7VAj-Ka2hlqLGmtmdvvIYnb1kWmfT5mDSvrcwvyP8U9fZKHsEZWDAO4p-uI9YxZRX9Td4uZbuK6LXn6ESKs7xi5W8o7I9ipRDUQ8XygU5QKlUHDmoyL_tCkMNoE1RtwJW8Ewo9sgsVMWYhYFoxYktsSdLgj4oUilRYtUkGSR5KEvznBxt1gYW9UmiOYK8X_SZ18ypIVLGw7nXaOW8mpv2lS8fVnQArtiF_QCwxJdNkUEIN5l7mC0soTKL8M1mlFIWdp2DLigrUmuDleBMUj3elkmt-weaucYGC2fzW9KLJMn4-_Nt9WrcOR81XJisIPFWrbfthcufsXu4kzi0hvLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
سخنگوی شهرداری تهران:  گفتند حال مادر ماکان چند روزه خوب نیست؛ پرسیدم علت کسالت ایشون چیه؟ گفتند: اول مهر.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/463898" target="_blank">📅 16:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463897">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">طالبان و پاکستان درگیر شدند
🔹
روزنامۀ ۸صبح افغانستان از درگیری طالبان و نیروهای پاکستانی در مرز دو کشور در ولایت پکتیا خبر داد.
🔹
این درگیری چند ساعته ادامه داشت و به‌گفتۀ منابع، شماری از گلوله‌های خمپاره به خانه‌های مردم اصابت کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/463897" target="_blank">📅 16:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463896">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e66e9f8a0.mp4?token=OulthoXzX08Ytoh4maa8oO3AyW3jgUZv6jkZJEcbOV58oYDe5vwMgrfA5z06ax6SPKQ-g6Yp9X2_O9PSLMbazqV_NutDW9a89greZ5goBJoaRkbD7YOMvbpyYgDNX06ToLzmIjWDPzaIBuuYZ2OvhnM1mbr3vSwrsH5eMgQrDYtpISoxIt2fz8x-qHd72qhn5SdBpHKhJN9HGxLUhKT2GzHKghei8q6z8aPJhB2_LfcX1ZzQ3gk46x4AsDi3OHryIQMQjCz7YFCyq4nNV-j6ngj-4cWEPb75DNcZuQz7t77PHYAwGcjaMgrE2KIY0pEw_dWoZPRlqWZfvNEPmghjQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e66e9f8a0.mp4?token=OulthoXzX08Ytoh4maa8oO3AyW3jgUZv6jkZJEcbOV58oYDe5vwMgrfA5z06ax6SPKQ-g6Yp9X2_O9PSLMbazqV_NutDW9a89greZ5goBJoaRkbD7YOMvbpyYgDNX06ToLzmIjWDPzaIBuuYZ2OvhnM1mbr3vSwrsH5eMgQrDYtpISoxIt2fz8x-qHd72qhn5SdBpHKhJN9HGxLUhKT2GzHKghei8q6z8aPJhB2_LfcX1ZzQ3gk46x4AsDi3OHryIQMQjCz7YFCyq4nNV-j6ngj-4cWEPb75DNcZuQz7t77PHYAwGcjaMgrE2KIY0pEw_dWoZPRlqWZfvNEPmghjQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط جنگندهٔ انگلیسی در ولز
🔹
رسانه‌های انگلیسی گزارش کردند که یک جت آموزشی Hawk T2 امروز لحظاتی پس‌از پرواز در پایگاهی در ولز سقوط کرده و خدمهٔ آن ایجکت کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/463896" target="_blank">📅 16:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463895">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyZ_48eVGvweV-_BnM-j8ICQzIHuWnvcezPRV-dW3icNPIPKmqTj4zEwg2N76AGc3hXl6tiI6lrDLlPUzOvpRubaZubIg8hfUjdI0AvPa3OH4ddpX10jGcgv2sV6MQatdWnck4GnVc9nKftNYb1E97mpbgYnctSN2SHI8PBfdNrozlUF9odlpBaP-yLHhgw4Ewk_WhHD8ixnAx2zhDE6-uZcywgNOuOQWvyb1dnGgXJC4iwjVkvRatKDWyCAhzu8VPce3TtC8EhB4ZayoAt9DrkqDc-SguImp8XmsyuZGJjDB_3rML8o1ovo6ZDQc8r5STa5uw-uAn6FI0oKlaFAHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نفت دوباره ۳ رقمی شد
🔸
قیمت جهانی نفت برنت از ۱۰۰ دلار عبور کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/463895" target="_blank">📅 16:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463894">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
پاکسازی خانۀ تیمی تروریست‌ها در جهادآباد سراوان
🔹
یک منبع آگاه از انجام عملیات ویژه برای پاکسازی خانۀ تیمی در منطقۀ جهادآباد سراوان خبر داد و گفت عملیات علیه تروریست‌ها همچنان ادامه دارد. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/463894" target="_blank">📅 16:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463893">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f3837d385.mp4?token=MUsxSM8G31RP24FUi_BbjTPHeWRxVE55z_18MzOVcMpRsAuoSdQ3WDFDteV-rnjUpEz1HF--M4kb9UXU5gbR5zE1ZwxgngHsJux51CYGVVxSoanR3O4QDw5GClgTMCcZuZ__YzsAnDNnhoSlcsa4S8blPb6pU5noVo2aWkhpOruRdHZ8l7y8wq1Su5xl1kbkbwF7cqwNb5hv6LpXxzwjFrBwCpzRv2jPKs-ZbsW0dr1HF48Ey0hBSyHGL38N2V_LblWm3lvZkcd_70qhw8UMVmVFA1bKDEPOX1ZOgr3qTJCN4QZv8W_jPdKL4lBvAyOkW9JmzjhlMar-zRU632JHaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f3837d385.mp4?token=MUsxSM8G31RP24FUi_BbjTPHeWRxVE55z_18MzOVcMpRsAuoSdQ3WDFDteV-rnjUpEz1HF--M4kb9UXU5gbR5zE1ZwxgngHsJux51CYGVVxSoanR3O4QDw5GClgTMCcZuZ__YzsAnDNnhoSlcsa4S8blPb6pU5noVo2aWkhpOruRdHZ8l7y8wq1Su5xl1kbkbwF7cqwNb5hv6LpXxzwjFrBwCpzRv2jPKs-ZbsW0dr1HF48Ey0hBSyHGL38N2V_LblWm3lvZkcd_70qhw8UMVmVFA1bKDEPOX1ZOgr3qTJCN4QZv8W_jPdKL4lBvAyOkW9JmzjhlMar-zRU632JHaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پلی‌استیشن ایران طلایی شد
🔹
تیم فوتبال الکترونیک ایران (حسن پاجانی و ابوالفضل آقایی‌نسب) در فینال بازی‌های آسیایی ناگویا موفق شد مالزی را ۴-۲ (در مجموع دو بازی) شکست دهد و مدال طلا را کسب کند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/463893" target="_blank">📅 16:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463886">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WZmY3WCwJMc4CioETzD-uZM8FuY7nR-u284k8UkjgGtyVh8k3hEUNrZJzoomj6B3HCn3pnEvo652LsITce1j8_jf_8_zzlIpSpnAYT84scje09yH4VOBPDjxH7mHqTOVYH0SMpVu2NC09HZI1I-6aiQeWBr7l3MNd6EkViMeuC6nZDu8bLYbXr1moVJigH58FM6XYOrploOIH24F4WbSmQTqAzr8bZlF7M9ByXLN7iRWZX2iwBiQDrXcGfnid0u6wu4mrRogZbrjgmuTwgeoaZ4yj6cepHQXk4wnHyq4DsbLrgv6P5iFJugmEdPZLNdjgjqggYt9elxfYujX89Ir-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pooRh_-B0JqFZ1f-rB2uR3xRA1yqD4m8g10NQNU6gAinGugIpjR8vkEHTdfzmV-gVfGrAdpDOoJyyyfYjIjHh8ysq4KIJ2rQIUX8errUOQ3LTT3ul2AWy2_dBaLEvRtRWBaIc_vZwMXaGvUFa7ko7i4Rfm_7oC8sLIIQZWev2skUuM6DMeyZX-aruWB88c0Q50J7pOCtK_rTO2eUGR-E1OGr07q_EtwclAWl8uLp13S6ec3-ZtEj7mSfDUdkG6UcGZ_IgXc22EmlPU5Pfp_6LMV04oyzIWzGxlZNhQF6F6bcYpD_tHr7EIm425lTeNu5J1VUY3QfUkVZcGiVICd0lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WfQ9N_jtPGX_CUsOATV0tx430nQwgkqu0PfZBpXvBRquMLMUXtGL010PoLOazGjJCIAbiarFW86r_OPTOZtXUtuG6iWpW2rw2uVELvf1BizwlJLLi6jxKd9RQVWlNIiC7dAIbDvOSX64vNl6GSMr5kmHXg91HphjFqObGQG6yrG4WmxclzZchPsoWB7e7PhuAGrlbACsWgllSi9NnnnqS6hXESHE2iVnQEBncoziWqWZtJ95RvfO0W4xW6fhiFwoNq85Al-50QbfRrbav-dxADOtFgfb-JbdIY__6FlQVO_pQs8VUtlZQmTRWmTyMBC9aGUKllLaKEcF9teC0uZDmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qQwdSzn7OS5zwB174uVYl397cW06ReWfvBTj5Iv9q-dP6-vHG4NL6aer7tjsLxFRZPrA-tFhPpudstt15W6WWUiDdSDd52faXGD4yFt-tfdHjb_1i3smt5gGIPGuPNs0z9PZaJzYdlGTh26LviejRUZjdnBF_gs0zjfGr-iorWCyxrE7HsdSZUGRi7-aPoR0a5KSUXaHHEbjo-b7EXLHtkSdWt2Ln02twecih9VoK6LF2F9_amCJkBI6EYQL4s13h3WILOvHX12dVsMrayK2jDUoBXkodm5nSWtC_sc-tjzG7wAVjPoeg-bUrZaAdTIFyU3Jyf-YSU_EbqI2fgWVnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mo7sjCgNR963tsmsDt5hIDUHcPSQLfhMGZ3fE6O1P8XZPsQz9v_CC2Yr9wJqfmlarDshhLXp8ykTwgkiXjkfjAudMb0fuoB7ZJKu807heCfYmLtHHpKanYcDnSWCWcFDTnFpA0oQlhBCjfayN2hckzSkVy0f-Awqo-AIzL5WpMGrJsvwNFyLYo4I_q3_jFUxO7OclDKGuHhZyfQCXSi2mhJ19FgYSdAcfrfYO_yWEP-WNWpYdCC6EvuJQ7_q0gLCz4CXvh3rlUKQJxAdCu5yblBGM64-KM5B6-mRZsf8yQjGxSsbTPJfOvHenMS04M9Sawr5ls4UiLESgrGgbB4axQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MEnouD1tAuRfadBLokPT1EpjlpL--l2m7Gdu4KhnrMCzOqOjvFxH1J4Mno_Dt3TMzRLathoW2TCfFzOGyTB5AFFD8x5FPGALCoVTeAOtnZWxnkTQ-Q28CXWX4ISsZ_5a3pDMs3Y8NCZwtJruBZAZL7ZJuWSHqakxKlN5eddaGzg4LS8P9IuQX3dHunyUMREF0ovd0Gqy6wiwDZxb3dQsvTbrBYbxXW7bnO_9TmIJwL2a-w6V7CMP5YO4fvtPvsvymDjMP0xv7G-eTN02tgbSpdxdGKHdOnLG7nlJmm0j5h8f2EsY44kSFttZHg7wbFlDtrgIC-XztMwaG9zxl7al0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m1oo8gL99FDLrG34WWBx9wG35y6o1PfOLdHiBwR1d-J0ASL1v35LSvvXmwAhbHGhptfACoJuxycnieew2dydfYzdyC_ke4lvbsSOy83ziR6lv1CtBLVlQq4EOy4DpBXoP4Q2QOWu_3OWgV7okzCoHOyMm3XywpSUZkZYyCnzY8vo9DC2ekq8u8ixlU0RoAG8VKssPDa_l-rdJWKJ2NmZ9Apf8O8R4CwTJDC39gy_rexMLjbqBZFrtjeL4YXefYRUDNItZm1Kzdt8ZeZwZL-gP6fEFKniZ3DVBaYIt2ry6OIjCL-iua3jJdBHhF0F9cSXek1J0qTfIF6ReMNCbljVMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
روزی برای «پرچم»
🗓
یکم مهرماه در تقویم ایران اسلامی روز پرچم نامگذاری شده است.
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/463886" target="_blank">📅 16:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463884">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcaf48ab2b.mp4?token=Ybueu1F8pQygg-xxNwwYDxJe-oBoy5ki2xbPXu7Ef7no2YXEVVDkYIFPe-pUJUIXwePWe9SsGF5v13FziVJ4fcDxZnT2FR56p-5GxXE8T-7TGPSqJFyz7bQsxoJ79hZ4nRaBYUK1x3yp2myftDfrRb8vx2CSYvf8heBnJDhdWCdQD63m5Z3Dd5Zelp3S7rzObSgwxi73skYRnv0BZXvUmOFFJi8zO3yN1Y2MqIc5Bpc6ocC7vpQwGZphF-bfV05UF-s1qDk6P7qdHEnNQmdT8jnJsxUy2R-9zA7GtZ3P1FGUj_o3MQm5NA8baWVrpHIa99WZyWWioiRF22A6Ujd1fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcaf48ab2b.mp4?token=Ybueu1F8pQygg-xxNwwYDxJe-oBoy5ki2xbPXu7Ef7no2YXEVVDkYIFPe-pUJUIXwePWe9SsGF5v13FziVJ4fcDxZnT2FR56p-5GxXE8T-7TGPSqJFyz7bQsxoJ79hZ4nRaBYUK1x3yp2myftDfrRb8vx2CSYvf8heBnJDhdWCdQD63m5Z3Dd5Zelp3S7rzObSgwxi73skYRnv0BZXvUmOFFJi8zO3yN1Y2MqIc5Bpc6ocC7vpQwGZphF-bfV05UF-s1qDk6P7qdHEnNQmdT8jnJsxUy2R-9zA7GtZ3P1FGUj_o3MQm5NA8baWVrpHIa99WZyWWioiRF22A6Ujd1fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس مبارزه با قاچاق کالا و ارز: بسیاری‌از قاچاق‌های سوخت در کشور به‌صورت سازمان‌یافته انجام می‌شود.
🔹
در هر نقطه‌ای که سهمه‌بگیر عمده و جزء داریم، قاچاق سوخت هم داریم؛ در حوزه‌های حمل‌ونقل، صنعت کشاورزی و نیرو به‌وفور سوخت قاچاق می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/463884" target="_blank">📅 15:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463883">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8eyXxVVo1Ru8WQF9ig3jck-n3nANWGmdk5WCbVdG-iuPvCHI1Ao621BlOkcDs79yzBADFFMQDpDZ2QdWhoBgzNLcbAVcyxGumPz-2xSPfsGVgil8RzaXn6ePp_5a4k4VQ2RU_tXU1W0J1_A6l1J6PdCMLQ5B0jg0IDHlagqep_oB88yI5_52QgXDKsxvNforcjUhKXvkjZLQmSTOcPwqtdTdh3dRd6xvdgzXIs4UuwJoiUMR4ZO4t5l6biFi8eIMNhNLpVhjise8ZNpDg4-ytcfA-oU4tjjVD9sHdfx_JkGZ74YA5Vr7K8lLmhGGaiI0ykEtmN0az7lhks-HBBjdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی‌دلیگانی: نشستن نمایندۀ ایران پای سخنرانی ترامپ مایۀ ننگ است
🔹
نایب‌رئیس کمیسیون اصل ۹۰ مجلس: درحالی‌که عامل و دستوردهنده به شهادت امام شهید ما، کودکان میناب، کودکان لامرد و دیگر ایرانیان در آنجا سخنرانی می‌کند، واقعاً جای تأسف و ننگ است که افراد ایرانی…</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/463883" target="_blank">📅 15:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463882">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4171168b2a.mp4?token=QtKgHNoKM1jbTmYIy59u0X4w0YWm-hjtSz0jhZxnAQIzxZLU56kX8g87yKGo4vymGMgvTvwdrRVNu8pBPc_5O2HrEfV5o3kbbPUiyavU4GcrAu_t34ocOpnvocpO7shXQVgRooN1fTxyCEbYiuuuhdydVJZjMBqidmRPQmtcJpiaEzhfMcCLYuF6c2ITDOYQLr1sCLyctqJV8qKLIwPQx4VqP7Cm1028zA1WGf0Mmhnbwo4DxuptZXxUnPDLpwSpm2ifrM1cWloCni-p8ahv7CRDccsoPwcQeReSY2ngwbOUNeVDwNnPhDyIV_hKZOoq1y2UdyYxOp6mwvZ9H-vz4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4171168b2a.mp4?token=QtKgHNoKM1jbTmYIy59u0X4w0YWm-hjtSz0jhZxnAQIzxZLU56kX8g87yKGo4vymGMgvTvwdrRVNu8pBPc_5O2HrEfV5o3kbbPUiyavU4GcrAu_t34ocOpnvocpO7shXQVgRooN1fTxyCEbYiuuuhdydVJZjMBqidmRPQmtcJpiaEzhfMcCLYuF6c2ITDOYQLr1sCLyctqJV8qKLIwPQx4VqP7Cm1028zA1WGf0Mmhnbwo4DxuptZXxUnPDLpwSpm2ifrM1cWloCni-p8ahv7CRDccsoPwcQeReSY2ngwbOUNeVDwNnPhDyIV_hKZOoq1y2UdyYxOp6mwvZ9H-vz4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس مبارزه با قاچاق کالا و ارز: ۳۲ درصد از ۵۵ هزار پروندهٔ مبارزه با قاچاق مربوط به سوخت است.  @Farsna</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/463882" target="_blank">📅 15:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463881">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnKPABozTj-YI7Y0fMt1yrTYH6nJJ5gUnwUmacdOY8jW5jcUdWXAzLTJhtpBnnOHVvO3stD7IT1BJqHEFTx8MT_yxjllXxXNJ2ZRDaN2P-3P6TefPww4UpdNBGJjCQK2PepOznBto6Bm_HA3Jukdh26m39E83P8qtlmptG3_XipZxo0SW3SLBDnAFXu4YuZfMR2esuhM2J4Ag_-UC9FeB10fsvO7qk3UBPy4do4G6z6g96RiAXfe6Px952gFUduyGJjFy9BEuL7ZScFf_zQapXW0rMjZLJRssIRcT9zD7RxSs7YcqlGWeOsTq2PULOZI3OsX2BRL-hL4y-msKCso8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی سازمان غذاودارو: واکسن آنفلوآنزا هنوز توزیع نشده؛ هر واکسنی که به دست مردم رسیده قاچاق است و نباید استفاده شود.  @Farsna</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/463881" target="_blank">📅 15:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463880">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4ee_v75A2WFvaVkmWbx_4dOjdNLh1PWT5cEFrR5P44ar6Qk_Ngg4rG-Fs8r6tXMSAhoIzv7O15WQV2xT7m21d-0LMerwZ-wYg2rZTcM2WFWxvk8QOHaEn1wGE04zjQ3Cn3tVZoDEURfIL5vLLOY9_AYMWhFzGSXmM_t2fecfNy-p0l3PcVp2DmZwtDCaKnzx6EFBGHDJa3xdtLWa2IJqfM1gDOTUKahncTA16WG1D66_hdB3UkZVDlzWBffuIqqPt7hGDhGG3UWa2KHuwRVTYc2yA4PXi2lzXPBX8IakiQ_YtiYEv3n0a9Ao_cGUoczn3zFejuhLD7zx1Ca791wHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دکتر «علی محمد خانکی» به عنوان معاون مالی و امور شرکت های بانک شهر منصوب شد
⬅️
با صدور حکمی از سوی دکتر سیدمحمدمهدی احمدی مدیرعامل بانک شهر؛ «علی محمد خانکی» به عنوان معاون مالی و امور شرکت های این بانک منصوب شد.
⬅️
به گزارش روابط عمومی بانک شهر ، دکتر «علی محمد خانکی» طی مراسمی با حضور دکتر سیدمحمدمهدی احمدی مدیرعامل بانک شهر و جمعی از اعضای هیات مدیره، معاونان و مدیران ارشد؛ به عنوان معاون مالی و امور شرکت های این بانک معرفی شد.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/463880" target="_blank">📅 15:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463879">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک کارآفرین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd47d59cdc.mp4?token=hBePfQxrW67g3J8c0XumjmSaWncpuHG8CAUInhnEV1v5ks6U2OnAXDFk-__gqsNkdEsTreXJiIS9zm_5AZvUt9LeE5IL6RUL4WZmenx5PXKkd1LoE5TyDCK37nfCVYCov3-k6BpRzeaIgoZQHouUJYk9_4InujPgE3e_dvEq-WGgCDdMEBaok03RnZnyW3TVF2PIXKuvQ5sokQ6TgNpJ6HnacFHK80fSa3Y4WOxdvy-pW3_eDNQRHIJfS4Yh5Yc_Wdj9df_ifcClQVc6zoYWmrhO4TmNaYqQJ62jwAUxLe9uMeQ7KAaJ_NKVW-n_pe7ex1HsdDnoLo5FsAR0rk-LBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd47d59cdc.mp4?token=hBePfQxrW67g3J8c0XumjmSaWncpuHG8CAUInhnEV1v5ks6U2OnAXDFk-__gqsNkdEsTreXJiIS9zm_5AZvUt9LeE5IL6RUL4WZmenx5PXKkd1LoE5TyDCK37nfCVYCov3-k6BpRzeaIgoZQHouUJYk9_4InujPgE3e_dvEq-WGgCDdMEBaok03RnZnyW3TVF2PIXKuvQ5sokQ6TgNpJ6HnacFHK80fSa3Y4WOxdvy-pW3_eDNQRHIJfS4Yh5Yc_Wdj9df_ifcClQVc6zoYWmrhO4TmNaYqQJ62jwAUxLe9uMeQ7KAaJ_NKVW-n_pe7ex1HsdDnoLo5FsAR0rk-LBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بافتن پرچم، مثل ساختن آیندهست؛ تار به تار، نخ به نخ، باهم.
روز پرچم  گرامی باد.
🕊️
🇮🇷
☎️
۰۲۱۲۳۳۵۰
🌐
karafarinbank.ir
📱
@karafarin_bankف</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/463879" target="_blank">📅 15:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463878">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/463878" target="_blank">📅 15:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463877">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
هدف‌قرارگرفتن یک کشتی در تنگۀ هرمز
🔹
سازمان عملیات تجارت دریایی انگلیس اعلام کرد یک کشتی باری در داخل تنگۀ هرمز با یک پرتابۀ ناشناس هدف قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/463877" target="_blank">📅 15:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463876">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3f2453fbb.mp4?token=oqlmQSrEs2R_emxIQFNDRq3f2Lh710NaKchC-dQvconNkAUwFSmkYF4FXvMJNV1yDirYEJYBb4CQyTweOlxAhExcYsWEgIlBrH9B_p1g5DWWwlGT9NA3YHxwu6s4k5s6TjMaGVgePTem46r9uuxFdL_ZeG8FEfO-Ht0ponLp9-2ZP064MvRc-0FEZpljW2SKlp4PQaDbQeTBDYgeiJxYzYOP2oMstEDKmp2l9H15J3ouZXYoX05XWguVf4yjn9I-nL5RRKdKhtvbIXB29flffHRwZEe8vgyWpaWsj0lA-hKyCdReP4TscD5whKeYZle3cspaAzOA_YyOUvW83kpy6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3f2453fbb.mp4?token=oqlmQSrEs2R_emxIQFNDRq3f2Lh710NaKchC-dQvconNkAUwFSmkYF4FXvMJNV1yDirYEJYBb4CQyTweOlxAhExcYsWEgIlBrH9B_p1g5DWWwlGT9NA3YHxwu6s4k5s6TjMaGVgePTem46r9uuxFdL_ZeG8FEfO-Ht0ponLp9-2ZP064MvRc-0FEZpljW2SKlp4PQaDbQeTBDYgeiJxYzYOP2oMstEDKmp2l9H15J3ouZXYoX05XWguVf4yjn9I-nL5RRKdKhtvbIXB29flffHRwZEe8vgyWpaWsj0lA-hKyCdReP4TscD5whKeYZle3cspaAzOA_YyOUvW83kpy6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس مبارزه با قاچاق کالا و ارز: ۳۲ درصد از ۵۵ هزار پروندهٔ مبارزه با قاچاق مربوط به سوخت است.
@Farsna</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/463876" target="_blank">📅 15:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463875">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
پاکسازی خانۀ تیمی تروریست‌ها در جهادآباد سراوان
🔹
یک منبع آگاه از انجام عملیات ویژه برای پاکسازی خانۀ تیمی در منطقۀ جهادآباد سراوان خبر داد و گفت عملیات علیه تروریست‌ها همچنان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/463875" target="_blank">📅 15:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463874">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMeunXfpKM7ng0m-bnfxcx0HUuE4jYSq7DMTxPfIWTlHN4m2XcSrncTFkSvmiUmxVr6zlfSysFcQjplcV-mLN_vhJLDN1YTF1FZssjUv5RxgTQjuEnFnDI7UqlaaNKSGv2WbMp952ogHsKHHRLM2gfkoNu2sxbMKDSuOUPA_XS-cAvscCywzIiZn8xUsHZDFclFaUsluqhHDCfzEvqBhV3urlDVWTKTiQv9ABJF6BnwrjznQiZxT72jncIysTfOm1Ko05Pm23qTMjmQ5tKxFiFZnkm6DHf6Ph1uN1KVzxQuBIlkuvO8cLxf8kidYrjwaBoHNZSNA27qlgcisAR5Y-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا دیپلمات‌ها در مسیر جبران باخت‌های نظامی دشمن حرکت می‌کنند؟
🔹
چارچوب سفر رئیس‌جمهور و هیئت دیپلماتیک ایرانی به سازمان ملل ابعاد چندوجهی و متعددی دارد اما فهم مسیر درست از مسیر غلط را می‌تواند در چند محور تحلیل کرد.
🔸
۱. سؤال اصلی در سفر آقایان پزشکیان و عراقچی به سازمان ملل این نیست که آیا ما با آمریکا مذاکره می‌کنیم یا خیر، بلکه سؤال اصلی این است که رویکرد ما در مواجهه با آمریکا تحت هر چارچوبی چیست؟
🔸
چه مذاکره بشود و چه مذاکره نشود مسئله مهم موضع و پیامی است که بنا داریم به‌صورت مستقیم یا غیرمستقیم به آمریکا منتقل کنیم. اگر موضع ایران «اقتدار» و «مطالبه‌گری» در خصوص حقوق مشروع و جبران خسارات باشد از مذاکره و انتقال پیام هم باکی نیست. اگر هم موضع دیپلمات‌های ایرانی موضع ضعف باشد چه مذاکره بکنیم و چه مذاکره نکنیم طرف مقابل پیام ضعف را دریافت می‌کند و کشور از تبعات آن ضرر خواهد کرد.
🔹
۲. توهم حل مسئله با مذاکره را هم باید فراموش کنیم. امر سیاسی نهایتاً باید به‌عنوان ابزاری در اختیار حکمران باشد که بتواند تنش را کاهش دهد و این امر قطعاً جایگزینی برای قدرت داخلی نخواهد بود. به‌خصوص تجربه دوره‌های پیشین نشان داده که این ابزار کارکرد کاهش تنش را نیز ازدست‌داده است و در دو جنگ پیشین هم‌زمان با مذاکره، ایران عزیز ما مورد هجوم دشمن قرار گرفت.
🔸
۳. اختیارات تیم ایرانی در حل‌وفصل مسائل سیاسی قابل‌توجه است. ساختار سیاسی ایران منسجم است و هم‌زمان این میزان از اعتماد به دیپلمات‌های ایرانی در درون حاکمیت نشان‌دهنده اوج قدرت درون‌زای کشور است. نگرانی از اختیارات گسترده تیم ایرانی هم چندان معتبر نیست به‌خصوص که هر تصمیمی در نهایت باید در درون نظام اسلامی به بحث گذاشته شده و مجوزهای لازم را بگیرد و سپس به اجرا درآید.
🔹
۴. تله‌های دیپلماتیک را باید جدی بگیریم. طرف آمریکایی هیچ اعتنایی به پیمان‌های سیاسی و دیپلماتیک ندارد و از نگاه یک سیاستمدار آمریکایی مذاکره «ابزار کاهش تنش» نیست؛ بلکه مذاکره «ابزار فریب» است. در واقع باید به‌طور شفاف این مسئله فهم شود که قدرت مذاکره‌کننده پشت میز مذاکره به‌طور مستقیم از قدرت نیروهای مسلح و انسجام درونی جامعه تعیین می‌شود و آنها باوجودآنکه در میدان شکست‌خورده‌اند تنها راه خود را در جابه‌جایی این متغیر جست‌وجو می‌کنند.
🔸
۵. پذیرش ریسک‌های بالا برای یک امر سیاسی در سطح بین‌الملل یک اقدام عاقلانه نیست. ریسک در هر امری یک رنج منطقی دارد و اگر از حد نرمال خود خارج شود آن اقدام توجیه منطقی نخواهد داشت. در شرایط فعلی یک سؤال مهم این است که آیا این اقدام سیاسی ریسک منطقی دارد؟ تهدیدات متناوب ترامپ هم‌زمان با کاهش نسبی قیمت نفت می‌تواند مسئله مذاکره را توجیه کند؟
🔹
۶. هدف اصلی باید هوشمندانه تعیین شود. نیت دشمن قطعاً «فریب» است و میدان نمایانگر «باخت» نظامی آمریکا است. از سویی دشمن درحال القای این امر است که ایران تحت‌فشار است. هدف منطقی تحقق شروط ۷گانه ما پیش از هر اقدامی از سوی ایران است. شروطی که باید مبتنی بر عنصر «زمان» باشد و بتواند تا مدت‌ها دشمن را از استنکاف تحقق شروط بازدارد و یا احیاناً هزینه کلانی را روی دست دشمن بگذارد.
🔹
در نهایت اینکه موفقیت سفر مقامات ایرانی در سازمان ملل، در میزانِ نزدیکیِ کلمات آن‌ها به زبان دیپلمات‌های غربی نیست، بلکه در میزان حفظ استقلالِ و نشان‌دادن این واقعیت است که ایران، بدونِ امتیاز واهی قدرت‌های بزرگ، مسیر توسعه و پیشرفت خود را طی خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/463874" target="_blank">📅 15:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463873">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20916f1ead.mp4?token=KiiRv9WQTC3_1yw7SkNkTEII98fWqfv-wy44F_JNa0BT4mp8wWm_KyZH7K3UMyV9z-SxVvIOwgvpHrdHdyPpXboRavBlM3KwsuYsqb0L-2XqgFExp_wiSJfsydUAOMq9fGTCqDX27dYkQcQegOyRZKzZ3mT0bfxaTq2rMyJ7nDMCytvyL7wfPk17ONfT2NZz_XHFpaDk3QWNdrNitEDOZOHn4TAhPZoWGpRIlunUS3JBjG7GQ4SMfNK6RD8J4tPUazfrsvLtWE12enyQF4PDM8yTMZq0tKiDL8A7eW5u3FnjZTyGbUfGjw38mq334OoG5O8Nu3mxrYMrvQfVoS9KQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20916f1ead.mp4?token=KiiRv9WQTC3_1yw7SkNkTEII98fWqfv-wy44F_JNa0BT4mp8wWm_KyZH7K3UMyV9z-SxVvIOwgvpHrdHdyPpXboRavBlM3KwsuYsqb0L-2XqgFExp_wiSJfsydUAOMq9fGTCqDX27dYkQcQegOyRZKzZ3mT0bfxaTq2rMyJ7nDMCytvyL7wfPk17ONfT2NZz_XHFpaDk3QWNdrNitEDOZOHn4TAhPZoWGpRIlunUS3JBjG7GQ4SMfNK6RD8J4tPUazfrsvLtWE12enyQF4PDM8yTMZq0tKiDL8A7eW5u3FnjZTyGbUfGjw38mq334OoG5O8Nu3mxrYMrvQfVoS9KQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیم پلی‌استیشن ایران با شکست ژاپن، به فینال آسیا رسید.  @Farsna</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/463873" target="_blank">📅 15:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463872">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7c55fce58.mp4?token=dl-Ys0c70t1Kowzp0aJNsPWZNGwx0gipmDDN1IpVG2xXuxjfXAcF2Ka-KIW-rjXHrJEugsYfu52tXhNxKXraOD1BlgNgKdB0DT0RT2nEsh_-ba0ZryY80AosRzumSenn91371BluG-FXjiH_w7_H0jKBBRUGC-zSFDjMQ3fgJX5woqwhFPUluV49uCqbSn3wVK-IIB1PI4wZWa9ZpbqOWOm4hu78XWyxvywuqjisI_UciSoXtd0Ge1n1yjj8UYAdqd9-jJ3uRZIxOWq54wUurQXE7w4HNtN1fGmfIaGV2v5fPeEily__9OJnfGjulD5nS7uY1UnOMWwTMXYcPnb46g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7c55fce58.mp4?token=dl-Ys0c70t1Kowzp0aJNsPWZNGwx0gipmDDN1IpVG2xXuxjfXAcF2Ka-KIW-rjXHrJEugsYfu52tXhNxKXraOD1BlgNgKdB0DT0RT2nEsh_-ba0ZryY80AosRzumSenn91371BluG-FXjiH_w7_H0jKBBRUGC-zSFDjMQ3fgJX5woqwhFPUluV49uCqbSn3wVK-IIB1PI4wZWa9ZpbqOWOm4hu78XWyxvywuqjisI_UciSoXtd0Ge1n1yjj8UYAdqd9-jJ3uRZIxOWq54wUurQXE7w4HNtN1fGmfIaGV2v5fPeEily__9OJnfGjulD5nS7uY1UnOMWwTMXYcPnb46g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: دیگر هرگز به هیچ‌یک از دشمنان آمریکا اجازه داده نخواهد شد بدون موافقت کتبی و صریح ما، در گرینلند حضور نظامی داشته باشند.
🔹
۲ پایگاه نظامی بسیار بزرگ در گریلند احداث خواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/463872" target="_blank">📅 15:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463871">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21815cba9d.mp4?token=hAWDONyuNdWiUgpGBJZx5KbtaXcpHKsJZPGCBCVWCreTHa2td1zfP3qvV3RkAengnNyqCeWVZSlBHyZ0kD5TMgaXANkqfAaAWOirHdQDtrhfEfMsaWqDCnZhMltZga4AqbpY2tMPCjMymrNh2Yzh8bvTT3aUUmyBoNaEOlvtb1ubfJtmH3HNaqNb5Nd8I9PwVVX6CucjnsOOuicmGf0w72sg3ms4g6DxvhrfIpYbYdQWY-XJmbWtlMwv6SI35ALR1RWlHO0n0osLTZiQjbRLVfYkXacBtL-CeR18OW85KVeM5trrZGyvWK3axS-qHCbVarLecYaqh2di2sextdYRNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21815cba9d.mp4?token=hAWDONyuNdWiUgpGBJZx5KbtaXcpHKsJZPGCBCVWCreTHa2td1zfP3qvV3RkAengnNyqCeWVZSlBHyZ0kD5TMgaXANkqfAaAWOirHdQDtrhfEfMsaWqDCnZhMltZga4AqbpY2tMPCjMymrNh2Yzh8bvTT3aUUmyBoNaEOlvtb1ubfJtmH3HNaqNb5Nd8I9PwVVX6CucjnsOOuicmGf0w72sg3ms4g6DxvhrfIpYbYdQWY-XJmbWtlMwv6SI35ALR1RWlHO0n0osLTZiQjbRLVfYkXacBtL-CeR18OW85KVeM5trrZGyvWK3axS-qHCbVarLecYaqh2di2sextdYRNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی: نشستن نمایندۀ ایران پای سخنرانی ترامپ مایۀ ننگ است
🔹
نایب‌رئیس کمیسیون اصل ۹۰ مجلس: درحالی‌که عامل و دستوردهنده به شهادت امام شهید ما، کودکان میناب، کودکان لامرد و دیگر ایرانیان در آنجا سخنرانی می‌کند، واقعاً جای تأسف و ننگ است که افراد ایرانی در سالن بنشینند و هیچ عکس‌العملی از خود نشان ندهند و حتی سالن را ترک نکنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/463871" target="_blank">📅 14:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463870">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815826f49b.mp4?token=tjcYyFoMnz4GjLavKarOV6jKH-8ZpLxTs4k5dF9WU7qsNKW4oyq6qxsh6efTFQvpMbJ1Esnd9RJEOAdnmsmGR6eMX-MUt7yfVbHwc3rV3Xbxa6HMTJTpTVD9UX0-wACEkrotsLbXq6wlGVXMA1UQuB9_k3oRIkMsOe3ggFy0dqw5XJyKrX6dS37O7NEF-1r5pJMQEyJityeZoompy8hP8dFd44CVZs4X7ZD6JNMYt046SZH32dqobMUxOKK-9BrFVA3_WiL4kNPqJ5W8bGpLxekSMGEkpr72QPiZVIKRqNAyJiYrFQ138QycR22EbR7bnIlOT8X5JQ1KTuiprjElAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815826f49b.mp4?token=tjcYyFoMnz4GjLavKarOV6jKH-8ZpLxTs4k5dF9WU7qsNKW4oyq6qxsh6efTFQvpMbJ1Esnd9RJEOAdnmsmGR6eMX-MUt7yfVbHwc3rV3Xbxa6HMTJTpTVD9UX0-wACEkrotsLbXq6wlGVXMA1UQuB9_k3oRIkMsOe3ggFy0dqw5XJyKrX6dS37O7NEF-1r5pJMQEyJityeZoompy8hP8dFd44CVZs4X7ZD6JNMYt046SZH32dqobMUxOKK-9BrFVA3_WiL4kNPqJ5W8bGpLxekSMGEkpr72QPiZVIKRqNAyJiYrFQ138QycR22EbR7bnIlOT8X5JQ1KTuiprjElAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس گمرک: زمان ترخیص کالاها به ۳ روز کاهش می‌یابد
@Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/463870" target="_blank">📅 14:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463869">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92a555b959.mp4?token=N3dphobohrtgQi9ErEwpLgO96ZRV2r1208iYC1AO8YHGBIR0-BRptN58-2Q3A9BuJm9JdO_afUg9vuZwGx42wy1Lf9-pTwYfH_Yj3fWi7VndU1hxyRsaJt944OJnIl4XTgg_Ho23ZOx_63ViIJVAQHeDmQ5aera87rdNmUhu8Ix3TdeQgVAI0_SLV_ngDeL-BvfwLaXLyyrpNpQ3Zjs1U8i4cgoyhBdpJGFMaAO7DlZEWXDjvSydA1Oej2kbCH-1-zHE2_MOOZ8s9kN-10JBFQhIOUAGn68_bS53eaj7aL_43g98FGoXa58N-OZWrLkdruP9As3_OfTyUTusBE2pdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92a555b959.mp4?token=N3dphobohrtgQi9ErEwpLgO96ZRV2r1208iYC1AO8YHGBIR0-BRptN58-2Q3A9BuJm9JdO_afUg9vuZwGx42wy1Lf9-pTwYfH_Yj3fWi7VndU1hxyRsaJt944OJnIl4XTgg_Ho23ZOx_63ViIJVAQHeDmQ5aera87rdNmUhu8Ix3TdeQgVAI0_SLV_ngDeL-BvfwLaXLyyrpNpQ3Zjs1U8i4cgoyhBdpJGFMaAO7DlZEWXDjvSydA1Oej2kbCH-1-zHE2_MOOZ8s9kN-10JBFQhIOUAGn68_bS53eaj7aL_43g98FGoXa58N-OZWrLkdruP9As3_OfTyUTusBE2pdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دانش‌آموزان میناب به‌یاد همکلاسی‌های شهیدشان سال تحصیلی را آغاز کردند
@Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/463869" target="_blank">📅 14:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463868">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b42e397354.mp4?token=DSvFJbIZ0dDuP9lZHK3bHVaXazWKhEwllvq54mu76Zto637nAuPCDFSpaHn1pOp5eEVOmJpWOAg4iIWaGhTsaeFShDmFjkJPuSw8vcmHehPDvPsa9_SaOmhjU0nTP_0OoVBIBjGhlJ078L9hoRN3YzM47yburrJSQJ_6LghL_TMEDEj0CThtvbxKuN1os_ZitFdN__7rBnMBxjkaRrzUwSacrQRAxvCXsNlHCtLapI181aW3BBe3TXaCtGdFfDPFwER2R0MD81OS1_jw-VExAN0L17ChgwVf2R-mWja4GNhtpPJuWte_n2WgHmGcyFlegYwSxRDkcSbShQRI9ZPLLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b42e397354.mp4?token=DSvFJbIZ0dDuP9lZHK3bHVaXazWKhEwllvq54mu76Zto637nAuPCDFSpaHn1pOp5eEVOmJpWOAg4iIWaGhTsaeFShDmFjkJPuSw8vcmHehPDvPsa9_SaOmhjU0nTP_0OoVBIBjGhlJ078L9hoRN3YzM47yburrJSQJ_6LghL_TMEDEj0CThtvbxKuN1os_ZitFdN__7rBnMBxjkaRrzUwSacrQRAxvCXsNlHCtLapI181aW3BBe3TXaCtGdFfDPFwER2R0MD81OS1_jw-VExAN0L17ChgwVf2R-mWja4GNhtpPJuWte_n2WgHmGcyFlegYwSxRDkcSbShQRI9ZPLLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر جدید دوربین مداربستۀ بیمارستان لامِرد در ساعت حمله به این شهر  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/463868" target="_blank">📅 14:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463867">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7951a11eab.mp4?token=VD3lhdb5AKS4nJUz0j_mGmn4SNtJIv10024ASGwG_JKXjti9dh2QzV00yuGBaQK9rVAtebR3c5SwSo3TOtyaGpgao6JhPJrsuT6JIr9KBAuZNVx4gWM_YTW1_TNan0kdB_9WMJUoCJVZWAgOF6xo9olrvNrwnobRL_l1sdrOudvpSatDVIMLIf5_nKBDrZNM9882ID0RxN7Jh0LaVUywOmKy54b_rjcd4YHQe43ezeK2f4_ckgWuJpO6lARpJEaW-xZu5Rxe1jGnb2qcuYBnca6B4Qt2K23ZG7IG7daBfryP7yVZqMtcmtEr-0_h30ElM_53nubiAZ_9RT978lzS2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7951a11eab.mp4?token=VD3lhdb5AKS4nJUz0j_mGmn4SNtJIv10024ASGwG_JKXjti9dh2QzV00yuGBaQK9rVAtebR3c5SwSo3TOtyaGpgao6JhPJrsuT6JIr9KBAuZNVx4gWM_YTW1_TNan0kdB_9WMJUoCJVZWAgOF6xo9olrvNrwnobRL_l1sdrOudvpSatDVIMLIf5_nKBDrZNM9882ID0RxN7Jh0LaVUywOmKy54b_rjcd4YHQe43ezeK2f4_ckgWuJpO6lARpJEaW-xZu5Rxe1jGnb2qcuYBnca6B4Qt2K23ZG7IG7daBfryP7yVZqMtcmtEr-0_h30ElM_53nubiAZ_9RT978lzS2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رهبر انقلاب خطاب به دانش‌آموزان و دانشجویان: پاسدار هویّت ملّی، عزّت و استقلال فرهنگی خود باشید
🔹
[دانش‌آموزان و دانشجویان] در این مدّت [تحصیل]، درست فکر کردن و ابتکار ورزیدن را تمرین کنید و همواره پاسدار ریشه‌های هویّت ملّی و عزّت و استقلال فرهنگی خود و زبان…</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/463867" target="_blank">📅 14:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463866">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKEq-e88hpEmHi3eCShUFC2o13EztHfdegIqoMGi3jK5Gg4mPrEYGqb3hAX6pyS6aDIJr6r0afibMePqgAl5d1LvH-paglBqPm8Wdc2otKbNpajTx-Njd5dnR582uUPvDa2COXWAfXgWQqtBYnH5vL50ZvUX0_4H8IgvjNxURnK46VqeD9aEfuJQulOOeWC5VLzxywHYuFRTzSP89jLm_FgcpCacR68egGF_b9m0j_3F5I3SVSeXwqX2EbpJ2aFU9WCufvhDPeM0KEuYLP0aJ6uTx-NU_0BwzoRiFSHTDpsMcQCklHGd0vqoNcXWFAKUjJzv7mTNixiqrfzBhycL-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنگ آغاز سال تحصیلی در مدرسه شهدای میناب نواخته شد
زنگ آغاز سال تحصیلی جدید با حضور معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور و جمعی از مدیران و مسئولان استان هرمزگان، در محل مدرسه شهدای میناب نواخته شد.
این آیین با گرامیداشت یاد و خاطره شهدای دانش‌آموز و با حضور جمعی از دانش‌آموزان، فرهنگیان و مسئولان استان برگزار شد.</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/463866" target="_blank">📅 14:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463865">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4M6zWCWC9hYZLT8t-fwRIk3Uk3lz3FpAw7OjCo69WVMbvm4vLuma7OF5eXSF-Vnkb11ppIDZBgdM5eZyH2-H_Bna79bgeD8L0KGYGf7AWYMReLneR7agDwEBy17XD2XGn9q5NzODLF0-Skxxl0If9Fu1DQYQcNZeEicpwIMjxEqkQF05NbWrlxn8WUsQua7sls8pubb48xelaDY6cXlqpGxSpp7ZOz_8XnFYMnCeFlB_Mp9Gs37UDDOZqDzsIfsbu2_SLgz8fBeryyovgpwfhTzwkmjjJWVMI6tiGPwURh4CJVE7j6TJwnVR5afmuAgea1VxpHjsJDt5ccul06C9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار دبستانی اُپارک شروع شد!
🎒
💦
شروع مدرسه رو با یه خاطره هیجان‌انگیز برای کوچولوها همراه کنید!
🥳
اُپارک به نوآموزان متولد سال‌های ۱۳۹۸، ۱۳۹۹ و ۱۴۰۰ یک بلیت هدیه می‌ده.
🎁
📅
۴ تا ۳۰ مهر
🎟️
کافیه هنگام مراجعه، کارت شناسایی معتبر کودک رو همراه داشته باشید تا بلیت هدیه‌تون رو دریافت کنید.
👇
برای مشاهده شرایط کامل و اطلاعات بیشتر، همین حالا وارد لینک زیر شوید:
🔗
لینک</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/463865" target="_blank">📅 14:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463864">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/463864" target="_blank">📅 14:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463863">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b234eb1a89.mp4?token=u9Si8t5QDtVmx1FFuYFtpEqnefEfQHgwYoxbxMkUivm4oMcu1_Z57TJxI-zVuaY5C4WP-tNzMSWOfWhcQtvQr1feOhvMtgnAnDkN0L62ZbWWjNOwG3HjDCrw35gxEDaZUcqb_jKy2GPEY_1u0PTffn5N7KzWLsxXSnzTxNRbwKzZmcRTGWtoo-ThyWm7zN_KMTHwnV0fwzezhKky16ubQAfQjGn0YAuMgMcrojr6f--MSVKamBnzYvpmT1nVZje9SJfUNiDsFey2Jz3Ci9O9CFkPc_4AXPucb--FNUCbEY-0r_g2PIg6stoclDkMN7pw0X5rkd4h_5GHA1_e0H_gGZyB-2Ab4a2QIyiX-tiucK6Mx_rYM1-J-Y0EpwxD6ll9-qhe6yquNjrGmNkqXIFQMtvt2S3DceSyVhXmVujFdTbtG3u_k6kJvHNCzbh7cdkLR_rKpD7jCEfyLhJXiqFZePOdX3MKrhiAKXQNA7FWvgFWChORzVqIipceYUqdynSoBqqOCXhZ4x0F-39xLZvoYi0uvRGfYfxSyaXMIcEw3W7wTY1J53NIH8OjO7QkkTXqVRmY0W3Q1YUOkFMEoha6SCocY-2pcZKVmyY-TOkmltrf2zK7O0l1A3-omx8FogEcBAexyS60l1egL-KqHFXqhZKWvePd4UIRiz5B2ovqA0I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b234eb1a89.mp4?token=u9Si8t5QDtVmx1FFuYFtpEqnefEfQHgwYoxbxMkUivm4oMcu1_Z57TJxI-zVuaY5C4WP-tNzMSWOfWhcQtvQr1feOhvMtgnAnDkN0L62ZbWWjNOwG3HjDCrw35gxEDaZUcqb_jKy2GPEY_1u0PTffn5N7KzWLsxXSnzTxNRbwKzZmcRTGWtoo-ThyWm7zN_KMTHwnV0fwzezhKky16ubQAfQjGn0YAuMgMcrojr6f--MSVKamBnzYvpmT1nVZje9SJfUNiDsFey2Jz3Ci9O9CFkPc_4AXPucb--FNUCbEY-0r_g2PIg6stoclDkMN7pw0X5rkd4h_5GHA1_e0H_gGZyB-2Ab4a2QIyiX-tiucK6Mx_rYM1-J-Y0EpwxD6ll9-qhe6yquNjrGmNkqXIFQMtvt2S3DceSyVhXmVujFdTbtG3u_k6kJvHNCzbh7cdkLR_rKpD7jCEfyLhJXiqFZePOdX3MKrhiAKXQNA7FWvgFWChORzVqIipceYUqdynSoBqqOCXhZ4x0F-39xLZvoYi0uvRGfYfxSyaXMIcEw3W7wTY1J53NIH8OjO7QkkTXqVRmY0W3Q1YUOkFMEoha6SCocY-2pcZKVmyY-TOkmltrf2zK7O0l1A3-omx8FogEcBAexyS60l1egL-KqHFXqhZKWvePd4UIRiz5B2ovqA0I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زنگ مهر در سراسر کشور به‌یاد دانش‌آموزان میناب به‌صدا درآمد
@Farsna</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/463863" target="_blank">📅 14:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463862">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc6894b3d.mp4?token=MJypRqZ-3AhxZlSi-vlB4It87rQ9MxboODw04vEmEg8YFT14fbyolBgfLSXMrrgxB37M1LIYBEn5ErbLtroS4odkKGzWn5Dnucf4NW7Yd-oWjdmgDljMe5EzEU4bi36uB_F1AywwPSk1a6vBCyQ5-whMLBD3YfTJg8_09kRVIkAgVgCr6VuOR0bNCtc5inls_cduXAlHBUcoL06hpmPtSZKV-IqKq8PAUc1wm2Zfn1DkD2i703rpxWWTzoBOw-NrtzeSozUhYgr2Pwfeol7e0f7DGjQB0sEjRdO8nGw7CYjOPBAP1_0YoSEwI-gO8uS-SuBDaF_Yn7GUKBIq_auKzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc6894b3d.mp4?token=MJypRqZ-3AhxZlSi-vlB4It87rQ9MxboODw04vEmEg8YFT14fbyolBgfLSXMrrgxB37M1LIYBEn5ErbLtroS4odkKGzWn5Dnucf4NW7Yd-oWjdmgDljMe5EzEU4bi36uB_F1AywwPSk1a6vBCyQ5-whMLBD3YfTJg8_09kRVIkAgVgCr6VuOR0bNCtc5inls_cduXAlHBUcoL06hpmPtSZKV-IqKq8PAUc1wm2Zfn1DkD2i703rpxWWTzoBOw-NrtzeSozUhYgr2Pwfeol7e0f7DGjQB0sEjRdO8nGw7CYjOPBAP1_0YoSEwI-gO8uS-SuBDaF_Yn7GUKBIq_auKzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاکستان: ۸ پهپاد طالبان را ساقط کردیم
🔹
درحالی‌که تنش‌های نظامی اسلام‌آباد و کابل فزاینده شده، ارتش پاکستان از مقابله با پهپادهای شلیک‌شده توسط طالبان خبر داد.
🔹
در بیانیهٔ ارتش پاکستان آمده: نیروی هوایی و ارتش پاکستان با موفقیت تلاش برای هدف‌قراردادن اهداف غیرنظامی را خنثی کردند. ۴ پهپاد در ارتفاعات کوهستانی حومه کوهات و ۴ پهپاد دیگر در ارتفاعات تورخم سرنگون شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/463862" target="_blank">📅 14:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463861">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf960b15c3.mp4?token=oXfN9Fp-8nNIcB8RN6AMSLpq9V8vsnaTAbiX8RTGksGGRTbNSAyAgOnNx9DxBPXAWTmet69C2m2Dt_B7wYMHTDjftp97g1rkE5hng_nAp75nz0RvECovbDXnYfemxMX9nCyVSYQVkl5YrGibQyn1zAhZOQnYOx4pQ2ygJ1SrJ6RQnlnTWEQzpxthwI-g8hf7XHaR_y8Ibt6baPl91mz5PVM0X0suQuYzHeSzymL2aYYYzkrTkv2v5mDLRPqvhNUXmxlUo_NSUvtOdCS_xS2lb8m2m-Y6pJlUiYQdcOJHPPrHcokzTzZdQatMOGMPPufyUDQrki3MZTT8N1Zlx3anYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf960b15c3.mp4?token=oXfN9Fp-8nNIcB8RN6AMSLpq9V8vsnaTAbiX8RTGksGGRTbNSAyAgOnNx9DxBPXAWTmet69C2m2Dt_B7wYMHTDjftp97g1rkE5hng_nAp75nz0RvECovbDXnYfemxMX9nCyVSYQVkl5YrGibQyn1zAhZOQnYOx4pQ2ygJ1SrJ6RQnlnTWEQzpxthwI-g8hf7XHaR_y8Ibt6baPl91mz5PVM0X0suQuYzHeSzymL2aYYYzkrTkv2v5mDLRPqvhNUXmxlUo_NSUvtOdCS_xS2lb8m2m-Y6pJlUiYQdcOJHPPrHcokzTzZdQatMOGMPPufyUDQrki3MZTT8N1Zlx3anYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامهٔ نماز بر پیکر آیت‌الله شبیری زنجانی به‌امامت آیت‌الله سبحانی  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/463861" target="_blank">📅 13:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463860">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_5kaMH8us8O4Mi2SaSfhp9vHC65LMhrmPt6dM63_WmBxauIczDWpN3k5yXA8GGn8yKN0Qumw-MqK5HAkqEfR3ZsTpUjsKUK0HZUjjh8Z0jVHSDhJlOgrX1CleJXD5PbrhFdv__Ojx7GeZTNPMis49a9IGFrchSRjlnJxohX4Xf_QqL8-fhpA8l_GLpQ81inHShbYMddxA0POHPEjAjcUjXPZGskEyQhdiq4YJK6cW1c0XmKfjakwwuPRQyhLYYTHyWy7VDGLCkkBMPkqy80C4d00zGScCNiJ-Tii0McBenz4O6BSXZjmE_4GRmEMoI9XQz45KYF4DYiI1Ma4LzSkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: دهه هشتادی‌ها، نودی‌ها و دهۀ آینده ایران را تضمین خواهند کرد
🔹
رئیس‌مجلس در دبستان پسرانۀ شهید آیت: شما دانش‌آموزان وارثان نسلی هستید که بیشترین شهید دانش‌آموز را در دوران دفاع مقدس داده بود.
🔹
امروز در شرایطی فعالیت مدارس آغاز شده که تعداد زیادی…</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/463860" target="_blank">📅 13:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463859">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyLzl-Y6NUFXt8BRYzIUSUEL4qkhZoFb1rs0VIrDpV7Hd43axrR4oM326RNjNGFwp4IM-n-W6Kx3WPWXQhsAuVgfcQIU-Zq415iPdWQolM3Mf6Scc4fS111CozkxKIoSmOU-hJtsnAG3ID4VJgxMxxPqRFKrYd86Bh5GY-haX4rVvr1d6yZ2wUWgY11Acpo3iPYe7mZEhLV37mjNRZOyniXzTRzOglbzSy7_J_v6H_M31UFOd6zTgDjziQvEO7_YwhJTJQyidCbNu0hjqqFscUUKtx9rV8fdSXOvYQy91eOzgYsEZohtyyUmMouGL3BfCEhlUaX0QqdO3qY8vBVfSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
امیدها دوباره همه را ناامید کردند
🔹
تیم ملی امید کشورمان با شکست سنگین مقابل کرۀشمالی و با توجه به نتیجۀ دیگر دیدار این گروه بین تیم‌های امارات و چین در رتبۀ سوم قرار گرفت و از گردونۀ مسابقات کنار رفت.
⚽️
ایران ۱ - ۴ کرۀشمالی @Farsna</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/463859" target="_blank">📅 13:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463858">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlHLQYpMeTfEQFF3iznDmcSfWg10ninF-GWovuCXAv5OktBt6zOjFejz0DG4YKC2zptP_u4B-Y5m4moxVGPU36aLaqS5uK3FvTtIDpWaUjM-qW5jRAbquAJi_Kv3JqP4H6QcXWfdM4UbIOLJhWx5Zct_aY4QO7GYLYkY_7bbMLOR06ke3KjBqNP7RBVw0z54vHNUITej-9N-2QomnjjIjpTX7Patnd36wwS--Kje6JNy92-2XnF0p_OqES81UDqiOz4d2OURwPeviIqvocQaeb9ZpUtc_j_9DgPoG16NFOhwEdsUZwc5DhBQCUvzUgEtcR2sgagLOSafP82NxZ3hWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: دهه هشتادی‌ها، نودی‌ها و دهۀ آینده ایران را تضمین خواهند کرد
🔹
رئیس‌مجلس در دبستان پسرانۀ شهید آیت: شما دانش‌آموزان وارثان نسلی هستید که بیشترین شهید دانش‌آموز را در دوران دفاع مقدس داده بود.
🔹
امروز در شرایطی فعالیت مدارس آغاز شده که تعداد زیادی از هم‌کلاسی ها و هم‌سالان شما در مدرسۀ میناب و چند مدرسۀ دیگر مورد هجمۀ دشمن قرار گرفته و به شهادت رسیدند؛ آنها در حقیقت رفتند تا ایران عزیز ما بماند.
🔹
پرچم زیبایی که به‌دست شماست، نشانه و شناسنامۀ این ملت و نماد عزت و اقتدار آن است که به آسانی به‌دست نیامده و جانفشانی‌ها و تلاش‌ها در این مسیر اتفاق افتاده است.
🔹
بدانید آنها به شهادت رسیدند تا به من و شما بگویند آینده این کشور از آن شماست و ما چشم انتظار این هستیم که دست‌های توانمند شما دهه نودی‌ها و دهه هشتادی‌ها، آیندۀ ایران را تضمین کرده و با دل‌های بزرگ و خالص و خلاقیت خود آن را بسازید.
@Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/463858" target="_blank">📅 13:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463857">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPU0z5PlzlVaWll_zftse0gYOcJ8whbAOFdKHuG00K_XqE9Ire6UD9BCHFkl5-N4MdxEhIrFW-0GylXuz5RmtKOS9jf9sXE06DMeOEkrK4bsRW-sie47jG5v71bDgmmaHYa20g8KFtbWYrSER_OWs6vbKHMkAIHOqpF4i8lxv58eMzHDTDL9RRBoEZyNQFCWD_fx2gZiCLW67z78ez3bbH6kS3sHMuVvdNs3WCATyEd-d8f_H4L7WbwlLkDoLQKp4-DS4hkgyJ_T6Xod5y4cOAKG9ybmc6dpb_oQJBK-1FullMjpyy9TCso42ToFmJHM7FJiSu2eACprqy4W1H95jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش میلیادری قیمت ۴ محصول ایران‌خودرو
🔹
قیمت ۴ محصول ایران‌خودرو امروز حداقل ۷۸۰ میلیون افزایش یافت؛ میزان افزایش قیمت هایما 7X به بیش‌از یک میلیارد و ۲۰۰ میلیون تومان رسیده است.
🔸
این افزایش قیمت خودرو درحالی اعلام شده که پیش‌از این ایران‌خودرو توقف تولید محصولات خانوادهٔ هایما را اعلام کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/463857" target="_blank">📅 13:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463854">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RI7fqral5McC26NCLwM0ZfAZOlhkyi6OGOCIBDzwLKTTPilkH7sH3ZprSDQnmnDm9Eqzw6oTsed_oy3T--PtGX1wALi7itJx9vwuWvYZvb6AZntdHHvHrTWfFEXn8s_fdZtCY28QWJK4g1sYszljBKjrFJ5IGXaOTsYpSqmY-EiCiCYV5Fi4l35YCqQZlemluactyNpeRCBXGCGLb3mjBjkqCGKy1SVHdpmkwb0OIaIGsSTSyviKIRlc4V9sC8SgReH60lULyJF_Z5TuaLa9sc7tC1Sjw0C4he2hNKPO9d-P4qpqvFH8nYBznuGsaNLjuZKM-127iWaa_D8b-_pPSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ پرسش از عراقچی درباره علت دیدار با ویتکاف
🔹
به گفته سخنگوی وزارت خارجه، دیدار تیم ایرانی با ویتکاف در سازمان ملل، با هدف ابلاغ شروط تهران به طرف آمریکایی انجام شد. این درحالی است که طبق تصریح محسن رضایی و بقایی، هفته گذشته شروط ایران از طرق میانجی به آمریکا ابلاغ شده بود. بنابراین، سوال‌هایی در خصوص این دیدار مطرح می‌شود.
🔸
۱. همان‌گونه که دبیر شعام و سخنگوی وزارت خارجه تایید کردند، هفته گذشته شروط ایران به‌طور رسمی به آمریکا ابلاغ شده بود. درنتیجه، واشنگتن از شروط ایران برای هرگونه مذاکره و پایان جنگ، مطلع بود. طبق اظهارات بقایی، دیدار روز گذشته عراقچی و ویتکاف، موضوع جدیدی نبود و در این دیدار، شروط ایران ابلاغ شد. بنابراین، سؤال این است که برگزاری چنین نشستی، چه لزوم یا دستاورد یا ضرورتی برای ایران داشت؟
🔹
۲. بر کسی پوشیده نیست که یکی از اصلی‌ترین فشارهای داخلی و خارجی بر دولت آمریکا، افزایش قیمت نفت است. همچنین پرواضح است که برگزاری ملاقات با طرف آمریکایی آن‌هم در سازمان ملل، بر قیمت نفت موثر بوده و فشار آن را کاهش می‌دهد. اگر آمریکا هنوز پاسخی رسمی از طریق میانجی مبنی بر پذیرش تمام شروط ایران ارسال نکرده، چه لزومی دارد که چنین نشستی برگزار شود و از عوارض جانبی آن، کاهش قیمت نفت و درنتیجه کاهش فشار بر آمریکا باشد؟
🔸
۳. بر اساس بیانیه اخیر قرارگاه خاتم‌الانبیا، آمریکا با هماهنگی متحدین خود، در حال برنامه‌ریزی برای اقدام علیه ایران است. هرگونه اقدام نظامی جدید و سطح بالا، شوک بزرگی به بازار نفت در سطح جهانی وارد خواهد کرد. بنابراین، آمریکا نیاز دارد پیش از اقدام، قیمت نفت را تا حدودی، هر چند کم، کاهش بدهد تا بعد از اقدام، با وجود شوک نفتی، قیمت نهایی آن عددی دور از انتظار نشود. بنابراین، هر اقدامی که منجر به کاهش قیمت نفت در زمان فعلی باشد، ناخواسته نیازهای پیش از حمله آمریکا را تسهیل می‌کند. سوال از وزیر امور خارجه این است که چرا دیدار با ویتکاف، در چنین زمان تعیین کننده‌ای، انجام شد؟
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/463854" target="_blank">📅 13:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463853">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f719d6b1.mp4?token=aNGVQZbzZ-MdmY6aqrSy7z4rGgKk3zJuVYApR1TRxZkLL-bZWBFvwiTQCFSKEYT4locmzOI9Y0em3tFEyVunW967toFouTws7XfseTvT4lRGQqXLHAWfJgJGusqgYbF2lQsb7V6svL4H_BujiENR3iCULI8X3JVWQ3J1YfRLKS5E4FRsD-lC_GXJUodvDgbI1jUxTB1ZZ-WzpYsLTu3ngPv_5BHmAWQjSVodDlbAVnmzDZ7cmXz7MvZtdCFWuiD0gLFvW_UgTB3iMvLusC9hlfHy6s_zZFGVIuSku6cpfIh8qSeytMApbkL6reSeMJ57xf-3UORekk3QThgVUX8jF08QqTTmM-BV8QS07YqFaNBB86CfOUoPbIhzAbGh9XCgQGRNLhuhGdPRupU8WfNRpQp2xjUhEiviFhHobINBct8ITWelCk5QgOYh_ZFo--7nqmFLmiulsMBcZf5E4abqNymiMYILchJtcR4C7--VXd5fOSwt9WAgwhcDr1r4KLxZa3jbIEaYKK5UbNGEmj96o85PhGGQsd3p31EIlUCbZEvATQ6tNHpZ0iz-hPbisZrV2plSr3p0ciww4_uzlCO_UHb43z3T4TXJkVx4HFF_YtiN4OFLEEMQWhjZxaHlIvN3xr0z1foC2ZJGZLmJY8E-vZGhkAY8BkoR155XFW5O1ic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f719d6b1.mp4?token=aNGVQZbzZ-MdmY6aqrSy7z4rGgKk3zJuVYApR1TRxZkLL-bZWBFvwiTQCFSKEYT4locmzOI9Y0em3tFEyVunW967toFouTws7XfseTvT4lRGQqXLHAWfJgJGusqgYbF2lQsb7V6svL4H_BujiENR3iCULI8X3JVWQ3J1YfRLKS5E4FRsD-lC_GXJUodvDgbI1jUxTB1ZZ-WzpYsLTu3ngPv_5BHmAWQjSVodDlbAVnmzDZ7cmXz7MvZtdCFWuiD0gLFvW_UgTB3iMvLusC9hlfHy6s_zZFGVIuSku6cpfIh8qSeytMApbkL6reSeMJ57xf-3UORekk3QThgVUX8jF08QqTTmM-BV8QS07YqFaNBB86CfOUoPbIhzAbGh9XCgQGRNLhuhGdPRupU8WfNRpQp2xjUhEiviFhHobINBct8ITWelCk5QgOYh_ZFo--7nqmFLmiulsMBcZf5E4abqNymiMYILchJtcR4C7--VXd5fOSwt9WAgwhcDr1r4KLxZa3jbIEaYKK5UbNGEmj96o85PhGGQsd3p31EIlUCbZEvATQ6tNHpZ0iz-hPbisZrV2plSr3p0ciww4_uzlCO_UHb43z3T4TXJkVx4HFF_YtiN4OFLEEMQWhjZxaHlIvN3xr0z1foC2ZJGZLmJY8E-vZGhkAY8BkoR155XFW5O1ic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دانش‌آموزان اصفهانی روز اول مدرسه را با یاد شهدا آغاز کردند
@Farsan
-
Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/463853" target="_blank">📅 13:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463852">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بیش از ۲ هزار استاد دانشگاه: راه علاج مشکلات کشور، شکوفاسازی ظرفیت‌های ملی است
🔹
بیانیۀ ۲۲۹۲ استاد برجستۀ دانشگاه‌های کشور به‌مناسبت آغاز سال تحصیلی: آنچه برای دشمن و نظام سلطه جهانی غیرقابل تحمل است، پیشرفت ایران و الهام‌بخشی آن برای کشورهای عقب‌نگهداشته‌شده جهان است.
🔹
آیندۀ ایران با شکوفاسازی ظرفیت‌های وسیع ملی روشن است؛ باید از توان علمی، انسانی و فناورانه کشور برای ساختن ایرانی پیشرفته‌تر بهره گرفت.
🔹
راه علاج مشکلات کشور، شکوفاسازی ظرفیت‌های وسیع ملی، توسعه علم و فناوری و تبدیل توان علمی ایران به قدرت و توانایی در عرصه‌های مختلف است.
🔹
رمز موفقیت ملت ایران در برابر تهدیدها، نقش‌آفرینی به هنگام، وسیع، آگاهانه و منسجم آحاد مردم با گرایش‌های مختلف است.
🔹
حفظ انسجام و وحدت اجتماعی و پرهیز از شکاف‌های اختلاف‌برانگیز، می‌تواند زمینه‌ساز نقش‌آفرینی مؤثرتر مردم در مسیر پیشرفت ایران باشد.
🔗
متن کامل بیانیه و اسامی امضاکنندگان را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/463852" target="_blank">📅 13:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463850">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzfxcXrX6Rh3jExyf1Xnsh-joUn1sd-_MrtoMpTZzj-KT3WtidDLgb4nudDNv5S0k37sxSjHputG07CFsciMc3Hd2qDhZ5fnmO8I16LHIEAxcCh2163Xq8k5S2ie7OlYNiyRFsRo46fc1PontQhEKU2-Wp6BlYjqsps3izZV0CWfN8CNV6YBroEldlHnOm1N2vTWklee4PrLhhneytUn_ovt69AHuyjuT-hz3i2W4A8oliu24t2hUm9P8_J4dJITcO_leeF4dVF-INy8lIL6BacnrI3yHB0dqsefwXcagdlrTKQIf0NP_V7rehMjT7LYtFHjqch2Z5JHml4kUbY_VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس هفته را سبز تمام کرد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۸۹ هزار واحدی به ۷ میلیون و ۲۵۷ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/463850" target="_blank">📅 12:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463848">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQllPuXkXtAIEBAkBdtA4WS9EsShxAB_prNG_vPs5I87TmXh_fc4et_AUUfEp963X6xN-UXGKFGb48EezH0mpfrnHAeYHG7oIeehG-HWmHCXR0wJN8pq3RQ8l_S9VeFF2tIiWRUYRPu_D5JJDlwKbWVaVTHDs1BNCUjJ0IFqovvm4zufcTHsx34Jz9hXroIPs5-YJ1zcAD8ehm7b2gEteCHkQja7HyE4E2uhDWyKSL7AShLB69FPqAXhycIqiNnli0mtjUxEonWgjm1_uF8gavs9qiMviBrIdvrG5WZhmgWuqnwEnC3uEnhMYJR6jtzWe9LGTXnWO5xybTsHz1VSDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تأثیر قطعی پایهٔ یازدهم در کنکور ۱۴۰۶ پابرجاست
🔹
دبیر ستاد علم‌وفناوری شورای‌عالی انقلاب فرهنگی: درحال‌حاضر، تأثیر پایهٔ یازدهم برای کنکور سال ۱۴۰۶ قطعی است و شورا مصمم است مصوبهٔ موجود را تغییر ندهد. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/463848" target="_blank">📅 12:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463847">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97bdd86324.mp4?token=JdufpnIRT7ik5KKqusDQVh2qGeSbDJ3z_tyvo1VCd2Pg8HJ5cgZ9JhsFgO7fIh6-rdYbfzzIp2rpUApBfygJCipiRynm0OfYwaf7KiKEyN5y-ngL8J8k2rMVQkw5CrErG-JiaYdSa6mcf-rcHJTkYCfmTQrxzACRuV8pEkAPUmvKtpXlE4MxacHt3k1W3l-7hpTv4q4_zt6TdnGG_GmL5j2bh47iscJHIq6uO4Sf9jpr08elxmtcOq94bcTbQhwAEjRD8kAXGCh1yRXsyoCh_xrB9c64YJQjRmjQGsRCfo938Eu90aD-9OhVFcaKVwziiPXKRRWc22wAaOAXaosXaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97bdd86324.mp4?token=JdufpnIRT7ik5KKqusDQVh2qGeSbDJ3z_tyvo1VCd2Pg8HJ5cgZ9JhsFgO7fIh6-rdYbfzzIp2rpUApBfygJCipiRynm0OfYwaf7KiKEyN5y-ngL8J8k2rMVQkw5CrErG-JiaYdSa6mcf-rcHJTkYCfmTQrxzACRuV8pEkAPUmvKtpXlE4MxacHt3k1W3l-7hpTv4q4_zt6TdnGG_GmL5j2bh47iscJHIq6uO4Sf9jpr08elxmtcOq94bcTbQhwAEjRD8kAXGCh1yRXsyoCh_xrB9c64YJQjRmjQGsRCfo938Eu90aD-9OhVFcaKVwziiPXKRRWc22wAaOAXaosXaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربستان در پلی‌استیشن هم حریف ایران نشد
🔹
در رقابت‌های بازی‌های آسیایی ورزش‌های الکترونیک، ابوالفضل آقایی‌نسب از ایران در رشتۀ eFootball Mobile امجد عثمان از عربستان سعودی را ۳ بر صفر شکست داد.
🔹
حسن پاجانی هم در رشتۀ eFootball PC عبدالعزیز فلاح از عربستان…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/463847" target="_blank">📅 12:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463846">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9BUUHsNXF0sTIJ3JTuxhGrwhC7K7l0vQAU2rf5KQBRtfoogvQKFZawKlja07TxnNmGBx2KSZZMW1yEjzrfzajdl0o6gMOZSImfB12JMIV5gKhbHkHaYaMeHzJf1jK9CRhbYi6NcdaS-vGejYrR2rn8g2buL8ujUrsVjfOx68SgxeRXW3XEeCVl9SIPJe46FLLw_oDMvV5feYMaEjXbkunKWD40VArLXAAIkpAtIq5GHQYE1GQ9ZkIhBASpv6SvVso2pz6784MQuZb-lQwqFu_PZZgcB8EH6RFF82grBDHVE_DLv5Ck0-S5EdxziIgw-i0XRBa7U9SAwJ0fNcMM-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
‌پزشکیان وارد نیویورک شد
🔹
رئیس‌جمهور دقایقی پیش به‌منظور شرکت در نشست مجمع عمومی سازمان ملل متحد، وارد نیویورک شد.  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/463846" target="_blank">📅 12:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463844">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bb61ac5a3.mp4?token=P0tP7euwursbr6F_1eblAvMcsksLDKSuTJbGB3Ab8yEYryvUB_H7HUmf-O3-lLZ6M0zheaeo8OHQq_2WC8vbdgUM5upRlLBBVZ_NxcCDYcR_bw264zKSobvIfGAWGbDfOfRrI1amslYQVgDq2OSDJVcGUOtW9H6YATvpHhESXxPU8C0cQmRxfI2PHz4MoAN_wL3e5izXkCTT2716VWGZ8kLEinvniwXukliGmAvqmirWEUCDe8-SBTSxFFnNlozBXrpvaDPFirdt-fip_HYWSp4F5cViDyiATihMnjXF_IHhZLvsHKYqarrHUgKq0G7YJPFbJ4-hBdUZSJ8cWWwkJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bb61ac5a3.mp4?token=P0tP7euwursbr6F_1eblAvMcsksLDKSuTJbGB3Ab8yEYryvUB_H7HUmf-O3-lLZ6M0zheaeo8OHQq_2WC8vbdgUM5upRlLBBVZ_NxcCDYcR_bw264zKSobvIfGAWGbDfOfRrI1amslYQVgDq2OSDJVcGUOtW9H6YATvpHhESXxPU8C0cQmRxfI2PHz4MoAN_wL3e5izXkCTT2716VWGZ8kLEinvniwXukliGmAvqmirWEUCDe8-SBTSxFFnNlozBXrpvaDPFirdt-fip_HYWSp4F5cViDyiATihMnjXF_IHhZLvsHKYqarrHUgKq0G7YJPFbJ4-hBdUZSJ8cWWwkJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور مردم قم در مراسم تشییع پیکر آیت‌الله شبیری زنجانی  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/463844" target="_blank">📅 11:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463843">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSiX4_7sHFlxgFvTvXMo5ZUpPzkG6kPtcIXVjPLxuc-CvXYm9zC9p6bNDkbbLcOb2zoV1KUsnj2Bd_49UGfZuHMekhB_VNFoO-LdUFILsLXrhMQLXzvJ775eBdtzsOfbBqVQASxC6wTwJvwE7zYMjyTT5Gz0SQdx2yCib40s7LQpCiUoEKVP8RkMj0SkUANBfY0uhJ2n1Lbp68hpayMwL2Wc47w9yvOQaXeSt-Ui9InnajjB4a3VkjkemD8x4BpYdDyG8v9DAPE1ekYJwi2TmHJcB3wgzoMUHW92EyDd-YlhZgsKFOsdnGo-kMs1OzdBgpO-hmWgSqjdslNT7pQQAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مایه شرمساری و تحقیر ملی»؛ توصیف مقام سابق آمریکا از ترامپ
🔹
«بیل کریستول»، رئیس دفتر معاون رئیس‌جمهور در دولت جورج بوش پدر، در واکنش به سخنرانی دونالد ترامپ در مجمع عمومی سازمان ملل، در شبکه اجتماعی ایکس نوشت: «تماشای سخنرانی امروز ترامپ در سازمان ملل برای من عمیقاً افسرده‌کننده بود. اینکه او رئیس‌جمهور ماست، مایه شرمساری و تحقیر ملی است.»
🔹
کریستول در ادامه گفت: «هر کشوری در جهان، چه دوست و چه دشمن، می‌بیند که ما زیر سلطهٔ یک خودشیفتهٔ ابله هستیم.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/463843" target="_blank">📅 11:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463841">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69749884d3.mp4?token=fzGHLSpbXXn2WuB8bYlzL_-uWRog8wDMlaUGZpedCpFZTAdp4FaXQh_mK0f0Y7rG5pCoZvnO0xce7hHf5ithIOnF1Hl35IhP1OWZNJn-SUIeSysLqSeYIytt1HmBSMX7oWout58Abfgk8zEXO2AL3-RLcd5ay_RfyduUFpXYr5DF-_WomjbXI-ptGi-eaRX5Hyq1UmpgF3LrGaUZMVzl1m7PcRJv9fu6GeCLyuqogKoZ1cnSSVM_D58D_1oNqXElcUEAjdTAaV-olmufqsVlcy_Mv8JIBBqxz6ETeCj86OfMol6Rb9UCZh-YeV3rMh1nujCQxxL7mnV306Lw_ynZqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69749884d3.mp4?token=fzGHLSpbXXn2WuB8bYlzL_-uWRog8wDMlaUGZpedCpFZTAdp4FaXQh_mK0f0Y7rG5pCoZvnO0xce7hHf5ithIOnF1Hl35IhP1OWZNJn-SUIeSysLqSeYIytt1HmBSMX7oWout58Abfgk8zEXO2AL3-RLcd5ay_RfyduUFpXYr5DF-_WomjbXI-ptGi-eaRX5Hyq1UmpgF3LrGaUZMVzl1m7PcRJv9fu6GeCLyuqogKoZ1cnSSVM_D58D_1oNqXElcUEAjdTAaV-olmufqsVlcy_Mv8JIBBqxz6ETeCj86OfMol6Rb9UCZh-YeV3rMh1nujCQxxL7mnV306Lw_ynZqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس فدراسیون کاراته: به مردم بدهکار بودیم
🔹
رهنما: ما می‌توانستیم مدال‌های بیشتری کسب کنیم. به بچه‌ها گفتم که به مردم بدهکار هستیم و باید در این شرایط دل مردم را شاد کنیم.
🔹
مدال کاتای تیمی خیلی خوب بود و مشخص کرد که ما در کار تیمی نیز موفق هستیم. فکر می‌کنم…</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/463841" target="_blank">📅 11:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463834">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D3QCojSHuEGq2qWvoCZYuqvSra5Wy1a_qeYKifdrxFs33oK8227u6topUyFr3PunLoKKWGl0ohiM176IJ_ZEamDCOxbuBGW-xvLsWQXLMvBYFQU1Ort6cDBk1NauGRU4o9aYfUu9alUoNy8julmDc7zBM0dkWc0IGvMX4gIiMB9Vd7Fnjpvi-O1dsR5vdWY86f05OqIHTwIN-Lbof6f3e_dO7qYjUZ4pdmmC9hUpa4-ch4b77x-QDIZ7302COTBFIMcLlWLhL1y1DZya31q4Lxo_nAVLWX3PpYilyooiKV8zS3Vs6OLVZ_qQndByBY6QQ0U3KwT1oiSIYfPt_oh_dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g-rdPW4ccLoJ2s1n-oml01ka_j6QOO15hF2HQdja_j01O-zZkBkl39O6oFj8z8xzoxmx0RfpAdcVYktMeE_YYktOXLuHhtYZjRtkqHJSWaG3HqySwzR-OUyy01Lx-wzGDQuUNBUbnmGhB3x5T6tktZpmnxPK4XoJw2_14Fze2iIKt71GYlHjsN5vTy9F5yCdbuL5A6kANt27GQs6BUAlBreih5_2NkPM6fl5EiX_8f1KiXovGdvTPOKSUvqQzejVeSxukchqB72RZNYPU7nO1Fup3dFBOVQCFIfy4WSzQUwdWANC6AKmsQSG9B74Lwmkgj7IpfD1rL4tAuOOq5qQ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lVC2TsCD1k1oQu2iVa_2AcX209jSAAoMul1xK8r16yqoBbtvjxTxGTGjKU1Pn3Tw8HFfqWP7MDnY2-B9UtgsB9zhO15ASASwNplcURz5XusCahwIpe0ebnciqiYOzMYjUI-HXrm_eBXAdcQpcaQOmptCXQBvI-O4aoG8wLsi7lcOTvHSFNPyjS2ZUAOZpFu2Ahgrku-SLOT1eFqNqIxoU-7-ts47xd5LGc_egqeLRdEEfl6GKxio-_MmclhLN9q9944dWi0TSbWhhOfechBQIuxbGnRSz_0YlTPmpOA3spfh1phv-9wesWleXsWvMvm0BXyzRzngAPfYvY83zKJLIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kc5jKZRZ32E7QcZO7AURPR2HFBo2V6K1ijNhZIBUEKBEejdWd6sGtE5qQshG8gBy5uNSJYKvSZh6-u8mIpBq3rl0c7NhhW8u9dpIJWIZxvaaqdC-xC0xGdWR5daYvGoCBiKgFQu_BeQNMD2GhzuRjebEIWwba85bJpIVD0OG2tl0Shr25LrmUnl4Z3jQTFW7qcMIxo0s6_CGedUsu3JsjyNvvnki5horkXHLOLD3ZbGk4mvPQaea1qmzTnypU2hEsnKfaflaICmcO_ii5K4dGo8hQfGeYvh6V5nPy600XQ4s_NdrY-MLkd5XBn1kHzTAxC8qnnyhJD2i2i8bvGYzpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bSnArEutFdGp8_2jk7mxxEqW-Kry_1DlGHmxPR9xESnQBVnpaCwHEmHjvy8nkrzN43MmXIVJ2wKcO0mqw7p_EvL_jOh_08WjKzlq8noa3Znhne_uWBb3pHadig-919Iax-BuVE_VqNkkDARnMeu6qoV3LcR3iGq03hE3k4hNoYHjGUBI7TRtsnL2UL8EMZ02S_plAK3QaShFfiMthFmrgh8myjVAcmJtIf0eOFTcyW_XjRefFjgxrlZWqPAnb3IyQfW9jyNX1kpANUwa4yEAWAO6S4NKX9AODSXvXSjUx9e_HpZ5wbK04aPxr_TdZMNIIMBrj8ohWeNUXW6PiK9CTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcK_eO2oJl9XRmrz7EIQLVimzzFBaGD5KLBYHe257aW5VK3URZ67uguarn_mYJels20pd4n9M0PEQJ_hZbov9FGpr_cql0fGdTi4tSMO7a_vbjxE6vJogWBn4ao0QFMg8CjzZ-O-j09K9MkUfbNzozb2_3F7XAAey2x9tNP_RHoexiKIaRqT4j2cHozLnZjRFaDmOdjsjQDi06gaEq4zlqb1jn_2CKO9989Fn4N8ikn88lpxNl0XbbQ4vvjfHcL4w5biAVvFWayCIv_0kOx0kUqW7E-OsbMEaAEUG03n42MAKc06z4s_oD582g0F2-iezqEqZFgclSo4r-sC4WsazQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J5iixbpT6cB6IdkiphSUbBBghTHYuNXel-Y4slAiMo37zoYsfiC-05ejhcdLxHBIWowJw7njt1OviIsPVw0mVDye3lvSt1S_agwcF12jQWdreA8_s-e23HieCmV9-cHe7GpU7QaOrLSUueXeEx85XK6ALTKPt2dlgVmdqswE8bCtLMdCmiPn2sSA8SEERiasNhmsVkJ9BjZ4DPLW7_enxZ3SGTLBrqEha-U3nYiuNqtwS95uLwGYMBN_DWpHHKURLa6fS5FYTFglLG7VflmbtCSGdcPZmry2oq2Z-NEBEdbaTJaG5258Etg51EBvT-R5iMS89YQp5F36tt-cAPQKRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
باز آمد بوی ماه مدرسه
🔹
مراسم نواختن زنگ آغاز سال تحصیلی ۱ مهر با حضور معاون اول رئیس‌جمهور در دبستان دخترانه شهید بهزادی برگزار شد.
عکس:‌
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/463834" target="_blank">📅 11:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463833">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa88be9b77.mp4?token=oybHSl3GKFtrBS4OzNOkGLZ_ruNisnezZ1OUbwCkDzRA15kYV2ZZ9edAAGQOVXykDfuaKefcg4nxRvyVCEdGnIusng2lq0vabN6C8uPDLmvSrcCdLo5Pt7FEM-C5LgmNREM0lEsJ5zroD7MspoVYpaYe0_T35A9aNpvuE1B25h8JRxD0KthWohDgCklm6rwKMUKTqQ6wwMZcF3DBQvop8rw1Xw0kv5enHabOyXQmLMVobnQeRmtKkxtDSx2x4xFabyiZ0VzuFUVxFlNRDm_OItk1Xtg5SlxrDknStRp7wIDgeBiTdZNsA8w1XggjfIy9pvDBna6udH3OpNibLxx1mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa88be9b77.mp4?token=oybHSl3GKFtrBS4OzNOkGLZ_ruNisnezZ1OUbwCkDzRA15kYV2ZZ9edAAGQOVXykDfuaKefcg4nxRvyVCEdGnIusng2lq0vabN6C8uPDLmvSrcCdLo5Pt7FEM-C5LgmNREM0lEsJ5zroD7MspoVYpaYe0_T35A9aNpvuE1B25h8JRxD0KthWohDgCklm6rwKMUKTqQ6wwMZcF3DBQvop8rw1Xw0kv5enHabOyXQmLMVobnQeRmtKkxtDSx2x4xFabyiZ0VzuFUVxFlNRDm_OItk1Xtg5SlxrDknStRp7wIDgeBiTdZNsA8w1XggjfIy9pvDBna6udH3OpNibLxx1mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل چهارم کرۀشمالی به ایران
⚽️
ایران ۱ - ۴ کرۀشمالی @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/463833" target="_blank">📅 10:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463832">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7452c31cae.mp4?token=X91NCwhxclIDbnOf3B9aFVlapHWv4te9sQKEgyyxVg_rsSmUd_UqjyfwS0IXZHPNbRRpsg5A_J3yqxxA6QjOBoL0Oml0OylNTa9PY96q7X3c43a0tg4kM8QPFPFIGlorefewjvCeqAqmzRrdBZESH7LZCRwZBrL9Q2jL_4Yc-S5dhKBktb66gCxZAVylM9JZzieoAjrLH85veYgH5QpY81SsZm3KVLCcOHeeYbTvJ4uc5SdgbnWOaIpT08R2jzT-A6_7GzQLSqaiD-mJTznOqvNB6E2JJrkOnwc-z8DyI3NLwDGSJJmwpjw0leH5qq-73L3LR6WakThyBHPxlllXnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7452c31cae.mp4?token=X91NCwhxclIDbnOf3B9aFVlapHWv4te9sQKEgyyxVg_rsSmUd_UqjyfwS0IXZHPNbRRpsg5A_J3yqxxA6QjOBoL0Oml0OylNTa9PY96q7X3c43a0tg4kM8QPFPFIGlorefewjvCeqAqmzRrdBZESH7LZCRwZBrL9Q2jL_4Yc-S5dhKBktb66gCxZAVylM9JZzieoAjrLH85veYgH5QpY81SsZm3KVLCcOHeeYbTvJ4uc5SdgbnWOaIpT08R2jzT-A6_7GzQLSqaiD-mJTznOqvNB6E2JJrkOnwc-z8DyI3NLwDGSJJmwpjw0leH5qq-73L3LR6WakThyBHPxlllXnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور مردم قم در مراسم تشییع پیکر آیت‌الله شبیری زنجانی  @Farsna</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/463832" target="_blank">📅 10:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463831">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76403b064e.mp4?token=Tw7d21EEWvw1j5kYOqL9BkfDPkUvcwZ2dho-AVAtYX6f7MXNRQNZetcS1qNRNoRnlHx8Hn7g7TCQdVSVq1lxbPkXbZPf5Pt1o4hf61EEB59NAkay2Xy1tSCUf_1GPhcUlJ4BSLwxdDDIbltUBZ-WXn9o_vnMz0YjO63FI2IF0zGadRDOC_g2ukD1MtcL3XEAjmYU1CGpV5EaFg3vp9elSAUn5aNFcSQb3PYHbAT1ExE99X3kDr6PUL11o9RZ42MnzuDZJZMpZuBEi4EUhZTcWU3uBj0QFrZDyK3axhZS07zr_HD1XiNE922YpEV38epcyG3AJFemrzkWCjnb4jsWGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76403b064e.mp4?token=Tw7d21EEWvw1j5kYOqL9BkfDPkUvcwZ2dho-AVAtYX6f7MXNRQNZetcS1qNRNoRnlHx8Hn7g7TCQdVSVq1lxbPkXbZPf5Pt1o4hf61EEB59NAkay2Xy1tSCUf_1GPhcUlJ4BSLwxdDDIbltUBZ-WXn9o_vnMz0YjO63FI2IF0zGadRDOC_g2ukD1MtcL3XEAjmYU1CGpV5EaFg3vp9elSAUn5aNFcSQb3PYHbAT1ExE99X3kDr6PUL11o9RZ42MnzuDZJZMpZuBEi4EUhZTcWU3uBj0QFrZDyK3axhZS07zr_HD1XiNE922YpEV38epcyG3AJFemrzkWCjnb4jsWGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲ برادر و ۲ طلا برای ایران
🔹
محمود نعمتی در فینال وزن ۸۴+ کیلو کاراته، برابر صوفیانی از عربستان ۶-۳ به برتری رسید و مدال طلا را از آن خود کرد.
🔸
دیروز هم اولین مدال طلای کاروان ایران را مرتضی نعمتی، برادر بزرگ‌تر محمود کسب کرده بود.  @Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/463831" target="_blank">📅 10:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463824">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S5hGeJByN84WcmSWOfc04BkuQ2hEmgHcMLK_yKXUc6dziBuxOWDagG2LtrtMwOoXDHtDd4IerMubVJXr6p8t21jUkkdbGtMqCScKLsmgCR680pXy7vJFQboRDbbLm2ZCSdkKFL6xDv1WZibU3m9MmqYwJ2Hmc6iVinUnElpjOy371BCUKnFZv6WzHUXcTutcPPItRMtosCcmFFTGQYdlqGoxAJksesGKDSgq8E3p8DRXmIgPaJVvjOVGZAS_1FTpYAZZbmmsy8UnybSh5DZ78xRvZypIrMpS5qitsDVbGd99ho4obOuaWnQJoo2i5DjosqqWjGk73E5-yBDo4Ie6iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SMJ5YEUx_h5Y3AGAFTwDhjOqCBXKsIgwLoBBETeQaynMmKRG4rMpIdsDpJ36GB5TTJ7EHuB7rGXwl6HxMgZTBu_Q8gZ7wi5Ggi9dwGu7cxcx1XI1MXuyDcgh4lJYwZQfu32iU1wYvmQU18hdKhbO7H55b-qIzvukqpZSRWswV5vd3zlMw3WPgJ8uBQsFf0q_Ml04gJyqUocF3JHExFm7KTYtjbZUULJvUKTbpRrLRJ0VFezq6oxl17DaW18Hv8nL5IEq4ubafKKeko6mPD6iUXHnBRNR-RXUjbq-tLqRkUr5CTHeanrgthDRIDJeFCTHPVWBIY1NQYYIgx7uYQdNcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hl4lT2dSUJlgIF3FLaihmgGoDHBESu0vmJ9c2thevzJugIh8Uk9W7jK3rctv063Dhf4SOVMCR91EoFOKyNd1FYTJNLvW-LKwlLZ-ZGrLgRCOIx_ylICYumcuIwnzTHKxqrUCIjDrsLYh54iGjrPaB9NwQNhI6h3QQzkpXlCSyZ_gJ0j0iurSg3c5tiGYeEPzAnNKOJxNEZ1Zcz7aHiLebseM_ubkRKZgICwtO8XPvLHUUCeNIBc9I6BbJnw0yF5KqCRf_qsa4atLEtlqPCqDDD_1Y3wa9TEnJ4rwBhMwPrjiDiY1KahbgFbCMubVARvzTB-Adwt4yyp6SFeUJbq5Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ud7_r-0S4SuhR6pNkHAZWsR4dcf6tqB3zNtw79YlXPHXWawfmU13ulflziM5IWg6h_axQ1ncX1e3bF7-704flTygWoBhSMhhjtWAYQ9FLxD3Awx3BdWGI1po-4Ho7c7DY_r4vjMB2Pdcreot34KV5J388fka9cR9-5J_8-8OlCern9AVNjcTEPoz6mBeqsS4cCcp6mgwdcAflkh697FE6PjPRmpHgc6vA7Z76J86Zx1jNbKxU5zbeKe7YQUvSA__-RPc4ruqNKcTM_REb7YqQUABevAAtpc2kh01QBv9bE1ShaAtpS04pTWu7Ihq9RToavAMjBHNZBbBQA_UDD0g2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q606KNr0GEDENM86Pr6n0FfGyYAE8wnE5EXOQF4G9ltb1OGiQke5NrAxHtH-diaWCCksXYGU0Zy65caPQ0xljRifE3w7LrmbXOHT5mxLpZ3V4PaquX1LqBWDXmGnYUd9ncg2xQ4vchUQjezRRkfK-2D_67XCOHCf6jpyzUq1JVDnUtqen283V6BPnvIizkPYYwliyO81kJFJ8WGtaovKbyQq5E7e4Y-1tv0J7g03WEpKRZa1RCwH-0A1FxBWvFzCZTFxdNp-XuUM47sv8CpOcQ47MZgO395nIHyA4KwxIOqqAIV9EuCZ1maR4AtMmxJPwZzNrIolWm2ZNpDbGIAOYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iz79ZWjEq0sGdTKPT1TC4ykyd07swxk2jXtvo3toqSZbhdUSArL31ZfebtnBSX_VJ_pnrFIk8jLQTQ1muNwEY0FPiPEGlYcZ1Qc8qLPHXWkwaRZpHNPN7fxwpwEF8kVV8bgRdweO2iXwVM0xfqa8wVnmPX5EMaQ5k_jXEGByClw0f1rr-McnHnLlplaKp-iLNpGFHBcC8xApo7lcQzVJsLEILTf5MUZtdldRNQYHm4PMXKlNEye52Xh9GzNBGvy_NvbL9utGFk0OgjreRuh_qsgdsY7tUer_WRwws7LpZo85IxH0RnKH5y55kUA2BjXWkzq2gyb9swhidJcvEjBkMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c5FW3_8FJkeNwBKfddUPHqclf0M4W595F4oxSVaLZCbdEUftUORRZICbfxDTaFS6p6g0rAAX7cK2jvr4V1X7_AGUk1FV1-b4SqnHMht0Uc0LoC17R8-rLCvh-YQkh0xDLB2mcfpQwg0t1P2TA5tdVYrbWF8ASt6G3tFGTrLv3pYQz8pUFfZQNWn8qtAaqF3bXvzibVDrDpAHELgP4p_NXkXG-_UEYG3hAKqHuj0R_VXWyE0BrEnF--igduROVNHwJcwvhDmCjH9xpKg-OcSJAZbqhnDgfCRy9IDuB83R6xPU3BpE2on5q8hyoz2eSqWAmyRD_tfbNOhMVlukJzBteg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اول مهر و ۱۶۸ نیمکت خالی
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/463824" target="_blank">📅 10:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463820">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f9E1U23QtODOl6H8k4-7EwgXJ3rC6_UCEYY0cVtQ_2SQ69fbG3oyag21J5CvLtVTm_T61-t2B1_OE8KvOs9-Dm3HqQJaDPF-i2mPwv6TPhWj_j492WjPcORs_XonvmJGXoboLlVwbnkBKXEgJ5AZZQUI4BSlHuMSoi30FwxFYQSH15O1QISF6gw336GbpD_zEhm2KMJHvsouN15P10ZhGZN5q9iqA_O4MFeez5kah_CVu8522HOy8h2mOxp3PjEcbMLC_sNWqws3JE1uVDWpoPlmDcdxYof-BR9QuqCAe93nPP-SS_BvE_Rx6UHbkLkdO7xAYtXbrNJFefW2es9Uqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XuHlCr67oGsgGEZE2pDtkBt_RZDDfoXnJUsxFbiB528iWAN-R0TJ9zovHFiH2niOH0fV7RYUb6ZIiseN2Ljo9glqhhF1vKPDmk7ogaDCcHxJTuhlyQMUEj3EUNYfIA33W55t-U22t3Yq6u3o_T6hFFB6eaB9ctXRK3VJ9nTswLxopzJxkUrBha6mhcIv3_Ce0_b1NFKE8cHkwbuH6H9IwbUYD7Yn5vAUFEsGE-73rZC_A1Jik-UxycKDtypLPuGcY9bR1HFeTpFe7gt1DAlaH1Z3_ZMrQFXZmcvj6Q1U0Ufh1-1H6QIkCVilSjQ80h4X8TjNigQgHYhnO3P2sNryXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s9Udv9C9n2J8TNI6jrUCIWQTxlrskqQLSzj3hUUb_4BLVUWi80ppzR9H9kNNwnMWvyxN98dr2AZTU20WUGsLen6ekFoJsYyYP5IHyuPzgdiSaJlEqJKbOj-K3Hi3y2d9X3JEqfXZsOI_nrN6V38aGoVLFZ7Bko3nIDdmF1qKZtw9SgTdcBVY2DCrMZL3u2Wm6fNHJ88hBVlcjgSSJPf0-8vraz1FR-ihI9ULFAFkbtqeoDzMdDLU1kiJzQx2gf6_sT01Qelo6SFakvCstOiV5oqF_047o64ic7QaqbRw4klbdINmPK-j30ahspt9ZgCO61K_013VhJY5_pfe1MCIgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ShvvfrP8j5g-NT8iMGJpfrVfrsmUTM2AMAkoO0IRhiBrZpseBZAzssz0ivd0o2t24Vp1kF1o3-pE1dXVa1Xt07en4VqGss_BWAPG9TPameM7L6nGtT5HXlJg9sKx1SlXN1jCJwpVOjszjn-bDxKHhRhrFUCxvrxdtYDq5rD47qpbPMBLwLmGGAD5XHBskzwQBE1KfUB6zsCAFbg3HzFmpT8jFQdfr8Uo__LlWv6kqr0_QfYMIppS2MRuGgJN2f-M7lQihCcOlyzzR7dM8BerH1kvwDq7KNTqb-0pCX_clXS52ByRofpvQEtavA7r0uJUrhZIx3bgYtpxdRPdOtcnYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید فرمانده نیروی زمینی سپاه از پایگاه‌های عملیاتی مناطق شمال‌غرب
🔹
سردار کرمی: همچون دوران دفاع مقدس در مقابل دشمن ذره‌ای کوتاه نخواهیم آمد. آینده از آن اسلام عزیز و ملت قهرمان ایران است.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/463820" target="_blank">📅 10:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463819">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31dbac331d.mp4?token=MUuJ4ewqi6-btxsqdluCsV5KSdy0pVXrpAbU6myMCne8JUJW3e-MoSm-Gb_ImQou2CEKBh7m9IDFsIUgE3irPWOYQgmk_xglwkKITqlwHUCoX-6OHiD355LMg4VUKrXIeGjJ6IEyNLOJRjLjWxyVQBuEKGTaP1keylOf35_prkepLOLlfgR8FD59Gpd89Kas_bWlEnPSLoJkRElr8izU4TGu7jdJ2HDXHgBavO7nVu4mqtiqoVRE39dz_TAd1HD0Ii6C4fVK_eZDtXBMvnpUELSPKumIjs8RziQ0wUyf8q6izkiAk6JooXf2M9MuNqdANHaY6ZTVc4pl0soqvufE-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31dbac331d.mp4?token=MUuJ4ewqi6-btxsqdluCsV5KSdy0pVXrpAbU6myMCne8JUJW3e-MoSm-Gb_ImQou2CEKBh7m9IDFsIUgE3irPWOYQgmk_xglwkKITqlwHUCoX-6OHiD355LMg4VUKrXIeGjJ6IEyNLOJRjLjWxyVQBuEKGTaP1keylOf35_prkepLOLlfgR8FD59Gpd89Kas_bWlEnPSLoJkRElr8izU4TGu7jdJ2HDXHgBavO7nVu4mqtiqoVRE39dz_TAd1HD0Ii6C4fVK_eZDtXBMvnpUELSPKumIjs8RziQ0wUyf8q6izkiAk6JooXf2M9MuNqdANHaY6ZTVc4pl0soqvufE-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل سوم کرۀشمالی به ایران
⚽️
ایران ۱ - ۳ کرۀشمالی @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/463819" target="_blank">📅 10:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463817">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d77a05b238.mp4?token=c9xMn42CcO2PF_FTZUCXh3UOwBO29IILEMnmsVExWeGoHZSUqXfzHLp6ssZ-fsufzoG5Lqlzz902n2g7jaO9AIV0qZxg9t-7yYJ4nUPG_sQpB1ilo2SL-f1STOEm2WM2n1vq6BzKB_PoIvFW7J03qD0Y_xsVb0s1wRNa28_65h_XVAosDiQbG_mtRqpMr9N-1fmvKjGiUAYOm5E-QkACJ4z76dN3KNc8Tv15lUaVnfmVFjFIa6LVMM3fi54Z4DBI208YZno6qgBF5zx7UKQJWiPsQFc9jjcOnbgc9lJrRz796qSbyI0OsRf54ik1k6aGJ9A8o9YnhqjMGE84rEaxXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d77a05b238.mp4?token=c9xMn42CcO2PF_FTZUCXh3UOwBO29IILEMnmsVExWeGoHZSUqXfzHLp6ssZ-fsufzoG5Lqlzz902n2g7jaO9AIV0qZxg9t-7yYJ4nUPG_sQpB1ilo2SL-f1STOEm2WM2n1vq6BzKB_PoIvFW7J03qD0Y_xsVb0s1wRNa28_65h_XVAosDiQbG_mtRqpMr9N-1fmvKjGiUAYOm5E-QkACJ4z76dN3KNc8Tv15lUaVnfmVFjFIa6LVMM3fi54Z4DBI208YZno6qgBF5zx7UKQJWiPsQFc9jjcOnbgc9lJrRz796qSbyI0OsRf54ik1k6aGJ9A8o9YnhqjMGE84rEaxXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراسم تشییع پیکر آیت‌الله شبیری‌ زنجانی در قم آغاز شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/463817" target="_blank">📅 10:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463816">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f30ef874f2.mp4?token=tQC033dJljzcnnkfmNMQtCFDXp3ysWRA7iSpKDEgb3VVco15oqLZbixZ6Z7M75YAW3f4U5kPd5BeHqh98EwBgP2eYexu7_jy--4atKgVxoThUgl2mcdSM4xJQnJww5Ufmg_vizfSv0mkKlMf2gI2GYS5gLE3-lF24uhnVOnCd40I83AWk7RaW8t-CISH7lS7phzLyxTkGg4NdTtSHdz4N7dChj9sP5nXt-KmxKsDbQobxlnzRa8vmehFM0xpo_70pV6zAADP2s8VpsaF1HgKt7WtxRlxfW0zPiNC5guDG49qE1RIYAjqRabio3TteGHRaFg5mCdY3tS_CKfN3-fRVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f30ef874f2.mp4?token=tQC033dJljzcnnkfmNMQtCFDXp3ysWRA7iSpKDEgb3VVco15oqLZbixZ6Z7M75YAW3f4U5kPd5BeHqh98EwBgP2eYexu7_jy--4atKgVxoThUgl2mcdSM4xJQnJww5Ufmg_vizfSv0mkKlMf2gI2GYS5gLE3-lF24uhnVOnCd40I83AWk7RaW8t-CISH7lS7phzLyxTkGg4NdTtSHdz4N7dChj9sP5nXt-KmxKsDbQobxlnzRa8vmehFM0xpo_70pV6zAADP2s8VpsaF1HgKt7WtxRlxfW0zPiNC5guDG49qE1RIYAjqRabio3TteGHRaFg5mCdY3tS_CKfN3-fRVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم کرۀشمالی به ایران
⚽️
ایران ۱ - ۲ کرۀشمالی @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/463816" target="_blank">📅 10:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463815">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2079f800d.mp4?token=I1cS8c57e4cXv8OHhWDATjWrxlvgo6jkoekpE3I7fCsuz5KWQlceZft6uVvl9NEglEUZZRspDhD8C1JnDPFl_EVpDnT70pceETE0I2la1hLT99eJ4nMEf_zzSqFvBdJMIv0Mi4wSiR1dk3Th6ouYNuDhnnjRSl1LAVWqN9sf9KErrtSKdTT9QE9BdDS31ErhYofgVtDrAaHBvMDNXelwE4FD1MFXk1VzQQEZ29H1kCTp_ndFGLUCihcHB89SWZ0OXcDx6yb07oOmbVwDZint_6teyYEQ3dB61eDhWlGrpuG68MuPc4ay25z3pJm_8zLY-CglGUfzbOAze1vLzQtHYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2079f800d.mp4?token=I1cS8c57e4cXv8OHhWDATjWrxlvgo6jkoekpE3I7fCsuz5KWQlceZft6uVvl9NEglEUZZRspDhD8C1JnDPFl_EVpDnT70pceETE0I2la1hLT99eJ4nMEf_zzSqFvBdJMIv0Mi4wSiR1dk3Th6ouYNuDhnnjRSl1LAVWqN9sf9KErrtSKdTT9QE9BdDS31ErhYofgVtDrAaHBvMDNXelwE4FD1MFXk1VzQQEZ29H1kCTp_ndFGLUCihcHB89SWZ0OXcDx6yb07oOmbVwDZint_6teyYEQ3dB61eDhWlGrpuG68MuPc4ay25z3pJm_8zLY-CglGUfzbOAze1vLzQtHYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برگزاری مجلس ترحیم آیت‌الله شبیری از سوی رهبر انقلاب در قم
◾️
مراسم ترحیم آیت‌الله شبیری زنجانی از سوی رهبر معظم انقلاب فردا پس از نماز مغرب و عشاء در حرم حضرت فاطمه معصومه(س) برگزار می‌شود.
◾️
پیکر این مرجع تقلید فردا صبح از میدان جهاد قم به سوی حرم حضرت…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/463815" target="_blank">📅 09:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463814">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d13ec09f5.mp4?token=dcykVxxAfNcrMi5k8GgE3jiNwMpzXd7jtWR2ZD3OZrvE8RR7klu0No3ygL39YampT1bhZ-vZ2qik2p4g6faZhIeY9SrgZDlMZxUzw96wchajdj0emyDtnnKUBi8I70llUWxANRiSRiLgA3cQmyswS_p3HDrX12yzuOQILXTrHj4U754YjxDEfZ8QEyWVjq0D6mKT4ijV8ifs3zfDR3AjywwmIMksIYfICA8bT2427agszmr_mNRLa0oVsTFxw3YEyIoegNzy7x87IHB68rm_yDJynk2b5q2_d6uoY2LNft5FJcV3cnGym8oQ-wYWv1ePevzyKnEGCJ_CqUSZxaTpXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d13ec09f5.mp4?token=dcykVxxAfNcrMi5k8GgE3jiNwMpzXd7jtWR2ZD3OZrvE8RR7klu0No3ygL39YampT1bhZ-vZ2qik2p4g6faZhIeY9SrgZDlMZxUzw96wchajdj0emyDtnnKUBi8I70llUWxANRiSRiLgA3cQmyswS_p3HDrX12yzuOQILXTrHj4U754YjxDEfZ8QEyWVjq0D6mKT4ijV8ifs3zfDR3AjywwmIMksIYfICA8bT2427agszmr_mNRLa0oVsTFxw3YEyIoegNzy7x87IHB68rm_yDJynk2b5q2_d6uoY2LNft5FJcV3cnGym8oQ-wYWv1ePevzyKnEGCJ_CqUSZxaTpXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی‌های آسیایی ناگویا | نعمتی اولین طلای ایران را شکار کرد  کاراته‌کای وزن منفی ۷۵ ایران با شکست حریف ترکمنستانی به مدال طلایی آسیا رسید. @Sportfars</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/463814" target="_blank">📅 09:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463813">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/144d3e014f.mp4?token=eCstM7Q4bQO_WucTGGpkNJHymhCOQUGtMY4r5qXO9PXWQVHi-omVAY7lemXXVFnXt9wsKBp451LbxooM0GH_jJVQJF9tNMI3DEj6xbylYjBYgZ_FDVEKFlCwBZpwHTRnlY_Tq4kJpK1bZaKc2XV_Go3LkRBj_BdeyecbPJXq2z2Tf4tEDkA9TJxZ6IW0xMhTGa-v82vftdmD29ZbvIvw90PqW0j83OFli6ntSw-7mEUZbYkyn6-rAhT8Q9EVM_y6yoWEh0A2AgR-Ua0NETiiJUddLg2fWep8DGMcuiW1BwGS_wnrLgu4JAPCyYcHZnbSLGhqTPBMcj5BTy5KP_d_Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/144d3e014f.mp4?token=eCstM7Q4bQO_WucTGGpkNJHymhCOQUGtMY4r5qXO9PXWQVHi-omVAY7lemXXVFnXt9wsKBp451LbxooM0GH_jJVQJF9tNMI3DEj6xbylYjBYgZ_FDVEKFlCwBZpwHTRnlY_Tq4kJpK1bZaKc2XV_Go3LkRBj_BdeyecbPJXq2z2Tf4tEDkA9TJxZ6IW0xMhTGa-v82vftdmD29ZbvIvw90PqW0j83OFli6ntSw-7mEUZbYkyn6-rAhT8Q9EVM_y6yoWEh0A2AgR-Ua0NETiiJUddLg2fWep8DGMcuiW1BwGS_wnrLgu4JAPCyYcHZnbSLGhqTPBMcj5BTy5KP_d_Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول کرۀشمالی به ایران
⚽️
ایران ۱ - ۱ کرۀشمالی @Farsna</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/463813" target="_blank">📅 09:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463812">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMgo3fpdtBjQSkl2J4zwTBmZQc9NS7tOAqygsFPRUzY2FpAVIow0xUYPIESYJaaKHUaJTrAJDEaXWAYaO99zeLuMdGQVUd6iEUeGzuPWPMOaoqJ02y5rXDXHRWT--HKN-BLnmMJkoIlVLOFP-QCX4BxAbvPv1HPypsUnyL5qSjqrjVyH0rWgRlSJkx6WZVq5l4oXpGdxpU2URZ3FQuPkq6_uw8XwMFGuPIEgfCJq05CUka7_jtfuHGOdemAzSLg1h_aLbcqtjM6VoLZ2LPdfA7lZMqak4Z5Advs9h6XbdLcwvsk0q5fQN8Cr-I0IbVWj_W2FVlFrFOX2jFgtzkPRVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دانش‌آموزان مشهدی سال تحصیلی را در جوار رهبر شهید آغاز کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/463812" target="_blank">📅 09:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463811">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e623abd6.mp4?token=eUuiItrA8lUY2y18RCcAY2cQOibo2v3lekzLVyDmFmgOBWCUeYlXsjEDVw2SAyg_WdT0Vh1-pdBT0RGfyBON58Fb4wW6J2B-wlskEEBXcQrZ-iQ1sXXb2XeAQ-SCgDKKYcg6RKalk_jjWEs5yNTLukOnHG0V0YwQ_rBuflKDQ-8UtnPFsSIF2vVAIjY1_aAQ-dKbp_Gui_-5HG4LsXH1NvII7O-MuHf2BfbMNH-jzNSz_33WWemL7xdnKOetBawpzcNjDpOvNi2cQGF6ckyOO3WDjYz5ZY8cJtluBG-t1qGDXXlkpoZdZTcT2WhOlbYVrswtpGwnHdoS6H2M5PdBog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e623abd6.mp4?token=eUuiItrA8lUY2y18RCcAY2cQOibo2v3lekzLVyDmFmgOBWCUeYlXsjEDVw2SAyg_WdT0Vh1-pdBT0RGfyBON58Fb4wW6J2B-wlskEEBXcQrZ-iQ1sXXb2XeAQ-SCgDKKYcg6RKalk_jjWEs5yNTLukOnHG0V0YwQ_rBuflKDQ-8UtnPFsSIF2vVAIjY1_aAQ-dKbp_Gui_-5HG4LsXH1NvII7O-MuHf2BfbMNH-jzNSz_33WWemL7xdnKOetBawpzcNjDpOvNi2cQGF6ckyOO3WDjYz5ZY8cJtluBG-t1qGDXXlkpoZdZTcT2WhOlbYVrswtpGwnHdoS6H2M5PdBog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول ایران به کرۀشمالی توسط حسین‌زاده
⚽️
ایران ۱ - ۰ کرۀشمالی @Farsna</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/463811" target="_blank">📅 09:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463810">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-qGnUtGuY3_CNROsqGEEqRJSZ2RrFPqqT7FvtK_muNwrW71rg0sVfLbprN6QuiEnlunsm0eSlKurhvg32mNAP4qAnJp8tOIm0nYHFjaXYzBT6D8JypvOZiY_cU5xBumvUEjhpKn2-AWzqwBM6oOHoFaHVkBFoEvN-Xnme7O6VWhHG91Z4i-AZalwjLgcDWkVjezoS1RiPtVQAwkBGbDLvUgowos09-b8s1GOhLg0hCzA8obByxPSZCBSHmKuWkGVTfp3AkWyY6ZJ9vzU_UzGynUEgwVVgxgRP3V7BCZD18JFeQi-T-WZIUwvam07Z5n9EfZ9c4McmgOtnGP7qn4ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/463810" target="_blank">📅 09:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463808">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjSAqDELf2b6tL-P_t03xP8m-XFZQ_1ABFtOuhgGJrMQXieIHR-3GMXxchzQo8f_DFUwixptd53f_HCpWBmJoxxrjd_C7_s15GN7SwCKOPQbnKTaLDRHpjYFC2WozbelG4Q52AKtGs9Y-ccQTir00jbCA1rFHqhsEC2V6XwsByU77HK3JeFGgtI8_8eBb0z7Ar1wPUJQaI-TiTOat01J7pmNCohQGVW_0LhRuLDpCOVtL0K9rpNnhXSF9yYz2SMZRO6ccnUQ3Jw_6t3MhToUUZBRhRNrL9yPYbPVSMEtBPsfgab0OZgfHCQMoDQTxqPue5zmfSq4A8J3C0yw4x55xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واحد ۱۲۳ مگاواتی آسیب‌دیده از جنگ به مدار بازگشت  مدیرعامل شرکت تعمیرات نیروگاهی ایران: واحد گازی ۱۲۳ مگاواتی G15 نیروگاه مبین انرژی در منطقهٔ پارس جنوبی که در جنگ تحمیلی دوم دچار آسیب‌های شدید شده بود، به‌چرخهٔ تولید بازگشت. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/463808" target="_blank">📅 09:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463807">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a51315c2.mp4?token=icYkzxa195NQ5duuaNy6LTwpJOtTLOqmhzhgDU4TyQSFQmtfolHy-OfDBXI3vHUZWHCiyRlXTUqAUERIoqln0zLPDkksQDNz3XTUeQifKy_iY8Vaq-h3vIpAB6-Mmmof8DZPN1kd6NeqtPxQk1j19s2uNR7d4MEn6drpQQjW6WWJ1XuDPrpQGHiTyuG6ArJGOuDfpYRryRLeJAilKo3XRK4YJNh-ai_Z7NTaEpCJwboKkYzM73Ta0b2Ovy09GU2fRToBfmDhVaCfbl2CCChmV6qwYEK_FMIjW9HjovZHdV1AnXS1fyokbemrTO98vVPBL78YXj8Nye-wrSfYyueVsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a51315c2.mp4?token=icYkzxa195NQ5duuaNy6LTwpJOtTLOqmhzhgDU4TyQSFQmtfolHy-OfDBXI3vHUZWHCiyRlXTUqAUERIoqln0zLPDkksQDNz3XTUeQifKy_iY8Vaq-h3vIpAB6-Mmmof8DZPN1kd6NeqtPxQk1j19s2uNR7d4MEn6drpQQjW6WWJ1XuDPrpQGHiTyuG6ArJGOuDfpYRryRLeJAilKo3XRK4YJNh-ai_Z7NTaEpCJwboKkYzM73Ta0b2Ovy09GU2fRToBfmDhVaCfbl2CCChmV6qwYEK_FMIjW9HjovZHdV1AnXS1fyokbemrTO98vVPBL78YXj8Nye-wrSfYyueVsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود کاروان تیم ملی امید به ورزشگاه محل برگزاری بازی با کرۀشمالی
🔹
تیم ملی امید کشورمان با ترکیب محمد خلیفه، امین حزباوی، دانیال ایری، فرزین معامله‌گری، ابوالفضل کوهی، مبین دهقان، امیرمحمد رزاقی‌نیا، امیرحسین حسین‌زاده، یوسف مزرعه، سعید سحرخیزان و کسری طاهری،…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/463807" target="_blank">📅 09:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463806">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulXvs9PqeRplIkhR2Skl0Kxed7aCEyOD7kTM6KM5a9ad_njLO-dZBrxhBjt7KqVANAK-7zprgk2L9A1TQML2-eQCqvhkrzfvYzyv6ajwhtYx7RCdaB-7tUfrHSVU9vMe-DnzuXfWrtUGr2aZ6gXDEkl7udN9iIGKG5MoYL73cvL57l7adljwvq9glqr3YbXtbVEhJj_UVChyQre-2z9XN6_0-PdhP0hRHZDQ4XDZeBI0KwJx-HcqDgtSzdFXyPCBq8QPBRCi1cf9ca1a8Up5jZx3zDFtKLP0TSgtBSJ3largHlZrlIHgPp3ajwGGasM0AUXBbImBhg4SYQ_PFE3anw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حال‌وهوای مدرسۀ شجریۀ طیبۀ میناب در روز اول مهر
🔹
پس از برگزاری مراسم ملی زنگ بازگشایی مدارس، ۲۴۰ دانش‌آموز دبستان شجریۀ طیبۀ میناب در فضای آموزشی جدید وارد کلاس درس می‌شوند.  @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/463806" target="_blank">📅 08:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463805">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74bda766b5.mp4?token=dWSHtbH6-hVBqJ4J6oeSfdBvUlg1xwNXpqlDCPBCgdWMCD6nab7HTRk-FztmUv6i79r_7yqIQTmNKv3fG4HVCKpp3eUNiZWZnHwoBVt-bBnRHi79VOSSCNgqo2WNoVPH0Srnc3neSilmLnoMvZkUlWFywN1Phfi7oasA5Aca0N-tHyFUKaiGksGE_bZKfYMXM6cjJcWyTYVklffOCbmXaZ7FVRDjHkPoTCr8jBm11hnbJqG_ewoRaMhHjHWv1VMgizkmPoPghD0V8vjix2-iwjDtS6UMC1oBN9DIU122o45WhG5TusNITd8jSZAMcOYT2VevzxlKY2uhbXJE6BVheg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74bda766b5.mp4?token=dWSHtbH6-hVBqJ4J6oeSfdBvUlg1xwNXpqlDCPBCgdWMCD6nab7HTRk-FztmUv6i79r_7yqIQTmNKv3fG4HVCKpp3eUNiZWZnHwoBVt-bBnRHi79VOSSCNgqo2WNoVPH0Srnc3neSilmLnoMvZkUlWFywN1Phfi7oasA5Aca0N-tHyFUKaiGksGE_bZKfYMXM6cjJcWyTYVklffOCbmXaZ7FVRDjHkPoTCr8jBm11hnbJqG_ewoRaMhHjHWv1VMgizkmPoPghD0V8vjix2-iwjDtS6UMC1oBN9DIU122o45WhG5TusNITd8jSZAMcOYT2VevzxlKY2uhbXJE6BVheg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: تا روز جمعه روند افزایش دما در بیشتر مناطق کشور داریم
🔹
از روز جمعه کاهش نسبی دما اتفاق می‌افتد.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/463805" target="_blank">📅 08:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463804">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f430bde39.mp4?token=dzGaR2KOkXqsx_UM6NiCPjo6LdXgwvsrz7lDvmZITElGzMd1FPS2HYeMCIT9m4msgpigRYUrdof_udFw4Tmh5JDhJiUkF2dfuh11GI_CLd7zdBblLafJiLLsZbkO_4GzhZpsnvYmXI41dUlKLnNimInoX5Xh4L-ZTIdmUq_U3HMAxK8n987-IIkCx2ktQpzf0mYaor84lsMf5uXrRSPrvH70z9x5LyXrgicRY92qeDLa6ZrlNeQ9rpaNpIxzgtYc_Ff2B_FSb-HuGyYOhgnUqN5lB-Fghbt8r9NBhMgB2hKVZm7hm9rbg2HZayKC9wNqNjwP5TV_Oz2-v4LCyeon7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f430bde39.mp4?token=dzGaR2KOkXqsx_UM6NiCPjo6LdXgwvsrz7lDvmZITElGzMd1FPS2HYeMCIT9m4msgpigRYUrdof_udFw4Tmh5JDhJiUkF2dfuh11GI_CLd7zdBblLafJiLLsZbkO_4GzhZpsnvYmXI41dUlKLnNimInoX5Xh4L-ZTIdmUq_U3HMAxK8n987-IIkCx2ktQpzf0mYaor84lsMf5uXrRSPrvH70z9x5LyXrgicRY92qeDLa6ZrlNeQ9rpaNpIxzgtYc_Ff2B_FSb-HuGyYOhgnUqN5lB-Fghbt8r9NBhMgB2hKVZm7hm9rbg2HZayKC9wNqNjwP5TV_Oz2-v4LCyeon7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مدرسۀ شجرۀ طیبۀ میناب در اول مهر @Farsna - Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/463804" target="_blank">📅 08:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463803">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318fa54bad.mp4?token=BW4SREg8Vhity3AuDCjFKBIAoOYnRTQIikjhhr45VvAyQtvol8xejvaUcZlkKg7Yj30FjZYXUH5jMWUvwWy4ksFcb6e0MGrX3XFNzLAOnV1dVMB67-lNXx0A4Ugd3pE1kOK7ATHDzApujIz0n00ygxbiKvXLw4tSyhmsydu1PaNAuLoQy0HPsd3miDL1oQrLAANfe-41HatRzvrKyhsBrdnN45YdX1sc-qPAG7Uap4cmVflQFHMXvHwyn7lm0Q83PbMPN2LmLyiv1GvZJ0_lTHTOe-IiSru-FZfGxADepd4eN4L0_yXL3QLbd9bezFK1jyeATmD-e0Fjscxv24-aig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318fa54bad.mp4?token=BW4SREg8Vhity3AuDCjFKBIAoOYnRTQIikjhhr45VvAyQtvol8xejvaUcZlkKg7Yj30FjZYXUH5jMWUvwWy4ksFcb6e0MGrX3XFNzLAOnV1dVMB67-lNXx0A4Ugd3pE1kOK7ATHDzApujIz0n00ygxbiKvXLw4tSyhmsydu1PaNAuLoQy0HPsd3miDL1oQrLAANfe-41HatRzvrKyhsBrdnN45YdX1sc-qPAG7Uap4cmVflQFHMXvHwyn7lm0Q83PbMPN2LmLyiv1GvZJ0_lTHTOe-IiSru-FZfGxADepd4eN4L0_yXL3QLbd9bezFK1jyeATmD-e0Fjscxv24-aig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شیفت کاری نامنظم چه عوارضی دارد؟
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/463803" target="_blank">📅 08:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463802">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97cb710862.mp4?token=DQQ9dp-yv3h1nQ26YOjBMv_lMdIfXGcMwdAKKhPW5leAE01Ac8dCs9C6p_sF9d3nHO9i464i0KyhLItlt-gEuq4hN1R9UGniAmbZABIY0oNFg1pPlK5k175vGvSTKa1gYTLEWgWqId5L9tCPnUMMuiPJdgK_dMZ1_hh671ku8mq7sZS-WiuEx8czD29YasR5tJGKbh0bBb5RJ0dinOtW08nkJCtRGvVjYHcIntVSzI368CJsOo31SA8Dcw91AxdOGJaWr1HmQqOeC0PAEw3sO7nczCMCeKKnrrFGbmKIHMrzGYAdxli5E-fbV9_MNCh1YpfLkuA8hxIaaI96SIly0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97cb710862.mp4?token=DQQ9dp-yv3h1nQ26YOjBMv_lMdIfXGcMwdAKKhPW5leAE01Ac8dCs9C6p_sF9d3nHO9i464i0KyhLItlt-gEuq4hN1R9UGniAmbZABIY0oNFg1pPlK5k175vGvSTKa1gYTLEWgWqId5L9tCPnUMMuiPJdgK_dMZ1_hh671ku8mq7sZS-WiuEx8czD29YasR5tJGKbh0bBb5RJ0dinOtW08nkJCtRGvVjYHcIntVSzI368CJsOo31SA8Dcw91AxdOGJaWr1HmQqOeC0PAEw3sO7nczCMCeKKnrrFGbmKIHMrzGYAdxli5E-fbV9_MNCh1YpfLkuA8hxIaaI96SIly0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود کاروان تیم ملی امید به ورزشگاه محل برگزاری بازی با کرۀشمالی
🔹
تیم ملی امید کشورمان با ترکیب محمد خلیفه، امین حزباوی، دانیال ایری، فرزین معامله‌گری، ابوالفضل کوهی، مبین دهقان، امیرمحمد رزاقی‌نیا، امیرحسین حسین‌زاده، یوسف مزرعه، سعید سحرخیزان و کسری طاهری، ساعت ۹ امروز بازی را آغاز خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/463802" target="_blank">📅 07:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463801">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fafc0ac85a.mp4?token=tH671h3rBKxZMVWYIYqd8i5PoEUmsfB8yhZVE5I7Y7Ia6bR-Ykykqtp3J_QqnOio4yl_zScVWFRnDYs5fcNT19P565uNH3Oi-JOvdel0NzzTqIHvT7ehV_FE0NMhJyKcJmMau5vvmqQOTEDOo0SkwGOOiILi3AA_rrBSABa1f4votqX_ZVqpEq8oA2WEI6RXhiO0ZMrDmEgwGhZn8384T13me9anBvOYgf8yRBYtizh2FH2U2IZc88WOwXmeRiN3NiujS3y6C78BcHB3S7139ugD6Lv_vGW6d_FBQvmJ8j7tclpuvDhKLncPxZS1fzAi83evhjnlbnMJq3_NJyMCtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fafc0ac85a.mp4?token=tH671h3rBKxZMVWYIYqd8i5PoEUmsfB8yhZVE5I7Y7Ia6bR-Ykykqtp3J_QqnOio4yl_zScVWFRnDYs5fcNT19P565uNH3Oi-JOvdel0NzzTqIHvT7ehV_FE0NMhJyKcJmMau5vvmqQOTEDOo0SkwGOOiILi3AA_rrBSABa1f4votqX_ZVqpEq8oA2WEI6RXhiO0ZMrDmEgwGhZn8384T13me9anBvOYgf8yRBYtizh2FH2U2IZc88WOwXmeRiN3NiujS3y6C78BcHB3S7139ugD6Lv_vGW6d_FBQvmJ8j7tclpuvDhKLncPxZS1fzAi83evhjnlbnMJq3_NJyMCtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیمۀ اول دیدار تیم ملی هندبال ایران و قزاقستان با برتری ۱۶ بر ۱۳ تیم ملی کشورمان به پایان رسید.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/463801" target="_blank">📅 07:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463800">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUL4OG2oUUyGuVuZ87sS_zRom69VzoMIs0conAm1htL14DoiUFN1pc1A1NIs4wUWzt-kQ3NLbYd2Y57dscczSL0P4WCi99qlJ269xyzs6XsL8Rc6rM-Swk0BQwxxO2t66h9KG0gXXaRGQc-nEJk7gILbCwNx3f9XRCOV3Ot4LzcVGxVzEQ_3-qP9VGVZmBM7jKxqKvo18CNWoc0MD32sBY4B-KVhGWNtQfqEENKAXMP0xZTXhmyTmcJqsDEUxdD5r25q2v2rm50Huh1XEeKMoVLb4zYO9JX4eVSSboEs3XKlU4vBDJw1x8fq_woLq5hzgF0NqTqN-8RARXB5Qhzuaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنگ مهر به صدا درآمد؛ ۱۶ میلیون و ۷۰۰ هزار دانش‌آموز به مدرسه رفتند
🔹
سال تحصیلی ۱۴۰۶-۱۴۰۵ با نواخته شدن زنگ مدرسه در سراسر کشور آغاز شد و دانش‌آموزان تحصیل را آغاز کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/463800" target="_blank">📅 07:53 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
