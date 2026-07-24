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
<img src="https://cdn4.telesco.pe/file/oaJR6_oARiZaEJdHttV3BWYUmvvnFFlDB2OM_BYpT7cJfnhu23F7FtHlSgjqxwawUbIHrUK0K_DS7GXgX08wPEw9IfebAwGeYpshxTaZAzIWXZdvNuCDXWrFTik1K-StRd4Qs3Zli9FnKvkaQH99sq1a1CsqxRlxQdmd_VTqb-t5hhUxTMJ-nPbzPdvwwtxt5gwng8w2yJDF0hkvClZj1ZX8jb70vjkwYh2UtzG4KnSqUGOakrCkRjkOkQZy0XQnTmRQLe_dwgy9VIQsy_zaC9h8f6BOkOb6y6cgCBvyJZPSaFLih14VkuSyqJKuB9qdwaIL8VDyu5JsS_wR_I1x6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 109K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 15:28:59</div>
<hr>

<div class="tg-post" id="msg-1291">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_JSIkrcvBFzYFuJm0-Ck_3SneJj0YqtLZd-IL9NKl2wmi9xHiL0dkgYWipZM7RZzvbVlPcbOJFoQVL_Q8uey67ag8z_J9EA-VLD_bNUVv_38YICl66tjB29yMkN-PW1jMiNn1UAFnI0rVKHZGs7DlCKRkJgsAFZYu7Qgr8q7wG0nX2YdwRFOGZPJieKgd19IwaXvI-LRB116TiudgtZYXVx5_Z18ppeyJPkGqpvS4otcyuhN8ylW47lF51FSEyKP0CbCmgK2tPoGIIx61_mvgvz0KsBc02mBayti7BHeAUZC37bcala-7cRrlrpoQuYTveAIzxtwB94Su4jTWzcyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
انتشار نسخه ۱.۰.۰ اپلیکیشن WhiteVPN
• پشتیبانی از فارسی و انگلیسی
• انتخاب پوسته روشن، تاریک یا هماهنگ با دستگاه
• ارتقای هسته Mihomo به نسخه v1.19.29
• مدیریت بهتر سابسکریپشن‌ها و کانفیگ‌های دستی
• پشتیبانی بهتر از WireGuard، WARP Pro و Amnezia Noise
• بهبود اتصال روی Wi‑Fi و شبکه‌های محدود
• بررسی واقعی سلامت اتصال و استفاده خودکار از Clean IP
• تنظیمات پیشرفته شامل TLS Integrity، DNS رمزنگاری‌شده، Split Tunneling و IP Fronting
این بهینه شده تا با ورژن جدید BPB  به خوبی کار کنه.
برای استفاده از اپ، سابسکریپشن های Mihomo را از پلن BPB داخل اپ وارد کنید.</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/whitedns/1291" target="_blank">📅 09:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1289">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنوا پروکسی | Nova Proxy</strong></div>
<div class="tg-text">🤖
ساخت پنل نوا پروکسی فقط با ربات تلگرام!
دیگه لازم نیست مراحل نصب رو دستی انجام بدین.
😎
فقط وارد ربات نوا پروکسی بشین، اکانت Cloudflare بسازین، توکن رو دریافت کنین و چند ثانیه بعد پنل اختصاصی خودتون آماده‌ست.
🚀
بعد از ورود به پنل هم فقط کافیه رمز ادمین رو تنظیم کنین، کانفیگ رو داخل کلاینت Import کنین و از اینترنت آزاد استفاده کنین.
📺
آموزش کامل مراحل داخل ویدیو گفته شده.
💬
اگر سوالی داشتین، داخل کامنت‌ها بپرسین.
🔹
ربات تلگرام:
@IRNovaProxy_Bot
🔹
وب‌سایت:
https://novaproxy.online</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/whitedns/1289" target="_blank">📅 09:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1288">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">📹
آموزش ساخت فیلترشکن رایگان با BPB Wizard  https://youtu.be/vmazT67nRs0</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/whitedns/1288" target="_blank">📅 04:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1287">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1287" target="_blank">📅 04:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1285">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvPIpimDoOaS5sjK0XSdIwnYPvjKd_9MmigLA82xJZZ0ePEuxuPLJ6q38ZghwL1bJDDY6ulHYUpM9jtEV_owDqP-177Vc-48knomHOh6FNuzQ-poqfCAaCq4jjIgQMgoza3HbSecynKtrKn8cwv98Oz6NgAdydlQoN8g_0MQtTM1nHfQrbEfHUCyz00mZVXYF1zrQ1Qh8l20qU_rcIuMISDuaqAj7RYep6VG2gWHE80unrONqtHlooJhilDYWJIRq8g1qLr-nqJ2ZbekHXhCBKRK_fqO9ygzrLuJ4eK4qX0GRZXAmJOfr-IAHRgflgC58szG16qvVH-zShqcWDP3kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین سرور اختصاصی برای اپ WhiteDNS
🌐
Tunnel domain:
v.anonymous.observer
🖥
IP:
78.135.93.50
🔐
Encryption method: 3
روش رمزنگاری را روی AES-128-GCM تنظیم کنید.
🔑
Encryption key:
b275039199b1c8c9
➖
➖
➖
➖
➖
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/whitedns/1285" target="_blank">📅 15:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1283">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یک ظرفیت جدید برای تست فلایت داریم که میتونید از لینک زیر استفاده کنید
🚀
📱
اپ  CoreForge  یک فیلترشکن ساده و قدرتمند برای iOS / آیفون که مخصوص استفاده در شرایط سخت، اختلال شدید اینترنت، اینترنت ملی و حتی دوران قطعی کامل طراحی شده.
https://testflight.apple.com/join/3htm1Whc
آموزش
🎥
📹
:
https://www.youtube.com/watch?v=filwdiPKN90
@whitedns
📢
🔗</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/whitedns/1283" target="_blank">📅 12:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1282">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/hLgrJTWY-aZLEWezSn-jyAf1hcsG9IooxvVMXiZxAmTfBblKgKxCeje_xl-LiuItXJlcwZvsGrY7TadKzGmRsDNpjxFu2w5WsmxiBubxZxQKuO5FvmUwRCFhdgdXsIpYPsN2uxEtd93SEenLSj2JovJWgXg05Hx_Tiw33S2kNDcUFl_nNrjRR9P9jEHkbk40XCwly2-VdkxleAnh-6gffi1UpD2oPmljD4E4UC7ApPt9W_Z-l8tw_FIl0OlV8URsH-GA_szkal0WTDT7R5EjKSaSoeqUV0bVBn-2weHSZ03Z4AMs7VSfV78qGPMcSZGL6y8KWRh3I52zw4SodgmmTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
🌟
با توجه به شرایط کنونی خاورمیانه، ترجیحاً هم اپلیکیشن WhiteDNS را نصب/آپدیت کنید و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی دست یابید.
🌐
📱
لینک‌های مورد نیاز:
دانلود ورژن آخر اپلیکیشن WhiteDNS اندروید | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
🛡
آموزش
دانلود ورژن آخر اپلیکیشن WhiteDNS ویندوز | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
💻
آموزش
دانلود ورژن آخر اپلیکیشن TheFeed اندروید | جایگزین تلگرام در شرایط سخت و محدودیت شدید اینترنت
🔄
آموزش
لینک‌ها با توجه به نیاز کاربران آپدیت میشن.
🔄
@whitedns</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/whitedns/1282" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1281">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/XpHeqNHOcEAyNtjPkBF17V2Zgfpn166VXrWGgcfhTJ5OoOyK-FX93sTALnpQnwCmF-AmFaOehWhtqbWRMJd55r2-mQRj_WI6JHUjhGocd7UgFsaGS9ab4QiEyr4efDvRGYPAlPN8dnqV6oNnpUBx-kawiL60eRTR-ouCRhxI-bheX6pHWCpc2m6FDldsq6lyL3-1Twwhkgiow9vYNIOsw3VezS-J0xjMx1y-rOPrgH7InXbj06cSRF0CatdPdHCd6MwBuvMtE6LPbVXIPdgyhYSZfLw2EQxm0lpsjjCQr2DjX8tJ6n2nPvpbBhfjsDNRWjCUZCY9HRAB2pMupA8S_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد کردن تنظیمات بهینه در whitedns android</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/whitedns/1281" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1280">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/TcFkcGXCUQWSollqIQFsClqOw18OGLkax_3BVojKdsq4vGmY3J7fcob6IBPdvnyXaGXABW9seSlfl5CyaQ6CaiPaMxnyPWVEeJFtj-Veepw7lUupV5roLfuc6DEHz19cT_4YlMqs3s1XtQwL_ob64-FLaWIIrb4FUFP7Dj1q9uKsxWi4nuBQq0hlLosx8Nhou5020mMd2w991L_RZkCK1m2gZvcgVm58bAGuS1jZQducifxtE_tcWaxUan-YuV6RwAKY04UV4tSWRfsnRxRhaHAoJgQfR6O70uXjBHjGy4VHcBsM3YytRv8ov8lfsQK9h3MRrMkxHxTpbHUDZcvbtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد کردن تنظیمات بهینه در Whitedns windows</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/whitedns/1280" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1278">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Android.zip</div>
  <div class="tg-doc-extra">2.5 KB</div>
</div>
<a href="https://t.me/whitedns/1278" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/whitedns/1278" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1277">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/H6f20pvXdOA1m_OtJZcxN3pFS9zhwuUMnOcNSZnf7FLxZHXtby13A-0ALPZ_qEl1ch8VNIO64ifAPpXdOKqLF7AP16Do-vlj8440qNyz1QL7f1qjHr7HwoCwfjrff7ALY2JuXrl92ity2Jn2b0G1QPVrXrX_khYQsry8jrIpnsXQ16v5jNjZTfzdZzBTzWJKGQA3Nfu7VPRtbBUObPh10L0Mo1HeBaDK4VR5dK9QgfCa8IRf4pM8FdSIg-rNMqSIccTkrr9VoVy9_y2BNWQ4nAL6m9ZOE29SZLbTv4ZrKj285IB_8G2qY28UvrMSiGHvfaTtTAfoRk6GelhyeMkO5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
افزایش سرعت اتصال WhiteDNS
تنظیمات اختصاصی whitedns
یکی از مشکلاتی که بسیاری از کاربران با اون مواجه هستن، اتصال موفق
WhiteDNS
با سرعت پایین یا ناپایداره.
✅
یکی از مؤثرترین راه‌ها برای افزایش سرعت و پایداری اتصال، استفاده از تنظیمات بهینه میباشد (البته استفاده از سرور و کانفیگ اختصاصی هم تأثیر قابل توجهی روی کیفیت اتصال داره).
📦
به همین منظور، ۳ تنظیمات پرسرعت برای
اندروید
و
ویندوز
آماده کردیم که می‌تونید از اون‌ها استفاده کنید.
🍏
کاربران آیفون:
اپلیکیشن
CoreForge
به‌صورت پیش‌فرض تنظیمات بسیار مناسبی داره و در اکثر مواقع نیازی به استفاده از تنظیمات اضافی نخواهید داشت.
📥
نحوه استفاده:
• فایل تنظیمات رو مستقیماً داخل اپلیکیشن
Import
کنید.
• یا فایل رو باز کرده و محتوای اون رو
Copy/Paste
کنید.
⚠️
توجه
:
این تنظیمات فقط
مخصوص اپلیکیشن WhiteDNS
(مناسب اینترنت ملی) هستن و به درد استفاده در
WhiteDNS VPN
نمیخورن ؛ لطفاً این دو مورد رو با هم اشتباه نگیرید.
💡
نکته مهم
:
ممکنه این تنظیمات باعث افزایش مصرف اینترنت بشن. بنابراین بعد از اضافه کردنشون ، مقادیر Download Dup و Upload Dup رو متناسب با نیاز خودتون تنظیم کنید:
🔹
مقادیر
بالاتر
👈
مصرف اینترنت بیشتر
✅
اتصال پایدارتر
🔹
مقادیر
پایین‌تر
👈
مصرف اینترنت کمتر
✅
اتصال حساس‌تر و شکننده‌تر
❤️
امیدواریم این تنظیمات تجربه‌ای سریع‌تر و پایدارتر از WhiteDNS براتون فراهم کنه.
@whitedns</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/whitedns/1277" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1276">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">📌
چند نکته مهم برای عملکرد درست برنامه‌:
1️⃣
حتماً فایل PDF راهنما رو بخونید
تا برنامه بدون مشکل براتون کار کنه.
2️⃣
وقتی متصل میشید، صبور باشید تا
آی‌پی و پرچم کشور
روی صفحه ظاهر بشه.
3️⃣
دوستانی که میگن آی‌پی ایران می‌گیرن و سایت‌های هوش مصنوعی باز نمیشه:
• یا چند بار قطع و وصل کنید تا آی‌پی غیرایران بیفته؛
• یا از قابلیت جدید
حالت پروکسی (Proxy Mode)
استفاده کنید و اون رو با سایفون ترکیب کنید. این‌طوری هم سرعتتون عالی میشه و هم مشکل هوش مصنوعی کلاً حل میشه.
💡
*نکته:* ترجیحاً نسخه
مودشده سایفون
رو نصب کنید تا محدودیت سرعت نداشته باشید.
https://t.me/whitedns/1261</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/whitedns/1276" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1275">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnoKaWCV7UIYXl7NzPLGunLxy5PzdDqfV5O4YXkJaBx1_ZGJCo70doWwMsT2bIT2K7hZH2hrKMDGm4Zc1Y05Pkv7SLxeQh-OU6J_TrPT7XSbk-2Jh23mdpQ9xKxEZou2FjWFRkRoPj7EpaumCTYb6FlKIjNN_FVOrT6beACxOAE-43swUpT0dplH2Bd6zhcrs_xWbLZM_fvvYuCJWJha9SLMF4QEwmngmuy1r9DcqMe2-R3fbf61j8K8PznxLhEgBP87FiV9DTrcbKb6-QFshidKBqZu_bagPqST9lrrbH3sXcNex6VR6RyQLJHfffgRj2vvF-xfrK3swiwCSS4qGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین سرور اختصاصی برای اپ WhiteDNS
🌐
Tunnel domain:
v.anonymous.observer
🖥
IP:
78.135.93.50
🔐
Encryption method: 3
روش رمزنگاری را روی AES-128-GCM تنظیم کنید.
🔑
Encryption key:
b275039199b1c8c9
➖
➖
➖
➖
➖
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/whitedns/1275" target="_blank">📅 06:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1274">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">📹
آموزش ساخت فیلترشکن رایگان با BPB Wizard
https://youtu.be/vmazT67nRs0</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/whitedns/1274" target="_blank">📅 05:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1273">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1273" target="_blank">📅 05:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1268">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">20 MB</div>
</div>
<a href="https://t.me/whitedns/1268" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/whitedns/1268" target="_blank">📅 05:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1267">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfLEKYkMDe8KtGKMAp8PAbVCtmKhWDIUgErHPIDj3s1bNky1-OpRUP7JuDiFpM-hvRy-HTqpBs-vNj0T7zZySTWgpIbH5BLe44wCxFmOJtMIc_9T9z-W3ZaOcbYMLEFKwTBN7HWnsiT8qEtHXXMBb-ayxFPQNwqnO18lIgUlG10lfShY-8XukIYli0oLVuIlz2ALwmUD8DaBALlBB0JYdYxdDXId2gGmymrzlrrW2TkqajuZBJR_Z3JKfDNmmdHRBciphifyzia_OBq27S2GvrVA6lwHij0j49jChk3SCO7mHuUNE20q0RwxGLlLWl2YvJkC37WjeL8GNU--492vzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
انتشار نسخه ۱.۰.۰ اپلیکیشن WhiteVPN
• پشتیبانی از فارسی و انگلیسی
• انتخاب پوسته روشن، تاریک یا هماهنگ با دستگاه
• ارتقای هسته Mihomo به نسخه v1.19.29
• مدیریت بهتر سابسکریپشن‌ها و کانفیگ‌های دستی
• پشتیبانی بهتر از WireGuard، WARP Pro و Amnezia Noise
• بهبود اتصال روی Wi‑Fi و شبکه‌های محدود
• بررسی واقعی سلامت اتصال و استفاده خودکار از Clean IP
• تنظیمات پیشرفته شامل TLS Integrity، DNS رمزنگاری‌شده، Split Tunneling و IP Fronting
این بهینه شده تا با ورژن جدید BPB  به خوبی کار کنه.
برای استفاده از اپ، سابسکریپشن های Mihomo را از پلن BPB داخل اپ وارد کنید.</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/whitedns/1267" target="_blank">📅 05:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1266">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اگر توی نصب مشکل دارید نسخه قبل را پاک کنید و این نسخه را نصب کنید</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/whitedns/1266" target="_blank">📅 05:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1262">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">14.3 MB</div>
</div>
<a href="https://t.me/whitedns/1262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/whitedns/1262" target="_blank">📅 05:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1261">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/crWN7uL7DgoJjzEPzKG829MYn6O72cVGoCshI0jc4P2u2AgWRy8aF-MLuB2YuRiOuG0rfWeMYvQLBGENli6xKItvWfgh_5MY9ln5fvCuux9vhkefspaZZPVVMfNnAsj3geOlqVEJzSaxYvCcySI4Y4vymWHM_0OD8iJgAI8QhrfayKmZ66vmezBVoEnPosfb7Oq6FqIJMXridat_dkXsyP5zwyBQnL8CndC1Z2NAo7cYV3IL3pBsxLeCuew5X_3U__UgrKHVACDdHZtGE-yJG60hdn4wLRVw2d3XAnpjr3KRyGOrXouS8KCvSkI67t6EVxIwQdQB9Ddzv_gwAUMUTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Aether
1.2.0
🌐
✨
(فقط برای اندروید )
آتر یک ابزار ساده برای اتصال امن و عبور از محدودیت‌های اینترنت است. برنامه به‌صورت خودکار سرورهای سالم WARP را پیدا کرده و یک اتصال رمزنگاری‌شده ایجاد می‌کند؛ بدون نیاز به خرید یا واردکردن کانفیگ.
🔒
🚀
📱
روش استفاده:
1️⃣
اینترنت را روشن و برنامه را باز کنید.
2️⃣
تنظیمات را روی حالت خودکار بگذارید.
⚙️
3️⃣
دکمه بزرگ وسط صفحه را بزنید و درخواست VPN را تأیید کنید.
📲
✅
تمام! بعد از نمایش
Connected
می‌توانید از اینترنت استفاده کنید.
🌍
🎉
مهم :
⚠️
برنامه روی حالت اتوماتیک اول اسکن میکنه و ممکن هست بسته به وضعیت اپراتور شما و فیلترینگ حتی تا چند دقیقه طول بکشه. پس صبور باشید و به برنامه وقت بدید.
⏳
💤
یک فایل PDF با توضیحات دقیق در مورد کارکرد و نحوه راه اندازی براتون گذاشتیم . کامل بخونید لطفا
⚠️
https://t.me/whitedns/1265
کد پروژه :
https://github.com/QW-AI-Code/Aether/
@whitedns</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/whitedns/1261" target="_blank">📅 05:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1259">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-QDraZLd-xAj3JnZ3ALHy64PhDW_FecJgzC5t_M8D-x3jlUshlGuP_Z8KLaGZMIgBxZOAluXxw3QZsf9jRWY-dw2rolgcqYEK8_MOhJYCXhqIShqvuKeVHs08nhJz-VS9akeAd52hbgyqNZkWg6Jf3amRQqsrzMCoM9eWbiBAp4iUTqXV8Cx92C-1xkqtNEEMEHqN8LGsm6_KjPdWxuPP7rojEzEbtoprcKxhv79Oy8Mz_kfQHdCoti4SjhNlFgakUjhSi5xS_A8HOD6GSZSPxYPSiIwIqpumc8Hc0UNi2wixkvMIiFWt1_mErbn4YJJi6uM3bUdO60zULhXBTmcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین سرور اختصاصی برای اپ WhiteDNS
🌐
Tunnel domain:
v.anonymous.observer
🖥
IP:
78.135.93.50
🔐
Encryption method: 3
روش رمزنگاری را روی AES-128-GCM تنظیم کنید.
🔑
Encryption key:
b275039199b1c8c9
➖
➖
➖
➖
➖
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/whitedns/1259" target="_blank">📅 01:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1258">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">📹
آموزش ساخت فیلترشکن رایگان با BPB Wizard
https://youtu.be/vmazT67nRs0</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/whitedns/1258" target="_blank">📅 15:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1257">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👆
انتشار نسخه ۱.۰.۰ اپلیکیشن WhiteVPN</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/whitedns/1257" target="_blank">📅 14:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1252">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">20 MB</div>
</div>
<a href="https://t.me/whitedns/1252" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/whitedns/1252" target="_blank">📅 14:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1251">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUQsF8AAyrz84IKlFwHcYq29cH6pEeKsNIXHPnzozLGLVuJYJNJof7TMPTeo0hAU12VsaQmStJwGng8h7qjXSI55AKUmINjFXXK9gH5l2MAeAPhjTTbtKxVHJzLVPV4VCOGjws1fuJz_EVNZxa1NNaplMNo76drtV-5vytcS5VhmeQOvAHJKDD6vc3HspE1BEvuazYKweb61uu1bnrBdKeIEdQGjvZHIF4G78p3y5454A-BHyHWQy0jiBqii773jzJSknN3jXyygtPPMKukWZVmPt7Lm8WPz_sVu-gVkdgR9QmZc6d6oRD8x90VsjBQq9iXz-Yxhg-cJH7qimMjBIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
انتشار نسخه ۱.۰.۰ اپلیکیشن WhiteVPN
• پشتیبانی از فارسی و انگلیسی
• انتخاب پوسته روشن، تاریک یا هماهنگ با دستگاه
• ارتقای هسته Mihomo به نسخه v1.19.29
• مدیریت بهتر سابسکریپشن‌ها و کانفیگ‌های دستی
• پشتیبانی بهتر از WireGuard، WARP Pro و Amnezia Noise
• بهبود اتصال روی Wi‑Fi و شبکه‌های محدود
• بررسی واقعی سلامت اتصال و استفاده خودکار از Clean IP
• تنظیمات پیشرفته شامل TLS Integrity، DNS رمزنگاری‌شده، Split Tunneling و IP Fronting
این بهینه شده تا با ورژن جدید BPB  به خوبی کار کنه.
برای استفاده از اپ، سابسکریپشن های Mihomo را از پلن BPB داخل اپ وارد کنید.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/whitedns/1251" target="_blank">📅 14:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1250">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آموزش آماده شد اما تا ادیت میکنیم، ورژن جدید WhiteVPN رو ریلیز کنیم چون آموزش رو با کمک اون ساختیم.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/whitedns/1250" target="_blank">📅 13:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1249">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">همراه با فیلم آموزشی، درحال آپدیت کردن هسته WhiteVPN و اضافه کردن بهترین پشتیبانی ممکن از آپدیت جدید BPB  هستیم تا اتصال شما ساده تر و پایدار تر بشه.
نامگذازی اپ هامون هم داره کم کم تغییر میکنه تا کمتر گیج کننده باشه براتون
به مرور زمان همه اپ ها تغییر میکنند به نام های زیر:
WhiteDNS
WhiteVPN
WhiteScanner
WhiteBPB</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1249" target="_blank">📅 08:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1246">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">White DNS
pinned «
جلسه پرسش و پاسخ توی همین تلگرام به صورت انلاین بگذاریم  ؟
🔥
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1246" target="_blank">📅 16:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1245">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-poll">
<h4>📊 جلسه پرسش و پاسخ توی همین تلگرام به صورت انلاین بگذاریم  ؟🔥</h4>
<ul>
<li>✓ بله❤️</li>
<li>✓ خیر🫤</li>
</ul>
</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/whitedns/1245" target="_blank">📅 16:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1244">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/nm_lhurI0jpdoA5IDjae7MrGgn0dZBqN69ldOyG2Ca52Kz1gu3wfV4RhhfqgNDSYGhczqQKIm9sSU95QDZ9Q9nFlUUml1Bmx-Xy75Kb4bvfGC1Daj0CyyJ4i9WnUhlwnRbyWm2-sZkJ76cPXOZgYml8Seeb-TlwN7aKbgynXB6U-pkLJ37b9G7rlKrITBREShiAuv6xoRyeMIzn6um4eLrMWIabrVgzqdJF5QD7_7MCfyYXy1m6F-ND1Wpm-A7pkAnzvBCSnZJ4NN7gZTBR28XA1NkYkHrgaUob16lMibnrSJTEp01b8b0fZoMGs4f4vLeEJogo6dv9TlZvJcToGeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت بزرگ و انقلابی BPB Worker Panel (نسل جدید - نسخه 5.1.1)
🎉
نسخه جدید و کاملاً بازطراحی‌شده پنل BPB با امکانات بی‌نظیر و تغییرات ساختاری عظیم منتشر شد! در این آپدیت، مدیریت پنل و سرورها بسیار یکپارچه‌تر، امن‌تر و بی‌نیاز از درگیری با داشبورد کلودفلر شده است.
✨
مهم‌ترین ویژگی‌ها و تغییرات این نسخه:
🔹
نصب سریع با One-Click Wizard:
دیپلوی پنل حالا فقط از طریق ویزارد آنلاین و اختصاصی انجام می‌شود و پس از نصب، یک لینک کاملاً پرایوت به شما می‌دهد (روش‌های نصب دستی روی این نسخه کار نمی‌کنند).
🔹
داشبورد مدیریت داخلی (Admin Dashboard):
امکان آپدیت پنل به نسخه‌های جدید، حذف کامل پنل، و ریست پسورد مستقیماً از داخل خود پنل اضافه شده است.
🔹
راه‌اندازی ربات تلگرام:
مدیریت کانفیگ‌های تکی، دریافت لینک‌های سابسکریپشن و مانیتورینگ مصرف (همراه با هشدار مصرف بالای ۸۰٪) از طریق ربات تلگرام.
🔹
حذف کامل Environment Variableها:
تمام متغیرهای ثابت (مثل VLESS UUID، Trojan Pass، Proxy IPs و...) از داشبورد کلودفلر حذف شده و مستقیماً داخل پنل قابل آپدیت و مدیریت هستند.
🔹
ارتقای چشمگیر امنیت:
لاگین به پنل حالا نیازمند ایمیل کلودفلر شماست.
مسیر ورود به پنل به یک آدرس تصادفی و امن (Secure Path) تغییر یافته (دیگر با زدن
/panel
وارد نخواهید شد).
🔹
تنظیم سریع Custom Domain:
دامنه‌های سفارشی خود را می‌توانید مستقیماً از بخش Common settings وارد کنید تا کانفیگ‌های مربوطه با تگ
D
به سابسکریپشن شما اضافه شوند.
🔹
قابلیت‌های جدید شبکه و پروکسی:
پشتیبانی از Xhttp و VLESS Encryption برای Chain Proxy در هسته‌های Xray و Clash.
🔹
انتقال آسان تنظیمات:
اضافه شدن قابلیت جذاب به‌روزرسانی و همگام‌سازی تنظیمات از یک پنل ریموت BPB دیگر.
⚠️
نکات بسیار مهم برای اتصال کلاینت‌ها:
حتماً کلاینت‌های خود را به آخرین نسخه آپدیت کنید (حداقل Sing-box نسخه 1.12.0 و v2rayNG نسخه 2.2.3 به بالا).
برای اتصال پایدار در v2rayNG، حتماً گزینه
Hev TUN
را فعال کنید.
در صورت مشکل با فرگمنت در برخی ISPها، حالت
Packet
را روی
1-1
تنظیم کنید.
لینک ریپو :
https://github.com/bia-pain-bache/BPB-Worker-Panel/releases
لینک ویزارد :
https://wizard.bpb-panel.workers.dev/
@whitedns</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/whitedns/1244" target="_blank">📅 12:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1239">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/whitedns/1239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/whitedns/1239" target="_blank">📅 12:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1238">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llLxgnTzQblWWVqBp5qkn2-UwOsTE8H9QrVzoxBmIl5AylclY1AFGuFvcCxX3vsFqmbRfLc4CnzMdNmlZxc4GnSUwQwe3U8Urkb5DGEyyu7r0G3n8ADTst8dcudzaXzi1u3R8IzLwsm3xKbjO1QOpawEDDFIh5b_3EZfVK2rvoXKkNqj1Xof1GOXeQL8lxjonuCfTg4sW5VTdTSgmcQi_ESHfsEJr-YJrGdO3VWNThQhc4pJAyz9O8YOlyNeoEqS4P_9lzPX6CegVmu0WkSioPWcobhtIkxvEaS9oa0neuGdK8wdBfpetbotJssbh2FIglsu9pUj2r9dk_TEV77ZhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/whitedns/1238" target="_blank">📅 12:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1235">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-1.1.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">14.2 MB</div>
</div>
<a href="https://t.me/whitedns/1235" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تازه‌های نسخه ۱.۱.۰
🆕
اِتِر (Aether)
تایل تنظیمات سریع (Quick Settings)
— روشن/خاموش کردن VPN مستقیم از منوی بالای گوشی، بدون باز کردن برنامه. یک بار اضافه‌اش کنید: منو را پایین بکشید ← دکمه مداد/ویرایش ← تایل
اِتِر
را بکشید داخل.
اشتراک‌گذاری VPN با لپ‌تاپ یا گوشی دیگر
📱
💻
— از منوی کناری ←
اشتراک‌گذاری VPN
. گوشی شما یک پراکسی
HTTP (پورت 8118)
و یک پراکسی
SOCKS5 (پورت 1080)
روی وای‌فای/هات‌اسپات باز می‌کند. آدرس دقیق
ip:port
قابل کپی است و کافی‌است در تنظیمات پراکسی سیستم دستگاه دیگر وارد شود.
تنظیمات پیشرفته در صفحه اصلی
⚙️
— دکمه جدید بالا–راست صفحه، پروتکل، حالت اسکن، نسخه IP و بقیه تنظیمات را در یک پنل پایینی باز می‌کند.
آپدیت بدون حذف برنامه از این به بعد
🔄
— همه بیلدها از این نسخه با یک کلید ثابت امضا می‌شوند، پس نسخه‌های بعدی مستقیم روی نسخه قبلی نصب می‌شوند. نکته: برای آپدیت
از نسخه 1.0.0
فقط یک بار باید برنامه قبلی حذف شود، چون آن نسخه با کلید موقت امضا شده بود.
رفع اشکال:
پنل اشتراک‌گذاری VPN حالا بلافاصله بعد از روشن کردن سوییچ، آدرس
ip:port
قابل کپی را نشان می‌دهد.
✅
عنوان ریلیزها تمیزتر شد (دیگر پسوند "(build N)" ندارد).
📝
Downloads
📥
https://github.com/QW-AI-Code/Aether/releases/tag/v1.1.0-build.2</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/whitedns/1235" target="_blank">📅 11:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1234">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⚡️
اِتِر (Aether) — آزادی، با یک لمس!
⚡️
نسخه اندروید   درویدِ قدرتمند و رایگانِ اِتِر؛ اینترنت بدون محدودیت، بدون ثبت‌نام، بدون سرور شخصی!
🚀
🔥
چرا اِتِر؟
🖱
اتصال با یک لمس — VPN کامل سیستمی؛ همه اپ‌ها و مرورگرها بدون هیچ تنظیمی از تونل عبور می‌کنند
🛡
موتور…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/whitedns/1234" target="_blank">📅 11:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1233">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/u8MTX2pkFGfQavcQma1hklHn1_UwIO9tLF_p3wWIVm81bfMYUI3dmCObCvLAX82-UQ6eQcM66PDd41VZuAwlgZAitTlLrQChNSItPdBigfNAgJliHA3Tyh8nMvVULZUqjwbQetdKtw-8EpcCxTgjg0HN6JNlOmfSGWQZK7gbcDHLYEcziCfuyuUjnLHnnIfWvcxbiHPFgGVeF60C-eWHVVjo7dJrs_qtHPg2HwD79Y4Si23MDKK5kSc_3nIwlU7dYazsmm4WTzspPABWNmIyZEwshtG7bWT0hutIn3_Lf2ZtZ-SJxUGrOZ_vil3BN8CwmWnn1pF0VTd_JExTMl5z0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :
ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.
پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است همیشه کامل یا دقیق نباشند. این ربات به اینترنت زنده دسترسی ندارد، جایگزین پشتیبانی انسانی نیست و اگر اطلاعات کافی نداشته باشد قادر به پاسخگویی نیست. لطفاً اطلاعات حساس یا شخصی خود را برای ربات ارسال نکنید.
برای مدیریت بهتر منابع و کنترل هزینه‌ها، محدودیت استفاده از ربات به شکل زیر تنظیم شده است:
- هر کاربر می‌تواند در هر ۵ دقیقه حداکثر ۳ سؤال بپرسد.
🕒
- سقف استفاده روزانه برای هر کاربر ۵۰ سؤال است.
📊
- در صورت رسیدن به محدودیت، ربات زمان تقریبی انتظار را نمایش می‌دهد.
⏳
- دستور /search و سایر دستورات عمومی شامل این محدودیت نیستند.
🚫
- محدودیت‌ها پس از راه‌اندازی مجدد ربات نیز حفظ می‌شوند.
🔄
این تغییر باعث پایداری بیشتر ربات و دسترسی منصفانه‌تر برای همه کاربران می‌شود. سپاس از همراهی شما
🌱
لازم به ذکر است در صورت سواستفاده این محدودیت بیشتر خواهد شد - پس خواهشمندیم با استفاده درست جلوی به ادامه این خدمات کمک کنید
لینک ربات :
@WhiteDnsResponder_bot
🔗
@whitedns</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/whitedns/1233" target="_blank">📅 05:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1232">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⚡️
اِتِر (Aether) — آزادی، با یک لمس!
⚡️
نسخه اندروید
درویدِ قدرتمند و رایگانِ اِتِر؛ اینترنت بدون محدودیت، بدون ثبت‌نام، بدون سرور شخصی!
🚀
🔥
چرا اِتِر؟
🖱
اتصال با یک لمس — VPN کامل سیستمی؛ همه اپ‌ها و مرورگرها بدون هیچ تنظیمی از تونل عبور می‌کنند
🛡
موتور پیشرفت
ه WARP با تکنیک‌های ضدفیلترروز:
✅
پروتکل MASQUE (HTTP/3 و HTTP/2)
✅
تونل تو در تو WAR P-in-WARP (حالت gool) برای سخت‌ترین شرایط
✅
قطعه‌قطعه‌سازی ClientHello و مبهم‌سازی ترافیک
✅
اسکن هوشمند و خودکار بهترین endpoint
⚙️
۴ حالت اسکن برای هر شرایطی: Turbo
⚡️
/ Balanced
⚖️
/ Stealth
🥷
/ Thorough
🔍
📊
نمایش زنده ترافیک — سرعت لحظه‌ای و مجموع دانلود و آپلود، درست مثل VPNهای حرفه‌ای
🌍
نمایش IP سرور با پرچم کشور + تایمر مدت اتصال
🧪
تست خودکار سلامت اتصال — بعد از هر اتصال، خودش بررسی می‌کند ترافیک واقعاً جریان دارد یا نه و دقیقاً می‌گوید مشکل کجاست.
🔁
اتصال مجدد خودکار — اگر ارتباط قطع شود، خودش دوباره وصل می‌شود
🔒
امنیت کامل، بدون نشت:
✅
بدون نشت IPv6 و DNS
✅
بدون بکاپ اطلاعات حساس
🎨
رابط کاربری زیبای Material 3 — دوزبانه فارسی و انگلیسی، با منوی مرتب و مینیمال
📱
سبک و بهینه — نسخه مجزا برای هر معماری (arm64 و arm32)
📥
دانلود مستقیم از گیت‌هاب:
https://github.com/QW-AI-Code/Aether
@whitedns</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/whitedns/1232" target="_blank">📅 03:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1231">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سلام دوستان عزیز
👋
🌸
اپ CoreForge یک قابلیت جدید برای کاربران iOS اضافه کرده
📱
✨
این اپ شبیه WhiteDNS است که برای iOS و شرایط قطعی اینترنت طراحی شده
🚀
🌐
🔗
لینک:
https://testflight.apple.com/join/3htm1Whc
🎥
آموزش استفاده:
🔗
https://youtu.be/filwdiPKN90?si=O-hvgeNw43t4BUmR
📲
کانال تلگرام:
@WhiteDNS</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/whitedns/1231" target="_blank">📅 17:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1230">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromامیرپارسا گودمن</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6b89a933.mp4?token=AS3rFBe0KsypBocu8rGPcdFDC19gYVkIaRwcx-TWEKXL7TVKR1ZWd8UuxPAiO1Pkp8D0fBLw_47yHhFdCkNoINStj_6r1ImQL48obyP06i46Kd9yTczuww-IB34gffjyOiq1jueresqNPS8UZykJCrFzz1Odxr171wMLn6Wa4f_WRH4fWxG3xa3O4UMvqPIYQ44-hge8PELMZwyV0LvrgHtC_zRX08vE4f3mFT-AEJXjYZY6kYg-k5bZak8ZWKRilHQabOeVEJ9W-KDoG9T1ffvtCGOaAPzKnYtKTVWGn3holFcSrPHapxL8RuvRgBrtAPXE2pppvyT48N1VpA6QRYAd6c-URDjsmNgYknvPijP6HW8nHAMtBTtOHe65yJ3vlmTQDOGIZRTKC7ey9dx2-PdcEunDWBC4MWeKQY1k4kPU4IrCPVeM7T0dHWt_pdWZO3JkkdslbDrnYqFfmWqFVZEpJkMh6emhfrxNty_XqCSUAcWTaIT9anDs5UWztsEIlUFo1FJn89Ffka3JB_ZOd77bxmd8WbnZ0fAs5UTiw9E8d9MKfoOfhEoWWKTEtBOJuL3dj5ohnBXN3Xo0ikLfOIeFzecKRujIS3-bFivZN9-g0kQe45K6dylei6e-9mjh2bCyuEsf0nwXSoFNKUPPvs4Q-17HXXr1JnOf3jv-16w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6b89a933.mp4?token=AS3rFBe0KsypBocu8rGPcdFDC19gYVkIaRwcx-TWEKXL7TVKR1ZWd8UuxPAiO1Pkp8D0fBLw_47yHhFdCkNoINStj_6r1ImQL48obyP06i46Kd9yTczuww-IB34gffjyOiq1jueresqNPS8UZykJCrFzz1Odxr171wMLn6Wa4f_WRH4fWxG3xa3O4UMvqPIYQ44-hge8PELMZwyV0LvrgHtC_zRX08vE4f3mFT-AEJXjYZY6kYg-k5bZak8ZWKRilHQabOeVEJ9W-KDoG9T1ffvtCGOaAPzKnYtKTVWGn3holFcSrPHapxL8RuvRgBrtAPXE2pppvyT48N1VpA6QRYAd6c-URDjsmNgYknvPijP6HW8nHAMtBTtOHe65yJ3vlmTQDOGIZRTKC7ey9dx2-PdcEunDWBC4MWeKQY1k4kPU4IrCPVeM7T0dHWt_pdWZO3JkkdslbDrnYqFfmWqFVZEpJkMh6emhfrxNty_XqCSUAcWTaIT9anDs5UWztsEIlUFo1FJn89Ffka3JB_ZOd77bxmd8WbnZ0fAs5UTiw9E8d9MKfoOfhEoWWKTEtBOJuL3dj5ohnBXN3Xo0ikLfOIeFzecKRujIS3-bFivZN9-g0kQe45K6dylei6e-9mjh2bCyuEsf0nwXSoFNKUPPvs4Q-17HXXr1JnOf3jv-16w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">https://t.me/xsfilterrnet/3623</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/whitedns/1230" target="_blank">📅 00:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1229">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/EqRRrYXpHlb65Ok7bq8WbJwSx8w_8gkR7I3KgnDn3dubw3VHslL-0IVS81AMhWYCBfq640n9RijVigq4PAbjryNZEACyPOgCmHGH6wMtrxq1qrk6Y7oMWbtM0zGvCJuuZWpBAgpkN4G0H-BBtjdvfppqm35FbR_Meyza1WBXwHraiOWe_YLVt-ENl_0Ny7NhA3Bou2172mEJ5Sj2wCrBeovkK4N7scGfhpuynkVpOqa-aLRPNl1xwSCPnF7yzXNUKEjHb8EapqRuSTcHxYa9aHPAFY3Wxvc9qaZQUfpWv6HDMka6YaCsXeVquOZZBM0Y92bpxO2cIEoKU_uMt7dhNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی کانال یوتوب WhiteDNS
🌐
اگر به دنبال آموزش‌های تخصصی و کاربردی برای دور زدن فیلترینگ، پیدا کردن آی‌پی‌های تمیز و ساخت سرورهای شخصی هستید، این کانال یکی از بهترین مراجع آموزشی است!
🎓
در این کانال می‌آموزید:
🔹
آموزش صفر تا صد V2Ray
و راه‌اندازی پنل‌های ثنایی (3x-ui)
🔹
پیدا کردن آی‌پی تمیز با
WhiteDNS Scanner
🔹
راه‌اندازی
پروکسی MTProto
برای اتصال بدون قطعی تلگرام
🔹
معرفی ابزارها و کلاینت‌های مختلف (مثل CoreForge برای iOS و FlClash برای اندروید)
🔹
راهکارهای ارتباطی برای زمان قطعی کامل اینترنت
📡
و .................................
برای یادگیری ساخت فیلترشکن‌های امن و پرسرعت، همین الان به این کانال سر بزنید و سابسکرایب کنید.
👇
🔗
https://www.youtube.com/@WhiteDNS</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/whitedns/1229" target="_blank">📅 17:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1228">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/whitedns/1228" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1227">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/whitedns/1227" target="_blank">📅 12:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1226">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/whitedns/1226" target="_blank">📅 12:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1225">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/gQ4_QAQTSE9p6sVLxYxIO3lRPI0K0vr1OPzHTpzlHS227udmB36bg5hI56YDmu6ppuLJtIOwure-lcFad_ilPLIYJzb5MKYMCJjqk8ZWsO_iwWFO7y4iIt9gkJJ0QR6fodz_ZuVslBn4S7HCydKeB7x1vwFU4Dkz3Zux4aWD-oL9MYtmQUl7Pe1y1-DQ_mDKj1C2mUTrLR7jNzf7Qn3NbKi8MLqJDYf2A8t35zj8xuw2u4h19rZXvr5JV3EgBdLfSzwqvNqqyXswEeE4x50Cbst4TNRudQJz073tqhu_74kpcGZzSj84EMhbuTKaBb7nWE_HcVtZ4PHQSDdAkpajMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
🌟
با توجه به شرایط کنونی خاورمیانه، ترجیحاً هم اپلیکیشن WhiteDNS را نصب/آپدیت کنید و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی دست یابید.
🌐
📱
لینک‌های مورد نیاز:
دانلود ورژن آخر اپلیکیشن WhiteDNS اندروید | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
🛡
آموزش
دانلود ورژن آخر اپلیکیشن WhiteDNS ویندوز | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
💻
آموزش
دانلود ورژن آخر اپلیکیشن TheFeed اندروید | جایگزین تلگرام در شرایط سخت و محدودیت شدید اینترنت
🔄
آموزش
لینک‌ها با توجه به نیاز کاربران آپدیت میشن.
🔄
@whitedns</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/whitedns/1225" target="_blank">📅 06:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1224">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/UKt-zFD0gi4tm06YF5dtiU1XJHh56pqjgEgyWldjXbFlhyQuMQ5_nRxFLBnEYBUPIiz6vAE9bSFpan8Bv8-qxv--Bb0IqWaYUozkAu-h3nzMMp6kkD0FEGmfLiWhXTXQbujFNnVQJooEj1_21P-JsK2ODA1iqeSMXBnf7uO8hwSpzymG4TSCfNyN5Si--OmBOM8Ost67qtF3VRFo6HdH7Qzp4qqSU2x_un1CZziAkANgHj0w7YAYVxfpP9iAQrxv2x4nKK3bQOsnTC2JB0lSGhcHAZ0E798fssX0iBeaDheu-4ri6_AdX2ve2xNzGfQfRPNJz7Sk_QIvG1pHGw9VlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :
ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.
پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است همیشه کامل یا دقیق نباشند. این ربات به اینترنت زنده دسترسی ندارد، جایگزین پشتیبانی انسانی نیست و اگر اطلاعات کافی نداشته باشد قادر به پاسخگویی نیست. لطفاً اطلاعات حساس یا شخصی خود را برای ربات ارسال نکنید.
برای مدیریت بهتر منابع و کنترل هزینه‌ها، محدودیت استفاده از ربات به شکل زیر تنظیم شده است:
- هر کاربر می‌تواند در هر ۵ دقیقه حداکثر ۳ سؤال بپرسد.
🕒
- سقف استفاده روزانه برای هر کاربر ۵۰ سؤال است.
📊
- در صورت رسیدن به محدودیت، ربات زمان تقریبی انتظار را نمایش می‌دهد.
⏳
- دستور /search و سایر دستورات عمومی شامل این محدودیت نیستند.
🚫
- محدودیت‌ها پس از راه‌اندازی مجدد ربات نیز حفظ می‌شوند.
🔄
این تغییر باعث پایداری بیشتر ربات و دسترسی منصفانه‌تر برای همه کاربران می‌شود. سپاس از همراهی شما
🌱
لازم به ذکر است در صورت سواستفاده این محدودیت بیشتر خواهد شد - پس خواهشمندیم با استفاده درست جلوی به ادامه این خدمات کمک کنید
لینک ربات :
@WhiteDnsResponder_bot
🔗
@whitedns</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/whitedns/1224" target="_blank">📅 20:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1219">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/whitedns/1219" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/whitedns/1219" target="_blank">📅 17:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1218">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9WjkmaqscfHE5b5kB51Xi7n9jTJ4ngcdsNrqiVozoTsQVXa33jR30wjGw-AO9PJxiBpmg1gb8EYXZO-HH_z3xYdCOkNBHS1mA7nEitdtbr5m6ei-hfwTvTIe_WHwhX1ms9Zrxp9wfqnRWoq4Kcr6Tvqm4I4RCxX_ZfteYJ8Q4fkADp_591i5rszJNuZKgLnb-3t6Y5hJQ3Q1pRKt6s-B_cKKw4_2SEHf4gtaOxkWpWI-adsNsryfYtTUkzLUoLljNveZmg6B8Pvej3J8Id0lFl3gALuXo7opWrbu3_-cTCVfsBFbu22DEWTuxafKIT-8jgIRd3zj10SDDYmLLh_qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/whitedns/1218" target="_blank">📅 17:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1217">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/whitedns/1217" target="_blank">📅 17:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1216">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⚠️
⚠️
⚠️
⚠️
اطلاعیه مهم
با بالا گرفتن تنش‌ها و با توجه به تجربه‌ای که از قطعی سراسری اینترنت داشتیم، پیشنهاد می‌کنم دوستانی که تازه به جمع ما اضافه شده‌اند، مطالب زیر را با دقت مطالعه کنند.
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/whitedns/1216" target="_blank">📅 14:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1215">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">White DNS
pinned «
دوستان برای همه اینها اموزش هم گذاشتیم که الان لینک را اضافه کردیم .  لطفا بدون دیدن این اموزش ها سوال نکنید
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1215" target="_blank">📅 13:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1214">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">درود به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
🌟
با توجه به شرایط کنونی خاورمیانه، ترجیحاً هم اپلیکیشن WhiteDNS را نصب/آپدیت کنید و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/whitedns/1214" target="_blank">📅 13:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1213">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">White DNS
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1213" target="_blank">📅 12:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1211">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OWBcODHTH-RNL1E6hAm1mMcwQcvKZZq3aJzh6IGffSv6qWLWh59PjP8hijiE9YLMtHQu49XnwoX1clSkO2_z6K9SjFbU68BNoHi4SHItUmC2MUOLNgyE9Hmx01LK2jRl5ZdnB8v4xueswQW92KSib7vXouFxmnyiK26ZxVmDeLt6IEENV9KTH6LOtjmGXj1QysUW9Xisv64VRzA8nBNd7D7IMN3Pl1XgmQlioNu5_Kw6AVfvREywQdWlTYaVNWhWtZRZJy3QbDAygpVkRJqMplDWR5gBb_D_IvqV5tknW-t22EHedWURdm297RSO2cubyeTryptzkuC3dRKP3wNniA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
🌟
با توجه به شرایط کنونی خاورمیانه، ترجیحاً هم اپلیکیشن WhiteDNS را نصب/آپدیت کنید و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی دست یابید.
🌐
📱
لینک‌های مورد نیاز:
دانلود ورژن آخر اپلیکیشن WhiteDNS اندروید | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
🛡
آموزش
دانلود ورژن آخر اپلیکیشن WhiteDNS ویندوز | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
💻
آموزش
دانلود ورژن آخر اپلیکیشن TheFeed اندروید | جایگزین تلگرام در شرایط سخت و محدودیت شدید اینترنت
🔄
آموزش
لینک‌ها با توجه به نیاز کاربران آپدیت میشن.
🔄
@whitedns</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/whitedns/1211" target="_blank">📅 12:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1210">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/mnlSVAT3XWRlRmO4Wm4L5UJxT-KM4xFUTe6rvUbG8XK7GOKV5NGYBRttzt0HxJ5Y5mBecUmu6QRpzJoy1LKwV4P7MyxoeACfTj8IvrLDPXkqQmuOu0Wfu2Rbo9smwDjxFYhdL0vr2h6ACewAcP2-Sn3wzN1X710LjLHk7UxZNwHP0jlSyKpxQGsktHa8A-9Dv18pvLwzjeic5cm2KY3LNPzvdwdFgBxm8UlJx5jlD46-MtmWkWyb526h9FvSICKL5uFdi0uEMRrlN06X_8ZOIllGiRdS9FymCPpG0bC0ksUznO34TEyzFqyyGcGkHWGQZJf25CJdl4-I7c4frximhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد کردن تنظیمات بهینه در whitedns android</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/whitedns/1210" target="_blank">📅 12:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1208">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/HztEc68S6Meaa36R9yx3z7x9XSWar1tn0Q4UwLac1Kqu3sgqzz1tkRE-1SPHg6YopON9TQdAK_wjSJMlETlMlQiy6ZLmI19NYEiHHGWc4E0rvGf3wNubtZ6nb05VtNfOXeI_e_PjzDhDXuzm51g7yoTUzD7G5xNzisLAlMfdw7SisAVe7aEDq2Kb12uWM4dKfZXDGaOA8TFeqGfDhYuLThXubysHtUq2TxMnGN5bE250io-MpyqIDRv4SC8c53IaC5nn2ffyXzZMc1OjD6UCPCdeCVrtn2JI3CqJms9R2KjwZQHjUkaGkA7D0DHiL3siujji9S7QZLlf2IMUc-JveQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد کردن تنظیمات بهینه در Whitedns windows</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/whitedns/1208" target="_blank">📅 12:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1206">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Android.zip</div>
  <div class="tg-doc-extra">2.5 KB</div>
</div>
<a href="https://t.me/whitedns/1206" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/whitedns/1206" target="_blank">📅 12:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1205">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/DypDG2FtOoSrqqVUrSWSrZLces_xktdiKWqgxRhy_ydIbBttNmKG0J474YtwR85wbysnAZbL9cmHXhG2g9FH-7kS_GiewE_Zs57jQ_J_EquXOCeaNEDIsAt2NmwTqjeIh_xcVPUI1omhZnz07TYTa1WS_gGWII90kTmPJs9T_92rmqctEvFLWnF7xTsByVqTYHS939m6cH5ydbsDBG3MHWg-Q35iBgHUhv_K5X6cFBRCust1e7Q3w9r9un8L-VhaUGWDJX_mQL01Xe_DD7UiMAio-prFhg29j-ezufri6z3Xvr0cjb0vEWtWM8a_T84b2iF3rNl1euxbX0m69lhnBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
افزایش سرعت اتصال WhiteDNS
تنظیمات اختصاصی whitedns
یکی از مشکلاتی که بسیاری از کاربران با اون مواجه هستن، اتصال موفق
WhiteDNS
با سرعت پایین یا ناپایداره.
✅
یکی از مؤثرترین راه‌ها برای افزایش سرعت و پایداری اتصال، استفاده از تنظیمات بهینه میباشد (البته استفاده از سرور و کانفیگ اختصاصی هم تأثیر قابل توجهی روی کیفیت اتصال داره).
📦
به همین منظور، ۳ تنظیمات پرسرعت برای
اندروید
و
ویندوز
آماده کردیم که می‌تونید از اون‌ها استفاده کنید.
🍏
کاربران آیفون:
اپلیکیشن
CoreForge
به‌صورت پیش‌فرض تنظیمات بسیار مناسبی داره و در اکثر مواقع نیازی به استفاده از تنظیمات اضافی نخواهید داشت.
📥
نحوه استفاده:
• فایل تنظیمات رو مستقیماً داخل اپلیکیشن
Import
کنید.
• یا فایل رو باز کرده و محتوای اون رو
Copy/Paste
کنید.
⚠️
توجه
:
این تنظیمات فقط
مخصوص اپلیکیشن WhiteDNS
(مناسب اینترنت ملی) هستن و به درد استفاده در
WhiteDNS VPN
نمیخورن ؛ لطفاً این دو مورد رو با هم اشتباه نگیرید.
💡
نکته مهم
:
ممکنه این تنظیمات باعث افزایش مصرف اینترنت بشن. بنابراین بعد از اضافه کردنشون ، مقادیر Download Dup و Upload Dup رو متناسب با نیاز خودتون تنظیم کنید:
🔹
مقادیر
بالاتر
👈
مصرف اینترنت بیشتر
✅
اتصال پایدارتر
🔹
مقادیر
پایین‌تر
👈
مصرف اینترنت کمتر
✅
اتصال حساس‌تر و شکننده‌تر
❤️
امیدواریم این تنظیمات تجربه‌ای سریع‌تر و پایدارتر از WhiteDNS براتون فراهم کنه.
@whitedns</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/whitedns/1205" target="_blank">📅 12:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1204">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1204" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1199">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/whitedns/1199" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/whitedns/1199" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1198">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxSvaPnNWJKTSnry0rDSEiVcvM_sDJEqkiZwBTw1d9Woiu7DxtL3tRMBckQdosMDyC4JAokqUbENVx9JgbaZtOnNwnjIm8OwXcdyCpz0s8zbDnlrq5685cdCG4F-DDPtge_s8WcJOvJi_Lfxiuyz43yL8EeEteloLbgY_ID_R8tp0fjmT9wU4sv0T0IAMTj6dWqLLl3ZJkoo-5ekp0JZyuOkT_ujgbmzf5GNALzD5BMTNDb2WaFmchji5a0sIBewQ3lJEhwFyIDtklUPvHpMoBbCNcmMICFK3knPzqHZtFIFrNdiZ4ZVNkjxMneae_z2AbSRSkdqhNIerpueMC1h-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/whitedns/1198" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1196">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rml7lkZqps2TheTxxEQhNkDFtU9mYgbJdRtYL9rrpkOxhf8XQqbpgt9cZWcSKGlS_sjzrKMuvy9rrHctYtJUxP7yHwtdBjevlBd6Q_SKv02c80yQVBx0RPLBruwwll72Dhgecm4MxfF78ypWxvxxAU4PKujJdyPga-gXPo39XPtKq31vbpl7FhnGaMHwzJKGduc3xeSdrKZM1SFsLJiuTjI-QzTJrmppaAD00GA2fhlm2ux3Yrc08EuOJcuBF38y8jSxUoUfPCJEJGOUddVgLtWEpZmQVmbORtBGzPrkGbVsauKWgHU-v17bYG3txV-nJjLSO6S98UfuAruBxwALfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LEjyCn1OD776PfC9jnVRqns-hTUDt0pHv9RjYubwTp0m_4_bVOmM-61aWBh95RFbs9P4wPl2h22avpF28sCcBurMHlGcG8ejQ7trYnU_pgbwiaYzNzsGX5o7kSOVUafQzgs98SvzMcJwSPEyIWXATlv_6H0WU3JY4VYzY8VvukO8fZW2jT067C6hHbH2-GELTe2qoyRrS6bIzkpeZDOZZ2Oc4MjgUY03tiynNxftGqZFl9UeLqGaLR9mB8bjyjRGJSguTTp78hWJyybpf0qefvJUs2JLuAmyEzsExL66bRQ8xnVK_07LHd5VlWDgD9T4pgYtbxV92yB7EitLdb1z5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آپدیت جدید Aether-GUI (نسخه 0.4.0) با هسته‌ی جدید!
نسخه‌ی جدید برنامه آماده‌ست. توی این آپدیت، هسته‌ی اصلی (Aether Core) به ورژن
1.2.0
ارتقا پیدا کرده و قابلیت‌های زیر به GUI اضافه شده:
🔵
رفع مشکل وضعیت Connected فیک:
قبل از این، بخش Validation ابزار با پینگ کردن
1.1.1.1
(که داخل شبکه‌ی خود کلودفلر هست) وضعیت رو متصل نشون می‌داد؛ در حالی که ممکن بود ترافیک واقعی اینترنت قطع باشه و لود نشه. حالا ابزار یک ریزالور خارجی رو هدف قرار میده و باید ۲ بار پشت هم موفق بشه. یعنی وقتی می‌نویسه Connected، واقعاً متصله.
🔵
اضافه شدن انتخاب ترنسپورت برای MASQUE:
توی بخش Advanced الان می‌تونید نوع پروتکل ارتباطی MASQUE رو تغییر بدید:
HTTP/3 (QUIC):
حالت پیش‌فرض؛ سریع‌ترین هاندشیک و بهترین کارایی (اگر شبکه شما با UDP مشکلی نداشته باشه).
HTTP/2 (TCP):
کاملاً شبیه به ترافیک عادی HTTPS؛ مناسب برای زمان‌هایی که شبکه شما UDP/QUIC رو اختلال می‌اندازه یا مسدود می‌کنه.
تنظیمات انتخابی شما به‌طور خودکار ذخیره و در استارت‌آپ بعدی اعمال میشه. (این سوییچ فقط روی پروتکل MASQUE تاثیر داره و برای WireGuard/gool غیرفعاله).
🔵
به درخواست دوستان فرانت کار لوگو هم از دیفالت عوض شد
🤠
دانلود نسخه 0.4.0:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.4.0</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/whitedns/1196" target="_blank">📅 04:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1195">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/RXdt2IQ3vTGDjAPvWh_vXVQqTC8cpoN--8PMAksnxUwMp14gHOnMjcfd2d65iUNJMSEHbrHkLsAt3q7ZCJlMJY9oovmSVQWgaBokAnhQo8817-1McEsS8yx0rVGFdeiI9T0En3owb_pK_6IIAkXfEBRFfpxwg2lx91UogZ_mdHCcQAa66_gH9sEflM3iwvyO2RiQfUE8Rohqruvyu5xDM7rlEBI4K0Y9yk_4c-K8amjmnt92sjMf3yg7ZFBN4BRoNuIN57LHEaB9gpgv9L_WSgKw6a-dDgoKKePgZDVQYr-A-EdDslpk404crhvmhr_uO0Zjov0vbll6Vu13-S4eHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
راهنمای جامع تنظیمات APN اپراتورهای ایرانی
📱
📥
۱. مراحل تنظیم در اندروید (Android):
1. وارد
تنظیمات (Settings)
شوید.
2. به بخش
اتصالات (Connections)
یا شبکه و اینترنت بروید.
3. بخش
شبکه‌های موبایل (Mobile Networks)
را باز کنید.
4. وارد گزینه
نام نقاط دسترسی (Access Point Names یا APN)
شوید.
5. روی
افزودن (Add / +)
بزنید تا APN جدید ساخته شود.
6. فیلدهای
Name
و
APN
را مطابق لیست زیر پر کنید (بقیه گزینه‌ها مثل پروکسی و پورت حتماً خالی باشند).
7. از منوی سه نقطه بالا گزینه
Save (ذخیره)
را بزنید و آن را فعال کنید.
🍏
۲. مراحل تنظیم در آیفون (iOS):
1. وارد
تنظیمات (Settings)
شوید.
2. به بخش
Cellular (تلفن همراه)
بروید.
3. گزینه
Cellular Data Network
را انتخاب کنید.
4. در بخش
Cellular Data
، روبه‌روی گزینه
APN
مقدار مربوط به اپراتور خود را (از لیست زیر) وارد کنید.
5. یک‌بار اینترنت گوشی یا حالت پرواز را خاموش و روشن کنید.
📋
لیست مقادیر APN اپراتورها (برای کپی آسان روی کلمه‌ها ضربه بزنید):
🔹
همراه اول (MCI)
* Name: MCCI Internet
* APN: mcinet
🔹
ایرانسل (Irancell)
* Name: Irancell-GPRS
* APN: mtnirancell
🔹
رایتل (RighTel)
* Name: RighTel
* APN: rightel
🔹
شاتل موبایل (Shatel Mobile)
* Name: Shatel Mobile
* APN: shatelmobile
🔹
سامانتل (Samantel)
* Name: Samantel
* APN: samantel
🔹
تالیه (Taliya)
* Name: Taliya GPRS
* APN: taliyagprs
⚠️
نکته بسیار مهم:
اگر در فیلدهای
Proxy (پروکسی)
یا
Port (پورت)
در تنظیمات گوشی شما هرگونه عدد، آدرس یا کلمه‌ای وارد شده باشد، سرعت اینترنت شما به شدت افت خواهد کرد یا کاملاً قطع می‌شود. حتماً بررسی کنید که این دو بخش کاملاً
خالی
یا روی
Not set
باشند.
@whitedns</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/whitedns/1195" target="_blank">📅 16:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1194">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1194" target="_blank">📅 13:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1192">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :   ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.    پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/whitedns/1192" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1191">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1191" target="_blank">📅 12:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1190">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Y6IAvS_ABDt_DZ3rSgoee1ICHcLdH6lgAFDjNs-shDG74zdtErtGRz_XFLtzgpfBJXkCQc9UdfvKeR3FEdYwu5vvO_gvbXji2Ag5gd6vIbNsU5aMvzdW1WHVvxMFKTdawWs3fNz3FiSPPZxLQcabUYvdrHhWCEnoMq4pxW7jxG5Gxdm4sIWvzKQjvsDOCRfBJfUg07uYm5khp2uINJ3pXLholVrg2bxz7RdNcbkLHF-7txuwRuozrh9XrmzQ2mPgPYVeG00YAQG5agNFSoW7Gh33kxZZMh4ZCDT_aPGs7_SohLlO_DU_0YtVP2fKhLey6lh3KpW0-oZ9TQe0Ybnarw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :
ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.
پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است همیشه کامل یا دقیق نباشند. این ربات به اینترنت زنده دسترسی ندارد، جایگزین پشتیبانی انسانی نیست و اگر اطلاعات کافی نداشته باشد قادر به پاسخگویی نیست. لطفاً اطلاعات حساس یا شخصی خود را برای ربات ارسال نکنید.
برای مدیریت بهتر منابع و کنترل هزینه‌ها، محدودیت استفاده از ربات به شکل زیر تنظیم شده است:
- هر کاربر می‌تواند در هر ۵ دقیقه حداکثر ۳ سؤال بپرسد.
🕒
- سقف استفاده روزانه برای هر کاربر ۵۰ سؤال است.
📊
- در صورت رسیدن به محدودیت، ربات زمان تقریبی انتظار را نمایش می‌دهد.
⏳
- دستور /search و سایر دستورات عمومی شامل این محدودیت نیستند.
🚫
- محدودیت‌ها پس از راه‌اندازی مجدد ربات نیز حفظ می‌شوند.
🔄
این تغییر باعث پایداری بیشتر ربات و دسترسی منصفانه‌تر برای همه کاربران می‌شود. سپاس از همراهی شما
🌱
لازم به ذکر است در صورت سواستفاده این محدودیت بیشتر خواهد شد - پس خواهشمندیم با استفاده درست جلوی به ادامه این خدمات کمک کنید
لینک ربات :
@WhiteDnsResponder_bot
🔗
@whitedns</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/whitedns/1190" target="_blank">📅 12:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1188">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🛡
ورژن جدید WhiteDNS VPN
👆
👆</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/whitedns/1188" target="_blank">📅 11:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1183">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/whitedns/1183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/whitedns/1183" target="_blank">📅 11:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1182">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4kQKGZbdqNPCwV69Z6gKm-D0Sp4hHB9d0-QRy5ryigM4txo1Qj6FUOZNvSKwM8wt8mXX8lw3MQlILo_FobGhsh0Q-6vH4S9mje2XnR0qhKaF2mHFHFBfg8ZuLNISFmBVpSr63JNOiZW4hBk1V4lCwgY_m__GxNwukqDfF2VwKFtAfkzvFqtcfpQQR56iUx_tiiVNhVqdkd7RjxwXmlOlk5YAwHQKI0r_YpFISK6SoZdYe3ewWWXbC7qTFajwzY5NAsUcPi1Mw5_wHSMX35k4vD2zo_Fi7rwy7lTASWJBjyhGn0HmrlJLgNbjoCS_iYOknOj7CBSQ5VhlQHiATFDwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/whitedns/1182" target="_blank">📅 11:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1181">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1181" target="_blank">📅 08:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1180">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/mrGgyqWYeSa_uLz-a-JNU5qLghwg4iD6VdLAWL8dW5rde3iZPGEfV5jVKRQcg-QjQAXYZd5-m3xZUvUKbxU9r2kZN1p57H8molijZTPJjLT_HD1HatrsnmlMbFYfg5z6_CjEX0916jHCNVTFhqK5IV10NTnAM_l00f86scgpfJFEBLgiv6NSO94SvcxnS7w7UgOgswhNrybg1rA5fUKmQI3V14EzmXsENvSoB9Ytz_Mwk6OCgFOBUuzvo00A2XlPL_-ApIFJE40smYxgR0b5odMJXEt3Yp23x9cSSA41LH9RlkBo16QEeRKZPickFEmh9Gu0V10XfS_sLf820lj49w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی کانال یوتوب WhiteDNS
🌐
اگر به دنبال آموزش‌های تخصصی و کاربردی برای دور زدن فیلترینگ، پیدا کردن آی‌پی‌های تمیز و ساخت سرورهای شخصی هستید، این کانال یکی از بهترین مراجع آموزشی است!
🎓
در این کانال می‌آموزید:
🔹
آموزش صفر تا صد V2Ray
و راه‌اندازی پنل‌های ثنایی (3x-ui)
🔹
پیدا کردن آی‌پی تمیز با
WhiteDNS Scanner
🔹
راه‌اندازی
پروکسی MTProto
برای اتصال بدون قطعی تلگرام
🔹
معرفی ابزارها و کلاینت‌های مختلف (مثل CoreForge برای iOS و FlClash برای اندروید)
🔹
راهکارهای ارتباطی برای زمان قطعی کامل اینترنت
📡
و .................................
برای یادگیری ساخت فیلترشکن‌های امن و پرسرعت، همین الان به این کانال سر بزنید و سابسکرایب کنید.
👇
🔗
https://www.youtube.com/@WhiteDNS</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/whitedns/1180" target="_blank">📅 08:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1179">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✍️
در مدتی که اینترنت وصل بود، تیم ما تلاش کرد ابزارها و روش‌های جدیدی آماده کند تا در صورت بروز قطعی شدید، بتوانیم بهتر از شما پشتیبانی کنیم.
متأسفانه بسیاری از این ابزارها را تا امروز منتشر نکرده‌ایم که برای این تصمیم دلایل منطقی و امنیتی وجود دارد.
در صورت شروع محدودیت یا قطعی گسترده، تلاش می‌کنیم این روش‌ها را به‌تدریج معرفی و در اختیار شما قرار دهیم.
برای شروع، تعدادی سرور MasterDNS نیز منتشر خواهیم کرد. با این حال، پیشنهاد می‌کنیم در صورت امکان، یک سرور تهیه کنید و با استفاده از ربات زیر آن را به‌سادگی کانفیگ کنید:
@WhiteDNS_installer_bot
❤️
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/whitedns/1179" target="_blank">📅 04:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1177">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/j5a4wr_E5d3XkQd23prjtgXC8xJrUF4PpZ1jO0zSDfGO3IpCS7oS3Dv7I206CkHp150KKU-07rWS39U43DGpiSvsSgt9nnQCQg15tA7tvpYcI0pwgRNlXe5sPq3rKC3Te7sXYTgP8SQdNBxlO8xlNKDgesGj-9EttF-UEegiOELw31gQdGI3L2xiVWalLbVa4LcXjlAYiV0__TcMpci9ZPbx6zDVsZ0mkIr71rIFIhQZEXb9D5VyQZuuOGc147U7_yXmJqYWSnlM8jC1SHk2-kTOFx9u3Evu-JfH8cg5k0xoXijQXaDJJ-EribIScZOGDJ-gAtOjTpdIeuCLVgzazg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
دستیار هوشمند کانال WhiteDNS
👉
@WhiteDnsResponder_bot
✅
جواب سریع |
✅
۲۴ ساعته |
✅
رایگان
نحوه استفاده:
۱. روی لینک بزنید
۲. Start
۳. سوالتان را بنویسید
مثال: چطور فیلترشکن نصب کنم؟
/search عبارت — جستجوی مستقیم
/contact — ارتباط با ادمین
⚠️
ربات WhiteDNS در چه زمینه‌هایی جواب می‌دهد:
✅
فیلترشکن و VPN
✅
DNS و تنظیمات اینترنت
✅
آموزش نصب اپلیکیشن‌های WhiteDNS
✅
رفع مشکلات اتصال
✅
Warp و Cloudflare
✅
تنظیمات اندروید، آیفون، ویندوز، مک
✅
سوالات مربوط به قطعی اینترنت
❌
ربات قادر به پاسخ‌گویی به سوالات غیرمرتبط با موضوعات کانال نیست.
💡
نکته: اگر جواب دقیق نگرفتید، سوالتان را طور دیگری بنویسید یا از دکمه جستجو استفاده کنید.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/whitedns/1177" target="_blank">📅 17:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1176">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/e85B6vZWLvH0TFx8pAAjkUw12XfLqEXj6uYaVSQjr-mn2WCRddZJPdnpZMTqY6Q4DdurrYt9w_BtYAWDGF7HBKGq3KMJhDgoKNj5WBm2CPb7bX4fKG_hXF9w3L3Pf9pDx17GLX_xLeLPlZIE5X1Phl6Mf2OmmRDW8ug-FDTnAFD7b0TNZSflFQ97tlNjaAIMOYATX-pD3Ft40c5k-0Q9E1w3YTZUavHsaXgHl8smhoBPUlKYFtHWyhTceOjrEa1CHEbaGw-PHsevyEpllKTXqPBE_oMaaAdrmjGZccRzaQIuHibCRMRzZYHutrFgxHPRRIe-7Na2q1Sxp7D9HrmZ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
OnionHop V3.7.2 - انتشار جدید: اتصال هوشمند و عیب‌یابی شفاف
آیا می‌خواهید ترافیک سیستم خود را بدون درگیری با تنظیمات پیچیده از شبکه Tor عبور دهید؟ OnionHop، ابزار متن‌باز، سبک و قدرتمند ویندوز، برای همین کار ساخته شده است. نسخه جدید 3.7.2 تمرکز ویژه‌ای بر پایداری در شبکه‌های سانسور شده و شفافیت عملکرد دارد.
✨
امکانات و قابلیت‌های کلیدی:
🛡
حفاظت دوگانه:
انتخاب بین حالت
پراکسی
(سبک) و
VPN
(سیستمی).
🌉
عبور از سانسور شدید:
پشتیبانی کامل از Bridgeهای Tor، شامل
obfs4
,
Snowflake
,
WebTunnel
,
meek
, and
dnstt
.
🌍
انتخاب کشور خروجی:
امکان انتخاب دقیق کشور نود خروجی (Exit Node) برای تغییر موقعیت جغرافیایی.
🔒
امنیت بالا:
شامل
Kill Switch
(قطع خودکار اینترنت در صورت قطعی Tor)،
DNS امن (DoH)
و پشتیبانی از
IPv6
.
🚦
تونل‌بندی هوشمند (Split Tunneling):
انتخاب کنید کدام برنامه‌ها از Tor عبور کنند و کدام‌یک مستقیماً متصل شوند.
🤖
اتصال هوشمند (Smart Connect):
قابلیت جدیدی که به طور خودکار بهترین استراتژی اتصال، موتور Tor و Bridge را برای شبکه شما انتخاب می‌کند.
📢
مهم‌ترین تغییرات نسخه v3.7.2:
۱. تشخیص و تأیید ۱۰۰٪ پل‌های WebTunnel
در نسخه‌های قبلی، برنامه فقط آنلاین بودن CDN را بررسی می‌کرد. در نسخه ۳.۷.۲، OnionHop یک
اتصال آزمایشی واقعی (Handshake)
با خود پل برقرار می‌کند تا مطمئن شود که آیا واقعاً ترافیک را عبور می‌دهد یا خیر. این یعنی دیگر پل‌های خراب به اشتباه «سالم» نمایش داده نمی‌شوند و شما زمان را برای تست اتصال‌های مرده تلف نمی‌کنید.
۲. عیب‌یابی شفاف با لاگ‌های دقیق
اگر یک Pluggable Transport (مثل obfs4 یا Snowflake) به هر دلیلی اجرا نشود، دیگر با پیام‌های مبهم مثل "status code 2" مواجه نمی‌شوید. OnionHop قبل از اجرا همه‌چیز را بررسی می‌کند و دلیل دقیق خطا را در لاگ‌ها نشان می‌دهد؛ مثلاً: فایل اجرایی خراب است، نسخه اشتباه پردازنده است، یا مجوز دسترسی وجود ندارد.
🛠
راهنمای قدم‌به‌قدم اتصال (How-To Connect Guide)
براساس اطلاعات مخزن گیت‌هاب، نحوه اتصال بسیار ساده است:
نصب و اجرا:
فایل نصبی (.exe) را از لینک زیر دانلود کرده و اجرا کنید.
اولین اجرا (انتخاب حالت):
Proxy Mode (پیشنهادی):
اگر فقط برای مرورگر یا برنامه‌های خاصی به Tor نیاز دارید، این حالت را انتخاب کنید. نیازی به دسترسی Administrator ندارد. باید تنظیمات پراکسی برنامه خود را روی
SOCKS5 127.0.0.1:9050
قرار دهید.
TUN/VPN Mode (دسترسی ادمین):
اگر می‌خواهید
تمام ترافیک ویندوز
(کل سیستم) از Tor عبور کند، این حالت را انتخاب کنید. این کار با استفاده از Wintun و sing-box انجام می‌شود.
انتخاب پل (در شبکه‌های فیلتر شده):
به بخش
Scanner
بروید. اگر در شبکه‌ای با محدودیت هستید،
Bridges
را فعال کنید و روی
Scan
کلیک کنید تا برنامه‌ها پل‌های سالم را برای شما پیدا کنند.
اتصال:
روی دکمه بزرگ
Connect
کلیک کنید.
Smart Connect:
برای راحتی بیشتر، می‌توانید Smart Connect را در حالت خودکار قرار دهید تا برنامه خودش بهترین تنظیمات را اعمال کند.
🔗
لینک‌های رسمی
🔗
متن‌باز و رایگان
#اوپن_سورس
🚀
دانلود مستقیم نسخه V3.7.2:
https://github.com/center2055/OnionHop/releases/tag/v3.7.2
🌐
وبسایت رسمی:
https://www.onionhop.de
@whitedns</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/whitedns/1176" target="_blank">📅 14:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1175">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns16.7.2026.txt</div>
  <div class="tg-doc-extra">18.3 KB</div>
</div>
<a href="https://t.me/whitedns/1175" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@whitedns
🔗</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1175" target="_blank">📅 12:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1174">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/VaTa0UKWE7BmKLd2K3EjCyaVQoH31lYa52OFmluS-DMWtnYJRBlJjC0WkTDonpqxpdzoj24PY4Ovauw26r8LMSxAHXpx0XRSUr-2jxghXwLB8v9ex8pkhA13wIhyn_J3b_Fwkch3lrx9LhxEdovkgwtcvSnx_SjmoXO7Zsg9iXaPy8NRcG81VfA3QMsRsFExURs--MKveqO21ZsPvcM6QGxpiVykGZGH7ax2kRMIll5asFb8futnWepQtK4PXCBBUPKzE7Wf-b4boRiCxs53CL3zxUEIMh7tJVn57aO_owwmjnOq9Ulo-Bo-BeYtY8t5WmRPxNkfTjALs81TTvfqZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">16.7.2026
فایل زیر را دانلود کنید
⬇️
1. کانفیگ‌های داخل فایل را کپی و در برنامه v2ray وارد کنید
📋
یا
2. خود فایل را از طریق گزینه import locally در برنامه v2ray وارد کنید
📥
@whitedns
🔗</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/whitedns/1174" target="_blank">📅 12:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1173">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1173" target="_blank">📅 12:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1172">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/VPuka3vnwf9I9vQJ5cl5ckrQAwNg6CaROkGIPX8dHbX-YMOZFXM5CqxAxXtZCNEu0vE7Z8GfqZnTe2dRXLmF6cL0_Hf1LYNx0RJnSdGYZ3tSPnHxITpwgw0aaTLsBak2Oswo0qrG20ZzFEfZpnRyWr3zsvd4c7DW_I0k70LBl2rkJ400tH6eqV7F2tBgrWIJzptdP1h_TfEGc2N-RXJtI6lJkm9cXiEhs9Ublj0sJOG16iD3nuVLlmNygU_D3tOl6rUCwjkper1E4A6OpT5gTMbnQRKp-IEHBPAtKqW5n3chucxHZv2y50dbej8NQBaF9LtJ8pzCBnGmY69vpKiWdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش جامع استفاده از
WhiteDNS VPN
و
WhiteDNS Scanner
برای اتصال امن و پرسرعت!
🚀
🛡
رایگان
در این ویدیو به بررسی تخصصی ابزارهای اختصاصی *WhiteDNS* پرداخته شده است که به شما کمک می‌کند بدون نیاز به دانش فنی پیچیده، به اینترنت آزاد متصل شوید.
🌐
🔓
خلاصه‌ای از مباحث آموزش داده شده:
📝
راه‌اندازی WhiteDNS VPN:
نحوه نصب اپلیکیشن و اتصال اولیه بدون آی‌پی تمیز (0:00 - 5:30)
⚙️
📲
*
اسکنر قدرتمند WhiteDNS:
آموزش کامل کار با بخش *IP Scanner* برای پیدا کردن آی‌پی‌های تمیز و پرسرعت (7:40 - 18:00)
🔍
⚡️
*
کاربردهای حرفه‌ای اسکنر:
بررسی قابلیت‌های پیشرفته مانند *SNI Scan*، *HTTP Proxy Scan* و *Config Maker* برای ساخت کانفیگ‌های شخصی‌سازی شده (20:30 - 27:30)
🛠
🔧
*
نکات طلایی:
نحوه استخراج آی‌پی‌های تمیز از دیتاسنترهای مختلف و استفاده از آن‌ها در برنامه‌هایی مثل *v2rayNG* و *Psiphon* (22:40 - 25:00)
💎
🌍
✅
این ابزارها با رابط کاربری ساده، برای همه کاربران (مبتدی تا حرفه‌ای) مناسب است.
👨‍💻
👩‍💻
📥
لینک‌های دانلود:
- دانلود اسکنر: [GitHub WhiteDNS]
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/1.3.5
- دانلود اپلیکیشن: [Telegram Channel]
(
https://t.me/whitedns/1072
)
💬
با تماشای این ویدیو، سرعت و پایداری اتصال خود را به شکل چشمگیری افزایش دهید!
📈
🚀
لینک ویدیو :
👇
https://www.youtube.com/watch?v=N5hKuWXp37w&t=57s
@whitedns</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/whitedns/1172" target="_blank">📅 11:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1171">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/IT9oMVZ4oUe6GH0S8KnhD1YF1xFIWzXQeLNU_zscATmOvOkge1DOkxRZE54nLh9S2o3OEqCYeWXimjwRg6K4tEfRQbXK6G8HLOGWd6wyPE1HElgy7YuuGbumQmmDwJRJ0czdb5HkFjMWPWsmwddGrzVf15qoer5-ONpyvLr-CEj2HK2O04CwLg-HEDxzhmx5xKfxeJp2wNNtofhHK0xTiT2gMkuRHTBkFtdtz-TyFOJZZG8I9j_Hf-uc16MTkwXiq7ijQ2M4csWGgB2RLE2CdLfpG8YbYbHTzgVcKQv7z3RsNc5mqB4PZTX_yh3eq0css8ZXiTHpSvYSdntudIGuUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش کامل راه‌اندازی V2Ray با پنل قدرتمند 3x-ui از صفر تا صد!
🎓
اخیراً با کاهش محدودیت‌های اینترنت، روش‌های باکیفیت و پایدار دوباره فعال شده‌اند. در این ویدیو،
WhiteDNS
🛡
تمام مراحل راه‌اندازی سرور شخصی و فیلترشکن اختصاصی را به زبان ساده و کاربردی آموزش می‌دهد:
🔹
سرور و دامین:
نکات کلیدی برای انتخاب سرور خارج و ثبت دامین در کلادفلر
☁️
.
🔹
نصب پنل 3x-ui:
نحوه نصب این پنل کاربردی با استفاده از هسته Xray بر روی سرور
🛠
.
🔹
ساخت Inbound:
آموزش مرحله به مرحله ساخت اولین ورودی برای فیلترشکن
🔄
.
🔹
تنظیمات کلادفلر (Cloudflare):
نحوه ثبت DNS ریکوردها و تنظیمات امنیتی ضروری
🔒
.
🔹
استفاده از آی‌پی تمیز کلادفلر (Cloudflare Clean IP):
روشی برای بهبود سرعت و دور زدن فیلترینگ با جایگذاری آی‌پی‌های تمیز
🚀
.
🔹
ساخت کاربر و استفاده از کانفیگ:
نحوه اضافه کردن کاربر و دریافت کدهای تنظیمات برای استفاده در برنامه‌هایی مثل v2rayNG
📱
.
این ویدیو یک راهنمای کامل برای کسانی است که می‌خواهند فیلترشکن اختصاصی خود را با امنیت و سرعت بالا راه‌اندازی کنند. اگر هنوز شروع نکرده‌اید، این فرصت را از دست ندهید!
✨
برای دیدن آموزش کامل، روی لینک زیر کلیک کنید:
👇
🎥
https://www.youtube.com/watch?v=vVjqNQBUGIc
🆔
@WhiteDNS</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/whitedns/1171" target="_blank">📅 09:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1170">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jGGZnkELEs39_v8G1DCDQ2ipHZxFYeVMETXtCJQTk2EWuk34C5VCsGRGBkvt_fmXz-F3V0NV3k0Vo83bTFIOwlvQzeF1GFWr3JfifyX2_SyKSOMJ_R2kw2f2_1XULrwCPt0Rs9bkSalODwhiEy6Ouv0ou5qvnWvn2gK8-wjDUH3k1Nfg647_PSNLCwtshuCfwjWwYvu40aqkbIp-ElkX9q0EL_BvboYZtIIZn-ePAApjF8r1kc3x746Mb63qaOU9dB9H7QpVzU7CyFRm3i8IAPa-drKqDq6WELxF_kXWjpvi2a-qBThiGDb4NQClys9GNfmdyvfPLqDbXk_ery6cWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
اتصال رایگان و پرسرعت با پروژه Aether + پروتکل ویژه گیم Wireguard
⚡️
لینک پروژه‌ی اصلی:
https://github.com/CluvexStudio/Aether
لینک پروژه GUI من:
https://github.com/MatinSenPai/Aether-GUI
دستور نصب از ترموکس:
curl -fsSL https://raw.githubusercontent.com/CluvexStudio/aether/main/aether.sh -o aether.sh && chmod +x aether.sh && ./aether.sh install
دستور غیرفعال کردن محدودیت مصرف CPU و باتری:
termux-wake-lock
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره. حتی نیاز به اکانت کلودفلر هم نداره
😂
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/whitedns/1170" target="_blank">📅 13:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1169">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/kXjAvFFTxPIGzCrjAQ99sj9waU2U5rdxYG9Gq_k3I781kKq-0Bs8CpJNBM5wXHxmCB5zJzI8NntSFy75N_QG2jiRn1qDBpDR5vwCc2zbvp22Th6JohqnA4uC90XNaSYpSy-uuOIzbtbkcttxsEWszNRtfWwRs1iYw5-WDWZp6OjBclrmtPPmu3FdpiMNZ9lUNhfn3Wb8CwkBH2213MGVbibEvVLBsuTP8bitIE9i7j9t3N4B-XFJY42grZOb2qgGHYXhPJUq0MmmVVH15-qbYT0JlP7F-zUVkHlJ0oul7_IL_GnPN56avapa4CQlWrNErOO3zLM7N1fPKjKbPazSVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر برای استفاده از سرویس‌های هوش مصنوعی (AI) مشکل دارید
🤖
این پراکسی را چک کنید
🔍
برنامه یک اپلیکیشنِ نوار منو (Menu bar)  و یک داشبورد محیط ترمینال است که به عنوان یک
مرکز کنترل و مانیتورینگ برای ایجنت‌های Claude Code
عمل می‌کند.
به طور خلاصه، این ابزار کارهای زیر را انجام می‌دهد:
نظارت یکپارچه بر ایجنت‌ها:
وضعیت تمام ایجنت‌های در حال اجرای Claude Code را در یک نگاه نشان می‌دهد؛ بنابراین دقیقا می‌دانید کدام ایجنت در حال کار است، کدام متوقف شده (خطا داده) و کدام منتظر تایید شماست.
بررسی وضعیت اینترنت و سرور:
به صورت مداوم وضعیت اتصال اینترنت شما و سرورهای Anthropic را چک می‌کند تا در صورت توقف کار ایجنت، دلیل واقعی آن (مثلاً کندی اینترنت یا مشکل خودِ Anthropic) را به شما بگوید.
حفظ لوکیشن (Location Fencing):
ایجنت‌های شما را روی یک کشور خاص قفل می‌کند. اگر VPN شما قطع شود، به جای اینکه ایجنت‌ها با خطای دسترسی (مانند خطای 403) از کار بیفتند، درخواست‌های آن‌ها را موقتاً متوقف نگه می‌دارد تا دوباره به اینترنتِ همان کشور متصل شوید و کارشان را از سر بگیرند.
ردیابی مصرف (Usage Tracking):
میزان مصرف واقعیِ محدودیت‌های اکانت شما را (با خواندن دیتای خود Claude) به طور دقیق نمایش می‌دهد.
https://ghhrmnzdh.github.io/tower/
🔗
@whitedns</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/whitedns/1169" target="_blank">📅 09:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1168">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns 15.7.2026.txt</div>
  <div class="tg-doc-extra">48.7 KB</div>
</div>
<a href="https://t.me/whitedns/1168" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/whitedns/1168" target="_blank">📅 09:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1167">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/AdnD5xow2qXN75D8FXZ1DgXRCAh2Mlc7Bh0Cqq2DxqbQxct2aaktfAu-in9Z9v11LrQ-pD8S5lZ99ZMcFVkq6UaqXN1RpcFVpjOKa0Bxy7-DNoFWLm7dwDKb7oDQIdl5Ks2WFqKFlI9d2EmkyXBdxqeRabfQaVXCB1NAF4M9QmpKMspb3CTyWRuEE6p31z3dpWxlCJ_AK_RfEk18d2OTRUNdQnVvLjVuYWx0fDx90zWnhOvp7Q3hOB9z8kfcat9fs7g11iHJipRMHAgMjvA7G88lGiN2MHt_b-ZIMa7kkUGk5jw4Ck56tcO9lPRtxu6gsJ36GYhTqblnwqKlabGacQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">15.7.2025
📅
فایل زیر را دانلود کنید
⬇️
1. کانفیگ‌های داخل فایل را کپی و در برنامه v2ray وارد کنید
📋
یا
2. خود فایل را از طریق گزینه import locally در برنامه v2ray وارد کنید
📥
@whitedns
🔗</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/whitedns/1167" target="_blank">📅 09:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1166">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سلام به همه
👋
یک موضوع مهم که خیلی از کاربران VPN با آن آشنا نیستند، مسئله‌ی DNS Leak یا همان نشت DNS است.
شاید برای شما هم پیش آمده باشد که VPN روشن است و آی‌پی شما تغییر کرده، اما بعضی سایت‌ها یا سرویس‌ها همچنان شما را به‌عنوان کاربر ایرانی شناسایی می‌کنند یا دسترسی‌تان را محدود می‌کنند.
DNS نشت یعنی چه؟
وقتی وارد یک سایت می‌شوید، دستگاه شما ابتدا از یک سرویس DNS می‌پرسد آدرس واقعی آن سایت چیست. اگر این درخواست به‌جای عبور از داخل VPN، از طریق اینترنت اصلی یا شرکت ارائه‌دهنده اینترنت شما ارسال شود، به آن DNS Leak می‌گویند.
به زبان ساده، با اینکه VPN روشن است، بخشی از اطلاعات اتصال واقعی شما هنوز قابل مشاهده است.
چرا مهم است؟
DNS Leak ممکن است باعث شود:
• موقعیت یا کشور واقعی شما تشخیص داده شود
• بعضی سایت‌ها همچنان دسترسی شما را محدود کنند
• حریم خصوصی شما کاهش پیدا کند
• اتصال VPN شما آن‌طور که انتظار دارید کامل و امن نباشد
چطور تست کنیم؟
1. ابتدا VPN را روشن کنید
2. وارد سایت زیر شوید:
https://ipleak.net
3. چند ثانیه صبر کنید تا نتیجه نمایش داده شود
4. بخش DNS Addresses را بررسی کنید
اگر در نتیجه نام شرکت اینترنت شما، کشور واقعی شما یا DNSهای مربوط به اینترنت اصلی‌تان نمایش داده شد، احتمالاً VPN شما DNS Leak دارد.
پیشنهاد می‌کنیم همیشه از VPNهایی استفاده کنید که نشت DNS ندارند تا هم حریم خصوصی بهتری داشته باشید و هم سرویس‌ها کمتر بتوانند موقعیت واقعی شما را تشخیص دهند.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/whitedns/1166" target="_blank">📅 08:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1165">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Whitedns-14.7.2026.txt</div>
  <div class="tg-doc-extra">241.5 KB</div>
</div>
<a href="https://t.me/whitedns/1165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/whitedns/1165" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1164">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/efsVYUGdpXnzBbp9Q0CXuXszeCaH---sfHfRsHfAEim7zpieisF7Wr9mKdK7rZqoho9gWHL94VhgOuBvOHzMYXehJzMdnXE5m-CdLVEq98NhdCVYKm__rfzpjlPJciiqPNNeqA1vxS4W7ku5DhOkumcF3YtRmWbi2X-hQ9n6u_JKnyxJEeLDh3mqTcBbem_YGt51VqwZ_By0yi2BM4_OeTTxHCh07Nnt0C1cXg61yvZZoWDlxchxAA8M6D2Qy14K4HsKs3Rhbb0WvGfX-K2STp9eQJGm5XSWOEg_IuRHJ7rA4_u9yoV7n8T-tXQ6JvSh99Vx0XhdvBnJMKFoV9R-dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">14.7.2026
فایل زیر را دانلود کنید
⬇️
1. کانفیگ‌های داخل فایل را کپی و در برنامه v2ray وارد کنید
📋
یا
2. خود فایل را از طریق گزینه import locally در برنامه v2ray وارد کنید
📥
@whitedns
🔗</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/whitedns/1164" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1163">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/E-BqjAKXNjTTTsHgUOyZAOZwVDIjd0BOYLhahn5w_i8jdH14w31n8q7IKSZdvaDWmWoepoQN_7VVoTwAAcpSN_e4ldqem_5NesVRRZAoTrKly2aUnAMX6Mqv27hc64JcLz9ZfqQF4SGILM3ovy4XNYsWQPYI2pzyfEXkMd-My_9kJafMzqarRAgxiG_E7sKP95npBBPwdCG3uvjokEIi_D4lBnUkHNcNAtVULAdXwhLwZsmjEp2nVe-wDrZpKPCH6QGLPrpuiWYAtdFm0Pnm3E_lRq0SDHuGwp7gk6gM-cdD4dpXG7PxsnzaTldgk8gvJxt2UM55tVe6dxXlXSHa1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
دستیار هوشمند کانال WhiteDNS
👉
@WhiteDnsResponder_bot
✅
جواب سریع |
✅
۲۴ ساعته |
✅
رایگان
نحوه استفاده:
۱. روی لینک بزنید
۲. Start
۳. سوالتان را بنویسید
مثال: چطور فیلترشکن نصب کنم؟
/search عبارت — جستجوی مستقیم
/contact — ارتباط با ادمین
⚠️
ربات WhiteDNS در چه زمینه‌هایی جواب می‌دهد:
✅
فیلترشکن و VPN
✅
DNS و تنظیمات اینترنت
✅
آموزش نصب اپلیکیشن‌های WhiteDNS
✅
رفع مشکلات اتصال
✅
Warp و Cloudflare
✅
تنظیمات اندروید، آیفون، ویندوز، مک
✅
سوالات مربوط به قطعی اینترنت
❌
ربات قادر به پاسخ‌گویی به سوالات غیرمرتبط با موضوعات کانال نیست.
💡
نکته: اگر جواب دقیق نگرفتید، سوالتان را طور دیگری بنویسید یا از دکمه جستجو استفاده کنید.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/whitedns/1163" target="_blank">📅 17:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1162">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">White DNS
pinned «
👆
⭕️
⭕️
⭕️
⭕️
موقت :   پرونده اتصال سریع و اسان برای افرادی که دانش و امکان درست کردن کانفیگ ندارند با چند پست بالا بسته شد   این مدل اتصال در صورت قطعی  سراسری کار نخواهد کرد
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1162" target="_blank">📅 17:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1161">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👆
⭕️
⭕️
⭕️
⭕️
موقت :
پرونده اتصال سریع و اسان برای افرادی که دانش و امکان درست کردن کانفیگ ندارند با چند پست بالا بسته شد
این مدل اتصال در صورت قطعی  سراسری کار نخواهد کرد
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/whitedns/1161" target="_blank">📅 17:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1156">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-IP-Scanner-x86_64-release.apk</div>
  <div class="tg-doc-extra">15.6 MB</div>
</div>
<a href="https://t.me/whitedns/1156" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اگر براتون سوال پیش اومده که لیست ipfronting ها را از کجا آوردیم . پاسخ خیلی ساده است
😊
👇
با استفاده از Whitedns Ip finder
🛠
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases
📂
@whitedns
📱</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/whitedns/1156" target="_blank">📅 17:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1155">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qrCVdtJs6i1Sm9q7pNZJwPd8Dw-D5FiKSIaPFu87ft9cN95ODpEogH7yivx-CGabqkafYRf3rrmi9ScsIZmvd9wiTb6-xIqiKChPIYCzU2DR4kiDbxYheewIV2AAsf6eAr5iL3APdAS8SVaJ0h48ZexTrXC5W9oZaGe0EE-ugcOFifzhtDoJRVFGQzFQobNQ1bc7frWxlIU1RXXeeJKboIUZGLx_gh71Ri-2adgp8L5vTDx0MvmDmrTI_vKQRuMUnlGUjKLda_TNiA-igqSl1wGxGWciX3P3v20YOdUjNKuEPCmesfVDV2vzTO7zBLojhNh9ysDxfmvaVYnNkv5c_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/whitedns/1155" target="_blank">📅 17:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1154">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/XDVLStbNOjt0Md56BVsb-wUiDkWvXaC_AqkOeaYveObOiK5CTnD2b2TNm525HKJC71ugCuQMQmSNtXhkDMsdy7bWMcGuvVMPNeNbMOnUI5CZsCVVa-aufxutrSgfiFQ5gQ8a34mNLVaZoPKDzySQhyzf4gk8QvSfc4noniLWncoSJ3QvlrNrhYF4mq8gf2mKDHa2KtxUDIWiTmHCT9pxmk8-8gBTI0turjEjb279slgck0RKj0H0pS1FzLSE_HSHryi_W-vyy1orzQcpXxqPNlzd_G-qrj_KgQBoQZx1v3B9ngmPEfD8mV2kn-r0h5WcWHFKbulLz8l-ZeNOw46GPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان :
در صورتی که موفق نشدید با برنامه whitedns vpn وصل بشید
🙄
🔌
وارد قسمت advanced بشید و ای پی های زیر را دونه دونه امتحان کنید
👇
🛠
2.189.86.45
2.189.86.102
2.189.86.42
2.189.86.46
2.189.86.41
185.8.173.179
2.189.86.44
45.149.77.160
194.62.43.166
94.101.184.211
37.152.185.169
37.152.182.54
185.226.118.234
185.231.182.55
185.226.118.234
185.231.182.55
185.226.117.67
185.228.236.4
2.189.86.43
2.144.21.79
2.144.21.120
2.144.21.79
2.144.23.129
2.144.21.120</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/whitedns/1154" target="_blank">📅 17:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1152">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">White DNS
pinned «
دوستان :
👋
یک مورد کوچیک در مورد whitedns VPN بگم
📱
این اپلیکیشن بر اساس کانفیگ های متناسب با هسته x-ray یا سینگ باکس هست ، به طور مثال vless ,vmess, Trojan ,....
⚙️
اگر وصل شد حتما اول با مرورگر یک تست بگیرید
🌐
، اگر هیچی باز نشد ، دکمه refresh را بزنید…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1152" target="_blank">📅 16:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1151">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دوستان :
👋
یک مورد کوچیک در مورد whitedns VPN بگم
📱
این اپلیکیشن بر اساس کانفیگ های متناسب با هسته x-ray یا سینگ باکس هست ، به طور مثال vless ,vmess, Trojan ,....
⚙️
اگر وصل شد حتما اول با مرورگر یک تست بگیرید
🌐
، اگر هیچی باز نشد ، دکمه refresh را بزنید
🔄
اینقدر این کار را تکرار کنید تا یک کانکشن پایدار متناسب با وضعیت شما براتون پیدا بشه و هر بار تست کنید روی مرورگر
🧪
✅
تیم whitedns
👥
@whitedns
📩</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/whitedns/1151" target="_blank">📅 16:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1146">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.8-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/whitedns/1146" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اپلیکیشن Whitedns vpn 0.0.8
📱
یک برنامه بر پایه هسته‌های x-ray و singbox است که بدون نیاز به وارد کردن اطلاعات و تنها با فشردن دکمه‌های Connect یا Refresh، به راحتی یک اتصال اینترنت مناسب ایجاد می‌کند
🚀
🌐
.
ٌ
@Whitedns</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/whitedns/1146" target="_blank">📅 16:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1145">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Dlsj1OJvchYfPpLAd6TLPotTv7W954xTo6QAzw4PK2Ttyz36-UfkqKXZSvtzEIdTqqMQ1iTyBqH7o7TVnkJmDiiw82eaG6U1Mm_EUEUtUmSNla2vCP-yzhLTbtg32l4_vTJggf7g1x9p2NyLJ5hyFdw5FtG5NR3D-M7FaxedwS8hhjys0LUc9LDSO2BUpaGKF82VWeGuEEvh7IsWzHM7HQBoKj5TXpsIyjIXBvFTyCCBp3TxKxD_Min4NxVubRuDEvWsxMdc1Jj1TJVWX20zDOVcdy55D4CEM-oB3gmjhamlIrM57YNWxqHINTjLqzb4jd_7EaHwXbIzB1ItxlJNtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/whitedns/1145" target="_blank">📅 16:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1144">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">برای اینکه دوستان قاطی نکنند، ما دو نوع اپلیکیشن برای اتصال داریم
📱
:
۱
. اپلیکیشن بر پایه پروتکل‌های DNS محور مثل masterdns, stormdns, ...
🌐
مثل Whitedns 1.5.1
۲. اپلیکیشن بر پایه هسته‌های x-ray, singbox که پروتکل‌هایی مثل vless, vmess, ... دارند
⚙️
مثل  0.0.8 whitedns vpn</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/whitedns/1144" target="_blank">📅 16:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1136">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-poll">
<h4>📊 وضعیت اینترنت چطوره ؟</h4>
<ul>
<li>✓ ☺️مثل قبل هست  , وصلیم</li>
<li>✓ 😔اختلال داره ولی وصلیم</li>
<li>✓ 😡اختلال شدید ، به ندرت وصل میشیم</li>
</ul>
</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/whitedns/1136" target="_blank">📅 16:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1135">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🛡
مدتی پیش اپلیکیشنی برای اسکن Resolverهای متد DNS ساختیم که می‌توانید آخرین نسخه‌ی آن را از لینک زیر دانلود کنید:
https://github.com/WhiteDNS/IP-Range-Scout-Android/releases/tag/v0.1.2
اگر امکان اسکن Resolverها را ندارید، می‌توانید از ربات ما استفاده کنید:
@dns_resolvers_bot
همچنین اگر برای اولین‌بار از WhiteDNS استفاده می‌کنید، پیشنهاد می‌کنیم در گروه اصلی، تاپیک «اولین شروع» را مطالعه کنید.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/whitedns/1135" target="_blank">📅 03:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1134">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">درود به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه. با توجه به شرایط کنونی خاورمیانه، ترجیحا هم اپلیکیشن WhiteDNS را نصب/آپدیت کرده و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/whitedns/1134" target="_blank">📅 03:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1133">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">درود به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
با توجه به شرایط کنونی خاورمیانه، ترجیحا هم اپلیکیشن WhiteDNS را نصب/آپدیت کرده و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی دست یابید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/whitedns/1133" target="_blank">📅 00:33 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
