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
<img src="https://cdn4.telesco.pe/file/l1jc-ofSF6lu0fxdUE4p9PWiFwlnpYfLmN1Xk4bQ4QOnp8kl5zZ1IIXwlaN5aHuDJ4oM-ZQd7P99qfQaOoAVjDV0Zqy-7QlJ7eo55bJWsxKkrRamDGUzVKmfAL9ZgXfZhjQjR3Yutf8Re3rAMNdIm7yheohWVdDrdWdTQ68x82JC3xkRDzY8iplt6YGinUNSrY1_wMwZRhgwcmz6UFPRgHCfcC6hcEqVsNk71BTYapF7HOKN2tnKHz1ETBSh2tPqALj3NNeiCdR5uvE85opIfQLOgoFEbM0VTRv8IT7VRfWsz2LQGSKn4G7zX_HLq_dq4yoqaGx6Y5YfMP4Ru0v4xA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 00:24:30</div>
<hr>

<div class="tg-post" id="msg-72540">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fe1c6438a6.mp4?token=aJBT4RWu_QjpSEGTxkGxC1i4-_L3lERv2-y-8h_dGhO-nzcqS-ZjBnehpPeEUQ_2lSZ9YZArEDijm-f6ca2YbGNooe6NENHheXOlFVFhmNk-73m2WpZwYxwEoNsOYtDeZVchQsuiWe7QIrI9-PlZhP39X2b8WbwZPerhqWncqrHFVJo8nf-YnplBj2nOtFWs3BLK2Xv3lC0AggWuLHks-E3HrAv5Jb_haIbg4vEMITtUBiSJ9E7RcJmV13bBnL4i4KJpUQ9jHlCY-xfFiB8vgwFT7UeaXurZNH1UnjHKr4nXSLW5Q_xx52FZR9abRGqqu9bIP-bRETg0fXEm7-MjUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fe1c6438a6.mp4?token=aJBT4RWu_QjpSEGTxkGxC1i4-_L3lERv2-y-8h_dGhO-nzcqS-ZjBnehpPeEUQ_2lSZ9YZArEDijm-f6ca2YbGNooe6NENHheXOlFVFhmNk-73m2WpZwYxwEoNsOYtDeZVchQsuiWe7QIrI9-PlZhP39X2b8WbwZPerhqWncqrHFVJo8nf-YnplBj2nOtFWs3BLK2Xv3lC0AggWuLHks-E3HrAv5Jb_haIbg4vEMITtUBiSJ9E7RcJmV13bBnL4i4KJpUQ9jHlCY-xfFiB8vgwFT7UeaXurZNH1UnjHKr4nXSLW5Q_xx52FZR9abRGqqu9bIP-bRETg0fXEm7-MjUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنجاقک‌ها زیباترین مدل رابطه جنسی رو دارن.
اونا بهم متصل میشن و شکل قلب تشکیل میدن و تو همین حالت پرواز میکنن و... تا کارشون تموم بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/news_hut/72540" target="_blank">📅 23:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72539">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a16c7cb51.mp4?token=TEFhAuGGWRtB3DIo563jvZxGLLowrITthabWa195tL-qIVN9y7Fj3aVa_RZs1uTbDv6WuxHVjQ2qQxlhDV-pFJZve_PagF-9ahzg7DDPM8xpSHBN5jSSm8EVgjuCZf2H1CW4l4jnWWmfDk46IFZf9oQd7w4RMGHuUDoqMYCgFDErL29bQv7vgpoiI51V9tEhIqaLkKcOmAtK-qD53RKlXB8YXsHLAjsqkmRUQTAC0QE9UF1PFO-uUn1kFwijhnhBZgBVqkTzYZaHk1GbYyjIUjxFJXQptpT8reEbP7zp68bCf0buNlZhHgYKe0JIY6iidsGqwwrlko3vGrFNKhdhLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a16c7cb51.mp4?token=TEFhAuGGWRtB3DIo563jvZxGLLowrITthabWa195tL-qIVN9y7Fj3aVa_RZs1uTbDv6WuxHVjQ2qQxlhDV-pFJZve_PagF-9ahzg7DDPM8xpSHBN5jSSm8EVgjuCZf2H1CW4l4jnWWmfDk46IFZf9oQd7w4RMGHuUDoqMYCgFDErL29bQv7vgpoiI51V9tEhIqaLkKcOmAtK-qD53RKlXB8YXsHLAjsqkmRUQTAC0QE9UF1PFO-uUn1kFwijhnhBZgBVqkTzYZaHk1GbYyjIUjxFJXQptpT8reEbP7zp68bCf0buNlZhHgYKe0JIY6iidsGqwwrlko3vGrFNKhdhLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای زیبای این پسر در مورد وضعیتی که برامون ساختن، ارزش اینو داره که ده بار گوش کنی و براش دست بزنی!
@News_Hut</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/news_hut/72539" target="_blank">📅 23:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72538">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFoIf_Nfr0UfW7nSEXZyjVtBdP2cP8gmw8J8DCzAl9jjdgBF-KF9zjgidu5-v7Sm85jH5mz2Qqyrwclur4lAHogsoh3jfShsxUX9MIgcgzBlorVyM1LUNlJdUiWRsN9meT2EVaxkbLfxVjA36GiOMoTMT8J31fwmYv_DydabfaeBTO5ipS3ZSLLcB_j6YB1gmp_XVVSq4q2J9IFtZ_Crxl5le6Utfo6MfxR0r2dtudhXEu3alKxRAC3mWhSN7JwIW8PqQO89SUEPYvgrqPnVa78_Mt66I-h9q-iTvxrJxVJFSBi4vx4HAlpNnkMIui8wQ8cQywCnLXUdEwdUonRL4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت بوئینگ با پیشی گرفتن از نورثروپ گرومن، برنده رقابت نیروی دریایی ایالات متحده برای پروژه F/A-XX شد؛ قراردادی به ارزش بیش از ۲۰ میلیارد دلار که به توسعه جنگنده نسل‌بعدی نیروی دریایی برای عملیات از روی ناوهای هواپیمابر اختصاص دارد.
انتظار می‌رود این هواپیما در دهه ۲۰۳۰ وارد خدمت شود و جایگزین جنگنده‌های F/A-18E/F سوپر هورنت و EA-18G گرولر گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/72538" target="_blank">📅 22:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72537">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره ایران:
ما تقریباً کنترل کامل تنگه هرمز را در اختیار داریم؛ البته باید بگویم کنترل کامل، اما هر از گاهی آن‌ها مین‌گذاری می‌کنند و اندکی در وضعیت اختلال ایجاد می‌کنند.
با این حال، ما عملاً کنترل کامل تنگه هرمز را در دست داریم.
در سه روز گذشته، حجم نفت عبوری از تنگه هرمز بیش از هر زمان دیگری در تاریخ این تنگه بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/72537" target="_blank">📅 21:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72536">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ درباره عراق: داریم با کله از آنجا بیرون می‌آییم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72536" target="_blank">📅 21:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72535">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88278c6cad.mp4?token=U-NY_qiFSSZ7BWzWgFl5nuFZk2j18QgHs-8WKo0rMXPPRkMI2zPrmvVKa0QXthQ4cvEHFx8_abEMP0oJuNb16q1c4sz-1K8OelMewngO6t5bnFBH1CiHmjrnrynQdJjwC_DRxEfbSp218yFMIaHBlIFXhZu1Pr7Old4gTRTKUevWff5l4rqksT9VdUgEgzStlNgu4zJxeBK4G9qvTHW1Bb81QG4smwyBB98mFlQBi1BjhIYRXOgE9iUR1S4pcKUk5kIm7rf8OgiQ8JzAIyRkuNdzpXiwwbUUboQ4c78Y0T6sRWrDEx2zn6hjmzca3bfkDeIbBBvMZ7qtey6o2w5W7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88278c6cad.mp4?token=U-NY_qiFSSZ7BWzWgFl5nuFZk2j18QgHs-8WKo0rMXPPRkMI2zPrmvVKa0QXthQ4cvEHFx8_abEMP0oJuNb16q1c4sz-1K8OelMewngO6t5bnFBH1CiHmjrnrynQdJjwC_DRxEfbSp218yFMIaHBlIFXhZu1Pr7Old4gTRTKUevWff5l4rqksT9VdUgEgzStlNgu4zJxeBK4G9qvTHW1Bb81QG4smwyBB98mFlQBi1BjhIYRXOgE9iUR1S4pcKUk5kIm7rf8OgiQ8JzAIyRkuNdzpXiwwbUUboQ4c78Y0T6sRWrDEx2zn6hjmzca3bfkDeIbBBvMZ7qtey6o2w5W7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فووری
؛ترامپ درباره ایران:
خیلی زود شاهد وقوع اتفاقاتی خواهید بود.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/72535" target="_blank">📅 21:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72534">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مَردی پنج ساله به بایدن فش می‌ده که چرا از افغانستان کشیده بیرون، الان خودش تمام نیروی نظامی آمریکا رو بعد ۲۳ سال از عراق خارج کرد
#hjAly</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/72534" target="_blank">📅 21:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72533">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af74dbf4d.mp4?token=pkrqloHLrLNpnnT_XJ37RmbE8mg79o6tUX82DX5Su32YPygQAczQOUmnXX_-3Ej8E7JhFWC2my3mcEr4orHkvtfeawrML8JRr3Cl9E4iizjmAqUJRNd0Tyxg8XFU_rgpkRL7kTf0Sm7SYcS9xWmcpwg4XjENHCxSksuWpake9bQv0CgKvazV-i69XJKeOKTTcLBXqh2IsanPt9Hk6zDTHqttKx6ByKrEc-VcyzrzkF-9mOyL8NjDOWgv7KsnoWa6FF6A3I2nzIdX8PrHqNKRRIKH1P39Lq7QY30YiuUpn5TcABaZacfleiFHUxllNCyrx1R_0XkOYu0CoOByR68CsRd5rM2h7iCVhxrf43ghzPaWuwjl9jsYPh6GJJuM1QdXcukNH2Stg3sG2ALHpYZzpDJQZl0hmecLrZFC8oR3MJgNYV72XAeHcHUxHx51AwnTsa6H229dJnCfqvmK9L2IJl1-GV7IJnX0kO3f-H-QoFAxAf76sNMTsDja6En8PpGesG7EDhZhvzLBZcsbcXsWDdV6lQj3TSAiCvKgLDtRCt_A8U0XciZ3fZ4uHvlX2QcX7uCwmkVimDQsDwx3d2PkTCFNrEyHzzb3kRHSHSGwnneOxCESYAs3CHvrgbWaT2uC97UJyGts7FRlEiWKV_ZlKc6KbXDvQ89ZRXbjsm9IxEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af74dbf4d.mp4?token=pkrqloHLrLNpnnT_XJ37RmbE8mg79o6tUX82DX5Su32YPygQAczQOUmnXX_-3Ej8E7JhFWC2my3mcEr4orHkvtfeawrML8JRr3Cl9E4iizjmAqUJRNd0Tyxg8XFU_rgpkRL7kTf0Sm7SYcS9xWmcpwg4XjENHCxSksuWpake9bQv0CgKvazV-i69XJKeOKTTcLBXqh2IsanPt9Hk6zDTHqttKx6ByKrEc-VcyzrzkF-9mOyL8NjDOWgv7KsnoWa6FF6A3I2nzIdX8PrHqNKRRIKH1P39Lq7QY30YiuUpn5TcABaZacfleiFHUxllNCyrx1R_0XkOYu0CoOByR68CsRd5rM2h7iCVhxrf43ghzPaWuwjl9jsYPh6GJJuM1QdXcukNH2Stg3sG2ALHpYZzpDJQZl0hmecLrZFC8oR3MJgNYV72XAeHcHUxHx51AwnTsa6H229dJnCfqvmK9L2IJl1-GV7IJnX0kO3f-H-QoFAxAf76sNMTsDja6En8PpGesG7EDhZhvzLBZcsbcXsWDdV6lQj3TSAiCvKgLDtRCt_A8U0XciZ3fZ4uHvlX2QcX7uCwmkVimDQsDwx3d2PkTCFNrEyHzzb3kRHSHSGwnneOxCESYAs3CHvrgbWaT2uC97UJyGts7FRlEiWKV_ZlKc6KbXDvQ89ZRXbjsm9IxEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛
اندی برنهام نخست وزیر بریتانیا:
شواهد محکمی وجود دارد که نشان می‌دهد ایران در وقایع آخر هفته در پایگاه نیروی هوایی سلطنتی «فِیرفورد» (RAF Fairford) نقش داشته است.
در زمان مناسب توضیحات بیشتری ارائه خواهیم داد، اما می‌توانیم این باور خود را تأیید کنیم که ایران در این ماجرا نقش داشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72533" target="_blank">📅 20:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72532">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">#فوری
؛کانال ۱۴:
بنیامین نتانیاهو نخست‌وزیر اسرائیل طی ساعات آینده با ترامپ تلفنی صحبت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72532" target="_blank">📅 20:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72531">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e30841564f.mp4?token=bIGFFb5Er8qCYryEi7oMzq61OO7MK7ry47iI-sxEfkxt17Non_O6MB8CV3TmDAe8dE1HIbg1PG5Exd-ncMn9B6ZYghDjhDt2Imvq3qqMcXHb5nMsB3dNdd7cxYBlLuHRD2V2W_XZ3ofCCxzTkRm-QD-piBQ0f3BG2QttRNpzOtsMWnmGndTWxoa7pSU1qlGDkxD_ney3sQf6QwnqhBzA43T8fNldpVrfizb5seFshVluzs1NtOmU53H0nRW2QQm09PxLrgCQLjRQO3aRvbynOUo7lycXi8LNmh-dTUa3AKZFrBqWUHMMlCP61KG5bv2AQ9hwW5jB3tC_WhwsdMPG7IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e30841564f.mp4?token=bIGFFb5Er8qCYryEi7oMzq61OO7MK7ry47iI-sxEfkxt17Non_O6MB8CV3TmDAe8dE1HIbg1PG5Exd-ncMn9B6ZYghDjhDt2Imvq3qqMcXHb5nMsB3dNdd7cxYBlLuHRD2V2W_XZ3ofCCxzTkRm-QD-piBQ0f3BG2QttRNpzOtsMWnmGndTWxoa7pSU1qlGDkxD_ney3sQf6QwnqhBzA43T8fNldpVrfizb5seFshVluzs1NtOmU53H0nRW2QQm09PxLrgCQLjRQO3aRvbynOUo7lycXi8LNmh-dTUa3AKZFrBqWUHMMlCP61KG5bv2AQ9hwW5jB3tC_WhwsdMPG7IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آشیانه‌های مرکز پشتیبانی لجستیکی شهید اثری‌نژاد نیروی دریایی سپاه پاسداران در شیراز، پس از عملیات خشم حماسی:
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72531" target="_blank">📅 19:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72529">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PvqDnHQexkrG-8DtkE0n8PTugFKL7t-1-h2Kggw_h571WuaG9QRY6dCJNu3nAqG4FVC8FATFUihCF2bJb9JAUVShk9mBjjUM2S93s5Ds9p2fkjs62j8u_-ta2yvitjSJIRjfCNvAmK-F2lC3O06ikDCpPlon6n9gfj1CkHyT8wTTx0Qf26MjFH2gB8LiSuB-nle1aNMA7PjFccakGk6oqDNiL_vt23clW4aqXOvKxosc-zAngxO_kxlTgXKzfgBxNoEVK7hN-WJP25BIPF2iZWgq2Xk_vZ47AZoozEDwFI_fAL4VwVtsqgC3JNah2gMTXQU8ABDpu-hkUSUpqw5DpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RQCyaYMjYA0csIngHp0ToAcb1VaD-dnsv13oA_KB8cpP0V7U3qELZeyxpaXjKuSmBqzkpnvpnfTjgxUi2NYSCDtP1NRPphy3JkfHHVhVzU2cfupd4GnJd4fyer6sflNvSEKXArBhrXivxordUKpxfYUofyloVZyhni-uEGsIPlQ2D0BeM0-J7eCeRoHu7ShZ3jH80xq-p_BWU5vdkUlUuq-FbE2q43fTMBffBO5DGVx-Mca6QviHZA-hlWjDO6Bify8vFk0uKt3ncsRYwv8ZICuMJby-9tb87L3G8ql2OvbRaSHB9M3QY69cjFfIvjJokRd36XRs15T7ggV3oC6vtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرتاب موشک از استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72529" target="_blank">📅 18:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72528">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نتانیاهو درباره حادثه پرواز دبی:
«یکی از خلبانان، خلبان دیگر را با چاقو مجروح کرد و ظاهراً تلاش داشت هواپیما را به همراه سرنشینانش سرنگون کند.
هواپیما وارد حالت چرخش شد و شروع به سقوط کرد. یک مسافر اسرائیلی و یکی از اعضای خدمه وارد کابین خلبان شدند و خلبان مهاجم را خنثی کردند.
یکی دیگر از اعضای خدمه پرواز نیز موفق شد هواپیما را به حالت پایدار بازگرداند و از وقوع یک فاجعه بزرگ جلوگیری شد.
خلبان مهاجم هم‌اکنون توسط مقامات سعودی مورد بازجویی قرار دارد.
به دستگاه‌های امنیتی دستور داده‌ام برای مقابله با تهدیدهای احتمالی دیگر آماده باشند.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72528" target="_blank">📅 18:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72527">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72527" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72527" target="_blank">📅 18:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72526">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6UhA3LVydapccpK0aWeIX4qKGuj_oCA7lEsnjD2cq3SDWh166b4Ds4omMMBTJgLtCjnqEHq_d0E4fLpMb4ZzUTa25QtOETpUL5Nz4jX6nNvyTWCRf5PMrfS_qAmgZjEMW0-yaJU-zLIiXljTGt3dcF_-FPyMN872I2lYjEGhU7W2oLK7EqqUqbNw5-F2u1za1YyjuXk6ecY-H_uoncvmC_Zd3Ne_fDzWtLzgRLph5YE99aW__Pe3aB90VjEfGFGij7W4Nyz4t9lMFg2KabFPSJYaYbBsITcvSuixdE0Z_zBHjoUpndceV0kWK7PoeaCGZuuLg9Rb0qbWyy6BxCiuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72526" target="_blank">📅 18:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72525">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fbae6ebe2.mp4?token=P7hCk4aKqie08KfA7RrQVjlaAdazl3C3x4XandEEtZmQiRdwL-KVKEsDI6oxW0N9ZLLeyAsDe5av_WliKMOSzaGpXgJMnKN7Rx1qyL82Q8ylkJ1pRZFoPpeTugniHHLAYWBMaBBPM8Jxr_p1Ud0IKf5AzRbW_O9ywYwVOw1G-u4NLF1Q4vUdmmOZua96DvLsrkV6NApVXvqJaUPbR-X-42sT-koctnrocjjM3OaLH_aq8468OW6UP1VBOsZB2-8fAFPiVLWDxbis4bRxBkzbxZdJlGxxEJKB6YYJ6ZhxCZl9B9cw7oO8dvhBcPOyiFe_TGgzH4MDx0YjvzscjYTDPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fbae6ebe2.mp4?token=P7hCk4aKqie08KfA7RrQVjlaAdazl3C3x4XandEEtZmQiRdwL-KVKEsDI6oxW0N9ZLLeyAsDe5av_WliKMOSzaGpXgJMnKN7Rx1qyL82Q8ylkJ1pRZFoPpeTugniHHLAYWBMaBBPM8Jxr_p1Ud0IKf5AzRbW_O9ywYwVOw1G-u4NLF1Q4vUdmmOZua96DvLsrkV6NApVXvqJaUPbR-X-42sT-koctnrocjjM3OaLH_aq8468OW6UP1VBOsZB2-8fAFPiVLWDxbis4bRxBkzbxZdJlGxxEJKB6YYJ6ZhxCZl9B9cw7oO8dvhBcPOyiFe_TGgzH4MDx0YjvzscjYTDPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏عاقبت لایی کشیدن در نهایت همینه؛
ممکنه چند بار تو رانندگی از روی دست فرمون خوبتون موانع رو رد کنین، ولی بالاخره یه روزی میرسه که ممکنه یه همچین صحنه‌ای برات رقم بخوره...
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72525" target="_blank">📅 18:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72524">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8caf88eae.mp4?token=IE7BXHrVbi0rqvuFAp2HCF79RhXlTmzi12dQdpDnyfS_QtZjtAQkODjMTJFRlWAr6QcdRR0I9UIKe_Lt0sryCvbkbEiuEiVGJ0yAw16MHIqPRH_Ot1H_VLeIwj-wkKo2D-je2U1pTX8b4hxS1Q8HrkrApOu-UYTbal6Y4P-32lK2zZQon2_-RL39krix9kYX-076Ogn3CnVC_5RSffRvXeKSjtZRaO2gxzhDJX-ppEhtED6qaV3yWw6PFRHPgGgjWCNy3K1eThkq_3fIYDUjeIIi5f9k7oXN6nGBSTxejhChnuwyxyiC0nIL382jzz6KKd139fM3gGsrlUq2jnd0OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8caf88eae.mp4?token=IE7BXHrVbi0rqvuFAp2HCF79RhXlTmzi12dQdpDnyfS_QtZjtAQkODjMTJFRlWAr6QcdRR0I9UIKe_Lt0sryCvbkbEiuEiVGJ0yAw16MHIqPRH_Ot1H_VLeIwj-wkKo2D-je2U1pTX8b4hxS1Q8HrkrApOu-UYTbal6Y4P-32lK2zZQon2_-RL39krix9kYX-076Ogn3CnVC_5RSffRvXeKSjtZRaO2gxzhDJX-ppEhtED6qaV3yWw6PFRHPgGgjWCNy3K1eThkq_3fIYDUjeIIi5f9k7oXN6nGBSTxejhChnuwyxyiC0nIL382jzz6KKd139fM3gGsrlUq2jnd0OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ بعد از دیدن این کلیپ تمام ناوگان های دریایی شو جمع کرد و دستور داد همه برگردن امریکا
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72524" target="_blank">📅 17:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72523">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f862c5d3f.mp4?token=dvUYAo_tcycVsy2zV1hN3alW5E25qhjDbqMcxHX8mQpY0mi_AToSAih15eMPHL5Z8m4QwSYaUloaYoIDX2TWDh9Pcawx2ktk9ikiSabwb8H1WnP06WjcrXn7HsDfUfey4gj8FVYbXy-Hr7uyHAbu5LI8b-LjxjPUK1afYdHaYH7RYizgsmspIpRj4PrVdsVzroYgVw0M1-LcXCt0RsFQdd5Y1ktwD9rcHEeX2NktLfcFdM5OzFIX5TPVMbNbu3azz0fCYoRuW0pz0niBD71qmu3cChGjKzCfdji5kgfpZTgCg4hDe1DgFYslGCY2WN2H-BOr2WlVAhLnc5EsluQjeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f862c5d3f.mp4?token=dvUYAo_tcycVsy2zV1hN3alW5E25qhjDbqMcxHX8mQpY0mi_AToSAih15eMPHL5Z8m4QwSYaUloaYoIDX2TWDh9Pcawx2ktk9ikiSabwb8H1WnP06WjcrXn7HsDfUfey4gj8FVYbXy-Hr7uyHAbu5LI8b-LjxjPUK1afYdHaYH7RYizgsmspIpRj4PrVdsVzroYgVw0M1-LcXCt0RsFQdd5Y1ktwD9rcHEeX2NktLfcFdM5OzFIX5TPVMbNbu3azz0fCYoRuW0pz0niBD71qmu3cChGjKzCfdji5kgfpZTgCg4hDe1DgFYslGCY2WN2H-BOr2WlVAhLnc5EsluQjeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسر بچه دهه نودی با اجرای رپ خیابونی، این شکلی کلی مخ زد و از دخترا شماره گرفت و بوسش کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72523" target="_blank">📅 16:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72519">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNBNW3j6cBCivss65DbuKm2ZA2Kcr_BPPza6pzJ0s4uux89oB6ML3X2Cz72pLbGAWPo5pDRN2GlxVrAABiZe73y1W3aQss534JN_BTgdGTw7uQCdPDR_Nul4qbJBuuUWzaoew5AWPt3PkTgMmTkzvFt0iN7ochsHwEpeBoKIvlb08tbrr4kkbYUlKjDFSBPwfKrI0-hroLmks9N-lgK9a-qwgS28Fn0WdY5qaZPmlkhzqbzj0oqCRzHhCWQSbceqwJQsAWWd-lGF9ht55VvJMxN1XvWCnOyAH5BGg1jV3honVky9eXVSqz-OVieP_lX-4eBQ5ybhDDy_lOiM8j_Udw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/670f963d1a.mp4?token=p84ub3UFhfN8lq-68jfHJrQnCsZlC9Vav6Easrar2qWvVdKvRyDZyfb6Qwj6fWtbAmp1XcJMgeMZ3sZ7p_zEw_SByobb643WXvfafEo-9Fzo1mY7usYK71LDJ5tTN3a41aGlxwBGCYlGxDIvgxtsY_c10_wAu5eok9f5Sbf-44FpmaEhObBYGQeJ3fPmk41zkNIghLyQ957a4gLpiglF3AiaJFqsMe7kyrHabKyudlnt3aW7k1ZhOdHBzjesVn8LikYn03PPNgGUGXcbp34-6iGuFExi0TYiMmri_kB41l6hopxAAhk8CypsnXnBPAa26fUjBh0-yagq6w83Ydt-Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/670f963d1a.mp4?token=p84ub3UFhfN8lq-68jfHJrQnCsZlC9Vav6Easrar2qWvVdKvRyDZyfb6Qwj6fWtbAmp1XcJMgeMZ3sZ7p_zEw_SByobb643WXvfafEo-9Fzo1mY7usYK71LDJ5tTN3a41aGlxwBGCYlGxDIvgxtsY_c10_wAu5eok9f5Sbf-44FpmaEhObBYGQeJ3fPmk41zkNIghLyQ957a4gLpiglF3AiaJFqsMe7kyrHabKyudlnt3aW7k1ZhOdHBzjesVn8LikYn03PPNgGUGXcbp34-6iGuFExi0TYiMmri_kB41l6hopxAAhk8CypsnXnBPAa26fUjBh0-yagq6w83Ydt-Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک بمب‌افکن استراتژیک روسی از نوع Tu-95MS در جریان یک پرواز آموزشی در منطقه «آمور» سقوط کرد.
این هواپیما حامل چهار خدمه و سه سرنشین دیگر بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72519" target="_blank">📅 15:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72516">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cAnFo-B-of4sIOCQ4GydXP_zrHDoljGscC3r4g3DQzRgDhD1OGn38jN-xqNAr3StBHebn1hCoJNuwF54f2QZoSLVQDPdD1xb6fpB3pKhkje4f90sr5aKk__cqyg1e5cs8auJoQ0Ibn40mQ2qZBs9_yTdr5aPVSTeNUNaSI1fxW0VWhgQ5r0bdIMPnbwFGxyks2Y7bDbv8Euk4RDbR4R6oMGc4dOr-Tz-tqmz1fN8-pIj3u8_TN7uqbJRo48poxeYaAhgeDsI4hNnTGf9MrX7uTJzNd1eHdRPKvvjBSR6QSaokhUuu-4FxGb5CpVdgVTOJKbatW7l-aBOVicOQy81mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m-IATSsdmKjfTDC3dkuO2FQvA_TalGd61u5NSt7xdFFWLmszORfhf7_ttpX1EEDQs00fDOZsuBIP4NPg1z_d1cvmYmhcBKX94G4J9emAy_RcSnMVNyV18q3HdVinJGSkK1cJWMR7tb43AnADvNV8SSupuxgxRFMWjtrI__WrAwsPqI-UGurPiWyKG-Z2PbvB6g36E3l_Xnz-a7u0TRKbh4D4oy8lPyKNWYZcRhc5bChM19SAgEm05TqLLDlWUeUE1S94hFxMrZKzC3woukbjPlv8XOlam6P5Hbqsjz047t915oNETPb3e7iimQlJjRRNuVLL7Zc8VJDzEEWs2MAv-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/riAnVB8vT0NZXoiZroQb2TTkfo-uD6NLJvAtc_Iby3Sz30nsLFtifsZxLIUCh3UnII2f2Iuc2pJPFC2b0884pVG_3hxlsOxKk3zFydvKTnLcxeByFWOiy1GXpCpaS91uFyO3ZGj41OsV5kUa_IP_Lh2Z8a-GBr8Iv4i1C3w78tjggii7R6oVb5eB2q7Ff8X92uKR8PEWD85a70uextpd-Y_Kewa-TkSMqZ8rGvWyk3fZVQbMxWFbiJfd0frExAXUksS4my0u8spVn3QSXI5bonI8SRymcs9dkEw4V26CPiaOIpMaw2unEjJxwwoZkHm6JZZuLZSyQPkI00Zl9XMO5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنا بر گزارش UKMTO، سپاه پاسداران امروز به ۳ نفت‌کش و کشتی حمل گاز در تنگه هرمز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72516" target="_blank">📅 15:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72515">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4993b45c70.mp4?token=k3PMURuQAd2PyT9Jc3UWFt3fLzPERgaW0cLjjpmAOh7IKywfIAf1nKDmlO4-YK4gjzWkwDabRJPpMioqJZAd03CQJi-pmcXSDXLQ15aLLsny03_W6WpOen7FB5sIk_n6zEHvASzGHTsPZHfU4Zpl8rf4cmkaMef5yZ2lNu7s_1PFkMesn-rAQN8GZ3B8tBcizTEOvn9CDl-Y7igROPvPpFcCadtyRdyvmXTXtBzobmHF4Fs31iyYz6WaTpSjQXY18Yv6dy_-O7-6RWiFXLIriokEVbuzpl8yEJkM4Lrr2s4UAn69UoG_L-gRdvDk8Rw3qoveJF8F3VcwFgF6WI-KjSzF8AbvsNcdgeV3Gtefdmjr1p6rqPvZ13nIl4iO_JP_DlkvGBrPvTaD1luYTszvHToyKxDXVigxNHSuOKwHv8k8nhVGDq2nXSw9XUCwB6jX7TE-tnyiJdyrrLqULZqb_UJaV046vSE2DyZwm7QReR7TI-JFzaGA4LxcQJujsK7Ex6KIS7H-fJ6-_aMLbpPD0kbKTIm7B6ZGbB7RH7viFL2vMFWmYPEQ8PRD1I_QQELnKZ9YiyRF1T1Y-PTvZ_7MrVtdDloSNjvAmBOU4c81wvBctPqqyY2rrNiZL-9nlnwEzOh9d0m02y_Tr_U6p8AQZYBcdfEjpK9tMtodGVKvo6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4993b45c70.mp4?token=k3PMURuQAd2PyT9Jc3UWFt3fLzPERgaW0cLjjpmAOh7IKywfIAf1nKDmlO4-YK4gjzWkwDabRJPpMioqJZAd03CQJi-pmcXSDXLQ15aLLsny03_W6WpOen7FB5sIk_n6zEHvASzGHTsPZHfU4Zpl8rf4cmkaMef5yZ2lNu7s_1PFkMesn-rAQN8GZ3B8tBcizTEOvn9CDl-Y7igROPvPpFcCadtyRdyvmXTXtBzobmHF4Fs31iyYz6WaTpSjQXY18Yv6dy_-O7-6RWiFXLIriokEVbuzpl8yEJkM4Lrr2s4UAn69UoG_L-gRdvDk8Rw3qoveJF8F3VcwFgF6WI-KjSzF8AbvsNcdgeV3Gtefdmjr1p6rqPvZ13nIl4iO_JP_DlkvGBrPvTaD1luYTszvHToyKxDXVigxNHSuOKwHv8k8nhVGDq2nXSw9XUCwB6jX7TE-tnyiJdyrrLqULZqb_UJaV046vSE2DyZwm7QReR7TI-JFzaGA4LxcQJujsK7Ex6KIS7H-fJ6-_aMLbpPD0kbKTIm7B6ZGbB7RH7viFL2vMFWmYPEQ8PRD1I_QQELnKZ9YiyRF1T1Y-PTvZ_7MrVtdDloSNjvAmBOU4c81wvBctPqqyY2rrNiZL-9nlnwEzOh9d0m02y_Tr_U6p8AQZYBcdfEjpK9tMtodGVKvo6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ای که هواپیمای فلای‌دبی دچار سقوط ناگهانی شد و به سرعت ارتفاعشو از دست داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72515" target="_blank">📅 15:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72514">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8d2f0129c5.mp4?token=HR0vitmMW2hVUizrJ08NkBAzCsdQy7s7myj2PyBet1KBj2loYplRkAlr0zjgk95jwdmJ3fHtBrnEXtCw-bL2Pk6gZPoYo8pP06kFZcoSq0_B7nKnzGhl-lewjd4slI7TTFkP1n009RBjdoudfgc5FIhH6MtfP78Ot2NtiNMFjk1iX3CeBE87RuGhbLEInQF0Ty6vhnaqXzvkglxgK4N0pG14_2enWUr5qrhe8nRAwz-Q4hVc8wa1X-Xwr6S2ULm3Ut81j2v7tPcKkkSmLM6qn9pqedO1HCeZONHa9r024eEOAFnP2mO-IUGUHLaNyzpdwCzrdfhAMISLW05E81ClwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8d2f0129c5.mp4?token=HR0vitmMW2hVUizrJ08NkBAzCsdQy7s7myj2PyBet1KBj2loYplRkAlr0zjgk95jwdmJ3fHtBrnEXtCw-bL2Pk6gZPoYo8pP06kFZcoSq0_B7nKnzGhl-lewjd4slI7TTFkP1n009RBjdoudfgc5FIhH6MtfP78Ot2NtiNMFjk1iX3CeBE87RuGhbLEInQF0Ty6vhnaqXzvkglxgK4N0pG14_2enWUr5qrhe8nRAwz-Q4hVc8wa1X-Xwr6S2ULm3Ut81j2v7tPcKkkSmLM6qn9pqedO1HCeZONHa9r024eEOAFnP2mO-IUGUHLaNyzpdwCzrdfhAMISLW05E81ClwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این موزیک به اسم «مفقود» در مورد مجتبی خامنه‌ای، فقط تو چند ساعت بازدیدش میلیونی شده
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72514" target="_blank">📅 14:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72513">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آی‌۲۴نیوز:ارزیابی‌های اولیه حاکی از آن است که خلبانِ عاملِ حمله با چاقو در پرواز FZ1073، تبعه عمان بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72513" target="_blank">📅 14:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72512">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2GMHutaWfkq1cNO4mliZ-ogKGQFlnoCrnryp-sUfXVRsdEURLw3K5aSqLp6PJqQhUd-Y1CofKcF6MuOAuuiZ9_RyWFxlshIQjUkriRTwiFVekFSfzwpLawe62QixJLkZSPgMkvcH6DCiT-F_7mm-JJoSIzu3HJkR0SNVwP5sTX9cdkOZpSG7PGOuPNVYCe8GVvCAs_3y-k9Y89yFNRHZJ03z7sS8JzSb-e2RE8SJlzD9kTY7S3K7dk488jR92eK_zKaea1IP3tS1MuHnC1TPfX7pD4oAiv3ZQ1UP8l3u5-Ri9EoDhQPn6mEoURkAZ-kwNLSGCUyAZKEOwQJcnVSOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدیو اول تصاویری دلهره‌آور از داخل پرواز «فلای‌دبی» از دبی به تل‌آویو که ناگهان تا ارتفاع ۱۵ هزار پایی سقوط کرد، وحشت و هراس مسافران را نشان می‌دهد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72512" target="_blank">📅 14:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72511">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af8284df28.mp4?token=jKTjbiniyRmiqcbiSSp_yuKwN5y0GvnhCZVMa53HBGOoh0TtGFvqi5s2dSPiRXd0eDDBp-eG12BPqJ35046ZVAuhK9VDo5KoFMxnvUR-2ZZ4ooPRKKFOECy3CkE6OJkULMqTSlN0yGBGu9pmwlEIg6GavxXdlWHFF7vGNNYuuxSmSUMDZq1_RcfbGBJLyP71uApuGha-S5Uwc0c3_koCsr5ttjvRmY5D0kuRXNRmMsnQ_GS5xof0bLzGhg_pmo8Zv0HTNrTO4BMCBp3LmoKNssg6dLxXf4HAdLylhliHk64FjPnINvPyT9QwQRRps-5TIkSULZ8hy_jgpu8BLy-WhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af8284df28.mp4?token=jKTjbiniyRmiqcbiSSp_yuKwN5y0GvnhCZVMa53HBGOoh0TtGFvqi5s2dSPiRXd0eDDBp-eG12BPqJ35046ZVAuhK9VDo5KoFMxnvUR-2ZZ4ooPRKKFOECy3CkE6OJkULMqTSlN0yGBGu9pmwlEIg6GavxXdlWHFF7vGNNYuuxSmSUMDZq1_RcfbGBJLyP71uApuGha-S5Uwc0c3_koCsr5ttjvRmY5D0kuRXNRmMsnQ_GS5xof0bLzGhg_pmo8Zv0HTNrTO4BMCBp3LmoKNssg6dLxXf4HAdLylhliHk64FjPnINvPyT9QwQRRps-5TIkSULZ8hy_jgpu8BLy-WhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارش‌های غیررسمی؛
علت حادثه پرواز «فلای‌دبی»، مشاجره‌ای میان خلبان و کمک‌خلبان بود که به درگیری فیزیکی و ضربات چاقو کشیده شد.
خلبان تبعه روسیه و کمک‌خلبان تبعه اوکراین بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72511" target="_blank">📅 13:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72509">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0f8e2c2fd.mp4?token=WUMoqgz62U44YpUakmO7KoTh7iSB9Ongzw7BTw0y-CZc5HWYcGfh1VAMGCW-juGLMWPQMj4-BkxLVF1SuhmSKKAqdYrysO30dkga37jGdgw-tloITmQT57ALEmgy6WMXB2Z2qaGePqLi43IrOdLi8YzQz2oiLb2goVogi5fWDp7_QsqaWa3zFLE88Ah8MsnL5T_nOBouwAoO-66pgt-T5H83BDEH6_Ur_gGSCACGbwrufrPH3SPYNoqenaSxF5pK6Nu4Pke8VO8Ak0R96W41bWB1vWYYeBTeodnfRp057lermhteMPnfymTAplRkc3e_eaARa1gW3RF3OJWf-H72dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0f8e2c2fd.mp4?token=WUMoqgz62U44YpUakmO7KoTh7iSB9Ongzw7BTw0y-CZc5HWYcGfh1VAMGCW-juGLMWPQMj4-BkxLVF1SuhmSKKAqdYrysO30dkga37jGdgw-tloITmQT57ALEmgy6WMXB2Z2qaGePqLi43IrOdLi8YzQz2oiLb2goVogi5fWDp7_QsqaWa3zFLE88Ah8MsnL5T_nOBouwAoO-66pgt-T5H83BDEH6_Ur_gGSCACGbwrufrPH3SPYNoqenaSxF5pK6Nu4Pke8VO8Ak0R96W41bWB1vWYYeBTeodnfRp057lermhteMPnfymTAplRkc3e_eaARa1gW3RF3OJWf-H72dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو اول تصاویری دلهره‌آور از داخل پرواز «فلای‌دبی» از دبی به تل‌آویو که ناگهان تا ارتفاع ۱۵ هزار پایی سقوط کرد، وحشت و هراس مسافران را نشان می‌دهد
ویدیو دوم مربوط به فرود اضطراری پرواز «فلای‌دبی» در تبوک، مسافران اسرائیلی را نشان می‌دهد که پس از فرود ایمن، سرود «اُد آوینو های» (به معنای «پدر ما همچنان زنده است»؛ سرودی یهودی درباره ایمان و بقا) را می‌خوانند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72509" target="_blank">📅 13:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72507">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/arNtL1cF0Jukp5DPaIxPvhszFu0PktDUJzihNi3KxwOmDr13iYwJGgXDAKTA3EG0YSG53ULcdG89RHvr8jbSI0vSmpbhKg9Qr8TZ2qMKWwq3DdAJj3wo_QNj-uueT0mlAMW8Cg1-LtdQ9Q7_cLuHdd8YQmp9j2LPe2RrjJIswOEXySRowwAyRxcqMErnm9vfIfoWu0ROebkGHZlRWzqMr1Ih7emLuYvffNeT-e2VkMiAQNIWGx5ZkffU3dKyNMO6xL6OBbK8HRhqgVCwasQnRyU5G6aJDtz9F-amuOl8Dxey0fqrYF2rlgAZIxOmORH3ac3JpFD5EkEFxk-ruFKLNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hsQR5wBiuECEN1Sd7ILq14CQNBJ8QGPvs3mScOj7Y_kl2SSq8XO0_UH9KKDNK_kbzhUF3DsT9-96nYXmSfKf4iajjFU38we8Kt_9JGmzPhqOBdwTuAGD2jk2dFWC37aptNTYT2C5QlMiwT-Pp4TzGi_pFKlyr0Wq5NTCuj2JnfulfIMccBSaqigVSMzlBBRiqhYR-ccR-qP1Izm9u9sHVxTGQaHXBZLZdKVcsIDdbNB_acJPNMVLBGCgrth1qyF0xMB6oJ4JLrZv5SM5RvIGFjueBO06p8Ci89AKsUw3FwHh9IvAHm8KUeyR7sRpUv1f-EzU3fyb_v0DU0104Z5UWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حادثه در پرواز فلای‌دبی؛ فرود اضطراری در عربستان
پرواز FZ1073 فلای‌دبی از دبی به مقصد تل‌آویو، امروز پس از وقوع حادثه‌ای در میانه پرواز، مسیر خود را تغییر داد و در فرودگاه تبوک عربستان سعودی به‌سلامت فرود آمد.
این هواپیما در جریان پرواز کدهای اضطراری ۷۷۰۰ و ۷۵۰۰ را ارسال کرد. کد ۷۵۰۰ نشان‌دهنده احتمال «مداخله غیرقانونی/هواپیما ربایی» است و باعث واکنش امنیتی شد.
بر اساس گزارش رویترز، یک مقام اسرائیلی گفت این هشدارها پس از درگیری فیزیکی میان دو خلبان ارسال شده است. با این حال، فلای‌دبی تاکنون تنها وقوع یک «حادثه» را تأیید کرده و جزئیات بیشتری درباره علت آن ارائه نکرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72507" target="_blank">📅 13:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72506">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4587e16a26.mp4?token=tZr4_MEJez-86LHAYOg7pVuu_8Ov8B_xsGqYwemdicmU4JLFGKjL-9vuoogvyCkMP4X_gh4A0uqcn3O-8Y7LRhWa6IhK_N4CJvxLQWFirm2ZYh3Bcu0aEn_vJcjetCLwrUYjDcIA6OG8-tUNzpqh4Gm6VgvUrqx7_vD7L-xH1F--8tNqYN9DmbzY-S5leYT5C2CoSJruYDVNPIGubzbv1mYMRyfACyeL2hlXbxN8fmBlcmH7hVfzpkzC3KcwZTwDrk2U3BpP2JutwJpQ7jJ-NcIYvRApVlavBW6U9pA82R8GGQ8ZsJx5D9mxDNnromV0Nh50548CCQdzL8qK9RARrA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4587e16a26.mp4?token=tZr4_MEJez-86LHAYOg7pVuu_8Ov8B_xsGqYwemdicmU4JLFGKjL-9vuoogvyCkMP4X_gh4A0uqcn3O-8Y7LRhWa6IhK_N4CJvxLQWFirm2ZYh3Bcu0aEn_vJcjetCLwrUYjDcIA6OG8-tUNzpqh4Gm6VgvUrqx7_vD7L-xH1F--8tNqYN9DmbzY-S5leYT5C2CoSJruYDVNPIGubzbv1mYMRyfACyeL2hlXbxN8fmBlcmH7hVfzpkzC3KcwZTwDrk2U3BpP2JutwJpQ7jJ-NcIYvRApVlavBW6U9pA82R8GGQ8ZsJx5D9mxDNnromV0Nh50548CCQdzL8qK9RARrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر ۱۸ ساله به جای اینکه امسال اول مهر بره مدرسه و درس بخونه، با یه پسر پولدار ازدواج کرد و رفت خونه بخت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72506" target="_blank">📅 12:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72505">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNBzVTQJJqvghgAWs2di-FgzIi1og51NwXzmF7YgjQpi-4pi2E_egVcAr751uaDLd2WKbJ55VuEpUpJRj01cbKbvmto3PH5GZ7Gne9wbyYZn0hj0hTudgVnJyHGuAHi8-gf4G-45EPKrOguK_Qav6wwzFbtGjeXa1hnMOvVmGC2ieSpHHIC2Io0dEUZ2iVo1ZCVWklOUH8FKYw74pjgwZ_DSmBAAhFq3sgl_ZX9fm3bydYKg_KjtskfydrJXJ7qurFCEBD8VtVgUR2nS-wvaTrQMqRnqlrzjNtDaW4BnOZI_6ZSgpfYwuUHI9eI2eZV4Qy5xTaD9DcB4plG2al_MKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده و شرکای ائتلاف پس از ۱۲ سال، با خروج نیروها و تجهیزات از پایگاه هوایی اربیل، رسماً به «عملیات عزم راسخ» (Operation Inherent Resolve) در عراق پایان دادند.
پنتاگون اعلام کرد که از این پس نیروهای عراقی مسئولیت اصلی تأمین امنیت و سرکوب بقایای داعش را بر عهده خواهند داشت، در حالی که ایالات متحده به ارائه آموزش‌های هدفمند و پشتیبانی اطلاعاتی ادامه می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72505" target="_blank">📅 11:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72504">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b10awXLfTgTNtejD8YiUmu30wYMbcdXpBq9oXgZHEfto8gcvWTPutNmSX09Lyjw8766ggu0a0Wo8YasZbvsuQ7a5oBzHMLWANEJui-TZ9ahuj9ZRFzYlny7wXqjMcWzjLZWOAZ_TtTAKQv_DjCC8PDq7SYjdhmVj5X1huvdDondSyC0mU3OgjF0ZROpHjld4vLCpjhqdRCbEIAa4x18O3rPs-SPZmoNbxiI68jlIfBA0LgcREv07VIIPYugh4yrHhCHBbNDspl5aExyagDfeqwMjkvmJhM1KCxxTCf1mSkDe6xrKW5cnzvJtfZQs2ALHrPB7ArSM0B-7PNOOoWOVNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش سی‌ان‌ان، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اطلاعات اطلاعاتی جدیدی را به شیخ محمد بن زاید، رئیس امارات متحده عربی، ارائه کرد که نشان می‌دهد ایران در برنامه هسته‌ای خود پیشرفت‌های تازه‌ای داشته است.
این اطلاعات شامل جزئیاتی درباره ساخت‌وسازهای جدید در تأسیسات «کوه پیک‌اکس» (Pickaxe Mountain) بود.
یک مقام ارشد امنیتی سعودی نیز در این نشستِ گسترده حضور داشت. گفتگوها همچنین تحولات منطقه‌ای مرتبط با حوثی‌های یمن، باب‌المندب و تنگه هرمز را در بر می‌گرفت.
نتانیاهو همچنین به حاضران گفت که ارزیابی اسرائیل حاکی از احتمال انجام یک حمله منطقه‌ای از سوی ایران در هفته‌های پیش‌رو است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72504" target="_blank">📅 11:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72503">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72503" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72503" target="_blank">📅 11:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72502">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhelK0lsO6ztHaUwDNHRFNSkckGEqKE6_smGZ2Y_FtPa3jaKp5OahQ4ZzsvhHwpn7X7Zcm_lvQ41DTqCJOy-1a1hSxx6Iy3_YLc4R0R38yDhy76WD0E9ndG1HXUK2TJ1dLPp45fwNE7o2IEOEzVVZkihbxFJJ6Nh9C3aHKMQWWU78n-FfVeU5TpF-gCCfxQS8pN3cUgx_koD6wQOfg398Va3UMAv7BAT1CVMODEoi_5XbOep2xKBky4viSFNkDtoPkd8C5bncrcUVXQ8BzJSdfffoISsI14nJ3gEPiIskAYBSJcAsxe97n3GwoXDJ-1m5mQPYEwVYVrIS1HrstuR4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72502" target="_blank">📅 11:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72501">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58cfa5fb8d.mp4?token=F_Xy7FcxLz75vKyq4UU6--HXbxNWnrZjVrRVAytrLomimfwVVgk42Bvt4xYv0rdxbdUnfvXDm5IGYEtxF0DaQKSQBYebKw8SxCKzVSy05avUlj-TZKpXGWbcJg-AtGsn54ZVGVOrEl7BKv9hK6LlHE-LHFehExQ7P6ydLo1Gvkk2e_svJJe_C6V1627-H6t7iYwuyc0Pc3h9k86SHJlhdnO5tjoJwOFZVAg7YriMJC11G7L7R66R1xFMdhHmaWbDx4cKirsayWE0tAyYVaOzBSrItybwAEjtrtuXZ-WTFhw6cSJr4pDhca5OSVroTAaqHgkA-ElRAvLR1ZmbeaFQvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58cfa5fb8d.mp4?token=F_Xy7FcxLz75vKyq4UU6--HXbxNWnrZjVrRVAytrLomimfwVVgk42Bvt4xYv0rdxbdUnfvXDm5IGYEtxF0DaQKSQBYebKw8SxCKzVSy05avUlj-TZKpXGWbcJg-AtGsn54ZVGVOrEl7BKv9hK6LlHE-LHFehExQ7P6ydLo1Gvkk2e_svJJe_C6V1627-H6t7iYwuyc0Pc3h9k86SHJlhdnO5tjoJwOFZVAg7YriMJC11G7L7R66R1xFMdhHmaWbDx4cKirsayWE0tAyYVaOzBSrItybwAEjtrtuXZ-WTFhw6cSJr4pDhca5OSVroTAaqHgkA-ElRAvLR1ZmbeaFQvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هادی چوپان:محبوبیتی بین مردم ندارم و هرشب کابوس میبینم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72501" target="_blank">📅 10:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72500">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2b6a15d8.mp4?token=EY6wEXobsSaePKt7nrtmt1JVPOF7Tav9xB-mEaLiOqZS_RS2FH3LVCtc047Lktww1NAlKCbXV8qyq01TfWlEjKl4MKhXDd8tYic0HkDUonyFfG5kOxhu1nUsYnPZztfhN5oUKptApynHtlxfekZ_dMACZ4gdsNBQ8V-9_7wEWxBC-lgQfWmX8Hn19sNgDxM47lDmGHyIcfM0Sgp-Cjdb79-th7hKmaab1QCydnLvPM3qfUkA-pTHO2blvKEUkjyq8JqVfyGqmah96HrluetIA1AZzfdK8RD972SOKAZVVZUXLHpJU_CxGzlzzbxYYE703Bg3LryetSUkxHPnILoqNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2b6a15d8.mp4?token=EY6wEXobsSaePKt7nrtmt1JVPOF7Tav9xB-mEaLiOqZS_RS2FH3LVCtc047Lktww1NAlKCbXV8qyq01TfWlEjKl4MKhXDd8tYic0HkDUonyFfG5kOxhu1nUsYnPZztfhN5oUKptApynHtlxfekZ_dMACZ4gdsNBQ8V-9_7wEWxBC-lgQfWmX8Hn19sNgDxM47lDmGHyIcfM0Sgp-Cjdb79-th7hKmaab1QCydnLvPM3qfUkA-pTHO2blvKEUkjyq8JqVfyGqmah96HrluetIA1AZzfdK8RD972SOKAZVVZUXLHpJU_CxGzlzzbxYYE703Bg3LryetSUkxHPnILoqNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی یکی از مراسم‌های عروسی در ایران، عروس یه دفعه تفنگ رو برداشت و این شکلی پشت هم شلیک می‌کرد!
از نگاه‌های داماد معلومه ریده به خودش ولی کمکی از دست کسی برنمیاد
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72500" target="_blank">📅 10:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72499">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cc8901fca1.mp4?token=RAnMdUqye8xpluMoP-3mL5_Bw3cXjEB5OUCyRrf0bHE_tGaBUMbpOGa1OUH8td82HPdf9IzedCb3S3qo7RHGi0xYD-lN-K8I8BP4f1RK0iynvgUZ5eq4FwDNAAE5SUWPsnLY55MSciYiXe2oDqmmDg4Wx3a166q0bzV8IJ3CbqWJL21SCU7uKbqLDLjLGd-AYZSKo6d9L1QaTBOD8WOVeyy3V73i7-WNUF3bkAaSt6BooDJWc4BHkA2mBlD7sHkOHLC_LewR76n1O04xFsy1JDLMW7lt3K5JTgRXI4GaBbn55gFeenrsfEGrwA0RdILES65AQbv6KP27A8M96vU6sg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cc8901fca1.mp4?token=RAnMdUqye8xpluMoP-3mL5_Bw3cXjEB5OUCyRrf0bHE_tGaBUMbpOGa1OUH8td82HPdf9IzedCb3S3qo7RHGi0xYD-lN-K8I8BP4f1RK0iynvgUZ5eq4FwDNAAE5SUWPsnLY55MSciYiXe2oDqmmDg4Wx3a166q0bzV8IJ3CbqWJL21SCU7uKbqLDLjLGd-AYZSKo6d9L1QaTBOD8WOVeyy3V73i7-WNUF3bkAaSt6BooDJWc4BHkA2mBlD7sHkOHLC_LewR76n1O04xFsy1JDLMW7lt3K5JTgRXI4GaBbn55gFeenrsfEGrwA0RdILES65AQbv6KP27A8M96vU6sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این فیلمی از رینگ کشتی کج نیست! یه دعوای سنگین تو فوتبال پایه مملکته بخاطر یه تکل ساده‌اس!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72499" target="_blank">📅 09:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72498">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324e32bd1.mp4?token=AjHJDpaDYJ5BCCrntd2AKv8AhmHbRQW_6TBmsRbmP0-Q-R1OMeYA-GotRdwMllmV1vIvlWnsVlZCnP400pRopI-CiWwvLEP39uMusf7M2h7qkkdQWkUAc0SA063lHq4VuhztSJGIX9jyyVaTHm4BoZj4BdB_oyQ9xMnABz3mXvDAidvusJXfNOTvHOJlMQm8UFQ6-hXxU9ix5h_giek8P0vQrWcUqVHGihZggOuFQz3IprawJVUXNSs1W96Yn0Ci4o6vZHHD3XJDKou-Si24YyDbqxEPr1c8lUbv3vth_WUKLrZKkdA6BBcNT_eWZLwtjejQRj7OOU9PtZ6cs1RMWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324e32bd1.mp4?token=AjHJDpaDYJ5BCCrntd2AKv8AhmHbRQW_6TBmsRbmP0-Q-R1OMeYA-GotRdwMllmV1vIvlWnsVlZCnP400pRopI-CiWwvLEP39uMusf7M2h7qkkdQWkUAc0SA063lHq4VuhztSJGIX9jyyVaTHm4BoZj4BdB_oyQ9xMnABz3mXvDAidvusJXfNOTvHOJlMQm8UFQ6-hXxU9ix5h_giek8P0vQrWcUqVHGihZggOuFQz3IprawJVUXNSs1W96Yn0Ci4o6vZHHD3XJDKou-Si24YyDbqxEPr1c8lUbv3vth_WUKLrZKkdA6BBcNT_eWZLwtjejQRj7OOU9PtZ6cs1RMWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره روحانی از ملاقات رئیس‌جمهور سوئیس با علی خامنه‌ای:
رئیس‌جمهور سوئیس به آقا گفت ما ۱۵۰ سال قبل کشور فقیری بودیم، اما دو تصمیم گرفتیم؛ دانشگاه‌های خوب ایجاد کنیم و با کشورهای دنیا روابط خوبی داشته باشیم. سوئیسی که امروز می‌بینید حاصل آن دو تصمیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72498" target="_blank">📅 09:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72497">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsNPz06DqJBv4R2nm7ydkdAvEz3ILH-3v4T1WIO3FbrTWBuZPezNC3Trb58QOdn1UlHFC8oJrPf72fX1JPYq4v13ZVx38VOwBQ3nGoj6Dp31NyokppfURPgLF1a0GcemHLuBCozN_OS9BcVX4D6t2YBqdB5l2IztTR4OlXc98pqq2ZS6t8C6RsUHq1oFoTGCn6Ob_wLmqqOtlyFnA1F_g3Ldn6brYGiz0NTChkazcRl_E9VP_Yp8eri2phzAA1uC5H-ItpaJ8fBdhLycgqxSGoIa8dJ-NFIKZk83I-mtVZeGo2fo5Gjpa5QXjOlPHW9v1GOqggJvUNvSejaJQIjSuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووری
؛مذاکرات به بن‌بست رسیده،ایران میگه اگه آمریکا به تفاهم‌نامه اسلام‌آباد برگرده حاضره امتیاز هسته‌ای بده و آمریکا هم میگه حالا که دست بالا رو دارم پس کیر تو تفاهم‌نامه اسلام‌آباد و کوتاه نمیام.احتمال شروع درگیری‌ها بالاست.
اکسیوس؛
تلاش‌های قطر برای میانجی‌گری جهت دستیابی به توافقی جدید میان آمریکا و ایران پیشرفت اندکی داشته است؛ چرا که مذاکرات بر سر دو موضوع — یعنی درخواست ایران برای رفع محاصره دریایی توسط آمریکا و مطالبه واشنگتن برای دریافت امتیازات هسته‌ای — دچار بن‌بست شده است.
ایران تأکید دارد که تنها پس از بازگشت آمریکا به تفاهم‌نامه ماه ژوئن، حاضر به بررسی اعطای امتیازات هسته‌ای خواهد بود؛ در حالی که واشنگتن دلیلی برای کوتاه آمدن و مصالحه نمی‌بیند.
قطر، پاکستان و مصر همچنان دارن خایه‌مالی میکنن و تلاش میکنن که توافقی صورت بگیره.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/72497" target="_blank">📅 06:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72496">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/72496" target="_blank">📅 00:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72495">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72495" target="_blank">📅 00:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72494">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56db93255e.mp4?token=WV2SmULCiXWiD8Wim-0tL_Tfp7-k-846LMKwGqWlMNGIaNhemHXtxxYNtkGMtYn-PS_FaK6fjdoPdl5K5RibpeSDvsAc0VHe6rvpTJRGoyKQo9w6kbeJR_czi9Yymdt69bwKvhgcm49k3ARCl6aKaTj_291qsjNEYRCOZu1AmzTcAwDVS3AU7gN80_Yg_C_lCYWg9EtxVRjS63JjGAfAYjt3LDEXlgcs4bZbekN0WyLrqgxBJC7Fe3nxSFc3K5AITZTx_Qx9ut32fphBBvVu1jnHtEB077IrnZ668lfyxk6wEOaf0KK8pknCjdvjMo2kiyJyhni0mhCeO2ALqntnxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56db93255e.mp4?token=WV2SmULCiXWiD8Wim-0tL_Tfp7-k-846LMKwGqWlMNGIaNhemHXtxxYNtkGMtYn-PS_FaK6fjdoPdl5K5RibpeSDvsAc0VHe6rvpTJRGoyKQo9w6kbeJR_czi9Yymdt69bwKvhgcm49k3ARCl6aKaTj_291qsjNEYRCOZu1AmzTcAwDVS3AU7gN80_Yg_C_lCYWg9EtxVRjS63JjGAfAYjt3LDEXlgcs4bZbekN0WyLrqgxBJC7Fe3nxSFc3K5AITZTx_Qx9ut32fphBBvVu1jnHtEB077IrnZ668lfyxk6wEOaf0KK8pknCjdvjMo2kiyJyhni0mhCeO2ALqntnxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو نپال بر اثر رانش زمین، این کوه با این عظمت به طرز ترسناکی مثل آب، نصفش تو رودخونه سقوط کرد :
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/72494" target="_blank">📅 23:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72493">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299316a1b0.mp4?token=KAxgK-b464Lye4t7dtvQmaQK6YvMNyt7-81b40qnEIS8neoAKeFex7qjfFVaX6aZMcpCWKvdgoQcKURhLhE9yrJzdzhoGXmIjU7pqCjhmvL229ad9fxG0duCJNlHiTh1gU_5jRJVqP6UkbhSc2VbcDx2Bq3Af26QW5WiHVJYbx7O9200JlTLZN6bqWiXzZ-HhvOwaNGiRPpJZQBvf8hBQNk28lPDDonHmKEdd9t89Xo8hpnHo44myFobfRHVGKLs2dgeaHqDDDTJBl2SFDjiPsQPa__FsXMZiWov4hNtRrxFrksahdCKDg0AqcHD1Ofqm9yrTRLnGdyEBJFCkN1onY6m9ZrH6PVqONBDXhOq8FAY6powb1Vo2A0cIUyFtkRWRnM_IOPgTFq_yDFlH-08i4JcpUT26JWgek5qivBCtTCZNa98q0dt-lFFMVqIt2v6lqnX6W-zztkbHF_YAIqvBA9Dd4GziOQKYjfwabnPXsqp0gEndtFjvUThEVd4EiPIB-Ll2O31fa0Fo6Fcvnce72jpuv6UOCDswCApVYj7LFXorEgbEHa9-r3j66XOb0YHnmxrhkXigcipE0GZ7XpJhgTmknuuiW3nHF0pxvXpKtvB3SFKWUL1hzqV7VP3qU2tXuylIyy4_kYT5ClDDSx2sqPAGXCgbEyGDZG6mskAQRI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299316a1b0.mp4?token=KAxgK-b464Lye4t7dtvQmaQK6YvMNyt7-81b40qnEIS8neoAKeFex7qjfFVaX6aZMcpCWKvdgoQcKURhLhE9yrJzdzhoGXmIjU7pqCjhmvL229ad9fxG0duCJNlHiTh1gU_5jRJVqP6UkbhSc2VbcDx2Bq3Af26QW5WiHVJYbx7O9200JlTLZN6bqWiXzZ-HhvOwaNGiRPpJZQBvf8hBQNk28lPDDonHmKEdd9t89Xo8hpnHo44myFobfRHVGKLs2dgeaHqDDDTJBl2SFDjiPsQPa__FsXMZiWov4hNtRrxFrksahdCKDg0AqcHD1Ofqm9yrTRLnGdyEBJFCkN1onY6m9ZrH6PVqONBDXhOq8FAY6powb1Vo2A0cIUyFtkRWRnM_IOPgTFq_yDFlH-08i4JcpUT26JWgek5qivBCtTCZNa98q0dt-lFFMVqIt2v6lqnX6W-zztkbHF_YAIqvBA9Dd4GziOQKYjfwabnPXsqp0gEndtFjvUThEVd4EiPIB-Ll2O31fa0Fo6Fcvnce72jpuv6UOCDswCApVYj7LFXorEgbEHa9-r3j66XOb0YHnmxrhkXigcipE0GZ7XpJhgTmknuuiW3nHF0pxvXpKtvB3SFKWUL1hzqV7VP3qU2tXuylIyy4_kYT5ClDDSx2sqPAGXCgbEyGDZG6mskAQRI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش:
اگر بانوی ایرانی یک سرباز آمریکایی رو اسیر بگیره بهش ده میلیارد تومان پاداش میدیم.
مردم کشور های منطقه هم اگه یه سرباز آمریکایی رو اسیر بگیرن و بدن تحویل به اونا هم پاداش میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/72493" target="_blank">📅 22:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72492">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دلار ۲۵۰ تومن
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/72492" target="_blank">📅 21:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72491">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzO7iNH8OsTVkMEkgyyHwdv_-hFAbibaeDwugNERrkZyEN3vg5m2NNA5t-kyFRSeK83prVfIdXy61sdgOQqsIgglAVKBkmvyvVR6oH_6SFGc4e9HlD4IjNEpPWKNlEiLs3Q7Kfy5RtGIIEZG4RgX5aSOsPMpVvCwz9_Bi9UCrRhQPSoioN25eDlbLPvpOmkIL-JTCXIB_BTyBGaI_KoLhs340jmriAfziT_Je0piDi9ay5eTQckDWtMTUvm6x6BbErJ6y5OTovKY8R-ew_LAOWi-hD2V4zrBfWoVzgESktnkh2FPuCx9Eo7Pfa49QC0CXp_hEInLUpe-utAhmnzP5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا ۱۰ فرد و نهاد را در ایران، چین، هنگ‌کنگ، پاکستان، عربستان سعودی و ترکیه به اتهام حمایت از تدارکات نظامی ایران در چارچوب «عملیات طرد اقتصادی» (Operation Economic Outcast) تحریم کرد.
به گفته وزارت خزانه‌داری، این شبکه‌ها برای «وزارت دفاع و پشتیبانی نیروهای مسلح ایران» (MODAFL)، تسلیحات، تجهیزات الکترونیکی و قطعات با کاربرد دوگانه تأمین می‌کردند که در برنامه‌های موشک‌های بالستیک، پهپادها و هواپیماهای نظامی مورد استفاده قرار می‌گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/72491" target="_blank">📅 21:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72490">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcsoGJ_tEzCpl6uXCPXcPnov3n_jWQRcQG0qqh6sn8zp4URDqMPu5HUdSBi5y75GG7zsbYLCm9nuXw37vhNZOa2pYLlo-IclSpdpopEYTqJyv6F6rPX6NTOAfuGylVX0cb__qg1sQVE7vlZZFNNQ8hGu94u8dgBSW200dNEuYjl615AS4HD5a2VXBa1s64FvuBs-0f7p__p0Fwdk21XgJlfbbhw9VD8s99G2QFzruxNO5YuDGfZpaOhvKkwirsXAyMdGIcp-2QBLVApa16i7a0aU3XnYeBvx6Ie8BCJeWJ9axvs_KvNoAlniPngGzOUC-6Yz2wqjj620j6TKXjhNLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آی۲۴نیوز:
یک مقام اطلاعاتی آمریکا به شبکه «آی۲۴نیوز» (i24NEWS) گفت که ترامپ با ارزیابی نتانیاهو هم‌نظر است؛ مبنی بر اینکه ایران یا متحدانش ممکن است پیش از انتخابات به اسرائیل حمله کنند.
کابینه امنیتی اسرائیل امشب تشکیل جلسه می‌دهد و نتانیاهو نیز «یائیر لاپید»، رهبر اپوزیسیون را برای ارائه گزارش امنیتی فراخوانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72490" target="_blank">📅 21:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72489">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f526b16f27.mp4?token=Lb78GKzHdCNcyp38c8KeamYBNzOxafNAIYFYSSFnv8s5hCXrfFr_8TQpwOmhTmxO9YM0iJVLPmCkq1pow9ilMhlNKq7S2QWvAPhRmNP1PE5YQMjUE04dq5DmU_elrI445BjHZccHCGFhZ6YuyBqMb8LRtUmbkbh9xVtasOjGqn_fX5_zy3TqTSCpT4Vp4YNKwhcvq_io27iOsQQTTyEM4oE4nNrc693znPk67yJt67Hjd04wh51dmvGT1bDS0FaDt86-KxwElkvQWP9FDByx3Zq0wcywP_lJzTBqChox8IGaqgNL-4YKPR7uf9KMmaLauVXiJXFxWso0ih5iTAnQ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f526b16f27.mp4?token=Lb78GKzHdCNcyp38c8KeamYBNzOxafNAIYFYSSFnv8s5hCXrfFr_8TQpwOmhTmxO9YM0iJVLPmCkq1pow9ilMhlNKq7S2QWvAPhRmNP1PE5YQMjUE04dq5DmU_elrI445BjHZccHCGFhZ6YuyBqMb8LRtUmbkbh9xVtasOjGqn_fX5_zy3TqTSCpT4Vp4YNKwhcvq_io27iOsQQTTyEM4oE4nNrc693znPk67yJt67Hjd04wh51dmvGT1bDS0FaDt86-KxwElkvQWP9FDByx3Zq0wcywP_lJzTBqChox8IGaqgNL-4YKPR7uf9KMmaLauVXiJXFxWso0ih5iTAnQ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از فضای معنوی مدارس مملکت و دانش‌آموزان نمونه و پرتلاشش:
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72489" target="_blank">📅 21:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72485">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8f5d17f2e5.mp4?token=W2FqABRZ2vzF_jPEVLbQIjo9q1_0o-YczkXobw_rdpIUFqWzbBQzm0ufmzBh1A9DIquOdkyC9P9WLtxRbDppwcaSjTl2jJy4hbQzIImeDjb3ZJjvBEnT86doNxxeOgNqt0DBe_MHGJZ05I41l9j2tjIVBU1IPJRPPCx9YWe3TY9x-DKWVHCo-LqUCUutu2rPo_Oh_HEP73xn3Fu2a4NabdZuDnBYtera4xBPcFk4yPZSTuGpvBmm073rLGfpBNHl1GYWAL2s6RIpnhE6XcV9or-AI8oGoSbIg925glmhiKTHJC30Rxqo0RcSgDWzPrmvFzlZpObmV1h9u1oSxb6hRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8f5d17f2e5.mp4?token=W2FqABRZ2vzF_jPEVLbQIjo9q1_0o-YczkXobw_rdpIUFqWzbBQzm0ufmzBh1A9DIquOdkyC9P9WLtxRbDppwcaSjTl2jJy4hbQzIImeDjb3ZJjvBEnT86doNxxeOgNqt0DBe_MHGJZ05I41l9j2tjIVBU1IPJRPPCx9YWe3TY9x-DKWVHCo-LqUCUutu2rPo_Oh_HEP73xn3Fu2a4NabdZuDnBYtera4xBPcFk4yPZSTuGpvBmm073rLGfpBNHl1GYWAL2s6RIpnhE6XcV9or-AI8oGoSbIg925glmhiKTHJC30Rxqo0RcSgDWzPrmvFzlZpObmV1h9u1oSxb6hRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج استعفا در ایران طی ۷۲ ساعت اخیر!
طی چند روز اخیر، یکی از شدیدترین موج استعفای تاریخ ایران اتفاق افتاده و پرستاران، معلمان و کارمندان به علت حقوق بسیار پایین، از کارشون استعفا دادن!
به قدری این موج استفعا شدید بوده که خیلی از بیمارستان‌ها خالی از کادر درمان شده!
خیلی از کلاس‌های درس هم دیگه معلمی برای آموزش وجود نداره و صدها نفر استعفا دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/72485" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72482">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f441db6e.mp4?token=iNAyYBCuqP8cPW9ZnwBCe4G1wmCqxhjNXeadg5HSCtk12iZeHSk7KsSODfgr0BHtoLLyWGgL2xKz17kzkVZwke-Z9cvBokgmWDhwYs3yZJB2cddFsjGT7KK8Y9NZDMzkNiKNTCGjZoBV0qZZmwEhgFnH93TJyPxS51uwgoBeVH17FbgfK6TBfW3GghqyL4Y9IkqR4yMzTCcmMGl3psxuCeIrdgq71YPVtf2BAkFX6nEKMeUXRq-zdhsdX-PtYb0mo8h3Cf8AUrWR6oksO-pcxUcFLTSqCZnvJOWJOUKpcsW7jU-OaZoN2j36oTb6skMhgxerIgl2wcAn1Ojs1Hs7qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f441db6e.mp4?token=iNAyYBCuqP8cPW9ZnwBCe4G1wmCqxhjNXeadg5HSCtk12iZeHSk7KsSODfgr0BHtoLLyWGgL2xKz17kzkVZwke-Z9cvBokgmWDhwYs3yZJB2cddFsjGT7KK8Y9NZDMzkNiKNTCGjZoBV0qZZmwEhgFnH93TJyPxS51uwgoBeVH17FbgfK6TBfW3GghqyL4Y9IkqR4yMzTCcmMGl3psxuCeIrdgq71YPVtf2BAkFX6nEKMeUXRq-zdhsdX-PtYb0mo8h3Cf8AUrWR6oksO-pcxUcFLTSqCZnvJOWJOUKpcsW7jU-OaZoN2j36oTb6skMhgxerIgl2wcAn1Ojs1Hs7qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه حال‌وش:درگیری شدید بین نیروهای نظامی و افراد مسلح در ایرانشهر
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72482" target="_blank">📅 19:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72481">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/488280f6be.mp4?token=ivjFNLc5XVJXjmBaCv5ZAmKkL16l36_V4BJgBJAy22WlNCn7FiuIhy314soAZ8CKQjrEHHXdwpYIMiKHxzScB9dc0kwZt4ed2fjT9yfs1gwTwOTuzbvdZHFl7VGVCezVESQe5QSXw8nECl-hoK2wS22d3sXxpx06z-HFUa7vUTZSwR14MMhN-8bktYTYe5OdoQcqKZvn9gqjDOTZSrO_UZa1pqNKXyzEwO1dEhmmq5nzgan3BqRhOzxAmH4ULsGbUBhCiyjFhhVOLGmBSh3Pya-xEq-I2M70w6NIBc4Dy4lJ-u-mRi7o70AJHzlslRCO2m8QzMTw0l79xkVW8E50dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/488280f6be.mp4?token=ivjFNLc5XVJXjmBaCv5ZAmKkL16l36_V4BJgBJAy22WlNCn7FiuIhy314soAZ8CKQjrEHHXdwpYIMiKHxzScB9dc0kwZt4ed2fjT9yfs1gwTwOTuzbvdZHFl7VGVCezVESQe5QSXw8nECl-hoK2wS22d3sXxpx06z-HFUa7vUTZSwR14MMhN-8bktYTYe5OdoQcqKZvn9gqjDOTZSrO_UZa1pqNKXyzEwO1dEhmmq5nzgan3BqRhOzxAmH4ULsGbUBhCiyjFhhVOLGmBSh3Pya-xEq-I2M70w6NIBc4Dy4lJ-u-mRi7o70AJHzlslRCO2m8QzMTw0l79xkVW8E50dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور، درباره مجتبی خامنه‌ای:
ما تصور می‌کنیم که او زنده است. البته دقیق نمی‌دانم؛ هرگز او را ندیده‌ام.
اما بهترین شواهدی که در اختیار داریم، حاکی از آن است که او زنده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72481" target="_blank">📅 19:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72480">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKZ3mmdnmCdJtWWLulIBLeLj6DhLOgj6qjxtbn_Qw2Vph5aFIniEEDPohcMkdPWzvOQx_qnbOEjuunV2W6h9x54QDjDP6YEwvTORmQDvoPLDF4OCM4Xet5UVAdUL9F77QeZfgW_7XTcvbGNZTyvWNxXCs9uRoVlyGhO2i9K3APTH0psn4RPaV7_XMRavz4gGY4QhrVQkN9GP1d6nbbBXRNXC1TDKU4wWjoHAu91ynWukxBQFRF5PGfZfZU8mRGNH8ofpPoXU7C9PJsoalmnsJar3QSC5x45Qyh2IM9gQ6eZQthwPo7Eo3CQGikLRw4-F29j0rtxcinfHal5QwbMp1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی از اصفهان؛هر لیتر بنزین سوپر۱۴۰.۰۰۰تومان!
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72480" target="_blank">📅 19:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72479">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72479" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72479" target="_blank">📅 19:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72478">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrIxmRtsQxvLbjrpqj1YRoSy5vZGGYGk3pk33q481c-irzK8bpYc0wENwi-zgiMmlHmCuQHVYsnEB-7gVuNmvhVTTicqqS5JaYMkpREBH2nzzLIW_d_bSvZZOpA6lE07GgkevnSJuWK0nPX0-NOegMyrPRhi8wWrL-NrtHbfFn02tyEizKlxUiN4Rrn7vifd0uMqYdNnAD7VXcssc4alxoaHeXdNyrZzCC03LayRQYfqaUo55VYaBekkS6GEs6N3i3cFna3NEkeirLlXfMPjsTaYuwiSZO9rAyiJytonPTscoHDI2L0j5qq6hCjnBG76VzoDjlOlpoAl3KCmYlABrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72478" target="_blank">📅 19:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72477">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مذاکرات ایران و آمریکا بدجور گره خورده، آمریکا به دنبال اینه که مستقیماً بره سراغ مسائل هسته‌ای، ولی ایران همچنان رو تنگه گیر کرده، این در حالیه که آمریکا می‌گه تنگه بازه و ما مذاکراتی در مورد تنگه و رفع محاصره انجام نمی‌دیم  بنظرم یه دور جنگ و ترور رو در…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72477" target="_blank">📅 18:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72476">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">معمولاً تو اسرائیل وقتی نخست وزیرِ وقت بخواد تصمیم مهمی بگیره، رهبرِ حزب مخالفش رو هم به یک جلسه امنیتی دعوت می‌کنه، و امروز نتانیاهو از لاپید، رهبر اپوزیسیونِ حزب خودش دعوت کرده به جلسه بیاد؛ احتمالاً این جلسه امنیتی در مورد ایرانه #hjAly</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72476" target="_blank">📅 18:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72475">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">معمولاً تو اسرائیل وقتی نخست وزیرِ وقت بخواد تصمیم مهمی بگیره، رهبرِ حزب مخالفش رو هم به یک جلسه امنیتی دعوت می‌کنه، و امروز نتانیاهو از لاپید، رهبر اپوزیسیونِ حزب خودش دعوت کرده به جلسه بیاد؛ احتمالاً این جلسه امنیتی در مورد ایرانه
#hjAly</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72475" target="_blank">📅 18:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72474">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ برای بار هزارم:
ایران به سلاح هسته‌ای دست نخواهد یافت و آن‌ها در وضعیت بسیار بسیار بدی قرار دارند و به‌شدت در حال شکست خوردن هستند. این ماجرا خیلی زود به پایان خواهد رسید.
این وضعیت خیلی خیلی زود تمام خواهد شد. آن‌ها سلاح هسته‌ای نخواهند داشت.
قیمت نفت درست همان‌طور که قبلاً بود، به‌شدت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72474" target="_blank">📅 18:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72473">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره ایران:
در سال‌های پیشِ رو، وقتی تاریخ کشورمان را می‌نویسند، خواهند گفت که ماجرای ایران یکی از مهم‌ترین کارهایی بود که ما انجام دادیم.
در واقع، این یکی از مهم‌ترین کارهایی است که ما انجام داده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72473" target="_blank">📅 18:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72472">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ: «اخبار جعلی» را فراموش کنید. حالا می‌خواهم آن‌ها را «اخبار مصنوعی» بنامم. از این عنوان خوشم می‌آید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72472" target="_blank">📅 18:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72471">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoTc_JSKz_Rp7ClownGBTi78JzoxqAMjJB-a__6QLoKudn-vTWmf0Gzt8Q_ALv1UKFkIWdnQmDq9-njbnYDiyKSjwAtGEPTKFm9uamv2sy1cb5lt8MBwCj-7AlFqVDjhyyHmuyOplq6nqyXoh9MU6uhny4F1yvTPXcs5Y3CkzygMU2l0gT2lriMl9edxdvFvv5bhgMcLgGekWQ0wA2SJW_bdpwmhU_qvh6oJQYQTrIIdn4dA2_wBCR8erDVJKIshSg9Tc1SMFpkQWF3VZKR2ZjLy0liMMjko5yp_O5k5tqojeqtOMqSNihPszEsA-Blip30ef_kzc-Ytuf4K0MIQQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا در حال اعزام ۶فروند جنگنده اف-۱۶ به خاورمیانه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72471" target="_blank">📅 17:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72469">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89765f99e7.mp4?token=AFwR7S62gMGVpwTR5JV7xxbXUanKG3W3PoAseJ10Z7HLV_G2xn25sgn2ykRLOk-aHTcMSCVo6ncPMK_0MLERiffZKsE47KtbRt67kZxdaEMdRrdw8lYHM3nL2W-UUyWE_F7uB4rgisSO-ESQHfCTofOPjRZjIkvq_1wQ0UoDjFfpShf-NVmCMkvvwJn9FasoNyCYIYms2xm0XuwLAIVOfvSauLepSkTP2wSazQTFiQiGPr_8WqURzBrg3Dsh57DPwJJGSfG1vkRaAc9dWZRi0usVXN0aUOuNpQgq3H78MGqTzFnY_4u-138j5Ccrb6LUx8oxDQD3UL4nINOWMMCRfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89765f99e7.mp4?token=AFwR7S62gMGVpwTR5JV7xxbXUanKG3W3PoAseJ10Z7HLV_G2xn25sgn2ykRLOk-aHTcMSCVo6ncPMK_0MLERiffZKsE47KtbRt67kZxdaEMdRrdw8lYHM3nL2W-UUyWE_F7uB4rgisSO-ESQHfCTofOPjRZjIkvq_1wQ0UoDjFfpShf-NVmCMkvvwJn9FasoNyCYIYms2xm0XuwLAIVOfvSauLepSkTP2wSazQTFiQiGPr_8WqURzBrg3Dsh57DPwJJGSfG1vkRaAc9dWZRi0usVXN0aUOuNpQgq3H78MGqTzFnY_4u-138j5Ccrb6LUx8oxDQD3UL4nINOWMMCRfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارش‌های غیررسمی میلی گلد دفتر رسمیش رو جمع کرده و دیگه پاسخگوی ملت نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72469" target="_blank">📅 17:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72468">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3194b055f.mp4?token=gPAbs9G1LSE1fO9O1KOEZ4KCtpYXkimCDawhMrHONe64qXDRV_udGB1tp3CY7ew-cz5loJfH5I4FXYPoM4XI3Jr67qhqBZ1M_MW4BI-1OR086hOHvhKz36R7kvi8HHK7aAs3YTfXudDPkiIYPIycf3UPuQe-kjDtG_DdHtdTrcaOz_hxfV1rwJ4AsRrX4iUFUj-c7aM3xw9DTjsElXe4pTMVumOaTnsi3xg56-RXm3_vgqPRDAqGHmT0_RuSSGxyiWBHHG2rM40bn5eFd9JDVSJFvntbWn4JBFijA0W8MaceYObqx2nrraY883VWjY4s7fSINRBRN9IRYCmR3IJFoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3194b055f.mp4?token=gPAbs9G1LSE1fO9O1KOEZ4KCtpYXkimCDawhMrHONe64qXDRV_udGB1tp3CY7ew-cz5loJfH5I4FXYPoM4XI3Jr67qhqBZ1M_MW4BI-1OR086hOHvhKz36R7kvi8HHK7aAs3YTfXudDPkiIYPIycf3UPuQe-kjDtG_DdHtdTrcaOz_hxfV1rwJ4AsRrX4iUFUj-c7aM3xw9DTjsElXe4pTMVumOaTnsi3xg56-RXm3_vgqPRDAqGHmT0_RuSSGxyiWBHHG2rM40bn5eFd9JDVSJFvntbWn4JBFijA0W8MaceYObqx2nrraY883VWjY4s7fSINRBRN9IRYCmR3IJFoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری فیزیکی مسافرین در یکی از هواپیماهای کشور:
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72468" target="_blank">📅 16:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72467">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کانال ۱۴ اسرائیل:
نشست نتانیاهو در ابوظبی گسترش یافت و نمایندگان ۱۰ کشور را در بر گرفت:
امارات متحده عربی، اسرائیل، عربستان سعودی، ایالات متحده، مراکش، کویت، بحرین، لیبی (حفتر)، عمان و مصر.
ابتدا دیدار دوجانبه میان نتانیاهو و «محمد بن زاید» (MBZ) برگزار شد و سپس سایر مقامات به آن پیوستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72467" target="_blank">📅 16:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72466">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f4e41635.mp4?token=VD-b4luEgJ-GnrFAybUfyxW7klb_tk3eyt16CZ3Ep3ymEljcvaZrrdmXIGGN1tTbSX765YzMDlomJxqw9q3ppoe7g3cH9gWIS-WYI8z3ffH--IMZ0ZC0qpNDrfMMZWZ0YPMX0j7HcagSPbmAe_LD5gC3j1FnIpnbGrnGapoyaXKXhk7bsDRonqN-LYJti9aparEf8NNlx9h5ArGOLQlLCXwXAcnKWwkQRj6fgYVofoJVBGdaP5N4SK8hgPfRNBmzvOdSAZzuwWtr9S--RtVZWUcxR8153n11ojUKK3e-UTYUh5QFrdHlr4PMrwC4B-PF5Stl6hCHLe71AaB5Q_9NFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f4e41635.mp4?token=VD-b4luEgJ-GnrFAybUfyxW7klb_tk3eyt16CZ3Ep3ymEljcvaZrrdmXIGGN1tTbSX765YzMDlomJxqw9q3ppoe7g3cH9gWIS-WYI8z3ffH--IMZ0ZC0qpNDrfMMZWZ0YPMX0j7HcagSPbmAe_LD5gC3j1FnIpnbGrnGapoyaXKXhk7bsDRonqN-LYJti9aparEf8NNlx9h5ArGOLQlLCXwXAcnKWwkQRj6fgYVofoJVBGdaP5N4SK8hgPfRNBmzvOdSAZzuwWtr9S--RtVZWUcxR8153n11ojUKK3e-UTYUh5QFrdHlr4PMrwC4B-PF5Stl6hCHLe71AaB5Q_9NFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده امارات در سازمان ملل:
جزایر تنب بزرگ، تنب کوچک و ابوموسی در خلیج فارس، جزایری متعلق به امارات متحده عربی هستند که تحت اشغال ایران قرار دارند.
ما تداوم اشغال این سه جزیره توسط ایران را به‌طور کامل رد می‌کنیم.
هرگونه تلاشی برای جلوه دادن این موضوع به عنوان یک مسئله داخلی ایران، تغییری در این واقعیت ایجاد نمی‌کند که این‌ها سرزمین‌های اشغال‌شده هستند و نباید تحت حاکمیت ایران باشند.
+کص ننت:)
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72466" target="_blank">📅 16:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72465">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8551b8a147.mp4?token=fgCKgsnU8KZNIqwDGRfYwSOQpOdrLBb8peAYre-5GrYmzMlTdKQlghsibM0rfxizh6VGziN70EMbCE5dc3o7PHLNuyBLGUbDjwoQQzmUCKB2rttt56kfHQAq0B9sJspxIEIL7VzRHItlwWj6y5LLkZlHc1ExfphdYu9MGySJunsHg80VuCxTPTHPtJJ7MlQSfw5SQeh0U4TXm_YJthswTfW_uqMH4QQ9IaMFlRyyvevfv6ptfgCos4PJ0-x7zE53E6sqHsMhv1O9Vd1dyy8SYMbI-VlghnNLgYGk-UtaPeOucvxofCHyawzD8e7KRDFS774o19Wgxb6c7DjTxtH8Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8551b8a147.mp4?token=fgCKgsnU8KZNIqwDGRfYwSOQpOdrLBb8peAYre-5GrYmzMlTdKQlghsibM0rfxizh6VGziN70EMbCE5dc3o7PHLNuyBLGUbDjwoQQzmUCKB2rttt56kfHQAq0B9sJspxIEIL7VzRHItlwWj6y5LLkZlHc1ExfphdYu9MGySJunsHg80VuCxTPTHPtJJ7MlQSfw5SQeh0U4TXm_YJthswTfW_uqMH4QQ9IaMFlRyyvevfv6ptfgCos4PJ0-x7zE53E6sqHsMhv1O9Vd1dyy8SYMbI-VlghnNLgYGk-UtaPeOucvxofCHyawzD8e7KRDFS774o19Wgxb6c7DjTxtH8Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور نیروهای رژیم در یکی از هنرستان‌های دخترانه شهر اندیشه برای تشییع نمادین علی خامنه‌ای!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72465" target="_blank">📅 16:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72464">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fb8d0412d.mp4?token=rPyQvL7tqa0EUHAJ_dof1J-kM6DmcFAljXn3mPUJ8vYMDeRL6RkvyEYvvcz0cHOGUUbhf3y561i9dNSDDFECFA7XAkXEUpHiy3SwKjb7YLEWK9n5p0nx_p5Pz3AA_v_9Yzs49xGQTnkJD3vIWUk7mN-U3YWyfjukqwjc4fF6lRdY6S7DzNnfOsSCofsm675mZziw6X2fi1KbtzsKsVJ6r0TGdccpwOHKwnYpCOIXrMItVagO3_piR86-kWw5JdUCo-0tODEHxEAQRk2E1_MTofm_hTmiwX2SBjqzEoIpVdiuCOZY2wMo2tR4huYy3Y5_fz3kTCYguN1LTDjAZUoPHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fb8d0412d.mp4?token=rPyQvL7tqa0EUHAJ_dof1J-kM6DmcFAljXn3mPUJ8vYMDeRL6RkvyEYvvcz0cHOGUUbhf3y561i9dNSDDFECFA7XAkXEUpHiy3SwKjb7YLEWK9n5p0nx_p5Pz3AA_v_9Yzs49xGQTnkJD3vIWUk7mN-U3YWyfjukqwjc4fF6lRdY6S7DzNnfOsSCofsm675mZziw6X2fi1KbtzsKsVJ6r0TGdccpwOHKwnYpCOIXrMItVagO3_piR86-kWw5JdUCo-0tODEHxEAQRk2E1_MTofm_hTmiwX2SBjqzEoIpVdiuCOZY2wMo2tR4huYy3Y5_fz3kTCYguN1LTDjAZUoPHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درد و دل یک معلم منطقه سیستان و بلوچستان را بشنوید که هر میز ۴ نفر دانش‌آموز نشسته و درس دادن برای معلم بسیار مشکل است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72464" target="_blank">📅 15:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72463">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یک فروند هواپیمای بوئینگ ۷۳۷ متعلق به شرکت هواپیمایی ایرانی «کاسپین» در فرودگاه استانبول، به دلیل بدهی ۳ میلیون یورویی به شرکت خدمات هوانوردی ترکیه‌ای «ACM Temsil Gozetim» توقیف شد.
این هواپیما در حال آماده‌سازی برای پرواز به ایران بود که مأموران اجرای حکم قضایی وارد عمل شدند؛ آن‌ها ضمن دستور پیاده شدن مسافران، هواپیما را بر اساس حکم توقیف در فرودگاه نگه داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72463" target="_blank">📅 15:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72462">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26341dd428.mp4?token=phRraKGcejL3bVY9ToIv2EcRZ5bas-fwfwJ7FJRyzTahCc-l4k8h8L-Xjnk5VLS-IXxyTLwiG1gM-rwAFfHxERSZE9laUMKo_Sk5UBClxQX7zivUxVh4UC97FGdEVx-L3hgPZ4I7XzEWGUCU-3IOaKKN8HuBBRJiHDjyY04zK5P_iVLzB-3j1o1MBJzClpvooFqF_gvL3Xzevmt0wL_ovSERFM4uKuq2rBCJJYE8AjYxKtaO3wC2abeLpMkZUmgx2WldRea3M9ez8Lx0aBtE-1c-ldRtc1__6X6h3jpJhHmZnu4nxBXWuggeqWi9x17OgOERWpPfXZ88N2id1aYu0Evv5wnGm32N7wjbXgTYEFWVulVJkoTA4shf_JmPyYkh4ZG6Hs1OuneBZwT_2_3vQSESFuv57OBxGafYzmSBRPEfqHjye5nIq09ELdmuGgySuNT6hVYJoxPVO1TjT5S5LyHIMQjUmE4bP0D0v0NWOFzPDOcc-rQPDTA11bJb7I2Q0n9LQdokNrHM487dm4B2Ac2ms15ws4Ydrbm1pwUH8iHUb6aTC5IRjjjM16VUdBB2FoU_0E69xLb5ko4dTjtMe4YTkiVgwZIjGq6u7BHa87PkoUUUA4DYHnYo3mAD0JneIfC4VJCb6Z075_dtxrv2P26PiO3MF4TUenEtCZoSxa8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26341dd428.mp4?token=phRraKGcejL3bVY9ToIv2EcRZ5bas-fwfwJ7FJRyzTahCc-l4k8h8L-Xjnk5VLS-IXxyTLwiG1gM-rwAFfHxERSZE9laUMKo_Sk5UBClxQX7zivUxVh4UC97FGdEVx-L3hgPZ4I7XzEWGUCU-3IOaKKN8HuBBRJiHDjyY04zK5P_iVLzB-3j1o1MBJzClpvooFqF_gvL3Xzevmt0wL_ovSERFM4uKuq2rBCJJYE8AjYxKtaO3wC2abeLpMkZUmgx2WldRea3M9ez8Lx0aBtE-1c-ldRtc1__6X6h3jpJhHmZnu4nxBXWuggeqWi9x17OgOERWpPfXZ88N2id1aYu0Evv5wnGm32N7wjbXgTYEFWVulVJkoTA4shf_JmPyYkh4ZG6Hs1OuneBZwT_2_3vQSESFuv57OBxGafYzmSBRPEfqHjye5nIq09ELdmuGgySuNT6hVYJoxPVO1TjT5S5LyHIMQjUmE4bP0D0v0NWOFzPDOcc-rQPDTA11bJb7I2Q0n9LQdokNrHM487dm4B2Ac2ms15ws4Ydrbm1pwUH8iHUb6aTC5IRjjjM16VUdBB2FoU_0E69xLb5ko4dTjtMe4YTkiVgwZIjGq6u7BHa87PkoUUUA4DYHnYo3mAD0JneIfC4VJCb6Z075_dtxrv2P26PiO3MF4TUenEtCZoSxa8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر منتشرشده حملات پهپادهای مولتی روتور FPV نیروهای اوکراینی به سربازان و مواضع ارتش روسیه را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72462" target="_blank">📅 14:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72461">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311fdab4f1.mp4?token=BkQ98gjV_SJgEGxL1a2HXyyGwFwLXIs0rHm9DApQB4WrElN8W33BYjLNsekKYbF7U8TQWoN2fenB8iIpXPMx757VCBF1OWAcM7HQ7nMEAMpB3N40ez06OkNwaMk0YoppN7Z0h-kvvaYxJPvAx7EpklFvT22AwgoFOkRpbPFkZs1faqBR4ct0zd65yupM6ioxpWysS7S-Vh4wjfEDI5IElG4SbfWaLzsLqnepqIrCF-vegoGQsgaNTYDP0HBzztFC32xcuddkd4qaL_APEj1rkXRjpDvsqzjo_PLmUyeY_Q4uPGiSZuCxswD1LGgg-lfz17JUzy9JY7lSYseCbpr0LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311fdab4f1.mp4?token=BkQ98gjV_SJgEGxL1a2HXyyGwFwLXIs0rHm9DApQB4WrElN8W33BYjLNsekKYbF7U8TQWoN2fenB8iIpXPMx757VCBF1OWAcM7HQ7nMEAMpB3N40ez06OkNwaMk0YoppN7Z0h-kvvaYxJPvAx7EpklFvT22AwgoFOkRpbPFkZs1faqBR4ct0zd65yupM6ioxpWysS7S-Vh4wjfEDI5IElG4SbfWaLzsLqnepqIrCF-vegoGQsgaNTYDP0HBzztFC32xcuddkd4qaL_APEj1rkXRjpDvsqzjo_PLmUyeY_Q4uPGiSZuCxswD1LGgg-lfz17JUzy9JY7lSYseCbpr0LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در آن شب او یک ایران زخم خورده را به دوش کشید.
به یاد جاویدنام حمید مهدوی، آتش نشانی که خودشو فدا کرد تا معترضین رو نجات بده و در نهایت با شلیک گلوله، ۱۸ دی ماه به قتل رسید.
۷مهر روز آتش نشان بر حمید مهدوی ها فرخنده باد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72461" target="_blank">📅 14:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72460">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d05cdce3e.mp4?token=Jnd9Ej-jA5_1pMMT4_VaY3LEW6-Obv9x1VWDV2bsIibqVWdBWYLcrr_ymaqG-h2NdTZvz29V5bSmyK40ytXFn05tqMcWJI0EASQMtYLgvnHrU_bPkJYoY5jzhthRXo2yFIhnniuLTXCHITPkofrDhwLDO565wuSviYTbUz8bzEAk23cy5WSCbvk7kaq8SWCnjYlnvDNovZFFh4woVt9Ff4zv25VLwo7iQng7WxmzBEjXfL9Gda0tMgyTv3GF_G6qcUnuBIEnIrFIpnmkHbXySyG7fGAgU1HR0gcqF_hp90Nt2AwwTjaISzxLsfB5qGveqNYJ3KcmdLrmmkVTKa-TjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d05cdce3e.mp4?token=Jnd9Ej-jA5_1pMMT4_VaY3LEW6-Obv9x1VWDV2bsIibqVWdBWYLcrr_ymaqG-h2NdTZvz29V5bSmyK40ytXFn05tqMcWJI0EASQMtYLgvnHrU_bPkJYoY5jzhthRXo2yFIhnniuLTXCHITPkofrDhwLDO565wuSviYTbUz8bzEAk23cy5WSCbvk7kaq8SWCnjYlnvDNovZFFh4woVt9Ff4zv25VLwo7iQng7WxmzBEjXfL9Gda0tMgyTv3GF_G6qcUnuBIEnIrFIpnmkHbXySyG7fGAgU1HR0gcqF_hp90Nt2AwwTjaISzxLsfB5qGveqNYJ3KcmdLrmmkVTKa-TjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
افزایش ۳۰۰ هزار تومانی کالابرگ، پول یه پفک هم نمی‌شه.
سخنگوی دولت:
قطعا کالابرگ برای خرید پفک داده نمی‌شه!
+بیناموس مردم با سیصد تومن بیشتر چه چیزی میتونن بخرن؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72460" target="_blank">📅 13:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72459">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دلار ۲۵۰ تومن
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72459" target="_blank">📅 13:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72458">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a114556ee1.mp4?token=QQQSL8Mz3uPngUM2EGisDPbrTJN6lw6ox2vI-fQzW_0oUK8w9UGYvOVYKNGCfD5nZPW-niN567xokJ9COj4As3eAcJsAA6uSEkeAmOZMOgoa4aldZOfIQvpn6tyoZanK-bEuKak2wlhySynsXwrasndkr3hMr9ExQHTRJTUVYqY0rYdM3H8jVAiysjYl1SGKIWFY7BkoF2cmDylTr-vN1QlNHCW0KC0XFburtLytWP7lu1JCRRKJd0dhaMmKi7jfuKojGttFgJr5jPfdjcBhZ9PJr_GKY2gMCaadRXdlFUf670Ka1WK229gRoOTW2Y9NfCvQR100ccHJywqqbTuxoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a114556ee1.mp4?token=QQQSL8Mz3uPngUM2EGisDPbrTJN6lw6ox2vI-fQzW_0oUK8w9UGYvOVYKNGCfD5nZPW-niN567xokJ9COj4As3eAcJsAA6uSEkeAmOZMOgoa4aldZOfIQvpn6tyoZanK-bEuKak2wlhySynsXwrasndkr3hMr9ExQHTRJTUVYqY0rYdM3H8jVAiysjYl1SGKIWFY7BkoF2cmDylTr-vN1QlNHCW0KC0XFburtLytWP7lu1JCRRKJd0dhaMmKi7jfuKojGttFgJr5jPfdjcBhZ9PJr_GKY2gMCaadRXdlFUf670Ka1WK229gRoOTW2Y9NfCvQR100ccHJywqqbTuxoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی دولت : خبر خوش دارم اونم اینه که الحمدالله بحث کالابرگ حل شد و از نیمه دوم مهر کالابرگ رقمش میره بالاتر
خبرنگار : به به خوش خبر باشید دست شما درد نکنه
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72458" target="_blank">📅 13:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72457">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1910edd949.mp4?token=lsTRXfZhIOJapELul6UVexlCBKv47y4_04E68H9rANmbMBIo0fQDT2m8aniKo6qWE_Qd469thE65FFKgUhh-7ieUXkh8BnUujXvUDdw1NcCqP8A0quNZQCAJs2u5pWtFaIDU96jFfrRLy_azUjEC2HuBFMjILzY4RxOsrVQ3WpOA6IGW2sp2Mgwsj2dCZ8xn43NU-CbzKNR87o8Gqq08JdBd5b5VQks7dN4kJJKqXJ0KJfh3wXuufpnlb8OFbc4OBbZeA25vKTpayULcGhx0Q8mYZx4Ynyqr6XG3tUATyvT4O_TBF9gZSIjv2688Bq_dO-oduRDuB851JliIlX4qvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1910edd949.mp4?token=lsTRXfZhIOJapELul6UVexlCBKv47y4_04E68H9rANmbMBIo0fQDT2m8aniKo6qWE_Qd469thE65FFKgUhh-7ieUXkh8BnUujXvUDdw1NcCqP8A0quNZQCAJs2u5pWtFaIDU96jFfrRLy_azUjEC2HuBFMjILzY4RxOsrVQ3WpOA6IGW2sp2Mgwsj2dCZ8xn43NU-CbzKNR87o8Gqq08JdBd5b5VQks7dN4kJJKqXJ0KJfh3wXuufpnlb8OFbc4OBbZeA25vKTpayULcGhx0Q8mYZx4Ynyqr6XG3tUATyvT4O_TBF9gZSIjv2688Bq_dO-oduRDuB851JliIlX4qvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار افراد از پنجره‌های ساختمان در حال سوختن آکادمی علوم کی‌یف، پس از اصابت پهپاد جت‌سوز روسی به آن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72457" target="_blank">📅 12:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72456">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a809065ce.mp4?token=I71OK27jIdN8Xtn_mQJET-3HArkEISsykzZcvSMrmxoi9TkNVQ6EHP7vYwNdhpEL7xkIaB8x9qLnJyRWu0vRBnn9jCAJOahwH0SaY162r8x1DvguZKXrTjXsjqBHONzEiIatuMGNPczxQxbAR9ueVNKGSN7bdyeYVaYlF10on5m6hAe4NjVKnbu-JU384eNLwfqhzs0-yoF3Oyyf6RjhZsbg8ydfqT7sVeUbRVjWUMk1r9v1BxMGkMb56jNAmfwr7QYlvWWSk9vpb81Asu6LRHPMzbCKdI7n9aZLXBbbZ1vAa10gjNkRs2ghDyuamEV_mKL2ttHA4c-4aJvJx0WKQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a809065ce.mp4?token=I71OK27jIdN8Xtn_mQJET-3HArkEISsykzZcvSMrmxoi9TkNVQ6EHP7vYwNdhpEL7xkIaB8x9qLnJyRWu0vRBnn9jCAJOahwH0SaY162r8x1DvguZKXrTjXsjqBHONzEiIatuMGNPczxQxbAR9ueVNKGSN7bdyeYVaYlF10on5m6hAe4NjVKnbu-JU384eNLwfqhzs0-yoF3Oyyf6RjhZsbg8ydfqT7sVeUbRVjWUMk1r9v1BxMGkMb56jNAmfwr7QYlvWWSk9vpb81Asu6LRHPMzbCKdI7n9aZLXBbbZ1vAa10gjNkRs2ghDyuamEV_mKL2ttHA4c-4aJvJx0WKQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط ۷ سال گذشته! وقتی همه می‌خندیدند که این ربات‌ها چقدر دست‌وپاچلفتی بودند. با نگاهی به اینکه مدل‌های هوش مصنوعی در همین مدت چقدر پیشرفت کرده‌اند، واقعا کنجکاویم تا ببینیم ربات‌ها تا کجا پیش خواهند رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72456" target="_blank">📅 12:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72455">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3U-dWE8bOToXwHOZgor5Il-w_vBp2axGYvG4sI3En3ImvDQOfd6vg1XyiBj_l-v02pGKlykBZbhhQ_bSaGSd6pQm41iRHJ-a-EM8Qui2LiyMaY4qruf9VSj7H18kHCP33w3o4ABFUiccGMwbublE6oa4cYMQ1Lo87Hb2dmOZHyOWJGqisRmfjvEIgK8e9nykAIiJ0IAlwKhVN2Qj4g6A5rmeAK7oh5su5VKn1fmmwLu2uHV_xAjWHQNnExbHfAEEwUd_F9_WCSd-8Y5I281ioTCiYsZQNuwj1B6pXDq9wwXEkAqQ9XG9M9DNVXBxxusmOzTg4kJLzmI9BnZMOF_WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
قوه قضائیه جمهوری اسلامی: رای پرونده ترور قاسم‌سلیمانی صادر شده و بر این اساس دولت آمریکا موظف به پرداخت ۴۸ میلیارد دلار است!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72455" target="_blank">📅 11:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72454">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72454" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72454" target="_blank">📅 11:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72453">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeSmhysY0cPj3mU2mZe-y1tyv-2f8Cyad-E3lTWlnJGE65w_3qEKHTUFFvYz6nTQPw-G6awPELaPClTxzCJD2b1btBBeoxPcYfOMD04S4bB1FuajMYX0ikxllNPYznoULo2bLCn3kG_0tf8KoAQkrTYl9kuoe5xCaPb5B1glAp3MMTMFFv4c_IcbTf-tfguLa4ZwgkaJY-ZnW6qGXen_l8GI_RPtTbYPGV4ghOEnLf0giY3RFNw-HP1BrHOcniR2R0SLZnLS1V8hyqhlprQi14rqKnwX59v-s1VQ2ipLRBEmj8Zd5L143NANMrStaxmWsWUx31qNGb6tL59qN3xAVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
انگلیس
🆚
چک
کرواسی
🆚
اسپانیا
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
https://TrexBet.com</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72453" target="_blank">📅 11:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72452">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دلار ۲۸ تومن شد</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72452" target="_blank">📅 11:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72451">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/375e130021.mp4?token=Sw9b5yC2namAU-vob7xdlBOq5q1s9XJQm62AVO7y0mgOb7pezxQfn9fhDlU2YPitGzbh-xt_IwPbwNyttceJvjKP8Gzooy3sdY0X9R9WQiB2R6Qe8rTSRSpuRo30C0jVa8XdxSwtWNaOCQ215LnRRPUtD7bKqQM3vNXsPQKfEvswX_MhhcVPieAT76g6f2wDEZSrSr0ppE87GLXrjzeV0tCEy45YCUy98ZSUxSxvcutj7TDxrg5I64V_6d4y-NV5aUvlGQBpn1t82HLnafJAt02vvkeDyleGOmfyOTisyVHdtScsgTbU2YjVQNZyhheKqlM4G5gHJ24hiIiwszaaww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/375e130021.mp4?token=Sw9b5yC2namAU-vob7xdlBOq5q1s9XJQm62AVO7y0mgOb7pezxQfn9fhDlU2YPitGzbh-xt_IwPbwNyttceJvjKP8Gzooy3sdY0X9R9WQiB2R6Qe8rTSRSpuRo30C0jVa8XdxSwtWNaOCQ215LnRRPUtD7bKqQM3vNXsPQKfEvswX_MhhcVPieAT76g6f2wDEZSrSr0ppE87GLXrjzeV0tCEy45YCUy98ZSUxSxvcutj7TDxrg5I64V_6d4y-NV5aUvlGQBpn1t82HLnafJAt02vvkeDyleGOmfyOTisyVHdtScsgTbU2YjVQNZyhheKqlM4G5gHJ24hiIiwszaaww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنندج؛ ضرب و جرح شدید سه نوجوان توسط ماموران انتظامی
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72451" target="_blank">📅 11:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72450">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16f0cd62a0.mp4?token=MxFCYCEhr7wL8zg37ABen1fwIqj0X2RTldRDcCv-NxX5qoFLOSZIt5q50j96ki1AysoXrsFJXoeX81x2fWGsMqekiB7c_aUSEhJYnkZUA-UItuPI2ws9xFQMHaTsQP_zIsVsjuzytiCgokCwlnzgS_gOUtihQuvppyuV_8scnVf_8fTj2nv6IEMwMgz6S1uzHgTm0RZVA22pph-FYmhFZtB2WoIA-6gxcoBEuKTvtCQtQjDEOh1idtfztgYe6z8V8RkrjNhuO8nFrnqWJZEfxaZ7KcctTczZ3JBStVI_NLcbKzaD_fwbdNt_ecSCLpb_KjDsBxuS9U0Gh7Y1rP97Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16f0cd62a0.mp4?token=MxFCYCEhr7wL8zg37ABen1fwIqj0X2RTldRDcCv-NxX5qoFLOSZIt5q50j96ki1AysoXrsFJXoeX81x2fWGsMqekiB7c_aUSEhJYnkZUA-UItuPI2ws9xFQMHaTsQP_zIsVsjuzytiCgokCwlnzgS_gOUtihQuvppyuV_8scnVf_8fTj2nv6IEMwMgz6S1uzHgTm0RZVA22pph-FYmhFZtB2WoIA-6gxcoBEuKTvtCQtQjDEOh1idtfztgYe6z8V8RkrjNhuO8nFrnqWJZEfxaZ7KcctTczZ3JBStVI_NLcbKzaD_fwbdNt_ecSCLpb_KjDsBxuS9U0Gh7Y1rP97Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از یک سگ که بر اثر صدای انفجارها وحشت‌زده شده بود، در جریان حملات روسیه در اوکراین ضبط شد:
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72450" target="_blank">📅 11:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72449">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8923a23fa4.mp4?token=ipT9dAvtQjlfpCQvwVKXa_FvhX0s7tpdluMxuPD7LKADa7_mG9tUMyZhw2wBWbi87X6XM6bUBrhCFvGROeeu-Wx7mzZzc9vc3bGEfmEDwqlVUKLrLNPxS8cdVagJ68qcLoBmq7Eg0qMXMizQl_8x9CZRISEyC5sTEVUVZfrxJRS8OPt_kmTiJQWXxE0NfzuyPl-5P2KB6_l_FcwaAij5VUL30TkSUtxDRZPFDFpzUPGMEwcVV6290G4z8f-Zu1VXBtHAAFxtOkUxsi_CfcBEVX2x-norcl3UEiSjCc8fV-QGAm6ES7Gpi19YoyV4e7GfsfL6idlZgBm_8LWkyqC2I5sfZniQvosQPi-J2NJfplqn0UlfYltf2R4_U_H_RatC8ROvDPOgjitu0fUGbiWZ1fKogqWQEze7xU6CIrRfAzwpwqBR7rF3yCzLYal202JwD3C6VvIp9GMT4k2f4kEWClQfOr42_JHr_ffL0r_AbQahz7KBjJf4sgbg8RLTOqwn3QBEhA00ngH7CpUwn8XfYHl1S2Kx3pAiTervFrom0Ah134V6I2c0UJR651eD4phS_xGjeH44fi4HDg041NuObLlCNZTZmU8PZP1cfHWuFYZslwhy66YXaZGTwrEfM9A5xo8HPbwxT2EnWOzYgtq1C_H3p3Ui8xXGgv5bnfFVbQU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8923a23fa4.mp4?token=ipT9dAvtQjlfpCQvwVKXa_FvhX0s7tpdluMxuPD7LKADa7_mG9tUMyZhw2wBWbi87X6XM6bUBrhCFvGROeeu-Wx7mzZzc9vc3bGEfmEDwqlVUKLrLNPxS8cdVagJ68qcLoBmq7Eg0qMXMizQl_8x9CZRISEyC5sTEVUVZfrxJRS8OPt_kmTiJQWXxE0NfzuyPl-5P2KB6_l_FcwaAij5VUL30TkSUtxDRZPFDFpzUPGMEwcVV6290G4z8f-Zu1VXBtHAAFxtOkUxsi_CfcBEVX2x-norcl3UEiSjCc8fV-QGAm6ES7Gpi19YoyV4e7GfsfL6idlZgBm_8LWkyqC2I5sfZniQvosQPi-J2NJfplqn0UlfYltf2R4_U_H_RatC8ROvDPOgjitu0fUGbiWZ1fKogqWQEze7xU6CIrRfAzwpwqBR7rF3yCzLYal202JwD3C6VvIp9GMT4k2f4kEWClQfOr42_JHr_ffL0r_AbQahz7KBjJf4sgbg8RLTOqwn3QBEhA00ngH7CpUwn8XfYHl1S2Kx3pAiTervFrom0Ah134V6I2c0UJR651eD4phS_xGjeH44fi4HDg041NuObLlCNZTZmU8PZP1cfHWuFYZslwhy66YXaZGTwrEfM9A5xo8HPbwxT2EnWOzYgtq1C_H3p3Ui8xXGgv5bnfFVbQU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه امیرحسین قیاسی با پسری که رتبه ۹۲ کنکور شد ولی معتقد بود ریده و پشت کنکور موند!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72449" target="_blank">📅 10:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72448">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Edi4R1I23DwRFNWWDpgLtkqu3VS2-fP2D8K7zm0lGwHeaeZ0G42o6f8WEyz7nW5wsA_VFcy7PJztRcf6kcdkxMqXiK6Y4smEYMeIykio3jkqABhTE_EGZcm80mTf5AFMwTjn1M-U9OG4zD-hvEmflnyFz3_obDeFkin8VDAnjg_WALYcQXHjyzrDHoE6TiRa9pMumJ7-dyjEiJ8J36QjmbroSjy80uBWMKx3cWfxN6FD59H6YAEsKAQb7xL0ZphHBjYbfjUVx7ENmNHJorn4DlbqxuRoWi94ZxDOCPNmTo_xgEotK24NV8ZJtHx0YKCnJLJRkC2-xRteSrj49icz7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛به گزارش شبکه خبری «کان»، سفر روز یکشنبه بنیامین نتانیاهو، نخست‌وزیر اسرائیل، به امارات متحده عربی که در اصل برای هفته گذشته برنامه‌ریزی شده بود، در آخرین لحظات و پس از اعلام عدم امکان دیدار با رئیس‌جمهور امارات (محمد بن زاید) از سوی مقامات این کشور، به تعویق افتاده بود.
مقامات ارشد چندین کشور حوزه خلیج فارس، از جمله نمایندگان کشورهایی که روابط رسمی با اسرائیل ندارند، در گفتگوهایی با نتانیاهو که بر موضوع ایران متمرکز بود، شرکت کردند. نشست منطقه‌ای مشابهی نیز در جریان سفر قبلی نتانیاهو به امارات در ماه مارس (هم‌زمان با تنش‌ها و درگیری‌های مرتبط با ایران) برگزار شده بود.
هم‌زمان با سفر نتانیاهو، هواپیماهای مرتبط با نیروهای حفتر در لیبی، مراکش، قطر و امارات در ابوظبی حضور داشتند؛ از جمله یک هواپیمای دولتی امارات که از مبدأ ریاض وارد شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72448" target="_blank">📅 09:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72447">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2070144954.mp4?token=vPoty6eLZbLWANlQ2soEQCVBSwhgjPliuf5WlJT5b9aZ9u2ggd_97_36zc7nuh6fv7vA_PU5vv02C2QfyjZP96h9NcSti9vr_x2jB3daPGyrUn7Ea5pVXpcj0ru0MANPS75O4VfiI-acBurSQQG4ZlR-xw7CHMjzc4gwHmiIqflvwUN1_3GXSJaYSMl5BJoVGGIkagONmqkFBK5wRIFhPrWaA6YPJ5eKCoVFaSg5YAEAoW9JSC1Y5IlmFru5wV1T4-vVwR37RHc_bgc3REj9z0e6VPArPde8q0JqJN0Ii1EeBb-QNhnRIT1h3ba0fmAQYfkkNGlBzSXsk9SoTyEfUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2070144954.mp4?token=vPoty6eLZbLWANlQ2soEQCVBSwhgjPliuf5WlJT5b9aZ9u2ggd_97_36zc7nuh6fv7vA_PU5vv02C2QfyjZP96h9NcSti9vr_x2jB3daPGyrUn7Ea5pVXpcj0ru0MANPS75O4VfiI-acBurSQQG4ZlR-xw7CHMjzc4gwHmiIqflvwUN1_3GXSJaYSMl5BJoVGGIkagONmqkFBK5wRIFhPrWaA6YPJ5eKCoVFaSg5YAEAoW9JSC1Y5IlmFru5wV1T4-vVwR37RHc_bgc3REj9z0e6VPArPde8q0JqJN0Ii1EeBb-QNhnRIT1h3ba0fmAQYfkkNGlBzSXsk9SoTyEfUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو به‌تازگی در برابر دیدگان میلیون‌ها نفر فاش کرد که باراک حسین اوباما به تأمین مالی رژیم تروریستی ایران و مرگ هزاران نفر کمک کرده است.
«در مورد هر دلاری که ایران در اختیار دارد، کاری که آن‌ها طی ۳۰ سال گذشته انجام داده‌اند این بوده که هر زمان پولی به دست آورده‌اند — چه در جریان لغو تحریم‌ها توسط اوباما، چه از طریق فروش نفت و گاز و غیره — آن پول را صرف ساخت بیمارستان برای مردم خود نکرده‌اند.»
«آن‌ها این پول را صرف دو کار می‌کنند: ساخت سلاح برای خودشان و صدور انقلاب!»
«آن‌ها این پول را صرف تأمین مالی حزب‌الله می‌کنند. صرف تأمین مالی حماس می‌کنند. صرف تأمین مالی شبه‌نظامیان شیعه در عراق می‌کنند. بله، این‌گونه آن را خرج می‌کنند. آن‌ها این پول را برای حمایت از تروریسم و توطئه‌های ترور در سراسر جهان به کار می‌گیرند!»
«[ما] مانع دسترسی آن‌ها به پولی می‌شویم که قرار است برای کشتن آمریکایی‌ها استفاده کنند.»
اوباما پول نقد و لغو تحریم‌ها را برای ایران فرستاد و آیت‌الله‌ها آن را به موشک و تروریسم تبدیل کردند.
رئیس‌جمهور ترامپ دقیقاً برعکس عمل کرد و جریان پول را قطع نمود و...
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72447" target="_blank">📅 09:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72446">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb7b6e5b41.mp4?token=OGr1egvZ7TWdLNfdf5kgz92lHlwfFe6GLrtIQxtYamWEsVr4lfwk7OVi5KzW1nRfTYwc6xRj-kxeyv2ybaN1169zwrERXXMdH7j4Gr6YG4gHtb5TiS7ue1WBk8LD8028euN7yi1_eG9Vl0reW7vcfOfiTpmSAPAYLufYRwbcYNN_F9ea90VRIvRwZi0cRZjDn97-qRgx31q_ULQjkiDX5j6sRwpry0-n1DsknVGanIJRRunLguaQYbMZwPQ7boHU6Yx-bjvLWZdwXdjMfwC6ygBeke64ftngIHkpl_NMhxGPc9CEfhVUmAXoDOoxAVY6Pa-joNTMVAX2yuuv5QKvsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb7b6e5b41.mp4?token=OGr1egvZ7TWdLNfdf5kgz92lHlwfFe6GLrtIQxtYamWEsVr4lfwk7OVi5KzW1nRfTYwc6xRj-kxeyv2ybaN1169zwrERXXMdH7j4Gr6YG4gHtb5TiS7ue1WBk8LD8028euN7yi1_eG9Vl0reW7vcfOfiTpmSAPAYLufYRwbcYNN_F9ea90VRIvRwZi0cRZjDn97-qRgx31q_ULQjkiDX5j6sRwpry0-n1DsknVGanIJRRunLguaQYbMZwPQ7boHU6Yx-bjvLWZdwXdjMfwC6ygBeke64ftngIHkpl_NMhxGPc9CEfhVUmAXoDOoxAVY6Pa-joNTMVAX2yuuv5QKvsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
مشکل اصلی در مورد ایران، «انقلاب» است؛ نه آن مقامات دولتی کت‌وشلوارپوشی که در برنامه (Meet the Press) شبکه ان‌بی‌سی ظاهر می‌شوند و در رسانه‌های آمریکا بی‌هیچ دردسری تریبون رایگان در اختیار می‌گیرند!
«بحث ما درباره آن‌ها نیست؛ کسانی که در ایران حرف آخر را می‌زنند، روحانیون شیعه تندرویی هستند که دیدگاهی آخرالزمانی نسبت به آینده دارند.»
«آن‌ها معتقدند که رسالت مذهبی‌شان این است که آغازگر وقایع پایان جهان و آخرالزمان باشند.
این واقعیت است؛ این هدفِ اعلام‌شدۀ انقلاب آن‌هاست. چنین افرادی هرگز نباید به سلاح هسته‌ای دست پیدا کنند، چرا که از آن برای باج‌گیری از جهان و کشتار مردم استفاده خواهند کرد. این ریسکی غیرقابل‌قبول است.»
ترامپ دارد کار درستی برای جهان انجام می‌دهد. او اکنون به دنبال کسب پیروزی کامل بر ایران است، زیرا این تنها راه چاره است!
بانک‌های مرتبط با ایران در حال تعطیلی هستند، ترامپ عقب‌نشینی نمی‌کند و ایران قادر به صادرات نفت نیست.
اوضاع کاملاً علیه آن‌هاست. هرگز نباید سلاح هسته‌ای داشته باشند!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72446" target="_blank">📅 09:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72445">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c2b12f18e.mp4?token=PLPsps5Im7QBJz6ONr-gxaDGzrjOciLlMTGdNiD0E-h6Q1-8TJRGwMIvNwuksdYDy-dqCwsJLE-HxoNuNZeZ0BhlgLj_et9y-HAdi5tMES_MlO26esIhZ2qyiyrjHlu1ngz_0kV2hupGJ5rjLWlKq-bUsk2MR_o3Bk242QRbHYtYKkuEyUx0dWTZoUS_wOgXffWjRTKo73Q_z1ZyUGPeyeCkAZkKSNV25SK_AM6KaulNSaAN9MwdfR9mricruU0JSIUqHxKQbU_paKuY2_HN_o4ZGL5VRjc6kN5Xyhby5MLADTlZhqxoFDEOYznHx71dEodP9moFnyVs-fjHJdo6rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c2b12f18e.mp4?token=PLPsps5Im7QBJz6ONr-gxaDGzrjOciLlMTGdNiD0E-h6Q1-8TJRGwMIvNwuksdYDy-dqCwsJLE-HxoNuNZeZ0BhlgLj_et9y-HAdi5tMES_MlO26esIhZ2qyiyrjHlu1ngz_0kV2hupGJ5rjLWlKq-bUsk2MR_o3Bk242QRbHYtYKkuEyUx0dWTZoUS_wOgXffWjRTKo73Q_z1ZyUGPeyeCkAZkKSNV25SK_AM6KaulNSaAN9MwdfR9mricruU0JSIUqHxKQbU_paKuY2_HN_o4ZGL5VRjc6kN5Xyhby5MLADTlZhqxoFDEOYznHx71dEodP9moFnyVs-fjHJdo6rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
اگر رئیس‌جمهور ترامپ اجازه می‌داد ایران به سلاح هسته‌ای دست یابد، نه تنها همه او را مقصر می‌دانستند، بلکه ایران کنترل کامل تنگه هرمز را در دست می‌گرفت.
درحال حاضر تقریباً همان‌قدر نفت که پیش از این مناقشه جریان داشت، از تنگه‌ها عبور می‌کند؛ به استثنای نفت ایران.
«آن‌ها می‌توانستند تنگه‌ها را کنترل کنند، حق عبور (عوارض) تعیین نمایند و تصمیم بگیرند که چه کسی در این سیاره انرژی دریافت کند و چه کسی نکند. اگر آن‌ها سلاح هسته‌ای داشتند، دقیقاً همین کارها را می‌کردند.»
«اگر ایران سلاح هسته‌ای داشت که می‌توانست با آن همسایگان و جهان را تهدید کند، هیچ‌کس نمی‌توانست در مورد تنگه‌ها کاری انجام دهد.»
«۵ سال دیگر، همه می‌گفتند: "باورم نمی‌شود که اجازه دادند ایران در پناه یک سپر متعارف، برنامه تسلیحات هسته‌ای خود را بسازد و توسعه دهد!" وحالا شاهد حضور یک کره شمالی دیگر در خاورمیانه بودیم. ما در آستانه چنین وضعیتی بودیم! این همان چیزی است که رئیس‌جمهور مانع وقوع آن شد.»
«وبدتر اینکه، صحبت از رژیمی است که در جریان آن به اصطلاح انقلاب، ده‌ها و شاید صدها هزار نفراز مردم خود را قتل‌عام کرده است!».
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72445" target="_blank">📅 09:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72444">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">عراقچی:
امروز (دوشنبه) یکی از واسطه های قطری دیدار مجددی با ما داشت، بحث هایی را انجام دادیم . روی ایده هایی صحبت کرد و اینکه چگونه می شود برای تحقق شروط ایران راهگشایی کرد و چگونه این شروط را محقق کرد.
ایده هایی داشتند و بحثی را داشتیم که باز با طرف آمریکایی هم مطرح خواهند کرد و بعد پاسخ نهایی طرف آمریکایی پس از آن به ما منتقل می شود که امیدوارم تا فردا (سه شنبه) این کار انجام شود.
من چند ساعت دیگر به سمت تهران پرواز می کنم و پاسخ را قطری ها هر موقع که داشته باشند، می دانند که چگونه به دست ما برسند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72444" target="_blank">📅 06:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72443">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72443" target="_blank">📅 01:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72442">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72442" target="_blank">📅 01:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72441">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tj76EVDOyFBvfww1wYJVXr0GtZ-a3dDwqnRHVcd56_vh-fuH8zo4yDHPWrigeqqeuQzURlYyCSRrVMMz7Ep6gVB90ISAbmReLh9n_AwSpuqswg3zc5io1rUpZUN9Tm_PaxYbCpPTKWIWALwoVXv1R3v4OZYrL4Pp-VAkISTDejYooM_ZWzdyImxvgYvpPj7BF-CEHtKQuOAVdcudQtUAmE3ft0AqzVObsiOugANw35F1qE8uXT1go2xvcISihbnuDyhx-5YLoQFv63hKefVJtRlmC4v5T5-R3pUGBMj07F7RFgnVb3OK_3hfp-C1l0DdK1xqLIFlt7acbZgRQKu1dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام امریکایی به باراک راوید گفت:   رئیس‌جمهور ترامپ مایل است در ازای پیشرفت‌های ملموس در پرونده هسته‌ای، تحریم‌های ایران را کاهش دهد و وجوه مسدودشده را آزاد کند.  @News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72441" target="_blank">📅 01:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72440">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iED8Kj87Kq6XlBKh-I3m5rBmQuM8_3UlGhO4AiK4W3qqaaWQYsuob1Biezz4LpEY4WAwqD2SByzCqUfWg7QoLvYkfaTj_Ig5TZF0jzEGYUJ1sOfqyNs64dj6DoIaoA_lhSDJtjMzzrDP05tN4mYd0JYSTsEtYpDlcBPIqavYqW4tyE3nG_fCDoYZSuTRSEBfYnkyoZtc05wgynDW4Tmm-Zio8ZuEf_3p8epI2K84-ERMGAGJIAOO0BuZ8HO-z27ev64MQxHVpW7LV6ao2d70CEvW3iDPlMosrTrEvbRWxK9pBhAbJMlRdIWfLFG76wJUFa1DeI6c6NhMK-X1wrxHsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر نخست‌وزیر نتانیاهو:
نتانیاهو و همسرش دیروز به دعوت شیخ محمد بن زاید، رئیس امارات متحده عربی، از این کشور دیدار کردند.
در این سفر، رئیس شورای امنیت ملی، رئیس موساد، منشی نظامی و مشاور سیاست خارجی، نتانیاهو را همراهی می‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72440" target="_blank">📅 00:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72439">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نقشه‌های گوگل تصاویر ماهواره‌ای پیش‌فرض خود برای غزه را به تصاویر ژانویه-فوریه ۲۰۲۶ به‌روزرسانی کردند و مقیاس تخریب را بلافاصله برای هر کسی که برنامه را باز می‌کند، قابل مشاهده ساختند.
کاشی‌های ۲۰۲۶، بلوک‌های مسکونی متراکم در رفح و خان یونس را نشان می‌دهند که به مزارع آوار خاکستری تبدیل شده‌اند، منطقه بیمارستان الشفا به شدت تغییر یافته است و اردوگاه‌های چادری عظیم در زمین‌های باز باقی مانده قرار دارند.
آخرین آمار UNOSAT: ۲۰۱,۲۹۰ سازه آسیب‌دیده (۸۲٪ از کل ساختمان‌ها)، ۱۳۴,۴۲۲ سازه تخریب شده.
این تصاویر حدود ۲۳۵ کیلومتر مربع را با وضوح حدود ۱۳ سانتی‌متر پوشش می‌دهند - به اندازه‌ای واضح که می‌توان دیوارهای جداگانه و خوشه‌های چادر را مشاهده کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72439" target="_blank">📅 23:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72438">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa72acf92f.mp4?token=bywrOvo970cSWl-7XbDcDp_WEDuLir-5R1Uf4gIQtqv6_r2-25JteIELXhjtUjdN66mrjUjdCUxE6UPyi1cqo8NBhaYEURCMi20tMRgFGY27vu-D8GoiBAAt0yxdQCsEW9XYViHDEzjPrOP2fwaH-h0mlx-hRM_EJAO8_gnTJ9YNmuXwi3pK5W4n5wlxwmwtIVKLoN89qvNMfQre80qrmiCpAUhSS2eSQHhWvcwYjV2lvW-iefSv93SinGpKt7Eq7q545Bj1O45SfJahjv-fDvzXXp3K58Mks3moHOk4w1YQsm60QEdY1y0zCNKlgzzITHSTm2l2f1Dm02ZlCFbg_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa72acf92f.mp4?token=bywrOvo970cSWl-7XbDcDp_WEDuLir-5R1Uf4gIQtqv6_r2-25JteIELXhjtUjdN66mrjUjdCUxE6UPyi1cqo8NBhaYEURCMi20tMRgFGY27vu-D8GoiBAAt0yxdQCsEW9XYViHDEzjPrOP2fwaH-h0mlx-hRM_EJAO8_gnTJ9YNmuXwi3pK5W4n5wlxwmwtIVKLoN89qvNMfQre80qrmiCpAUhSS2eSQHhWvcwYjV2lvW-iefSv93SinGpKt7Eq7q545Bj1O45SfJahjv-fDvzXXp3K58Mks3moHOk4w1YQsm60QEdY1y0zCNKlgzzITHSTm2l2f1Dm02ZlCFbg_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها دیوانه‌اند. هیچ شکی در آن نیست. آدم‌های بسیار دیوانه‌ای هستند.
من همیشه به آن‌ها می‌گویم: «شما دیوانه‌اید، رفیق.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72438" target="_blank">📅 22:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72437">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de98b8705f.mp4?token=Tq4cV2oIsdNoxFa-F42SMOKkkNKbZebAKPGMLk-fdhUVTd4VbZmHqMepkJESstFoHM-AXu388xcT8Nb7MdHAH9zyX8ukxw0Om9TSZycblE4FtEzltqzBdf1dat5E0YqoPdv5ZkLkAtaZEr7dVRZk2VX6TtDq9wHZo3g23x2HjLf2uMJ7xhH_-_60cGAQSHxU36yUJgHQZQaWNaZuFRX2qkLnxx3CesSZafF4Q6w6PsTm9Pji126OiKkP56tA56nM5kGJOzYeMlF94tKNjM72o-7GxAloKI62fURkEApRNWhiWAU5woosZDYJugY2S2uxLqcwf-avZ_VanX_ESzN5JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de98b8705f.mp4?token=Tq4cV2oIsdNoxFa-F42SMOKkkNKbZebAKPGMLk-fdhUVTd4VbZmHqMepkJESstFoHM-AXu388xcT8Nb7MdHAH9zyX8ukxw0Om9TSZycblE4FtEzltqzBdf1dat5E0YqoPdv5ZkLkAtaZEr7dVRZk2VX6TtDq9wHZo3g23x2HjLf2uMJ7xhH_-_60cGAQSHxU36yUJgHQZQaWNaZuFRX2qkLnxx3CesSZafF4Q6w6PsTm9Pji126OiKkP56tA56nM5kGJOzYeMlF94tKNjM72o-7GxAloKI62fURkEApRNWhiWAU5woosZDYJugY2S2uxLqcwf-avZ_VanX_ESzN5JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
اگر می‌خواهید هرج‌ومرج را ببینید، بگذارید شهری را با سلاح هسته‌ای نابود کنند.
من فقط درباره اسرائیل و بخش‌های وسیعی از خاورمیانه صحبت نمی‌کنم.
بگذارید با سلاح هسته‌ای به ما حمله کنند؛ خطاب به همه آن آدم‌های احمقی که فکر می‌کنند این کار اشکالی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72437" target="_blank">📅 22:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72436">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/530a31d83d.mp4?token=jz-6E2GHfVsZpWkf3-EqpfTsI_WC-80yB57vOlPOubnOQm9wBYnl4VYoBUbCJ_oBGME-rw5WURCR8W2G7TARJ9S87RDdZjQixSF22lQqK_oavR9TfMpeWyEoxT_JPdX4zoeUEp7V-S-aVCNhViljUHMIEAk1SzhkU8h3gOjaGp22KzRw3L_J1Akf8CxMsne8a7kqlX6YgMqV1jsmFHPfaRw26MESGomP1bIqj-u7lvqeAHcckUMMLp-M_SgcPs-yRb-elogkKUP3iOAgStsYQJLy2uTpKnAOCAqRcuP84SmKTgLggaL9E0uYrmR9Mqi75fjr5TEAfGTac9yOMxL0TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/530a31d83d.mp4?token=jz-6E2GHfVsZpWkf3-EqpfTsI_WC-80yB57vOlPOubnOQm9wBYnl4VYoBUbCJ_oBGME-rw5WURCR8W2G7TARJ9S87RDdZjQixSF22lQqK_oavR9TfMpeWyEoxT_JPdX4zoeUEp7V-S-aVCNhViljUHMIEAk1SzhkU8h3gOjaGp22KzRw3L_J1Akf8CxMsne8a7kqlX6YgMqV1jsmFHPfaRw26MESGomP1bIqj-u7lvqeAHcckUMMLp-M_SgcPs-yRb-elogkKUP3iOAgStsYQJLy2uTpKnAOCAqRcuP84SmKTgLggaL9E0uYrmR9Mqi75fjr5TEAfGTac9yOMxL0TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا رویداد پایگاه «آر.ای.اف. فیرفورد» (RAF Fairford) به ایران ارتباطی دارد؟
ترامپ: ممکن است مرتبط باشد، اما باید بگویم از اینکه آن‌ها را آزاد کردند، تعجب کردم. من چنین کاری نمی‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72436" target="_blank">📅 22:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72435">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ccb54f2ff.mp4?token=ENAgXdJKcgCWSkVF96lc1EmbwGGxp_RuA7yQhHPBYJDqfR0j5K6VETUsWSADDOe3hXZ4PcIAEa3XUAiV_-Ig5Wvun5Y9R3C8Z1i4oZp4nW1NAPOhFD9mqqsoqZvIZMD-L7Khun8LfS3C95oNDdFfY93TupG45OvTrZNHl5jw9GEWOto-iS5d2E6yflVxeDbGeSA88j_1NjuwmWgWsWrLtVl-n3AQvLDMLBkRw1fRzPd2xOybXlwari6uCx02ZVFzpFktdM3hnYLUT5W5-uQNnKdXESS-WEoq2sism1Lg54D8aeu9foO-VNN1ygWeh2wAlNd6tCEIlxrvyR9suEEuBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ccb54f2ff.mp4?token=ENAgXdJKcgCWSkVF96lc1EmbwGGxp_RuA7yQhHPBYJDqfR0j5K6VETUsWSADDOe3hXZ4PcIAEa3XUAiV_-Ig5Wvun5Y9R3C8Z1i4oZp4nW1NAPOhFD9mqqsoqZvIZMD-L7Khun8LfS3C95oNDdFfY93TupG45OvTrZNHl5jw9GEWOto-iS5d2E6yflVxeDbGeSA88j_1NjuwmWgWsWrLtVl-n3AQvLDMLBkRw1fRzPd2xOybXlwari6uCx02ZVFzpFktdM3hnYLUT5W5-uQNnKdXESS-WEoq2sism1Lg54D8aeu9foO-VNN1ygWeh2wAlNd6tCEIlxrvyR9suEEuBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره ایران:
ما خیلی زود در آن جنگ پیروز خواهیم شد. ماجرا تمام می‌شود و قیمت بنزین به‌شدت سقوط خواهد کرد.
هیچ‌کس دیگری نمی‌توانست چنین کاری انجام دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72435" target="_blank">📅 22:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72434">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/323953406a.mp4?token=sYfns4cZAVWj_RAI8vqqdbkz3bysXeR6DNyThuq-hJPIQhjUVqGqcGhJj2E3tfhQoNLF5J0Q0i4ljUgDY_mFgo2V0ENnOUsz6mOy0hlepncosw-kQy_2F12ikxrYzFqkW77uOLxV3cFreqx9oabo39htbxntK1wXJKUoKgH_0Ih_q7cMJKKmMpz_r725qmGVcnD6raPZR64G72IpKvvx33wFm5G4Wxqu-ppT8aqcSBTMiM-ytfikoxQ4CQl0aOMqtrq17nWqX404fay0NlMwmcXgyFLYOXLJo867MDn32M7CX2RVxXccSo-uTTysvNj-QNhstCAncuaPbKPEN4aP5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/323953406a.mp4?token=sYfns4cZAVWj_RAI8vqqdbkz3bysXeR6DNyThuq-hJPIQhjUVqGqcGhJj2E3tfhQoNLF5J0Q0i4ljUgDY_mFgo2V0ENnOUsz6mOy0hlepncosw-kQy_2F12ikxrYzFqkW77uOLxV3cFreqx9oabo39htbxntK1wXJKUoKgH_0Ih_q7cMJKKmMpz_r725qmGVcnD6raPZR64G72IpKvvx33wFm5G4Wxqu-ppT8aqcSBTMiM-ytfikoxQ4CQl0aOMqtrq17nWqX404fay0NlMwmcXgyFLYOXLJo867MDn32M7CX2RVxXccSo-uTTysvNj-QNhstCAncuaPbKPEN4aP5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
اگر جمهوری‌خواهان کنترل مجلس نمایندگان و سنا را به دست بگیرند، به هر فرد بزرگسال پنج هزار دلار پرداخت خواهد شد؛ و ما می‌توانیم این کار را انجام دهیم.
دموکرات‌ها نمی‌توانند چنین کاری کنند، چون هیچ درآمدی ندارند و ما را به سمت رکود اقتصادی سوق خواهند داد؛ آن‌ها پولی در بساط نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72434" target="_blank">📅 22:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72433">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/979f299405.mp4?token=lRhl-cKAkCYsuSFEUaNaVPGtkaS46zcMzRNsqJzDHskPtDjt2f-JCNK7i5wdoGistufsaAlK-3QGkQS3etZCIh-IX8E07aXXEDT_bI1u9cb7ugbfaBpHo2e4Ka9x5vfK0htHyUQi-8Xa4xYkjIaRdX_f-O5dzQfvPh-AsRT_ekSnkM_sqwnN5yi5UZs2tHA6SH6hgPbl9C1ulvpBQYa-N0UpZYZqH2k3fTPaYPC-5nf9LkSWq5Fo4ogCpQ_k1K2WjRRG2lhWqpiWcRkaZe39FZSTXMMY7hVY_Fm_nmXow-mpAvfHJ40TqFWYQF1lciNiI9LgcGg2Ar-uzUILIN5NDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/979f299405.mp4?token=lRhl-cKAkCYsuSFEUaNaVPGtkaS46zcMzRNsqJzDHskPtDjt2f-JCNK7i5wdoGistufsaAlK-3QGkQS3etZCIh-IX8E07aXXEDT_bI1u9cb7ugbfaBpHo2e4Ka9x5vfK0htHyUQi-8Xa4xYkjIaRdX_f-O5dzQfvPh-AsRT_ekSnkM_sqwnN5yi5UZs2tHA6SH6hgPbl9C1ulvpBQYa-N0UpZYZqH2k3fTPaYPC-5nf9LkSWq5Fo4ogCpQ_k1K2WjRRG2lhWqpiWcRkaZe39FZSTXMMY7hVY_Fm_nmXow-mpAvfHJ40TqFWYQF1lciNiI9LgcGg2Ar-uzUILIN5NDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یستنیتیاساتتیاایایایایایایایتبتیتیایتتیتیابتیتبتیتبتیتیتنین</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72433" target="_blank">📅 21:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72432">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1l-R7juEe0n0-7kAhV4h2HXY3I2Y7Kq3sXPwdux79xbPeH_dzU2pSpm8JboMnMbyM52fB67xT-wMlP7cBNBVN7KXt-_5-uO6mZGK9fIqB1wIYEnsIzbFnivqUN1AREF3v6ewFizlWn5ZL3c6KYtfnzc3CgRW03wsNM7IdptxTQHMurPiZaf0XEYJOvGKrqT1_SNDkV0jCmTVj_jSilLXnohJ_ZLdHOJJud2NWm9NkrDy6FRl-IMxfc4Nyrx5WV_lS0yZlZ5-j7QPQVjAYGg2GLz79Ovc_r-CZGZdsVqLuj3U0auY71xOwN6iQk4u5qeZRD6lE88Tw_cMWlXXPK8HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
«عملیات طرد اقتصادی» باعث شده است ارزش ریال به پایین‌ترین حد تاریخی خود برسد.
ما به تضعیف توانایی رژیم ایران برای تأمین مالی تروریسم و توسعه سلاح هسته‌ای ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72432" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72431">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kf4YH3Js0JWwkL4dp2LmxhT5eW0uAvFQNTtUDsOH1TEukYbnu5Bs9TDy57gsb4Cev8dGzkJyig_yCzeQn0D3N0nU2mwxh7-_zzV54qJFDFU4aVf_-DgefVfhHLcOYBq28vxq4kRqCpj8uFmiPMO9uKprwVEcgm03imt7dcxuWspVH9GnXiCnzvDBxVZIjHjhsPYO8VErdvBWhR_CNRUtbfF9yGrhXxxFMiFocWJeOc7gJvPqXfWMHEiRdSQ56V8lETbOZartRxZNxe3inJjc8mn9Q6jybnRYHfqzWiEFEX8CgieiH49MYJosQwr77J7DKvkR9id7eFAk0g1PClA0_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک منبع آمریکاییِ دخیل در مذاکرات با ایران به العربیه گفت: احتمال دستیابی به توافق بسیار ناچیز است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72431" target="_blank">📅 20:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72430">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sw3XLJBSHa2P_YPzqSP429b2whJSF_vKbl2Ovo4HjDBTuf5XRWCDo7Gb71yZ1FYuFDOUTDtCcGJSRW-FByXL0YfWuUoPzp4jK3NQLRicbYu2xeCTJb9ItUzQWS7UuuSmjkB1-p0uPeeQ1rWP905_saiplBZR04RcS2nWslgSzflS15E8zV9O1WbBv_5FaLpEXEYSoqAKgOjsbi7Qnsv2JeyLZYv5CZugqFx0rSjKNhpUqdcSjlA8_1KFZhED5espq3dipE6xngiNTzw6Jf6EmvhCO56EMLlBKB_GLFQxxBf7TASqSypTnNQ-yiOqM_4cI7hfUm41dEvgFamVeb60jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام امریکایی به باراک راوید گفت:   رئیس‌جمهور ترامپ مایل است در ازای پیشرفت‌های ملموس در پرونده هسته‌ای، تحریم‌های ایران را کاهش دهد و وجوه مسدودشده را آزاد کند.  @News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72430" target="_blank">📅 20:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72429">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291ffe2bc9.mp4?token=GtEElVHH_H6eBygYT2V7UZ7-9lUfGLHN9G-vx695_53V8mnmQUjZpYYcGREoVAG6MFuDP-AVN7_8BXbyJttFefeulkWzJQm1UVDEPZ7J472NBEwS-endLMHkJKvVsgopQyq6hficqnITjQrl8Q79ZIjxjDvmFlzAyP8bEz4FfG4fWAnLWBPQv9vKnwEAZfWFhULa5aKOTYeUyF2z8CwK4xbS8hVZARxCBPJlq5zC_RWVVQXaqQGMEntXDsTlTpFlY-B-BiZG8E02J3Hwa-pfhHSp0bPJm5vqd15GVrw6YAJOK0p2zNszrOTUelU_2YYOvRYS1ivZ-VTLj0IBnVxxxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291ffe2bc9.mp4?token=GtEElVHH_H6eBygYT2V7UZ7-9lUfGLHN9G-vx695_53V8mnmQUjZpYYcGREoVAG6MFuDP-AVN7_8BXbyJttFefeulkWzJQm1UVDEPZ7J472NBEwS-endLMHkJKvVsgopQyq6hficqnITjQrl8Q79ZIjxjDvmFlzAyP8bEz4FfG4fWAnLWBPQv9vKnwEAZfWFhULa5aKOTYeUyF2z8CwK4xbS8hVZARxCBPJlq5zC_RWVVQXaqQGMEntXDsTlTpFlY-B-BiZG8E02J3Hwa-pfhHSp0bPJm5vqd15GVrw6YAJOK0p2zNszrOTUelU_2YYOvRYS1ivZ-VTLj0IBnVxxxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ساعتی پیش سرمایه دارای میلی گلد ریختن تو شرکت میلی گلد و رسما دارن مسولین شرکتو کتک میزنن و هر چی میبینن خرد میکنن و فقط صدای عربده و ناله از توی میلی گلد شنیده میشه :
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72429" target="_blank">📅 20:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72427">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یک مقام امریکایی به باراک راوید گفت:
رئیس‌جمهور ترامپ مایل است در ازای پیشرفت‌های ملموس در پرونده هسته‌ای، تحریم‌های ایران را کاهش دهد و وجوه مسدودشده را آزاد کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72427" target="_blank">📅 20:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72426">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سرعت آپلود بین‌الملل رو انقدر آوردن پایین که عملا دیگه نمی‌شه چیزیو تو تلگرام آپلود کرد!
#hjAly‌</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72426" target="_blank">📅 19:44 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
