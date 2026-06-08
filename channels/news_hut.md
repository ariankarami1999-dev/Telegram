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
<img src="https://cdn4.telesco.pe/file/qj2z_LIJ9KATlMPj7pry0Pnn1SfbZ2jHkyQxAypfrH6NzFRfQZ4_Jjc2h0AZl9ijfheSneknI7j_VT5lA4lxvzVta0vnSycXceblP6G60uAgKd21SzZpn9k08clo2VqOhfsjQrVLbnstYa4mshxcpwYdfemONtY_t-Txyog0LfRHvUSrJ2p79QUo7TeTEP_IGg1E1Iv4uv-LuS5tX38sv3VDCqoxVSKBpZYLSY2qpnbXslDN_vzVCS5gbH6tSwmoymxInYUdPE7JCutYaqjihcXP_jm51LZOsG06YiiXkYW4F9KjVUTbA5DhgBbLwqvjiOjdHFXLzh7ZHlBRrg1asA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 228K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 21:14:30</div>
<hr>

<div class="tg-post" id="msg-65483">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
سازمان هواپیمایی کشور: حوزه هوایی کشور به وضعیت عادی خود بازگشته است و عملیات پروازی طبق اطلاعیه‌های پروازی صادر شده (NOTAM) از سر گرفته خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/news_hut/65483" target="_blank">📅 20:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65482">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/103c84b28e.mp4?token=H3eySMJY9kf-Xp4IlP9KLJbXLyBMhQ9ttmiQvGbObdYF1m_iVlIuQ-8aYYA_zcomvUmiSaU4Gb5mM5pSPAJ-452_GOBwneLqlYxZ3zb14_-yEYPQ6U1ALNFiHbrJj_lrFhxEtAqHOZkQ323SeAroCpR7-SMIcrWRmk1RXINzficLQcjiEwIWZ2TZ-9zEskFEnPPfc_t2_7ER0-H6ORvdP5YgatSdmMap4TymsTj9D8OyKTQw729vSjGDeI9SL972-v6zw87XXLNKKtJPQiMF8ufZU5L3-EqVAAV6O1xq9A5nRt3A9x9yFD00vB0f1ukXhyv-GklsJ1J0HeoFFuH0tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/103c84b28e.mp4?token=H3eySMJY9kf-Xp4IlP9KLJbXLyBMhQ9ttmiQvGbObdYF1m_iVlIuQ-8aYYA_zcomvUmiSaU4Gb5mM5pSPAJ-452_GOBwneLqlYxZ3zb14_-yEYPQ6U1ALNFiHbrJj_lrFhxEtAqHOZkQ323SeAroCpR7-SMIcrWRmk1RXINzficLQcjiEwIWZ2TZ-9zEskFEnPPfc_t2_7ER0-H6ORvdP5YgatSdmMap4TymsTj9D8OyKTQw729vSjGDeI9SL972-v6zw87XXLNKKtJPQiMF8ufZU5L3-EqVAAV6O1xq9A5nRt3A9x9yFD00vB0f1ukXhyv-GklsJ1J0HeoFFuH0tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فیلمی از کشتی M/T Marivex که امروز صبح گرفته شده، پس از آنکه توسط نیروهای آمریکایی به دلیل ادعای تلاش برای شکستن محاصره دریایی ایالات متحده علیه ایران، از کار افتاده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/news_hut/65482" target="_blank">📅 20:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65481">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwDjw2avPqrTXE5-8i4ThobF_rej6WJvyGVrVKlSjBvHVdZ5QCV420cBaZM8VEWYm8rYwACbtoxSuQEFAAl1b-NTrZ6CtBPX6Mj_P4FdZllph2_hiGpZNxgiHEeKt4V1nIUhb79yp4C5k9EFporxFR7BlSsBCT-14_FfejWucQTG5GfleH7-pYruqA3bluwxB3da15cL-1ahF3HZYspYr0ISPmzJ9dCSAd0qscqoQ81F6ueoPCwDv1zaRM4nbEi9_4fHv6KBvCuS-X82WG0PB2AFBBbNrfx6Qt4W_B8tsu5nvo3T1GmyU2rUacHWts7EeagNZLsUVRX1rk6_HpxprQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
نیروهای ایالات متحده یک نفتکش بدون بار را در خلیج عمان، در 8 ژوئن، پس از اینکه کشتی با تلاش برای حرکت به سمت یک بندر ایرانی، تحریم‌های جاری علیه ایران را نقض کرد، از کار انداختند.
فرماندهی مرکزی ایالات متحده (CENTCOM) کشتی M/T Marivex با پرچو پالائو را زمانی که در حال عبور از آب‌های بین‌المللی در خلیج عمان به سمت ایران بود، از کار انداخت.
یک جنگنده F/A-18 سوپر هورنت از ناو هواپیمابر USS Abraham Lincoln (CVN 72) پس از اینکه خدمه از دستورات نیروهای ایالات متحده اطاعت نکردند، یک مهمات دقیق را به بخش‌های مهندسی و فرماندهی کشتی شلیک کرد.
ماری‌وکس دیگر به سمت ایران حرکت نمی‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/news_hut/65481" target="_blank">📅 20:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65480">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65480" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/news_hut/65480" target="_blank">📅 20:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65479">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONvhrWNAk8sa-RB2kEclmNyU2gE6IX5E6BviLPbz2-gHTOWam6QM_F72_ONcJ8fT5Bueu3NAvJ60wGtjpHsiMAvi6La-luuXEPwNwX8dPLCO2prtYNz43QrEFdwm3GIAbIwu0wmCULU_qlwjQ_kw5iDoZlFq_UsrSY7K0CVIxrgvrWrW5vuDcA-R0Tn4vPZkeK7b5cN5kKdCOnARU3qnIC03k5qUgJhy0W8HdNx60uqajxWwy_hm5OvNegA1xDiBecZq05fwqcc1vJfj0E4CybFF5q0ZgSgn80JxgiWVbOLATjvntznr8jsiMm1fWKbmyQcwrlZlRZEDx9AivzPXSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌇
بونوس‌های شبانه از 1xBet
🌒
هر چهارشنبه و پنج‌شنبه از ساعت ۶ عصر تا ۱۱:۵۹ شب، برای واریزهای 5.50€+، 50 اسپین رایگان در بازی
👑
Crown Coins
👑
اهدا میشه!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/news_hut/65479" target="_blank">📅 20:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65477">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
رادیو ارتش اسرائیل: ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند.
«این حمله گسترده انجام نشد.»
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/65477" target="_blank">📅 20:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65476">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
فیلد مارشال ، محسن رضایی:
ایران از غنی‌سازی کوتاه نمیاد و در موضوع آزاد کردن پول‌های بلوکه‌شده جدیه. اگه مذاکره نتیجه نده، محاصره دریایی رو تحمل نمیکنیم و اقدام نظامی انجام میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/65476" target="_blank">📅 19:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65475">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
ارتش اسرائیل تعدادی از فرماندهان ارشد حماس را ترور کرد
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/65475" target="_blank">📅 19:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65474">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
نتانیاهو:ایران فکر می‌کرد می‌تواند به خاک ما حمله کند و ما واکنش نشان ندهیم، این اتفاق نه رخ داده نه رخ خواهد داد، دست کم تا زمانی که من مسئول باشم
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/65474" target="_blank">📅 19:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65473">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXUcLTtt_6-u1bOwuEmDgqO3Fyr6h3XW-DaeucxiSlUlYfcbJJb-J1aLrQ0lTfHO1A0lvaW9yaul9SItp7Th3YQhJagO5QCm5jo-J7oaAiZTiA6zgdjg5enHRwlnB7Ew7oXAsha6QyizIyeqkM50GH1qlP04DUuwZP2m6VX8xdJbQD7LxKJjrlAc47cpbTt7FWw36Q29VXyvpEEfEbPP9rje6FVzJ9lusPC2oLYYTNyWQHRhfTgZT-CtYr-6phLkxN7_soHE7E7njgx6AHKUuLG7kffVqq9xtw_7MfwSPNvhYa-L--1YUIkswV9ZrWTxyT8NesYPkSb15OgYIa0uCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروی دفاعی اسرائیل (IDF) دستور تخلیه محله زقاق المفدی در صور در جنوب لبنان را صادر کرده و به ساکنان هشدار داده است که فوراً خانه‌های خود را ترک کرده و به شمال رودخانه زهرانی نقل مکان کنند، به دلیل حملات قریب‌الوقوع علیه حزب‌الله.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/65473" target="_blank">📅 19:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65472">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
نتانیاهو:اگر رژیم جمهوری اسلامی اشتباه کند و حملات خود را علیه ما از سر بگیرد، ما به شدت پاسخ خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/65472" target="_blank">📅 19:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65471">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
نتانیاهو در واکنش به اظهارات ترامپ: اسرائیل حق دفاع از خود را دارد
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/65471" target="_blank">📅 19:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65470">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
نتانیاهو:اسرائیل فعلا از حمله به ایران خودداری می‌کند ولی ماموریت ما با حزب الله هنوز تموم نشده
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/65470" target="_blank">📅 19:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65469">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc930bac93.mp4?token=VgKUq8-JYoQlHDlbPT85SSRO7nIx4CgvGgis1gi2fvSe_WWoakMDMIbXbu6AYOKXLNdH4vljthONWeGlhzWACNSHT4zdUmv7_ezO0aIs8Q-XGFS8rf3yBRc8sCDtPHtPb7qk0ZBsdHS8Nit20IL7aaq53x-_MNGBgyH1Cg7znw_I0jH9Oh-WgWv5X3VLLFU97Zx-FOfNzFnDSOtcd2zKDSR4I_asmBZT39KZpzMB9gZocMcvZp0zaiBnitHJnzSL_Wf46Ep01N7_eq10Xnzw_zAili1iF6L77bgdoGPlU1fdKzi7TROk4IaOxvfGlofAee7EJ5Lz1yB-wc_wYtPBvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc930bac93.mp4?token=VgKUq8-JYoQlHDlbPT85SSRO7nIx4CgvGgis1gi2fvSe_WWoakMDMIbXbu6AYOKXLNdH4vljthONWeGlhzWACNSHT4zdUmv7_ezO0aIs8Q-XGFS8rf3yBRc8sCDtPHtPb7qk0ZBsdHS8Nit20IL7aaq53x-_MNGBgyH1Cg7znw_I0jH9Oh-WgWv5X3VLLFU97Zx-FOfNzFnDSOtcd2zKDSR4I_asmBZT39KZpzMB9gZocMcvZp0zaiBnitHJnzSL_Wf46Ep01N7_eq10Xnzw_zAili1iF6L77bgdoGPlU1fdKzi7TROk4IaOxvfGlofAee7EJ5Lz1yB-wc_wYtPBvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو: ایران و حزب‌الله از همیشه ضعیف‌ترند و ما از همیشه قوی‌تر.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/65469" target="_blank">📅 19:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65468">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
نتانیاهو:ایران معادلات را بر ما تحمیل نمی‌کند؛ پس از شلیک حزب‌الله به اسرائیل، به بیروت حمله کردیم؛ پس از حمله ایران به اسرائیل، به مناطق مختلف ایران حمله کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/65468" target="_blank">📅 19:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65467">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
نتانیاهو:نظام ایران پس از پاسخ ما عقب‌نشینی کرد و اگر اشتباهش را تکرار کند با شدت پاسخ خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/65467" target="_blank">📅 19:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65466">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو: تسویه حساب اسرائیل با حزب‌الله با قدرت ادامه پیدا خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/65466" target="_blank">📅 18:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65465">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53d663dc6e.mp4?token=Fu5sprlGXP_NaRYBewypNk_qQYcd8F6_COae3sXkV-nT-c1Sa1niD6J7o2J9wHBxsUHHgCfssDU4-_X3jmsnTISuvML0XoeatwBwohwQ0uKTDOjM8XOvhKPirpgtZkkwDycz-etrqatjENQ128RgVMkIVl6beosFPbMxU-H3LGqSNijOujyY9uXiL7EQhOoccn8NslQuCI-NGoB2nKXC5pwuTm6oXT7Wo0wTEkwPlV4EgzToXSNN-SPENnb6jEj15cyzyRS9188B3ynivPkZYskYxMCgrqATHuGGCCqCf0zSatcD3AD_KbJTiRsGN_KbUPbmAgE_fHPeIuPds3K7FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53d663dc6e.mp4?token=Fu5sprlGXP_NaRYBewypNk_qQYcd8F6_COae3sXkV-nT-c1Sa1niD6J7o2J9wHBxsUHHgCfssDU4-_X3jmsnTISuvML0XoeatwBwohwQ0uKTDOjM8XOvhKPirpgtZkkwDycz-etrqatjENQ128RgVMkIVl6beosFPbMxU-H3LGqSNijOujyY9uXiL7EQhOoccn8NslQuCI-NGoB2nKXC5pwuTm6oXT7Wo0wTEkwPlV4EgzToXSNN-SPENnb6jEj15cyzyRS9188B3ynivPkZYskYxMCgrqATHuGGCCqCf0zSatcD3AD_KbJTiRsGN_KbUPbmAgE_fHPeIuPds3K7FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
سوخت رسان های آمریکا در فرودگاه بن گوریون اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/65465" target="_blank">📅 18:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65464">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
بنیامین نتانیاهو تا دقایقی دیگر سخنرانی بسیار مهمی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/65464" target="_blank">📅 18:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65463">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
وزیر دفاع اسرائیل، ایسرائیل کاتز:
وضعیت در ضاحیه بیروت همانند شهرک‌های شمالی است. هر حمله‌ای به شهرک‌های شمالی منجر به حمله‌ای در ضاحیه خواهد شد. ارتش اسرائیل به عملیات خود در لبنان علیه سازمان تروریستی حزب‌الله ادامه خواهد داد. ما تهدیدات ایران را به‌طور کامل رد می‌کنیم. هر تلاش ایرانی برای پیوند دادن لبنان و ایران و حمله به اسرائیل با نیروی عظیمی مواجه خواهد شد، همان‌طور که دیروز اتفاق افتاد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65463" target="_blank">📅 18:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65462">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3210944dde.mp4?token=LqOyMTmALf683jCigscgJDCu_hQwwxlzyH4ABGsFcmWFGEjmTC6T1iGvuEmZiYzDVC4UlWPu-plU-NuiPKGy4YXOY8osSQkD55ceXX6LNWfI8E2yHUCGerhowC0CcVISWEmeoWcbtOa2j_crnwgAoepJ9x6Oue6zIPWQKrxHCalGFIphzO0ZqcKk70Hg-mon6w2ozwBb9mZQyEtQCsSHEbZxUG0eWb6UqFnz0s88AVqaofwPO9bk6KPISQjC078fYiiKos7bNJjxIDjt1TTwhqlOAe0pUWNOv64Of1k-ccxs24__yLAm0ryPJpYQUK0_7Qomxw_ZV8LRVS3XSQJOsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3210944dde.mp4?token=LqOyMTmALf683jCigscgJDCu_hQwwxlzyH4ABGsFcmWFGEjmTC6T1iGvuEmZiYzDVC4UlWPu-plU-NuiPKGy4YXOY8osSQkD55ceXX6LNWfI8E2yHUCGerhowC0CcVISWEmeoWcbtOa2j_crnwgAoepJ9x6Oue6zIPWQKrxHCalGFIphzO0ZqcKk70Hg-mon6w2ozwBb9mZQyEtQCsSHEbZxUG0eWb6UqFnz0s88AVqaofwPO9bk6KPISQjC078fYiiKos7bNJjxIDjt1TTwhqlOAe0pUWNOv64Of1k-ccxs24__yLAm0ryPJpYQUK0_7Qomxw_ZV8LRVS3XSQJOsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو ای از اصابت پهباد به مواضع گروه های کرد در شمال عراق
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65462" target="_blank">📅 17:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65461">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
اسرائیل هیوم از منابع: هنوز هیچ محدودیتی برای فعالیت ارتش اسرائیل در حومه جنوبی بیروت وجود ندارد
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65461" target="_blank">📅 17:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65460">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc72e760f.mp4?token=HGNaLrWp2NgwV02F3f2xjZU_X8AZgxhSSXKVm1m44YKz871mcs9adVF9l7Rkv-dNbIKxodv5ZLlAtHmmDfycDZMwdrQxQuN5fLSFAfnPkKfAquj6ALhK8-wiTGaCAM7lUA-mStEkCYTCQOnbwudQ6Srqcw-S0mZzwQTQMpXhl1tns_1rDDZ35KqlbYixs1SIE5t1n6zsofbCf0te4fvbhzPGwPQvKVXgd2Fdf9vgIkK-87HwBhMgFzOtv_A4rgu177sRMhn9ITLDLKdqAbJCjPmLr9MFc7zMuY201yOfrd5VqUBXeOOQ9s0iNQO3mGKj67xWVKf-PbHFZy-P7Ehtkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc72e760f.mp4?token=HGNaLrWp2NgwV02F3f2xjZU_X8AZgxhSSXKVm1m44YKz871mcs9adVF9l7Rkv-dNbIKxodv5ZLlAtHmmDfycDZMwdrQxQuN5fLSFAfnPkKfAquj6ALhK8-wiTGaCAM7lUA-mStEkCYTCQOnbwudQ6Srqcw-S0mZzwQTQMpXhl1tns_1rDDZ35KqlbYixs1SIE5t1n6zsofbCf0te4fvbhzPGwPQvKVXgd2Fdf9vgIkK-87HwBhMgFzOtv_A4rgu177sRMhn9ITLDLKdqAbJCjPmLr9MFc7zMuY201yOfrd5VqUBXeOOQ9s0iNQO3mGKj67xWVKf-PbHFZy-P7Ehtkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیویی کوتاه از حملات امروز اسرائیل به اهدافی مشخص شده در ایران
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65460" target="_blank">📅 16:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65459">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnWEQtCdgFYInPfBcemqse7uYgMjeDtWz8XpI3r_XuN2ZuSNV2lqq4RIf78CYFKaJs47Hw3hwKtgp80tUpdvFkmrpyLm33L_2Tp0tJeZOvW30XbRkFcljQJALwJpK4gPAd_ODz-k2w-5p68Ya8BQG612ZrZziLEteemhEU5NjGQNlthq6ISkfdmNVuVn0LO9GzLw8pQvJnqHSAPe6190a2K2sWgwze8di6rDeXlWaUy_U7W3oflBVGfqUkLMlHCMnkv0tGyB94g6b1V7RNyj-64pGCgmIASA9Jv6ujgB8nzYiOr540ykLirMMGhL33eowKR3oQg_OrmTErW0_7lKfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری دیگر از جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65459" target="_blank">📅 15:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65458">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7kjFsOSlvudLjrQRj3O7Q0gJ4178E0E49k1R5uZ8Gou62wUX5LhpgwNLEmBeZvK6xFuQnP9N55CtphDmdvhPmWVDVMvcXOolTeIKutmVpf7GMsDFv7Yh0Gl0lwyAzLuU2ACbvKobFDZZdyzjJLfLFHuPyEM7iqs7GzxtJi9KRsGPeuTTN8huzMExzutiIBj768ooR0_-A2j-we5FucP-p3haTl2XihRXfFKdObmxlR8hmXngy-PaaxFrm6uile0T4DuaIjQ1iPwDN259Ax6w0nZzwdEbnokFNcJIL3SG2umty-mFmssSlGqK8zQIM2p__PCk_NgGilTVG2NbWGHSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش ها حاکی از حملات مجدد اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65458" target="_blank">📅 15:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65457">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMNv4ysBae8bBTI5hjpRR0ty33AXtuxNUtmAfYn40nY4BLIw4edBdJHRZWaBkQL0O2vbTvEVzFNhOCP7j4YvyaG6Cabnmm9QVVTRia_tVstmP5l7xk5rMcNLnc9uP-hvB3qt_BHvB_qNyVaDKvqGALqXbXyIazSAH9M4vLz0PIcxBznj8mNdcGBSUPldpkUgRCqTdD2aA7LZ8E_C6kyfuwl6g5tXOAzOUv_o8ESuKEEyI2JM2KIhz5Hfw96hlxLnv75tCBEy-rR4DrGbhNd7pHTlEFG3sMIXYw_xfWpwuo4Q6c0KMQS_gn4qdZFfiMqvrIYkcPTn4ULJH7wQTn1bHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما پایان درگیری‌های دیشب و صبح امروز رو رسما اعلام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65457" target="_blank">📅 15:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65456">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🇮🇷
فرماندهی قرارگاه خاتم الانبیا:توقف عملیات نیروهای مسلح را اعلام می کند. با تاکید بر اینکه در صورت ادامه حملات و اقدامات تجاوزکارانه از جمله در جنوب لبنان، اقدامات قوی‌تر، خشن‌تر و قاطع‌تر از گذشته در راه است
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65456" target="_blank">📅 15:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65452">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VoltcB2dRwVE0_h56r2I2vudF2mFPSxNUm1pnf00z5syucIxtDMsQoj9p0h7Z190ofC4I4LTV5GITIvfDQp7g5gq0pzsrsd4CmNB4zV2BVNzqKesxtXqhgNLIzNIIo6yiD0fq1C67jno5oylWwGoIkKxilY4RH0dW52GBt-SoWepOxY1iuzQHI3NE-ifRuKMN0zgv4rMbabM4Pcnqzqzk1QaXexdPxYllh842NAD39WOas_xq_xM-oAKNbin_llIgNBCWP67WiwF7T3QfRLWUbedZckgqe9iMvKAx5VCD4SPp_QqG_Jf1dDE_GFONBuceu0bZUS3IQFcqX_l9xiSEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FN22t3xj6yzPBzLB93OhDnAb29rwZmhJMHSB609aXahQ67hG4de6hjQ5SsDI_2PKz3hnD_FU_po2yTUWek7RaWmhJaZjMuGGh3fTTPkDaygcucWxVNr9cJX7Dx034yqZzRRWDyOOd5D0dZ56rdYTnHpzrluOz61T9FOwKONhhPHNHzN2YHEM_HN5BaiR3F85_nsmj_4hxM5PJ5AJTgd6LbJRAQuskBaLnN_ZP17PcKuz2SdpLg11Do1DUCqz3qGG1hhcN5iu8ZhN_VwNJ10J2zgcVWwOsf9g940baFmLvv7F3FdPGZ4jXpJ83uiGmS2FVS23bbLOPV1hSr_jh-k2TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kjAzZ-qn0i08yO5pcXCKk8XPg8r5Hvi_pv0KyncpfSVo1Cw2lOTfwteJZr765samUOlp28LbJOT33v9HoEngquS8UayJS1fD6rSBhzra-6S7mEf4BhJr-Q6Jta0XM4KcplEEi6T0S4hZ3k383U5Mu8RGsM-0w-VZFwWzud4gnpjzsdAXQQ77-91v1Lse85TBUasJqD0Y8tB2ZqucoGl9oQgkNms34Y5hfaLCqVNpZc8gIChC0axfXc09LwQpGbfR0sy9Hs0m1HLM5WFQasCFUUCPQm82ILREBzeZxEe11dA_GaOA7uQLd-LkiS4meGnqxUtlpbAb4Hf13SChB5wGlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0wAoZrZx-rsCyftKRq66dscVN67uix2mmx2xJLcnxkXbybxi2lA0bNfu_eOTafl6cW_fRAATR-nrRhqJqgD1jM8-hMHMkYrQdeC7OhfPj_8QZaNjEqObVnBTEsLk64yxQpkkaw66QuZNgrjC-xEuFFdExD6Vykz6Q9Hf1LpyvORsiZ4nQ2yFBTxQFBBKnm741FGk7qhHe41aGqn3XmBSSM7g3NFlSN4RTWxtB145_0KdmWxouemYacVQZQ9xCB6_nokIq9gfUdZDmOZkD63yFculVqonKSxd0kjF5iqivWfaJxPc5ENpLRZtm2Gzr3uWRaPu9skEGm-rVXD9MKw8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکاس
اسرائیلی
؛ رفته کنار یه پوستر موشک ایرانی که تو اریحا فرو رفته، وایساده و عکس گرفته
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65452" target="_blank">📅 14:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65451">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-text">سایت های شرطبندی به دنبال ترورش هستن ، به عشق مردم داره میگاعشون
⚡
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65451" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65450">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sf7gLoue2fl_hMpIhShAdDhetERg00nT_ylh5E21oeurHPvqK-Kq8_8m6v_Uxo3muWR8Y3yJ8Sevy2mq6P9nSeVEUQrUJFZnXP6bklz0UBCWJrml8Z-0NZEO57ydU4WHSyPyt5VWUq6tBZLAyS6Bx7810K9sFr47hN6QFpfxoaq3Zs_K5j3rIvfadyk97K9lEQfsK_u-AIpJ_Fkpt4Ec73CzDXnICDMnIiocxZ5l5Nb4uqaJvxsgiZfokXnobyI-iAB4_gkGy9hT96d9wnmtwMaNDMEWjjJ9SkK93vIn2Lyehb1v6_aOUiKK277DrSfmnqMZEFjG9uIOXEIHaHqS6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبانی
🆘
کامل در لینک زیر باز شده است، برای دریافت آن کلیک کنید و عضو شوید
👇
👇
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
1 دقیقه لینک را لغو می کنم
❌
❌
❌
سریع بپیوندید
🖱
سریع بپیوندید
🎧
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65450" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65449">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XD8cYoM2OEQ7nlgB0WI-GkTQ65gO-N_aVHncI7c98Bker6RQSOk1hDIHLDzhGPlvOXA4vDqAUTwYFB3qKWtonkPb8Qt83RCNOZsROXMnmjJjjnPvJwsNPkXUc8vQl0z_R5oMmNyFoC73V1zasOyxsHcN3ypo1w3P9OE1C5VGaKllp_em2tVsrLNXPHgM_RUpNl-iz6d75QVeTNANjb_7ZzbVxK4t76s2W0syXmqTLkyrStnJoqch5Aa2hieS9fqzDn3FOhYAVju1GPYbXCf0dTuzBEt6c1jVNBkBzn8_Yb-TJr7i3CHt2Uwcot3Zjxi94G6xyYu8L67_9lHmqM8bBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:هر دو طرف، اسرائیل و ایران، به دنبال برقراری آتش‌بس فوری هستند!
مذاکرات نهایی درباره «صلح» در حال پیشرفت است، مشروط بر اینکه جهل یا حماقت مانع آن نشود.
محاصره با قوت خود باقی خواهد ماند و با قدرت کامل اجرا می‌شود، تا زمانی که «توافق نهایی» حاصل شود.
اوضاع باید سریع پیش برود. از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65449" target="_blank">📅 14:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65448">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
یک کشتی هندی در دریای عمان هدف قرار گرفت و دچار آتش‌سوزی شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65448" target="_blank">📅 13:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65447">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cty0FMP1N6CqCSDjz4dz6Do3tduzTItGQNUypcj7QzwhkTjBLVlmcjtFKlNPE0v_daIrrQ5YEv4jGBYBPzjbevyRdpBklSO3hBTiOXtfxm3t7231glP33mTjhnKE_y8WQ-kc9wMclzRfCTKQykAgy09y8jlZH_ZuCoruZJK3XgfXifjL3f5_fcWbV33ywZ5XS3R19Vs8B9WZqQPE1JvgFFm3FN3tZc0oe-POIuHVjjGg_tC8vmRsemzdLP3xdKASevuwWWg7I46-4gdTLmgBKeTzEtsWNSj2i8WQZra3V-XVT-CVWpwjezi0hokR8VriOY6IkTzWfXjxV_j3OvTkKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
دیلی میل| یک فوتبالیست بین‌المللی متهم شده که در یک هتل پنج‌ستاره در ترکیه تلاش کرده یک دختر ۱۴ ساله بریتانیایی را برای «بغل کردن» به پشت یک پرچین ببرد. پدر این دختر در گفت‌وگو با دیلی‌میل گفت که دخترش پس از این اتفاق دچار وحشت شده و در حالی که اشک می‌ریخته با خانواده تماس گرفته است. این حادثه زمانی رخ داد که او همراه خواهر ۱۰ ساله‌اش کنار استخر بود و والدینش حضور نداشتند. دختر ۱۴ ساله که از دیدن یک چهره مشهور هیجان‌زده شده بود، از بازیکن درخواست عکس کرد. پس از گرفتن عکس، بازیکن تلفن او را گرفت، اطلاعات اینستاگرام خود را وارد کرد و از طریق حساب دختر برای خودش پیام فرستاد تا ارتباط برقرار شود. به گفته دختر، پس از آنکه او سن خود را اعلام کرد، فوتبالیست او را هات خطاب کرد و درخواست بغل کردن داد. وقتی دختر مخالفت کرد، بازیکن اصرار کرد و از او خواست به پشت یک پرچین برود؛ جایی که به گفته او هیچ‌کس نمی‌توانست آن‌ها را ببیند. دختر که ترسیده بود، به او گفت پدرش در راه است. به گفته خانواده، بازیکن پس از شنیدن این موضوع به سمت دیگر استخر رفت و خود را پنهان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65447" target="_blank">📅 13:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65446">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
اخبار جنگو تو چنل دوممون پوشش میدیم عضو باشید
😉
✌🏼
@Futball
@Futball
@Futball
@Futball</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65446" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65445">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAXwReAj-J3hISKx8zTX6T_e9V679knjycTtLyouuE_3CaAzQqNq9O7R8UH-Hc2B7Y_daAaYhRY015rzlJhc6DpBju3tHlpVmvbTBdr9RUzbRpTu96nVkdiZOBur9mjndAWkE1DIQ-FWiUGVmStObr4VN7VAHtLSFF8VFwP9IttK1JnY_qiOoM3-6oxJeNfj5t5TSH7Bt8aoUW4C4jqWdllR_Z2Fzh2WtBBA6twmA3eCXJBqxdlb_VtrsQSK4ZcriH0U3cwIxCqmHhNOSWNAmteQoF64neV7omjJt6qT1fJgLNj3P7ilWxZrQaaeQ8bfTuOqWJgt1sGqz2b_TtLv7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65445" target="_blank">📅 13:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65444">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
مارکو روبیو:فقط کشورهای احمق وقتی به آنها شلیک می‌شود پاسخ نمی‌دهند
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65444" target="_blank">📅 13:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65443">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🇮🇱
منابع اسرائیلی: حملات دیشب و امروز کاملا با اختیار و بدون دخالت نظر آمریکا بوده اما سنتکام در رهگیری موشک‌های ایرانی کمک داده
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65443" target="_blank">📅 12:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65442">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8c5e38e196.mp4?token=lBVHEDHcMKotLLANHAUsuBKqjV75zInL1d2cfzFksy05_T03D8lp1wugs7aDe6wZNwAbq9ie67MI4-eRSZd3SMeK8ndcY9c6UjmYr7-9gSz-iS6q0yyq1Z8tJaVQwNQgEJINnPRyDXlNmgcapgnP6l4F8KYwIoWxn564ZLQAgDg0PjAX7apIn_c8OKbIXklLYBDIWZK_vVG989j5dJ12OIAR1GZjiOtLEdsKK29lPkkKMjlu1c1ylsTPDZbgRFdcOa3ZqkNdOBJbfTrK7wMl0oh83E0qJ5OvhfFCf2Fhn4rtI4Hf-tZ2IH4OKXqTa0UDVvEG6bt3Jatf-tJ3htQgvA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8c5e38e196.mp4?token=lBVHEDHcMKotLLANHAUsuBKqjV75zInL1d2cfzFksy05_T03D8lp1wugs7aDe6wZNwAbq9ie67MI4-eRSZd3SMeK8ndcY9c6UjmYr7-9gSz-iS6q0yyq1Z8tJaVQwNQgEJINnPRyDXlNmgcapgnP6l4F8KYwIoWxn564ZLQAgDg0PjAX7apIn_c8OKbIXklLYBDIWZK_vVG989j5dJ12OIAR1GZjiOtLEdsKK29lPkkKMjlu1c1ylsTPDZbgRFdcOa3ZqkNdOBJbfTrK7wMl0oh83E0qJ5OvhfFCf2Fhn4rtI4Hf-tZ2IH4OKXqTa0UDVvEG6bt3Jatf-tJ3htQgvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
‼️
‼️
‼️
بدون شرح:
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65442" target="_blank">📅 12:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65441">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb70e7631.mp4?token=rHoGH6F9KI7mPsjkWaMvjbX10xQBNOGY0nQ6QkfjtqCfValhLVqry_dCGaZpix9sml5byiFKxc0K4jeDO02OgSqUa51Frc_FH0nDsD_VtS-be6vPS-QOuw8dEcHDf4RDXTqTXrNPYtagHxO61qefE-s1GKuzJQhJbqJv6947JgRMGLSVJfJovzkSMdMpjYJ4NwxFdurzUd77G0XITJG8k8Bz3mpvIy2GtBSdUcbI4EIgJ5KlpaXtz2fV3eqU1bJ-gyPvw4KT0stZIKt0UHXn1snXwRhziXsp85DZqiYK9s7riVpNFzNje0aitFCSczmUO5Z656FaoKDxlJngXjbDw56Cow7V39VPw7-KLDV0QOL2sXxA0Jay6yg3QVSVFf-dp0YFSCHoKnssXiHQjUc8gajaz7WKS0ErYrG8A7OfSgf81G8-RMTdvjCEbaTclf_bhF_XxVKxvrG9m_Tj9tIL8894Sat7IgcPzqb4IrihQPo1bvzaKnB4fxddsfqGb_YeZyvA71TyodSXsW5zdXh9mWGHyu7J3Au070bhD1s1tT5dJWKO8iJOPfOooI6Qdg_0kl92TTYkzboJFUfM3PygF0kS79v5IieU3TWiki_cq4PDXRZwZiqTTHf3gsopYiO4AX1fKm7jo1hufRbVPhR2OJa0pE7HpSRq0j5p1sfpeBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb70e7631.mp4?token=rHoGH6F9KI7mPsjkWaMvjbX10xQBNOGY0nQ6QkfjtqCfValhLVqry_dCGaZpix9sml5byiFKxc0K4jeDO02OgSqUa51Frc_FH0nDsD_VtS-be6vPS-QOuw8dEcHDf4RDXTqTXrNPYtagHxO61qefE-s1GKuzJQhJbqJv6947JgRMGLSVJfJovzkSMdMpjYJ4NwxFdurzUd77G0XITJG8k8Bz3mpvIy2GtBSdUcbI4EIgJ5KlpaXtz2fV3eqU1bJ-gyPvw4KT0stZIKt0UHXn1snXwRhziXsp85DZqiYK9s7riVpNFzNje0aitFCSczmUO5Z656FaoKDxlJngXjbDw56Cow7V39VPw7-KLDV0QOL2sXxA0Jay6yg3QVSVFf-dp0YFSCHoKnssXiHQjUc8gajaz7WKS0ErYrG8A7OfSgf81G8-RMTdvjCEbaTclf_bhF_XxVKxvrG9m_Tj9tIL8894Sat7IgcPzqb4IrihQPo1bvzaKnB4fxddsfqGb_YeZyvA71TyodSXsW5zdXh9mWGHyu7J3Au070bhD1s1tT5dJWKO8iJOPfOooI6Qdg_0kl92TTYkzboJFUfM3PygF0kS79v5IieU3TWiki_cq4PDXRZwZiqTTHf3gsopYiO4AX1fKm7jo1hufRbVPhR2OJa0pE7HpSRq0j5p1sfpeBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
🇮🇷
حمله شدید پزشکیان به رسانه دیکتاتوری جبلی
: صداوسیما هر روز شعار می‌دهد اما باید واقعیت را هم بگوید
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65441" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65440">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65440" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65440" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65439">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doiVNHVm1ByNZAqxFLmCrYgXbLjWdOkcqGrmauxEMGh2Nb6TMLtxMUb0x99jsmyPTCIH-YxC7DebYWn4JEmUtBE2P94LsSRpaxQ-sMnhn7Gv5JgBczd2ewJjs4GJpJ3ArZIrUFnVkp2mQ1sVTAC4fhK4hBXhbQxBoCuTPftPMWGIl8Ue7fnAbwjXTw2QTTLPfJlNfyQEyBSOZbPOpkAsO7z760pQElkZR9HEyXudjtOdoUlO_jSJk4iVvm5HNXpfxyBBazYzlEasxB1vZzCURRvlOi58G7w8NAu9CD-ziQC7-dUs8jLikLMSCJ9o9OY9_i4mNXoP9_S67guxRC5Qyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65439" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65438">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری‌فارس: سپاه دیشب در حملات خودش از آخرین نسل موشک‌های خیبرشکن استفاده کرده و تونسته تلفات خیلی خوبی از دشمن بگیره!
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65438" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65437">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8792984a2f.mov?token=tl7T0cq1VHB3nb81XKFClP0-jR4be1hoSCrftPuX-rBHOzDiTq0dhphA3ivFuqsz2jWLGOCgnDVAvpXqaBy9m5K8E9HtuCHzU2qKdiP-5iq4oxSu-bPljPCQT5fhF5AkDgqOITG7V6BULWKFEHMMOPE88zc_m49LmB3gzi95lmvbO2iR7ZO5gXPWzGjcYkf4ApJk4FvFUJbW01ajHNdssiyb7O9rJmTUyX7EIfKReH0fo0qzfl-_v7b5-Cpl4dxZbze9r13B0gW5bKTh33aPI_gxYsPIOYvH5d3OLxN9N-FXj2nusHrk4CHviFHOv8x6Hgo4DBGc35cDZeZ8hnyIunnKkkHdLPNbLCyu_BVyFR8GpfiQXIVvI6dxFrVlhsUXjKgww6XTJ8yXJbq98uRc4K0gTDaFSRoubLtTfuhWPr5KreodO7r9uFM07jx5zXxu1-vYKLSvbffrb4Yt-jpZCQYWt9JQQQ8ZEacqSGDh0QIsdSXUsOMvW-OkXkf9Hep9fSazjKalWyZxtCoAgaKBtLdbLQKt61JV_DEtiK3IjU_p0EAqsl_nbCTwljDPeKQ_am-DI1tSl39PRCh5-CUJTYtky3ksjvH2lixF0GyJ_hI2vM25xTQCf0TWDL43JZMNgB0rdVkqSKiSSHyRRKoJ2XUGftFjmCCccmu1pcKQVZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8792984a2f.mov?token=tl7T0cq1VHB3nb81XKFClP0-jR4be1hoSCrftPuX-rBHOzDiTq0dhphA3ivFuqsz2jWLGOCgnDVAvpXqaBy9m5K8E9HtuCHzU2qKdiP-5iq4oxSu-bPljPCQT5fhF5AkDgqOITG7V6BULWKFEHMMOPE88zc_m49LmB3gzi95lmvbO2iR7ZO5gXPWzGjcYkf4ApJk4FvFUJbW01ajHNdssiyb7O9rJmTUyX7EIfKReH0fo0qzfl-_v7b5-Cpl4dxZbze9r13B0gW5bKTh33aPI_gxYsPIOYvH5d3OLxN9N-FXj2nusHrk4CHviFHOv8x6Hgo4DBGc35cDZeZ8hnyIunnKkkHdLPNbLCyu_BVyFR8GpfiQXIVvI6dxFrVlhsUXjKgww6XTJ8yXJbq98uRc4K0gTDaFSRoubLtTfuhWPr5KreodO7r9uFM07jx5zXxu1-vYKLSvbffrb4Yt-jpZCQYWt9JQQQ8ZEacqSGDh0QIsdSXUsOMvW-OkXkf9Hep9fSazjKalWyZxtCoAgaKBtLdbLQKt61JV_DEtiK3IjU_p0EAqsl_nbCTwljDPeKQ_am-DI1tSl39PRCh5-CUJTYtky3ksjvH2lixF0GyJ_hI2vM25xTQCf0TWDL43JZMNgB0rdVkqSKiSSHyRRKoJ2XUGftFjmCCccmu1pcKQVZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فیلم دوربین مداربسته از لحظه حمله‌ور شدن الهه و شهربانو منصوریان به حوزه ریاست فدراسیون ووشو و شکستن دوربین مداربسته و درب اتاق رئیس برای ورود به اتاق ریاست
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65437" target="_blank">📅 12:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65436">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b744fd7fb3.mp4?token=UGNRbp4DKgZd6dLxclt179HmSgzw-xpQLQsE4UhsPN4L5H3MhxO3jKVBjxYzu03EZSsLgblAxFX87srGpOhYGtXSgMhWTZijvFSehk1rpxcd0SIXVVZJfjbsUnKMUtwkuLGvbazk5vxMBajtfE2ai2VCuiAE-FrdjbYAX6SBKbX7pz4rZuEpS-J0xtxznMkkNZZeSXe-Q0V3YsPh4ETlY8bq9E8bFvxwu2-eLFiTaouBvzc7K5fh49ArTR60nw4gs2ER-ixqBkqc23DsCUQtufPnQOS6AdhmLHYcAMYXbJkOaEz-xyvBjd3yBleXXi2Pjhu0MI4JFt-TsuUXJt3dow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b744fd7fb3.mp4?token=UGNRbp4DKgZd6dLxclt179HmSgzw-xpQLQsE4UhsPN4L5H3MhxO3jKVBjxYzu03EZSsLgblAxFX87srGpOhYGtXSgMhWTZijvFSehk1rpxcd0SIXVVZJfjbsUnKMUtwkuLGvbazk5vxMBajtfE2ai2VCuiAE-FrdjbYAX6SBKbX7pz4rZuEpS-J0xtxznMkkNZZeSXe-Q0V3YsPh4ETlY8bq9E8bFvxwu2-eLFiTaouBvzc7K5fh49ArTR60nw4gs2ER-ixqBkqc23DsCUQtufPnQOS6AdhmLHYcAMYXbJkOaEz-xyvBjd3yBleXXi2Pjhu0MI4JFt-TsuUXJt3dow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو منتشر شده منتسب به آسمان یزد
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65436" target="_blank">📅 12:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65435">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-Y9YtgZe4mJlvb8JtTeH8SaO2BzgUL6USRwpyOE3ZAnMj8A-0kxHLC7e7F5O0tBpg4-IWbkHIHKe_ivUV2v8s72kO-ytQuJwmb2THua-i3I8Km98wE_4MSgxg9E5OB8QFrC2fjevcsGk7jcsftOe1aJJVU5nHxBd8QOgVo27Ok4bijOd62BjQQV3FZ_TF-JMs2kyZyH8JWlBkRVlPgi0RUkhCDlSC-quOq8-rFcU4LRnJ2xAyH8RmLHJU2v1wKiHVJNdUggQrhSjqjBWS9aoCTzfd61LMwC8mCVIeEDzah5pBKSdwXA_fVFgxO8kKw3_y8wj5EKMXJPaIpmk-upiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
مشاهده ستون‌های دود از شرق تهران
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65435" target="_blank">📅 12:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65434">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
گزارش رسانه های اسرائیلی از هدف قرار گرفتن فرودگاه شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65434" target="_blank">📅 12:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65433">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ اسرائیل: حمله به‌ نقاط مختلف ایران را آغاز کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/news_hut/65433" target="_blank">📅 11:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65432">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
صدای انفجار در اصفهان و همدان
@News_Hut</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/65432" target="_blank">📅 11:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65431">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
گزارش ها از حمله به دانشگاه هوا فضای عاشورا
@News_Hut</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/news_hut/65431" target="_blank">📅 11:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65430">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
غرب تهران و کرج گزارش انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/news_hut/65430" target="_blank">📅 11:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65429">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
صدای انفجار های شدید در تهران
@News_Hut</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/news_hut/65429" target="_blank">📅 11:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65428">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8514d8db20.mp4?token=cD6TkLreM_wy_CQGes_lpDXAfFHeX6Jt-fvUMsBQ5yW0lxFBhcOoZh5rr46lC40y5I5vcTsCZ827mCKND00ft-sUJWqrNKYhOzTX_XEh7LboTSwtdGZ_fdzlp11MNp9apc-5G_qOhe5rrSOqIHPU-mVCjL9qR3CNgR6iMkKUrzpQtKZrmEfCrX6NNjLkYCBmpGdaWqESlVjkRxJCWQrkHNLMvIZ0eBy48CSEJzuYot0b5FDoFLsgwA9e5L0MeSf_tAZ5EXuvfPkTCKCTMaljBeKSh6QItlQ-MdUqH5x4y6qxGYBWYY3orV8wC2ta0rUIXD9TgBkfbIV3MrjbiK2CJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8514d8db20.mp4?token=cD6TkLreM_wy_CQGes_lpDXAfFHeX6Jt-fvUMsBQ5yW0lxFBhcOoZh5rr46lC40y5I5vcTsCZ827mCKND00ft-sUJWqrNKYhOzTX_XEh7LboTSwtdGZ_fdzlp11MNp9apc-5G_qOhe5rrSOqIHPU-mVCjL9qR3CNgR6iMkKUrzpQtKZrmEfCrX6NNjLkYCBmpGdaWqESlVjkRxJCWQrkHNLMvIZ0eBy48CSEJzuYot0b5FDoFLsgwA9e5L0MeSf_tAZ5EXuvfPkTCKCTMaljBeKSh6QItlQ-MdUqH5x4y6qxGYBWYY3orV8wC2ta0rUIXD9TgBkfbIV3MrjbiK2CJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
در ادامه اوضاع بگایی آسیا، تو فیلیپین زلزله 8.2 ریشتری اومده و تلفات نسبتا زیادی تا الان داده!!
@News_Hut</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/news_hut/65428" target="_blank">📅 10:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65427">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b691d50ba0.mp4?token=TNBOQLvNg5Mo9ZhSM-p5tR7PswPpuJyfQY-D4DYZlZ1Yh7w6MU3hSJW_Mg9OvoPqaLM-hIaX9ETW-SDYkI0YyqARIZwqU-AJXgmf8kkh5lwm7UltSHNueuncalZ0VOD_f0d0PCE-ZxchfyoVbJLTTGcXxRNe3tfM_n6hNYVB0t0GYutUap6lRN35oAhHEZ5taFUHHa8nlnzeFOCj4yYOdRI8w0J1y99XKBOKl7jQlg0YIb6K9yn6ZGNqnbXDAkpy-qTyPeIy-yNFHRl5A7dZ27MKX9so07cmEJQaWpnm_fTFT6pW0Jfq6fXeOKWNKgqZRCm3sCrevrCyPA30R4WL-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b691d50ba0.mp4?token=TNBOQLvNg5Mo9ZhSM-p5tR7PswPpuJyfQY-D4DYZlZ1Yh7w6MU3hSJW_Mg9OvoPqaLM-hIaX9ETW-SDYkI0YyqARIZwqU-AJXgmf8kkh5lwm7UltSHNueuncalZ0VOD_f0d0PCE-ZxchfyoVbJLTTGcXxRNe3tfM_n6hNYVB0t0GYutUap6lRN35oAhHEZ5taFUHHa8nlnzeFOCj4yYOdRI8w0J1y99XKBOKl7jQlg0YIb6K9yn6ZGNqnbXDAkpy-qTyPeIy-yNFHRl5A7dZ27MKX9so07cmEJQaWpnm_fTFT6pW0Jfq6fXeOKWNKgqZRCm3sCrevrCyPA30R4WL-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
لحظه اعلام خبر حمله موشکی به اسرائیل و واکنش هواداران جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/news_hut/65427" target="_blank">📅 10:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65426">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
فرودگاه‌های غرب ایران کامل تعطیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65426" target="_blank">📅 10:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65425">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Naery8yJ3pBpo4V1PMByd8lzV9ZHKLPk4VLD0P1EP-Sr2OSvVayeZIdT3CCKJr0UgWiDWHQb1BOZRBzTbZWJkG24amkApND6PScoBfCbvLQ2bQB0ns0AfalVUGwdecNBFIAB_SZ1wzp4x2yD8zXoly1Y5CH3U6GbBBiHoi4_0ctP-EjYUumKSBfA2VFMhjGue9FWQLm9PqyaQLJ-NbFeKc-jgojUKkSw6OJshPBaGaSCyRG2SM0kSo5K_sGd8KZweoJ-v0IBK0sxHDd-_xdydImjOgTI_XStg4rsLVzND-CTPvQz0rlwpZqcmxVMkgmwp_t4rGdrP_Qg5lIbhgJ8Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توییت ایلان ماسک درمورد ایران: « تنگه هرمز به نام اهورا مزدا از زرتشتیان نام گذاری شده »
@News_Hut</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/news_hut/65425" target="_blank">📅 10:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65424">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1O3r7fCv0hbaixXiby-atTC6ni7dg49hKHwJZ_akHTj9FhUwv0PpvVw0h5ZbcvdBRYaSAaf1KYJEpnP29hxsjQfPeQLLPoEYZJzqxvfsI4BiKx3dz__EXdJIC3oyOHpAjsW9OTKCR6RhmnCItwRv_4mXGgZFoFfo4H-zFi_M9aT0IRTziW5L1ei_OUvzfX76ju8Dh1gavk2NHB_P5QwwPmdYHUD6_pMJV0aavXXJ7EMGw8wV9qz7Qd4NIaTk3Q33GpyRUTQoS79XYdgsfIANFi33sMUEb-zgl35dgXPPC10XZCpAXGNuT2IG9lEzvhiyODT6efpLEhjuuhfXiIEBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
حمله موشکی سپاه به مرکز انرژی اسرائیل در حیفا و ناصره
@News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/65424" target="_blank">📅 10:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65423">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56aa95f90.mp4?token=n3h7fGhQbeMWEmPi-auiv9lZ22ryN9qq_mPio4KjSf0wAc-0Q50jebfsi4L9eEQ26gKbst4ZTbcvBI6zLm5Ankb8F49YgwKEUaxNKRt4IcGqtG6KQ4V8H2d9KnEVQBfW01QOGFtWDEJJp6-xQPRD_6S_vWC-FvcxZ_J_HGl7eC4-OWslbKURAd6vI0IbC0dhdcXGgxr8oGYka73hyYB75a6MoWyA0wG82w8RHlaZuE3iysMiNbMpI6WnzpxX0hXf8h_GKrE_MdDEY1ACxCahL4hzzzj4aEtP1NYP_bUM2-lFHcfqrylPTxJ9tuAU1lPoycVUc3j-9Umb5BRnDmYlRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56aa95f90.mp4?token=n3h7fGhQbeMWEmPi-auiv9lZ22ryN9qq_mPio4KjSf0wAc-0Q50jebfsi4L9eEQ26gKbst4ZTbcvBI6zLm5Ankb8F49YgwKEUaxNKRt4IcGqtG6KQ4V8H2d9KnEVQBfW01QOGFtWDEJJp6-xQPRD_6S_vWC-FvcxZ_J_HGl7eC4-OWslbKURAd6vI0IbC0dhdcXGgxr8oGYka73hyYB75a6MoWyA0wG82w8RHlaZuE3iysMiNbMpI6WnzpxX0hXf8h_GKrE_MdDEY1ACxCahL4hzzzj4aEtP1NYP_bUM2-lFHcfqrylPTxJ9tuAU1lPoycVUc3j-9Umb5BRnDmYlRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
تصاویری از پرتاب موشک از ایران لحظاتی پیش
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65423" target="_blank">📅 10:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65422">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
با اعلام انصارالله یمن تنگه باب‌المندب بسته شد
@News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/65422" target="_blank">📅 10:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65421">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
اسرائیل هیوم:
یک پایگاه آمریکایی در عربستان سعودی هدف قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/news_hut/65421" target="_blank">📅 10:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65420">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9d994e5a.mp4?token=i922rPiwQpO4tucuL7wq1HNm-60ntG_zMgOpCBlD4seHPFqlrxyvWL33FmGicbUIJFd6vbg5d8WtyyQAxtSgV_XbEPyvVNAGy4W9R5oX3PhlbroTC7zIUqFTAbqJjQQGobBDcn-6Ss9rdxuNe0MwFfoHt2MMC_pJgr05isSybjCZaZ8e4Z5Dr5UIM4inYijWdSeVGx0sw7X1u5Y5nNKpdrFXc918WZaRhOG0k91DOoGA1-iF8ouViPAa36dmFn8NqPwru9vVLcULikrhJLrpczBS7ihXScbf8j1hbx9MGSdd81Jvz-eyltU4nluMJiWYH70_w-2MWZabpTb5sctiuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9d994e5a.mp4?token=i922rPiwQpO4tucuL7wq1HNm-60ntG_zMgOpCBlD4seHPFqlrxyvWL33FmGicbUIJFd6vbg5d8WtyyQAxtSgV_XbEPyvVNAGy4W9R5oX3PhlbroTC7zIUqFTAbqJjQQGobBDcn-6Ss9rdxuNe0MwFfoHt2MMC_pJgr05isSybjCZaZ8e4Z5Dr5UIM4inYijWdSeVGx0sw7X1u5Y5nNKpdrFXc918WZaRhOG0k91DOoGA1-iF8ouViPAa36dmFn8NqPwru9vVLcULikrhJLrpczBS7ihXScbf8j1hbx9MGSdd81Jvz-eyltU4nluMJiWYH70_w-2MWZabpTb5sctiuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
با تایید اسرائیل، پتروشیمی ماهشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/news_hut/65420" target="_blank">📅 08:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65419">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
پرتاب موشک از ارومیه ، لرستان و اصفهان به سمت اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/news_hut/65419" target="_blank">📅 07:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65418">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووووری؛ انصارالله یمن از آغاز حملات به اسرائیل خبر داد  @News_Hut</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/news_hut/65418" target="_blank">📅 06:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65417">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووووری
؛ انصارالله یمن از آغاز حملات به اسرائیل خبر داد
@News_Hut</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/news_hut/65417" target="_blank">📅 06:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65415">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
با توجه به شرایط خاص مذاکراتی و همچنین آغاز جام‌جهانی، حملات ادامه دار نخواهد بود  @News_Hut</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/news_hut/65415" target="_blank">📅 05:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65414">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
با توجه به شرایط خاص مذاکراتی و همچنین آغاز جام‌جهانی، حملات ادامه دار نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/news_hut/65414" target="_blank">📅 05:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65413">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b906cb3be.mp4?token=de440BZjE0IxOdm59H0L9VJ8wD-m7-fMRuU2se-HEgnhQa1pssDSGuOwfO9PQDYcGeWUmkaFPr1JRxf3zqd0D4x4X1qMlHsIeS49-2cQ_xReBqsWnaHQfUH45UNKR2d7dsFThm5EYvKfFMKooSxjO9AmnVOyZ56Lz_IVo0oA-6Mwk5kORuhrfqgfTjm9o8pjHAjOLBB3Aw6nEUG-bLEQ9WgfvfijT7IvpEgY4GODgN_oZWrMnPOeD_-bsd8Y9mstiyksQq0j0vnrtB_RL6k1HdBF2a6jwSNUZf4RNw0AItGP4u0kpCbhhnpmN9E6Pqychc09zcvR_rVttKYnHV7WNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b906cb3be.mp4?token=de440BZjE0IxOdm59H0L9VJ8wD-m7-fMRuU2se-HEgnhQa1pssDSGuOwfO9PQDYcGeWUmkaFPr1JRxf3zqd0D4x4X1qMlHsIeS49-2cQ_xReBqsWnaHQfUH45UNKR2d7dsFThm5EYvKfFMKooSxjO9AmnVOyZ56Lz_IVo0oA-6Mwk5kORuhrfqgfTjm9o8pjHAjOLBB3Aw6nEUG-bLEQ9WgfvfijT7IvpEgY4GODgN_oZWrMnPOeD_-bsd8Y9mstiyksQq0j0vnrtB_RL6k1HdBF2a6jwSNUZf4RNw0AItGP4u0kpCbhhnpmN9E6Pqychc09zcvR_rVttKYnHV7WNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
💪
گزارش انفجار در ملارد
@News_Hut</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/news_hut/65413" target="_blank">📅 05:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65412">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
حملات به تهران  @News_Hut</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/news_hut/65412" target="_blank">📅 05:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65411">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nA0i1ncXQVtdq5-S-mFgy7L2jE90QQwl8dC1LNUu1HLFB1-2Km_jC5yqiEsb9RSWkYctNw6qsoUx1Enix7o_h13JJQrHsAhhlWVLIxZ3nLYeIy7K4ntgj4dele0beQmP-0CGcolVCu65QHTOW7t-8o7fOIfz44ptmrFw1ZU9ZDRVmRjlW9iHF04ZGkUqB9YfgI9z0uuHLKfdxVnh1XSvDW5ATpOiJlRvnEQ6kuU8To15ljsmT8sqYnpsKaVYzYOhOtM0fgS1wjIx_cfD27Po_bGc6_lhkqDdu3YkxA9WDhw20SlZB3R3DiWuq57629eNdgHQfkk2WpIRq3dfFEtmeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات به کرمانشاه  @News_hut</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/news_hut/65411" target="_blank">📅 05:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65410">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sc7Wr8iW0Hq7EoT6r6YMvUweyvPNYgMt_Huep1j6Pm7tUcyBFozrF05XMgm6PB_BMdMYzuL7k36FGxXSUw524w1AkOttYLMaoWfbIQUDqOhZaGVWghf3yrEh0ToVpKH11KnD0DHPPPjV-q2UitjVv3qdbwbFBxebb15flKtH6VJ3dXcUMvWy2oSXNcYVD6DSyq6VsbGwt977gTmp-gZ1d_ewhCKOHvA0byrtWi6yA7XCmvwbCqf0sC4QhFo28VzpvMbvQk1j1nvy26lgn_ItpGxcvwrqmEK3pro5eDWU8OIwNFnoeC9zHahD-k7AEp4RZaphVwu_rOV5PVMwZY6mjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات به کرمانشاه  @News_hut</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/news_hut/65410" target="_blank">📅 05:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65409">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13951b2150.mp4?token=Ig-sBnqBtJPxa47EBNlaP_pkR03sXFhZDL-tFO7mcKzflf7wM1yCFakuDumVirgi3isXpGxCnZvVbNEmJVHg7zfMAkyf_y2U0xzSyQ0yuF9d8GFl_lPsm-g6-WfS5ULDB_w9E0HsmxCEeoXCVRseiSRvx9Vei0FxStrsTtRVNVV2Q6yhO6xo3AMMlhzpMzGAmVamn8uCZ_3tWSIEs0ybSLsCHqU2NSW5iSj3wnA0KmC-6708CdQhYU02JluMSzViMew5CKrk4jvdAJAEuF9iZcSjpQDFSpDNg_g6UTSY4nxBO1Tk1oAXUHyZavdvH6ztKqY1D8Vhle7wxITt_eO8Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13951b2150.mp4?token=Ig-sBnqBtJPxa47EBNlaP_pkR03sXFhZDL-tFO7mcKzflf7wM1yCFakuDumVirgi3isXpGxCnZvVbNEmJVHg7zfMAkyf_y2U0xzSyQ0yuF9d8GFl_lPsm-g6-WfS5ULDB_w9E0HsmxCEeoXCVRseiSRvx9Vei0FxStrsTtRVNVV2Q6yhO6xo3AMMlhzpMzGAmVamn8uCZ_3tWSIEs0ybSLsCHqU2NSW5iSj3wnA0KmC-6708CdQhYU02JluMSzViMew5CKrk4jvdAJAEuF9iZcSjpQDFSpDNg_g6UTSY4nxBO1Tk1oAXUHyZavdvH6ztKqY1D8Vhle7wxITt_eO8Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
انفجارهای متوالی در شهر اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/65409" target="_blank">📅 05:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65408">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuvyJBCkMSeSTKTI4Oe3f71g5AMsDxlMnOkehasJHct6ExpFqyd4e1vZDG4fV1GFu_SRzAq5I2b8QC870WOXz9p79betrvCASGN4n8jFtTq8-UXwmR9wHwHUN4bjcn-69YPk9KBq-13UJwF1sZ_PFN1eV_szufClKh5pCPTjHs1KUMY1sOgStjyHAof6xY743oJLtUYaWWSpVdgdRb7weMxR3iZcaOPVWgrp3iZVz5R2KdeR3YnHv0dW8qGWpuIqrWARWrqXT5f5qAiAt5XElsbLpUunxQodpHyl2HfBO5kSbyIGCOgOEvfMTKaknR3twGgtxOsCr4dsfICcRt-WEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇱
نیروی هوایی اسرائیل اندکی پیش به اهداف نظامی متعلق به رژیم  ایران در غرب و مرکز ایران حمله کرد  @News_Hut</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/news_hut/65408" target="_blank">📅 05:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65407">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jNBmiCbt2YAudE3ZI897Z3LFTrh2lAhWp5QXlEXMolQ93TzWoKH4JnOEp56UsT0-VFmJ8bC90GNyMsU9V4hoC1CMIl2sdFMBPa3LdIqaGr1IzoMuDuchXp2bYJYdhE7XikhnMKPIx57OoY-VEcimSHcIHiOT-zr1sGnY180iJN7_MZF0j5pqPnS167LKsLiKSXvkwplnqFgZrutcDdGg8J86Q9Fi6jg4wiIWq9J2JUH-VLuE1UFvoXlf6uEeMkBdnZhMngKUSLRm3soglGyvC0z91kNkM75jw0q0uXm4LZ76FqyXUs_jtcLYBHdOFD0Y5P8q7cQLvrMaKr12dKcJtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇱
نیروی هوایی اسرائیل اندکی پیش به اهداف نظامی متعلق به رژیم  ایران در غرب و مرکز ایران حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/news_hut/65407" target="_blank">📅 05:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65406">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/news_hut/65406" target="_blank">📅 02:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65405">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eg5V3ZhdwLViWhAVGz0WxafsbPKOFP-pf_AqetGYDF0V-07VtDkoAU0Xi5RxIiUhkXexPopL1NVUHtAq3KVdS55UlQVJdx9n5bw4jIt4VNxT4t8U_T_uUqQOd1iEb0wz2IC46pCfzW6PnmWNCun_lzkKFXW8qH7JZSpIgLOVziiepnUO86yTVgYrW0CFzQxeo2DXp4kpSIlJUIMsL7-O6p2SOcWYdnzvvmv0CeYe0XLS3I2aIJIvHZwMTPRJ3bXzmo6ZopvyGLQsWFnxYUn7_TdHGPni5bj7Pe8xDKVVx8nvKYfwUn4RzwDlqiRAEsyMlEStctBd3-UlZDZ1_85qgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/news_hut/65405" target="_blank">📅 02:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65404">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4k6jfebxjdMOdygGNeolQUb4IE-JVXiRMFYz7hY42XwVSPpMPG3QKRAEIDzir6AapOn6Lw92Hky2uQt56sHj_ZLbwNBaYJC4NKMzSAHNRTyvLzz7a6B6Z8P5cjIOBo8azBZXmvFuBletULKTMsCokVjXlc0hvTMvU_aBUXWVqKVCAOiJtzekhJlt4djCMsRQVj1P2i9sAUGR5qGbqVGvEJYuJK60Vd3Qj5p38XZnUo1LWn7oWTZhmMd2aOgX1cD3svvg5dxzcwW9LaL--KO7MCWuFU6ddVJxYbD4VAQUpNJvlfG73UdWQqv1zvrsDrr2x5hT-ffGnQQpcF1NWG57w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مراکش
🇲🇦
-
🇳🇴
نروژ
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
یکشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ردبول آرنا
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
مراکش در
۱۰
دیدار اخیر خود،
هفت
برد و
سه
تساوی کسب کرده است.
✅
نروژ در
۱۰
دیدار اخیر خود،
هفت
برد و
دو
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر مراکش
۲.۵
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نروژ
۳
.
۸
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب:
۱.۲۷
🧠
وقتی از بازی لذت نمی‌برید، متوقف شوید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/news_hut/65404" target="_blank">📅 02:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65401">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: نتانیاهو چاره‌ای جز پذیرش توافق با ایران نخواهد داشت.
@News_hut</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/news_hut/65401" target="_blank">📅 01:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65400">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frombetcart - کانال بتکارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqtoPx8yIC9kHlpvsfLTM6sFFi-6s12N2OiwT-4sRO2lw-IhPD3wlurBkhbHnykpyduOh2noVexEi0pc5tvz2nPgLn6eNZy2R1402zqum1aDHH6C69B3itpx8tr11PqtZgxwKWs2uh3rfEtF44kwzCAh3o2lRlhBSRBoUwOvGfglZYu5bNdRCPfYCAXqw8lVwBKn5PL1HTboMBGtxKED5pAwF2ZC6dvxybFueOU_HfGbxnkIPCl68JevcddzIgzyRNi_nBABybF6-02uqmn9P8_BHZ2cvNa8354qUqxpqkG7_pzQ9746fXE7p_G5AnZWDumqAn8m-dZXrsBHYalcWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یه فرصت تاریخی!
💥
بزرگ‌ترین کمپین تاریخ بت‌کارت شروع شد!
🏆
برای اولین بار در همه‌ی جام‌های جهانی؛ جشنواره‌ای که تکرار نمی‌شه!
0️⃣
0️⃣
0️⃣
,
0️⃣
0️⃣
0️⃣
,
0️⃣
0️⃣
0️⃣
,
0️⃣
6️⃣
تومن
❗️
☄️
جایزه‌ی واقعی برای ۱۲٬۵۰۰ نفر
👉
http://bit.ly/4ep75qf
⏳
تازه لازم نیست منتظر بمونی جام جهانی تموم بشه...
🎁
بت‌کارت هر هفته جایزه‌ها رو مستقیم به حساب برنده‌ها واریز می‌کنه؛
✅
سریع
✅
مستقیم
✅
بی‌دردسر
⚠️
ولی یادت باشه...
این جشنواره‌ی بی‌نظیر فقط مخصوص بت‌کارتی‌هاست!
🚀
اگه هنوز بت‌کارتی نشدی، الان وقتشه...
⏰
فرصتو از دست نده!
👍
وارد شو و شانس خودت رو برای برنده شدن میلیاردی امتحان کن
👉
http://bit.ly/4ep75qf</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/news_hut/65400" target="_blank">📅 00:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65399">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
آغاز حملات اسرائیل به لبنان  @News_hut</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/news_hut/65399" target="_blank">📅 00:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65398">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
آغاز حملات اسرائیل به لبنان
@News_hut</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/news_hut/65398" target="_blank">📅 00:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65397">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل: رژیم ایران اشتباه بزرگی مرتکب شده، ما آماده‌ایم
@News_Hut</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/news_hut/65397" target="_blank">📅 00:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65396">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
ترامپ: نیازی به پاسخ نیست، صلح نزدیک است
@News_Hut</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/news_hut/65396" target="_blank">📅 23:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65395">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🇺🇸
🎙
ترامپ: به توافق با ایران نزدیک شده‌ایم و نمی‌خواهم اکنون در مذاکرات اختلال ایجاد کنم.   @News_hut</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/news_hut/65395" target="_blank">📅 23:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65394">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🇺🇸
🎙
ترامپ: به توافق با ایران نزدیک شده‌ایم و نمی‌خواهم اکنون در مذاکرات اختلال ایجاد کنم
.
@News_hut</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/news_hut/65394" target="_blank">📅 23:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65393">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید: ترامپ بهم گفت الان زنگ می‌زنم نتانیاهو و می‌گم به ایران حمله نکنه
@News_hut</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/news_hut/65393" target="_blank">📅 23:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65392">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: حملات اسرائیل به بیرون هماهنگ نشده بود؛ اصلا از این موضوع خوشحال نیستم
@News_Hut</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/news_hut/65392" target="_blank">📅 23:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65391">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید: احتمالا اسرائیل پاسخ خواهد داد  @News_Hut</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/news_hut/65391" target="_blank">📅 23:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65390">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید: احتمالا اسرائیل پاسخ خواهد داد
@News_Hut</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/news_hut/65390" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65389">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
📰
فاکس‌نیوز به نقل از ترامپ: چیزی که به ایران پیشنهاد می‌دهم؛ موشک‌ها را شلیک کردید دیگه کافیه به میز مذاکره برگردید و معامله کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/news_hut/65389" target="_blank">📅 23:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65388">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ارتش اسرائیل: تموم شد بیاین بیرون
😐
@News_Hut</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/news_hut/65388" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65387">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
ارتش اسرائیل: تمامی موشک ها رهگیری شدند  @News_hut</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/news_hut/65387" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65386">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ارتش اسرائیل: تموم شد بیاین بیرون
😐
@News_Hut</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/news_hut/65386" target="_blank">📅 23:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65385">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
ارتش اسرائیل: تمامی موشک ها رهگیری شدند
@News_hut</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/news_hut/65385" target="_blank">📅 23:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65384">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
وزیر امنیت اسرائیل: امشب تهران باید بسوزد!
@News_Hut</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/news_hut/65384" target="_blank">📅 23:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65383">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d76423eea.mp4?token=aNhSI1XrwRmpk82jF-70RMROvktJKJi7He6AD54KOGMAgy_IdS62PWif2WLbX5m2b6rWq09XDW0YWs0wA1rwRg2o610K4-g5dz-F-kaodEtNS7lEJ8WuYecytdmDo1_7IkoxO6tLVlZr5_jqHw3bOWM6qm5ZlBAZBg08EhYpxXAJzRpmKoAHxMZ7S_rDpSgsf-LwBDVMAljZOVhzPJhcQZc8XZ1pAv-2n0uNjWXQlKTL1X_cbSMmXO4ExWh7gyVuNTMo8o_U-H20zldtg9U4CuXhJDJQ2xQipU5mCaFy2TS4cgBFOSLQM0S-8PcYKpGuxfh1GgoLAf7N4YRfsudrSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d76423eea.mp4?token=aNhSI1XrwRmpk82jF-70RMROvktJKJi7He6AD54KOGMAgy_IdS62PWif2WLbX5m2b6rWq09XDW0YWs0wA1rwRg2o610K4-g5dz-F-kaodEtNS7lEJ8WuYecytdmDo1_7IkoxO6tLVlZr5_jqHw3bOWM6qm5ZlBAZBg08EhYpxXAJzRpmKoAHxMZ7S_rDpSgsf-LwBDVMAljZOVhzPJhcQZc8XZ1pAv-2n0uNjWXQlKTL1X_cbSMmXO4ExWh7gyVuNTMo8o_U-H20zldtg9U4CuXhJDJQ2xQipU5mCaFy2TS4cgBFOSLQM0S-8PcYKpGuxfh1GgoLAf7N4YRfsudrSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات جدید از اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/news_hut/65383" target="_blank">📅 22:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65382">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1Z2kYxw88oyVWVinivPto9B3hjYguhaRE35E_k9v1xACBt1jNUozTngKyOHJchm5eGneiUIDegsVWUX1t6NW9gn9xaAOoSfPjm72oz7EZN2Af9PZ95VGAElMcc1KkmK5ZclFl_dem3aVgX2yvtHHHE5dApm5IN20XG0FHKNVgiuBKkGcrrvRmc58Zdc_VLLuFHVq8bbtkDcmAbdeVG8FMipsCxdacwsPxj6G4ItgWibPRG3JAb3j4Z8zBLLhQqh5iRCi0QdyulHRcsPRAcRwCSVQ6tayrmf7olrYLSG_3ltmi5p3eABpcMR4ufazcZ6DrNwkoVG2jYk5UYC5jMBIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی سپاه به اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/news_hut/65382" target="_blank">📅 22:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65381">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
📰
#فووووری؛ خبر اختصاصی ایران‌اینترنشنال: سپاه پاسداران آماده‌ی حمله به اسرائیل است  @News_Hut</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/news_hut/65381" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65380">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
گزارش غیررسمی پرتاب موشک از کرمانشاه
@News_Hut</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/news_hut/65380" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65379">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
📰
#فووووری
؛ خبر اختصاصی ایران‌اینترنشنال: سپاه پاسداران آماده‌ی حمله به اسرائیل است
@News_Hut</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/news_hut/65379" target="_blank">📅 22:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65378">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Byg4_dM52CA_jd0PRrgw5O1hjol7iGgQFKLd220Sb-S6NpRkeiiCitm4PIqo6gv4Dmgd7YprjcBCnlVefdsBfXLsD-jEaDTeDoDFfyYveTkphPPsZ9UqKgF4TmeOwOXP2g3gZ0_ECJoKeiYvYD1EyP-ykagtuOJycmq0mnn598nOoHXCX4GDfsveoeHWtrvOxTxu_ZJYdzMjoTr2WDRFyBQfZDbvTn1pznGAdo-jXOMWUwsF-Bh3-F-tTLSZ5OL2YXN4NPPIFHYctXNGnXv3v3-OoMXRPUjJW8NWdZrp3F9V3FBoVZC1Kc8fB6sovY1ZylgCwBEn0y2pnBQq_LGmmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پرواز تهران به استانبول به دلیل حملات احتمالی ٫ مجبور به بازگشت اضطراری
به تهران شد
@News_Hut</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/news_hut/65378" target="_blank">📅 22:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65377">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65377" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/news_hut/65377" target="_blank">📅 22:06 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
