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
<img src="https://cdn4.telesco.pe/file/SpMsXhxVVV1JWMj17FDqqv89O8F-Nxw1X6wmllcsmqok8VEPodjS9hrU5TTD7-O3MlrDFzVHqtalxpHO2RHGCQO9K0zLkXRNtIAJie6dQVufjHIFymWIEVKW9uVWRNtVTwyoE-I3wCLPRz6oUTM4QEvSwwIb1R1hEzOq6Ih8X51iMpoeN-eqN6zzvHEVkRaYglnd4DA9PQzGyY6e2he68GpQWD2K-0o3usLBpvShAFmZnjww8-tZZ0bG2CPqFWIMNtsS2Wdby7VsmqA6Ahi_t8tM13DN9LtnxaCWhrIpSXXNR4ERsOGsFVk8PZbeqYsxFawHFyYzqZ3G2tbwmgJ5wg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.65K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 03:39:11</div>
<hr>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QK1ZiNG_Rz-mUKGyqJPCMBvUV-tSNY8Yi-AwNOxZTZKj9y_rDtQl3bCsED11eK2BkE45gYODDGHksdY_HD2mrwrpSW47RTssVI4P8tw1DR8ms6u_Y-wGNtqjnTb6s2z7k3QIcj0X5T5-sUoJp78AOmHl3uJVi2jZruZtM3BkRBjHSHbOZ241GAq8WLEShMVR4jtjcqQEyDWi-nlcd6BSQs_CahqO0p75pQ4LK8ooR0Nk-XJdcR9OqE3tk72If0pvOlKJPBtvFASUuxah0bIjfiG_5U5aLkySrn9Afi8tvpyVtSzH6fn_86GGKoyY1LiwYdpdPYS8aDTgBhqmEo3iCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
۶۷ کلید ترکیبی پرکاربرد در لپ تاپ و کامپیوتر
⌨️
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 728 · <a href="https://t.me/archivetell/6445" target="_blank">📅 01:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #99</div>
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
⚡️</div>
<div class="tg-footer">👁️ 823 · <a href="https://t.me/archivetell/6444" target="_blank">📅 00:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhRELl3KBP-uVScBAIHNBIVWIWS2pm6GzfuMdJKeDv45EGRIzjytbqOesA66Slcw4eXfu-1V1JFgDA3KkXXEeJxea5voDokBScFeOPTUAoHmhVXmoHEvEkT6IcQ1WWmklIjwiwtWrcvej9nUQnBog6v6XmHtJu0JfxHCyumKFynSWmI2xGUIvRsywGDKo_Q7khHG5mVs4kGmpW2_ioiBcza7OH9xXPAZrLFM2TAXQVnhMplz9NLX2dj0-iSn7TaG8JEXaHdROQHdjhIFSdJTorvbQlswEQF6nM3mHfnVP17-IVKHeG_qBqwjOQ-Oyctu6L1aTyGlUec4A0JXgpRZYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/archivetell/6441" target="_blank">📅 19:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/archivetell/6440" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toRblf6LXipOrJYgCA9hIWd690ih6Qi_ChxBRqG8l_AbJS63oxNynIO1vBIWByQqELE4sF8mN_EcO5Dy8V07Lgo29EcJgC0QLK1F_CFSmVna96G5A9zq1RrwaZoal7e6OO3c10Y8QyYkaEAG8nR4bu7ZtqaAy0fAiIyMJSmYWrGgAxwJCowHmbrygItP60BlB7R_zZE1obcF4W55Ap5Hp7_zFOAWN5ZiuWh0OugPx8DSTD4PpgFV5F8rSNgvPck7CIe4V49fLHM6vfcWPJoY8TXqEtsVuhCIw7IuA9SKTHZWhfmWG0Ed9YdtWYEuGgK1RmeyIQtn-ozxbSnBgzFZng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
راک‌استار از کاور رسمی GTA VI رونمایی کرد ، پیش‌سفارش این بازی افسانه‌ای از ۲۵ ژوئن ( ۴ تیر ) آغاز خواهد شد.
#GTA6
#GTA
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/archivetell/6439" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6438">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/archivetell/6438" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvroK52sLiuMVaxAruf8MPu-zHWGlIGi9Q86IuOJ6BIiiBB9SHH2fvUImp826CwcMAl01ql0kO2VIqBOqfm2Lw9WgxQMtl4GnX0-QsVtprNCPKOC9s3MT99JhKAfwK9Rigu3aNG1aeZvlKjItEO0refromGF1wqmaE3MMviSRaptOplMVD2GWWbg-vGuGgFyrsF5-Y7JfrJHQPv0rzQgVsAjXFXMq5x5xtPsX3jtnG3-yJn8Tg2u4vRH2sr_FJ882pSYju9qbf8fXvhbS8u7PirtdwfqNxMzptjGLvdPkSwkcE6yB2LCpP8hTk12F9aT_TPBKPHY4A5YeiN0dhBGAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/6437" target="_blank">📅 15:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6436" target="_blank">📅 11:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ni-INrsDP8hdYeBUgtZln2xSKgKetJIJ8bki-wsQnmRwlqoWc5epGaKG6tGVI6QQJop0L_6N3WdjNpTXc-EgRoZ1_ui4NYVchXx0F3f3xTbCgx41I0xOCH6vRVz4b-wSig9yktjmKj9AJoOoImXVP2f5BasHItycOLb-YJbxU7MOd9-FIaBmfvwbtg_Jhi5IDiP5u9v5lr_C2tIeg9jOegDK3kEjxptk386zWkyeoTOpthU0yne8qRbwgJVQrGdDjb2K_qiQPRGhA29kLyC8eHqn-DYqHGXWU_eJ92btc4iLvdzVuBIxk2bSdGsA2JmLx5Qa2Js7IdVX77SQsITtZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6435" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=DJBXirxaJmnjHvuUZ9uBb_TPmZn34LO-XZDtGTJmtNGdjL0wRkxtH4tWZFSMFeOwEGxTtUr0zat7iIONI2DpqWWcP-VI-rIcNh6Z2_g4JWH5ASqf6iQ_8pQXun30nd6iVrhf6crgPChLGmfj5J0ysqrQ6E1cWqWyA2lYvBJF7wnUHT22KEitYSzYO_ei-Frv2xmoNy7VI_7VOcFmhVuJsNwGL5ZXEmWxgfRTgYo6jwlbHrjWQZ39Zr0iB4HveHhnk-1jq1K3-O-D76KBrx1L45TSM-cJmy73hm-2eJ5oi6KVY-rg2W8xTpSO-lRr1kOfAfqIqUzgoRL1GdhRhcedvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=DJBXirxaJmnjHvuUZ9uBb_TPmZn34LO-XZDtGTJmtNGdjL0wRkxtH4tWZFSMFeOwEGxTtUr0zat7iIONI2DpqWWcP-VI-rIcNh6Z2_g4JWH5ASqf6iQ_8pQXun30nd6iVrhf6crgPChLGmfj5J0ysqrQ6E1cWqWyA2lYvBJF7wnUHT22KEitYSzYO_ei-Frv2xmoNy7VI_7VOcFmhVuJsNwGL5ZXEmWxgfRTgYo6jwlbHrjWQZ39Zr0iB4HveHhnk-1jq1K3-O-D76KBrx1L45TSM-cJmy73hm-2eJ5oi6KVY-rg2W8xTpSO-lRr1kOfAfqIqUzgoRL1GdhRhcedvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6434" target="_blank">📅 09:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">با سلام درود رفقا میخوام یه ربات open vpn بیارم
دنبال پنل درست حسابیشم
اگه کسی پنلی داشت که بشه حجم و کاربر و ایناشو مشخص کرد ممنون میشم داخل کامنت همین پیام یا پیوی بگه ممنونم ازتون
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6433" target="_blank">📅 04:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6432" target="_blank">📅 22:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6431" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6430" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6429">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lo8oSB5e7kauHX8GY_yAmEt6rqd8ttPHWsQ9Zo34sQFQX8akupoJVS9M4H0vgoeJGddyaLUiGk-ybH_uKvJK_bqCtf-x4AWyf4YbObe7187Vjpe20fujLGPuxeOYOPJnh0ooSGmQuzUV6HyWrW0XxR2EBr_3Tiu40lyYOOZ49_2fO8XSA8Pt6Hvo-xsKxRmuQawOoRpgFokVDTDtsaBvFVdeJ-pfp0Fv1S898WkPnEUEYjdetNJgm-5MnJR6Gq29PgkULrzQI7imthfdhsLKzySLEYqrJ-SU7JNRZnIYLa8XRZkDEPqfbhnZGPQKcBQgwwHLI8aT-27NeSKvbdU3Fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6429" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6428" target="_blank">📅 15:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/archivetell/6427" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klcnfy4oxv_hNY0lWk8qofcY8Odeql7UppQjT-9jKW767g_lx2HA77KzJI6xsoQohAHdLwNO3kRnu0VtP5a1hDzIag7hH3qTNbH7smr_tfqpOlHi1Zi9WGjCinakjBrhjKgJlSosLMLGA8g857lYA68BvF5Ir67zWwd-miT_eEghhbiulwRtSr5m6XUyAP2EuUBSywInguRfYNJlwjAmhZ0FzhhqUWVtQ_LBpRWNYgKoiqUG8KW7H9Wv3t2akuEY78F9JJbd5j3fIgOPfGzdFZDSkk9pLgbsmXfdh8YXoZ6znoHC79yI7d_7SCEZzfso3XTqaRdIfmEOJjM5kmHBhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6425" target="_blank">📅 13:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_fTlVGsLbUyhVT7CAjPf1E2Mg4XOpsQpFOY9aytDBMolcp0XBvhJZxi-hZjMWfvNUmDc1n8iMnBfYSO3inmHVmcYpo6kmdPVUTCJnjmWnB8lfdmx8XdrPTpseO1fqFYFE8OHeIHPZyBKByH028Zl-d-pkCT-KrnFMYBJpjiTrMcXPJDw7ICLd7Km3BpTPYjgcD7oxzCxcn9wdh8k9LBTO61fQ81fMegVSbAhx762jBOatdgvXPBWVGp8fX0UOLHqhv4vvrzCwh0IxBEx-vaQ5oQBT8nh-xMesm6gz7XTFH4-JBleCw3Y-2O1wswMro6y14FGVrmMLIuyvg1RIuYlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQjuBx4S1E1p9x8bAunPmxUIJ2bSflTULe60OQSwkFBLL-ZLLRNJyniCDqh1Jo-JgtgEH3ASNxi7eHyVKl_nU59TXXD_SUcw3ZoU_yBJqOKI6RVAAEhIHmisX9DMsA9TJwEJhqC9anrsHSjqUEXgAhZp8r5OsVhFpJu6MgR2rAuc_tLIl2xqmRT3pf-JRzc1Njsu1e_2YWDYWOD4yVLM7s4fhukSohcbD3NCQQEmMmGRBr_KNbffTCpnEDLpX4nwblRQK2Ae15yzDM3tEsquaDRvfQuvx-SEJ_iak_Y0GeJU9s2UdXfbel2TzlTCj3E5z-V5wWA7n_xLxrGSwePPnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت api رایگان- GPT5.5
لینک 10 دلاری
ثبت نام بدون لینک، اعتبار نمیده و با صفر شروع میشه
وریفای کردن هم با تلگرام انجام بدین که تایید بشه براتون
با شماره مجازی نمیشه(چین)
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6423" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fv9A0LMexgLC5Sn6pqptfodNvdQjNjIq6Elf7Sz4H9oXoDUbpbEhpWU5PxZsMCCIcKajRISLDBvPZtuaHeHbr_egb6fOwPkwYAZ_MmXM5Lc4gSwiJuEcURTTC4fVBdZ0blLPgUgKmGpz-BFUV53NSYLywYrGiVv04QMHWl5bQPwHo7CLCXCdJH8qetlAQstpN4Iuj-4PvbV77Fjh1O__L-p1-v-9sNkShD7BigG47mOWTqT2GsQzY2d_732Gd_TytL1qz6TQu8mh29_CRXoi7G3xzLFS3qgyG7CDqr46tu1W47qMzYmpWieIGJm94TX2BB1Sd_UMEqMOmaXcAlm1JQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LwS49CZixcJbGdPWbulb6o8-CmfqwdpVFQY1qxz-hZkgU_uFYq5plhbkk1L2ZZDuboXrOzXO95ekbYE9x7VOI_CcLZDJPdyIO7d3hhDhfJG92lF5yJpekITI9i9RI4XeurR2hPHprz5R6D6R0_hnMcYlz22f8aC-U3xfHjhtf8IjHkAicYJ9_9nyTHVIEyEuC5OUfMOIrJPhX1sNUWwU_LUaOUqoNoVavxnAc4OUAyDA5ezbU5XVMXv0Hwc8z5BOkNyNda_5tQFb7aZeGez9NvzwW83myfn1hZDliesynzdQ9wHUhzUer-B3jJ8AmGd9Ja7X-ee3Jggey9kpHv0TKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDi8_m6JL4P2KKA9QnoexXMsG1so4LOM4KMEeKH-jKvfA8e7UhDyF47NHS6hMxia6YiYeMu6w8Tu2SJMAWivd9IbCGQfZQiiHzG04-n5Eqh_6cKPlq-SGAlKZv7MjUuox0PUz9Zahg_ahuaBIBhcHA_3XzbF22fe_vsLSil6JjGCVYs_UDiMSgyOR1B_bfLGiuD1YKQ42q2T83NDvOUmVv0k2jMYiRJQke1AAoi3geByI_WpXZLChDLAzXtnZD-Gpd7wXpeiI71cl7TH2nbseolYxQ3SDPZQDBDxohwdOrTlxFNXLnaVEydCwtJKihyr_m1bAE6Ytnt6rdlHjB4MjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BvIgz9fnGy0gSlxT1mEFWjua95F4hE6ccEXYmBWqxg-9vAhCEUS9jQz5VlF_xtf3SdyJLCPyzrbfn_uQIwbp4_DrSkhUqov2spkzxApwAANPRc8UKGISFi1MW16ZSGasrOeUbUbKivmW8rz0KFxWDgRRw1eEQmbFuRA47Qpb1vuxQNIQu5vJZyGTfaQxNEJCvOPkxgU0eZs72Z81YO6sQJRBq_BITEUX0lwrBu8TUMESC47VmrLAojcgjXUSY0E9C6przAerD59CEkdKnXlIjstk8fHpyWR5M4Dk_sEVmw3yW-8RnD2oGgkodemOPr7AQLx3fARMgr5mqMMhNziM8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل جدید GLM 5.2 از چین معرفی شد  توسعه‌دهندگان چینی نسخه جدید GLM 5.2 را منتشر کرده‌اند؛ مدلی که به‌گفته برخی بنچمارک‌ها عملکرد بسیار قدرتمندی در استدلال و کدنویسی دارد و توجه جامعه AI را جلب کرده است.
✨
نکات مهم:
🔹
عملکرد رقابتی در تست‌های Reasoning و…</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6419" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gYaBsSj51cEfegS1rtfcenhYTaHT4Ap6NUPulo2BrlUvhEZk2YiZ_batGYt5nnUiiQxbIDqFMv1pzwsVj_SxgLyEzbQBbQl07LJzRrm7DwDRpS83FAznhU2aIHRaiNKfS1Eg72ec0cj8Do4GIJXN6Bn7z4-pTgrOwfIJoDxwyu1EwaE30gyrYMlGwpDsbn1cWNoR1ueD3IdcQbP9PGDp8IBvAmQtBiYIFJJelqf4befUmSz0d0iqVATNdqltb2D8YdmJlNyCQgEza4VK8fwB1wKm637N_KI4de6Hf7HR8p4LqTNvwAV8zVLVJhjbLa106hXXx9hlS84nJcskvW0jKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tMd26-Glaei9Qp_M4Qcka_rmKOlLkaPlsqZ8XRm-sq1uhbbj1LPNfyOxecgoAk_RyxhjWkflGWOCdij0JkdTce64wO9sVBBN-fbPZhVAqH7PxsoOdw7-mqBlfjcRIImaYnkwwDjM5fsW-F4bVIv7eNUy08yi3uWU2r0zKTNIL8nwMB2o_hnkRjqARBCaxoQh7iwOCQWtrH353sTPHdBFDKBQGjjx_sdQUCgwsZbJMvErta6JOmYn7p0ScGQrR096ZxqpWjDxMjeWWufKiNourHNiupymDGG21eFM-Q_KnILTnf7mWJXxbN0cUHsoIGPxbi5s4twVQBpSqS219MGUZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6416" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Heybaat.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6415" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">sadra.ovpn</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6415" target="_blank">📅 04:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6414" target="_blank">📅 04:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6413">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A0qyen3yhRHTpRUlvojuXUL4H6rgqvKDDA0ldYqQdf-s2MpSIeveP9pvzOBblpMICy5X4j1pg6yVPJP6F0MHqhqLc0iLCh14cu_CFywe77PrwbGaQIFq9D5h6exfhRzGCLmyTwkaE3wklMt60lcA6byqiuQ9olGoElAREFc5Y-6Cr0XzgpE1sgQfu_mEvbQyrMSmXYj_J2YKh1XuoeYdMSlL0iq54iz95bzQEHz8GDBNKCL6XDLP0sIFVkX3MHgO0ypwQx4VhLFkdEmEARjQnb33I-1ZY23unoPTkt6Mxac0lOdroJlrDlnq1AqQ3ZpqN5MMqxR1eZ2xMvErYzC3FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgoEfCBZn7X22eL4O5IgReeSPoKmGWfCp0_nJvk2M8-6DCngBSfZeaXFG2sH2Kd6nSgLaxhp_HJv301yucDZtxKFvmOKAKfDmWIKwbL2hrm6qTdMpz92yzAaH6y4q0WOFd6Xa6Mzt6rZrblJOm4hNpTgn5psyNbeRt4I0RnhhwkdWev47d1-BPX-2BBlevGq9zMMAdGVULT3ROecNMB__Y8myvf4SAORbHWlgc_cJYL2Ll94pLBFfwfl48H8GyvxfUp3tPfIJnHhcmZyjcEADTm6vtalpjPEIhEvSOBd_ziu3V3msa7fseizei2Do5fQQYeS5fnOPW7d54Q_iRYNjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vwMLVr-jZfAltBWnEO8vS7xnqZsQV6x9HyTKwdXvtSUnLQAnONDHJ2Uil_MqIDTa14sk2IJ67vaYs-yBBOiq0zne6tsNSsHU1E7Tl4NBOB04aWl58YlGfe82b4N4eBITt3cuFerHTjDtOU36QGakvfVOI4PxIkrXmV8a79R6yQJ0wHrNDIMZ0gZaISP4RNmFo3OQk2_WGLi1nDYB-4VkpcyEEE18K3JeuPoCUbB5QisbZc-oKAncr_0aslFtxkrktKYCZljD-tscCULI4DKeSTW7uFXZZG8W5rhoxTfB-8LZzRX6L_ZjcppTFwqd3hd_V0ESMpKqtBSMixUJhnyGlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l6Mn1xuHO49QAlkYGerk1HF9tZZtST_OpWpQjoltjsjZQ8CCx-Q-pvc8VGf-WpZAQnuL28tSOI71qvrQYEBWSVNFaW1E-0XZID--AR2b_wJ8FLPdFtlX4eXW5-CNQ24TBSKFMGuKEGMMe8eMpBaqccauAwsOfCu8n2JoYwScVyviIZN56ICwWqB-9P2C7e8wewKjJOqYxxg60aaC4RpxFqneS-6hdV8fiWH_SCR7bZnjCHo1FXUj8JNyR1JSinHvmzhe3RSfJL97303U1Il67tuw6BmJNSLRWlwM7k9IYddXZgzSXqFfxIiumIoXLeHFcjxFymlsFoZ_pEABoivUbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت تصویر به‌علاوه کتابخانه عظیم پرامپت‌ها.
- طراحی‌ها، تصاویر، نقاشی‌ها و راهنمایی‌هایی را که توسط هوش مصنوعی و هنرمندان و طراحان برجسته جامعه ایجاد شده‌اند، مطالعه کنید.
http://Arthub.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e186940244.mp4?token=c5DT98bS_zjSRF3mdP6eXkkyP_MlcmWC7lSUaRXrIX_Vhahn4irUVdm_VNUpK4EDqOUlP3r0Q5_XLX7dA7AAY7T7SiUMDAaw_tgysSjtgGhZqEChjmWg8rVqCoJyd69u0aW9e-Xxdmz8Lwvylvt-FTbv5Xzd7Xud1Y6jdtWVbaMdTsGP0-E63RMEziaWi_dhxJlJCCgmwLErcBqKo-h_WpGNOKm_IJdlIGfzVX96a5T_F1KlIPqtgbS8Quwc9QICe4FUYZj5bYIz1zUkJUUR93ItkS0yog7Sgkg82OAlUkyFaAnwDA4Dhy4s5ET2NbW3zqsGw73SOOv7UAt5ALf9lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e186940244.mp4?token=c5DT98bS_zjSRF3mdP6eXkkyP_MlcmWC7lSUaRXrIX_Vhahn4irUVdm_VNUpK4EDqOUlP3r0Q5_XLX7dA7AAY7T7SiUMDAaw_tgysSjtgGhZqEChjmWg8rVqCoJyd69u0aW9e-Xxdmz8Lwvylvt-FTbv5Xzd7Xud1Y6jdtWVbaMdTsGP0-E63RMEziaWi_dhxJlJCCgmwLErcBqKo-h_WpGNOKm_IJdlIGfzVX96a5T_F1KlIPqtgbS8Quwc9QICe4FUYZj5bYIz1zUkJUUR93ItkS0yog7Sgkg82OAlUkyFaAnwDA4Dhy4s5ET2NbW3zqsGw73SOOv7UAt5ALf9lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omujpsm2fX9XN3M5GxYwmIdrGxSe7laCxKiLiI9hBaXMAZzI2_eoI9PpPENzr6hCS7pkR57KkVNK90JVUW5dDvVntiumSq0a4AeZE4CG6mDxGG85qp5rmNdUfYE4pSsLekgOW4Oh7841jdoPbsT9sDs2J4WeGZsvTaIpDZr-cd5SC8ybHZPgOHNcfFM9D6pfCkSHNDkJ1fiN14i6pT4yEuqJObwi3XZQWW_6OrmvIHtQXmhQ4Y7SAFLAcmiyvO-sNZ4FbnVDDpl1FIx0sO-5LGb6xznkaCbn1nOgFcY5hqZtmFEUOjOrjt1IftHcR9Xqh8MhdqtwwniEV7oq89CewQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087fb590da.mp4?token=Iput9EAwufY6V2Dfg4ADJG_ZDJY0ISS9DOI5kUmZHd1W_bOSfDWZzsWljXC_BIcfEl7uYdovuRjTxvUehJaRyAapdpvdsVaa4TQyQdgAs6tC1WNY3OtvYkDvmxKdr_DcjseJ9XryQiaObFsOyDTrX1LraYjuzvKpgQIbehEcc_c5IX-zvsTzK5-dyLxRB4DdGn9FzUX6J6Oj2t9MNDGUSK854BKa2SM0IDFpl4b00JxG72VnwlVNhIfnLnOjWW0yuIXJHqA5zNxGctoz70vSDV3EzmXF593h6Q_Z50DwuHVSH5jmwc5YjwffHlage7xx8bv9C4JbK7c_DWynSIUzFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087fb590da.mp4?token=Iput9EAwufY6V2Dfg4ADJG_ZDJY0ISS9DOI5kUmZHd1W_bOSfDWZzsWljXC_BIcfEl7uYdovuRjTxvUehJaRyAapdpvdsVaa4TQyQdgAs6tC1WNY3OtvYkDvmxKdr_DcjseJ9XryQiaObFsOyDTrX1LraYjuzvKpgQIbehEcc_c5IX-zvsTzK5-dyLxRB4DdGn9FzUX6J6Oj2t9MNDGUSK854BKa2SM0IDFpl4b00JxG72VnwlVNhIfnLnOjWW0yuIXJHqA5zNxGctoz70vSDV3EzmXF593h6Q_Z50DwuHVSH5jmwc5YjwffHlage7xx8bv9C4JbK7c_DWynSIUzFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdz9P5aM4y901YW86mtJ0QstfEciV2UAu-nw3DPcJ2zk-LaqE00tINu2ZFL7N8j8E5AEfLUf_uERNbxcWfISzgmGBwnHDCdBcQHWV2fKOI6eVDBxhK2PJmT_JaFRZwsiDF85GzbVGkdBqJg7q_jGhB7qwFCZEdR3Jhysx32HyhUlzbAlY-3n8TTLR5pSi1JqBz8lCbhSGEUtgNls9wHfFB3tiQ1Q3tc7mb-LNJ0WIheGQK9aiei7_trqh2X3ba2-lDiXFT7HynHcdcemTerz2NvBp17qkopXYRG00ir7BO9hheQwffhlyhBq9EV4Ae_s4OB0TLbaNJMy5GqCUqiKOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VjpAzCod7rCqBjdRqsSwQBUqk2-WJiQQQyrAOH-6KRekgUt0dMdhUYh_zYbpLGgpiUwaVc1RJUPh4KP0ySu_GB-wcpV13HDGO5mA8ifb2z20W9jx3SnMORAt3VL9uh4RhURkDgZnVxC7B8aXWN5PwgnddrSmIUT0Y1y0KqzKc58nTq7uoFEYicJLd4PpLCH9GLbqAwU6dJ3wnm_ACKTIILwN26bU0794jKVloMd6ukxgnMgXIsCQ62OgdRX6EjqvujHD2IFhatBIieWpYMzOrUgMq57L6cBDWBxa8hqxceN_ePvu4bEc857DjD7MUWrPldlr0otugxJGHJfQ7IAHow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت Ponytail هوش مصنوعی را از نوشتن کدهای طولانی نجات می‌دهد
☠
این مهارت عامل‌های هوش مصنوعی را از نوشتن کدهای طولانی و بی‌فایده نجات می‌دهد و به جای ۵۰۰ خط کد، عامل می‌تواند فقط ۵ خط بنویسد.
با Cursor، Windsurf، Cline، Copilot، Antigravity، OpenCode و Claude Code کار می‌کند.
https://github.com/DietrichGebert/ponytail
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFcdpwHF50VoRFO17dWlGKlS7jAOv_W3zRub376L-G4c4TcX10XTGlZIjcbfuSMkQEyBmG7MD0eD9xbj3dJvQTp_cokCYp437qlsz2AfzUWikC_tjOktpXrlruKjY8PfoGM06RLNoEgeNzUz_EHhwAL3VYWCx6z77JR93YzCugbyREX4hGidLYetRDB5Z0IS24xHOO7Q57iTC4c1VIV6v4x0ZRhmAwzW0xXviYZvAqaZEEhXlfqT52dLg69fvNyqeVutfSi3farYvi7DpeDFtVjpfmmCREWZJu-pnr9hbe8pdJle1TacLwZA5Vs_hIqoPBiIH-UZqYv2ku5W6scZcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
متوقف شد
❌
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piblzqBjjjhENJAdUYuD_CDuOqQ6lOi5fyUU8q_UPNlmQpD3z7wImtFOFdTX4lkrQS8Gp4stYGAfgbyvdouFOvsNWRx1EPYSDHoYw3Bf5IIuNvu2k0hD_o2IXXiXGsXabV51p1oFHQuN-oXRS_Bbb2RzKOBfh-m5aJHSZKqUf9rfTipqvE3UnIZeZhl9eabgqwxku__3l4vqkKBCArcUbvUyinSB6zMald-J_UsIJKPjsGBUvlrgkQHfnWJSpgygBdSCmEGYi-WGLwQKRsNENH4AuI_zaoLwWpdsCpEtQedlYXc0SRC_le_2Qsp0R_z1tAlB3v5HIzWmywcIns_NGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQ5H2VYENEr2Pl_SOnYGFpTIq5UrDUN8oZxQHwvndDb1F1U1xPvc1i__LEB0fM1my4We7WrqARHTC-0IKe-oaIdmAMnTVM5NZFncwoNMEBNgWKdLu2bOszA7YVB5eh7axUJje8YU6OeAJILYWOwYg5eBi5zB8ySzzIlu3bugs4fr1tB6Ok-GB5EfzfvmCtWGXW5pBJ5GxJy2AGIEL_9gFdoHsabYSj8cI59EiD8crnFz5EO_mAM6JWvP2NeX9hOrKo-VOfA6gZgXxmsYc_nF-JgBQEIXkLAhRhlbsCJEF9FEgdbLuSa_3aeG3fWW45d4yF5rROYOMOf5Iitn4Akt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeeFteh3bj4SDU3AxzgXobUNN0jXL8060rQHhYAn74Of4aFi5OISZvHjpcDTlBj_FDlHabfsAVSuujoSSId9zIFlV-eG8Xej748_gTi09_hcL5iZ-om34MxfemNC8T_-dW-WBukMViH-A1Ao1Gceb0Y6MmeXlnNhG6WL5dClBCU1dIHxk8MeFSJcQ3EOT98HJIrljqZKOqesDDltJCNT-QFCrScy0mT9KTr6Uf5LvdXmxn69tZh-RgfBUTPBxKYzdkvCxfBcmhWux5TcenXR7FR2K8TtQwBQvZooFuRouchboHLUqgUvSVONUSgk201NEfCqHCgAeu4luCGQYKzzzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCVMFWnKsK3RA-r26VoRHNF037jge_aaY_RmyXrXA13bC3W7vpNYNUpkP4-5NOFnrB6IX1n0pICu81LXF9Fph2gLl0y3h5od6bO8IBt_iW6bcPnfEXJyd1XXuMFGZRm-PY9xKutKO_splbJNLpjBjjcJsQOrQYehMZKOmfc6ROR3JOiJKtfCPs-5oE44WgFOTUBisf8bJL7rSLdIXDOz8p6S2OReaQh2vM-z2l6pDlqmzKRLUsQMvMkYYiKLWjojaI-tMpj4s1cwJSk7CbOhHGzeJof3855MkYAZLV2uO5KxiKHP9YEMk9GO8YZZns9dEFmEpX4QUJV8fVjwDW50oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5vDXX7dU_tXiGgnTN6N2m_G6Xf6afudLjXfEiI1DICJRzy1YFAEB4_hYG-dub8_j6pl0pzuJlCBYhM9GRSuDe2EGrAonPNqFIAlG7D1-AG_kQhxz1g5PPPSlf5LGF2eOCyxlsb7LwaHdyxN6jw5-XFDBv-G3HVZkSQRpSQGMSG5wUcNjLKaGPgezyNi8kHzyPrx_S_jbbjcZtROs38uTD6cMWLkfFnAiLSAZdHi7e74XbUJkJZH4-rfK8MaOH4cH0yjWoi91sKJcsa-iandlev5cr6LdBOxiELjTew3wlbI4HUAkkGVqD2UrZLIb4G_tLWEXJyM2xKyWSCQqmS7OA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8Qz4BMBsZDp1KcI7-yc6gL3rE6bBvxM5JzRS6nHHoub_ZG63XHIfsihX98mqzvZZND3Cjs9m0B_RXLsAULr_x9s-KX5upOJdWMqRLYIer1-XbhNa9fXcc4rGzh05H6XMxJxIDPla2swiDZDks0E-espzh2484CzxVBuCVC5kecl9BgY0sszwWVFM_MAdbz422bAeZb2209UZG0AnR6yfdZRvRia7HIZEkKUiepSKyIFMFr0G5YVWMdOGXFdz3pthO4sWSbsCY5VDf2THa_TGGlWeZf_6WsSAyWHszyu-odcGJinWPbMFB1-GVzMtsiJ-9mmUxdCsBmot8mvLDjXiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZcnFLb_oCiwLQRGdgs8fHdRwoz355xlvroBjmYrgClIljwl98LKG00-Aaw-3z8DX4VFHc9ZFhonL9zpuRMO_boaJeHTMSjIa-bLaFMaIJxHJetoVa-wByLSC5AkmA5HWge_mgREfk2eTmWMI6z9-yJFy5N6nQzYM1HiqlS9A-qWpgjtjjEOFdU-yLUEx4kEAwmNFAoqKbhmSvdtydxnoBJ5kG490LYtNG_jfUOG9rgBDz_JMKbrnWUrvuqAMBLdAKWsIDAHcCyJM-q39UC-CX-OcIv1h2l9C_yKe_cKPvFQ9WmcgVNHmdrI2hBgcHHl4p3lZ8gzQHsL263dzbYHaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzNMSl1YG3GSD5NzG6AJs0DfzjMgTrVA_UKcfDgLuv8Iy1U0TzaFoIFN9F7pzf68ECoNXLSjA5OXUbrYupJ5hSBbg_R5tC7lSUIDQTGOfSmQuQc0TkH49joWrOHYDEPIXd-aELYLomBch0UZRcwnpWvd8YiHRcVjhnV6ojk3d7paaACrBuKfdHGTmXGuoimt3GVZRDqvq30yp_nv4C-sIyvtDH6fIuC1OVg1jzkv7sBPCyWDmB7Sj_T_GcLe0DdJTaHIn5oz-UAce3lYPTAOe6ma5aXFjVYyyGAmLSiPZomDb0ZiTXmUxMiBPvsypfG3-QrzsEFHHT3ZLbb0AbO0Fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=T69_pAOdyacG3F-KNaWeHO50z-XWumMpnM0chSsvUoSWZ2NLhFWl9Ozi9ja5PCLDkP_Vf1MORbozUSAV_XW65ahmuUVAEpFGvH8nPbKswiEie-FsSN8NXeRPhuauCVXRnWNo9MCUH7z6pWJisGhdXRfgteXsrGvrZpHcpZs6lBzCyD6xPBzPZ3vyVVAMShi-_NksxGjIPHyW47-w7kI436Tx_GEAczX9G_CjJdWc04RS0KgJo8SqXJg0M3kJ2VMUqoLF5OGiXIuC4D9saEHGBTL6DrLQfrke0oHJEr5nFe7qOYYUpvCzm2lK9CxaSp8Ycr3zSDiVwbQV1FFr1WUVWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=T69_pAOdyacG3F-KNaWeHO50z-XWumMpnM0chSsvUoSWZ2NLhFWl9Ozi9ja5PCLDkP_Vf1MORbozUSAV_XW65ahmuUVAEpFGvH8nPbKswiEie-FsSN8NXeRPhuauCVXRnWNo9MCUH7z6pWJisGhdXRfgteXsrGvrZpHcpZs6lBzCyD6xPBzPZ3vyVVAMShi-_NksxGjIPHyW47-w7kI436Tx_GEAczX9G_CjJdWc04RS0KgJo8SqXJg0M3kJ2VMUqoLF5OGiXIuC4D9saEHGBTL6DrLQfrke0oHJEr5nFe7qOYYUpvCzm2lK9CxaSp8Ycr3zSDiVwbQV1FFr1WUVWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R41MChaslm-jtSbuyR1JqS60AJ4E1kKXOdBRh--P1I7cu5-cBsDfpZcPwoj_zmgVE_tLDFLkHtdMVSDbnxKnKUO2YSVgRWsEk1jK96EdD7w3N0_M9Huk9w13OdX5cvRWfVXnhAUUhUohnYWDlik8bBM8p3CkopW_tbDgSY49b87GiKSJBMEQQ-23ErYoqT_rckZnPAbZiUp1B5XjgenvfNqigF7M5LKRfMpZbb0tUYOx2l6-nGLMAfmXBNvCNU4_Olx0PjkRGfU8Q9zY3MEkuUHzGmuyq_QidBwUzfQoxNDQ66jzOW8rcj4UGg3X-DBR1gXIeByV04I0HpatYS2WWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCUwHwyj8TCp280VxlNHkIZM6RHHdDGo4ni3UVbR0IGPwtjiobtba_mfnXf_MZVFgaBgI5G2J0FftjDPXEhIVoco6zmtlO7Uq5ilmvs-C_DI3WbilMOZtFWaCkpxO-SVyKhWIJ-r1ui2-Au-lf_xJWKITqUHAt_EciF8E2hRdMLHlhrvsS_ZG0psMARQXMcNF5SbfhWaDczaYb-tHqa9f5Ph9z9vrR5Bv6IijtvlyxHF3zgv9iaBG66oxeIY0h5CedkWofvd-57SskcXMfmz5mSTK71CYLllcvL_58Fd8V1tGvgPt0YGKYZEmBWwO0imqp2rPlR0quzAW0cS65iYaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=OGpP54xFO-3uWAsR9enjGP560iPkakib9u01et4eJXdVNABz1qAJmleekyGDHgZkMeV4NzQFfsqnbhjDFU8cYSDJltsEnU7nD3HHHp14pEjZuqVe3JEF1VOFOcg6quzPhht4IuGGGVKbvK_TZxaTLSnLWlxbIr_eWTSn4jjW8yrs3mK_byz_zuv2RQt5l1J9vc1Tpgtvh_QzqP3HguhJrLskEFGNInksHQd24z2ApcrAY5M7qDfMZluqZ38WdxEzdXJ3mDuSAcW4PGk_SgvM3cUal5EGt4ACxVlOeplDWbQEtN-QALnR53tG35vYQayy6PPszJPnDiMtRpuUMxcttiZtpIoUkbAPDOh7wDB4ro5Mml7qzJRoAsungI5k_SIbPWK3Nr7kFVoxKOOhrOpn-MvSgGIZjfktIrH_S0AGeHvK2RSPFN5TxpRXtR1fo5Y5RpZVoyml_1sgFE2bpxmiP6ARMvrP7iJ1q0DyuqkuDQ2XK9QUikySxVf9ykYqIjCfis5pZhkGXc4XwOH80XF7pZfFgWu7FbSA7qrCHR6cVfUiThBObcCF-bzRukSffhL3htaJnj7Zfk3DobE1bUiLnE634B1fKUjYX7akw3mczI32Bpu0_s_Qw9rN2gaCJp4iKNnHWvv3qLhdzUJDy7qPCDLEyvPgK3dc8BWcpKkSepA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=OGpP54xFO-3uWAsR9enjGP560iPkakib9u01et4eJXdVNABz1qAJmleekyGDHgZkMeV4NzQFfsqnbhjDFU8cYSDJltsEnU7nD3HHHp14pEjZuqVe3JEF1VOFOcg6quzPhht4IuGGGVKbvK_TZxaTLSnLWlxbIr_eWTSn4jjW8yrs3mK_byz_zuv2RQt5l1J9vc1Tpgtvh_QzqP3HguhJrLskEFGNInksHQd24z2ApcrAY5M7qDfMZluqZ38WdxEzdXJ3mDuSAcW4PGk_SgvM3cUal5EGt4ACxVlOeplDWbQEtN-QALnR53tG35vYQayy6PPszJPnDiMtRpuUMxcttiZtpIoUkbAPDOh7wDB4ro5Mml7qzJRoAsungI5k_SIbPWK3Nr7kFVoxKOOhrOpn-MvSgGIZjfktIrH_S0AGeHvK2RSPFN5TxpRXtR1fo5Y5RpZVoyml_1sgFE2bpxmiP6ARMvrP7iJ1q0DyuqkuDQ2XK9QUikySxVf9ykYqIjCfis5pZhkGXc4XwOH80XF7pZfFgWu7FbSA7qrCHR6cVfUiThBObcCF-bzRukSffhL3htaJnj7Zfk3DobE1bUiLnE634B1fKUjYX7akw3mczI32Bpu0_s_Qw9rN2gaCJp4iKNnHWvv3qLhdzUJDy7qPCDLEyvPgK3dc8BWcpKkSepA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=hYaYzDfqLR_E9XAdIPGNJVPtQPUzIXrSrFujpIiOmwzYBsLTNZhms0rYA3Uo75nfpdR4T9c4Tq8M3z-VMo0il1d7kGEqWLueFv9CNRclLtVw5_a3obaa3xcZZQhDVBDKGRnWlNbPz8qoUIQaBFXG1hBWU5zHoRzAT3l83Msjc0FjJua64cWr5oxDocmykSRn6BFmNAEzGYI--bUdchI2C6Y229s9zDuw_fiB5bpLtOuprPNBObM40GUFXZQUwH1jNA-zbH5-i80pJHQH5m7lglV0oqA8hMryeSR_FNmCCaS1cuGIIpwOvsOSq_L5ioXc-SOZjzo4pQdugBImT4Yjpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=hYaYzDfqLR_E9XAdIPGNJVPtQPUzIXrSrFujpIiOmwzYBsLTNZhms0rYA3Uo75nfpdR4T9c4Tq8M3z-VMo0il1d7kGEqWLueFv9CNRclLtVw5_a3obaa3xcZZQhDVBDKGRnWlNbPz8qoUIQaBFXG1hBWU5zHoRzAT3l83Msjc0FjJua64cWr5oxDocmykSRn6BFmNAEzGYI--bUdchI2C6Y229s9zDuw_fiB5bpLtOuprPNBObM40GUFXZQUwH1jNA-zbH5-i80pJHQH5m7lglV0oqA8hMryeSR_FNmCCaS1cuGIIpwOvsOSq_L5ioXc-SOZjzo4pQdugBImT4Yjpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/6348" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1MncdSM9s_17vFe_JGaCdR-rgPijzz8cnlGhT6eph4ZJg1vpzS4lf3MScN1QYnks0tYiG42Z7xXzfANJ_FQWjl_mSfLt74ZnWgihY-_dBofuUCiFypphasYE7anKQM9y0snxPojlCRmYdP1Rn5NYhut1m0jeyIvlmKTW4XZl661I5I7FoSpzRkC7CmxaLkU3cqatPGo-a5pFlet1-Tjs0IEGsMro0wZJP8yzR2ufY9an816Sdj8jaYenwhVa-dzUuV7Ks3-mXQsLTQ_0h3T3-jHkObvVaKmJnHOxMw64UyAReeWJKRoRjU9miCSjkbIBTwFES0Nxjwi3EOGDTPQbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکن ای پی کلودفلر 2
نتایج این اسکنر معتبر نیست یعنی ممکنه پیدا کنه بزارید تو کانفیگ بازم کار نکنه
بدون vpn وارد این سایت بشین اگه باز نمیشه واستون از یه
اسکنر دیگه
استفاده کنید
https://cdn-scanner-pro.vercel.app/
لیست رنج کلودفلر که پایین میدم اد کنید و اسکن کنید.
هر کدوم که سبز شد بزارید تو کانفیگای کلودفلر
با پورت 443 تست کنید</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/archivetell/6347" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8iiUDkQrDitnqvxECq9qmt1FYh9Q8qnZPUw0h_Ex6LIvYpnBugfJ0-2--dPqJeg4JI2SyhFwH__EUx4WVy4YeJ5D50G2B31C_-b0UpUV6FZ3jF-ncWEss8BwvSF28AwnkpPVWxPhA5WbDDAXA2bQ3OwHwkPE3_8liyziiIz-_nM3wJyhMuroLdQh2qzeCak2rp2VwMa0JnMKWzRvD6R7X3kd8gaZ3IMXvLwLg8xCZJKFHUaEMgIKJiLFvFb9AY4XqPPLFSzXS3OxEOmm-EPXCo3_ylJGachHcSPehoEJPCa8unhrKtPOQRtCAeEw0ODTPiI132YntWqCx4ipyjSQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M0Y6HAOuCoqzoc1J1I2_6-wp9BkUCDisaVUXn18RmlmDk8bRgiH4htXaZPHiUC99C6MSp4xdLNc-jDtsk9LePi6rBqFYrJh9xfniX7lypBuPCViqIQ3gaBsPwpSQylpQFrOUT2Ve8qJYguZyH02iuZgRSOy0a1LKMrt2DKATTEiLpj95H3u84uVkkjCtbPHYl4CMpSwYPM0qQzH_WOAVzgOdh65KK22G_Ma4OevVjEGsb2yIxKKem3IhjjGhMgx7Gynnq_sfPe8FRIDc-e2d7t-r57q7KDfhmFTmsptKIRNHblffw1mU2lbkLIyPXpN2PCD1zoQNu6Fx-9kCNmezjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/afhVzzSU6DXMfGfjueX_z9MBmkEifKyGFwShLGTR-zFgHUnR7efU9KcjIw5b1QGm4qcptN6oPtXshqzftVnoARifyjJodRSW6Zxbn5w373YONYoSoDSvjHyF3dFoYjuDv8eW4SkuQXnJpfD7NEc0TyOIS2NMP-60pQ8D8Loli1dCOWWTCXBBLPQv7AvIP6TlYFL0dfRoQBXFP5Cjt4TZLhUv0hRYbFkCJgjwZwR9S0ccBv9WxulzjJj_JDTRH3Pc4Wz4_P9AJ0zj2kjCYvLO_Q_sZd-Om5hZjAl2QO-Ya7SZ9b3A2cQ_LLwyoqFtohVAKacFw_1Pe8PaIeU-DI607Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k92kshabW8t_X43XZnEtRreplAhhGtLc-4OMZtnR_NUo4ifrgUZz8gEP3Wr1yZc2Z-rGXuWe1nd1U3Nnz6yZmBT3qYgp9nbyV-2geq69NNlJD3EDk0Tzr7sXEMBx5aiv2SvCmjlPcZCL5f7pmk61Z1g4ko_xReY_QXMfMNqvujHKaS9WFA9k846cc8mxCRmkN5k4B2qXQpOpN8vPfZL2e3ugHk53Kwgvr-7aPH4FGJhmK3vjnoPNiKErC2RB69lDq3pKzQg9v3_6v692WsLbRNGn6c_sg7ucjCHekftY4rHCIu7vvRgm3QZqL0PWkFFii2NM5pNhYSZzavu7t-yOPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">7. به صفحه اصلی ورکری که ساختید برگردید و بزنید روی پیجی که ساختین تا باز بشه
این صفحه nginx که اومد یعنی اوکیه اگه ارور 1101 گرفتین یعنی اکانتتون بن شده باید یه اکانت جدید کلودفلیر بسازید
به اخر نوار ادرس یه admin اضافه کنید تا پنل باز بشه و پسورد رو وارد کنید و لینک سابی که میده رو کپی کنید و داخل ویتوری وارد کنید.
کانفیگایی که میده اگه پینگ نداد نیاز به ای پی تمیز کلود فلیر دارید.
مثلا این رو با پورت 443 وارد یکی از کانفیگا بکنید تا وصل بشه
188.114.97.6</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/archivetell/6343" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxJZ5jzSfPuNxNxVHJNabPQEfOnPsoDBz05B0d50OgdlnY5Hm-bYpxDzeaJpznw4hyXLzbD1v0sz_y10z8RoQ1IVWe9NZ0HgxThfA3W59mpfeTTuV3a9liofEEUZsd3q2Io8lP_oPgyZImQ0luddpJ0s0trm_A6TMndJgLyOyFE97g5E8rotltCfBVBiG6cw6n9I9Ea6u0e1Aw7XUIud8QK-T8p5KjeLWOOQDZPCeGUeq6jXFTiFnywN1N6tU1xitaFZmLPqQ5lapMz9y_SLaH02tHQcgO4KkirELqGsih5rHSwfOoj1As-X3dB-elCh5uM4d9VxQa4P0YeI_cHT4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCcm1shOR5kJBhCZCjqc8B29k-cHcZMwKs99HpQYmveqe9dqr_mDZxFI8kKTEs3srLb318OkOhVQDDJMaX6bck48A1QbDCYlChPeIW-bmv98c3mnTanDaFOWMF1IT5QzzMKxZI3aZCwH-iulg16TtX_k1a2Ga-iaieHaE_A6le3Tx0Apo8z8-EC3zVNG_U94iuZond_vDdtD2AvvoVrETUUfs1adu5Dv0cdkUs4FUrqRWgYY7LRS5PpEocbetT_nb2rjRprJF33gxRcRzOMUTp3ClgcKWkZ1WY4OytC5GjQufBmAg7poJZiHl9Z_vSr03dhoAhPJIZrCcq4d9wjVHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoBPdEBCqi9rl9ztMCiYMkGG0C1rA0BnqpgvzSrlku_rmSof0RK-iADCgvKY0r8qH-gQV5Y1KmzFDILPlrHU7xJpgtTomMnFVcBil978MqbneEQ9g_TIJ5v1JqWirh-eaUB_0cpFc6zW3nO5i3fQUQaVfUSivWLNS5OL6TjATt7JrJ1iikUHW2cbGtXFOPUwZ2nwyNJ1FderNSVCLHGvOuhTdmbcX7iK8klrmcjqvOdVtY5HpPc_rXnWGyquY4Ill04YFfKsEazVOWbyEzfkvXDL02J2iogWj00smex7eTU8HNA09Z1TAnm2xrr13cBAsJ8Iix3xemVDgtdjNpkESA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dY1gVsBE_qb8BnE2uL4nqbXaz_hsqHx4kPSQUbAim6Tu8nD0YLPnPrFkGWghBi5-AOlX3gleRXY7i4RQseoepKb7W6ctbMffUModb9M6RDj0WBVoOlf-l4y4m4HBxx6x0uHG0kExS2OKeMqU05vXfOUD6UuyYMtrdIZrjkkORbM0LWx_PFuqD6XV4DuDnKFfTRtlVaaFHOBcNbbtf13gngR6aITjrKY2VckOk3fnksmWRTHCS0fkwg1glD9HLZXLXTIvwS9i9DmoWzegx-HixxYrjZCiKXjrYvHZFmDH0TiHPJqvbWAQPtf52e1biYZcWSqqLXQ4Pb4x-rxZFmBUUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyMRLPzkw61zCL-JKtk1GfPx6Ek9ERsZ_d6SsDEKvyp22zpe_VvaUnaTOswuGPHBU2hRyo0aS7aCQX3y6EQ6mqxvvNx54JttTxXmMbxiBhNwOSrrvQu5w0j44TDDYbMhLD9jrcMt7ac7IS1FkVf7SVpVoWclq0CqFNOQ6q70n3nvAFTSfBqmLywK92vIbFmLhhsrlTsI6nUvzp4ExNpfdeOmwv8kj3qf4pS2xGuz5p4XWG2at9b9kSfwA2N8NH2mvH53UfmvPXD7XmazIKTY2Ni2AoqKr4DFwBTn0nzBy2LRFWMGl0jUB6JDSMMBaTemjWD0Y2smTeNEbzYIVlfKYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZzOvvh1y-xjw24uDa1W6oXEYjztgYx8Pm6EIxxS1tqbNdncvJsA2_jV2PEqPIdAG3Srm5k2uG_rVuwNxFjXWCHNfuvjdTkFV0U6mvRB4V2qe6RvHAbnUUBn4pJZwxavehiL2M3EMnBhuSq9SCIWBYC0XyFRPBjtyRJ9iwqNLNM5V-ubR-qzEoshakzO1ukI3riDAHBmr166hDcDI3IfxhpUZZwUUHMhW0o4QqxRja80xiSMW1XsrwKK755jxdqqGX8E2GwqUfDnUUcx9BulanZ2Sshx4VeELhXzsDrktSETM1q27GI9ydCdGuqZeKn7Hm2ZW0H90veZAN0eNwg5Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RowEGqqdiuoiVzsPbGKSLhkN4uA9OcM54MetUhD1P3C2gj2atxctUX_NpZ2hcl-G0HE_kyx7xG5u2PFivaOs6fhE4owfZUSAyoA5dRpngu4XJ_zdsxGM7afgmuWjsbXfStmkXCDO5iOxNV1l4E6pCksRuRBhgaFpQXMU78HbSK4Bjtn4TljYxbSrrwxvBtc9x2o9vLuPtwAt9R9HGy5aTwFKDFg5HkRfgCa00CKwG6_jNc_QRXMyBiUd-ITmiqTXBHIC9yg9--HxAkJlp-4Gg3xpNnv7dKReIVp4Ko56Tc9DXufgs7ZHrKZpmaEKfAJwd52je-ZLv-Cno-GtqryIXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=Nrnxjaq90cQ-rZXB3P8F4ZLPueoMcgIzlnTg6rPzIKCay6i_T5dMvEtOKyN4hLNWCg5v3krQZNxDgr9n6s94usZ5ubh2DSC4fyhOZl7rS7wYnLndiA-o8ht4PMZziAPJzvUGJ6KTlkuYKGBUXf2yHmjfA-5v0nlQu7-KA_zo13jiBl61NDZUvf05Q71efee87NmsszZv8NIjg0sqnV_9ljXjlpCnrPMWtMuy_2jvx1OzjuKcObYmil0XwFnvW5ALTEWnsO0ikNvZVoDZihys5AalUyypAeJLZPhpewtY2iMLC6mlULjxwVwZSFvX_acnu4unzXqK5cbl682SpmgFcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=Nrnxjaq90cQ-rZXB3P8F4ZLPueoMcgIzlnTg6rPzIKCay6i_T5dMvEtOKyN4hLNWCg5v3krQZNxDgr9n6s94usZ5ubh2DSC4fyhOZl7rS7wYnLndiA-o8ht4PMZziAPJzvUGJ6KTlkuYKGBUXf2yHmjfA-5v0nlQu7-KA_zo13jiBl61NDZUvf05Q71efee87NmsszZv8NIjg0sqnV_9ljXjlpCnrPMWtMuy_2jvx1OzjuKcObYmil0XwFnvW5ALTEWnsO0ikNvZVoDZihys5AalUyypAeJLZPhpewtY2iMLC6mlULjxwVwZSFvX_acnu4unzXqK5cbl682SpmgFcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
- لینک سایت در مرحله اول  - لینک سایت در مرحله دوم  #GPT5 #AI #API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6335" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMpytdP-a5tayeS4S4zhLZ4cqB7KKv7obO74zsvTb5MOjEIydYYd461JIH6rkmm1-PW0i92uQhmAWr5iLV_3Bickp8EtJlGMpuk1qdRs2BlevpeJFX6j7aLIrzn3ZWGyzFRtzYGmE82y8RU_hsc9QliypokgOGpcVo96giEQue1sfVupwGbK77vIQSUj0uzNHh-DeiTC4Vs2VVzIXO7JwcMpIogApXS73q9NaRAuR1NgjYs2zDbhMcZLQhOXJ3oZpdSmTjAamgdji4pI-Od6CKZRbrKTddSgXd97qkdcF49uo7_WS8DDi60xvNyBRx8ZjJw0KvX814vRrmZegzABrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X90EcnrXEA5DehKh0u5cw6KKtzxb3U7ZfkFtbqRlD3Cs0Cyq5RxoSunoTXN-rc0X-qtcTrCV8wU5MYjAOSb3L6rZM2R9pNqBjRXznwhL4CKKtIxn6S7siGxHQhE0C1BzOb15xO09FtkcqNV3GZ1va0VwRJT2emXJWJLSnut7I2_WVPBs6W37khQsTpY0rHC3b87ky8fQ8mEZRi3_HhE7uwCmgipT7zXY4KNnylMg2fwGqalX6BYuy0bD3gvCnIFW05FxvD4cl8zrAI6zG3POMMfddqbDmqZSEMev-6ML8Klv1biXFISpPEMFQoJ_ct4io7_VqT1hxU3bCUsdbOflig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
-
لینک سایت در مرحله اول
-
لینک سایت در مرحله دوم
#GPT5
#AI
#API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6333" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ghs3EE8GlPl8XcviBiW-L4HAg0yDO_Quo4Q0ldWncqBCddLCfsC31nbxAuYGAF6pWOt2zjAr3C9sPF-gJtYo8pFfpmUJUclz_7kBcT_ETO0y-seTKePgN5XnwHxEvOCOHieoaltvAwBKRQDwlK9GBP82MdGuMQ972pLO_q1j67qiPDOft1wtETErZmcib_TBW0U4aSPl8N1Rz6wLHq8vsz0kX9ZNoE0A6glx09M-szLUweFdYdaFMvswQgTGriHvMorcTcZxNXjAgV3zC9zqEuiGSg6rRNREY3X7ouLU-pQ4iSA4VlD3nA8CMrjlxOPUBt981dljPAiP7tdiUbq0Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3dA2al88vJdCKlxvmeAdDJjxz1gFyLKjvb-VflYWRfd1SWoJXtmUBWPL3RXdU3cYtyJ8wEidniPemSDXPxEyVmAPkWd2C4Q3ckLm5OoEIT1-9iWaqbN4LT-0Qv0I0iiHOgDEsOGt9DV7bFSEnBL-sTkpHUXBVJTqhomHHgP41y2SHNR8rfHGcPxbrGhNyEaryd6SCq7Lg04EX5gdfkEs2kuAfK1EKsXs7HGAHHMD4wsus0hel8UKWS677IEUIakZHbaud3BmadKLP_O6_4V1Q9qb61VsHb6WEm7ceCUV5ZUjOKSsbZjpYJASPFpbKF6I8G6xsL1YYLP6kTxRGH2FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت بازسازی عکس‌های قدیمی بدون از دست دادن حس نوستالژیک
📸
Repair physical damage on this vintage photo: remove scratches, creases, stains, and tears. Restore faded colors, rebuild missing details naturally, and keep the original grain, lighting, softness, and period aesthetic. Do not modernize the photo, oversharpen it, change faces, or make it look AI-generated.
#ChatGPT
#Prompts
#AI
#PhotoEditing
#Gemini
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6331" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=dAvjbmk9WQJlXyXGKKrgtwgY6N_tN1Jno9jtlibZGzAh7bDoYxrmPcn8hNSdHBsJ6C4MdoSIotzHcgz_Q_S9sgflMY57rbYfg-SJ3e2w0Y39I1_jhuu6qUbE6YkgAturXV7mRLHlIhoeyF5CcfDjVpuS-4VT1btfLuciXRHi-013LjP6xqxbl-iQ23D3o5b8dXjZLvTsffrz_Dn4GGlnBu81tYCTICbtl17cCIVru-WZ-UP9B0RVNPupZJWrxnJNSOxK2UF2QIxhnQi4pERQDvZJU5tAOyVyumV3UzylGaUk0aJU7xcjf6REKZ517VH_QDHk-YTQKE57fYqjdu4Ksw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=dAvjbmk9WQJlXyXGKKrgtwgY6N_tN1Jno9jtlibZGzAh7bDoYxrmPcn8hNSdHBsJ6C4MdoSIotzHcgz_Q_S9sgflMY57rbYfg-SJ3e2w0Y39I1_jhuu6qUbE6YkgAturXV7mRLHlIhoeyF5CcfDjVpuS-4VT1btfLuciXRHi-013LjP6xqxbl-iQ23D3o5b8dXjZLvTsffrz_Dn4GGlnBu81tYCTICbtl17cCIVru-WZ-UP9B0RVNPupZJWrxnJNSOxK2UF2QIxhnQi4pERQDvZJU5tAOyVyumV3UzylGaUk0aJU7xcjf6REKZ517VH_QDHk-YTQKE57fYqjdu4Ksw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
ClaimCircle
با یک کلیک، خبرهای جعلی را شناسایی کنید
✨
قابلیت‌ها:
•
🔹
تشخیص خودکار متن، پست یا تصویر فقط با کشیدن دایره
•
⚡
تجزیه و تحلیل لحظه‌ای محتوا و نمایش نتیجه در همان صفحه
•
🛡️
حفظ حریم‌خصوصی: پردازش در مرورگر، بدون ارسال داده به سرورهای خارجی
•
📚
پشتیبانی از چندین منبع اعتبارسنجی برای نتایج دقیق
🔗
لینک:
https://chromewebstore.google.com/detail/claimcircle/ominadfbilailbklmclcmdbpmckckdad
#claimcircle
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6330" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4JaQQd9kuWohAJKuhSHpHdrOYwzmGd1xTwLr_UbpDyBw5cIwM5iLIDCaW72w0hZ3trx_PVfWVUcQ8ww6BXb2mYlANpdZ-MQ-qPeiDJZSBXmDiUcOyflYiSqly_qHoJ34WXnlUZw5FcBRb2nncguvE_xLLcCBsjEFxOu8Oiy1bP7y4rRGZM1daPS45lKVTG4tIaSMK_voPOV_uZ6LlC5LrgmNSokccKisQmy4o-FZhf9aJAVFk11-tOF6MTqWJcwD3wdY6_jQolGwiyr5ZJY699BR2MF2FOHEw_W5SZg_Jxmn9TPwVCjSudczM3mZ1GDPbtUoe81MkpygiEZJKIPyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
پخش FLAC با کیفیت lossless بدون محدودیت!
✨
قابلیت‌ها:
•
🔹
دسترسی به کاتالوگ گسترده موسیقی از تمام ژانرها
•
⚡
دانلود همزمان چندین ترک با سرعت بالا
•
🛠️
ذخیره فایل‌ها با وضوح اصلی بدون فشرده‌سازی مجدد
•
📦
پخش مستقیم بدون نیاز به سرویس‌های استریمینگ
🔗
لینک:
https://flac.music.hi.cn/
#Music
#Flac
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6328" target="_blank">📅 21:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">📢
جدیدترین قابلیت‌های
ربات وگا
را معرفی می‌کنیم:
🔗
قابلیت AI Agnet در گروه
🔸️
ادمین باید از پنل استارت ربات در گروه به بخش تنظیمات برود و قابلیت را خاموش یا روشن کند
🔹️
با این قابلیت ربات طبق اتمسفر گپ صحبت میکند
🔮
قابلیت خودمونی بودن در گروه
🔸️
ادمین از پنل استارت ربات در گروه به بخش تنظیمات برود و قابلیت را خاموش یا روشن کند
🔹️
با این قابلیت ربات بی سانسور و صمیمی جواب می‌دهد
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
⚡️
Vega Bot
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6327" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
50GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 50 / 50
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6326" target="_blank">📅 18:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XswcXVmXi7sGOlkVnlqIIjDUoo4HVIThLdB2piH3wTsjuiZkwLsapA0wV926Jhmx9hFSyDNC9eEXD81DaVT-XoiYSKmDIbyIRUQu64_JOKPfjCo63oehDd9UF0JKKHferMR4XB1ji-54fJ2QnZDOiKz5cSlE5ELAUDxQxjLzw4-EtaJtBEHTxKqGrCWWMYRoVbWrWYyTWQ-NhokcukSEKnfbHvXs-eCsXYOGc9n7s7eMsRhNaZUUNQu3mr_av6iBFC7wE8ouAfOk47ns_lNI2lkqM0Vi6M0Re28vJLTiU7HUa2Oo_MbUxVwaQtdESwZYr5R6IiHCg0UWftbF3GHtIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
تولید انیمیشن کوتاه از متن + عکس فقط با یک کلیک!
🎬
✨
✨
قابلیت‌ها:
•
🔹
حفظ ثبات شخصیت در تمام صحنه‌ها
•
⚡
پیوند صحنه‌های طولانی بدون قطع
•
🛠️
دوبله چندزبانه برای مخاطبان بین‌المللی
•
📦
رابط کاربری ساده و سریع
🔗
https://aianimation.video
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6325" target="_blank">📅 17:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAzQliA3dUhzY19nUkBafsJ_n_-AF92-588qmtr8NaI8Kp4LOC36A16NJ6RIs3hMnGXBu1C9eR7cgMh7pvxKmuHxjcxRY611ttweQFmjxqD_sGKqyvQXRNOkNn9YDAniDkEHFj3JfQJNLF8pfxCUEvwSy-XohMVFHwWJ7zsWX6Fqq-NjQdLVkNXiaAgIVH7uosX27EYF0D9iRyQKIiTckztncFvsnJ_Z6vXkr1U2bTXvNlAB3iQ1qu1VAWErNFW0ybSMB2SQD4jBnVUe-bMVwvMqhNVViYb5uHa_nPfspGI9nbRYwt22JhpMDEasEAY-QSTwJ2n1wtF1glAfO6W-Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
تولید آهنگ فقط با توصیف متنی!
🎶
✨
✨
قابلیت‌ها:
•
🔹
نوشتن شعر، ملودی و تنظیم خودکار
•
⚡
ساخت موسیقی پس‌زمینه بدون حق کپی‌رایت
•
📦
خروجی با کیفیت حرفه‌ای
🔗
https://memotune.com
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6324" target="_blank">📅 16:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFVniX1MEuKjKKMAxYMvn_vssKb7zipIGsj0RULLRj11Un_NvJ9J_maI1HAueZ2abBP5gAfwlReGg07Io229u2f9OpmbdQJlP1W7JLGK3b6qzlB2Hh3888vteL6OGwAZerkamVnmjYRoVuDn46xsC-g4EVxTiTnyY2F-WiWzmUOKo9WXG_c6S2hLrYHG6g_DfH1KpDsQ3GvcT6urt7sa_zBcgP3tLn9hfjTDelTZE2OC90IaJCaHJPMWR1kXq6Ugh12brTsRh9HK9jEJHrdsXZjigXycSsKHWDHyGkADPNu2GzMnmb7cOk1f-8aV7l_aY3nm07dlbfEetZAaK7BDxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ویرایش تصویر آنلاین با هوش مصنوعی، بدون واترمارک و بدون نیاز به دانش طراحی!
🎨
🖼️
✨
قابلیت‌ها:
•
🔹
انتقال سبک و رنگ‌آمیزی عکس‌های قدیمی
•
⚡
برش تصویر و حذف پس‌زمینه با یک کلیک
•
🛠️
افزایش کیفیت و ویرایش دسته‌ای سریع
•
📦
خروجی با کیفیت بالا در مرورگر
🔗
https://stylizeimage.com
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6323" target="_blank">📅 16:08 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
