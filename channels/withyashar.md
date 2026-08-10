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
<img src="https://cdn4.telesco.pe/file/Tr2qaGWDeCWS59IZD8ajN28a9Zq2zIH_veViWfXPI11t_FWB7HdaRQw56vAn7epoTznmBsnlD7P1bbWxXZb3ln145cBVWcVSKoE7Y7pw1TjYXBhRRjlMUCulAIT1UxFX7qZ4uHwrLfJgiyY2Y-2I8sM28Uj8CG-JDTkx8HQlg-qQSPhpqEMNRAeMa_3kcBrAFgYijyVDTKi61xxxd0WvtstGL-MZWNp7JB6YrymhZalIquSHdl9Q3jlTyZQnnsB5r8hZTw_JXjafNUk6_G-UidBYVT2N-6ZiHmQyUl3Xp6bnvG1bAgnMP-Yf_FPuu6HagXq1_2sEuqt4KC3GugSP5A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 446K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 00:39:06</div>
<hr>

<div class="tg-post" id="msg-20789">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کامنت جدید برای ترامپ (کارای اداری)
آقای رئیس‌جمهور، فن آخر استاد را اجرا کنید
🎯
https://www.instagram.com/reel/Db30SjjS-Wl/?comment_id=18183518170406206</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/withyashar/20789" target="_blank">📅 00:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20788">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏
رسانه‌های سعودی: اسماعیل قاآنی، فرمانده سپاه قدس، به بغداد سفر کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/withyashar/20788" target="_blank">📅 23:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20787">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عراقچی در تماس تلفنی با همتای آلمانی خود: تضمین امنیت تنگه هرمز مستلزم توقف اقدامات تهاجمی آمریکا، به ویژه محاصره است.
@WarRoom</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/withyashar/20787" target="_blank">📅 23:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20786">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ: رئیس‌جمهور بعدی بابت کارهایی که من انجام داده‌ام، اعتبار زیادی دریافت خواهد کرد.
لطفاً یادتان باشد که این من بودم، نه آن‌ها.
@WarRoom</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/20786" target="_blank">📅 23:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20785">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خبرنگار: آیا پاسخی به نتانیاهو دارید؟
ترامپ: من امروز آن را در تروث منتشر کردم. من یک پاسخ دارم، یک پاسخ خوب. بله، رابطه خیلی خوب است.
@WarRoom</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/20785" target="_blank">📅 23:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20784">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6383d52564.mp4?token=hHtSHoAekO9-IGNF2hwChxDPWK9nssUzaStgk4u5Rm4Pu3YMvIi6qXIF8KU197q5jE4RzwovfKEsIIiQVStbt9E4UrT7FcBx0xgMuxsM9nF7UBIkgYEw0aT7biJSEsNQUAiOWKoCg0uexMXK-yMBygP6IPVjBjuyys75DuqZYpMkfgYna26uzCVejkZBtOKFpUB5W1g9gj14IpUeEuH4125eOQqYiixihnd5EelnGkCPl0THbLbhIGDL7gSK3TUMTJoLAzPKx7MUOStmrx3bOhxlGzQBBz_TRghGwfTgKuIkwbUEust6tppTEkUolSilgSsQubbtSYiLwm9L69yt9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6383d52564.mp4?token=hHtSHoAekO9-IGNF2hwChxDPWK9nssUzaStgk4u5Rm4Pu3YMvIi6qXIF8KU197q5jE4RzwovfKEsIIiQVStbt9E4UrT7FcBx0xgMuxsM9nF7UBIkgYEw0aT7biJSEsNQUAiOWKoCg0uexMXK-yMBygP6IPVjBjuyys75DuqZYpMkfgYna26uzCVejkZBtOKFpUB5W1g9gj14IpUeEuH4125eOQqYiixihnd5EelnGkCPl0THbLbhIGDL7gSK3TUMTJoLAzPKx7MUOStmrx3bOhxlGzQBBz_TRghGwfTgKuIkwbUEust6tppTEkUolSilgSsQubbtSYiLwm9L69yt9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ایرانی‌ها صدها هزار نفر را کشته‌اند.
حالا دارند تاوانش را می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/20784" target="_blank">📅 23:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20783">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ در مورد ایران:
آنها می‌توانند دردسر درست کنند، اما ورشکسته هستند. آنها پولی ندارند.
ایران کاملاً ورشکسته است. آنها حقوق سربازان خود را پرداخت نمی‌کنند.
تورم آنها 309 درصد است.
@WarRoom</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/20783" target="_blank">📅 23:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20782">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e43e103fdf.mp4?token=qRvmhlbTHgf02NIIdp6GB9OcRv7hQeEm6RMqclbM-L006O2Ou6WScT_JX6QzP4l-XF6WLh72prw7VUGx7oWi0ggk7q1sIv_oI7G5GKQj25outXBLjpASz9JracdMxNY-H8p0ZhHq2Sc96Ud7wH1vLjHuRgHC1u131GnG5fuuDzcYd7xwNwyRJvZT-Ynb-4U0lf0TUzgq6LbZ1Lgtu7BkVEvjq5GHxNKZoG-21_svV_7N7jHAdgF-plGpOzL5GhAdvMjV4wGhktMMCdG6poSUybuSyB3nbK61hSbS11TkGAEjBZ6dgkCxgaC9uhCrWKQphh7O2D5xFR-V3Fq5jATT1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e43e103fdf.mp4?token=qRvmhlbTHgf02NIIdp6GB9OcRv7hQeEm6RMqclbM-L006O2Ou6WScT_JX6QzP4l-XF6WLh72prw7VUGx7oWi0ggk7q1sIv_oI7G5GKQj25outXBLjpASz9JracdMxNY-H8p0ZhHq2Sc96Ud7wH1vLjHuRgHC1u131GnG5fuuDzcYd7xwNwyRJvZT-Ynb-4U0lf0TUzgq6LbZ1Lgtu7BkVEvjq5GHxNKZoG-21_svV_7N7jHAdgF-plGpOzL5GhAdvMjV4wGhktMMCdG6poSUybuSyB3nbK61hSbS11TkGAEjBZ6dgkCxgaC9uhCrWKQphh7O2D5xFR-V3Fq5jATT1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: تنگه هرمز کی باز می‌شود؟
ترامپ: الان باز است.
ترامپ در مورد ایران:
همانطور که احتمالاً شنیده‌اید، ما تمام تنگه را مین‌روب کرده‌ایم. شاید نشنیده باشید.
ما ۱۰۰٪ تنگه را کنترل می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/20782" target="_blank">📅 23:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20781">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ: اگر قرار باشد خسارتی پرداخت شود، ایران باید آن را بپردازد
ترامپ: تشدید شدید تنش‌ها همچنان یک گزینه است
@WarRoom</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/20781" target="_blank">📅 23:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20780">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خبرنگار: شما گفتید این آخرین فرصت ایران است. حالا چی؟
ترامپ: خواهید فهمید.
@WarRoom</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/20780" target="_blank">📅 23:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20779">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ درباره ایران:
هیچ اتفاق بدی در نتیجه اقداماتی که ما انجام می‌دهیم، رخ نخواهد داد. هیچ اتفاق بدی رخ نخواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/20779" target="_blank">📅 23:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20778">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOA4keGb9aVVwirohPmXwdCemJAeNWZovVHqD8hTOkvRgrHWqNp42hlznRw5UwC-aMwOnKXmC50KU-DYy-HwfzJ5FemHfdA60uEpdgT9uPMcs1bnubr33AzxU_AIYu9pngzPMWMmPgkq0n30-7kQpcrxADOD8Aqofyhc6RMKpn1iDn3fVY_gxJKghu20I3jnw3wR8v2Szddo9gkHkqTUKDh6_LHPepICwB_JpzCE2ASC3LqGpiTmFAshU6GVDn8OW2IiigbDgGKD5N83Ada9OwOsVE2BvUz49J6OQHvLiGB9KjmmFgDegBh77SYi1kveXR_ijSi447OSqcyE4W5y7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار دریافت غرامت بابت خسارت‌هایی شده‌اند که در جریان درگیری نظامی پنج ماه گذشته به آن‌ها وارد شده است؛ درگیری‌ای که از آن‌جا آغاز شد که آن‌ها نباید به سلاح هسته‌ای دست پیدا کنند. با این حال، چنین…</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/20778" target="_blank">📅 22:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20777">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پرتاب موشک/پهپاد از سیریک
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/20777" target="_blank">📅 22:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20776">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7OqoJTqrYJStDGYWL4vX1TJ__KbWl-M0KUx3zA8GRFDRas6etQN28MwoXbZRhqCPUqPkcOwrHrtHJ11YVjD3CqR_TOwxpZcLsSqX9JSSVM87uEM_zT7jPjUR0qyDtgwKKvLl1YFGFssRw8ubqS5-xg5opXOSd9eTjYSZxi2mmsNHohsnU3WU0Iv5Ia6JYqAH0EqeND8RpV5Kfd3Hg8YyJkH6Pmv82AERWlQrksHJoWDQVfu2HGgVJyjfaOUbINQ44M65PAxxsJIBa-a8-FGFndtOBU5IAPFRAxWopxesmENsp6PHCvoWZ_SxlUzHibrTzwB4yEL6CmWKOHy2IUZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان KC-46A پگاسوس نیروی هوایی آمریکا از پایگاه‌های مبدأ خود در غرب ایالات متحده به پایگاه هوایی مک‌دیل در فلوریدا، در شرق آمریکا، منتقل شده‌اند؛ جابه‌جایی‌ای که می‌تواند نشانه‌ای از آماده‌سازی برای اعزام قریب‌الوقوع شماری از هواپیماهای پرمصرف (احتمالاً بمب‌افکن‌های بی-۵۲) به انگلستان و سپس خاورمیانه باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/20776" target="_blank">📅 22:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20775">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏کانال ۱۳ اسرائیل گزارش داد که این کشور به آمریکا اعلام کرده به هدف قرار دادن نیروهای حماس که در حمله هفتم اکتبر مشارکت داشتند، ادامه خواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/20775" target="_blank">📅 22:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20774">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7c44f7cd8.mp4?token=Za2ooU-u6EQQR_sk9RLQGrImOZADtMPVoG0g2THNxwr5-6jncdYtM_2mZtqnVfgk81KY7bOOAL5rWobvjTjKnGImAh1sU5wXf4WyA6AE4Xxa9ErgzETtOSO6dghXOjw3HoNpmRdZ8XIjInI7QUDRQEZiC7-eC82-1dtGHwAC0036tpcEotKSjCP9us_hdTvle7H_ZGuRa1cCRJO3TViSO_HYZGMXUB0dGDx5TTQ-x5wIQJqRb90lFGNCfJsxvfBpsd7pd6iyIKlxzLPo2-t2UHZA39lhd5TOCsb1RLW8uoo-S44ylkQNggcpdTcpu7LsrEnbs2wyCsYRVxIAZtCMSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7c44f7cd8.mp4?token=Za2ooU-u6EQQR_sk9RLQGrImOZADtMPVoG0g2THNxwr5-6jncdYtM_2mZtqnVfgk81KY7bOOAL5rWobvjTjKnGImAh1sU5wXf4WyA6AE4Xxa9ErgzETtOSO6dghXOjw3HoNpmRdZ8XIjInI7QUDRQEZiC7-eC82-1dtGHwAC0036tpcEotKSjCP9us_hdTvle7H_ZGuRa1cCRJO3TViSO_HYZGMXUB0dGDx5TTQ-x5wIQJqRb90lFGNCfJsxvfBpsd7pd6iyIKlxzLPo2-t2UHZA39lhd5TOCsb1RLW8uoo-S44ylkQNggcpdTcpu7LsrEnbs2wyCsYRVxIAZtCMSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرمانده ستاد کل نیروهای دفاعی اسرائیل در کنار فرمانده سنتکام: "ماموریت ما این است که بر واقعیت تأثیر بگذاریم، نه اینکه تسلیم آن شویم."
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/20774" target="_blank">📅 21:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20773">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پرتاب موشک/پهپاد از سیریک
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/20773" target="_blank">📅 21:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20772">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">جان بولتون : کناره‌گیری از رویارویی‌مان با ایران یک اشتباه است. ایالات متحده ضربات سنگینی به ساختار نظامی رژیم ایران وارد کرده و سال‌ها طول خواهد کشید تا آن را بازسازی کنند. صرفاً به این دلیل که نمی‌دانیم اهداف نهایی‌مان چیست، نباید با دادن یک پیروزی سیاسی به این رژیم، برتری بر تنگه هرمز را به آن ها واگذار کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/20772" target="_blank">📅 20:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20771">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/544e884864.mp4?token=BU24txsH2kM8UA6pHIBq32bN_NBpx_06Gfxz6pyB4blLsCjIWy97TU33AmiPHT1YfW_T7Jo6F1j_z2ls6ysqM6UDbTsNevHGG4PGuc74UuJi_8KsX4yUa22t8e_gU2zwIn4kvBUlQJsWHUjM_wqDSXftKHNpIJ9g_XKlCSmZq21-I3mhYytAG2sqV6eUX_IPDFoFQe132z93QcCteQ6Hz5YxO01cyjaIsIWvhU07u8XXWlzILXl3GYR_nksOydjgQxZjaSqj6rFy9ASEFxS6Uhnlcshq-WYAblgfx3Z6uT8SuFhe4SMhf_W0ZgiEhlb1-ZsjuexBvxOgi0BB7TbJBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/544e884864.mp4?token=BU24txsH2kM8UA6pHIBq32bN_NBpx_06Gfxz6pyB4blLsCjIWy97TU33AmiPHT1YfW_T7Jo6F1j_z2ls6ysqM6UDbTsNevHGG4PGuc74UuJi_8KsX4yUa22t8e_gU2zwIn4kvBUlQJsWHUjM_wqDSXftKHNpIJ9g_XKlCSmZq21-I3mhYytAG2sqV6eUX_IPDFoFQe132z93QcCteQ6Hz5YxO01cyjaIsIWvhU07u8XXWlzILXl3GYR_nksOydjgQxZjaSqj6rFy9ASEFxS6Uhnlcshq-WYAblgfx3Z6uT8SuFhe4SMhf_W0ZgiEhlb1-ZsjuexBvxOgi0BB7TbJBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایگاه مشترک چارلستون رسماً به پایگاه مشترک لیندسی گراهام تغییر نام داد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/20771" target="_blank">📅 20:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20770">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrD-Wzw3VvgRmL4m80kANAoCvMDA3Gh5yguh0iGm4SD5Eb51gIL2-85KAYu9lUcIpIMKcU4hJJvn-ZJ2J0b8H97HtznL95Ct4P--hdJZUYYyrXfMbAOdiDEFmDVKmS0SuLi9qxFV4yPEcux1YbUlBUAqXYUmx4EAYEF82MLAtzFfFoY7jVqijoZyNlB44RLVr2JKZiaIpnb_bOh_ySjrHXMFShQrjQl602u_6fyk0FsT075E9TXCWbOfADizdSjLFAM0gBoi4cykeBvUMuKGCxYs44-odkS67q4B8WTJruMJ381iUE49xfdEg8uAbwm9yyyftT5NGSC1NykIAqz3oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار دریافت غرامت بابت خسارت‌هایی شده‌اند که در جریان درگیری نظامی پنج ماه گذشته به آن‌ها وارد شده است؛ درگیری‌ای که از آن‌جا آغاز شد که آن‌ها نباید به سلاح هسته‌ای دست پیدا کنند. با این حال، چنین موضوعی هرگز در هیچ‌یک از مذاکرات یا دیدارهای ما مطرح نشده بود! اما این ایده جالبی است، زیرا حالا من نیز از ایران درخواست غرامت می‌کنم؛ بابت تمام افرادی که با بمب‌های کنار جاده‌ای و درگیری‌های متعدد، که به آن‌ها شهرت دارد، کشته یا به‌شدت مجروح کرده است؛ اقداماتی که در ابتدا تحت هدایت ژنرال سلیمانی انجام می‌شد. این شامل خانواده‌های کشته‌شدگان ناوشکن یو‌اس‌اس کول و هزاران نفر دیگر که در نبردها جان باختند نیز می‌شود. افزون بر این، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران طی ۵۰ سال گذشته کشته است نیز غرامت پرداخت شود؛ چه برسد به ۵۲ هزار نفری که در پنج ماه گذشته جان خود را از دست داده‌اند. به نمایندگان خود دستور داده‌ام که این موضوع را با قاطعیت در همه مذاکرات آینده مطرح کنند. از توجه شما به این موضوع سپاسگزارم.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20770" target="_blank">📅 20:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20769">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مرندی ، مشاور تیم مذاکره کننده : جمهوری اسلامی آگاه است که نیروهای دولت ترامپ در خاورمیانه در حال آماده‌سازی برای یک حمله برق‌آسا هستند؛ حمله‌ای که ممکن است با همراهی نیروهای اسرائیلی انجام شود.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20769" target="_blank">📅 19:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20768">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">با حکم مجتبی خامنه ‌إی آی، علی عبداللهی فرمانده ستاد کل، احمد وحیدی به سرلشکری فرمانده کل سپاه، کیومرث حیدری جانشین رئیس ستاد کل، ایزدی جانشین فرماندهی سپاه، عظمایی فرمانده نیرو دریایی سپاه و طائب رئیس بسیج شد
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20768" target="_blank">📅 19:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20767">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhMcK7Fgg6bghxZpubMPLVpXgD_VX3Pv7IX1fse5_BQ7IHY-llMQw_JQpmGKrTrFnFdjxM8_HF9ZHTv5CStesVUd3tS9GAUxDONDu6Mqd-ZZAaKwGCiNGRXnCun3SB54TeYXTVMort1O6_LyOD3S9LlRJQPLfX18PBKdHoUWezH5oqpleV2BOh5RhYE0KZSQsxccR3S6jni3ehDYcJMys8nw8JZt31ADkYfM4hFa4HzrnpUYwsUPg427p4DU62lKrlqbwlZmTQqB-yLC77bE5yFnc53Z4_c0RPn1H2JXzNynvbbw0g7FM70Va_MrRLRCSyRb8c0y_9x1z7ybYp5ulA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : جمهوری اسلامی متوجه شده که با بالا نگهداشتن قیمت نفت، حمله قریب الوقوع آمریکا را به تأخیر میاندازد. امشب، ساعتی قبل از باز شدن مارکت، این حمله ها را انجام داد و هم اکنون با باز شدن مارکت، نفت در لحظه نگارش این متنالان حدود سه دلار گران…</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20767" target="_blank">📅 19:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20766">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHl3r-kFR-piaRfoAvwgqz4gTeSDGAxkRvvGtovr_bgy2j83MHOk4q6ktUdns3xkGcmZSF6cKubpwPCI4aURksxuRnXKDYJj71BHHxyzn1iuEoR5plWn7EMzGy02t-xOfZACZO-7jFvyuOGvcZ8JZ6gDall7SHMeYLxY3BNId1QTq8v5eFiDrWMT_ej7zvm4hr6QEhve-bxx5Ta4tMfyPmbdFLsRTM_s7EyOY_ZwIkCW35yjDtIRxa3s3ZxpZh6tgurNYT3Zw_qxzDL-8kV0vv8cddBvEW28OFpHGbeGu_tCyE8iyRoygx_tg6ix6_rwQMPxmuRPEiZIR6jYWu1rjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ : عاملان کشتار جمعی اکنون کنترل ساختار نظامی و امنیتی ایران را در دست دارند.
ایران به‌تازگی قدرت را به‌طور کامل در اختیار دو فرد تحت تعقیب اینترپل قرار داده است. محسن رضایی اکنون با اختیاراتی هم‌تراز با رئیس‌جمهور، ریاست شورای عالی امنیت ملی را بر عهده دارد و احمد وحیدی نیز با اختیاراتی در سطح رهبر جمهوری اسلامی، فرماندهی سپاه پاسداران را در دست گرفته است. هر دوی آن‌ها به دلیل نقش ادعایی در طراحی و سازماندهی بمب‌گذاری سال ۱۹۹۴ مرکز یهودیان آمیا در آرژانتین، تحت اعلان قرمز اینترپل قرار دارند
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20766" target="_blank">📅 15:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20765">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وای نت : ‎نتانیاهو قصد دارد انتخابات 27 اکتبر کنست اسرائیل را تحت تأثیر حمله جدید به ایران قرار دهد تا ائتلاف لیکود متلاشی نشود
گزارش ynet می‌گوید نتانیاهو در شرایطی قرار گرفته که
تهدید ایران و بقای سیاسی شخصی‌اش عملاً به هم گره خورده‌اند
؛ زیرا اگر بدون یک دستاورد بزرگ وارد انتخابات شود، فرسایش قدرت نظامی و نبود موفقیت سیاسی می‌تواند برای اردوگاه او هزینه انتخاباتی سنگینی داشته باشد
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20765" target="_blank">📅 12:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20764">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ecy1hqXO_X2a_4XmBNP6IA_uKMoetYPDANV7sdYyZijALDvqp-liaXeQ0LiHWk5r1D98_4wGOwQWE1TfFZNJWrg_JBm2rrS5EOWFlzldKQExoFiQk0EbZdmzrYkvzrxmSBIHd2sXl3OtzZjJHWRIfEd86Qb6VtRxnq2fz0XrRGYdP-er8av57diRJzAixCuXTJ3jBatSEcMjMbqucGehxeexc439AK5AkVwF9HTl4LTwMY1j7ob6J5DgmZxsqL8VqIZzspAybBjGEkfR3Bkf6NM7hdCNkgJaCgb41B_NsCkYVvvli1GR8dnCUTk4IPWIiOaGJh8-Yc2Wt4gOWHMY7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور محمود بوتاکس در جلسه دیروز مجمع تشخیص مصلحت نظام
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20764" target="_blank">📅 12:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20763">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مقام ارشد به کانال 14 اسرائیل: بزرگترین ترس دشمنان ما این است که نتانیاهو در قدرت باقی بماند.
خب،این به چه معناست؟
نتیجه بگیرید.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20763" target="_blank">📅 11:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20762">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مجید شاکری ،مشاور قالیباف :  ترامپ با ما توافق نخواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20762" target="_blank">📅 11:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20761">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">باراک راوید ، آکسیوس : یک مقام ارشد آمریکایی به من گفت که کاخ سفید از اظهارات نتانیاهو درباره طرح غزه «نگران یا ناراحت نیست» و آن را بخشی از فضای رقابت‌های انتخاباتی در اسرائیل می‌داند.
این مقام آمریکایی گفت: ما نیازهای سیاسی بیبی را درک می‌کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20761" target="_blank">📅 10:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20760">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbdnkiPypyzW1X7nmigqC-Spe7qLULSvK62UlbU5ljhYHokmAghE086lAuqqlTivK7Gk31SulN2sLyAD4iqD3nWK4vS10Zn1T7gEp7gzXh77lI5FiLg-Mo20720X826LOWtSj4VTO0oEpIprAmJRgOXr4vJIFdNEUKZ1r-Tjm5xb0WxeZqS6Hs0YOFX-Dzjy5Kq1wf7o_Inr1bm2_xJecB-s3LFv2hM6KW_NWFRshsa7uuXz1fNk6jiTE4zMUUToNDzZqiTa3MufVyxTJDXDZgRlIpBOKw21T01tsYLpYWZGbc7z1k-zvR2LfT2FfF_yoEiWfT-jcbgo0WSGfrkvTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیز نیست، بی بی داره خنثی سازی و بازکردن ورودی های تونل ها رو براشون انجام میده.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20760" target="_blank">📅 10:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20759">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza</strong></div>
<div class="tg-text">مهم نیست داش یاشار مهمات عمل نکرده دوران هخامنشیان هست</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20759" target="_blank">📅 09:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20758">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbdiM9ET-ozVfpvEoltD6osL6zNo7b7Tco6BoPDhEPSUDJmIZQ4zKMPrGjGTk_UeMqD-M1Yz9vfKTziqSQS1p-D-YLXW9ZMpb41bpgtS9Vt2r2Od0Veymel6DaZU9tDWAl4LPaqhOIdaznS0O0KEPNqvqVII0XJ3H4JlL57RRY--HhhMGtoHZBBlwVPLIce9_4KLHoNrFqtBHNN3C1gMt3glEZTzEHVKCXGnzBG3SSwfU5JKWfGHVSOmXh21OcMfYsgr4dHhOdvxhTdQzqXFzrb8IkcCW8Yrml72ebkIx0Qgg_gDPS8ma_z9-9n1_wm1k42HpXWHEdTjUikp_CNidg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصفهان سمت پادگان ۱۵ خرداد انفجار جدید
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20758" target="_blank">📅 09:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20757">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtR7PoNHNRby1sGsYrPGareZ3ZOKD_hc3TCHK1TgYpBwGg7CTV7CKSb8E1UYCdBz-FkgWw8aJ8-76CUhojA1CJIj-oWSH0cG5txmWWwor2F0x7qTrFB9yzJjBU0ifTPRQm53yOuhZvbGNhalutFcO1FFebKw5eLFiZ-LKkEvrglSr0241ync24ujGCiPOIOV9xyERP9UAP4p4t8bqRT0BlQQ_bVs57RPidnHbE-s46cKhSdbHki05cjlNtKe-B5XVanPKKuCMhhE5x9NjiQl_CszWPNCjx-h6xL1NLlRoeEfON90KGPToBuEqJhE4PQNh6xHjoCNSuZZ39fNkio6Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو انفجار شدید در اصفهان
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20757" target="_blank">📅 09:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20756">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0rGoUSc-VshvLifn6LO-ud2mTsUSIGMzY8T0OrQZbULoByjuAQPVwEN458VUWqu-LQHvlSQfHX9F5ro46I7on11XqkOXujtvns1hAvjeD0p0mKPA87e8CrbPaGNGDQw2NxpOPJ-N_VkD97KUV9be9tvJLzbzp4vvdl63UJbNV0MpgScSVbCxURzk_nClqL4qx9ADqeDNp8-tUOtxQl45DChpUXoZM8yfn6sMLdDUW8-EhN-sYDOA3G0_MdJDMsFgT2ZJ1N7emsAwsfZULpd201ry-6zUgHeZnUL-LgYtyMw74Xd0BKq0TXWtVLMDUeSe3uP795A42lUX6OuvMBcHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس‌نیوز : زیردریایی جدید «روز قیامت» اسرائیل که با هزینه ۶۳۴ میلیون دلار در آلمان ساخته شده، توان بازدارندگی این کشور در برابر ایران را به‌طور چشمگیری افزایش می‌دهد.
این زیردریایی از کلاس «دلفین» است و شرکت آلمانی «تیسن‌کروپ» آن را ساخته است. همچنین، این بزرگ‌ترین زیردریایی ساخته‌شده در آلمان از زمان پایان جنگ جهانی دوم به شمار می‌رود و به جدیدترین موشکها مجهز است
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20756" target="_blank">📅 09:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20755">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4468b68072.mp4?token=MojkgO7b7T385qjP8Mrn36Pe-qXJriV8N4B1sUuBV7JEYUOku5B7rh4b4NF5qgD32pcaVforNTYnO7FgZwIP0DAWZIghl8NBhW-vhrLCOJZbeNqyEi7Xa4HpMgrvImMcRWjjhJ2GwuWOopR9O6fP0XfxO9cMbLKeYkN1HBqreoZBJC5kA10bvUDvhfOKNWewgW6zAu1QMSFtSNq2heQT5JkTsj9y720onF2Mzv8QG_pCIYw3lzPdt8lUMbT6ApYoRI3Nuo4nU_zs5LsUBb_GGiWd3wAFqtyG7hY---45EXcMSTqk5G8Ur34VtMtrgUuhhrZ6Eq8iz--GJMY80-05QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4468b68072.mp4?token=MojkgO7b7T385qjP8Mrn36Pe-qXJriV8N4B1sUuBV7JEYUOku5B7rh4b4NF5qgD32pcaVforNTYnO7FgZwIP0DAWZIghl8NBhW-vhrLCOJZbeNqyEi7Xa4HpMgrvImMcRWjjhJ2GwuWOopR9O6fP0XfxO9cMbLKeYkN1HBqreoZBJC5kA10bvUDvhfOKNWewgW6zAu1QMSFtSNq2heQT5JkTsj9y720onF2Mzv8QG_pCIYw3lzPdt8lUMbT6ApYoRI3Nuo4nU_zs5LsUBb_GGiWd3wAFqtyG7hY---45EXcMSTqk5G8Ur34VtMtrgUuhhrZ6Eq8iz--GJMY80-05QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در واشنگتن دی سی، در پایگاه اندروز فرود آمد و مصاحبه ای‌ نکرد که به نظر من بازی با رسانه هاست تا در خبر های‌ زرد و دروغین خود غلت بزنند تا غافلگیر شوند
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20755" target="_blank">📅 02:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20754">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7NHFxp6akoZbGQuANY42FNQr2tjIzl4f76XjRWvBfopLPSsNrwhj13iFe9e3CUre4x6p9B7ycVTRdxgfOtCk5BdnU7wMh9YcUI-gYsNhmCVUg_x0XgAetrmTAyyU87MQ_85W2Oe8vwOa4VYLWr4aXKguuPHFJUVa9-bqBnCT_CQY3IWg-h8veYo2TBqlnvNmQIgiJANZjDJ-uUOC3YJ3XFkbVhCZbL8aTKB6stgJr834T7z-SxsuuroAsFZKYLheLgPBLkaE42bIa_c6CGInm4MGrLvOyxVw_hJIFqvF9uv8fnQjIVR3isXa2OROGXVJzix9TiwAktumlf9ZYUcvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : تا اینجای کار امشب در حالی که در سراسر خاورمیانه آرامش برقرار بود، در ساعات اخیر، حکومت ایران تعدادی موشک به سمت یک کشتی که در حال عبور از تنگه هرمز بود و توسط نیروهای ارتش آمریکا اسکورت می‌شد، شلیک کرد. سپس، آمریکا و عربستان سعودی تعدادی…</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20754" target="_blank">📅 01:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20753">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اتاق جنگ با یاشار : تا اینجای کار امشب در حالی که در سراسر خاورمیانه آرامش برقرار بود، در ساعات اخیر، حکومت ایران تعدادی موشک به سمت یک کشتی که در حال عبور از تنگه هرمز بود و توسط نیروهای ارتش آمریکا اسکورت می‌شد، شلیک کرد. سپس، آمریکا و عربستان سعودی تعدادی پهپاد به سمت جنوب ایران پرتاب کردند که پهپاد سعودی توسط سپاه رهگیری شد.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20753" target="_blank">📅 01:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20752">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8M-sgXArjAkJaHjibnBPDrzrP0GC9_vNg-mvwb-F7hAaYx7uTYnrBwJlaxzrjg3-XnXJI7PlYXo5llJnqe8BaZb-BDfUcbod2Cxrj_RMC8Ys1gBTvFhe0geC6tPcELBfb8ZA6AAosMvZJz7G_9dKPpbQG4lj29QgxXHxkgYfraQDp538x1q0Se3fuQ-c161QnrAyjAgOrW0jgC_CbLpCrYZa-qUSR9u94i7LaR9k8T_k93SAqGKPZeATQXxNL-87L7-u1N5icBpkqTNhlT_mrL5DjKP_Ra3ey_q56m1QPDgTdVNEEPzEXWhoGPIEugCPSd6mLpK5ABLmzqD_VQ1-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام :
ملوانان نیروی دریایی آمریکا
بر روی پل فرماندهی ناوشکن
USS Ross (DDG-71)
در حال نگهبانی هستند. «راس» یکی از بیش از
۲۰ ناو جنگی آمریکا
است که برای پشتیبانی از مأموریت‌های نظامی در خاورمیانه مستقر شده‌اند؛ از جمله اجرای سخت‌گیرانه
محاصره دریایی آمریکا علیه ایران
. ما، تا
۱۸ مرداد ۱۴۰۵
(برابر با
۹ اوت ۲۰۲۶
) نیروهای آمریکایی
۵۵ کشتی تجاری
را تغییر مسیر دادهایم،
۲ شناور
را از کار انداخته‌ و برای اطمینان از اجرای این محدودیت‌ها،
۲ کشتی دیگر
را نیز مورد بازرسی و سوار شدن نیروهای نظامی قرار داده‌ایم
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20752" target="_blank">📅 01:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20751">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بلومبرگ: توافق هرمز همچنان دور از دسترس است، با توجه به اینکه ایران از مذاکرات مستقیم با آمریکا امتناع می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20751" target="_blank">📅 01:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20750">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20750" target="_blank">📅 01:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20749">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">روزنامه کیهان : اردوغان و شهباز شریف مثل روباه مکار و گربه نره بن سلمان را سرکیسه کردند!
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20749" target="_blank">📅 01:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20748">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead9f1f71d.mp4?token=CxE7JXE6eZzbk2bWgXhtCXLrmiYA_QnisgnSg82fy_eYPdqaltcilZrfaeRQKxkyUL-qHhjYtWvPBcnDrbcBCEpn-TdIy2O0yp-qIjQfPib798TsewTwkAmpQTWNgtBF9uhOsZ5RFAsPQeF2feYdZkZoWZx2SHiHEFoYHP7janaFgZBc7xqxDG2I7GQQkhkcuAN8hBFZ43SfyUzfOyvJ3ZtFV_39KkB1TeQPUNCdr7gGYYanuUPAKJBhe116zCD3ND1zhZ0RwIwHDZXSe9ExoJaz0N-uAGPIf3yYL6vStXf0h0GcVLd6CzCeaZHpRVpiczoBnYrWFyXCnNQ0V4X8sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead9f1f71d.mp4?token=CxE7JXE6eZzbk2bWgXhtCXLrmiYA_QnisgnSg82fy_eYPdqaltcilZrfaeRQKxkyUL-qHhjYtWvPBcnDrbcBCEpn-TdIy2O0yp-qIjQfPib798TsewTwkAmpQTWNgtBF9uhOsZ5RFAsPQeF2feYdZkZoWZx2SHiHEFoYHP7janaFgZBc7xqxDG2I7GQQkhkcuAN8hBFZ43SfyUzfOyvJ3ZtFV_39KkB1TeQPUNCdr7gGYYanuUPAKJBhe116zCD3ND1zhZ0RwIwHDZXSe9ExoJaz0N-uAGPIf3yYL6vStXf0h0GcVLd6CzCeaZHpRVpiczoBnYrWFyXCnNQ0V4X8sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پهپاد ساخت چین که توسط نیروی هوایی سلطنتی عربستان هدایت می‌شد، در سیریک، استان هرمزگان، ایران سرنگون شد.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20748" target="_blank">📅 01:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20747">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بازهم صدای انفجار/پرتاب از سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20747" target="_blank">📅 00:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20746">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwPLpi35TFE9ss_x3PoKFDlmrgGn35TmDj-g8rjEAKAEJ_7AYexbV_PtNN_p9W4pz9onULV4dA4oUG2GLcvFSEKicHOx8H8lZJZIKVfJSsPk2toQMCeP2b1SJHZQ8qJLk7wZkIBHXfdn6eD3asLEvNOSEBG3xx_AidklgETYdE_c5xoHYshw3Dw71p9SjNmISZs8btSWXSkTJytiK7tPqSnQ5vrNriQwMhitdJ5Js72US9-E749JqMLOzhG2Qz2ppgBysV-eTzJSdYFfMtMtLVmnJGBTSDp71hUv4UAnL1tsLVxiEqzDfUfL7xdSAKB2Ecqy-rSzvzduXuofIU503A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث
: 51 سال رفتار نامناسب ایران!
@WarRoom
حالا چرا ۵۱ !؟ ۴ سال آخر شاهنشاهی هم قبول نداشته ؟!</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20746" target="_blank">📅 00:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20745">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766d8dae53.mp4?token=N2PduvbZBrm8lncLTvjGMQaSfQWPJt_99iUB9Zh1l3khaBscYzxkkHo_v6TFjFns_GoKh9vHLk2_T5PbR7ad3M-tislhsuWOtdnp3HdDPuEvSMZapGZs658_2TEhX5y987viMFeqx17IOj8tSb2ocVBNKZRvnnoqXZlNAyNVDux7alBT1u9iN-r5EBpr5yU3gOJe_jEY0lPFqskYSpecWtxTSLwD1-wj6tsYnvWCHaxhtAYibEsp1ypwQ6kR9S814NUsCsaDWnyka4t9DdOD3Qr7Gf9JOsKeS68yddd8hHMio6ZU7mgUUAUiS9LIjRi5pJAxmG6RO8bf5zFInRP63w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766d8dae53.mp4?token=N2PduvbZBrm8lncLTvjGMQaSfQWPJt_99iUB9Zh1l3khaBscYzxkkHo_v6TFjFns_GoKh9vHLk2_T5PbR7ad3M-tislhsuWOtdnp3HdDPuEvSMZapGZs658_2TEhX5y987viMFeqx17IOj8tSb2ocVBNKZRvnnoqXZlNAyNVDux7alBT1u9iN-r5EBpr5yU3gOJe_jEY0lPFqskYSpecWtxTSLwD1-wj6tsYnvWCHaxhtAYibEsp1ypwQ6kR9S814NUsCsaDWnyka4t9DdOD3Qr7Gf9JOsKeS68yddd8hHMio6ZU7mgUUAUiS9LIjRi5pJAxmG6RO8bf5zFInRP63w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش ۴ انفجار در تنگه
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20745" target="_blank">📅 00:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20744">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گزارش ۴ انفجار در تنگه
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20744" target="_blank">📅 00:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20743">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دوباره از سیریک موشک ول کردن سمت تنگه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20743" target="_blank">📅 00:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20742">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJuF8D-tK9iMFjiuNm4enrBQXSTBiiDO_zR0wTwDcptJpRweD8NBxqM6rKRwlEgUOApnVAc0w0Lg5u3SY5irG56l-_bexE6lOUAJloKMTXU4Xlt6rIIGfF5do7c4SZn3e1dQFJ-C0w9migEdn6Sc3TRIiuPWaKhNJLj0lmGzAEorGGdV1DeNB_EtQEr3o-0DcHnkZekL2dtoNVmCjDS00pZYdrboJ51eznvAKSKKwLElXPTR6WDoxMIzdvoEaPtEZPrIpO9vzKY1lB-2dUEMkLBWnrkDBTewC4OvWi8DT-z-Gc2-muoBiEN_W-X1ALINp-ZRTa4ZWLJjZhAyTeWPWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیریک :
یه نفتکش میخواست از مسیر جنوبی
عمان عبور کنه مورد حمله قرار گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20742" target="_blank">📅 00:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20741">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گزارش صدای انفجار  پرتاب  موشک/پهپاد از سیریک @WarRoom
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20741" target="_blank">📅 00:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20740">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd95915a0b.mp4?token=kQTbMc7OgJlSSeLrjviPd_L34OOhRqcajzkDgPPzHfGFDesE9NA9Nv06d0H4x63XzgYkOS_y-HqZiWnPxn0FplVDZIJ38wJBQu453hfxWBd3Yi8PTFEbLO4Ixm9e2DkQ-hMxhu3NudneE_oJoo0cN7TZsqLJpmfGeKU2lUWpRCrm-5Z4AImMV0qQjUotwX6CNGI_HcUtEIyPAva11St1Vxv0x7VS9vk7jDfSBXRFU8VyT9qcpLGQ0PqjKP4CV49py3F7XygwMsvyKMCxzTrko8sw7NCIel3xRGn2LdwWB3FM21dErcukQ9vVDWqHZqKoKA1piozfAGazK6zQ-FeC1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd95915a0b.mp4?token=kQTbMc7OgJlSSeLrjviPd_L34OOhRqcajzkDgPPzHfGFDesE9NA9Nv06d0H4x63XzgYkOS_y-HqZiWnPxn0FplVDZIJ38wJBQu453hfxWBd3Yi8PTFEbLO4Ixm9e2DkQ-hMxhu3NudneE_oJoo0cN7TZsqLJpmfGeKU2lUWpRCrm-5Z4AImMV0qQjUotwX6CNGI_HcUtEIyPAva11St1Vxv0x7VS9vk7jDfSBXRFU8VyT9qcpLGQ0PqjKP4CV49py3F7XygwMsvyKMCxzTrko8sw7NCIel3xRGn2LdwWB3FM21dErcukQ9vVDWqHZqKoKA1piozfAGazK6zQ-FeC1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
نیوجرسی را ترک کرد و جواب خبرنگاران رو هم نداد، تا ساعاتی دیگه میره دم توالت شروع میکنه
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20740" target="_blank">📅 00:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20739">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شبکه i24 NEWS: اسرائیل فاش کرد که رهبر حماس، "باسل صالیه" را از دو سال پیش بازداشت کرده است. این خبر پس از دستگیری او در شهر حمد منتشر شد. این گزارش حاکی است که او پیش از این با سنوار و الضیف اختلافاتی داشته است. اسرائیل او را مسئول شلیک موشک کورنیت به یک اتوبوس در سال ۲۰۱۱ می‌داند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20739" target="_blank">📅 00:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20738">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZqIXSRJ_mUWRSeHbL0GuHTCeR4XwvDaZr1ErGegWveEv8q57qPL63Z6w3Q5spwov15ubMJQmn2CdN_zz8Er3ntlExQ1KUMiSBCYkKYzg7zLbqQiAhcBQj_u2X4coL4brNug4djOcooJEfKas4ZZ9R_SjlAr8fNf3_50wcEvEKfgwz9YnabkZdm0djV_WxOziNgrg2LB9LjO83lhEwHUNP0rxatz2LDZqK2B6D9W0Y9myT06_CxETIoK-p59p9ADQLYTISvUJNLmJx0KpGTSj7AApRKxRpZuAcM0ksnFQPAhKW-jq5GArifb6EYBhJubXXLRvXgIdm0oOFRh9-kV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرکت پیشرفته‌ترین نسخه عملیاتی خانواده E3-Sentry (آواکس)  بوئینگ E-3G Block 40/45  از پایگاه رامشتاین آلمان به سمت منطقه خاورمیانه،
با مشخصات :
قوی‌ترین ارتقای انجام‌شده روی E-3.
رایانه‌ها و نرم‌افزارهای مأموریتی کاملاً نوسازی شده‌اند.
توان پردازش اهداف بسیار بیشتر از مدل‌های قدیمی.
لینک‌های داده و ارتباطات پیشرفته‌تر
و موارد بکلی سری بسیار زیاد انجام شده
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20738" target="_blank">📅 00:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20737">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گزارش صدای انفجار  پرتاب  موشک/پهپاد از سیریک
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20737" target="_blank">📅 00:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20736">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130cc3cf42.mp4?token=QuCejPfpTErdoCzsjfw8dp0Ndd-LMjDXkic82jqLadaS13OaluTQ-KGc-dgRYao3B_XegshIt8o-S1pnFkxPGZpepKSk3-E0apFcxswGwzAGK4Pi6eRzDvCGMS7NgT1-Jj9feztblmjMGM23aaGY0HDNYehHCQHkK8zhY47Qa6YALT_B3Vz5clfIZkPdYf4GzQBykiQPqIaElGC6f0L04jvZzGulKsFIXT9axuqTDk6BsfXX1Sg_XcCvGnD1KnE_gnF1S1FhmhCcLoUh5--rOkuLyCGqL8yuu4n8FD6aZ-ALZv6jRmAPCnLjkiHvVUUE4bKyAm6g4Hy7wnKpQgs2wyNIQuOhIRvul73BmDKAku-QV9LqQzL6KB2Hgakncd-kxVVe0DVHyaIme5zgrxGOCr7R3ShpEqgTm5lIcvNtnmK9HAs6VVJRBvZ_zukCXMzfrAmthw0WBV0lLb911Lgb_K8rC--vRPDhzI51Cohb4qeqyc4XLc5GfEPmULmmFjC6jGblLog2Gl4D1dvyuc4wSep__3zdi5HzHKYJgBFQDzttoaPuHFpD_prS6dU25dfLuHP5QotQSpkQpfwQIDHsmsyCWU1G9NfbK8HA952sjM8Brub4Mw6r5hrqQ1IpokRRtzp2McfaHEwkN6iCMVbXQpV_I8VrCBP73e3AeqEy4EI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130cc3cf42.mp4?token=QuCejPfpTErdoCzsjfw8dp0Ndd-LMjDXkic82jqLadaS13OaluTQ-KGc-dgRYao3B_XegshIt8o-S1pnFkxPGZpepKSk3-E0apFcxswGwzAGK4Pi6eRzDvCGMS7NgT1-Jj9feztblmjMGM23aaGY0HDNYehHCQHkK8zhY47Qa6YALT_B3Vz5clfIZkPdYf4GzQBykiQPqIaElGC6f0L04jvZzGulKsFIXT9axuqTDk6BsfXX1Sg_XcCvGnD1KnE_gnF1S1FhmhCcLoUh5--rOkuLyCGqL8yuu4n8FD6aZ-ALZv6jRmAPCnLjkiHvVUUE4bKyAm6g4Hy7wnKpQgs2wyNIQuOhIRvul73BmDKAku-QV9LqQzL6KB2Hgakncd-kxVVe0DVHyaIme5zgrxGOCr7R3ShpEqgTm5lIcvNtnmK9HAs6VVJRBvZ_zukCXMzfrAmthw0WBV0lLb911Lgb_K8rC--vRPDhzI51Cohb4qeqyc4XLc5GfEPmULmmFjC6jGblLog2Gl4D1dvyuc4wSep__3zdi5HzHKYJgBFQDzttoaPuHFpD_prS6dU25dfLuHP5QotQSpkQpfwQIDHsmsyCWU1G9NfbK8HA952sjM8Brub4Mw6r5hrqQ1IpokRRtzp2McfaHEwkN6iCMVbXQpV_I8VrCBP73e3AeqEy4EI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی دفاع هوافضای آمریکای شمالی (NORAD) اعلام کرد که جنگنده‌های اف-۱۶ این فرماندهی، چند هواپیما را در نزدیکی باشگاه گلف ترامپ در بدمینسترِ ایالت نیوجرسی رهگیری کردند؛ زیرا این هواپیماها بنا بر گزارش‌ها، محدودیت موقت پرواز اعمال‌شده بر فراز آن منطقه را نقض کرده بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20736" target="_blank">📅 23:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20735">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کانال ۱۳ : اسرائیل به فرمانده سنتکام اطلاع داده است که در صورت توسعه برنامه‌های هسته‌ای و موشک‌های بالستیک ایران، به ایران حمله خواهد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20735" target="_blank">📅 23:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20734">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">به گزارش اکسیوس، توافقی برای کنترل عبور و مرور از تنگه هرمز بین ایران، عمان و ایالات متحده مورد مذاکره قرار گرفته، اما چندین روز است که در حالت تعلیق مانده است.
مقامات آمریکایی می‌گویند اختلافات فزاینده‌ای در درون رهبری ایران وجود دارد. گفته می‌شود یک ساید به رهبری رئیس جمهور مسعود پزشکیان، به طور فزاینده‌ای نگران فروپاشی اقتصادی احتمالی است و معتقد است که تهران به توافقی با واشنگتن نیاز دارد. ساید دیگر به رهبری فرمانده سپاه احمد وحیدی، با امتیاز دادن به ایالات متحده مخالف است.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20734" target="_blank">📅 21:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20733">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دونالد ترامپ، به آکسیوس گفت که ایالات متحده در قبال ایران «فعلاً با سر و صدای کمی پیش می‌رود»؛ اظهارنظری که نشان می‌دهد واشنگتن اجازه می‌دهد فشار اقتصادی افزایش پیدا کند.
ترامپ گفت: «ما فقط به‌صورت نیم‌بند با آنها مذاکره می‌کنیم. ما فقط داریم ایران را زیر نظر می‌گیریم؛ با این تورم شدید و این واقعیت که پولی ندارد.» او با اشاره به وضعیت اقتصادی ایران مدعی شد که این کشور «در شرایط بسیار بدی» قرار دارد و در پرداخت حقوق نیروهایش با مشکل روبه‌رو است؛ آن هم در شرایطی که محاصره دریایی آمریکا فشارها بر ایران را افزایش داده است.
ترامپ درباره رویارویی با تهران گفت: «همه‌چیز درست خواهد شد. همیشه درست می‌شود. این مثل یک بازی شطرنج است.»
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20733" target="_blank">📅 20:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20732">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اکسیوس: میانجی‌های قطری و پاکستانی اطمینان داشتند که این توافق روز
چهارشنبه
اعلام خواهد شد، اما از آن زمان، چشم‌انداز دستیابی به توافق کمرنگ‌تر به نظر می‌رسد
یک مقام آمریکایی مدعی شد که حدود ۸ میلیون بشکه نفت هر شب از خلیج فارس از مسیر کریدور جنوبی تنگه هرمز و با هماهنگی ارتش آمریکا خارج می‌شود. آمریکا قصد دارد تا زمانی که توافقی حاصل نشده، تلاش کند نفت بیشتری از منطقه خارج شود.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20732" target="_blank">📅 20:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20731">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDku_LD6cotLGzltA1s0ULXBoTKHaTi20Y6eMdSS9GasqKnAjqNb7b3NyGAAsRTKtoXlmAofE_Xk4UcpHRlqbJWLO1m6OT1qGHvuylfX0auZpzwF51PbCsQ2wJMuJi-G5Be-Six5mPi0f-EAzHnZCIM7VOlAKv8C7Jlw6S7y__LX7Zel7fqvvkhukojGEbpXBFe-rgu7ykabJ-8io3tz1lxe3MsHMvxp-hHHxH17EjPi5zH585pdq1K6DQZhlP3DE-p4Fk0LwS_nmoYOwKlMW-l8PKv6MPt79u89Ps5eN5amdN0w75i_oURs3olM4CGenJOXk49oxyIbhlu7vhJmLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : جت‌های جنگنده رادارگریز F-35A نیروی هوایی ایالات متحده در آسمان خاورمیانه گشت‌زنی می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20731" target="_blank">📅 19:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20730">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حسن قشقاوی، سخنگوی کمسیون امنیت ملی مجلس، اعلام کرد کلیات طرح «اقدام راهبردی تامین امنیت و پیشرفت تنگه هرمز»، با اجماع همه اعضای کمیسیون حاضر در جلسه به تصویب رسیده است.
- کنترل بسیار بیشتری بر تردد کشتی‌ها در تنگه هرمز اعمال کند.
- برای برخی کشورها یا محموله‌ها محدودیت یا ممنوعیت ایجاد کند.
- برای عبور کشتی‌ها نظام مجوز و در برخی موارد تعرفه یا عوارض در نظر بگیرد.
- از تنگه هرمز به‌عنوان یک ابزار فشار سیاسی و امنیتی استفاده کند.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20730" target="_blank">📅 18:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20729">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رئیس مجمع تشخیص مصلحت نظام:
به هیچ قیمتی از موضع خود درباره تنگه هرمز عقب نشینی نخواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20729" target="_blank">📅 18:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20728">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c89aa1291c.mp4?token=tg9haB45_RsRth6jxR9mFLJJDYNnAdVOAkFDDvatncivY3qY0QVMhBpqixn2RzNiz_-7a4axs-rGZdOuVp2jTkEDh1hMnq4VRYnoujVU4s7_cvUzNL_6_N0lytW-o3rLblRBkmsJY_M0bGX583jyeL26L2XLweU-tdM1zv-FzVIVYIM4XIodTSRaN8r9sN7jCANQh2dd-RMrb9lOahXqJMEY-NXwfQ9Nx8YlXV1hQICLGhU0rr8nYawPo2RUBk30IHyiKhMGu8C5C1Mcy7hZEXrg9cC9NQoTCT5PmJfFsUh8JwP8D59e95DwLMNAMcOpbyYmrrnCTG_QShMmeDGam73yQvTBOPHpbY9zCzgdmKHtjrbiyZQ9aucDQPZuv6jdKBuE3OCnTPs6LJRJz01SyeToKKid3D2d4SVFjamkUxt6xCVU6uKEJAGzfE0uC0lgfN4ebpbauqJPyyuIaz4IC0WuoEawU6PbpK3IHqDP69LDyJ7ybG3qzFbcIRyNmvdFA9eLY7rvmuqR069SXDDy-q8CaCCkzasKoNYYcoi75TCJC8rmU8pTD6fypYvYPct0qPg6riYrgCHKryM19Zxs9y65xI3ZwKegbIFL8gwKVVrp2LMv9ydWNrC4A0_PCu2JYBz_svJoINsRR2zYF-c6i96ACv2iOMYyQ7coiL7bj9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c89aa1291c.mp4?token=tg9haB45_RsRth6jxR9mFLJJDYNnAdVOAkFDDvatncivY3qY0QVMhBpqixn2RzNiz_-7a4axs-rGZdOuVp2jTkEDh1hMnq4VRYnoujVU4s7_cvUzNL_6_N0lytW-o3rLblRBkmsJY_M0bGX583jyeL26L2XLweU-tdM1zv-FzVIVYIM4XIodTSRaN8r9sN7jCANQh2dd-RMrb9lOahXqJMEY-NXwfQ9Nx8YlXV1hQICLGhU0rr8nYawPo2RUBk30IHyiKhMGu8C5C1Mcy7hZEXrg9cC9NQoTCT5PmJfFsUh8JwP8D59e95DwLMNAMcOpbyYmrrnCTG_QShMmeDGam73yQvTBOPHpbY9zCzgdmKHtjrbiyZQ9aucDQPZuv6jdKBuE3OCnTPs6LJRJz01SyeToKKid3D2d4SVFjamkUxt6xCVU6uKEJAGzfE0uC0lgfN4ebpbauqJPyyuIaz4IC0WuoEawU6PbpK3IHqDP69LDyJ7ybG3qzFbcIRyNmvdFA9eLY7rvmuqR069SXDDy-q8CaCCkzasKoNYYcoi75TCJC8rmU8pTD6fypYvYPct0qPg6riYrgCHKryM19Zxs9y65xI3ZwKegbIFL8gwKVVrp2LMv9ydWNrC4A0_PCu2JYBz_svJoINsRR2zYF-c6i96ACv2iOMYyQ7coiL7bj9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش فاکس نیوز آپدیت آخرین تحولات تا دقایقی پیش…
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20728" target="_blank">📅 17:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20727">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYmB_uvNiA2vWS59zwuKG_vhvNiYhWfIDFMK9ISPYnXivYBnJYnBV8NvPhg4lLZosq8JzMrOw4ilIFBW2k7KYgpjiIujPj2jfjxXg2Bj7iPj7VX91PmARiUEsmZ2epZqpUYdpH20Rr7BvCV9xkEnOu5wCB6ipTht_OSIRtUIRPPsnmUDU4JMqEtZHkkRJ_c2PTqUbnPMaMG3I5sMZy15f8wA1EWdO35YU5wvkNIQ3Td-dQhxmi8rzS_C7CAY5yNXzEGQflpVC6OuNPoSHm1C49Lhq573SmgYG8-3KLWjYmf8P5yMzGr8O8wE6aw7p8uA0hEf0hTz8ciuuseIKwtrgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود و صدای انفجار در اصفهان
چیزی نیست بی بی داره خنثی میکنه
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20727" target="_blank">📅 17:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20726">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77914048f8.mp4?token=NmNkkCt5dnZqqnmZxx1imaBLQUpqZ7K_1cbJLmj-XNqTrlm2JtVdTK_9K6wWj2VvKEFaPGvwJttju4qWduJTpsDcyQHd9acLvEpi4aMuGBFP_A2YDB4EFs2P9JEy09tI6NsIuN4H_E-MNsXUWTzTqzKWciKbJOM8V49h-h2Enq3jkL6FxBj-OMl-4xOCSV691Te_X60A2lhzQeQOR1mNti3AFCeBWLBHNjXF78F9rT5LwV462VZzP7KDcEGmrzS0B2nK8lJgaQLpqPCvMTZ8fMO0BqHnbt36vdtASgtEXJOu1y39bjC8PR4DwNu4UJ6U0itCUaMQdNz0JYACCA_rmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77914048f8.mp4?token=NmNkkCt5dnZqqnmZxx1imaBLQUpqZ7K_1cbJLmj-XNqTrlm2JtVdTK_9K6wWj2VvKEFaPGvwJttju4qWduJTpsDcyQHd9acLvEpi4aMuGBFP_A2YDB4EFs2P9JEy09tI6NsIuN4H_E-MNsXUWTzTqzKWciKbJOM8V49h-h2Enq3jkL6FxBj-OMl-4xOCSV691Te_X60A2lhzQeQOR1mNti3AFCeBWLBHNjXF78F9rT5LwV462VZzP7KDcEGmrzS0B2nK8lJgaQLpqPCvMTZ8fMO0BqHnbt36vdtASgtEXJOu1y39bjC8PR4DwNu4UJ6U0itCUaMQdNz0JYACCA_rmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفتر شاهزاده رضا پهلوی با جمع‌آوری ویدیوهای تیک تاک از آهنگی در وصف پهلوی یک دابسمش منتشر کرد
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20726" target="_blank">📅 17:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20725">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oD0q0F03H1R7UCIkIw-5xEpSajzm9laCgT3FhY3jrrr-_J_XOEqZV9IHWS09X5FsGrs9MyJK_2dMcV_nbGvWOeUF5laOZAzRDo4u84DHl2v5DBIFU6xU_B1o1mNOAysLEBrzKf-hm6d8f_YpFnJNXjcmF3KFY99XiO4GnEef_k7X1fbESc3RpON0skDpx2i_EjUYCfv_RFxNtrWb3OFQDlqboLI666nvpXdNLuOG_8ZYvq2TT6i-0YNJrg528GFchJn9FUdATzKKEvI6JjQ_bN9pysDTfpShE8JqJi7tywiXupj3HMlP-atI4DWh7TrmTat-5ZRPTO1xlzvZ87-3yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارک لوین با خطاب قرار دادن عراقچی به دولت آمریکا : این بیشرف می‌گوید هیچ مذاکره‌ای در کار نیست
یاشار: منظورش اینه بفرما این عراقچی بیشرف هم میگه مذاکره ای در کار نیست کار رو تمام کنید
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20725" target="_blank">📅 17:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20724">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یکی از معاونان نیروی شبه‌نظامی بسیج ایران ادعا کرد که تصاویری که مجتبی خامنه‌ای، رهبر ایران، را در میان مردم و در خیابان‌ها نشان می‌دهد، در آینده منتشر خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20724" target="_blank">📅 16:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20723">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyH-MOZnh7wJnH_n2P-HybMGyBG77JYVmQ1HzwRRKF6VJp4OKM7boWVOZoJ9SGg4BvaTob7TAxAg74OMtkPV5R4VpC6QW0lyL7gyNYvyQvQAcXQHjfTW2GmRzlWb2Bf855g7uP4heIv8cgc8bejErr0ebY7mTbtjsTEXw6WjPzR4ggM4d7ebnsfn47attyWF6rW_wPiM-QL5PBwtcoSoqJSqJvgF1uPioV_H8yLADKRW9Bd_584-ZBq_WpNfz-ymXRfV7v55AYjYQ1ylYZ0FpgXO7dDrPxnz5arHIlw-TMERkpqHBOl4s87cXn_yz5CPJwuUhvCC1dRfOllaRYYw2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه هر روز پیجو میززن و برمیگردونم
پیج اصلی :
instagram.com/yashar
پیج دوم : ‏
instagram.com/yasharmotors</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20723" target="_blank">📅 16:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20722">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067ef90d71.mp4?token=ATrqLRvqKEW-IIE_D9EGoB-HuzIBC-PqRtW9MnkyJve1bVSkXvcxvyvrtwAPD4jwVi_IeuMZu7ahZ3kmetpnvEdhKxn-Z_YLMuXHIk4KrIVeflVJnrzRH9QDB7_38ESKM7g35sCQQB8PkSbBXL8C8tmAr3GxGs1SFCH9SVOIUkUSosyHGcDUFfHLaNNehTn_3vKuvd7OW9F54j-VGCmFFHq-nDcKkpckD0d2jG1c8eEOM9LXBQozetR7l2d4FEnPkv7X5xfToaz-Rc-bWmzhTe51-TJ0bSAiy_wH6i2x1yDmbOgEmuUn5LuYn53gVh6TfVKEjuv6fleC2Ej0Q6vm9mrTy4gA3CF-J094dxgtTxtSq37yjoqAtbTeC6MO46RfBtJR1lBOoYEu-GuQDjYn3B19Qx2Tda_F-RXTfGNdWcfKoejT8F5J-bJnr2KNIPAN6O5jEhuQHXFMG_qpedOaBzBiajcb37ZpVEYAuatoNJmfYkOo9M2OjR-E7TfgzSMim1Y3_V7NclB1Ie4UgYdILRkrUmTcG2mD8PFzA0RHRRXDEIIdVUTkol3KjzqHNKLE25vFOxkidtBfTytq6re9cYWX2Jj-i1qBVngflBpS1cleCNiZY6ZulG-TlPTcbCly_o_5jpM6b4BXaLJx2M4ltbxTuEfuUWbCa-YWV4P0w4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067ef90d71.mp4?token=ATrqLRvqKEW-IIE_D9EGoB-HuzIBC-PqRtW9MnkyJve1bVSkXvcxvyvrtwAPD4jwVi_IeuMZu7ahZ3kmetpnvEdhKxn-Z_YLMuXHIk4KrIVeflVJnrzRH9QDB7_38ESKM7g35sCQQB8PkSbBXL8C8tmAr3GxGs1SFCH9SVOIUkUSosyHGcDUFfHLaNNehTn_3vKuvd7OW9F54j-VGCmFFHq-nDcKkpckD0d2jG1c8eEOM9LXBQozetR7l2d4FEnPkv7X5xfToaz-Rc-bWmzhTe51-TJ0bSAiy_wH6i2x1yDmbOgEmuUn5LuYn53gVh6TfVKEjuv6fleC2Ej0Q6vm9mrTy4gA3CF-J094dxgtTxtSq37yjoqAtbTeC6MO46RfBtJR1lBOoYEu-GuQDjYn3B19Qx2Tda_F-RXTfGNdWcfKoejT8F5J-bJnr2KNIPAN6O5jEhuQHXFMG_qpedOaBzBiajcb37ZpVEYAuatoNJmfYkOo9M2OjR-E7TfgzSMim1Y3_V7NclB1Ie4UgYdILRkrUmTcG2mD8PFzA0RHRRXDEIIdVUTkol3KjzqHNKLE25vFOxkidtBfTytq6re9cYWX2Jj-i1qBVngflBpS1cleCNiZY6ZulG-TlPTcbCly_o_5jpM6b4BXaLJx2M4ltbxTuEfuUWbCa-YWV4P0w4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : ناتو وارد میشود
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20722" target="_blank">📅 15:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20721">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نتانیاهو : ما می‌دانیم چگونه در موضع خود باقی بمانیم، حتی در برابر بهترین دوستانمان، زمانی که این کار ضروری باشد
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20721" target="_blank">📅 14:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20720">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏مسعود پزشکیان: «دشمن افرادی را ترور می‌کند که گره‌گشا و حلال مسئله هستند.»
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20720" target="_blank">📅 14:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20719">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نتانیاهو: تا زمانی که من نخست وزیر هستم، هیچ کشور فلسطینی، نه در غزه و نه در کرانه باختری، وجود نخواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20719" target="_blank">📅 14:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20718">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نتانیاهو : در روزهای اخیر در لبنان عملیات هدفمند انجام دادیم، از جمله در منطقه تپه علی الطاهر، اما وارد جزئیات نخواهم شد.
ایران به اسرائیل حمله نمی‌کند، زیرا می‌داند اگر چنین کاری انجام دهد، ضربه سنگینی به آن وارد خواهیم کرد.
من طرح ۱۵ بندی «شورای صلح» درباره غزه را رد می‌کنم و از غزه عقب‌نشینی نخواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20718" target="_blank">📅 14:38 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20717">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یکی از رسانه های رژیم نزدیک به جبهه پایداری، با انتشار پیامی از هوادارانش خواست برای سلامتی مجتبی خامنه‌ای دعا کنند و «قربانی گوسفند» انجام دهند. در این پیام ادعا شده که «گروهی از علما» از در خطر بودن جان او خبر داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20717" target="_blank">📅 14:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20716">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، در گفت‌وگو با کانال «12 نیوز» پیش‌بینی کرد تنگه هرمز طی 2 سال آینده اهمیت خود را از دست بدهد.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20716" target="_blank">📅 14:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20715">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ادعای تسنیم : محسن رضایی کج بند ،نماینده مجتبی خامنه ای در شورای امنیت ملی شده‌ @WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20715" target="_blank">📅 14:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20714">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ادعای تسنیم : محسن رضایی کج بند ،نماینده مجتبی خامنه ای در شورای امنیت ملی شده‌
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20714" target="_blank">📅 14:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20713">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ادعای فارس : پزشکیان با مجتبی خامنه ای دربارهٔ مسائل اقتصادی و نظامی کشور دیدار و گفت‌وگو کرد
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20713" target="_blank">📅 14:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20712">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تسنیم با انتشار این کلیپ که قدیمی‌هست نوشت: پخش تصاویری از رهبر برای اولین بار @WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20712" target="_blank">📅 13:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20711">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP3XTq4mlQb3MV9Iagt78yH2TNpTj8UcTFAN3TOorSjbvM5ZRJDvGWtJQ2pOQDOatRF8YnP8lS80rFg6mgpO1LtwJJlBWx2wrVKUJP31M_g6Sh-esEjBGyfldXng2EVWY0srcM7JNaTCShP9mcZlqVesPFa3ALm51Fot1BPkT32O9FJjLH_jSVGsFPWWIdTUvt-91HudBYI3Rm6k3oBPBvOcsLXpUlMZTGNRIUf9g6xOMC1FkYALyU53lsrNhkkRnNdoyPTQV3BsBMx5JCcKpasf8cEeLbKqGxSO-Hns91SUsPkTObE-QdCnQwCtn04hQgE19MmPQap4HBpXrCua0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : دو آمریکای بسیار متفاوت.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20711" target="_blank">📅 13:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20710">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from╚»میلادم«╝</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIO0bfaSfjniMvEKe2kapmWzQ2divChWfJL_t-2NkVIruqagjK91WpWPbZSkX4s8Dt9GtY_ipQmIHrKJGdScrGx9hMxX8eEheHL-D5IBAta9Hm4gWPbYfqJQAx3YtcBaiQurrJV5YPQbDZa0INjQd2zpK-Rd0y3oiDjgPpIiiEgSTDkqKyNeicVOvseBswubfbl9Ziu8GaOvmRhukm_XVArRxHakgtC-e9HmmgBdP--6H2rg8aknfDepWBmWuUnxFXIbAX59q-JxuRZpFJJ-tcQ9ALYQ9VqpnSRODlKvjyOPcDIbD5Qa7mNHxEVx89nabuh8juHiFyivG4Mw3ELppw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20710" target="_blank">📅 12:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20709">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">عراقچی : در حال حاضر هیچ مذاکره‌ای با آمریکا نداریم
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20709" target="_blank">📅 12:28 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20708">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دبیر شورای امنیت ملی ایران می‌گوید که ایالات متحده باید دارایی‌های مسدود شده ایران را بدون قید و شرط آزاد کند، تحریم‌ها را لغو کند و غرامت دو جنگ اخیری را که علیه ما به راه انداخته است، بپردازد. @WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20708" target="_blank">📅 12:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20707">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏وای‌نت : دولت اسرائیل امروز اختصاص یک میلیارد شکل(حدود ۳۴۰ میلیون دلار) به وزارت دفاع برای خریدهای فوری تسلیحات را تصویب خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20707" target="_blank">📅 12:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20706">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سپاه : استراتژی ما حفظ تنگه هرمز است تا زمانی که دشمن تمام شرایط ما را بپذیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20706" target="_blank">📅 12:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20705">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حملات توپخانه‌ای اسرائیل به جنوب لبنان
رسانه‌های لبنانی از گلوله‌باران منطقه واقع بین دو شهرک «میفدون» و «زوطر شرقیه» در جنوب این کشور توسط توپخانه‌های اسرائیلی خبر دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20705" target="_blank">📅 10:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20704">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e5786aba1.mp4?token=Okwcw6K5BqzMPt-OHVlrkaXPhJZNFBZWP82UukzYWWIKc4xZGvhwju4YDfbuJx0TS23OY_VP54AfG9lBqoc81ZHYHdi-HHs5fVr44PCjDBOpVNsL8a4vg03orEi4PFSDDtsJcTw8MYEXVMr0HD3OJdk62cR7JIQ-Qdm6NLxV9Eye-l0btpOXg3LthVVL6zb_XttAollHlJXLapOt-u6OLbBd1FyRNIYk2efTsrD_YWF1lM2Z-E1DPVnydXCuQhGAXNgpo8K853nRmS17RykJJC5oO6-LMXh6LcWx_fSLd3_LjwnCAMW_xJk5q3OA5c0oKj1oGfY3t5bPtVpsmWs2zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e5786aba1.mp4?token=Okwcw6K5BqzMPt-OHVlrkaXPhJZNFBZWP82UukzYWWIKc4xZGvhwju4YDfbuJx0TS23OY_VP54AfG9lBqoc81ZHYHdi-HHs5fVr44PCjDBOpVNsL8a4vg03orEi4PFSDDtsJcTw8MYEXVMr0HD3OJdk62cR7JIQ-Qdm6NLxV9Eye-l0btpOXg3LthVVL6zb_XttAollHlJXLapOt-u6OLbBd1FyRNIYk2efTsrD_YWF1lM2Z-E1DPVnydXCuQhGAXNgpo8K853nRmS17RykJJC5oO6-LMXh6LcWx_fSLd3_LjwnCAMW_xJk5q3OA5c0oKj1oGfY3t5bPtVpsmWs2zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی آتش‌سوزی یک واحد صنعتی در شهرک نصیرآباد، ۶ نفر مصدوم شدند که یک نفر جان باخت و ۴ نفر به بیمارستان منتقل شدند
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20704" target="_blank">📅 10:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20703">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‏حوثی‌ها اعلام کردند پالایشگاه آرامکو عربستان سعودی در جازان را هدف قرار داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20703" target="_blank">📅 10:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20702">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtfzBPr2GaOP4hjWri6XdzhJNHwG08Q_4BxMK5Xdoay0lDo2dco60r9028Ob-rCUB3tJmaV_3OxfINkpXTe2Mo3x2TF4NygZQ6ZytvM6ISrByeb-RJt5mKW0WKzIupGxAZEfdeGRFVnuTX5owI0s83F7fXHAGRlUslfXN9F-4xW3AH0EXhwH4iq7QieM08x9nilSJ725Q5feWW2qbpCIF-P2h5F1OxL_w-AqNe1LRR-kiFcSExB7f41TQj5-vK6GriSLNVjN4DxjjjgTZk0xyuBVCapwhycVuJSXAbHNsuz5vvgGxvCMM8SCFUc9VfMfXERp2HiYMKz6Cw8a4xgKkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورشلیم پست : ایرانیان آزاده و اسرائیلی‌ها باید در کنار هم بایستند و اطمینان حاصل کنند که سنگ بنای صلح فردا هرگز قربانی تیترهای جنجالی نشود.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20702" target="_blank">📅 10:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20701">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کانال ۱۳: ارتش اسرائیل به فرمانده سنتکام اطلاع داده است که اسرائیل برای جنگ علیه ایران نیازی به تأیید یا حمایت ایالات متحده ندارد و اعلام کرد ما در حال حاضر در حال آماده‌سازی برای شروع جنگ هستیم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20701" target="_blank">📅 02:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20700">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اتاق جنگ با یاشار :
برخی کانال‌های تلگرامی عبری مدعی شده‌اند که یک ناو هواپیمابر جدید آمریکا در راه خاورمیانه است.
بر اساس ارزیابی‌هایم، محتمل‌ترین گزینه
USS Theodore Roosevelt (CVN-71)
است؛ ناوی که به‌تازگی مأموریت
RIMPAC 2026
(بزرگ‌ترین رزمایش دریایی چندملیتی جهان به میزبانی آمریکا در اقیانوس آرام) را به پایان رسانده و به
سن‌دیگو
بازگشته تا وارد چرخه آماده‌سازی برای استقرار بعدی شود. برخی گزارش‌ها حاکی از آن است که این ناو احتمالاً در
ماه سپتامبر
جایگزین
USS Abraham Lincoln (CVN-72)
در منطقه خاورمیانه خواهد شد، اما
تاکنون هیچ دستور رسمی و علنی از سوی وزارت دفاع آمریکا یا نیروی دریایی این کشور برای اعزام Theodore Roosevelt به خاورمیانه منتشر نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/20700" target="_blank">📅 01:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20699">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">😁</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20699" target="_blank">📅 00:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20698">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCiOSqKNtqwuS_maptfw06KRKbpGBGznk4U8lE-t6W1ujW7jbnRmGEu1rc1ZIpwUyVjK5_iqXK0WUnsalmCNLRsfZ0FqkzLl0oyKU3f-m5kZ7FhEtQjZED2B3qgLIzLKYk8s1CMrAkXIySyYbXH1XP_meK44dWqRU5i6huOSoNuiRpAYl0qPfUQcQNLOwqR1DCJwQeSseohOrMPLN2Xtmdy2nt9HLm_8FI1FGjZnKcyl8hHF65_nKEsis25xIEPRF3uRxYbh7Yu407comIzJPDLUA5idWSeLXCUkbc8VVf0ZV5fxESyR-y8Nw640lHZ7NAzH0pcq5N_cKiCgALETcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین باز دید پیج اینستاگرام از شهر های داخل ایران
😁
تبریز
🥇
🏆
اصفهان
🥈
تهران
🥉
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20698" target="_blank">📅 00:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20697">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2Trtad6f3r8vV_2pg1Wg_bP3GusLzwyTGvTWv_XefY-nEOjGh_4ilW9ApNv08QS1amZQpHCrV4bcH2znJBKF5JXO5XKft_A7wojgMHTgYTNaXDU9EBL3i4vTc9TjPf61XwFmhEIwpbJQHZNW3QaIKhDoFVJYPauoyJPuGX6HTB91PBDqkbjmSC4Qn9v86241wN-Ano8PVLlbUIECYb0hrWgSVZibcoTZym94SgcXsT01xLEArosp051KxCM7gCy1ya7lbF8_kgZfcgJS0w3bzObSnbFleXvrN9Z-CYIi6RbEvVJI348F0RoQdDZvr8J-_X5YEWwkF_dW2tnmxSMWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک پست: تأسیسات هسته ای کوه «کلنگ
گزلا» در تیررس ترامپ قرار داره
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20697" target="_blank">📅 23:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20696">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoF0W8NEqNbBfV025U9dI_wMBv3JfVGf4U_J80zHUlIaMVUtkBElyWXcuPYG0j4nuyNcYYQWadBkCE3aSDN3vaf3WAPwUynMUjY52I9y91ESuCJJ4xXPSdTP6H8Pt6g9283bDmK8QZl2sJ5q1lgrpMiXBYcSmHUy56DvygCHDq4L-B9uGDPCun4tATH5MTjhT2RjSH58z2ax3o9koC9-gMm_YEWpQUgSr-J8VGzBhpV1b4-fJGaioTdrFAc_Q0aIwYGAS4hKG5VR0Qvn_SqCsgGWSaxlOjx5dizVXUNKal2DJYfpeIUurBWPaSCICyXqh5QxuvTxsd0iZilgSm5sFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : ملوانان آمریکایی در حال تعمیر و نگهداری هواپیماهای F/A-18E Super Hornet در عرشه پرواز ناو هواپیمابر USS Abraham Lincoln (CVN 72) هستند تا اطمینان حاصل کنند که تجهیزات گروه ضربت ناو هواپیمابر برای اجرای محاصره ایالات متحده علیه ایران آماده ماموریت هستند. تا 8 آگوست، سنتکام 53 کشتی تجاری را تغییر مسیر داد، 2 کشتی را از کار انداخت و 2 کشتی دیگر را نیز توقیف کرد.
ارتش ایالات متحده همچنین به بیش از 30 کشتی اجازه عبور از محاصره برای کمک‌های بشردوستانه را داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20696" target="_blank">📅 23:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20695">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHbMNXecWJJDYP7fRCWURVZDKgTIGVUrNY-hQvQRikgbONEOXl4zfgqELBDVjBgqaaqEwTxJnMxXro3KADB6oq28h7zdy-WZhQpm27P52Yg4tlZbBtIbfdCAOcFARpCw_Wl9S1yfGuPLuiD2lZpK1vwbcm2FuEwruvkKLnA86muiGe9NaPedsIjoryk6g6-J42lmZ2sv0WTi1Q4cTsyMbBOYDfy2Bh98hTS9tHWP3YLXCJWunXEGyn27DngbJrP7KVXrfxXt72mjhd554KObbu27pRInDeQFKGgiahepX8E2cmAbieLRMl6QA43UpqdX5QpzFTwSWf1rmyU4HculxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده سنتکام وارد تل‌آویو شد  برد کوپر با رئیس ستاد مشترک ارتش اسرائیل و دیگر مقامات ارشد ارتش دیدار خواهد کرد. @WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20695" target="_blank">📅 22:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20694">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تمام مرخصی های نیروهای نظامی اسرائیل تا اطلاع ثانوی لغو شد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20694" target="_blank">📅 22:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20693">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وای نت عبری : آمریکا سلاح‌هایی را از آسیا و اروپا به خاورمیانه منتقل کرد، زیرا موجودی سلاح‌ها به سطح "نگران‌کننده‌ای" رسیده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20693" target="_blank">📅 22:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20692">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نیویورک تایمز به نقل از مقامات رسمی نوشت: ترامپ تصمیم گرفت با وجود هشدارهای ستاد مشترک ارتش در مورد مهمات، جنگ را آغاز کند و انتظار پایان سریع آن را داشته باشد
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/20692" target="_blank">📅 21:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20691">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فرمانده سنتکام وارد تل‌آویو شد
برد کوپر با رئیس ستاد مشترک ارتش اسرائیل و دیگر مقامات ارشد ارتش دیدار خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20691" target="_blank">📅 20:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20690">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کانال ۱۳ اسرائیل : اسرائیل در حال آماده‌سازی برای احتمال اقدام یک‌جانبه علیه ایران است
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20690" target="_blank">📅 20:44 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
