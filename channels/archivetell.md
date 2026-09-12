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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 14:30:57</div>
<hr>

<div class="tg-post" id="msg-7716">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGKsBU7SuQZEBp8ItWRlHQ7IZ_dENAuLEA0lGcBL2Hw7Bqp44MReW9_GgKx-M5xOtTwyOD4NTetW9zUPmVE30kLWkJ1UR5jlb02bBbJIAL0pQIYrhv0RRo67arANK3pihXdZvi1W6jrK6a6PGqDwuC_0T8X_C_ZUw5ImpdnGmTU1Uyl50Rb9TpwNuj-zrR-EYa8UmQIE85fheY41XWyEkeXOot_sDWr6J1bRW2CnLezgqZtvCe0j2NyfQokhV3W03tsMrUZrNZdD2Y58gi2FME2KzuXp3eD0xV4PALZ7b7mYU7rJ2b6ehTj4fn6njlTTkroAYwJfpk5M-BR9oqtBtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥁
کیبورد لپ‌تاپت رو به یه درامز حرفه‌ای تبدیل کن
پروژه خفن KeyBeat یه استودیوی درامز تحت وب هست که بدون نیاز به هیچ نصبی، مرورگرت رو به یه ساز واقعی تبدیل می‌کنه
🔥
یه پروژه اوپن‌سورس عالی برای برنامه‌نویس‌ها، آهنگسازها و عشقِ موزیکا
🔗
لینک سورس کد و اجرای مستقیم:
https://github.com/faithsaly5-stack/Keybeat
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 643 · <a href="https://t.me/ArchiveTell/7716" target="_blank">📅 12:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7715">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLdNBzZhziyrT7wwbkqfJbLONxHba86hPCOBgkh7bd5WvyYuRphl6KAY5jFBJcuRE8c138oRUcCy_z8ebAjwcog0aVW21ImDHXOT2nh_HLULHdDfCBPYk3lIQZhnhX094kN-7LVjR8yBEqxcQtAQefvvzinTBri00j8S-YTNqwnuNZoMcXO8VANj--9pSPL3fx2i-jb5EE-Z8mKqWGOUE37klfA2sSl3PAnBp0VKZdcAOiVn53klrg1oqIMioQYqrHnoQ_O2YrrWof6sFy6wHwozEVPlEThy59ym4svCiQte0olT8dDhEhaalspBvgb--tQfti0qYPER4FJXLeF0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
دریافت آیپی رزیندنتال رایگان
💎
با گوگلتون سایت زیر بشید و روی claim offer کلیک کنید.
بعدش برید بخش proxy generator و پرش کنید و بزنین براتون 300 مگ آیپی رزیدنتال میده
🆓
http://rainproxy.io
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/ArchiveTell/7715" target="_blank">📅 10:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7714">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7714" target="_blank">📅 22:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7713">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7713" target="_blank">📅 22:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7712">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7712" target="_blank">📅 21:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7711">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7711" target="_blank">📅 20:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7710">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است.…</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7710" target="_blank">📅 19:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7708">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل: ① به https://arena.ai/ مراجعه کنید. ② حالت Direct Mode را انتخاب کنید. ③ در لیست مدل‌ها، GPT-Image-2.5 Sunburst را پیدا کنید. ④ به مدت 72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود.
✈️
…</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7708" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7707">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت گیت‌هاب قدیمی داشته باشید و از طریق این لینک وارد شید
✅
🎁
با هر رفرال شما 100 دلار و شخص دریافت کننده…</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7707" target="_blank">📅 12:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7706">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7706" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7705">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7705" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7704">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-2V8yTwxwCwHU76C5ss0EK0D48txwiZ08DZj9jbmv3ChzudwPMZKFXWP7sacgiR_MArtx7Qh5pSJrSW3vEX487CQF4f1qIxBpgGzjB_38ErUaSGfJZwhYWmLWqW7jbIS4R5BmcS4PXsPq9tr1aQ3f4Fljkn4tHwNltIr-Qv9kK5tTTl9gJxfx0rLoRbAhRk1jUFZB78bELHEXUX26PiQKNH7ALhBPMMhXiEKtnxG-Pyb8JM2oYMZabGolRl7NiLrrqfEVnCY_pLvf6WxegQgfBRb_pAX32PQRgqyWwuQqsHVTD8tsvUFs1DR8WBN9Z8QiunYy8HdsHQxOyVQdYEvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7704" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7702">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cw8-Gzl7S4IIwPg77D6brzAQb0feA-kw3aRvCT-VNb2TBkl_-ObMzsiHtcqg1v1mPVU33cwNmfqKSnDCk_bHfEDZNzIF5f_w4eDR1P7DPz4ymWuXVtXdu8S7axi5SUgsNMKEwdGucP6BAabCsb7mQo2p1sR8vyieFHCFdCW6dzNLdfr_4HdfPMdl8sh1n7g7uZoPgbwB9BXxOKCt2kdg3u_Vc96C8QjGpTuci0GSHgqTaFM1KqxMvztPSsfiW0dUuvrQL4LLmok_OZ9i4-OhkCj5t5b2bG7Xpvj7675V1XKyXXxmtIQx7R-VSfJL45WmVOxkHKATk1yxhT5Za0dobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GPT-6 Astra
1 Day Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=gpt-6-astra-medium
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7700">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FltTDLmFavCU4dVsdkafl3rLrG3i_dqJsND2DCXKwS6zsBRxo38Fxg5HXrV_yrNjd9y50B1NAI2Mo4H4PUSclyRQRTTa57mmng5KKemYguTl4OdO1cqwYrrdWZ_v5foJj74dErYeau-K17mXB2N82sFagw56m6sNmIKjNJHhICilWEIv__WFGgcLo_r7h17KYTqIeG4xyYNcQbA9YkVwY6tOjY2yJ4lN2sGshMkcIftNDNcy6MphHqsNoEwjTiW0oUv2LKoylso2SqbNCVBdr5PW8y7vaDHl7Gnp2OmC99NLHAWdgwjnWG5yj97_47lcac39pT1gGdarwqY-2I17lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aj2ZfaTzF9wpm3q8J6yiC1R4fG0RYQwdGeis54yzeGpgjbhVQ8PpYO-r81LlVJDuHvo-3KLdP2X8pvS0iaUc9QcNBD-Z88dGCXaQIZBxtjSR06S348mpRgtOiMWrSkJHI1Q9A-nTWNnXEZ9p4rLbe70trG_0qPBYbf457y-23sVWxQfjVidsUzWN8zLTrbFCnoxbaAj575KYwmxLQINFpb1zQ52UIn0XxHfxJUBQ5fK-xR92CKQER20NV6kmkwUMcvnHHlh62523JlsC1WpoI7M9rX2hD27M1ilHTX88kAe4VKwVovKMIrQzRXGjDuz4iA1oE6OSP3A7fytpHQtLrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRlIXiHv_8RtMbyK-xzN6DmfQ6MVWiTkFD85j8obCpJ_uWQ68LSoxPriGDE3e7Ie2Rpgb1x86YVCEYxI9B0adNgC1A_5Swrft5HI9gX5LnZpd5HrIrciBNHg1nqjc7J-JlxU9Ti_3vghdwppejp-ipTvtmqgtK-Es5xrmWuoVZHyuVpXenX3MuJAA4DU_FHO53Yz9QV_PQ521pKJzQzgIE58US0WHmhA4hyd2c86DT1YcOCosbb3tJOYybvuh3w6KFSWovk2D5DCUy5qnLQsZZc0xZAUypOF5G5LFU8ixgPh6rBEfRUG69Gbyd2n8zUP5bf3ezusGrh9G2G4zi2E7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=lklY83_IcgvSAgpTRuB6JvUO5Lo3G4pM5omZAEXYHizT0tui25s0fVrP001C4THYHRONvK5okbdVn4oAPk2KqWT_6GWoBXeMqqG0W9jQHTRGNWGR6Jr2MxS5DSJcffdlzUpAsX2lbo8JnUumcktNMafe484CbYXqiRREn5T_g-WgWvDvK7YD2hrkVAWVJDqExZ3EjwDWcjy2A-c6nY8vlf8Z2LChcFdHZg_ikSnGanKamloqYbpfPw4SGF5o8bc9TqqON7kOWdaXK7wd-4ArK74VJOQJUN8WA4nwKW7zNuD5WE3ikKF3XvfLRiL72sFHeG1xh3sGMOeB5tKZYJromUWx--hE_A0DZCp2_gV4PndVfJbWsBjqCRQ7nM1AHonkPsrV5GZiTKIvDgziaeB0Yubh5nTVHQwLxfIEu6YYgG-7Lr3fJbqdSHn0zNP3rqqmv0UwOiy0gKxSfJ1WjeAEAs80d5geqsD09rY4X0rqVrqVR6QO3biTJxv2dOlZWq5X9Q7JxNYjW6tJ1M6f6HAxD2_S46XVN-wx0j_59AS46r5yOZr55wO9OzgagQJTEa79GE7YbO0TLnkpqxswdD5W2NKkZT5PERU1RYP6amlBXZjBXCIUa5Q8XtcrOguqFy79aW9ncvGeAHiUTnQFyb5EltohMp-47I2bgQwNxfj7RGY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=lklY83_IcgvSAgpTRuB6JvUO5Lo3G4pM5omZAEXYHizT0tui25s0fVrP001C4THYHRONvK5okbdVn4oAPk2KqWT_6GWoBXeMqqG0W9jQHTRGNWGR6Jr2MxS5DSJcffdlzUpAsX2lbo8JnUumcktNMafe484CbYXqiRREn5T_g-WgWvDvK7YD2hrkVAWVJDqExZ3EjwDWcjy2A-c6nY8vlf8Z2LChcFdHZg_ikSnGanKamloqYbpfPw4SGF5o8bc9TqqON7kOWdaXK7wd-4ArK74VJOQJUN8WA4nwKW7zNuD5WE3ikKF3XvfLRiL72sFHeG1xh3sGMOeB5tKZYJromUWx--hE_A0DZCp2_gV4PndVfJbWsBjqCRQ7nM1AHonkPsrV5GZiTKIvDgziaeB0Yubh5nTVHQwLxfIEu6YYgG-7Lr3fJbqdSHn0zNP3rqqmv0UwOiy0gKxSfJ1WjeAEAs80d5geqsD09rY4X0rqVrqVR6QO3biTJxv2dOlZWq5X9Q7JxNYjW6tJ1M6f6HAxD2_S46XVN-wx0j_59AS46r5yOZr55wO9OzgagQJTEa79GE7YbO0TLnkpqxswdD5W2NKkZT5PERU1RYP6amlBXZjBXCIUa5Q8XtcrOguqFy79aW9ncvGeAHiUTnQFyb5EltohMp-47I2bgQwNxfj7RGY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=RuG4278GkzFp9QGL4URfpzkGZEMd0Mk7dRreXKR92vB0K_E2yaaQJhFppYCFN-jfXibaDsWPErwkZw-qA6coZxOXUcG4ppJaGv9EiJN2sVj6BtsSOQ2kkuJIN5b8SccI9lSFsoDhSHm6heYnY0ujJ0nGkF4tgeJNfLIMrJMekLy2uMBm4xNjjrzFB4uTLSEswu_EWsrAlWud4E6H5FjvSH_coH3_M2vvWpFhUMCc9Dq26sIFr2Dt-2iT4RYcK8rmwUu1LqLRZb9pGLwe_LekZXK13aurRuTtvX2Bpmm7C9LYm7V1vWgasz1aJqL4c6SmURA7Plp82fiX013vKVo-SSKGW93Hb8pr1WMzCOYqj1u7ty3LQw0b0cl07xt40hcIP8siyMHPJ95xHmEszByO0HN8zeAGJs6cKhapM5sLVJ_GCo4f9cH_SzVvXhzMVbkY5qNDuTFRcTxz946iFa2fymcgIKCYM3JkGp17Q3rmnd2kkLLJ0lB9FQvWt_DXTpcBQv2UovCos_d_yWKafgbT7z4DoMZjL-kU9wiUMvgxGLd6qgythjXDMzbusEXU70uyKSSG3CY568UIvpiXM-a1OploqNCTGOUC2YnKCD041EaBU29GYYuxEQJfWyTkJ-ZrLcrjmJIwbwGkQnbh8VVccPfwqNuPl58doWY54MvpchI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=RuG4278GkzFp9QGL4URfpzkGZEMd0Mk7dRreXKR92vB0K_E2yaaQJhFppYCFN-jfXibaDsWPErwkZw-qA6coZxOXUcG4ppJaGv9EiJN2sVj6BtsSOQ2kkuJIN5b8SccI9lSFsoDhSHm6heYnY0ujJ0nGkF4tgeJNfLIMrJMekLy2uMBm4xNjjrzFB4uTLSEswu_EWsrAlWud4E6H5FjvSH_coH3_M2vvWpFhUMCc9Dq26sIFr2Dt-2iT4RYcK8rmwUu1LqLRZb9pGLwe_LekZXK13aurRuTtvX2Bpmm7C9LYm7V1vWgasz1aJqL4c6SmURA7Plp82fiX013vKVo-SSKGW93Hb8pr1WMzCOYqj1u7ty3LQw0b0cl07xt40hcIP8siyMHPJ95xHmEszByO0HN8zeAGJs6cKhapM5sLVJ_GCo4f9cH_SzVvXhzMVbkY5qNDuTFRcTxz946iFa2fymcgIKCYM3JkGp17Q3rmnd2kkLLJ0lB9FQvWt_DXTpcBQv2UovCos_d_yWKafgbT7z4DoMZjL-kU9wiUMvgxGLd6qgythjXDMzbusEXU70uyKSSG3CY568UIvpiXM-a1OploqNCTGOUC2YnKCD041EaBU29GYYuxEQJfWyTkJ-ZrLcrjmJIwbwGkQnbh8VVccPfwqNuPl58doWY54MvpchI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfeVF4R8KeA9rV2Zn9YDnf-KrcwNqhibXvIsMl3J9nTCCEHNzd9UGlafNL05OGQlWzDOFJJTy49tCWv6ETUczyBZ-zRuJzAy2csdCMI92xZ4MTSGssAr9-GAyCdupRWW8pP4Uvqhm8X_k7dZw5_fVSiSPq6NJ1ft_1IdgZotbLgaUvNkt6k4cTBapnqZNLQqxSs22smGk23a5s0jZE4Yg88ZqmBDUVIKkiKZgbkejlizi6_QgBdnaUhAjtZDlYCb3ErSQ96yU34ygO3wKwW-PX1xFHk250BgdFLyB_Arxwz0Ik9tAn3LpIafsVHJnXd41pl9E8SrJpMi234YenzZAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=R6YuKO2qnYTj45GJtMnUY-lD4XbD1I4G4Tvh-Bzhr0RPcbcNtL5zjOUgf00EIUp-cPpIbY98SMrSNCgbfacofBoE9Q1oYmdF19JsrK4abZmGZ-vlWNwanMZ9T-RN5PaxDeBuN_jl57DrYjSpbbNp1QGda6VSE1g2fkhq_80ReAIX6ciQe7oWIibQtzBbUQvsvBMGedrTTTzMuHr9UsNuNwGVqrBFsqBjV1FCWwiFKzGIeIDi0JlcEdzxFUdnRkgEquw19oLqeS8BBf856K0DU3rlA60nWE49tAj7WHNc2wrm-xIuh6A-0ODZoWW3zY19kMxdAgnuQqoafEZFsmmVrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=R6YuKO2qnYTj45GJtMnUY-lD4XbD1I4G4Tvh-Bzhr0RPcbcNtL5zjOUgf00EIUp-cPpIbY98SMrSNCgbfacofBoE9Q1oYmdF19JsrK4abZmGZ-vlWNwanMZ9T-RN5PaxDeBuN_jl57DrYjSpbbNp1QGda6VSE1g2fkhq_80ReAIX6ciQe7oWIibQtzBbUQvsvBMGedrTTTzMuHr9UsNuNwGVqrBFsqBjV1FCWwiFKzGIeIDi0JlcEdzxFUdnRkgEquw19oLqeS8BBf856K0DU3rlA60nWE49tAj7WHNc2wrm-xIuh6A-0ODZoWW3zY19kMxdAgnuQqoafEZFsmmVrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7681" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7680">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=sdxw-eV4xfe1JwBc5CIWGTOA2atr_qlMNva-74I_63ES3Wv34jx0nROYjGoF0WUoLHgKE0CjdP1EGfW26vGQL2SzLG16KHsr3qasKDKnWBpJsTBKIb8HB6GIafxwWya_FqQll-D1u_cb2OtyRvq-JCRPYEmgHTMZJltDWRoIVGKmMqJJFfQARwOGUTUWf5saYNo1F-2zgzfBNCEc9PAsufeE2AsCWKdx_JP2KLTYpSZF74mtvFW7uf_yrrLvSPAqJhWqsfFpOdfejXFJMAJwVE2yft5Ck4pou_Y0r6SfjDwrJZtlT2WgpPcZwK3al0_7CpiDMZx7fL5kHfowORpjjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=sdxw-eV4xfe1JwBc5CIWGTOA2atr_qlMNva-74I_63ES3Wv34jx0nROYjGoF0WUoLHgKE0CjdP1EGfW26vGQL2SzLG16KHsr3qasKDKnWBpJsTBKIb8HB6GIafxwWya_FqQll-D1u_cb2OtyRvq-JCRPYEmgHTMZJltDWRoIVGKmMqJJFfQARwOGUTUWf5saYNo1F-2zgzfBNCEc9PAsufeE2AsCWKdx_JP2KLTYpSZF74mtvFW7uf_yrrLvSPAqJhWqsfFpOdfejXFJMAJwVE2yft5Ck4pou_Y0r6SfjDwrJZtlT2WgpPcZwK3al0_7CpiDMZx7fL5kHfowORpjjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKav_5wrmA40PROvSf2lrORwqGCqzShAaNrjUE9oNNqUfllbUnmS2h1rbKF8AJjJcHaHZ3H4TRBgHoYbExh4xrxUhbERYCwAtJBV-9ubgU_HswYfHhrEE4FaP8FIryAijS0Y7HedMtpEgjYxnvgGZXN6KwG_yqMaNFRZm8HVLtcpXjhODAYomo8Ge1bCgfd17ssz8CGPZzCNXaueaSKUEB8wkhK9LgKK1DPmDDjlgSN-zBY-_8MKJP6QiCXnDdnjQO_NIgsaSluV66SolGIAqG1vLXF-n_zWax1PdK_W6-rtNIwlfOeLoQ9Fvi43-urGotpgRHTG17fC0Z-R2Oewww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVWOeLvgvR0jCMicgoc2a1-xTijZF0W6LELe6aUeZIE2HouqY-tN7sVZJBp5WwgWVmeRYhlqfp4k3Mz8PJJAM2eT8wYdTiTcY4072t9KDkF99hwqhHpLBVqqiGJm2pyIhZGSPTpIKsayVs4HecUIpgWwWwm6swTRy_lyhuh2Hn94_aK6Sscsnb8LqIwPVBCcLWOReVapKfxiquo2S364JsEyi4Acfhy7WjMBvdZNgIKPxrXXa7FK2ET-RBSIty-r7AXKZfKOXlAkDWRy4ZCUi_wHRMJFa9unApuifcrv8506HhTbO87uS4o0cvkg0ZOqoH7qAnO7pL8lL57Jafk6IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/swiBe5WEOvlg5ysIS6hsQLDKZjPRMxFEm90L5YLuxUziT1kt5UZipaNNru4gxMJ6GMq1WROr71x4-mFmw9j53vmO0FdlXDj7nrwvTx4E0UG3PNI-hpsMcN_1Q7Rkp_RDNb4n5Pzvi8Yda5LZQJ68RPcSfgrVSvAMUTMoODiqyag5JviPtlGkQ91bogF0Pa3DVONXbkRJiMLiV9n0ebYperyQoeMqwZxLQvV1hBm7NhcKsKgyoMLzRpG5qq8kEIYo7GZ2Vj78fjV6Nugfm0OgDpld7ZGcDY5LbILYF5Hj2-nBuN4dHttND5udq8AiKxDhcR3d9-9nUm7ZH8mbMTykPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=r_Lxgpbuiv6qCNE4OjcZ-4MD4240vI9iXZaIxEpb7RNpyI21T66IDfq67P4wJfBVoA_2w3m9bs6_BSWbHXN9PRldZVfYt38tsfDOPQH-ATfGCECKliKweIYfejg0NHo1luRoCusSkyt7i84Eu_gOu0k4JVcL8ak2ATvcH6SAtVI3IP8pWrowcWMFle76sCMxRWv0ZqLPcFRtZS1zbwzulBkV7IqiANIkc1sejesbg6ZrGfsRebuzYCWvI5qcpdi-eyZ7Ar0QLykfxOM-t0gdi-Iyudm5T02hpcs6sOEpBvJRPBJkKSYeagZF4891HbVqyH5SlEluijdi4MmH4IvCmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=r_Lxgpbuiv6qCNE4OjcZ-4MD4240vI9iXZaIxEpb7RNpyI21T66IDfq67P4wJfBVoA_2w3m9bs6_BSWbHXN9PRldZVfYt38tsfDOPQH-ATfGCECKliKweIYfejg0NHo1luRoCusSkyt7i84Eu_gOu0k4JVcL8ak2ATvcH6SAtVI3IP8pWrowcWMFle76sCMxRWv0ZqLPcFRtZS1zbwzulBkV7IqiANIkc1sejesbg6ZrGfsRebuzYCWvI5qcpdi-eyZ7Ar0QLykfxOM-t0gdi-Iyudm5T02hpcs6sOEpBvJRPBJkKSYeagZF4891HbVqyH5SlEluijdi4MmH4IvCmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7670" target="_blank">📅 20:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7669">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7669" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7668">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7668" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7667">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DyvKLe0KiyDUQ09l35kOi3Uy7waWX4QXoROt0CDDqMQGiHqAdZknE4fB0JLyXXbG-D3tSgPpJdWdfAw3gZfzknBsSQPpvrCcqPhE-k76WIA62vKQ-Y7TBa7THtQNcOVxMq7cHUsUbbUR7fxZTGzVoW2aHxrJvoPzIG1sQFZsjcrrIfkN-_7bBQZOXbmgGeYic6llAEgUTsXuWZw9kKcEjEqheN2WmdqnIxsbayzCiKcS7PBLJuIFY76ZWMNk_-5arW5AVSAi0YT8b1uWH2Je0k_y43Dj6XLpokHD485jnovyZuuhBMAkmeRtcx5OrdcF7cE42nvFdFmWdzfaECcoVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7667" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7666">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzVtVoKcdCwn_-19hO8wrzulG0tJkue-S31x8WJqnTtq3Lj1YnbufqYuPPgIV_gyap1mxOsVzjLhM7dkEglHCwdZLq4RN76rEoXvSArHwe8ZTPCJAQcoXhKMWgCPGubwDI3oZoGR-wwf8Z9qoFUcWadc6yPUs8SC3U4SB6LDyXhKb-e9inay3VZhAIhv7hORnW1uZsvIn3FwiqwMEmvhRdv_5xDRKijvCQvdou1vCKjA1Rinb9OJn4QyCCD9OJFhQE79ERQnGcujfMMmjwr7rfBfLeFa_L1sr_1hMIBMrzNG5av9AcPAAzc2whwJOGQa3F9999gTLxNxE5JHEN-SRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7666" target="_blank">📅 14:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7665">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnVM7ZmFVeqn-8CjLL24x5BKt5HMVGpk3_Wf-l8jLXhigmNzunq_yApeolJEsHPCgnROlCBCtAisDuKSXpz14gGd1vCOvf7oiDYBjSNPP8h-M2MC8xBri24NBBDis3H5LLJX77UQFMdfmtZKs4ded_Y_d6rGcPxNR2DSe26rZWHP0RiSA4wjpu7cmVTpRLXNMPqTlbxe0e5v4zVy0WX3xZ0bi9HiZg97YVE9iu-tESaShbUdtBdA4sfsUmT5RjCaw1QzBRSSmMJxjWdegQy1dlZU2bq9X_J0BZWZBZLRQlLJhsRu5gtEbAn_ZklZn3_1wpOjw2stimlXLrHJ9d2r-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7665" target="_blank">📅 14:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7664">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIksqolKzu7207ygmgqzbhaYeQydXLyc4jMJVXWRE4wzN8z00YIX88dmSpZpQw080O0rNDL3VTq8XCWwjs7fDHS2_bVJSlTK90YwATTP167k1GC8V63tL8NVK6SIvvdHWT9Ku8gGrGZYEeEQUo_4boIvesSdQW0VVdFoSwrLZA8dY_zb-V_ysFc4bz3EnKRacT7Y99uNdYDzWhIW9X0zwoHvySmd6g-fhcbixFLqcdsaJ4qI3unoW6Q4ZsUsDDdwZvpt9hYFX9hp6DAVw8c8KkDTIhJzKtlm9UyJMc8AGNM8jaCSS-deyBQgENw_UA2xPmllX8o3puApGZNdJSq1GA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7664" target="_blank">📅 14:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7662">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMpGe8SJMOH1JcnKoap4s-j9G_bGVLLMVmUoB235L6ViihJVl40JmgT3z3LOtFuJ_cBscDPywKPh6TKzoORhpgEt4q4okkUB730wmMBjTTWF0BHqfhV3xKHLrVIVmaKzP2zHs3tPYJ7lCb1ceOQfwo57lgULx9amRofX3GtgtSeW5kCH7Hlo3Jvq7Wyklg2jA9JpR2gMdOar1fP-QytgJ6D_hcDVT0NK6D5Z_EKJBtcI1oIgl7r5t287T3GKK-Ts_s3xtbuXv03Se29cYaGykTjc_sxlohbnakMXkMAxvytVP7raawgyAPSuDagv088th8JUBwzxopwy2eBPyTGR3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7659">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZFSG0Ir40MAau1iJidPKqkDxEiwXo1lvoU_Hj_p4Y1pwbWj2R5s86NBj_3rTyWYus9lDM0STnRs0qTPjRg9TpALvxOToRbvG0hm9zjTt1n0R0_N5_AIMHoz3sMeoNKhcscuVCeL9SXm6N3kQrhwZ7a7_xhYeLoSs-yAiWrGKLM-WCNBEv4IGk5lp7bH1DX_DGjhJPxfN9TFwLqdeJ8xZx55JTnLxWpZDW-XC88Bg5iIWejBqkLHP6ltPSXOVDBGjadhxW8GZNkYvtU5f6AcsNME0vE22LtL9lieB8_dE9puqbLfowt9ZJDDoIlT7kmlZ5yDOn6WRRfMgnbgYzh34Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhWktmKy5b3EOsgnw0ZfdPPuxsnWrLYBrfO-N6yLgMzJgfMw07I60aYI4ker4klh9MfZUVxdw39YXbgv9R8a1hFdahyLeZy4jdxMy40AU5_lKMWG8e0weAU41cSrZEn3ispDfz1VyGTkOB0bVODZr-bqGf9hwNXrdiVf61cid4u8wX18NcW8x0-iyJ8iFkDIJ8ByeC39ZGRj1A7dGg8DHGtNACqTH40vp1kQqC4hHPvaojRsa4NmESjr2WHccGzymRxLrECSNVNg2tZsF8Yh-d0DLqTwUkcdqoxHky0P0Q5F7hVR4J5fSOXR8d9626_YQ_Hs_6wRc1Rh6bg_4ACGNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QG_zqRbIcgBfYs1N3YAik4Rn_Usy2_Twwn6dgTJAeAV7l4auyxlV0EHWw4VRYPb_yY6ek2Eg1PxuMV69IQ3CeEfxEqxf3y0KltSkHMizKYtfUqUtRoEZwNAIjlDcHvdXK4gqahDFFxPWh9SSKE8FKYI5HqbzzNQSp_YJENocMomco84jPSRsG9GLA5-fUPt8DOvGohT_b3LI-NWPEQ5ldfBlM7coZcqY1nOIUyhPymNg8jrWy7OrglM9EV4eeeLM_3atMT65epopbjo-ct-vFbJY87tNTIj2hCOJ0ZsMDRVwx_7nh5zQ-gJ5b6fQ4MBXuldO9N-7YjxHA6O5DrOOIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QeX6VCcBtcQTVTnNDKJjM_ncQYfKknBHo8sKzCL893sZMVqttX8qbYxmchsd83RDAvA1yuuyzFKpIIpIA1AVSYfNlnqSU0jvWqKx0x0mdR4B3evIqFbSsmqCslN4fFc1XMaB8j-Z89egUQ4qRG0LBmnbx12sb9zOk5n0gVo_BaU9RIbBs33grr1OqtaNZ70T-BESS-c-garcPht89babIsw1V2CqhO2EM2YyfARxgK-2LN6JIPFPOi1ZXq63DZoj2_mUhbf6yhLDNR3I_Eg_YycJjpucXMZa5X59f9aYZO-x1MtErwexI4F1Cobi4hSQdFkP1ZPT34Mo67XPMiSB_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdd6nwjhRluEEJNUKyUcyFhUI3MNqhPZQ7MPdBVI3PiMh7HoGNwhortQJWo9JjpmQmRgw_eVo0dtBsBhURohG1WhuX6eLBqoJslckY3HD0j9_C4vlycDNbwygGCl-BXXPCMJPGX2SSsApEDP30f-RosApAHUfE_nPKK_mrvjDU1xNkdYSbt4fwzNwFeDfh3do2CLjT5iaToGjZMXv6Fp1FrU44jkrc7VwGCJXD90ccPj0ATy-t_BpwqUE1PJzS_5xihtmnI-xEOXpAcFx6DZl8EO3ryhVH92tU0IwjvjdkEjUgIXNilLuvSlXMf-Nbqf62BfGpq_RjzlMlG8n940Yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUerQ3vBHm2dBC6HbgiezMiN3ubBD6NSaWcNe2jzKosSBylaggEeclv12BDmUwsZxQqkViZs8FPQAWnfXpM9Z6XzwP6FukaiV__yLRdZ0YQ_W7YjAXbwRi3OuV85_xsFXjv-1AMcjExieMOfuxuaxwBiVyuw0Usixr6kz2zTwzuo8nLvnJntb-Ei4WSYOE5oHAv-ElzJEVlJmiaHPgGNBK87EZVjiTVy8B48j-U0WVHbMj8AVDuT0fZMoYgmyhbxe6g9KMXGeGHKnKHSnUsqkqi_QZT0e6F-T3PCG0IuMjU-6e6WfjNzRzynVsMUld58DtJ3YBosX6p-cQxznNlcIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKgZ0gToX1u45NmWrGuPKotl8mazHxakJ8TrWt9Lf-xpABU3R5nEziwx0cE9LwOjQ62pWD0dxhlNqwIm1of1UPLc6SWUlI2q3UqRFBztCXEYjh9wpxVFX-QwwObEhYaRS0WFtMW4dAcnVNupqQmC-oUbIqABHhFNiZwgsGAn-q2Q3VA5YeSlyOyoYWiJgyk4As-H_mu9L_KlL-QiQvzefyyIGAYucav9RahTrr6eIqociRUbsYBOu2OqmMCDtyqzJIvDt_gRA7AtE85kwLA0i41ePxEu-7roz3IwI4JkpMiIBBV8TuTvv48Ro744QDJ0nUM9HdcdClNso1YpPbzgGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHJHhpMecWOU2wJPZSAbQyDEkJA8vI1wNoc8YrMXqslA8hO2eGxOeB5O7QViAlCujQFKb_Nr_HSYDgmnpvCyW0yOpD2_Gt3_38jWa-uYA3DbQdquKzNgiyQrzPWeadfUp4nyXbHf8yx9UsTKYmsAOhOMhYC5DYwpx50InJoaT8Q1boE1GA92TK-8kUZYDygPrDfSvPK51eTNoTvj1GjG7O82kfxxgfBU_p04fO8_3seXjpjCePF9S27SGDZlfaiffxYUD7NewC9PWJOxp5sN_HdfpnQ1isxxpdjhygvD2WeuHqp80N47hp42zepl_yMOM7dW7bZzcKM8nOgVLs4-tQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8mFlIZdg5dLJAAwFIK19JWId90VFascmBTfbgs3mUsHihmtqHeeirusyFex3PmqV7YwDoKWElI0YtPbwMMxzggba6iI7rPHq1ZL5NCkoC-ZEKHGTulynz8UiDx5ryYMZQGJHIes-kHtYxAHCbEsbidqVlmay8fIjhiJRMZa_6B35U3ycwpe6FbSM-vRfEyOwiR3LsZBogD8QnJ75mieTzippqTO-YlZnMh96MF2q-b0oDOL5RhsZzK0D4ZQ-IMC1LSgHohdn9-6mET13fY9Hj-kYPR0LoqC7qAfi9wK9AHjkzf5PYycgpqUJJZkY5VxgAsQ98bo-E3h3xK9WCorXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nk3ajsYSeisOvuVZSvFJF_Czy6ana6g3sCHJ6dYPIsNLEWpSUGHbn5ipsASFuN-wCLSah7AAG6qUZcpj9Uq6yMpDig8ycvygoW7MBODkl8U2Lbf4BWknrYBvG_ydCXzbFtAZGuqW-_E4AigCFcYXHb25qUzk-t5XAFIrjhLdgFDhOLdIyAIhOFRapMrvEAuCj1SGr7VONcuM4rm03pDnjkLKIof0oyGK04fx-q4gV411nVeAtQwNi64ylonOgEE69rMl-7irQr6yIcjME6KATTimMRrBAilZgt0W2yist0SDcBmnAnMWpjn8VDYTccflYfXPfW6GlfCYfWxr5TzFZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7645">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWhVX_wgz__CtraIFl3kJWWr0iihnMhazL7MyINiJCLj92XruYSIsbJ2KMZKJrJpivitlUnUCVgIuLdHWqRolw2DUYg-xPlCHufZO6_fysN3U6UGaCK-Ag9a2LUOBpEPh2nt0UmQN5xZMEYOHwhWU5XEEajGHbG8-Truyk2N4h1kd6VfOfOXZv6wYTikaAm-LgcwF0Y2PCPYXvvaCrV8cJHPGjUvwWdELD_qrIJrL4fDQqsPq4tjqzBLaYlp-mcextO-Td5j97zawA5B84-6f3vsSeTcTIja615ztJqWM5uj4WPLq2mTA6NfNKIIaSQo5CD0xD4Yqq3H_PdpTH-UUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3SaGcZR1epUz1-fJwlnJbEVdr7AMfTgwFd1HTbMUxBJ9KIH4PmTeEAXh6obapbK7QLz6jn7b4C4J_KB55O-szRphT9E1iIAZhJRUVSLDi9eWWBLSNJNO-e_SlJuR6O-OdO_xPW8e7QcX-7mvRuUd1OiKVgBbT_o9bzJ1SBuZHQnhwilLkI8PHj8WenLrMvMceA3mDaatwHM4494ts8wWt-9GKHVc507d3PAuZ-hqNBu56k-m7xdFrf3VUOWLJd_BHPvIUXbdHACaeKEjn_Pz-mY9LC5R9P_EtbExWQWwMzqBTcvhVmHxPc14K0ZfX_ynDCsBnXXq8onGeDz429Onw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U34YvxlqIzN9-d-GjMJc0nqQr1-_owgUuXFkdBXaa7xeqWGFO0h0caj0bPgKyfnNNxAAn6hS9HRAN4Uj7MYgG8_4EDHMa1xmo4PoPBZgk-_UVwApxdzZfdK42LGO5n7aAx--i3yxh4MoJsoMiJ0GPUAI379pG3dP01L6Xi2RTa9gWRG67kkcBnAUsQf2KruGzb_OYB5to6ejoMrGQ0lEGtI410a37xkStCLblkGYZqo_ednlASXp6TfezXwZ1I-Kek-mYFkQHyByfa5HikhYTrBgBffCVIjzGr3ityBkfHpIYKGtefruEgJa_ts3nU9ySInM6MWtO2FofA9v3ralYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoQYYPbEVa_bxFtWsZJjxb-zkuEwkl1_LvDkuJCBEVjnnNIuMYxMeQFJAkimZGy3eG-91A_zRcfoQy7at40DJJGlR_VCbRRUY40x9ge8eUYnPe11YppibHXemoMPxCmo_BLHZPZVqLtY5GX63mUCrvOaH316FPO_CWOUe50pWwjKjvsAb6jWF9SBmCgI7SLMupzo_n1CMcQEwBpQ9YAYZ5olkFpyphK4mciGcif83_ddN5RsWonQLOcCTMWSmihVWwHG8cfuNXDwpRzm_P3HctfxPv-ZybId6XBsFXHFxbpvPQ6C46_jP0yavrXb6fsiXcFlLWizHPD002d6jK2n4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=a9wr-vXKjC9LCU_8mOL5Ws2cvbrVxLvr5UllHG1r2LIJToZxA3Ta98cMwwelPgkfcyG4hzQBAZmc6b-t5mHY6Tfx8QvHHzRhxNyFvVd2SZpMfsA7pa9BTNnwXVLl-38bNz1ENAmod2PwUT1lKPpCGxr1D9MX0TOzZNPpbvls5pkTdqVXnTMyZ7v15AWOgousz2AkU9AVaYkoiI0zNZJQVsCk6UV1q8UFspaWCaMyr1hRcL4PivLFcfR8cO-oivi3cY_WJE0ip59RfZ6uJnopVtRwMmTeFwheqZQU37tbxdzKADbQYdLB55n3FYuDN-N3QtN7NoarMcyUiohzv5nj7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=a9wr-vXKjC9LCU_8mOL5Ws2cvbrVxLvr5UllHG1r2LIJToZxA3Ta98cMwwelPgkfcyG4hzQBAZmc6b-t5mHY6Tfx8QvHHzRhxNyFvVd2SZpMfsA7pa9BTNnwXVLl-38bNz1ENAmod2PwUT1lKPpCGxr1D9MX0TOzZNPpbvls5pkTdqVXnTMyZ7v15AWOgousz2AkU9AVaYkoiI0zNZJQVsCk6UV1q8UFspaWCaMyr1hRcL4PivLFcfR8cO-oivi3cY_WJE0ip59RfZ6uJnopVtRwMmTeFwheqZQU37tbxdzKADbQYdLB55n3FYuDN-N3QtN7NoarMcyUiohzv5nj7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJhf17WHW7TpvJGbtrQRgNqfCbTm-j84Skbconm_bwRrj6ddNZlRzuXubrWthHBHinPnAsWkS2XmAecDQxjCQGTDy-wrje4nltXBLL1yXCnZAI71q4pR-00lequZzudYZ4Iysjzw74achCRptSoBKHLqIgs_YswgAfzXnxnmzbik0H-2ae1RoZOKLtXXFa-6W-6xNsMm4DnCnqCBn6Y0bglFGo7Ix9YacLdGsWKy212_P8uYiU-2YNoE1Z8gZdKJ-guj6YeFj-QVggdWPh5rXf2z27o_hREq4dutwsdsivxbLo7dGNQCRtXpO12jZaOwsPf8TsrUyMyI3txvxYDrvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/in6UpBEx8a-MvukWATkdkD2zuDNqia3Lq_H5HByS4tsvRqf9m-FxIIG7C2csY9tWL285290Ga1RxRNY95_seYM1hjfXgJECBJ45rGJefOhH_9H0EieyL4FmyXstPNYEnF4quU3QT0Ea2ax_SANEfI7QFDQndEF_OV9wsD5Uef3jf7U4ZBZiv4S-NrfmGwpcvIJqeQO5ILvKgdk3FQnkEV0A1tmxngvwcZ2SAohwh1blBbBpy6_HnwSe_B0NnKJOl37zYsx_VzRLiRuEO6994u3EQw2rniZX8gBUBHW3qFQA1Rb3q9vsN7aMqQ8PogSevw9QT3sgDxiXcz-jNL1cYUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=Y9lS2mpmqQ8zXqlkbYFlsMcE-oxXMgUGZT42fY_Qy6QLRHZq5otncoAul4tpiXaX-uPyIlXj4YXv5rMfKzALn9HvcBVy5xsv2m-BsD2ApwNVmuLko3Wekof3SQ1K1k8gX9oGFEVdbAYEzdNxnlWFkjbVIZMwFvVd9yNjkCSYigOwyA5wuA1lMKYhtTqS5zFeNXgjazWd18tqiWWoLA8LD8klGRWZXiwity_bR3zHcUPTLWwpM9CAmyfNRvK1pXOfvNNz1DSu07oDQ5PPwhEusa-EK81JH2dKVyE1DRzZxG9zmOfjLAd-biMY73Kh1-mHlrHNlE-JVFMRx4PcIZ51Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=Y9lS2mpmqQ8zXqlkbYFlsMcE-oxXMgUGZT42fY_Qy6QLRHZq5otncoAul4tpiXaX-uPyIlXj4YXv5rMfKzALn9HvcBVy5xsv2m-BsD2ApwNVmuLko3Wekof3SQ1K1k8gX9oGFEVdbAYEzdNxnlWFkjbVIZMwFvVd9yNjkCSYigOwyA5wuA1lMKYhtTqS5zFeNXgjazWd18tqiWWoLA8LD8klGRWZXiwity_bR3zHcUPTLWwpM9CAmyfNRvK1pXOfvNNz1DSu07oDQ5PPwhEusa-EK81JH2dKVyE1DRzZxG9zmOfjLAd-biMY73Kh1-mHlrHNlE-JVFMRx4PcIZ51Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=dcgsrKPX3kgsWbIY-Oo47h32j0yXQm_DQHygug5ZfbEpALg0bgxEHArCI9EGk8cjivdCnK4_Vp2weQopyjYxVmZ5KiYRYd1H_J-GAttv7uuoc8TmmjuKxiPB-gj51mJEGipaqXsY5-dhvzbthwZFYISJ02morDG4Q8oHBrYUTwpJSEYO6gb_ClmRCtnvBCmW3a6x1FsnV3YDxDtb1elu3RTkT6iKM5B3TM2mS_5PDZMOzG6CPy4g8JfBd0G2FS5Y5jNY4JKgm6beMAghocGu7PeBejp0X167okbf8_Ec1c1C0D_Zv9PN70KFd-aqVyF2W_B08k0DDMPgIWinIsUwng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=dcgsrKPX3kgsWbIY-Oo47h32j0yXQm_DQHygug5ZfbEpALg0bgxEHArCI9EGk8cjivdCnK4_Vp2weQopyjYxVmZ5KiYRYd1H_J-GAttv7uuoc8TmmjuKxiPB-gj51mJEGipaqXsY5-dhvzbthwZFYISJ02morDG4Q8oHBrYUTwpJSEYO6gb_ClmRCtnvBCmW3a6x1FsnV3YDxDtb1elu3RTkT6iKM5B3TM2mS_5PDZMOzG6CPy4g8JfBd0G2FS5Y5jNY4JKgm6beMAghocGu7PeBejp0X167okbf8_Ec1c1C0D_Zv9PN70KFd-aqVyF2W_B08k0DDMPgIWinIsUwng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=hSyWeHriAyUVhmsC6wjhvvkCQnTcjN-pvNFHN9irpkGRl9mFoKyM1_Gl-Dtej3LBR3KkTajMRihG3Z5FrUCaHCAeRchrEmi23UOz42m9p5Zqzla2A3-uLf3Da-udgiZkcIwxhHcoV-t7aoqviY5cRhS4vJtM8MkvNTSkwSV7ouEKVKFydr607tu2Pa1Mk1DNnlS8mh6WFa4DH5z7DzsLdqzQiv776mDEu4CuG9RBR2I7gr-ki7DqDao1NoR5a77CQa1LqCgylV3z_iUP6QfKLfm1MkpId499GNX6AC5oCSqyRmNbNTyzG6YxjsQ0q7Ifua8GyzyFRlXbhZfBzSUS0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=hSyWeHriAyUVhmsC6wjhvvkCQnTcjN-pvNFHN9irpkGRl9mFoKyM1_Gl-Dtej3LBR3KkTajMRihG3Z5FrUCaHCAeRchrEmi23UOz42m9p5Zqzla2A3-uLf3Da-udgiZkcIwxhHcoV-t7aoqviY5cRhS4vJtM8MkvNTSkwSV7ouEKVKFydr607tu2Pa1Mk1DNnlS8mh6WFa4DH5z7DzsLdqzQiv776mDEu4CuG9RBR2I7gr-ki7DqDao1NoR5a77CQa1LqCgylV3z_iUP6QfKLfm1MkpId499GNX6AC5oCSqyRmNbNTyzG6YxjsQ0q7Ifua8GyzyFRlXbhZfBzSUS0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7631">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bo0JTsCYy18OnpnPu2B2AZHq8sM4Vqq8we7-mCRo6Xc9OPwHChhpM9m8NKuoIROU1KJzlb25xOZC6wqBJJg35n8S2Td57PED6XnHJGgGQL9-1UB1DR1jYO5F182c3mVRst7R7JGZwRctonCNWmYk45fcnBqk20LsciJWXGblIopSJMCt0yXthrPLCRCSJaGUiNjZLbed2WQTQCZpzUOs2J8GEJr_1WeRY_LtkDqrdnd1ddJqN_X_ppw1ywPKFiNZSipRUOZr7aBXF9bZvdEab8-RlKccsK_rrU0HaDVs8Vl--CBFA6bdM3PZYpt5LGNeqbq7bid4fqHoPpJBUl-35A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=EHJ_rLf33O-RbFZi3JBuGN4h6gvjayfocEwzEJOQOUbdwflCEumxXKGXTPub_oKZps6buG7jAhM53I9u1uCjgutZiN8AieJDHbMNoed2ZQWfs2PSAUQ8GhAxKuIiGsUBWIpxbCIzSTPN8oMZ0b0wwwjn77Ao3qI-sjh12A7e5HSq5zJtYJwy9aLhh7wGJ2nPFgUJ4EhyXmTwZT6tM4wXg_Xzj8xluiMYfI_8v_hztcs1ED2g4osr3Va80TeioLI8XMUDT0aCmVQ8RGwIyO21GRXjK-nI0KQPdwRjPTY2iM22XTJoRQNV34tIlZMdFVBkLNvXdg6HoYZ2olKV-j4IDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=EHJ_rLf33O-RbFZi3JBuGN4h6gvjayfocEwzEJOQOUbdwflCEumxXKGXTPub_oKZps6buG7jAhM53I9u1uCjgutZiN8AieJDHbMNoed2ZQWfs2PSAUQ8GhAxKuIiGsUBWIpxbCIzSTPN8oMZ0b0wwwjn77Ao3qI-sjh12A7e5HSq5zJtYJwy9aLhh7wGJ2nPFgUJ4EhyXmTwZT6tM4wXg_Xzj8xluiMYfI_8v_hztcs1ED2g4osr3Va80TeioLI8XMUDT0aCmVQ8RGwIyO21GRXjK-nI0KQPdwRjPTY2iM22XTJoRQNV34tIlZMdFVBkLNvXdg6HoYZ2olKV-j4IDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7623" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7622">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsdy_O5oR1S2OflNJ1_MJRdDRH_gzOs6K-VfeALX_cqEl3Yxd3n6bWfOEbgLxLD3VofTSj70cqULnBgaidUXnguKwOHfRrwcIbkcYKnQr90s6ZzyykbXQoaETuDrQngoMfpYjTE3Lr1Spr321XsrF6M2SUL7lIhhrQZG_rin8ZtzT5F_0ZRHmgqCSU1_vboH-JSPPv2VEXwtz-DkX0SF5UXFqtyo_9LqCRSJRh2kN512SYwqGrw7lNbI3zPow_iUtguDTbMK4b00ocEldvesRf4K2INeTKWUt6UoUQ-PdcxVyOWOSafYZ2aswF63mGQpA_HI17QLZmvzjm9DhM9kXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCxCzTqZvRBH9fQO130b29anAAMTGfTLRIK3DpxiOZmiu7cu_WdTRoFa9sXBt9AQPAwf9m0XaNwWC6IkDs1Oc1lpEJhtU844HN530BkFHbX8KPxwoHCu68OmW7_TKPYXVXlz3rVTAUxdZL__rbuERZyuEWDpD_S-99qXkBZfCzMqa6moGPXBA5VFyFLz4Vp7mIQ7sjoSqDjykAuAKdZU4jl_yE4GRUV8jMofrDr3PZywDpGGl2woR7HMdhsE0Sx9722YAiklosD5AQuWIdWHOE-TwzNKkAEGeHWf8FPZ5v86Er3Ab6tNLWGE-0KAr7wlPHv869zfldMHQCR8TxDGvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5.1 2 days Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=claude-fable-5.1-high
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boeVeyWSf0Y3rpNvJz4BzukrzX6q5FjG3s2SiGKbiPSgvamYtHdz2Wzm7HJFoKHtIf7KLR2evnSG4Gka4cp2u26iVx-nXZ44DAR4RsQv58Nx2aNfKggOqrghW_3rO8nSemzeg4MrpQb39IrR8JIYI_p8xPolB0d0yEG7veCy3Grhq0gurykH-7_E3nZtGJEIbIN-tvQOFpQBUM6lB2YMkH8QofW-DPUi7YHprhqVXRO5FU2fQsZppkcrqvKS1KMeUg_ED-2qvqj9q50NaAMS_3y-binFZiGo1zVNakg9KYmmB2tWN2JNq1e0qA4ZXvKlVkYpesk_YPzTAtjOVivRbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7614" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7613">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cp9kowg0ID-_35fHPMBahoeQyLupVy0l-ovOlWVcPM-lxbL_oAUoLkLKPDxG6Y5lWQi_IFiFAp80JFACw4xwgnTDbNmb1Ul4RgxR55LGVE65GcfoUzdzUklMVk82CWUqdYLjQMkhYYdjZnVfWkBLyvDFUMc-kcC-ClTHJtwHLdCV5o_rcAytjwP2R5eJzKKsHSsInkwwwKWm_8nM7K5Bw2251_-s7FTdfAUcsfrMro2e7v0MoS3LRUR3WXiNpn-Pafm7-9FrmDCxhw3yLswHt2MltBL-LswhnYPPutUFSG4z1BVRDNgrJ3f7LJ6VNHV-dWNGzHc8OZ5_2DR-U6WQxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7611">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7611" target="_blank">📅 14:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7610">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdN2kKYNWhskhDbkJqIm1OyXkoiFJMKBg8sTlfrJ74MqvvujiKfxg3A7tqTaRQNku81i4qWGCNL7mI_HdkyRockuLnUVDQybJZVuUhYI7MePmtfXpjfWKcYGtybg6bI35okrGtgdrZeJSCJeSDadDw-qq9geLicw3RyMXbBBZrX4fYN66U9KFZK7aIkJ-T9lHtMsjbBtUBtQ9wsaVAFD4MwUfd_0ulpeCDG0fcvGw-xLizDAYLWnShqvK-lgp-2TvWmq1wWFOKgEWXswOOOM3KH-xHHshyw-IhAYMwEr1VwrmxQ5GBfDdJgmSGiOoYDN-YXe6B9V0EoKoemk8NpSsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7609">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hm7yZUAn28HvCfvWWz-vvIxMW5uQwqwmpS23Gv9vX9D6MsG53nNARkOeFXT5qIdo-BuHPCDjZLvgdtO2Q75q0PUeeq_pCg0bt3CJPTPqXUs70YjRKb__G7BybDL4z6EuDA6B6NRfryL5ChbazMBpympVGkEM87MXx5m_UedSd10fmddPo3R7cgCINoo1ZotbL65xUZI794CRqDJie-EUvFGvkZZxbTQheHJ088b5uHS4szFAkVzgABv10WrX-nkjRNE4Y1YfzcfP0HwnMA_Qk8NZmcTDFTDlBHi4GMEeqGnXFzT-SsUoCH1brzanL62KRu9jQj-O7FqN945LIwMxqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7604">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tj50_50-c3GIeN-LCMkda9RtSulfMLu_ettIIaBB-eDzvoJneAMkiHahBYhcbxGc452AmiDGyvOmZJAUSK_4GkLex4KFMLIfdXV0AkimrPb-62FN3VrUbHxhqPC7SQkkUHMMqpz3LoV0GayM84FXL4yJpkn9O5MmBGTnd0PXxo_Pe3mBR0VZ47_A6R0HCpjmACaIClclm_3wLbY_eGNeIKDSxZT4fweKPAWF1TSOxMq8_RKJ5Af7GVHxjOlBptgcJ05mlmx-tFE0XB7A0kQ7z6G47jydmJhXRUslKTEs8S1hnoZX0hWZA5sEvwvlENGxOvJoaXbSsK1kx7x33Y-nPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sx3EAzF8LjvSTDEwTiOalfEn_xm5RzpWgd9m_Ng5sFvavzuSZoi-Zq_FuROqMzFCMIqAJrJeOM0AKljJDZ3aEIkx4WmmsAtk3dG3jMuvzd7bdkrCYasFMsUAmKcW0dgp5S9Da1PByA4LV8QrBzGg_JrBmliCEw7gx_ZwkXnbYNR_v3k6T2X-1sCipgaEaiPf-SP4igDLoEK-hYpXT9AWA-AOQti5pYTu3rlz6H-izhaFqtO-yvlwJjyMR0opVKvPTPyWz2L101t1C_nFYKIFeoF3GCEPP1oj9AsN6r6enRDuAAaqfgZR-rljDWo4JJGMks3oiiMjrjLpGBlusgrFxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDCvbIM-XXzmxptQemCSkSEVOOcj3WKhNaxe97km9sAW_d1iASIPJzB69UrF3Ma-eQq2bottnmqhi0dQZEN6psFIqagNvjGDdzGJsbIgamRkLwRIJSgzmuKaUpGcS0GQADKU_NAO9mPqswghN6rdWFwixwss1cXjIvSqCE_Bx7X6Phdml_a8X1eOitgA9apkKwgOz37uDwu5MES_6Bqr4kRtZ52ARZZV5WY73H9ORAVnPIl026BkHT7cjv9LgDobFmXKW6DK8Ql45fm10eGO_PyBJntmQVy_hrPdjBDBJkCu8jTCVNwXEUtMIcAA3fWYlxUgtQ-B5_Zk-l_79MfSLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEfgkZaUByPY8gppR7JjeyGkpz2zL3_VQlHMneFPQyHATiviFbe8alak3qLP_xY0FdoR3RJNi76qUHL_loZ5Yp3RsofSWB02-Js4CZNz22ukQbrZ4o9gzL_O56jF8HP0PNbWwE6oPCqIqD6rcgvt-ZE0DZaf_pVGcg-mNAOvbLnVgaWc5tCzR_TrgmJa6nfi8TTKBeytIbib3sS1FpEmFAhlann4hkZi4YLMfr8sGp99iiG_KoGxnohhP8wffxwlrSbIlmfwnZEzIQANx2nV_H-tBjsPVuydew8bK1Z9nP9Swj5Uio-97t-yhatkr_CekRycfa0lX_L9IDIQgbYrSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHXZV6H1ZxwKdsvL9jBPbE-B8lG6SjvNeWODSgpqeHkZgasv69MZd7SHv5BQB8O-7btAM5riGmI2TPemvXS8O2ztTefJ0cymawDbBAJ6tBn8rdcV62zkmoi4YiKz5PgWdS8ORZZxVgNrp_gnM0q551oR4Y0dkMQ_hIFwJO9YWwpFijNu8E4c24HiKeR2iH0lNZ7J_su0PE5i6BIsXr24aQXqbFxnVE5Mckr0k_4KTyDHMBmYLXQWPr-lZMQYE6FKfSwff18xX0rCaB1QYmeTBsuYELs7lESfeMUkk2JGhWI1FlkzdrnlOScG5bXO836tw4vsxuiXMU9F4lB81xEG0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKe0BvAOJTMgbaGGiZPnqvfmuDTqhOPpQMPxApedNdJYu_BX_ynUF-2cKUqbbWs2tRW9VAwznJLg8rrM55gdaNzwZ32xnkPbruTAnkHh9D7u5YWzhC7rWdnxlysEd_HlBZbMVirPUnJIVUzqIwNr6l7olzfIL5H81FmbusikFrDiRMBXGFIzuutt-5KMCh3CUgK2P4tU4gej9Ga6Py-FWOhjAu94iro8qThIIWG0byJtjadscSbOVLNKDDMhEWQagsvC5ridyS8wRAyJGjEbj_g_FHLIsYri3wPJu1w5LvT93z1_6Yf0ujGYpW0uBWORzwiTL-JMfXA4eFc3p5XFlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWeID3wODUijB0ktLAYcffYoNsjrIvJkObAzwSlmbR494vEFv9pcvdZYiQz3z2aL1o-HIsk7IZyKhsp7edMf0ONkeGEnxcJLW4YeE0zlmkcvIiWsFovZkqT96iA41M-gf6iirBwaibYZdLFv7DndvMeDs7v4ioOt0qb0neJJLGi_KhkForKLBNJB4PG-cr8GxQMzbQJPrpYttUH5TbXKx3hV34_nIqnB8XgHl8aHD5vLC9ydQE2LVIiia9gYww4vPjhc0wM7G4PYRTr0ZKWWod2aN2U-rXEu4oTLRjs64K4QvwxXzNa4vFJ_ShZKqev4i2IuTNU47bV3cN2Qg7Whmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnRZrdZNHpr9_4NtFWqXpMjt0pbUQXimJ7ejSrDekp1VyDt4piz1v-rG1TDlAye_CyEtUdk_1fDiBgig_fSexvT2KIh2Idf_HK-mbzNlBzKlS0T70t5BbGfQyJf5ux498Ooms8zsk0h2Iu3vwtFQ4wFayY5Yg93nfJl4Kuu46dFj0ApyCwvjVcYcgU0KJEJQUYeMyvEBz2qqzTUto-iWP3CuAJyuFk9kmLtnytVY09VSu6SA0Hzun58CrPNVmrhYcpCxENWrpKXFezOhvdGT16k2fHwmTiuRitPUeJpyeMWXGG8apNyo9SGk5ZfdH52GDiHE09Wp-vGUOEPj8PBA2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMUYraUr7L9fgmxVLzt5eqlhuxrP9KhEwiOYOqGNp8yjuaLNezXTpw5EU25V0256VpdJyTChuIUoFMKDsKx5nqcdYO37WTW8yDJz2faC8lA5k7hScBLWkUJ2V055mBPnUxyYKqqJ_wiiwxSn_7twv0KY74M96cQJOhr984Guo5cpbmkMT69EV2txliBc8PvNVZu_p8YQbv0xQKGq7LlykrDrD_FzQERxSjjWDpJyrm7C4l2byFlqZ-Q34qb2hDr03JA85U_hm-JSGKsMmZeKNhVlfKhqs77e6Vxbu8kubT00EOvDhdeBSow5KY2f7gyHufAdMckWJmWlwLvykMxUJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
