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
<p>@archivetell • 👥 9.64K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 10:56:56</div>
<hr>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8o_R3jogyF990u7hvY3uMXuOUdwAmm02XAm7WUbaf7Kx4-KhL3wBCLBdoxff_zPmhz6-AaJEm4UmxYZTrTPp2T06VmTeuEB-fBisaxfTXiCtsMbGbuz6sB2lw1CZzAwBH5U4v2QXd0uP_hsIdZuKJptWzHUGvJZ12S80rT5PhHNiSFPHFc4T4Pe3GlkgkfyPudUWc6ePnJDH14Pfp1TBepU3rJvUzwr3QXfLnurj1j0Gvs1YV0ikT6jcy01pTTktAVm8CJaVpNozji-kjPXUHZvbsQTchAPbD6WxGYSjBH2T9ikRMXKUFhDT_7MUsEJ07obt4moasFUYsnO61vS5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی کاملاً رایگان به مدل‌های هوش مصنوعی با Unlimited AI!
🤖
✨
اگه دنبال یه راه بی‌دردسر و مجانی برای استفاده از مدل‌های هوش مصنوعی هستید، سایت
Unlimited AI
دقیقاً همون چیزیه که نیاز دارید!
🔗
لینک‌های دسترسی سریع:
🌐
وب‌سایت اصلی:
🛠
اسکریپت واسط (Transfer API):
اگه برنامه‌نویس هستید و می‌خواید این سرویس رو به پروژه‌هاتون متصل کنید و ازش خروجی API بگیرید، این ریپازیتوری
گیت‌هاب
کارتون رو راه می‌اندازه
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#FreeAI
#API
#Tools
#Github</div>
<div class="tg-footer">👁️ 422 · <a href="https://t.me/archivetell/6477" target="_blank">📅 10:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6476">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=ouuvnu5K3GNIhmUlPtfX8-WHHBXUkmZKvjo_X5ee12x__--nahLPwuNzm7BTu_somHgvOA_WMPk8OcLXvP-7pRfV0xdlf506RgI1AWCKIbDDYPh4AdilYFZlgMhp1eOJgbdEA0L0Sj-FPKdi_T6_0Qci5UzijoLCgNzElTPKXC9zVwt_7o6bXqJ4ox2wuJJSHuMZPlm8WC-eDdG_w6KFqKWHGXFWztqSy2SZy1yHpGLl29fYgmok4YNdJUoIq9LkjnJhv-PUItXsAhCPLX4xFUuxrBBtObU3Jz4QJuWBn8NAnwE_yF4P5RDLTrl6BzYNt1vNrz202_bN_e2luQYyfg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=ouuvnu5K3GNIhmUlPtfX8-WHHBXUkmZKvjo_X5ee12x__--nahLPwuNzm7BTu_somHgvOA_WMPk8OcLXvP-7pRfV0xdlf506RgI1AWCKIbDDYPh4AdilYFZlgMhp1eOJgbdEA0L0Sj-FPKdi_T6_0Qci5UzijoLCgNzElTPKXC9zVwt_7o6bXqJ4ox2wuJJSHuMZPlm8WC-eDdG_w6KFqKWHGXFWztqSy2SZy1yHpGLl29fYgmok4YNdJUoIq9LkjnJhv-PUItXsAhCPLX4xFUuxrBBtObU3Jz4QJuWBn8NAnwE_yF4P5RDLTrl6BzYNt1vNrz202_bN_e2luQYyfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
گوشی‌تان را به کنسول رترو تبدیل کنید؛ صدها بازی کلاسیک مستقیم در مرورگر.
•
🕹
بازی‌های PS1، Game Boy، Sega و پلتفرم‌های نوستالژیک
•
⚡
بدون نصب، حساب کاربری یا اشتراک
•
📱
💻
قابل اجرا روی موبایل و کامپیوتر
•
🎮
پشتیبانی از گیم‌پد
•
🆓
رایگان و آماده اجرا
🔗
لینک:
Site
#Gaming
#Retro
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 663 · <a href="https://t.me/archivetell/6476" target="_blank">📅 09:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbcxoqvEQp2cjCEb6Ebm3xndQwdjQ1ElFTpIK-IWUeDbJ75oFYgaCpEuQ3S1abSC2r69FyfvWMZCRz6QvNUhcBnxycBK08lDPap6GSBaE1YO8YUXA4ZA_igdcpI_xgbb__Cg4m-A4NWa1yl2jfvkcBObygXAEmu8ML43J51fqkKIibJC6sAZ650ns-HlV7z8HxrPOk5pcklUK5s8EIo6NhdlYmdtqfuOh4yDEq-Bhw0_mS6EPmRUqHQhoE_ONyRdmZwliS2LVs9sNexLSe4TRaMsdKA2R7IvxaNtBoeIexWHFVNPDtU4Fi6_DLPsSn7wj-oO7qlLTi-919hNtpNJSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی رایگان به API مدل DeepSeek-V4-Flash تا ۲۸ ژوئن!
🤖
✨
یه فرصت بی‌نظیر! می‌تونید مدل جدید و فوق‌سریع DeepSeek رو تا ۲۸ ژوئن (۷ تیر) از طریق API کاملاً رایگان دریافت کنید و بدون پرداخت هیچ هزینه‌ای برای توکن‌ها، پروژه‌هاتون رو باهاش پیش ببرید.
🔥
چه کارهایی می‌تونه انجام بده؟
1️⃣
تولید کد و اتوماسیون:
ایده‌آل برای کدنویسی و سناریوهای عامل‌محور (Agentic).
2️⃣
تحلیل و تسک‌های فنی:
عملکرد عالی در تحلیل داده‌ها، تولید محتوای متنی و حل مسائل تکنیکال.
3️⃣
پروتوتایپینگ سریع:
تست سریع ایده‌ها و ساخت نمونه‌های اولیه بدون هیچ نگرانی بابت هزینه‌های API.
4️⃣
پروژه‌های خلاقانه:
خوراکِ آزمایش و پیاده‌سازی روی ربات‌ها، سرورهای بازی و سایر پروژه‌های خاص و غیرمعمول.
🔗
لینک دریافت رایگان
🔵
@ArchiveTell
| Bachelor
⚡️
#DeepSeek
#API
#AI
#Free
#DeveloperTools
#LLM</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/archivetell/6475" target="_blank">📅 01:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/archivetell/6473" target="_blank">📅 00:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/archivetell/6472" target="_blank">📅 00:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/archivetell/6471" target="_blank">📅 23:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/archivetell/6470" target="_blank">📅 19:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/archivetell/6469" target="_blank">📅 19:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/archivetell/6468" target="_blank">📅 17:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/archivetell/6463" target="_blank">📅 16:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/archivetell/6462" target="_blank">📅 13:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/archivetell/6457" target="_blank">📅 12:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/6456" target="_blank">📅 10:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxIFTwiPTkTGy8hSYk_7jlVvpQFmgk9IqibGN6Pt6u-fHg0Yo0cul8e-HHT-692QhGxUKJCSsgCchy6kvnhBN7LZ5JaqVm3mfMQrliaReVd4YQdhfITkL3CtzTwPusLteqHBH_wOXJ3hcgcKYBHycbFf1QwzQgTYxKSi4pxzUbgdF-DwBkNP4ZPWFJO0A-xzOVRgTNx02gDxd-O2ca-9pvy7joqFI2Ul-6TUx167JWeW4JfFNRPZly9OEqLdAp7ZdU7hsKpPfrfykEW_wVU44SH4WUtbJew4yZI_5ElSH8Kfolc0as7thIe-UP-JDA7915lJYJS59LD6QW6M7Emr6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6455" target="_blank">📅 08:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6454" target="_blank">📅 02:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GQ4jN7ISCA1_pVz4Yxy0InoT5PoD4bbZzY2qNp3xdwyQ9UZMnI3-rkNFesdX9rfMoFmJakK7_oBnS6EsZvxoEcmUXfYiEdoMNXoCBlL0DOynWFfK03drCoVCB0zy2YUw8HYDSHZfjZnCtI2b8lujmDUaLLSKrBXcDzpNqB8zlyhiVZa8CyXNiWI7xlT9tTZ6AgUELMi7jPJWuLlrpRc1HFZ64Yo092pB5ddSpcIJSSUBHm3AleeJD2D5ldwnHOmBuUD46Bvl7u-efYmfPMwOIqjE1wuE2cMyZ2CZxAmVujghxbN09anO2s_uQdQ0O4RuokbH2lbNLtLbikLt2A5nYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUD7MQeNiO9Yw_w4OJyU8_9HmV9bNS6B3ovyaK0Ir9iRWPIstzc7AC-2AdwVkL4umW8YNHlb2v2TWP4YXdwwSwDmTqgGGYw4gsVVmasdwW7cFQMLyzyNf6QTuJxdNq4_zLk3QbDSTDqawcgzBbRuK9-MPrSSMcCCPJQT_03lOg-Q2yzBol973PaUCvdoaKNIE1ndrrXBR5DjuhzXVhnrBZ-8xG8BQZ79s8OI6ojmn4AUFrNmGWYNYA0k5D_FUPLBAGyL_RPHDItngWZYj0uVmtP6gI_zBlrQVplDrnu1v7R_54M9xL5oGjRYvWpgJeOlZsB1SsyW_jRALLTL4gmXcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Product photography on a solid sky-blue background, soft studio lighting, no shadows.Product photography on a solid sky-blue background, soft studio lighting, no shadows.
Two thick, fluffy, plush terry towels are neatly folded and stacked one on top of the other, deep soft folds, thick looped pile texture. Top towel: white with thin blue stripes. Bottom towel: solid cream. [product from uploaded photo] rests nestled inside a deep fold of the white-striped towel, partially sunken into the fluffy fabric. [product from uploaded photo] lies diagonally inside a fold of the cream towel below.
Water droplets cover both products, fresh just-rinsed look. Top-down angle, empty blue space above for text. Photorealistic, high resolution, sharp focus, no text, no logos, no people.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/archivetell/6452" target="_blank">📅 02:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwGVZvK5ojEX69GK-OABqpx9vkRmJjQMC_0ifWsWyDHjK8HytXWH2mVmkjF25xrCPhyslmknCczO1PjBRDtl_JcPQFX82Chv9l6Eokef9XiG4YBB1YuigA_hxYBo4V3iTgX9qjFKMYXnCybiYZ7QrhvqZzyrZCymKQyG66ZaZwJPUv6MA72sedIZsDCCXj3z_8TcCOCNgTYJCn3nUsZGFYFBl6aJkZOOoV5wqVaqmuWJo9g6Z5K_WO7li0hReQz1AMOfmxWuWpvaPcYXr4b6cgXfkhTAfI2Y6DtaZKl8aTLW6pwfV3-7jYjwTvwhEuDnmu177hPI_S1o8glGaQvbBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6451" target="_blank">📅 23:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6450" target="_blank">📅 21:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6449">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=pIkn8fZyP0deDw-UsERhNiTD4UbJtNTpUFZsbdE8W7z_dEGG4jL_2lKulXl_dEt_bYAoZA5DP-lySjBvRcGxwxrnE7QytqVChldlE5lRjPzJq0EZL6KhfBmF84Kn9ODGfZt72mim3VIPvSTWtBI56HqD18rPeQC-Ii1ziUgbzdowOTjGa65g7mZwYBrflMPopuvSnPNXE0FntedTdc7ydboc4NihDrYudL7VhTkmVmO4ogEbLWw-uYGpeUiNGzt7i8D6uC5fNi4tIdJkaESOzSbxEKZ8JHScFnkluUUWinLEAMfFhUWBCG5X_D6p3MJolGk0mJKe7nevDBR0rPCTzpFNG3e3h0pYIMVwlOcVmDP2OPO-qRuDPyKtT9y2n03-8_x6Tqqb7_mAfn5CClcNC5WXVpLLQURBs9L7rVcc5BQ1IJ6H8yOrISxfzLTZ9D8sLwXa7ylRCzNjkfsWt7aMsy7CxI4uzaFz3XuEW2FEelVnSoL93zQYM2sJYoORVeixPZe0HhGFIySEeHMu5pAvJDtWYzAztXbXCC2Tcr8plD8dZpxm6cOSg987T5WZfD39KlzYFKzm9TJzpjA39nQbVhcM4nDOuZ8A1CWFLpTMI-3YJ77Avj2vqh9iGyPYfKRb-qA-4YqIYeh1P8bB_vcZ3-U1oOG7J98Z0tE8QY3Tsos" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=pIkn8fZyP0deDw-UsERhNiTD4UbJtNTpUFZsbdE8W7z_dEGG4jL_2lKulXl_dEt_bYAoZA5DP-lySjBvRcGxwxrnE7QytqVChldlE5lRjPzJq0EZL6KhfBmF84Kn9ODGfZt72mim3VIPvSTWtBI56HqD18rPeQC-Ii1ziUgbzdowOTjGa65g7mZwYBrflMPopuvSnPNXE0FntedTdc7ydboc4NihDrYudL7VhTkmVmO4ogEbLWw-uYGpeUiNGzt7i8D6uC5fNi4tIdJkaESOzSbxEKZ8JHScFnkluUUWinLEAMfFhUWBCG5X_D6p3MJolGk0mJKe7nevDBR0rPCTzpFNG3e3h0pYIMVwlOcVmDP2OPO-qRuDPyKtT9y2n03-8_x6Tqqb7_mAfn5CClcNC5WXVpLLQURBs9L7rVcc5BQ1IJ6H8yOrISxfzLTZ9D8sLwXa7ylRCzNjkfsWt7aMsy7CxI4uzaFz3XuEW2FEelVnSoL93zQYM2sJYoORVeixPZe0HhGFIySEeHMu5pAvJDtWYzAztXbXCC2Tcr8plD8dZpxm6cOSg987T5WZfD39KlzYFKzm9TJzpjA39nQbVhcM4nDOuZ8A1CWFLpTMI-3YJ77Avj2vqh9iGyPYfKRb-qA-4YqIYeh1P8bB_vcZ3-U1oOG7J98Z0tE8QY3Tsos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6449" target="_blank">📅 19:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeBTjgnOAgcC8foSp4cuL295iqGoDiVXDex8kRm3XqSTtn5_0uurxEY7CmMI6lSJg8OA-eLr8kY2A5I0KaMljXFTRflGN-MeIAtqmUlg2UziJ1vo-ZUP15UBTvpPjww01UOlP6Ic6mNujQHOPAR0Ci084Hve-mJJLzA5fmJJVfjeWl6e--GyQgZ19qbfAhr1LuwKp9P4jj71NCnluBQxGZYu131GeiggMe1cUF_msAwk5iRJDVF0nweVQPcDtqKBKXXwCflf5tT7A78OXjurWOYNWjoRcddztXTatcDFCmLVTb2dhu3pomSPVog5N_HcX5Gg0JEGZXDES0y9AeH3qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اگه حوصله داکیومنت خوندن ندارید و یا پروژه‌ای داکیومنت درست حسابی نداره، به جای این‌که سر خودتون رو درد بیارید، یه سر به سایت DeepWiki بزنید و با کمک هوش‌مصنوعی، جواب سوال‌های خودتون در مورد رپوهای گیت‌هاب رو پیدا کنید. اون خودش داکیومنت و کد بیس رو کامل مطالعه می‌کنه و کار شما خیلی راحت‌تر می‌شه.
🔗
deepwiki.com
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6448" target="_blank">📅 18:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evIP0gTyZ1rtEcpkRFHBjmpfUxAWX53zNX_v9HbdpV46jMeYyapSRrD8jRdf6sxfihXkc4gfJGvYH5ss9WIC5MQLdqZovxVt3zFpb-xovDWbusyaGI61KN7Uu5raEZEISi5kYsuYfHKF_G5M3DVxZ6TTq9IrY1TWugcK_y77ARtvX50yDEF8lUEAL08dvPH8sVyY6qqZ5ZR0b6VeRiwjv0goPmvKtos4EIFWLp5AIduOj2OpqRwHropLb2JUSb-snXPXtbHKifTNklsgDe3XeRn0WcUuWupjHX8KJ2mw1So1tksgMNPKZ8TCjGbEMuPE1H3zdUU9Bzp8brd7zZv3og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت موزیک رایگان
🎧
https://freemusiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6447" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6446">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6446" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKjKKiNskIknAJ_B3pHoBqYLO1FIVNCuNHzJsXaOQusDXOyH1AeX23ZRDxsqxzKCAQwLZtznu1u9dXALS8JY2Z2gAlSMK80n4UN7so-oBQSi5LCLkdIg6yEmHk98RVqb3B2hWz06zRV7DeHJE546UApOTc_aQDjJURTo9hxihVG5-hx0Re5d0l2LIe2duPolXMBWVKelpk9EFv4pPRxSbLpWmtg2Sp-ySSuvCwHL19efnsvPqjLu0EN_MHZQXpsPo56hU51jmvo7Qm6Xa5QP3x12LOEye0bpoJKGxKfDF_AkNRRxtmEf5-e9nDBATD__tJb3WoAW6_RLwqP7Lhw3mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
۶۷ کلید ترکیبی پرکاربرد در لپ تاپ و کامپیوتر
⌨️
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6445" target="_blank">📅 01:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6444" target="_blank">📅 00:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PT36okdTGUl8OvgmyPkA6KfF_Qf6nweL1K1MouQdVAnxaZu7LPzHKZs6-Ar3j4RprZjIWVj8Lhy8FwXjLFxbJEzdkrekfQFUKTCFTnO69YYZrrW-FNjyQwp91Lldv9up4o016FA9sOr5PUgSM-lwV_xvoyK8ZqnRhqsZgwOxa_y0RLmyD7gTtNWogIUmrl5DJduLueFqbwFoIQZ9w-C-bVa2iWbwjhfg3wA2TVSWVS78pIT9GY75OxuGMP-XZt8WIKhFTVkMdJTn2EGB68A93cQAx5i2DcJeAbNK73uROO01OkZIsoI3C7nUGftu96clO86VSt4Hi8hc8AAzKVDrjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6441" target="_blank">📅 19:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6440" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAiF0h9uzSVVs3T2-eGewsk8XwhQyal7hCi5GNV8BmRsVtipnn5I7dMQ8shL_4vAQuHlEHZOhkOitl62rByVy_RMw2mK1gKi_vE_MQ5fcs6fOQNFVZ6sBCVLhSDFgwZzaNS6Q34G4p6nAWdER4XNvXdFvQJaPFFCD0cALt39oQc4qjmxm7PrcNGrqx_k0kcYF1e6fYf0J4T7339ID6e-aeCeGBsAdiQQ_1nIGZKiad-U-0B92eO5yodQTYYoLRv5vFTGqyyQpwFfjBmcADyYywwZyVAiMBQ9lvfzFxJFkLDyQ1o-KxVojvSuZQlMuGOMXxz1egMdkaRPzIuzzngDsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
راک‌استار از کاور رسمی GTA VI رونمایی کرد ، پیش‌سفارش این بازی افسانه‌ای از ۲۵ ژوئن ( ۴ تیر ) آغاز خواهد شد.
#GTA6
#GTA
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6439" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6438">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6438" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6437" target="_blank">📅 15:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6436" target="_blank">📅 11:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0g-h9DxuvOsdCcca5QvywANp8KZ0a2k0T4GAWUWukqllZmxgARxIyKGVW5hum6QhC_FHSgHA9DfhRpFyQpH8YfAUDGo3ubM2No_FGC0nwz2JIl4j6dyehhQxoopdJNHrfI2SkW9uZyUDNCOiQY-HxC_78EQEkDMtKzGqbvp_6X8rTk-duzta6R-pCDGWf_Fig7v-uu0Fbm-W0fPteJaU8dD9LmJsJeTuuOld-KylGytL1veW5LwNmvW-RJ_njxZFzHJOITzIfn_CgKT4nF5Q2R1H7gJtbSYxdRIuuPQrv9yq3igwycOlObx0DEhmX-mrbFwyNbVpE1Emy_W7HCffg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6435" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6434" target="_blank">📅 09:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">با سلام درود رفقا میخوام یه ربات open vpn بیارم
دنبال پنل درست حسابیشم
اگه کسی پنلی داشت که بشه حجم و کاربر و ایناشو مشخص کرد ممنون میشم داخل کامنت همین پیام یا پیوی بگه ممنونم ازتون
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6433" target="_blank">📅 04:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6432" target="_blank">📅 22:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6431" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6430" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6429">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7UMDwLx4WGtfr0LYDICTweq0GyGN-89w7Z9eV-FixR2-U9smUoj6YN8f0ylMnr7O1iYWJBemZNsqEl4RgoB-wFTsLpFdfUF2uZfbN9u6OJ3c80Uxx4loLNzdy2TCQweKO_aa5s0Qa_CRAQz36Ko2Xp9D2v74xah99G2VLgOUz_c90nZewLQZWHtCMoFxYZAG_-c84cs73nI57yZsNWqFMKEHWD9BnRRLVZJBBF0i0KbLXZaMpy9RTpYnTCiQiQsWNpG1JDTtqmE1QHHbn034qZo8LVSqBNGjZ49g9nYqBBYuVlzjndbDJCAGdr_VIodvPJLErgJMl6Z7TUq52_M8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6429" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6428" target="_blank">📅 15:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/archivetell/6427" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rchvoDoa2cTBERy1zBidUU6C4eLAicR9_-pz-2a5Uwzf2zWhvJI_e0C3KR-OaJGcpJMfdxOrv6LLGBRAgsWp3mVRcmdED0jA--tTiZL_B48dtbwHb8YioMcXVki9QAbJZE97Apj7356M4T0jEYDSg7s45YaJY3qLCZimNz9edOY2ftB9JAdZ9zdp4HJPyCu0zEKanvuWBoTsw0Fjr7KjnUMACWQmGW3PFdRLnErlXIeB9bBnGkyUn2uxyWjl6iN0lJcZLgTQQyVdevbENRMW3i2XiDu-C22ic-lC-4CZmHrxVvqhlIrwP_oolXXzxXyIFkTfJUlGXi4f6DlIvIepIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6425" target="_blank">📅 13:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBRCa-L46_lDa93zsYe6olyctq7zZ7RaYq_pb9qBuA5LkIfzVoirGt9A7qSqAaoMB0H84_-909sgV2vfbS-KuOd9QnUYuTTpaiBb2fK7SViXGfMe1I3mHbxlRN4B1ZKOJ_3OnHjyXwgNe7hd-jtQYZWXzhAJcqjcPXBABqrDk_y6gKVMVhKGkUA0-Ru8oUanY3QkOvoeU6ZDW78QaIyso4zNFBOF1N2yKb6l1gdhwc6WPXtEWg1f0_X50sT19GGsbftlKZgv_jZ-mHjZSELZU90qCokno7pTqtrsaxJOQBiGW36uidoNUmgg1PnSqNZivr5xE7MEdkSkuLFxB4dTDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJ7cbtBbIu8jZOZrKVT7v50lG0l_sUvjc5ztSy5d3KWxFs8pceg8szJbr2D7Y2k2C15bxD3CK2fybgRGgnZRMI9xd6N-rKR38_je2EkUSHZVFyIqKinJrIwYlpmr96M7nmclXgKzcCAY8SP200AnPK-hD5R0uDsXJi5kKPq4u8M9wtxl1YpnMtnw_KSYrKTPzaChVvl-q5qFivtYHLRGRMOAEPY032L1BaQG1V3Ry5BC76GlXkPQN-8DX0TtXy-WQo275eLf1n8n9UFCHcsGtXUMxgOkbxaLBnvHvVeCYaXyaSRSNuvpMhwKZ_qlFVhc-k4tD5gcNnpbjfyMyg51cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت api رایگان- GPT5.5
لینک 10 دلاری
ثبت نام بدون لینک، اعتبار نمیده و با صفر شروع میشه
وریفای کردن هم با تلگرام انجام بدین که تایید بشه براتون
با شماره مجازی نمیشه(چین)
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6423" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4LrwLai4pCmwhx4fDTK_jxRNcS4h6tL-3YZA3cCmEE4Y2ZUifGpEZdb5RnTo2wNwZ0szdgYXqr-YKBFpwqi1wsvK1m_yH3QOO2227BVZexSgZNIWdB3RnIEDzAZOon7VulAw-yMuDsfkTuy4jw5esM1fD61exdnygKO5N3qTsqmnuDkwYUKB-4doKdO1cgD42EAgRd8w4tvb7tmwsNNk-qAt7asS4v2jLmGRYIUcVcX_WO28Jciuv8cpiBaV1y6Wbtd7WJi_GPVa0P8MaOOm9k7xSvutC7YbMBezL6iCrMghk6pTKN5p242vg6HTtbXnoDndRvV7oYhVvJaJ-oj2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ty4p4paFdPbd2IRjYe7fh9xgrCJvh6vuRwHujAPsuDkwhRXq7qCl726j-6RA1-J0EvawCZ7areAzzu3shsQHvnQvCOzYfjPEEYbhi1aT7zCMyzTC3jQTi1k2ne1e3D0dlIOeqksu8FPY7R164K92PBmvdpmH_BLHZ6J46e4qMz7SnfTYNJDHJ0iDMflFXMiSrzgEjwx1pfJr2gCjANLAM9igdpJQ6MMS-VWoD72t2ubptrrvP5CUDTfDdSiIO9lYV3KLFhHubTVUlc-b7iNNE3f_ASKe0wU2rPJK1b2DtTR1mL4OTxrCX00fA0bytKlADUsVFjG_d7OT0UqzL04KqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keeXLMF-KQ1Ey2_XYtw2f6knrXpGUTPpf6iM-lcg5D05ZjVjujRsVrPbAJlJn1bB2M2C05dZE8oK0n9R8HXXZYI9670Ohma9iWl1pCiOKnROb3n0VYuIzNF_1RhT_fHnDCh7DodHFizrQ7wPeTzNGSlsiuoZgvwfpGgms7WEFY39yAXkiju2nqOTnwHxkdsfb4-ignqlKq2K1icNTIUS62IvmGB6B2Uk__ADahEf39yaVb3uMMWTEZm0OfA2j8xkd3QCoZkd0WD8adSTaZU1geXVv3q311gQYlH7wXcLGJDZVqIGFBoAbAlAH96LJ7FCVW86EoEsj76ne6HhoQhFiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c9wHVr2B_ycNmuD5ZJaOpQeMdqyQ2TZ-_oplmoRpmm8A7XKFJxMcR4wEU9WXkC9IHjxu8KxRNj7hDRi8i9NixCaXHlYmf3bc0MrcMhfnV8D34sTMQgi6V3pmd_CEHx9yEZ8Xq4yIle0Cq_ODkjxpASexH73Bmb52zJPMfNjJmIeuG6qWZtb19813__1zZGS8ESoiJfZ-re9NcCeUsZkahKQI9C21A7GLtKv3Bs8GvKixfzGia213FQEGECPlFh3IZtsj7Mhw0ZwkbZd1Wah3j8I5ikWyDxIJYnJcrCSRvIiACiYkAv6tGzxVakpvDQ8_hhlodF8uQDes3-iIY5d88w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل جدید GLM 5.2 از چین معرفی شد  توسعه‌دهندگان چینی نسخه جدید GLM 5.2 را منتشر کرده‌اند؛ مدلی که به‌گفته برخی بنچمارک‌ها عملکرد بسیار قدرتمندی در استدلال و کدنویسی دارد و توجه جامعه AI را جلب کرده است.
✨
نکات مهم:
🔹
عملکرد رقابتی در تست‌های Reasoning و…</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6419" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xk2hqIVQqV-akj8jhk_JzNcaEM5Ya7Os-_YEZqg_63dmRfAWNIXMpUDaBJJ9oejom3YT1L-P9sfiAPPeQQ7lRol27kR59o3lnhRuGVuwpFmM0NQFOhCFn6ZXgGYHMx-gHersX6gQqspOHeiqzOG3WgXxUg4CNvoi1YwA-nYS4ymsTmenJFmt0suRQOTskwy7sUZlREBfzJwl6ArND2wLOIi-TG-OSQnZ_cJd54H5uOVxh6GWakfRZgeLWNH_MBPmrkSBaZ97opUEnvUSzlMDya8uRcD6pmaQNJxQXDolaj2-tyqj9Ak5-cXQD1zWpYjotkHaIErpptXTZHcnpF_N3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IawMAoGHFESFp7Q9BlsGI1M82j8JVaAUv3rJG23aLeq1zwi0e92-oGILvU0-UnbHkq3cEgSsriDN9i89cAEROgIRgJf-pk_LB9zO42GpLCj_HCcPkCJzGkMtrvfrzbF1guL1wBTOCWyE7Gfs6Eidmrd9JQxM0863bGWaPBwL_E8cY9KLXck6Vvd_x1RM1Zjw4n4b9rORqlU5h1VBjjxXwRb0MqwuAJs_dASFgxQGR2ERLY7EQCsN3H5rlUdwIsZLVWA9_SLoPBDjb9TEQ8upwdV3bReZdlrkhlcsy2egnIxrM0vj7neRTmp5LvnhEe38DpqMubfIx8C4FeDaAgt1nQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6416" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Heybaat.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6415" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">sadra.ovpn</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6415" target="_blank">📅 04:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6414" target="_blank">📅 04:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6413">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qil5au13xST6HugvbeoTgyN4mQh9q1KMEjO1SOqykxQh6gH8t5pyjI9XOGkGiFx26Hjv-3TRhd08AsmeWclF5CwpsTRRfTB2sdJHgsSz2SkI1bycyyfpuQwPUEZdQeyrYb5dOmrArhf-bkiIKMCxlX_aUB7DjobSzKAZFYJhIAtf7oukd-j-xxwlwUm7mF1aF5fmABxwz-d2zwrs5kk6q0I5t3ojdf_8V4B9Ua91YCeEZaAi6ZJUCiEHZSo-w0z1qYVw2XkhOSJQzz2Xt75rvbQk9eHeFWNltRoACLYvsHZOmWv9DlwblFKNEvgJTsxUBERI3s7IdPlNfeZDWKlaaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AkOXVlY4D4oScLdEVtk4haTvHMSw0sEQ4dFyJv7qM1LPThquTvW1BQEcDUPoQxRsGFTpf9tPsF1DHlkNUuQVT5d8CkOkD4NE7_LsdWa8I1hHkCcid2dpjnLaLuoXWOLtBfMk90t3P3oP1ebbakkl4PZckuWzEuUpdNIHxWif23r8mhZksC17qxnwVZIhK105JCClynQfde9Gf4cywitEq6o1BS7xCS3dBK0t2sTF_gqj3mA7iNwi5DCFA8bPOz59M3gA7YfDaSbQrkJvnSb2hpCr1xl2HWUmpFzqWINPG5DTQqnUFuqZNT4YW7sBHuuGIWi63Gko9nMZLZ-BmDCHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bYqHKAXKqU530SeLv_Z2zk1goG9_rw_g-b77hrdUPYDkyK7USPESw0zhOvwgQyiECEBTTHD52clheFwQkuO-aUD6MHCIwZuZQhE0nltkgB-owPWQ2gLOio_1RbYl0WyK4wXQ31eOj6aXaemkKydE77IMRsj4vp7Nac6HPbr92GUT9FwYw29be_FdkEU-d4radguRipoRQNEX2P6cCHMwSFWzdYqTnPixxyF_U4qUDTVMRIvbkRB_p95tgW7vqTFq3UvTCG04aMYWUS84BrZZN-dw9SsQnXR3nfOAX4PTBpMKTfeFQJUuvLAzYi3uxvNM58m5SEmW3OMddAC9HpaYrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eCNSXRaGnwHW2frUGYhM2YBb7scIr9ibEgg6De2JIGWX186SkEdYUps8uDABzxvxuiT7sE3xIjPncYzPcyj1M8CScCSa_tw_Qoz9k-C6qJlcpGEygUbIz55gSWxn8ENcN2XmdXTHQhMmB-PSaxgtAMpcML-KTat1C75NGQSQEwPK9xqyWiqWlKXNn_1V4exxmoYuo2Cpqx52hXzakw0Drpaq_6-BgZ9aAYbcTGmtyhcobLJRoRVcIYx9ukZCc_XVqd80Z4OGINj0ckBkT_bOaJtqd43LDkjgMRsdt23pQi_ZTaqsfULySTfSeEkgRUBr5OHezgrJCVzCnK1m087sXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت تصویر به‌علاوه کتابخانه عظیم پرامپت‌ها.
- طراحی‌ها، تصاویر، نقاشی‌ها و راهنمایی‌هایی را که توسط هوش مصنوعی و هنرمندان و طراحان برجسته جامعه ایجاد شده‌اند، مطالعه کنید.
http://Arthub.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e186940244.mp4?token=D220-aEX9BnGDHz2DpGJN25sSyztSqgrq71MQxskkAO45wECQ6aRbbO97CBT5Qgf_w-xRcjYj2C_ZpwqesWhKUfvK-ZFbOCCanjOdwgSwFDIS_wIp-_6fELuIVTN_C2aGngEbqWCagHfG6s0Vw_alU82XcnVWoratRA4EwG16FvkadXHn9BEnipE6G-HG2a9XJWN-zlnNEItUk6U2nc5GoWpmPk9kAddy0uIr1xp5bcrJCdGkR5p92wmKQGqoeQFzWJIo6OD6WcuXK6UPHVVYmDldbuAJQCxJvCQYyk0y9s821xpNqKFt6U3aTprQWn2t1kN2dI2d9DD1rNzOH_d6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e186940244.mp4?token=D220-aEX9BnGDHz2DpGJN25sSyztSqgrq71MQxskkAO45wECQ6aRbbO97CBT5Qgf_w-xRcjYj2C_ZpwqesWhKUfvK-ZFbOCCanjOdwgSwFDIS_wIp-_6fELuIVTN_C2aGngEbqWCagHfG6s0Vw_alU82XcnVWoratRA4EwG16FvkadXHn9BEnipE6G-HG2a9XJWN-zlnNEItUk6U2nc5GoWpmPk9kAddy0uIr1xp5bcrJCdGkR5p92wmKQGqoeQFzWJIo6OD6WcuXK6UPHVVYmDldbuAJQCxJvCQYyk0y9s821xpNqKFt6U3aTprQWn2t1kN2dI2d9DD1rNzOH_d6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJ4jF0qKeCzToFpODZ5-ZuK1KSB76de0INQhSszbtQ4kVuJmpChBug0j_wFo2RsQ2-obw7g0fvUGJzAxBxiWekNtEWwQXF-1L3x9x9LJDEfZvYVJVrpkO-1PIw3JYwe6o3jrgV_fsGS6618aUndbIgTBilhWMHvwRtZyk4SrvkRuxY4ujhvEr68me08LNjsOzQS685eTZdJxSjonwgGd6wnGRVVkTUYl2R1R-BHJGfaKWv2AgDjA31ChxBqRllUj-C3okYJbNx407ySGwUU_7U1ieTJ7F9lR1SDWn8-p5qOhIydaNqy6gpUY-RliwFiDCyY-6595g8P-wk9-nHz-4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087fb590da.mp4?token=mOIcXaWT7AIQ1Y6wGKCC2rwNdF9PUtimVuimjZvAFmLlMPcWfiQLoNCjpo4grNp2jsMXx06SBoFN0YxEnwuBVUyC3QTMf_ffov_1k4853osvtSFOaEhZOTn5_md1v1CQ0cjisEEfUv1CDYm8KmFY_9fIgHOOjS75v5exYq6IMrzxIfrmr2nwFV2nAVNNCPiRCBDZOtNt4iRMmNrJqTyVeJgC1II6LKK5S4BfSZfipI1axgmlKlnBFo8TBXmV6Qygb6Q-6jzJ-QQp_SncmWmZBwH7jeXsagubn14UwuvBnwZ_krP-6-KS66y3JIci-N466YKJJvWOulPSLl-lFenhfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087fb590da.mp4?token=mOIcXaWT7AIQ1Y6wGKCC2rwNdF9PUtimVuimjZvAFmLlMPcWfiQLoNCjpo4grNp2jsMXx06SBoFN0YxEnwuBVUyC3QTMf_ffov_1k4853osvtSFOaEhZOTn5_md1v1CQ0cjisEEfUv1CDYm8KmFY_9fIgHOOjS75v5exYq6IMrzxIfrmr2nwFV2nAVNNCPiRCBDZOtNt4iRMmNrJqTyVeJgC1II6LKK5S4BfSZfipI1axgmlKlnBFo8TBXmV6Qygb6Q-6jzJ-QQp_SncmWmZBwH7jeXsagubn14UwuvBnwZ_krP-6-KS66y3JIci-N466YKJJvWOulPSLl-lFenhfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekjhs5TZW3uVCxfbGSCZ9XpQzfQyTydkcEmVM0y1iTIQixckMHj2m4YN0k6OBe8sVOB6uuNlnx0WejYJSuc6dncV9_gUpa7wsxKqlFh2kvWwK2jHy9itBlJf6Kv5KYXLekj9zZq0RId_s96bFBnnkhG_4WQHRUHZnMmQJ8hTXYk7LbCixKdzNY-LTlVZ3z19HJXsUK3ecK1WKHva83gahw0Tuci2j_AaLb_icjRsn2Np8uq_IqcsVPE37pMxo8eI9TWfUgkpC8_F5L5x6ULpHoVTMMnHkFJiHIC1NptDTBhnIseJd-To4JYBe6kfn-Qa-lcFcdYj2ZfByz8cwiDqCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eWt88zsspTila7B4R6eAGSDuzBExoMBf-fv-kMB_LlBHV5_3ehSlRjk5-bvHgUDZiTlu97TchUe-ajBdxxNVUro6geVVZ9uSddTpxpgeqVUvR09DgU_QmP_3HmTmoU4T9o_ifoRb1oQrREulyKOots8qKkm4CTXaqWo_kypb-JBJ8HS6D_LoktJR9FvbdBuFPs8pA22k2E_WnW73xS_I4zZdHJr1VS3-u6UW6PiPw8N83Gim62yK8eyP9xeociaLRmifIninURuESUUzSkwTFhCMcUVjuw5pAlny8o5xdVJnHMlqEWDFJZBPQAi3tJIXdfEHcgQ9Q5PS28IbMaYBtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت Ponytail هوش مصنوعی را از نوشتن کدهای طولانی نجات می‌دهد
☠
این مهارت عامل‌های هوش مصنوعی را از نوشتن کدهای طولانی و بی‌فایده نجات می‌دهد و به جای ۵۰۰ خط کد، عامل می‌تواند فقط ۵ خط بنویسد.
با Cursor، Windsurf، Cline، Copilot، Antigravity، OpenCode و Claude Code کار می‌کند.
https://github.com/DietrichGebert/ponytail
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syFjUstcsxud8XEy9RXiUi0oBPjF4OSWFwVGUDQFCxAB11dVNPAYazp62etLwuy0FDNycKO3o4g5l5-bTdTV5jSFNiSgl4TGZUsOSi7uQbzVA_Wru49sz39DLpFyBDFU0ESMS7rL4n8kIqNKwr_hXG7GMGQUY7JzV2Nvui51WCJtHjfUuiGOG6aWTIYB3zhPs_rMjMMOYs3ry5QHrWKjWOxy-8-y1zPRah60IRWwtLzwOAHdywn01rIt8q-AoZTZOXr367hS_OXj8LhlXXyHEw_NgkhPcgi7-W2DhZOd4KtTJZ43OghGHF9r60V3QotuBloeW19EBXaLOI9-2yu56g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
متوقف شد
❌
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsK1k2jrXC2D4zXcLq-Ndczx_zrEJEcO0uen_m3kbtynSPdU67GhVwTamYrfdZDaz7dIyQjJToSYAQ7fXAApid0jDhoe6arKoY95iiO0LMKOg1a03Fs0lGMoX2Xi6SRXpnaFz-Ugm575BMEFz364g2BmHuINPXKfY1JnQa1cqLURS2ze6I8GcukvDGuG7mnxdA6kkaprM6e-xfSjV6aYyhsqoyg-dIa3SV8N-Bo0lmDuCGAa4yAXCkpREMAq_KZeUxq84UIPXtShmDrlEdutUcaKbMDZrw6FlRYhcu9xPd7YXQhWxQuSizaf_c_Y32ftY39f6wC2jc4BtifoA1qxZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CN2hB0B75mH_M9PBRTjJvkiW_6fecX2jLH_2vUN5zVtrUqfTa-nmiFjl4nZmqjdISSLJ78O5NCG4qfiyyOV_op3k3LbiroBtyiY-OdLXUtXDscYlXdnQ_zZ1H1GMpZcz19ChGEnBFM2hgbZ5vRwyWFy9ToLuupUvuICenWbsmTmbZlIdQUD5RK6JH7jb763E-I5IOnw1Wk5B9B96mi-ADznvsc8Pg6myrdJCjB6v_H22ZfqWy2gIrD_5q18nxpeg92JFFittESZaRMB5OW6FtkW_ZSR4AirzDgCFMmC2ZKLXp_UQcmt73GyKbl5RbpCXRGKDg_jRFWD5qM1p_SXicg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NO5N0jvGJMhGUoMgvXc6VBpQezf2dUijGox4m7tqtPcGdyqwhr7M28J2DX4N5brfmU39uzU5ddDX6wuR3JQwG91QwiKO9G3FQoFugoQaH2sj7IUpVQHhByUoZ1L0_VtRmTMHfTgUXsTdZEtpBB1G2OaJdy0jhTq3ePupnnrFjgNKoaFnrJ2TcUtrBLCv5FkrzFxqBDBCqGbH7wwVEq9sxc-aQPqUzLdOExOF0cz8QbcsoBq4tRX2B808tvFdrTV77a9e3Y7vyc2OCtjlNg3DlrVszVVM_WdeE8DZksH5KJ-xQpOgxtFHUrcUYfrcmvjPsrUSqmmpv6CiinB-tfjhyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZVHPjkmIQZOwxnZbNcTeBWJzAYNCum5UOr-CEDJ4nkvU3r9KFNJYqb5-SrKHkzuSGHnsLgRocoAAUdCtBYKPrP-iTqv11Q0wGaRwY3jen6jTqvVBBobIid_2LznpJzspYX9fAe_XmozG9BJkeH7akdlvve4xGO6TGEKafZ-451TM1-Yc2L3KXFLZgbBK3Z_jjWE75wgrpcxmtpqi02Hgfh21SwU43q3eQMbxaB3GAL7Qlx3EVNMtUQCIiuG6tIY10g1HYyMmSRkIibrC-UF5IXdWZU2DuIEYPHE0KBh1Df5lw4BqLHyzbejU5wDmT7k-jrCNBJsTCRHshDfUvefXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDOY6T1lvRivaXLlwqxJaY7wexBZ5CsCO-wtXVJsvYjv0zxuBUK4Y1w2aPueoNgqc5NmNedG75zoLypi5qfnpFdR-hrs9Bab1AgFCB02Rx8fPxM0TXfSqQpMUZ8w1XvOEGoqwufrAe44LviH1pi3oPtyQm_j4TWMGWlrgVOv6EExHRrwvBuDlDlIEqtvBjUW4EHOe4CMb0YqJhe90KCQFsad7ArwljwPJsMAks8qD1KxPfsxEwj7k1D_b5wYLCZzz1jN7msGkwdY0krjoHtRkUAj5ICZgeyxTYt4TAP-mblRfT1C2AwFW2mZzimE6HkxaHMiQVc0TYCVRiay7S8mHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNcKlmcLB85nEbUtip-MSVwvAX-4HXngqc86bplHhnX85NhxKF2hJqFFWUJdrLT5tvQCBDXkCzAhVZF5ZmR8oEpTBkf3A6Kd4Pg0IqRIiVeP57-O3eWhtKXCQHHfFyES5sGs2QFIUCUnf_up38mXbG7XfC8-u9uq0JDUM7fhksBjpiDDzSyy_6yGOBEtsY95CVdprnvhFTWk8K6vi7a4-oZd96sH7PJ6j-tiTqGzfwTybSDuZP-cCdyBSZHBnfcSErlGUdfJ5qksDFyO_uDMdPLtpNAgrNkzPVnRlfU-OYkAvj-3e3L7IMSNoOA5mLzhatmK7N0cdjW08-4bVkE84A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veILvp9SdQNV8WrOzUEP1n8on0J34vIPTABo281aGy4V0IA8GX2YZ0NHVuvDIRqU_a5_sXK8viPxyIOnJmrhJ1UbWE3cUp-BeENNrBfmaEwmUujkg6iRPFD-wrAiRX_GRH93xcwmQFOmycbr7W8gmCjPKT1RwcoHzxuhtZ8ni0bYywoOXZbmOeNxCu4NPzC45XSoU5-wezFgyyVDt2AeqyAvjPm6ZXnnhdRekRgnpfByjRZaSCGRjpq4qoBq7PD5trMq0FFiSHGEwsbKBQvNfwdKXiREW6axezFlpBRgNxVHmK6atpkOl15sGiz7DmgO1OUIxhBtKwd2sTlB7-M97Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ll6SwDJPyVJmFz3szRFcH2m6vCCJDpFbrhdzUmsgqrztGvHjOIXfSbBSC1D8F_ei3Nu_dzgOAHow3Kjxqk67mXYOjzAwT-O7u9AXfvh1Gft6UxQ-5oW9si0QIKJ5WCQXLr7TyestmIPqnLOiqrmh9Qi0nKmRyNdY3NSetpdzS_WD21KhJnDK9TcKtsNRf8ytqGv31PZxf5Fp1uVZ3NODzGuztMwUvQx7zlaP-Jv14Ai26bMiH8dFrl4u6nhS6q93vDx_dsrYon_Lx9onTSMQ80jUxHwubFSIdnH3reSSVOJC2LbXwEBIC7-hKlsWvdrK06Z6FNAQrEBD9k5v-5gksQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=h4mt_iZ_SKIarmStJRhP0iDPT1kwJnzHALtx9NdXP8M7-fC3Vl2CCS3l1-UljlfCdBzq_UdkFg2Lreu5NRpVc4OwmilUnm1ulXZqcxfQCKtOZftqK37bxm_Olcem7wGVjftNzn-sZYvREPA_AwCbPPL1poGLI5K0lyMX2G8gzOjpbB9y5EY03MqJ0h9wPnGQtWLpqve7lQkb-yK10Y7-THIaxdtr52PUVKnfDoIrKgQyn7uh0l8-XJlBksHWw8ukvi343Gkpa5OR2ByOG6SOpYRPy4I4VY3dkgGL85tQswuhPiu_jkvbKtpZI2bmWKdPw-g3muBXor7lp46_MM4TMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=h4mt_iZ_SKIarmStJRhP0iDPT1kwJnzHALtx9NdXP8M7-fC3Vl2CCS3l1-UljlfCdBzq_UdkFg2Lreu5NRpVc4OwmilUnm1ulXZqcxfQCKtOZftqK37bxm_Olcem7wGVjftNzn-sZYvREPA_AwCbPPL1poGLI5K0lyMX2G8gzOjpbB9y5EY03MqJ0h9wPnGQtWLpqve7lQkb-yK10Y7-THIaxdtr52PUVKnfDoIrKgQyn7uh0l8-XJlBksHWw8ukvi343Gkpa5OR2ByOG6SOpYRPy4I4VY3dkgGL85tQswuhPiu_jkvbKtpZI2bmWKdPw-g3muBXor7lp46_MM4TMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB-xKQs4DncF4FsIQeTqjOwgGrzrVRa_DZDx-0K3Upr3tK4T6HPHNyiVEdc-Duv1aQ1NWHpDfmE1lLfr58VOd54dFljkLUOHWqobYC-rK4FOsrE5vjkc_gLXoyAkZaAXdV201Qt7oeoRlkcn7HkoK1Gv5JhPUe-SBUwXU1fhF3gFDYboEJbCHel9icxYx07KXgHHEwpf5PG5HigggWp7m6WdSatnnDmXVoKcleQUlFijZgzNYYwPbg0IbNBvhuajphZVwG2DVVWDepfS7GE2Qrr9J1thQmYXiYSBuonsbCz1Vq4QFuk5vaC257wAXEquJ9BETHV9OjxfJ-C5UYSBqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atmd1ltBh5KptCJXjuDslMkQK-jHCSSnbDdtgWbGlO87kxNTLVPe8C-ufnbdekH7mfakjYKz-8Lh_MHcwcnErXUP0XFL40Y7DhtCMuwRtUJsHyEySIjRIOtw8zPnLFhA_4Pq8bn0SJUrADwP2ne4E1k75QkZS6LG0h1K4B9NGfMUwNM3HbwumZJMsRAleo_c-Ydp_n29SbHivo7L55OtcXvn-wCuR95hiXxvIbRhWdhF5fDakqmq6V7C-n68Nv0kecckg6rDLi_RChpxK919HlmkDHpEX3bHno4wgMMFj6oC6BtyDdWFzm1Jhy2X57AWyDzLd0D3GnOCMZKbcBTlGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=XpGOzAEzLY-88NNbN01CHlElZyK1_R_Uyfoy0BFA4ruXKZlSxQNBaXaVnQYkiACBVhiGd745kwoNFerXIjGj5Ck4VVoOGb8nOThbpkqqJDyZfjHZTUDi4pJhkaB2v12yoEqF65iGpsMRrxyuaOmyJ16KCSyYmb0dmzFrKB1HQ_OYeYLeJ2eJe1TwbbCEOSCXbig-YTQyGu0GkufobEN_SVUiJp3LKrdwk9KPDlnk2YNFCEPK8qdrjHYlOROGa5uvodIJjl-yg4LYiIJRu4tXwAdXY4owlEb-V0KW1ogJF3OAbaJ5gZ99pBdSh6SwzH9GgemJSCm3irLAMNQvdndr0HOXD67mnNpKcIuu2q-h-rzaozTf49MJ9-pXWgCHCUkSiHvmqX97hJ1MoDrcBraPufhtt6-E-vd_DT-Zqfbg1M4Uk1ifWdYFEEeobi7sAwCCTI3FAXxn1Zb_uBbSVX_I2CEMhPAOq2lnQNx4ocsmhXV08Pry4Dbgdo-0F5JjL6atU_OHM8V7_QAg9twYSKK8395uBfK2JFiFm0F9c-gaO2xP1Z26HPmgy5Hu_MjWimu9ugD3u2ymxA0kuxMCU8X4YNDgyDIlPNi4P-gIZU1S-kLBsqeQcFk2QJwH2xcYwGGqsoDDTcZECdddV5Y06RiwDZQFQaq0O7wLZt0yZoxO-8o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=XpGOzAEzLY-88NNbN01CHlElZyK1_R_Uyfoy0BFA4ruXKZlSxQNBaXaVnQYkiACBVhiGd745kwoNFerXIjGj5Ck4VVoOGb8nOThbpkqqJDyZfjHZTUDi4pJhkaB2v12yoEqF65iGpsMRrxyuaOmyJ16KCSyYmb0dmzFrKB1HQ_OYeYLeJ2eJe1TwbbCEOSCXbig-YTQyGu0GkufobEN_SVUiJp3LKrdwk9KPDlnk2YNFCEPK8qdrjHYlOROGa5uvodIJjl-yg4LYiIJRu4tXwAdXY4owlEb-V0KW1ogJF3OAbaJ5gZ99pBdSh6SwzH9GgemJSCm3irLAMNQvdndr0HOXD67mnNpKcIuu2q-h-rzaozTf49MJ9-pXWgCHCUkSiHvmqX97hJ1MoDrcBraPufhtt6-E-vd_DT-Zqfbg1M4Uk1ifWdYFEEeobi7sAwCCTI3FAXxn1Zb_uBbSVX_I2CEMhPAOq2lnQNx4ocsmhXV08Pry4Dbgdo-0F5JjL6atU_OHM8V7_QAg9twYSKK8395uBfK2JFiFm0F9c-gaO2xP1Z26HPmgy5Hu_MjWimu9ugD3u2ymxA0kuxMCU8X4YNDgyDIlPNi4P-gIZU1S-kLBsqeQcFk2QJwH2xcYwGGqsoDDTcZECdddV5Y06RiwDZQFQaq0O7wLZt0yZoxO-8o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=lmKaeKWL-NwvfQzGb8IjpwMEmnw-N0baokKGk109s3xdVRGYdaSN3XFCRt4-IMFczU5cCESkn0R9PLMYjlPEvPN6IX4E9KP4S112do40Qka3vhKRmWptVmWSZyAoOZoGrxiyCsEPojy697R2rHk16PRKH-0s47LPTEAwQmol34Lpsd6Q7qxhES3nS6_5-JnE47hI6Lopxfc67MXB1iBNToC6xH1Aje7K2P0Y2t3CODiTlmfN4NGkfjCTgUaqQAdl23sR6ZUqahMz591L6ohYqNsB-URce9AroEy8d-fXTpOXUKIH0GTcfAljLAVD9KGAcbhIy2v2j309gNrLgAkdhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=lmKaeKWL-NwvfQzGb8IjpwMEmnw-N0baokKGk109s3xdVRGYdaSN3XFCRt4-IMFczU5cCESkn0R9PLMYjlPEvPN6IX4E9KP4S112do40Qka3vhKRmWptVmWSZyAoOZoGrxiyCsEPojy697R2rHk16PRKH-0s47LPTEAwQmol34Lpsd6Q7qxhES3nS6_5-JnE47hI6Lopxfc67MXB1iBNToC6xH1Aje7K2P0Y2t3CODiTlmfN4NGkfjCTgUaqQAdl23sR6ZUqahMz591L6ohYqNsB-URce9AroEy8d-fXTpOXUKIH0GTcfAljLAVD9KGAcbhIy2v2j309gNrLgAkdhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lA_ug2-fUKyZv1-MvVx6Ckurbe-yDCvONIKLM-F-sU1WLh40pUhczrOiDPM_B1DZyN3sw9yA8tmxxQhyj-U6z9ObmXVErr130Wxi_6qzup2x2MufANrPEph7HnYpR_nd0dHfuzgWWEIGE1Y2MQnQ1bjQapdqShGc8lF8nA27WQpEilhxUrfTeoCNtCu74HMs8opTivtR1Co3d5-w5Ba10iROnoTvZDqCfuminWzf4dI9-G_T0xWR_cOB5us2_WRHZZucgwTKRPpnQ7s8xiiggAUja6TjysyvTgpnEppDBrM0Q5ox6fzd6oifdlUjeNmkbRhPn_f7G0KpuwNRrQjsSA.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
