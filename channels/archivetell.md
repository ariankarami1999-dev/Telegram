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
<img src="https://cdn4.telesco.pe/file/YuSlRbZGYlrwGtrJXIYHhseK9nZoBr9bmHpHQYCqWK4gKe4EtLqAiVAmRV4xXJkw7k8KjCzbvruEg7BjomooXEGWm5pmIqbUr2GbHaNcC2YFo76KZa5ELczK3hkcVLMN2BiWbebpHTLqEzY82CRYm-Om-ZhQkqchQXF5C2NWSoAXScx8nRL3ZsxggXPC5JmPIXomWX4rqd3tcFQH_BIDFTOiJX908IlDvVNWfkgbeDrU1aYvqcKl56_FwaF1jHD8OIAz0KqUknegn1VrZo3TfrMTW-DxdlrZbz3WUpmrtX03oZeJy0EL-7-SYyKbSpdz8HK2KBZLR_MgMRAPr84-UQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 22:23:04</div>
<hr>

<div class="tg-post" id="msg-7714">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPRIMIUM STOR | KYC</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GooYm63CNndqdmKA7jT59SgqFFW50zeZeu485cusCsHZ6Ab1rctJtAi0eVWrGR0kmqK3WAWgzoTS2z0YubpCJ4Cj43oiH30AIE7_kjmx-6F_3GdRHHsSU4zbaa5DCHB3Gswfy9FFlJwDza05EC0iHsWYNq9fF61a3f9k2OztH5xL1OGHQHI2s8Y1nZIVISJ9Yg0mpQs1GZ2MmNWxrzMSwewwsLtzlBny1wEpSNXtbkIlFxSKOiqHsw6gxQ0-2YfgLF450wJae8ElSUsSKBhNRsXH6r4g5lDa9z5Bj33Ci4KPp1gxwk-Brm-YoXQnDzyP1Nd8ScKyn-u3KZNTVQ0TDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش اکانت جمنای پرو 18 ماهه مخصوص کاربران چنل ارشیو تل
موجودی محدود!
این افر مخصوص مخاطبان چنل ارشیو تل هستش!
فعال سازی روی ایمیل شخصی خودتون بدون نیاز به پسورد و لاگین
18 ماه جمنای پرو + مزایای زیر فقط 1.5 تتر
5 ترابایت فضای گوگل درایو
آنتی گرونیتی+جنریت عکس و ویدئو(1500 کردیت ماهیانه)
سی ال آی اکسس
1.5 تتر
خرید از:
@PRIMIUM_STOR
علاوه بر جمنای اشتراک سایر هوش مصنوعی ها هم موجود میباشد</div>
<div class="tg-footer">👁️ 374 · <a href="https://t.me/ArchiveTell/7714" target="_blank">📅 22:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7713">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 379 · <a href="https://t.me/ArchiveTell/7713" target="_blank">📅 22:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7712">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhwccVpbUAAX4xpVzq1WqUcke9HUMPpLvVhXiudWrZ0e22jh8yE_jxrBnpTyjRjHSxhpJtf39JTO-KNwF58tpfRygW2a91bgjG6hq5zM4cQJqJtq7sr1CZATmqhg3XcNkkXlh6Mkhk-qLgp-FQKEan1KzkYj0Sf0YSGFH0j7NeN7mFIi5iTZBBJUeZzLjYrRqZeI6C6t9gh0_B_Smdp6pvIooigsH-d1GWSsC0jd6vcI1q6mnoH8TFOQJTNqguGxNuu03Muu-fKQgnoBqvsdsmacPHnlAMCPZeAuZACZWjciG73e8Vm9-o46BacvhM_ogLM2zk6j1DmZwfgA4M2fag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
15 دلار اعتبار رایگان برای دسترسی به بهترین مدل‌های هوش مصنوعی
استفاده از مرورگر به شما 15 دلار اعتبار می‌دهد تا مدل‌هایی مانند موارد زیر را امتحان کنید:
• GPT-6 Astra
• DeepSeek V4.1 Flash
• GPT-5.6 Luna
• Claude Opus 5
• Grok 4.5
برای دریافت:
🔗
browser-use.com
با استفاده از حساب گوگل خود ثبت نام کنید و شروع به استفاده کنید.
برای دریافت اعتبار بیشتر، از چندین حساب استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 667 · <a href="https://t.me/ArchiveTell/7712" target="_blank">📅 21:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7711">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🧰
جعبه‌ابزار همه‌کاره و فوق‌سریع تلگرام؛ معرفی آپدیت بزرگ بات Amir Tools!
بچه‌ها اگه کلافه شدید از اینکه برای هر کار کوچیک (هوش مصنوعی، استعلام قیمت ارز، دانلود یوتیوب و تبدیل فایل) یک ربات جداگانه استارت کنید، این بات همه‌کاره دقیقاً خوراکتونه. در آپدیت جدیدش کلی ابزار مدرن با رابط شیشه‌ای اضافه شده تا از ده‌ها بات متفرقه بی‌نیاز بشید.
🧠
هوش مصنوعی با حافظه اختصاصی:
مکالمه پیوسته بدون فراموشی کانتکست چت، سوئیچ خودکار روی مدل‌های پشتیبان و امکان ریست سشن
📥
فایل به لینک مستقیم و دانلودر یوتیوب:
تبدیل آنی انواع فایل، ویدیو، آهنگ و ویس به لینک مستقیم پرسرعت + دانلود مدیا از یوتیوب با بالاترین کیفیت
📈
نرخ لحظه‌ای و چارت زنده بازار:
استعلام آنی قیمت دلار، تتر و ارزهای دیجیتال (BTC, ETH, TON و...) همراه با نمودار اختصاصی و باکس High & Low
🤫
پیام ناشناس امن و دوطرفه:
ساخت لینک اختصاصی با آیدی تصادفی برای دریافت متن، ویس و عکس ناشناس با قابلیت پاسخ‌گویی مستقیم
🎁
سیستم قرعه‌کشی خودکار کانال:
ساخت مسابقات و چالش‌های گروهی با دکمه شیشه‌ای و قرعه‌کشی کاملاً خودکار و عادلانه بین اعضا
🛠
میکروابزارهای روزمره:
ساخت بارکد تصویری (QR Code)، پسوردساز غیرقابل‌نفوذ، مبدل ارز به تومان، هواشناسی و مینی‌گیم‌های کوئیز
💡
نحوه استفاده:
وارد ربات بشید، دکمه شیشه‌ای منو رو لمس کنید و بدون نیاز به رجیستر یا مراحل طولانی، به تمامی ابزارها به‌صورت یکپارچه و رایگان دسترسی پیدا کنید.
🔗
استارت ربات هوشمند
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 800 · <a href="https://t.me/ArchiveTell/7711" target="_blank">📅 20:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7710">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است.…</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/ArchiveTell/7710" target="_blank">📅 19:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7708">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل: ① به https://arena.ai/ مراجعه کنید. ② حالت Direct Mode را انتخاب کنید. ③ در لیست مدل‌ها، GPT-Image-2.5 Sunburst را پیدا کنید. ④ به مدت 72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود.
✈️
…</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/7708" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7707">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت گیت‌هاب قدیمی داشته باشید و از طریق این لینک وارد شید
✅
🎁
با هر رفرال شما 100 دلار و شخص دریافت کننده…</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7707" target="_blank">📅 12:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7706">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmBP3fMr8CDBX8hC2dAkp9UPtG6NAwpT7PuzT06afYR17q7wo50crkaWqvfkJDiksi2ZWeqAdZ6wIPQ-epGhmhFelct2QSfGDBX3gTWl7f7-sT-tu1v2rihN0rjiAAMGoH-vvJeCPIZOxZY1QTLgylEQBjLgmAobqhdb-14EkySxQv8huDlKF6Ib5uLZx-GQ2axSeC0xqEFm75pG4hOFt9620H_b5u8YoK4Vp7JJTj2dXpXX2oJKhFZcIY21sXDhYcFCl--0n4IFIFDqRwet1JBkCiFyRs7BSWnlEjgvzwjVjZBlV8gfxbk9iLiHB9paQ8PRpDpVKFgnBiJCuTcSxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل:
① به
https://arena.ai/
مراجعه کنید.
② حالت
Direct Mode
را انتخاب کنید.
③ در لیست مدل‌ها،
GPT-Image-2.5 Sunburst
را پیدا کنید.
④ به مدت
72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود
.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7706" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7705">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijX6K_tbfYKNbzy9kQbQjYWp3MYfbFJaEwO2qfk-ibFq577RRht8RhTbV8gHbc8MaTltWYY1DnDRdVMQPRnxEPuvWP89q_ppOLsuZ96C090XqiveO6FbjbbXirPr9skuz5g9fYRjNvo0TTtfAMcPRw1TnYu-SQI81StR_OrDBscH30sf3Qv6NqBfnw232d3jqX4pqgjQdRtHOUW-8abkkICU3LhgrCKokx8pGs26HCNNLg9yG8J-_ff24l8_3MgCTptZiloGnnMJmv8Ff4OicioPbmfRNHEkwYP3uthX232EZG5CZdRaQUa9K9PZ9Mr0q7tKm80XXowCy-tVavRn2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4.1 Flash به صورت رایگان
💥
🆓
این نسخه ۲ روز پیش منتشر شده است. دارای ۱ میلیون توکن متن، قابلیت‌های بصری پیشرفته و کیفیت مناسب برای استفاده در سیستم‌های هوشمند است.
🚀
🔺
رایگان به صورت روزانه
🔺
پنجره متن با ظرفیت ۱ میلیون توکن
🔺
سهم استفاده روزانه هر روز ریست می‌شود.
هنوز مشخص نیست که این سرویس چه مدت به صورت رایگان باقی خواهد ماند.
‼️
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7705" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7704">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AF-szmxIQtpSrP1r9-T3Y-3hC6_z3gyF9pdlj2XrsXDzGrLoZK_cvKutCEGdCclucBVMhhdm-ud5plDl7mQTGMCO2Q0w5uiUfI0hP2Q1l5hYNT105fgU0E0yfSv5Sjgv0up9CnAbSW3hXrOC_ym28hL3Htm2bwrsCJYMajo0o1mF3cV1f8Vij82e1mSDonWa8RvWdfZFo6Tz7k9nJAeUyfIznUBFF-NKiJpTL7W7wZb2hImG8xnLRhr2iIDOpgFS-jNSVprRAX94FJNJqfRjGs97jYcpXZg_jLlEdHXwOrts8hP5rvMi7ln9mHfbUu9ENSBbe1R25UVuMfuknriFvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
با این سایت میتونید 5 دلار اعتبار رایگان برای بهترین مدل ها دریافت کنید همچنین این سایت 3 مدل کاملا رایگان بهتون میده
💵
😎
Kimi K3 | Deepseek 4 Flash | Mimo 2.5
✅
📌
Base URL: https://tokenharbor.ai/v1  با جیمیل…</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7704" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7702">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cw8-Gzl7S4IIwPg77D6brzAQb0feA-kw3aRvCT-VNb2TBkl_-ObMzsiHtcqg1v1mPVU33cwNmfqKSnDCk_bHfEDZNzIF5f_w4eDR1P7DPz4ymWuXVtXdu8S7axi5SUgsNMKEwdGucP6BAabCsb7mQo2p1sR8vyieFHCFdCW6dzNLdfr_4HdfPMdl8sh1n7g7uZoPgbwB9BXxOKCt2kdg3u_Vc96C8QjGpTuci0GSHgqTaFM1KqxMvztPSsfiW0dUuvrQL4LLmok_OZ9i4-OhkCj5t5b2bG7Xpvj7675V1XKyXXxmtIQx7R-VSfJL45WmVOxkHKATk1yxhT5Za0dobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GPT-6 Astra
1 Day Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=gpt-6-astra-medium
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avEAj8xVHtivy9PRO9fChk2xoRMQwWLOuDptrLL2BfjZUJDmcuZNuRsDNw05hoAwRVFidrw1DpA647ctasbuj6hwNFWsUtyETPEEGQ8RvgUOeJ9GCahNVmrWsfCE7eyaKYdjwyPnr9-Dg2TliTWuXuCR769ab3hC45WBYNwwPjhccrmgY4Prg3GPxMgRCOlfcP9pCJ1muLP-uN7GxndkUo57fRfA199C06BYgwzCioRm5FCaWYsrAw9-3NJqD7oxildha0aXKCXI_HQOHytn0_wAZegnXeWNWb18D8oa-ipnOY3uUJlzrXSt2k8QE-9nH2D0TYd6izMfbYuCb1HJWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">150 میلیون توکن رایگان برای مدل های زیر
💥
🆓
GLM 5.3 Flash | Qwen 3.8 Flash | Mimo 2.5 | GLM 5.3 | Hy 3 | Qwen3.8 27b
✅
وارد سایت زیر بشید با جیمیل ثبت نام کنید سپس از طریق منو 50 میلیون توکن امروز هم دریافت کنید
✅
‼️
نکته :
از مدل های با پسوند Free استفاده کنید و احتمالا این دسترسی شامل محدودیت تعداد ریکوئست در دقیقه باشه ، همچنین ممکن هست هر لحظه اشتراک رایگان بپره
📌
Base URL :
https://kiraai.vn/api/v1
🔗
لینک ثبت نام
🔗
لینک گرفتن کلید
🔗
لینک دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7700">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🧠
پروژه OXYGPT — یه ربات تلگرامی که هوش مصنوعی رو حسابی جدی گرفته!
بچه‌ها این صرفاً یه ربات چت نیست، یه اکوسیستم کامل AI روی تلگرامه: چند مدل هوش مصنوعی، مربی‌های حرفه‌ای تریدینگ، sandbox واقعی لینوکس، اخبار فارکس زنده و داشبورد مدیریتی. خوراک کسایی که می‌خوان یه بات production-grade بسازن نه یه دمو دو ساعته
🔥
↔
مسیریابی چند-مدلی AI
: استخر کلید Gemini + سرویس‌های سازگار با OpenAI، round-robin می‌چرخن و روی خطای 429/503 خودشون فالبک می‌زنن
🪟
پنجره‌های مکالمه مجزا
: هر کاربر تا ۵ چت جدا با تاریخچه و state خودش می‌تونه باز نگه‌داره
🧙‍♂️
مربی‌های تریدینگ (Persona)
: چهار شخصیت آماده (ICT، Quarterly Theory، Matrix/369، Price Action) با یه دستور سریع صدا زده می‌شن
📓
ژورنال معاملات
: ثبت و پیگیری ترید‌ها با قالب‌های اختصاصی، مستقیم داخل تلگرام
📰
اخبار فارکس زنده
: رویدادهای پرتأثیر Forex Factory رو با تحلیل کوتاه AI نشون میده
🖥️
قابلیت Sandbox واقعی لینوکس (E2B)
: مدل می‌تونه کد اجرا کنه، پکیج نصب کنه، ریپو کلون کنه و فایل بفرسته/بگیره
🔑
قابلیت BYOK
: کلید API خودتو وصل کن، از محدودیت پیام و quota عمومی بی‌نیاز شو
👁
مانیتورینگ کانال با AI
: کانال‌های تلگرام رو زیر نظر می‌گیره و پست‌های مهم رو تحلیل و تحویل میده
💡
دیپلوی با یه دستور روی Docker/Railway انجام میشه، و هر ۵ ساعت یه بک‌آپ خودکار از کل دیتابیس‌ها زیپ و برات تو تلگرام ارسال میشه — دیگه نگران از دست رفتن دیتا نباش.
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FltTDLmFavCU4dVsdkafl3rLrG3i_dqJsND2DCXKwS6zsBRxo38Fxg5HXrV_yrNjd9y50B1NAI2Mo4H4PUSclyRQRTTa57mmng5KKemYguTl4OdO1cqwYrrdWZ_v5foJj74dErYeau-K17mXB2N82sFagw56m6sNmIKjNJHhICilWEIv__WFGgcLo_r7h17KYTqIeG4xyYNcQbA9YkVwY6tOjY2yJ4lN2sGshMkcIftNDNcy6MphHqsNoEwjTiW0oUv2LKoylso2SqbNCVBdr5PW8y7vaDHl7Gnp2OmC99NLHAWdgwjnWG5yj97_47lcac39pT1gGdarwqY-2I17lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTsLl1UNcXbMnlGUyIaVsJui1p45Kodtbo3x5E4xwIZjIdYbxz19d3TZjK1GO2SwANFlwlvFKYGtr9Df9ORrna8UfrOp8J9zm6pPGhS2s3mdadma6DXwlEnOSm7yb5n5hEDdgn-66wr6Jd9TOsfiUG95vdNY00HFSbD9bLQklM7jp-HxOwhMHFq74HIVoZmSk2MKh8trKEZfLrmF55mE4uKbDbgcKB53XN_9lanypLJjo_1XkQbVPZoAhOWpB6LCpKFmyvPtuvmMLYxaq6G_lwCBDbZCDBZEAwdj1HVL6jSRiP-Q26kv7q8HHeFqyTOP1TP8nUTAGowWBi7lj10Eig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزانه 1 میلیون توکن رایگان برای مدل‌های زیر
💥
🆓
Gemini 3.8 flash | Muse Spark 1.3 |GLM 5.3 Flash | Deepseek V4 Flash | Deepseek V4 Pro | GPT 5.6 Luna | Gemini 3.1 pro
✅
وارد سایت زیر بشید و ثبت نام کنید و یک کلید دریافت کنید
✅
‼️
نکته :
با هر آیپی ۱ بار میشه ثبت نام کرد اگه میخواید چند اکانت بسازید هربار آیپی هارو تعویض کنید
📌
Base URL :
https://apinex.bond/v1
🔗
لینک سایت
🔗
گرفتن کلید
🔗
دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7vtXAxi6qhMxjvpT2l4gB_uFo70B7kuig_GshNj8CxCKg7Kxt5LDwW_zoFtYJVGHjbFFSxqVxqIuZXtvkIdq64QGwPIxrvMNKv2oL76YpGq77dQSX2_mtVPS7KAJgA7dyhQINncASOXllMo5r2DaYj3I7w8pDDZ8FXgmV2m79fwjbeN0pS6Agyno5mMEzLR09jW-83O6RbloFXdle7Npz-ANIcaNgpa4Rr6BzRIdsi86k15x9LdG0LIsUBBb1TaclhWDJsC1VjiXx9QHxqlrh0SMnI7OB7Da0AS0e22KSfJ31ssnHv2ErxD4KO2AbWZmLjHH0G_-CWUjgNjl2638Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 میلیون توکن رایگان 1 ساله
💥
🆓
Fable 5 | Opus 5 | GPT 5.6 Sol | Grok 4.6 | GLM 5.3 | Qwen 3.8 max | Kimi K3 | Deepseek V4 Pro 0813
✅
برید داخل
این سایت
ثبت نام کنید
حالا برید داخل
این بخش
پلن سالانه رو انتخاب کنید و این کد تخفیف رو بزنید :
DEVWEEK
بعد اینکه تخفیف اعمال شد تایید کنید و تمام ، یک api بگیرید و استفاده کنید
✅
📌
Base URL :
https://codecraftapi.com/v1
اکثر مدل های جهان رو داره میتونید از Playground چک کنید ، چون سایت شلوغی هست طول میکشه تا ریکوئست ها جواب بدن
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnDO5wpXGCelV_6xINJVHjVHCfUaiAWzwuY99VB15YowXERGvdANW7MwqQN8OCD6s-0zuFECDDV74jIbqOiK_emTwMoQywK1iJ30n5eVl2wOXMjiPCfT2LYDat2C-Zmp6_ns97sR3lujPzZO83YTpfSBotnRgoA-0_ekOAMfgwmtFoOvJ-t4cf7e1ZpQv1BNUh2ilE1-O7yKqqNc-CURgNwtxyZbBkEJVYzSB7E0QehIfiyVmnZNyeA_PxC34R9Znvn1pEmWZR6wIKnI1KfGx_zg6QwC0z9g4ow4pI1xew8vedaacuE-w3arm55r_xzsgUjf7crev5G0Uqi2Irj01w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
تغییر ریجن گوگل در ۳۰ ثانیه
⏱️
با فیلتر شکن کشور مقصد یکم برین تو گوگل بچرخین،
بعد به لینک زیر بروید، ریجن را انتخاب کنید، دلیل تغییر را بنویسید و ارسال کنید.
https://policies.google.com/country-association-form
حداکثر تا ۲ ساعت ریجن به جایی که میخواهید عوض می‌شود و ایمیلش میاد
✅
بعدش میتونین به راحتی از antigravity و سرویس های دیگه گوگل استفاده کنین.
از توجهتان ممنونم
🙏
✈️
@ArchiveTell
|
#method</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📌
Model :
gpt-6-astra
📌
Base URL :
https://api.eirouter.ai/openai/v1
sk-e76d452dff7eccef0a1b6bde4f8262c7f628f4f2991676cf3188d0cb68023b3f
sk-778bbaffd07397311260074542e405ab11833bf458e0250363ac1afd7db02297
sk-b028d3f23d96d0b0fc96a24985164437fcaf272276caf33548a664a0df424dc1
sk-1f153c31ccd2448b30c2f56287d5dc8fcc8ddafa579d12a797450321d86e9d29
sk-3334618935b09f67a70938d3379971e3ad350fec1154008d3abbaa07565c00b3
sk-242582ef9fc5e53351eb2fd67178b83033a450a61d048cf66be6aacf98a9e2bc
sk-db726cb7cc5b14160f9d8900455fcd34fd56cbb94f3afac65494a5161eee35b6
sk-7e85fc089be2d58f76c236c8ae1efc6062f68a459bdc9f87bcbe896c2d7307e2
sk-cca857a86f2c62b5d704f2234ed5632f8ef4dfbfcc0da509fe0e021516a0406d
sk-3c3eb497a104328775de0ddb333c7c8d596c20a89e25bbe7e204318f35e2b050
موجودی هر کلید هست 5 دلار ولی نکته اینجاست توی سایت قیمت هر یک میلیون توکن این مدل هست 1 دلار
😁
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=vNs6btx0XRAsObyeewmRDlcrFIN997AqQ5WDunEqt97GGmD7p8hwbOwlFEMVaspyfVg2uzwEc7OEDuiv3fQEa3N0G1caxqh2ohqmsQCY2Wmk5iLzZn17O04SfywbZJ8gzWj-_B1VX2cwhmy3SPDMYaU70i1OSVxJf3nzoo1jl8e7Z2DjqMCRl-1dtihUzhxl-d9Ra9DHLDZpjU7SdkKPw7FYt6xyIIjOptxyb2OrxprcbsL5XCCBvJwfXQ91IwS7_jM-DldyyEigSgY4am0PH90tjeTFiqg5GpzZ0fLVupOyaKK1wDT7x4fYpYJEOCdsHncxV76o1NpyxdvE7K2FuRcW-EtC7p0KGWezMLIX-4JEGOd31GtT_UVLyAwO85TvZQkNylFD4GtFRGfOf8aalO8lHUAo6e9rZXnZBAYnJYmsFuY16g0pdHNVB8ufku3ch0QmVsDqtM1iNr9pt-0iumSHLDG6SloCrwdiLmIEWmGxG1GqcfDBeATkyP_dt2UrJ63kCJmwXVvb3wN6bPTr9e35mKV6sk_Agh6GbiPkGpdgQV5RCm7gaCOThXDzROQzjvwMH-VwCswYReybZn55ECYsS2SNdAUhFnouThsTEId2ctZcTH5sukiWynJ74HMOZTgGvQfVzZ92vETEZKEB0Ir_wZyZceDEMtX8Xws84Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=vNs6btx0XRAsObyeewmRDlcrFIN997AqQ5WDunEqt97GGmD7p8hwbOwlFEMVaspyfVg2uzwEc7OEDuiv3fQEa3N0G1caxqh2ohqmsQCY2Wmk5iLzZn17O04SfywbZJ8gzWj-_B1VX2cwhmy3SPDMYaU70i1OSVxJf3nzoo1jl8e7Z2DjqMCRl-1dtihUzhxl-d9Ra9DHLDZpjU7SdkKPw7FYt6xyIIjOptxyb2OrxprcbsL5XCCBvJwfXQ91IwS7_jM-DldyyEigSgY4am0PH90tjeTFiqg5GpzZ0fLVupOyaKK1wDT7x4fYpYJEOCdsHncxV76o1NpyxdvE7K2FuRcW-EtC7p0KGWezMLIX-4JEGOd31GtT_UVLyAwO85TvZQkNylFD4GtFRGfOf8aalO8lHUAo6e9rZXnZBAYnJYmsFuY16g0pdHNVB8ufku3ch0QmVsDqtM1iNr9pt-0iumSHLDG6SloCrwdiLmIEWmGxG1GqcfDBeATkyP_dt2UrJ63kCJmwXVvb3wN6bPTr9e35mKV6sk_Agh6GbiPkGpdgQV5RCm7gaCOThXDzROQzjvwMH-VwCswYReybZn55ECYsS2SNdAUhFnouThsTEId2ctZcTH5sukiWynJ74HMOZTgGvQfVzZ92vETEZKEB0Ir_wZyZceDEMtX8Xws84Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده:
جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch:
کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی خودش اونو به آرت نهایی تبدیل کنه
🎯
ادیت موضعی دقیق:
امکان هایلایت و تغییر دادن فقط یک نقطه خاص از عکس، بدون دست‌خوردن بقیه جزئیات تصویر
💡
نکته دسترسی:
تعدادی تمپلیت آماده هم برای تسریع کار اضافه شده و این مدل در حال حاضر به‌صورت عمومی داره برای تمام کاربران فعال میشه؛ حتماً حسابتون رو چک کنید.
🔗
ورود و تست در وب‌سایت
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⭐️
۶ پلتفرم برای تست رایگان GPT-6 Astra
دسترسی مستقیم و استفاده از API مدل‌های پرچمدار و سنگینی مثل GPT-6 Astra معمولاً هزینه بالایی داره و اگه حواستون نباشه خیلی سریع اعتبارتون رو صفر می‌کنه!
💸
با این حال، یه سری پلتفرم کاربردی وجود دارند که اعتبار (Credit) اولیه یا سهمیه تست رایگان می‌دن تا بدون نیاز به پرداخت، بتونید قدرت این مدل رو توی چت، کدنویسی، پردازش تصویر یا ساخت ایجنت بسنجید:
1⃣
پلتفرم Vercel AI Gateway
یکی از مطمئن‌ترین گزینه‌ها به‌خصوص برای دولوپرها. این سرویس هر ۳۰ روز حدود
۵ دلار کردیت AI رایگان
به کاربرانی که حساب فعال دارند میده. محیط Playground، پشتیبانی از ایجنت‌ها و سازگاری کامل با فرمت OpenAI API داره و برای ادغام با پروژه‌های شخصی عالیه.
2⃣
پلتفرم Brainbase
اگر دنبال کدنویسی پیشرفته، تحلیل ریپوزیتوری و ایجنت‌های خودکار هستید، اینجا فوق‌العاده‌ست. بعد از ثبت‌نام اولیه،
۲۵ دلار کردیت رایگان بدون نیاز به کارت اعتباری
دریافت می‌کنید تا بتونید تسک‌های سنگین برنامه‌نویسی و اتوماسیون رو با مدل پیش ببرید.
3⃣
ابزار Roboflow Playground
بهترین جا برای محک زدن قابلیت‌های بینایی ماشین و پردازش تصویر (Vision). توی این محیط می‌تونید اسکرین‌شات‌ها، نمودارها و تصاویر پیچیده رو بدون نیاز به کلید API آپلود کنید و دقت تحلیل مدل رو با بقیه ابزارها مقایسه کنید.
4⃣
سرویس CometAPI
اگه مدل رو برای اتصال به ربات تلگرام، افزونه یا اپلیکیشن خودتون می‌خواید، این سرویس کار رو راحت کرده. بعد از ثبت‌نام کردیت رایگان میده و چون ساختارش دقیقاً مشابه API استاندارد اوپن‌ای‌آی هست، بدون تغییرات عجیب غریب توی زیرساخت کارتون راه می‌افته.
5⃣
پلتفرم Imaginode
یک فضای همه‌فن‌حریف با محیط تعاملی Canvas، چت، API و ادغام با پروتکل‌های MCP. بدون کارت بانکی کردیت اولیه میده و هر پیام با این مدل حدود ۱۲ کردیت مصرف می‌کنه؛ بنابراین برای ساخت سناریوهای متصل‌کننده متن، تصویر و اتوماسیون حسابی جوابه.
6⃣
سایت Vibany
ساده‌ترین و دم‌دستی‌ترین راه برای تست تفریحی و سریع. در بدو ورود حدود ۳۰۰ کردیت رایگان می‌گیرید و هر بار اجرای مدل حدود ۱۰۰ کردیت کم می‌کنه. یعنی حداقل ۳ الی ۴ تا پرامپت عمیق و جدی می‌تونید بهش بدید تا خروجی رو با مدل‌های قبلی مقایسه کنید.
✈️
@ArchiveTell
|
#AI
#API</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🧠
شیائومی وارد میدان ایجنت‌ها شد؛ معرفی دستیار همه‌کاره MiMo Desktop!
بچه‌ها شیائومی رسماً وارد قلمرو ایجنت‌های سیستمی شده و یه دستیار دسکتاپی معرفی کرده که مثل ترکیب Codex و قابلیت‌های کنترل کامپیوتر Claude عمل می‌کنه؛ این ابزار خوراک خودکارسازی کارهای روزمره شماست.
🖥
کنترل کامل دسکتاپ و وب:
اجرای خودکار تسک‌ها، کلیک، تایپ، کار با فایل‌ها، پر کردن فرم‌ها و امکان ضبط و اجرای مجدد فعالیت‌ها (Record & Replay)
⚡️
پیش‌نمایش تعاملی و ادیت موضعی:
رندر زنده سایت‌ها، گیم‌ها و داشبوردها با قابلیت هایلایت کردن یک بخش و بازنویسیِ انحصاری همان قسمت
🧠
دسترسی رایگان به مدل‌های نسل بعد:
بهره‌مندی تسترها از دو مدل معرفی‌نشده و پرچم‌دار MiMo-X-Pro-Preview و MiMo-X-Flash-Preview
💾
کشینگ فوق‌سریع تا ۹۹٪:
فناوری بهینه‌سازی توکن برای تغییرات مداوم پروژه‌ها جهت جلوگیری از هزینه‌های اضافی
💡
نحوه ثبت‌نام در نسخه بتا:
ظرفیت بتا کاملاً محدوده و اولویت با کاربران فعال اکوسیستم MiMo Open Platform خواهد بود؛ فرم درخواست رو پر کنید تا لینک دسترسی و مدل‌های جدید زودتر براتون فعال بشه.
🔗
فرم ثبت‌نام در نسخه بتا
🔗
صفحه رسمی معرفی
🔗
صفحه رسمی قابلیت ها
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=TEPQBQkpC-h7OPpkyTLZdkLemzIdg_HMmvY_TL1rn41jb8V1mhAtk_GzMkYF6-XtvXegFQEj4-NLo5WHkwpLmq2SZVxFeMm1-V5ozws2K6QtaRJ3O1dXOfCqCSDDws39ns96d5f_E6R5ZXR46vEvNx4wSp2jLn9yucgiGqlsl83oNoAcc-2IdCkmJDaV0AKvfDl8_HPjalmiZjUasVEMZKNwRl-HXohdVX4NP-5VO7YyDTFmgdT3Z3yI1EmgiSD2ZPlwwBWDOCsy3A_VW9qPBFuyVhxANrY943Oowl_17NcIgSp6LnRvbwyJx8nSij-Us-ooDAnyLjNviOtvaGvrGBgS1R7txcpFGjD6ZTwkffNQUQTs55WtgtF55lZAB8ffjA-KjcvXjIz20jpH5E11Id1dfUaCEa8xxoWxSk8gkyuu66cO221E7i788nEWaT3JXLymb_PkOeEVU4Y0QgNIrUM5-7jq0FfKzxGS5L7IzEkoTmepfg3AbUSfXgM84EoqdaamV9ylqxoEpoWzINKYZZXOKny16H1zcBDlGpZJOJw8L7-txLrX5ypgTKI-FAAI3lrDAq904xiz0ZGMeW4djMeGNNpTRYqVIJA6K1skbtg_InarL4WNVZsgHB6Q6zp32KtvAkRtaWvnQgWAie-E48XEVHwAlvDKygI6c6QnfWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=TEPQBQkpC-h7OPpkyTLZdkLemzIdg_HMmvY_TL1rn41jb8V1mhAtk_GzMkYF6-XtvXegFQEj4-NLo5WHkwpLmq2SZVxFeMm1-V5ozws2K6QtaRJ3O1dXOfCqCSDDws39ns96d5f_E6R5ZXR46vEvNx4wSp2jLn9yucgiGqlsl83oNoAcc-2IdCkmJDaV0AKvfDl8_HPjalmiZjUasVEMZKNwRl-HXohdVX4NP-5VO7YyDTFmgdT3Z3yI1EmgiSD2ZPlwwBWDOCsy3A_VW9qPBFuyVhxANrY943Oowl_17NcIgSp6LnRvbwyJx8nSij-Us-ooDAnyLjNviOtvaGvrGBgS1R7txcpFGjD6ZTwkffNQUQTs55WtgtF55lZAB8ffjA-KjcvXjIz20jpH5E11Id1dfUaCEa8xxoWxSk8gkyuu66cO221E7i788nEWaT3JXLymb_PkOeEVU4Y0QgNIrUM5-7jq0FfKzxGS5L7IzEkoTmepfg3AbUSfXgM84EoqdaamV9ylqxoEpoWzINKYZZXOKny16H1zcBDlGpZJOJw8L7-txLrX5ypgTKI-FAAI3lrDAq904xiz0ZGMeW4djMeGNNpTRYqVIJA6K1skbtg_InarL4WNVZsgHB6Q6zp32KtvAkRtaWvnQgWAie-E48XEVHwAlvDKygI6c6QnfWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آرشیو ۱۵۰ پرامپت آماده برای خلق ویدیوهای سینمایی با AI!
بچه‌ها اگه با هوش مصنوعی ویدیو می‌سازید ولی خروجی‌ها تخت و مصنوعی میشن، این کالکشن خفن خوراکتونه. یه دیتابیس آماده از ۱۵۰ پرامپت تست‌شده که دقیقاً دستور زبان کارگردانی و سینمایی رو به مدل تزریق می‌کنه.
🎥
کنترل دقیق نور و دوربین:
پرامپت‌های تخصصی برای مدیریت لنز، زوایای حرکت دوربین، نورپردازی و دکوپاژ
🎞
همراه با نمونه ویدیویی:
هر دستور شامل پیش‌نمایش رندر واقعی است تا قبل از خرج توکن، خروجی کار رو ببینید
🎭
تنوع ژانر و اتمسفر:
پوشش کامل انواع سبک‌ها، سناریوها، اکت کاراکترها و فضاسازی‌های سینمایی
💡
نکته استفاده:
تمام پرامپت‌ها آماده Copy/Paste هستند؛ فقط کافیه کپی‌شون کنید داخل ابزارهایی مثل Runway ،Kling یا Luma و المان‌ها یا کاراکتر مدنظرتون رو با کلمات کلیدی دلخواه جایگزین کنید.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvcTEftT4TTGzUFtZqPghlUcN10jVGYeMh-hNrSwHoAkmKaWXZ4iZy9Mjn9FSuaASNQpSvrrk_F81fDwnk6z26B3ZVDijGfqU-yMuyRjDtvO_lNcGG_KapXLxtKL1DxnMKLJ8uMOinYTLNFgG3ARtIQvsr5Xamkyswhj_9rRam75Xyy9QkyWmvVI6be8Q27k7JQY11KvVWEderCbi_Cby2ntjI77Yf3iKkcfrcHAiLzHbVtnKyQkXSzUcG2JbTV7HnCPa-yCHaWHv5GSR2x4k5Tn9xsfMuII_hzameh1B-4RRpbW8ucCGDAhCSSszXf8QxD2uFwKzBZizDVdKnEXJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مایکروسافت آفیس رسماً مرخص شد؛ معرفی غول اوپن‌سورس GenOffice!
بچه‌ها اگه از خرید لایسنس آفیس یا برنامه‌های سنگین خسته شدید، این پروژه جدید خوراکتونه. یک جایگزین کاملاً رایگان و متن‌باز برای مایکروسافت آفیس که ایجنت‌های هوش مصنوعی رو مستقیماً آورده داخل اسناد، جداول و ارائه‌هاتون.
📝
پکیج کامل و همه‌کاره:
مدیریت بی‌دردسر داکیومنت‌ها، شیت‌های آماری، ساخت اسلاید و کار با PDF بدون نیاز به ابزارهای متفرقه
🤖
ایجنت‌های تحلیل‌گر:
اتصال مستقیم به مدل‌های قدرتمندی مثل DeepSeek ،Claude و Kimi برای تحلیل داده، نگارش متن و تولید محتوا
💻
آزاد و مولتی‌پلتفرم:
پشتیبانی رسمی و نیتیو از مک، ویندوز و لینوکس بدون نیاز به پرداخت حتی یک ریال
💡
نکته جالب توسعه:
جالبه بدونید نسخه اولیه این پروژه رو فقط یک مهندس، توی مدت یک هفته و با سوزوندن ۱۰ هزار دلار توکن هوش مصنوعی جمع کرده! ریپو تازه پابلیک شده و سرعت استقبال ازش وحشتناک بالاست.
🔗
گیت‌هاب GenOffice
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=peBMP9wr6wFRE-M_VJGhcyD3SCG0kLlF_vZfLV3_i92n9wKh0ggBV16MA3QdPVoWIa63j9B1w1m_ue8JrLSJkI5FSvsdgO8DbEZ59aO0EWrK49Rzb_hd_Yq_YJAsqv9zXD-hQ3C1jBc4gYrCJQVCpuICknbctpw7HSppBTQlAdI27Jg8s3lO-8u9Yfyup4WrK3oc-TX3iMreYC_yrrOazxGsnD71zbLY0mjtwuKWWhLXjDz3b09gBq4HWXrrEOMQHKCk0bN0EwXg3RgsH5c2tpf5IjuL7K_Y97ynEkpsddUeLwFjQV724QpPiqndKYuj0SkBt_-LrVDE0Aus1UZn1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=peBMP9wr6wFRE-M_VJGhcyD3SCG0kLlF_vZfLV3_i92n9wKh0ggBV16MA3QdPVoWIa63j9B1w1m_ue8JrLSJkI5FSvsdgO8DbEZ59aO0EWrK49Rzb_hd_Yq_YJAsqv9zXD-hQ3C1jBc4gYrCJQVCpuICknbctpw7HSppBTQlAdI27Jg8s3lO-8u9Yfyup4WrK3oc-TX3iMreYC_yrrOazxGsnD71zbLY0mjtwuKWWhLXjDz3b09gBq4HWXrrEOMQHKCk0bN0EwXg3RgsH5c2tpf5IjuL7K_Y97ynEkpsddUeLwFjQV724QpPiqndKYuj0SkBt_-LrVDE0Aus1UZn1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت خفن: تبدیل هوش مصنوعی Astra به یک بات بازی‌ساز حرفه‌ای!
🎮
🔥
داستان از این قراره که یه دولوپر، Astra رو طوری شخصی‌سازی کرده که عملاً تبدیل شده به یه ماشین بازی‌سازی. اصلاً هم شوخی یا بازی‌های دوبعدی و پیکسلی دم‌دستی نیست؛ کیفیت کار در حدیه که باورتون نمیشه کل این دموی سه‌بعدی خفن فقط توی
یک ساعت
جمع شده!
👀
⏱
سازوکارش چطوریه؟
🛠
همه‌چیز با یه اسکیل (Skill) جلو میره:
* اول Astra باهاتون گپ می‌زنه و از بین ایده‌هاتون، کانسپت اون بازی رویایی که تو ذهنتونه رو درمیاره.
* بعد طبق همون پلن، توی ده‌ها دور آزمون و خطا پروژه رو قدم‌به‌قدم کدنویسی می‌کنه و می‌سازه.
پرامپت استفاده‌شده برای ساخت این دمو:
📝
Prompt (high effort): /dream-loop Build me a graphics demo: isometric camera, voxel-ish art style with realistic shading and reflective wet floors, a character in an interesting scene. Fantasy setting (think Elden Ring, Diablo). Three.js in browser, >60fps. Don't download assets. Time limit of 1 hour. Controls: click to move the character, camera lazy-follows; drag to rotate camera; scroll to zoom in/out. No gameplay for now. World should feel alive: motion, animations, subtle environmental behaviors. Area around player should look expansive, but only allow movement in a limited space. No need to confirm the art with me or ask questions, just go!
🔗
دموی بازی توی مرورگر
🔗
خود اسکیل Astra
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOs0VgMiJ-QjV7zkKP8HBzdPASgq84YOVFnzOceaoJSL5shvZff1Eq1Z2TpzAeMN6Vj58tZqKJsN31sbfTVtJR_O0NiD9Y0ErEfloCkF8efFHZhwSaIuT4nBYnPZPb1PwmVxWSVuonjV9qiyDxDYNH1njCHYejPn_crI_nv2dzXMHdcgP_Yqq1JoKEYaN3YKc4AJ5pkyAk3148FbRhHrqhS8RVi4Wq7YPvACIprkeY9oCunAZjrNdnaKEzQRtl0CxpcFou0j78PmMr6S4_fj11G9j65sM-Itm1A2d3nKyiAtB4OQ_UZ3Rd1Ircj1IYYvtxK-T3YgqHYFRfANXp94zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📝
باز کردن بی‌دردسر فایل‌های آفیس روی اندروید با OpenDocument!
بچه‌ها اگه فایل‌های متنی یا اداری دارید و دوست ندارید برای باز کردنشون تو سرورهای ابری آپلود بشن، این اپ خوراکتونه. تمام اسناد OpenOffice و LibreOffice رو کاملاً آفلاین، سریع و بدون نیاز به اکانت باز می‌کنه.
📁
پشتیبانی کامل از فرمت‌ها:
خواندن بی‌نقص ODT ،ODS ،ODP در کنار فایل‌های رایج DOCX ،XLSX ،PPTX و حتی PDF
🔒
حریم خصوصی واقعی:
پردازش کاملاً لوکال، بدون اتصال به اینترنت، بدون ترکرهای تبلیغاتی و بدون نیاز به ثبت‌نام
⚡️
سبک، امن و باسابقه:
یکی از قدیمی‌ترین و پایدارترین پروژه‌های متن‌باز اندروید (فعال از سال ۲۰۱۰)
💡
نکته کاربردی:
بهترین گزینه برای کسایی که با فایل‌های کاری و اسناد حساس سر و کار دارند؛ با خیال راحت می‌تونید حتی در حالت Airplane Mode به تمام داکیومنت‌هاتون دسترسی داشته باشید.
🔗
گیت‌هاب پروژه
🔗
وب‌سایت رسمی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7681" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7680">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=MYYHQ6Pfft440ER3AJ91duK3GnWE7NzfWRH9UAyTWJf3FtW3-POaArQvBw8CARw0RmHLu-o3qIBdX6UTjNe9qAKeUNU4bU21qu7xHY2li-1il7b0Fh-xLupoNA9WT0NzJ0pwHylx2HT0mmsn98sJurbAcB3ZcjLp7z1g02Fw2d22j365yUeBbmrzDMs1aFzjJKBADyJsbKD09oBIBvLRRs4qL8EKhDCRFeYcLmxHOaG15TQKJzsZUNrJqXMFSYd2iQ1DyDv08neUv_9nkOjFQOPh8jY9rOP33EqRyPNGgsW2jjbSmn-vWqmFAtUVsS4jMXrERhoYccqjMht4t2oWVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=MYYHQ6Pfft440ER3AJ91duK3GnWE7NzfWRH9UAyTWJf3FtW3-POaArQvBw8CARw0RmHLu-o3qIBdX6UTjNe9qAKeUNU4bU21qu7xHY2li-1il7b0Fh-xLupoNA9WT0NzJ0pwHylx2HT0mmsn98sJurbAcB3ZcjLp7z1g02Fw2d22j365yUeBbmrzDMs1aFzjJKBADyJsbKD09oBIBvLRRs4qL8EKhDCRFeYcLmxHOaG15TQKJzsZUNrJqXMFSYd2iQ1DyDv08neUv_9nkOjFQOPh8jY9rOP33EqRyPNGgsW2jjbSmn-vWqmFAtUVsS4jMXrERhoYccqjMht4t2oWVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📍
با GeoSpy لوکیشن دقیق هر عکسی رو دربیار!
بچه‌ها اگه دنبال لوکیشن یه عکس رندومید یا اهل چالش‌های OSINT و ژئوگسرید، این هوش مصنوعی خوراکتونه. حتی اگه متادیتا (EXIF) پاک شده باشه، از روی خط‌کشی خیابون، گیاهان، معماری و تیر چراغ‌برق مختصات رو براتون پیدا می‌کنه.
🌎
جست‌وجوی جهانی (Global):
پیدا کردن چند تا از محتمل‌ترین کشورهای دنیا حتی از روی اسکرین‌شات یا عکس کراپ‌شده
🏙
مود شهری (City Search):
اگه شهر مشخص باشه، با عکس‌های خیابانی مچ می‌کنه و آدرس دقیق پلاک و خیابون رو میده
📸
تحلیل چند زاویه‌ای:
امکان آپلود تا ۴ عکس از یک لوکیشن برای بالا بردن نجومیِ دقتِ حدس
💡
نکته طلایی:
کیفیت عکس اصلاً مهم نیست؛ این ابزار حتی فرم شاخه درختا یا مدل آسفالت رو می‌فهمه! موقع ثبت‌نام اولیه هم یه سهمیه سرچ رایگان بهتون میده تا تستش کنید.
🔗
وب‌سایت ابزار
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dM2VDIJvRQymAQU3HiRFv-uvv23eTB8g6wZ9cCxytIaUW627H5yNpc5Cr98oIT0wTBSN9q23mY2EGb_2C8MaOd9TAMTPrqWUieVi_wkQjn6nsJsCYCdOsmzQAaBPhAUUqflV1tNVo3pj5eykxxrEteGWe5TI0AwBxS8GZwtA02CFrvhZy6odZXWCX1FDq6cVso-8uIPr8prqOD4LzSnWSdjCYXo3B4G7hVZSgukuS7WmBCcR2W7iyJyk13VUfCt97fYlZXChYUAtXzLVm-qMRDoqPdXIfkKaMsJto5bnXPLKvTpWcWkoNlDAMHDmSZNzf9EzmWIxu_QGEEZLbBJJbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕸
با SpiderFoot ردپای دیجیتال هر چیزی رو توی اینترنت بیرون بکش!
بچه‌ها اگه تو حوزه امنیت، تست نفوذ یا اوسیانت (OSINT) کار می‌کنید، این ابزار دقیقاً خوراکتونه. اسپایدرفوت یه ابزار متن‌باز و بی‌رحمه که کل سطح وب رو شخم می‌زنه تا تمام ردپاهای دیجیتال و آسیب‌پذیری‌های یک هدف رو دربیاره.
🎯
تارگت‌های همه‌جانبه:
جست‌وجو بر اساس شماره تلفن، ایمیل، آیدی توییتر و تلگرام، نام، IP و دامنه‌ها
🤖
اسکن تمام‌خودکار:
جمع‌آوری آنی داده‌ها از بیش از ۱۰۰ منبع اطلاعاتی بدون نیاز به سرچ دستی
📊
نقشه ارتباطات بصری:
تحلیل داده‌ها و نمایش گراف‌های دیداری از اطلاعات لو رفته و پیوندهای مخفی
💡
نکته و اجرای سریع:
راحت‌ترین راه اجرا با داکره؛ کافیه دستور docker run -p 5001:5001 spiderfoot رو بزنید و پنل تحت وب رو باز کنید. (یادتون نره، فقط تست امنیتی قانونی و اهداف آموزشی!)
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahw2e33u1LlyU8xgRC_W8Sjw0VsISw1IJhFM0J_DmlwYcT8eakKhi-5jCvsGkP28voq80z8GsYzOtk80sHuRLcQyV9iZXflIZu6vM84b1VeWMMXldN54zBxWXUp3fjXK9bxIW8MwH28ovgKmATpVRw5IzTajfUD0unyjnAZDOCYJTUofnl9sDQxvwUi0wp4efrpxAvm5j-ug1aCzSIL7f3XMWvYmuHevJjk_dGudrJEPcJHP4aMl_Sb8gU6ckMODIOBr3P2vW8gTaEy0VC3jC7_MJMSb5U5_sdGyRzGvqLPtiSWivzdjp1xPVkcnymJk1f2wvSPjbTZsr8ZRKKYV4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توکن‌های نامحدود برای Claude Code با شاهکار مهندسان اسپاتیفای!
🚀
🧠
پلتفرم
Portal
مثل یک مدیر هوشمند عمل می‌کنه و با واگذاری وظایف ساده به مدل‌های ارزان‌تر، تا ۹۰٪ در مصرف منابع و توکن‌های هوش مصنوعی شما صرفه‌جویی می‌کنه!
🔥
🔺
تندخوانی با Gemini (bulk-reader):
فایل‌های حجیم و چند هزار خطی توسط Gemini 2.5 Flash آنالیز شده و فقط یه خلاصه مفید به Claude تحویل داده میشه.
🔺
کدنویس روتین (code-writer):
تولید کدهای استاندارد، تست‌ها و تنظیمات خسته‌کننده به مدل‌های کم‌هزینه سپرده میشه.
🔺
تمرکز روی کارهای حیاتی:
با این روش، Claude فقط درگیر کارهای پیچیده و استدلالی (مثل رفع باگ و طراحی معماری) میشه.
💡
در
نتیجه:
یک ترکیب هوشمندانه از چند مدل AI که باعث میشه هزینه‌های شما ۹۰ درصد کاهش پیدا کنه و خیالتون از بابت محدودیت توکن‌ها راحت باشه!
🔗
لینک دسترسی و پروژه
✈️
@ArchiveTell
|
#TOOLS
#AI</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNfCxhhN9tliavNlXDNU08rqebOqei3gV4ZmNczJ9gr0g7dRrFZTYMspNnJ9TPawNg1YBFy1ET1bf9gxTnnQfyD6x21Xvz7PZyB4Tgj4i8lwYtn86FnKz1xL0l8d5Fawrp3mbQ514S2tjv6KDPMz8sMMIVbkOQrFPKX3i2mxpfLCenitv3nw6Y-ITCdOCnO_KE6tZ7jvjS5rDJnyExuj46lT4-OY73Ww9UnaVc-BSPSxTI0FrPPP9sZYFX-sAe1dX3TLR4bcDD7C576Zkg6HDogg-qXJ9uJdhvmlx9MJNxNoIRNKHad1XHf3SlyjxWAp4ii_Oi6lEJWNqVqYka8xzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت
یا کاملا رایگان باشه یا فریمیوم
با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم
اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uab627mtmR_tLJdvSKahQycDBBFVGxHJ1_PC3a22hGigz52XLZKQpmaD8YTEJgn9V-_AmQUpcUxfLW0e4uVZqcXJvzu64SuCfirNAuO9Ofs95wO04iZ-CZe6u1Lo9rjZHTFRgjMy_4wDBL6f6P3BJmMCAC6K2STrySlSqsIlqjKUHr3SbdbadVFjbcBF_RmzvmT1Tvvi6KyMNVtcShZtI79w3ajuHYYKMr-dgz6_lSRCSw2jOKFj21YlXBLWM6NqxGe4W2iDRdZdvPtRDy8IN6BYT_Tun2Vj2kurVsV4DQbuZ_4MbO3X8hx3hl-ph4HBqHk7yDOZACEbY-hpPdKLpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYtsOIJmFkvDZ0L10YR_XzKj2jbKCeIv8hF1DIchNgDnc_LrXN6KpM3Q-yDLZ5n26tHHf6XRx_dI7sh6R4M_-PDhCX-S1ematdPeCMmY7lFDsDl9bjNsJtDZ19E8gh6pzEdHuZvWs47lGJLfOrQCt6wmHBbHDYaaqHfi-lMsCjaKVB9ZwpV9ixn61BfCfVcqUYCeKueTp8eUacSq6kXQeMVUo6qp2TvVWAH6ENUrHq4ljEyu3Jl-kSIX6ST_wv3Co7i0xmvwmgJBvub-OLzkqxaH9hbYRNIYdTqOgi9w61mZaKaStL8Y9xRt6EAHFJ5c8O-SeFLVkLCQGUp3pDIRhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📌
مدل GPT-6 Astra بازم یه حرکت دیگه ثبت کرد؛
بازی Portal رو تو 23 ساعت و 43 دقیقه تموم کرد!
مدل به طور خودکار شخصیت رو کنترل می‌کرد به طوریکه هوش مصنوعی یه تصمیم می‌گرفت، بازی متوقف می‌شد. GPT-6 Astra با استفاده از تصاویر، موقعیت شخصیت و زاویه دید دوربین، تصمیم می‌گرفت که چه اقدامی انجام بده. بعضی وقتا هم تصمیم گیری هاش تا چند دقیقه هم طول می‌کشید، اما در هر صورت تونست بازی رو به پایان برسونه.
🔥
این کارو آقای "cozyblaze" با کمک اشتراک ۲۰۰ دلاری Codex Pro انجام داد.
🔗
سورس پروژه
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOjVyR8MBh554Msc6nuOXgzNdLf4852_vLxuhI9djWahuNxCcmycNPceEbXkVFtHFsszR1UZGP_ga22Wh8jNsjODRxvuweY9gkWsojXCgHhibG_KSLuS8MyosBntAUFOuT7AG_Rc9EP1g-nGmDCi2DDolaMdHHxjJL-yqf6CrXzLNa4RFVYyxF4uV9IWCIj2_23QxAQsBasq1ODG1lzRK5mBbyru87z3FLDZxIzd8rGOkUuyS5XJYyNIOvmPM5lZLofQ6mjBelMOw1FA70ueNo4qzKNscyva9pCfpv5QSkEihwboXY3_erRBWtOWFqQ-2mmol1WlIB7koGgloFHhqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعبه‌ابزار همه‌کاره برای برنامه‌نویس‌ها با DevToys
💼
اگه خسته شدید از بس برای کارهای روزمره (مثل تبدیل JSON به YAML، تست RegEx یا دکود کردن JWT) مجبور شدید سایت‌های مختلف رو باز کنید،
DevToys
دقیقاً چاقوی سوئیسی شماست!
👍
🔧
بیش از ۳۰ ابزار کاربردی:
انواع کانورترها، انکودر/دکودرها (JWT، Base64، QR)، فرمترهای کد، هش‌ساز و فشرده‌ساز عکس.
📄
تشخیص هوشمند کلیپ‌بورد:
به محض کپی کردن متن، خودش می‌فهمه چیه و ابزار مناسبش رو پیشنهاد میده!
🛡
کاملاً آفلاین و امن:
تمام کارها روی سیستم خودتون انجام میشه و دیتای حساسی سمت سایت‌های ناشناس نمیره.
➕
پشتیبانی از اکستنشن:
میتونید ابزارهای دلخواهتون رو هم بهش اضافه کنید.
📌
لینک مخزن گیت‌هاب پروژه
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=EVW0bjfaSMQ0lJrh69rHkeTvwvzr0YD-SQ6UZWdUIetmT1dF3pPz3gcdDb6u_kmEnCri1Wm81uE87QB87sh-0A20pA-qghDY9aZiNItclKhSD_t1J-pNtyxjoDIO9FLXjuXK28XwUwZSINc4lUXtWKsKVScNygdmK3VHlEyxnBnUEc5xuXYCCqM8S18tBaDs2iHiPvPdymMgFgQGKygKk_v9KU4iG1DE7wXva9HJId55VJtjGaS9wR306sDXjHj4Rn2DuwLF2A5hUoNR5DEHF1DZRRDrQU_a_9kNBCGsOXqIFkHgWAVGnoB707Ao40traenZqlQ9r8XiIVSne1yFDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=EVW0bjfaSMQ0lJrh69rHkeTvwvzr0YD-SQ6UZWdUIetmT1dF3pPz3gcdDb6u_kmEnCri1Wm81uE87QB87sh-0A20pA-qghDY9aZiNItclKhSD_t1J-pNtyxjoDIO9FLXjuXK28XwUwZSINc4lUXtWKsKVScNygdmK3VHlEyxnBnUEc5xuXYCCqM8S18tBaDs2iHiPvPdymMgFgQGKygKk_v9KU4iG1DE7wXva9HJId55VJtjGaS9wR306sDXjHj4Rn2DuwLF2A5hUoNR5DEHF1DZRRDrQU_a_9kNBCGsOXqIFkHgWAVGnoB707Ao40traenZqlQ9r8XiIVSne1yFDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم 7 برنده خوش شانسمون
🎉
:
1.
@reza1629
2.
@mhti9
3.
@KIING_ZOG
4.
@Gogogrugo
5.
ＮＯＢＯＤＹ
( 6641463426 )
6.
@an_Y008
7.
@AshenOne2077
برای دریافت جایزه به دایرکت مراجعه کنید
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7670" target="_blank">📅 20:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7669">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7669" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7668">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🥇
رکوردشکنی دوباره از GPT 6 Astra
خبر رسیده که GPT-6 Astra تونسته تمام ۴۸ مرحله بازی «I'm Not A Robot» سایت
Neal.fun
رو بدون غلط رد کنه ، خیلیا جوری جو دادن که انگار آخرالزمان امنیت سایبری رسیده!
😂
طبق معمول، ته این هایپ‌های رسانه‌ای خبری نیست. کپچاهای تصویری سال‌هاست که عملاً مرخص هستن و حتی مدل‌های پارسال هم با یه پردازش تصویر ساده دورشون می‌زدن.
سیستم‌های امنیتی واقعی وب الان با تحلیل رفتار موس، کوکی‌ها و الگوی کلیک کار می‌کنن، نه با ۴ تا عکس چراغ راهنمایی و خط‌کشی خیابون
😁
تست کن ببین رباتی یا نه ؟!
🧐
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7668" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7667">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzhC25m03GaI8kwzx5m22_WnUNHaU0t9OhWDJF5Zg64ib1WOK74NFe4ncrwfccDUSczbe6Ade-V663Y9kIaDIJHcqamGUzgs8Ft-dDe0H4mFhcIzRi2V5lm_iajKVKY9WqN08rWr-XlDvEvC9_wn-kNiaao-AcaM2-mr8DkCmuUzzhJagRpCDWPFb4M-bUyfhGrL_HAfBie4Ff123fPV4c1v2ZSX28xHDhpeiKWb2f0GzMIl0rcdYatXv9Z4CEN04OrBEY0EvAWYC4Ex7TD0Q0bGGA8Cb6obH_Cs9nM4YIX8MWxZCzJRT9zcZKc9aaL-1J6gTwxkbM5W4A47xkm4kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جداسازی صدای خواننده از موزیک با هوش مصنوعی؛ تمیز و بدون دردسر!
🎤
🎧
بچه‌ها اگه دنبال ساختن نسخه کارائوکه هستید یا می‌خواید صدای خواننده رو برای ریمیکس بردارید، ابزار آنلاین
AI Vocal Remover
دقیقاً همون چیزیه که لازم دارید! با استفاده از مدل‌های صوتی AI، وکال و ساز رو در چند ثانیه مثل آب خوردن از هم سوا می‌کنه.
✅
🔺
پشتیبانی از انواع فرمت‌ها:
هم فایل صوتی (MP3، WAV، FLAC، M4A و...) و هم فایل‌های ویدیویی (MP4، WebM) رو به راحتی قبول می‌کنه.
🔺
بدون نیاز به ثبت‌نام و کاملاً رایگان:
پردازش تماماً در کلاود انجام میشه، قبل دانلود می‌تونید آنلاین پیش‌نمایش رو گوش بدید و تا یک ساعت خروجی MP3 یا WAV بگیرید.
🔺
کیفیت و دقت بالا:
تفکیک دقیق لایه‌های صدا بدون نویز و افت کیفیت محسوس سازها.
💡
نکته:
برای آهنگسازها، تدوین‌گرهای ویدیو و یوتیوبرها برای برداشتن کپی‌رایت یا ساخت بیت‌های بی‌کلام، این ابزار سریع‌ترین میانبر بدون نصب نرم‌افزارهای سنگینه!
🔗
آدرس ابزار
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7667" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7666">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prtgb2W10MFbIrSjtE-ziJkwZCv8NL5_-u2-lVVkD5tHJB1S2ArwfU-Oq99KgOYzTUj0lr4OtYCn5Ut9SHJ6uqYT_ztYYAutVmCsK-DFSihFGBQYTA6kwsaaRYu13e6ak9bv7fLNDbkIhJzbPdyVotsKEAU4YBCiQMUVAXh0WyIM21fDbVGemvbYtD-O0iE7e0bZzLnhNGkJD5FThzB1_ybOMv2ITkXIlM4KwBTddl6hdv_LISURhBaDWJMFah8WpMyJ-aOIwuFYkbTKzse4T0yKwXZ8U1Ca9yxfRHVO1r0hD5cqhmJfWW1vhMZtV2zCmllJYfku7PIhRAb75exqWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل گوشی اندرویدی به یک کامپیوتر دسکتاپ کامل با Android DEX!
🖥
📱
اگه از قابلیت محدود سامسونگ دکس خسته شدید یا گوشیتون اصلاً DeX نداره، این ابزار خوراکتونه! نرم‌افزار
Android DEX
با ترکیب جادویی ADB و موتور قدرتمند scrcpy، گوشی اندرویدی شما رو به یک سیستم‌عامل دسکتاپ واقعی با پنجره‌های شناور و کنترل کامل تبدیل می‌کنه.
🚀
🔺
تجربه دسکتاپ چندپنجره‌ای:
اجرای اپلیکیشن‌های اندروید در پنجره‌های تغییر سایزپذیر روی ویندوز، مک و لینوکس با اتصال باسیم یا بی‌سیم (Wi-Fi).
🔺
خوراک گیمرهای موبایل:
کی‌مپینگ حرفه‌ای کیبورد و ماوس، شبیه‌ساز جوی‌استیک WASD، قفل دید ۳۶۰ درجه شوتر (FPS Mouse Lock) و حتی شبیه‌سازی ژیروسکوپ!
🔺
دور زدن شناسایی امولاتور (No Ban):
چون بازی‌ها مستقیماً روی سخت‌افزار واقعی گوشی اجرا میشن، آنتی‌چیت بازی‌ها شما رو شبیه‌ساز تشخیص نمیده و بن نمی‌شید.
🔺
امکانات یکپارچه سیستم:
مدیریت اعلان‌ها، پخش صدا، انتقال فایل با درگ‌اند‌دراپ، رکورد صفحه و تعریف پروفایل‌های اختصاصی برای هر بازی.
💡
نحوه راه‌اندازی:
فقط کافیه گزینه USB Debugging (یا Wireless Debugging) رو توی Developer Options گوشیتون روشن کنید و برنامه رو اجرا کنید؛ بدون نیاز به روت!
🔗
گیت‌هاب پروژه
🔗
سایت پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7666" target="_blank">📅 14:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7665">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qazxhZX-RDwU9GjIMrFn4y6kPUXsc0Evr5AvkNHd3aVMd6geWYnrCQS4EU_vWVDuik7HayNjCLSXDdcqP4ViyhcHMiBH4C8f1OhowTGa5jfqN53hoOQQNbtVUe1rSGYHPcc8PnZwAbDnSQaMgLm914hkJSo7IVmkTjZuMVT-cFIKGbVYdMiFIO6xhevShrANsL85HRoaKO_ejIuoO7hHsjN_UDZ33jI9QfbB-e5yzz-tRUB1YKM47O2QESYKIqcHdrRBNOGeS8LUuV-VBBK8E29UyBodmmue9JnAglDCshdRI7baxYpF3pdgKCLWqn5LrXIQiYOmTlSAVleJJSk4RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معدن مقالات و دیتای آکادمیک اروپا؛ گنجینه‌ای که کمتر کسی می‌شناسه!
🎓
بچه‌ها اگه دنبال مقاله‌های خاص، دیتاست‌های خفن یا پژوهش‌های پروژه‌های اروپایی هستید که جای دیگه پیدا نمیشن، پلتفرم
OpenAIRE Explore
دقیقاً خوراکتونه! یه پایگاه عظیم با بیش از ۱۳۰ میلیون دیتای علمی دسته‌بندی‌شده و رایگان.
✨
🆓
🔺
آرشیو عظیم ۱۳۰ میلیونی:
دسترسی مستقیم به مقالات اوپن‌اکسس، دیتاست‌ها و حتی سورس‌کدهای پژوهشی پروژه‌های اروپایی.
🔺
بدون لاگین و کاملاً رایگان:
بدون دردسر ثبت‌نام، پی‌وال یا محدودیت دانلود، مستقیم به منابع معتبر دسترسی دارید.
🔺
ردیابی شبکه‌ای پژوهش‌ها:
می‌تونید خروجی‌های مختلف یک پروژه (مثلاً مقاله + دیتای خام + کد نرم‌افزاری) رو به‌صورت متصل به هم پیدا کنید.
💡
نکته طلایی:
برای پژوهشگرها، متخصصان هوش مصنوعی که دنبال دیتاست‌های تمیز و رسمی اروپا هستن، یا کسایی که دارن روی مقالات بین‌رشته‌ای کار می‌کنن، این ابزار مثل یک میانبر تمام‌عیار عمل می‌کنه!
🔗
وب‌سایت رسمی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7665" target="_blank">📅 14:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7664">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pwm-qrnPeELDgEwC7SJr_dsi0xH4Gwy7bmEXPI7jIESiZcSp7kVHcpDaWydzePGGM7HV-g4EfvDZUKhCBiGzzzXLYsLhAhuZgy1fhJk7dE2-UJ919YGCszuNzhc4wi_H8suDeM28obH_d7dyauVtTkYRZbhb0xDALVSyUkPB1Dd0bDvqz-xqZG8ANT_dpxjdHsm3ylvrvitHOT_VxcKYrPWZRn-YkP9SsEz5LRMmE2TS1JPR3aF1TuuC5l0UPMqr_35M4JWgzBYVi3QCNOhiiOWsXtbsL3882ulsDhXaRHIvyFqwfx2CnHV2ebZAn9aew9lM629uVNRV5y1R-7qM2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیبورد «شریک جرم»؛ قبل از ارسال پیام حواست به جریمه و حَبسش باشه!
🚨
بچه‌ها براتون یه پروژه به شدت سمی و دارک آوردم! این کیبورد اندرویدی اسمش «Соучастник» (هم‌دست / شریک جرم) هست و کارش اینه که موقع تایپ، متنتون رو آنالیز می‌کنه و آنلاین بهتون می‌گه ممکنه بابت این پیام چقدر جریمه بشید یا چند سال برید آب‌خنک بخورید!
😁
🔺
کاملاً لوکال و آفلاین:
نیازی به اینترنت نداره و داده‌ها از گوشی خارج نمیشن؛ با llama.cpp مدل جمع‌وجور Qwen3.5-0.8B رو آفلاین روی گوشی اجرا می‌کنه.
🔺
سیستم دوسطحی سریع:
اول با یه دیکشنری سریع کلمات حساس رو بررسی می‌کنه و بعد مدل هوش مصنوعی جرم یا تخلف بودن متن رو می‌سنجه.
🔺
پروژه کاملاً اوپن‌سورس:
کد و نحوه کارکردش روی گیت‌هاب قرار گرفته و برای گیک‌هایی که می‌خوان اجرای مدل سبک LLM داخل اپلیکیشن‌های اندرویدی رو یاد بگیرن عالیه.
💡
نکته:
هرچند قوانینش بر اساس مواد قانونی روسیه تنظیم شده، ولی معماری استفاده از مدل‌های فوق‌سبک لوکال برای پردازش آنی متن موقع تایپ، ایده به شدت خفن و قابل شخصی‌سازیه!
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7664" target="_blank">📅 14:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7662">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRYxcsubayUbOrogK74SjKORTUPU8ci1ED7LYNhleSbetqpp-rc-u16tDb3AVooNeJckJLKh2Qv0DuP4zYJcCgSpt2L1Y8SSWzZEAQme6QwYh7q4dB-2Dfxfu5ZMgIfu2os7ZZ6ICFaANgptEfL7G05pR5dr9wKOYnkdYO-F4Yyc_2NS-_7SDysHTVymW8pk0Zt0K8TQAQn0XFURoYqKOKN7qdZmvEtnL7KHCnU6IMRIFKzFOH8w9oQjGZ_TkFRJT3W9-Hno7oFUlM65Gt9duTJcFZ8H6dMKPRzbS7sbjviP6xYI4wSWgPyKzXdFk3Xp4Vzsfd5zAyhoY0T6wVBBYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طراحی و ساخت اپلیکیشن با M3E Canvas
🛠
📱
پلتفرم
M3E Canvas
یه پلتفرم اوپن‌سورس و جدیده که بهتون اجازه می‌ده با درگ‌اند‌دراپ و کمک هوش مصنوعی، برای اندروید و وب رابط کاربری بسازید.
🔺
طراحی سریع:
المان‌های آماده رو می‌چینید، رنگ و فونت رو شخصی‌سازی می‌کنید و همونجا تو مرورگر تست می‌گیرید.
🔺
تولید پرامپت جادویی:
جذاب‌ترین ویژگیش اینه که در نهایت از طراحی شما، یه پرامپت دقیق می‌سازه که می‌تونید مستقیم بدید به ابزارهایی مثل Claude Code یا Codex تا براتون تمیز و بی‌نقص کدنویسیش کنن!
📌
لینک دانلود / گیت‌هاب پروژه
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7659">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه
ArchiveTel
رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد
این ربات
رو استارت کنید
2️⃣
در چنل ربات جوین بشید
3️⃣
با آیپی خوب ترجیحا آمریکا وارد دکمه بشید تا سایت باز بشه و دکمه وریفای رو بزنید
‼️
نکته :
در هر گوشی فقط 1 بار میشه اگه میخواید با یک گوشی تعداد بیشتری بزنید باید هربار کلون های تلگرام رو نصب کنید  ، هر 5 رفرال برابر با 1 اکانت هست ، تمامی کریدیت های جمع شده تبدیل به اکانت میشه و قرعه کشی میشه و لینک فعال‌سازی به شما داده میشه
‼️
شرایط : حتما باید در چنل آرشیوتل عضو باشید
تاریخ برگزاری ، فردا دوشنبه ساعت 20
🚀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngUae9ZpdfTnI2ZLq9VuGrm23N-k8XCZqJsVnJeyLKkKdr0eueK7OB4OQPc_rrRDXHraIFZr_RzI4St8pIfY5O_F5QtHgaFxIxF_x-MvWkPZ76Hz4wqf6_jJ22Vq_j5MzWQkt_pmASG5poz-NLPMGK8k2z-cdOiUDf1I6Buyi20c8XGdlD7IuVqbc-8UAnJxzKRt1-ZYyvRwCshqbH7vmZG8hkxZAZG3_BIs1t_IQUoKik7LDPCCvUrzHtUh1HrhjFd7JrGQnGY7zZB0yIDIgkb1dYeyT2Wui0rf73KPsKEXtujnEJsjYA07O5qL9mkzIP3EJo-QxbXEElS7V1ELpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API هوش مصنوعی ها
💥
🆓
DeepSeek-V4-Flash-Vision-Exp | DeepSeek-V4-Flash-0731 | Qwen3.8-Flash-Next
✅
این سایت ثبت نامش کمی آزاردهنده هست بخاطر UI بدی که داره ، باید با گیتهاب لاگین کنید بعدش میره تو داشبورد و به ایمیلتون کد میفرسته و اون کد رو توی مراحل وریفای وارد کنید ( شماره تلفن لازم نیست ) حالا بگردید عقب و از سایت API دریافت کنید
✅
هر روز این سایت 1 PTS بهتون میده که معادل 10 دلار هست و خیلی زیاده برای این مدل ها
🚀
محدودیت هم هست 20 درخواست در دقیقه
‼️
📌
Base URL :
https://developer.amd.com.cn/radeon/api/v1
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL : https://api.b.ai/v1
📌
Model ID : deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید …</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8rGDmDTfaPRns53Spu-zNwoz0hGrLaAW21DVJE8C-zX1_ikVS1M3cHbsTBx9NglCFadXF5MgmV1aJtemK4ny3hRbpRp0xa9-kYduAH7scPhoimEHFkHnQgfd9Ou5tPVHKvhwRC2FzC3SAIb5CoBgQC9QvXciUWoOQR24inuXxnPK_Evu2SWr2hMW2A0VuHxCnjwjr4KJABUXfFB-xWnbqR5i2BRDaknUxDqDNVfIFZ-YM21Tw_aP7JUO6IUwACJMipZwwh1JPTjbyiQAuQUmyYRY6qC3TCcQeKRzZ8Pmr0icimjx9GwrWgHXNnH8Zey1cNSN8EfmkWIBw0Yhmeo1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به هوش منصوعی های محبوب
💥
🆓
Opus 5 | GLM 5.3 Flash | Deepseek V4 Flash | GLM 5.3 Flash
✅
4 میلیون توکن میده که میتونید استفاده کنید از API هر روز هم ۱ میلیون توکن میده برای opus 5 ( حد مصرف روزانه هر مدل ۱ میلیون توکن هست )
📌
Base URL :
https://helyxai.space/v1
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEPBFVBFyYHwMgVyKWIOIbJSJBRgQEuHLANWjQLUtX4jRbOpccZCMlN_KmTxLWDBoJZcJ6P0FOYLHa98_dUkmWPIQXZOd2jUpoGJmeyH3Hepr1dBPkQTUxtxks23PZoqy4YIiqJeQsogxMarFXzEhuuY32KelGRU99KF09y6htyKr_0pLu7LWg569lBcAh4CSVE055PbMx_sIzsgJETG8a4kxo8LD5rKqPPkYOTXdSomYFZgM6o_1eOWOS3CJAkFzBBPNzeVfCeGvLUWxZnTQf1B6_FPftuEnpsWIeCVSrFH0JVs4uUyfXfBe4HoCkXlTiPEi305q1X_OmlFY0T7AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏
اینم لیست مزایایی که داره:
‏• جمنای: ۱ سال رایگان
‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه
‏• جت‌برینز: ۵ سال استفاده از تمام ‌IDE⁩ها
‏• گیت‌هاب: پکیج کامل توسعه‌دهندگان
‏• آفیس ۳۶۵: نسخه کامل ورد، اکسل، پاورپوینت و تیمز
‏• فیگما: نسخه حرفه‌ای مادام‌العمر
‏• نوشن: اکانت پرمیوم مادام‌العمر
‏
برای دیدن آموزش کلیک کن
✅
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dz8jvQVICXy-OmtPX_W4F2RAGFYIVil_9ZWzTYWUuWPJsVBJqav1zhSRw3wHX3HqvFSZlN2UiOLX31wiPJKGcdOXVgdPd_v7TuwSGCPUvzBt2wLB2MVPADYbQYT-Te7X8wSEFFUAX9jwndPksYUPngM9XB8fRrNm8QDO9XGrNuQRBf7XVpyDAqtJMHkrJ_9Hdfp0OvBES31T3IOjpoReKm-3uelZEt1IIChx1RkSnnlvVhQRknExZi-sL6uowlYJlJpPlmpbIdKuSVZ50-A_5NiPFZ5ABVYt1BhrnK5cS_dbj2wG6xdRO2Yjj93cauXSeiBbBNNyhAmmNHTwiIHPRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
داستان GPT-6 چیه؟ انقلاب هوش مصنوعی یا فقط شوآف تبلیغاتی؟
🤔
این روزها همه جا پر شده از اخبار رکوردشکنی GPT-6 Astra و نمره عجیب ۹۹.۹٪ در بنچمارک ARC-AGI-3.
طبق بررسی‌هایی که کردم، این نتیجه تو شرایط کاملاً ایزوله و خاص ثبت شده و توسط منابع مستقل تایید نشده.
قیمت‌گذاریش هم به شدت نجومیه؛ هر یک میلیون توکن ورودی ۱۰ دلار، و خروجی ۵۰ دلارِ ناقابل
😁
(مقایسه کنین با جمینای ۳.۸ که ۳.۷۵ دلاره)
در ازای این هزینه سرسام‌آور، وقتی در کل حساب کنید، برتری خاصی نسبت به رقبای خودش مثل Fable 5 نداره.
یکی از معدود بنچمارک‌هایی که هنوز اشباع نشده و به نظرم بهترین معیار برای ارزیابی مدل‌هاست، بنچمارک Humanity's Last Exam عه
تو این تست، عسترا نمره ۵۷٪ رو ثبت کرده؛ در حالی که Fable 5 با قیمتی مشابه و حتی پایین تر، نمره‌ش نزدیک به ۵۸٪ عه
🔥
با دیدن همین آمار میشه گفت OpenAI با این Gimmick های تبلیغاتی، رسماً داره به شعور کاربراش توهین می‌کنه
😐
من حتی کاربرشم نیستم ولی باز به شعورم توهین شد
#طهلیل_ai
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUr1d-TvFYNC2CDKTPI__goo0-a0gc7UYXF_G1u8MH57UT8AkCzFfO_kPPg4Q7obHa4Cs41XyEQGUOnt0iy04lWJkfM7rdiUHtWn7J_VlNruV1LOyD1A0niBHSraHfeHn5rBFNelMlqlsWq89Ytlsc4FfZrpfHDlWeEsg5ePkPADbAK3zdLL3YOg3Tuu6LvI1iREe5wKnUFQ5C3b8OfYQ7zA_q6jb6KvIMRu_psKB6VE2M_4d1S2ReI3lof4VqQBcdnHhnsDKMS-bTcIlDIXlqPVqcoM2C-xlBPY0_lPAKVkubeyqSkwtRv1LeZJBp_yvbXiAX-sM2UpcbDXKe9u9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Free 2k$ model GPT
💵
📌
Base URL:
https://vip.9aws.net/v1
📌
API KEY: sk-g926rIr0SG7pfoD4WextkZwRRAgFOwYZDsG5hnDr8mL2ZH9d
📌
Models:
gpt-5.5
gpt-5.6-sol
gpt-6-astra
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KN1ykQu4-XnNP7K-veS1QToRbMGMwL0du1N_jblqg-KpRcUjO-pGO-Yr5q98CRafYr4unXcfDQXE7TC__INQ-WTcPyItuWEPQ9N5z9LwZuDHScGoFRYeGzpA2AiXAKbbWFs4efANTyhDe_nYLxean_VbFJgqPP1NqqDYucQIMXGsOFav3DNsVylw7niI0htvBq_nXnu_33G3ZCLEMgxGj4mNrk8sE6as4KnGZrCdkLO3_weX-S0ta1Gho8ivLXat76ukFj-W8uzkCUuPXWBIV4FOorK4fAsZqIzqKpOQ_Ye6JypowqjOYrbjEh5m39fOsWz0iFRaGQQEjimy9y8oQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی آزمایشی رایگان به مدل‌های پیشرفته هوش مصنوعی
💥
🆓
Opus 5 | GPT 6 Astra
✅
سایت ClickUp فقط یک ابزار مدیریت پروژه نیست؛ ClickUp Brain حالا امکان استفاده از مدل‌های مختلف هوش مصنوعی را در محیط کاری ClickUp فراهم می‌کند. طبق مستندات رسمی، مدل‌های OpenAI، Claude و Gemini در Brain قابل انتخاب هستند و می‌توان بین مدل‌ها حتی در یک گفت‌وگو جابه‌جا شد.
🚀
🎁
سهمیه رایگان
در پلن Free Forever، نسخه آزمایشی Brain شامل ۲۵ استفاده برای هر Workspace تا ۱۰ نفر است. در Workspace های بیش از ۱۰ نفر، این مقدار ۵۰ استفاده است.
✨
⚠️
این سهمیه ریست نمی‌شود و پس از مصرف، برای استفاده گسترده‌تر باید پلن/افزونه پولی تهیه شود.
🤖
حالت Agent هم دارد؟ بله!
دارای دو نوع Agent است:
• Super Agents برای انجام کارهای چندمرحله‌ای، تحقیق، کار با اطلاعات
Workspace و اجرای workflow ها
• Autopilot Agents برای انجام خودکار اقدامات بر اساس trigger و شرایط مشخص
💡
علاوه بر چت معمولی، Brain می‌تواند روی فایل‌ها و اطلاعات Workspace کار کند، جست‌وجو و تحقیق انجام دهد و حتی Task، Doc، گزارش، اسلاید و موارد دیگر ایجاد کند.
🔗
لینک وب سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozirwLL6u56_7F1vfkahmaW8NSUD_zOXs9mXbVPLRUAEOh0KogU2Xms70y-BGnlnnyPan2WW6zzgldA_Dlw9NGxMek7Cf1yo7PEUThtCynx6tfa4b1VTqPlSEVXY0iRFI7O6SbMCruiOvAn7UK_vWIiT2iT8t32m6bMAir8PV0b9YMLCU98Ja5Wx5pLeLbnlhBg5TO88uAnWthvtPnwoUtERjdAihQ3ZRvsiCkiADpI7h_0VkctiL54zuj-66zNWRwT6mY2PN5zxCJpBWV2HigOTL9fuAjjNTbuChadvN3-S-GbvbhnYyXRIFJqfDjKLmzyM9cIfxVZWRgsdYEZr2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های هوش منصوعی
🚀
🆓
Opus 5 | Grok 4.6 | Deepseek V4 Flash
✅
برید تو سایت زیر ثبت نام کنید و موقع گرفتن api باید گروه Free رو انتخاب کنید از این گروه این سه مدل بالا رو تست کردم جواب دادن ، بقیه چیزای خوبش کار نکردن این مدل ها رایگان هستن و کریدیت نمی‌خوان
✅
📌
Base URL :
https://kiosapi.com/v1
اینم کلید خودمه اگه دوست داشتید میتونید تست کنید ریت لیمیتش رو نمیدونم
📌
Keys :
sk-ZoCd9hc91if9INutCoTC6zA0wJ2pbrd9a75GQJTyj5V4gIup
🔗
https://kiosapi.com
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BijV4f_MxKKzOVGe0NFNYt7R1XA1nedGrViTcrBL1gbI1kN7WQRpe94iY7sXZQHP1BxFIngLgE6JZ1yj0Xa2luH0bjBIxiPHSAwDSlPGQZGBWVPNC7sLgF9L1MEVX3XB-_KulzVcPXtGRFkPlUBmfDG-G0Gktzf5o4O9uM0mxIanXRRdmwnrrwM6YZzt7dIFw3ep_JTSzrzTnlsML59oc4CdN1pZXQIu9L9Je0rdAu7jJK8PLqERODgvRime9rPVoSXQ--x2PM9jUroLZlFrm8kWOAl1-zHrK2cevISNxoRkc6XIORJn2lRbh6JvaVfT0aEPf0JcIvdY-ENzeRy_FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5000
دلار
😎
📌
Base URL :
https://vip.9aws.net/v1
📌
Keys : sk-faNuu4uK9WqIYAiXjdmYxeX6PI1Z5wNLzCsIXKbKVQ67W1rG
📌
Model ID : claude-opus-5
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTQVb8GNNbb9CZOEUS40jl_XzOWI8eMInyWKxjUrMuha5IaTcP_VHK40V9lHlqZUkZBoJ-OqTn0rZ--E54IlCcvROfW4eQ0gPCpcYHTPAmF077AFmL-BXTPHzHYH7tDyoMsdVRB_DYs7nz_L1tSW9lSWWRS-pc99ogbLTpGQjsqIHauGgv8spoIWkthkWNsetxXLRct8QxbqYzcUpCyFAXG9wjvxttPBpj5Hg2N-Fw5_RtPlHxLgoxqjF3A8mDEQXew4-ezMe9UVAT_fSNElAi7W1CpgQqrEdsJsToUY4s-HGjeCR84FRdwl9qMqUf9FbtdsqsQ3G-L3YZ0gOb9_wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ساخت وبسایت ۱۰۰٪ رایگان، فقط با یک کلیک!
​سایت شخصی یا پورتفولیو می‌خوای اما حوصله خرید هاست و دردسر کانفیگ رو نداری؟ این پلتفرم اوپن‌سورس رو دقیقاً برای همین ساختم.
​
🔥
چرا ZeroWeb؟
​
💰
بدون هزینه هاست: کاملاً رایگان و مادام‌العمر روی سرورهای کلودفلر.
​
🤖
مدیریت با تلگرام: پیام‌های فرم تماس سایت مستقیم میاد تو تلگرامت و همونجا جواب میدی میاد تو سایت.
​
⚡️
نصب با یک کلیک: فقط روی deploy.bat دابل‌کلیک کن، تو ۱ دقیقه سایتت بالاست.
​کدها و آموزش کاملش رو تو گیت‌هاب گذاشتم. همین الان دانلود کن و سایتت رو بساز
👇
​
🔗
https://github.com/faithsaly5-stack/ZeroWeb
​
⭐️
خوشتون اومد استار بدین
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJXOv8rxoEYxwJu-asaO-TLCFwwFPcU1EXT6vGetkTNCYo3gALNM6L59UwVnDTEMxClks1Yk2L1FITyIxYsOiI8TpfH7GwpU7xjkfVsdMTMkDATPqU-P92W5wl3h2Nz_-brsR0uUXpBW9W9SxOSeINaASwZ_DFFLY2xipwwFDthP3JTIFoX5xEyrpsG3GwJUxjpN_5_pBmxvHvVgVQlqsMqxiqIY6ZfObMadSHZR8Lc1oycuYetdOVt3bIHMTcMJ-BXyGiqLD45TA9zNn2XUB4dd2PqS0wZfslbMGUP5C-0s08pv97weSbPa9LC10wf_DtGaTlH-VqLOkbHnpAkJqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM-5.3-Flash به صورت رایگان
💥
🆓
شرکت z.ai کمپین Global Build رو تو اپلیکیشن ZCode راه انداخته — از ۳ تا ۱۸ سپتامبر
🌎
⏰
دسترسی روزانه: ۱۰ ساعت ،  به وقت تهران: ۱۸:۳۰ تا ۰۴:۳۰
👑
کاربران Coding Plan: هر روز، تمام ۱۵ روز، رایگان و کامل
🥚
کاربران جدید…</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7645">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIdo3f2QcQtgpRakfLR_vOf0-jve9VM7qcu3obuUonAYJEuy5dWyh5m3RR0RDKRjV026zB_m-mjVvWpngExQ9-ecIo8yacCZGZl_r91-8VKG5pgYierAN_C9xxwqTpgXaGnO0ZzcQCFPufqmA1b-N6SUkHwaeCAetY8QbeOXUFbhRPlUji_ssih_TZIEfsHS7hzvSJC2XAYawDbJngHR66IKRzf4K1NGkzg7KCio25-fk2aHmyh7ITLi6Jg8P29jiAZVZGhPim61Tx7mtvqj4i7JPW09fggRnCE2VJmi_iBldKeoEvBTdVE0UzQDKj4bHItdIt4fVxVGep8BFlqIsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1,000 دلار
😎
💵
📌
Keys :
sk-ByTi6xCfB7Pt1N8Hp9z7VdsRwGIMM5pdnh4CsorUfflysvbq
📌
Base URL :
https://tabitoken.com/v1
📌
Model ID :
claude-opus-5
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfTwYkfapLAWHgrWUmFyrMERDRab3iXPco4M0oZyDkP4yztcQ3R0CcCJScEFAqjSU2Ar4YKUV8diDwPzVN6fS_yLCcLnzGNG_jS4Q_9NzAbt5vj1JWwB_r-GedXPfT2tUwqc3QJ68Ssmti0wf1NExYdBAmSxcjg152FObSNjUZVzwv_W2fiMzwsNFAFblmqNS4EBRm0YluPX-2CpLgTJkFRmoxxB0z5a8G-JNmjIDPQxZTnObHyfDd_3nc7blEhH-U0-HfM1Eobz6rVw280PGOaDRmXqsGDHF5bND8ulmronsXJn0xGWRnC-8cvUmHt6_8czi_GMMSVf152U9rHTww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snQmL-gkc8-ZAhAk_iVGWkEwKV5IPoQS8qF-5VARnZ00gYMDgOKzlYN4__PT1_hXlbIWViGlsJ9u7fRZSL7PsJRXJVsMvI8kTXLKZkQbjlCVs7tiWqCziA4B4HhWvQnmuQzM31BDvFYg2H71_PcJxjS1KINQpDGJqMsfQCRKGKeN6VYhY-Y2AlMyv6lv4sS5xv4pLsowSMsIMSXhldBhVsSoHk1bsbb-Wg4uHaVjkY55pHl2-351n1nv-0IHAmxR24kFdyEHv8EAbWzTdf4_iniIL7WAdZ_xVOem7EpKJA2P_7IJzWP9Ww8FB-l_r56oR0cmwX8AzoejcfoGXGf3wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت هم به دلایل نامعلومی میاد API مدل های Fable 5.1 و GPT 6 Astra رو میده ایشالا که خیره
📌
Base URL :
https://api.experientiallabs.ai/v1
ماهانه 5 دلار میده و همچنین فکرکنم Fable و Astra کلا رایگانه
تست کردم اوکی بود
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3gqX_i_3SkWjbkfvNZr-ZwogsuoIfdJGqXyHQJbeLNWZrKJhPf8xdi3S2j_avYVashGRPnT_Qj-H2u0G305NppAGI7G4ZqKujvZdSpG4_o2rbpgW_iYNGVn7Du7Vw8mhyQB7Q8SJhjGVFkhfSUG_vl0dE9MbpwMK7cu0Xcn1O0-cEWNhOXM0rbzyPFAm4s9zkff0488_eTW8rBr7GiIsR8wrwWGWBlAdzTwerKoGyjtyMqQYcIEuZzfgWzdje3GX3nuT-tNpphBrIbwsMBWIKgf61UYiGec_YBqmob8QngKu-9eIGs0t43epEE2CzdcnBKNONgUdCukGwrUg28Rkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=b9PkbCXhB8UJ92XIf9pJ0S_0QiIDww9bETyjzT8zGtjt53_zmnz8WpFH4cIybOEG5wPQxGOPJjXncYGhubx4od6kk-T8GqrlYQDwy3Y8FTFLn2pLeNZGy3_oNP7TS71ivISsAuDbXLAO3Y5rg1W6fm45wKjf7iN3aKuqtygLs0rB64mYN0lJE6lwrmiTOIncR6MiaxOmx8ftexPy1c0cI8jAst4uYlHR7lQY38e5UP3rkfqnAynnGDFasbrSH-g0wGY_Mngym5I9-vjg9ChPtlgkjROvMDrrT7Cusm9UfyQ_-3e5mJ3IskFHTEvX6FcKPNOGNvPHZQfm7Xw9XB8McA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=b9PkbCXhB8UJ92XIf9pJ0S_0QiIDww9bETyjzT8zGtjt53_zmnz8WpFH4cIybOEG5wPQxGOPJjXncYGhubx4od6kk-T8GqrlYQDwy3Y8FTFLn2pLeNZGy3_oNP7TS71ivISsAuDbXLAO3Y5rg1W6fm45wKjf7iN3aKuqtygLs0rB64mYN0lJE6lwrmiTOIncR6MiaxOmx8ftexPy1c0cI8jAst4uYlHR7lQY38e5UP3rkfqnAynnGDFasbrSH-g0wGY_Mngym5I9-vjg9ChPtlgkjROvMDrrT7Cusm9UfyQ_-3e5mJ3IskFHTEvX6FcKPNOGNvPHZQfm7Xw9XB8McA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هوش مصنوعی حالا می‌تونه با YouTube کار کنه!
یک قابلیت جدید به نام youtube-skills به ایجنت‌های هوش مصنوعی اجازه می‌ده فراتر از باز کردن ساده‌ی ویدیوها، مستقیماً با محتوای YouTube کار کنن.
🤖
🚀
قابلیت‌های اصلی:
🔺
استخراج ترنسکریپت کامل ویدیو همراه با تایم‌کدهای دقیق
🔺
جست‌وجوی ویدیو بر اساس موضوع و پیمایش کانال‌ها
🔺
دسترسی به ویدیوهای جدید و محتوای پلی‌لیست‌ها
🔺
دانلود زیرنویس‌ها
🔺
پردازش گسترده‌ی محتوا؛ از جمع‌آوری ترنسکریپت‌های یک کانال یا پلی‌لیست گرفته تا تحلیل چندین ویدیو
🔺
امکان انجام تحقیقات عمیق با بررسی هم‌زمان چند ویدیو درباره یک موضوع
📊
یعنی ایجنت می‌تونه ویدیوهای مختلف رو جمع‌آوری کنه، متن اون‌ها رو استخراج کنه و برای تحقیق و تحلیل از محتوای YouTube استفاده کنه.
⚡️
مناسب برای ساخت AI Agent، تحقیق، جمع‌آوری اطلاعات و تحلیل خودکار محتوای YouTube.
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDnd7fnAworDFSRsSBzdYrXa2vOU19Mab6knsH_gBo5SVq_baSSGSXFaAkQFcLXzf77mnneGEyhRfCVz0w26_u_ysq9YCy0T2YgxmeBDZJ_O6xbEv1E_ZuCoz6ov7cDwjSIxD_gV3uoRUUU1hHUADOC3PLt9kgp9tWjFufI0jPxMMMJWBxRTlwj6AD1z5wCJdI0RizDDTU6XaWwXGvp9euhsWOCpNIO5B81k6T6Uw9APB_VJc7l2C8HBdWZu3HLTUX31yhDoVsS2ruOJ_iYqqcFt_Vb0UgP8e9DQR9qO-Q4_9sy5VrXRcCXf47zIlc2W7gxuTIf8M7SgtSHVJuutWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">200 دلار برای دسترسی به مدل‌های هوش مصنوعی محبوب
💥
🆓
Kimi K3 | Deepseek V4 Pro | Deepseek V4 Flash | Sonnet 4.6 | Haiku 4.5 | GPT OSS 120B
✅
کافیه با جیمیل ثبت نام کنید و یک کلید API دریافت کنید تا 100 دلار دریافت کنید
✅
📌
Base URL :
https://api.you.com/v1
📌
Example Model ID :
kimi-k3
حالا برید بخش تکمیل پروفایل و یک ایمیل با دامنه ناشناخته وارد کنید
مثلا تمپ میل
سپس 100 دلار اضافه دریافت کنید
😎
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎯
چالشی بزرگ برای وایب کدر ها به همراه جایزه
اون لحظه‌ای که به یه دایره چرخان خیره شدی و منتظر جواب هوش مصنوعی موندی؟ Commons میگه این وضعیت روزانه
۳۰ میلیون ساعت
از وقت آدم‌ها رو می‌بلعه و حالا با پول جدی می‌خواد حلش کنه.
😎
💵
🎮
چالش چیه؟
به‌جای یه پروژه‌ی کلی «چیزی با AI بساز»، این‌بار هدف مشخصه: زمان انتظار برای پاسخ هوش مصنوعی رو به یه تجربه‌ی سرگرم‌کننده تبدیل کن. یه بازی کوچیک، یه تجسم تعاملی، یا هر ایده‌ی تازه‌ای که به ذهنت می‌رسه.
🚀
⚖️
داوری روی زیبایی کد نیست؛ روی کیفیت خود تجربه‌ی انتظار، اصالت ایده، ارتباطش با AI، قابلیت استفاده‌ی دوباره و کیفیت اجرا تمرکز داره.
💰
جوایز:
🥇
نفر اول → 20000$
🥈
نفر دوم → 8000$
🥉
نفر سوم → 4000$
🏅
رتبه‌های ۴ تا ۱۹ → هرکدوم 500$
🔐
+ 20000$ جدا برای بخش ویژه
📌
مراحل شرکت:
ثبت‌نام تو
commonsmade.com
← بخش Hackathons ← Join the hackathon ← ساخت پروژه تو بخش Code ← وقتی آماده شد Publish کن و تو Hackathons ارسالش کن
✅
🗓
مهلت: ۱۷ سپتامبر | کاملا رایگان
اگه مدت‌هاست دنبال بهونه‌ای برای یه پروژه‌ی وایب کدینگ بودی، این هم خلاصه‌ی مشخص داره، هم جای خالی تو نمونه‌کارت رو پر می‌کنه، هم یه جایزه‌ی جدیه
✨
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7635">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAdHvkH_CRIHTAkhGhzRPJSRdNvm0-kouO8W-liYuL0WNSobzu-JrwPUqHXQsYXMNXlb8OxJNOVStQwreCFKXL6E_98c3mpMm00RTJJPQtBLOrR1Egt2_LPAF6_vxfHZX2yuiECkDdrCMtTjwo8zfSRQle7jMu-n_VgxTKuaXxsVoMuvXKLienwDeTV_yss7jtPdTOGHCrt_w1g6cQXtF1COaIt7NyCjHi1f4pD_GC7Bb4LUXJVmGl6UvotG05gJ4mR_Dwo3CkrqRze7EswhKZE1AnweVWQKRP_a5toq6xZjSJgIQUI9wX9q_vTv1kh73l75jTOyVoW8Zm4aoJlQDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM-5.3-Flash به صورت رایگان
💥
🆓
شرکت
z.ai
کمپین Global Build رو تو اپلیکیشن ZCode راه انداخته — از ۳ تا ۱۸ سپتامبر
🌎
⏰
دسترسی روزانه:
۱۰ ساعت ،  به وقت تهران: ۱۸:۳۰ تا ۰۴:۳۰
👑
کاربران Coding Plan:
هر روز، تمام ۱۵ روز، رایگان و کامل
🥚
کاربران جدید عادی
: یک‌بار ۱۰۰ میلیون توکن رایگان موقع ثبت‌نام (تا پایان کمپین باید مصرف بشه ، با اکانت جدید ثبت نام کنید )
⚠️
توکن‌های رایگان فقط داخل خود اپ ZCode کار می‌کنن، نه از طریق API.
🔗
لینک سایت
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=DSUHoM5VPaJbSidh6yOyj91d7w8CRtjmCPJfW9LiU3fOzRUG9exnAWxkdNe9eDkN3iTDRtVXPN0MQLfSWCrDJuySS8uIxfKMW1o_CrkLrKACpmacfPW8K5FW7GjZX2n1cxOfqwIfkcygq4EbjlTrqyAQQ_qOivFfW14op04vxMBzw-V8yMuH6Tz3ydar42XwanyX73eLFI6ksaC7KVpzdmeARcf1xG0vnIcqfDUvEU2fLckpdsi_hlmmKSCOb6IVL80qLI5cXA8XSqRPtIq93zlHe4qEX1dzU7c5XQoOrfQcUgDmoV-YvEF8qVf6LgpNpsZEWu4dUb3_Ft2fm80Xow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=DSUHoM5VPaJbSidh6yOyj91d7w8CRtjmCPJfW9LiU3fOzRUG9exnAWxkdNe9eDkN3iTDRtVXPN0MQLfSWCrDJuySS8uIxfKMW1o_CrkLrKACpmacfPW8K5FW7GjZX2n1cxOfqwIfkcygq4EbjlTrqyAQQ_qOivFfW14op04vxMBzw-V8yMuH6Tz3ydar42XwanyX73eLFI6ksaC7KVpzdmeARcf1xG0vnIcqfDUvEU2fLckpdsi_hlmmKSCOb6IVL80qLI5cXA8XSqRPtIq93zlHe4qEX1dzU7c5XQoOrfQcUgDmoV-YvEF8qVf6LgpNpsZEWu4dUb3_Ft2fm80Xow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌍
Pythia — رادار زنده جهان برای هوش مصنوعی
ابزاری متن‌باز که وضعیت لحظه‌ای کل دنیا رو جمع می‌کنه و بهت میگه احتمالاً چه اتفاقی قراره بیفته
🛰
🔺
بیش از ۴۰ منبع خبری و اطلاعاتی رو هم‌زمان رصد می‌کنه (اخبار، درگیری، بلایای طبیعی، هشدار آب‌وهوا و...)
🔺
پیش‌بینی از فردا تا یک سال آینده
🔺
کاملاً رایگان، روی سیستم خودت اجرا میشه — بدون اینترنت، بدون سرویس ابری
🔗
لینک گیت‌هاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=YFboPp8YciUxrDX6HWtblnK7Qh_1YPYrTIPc5eR3d47P1dUwIsa7d7ToomV_HHwYyHxNFjlcOxPGrkzP1GzCFIqJiSV_YKCbuTzYMeG6NuWi8XBNwnFphFmq_YHiUPXGSlmtuliLrrR2Q3X0DdcHRGHpIQC4iEGiJpt1D8dDZEkKbUYO0KdZpRQbRr_2NHm3-d8agMZ6d1avkt5CCRWaYoW1lnEFrJ4CPPiX6J6L7rnKY95kb8-337BE_BvOPexmB3z_N-1uY7enxZH78yb4Pd5qeObEBTl2hBxdcVVyZufU9VdukLK93BTxFtjnCU5TPEXRjGZrczEnVC90wIxWSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=YFboPp8YciUxrDX6HWtblnK7Qh_1YPYrTIPc5eR3d47P1dUwIsa7d7ToomV_HHwYyHxNFjlcOxPGrkzP1GzCFIqJiSV_YKCbuTzYMeG6NuWi8XBNwnFphFmq_YHiUPXGSlmtuliLrrR2Q3X0DdcHRGHpIQC4iEGiJpt1D8dDZEkKbUYO0KdZpRQbRr_2NHm3-d8agMZ6d1avkt5CCRWaYoW1lnEFrJ4CPPiX6J6L7rnKY95kb8-337BE_BvOPexmB3z_N-1uY7enxZH78yb4Pd5qeObEBTl2hBxdcVVyZufU9VdukLK93BTxFtjnCU5TPEXRjGZrczEnVC90wIxWSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
شرکت Anthropic ابزار رسمی بررسی محتوای Claude رو منتشر کرده
راهی برای فهمیدن اینکه یه فایل با Claude ساخته یا ویرایش شده — مستقیم تو مرورگر، بدون آپلود
🔒
📎
دنبال یه نشونه امضاشده (C2PA Content Credential) می‌گرده که Claude موقع تولید عکس، ویدیو یا صدا داخلش می‌ذاره.
🖼
فرمت‌ها: عکس، ویدیو و صدا (تا ۱۰۰ مگابایت)
⚠️
محدودیت‌ها:
🔺
فقط نشونه Claude رو تشخیص میده، نه هوش‌مصنوعی‌های دیگه
🔺
نتیجه «پیدا نشد» یعنی نامشخص، نه «قطعاً انسانی» — این نشونه با ادیت یا اسکرین‌شات پاک میشه
🔺
هیچ اطلاعاتی درباره سازنده فایل نشون نمیده
🔗
لینک ابزار
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=TlcwjjQ4Adw6rjlXit1uI90W19Buz7AOTCKxzBXLFKjPLoJOmPIwegW52MSdoTpjUCjFTO9o1tmOyqM7ksnUr8zhfaMNpw8mDTCrJ0PLVRDCVBNX9fI9EhjSG6pCLKJyZd1iEN7yJF6H0JAI7RTl6v0TOlsX-jhnurg4s489m88CaXdi312sNgTvuTIWdZik0dii86vrYJ3fdgMcRRiwjQUeoJ1GpyFzhidbm8ygZH3NhRWJd3Hs3RN60PNreYTUuqttxVMr2uJtI3a5RvQ7KxyAT1fHX1VQYn0NJnmK9hMSQ5qMHKyUwCtEAEcXXspmnMK18mRaDR-5KP68Q-E3KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=TlcwjjQ4Adw6rjlXit1uI90W19Buz7AOTCKxzBXLFKjPLoJOmPIwegW52MSdoTpjUCjFTO9o1tmOyqM7ksnUr8zhfaMNpw8mDTCrJ0PLVRDCVBNX9fI9EhjSG6pCLKJyZd1iEN7yJF6H0JAI7RTl6v0TOlsX-jhnurg4s489m88CaXdi312sNgTvuTIWdZik0dii86vrYJ3fdgMcRRiwjQUeoJ1GpyFzhidbm8ygZH3NhRWJd3Hs3RN60PNreYTUuqttxVMr2uJtI3a5RvQ7KxyAT1fHX1VQYn0NJnmK9hMSQ5qMHKyUwCtEAEcXXspmnMK18mRaDR-5KP68Q-E3KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساخت رایگان ویدیو با مدل قدرتمند Seedance 2.5
🎬
🆓
خبر خوب برای علاقه‌مندان به هوش مصنوعی! سایت Dola مدل Seedance 2.5 رو به خودش اضافه کرده و حالا می‌تونید هر روز به‌صورت رایگان با این مدل ویدیوهای جذاب بسازید و لذت ببرید.
🍸
🎉
✨
ویژگی‌ها:
🔺
تولید ویدیو به صورت…</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7631">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1W6X1Tau9PlEwutGi0nlx7eKnW_ucoXj0cocnbCjdpA1pl29UdycL5mPmr7EQn5t4gHhJzMFePEA4oeRYz5rv_ehlWtOUrqXZgfoIQaj9Rb_JlkqweC3_uMuscC43IrSwgMnnQE6ykGrV2ibZ9Em4cBessl_YJE3X4D_3cPOsNwoPbS995d6GT10bPJvmicMy0jBJGN_OhbLv6wjaoRMwTzkfG4x1IELndmGDd4Wdx1gfO2oCUk3y32wwIi-6EY2KtUO3uKAme715SMJWMI2ajjZIpoS9daKOyyaqj7nMzJb3HE80j5TsU9iIoZoYtKSR18W7EUMcbZRnzMFFPrYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن API رایگان GLM-5.3 از طریق TokenRouter
💥
🆓
بدون کارت اعتباری، مستقیم قابل اتصال به اپ، چت‌بات، اسکریپت یا هر ابزار هوش مصنوعی دیگه‌ای
🤖
📌
راه‌اندازی:
1️⃣
ثبت‌نام یا ورود به حساب TokenRouter
2️⃣
ساخت API Key
3️⃣
تنظیم Base URL:
https://api.tokenrouter.com/v1
4️⃣
انتخاب مدل:
z-ai/glm-5.3-free
⚠️
نکته :
به دلیل رایگان بودن ، مدل کمی کند هست و باید در ساعات خلوت استفاده کنید ، محدودیت و ریت لیمیتی اعلام نشده ، این پیشنهاد به مدت محدود در دسترس هست
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=umH-RJbUNbpX3rv1_lr3AUmc-ZQ_QXS0nBOiI4qE_w_TjVMNr6fTI_SSZfFj6jiHbM9pxMV5QRuTbYP1mzFdfouRj3qech7V94PgCETdopfu2pdgFHKFFd-U1_uZt0rU0NU_K0jmSDWNZxh323nIwRv5EkvyyzHJ8TQbXSlOsJP15jhejndJOCFwbjPubcAN2pfFugWUzvKFwUvF-HG1opdp27YNwNLOLi3enoG1_S6y33s5-EoqYvGWoMf4kxPujCXg9jB3jstqecs-H4LDg9da_D66L7ursIDjnixmTI9gkd8JLGADGAynQB9NR6wBGd1SOVoQoDru4aYSmUVXTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=umH-RJbUNbpX3rv1_lr3AUmc-ZQ_QXS0nBOiI4qE_w_TjVMNr6fTI_SSZfFj6jiHbM9pxMV5QRuTbYP1mzFdfouRj3qech7V94PgCETdopfu2pdgFHKFFd-U1_uZt0rU0NU_K0jmSDWNZxh323nIwRv5EkvyyzHJ8TQbXSlOsJP15jhejndJOCFwbjPubcAN2pfFugWUzvKFwUvF-HG1opdp27YNwNLOLi3enoG1_S6y33s5-EoqYvGWoMf4kxPujCXg9jB3jstqecs-H4LDg9da_D66L7ursIDjnixmTI9gkd8JLGADGAynQB9NR6wBGd1SOVoQoDru4aYSmUVXTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثر های شگفت انگیزی که تا الان توسط GPT 6 Astra خلق شدن
🚀
✨
🔗
منبع اول
🔗
منبع دوم
🔗
منبع سوم
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7623" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7622">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFkdOd_RcnRr3rpE3QG3HHMv_8kSXD6SBlnTLOb2BJ_C4N6hwbLtrBpqydJxQMd0rRftyGeWQqQr3Cyf9wYcKl2k8VSrwfDgQLAU4pB3iGdo25OFSGtfHZGEeWYQ_0vTJ14wnrcEIUnd_-B8EoORxQb7wO4-eW2FAze0-U37zKuInVPcsNSwd7vXDrlg263p2NpR6wUAYNFRuRfDKnRw11DEotkghn56UZ6TNbKwWPeZBbIu0TNBOc4ROpWA9KPV6Twg-YX_d06nWe7S2OH1LbVE-JD-5m37gVRARSOuyNnA_oRV6DhLfNI7qJjRoPz3LvWQfxlBk9yncd_rR4ywfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
کتابخانه پرامپت YouMind
بیش از ۳۰٬۰۰۰ پرامپت آماده برای هوش مصنوعی
100% رایگان و هر روز آپدیت می‌شه
⏱
📦
چی توش هست؟
🖼
پرامپت تصویر (+۳۲ هزار)
🎬
پرامپت ویدیو (+۹ هزار)
🌐
پرامپت طراحی صفحه وب
⚡️
بر اساس مدل‌های داغ:
GPT Image 2 · Nano Banana Pro · Seedance · Gemini · Grok Imagine
🗂
دسته‌بندی حرفه‌ای بر اساس سبک، کاربرد و موضوع (پرتره، انیمه، سینمایی، سفر، اکشن و...)
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7620">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCxCzTqZvRBH9fQO130b29anAAMTGfTLRIK3DpxiOZmiu7cu_WdTRoFa9sXBt9AQPAwf9m0XaNwWC6IkDs1Oc1lpEJhtU844HN530BkFHbX8KPxwoHCu68OmW7_TKPYXVXlz3rVTAUxdZL__rbuERZyuEWDpD_S-99qXkBZfCzMqa6moGPXBA5VFyFLz4Vp7mIQ7sjoSqDjykAuAKdZU4jl_yE4GRUV8jMofrDr3PZywDpGGl2woR7HMdhsE0Sx9722YAiklosD5AQuWIdWHOE-TwzNKkAEGeHWf8FPZ5v86Er3Ab6tNLWGE-0KAr7wlPHv869zfldMHQCR8TxDGvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5.1 2 days Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=claude-fable-5.1-high
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlmoEfVImFdC2YF7Fr5MogaGOf_oNi6n9MsrRIa3XW1I4GPXPYXAillJ5bIqm7GYr5cvgLX--07baP52jTd72Do5WlDU8IMPXbq3gJHkaNfrQU2kgx8iK5mwFUqWlVNPhg1IhmSeVVNYxx_718vaN6X9Y_tS1X9xzibVvGtfrIvV-KNZbtm9z5k9ZIpz1EmBDp829PFCa2jbRC-jvwFeooEN0KsA7jLp2C8nC6-aASqsZ4BKZyT8kSJLVf-XPj7YXbQHGIoajnhARBMaBOm4sLGBkYu-LVDaM-uVh64Bv9ic9YcwxzBMiP-MFipkIzLtXLTs0K7F2KHzWfqUhRk1qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
خبر خوب برای برنامه‌نویس‌ها و علاقه‌مندان به AI!
مدل‌های قدرتمند GLM 5.3 Flash و DeepSeek V4 Flash الان به‌صورت کاملاً رایگان
🎁
داخل IDE چندعامله‌ی Verdent در دسترس هستن — بدون نیاز به کلید API جداگانه یا اشتراک مدل!
❌
🛠
روش استفاده:
1️⃣
برو به سایت
Verdent.ai
2️⃣
نسخه IDE رو دانلود کن
3️⃣
وارد شو و از GLM 5.3 Flash یا DeepSeek V4 Flash به رایگان استفاده کن
⚠️
نکته مهم:
این دسترسی رایگان دائمی نیست! محدودیت مصرف ۵ ساعته و هفتگی داره پس قبل از شروع یه پروژه‌ی طولانی، حتماً سقف باقی‌مونده رو چک کن
📊
⏳
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7614" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7613">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOK-jnd_CRcPjivvj1_ayp7Db109WP8X77nO2TO8Bik-ODiQ6UpWKUGEuztnvRBPW8tU2wp3qIZgbhK98-4s94bEKLvZig4EIlKu9gNWklio0hiu8ycFepy-un-joQW4EOlT0d2Fj_lVMCvY01B5sw0jpQpnw9adrmAqPK7N5fw6rKZ3MgAsh6eU9Enqk7pTMrT98UR98hKwY28IRe2CxXNQnZzAXYCjSXqPivPs7291KxQQ58cuffoXJcIMMI1P5hY6Yj4Tsktg1QhGFz5dSEEbzlO4nAN8CM_QVB4az3ho4uUdJXV8Aj_YYYOiiVvliQ_aGjm1Xq0JvQiZJvaA1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه
سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت، Prisma، Supabase، و اتوماسیون‌های ClawHub (اسلک، دیسکورد، نوشن)
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7611">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">10000 دلار کریدیت رایگان Fable 5.1
💥
🆓
🔺
Base URL: https://syntro.up.railway.app/v1
🔺
Model ID: claude-fable-5.1
🔺
API Key: sk-pHXhquluKg5xOejYuGxaFkrZbgArNB7kX9HtvekqCwA64pWc
✈️
@ArchiveTell | #API</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7611" target="_blank">📅 14:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7610">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYQDWXqzQUlwxKDsXJQ-0XiI1KmV3SxvBLFn3f3QdmyGehxqXghqf4KduiqqXgl-RHvL6SxD0zWqJHOA49u4kP55iFIqCOe7arz1AYgSAwvyoKv8ZbzAhUfds2urH_1a2B1FMa8b8_bADpLmJFvKYInjT6DPP-DY9SQaYJy1mNQATeICdOUI77odGpPzGONJZ9AY4NFsHq0mEXCS9SzCPUB4vzREhcuBEWFlyMgI4zpuigrkooCZsBh7JNv1JfOUMpCWWgiMVuWVLZdCw6E0pxFL1Rdzo-FzPpNBWsNu-UFsAGsNsxd1AckK4w_Mm0HtI38aHeTzfx93ka38Bzp5Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10000 دلار کریدیت رایگان Fable 5.1
💥
🆓
🔺
Base URL:
https://syntro.up.railway.app/v1
🔺
Model ID:
claude-fable-5.1
🔺
API Key:
sk-pHXhquluKg5xOejYuGxaFkrZbgArNB7kX9HtvekqCwA64pWc
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7609">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">Free Deepseek 2.5 Billion Tokens
🌊
Base URL:
api.pkay.fun/v1
Endpoint:
https://api.pkay.fun/v1/chat/completions
Key: pkay_f38d9bbbfdaea88a190f415eb007ef2ffb74bed33961c366
Model: deepseek-v4-flash
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RawJ1kpxTNiVbM5hkSDQZ1GqwTFP6xhOoqzgEdAD1_1-O0_ki-ygapip7sRZMvILHdG0pv4cm_xwEiNCRB0KEl7WHThKVoZ4MpBO5dAhXEQATCCekqL1Kj3fTjE41d9zmJDbUK3HqhhoX99M-eQy0-SOH-dZeXw80x4uqC0oznlGXYKdCxSoneuINueiwuiDxvLKnIPVY7_bSLQGNDTQMprYWgJWwGnIA202Xm1bAKFTvILwhLK5S5vPT0x_MovNfxhVJFkDHA9i0GaJi-DGq5rUFPD56MzeDlLXO_DmSDg7O2cK19iOuCwNLpyVIkbb-eJY3dxMCWrIdcLNW42niQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل Gemini 3.8 Flash در برخی موارد از Opus 5 پیشی گرفت - با قیمت 0.75 دلار برای هر میلیون توکن
شرکت گوگل، سومین مدل Flash را در عرض شش هفته منتشر کرد. Gemini 3.8 Flash برای برنامه‌نویسی، کار با ابزارها و سیستم‌های عامل مستقل طراحی شده است.
بر اساس تست‌های گوگل، نتایج به این صورت است:
⚡️
Terminal-bench 2.1: 89.4%
در مقابل 89.1% برای Opus 5
⚡️
Finance Agent v2: 61.4%
در مقابل 58.6% برای Opus 5 و 53.8% برای GPT‑5.6 Sol
⚡️
HLE-Verified: 54.9%
در مقابل 54.4% برای Opus 5
⚡️
پردازش ویدیوهای طولانی: 87.8%
در مقابل 75.4% برای Opus 5
اما این مدل در همه زمینه‌ها از مدل‌های پیشرو پیشی نگرفته است:
⚡️
DeepSWE v1.1: 71%
در مقابل 74% برای Opus 5
⚡️
Terminal-bench 4.0: 19.1%
در مقابل 51.8%
⚡️
OSWorld 2.0: 59%
در مقابل 75.4%
به عبارت دیگر، این مدل "جایگزین Opus" نیست، بلکه یک مدل سریع و ارزان است که در برخی وظایف به مدل‌های پیشرو نزدیک شده است، اما در کارهای پیچیده و تست‌های جامع سیستم عامل، عملکرد ضعیف‌تری دارد.
قیمت این مدل تا پایان سال 2026 ثابت باقی می‌ماند: 0.75 دلار برای هر میلیون توکن ورودی و 3.75 دلار برای هر میلیون توکن خروجی. پس از آن، قیمت دو برابر خواهد شد.
همزمان، گوگل مدل Gemini 3.8 Flash Cyber را برای جستجو و رفع آسیب‌پذیری‌ها معرفی کرد. این مدل در CWE-Bench امتیاز 47.2% را کسب کرد، در حالی که مدل پیشرو امتیاز 47.8% را کسب کرده است. دسترسی عمومی به این مدل وجود ندارد: نسخه Cyber فقط به متخصصان امنیت تأیید شده از طریق برنامه Fairwind ارائه می‌شود.
در حال حاضر، این نتایج توسط خود گوگل ارائه شده است. هنوز هیچ تست مستقل از این مدل جدید انجام نشده است.
⚡️
جزئیات بیشتر:
Google
⚡️
بنچمارکش داخل سایت
https://artificialanalysis.ai/models
اومده
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7604">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_QsQupo-1DWnAxdS_46MjWh4ds0QiK9wig5UEXdbB8Wk-4GBIlCd_2MLj_ogGlIyawgvYMp2ov3nfX9VDOqq_NmuN-S0bHyZh93iSO2Bhrqrox0WyYnCY1eUtqvYCL3ej2wqaeD-ZIIls4Kz_NifrD9Z1JELt7rgBJTwnB5DU3Y9PiEQFusdHOizXW8qjOcNEqvUcKN48yaQU-PBMBFWgzhNHRTYR8y-HAw2ss8SFQjr7JhAd2KagReRkdLUYA2j5dA87TqgrAHOfzzlH822ZGErcfD_Z2ma7shyZ1sVH70Tb_CXTl1W_9B99K5A-m5iEA1EklF12G_21b3OKkqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KS53SgxYLGBsnMWWLg_YSL90szDTDKnQ6-Jl6SM7RwJ7-l3qIwBEt0T-eBj0JmQGzpJDA4XOtBL0Lxl6wI7ec-tE69aeG5yxr8EWdb45BrxIa_V6MXnU_09F064CiW-fH-ew0YCWNNwnyN5Z9hPjTS-fn-Hm-Fe5KQMjWlG4dfTXb51BGO6T_fIFrhwJX9Ey_oK2sqtEO8jj4fv3xBD8vHoWHRgThsIMnkGsqeFuH0uwt4IS-DD2M_6wBXPBLDY2IumZnRqJLR-tlJq6xYf9XyTvHMe2-rnoBDkPT0ynfAl6O9-f0rP7VwX5NO72czpqNSqMt3TbTIlCYEKa4rKXSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVqMri2IzkfnHmb3KdnuvAZvVHz1Br5z-zrnX6Rr3MaN0zlJNElVfe41tXzQ28IONAF7lIIdKe9JhwxB4Jvf1ewLVHuZAf_cnQYiZs4fZ3BDjGVZu1YjDgZEAdw0xLuihT5p0Td_erVHFhlGAMIZYpSUZZkfc8Cm_qLooZZgUXPePTgjyZisGbiwbOluB5Z3Icj7rlIsgqLN4htQ17_uEJXqJ3SC3xZfuTsTghraQBL9e5_uXm2qbC-t34_nu_QjjT5BFeZAHGhhCnI-BvG8nBIqI0n7bYOljYAh9iphA5C3ZThX5eqsrV772a4GwTJsZooJsFWZKF2-WV1OACBS3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ریپوی ArasClient پابلیک شد!
بالاخره سورس کامل کلاینت روی گیت‌هاب عمومی شد
✅
🔗
گیت‌هاب:
github.com/ArasTey/ArasClient
📥
دانلود مستقیم:
github.com/ArasTey/ArasClient/releases
فایل arm64-v8a برای اکثر گوشی‌ها
✅
فایل universal برای بقیه دستگاه‌ها
⭐️
اگه خوشتون اومد یه Star یادتون نره — برای ادامه مسیر خیلی انگیزه میده
❤️
━━━━━━━━━━━━━━━
چرا ArasClient؟
چون کار چند تا اپ رو یکجا می‌کنه:
⚡️
اسمارت کانکت
یه دکمه: همه سرورها همزمان پینگ می‌گیرن و سریع‌ترین وصل می‌شه
🔃
سورت سراسری
بعد از هر تست، سریع‌ترین کانفیگ از هر سابی بالای لیست قرار می‌گیره
🔓
فرمت اختصاصی .arasc
ک
انفیگ‌هات رو تو یه فایل رمزنگاری‌شده امن ذخیره و به اشتراک بذار
حالت Protected: طرف فقط می‌تونه وصل شه و پینگ بگیره — نه آدرس، نه URI، نه اشتراک‌گذاری مجدد
📊
اطلاعات ساب
حجم مصرفی، حجم کل و زمان باقی‌مونده ساب مستقیم از لینک ساب خونده می‌شه و بالای کانفیگ‌ها نمایش داده می‌شه
📣
اعلانات ساب
پیام‌های سازنده ساب خودکار نمایش داده می‌شه
🏳️
پرچم کشور
کنار هر کانفیگ پرچم کشور سرورش (از روی IP واقعی سرور تشخیص داده می‌شه)
📊
آمار اتصال
تایم اتصال، آپلود و دانلود لحظه‌ای + آمار کلی در تنظیمات
🛡️
همه پروتکل‌ها
VLESS • VMess • Trojan • Shadowsocks • Hysteria2 • WireGuard و…
💎
پر-اپ پروکسی، روتینگ کامل، بکاپ و رستور، تم روشن و تاریک
━━━━━━━━━━━━━━━
🔒
ویژگی‌ای که هیچ کلاینتی نداره:
کانفیگ‌هات رو با پسورد به دوستات بده — اونا فقط می‌تونن وصل شن و پینگ بگیرن. نه می‌تونن آدرس سرور رو ببینن، نه کپی کنن، نه برای کسی بفرستن. مخصوص فروشنده‌ها و ادمین‌ها
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eb0nOGuEuVfXNj0WXn4Wkz0eOA4YsypqFRXBycUDlqOeX28gu8B83m7p7jriennpu37Tb-E9k3gTA0qrRUaFCIxrk9Nq8o9pW5sgjVx7LnMargeGcOv2-F4RgnLDNYiYfDwPl-cLFhepy9YpN0slzhFG849T_qZhtdvauE2vNvbi7yq2YeGHtQPOIi50jFNLmx4WLw8vF8ZQjQzUMNBoY9t52CEUCHGqeBadW2e-v-MOY9dzngqTAvQeWiYXBTiBASAkSkRITsL3OxvoGbKLf_1xiOVa3b_VCIkiQZMA0lHYKJLcM-yh08ePc9bS8M1nQf7lVRcYPc7p_K_V6Qb48Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧑‍🎓
✨
OpenMAIC — کلاس درس تعاملی با هوش مصنوعی
هوش مصنوعی داره تبدیل به یه دانشگاه آنلاین کامل میشه!
OpenMAIC
یه پلتفرم متن‌باز برای ساخت دوره‌های آموزشی تعاملیه — شبیه NotebookLM، ولی با کلاس درس مجازی واقعی
📚
📤
چیکار کن؟
یه موضوع، فایل PDF، اسلاید، صوت یا ویدیو آپلود کن، سیستم خودکار می‌سازه:
✍️
ساختار منطقی دوره + اسلایدهای آماده
🔤
آزمون، تمرین و سیستم تصحیح خودکار
🔬
شبیه‌سازی، مینی‌گیم و مدل‌های سه‌بعدی
👨‍🏫
معلم‌ها و همکلاسی‌های هوش مصنوعی برای بحث گروهی
🎙
سخنرانی صداگذاری‌شده + تخته‌ی هوشمند با نمودار تعاملی
📦
خروجی:
فایل
.pptx
یا
.html
قابل ویرایش
🔌
سازگار با:
ChatGPT، Claude، Gemini، DeepSeek و مدل‌های محلی (لوکال) هم پشتیبانی میشه
⭐️
۲۰.۷ هزار ستاره روی گیت‌هاب
— پروژه‌ی فعال و پرطرفدار
🔗
لینک سایت
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thB_8jaDQQOzJD7P0ljWJrK8tQPPDEUqyZL-QsuITqzIn4enRilSvrVl9QD3mENHfgb8YgTAhG5fDc0z-J5D8vjQyI8o4jKUBp2ZVnvIdqeNHQjr3wJTnxl8zjJJxBBc2t3n7tHTtfYrVBS4nsDAQ8PQ2A97d10HVhb969DVuqQsqCdt_c7mhi-qEVA1dKDU9Iivoiq7zvTvyHT7n3BgpgMaBEwkRRzbPxOno50pfbZfcpLQgSe8g8_PRHfKkb06F6UjOSb6y3KTUwkuy88lUuIcPeVLMMKwA7MLhwQO8CQ66FM6tOlNjJ36IzkJB4_5PwYm2MDqB1pVXmD_y0yqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
✨
۵ ویدیوی رایگان روزانه با MiniMax H3 Max — بدون ثبت‌نام!
با این سایت میتونی این مدل ساخت ویدیو رو به صورت رایگان امتحان کنید
🔥
✨
ویژگی های کلیدی :
🔺
روزی ۵ بار تولید ویدیو، کاملاً رایگان
🔺
هر کلیپ ۵ ثانیه، کیفیت 768p
🔺
صدای طبیعی همزمان‌شده
🔺
متن و عکس به ویدیو
🔺
فریم اول و آخر بده، مدل حرکت وسطش رو بسازه
🔺
نسبت تصویر: 16:9 | 9:16 | 1:1 و...
بدون نیاز به اکانت برای ۵ تای رایگان روزانه — با لاگین هم ۵ تای دیگه اضافه می‌گیری (تا ۱۵ ثانیه‌ای)
💡
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNgMTGTY2DRN_xBSY2hTvUCXO8M8ijZEjer39qAflWS6SWHn6z5eyyZF8YPmNJWHdpVEjjhj7v1XpC643jg7d08vwGpkGHU2ttsu87pMiPnOFFIRq1LR5Sc_EaH4z6WOIja15JmPd2Sc41OFpEbEhpCERQZNz3bh9yo_42xNNKxS3z-KBXDLQfodZPKgJ57peXIqtjNu4Z2nEsTO1JJKLES0vRJ9OetrR3f2AxwzF3eGrUyF1zmyLdF2qa7TbKW3WvZJiKMjucTkNtNteXjHBErvk2YQpy5ZIGL3QM8H3leViA3NpW0FVyjEngK2cU9TYJlAs5kqE76Sf_2MNIzndg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔧
✨
دانلود کامل گفتگوهای Claude با یک کلیک!
معرفی
Discussion Downloader
— یک اکستنشن ساده و سبک برای Chrome که گفتگوهاتو با
claude.ai
به فرمت
Markdown
ذخیره می‌کنه
📝
📥
چیکار می‌کنه؟
کل گفتگو رو استخراج می‌کنه — همراه با:
👤
مشخص بودن نویسنده هر پیام
🖥
بلوک‌های کد سالم و دست‌نخورده
✍️
لیست‌ها و جدول‌ها با فرمت درست
🏷
هدر YAML با متادیتا (عنوان، لینک، مدل، تاریخ)
⚙️
چطور کار می‌کنه؟
برخلاف روش‌های معمولی، داده‌ها رو مستقیم از API داخلی
claude.ai
می‌گیره، نه از روی صفحه! چون توی گفتگوهای طولانی پیام‌های قدیمی از DOM حذف میشن و روش‌های عادی نتیجه‌ی ناقص میدن
🎯
🔒
حریم خصوصی در اولویت:
✅
فقط دسترسی
activeTab
و
scripting
✅
بدون آنالیتیکس، بدون تله‌متری
✅
هیچ داده‌ای از مرورگرت خارج نمیشه
✅
رایگان و اوپن سورس
⚠️
محدودیت‌ها:
🔺
فقط شاخه‌ی فعال گفتگو صادر میشه
🔺
آرتیفکت‌ها و بخش thinking صادر نمیشن
🔺
رابط کاربری فقط روسیه
🔺
نصب دستی (unpacked) — توی Chrome Web Store نیست
🔗
لینک مخزن در گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBd76JEna5rsanErqUqi15ZfhO1OgIcUGDIkUHqX80HFj91LjpcUrctG_pTxOo3Y7jX0MCQlpPvubAWsD5zDT2FhB_AFKewjgCSfEhxbmo1NyiVyzaNMSht0DOIcTKT_p9cFYFCcZUBVupkXB-w6Lh3QXpsuX43GOCjvO-hSxJF6hGamyV6PxT-q5DljpTAHAt50sVpShiilhoQ31Z6qOqRHxTZsr7MVUQoXZPAtK7WjmRqucooeVnu85vbzn5jxfkPS9BVwgqMH5sy8GSmgkEs91SeHypbid2eT84-i-nMx0fMqP-xlXDJiFWg-7PpONsC-d-AfhvtjuL20Jh-7bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦆
✨
حریم خصوصیتو با هوش مصنوعی معامله نکن!
با
Duck.ai
بدون ثبت‌نام، بدون اکانت، بدون هیچ دردسری به قدرتمندترین ابزارهای هوش مصنوعی دسترسی داری
💥
🆓
💬
چت و وب‌سرچ با GPT 5.6 Luna
🎨
ساخت عکس با GPT Image 2
🔊
ویس چت با هوش مصنوعی
سؤال بپرس، جستجو کن، تحقیق کن، عکس بساز —  همه‌چیز رایگان و خصوصی، بدون اینکه ردی از هویتت جایی بمونه
🥸
🔒
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uo6NsQCu9pOvajTy_m5bxhJPF_0iD0OqfgoxWVzk_IBmP8uXeuAn33nWC2NAeQ_wBhIR8-iJyPFZTOvn8c1Mc8YfOTCLzscKcXUkW7EjKN7WzZX-HKwivqMdG--zslZ_rF8m4T7aE5tkybnb7CSjsWs-iDZ9T0du_m5sFKCRW4oWQSwX_4DC1nn2QRPkx8JfznoGQsydNNnam0byEVVA83TRwVP_H7nbwaZ1DiUS6FNLYa9OGhw-xtkUcbMPWg4sDYr07edtLaO48Kw4jteT6qusFoHdOUfQ5CTrHC0SsgrQpH5bK_WEyiOwu6BRM5YCtXYZHEzj-dJ7iEa5K4xPnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Hy4 Preview: رقیب جدید GLM-5.3 و Kimi K3
شرکت تنسنت، مدل جدیدی از خانواده Hy را منتشر کرده است که قبلاً با نام Hunyuan شناخته می‌شد. این بار، برخلاف روال قبلی، مدل به صورت عمومی منتشر شده است، وزن‌های آن در دسترس قرار گرفته و به سرویس‌های محبوب اضافه شده است.
اطلاعات کلیدی:
🟢
770 میلیارد پارامتر، با 49 میلیارد پارامتر فعال به صورت همزمان
🟢
ظرفیت پردازش متن: 1 میلیون توکن
🟢
حداکثر طول پاسخ: 64 هزار توکن
تمرکز اصلی این مدل بر روی وظایف پیچیده و طولانی است: کار با کدهای بزرگ، تحلیل چندین سند، نمونه‌سازی بازی‌ها و تحقیقات علمی و غیره.
در یک آزمایش کور، شرکت تنسنت 203 وظیفه مهندسی را به 163 متخصص ارائه داد. نتایج به این صورت بود:
1. Hy4 Preview – 2.99 ( از 4 )
2. Kimi K3 – 2.94
3. GLM-5.3 – 2.92
این مدل در تست‌های منتشر شده نشان می‌دهد یکی از قوی‌ترین مدل‌های متن‌باز موجود است.
نکته جالب دیگر این است که این مدل به طور جزئی در فرآیند توسعه خود نیز نقش داشته است. این مدل نقاط ضعف در عملکرد خود را شناسایی کرده، پیشنهادهای بهینه‌سازی ارائه داده، آزمایش‌ها را انجام داده و به افزایش 31.8 درصدی سرعت پردازش کمک کرده است.
نحوه تست:
>
WorkBuddy
– به صورت رایگان در دو هفته اول پس از انتشار
>
CodeBuddy
– دوره رایگان دو هفته‌ای، با تمرکز بیشتر بر روی کد
>
OpenCode Go
– مدل به اشتراک اضافه شده است
>
Hugging Face
و
GitHub
– وزن‌های مدل برای اجرای محلی در دسترس هستند
برخی مشکلات شناخته شده وجود دارد: مدل گاهی اوقات بیش از حد طول می‌کشد و نتایج نهایی را دوباره بررسی می‌کند. به همین دلیل، این مدل در حال حاضر یک نسخه آزمایشی است و نه نسخه نهایی Hy4.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Joxda5oc7rxnNdhu-y-p_vmnlY4UJJSTfbPxsqIGNzkmvl4mlj3Yv9aLY_yB81g9wr_nMMddW-A_X3yebYWln-y_aiKalMno6LHzUVpP4rZk614AfK06-gLWpmreLBEmLcWFu8XuXHpm1A5dNHMrzU9LYmwSwiuLmFlliGEzzVYcWOofFxTpgrU5o3V-o0OTF3zB2HrsPua_fpReOXvzgenF_k18uOFiR2d_wCj5mkirjXMCZuAwxFeFfLvZv9Rgr1ABIN9--LRvx19ZRiYW_vjJDn7fLdr9EICEB92eJX-l-tRRX6SlgqCGzdEjGGxzJ7pFDINqIfRGf18IXkKVvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تبدیل PDFهای قطور فارسی به متن تمیز برای هوش مصنوعی!
نرم‌افزار ویندوزی و رایگان
PDF2MD Studio
. با این ابزار، PDFهای ۱۰۰۰ صفحه‌ای رو به متن استاندارد مارک‌داون تبدیل کنید.
فقط در ۳ قدم ساده:
1️⃣
تبدیل هوشمند:
PDF رو بکشید تو برنامه تا به عکس‌های سبک و باکیفیت تبدیل بشه.
2️⃣
استخراج متن:
عکس‌ها رو تو Google Drive آپلود و با Google Docs باز کنید (بهترین OCR رایگان فارسی).
3️⃣
تمیزکاری نهایی:
متن خامِ گوگل رو دوباره بندازید تو برنامه. نرم‌افزار تمام خطوط و نیم‌فاصله‌ها رو مرتب می‌کنه و یک فایل فوق‌العاده تمیز میده!
حالا این متن رو بدید به AI تا براتون خلاصه کنه یا تست امتحانی بسازه!
😍
🤔
پردازش امن روی سیستم شما
🤔
بدون نیاز به اشتراک پولی
🤔
اصلاح خودکار باگ‌های تایپوگرافی
دانلود رایگان از گیت‌هاب
(ستاره
⭐️
یادتون نره):
🔗
دانلود نرم‌افزار PDF2MD Studio
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCTyNp7Kr3_MgGZaEk3llmo2TTMPzuNkremayf4pSnOJda47T75yUesodGMVZX6bujyTXLBI-VV_htcPR-7-rc3m9rXADloPgsrfWTeOEqEyNPLeeXfIHUsvIpafEgEIkuzQOCseenlY4m_-iMstM_Z2EnBcnNgSQ7OpISp1yfZOtkykdkOLeSSN30wCMx8suJfOE1ysN-fXiYladkwmbPbR4GCQIUauBP3VBYPf9ELhdtB_BheCJPIdbdejVJz3RyGHXjbqysHE9GN0WKnkm3EN__QmJLbFCaL6prGDbrk1GON8PHZV6U4bClhSlimGmyZ9a7RslaXCv8puAVGIRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100
د
لار برای دسترسی به API بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدمت یکساله )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
25 دلار
و شخص دریافت کننده
100
دلار
دریافت می‌کند!
همچنین 20 دلار پاداش روزانه
🎉
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkZpswKs5YyUlJxnaiPPa5g_f_vni10WlGB1TpHNgTW4PVgJWPcEESSaBP8QmrBR385FUJY3HroFNeSlcnnju6DObUVlgY6rRQmvAj7PZHXS8kOUD6Tj2jiM17X4hL3P47xx4C3bNavAgFGUatQeLioAldwOjmPQI0-NTASm2bfr_j9gLyZddKVf6MEv9M4-3uOFGw25_LWZp3x8u9XLkuYrPfEvMOWkCwLk5gFAuLgEDetHcxSLE8PMJEostxWaXrTJNSkfgWfYo8sJhDUTaz7L3u5d-uA7PmlUEwqe-FWsuAd1ERg0zIiMK2np9Y2zRXV2TNpZXC1aQSY6L_QYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت 10000 کریدیت رایگان سایت Genspark
💥
🆓
با این روش میتونید داخل این سایت برای مدل های زیر و دها مدل قدرتمند دیگر 10K کریدیت ۱ ماهه معادل ۲۵ دلار دریافت کنید
💵
😎
Opus 5 | Fable 5 | GPT 5.6 Sol | GLM 5.3 | Kimi k3 | Grok 4.6 | Deepseek V4 | Nano banana 2 | Seedance 2.5 | GPT image 2 | Gemini 3.1 flash TTS
✅
❗️
نکات مهم :
چت متنی در این سایت نامحدود هست ، محیط وب سایت یک محیط دارای Agent هست ، همچنین می‌توانید از این سایت API بگیرید ، همچنین این سایت یک نسخه cli هم داره
برای دیدن آموزش کلیک کنید
✅
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
