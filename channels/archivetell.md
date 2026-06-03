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
<img src="https://cdn4.telesco.pe/file/AtKwh_4hBKPjendd2ecLivNb3WJ1or4l5qq5zLwLPLus3p-7nNFZtIQxb-x8_5z2zxrMUplMm0-b7jJ2btVd36YaUe-JYHpvla7Jbcs_WTiaacfQRc0TLuTpnI1nCk2QbkJQLbdrHW23kmI95y3M72l93A7Na3t4dtSLQaICRk5FJe4smyreuGhylyGAQYcIPHXL6AdtU48hevMX2RAlCUnLS3ev3luy_cw79aFoFZr4gedLb_l3xW5GOr2LDaOQSJHkhE3ZYmrl9XT0SXnuSehsU8hI_Y3QDiM7tSRrzPOHMaC7OVJoWqIVDvmrITpBZS_Z6sSz61snCqOH1Pl3mg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 8.93K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 15:47:09</div>
<hr>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aH3VrCFuJJhLS27zw0cAwIGGhkQ4ZvV9LsH0WpRkla-4-uj6e6srJ-zmP4vnD-7zpagt1rkYBjVlfWsQVoYj75bgKC92gUWWunVEZbmux7JRZ7XMLVRIu__e4CePIkj8cASGURz1wDNW03jZrgCA8fSRKVE3mWLwnq2n740sTBpKn9Cy9wQyGrGCHfp2lSMFT49XX75ie5e6pNFHzwcMCCQmwaAoQVZmNJW2CfjGUgseuaf2kHcWChOWaGG0QJR0uR0ItxHqi0wY4Y-Rjp_t3fNoIMmJYmS_b9c_zsV6JUnQGDR4IAmYtpA952DMs6-NFspIEtkijj-AwPGb8e2wJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت عکس نامحدود و رایگان
پشتیبانی از مدل‌های GPT Image، Gemini، Qwen و غیره، بدون نیاز به ثبت‌نام، کاملاً رایگان، بدون واترمارک.
https://freemake.cc
@ArchiveTell</div>
<div class="tg-footer">👁️ 485 · <a href="https://t.me/archivetell/5958" target="_blank">📅 15:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZNDbLvn0I9OPDlHw_3zGJjPw7eLr0pbZ66hxBHpls4p3MmBYBhEdILINp5S8oasK7qlLMxieoJ5D7D_-xiTnmWZ7dtlpGJk7fkllIEwWMDF-YXO8eqRglBgizwwrOcUV8y8gAx6yTs9HQfWD6c4cugOJorVVlf5ExQFXgh6M5w2LMzS6Wymp1KwnS-SKsecWHVbStCH-rO_FIDzwBD6Hlxx3l9V9la-8uMELYwgP7o6OQBHpsq22DKME9Ch1YBRaJ6BqyzatBA3B7KqXjR_nTKRkR3pna03c8D_VNSovey8QPdTowxa0WUpJtYA5PrFObjQNWzchMCVlMIXK5G-9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۱۱۰۴ ابزار هوش مصنوعی و ۶۲۴ پروژه متن‌باز
https://ai999999.top/
@ArchiveTell</div>
<div class="tg-footer">👁️ 632 · <a href="https://t.me/archivetell/5957" target="_blank">📅 15:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8404d116e.mp4?token=GCs8tUvWUG6Xe69J_8ZmriEHvdryRYq2lRADNsehCBS-9UWv4PvBU9zCajuYltNPBf_XanMDRTsvZeSEridvhxce96egJVvXU9OpmrRW8kwB2MOhwUkDaOUDhpStr6qsQyQa0UrgdYjE8xyx1hgmFIDGAzYq-YNJk9Bs_5htK5Amlb1-C6NQ5lqbiI6fwHnoLKZ7MJsR8PZVIWIskYV5ClL-YSDtNxVcsJk-Kv0qXsjqek_SXPpy6XcXQCRfIgxrMITsvuwIDsqlLj4VsBG6E7iKNLnjxRGsIlguwJ_OrOEBaCFlpvAJ8XCyfAYElWAXSoboxvJYBWLJXp0ZSunxog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8404d116e.mp4?token=GCs8tUvWUG6Xe69J_8ZmriEHvdryRYq2lRADNsehCBS-9UWv4PvBU9zCajuYltNPBf_XanMDRTsvZeSEridvhxce96egJVvXU9OpmrRW8kwB2MOhwUkDaOUDhpStr6qsQyQa0UrgdYjE8xyx1hgmFIDGAzYq-YNJk9Bs_5htK5Amlb1-C6NQ5lqbiI6fwHnoLKZ7MJsR8PZVIWIskYV5ClL-YSDtNxVcsJk-Kv0qXsjqek_SXPpy6XcXQCRfIgxrMITsvuwIDsqlLj4VsBG6E7iKNLnjxRGsIlguwJ_OrOEBaCFlpvAJ8XCyfAYElWAXSoboxvJYBWLJXp0ZSunxog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏰
WakeUpBroo — ساعت زنگ‌دار که شما را مجبور به بیدار شدن می‌کند
برنامه‌ای منتشر شده است بدون دکمه‌های «تعویق» و «خاموش کردن». برای قطع صدا باید کدی را از سایت وارد کنید — تا زمانی که به کامپیوتر برسید، خواب کاملاً از بین می‌رود.
چگونه کار می‌کند:
🔹
هیچ مصالحه‌ای وجود ندارد — فقط بلند می‌شوید و به سمت کامپیوتر می‌روید
🔹
کد برای قطع صدا در سایت تولید می‌شود — گوشی هوشمند کمکی نمی‌کند.
عالی برای کسانی که همیشه ساعت زنگ‌دار را عقب می‌اندازند.
لینک:
https://www.wakeupbroo.com/
@ArchiveTell</div>
<div class="tg-footer">👁️ 704 · <a href="https://t.me/archivetell/5956" target="_blank">📅 15:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b20169ea80.mp4?token=oHTK644LvB0qAaYW3r-9p2UYAjtOqTHw1sBu6NHYqeriMonxcR5bGWeNmSpFb0GPEw63yDTcoYqfi5Yj6Ebb7ofJMyMCaDQ4jBZVLINYB_JQDNyqBVqwTYQNRpaj3hsepZmiHgLLr_uqkAOj41m6FuFwWSiEA3snSuB2Hxn6_Y6Eg-_31N9yDS1e0tOwzpu6MMroeyxnvZiPZkBHpriRQgXMkx0hBMLwFc_pjq7eb7p8wmfj1gZsb_TEAYsRS4f9qrnhGPZwReCxE5wR1WTc6X74dTJ1RH2_gHE0HyoiE_D7wtlz65IswHfxMMNddj7oxw__FPd5tSHkcHmhGxrSkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b20169ea80.mp4?token=oHTK644LvB0qAaYW3r-9p2UYAjtOqTHw1sBu6NHYqeriMonxcR5bGWeNmSpFb0GPEw63yDTcoYqfi5Yj6Ebb7ofJMyMCaDQ4jBZVLINYB_JQDNyqBVqwTYQNRpaj3hsepZmiHgLLr_uqkAOj41m6FuFwWSiEA3snSuB2Hxn6_Y6Eg-_31N9yDS1e0tOwzpu6MMroeyxnvZiPZkBHpriRQgXMkx0hBMLwFc_pjq7eb7p8wmfj1gZsb_TEAYsRS4f9qrnhGPZwReCxE5wR1WTc6X74dTJ1RH2_gHE0HyoiE_D7wtlz65IswHfxMMNddj7oxw__FPd5tSHkcHmhGxrSkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه عوامل کدنویسی سلاح بودن
😁
Claude Opus 4.8 Ultracode
💀
@ArchiveTell</div>
<div class="tg-footer">👁️ 703 · <a href="https://t.me/archivetell/5955" target="_blank">📅 15:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ArchiveTel
pinned «
سرور اختصاصی 1000 گیگ اهدایی ادمین چنل:  vless://75700dda-3aa7-4f8e-b978-2237516f84db@45.130.125.66:443?mode=auto&path=%2F476T682e67a4f84a3c838ca94R86273&security=tls&alpn=h2&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPost…
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/5954" target="_blank">📅 12:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سرور اختصاصی 1000 گیگ اهدایی ادمین چنل:  vless://75700dda-3aa7-4f8e-b978-2237516f84db@45.130.125.66:443?mode=auto&path=%2F476T682e67a4f84a3c838ca94R86273&security=tls&alpn=h2&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPost…</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/archivetell/5953" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtlHvPAWaBZyQyIJFWuFbxWNTQygTIjQOBNtvk7Q25dp7De6OBFznjSr42ctCRmYo5HDrhO_YKB7wyt0PX6u_--bEOWCMBupEuVwLpvaEpiOwbyAedsYrZE7J3CS8bfbSpvH3Ik3zHiYIUhbSd2488RcwViEvSW2O0SrbDi7PLsBvMUmMjHcrOC-WDdyyv0pKji4IP-rBuW6bfIUya3eyhw7hXaYjAD7NXDcyhQRdBdkLdlzvD89Nr05KCO4LCNJEOjoocszVFDN0qWNlqni_gFsjaqJCs1aQKCNzSrmwgZXsz4ZSc8AqSWeg8E6D-MEXNVGYb9v5GaL3B-x1XuArg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🪗
می‌توانید اسپاتیفای را فراموش کنید — پلیر موبایل رایگان Metrolist را پیدا کرده‌ایم که دسترسی به موسیقی را بدون اشتراک و بدون تبلیغات فراهم می‌کند.
Metrolist چه کارهایی انجام می‌دهد:
🕤
موسیقی و کلیپ‌ را با کیفیت خوب پخش می‌کند.
🕤
موسیقی و لیست‌های پخش را برای گوش دادن بدون اینترنت ذخیره می‌کند.
🕤
بدون نیاز به احراز هویت اجباری کار می‌کند.
🕤
متن آهنگ‌ها را مستقیماً داخل برنامه ترجمه می‌کند.
🕤
امکان گوش دادن به موسیقی همراه با دوستان را فراهم می‌کند.
https://metrolist.cc/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/archivetell/5952" target="_blank">📅 12:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سرور اختصاصی 1000 گیگ اهدایی ادمین چنل:
vless://75700dda-3aa7-4f8e-b978-2237516f84db@45.130.125.66:443?mode=auto&path=%2F476T682e67a4f84a3c838ca94R86273&security=tls&alpn=h2&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%2210-50%22%2C%22xPaddingHeader%22%3A%22apinode%22%2C%22xPaddingKey%22%3A%22domow%22%2C%22xPaddingObfsMode%22%3Atrue%7D&insecure=0&host=ticket.fibernet1.qzz.io&fp=chrome&type=xhttp&allowInsecure=0#ArchiveFast
به عشق اسما
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/archivetell/5951" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">۱۵ گیگ کانفیگ اهدایی
⚡️
❤️
vless://4497c7f4-f6ac-4608-aa26-6948586470c3@94.183.157.63:2086?encryption=none&path=%2F&security=none&type=ws#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/archivetell/5949" target="_blank">📅 11:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">۱۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
ss://YWVzLTI1Ni1nY206WmpnM05URXdaVGMwWmpRMU16ZzBNVE0wWVdNMk4yWXpOak00T0RZeg@37.32.13.159:10112#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/archivetell/5948" target="_blank">📅 11:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">potato vpn آیفون
همراه اول
✅
https://apps.apple.com/us/app/vpn-free-vpn-potato/id1473774730
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/archivetell/5947" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YX1UABc3oO8y2lAGAoP6opSk8c-uPFi21WsbZFvZJxHgaxr1VZogwor6dW7kckgah9Q2myPeyMfjLnFyBPGkd0CUaYQlkRriW4254bQAxYbNGXVtkoDfyPLDGBc_NpR43Qj4tROdyr-3RKkyY25bimqxJiPzHA9ZoqzOvj6UO-zzQaaFnF2LqDvEELrw4JwfVC4WS9RcCW3lAku9Ab-LK66RsVAWPDnUR9h3nUSolW2SSuh5cHM6Q5wU792d_ZHtdlPCXPdcB4vUbq-8iO14INVrOzHlWWxP_3pOHshxP45tkKoHUsqmbd0OaXPOmgqyn00WtqiTmfW1TUfyvYhKgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KMW437wAsOmNBUJ6TIzPQwkB6de5KQxUxipCzfp7KVrPDin83BHnCH__vs_bQKX99c7HDpLeN-SC0lWttQYzYjT_FSHUPK18nLm2SlrutLvzrVBbG9cvagASaxNUAFVfP_3F0LfUsulk7_PSp6m9GakQEPKsOUsh9vru-GE1-GZR5JjXo_i4DyR3CJf3Xamf4lhTO8az_kzWdNPwVjTv4xiu2ypMlgzrNf9MmI2FlaIo6RytlBmiiFyEbrUpW-pPlQUVQRBeuAt6uukQkbW1yyhfgKIn5P_ydaTs8OdqxEOiCyTRyyvE4uZBpO128tDjdLMYnc3f2C2xkNIyEm5giw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Fair vpn
ایرانسل
✅
اگه سرور پرسرعت خواستین پینگ حتما زیر ۳۰۰ باشه .( اتصال به سرور دیگر) رو بزنین تا پینگ خوب رو پیدا کنین
✅
https://play.google.com/store/apps/details?id=fair.freevpn.vpnfair.fairvpn.fastvpn.proxy.vpn
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/archivetell/5945" target="_blank">📅 11:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">GoFly VPN
سامانتل و آپتل
✅
(اول با vpn برید سرورها بیان بالا )
https://play.google.com/store/apps/details?id=com.ambrose.overwall
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/archivetell/5944" target="_blank">📅 11:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یه کانفیگ از اینجا بگیرید. warp-generator.github.io/warp/‎ فرقی نداره کدومش باشه از Amnezia باشه فقط.  اندپوینتشو تغییر بدید به این 188.114.97.6:7281 بزنش داخل Amnezia WG با همراه و ایرانسل و مخابرات وصله.  @ArchiveTell</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/archivetell/5943" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRzFNGK6YS-IvyzWde1wvlY9aPtFcx0HTahaAWPAAvcgMi9EG5QoshtWe9Bmq8mgp24dpl0KsxepLWvPKlrMyUyav9V9Rclqmj8QPj_hVXaSefYid2-lU38ruxdTN7PDw07WhY-d_VVNGDr1qBNP2iitFTpMzGryA7KsDLlD2Lcx3gzxNlk5Wi3vJ_uGak1YUVmQIv1Ea9SGmynfJ75bV36feVJgoFpHWQ6ikOQhuAzmhLyaYBmQx5YwrcwlXsk83jNeWzbw9F44KovmaHoJh5DlV13mjsPEO9xWR8drNduiY4rLO227Ynep6KQNV2LTR2XWdZzok9s-7cUxrhWQJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Cybear vpn
ایرانسل
✅
https://play.google.com/store/apps/details?id=com.bear.vpn.super.fast.unlimited.connect
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/archivetell/5942" target="_blank">📅 10:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjpIIdYetxvXOG3b8u-yMKDvnFv97ldqLmGOW7QL8fRdSi6sOHcj1go4woQSS_J4MklWxARBMuryMn0xJxGhKeLtpMk9eWFQ9YKx8pIqy1YSZHryFDnObELZyKPdDNoHii-32pc9EOi6rckpsaRmEurIGfEnH3ZYkU8C6hrNVfIJnyigR05I6viEbZGHi8mgUgWgcnz45qxW54gGT4XqnTD4aGWhwkoM7vbjhG9jmvZaPf0pPN3ppqOPAkS4Blzml5Q1aCD_wUqhoBqB-t4nGndtt7G4Z_YKv2SiETs326dWo3zyFuaxSEEwCfR_m5i0_q-nWoNqowy8VKefwiCkrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Soren vpn
ایرانسل
✅
https://play.google.com/store/apps/details?id=com.provpn.soren
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/archivetell/5941" target="_blank">📅 10:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_3JGfykzCh21k2YeJ_UDPMl3d2uuQ5kkxxCI_unsSlcjP5wnqAQ9NFJ7vLtbctZbQol9LNduvxIXQ_s7ltXskQEJxYaNFiUofvX30SO-ZKCEkdjybfnraplHIFWg9yge3sH_t-ARVj2spsHwBwAPNMFs9xGZ2_QChpb87LhQPgmjyF0_YaHIkn3YIlC5nn6YiUGGXtTZaO64cQV3w5iEMM6OnLLbItTomQe3KqWkqAJlQKdeJWoJ6yPxQf2WiItEROSzy4tuGVNnm68NWJvvQbQTy-nQwMbEPHue-itjK4RbF7zszr2_J1GVteJx9-wbj8pO7cJXBLfgIAr7eR2LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥷
۱۳۸۷ تجزیه‌گر OSINT جمع‌آوری شده‌اند - یک کتابخانه جهانی برای تشخیص نشت، تجزیه و تحلیل شبکه و دستکاری داده‌ها.
🕤
شبکه‌های اجتماعی ، تلگرام و فراداده‌ ها.
🕤
جستجوی داخلی ابزارها.
🕤
به‌روزرسانی‌های مداوم.
🕤
دسترسی رایگان.
OSINT Tools
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/archivetell/5940" target="_blank">📅 09:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">https://hjfisher.github.io/SNISPF-HJ-Configurator/
انتشار configurator مخصوص SNISPF-HJ
تمامی تنظیمات رو می تونید اعمال کنید بدون هیچ سختی و خروجی بگیرید و استفاده کنید توی برنامه
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/archivetell/5939" target="_blank">📅 08:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🛡
معرفی SNISPF-HJ — نسخه پیشرفته‌تر SNISPF
🔗
لینک پروژه:
https://github.com/hjfisher/SNISPF-HJ
━━━━━━━━━━━━━━━━━━━━
⚡️
چه چیزی اضافه شده؟
━━━━━━━━━━━━━━━━━━━━
✅
پشتیبانی از چندین IP و چندین SNI به‌صورت همزمان
در نسخه اصلی فقط یه IP و یه SNI ثابت می‌شد تعریف کرد. اینجا می‌تونید لیست کامل بدید تا ابزار خودش بهترین ترکیب رو پیدا کنه.
✅
Health Check خودکار
هر ۳۰ ثانیه تمام ترکیب‌های (IP, SNI) تست می‌شن و اگه یه مسیر ضعیف یا مرده شد، اتوماتیک جایگزین می‌شه — بدون قطعی.
✅
انتخاب هوشمند مسیر (Weighted-Random)
به جای انتخاب تصادفی، ترکیب‌هایی که packet loss کمتری دارن شانس بیشتری برای انتخاب دارن.
✅
Graceful Rotation
وقتی یه مسیر ضعیف می‌شه، کانکشن‌های فعال قطع نمی‌شن — اول کارشون تموم می‌شه، بعد مسیر عوض می‌شه.
✅
همه قابلیت‌های نسخه اصلی حفظ شده
Fragment، Fake SNI، Combined، TTL Trick و Domain Checker همه دست‌نخورده‌ان.
━━━━━━━━━━━━━━━━━━━━
💻
نصب روی ویندوز
━━━━━━━━━━━━━━━━━━━━
۱. Python 3.8 یا بالاتر نصب کنید:
https://python.org/downloads
(تیک «Add Python to PATH» رو حتماً بزنید)
۲. در CMD یا PowerShell:
pip install git+https://github.com/hjfisher/SNISPF-HJ.git
۳. اجرا با کانفیگ پیش‌فرض:
snispf-hj --config config.json
یا برای دانلود کامل سورس:
git clone
https://github.com/hjfisher/SNISPF-HJ.git
cd SNISPF-HJ
pip install .
snispf-hj --info
━━━━━━━━━━━━━━━━━━━━
📌
نکته
بعد از اجرا، آدرس
127.0.0.1:40443
رو به عنوان پروکسی در v2ray، Xray یا هر کلاینت دیگه‌ای تنظیم کنید.
⭐️
اگه مفید بود، به پروژه ستاره بدید!
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/5938" target="_blank">📅 08:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://2ddbde64-5bed-4209-b0bf-6a3f090d198c@se.sanaz.online:20609?encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%2C%22scMaxEachPostBytes%22%3A%221000000%22%7D&fp=chrome&host=se.sanaz.online&mode=stream-one&path=%2Fstream&pbk=aVfj7ITwEFsWQP4YjFuM-FBb8PWmfBYOwKu_Ag8dVVI&security=reality&sid=d675939d&sni=www.yahoo.com&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/5937" target="_blank">📅 08:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromℳ𝓊ℎ𝒶𝓂𝓂𝒶𝒹</strong></div>
<div class="tg-text">ترامپ فردا:
من در کاخ سفید داشتم قدم میزدم ناگهان یک ایرانی از 300 متری به من سلام داد پس من تصمیم گرفتم به ایران 2 هفته مهلت بدهم
آنها آدم های فوق العاده باهوشی هستند ولی نباید سلاح هسته ای داشته باشند زیرا به محض تولید آن را بلافاصله به سوی اسرائیل شلیک خواهند کرد، فکر میکنم آنها میخواهند توافق کنند، به پاپ بگویید خاک تو سرت</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5936" target="_blank">📅 02:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85efdead3b.mp4?token=TkIbwgijX7-GssBvyBFgFYtTNqQAqufIa59ZxfugDHx3Y31FtO3gi46ddQgjQiQy3RoKhsi50VvGkBE7ssn5n8y6ply1X5vRYKgOfC6IeTxyW4CmQLlo7ELc3vFt47GPm8YI347J3ojT8nN8bF9KGd1oBH_Naf7iKMhY9Snq-6TSsU0Q3lveIlJN8FR5M5WKanZCDTi4WKkF0vA_TJrgcMh7kVYviz7Bm-7TN084oAMexDIoj-Dk_IvLlWKIl7TFAPjaOpW3e7RtmoGSbu4g8sPvhWgbx2i_ddAaYU26b0wln_YOxdFUXBaLVBuqhxNZO5_VmrDiBjQieI3PevapZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85efdead3b.mp4?token=TkIbwgijX7-GssBvyBFgFYtTNqQAqufIa59ZxfugDHx3Y31FtO3gi46ddQgjQiQy3RoKhsi50VvGkBE7ssn5n8y6ply1X5vRYKgOfC6IeTxyW4CmQLlo7ELc3vFt47GPm8YI347J3ojT8nN8bF9KGd1oBH_Naf7iKMhY9Snq-6TSsU0Q3lveIlJN8FR5M5WKanZCDTi4WKkF0vA_TJrgcMh7kVYviz7Bm-7TN084oAMexDIoj-Dk_IvLlWKIl7TFAPjaOpW3e7RtmoGSbu4g8sPvhWgbx2i_ddAaYU26b0wln_YOxdFUXBaLVBuqhxNZO5_VmrDiBjQieI3PevapZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/5935" target="_blank">📅 02:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وضعیت الان کانفیگ فروشا:</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/5934" target="_blank">📅 02:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">امشب شب طولانیه🫪</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/5933" target="_blank">📅 02:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5932">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cc42fd82.mp4?token=UBd5YRuqqtverKmKh67iHXwjLOSQXI5yenF4nAPCf5FTUk1dovtX82RLAJZ5b0jAYNtAlPAcSS0yvUuPapVkcfQU0CHoFRG6hB8yyK-YT2N-4M8t0GdQ0w2fig5b7vPu8G4teP1rqMVvPn4jD27FBWdWcLWAn9CZ5YuHFcKoz153gxiC1PP_k5ypYRwGYQduqW705ql9D1S_E6WBoLSBhnFeFPnPdk8zgIeEUKbdM7rA37-PsyJvKzGSaW_rtQbInj7Bd1NIEwCnk4DMqmFU83lfjxQdaG0D8dIxwUmCTqPk7if6_l103aToD_f6lkM8VO9sMY5GVIZatdRiROutNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cc42fd82.mp4?token=UBd5YRuqqtverKmKh67iHXwjLOSQXI5yenF4nAPCf5FTUk1dovtX82RLAJZ5b0jAYNtAlPAcSS0yvUuPapVkcfQU0CHoFRG6hB8yyK-YT2N-4M8t0GdQ0w2fig5b7vPu8G4teP1rqMVvPn4jD27FBWdWcLWAn9CZ5YuHFcKoz153gxiC1PP_k5ypYRwGYQduqW705ql9D1S_E6WBoLSBhnFeFPnPdk8zgIeEUKbdM7rA37-PsyJvKzGSaW_rtQbInj7Bd1NIEwCnk4DMqmFU83lfjxQdaG0D8dIxwUmCTqPk7if6_l103aToD_f6lkM8VO9sMY5GVIZatdRiROutNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/5932" target="_blank">📅 02:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985e567cda.mp4?token=pO_U3xNOtKESa0hVc-2esBZlQMeuz0DX15aBa1zBU-5uClHqRX0ldFI-MuiH78cHNQJQccUYzTyW06n7tXS-Ymybr1gE0pylXdx1wZbl3L06lkSLz7AMWIrCsWM9XCGyzBNTN6HzJW3cj_b1ZX7pcbORdDYLtB7n-Vq-WFfT9q7GQWfjsxfjoNdoBztbuBN6VuuRek8Ab21G1NBQ7KyHAmzgHFQQg2OVfsUkS9IOs4Ya5jEH6GYFK3sOrRDxhhGjhgAANvO5gSzMhhAqxahaLMHgREOKgEuQz3UqVV88Fe9kuOPFDAURoRoSy18cxFM2ZWXZAGlLRrrrb7ZktT3b2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985e567cda.mp4?token=pO_U3xNOtKESa0hVc-2esBZlQMeuz0DX15aBa1zBU-5uClHqRX0ldFI-MuiH78cHNQJQccUYzTyW06n7tXS-Ymybr1gE0pylXdx1wZbl3L06lkSLz7AMWIrCsWM9XCGyzBNTN6HzJW3cj_b1ZX7pcbORdDYLtB7n-Vq-WFfT9q7GQWfjsxfjoNdoBztbuBN6VuuRek8Ab21G1NBQ7KyHAmzgHFQQg2OVfsUkS9IOs4Ya5jEH6GYFK3sOrRDxhhGjhgAANvO5gSzMhhAqxahaLMHgREOKgEuQz3UqVV88Fe9kuOPFDAURoRoSy18cxFM2ZWXZAGlLRrrrb7ZktT3b2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/5931" target="_blank">📅 02:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یه بالستیک که این حرفا رو نداره...  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/5930" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یه بالستیک که این حرفا رو نداره...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/5929" target="_blank">📅 01:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">IObit Uninstaller Pro 15
License type: 6-month
Platform: Windows
License code:
2F93C-7EB9A-0BFB7-0B6TE
146D0-5E924-04007-088TE
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/5928" target="_blank">📅 01:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">100 گیگ مولتی لوکیشن
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@greblox.forum:443?mode=gun&security=reality&encryption=none&authority=greblox.forum&pbk=Tb21e9Z3rtr5NoprXQQtcqLLRZOgIVyIbuZmqPJkGXM&fp=firefox&type=grpc&serviceName=grpc&sni=greblox.forum&sid=c4cb37f029af5828#%F0%9F%87%B3%F0%9F%87%B1%20Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@crope.top:443?security=reality&encryption=none&pbk=Xgq8hNKvlfsBVHeJtXwjytbB5Fv2Tnu7vXJdZOgS8ig&headerType=none&fp=chrome&type=tcp&flow=xtls-rprx-vision&sni=crope.top&sid=b5af336756f77990#%F0%9F%87%B3%F0%9F%87%B1%20Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@birch.gouher.one:443?mode=auto&path=%2F&security=reality&encryption=none&pbk=y_1jLoCup4gdKlQHsw6rj0FiPX0Mt6cyg2w1bIR9ris&host=stream.greenfield.lol&fp=random&type=xhttp&sni=birch.gouher.one&sid=28e92c6d545c9c26#%F0%9F%87%B3%F0%9F%87%B1Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@meadow.pinevalley.top:443?security=reality&encryption=none&pbk=JfUgtIVRM26EKkksroAENXLWNJp9n28mSG-z-8CDAHc&headerType=none&fp=chrome&type=tcp&flow=xtls-rprx-vision&sni=meadow.pinevalley.top&sid=e86995a2ccab9364#%F0%9F%87%BA%F0%9F%87%B8%20USA
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@rouze.click:443?mode=gun&security=reality&encryption=none&authority=rouze.click&pbk=PqunTCzbpHjmqH97ZpXHL0RBMyHaFzjJAO8i3uHr-XE&fp=chrome&type=grpc&serviceName=grpc&sni=rouze.click&sid=7fcb3d98608f93b6#%F0%9F%87%B3%F0%9F%87%B1%20Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@berry.riverpath.live:443?mode=auto&path=%2F&security=reality&encryption=none&pbk=y_1jLoCup4gdKlQHsw6rj0FiPX0Mt6cyg2w1bIR9ris&fp=qq&type=xhttp&sni=berry.riverpath.live&sid=bdf09e70262b409c#%F0%9F%87%A7%F0%9F%87%AABelgium
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@road.oakvalley.digital:443?security=reality&encryption=none&pbk=rkgs3hpc8oIb2gCtzdy0AnD2AD2LkhtArGzTDDjcPnU&headerType=none&fp=qq&type=tcp&flow=xtls-rprx-vision&sni=road.oakvalley.digital&sid=54aafe829679e92f#%F0%9F%87%B5%F0%9F%87%B1Poland
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@stone.quietgrove.forum:443?mode=gun&security=reality&encryption=none&authority=stone.quietgrove.forum&pbk=MchbHn3bpJaqAX-oqnNXYiXrbUTN0n-K203T8YGr8D4&fp=chrome&type=grpc&serviceName=grpc&sni=stone.quietgrove.forum&sid=0ae20b3e5e2c0bc2#%F0%9F%87%BA%F0%9F%87%B8%20USA
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@flame.quietgarden.live:443?mode=gun&security=reality&encryption=none&pbk=fzbtjP1MtR9JYN-pKDJQTWB9I-V_EPEgdteL76Ed5yA&fp=random&type=grpc&serviceName=grpc&sni=flame.quietgarden.live&sid=06d7e21ecb57367a#%F0%9F%87%A9%F0%9F%87%AAGermany
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@ember.quietgarden.live:443?mode=gun&security=reality&encryption=none&pbk=fzbtjP1MtR9JYN-pKDJQTWB9I-V_EPEgdteL76Ed5yA&fp=random&type=grpc&serviceName=grpc&sni=ember.quietgarden.live&sid=fd488ee90cc0b9eb#%F0%9F%87%B3%F0%9F%87%B1Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@valley.syrniki-iz-samokata.live:443?mode=gun&security=reality&encryption=none&pbk=euMfJzUx3qAGiaXwcvAXqXiqglBQKPOqxkTdSqwnqEw&fp=qq&type=grpc&serviceName=grpc&sni=valley.syrniki-iz-samokata.live&sid=c6046d150f597d04#%F0%9F%87%B5%F0%9F%87%B1Poland
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@field.wildgarden.digital:443?mode=gun&security=reality&encryption=none&pbk=dtxZ0lFLHE0IGfg45g2t1t7WwHWHuDW4xbfww3zKhDQ&fp=random&type=grpc&serviceName=grpc-bridge&sni=field.wildgarden.digital&sid=bbbbe9607d343bb6#%F0%9F%87%B3%F0%9F%87%B1%20Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@bridge.oakvalley.digital:443?security=reality&encryption=none&pbk=rkgs3hpc8oIb2gCtzdy0AnD2AD2LkhtArGzTDDjcPnU&headerType=none&fp=chrome&type=tcp&flow=xtls-rprx-vision&sni=bridge.oakvalley.digital&sid=5278abf8d6d75483#%F0%9F%87%B9%F0%9F%87%B7Turkey
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@eveningwalk.sunnyside.city:443?security=reality&encryption=none&pbk=rkgs3hpc8oIb2gCtzdy0AnD2AD2LkhtArGzTDDjcPnU&headerType=none&fp=qq&type=tcp&flow=xtls-rprx-vision&sni=eveningwalk.sunnyside.city&sid=54aafe829679e92f#%F0%9F%87%BA%F0%9F%87%B8USA</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/5926" target="_blank">📅 00:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">10 گیگ مولتی لوکیشن (حتما ساب کپی کرده و وارد کنید)
https://cdn-biz.ru/sub/1/0588b70e-0b61-4e10-8d34-e83e8968cfd5
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/5925" target="_blank">📅 00:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">۲۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
لوکیشن ترکیه ، همراه اول هم وصله..
vless://b9dccdab-0f77-4fb7-8949-4d378e92df5c@cdn4.greewebservices.ir:2095?encryption=none&host=turpanel2cdn.consolegamenet.ir&path=%2F&security=none&type=httpupgrade#@ArchiveTell%20%F0%9F%87%B9%F0%9F%87%B7
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/5924" target="_blank">📅 00:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
فوری؛ آمریکا چهار صرافی بزرگ ایرانی نوبیتکس، بیت‌پین، رمزینکس و والکس رو تحریم کرد.</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/5923" target="_blank">📅 00:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
فوری؛ آمریکا چهار صرافی بزرگ ایرانی نوبیتکس، بیت‌پین، رمزینکس و والکس رو تحریم کرد.</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/5922" target="_blank">📅 23:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">۲۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://b9dccdab-0f77-4fb7-8949-4d378e92df5c@areal1.greewebservices.ir:2425?encryption=none&fp=chrome&pbk=xQnXh5EfPDhcEBB7rRiLca33GYrMEeUa35domLL_yA8&security=reality&sid=9b60d3&sni=yahoo.com&type=tcp#@ArchiveTell%20%F0%9F%87%A9%F0%9F%87%AA
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/5921" target="_blank">📅 23:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کدام مدل‌های هوش مصنوعی روی دستگاه شما قابل اجرا هستند؟
یک ابزار آنلاین که به کاربران کمک می‌کند بر اساس مدل GPU به سرعت بررسی کنند کدام مدل‌های هوش مصنوعی را می‌توانند به صورت محلی اجرا کنند.
https://www.canirun.ai/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/5920" target="_blank">📅 22:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">۲۰ گیگ
⚡️
vless://2ddbde64-5bed-4209-b0bf-6a3f090d198c@se.sanaz.online:20609?encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%2C%22scMaxEachPostBytes%22%3A%221000000%22%7D&fp=chrome&host=se.sanaz.online&mode=stream-one&path=%2Fstream&pbk=aVfj7ITwEFsWQP4YjFuM-FBb8PWmfBYOwKu_Ag8dVVI&security=reality&sid=d675939d&sni=www.yahoo.com&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/5919" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Re2__YIOM9ttYqiJwe_DkVsr9uSp82aMwyDYisOs_-1gJm8RH1FygQTwURQH4V63FIFvgTL6n3BrmC-TDaXO0rw8lOJXPBd9Cf-adUusCc4H-ogRCxAKbg5zCxu_d9GNepwP8diQl_sjNtjzjvIiFYrpoGH16CF9T7wKgbhRrgZU82-lAU1lA0rK8M1FDGOdoPKHol_oIJvGS7yr7tqPkYdHPJKNplyqGLeFfyKTeZtNZ78RQul30LQPWzVLISKat-FhAfVvwksqfd_XUhEdn46lJKg8UKbZk2ebzI0mkNr_Nr-6FhPZl4p47L1CaSO4VX1ZFIgHCqDgxdUoWMhh0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚒️
۱۳۰ ابزار که جایگزین تمام نرم‌افزارهای اداری می‌شوند: آفیس، ورد و پاورپوینت. همه چیز مستقیماً در مرورگر کار می‌کند، بدون نیاز به نصب و محدودیت.
در مجموعه:
🕤
ویرایشگرهای تصاویر.
🕤
ابزارهایی برای PDF، ZIP، CSV، Excel و فرمت‌های دیگر.
🕤
تبدیل فایل‌ها بین ده‌ها پسوند.
🕤
فشرده‌سازی تصاویر.
🕤
فرمت‌بندی و پردازش کد.
🕤
کار با صدا و فایل‌های صوتی.
🕤
ضبط صفحه نمایش.
🕤
ابزارهای متنی.
🕤
برنامه‌ها و چت‌های هوش مصنوعی.
🕤
ابزارهای ریاضی، فنی و داده‌ای.
https://github.com/aghyad97/browserytools#-features
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/5917" target="_blank">📅 21:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">VideoNote: ابزار یادداشت‌برداری و قالب‌بندی محتوای ویدئویی
یک ابزار یادداشت‌برداری ویدئویی کاملاً محلی که می‌تواند محتوای ویدئو را خلاصه کرده و یادداشت‌ها را قالب‌بندی کند.
https://github.com/xiaokeaijqx/VideoNote
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/5915" target="_blank">📅 20:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uAYbLB5yCvA6i12EFoPll2QeWMDGSnOORRvWMcJ7iLMEnSG1x2Ff-hkcveqBLYMITnc-tka_tEeRQvDXqDvBZJ1HjG8QDwQEk1HXynUMpUeYufHMB_nj-y9eMgqqFdUJ_u_8-7H1jabhkZ2vf1plBUkGJUFIrclNJL2c_8_44ul2fc8cWlQqCfB4Ivnw3O6uv5_IOsoQPfm8Cp6vt2EQB8GJU9UgvO8yQrhZAuP-8pG4ypLJooR9f4klKlr48YxB7I0MlIBTami5rrlRiVoGsCbv-T_MRcei4fVVQvAdlq7PvJKw8Zd82M1EMHW6fnw1W4yTLw2GCJLPYiagnSb1aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k7wyymBqTQ_M97WvaLg5yJ88U6woC8XBjAAUgWuBkxCJGKWxmHVaJFCxNCD5G_2UlvVGEyCaETfvpXGCIAvx3JbhOZURA5rRqmc9f_WyoWciBx2c7wHjXzbashGRWncEplgMCBBsJDdbZ4LK4lYvMI_U3bRX5im9wSwekl873po7SOec00hSduSy-GeEude073BBXNBqyFqsfXNrK9YM1fgAGo5ujS32-iFMZzMR0M_Vxm8v4_TFRZzEe39f8LR_e1BLiNcEThluvytJCBOuIjZjjOrr1FoYucTx7odqeN9gsILNXykOLHRBEQz3VZ4JtL4T3Ued0peTFyw9oxOYOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت عکس و ویدئو رایگان
https://www.mindvideo.ai/creative-studio/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/5913" target="_blank">📅 20:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پروکسی اهدایی یکی از ممبرای عزیز کانال
😎
❤️
https://t.me/proxy?server=47.86.102.135&port=443&secret=dd887aa96cd9b760d42f62217afdcc6bc5
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/5912" target="_blank">📅 19:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvjDRcGjcSjjpjF9oAUZ3YaMad_8_RmvoiJfM2-y00fODRIeCk8UlxdhXb4eNNe8adQZWyOiaagxjpNxDWBzX4850gyxusLORUViFcHTs1qggf_Ig_ecqj5RtW4ghig7-kGcuL97sEtxJOSA1uJwhhnm_AcbvGXhpadyYuREhHQBoeY1I2SweTpts3ZhcQZgyAJsEq2BV_YhkUUWKhKK5yOs64t2uLjHgfjnEWtAQ0bPFcZkfVVq5NDpSXVl1OQh5xfH-T8qKmGzveRVFK-3upS21jRIFUZnkiwqDrKoO8tuRLuJtQMYTvUm97rw3vR0cqTOyU6u89c3rf3ZPnpY1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
ویندوز 11 را تا حداکثر توان ارتقا می‌دهیم
1️⃣
بهترین نسخه‌های ویندوز 11.
🕤
Flibustier 25H2
ایده‌آل برای استفاده روزمره.
🕤
Revision Group 25H2
حداکثر FPS ، مناسب گیم.
🕤
Ghost Spectre 25H2
فوق‌العاده سبک که حداکثر بهره را از سخت‌افزار می‌گیرد.
2️⃣
حذف زباله‌ها و قابلیت‌های اضافی.
🕤
Remove Windows AI
حذف هوش مصنوعی که منابع را مصرف می‌کند.
🕤
Win11 Debloat
حذف برنامه‌های پیش‌فرض.
🕤
Ultimate Tweaker
بیشتر از ۲۰۰ تغییر در یک ابزار کوچک.
🕤
Open Hardware Monitor
کنترل کامل بر سخت‌افزار
3️⃣
نرم‌افزاری که بدون آن ویندوز 11 دردسر است
🕤
WizTree
— بالاخره می‌بینیم فضای دیسک کجا می‌رود.
🕤
Revo Uninstaller
— برنامه‌ها را بدون باقی‌ماندن رد حذف می‌کند.
🕤
TaskExplorer
— مدیر وظیفه با قدرت بیشتر.
🕤
Explorer++
— مرورگری که واقعاً راحت است.
4️⃣
ظاهر و راحتی استفاده
🕤
Windhawk
—
مدهایی برای بازی ها
🕤
Jax Core
— پک‌های بصری و ویجت‌ها.
🕤
Seelen UI
— سفارشی‌سازی عمیق  رابط کاربری.
🕤
Cursor Mania
— هزاران نشانگر موس برای هر سلیقه.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/5911" target="_blank">📅 19:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ارائه‌دهنده سرویس‌های پرسرعت، امن و بدون قطعی اینترنت
🚀
| خرید و تحویل آنی | پشتیبانی اختصاصی
🛡
کانال: @ArchiveTell https://t.me/ArchiveTellbot</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/5910" target="_blank">📅 18:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ارائه‌دهنده سرویس‌های پرسرعت، امن و بدون قطعی اینترنت
🚀
| خرید و تحویل آنی | پشتیبانی اختصاصی
🛡
کانال:
@ArchiveTell
https://t.me/ArchiveTellbot</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/5909" target="_blank">📅 18:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">۲۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://3617290e-f2e0-4eb5-9576-a610aa6f2c95@104.167.199.23:80?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fp=chrome&host=104.167.199.23&mode=auto&path=%2Fmohraz&pbk=wtVFe9j0FtOMtxUBKJqjd7NZs9-47lsjbnUlWq_MGEs&security=reality&sid=26a4&sni=www.samsung.com&type=xhttp#@ArchiveTell
https://104.167.199.23:2096/sub/ugqvbxg55h1u87rw
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/5907" target="_blank">📅 18:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FG1yKAjZuenJbQx8sX5_uQX9QFAIEDQAfVXSHpM5BckO4CDTY3EJO2LNscsYOmraBpih4lqQ_cOux4b_qQ9Tc_GHqk-AEH5yCCwjS6xjTmIO2KJk_km_oHRKQdVjaE_qAodtdCC7--aZoIE-nyNKbdl2XsnPPwmjrckshAjPWr8ScqSedYmO0hDc5jAbS_SgeDBbEEY08XovgTS2jM3aZ182qUNVw8FBiW6Gg9Vhdlajq5GEER1dZnAqn84Q6m9vvtIY2vAJ9rYNUUXc3puQ9t4pR-Mj3OznS2hI1HUhIA_GJyeKS5wNfsT8rhNzUSF_D7tEKcrLvKsgwD6pHcUFrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نابغه ها قبلا ی چاره دیگری هم اندیشیده بودن پرایوسی سکسی</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/5904" target="_blank">📅 18:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">https://obito.96s.ir:2096/sub/cqx44nj2vnu1mebr
لینک ساب 50 گیگ ...
@Sina_1090</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/5903" target="_blank">📅 18:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🖥
ویندوز ۱۱ از تمام برنامه‌های غیرضروری پاک شده است - نابغه‌ها یک نسخه رایگان از این سیستم عامل را ایجاد کرده‌اند که ۲.۳ گیگابایت حجم دارد.  آنها موارد زیر را حذف کرده‌اند:
🕤
Xbox Center.
🕤
Windows Update.
🕤
Windows Defender.
🕤
Weather، Office، Solitaire و سایر…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/5902" target="_blank">📅 18:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_ibZy6hL9bq2w30p2m5bt2PeFFkd9vU-N0HtNEoiTL6nHwL6bBvhJRdmK4__G4w-w8kzX7jdN_B8coigk7G5khWvG2Rx0OMgEcnkt1GDNHwZw5ptSJzOl3fA_EABENszYTxYUQiUq6uesiq90f0l__0B2bGrKsTWwWJwMbUgiEmnyAUkX11N5A90dRJBf-viLc4V4Ioe6Mht0g_eyofP81CDuYKz4_Nra2pK0oMoqOOmWo9k_Pu-dDsFcySw7J7PEWzXx3yMV9OoGoS6zGZNN2KEXuVpMf9rcMNtRPJ3xMSoAASoU4c7Ei2OirRwgl_tmqhHenUCsX9BZvENsLMIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
ویندوز ۱۱ از تمام برنامه‌های غیرضروری پاک شده است - نابغه‌ها یک نسخه رایگان از این سیستم عامل را ایجاد کرده‌اند که ۲.۳ گیگابایت حجم دارد.
آنها موارد زیر را حذف کرده‌اند:
🕤
Xbox Center.
🕤
Windows Update.
🕤
Windows Defender.
🕤
Weather، Office، Solitaire و سایر برنامه‌های داخلی.
🕤
اکثر درایورها (فقط ضروری‌ترین آنها باقی مانده‌اند).
🕤
Microsoft Edge و Internet Explorer.
http://github.com/ntdevlabs/nano11
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/5901" target="_blank">📅 18:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تولیدکننده ویدئوی تصویری هوش مصنوعی
ابزار آنلاین برای تبدیل تصاویر محصول، پرتره، پوستر و سایر تصاویر ثابت به ویدئوهای کوتاه، پشتیبانی از چندین جریان کاری و کنترل دوربین، مناسب برای صفحات محصول، تبلیغات و تولید محتوای شبکه‌های اجتماعی.
https://image-to-video-ai.best/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/5900" target="_blank">📅 17:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">https://185.211.101.214:2096/sub/2f6ve5e7v0qim80w
سابلینک 50 گیگ ....
با نت های مختلف تست کنید...
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/5899" target="_blank">📅 17:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jLQh87T8xMfEeTMv94p5tQOouVeoZrJtIqNUmTj9aYoJE1eJwBBMYBzr1uZE6LkYDG9dEUW04iMrzXiiF79zwRhiJpI0P_5HQa2VRjJ0wT5EpABRoEg9dZ5ZVSvFeK_gew_uNo8Dg6YKq0d3rnpuofJ6ptloTN0zGzhLs1eoCPRh2yPcGi1AfgjbAUiAk2q9iQ8ZO3oqsG_V4ZU8sClCbNYB5C87mdYwHTooqKJo9Xh2P_3LcTA5l7rfNiDrhGLieBav4cMa0co-3l74wnzJo0y6IG-ZGWKsqNiL15SlrjYCWHpEyeEOJHWyFsI_T6u9cp0YftluhGTXyVWPOgUnFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uop5ZFNO0mTzVOG5KVxYcusDns89Vt5Qbh_MCje2jmgTFGTUy6UMmIP07Vc8zYB9P5eKBoUBaoYNB4LZZLLVaEpZznuGPXaaNESrGQk3uYj2wNyVN8nangiZuPwY6zuoE9iff8q4SovPKlOx-JhZ8I89Hisl8LtnZ2dDVGeCOEgovqs_-we8gdMF0o1oQgMKtJyMu4C7-sEISlVN9G4a1rocWwgdM_SdyTvmkC7nxqBq1dcU6CnpmRGFvoK40HUmCruwcavVXwpskyXfnrHUVK1_Tn6AltVBkb6P-y9b2rjre03UOVCNt37ZcDpjZOy1D98sQHlaepga1VQ2I_MM2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">https://khan.shompolexy.shop:2096/sub/tvhnms3g1zjuotay
سابلینک ۱۰۰ گیگ اینترنت
با همراه اول هم وصله..
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/5897" target="_blank">📅 17:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">Gemini Omni تولیدکننده ویدئوی هوش مصنوعی رایگان
پشتیبانی از ورودی متن، تصویر، صدا و ویدئو، قابلیت تولید کلیپ‌های ویدئویی با کیفیت سینمایی
https://omniaipro.app/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/archivetell/5894" target="_blank">📅 17:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0b6BI-95oTHYy9aGB7_cOZQF_DWpSnUam0nmfFIGVZmjyV3YRRz-8X2yWklOIb4yXVDHJHm6dB-KQSuqbE29Ffyr8Up-BWfVfeKgMzhQ_MKVB-JLJB-AdftoX5zCjioBysgD8wTyrTAa1waAF12dYtLFjOZSeutxVGKmRz80AjUawIL-8DvWib2WeLJwjX-9KUozvCbcvpvo6cDrr8utdMfmur36ZgAq0c8l1cdajzKKsbVZXNGuJevdGq87Kwim_GY2VJYrzA3lbUN5v-sUPtr_-jLtVdPolS5fZz2a59BXXPGgiTjsK2FWdIRdApvOkp1A3nUcJonVR4iYt9MXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">slipnet-enc://AVYDFT1SX5QRahOVGapvCIQOi5iX+F+Ayz7d82kXBzKUgbDFGOsXcyY12oASii0n3Ye5Fj9LOHfyxzQpTH6aZzsHCccHQuHa78SADfbTQRNENnLD6CeHOuPxRffHOjkB+5tHdtQ89Kfk8TzpeVOxfFMxXDMxDhTuX7D/hrMsm9KchoxYpj3l1HNlOSDSMkO6td9WttjNX/TrOGk9jSX3n+bBnR1t64wJs9TYIUUycW/wKH9ntwehzsQ0l7MkpkxjVGD4Qqx8G/AGiOGcqy0OHxb4WsNfWIvP+mR1UcoObW2qJCMqPvMmimZQGTCI0cHIbpH1Kx0GLVXI9USz59N6D+2py/TLS4sGIKK40X2xohmjXthNyo3zcIw20FmuSnV8Dez5RVaSAbUhuCY8Iqa5G/B9U2PmqAMcZSVUh+yr4IoK/7Uelbj4rUAT6SfYQlZiliDE6Wkx7eM5dd8rR2Zxmtjl/Lr1X/qtrMeQgbJ5w5QAlxmAltcolUJt3BH58ZOqpwTe</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/5893" target="_blank">📅 17:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">OBITO.conf</div>
  <div class="tg-doc-extra">530 B</div>
</div>
<a href="https://t.me/archivetell/5892" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@Sina_1090</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/5892" target="_blank">📅 17:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-obito.conf</div>
  <div class="tg-doc-extra">532 B</div>
</div>
<a href="https://t.me/archivetell/5891" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@Sina_1090</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/5891" target="_blank">📅 17:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">هر کی دلش وایرگارد میخواد
دست بالا کنه....؟!
@Sina_1090</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/5890" target="_blank">📅 16:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">100GB مولتی لوکیشن
vless://d49eb175-facd-4c33-b1be-32c746701184@maple.cloudureld.com:443?security=reality&encryption=none&pbk=-VM1_ol58XU8fQHPvCnllupmpqyI6E1_bp6vpD6hD0w&headerType=none&fp=qq&type=tcp&flow=xtls-rprx-vision&sni=maple.cloudureld.com&sid=7e52de801e7c71de#%F0%9F%87%A8%F0%9F%87%A6%40ArchiveTell
vless://d49eb175-facd-4c33-b1be-32c746701184@island.cloudureld.com:443?mode=auto&path=%2F&security=reality&encryption=none&pbk=U-aI9goYn0iGJ31emKZ1ltON45Ry0LjCl15MnumMD2c&fp=qq&type=xhttp&sni=island.cloudureld.com&sid=a7f9e69f037466b1#%F0%9F%87%AC%F0%9F%87%A7%40ArchiveTell
vless://d49eb175-facd-4c33-b1be-32c746701184@greblox.forum:443?mode=gun&security=reality&encryption=none&authority=greblox.forum&pbk=Tb21e9Z3rtr5NoprXQQtcqLLRZOgIVyIbuZmqPJkGXM&fp=firefox&type=grpc&serviceName=grpc&sni=greblox.forum&sid=9e327f04ce93c187#%F0%9F%87%B3%F0%9F%87%B1%20%40ArchiveTell
vless://d49eb175-facd-4c33-b1be-32c746701184@developer.projectauths.com:443?mode=auto&path=%2F&security=reality&encryption=none&pbk=U-aI9goYn0iGJ31emKZ1ltON45Ry0LjCl15MnumMD2c&host=developer.projectauths.com&fp=random&type=xhttp&sni=developer.projectauths.com&sid=68d14e7adba07698#%F0%9F%87%B3%F0%9F%87%B1%40ArchiveTell
vless://d49eb175-facd-4c33-b1be-32c746701184@dev.projectauths.com:443?mode=auto&path=%2F&security=reality&encryption=none&pbk=U-aI9goYn0iGJ31emKZ1ltON45Ry0LjCl15MnumMD2c&host=dev.projectauths.com&fp=random&type=xhttp&sni=dev.projectauths.com&sid=8a9d1d8916227e5b#%F0%9F%87%A9%F0%9F%87%AA%40ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/5889" target="_blank">📅 16:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOI11ClNsiGOLcaspRehzwm2quBDNbaozjnyMSMT5xEj4pVgqm7HDoFhDtzqRUYhHzNIEdwnhxoptfbzK1abV3ppXmDqVGuiOAYvpQbukXMo8LxjqYQydzsMUrAYiYRAAH1AwUvxVtokkwcZ5hgMrUlveD8tO8eGcbd0LRYg7fbFYVsT8s9yORegTowMtjedF2u_tBDpXJydaSnk3Rr6wiqUyk_sifzLz2sn4vUNztRxbqLCZdhdvsUiLWj3GIffNs4XBXSbthHY1EtrU4SRsAyUthoo7QyABT3MVjua7Ao3NYbhFMvfjKqLVk0ctHcS_HvoJb8I7uzck7OlsnMMtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطوری اندپوینت endpoint برای
کانفیگای وارپ
اسکن کنیم
داخل لینوکس یا ترموکس این رو بزنید
pkg update -y && pkg upgrade -y && pkg install curl -y
bash <(curl -fsSL https://raw.githubusercontent.com/bia-pain-bache/BPB-Warp-Scanner/main/install.sh)
به سوالاتی که میپرسه جواب بدین میگه چندتا اسکن کنم یا سریع باشه یا نرمال. ipv4 رو انتخاب کنید
دقت کنید که اسکن باید بدون فیلتر انجام بشه. اگه فایلش واستون دانلود نمیشه فقط قسمت دانلود فایل رو با فیلترشکن انجام بدین بعد قطع کنید و اسکن کنید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/5888" target="_blank">📅 15:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5887">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">۱۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://3617290e-f2e0-4eb5-9576-a610aa6f2c95@104.167.199.23:80?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fp=chrome&host=104.167.199.23&mode=auto&path=%2Fmohraz&pbk=wtVFe9j0FtOMtxUBKJqjd7NZs9-47lsjbnUlWq_MGEs&security=reality&sid=a99c6c05&sni=www.samsung.com&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/5887" target="_blank">📅 14:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">vless://cc074e81-342d-402c-9fa6-fa907728222a@85.198.20.217:80?type=tcp&encryption=none&security=none#tunnel%2050gb
50gb tunnel
تست شده بر روی : ایرانسل , سامانتل , رایتل , اپتل , مخابرات
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/5886" target="_blank">📅 14:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یه کانفیگ از اینجا بگیرید. warp-generator.github.io/warp/‎ فرقی نداره کدومش باشه از Amnezia باشه فقط.  اندپوینتشو تغییر بدید به این 188.114.97.6:7281 بزنش داخل Amnezia WG با همراه و ایرانسل و مخابرات وصله.  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/5885" target="_blank">📅 14:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یه کانفیگ از اینجا بگیرید.
warp-generator.github.io/warp/
‎
فرقی نداره کدومش باشه از Amnezia باشه فقط.
اندپوینتشو تغییر بدید به این
188.114.97.6:7281
بزنش داخل Amnezia WG
با همراه و ایرانسل و مخابرات وصله.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/5884" target="_blank">📅 14:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ابزار خط‌فرمان دور زدن DPI روی همه پلتفرم‌ها — با pool تطبیقی چند-IP/چند-SNI
به‌جای یک upstream ثابت، ابزار به‌طور مداوم ترکیب‌های (IP، SNI) را بررسی می‌کند و هر اتصال را از طریق سالم‌ترین جفت هدایت می‌کند — بدون قطع شدن اتصال‌های فعال.
روی Windows، macOS، Linux و Android (Termux) کار می‌کند و برای روش پیش‌فرض نیازی به دسترسی root ندارد.
روش نصب
git clone
https://github.com/hjfisher/SNI-Spoofing-HJ.git
cd SNI-Spoofing-HJ
pip install .
snispf-hj --info
https://github.com/hjfisher/SNISPF-HJ
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/5883" target="_blank">📅 14:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0023e0a6bf.mp4?token=tJIvteWopSFZz5NILPEtu4nwrIu80s7LQ7Ncn0RmoyIQRKf827AdUmneyY4_X21q40t7FAKcIQxdfKjt0XCRE9kNQVSgRltdPVHnZpE_lNrS-cXZb9qCoOtGHa99SSLKJ7KJMF0_1c2JQyQPFkTs1T5Ectwof2t5Wsasca5k4nKWXjJCGP30LTw5JogF4R0MO8kHzZ9aB0Xz073yVite6ihuyafjhcoKfwoeJkaBquY_zFR8m7R0jW8oduxgkFvy77XLaL6TNoglC6YTaNT-dd6m2Wf2DKV5jzaKaagS5V8M3yXv8dKa7YIXpl7kSZ7F8gINbHFeD2XvJaK51zqmfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0023e0a6bf.mp4?token=tJIvteWopSFZz5NILPEtu4nwrIu80s7LQ7Ncn0RmoyIQRKf827AdUmneyY4_X21q40t7FAKcIQxdfKjt0XCRE9kNQVSgRltdPVHnZpE_lNrS-cXZb9qCoOtGHa99SSLKJ7KJMF0_1c2JQyQPFkTs1T5Ectwof2t5Wsasca5k4nKWXjJCGP30LTw5JogF4R0MO8kHzZ9aB0Xz073yVite6ihuyafjhcoKfwoeJkaBquY_zFR8m7R0jW8oduxgkFvy77XLaL6TNoglC6YTaNT-dd6m2Wf2DKV5jzaKaagS5V8M3yXv8dKa7YIXpl7kSZ7F8gINbHFeD2XvJaK51zqmfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
قاتل ChatGPT و Claude از PewDiePie جامعه هوش مصنوعی را منفجر کرد: مخزن Odysseus تنها در دو روز تقریباً ۲۵٬۰۰۰ ستاره در GitHub جمع‌آوری کرد و حتی Anthropic نیز به این پروژه علاقه نشان داد.
این جایگزینی برای چت‌بات‌های شرکتی است که بدون محدودیت و نظارت ساخته شده است. Odysseus پاسخ OpenAI، گوگل و دیگر غول‌های صنعت است.
چرا این پروژه اینقدر سروصدا به پا کرده است:
🕤
راه‌اندازی روی کامپیوتر یا سرور — بدون حساب کاربری.
🕤
تمام داده‌ها در اختیار مالک باقی می‌مانند.
🕤
عامل‌های داخلی: مرور وب، ویرایش فایل‌ها، تحلیل اسناد، مرتب‌سازی ایمیل‌ها و غیره.
🕤
پشتیبانی از تحقیقات عمیق.
🕤
API برای اتصال مدل‌های محلی.
🕤
رابط کاربری آسان و کار با گوشی هوشمند.
🕤
امکان کار آفلاین.
https://github.com/pewdiepie-archdaemon/odysseus
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/5882" target="_blank">📅 14:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">vless://fec5f560-7e78-4b71-9432-418621738d3f@snapp.ir:80?encryption=none&host=netrox.cnxman.ir&path=%2F&security=none&type=ws#netrox%20--tunnel1gb
1 گیگ تانل
تست کنید با ری اکت بگید</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/5881" target="_blank">📅 13:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">۲۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😁
❤️
ایرانسل تست شده ، بقیه نتا وصل بود استفاده کنید..
vless://3638b964-5404-4145-b19c-89f7cc8c237b@31.56.229.237:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=rT-KdyGuCqbP8c-CilgD2sSWMkSSLe8xbEeRNxypsSk&security=reality&sid=57e7bd&sni=www.amazon.com&type=tcp#@ArchiveTell%2020.00GB%F0%9F%93%8A
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/5880" target="_blank">📅 12:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اینترنت امروز فقط برای من خرابه یا نه  همه اوپراتور ها یا پینگ یا 1-</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/5879" target="_blank">📅 12:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کانفیگ نامحدود اهدایی یکی از ممبرای عزیز کانال
⚡️
❤️
trojan://4bdbapq0n755s7cr@168.222.43.197:48309?host=168.222.43.197&path=%2FEmpty&security=none&type=ws#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/5878" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اینترنت امروز فقط برای من خرابه یا نه
همه اوپراتور ها یا پینگ یا 1-</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/5877" target="_blank">📅 12:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">۵۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://81a1e8f2-3b97-41e5-8c60-7d7d1576e028@185.92.181.217:80?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fp=chrome&host=185.92.181.217&mode=auto&path=%2Fmohraz&pbk=SqXIQC6Q68_mpLX_JVFXLHwCeSLHpyk5JhKvrd1P7DA&security=reality&sid=bbe112&sni=www.nvidia.com&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/5876" target="_blank">📅 12:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5875">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCx_E4s1zj-EqxNhRHpwTFZoeXnXfH81aUnQhrneQ_QDd-W0Y1sUwWnPwWlC5QWue-j7VOFoY5vLrYCNIQgHyM4OIN75aFvICE7L4QCYYK_L1WPMuxB0bo7NeerDNBxD-t5Fjy5GJk-zgH_gd4gyZCMm3hhu1KnB-IwtrrmKCmS9rBxNHq7RlYO3HzZ47VTmktPn871QR9p8AW5lFxmP9HjwowTrAEDucon4HYDgAfGUIjORCiw3LHY9iHMxTXY3_XOElYuqsVZ5qI6yoHxQc0bxxWankgdE1T1z7UgTZ2hVV87qQ95lP2ZuNHPqwdoZFd2JriVmHGOnn3RS5RJkWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌏
یادگیری زبان از طریق دیالوگ‌های زنده با هوش مصنوعی — PrettyPolly، سرویسی برای کسانی که به خوبی می‌خوانند و زبان خارجی را می‌فهمند اما در مکالمه معمولی دچار مشکل می‌شوند.
🕤
هم‌صحبت هوش مصنوعی برای تمرین مکالمه — می‌توانید بدون خجالت و ترس از اشتباه، زبان انگلیسی و زبان‌های دیگر را تمرین کنید.
🕤
سناریوهای آماده برای گفتگو — سفر، مصاحبه‌ها، مکالمات روزمره، صحبت‌های کوتاه و موقعیت‌های واقعی دیگر.
🕤
کمک در حین گفتگو — ترجمه، راهنمایی و تصحیح عبارات به صورت آنی در دسترس است.
🕤
بررسی پس از مکالمه — سرویس اشتباهات، نقاط ضعف و کلماتی که باید تکرار شوند را نشان می‌دهد.
🕤
سیستم حفظ پیشرفت — عبارات جدید را می‌توان تثبیت کرد و به تدریج در تمرین‌ها تقویت نمود.
http://prettypolly.app/app
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/5875" target="_blank">📅 12:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2e603b0b.mp4?token=YtLk8runteEhoSJYibfNqTXR_Dipp7efAS4v5S1zACSvFy52KSyPE9oop-DOrH5qrpJ5DpZd4D_XKUx7rT56g9Y0_iTMtpD5IknuNT6p1KsKP1KwDevYGNfsoDw0Cna-TptEXCn3RQZL7xDi59RT5FrzeUCGRwz9D-K8yBdW9y7bJAXvT9GiRfYHSOWGO2X_Wdu0T8tzLB4FFhDY05nLoPCNxL645UN_YiwUsZDp58erLYsq4T1hvOFKK2C0qrRnCLG7xd_H5kYTJXBXkK83rdAnxU3BhXTVkXcB43EazBA1rtI_T0kvCFVTuQ5tRuwrDyKgtMdO0khHRHKx6OlD6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2e603b0b.mp4?token=YtLk8runteEhoSJYibfNqTXR_Dipp7efAS4v5S1zACSvFy52KSyPE9oop-DOrH5qrpJ5DpZd4D_XKUx7rT56g9Y0_iTMtpD5IknuNT6p1KsKP1KwDevYGNfsoDw0Cna-TptEXCn3RQZL7xDi59RT5FrzeUCGRwz9D-K8yBdW9y7bJAXvT9GiRfYHSOWGO2X_Wdu0T8tzLB4FFhDY05nLoPCNxL645UN_YiwUsZDp58erLYsq4T1hvOFKK2C0qrRnCLG7xd_H5kYTJXBXkK83rdAnxU3BhXTVkXcB43EazBA1rtI_T0kvCFVTuQ5tRuwrDyKgtMdO0khHRHKx6OlD6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل راهنمای رسمی پرامپت‌نویسی در Gemini Omni را منتشر کرد
در راهنما چیزهای بسیار جالبی وجود دارد: کنترل دوربین از طریق اصطلاحات حرفه‌ای (dolly zoom، locked off، oner)، همگام‌سازی نور ساختمان با موسیقی، تولید ویدئو بر اساس استوری‌بورد، تغییر سبک با حفظ حرکت، ترکیب ویدئو، تصویر و صدا در یک پرامپت.
نکته کلیدی: کوتاه بنویسید چه می‌خواهید. نیازی به شرح هر فریم نیست.
https://deepmind.google/models/gemini-omni/prompt-guide/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/archivetell/5874" target="_blank">📅 12:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">۱۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
https://cdn.mozcloud.ir/XS_AZ/cue4q8rhm47n4120
بدون فیلترشکن از بخش اسکنر استفاده کنید و بهترین گزینه رو اعمال و کپی کنید
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/5873" target="_blank">📅 11:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">AVG Secure VPN  Code:AAUNB7-KK3HT2-4Z4J56  @ArchiveTell | 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/5872" target="_blank">📅 11:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5871">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">۱۶۰ گیگ پروکسی اهدایی یکی از ممبرای عزیز کانال
😁
❤️
https://t.me/proxy?server=hdi.mahdii-coder.eu.cc&port=443&secret=dde9a1ae9b1c4ff69a688d03b7257db653
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/5871" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://2ddbde64-5bed-4209-b0bf-6a3f090d198c@se.sanaz.online:20609?encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%2C%22scMaxEachPostBytes%22%3A%221000000%22%7D&fp=chrome&host=se.sanaz.online&mode=stream-one&path=%2Fstream&pbk=aVfj7ITwEFsWQP4YjFuM-FBb8PWmfBYOwKu_Ag8dVVI&security=reality&sid=d675939d&sni=www.yahoo.com&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/5870" target="_blank">📅 11:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚀
حالا تقریباً هر کسی می‌تواند اولین اپ خودش را بسازد!
دیگر برنامه‌نویسی فقط حفظ کردن کدها و سینتکس‌ها نیست؛ مهم‌تر از همه این است که بتوانی دقیق توضیح بدهی چه می‌خواهی.
🤖
📱
گوشی اندرویدی را به لپ‌تاپ وصل کن، Cursor یا Windsurf یا VS Code AI را باز کن و ایده‌ات را بنویس. هوش مصنوعی بخش زیادی از کار را انجام می‌دهد و نتیجه را مستقیم روی گوشی خودت تست می‌کنی.
💰
مثال:
یک اپ مدیریت هزینه‌های شخصی که آفلاین کار کند، هزینه‌ها را دسته‌بندی کند و آمار روزانه، هفتگی و ماهانه بدهد.
🛠
مراحل:
🔹
گزینه USB Debugging را فعال کن
🔹
گوشی را به لپ‌تاپ وصل کن
🔹
پروژه را با Expo اجرا کن
🔹
خطاها را برای AI بفرست تا رفعشان کند
🔹
نسخه نهایی را روی گوشی نصب کن
💡
ایده‌هایی برای شروع:
✅
ردیاب عادت‌های روزانه
✅
فلش‌کارت درسی
✅
تایمر تمرین ورزشی
✅
اپ یادداشت شخصی
✅
مدیریت مشتریان (Mini CRM)
✅
برنامه‌ریز محتوای تلگرام
🔥
نکته مهم:
امروز لازم نیست از روز اول یک برنامه‌نویس حرفه‌ای باشی. کافی است مشکلت را بشناسی، ایده‌ات را توضیح بدهی و با کمک AI اولین ابزار کاربردی خودت را بسازی.
🌍
دوران جدیدی شروع شده؛ جایی که ساختن نرم‌افزار از همیشه در دسترس‌تر است.
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/5869" target="_blank">📅 11:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5868">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">AVG Secure VPN
Code:
AAUNB7-KK3HT2-4Z4J56
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/5868" target="_blank">📅 10:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5867">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8axqvEh3ZSxFKwwJhcFgc18-ae2RscN5dgaXp3ah2zr58WpFEfxld3J0aV7OVmZxFzwNKYKMEnWvh7WO6dgfaY_GZhdscFFZQryPzZjHT2wd1Z4i50fGJ3xmvq9w8m_Fm_t-0YmU7I0wXUoWhezpDwddV0-w-Sg5QqIpyuh2a4BrjLHdiBtM97e85T3L2cONWBkRlNEiQ_58VcAA4s5LI1JucuG00qk_SmQScMa8glAs-7B0n8AMl0QpaUPCIkc_0_P0K7tfytKBfrkqOyzMVpH04kReD7j_7XUwvq3-jM9Sy9jN6yxz7Zl2hLeLK4wihOBYBSbSwl6W4w1mxf8MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✴️
استایل‌های سفارشی در Krea 2 اکنون برای همه باز شده‌اند
Krea LoRA را برای مدل جدید خود عرضه کرده است، بنابراین می‌توانید آن را با استایل، شخصیت یا شیء خود آموزش دهید و سپس در تولید استفاده کنید.
قبلاً این ویژگی به صورت بتا برای Max و Business بود، اما اکنون دسترسی گسترده‌تر شده است.
https://www.krea.ai/image/k2-large?style=y45oxkkdp
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/5867" target="_blank">📅 09:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://2ddbde64-5bed-4209-b0bf-6a3f090d198c@se.sanaz.online:20609?encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%2C%22scMaxEachPostBytes%22%3A%221000000%22%7D&fp=chrome&host=se.sanaz.online&mode=stream-one&path=%2Fstream&pbk=aVfj7ITwEFsWQP4YjFuM-FBb8PWmfBYOwKu_Ag8dVVI&security=reality&sid=d675939d&sni=www.yahoo.com&type=xhttp#@ArchiveTell_@Lozkc
کانفیگ پینگ پایین منطقه ای
اگ وصل نشد خاموش و روشن کنید احتمالا درست شه چون شبکه باگ میخوره گاها
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/5866" target="_blank">📅 09:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMDrUzlsKIOAKgCp4MTDiAMidpp0rBnkH5Qq3GPl-13O3X2AvPuhUQdZgbrdxvPnbtMR6YOzFGZnYTgmdv3ADITfNvgYANJZMvYkOtumOfKOF9g3wy03YGMs4sbH54aYf921NYTdRBNs--8276ZZbXzE20GNjKqx0ZuTD85QAAQPZ8DRF0AGYv-dPsDE0fUbMZYMhqWJq9x0vHqA_TAsbNU3lBTCdLMiliNxzz_vm7ysQD7w74YGgN0EExrexUnrnk2Px0nOx8NaXi89BhCxSI_2LzpkdHGCrX13cHdaUWE9cs8VJgWZO4-F9YqkdH8BLAe54y8PmhQDtzzd3adEaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
ما در حال ارتقای Gemini به حداکثر هستیم - افزونه‌ی Voyager را پیدا کردیم که ویژگی‌هایی را که در ابتدا فاقد آن بود، اضافه می‌کند. مناسب برای کاربران AI Studio و کاربران معمولی:
🕤
حذف واترمارک از تصاویر.
🕤
مدیریت پیشرفته‌ی چت: حذف دسته‌ای چت‌ها، نقل قول پاسخ‌ها، انتخاب مدل پیش‌فرض و موارد دیگر.
🕤
به شما امکان می‌دهد پوشه‌هایی برای مکالمات با همگام‌سازی از طریق Google Drive ایجاد کنید.
🕤
به شما امکان می‌دهد پیام‌های مورد علاقه را ذخیره کرده و از آنها در Gemini، AI Studio و سایر وب‌سایت‌ها استفاده کنید.
🕤
جدول زمانی راحت: در پاسخ‌ها، رشته‌های مکالمه و پیام‌های مورد علاقه حرکت کنید.
🕤
Markdown، نمودارها و چارت‌ها را به خوبی رندر می‌کند.
🕤
مکالمات را به PDF، Markdown و JSON تبدیل می‌کند.
🕤
تاریخچه‌ی افکار را از Deep Research استخراج می‌کند.
🕤
در Chrome، Edge، Firefox و Safari کار می‌کند.
https://voyager.nagi.fun/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/5865" target="_blank">📅 09:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uLzxEWA-9v91RLR8DRiTnI0R_6by0I94xrNp07mzuzNbazBmiF6Ir11nVexdEpP-1UjOhWTRrLBwyIWXIYzNY5iVXmi-TAR_QfAs1xbBuUKMCPevD1o4-uKY4Il9t6CJWL2Cfb0NiZQgP8Ze_Gg5ejW1wH6yefr_alutPrCADb30178dkpt8OStH94J8CTiDTjG3RmD3OoT1Bo--ya2oSwk-czGN1inolN0fuezHJoODHECvuPSfOaOFO5RTlUclr5QV_CJH5ObddFZgYU67YooXHMeU1mtELKxVpmOR1xFydAraE0Ho3lQSdSZLZ6miJYGte0A5gi_uJZFiaGcFXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r7smlWStUYhjRDtuivaykwqwUmhfD1SC-NsBnSsyxzTq0Mq5Qit3G8n-QCQcNUtTP_d8xIGRdpQE7LZbGr-8OQbz62d973O7SB6l_lRpjXmSMwfCkJ-wbF2YCwioZBh-joSzi4gW9uMxXnW8Hsb7nyIekrfxIhcPBlQTZ8Ktdsl5La1SLCz4hA2g76qBe4c9NjBnaJ7fKr8xr5yWlByIsuiqyPNkfANJLe0zYgbS7YkyJ4KP3kY1ZENyloIlo-aIYGmE9zjQh3Tt16Kc7-jcgFgr-RdXFQlQpKXlUzsjcwxzYKKQm6h7wwpkVZmxms4vtw8JSHOtYhKtE1mGvyWVYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXdgTEtWY3-KAWa8wwkO6yqdgzpVFfTfsS__4KVIOFLj8Ji0N77Hjys6CvHz_mdWHb44orIHS3peUm_D724QxiH55NvmVm6RVp9o4kDi5Le7LqYDA_EDF8bs66Znxy1kRf4OxreOxBYodGX9FUTyRoLDzWnybaH_WkyEL4HF1BcPTUAFi2emH63eXvJuvXn42pWBAG6qL3HZAYQV45zTLPTQYJ3Hcvkfy8tS8LPsDwBrUurGka7C2Htx4wSPCch1M2up1mRKSRVgOmI5YmizkHy9a8AdtaGNaIAvVuQxIPG4Wjm7zTDGuP02dQcDHHH3Gyn0z3ZOV6vePMtsB1aVHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">منبع بی نظیر بازی های PSP
@Ppssppiso2025
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/5862" target="_blank">📅 09:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/InOm_oGZuCsowAmz2zSuqu_kge-rHibpHeFIMdZRgaPxr7gMrcNzni9QlIk6alecnNF32JC0-hcs_QxvirkIhUJpfN3u_pDLPvdKefEPGE6YV1RcS_TWkTMWz-3ejNrD-Gp5q8Koulnhi3mNVfdLjoJC293lSjygbbo7mNeB_9OPtxJy8LipGyY_T6lBCBJxGbL2OIi8rJrx9qbkd25bPZpNu61PbB7xhkZC7OwWaRIy76pLv7iRPv1eOPmjyCU8ylvjkSR-Ll6k3p3aHqXA9AyufJdL1RzgDLSes_HNSeheJZ0dXRWmgAKVo5aCQj6gtoA1Ii1iotEpNrI_XiYUQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c71fUm7OjnOBUwr5-QvLvTa4P8OwlIc7bO2g0N3JI6Ejes8RUFDytulZNs7qg7U9635KdTFJVK2Fj3pkQLjJjjicAEvk5-leruxpDdzcQADHsVPtwpLMnu42KJ4nT-dbSV2uv1qVOug7BpO3PUuHcGVtqc8e6gcrAYhNzlBl8-WTBkWikllIKtwWfNYrKlc30GbSs1BwIWSapLfU2vT3k3EalFvb9ZtcKCkDdQsGJAjKK5LviarI5WPWN_qfGvddj26m0_b7WYlCk9--JQLZQ8LIZRiZSjj5OkzsQXK_qpayJz-GuOJUMSIKVSdXT2s58K-6FmM7KrBO9HvJw-GaHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎮
اکنون می‌توان PSP را مستقیماً در مرورگر اجرا کرد — یک علاقه‌مند نسخه وب شبیه‌ساز افسانه‌ای PPSSPP را منتشر کرده است.
🕤
همه چیز بسیار ساده کار می‌کند: سایت را باز می‌کنیم، فایل ISO بازی را بارگذاری می‌کنیم و در عرض چند ثانیه بازی را بدون نصب نرم‌افزار جداگانه اجرا می‌کنیم.
🕤
رابط کاربری تقریباً کاملاً مشابه PPSSPP معمولی است، پشتیبانی از گیم‌پدها و بارگذاری بازی‌ها مستقیماً از دستگاه وجود دارد.
🕤
God of War، Tekken 6، GTA: Vice City Stories و دیگر بازی‌های محبوب به راحتی روی کامپیوتر، تبلت و گوشی‌های هوشمند اجرا می‌شوند
https://root-hunter.github.io/ppsspp-web/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/5860" target="_blank">📅 08:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اپن سورسه پروژه
البته باید کدش بررسی بشه
ولی شدیدا روونه
و کلا انگار ی اپ دیگه اس
😂
خیلی خوشگله
در کل جای کار داره و ابتدای کارشه پروژه ولی خیلی باحاله
اپشنای خوبیم داره بررسی کنین</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/5859" target="_blank">📅 03:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMonoGram</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">monogram-arm64-v8a-0.1.0-release.apk</div>
  <div class="tg-doc-extra">49.1 MB</div>
</div>
<a href="https://t.me/archivetell/5855" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/5855" target="_blank">📅 03:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RefZ04cTUbpajrrn2cJ6m2hUiRTjZ7YhTSvn1CQobUaJjjk8xB5qCU9MedQwwMeiOHxfuprRN3zvDSR5CHvPvEtjgYrJYlF1IbOl3uaTqL0Sbd3X1i93Bcp3Mpu04IIysZV6Jr0UcZgayfXFj0f2m-GH_RFNJasL35dSyQeDrvZLtkuiMbKsiI0HAjM9BCNhXiJEd93dkN0WUe1ROTnmufwZ5YHGJgd58J1ohUnHelwmZ1vWuvlxbhijPYgcEzhraKy3MoYWsZjIuofAiqDM2wbNtwvXxrlb7nABE5ITs0CE9Qu_B6Kv4pr7TprKBDeKDGuj6F6U3gRClBUPg_1V1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛠️
MonoGram؛ یک کلاینت متن‌باز و مستقل برای تلگرام
MonoGram یک اپلیکیشن غیررسمی تلگرام برای اندروید است که برخلاف بسیاری از کلاینت‌ها، از صفر و بر پایه TDLib توسعه داده شده و فورک نسخه رسمی نیست.
✨
ویژگی‌ها:
• رابط کاربری مدرن با Material 3
• عملکرد سریع و روان
• قفل بیومتریک و ذخیره‌سازی امن
• پشتیبانی از جستجوی داخل چت
• مدیریت بهتر فایل‌ها، رسانه‌ها و استیکرها
• متن‌باز و قابل بررسی توسط همه
📌
توسعه‌دهندگان اعلام کرده‌اند که MonoGram روی تجربه پیام‌رسانی، طراحی مدرن و عملکرد بهینه تمرکز دارد و قابلیت‌های NFT و کریپتویی تلگرام را اضافه نخواهد کرد.
این پروژه هنوز در حال توسعه فعال است، اما با انتشار نسخه 0.1.0 امکانات و پایداری آن نسبت به قبل به‌طور محسوسی بهتر شده است.
🔗
GitHub:
https://github.com/monogram-android/monogram
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/5854" target="_blank">📅 03:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">100GB
⚡
vless://29f8120c-fa78-4b20-b5a5-5390d9cfbbc9@greblox.forum:443?mode=gun&security=reality&encryption=none&authority=greblox.forum&pbk=Tb21e9Z3rtr5NoprXQQtcqLLRZOgIVyIbuZmqPJkGXM&fp=firefox&type=grpc&serviceName=grpc&sni=greblox.forum&sid=a28e08feb9324fb0#%F0%9F%87%B3%F0%9F%87%B1%40ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/5853" target="_blank">📅 03:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇫🇷
ss://YWVzLTI1Ni1nY206ZjRlN2NjM2ItMWZkZS00ODYxLTlhN2UtMjk0NzI4ZDhhMTZh@51.195.235.71:2083#%F0%9F%87%AB%F0%9F%87%B7%20%40ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/5852" target="_blank">📅 03:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⚡️
چینی‌ها از Qwen3.7-Plus رونمایی کردند؛ یک مدل چندوجهی و Agent محور جدید!
🤖
شرکت Alibaba مدل جدید
Qwen3.7-Plus
را معرفی کرده؛ یک مدل چندوجهی (Multimodal) که بینایی و زبان را در یک معماری واحد ترکیب می‌کند و برای اجرای وظایف پیچیده طراحی شده است.
🔥
قابلیت‌های کلیدی:
🔹
فعالیت به‌عنوان یک Agent کامل در محیط‌های GUI و CLI
🔹
تحلیل همزمان تصاویر و متن
🔹
کمک به برنامه‌نویسی و انجام وظایف بهره‌وری
🔹
پشتیبانی از ورودی‌های چندفرمتی
🔹
درک تصاویر، استدلال روی آن‌ها و ارجاع پاسخ‌ها به اشیای مشخص
🔹
استفاده از جستجو برای افزایش دقت پاسخ‌ها
🔹
سازگاری با فریمورک‌های مختلف Agent
💡
به زبان ساده، Qwen3.7-Plus فقط یک چت‌بات نیست؛ بلکه یک Agent چندرسانه‌ای است که می‌تواند تصویر ببیند، متن تحلیل کند، کد بنویسد و در محیط‌های مختلف عملیاتی شود.
📌
این مدل از طریق API در Alibaba Cloud Model Studio در دسترس قرار گرفته است.
🔗
وبلاگ معرفی:
https://qwen.ai/blog?id=qwen3.7-plus
🔗
نسخه آزمایشی:
https://chat.qwen.ai/?models=qwen3.7-plus
🔗
مستندات API:
https://modelstudio.console.alibabacloud.com/
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/5851" target="_blank">📅 00:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5850">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyofAfbYldfwrMs0Mk0OiJmnUxJ9eIoQcO0-CfVIaH2IhUrxtoOjAhQhOUKsIu6ZeX1g-ATdJruUq_IjKG_4M1059BU6y982FAK4R5uif9RikMi6GE8MtBIONkY8byGvTKrM3VWWaAeif79ME5BYoQg5lS4sPin2RjQ4YCCo0y29ZWnVV-Z_PlJIIN0dWz2bPdmgszxlbdqY5-xKE-NOP2ESGLnbibH-OW2qeHNiUomLByXjxpLhAAhjqAxzRh2nc2eqzet9FEiCBHpk_cgH8s5-XRznAiLfS5kr0KFiVY_hqjZHjdG2Ett4NIjhgXzaem303F5YObiShS_ilw8isg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Golazo پخش زنده متنی فوتبال
⚽️
فوتبال را مستقیماً از طریق ترمینال تماشا کنید
https://github.com/0xjuanma/golazo
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/5850" target="_blank">📅 23:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترجمه پیام Void Verge: از زمانی که اینترنت ایران توسط دولت بازگشایی شد، تغییرات گسترده‌ای در سراسر شبکه داخلی کشور در حال رخ دادن است. پس از هفته‌ها قطعی، تقریباً تمام روش‌هایی که در آن دوره استفاده می‌شد، مستندسازی شده و به مقامات تحویل داده شده است. سیستم فیلترینگ در حال آماده‌سازی برای مرحله بعدی قطعی‌هاست. روش‌هایی مانند DNS tunneling، MITM و Domain Fronting قطعاً در قطعی‌های آینده دیگر کار نخواهند کرد.
علاوه بر این، مقامات فیلترینگ گام‌های مهمی برای ایجاد ارائه‌دهندگان واسط برداشته‌اند که خدمات خارجی را با محدودیت‌های شدید به ایرانیان ارائه می‌دهند، یا وب‌سایت‌های ضروری را که نمی‌توانند از روش‌های قبلی استفاده کنند، NAT می‌کنند.
در این شرایط، انتشار علنی و عمومی روش‌ها هیچ فایده‌ای ندارد جز اینکه کار مقامات فیلترینگ را آسان‌تر کند. این مکانیزم باید زیر رادار عمل کند — به صورت سورس‌بسته و بی‌صدا.
در عین حال، مافیای اینترنت ایران قدرت بیشتری پیدا کرده است — مافیایی متشکل از افرادی با دسترسی به «اینترنت سفید»، ISPها و دیتاسنترهایی که فروش اینترنت نامحدود به فروشندگان VPN را با قیمت صدها میلیون تومان از طریق مکانیزم‌هایی مانند سرویس‌های پروکسی و سرورهای اختصاصی با قابلیت NAT آغاز کرده‌اند.
این مافیا چنان قدرتمند شده است که موفق شده شورای عالی فضای مجازی ایران را به سمت محدودتر نگه داشتن اینترنت سوق دهد تا سود خود را به حداکثر برساند، آن هم علیرغم شرایط بحرانی و جنگی هفته‌های گذشته.
ارائه‌دهندگان ساده میزبانی وب در ایران، تنها پس از دو ماه قطعی، به فروشندگان میلیونر VPN تبدیل شده‌اند.
ما در هفته‌های آینده به جمع‌آوری و انتشار داده‌های لازم ادامه خواهیم داد. اگر این وضعیت ادامه یابد، هدف بعدی ما باید مافیای اینترنت در ایران باشد.
امیدواریم این روزهای سخت برای همه ایرانیان بگذرد. دردی که دشمنان داخلی و دزدانی که به بهانه جنگ مردم را غارت می‌کنند ایجاد می‌کنند، به مراتب بدتر از خود جنگ است!
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/archivetell/5849" target="_blank">📅 23:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">SNI Spoofing
{
"LISTEN_HOST": "
0.0.0.0
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
104.18.35.46
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
replit.com
"
}
{
"LISTEN_HOST": "
127.0.0.1
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
45.85.118.176
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
shad.ir
"
}
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/5848" target="_blank">📅 22:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚀
آموزش راه‌اندازی VLESS WS با دامنه اختصاصی ابر آروان (روش True CDN Proxy)
این روش آی‌پی سرور خارج شما را کاملاً مخفی می‌کند و با عبور دادن ترافیک از سرورهای داخلی، سیستم فیلترینگ (DPI) را به طور کامل فریب می‌دهد.
پیش‌نیازها
:
* یک سرور مجازی (VPS) خارج و پنل 3x-ui نصب شده.
* یک دامنه بین‌المللی برای سرور اصلی (استفاده از پسوندهایی مثل .shop به جای دامنه‌های ملی، امنیت شبکه شما را بالا می‌برد).
* یک دامنه ارزان .ir برای ثبت در شبکه ابر آروان (به‌عنوان ماسک).
🛠
مرحله ۱: تنظیمات DNS در ابر آروان
1. دامنه .ir خود را در پنل ابر آروان ثبت و تایید کنید.
2. به بخش
رکوردهای DNS
بروید و یک
رکورد A
جدید بسازید.
3. در بخش مقدار (Value)،
آی‌پی سرور خارج
خود را وارد کنید.
4. حتماً نماد
ابر را روشن کنید
(پروکسی شبکه فعال باشد).
⚙️
مرحله ۲: تنظیمات پنل 3x-ui
1. وارد پنل شوید و از بخش Inbounds یک کانفیگ جدید با پروتکل
VLESS
بسازید.
2. پورت را روی یکی از پورت‌های امن و مجاز آروان (مثل
443
یا
8443
) قرار دهید.
3. در تنظیمات Transport، بخش شبکه (Network) را روی
ws (وب‌سوکت)
بگذارید.
4. مسیر (Path) را روی یک عبارت دلخواه تنظیم کنید (مثلاً /secure-tunnel).
5. در فیلد
Host
، نام دامنه .ir خود را که در آروان ثبت کرده‌اید بنویسید و تنظیمات را ذخیره کنید.
📲
مرحله ۳: ویرایش نهایی برای کلاینت (v2rayNG/v2rayN)
1. لینک کانفیگ ساخته شده را از پنل کپی کرده و در کلاینت خود ایمپورت کنید.
2. به بخش ویرایش کانفیگ (Edit) بروید.
3. قسمت
Address (آدرس سرور)
را پاک کرده و
دامنه .ir آروان
خود را جایگزین آن کنید.
4. بررسی کنید که فیلدهای
SNI
و
Host
(یا Peer) نیز دقیقاً همان دامنه .ir باشند. ذخیره کنید و وصل شوید!
💡
چرا این روش عالی و بدون قطعی است؟
در این معماری، کلاینت شما مستقیماً به آی‌پی‌های تایید شده داخلی ابر آروان متصل می‌شود. فایروال محلی فقط یک اتصال امن و داخلی را می‌بیند و ترافیک را مسدود نمی‌کند. سپس خود زیرساخت آروان در نقش یک تونل معکوس، ترافیک شما را به‌صورت کاملاً مخفیانه به سرور خارج منتقل می‌کند! آی‌پی سرور اصلی شما هرگز لو نمی‌رود.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/5847" target="_blank">📅 22:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترمینال برنامه‌نویسی هوش مصنوعی با عملکرد بالا
🔥
یک ترمینال کدنویسی بومی هوش مصنوعی مبتنی بر Rust که از همکاری چند عامل هوشمند، رابط کاربری TUI و محیط ایزوله امن پشتیبانی می‌کند و مخصوص توسعه سریع طراحی شده است.
https://github.com/Agions/synerix
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/5845" target="_blank">📅 20:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrDNXej5t_QF2ng4md8dk8bsrXudmxQSa14Y3a4vhrxbTKW9gw5BX3MOLyVsUQmz9KQ89pBBmiJG_uYlEUSIv4Cmd3rqYh_f2nqTjb5hos4ACYK6f-WU4CiDvmrW2sM6rZQajUlWei_qG6dPgFCkfnbyWayWjSJ61DE_7EDWMckLFAwmurK6Qlv3lKTw6yy6sPhFeL8zpkJT6brl6mWY-f0c2d5N-ZFVuTyEyTgcf4f6d4ZF9n3O4FqSNw25T2mCcWOtT7EO0BCsz9PE8LcGHNB85HSqb-Ux8UdEQZvmJmhNNWH9dOsYermU_r3OQX2Iybe9yNYEiCEt6Tp2goofGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
TON رسماً به Gram تغییر نام می‌دهد!
🪙
پاول دوروف اعلام کرد که ارز داخلی اکوسیستم TON از این پس با نام Gram شناخته خواهد شد. این نام در واقع همان نامی است که در اولین وایت‌پیپر پروژه تلگرام استفاده شده بود.
🔹
فرآیند ری‌برندینگ حدود ۳ هفته زمان خواهد برد.
🔹
شبکه بلاکچینی همچنان با نام TON به فعالیت خود ادامه می‌دهد.
🔹
Gram به عنوان نام توکن و ارز اصلی اکوسیستم شناخته خواهد شد.
این اقدام چهارمین مرحله از برنامه ۷ مرحله‌ای «Make TON Great Again» است که دوروف برای بازگرداندن هویت اولیه پروژه TON معرفی کرده است.
📌
خلاصه:
✅
TON = نام شبکه
✅
Gram = نام جدید ارز اکوسیستم
✅
زمان تکمیل تغییرات: حدود ۳ هفته
🪙
به نظر می‌رسد نام تاریخی Gram پس از سال‌ها دوباره به اکوسیستم تلگرام بازگشته است.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/5844" target="_blank">📅 19:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLXYKBFEo9d52aTwSyrYX9HqWtaZRJhuf0yk5iMJBf8_mFZk3mJiM9f_M7OIfBIGoIJ6B_yuxRUEY7PN97uw1jYY6CUZDtVzl7aa3R52f0fQvJUEZzpHSyz3Cg7d5K0gSozsIPHGU81dNIFFdQCvXbBegtCrtkxAQeg0tpB3RUoB_VX-gFa97q6navJ3Iy8TZs_M9hGnteUN7cUaonr_IEHoWJWYGjrSD6NIZ551S_8NDOy-g7sPpCf25PLnZxjg_sXckVsHTieLmjjHy1zpjeR2_hIWJ-YKPhCJcvu5C1DGXkHJc4ZWh61IdlTiz0ERVS6mtp0bfTKaFksnX5_fNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
پوسترهای فوق‌العاده حرفه‌ای از شهر خودتان با هوش مصنوعی!  اگر دوست دارید در چند ثانیه یک پوستر سه‌بعدی و لوکس از شهر خودتان بسازید، این پرامپت فوق‌العاده را امتحان کنید.
🛠
مراحل استفاده:
🔹
وارد GPT Image شوید.
🔹
عبارت [نام شهر شما] را در پرامپت زیر با…</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/5843" target="_blank">📅 18:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⚡️
پوسترهای فوق‌العاده حرفه‌ای از شهر خودتان با هوش مصنوعی!
اگر دوست دارید در چند ثانیه یک پوستر سه‌بعدی و لوکس از شهر خودتان بسازید، این پرامپت فوق‌العاده را امتحان کنید.
🛠
مراحل استفاده:
🔹
وارد GPT Image شوید.
🔹
عبارت
[نام شهر شما]
را در پرامپت زیر با نام شهر دلخواهتان جایگزین کنید.
🔹
پرامپت را ارسال کنید و منتظر نتیجه بمانید.
🎨
خروجی چه شکلی خواهد بود؟
• پوستر گردشگری سه‌بعدی و ایزومتریک
• نمایش معروف‌ترین جاذبه‌ها و نمادهای شهر
• معماری مینیاتوری بسیار واقع‌گرایانه
• افکت‌های سینمایی و نورپردازی حرفه‌ای
• دریا، ساحل، پل‌ها، جزایر و مناظر شاخص (در صورت وجود)
• تایپوگرافی اختصاصی با نام شهر
• مناسب برای پروفایل، چاپ، پوستر یا شبکه‌های اجتماعی
💡
نکته جذاب اینجاست که مدل به‌صورت خودکار مشهورترین بناها، خیابان‌ها، سواحل و نمادهای شهر را تشخیص می‌دهد و آن‌ها را در قالب یک دیورامای شناور و لوکس ترکیب می‌کند.
Create a premium stylized 3D isometric travel poster of [شهر] designed as a floating miniature world placed on top of a large ticket, postcard, or stamp platform with perforated edges. Automatically include the most iconic coastal landmarks, skyline, architecture, cliffs, islands, harbors, bridges, beaches, or sea views associated with the location. Arrange everything in a compact cinematic composition with realistic geography and recognizable visual identity. Style the scene as: - ultra detailed 3D diorama - photorealistic miniature architecture - cinematic travel advertisement - luxury tourism aesthetic - highly immersive but minimal - clean and elegant composition - realistic textures and reflections - soft atmospheric haze - subtle depth of field - premium Instagram-worthy artwork Environment details: - beautiful coastline and ocean integrated into composition - tiny boats, ferries, or sailboats in water - curved shorelines and waterfront promenades - lush greenery or terrain matching the destination - floating soft volumetric clouds around the city - warm cinematic sunlight - subtle shadows and reflections Add tiny realistic miniature people naturally placed near landmarks or waterfronts: - tourists taking photos - couples walking - tiny silhouettes for scale only - avoid crowds or clutter Typography: On the blank white ticket/poster area, automatically add: - the destination name in large bold elegant typography - a short poetic luxury-travel-style tagline matching the location Typography style: - modern sans-serif - premium travel poster design - minimal and elegant - subtle shadows and clean spacing Background: - smooth vibrant gradient background - color palette should naturally match the destination - minimal distractions - lots of negative space around the floating platform Composition: - floating centered platform - isometric perspective - balanced proportions between sea, architecture, and typography - destination should feel suspended in air - cinematic framing - visually clean and uncluttered Aspect ratio 1:1 Extremely detailed, cinematic, modern, premium, luxurious, artistic, visually striking, travel-poster aesthetic.
🔥
نتیجه نهایی معمولاً شبیه پوسترهای تبلیغاتی حرفه‌ای گردشگری و کارت‌پستال‌های لوکس خواهد بود.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/5842" target="_blank">📅 18:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پروکسی متصل سامانتل و مخابرات تست شده
https://t.me/proxy?server=87.248.129.52&port=15&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/5841" target="_blank">📅 18:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">trojan://humanity@198.62.62.23:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#@ArchiveTell
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/5840" target="_blank">📅 18:04 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
