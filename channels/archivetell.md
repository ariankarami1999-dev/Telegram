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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 13:44:06</div>
<hr>

<div class="tg-post" id="msg-6446">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 361 · <a href="https://t.me/archivetell/6446" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QK1ZiNG_Rz-mUKGyqJPCMBvUV-tSNY8Yi-AwNOxZTZKj9y_rDtQl3bCsED11eK2BkE45gYODDGHksdY_HD2mrwrpSW47RTssVI4P8tw1DR8ms6u_Y-wGNtqjnTb6s2z7k3QIcj0X5T5-sUoJp78AOmHl3uJVi2jZruZtM3BkRBjHSHbOZ241GAq8WLEShMVR4jtjcqQEyDWi-nlcd6BSQs_CahqO0p75pQ4LK8ooR0Nk-XJdcR9OqE3tk72If0pvOlKJPBtvFASUuxah0bIjfiG_5U5aLkySrn9Afi8tvpyVtSzH6fn_86GGKoyY1LiwYdpdPYS8aDTgBhqmEo3iCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
۶۷ کلید ترکیبی پرکاربرد در لپ تاپ و کامپیوتر
⌨️
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/archivetell/6445" target="_blank">📅 01:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/archivetell/6444" target="_blank">📅 00:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/archivetell/6441" target="_blank">📅 19:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6440" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toRblf6LXipOrJYgCA9hIWd690ih6Qi_ChxBRqG8l_AbJS63oxNynIO1vBIWByQqELE4sF8mN_EcO5Dy8V07Lgo29EcJgC0QLK1F_CFSmVna96G5A9zq1RrwaZoal7e6OO3c10Y8QyYkaEAG8nR4bu7ZtqaAy0fAiIyMJSmYWrGgAxwJCowHmbrygItP60BlB7R_zZE1obcF4W55Ap5Hp7_zFOAWN5ZiuWh0OugPx8DSTD4PpgFV5F8rSNgvPck7CIe4V49fLHM6vfcWPJoY8TXqEtsVuhCIw7IuA9SKTHZWhfmWG0Ed9YdtWYEuGgK1RmeyIQtn-ozxbSnBgzFZng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
راک‌استار از کاور رسمی GTA VI رونمایی کرد ، پیش‌سفارش این بازی افسانه‌ای از ۲۵ ژوئن ( ۴ تیر ) آغاز خواهد شد.
#GTA6
#GTA
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/6439" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6438">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/6438" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6437" target="_blank">📅 15:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6436" target="_blank">📅 11:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgPAgtVR7cupEQWVr7ZhszI9CLLKo67Qre2VRDExIu1tiRk943Gkc7i_fpo8OFkrylOQ0trPm7Jp2L-5MGATasz6RyPhul_yds7y550QnINCvkq_axjXoQqWPhKxVRBqwXIFhMQcAaEMZsmPGusTc9WxIRmg2_JDc0vV0DrnZdrLVFWk-uJhlIsii_ZoJROZalOaOerKeUXtVnoxcB6XCQHEbRbDqvEoCBttzsEytINzUoebs8zgL1nthl2bCqRU7eYEKPlSRSPFI8DThkAB2jIo3bYT5Z26vTJp7uXI7Tr2YTJvJoa1SgvoSqKgPZ1EeOZQmC_wNQkJQ_MY5Su3Rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6435" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=GBRFP_8WVI7eRN-ZEoWd_fvoGGAOn4wzuxTmMVeDUTf9yv-KT9thoxXDJ9Ifymb5LpmySC94fY1RDS5rWefPYMDzwdLBYaOp2ULvesXGDKVW7ezBB-eoEs9lC7HObcr4InPEwNrGFoErOJKRmpXJZk0vH1YaN785Ce2-pEo-BDXU9F59Fr1lfVWjrDYjqMyNMmmhNwHeYFl7saadJt75SDwPYR-hFZfOcFXY5NuCwpaGZN6s-kRBn6M0S8VqCWWJ8OjZCpETMe2mQdNAfsn-QYMCOiDTySljkDSukOepOcOpxl8d7A4GPN5yEEN6dnGAFu1t0qoAkCQwPWWUYOE_Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=GBRFP_8WVI7eRN-ZEoWd_fvoGGAOn4wzuxTmMVeDUTf9yv-KT9thoxXDJ9Ifymb5LpmySC94fY1RDS5rWefPYMDzwdLBYaOp2ULvesXGDKVW7ezBB-eoEs9lC7HObcr4InPEwNrGFoErOJKRmpXJZk0vH1YaN785Ce2-pEo-BDXU9F59Fr1lfVWjrDYjqMyNMmmhNwHeYFl7saadJt75SDwPYR-hFZfOcFXY5NuCwpaGZN6s-kRBn6M0S8VqCWWJ8OjZCpETMe2mQdNAfsn-QYMCOiDTySljkDSukOepOcOpxl8d7A4GPN5yEEN6dnGAFu1t0qoAkCQwPWWUYOE_Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6434" target="_blank">📅 09:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">با سلام درود رفقا میخوام یه ربات open vpn بیارم
دنبال پنل درست حسابیشم
اگه کسی پنلی داشت که بشه حجم و کاربر و ایناشو مشخص کرد ممنون میشم داخل کامنت همین پیام یا پیوی بگه ممنونم ازتون
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6433" target="_blank">📅 04:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6432" target="_blank">📅 22:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6431" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6430" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6429">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6429" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6428" target="_blank">📅 15:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/archivetell/6427" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoOXTtopaDQf0CxbU747Jz-u-Gzr-4K6oarM8ZxVu-bgH7SueuV5zhcCYSpURJ41BEpiyh1fduLYb1rtgUJ-bnNwqelRC5WKYqGWgb9T0d-_6fyXoPlslS9rXlG-d79dmGwEc2db-cTudP8regigfeRxELIo-EcJKVXi2S1UzCO9_x7LtvvkzKyms6bQz68Tb1BZcgvo8mEZTSGiU9H0zyRNehVINm5y9T9Mqbwhagr3VF2Uy8BCCEP_BE3WGyG05Arto1UtBPSyAPc9DiQrCZ7J5FVfymj5qLwzVDuz5VBM2Youy6Y7uExwZCRk6nrlx7Oc6QVAvVIiL5KG-vU74Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6425" target="_blank">📅 13:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if1Sq7tcWTToiOAupH1jU99YvKm2Qj_dl7xQvbTpKaHgUW8k8eS6xxtRyg_PX0LkJOTx7NYg-54x7fvT4dJuWYr9nzTtCRtdY0O81mISFWsgNDVm7-9M5E4t2UrqyJ6ViuF660XEcEhDXkiRkrhp0bXBzV2p8IA5sJQLl67IDZ4fOaG-67K5fgYDtMyd-ZOwkAOvJz-1Q7tQh-t7TznmLoX6Ytlr_9tAgFdwHFe1BgCSuVwdTDOUDOY-pd4hO4ok0jSY4tNc8DrDqlSk1Zl5pYssMNVzQ1f8VUYUsEH44EZgtfwpSTTCQpVOtUaz3B4mVbu2zwYKzu3keHN15P2A1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHMpq1yxdSM9MQHzQk9KBkc5qSRT-1b6okrmahy9jdMj7SpjPfag8uKYvYYCHPTJuigRCsHc7toyLQAbl7nmm3RoxIp8xvtZuIZmaXRBzbhNe8D6fNe1L56ZGsdPPnHhKjUR1zRYlk4YK4Zk7zvhHugkwSKUKuYmvjFkElVX0SiiRPeHP7mph-9NTelCne30u-2Q3bKWXzz-ITgzlwSNd2_1Z9pVBeLp89PD3xx3MUSfuFe_lTMQ22bLK5qVNhk5JUNgmAHuwjpgOpb571tvIz1JSNj06HYVKcMBC3wXuC2pszyLaIqyX8GBhKIk2ycpef2BLGtYw1cnGQtScAeo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت api رایگان- GPT5.5
لینک 10 دلاری
ثبت نام بدون لینک، اعتبار نمیده و با صفر شروع میشه
وریفای کردن هم با تلگرام انجام بدین که تایید بشه براتون
با شماره مجازی نمیشه(چین)
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6423" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vj5Rk1R5u8DuByx3uSOMLi50YD95W8jxQamHITOkzsGznTiKlHlYEby2VuCH2GBh_UJlTNHNmTU73LyFT_R5IOv0_O74uj46v1nDAUKq3E7QLIfpS3aGaLcie45l2hI0m5l6Hl5H_cfEH4LJGkL0u_FXtv68i5wrQW5o7YWDp779FcPWnEnc6IdglrIJqcy2HNsn1RynKaB4Rl0_zLrbQZFOMpeDdwwL0P5TVJUkY-yzxL-yHPejRfmcpeLE0KrK7WSgKdzKFuRAL6478R9bjGyYpwTRIs58zH-qXPFcgeqFU3B2PUvhTDB_Nm8_LwgmyjNgZuBeRgOO_WxepMp8Ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jd3_U8ITaQcg3D9mm-sZVG9OcEyznuFHYGFtO8vhPa3JjDbi7sppK61oSk7UoHpRcABCjXHSRgUMmsl2KHivLCL7pmdYU4-Bq_BRpYKDgVQhFntpfeb4piAKRhaCTOBOKSnXFWDHJnmrEZ9mi_cxK2B2OQOBVigjSCWsMn4-3t-rYu05GkNHSuFbDJ0wzecdv51dR4O2fV_W5C5LfkhG7abxI9lyGseHizcJGvuu_vGyBjnvsJzUC4uRkPPkRfzMglZx2IdE3Zy7ENb-JyVxhAot-Sha70p5PQzjCzVD4px8Fk393XyXSrX5YCQBpHIiGwVo2dyOCQMlVWN3EiMMxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uPCZ0Q1KxcnW0wVmJ_rU9taqWenJfjMKNL5sM8NzUKnlkynniv8qZYTW_sZN-6AFvU6dl0NU1EGfUsTVmXo_gFqxCBrmSo7Ufr9A06T8YzrePn8fuD6NuVN6c-cHVWH8btBWbKTyYOWLzKfXRt9eZvAPD4WkVtxS6AN7Rl-y60PmFaz1jnFTqmIHHpI6KMWPM3gGU1MyVU1iXd5SJ23qosvyT70KQbeadEBCiqdR0upsskSX9D2ll6y3jAxJutq5vKXGhFrNhZoc0ry5E2iyQWJMyzvDPMOeFKvTCU748frqjXBCLXbikIDuUduikgNe6TWarsGOL3guQZ7XGMMlDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uQUTE9HGZFPIx46cLFLAFLgfOkWqr93GRghEOMroJK2UsmK7hfAtD47VlgcfUuYsrZUwwy0uafRqmcJ2P0iATbT50GND5li74tmc8SSn9Dx5e1iqqJ1lQ9myHI_pM6lvXVoEOiNlTh_lhbiwahVZwjbB7SOLRt-DpKW_ro83dDsbny3jUGR4QWwIAEaybr3069FefYQdymstKLcnR1s24RKwdHS2fRbeLEztKOovj8LjTMKfw1mDaCe_JyTs6uLWfs91yK6Wfubj0u6VxW88ls4qh1H4i-sOthscZDFyolyo8G496Kr_zKDRea2TYuo0RmE7BxGR6qUcF9MUL7yIiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل جدید GLM 5.2 از چین معرفی شد  توسعه‌دهندگان چینی نسخه جدید GLM 5.2 را منتشر کرده‌اند؛ مدلی که به‌گفته برخی بنچمارک‌ها عملکرد بسیار قدرتمندی در استدلال و کدنویسی دارد و توجه جامعه AI را جلب کرده است.
✨
نکات مهم:
🔹
عملکرد رقابتی در تست‌های Reasoning و…</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6419" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g67CkyNGl_BosBKptSsZjULNvTAPYxk2rDRh174_icka_0o8TAbRR_8_rk-U5XjB0MxS_lSRMnFiiy_UQF0G7QxF4eXrxdc-RtMIIWAZkzRp7VfnbGWBqbD2r4Pum-3IsRpdjgYMr7kuWRigwdxgPuR0vioO2CFjgNzn4ud7YDl6zpVuWV-N2r88CvZP8c44akP8nhv8D52hGURE9EdZ_NpK0BlhOKLKDfpmfV8glUxeXkg2DDt65XoDpzxOAxSCr5JMC9wqnF-St5NtXtYuR_0T3-v38FpZJxt8qZsvLictXMLAg1jK42OeQXxk_KtF78Jckhox3TulU0X-pdbzsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xx7KcdUTAfD4AxukZiKSaYxgI3JWrEDpLVkCWVE47bQ6eMW5TzsSNziwNVq1e7q_heSWi3UZPbN8FCV1YKkwWTlzZWE59uMHAbEbBF1KifF2zT08NFsQyJxeq641fSYNP1tGy4znisC-u8-dGyUQRiXGNcfjuQAexnJoFfJivUvZ-aQ-J-f5Y_T2zBj-svKwosFwwXgCepEt9DXY9B19nrejP0PG1uUudM5cLCPYgMdrh9Vqretpoac6i07OxTC9ICUXFmSnRzA8bQeLeC2ZEhx4TBNHcEylPzIdfsxQL3RVHdlHiPm9Bc5XO2m3S-koTSp0XuatEGP-WMqzijukvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6416" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Heybaat.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6415" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">sadra.ovpn</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6415" target="_blank">📅 04:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6414" target="_blank">📅 04:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6413">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qfc2zrqLdb2C8_WybWeqiR86rFHHXeBIj-Q_O_u7jY3zqyBeN6MSQVluHAB7cszv0RRhV_91Jce8Xyz_ELg6azMzs8mBVBa_ULfxLMD_uL5oISnuL4vZvis2P18wyQw9O3I0RHGd5SoZRPDzkNKDBScGKXCuKuURMPeclOve-87WyQrqLhuLTrvgJdq_PKDZ793jqvR04MmyCNPJ5xCJxixZ-I7PceS9by8ju7teIGC8bMkTMnVj6F3IizgKRpDgAGqWF8VhRw1lnHXnOLrr7tY63TeVVYr_Qv--fd00-t4B5S2zIb20Xbkv0hcunjzyiawlYwK-U8Z6ivKnZi3vpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jjQtgaU5XVKwTLHVyas4l9G5sJEqIHUfObSQbFN2rp89kLHvlpHYyo-tGvexODLfOkHgAaJGyn48MBpyMrLP-reMvInPSrmC7fpSPAgUMhPwUhwFafic-ofYC04gXj-5Oc4NbLW2jr9PJEQbkURCQkMUz47e4Ofe3frOTVHEO7SzGNleGEPu5A3ZK1S-GNDIze5g4KDhVthlbbracx9AGXnL-UKXQhY88qdiCezEkdRPJAg_RK1aVFfsJN_TDRS4FNcB6pguStMsFGmkGxL-5Abwq_qfoEs1Dj55zCd5QXPGQiXfanGomkmAJE9tMx_hIlP_fz2SMDnf-wFhgtTqTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ddZQqIKAbNx9X0Hg8IMtERUKVybhH0skmuMF0x8DObrUJVp2hRP57wgHCgHFPiNIKA99IY2wtW6WU8BYUrSLrNxqwOw5ylQZAS3Av2WS6LiovH6NoDb3jyq8qoH77TPCQP4JK4qw_bbGb-yKCk3ElRKL65igbih8Z7K8TJoR0sxSH9l0PTEvsiMsGb8eem3maB5e9x92NvrswKnA6lUBLbqaGopuKHczW6Y9A4Qibzdyays29vq7H1RgunHFzxg3Rs1aUvsrRl8UBD3BtgdWlzpgtonYVwOrgYuFT4PCWwX2qIlH_qofVmYAOwSkK94TGBHLzZoyhRP_EdN_rh5cIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CRi8oxMAUEAK47fSGPlFi0Ig4ONyEFTIjJA9gnNqNgcSJa1gJp2n-8jzTrB_5P-rbmLUnZCtOy-_CV1VssmZ_pyowMj7pDg0_q5gO4SUxFA3vQprjJFXWqieSr8iUO0bGuGRpC9N0RUazylqSWJUvZFGPc_vdf3MAUFYRswvxlhAKPeI5sNJ4DsXurN5fAEAU1j0EkzUkn76p2OwmOOpjQf0ApeZNdwB-ULUo9p6nvzLipDcmy72i4K3dWdJ2gbH7fj9-y_3lHO7nJGJIYe8nDBK8LidQ2iYXiD_OqfeCLec9SYO8RaAsT8kaXlMkFbLpW6Bw9NGPEB4r1p9O8_wEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت تصویر به‌علاوه کتابخانه عظیم پرامپت‌ها.
- طراحی‌ها، تصاویر، نقاشی‌ها و راهنمایی‌هایی را که توسط هوش مصنوعی و هنرمندان و طراحان برجسته جامعه ایجاد شده‌اند، مطالعه کنید.
http://Arthub.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e186940244.mp4?token=Dy9V3f0MtzafmqM52FsZjPe3tqn2aRv02vcSo_GTsNy3Gfpjv-hmajoRgpp6dtEIO1RB8w116FIPFtZ9InagHGAE4oi0RYPH9L3QonViDPkAbIZfwEOjh8KcFYcQeP5oYkRye3IRbqoe-vD_NsPGWBHws50TG93cWr_Isv2j9WGQbD3HqC91XpQu_a1T7VS6XcAOR7adnbYnY7implVTnLzjZ9p3yB5FIr6CDrLpfEtuwmsasIrezHogRusbN3AaHP1FfMvqnYkAPhqahITBulX-cFs8YBJzVpqDeM0Pu6hXHjfHxCjSgqFVd9-p6yXINyDRtA9bmOhMe_Y7SiAuBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e186940244.mp4?token=Dy9V3f0MtzafmqM52FsZjPe3tqn2aRv02vcSo_GTsNy3Gfpjv-hmajoRgpp6dtEIO1RB8w116FIPFtZ9InagHGAE4oi0RYPH9L3QonViDPkAbIZfwEOjh8KcFYcQeP5oYkRye3IRbqoe-vD_NsPGWBHws50TG93cWr_Isv2j9WGQbD3HqC91XpQu_a1T7VS6XcAOR7adnbYnY7implVTnLzjZ9p3yB5FIr6CDrLpfEtuwmsasIrezHogRusbN3AaHP1FfMvqnYkAPhqahITBulX-cFs8YBJzVpqDeM0Pu6hXHjfHxCjSgqFVd9-p6yXINyDRtA9bmOhMe_Y7SiAuBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEVyC83GsvMsKNVKluYMv22yJLXFODu39NRBhfQpJjJOGxfLVq6VBFFO2LWiwXlQ9YhHMkaZoQHoti7sGWM3nyicEJhPqGprmE1Qg6NtQZQ-8q5u095p9FAf7GrbDejN7gdAF7E_FMO6UJez7ucUim_cJUd2aTKY3V_NQ2FV2I5Fz7C2xtg5zJNl2kpGpVAPJ1w7Ds-yAa0aIG5uBRYgPUpsoHBV9DJzs7Jmn1PQfbrsZRRMaA9DhzHv6dihg1QsCqFhJep6xMTrgIe1Dk71ws6_0v_oHYaiTjZ1cKAgGqK59sQG8-_c211DpL1St-UAfH2RKALj1Pt-qYl45OuGOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087fb590da.mp4?token=IsnM6VIE-W2OYX2qcz1fNOhZTY6idtT9ojHnvjRHNPBWpZygWPjOBiIVWYNemcgHuuSCiPIOOeehy4-U_6ZIPM4S-MiecdVnHQUianlrMNqMTHSo1rsXV75oWcZBLjxz6K8W4X3U-IFeVYmvJk3CCm9QlyrajSUJjswm0s5UmMrV7C5UbJWmglgmnnuVOEq0vp7z3jqh-aWXeVUvNlMEx09qZggC4b_MMtkw2g_VCkkMvi0ClUqozZPy3LSRn0L13py2RqeYFJfY4Hbi1EcJZm50deC1UZULveBlNb2IUIdgpa3NarsQTZP6V7OxOFoqlXWtYG95YMO3Mle4Q2VrlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087fb590da.mp4?token=IsnM6VIE-W2OYX2qcz1fNOhZTY6idtT9ojHnvjRHNPBWpZygWPjOBiIVWYNemcgHuuSCiPIOOeehy4-U_6ZIPM4S-MiecdVnHQUianlrMNqMTHSo1rsXV75oWcZBLjxz6K8W4X3U-IFeVYmvJk3CCm9QlyrajSUJjswm0s5UmMrV7C5UbJWmglgmnnuVOEq0vp7z3jqh-aWXeVUvNlMEx09qZggC4b_MMtkw2g_VCkkMvi0ClUqozZPy3LSRn0L13py2RqeYFJfY4Hbi1EcJZm50deC1UZULveBlNb2IUIdgpa3NarsQTZP6V7OxOFoqlXWtYG95YMO3Mle4Q2VrlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNvUrhfXDYHtrG4bu4ZtM4VgVQneQ-f6JXVPNVBFhJ-CxQo1u_JSRfKjsF8-1ILvGMhsHwNOUPll4ZWz15WgZ2UJbXIkR9aEMbksHGKhdlj4IRTiBXYd8nUf0dTS_QRyjeo23CIVwCz5IiAvfhpUmVaiFQP4_MZ4SKarEALkbKu7qZ2nUiG36tDOCZB9_5j-dCkNlE_6_fdb1nIj959H8THIh2xVs491DvIgZhpKocgczYl4XiDWjS1KT1VFP8gq4LOtUQZ3vvV-H8nA7ALXyr8_FYMWcgKCKTSO1jzHBW4TJKuSsRs1ekwU6QNo68MISYLWEjet5aJ-Pp7EI1VW7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YT4tyxknMPjsBfeU_e3P5krWL-VWQgx7NjbdWO-OJqeatqu0_kKeT4E-nSKV7Uq-h8qpvJ262c-YDzvrJ0KjfHVVbT6cLXht_KfXpdNYoZP5AgVbGL_6RQlzdTPRSOVliVG1-axl3JCmPfhMMe8bZWKZJweK36xwCKuSHFGV9it0oE4TWqJydKnmVNEl5sTmatkdHp1KCqQ6o5ZjW8OOTcgK5cOnDjBl0XtPaVi_syZCLZVNn8Aqqe-S4yS3kidoGqyMojQAj7RSh-9-CvIaxy8dvBmH6NWkPR16nV3j6QWp28u6RvKrkurpRALBv_br7cM1EwDQ-3XdryLeJmALBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت Ponytail هوش مصنوعی را از نوشتن کدهای طولانی نجات می‌دهد
☠
این مهارت عامل‌های هوش مصنوعی را از نوشتن کدهای طولانی و بی‌فایده نجات می‌دهد و به جای ۵۰۰ خط کد، عامل می‌تواند فقط ۵ خط بنویسد.
با Cursor، Windsurf، Cline، Copilot، Antigravity، OpenCode و Claude Code کار می‌کند.
https://github.com/DietrichGebert/ponytail
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRimorUgAUFUMDXbEdZVuawo97HODKhtejiQ3skDX3bWD7-8WXvcFyl68nWmoEiTI4v6zzh9r5P40EQY45YQVQ3sdKR9vGPwghwIrrN4e082_qxi_pjFEV9w4gMXhxIw8i3VkZy-qD7KQvl6_8F8UDfcggL3lwYg_XUJxKX_qsp4uiWMV-4BLN_dnoeeKQotKomdBcv7q9s4MMDNwF8KqTrS5S2I7LmUdNISewT43USOguDX4gFNWIG7vjWYE_lrdI9B1EI_PoSBhf5QX_XIYLoNlmO0UEb4TWHIb3xcxoLZf-x12OP6gjLkTXDfyWkOaNGcdJaUD73DjHfNlTcpOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
متوقف شد
❌
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6G9mmJlYosvIMis4zJISl-bRZ9t80t7N2ydsUUwKQEZe0tj6PllnluM67F2oISEWVdy7P9VCRcWqYrNDNxwNZMYO0Yh22b0yMpET7DubVr6mBEiXujhQ2fQenADSDV2pOWs0v6uoCi6nX-scDVD4D7sQglbp9Sh_1FWIqfQFFhCbYMLV83bDjsxOg44hUqs2H8zO1mhRDQFDIQdKJUj5MiVh4BmbQynltID21s2BhCiAwnepLVpXtDVIHGbodmp-UQ_RMyD_0G2CHoRH6EPB9RPIWygTxWdBlO3w7eSW99MrVTs_FJ4s_29FcNQBkNThLjfCn4fhaQOlupb5iIjAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTjnHEhpdqpTugf4eFAWVpYXIIcOXtqnVRAPmCdX6FmezA9ZOq3P_a8GN4uiFRB9EqGrCSJqmAVQQQSEYhjX4oqyGpk66qnmKmK5WPk4f0uw1-AWNCy7RSOX42lodPKfufTo1raaI5yHtc7OdDVRgwwAsf6R7s5b6bGTIv5g7PIRPTDFCtvm1wlVkqm8PmOohUL26vAMLyTyhA-CCyd9Djl85TN3J3lSHcL06tBcJH17eareydtHI-bLhI0oWjk9Q8NeKtCJnc_KYzY5SMUWk19kSnrD8NeuiPETqLJvoeI282PzJiqqPKg7_ZWQngRSDzkP9sFGnkxi-tnxR879Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8_wW_TiKr1AO1PRI2J9nwklxq3az4COvtT1bLUH4-C2NudFKisdAcTSdRtrqAGGdnPnPza5_GtSoeGwi4Kr69oD6fcIfpHqTkoRs-OhknLKW2U20Zk9UMNvg4n6_0NSF9bTZf7V7dVaxwfYps6uALhrFTfeNLBz7GaQ5T_l0Hmb6ab-0f-qzoIqOSdt06A2jN0yzyUAtcMR8agYcwP7FDjJ6eF3urtQoV7kOu1mjgbxEbeZrVJrU-qCOk0NEOVP59P5U7IhQWoqJa0bMD2_c1s9m6yaphu-LdrEZ1Xyh-xAyXFT6pMWMe2XO5jDXrvtUBVw-wcJg3-JeHol_odX3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JC2QLyc6Meojx2Jde2lDZNm-g8fyaHpgNbNlloqCBXM3iQxGWd3asyTw_JbFT1h40SHYJ3QVGMONwehsGv54geE3Q93BKSkOQHIfJqfMczLj9Ua9-IbCTBnBhL_xxTEZEgo6iysWZbBeyqbInFd6LkWh0a-mzP9nPIjBAaDuOqBwwjkpzgxkNpTeztc5QLiw7fXMzdQ6Sul2ABK2saQyC8U-aG1kr6Enmk_NhGk7EWtntJRJTGoIlOQe6_yRglOnc9QjhRP5ANZ3KcoQGGXvX3fHuU-2-rncPFRbXkp0TZGItAqLAqxvhYEnVjkUM8vAsMssBeKxIhGSlfE0wk5GtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzDhiZxsqA1OESbcRHyYzDYZZVZDnM6JNQjv-9XNSibyFlsSe5Pv5c2sBvmzBP79vujI1DpMjK_Z-TESuXr1EDYz528AK2uFS52uo0XT4vMz10ItCPYJvz6o8J861SRpAmST_4SKqA_rVLcl6dVxhgFD62fc0CjFyYTGaYBtSbWZUzMYs3eKSLR7fle5wM-Wy4HxeuNHWEeWgAjUlinirQro6iUGE14T4IS_a6Vn3gzY3lPNDlDByfcbuVTr164nCpJERgkTFHmmwHC1ec_fdgTlM7shP_guI5hJjW0rcaNzH4Coy8uIrKx9xB-foLQMiUEZWcDCKbQK8WqR22QTZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brnaVXGtGtDPFs2UZH_1tpNyENHaiT2fUiA12EKaXkTNUAPfrSTF8FYVBhWvjadGh4jbi_2903e3sp--mlc77cRV9L604-zwuPwtMfNysb4i1-H41Ji9_rLG5PAx1kYBPoIBggnl1CSAY-RwsbWXdBA8fx38avyg44qoH-o3Kabm8pxtcBmPJjWJfUpv_8GGLBzyPDk5uspq2XfxKnVdfhiOyzz4j4tWXRJhJLkalSuYVvuUsCQFNRfEdakEO0BbbYwjeljwBQ3FOKgZ5cOugXjufnIqT_4L1u7Ne-KzBXAlC-b2wstjkWqT6E7qhbCiR_bNqh_Cf7BN08xPLyOoug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYz304ZJjJWzspYNxx8PuCGuFg3jCqUiQ-RK4TM-FpuVusSOVXfCJ7R1aofK2yCMVGy5tPaF3LzC-Tl6LOsUMnwOYexFQ9YbuVGFBkaN8vCRxGKphyNTrasX0H3PEXDmJI6jXmFJv4sfKSTe4HFu38_-oPQQrFwD0con1skAZdVPLD3uPPdnkljYmRlRkRm36fLWWPRkuO62m07EzW69CjHUfSBOE4u246wUU7LDhTO2FExGvto2Wwb3NIr9BT4PJw9cJ6ojQCAbg-HLocGNpvtSps9ChaT3Z1Ny2UhSHw6abrbmFgyEd7hdmuxkxO0OrRB5W4b6vQ1WwM75YNzECQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNGEHDB2WUPdjfDGtYwQ_9Fzj-cfna3DPSEbYk921o6HHK5wXvyKDPL5TfmX0-aUuQHS4M1OkF5AYU1-NgSWj1urB-L8lcV6zYmHp6xsMcT-VCLs3RyHKSfAx6hAmUFSuNRDEA_6XmbP6H1eAvaAF6YW1qDNDP4PwFYU6ruOU7MDUIO7BujtU4lTGWXnBAyDwIiJ_3iSwenrLg648gYDo6gxA9vQANxXZTK0TNHBqugYJ4NLcbxRpxv90TTxHog7nVC6MPnkiNm2YLKvqP3-udu6h1VyXSumIMDs_rJ5QKLrxWdYit2TVLZa2BUjID1Jxml3ucjZv4nc7rPRe4TrlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=OTtF5g2H298PgZdW4n-xEJ_lBcZe7JBZvOmSyGapkBdTgRFC9KYoUjrhWCR9F2eVchkV8nxpYZBnN8CZQG_XQV7OmabDH543pOQs11U8wrLz-8bUNU7rYLeo-1__9N3Am5NM756_VTtuEITx0pHooaY6aP_dq0itdUkkHvJLrcnRxm6dcDk97w0X5vI0kCn_kwrV9gUnawiV18VxcHRr4JfdVUTKNX6ommHvsF4MofBel2LgDeFsLJhE4k9HvTgbKM0jj5mnKMZofk0jntrZMO5klCN3OcNYRdI346JUVt0trlhg-zitx2kNRJzV_yM_2dcBgjD8foiOZRl6M3XgEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=OTtF5g2H298PgZdW4n-xEJ_lBcZe7JBZvOmSyGapkBdTgRFC9KYoUjrhWCR9F2eVchkV8nxpYZBnN8CZQG_XQV7OmabDH543pOQs11U8wrLz-8bUNU7rYLeo-1__9N3Am5NM756_VTtuEITx0pHooaY6aP_dq0itdUkkHvJLrcnRxm6dcDk97w0X5vI0kCn_kwrV9gUnawiV18VxcHRr4JfdVUTKNX6ommHvsF4MofBel2LgDeFsLJhE4k9HvTgbKM0jj5mnKMZofk0jntrZMO5klCN3OcNYRdI346JUVt0trlhg-zitx2kNRJzV_yM_2dcBgjD8foiOZRl6M3XgEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_TX9giGsesbPCLFQ7JjVTnvU7kU5RnBPJlNLZUt8BdDjeG4mlzfcihvWHUESfSSgCZVYtDyV7oCvsqISthZD95JNkvS_uaVixSUFgntQzHSNI2gjufpM-66wxMgi_Wss1jATYvBMVs4eeTgG2xi4M9D8JyscR-Mu8JvDzZO_O07IKND2jOnxjhvrjKrfOEkR_vxFWkhbRMvJ0EvjIFpvOn0hUyDHYNnc41VT5Ye9ZvzHi4-rnaRTg_bprshBR-mab-v_KtBDK5xXWj1GQE6hC3KdfGKDXyRlU3AvUmQhyw7akfKCavomt-aBZWzXe7Dp_yKacjtl9w1aFk-FEraCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERWQy0TOH2lgjazS5ngQwLJTzGRS49Fck1Zp-WKfYrTShHzg4_ZBJ-TS_DNlkAjjTZxg3-ro68zP7pv7Mt7FjHs3dVkW68qL-MAYDUkGa-ESFG--VZ__nosNZsyaDAA0GEvqSfwoZGHPllz1PHBS1iYcXXSwG6T9ogZenf30eSDCF8VMWkofTzLQNaMUEUi8LAZP_qG8fZaqRJrj3itTgJ9oknbUqw1pnfU-FOwDcw11T76KF260FP8HUB-i58c5TlSIWMIyfylobxH2yqbA1lF1k-DGY2t9C5VyoWeVQDFz8mQLPq_2GD28vQXAulZFNmm-UkJVKgmemza1Jlc1Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=umUinOSeSkaPXcgc-tj3DAwBWyY3PeE0u5PlJ1pOno_AZ1lCHSfKXU9mphA5uT43E8VhEAUEMVeLRLhfsxYEiGsxIr-PsosLFMegFBg7lBCfkL1hp8OwCiZUuA5Be3NGGUMl2G0-c7Y4JyooM7jpqRd9giRAbXld2sNREuYkrhPPHPXR6OMc8GMj2kNw1MXMHkATXRSvsJysw4xLHLDXUvIhhCmUbFbmbYxUenHMThO54RHjZLi9WBQCUSDV0HqWCKFq3XoL5jYZHM8xhRGNYEdb6X9OmBfVTlN6dF3D3paUgWv3wuEmwG-axm1t7aIsJp08wEpj9TX8GQAVizIvFTnSJerqNObA6dqesdgij-7tBMtsOfBcAUEuoQFXzYWaSDbRI2KB7UIWc0_dmzNdl5YxgBRsXPgQPL4xej5MkJPD3A1M6zofwzEVDClPCPJ63Et44CNn76vHXewxe__eU8uSSGtcwt8c2sjohXbs1oGDRO8teFZEkoGPZV8WOxkq-ynLOd2LxRwhrzdepVvRDGmcsrFcClAV2LR80SKomyC8pEXRYAfU02hlgEhXM9eDp9rRALlGUO167c-JDYSsdqyAxzOqBTwPwtTz2eEkiKOM2IvIPNnCGzqEitc56oRbrXOQVPIg2P883JvKYiz7iOEMZvUpkB8s_SNwo_mz7oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=umUinOSeSkaPXcgc-tj3DAwBWyY3PeE0u5PlJ1pOno_AZ1lCHSfKXU9mphA5uT43E8VhEAUEMVeLRLhfsxYEiGsxIr-PsosLFMegFBg7lBCfkL1hp8OwCiZUuA5Be3NGGUMl2G0-c7Y4JyooM7jpqRd9giRAbXld2sNREuYkrhPPHPXR6OMc8GMj2kNw1MXMHkATXRSvsJysw4xLHLDXUvIhhCmUbFbmbYxUenHMThO54RHjZLi9WBQCUSDV0HqWCKFq3XoL5jYZHM8xhRGNYEdb6X9OmBfVTlN6dF3D3paUgWv3wuEmwG-axm1t7aIsJp08wEpj9TX8GQAVizIvFTnSJerqNObA6dqesdgij-7tBMtsOfBcAUEuoQFXzYWaSDbRI2KB7UIWc0_dmzNdl5YxgBRsXPgQPL4xej5MkJPD3A1M6zofwzEVDClPCPJ63Et44CNn76vHXewxe__eU8uSSGtcwt8c2sjohXbs1oGDRO8teFZEkoGPZV8WOxkq-ynLOd2LxRwhrzdepVvRDGmcsrFcClAV2LR80SKomyC8pEXRYAfU02hlgEhXM9eDp9rRALlGUO167c-JDYSsdqyAxzOqBTwPwtTz2eEkiKOM2IvIPNnCGzqEitc56oRbrXOQVPIg2P883JvKYiz7iOEMZvUpkB8s_SNwo_mz7oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=JNe2PpnC1Yqu4J2A3Srk_DjuUB9GQQyWZJhfWjPCMGh4TP390QSIRneQrHiQNlP4X9dCkuZgIVjHqEWe-axZwXcAC9U29F_79jtv7rSCFIEMG_F4Rwzwx-tEu4-eVLkPYGC1V93dOl5IXMatb7xuYme6w8LwmLYromqvm6KuEIfkqxVP1um8SX21IDh_2LhbF0t-8wwT8DO5C7ms1ZhvpEaO4laNYjhR08lnEWw8CL1SC01ITeA_pj1esesNsYH-huwPdgEw1Vz82Uo2TKx9QHmWUlG06qXkt00ycEt4EerG5-aMQyWOw45LrQu2EPc7p3lMToQTDWRFWikD13VS-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=JNe2PpnC1Yqu4J2A3Srk_DjuUB9GQQyWZJhfWjPCMGh4TP390QSIRneQrHiQNlP4X9dCkuZgIVjHqEWe-axZwXcAC9U29F_79jtv7rSCFIEMG_F4Rwzwx-tEu4-eVLkPYGC1V93dOl5IXMatb7xuYme6w8LwmLYromqvm6KuEIfkqxVP1um8SX21IDh_2LhbF0t-8wwT8DO5C7ms1ZhvpEaO4laNYjhR08lnEWw8CL1SC01ITeA_pj1esesNsYH-huwPdgEw1Vz82Uo2TKx9QHmWUlG06qXkt00ycEt4EerG5-aMQyWOw45LrQu2EPc7p3lMToQTDWRFWikD13VS-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PB4-P9x26f72524VY8VLcBG_yfcMGnLJnSjfLCQy-p6-P6N6E337s60tYvk8ej90WoXr6rwy0zjrt6GWvTIoe-DzKF4xeaJNsTNc1wBCGqvugfsnir-B7ge1KHCWR2-hS9DuKyvPpA8ysrzk75YfZWP38CujOg_AFVZ17Bih0AAaJAZKSLmzKgxpyPYtJQljPn3mfPeZv6eI3SbJQIWRoDWZdbAt_ZVjNBxgUWt_f3gMWChtseYXu6hIKVA8QbUqvEzjM5WzRYFFasEnisE_C4PulIF_LJcUPv82wyqlY90dFmSHkeooIes_o-jQmD9dU8g7FXApFtdz-SJDuYYMkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZpRN_j43WM_ZZFPRmoUcGUnZAoV1yPSHCtknQrLBw2iCjNCkpPxFAcdaVasbUQFYP-T2cdz-3UyZEMJiCY3EgDLQ5KVlbCakp-iVIZPEEBZJ3_mv0aXlK6m1WgzIDdoAnEgrYtQazL5g7kH_opm8LacvvH1FOFuYK2Jt1RB5ntEd0Us2ug2cyQ7fibVnu_FKweDYBnO7LAO3QjP26zWb-ddv1a5EaoZi4DUDFyXIsab7PJzt0z8yAVTVj7hiZaYasq3-JnXDjXiDlXK87GgrvyB6dMF3KwoDB4Gg5K33uYysTdhoYgnvQs6Fxg8MHPHgWhUG2Cw3RlMyCOKU6wwMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NvO9wDOAlwMynevrqQOlUcSNl0TZUW_ZO0v3nmvsvnX41XNKBAYIC8J97sTsIOn_qXtyvoHkl0acSCeO56Vec49ts3FQnu7Sz_X7E1P4JEr7SosWkbvazRiuW5vSyl5QVjs_AMaah9qpW6x45EJ52iLhpq3qvj0e_7nX6V6Kxyr76kT3faHAmHXEhegjyv3k_mHBsAKQM9BjBetRnu2KQwiPG7NCEtlLmhq0jZF8KVC-MHpoF0hUV_2ITXK4xVnwyIhdABH-cIfLrylBT5xXfEsb3CtMzMokuS7kD-bURv8spMIKfQzXfLcXR4UfG4DmBavahL5M6-Stcy7GkinikA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FOOdtPbLLfNhv0x1KANneRxDmN8D8p1Kf9frr_Fat-HP8h9_6xEHmqrjlEE_iqh8WYNl_xNs4qu6wtDPCRx2XoN6fRxjANG3PMXET_bdNxOxVuVQ4U9BL5Gkuo9PARoXmUW4hF5eXyic3Dh9f8lOSDL2-6J9XAPEgAFVskl-7lAXUULs1UzK3VTiZlp3Iq4PdTptywGWhX_JsiUZy3nygkuyAMf8V1ON8fgomyLmy65iwScC1n8fYQSV_TnI0n05oNm-vCDBpKApCWJjhFWGHgXpVt2tr2B65KNJswQKblNXRzVKU_w-vV2u5Q3B7ZkAIGuOTpkKIY93bGXBed-p9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W7JjE98zGa1Ea3GAXkEMY1ULXR-_-kC7EOlWoJycRlNGh746M10LuQXmcGaHqMFZckXHFaMB-RMkE-SSFo09DscmrGdjhHyX8Qc4bLJ_Jfpni_2WS4649xAaoBqJijrD2xGutAatP1sNUx29E_IpkHZcy6nMtY3yo8Zi26_iypUvXTcIx-cd83X_2hVevnyE75DXMuwZu5CbD0sBu4ogx0GLc3Th3uhG9NYglUJjpcjIE3gKNmB2d48FgHN5DPsbCnTTuYd3mQO_DAp6eHdT6ia31NAFHxZvcyFEULWL4tEXbeqBQBxDaNGDJAJV8He41a8Qd4pEfvMk0Aj_JUKpag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoC_QG1UcjXEeEIcQJIhQgb4nrkXHII138TDL5QB8EQEmNe-bBJ7-C_BKUGpFGLkhLR9Mz7-OmpaORl0x1QvAVCEQ9jlNY5IFgIAa6P0qZS1IXiDFWFxbTugoFAlgR9rG8VC-TjGCD-4sMm0JmHpVwXQM_bkLRhkN-B-As5RZosvbAsapngkH-RPJyIaersi_KHgVfB8P3sj3NI39M_P0sFVjqMxqJykAjqXx0ZfBvivGncCLWsVqGWsU8mdqiR4vnE-Y4W1ZMHCQQuzdQwAFXnYqpub1crBcIk6LnNlU0aKy5gZ5RlZXEc-BuXWWhKg9njKws79D6nba5aOdSwNqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Le3KWse54Vm8w454dY0dVkFUabuTsbtiVE25u1taHtexGujSIBbMgEWVI_Y_3rmbmG_SlYA_ZdlqICCagtgER4SgAGHJmvr4Nl9wChGDG4AsPFJQ1pev2Se1BQpvtV48fMna70Mur1jNmPfDbj7PyJAA9K3NYBerCdWGipmi0PJWRNLSAnHRQEh6GZQ1AmPFwjmIJoHRrb8XqnFID51YML0mfIgTdoIr-M6xy2MsE-HvvwSITUxY7dNNyuCiamK8B_bVikannUzkQRoiSyhLCg1ARfLfhHkIMNLTHrKQ671Pmk175eMleRbYb8Tl1bHGMscOiUjn74qfASztj8uJmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVg41rYIeqb-m8Wkojjb6IJvuHC0JWcOlX-Lr6LZcBvDtHs-DmAr7RSLj4g4wHxQQ1IyDVEdLSIe8dGom-nRU_sruBtRRW4OFrKiCPKVR0Pg-ruJMb2F60x_hwzwSPb-B4ViaDkIOUM3JMPaUL_bVshqGroR6Hdxb3264U0OY__D-OuFnhsgx1wyP_4uk--Je9CaUjfClH7KqjR5zd94A3W_r72YtXp4Zw-D_FmUhwH225ANPeQi_bKVsvRv0PnWR4xqf4LnwXo75SfXCmobFERA8QwtcJVMvNnXH1AeOIGbgH1UiGK0KjaC9BrELSKXdNZBmgmUe8w9bCbEfr9S4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drfRBu2ToAhI8kndbmLBMbJCPfppB4M8PR0g51hUe1RJlBfeja5NBwKO0bxGJgppGdRh1QNZ9bPGmOCbuzZEN-GotjpzDk-xLQa9r2EZSXDX2tag88BtRK7keEaftz8_HscCMm4QGCDQjNaOaSScNgvPF_Z2620z1LKGeRg7TedEgtaQSliTIHZG3mw585SK1QGTcLhigszJOUsSQW5O3M5rlKgOYlzhaUC2Gxl5N6kH9bK0WBA-MsEZZE73PuPaMpj0G2utufvgAFUoHxqM28ySE705GvmwDSyqBgOYUUBCLW2e5MbecZeA6uulM5-jdeuzUbKjbf_REslk8GeTxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2F6indDy_eRIkl-CkJJF-7JiCxawUeQydcDsK43yWO_sPXTnz6QfUn5R3vkVpiyTorJ5RIx6a5Xpz1ruvTy-Uf-_lky_q5qQHs5udn-6Safw3uEtomryUIjWpdwvxPNt3oYC5o2f59xLI9S6dad8zR5A97PbeZ3bJFe6MDhPrYZnIu6yq8b_jZEkaOvAzKkRK5JEE2Y5J8xdvCTCmlqqRRTkdj1t-nAn0tMrgeYas_nDL_8C_AWV2s6qLfBBcVXF7a9-kTDhqDhfyKU8rTJy4KJAK0ho6Awyo0oCmIIjIPS9asjJAdHgly1ESH7DRggHQRtFjyNHJpPFiVix5_fWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6cEwB9sUufL6n-5F3Rr86Si7wxviZpSVkORLc62phL1ZJLI9beSl4YF_r3FV8klBFri7k9lsKbIryRdKYGmNEXIT5fvrIcP9IJQ1vc27lxu-6XVnRP9iJMuXPqLGkFzQ3wk64-QJXr9uXENnbZ8XrS-VbMKZCaKcb4dn2cFs3r59yLckIKWbo4cznP9GXHGpa4K3x7e594_2jd9gtnpXw64vOeCVOwEf1i1bS3MZ2maL43qJN_gStp7nFSgT39HZ0PA5Tdpyamx4OEJbYcHDhMRIXw_lhU3E6kNG3C_fIxZHep51TcJbXUlgIGPdMa0tpvIiyK1v4u-c2qcUQRcBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODKgWJlIYHTQwdTaAU52NalCfrw68jDFpJ5kjVg-DrxKEqyXVPt-3WA2kxn7L_hLfFWMjro6-QV_JW279K9LfohlxJPqRn4Hp2psgcyWMdXxTaGu7qN-nhuTekD8eLD4VqrcA_wU5XVgYvrE46hJ4zHUUhMW8HT2W3qx1pRWPcKhmaDI0zk3dlN5EXPemjO202AFryVsLTmp4NzfTJt9SF5AlfVcZHxmeLVJXJqVEX-_hqAc6PCgOUHSCzBE_SfwG--YDfrl-OM3vaFvm6QGPCdEQlCtyGlhVEyTXpkFKMq1Re2nA-ARFTnTqErxHebN-PluW8lh50O7y7dg3aMmfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=dYakQmV9lacnYg2lNUM7I5A8YpY0PEKpGAf1mX40kK64dXkcAL57uyGi7tHU7zg0mbQjTpl0qnClr9o-bIxIyY84rVC3fGQJqrVWblotE88LUjUM3re-4d1jBAAU9dC663-9FfCJM5Cd2W0mOl3oCwUUVdPBpB_VUzajM_ZOghE8lZHBYY1ptdhfiKIgZAwJcD7MZUuzOsaEIhqtSpXZZxm5G_SogUNeQ1aPFN77jFoEAVyj_Df466taMZbg4rVN6RHTQ7BoR-Q-smhOnPLnd17AEcQr5xOq2ST_wadMZsOMG_afDcLwfgDOAJiE00ewXA5UxjamGIzthvH4vA8Wbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=dYakQmV9lacnYg2lNUM7I5A8YpY0PEKpGAf1mX40kK64dXkcAL57uyGi7tHU7zg0mbQjTpl0qnClr9o-bIxIyY84rVC3fGQJqrVWblotE88LUjUM3re-4d1jBAAU9dC663-9FfCJM5Cd2W0mOl3oCwUUVdPBpB_VUzajM_ZOghE8lZHBYY1ptdhfiKIgZAwJcD7MZUuzOsaEIhqtSpXZZxm5G_SogUNeQ1aPFN77jFoEAVyj_Df466taMZbg4rVN6RHTQ7BoR-Q-smhOnPLnd17AEcQr5xOq2ST_wadMZsOMG_afDcLwfgDOAJiE00ewXA5UxjamGIzthvH4vA8Wbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
- لینک سایت در مرحله اول  - لینک سایت در مرحله دوم  #GPT5 #AI #API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6335" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeHMC5Wvbgj3iINHoU3J3yuSQV2xoUDTrxqEuEY-KjOcqsC_Go-58xvg68_XHtRc8K8htctnjjS4v6PzmCFk-f58yOeZ8Qt6W7-ZJAXbjutTD0s9kUu5Mk0F5cH8xYi1Cn7vWCDAnRnFo0vckYkU3kwRfYZ0Fu74sBEGXH1pHL_718BQIEuQ7igIn650E7pKf7ojWPGbK102W-FEPVVDAGBMhnq4-iOsIEtob2Wn2zNUfgU0n9GXOF-_SJEbwTz4-cKSw4GEKznRmjeB046NxDgFT5sq360cyvA491iO3PAqRyvNyZselKbnubm7xpuij1-lUaqQHF-leC06thBDNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKP97Q0Tmz7I15KvIz52mDHtf2BgkMdlBE-ERl_BdFCXO2c8PXoPTAMzghtu-Yxqq9vKBo4X07jvX-P5WO22_RgIrZPmUjbPdpoD6YHpjN1lEHxiixLd44-M06LT8nLX2t21k6RcT8oHOT3QdGgpWVpkPU3hVJ1YANFwhCVB9Im5B6vSkDIMF0eR3GCt5Sd3awu3yNuEmvGdsyDu_toRDDCV5_FUYbgEfxK1CepaRgWQ9uJc15UelV4xQ67jNhwylZ5MHD0ZVVHxSNPFA-1fM3HITGFaFS-cXnMGiHTBAj9doEakTcc_nVqtBnGEr9_5sXjYuud5W6smY5TPokCBsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6333" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQ4zebuQd8YjZ3me6K_YLG5-SjacSNjmAfxTpoMf9nxSgTAMm2vdUheJpokBcbsn016_BkvyB62L-BbRnkG-MTOWYP89sWyrvx1NSCW5Ja2A9HxBA_IbaAyasVjc32O68vEc1opChkC7HRpf29sIBnTRIZy9nKu6_8fw9WeAWaiN4njuOtjXYH13wXQt-nzMKeSgGar74TNwe_KH1BZyBSNDMSDDvvVxiQIawjNHOj6qWA5yhCXYaIE-8qdYRDSfLtynLo1OfJKzJmpC2ij8nplGhEQOS6sXTqNFpBJlI4p9bxJDF2ykSfqfhW8z0df0veSgmNIfWgxlMw1WuepLRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwn54JjOtaMuBmPky26mQlkbB0tH1-O-RaDg-VyBlahPxZsr6qOhck4_K3kp0TUyD2myfIvOa1Zk3RfDJKgqNBq0dOxxc4K2KfwjT6H_A4K997JXyJpuB1EStNbnLCOgAzxKV00auaS1ETaxy_aeHAn-G9v9Ue7P6Ncx-ugM949DdBflwgYgf40r9dWlyvkc2jzD-O1EmdsBEdTojpg11lhIVyF9sSuDBNrwgdal8xlXpOjztumFQZvYr-Kad8Z0VNvkWkuYf9SVJpIl97SDhgrs6v1hqp_DzDCM-ha6qpFax31eH4v_DkO5LcoSmSlSdb28-8gwPiAkpgi0EB5K8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6331" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=vX9xjHKBA4wPFiQ5HhziHz42xS8Pe3uDE0k6vr0ATRda53rsDrOCGOBgrqvXESK2qaQWLBYZUWfCIgVkJeeIj3jBr-ok-QmGChXbjHcOK3qOzKYpJZ73slFhmUUyiPUyKYW5C-Whcq8Ww2lXaciHXuh73m-VCpOEITqQNOoXQpDQ8p9BqbZHvxNw8vGPzEnO27mGj9Q-LpVupi46HKJbOZXBuMvZEmBq93VTfY75l8g8ne3J4tVaWd9uFVtOrzIAP0O6ngn7MEIambezo1ESyvMQ3CmJ2_e4VXv1h5spNO7OYoo2zAwrkAojiW7p1P4hBRmYAu0ebMbLD6rYlpJ9HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=vX9xjHKBA4wPFiQ5HhziHz42xS8Pe3uDE0k6vr0ATRda53rsDrOCGOBgrqvXESK2qaQWLBYZUWfCIgVkJeeIj3jBr-ok-QmGChXbjHcOK3qOzKYpJZ73slFhmUUyiPUyKYW5C-Whcq8Ww2lXaciHXuh73m-VCpOEITqQNOoXQpDQ8p9BqbZHvxNw8vGPzEnO27mGj9Q-LpVupi46HKJbOZXBuMvZEmBq93VTfY75l8g8ne3J4tVaWd9uFVtOrzIAP0O6ngn7MEIambezo1ESyvMQ3CmJ2_e4VXv1h5spNO7OYoo2zAwrkAojiW7p1P4hBRmYAu0ebMbLD6rYlpJ9HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNreBIAtjRj3nHkQTWKkemq6YuPZqm5nhi7oScZ5lSd9XM2RKe6Uru_OB2H2ezruTLwcR1IRB7RdQu8AlFsR2zIj5eHNGW671Yg3vdt90eCWnPhFxXeao1Z-2t6kqz2qscKbjn-rtL6wISGg7NrJHcYyEbO61laEyZ3OiXQWIGZgQUvOu7L8Ma1jxgMZ4CZxGUO91uYsrCDREfEODnc8s_L0yb2HYAwk9okHDgsX6ivEOkKBYUJufRG5VB1f4g_abDgnO4jJ5_g7O4FaxL7f5plL7QEmuw8nnOUGm1lRgJSessJoCmP4NjpJoSVEl_X703aHe7TXJH1W1alo0ukquw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6328" target="_blank">📅 21:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIo7lm6U0FrHgqbufTdc9P_XiH20q6M2PQ_ckfYwnzWCA7cPqRPk4I8fsLw7ZsCaoGRS700JrRnlH4lSHUI6LOdo6vusfce_zEYbW7YMwg8pQV07kYBoPNQVmiD9uidaakQmyLovGjF2ayVMxrjJhdk2VMLhqMaWsmDDd5IZlylVu0pQcaeboSkOOs0xOMf1TCIENvzkHAI0BsPa62mTDgNtA8nQBhlo8jsCnMuCe-Fl04xyY_qVbRdWa7QPwjs5c0XGlBQVPGqhEz7HHOAW_XfyLoRFQM6ZkBgq7kATS8ybxekqxI6XpsY2cd6HwJaOYaneqmzEtgxrEDujRPpRVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayd0tGGRff-PMY04AZjrko3MgfQ-XXWM95vvjHLB5ehZnpTn4tX3doObHQGauJEOSc8gZ7d2FPS8wgOhn5VmhCKnOzbbJf09nyn1Lyx1-tLwCwiteae0FWGAzHYnzvdHmsAEKkoqt54AI1tN8A9-8NHIs5sKtTqdPkBUL5S9j7hyj1s95VSIit34gnp21PWAgkRTQNdwSfWxh8RlyGs4l3Uu5dcEYvvg6vOGIu3WpGUq7t75HffU6JUNW3jOUVHOGkjdj3CQwLMsVNSJNRs0dfsq_lNUJAAeFu3YCudep0c89Tza5ilieYAwiNkE29x91ec6IB-2E_1JPf25WYhQRQ.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
