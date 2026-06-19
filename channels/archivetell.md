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
<img src="https://cdn4.telesco.pe/file/JwrmCitxYlfG27FkdPHE1LcuQ4_hMLryhFdp3lzxW0icrN4M7lGelSdS6ahHH8RVwl1B9JFQt_kG8Ou9orALZZmVN4KMI7enba7l0CIKOkLTDgCbpaan1SaCDUmPR5y9TDCWdz_l7DWA0s0RGAuBHs1EE7ydmoZH1FdkdD73n_-nuzuFAJiMv1i7xwIpGR47tugqhyuxQF-p2WeAqy4RtBzaSccSYrYrflLlDQQyzdRNvbGt0w2gNotPbH_ykVmjxymz5sYDnLBzXaRlWJjOMNXQ3DyyBZ2RutZc5HJiic9C4IwoAUk_TvJZ03IiWwYGRn-v7-m884TZGB9hRJSXRA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.65K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 17:23:16</div>
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
<div class="tg-footer">👁️ 958 · <a href="https://t.me/archivetell/6446" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/archivetell/6445" target="_blank">📅 01:03 · 29 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/archivetell/6444" target="_blank">📅 00:41 · 29 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/6441" target="_blank">📅 19:02 · 28 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6440" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFMKPfrAYxwdXVvc3fqMS1dXl-B8eWd6X_nQCDH9IkOQqNV5JS1lOVVD5zlb2j_LBvYXPIDZ1kycOq7XZehWLIe3A_8NMW2RYfVydT4QVs6asg5L57UFCrWjfouQkUboPzEaCOGrhYux9za1gyV2-zpErwJZjACGua262QQhiBRJ8oj404jZICpYu6JUNpN8V0weifW0F_a-Zu0kU_zEDktSU_P4pUXFN2hjfPl3kPOkup_bfWZ3I1xbxah--euqp_1OqOhOJTh30_6DuSfbXVCHLQk2fYpOogkZwBxrrcOfM212-6QMMFdnLdtroa7Avl-1i0DjtlftkQN-idgSrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
راک‌استار از کاور رسمی GTA VI رونمایی کرد ، پیش‌سفارش این بازی افسانه‌ای از ۲۵ ژوئن ( ۴ تیر ) آغاز خواهد شد.
#GTA6
#GTA
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6439" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6438" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-WC6w9qnMCvEu8kp4WeYD_HvRlw9Iwbs1KJyvq-AysodwHQxXsxBtRr77X6-6xqqFu5B7QSILI615-Lqjj857WRw48SGrT27jVbHfxw6JFvDg2d1Ivp28QV5HzyKSwSzzP_VrHaGOsOpzZ7qd7izdLoakIvaQsSDQ-TarTYe_5Kqeo669VBXWXmPDBVDOv6AOXa7KiuPueg5ScoGiCkbxR_L4c4CXo5tqBfCD7n6TqjbCZdtXM66TUfivhuwi1qMgXhZH3SBlfSLqIwhb2x9Tf5AWYMzp6uTtBGnaLkvWCwqcWe_PDRblLvJ4dm4B7BnLL70_pjjzl4sGcwc6E2fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6437" target="_blank">📅 15:32 · 28 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6436" target="_blank">📅 11:50 · 28 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6435" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6434" target="_blank">📅 09:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">با سلام درود رفقا میخوام یه ربات open vpn بیارم
دنبال پنل درست حسابیشم
اگه کسی پنلی داشت که بشه حجم و کاربر و ایناشو مشخص کرد ممنون میشم داخل کامنت همین پیام یا پیوی بگه ممنونم ازتون
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6433" target="_blank">📅 04:26 · 28 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6432" target="_blank">📅 22:01 · 27 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6431" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6430" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6429" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6428" target="_blank">📅 15:33 · 27 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/archivetell/6427" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6425" target="_blank">📅 13:25 · 27 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRaH6EU-2AQGpGkFTrUMX_GkR5G8fWmbWclhiVMEQ4sDGfNqadFXaGrJaatIM1w17utNxBVetH-AfbH7ClSNZT5ulL0hds8EPEVAqFB3LyuLygWXgwT8o6YxPM9Dmok0dtYwFPcBHHcDjs3DSifAlHniJAx1Nxpgo4DbV4-9Oc7hkBn-S1be04AyUm8eisuTI1vscztF5LJlykawuXds5rqdmLCgeRBaXsDiR9dyhGzq2GPYrp6KnWtU5v1ErSPakvXmz89Kiv2oiGV8RwAEP0HUwbvwGtY4MJF3VMZfHLY6HIA-uCtANBCBPOMGVYS2UPno6SBqUeaB0YAUzYiaog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت api رایگان- GPT5.5
لینک 10 دلاری
ثبت نام بدون لینک، اعتبار نمیده و با صفر شروع میشه
وریفای کردن هم با تلگرام انجام بدین که تایید بشه براتون
با شماره مجازی نمیشه(چین)
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6423" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a7SuRKEy6XVE2F31WMDor9ySGyjx3Rt-KZpZuZvldjGBVmw9NC4ZxMMOJvsynkP8BBJDKRH_RV50OZcdCKJmEKoaq3qVce4eLgm7QSiMZ-zCLAxjIZrB7cGPYD195b_-tpu6Xs8nf0-DnVMswvufi62W28n4kFmnAFJKl6rxlNFTdQBPngUblQL800CVTceVree9g5QYjz3Zai2A-pbAoQpJYNPeU8KyjMSKLHpAziGDMZztskf2ZVRatM9pbhqi50EDrS1YZI_i5b4dZ2L6hbv2iSm_R8MGIZdyUpJNCS_ZdRSgnNWsa7HCGX3TnNj4v4ZcVREhPULt7OvSwo7Dlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uPCZ0Q1KxcnW0wVmJ_rU9taqWenJfjMKNL5sM8NzUKnlkynniv8qZYTW_sZN-6AFvU6dl0NU1EGfUsTVmXo_gFqxCBrmSo7Ufr9A06T8YzrePn8fuD6NuVN6c-cHVWH8btBWbKTyYOWLzKfXRt9eZvAPD4WkVtxS6AN7Rl-y60PmFaz1jnFTqmIHHpI6KMWPM3gGU1MyVU1iXd5SJ23qosvyT70KQbeadEBCiqdR0upsskSX9D2ll6y3jAxJutq5vKXGhFrNhZoc0ry5E2iyQWJMyzvDPMOeFKvTCU748frqjXBCLXbikIDuUduikgNe6TWarsGOL3guQZ7XGMMlDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_hlhzTF9EoJstqLN9t-B1gnJftmjRburw8kdKdFfRdKJVpul9xu_d3ka0Vm1gkMPSFncUDObi3coheL_I1JfVzF1rxGJZASjS2-_uQu_ZCeJ3953pkNka3eIqvzBlTeFu5aMOz1xM5QUuhEhEsr0jQbnmkcZnWWPrvCpcN5WtOQr_7zEAxDSZNLcJhVsa-VAOk8Xz0RW8CHylkmUkTn_9uA4P5sBN_yIu8iKEx5_hiAg1Wu7ZaSKpEbZ19oh3VD_P0dInFbJRQ5or4huYkxF0pF7knK-iVGPN_itBejAFr3Qo5cq8Ta7OSnHt073txjDehVG7bBZR3kyWlqIawWlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل جدید GLM 5.2 از چین معرفی شد  توسعه‌دهندگان چینی نسخه جدید GLM 5.2 را منتشر کرده‌اند؛ مدلی که به‌گفته برخی بنچمارک‌ها عملکرد بسیار قدرتمندی در استدلال و کدنویسی دارد و توجه جامعه AI را جلب کرده است.
✨
نکات مهم:
🔹
عملکرد رقابتی در تست‌های Reasoning و…</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6419" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ns8iczNuf5hRI4UQTXhIzfMLETs3EtaSK1IrHi3jqA2TMw4bByI9FfDex2jo7E39euDnXmaG4AqVSHzpX5TumJmhi2lLSeRsDWshiM-_5B-Lxw6sfZdUA9_rtERHfZJ56hMBehlC3zrrdEOOo8r6_TtOwOa4DlBwRia8QaWBIq37oDWFzsDM7nKWpfPe9RCELsd8gH52RlFaoaZJH_zmIqh-Bb4KWdL5zMs0Iwqirv2LL-ClQ61I6Xmvi9RWrWGQXxCLm6LEChIFjWhjENnI73Yorh-ZaAxid6Ab9oDrEWPJT0WtFdsUahAQ04yBoUbn-RIeg1XT6AI3vl-yL1rjSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6416" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6414" target="_blank">📅 04:22 · 27 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qfc2zrqLdb2C8_WybWeqiR86rFHHXeBIj-Q_O_u7jY3zqyBeN6MSQVluHAB7cszv0RRhV_91Jce8Xyz_ELg6azMzs8mBVBa_ULfxLMD_uL5oISnuL4vZvis2P18wyQw9O3I0RHGd5SoZRPDzkNKDBScGKXCuKuURMPeclOve-87WyQrqLhuLTrvgJdq_PKDZ793jqvR04MmyCNPJ5xCJxixZ-I7PceS9by8ju7teIGC8bMkTMnVj6F3IizgKRpDgAGqWF8VhRw1lnHXnOLrr7tY63TeVVYr_Qv--fd00-t4B5S2zIb20Xbkv0hcunjzyiawlYwK-U8Z6ivKnZi3vpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/krZFVTxekvy2Gxj2GOrW3tIsLldkm9BIecrmQZvxX9c5-tCdezJpRjt8giWVWjE051FAbJ0JPD_0jaxOL9v4KigWvZ8NgR7aCmJ6GD1ze9uZI_k50K1zPhtn668_z_4suJC5nHhUb06kos1x52I9r6Ut1bqrauPaHjQphmkr8WB7y48cqgfFi8rhV1ZelVRXK_C0GRRkmYYCyBaKo-pDI-H-Uw9xL2R50mCyo04zQ4jMFu-NpJVimE8jYZZw-3Ua_-CvvY3nwpbj7JTAdTW5081pIeBH3JHKLsRUlWhwPyE6fBk8dOP8usoNW_mh3AV4Bev8sF-uGsbyZFNBl20yWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NfI80D_IUavHM9KmUcnARumDxdFk1hk9a0lRkQaI_SF1v7A5fnDMl_FeMqaUQ8MrPB-izjNaYvNTDnW9DjQ8HLclExrM2sjLZ_p5eqRc6Y1KJ0oQDs0VnaQ9uNSHtc3eO_YQ0vr4ap61mNPqUf8pjOBIaAF6jkOP6Nef4jfW8bNaoKs6HXOwVFcjyMh_x-wwsBavjr7ryPf97tQX_cHc9YO5AfGm5yY8cWnjJif7zWWd3ZRHeg_DClZFtcMUxUU4q0xGnYFJagcjgO7RTDvM3uYujCn5pxQI7JomhxpS4UgCf3BIZmqa-_GtTJo0T69xpO-algyhfy9KIMQHjdKdPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CRi8oxMAUEAK47fSGPlFi0Ig4ONyEFTIjJA9gnNqNgcSJa1gJp2n-8jzTrB_5P-rbmLUnZCtOy-_CV1VssmZ_pyowMj7pDg0_q5gO4SUxFA3vQprjJFXWqieSr8iUO0bGuGRpC9N0RUazylqSWJUvZFGPc_vdf3MAUFYRswvxlhAKPeI5sNJ4DsXurN5fAEAU1j0EkzUkn76p2OwmOOpjQf0ApeZNdwB-ULUo9p6nvzLipDcmy72i4K3dWdJ2gbH7fj9-y_3lHO7nJGJIYe8nDBK8LidQ2iYXiD_OqfeCLec9SYO8RaAsT8kaXlMkFbLpW6Bw9NGPEB4r1p9O8_wEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت تصویر به‌علاوه کتابخانه عظیم پرامپت‌ها.
- طراحی‌ها، تصاویر، نقاشی‌ها و راهنمایی‌هایی را که توسط هوش مصنوعی و هنرمندان و طراحان برجسته جامعه ایجاد شده‌اند، مطالعه کنید.
http://Arthub.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7s0Uc1V3zCDnWffC5yecttut2CRV4oMjDTuXvwJHb2cAMaMeDh_fyfUC9imdCSdOaphv4oR4Gsk6GTVK5wL99OhhOqjSIO-Ck_Apsc8tbLDHYCZVt7n4cSPbgMVDFIfy4-5UxZmlgQzxYF4vnYvbcdA9WHKxMz24CScrgtvGR1s_bgmcp_mDuOaeheqfMVjgSckODZcnnqDBJ_xA9dtdaWpBScSO6gbHBYh7aRNRn-qWBSbLs8acge6qfA3v1fT42izu0K1ZNlzPzCQ_3wKqSS30yEQ1YJAElhjuJRaBXSRdy80zHgSam-RbAp3Y81vVoO6DX9c5yY57rFdSiQ2Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087fb590da.mp4?token=kElA5FbI9zV6ffglLVtCPr7eQm9yMHF_Glx6achpLGHlrO44urnOwCHTfWOsXbDf9hwuHuebclQx7VqhvPpwtnbKTJ-_6pUSA3vTRV9jbbIusfqaRtmI7E79QJ9ZsBxUJAvdSWvmVfgxL-HPF2TYIJqIqj69VRVUydDRhiifalCshue5SdUliDoL9M-6CJ6p2NG73TwoxmOPv2dPtGBzsdSIwDEjUI0Um5PsXp6LkwumbjHIC4iwuiGl4P6XX3RgiNbC8nTnv9m3EPooE6i03LcpmknMZURahgDuuE9vrlcfpzBc4WSQcjMlf1pG0WQv8B0rbjSZc9PPZdY-EteSCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087fb590da.mp4?token=kElA5FbI9zV6ffglLVtCPr7eQm9yMHF_Glx6achpLGHlrO44urnOwCHTfWOsXbDf9hwuHuebclQx7VqhvPpwtnbKTJ-_6pUSA3vTRV9jbbIusfqaRtmI7E79QJ9ZsBxUJAvdSWvmVfgxL-HPF2TYIJqIqj69VRVUydDRhiifalCshue5SdUliDoL9M-6CJ6p2NG73TwoxmOPv2dPtGBzsdSIwDEjUI0Um5PsXp6LkwumbjHIC4iwuiGl4P6XX3RgiNbC8nTnv9m3EPooE6i03LcpmknMZURahgDuuE9vrlcfpzBc4WSQcjMlf1pG0WQv8B0rbjSZc9PPZdY-EteSCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aX-SDWfFYwvncGUcBbnj1b3IVezDhJRFL7tPylF6JbBVBi_VSDKdnUPU4OoE46OmmkfoYIC0Ej-WHdsUSrj_TUhNLc7x41Tb9NT4njrOvzgRiM8TbNaSoONuyjvx3Oaxy_IYw_cTKt6iOS2RI4yD5zZrDVnA25o5CgezhwswzW-8ykYOu7Q9JLSJIA9d6C9uYKRhjNQ2M6j-NU6txPeG9EfGxCRlGe_1fpTTtaBeLO6bEyCpkX2VP6v5DnaYuzXBq8J3rz8RBun7S2IfOjnGvgxZ5TO1SNk8320HwMwWp5fhyyAWdtV3QOnUTrpD9YYNc0hYcUuFHz4KiT4yNlquqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pT3DW73mwFcFkBcI-_MM8Hma75JX5WwM_c0WkAFlB9XzrzPuKPgcGKx8QHxYC5fXS-z6E9cGwl8YbINjQj7zPq4fTATNU5PxiAL8Un54r4XxqRXtSNZ6DXmFZWRRtEmr_h10huoqtGPMMvIcmhoLDzQNQ40FUXmFldj0671-GL2DwgPttuYcJNWaDvERTx6oNv-Eh7dAVcOPxZYCtnnmb2EasiIAo7ruZ-Xw5lCYbRiou7Ytn7YLmVgKlnURoYV_Z-c3umcVMmaowQyulgUp-qG9YUCege7KK1VpHKYElLv6k6WkCndcQqYefAP7qW0EIOuzarNoYX8_Wrd41P3i7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت Ponytail هوش مصنوعی را از نوشتن کدهای طولانی نجات می‌دهد
☠
این مهارت عامل‌های هوش مصنوعی را از نوشتن کدهای طولانی و بی‌فایده نجات می‌دهد و به جای ۵۰۰ خط کد، عامل می‌تواند فقط ۵ خط بنویسد.
با Cursor، Windsurf، Cline، Copilot، Antigravity، OpenCode و Claude Code کار می‌کند.
https://github.com/DietrichGebert/ponytail
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ad6YZXPLbnxk8XLeJb3WQHO2PcuNE4WXJAVxXrAf0JN3j8BYy-GRDepu5AT7YTvuMA6pPKFbhxh9mZ7WlDB5gk9dH8BSsxvsb0hooOY_OCC6s5pFfgeBLJVCR2DgBdpfUJgZu9_hlOUTXVxg_moJi0hDzYG-qxbyxRkXiqC9fpEcywbF7zZU3_8X0FjkItq1xo7MO6YKiSCRlHg64ix6mI61wT9lYyANomq1TLEfuIUFUxVkRZTf4FXoGj0JystABkbUfrwprO656FhC31nYmPRLFBAkgvRteJ_PynAeSl97gqSwaaF6ud_dH4z-EM7EjwBvx5jfskbx5dKs4jgtrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvRcPncghmxc7EHHfjri9dqyoJRLgUNG2iJ0ZEBrF4aAb6RKL6Dlvpz5eyCf_Cw9vz7reSK9rA7_p3SAumGL8Wf7Nq3XSFLgTz2YnID5bzZAvBTjdPg1w-PtY10qV4Tddz-53vvtomx9xLe6kQyjWeAP2l2mgrbX5-E9MOvbEFoRWbBsF4htCB8thqmVV-uxnDgOcjDqMFqbuCd8JrIJ_RDa-SOWAFzNP7i0zbu7V8ZQTDuhoYaxizTGHnBdRhX2oKlCtasjQ-p8f-fVUFL14iKVWvSQtA8fhL71akjPQm_zrwSByv8DLjafY7euqFz8c1i9pCeDpiMfhktJONnzww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZNmyeDiQwCK_dq5jrQIkYHQoKXPNkv0pafvUJkWWIP5uzZozAgIEF8t9IRuRXW0u-P4M6qaVZMWYQBAkMmaQQtg1f-ejjYP_yj09vd28QBDHp_KqFwbv_X_XcNq0ircKZhcpV1y1PfapHHjocOaFRqpC7W23JCtFh_0OZNrNj-NOSRRPsL_sPiKsWjt7W4C9W0L9mlaGfLRNPMPdXPFP5gyoAl5WqhsShsBXNGeMFbQRM8hwt3UCqP4p7yvPIp6Mi3tQO68sCwoSAEk0vXH1iwk_dANU0NI_SHFGd67LNbMtpoK8w1mHErKQeHU1_yxCP3lDixULAnTGYoSNjA5Ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GilDetR5hAKzk_d53BBiV68G7rGzu0LaLvvMVl3LGvA9EOvAhwSdvhMu9b7IuDTBUFty5z50COL0ITinzkmsqbdue5I1jGxB1pN9gyJlzk9xZbk6NvL9XFkrkK_L6jClXvT57fPhrA2a3sy06t5bawvzBIFyI-ADA9vc8emhVwDxvAGB5hMuxKl9WOMRtPBhY5Riav4dwhg6xvdu5YX2B2OCuVkcQSQVnKKSB7kVE90RdF6MqF6XXZtmSjcqbWceGNk8i6ltf-m6NnEVufevl-a7WJWZ4rrPYs-cWw_ttaN4IBaoSCGEPSJX9xwcZpmQK09bJz0RbSSbEUE9bylz8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAJQQeVaT4O1YY4ofFiG-f55pPgVnRlmFFOCgjWGVhNWwmi_PNlS_IT0q-dkx1AyWraOT7RUDsTAJS9HZFe10j-GR6-90ei6Zx9oIc6ndjRjZyhDha3VtgfofPJkS2UX75ZtG6IZfdtX2B4dt__ramVjOqCfwECACaPDS6dko43Pmlm8qy1lbFc97EHhzQNKPddfR1xDHBnQtUidWUcszoq6CyDeK3g9CvhPxeS8N3-4CGN0r5xCRlSWl7rH1Mz7fb3x2evTZOnjQk_R-lFWrmxrR-4vKSpMkIyQ-foN1yWYbS151jSFjlouWNIDCbxhqPrNytxNBC2FYegm16mYNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzQw22mluOXsxec671rHM1coX1dsi9otbQkS2b-Zr7uUmlUp5OzjIfYcszK7eigPrHRJ2Vj6Wi_ylMH3E-bvBILfDPjpSsba3TeozGDdxhjt48dAr5z1d6pqwQyqAZo9OpJaUgBsdkJXEHWKJJBd1DDWHkQxKJnK6eItIVy9_YBtnfmxrenUgI1cTrhyBTh6J2SRPC_bluAVq7YR1iC4al-TYLDMn04pFPExXI3y9d5fAl_6m3t5FfMgGuCcTz89dbDBz_70qwqH-jBHaQ03o1Nb-KYZZHL36XGMTFYBzovCcbdcsyafJtyWIz-fQjsVMriFluju_GaiNNCxCqwBjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SV5s7hHDqNFus3l1MEkb5ZvpHWa1_sk9k1BwueQ43rxZZZXshgM8qCX_QOjHIusBEOcoQFE6btjm_HFtjUZMODowfvC7sT3xlEws7shhfphMwXF3rVaelEhTT5-djtQNaRrbtDhp4y_eZgKpzY29M6MuPErsFcxxv266mhI8_C7QCwhrrU3B6_R_njuNBj3p5G_e2Z9AGuCZ7GJqNVPvPwu8exgO2s7Ltg3lKC9XB6akADQ6cjscsI3738gkdbKyGEZfF5EaJ22AjXskV6byrRbHWEU6hPw9lCubZaK8dQLv7TM7B2ud2akMrUU8g6uPswOTaMUkyqSZVfd4yz0oWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhbVfW3G2rbMryR5-t7DLwSjVn8qZe1B3N5VA9GT5xPCAbOttfuRtsnsKzJ3jmEjdQ2HnTwziioPpKzJ7jHB8iAHjWuP-yY2Sxc36Kk7g5Ri0Yk_UvGaJAHK2i5c4Yz0_u5llvGnmmZfhi5TkARp3PgF3sIwUUCoFod_ZiWoZanVbOa8wAjO-TDqjAzE_xaiN0FGFGR4Jjpc0LnjzvRSB-QUavx4PwTrxv3ht0Iw4nYRDk0Fze8nCPZxAc65gWRFhODX2oUIved76ujEllmqt8OmZ6IVYUhuo1prS1GbK2Tlkic3WqKzt4LNrL9iibOEQj4Ex6rNVLt_Cc9Mncaqtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnbDutm9_-lH3FhSKShq2wYLCTmHUFFrQUejtuH5Lrn7ZuxtEfbFOn0nipARhaBUM1xpWO-YMvC3srZG2T7fOYJiwuFD1jSj2L-7cZ2zppC--GGuRGgNr2D8Cna0R7xJkRgZZSL8IbET25eQIYmsI7NZZxs1CJjMojBSyiLthaeXrOJjZk_Vkc9p8mXhQ1tI93GLR1nNkxSd_yiloloFCeUFY56y64cwCOdESNUtwS_jnth7mHDeVWc3B6gsXdgOgrrKF74wNP4KT2Xg2TirIHjd0uYWfzXHzTK3KhPyNpt1sN_iH6A_g_d4pWylkOupJaXok-ahwq0cTOTFVisXGQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=AMvW6evj3u8ZaG3WGqqI-tw_Xt6cXpygd3al2UwsXxHeL9G7GIW5pasNtL3-MvokopC1gQCeOFc9-J-eM9yO8Dh6YoejTxKLDLX9-OB00E7xX7L7lKfS_Dig9bOzNgv5WdNA1EBTX3KM3HvNmm4zBl1tSsySIPxuZHE73mVIlUph_-KGJdv9TIVwxZ3TPHYlj-qnPZ2GDPmD2ZTs9pAsCPzSeLogfBD_gWy6Hb2DIsMxFKY0APMhZ9f8Ss0cjB5POUE_ChjfES8SOFpHHeYAicfWSMGYtVE-dxKw_QMD27JD6iQgLBLb9zMxRnIjDxTcrmWHqVW1GfQ25PRhHHaaew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=AMvW6evj3u8ZaG3WGqqI-tw_Xt6cXpygd3al2UwsXxHeL9G7GIW5pasNtL3-MvokopC1gQCeOFc9-J-eM9yO8Dh6YoejTxKLDLX9-OB00E7xX7L7lKfS_Dig9bOzNgv5WdNA1EBTX3KM3HvNmm4zBl1tSsySIPxuZHE73mVIlUph_-KGJdv9TIVwxZ3TPHYlj-qnPZ2GDPmD2ZTs9pAsCPzSeLogfBD_gWy6Hb2DIsMxFKY0APMhZ9f8Ss0cjB5POUE_ChjfES8SOFpHHeYAicfWSMGYtVE-dxKw_QMD27JD6iQgLBLb9zMxRnIjDxTcrmWHqVW1GfQ25PRhHHaaew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AraOITvYQtT8EfcQvFq8Ha-dGri2KBd5Ym79rEF9CovwTpmVB-6OO7AT8gw0w5L28i4b0AfNbM3qL6-gJV3xYDgyQYqNi1gIryqfdHikahb3JlR3w-CdclFm5Yr-J79oxSiwjH9Q2fbypu_KZTe9MdSoH9FRxAjnKMeyRVyloEY6OZ9ls5dg1NRku9EFGj2TiYfVPxKpNoOAKN-WujjJ4XAjPIGhQ7weVh2iXf57iThdwvZD_VcvKIryGvcTivlD-hTW0_gZet5Z80pgq4A7A9C0LwYaDRjgC86mz-ekGu3Kp3suD6J8eJlQoQUgu0z_rUQAPDGDNG-8ESI1mm0--A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iy0j2Hxr4edQpIW1N1hqY4PmVTkj6iB3mWXa0mbmh9XiI1MsyK4LUl0Nbjw-3x1wGpcFFa_g1rs6nszL9AITHMsuf5DGAYQzmsLHpwnOtug8v-F2V4rw3K7tGhpUlhi3RXGQBympNjNrDffkO1G1vz4P7XvqqxmqjPN8Dn1FfLSN5dJb0xQ6zYuluQRdNBEpYtz1pT1H4AI9ILDrznat8m35MRMpAmBCa-xLc5rj28MC2gmEauKBDcNWwQ8E1H8LfkL8UM0pf-Xhs-NqZ80EsNRNCpVfIFZK4Gt5poDbt79tVk_3KrNR4WJnCEu37lJIDvPdhkOVdDonKuN905xbTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=BxSH-mCg67dDyho19Eep3XzubpAO01a0y2jO5Ei7iMJOjye8PsmW6tZJvurUCTXPxT0brC3oYQOpKklttt0EcAumaAOnMk8SOd_v9DgADhSf6fPR-Cz-sQl2SrGgzDDQUcWZGefcMnRJGPfm2rwdwu55UyfLcS5U5t--94N59aoAyKUxo8ef4150VaLKT2LnQxmZmG7rVobuppy8LwSt-jb1yzYgpOdjAu3qh_wguXmjgRhhg_dpLbfEeiR71BQc1X71YldtWnC0pEiYJadt3asylS8HTM3oY3AD8wyIdWdgNVmtC2qISWWHhpNqinRUyy_bVpnAV6yUAJN1wDr4TRXDq0LWSuK-45q2aujxqznSKE02usLc_qhJ-NeLW-gqV_4CzNDpAx7y4Bu2ZyEIuCFjSPPS-HlE4axyXweT5UmaPeFw3NMYcFqeftAGc9Q0uqyT5iLN0XtbVxT2oBd8QVVvLpJ4u0jsH962LANkW_9O5zp4s3JJSDYlwrS9-4B0RpFDKbFR6NnqvYcZNdDTvhsmveAMkimwsDs-W9uAabWCHdVJDksTgclY9cXGbv7zY9x-ExZi-1hafh_0P-vYB0ZQclTpPt32pTHCVQi31eRsKaIF_TBnyIP8VM4ByZE9igfqVArwFP2YoWlgnOxjZgHh6ybiUMNa1zQwgWhntxo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=BxSH-mCg67dDyho19Eep3XzubpAO01a0y2jO5Ei7iMJOjye8PsmW6tZJvurUCTXPxT0brC3oYQOpKklttt0EcAumaAOnMk8SOd_v9DgADhSf6fPR-Cz-sQl2SrGgzDDQUcWZGefcMnRJGPfm2rwdwu55UyfLcS5U5t--94N59aoAyKUxo8ef4150VaLKT2LnQxmZmG7rVobuppy8LwSt-jb1yzYgpOdjAu3qh_wguXmjgRhhg_dpLbfEeiR71BQc1X71YldtWnC0pEiYJadt3asylS8HTM3oY3AD8wyIdWdgNVmtC2qISWWHhpNqinRUyy_bVpnAV6yUAJN1wDr4TRXDq0LWSuK-45q2aujxqznSKE02usLc_qhJ-NeLW-gqV_4CzNDpAx7y4Bu2ZyEIuCFjSPPS-HlE4axyXweT5UmaPeFw3NMYcFqeftAGc9Q0uqyT5iLN0XtbVxT2oBd8QVVvLpJ4u0jsH962LANkW_9O5zp4s3JJSDYlwrS9-4B0RpFDKbFR6NnqvYcZNdDTvhsmveAMkimwsDs-W9uAabWCHdVJDksTgclY9cXGbv7zY9x-ExZi-1hafh_0P-vYB0ZQclTpPt32pTHCVQi31eRsKaIF_TBnyIP8VM4ByZE9igfqVArwFP2YoWlgnOxjZgHh6ybiUMNa1zQwgWhntxo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=MXiii01SYGkRtLR6Ftpsg7jEYDRUIKekyLWOboMfkHwLpznZtWzQInglgeOKczZtDctKAnbMIL9vrQP1OvZVFZvUckqsQM72hxuG4tl2a5GRjFOdzW9EvVkA0kxVqRF6pRa8mBe2TiORRtgsO3Lp-ftu5Y4Rc-CW9BHWID1JCcWKZzVsEgPvlL6Atc0aDUlAMZYCKZFOIgytg6Q9xanzUzNNsk-jvbArXmcXfrMnAIcrPd9n9AyszxjD7hTfDy3TATODh21pp1gjDCqJeD8cgctRmaJwWuZuJnQ4lNf_X4KUVoDRu7Y2-ZKzQ93KYk2J0p7RPC2D5C3Ftsd5xydwRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=MXiii01SYGkRtLR6Ftpsg7jEYDRUIKekyLWOboMfkHwLpznZtWzQInglgeOKczZtDctKAnbMIL9vrQP1OvZVFZvUckqsQM72hxuG4tl2a5GRjFOdzW9EvVkA0kxVqRF6pRa8mBe2TiORRtgsO3Lp-ftu5Y4Rc-CW9BHWID1JCcWKZzVsEgPvlL6Atc0aDUlAMZYCKZFOIgytg6Q9xanzUzNNsk-jvbArXmcXfrMnAIcrPd9n9AyszxjD7hTfDy3TATODh21pp1gjDCqJeD8cgctRmaJwWuZuJnQ4lNf_X4KUVoDRu7Y2-ZKzQ93KYk2J0p7RPC2D5C3Ftsd5xydwRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7griy2kY82YODLivqzwRNcBMgjVds17ROf-pYzM0ZltNzdSYUUpx5tYryfIYf115YkAUVl32RR4GS_M0p6ZB0yTAHSYOcVraBnlgwzLzA2g9kC4TGL_kSXngSV8G2M7Y610nhh6YkLVE4WJ0oFOsr0Yblbm6jAZykDQeO2IGynZ7hrWxExB_CqC3108kz-LdNZ2thela-5KXSvAqDI8LXazjg3u5AXFX637x1gNbiryuDdPgpoQSIf32QtGmuSID06h20Y-_9JmzMumEeoRMk34Q0zkaN6ngSQuDRUbS06TIoUs2JBmz0U66eiVdT3m7fxXxd-z1aT4L0T2mgqfLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکن ای پی کلودفلر 2
نتایج این اسکنر معتبر نیست یعنی ممکنه پیدا کنه بزارید تو کانفیگ بازم کار نکنه
بدون vpn وارد این سایت بشین اگه باز نمیشه واستون از یه
اسکنر دیگه
استفاده کنید
https://cdn-scanner-pro.vercel.app/
لیست رنج کلودفلر که پایین میدم اد کنید و اسکن کنید.
هر کدوم که سبز شد بزارید تو کانفیگای کلودفلر
با پورت 443 تست کنید</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/archivetell/6347" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkCsT_HudxXvYPmqARye19Kr98HppidJKQ-vGlM1RaqINdsgUtiRyfkobYJ7p9oZoGkLhw7lSwjxNSth_2BJS-mR1XB-zM6Q5uIpb4c1rYh54n9ksgVaS9hoSFfA09AXs6348naiArcq75d0FUs6EHBd_kKQb_0gm_4XA0tYcbtQkzuN4qL7gPwciJVqIaePeKzJ9d6QFZrYiYxiI73TVud2FZcRaEO_5sfsPU64JRXjkRm7fFFUQASk0F-HOCdbUOnreWA1VEB-TDlzHzBHxrGscWqR-tytWhb2w9iDbq9UI0hxCgTMjMfp_i-Tebe7NfeK-NnFIHwkC__OqmSChg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hJSVfvFCoq0e8SbWjxDX-4q0kwO02j1TkbqRr7cgl3o_mAV0tTQZ9pgWayET1a5vQiAYK6VNpdF5g04Z9a3VFO-WtG1FMgmnyx8rrkjSjzdLEPcX0a53-qoGq34Yem8IE5PFx-A_k-sx59Jz-AqxhFUgSHYlORAJti456rNxx-SowvawXNaxB11xKvn4fwRbVZ69MVs0i-eaCQrA-Kboe-m1VR_gkG7kbPlnlHq52Me9R8DivVx8EEQwZidgJS15UEVC1JZFzGoq3UJ5IJ74k0n5pijYU69YDZx-8CrYmsH8khTZ1ej3RD9SRfUwSlZVAIJAkGfGnPsTRUbXIgon_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bywsLNC4uJmeYZAz7zVJqTskYbkrfp0XX9Zjdawm-O6EejPy3xDq9fOIBYP6wUSW6W7BUfQ42sEEkDa4pqc-6L-fDEdAk7T5U0NgEapZV2ZBRi32FWFveWRIZlzsSJVWn9VkrXZ6GxG24hvMrXCRJ9R7TuY2bQpVRg5CznBgb19gqel6OaGUNrOGjKCPDO6HtBWseww3hIQ47rjKJNtWBa_CXAJHDXM9H-nLX-wN6_osnVN31ECJXr4wj8WRto3m8y8OJ82F7yYvplq1MEG2Zv2kk83UnwqgLSAgU6gVSpegfPHRJPs2QlnR5SV4RR-8fgZe7WQxIihN_gzwMGgWQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SUaqzAB8bxsvX2PUC-oxRv9Kf9Kn4OPg65IYchcUwkPLy5Pe3V6RXreciVHxfw9qk1sJ4Fp3LDba4ZzJbzl9j9B-tr33NjCigBHqwpRWn0Bsj0odWrgQswHjKEunF_774RI3tY-aQp0FwwVDVK-KC6cdk-1qS4sqGd5bkJfe7wfwYX8E1ktCvGsmxN2QW29BmbqnLr3jNT3cVpB8mTs54K2awDKguAyZJCAM6OHrUTSiXuCfW3abkxUWVYuwVczkv8FpVC5VJqXicFquoJLe-6zaXBxt7SYaGWlPVHky8RfghUbdn5FZfeS1PZq3ynkQPeDiEr0NlwDkb-kSZhiOXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1mAPoLQIFLKY2swG4vwrCopHF89lcvuXeVAgyKBJXLgltNehX0w4AsQthsEVCMW6vuBOrahCCH1Cp2UrMQGHfj6rYi5YA88-2MxFvVYWHehi5zmmPI96tZHA4D0y8ZyOKBYdHhOX3MOB3zsK1dJHL6wCjS8xqFpB2zYy3qyTHke1Fzzig0hVA_yQsqAZT7j9Tr7OUegQdZeNJuNKDIBpL9VBeQ8JG32IIZxLHHR03syGXHRZNr_2ltntstBGK8q9bSSBUzwFhi5wDxDjXDfNRUyRjs_mWShtecXjRt-E-EbW3WOyR9XaKC3nOe0rcL3nCwCXWx2iU2haeoidiiWAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vu9SxhwqHC0xZ_l_MsomQ0nvrkxvc70TyFZKf0nLeupq5SQh7sDjNnmhXudogHrV0kUZCUzha9fsQQSiFm5kT4vQZqVDzMzKZvTdfmbg8y3jzc24MjuntTmfdYEG6NIO3olVdLMAFezvBZNdGQfIEy2VymYMY1cVYXrgfaAiqTAUgxmIt2QaoutU1XsGyzhnn86ejCdnS0Ya-7yoFLt8zl-tvWvO0bzQFTBuutIH5V7oMObJOcEsxP_Hs2_FYq_8e5vb-3caGHY8bE8hC2px5NoeZz8YT3mGefCSV8hKxACcTEM8TlaI-XwOMUXYd3SEDOJ0GVFaAWenKzs1uJVCLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkIr1DqHFmR9uKKkpGsCz2mu5S2hggOs22kYZyuTFrgTeZrNAmoSPoBkGjagTCVE22DbIjqCS-wX45tXDPD1JCeH5CgXN7L1-jF5qVtST70CX3fYXasBVGFLhYPsVw5K9maDVkAvikvVo3oKmNS9PM7Jw-wc3TfHRp2LgbNlQtIKjayDruITt1ER0-Qj7EaCmifK16nZ7E8bSXLDXEmCuwOkLPjt3UvZujBHVpV0u9EEpT72AJfTNGbrHNzamyNziYFhkwV3ftZPcQ0oZrh_CIMdFzpTgc4QheWdsEsg3SfzqYjj3qgjf1y8w-MQ4YIJg0totoVsNpD0rKBn8E6w9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLlmLl421KjkzUtt7TMrwX7lbkWHFc5IeMEKsXm1Vzw9aNppIrqgPIZle177awZz5CI1MPa3rD8abdzbsTt8g3U5s1ClmqUufZFJVHthU0EIBDpmBsbnhcRCXC28xbjiy94LR-zS0Mc99bElj0EX8ud3LQfijZF1MC-DKGOL9r1pSjCxKKnGwxq58F5jE9bc2ahh_MxY-W_8Kj-lbreWDhJzj3ePOvbQGsjt1njH6ZFqXFuG6g3-Cd1vjyld7f4RYRd74vsM8HDbmNKzKhcDU5vo4043LMsodTBqyk2BgU2ynB-btYyJVJugVLmIfuc71IFx8lSb7LKDCv-z72E_TQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbOUXWEWkGnzr7fQ0Ig03Xa5d1Dr3_RUIEiWatyVObwXwNNX3zQ46ZfaTXjnWSjM02z1Dg7DOZuAkpeDAM1u762E0m3_ZYISXyxsyPSYT51efsZ31ZL8221DsCQySGt2rmcd3yBKBNQyABXus5j_PWV2sNt0r_7ct_tkrnZaTVgsUcw9iXP4po_9KcLDYJKMnSCa-1HLcYAazC3FrenVpKH806FL_dgCWwslXoV52Vrrro7hAx7C9UJAX6Hg3cXeRWkoJv5nDSzwWgD5_Vbl73R2A5IIb_cuWbsXuwwqiJy_89Q9F9gphHE5_0OmfS8EZSUqG07sMNQsy8RpztJ2fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GiKhaKjWNXkMSES8nzViAO3xadTjHkUmcl83reFYSMO3KSwsVefCtSnEnNCjv8j3_Fs4i0-TX9WCvNVxg9Y9k0O7fv72XMxwuKyAl7fLKo0gknd_9MMJO3CKct2_eh198GerVwKQxGwR__UkwhA4Mfl1zSvcsnaDl9AZXjwgW55Zg0etlv7ziaQ-hNY3CmgoN8dEwWjn4wU5k-tli9S_dfXK7A_HtVAMkBAe3UiiGZCQ_H6x8zy18c8UJ03BZB5ZZDikZ5vBkfjNNNJ8zCK3qruf63DkXXAurE7f-PPZMyc8CKN_NjRQTkdU4p0sn6homTLV9gaLEoItkb8nLOKT6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2ThWf5o7MYZW9eN5bPUzpKrCHRuJdK3CVbxVyeM7GY0PczigsGfTp43ltZUisVH2tH7Fs0gXom8qGT1arQr_qPoIvrr1pc7nwdR3i1NAE8PGvvVvJlb7QLRsooWVf92tYFklJ2DbOH4PumuULpvJsYFLP-GXlNZhG5FdIHAj8lxviR4gICKxoYiRHFsfTmI4sDXL7qvxr8mxV_EC7UUDIxD96e49fE93Kn0I4mbpPbPJuY6kYV0IpI2GZRFa218eLtPnhJG2SO7WlXn7N1-fd5GbtcvXQStONF6zVpstkFpudzsn2Yzd8gn8KZr_PVUSI4X5eHbfiflxU_q5SQ_sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=ctqae0vaTo5ub8YMpGUScDyx0POmP1ocuEGiHKi_H95OFm0RVqQT2cbWDK9Ng_Hc_-XfnxchJWhJeHDqc88uKRN-NocInwLuv69057UollPhj4wc7ITNbSkT-Pi8vekIsvAf9r2dsc-te4mSAJJIfvfEw5P7R3lbREt02FftFn4VBMgvEzXU50pt5hir1RzP7FNC1yoxt5PJ1oaEfINENL8PHR1nGVocDuRhl5FtN49e4BaQ9wZRP9wTK9GIa3dczzE-VTKmdQNXMHxG1BRzzwgBGQi6Cc-yVKYO6CMyAlus4KsWVGCFs2Vaq_-aaLd2PxboCqPwiA7KsJGW55b0uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=ctqae0vaTo5ub8YMpGUScDyx0POmP1ocuEGiHKi_H95OFm0RVqQT2cbWDK9Ng_Hc_-XfnxchJWhJeHDqc88uKRN-NocInwLuv69057UollPhj4wc7ITNbSkT-Pi8vekIsvAf9r2dsc-te4mSAJJIfvfEw5P7R3lbREt02FftFn4VBMgvEzXU50pt5hir1RzP7FNC1yoxt5PJ1oaEfINENL8PHR1nGVocDuRhl5FtN49e4BaQ9wZRP9wTK9GIa3dczzE-VTKmdQNXMHxG1BRzzwgBGQi6Cc-yVKYO6CMyAlus4KsWVGCFs2Vaq_-aaLd2PxboCqPwiA7KsJGW55b0uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnPYADWyqIdDTzlkms1yy3d-SjkuDWLQAe16vPTUwuTwwFrX2desfnDSLRRUNZYivp2g4d6DjNkreIgJcka6LY-9V7OpEdTemm8sLMWzZK-WVRmvudzVt3dWSHUcJ_ADHtVfxtPC7M7B1YBpDM-i8pTcLwIFhJaj5aLnhmwE6wCL5amIMJJlT-KSq-wLtmg4eJ6ukUNtbhGmZoOVmR6nwWkcEYz6gkvTpNHmNjFUTg9pzcdQU89WwR6V52Zfs8ej-IGoqB8wpwnEd4ylW-Zf1ar5dDEmIMAeAF99UHVWUhoHyy-qqcL4Gxu92vyMSyB_I7W98LXr-Ma2Wq4270MfeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFXozLCM5nk_CMrybWWbZbSE80B6aggvU4XK_XndyV7ISiZaIbQ-xMQWe6wbvl-lzuWXLWNOMiplclnAFI__BD6W5d2y1Pcfq2zxitKM9uf156mRSy0DJT_C0rmY6_r6L3S-Gzu0SjNs1vvaHx_lpvAZYwnETPxvGK6-s4bQKQabDaF58ziJ4I3hxsmPRaH7r0ptVgipNlTAu6EsH4BOH4NXlfVN0fsNWkrQ1B3ir8tD4Igdoq_iW3tYwmqwBdn9KqsCGjsKKcydFpbXh5aQqjIOHEOvK_yK5EXCP5ecz7rWTlswDlOhO2jcOPQVKLSuqQfQuJQIIoeAWK-NkDvfrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMV7zd2ljgo3_hEprgvOjTfSW3FL0WHwE4y-O8X5mev9NwmS5QZ_I0Z-xdIPPuYz_ctvu2emiOHfxqxgFCzYZjCDZDPrAn2E8mR7M0Ldr2EmuEtOOeaGRcyw3XMEdEtdRwh4WmexP-cTkuarNZ9TkRKtCqbUatrjGizChGvzM0Si8rJFhi83DBagB0st8PB9tDCJBLddew4D2UDYKo8bHgwF2Yzz7Sw6M2_74kcuDRNxnR5oibBSmoCjxG7pX2Vq3MZ-hudpN8CQOmDJYZKMZPgPJaD_4IrTjxWtjQ7HOlHVu28V_mJ9VPL-oxNUFQ4vvwevxQXmFAAm0SAA83GC0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5qLEYc17_nd1UTLl_UWBE8_qmNE2PQ-3KibTp0wnCmXLMOzJtaWtQaoRUKIyyru3f571nSwskYj7Kx9-k8_VrFs0hrHD3OR4gU7YzNR_soGFQxnuPIEJ4gmHr8u7rFufpeLqQI2BtN1zkq10ZLylWL5TA9J65qaMkx2bwcnLy1XM4-78VgbU0iXhtwIKANd7Tlgkq3PizkPNBuI5a4ff5hpnZw8hcw9pwEy9vCPajW2i0gafJrdEOlkoi8rNl5oxZkYMJTZz6JOatvDMHT91dcqoUIPKGTwZAEjL01wbNUOFOe6kaHFvfYBmVb30-5vQM4Bb7nq_wppFFKZeSlIsA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=HQpUiAggKR8TvBqT9aiA5KEbNwnffram3bcA2g29vzFoEwp3i9QpwAv0xVtlJL8SfrnQl0kJjkXxhMUurnPwjBdNPFhPeIcK5GvAIFBPeJ3sP2qVJemPK5NiScy8VQzyYCkO5_D7xpsGrYWnCQrokIlyCQUUntUilLzAMtzZilsDuT-ACWjWSgN8F65N_YeXlGnSGoKWWwBoOMJWwm8tEwdVoGrB6nNEcrtNWbdsa6zl-IIQUPJVMBSSf36Ri6__jJwXTyasahJWIR6LrQ3QRtLIt-4mlj2wcg3W7cHTIvPPP-mjtb6HoAroVpfqXc4l4zWC0JlIICxAAJxTbWgF5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=HQpUiAggKR8TvBqT9aiA5KEbNwnffram3bcA2g29vzFoEwp3i9QpwAv0xVtlJL8SfrnQl0kJjkXxhMUurnPwjBdNPFhPeIcK5GvAIFBPeJ3sP2qVJemPK5NiScy8VQzyYCkO5_D7xpsGrYWnCQrokIlyCQUUntUilLzAMtzZilsDuT-ACWjWSgN8F65N_YeXlGnSGoKWWwBoOMJWwm8tEwdVoGrB6nNEcrtNWbdsa6zl-IIQUPJVMBSSf36Ri6__jJwXTyasahJWIR6LrQ3QRtLIt-4mlj2wcg3W7cHTIvPPP-mjtb6HoAroVpfqXc4l4zWC0JlIICxAAJxTbWgF5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1owZlwf73njiQC8l-2FuktL10kO9tYAmHWSKv2-9PjtOGlKLMkiJamgWgBesKYMSbVLZka9CCMzoB0xTCoDDINFtoreU-S0cYZtturZxavo61M3GygJV3d3-g4rcVJ79d-mqjDQQcyHQZs-tm4SXBC-nPC1IIsaWfa_uH3jJec0LXEgwnTTSWEgAFI5rqAQPl5h_yOuH57Vj7xiDN-Z3TaG-9SfZJPQL4hpxf6UCOADxnc_nD6wltV00xvx1g3gshputaBZiuVtgKuCYtn3fXGLIEd6YIoV1rf0QwlQmbPZCiiMxDMSAD0PAgHl9e7lck1jeAEs2_dlg7TvZ1zFFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puPjzMVFnQaF-dpdwUQuPFc_cpS7LWn0uZkARHi977kLiF_Lu2Cjh94-13Rt2HsYEFrlMh0i0zPOyRfRpi0cP8P4H3o8LsGRg0Xq95sXdgOU6xURACxtRVe4Byq15RYrWWmbyi_5Gw3wZksxHO4IojYxrTBcozPv_0tFEIIcIes2vqJ0PzcG2RCoad2gR5hwbzW4LcLI6LjQ74YMtA0Z7jKhyYkAiJVKYLgw4iLpnFzhaNt6qlJpMo1YlugoFCPF2ZaJVn7_IVTQuGnYinYKAtTIUitq8CPEQuq6vevC-0URT7eBFEuvanhyA-6j2tEXIcPisO5vJFgSU1_IMPmzRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6324" target="_blank">📅 16:56 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
