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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 14:21:26</div>
<hr>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚀
معرفی WinScript؛ ابزار قدرتمند و متن‌باز برای شخصی‌سازی و بهینه‌سازی ویندوز!
🛠
✨
اگه دنبال یه ابزار سبک، ساده و متن‌باز (Open-Source) برای شخصی‌سازی، سبک‌سازی و افزایش سرعت ویندوزتون هستید،
WinScript
رو از دست ندید. این برنامه به شما اجازه می‌ده اسکریپت‌های اختصاصی خودتون رو برای ویندوز بسازید و روی هر سیستمی که دوست دارید اجرا کنید!
نحوه کار:
خیلی سادست! تو رابط کاربری برنامه، تیک قابلیت‌هایی که می‌خواید حذف یا بهینه‌سازی بشن رو می‌زنید، یه اسکریپت آماده تحویل می‌گیرید و هر زمان که خواستید اون رو روی سیستم خودتون یا هر سیستم دیگه‌ای اجرا می‌کنید.
🔥
امکانات و ویژگی‌های کلیدی:
1️⃣
حذف برنامه‌های اضافی (Debloat):
پاک کردن اپلیکیشن‌های پیش‌فرض و مزاحم ویندوز مثل Copilot، Edge، OneDrive و سایر نرم‌افزارهای غیرضروری (Bloatware).
2️⃣
حفظ حریم خصوصی:
غیرفعال کردن کامل تله‌متری (ردیابی اطلاعات) ویندوز و برنامه‌های شخص ثالث، و مسدود کردن دسترسی و جمع‌آوری داده‌ها.
3️⃣
بهینه‌سازی فوق‌العاده:
تغییر وضعیت سرویس‌های پس‌زمینه به حالت دستی (Manual) برای آزادسازی منابع سیستم، تنظیم DNS و پاک‌سازی فایل‌های موقت (Temp).
4️⃣
نصب سریع نرم‌افزارها:
امکان نصب گروهی و یک‌کلیکه‌ی تمام برنامه‌های مورد نیازتون با استفاده از ابزار قدرتمند Chocolatey.
⚠️
نکات مهم پیش از اجرا:
* اسکریپت تولیدشده حتماً باید با دسترسی ادمین (Run as Administrator) اجرا بشه.
* چون این ابزار تنظیمات ریشه‌ای سیستم رو تغییر می‌ده، ممکنه آنتی‌ویروس (Windows Defender) بهش گیر بده که این یک هشدار اشتباه (False Positive) است. با توجه به متن‌باز بودن پروژه، خیالتون از بابت امنیت راحت باشه.
⚙️
سازگاری:
ویندوز ۱۰ و ویندوز ۱۱ (کاملاً رایگان - لایسنس GPL-3.0)
🔗
لینک دانلود / گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#WinScript
#Windows
#Windows11
#Optimization
#Debloat
#Privacy
#OpenSource</div>
<div class="tg-footer">👁️ 618 · <a href="https://t.me/archivetell/6479" target="_blank">📅 12:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsSjzvj7fCgxWibz3cu0cSdhiGxzH3Lvv1A1mn5gd4QSQGihPsyPJ3peEWwYuyzc3y5BfbmCLKa7XWE-ge3pInjKwusuUrMbRiUJCvdq9Ey0wPuBhmiIoVUySLdbSz6Q_DMaG7CdhXNZOfQub5XGrQzfbV-WOBa4B9CNkfOlQAWsdChKeJdJMIxuIQ1m3j0bfo7nFErJIKHGsU0Mo5x0ujZzr2wYhqGQNxqb3KsocKYTpjhIoBPZGRmk6BaY17Tg1JS43Bf_sQMeOiD2duuZcxfyQBDRCx05aPV2-bbZK3PsvSt9D5Tt2bNTdPrbHrxj3FzE6G0NRJlCJm2Tt7avEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
با GeoSpy AI می‌توانید محل احتمالی ثبت یک عکس را از روی جزئیات تصویر پیدا کنید.
•
🔹
تحلیل جزئیات عکس و مقایسه با تصاویر آنلاین
•
📍
ارائه مکان‌های احتمالی همراه با مختصات
•
🎯
مرتب‌سازی نتایج بر اساس احتمال تطابق
•
🏞️
دقت بالاتر در مناظر طبیعی و معماری خاص
🔗
لینک:
Site
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 724 · <a href="https://t.me/archivetell/6478" target="_blank">📅 12:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/archivetell/6477" target="_blank">📅 10:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6476">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/archivetell/6476" target="_blank">📅 09:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/archivetell/6475" target="_blank">📅 01:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/archivetell/6473" target="_blank">📅 00:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/archivetell/6472" target="_blank">📅 00:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/archivetell/6471" target="_blank">📅 23:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/archivetell/6470" target="_blank">📅 19:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/archivetell/6469" target="_blank">📅 19:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/archivetell/6468" target="_blank">📅 17:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/archivetell/6463" target="_blank">📅 16:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/archivetell/6462" target="_blank">📅 13:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DWxrrn1E5x8NxWisWPPEuw8qyYlJLSK8dVXU_Kc6MmNUjVsaV2K4iNDLns8jIDHhnayu_OzNOYf9LuhCQVMtpPGmv7D-xBOp30VWOdAaypXmcXlKvow4g370bQhXpIRpOTEAqJw3sip1wBGcsnm-46pIxEkU2RkTYLUGrBO07yvFqZhcyylga8_lwzLb8cXbbGOzOmPQLTRpfDpbEMZeJyZ891ka1JicNn_g3gYU91N8N1QLuN5MUravqw1sAAHKSNcGHkHibLHQX6l4ZiK74VSTSZsnaG67nIGjahIwO2RWicvAp8G8-slSZEersRF94V15jKrdM-qLSAHE9RlQxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F9L-7_aIfR1QlC8ux8yQJ_euPqRuhfycn1-yxD5PkG4KI2gRapai38p_WEIIEa0tBlgFgJCBLQDF71yFT_LcEzevDnma0Zvbu1X7B53--Uvb7rxGlx6uY3QdxH87nay9eNXjQfUU8CJeIzXIOw_D6gqf3xMLikESFiPPfgHrXCGwNcGIUzWZQzCXhNrWSHE1tphWTgbmOoaR7EAgVCsEqnRUdjyGArwvTXjXijWjnB26kYljgjSkwc8DOxFdZyB46Y5uZyTT2Ffx9JOOy3DYIKz2zrMpHwofbIwdk0dwDvSPlKmq_06aFe2fzCOV5Vexg20rlAKfTnTX9f-4DeWfiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvXCJ8VTEQ9ZJ4keQZtZR2aZYEFWdI75N9Pyqw-LSGBaga6NrsLHDdl-aPEiOo7goU2jibpAOHPYXUUlBUbwHhUO4HqMpDh1MG4xNaBsHeMVENRBNm4fTLWB3utX8lpz5xZ7pYepqvmCnNo_lSGuRrPH_IaeTkHLM2eSZk8SMXBI-PZWDZnPLxK16SGJ_CaASpOldQiTONmLXAhBxGfbW4EB3CRgza36zqJJ8Cm-M0QSlO8nMXjozKvmFmgPyrdimrPlLxP5vcKITCLDsCMsOg1gVHFwamlmBSe14LSpkgW7hsff04n8ldI_XTnrE17gOrSZsKb0QvHbzHjs7UG4xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c_rSRBNYQ0ZyxLrfsGpDarhZv6MSoFv3WqPW9TP9jMzKTg_g-YBDuoaSsrcsrN39v7z9n_s9LTnbvjKR5CbG__-BhWzwk7Zr_MzbpnzMD1Le0J2bkEkzwKj3989ou0jm2EluGLM4kavNSEw8CaIdzIEGYmIZAdKa_9FqxxTs4zeYmJsNl7Is4zie3pKjOpR2wcqnX2RyX6cYwh_mKSJIhf4-_fFfFRTld-xAiJ_OzII6Qzrj50waR_MiPZ6WEQARYM9I7sV3y2M3R_3sgHEMsMFdrEI5GdZTvSd7y2ptd4wLjfSNM44wdtsI5gsyJ-yeMfvZz_RqYJ2u4q1wGWSpGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ded905356.mp4?token=pCBCo9NnzV0W4tUse9BCRdDS_UYD6ur4h0_VgJZ_6zNxOFjgtJYhi9mln3rHtICPSrvvgL7ccw8zni-NgyhVwCp2q9JwD90jRNEs_7KVC7CX4NU85tQ9R_izqwW5V0RT2CIXaVoaTVVhvZgpPhSX8-WIJa991kQfCXK6hm4RKDqPobLxOefjTNwCRngNgHB_f1hyyACL0wVlKORQlEUzYEBP8uT6XbeAdREIal_3tqr8628P9h9FHbodwjXxsmj-ISF6pUeDXwuwONUWWFC-pszgjX0d56NV094CmrqxzPeTEa1HIfdRhQKEC2KonEXN-tHtA8HUX25ZF76sFyiiDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ded905356.mp4?token=pCBCo9NnzV0W4tUse9BCRdDS_UYD6ur4h0_VgJZ_6zNxOFjgtJYhi9mln3rHtICPSrvvgL7ccw8zni-NgyhVwCp2q9JwD90jRNEs_7KVC7CX4NU85tQ9R_izqwW5V0RT2CIXaVoaTVVhvZgpPhSX8-WIJa991kQfCXK6hm4RKDqPobLxOefjTNwCRngNgHB_f1hyyACL0wVlKORQlEUzYEBP8uT6XbeAdREIal_3tqr8628P9h9FHbodwjXxsmj-ISF6pUeDXwuwONUWWFC-pszgjX0d56NV094CmrqxzPeTEa1HIfdRhQKEC2KonEXN-tHtA8HUX25ZF76sFyiiDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/6457" target="_blank">📅 12:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6456" target="_blank">📅 10:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhsqqpK5DeOPjFj2pW0lAKf8c5c-P0mzLdbiamPQcmKviVBcSZRsnK_2NzN0JiQNolIJfcXQWMLs8knrfvbeHv3PNHO8CzP2i2lRLhAk_ef28NrMFl19nKfAFsKU-LHHYZKiHvlxhfZyLA9tZ_GRZOEiBTdQV5viJbKVZmGDfWUaWVSnG7dmZZsgqO2avkipOa7QocfcRZwh6_5RTXWGoQ3Bq4mjpuGAtJQYpPGTI1MydQHVKCliMKHrhZEsjNU7hbv6swVct-sCuH3Vw8G1Rk5xf_FquSXFIE-_yvOv2c9tVN_S-GW38jWuC6NPUq8CqIMeW_SZV-T9SmyeaWyI0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6455" target="_blank">📅 08:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6454" target="_blank">📅 02:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D67Hn5Fndm_961N_xKGlY0OvPJRG_JFAzrIl1l3cTh1gKRnAMCiMbesM5pvya_P9Tz0577C46lNU-gnUwJfFdDcuLcYTUwd_eeyJnN61VdA2hcavOHf_NV4I_-PcATPq1Pp0o7a7Yy9lYrbblDXeVOoELQ-wo-uiy_7fAuOclnNqx0PfbI_G3bpx7KxRLqI2MSB3NZ7ITsdhHR0TDfXSjPbAyHQIhWnjCZNFs5TiVzX23j2LeMEqtvWZf5kRP9CEW994iGJMYYiO6_oPH45G8vZ4iGFNsUdJ2erByL_4vM-IQCgY2q0d0ky6E_23Tez19va985FlUNpUVA8DeR01-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o1ILf-YBP747lORJeJ0OQdCWrrkwkwVvTarShTCAXgXZfpVILUmQiJuXXxkIuQePg73FYxJsUok2TgX7-1QeF7vrtatlLPVVh8fC_8pIwu_fdoSs2d7aViOWYjOxpYLmtz20qLhP-ISPkDguWKfqXtU7uSO5iOQKE1BrTMMlc-qfH0uLuAHWWCDzTFoNqW-1tJ4qdH7BLWgeNUqAop3tsI-r3Gu8zDWLFMFTLNXyZqlgsDoDJdrvPT4tsvtPbsuzR_TIDcREmIwxtR5hvXad6gPsbldkLcUQ7kw0CWBihZj8chkiNoW1byNtdMykz29dEaegiXK2AzS-u8nul-adJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Product photography on a solid sky-blue background, soft studio lighting, no shadows.Product photography on a solid sky-blue background, soft studio lighting, no shadows.
Two thick, fluffy, plush terry towels are neatly folded and stacked one on top of the other, deep soft folds, thick looped pile texture. Top towel: white with thin blue stripes. Bottom towel: solid cream. [product from uploaded photo] rests nestled inside a deep fold of the white-striped towel, partially sunken into the fluffy fabric. [product from uploaded photo] lies diagonally inside a fold of the cream towel below.
Water droplets cover both products, fresh just-rinsed look. Top-down angle, empty blue space above for text. Photorealistic, high resolution, sharp focus, no text, no logos, no people.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6452" target="_blank">📅 02:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCddYRraAWx5_UagOX246gB9WlAonV5zz3rLEt7YoZ99y3su594OzbAdRQ9LNVZgmaoh9e9arFdpT6cKC0d6SRCZaMu3C5d9jnlGlVE1WAnA6fYZzS3R_3FhftR4yXtQx6_SVNbvYyUq-UooYprt-jPOv9ew9fc5BLwkWpv8L22gh5WOIyiN__H_7aEV3fsV6yb5Rc6gitmVhG9erVwuEDEmX2mu_DNqQA9EZD9DMw5oGvjDXmctHrVZdMjEEVzgmeSjkB2_ZnIacgg0YzROjUj7VNjb3pCdi8lvji12wtZ_5OyJnKlaAbFmJgC9_hgratvbPQkdvQgFFzYGFq9p3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6451" target="_blank">📅 23:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6450" target="_blank">📅 21:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6449">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=pIkn8fZyP0deDw-UsERhNiTD4UbJtNTpUFZsbdE8W7z_dEGG4jL_2lKulXl_dEt_bYAoZA5DP-lySjBvRcGxwxrnE7QytqVChldlE5lRjPzJq0EZL6KhfBmF84Kn9ODGfZt72mim3VIPvSTWtBI56HqD18rPeQC-Ii1ziUgbzdowOTjGa65g7mZwYBrflMPopuvSnPNXE0FntedTdc7ydboc4NihDrYudL7VhTkmVmO4ogEbLWw-uYGpeUiNGzt7i8D6uC5fNi4tIdJkaESOzSbxEKZ8JHScFnkluUUWinLEAMfFhUWBCG5X_D6p3MJolGk0mJKe7nevDBR0rPCTzqBuHFrJ1bkuaw0D4OB8u_JNevrfmmelrdzwmlu7Z2-u-byX7V74XLmiQIwZ2Tspwrb50-HJeyoDDFgBXepEg31rsHyPhh-RqNBSmWIQewvoNqk_-ct3-NP-vlbzFOKZEU91aHSQj1RpBwyfBo38dRbIcPyXq01tBrCDCUniaV0kTL-SDErw_4SrhXEteBypQ_w7HopGTBnK4quXQRIAX2qEXVKmk5DgPH1RIpqQBayWpfMoIa-aEBBr-P-bU4YTyWwR-YaS-hGM24Wt7FkBJOB2oRhQyR8xNd1GpEzb2jUdrAKJC21u9Q3yrCH2CrKkXZ-4b1taslXeF-DvOkDnfcU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=pIkn8fZyP0deDw-UsERhNiTD4UbJtNTpUFZsbdE8W7z_dEGG4jL_2lKulXl_dEt_bYAoZA5DP-lySjBvRcGxwxrnE7QytqVChldlE5lRjPzJq0EZL6KhfBmF84Kn9ODGfZt72mim3VIPvSTWtBI56HqD18rPeQC-Ii1ziUgbzdowOTjGa65g7mZwYBrflMPopuvSnPNXE0FntedTdc7ydboc4NihDrYudL7VhTkmVmO4ogEbLWw-uYGpeUiNGzt7i8D6uC5fNi4tIdJkaESOzSbxEKZ8JHScFnkluUUWinLEAMfFhUWBCG5X_D6p3MJolGk0mJKe7nevDBR0rPCTzqBuHFrJ1bkuaw0D4OB8u_JNevrfmmelrdzwmlu7Z2-u-byX7V74XLmiQIwZ2Tspwrb50-HJeyoDDFgBXepEg31rsHyPhh-RqNBSmWIQewvoNqk_-ct3-NP-vlbzFOKZEU91aHSQj1RpBwyfBo38dRbIcPyXq01tBrCDCUniaV0kTL-SDErw_4SrhXEteBypQ_w7HopGTBnK4quXQRIAX2qEXVKmk5DgPH1RIpqQBayWpfMoIa-aEBBr-P-bU4YTyWwR-YaS-hGM24Wt7FkBJOB2oRhQyR8xNd1GpEzb2jUdrAKJC21u9Q3yrCH2CrKkXZ-4b1taslXeF-DvOkDnfcU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6449" target="_blank">📅 19:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SA-9NyjJyJ59iRTl2a32lRU8kKpu2304kyMS4JxYS5afGl1uZ-MWs6XU3vNeedfn9Oj_ajoBAa-xCdEqP7VBZIVxRTxZCZTuHp_echvYPvgg7oEMEGZYJARnxxfy4mbhTyJ0_HearCOyUEdMqCshZVa07nWt0jh6O88SyICdEIgpoQYdhZUP-5GjJGbD2gqudFnrt1cyv2uNOrwAa-XaYLgOhs4FJWjO9eEPJPka_Awe8zHbp0ePpUDL19INE6gl7v3TOd99FdK6SKdJwhUPBBk8Jl8DmiUGRT416r8UJNE057jSeuXI_BSswM9UdTwi7r-D-g8JoIV8P86SYk71dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اگه حوصله داکیومنت خوندن ندارید و یا پروژه‌ای داکیومنت درست حسابی نداره، به جای این‌که سر خودتون رو درد بیارید، یه سر به سایت DeepWiki بزنید و با کمک هوش‌مصنوعی، جواب سوال‌های خودتون در مورد رپوهای گیت‌هاب رو پیدا کنید. اون خودش داکیومنت و کد بیس رو کامل مطالعه می‌کنه و کار شما خیلی راحت‌تر می‌شه.
🔗
deepwiki.com
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6448" target="_blank">📅 18:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8aEOlZ8ojcigCaqM9TtaZ5iaDX6Xg5GUy-_mQ-Nx-se5RuVaX9JeuUYtL0MiL4bDHDjZdHl1oa_1PELNRm_yJOuiePd3zB_E_6u_Gy3mp_7g57TvicXHeosHeMGuj0meYVwm4wAkuy9hCrgxfD9AytE7I05SvFYoESWaO0GhPGVAI4M4hPCW6mKxkuB8U7IsWuV6tKjW_Qk6sxSYUOQA1s3BNF1CovhCd_WWfQkbuUU6h2VULwtHomOuy69RMvsEJoNwT7PaNijydTiBtdZrdhQs3RKfyyJmarPMGu9FkW5sGnDVdcJ6tb9l6MGgS4dVaei-dKobEJ4Wwrc4UYdpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت موزیک رایگان
🎧
https://freemusiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6447" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6446">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6446" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeoJjVY7qyoZh4zmth31GwkFzsSzhZqjeivnDt-a80Kv1VA5ITzGixITBZRYQgH74UnUQeKV8qR2zfxJ5rsLI1XrAqgnwLJ5c0Q3-LECqn0mMOGLc4S-1nqtZ-heds9eu9yEmUn45HsQcgKoM2Qy43XMKerVNakx5s687R_UEG2SMUYni_-pWttVky0rMku2_wFAEKN0exifJpNpZqawQb88ABph3rFP1KnlaYVum_gDWV37gUv8tFE1Yqu6qj-6I1aycRc9ezWqBxybFG-OFJBjUh09e3EjIMUq82Fmx8fGMhi5p2ur8XVHlT9JgTAxUL4l0XxHI_zuEBAMkxq8vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
۶۷ کلید ترکیبی پرکاربرد در لپ تاپ و کامپیوتر
⌨️
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6445" target="_blank">📅 01:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6444" target="_blank">📅 00:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvo2LaedueOT-DkQjdmaUVi34A0r_AzI-UHV2MT96CgiZBt-PRq_D09j8WxjS7HndeYA-eui6HqtcV_Oo88kS5mVZefvsterHZkTBVPUky2TM2P01BgHcSX3woF83tBv1KcSfn45b722TrJMAMpqEm6sMSX3bdag4XNSeY1gezAat-SNUS9DjGieyKw1gGYmRxUqinxWAMre5kB5dEujHJ1CFrjiK5tMoR38BqlXRaDEe1RjLQUiYMcIRz0JEQDLW8Fe2EcKs4an_IWW-gz-YN_tsMHUAZQ3A9N1ZM_oaRPlaQY8UkZI-PskcZX-x7Agbo57WfapE1ZunoMWE1astA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6441" target="_blank">📅 19:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6440" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1S-6-CqpAjBXeoyefxAu7q8VSV0m9-C-kw9FQHm8RDuElFWSwrBwztxncCW3hcT0yVsB4Jx8WYHAL_D9t_VgqeQrgVAbYiyUiQJ0GQEmz6EIVp5OpNh6oMqpVpiM8SMZFwB6QXHch_nocKTVWlg-jL1F5tU62LR_H8m6agRF6zO4Hv6qgKVjfYkLbVvZBRDRwH-_RcAz9Wfs3RPmNbplqGwrnwdYUdxh1vJnPY_Hvq-N6sVCYEU3cbUnlWE1Olby_eVWoARJtbM1VCza3awc1XJHrFAm6j4COYfjwzn-yJSSH1X9Oo4pY_YlxI01K7LgUabnC4QkldrE8o3ChRvBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
راک‌استار از کاور رسمی GTA VI رونمایی کرد ، پیش‌سفارش این بازی افسانه‌ای از ۲۵ ژوئن ( ۴ تیر ) آغاز خواهد شد.
#GTA6
#GTA
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6439" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6438">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6438" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8xBbfi1MkegNpwbV_z80ATmUFp603MY_De6DcOMeescQ0Au54EE-4Tj8T1zr1gJxlgwxo4PssM3K8yIEdngBJmvYoa-yZVb-A2O_j6VaXPjmF2L5jv1to8tBVRT7s2myRrXtymdc6WpJ2lsM4jLjqF9hB40x1riaZE2F_JsTtPcc25sMKTnHmAJZnAiJKV7zaibAzwaV-pRx-E5gcWYljTrFkwkd44tGgibRvwZRYNb9dXyrWydb1T0XVTlo2oIUp6ZN3EZSrew8vceRQkTZtMVn9ns87N6ZxHzHJaw32I0ulpBM8T2uljF1W7CAoJPiyPGJScWvlRlpIO4S2ExkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6437" target="_blank">📅 15:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6436" target="_blank">📅 11:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXExecotmptr24nRENVMmUAv9xDlp0neuH-0vln72ur7IZR5J5DvSMxTxT7l6TZeDO5s_IE7H26AuUD1q35MOiwMeQqdVIeN6UPJmbAqTsskhsNbb1C272TakasM0peeQm9kqxJ3aNJlfhqEUiSP2_JMOYq_dJT3Q3iy4dSsw-VWUVTa4cuJ4cuOE0RJnvbYvqm9EoTeroWbOeX50uYkWKzCpnr_yY8GWDnp3fWTtTLSssqUL8C1mlChQohLUbDEJGHoRyA6WHF7IABQwZeJsSGw-qZPqqly-R4ihKb5SAywifI1Bs2v1h1g3oHN7BUhC3v0g-IU8vSGXiT-F-rSxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6435" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6434" target="_blank">📅 09:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">با سلام درود رفقا میخوام یه ربات open vpn بیارم
دنبال پنل درست حسابیشم
اگه کسی پنلی داشت که بشه حجم و کاربر و ایناشو مشخص کرد ممنون میشم داخل کامنت همین پیام یا پیوی بگه ممنونم ازتون
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6433" target="_blank">📅 04:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6432" target="_blank">📅 22:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6431" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6430" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6429">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUrGML7gEJYlLSQxFKbS6AdkbqklP9JBLW8CacDCdklgbGRbz8a-kbU0TfbuF86k4X_mApuVppYDoWrrhyjv6_I9tkYDNJIdFkb6HQOsPloo32EiYoECO7dRQhZ2CMTWnIW4aoRu7wTDYo3jsNlvEaEHfrhIVDFK4CyV9F8HMn15Du9iwSfVcJ1dPTI0Y5Cs1Ysq9RCkKpkQ69f1fle-UZfs17xCyKkJ7KHI7_phD4NU1KZsXQAiueqBIaS3P7yC2t8QkiQNNUn9lzO3L7pCnwgpqdtL7ezhJBo0XBL48DTx8PpZzghFVy7B7hooCcrEDMWjXV8m7xscZZh2dvQEJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6429" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6428" target="_blank">📅 15:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/archivetell/6427" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0QZ1K2ZtxWhdXibKBv5T9U9tvt73u9k-ebK4ISqvup7oWG5lY-FAwkg-leKABnpMfPsob5Qis-81hUHO1nwp8wRzvAFKsKU7AHGaISXNA0lRSWI-8fxp2lE-JczYizRhL6P_X3nanrEiv6cV0XolUvNloKYD2fhkuT2xWQZdAp1ma3erbkFsXO_DuDAj631VjTrEL-8Fvini47gz2b7Ojk5hGI4qEhQDdMUtg8HdnOjJJbsRCee8_kP1ttAnclKS5YdIctepf9fOEHj21aX-GUiLtnJId-7hRFz_0cdmAJds2wIEX4JDzZeswxNvnzNQeK-KCGATBjejbecLYfd9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6425" target="_blank">📅 13:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHnSV-L0zswnuQoe8UAitvnbPcgXCsbhGLNqnIUpaMLeavBuQfdpFsA1fY0FJvx3Tkak9hdZwve0TKPhNTarv7uoZyI2vU2qHLpFgJcbcDUplL5zXoFS_pgE-52HQ1H1W3go9NzOd_snos4m4q9syFnrKQJeww5RyDWlzoe7sN1LxcSB8O5k_Llv1XTQYITOS7jENAz33qmifG3oSEyR1cZ_6XMXGwVuPa-0oSsfuJeNkN1AcQmGSClOw-FnuB7SMomdI-b-6x7OH1bhpzzofrkR9fOudvk5MjP4H38GFPKKfMBVbNIrRTHsGbTFSHHMnuR3qFqbSG_8WPViYJv3pg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8RV-1iEK8yJGJWyOFdYElF7z-bfJz_eQC3w7QhqcOF72apm2jcNorqWX9PrWpXf_ERtdohe7FyL_xrjAyLXsnYpP3tIm1zk09ZIDOjgun2ZXqjbcaQvYCT4kaJBxR_apjI2IVKKQu71YdN5NwJ9eNGdDQlEesWg1lgNxZ-Ly-c9dJboc2WKLdd9G52Ih4go5g7Kc2fscKg_tYMYemYaSSE2PrLyjlIDUiH0uQ0XurekctBE9FdcNiYJLG_aQyOEb_BBvr3WSbIoFMwPdSy6GQkbz_r2mHlErWaLHtYXZdK2Id4ElMYlXZvZl2EuTajnwyQ9XfBVGJEl0cm2R-AAWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت api رایگان- GPT5.5
لینک 10 دلاری
ثبت نام بدون لینک، اعتبار نمیده و با صفر شروع میشه
وریفای کردن هم با تلگرام انجام بدین که تایید بشه براتون
با شماره مجازی نمیشه(چین)
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6423" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCHbUyS1aUVzEdOqOWS72FeRoIrawAbQStzpdUM-xtB3EM-vuvTiPLlBsj5omRulTwVdxjV-AcLhQoi5lBzv_7ofrFfwfgkaVs11sTbAIjFQXMWUzsEPO-zd5Gp4dKa2VlnMQUwvSowy2dsxePwZ8Lb7Kj2YhgKyZJ_JTdcoxWSTNTOBoxXqOLd-0-8D2xpNEPg8UASJNC6z9CJYzvhQ-TszVh0Pn80oz47Mvj4WUdohTs_d7qjgJn_wT9bxsgKOjTBmGHUV3bg3jquYOOtdEuXjqjRY4LDoFxdr11VF4rZAtvHN15kHGXTUmsgYkNluBIZDo6fSrdES5LEocTFYDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qasxBm0ott6odhCWH_3iR9qZUIgDpqYYPCJd-N2bDeNek4CT4oDA2u7FpiqRFkEQpfD9hiavlvaSeDG6ktJ_EoG68Ma_yPOUIwNtlRvpdAh94UxNMpzjvHvSx0WoF_53DK00xJpvPWOpU7FrA_gDWMG5oWRXusSNjiG8FSUw0z9wei0i_sydZXqsQFGMGOTexQ2XqPlBNr9RE8_e_d8hm8zjy7__Xtg8r7zot8iP8zu-eAw1w0xVteQG0BMTDckm1lNa-foHjekiVvNhGK0vFhF6c1fRDp1XGvHeAK73-dyXJ4TIRqmquP5USrt9lQ4b_vSGw0PanwISJy9-QB8yLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ev5evc7z5s8FNZnR9WbaSrRnGforRpx6JZueGyYTmECO___IBS5lIheVqJ-BfDv-yVcxwAUyWGUlRVsJ8flaUhEmuEDJGA33_ClYtQd8ziNy_7LNvvoXk1v1GWiY3jMiHHs1zxsSxNi3SFHtF7ufTeGZACvUQ73nC_EiCGeP1IKeOqKxV0nUQYchjaYBcxLFJO005zLy4RQoJCAaW4mVpJW165P4jPETA2b0ACBGEOMwoKdI5TkK2FO5NEnR2ZGqdr9-8p2rzSNIGYGrpJT1djLerOvd3Xy4tqS4wxiiK_kyY9ZPMo2hPZboiuYLo7QnoUfJm056pwsUfIiJlTlWkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ADMB6SH1zeuyJSQPUfcY30sxKF1rD7-npFJRpNnLcUzS0D9cRqy0OnEgiTUBYxFXHiL_MVZ3y1v7sonE0lLG4FRMhYn216ba8Wst06NwGaSk50r7iV5RiGrTnZDX6G5SnJtqoD8AxOstvSi0H1sVSyB1k6Num8DaW8qV4jladuStJt1DbTsNYWeGp1XhNHRe9PaxLvaPEgDvdtE4ldl64FBeNu0w1nJ7y-gof5jehgdcLDnPdvFGMrY-Yr2Mp2Owuf5ke8_dShN2tazFuQwFhKavVm_q_ZtXOLEQxqsF7YRUNF1cxWqFagdZXR5PS1z5OBBsOPW9799c9qsyeTwjhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل جدید GLM 5.2 از چین معرفی شد  توسعه‌دهندگان چینی نسخه جدید GLM 5.2 را منتشر کرده‌اند؛ مدلی که به‌گفته برخی بنچمارک‌ها عملکرد بسیار قدرتمندی در استدلال و کدنویسی دارد و توجه جامعه AI را جلب کرده است.
✨
نکات مهم:
🔹
عملکرد رقابتی در تست‌های Reasoning و…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6419" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jcLjwuwOLiEtCDO8cczPp1uumwScBkssPJtfpNT86DtS4ODnuR1D9fLfJJFWcAcErJXxG2wp_P8ZSp3wKrd8N0LuNL-8McJf9ePqZak8kXA1cbaMkW3Zh1T3MX69vrzWvOdBXTNcQ17anovRuQEIK6IL7qGS2MwlS5irdCrnXlDpRvq7A-dpXR8ZPCN_y0hV2EjP7RglF88C_1xW4UtCpbJXx_7r9lER36_zD_tNplGwLfqiEqmySYv_pBqYiKwmAbkoDCKCKTp6ym-LbknXnFG0tM2173SB3FDHl9fu6US84fn0hCveqjqu_WlhmHs9K26vgMG0SYdSsKbwlmxcbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o3QuUXyfj9Xjotk53H23wXm3a4CHC2GdJYcbXqpOhjPgCbKnyolLWDWtNQwY_9IvAT47F0SAdiwlo-wf0YpHwFe_99Else8xVsk7Yd1540BWSKMwXBh2qZL0W2OOFLGI4eywHuub9IuoP63A1SCAuZlsYudsafW2ACaHvYbpGNKBR2zoi__VRvqS2WD5JtrmqMu6RzlvS7KJ9rQ-vyrVqQ92e_bHIG0j9MGrWQcWrGN_9FszHTGmGwoI7CM6vfHGNMFhIMveps_TrjWr54LiSlkRX5y6Hvna-5BuKPHuGmB_ByOZRN2dcgNk0XGAs-5rysACi8B5h-ktUF4zJQXlUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6416" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Heybaat.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6415" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">sadra.ovpn</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6415" target="_blank">📅 04:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6414" target="_blank">📅 04:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6413">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iSlDNzGUNdzYsG8WrHdIN6QF-eNH554RO2Mmb3iAT7OJU8MurIW85LF-XiWvEwzGWH3Px4HAT9l1phK0nvg-EM9G9Ej32nD3YirZz7BSKuxQR8t38s6RQ0V4yF9bBHrdzPX8XWtI8o4qeUerydd61TSgjA-dzHh1rX9EYiEcsoQBeRL3QmecrCIC0NjqhFLtNrDF75Ri_f-rE2OmejZE6Ej2lMPY1YMbFJWDAqMDUEhLzilzTBzxAXmVG8R24Ic5ODkXiTkuAPi-HyElxipsXEa9VYSRzqbCkWm98AI9U9v7RoTOTKcfyrWWBJcg7OPsoOT8aUdbytJ-Uv_xHMlU7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zqm--FzzFo3bd5Zu221n3x9GFBNF_aXf0E-Ba2rNxjWgcmzENxq6ClCLlX_IeXKXauuj8t5X47b7OlH_dxy3R9BYX6NHN_uapsoCq9lfrImqchG6rY2RU8-xsD5BTzeACAFcnfg9_l_nw4BHnCXFUylI_8kdYZvzKYvSK8EwD5eWecoRo1-UrFOIrJeCH5WybyMl9G2gRAZWlHGWcZeW-MkME-srhaIHSua6BJhgd0YQEIqv7yRI_DX2bKsNh5TgjjJMGymph1P8tqwliYai4X_uS6qX7PVu9F34JKHKbNh3tvLNn2rp7yS23-CAx0cccbba4_uc1iSzjuoMusSy7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cmqfs5Tz3_ZOtNlpxgI-RejYkQI8edcaJvxzifUBnECKAL5oU6egqr5mgkZW7v9Ndr7tgg9Pdu-z4hzI5otFbSrrJgciw-S13bJrQAshiXkmeu3jSze2AUMCK0L87bqqyq5FwrwAQIw1O2OnQ9y0cHRhW2Q7wPMsUAsF-ROlLeaOK160q3n9ObJ11Z5zI6S_dlQJn0KsaZ3z_q7NZsqbUmEU5Y8R46GVSNGkDUtArjvVHJcQ2x5zdznsJ49svMs_eUerlbeQFaRNxZcSBcXi6Mk7-O2DGf18bwY3TSlkUjWjb37q335GsP5VJ_-iageP6FsMDaku4jfCL5BAJzsAWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GKOVaOahMzFn5yq3a8r3lb86JhDlJMDDMuqwEhbS6YmYBuGwZyU9IhN7kLtQyxTGsVEcGcnnrcZxP9N_5J49iIY2HhTmqF8S31dgUlz4pkwGftcYHsi2z7DGUT1hASZE63O1EZu6pPwPOCrwG51FK3jjctejGYbV7z5dLskCThqwszCbfPaeOeDVb1Mii4eLBpDbbUlnl4ufFJ75pbh5KE3WLTLQGMWMH_IEArWT269iCMmvEfE6v-FuXIHw5rbC-HUKw_YHBIJXU_eX6oi2G73yjAWuTCQoD6RcbIpmEDCkfoJBB2KWZo4DWHz6yUfjroSxvqc4Ov68Hyc5Irfy-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت تصویر به‌علاوه کتابخانه عظیم پرامپت‌ها.
- طراحی‌ها، تصاویر، نقاشی‌ها و راهنمایی‌هایی را که توسط هوش مصنوعی و هنرمندان و طراحان برجسته جامعه ایجاد شده‌اند، مطالعه کنید.
http://Arthub.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzE9rZnV9caeBsdYzsOw25tn48yupXikJHZPe2N9YfvDcJUIiViiT5BFmgjbVprry8raTahtjdv8ycsB6rz-LqkiYehXuOpUWloq9pTvchg9nPPWTx4DiJdCoayX6bwcckn5qoye14QQGh98NhggdZDlnq7vqr8PS2An3Jna-5h80sI3gclzrXbZrun1_q4tA8eSz18oS3WiecZX-7lMLmz87Smp3Pun8N-LDiE04YBc4HlugYJTlJKzBMOivR0Oy7iAocgDMpSZJ_rRhkp8T2Qj9JZpJ-JmOuMaSzFkMaEaOPgzzuxU4VwoMxLhlomBD1xkb8JHVOEGj3svLkqoog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087fb590da.mp4?token=h-kpwaxK4uE7n1I6Cyj6M0JIhypmcd4H367hBEldwzDvTs8ZQkrwgjLWe_jQ1CxE6qk5O7lBN5txSJx4JsZU5xI2pu9lgeSeTAXxZLxS6SyVX2CCbQi2K9NgJoK4fCMifZrOdFvZKjijhiNXq0yTCa8yaln26ZYaBkJpC5aAnk3TW1CbEl28PBr7VOrEZY1hsY8qIB5422LGe1j9H8X45rPQ3jZD_StXGzab7aVaAVTYDBPAqWBMwao2jHyCL9rxrO1qOT-yjz4ySQ0pWio6U56HGxvxUmcAJ1vriVj7gThmyptCkVTHd4lzrLFf0iyRk0G1PBFmdyLBM1K4FfWS6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087fb590da.mp4?token=h-kpwaxK4uE7n1I6Cyj6M0JIhypmcd4H367hBEldwzDvTs8ZQkrwgjLWe_jQ1CxE6qk5O7lBN5txSJx4JsZU5xI2pu9lgeSeTAXxZLxS6SyVX2CCbQi2K9NgJoK4fCMifZrOdFvZKjijhiNXq0yTCa8yaln26ZYaBkJpC5aAnk3TW1CbEl28PBr7VOrEZY1hsY8qIB5422LGe1j9H8X45rPQ3jZD_StXGzab7aVaAVTYDBPAqWBMwao2jHyCL9rxrO1qOT-yjz4ySQ0pWio6U56HGxvxUmcAJ1vriVj7gThmyptCkVTHd4lzrLFf0iyRk0G1PBFmdyLBM1K4FfWS6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSP9TLW_UVrk8fC-OTDRuNUBWWHE7snZ3jqnhNJhsM9JPy3RGRPhYrfb5HNDaZjVh2oGsGsd9kyGIOqW1tqk_Dwm_gxHRTVy0oH4ZHzdmUHtJp-nvg88iKtUKNXbmxdCne2Gu1yhLNtzrXq1xDLaEdwxsriLLwYXWOjKyPjBHzwXOMOKgfhsqghGR0DkPZf55Q8OkdHqp1irFTMX2h9Ja_0DRcvc1L8ixlXQMaUqSrUT8QMypSlEFA-MT-FODGTKmc9e9xfRpzAN7M009Ptfra6xBx6Nr8SBeuiREV9gsVQRx9XsuoR4ocbijuyTYhJ-Hk6OASGTKcIzrPtjryTi1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WB29i-nGWa4aLGWojr_JW9coNBUaTU5JF41Twe720qi4t32hy0BQkrqMGCgXlM3fp1RgZhvykpr9ms3kfqej1rtcClR5pmi4CRsW90iCahHZeLROVqn-PVkDmdPoAz-I0OMpaqLQE8pNF_8GX49e_-jJdBClxYRqY-AxYHHJUbX5CyniBVgQDyjLFQZ4L8HjeTWczab3ZNnCzxgTVULcXZT788JX3Nz0ZW-u17iFDt0Rv2xlNTC93dW7zX5x1JptEXDs3Q7FL03JKua7aLd1HqbbX-gaobspfiTyeQ9KAUgkF6DQu0I0B0plsNPUO1jaNRnBEr1fsUDubZxaouv3JA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwSHAO78c5mfgwSf3tSYTLiOVh-SKC0BQLuDiP3fBAoPgP8RqvyumpeJHtz72eFWTqgO_wW7MZIUo7b2abb7nHB6zOjJA0Hy3ii8unmAcfDD5r1nSH1xOds9JLXNobO-EzfrGSOerV9A5qk8lJmpEaD78vxmzMC-5b9CrMmY8u2acXH1rfOAi9lhUYTYjI2u1ehqkj-8VRev-5hVbdT9c0QssJG1N9fVxYU9h2QS0LXUefPhDuR56Qs1BiiYS-OT_jx8SawV4TaTVVqZEcRSi0A0p3tkA4C-ILqc1LrtXCNsQOyldweHySz-QChoJkGrL-DOgUCZnB60cYK5j2HHLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
متوقف شد
❌
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mz-ou7cPSb9rsdxUQjqby1ieNiXr6XiKX3Lu6qCVP8r7qQTETN3JReUERvXgAQI-wPjPxz4zSg4Bc3831vB2ynddKft-vdWUgpoQ-powmVi8bpbKGTK8RIGrLFPogs966ppismKgTlRz-vtFPTkRKvZsT7JYGJT51Yu6ovklfs278XZp85SmSRqM6C2oa0ArkMGJ1pHAbwA_Zw9hLRiwFvpUkXR5Yd0sNNJs_CTq8Xwbl-WyL5bP-1L6VxQJfWXiM4s8LwlJyOVL4VEcPdqnyVBkJSP8NkkN_dX_bO8GkCiIZk5rjJHQDdvXYVWPskCXvVbxer1bmMjR1d9gnHDpaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZGFNptqe4x6HFLgEoAtlJWGiYak0-nju2heoSH_pdw3eE4XUsbPbPSul6hKHiP_WNLaYsmQVw9zZwyO7OCgA5tgnN9OyzUJc0GbapU0iT_LVDvhgffnj9orwHrUAycHpwdMJIuQdPucKlLMhyJJX8G5m8lVW9cJkF4aI_AK5Z2RlTvunoM02TzGhORteAF5YuMKQE1r78EiDeOkKGyQk3yAw_-T3YLt9eMdYSMFkKgbc0Obgc3fCTpbyHw0ZHt8GolTumKbIaK34WEUXuTslZLE7FotJsvCnne2ScqV59meXFYCmqq7zXgmlFFUBZj8XbvuDs2YkusjMdDaiqaGEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkgDc60jRofA3lHFZFq2HjGulm-CxziYBwcmVhwwVf2qr76vhTPrcO6XpVvpomcqfwR9xYFlWFhR6w4bHgd_UsSRY0mLdt6kvOc4ayx5BGR5r63hhb2oqi6nwTrRhSCdZIgmgcZk4c1IVz7BerXogr0pow5YOrT7ZRwA-c3xZDx19u_3qt3YUVp1Dzw77c3WMC3Xvj1jAfIqQGG_UaEvdrjLoONJ5QUHZU0uh0uIFfWifgUbh8fFkQW_ANVBRifHuHcYG9jPPqmFF5LPSX_49Jbq9DvDs2sr2f8FCDdVBRbV_MUob_BOPc_eAXWezfhC5B6NPMKwW4d5KTlKskEyZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCqcvzIE4yIz3De_tfzhiY9r0U5SdF5UcIfTp6Pa95TsPU0CaR3HSRMwd2IibUGmFX4sjYgOzdhx2ppgGOg3Qzab516K2EvIzuTUddvQRc2zW483r3EPOCYiI9WzBKHFKB-J87NQLw0PPc2nIge-K2JbWcJAdTIBPKlKoqkRWeUNH2MwG2QE9wuWwST7MSx3Fd6junrGSNn9fNt_rbix8QAbY7oytPnaM2SquID2lAJVBATi6fd9zour5tUUhS19TGl0z9QDgbyqT5lbSX1Ua5LWeeJfvn2ls4gZVF_CPxEhkWMsANmS8sQX9fKadkJqNujhm_FBApi5yu5liIKlfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RP9SB4TN6KpPXj2SHFjT-Jg1izbh4edA07CvVW8IY0VEv0zv8COWERT8KMueVQdwuZbQ2ti8i63nscj3eE-m6P_EiMTHrMA1A9qNPEK1gF2MP9A8iXAcAwvz1_7UO2ZbZrhg5PtUGmXNkkMot8Qwa8HWRUT0LqfZGxoYohnihlXq4u_K2lRcJVUkZS3C9dnsVlf53V0LCQ1dhXnBW4u45gHS0B8Dy4haBlwagiGhx3GftxfybVfbRcZhjz21WgOd2olkc--ZoorFX7X2LKXc2fNxlohRjWjG4Ad9ZH5UL2hiEH-7ZEoBjfos5h3bTPNmHNs-OnGDFNMoApWvU9z6AA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsOd1pbSbkPV_6Nh_9zWMkhXxcDC-ph2ujnI7JVUFUrCKIw01uPzOhwFO4zPJJjdA_NzIzqvq6SiySl8Q_RTf-sxlB7tDWAd9DHMvjzWjV545SKmxeGu1KFSJKttqkvNOEZ7WbeWj0x-cepBUYXw6C76ApiCXmzl0TsjKGie5zzo48mh87XU8VYL7BsT0U9xyIXeRpOeNpcSepXsvFZ_4zhkC_F41unZTwOJlZSwNihHr1I0aAVeNAvzKObccqmonTGBW0WATiMTwV7dHuwN6qG3TYeOWS44gHAYU84rda0YczAxT8lZOpUdc7rqko8d9ZEfcc9JTIS6eEH7rtCXow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjOLGyxpjV49os7341i0d0kSNf73b_HafCB_oFNW0p-qpfygUScYVG5EUMQrPj13As0A5Q5VrCEk00-tIDQb4s4__KkWf3_rY8PSAtbFfV-GjQYUCmK-Ys7Mq8MKrR5YvQT72KjbekFErtLJQtEmdtLeyuKhaOG7_sAWRrZg0-BjPw0veNHdZzV-bd9NDvMaYAGzo5vk0rpIZng0dIA6mhgpA9-mc4xunU3xScgmX_a6jjge3q70Lj8iMEZUQD5CgLVBqhqo3b48i8-2bPVjaoYI50fH9saE2KCvvJwxCyLZTJ1C5OZ_jxNKmdMIj6Hm1qpX_ZzY1HKW9-fqev3r7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agnKghqaVEqkjwbqeaKGLhyxZducM4ryjjB9da7-cIsPfLaJ3mucb1jGud9bXNdLq9uPDtV7SuMae9txtrtdt9-_ZLMYuwGwAoNE7spREV9f11tcAH5buSEMai-dTgdapGGXlaXNlc1LvLPdX-GP7_y3jfpQPN4JbgYY0RVw15WWzN2oRWL6EwIKZez4m5WAtMDkZf0VycmLbmDybmJvBTDk66SrZ-ihehvrSnCmVc_a9Ert-7eEKL6L43xTdQONY_aH8iMBgkhQJqOmjEJ2-yIQOwgTCn4IzC7mjjGuIHy_ze1leklFHwEg3E5c-TtCu94BRYVrMW-dyE7TKRIj4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=YFmCvp_YwT7qqTS628Oprf7szKvKcT3fj2Wo0PTzTKJXBCcQV4HtD2iXdtOdwtg15OfAzMgjcCjZrr6Oz3lpFhwBg1JTKieG5XuLIvDySbTx1zfwAhf5rQIrC2ogiOtL8LYX3Qn1746nQk1VplhxtpJFtj0BD4Y1WzLaU2PlHv7y0U_Uz19_9f9-YSLF50inzysxUnsc_68sk1nM-JUUxo0MGhyZS4ednVsmbvEhQiuq99ajjqQ8Lt1cD4N7X9VJ-jZYNh0PDqflVBBMtH7_K6on43KDdkzPKi4MBxZ9-tn2RkHD5WUIiJbAa8fWN_chZownM-fTfzPZMDskk-GauQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=YFmCvp_YwT7qqTS628Oprf7szKvKcT3fj2Wo0PTzTKJXBCcQV4HtD2iXdtOdwtg15OfAzMgjcCjZrr6Oz3lpFhwBg1JTKieG5XuLIvDySbTx1zfwAhf5rQIrC2ogiOtL8LYX3Qn1746nQk1VplhxtpJFtj0BD4Y1WzLaU2PlHv7y0U_Uz19_9f9-YSLF50inzysxUnsc_68sk1nM-JUUxo0MGhyZS4ednVsmbvEhQiuq99ajjqQ8Lt1cD4N7X9VJ-jZYNh0PDqflVBBMtH7_K6on43KDdkzPKi4MBxZ9-tn2RkHD5WUIiJbAa8fWN_chZownM-fTfzPZMDskk-GauQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1IyuHoPhoe0pFd57rLfpPFOle-EWA27EEhCLZzFEHhhTHTwt-BMzk-sGiS-csPG4tGiveRxYVbbi5Vl0w9HaJhIW4lAdxQfFQultnAMWR7iUc90la11qiP8HhG-sTq26EErJ-HPtdJZIF2RAsOwu_dEhLOMAIcVBqkMdny0zZDX_-jGrJPzkgoh8zhNAiy8BhuoyIy-NTRZeK3prYcDsN6-Kzu1h3vcc07QQKTs2mMrGyUMxDmm6rIGm4BJRgdV_qW8Q54XLQItOkPdxl8vvAs3oioshpNKwCFKxK8mfOxcXAP7tDzV70YpYnsHQ5bkzpQjaD4-t1ZB8RTLFBoB-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fV7tQQ-1D5FsXNCYJvq-qoTFh_rYipTobQeswH2nXL0TeZ9Beubyb_5gcfW8yfmVUzqk80qzA7W_m_CEpvaxbvKQQ2zT2s8_7WuukFwNk9now62g7F3sygJ6xv1XdRlVV53wVc-zggWdGRmx_DMVklBSohhgS41zGK4uyo1y8F8e1W7J1BR8djf1BKr09mP8JNZctSwoTvFBXXKJiPHGBdGurLmLVEvI7Xw_3YeaZ5YRJ4c94venemyIv0RYcSIXZIBkpAC7uzu5Jefj03cP98Kx6PRp2zpLsVStyoY3OXbTXx4Z9z1XqqtruI9mGT2qdZazsZi3PVIcpxGoeM-mqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=XyhV-phjSDUEvY2mJQaoWvoQRSKsPXS0bfdSdFTCSMJ24shn86JZgUeConTfnn5cBcRRYNSwL1zGTmGfOEgFgEa2qjAR77WVehrKNwxBMKID-VadVKL2b-RqYwf8fvfD5khnFPZjysdZg2iacn-tM7JLHVb51kNWv0-kwjuSJmR5vh5KLudJj2dcA31d3QOK7OXOIHsJwigNJtKlbUgBfuestA_JOKNKhoCXzIL-6Z5L5TAcDrgPs5-80NfCIRLGib5ELAGIYLrzmgTnPOSylZih0PsuDURYxu5BMBroOKtSvuwDUYjKR_UwXf7q1OEHmLRgRD-eQ-yX6Wa3t_hzqlCM747UplzQMNOT5I3KYxAWE-j0WbOV_Sa-H7-TXvAK3t4vX827P0RZ3iFfKhjU36pPnljz5-2xbfzji-ntnhgTqKXCTH4no-aYAo93KXJy11Wlppm0sksEkzztX3qeaqfWiXd4NzLIgAtISh1siJqqgxqE3ziXdj6yqDPzVjs1RR_I2qc4GO2wTw63S8ERW4NArXbo95GesT83uz1k3JnCClovz3CRG7EfVOlkQyHjoSJb1IKzYY4BpdLH6QgxUgYVeM8el5KN_5zXUONKq-lzoEYLmMwyr9csPTMaPDSrS3nm3nnZbJyTXXpBbjKVR3vOKuKnzNs0JyOkkQT8jCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=XyhV-phjSDUEvY2mJQaoWvoQRSKsPXS0bfdSdFTCSMJ24shn86JZgUeConTfnn5cBcRRYNSwL1zGTmGfOEgFgEa2qjAR77WVehrKNwxBMKID-VadVKL2b-RqYwf8fvfD5khnFPZjysdZg2iacn-tM7JLHVb51kNWv0-kwjuSJmR5vh5KLudJj2dcA31d3QOK7OXOIHsJwigNJtKlbUgBfuestA_JOKNKhoCXzIL-6Z5L5TAcDrgPs5-80NfCIRLGib5ELAGIYLrzmgTnPOSylZih0PsuDURYxu5BMBroOKtSvuwDUYjKR_UwXf7q1OEHmLRgRD-eQ-yX6Wa3t_hzqlCM747UplzQMNOT5I3KYxAWE-j0WbOV_Sa-H7-TXvAK3t4vX827P0RZ3iFfKhjU36pPnljz5-2xbfzji-ntnhgTqKXCTH4no-aYAo93KXJy11Wlppm0sksEkzztX3qeaqfWiXd4NzLIgAtISh1siJqqgxqE3ziXdj6yqDPzVjs1RR_I2qc4GO2wTw63S8ERW4NArXbo95GesT83uz1k3JnCClovz3CRG7EfVOlkQyHjoSJb1IKzYY4BpdLH6QgxUgYVeM8el5KN_5zXUONKq-lzoEYLmMwyr9csPTMaPDSrS3nm3nnZbJyTXXpBbjKVR3vOKuKnzNs0JyOkkQT8jCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=PIgrTjcO_xfrxDr_R_wZ5nqVt5V3_5S0r1_lauo75kU_sDxnHeKjUG4vRZlCCMCUs8QbVYiDTQwB526zSinTaZgFu5OKH3AU3wVyTC3I0ZKzjac7rofN_1a5T8_t98xsMfi21vyEHFa4yojfKPvppR1fC5Gesj4C4TzdntRvvdA3il10CFRaBEkNS5g-VSwtcH12ckP9fjBGSBOuHbI1XS8tVFZ5y0CP0pNmMc_A9cJXI81cyQ7fFDGFiCNAZEZnF6XdzQIhO1DkF8oG3uLGmc55jfEocGIPToZRckWO9-OZTJmnYrnKmyagW0RjMzkB3pA-sqOz8omeWpz_VQtzaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=PIgrTjcO_xfrxDr_R_wZ5nqVt5V3_5S0r1_lauo75kU_sDxnHeKjUG4vRZlCCMCUs8QbVYiDTQwB526zSinTaZgFu5OKH3AU3wVyTC3I0ZKzjac7rofN_1a5T8_t98xsMfi21vyEHFa4yojfKPvppR1fC5Gesj4C4TzdntRvvdA3il10CFRaBEkNS5g-VSwtcH12ckP9fjBGSBOuHbI1XS8tVFZ5y0CP0pNmMc_A9cJXI81cyQ7fFDGFiCNAZEZnF6XdzQIhO1DkF8oG3uLGmc55jfEocGIPToZRckWO9-OZTJmnYrnKmyagW0RjMzkB3pA-sqOz8omeWpz_VQtzaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
