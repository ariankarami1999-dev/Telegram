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
<img src="https://cdn4.telesco.pe/file/Z37a9DRXh6UxHrlp9BlJVFK0TS3DPLEaBViAkcr9kkYcWxU5BQYIhiyguRLk8i0jBZ-MjDaKBc1Lr5FS-XXJeOb7iXCid4_C2PKrlXlB4AV6U33Moy7dmCFz8_uK9d19SS5En3mZ3QdKizApCFbNTyCSIv7ALGFjX18PL9gkF9WR1PYKrp1917fSiz-_TRjp03bj9DkPLbO3lES0mEhIpkweZ6f8B1MyB-umZ1pSaLjDw8ej2bLTfKlG0eEnayh0E2lJA-lR3xg8tI86kObMgQOJRbNZ2EjcNUTvq5bEKNtLyL6dBA-LsVon3iqh4NoSwyM4Vm3qPhFV-gFq7xcSgQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.65K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 01:30:28</div>
<hr>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqHhYqp8GPjPznZGx-TxAKRlarsSk972CGn2rTXabE5TeFu9UELoKnGW7LZ9gmvAin0pgZq8Gcj2AFSlz4fkXv7LPsYrfCG_lHJpt9B0dWJ5IWSXXEtKNQ1Mcv8XaixN8zvLMLkaIx16Hh9qp1n5DaXx-Jax2wmvNOahnMycRkwsInMsL-hV8bUsnvQkmTGuXqlo1C_nl2gflgQuyNC8UvS3zHPXHEleZCEbqK1wU3ne5Tg1XhOT1knRNoyG4EMxx3GVkxFHC-oQAKHRSx7VEuI21fT-3H-rOMHIIk7nS6EP1yJE8AnzHIZjmtdEYAWWY7sE7J1JLQaP7L-6SDuQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دریافت یک ماه اشتراک پلاس رایگان پلتفرم HotGen AI!
🤩
✨
اگه به دنبال استفاده از قوی‌ترین مدل‌های تولید عکس و ویدیوی هوش مصنوعی هستید، الان می‌تونید اکانت پلاس پلتفرم
HotGen
رو به مدت یک ماه کاملاً رایگان دریافت کنید!
🔥
مدل‌های قدرتمندی که براتون باز می‌شن:
>
🔹
Seedance 2.0
>
🔹
Kling 3.0
>
🔹
Google Veo 3.1
>
🔹
WAN
🛠
مراحل دریافت (بدون نیاز به شماره و کارت بانکی):
1️⃣
وارد سایت
https://hotgen.ai
بشید.
2️⃣
خیلی راحت با اکانت گوگل ثبت‌نام کنید.
3️⃣
توی داشبورد کاربری‌تون، بخش
Tasks
رو باز کنید.
4️⃣
هر ۶ تسک ساده رو انجام بدید (ساخت یک عکس، ساخت یک ویدیو، اشتراک‌گذاری و غیره).
تمام! اشتراک پلاس شما به‌صورت خودکار فعال می‌شه.
✅
🎁
با این اشتراک چی می‌گیرید؟
به مدت ۳۰ روز، سقف محدودیت‌های تولید ویدیو و تصویر برای شما به‌شدت افزایش پیدا می‌کنه و می‌تونید از بهترین مدل‌های روز دنیا با بالاترین ظرفیت استفاده کنید.
(البته جمع کردن توکن به این راحتی نیست. زاییده شدم
😂
، الان تست کردم)
🔵
@ArchiveTell
| Bachelor
⚡️
#HotGen
#AI
#Free
#Kling
#GoogleVeo
#VideoGeneration</div>
<div class="tg-footer">👁️ 384 · <a href="https://t.me/archivetell/6473" target="_blank">📅 00:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚀
معرفی Remnawave؛ پنل مدیریت پروکسی قدرتمند و مدرن مبتنی بر Xray-core!
🌊
✨
اگه دنبال یه ابزار حرفه‌ای برای مدیریت زیرساخت پروکسی می‌گردید،
Remnawave
با تمرکز روی سادگی و راحتی کاربر طراحی شده است. این پنل به شما اجازه می‌ده نودها، کاربران و اشتراک‌ها رو در یک رابط کاربری وب بسیار تمیز و به‌صورت یکپارچه مدیریت کنید.
تمام بخش‌های این پروژه (بک‌اند، فرانت‌اند و نود) کاملاً با TypeScript و با استفاده از فریم‌ورک‌های NestJS و React توسعه داده شده است.
🔥
ویژگی‌های کلیدی و پیشرفته:
1️⃣
معماری ماژولار و بهینه:
دیتابیس، پنل وب و صفحه اشتراک (Sub Page) کاملاً قابل تفکیک هستند. یکی از بهترین قابلیت‌ها اینه که حتی اگه پنل شما آفلاین بشه، نودها بدون مشکل به کارشون ادامه می‌دن!
2️⃣
مدیریت حرفه‌ای کاربران:
تعیین محدودیت ترافیک، فیلترها و قابلیت جذابِ محدود کردن اتصال به دستگاه‌های خاص از طریق شناسه سخت‌افزار (HWID).
3️⃣
مانیتورینگ و امنیت بالا:
مانیتورینگ لحظه‌ای ترافیک کاربران و نودها، پشتیبانی از ورود با اکانت تلگرام (OAuth)، احراز هویت دو مرحله‌ای (2FA) و هماهنگی کامل با Cloudflare Zero Trust.
4️⃣
امکانات ویژه:
تولید انواع فرمت اشتراک (مثل Mihomo و Sing-box)، پشتیبانی از وب‌هوک (Webhook) برای کاربران و نودها و ابزار داخلی برای اعتبارسنجی کانفیگ‌های Xray.
﻿
⚙️
حداقل سیستم مورد نیاز:
برای نصب این سیستم قدرتمند (از طریق داکر)، به
۲ گیگابایت رم
،
۲ هسته پردازنده
و
۲۰ گیگابایت فضای ذخیره‌سازی
نیاز دارید.
🔗
لینک‌های دسترسی سریع:
داکیومنت
گیت‌هاب
داکر هاب
کامیونیتی
🔵
@ArchiveTell
| Bachelor
⚡️
#Remnawave
#Xray
#Proxy
#VPN
#OpenSource
#TypeScript
#Tools</div>
<div class="tg-footer">👁️ 544 · <a href="https://t.me/archivetell/6472" target="_blank">📅 00:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJtdMoXGHHuFJ_Yh7pwekZKqrz2ZVpQSGqiU21jZTjprLWghkXz_aJ4CLIzMbNFo9_KQkf4lEhoPjZdw-Dqh_yCSt24TuE-99K2AQABrr5fuvpGPTNND3hp2J4xtVriBfYfJJ0A5Bwl-5Zizc6yC-qMpveW9LGxPTjMzGr-jSDY93VgJmd8dHtB9ydzYtdWraL9qbStWrIvlvaviWD3JRjqf3xXt4Bmi97-obYDuAY5ivzzKt7OuHiGri24r5CAcqU-hFHiIMQDX5MN_0Yfb7-9WGXtjJxITfMAu6TJyeUbIS4nHaazP4m3X80yr2Vzb3bB780BhL4fF_7SHg_hoWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
یک کتابخانه رایگان از پرامپت‌های Nano Banana برای ساخت تصویر با
AI Studio
منتشر شده است.
✨
قابلیت‌ها:
•
🔹
پوشش سناریوهای متنوع برای تولید تصویر
•
⚡
قابل استفاده رایگان در AI Studio
•
🗂️
دسته‌بندی منظم و جستجوی سریع
•
🔄
به‌روزرسانی مداوم با پرامپت‌های جدید
🔗
لینک:
Site
#AI
#Prompts
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 737 · <a href="https://t.me/archivetell/6471" target="_blank">📅 23:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚀
معرفی Ladder؛ عبور از پی‌وال‌ها و خواندن رایگان مقالات پولی با یک کلیک!
🔓
✨
🔥
🔥
🔥
اگه برای خوندن مقالات، اخبار یا کتاب‌های معتبر تو سایت‌های خارجی با درخواست خرید اشتراک و صفحه‌های پرداخت (Paywall) مواجه می‌شید، ابزار
Ladder
این مشکل رو برای همیشه حل کرده! این سرویس با شبیه‌سازی رفتار بات‌های موتور جستجو، بهتون اجازه می‌ده محدودیت‌های هزاران سایت رو دور بزنید.
🔥
ویژگی‌های جذاب و کاربردی:
1️⃣
دسترسی نامحدود:
باز کردن مقالات پولی و ویژه در سایت‌های معتبر علمی و خبری مثل WSJ, NYT, Bloomberg, The Atlantic, Nature, Science, The Lancet و کلی سایت دیگه.
2️⃣
وب‌گردی بدون مزاحم:
حذف خودکار تمامی تبلیغات، بنرهای پاپ‌آپ، ترکرها (ردیاب‌ها) و اسکریپت‌های اضافی، تا یک تجربه مطالعه تمیز و راحت داشته باشید.
3️⃣
نصب و اجرای منعطف:
می‌تونید این ابزار رو روی سرور شخصی خودتون (Self-hosted) یا حتی به‌صورت لوکال روی سیستم (PC) نصب و اجرا کنید.
🔗
لینک دریافت ابزار
🔵
@ArchiveTell
| Bachelor
⚡️
#Ladder
#Paywall
#Bypass
#Articles
#Tools
#OpenSource</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/archivetell/6470" target="_blank">📅 19:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfxOqXzf5gdw5qElWX-dRzzQFgBoxxBuyvllDEOnuNaJhXsSH1DVAd5rSdnW54ob3AzxvZEcUeqsihzK_0kWYmiMPMP0wavBVeJPw6Ng23Qcrn_Bg_Z0S6ugo1Tr0pJVyZS1kuqLYlK1lrMQ0rMA1Owbgjz0lGI4lMA9Szwgqlf8r-6Y0FLKeQ1YfVfsaMFR3i2QrvuFvmYR3yqdDWoPpen472uiUD7xVDG7_BI123Xk6if2Uk2DFa_KLrmJM7eThrYq55Fw-JdbzdpGURMopLwxWRbykPa5OS1G9K4wJSCmR8IJnDVZEOLvE6muumPWGkHndKn5CKg3zCo374K-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
بازی‌های کلاسیک کنسولی را مستقیم داخل مرورگر اجرا کنید؛ بدون نصب و دردسر.
✨
قابلیت‌ها:
•
🎮
شبیه‌سازی کنسول‌های Nintendo، Atari، Sega و دیگر پلتفرم‌های قدیمی
•
⚡
انتخاب بازی و اجرای سریع از داخل سایت
•
📦
امکان آپلود فایل ROM برای بازی‌های دلخواه
•
☁️
همگام‌سازی ذخیره‌ها با فضای ابری بین دستگاه‌ها
🔗
لینک:
Site
#Gaming
#RetroGames
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/archivetell/6469" target="_blank">📅 19:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🎬
معرفی OpenMontage؛ استودیوی شخصی و هوشمند شما برای ساخت ویدیو!
🚀
✨
اگه تدوین ویدیو بلد نیستید اما ایده‌های جذابی تو سرتون دارید، ابزار جدید و متن‌باز
OpenMontage
دقیقاً برای شماست! این هوش مصنوعی خفن، فقط با خوندن توضیحات ساده‌ی شما، یک ویدیوی کامل و حرفه‌ای تحویلتون می‌ده.
🔥
ویژگی‌های جذاب و کاربردی:
1️⃣
صفر تا صد اتوماتیک:
از ایده و سناریونویسی گرفته تا پیدا کردن متریال (عکس، ویدیو، موزیک)، صداگذاری و تدوین نهایی رو خودش انجام می‌ده.
2️⃣
الهام‌گیری از یوتیوب:
فقط کافیه لینک یه ویدیوی یوتیوب رو بهش بدید تا سبک، ریتم و حال‌وهوای اون رو تحلیل کنه و یه ویدیوی جدید با همون فرمون براتون بسازه!
3️⃣
اتصال به ابزارهای مختلف:
این سیستم به ده‌ها هوش مصنوعی دیگه (برای تولید عکس، صدا و موسیقی استوک) وصل می‌شه تا باکیفیت‌ترین خروجی رو بهتون بده.
این ابزار کار رو برای تولیدکنندگان محتوا، معلم‌ها و هرکسی که می‌خواد بدون دردسر ویدیو بسازه، به‌شدت راحت کرده!
🔗
لینک ابزار (گیت‌هاب)
🔵
@ArchiveTell
| Bachelor
⚡️
#OpenMontage
#Video
#AI
#ContentCreator
#Tools</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/archivetell/6468" target="_blank">📅 17:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uwVy40eDErVQW-ZZQbmJ3aKCR8ZNZPxCMrUtdAlPz2IJCYeN7cs6IvoMOaQCGme6Lv356F_XEzVzLCZOYB9oTLACroQt_KnxRwD4Rbpk4tFhQEbzfIkBVm6qM9prc-NlO5ivgZLHBKTxyKmllHowokBRNC8x5L0ap5QPwH65FV2B6CZ590MgEBXkGKE1EQV2k0ffuTVgaRULgQgOABseLN46ltitZxquQaodJOsm0OlfvBvxAeL5YNDUw0Z76_kO3X8j9zi8qNHNwHQc6T3lGBnIvrwPHouNc2eMNx3_G3lNYUXSYj_ZN_-bKDA3NFiCMDVEJtVGT0kFe_HIKkF_ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oJ9aNCpAbvr5sFVvv9bkk_JB7Di9YxOxVS49lxA9aoGSfSabgphxLKT1uMC63kWVg3UyqKA7VvLWQBtr0qZRVQe4ER1UVH4m-x7iMFYGWKqXLUIPbjKv4vs-y8r8X5lauLyrRcBHcDEvZ_5dwugWBFkqG7k1shfPGM5ZI1QbazhW1WmsSZHFIyTddE_IQuAIE7HaCH-8BSCJ52nK_4BXi5oenMmoW4GJEpZ3JNnxVoPoqN9hJzZWOoIH12KEJEaNtQqUgq9yuDzLUqjrjvUDhwBb9_3YkiaYM24wauV5grETOEKaQAk6hoOF4o94x79U8qkEPSqSwSaaYrXnQlQ27w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P4EEEbgAlqcHNjkCVX6N_cmN50quYiJnYSzxgAx1DVRKQDNyA3nzJS8CQBOB1H8Fn7ohrs0ghjMB2MPIHcRuqvLB2U7OVCcKalsfB1BiBEWvy_zitHXR48XZS_Rj9qnU8It4NQmmmF10ANQ7-zedK0_KntzFzYUwwlqoY_dYKMnhnb5WTCSkAAtu7A7WfqS1d15_ivRQR84IZxAtRzAtioplZIciMxCtY8W-_0a_Ri0H_MND8V_XhjWBTN0LmmLOBD2k-ujoWyDuBeLwxPiTvawMaOgB2Btui9OLEgWV83Y_H1i8JBG80rTMqZGAFAVnl_OBSOxMKOgHjZfC3GsdYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U13G4b1AVJqAEq7cThbHgAvDXEckcOce214mbOXgDe7ickDqufFnCYNu43tA1GDuHtEhjbR5_GF1WGqRKGBsXWF-QmAueDOuiJbk-r2aX4oTiBgQsrCq1Kg9QhbMsFC2qGqi8ZXV43ec9o15nEUx12p-heP9BXkoZzT6yz3saqZJ1LC6rzOX4f1O4CuBBwWbApV_hl2XffWVxbeODyJhz70qXEag9CSPETYf91v0ITjZj7vfmHm8zJzaEndHhuq8FS8sQv-zIxWT_DIXrpQfz7r1ejZoRh8D44Jt0HjITT8etiGvY9PRSR7g4gKc7kQwPEY45WvMe0uaZYvGOC14DA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Splayer
پخش‌کننده موسیقی متن‌باز با قابلیت دانلود از یوتیوب و اتصال به اسپاتیفای
🎵
✨
قابلیت‌ها:
•
🔹
پخش فایل‌های محلی و مدیریت موسیقی‌ها
•
⚡
دانلود صوت و ویدئو از YouTube
•
🛠️
واردکردن پلی‌لیست‌های Spotify
•
🎧
متن همگام‌شده آهنگ‌ها، پادکست و کتاب صوتی
•
🎚️
اکولایزر پنج‌باند، ویژوالایزر و ویرایشگر صوتی
•
🎨
شخصی‌سازی تم و رابط کاربری
🔗
لینک:
GitHub
#OpenSource
#Music
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/archivetell/6463" target="_blank">📅 16:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚀
🔥
ویژگی‌های کلیدی و پیشرفته:
1️⃣
تبدیل سایت به اپلیکیشن: هر سایتی که فکرش رو بکنید (مثل ChatGPT، یوتوب، ایکس/توییتر، اسپاتیفای، دیسکورد و...) رو به یک برنامه دسکتاپ مجزا تبدیل می‌کنه.
2️⃣
حجم فوق‌العاده کم: برنامه‌های ساخته‌شده با این ابزار تا ۲۰ برابر کمتر از اپلیکیشن‌های سنگین مبتنی بر Electron فضا اشغال می‌کنن.
3️⃣
سایز مینیاتوری: میانگین حجم هر اپلیکیشنی که باهاش می‌سازید فقط حدود ۱۰ مگابایته!
4️⃣
مصرف بهینه منابع: به لطف استفاده از قدرت زبان Rust و فریم‌ورک Tauri، مصرف رم سیستم به طرز چشمگیری کاهش پیدا می‌کنه.
5️⃣
پشتیبانی کامل: این ابزار کاملاً رایگانه و روی ویندوز، مک (macOS) و لینوکس بدون مشکل کار می‌کنه.</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/archivetell/6462" target="_blank">📅 13:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hxmqW4zZ_Vdhy1Mo8WGx3pCJZolq7Ccyo6-eUU55V0l1JGuuQExhGabBqt7G6WKqaYmJF3rviSPQj832cYgVTceWfbsJfEd9Zi1S-_QAVchdm6COVPw43uP-V5hB0HvLqLVX2UOO6jj6_aU_ThDiVn0k9WG4dL6zTThR7fcX0MGN0ziOFQRT8Ma5snzlGYd9aSo5hZj_H33lJe1z7KwvmbR8SJcLTdY_Zh1OejNEA69oheFAAtnf5b2BYh4mll24qfRC5JmKAi2eYF4QFMcCEyIgGcUanvM0FHXYFatj6YPn2csekKxK6mP55FZo3SRC9YEGhihiSWyuePuOvN9zbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d1jSBM2YaPHnfmUz9ZUxG2pUYZygQZRS23eHFzLLHAea5qzfDK47IXq5qmJ4w5BvCnqPpxYpV4h3vJx_vBSkH9zjxenTLhVeaNuVG0_52PwUWgOUL9zdBHgwSO-lcUZ0rCFvWr8_a3YtFuBiFLRjOVj9iyO3zbOOXLfW5jo70tba_LlfmXx4k3K2Ml6XMihl1hOSHRewDWq3xhDFCFqbdxvNYdmOWfuJ69xbwTeFs0kZ9ydu5zG-RFm_wfrkvaq9VXDjxqniC-v63n3E-MrEgBCUoj9fMVOFOQ2Sonl5biamXa3cSc6fvbY-hBqztdmybY9zWTWg8I-ddJlMd9rEVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X6BgPBMHShSg3e6Dz-7zK35-OjAO9P9SWogLS0FygrGuoX7ZfpeslapryfRdCkQ3N2Y-L8jAMje-oNM7jN9p2aeHojoRK1QOfUp79-NiZJjUPUsUFQ2equlyOlHID5p1BB-AJwMNExcfqol1ZyIOcO1SiFuz2m6HXQuTUl53aafBpar4GSOyQ96pWxYUOaNhRzkR6g7CnL2ZzjA2gbUXc5xDU-ES-PEpvCgeH99ApjE-LbYRzg971E1YMtYyFLmFbiOuLAibH7y4FkCZc0bFzSQ3qsPTGiHR6dJ2HSRle4gK3OuE4oiIf4tcFfXAXiSceg5oY2zg9dAiCGl_JkS0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Or9uiw14GGC2igPcAzDNpBsNKSXHyo44bX2P9n8gjomdCfeqlBL02vBYhuq-kiwLTgPQd7NFxnqGWz4VM8Svhfz2WVyQ7Bi-UI7kHcO7aihPyflVWWHSZecjDAthe-qd7xJ1OxtlYjyBN9cIcbUl5gdTOa2e2cCCrHCm_p5qkYy-K_GCm-hRW9pUL2Aty64JuKEUN4Ifk0nKyf080wpCkC3lOkV1llaKswKWoTbK_QLiHkweK2H3FLert3kdB5LtKxlYaft6rEW0Cw6IuQGpQdEB2vn_AGqABI3a-gco8-cCZHInFB9gM8bLc11Zr3Y4hTIBqA9a5VfhtMU1LAfyPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ded905356.mp4?token=SivPGiZqbnu81tlVdJVV4SZ6e59aAm4JLOLsr-gKwov0sk9k6YPN_zaofXS3fhz6wbiSeyjUpBo32fTrzWIsBUOxfUcnUR2pZLlTkDUR-IDK1ZHuTmPqSfABPhGJ1hXCBLntKQowsSfuqt6vnhZ0z41XklozYOK0CFS3tiR3mTtBubEK6ttoschOKW9kh3Cnufar-izPNoBWJWWfXFNgwMlXYORUbTqdAmd4QTWLhK_1ieX_jUABjiPebnmK5l047wc93r3pT3ZGHIW5YIpbX_O860oPPmUfV_GXFoufJHRJxssw3oYszKy7bbSeQFZcxLhKbALGtuFhfw-BuYVkNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ded905356.mp4?token=SivPGiZqbnu81tlVdJVV4SZ6e59aAm4JLOLsr-gKwov0sk9k6YPN_zaofXS3fhz6wbiSeyjUpBo32fTrzWIsBUOxfUcnUR2pZLlTkDUR-IDK1ZHuTmPqSfABPhGJ1hXCBLntKQowsSfuqt6vnhZ0z41XklozYOK0CFS3tiR3mTtBubEK6ttoschOKW9kh3Cnufar-izPNoBWJWWfXFNgwMlXYORUbTqdAmd4QTWLhK_1ieX_jUABjiPebnmK5l047wc93r3pT3ZGHIW5YIpbX_O860oPPmUfV_GXFoufJHRJxssw3oYszKy7bbSeQFZcxLhKbALGtuFhfw-BuYVkNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
با Pake هر وب‌سایتی را به برنامه دسکتاپ سبک تبدیل کنید
یک پروژه متن‌باز برای ساخت اپ دسکتاپ از سرویس‌های وب مثل ChatGPT، YouTube، Spotify و Discord و ... است.
✨
قابلیت‌ها:
•
🔹
تبدیل هر وب‌سایت به اپ جداگانه
•
⚡
اجرای سریع‌تر و مصرف رم کمتر
•
🛠️
ساخته‌شده با Rust و Tauri
•
📦
خروجی کم‌حجم، معمولاً چند مگابایت
•
💻
پشتیبانی از Windows، macOS و Linux
🔗
لینک:
GitHub
#OpenSource
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/archivetell/6457" target="_blank">📅 12:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇺🇸
ترامپ: شرکت Anthropic دیگه تهدید امنیت ملی نیست!
🤖
✨
به گزارش Axios، دونالد ترامپ بعد از دیدار با «داریو آمودی» (مدیرعامل شرکت Anthropic) در حاشیه اجلاس G7 اعلام کرد که دیگه این غول هوش مصنوعی (سازنده مدل‌های Claude) رو یک تهدید امنیتی برای آمریکا نمی‌دونه!
🔥
جزئیات و حواشی این توافق:
1️⃣
ریشه اختلاف:
قبلاً سر آسیب‌پذیری و باگ‌های خطرناک «جیلبریک» (Jailbreak) تو مدل‌های
Claude Fable 5
و
Claude Mythos 5
اختلاف شدیدی بین دولت آمریکا و این شرکت پیش اومده بود.
2️⃣
اقدامات قبلی دولت:
وزارت بازرگانی آمریکا تو ۱۲ ژوئن محدودیت‌های شدیدی اعمال کرده بود تا دسترسی تکنسین‌های خارجی به این مدل‌ها محدود بشه.
3️⃣
همکاری و چارچوب جدید:
الان Anthropic با درخواست‌های اصلاحی دولت کاملاً راه اومده و کاخ سفید به همراه چند نهاد امنیتی در حال تدوین یک چارچوب فنی دقیق برای ارزیابی خطرات مدل‌های هوش مصنوعی هستن.
﻿
⚙️
سیاست کلی آمریکا در قبال AI:
ترامپ تاکید کرده که هدف اصلی، حفظ برتری بی‌چون‌وچرای آمریکا تو رقابت هوش مصنوعی با چینه و اصلاً قصد نداره با بستن یا تصاحب شرکت‌های داخلی، جلوی رشد این صنعت رو بگیره. البته این رو هم اضافه کرده که در شرایط اضطراری، از استفاده از قوانین سخت‌گیرانه نظارتی (مثل قانون تولید دفاعی) چشم‌پوشی نخواهد کرد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Anthropic
#Claude
#AI
#USA
#TechNews
#Security</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/6456" target="_blank">📅 10:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqGnd-qP9-EqtNSSJS_fjYNg4B3SA0HMbs5qJE1m0-FcBeT7lnFLKTHwymRP_lsnHh5Oq4_sioRsrbZfVAr4L8As8gPcQA48dKvWb-w50XdybkW8bzE72pm-82WkQPagEpHKkfUAsU0DXViPXeKHailcqcE8Gc8snEjvT-FdKgCspgJar6JdBnH7MEZB5_XxU5VSy55EPhXnw4AhiLgHWWMkwVh1iLgRWk5eTAxJV-TlaeyjFRqADFkWisLIFxYFBnzdBZpbUhP_tN1QmmbH6hmPUWDzwF8UK0OAFVCFJ1pXcIAEM9VLJQMt3oor2pKH9L16lxwuOtqP-GnDeprHOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">KillerPDF
جایگزین متن‌باز و سبک برای Adobe Acrobat
📄
✨
ویژگی‌ها:
•
🪶
مخصوص ویندوز 10/11 با حجم حدود ۶ مگابایت
•
✏️
ویرایش متن داخل PDF
•
🔗
ترکیب چند فایل PDF
•
📑
استخراج صفحات انتخابی
•
🖊️
نقاشی و افزودن امضا
•
🔒
اجرای کاملاً محلی، رایگان و بدون تبلیغات
🔗
لینک:
GitHub
#OpenSource
#PDF
#Windows
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/archivetell/6455" target="_blank">📅 08:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚀
مدل جدید Janus Pro از DeepSeek منتشر شد؛ پیشتازی در تولید تصویر!
🎨
✨
استارتاپ هوش مصنوعی چینی DeepSeek به‌تازگی گزارش فنی مدل متن‌باز جدیدش به نام
Janus-Pro-7B
رو منتشر کرده. بر اساس بنچمارک‌ها، این مدل در زمینه تبدیل متن به تصویر (Text-to-Image) تونسته عملکردی بهتر از رقبای قدرتمندی مثل DALL-E 3 (از OpenAI) و Stable Diffusion از خودش نشون بده!
این مدل در واقع نسخه ارتقایافته مدل Janus هست که اواخر سال گذشته معرفی شده بود.
🔥
ویژگی‌ها و بهبودهای کلیدی:
1️⃣
کیفیت و پایداری بالاتر:
با بهینه‌سازی فرآیند آموزش، ارتقای کیفیت داده‌ها و بزرگ‌تر شدن سایز مدل، جزئیات و پایداری تصاویر به‌شدت بهبود پیدا کرده.
2️⃣
تغذیه با داده‌های غنی:
در این نسخه از ۷۲ میلیون تصویر ساخته‌شده (Synthetic) باکیفیت در کنار داده‌های واقعی استفاده شده که خروجی‌ها بصری بسیار جذاب‌تری رو تولید می‌کنه.
3️⃣
مدل ۷ میلیارد پارامتری:
این مدل با ۷ میلیارد پارامتر، درک بسیار بهتری از دستورات (پرامپت‌ها) داره و سرعت و دقت تولید تصویر رو به سطح جدیدی رسونده.
📉
تاثیر دیپ‌سیک بر بازار تکنولوژی:
جالبه بدونید اپلیکیشن دستیار DeepSeek (مبتنی بر مدل قدرتمند V3) اخیراً رتبه اول اپلیکیشن‌های رایگان اپ‌استور آمریکا رو فتح کرده!
موفقیت‌های خیره‌کننده دیپ‌سیک و صدرنشینی مدل V3 تو جدول مدل‌های متن‌باز، حتی باعث شد تا سهام غول‌هایی مثل Nvidia و Oracle در روز دوشنبه با افت مواجه بشه. (شرکت‌های OpenAI و Stability AI هنوز به این خبر واکنشی نشون ندادن).
🔵
@ArchiveTell
| Bachelor
⚡️
#DeepSeek
#JanusPro
#AI
#DALL_E
#StableDiffusion
#TechNews</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6454" target="_blank">📅 02:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SuKitqaby5iyJ7YvD2SZ-OkvBdMde8t8kVldo_rmyGavZALgWIKFkHjHgXCNZ_pMC8CQl7Z6zb0m4_azLKoIITojVwP1iVWKRQvPPhsSM_bNfmp4LtX_eDmlicmM0dxHOHUBYC7Lwtbvv4PBCiHnHJBWiB9KaIjc0JKcawDaHx0zyz8VrSYCu4pdXOfIGz-MwN3QZXx3rrFPOvncJlboDbJlrFQxfcUoqR3a_dQMW_xvYT9tk1MV7mPyQ9B2yyRxxVW-fELLKn_6ouARdv_dbrmNfA67-Luj_8aif0Ked9w21cpUCRugPCjl5abHMltrK8kafH504CQFkmrX0vnbNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JfVOHgPka5BRdgW7Fiu8xu0ZO-UxH4ivUazcVMXzKoqtztgQGi4JlJGsQCDvHMEdTcYdf5rzHRoUsTKQomHYdFQTJYbOW6pLPZfoBQAvchbhZv3osxCUPu8hwHeLa2jQ3dAuwuC4Kt6sIZM63WdkEJa3O8l7hbMQHVdKhmbrj4iPqVKEfLq_5W1Vo683C1_Uo_eiIfAmiZRFScdzaFNAcXFIM1s9JPfjaZ2vv9dR30JpGFOi1FLXef5J5j_U6wSdddtY2BPGvFsZeKY-ZgwdlPIltmkloOpPwfC3jHGfR_d5KESu_Ol3Sg3MYQz5BzbmSX75HcUAoesunQIUBt9AlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Product photography on a solid sky-blue background, soft studio lighting, no shadows.Product photography on a solid sky-blue background, soft studio lighting, no shadows.
Two thick, fluffy, plush terry towels are neatly folded and stacked one on top of the other, deep soft folds, thick looped pile texture. Top towel: white with thin blue stripes. Bottom towel: solid cream. [product from uploaded photo] rests nestled inside a deep fold of the white-striped towel, partially sunken into the fluffy fabric. [product from uploaded photo] lies diagonally inside a fold of the cream towel below.
Water droplets cover both products, fresh just-rinsed look. Top-down angle, empty blue space above for text. Photorealistic, high resolution, sharp focus, no text, no logos, no people.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/archivetell/6452" target="_blank">📅 02:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVVpGUvr8NivhQ-ToEgq2crTdGJR5otAu7k3HNIY4a0eFvQfUiV-1IMC03Fcc8FwrlZJZw7L4RfTI4Urp63CYtCmpjPIXnX9h_TLt4iyPFAKbzGJUM7uCMBOGa6IsVcihc5E-117cZineFuN4F123NpwHFWDoeagimd3kX2Ftw9d6oA0zghvlpnphB7u28EQ0PYoMkU4mErmZPVRFao22S7lka3702R5yJf54jAxWRjqFFCBXjp7ifhbTEdkVQ6IZZzzUSg6khKvGJ8l0UIfGUy-2xAd2qu02q38jF0cFK9dcBJZazG0LouAQnUNmse2xH1_M76g5YZAFv_y6FveTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی BleachBit؛ ابزار قدرتمند، رایگان و متن‌باز برای پاکسازی سیستم!
🧹
✨
اگه به دنبال یه ابزار امن و کاملاً رایگان برای بهینه‌سازی و پاکسازی سیستم‌عاملتون (چه ویندوز، چه لینوکس) هستید، BleachBit یکی از بهترین گزینه‌ها برای حفظ حریم خصوصی شماست!
این ابزار با حذف فایل‌های اضافی، کش مرورگرها، کوکی‌ها، فایل‌های موقت (Temp) و لاگ‌های سیستم، هم فضای هارد دیسک رو آزاد می‌کنه و هم ردپای دیجیتالیتون رو به حداقل می‌رسونه.
🔥
ویژگی‌های کلیدی و پیشرفته:
1️⃣
خرد کردن فایل‌ها (File Shredding):
حذف دائمی و غیرقابل بازیابی فایل‌های حساس.
2️⃣
پاکسازی فضای خالی (Wipe Free Space):
پاک کردن کامل فضای خالی دیسک برای جلوگیری از ریکاوری اطلاعات قدیمی.
3️⃣
بهینه‌سازی دیتابیس‌ها:
فشرده‌سازی دیتابیس برنامه‌ها برای افزایش سرعت و عملکرد سیستم.
4️⃣
امکانات حرفه‌ای:
پشتیبانی از خط فرمان (CLI) برای اتوماسیون، اجرای پرتابل (بدون نیاز به نصب) و امکان تعریف رول‌های (Rules) اختصاصی برای پاکسازی.
🔗
لینک وب‌سایت و دانلود
🔵
@ArchiveTell
| Bachelor
⚡️
#BleachBit
#OpenSource
#Linux
#Windows
#Privacy
#Tools</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/6451" target="_blank">📅 23:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🌐
ارتباطات آفلاین، امن و غیرمتمرکز با Nomad Network (نسخه ۱.۲.۰)
🔗
لینک گیت‌هاب
پلتفرم
Nomad Network
پلتفرمی برای ساخت شبکه‌های مش آفلاین با رمزنگاری قدرتمند، محرمانگی پیشرو و حریم خصوصی است.
✨
ویژگی‌ها:
>
🔹
کنترل ۱۰۰ درصدی:
بدون ثبت‌نام، قوانین یا وابستگی به سرورهای متمرکز.
>
🔹
تکنولوژی LXMF و Reticulum:
مسیریابی همتا‌به‌همتا (P2P) و زیرساخت مش رمزنگاری‌شده.
>
🔹
انعطاف‌پذیری بستر:
اجرا روی امواج رادیویی تا کابل‌های نوری.
مناسب برای دور زدن محدودیت‌ها و ساخت شبکه‌های محلی ایزوله.
🔵
@ArchiveTell
| Bachelor
⚡️
#LXMF
#P2P
#Reticulum
#NomadNetwork
#Mesh
#MeshNetwork</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/6450" target="_blank">📅 21:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6449">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=Due-o-WLTwBDkm2BLIcHnbaZE1y-nSkiDoUzF8P7L3mh5ZN3mtR_EyMDpaULbzUgeOQrxBrzggWD7vjbjH_XnBcQcOr7hGzFmylA_gvUuAj2TSbMCLZRfTcwW-CpHslPaDpVu1cxacLY0oGlobydD893B8_VKrIxogYa6IVxAl82_DkE235t-OGZXZpDmC6tVWfB1SaeUL7f5FMS7xzP8eSDPhul6u4lP7XANCpqNKYm9L-X6jLK60xphfakj8Lcais7sBUKjU3cWAzkMkiooxGq3-RnczWzRIMmkm8VKNSZdcdBRzMF2aOGVVIJDGl1Zs1gE1KrWuwJcbswq00VHqSUfpGnKdtcnsvPoh5kqeyCv7wAbMAsJ_9HZggZrhLW2Fxk4T09-Gu2JxPRlZ5e9K5RnuDjtVS4konBsqHSDpgzkfJ088WJSULUzDX8GAcol7MdzvRZqLNeplu6-yDhKx_X2StM_ovGihkZz9JYJ6hayGAYT_JQNYRlhACumdsWsJBagZDAwHsC6K1bHlSU56ujqJOWUkAloa17EqHc8G9Cvcchj8QoR8j_dtcAihbsWmzn7IEVACGnU4bVQHV_Msog9oxbJ6daRHmw64ELGWXcgArQQm2VOuGVdf7dbpNMm-YdMjmwzZKfQRoeF2bdqHbbN0TxlpuhAA74XAdn_1M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=Due-o-WLTwBDkm2BLIcHnbaZE1y-nSkiDoUzF8P7L3mh5ZN3mtR_EyMDpaULbzUgeOQrxBrzggWD7vjbjH_XnBcQcOr7hGzFmylA_gvUuAj2TSbMCLZRfTcwW-CpHslPaDpVu1cxacLY0oGlobydD893B8_VKrIxogYa6IVxAl82_DkE235t-OGZXZpDmC6tVWfB1SaeUL7f5FMS7xzP8eSDPhul6u4lP7XANCpqNKYm9L-X6jLK60xphfakj8Lcais7sBUKjU3cWAzkMkiooxGq3-RnczWzRIMmkm8VKNSZdcdBRzMF2aOGVVIJDGl1Zs1gE1KrWuwJcbswq00VHqSUfpGnKdtcnsvPoh5kqeyCv7wAbMAsJ_9HZggZrhLW2Fxk4T09-Gu2JxPRlZ5e9K5RnuDjtVS4konBsqHSDpgzkfJ088WJSULUzDX8GAcol7MdzvRZqLNeplu6-yDhKx_X2StM_ovGihkZz9JYJ6hayGAYT_JQNYRlhACumdsWsJBagZDAwHsC6K1bHlSU56ujqJOWUkAloa17EqHc8G9Cvcchj8QoR8j_dtcAihbsWmzn7IEVACGnU4bVQHV_Msog9oxbJ6daRHmw64ELGWXcgArQQm2VOuGVdf7dbpNMm-YdMjmwzZKfQRoeF2bdqHbbN0TxlpuhAA74XAdn_1M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Palmier Pro
ویرایشگر ویدیو نوآورانه و رایگان که با هوش مصنوعی کنترل می‌شود
📹
•
🔹
اتصال مستقیم Claude، Cursor و Codex از طریق MCP
•
🔹
برش، تنظیم ریتم، صداگذاری و افکت‌گذاری خودکار
•
🔹
درک رابط کاربری توسط AI بدون تنظیمات اضافه
•
🔹
ابزارهای جانبی برای تولید تصویر و ویدیو
🌐
Site
#AI
#VideoEditing
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6449" target="_blank">📅 19:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeBTjgnOAgcC8foSp4cuL295iqGoDiVXDex8kRm3XqSTtn5_0uurxEY7CmMI6lSJg8OA-eLr8kY2A5I0KaMljXFTRflGN-MeIAtqmUlg2UziJ1vo-ZUP15UBTvpPjww01UOlP6Ic6mNujQHOPAR0Ci084Hve-mJJLzA5fmJJVfjeWl6e--GyQgZ19qbfAhr1LuwKp9P4jj71NCnluBQxGZYu131GeiggMe1cUF_msAwk5iRJDVF0nweVQPcDtqKBKXXwCflf5tT7A78OXjurWOYNWjoRcddztXTatcDFCmLVTb2dhu3pomSPVog5N_HcX5Gg0JEGZXDES0y9AeH3qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اگه حوصله داکیومنت خوندن ندارید و یا پروژه‌ای داکیومنت درست حسابی نداره، به جای این‌که سر خودتون رو درد بیارید، یه سر به سایت DeepWiki بزنید و با کمک هوش‌مصنوعی، جواب سوال‌های خودتون در مورد رپوهای گیت‌هاب رو پیدا کنید. اون خودش داکیومنت و کد بیس رو کامل مطالعه می‌کنه و کار شما خیلی راحت‌تر می‌شه.
🔗
deepwiki.com
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6448" target="_blank">📅 18:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNVKSLwgFE7b8KZ-fGsRONkIGEu5w89ijaJXaQk_saOdaNWEZ0eUvzq0h61pbGRX51hHYqgW9iZEtF1iysxkyUAELdYGMOw4Nc52M-me9GdLOySN3zb1DQNYlmQQhofl0WHU3oh4qHk9hCA5J-zXTt-y_06m4G08E1PoNs1PVEAFHKv-hPkUa6Z_Pskz13w96NlkGIUyc308pE3ys--kGd06jGAUwIKtdjq6hMbU27asxhVFyX-mqwlwlLd9Kxojj7NuqsTcmytX6uSFv6N1QFWuu7Jb1Yj6brfnr51LHtiOnE2l1vpaYCLRMZZ981mLOclQ6aZwGgC8prq1fVx5Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت موزیک رایگان
🎧
https://freemusiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6447" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6446">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚀
آموزش استفاده از مدل‌های قدرتمند GLM در ابزار Claude Code!
💻
✨
اگر از Claude Code (ابزار برنامه‌نویسی محبوب مبتنی بر ترمینال) استفاده می‌کنید، الان می‌تونید با اتصال به پلتفرم Z.AI، مدل‌های بی‌نظیر سری GLM (به‌ویژه نسخه جدید
GLM-5.2
با کانتکست خارق‌العاده ۱ میلیون توکنی) رو جایگزین مدل‌های پیش‌فرض کنید!
🛠
مراحل راه‌اندازی سریع:
1️⃣
نصب Claude Code:
(نیاز به نصب Node.js 18+)
تو ترمینال وارد کنید:
npm install -g @anthropic-ai/claude-code
2️⃣
تنظیم API و متغیرها:
تو سایت
Z.AI
ثبت‌نام کنید و کلید API بگیرید. برای سیستم‌عامل‌های مک و لینوکس فقط کافیه اسکریپت زیر رو اجرا کنید تا همه‌چیز خودکار تنظیم بشه:
curl -O "https://cdn.bigmodel.cn/install/claude_code_zai_env.sh" && bash ./claude_code_zai_env.sh
(برای ویندوز باید متغیرهای
ANTHROPIC_AUTH_TOKEN
و
ANTHROPIC_BASE_URL
رو دستی توی سیستم ست کنید).
🔥
ارتقا به مدل ۱ میلیون توکنی (GLM-5.2):
به‌طور پیش‌فرض کلود کد روی مدل
GLM-4.7
تنظیم می‌شه. اما برای استفاده از نسخه
GLM-5.2[1m]
، فایل
~/.claude/settings.json
رو باز کنید و این مقادیر رو به بخش
env
اضافه کنید:
"CLAUDE_CODE_AUTO_COMPACT_WINDOW": "1000000"
"ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-5.2[1m]"
"ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-5.2[1m]"
⚙️
نکته حرفه‌ای در مورد قدرت استدلال (Effort):
با دستور
/effort
داخل محیط کلود کد می‌تونید قدرت تفکر رو تعیین کنید. اگه این گزینه رو روی
max
یا
ultracode
بذارید، مستقیماً به استدلال سطح Max در مدل GLM-5.2 متصل می‌شه که برای حل باگ‌ها و تسک‌های پیچیده عالیه.
💰
هزینه‌ها چطوره؟
استفاده از مدل GLM-5.2 تو ساعات اوج ترافیک (۱۴:۰۰ تا ۱۸:۰۰ به وقت پکن / ۰۹:۳۰ تا ۱۳:۳۰ به وقت ایران) ضریب ۳ برابر داره، اما تو ساعات غیرپیک (به‌عنوان آفر ویژه تا آخر سپتامبر) فقط با ضریب ۱ محاسبه می‌شه!
🔵
@ArchiveTell
| Bachelor
⚡️
#Ai
#Claude
#GLM
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6446" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTiamnIsEj2FF-xhAAsDnTonCsL1zoOIQcujTBDfRXTBzJ1HrdDg3RpEnaC_ySoOHXuZmwKYL7-5MMp2j3z9t9KhSYSxopOM3DCXnRNem6_oj4fjIBJHJ-wHa8Cl59wFM85M_kud_aHQbslqmX88pD0Bgq4Gka2Z5_UBe9jRmqj68OQizpaCzKT7dCs5Il8c5hH8t9CGnGN75deAOR6_wd0f16hDzWw5uGrMaMXE1oMW-rvkB-6x12qzyG47ZuDt1sPZUKNwfkS1GX9sj7KliV7Bvu49HBxL0o29SCwypwl04lnVKekLCMhKFt6jsu59NYpuQS4SgRrd8zab-ZiOaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
۶۷ کلید ترکیبی پرکاربرد در لپ تاپ و کامپیوتر
⌨️
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6445" target="_blank">📅 01:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🎯
پروژه Universal Android Debloater
📝
این ابزار یه رابط کاربری گرافیکی (GUI) کراس‌پلتفرمِ نوشته‌شده با زبان
Rust
هست که با استفاده از ADB به شما اجازه می‌ده گوشی‌های اندرویدی
روت‌نشده
رو دی‌بلوت کنید (برنامه‌های اضافی و پیش‌فرض سیستم رو حذف کنید). نتیجه این کار؟ بهبود چشمگیر حریم خصوصی، امنیت و افزایش عمر باتری دستگاه شما!
──────────────────────────────
این پروژه متن‌باز (Open-Source) در واقع فورکی از نسخه اصلی Universal Android Debloater است که با تمرکز ویژه روی افزایش امنیت، سرعت و بهینه‌سازی مصرف حافظه توسعه داده شده و با حذف اپلیکیشن‌های غیرضروری، سطح حمله (Attack Surface) رو به حداقل می‌رسونه.
✨
ویژگی‌های کلیدی:
🔹
رابط کاربری ساده، روان و کاربرپسند
🔹
دارای یک لیست جامع و کامل از پکیج‌های سیستمی
🔹
قابلیت دی‌بلوت کردن دستگاه (حتی بدون نیاز به کامپیوتر)
🔹
دارای ویکی (Wiki) و مستندات کامل شامل آموزش راه‌اندازی، راهنمای استفاده و نحوه بیلد گرفتن از سورس‌کد
🛠
از نگاه فنی:
این برنامه با استفاده از زبان Rust و کتابخانه گرافیکی Iced ساخته شده تا تجربه‌ای بدون لگ و یکپارچه رو ارائه بده. از نظر حریم خصوصی هم خیالتون راحت باشه؛ هیچ دیتا یا اطلاعات کاربری جمع‌آوری یا ارسال نمی‌شه و تنها ارتباط خارجی برنامه، درخواست‌های (GET) به گیت‌هاب برای دریافت لیست پکیج‌ها و بررسی آپدیت‌هاست.
چه کاربر مبتدی باشید چه یک متخصص فنی، اگه می‌خواید گوشی‌تون رو بهینه‌سازی کنید، این ابزار یکی از بهترین گزینه‌هاست.
💡
حرف آخر:
با این ابزار، کنترل کامل عملکرد و امنیت گوشی اندرویدی‌تون رو دوباره به دست بگیرید!
──────────────────────────────
🔵
@ArchiveTell
| Bachelor
⚡️
#Github</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6444" target="_blank">📅 00:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oN6lbtKvrpwbxtIeYXYWJcgrR2T_gs3vfV_6XR7ZcNORHVDyVbeqdAAYUHptE_g7kNKj8_BULYnm2Y17ECKeKyyxz1UK1z0i8x3QRj9o9D5EY9mssbrtTJe5CqignyH-w4RIVFDIJOqCMDjCOTysarC26nvNIVGJIvjZp-GoSa9hUwMFaT2Vmx5-Q59CQ3timj3d_EnMmOJ0U0msbPKRXzBnQFyxEmpkeV57PE7PWayM02KeoQgB7tCDUUe8rtyjTf3RsBu1zUOfs7JwKEtz7Bp8FrsU2i4v-hPNfD-olG9erUQNiFcgEb5V4CN2qFal0DzX__orsKb68m4pxeYIUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دانلود کامل ویدیوهای یوتیوب + ویرایش فوری بدون افت کیفیت
🎬
یک توسعه‌دهنده دانلودر شخصی خودش را متن‌باز منتشر کرده؛ ابزاری ساده برای دانلود و ادیت سریع ویدیوها.
✨
قابلیت‌ها:
•
🔹
دانلود ویدیو با کیفیت اصلی
•
✂️
برش، چسباندن و تقسیم ویدیو داخل برنامه
•
💻
اجرای کاملاً محلی روی سیستم
•
🆓
رایگان و متن‌باز
•
🧩
رابط کاربری ساده و کاربرپسند
GitHub
#OpenSource
#YouTube
#Downloader
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6441" target="_blank">📅 19:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚀
آموزش اجرای GPT 5.5 xhigh در Codex روی ترمینال (کاملاً رایگان)
1️⃣
ثبت‌نام در Freemodel
وارد سایت
Freemodel
شوید
با حساب Gmail ثبت‌نام کنید
بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🔹
گزینه 1: احراز هویت با شماره تلفن
🔹
گزینه 2: احراز هویت با تلگرام
✅
گزینه
Telegram Verification
را انتخاب کنید
🔗
وارد ربات تلگرام شوید و Start را بزنید
🎉
در این مرحله پلن Pro برای شما فعال می‌شود:
هر ۵ ساعت: ۱۰ دلار اعتبار
💰
هر هفته: ۶۶ دلار اعتبار
💰
2️⃣
ساخت API Key
وارد سایت شوید
از منو بروید به بخش
API Keys
یک API Key جدید بسازید و ذخیره کنید
3️⃣
نصب Termux (روی موبایل)
📱
اگر موبایل دارید، از Termux استفاده کنید
4️⃣
دستورات نصب در ترمینال
(
به
ترتیب وارد کنید )
1⃣
آپدیت Termux
pkg update && pkg upgrade -y
2⃣
نصب ابزارها
pkg install proot-distro git curl wget nano tar -y
3⃣
دسترسی به حافظه
termux-setup-storage
4⃣
نصب Ubuntu
proot-distro install ubuntu
5⃣
ورود به Ubuntu
proot-distro login ubuntu
6⃣
آپدیت Ubuntu
apt update && apt upgrade -y
7⃣
نصب ابزارهای ضروری
apt install -y sudo ca-certificates curl wget git nano gnupg lsb-release build-essential python3 make g++
8⃣
نصب Node.js
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs
9⃣
نصب Codex
npm install -g @openai/codex
🔟
تنظیمات Codex
mkdir -p ~/.codex
cat > ~/.codex/config.toml <<'EOF' model = "gpt-5.5" model_provider = "freemodel" preferred_auth_method = "apikey" model_reasoning_effort = "high" disable_response_storage = true
[model_providers.freemodel] name = "freemodel" base_url = "https://api.freemodel.dev" wire_api = "responses" env_key = "OPENAI_API_KEY" EOF
🔘
تنظیم API Key
echo 'export OPENAI_API_KEY="کلیدتو اینجا بزار"' >> ~/.bashrc source ~/.bashrc
▶️
اجرای Codex
( با فیلترشکن خوب وارد شوید )
codex
✨
حالا Codex روی ترمینال شما آماده استفاده است
🚀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6440" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp7E_3ptToRBN2lYWZsB5x5Jyx3TVebYTKbjFIgnq-jpOeU_piP_jMSQaow0HceFSi0yb1yfACk-JxP1UmM6G_MrVI0cGNjSvivfbQdSBsrXRwHQvrZH7bFthoDtqX22shfZ2CrHN3YusRBHr6X1lOGHM5aFkiVcFJN2JsNKoRq8wU0_wauNvgvJJp78-9E_OV6qeC3YB6jOwAHuCUpTlHMngDBQbheaGjI7foERyj56BVSZserTqM5rFRaCJ31MPxu_VZcWXp7FxPccfdRDVy7jOLWXcgSnD36NXOSgqwWFhr4cNAf2zursFrNR2HM169-VMqx_IzlXqLHDxWscxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
راک‌استار از کاور رسمی GTA VI رونمایی کرد ، پیش‌سفارش این بازی افسانه‌ای از ۲۵ ژوئن ( ۴ تیر ) آغاز خواهد شد.
#GTA6
#GTA
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6439" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6438">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">💻
ایده داری ولی حوصله نصب ابزار و دردسرهای راه‌اندازی رو نداری؟
🚀
Replit
یه محیط برنامه‌نویسی آنلاین با AI داخلیه که می‌تونی مستقیم از مرورگر پروژه‌هات رو بسازی.
✨
امکانات:
• کدنویسی با کمک AI
🤖
• ساخت سایت، ربات و اپلیکیشن
🌐
• اجرا و هاست پروژه‌ها در همان محیط
⚡
• بدون نیاز به سیستم قوی یا تنظیمات پیچیده
🔧
برای شروع سریع پروژه‌های شخصی، استارتاپی یا AI گزینه جالبیه
👀
🔗
سایت
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6438" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6QiW8jN24V7zDDoWRnyAZ763t_rx8pcrvp1H-IY3Nrf0fK1bVxzOiWbV-TWX8AvseOhoToWeluZwDlnBVwTHicINWmCqxNLsLMOKS2enM7pjSVNIXMCX2A6NQRmXddmasfzbz2N15cmAZIxu71QzF8o88-TzzXgO_mK7RNUNnS5yrH0UBhU34IAWtJjDgGBr2vjHKStacSMzvmcBrzcRQ1ZzJqAg-B59ZJsB0K6XjM306mqriRjTaFcQ2XRAeMJHa_YNTuKuJpRok3R640igmZjJ8CKkqwztHMQlN9Wf6WwSosLjWN7GQpZRlGLF4StJ2lkk_Av3iTKVUE3P_bn-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دسترسی رایگان به Claude OPUS 4.8 و GPT 5.5 + دریافت ۷,۲۰۰ اعتبار!
💯
🤩
پلتفرم
Gumloop.com
یک رابط کاربری چت حرفه‌ای با قابلیت اتصال به سرویس‌های مختلفه. جالب اینجاست که این شرکت به‌تازگی ۵۰ میلیون دلار هم سرمایه جذب کرده!
مراحل دقیق دریافت اعتبار:
🔹
از طریق حساب گوگل یا مایکروسافت (OAuth) ثبت‌نام کنید.
🔹
در مراحل ثبت‌نام اولیه، به سوالات پاسخ بدید و هر گزینه‌ای که می‌تونید رو انتخاب کنید.
🔹
وقتی به بخش اتصال سرویس‌ها رسیدید، Apify، Semrush و Reducto رو انتخاب کنید (هیچ‌کدوم نیازی به لاگین ندارن).
🔹
اتصال به Slack رو اسکیپ (Skip) کنید و نادیده بگیرید.
🔹
اگه مراحل رو درست برید، حداقل
۷,۲۰۰ اعتبار
به حسابتون اضافه می‌شه!(که مال من نشد
😂
)
🤖
مدل‌های هوش مصنوعی موجود در پلتفرم:
Opus 4.6 تا 4.8، GPT 5.3 Codex، GPT 5.4، GPT 5.5، Gemini 3 Flash، Gemini 3.1 Pro، Gemini 3.5 Flash، DeepSeek V4 Flash & Pro و Kimi K2.6.
❌
در هیچ‌کدوم از این مراحل نیازی به وارد کردن کارت بانکی (Credit Card) نیست.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6437" target="_blank">📅 15:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚀
آموزش اجرای Opus 4.8 Ultra در Claude Code رو ترمینال ( کاملا رایگان )
1️⃣
ثبت‌نام در Freemodel
وارد سایت
Freemodel
شوید
با حساب Gmail ثبت‌نام کنید
بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🔹
گزینه 1: احراز هویت با شماره تلفن
🔹
گزینه 2: احراز هویت با تلگرام
✅
گزینه
Telegram Verification
را انتخاب کنید
🔗
وارد ربات تلگرام شوید و Start را بزنید
🎉
در این مرحله پلن Pro برای شما فعال می‌شود:
هر ۵ ساعت: ۱۰ دلار اعتبار
💰
هر هفته: ۶۶ دلار اعتبار
💰
2️⃣
ساخت API Key
وارد سایت شوید
از منو بروید به بخش
API Keys
یک API Key جدید بسازید و ذخیره کنید
3️⃣
نصب Termux (روی موبایل)
📱
اگر موبایل دارید، از Termux استفاده کنید
4️⃣
دستورات نصب در ترمینال ( به ترتیب وارد کنید )
1⃣
آپدیت Termux
pkg update && pkg upgrade -y
2⃣
نصب ابزارها
pkg install proot-distro nano -y
3⃣
نصب Ubuntu
proot-distro install ubuntu
4⃣
ورود به Ubuntu
proot-distro login ubuntu
5⃣
آپدیت Ubuntu
apt update && apt upgrade -y
6⃣
نصب ابزارهای ضروری
apt install -y sudo ca-certificates curl wget git nano gnupg lsb-release build-essential python3 make g++
apt install -y curl nano nodejs npm
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs
7⃣
نصب Claude Code فیلترشکن بزن
npm install -g @anthropic-ai/claude-code@2.1.167
8⃣
تنظیمات Claude Code
mkdir -p ~/.claude
دستور زیر را برای باز کردن فایل تنظیمات بزنید:
nano ~/.claude/settings.json
کد زیر را داخل فایل پیست کنید (کلید خود را جایگزین کنید) و با زدن Ctrl + X و سپس y و در نهایت Enter ذخیره کنید:
{
"env": {
"ANTHROPIC_API_KEY": "کلیدت",
"ANTHROPIC_BASE_URL": "https://cc.freemodel.dev",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلیدت'"
}
▶️
اجرای Claude Code ( با فیلترشکن خوب وارد شوید )
claude
✨
حالا Claude Code روی ترمینال شما آماده استفاده است
🚀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6436" target="_blank">📅 11:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfsUUkVfANU6nyrKfM1A1j40wasHh3alwnMrwmbIbU7NnPkgbnaeT15Mm7gZV0FvLw8MBvMECDtW2rp7iCpc3zq8_wv33uG4k3N4AzFdi5SkorCk2BtDwsht6JJEFjsAv_BJrxUV_bhZermiukwRjrWRbLORfXuOcHIdS7IFaMrF_FOQmMJnOQwePxNcDOwpjDk2Ynmu90J1uyRKBENi5bJuRKdv8nKPTH2HJc4I1LlZRbl9f2BW1WnZ6mVeRwTllHygfJRiatxDoZXQGt2VyW3JTRSxkVE6nCLkUwiM80FS3npumUkPS15nAHSFL2a92VlHPjaUzReqJlcHoXWbJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ دلار اعتبار رایگان OPUS 4.8 و GPT 5.5
🔥
🌐
ثبت نام
#API
#Claude
#GPT
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6435" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=XBXJBq2gpK5wDW8-3CeE9cqYecmY_fC8GjwyoHcysw1wxRuG3l5ome0k7rsvnaJwiDm_gYx0l07m_MESpQdbl_8azd1-tsfl81KERJqMZcJjp3dooUWwplDXiFKOuXWyU7jyogJDo7GTi9ghlxA_NzjYXZlZgN3KUPssQLgWq1S8u6u8k6yaJuuTvN0ublgqM1QqJ--tofCqPJu6RbuJ3etSjN65_fQKrud4s8jhi9BQMKi-zK8LzV22nFWj62rNcCwf1vHVUPym5KutB-C2rAvnOlYsE-rR2RqkMRL2CggfC7Eu4lnwPn4Ka16EeSg9g8Hym80bvpvzHbJiypXtFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=XBXJBq2gpK5wDW8-3CeE9cqYecmY_fC8GjwyoHcysw1wxRuG3l5ome0k7rsvnaJwiDm_gYx0l07m_MESpQdbl_8azd1-tsfl81KERJqMZcJjp3dooUWwplDXiFKOuXWyU7jyogJDo7GTi9ghlxA_NzjYXZlZgN3KUPssQLgWq1S8u6u8k6yaJuuTvN0ublgqM1QqJ--tofCqPJu6RbuJ3etSjN65_fQKrud4s8jhi9BQMKi-zK8LzV22nFWj62rNcCwf1vHVUPym5KutB-C2rAvnOlYsE-rR2RqkMRL2CggfC7Eu4lnwPn4Ka16EeSg9g8Hym80bvpvzHbJiypXtFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
Open Design
یه نسخه اوپن‌سورس از Claude Designه که واقعاً به درد می‌خوره
😮‍💨
باهاش می‌تونی از روی یه پرامپت، سایت، دک، تصویر یا حتی موشن بسازی و بعد همون‌جا توی محیط امن ویرایشش کنی.
✨
چیزای مهمش:
• 150 تا design system آماده
• 260+ پلاگین
• پشتیبانی از Claude، Codex، Gemini، Copilot و بقیه
• خروجی HTML / PDF / PPTX / MP4
• همه‌چی لوکال و بدون قفل شدن به یه سرویس خاص
خلاصه اینکه: یه ابزار جدی برای طراحی با AI، نه فقط یه چت‌بات دیگه
👀
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6434" target="_blank">📅 09:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">با سلام درود رفقا میخوام یه ربات open vpn بیارم
دنبال پنل درست حسابیشم
اگه کسی پنلی داشت که بشه حجم و کاربر و ایناشو مشخص کرد ممنون میشم داخل کامنت همین پیام یا پیوی بگه ممنونم ازتون
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6433" target="_blank">📅 04:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✨
ویندوزتو سریع‌تر کن با Sparkle
🧹
یه ابزار رایگان و اوپن‌سورس برای بهینه‌سازی ویندوز
• پاک‌سازی و سبک کردن ویندوز (debloat)
• بهینه‌سازی سیستم با یه کلیک
• مدیریت DNS
• نصب برنامه‌ها با Winget / Chocolatey
• حذف فایل‌های اضافی و junk
• بکاپ و ریستور تنظیمات سیستم
🚀
همه‌چی تو یه داشبورد ساده و مدرن
🔗
GitHub
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6432" target="_blank">📅 22:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🧠
AI OS
سیستم عامل هوش مصنوعی لینوکس
👇
یه سیستم‌عامل ساختن که بهش میگی چی کار کنه، خودش واقعاً انجام میده
🤖
🔒
HAL (امنیت):
• کار ساده → خودکار
• کار حساس → تایید می‌خواد
• سیستم → بدون اجازه دست نمی‌زنه
📁
دیتاها لوکال می‌مونه + حتی آفلاین هم کار می‌کنه
خلاصه
👇
دیگه چت‌بات نیست… یه OS هست که کار می‌کنه
🔥
🔗
Github
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6431" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⚡️
Gemini
داره می‌ره سمت ساخت ویدیو با چهره خودت!
یعنی یه عکس از خودت می‌دی و بعدش می‌تونه ویدیوهایی بسازه که انگار خودت داخلش هستی.
فعلاً این قابلیت دست یه سری تسترهاست، ولی اگه عمومی بشه، تولید ویدیو با AI یه سطح جدید می‌ره
🚀
#AI
#Gemini
#Tech
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6430" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6429">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U81NFTJqbE5xMGGPpZ3N3xRvnGUy5XIPjvhfGTb2wPgZZco0RUKtjFvGrwhts9ZMD4h0oBQhKweITxLSewvTu6UF4sb-T4Xp3IM-nAmZi6nYxhbos0ggIRUMb2P6ArI0WdLOmjpXbT2O0jA6DkGuWF15MKWjwFQ4JTOHRDtPHu0Jo519FVYD6Mw83zR-fTzaExOX9U5pFimnkIOmcgnfylQ1QG5NL7zkgniOUFTZx9s-JL0brdhLM20B6fx_5CQwj_MuUWq2nyaiIND-gSlajDuv-CjISn5hsvodrOa1Y6A5lSre-VNFTbmQH2D7Kw4_glYp7o536s7YuRPiM5QWIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍎
اجرای macOS روی کامپیوتر معمولی بدون راهنماهای پیچیده و تنظیمات دستی — علاقه‌مندان اسکریپتی ساخته‌اند که نصب سیستم را خودکار می‌کند.
🔹
نسخه‌های macOS از High Sierra تا Sequoia را پشتیبانی می‌کند.
🔹
روی پردازنده‌های Intel و AMD کار می‌کند.
🔹
به‌صورت خودکار ماشین مجازی را ایجاد و تنظیم می‌کند.
🔹
کمک می‌کند محیطی برای Xcode، Logic Pro، Final Cut Pro و نرم‌افزارهای دیگر اپل به سرعت راه‌اندازی شود.
🔹
به‌طور منظم به‌روزرسانی و پشتیبانی می‌شود.
▶️
دستور نصب:
/bin/bash -c "$(curl -fsSL https://install.osx-proxmox.com)"
GitHub
#OpenSource
#macOS
#Proxmox
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6429" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🌐
DigitalPlat FreeDomain
راهی برای گرفتن دامنه رایگان
این
پروژه به شما اجازه می‌دهد بدون هزینه، برای سایت یا پروژه‌تان دامنه بگیرید و سریع راه‌اندازی کنید.
✨
🔹
دامنه‌های رایگان فعلی:
• .DPDNS.ORG
• .US.KG
• .QZZ.IO
• .XX.KG
• .QD.JE
📊
طبق اعلام پروژه، تا الان بیش از ۵۰۰ هزار دامنه ثبت شده و مدیریت همه‌چیز از طریق داشبورد آنلاین انجام می‌شود.
🔗
ثبت دامنه و راهنما
#Domain
#FreeDomain
#Web
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6428" target="_blank">📅 15:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">ایپی 188.114.97.6، تنها ip واقعا تمیز کلودفلرِ ایرانسل دوباره باز شده، بقیه ip ها رو alpn-1.1 (وبسوکت) محدودیت شدید آپلود دارند، در نتیجه پنل های bpb و ... رو اونها قابل استفاده نیست و فقط XHTTP رو سایر ip ها قابل استفاده است.
///
ولی علاوه بر
188.114.97.6
که مستقیم بدون نیاز به چیزی وصل میشه، رو بعضی ip ها مثل
104.17.121.43
نیز فرگمنت باعث میشه که محدودیت آپلود برداشته بشه و اون ip قابل استفاده باشه، تنظیمات زیادی برای فرگمنت کار میکنه به طور مثال در حال حاضر میتونید از:
"ip": "104.17.121.43",
///
"packets": "tlshello",
"length": "1",
"interval": "0"
استفاده کنید.
///
تمام مطالب بالا راجع به ایرانسل (و بعضی نت های دیگر در برخی مناطق) میباشد، و رو بیشتر نت های دیگر محدودیتی وجود ندارد و اکثر ip های کلودفلر به طور مستقیم قابل استفاده اند.</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/archivetell/6427" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bub1J_NmalrRB7Mc01bj8p_cwMDR36qVhaaX7RLlaPoS7uQ3VLyMiapkMdF9jK6Qazaqutvy5e9LUIf_ANjrmzFS_eU4-uMLoNbqlEZ0c3wPKsgRthlITk_kiQmU6D2fms2BgZRJkqapun99cwHctSGmVCsrXwnT84V_URKkzDeYTxkhOylY5M1iJc8Pv9FAktTP2tKhkECD9CBF9OHtPISpuKe8xJEkTt75eyYzMdd-DQGk55j3X-lXJGVGpiud0gtxG8SCbZvB9LKr6hbcX9W38C9d7zUIQWKWhIAks8aSDX07Vimk3cSj_FmAz94AVVKZmEAo4YQE7HK_nZ8VEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡️
برنامه Sandboxie؛ اجرای امن برنامه‌ها در محیط ایزوله ویندوز
اگر می‌خواهید نرم‌افزارهای ناشناس، فایل‌های مشکوک یا مرورگر خود را بدون دسترسی مستقیم به سیستم اصلی اجرا کنید، Sandboxie یکی از قدیمی‌ترین و قدرتمندترین ابزارهای Sandbox برای ویندوز است.
✨
امکانات مهم:
🔹
اجرای برنامه‌ها در محیط کاملاً ایزوله
🔹
جلوگیری از تغییر دائمی فایل‌ها و رجیستری ویندوز
🔹
ساخت تعداد نامحدود Sandbox
🔹
فایروال اختصاصی برای هر Sandbox
🔹
محدودسازی دسترسی به اینترنت، کلیپ‌بورد و فایل‌های سیستم
🔹
محافظت در برابر اسکرین‌شات و نشت اطلاعات
🔹
پشتیبانی از مرور امن وب و تست فایل‌های ناشناس
🔹
متن‌باز و رایگان
برنامه Sandboxie از سال ۲۰۰۴ توسعه داده می‌شود و امروزه به‌عنوان یکی از محبوب‌ترین ابزارهای امنیتی ویندوز برای تحلیل فایل‌ها، تست نرم‌افزارها و افزایش حریم خصوصی شناخته می‌شود.
🔗
Github
#Windows
#CyberSecurity
#Sandboxie
#Privacy
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6425" target="_blank">📅 13:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NE0piIi09DYVX2Bxog8tkIxWrW8b8gMjk1kS6ju8b84b5DdptBwss9xRcMbceAYtZ_IwRZKYGxp3NzVolCeCFz12g8S-zTaAESCtRSkLeZH0ln3akNSQPA_vuyR9OtnnPVapeUKGB76sqxtRkGe3hfRoStM-_FQGOX1nTwiK9qlRv00t8fg5NbwYbeUwxH-Vt7sn-qOgJJx4GIfy647bEgLfVMc3uB4GIAe6f-SmKJRoCYfzEEentOVOfWzLfnSD3nHYhOnM_LSHqXu5Xb3rCaJRr4PqFauVU9C37MkuuaHn8gZO8eT9O3PgNES1rTkM-Nx1LfmU9ygKo9o8ojJZUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏬
دانلود ویدیو، موسیقی و پلی‌لیست‌ها بدون تبلیغات، اشتراک‌ها و مبدل‌های آنلاین مشکوک
یک رابط کاربری مناسب برای ابزار افسانه‌ای yt-dlp پیدا کردیم
🔥
قابلیت‌ها:
🔹
دانلود ویدیو از بیش از ۱۰۰۰ پلتفرم محبوب.
🔹
پشتیبانی از کیفیت تا 8K و صدای بدون افت کیفیت.
🔹
قابلیت دانلود کل پلی‌لیست‌ها، کانال‌ها و زیرنویس‌ها.
🔹
امکان قرار دادن ده‌ها فایل در صف دانلود.
🔹
به‌صورت خودکار مرتب‌سازی و تغییر نام دانلودها بر اساس قالب‌ها.
🔹
اجرای محلی روی کامپیوتر شما.
🔹
پشتیبانی از ویندوز، لینوکس و مک‌اواس.
GitHub
#OpenSource
#Tools
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riJ2Htin05Wl301fYXoro3hwo5dTVdOoeuiOzHhjztlM9BL1o94imSVbFqCZFLrxmMe99lZrbQ30BsH3R78ctvOW9eUuLM3VUs5VT-fbULVbYw1-rgz6AvBqoB0xLEISJI1J0XREE2HJyCcO_HcZWcVsQkhLiGtz206Co6xtgRMu2mebkmccecI2Fvy8mEqpozl-Uo78udfCOQq1iDA9JtcjO74Bwn8tTQ1oZEu2RPgfqbPXaTOwoz7JAJi7IMn3IkeAiL4Y2Y3rUFbaqH2qqbgYZouPA8wjJH20G8OotS8qbPXMnXGRHMIcGFJph659ZFDJrj2b2mhTeoMfLB7dOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت api رایگان- GPT5.5
لینک 10 دلاری
ثبت نام بدون لینک، اعتبار نمیده و با صفر شروع میشه
وریفای کردن هم با تلگرام انجام بدین که تایید بشه براتون
با شماره مجازی نمیشه(چین)
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6423" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAeGXcy6aFpIsVAdArYLu7R4rkZUHRQ0MFEGnccnwMj_OtS3YpuFsknXXBpkGAdyyTk3g6sBqGDAPlRIAf0-Ff5VYzsl_QSeOqJf1G-O5998JxYw7JVYFRWrIvofX_RIo9hFqXrdDmT1kLKmBfxy8wDk_qMQtK_aZQKY1cSlOR5RqPwnKJ9GIrtDSL09C70roNWrIOKIseNOarlcElfr0RWNfHWXqRG7oo1feXNWP2wFhyrpo-R6C7can3okhl3bFwEUXaCcMlaIyymojYdkXtWUv4imyIvm9Y69aqa5MWrY6_bxhDPeJND0stKMJgnFnOpxrDWZaOi0OgR2l6mF4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مدل Cursor در حال توسعه یک مدل جدید با 1.5 تریلیون پارامتر است!
⚡️
نکات مهم:
🔹
از صفر آموزش داده شده و نسخه ارتقایافته مدل‌های قبلی نیست.
🔹
گفته می‌شود برای آموزش آن از حدود 100 هزار کارت گرافیک H100 استفاده شده.
🔹
علاوه بر کدنویسی، از Agentهای هوش مصنوعی برای مستندسازی و مدیریت تسک‌ها پشتیبانی می‌کند.
📅
طبق گزارش‌ها، این مدل طی چند هفته آینده معرفی خواهد شد.
#Cursor
#AI
#Coding
#LLM
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vxRDiOFy0qRQmbH8p7MPKWRYuZTbo6666oPZxGG9f1Eyh-vut-GWkGxFocnzEyppSogd27x25ahEzD--8vgoYF7xaUHb0dCcvB09wVSDT4sl4okptL70mNhFBDcxtdchJoXaFocTHTwiZpT9YLjGOqWiV1Nf6s0hPXrNrII4G9Y9pJC44Tp0Ivft6Y5wx4JWC21HWbI0nv-Esaml-MFIWp-kkEXtKeCgsWvS7IiVIhHaKf_t5sXeAyGwbsDHgl4zjBportjNRp0XMhW4b0Jo0J7I05jT5OOuoAs7aJf8rA41jHH8t1oM-0R9WRoKnyKO0LAMWfJQ9hM9210aNQt_7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P4YdAR-rvXlKSnO5YGgrRu8Fy-4YPCaKO8GR5P09EQPikWFLqMMTxuxxyS4ra-Bw__EH4QqHg1SKRMEHm2KUXOSFl6QZOrRvqU0WR9BqvqfZrsOQLV7peFxsenk9aIJ3uxnu4elXpC0m_gN4oUGyJTsx8HoTu3nyBd-E7XbLTr_F1VGO2Kz_2PVlavIGl3tM_G8jf-WLALv1H59eTC4Xlvn_TsGm1wulwtQSM_s1yw1mpyu7Bt_Bu9eF-GboX4Rj-XuckwH77vVWctH5l40fAnkxa2JhYg09qXEa18_RkPqCwxkG4091s34wCU_VnS7usCAyRfkJgjeHceXOovr8gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fjcuJFSeqp4meHs1YCOPsG_x8i3uKDE06W0JJFCWB4comNKfPlPv4nbOSGAJ48bn6khwKiMSKdn5jvd1kVeMO3XSXNxd1zWufStx0tJN1mBf4ohm9Aof_jWgWxX1BcEyCuIRSaA4iW8m-haWxTxmEiaiokVWw25nNqf0GWm0zWSDc9AbQ7iuAKGlmd2qqjftFxfDPikbMATQQ0vwXgbJuOUfgRWFY5UDstPY_Ob5DCabuNuUDDFjRWRzUD1QJPsPw8xj0vqPjnIr671Qg3PfcLtok3bHh0GfGfN7BrXlsOGArCMpIGKZLbaJ3Ak3NW4x-Bi3xPqljooVGnn-ZTjbUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل جدید GLM 5.2 از چین معرفی شد  توسعه‌دهندگان چینی نسخه جدید GLM 5.2 را منتشر کرده‌اند؛ مدلی که به‌گفته برخی بنچمارک‌ها عملکرد بسیار قدرتمندی در استدلال و کدنویسی دارد و توجه جامعه AI را جلب کرده است.
✨
نکات مهم:
🔹
عملکرد رقابتی در تست‌های Reasoning و…</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6419" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LfEt1SU2LMZhyMtfwPVAKS9a7K_ceeYds9fofu-t2x4k_7lj-Qt5YAXB2Oi8acoHzAP6dFxWVaBqZJvWmgC54ta5g251Gv7xLaPjUc3vgkxnMEs_mE3tYVYcL1GAwMVacNyZooBzodGtWmpq-kGICRRPGU7aj2az2lkAfu8eiBj8wo-Jzxy6UWVvii2tJ-I4FXwswsTGO9pYGcNXjAar_zfu6nuV9l1uir0TTgVVdv8r8hm-eTw1dhqyoNT9eHjDZ9WvpP-R_uzNX5frUgQoJp6ncaUiGfw0DPfpXnsYCc9z0D_42Z-yAvzGmHlVgpi4o_MQs0ePwp40dat58VizqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R72GLkL60-RVcm11Z-CytDF38jV9y11Q7ILstExYqX7c0IMEx4hTtW7IEwEbQAo5XpcpK8DDh8bLjbQBTQnkaFKMPkUj4qRyPWLaMawkIwOn0_GAMRCKtCNW3FqSq2z3M541EPVnw3nNrg-8x_E96B0JYbzJw0TGPw1clLTzKPY3CSRjt1raB_1ttBmuxtWl3BFM46Fc1t45gFDXh7nQuCF_bJNIlZn-MkIUJRZCVpa62dIvElaEW8M2kca2wISgIdaQwif-2f4pbn0-GMEwcsOBqg-NjfnsMRFqzagvqTi4W7Mta4lScQh-Wo0tj1gReM1FnCgxNdCEkLtlcPlmzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رقیب رایگان Suno پیدا شد
🔥
StableDAW
یک استودیوی هوش مصنوعی برای ساخت موسیقی روی کامپیوتر شماست
✨
قابلیت‌ها:
•
🔹
تولید موسیقی بدون نیاز به اشتراک
•
⚡
ساخت ترک با پرامپت متنی یا ملودی خوانده‌شده
•
🛠️
ویرایش دستی ترک‌ها با رابطی شبیه FL Studio
•
🎹
پشتیبانی از MIDI، سازها و استخراج نت‌ها
•
💻
اجرای محلی روی کامپیوتر با سرعت بالا
🔗
لینک
#AI
#Music
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6416" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Heybaat.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6415" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">sadra.ovpn</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6415" target="_blank">📅 04:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">sadra.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6414" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">همین الان ساختم
نامحدوده
تست بکنید به احتمال زیاد وصل باشه برای بعضی مناطق
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6414" target="_blank">📅 04:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6413">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🌐
ابزار متن‌باز
CF-IP-Scanner
برای پیدا کردن سریع‌ترین IPهای Cloudflare منتشر شد.
این پروژه با اسکن رنج‌های Cloudflare، بهترین IPها را بر اساس پینگ و پایداری اتصال پیدا می‌کند تا در ابزارهایی مثل
Xray، V2Ray، VLESS و Trojan
استفاده شوند.
⚡️
قابلیت‌ها:
🔹
اسکن خودکار IPهای Cloudflare
🔹
نمایش پینگ و نرخ موفقیت اتصال
🔹
مرتب‌سازی نتایج بر اساس سرعت
🔹
خروجی گرفتن از لیست IPها
🔹
اجرای کامل روی ویندوز بدون نیاز به نصب وابستگی اضافی
📈
اگر با افت سرعت یا ناپایداری اتصال مواجه هستید، این ابزار می‌تواند برای پیدا کردن IPهای بهتر مفید باشد.
🔗
Github
#Cloudflare
#Xray
#V2Ray
#OpenSource
#Network
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⚠️
همراه اول بسته نامحدود شبانه که لیمیت سرعت از ۶۰ گیگ به بعد داشت رو حذف کرده
✔️
بسته های حجمی شبانه آورده
🌐
100GB
💳
49,000T
🌐
200GB
💳
69,000T
🌐
300GB:
💳
99,000T
👍
خوبیش اینه لیمیت سرعت نداره
💵
کد دستوری خرید :
💎
*1000*252#
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🤖
ابزاری جالب برای اتصال دستیارهای هوش مصنوعی به شبکه‌های اجتماعی و سایت‌های محتوایی!
با این پروژه می‌توانید به مدل‌هایی مثل
Claude Code، Codex و OpenClaw
اجازه دهید در سایت‌هایی مانند YouTube، Bilibili، Xiaohongshu و LinkedIn جستجو و اطلاعات جمع‌آوری کنند.
✨
کاربردها:
🔹
بررسی نظرات کاربران درباره محصولات
🔹
جستجوی فرصت‌های شغلی در LinkedIn
🔹
جمع‌آوری و تحلیل محتوای شبکه‌های اجتماعی
🔹
تحقیق و بررسی بازار با کمک AI
⚡️
گزینه‌ای کاربردی برای توسعه‌دهندگان، پژوهشگران و کاربران حرفه‌ای هوش مصنوعی.
🔗
Github
#AI
#ClaudeCode
#Codex
#LinkedIn
#YouTube
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F2iW5sgk1NbZNS4UZ9dUW1tiN2IqROPDzN4GbqjguIq-EcYB-MepKmeRozIufqGxFbUX7kvXSc9oiwbk2jccySPoMItl1iRpk5hzgpX7W1sot6FhqrsMyq1LhDDG08i2_e6h6rpn2iOvwf_Ses-EFJrXwxuUNfGVQ02D3G0wAnMMwj01oYCD3RKheDCThKr_l4UQvEQvhMV3PMDLjRsjFkAyMpkaGfawnlLMXkCH_gfdxwMQCzepZiXIHDGO3JwqryJgXR1ohQ90lFtscZxlEHytdYeDkxsAvLWmFDS4W02nt_PTkHhLbHwQ2fq7rDU07bXYDiwlwc_0ZnilPQsx7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ARRTX70X7fAsDZWUQYswALQGeXhwkjJF-CdbutgYDS7O95LZYdwmjC9e4T_MWsJET7AgMYbd4iXXyXLK2-prsgvKFjVRypGePYLJw1fyn6ahDMJbPUkAJ7i_F5pnKeVVXUNfiAcsTotcUC5LLPKRSUVQCxhruX0gpdL1Qq4UQrrTBD-0-WB3LZrhxPIwgaI2aJ-uBAGD7vRyjfZ3K4WDqd_vS3eJFJqcMVH_V4yuAXn2eaelIb881atlmfSCQOMc2T_3UQGDNRd2SSI8uwvF6pVManpgoU_hAgLzjKqaf9HrThOOOK0uEWKG9Zvul8RtOuyQ93A-UmN-7ekXKtp7Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KzaZQLpTwFvlsdzTtD12dkUw09rGhtUnUSf-dtH3w-5aWYoLljVuPsnQxVlBov3_PgKM96D6K_Hyoy1W9uSOr9JHUvnrv2g7X6nnnwojbCaly_htmNJRpPVfUJNPAvQrBnbc9V7LU4i6KN3wI8VG1Ue00yt0MIincbSHcVsCuZH8QCJ96LpZzXtFH9eUq83pVYdYFeupUU9yHCrRvTYMUzAbE6QV0EV7tjNgp0PqtJdapfLENNCfV-uMydsg1wPzj6ktd44XuzVoZQVbq_s0l_WAZbHES4aTQ3ijiRqM0gKYdepH6VCOwWLuz4xr4dPbgtseFodarEhnukLl_rR7PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UyBZiMwHSnvWC98ok5ReRYKFkkErng8_S19sLb7Z-tPQ0K_OoV0KebBcBa1YfAapnLBxtykSJZHaeABIucuBv--Ke85HsHdkB4aOHk0t26D7DnnmZiT7K4rGKSoF83rDuSzl9o74gt3eINaU8Kye3AFzbZ0hKtlIuNaIOLauQM8UMmIAdnpmJGXIznYoZThAUHfhK9ZMkSyiTgeG2l0b1hJXLxSSHMn4M2F8F2MXnYrjhHgdyDqY09ZO3gVRqaXnK4Hj0zWnlj-Ynz-fRw1PBXHSzcGSNnQtKbcDjyRBBml1rg1ZI6uhqrCY6M345OpXoqFQT7ctI0-V7DJEmJzYzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت تصویر به‌علاوه کتابخانه عظیم پرامپت‌ها.
- طراحی‌ها، تصاویر، نقاشی‌ها و راهنمایی‌هایی را که توسط هوش مصنوعی و هنرمندان و طراحان برجسته جامعه ایجاد شده‌اند، مطالعه کنید.
http://Arthub.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e186940244.mp4?token=cWhXmSo4kkDge3WFqHCojORHI2Qt8Ig2ArzHiAOpp2QqeVZtOHFVXwdtsioEHK1MG-jiSrLr1ZK4fIKZTM3wE3Veb97s9oRZGZGOFfWaszlTXqQ7iNO5QvS4S886E9mdXj_aPXBeQrMM8a8uMfCVS1SjvN95fGZC1AtKmnrf3GxianHFCwKQmSxB3_hXlCQfxvE4vonW7Y5GlcWt9sydBKiTqs0Y3rMG_puY_oNMla7dlrASEw0EHTrKtS77mNpV0QzhFMOZA8DuDxdu0FWa-COaAzSTao_IhUnHzbuwvn3n8JdR4kPf9T0IMj0iFovNZGhHxIByqKXNgbiK1AQQcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e186940244.mp4?token=cWhXmSo4kkDge3WFqHCojORHI2Qt8Ig2ArzHiAOpp2QqeVZtOHFVXwdtsioEHK1MG-jiSrLr1ZK4fIKZTM3wE3Veb97s9oRZGZGOFfWaszlTXqQ7iNO5QvS4S886E9mdXj_aPXBeQrMM8a8uMfCVS1SjvN95fGZC1AtKmnrf3GxianHFCwKQmSxB3_hXlCQfxvE4vonW7Y5GlcWt9sydBKiTqs0Y3rMG_puY_oNMla7dlrASEw0EHTrKtS77mNpV0QzhFMOZA8DuDxdu0FWa-COaAzSTao_IhUnHzbuwvn3n8JdR4kPf9T0IMj0iFovNZGhHxIByqKXNgbiK1AQQcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
Fable 5
اکنون به صورت رایگان روی کامپیوتر شما در دسترس است.
توسعه‌دهندگان نسخه ویژه Gemma 4 Composer 2.5 را منتشر کردند که با داده‌های استدلال دقیق آموزش دیده است.
🔹
تمرکز اصلی بر کدنویسی، تحلیل و درخواست‌های پیچیده است.
🔹
کاملاً به صورت محلی و بدون نیاز به اشتراک یا API کار می‌کند.
🔹
در قالب GGUF برای Ollama، LM Studio، llama.cpp و سایر ابزارهای محبوب در دسترس است.
دانلود این شاهکار
#Fable
#Ai
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🛢
نفت خام:
81.5$
|
دلار: 159,050 تومان
🕰
بروزرسانی - 26 خرداد 1405 - 03:04
🪙
قیمت لحظه ای رمز ارزهای پرمخاطب:
🟢
BTC:
$66,152.52
(+1.00%)
🟢
ETH:
$1,786.95
(+3.76%)
🟢
BNB:
$615.87
(+0.07%)
🟢
XRP:
$1.24
(+4.98%)
🟢
SOL:
$73.79
(+4.37%)
🔴
TRX:
$0.32
(-0.41%)
🔴
DOGE:
$0.09
(-0.86%)
🔴
ADA:
$0.18
(-0.05%)
🟢
PAXG (Gold):
$4,304.90
(+0.65%)
🚮
قیمت ارزهای تلگرامی:
🔴
TON:
$1.71
(-2.06%)
🔴
NOT:
$0.000448
(-7.03%)
🔴
DOGS:
$0.000044
(-1.64%)
🔴
HMSTR:
$0.000158
(-6.08%)
🟢
EVAA:
$1.258452
(+88.39%)
🟢
X:
$0.000012
(+3.86%)
🟢
MAJOR:
$0.035791
(+2.66%)
🔴
PX:
$0.017240
(-0.23%)
🔴
STON:
$0.578778
(-0.88%)
🟢
REDO:
$0.077989
(+10.89%)
🔴
UTYA:
$0.019192
(-7.00%)
🔴
DUST:
$0.000175
(-2.63%)
🟢
TONNEL:
$0.627903
(+4.80%)
🟢
FISH:
$0.005469
(+1.74%)
🟡
قیمت طلا و نقره:
🌍
انس طلا (دلار):
4,335.20$
🌍
انس نقره (دلار):
70.01$
💰
طلا ۱۸ عیار (هر گرم):
16,296,900
تومان
💰
طلا ۲۴ عیار (هر گرم):
21,729,000
تومان
🥇
سکه گرمی:
25,500,000
تومان
🥇
ربع سکه:
47,620,000
تومان
🥇
نیم سکه:
85,960,000
تومان
🥇
سکه بهار آزادی:
163,625,000
تومان
🥇
سکه امامی:
167,010,000
تومان
🥈
گرم نقره ۹۹۹:
377,140
تومان
🛢
قیمت نفت:
🇺🇸
نفت WTI (تگزاس):
81.5$
(+1%)
🇬🇧
نفت Brent (برنت):
83.7$
(+0%)
#دلار
#طلا
#نفت
🫀
نبض بازار در دستان شماست...
‌</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAssa</strong></div>
<div class="tg-text">بچه ها شرمنده یه خبر باید بدم بهتون
من تحقیقاتم از سایت render بر اساس هوش مصنوعی بود الان شخصا سایت و قوانین رو چک کردم
مثل اینکه bandwidth رو ۵ گیگ میده اما پروژه اولی خودم تا ۲۵ گیگ مصرف بعد ساسپند کرد البته این هم بگم من کانفیگ پخش کرده بودم و تقریبا سه روزه داره دست به دست می‌چرخه با کاربر بالا
الان هم کد بهینه تر شده کمتر گیره
خلاصه که شرمنده بازم درباره اطلاعات من احمق برای اطمینان هم از جمنای هم از Claude هم پرسیدم
😑
💔
البته اگر قبلاً ورسل زده باشین میدونین که اون سقف زیاد مهم نیست و اگر شخصی مصرف کنید و ترافیک عجیب رد ندین کم کم برای شما تا ۴۰ گیگ میره بعد ساسپند می‌کنه
ورسل به اون بزرگی با هابیش ۳۰۰ گیگ رد دادم حالا این رندر که چیزی نیس
😂
بگم که ریلوی سقفش همون ۷۰ گیگه
و اینکه اگر ساسپند شدین فوقش با ایمیل فیک ثبت نام کنید و یکی دیگه بسازید بیشتر از ۵ دقیقه کار نداره
بازم عذر میخوام باید شخصا تحقیق میکردم</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFbU5kwF3wEOSvQDYxwg4CWZLeJW9QetjhE5pZDs7QhYP5RDq6Rn8IYQfaP1FciWc2Kd5hdpeJhaabEVHMw3Y00l-cCf38P5W-ehlU8WKrbfINedA-QRVOA6bXD2a7THCQNgx34W_JMuRsCGVmkJ9OzDKqh4kO6QivBgy701gKd5ZPt1shRouKKXuU0oZFD7SRPUYnGCa6x4TSiJVtbWsr4Wp8Y-8Aj3nIC309tcxGupuUYVT6cLBIp_w4T7wTSRD-1rrh_erougXUOwyXxYgnVyG09T2ROJTYy5E6HHOyUSjgxUBQ_hy9NZTe-05PUkT_9FXYaJsR5l0eDcUwEF0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087fb590da.mp4?token=T-_1BWWwzqv0YurYvnFtmRpJlilKza9LeTsvX6MppZQjUn1uYgzhVlJ3mU7szEMyuxI4VgUdgxjNYr5YzRn6hBBz22I-VSEofG0fwWctWZ3T0o2hY7tP3kkpl-AzZbIHP4r0NBD9HlvaRJJNSPLw1ObhY2yfwYiiMeG8KnGeGTKJ14ltQqpwwgDGnYz8E2HMuuoK8s24AeeotmeK58ECl8kClqp2PG5JQgixIRiBdAhGCcv95gFWHwAW84iI_MNuiw-w5vdCBbxrruKa5IFz_F4dTFeDZOomZSXjo75Krb3Mn1oF0v_HzBvD-lxncBkbD69LHbqkgjth82UIEe2euw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087fb590da.mp4?token=T-_1BWWwzqv0YurYvnFtmRpJlilKza9LeTsvX6MppZQjUn1uYgzhVlJ3mU7szEMyuxI4VgUdgxjNYr5YzRn6hBBz22I-VSEofG0fwWctWZ3T0o2hY7tP3kkpl-AzZbIHP4r0NBD9HlvaRJJNSPLw1ObhY2yfwYiiMeG8KnGeGTKJ14ltQqpwwgDGnYz8E2HMuuoK8s24AeeotmeK58ECl8kClqp2PG5JQgixIRiBdAhGCcv95gFWHwAW84iI_MNuiw-w5vdCBbxrruKa5IFz_F4dTFeDZOomZSXjo75Krb3Mn1oF0v_HzBvD-lxncBkbD69LHbqkgjth82UIEe2euw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
یک پروژه متن‌باز جذاب برای ساخت ارائه با کمک هوش مصنوعی!
دیگه لازم نیست ساعت‌ها برای ساخت اسلاید وقت بذارید؛ این ابزار رو می‌تونید روی سیستم خودتون اجرا کنید و با هر مدل هوش مصنوعی دلخواه، پرزنت حرفه‌ای بسازید.
✨
ویژگی‌ها:
🔹
پشتیبانی از OpenAI، Gemini، Claude، Ollama و مدل‌های دیگه
🔹
ساخت ارائه از روی متن، فایل و اسناد
🔹
قالب‌ها و تم‌های قابل شخصی‌سازی
🔹
اجرای کامل روی سیستم شخصی
🔹
رایگان و متن‌باز
🎓
مناسب دانشجوها، مدرس‌ها، پژوهشگرها و هر کسی که زیاد ارائه می‌سازه.
🔗
Github
#OpenSource
#AI
#Presentation
#Productivity
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🌍
افزونه Local Translator
؛
افزونه‌ای متن‌باز برای ترجمه صفحات وب بدون ارسال داده‌ها به سرورهای خارجی.
💡
اگر دنبال جایگزینی سبک و خصوصی برای مترجم‌های آنلاین هستید، ارزش امتحان کردن را دارد.
🔹
ترجمه کامل صفحات یا بخش‌های انتخابی متن
🔹
استفاده از Translation API داخلی Chrome
🔹
حفظ حریم خصوصی؛ پردازش روی دستگاه کاربر
🔹
دو حالت نمایش: جایگزینی متن یا نمایش ترجمه زیر متن اصلی
🔹
ذخیره خودکار تنظیمات و فعال‌سازی خودکار
📎
GitHub
#Chrome
#Translation
#Privacy
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCcxt5hLVEDWB9wqtRSS6KGt3d68N1ufWLJT4dJmyV0ZGbqFKI1nzTvRraNpYvTWgiq_vyAc0bikaUvUSAhWj5hJWtIO-lwkRn1o3UBE759T2BYP7AwR7TnUkxLjARmf9-n89ASVPIr-jNouYu0deH-T3oZ85RdmGaE80lNKUJylGvla3xsX8uEniBg4f9FxN0A345JrEr9Mp-_7ih4MqEXnJXKXJ9qYqNAMoVVLGfKnpg6ZKxJiVIAz3TmH4tJf024EyDAtMV2Il20Wg9elSddkd4PkCKyRebJfzfxqoMQUEaE7kDpyCox0AcfdMUxHHGpRGMtrIjP0wReW7rYxHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با افزونه SkipBait میتونید ویدیوهای یوتیوب رو سریع خلاصه کنید و دقیق‌تر داخل محتوا بگردید
🎬
✨
قابلیت‌ها:
•
🔹
خلاصه‌سازی سریع ویدیوهای YouTube
•
⚡
جستجو داخل زیرنویس‌ها و متن ویدیو
•
🤖
پرسش‌وپاسخ با هوش مصنوعی درباره محتوای ویدیو
•
🌐
پشتیبانی از جستجوی وب برای اطلاعات تکمیلی
🔗
لینک
#AI
#ChromeExtension
#YouTube
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
گزارش‌های تازه از پیش‌نویس توافق آمریکا و ایران
🇺🇸
طبق گزارش Reuters، پیش‌نویس یک تفاهم‌نامه موقت میان آمریکا و ایران روی چند محور اصلی می‌چرخد: توقف درگیری‌ها، بازگشایی تنگه هرمز، کاهش فشارهای نفتی و آزادسازی بخشی از دارایی‌های مسدودشده ایران. همچنین قرار است درباره پرونده هسته‌ای یک بازه ۶۰ روزه برای مذاکره باز شود.
📌
با این حال، Reuters تأکید کرده که این توافق هنوز نهایی نشده و بعضی جزئیات، از جمله رقم دارایی‌های آزادشده و شکل دقیق رفع تحریم‌ها، در گزارش‌های مختلف متفاوت آمده است.
⚠️
فعلاً باید این خبر را در حد پیش‌نویس و گزارش رسانه‌ای دید، نه توافق قطعی.
#Iran
#US
#MiddleEast
#Reuters
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
احتمال بازگشت Claude Fable 5؟
بر اساس گزارش برخی رسانه‌ها، کمپانی Anthropic تیمی از کارشناسان خود را برای مذاکره با مقامات آمریکایی به واشنگتن فرستاده تا محدودیت‌های اعمال‌شده روی مدل Claude Fable 5 را کاهش دهد.
📌
گفته می‌شود این محدودیت‌ها پس از نگرانی‌های امنیتی و گزارش‌هایی درباره روش‌های Jailbreak و دور زدن مکانیزم‌های حفاظتی مدل اعمال شده‌اند. برخی منابع نیز مدعی‌اند که امکان عبور از بخشی از محدودیت‌های امنیتی Claude Fable 5، یکی از دلایل اصلی این تصمیم بوده است.
🔹
هنوز هیچ جدول زمانی رسمی برای رفع محدودیت‌ها منتشر نشده است.
🔹
در صورت توافق، احتمال دارد مدل با لایه‌های امنیتی و محدودیت‌های بیشتری دوباره در دسترس قرار بگیرد.
🔹
کمپانی Anthropic تاکنون جزئیات کاملی درباره آینده این مدل منتشر نکرده است.
⚠️
فعلاً تمام این موارد در حد گزارش‌های رسانه‌ای است و باید منتظر اطلاعیه‌های رسمی از سوی Anthropic و نهادهای آمریکایی ماند.
#Anthropic
#Claude
#AI
#LLM
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o-EnQ3gPejQF0v0YzuJaNucoIy5oeLkfNknLsHKzaBcEtiKVbJVZFmD6kkXzQxpHrgBkQpF7lC_1zbn0JlIDHljRUVSuHobjXdT9ulD1GK9VPCx5bPDfG6NtNnmt_64gO-aDpH7x7CYUiFIK0LorksXe0INRF8PDiRT_igQSIFs4h-mhGf9jHaACK2Q9owZnLD4Y3lr2dqL3dik5wtp8T85M2D3v30dwjg4rCg7sQxUK9eb_4b38zwmwMWr8vNQaqO15k4xLboZ_5ht0GqO2hZCZO5Z-23OVVbmc7UZmqdKvZ7QNOanzjXpeW74nz4d0rBjvq1dDobCA1a0OklSrwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت Ponytail هوش مصنوعی را از نوشتن کدهای طولانی نجات می‌دهد
☠
این مهارت عامل‌های هوش مصنوعی را از نوشتن کدهای طولانی و بی‌فایده نجات می‌دهد و به جای ۵۰۰ خط کد، عامل می‌تواند فقط ۵ خط بنویسد.
با Cursor، Windsurf، Cline، Copilot، Antigravity، OpenCode و Claude Code کار می‌کند.
https://github.com/DietrichGebert/ponytail
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: آلمان
🧭
شرط: حداقل 1 دعوت
👥
دریافت‌کنندگان: 21/30
💾
حجم: مخزن
⏰
اعتبار: مخزن
🟢
فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
آلمان
🧭
شرط: حداقل 1 دعوت
👥
دریافت‌کنندگان: 21/30
💾
حجم: مخزن
⏰
اعتبار: مخزن
🟢
فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5BuGmSFP8pBC5QSmZp9AzZ-5SHpke430AEz819tNe2ycFbwwNsW4Q-CPbctydRvdZuVu6QnTOzfMwaUGs0ig7riRIev4uIzfSwoGc1enXaeoiC7krKtUQE8jDNTe_d6engCfAOVx0Aw3HhWvTjj1d_MntecUSQa-J61kAdr-4i26kv4qKKm7Mi3psAARMM9jvB2ohM8K8h57BFa6CqH6-4ngDFSM7K9IvoSQaFID2EK1b6P192YlBaVz_MvzKzEHxyCNlnkj8-iU9eEg_4wG0At0Q1lA0YO1DI-pC6q-rmpWC1k5GW9D7ZRisSjpSV6O6tZpWvOkCLHcE83abPYKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل جدید
GLM 5.2
از چین معرفی شد
توسعه‌دهندگان چینی نسخه جدید GLM 5.2 را منتشر کرده‌اند؛ مدلی که به‌گفته برخی بنچمارک‌ها عملکرد بسیار قدرتمندی در استدلال و کدنویسی دارد و توجه جامعه AI را جلب کرده است.
✨
نکات مهم:
🔹
عملکرد رقابتی در تست‌های Reasoning و Agent
🔹
هزینه API بسیار پایین‌تر نسبت به برخی مدل‌های مطرح بازار
🔹
مناسب برای کدنویسی، اتوماسیون و وظایف طولانی‌مدت
🔹
دسترسی رایگان از طریق محیط توسعه Zcode
﻿
📊
برخی گزارش‌ها نشان می‌دهند GLM 5.2 در چند بنچمارک حتی از بعضی مدل‌های پرچمدار فعلی نیز عملکرد بهتری داشته، هرچند نتایج واقعی بسته به نوع استفاده متفاوت خواهد بود.
🇨🇳
رقابت بین مدل‌های چینی و شرکت‌هایی مانند OpenAI و Anthropic هر روز جدی‌تر می‌شود و GLM 5.2 یکی از جدیدترین نمونه‌های این رقابت است.
🔗
ورود
#AI
#GLM52
#LLM
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
متوقف شد
❌
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚀
ساخت VPN شخصی (VLESS) کاملاً رایگان و بدون نیاز به سرور (VPS)!
اگر دنبال راهی هستید که بدون پرداخت هزینه‌های سنگین برای خرید سرور مجازی (VPS)، یک کانفیگ VLESS اختصاصی با پنل مدیریت حرفه‌ای داشته باشید، پروژه
REN Gateway
دقیقاً همان چیزی است که نیاز دارید.
این اسکریپت که توسط یکی از توسعه‌دهندگان چنل(AssA7778) نوشته شده، به شما اجازه می‌دهد پنل و تونل خود را مستقیماً روی هاست‌های رایگان
Render
راه‌اندازی کنید.
📌
ویژگی‌های جذاب این پروژه:
کاملاً رایگان:
نیازی به خرید سرور یا دامنه ندارید.
پنل مدیریت حرفه‌ای:
دارای داشبورد برای مشاهده مصرف، ساخت لینک‌های VLESS متعدد و تعیین حجم مصرفی (مثلاً ۱ گیگابایت برای هر کاربر).
ضد خاموشی:
دارای سیستم Keep-alive داخلی که هر ۱۰ دقیقه پینگ می‌فرستد تا سرور رایگان شما در رندر خاموش نشود.
پشتیبانی کامل از V2rayNG و NekoBox.
رابط کاربری دو زبانه (فارسی/انگلیسی) و حالت تاریک/روشن.
🛠
آموزش سریع راه‌اندازی در ۵ دقیقه:
۱. وارد لینک گیت‌هاب پروژه (در انتهای پست) شوید و روی دکمه
Fork
کلیک کنید تا پروژه به اکانت گیت‌هاب خودتان منتقل شود.
۲. وارد سایت
Render.com
شوید و با اکانت گیت‌هاب خود لاگین کنید.
۳. از داشبورد رندر، روی
New
و سپس
Web Service
کلیک کنید و مخزنی که فورک کردید را انتخاب کنید.
۴. در صفحه تنظیمات این موارد را وارد کنید:
Region:
حتماً روی
Frankfurt (Germany)
تنظیم کنید تا پینگ بهتری بگیرید.
Build Command:
pip install -r requirements.txt
Start Command:
python main.py
۵. روی
Deploy
کلیک کنید و ۲ تا ۳ دقیقه صبر کنید تا آدرس پنل به شما داده شود (مثلاً
your-app.onrender.com
).
🔐
اطلاعات ورود به پنل:
آدرس ورود:
your-app.onrender.com/login
رمز عبور پیش‌فرض:
admin
(حتماً بعد از ورود از بخش Security تغییرش بدید).
حالا به راحتی روی گزینه Add کلیک کنید، حجم تعیین کنید و لینک VLESS اختصاصی خودتان را کپی کنید!
📥
لینک پروژه در گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎁
دریافت اعتبار رایگان API برای مدل‌های هوش مصنوعی
سرویس AeroLink در حال ارائه اعتبار رایگان API برای استفاده از مدل‌های مختلف از جمله Claude، GPT و سایر مدل‌هاست.
💰
اعتبار اولیه:
🔹
ثبت‌نام عادی: 35 دلار
🔹
از طریق لینک دعوت: تا 50 دلار اعتبار
⚡
محدودیت استفاده:
🔸
حداکثر 10 دلار مصرف هر 5 ساعت
🔸
حداکثر 70 دلار مصرف در هفته
📌
مراحل:
1️⃣
ثبت‌نام در سرویس
2️⃣
ورود به پنل و ساخت API Key از بخش
New API Key
3️⃣
شروع استفاده از مدل‌ها
🤖
لیست مدل‌های پشتیبانی‌شده
🌐
ثبت‌نام
⚠️
قبل از استفاده، شرایط سرویس و تاریخ انقضای اعتبار را بررسی کنید.
#API
#Claude
#GPT
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuc5jVtXozVDrSJOE11eGvBHWN5Yqf3lscWlh-HeIZ-GHKeosDZ67RSv2XE53GkIPCKpJw8q4Yj_cGFMOOuNoAXQ0-0x2HJg17_c-iBNy5o6Ote2KNeaFoXeqBftAk5mpUqSgROjmUTEGHS9X81dDGB98AtWex1W50uea5SupsfLiU8FV18H_OoEBqW__DvpcUY5Z3EWA334tSwZFtJ1U42Ur5306GUAyezxF-k3kNFrGFS9QlU820-d0VEO5CXWsJspd4lblvJTF2gCkmI8NBNxeO2YV9_MszJ1VclpZtXtzgnFuvtUxS9-2rqLr839_8OTTzWG68BruvzCS-LwZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
OpenRouter قابلیت جدید
Model Fusion
را معرفی کرد
حالا به‌جای تکیه بر یک مدل، چند مدل هوش مصنوعی به‌صورت همزمان روی یک درخواست کار می‌کنند و در نهایت بهترین بخش‌های پاسخ آن‌ها با هم ترکیب می‌شود.
🤖
برای مثال می‌توان GPT-5.5 و Claude Opus را به‌صورت موازی روی یک سؤال اجرا کرد و یک پاسخ نهایی و بهینه دریافت کرد.
✨
نتیجه؟
🔹
پاسخ‌های دقیق‌تر
🔹
تحلیل‌های عمیق‌تر
🔹
عملکرد بهتر در برنامه‌نویسی و مسائل پیچیده
در واقع Model Fusion شبیه یک «اتاق فکر از چند هوش مصنوعی» است که روی یک مسئله همکاری می‌کنند.
🔗
قابل آزمایش در OpenRouter
#AI
#OpenRouter
#LLM
#GPT
#Claude
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
100GB
🧭
شرط: حداقل 1 دعوت
👥
دریافت‌کنندگان: 43/64
💾
حجم: مخزن
⏰
اعتبار: مخزن
🟢
فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfSz8zgZM3wqwMqW_ts9wMv0c2iW7mSnywm2WD0wk0DYIqllQ7rwzpIPBXQfmN-_7lzDGiC5al233F7esuUXtvPbJ52rQ8gpCvVHfgQJ7OLr8nBHMJZv4DJyAZ26XB009bwoDhgAcsWE_veg-jLgClhCkcy7dVvpLJIiHgRzvaTNOE6RIEuOf4_8cHdb3UH3tj648AMCFTjXV1cyiIc4l4QCjAn_O_SuVfgQ4YV8DV6ILIsMWtwQ0KSbroEn_uF8kEhWH4XbBmQba_NeMMjajD7dxSiLcazHZFUi9eJ2J2Iitof_7xvzOumGYsnDCU45qahUd8XPmSIkevrWr3tNMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smPY-e6e1_zMdTO74DdzZ5uCTt2NSimZIem9IlVSkDQRx47CCzLgscNSBtEEa_XPU-kCfygdfXkaifWZqSs2YgohJ0CoX2BREKp4uLl_AE_VlMeIwG4IpIq7tcJOnPP7_224vXiEiikVWY9H_PxY1jdkN5thcxKq42o1nU0SYI2UuoZbspFDxNLszLASvMKyeuYAGqewGCTQPWqEnPXU07_9c5cDXqIMYc7A5qSCivRQzhLxCLvFG_KkPMGXp-4BMOy_GpC1oepw-P6w8rOgZlMCjl8G7lZLQ31-eF5kyLfOb-cKCTuWfRTOdSIjc1ftZdAvOdXDLhas3vrxc6otQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه که هوش مصنوعی هم جلوش کم بیاره!
📖
متن چالش:
"Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off—then, I account it high time to get to sea as soon as I can."
🎁
جایزه ویژه:
۱۰۰ گیگ کانفیگ اختصاصی با آی‌پی ثابت آمریکا
🇺🇸
برای کسی که ترجمه‌اش یک سر و گردن از ترجمه ماشینی (AI) بالاتر باشه!
*(نکته: اگر تعداد ترجمه‌های شاهکار و برنده‌ها زیاد باشه، جایزه رو به قید قرعه به یکی از بهترین‌ها تقدیم می‌کنیم).*
⏳
مهلت ارسال:
فقط تا ساعت
۲:۴۰
فرصت دارید.
👇
نحوه شرکت:
معطل نکنید و ترجمه‌هاتون رو همین الان
زیر همین پست کامنت کنید.
ببینیم چه می‌کنید!
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKoMOdFJRwBe-Y_2nSW5zXpatezYXou5OQMkmxOkadBMVsvepGo5CK14Ke9Jo6wy-Ncb45eaBim0pnsIDzs72eXhi9AoPGad1JCYkJoP5JBYlPSu6iFmBhUTCFnIymrHnv6hsNP9KvlXPQdbdbq-iQqwi8fuK3v6ucncI6GoEd4GREA7bssg7fSPch3FakZ96CpkYX4CCz8ZbWF1rrB41nOA1kG-pAvqlMIMC6H-354EX0hvgQPLhZsQuEc67rwUmUdSCcnRYWmpixyKawyxmfEoYDWcaO-iDyW72WvcQp-jWX492YVUapTfApF_4tlrUzV5kHxfU2qMMfR6MZtCbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1sZmRTn_ab08A8Oe1_OWYpWRarxvQH5oHYPbw0GGqNd-9E9RD-54gym5nUDH1iO7LujiTp2H-kZmXwjOOwOwyVvzh9YW2nxgyfWXySOkSf3C2Tn-0kj3iIJnG1itmm7xRLev8_mdZtadMIk0fDWgQVrTD5Sr2dQlqecmyGn0PtVMf7bfe_QX4bxWEIoqPnV-QR3cM9GkIWYNgtkxo4z_pZxLBqxs8O1UfLihF5Nnrr6M6OHuGhHwwYRThvjMb1SVXJxnAv3aO-7dO6n21VAlz_SJYg6RtrfDpSSdQn31t7KidObe72RusBWAQGcdI4hwMoZkfwOqL0g5-qVu173tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن»
یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like it was never there. Match the background, lighting, shadows, and colors. Keep everything else the same.
#Chatgpt
#Gemini
#PromptEngineering
#PhotoEditing
#AITools
#Design
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auwOUmsYRF8_tG1YMw3VPn4MPY97rtjhB1Kik6-1e26zfRPtf6udiGjpmFic-yz3pqB6Tdxy78tlRRN2M3lCiKIoL583RrFcwAKSJfpoyL6Mldvbmv9Gcu0pfZmtdN4rMAZC4x-Ojkhg2tUJRqhqSy3cqSvTvOq5o4RN8-Cg95kaQ2IdzW-m77zYnDr_wNU4NFWkmtoQmiqVZ-kD_5uKZQIuoAl5MFahYgEkeNyzUbrE5x7CIrUNhvNaGcVwk7C1_zE9vYxeXEO40F6vxBGVlcrHEvOPaUNqXMyG8aGyxLiqtU5ZguUMo2Qwmo7jtFABFVZrN1HBEg2g1E6SHkdUdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnNqaX8MonC4B50NygUajNlE63-n2r9tyAhws_6CVzxZETdi9kkqQ9plgKVIbjo0pApbgD8Rkp0dOEamZEndy5uWGe5CGrddYd-hU5XRlBB6mHyGfxnevOAOLg_KG624fkzIZa645eDw6MTgjmHp81RUC3ys7rBxQ6RrKhx0U07mmuEOF-ErVEipRG4NVNfaTjCz5WbAjMUkVhfuoa_GRrHUfYQOnOMBfqQ22XgWiKpAx3_tZglNAhAP6qplTfw0e7bg2cfDS-EBRAkxFKJR8uNIlPi00E4eyeh81n6mlUoBLeVkNsKHDQl0E7c3cqQZZtNCOPTBr1juBJp1z5ujNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
روزانه 6 گیگ کانفیگ رایگان
🟠
پنل BPB کلودفلر
🔹
با جیمیل لاگین کنید
https://dash.cloudflare.com
💻
در ویندوز نرم افزار BPB Wizard رو دانلود و باز کنید
https://github.com/bia-pain-bache/BPB-Wizard/releases/latest/download/BPB-Wizard-windows-amd64.zip
🔹
عدد 1 رو تایپ کنید و اینتر بزنید (اجازه لاگین در کلود بهش بدید)
🔸
لاگین که شد بیاید تو پنجره برنامه گزینه 1 رو بزنید و ورکر بسازید
🔹
تمام سوالات رو بدون تغییر اینتر بزنید و آخرش y رو تایپ کنید
🔸
پنل که باز شد رمز دلخواه ثبت کنید و لاگین کنید
🔺
تنظیمات پنل
Common
:
ipv6 رو خاموش کنید
VLESS - Trojan:
- در بخش
⚙️
Protocols تیک گزینه Trojan رو حذف کنید
- در بخش
🔓
non-TLS Ports تیک عدد 80 رو بزنید
✅
بیاید پایین و گزینه Apply رو بزنید
🌐
دریافت کانفیگ ها در بخش Subscriptions :
- گزینه Raw (without settings) رو بزنید و دکمه کپی رو بزنید
- لینک ساب رو در v2ray وارد کنید (میتونید لینک رو باز کنید در مرورگر و کانفیگ هارو کپی کنید)
🔵
@ArchiveTell
|
#Mz</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_N-U6KBNpUPK_4iPOeOQjnU5hcGpS2Oq7BFuxmKhUT-1kVvUZh4hz2SDLC0bMFMZpYyXlAcOXRmR18EvFxgI3mgSnsXR9Yluvm4bhjHLHmc5tVG7q2pcdbq_wi3AT9dm8Wy3NVPa8HNVg79jXNb3ghchHEm5xF3bBAOJM-XuoEPz-twAMyHfB4vIyFvvaQgkpw_en8gUgwEkMSv9rYyuweBH0ER7c7dLw9YETJMFwAC5GvxLV5nZ9RE-r2PdpzzQWW1TGm_Pbm4MQbEIm4G0JbnZ3p8Qz9odjdxW5-ABYtEa9rf_-mByNgZv03DjbRnzo7e_6-thXlLBjxLy5Zw5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😬
کاربران Gemini از محدودیت‌های جدید گوگل شاکی‌اند!
ظاهراً گوگل بی‌سروصدا سیستم سهمیه Gemini رو تغییر داده و حالا حتی بعضی درخواست‌های متنی ساده هم بخش بزرگی از سهمیه روزانه رو مصرف می‌کنن.
😶
🎥
بعضی کاربران می‌گن ساخت یک ویدئو می‌تونه کل سهمیه روز رو با یک پرامپت تموم کنه!
👀
«جاش وودوارد» مدیر محصول Gemini بعد از موج انتقادها گفته تیمش در حال بررسی ماجراست و احتمالاً تغییراتی اعمال می‌شه.
📌
اگر این چند روز حس کردید سهمیه Gemini زودتر از همیشه تموم می‌شه، احتمالاً تنها نیستید!
#Gemini
#Google
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=N3v-4vubT7AKAvpOIb1c2ohW824jRgywU0vVabNIvi3cPNaC0nwBVjG3SeHeUzZ95p1IPC8VqQiR5gn03A0stiSnzD60V7TNW9UZUQ1L1Tz9NLq4xcCjCwsEXJvEYhndoKMiZtHFa80bmUM_F6EQLkV3wA70ZZtAqrnOVRFVIqB4gK1QZ5v6dloizY90OdRNalwx4dwcg8qdsPPpd6zfP7BszXjJe4rfF5zPY2IeMGwJ2vt3Veomb3uQp4T-VRXxGsI7YF0vxEi-KejUWWgCxTMYaEAq0ScYG0PUaX-rK8mHKjIOO-biPZELF2QGgCXOTZdHatdXJWBo0g09WV6MRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=N3v-4vubT7AKAvpOIb1c2ohW824jRgywU0vVabNIvi3cPNaC0nwBVjG3SeHeUzZ95p1IPC8VqQiR5gn03A0stiSnzD60V7TNW9UZUQ1L1Tz9NLq4xcCjCwsEXJvEYhndoKMiZtHFa80bmUM_F6EQLkV3wA70ZZtAqrnOVRFVIqB4gK1QZ5v6dloizY90OdRNalwx4dwcg8qdsPPpd6zfP7BszXjJe4rfF5zPY2IeMGwJ2vt3Veomb3uQp4T-VRXxGsI7YF0vxEi-KejUWWgCxTMYaEAq0ScYG0PUaX-rK8mHKjIOO-biPZELF2QGgCXOTZdHatdXJWBo0g09WV6MRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">WhatLetterAI
تصویر را به متن تبدیل می‌کند و به هر زبانی که بخواهید پاسخ می‌دهد!
📸
🤖
✨
قابلیت‌ها:
•
🔹
تشخیص متن از بیش از ۱۰۰ زبان
•
⚡
استخراج متن از تصویر و پاسخ‌گویی هوشمند به سؤالات محتوا
•
🛠️
دریافت خروجی به زبان فارسی یا زبانی که انتخاب کنید
•
📦
پلن رایگان با محدودیت ماهانه برای ترجمه و پردازش متن
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGNoLe1G33YJD4smJjCN_1nlnqQjkvOrcsWZS0_YdmfrUXs5M35HmYqrclYxIod-JC9uBfCSVMWNtrS9I6F1vjWIxAZB6LbcjwE6JsYojmEhCbd0NM1Iu4z_wCUVeAWMRJ_-vJApos9XkPto8Ky-AAaDJaX8zaPtuQUd0xG-2gwEAaqUHHTFhaN49xxStcyzLSGFj95LASEcw5ZhV2KBKrVI4Bjlm7Km3MSb-Edhg8HGSLlLS0QElAYYwhyLJxV9jjKHHR1nR9mnCwwEpTFfhvJfdc2NnMXjdi9RRfsrwqtbOJt8ivOBCPkihTQbPfVELywWr6q8W9rTylrxYi9p5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تولید رایگان تصویر هوش مصنوعی
🔹
بدون نیاز به ورود
🔹
خروجی سریع و بدون واترمارک
✨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKN3qGci7ZwbTPA8xBEH6f2bfJsX_5kcveO-CQ754CkyX4UiU-SQ7SogTmS9l9d-pMcUwHgRQeUpftRLEhVAywBiTSr5azM07wPcULK1rjzQJVZUc-GPsKwUa75wTfZDswodeSiGIAncHpzQ1_g38SZ3LiDxemh4ELKYcwqeK2QscFRyogGkbzfNeBIGUFOHTkWbsjAo9JVGsNZ6HJRVmNjXPwRpqdKPx51mE504nLIH595u7WcZ81e3pv9_Fb-A6sn-FlxkGq3d9nO_vDaNBzzMtUCevHZzhWKh-82fny4cKkoFHiAlNBUNaLVkbnjuQZ6E1NeXu64HPrefh6tbYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=bf-fLL36d5AJZykcy7_2qTkqn5EZ4rIxpbdDB6E_aZD2nsfBmmXdE6QzWuMvdk1HpJsNAOx2G6pzeZPUkNTvB1lnj_c7a4mGOUdXY86v-huahMxl9K5D6BLdo4xyQ9RBalvjztEOno7jpQX4enctMQuyGf0sJZKu6nQmKEwGXDpXgj-JPhPWFq6TcJLKPNR6RWXLHhxioW0B3lVE_Sl9H8iHXKOZuEnYwG_ax6SVNV5ip9qTnTUy_alIzTWFHmkkBVHG2CPR2XacgoNBNoRPIhcToNpa4P5b9iqgBGOFpTUnpw6s8L4v7_uzW8QOEjQZXTxsoZei45vViOppvXi1gmWDllgT46qQfcCnWS5U3hNIZNqRpIfC30ZKbP1fFqjq0TmhSHNT_K5lUwXn5hjsO3C8-MDIh-USvIp6FWhUnn40foanoa1BGa4j2PCP_FNhnjtji5HlSiONDo2x_p1G7GelIVRZQeCKvjI2_PklBnDS0VnaNQbS1DlwoLiByahKlZQ4V6gfqZupnrJYzHEg261hCSJ6Ru3QzAzQNWIOCmdkaBkLLMQSiaip4Bkcg3OIKfF0dIjDqN69n_s_H-RBYveMb7roJ6NYLUqRWc1aJf_SXtd5P2F6V33hXXy-sCw6Y2aDNIi4Ue7JtQREm3ONkAlJZzf4znmDFxTqOay6QoU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=bf-fLL36d5AJZykcy7_2qTkqn5EZ4rIxpbdDB6E_aZD2nsfBmmXdE6QzWuMvdk1HpJsNAOx2G6pzeZPUkNTvB1lnj_c7a4mGOUdXY86v-huahMxl9K5D6BLdo4xyQ9RBalvjztEOno7jpQX4enctMQuyGf0sJZKu6nQmKEwGXDpXgj-JPhPWFq6TcJLKPNR6RWXLHhxioW0B3lVE_Sl9H8iHXKOZuEnYwG_ax6SVNV5ip9qTnTUy_alIzTWFHmkkBVHG2CPR2XacgoNBNoRPIhcToNpa4P5b9iqgBGOFpTUnpw6s8L4v7_uzW8QOEjQZXTxsoZei45vViOppvXi1gmWDllgT46qQfcCnWS5U3hNIZNqRpIfC30ZKbP1fFqjq0TmhSHNT_K5lUwXn5hjsO3C8-MDIh-USvIp6FWhUnn40foanoa1BGa4j2PCP_FNhnjtji5HlSiONDo2x_p1G7GelIVRZQeCKvjI2_PklBnDS0VnaNQbS1DlwoLiByahKlZQ4V6gfqZupnrJYzHEg261hCSJ6Ru3QzAzQNWIOCmdkaBkLLMQSiaip4Bkcg3OIKfF0dIjDqN69n_s_H-RBYveMb7roJ6NYLUqRWc1aJf_SXtd5P2F6V33hXXy-sCw6Y2aDNIi4Ue7JtQREm3ONkAlJZzf4znmDFxTqOay6QoU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎵
LoFi‑Engine
ساخت رایگان موسیقی LoFi برای خلق فضای کاری دلپذیر!
✨
قابلیت‌ها:
•
🔹
تولید محلی قطعات منحصر به‌فرد LoFi
•
⚡️
صداهای طبیعت (باران، باد، دریا، پرندگان)
•
🛠
تنظیم تصویر و طراحی فضای کاری به دلخواه
•
⌨️
پشتیبانی از کلیدهای میانبر برای کنترل سریع
•
📦
کارکرد آفلاین، بدون نیاز به فضای ابری یا اشتراک
•
💻
اوپن سورس، سازگار با ویندوز، لینوکس و macOS
🔗
لینک
#OpenSource
#AI
#Music
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=szftXJ00Xo4vHgk6d9r33dVtP7YqN4T_09-bDOeL26vzBhmONomlCcDyqE4Tl3XmDB1Hle42UAewB36KCfA87H_HH5lAOfYtwpeO-r6hYg_lRLt4zobopHWBZ2HlZY1GuqUyxyO7OhjtkmDNpVpyZcqN_oSz3NyGRW992cSQOD0LBWTAt8wFeOlt-4lDNbRkEw5BqDPcnYjQKIXlWG2izooKtWaJSop74b2XJ-eMIoVPFdMFewX8ZLkKW8q5z_CjoNVwlTENj9tQxXmklyWMyUC5t5NSDlZEKxdssRCYEkA_Q-yEPAqsyPVlwNmcWGOuss613X_cZrS9nFDyClF3vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=szftXJ00Xo4vHgk6d9r33dVtP7YqN4T_09-bDOeL26vzBhmONomlCcDyqE4Tl3XmDB1Hle42UAewB36KCfA87H_HH5lAOfYtwpeO-r6hYg_lRLt4zobopHWBZ2HlZY1GuqUyxyO7OhjtkmDNpVpyZcqN_oSz3NyGRW992cSQOD0LBWTAt8wFeOlt-4lDNbRkEw5BqDPcnYjQKIXlWG2izooKtWaJSop74b2XJ-eMIoVPFdMFewX8ZLkKW8q5z_CjoNVwlTENj9tQxXmklyWMyUC5t5NSDlZEKxdssRCYEkA_Q-yEPAqsyPVlwNmcWGOuss613X_cZrS9nFDyClF3vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
Runway
با چند کلیک، عکس ثابت را به انیمیشن تبدیل می‌کند، رایگان!
🎞️
✨
قابلیت‌ها:
•
🔹
پشتیبانی از تمام فرمت‌های رایج تصویر (JPG, PNG, TIFF…)
•
⚡
افزودن جزئیات گمشده توسط هوش مصنوعی
•
🛠️
تنظیم سرعت و طول ویدیو به‌صورت دلخواه
•
📦
خروجی MP4/WEBM با کیفیت بالا، آماده انتشار در شبکه‌های اجتماعی
🔗
لینک:
https://runwayml.com
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">uk-new_domains.txt</div>
  <div class="tg-doc-extra">21.8 MB</div>
</div>
<a href="https://t.me/archivetell/6351" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آیپی کلودفلر
آمریکا انگلیس آلمان
با این آموزش اسکن کنید
https://t.me/archivetell/5657</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">Cloudflare Germany
🇩🇪
103.21.244.0/22
103.22.200.0/22
103.31.4.0/22
104.16.0.0/13
104.24.0.0/14
108.162.192.0/18
131.0.72.0/22
141.101.64.0/18
162.158.0.0/15
172.64.0.0/13
173.245.48.0/20
188.114.96.0/20
190.93.240.0/20
197.234.240.0/22
198.41.128.0/17</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">Cloudflare ranges
74.115.51.0/24
23.227.38.0/23
185.158.133.0/24
216.198.54.0/24
212.104.128.0/24
216.24.57.0/24
66.235.200.0/24
198.202.211.0/24
103.133.1.0/24
199.60.103.0/24
63.141.128.0/24
137.66.28.0/24
137.66.28.116
185.133.35.0/24
208.103.161.0/24
185.148.106.0/24
209.94.90.0/24
160.153.0.0/24
199.34.228.0/24
160.153.0.0/24
198.41.223.0/24</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6348" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQ2HRNediZ90PuLU62G8wNdbUqk-xNeBmu0XYJaP-tUq6ZDSjaVfwhDTIHG-t9xBuNA28pTjnnL8L-DD9w2yAZ9Tw9ICdimx-aTX4NmoniL2iCahqEeD2Xw2UUNK2BaXuiuqWGuKjpEtsyG7JKlhc7yUznx_P4TSyN-rdKY2BKaLOGJZ2jD5r3aJ37hP0A9xmWCQtSxQszNkEAoAXlxDDZHzTFxKQR1dM2x3yrdta4Sld4it_Skjrtse-spxoyBnWqJI0yEIg7U7t1zwkjkBQbwic5pHD3WBsTm4qYHgjMoSaBRTAalGTxpMuOu8bMXyKrnUkTEQpXoQpRMZZ4Wzgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکن ای پی کلودفلر 2
نتایج این اسکنر معتبر نیست یعنی ممکنه پیدا کنه بزارید تو کانفیگ بازم کار نکنه
بدون vpn وارد این سایت بشین اگه باز نمیشه واستون از یه
اسکنر دیگه
استفاده کنید
https://cdn-scanner-pro.vercel.app/
لیست رنج کلودفلر که پایین میدم اد کنید و اسکن کنید.
هر کدوم که سبز شد بزارید تو کانفیگای کلودفلر
با پورت 443 تست کنید</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/archivetell/6347" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mueXlgC6R1GzDUF5oPhUmKRomBUn-GERLv46nVvng1-oDu3KzJliABXMuRoEnmNC3fot4EfXkzIpVm262cI6w_UZw_2rc83BTTIWJVKDDDlNTFjJHXULV3-a9m1fjN1Xn_NANcmY3A_TCrWOrJrqiYwo719DRtVCNFW_6nZHMRSYbAvflvZ-rp3Rlkb0gYoV-sw01sex_TFYewTSXfdsf0xmGuxX1cTbOr3Hz-UrJ6Bz7eZ3HPxrZIuYwO0vYtFWpUfa52glpHV0kn-s8s8nAesq2alJO9rcO0Ann9r-OHZgQFuKeNLiTicQ3VrPJxhCABCjw4kmP228G24XUy6xVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DaPdbzhu2x5xdck-AlFSZwf1lSlVknEr0d4YEr_xrlYKkZs_PTo6bmv7JBDJS0i-1BkpfBdKo04lHLrhBfkPkiqmx1DRWh8hn9d40BZx9WBtdwGLvlRSfTDR7iefnobTCOGt6bUNWk0MxmTaEIgiVzFhMBhHT_kmEuOmcDegm01-DuunESLYIM4JxyOiXYXWF2J39rdrZ-Y5ZoTEc4riVEHBbM3Rzx2mNsm1PH6BBeO2Hvq6DanYhcYSXjBU3xpZXEFr189fKhuPBjk7Ya_sl-et3Pmn9Z3l9n9pspHquMknWnEdvasqEZZrUwgQIGECIoUFm3_00bSNG44SvLWT6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZIGywaq5nvM3TJurFsBGkXjNwI-RxKoTcoVPvmusOpyyPabkjNXC0kFgjK2I4yOZPkrfGDjv1E1C6gzS7yu1q2cG6rnvi0FQlxCQZjBuETIzIJCP9nrmc0fVHpgHOTD_Q8LDRfswyeNmHmCz_Tt4INSBdFxKXiLF9CgH_90cAiDZchrF6a7n7UXeJTJa9upkAZrfpZVPjPr0jIByN975NzTaL3WIVGvoHRkeKdK6V3aN2RDHDxF4WFaGdam-ArEI7yekYUbr3sIt2IYch42cryNrvcUoNt19fZuRNhLnALxvSgDpdkiTC0LhSWI0yOQe9RxT4AHchX0dd0zQEAxpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dvGl4lCVMk9EX2hOI7d-i_CBcXqB8J3jA0T55yjzGDXG1Sk17KJMRwmvLuQkMm3U98mlnVLgVAdNB0dMEtm9QkQj1VYRvVQPZc5UTCu7mc5A85k7w0qTD4qQaGJqEtas7AG_yEFR1GqUNWbqZJKmIbEIoprZgpD-kZLpz1K4b-IEyWxig8EqLetA1tLLaUZFW5WyU_3PAqfdJvCmWTK9Dck9_DRzUeM2RooNsCqIRFzo_3ATnBPqW9bZAM9Fgi4nFqNO8V4WgrrcQOdWXmBCdP864AV-SbU7b16F2A2Xj1509kIGCV7bUe6JEUPWVSZQYlu-pE35P1ahPeLyzu63Eg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">7. به صفحه اصلی ورکری که ساختید برگردید و بزنید روی پیجی که ساختین تا باز بشه
این صفحه nginx که اومد یعنی اوکیه اگه ارور 1101 گرفتین یعنی اکانتتون بن شده باید یه اکانت جدید کلودفلیر بسازید
به اخر نوار ادرس یه admin اضافه کنید تا پنل باز بشه و پسورد رو وارد کنید و لینک سابی که میده رو کپی کنید و داخل ویتوری وارد کنید.
کانفیگایی که میده اگه پینگ نداد نیاز به ای پی تمیز کلود فلیر دارید.
مثلا این رو با پورت 443 وارد یکی از کانفیگا بکنید تا وصل بشه
188.114.97.6</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/archivetell/6343" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXReOQ0g3KnDj3nWpngXy8v0Z_MNcGki1ZEMHgrdkG2IDaHMz0sq6WM6viaMH5iomuQHS2HesoN5QLq1zn8TEht84g8FI84izHuTym9Bk4xWxG6DKp1SnQByDRS83lPac4LzRjslRUFxZ3NUPvU6N9O2bUj_3Faeuiiqkzya9cmeMmC1NkYmWmYLRilsHExO1lxWotCxQqhHjb5woVYXgy2lQHFd1e0GPJDPgTlTqJF2accZDmVLHfHbGoh2pfgh4cC1kIuY9xUbsz5yYzqm44VY-mFgY2ZyfUJVZKypK-WP0Z3e8GMTtyYWBcHnD9oOQSyJ5H2299FVk2iI76WdTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
