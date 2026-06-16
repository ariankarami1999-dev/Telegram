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
<img src="https://cdn1.telesco.pe/file/RqMaorm3zKQiAfUDcJ_DcTuZSGPrkAOdChQOBZZ6YbLofkmLxDeMR2IQMUy8pUuZO8Zd9RUdhwEX7ZLvJ7_KqIwXldCmBK-CKSdwF08m8XSlm4vZwIzL_wIwJxxJNwhQzEOKUvagvWRUwBc-K6TWucE24MoMhb1PerkgqXPIHwZVVUf9CApyerYBy83QhfH346vSirWpsjLqKEC1g2YdkcNa721KMyV0uWeLMzTrQnz76oh34dOuFmL82nuNjHgmMbFy9oZiZDw5Sr96A7jliv2orRGuMOtb16R5qhFgM0vvQHcN5yChuPoBhMiUbyQBPXHeK4JWIrtTS4hqg-HCLA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 162K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 00:53:57</div>
<hr>

<div class="tg-post" id="msg-3909">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا من داخل این پست میخوام توضیح بدم این بکاپ ها و این ip به چه درد میخوره؟
ببینید قبلا یعنی تا چند روز پیش شما تو ایرانسل اسکن میزدید واسه ip اینا ۱۰۰ تا میداد برای مثال ولی الان هر  چی میزنید ۵ تا به زور بهتون میده و ip اصلی که
188.114.97.6
میشد که ملت روش وصل بودن رو بستن
❗️
یعنی ip ها کلا رفت تو دیوار کاملا خاکستری شد
اینجا (patterniha) بهش اشاره کرد:
https://t.me/patt_channel_x/68
بعد حالا همه ip ها واسه همه جواب نمیده باید ببرید پشت gpt با یه سری ip محدود برای sni spoof استفاده کنید.
جدا از اون میتونید تست کنید این لیست ip ها رو که واسه شما وایت باشن و مستقیم بتونید داخل پنل های bpb و نهان و... استفاده کنید
🫰
ip:
103.160.204.34
185.193.30.94
45.8.211.57
199.181.197.1
159.112.235.52
170.114.45.239
104.17.21.111
104.24.200.94
188.114.97.6
آموزش ساخت پنل bpb
آموزش sni spoof
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/MatinSenPaii/3909" target="_blank">📅 00:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3908">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AhF6hPTrsTwsX8IOZFP6-AVz3hKmIWV2h7EMvhdaWIC4FYAnrciUYUZl-cdTaX0OddWoOAwcOm9vrqquwTDUG4Ag2Wan9dTomIqpTJRMTJ1gvOK1WK0NBMfvcVpn_pEJ4rMvXmROlSfGvyKts4fgTe3DZPkyinJB3IuzSZY7HBNgEX_eHT-dMuJwG8U4A7AIIZDi-5suXZqQtaAnqjXQsPG37Ne-zRzn22uxWUzp_M-8zIZH8joGYjU5MvePsjcKrBZx4Tpy0ii5ZzCrc5g7oszUrF1pivtFUw75hlJhS_w2Kf9HluLW6rnwHzrrXRuI9hSQKL9V0wqapuNPbN-u-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/3908" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3907">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">متشکرم از بچه‌هایی که دونیت می‌کنن. چه کسایی که استارز می‌زنید، چه کسایی که به ولت‌ها دونیت می‌کنید، همه باارزشه.
من دسترسیم به ولتم قطع شده بود و مجددا وصل شد الان، دیدم دوتا از دوستان 3 و 20 دلار بیت‌کوین دونیت کرده بودن. ممنونم ازتون
❤️</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/3907" target="_blank">📅 20:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3906">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/3906" target="_blank">📅 19:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3905">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر:
https://dash.cloudflare.com/
لینک پروژه‌ی نهان:
https://github.com/itsyebekhe/nahan
لینک اسکنر:
https://github.com/MatinSenPai/SenPaiScanner
لینک ربات ProxyIP یـ‌بـ‌خـ:
t.me/nahanproxyipbot
لینک ویدئوی اندروید:
https://youtu.be/2otJfXgNWCM
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش ساخت پنل نهان
2- اتصال به ربات تلگرام و api کلودفلر
3- ساخت کاربر و مدیریتشون
4- رفع مشکل وارد نشدن ساب در  V2rayNG و ارور 1031 و 1101
5- اسکن آیپی تمیز با اسکنر SenPaiScanner
6- پیدا کردن و تنظیم ProxyIP بر اساس کشور یا بر اساس سرعت اتصال(توی ویدئو نشون دادم چقدر سرعتم بالا رفت برای دانلود)
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره
با تشکر از
YeBeKHe
عزیز
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
(نسخه باکیفیت‌تر)
💰
دونیت</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/3905" target="_blank">📅 19:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3904">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">داریم تستش می‌کنیم این رو، و خارق‌العادست. دم ویسپر و پدی و بچه‌ها گرم واقعا توی ۱ دقیقه پنل BPB ساخته شد واسم و الان دارم پیام میدم باهاش</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/3904" target="_blank">📅 19:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3903">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-BPB-v1.1.0.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3903" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">معرفی نسخه اولیه WhiteDNS BPB
نسخه اولیه اپلیکیشن WhiteDNS BPB منتشر شد.
این برنامه برای کسانی ساخته شده که می‌خواهند پنل BPB خودشان را راحت‌تر روی Cloudflare راه‌اندازی و مدیریت کنند، بدون اینکه لازم باشد همه مراحل را دستی و پیچیده انجام بدهند.
با این اپ می‌توانید:
✅
به حساب Cloudflare خود وصل شوید
✅
پنل BPB جدید بسازید
✅
پنل‌های ساخته‌شده را داخل خود اپ ببینید و مدیریت کنید
✅
پنل BPB را با مرورگر داخلی اپ باز کنید
✅
لینک‌های سابسکریپشن مختلف پنل را ببینید
✅
سابسکریپشن‌ها را کپی یا مستقیم وارد بخش VPN کنید
✅
کانفیگ‌ها را تست کنید
✅
از داخل اپ به VPN وصل شوید
✅
لاگ‌ها و وضعیت اتصال را بررسی کنید
در این نسخه تلاش شده همه چیز ساده و مرحله‌به‌مرحله باشد؛ از اتصال Cloudflare گرفته تا ساخت پنل، گرفتن سابسکریپشن و اتصال VPN.
اپلیکیشن هنوز در نسخه اولیه است، پس ممکن است در بعضی دستگاه‌ها یا شرایط خاص نیاز به بهبود داشته باشد. اگر مشکلی دیدید یا پیشنهادی داشتید، خوشحال می‌شویم گزارش کنید تا نسخه‌های بعدی بهتر و کامل‌تر شوند.
WhiteDNS BPB v1.0.0
@WhiteDNS</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/MatinSenPaii/3903" target="_blank">📅 19:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3902">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">توی NPV tunnel هیچکدوم از مشکلاتی که داخل MahsaNG داشتم رو ندارم. احتمالا به خاطر dns‌هاش هست اما خود V2rayNG و Mahsa و V2rayN خیلی اذیت کردن این چند وقت سر BPB خلاصه یه تست بکنید</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/3902" target="_blank">📅 17:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3901">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">توی NPV tunnel هیچکدوم از مشکلاتی که داخل MahsaNG داشتم رو ندارم. احتمالا به خاطر dns‌هاش هست اما خود V2rayNG و Mahsa و V2rayN خیلی اذیت کردن این چند وقت سر BPB
خلاصه یه تست بکنید</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/3901" target="_blank">📅 17:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3900">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مقامات هند، تلگرام را تا 22 ژوئن در این کشور مسدود کردند.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/3900" target="_blank">📅 15:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3897">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I_Nh43h57SFLCiUzR7BakO3epxHjXVsdd1KdLdySaf8GUskvHEPn4qX4zu4LDvIIVIWuIF_tBnTFS4Y7p7xu_zjk0RLWeSq4egzFKHUzCR5REpJo3C4C3VlJtGJ6lPPDOYxfbVv-7H0X9GcfZ6GWsUwbjwYFjyiK3UPtqd536s3xVIcXAxvZtkzyscpsfElBYZrQdnEzmiDH_dThnw48zcv87wk-ms9AqPZqWJ4vSJs6vhUw_KVdPvkyCO5Dqr-B0USO2w6VqROE11pD2xRAPEYSWdCyRFWXoIJ_x-ykaRE-PwLUfh-jgVfToOLOVZjFroySLwmjJwji6KwI7etRCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UmfdaWETUfv_GfY4u4wpNBO8rFZmv2P_0qI6YKF80h38BYSL3PESwNmk69c6wZY7ukVEQJgE28x9jTh9EUozTgG5Fjm3m52UZ4qNlOkeibOO0ZhbsPp6yHkARmgMOhpZUorCnuH8oYGqBkd0r3kB2qwF9tK00t8h4BfGRZvyL0OEyddRl1oPBOQo8t7rjV8L28TZWhzDmsl997akp-FpP9rwRmL6GPENlp5UdUrKMHAcDQzyNdk94RYCADlZpwOLKC3rjr-zBSiE0niSjtPzJoGDd4lLFbbw-thoZeTvk9y27COzA9Pxd9BZbYnrDnT72idebL9O4lHhRw3gZLWQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rODCBpLuBgUDtm9m3kXIe0ss7TBa5R6pK6e41fSDePG1s0PZGFH0P4O-xCwnHgkmrUUimdr1alhIvYspV7DepVjZbtRz898Tz9nYldasffzUiUEV2hHu8MnEnrcj2qdmCtJl5Iv5MyhEjc0mu0EYBalumKeFMYEBz-_jfpBYRd31CU44dbX3c-mBMMSOAwGo2vht9rKIwq81g7O85bTK64GmjVhH5ZISR1mCYW7IF8Ynb_CXn6fTRZuCcFaXC6-wQ6BpzCA4fmSX7qkFhyOgmu4p0Wgr9KJTMfvE2faeZ8XQjFtRKxNIup_Zbp-1RstbHYOQSuo3ACbbgwt51FW6Tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بعد میگن چرا کامنت‌ها رو جواب نمیدی
چون 90 درصدشون جواب توی ویدئو هست، اما ویدئو رو کامل ندیدن
✉️
مثلا اینا کامنت‌های ویدئو BPB هست</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/3897" target="_blank">📅 12:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3894">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pToho06QkX73pfORUqZ5MuTLkTxKAFQLDjsWb-9WwomXtholaP25CM_vbj7c-kI7AP_EIg3fCbSHBpEgtZxaEdZCb2XC3nnPXSOMYEssbu6-rKRGZBWSKFSahyFtYKAnPEuUh9oGcVzQ1oC-P2lTDvVotELtFvD2qfDZ9FE__4jQrQ--9vmRKn2xuBQ9jsUq9GShSexx5ubdSoM7nnFbXlA6024EzR0VvYu79izfByvGYM4f1N3qo8Jt0dXRp7DVrJT6R4qNR2llx779qyQ_VNh7UAWqnziIK2foHMHcQ19tT1QjXj1MVvQ8Bv9laj3gSLMYlTaMjZ6wcCH5TIFBWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XAKVj1N7nthayb0DXy_9YtyV2SafxUsV7jw0Ti9aqTG2ZT1CllMKgIF7MejsckBjxU0hg-l9r2yw37lDBNmpL8U0fifgaidT_a21XVQIQ2cOUKq4JgiashY1QfaHBzOy0O0G58nJX9l99AajiIaqqMKJJMfcKJgC-T4dUhItkb8HOc71N4yS0B22jGkOGqwnz9xWekZ3gMHZ-im7sbaQ6U2kFlgI88QM9PuPTx7e0anUvw4MdTpf44TqvDY9yIuXZAfuYy6AeExciGA1W-9BoziD9539aV8mkDH5CHzG4SaoDWFY_1i3ys8eQ4-p5nchQ0vdxBQ5zh9JgYoW-LFV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X8BkdzSEf6Boo9tUs3Yxdv3GOTQSkNpZjUpL_KhQG05tT2FPTyTamqIIRuQL0raRpzrupcBtBMJ1xp7HrP-o3a26gaU6jtwCsNi83BMcGenLdHNYELMHfFx1bqf6gp2uP_DYnynIS8XYTCSnbq_29fxFeyK2tCV53nxuYeK6MuRmZMqjAhoa-PEsjODpZ5JdKef1SVOwPI0weXnVq2K4CpKELqkDgd6rIPB0z3ek1zMKr-qNqYysFJv-JIGwmtgAKVWdaIaN9kqjQgrkOfpWZRU0Hlhmu6xiqw6pFOrazo4GFwkT60fcRd3V7J3aVKtjmFRPsdet0HX-QWW_TLFIsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا با WhiteDNS BPB هر کاربر اندروید می‌تواند تنها با گوشی خودش، پنل اختصاصی خود را راه‌اندازی و استفاده کند.</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/3894" target="_blank">📅 11:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3893">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">از دو روز پیش، دیدم که سرعت آپلود کانفیگ‌های مستقیم پشت کلودفلر روی یه سری اپراتورا توی منطقه‌ی ما به شدت افت کرده.
و بعد که چک کردم، متوجه شدم سرعت آپلود خود اینترنت خام کمه و زیر 1 مگابیت، و مشکل از کانفیگا هم نیست.
پیر شدیم برای یه اینترنت خوب</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/3893" target="_blank">📅 09:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3892">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">شمع iced blueberry
🫐</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/3892" target="_blank">📅 16:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3891">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ef-wm8UIW-iLs2lgIgpPMoS3_58valoL9BKqTMF3W_Of5j_OKzfz4YLdc9ZbGeXfsjdm7r-hil7V1dPD2-A2cBNYUIEFsBgVkTLO1sox1wK6dpo-IXqBKiO-z9Bv4mCk-_jRW4y8mMfFreyIHh15uWM6MuJRma3-r1TKqpNyF2zVGemzMwLxFgZMqStpsIHO08JyxVi54qNX_cKJ0f0UL9HEzyFuZufPi019u46V_YPb0q-vISz2kD9Hf4IqQjEBkrX6_t-L-gM4GPUdmnwM-8M3vUvBew8mp-l-qMdlSqZ-mMLdH4pmiUkyAEgwGLL_Px023vyPGFqJfIrn1D9c7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
جدا از همه چی رفقا این ابزار رو خودم قبلا ساختم این ابزار چیه؟
این ابزار کارش اینه که شما لینک ساب بدید کانفیگ میده با فرمت های مختلف و همچنین این که کانفیگ بدید بهتون ساب میده یه سری آپدیت ها براش میدم تا بتونید مستقیم تو اپلیکیشن ها استفاده کنید ولی فعلا داشته باشید و ازش استفاده کنید.
لینک ابزار:
✅
https://xsparvin.github.io/Abzar/
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/3891" target="_blank">📅 13:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3890">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BASO806cPJuKb3v7LOrji6HAv27IUR_PrT6WonfgCYLVBbNGQCqqg3Naqm1VO7gDuXQvzzX5AqWtQ_sRVLsNafHPvrl4bUWi09x1anAoiiSzUkU_ZFrSnEv4wqHqUN9l9MQ5RMPJ9M7sTkjSncxEKIGZ2oRdEHfHin-zdQrWHNpTkMgjgKThxRpXYzdse_WcuWAtRBRvfSTHUzxDpcDL75UTsFbOKiE_65G6ElJYVzCXKr6SQ1hbzJhRbqLuNiEVbxtKo8rIJGezor0V7KupnjXmyGhea41cm6j9qW6QjXIrICwBQYVyZW1zRF8U3lHROrrTxVzo9fHKrNOX5Jrx-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اول که ممنون از لطفتون و بازخورداتون، دوم اینکه اسکنر حجم زیادی میخوره حواستون به این نکته باشه
🧐</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/3890" target="_blank">📅 10:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3888">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IZU4xMhJRl27xFev50hG76YyBpIw0_7O7fguKmDQir54yCAbKwOe74niAX80yfXDGiREqlb0iRCGgbkuY1pX-4DK23KJB1ULZImVRB_s2F9-6vnkakY3jhWEBXhuDuyUMt_vk7u51wmvYPtkxNcaald4NioohVVpF6MEA71Cr9aZOmujZ3JdV9Mq1-v0dIsA-arnioDNu64eIfIFfPW3oa2M7t3_6xL3F_Nb22IeOZCsnlOvK3AQeVLHCOe2No5UhZyXai3Q-nJRHOo8tYndRt9CK1xS34CS-LqQAWTFIBJJJnBhknPbGMSSsRGo-o1_tV3Fk-9uMUcnfVoGZgAo5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EBatWJd0d1BUytXpZM1HxftTVh5FchX1c9Xqk2LXkw2qPxtBLvy_kUQ62VAoV67FhN8Qj7xB8QcCsFKXzUuF3Af1gs6MuSPZuzZs6FOMtJ51R1L3XTka2lcYKZ2KrdyT_eDtJ28J0HKaJ2Izk0udNqnvv6G2yhXiKhSaEFIRdtmza61UOYlPI1u4qp9vQAKS4_5Y4JCyeK7tnXqHpLI3H9Ut-oO0-tAKbxygUMGG_gpnkJwS3X73EX9zQ2zvBWmno5t2G9Ty6ZNgVUpiMomKbMlNQyjCMJy6IYa8ElASvfetXCtwFD7JcKx8L-zdjn2gI1BmdCO_UMDkfYSb_PMQzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور: @nahanproxyipbot</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/3888" target="_blank">📅 10:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3887">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YKrHwuKiyliHhiuSmQIZQ4sLLDcbtIkyNmMfYISqFVBNy7ohOACPW8g3CK4Od3fPvEkdjvsAaB1soxs-cSlFgy7GjyGc-cp4TgnSyPqpFHhPiamFPFGiipKwh1OmAcHeDaxAula_GHBqT8u3bwWea2ueuvLtvvzmTcrGMidkEbrpJadyZWWTVPaTDgcCQ8_KnqZs3iK4eWiAn1Uxb1QvTu_iVVC591xNAko1bYBYSClh57ILQXVQJRR3Zb8fvDWT17f9VRRutlzvoz0TipJZwoUTQNnOY3L-iT9V3cGDcnbrkK5CWShCiI_9UAnS6n5ZpQbum60IbKqorzsQvsJiRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور:
@nahanproxyipbot</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/3887" target="_blank">📅 10:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3886">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خب قیمت دلار اومده 165
انگار جدی جدی توافق(که نه، تفاهم) شده</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/3886" target="_blank">📅 09:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3885">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/na8Rk2HzL7AydljcJA5G-kgnxtA8FLtWTsgBShXYlkdfc0qZK3EZciSJUrsxSA4nu8-Zt8BUe73XeJyeOCbzJdZWfOUDCEqixbCNmSx7VtzRJJWRtpTvERyvR_BdSTNgSCsW6yXSKTT3ORoAr430qw7yZrtPm7GGL2VAq5PrriPK7LNnhFf6pmUapvAb0oxE_YpmXHS4dhsCIQB-eAHPOTtO9BOWhvXKiiYGFb0RjFKe-8emuj1o4x5f2Uluz7aD-RdA5K6K7Mr4DFt1FntjeNFBt5aQ0DgWB-UFC02MT2DW8AX0uUXTRoZNIQy7KS3Yh6brJONZo6u0aAPaXGje1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پروژه‌ی جالب دیدم به اسم SurfSense، که بهش می‌گن جایگزین اوپن سورس NotebookLM
📞
اگه از NotebookLM میاید، باید بگم که SurfSense همون کارو می‌کنه؛ صرفا با کنترل کامل دست خودتون. خلاصه بخوام بگم، یه agent تحقیقاتی اوپن‌سورس و با تمرکز روی حریم خصوصیه که شبیه به کار NotebookLM رو انجام میده.
👍
مزایا نسبت به NotebookLM:
• اتصال به ۲۵+ منبع: گوگل درایو، Notion، Slack، YouTube، GitHub و افزونه‌ی مرورگر برای ذخیره‌ی هر صفحه‌ای (حتی پشت لاگین)
• آزادی انتخاب مدل: ۱۰۰+ مدل از طریق LiteLLM، یا اجرای کاملاً لوکال با Ollama و vLLM
• بدون محدودیت داده: هیچ سقفی روی تعداد منبع و نوت‌بوک نیست، و دیتا روی سرور(یا سیستم) خودت می‌مونه
• جستجوی بهتر: RAG دومرحله‌ای در برابر سرچ تک‌مرحله‌ای NotebookLM
• قابلیت‌های تیمی جالب: به شما رول‌های Owner/Admin/Editor/Viewer میده + چت و کامنت و...
• تولید پادکستا بدون محدودیته
😭
معایب:
• نصبش هلو برو توی گلو نیست واقعا. رو اعصابه — باید با dependency، API key و فایل‌های Env کلنجار برید
• هنوز کاملاً production-ready نیست و در حال توسعه‌ی فعاله
• باید خودت میزبانی و نگهداری کنی؛ طبیعتا که راحتی NotebookLM رو نداره
#️⃣
جمع‌بندی:
صادقانه بگم، NotebookLM همچنان ساده‌تر و آماده‌تره ولی کاملاً بسته‌ست. SurfSense سخت‌تر راه میفته ولی دیتا و انتخاب مدل کاملاً دست خودته. اگه با self-hosting و سرور هم بخواید پیش برید، به درد بخورترینه.
🔗
ریپوی اصلی:
github.com/MODSetter/SurfSense
آدرس خود وبسایتش برای دانلود مستقیم نرم‌افزار:
https://www.surfsense.com/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/3885" target="_blank">📅 08:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3884">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/MatinSenPaii/3884" target="_blank">📅 21:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3883">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/MatinSenPaii/3883" target="_blank">📅 19:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3882">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vUTtc1DHrhqTfyyPPMX7f_dVUYQVZJif3L1_b2lb2SOCss-NJV8FIQnyXxUSG0hxWzU_MpFAF1jq5fnz258h3puWdVYa9i7Ug-_45v9Cm5Ek4fkcwYcK5vnUqvDXGs2nZpYrD15FHARVNrbXdaSsUiuGdwaYkCquyEXIrQ5t_FY3r41JvWAVTb8Pa1r6ILhnQnGOWrTgE0PR6BiFAdjvtttLgiUgKzrDT3j_bexWkPky7e5SOUEVnCC24jb1KsLf_1vQb1PESbvV4sypbUO3OICSSKtkzeWBzBeH-kxAsTGwkpXjKVDB2jLpBggTuKyA5k6kwaw9kqPeDQ2sMeXnBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این ارور رو برای اسکنر یا هر پروژه‌ی دیگه‌ای می‌گیرید، ترموکس رو از گیتهاب نصب کنید؛ درست میشه
https://github.com/termux/termux-app/releases</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/MatinSenPaii/3882" target="_blank">📅 18:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3881">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HOX8d9EC4bz4hY9buHRYSNPIwfb_LtmEaYKhOTnpD4qQDVL_l4DyqLc5ZVEJQi7wjinFcgV2EP3NNbOFn6spdMPWebC3gbSGbKfduvHcv_RQZiZcIILoHNidSKmGV-ACRfYCiTxv-TH0JQnbe2DnQkwGjcXep7dxR1d0JjYWVWZI2pSaH-uvjBZ2LnLogOwkzYJ1T7hOz6kv2rEpXjoeEIFIHuoQtsAKFyWkErbRI5TFVF1_8d4c81E4TR__6gyi-CH6si9WssltwDekiy-xaxlfryCMuSR8bL4Gh5jVoYlLrCfWf5JEYNqmWQukqGSAJFN8wxKkcY3MAmd2rnzh9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الان خودم با سرعت عالی وصلم روی ایرانسل. ۲۰ ثانیه طول کشید حدودا، منتها ممکنه تا چند دقیقه طول بکشه. ولی وقتی وصل بشه دیگه کانکت می‌مونه و قطعی نداره</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/MatinSenPaii/3881" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3876">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.2-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3876" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه جدید اپ WhiteDNS VPN آماده شده.
در این نسخه
• سرعت اتصال بهتر شده
• مشکل داغ شدن گوشی رفع شده
• اپ همانقدر ساده مانده و فقط شما باید دکمه اتصال رو بزنید
متاسفانه باید نسخه قدیم رو پاک کنید و این ورژن رو از اول نصب کنید. این مشکل از ورژن بعدی نخواهد بود.
ممنون
🔥
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/3876" target="_blank">📅 15:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3875">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fN1rP722wJzdFPBTKMQQliaK9kXATm9Cm57XVG3mDjQoXDCgyEQJWSGSuvw--GxGJFjNxjNQCSVsCfZKldwcfxPeaL2FhimsEbdYcNLgC2wAtdTf7_c6hS-W9FehxAnAkpyW4q-LFtoanxj43m8YntuAL8VWQ9bJ6QiGvZDNjty0nvbp4V3Knd_zov6Xd100tJCGzrrNi8xrPmueU_gg0SlxcPzvnJwzGtfgIM1VTlOVfel4oLE1U3XsrdNEwhygcYFKOij_zUKA-5Jbq3CBNlPM3jDGXDTRStorQrQjvZ8xHSjxe43yYCUQEKP3ny0k7eYGOurccJQZRQQ2bIvx_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکرشو نمی‌کردم یه روزی قالب وردپرس رو هم بگن بیاید اقساطی بخرید</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/3875" target="_blank">📅 13:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3874">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خب دوستان به نظر من اشتباه کردم و فونت وزیر متن هستش. مسئله اینجا بود که از من پرسید، گفتش چه ترکیبی بزنم؟ چندتا داشت، یکیش فونت مربع+یکان‌بخ بود. منم زدم همین و بعد دیدم اصلا پولیه. اما الان انگار وزیر متن انتخاب کرده
نکته اینجاست که چرا اصلا فونت‌های پولی و غیررایگان باید بهشون اشاره کنه یا دروغ بگه
🤔</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/MatinSenPaii/3874" target="_blank">📅 12:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3872">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SuzmI4E5D81P3uT5ipasxoLVOfZ8E5zEjNQ41yX7XTVVgbmAi03fblrNEaVaL0zbEZIS83-VTceDKxwmhN25lNwQ-DU5eQTuvmOiFfApyX1voVdPDUUYWkAof7j6r7dV6BeetoSxW754qgc1rgBDABCG9pQIC1r0SS_wChPPvvDiGNTK5QgCgFdkAQlOW2LO1T7Q1qCzw_pgO-qAnGV3YtIPd220ZdyJCVObafkwgkIOloSLNicvPa4yNv5SiPBDdW9vl4iCKG0phwuaisuHKHe2Vqu4OpKNhxJP9dNXmodHiKJo4dPKfdHvvhE-zMisbnNCjmndTt5NQ-vJMXTeMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kW3Hv5vmYVFnd6BpP3ZA1TWUUsFkoVhUltEmMeoCn6wsOrnhq9E928y_Xl303Qm_3Snw3MPxXinv7nudqW7V_gAGP0RGkcj0o9f86MP7yjDlL3lZSn4Ibfz2jhX7J8GOiepf_9Ng5bxWwEJtND-v5BB-a1J5FYwn7gb7eGe9CNCFSdcY1xbdcQF8kANDBf_zRaem92FwkoQThixggn4raxYGSGTQ4I5qg8GkKBSipc_4Lv4mdbTLRpWksRs0knY4dBHkFwFNHj9_72SJtlYHco9FeEXiDV7UrzV_bbL__Bn-FdD7CHBBWp7NjTULSa2wdRrWNOB_pjLWRziuI-HP2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم کپی‌رایت برای کلاد شوخی‌ای بیش نیست. اون از قابلیت اکستنشنش که کل UI و المنت‌های صفحه وب رو درجا کپی میکرد، اینم از این</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/3872" target="_blank">📅 11:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3871">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eoWXRR4aF8jW-oUrxc9LEb4j_m0eV5_IV0P3uhi_-WIAhuwqSOcZXheqMevUXBFAjM6x8ZmllqaHRCZKUVAoDQOgG9qmn-2Fs_E_sR07yOO73HOlzWaOccjTWte223hr62sPCCTg8ThlRBSsI0D920v-1P62_LjUHcB2mdf0z4jx1jBT8Mzom7nPj6YwauFlUXmda7TP2tDc4XkH2e6-pZ9Q52Y0d-f2IOa6nt4s-Preky5mv9sFcfGotpPnXne4W_e_Ssqmpg_9DNGkgtpP3geURPwUFSkTV1xMVNM1I2-m_FvJQlGg2PFTIGohCgezRajK3kNHu1dt3QUgop1ugA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این حد بگم که رفت فونت پولی ۵۹۹ هزار تومنی رو نمی‌دونم از کجا پیدا کرد و گذاشت توی پروژه
🤣
🤣
🤣
اصلا یه کار عجیبی کرد</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/3871" target="_blank">📅 10:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3870">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">در این حد بگم که رفت فونت پولی ۵۹۹ هزار تومنی رو نمی‌دونم از کجا پیدا کرد و گذاشت توی پروژه
🤣
🤣
🤣
اصلا یه کار عجیبی کرد</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/3870" target="_blank">📅 10:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3869">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">من منتظرم که شرایطم استیبل بشه، حدودا ۶-۷ تا ایده‌ی خوب یادداشت کردم هم راجب AI و برنامه‌نویسی هم واسه اینترنت آزاد که واستون ویدئوش رو بسازم</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/3869" target="_blank">📅 10:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3868">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">من منتظرم که شرایطم استیبل بشه، حدودا ۶-۷ تا ایده‌ی خوب یادداشت کردم هم راجب AI و برنامه‌نویسی هم واسه اینترنت آزاد که واستون ویدئوش رو بسازم</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/3868" target="_blank">📅 10:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3867">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏
بدافزارهایی که با ترساندن هوش مصنوعی پنهان می‌مانند!
تصور کنید یک سارق بعد از دزدی، یادداشتی آنقدر وحشتناک جلوی در خانه بگذارد که مامور پلیس بعد از خواندنش، با خود بگوید «بیخیال…» و اصلاً بازرسی را ادامه ندهد! پژوهشگران متوجه شده‌اند در موج تازه‌ای از حملات نرم‌افزاری، هکرها از ترفندی مشابه برای فریب دادن هوش مصنوعی استفاده می‌کنند؛ آن‌ها بدافزارهایی می‌سازند که بخشی از متن‌شان طوری نوشته شده که هوش مصنوعی از بررسی هرچه بیشتر صرف نظر می‌کند!
ابزارهای هوش مصنوعی کنونی، ترمزهایی از پیش تعریف‌شده دارند. برای مثال اگر از آن‌ها راجع به نحوه‌ی ساخت «بدافزار»، «تسلیحات شیمیایی» یا «تسلیحات اتمی» سوال کنید، فوراً ترمزشان کشیده می‌شود و از پاسخ دادن طفره می‌روند. حالا هکرها متوجه شده‌اند که با افزودن این نوع از متون ممنوعه به بدافزارها یا نرم‌افزارهای معتبری که آلوده شده‌اند، می‌توان فرایند بررسی امنیتی کدها از سوی هوش مصنوعی را هم مختل کرد.
به زبان ساده، مهاجم سعی دارد کاری کند که ابزار امنیتی وقتی به بدافزار می‌رسد، به‌جای بررسی دقیق کدها با خود بگوید: «من اصلاً اجازه ندارم این را تحلیل کنم» و از آن رد شود.
﻿
این نوع حمله نشانه‌ای است از ورود به مرحله تازه‌ای در امنیت سایبری؛ مهاجمان دیگر فقط انسان‌ها را فریب نمی‌دهند، بلکه رفتار هوش مصنوعی هم هدف قرار می‌گیرد و ترفندها در گذر زمان فقط پیچیده‌تر و خلاقانه‌تر خواهند شد.
✍️
NooshDaroo</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/3867" target="_blank">📅 08:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3866">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uh5_p0jDxdTA_oOFUs8ZSC76cLd57cxp8Q_2kWopafPdZ7KOYkeH4ynUYa_LnzGcOYEfwasux04eMtFhDx_16VNvqvV1nH9T6I_ut3An2ZeSie6utTfosHkgI0uiuws4IbIN3X5vARfKM5KKlEAKENDwelxDX5ZgA7MwjuGnxlz72-5_jk3aAdbZa9x4wR_e6yJ63-W-Nc8tXhzHJ_181nLHXsuAmuR9Iji4WK-dvgKAW-VbGkR9-9JHylIYVL7i8xokJkq88NX791EN1n--z0nj-zf7D_8GWM73TOX2n91SepzRnQSFcGysnb3IYx4z75h6nahytKmbo9ZZvlSyGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید دفید قراره قابلیت چت با رمزنگاری e2e داشته باشه؛
باهاش میشه ارتباط امن با خارج و داخل ایران داشت.
کل این قابلیت با ریزالور ها کار‌ میکنه تا توی فیلترینگ و قطعی شدید هم وصل بمونه.
طبق تست های من یک‌ سرور متوسط با ۸ گیگ رم و ۴ کور سی‌پی‌یو میتونه تا ۵ هزار کاربر انلاین رو هندل کنه!
اینجوری کار میکنه که هر کاربر یک اکانت رندم واسش ساخته میشه که توی سرور های مختلف ادرس اکانتش ثابت هست؛
ادرس اکانت شامل ۲۰ حرف انگلیسیه که هرکی این رو داشه باشه میتونه بهتون پیام بده.
(سیستم اکانتینگش تقریبا شکل شبکه اتریوم هست، یعنی‌یک seed دارید که با اون یک اکانت ساخته میشه)
کلاینت هر ۱۵ ثانیه به سرور هایی که بهش وصل هست درخواست میده و پیام های جدید رو میگیره و تقریبا برای ارسال یک پیام چند کلمه ای باید حدود ۴‌ کوئری دی ان اس کوچیک‌به سرور بفرسته!
واسه اینکه به سرور ها فشار نیاد محدودیت های سختگیرانه گذاشتم، ولی همه این محدودیت ها توی سرور قابل تنظیم هست و اگر سرور شخصی راه بندازید میتونید محدودیت هارو کمتر کنید.
https://x.com/i/status/2065531715041239193</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/3866" target="_blank">📅 01:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3865">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Opvq4Ndm-WXNyKQoAjEr0xPWfqxtL_o1eg4mQHlFV7tPe1aSze4R6XDPEH7NZm7WXKmNChqLxc0CCNAR-L5RXzWfIyfo17zNEOS6Dn_iYRfmo52SreNBq8JcKhTzkikQWU0uC_3OD0F94fxL3n52N54FyTE3-5PwCHdak4VcLiZ5Xr_TX2YOt_OqqBsQMiEO7CoyPttBpYdCgJKy9CRbFPoAdCQlojsb2U_Xt3O5LGheROcYYUrV_YcnuRRf8WTPOzu_PMVZIlEiPQPCJWvEttiQKHqdwBO_3sft8KuKBl90wOAl-afAQnF-szNMmp6ikRHU-GewUpjVa8CuCb31UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا به هیچ وجه روی کانفیگ Websocket معمولی سرور شخصیتون نباید اسکنر ران کنید. فقط روی Workerهاتون انجام بدید که ارزشی ندارن و ابیوز هم نمی‌خورن</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/3865" target="_blank">📅 19:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3864">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">برای اندروید و ترموکس، کسایی که مشکل دارن طبق این آموزش دوستمون برن</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/MatinSenPaii/3864" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3863">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">برقا باز شروع کردن به رفتن؟ خیلی دیدم امروز توییتر وسط کد و گیم و ادیت و... برقشون رفته بود</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/3863" target="_blank">📅 17:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3862">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مرحله اول  همه بخش مرحله یک  رو کپی و توی ترموکس بذار
pkg update && pkg upgrade -y
pkg install golang git -y</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3862" target="_blank">📅 15:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3861">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دیسلایک فیک میزنن انقد خوشحال میشم پولشونو میریزن جوب
😂
(توی یه ثانیه یهو ۱۸۰ تا اومد)</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/MatinSenPaii/3861" target="_blank">📅 14:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3860">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نمیدونم این کانالای تلگرامی چه گیری روی ری‌اکشن دارن
میگن ری‌اکشن بزنین انرژی بگیریم. انگار از ری‌اکشن برق تولید می‌کنن
عقل ندارن راحتن به خدا</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/MatinSenPaii/3860" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3859">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دیسلایک فیک میزنن انقد خوشحال میشم
پولشونو میریزن جوب
😂
(توی یه ثانیه یهو ۱۸۰ تا اومد)</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/MatinSenPaii/3859" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3856">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oEWI-64NBqDP5MxElXZOaz1JucslPX9h87IabAAWAzdf4RGTBBedpf9kEOrDJNaqzWTuILiRUtTn4NXegEXRkj8gxkWj8ZI-P56NaKGboCxTmFl0DQFddKue1QGTmRKZgUgUhKOCfK-maIwJP1B8_lDUixbK0eSFe-ax1IIZE0k33Eq7yEir13HfcNqa58cZkbTWKlJrBnb0xOfE_heqz7VSGClZwqEUNO2c7go6mT2CnBJXpxliR136Dd80KLcLmypBgxIH9bnjIMiX_9QurQjQ8W5M5iMhvIE90BSzbrNSFVuTh_5j0MyWPKnyv0PQGMVWMmWsGJ_yqWhewuCQEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v2MqKC0QMlEzHFBxuNeHwHirwMwSzfaLqd6S4slR1L3ob8LXb-RyfcNbt95gXMxI9S_xZ1hA1NrwbrLtkOygvtfaoThZh0Pog_6YSWJpeyZ4eJVyuEFbjD8S9VSjh55tQk5caKdAHF3XqF_9tStDeUrKgjRTyxuaAdLobwkCEb0Ti0--RWvfvVnfja5lqk4WNWRRAiYZWlUtE0MaFtZcpZkbQBgYumUANS3R70ex2oEQVOcQWjNG611vSpZdO7_1Kaftk88GPLphIyOSKeDokwhNXQ2TZtNrVp0ryrr__Q-Yqc922EEDDUYb_7y6LssqSszluJDysp5KzyobtH0V7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YTgGpFnZsOABhXWgvTrDyHmMIH6O3fxHY5RwlSYvBwgpnXskS4LdCIMXE8KqQZuBeRU090OVk8zu9dQSHbFaMuV3f_BCEe8PZ2VnuPIbx9aoyKizEj9UD6FqkzbLJ2q0c-xp34ixjOHEcckh5ujhzlU35WRuDOrTZfpNfmsbtkqkL8PcLUX7io5XI2EkzkozURyKtYndSkjUA9gzBbeeeWW1gv6TTWRqi50xMr5WLr0EiGjB1H-MEeJ6s8reYv9P_fhluZ8F4v68nPHczs6fmbsT7-SMke7uaeZa-8M2Jmcg8O0TNRy8MC-L2P99tON8IZZZiv27wWXcCgV4qGiWCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن 0.7.1 از SenPaiScanner منتشر شد
✉️
😏
پروتکل‌های جدید
: پشتیبانی از
Shadowsocks
و
VMess
اضافه شد — هر دو از فاز ۱ اسکن تا فاز ۲ xray کاملا کار می‌کنن.
🧮
خروجی چندفرمتی
: با زدن
e
بعد از فاز ۲ می‌تونید نتایج رو به سه فرمت صادر کنید:
1- لیست Subscription
2- Sing-Box JSON
3- Clash YAML
🔥
تنظیمات سرعت
: فیلتر حداقل سرعت، تست سرعت آپلود، آدرس سرعت‌سنج دلخواه، و سایز sample قابل تنظیم.
🤖
ذخیره تنظیمات
: تنظیمات اسکن ذخیره می‌شن و گزینه «retry last scan» هم اضافه شد.
📚
پشتیبانی از CIDR
: حالا می‌تونید توی
ips.txt
، مستقیم رنج‌های
/13
و... بنویسید.
📱
اولین نسخه پیش‌نمایش
اپ اندروید
با Kotlin و Jetpack Compose اضافه شد. معماری MVVM، تم‌بندی کامل، و ساخت خودکار APK از طریق CI/CD(هرچند CI/CD باید روش کار بشه هنوز).
لینک دانلود آخرین نسخه:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.7.1</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/MatinSenPaii/3856" target="_blank">📅 13:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3855">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دوستان، این شکلی میتونید به من پیام بدید:
https://t.me/MatinSenPaii?direct
اما از اونجایی که دایرکت به شدت شلوغه، و من پیامها رو اسکرول می‌کنم پایین، ممکنه گاهی اوقات زده باشه سین شده، اما من نخوندم در واقع</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/MatinSenPaii/3855" target="_blank">📅 12:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3854">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حقیقتا MiMo اگر پلن پولی بده، خودم اولین مشتریش هستم. توی تسک‌های متوسط Backend شاهکار کرد امروز
هم توی سرعت
هم توی دقت</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/MatinSenPaii/3854" target="_blank">📅 12:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3853">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هم پشتیبانی از Trojan و Vmess و Shadowsocks اضافه شده
هم تشخیص ISP
هم تست آپلود و شخصی‌سازی تست دانلود
هم WebSocket(که بهتره On بذارید)
هم هسته رو به کلی بازنویسی کردم
و این به کوشش دوستان عزیز برنامه‌نویس دیگه هم بودش که اسمشون توی Release note میاد و contributer پروژه هستن. من شاید 20 درصد از این 10 هزار خط کد که اضافه شد توی این ورژن رو نوشته بودم</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/3853" target="_blank">📅 12:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3851">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cNaiT-9CkBZ_TUfzyxzHhvqkwVzv4va1fQa2qFCkhLaNqNmgvrapgLGvFyRbnsZ4qkL2EXaE7E9b1_vsFE0hQJehv3ry6BjZgfcJQDZxIHt5YfWOCx4tKdyJIff3lXmIJdiQH3T71xC7RzvVIfnDCXsDkQSUmSAZFvL5KncJBQmRyfMho7dYM-ZV8Qu68WbW_8Ioqm0HYc4nQJhW-p4TiO1ZCoueO_HWvymgq7fTeu-hnHdmW-M4ACNw9epC_i1kE0GVyFbwMZhjBdsLsnqetuSdr4FyPhj6G0Y7HpkteOP03EFiYoLuMcrczNx0cJCqN6xe2cWMsxwLOf98eT-hJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pQH8dSVYKa3_x6vzsCNhppAzYkRxZhst6vZwPXkUwoY24anoJhXee6SUKf7J5xexM4akPBT-qDxlUAz09fIPZ0AwTNPaqdKz2SDjeC9vkIPZkcNg3e0wn-EmJDqreamhECCQIfzoBKmy0s1_fJPGFnct18J7gqvMwWOW68bX3hr0wkXGIUsMoLQY0YrlNkTkWzgOKdbztNBkMDgM29v3VPVhBjBU8-ylikIWx4STCjqz8nQkwPraJjz0kTaMNVuLlFR9JdjmmLm33CyZPPjF01P29tlOWOkHfqWdnuUBt8FkQAzg9CoJag1AhSqsv0Ib1CJPW7fQe0tnaBxaD-z5Xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بازخوردهای خوبی گرفت این ورژن که باعث خوشحالیه
❤️</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/3851" target="_blank">📅 11:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3850">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hJnOllz3gPDjZuag03wMoFUK_Zio1kshJsKvIDQy1C04HJGzO7YMXbfDE3pmvWM2GD-qX7RelaNtBkH3kALchiXUVeROZOcVeDYsWflPKqywrkTkNrz4GvTL-WUlxjEbEZ8Ys26te04SCKhJ0pR_TsDW5UfexKGT3zfUx4YmTsyO8VaYa4X936RQ0Fujc9jllNO1jmittnTnRqrcfQSj-C3uBUlpqQBiHLknUtZjkqMcBHck1cbpth_Foe0Fu_T_7o5iC7IM53ubYhmXMPvgEMH4n4obNwd4f-JYGkxQhitOjy4Pn1vTVDlHhgFDXINCqhONVCRSWwwE5rKu9XPTsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازخوردهای خوبی گرفت این ورژن که باعث خوشحالیه
❤️</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/3850" target="_blank">📅 11:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3849">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/3849" target="_blank">📅 11:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3848">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a-ev3MlRvukMyC1x6W5Ve_shZW9HT3RlV8RgyQX_3CR5TS9MRQ5kbEgb1XXLWZ3YZ5ZmBl6wgVCbMqjimBPKgWordWiltQrx94N6nUxSLWw6BfbvyMTxXONsfy9r6ykjjyOKKTqquV0yZ5rBIhQFXNsrmOQa_VJVXeX9vpeh9by5yWtCmQTgMmGx_Jaq9PJhyJ6RzEBIseu9yaR-gHYMFj8WlAy_q48hhdYuj2L57xOLRDOzLsc00o1GidUUbGn602LReRuJ9992vXxMFIhVX22wFEu2Ge9jOzJDDmFcMqG9xdI5J9XZHXUwKgMxR-SovjV5VrPwTQxEMqsD7c5VYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان خوب، لطف کرد و هسته‌ی اندروید و تمام چیزی که برای ورژن اندروید نیاز داریم اد کرده، صرفا منتظرم که خود اسکنر عملکردش به بهترین سطح برسه، اون موقع نسخه‌ی اندروید هم بیلد میگیرم</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/3848" target="_blank">📅 11:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3847">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نکته‌ی خنده‌دار اینجاست که دولت آمریکا دستور داده دسترسی به این مدل‌ها برای هر فرد غیرآمریکایی (foreign national) — حتی داخل آمریکا و حتی کارکنان غیرآمریکایی آنتروپیک — مسدود بشه!!  آنتروپیک اعلام کرده که چک کردن ملیت کاربران به صورت عملی ممکن نیست، بنابراین…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/3847" target="_blank">📅 11:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3846">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/3846" target="_blank">📅 11:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3845">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/3845" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3838">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">32 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3838" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خب، دوستای من هستید یه تست از اسکنر ورژن 0.7.0 بگیرید؟</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/3838" target="_blank">📅 11:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3837">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خب، دوستای من
هستید یه تست از اسکنر ورژن 0.7.0 بگیرید؟</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/3837" target="_blank">📅 10:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3836">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o2lAwO_sUIqCIy6bJ1ULdf984Dz6G3FUA3Il7GRdVeOhND1pKeLCZULtV55YT5ZdLSHuEzcsE3zCPGtSGViOA3Ai4IBPFre5NQ6AZRZESQ6YVab1A2U4gJf1FqJjR5kM5LKqwlXyF8uNui3gYfCkBIzrFuFE6nV_6DA0iy5_jWv8V3tA00tnSy6HQzkMrwNH46_t9XoUOK5Nia3-qwY3V8x35FW7yuen_deUpfVvI6dIucqvwdYClgvY9gA4EUhvfiQgyVgAH6_vbdVc66ijikxnlRnAwMDpbpaTma8qBAI1aiUEcwltzAF3r8ScWdwZS6XYF2u5-_XM5EV5D3Jb2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لپ تاپ اوکی شده الان اومدم تست کردم MiMo رو و خوشگله یه تست پرفورمنسی بریم باهاش روی SenPaiScanner</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/3836" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3835">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bR_HToxovXPDOUqUPvY2IALWBh_rzlfD2Qt6RcqFzSTHEd2a09i1KNVbbXnwR44zuhB2LTZms_eQlsvmKqiGdxpDeObtLsWRmrnsCywucNnGL1amx6OcpQOjOxVfDlP61YDvrg0pv7kDLk6JN-PGP9T9LrbZzMJnBLrgDv8S9qS2exHf53bYuiK8aecIwZKeF5l2W3pTILYG2g413VHaD1o6UrJTXVIRiJq5u1l0HxIHyiVt2yMG8gLSlenjP4aDRO9TOGoDB_CNFd5rbpNvkR0jrawSV5FQoJWpyVeBiN0piUBv17G5h9cYkn3CGfAmjYGD7e8pkojZGO5gcv3cMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد  توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش فورک OpenCode هست!).  خلاصه‌ی ماجرا: تیم…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/3835" target="_blank">📅 10:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3834">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">برگام! آنتروپیک به دستور دولت آمریکا و دلایل امنیت ملی، دسترسی به مدل Fable 5 رو برای همه‌ی کاربرا مسدود کرد!!</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/MatinSenPaii/3834" target="_blank">📅 09:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3833">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QDomfgk3L8EQoTUjaPqpKy3LZNBDbJ7TSeoiI_TeGHinaV1JrCf2Kw6R8AtwfGE-nYHnkIzk3CRdBkESw_Eb7ZMvPIbnzPCAsN0osufZoxWJDPRH8UtZ9KgG55G8Bmfn5nbxavQh4CLGfdbL3XtGGjQ5vStey1xOFH8cmyKMvUUAAjQJcxmXBlgFw9qE48XhX1yf008qP67yK-smAl71MNk2wDiogUZUpEwmDdm8uYPdX8okdU23C0E8xwjtmaA2X8nBKxlptOIF9Vxq3rpFLSb6bXdIi7-tfRijVP6W8eIk-WX6tjdgXzs1Xc44T7sJMtJ-Zvwc5sKDccBudcP4lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام! آنتروپیک به دستور دولت آمریکا و دلایل امنیت ملی، دسترسی به مدل Fable 5 رو برای همه‌ی کاربرا مسدود کرد!!</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/MatinSenPaii/3833" target="_blank">📅 09:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3832">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">این سایت رو یکی از دوستان معرفی کرد برای دامنه‌ی رایگان، یه امتحان کنید http://l53.net/</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/MatinSenPaii/3832" target="_blank">📅 02:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3831">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hpBhQdXHnvlQM_a_PHy6eJFC6UIhRLbH4Cyc_bEsmxnE473lvOiebeGHnWvV9_98WS89GCknEZ3n0onjT_zqiGnSVLsoKosE-hdraJh07OOWb-_zEp9ru_8UEu3tJ9wHIJjDoKlnptfg5_b_6RQDivwi7TiV4e5Hhth5Jxz97YpjYexlHhRpkNPbU5tAYB2GaaxxvLByYOQCoejpvWIWl_71OqQElD8EKv8ZukGUyVJPJFY-P0nQwQ8Om8jiYKs5-8htgR3BDOxJRLhR13uThjZOJAti_bD4Lfl44SROXEqXQJjmPQS7LrjlIg5GxKushridqum8veQpuh53WI4iHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت رو یکی از دوستان معرفی کرد برای دامنه‌ی رایگان، یه امتحان کنید
http://l53.net/</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/MatinSenPaii/3831" target="_blank">📅 01:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3830">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">من شرایط ضبط نداشتم دوستان. یه مشکلی هم برای لپ تاپم پیش اومده که باید بدم تعمیر و ممکنه کلا مادربوردش بسوزه اگه روشن کنم ترجیح میدم ریسک نکنم چون دیگه پول ندارم بخرم
😂
تعمیر شد، آموزش‌هایی که قول داده بودم رو ضبط می‌کنم</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/3830" target="_blank">📅 01:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3829">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWireguard Configᵛᵖⁿ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=RJXwCzoxJmr7jDtNE6zQvfgWrtimbzCDsyBnLoqHUtBiOfY4_9tn8RbhgUHf2_Sc7nMSonN34_F-2Ux1w2pfVU2fwrQsSV7JNqluGPbUGyZrgrr_EvYXlUxqyFWOzYJaNukXcAaDKAm96tu5PV6pzjWYZinFExlNQAiWLHRbq2xCcejrLFkjmPZloEGmFvX-PWCiFrYmLM9b62uxosENsmjduKj72l7uwLmxChl6PX_47enXYJdP-_ZhWiKBeA6EqH_ZA7ec8RT4ba8uXF5lJmN9yP5IBruw63LDVNLOynYd7CyOrt4shyCQCaAc3rIlK3nGkBxLIGar7wFts2g7nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=RJXwCzoxJmr7jDtNE6zQvfgWrtimbzCDsyBnLoqHUtBiOfY4_9tn8RbhgUHf2_Sc7nMSonN34_F-2Ux1w2pfVU2fwrQsSV7JNqluGPbUGyZrgrr_EvYXlUxqyFWOzYJaNukXcAaDKAm96tu5PV6pzjWYZinFExlNQAiWLHRbq2xCcejrLFkjmPZloEGmFvX-PWCiFrYmLM9b62uxosENsmjduKj72l7uwLmxChl6PX_47enXYJdP-_ZhWiKBeA6EqH_ZA7ec8RT4ba8uXF5lJmN9yP5IBruw63LDVNLOynYd7CyOrt4shyCQCaAc3rIlK3nGkBxLIGar7wFts2g7nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سا
خت کانفیگ Amnezia VPN
• صبرکنید ای پی ها رو لود کنه
• بعد یکی انتخاب کنید
• تیک فعال سازی پارامترهای امنزیا 1.5 حتما بزنید
• بزنید روی ساخت کانفیگ Amneziawg
• دانلود کنید وارد کنید داخل Amnezia VPN
• میتونیدم کانفیگو کپی کنید + بزنید بعد insert بزنید کانفیگ اضافه بشه
🟡
فعلا روی ایرانسل
💯
جوابه(همراه اول ،مخابرات،سامانعلی)
📍
ای پی جدید هم اضافه می‌کنم
https://darknessshade.github.io/Amnezia-VPN-Config/
@ConfigWireguard</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/3829" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3828">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کلا فکر کنم ساعت از ۱۲ میگذره دکمه‌ی بمبارونشون روی سیریک گیر می‌کنه</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/3828" target="_blank">📅 00:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3827">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tjxCE0LOXg40nzCPiyixP_gYMljKxIrNtBJJQZVm81-DFZ8lvAkpg2mTAfVQiIik_6qIH3W526fIWbqOB8MzVoVa2-Wwyg8fSZiGQU_zpOldr35CfW5hmP4O8sR8IpOJzyuYMXtVohlw598tU4QIFQ2KKWZGIUvJSQHLHNMO3cipyAi8Ik1V3EwXB8A1fl86KNbX0HHz6k66cwd3Jl0o4PQpu_0sXCSTEKA7acCY0DQETi3SulZpctvOmY7_TaGw5Jae5pkqHWqKuyKm42uSDNK9Omq8D8ahI_9aUONm8seIMspJOZipJ4HmLk8Jnv1mP6as0rhbkBRSgkLfS_orzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد  توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش فورک OpenCode هست!).  خلاصه‌ی ماجرا: تیم…</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/MatinSenPaii/3827" target="_blank">📅 00:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3825">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اگر مشکل باز نشدن توییتر با پنل BPB دارید، همونطور که توی
ویدئوی تنظیماتش
یاد دادم، NAT64 یا ProxyIP ست کنید. اگر باز هم نشد، صرفا کانفیگتون رو عوض کنید با چندتا کانفیگ تست کنید، درست میشه.
proxy chain هم صد درصد درستش می‌کنه.</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/MatinSenPaii/3825" target="_blank">📅 21:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3824">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j_fh6SrJhjEnDCIy6bXo09Jdfsc6tJPHJa861ertu4mpB9WuPklVrY-mbNTJGtN2rLRP1DllSOZpheGA47tQpn4s9BdCPVY8Mo73MKAUHYxe8iIHPzUh7vl6alhnnse0DbFdbcgeyBXCigFpB7n7dnca8muNC-9G3UeiGTj9VnU15lOjD9A99k3gieYWiCb7BfHvnMHWFZCSCK6PP6U9cEutxN5Q3XCNHzZnVr3oUDIRw-4isqvGRCLmwa_xj7qUYnxUgfXsQjDIuPrqLGhDnT5SNq40DtWBSg8ZbTbHHsqOpOWXN2y319-CWWOfL7OCiCdvTvw2fqmV_tP5lzgoFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد
توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش
فورک OpenCode
هست!).
خلاصه‌ی ماجرا: تیم MiMo شیائومی به‌تازگی، دو روز پیش (۱۰ ژوئن ۲۰۲۶) نسخه‌ی
v0.1.0
از یه
AI coding agent اوپن‌سورس
با لایسنس MIT منتشر کرده که توی ترمینال کار می‌کنه و برای پروژه‌های پیچیده و
long-horizon
(بیش از ۲۰۰ مرحله) ساخته شده. این ابزار فقط کد نمی‌نویسه؛ می‌تونه دستور اجرا کنه، با Git کار کنه و در طول جلسات مختلف، درک عمیقی از پروژه‌ت رو حفظ کنه.
از اون‌جا که نسخه v0.1.0 هست، طبیعتاً یه پروژه‌ی اولیه و اکتشافیه — ولی معماری‌ش جدی و قابل‌بررسیه.
ویژگی‌های جذابش:
۱. حافظه ماندگار (Persistent Memory):
برخلاف ابزارهای فعلی که فقط به context window مدل تکیه می‌کنن، اینجا یه subagent جداگانه (به اسم checkpoint-writer) توی پس‌زمینه کار می‌کنه و تصمیم‌ها و پیشرفت رو لحظه‌به‌لحظه ثبت می‌کنه. حافظه روی
SQLite FTS5
(جست‌وجوی full-text) ذخیره می‌شه و توی فایل‌هایی مثل
MEMORY.md
،
checkpoint.md
و
tasks/<id>/progress.md
نگه‌داری می‌شه. وقتی context پر می‌شه، خودش از روی آخرین checkpoint بازسازیش می‌کنه؛ یعنی دیگه نیازی نیست پروژه رو از اول یاد بگیره.
۲. ویژگی Dream و Distill (خودتکاملی):
دستور
/dream
به راحتی جلسات اخیر رو اسکن می‌کنه، دانش مهم رو به حافظه پروژه منتقل می‌کنه و موارد قدیمی رو حذف می‌کنه. دستور
/distill
هم کارهای تکراری رو پیدا می‌کنه و تبدیلشون می‌کنه به skill یا command قابل‌استفاده مجدد. هر چی بیشتر کار کنی، بهتر «پروژه‌ی شما رو می‌شناسه».
۳. قابلیت Max Mode (آزمایشی):
چند راه‌حل موازی تولید می‌کنه (best-of-N) و با یه مدل داور بهترین رو انتخاب می‌کنه. که با
experimental.maxMode
توی فایل کانفیگ می‌تونید فعالش کنید.
۴. قابلیت Goal Mode:
با دستور
/goal
یه شرط توقف تعیین می‌کنی؛ وقتی agent می‌خواد متوقف بشه، یه
مدل داور مستقل
چک می‌کنه که واقعاً شرط برآورده شده یا نه — در نتیجه جلوی توقف زودهنگام و خوش‌بینانه رو می‌گیره.
۵. ویژگی Compose Mode:
با زدن کلید Tab فعال می‌شه و یه workflow ساختاریافته برای توسعه مبتنی بر spec ارائه می‌ده — با skillهای داخلی برای planning، اجرا، code review، TDD، دیباگ و merge. کل چرخه از spec تا کد نهایی.
۶. ورودی صوتی، Git و Multimodal:
ورودی صوتی real-time با
/voice
(بر پایه MiMo ASR و TenVAD، مخصوص کاربران لاگین‌شده)؛ مستقیم با Git پروژه‌ت کار می‌کنه و multimodal هم هست.
۷. سازگار با Claude Code:
authentication، skillها، MCP serverها و دستورهای قبلی رو توی یه مرحله import می‌کنه از پروژه‌ای که داشتید با Claude می‌زدید.
۸. انعطاف‌پذیری مدل:
MiMo Auto به‌صورت
رایگان(1 میلیون توکن اگز اشتباه نکنم) برای مدت محدود
و بدون کانفیگ در دسترسه، ولی خودش هم از هر API سازگار با OpenAI و prov/erهایی مثل Anthropic، DeepSeek، Kimi و GLM هم پشتیبانی می‌کنه — یعنی vendor lock-in نداریم.
نتیجه؟
طبق ادعای شیائومی، توی بنچمارک‌های SWE-Bench Pro و Terminal Bench 2 (به‌ترتیب ۶۲٪ و ۷۳٪)، با همون مدل پایه حدوداً
۵ درصد
از Claude Code جلوتره(که هنوز بعید میدونم. به چینی‌ها اعتماد ندارم). اما می‌گن تفاوت واقعی‌ش جایی خودش رو نشون می‌ده که کار طولانی و چندمرحله‌ای باشه — نه «له کردن»، ولی برتری معناداری توی long-horizon.
نحوه استفاده (خیلی ساده):
۱. نصب یک‌خطی (Mac/Linux):
curl -fsSL https://mimo.xiaomi.com/install | bash
(بهترین تجربه با iTerm یا ترمینال VSCode)
ویندوز:
npm install -g @mimo-ai/cli
۲. اولین اجرا:
خودش راهنمایی می‌کنه — MiMo Auto (رایگان) رو انتخاب می‌کنیم، با حساب شیائومی لاگین می‌کنیم، از Claude Code Import می‌کنیم تنظیمات و... رو، یا خودمون می‌سازیم.
۳.
می‌ریم تو پروژه و کار رو بهش می‌سپریم (با زدن Tab بین agentهای build / plan / compose سوییچ می‌کنیم).
لینک‌ها:
- گیت‌هاب:
github.com/XiaomiMiMo/MiMo-Code
- سایت:
mimo.xiaomi.com/en/mimocode
- بلاگ فنی (درباره long-horizon):
mimo.xiaomi.com/en/blog/mimo-code-long-horizon
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/MatinSenPaii/3824" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3819">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hPlGw0wxuaBCg_iWocuoQO--0UGBqxbMjohcXHwA8YKNhiw5C1XKsJ9PTXNX8xbLjuqOvBLvV8pmy8EWnigqEmm_z07csO_fOX-KWO9oNCtFb3dhv_jKO7Pev8c5VNs1-CuxBmPPTt_pMyIHP2wAmc9C1oStGPkW2QFkYFH_EuTuhcaJNelK7mJzeI8eFL9R40Iv_ZKUn43tRPMQrt_doT7AomQsWqwzH8ktm4OAcoC05Oyj5LfNxyPRrnv4trKDkXQsLtRZ41--R1iovAy3o_s0kog-pzV82DfXIsfJtC5V5yBI0QWHGpk2H59hRMMQAO34zW3fQuR7owUoIBzU1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از ChatGPT بپرسید که
یه عدد بین ۱ تا ۱۰۰ انتخاب کن
بهتون به احتمال زیاد میگه 73! علتش رو هم از خودش پرسیدم:
وقتی کسی می‌گوید «یه عدد بین ۱ تا ۱۰۰ انتخاب کن»، من واقعاً عدد تصادفی تولید نمی‌کنم؛ بیشتر یک عدد دلخواه را انتخاب می‌کنم. بعضی عددها مثل ۷۳، ۳۷، ۴۲ یا ۶۹ به خاطر الگوهای آماری و داده‌های آموزشی بیشتر از بقیه به ذهن مدل می‌آیند.
جالب اینجاست که در آزمایش‌ها، وقتی از انسان‌ها می‌خواهند یک عدد «تصادفی» بین ۱ تا ۱۰۰ بگویند، عدد ۳۷ بیش از حد انتظار انتخاب می‌شود. مغز آدم‌ها از اعداد خیلی گرد (مثل ۵۰) فرار می‌کند و به سمت اعدادی می‌رود که «تصادفی‌تر به نظر می‌رسند». من هم تا حدی همین سوگیری را دارم.
پس اگر چند نفر قبلاً همین سؤال را پرسیده باشند، کاملاً ممکن است من دوباره ۷۳ را گفته باشم
امروز توی توییتر اینو دیده بودم و واسم جالب بود علتش</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/MatinSenPaii/3819" target="_blank">📅 15:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3818">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ByrIMOaXXOpv2XBdCdP2dQVLgZ8R0bEyeT2MukF99Q6aVd4kvKIAl7pcHeoqkN4NKIBsL4gddoJKpUMc8yqObnbmPOFb1mUO97jGXOdBCOKOnR-orstXXwLiHxTBsyuvjnWLqw75xZDU5zEZgGHAu78wcB-xFd-1BI2KxWMRZ7GNdSd7MDtSzXyy-2puQBKdPrBfnbeiTUBz8rU6Qger_Z-aMrOESWjG6ex2EjMRzvls2m9De6FvHj9KSm5XcQ8ocwZBKRFBwG319WjLwUTLlfkzZHcIHf-wr7DIZdLxBngt5lOLucdYCrZhTYJ5QlBCaJziAHWTfA7jUO1IA5ED8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار باحال آنلاین پیدا کردم: یه عکس می‌دی بهش، بهت گرادینت میده با کلی تنظیمات.
برای وقتایی که دنبال یه بک‌گراند یا پلت رنگی هماهنگ با یه تصویری، عالیه.
تو مرورگر کار می‌کنه و رایگانه
👇
photogradient.com
‎
✍️
Reza</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/MatinSenPaii/3818" target="_blank">📅 14:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3817">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا
ابزاری که امروز معرفی میکنم...
داخل این سایت میتونید تمام ip های مربوط و بنا بر نت خودتون چه برای ورکر و کلودفلر یا شیر و خورشید اسکن کنید
❗️
ویژگی ها:
💡
اسکن راحت و سریع و دقیق
رابطه کاربری خوب برا همه سیستم ها
داشتن ip بیشتر cdn ها
لینک سایت:
✅
https://cdn-scanner-pro.vercel.app/
توسعه دهنده
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/3817" target="_blank">📅 12:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3816">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2658a29175.mp4?token=NMfP7MUgn98XZaroMwRmoz_X6zYOqvF2tD0RpIeSFJyNyO3KzU3gdOKCkpV7YrFMf67C9FW0fpA84FFgRbKMPpnCLb8yebXwP2MgHdar09liy6UgkYgTZKD2V_BT5UP3v4fEjeBFFgDTplwB74PjiUDNfaDnrMhDjeU8UBwCWweY-H9--K8m1FzF9Nm9G2N4k-GsJI5vEQbQv3IdEfwBSIdTPOUbq_dj6qwG5nkbayDtYKfiwz4SK5cc90lbo-rrc5sFjw79WXIArBgPKK8JDfVly4cbS7DjdnnfCGesL93XJmpZvlnQE-qdKpuzdgm0512BtO20YfSunLI8oIBgWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2658a29175.mp4?token=NMfP7MUgn98XZaroMwRmoz_X6zYOqvF2tD0RpIeSFJyNyO3KzU3gdOKCkpV7YrFMf67C9FW0fpA84FFgRbKMPpnCLb8yebXwP2MgHdar09liy6UgkYgTZKD2V_BT5UP3v4fEjeBFFgDTplwB74PjiUDNfaDnrMhDjeU8UBwCWweY-H9--K8m1FzF9Nm9G2N4k-GsJI5vEQbQv3IdEfwBSIdTPOUbq_dj6qwG5nkbayDtYKfiwz4SK5cc90lbo-rrc5sFjw79WXIArBgPKK8JDfVly4cbS7DjdnnfCGesL93XJmpZvlnQE-qdKpuzdgm0512BtO20YfSunLI8oIBgWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیگما یه اکستنشن کروم منتشر کرده(فعلا برای کاربرای پلن پرو) که با رفتن توی اکثر وبسایت‌ها، می‌تونید با یه کلیک، تمام اون صفحه‌ی وبسایت رو به شکل فایل قابل ادیت فیگما دریافت کنید.
برام جالبه که سر بحث کپی‌رایت و اینا کسی بهش چیزی نگفته هنوز
😁
اما خب گویا هنوز با چنگ و دندون قصد دارن نگه دارن اکوسیستم فیگما رو بعد از اون سقوط سنگین سر Claude Design
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/MatinSenPaii/3816" target="_blank">📅 11:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3815">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏این روزا اسم Agent Harness رو زیاد میشنویم، ولی بیاید ببینیم واقعا چیه و به چه درد میخوره!  همونطور که میدونیم context window مدل‌ها محدوده و اگه به صورت کارآمد ازش استفاده نشه، خیلی سریع پر میشه و مدل مجبوره برای ادامه، یک دور summarization انجام بده.  بعد…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/MatinSenPaii/3815" target="_blank">📅 10:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3814">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X8KFSfdftdZBnrhhyTDAdJttjasnvkKfHE4_0i0i7t9gTxp0mcFEAyuM1MrtXIWT5DxSUdmSne6U1EhUwQ9-VSTearWc7rkT5-boJ7WY8pVquUA5b9LV12SFCdCgpMP8138ZQdwz9ok9cg0jBDBEwdDGr63bq2h5iG8UbY9N9Sx9AGW7J2z2H4ExisYaaDxKtFNBUsTEMN-pe4N8qNUTg2pf2gxTYD6sniJMC4JEudivfp713uvf-ssq6gJo-kvUzBLPqpugmHAoh0HCwg5gk4Zsa_0mkkRL60LBUE-oxXAHk3-oR3Da-y9rcbwvjzxoDEEJLrdeZdiaLNoQVGeWLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏این روزا اسم Agent Harness رو زیاد میشنویم، ولی بیاید ببینیم واقعا چیه و به چه درد میخوره!
همونطور که میدونیم context window مدل‌ها محدوده و اگه به صورت کارآمد ازش استفاده نشه، خیلی سریع پر میشه و مدل مجبوره برای ادامه، یک دور summarization انجام بده.
بعد از چند دور summarize کردن، نهایتا بخشی از دیتای مهم از بین میره و تسک به صورت کامل انجام نمیشه! پس اومدیم یک سری تکنیک پیاده کردیم مثل تقسیم کار بین sub-agentها تا از پر شدن سریع کانتکس اصلی جلوگیری کنیم.
بعد این ایده مطرح شد که بیایم هدف نهایی (PRD) رو تعریف کنیم و اون رو به تعداد زیادی sub-task تقسیم کنیم، بعد مدل رو در یک loop بندازیم که با هر بار اجرا، یک context و یک prompt جدید داشته باشه و بعد از هر iteration چک کنیم که تسک به صورت کامل انجام شده، و در غیر اینصورت چرخه رو دوباره تکرار کنیم!
در واقع به جای اینکه برای اتمام تسک به مدل اعتماد کنیم، ما در یک لایه بالاتر این رو validate میکنیم و اجینتِ تنبل رو harness می‌کنیم :))
✍️
Amir</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/MatinSenPaii/3814" target="_blank">📅 09:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3813">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z7fK95eSA2X4NRRAOLtDfcDQY0x6wUf2qk-3rWTfojAwm2kUOCJTxLq2Bvn5mBuCZr1lxZKKLXYuYNLltEHy4LrAsvhNYDMHL7g5HyekggGzequkV8A93uNLjzfoJqasZRNtpnTHpZstH8OQ5nzCLf4oY-3mOWH1D7NP_MTwvBX_Uyycs2kP9RqWiVpdQ2szuWl6ZYeMiXXq1xgKlaYxDuORk443RECQCS5LhpAPXkXT2NZ2mCRAQ9ma3LQvV69heRByy1byVr6v1jQXV40aAoAgPa7EOTorJsOUfiHxQt_9UhnsxbuLt0PxdZ2ikEMmCG7eoOG5u6nOSMhHK9AuBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله شما می‌تونید دامنه و سرور خارج رو از سایت‌های ایرانی هم بخرید، اما چندتا نکته وجود داره:
۱- احراز هویت سایت‌های ایرانی کلا جالب نیست و خب این ریسک رو باید در نظر داشته باشید
۲- توی شرایط قطعی، فروش دامنه و سرور همه‌ی این سایت‌ها میره روی هوا
۳- شاید عجیب باشه شما اگر از سایت‌هایی مثل netlen و با کریپتو خرید کنی دامین+سرور رو، شاید ۸۰۰ هزار تومن(با کارمزد و همه‌چیش) پات بیفته. اما همین دوتا رو از سایت ایرانی بخری زیر 1 تومن نیست</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/MatinSenPaii/3813" target="_blank">📅 07:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3811">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نکات استفاده</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/MatinSenPaii/3811" target="_blank">📅 01:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3809">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XkVpj_x0rLt5DFcRXqQU0bAdSmDEW2M6WC6TWLCsovuPx6jws1-72760nLcF4x4aeg016gAr0DJ1FkosO1k44YUAU4OD6nh64sh8XdwRfaK4jhhurCPCHiBqVJ6m8cR1dgmbQgWzPiab5kHvU9EYxOErDl7-B0jELyFBubvFp6_Q3Fp3ncvY21WjrWCvm-lmWxKhGCISDUre6KWYiVfe5XWOUJjFbwOz9xGiarluf0jNTzm6UX48ghpx1zanoW3Fvk_GiXI3MEIhmgqToPQqUNFDUA0bO8T4ZY7ezKhqVnDJ-NbeHk8vmW1RcynIkUAl9nns2Zu8fRmdWyBjJpusXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran  * دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)  ///  * حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)  * کافی است لینک subscription را وارد…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/MatinSenPaii/3809" target="_blank">📅 00:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3808">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran
* دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)
///
* حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)
* کافی است لینک subscription را وارد برنامه v2rayN/v2rayNG کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
* نکات استفاده رو حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/3808" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3807">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GS1ffA5UyDn022ljEAZNFDzove0R4M5eKJURSI7AxnKPlsovgvL-UyuSNlJyqKdle4FThFWP2WGNOovZ6grfJgc0vmQoUt4hhZsZAHlwprA_YJG_e4-xb4gpSw9wIazAQoGswW-jbSS0JKUJmwXpFSyPk7E4DtwlYVSF1Qh5ygwyRq5SZKh6ZWGFTG_eDs-vGmv-VlBA39VvD4lkaWlfE1e8Tp981pf6p6prKrCFkLD22EMIWrTmobxrYxKN6asdQsUYMyyw_wooThgSPAUyoA9O_56pZqYFIzOlTUC5msHbyYzA4NfjB97FBXLxAbJiEjGw25_8Znf6rZOOlrQ9kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از http://Netlen.com.tr بخرید، دامنه یه دلاری هم می‌تونید بگیرید و با یه سرور ۳ دلاری و کارمزد، کلا میشه ۴.۵ دلار یعنی کلا ۸۰۰ هزار تومن. دامنه یه ساله هست، سرور یه ماهه. یعنی ماهیانه ۶۰۰ هزار تومن تقریبا. ۵ نفر باشید میشه ماهی ۱۲۰ باز هم خود دانید</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/MatinSenPaii/3807" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3806">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">درود به همه رفقا
🍷
اگر از پنل bpb و... استفاده میکنید میخواید ip ثابت باشه ولی جز لوکیشن آلمان
🇩🇪
میتونید از ابزار زیر استفاده کنید برای ip های مختلف برای مثال:
میتونید از ip چین استفاده کنید برای دور زدن تبلیغات یا از ip آمریکا برای بیشتر هوش مصنوعی ها خلاصه این ابزار مشابه واسه خود bpb برای ثابت کردن ip هست ولی با لوکیشن بیشتر
❗️
لینک پروژه:
✅
https://smart-ip-scanner.10-354.workers.dev/
توسعه دهنده
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/MatinSenPaii/3806" target="_blank">📅 22:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3805">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏خطر سرقت اطلاعات و رمزهای عبور؛ مراقب نسخه‌ی جعلی X-VPN باشید  محققان شرکت «سایدرز» (Cyderes) کمپینی فعال را شناسایی کرده‌اند که در آن نسخه‌های جعلی چند برنامه محبوب برای انتشار بدافزار استفاده شده‌اند. یکی از مهم‌ترین نمونه‌ها، نسخه جعلی اپلیکیشن «ایکس وی‌پی‌ان»…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/MatinSenPaii/3805" target="_blank">📅 22:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3804">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lnabgnjjAdcv8G0IkU4ls0JPxQb-Jo0ogKBZJbtGuSDmsbohJZsIDbQWwbn_p3OyzQ5xh328RfPTdicUmvcA7BCIzQ5jp_oKa4yxOnPEnidKbRRlgRJLiygo4VsAB1eVM36N9Ty2g8t743Wm9J45Hlpfi0oyeEyDrfvcf-gwF1k6Oce48WbyxyY3dWitlWiLb7p5aoRu3Kvi6E6Ij75wG8gsaMnUPRjIepLU5vhTnTbAWUdJ3JS3q5fwx4PGU1SUp7n44LyDvrAhbinEwmZzN-6LCVbSeydws07LetFYHCcXHgPSlxISVCE3YJ7rIjDJSxM4HKqzZZmdXqUna89dxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
خطر سرقت اطلاعات و رمزهای عبور؛ مراقب نسخه‌ی جعلی X-VPN باشید
محققان شرکت «سایدرز» (Cyderes) کمپینی فعال را شناسایی کرده‌اند که در آن نسخه‌های جعلی چند برنامه محبوب برای انتشار بدافزار استفاده شده‌اند. یکی از مهم‌ترین نمونه‌ها، نسخه جعلی اپلیکیشن «ایکس وی‌پی‌ان» (X-VPN) است که برای نصب بدافزاری به نام STX RAT روی سیستم قربانیان استفاده شده است. این بدافزار می‌تواند رمزهای ذخیره‌شده، نشست‌های فعال و اطلاعات سیستم را سرقت کند و به مهاجم امکان اجرای دستور از راه دور بدهد.
در این حمله سرویس ایکس وی‌پی‌ان هک نشده و کانال‌های رسمی دانلود این برنامه سالم هستند. خطر اصلی متوجه کاربرانی است که نسخه آلوده را از منابع غیررسمی (در این مورد، یک مخزن ناشناس در سرویس Bitbucket) دانلود کرده‌اند. در پاسخ به این تهدید، ایکس وی‌پی‌ان به‌سرعت آپدیت نسخه ۷۷.۵.۳ ویندوز را با کنترل‌های سخت‌گیرانه‌تر منتشر کرد.
➕
نوشدارو پلاس: این هشدار مشخصاً به نسخه ویندوز X-VPN مربوط است، آن هم زمانی که کاربر نسخه جعلی و دست‌کاری‌شده را از منابع غیررسمی دانلود کرده باشد. طبق اعلام X-VPN، نسخه‌های رسمی دریافت‌شده از وب‌سایت X-VPN یا Microsoft Store تحت تأثیر این سناریو نیستند.
▪️
روش زیرکانه هکرها برای اجرای حمله
این کمپین ابتدا با نسخه‌های جعلی برنامه‌هایی مانند «بایننس» (Binance)، «بای‌بیت» (Bybit)، متاتریدر ۵ (MetaTrader 5) و کیف پول اکسودوس (Exodus)، معامله‌گران را هدف قرار داد. آن‌ها حتی به سراغ پلتفرم بازی استیم نیز رفتند و در نهایت تمرکز خود را روی کاربرانی گذاشتند که از ابزار تغییر آی‌پی ایکس وی‌پی‌ان برای حفظ حریم خصوصی بهره می‌برند.
💡
نکته: بد نیست بدانید شرکت Kaspersky (کسپرسکی) پیش‌تر متوجه شده بود که همین بدافزار با نفوذ به سایت CPUID، بیش از ۱۵۰ قربانی را در صنایع و کشورهای مختلف آلوده کرده بود.
بر اساس یافته‌های شرکت سایدرز، مهاجمان در فایل نصبی اپ‌های معتبر یک فایل مخرب به نام CRYPTBASE.dll جاسازی می‌کنند؛ تکنیکی که به آن «بارگذاری جانبی» (DLL Sideloading) می‌گویند.
به دلیل ساختار سیستم‌عامل ویندوز، فرایند نصب برنامه در ظاهر کاملاً عادی پیش می‌رود، اما فایل پنهان‌شده، بدافزار را مستقیماً به حافظه دستگاه تزریق می‌کند تا آنتی‌ویروس‌ها متوجه ردپای آن نشوند. پس از فعال‌سازی، بدافزار می‌تواند ارتباطات خود را در قالب ترافیک عادی و قفل‌گذاری‌شده وب پنهان سازد.
▪️
چطور قربانی برنامه‌های جعلی نشویم؟
دفاع در برابر این نوع حملات بسیار ساده است و نیازی به دانش فنی ندارد:
• دانلود از منابع رسمی: برنامه‌ها را فقط از وب‌سایت اصلی شرکت یا فروشگاه‌های رسمی دانلود کنید. این هشدار برای ما کاربران ایرانی که اغلب ناچار به دانلود از منابع واسطه هستیم، اهمیتی دوچندان دارد.
• تایپ مستقیم آدرس: برای جلوگیری از ورود به سایت‌های مشابه و جعلی، آدرس را مستقیم تایپ کنید و روی تبلیغات کلیک نکنید.
• استفاده از نرم‌افزارهای امنیتی: داشتن یک آنتی‌ویروس قدرتمند و به‌روز در کنار رعایت اصول دانلود امن، لایه محافظتی محکمی ایجاد می‌کند.
اگر گمان می‌کنید نسخه جعلی را نصب کرده‌اید، فرض را بر لو رفتن اطلاعاتتان بگذارید. فوراً رمزهای عبور خود را از یک دستگاه امن تغییر دهید، از حساب‌ها خارج شده و احراز هویت دومرحله‌ای را فعال کنید.
✍️
یونس مرادی(نوشدارو)</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/MatinSenPaii/3804" target="_blank">📅 21:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3803">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p-eXjSPX_HLMmvAtZPqcNyMwOLEdu3Kb2jEdFPJ2hqh2w5Hz-RdbdwNvjQ0JpeAxTWpX-1E0paVdYH4KkC43Rn8tMmRmZ1Cc0tRfMTpFB7L4nyTudvZ8Gq5HBiA0CzNdN4FAT6rlDP20MPaMmcfIsqztcMMQC5faLW-5ihssrQxMNkPVacKi9iDp7Bk4SvULlH5DmNSOHL-vN7JLp_cM_-MZ1Ejh8b353xvjBtb6lJSmOWCThgqpt_2A2JvHg6d1BzlGxFKL5cRhq-kf-bif8ROczVVzfxq_RECV5A3wuHeJbh3YpWNlzgO47yFoxArrqs7gWrkkr8nxaf3sUmRQ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏یه نکته‌ی جالب از کنفرانس WWDC اپل!
توی ویدیو هر بار که کلمه سیری گفته می‌شد فرکانس‌های ۳، ۴، ۵ و ۶ کیلوهرتز صدا رو کات می‌کردن. چرا؟
برای اینکه وقتی دارید ویدیو رو می‌بینید، سیری توی دیوایس‌های اطراف شما بی‌دلیل بیدار نشه.
✍️
Behrad Javed
منبع</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/MatinSenPaii/3803" target="_blank">📅 20:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3802">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اگر از
http://Netlen.com.tr
بخرید، دامنه یه دلاری هم می‌تونید بگیرید و با یه سرور ۳ دلاری و کارمزد، کلا میشه ۴.۵ دلار
یعنی کلا ۸۰۰ هزار تومن. دامنه یه ساله هست، سرور یه ماهه. یعنی ماهیانه ۶۰۰ هزار تومن تقریبا. ۵ نفر باشید میشه ماهی ۱۲۰
باز هم خود دانید</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/MatinSenPaii/3802" target="_blank">📅 20:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3801">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ببینید واقعا درک می‌کنم که ۶ دلار هزینه سرور و دامنه براتون زیاده، اما اگر سه چهار نفر با هم بگیرید بهتون فشار نمیاد. همه هم می‌تونید استفاده کنید
برای من سود و ضرری نداره صرفا می‌خوام بدونید که با نفری ۱۵۰-۲۰۰ میتونید راهش بندازید</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/MatinSenPaii/3801" target="_blank">📅 19:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3800">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-poll">
<h4>📊 میتونم بپرسم چرا هنوز راه ننداختین؟</h4>
<ul>
<li>✓ هزینش زیاد بود واسم</li>
<li>✓ آموزش پیچیده بود واسم</li>
<li>✓ حوصله‌ام نشد و بعد از قطعی مغزم نیاز به استراحت داشت</li>
</ul>
</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/MatinSenPaii/3800" target="_blank">📅 18:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3799">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اینطور که من می‌بینم، قطعی در پیش داریم به زودی</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/MatinSenPaii/3799" target="_blank">📅 17:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3798">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تمام آموزش‌های مبنی بر اینترنت آزاد که من توی کانال یوتوبم منتشر کردم به علاوه‌ی توضیحات و اینکه توی چه شرایطی به چه دردی می‌خورن. از بالا به پایین، برای شرایط سخت‌تر معرفی می‌شن تا شرایط خاموشی کامل:  1- متد Paqet، ویژه‌ی شرایط الآن(کلودفلر و اینترنت بین‌الملل…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/MatinSenPaii/3798" target="_blank">📅 17:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3797">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اینطور که من می‌بینم، قطعی در پیش داریم به زودی</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/MatinSenPaii/3797" target="_blank">📅 17:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3796">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-poll">
<h4>📊 آیا سرور MasterDNS راه انداختید برای خودتون و خانوادتون؟</h4>
<ul>
<li>✓ آری👍</li>
<li>✓ خیر👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/MatinSenPaii/3796" target="_blank">📅 17:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3794">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هرچی کانفیگ مرده بود با این تنظیمات واسم زنده شد. توضیحاتش رو هم میدم خدمتتون که هر کدوم چیه و Mux رو خاموش بذارید</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/MatinSenPaii/3794" target="_blank">📅 16:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3793">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RSmz3oD_yTI4e9jC9W0HHF56okPTEMzcKfvdHTf437ZBQJmS_Sx1HOkWAI_7hKk0OpZNcM7kqwA-RudP9sjTk5G-OKHShN2Lk2KZ4Qty21psvnQRSaqr7X0QX7YQ5Kedv5j5seMqaL8epRPbKkeaVKy3rUnE5QuD3Uxp8-WK1h7ptAGOQ1veeI7w409zeP70B8OgnoMgngdxCkvm_DAhi94tH87z6fJMfxMruqEj_MimHue9DB5b77mbW6gbwUKiojD7mto0k2MVwlqIi_8ukYp3GqD4KYwL7V_mzOW3Y3rNtbcbeKvpVxWvvgS-6G5BkWjVEPUPb5_Eho6ViQOahA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی کانفیگ مرده بود با این تنظیمات واسم زنده شد.
توضیحاتش رو هم میدم خدمتتون که هر کدوم چیه
و Mux رو خاموش بذارید</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/MatinSenPaii/3793" target="_blank">📅 15:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3789">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lm7weuE6U5TZIfy_e4G0knkGFjENA7WHnmSb_L-b19E7w1xQ3Yx2jKcsOPAP8Dgwoi5g7SAGf3tU5jpATxPjwYgO1MJiqmvPa40Kxz0Xxf7LKYz0Tqv2tNgp6_gFGe_p1I7WhRSAvwHkRVGOzSCijhuDq4DXlJ5uHQZRdlc_xnHIEirV9BRq8xAOucgCG_UCMNancRoeoPfG2tbOh3NbPY3HAdJFPLATtqqxlxhqm_9BcaAXro75gV2WUIiNrQTl91PICukaM7bEQCNCf6bCo4AVjWD-sE3g7HfKbXRPIKJmHx-gCdPKW25ztU2iQ8gR0Iw0GGrcvHDTOhdXH2Vzdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iN-U1RDEXaqXENmWItnE0JacawtbSB-O3RePI36dH0lLJQYPsgBl0AGsQ6bJgh8qoGc-gPod1b_QzGmVutjsT1yHtvYCWplR3SGFP4dY-S1SvvUv8qEXA_GBXFKsTY44qFgQZOapSLts1Yn3gkKHI2ez5Cfc53gYyhPH0weuKha-1lfV2WfMc5ig8ZVsP46d7I5iY3NDiOvmPcBFq0AEBK6jZdTX6-ejb2L7WBDGop-NDnzvuU33hNvTtFbomRmLt0nYVFTd50I3rnW7vI-mK1phnUbu817Y35aHvLCXhzyJkngegX_Ydur2ItXNkIl7tvqdp4dS9PcsHeqCUcpiEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PdGMyD4bOHxYaIGv8s95fa_TX2QeMweMKHjXCQGiIDc_b2whYE-5jEWlXshac0EM4XGz4OP-bZwn3D_RWxjvnk1QxRH2WD1yaRqLmTLaAHqYVdMrZWH27Of-sIQKBJVyO6FZebxkilFqFZXoT8ZVSJzdvAVN8okqKXajitbpMlTE8pK3v7FKJUw5wnuYVOD4tnbiZCYcvg_tjeybBbRm27I9mM_AvlPD8vgWe7aKyjw8sLwmr8FzaZYhutok9qslb5_5RhWFX98p5kvY3d2yxqKTR0Td7J-qCC1puGFuPTmW8cGJpCQLk5srHXnUbSkXTDufZe0s27XwpRBjr2v8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eXFfRwmlxJF7rP6g-2cqNEFWOWJZduAapj95qnGVRk_jjgrWQhNLv8GUZi-WgH5IQgBFehgmDQggp_7--h7h8EPsVnSFIr-LIEX6_qo8Ixbcg7TzTkB9FgncjTFZrX1QYQ6CuzOHHk66HhOg7jVEOHfAq5yn05nHZuErJA-wSTP376JHPwzPsTmXgBjxvwgt0r_ypDHe3ni841oMGeTpMbY4-dUCyKKlzvKATmvNEXqUvChkUv_nqRpqLixTpS0_0stEztmqb92t_3-sgimtaY9V2b94AB8x43Hty2zDF2PeLiUaJAL-qoFxB4Dr7xF0xBtZGMDxx_odLlASoiTKRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش فعالسازی Fragment توی اپلیکیشن MahsaNG برای رفع مشکل سرعت آپلود و محدودیت اتصال توی برخی نقاط
روی Auto بذارید فعلا، من در ادامه واستون یه سری تنظیمات پیش‌فرض می‌ذارم که تست کنید روی اینترنتتون
اگر الان کانفیگ واستون با سرعت خوبی وصله، نیازی به فعال کردن Fragment ندارید. چون سرعت کلی رو پایین میاره</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/MatinSenPaii/3789" target="_blank">📅 13:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3788">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ما آخر نفهمیدیم جنگ شد یا نشد</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/MatinSenPaii/3788" target="_blank">📅 09:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3784">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">امیدوارم
WhiteDNS
ستاپ کرده باشید. برای اتصال توی شرایط جنگ
دیگه حوصله‌ی اصرار نیست</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/MatinSenPaii/3784" target="_blank">📅 01:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3782">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اگر خواستید مفهوم فیلترینگ منطقه‌ای رو بفهمید، سوار اتوبوس بشید و از تهران برید خوزستان. به هر شهری می‌رسید آیپی تمیزهاتون از کار میفتن و باید دوباره اسکن کنید. به استان خوزستان که می‌رسید، گوشی تبدیل به یه پاره آجر بی‌مصرف میشه و فقط می‌تونید باهاش زنگ بزنید
😂</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/MatinSenPaii/3782" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3781">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uszwfsrjlpSs_iZwyqnWmLj2Q1AtfWgmH5kH9uK0fDpn54fQLDiSME28YlNSiYM_wmJuqff-N6SlvV-jiNQzMVLxqfmHDWOw4e-GRNHUhhvdlpRmCu09diPPU7fLWa5Aa5koBa8DCiYY-B82Qjm3ih5TZ8L5TPZRmHMXHtpoOn-4POIj7tqttVJDYQ66QvXxyIQYgCKsTHLhVA6Gw-sMxSq9mPwqRjm0hZFM5PNgLA28PNVFN1Nj5FVWOJrKDGWohkMcdAnPyA_sfsGuuY5JVyi7o5ZplIH1SFSq2G_1naVFJd7gxXnHFW5aWeFJ2bcPdsef350gnCW-MXKA0vqs6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏وقتشه یه سری حقایق راجب بورسیه MEXT ژاپن بگم.
حالم از این پوسترا مخصوصا راجب بورسیه‌ی ژاپن به هم می‌خوره.
واقعیت:
۱- از چندین هزار متقاضی، سالانه زیر ۵۰ نفر(متغیر) مجموعا از تمام مقاطع برگزیده میشن که اونم کاملا شانسیه.
۲- انتخاب شدن شما تماما به نیاز ژاپن بستگی داره و اصلا هم اعلام نمی‌کنن که ما به فلان رشته نیاز داریم. ممکنه شما تمام شرایط عالی رو داشته باشی با بالاترین نمره، اما «امسال ژاپن به رشته شما نیاز نداشته باشه»(مقطع ارشد و دکتری) و این رو به صورت مبهم فقط بهتون میگن که شما رد شدید! یعنی هیچ دلیلی برای رد شدنتون بهتون نمیدن توی هیچ مقطعی. شخص A با دانش نزدیک به صفر بدون بلد بودن انگلیسی یا ژاپنی قبول میشه چون ژاپن این رشته رو نیاز داره، شخص B بدون توضیح رد میشه با اینکه دانش و علم خیلی بالایی داره یا حتی مدرک زبان ژاپنی داره، چون به رشته‌اش نیاز ندارن. و فقط میگن رد شدی بدون توضیح.
۳- روند غربالگری به شدت غیراستاندارد، و رد شدن توی هر مرحله بدون توضیح هست(سه مرحله داره شامل ارسال مدارک و آزمون کتبی و مصاحبه که هرجا رد شدید، علتی نمیگن)
۴- ثبت نام برخلاف به روز بودن خود کشور ژاپن، به صورت کاملا سنتی و با پست کردن مدرک کاغذی برای سفارت توی یه فرآیند بسیار زمان‌بر و استرس‌زا(نکنه فلان چیز رو یادم رفته باشه) و هزارتا دنگ و فنگ انجام میشه. همه چیز کاغذی. همه‌چیز. یعنی حتی زحمت نمی‌دن به خودشون کد ملی شما رو وارد کنن اطلاعاتتون رو بگیرن. و توی همه‌ی ۱۵-۲۰ تا مدرکی هم که می‌خوان، یه نقطه اگر اشتباه باشه رد می‌شید توی مرحله‌ی اول. که باز هم توضیحی نمی‌دن بهتون که چرا رد شدید. صرفا میگن نقص مدارک
۵- شما ممکنه تمام تلاشتون رو بکنید، همه‌ی مراحل رو قبول بشید، اما در نهایت ژاپن توی اون سال Mext رو برای ایران کنسل کنه!! بله درست شنیدید. پارسال به خاطر جنگ ۱۲ روزه، ژاپن بورسیه‌اش رو برای ایران لغو کرد(
🤣
🤣
🤣
) صرفا چون تایم آزمونش جنگ شد. به تعویق هم ننداخت. لغو کرد. امسال هم همین شد دقیقا و به دلیل وضعیت کشور، لغو کرد. و تمام کسایی که پارسال و امسال هدفشون رو گذاشته بودن Mext، گند خورد به زندگیشون.
خلاصه‌ی کلام اینکه برای بورسیه تمرکزتون رو روی ژاپن به تنهایی نذارید و چندین تا کشور زیر نظرتون باشه</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/MatinSenPaii/3781" target="_blank">📅 00:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3780">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bZoBSP-IPdRUFIRMBPGdRy2lVUfPX5qUEpsYQB8Lrhg_SQ56hJ2U09nPTGjh7t8_HVhFew9b0I-EKoRD2GD-9_C6jC4FoAijs0Wopt6lsT_07srwwcYDD5-gQIhLtV5r-oEPdEjHJ3v0jSyN3p9FFxsRliv2Myrm4U_qprMynEtSkitAov38HWKWgP2MRbGrJ3iubitZWGffDhdQJNi-EgazFh1_QKEksMcZmAkDF4DHUPedYWh3C7tpQZiLMI4vUSPiQFn_SMTnKg_mtReK95GW5gJpD-lVf50hSr50qtooW8g0X0oDZBhn-rL_q7elr3XpbmBr21EexzqkW6XoiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
پروژه‌ی FreeLLMAPI — یه پروکسی OpenAI-compatible فوق‌العاده‌ست که ۱۶ تا از بهترین ارائه‌دهنده‌های LLM(مدل‌های زبانی بزرگ. همون هوش مصنوعی خودمون) رایگان رو روی هم جمع کرده!
تقریباً ۱٫۷ میلیارد توکن توی هر ماه ظرفیت inference (از Google Gemini، Groq، Mistral، Cerebras، OpenRouter، GitHub Models، Cloudflare، NVIDIA، HuggingFace و ... + هر endpoint سفارشی مثل Ollama، vLLM، LM Studio و غیره) می‌ده.
ویژگی‌های اصلی:
🔤
یه endpoint واحد (/v1/chat/completions) برای همه‌چی
🔤
روتینگ هوشمند + failover خودکار (اگر یه کلید به rate limit خورد، سریع میره سراغ بعدی)
🔤
مدیریت دقیق quota هر api key تا زیر حد استفاده‌ی رایگان بمونیم
🔤
کلیدها به صورت رمزنگاری‌شده ذخیره میشن
🔤
داشبورد باحال برای مدیریت api key
🔤
نصب خیلی راحت با Docker
در واقع همه free tierهای پراکنده رو تبدیل کرده به یه LLM قدرتمند و همیشه در دسترس، بدون اینکه مجبور بشی با کلی SDK و rate limit جداگانه کلنجار بری.
بهترین‌ها برای کدنویسی (بر اساس این پروژه و لیست هوش مصنوعی‌ها) عمدتاً DeepSeek V4 Pro، Qwen3-Coder سری (مخصوصاً Qwen3-Coder Next و 480B) و Codestral/Devstral هستن.
⚡️
لینک پروژه:
https://github.com/tashfeenahmed/freellmapi
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/MatinSenPaii/3780" target="_blank">📅 23:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3779">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">من خودم با Hiddify راحتترم برای ساب، از اون استفاده میکنم کلا(با نت H+ الان دارم این پست رو می‌ذارم با همین ساب) اگر پینگ نداد، توی تنظیمات Tls Fragment رو روشن کنید</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/MatinSenPaii/3779" target="_blank">📅 22:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3777">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i4MImJTGMuED3k2NxPphBFucEfgUm41tCpa80sPO1jsyev6tDC8KqkqaqUTo96eBW7W7djNRYxPUmWzaRhv1kKfyOv18HorM2e1GAcq_vKuT-sIqW3NUOtGtg1JSAZDoi5oDNqua8GgcbhQX7FKPC4VuTCHW9ZGCkmiQISD_y-dT_B64RyLfDH1MyGCYnkzXDUYxxOKE_pB9TSnECHJLe8uKyLkHw_uHhAaacKGw1DgsPG_BjdCt7Mvk7jlhcs9c5YQVrZk0JM4uLFcMBsw9tLhACESmAXtxVxQ0OCHPlU4iJ974Eqn3zyulcRXxSY02gRD0wX5Kk-xZ91ROFis4jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eTIZT1sVz7HP0qf_UfE0TrL-cn6A2qd7tRWzxhfJytGQ9q6Uy1iV2IdYJo-gpFiRSEzpztjL8Qu0xXXQYcMNft02wcNCW8lTjuXoX0D5QBK2cz2OG-7UP5rPCrpm4UNHGwlwqWnwJlPhBU9OLbFmhrx2uQwPI4RT1V57mPE2uFhlJ3VVd8M1qPghmXbFVh3Fil9nOBHWlbEZb-ouImC1pw2jqmi-LZk73_1-n4D28HL9KEmEo33lYNKzDtxc75o8Ij3V35JjUONtkUJkcILdZzj-5fHG_7REWwdqXBkOWdpE0hgoJengxuE41M2aCyF6XOZv4X1CJj8n93ntZEL65Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بچه‌های WhiteDNS دارن رو یه چیزی کار می‌کنن که شاهکاره ایده‌اش
(عاشق UI اولیه‌ی اپلیکیشنم
😂
)</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/MatinSenPaii/3777" target="_blank">📅 21:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3776">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NeSaYR1d3eqnFXmva-aDnDJ7_SK4Mo1nB1o_dYvBPSKpviKWxI6a_7OugKfJEKhuz3v6g71RDDT0Zz9H4CHhFHlsMMSfDTl1vHhAFLlahUkqle75-_hqbb4lLC316-dKF6B7meWYpgatgk8ApC98Ewfl0Junw1xTTh4ojgKv3asdQJhgpaqgsxf8e_Zz6XOtH1geFkezdL2OI08PGrFWh5ziMNqmUxAMGFIBICiD03p0zHUHznpk5JmqLBvnmOgjnJHAkN3-KtHYZbHBNCc7dwsFxHj3FV64yoUpySCzD9HZuCigNuMuRcacwqD4AYAWnmQY26eJoh5Cy_kCgpPPRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک هنوز جوهر Opus 4.8 خشک نشده بود، مدل جدید Fable 5 رو به عنوان قوی‌ترین مدل عمومی Claude معرفی کرد!  این مدل توی برنامه‌نویسی، تحقیق و همینطور تحلیل تصویر عالی‌ترینه؛ هرچقدر کارمون پیچیده‌تر بشه، برتریش نسبت به مدل‌های دیگه بیشتر و بیشتر مشخص می‌شه.…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/MatinSenPaii/3776" target="_blank">📅 19:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3775">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79adfc024d.mp4?token=VXGQ8EOFZa_9PnrdrGHW2LUFSXfCVXgG32i1svXHQVgxdTyrg9JeuK-8sRd75oNlcFZoUSS6UufaZlyS4x3rpq_B6fWSpsFtXfDnbeKD_mdsooI_mILHnVTHD2LyRfbOGvYYfeHI9p_FT6L4USSonqnzc35t34Q_WtPdUrdC6Hw0gLdbkztRZ2f_5793_fuMDleClEpGs77lJLW14HdiuE4__xh-X6WCo_MlcxC-FZv2VNI38mKfaq4eTr2GvmnFWLznxsCVL964uHM3v5eoeNp47K2X83TqLCLcUdV9_KibMipxUGcsV2ygT0eeIQ02FJvX7j4uamse9NBRnvjLkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79adfc024d.mp4?token=VXGQ8EOFZa_9PnrdrGHW2LUFSXfCVXgG32i1svXHQVgxdTyrg9JeuK-8sRd75oNlcFZoUSS6UufaZlyS4x3rpq_B6fWSpsFtXfDnbeKD_mdsooI_mILHnVTHD2LyRfbOGvYYfeHI9p_FT6L4USSonqnzc35t34Q_WtPdUrdC6Hw0gLdbkztRZ2f_5793_fuMDleClEpGs77lJLW14HdiuE4__xh-X6WCo_MlcxC-FZv2VNI38mKfaq4eTr2GvmnFWLznxsCVL964uHM3v5eoeNp47K2X83TqLCLcUdV9_KibMipxUGcsV2ygT0eeIQ02FJvX7j4uamse9NBRnvjLkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آنتروپیک هنوز جوهر Opus 4.8 خشک نشده بود، مدل جدید Fable 5 رو به عنوان قوی‌ترین مدل عمومی Claude معرفی کرد!
این مدل توی برنامه‌نویسی، تحقیق و همینطور تحلیل تصویر عالی‌ترینه؛ هرچقدر کارمون پیچیده‌تر بشه، برتریش نسبت به مدل‌های دیگه بیشتر و بیشتر مشخص می‌شه.
همینطور به دلیل توانایی‌های بالاش، برای موضوعات حساس مثل امنیت سایبری(هک و امنیت)، زیست‌شناسی(شاید تولید سلاح‌های زیستی)، شیمی(شاید تولید مواد مخدر
😂
) و مطالب مشابه، از مدل ضعیف‌تر Opus 4.8 استفاده می‌شه.
همینطور همزمان مدل Mythos 5 هم معرفی شده که یه نسخه از Fable 5 با محدودیت‌های امنیتی کمتره.
فعلاً Mythos 5 فقط در اختیار تیم‌های امنیت سایبری خود آمریکا و زیرساخت‌های حیاتیش هست و ممکنه بعداً برای پژوهش‌های پزشکی و امنیتی به افراد مورد اعتماد بیشتری داده بشه. طبق جدول منتشر شده، Mythos 5 و Fable 5 در بنچمارک‌ها امتیاز بالاتری نسبت به GPT 5.5 و Gemini 3.1 Pro و خود Claude Opus 4.8 کسب کردن</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/MatinSenPaii/3775" target="_blank">📅 18:54 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
