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
<p>@archivetell • 👥 9.66K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 21:11:13</div>
<hr>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 795 · <a href="https://t.me/archivetell/6441" target="_blank">📅 19:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/archivetell/6440" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toRblf6LXipOrJYgCA9hIWd690ih6Qi_ChxBRqG8l_AbJS63oxNynIO1vBIWByQqELE4sF8mN_EcO5Dy8V07Lgo29EcJgC0QLK1F_CFSmVna96G5A9zq1RrwaZoal7e6OO3c10Y8QyYkaEAG8nR4bu7ZtqaAy0fAiIyMJSmYWrGgAxwJCowHmbrygItP60BlB7R_zZE1obcF4W55Ap5Hp7_zFOAWN5ZiuWh0OugPx8DSTD4PpgFV5F8rSNgvPck7CIe4V49fLHM6vfcWPJoY8TXqEtsVuhCIw7IuA9SKTHZWhfmWG0Ed9YdtWYEuGgK1RmeyIQtn-ozxbSnBgzFZng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
راک‌استار از کاور رسمی GTA VI رونمایی کرد ، پیش‌سفارش این بازی افسانه‌ای از ۲۵ ژوئن ( ۴ تیر ) آغاز خواهد شد.
#GTA6
#GTA
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/archivetell/6439" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6438">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/archivetell/6438" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #96</div>
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
در هیچ‌کدوم از این مراحل نیازی به وارد کردن کارت بانکی (Credit Card) نیست.</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/archivetell/6437" target="_blank">📅 15:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/archivetell/6436" target="_blank">📅 11:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/archivetell/6435" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/archivetell/6434" target="_blank">📅 09:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">با سلام درود رفقا میخوام یه ربات open vpn بیارم
دنبال پنل درست حسابیشم
اگه کسی پنلی داشت که بشه حجم و کاربر و ایناشو مشخص کرد ممنون میشم داخل کامنت همین پیام یا پیوی بگه ممنونم ازتون
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6433" target="_blank">📅 04:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6432" target="_blank">📅 22:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6431" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6430" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6429">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6429" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6428" target="_blank">📅 15:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/archivetell/6427" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6425" target="_blank">📅 13:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6423" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/6419" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SIZ58_g37XWXttZ3aqtZPRGMfKGh0EJ7eF5dXer_B0w1rlFDCe7cIfYuD34YvlfH8eXIYoiGvBcL8NuB2akgsoFLfE6Apv3XnYBnUc3IrlaQS93TBlDH_YLMMCb1I7lwZsR0StSkcWdG7bAOWnSmRF92k9TD_I-5968P9m6Vhh8-c1C_eFg-HunBZ6BvgPmXd1FQOe7iHRswAbvo1JBI6vjJbm1uSAFqc6AOOz2PXNxDtptdi-oR5X6d54ifMF42fEg6IohQzkPvhmpp8McGYzfywEsVdIkqFc2us-khwiL1TCxTU-7W1DEaJYCHbGfaSWuYbyCTXUCy4OYAht_YEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SizVMLw7IBMxE-Z000X-n6F7hGPT3-VujXLSFD8LrBPZhiU_1EOq9B5CF5DZFSxs87LNe58FpjLqwXULEZSWCmPQerbrX80e6pMUJbAt5h6eXpcJanEPkQwKtbOTZp4tTxVYe_jZhjw0JvQSV8MrJ6y_ZxBXOGyDQXxFgKej3KcGzQoBskexbaPd-eQujCe3LDo0Zmhs1fzun_-j5HLUDqYQmlayDTMpfLnagcxFO28Ugkch5DZzjm_efDyg84_MWqCFNT9cpSznFl9lLVMUX-5nEHvGNBr-YWmgUbzLODqX7SY8GQ2ffAgcoR6avY6Ig5xxz1gDrY5ngQMAwuAj9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6416" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Heybaat.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6415" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">sadra.ovpn</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6415" target="_blank">📅 04:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6414" target="_blank">📅 04:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6413">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VBbpRy-TeCWfLLNwJQgL8FhjxuJLpSgOdlCehybnK4FkeCoLpLrV6Ut0j4I1SCQDFHsKVLU_5ZxsGlw5FrNau64Dn1u3ip0fu9g5i9fjEK4kdWajq6t-d9uFLE7by3XXcwAq5c8W102dtmRdlG4bUz0p9c1bHrVMXgflFgUBZEF2fmda3QjWk2j11avWWSvb7H8k1vhZ_Fhl63lAkHK7zF5nos4F2UYbVH8AH2CZZfrqA1RM08O-B2gMElKr7Fa54lQI3JkknynB5fQpbe1X2VSq9ZBGKwh8ZcMnjDXA80AHvc-pp294c8mx-DOtecgwn4RFHJnS1DaEjmNQBSN1MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qHEwgmAOsjeefdXAbvj2Qi8Pu3HzLT9gt9ftELNGK_ZN6ODCIsKrtLeobB7UIBOXCaEmOLCsjOErM2QqEsX1RKVgtx8HK6x45dbt6HwcK2Uz13Sf9UaEFG89rS3IhRTPi71V1HFmmBrujweYy7oBCDR4jx_qKXdIN18U9gYInO3bSabYLj9ao8hHx5GeBDCDFZt6VEtYFlTwCaL0ntdVyFoFTJShTyNSYEGwxDNnlx4Y2O4lcKx7pf9D1V0OdCg4fAU13PIT1JrX2gpYN5MHuNXJ0h7d43X_Ab3NCL5tfuFXjx2nI9LaNH2NkuzCav4RPUE8LJRgqyTV7Daea-nn-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nzHGtyuJkCpAQkgKTccq59FZMO4UfFF8qBYnU4XitGYct9ImeVweP7r9xcBomIS426EH6gAlRJWcjURM2tDNb5TMZkVFFqYk4VtpVgaWkQ7XdE5CTq5er2hQxwIHXurgmbv8q4G7Vby1cKib1Q4N1OmN8YKqqGVM2xUGc1tht6FeNhV1UwZGepXI0ofc3rcEMw-p-Q8b1J9c2heOwJX1nO1Qu7-v8RXDoLCfhngvQN_eg1De9UfInkaoWd4nkR-v3JVk9ALQ7ihgzdwzKR7W5uLxdNr8nr8R3yTYC1zNpWX8z7F62jJLO1goQNuSqtNKCw1fsvzkmGTpw3v32T0K0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BO6IU5tEKanVRkfOhZVdRhQHeQMklV_VmyfYFKGL2i503Zuea5wn99sISf2-36GCwKqVKnGN24VMJvIjEU699i8Hd4Mk8kzioQ1v8RyTg7B-QivHt8fBILqJ_FvtjVJ3WMEd5AADq4hWaClSwfKumOay86t80IWyZ-DOhIEurICUSWESaP78yFQowWEb9rXS-myd97ep5stDc-FTpdAVCyOl-JBkbTSrTy-2bVhzXOiZtBRJ3t-4PD3UExxOUVR6JWkImIDZMumLuHm09lYMp_kspCD-13XMo2PNg5KZgZqsZLUOreKtKG4PryE1A6he1g5UdBALFbw8L-Gu1AkLZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت تصویر به‌علاوه کتابخانه عظیم پرامپت‌ها.
- طراحی‌ها، تصاویر، نقاشی‌ها و راهنمایی‌هایی را که توسط هوش مصنوعی و هنرمندان و طراحان برجسته جامعه ایجاد شده‌اند، مطالعه کنید.
http://Arthub.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e186940244.mp4?token=iRfBZfecC-sb-1K2ijFc-m0_a8cSm3zrjcwOuQQ49eWjn7yLhJTTNKCNGKhEEb6LNqWR_rM8eiJt29stkDwUObYPGQFZkhrGiL0SpncBMh9wmL7WJqcpTxD1PEqfToBdvUghAYPoSQduM7gVDfUkyK10hr8Gmztp1rhxqatSyKq8QzbdLPpD4QeUFSzE7mDkpmr4B7Jsy24yX7_VDy-AWGc9-V-Xprft8Q897Oy9dEKdlRFTkqPnL-nXJXZoFTuMILqMJX65t2csqt8-UwrcmzhCWsUHpLaa7IaCt5aoHp1zKP6fwZsBihMAiBRg2xDLqZMGdGwE9tOyp5AZakbUKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e186940244.mp4?token=iRfBZfecC-sb-1K2ijFc-m0_a8cSm3zrjcwOuQQ49eWjn7yLhJTTNKCNGKhEEb6LNqWR_rM8eiJt29stkDwUObYPGQFZkhrGiL0SpncBMh9wmL7WJqcpTxD1PEqfToBdvUghAYPoSQduM7gVDfUkyK10hr8Gmztp1rhxqatSyKq8QzbdLPpD4QeUFSzE7mDkpmr4B7Jsy24yX7_VDy-AWGc9-V-Xprft8Q897Oy9dEKdlRFTkqPnL-nXJXZoFTuMILqMJX65t2csqt8-UwrcmzhCWsUHpLaa7IaCt5aoHp1zKP6fwZsBihMAiBRg2xDLqZMGdGwE9tOyp5AZakbUKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBn6gU0ty10HSUvQFleb9gizAdC6Zpns9ZFaEmnCJjF1wZ-6NqD0AFooS9lNnQgdtd9ShuaH0bJs7e_Re2lI49aUNEZMNWVB6YU5W6LxdS6WfdRL3yDBT14Y47x6wRLDsQiJFUpWukyEZS_845tEiuwFN7GtJ09YgEWgWo2brqwRAOlJ4M78KLkmFW1hMQ9giFksobQGQ3aAONq183QBRTyLjFtvpm-dgP0StFmQt1oePfpE47PUnjgSONXk9dbyT9q1IRbsryUFF1A9KQYSKo-W-ieV6MFeiWWJFep7CfPyk5QtSp14bpz-crf5SorOI5d5uS23Zj9yjo8fRwtlZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087fb590da.mp4?token=a9YbSQBgll14hwnLg04aR5Z_sUJPRcZCVw7v37OldcZ7NxzCr6fs2dgc6PbqNqY8G-DBL5zAckTr0Og6gNdBow7acSliEk-VpIlw5HMiVlWNSSudsRyquahXCTBDMds0zSg1trJU4-jfoLE4GmHYFb3zplB8STFTbdPLZt4fqv9InigHXwzDpZidCFXiSeqr_azgh9DMf1v2WHGMavqjAZS2totQilz-7Vef8AkTmz6g1xZiNZfE8UmEj9BMI6WqTw9h10AsBJQG12hl1R7SLNOL23xYJLoKDu_ow-0LWwOpwYK0_EmW5rknbBtE6_7SnQjlEGp-A28ngyv-oZAL2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087fb590da.mp4?token=a9YbSQBgll14hwnLg04aR5Z_sUJPRcZCVw7v37OldcZ7NxzCr6fs2dgc6PbqNqY8G-DBL5zAckTr0Og6gNdBow7acSliEk-VpIlw5HMiVlWNSSudsRyquahXCTBDMds0zSg1trJU4-jfoLE4GmHYFb3zplB8STFTbdPLZt4fqv9InigHXwzDpZidCFXiSeqr_azgh9DMf1v2WHGMavqjAZS2totQilz-7Vef8AkTmz6g1xZiNZfE8UmEj9BMI6WqTw9h10AsBJQG12hl1R7SLNOL23xYJLoKDu_ow-0LWwOpwYK0_EmW5rknbBtE6_7SnQjlEGp-A28ngyv-oZAL2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsByn0jOytaZ2RrbOVSDQXRA8HEJi6VSNmLz7UL4WbBaAnX8k_ZIcSjEdOfjg7N4-Gpb10F_nf-VZjfSLttCGnnq093iJfkc1sAHAvTqEgCCU7f0ZQ3OQlEoXVMmckFPOVXcl12d-FuiDDCmG2IZAj9YoCA7HmCNl0mYgeO4oXirMiNpDlRGPMPoLbFINPbMhgcQQzi8FPFgJ5kX8F5qUAUJP7TcKj5vUbsQaE7rOjIVHJP84191Vk6A2NonAF9s8RfnpFDLqyuqZJNbM8XjimGYjNJ2KaaM9G8DXWeK0IyXeFBVQk9pBynzS9nfs_AQOKvKaRHi9XMRwrtwfw00UQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r3j5NAGaFRjfBnDq0BnPqaUr3fX_yeoCBAYHewA8XGQMCMQqgfZu8xzf-_pdh86e01rH1s9L1k0mC5-Yi8nDzpBvsr1phHOK3-O3EEMKMGfNJCI4l_JkdkQKZPKRteSgk7E_v-VO1etLaW0y8SMZ-sJzzcnNYH_WuCB5LO8GY4GOdIoqltSHZKK6FntBh0tHjRlfLQ0Wgory1jXx9x9FmL1FzZ28hUJivO8Nh-mU04uwTZqBUvJUULQOsPpiuuTcz_li4pPS7tjrvUzobsCc-sh0MQvZ5H8SupnBgCKOU5gzb5M68h1N1tnX-A1q_ahEf-ftCXmCr5B03ZHfhATfOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت Ponytail هوش مصنوعی را از نوشتن کدهای طولانی نجات می‌دهد
☠
این مهارت عامل‌های هوش مصنوعی را از نوشتن کدهای طولانی و بی‌فایده نجات می‌دهد و به جای ۵۰۰ خط کد، عامل می‌تواند فقط ۵ خط بنویسد.
با Cursor، Windsurf، Cline، Copilot، Antigravity، OpenCode و Claude Code کار می‌کند.
https://github.com/DietrichGebert/ponytail
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKNdGpeTxKYTQRWS03AOHkLolmT9-ejI7Mka9z7FbLlkeR6IWJvIfBGn5HVbuFje-fJLH1RW2n2dKKk7OfeFcXfHR15uLwRGfQ-CHsP6xs2XGg8xirfGfKSpDzTUSdgunPkQ6bdQwsIunz6woOZ47TbwGgyak3xQGrBrFRqQXyKwmAi8vkv6wZl31Q_NjmN52Vgj3McAy_N4WXirMtIagLnAiVCxmVhCRl2UOt6us4Z5mC4_QY-oxh4VA60NSl8n0n2qVUx0syDlUbOo3JvIoncbhsud1w2VG9C8x_3rEXi_6wG7PomoD35vcYXrBGYQ7awq0m1_rT3b44tsLD2wUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
متوقف شد
❌
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyU1JdbMevxrrP2hlosWdimCyVGEI3GUl9a5yJ-sH18MdvR8KpzK-BDb8XO_tfDOzvb4jV_hlxASIciIJvQUG2KkIx00iTnmBcZCCV2u2n8UeGN-kqyXKYI8gt8eyt34DtPfsCNRqlibdcWdyH6fCT4CVVeH_3HQSMz6szOxWOvS3cJG8Sd5eaYcR5bSRINAntU1l9yuqZ7bFeen0gx-VcVgl7wzQJ7NBOLulYerWa-ZgzIR7K4r3iJA-JNGjVpI5U8XcyfPHeszMQcTEpZ9mEh8drZwmry2YU_TuBb73UCxoXmkn7Xf1J7Mj4CxnOH2NjrTOind2EUC9h_L0wTDqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zdo-Nt5mcracydHoBKjx9p5DWuM-NmUu_bMF79nfBTJrmuVV3uYAzYyG_w92iKWk0mK6Pswoq_qjvPw88547CcG-GgyVNk87ZYxM-VHFK4uyoH5gwmi9q0JKqVvFGLOS88AF1AiJCHcYumEBFtnprBdHAlgPxtfHmyTTiqNA5RKYMHqh7aZ8b72f5C5c14_tsTtX7zfKZhS4PvbpMiN8sddkV4oQgruNK7ut2A8jTZXTv0i_n3XrZHRvqR9qGd3BWEcJEFdY_zFXhC_dXDYMoe0SzDz4GVNjHwQaRehVua9aef_PDM4GggYMlAp2wjymHCH45yNalFxsnktnJoxn9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZ8TIWvgHoenRRdm4FRqsg0A2SkOiveBbxLv2kHPRaBw4WZHp2Am2gAI-hk64kWwjlZjOjxXkr3vBxwA0cxglmo3EfUTnXrPaWQG6bNKip-exK9JKFNmkC0I4N2jnew8e6F9K9QniZRVDPA8VPai5tAziXY6oeOoCXSyYF1vPzwyz8-5x5vJUyVYmByTjwF6h_UQvUnLiZ5C1xTGJ3btAU9qdwxQdjXpKBz-NVUqyRkCavM-1qL1CBIRs6FtXFU4CcU3RwldoXvp7j02W4g_X2Klnk2UbeLoHn-fvgngEcv4NQi7nYAIQHkNl5yq4sZ_wnB-HLVlzIndQ00mBqq3Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mx4JFtyaBYudeCdC6KUx3c90pVH4-UjC4CQnJsrm2NNdTeV-zTPljJ2N0F2sl-bnD5DPGZ1bOyjYQIZyTpbumHswUQxPho0fuImun1RC5NztUYaql2Y1QAQPWvdaiQG-8DLj8lKMNZtoN0y8lhSyPCMuUYygWte7u2OaOm9kjo9woX-ZWeW80yU-Da_M7AlVCbfsOuGAikWkMHTP4or1SsE94bXEXMIjihLcQ9cRsmjXSy-O3f0SXVUJhgoL-KmRNQquJcUlgshYuzQiMnLJFfcy-BlBIZ_D_qVOUCXpAln5LKJjr550_C5VhdoRlS0-d7HoIefV1glBScdTw2joLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEhikv7k-b6e2A3oaN9ITx261QRBw82ZSMJA-K_k1CN0JOyj4dicMiRvi7mx2asBR3fYBm4H_jjQNR-JqxjKtNr08W5TDbEbMSzqLKq1MAEZfY4rdVVR8KT4fm4hhUycub1SjRFXqWV2okIT2vbVRcOJO0PMk2r9ZQgD6fTyVzFj8UA1mufgz4PJS4F_EFQCdSdEkc-LkMNH_4VpKJ5x3JKs1ryNhyKkctjk2MmcjGBWMl0olW3DsPqJHOtjN7mKKbU288c-FmxxyqEzWeo2Qt-hXJvtbUEtatdzWtSv0lbwlji2xuqU-d29VTP4AYdKgvaKt0_KKS0FIloJ8Xg77Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b97X0UAw5WLpMCAbG8xNutcH4775MYuim4nLOlMq3LKa6KcX-ka_RqSxBf_7ZTG25EEcE6IjJneHyaJExpEls9unR9CwJNVWDnvW7n6PYnn8oypAlR7MB0khrR9vcYYEKVl2IoaD8NR3c2hn9cU-wqGUj6xeBGYlmHcdyaMDWRqLgBUrAQRRgSSFXut67d8gRryKuM_lS0_s9beOmqNgQ7wJ12oQ3e5cNsSN4T204FXYYNxb3moOmxp4LXqHnAmnarle1afzSLTSq0LtFv4b9BY_6mY9r5XLiLIwGVL1id_xc7U-Q0iKAmLopfWJI4z2AB3DflwZb_0cUOLYVzgh0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFyq8Doj9q-b_8Ivs6vuIXE6C0Ljj0--2Cs_ZY0rt_smmorhuZ8G1LIxFNZI9024Ze0HXnf2QJq-YUJQFSm4eaocz5GxcqWAi7NlU990SwqUL6npjepLLJrsjvd6o-m2h2z61wAeSzL0s7bdel4WDOvTCPh_551p5zKndkeAJzogqbmVXJHKEmS97_cQW2SoUpvyxMqAfsekJPttg8lN1M9y-hKVE-8iZOibHvWyYzxpJePALBLbUXvrMXA4uXbBhF6RcFyKx22SI8WPBLwcFUMOu6aMho37-YElxegFIBEcU40Otw737fxXW0u9jLV48IGpjgQVMmPEYHiANk6EZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUMpVc8V99IqJ0MM2hmWsQMld9k6eYTkjEOWAv3ODqUiqhOX87yIrp83lKz8cZQxbjzUfnsVinLiiL0mrbSVa5aXOBoGsp3e84Ef3mz4kydh_L2t7vLv2Z2iQXXCQ337zoehexEou7rBj3zJeCoxsGYHcGPFf4_znLB8RELmw6aj0sHMYMqIqfm19YmEiNmDylZirRTk5oEH78r5ODTQHlh4XS0C4Hif_g1m7o2W9aU8zophFTQQCFzwOcisBq--V_kMzYGe50FJNM8j7FkEWAkkOkxW5EZV9MdTOB_jlEEKH0F0TSinKG8PVXQGhmU_2A9g6IcrawpFQjc5LbSYeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=d-70FGDnvzgudb9rxxa8vD7OLFfZ_nJixsoqnlUNkvIOoJrdtqzTXr5aL75jJEQYkZP6SPSRKIu2KFW1tLX-8HJw-iBP4TNeKty3cM_FOQurWFv56FEfxa9WW7UMbmjFOcAZ5qxFz8eW3JRUmxov4ZcoxhZNfof8AfSTWORrCPTiG-HiAAjQdfHznghZI4p4wbUruTvml58WMzvCUVWX88Fe_a4JP8SWCfoUghVCgNAlHd1U_Z8qrBtq-LGHxiyjgHIi2wd21wK79b8_mJlzPWjOj4Z6ko9gwAnIRraLserfHUsyPTm4-DuEtgSxVyp1QVxAqee_X83jalCzchBBXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=d-70FGDnvzgudb9rxxa8vD7OLFfZ_nJixsoqnlUNkvIOoJrdtqzTXr5aL75jJEQYkZP6SPSRKIu2KFW1tLX-8HJw-iBP4TNeKty3cM_FOQurWFv56FEfxa9WW7UMbmjFOcAZ5qxFz8eW3JRUmxov4ZcoxhZNfof8AfSTWORrCPTiG-HiAAjQdfHznghZI4p4wbUruTvml58WMzvCUVWX88Fe_a4JP8SWCfoUghVCgNAlHd1U_Z8qrBtq-LGHxiyjgHIi2wd21wK79b8_mJlzPWjOj4Z6ko9gwAnIRraLserfHUsyPTm4-DuEtgSxVyp1QVxAqee_X83jalCzchBBXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwYz4EE7qG_I6qTXxK8v4aFR7uVYI2P0C0HVWC-MZQWDKnLDW1VdgoSHWJ-AAhCLtZX6DvUv-uAUPYZPiwdUiVJNE3Ju1kFdYRCU_qqK6CYiY_OP8mRdi_3XGIbB6cqdIOdHIH_oK46y2enOSssFWIB7smyVJUYu2uz9wsZoPqTTS1TBeLCy_ognR6d1RG5D3zlewLF8dmAfC-sKedEEmjp0KxlT78h3UYU9WpR-7netjHKO_z9JEpD8kq0m57WcpVe1rzfI_1QBpCx_Sy6ZM25FkmdRmFfJgZnTlIDQcdga2rWsSAIX8eGu2adcy5NeiNqJifUmUqncO08s0O0TWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5MLH4mFi-mS8lz9x6PZbMn91dffngbj7oOTH1VGQ6CLUngw-Ffw9c1t00yiHmD3wpG7wRDUK-6deTRdtMErLsJs7QjME6r80w80yy9XYB2axut61VjhQAbCApi8zq0WYe6EvpMLdjMV5cXt5d8O_z2ili2sE5RLr4dgjcpmtwhKWvDNcwJj5jLdCfVULU09GWF72nMGzJpdsVxgTm5QXboiwB4eK0_WvL-uamflzPsZzyEBDfvrIrBlFo5ugX-p9rGCz1FFuMhCpCjSCTI8MGokM5RGs8L_wapUAl56OljiBvXA7zOqwRsomLTQF6O_a7XuHJ0ZIl2Kf-MWyzVzKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=nqwnlhXkxo2gFutJrDWc22MHrMorpSiN9dKmtIWe882oq39itFRfNexp6IYbir7pngx6xcDuhGJjF3IXcaBJs92WY3x3fcqEwuXlzSnEf5DJKS4rv_IickuwJ3umQAmF70u-S_nnfYb_ADcFWOgxXOeusH87xKnWMYb8slf0-2ecbG27nWsXgrQTuls7_9UqrgnNFif7VDJXTATFvuDAbO3kRyTPiMi8fZkY-o4l0o1LKnyhyALRBCRgA1a1ijj1CWLp1JruhBQ67SuDszEJUOO0TagxSZY9DQGzRkpTQjNOcoY77mAYBoml8YqI2YCMtvjo_CL1LhFfwLcs0-h_nVQDiZz7BJlv9EgSAztr6BYmet-eBev-KtLXdV8zvNMXl7fVJkEQ2gBcKJU07X3GLr9XJRAoINVascOycaihwUYlg0w-TpHae5eOkSDYmdjyVIKB4PG7b93N6FU9t8-gIZJWm9W7VTIbHhEixx5L0ZAq6aUFtZMjGv70c41XuLIhxCBgRZ82xdIQx-6USw_TA1dSczZ5NiyrGuFcXr8MnXpLwVDNkKTRomBliW9sju-qgNq2zi3_yvCGMekpkXc2ehvbgMRhhABGXf3FlirSz8tYs2SsVStJRoJVohE_ZZF7JzMNpw8BldLHDs5nzwVa20PmJXT2wc71Zu9bJwnkNYY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=nqwnlhXkxo2gFutJrDWc22MHrMorpSiN9dKmtIWe882oq39itFRfNexp6IYbir7pngx6xcDuhGJjF3IXcaBJs92WY3x3fcqEwuXlzSnEf5DJKS4rv_IickuwJ3umQAmF70u-S_nnfYb_ADcFWOgxXOeusH87xKnWMYb8slf0-2ecbG27nWsXgrQTuls7_9UqrgnNFif7VDJXTATFvuDAbO3kRyTPiMi8fZkY-o4l0o1LKnyhyALRBCRgA1a1ijj1CWLp1JruhBQ67SuDszEJUOO0TagxSZY9DQGzRkpTQjNOcoY77mAYBoml8YqI2YCMtvjo_CL1LhFfwLcs0-h_nVQDiZz7BJlv9EgSAztr6BYmet-eBev-KtLXdV8zvNMXl7fVJkEQ2gBcKJU07X3GLr9XJRAoINVascOycaihwUYlg0w-TpHae5eOkSDYmdjyVIKB4PG7b93N6FU9t8-gIZJWm9W7VTIbHhEixx5L0ZAq6aUFtZMjGv70c41XuLIhxCBgRZ82xdIQx-6USw_TA1dSczZ5NiyrGuFcXr8MnXpLwVDNkKTRomBliW9sju-qgNq2zi3_yvCGMekpkXc2ehvbgMRhhABGXf3FlirSz8tYs2SsVStJRoJVohE_ZZF7JzMNpw8BldLHDs5nzwVa20PmJXT2wc71Zu9bJwnkNYY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=SJ-Ak7pvre2OQr12faFX_PHTyhRjlFxSOJtw5qCJvWfbIjoeupHdtPtVk0BHKUske8egZvP72ELHP4LBvIoyNSfup4Ck_CMwJ4cJ_kOIcg9Hghy6uXX5fJF01cDsZfqIX-OELQcHpmpNYi8KG1Rj_0KnqI-J48iRF2UQ8CZQfGiUNDQvu2rYz7zEufKPmNHa8sFYEi-vZXsAVegDoAY3DyK4EOExpIO0co64l2iL31_HO5IJ8-_-4OHJWjc4erFlE5_Vqj2f5FmdaUxXiAqvflaIVipYV2YgnQ5NCSaoz4b50Q9_33y_OcHqW5pgEkaNfJ5YflIFBY59O24IeVfhaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=SJ-Ak7pvre2OQr12faFX_PHTyhRjlFxSOJtw5qCJvWfbIjoeupHdtPtVk0BHKUske8egZvP72ELHP4LBvIoyNSfup4Ck_CMwJ4cJ_kOIcg9Hghy6uXX5fJF01cDsZfqIX-OELQcHpmpNYi8KG1Rj_0KnqI-J48iRF2UQ8CZQfGiUNDQvu2rYz7zEufKPmNHa8sFYEi-vZXsAVegDoAY3DyK4EOExpIO0co64l2iL31_HO5IJ8-_-4OHJWjc4erFlE5_Vqj2f5FmdaUxXiAqvflaIVipYV2YgnQ5NCSaoz4b50Q9_33y_OcHqW5pgEkaNfJ5YflIFBY59O24IeVfhaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6348" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UakzCNsAYpEM58mZzp4l3KCUfmxFVf9ffk06nnBEhHXHzAsOuC_hgw3aUIStzUk1Ew9Jo8iRrVc7Gyez__F3-M8Rpcm3mNt-AzqWbWF48YPvoPxMKPteQrDFZH6jVldNo-5PWAPLE54W8SbL5kmZx4rrb3ZPopb3xCVb-MWl-e6gGIAg1V3kDwMY6OUk9STNx5WQzCXYunBoHxhIpHwazT2vlpeQaBey1oeEvzDb9Ls6jnFj5ajJHSF8mzRpdr7_wOlbvPv-PYwTbJYwz6LA_e05kEtvjqw-fTqUK2cSNWv35Q6VfW8Hy5o_vhvZaAoO3nCvD1aXGM1ytJ8VAe4Pvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gotT3HeAXTmcFkv9U7aHe1OyCDiD8JNrzgIiFn85IhwOjUdsRjp2So2UFBy-NYiOrpaFIbm1uk8VjegL6mH0mjN8TRwJi-Y_OIGx8PtGWMbZ9sRVJLPmD-4IyZKCQNpiHUWJdmwKsi7C9icyCHX687nZ0awt0IrcM0V0ojNs2Jb3j1PvWAkIlJDgqHFBpLa2bM757Un69tNXmxqdUVSlidmJ7bo6pIoxB-RoSuvtePRPF6G6ggr389DLEIYhj4rMiTqiZMHOGaJzqq3-I_7qbmNqYsiKRgz5tW8TSU5CHe8d1dfXDnQprQvunbwp2rtns60rjIGgDWigNDP_gWWvpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntF-s_7Tyx1RLCyY6HMsU-A0-WCuhQASXwhakAV7qlcD22C00re1jDKz92VJARYCQj2Z_VYSRO-B8avpfgf1Lgm5Aak4XPbb9MSQwQWtOgrQ1QW25DURXhsSRZmuO75AiFKqkSgu0XU_RaGUcq9sG2HN2p5mTY9uL4kznDLC312mywfTsqM2gecKSvdXDGPf-q0LgEX28YzPTqUU00JgPTMx06j1tVXlD2NzaCwk0QMV63FtcX60ywItnnU5UTFiB_yR_nkQ7_ySXbnp8HYemNhP2wPJiiSvqXX_P2tNGZONWeMnGzI6sGZKDGoLTD_rvVLsFmzhHi62xftoSOh0Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/disN2BN3GCfTVsszTBdxXBQbkGIcQqVMNpIbsS32S1DEbw0b9XO1OEX6B6Lh31auoUXJ4dItV7sYCd5UFq--pB7l4tzxwsI90A-8zhtHCy2FXdX17C31aP6e_dYMuxV8tz5ovkSMuVPxNYBdcwg4KCRKj2s2tA0Ff4niEioyILX6w9ja6HwRmQyGkBw42BAgzxvXGMBOEWD9v3xDiYGSmsklbWJED5YswkgTEErYJYXv1MZHz1LCNCK7bsHKOAkK2U_zpxssSiLUhezHnpA2cPOh11JXanBLgfBkvpY9QBdKqki4Hr5W6ocZ8OWyTo4yFbx3vZddbE_MXGDCWKYs_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LVbCnTc9teeSP9VaPSTc33yrauMFcdhjM4b8o6pAnrLUutPPFMPIZpDT23FxWLPfqDGp4BR3ftGnKx8HR7Vgwdg7jlja645FZmMl-kyeKR7JS5c9BjT-G0RVHA85mbBDhQogryZJted_wQCNR0dugD2zRRJu6CHp8bXoCUNlYZw3lIyObQ4PNoZ9KHy53JBYXO4mdF-VN2VBpFo5rco4eEOPP1kycdkt6WWsxjtVlIamJgunvz-4ZUSUUr0DOEu_DtNSwG4EKAC40ae-6347-OPQzGGr5cSuFMIJjJ5nCYF7PXHOGBLX4RfWW6goJD8Q8oOaIwpvQTjb54eFmDt4rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">7. به صفحه اصلی ورکری که ساختید برگردید و بزنید روی پیجی که ساختین تا باز بشه
این صفحه nginx که اومد یعنی اوکیه اگه ارور 1101 گرفتین یعنی اکانتتون بن شده باید یه اکانت جدید کلودفلیر بسازید
به اخر نوار ادرس یه admin اضافه کنید تا پنل باز بشه و پسورد رو وارد کنید و لینک سابی که میده رو کپی کنید و داخل ویتوری وارد کنید.
کانفیگایی که میده اگه پینگ نداد نیاز به ای پی تمیز کلود فلیر دارید.
مثلا این رو با پورت 443 وارد یکی از کانفیگا بکنید تا وصل بشه
188.114.97.6</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/archivetell/6343" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5xNvLzdDpYIm8hkZWdhEgT9iJ-gEN5L7jDq37OGgEsvWWc1DObTQT3vhF9nsd9Nb8sOkfgPB-9WtR22QgJbc-tNZ1emwkCBrfJFVPWi9_8Sa84rghRI4bxxO-3O3KymPC63k5ZUP4IwMlBGckbOS7MxnxqaEj0TrpOztPr7OgCNEw8Jo_4lPr3za6kaNNU3x3-CBtelqpJrAVjHOndfQd4blPxDVR-mgEkd68EKORoAWC5t3QGj_OcByTbQFoe3bELDeja8bVktzTNDuku6A2r4YmCXWeBI7UgbMv8u3AQ4isfY_FbAN8Bh_JKi52fth3tMfYepGxuEeRIRsUEntA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHVaHoJbHCW5IOiPS2MnOoBsER8ffJy9C1zRKAJauK23R_319UASgIbiT-q70j5lgbPOEEtlbEnpANrCfiXMLq-UxEE4A0pGHJBXqE4Ezxpmj3ODHE-j57dwz_-MOGfbzmRsixh4vhoxT8ZdVQeSb3umERe_iZGmJCvmjvSjFvF1aEU1TLXRf1UBdvEV0UgSRZSlqsz6z1SQ2fzE1mTPsSw95V7ymUtfiJuUU9wYJCAgGeMsX6ydt6utCRSU7VvcnS9Nb4edSdd3gTDUwZcDLqpHqs87HZO4zFLqVBoJugVzvo_9tGkcqsZ4Qkn3AnsjiRzZRl0i_6w5eBd7gw7sKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GS2rksCxcYPFoYw3KIfWzRkuQ4k9p_d8fCG_WsvrN8qR4VN8CnqE12WsZmUpN2kzZwFPLyav6p1fP8M0I0ydfWRQextjpiviii86Cd8SnKnOSTuQvBVeJNAv1Rxh6GhpYQEprBOVjg70vZhkIny6INERb8e0q3NUdlmxmUeo93OSFOhTMCyQTYpWezK0_QMVpW8LgHFhDg_5mdLHANSpns4cXWY95qGgsCfNTBPgLVYauJSJ27C956h3KAm1bgR6tLoomWWWGl0VVDTc2kxKts-OxM6BGKFp-I3j-LhB7o6WV2d403Pl7ATwIahG6TNWXx59ambyk1ISAdjBMFGlyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHYZRTWj20V4ATjVcQzuDfKevOr-_GzfrzS6y29k11Kb7DpxBywub3WPF2rtGTCJV7170qRjwp7DU5puXU9XYGw_zEsXEUzoRgUofW5lk1dKA5O0r_wTOKMAJbVMkVPtzL9Uk3Rio2RselU17Ds6G5sGqg15NBXcDiCkL1lwm1dWhGCPL_tYpbU_xALtDxg8iJDnAzyPL7m--uQ6RFtk2BEPiU25DIVAEZ4bBeSgvb4wwbvThILH_K2LaVNDnsPtLt-Z3BE-WGKacr4eiSi1O6sWV0geCkiq9IUH_VSMyGEMw36OQkYIYQpEqhkWMNLCDbpsZeJWwExfytDol8aQog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1ioBVRvrWKwyhwg_Sm4faz8019o8AyM8eHJEBnmq_X-Df3KGcdv4FXZQDkDHJZyqLZxZL4YBGShMx7iXY4qXTn-SfmPciVtzXQ4b7_AVhwQ4Y8j2RbejNPLs_AAOIUgTVEw1qHiNm7gQUb5m0l2CQZYzh9ksONrSrEfLunlpAQKNvU5nz2zBCmBQZXhsV1BUKfbmIghn3Hd28Hdur2Q2y5V5HUTRbr4uIJNoJxlqTgn0b55F9oXmVJQrpRAS12B7W75AFk-A__lAbmtQj-ERkZ76PTT4IoCazwh8y5Xl7jQp09rPP-h1bHOfefImEsqzl5rZ4c_34p9PS8Rv10WTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLo1kSrKC5MTO4ye3J8MP7q_2gOiQM6BHX2oLN3_GzBKSLVnjmgvrowS03bEY0vbYWhjS_Nn8DIe1TmIOoN02cAqPyGCHu-9ugAqF818O9qsyuASHBsFwcB_3sxUW-EuH05TV76bk83XinbDhWzJClsdZSbUpTw7QU1jalLJdwSzE8t6TdvFOCp3SdNUFlv5Ein03dWOmbKM68YWpkOLYbo_tFgWlpc_C6BjDt21yXvWYqS1xZo2UxkcHQl9d9pgILks4Gi8jSIJgxYvVivRET9mBvlumRyQAlrgMLu-HbSYTYHTyU3Bak0hC7qeHELOof32cZMqQcSTZGXssAaKww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqqkrgDDtPZUVe9lU8V75INly_VkH75gNzK3pqr70QqR3YVWjjFkP6H29EdYtZ6smE6wirFHSZ1bb5x-y5gIoPxW3witflhrsivvA_PqFQZft9hsXHdDbyvkAY0dbuWqb-IS62ycOw1f2lrBshmDCN8lwN30KuS2Ipfj1S9-PWcdaYxl5s41S-g-WuF7oYfy9NiLbYv3zatWzJn-lsDA1NpM0nm7hT_6PGYgFRhKzBXSwejxP_NIBBseInxCdY1SZQQZ2IqDV2MaTycrcahd2IlMU5O-I9GzQkXDenk29NvhXSI4aK0lvW5yjwuGaLWJ-s4r7LQOH_MgKYHJkAewnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=ePNAAAYCxrtNTmF_1GsTQpiya2Kn7uo6LLxMhkX_B8yQOuf9CXFL1eFTywWYQkK9KtzEA9btkDXNtEKwYfm5eWzXkFY0i-4TnRJk5YIVBJzqK9hjN_1_G__N-71-ptoRH6HtNvOiOaM9zPWj6nueDYoQeGNfirXpL3YbZ4kPl5L7DXhAI6ijVBNU6pCF09XVHAialaENhxi9hwM_NpjK00_GNqA_G09hCG6lFfqnXzoBEOCkQXh4lURcF-gYHfMirGo_sArqyVSpQahUY9jA1mW2plp4NUEsRMAQixKsWtjrIjUHBblD57Tl9rQ42Pwf0eC3Ti2ep4tR2edbIQ2Cgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=ePNAAAYCxrtNTmF_1GsTQpiya2Kn7uo6LLxMhkX_B8yQOuf9CXFL1eFTywWYQkK9KtzEA9btkDXNtEKwYfm5eWzXkFY0i-4TnRJk5YIVBJzqK9hjN_1_G__N-71-ptoRH6HtNvOiOaM9zPWj6nueDYoQeGNfirXpL3YbZ4kPl5L7DXhAI6ijVBNU6pCF09XVHAialaENhxi9hwM_NpjK00_GNqA_G09hCG6lFfqnXzoBEOCkQXh4lURcF-gYHfMirGo_sArqyVSpQahUY9jA1mW2plp4NUEsRMAQixKsWtjrIjUHBblD57Tl9rQ42Pwf0eC3Ti2ep4tR2edbIQ2Cgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfp9aPXIODcEqOlslRegWaPiDmYZd7ty4es7ycmrcY7XoRI_xaQnbPhUdYKrn_bUohEhyR0Em8rdlp_GprsLCk05NIL2TGBzXqUf5LvCnRQ8sA0ZQGHAuzgaZ_--KSz1xk1tMt01Qqb30W9r9OQmyE8db2hLY14ZnBhNfwQXcDBb3ERUmtGWiLqc0lkdphmc1TcVjjO9B15-4FNwpPpyuOBIspPIV3oM2ZTKGvcZPtX0KigAkUjox8osdaJs7RhoXJWZ14TI-XdTs4EEDWyc0eV7YKOw5eF4bCv4ZV-RRbvF_X8KF5yfUgP0xVbTW3Sy5to6KimarVSZXnFzUjLhGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXNJw8c6937B2hwUu52M4h5TeA5J79gp7e13wS9zmx9QDTXDzS1_XN0JlOxWLgruQvy2YK3CWFDXaHyzL2T6gZfpDdSgWOPBsy9IVLV1U0WbOgAB3vHbDjrN6EO3JJcl2uF3XQ4foz7RTPQxiruju9BdhZT1Iv95a0YSEEZw988gh5cl5WSKMU3_0s_B_2cLS5d27YLfvp_F1osTN8OqSIoSORWip64MFtDu4ZuBc2zF2hbzVcH14cwBqnVvilcdkN1_z4qOBuURGUMpMJQ1KbTLG7kUcksoge3iEStaGHg8ruQZxQs_OLfm9B_HIiusrRuVtvw_HOf7x5mQe8auuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEluLgjMhiLultiZsUOHMmN0nMuGdvpIUxzyiOGA-Q6y5qW2M2YCRy0mPOYhaUjL0NXC2kBiJryD989dXT4gzMxW4574YgbBSs5lAe3_PsBXAYUQFziHI0fSRMs3PIcGy9tGwb8B-KmjfppeZ0o32PaNXU0BcSjO96ny8-1k-cL_WvUAjMbhZvneFzwwXGB4_26pmI9lsv0CbwLZvmwRVL6SNDaPU1qM6F3crSu7e71R22ZszeeT-OZIHX-bzQ4ePAAmIDw7DpJhLjg6Llhfs6k5VoD6Q01I2YXZ0AfmmR3anxWlTMvWUc6eaMWRFRjW1YxX9nlNU2UrvbXlwuo86A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLJsezXsfAooBEOzEuN0q-dzakcIcfNRZJoU4jKEp-yCvgv5g1ZX_BJFqlUVrDQ2TcH348eG04nDOOb51IWzu_l5tMTsWKv8tBaEOwsJv8fhlDG6_1DnuVPZdQUS0cEFPS8v5HYOfqIeKgV8C0gQt41Ims1euNjibLGQYvVPg0ynFh7kNpqMHIBAHwcDryIO5azxp_QuWK25zmlH4gLTv8fYJrCobf5VDCha-yA8R3Ldgm6Ag0lnIjNw09-EJQs7sWC1ITfV7zQlWINN6zeTwV_oVM6lMW1LRBpXXgmzL6fFJLeBi3nY34o3Gu9wZ72axiPiMKG92YYmS-AdMJw6rA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6331" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=cVh57XvbOUnn2Z3hU5FLfLgJUmYi5sdpCmxxyufAUw51nCaZK6T13hp_Mgj_xlvNjH0ZvhNRPr_Z2LFtJ73Tgu_t3D8aeIWsR_P3GQkySbXSKMfkxFdOSj7uQW7WTjaEBclBYuZMpRZ_Q7C6vxM4SFWQQeDnjPILEfSTVvzSDi8q22otEr8KweqyQtH7rQJDouLznssMyTzxYLi-6Qolz9KSAPLrrEldxCWhKmyH6PUCa-WVYioC7oPiqecRf-iTie32mZiJbwxTEXW_HAfs_M00mHeHC8ZHZSIvC2cAoctY7mUOLIW0Lnm6DpUdutTyjSxMPjT36MxQMJQ484RRYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=cVh57XvbOUnn2Z3hU5FLfLgJUmYi5sdpCmxxyufAUw51nCaZK6T13hp_Mgj_xlvNjH0ZvhNRPr_Z2LFtJ73Tgu_t3D8aeIWsR_P3GQkySbXSKMfkxFdOSj7uQW7WTjaEBclBYuZMpRZ_Q7C6vxM4SFWQQeDnjPILEfSTVvzSDi8q22otEr8KweqyQtH7rQJDouLznssMyTzxYLi-6Qolz9KSAPLrrEldxCWhKmyH6PUCa-WVYioC7oPiqecRf-iTie32mZiJbwxTEXW_HAfs_M00mHeHC8ZHZSIvC2cAoctY7mUOLIW0Lnm6DpUdutTyjSxMPjT36MxQMJQ484RRYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6330" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrRbSDb1-3EEOrWWH_eHfK31352yd-_marP3UipXbpL5lJ78aZ8KS7w6xan18on44_o_IpZeYp34qDWsCqrOWJeqNk_eBunuatIlIL4itHmjbEcmCx5dj7HcXJILR6dcbMke3h2rzpeD1eQaebSBkhMfmpTl45SibTVjg7oqoTxas1nKR2r7L40GYSl0EUF6fogaIIzRdyQZOQKzxAqSwfYQ6uDvApXQR0cQzPfKB7eNVBSH6TIPngNeWSxyBNsh7GbXzvEAhHRp1oZhscuKtICQvNNspz7FCp97GRoKNbm2zZbwppFz5ojVD2bVOgaTs_10k-zTJZEwi3Q5Iu526Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6328" target="_blank">📅 21:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6327" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6326" target="_blank">📅 18:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKPa5a2XOLTiP1N0R6NAXfRpyAQftuqc1EKxekhUzX4NewM0Qv0qkcAK3nx7XWZGAHWTrufW7TTOqdYOx65AibL6Y9Dk75KNcnjz5oSffljrIAB5o7g0iafeM3GMnBH9cQR0DSPEXebiQGG-GODxbADYHWsxxtJE7w8lBrfzzssyLLtcErPFEyKuHMqw4pzAPYCXihNrkJGlcKj2oXfwqIKv6Lk6Aeph3Zy1Hh5szMgNq2knrwuU5VmAaGppAC6hQmfumZJcafH3EDsKUqiaowOlctAsoawqqtCeXKEeYWw1O1FXjSkLbyQ_a02KeCoSa1Im2lJOfXiWcn5iL2QwrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6325" target="_blank">📅 17:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4vRe5QToclLFhcB9H8LC27Rxj6U4w7gK4o8kFm9bSK0kKJQ3h1lBzuilr20-yPj-jrqCVfxPLVgEBNtIabzqtsoV5DpAqszG4_mzvNqOH2cV0XamTJAYnE3iSg22ZCIzM19JwceMRrE-HdpJVdueLYLzzrcmMpefDnBq7PGqAf9C7Hc3-1tjPHXVriQ3fPlOim29elQkTrWKzxtefans4ULjv8ZjAHtPlfMfUA0r1hbb_hu3dcmLjeWujpFo58z501B_A0xWRwN_zeHF_f3j14zrdgwbBlr4bxNMrU79-2Prb1sAk8Wp5GnGnPuSOFFAyYql-87gNwS_I_PxCASpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6323" target="_blank">📅 16:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=pRCuoYnPM5TIWhahMWwE-Gma0-xv2Yft5bOLn0UTwmH4LGhAx4YwJPzysqur26N2hhWjXtXpjJWCbWnDplPXebqxtbuhE5Jt1lwl63in-ZKirDb5kJdUrEtuDipYi6T0jQwTNmUJOJvx7hiJnTZCxLD_KMxdMWei6OOA_K8KSe7mz4B6OFjFYYDwddTJtwQAQmFDCr7JSLPgqgb_YyiV64Kv5JojxPM4dzUP6ihw-E3PObr8_gD-RAKBVPyVcNFoHRhuu4vg70ujdEpfqrIe67iwRX_g_C8J6_bdmNcflV4MFYBt-NW1V2jV-zBoxw259Z9xi9DsdYDtyvWpdK-WdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=pRCuoYnPM5TIWhahMWwE-Gma0-xv2Yft5bOLn0UTwmH4LGhAx4YwJPzysqur26N2hhWjXtXpjJWCbWnDplPXebqxtbuhE5Jt1lwl63in-ZKirDb5kJdUrEtuDipYi6T0jQwTNmUJOJvx7hiJnTZCxLD_KMxdMWei6OOA_K8KSe7mz4B6OFjFYYDwddTJtwQAQmFDCr7JSLPgqgb_YyiV64Kv5JojxPM4dzUP6ihw-E3PObr8_gD-RAKBVPyVcNFoHRhuu4vg70ujdEpfqrIe67iwRX_g_C8J6_bdmNcflV4MFYBt-NW1V2jV-zBoxw259Z9xi9DsdYDtyvWpdK-WdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
افزونه GlifAI، سبک هر تصویر را با یک کلیک کپی می‌کند!
🎨
🖱️
✨
قابلیت‌ها:
•
🔹
کلیک راست → “Glif it” → دریافت نسخه‌ای با سبک مشابه
•
⚡
بازتولید هوش مصنوعی سبک نقاشی، عکس یا صحنه فیلم
•
🛠️
حفظ جزئیات قابل تشخیص در خروجی
•
📦
کاملاً رایگان
🔗
https://chrome.google.com/webstore/detail/glif-style-hunter/abfbooehhdjcgmbmcpkcebcmpfnlingo
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6322" target="_blank">📅 15:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRQ8clpibW6xQHmaAYT1tt_tLiWB3y_DLb9bMlD31fpy6hsb4voi3RgYPLmfyrOFoah9MBYNvw5H759Gq3or8AXl9zHm-EysbJ5v5rQrzb5_1WI0sUjALVEM5K631lVTVQb7GT5F-2YdJSGtCx0dTGmvriWaxasZ8I6j6Anm8-HeoQjD_l2gBJQgRl3wz17qyGrj9thXfp9mfHcmnciWxa6aa21bnr7f6EsigTmPaJiVTheupO-5lPY_RWqJlBloK_G3e-QMHvTfQlfAlp0aJO35fxSQtyuHts7nofK_7pFpNdqQ6JNJdxxgM6KQBh5z03itVy6N06dwUzSjF9duYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت موزیک رایگان
🎧
https://www.musiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6321" target="_blank">📅 14:54 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
