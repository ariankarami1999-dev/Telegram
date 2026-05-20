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
<img src="https://cdn4.telesco.pe/file/bmjhguE7-B_4R-d5d-6kt3pWt5PTtMBjN8HrV-jLPT0MbUeZ0BruyxftwrYCP6CSSm0A3GCbksOQKr0--_JBfOF-rVkCnwWYrNfXEfFf02rNJrW2DM3olh-YGlTN5u-8t9PFqg5D82n0cTlqIwLYfwIrz1qkd60q7Lppf4YoZKHVYM0dPbSz0-qct-nTrQCzHdERfv9ckxh0SAcXMphRBlUd0R8W5jBcO_aCsZMRGN9Mi49762ooA0yHfN2yHVMMp37rNO2JAhCpgHowbK7tOlvf3B60QrfiuaVU2XXPJ0wxgnnEHVUyax7-4IhNCTK1fzaMPpAO1chuyqRZRhV4_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 143K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 08:13:19</div>
<hr>

<div class="tg-post" id="msg-64975">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دموکرات های احمق برای بار nام خواستن جنگ رو متوقف کنن که بازهم رای نیاوردن  @News_Hut</div>
<div class="tg-footer">👁️ 679 · <a href="https://t.me/news_hut/64975" target="_blank">📅 08:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64974">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Be2cNgahM1VVjqgLJDxeYIWb4gfitHlthLFKaOrP6FDMObnVbxqcV8kLOzi0KdvNE33otGeIpnbFiUu80q0tDmcX6benKx1EwXukg3Hsu6I6gaM8lmM-LvJ8mW08VuFl428o5gmyxAERGaVydRo32ZSp9U_O0JelvsPbTmTX_LMogyBpucvAApoMx6uvTKCPb31ijf_CZILTZD9B_LTE_MN-0ZkdPPD2xx_dskDMvzpwanalYt4tynjZuM8fo96XCZOgXKOVOFa4sHCsq8wS-u5hLWPz3jA6aJ9spGfF2n-qIiU2wayCva9Bb3PIoxSoZmyXoxODUqWUzhwM4kMKlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سناتور لیندسی گراهام:
امیدوارم و انتظار هم دارم بعد از این چند ماه مذاکره با ایرانی‌ها، دولت ترامپ هر تلاشی رو که برای دوباره کش دادن مذاکراته رد کنه.
این رژیم ماه‌ها وقت داشت به توافق برسه، ولی به نظرم واضحه دارن بازی درمیارن
من ترجیح خودم راه‌حل دیپلماتیک هست، ولی قدیمی‌ترین ترفند ایران همیشه این بوده؛ امروز و فردا کردن، کش دادن، کش دادن، کش دادن
در مورد هر توافقی هم، منتظرم بره سنا و اونجا بررسیش کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/news_hut/64974" target="_blank">📅 07:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64973">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FasRPezAv-9QaKcS-V3yEYU4cKlqbxET0r_5xDW0QITa7a4dXYGeKyp8F8wCFtdXBGw85Cu14frMmtNPlHvJBrH17-9LeYxsoAF8yL8ycpl6BPJ_1Ha_X3tYUb-6K-0f90ieetPFuWGqLquvoIXRf14S1VuZFXrSNMxGbItJYqsKxi8D7WW2XATJnMoj0zQTOpiIVbJK9wZd_QZEN36kiUNJK4V3VHCa-VWIFxfcT6D5GfEsSrrfR5xpO2HWyfIoymx-pQim7ZwYyReuvypUqCTwpGJ5jVMXOFIvidWDR51RwNwNxYcN2bdpLcl-t8CJsio0Cp9vos1D9c5Fkqcmkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غریب‌آبادی، معاون وزیر امورخارجه:
امریکا میگه دستور حمله رو به طور موقت لغو کرده و در سایه تهدید می‌خواد مذاکره کنه
اونا باید اینو بدونن برای ما، تسلیم معنایی ندارد؛ یا پیروز می‌شویم یا شهید.
@News_Hut</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/news_hut/64973" target="_blank">📅 00:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64972">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🇺🇸
اولین اظهار نظر متفاوت امریکا نسبت به حمله انجام شده به مدرسه میناب و جان باختن کودکان این مدرسه:  برد کوپر، فرمانده سنتکام: ایالات متحده عمدا به غیرنظامیان حمله نمی‌کند. مردم ایران دشمن ما نیستند. سپاه پاسداران انقلاب اسلامی در این مورد دشمن است. تحقیقات…</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/news_hut/64972" target="_blank">📅 23:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64971">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b854a8a43b.mp4?token=pkj68I_AqkePWocGdDYv6utgNlbMM4AfSFD4i9c2T-cMPRcab4XJUVc0KHraQUZW6BJ0KFOg4UiCo7KLzwZTbTlPcQdH5pZ5X31RooCMAc298TtADHfa6UJxDgX43GcOvcg81SQtXIhii3olHRafGCnNMQjawnRKQokKUizFj_4mz3VY75FtQ5x4NWh0FNz4vwG29LcQSaMcrHEZj93kXpT6a9pcWjUO4Dwwla39FWElE2kD07ht9cejCi58SkMroIdDQsbLlYV6MZ-y6VIZjLnMmQ4pFcVOUKbffgw2bQjuC59YlKcfqis1Rf6sxV3z8F7beKM8a6ir9FS5XKnjPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b854a8a43b.mp4?token=pkj68I_AqkePWocGdDYv6utgNlbMM4AfSFD4i9c2T-cMPRcab4XJUVc0KHraQUZW6BJ0KFOg4UiCo7KLzwZTbTlPcQdH5pZ5X31RooCMAc298TtADHfa6UJxDgX43GcOvcg81SQtXIhii3olHRafGCnNMQjawnRKQokKUizFj_4mz3VY75FtQ5x4NWh0FNz4vwG29LcQSaMcrHEZj93kXpT6a9pcWjUO4Dwwla39FWElE2kD07ht9cejCi58SkMroIdDQsbLlYV6MZ-y6VIZjLnMmQ4pFcVOUKbffgw2bQjuC59YlKcfqis1Rf6sxV3z8F7beKM8a6ir9FS5XKnjPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جی‌دی ونس، معاون رئیس جمهوری ترامپ:
گاهی اوقات کاملاً مشخص نیست که موضع مذاکره‌ای تیم ایرانی چیست.
گاهی اوقات سخت است دقیقاً بفهمیم ایرانی‌ها می‌خواهند از مذاکرات چه چیزی به دست آورند.
در حال حاضر برنامه‌ای برای تصاحب اورانیوم غنی‌شده ایران توسط روسیه نداریم. این هرگز برنامه ما نبوده است.
نمی‌دانم گزارش‌ها درباره این موضوع از کجا آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/64971" target="_blank">📅 23:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64970">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmoAdmin</strong></div>
<div class="tg-text">⚠️
مدت این آفر 3 روز هست
⚠️
💎
پلن حرفه ای
1 گیگ : 280,000 ت
5 گیگ : 1,150,000ت
10 گیگ : 2,050,000ت
20 گیگ : 3,900,000ت
40 گیگ : 6,900,000ت
💎
پلن اقتصادی
5 گیگ : 850,000ت
10 گیگ : 1,600,000ت
20 گیگ : 2,800,000ت
40 گیگ : 5,100,000ت
🟢
کد تخفیف به صورت خودکار روی ربات فعال هست و نیاز به وارد کردن چیزی نیست
✈️
آیدی ربات جهت خرید :
@AmoAdmins_bot</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/news_hut/64970" target="_blank">📅 23:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64969">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e8365c27.mp4?token=CLXY9Zr6NWmA-4aWn9mSF0noMotTKPtfIynrpGyDd08P9-N8MV6UJdKmmiqWQyHLRUbJL9LhhVMiLz2JXln2bkuyN_PVhfN6tP2eXHTDnc0ophb87WOj-ap_Pg4K7qLEDoEbU6neFoIAiN4sf4y1JYy2rZ8DG1NmgiwFteFWlRQd1iQCnq2vqNESWgwzZn4SDFD0PJoBsqLtPa2U_Y1-MtowBqEijOQACGIz7zaa3wIKbxsmiwuY99Ax41xLx2lz1-9m1_9KOnJ1tw3YillkJuJWzxXPdefdrguNSc8fQO57Ht14V8C5QcRsRXnLorD3fDDJRWUmyYJoHyBoS_ZHqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e8365c27.mp4?token=CLXY9Zr6NWmA-4aWn9mSF0noMotTKPtfIynrpGyDd08P9-N8MV6UJdKmmiqWQyHLRUbJL9LhhVMiLz2JXln2bkuyN_PVhfN6tP2eXHTDnc0ophb87WOj-ap_Pg4K7qLEDoEbU6neFoIAiN4sf4y1JYy2rZ8DG1NmgiwFteFWlRQd1iQCnq2vqNESWgwzZn4SDFD0PJoBsqLtPa2U_Y1-MtowBqEijOQACGIz7zaa3wIKbxsmiwuY99Ax41xLx2lz1-9m1_9KOnJ1tw3YillkJuJWzxXPdefdrguNSc8fQO57Ht14V8C5QcRsRXnLorD3fDDJRWUmyYJoHyBoS_ZHqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره اینکه ایران چقدر وقت داره تا توافق کنه:
دو یا سه روز. شاید جمعه، شنبه، یکشنبه. شاید اوایل هفته آینده. یک بازه زمانی محدود.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/64969" target="_blank">📅 18:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64968">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2efb45471e.mp4?token=HikcRBYvrrgeIsO2q32EI0Av01O6oRqEfuCaQa1KxYYocIG0I0NjvSZ5CAOa8aOhc81d0LqUyWK6sEEBReixnxO5P54f1xI6vTz8JYBA9OOwCnnlMv0-W0azEvfmIcKhGcHUNiwSXel-oiHjtP4Yjtc0v40cgIFpu_7fmDMrrMQdjFnoKlNvt1tCFMsYq3dQPypAsMHwbr6xBYztfZ7OHyTwLZavNGzRpa58Yqkhk6RgSgjONkT0Sa6pQSGlEcYSFdtkUpxP901JqQ8ZV0vWToOaJdjJoxK_7b3lNYfF66BuO8QN2bDPJ6Gw61zP4WjhgI3FDVz3UVkptjtZX_nH2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2efb45471e.mp4?token=HikcRBYvrrgeIsO2q32EI0Av01O6oRqEfuCaQa1KxYYocIG0I0NjvSZ5CAOa8aOhc81d0LqUyWK6sEEBReixnxO5P54f1xI6vTz8JYBA9OOwCnnlMv0-W0azEvfmIcKhGcHUNiwSXel-oiHjtP4Yjtc0v40cgIFpu_7fmDMrrMQdjFnoKlNvt1tCFMsYq3dQPypAsMHwbr6xBYztfZ7OHyTwLZavNGzRpa58Yqkhk6RgSgjONkT0Sa6pQSGlEcYSFdtkUpxP901JqQ8ZV0vWToOaJdjJoxK_7b3lNYfF66BuO8QN2bDPJ6Gw61zP4WjhgI3FDVz3UVkptjtZX_nH2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: دیروز چقدر به حمله به ایران نزدیک بودید؟
🇺🇸
ترامپ: یک ساعت فاصله داشتم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/64968" target="_blank">📅 18:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64967">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:  ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم. خیلی زود خواهید فهمید.  @News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/64967" target="_blank">📅 18:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64966">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9954bd7931.mp4?token=rrf4cr_e_XHpEezRCFztwbEzWzfZVFJEv7k_swRAJnrgGuAQfiDjJd-tm0VJS1rra1ygvVpzvQN4bkzyV6bnPVdfmYpL2gQGVtJaOP7VpYaDxhoLY-5XkZss3xvu_WSVck2pJ2xyUAamph1F_fODVjeMV8fWNOaHxkB92AsGbE8HbkYwhoWegcGeyhncb7hBC-9qBAzL81JVnFDtYHEwblI0iNqELvTaYX2ypUn1G0xyPAOeZ2XrB46Md3k_wBDDnK0LB8zUMwGi_F-WImscpSvML7ObVJqgbVqLsI1cYpGd_MjCTG-sTvkPw80SH0lGDOnMJIFyNQ_MDWWX6h5lHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9954bd7931.mp4?token=rrf4cr_e_XHpEezRCFztwbEzWzfZVFJEv7k_swRAJnrgGuAQfiDjJd-tm0VJS1rra1ygvVpzvQN4bkzyV6bnPVdfmYpL2gQGVtJaOP7VpYaDxhoLY-5XkZss3xvu_WSVck2pJ2xyUAamph1F_fODVjeMV8fWNOaHxkB92AsGbE8HbkYwhoWegcGeyhncb7hBC-9qBAzL81JVnFDtYHEwblI0iNqELvTaYX2ypUn1G0xyPAOeZ2XrB46Md3k_wBDDnK0LB8zUMwGi_F-WImscpSvML7ObVJqgbVqLsI1cYpGd_MjCTG-sTvkPw80SH0lGDOnMJIFyNQ_MDWWX6h5lHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم.
خیلی زود خواهید فهمید.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/64966" target="_blank">📅 18:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64965">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba90deb154.mp4?token=oQICxkWk8V3bY9BVJA0EkScNvLJuVsPiYSpnzVtNSJn8vB989N79LsUZcHui_Af_1IWwz15m90uwpHaOjxPIATvBup6bEDPqLo07gGkyzJfZM8qrQZP-Y2wjY4TATYUcXfdugzymg10Rck_JmKkCq5JIs9i14x9AEF5_bVLEmUY-H4weO5Gxc513t_M1g33a3H_CtN7OLaYkkAy-BF1cGFk84eckKY6ZrN9RP6hJyYvErOWZMTAjHvUnOE90PyFRrBG7KOyhaFU_DEhJ8JDRCecQQI0a8VoS8e3a_7efbN-fB8qVfXXLxmDNuLl71kpGs5EVWk5ohG0nvAFTM0RK0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba90deb154.mp4?token=oQICxkWk8V3bY9BVJA0EkScNvLJuVsPiYSpnzVtNSJn8vB989N79LsUZcHui_Af_1IWwz15m90uwpHaOjxPIATvBup6bEDPqLo07gGkyzJfZM8qrQZP-Y2wjY4TATYUcXfdugzymg10Rck_JmKkCq5JIs9i14x9AEF5_bVLEmUY-H4weO5Gxc513t_M1g33a3H_CtN7OLaYkkAy-BF1cGFk84eckKY6ZrN9RP6hJyYvErOWZMTAjHvUnOE90PyFRrBG7KOyhaFU_DEhJ8JDRCecQQI0a8VoS8e3a_7efbN-fB8qVfXXLxmDNuLl71kpGs5EVWk5ohG0nvAFTM0RK0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار طرفدران حکومت تو تجمعات شبانه: مرگ بر امارات!!
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/64965" target="_blank">📅 15:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64964">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
خبرگزاری مهر: صدای انفجار ناشناخته در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/64964" target="_blank">📅 14:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64963">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yhxn0Rm82LjinjwaccLgKQBQ8pAn6odr_NRmRWIeqQCXtXl49lDgfp4Pquq6M_SVfbVGmoh3zyfQfFmkjEYV4oryn1FthSs8SC4jTVwPksBBYj5Llz-jsd_Pu6_xbn4MRBnz837xKOKHg2s2qO-7PSqJLdp9xJetLfRRikTUXsrgQae3Oc7SwYBCnSSl0kED-2GgXoF5ALdUHSzvlI_nocSNnGYYs0lTIL-MCYmDtFuBad-fnZJDCSx_yJ3DJnbXE9c5z_vUmYEjPSj9hpMESsVSBlSE4t4krhkQzOkXxvSIIJhCmGKIbGh5dhoebu0_eHo9HDIMJpoLW0LlR5cKvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:   من از طرف امیر قطر، ولیعهد عربستان و رئیس امارات خواسته شدم که حمله‌ای که برای فردا علیه ایران برنامه‌ریزی شده بود رو فعلاً متوقف کنم، چون مذاکرات جدی در جریانه و احتمال یه توافق وجود داره. این توافق به نظرشون می‌تونه شامل این باشه که ایران به…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64963" target="_blank">📅 01:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64962">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIZa6wI7jGgErNlVWvzit_XeTM0GqFOfgWvGCKm8VLWLI6XhLWUIFzl0bNh9nDxAAFYOKGJwk4PlgWLml-pa-42738Kn_uKIip8wcma6xc2btOb70boY8bkuncpfpxJ_nA5cA6choQdG8atnByuwLCJxt4FlVzBU9U-xL1deR8Iuiy61i5hM3NQtVPZMmme3UX8Z_oKVCw8irhCfBBjJ0X6W6rqld_QQGUWfGq6g0b-V7j8mxbi1yGINMholVa3byF42WR6Fcjb1Xdf_vzRkzBV_dsKhlo6429R3wu_BnE5mG-LrysrOnNDBWJlxUA8WiK-Ra9y9EhIqdt3PwHO6ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
من از طرف امیر قطر، ولیعهد عربستان و رئیس امارات خواسته شدم که حمله‌ای که برای فردا علیه ایران برنامه‌ریزی شده بود رو فعلاً متوقف کنم، چون مذاکرات جدی در جریانه و احتمال یه توافق وجود داره. این توافق به نظرشون می‌تونه شامل این باشه که ایران به سلاح هسته‌ای دست پیدا نکنه.
با توجه به احترامم به این رهبران، به ارتش آمریکا دستور دادم فعلاً حمله انجام نشه، اما همزمان آماده‌باش کامل هستیم که اگه توافقی به نتیجه نرسه، در هر لحظه یه حمله گسترده رو شروع کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64962" target="_blank">📅 22:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64961">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLLCdyNW1cK0qxBJDQuRTdtbCml3_8JOfdj52cv7esJJ9oPX2p9EsktXgum0oMCZ3HFzcbpgqsGeFAnzhKposIocpnG9kLlzOJlW1YKk-er8shfkRj0SEBVPocHte80jyTl3Ui8LbcIXiVf5BhzUVDUOJlZ3n1MiEnLb84lHMFAHeI30beu60DlsIvT5ykzyL447Z3t7gH6uGOfUDJts_HUUieMRAtKAlBkHNnYZxoUAahsmmO67xAdRZhEzGHRPAuaBrvQaytykMGdv_GmIaX5REumFdsaBa-fgoyTxmiHNYDaoyl7S1tYNPfkjXGDM5ysgUfKBoU58UpKcxAxinA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
«اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم» در حالی که پرچم سفید نماینده را به شدت تکان می‌دهند، و اگر تمام رهبران باقی‌مانده‌شان همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی بزرگ و باشکوه ایالات متحده آمریکا بپذیرند، روزنامه‌های در حال سقوط نیویورک تایمز، وال استریت ژورنال چین (WSJ!)، سی‌ان‌ان فاسد و اکنون بی‌اهمیت، و همه اعضای دیگر رسانه‌های خبری جعلی، تیتر خواهند زد که ایران پیروزی استادانه و درخشانی بر ایالات متحده آمریکا داشته است، حتی نزدیک هم نبود. دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آنها کاملاً دیوانه شده‌اند!!!»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64961" target="_blank">📅 18:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64959">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/asyvoV4KE8mbdgK-0GaXWTJJEnGqfVRWoZPCSyIFzwlhFvPt5LuVMqhwcmS66ZQ8xL1POGXvsyx1lrjO2x2DDdx7ThjoOLBarCor1cWV-4h3QtxtO_8_wtZQSmVF2SbtDcpEPQOw9chRWcEVfAXrljfDcp15Ut-G8Ht7HXC97nTNAtq08BY1253l2ZGSCP4KYdDwzjc7xmwjq-arr2RLuMPNz3bNto5VvhG-_wOenJ16BFZ_ifvSQADGkc1PR7Stc7dWOy1wwVQGZ13rkjrFQKefko721ItEwRALQWP-dgT1uz3R847JwpiCVo1D09iKNAff7eL5Fs9UbNSUxeRv-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TTocrwQDtFHBb3fG95esiK5Farw2TUYbMxYsEtTKe6DpWb7qjG2_tuZdAoWkjPjf3iKjwFyzSWhIAxnQZU0VTiOfUdnSjmncUeTqkyi96xu4B_ilaqlalokdN1BXCUdxF63-mDRBAZEiVao1miCNm0p95MprX38E_6nLPCY0EqVc62rnSRfHRUR2rYZ6zZ069AuRfrssvjBEVwz8i_ED4GxsEFefJUTRt8GLu2UNcr-pBScpJ3YxfSXTZe_3vMvP9ALBd4X-xcgP4lRQYUyfM4LrVmJT_8HqqnGoVwxOKYASp4Po8suwz9eNWVA-k_vVKn9AItnbCrjqzGYqWq9rkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت خودرو ، ۲۸ اردیبهشت‌ماه ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64959" target="_blank">📅 14:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64952">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Myc1lrt2HCJFrJkQYMCjmwYU1743jm8GjIV_PA9zvqvVVMsmH9a7FuKgCP-kimlLe5Q9fC1weHo5jkA42azEIKlnQTSuovolprJweVT9GGG_boHX5Y5C9i2MQeqTwBsngiln-KrIlrLmncE_nLiP_n0ehzdnAo8Te_7wKuBzExM_CZsH047vt4lP4VhLq34vFKZo66ywq08ow20YAHr9Zbvu-aa8cWjdbp4t0lcZU-Gr3WLmmZKB74w80b6GvWOk-g500x51No00OFlujymPnrDQxCKY4xfLhW6TMRoTcpwOP0znK3CjOaxufqz65GXfXCcf-_SjYQ7uNDHSFbaVGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VCZgNx13n0CfWy8sipw5OpF54hKPNGDWMGNGz1a5DdAD9N80qTCZUvV03xaxNfjCvM7mnz2FOM0_UygGc7CB1EK7sko_nPotmC-e4kvVZzK8V7fk9_uEqAD8DdnN5ZqRyIsTRFF-RJE2efcs3I-YdiU4UkY0MtoGzXsZr7TDvac7VtAkOsOga2mTufP-x3WkIKW6k2NVgZKIARlbTBr2DozrOuWfEY9HLyvBUHxnBPoP78_oBBUOUUx1h6CUBYrGI8m76hSRh7rCFRfMZrNg19Nn3nDSKvewswtHforYGqGW1ZCOLq5I-8Ph4whx2FiLaf5pOuN1YEM8QLQ10YLC2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Gij3n4lqIqVXYRk69sPRAgpM4xKD69P242dWTQnoAEtEC4-4gQ0DKOjbJtb57r7PeWO1N1gTkL4a6CQISDtdwEFNR1BzeKFOFF9NZE8MyFAbIAWgmndHGoZLrWWaqV9QGYZw0CZJIyhCZq6bTNYxqffFzaQst8V9PBXTuXEQsEaVdleZq4tDiQ5YQR4SXGpOGCVD9P_wLKjghJ-IqvZ-5z2ypCTllKtY9uKel2GzTD6BCVqoCQJ-B8WKaugafj_8iOwh1Zr4C5zvJiRJKMN0AsSk9nDPXoCIRCrAe_v6JG6MtpLNemNl_t6J50nK86fTsWgvBOOCeVxX4pVqBnGD3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rpwvmIufOClkSVZbiGp3BLPBukcyyaQUyc5jFk2ccvljvyWH0YVyPyh3qIGHcW7-nfAd0zrb-mn2QtaXgjwXnl1Em_iMd7V2fDEo2Coo7A4UOqtUDMZfeVXpx6JisgwGj-G0YWf3GcA0dCDxFd9TjLrn767Lu1XZiOQwKtvMjaU9FFz8agQPUFHvioGH88AHZ4ipoOVn3G3Rb-6pAFwC7S-Iaz0Kt34PavMw7OCBh8U-VHNbBa8S3rSm3CqH5et1s-Vwgf1qjXbWzJvVqJdJVhO_jhDDwubsv_81Aagqz6QgEBO9PY9q0YJOuioskJUJ3ldtgGoHNm9_PUkRBZaaDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vZ1YIX-bok-1of3kCVSR-V3FdO3-Fsgo1e5FvUdIlkPFvCm_KxyCN6W8obopn-mfCooWYyJHNNEPA2txo8s_XcOYIJYtYkdhwJXYTrpRm1uawkkcKARM2sapBxREkAXp-JRjgD3UPB3wZD-La-IQ2eO37OBMjFfAt9AJnL3IfaAHKIzlYsrdtbo1sQ3Wz3f9GnmVm3SCzeBcW2snGLAZu0HO6uag6wsuVbalGCZmSGUJc4YjaMMyiDOgoan0w_or5sWlaiNf7kQvxBvcJVg1Vb2mstRVj-5twW0uMXhf94QBUHLMf9ak2RtoSG1mm9rMpeZ1HGjZ6tis_cLvZGzP9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ml7d4t1P5WctohlyzU2Yzxv3_U-64ZbHwlKfs_j1XGt1MSeEpDWPtZ4jTt175pAiluW9mTRCOEC7RSu32LoCfnuQwRCg5mK-m2sXgPn3-KoEnyLAIgc0-T9c6W9epNyxxezvFGiBq3l9VS_qccOsmLpBRH7b_6JJVnM0qXbG5MJ0cKLRaykKrkoIMMEQXEou5zFaoeKswhWUjPL8ShPVCrKMPf46kpWhz1ZO-2f24N9uEocnY8pcDbvTit2o-ATFjNBmPtVS65pQTvtwxA3r5MS9wro12uVfRTKb5Poq0ZHwOs-6hj5M-LMjA53Gfp4DX24h4aT8lUuTNESMIeqLpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FL3f-gvT31aMWZu-WBGIttY70wlqWcNb5dlbAU69JKSjpwpyi1IMvLfN1c7bkcIAl1_Zw5I0YrCtaHOMSaSjEcAdPCh0zYfoyalzsj2HGyuTq3tE7ABF6f9EAnG28Tvh5UHNhHxKTLyZCQhqqGEQWa-f0iij_L1W673GffqZohpZDcurpgDm1Z5mzUpj3WYWSHk3omYsmbK0yw1-bxmT_DakvcCeL-g4mdF_DeOwq28E1n6NbDsNSWttLvxxstfRaA1ZdqUi9_sSRnC8gBYdJLFES7xyeN_kDGMCO3kd8-5xmhqyAi_c8twK5bbhq2m8gyhlssLJs7cojE9wm2KC1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
پست های دیشب ترامپ دلقک که با هوش مصنوعی ساخته.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64952" target="_blank">📅 10:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64951">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqgyBGY1D0dkRpg5D7t3p6JcJF7Mdku2gmBJ9ki1dI1uwDIQV_m4ZlGcICYgDydAhVx5DGV6IjUSvVGPIxiy9UFLoMh-Gj-PUgONKGrYkX19t3lBIBrxXOFWyIUYJcCY_fUMD_Vxw_gIh701XynvCMZ0jZgz9NqE94XQKR1jvqwdvXS_Bbd4tnZcohu72Naq0ydm0Ks5w4AqThsKlXiiRA3ax_dsT-zlL905Qs4Iu-lDwEchOeZ0attLIUxReG3ZyNxBldt0ubbB26c48kgeu_QPgfwGNlgT2aLXjBc2SziD4VUju1sC1KXCcOFNOLklswQ39P7vzWiLC6hlNzvC7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پست عجیب حسین دهباشی سازنده ویدئو تبلیغاتی حسن روحانی تو انتخابات ۱۳۹۶:
حملات و ترورهای دشمن تا رهبری حسن روحانی ادامه خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64951" target="_blank">📅 10:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64950">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/D_QDm4fRVU4zHuxA8MALv_stUZaGsMcOjdW4bnakiLpPLQnOBOXsY_Myj5L9Qr36R8xJVY_G8avigD2-oH7LkftyLZB31bwF7ou5bChHkhZ_J2Bn02cV523pPD21rL_aywL8o5qi5TIf90jREu_D5HdQfXlxWvAiLhcK2eyxe1yWbHyIsLe7flZmebItlLsoeVpeLfp7dF86EVfzaIrBJ4_q8cCkgUvaJohn_odhy4kBEr2zqtDmg5UH0gKeB5wYQPTFOR5hYfXv-d1IHOyIjgrYk1b9sRBgn1lRP2eex5HZ8i_RnWrXRUK4CPYMZuLT9LHG0iuR_BUA1cnwZOAGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در شبکه اجتماعی که فیلتر شده
روز ارتباطاتی که قطع شده رو تبریک گفت
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64950" target="_blank">📅 21:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64949">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJNON6OlKnF97tI4tYJnZyycValntjEhlTl5hGTX1saNKdVblWmGqfe8pjk3pQoR0F8NW6PR4uAmhLuuBTj-a3_LulYpFGLJWgsi250P6UEb_L5rxw8qWC7ixRsHgn1-5egnqTk0LM35FWK6pVSOOrT3SOI4Hss7Hc7NPA66YlvEXJgT_4X7nzIeX4QjfM11oPStAoB-h0Od_gHBfP3JstQCMXnMovN9YZrlaB0ZhVQNWG1m9ch6juClNWdZZKc_zulAOD8pVQE5nSA-IEr906ndVN8eAqsqcdvN1jkW5Ich4WabJTvlxeGHhjq3a99koaZLsKkWDpqvIiJjMUqMZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64949" target="_blank">📅 21:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64948">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=WsJAtUdhziidgx8_oKx5ECxYWlX6n6NuTV0oUevDsnyVSkXVBcVbH4mMJh5PIlQI-onv8KGZFlVCfu4tavG_dp6W0SRKf3i_bgdNL7UCh4CuJfXwb-jgBBM-xBFLldXbu1b6k39BiFbaWcINlKkofjFqX6XzGkdX2tn2im-n4iuatI-HQQ4Jf5yM1XhgOrCHWbOboRxHzSjwlv1P-rzCLv8Cb8JUpSs2-lBs55YOR6ymjQQJazW5DwcqI2jWXE7i8QDSHdOBplmxxm1PoGkvOY0vaSA6lTrIfcHL0kbyj3F8sVKA87UZCj5-79KCPeMlhxrDp0gfMt-0mL1ezQmh-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=WsJAtUdhziidgx8_oKx5ECxYWlX6n6NuTV0oUevDsnyVSkXVBcVbH4mMJh5PIlQI-onv8KGZFlVCfu4tavG_dp6W0SRKf3i_bgdNL7UCh4CuJfXwb-jgBBM-xBFLldXbu1b6k39BiFbaWcINlKkofjFqX6XzGkdX2tn2im-n4iuatI-HQQ4Jf5yM1XhgOrCHWbOboRxHzSjwlv1P-rzCLv8Cb8JUpSs2-lBs55YOR6ymjQQJazW5DwcqI2jWXE7i8QDSHdOBplmxxm1PoGkvOY0vaSA6lTrIfcHL0kbyj3F8sVKA87UZCj5-79KCPeMlhxrDp0gfMt-0mL1ezQmh-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام:
بر اساس تحلیل من، هیچ چیزی نشان نمی‌دهد که افرادی که اکنون در قدرت هستند با قبل متفاوت باشند
آنها هنوز هم می‌خواهند جهان را ترور کنند، اسرائیل را نابود کنند و به ما حمله کنند.
هر قیمتی که لازم باشد بپردازیم، خواهیم پرداخت.
چرچیل چه گفت؟ «هر قیمتی که لازم باشد برای شکست هیتلر بپردازیم، خواهیم پرداخت.»
همین موضوع درباره ایران هم صدق می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64948" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64947">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یک سری کانفیگ فروش طی یک حرکت بی‌شرفانه برا سرور هاشون ضریب گذاشتن، یعنی شما ۱۰۰ مگابیت مصرف می‌کنید ولی حجم مصرفی ضربدر یک عدد می‌شه، حالا ۲ یا ۳ یا هر عدد دیگه‌ای  اگه این حرکت کصشرتونو جمع نکنید تک تک اسم می‌برم تا نه آبرویی بمونه نه مشتری‌ای @News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64947" target="_blank">📅 19:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64946">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تسنیم: ممباقر گذاشتیم نماینده ویژه جمهوری اسلامی تو امور چین
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64946" target="_blank">📅 12:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64945">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/fee67a1237.mp4?token=F6ewIRV_SuCA39RjaZjU2uMuOEth924FPt63t8lIYqf9ARPXBxB4feK9T2aDmv0Twr1Q16mAIXB9T1ysnoucfX5Z1_4_S-KZN2wN2xmHA3ZsRvxD5v4k4D7AmRBKfs4Yl2JereAsg7tDkUJTSRhlhAU1nBlC0LKSqBu-aAhTcEkEl0JvBTBk4ltnDnbS9HBWHcYzRS2zR6nItW1-Ddip1gs4Jj6mcDVUNDsOFUKr8pr0q5i2rlslXOanr-tUoDNEE-1H_O-HtzXD3f3sWGk9XbdFPXzb8k5q5V4sZrEgUtqQNDyJzMVS0OAB_n03FX6PjleRTC09jscaym2J1K-Ipw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/fee67a1237.mp4?token=F6ewIRV_SuCA39RjaZjU2uMuOEth924FPt63t8lIYqf9ARPXBxB4feK9T2aDmv0Twr1Q16mAIXB9T1ysnoucfX5Z1_4_S-KZN2wN2xmHA3ZsRvxD5v4k4D7AmRBKfs4Yl2JereAsg7tDkUJTSRhlhAU1nBlC0LKSqBu-aAhTcEkEl0JvBTBk4ltnDnbS9HBWHcYzRS2zR6nItW1-Ddip1gs4Jj6mcDVUNDsOFUKr8pr0q5i2rlslXOanr-tUoDNEE-1H_O-HtzXD3f3sWGk9XbdFPXzb8k5q5V4sZrEgUtqQNDyJzMVS0OAB_n03FX6PjleRTC09jscaym2J1K-Ipw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
‏
حدادعادل: والا من خودم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64945" target="_blank">📅 10:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64944">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/GWXJ46Y091gUV7coP0EEz5tfp72MTG-Syc50pPHHojrSf5g3Lko62eKFnJNStbhv-2l72ubIe4Vxh0rJIX90LRozHM5FFnZPFOulMlqWP0VOs9s8L5-aN-Zq0VpHUDFgjTl7Z3c3gb9wOkRhfbsxCT4xUyeREmxxutEEmboW7X5oJNF6-EgP_qPeLfSqVp3RIn3L7zaAswnjelmCUiYyD54i2deFfTnby_zXScAEvtR_ARikwMzJWNvLTf5WNGBZx_QogaP-xpTh1E2_B3RMD9Q9BPsgIlxtMkGsTvCUalrfzyziqXrRpU3z3jhTtk6c_aDZoBNmRVGS4Auiz_Y2kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیلی‌میل: کیر میخواد از نخست‌وزیری انگلیس استعفا بده
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64944" target="_blank">📅 07:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64943">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyzaMYmgDgS0dutCGLgJaXPTMgrHcS_AvyvsvKaXn2Fctemn_mKlkkwdRsz_R--fbR1WMJwS-42wiaKolEWRPkIRHSWBF-tne4lzqx6mhxCsRkYE2c6KBwZh-vOOmBLUcdUeTZRzESQ28My9bFgYjh9jx5-L0fXoiqdmD7UBZlFuHcjhDp37JUOpIBktyDzB0wUa1VYwT1s2jKWwuE7pSPipk2ndlZYq6936xtw-rlrZDVv1B40uPmO66arm2Dt9RGWklD6uq4g2KNUNaCGsH5JNOa6E2FF6TA64NJGrDT259IRFjyCHqQ7QdKXKk1Z2tJsDHPXj3ySmj9bjmWTPcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در سوشال تروث: «این آرامشِ پیش از طوفان بود»
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64943" target="_blank">📅 00:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64942">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مثل اینکه شمال کشور زلزله‌ی نسبتاً شدیدی اومده، مراقب پس‌لرزه هاش باشید
❤️
‌
#hjAly</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64942" target="_blank">📅 20:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64940">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vTE6Tam0DmBm10noXfqQ-HJ_PAVuUKAwlFa6fXsK7drIwInzrVIB-v8eSHuzxWfvna3iRBgaODNHQrUPY-5mi97iam7MHAmYYUbx0h_P1Emc5Qm-BQxpDHzmcBNfmiCRKEGxKjBymDj_0q1_hFBIIBX_OLPITMSDKPUeaQq67PNjgi0-4rZLZmupIFh4_lM41kAKIZ_BP-LVWYuYmLFWfChJ7CjfN_XD06kkmuFy_m_uJc6Kd4X_Vp5YaHX1tRR1mYHXh-78Ph4LEfgldMmKF7sGdrkp-qXvc-MgZGguJv4uyoFRl_sDI-sbMuHyLxFgYIaE13dAHuHc2bFuCBdZyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f0ac308ebe.mp4?token=TQkvOVoNaxV3pRNqeoCJQHGTunO7L8N0W4pkkhe3VDHgbxa6tmG2ntSgAcN1ffZr3cHzxFArB_79OXHNCiW3QK6DSbyhTvLijxp1dTpzmql4UCEMoTg4yiITZPcDZV9E4qemhwMKwGT9C1pQpbwMK12Qkvpao2qb133vpZWGS084EMc_LGvuuHlgQyLZ3zYMS3mz8H58CRNS_OF8qDIEcLWmPyCiF14yz9Nkf2OfVHJmf7sX9pKjg0APpLY21cAJ1FxhTbmIFmeife3SSUhgq8ETAh12o50r7YA8gKt_sLbtdruMUaB_46i1OZE8hvE71TxYhT1wnqYtFBK_Rg2Dtg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f0ac308ebe.mp4?token=TQkvOVoNaxV3pRNqeoCJQHGTunO7L8N0W4pkkhe3VDHgbxa6tmG2ntSgAcN1ffZr3cHzxFArB_79OXHNCiW3QK6DSbyhTvLijxp1dTpzmql4UCEMoTg4yiITZPcDZV9E4qemhwMKwGT9C1pQpbwMK12Qkvpao2qb133vpZWGS084EMc_LGvuuHlgQyLZ3zYMS3mz8H58CRNS_OF8qDIEcLWmPyCiF14yz9Nkf2OfVHJmf7sX9pKjg0APpLY21cAJ1FxhTbmIFmeife3SSUhgq8ETAh12o50r7YA8gKt_sLbtdruMUaB_46i1OZE8hvE71TxYhT1wnqYtFBK_Rg2Dtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند طرفدار فلسطین از برج ایفل بالا رفتند و پرچم فلسطین را از طبقه اول آن آویزان کردند
شش نفر از این افراد توسط پلیس دستگیر شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64940" target="_blank">📅 19:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64939">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTcf_fIhbsdW8UZ0TOwpD1E1CyLIW_S1ap-CdmagrDux23jKHlE2z5829Dm4naOO1jGI_2vk1Guv1kAQ5YaS-9CQwhT1kwMiUp9pKB8xCOYpeWV3LtVgyQz880XyaXfrrwI6pmLKjXbxrEt8ul3NDyzG2BLsmbysAjpHCsB88jVXQ0LGwk7IcS53b2FE8jKVhlwDP9MSapTlt3rY6iDLLYeCf72xYUGhGANGvtw3VWps-6aJ3QmRQ9jHzCysnxQHaoPXQTZm40iNno85rvcCxdNo-w9jEFgRLXP96hP1seK67J8BJ7BrcLyNDSBPSABY9nw41Y-a7QPtr1G64wL7WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست ترامپ در تروث‌سوشال:
بازی نداریم! تماشا کن قراره بعدش تو موضع مورد علاقت چه اتفاقی رخ میده!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64939" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64938">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔥
🔥
آفر انفجاری امن‌نت
🔥
🔥
💥
گیگی ۱۷۵ تومن
🎁
۳۰٪ تخفیف خرید اول
کد:
AmnNet30
⏳
فقط تا پایان امشب
❗️
ظرفیت محدود
⚡️
اتصال پایدار | تحویل فوری
👇
برای خرید سریع کلیک کن
🤖
@Amnnet_admin_bot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64938" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64936">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hMxHoJX6jStB77dhGpXGmo4GGN7aRwMkbQoIIC39Sw_XcWZjpRQ8yzlBU_NoyrNLUBg-xUTn2etEkScpXj1kps0uYYzdxmbB_1yK21LlVZbQo-kaRecoX1JzqZGlIyzDsOB5llLTBmbuxU672iQIRnqrYjH44uowrSc5JoxyoLKAhyV8vDPz2r4bfeR1gJG_5_uc7plGv4_dqicjfQGdZPag7FqJhswXmejTG3kL2-2nndM2UtKVaq2MqkPYazfS7oUU5ApyJQQFmkmhSncAh8UW1QCXMADfvdBUQ0wLwi8Y6qMvRBxZ1j-YBi4H_gIFEpFhB7Ovq1V3qBkp5fkYgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qWh1CZzIBZBotQOY6KBxssRnRjlddZv8NjfQ0Vp5c2EGMlPP3pv3ncX-wgGVDqOLzkukyzZxhwcTPwDVi5SWH_EmQskb-xyxSA-HCRGk2eVIe5k2rMXOsm5ghI-KMkGLnEEREmccr88IvfGqBkX1VTah_Y9QO2lzU7S8pducC5zmoedlp9VZVSp2pX90W-d5jyVPM78BeFBdzAHfHxFMgkNh_O_LSnUL4u4q-ijBpNNBYUB23YvW_YHZLndKPu9r_trpbv5Dd8ZDU63RFRaeFDqDqFyKkNnwg-J4Q4uEwz3-Uo1OD1Y1tYuuds01yDBP5j3kVQAHW_u9ZW_ALMcagQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیکتاتور‌ها مثل هم رفتار می‌کنند
دیکتاتور ها مثل هم سقوط می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/64936" target="_blank">📅 10:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64935">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🇮🇱
کانال۱۲ اسرائیل گزارش داد که در اسرائیل برآورد می‌شود دونالد ترامپ در ۲۴ ساعت آینده درباره اقدام نظامی علیه جمهوری اسلامی تصمیم بگیرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64935" target="_blank">📅 10:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64934">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">عه امروز واقعاً روز پسره؟ روزمون مبارک
🕺
#hjAly
‌</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64934" target="_blank">📅 10:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64933">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePl12sYcwl5uWaODvR4wdtWEturuPHdEP8Cl3PGZVpbXDt52LggR8TU13aFzcwCCUz-_smETqjkgQxJcPu0-WtoivZbY27mfdjlUSmRNLDrxYTCohT1GQb0Xls-LvKejDGcsVBuHgnA03S-D0OZwkP4q971n7P2vwnbXElF3eQIZRxwx1Xv_PugEKJP8tAn9GK9RvyhsXxyzuuKEcdNuKjIpMbSqtQEjqqLy-5X1fvgkNh5CL7U-nmAzfssfu2QhMG7MVCUfmp0FFDdPVrQU-4cbZZhLKvgy6y-AZ_34YAB8XjhvKw2JI3M8Z7fz9xoN8lz4S6p9EGbxe9YVUVaU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزالدین حداد، رئیس شاخه نظامی حماس کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/64933" target="_blank">📅 22:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64932">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=sOgbZhghC2CsFUpkQ7fLih9zrFcGF8Jpn6-sXBLWVRwMYIhaEvpWUojBJoklC_qUH5uCWRIMT0T-vPInbZLksKh3ri8JkkM8-Hsm5mUtZkRGNeWyzcdfK0qK62PsWFeqlJ1eW4Nv7yCB_p198Fl2zN4zP72o6-Eoi3aDMKWhDq67ui-F5Yx_Fba17RaVPY0hRYnr3MNAPWDlaBv0Gj3WHZnoJA160xdA-LT1F1nNzgZiw9_jJcYoeN2MwjDYwMgir6owFXsL82t5fB9w0gw-955yvGV0MGfjkjuvBWuzuOFggjpHAB64_Xii3pV1uWMwnC7D05xQZ20GqHeh840bxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=sOgbZhghC2CsFUpkQ7fLih9zrFcGF8Jpn6-sXBLWVRwMYIhaEvpWUojBJoklC_qUH5uCWRIMT0T-vPInbZLksKh3ri8JkkM8-Hsm5mUtZkRGNeWyzcdfK0qK62PsWFeqlJ1eW4Nv7yCB_p198Fl2zN4zP72o6-Eoi3aDMKWhDq67ui-F5Yx_Fba17RaVPY0hRYnr3MNAPWDlaBv0Gj3WHZnoJA160xdA-LT1F1nNzgZiw9_jJcYoeN2MwjDYwMgir6owFXsL82t5fB9w0gw-955yvGV0MGfjkjuvBWuzuOFggjpHAB64_Xii3pV1uWMwnC7D05xQZ20GqHeh840bxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار
: آیا آخرین پیشنهاد ایران را رد کرده‌اید؟
🇺🇸
ترامپ:
نگاهش کردم، و اگر جمله اولش را دوست نداشته باشم، کلش را دور می‌اندازم.
🎙
خبرنگار
: جمله اول چه بود؟
🇺🇸
ترامپ:
یک جمله غیرقابل‌قبول. اگر آن‌ها بخواهند هر نوع برنامه هسته‌ای، به هر شکلی، داشته باشند، بقیه‌اش را اصلاً نمی‌خوانم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64932" target="_blank">📅 20:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64931">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
📱
👑
آی‌پی های جدید برای فیلترشکن شیر و خورشید
🛜
‌ ‌ ‌ همراه اول
2.22.250.149
23.58.193.140</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64931" target="_blank">📅 19:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64929">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">همه‌ی اعضاء هیأت آمریکایی قبل از اینکه سوار «ایر فورس وان» بشن و پکن رو ترک کنن، هر چی که از میزبان‌های چینی گرفته بودن [هدیه و یادگاری]، همش رو همون‌جا انداختن تو سطل زباله.
دلیل این کار احتمال جاسوسی بوده
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/64929" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64928">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5O7j9WJho5ATcBjB5C6VEwW3wjnMctk2fVWKaS4W06fSFuQRZ2hq7_eLaqvk0gt190hFOJN5p5EGzZGgrjzIzZIx8WQWnHMgNIl2J_PoGoqn3oUTC6UfzycJkTaT0AlCJmDuejGvzcFNViwN3f0Djt2OSBJc79HNZOA7i9mvrHJzUrewn94u8DfHcw5t2qC0g0R9nQL99dqGFcmB2I1I7hbBJHnACFC1C1Ry3nsvOcGlt6k833s7J-hNhoqzkm9WMskMYSDYUyvRZVwJiOSsBPxQoLD0trPtV5VTn2yddFB8wDYMKmym246o5MtpVGHpFOK9MgLPlBOacymo0vZfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/64928" target="_blank">📅 14:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64927">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: تعلیق ۲۰ ساله‌ی غنی‌سازی باید یک تعهد واقعی باشد  @News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64927" target="_blank">📅 14:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64926">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم  @News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64926" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64925">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم
؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64925" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64924">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تنها هدف حاکمیت فعلی، رسیدن به اولین شرط هست و بقیه شرط بیشتر نمایشی هستند برای بستن دهان طرفداران، چون به خوبی ‌می‌دونند که ترامپ، اوباما نیست و تا زمان انجام توافق، قرار نیست تحریمی لغو شه یا اموال بلوک شده آزاد شه!  منتها ترامپ به خوبی برنامه‌ی جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64924" target="_blank">📅 14:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64923">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
ایران از چند روز پیش منتظر پاسخ آمریکا به این پیشنهاد پنج‌بندی بوده، طراحان این پنج‌بند فرماندهان سپاه از جمله جعفر عزیزی با مدیریت احمد وحیدی و تایید مجتبی خامنه‌ای بودند، طبق گزارش خبرنگار ارشد الجزیره، تمامی این پنج بند توسط آمریکا رد شده!  جزئیات پیشنهاد…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64923" target="_blank">📅 13:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64921">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UnKK3lQ9zqWm6icpcy5CS3ioJfm0dLcfp2wRHdXi2uJMc8oyNhqjHu4QXwWdUACOcqGwo7lzkWNQ_d_A5Q_bOorS3o24PVf8-zgy0wN8p7qWgifZyWd0gH5DgQS8znDYekbT1iwISrvWBanbJ683SMFqxsdwZGaP6P452-H-y_hbU0G-p1ylkm8iQc4R3NRSp3m7l4aoiWIgolRqz0Cp5EaeGm_mwyxHBpmjZGBS25477iSA-cIiB1Sg1LXLASR6bchz6rY5_zBAGMlOJ5ymSigwL8wMWjjKPzUJe9UZDEkqHORfhszh-FQlL7_OKclIEHzeKfVW4Lnct1cjdrFnSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TNyvLezJXmhTn50Y07BqpoTKtBC_-Ff3qzPSAfMqwDMtFSCAs0-H0_JCrwKdvPni5Sovr2a6Nz8_6rHg5a5gMrYvOftGoD0scs8DvLHIUX8JJFzHQDZyRX0_vlrMYh-ocH2EJIfJnMQsXOPkbYIZgG7_-YjsTWNjPHpAe5uv07T0TwlChXnU66-0gsqHf4uIh1ApDbx9grM4Nbo2EWbpCeKPtCzAG7rrtr4JU9aJady75fyMvXcrvcFhbD0HxVwQbtOATgcloWAEojwe9hkK-8GS1cY1xxsD2gj1fellSZYa3DhEg_AEqrVDzUelQMUZ6Bzg2k0Z09IuRRTVdraQBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
#مهم؛ الجزیره: پنج بند ایرانی ها توسط ترامپ بطور کامل رد شده‌اند، مجتبی خامنه‌ای دستور داده بود در صورت رد این پنج بند، دیگر وارد مذاکرات نشوند  @News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/64921" target="_blank">📅 13:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64920">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2jOzr57zCtuO16RreMamhBVilSKzV5vGqgvA5-9K3vaMHYNpAVHDmhyJyw8QcQ7M4N_1EF0Wz9ix6QKIymUIcPKdSwsE63FQHsM6s20CSouQoJcgInWiclDrY_13UwIlhhgToma_hXMo6hL9sgR5i7kYwGhzIymyMANSyOIYIjleG-Xua78FzQYU35xLxlmvgHoMpylx1-WcECPiKyDVt_FKjgjvuhRjo0VU2BK5vVV0mfPGsIGxlduTVd3jxR3N3zHuC9t7RYg6crcmTZAO_OIlQ6sRx_RIEtKxOxLkvXKPhjOqtMtB8SbZnI0I1c0cqr7UDQOg2SU3qiFM76qsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#فوری؛ علی‌هاشم خبرنگار ارشد الجزیره: یک منبع آگاه ایرانی به من گفت که تهران رسماً پاسخ آمریکا به پیشنهاد ایران را دریافت کرده است و واشنگتن شرایط ایران را به طور کامل رد کرده است  تیم مذاکره‌کننده ایران پنج شرط را که باید قبل از ورود به مذاکرات در مورد…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/64920" target="_blank">📅 13:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64919">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇺🇸
ترامپ:  امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند. می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت. هر کاری…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/64919" target="_blank">📅 12:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64918">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🇮🇷
عراقچی: پیام‌های متناقض آمریکایی‌ها مهم‌ترین مشکل است، هیچ راه‌حل نظامی‌ای وجود ندارد و فکر می‌کنم ایالات متحده باید این واقعیت را درک کند. آن‌ها دست‌کم دو بار ما را آزموده‌اند و اکنون به این نتیجه رسیده‌اند که راه‌حل نظامی وجود ندارد!
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/64918" target="_blank">📅 12:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64917">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭 𝐕𝐏𝐍 ]</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.14@HotVpnPlus.apk</div>
  <div class="tg-doc-extra">23.9 MB</div>
</div>
<a href="https://t.me/news_hut/64917" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
👑
یکی از فیلترشکن هایی که گزارش اتصال خیلی بالایی از اون میاد، فیلترشکن غیررسمی سایفون بنام شیر و خورشید هست، دقت کنید این یک ورژن غیررسمی هست که تعداد زیادی از کاربران تونستند با این روش به اینترنت بین‌الملل درستی پیدا کنند! در آخر پست لینک دانلود این اپلیکیشن قرار می‌گیره</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/64917" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64916">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭 𝐕𝐏𝐍 ]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9ZwyiMDDVpxZiFy0J3u3pPermqFwnMiG5EHym3MI95qUaUIM8vpbAAvb1Ydyolw6TUeuUkQ0BPKLJbLnVwCvzdeDjnr5E453F9fY3HKppa2Jsq7Bvay2NXnoVRsf0PE_F15F_iMH_eGp8H2MNyqA5bHFdcj7y5QMkx9ybw-f0mpaRvG4phubyYbHH_h7mXwT9-nDEjms_HjLkm_AAhy6Up_avirxjhnwyHFnqqmZ0HE8IoC6tWeAt3oQLl_SAYRjIivdVpLmRl7VTbLr4Y1JqsrPdwqFn_-dbgIVyjYiArGS6yk_zUG8gQdOJGV3abVALzrbLi39tJ1HL_-yPelUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
👑
یکی از فیلترشکن هایی که گزارش اتصال خیلی بالایی از اون میاد، فیلترشکن غیررسمی سایفون بنام شیر و خورشید هست، دقت کنید این یک ورژن غیررسمی هست که تعداد زیادی از کاربران تونستند با این روش به اینترنت بین‌الملل درستی پیدا کنند! در آخر پست لینک دانلود این اپلیکیشن قرار می‌گیره
👑
‌ ‌ ‌ وارد فیلترشکن شیر و خورشید شوید
[دانلود فایل در پایین همین پست]
1️⃣
‌ ‌ ‌ بعد از اینکه نصبش کردین و وارد شدین، از نوار بالا برید تو قسمت OPTIONS
2️⃣
‌ ‌ ‌ تو مرحله دوم وارد قسمت آخر یعنی More Options بشین
3️⃣
‌ ‌ ‌ تو این مرحله برید پایین تا گزیه Connection Protocol رو پیدا کنید یبار بزنید روش تا با صفحه جدید روبرو شید
4️⃣
‌ ‌ ‌ تو منوی باز شده گزینه CDN Fronting رو بزنید و برگردین عقب، دقت کنید برا بعضیا تا همینجای کار رو انجام دادن و برگشتن به صفحه یک استارت رو زدن وصل شده و برا عده باید باید آی‌پی هم وارد کنه که در ادامه می‌گیم
5️⃣
‌ ‌ ‌ تو مرحله بعد باید یه قسمت برگردین عقب و وارد بخش CDN edge IPs بشید
6️⃣
‌ ‌ ‌ تو صفحه‌ی باز شده باید آی‌پی های زیر رو وارد کنید، دقت کنید آی‌پی ها مدام آپدیت می‌شن و آپدیت های جدید در داخل کانال قرار داده می‌شه، تو این بخش کافیه یه آی‌پی وارد کنید و OK رو بزنید، حالا برگردین به قسمت تصویر شماره
1️⃣
‌ ‌ ‌  و روی استارت کلیک کنید تا وصل شین، دقت کنید بعضی از آی‌پی‌ها hostname دارن که بدون هیچ مشکلی تو شکل شماره پنجم، host رو تو قسمت دوم (پایین فلش) وارد می‌کنید
🌟
آی‌پی هایی که فعلا موجود هستند
:
CDN SNI Hostname:
python.org
151.101.64.223
151.101.0.223
151.101.128.223
151.101.192.223
92.122.123.128
2.16.186.20
2.16.186.31
2.16.186.44
2.16.186.58
2.16.186.69
2.16.186.81
2.19.204.19
2.19.204.87
2.19.204.137
2.19.204.144
2.19.204.145
2.19.204.170
2.19.204.184
2.19.204.185
2.19.204.202
2.19.204.210
2.19.204.211
2.19.204.217
2.19.204.218
2.19.204.225
2.19.204.232
2.19.204.234
2.19.204.240
2.19.204.249
2.19.204.250
2.19.204.251
2.19.205.8
2.19.205.9
2.19.205.11
2.19.205.27
2.19.205.33
2.19.205.34
2.19.205.40
2.19.205.41
2.19.205.42
2.19.205.49
2.19.205.50
2.19.205.58
2.19.205.59
2.19.205.64
2.19.205.65
2.19.205.82
2.19.205.83
2.19.205.88
2.19.205.97
2.19.205.98
2.19.205.105
2.22.151.4
2.22.151.9
2.22.151.12
2.22.151.13
2.22.151.15
2.22.151.17
2.22.151.20
2.22.151.22
2.22.151.23
2.22.151.32
2.22.151.36
2.22.151.37
2.22.151.39
2.22.151.47
2.22.151.51
2.22.151.53
2.22.151.54
2.22.151.58
2.22.151.60
2.22.151.62
2.22.151.135
2.22.151.138
2.22.151.139
2.22.151.141
2.22.151.142
2.22.151.143
2.22.151.144
2.22.151.146
2.22.151.149
2.22.151.150
2.22.151.151
2.22.151.152
2.22.151.153
2.22.151.154
2.22.151.155
2.22.151.156
2.22.151.157
2.22.151.158
2.22.151.159
2.22.151.161
2.22.151.162
2.22.151.163
2.22.151.164
2.22.151.168
2.22.151.169
2.22.151.170
2.22.151.171
2.22.151.173
2.22.151.175
2.22.151.179
2.22.151.181
2.22.151.182
2.22.151.183
2.22.151.184
2.22.151.185
2.22.151.186
2.22.151.188
2.22.151.189
2.22.151.190
2.22.151.191
2.22.151.193
2.22.151.194
2.22.151.195
23.32.5.18
23.32.5.44
23.32.5.71
23.32.5.96
23.32.5.118
23.32.5.141
23.32.5.167
23.32.5.193
23.32.5.214
23.32.5.236
23.53.35.146
23.53.35.158
23.53.35.171
23.53.35.182
23.53.35.194
23.53.35.207
23.67.253.24
23.67.253.55
23.67.253.77
23.67.253.101
23.67.253.120
23.195.81.72
23.195.81.84
23.195.81.96
23.195.81.108
50.7.5.83
63.141.252.203
65.109.34.234
92.122.123.128
94.130.13.19
94.130.33.41
94.130.50.12
94.130.70.160
95.216.69.37
96.16.97.82
96.16.97.104
96.16.97.126
96.16.97.148
96.16.97.169
96.16.97.191
104.124.148.191
104.124.148.203
138.201.54.122
142.54.178.211
144.76.1.88
184.26.163.12
184.26.163.24
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
184.24.77.29
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
23.48.23.186
⚠️
‌ ‌‌ ‌ دقت کنید با یکبار لمس همه کپی می‌شن فقط اول ip هارو رو از حالت خلاصه به حالت گسترده تبدیل کنید تا همه قابل نمایش باشن، و داخل فیلترشکن باید تک‌تک بزنید
👑
‌ ‌ ‌
لینک دانلود جدیدترین فایل فیلترشکن شیر و خورشید
https://t.me/hotVPNplus/9
@HotVpnPlus
|
@HutNewsPlus</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/64916" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64915">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=N9AkMWCL1x-cXu2YyeoahIR1O_jddLeuZ_Vhu8wkXegop1I9alTmudOQGJAzDYgzB6m8WDezesNU0MBDXLSmtnoc3aJOkxn0485_mZwyhwDu8lmpkM-Yj8c8OEAdsX1Y4bZ_CTfWdsJy4_WktTYgFyMvY0jXnjDtls05X_u4tC08U6N_nJ_TcjBwoEm7z2NNdKt0PReK_MPfc1enI3NuPoUl6vDBG1d7p7VTd10ceYXoSH0WUo4Q9TzlZerLNk0I_mqv-uZYp5fnTxQCExeaCf69tjjhY_9b6OXcyqBlfzcFh0Vmu6ZvziRQXKLdOZlVHJ8F4hInHJRLLX8c7Kgssw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=N9AkMWCL1x-cXu2YyeoahIR1O_jddLeuZ_Vhu8wkXegop1I9alTmudOQGJAzDYgzB6m8WDezesNU0MBDXLSmtnoc3aJOkxn0485_mZwyhwDu8lmpkM-Yj8c8OEAdsX1Y4bZ_CTfWdsJy4_WktTYgFyMvY0jXnjDtls05X_u4tC08U6N_nJ_TcjBwoEm7z2NNdKt0PReK_MPfc1enI3NuPoUl6vDBG1d7p7VTd10ceYXoSH0WUo4Q9TzlZerLNk0I_mqv-uZYp5fnTxQCExeaCf69tjjhY_9b6OXcyqBlfzcFh0Vmu6ZvziRQXKLdOZlVHJ8F4hInHJRLLX8c7Kgssw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند.
می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت.
هر کاری که در چهار هفته گذشته انجام داده‌اند، در یک روز از بین خواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64915" target="_blank">📅 10:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64914">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
📰
کان نیوز:اسرائیل معتقد است که ترامپ پس از بازگشت از سفر چین برای از سرگیری عملیات نظامی علیه ایران تصمیم خواهد گرفت.  مقامات ارشد ارتش اسرائیل و فرماندهی مرکزی آمریکا (CENTCOM) در هفته گذشته درباره احتمال از سرگیری عملیات علیه ایران گفتگو کرده‌اند. بحث‌ها…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64914" target="_blank">📅 10:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64913">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/uR-Vi_lulPsNPTjHoZ0uJ-rvw3lTeNfrK3cG9ifQLrNuWoQV4a6InEthuzuoFeEmkYVdIxAQAFW_aUur55g0ZrA0QV8hnet5TAgz1a_O7Ixu-h_sZ3mBIvnIcgwX8e2r9yuGGPYOcQmWhsuh6O8wWBz1kh2F-qj9s96_wl_o2PBp3rMmoccbEY1FUpOnLUiGNfetctBCkNNcAvjXVApga7NH7yfv50_2I4Id1Czm4A7NUOLXACMcf_-oZkawRe-sPPdk2J176Cl6Z5MtmYpbZ5oxhv58f6dnfaOd3_0VmB7LAhSgzXiCf_tMcBdM72-Y7dpECuIHboQOnrExLKudww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/news_hut/64913" target="_blank">📅 03:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64912">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltKMuEmFE2q7MZNdUsfscxNYtuGGS5fnkka6ilY98V3mZM8OR2muNZ4nmxemhXSQxr_9L4mNPOEDuRjH90aTTfMxYRPx6dC4Iz-lhC8q4uulTqKCA7oHi8hWFfft8yBWS891hF3TQhYXekkqHo0u5C-s1poPKDXZHD878FSj6ev0PrkUmoGsYfz0qaGpKQPYnBi3CHky27_ct8xIA48SYG_cxj9alEGsy8T05hFG2nyHpG-efCtlC5XLXdjB8dTCuhz3crq0gpp8IeL4A5BFFkTjbtuYdJFqxEquZONP3f24QYhEWxLGu7LKSEHxrQvxriLyerdCh0GpCK7mwQy22w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی؛ نماینده‌ی مجلس:
دولت قصد داره میزان سهمیه ماهانه بنزین ۱۵۰۰ تومنی و ۳۰۰۰ تومنی رو کاهش بده و قیمت بنزین ۵۰۰۰ تومنی رو هم به ۲۰۰۰۰ تومن برسونه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64912" target="_blank">📅 19:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64911">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=TuKxhkHOj3whK4hCqnZ2oDTYIHripyl9VF7NNWXHd4neMJGckNiGeLob4YbEaTFIapCPKG3kiEllS2lICAYVZI3ywrmr4zGsYP2vvCxox7cwQGknEMHRLuHtXr4bMaknkpC3aU9e_53lqslQUnnyC4yoikkF4cWxNlPKx4PKgeL-GJRIfXVlN4MV2ODLmyL1P0PV9A5gJhrAEPvtTHIx8h-DgGFl1XFcT1C9j39lAqmBNU2WuKaZ4_X9Wmqm73l54JzFy-geD4QzIPZfq1LbmzNjSqobrFjfeCdZMVZFMorNnstCCHW5J_SKcdCGbK2rhnSWAPt2KUtA82xPeqYPhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=TuKxhkHOj3whK4hCqnZ2oDTYIHripyl9VF7NNWXHd4neMJGckNiGeLob4YbEaTFIapCPKG3kiEllS2lICAYVZI3ywrmr4zGsYP2vvCxox7cwQGknEMHRLuHtXr4bMaknkpC3aU9e_53lqslQUnnyC4yoikkF4cWxNlPKx4PKgeL-GJRIfXVlN4MV2ODLmyL1P0PV9A5gJhrAEPvtTHIx8h-DgGFl1XFcT1C9j39lAqmBNU2WuKaZ4_X9Wmqm73l54JzFy-geD4QzIPZfq1LbmzNjSqobrFjfeCdZMVZFMorNnstCCHW5J_SKcdCGbK2rhnSWAPt2KUtA82xPeqYPhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ی دست دادن ترامپ و شی
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64911" target="_blank">📅 13:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64910">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVsgwLD1m7tXVBVweNRGlHLzwN3UG6rEim1Fj-wi9HfaLmDmFabUFETFF9iEn2ljCwn8pgrZENrOMi_5h_SDfY5oiGbpArt8-TLSov3rjVLOhjAZsD_xKa4vu-oUFT4ZkTFXcAanpGFBsJbY1ojTuobNdc4ZP7D2dSsrqram-xHnBHyCdlTBvM8QtFQDhXe2XdKHz1LvnVDcOvgyydDwRz8XXWLZ0nRM96DW1iNne7hswHhNuyHoUX0fR6TEzy4SqpdWblDA5gy_wxLmk9wsJVGipwNf-0FRXbHw5wDMkjhWKDV0lB29j-IbjFuhxlLn5Nq1UJwO4ti8k_DzCs7-IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64910" target="_blank">📅 02:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64909">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64909" target="_blank">📅 02:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64908">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🇺🇸
#مهم
؛ برای اولین بار،  اینجا در کنگره امریکا، سه نفر از جمهوری خواهان از صف حامیان جنگ ایران خارج شدند و به قطع نامه پایان جنگ با ایران رای موافق دادند.
با اینحال این قطع نامه رای نیاورد و تنها با اختلاف “یک رای” رد شد.
در‌صورت تصویب این قطع نامه ترامپ به عنوان فرمانده کل قوا حق قانونی حملات مجدد به ایران را نخواهد داشت.
اگرچه در نهایت ترامپ حق وتوی این قطع نامه را خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/64908" target="_blank">📅 23:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64904">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cPqw-zRMIJvp_M4QmxLc3-VmL6XoR4KGkeu-4DREeapPzmQCgsKT7B14ya6bnZXaUACPCA0widSe29eCg6PGs-lpxF1vnvMAqPkhKEhmhkGrmvFib0uSB-fIe5amrOmzJhSv9QGNSriyzjs69e3vB9FPIeiKEilM6hiS0M1ipHl7GU13HPn4Dz01Oeq57N41uZvmIpCHlKcHl0BWl8VAJiVGWT4rQ4GCVWgsRD7wE8NAmf8w7Vt9A_nkp2H7puDl1mB1W3i4VpgUo9bj06SztmcsYRfh1epaWKb4OtdB24-sQ1Mqr3bimKIQAqHJB9MXjf1CpwbkzG1DlWtG8zgn6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LfOA1hQ3S-xJ_HqznVNTEr3D0trL5p-AeeUJeRsxF81VfozMEHRP_0SB0mFtHvZCZGSbBZXisWQufEpSBPtjeXefOXmjhgZ8AGF7SO0JQS3_pjRHN2drfgAocIVYXSedre_ajSih68hQAtG1fsBwKH08RNN3BlJhi-pDEamoTHGO6U7JG2FB-Mkjq2vKiZ5swDZCYPG-0BdMJRvPyeWc3GOaZUFaKxmD_MxLC8eTaokWEjkzBq2gXlX-CaFusipRC-SyeadOhYTy4tLBPsM6oQ00EIIhRA43tr0OHUJ8Pk24BvrWh_rZixp3yhP_4Vkxtmbrg--4waV8YZO-E4IQ-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=cMaHkmFLbDXotnSom7O0nj3LzX8E7PS9ife-zH0Xi-_VxpZlsdpn6a7ocLftKg7ZnV8iSjMiKc-K7Hylgb6sSwq2MHG-P1IWw03Gh0l_yoNPXCyU4MLz4GOM6aOtt1_82ksY-uEdXlbjmgacAzwMCBwBsR2EkJ3IvgxZ0gMqK5N5lQzuUdYmJLiXALXaGR7HM3pCONJAZ3B70HrRP7EWdiwFrW1860gm5blhPm7tU1RAepxyEmFkKC4veKdxACKHwdTLioWEoFGTQqcU26rjwSpEPnjewWYLyhqVk6mimTTeOSliEwNmu4bbQdeQ-MvHdycbf81--H1-V_SIYyTzdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=cMaHkmFLbDXotnSom7O0nj3LzX8E7PS9ife-zH0Xi-_VxpZlsdpn6a7ocLftKg7ZnV8iSjMiKc-K7Hylgb6sSwq2MHG-P1IWw03Gh0l_yoNPXCyU4MLz4GOM6aOtt1_82ksY-uEdXlbjmgacAzwMCBwBsR2EkJ3IvgxZ0gMqK5N5lQzuUdYmJLiXALXaGR7HM3pCONJAZ3B70HrRP7EWdiwFrW1860gm5blhPm7tU1RAepxyEmFkKC4veKdxACKHwdTLioWEoFGTQqcU26rjwSpEPnjewWYLyhqVk6mimTTeOSliEwNmu4bbQdeQ-MvHdycbf81--H1-V_SIYyTzdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم تو خیابو‌نا و پارک‌های اطراف پردیس بعد از زلزله و پس‌لرزه‌های دیشب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/64904" target="_blank">📅 10:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64902">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KWdlJH9qHEUgg4tcmzjLtAhY2P8YMo9oO7fLWuLAAMTDGTBkQYryuTxVwFfA16LG28lWxm0O9FJ3uFt_qtQNDmhsuoMkchfhwv3wCs4Zr2_8XafUk1a2ul6etizb3ktx3hn6UgX3L6TCPGa8s9Qzsy7No5g5KPn93PsTzP0OAFJWrj6nhEM3OulO3XyYkjEPvThPNLoQXKB8Gm4E1SSJ3CwJGV4LXHgyKfv_GIxyIAbnqy5Vwr-ucIFxVJDzQb8RRqYuI6ChFtzb0KY7SmM8-Uw2M7p4B9udu4UmIbnE9A8l9kJu8xrUbrID93CX1qfXYyiMEwVMe6wCwBbKrdtJOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UdSeXaSHRq5PHyMaK61PmnDhyKk8LUta1aiV9gO_f6TeyGPQAAVphq_vQmFDQpxiinl-q51K5irOLTWn6DaSpfqet8-NW1Qj4zRR3RtcAFaKTTMjcXrFCEr7WWKpRrtfNBLjYwCgUuQL1rySCMkN0InfL4nehnTT0svmpKfGnObR9qEe7Vb_k5nJnXpQA2eOzYMIKfpAGh-fMExs-fNzVWC-hvBJvUCF2Larvik0Aw-V9vOuTuVB9byKWHen9RXOJACeck_-zpOcpwFkHF3DvSfsolESRF3T60gy7iNculBidd1owFXsJ7L5lYL9w8nfplwdsz-HFynRpQsWfpnn0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با اعلام خبرگزاری قوه اعدامیه با اذان صبح امروز حکم اعدام «احسان افراشته» به اتهام جاسوسی اجرا شد!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/64902" target="_blank">📅 09:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64901">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
📰
خبرگزاری NBCNEWS: پنتاگون در حال بررسی تغییر نام جنگ ایران به «sledgehammer» به معنی«چکش سنگین» در صورت شکست آتش‌بس است.  یک مقام کاخ سفید به شبکه خبری ان‌بی‌سی گفت هرگونه عملیات نظامی جدید علیه ایران تحت نام و عملیات جدیدی رخ خواهد داد. بحث‌ها در مورد جایگزینی…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64901" target="_blank">📅 09:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64899">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OzqzJfMpRubDbqDVS7L5xWlxjamSAIV3OyQsocJ-JfZOS5AEJGuV7wwFFrn-9V20wjPfP8uNaMXnXO6eP9fJeEZMHvO7Ykujpp-B05Q_3rzpHRhkWEjlf1QECh2hw9mnauNA0lI4dK9gp45Tbx7ywjnTxr-y9jXJjam216KqIyqe4QPfd1XjRw75zukIahEXQNoMG01Mha3PqD4uCI_BAyC-Ct3-pKpRfvdntXWURUMzlr2RxAr7-cYcNr8l5gnmb6JG_1_YgupkyVR3iqggLvWdSBf6f4LHLjQeQry3N0sITLLjsQjyBRsA-bu01U2UFH31sVA-I8OFgIX9LOadBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBPRPKaM2_p7ktVKxP3JyIEJniWWkn12oxpeeDgBhD_uq-5UtWLP8gwjIWYiBS-zTMWiJEzrNnDA30z4a_gnbFhsaAKytRCZpBNKC3W8sfv6IJUmuqtc1o1YwYdbsVAQm9liM7pCQ_P-ge7tmStmaNRMeYP0OCCdKsPXp8PqfYcVqOhgccaGp6s0yZ9PYA0NmxXcyXyFDMIo8OB8IQGyqY-QCUE_KaR08Gsr9Dbfa0CYD0y3Z5QHPwpLjodYUMWDRJduWxJt58MHdK1uqH1NsITJB6WffzUyaKAt5V1ofYrzNbxlwVuEWrxqAfuo9lfYxizwTYcuCbL77q77ljMKaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکوروبیو داخل «ایر فورس وان» دقیقا لباسی رو پوشیده که مادورو پوشیده بود
هنوز نرسیده ترول رو شروع کردن :)
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/64899" target="_blank">📅 04:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64898">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MNkJos6WW4i8KAKgKKDlYaSr1UIITqvafLJ2xiUYL9vIktS06BRVFap4iZ0So8hLLxEEC-gZCJ1rgA9aXABBfmmwF6q5LO3fWcHZjGSAxEjUX092vFK12PX-zyADPV5bcKT25Trz6GHeWpt1NcgxyvZRwWm7YZgkZViUcNCmEHGqEO5rUZOlCt5EbkygOxCLdg2j8CGsOPAA8XhHqXlPKiFCPrxW7XiP2SsaCqH9gxxnCdiRpWcz8Kp9nAD9LuKu6U7fiBLi8-HZgHZiuEAA06e_yBnKJbMOmmoeFbHynx_c0c56juzXYXdW4b_ZejpHxgb45eja1C_hoaj-ZSYMYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64898" target="_blank">📅 03:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64897">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/64897" target="_blank">📅 00:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64896">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aDjioR-JNsAEORZwn2GyJJrmhAd_Wi1_t-CR4PVPgWLzN8B0OJEtIR3i_KJzXVYzgyQ7sx4X3-7o0MDYYUrl2AxGZh-q2J67fcpVPwyFWht9GpcmOdgbhDh5pxQOqLGJ90zF866QFwY_DLkIOSoCfjJ3NbGXROB7kJq90kswgwfwS0CzLRcOyjzIANyK4fIIN8BlqjntULqYBDj03drCbgV-e12-CqZC0meNF5YkFtSIknlWDav4TZ4dI0Lt6jMngxkenw-CKbjQv6gnWIILRdUiJQrbNj596MUOsFKzkThOOVUeShqkjV6WDl46eF6Osb3oB2pg3LSJXFErnJQolQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ قراره یه اکیپ کلفت از رئیس شرکت‌های بزرگ امریکایی رو با خودش به چین ببره  رئیس شرکت بلک راک رئیس شرکت گلدمن رئیس شرکت مسترکارت رئیس شرکت سیسکو رئیس شرکت متا رئیس شرکت ویزا رئیس شرکت اپل رئیس شرکت تسلا (ایلان ماسک)  @News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/64896" target="_blank">📅 20:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64895">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=PmO2LqEjQZx3Z_SIYaG6O0GieFGuSMgK7NP-aVw8G5JlQlvtufrbIBk-SJoiUJZFQW-3JGhddFYHhpDU5vYbYecXFcptsF6yKKoFPq5PiOF8k0g4cAbh6lrhG-uZ_FyJqzNEU-bISGZozhwtZ0bhX4xfjqez4guFrDpxwjNCNCJ99JUpvfzRTa76wGsngoBn5fLZiFvy7UtCyLF8V0Avj1P3FTPszK6Suq_FnhY_5lgv8bzNU9vMegf4wFQOyTWu-kHdnlwqH5OQEd2ceGUoXS8lPr6c8TpqmeEveOqCx26AYRtbuzFmDhehZNQOQhS4Z1jAGQa4NivNA4fm2HY4Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=PmO2LqEjQZx3Z_SIYaG6O0GieFGuSMgK7NP-aVw8G5JlQlvtufrbIBk-SJoiUJZFQW-3JGhddFYHhpDU5vYbYecXFcptsF6yKKoFPq5PiOF8k0g4cAbh6lrhG-uZ_FyJqzNEU-bISGZozhwtZ0bhX4xfjqez4guFrDpxwjNCNCJ99JUpvfzRTa76wGsngoBn5fLZiFvy7UtCyLF8V0Avj1P3FTPszK6Suq_FnhY_5lgv8bzNU9vMegf4wFQOyTWu-kHdnlwqH5OQEd2ceGUoXS8lPr6c8TpqmeEveOqCx26AYRtbuzFmDhehZNQOQhS4Z1jAGQa4NivNA4fm2HY4Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پیت هگست درباره ایران:
ما در صورت لزوم  برنامه ای برای تشدید درگیری داریم. ما برنامه ای داریم که در صورت لزوم به عقب برگردیم.
مطمئناً در این شرایط، با توجه به سنگینی مأموریتی که پرزیدنت ترامپ برای اطمینان از اینکه ایران هرگز بمب هسته‌ای نخواهد داشت، گام بعدی رو فاش نمی‌کنیم.
ما داریم یه ارتش رو دوباره می‌سازیم که مردم آمریکا بهش افتخار کنن
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64895" target="_blank">📅 19:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64893">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fX6wPW_9rxrKU2tnEvo_sgnPldjIXsXrDygE4opmS58V2NmFABg1TR_1EqPlaLeJCsFSJkM2zePqTUBMIBbglTO89nItDiZAZFKhx3Eh06zSbP4Q0E6iwr3nToTJcPzfKYUmZAoxh2-KS8f7yUM75Cwwzm-EgxfENW7CS5VNpjqgnIu2XV8Jn_TuUdo3Nf8h9Mh1b2iTCMXN57bUwZZ8rp8aiDL5Lh1eqMfjxj74BMsVOkLiR2mNfVPFROCF2Y_gCJ8eomJecVal0Lzkf8aDDu6aM-d1cYXHogi0lbzapb-uu6dxFfYKTmAsmzDQQQ32m6oYQdMN7tgmEAyxfejo0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nO7S2SnuI8BCKSDWjQQRYnzKWjFgpFdBF30dAUHYVuzUV4UnTDE8JTAw4z8CNJ5HxnAF4cOhJoMbySyJSJmttFa5yH8wqPvOAifWyXZRIyioZ7WATTVg4T_yl0uW_wJmleozo2RXXNqC2j4TOFN9e6K_iXbh37I_6WwiwgYVpZqAjE4FjVIrYX6_cXGCafRsLECYSfxwfA3X4E9KiM4iEV0mlH6UhkmVhrcf8p2r0MbPMS2bvyyk0CW2jixK4IPVMRP1o8mYUd8wk3H3mGPtyMeAmKP4ePUDFwQDBXi2_kpHSZmXS2OjU_QczRT7tPJ6LOlPQTKb7ez7SemE8X7bkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...  جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن #hjAly</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64893" target="_blank">📅 17:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64892">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBJ92E43ijPRt9NqWre3XJ9lW4a0ARuE6RWu5FcG879Dd8z7R8wrwrXSM0dASJ7kPjO3pvNtTUz4xNO9TL_uSxI66VlaV4tgSKm0TK6tZ3RweXlOIqqdHLfRiMKdTrVRNJiVTBymDnFwCNCXgb3RYUJU0WbEt4suU9rRCvmac3wSmTeGop_lRfR_9H1x8Ok1E0ou5y0_ORhH_W_kvDJZXsXrzGRlHY4Ox2o5HBU2OEkaJUzH-6iUR8HEdZJc77zzDxmzBa4_7KJkcN_EJQo_CBG9tcYjMREXS81M7VvSPMgH_4qUul3i63PhPjzkcTS4AaFrtjiYSh-U6Kt4SBRRnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...
جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن
#hjAly</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64892" target="_blank">📅 14:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64891">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=ofjy6GYQawmQOLjeF0EYB8moMKMn7sm6yHlhmpmo67YUGeFQZL0DjZJg8Zz5bHVE-caFbI4YWOYgIn4ViMfSNo24H8DYcZ14in-sGmichaUpXgHsI5nSAQDXD3s3XD9wwwwWOWhfK_HZs6O8vZrXftj8JyFWfQmNQ0Xf-2W6gb7wl258sJCQY4s8Htqa_GXHgQmruWWEvVa2n84kLbbkyWMTE1qsAwScinn8BGxRyCZ2kC1BzyI_8gYiZjDTRKLRE51X7J5bCVNSyKAAm_ug4TV-5IrdUki_A9md4xTdHPLiqFeA3Q3LPM73bM0BQBy6388o6OPwHFaV1q2p4UqCeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=ofjy6GYQawmQOLjeF0EYB8moMKMn7sm6yHlhmpmo67YUGeFQZL0DjZJg8Zz5bHVE-caFbI4YWOYgIn4ViMfSNo24H8DYcZ14in-sGmichaUpXgHsI5nSAQDXD3s3XD9wwwwWOWhfK_HZs6O8vZrXftj8JyFWfQmNQ0Xf-2W6gb7wl258sJCQY4s8Htqa_GXHgQmruWWEvVa2n84kLbbkyWMTE1qsAwScinn8BGxRyCZ2kC1BzyI_8gYiZjDTRKLRE51X7J5bCVNSyKAAm_ug4TV-5IrdUki_A9md4xTdHPLiqFeA3Q3LPM73bM0BQBy6388o6OPwHFaV1q2p4UqCeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
ملانیا بهم  گفته باید رفتارت رو درست کنی تو دیگه رئیس جمهوری پس از کلمات رکیک و فوش استفاده نکن. من هم همین کار رو می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64891" target="_blank">📅 09:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64890">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=dBtPApn42QRtKlVB0cUU_M_Skq2Ch5EmTr-4FEtR479Z8B3158s6pm_hefa9OEqiEYaZAfnRTwaK7TNpLYg9h3f_NsW_Y9SK_johds2QBYLTCjgcSdAgmhvy99LX67fY3i2dJeSdTvnnUrZtN8V4rDlo5dpU4p7k01JY1YkkiBBT3mm2spW30IKq44PLBnxKQG7ynYcyffUrSXA-0nUYpIjvTBbopMLbKxMpr74Gdmk7rrvlQIPaftWdRHQFhfpLDrE3EghH9jvogG1ogXw88dRro9LtEtixUS93gTGfoR4hb5zBovVT1lH7ECzY8tQ37Alwd5AaTGvKK_bdRxj8nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=dBtPApn42QRtKlVB0cUU_M_Skq2Ch5EmTr-4FEtR479Z8B3158s6pm_hefa9OEqiEYaZAfnRTwaK7TNpLYg9h3f_NsW_Y9SK_johds2QBYLTCjgcSdAgmhvy99LX67fY3i2dJeSdTvnnUrZtN8V4rDlo5dpU4p7k01JY1YkkiBBT3mm2spW30IKq44PLBnxKQG7ynYcyffUrSXA-0nUYpIjvTBbopMLbKxMpr74Gdmk7rrvlQIPaftWdRHQFhfpLDrE3EghH9jvogG1ogXw88dRro9LtEtixUS93gTGfoR4hb5zBovVT1lH7ECzY8tQ37Alwd5AaTGvKK_bdRxj8nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره نماینده حزب جمهوری خواهان تو انتخابات ریاست جمهوری آینده امریکا:
کیا جی‌دی ونس رو دوست دارن؟ کیا مارکو روبیو رو؟
به نظر ترکیب خوبی میان، من معتقدم که این یه تیم رویاییه. فکر می‌کنم کاندیدای ریاست جمهوری و کاندیدای معاونت ریاست جمهوری آینده باشند
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64890" target="_blank">📅 09:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64889">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
📰
خبرگزاری والا اسرائیل: هفته پیش ایالات متحده نزدیک بود حملات به ایران را از سر بگیرد؛  اما پس از آنکه مشاوران نزدیک ترامپ به او توصیه کردند که قبل از تشدید نظامی، یک تلاش نهایی برای مذاکرات را مجاز کند، تصمیم به تعویق افتاد. ﻿ @HutNewsPlus</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64889" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64888">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQMxTWUKqk2vNz5WctXHO-7EIQMwdr283_juryouk68pY9dLqOfUtPDheT5Q73sGs4bSRgR1_dQeqVkT9O1YEvGq_afLuFphqu6h_L5FGVl5MSttaz3sG4TMgoKAE0-09Z3nZSEbvcl2VvL1zOJxWu93UNm_qO3Mb8GvHDxSTxtVUTsM-fhm7AOh6Et4YtWluDPIksNFw5nUzfiMY-WMctFbNwQXmu3dEjF4u9d2MSMre3pDZbPY5jQ1C7cPaOY3B8ZA0CvTzDxbFuMmeP_aoSawqoxdqgJaqmwY5blvq_3r2zOFOj051zXPCsBhDnJvLAADZLy6VWq-SuwKxPzbyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: من بسیار مشتاق سفرم به چین هستم، کشوری شگفت‌انگیز، با رهبری، رئیس‌جمهور شی، که مورد احترام همه است. اتفاقات بزرگی برای هر دو کشور خواهد افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64888" target="_blank">📅 03:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64886">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.  @News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64886" target="_blank">📅 22:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64885">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/GNbCajibLYhj57BxEfu3fnLvFOUkLbE3tsXw34qxLkiuhlJzTZM9HwX5XigjYcXIfacokY3NUgbcv28IBXiKe8qGjvyArxTmboxP2zNmuACN02PvBK-aTq_rnARy4xOLn6sSvqjwiUEoBMaCmRlxrp8d77mG56aPardjpP0j4zDaMWmsI0q3H3SLTo3YQ8kNZCYkqAQsf9fpU5f5goJDwb5-8eiVIfrTTDhSga_O6lUN2rQE70uw2Pz4cZs6vq2DrZW11cCHNkrG6D1Cd3h7B0qpM94dvDLM1v8Bd04z40wiYvYUWXM32wqvmvOL7I4VwoysjNNe3N6xq-tzElXvIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/news_hut/64885" target="_blank">📅 22:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64884">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ به انجام عملیات نظامی فکر میکند اما ازسرگیری حملات آمریکا به ایران پیش از سفر ترامپ به چین بعید به‌نظر می‌رسد
+باراک جان
اینو که ما خیلی‌وقت پیش گفتیم
😎
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64884" target="_blank">📅 20:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64883">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64883" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64882">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64882" target="_blank">📅 19:16 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64881">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇺🇸
ترامپ: کُرد ها سلاح‌ها رو برداشتند، مردم ایران بی‌سلاح هستند
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64881" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64880">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا گفتن بیاین اورانیوم رو بیرون بیارید چون ما نمی‌تونیم، فقط شما و چین می‌تونید!
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64880" target="_blank">📅 19:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64879">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تا مرز رسیدن به تفکر اوباما</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64879" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64878">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">حالا ترامپ با یک نیروی معجزه‌آسای تاریخی بنام #محاصره‌_دریایی به دنبال حداکثرِحداکثرِحداکثرهاست!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64878" target="_blank">📅 19:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64877">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇺🇸
ترامپ: آخرش رهبرای تندرو ایران رو تسلیم می‌کنیم  @News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64877" target="_blank">📅 18:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64876">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم  @News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64876" target="_blank">📅 18:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64875">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64875" target="_blank">📅 18:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64874">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRPIPfcoKyevQ0gqQEwJWHZCKYHWGYtwtwyitXz4yZjshPB7IxFcRzg5zXdOh6eCT_Cy_W-XJSKrg5_sCdNOQy9O6PIP7RY_fG220PnAtr-7Qey54pmPXQguWMD5oiqkuTLWQ2FMePjld4mkpqs1OrCd8CEvJ8my_6Et2WQFdKAxCW0oMJf3rxFEleeBX_1VuPPA2-OBoU6Ira-mahZ9dMSI8699kISXeoJoLMVL7AX12ynIGSNuFX6qpxF40Fd3eAiBL6WKmwAm81RTodnFB7M0aNsc5aB7fOvGdrMNVFTREXYI78Fo8JjILkLpw1-MFRGHEb46oHSciySG0SMc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی بعد از اذان صبح امروز، عرفان شکورزاده، نخبه‌ی هوافضای کشور را اعدام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64874" target="_blank">📅 11:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64873">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZL1f-eSLRcyg1lFknyhHEJvACFyAnELR52IGAXMaCmjfJJPMX20Duo1NvvdUtV-dRB1QYFoe3EFdTqH1fLZIFPQbhS6TsUOD03Ok2A42GVeTuG1SxRBj8XsYYRxfRzzwG7wz3NvNavV2FNcEh8w9YHOgqi5eGYfVVhhGTqWZV4LBxo-CFp85W8cFA0qDYxnpGsSxw2wjgkwAyXZUPfRoF8s3986ijfIem_YJhpXuDwjxceWnabcwUkX6D5VBXtbVzaNZ1oCZsgxAOP78pAWvxY1cbdQDsI2JarzCx2hl_HjfOO6aR4V8Qo1E7KhW8zTtfQNZAXBa1qzY2UskCK4v9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
لیندسی گراهام:
من از تلاش‌های جدی دونالد ترامپ برای پیدا کردن یک راه‌حل دیپلماتیک جهت تغییر رفتار رژیم ایران قدردانی می‌کنم.
ولی با توجه به حمله‌های مداوم آنها به کشتی‌رانی بین‌المللی، حمله‌های ادامه‌دار به متحدان آمریکا در خاورمیانه و حالا هم این پاسخ کاملا غیرقابل‌قبول به پیشنهاد دیپلماتیک آمریکا، به‌نظر من وقتشه مسیر عوض بشه.
در این زمان “پروژه ازادی پلاس” خیلی ایده خوبی به‌نظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64873" target="_blank">📅 09:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64872">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
📰
المیادین: منابع المیادین جزئیات پاسخ ایران به پیشنهاد آمریکا را فاش کردند:  لغو تحریم‌های آمریکا علیه ایران آزادسازی دارایی‌های مسدود شده ایران آزادی صادرات نفت و لغومحدودیت‌ هایOFAC مدیریت تنگه هرمز توسط ایران  گنجاندن بندی مربوط به آتش‌بس در لبنان با تاکید…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64872" target="_blank">📅 09:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64871">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGsCFXlezjAGh0AXk6qP-d6owBBk-9F_D1HHuXuqQenT5kVG5yXobpmA7AWEqFkHVSPOpVqf5OypOZY2NcBgTH8FvkPWEiSIw4TNOQubM3gyAgSGImqTobkTWjTnr_qBgvYtpyLbkUVf5Gf23-W9GmoiERtw37QWW3f1z20FuRrZqjPoOqwRs9PsbNK8hAtYQJ6cMUds1mqSARWZxjohOlihqwkmwf7ebb_eTaj-WZwa9nqt67Hoi60Zt_l4hUc_dR4Z_W_3TVv06X42jwK_Y_n7jMleZZaOSi0MoZQN2J_KjA1bkU7AQPZZ89avvtWwVl8XpfozuwGcwpDxcHuLZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64871" target="_blank">📅 08:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64870">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=Jw-WHRkwnsQtvWAGeHeudJYc96LvBzIn0GRbRS5EwZGaeJ4JbCwBYu3Y6tJBkIEIVFudHnw6GZ8DKOaLjsaX0pDvPOyIaa8lqXk9-oyXBVvpZVx_TBBPcXo-xVPZ1fVR0LXL8YIQZqnc_syLe-nTCwXyZyln5NWgD5UcNxoP246Y6cUgqWkBppKy8Vu8xhO-Tx8Vl1Gkn6DGJ1kNCjAioA05BQu7dQZZi04CRNxUQC8h7bmNeehavwsczO63CBvfyziEpqiy_M6_qQQ9ljW1xYBofIWXySDwfwlHFY7G73Dwv9ENXrBv8k11zfMcZljZbwA9sLF5HuutjPPFzO3abw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=Jw-WHRkwnsQtvWAGeHeudJYc96LvBzIn0GRbRS5EwZGaeJ4JbCwBYu3Y6tJBkIEIVFudHnw6GZ8DKOaLjsaX0pDvPOyIaa8lqXk9-oyXBVvpZVx_TBBPcXo-xVPZ1fVR0LXL8YIQZqnc_syLe-nTCwXyZyln5NWgD5UcNxoP246Y6cUgqWkBppKy8Vu8xhO-Tx8Vl1Gkn6DGJ1kNCjAioA05BQu7dQZZi04CRNxUQC8h7bmNeehavwsczO63CBvfyziEpqiy_M6_qQQ9ljW1xYBofIWXySDwfwlHFY7G73Dwv9ENXrBv8k11zfMcZljZbwA9sLF5HuutjPPFzO3abw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو درباره احتمال سقوط رژیم جمهوری اسلامی:
فکر می‌کنم که نمی‌توان پیش‌بینی کرد که چه زمانی این اتفاق می‌افتد. آیا ممکن است؟ بله. آیا تضمین شده است؟ خیر.
شبیه ورشکستگی است — به تدریج پیش می‌رود و سپس سقوط می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64870" target="_blank">📅 05:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64869">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=B1IbJWWcdA8Rai0wHKhOtUpMpE9BdRfYIYvL_LsSNEgfEqPbY_-GHl3c3czU3B1fCc_AvoQV91PngmIsMbcXcYxhEPRVJlod0KF9tRsu2_glsVAiFBYSSQwy72pM3FKViLLEnH7iaGHO03UzR2StWir_IsT9vP8rJzN-ilKS9pTr3Eqs9tb0ORNj5DjIQtlLlaaEhErz1ZNhWRQZb7FrIy33DPb2YVIknVsvXy27C3etWwCKuVO0W6r_SVIIWwQQ6H_lHbNOTEaLHK0M3PtpWsAz7IXVvrIWbvRCCw1fbqKRdkc8lmo8md_Lg6Ei-U7dGEIaI_MYgkfdcAij2Crydg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=B1IbJWWcdA8Rai0wHKhOtUpMpE9BdRfYIYvL_LsSNEgfEqPbY_-GHl3c3czU3B1fCc_AvoQV91PngmIsMbcXcYxhEPRVJlod0KF9tRsu2_glsVAiFBYSSQwy72pM3FKViLLEnH7iaGHO03UzR2StWir_IsT9vP8rJzN-ilKS9pTr3Eqs9tb0ORNj5DjIQtlLlaaEhErz1ZNhWRQZb7FrIy33DPb2YVIknVsvXy27C3etWwCKuVO0W6r_SVIIWwQQ6H_lHbNOTEaLHK0M3PtpWsAz7IXVvrIWbvRCCw1fbqKRdkc8lmo8md_Lg6Ei-U7dGEIaI_MYgkfdcAij2Crydg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو:
در ایران، به نام من خیابان نام‌گذاری کرده‌اند. می‌دانید؟ البته بعد از رئیس‌جمهور ترامپ هم همین‌طور، چون او رهبری این نبرد را بر عهده دارد.
اما یک چیزی هست  من فارسی بلد نیستم ولی آن‌ها به من می‌گویند “بی‌بی جون”، یعنی بی‌بیِ عزیز.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64869" target="_blank">📅 05:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64868">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یک ماه و سه روز از ورودمون به چرخه‌ی سیرک‌وارِ مذاکراتی گذشت، و این چرخه مطمئنا تا روز دیدار ترامپ و شی ادامه داره [اولین رویداد مشخص شده در تصویر]، و بعد از این دیدار بهترین زمان برای آمریکا جهت آغاز مجدد درگیری ها به حساب میاد   #hjAly</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64868" target="_blank">📅 02:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64867">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aYnI6bNc8FsZmK0DAkNCtTem9tpWR-vdjyQ3oW3IRlKayXWYdjr1hD-wkBdsiW6d2DtagHvDYrj2sxNIQhCnCjdDa_Jf_N9T70nRWlt6ClA30zdy1t1jVw-MkB_xXanOuSczi2Py5UcNZHo4ezeSith1DHIFcmSjG-r6kB2hbCJCWDqIAHCm57qxIQjegD6y8-IqweZkJbIlByQoOVWEjBk8at0sjH6hg4VT5rGs15FyDKGCUyUPGmzT6sYNLi6B94s-EWwIx4Rn0eKFdObVDJwKQ6vmVQbtpufajNJJckky46qHnAHDfPk1d8KRVUJ1v-KDC5F3cqmphFr5ZwSp4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه  البته که در همین حالِ‌حاضر، احتمال از سرگیری جنگ خیلی از بیشتر از موفقیتِ مذاکراته، آمریکا بعد از خارج کردن اورانیوم های ونزوئلا، هدفش دقیقا انجام همین فرایند در ایرانه و با…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64867" target="_blank">📅 02:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64866">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pgPvBdFPIGoK3jazxwGf-n7htiNiAQtgapjkh13RwEcZT_-iYRJkfJqjCZudMO0pug-8UQAkDLzeGBS-k3rUTOYdW0gVlTgXsxsOLfLo_MWSksO9DMIdqtzu_A4eM0G3r7N0kAwWlpuwGsa-rMuK7XkJnof1bwdHDHRKaTTrYLx5ZE_E1_ZhULmMhSHktUcx2Wfx_I2jKGohEfSm0K5SicWN2UKM-sm9odHr7ilGUb9glU8mueYtztxwTUhncK0tQ9QkzQHEZcXIdIAgrrTPIXi4QQZ_HV6cfjl1bQZKxW8Uv3qcFW-4ykKLbdCMyz868khAJPI-wF6KlJo8hZnBRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/news_hut/64866" target="_blank">📅 02:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64865">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qa8whobo7vvkCjQQBJTTPfvJkO5msLdnYOU8rNuw1QdGFxMkUoQS2BZSxj4nHKkwrBRtbGglI3muLELWEBbuGoV-wfOah_VMev78y990fIsFI1bTXfD1s_VG1gbFtBPjii1QY8kV0gcDYQpdDLDjZQxotjgDOmdtHwFoEcBOfXOafHLb_VIxjr814D6vQ6GVrLAIcEkaUZusc97zwvVSDFWvoI02bsIw63Epa2nOe7yFiCsGLkhGuQPv7WzzEvboFjADeXcaI8zNEDxkHMzPMzSIuRK2QVqjaWMJ4diBwYv5W3jXlSPn90CfA96q22M9C0VLe6KTQqgXjitjlWkyrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریم به دو رویداد مهم نزدیک می‌شیم  ۱.اولین‌دیدار ترامپ در دوره‌ی جدید ریاست جمهوری خود با رئیس جمهور چین ۲‌.آغاز جام جهانی ۲۰۲۶  می‌شه گفت عملیات آزادی که ترامپ استارتش رو زد بخاطر دیدارش با رئیس جمهور چینه و می‌خواد حداقل وضعیت تنگه رو از این آشفتگی در…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64865" target="_blank">📅 02:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64864">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم   @News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64864" target="_blank">📅 23:57 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64863">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خبرگزاری فارس: مولوی عبدالحمید همکارِ نتانیاهو و ترامپه!
@News_hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64863" target="_blank">📅 23:54 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64862">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qt5oGw-dGkFbzVYXtZZSoMMt_ok7RkkXQqPaz4DaYFLX857XP2kC1xK7Ohl0DBknYpsV71-sgBcU9pnAwhslb8QkSjzMM3a5Tn1gR0cb0TC55ydXQ8OIlXb4qPxrGXz4sLsS6z_i8fuSncS-fsFYvTvocnBgvVOK4OawkBFVejYaRO714Xcf61iNVqylgNEyo5GlU1Fa0aHeKYbCRevLk-bs3YJEXMpN9axXXd5WsbysnESpDyngVv7kaJaeOHVSCbXWHRvPFWtCa5q0QY8UQ1QICKxijdAMH96BmaGcv_1hR60Nq_BKC5s_XI_8hhiYKbCm04fRjqpicBnkglL5NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64862" target="_blank">📅 23:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64861">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بعد مدت‌ها دارم ال‌کلاسیکو می‌بینم این چه کصشریه کاپیتان دو تیم وینسیسوس و پدری شدن یه زمانی کاسیاس و پویول بودن ابهتی داشت بازوبند
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64861" target="_blank">📅 22:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64860">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=Un41FcQIXaai38NDsO1pR7VvaamqDtNGDKbgCtu7AD1O9lpfjS-dkWR18RqL5qhJkaFdwlGc4ihysUYGa6O--1tOBA8M50HgoTfe426FARHwgqy3RN608xK7yO-e9d4KOVnPtp0BhUUV_gPIB_hLvBSiVUHt8YCe1sLvB8bPULHTkxXLvHLsXtzpSwMnLInPP01zCV2Sf2ZhFZy3I6R2AMylObuW4LZPfTx-y4PVUHC87wguLv6zPteNM95cUyFelwgprttfHzfZTm41608tqHbI_Rum1sD-3Br5n-pmrySbrlD_RtiIgi_SkMpZt7AglF4WysDqEkpvfZyc58Qmrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=Un41FcQIXaai38NDsO1pR7VvaamqDtNGDKbgCtu7AD1O9lpfjS-dkWR18RqL5qhJkaFdwlGc4ihysUYGa6O--1tOBA8M50HgoTfe426FARHwgqy3RN608xK7yO-e9d4KOVnPtp0BhUUV_gPIB_hLvBSiVUHt8YCe1sLvB8bPULHTkxXLvHLsXtzpSwMnLInPP01zCV2Sf2ZhFZy3I6R2AMylObuW4LZPfTx-y4PVUHC87wguLv6zPteNM95cUyFelwgprttfHzfZTm41608tqHbI_Rum1sD-3Br5n-pmrySbrlD_RtiIgi_SkMpZt7AglF4WysDqEkpvfZyc58Qmrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اونا دیگه نمی‌خندن
.
مجتبی و فرماندهای سپاه:
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64860" target="_blank">📅 22:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64859">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)، و سپس بالاخره وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» رسید. او نه تنها با آنها خوب بود، بلکه عالی بود، در واقع به طرف آنها رفت، اسرائیل و همه متحدان دیگر…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64859" target="_blank">📅 21:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64858">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-MkJ3MZPwZeAZDGWtrHfmEjj1a1hErYY3v-bm7HF4AoER2rp-g9fLmPILMrSBJIQ1UsKqcWqjtbWbLPasgfBEVJKA-_4DvATnN0Tpz27omYPe2hwwaOidD8n1We7chLoxz78QaCQsU4S9xvNSVwh2jhZbwoRoRAWjVRMFz3EMoBUw8_5enSl3mFwWx-DMS1_AkusKEgGgmK-YFOEf52tymvTNVCQ9T8py0yXAarB1NUsLIuNFdiaQyCTihnQpVdC77r-f6Y6tFj7inz6EJDobZBugpNrE11Bz7jocP9Jnbjr65UWsJjTLOUhg6WAxDsF-vOrkG0F4NpPagBiQ2k1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)، و سپس بالاخره وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» رسید.
او نه تنها با آنها خوب بود، بلکه عالی بود، در واقع به طرف آنها رفت، اسرائیل و همه متحدان دیگر را رها کرد و به ایران یک فرصت جدید و بسیار قدرتمند زندگی داد.
صدها میلیارد دلار و ۱.۷ میلیارد دلار پول نقد سبز به تهران منتقل شد و روی یک سینی نقره‌ای به آنها داده شد. هر بانکی در واشنگتن دی سی، ویرجینیا و مریلند خالی شد — اینقدر پول زیاد بود که وقتی رسید، اوباش ایرانی نمی‌دانستند با آن چه کنند.
آنها هرگز چنین پولی ندیده بودند و دیگر هم نخواهند دید. پول‌ها در چمدان‌ها و کیف‌ها از هواپیما خارج شدند و ایرانی‌ها نمی‌توانستند خوش‌شانسی خود را باور کنند.
آنها بالاخره بزرگ‌ترین ساده‌لوح را پیدا کردند، به شکل یک رئیس‌جمهور ضعیف و احمق آمریکایی. او به عنوان «رهبر» ما فاجعه بود، اما نه به بدی جو بایدن خواب‌آلود!
برای ۴۷ سال ایرانی‌ها ما را «آزمایش» کرده‌اند، ما را منتظر نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای کشته‌اند، اعتراضات را سرکوب کرده‌اند و اخیراً ۴۲ هزار معترض بی‌گناه و بی‌سلاح را از بین برده‌اند و به کشور ما که حالا دوباره بزرگ شده است، می‌خندند. آنها دیگر نخواهند خندید!
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64858" target="_blank">📅 21:30 · 20 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
