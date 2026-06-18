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
<img src="https://cdn4.telesco.pe/file/pn0vruaEyfIA68a2ZBP9wnGvQOM0epBM1Tzq9oEmCuH84wQY8E2ecqg4g0NddHtiSLW8H_Z_FxUtutkZCwziGAY7l5sJIen_pCyTL5y8ilVevi0pCQqdjV2e6C-xHETrx3I6zRG5-aYZqfV1ozSUvNoPIweG2Fn8Ax4zFc-dmAJv2HLsr006VPrCfT1wprVl3884yzle_f2qt5_y5KXCVAy5jBEVCeVyoAOGkBGpB2KJ0RTvEAYIiKa8rR_-qFBrRTmSKJXK_tXe0qSk_lAGpwBlW3gvpkzYOlW9n6gYoKst8pSY5SQ4tWSxkvC0zcOk6oAmeCPmqh-GwyMWjuofiw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.66K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 14:37:40</div>
<hr>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #100</div>
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
npm install -g @anthropic-ai/claude-code
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
<div class="tg-footer">👁️ 888 · <a href="https://t.me/archivetell/6436" target="_blank">📅 11:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 937 · <a href="https://t.me/archivetell/6435" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/archivetell/6434" target="_blank">📅 09:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">با سلام درود رفقا میخوام یه ربات open vpn بیارم
دنبال پنل درست حسابیشم
اگه کسی پنلی داشت که بشه حجم و کاربر و ایناشو مشخص کرد ممنون میشم داخل کامنت همین پیام یا پیوی بگه ممنونم ازتون
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/archivetell/6433" target="_blank">📅 04:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/6432" target="_blank">📅 22:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/6431" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6430" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6429">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTONbeFL16j2UpzbPgk5xz_cEHoWcGzA6PYiiYrk7ZPLlp0NG-Bu425NZa9m41c7BrPSvkjhXVMPjJYW80AW7pmUQf5mBN1_7XPkAbs-qt9YHgKkzzQkkPfIBjIerrbdQVHlMmNFWgtwfQCd1Hiahvu-BB7ms9mALR3_nDXxRLjvGsbFM_AOdrDPg5u1spuN38FlYxVOrLde57HfADTdNlwgGS3M_uekkgYdTnbdygL3QFGOPfvyQdr5U3QzTPx4Kip6RcR1ptO1rW4iJVBlT8pitUqA4XkNmBSa6-qNLOOORX_Kg645b84NrPmB1dLAsCXHzQWFxye1XHlwWI5LoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6429" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6428" target="_blank">📅 15:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/archivetell/6427" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6425" target="_blank">📅 13:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6423" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/archivetell/6419" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QP3DA36JOVPHclYGQIARYYL-_iSgoHwufRshZNt1Ettqww5GiGh-lpgF3l3z1MQIw1aneS5lR29CZHewbykzS_LQJ_LrXKDuQOY65TiDS-sLijlv67qzV-MoMhhNZtjJ3JAj93bLRUZY_Eek0h1GHMv1SlY8_wehXUVSTJ3V9wv3R2iADZafI_xQnf0wR39B3mZ-5RrF0V93Pxx6v50qOz425wLMMbp8MMho6cn-_of4EHy_zMWmC4Ofvt-LGwQTvlQhknAgmGAfZ8r0a59qM3heqoSSfn77DlvLPxTxyMhx5IY3XBGNheRvPUf1f2dWMMQzpxCwArbFacUezQaHoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MBSHiKYWrw7L2xCSlyPAc6dDTdQrpxSHW6YfsJf2SBXSQ3AV-E81xz9TZysYuRdjRBr0L3fUN_hFg2bYaoqwzjSR8jU0hXNwGAxWzsvPPbLyZU3A938soCq520DDUMJ8aOwvcji5DfVFdpY1nq3X5kGidVnwSoVEj8rtchnChRpDKsKIVAZcLmtzC3JKRcoKVDnTNZjqNFc8KVOB1rTzA1ndJrLlGqk7o-UgNesOYItWzNearVRq5Jr32BFUB58zcMUDrz3V1el7QZRkBj-bQpvCHjQ2jaGYraV-wLHfAoN57YWGX0rNJSC9bcwPTbFXBEmzw_H2D7pUorCeD8m7yg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/6416" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Heybaat.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6415" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">sadra.ovpn</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6415" target="_blank">📅 04:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6414" target="_blank">📅 04:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6413">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RWf_CxBtGnxnxyQkYUJ_DDtsu1QP1UHhu4fY7879qwPPTM1eOaZ6ArcLApICouYBYmv7TDjAVDOZpVTKAkciixvxGpGjpvkPfT0WOGx9o1l6O6FXcOZMEfCFu16nJ4BRJsV3QktX1Bxu8RnSz-a-ySUEtLuy8u6TjBsYwitYryzvC5q2JVDrr5PBQgPnHoMyovlWrydOlhmHfpiDVLw9HOCqosE9jbGS2TF-cC9HUpIN0mVywYs743VZi2RIFHWQicykhVUVcH_--y7w1WaE6zleUzwQSRKKGKHbf71UUL9BA3mEbVkRmK820OZZZ06cNRomsAWc-ARv1uoZgrp2HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kw_MOcvicp6DemQUDXPb7_CO_wET4vOM5S61_oDyEN41fg1CF3sCVE7_q9kCVSmllxvW8HPKgT6SqBWGrekDfXUUIuuLyuvsKJgQZTgBmOUjftJvqa91bb_z12rFtenTWYJkbrgn2SZaa7n7YH6eIabH1WVoXc4aHTc0WcVGMnqy4r6T4fiBla9-RTGXEZfFKlgxkLCF8_FMFYnQMTGBPLZCsO0I1avcvyQDfgzwmni-c0s9UeKUKn2oTKv3CMw9O0lb3mw6G4YDxvovQ2sr3tasaB8PAiKCb_7YzMHLz4DX41Nb1rDnosFzQ8pt2sVBhhLmWbdYSyqRyNsBF9ui6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CVVZBdMpCYpTlKeVs4KuXiY9HtknrOgoAB_-P_AQk04d1UU8J3BTaPM8aqswVZpAGqzuTdvymX_oZPI6F8k8q55ol81cGFrg_vigQ4ojDMbBedWfQ8lVwOeUEwH4nje8t94PGfAvVULGekbKRN9xxkdMPFiIYpNWYZvaTn8IurrooQTxTlh4F65uol___U_zBagf0TRJPXBjuKwY7T050n91B0JpSk08nZhmThkQ1K-qgDbFmW7Gm0BxeBVaMHh6uQbJ3iIrIQN1QWw-xnPowtKmD52tPsjUccAzAaICdCnZQLVO8iqoU4a-aW8ER-pmET5HGJZ0JkGBY1mJvAvVaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZWzCPlPUMvHkiJNs_9qKbXUISKxnTeosB3U1klBpq-VPJvPaX3-TJB6MYVRTVFBlpKJ2Ni9oTKogZqH2UB1ft8p9KMrAeQ-F10haL-ezKi89SSkmU_ViqgL9T2cWpX42yCdFp22yOQFNNrSwBG8h9DGUPXrsBqhb4CYk7B7alQovQeN1r-hheqxp5Vi6dA7yCrc-gEKNEum87VeZI1fVVkGGsOHa-X7K1uES2hf5CSG-pqtHb1tJAVa4rcofW7fKvswiA6bqCGpjw0HKoWEdEU_oUofDbAstw6v8DBCjxj42YIEI5KL4WgEZX1z8VIJSUb-lWkGD0G9T2NQFqWJ1Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت تصویر به‌علاوه کتابخانه عظیم پرامپت‌ها.
- طراحی‌ها، تصاویر، نقاشی‌ها و راهنمایی‌هایی را که توسط هوش مصنوعی و هنرمندان و طراحان برجسته جامعه ایجاد شده‌اند، مطالعه کنید.
http://Arthub.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e186940244.mp4?token=bZaK7ZQPjWhlYocsyJitlRCqxnLEn9V-YMAvHErWKfJgvFfVPf-kVypJVv1YcrAAlwAEz1UfDB-0mU9WHOQ7ESJTytawLdlj9aGSa3Lq-l74zoCv8k7SYmPd1nmgh1ryYo0yyLSRus5WdpxM5k4oXeSpzrMVyI17orAlwte0AhHXFFVdFV80Zw9uAezVKxusqQ_InaYZ3RjpdQiw9ChvUtM_34WHdUILLS2BCUWlpOAgekkdchR91oa5VFMbA0f1OnfmLePWS8ivQCwaIxE7BAzvZlSYgd5WJ8oad5hXkmrovsyxUgl17i_JXaHTfp4u5KP3nOIdk5o4NC6EfeI9hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e186940244.mp4?token=bZaK7ZQPjWhlYocsyJitlRCqxnLEn9V-YMAvHErWKfJgvFfVPf-kVypJVv1YcrAAlwAEz1UfDB-0mU9WHOQ7ESJTytawLdlj9aGSa3Lq-l74zoCv8k7SYmPd1nmgh1ryYo0yyLSRus5WdpxM5k4oXeSpzrMVyI17orAlwte0AhHXFFVdFV80Zw9uAezVKxusqQ_InaYZ3RjpdQiw9ChvUtM_34WHdUILLS2BCUWlpOAgekkdchR91oa5VFMbA0f1OnfmLePWS8ivQCwaIxE7BAzvZlSYgd5WJ8oad5hXkmrovsyxUgl17i_JXaHTfp4u5KP3nOIdk5o4NC6EfeI9hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoDa1mtl7-tp1FaUr7IU7wT-8uKaJWWsuhfT7vzI_JIVZKb5tGo2B7mRYSgfaHtOAMSoCW7KgufW9ZSRKc8RZE4zaIoaXTtoEkLb_Hepiw2aPpKUDS3Y389eaLOQa61xlfSiILr3tZT-QnRhujwUWHxD6MXol2wRg1UXBFsSpKedoqrXT2JBcVGpVqxbHChw8_-UKkFa_No3fvBDmDWhVaFDYZJ9HuFU6o7V5j-nlzPrXcutTFSNo8fcc2ZxWWJXiZjYlwCMZGZbKEFa1fjIvZTBNhDgEev5cpz90GGWpYNEgZfkhdU9x7lpcO3fRLvkQS7Y6M2NnBiPEmfpExN0YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087fb590da.mp4?token=a9ZQhBxaTdiuVIsFLSKMSJZOGpTBpMEMVFaV-PWbwG-eyXmsDUUQNTbXXrsFB95koMWzNeC4LWpOjb2T-G4tJH2cgoR_Z5NpV6_GSgVUI__3jjgsGDTyROHtxJtiY1a1xrs5uPrwiPYxlKigXRqc1lG7MN8Hsw1CdRukiUhrqF9qMvjeQheFKQoxucbmh-l7bPZ4e9FaWxS82ePq6HG2UBraz_goMf-7ukEjA0f5z9vkz58lO8U5IKZIFWxIhi4Xp4NA_fNxonPgtbDQhqBq0lm5jV6ZDWnH2M89V3CSKepcbarxz75wJ-4L6mJRBMeztK4VA16NwTqsbZ1S688odA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087fb590da.mp4?token=a9ZQhBxaTdiuVIsFLSKMSJZOGpTBpMEMVFaV-PWbwG-eyXmsDUUQNTbXXrsFB95koMWzNeC4LWpOjb2T-G4tJH2cgoR_Z5NpV6_GSgVUI__3jjgsGDTyROHtxJtiY1a1xrs5uPrwiPYxlKigXRqc1lG7MN8Hsw1CdRukiUhrqF9qMvjeQheFKQoxucbmh-l7bPZ4e9FaWxS82ePq6HG2UBraz_goMf-7ukEjA0f5z9vkz58lO8U5IKZIFWxIhi4Xp4NA_fNxonPgtbDQhqBq0lm5jV6ZDWnH2M89V3CSKepcbarxz75wJ-4L6mJRBMeztK4VA16NwTqsbZ1S688odA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csNqvgME_nEcm65vBMbNYACaHyQ2Ui7bt7HAGqsfEahX_NJMEoRfs9Co8ED73jaRHH7-BpzH7MilF_xsilQs9kBGrbuH_VmnpEk18_aAu5eQwXQzL_iN7LEEbZ_HnplHrORQ_b8PyGnZ5nuMy-JJ40REWeGoKohNVeEnDbg8TomIOnnYGSajHo-ASYz5luIhnUXQ6jW8Vf_FPYx9_5xcdS93eYwlLppzp-uuGwgGN6t-iPRP_3hKi6QMuNj4YhXpVy5mmvnpYuKtY7wn6-4z_dyMKTtD6R3zujm2G-ERlqpYawqsY_YmbbcZ-FLux-PFWAEVwviKmANwVGm0YDSUoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OzG257GhPF-fjK8jiPey40wB99Wx2nbxIbJIQkWOUbAraBo8WXBxeYbJKPY-1sCzBfGN1qcTN3fqMxvPlvMvmOySXkOfTJfE3fKM1EwrDqicZCqs9t0EXO_nCXpxuXBGHh3HCZpg40OTWcb5NPhG5PnUsA7lef6VrMPgzNc8wShlcBr_J15Myi2ZelAl4wdDD2J57bgU4QsYZDq9C6h-OaNjc6dPQkz6Knv0yYl_NQ7LUUNKF2kgTxFRrMPB5rnUDARdG3ShOcsSZXpBAJXPLPB3Mg05KmMWBbNJX7r7jR8x5wI-eJAvJfkgkxFw-OUt5Si0__vIzNuVJu2cDH8srQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت Ponytail هوش مصنوعی را از نوشتن کدهای طولانی نجات می‌دهد
☠
این مهارت عامل‌های هوش مصنوعی را از نوشتن کدهای طولانی و بی‌فایده نجات می‌دهد و به جای ۵۰۰ خط کد، عامل می‌تواند فقط ۵ خط بنویسد.
با Cursor، Windsurf، Cline، Copilot، Antigravity، OpenCode و Claude Code کار می‌کند.
https://github.com/DietrichGebert/ponytail
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLfct-jxS6yHQCkcr60Q3SngUZIckacqOhbivauoW_nFpU4r79ptGVEzvSEp7LAmb2ZAcHMq9tqxLW56oHIsSAICc2mEZqoQ2KG1uuq6soxOjhAEHcVlZlx-YR_aQJo0z6BViuP0zC02ZZdvxYkhdVmLoDeSNkSU-NH4LMydCkm2P7Yr7LZ_CK7wVVIc6rnLWWemlNpCtzL4pyE-vEmHddWUTQRy983Y9Br9iOxDieWoEeYwXMYM8oy58IHc_otL9yQXuIlkJO_aO8g5S-6IMNvTcRa1MmwC8wGqbBlKcE78qJd4mCDJ7gARRzVJvmw-vSiPEmMACY56banZOkWX7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
متوقف شد
❌
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dtzlj-URlJ8_NyGivFDIKBt9-Dd-5igcWL4vHG3VTgQuHCYOPCpObZgI0MBa740x_XZ38y0Ze1cF403VzLH-B7xxaurvCEc4hdG43BVTGWNTxCGGgi9kAbkKNqBbBs3QKCThxMz2XixjySBb0tNh989nGSmscaOamhf6-oscVQUcqs6m-Sly5z2qVwNHYD8JIsjXZ7VIYxwOqak78UT-mlSyTt9BUHM3qRb8tXyvjkTpGaI6tu5S7od1imGdqYRnWIgJCIprJPIQrgc5Pp0WB-11N2Ja94zAC3NWH59xdHGYYsUEAp4vKlta5RNxXHyptMnh8NXPdOsZYA4MTeZV8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TE3gkLC5rbftLbLJHerWXoYZCWhrnkl0QpzKXz6jDREShaCaNmgsIeO5TF-bKjLyVXWoeWmdQZL83y-HYoHFRggk-bk1rq65UoDzmHVqKfku90JN43L0JzcX03BO1Lsltl6G52UqixOjPYkIpPwiUq-G5nzkxWapQXJk4n-_s9j-klMWiIIj6_U83fHsdYBslPiq8zpw_CTHnYuuDCgBD7yTY83flsgm8j0hF4fPg2lytClzE14Zdxxw891LR3oNb5Rc4A5ZuwghMGoiRJT-W0c1Fo0lGHbmwcWkt41tB29Bqm7DleYgG5yqpD-UQrbcNmL4PmdoVXmNK9Lh_zsWJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq_RzOIta_g0PxAqSZdLaPrD32aDNQb80tng4ymJ-FDLTIcSvPWWDwaEj3-xHf_v0Oi9zuV9djVNKX8DZ5-TI7voZ6ZngshzVRRC2E9ImdbutpRM0V3A2Lm3sSHlMJjM3ulbEE7ZtzO2yyERkISWDvymxfDqEk208T0L_NoV1AsztPM7xHNQkcoigZop4SrjgY3tVt66lKuDHiiABD_6wk9NvBvjG-fztW0duIizxnU6OKDsmJZWlx-IdtfqYZ3ibo2TiZ_ayvBLdAe81WGT4H8c9WHMEG302tQVX098ynBS46j4QWkMqVVdZ3q-qXuy4BmyUNko5Qf9b_yZaZowtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkR4qdZ5j_wagIP3LPv_a1-_G4OBkNpJErEM6WjberznqfMAkgOSdagHE5CNDQq92-2n9BapYPkJLnoZCBK07G_GGOYRNirybGxO4IsmHhvlpjbGjrjQM31UcVkAokQr4S31wJ0sWZ-qEmf4Ga8l3trhn4rftWc_cyKU1rjKiHjl-24L3ESm84VHP_WcBdsvtJEgCfEhDlPsIvD5UMUi6QdkVd27P-TnnIimbsap6LgnHqtns3lcT4T9j8Wl1ZJRlzxkYFTT_b2Sv3oIjI2HCNBhu5TXs3Dv5u0dF0c-hehqe8XHBwmGh85hEhDApFDP1rNi9G6i15yVPUQbjBkNqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGg5lGhU3Tb6DqJbH44QEWD_T-QvIHzrgMIZlg-ZGMLmwM1bGvgUey_1sOTw9ET7GbxWCdLneFYGkR0raalthpH4-V7NXDd_RSa8aO1z2UDC6Yg-wuZd_d6RO99svmGkaCKXlChTYaZH9Ee4JHmbjn8spgZBR0Tzk3HK4_szyXC2l3fd7m8odicCrY99i_hpsqsQqTKQCKMBNKRm1QyBsZkHQzTfl6RQ9-Ji4agUsCMx4edefGl0iaTc8GRvvTOPqOX28w6AkPiggRRmtcKw-Jds2Dn6ZnqwxJsJe4rxq_orvuJElz34ZZRbUwREqQwcRJwee5ivyMeEOeqn6N6Nbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMyzUlzjsH3xBVChzTUlufERbpZu6RR5uXkVTSgoENLbYXMeoe6OJxRwHByGs8Arl0mfvdlyA5Eu1kmhAANSuo-Zh4s6TBCgZS9V6d2uRq_jmv3M8a2OqZLYlegNZjZ4ZpO9eM0lJ3ie9I0Suz5RFInTkAObca6-Juvt8EkCND4uQ-Q5I-x3YEKqDbN6gvYxYwrCo8sHPi6wKCHkr56JbOH9yDHkIvjrs7G-zhIulDtpXK0q0ZUx3BfBLgJgrm7ptD_YFX6N8vb4nl2l4Pa9oDrWXAddlguQTg32Iw_auQrhcfz0c7QhIWe4vNPW5gKToyCEZH5A0yzwP3IzrvE2qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaOMcAcMqsJGfmD15mNZe0sKVZvVE3Hou3hnasl5BgmhVGbihieHI-ZCcPagiPK1Z05I5LbaoLqIr_yVdIFD2RODJlDVm38XUQNOG8iK2ysg_JLXNVXTg9FoMyDXKb-4Q2av92OSYRVZPkm-f9dT5v1T3whzWONredWNJE2Mt03NG33uLlkCLSZrAQ13t838NprQMmkORDU7ZJyUz6xv7w1iXDLQMogDMIoISLiJR1x-lDYdJxrl8lLxNcDSM63B2KYFM_27okIz2yMETO37X5ZsK4QJ2Xzie50nPIIqJZy7uyIbdd2HDB099KsVGRGhPHU3HGLu5zQNg_wTWZcU0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fr9opVFQaYmtAE9sAzJmY1e5YSP1-UK76Zcs628roZDCrFAImoXTTWZFNziprv3XmMhVcdEG785TdTjJwGcwSe8IGj8565dOQXoIUpO4hw0T03MRiM0X2w-kln1CWJJnuPEYEyHkOXu1tB4le5UCNfUe-1GwMYfqfUKv0j6kLmL1JNcSJiPCW7iAPGQfihwysSyDougGTm7XcdywMNs6txyAHirwHsBBqvueyRIRf5Ju3a_Obtx-5atU3PWb7al3sBHEReFm7Q57kfuQ9CkMbYuRtt_RRCA8KJZjv057uWBEO2ekpWYAro9Rlvqe5WOcdRLCukvwxh4f1K7CONuUlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=bltBgpqt58e5sKs0RGx-JrwZnIyvRxRtAQPZ6ugFe4_nY42Y-2jGQgKKYre2JRLFhn2hSSK17wyAiLxBodfRy5yC7tFabQIjYjCaAz0Y6EPoX_1ZXpoE_1dtkXgH_fUL5XfErJEvTOTxqH5vXkHEQVAsoKH3NJRTvMlBuh9XEXC4wigPJbgbC-9LqzXtE-ZeJs9OpwES8buhk6TOyW4bmY0Z1c8MLoUJ2_FP6bhHu9TS114oyNWd08VYr33YCey-LYFuHXhZ8wn7_MD_GzmNKM-4IeccsMWpo3wc8LGt2zUbbYtxB59VGSLATLHSe48AQ1FC9JLSMSOPxdutby5nNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=bltBgpqt58e5sKs0RGx-JrwZnIyvRxRtAQPZ6ugFe4_nY42Y-2jGQgKKYre2JRLFhn2hSSK17wyAiLxBodfRy5yC7tFabQIjYjCaAz0Y6EPoX_1ZXpoE_1dtkXgH_fUL5XfErJEvTOTxqH5vXkHEQVAsoKH3NJRTvMlBuh9XEXC4wigPJbgbC-9LqzXtE-ZeJs9OpwES8buhk6TOyW4bmY0Z1c8MLoUJ2_FP6bhHu9TS114oyNWd08VYr33YCey-LYFuHXhZ8wn7_MD_GzmNKM-4IeccsMWpo3wc8LGt2zUbbYtxB59VGSLATLHSe48AQ1FC9JLSMSOPxdutby5nNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dP-CMHcSTNCn03skLy97EQd6AaKHvjjzBb5bwPu7q5HQtmhhbBxGdk76GxHbD8OKX6TGN8VStpG09qzcE45W4cebQB26YREovdRhGUJMUnv33-rlE5cFGL9wONUngAAZJ8rjh9aPx7zCE2baturP9Q88CNXe9QN8JQlnYj4FTYVAcWKdDtqINYFr1sYOB5Me5DCSUx_qzSHDzGmvg0WPlXOt7-M07CNePicxJH9Qbk09llPJ8D59XQluGU6V495gVAFN5TBaNZS00juNZB5PMb1jU3oNK299XyFTQzRGDxPMaHHDDGGO9H8ZV2I3kZUFSvt-ezFGLKDDuhmGNkVseg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpkWx_xtQUTEAp1jq9d5QNT32l3vnrjTW4lLZGFFjEZ08P21KepX6hn2QLdP-i9MVsZKUE6VmcrkL1pu3lBjH28Y-H252gIKkWSw7Ygll9OgNeCqA-tScAyrDeuEqZpbLU0vR3wjVxgXIJtrQWVRtyuqn71IaNxky2iH_rrAs2JLtkcMOQFRJ1Xo7dqACUvvfd4RroJCRzkiLJGiQHABOr5IUXLeZGYicgTqMGHNlhymx2MLHXG0D21dfATyuUbhXUP38uRHXRhTwXjk9tfowTP_v5w8eDOV9NFc3IfSPBTqtoaZEECXp0j9gu54ehcOCDaTQIl5TIKuGCDPFukqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=uq4L-nF6KzWfdMgopoI7zMdky_ryyrXaLKsdtv-96Pwd1X-VL71181ek8AmV0Vks5MJDQyVQyKxpTo-wjfE0yj6WuLqCwrd_a9VVaVbnI8xbAKfaQs7ithrNT804kNFCN34VoTYOOIKyyd8c5I-ApvYSIr2wiJ6hPUTMFGlX9If_yb9By5FMB5u881HKKUxOqwWmq4oLa_tcQ3-ug5FQ_SkywMTzxbxgpwlwTpRJk1Wln_a6Nbn8MxJphex9ZJKKNZswnGPOZN1ApFabf7onL9mX8BYp7PqDELUX02BlrmZ7LrClw1l4ACXwyLlOacz4KCKRNnaups2obm5anmKnkmNCLCmcS5lMb--ZylDfi1TfoQBlLDFJA9RXj2lTsV3LprpkEYFNN2fauAHGdM_J1xmWtnTRkvinc7E-_iY9h54nWSdbhRopP-C8JSBa9StVa6hl21e9N1d0n9rZFBwjE5xmcyiEN5pTyo-Q8U-StMDxN7znFKDHgZ15NWABlgs1hjOe8g3qy5rSjma7k0IiZwBpa8DKUk6C89jGigNL3czKBsUkEhU1VB6lnCQdaGf-qe9-p-xn1qNAZ9iPMiYk5mgmDE9Oofppi_JjVhMeKG9NBIJk9DmZRZ_DrSqzKdSuEmgDNh828ocFMsqaNGdIqgZERLnlzukKp8HRu1cq3M8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=uq4L-nF6KzWfdMgopoI7zMdky_ryyrXaLKsdtv-96Pwd1X-VL71181ek8AmV0Vks5MJDQyVQyKxpTo-wjfE0yj6WuLqCwrd_a9VVaVbnI8xbAKfaQs7ithrNT804kNFCN34VoTYOOIKyyd8c5I-ApvYSIr2wiJ6hPUTMFGlX9If_yb9By5FMB5u881HKKUxOqwWmq4oLa_tcQ3-ug5FQ_SkywMTzxbxgpwlwTpRJk1Wln_a6Nbn8MxJphex9ZJKKNZswnGPOZN1ApFabf7onL9mX8BYp7PqDELUX02BlrmZ7LrClw1l4ACXwyLlOacz4KCKRNnaups2obm5anmKnkmNCLCmcS5lMb--ZylDfi1TfoQBlLDFJA9RXj2lTsV3LprpkEYFNN2fauAHGdM_J1xmWtnTRkvinc7E-_iY9h54nWSdbhRopP-C8JSBa9StVa6hl21e9N1d0n9rZFBwjE5xmcyiEN5pTyo-Q8U-StMDxN7znFKDHgZ15NWABlgs1hjOe8g3qy5rSjma7k0IiZwBpa8DKUk6C89jGigNL3czKBsUkEhU1VB6lnCQdaGf-qe9-p-xn1qNAZ9iPMiYk5mgmDE9Oofppi_JjVhMeKG9NBIJk9DmZRZ_DrSqzKdSuEmgDNh828ocFMsqaNGdIqgZERLnlzukKp8HRu1cq3M8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=mjqwhZRMWsQZaVFCNQ7uFvdxpvv3Ea60EB9RQbTqvvEVtbhZRkzUKA39XOQRRKABSWNpzU_3OpTtrJhqhqkIa1zU93gmo3BOAbtMgfiip1eSNVWZdllpYCI0Jcr_PQavsTHCPwAcdmGetTVgFYEgKcLj97JRBGIiq8Ewmm43PTiEDVyatEDh3nogn4qVVKCLOZbXQKPXReFlbqDL-FvrMPu-SegJUOvLnfeMFrArOWSbXoBRL4DUYMBZs1Zlg7usAwX4kQpIFSMtYuLgYhA7nv7vWrNy6YehY0J8tkAaA1BDT7osX0d5E08t2CMB2lp99C-jqoVnbnWoTbR2hPnc7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=mjqwhZRMWsQZaVFCNQ7uFvdxpvv3Ea60EB9RQbTqvvEVtbhZRkzUKA39XOQRRKABSWNpzU_3OpTtrJhqhqkIa1zU93gmo3BOAbtMgfiip1eSNVWZdllpYCI0Jcr_PQavsTHCPwAcdmGetTVgFYEgKcLj97JRBGIiq8Ewmm43PTiEDVyatEDh3nogn4qVVKCLOZbXQKPXReFlbqDL-FvrMPu-SegJUOvLnfeMFrArOWSbXoBRL4DUYMBZs1Zlg7usAwX4kQpIFSMtYuLgYhA7nv7vWrNy6YehY0J8tkAaA1BDT7osX0d5E08t2CMB2lp99C-jqoVnbnWoTbR2hPnc7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6348" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzL1E4ikRWPOQ1PxSH_F-JY9FUPcw8q6jMMAUbVicF1yHpefDwyOYQImTisjIcemNrQeYaoXLjzVpU2AsdhmiA9cgpZ_ADzO78PZBRaA2QrtinFkJWxb3olq1bHSTsC9fCwo8smUtWPrzjP1izbF4tBjdWWOh9XeQY0cDQcUqhJ4JOlAr7XTMumxx9sLOKmD8eawj5clVxo850qG05xg1isHLypujiOhyW712uzwSjPXxyWa-YfZiGL0UzMQxTm43s8qMFGSw7wOVBv3ycnFygAQqmdaJVLd_RuEQyhHlwPg1F2X96O4sDVm01RMyM2c-G15jzJU7cd9MwzbJpt3kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکن ای پی کلودفلر 2
نتایج این اسکنر معتبر نیست یعنی ممکنه پیدا کنه بزارید تو کانفیگ بازم کار نکنه
بدون vpn وارد این سایت بشین اگه باز نمیشه واستون از یه
اسکنر دیگه
استفاده کنید
https://cdn-scanner-pro.vercel.app/
لیست رنج کلودفلر که پایین میدم اد کنید و اسکن کنید.
هر کدوم که سبز شد بزارید تو کانفیگای کلودفلر
با پورت 443 تست کنید</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/archivetell/6347" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dzch1OKbWk3iiQCKvPl8-TAm2xGB8KHOdiUeEuyyTcUyYRNmJ9YCz0a4EVitAWKv69quFZaxny3N7jLrjyMtOC8__J9xAM_mhpcv70DTDwg5tvU2WdQpgqsrkodE9yY1FGowVjSbA8_72L6L69xwgKq5tfcmDT52BgV5WPrE53F_IarTJaUTd5sJ9Wvo2TkSibXpHI_xh_eQIrpyzjAsEw8fTYxn0J16l5w-Iz3fFE7CWZ-XoMqH7JrDJKRSEunisSAkVlqWTlFE9FtUfg0XzppBxuKvci6YA3V-mehX7v_BDBUYNTpKurtStpVyRvrzGj3lfWU1mzsPr5k5xawtuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/scwyiO8vGG2jgM7RIJAgCcosjoF9Y_cgSdzs57-bcZuza3ZhV7bbt_iSne_LUd21-rF-mLlulLI4Xn9Cl0JpQGlG9m5YyMfhMBvYd9r-1tafvdFkMYXG6N6z8mVrqwcqES7mLkFM_NcHuuFRZp-SWpvgmokF4bETq1w8Sg3tW0IO9oPqGDDzOL6s8J7njz-tM_77-_ZMJU8tmqEJzOH2yQf3GLvhgrKuNlVIpBrLLJaRKn4dPe3NmTCaoGs2h-TpJD-_boMbhr8aUL-uA76Np2PdJ4TVf0gnNEAblyhFj1p9EKq6VtoVCHoCbSSfDAojgBq8ozR9XjcOxMyvjvEUWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bl8J_4RCgzugGmSUvShzOBfNSr_kGZ0VmsmmrX8Rrt4td1V8Ex7LOwq7iCAcqxLCwhiQyQzlDUuikLrAQ-iwZD998WwZHzhPVY-beA-OhDKwzrZFCSHck1WXJjVJisdfvEbTqkslFwdqYsscJwD1c_e-1flkVZbmx1P8ABuRHP2VFs9-17kOjSWn_7g2_baV6nnIyVtdOF59ofd-K1dJTBeMVZwZOdtCOHewI5Xciw7_W1LdcwXVPDyvIWCvOyENIU0vSU-LdKbI2Y791USUjsunN5PobdQdIgRB5Q3PjMVCfV5fSzEKGaszQv5yeYx1nMxCmNMptceTv3o2ZgpSAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ojg1NzmUnDFens6Yyl9fNGzRwraf8j9CJhxKSDJWo3El0wZ3lXkvztdDQxGWWmjmT3dA_hAqAyNYNdKY1rZ84Xi9R_v0Rd-VWFna4f7k-IS6m5XkROErayo9t7jpyQ-3X4Lc7b4ae6FKfVlhQUgkbjN-euOyhPqhSLH65QSzppqDt5L4sjLELyMJo2K3Mf6FACEEUiQCxDjo3mgC_u5N5RL1xwn9agBmVWxkpI9SQ7QRMGHTNggSlNL0AD3xH18_TJvvCejG2m4YpROwnW5Bh_lsHTRiS15rs5PvLvKp8eRih_PCPF4oYyc3A3pZMDvQ5PWyUab19Q8UbVyeBEFVbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inHm6n1iAIp1cHRRckBPLzJ7aFfv_IB-h5H5_zlwuHjsOzirL6ng4BDIv7ccBRk0tjxu32pneZq__ikYrOBtAY12ovXpvlypOdRnYSzGMzcaKVkFuHxPxW-k7ENrttLA62JisdAVKO5Cyxy0FlWlOQSjBYz1gbsf-0M1DXsDgW1lGhAcNZqbgo_gK7qjWz9enBRbtbMjE8lnyQdtI4Sjhhfxq7__QNwBdvw_nLu0zTq7XGrknM5yuEJtSJDJm9QwYiHB6e5w3ezEkivs6LMKYEoirvr6XOfKRNkeCQD8vC7trBZp0SOk0tMsXvvGo9k_M8iLnjrJbXELm0TrSKdu8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGq5vSUOwV7AgSgd2sgToxMO6IGczppPM1lKqbGoqILapV2_Pj_R3MWPzdaFs6mwAQGeqmVL1Ek7l52RSr9ITQmukLqnXAxKOK8eBj6pkPiDBDnyBiWbyDk8Ir8jK9BbTUSAKbiEZe-98pWUJJR-SsZinDfBguXS_Q27Vueao8_mHaYnjEn5OjQFNOafQArPqbVycR0Z9JqEW87xXGKMnIFKLeBunSaodAaShdHYsEOSi8wx7mLL9EbntelM-5C00ONQFtmm3wid7IVv0X31XeR1idrDTSpZzpLHpjWOqZy3Jfcf40VGmuEAVR8XrPXy0pTEQr8-JGMk70MxD6KFew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cw3vGQQo7UCiio98vb9ydhq9CRC0Kkw6ihJVPMLPNv4Erj5Ot_OGGRD9M4-ip35PGWcKobdk2JeUcV2kreCvxMxRxXTVSxYZY27t4n5A2ctDUhADS_skkVciVnM5TykoEFweEua5lytPkXknN9XAYcCwY_19Nmos01vMyiE-POMq56Z2liExNQpZwbI28W4Ob_aKrtOXtfhYBkwo0htXtLn-ruZC9NgicDLRLr6XfiPhjZDoz1Rfs8r24f2-ggnxxGGOHHQqgHARiY_PReRDzPT4e7O2OdVtLFdxPbXul-h6ukcHKYLSpc6cfZqcfQUFQzM_Xqfx18GIdxEfCrCHAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEpMI614zJry8Ov9AAQiI6pZrW2P9EVpZGpFu_OB8OywqmkgZvwgtFopeZX07fU0-FYQnOSqtrFfXSFeU3bSgy3dBST77g5RcDMse9fCOz4kgpIe_S5tB-7nrrMtB7_Dk5lprbafi_5qq5m8s_1MWBPJLYvVIll3EEhJva2_7AQBK_mIkKdJ-w4tNxI06bRFoinsEWoQ7yR7c6MKt6DYFiHaOz9pnLlFo9PtefIEQN7-7fRKk-jKRR4XyxTA8epOrEwTJYmE_SVhjUEwzQivPVlLlcCSTVUTNPDJxnT_7N7qJPnFevZtNgGRQWY38H-YWvys4NvqmMUAQFwvxvgMyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQF9eSpsrZoGOB-BSi55XlB2mzxo8-3E2A0HczRH1NTeCNSTGAdT7aIgOGFe71mZK9CiQ5yS0GIjOynzaE1CWRRQJ1FcJUfQdYspzQ6aXieHcmmn5fl0Csj03fNFXmGUGUh5VmxUwpXapXK7SsJrOjBO_8b6Y0fo4Nkcr128DYFNgB7UPUxJLubsXbpEW8-ykkWTDUW6hCuFP5Jlm8X02xP7LLsf9ko4D_g3Y9MoiE0UX4sCq_GaM7DVCUgkfvU4uOlOrgGDWAe8bA7of5_juAsz7PDZ048HGVTYuE8JocOl2_pKLdgKFcesVZZeV6bv92fyK_8o1SyG7MffCOdvOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVNuHkx4y_qrpyk4HcmFo_N7p5fVkNeBKApmzmNzVDjrhQSC9et685ZAt_CwTJKnf5UMj95LajKPTasEYbmQRDUxq-yCMEtaKV3VUQejZuJk1-tZ44sUk3yFnPFHfUywMUjgYMqQdYZB8Aj1-fKma9hpsdGJyKXei5afRA6HvANht959nBSnaNzmobMQHIGt_EW-w-rk_ITJ80OyvYnRbW8Qt0rdZ7IHppdsZSEqO9kxNA4wauyJKs34aIwEnO1uZ0Io6jyiwmx18dnCInUcJDur_nq3uqfCDN16oXxOSgPZnEQQK_TJpw3A_JEDzbx5dcgPZgA-O7FWOuV5Hie8IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8iVyBpyxyqv5icFoPHVRj5vZ4nWoLjl5nrzBAVfbxi4JwWIVYIKmpAafqDo0BDx2uMqs_W5561kiVMnfcQ9LVtGrZSo_DvNZMyfn9-Flm0BbTcAidSA-H8QDU4778aD7q9uIzSz2eX277PYBXP-QZuZcXdQNTk1-5u5sBMNaharJF1QR_Oc0bQy7zoZBpgNzVhelscjqV-JdATrvLi1lRWbSB4RpHv4vNt4b6m3AVEyRPnzCqGG_VS4oixnlH9GaoOCcvxDnAd2hl7nBWSCbZIQVqCmNBNqdf9ImNyuerGULPE4YdhQWn1ybN43R_Eg8-Qqe7Ka6XwCdb8IHkOsaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=Pk2XwTwhe71wg7yZutphurQJyVBLBrpyYKtntyluDOWlB6axfHptFEpoixwTabqFRb9sF8K5wjNTCBjUMYETpbNy0CF-zAzjEkiTud2DPyuV7SQBNsXELptQEq8Aam6SkwLA1fUfp6aUSWe0YDqgJXYLuKR61uxLwt3-KMOQSX0JaMN_UUEI4oOytTZnjB38r7g52KhFmGaP-sxaTY00R9oQ6FR4zN43SE9iVVJKlp6MTQ1X6j8W6xfKowx0IqLEdVaYT7yrYyJqov8873oFpvufAU0ZJGnX3oSdiuzzlKZyNr_BfvzCBnHZsR5oH3l546eplvNR348nlGZguEJOcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=Pk2XwTwhe71wg7yZutphurQJyVBLBrpyYKtntyluDOWlB6axfHptFEpoixwTabqFRb9sF8K5wjNTCBjUMYETpbNy0CF-zAzjEkiTud2DPyuV7SQBNsXELptQEq8Aam6SkwLA1fUfp6aUSWe0YDqgJXYLuKR61uxLwt3-KMOQSX0JaMN_UUEI4oOytTZnjB38r7g52KhFmGaP-sxaTY00R9oQ6FR4zN43SE9iVVJKlp6MTQ1X6j8W6xfKowx0IqLEdVaYT7yrYyJqov8873oFpvufAU0ZJGnX3oSdiuzzlKZyNr_BfvzCBnHZsR5oH3l546eplvNR348nlGZguEJOcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
- لینک سایت در مرحله اول  - لینک سایت در مرحله دوم  #GPT5 #AI #API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6335" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrhj6Z4V-nYu6eYmv09xtcYwtiktCAEaxYUbmElT4HJv6OvVad78M4xIpr9LE5U05GdvFkrfTujpIoSH2WM2h3PSgjszQX7TwcnSYP7_JwkISFH2ZcYB5nZn1b9zgWBhBC9WPfa7DNITWAe8HoFDp0SxyA2bhWzNWhwcH4G9fYw6jB0XE_Zk3hHGbvu22ylpWrSOzVIFEwfBLFjSWy7ZZ7jXCi-Feyxb6JCGE-MKMrR4iPZ_T7HsqsMaUszGC5WWhmQ-lBBwJPT106mvhE-7HdN9l7FRH7btGdOcmMNelFQPPDKoOym7W8hDYOS_dHBNb3dMLLMezR3_UCbQAmWMJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLXSSQ4lcqmibs1tmEYvfRt79I4oPE-GlnUP3PffZUdvUrq9CGibOUXf2rQPobKzauJj0VZzgOw2hKezo18DG0i-stOB9irXIR20VeUv1SlmQxJgqCqf8YaapwoNupn4qtYtDmxhbxWN1pJS8_AkJ5JbQ1tjTIHqX1VkolXnyW98PUxhQBQ-kyuBh8C3XHB6fn2AwJGz_i_YJnfla-BH4YgzVg2Ul6bFpatp5qpkK3T-0ycpCFoDYztOvqupKhf7_v1kdZBY3orVz5VjaKuwnmQsJOFZu0qUp8ZO8C3LFbQ5vxxj0BypXAP8uZEDpqIxhgFnSVC6WMjdCq03aP25jA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6333" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZcmMG3BlGikH7pld_rchzUfxMCHw1Ph7VDgmqtSN9HemqUF_NLazJ3VUQhGaGi88dqVrHdwyuTUcZaB4XCHTiaxCoMOVchZfSmAtJyjjzbSfB4cpIJK7N0cBbn1MkQHHueU36uT2v65wnJnCz-SILbM1SVQZJARrTF1yt1zzzINjQo4WN22uLMEJJAA6ejD3bKvzfYB519A2wAQywtpdV00fsJo2P9SdEJGxSB5CKMrNf6TEykexU6k8WGIrJSjG2U4amltOgoTkJ2WalbCF8jiIPu8MzFIlAMMMw3C5ynBeLsHzYVEgCXCY8HUa7E7CVWMcDeR3TBmQPCeGLnWLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iS4EKYL2dEArnMDA7A3KQmNyEeS05JWkCC1IZzCD6OBl8Oqv91uvuhLn-jM6Y3UJZG2zFtmun0w3L7ja95CEs9mo5U-LxcS1lQ9u7xB-4ktWALcLIXSrKTOIXAS2vNUjBLQryuVpYCGIr_RoGoYfJX2UVNHuauIUKvGUyYckmFBWVqAGBR_QxqfBr0KB5qNmoEu93QrXhUhy9B_7zo6EOziNd6CLCVFEytWwlsbUUlSkriHwtBdESY6Xpk1ppvN3FbBa8gzB1ENfyY12-5n4ZiDnlon2bVGgbE1EkdVAcxPxfGssotzvgVSMVwu4ACDSpGLkDuMA4PbLx-p31MWjnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=H9ROBrFODR-S1tkQyCltzQG2YhRaMlUZUWGKa-31dESg5-j7a23ilG6WYCVqr9CB_fC29pFKXRqDSVOlua_h1fzRrUj7cisvsIVn6EqwUyESd9xLBiuQXgvoYR4DVuz8KyWVnRVGULCiuCY8n3N4X18fHqbf9O0KjGisLULnagKah99biTAaPgHT9NUcyK7X1ALQk_OPnyf3JGjnIVTf9UEoVva8QXnmihgtP1zfkg_Lsbmhtb_UBN6oCoAZj99TKUgfRIuGxP0dWtq16yaxj-nF--rtwRHjzlyLVllajrhU-_LoVqn9ze84pvZiic3bwtA9qRkHTXOlUKC3XcFl2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=H9ROBrFODR-S1tkQyCltzQG2YhRaMlUZUWGKa-31dESg5-j7a23ilG6WYCVqr9CB_fC29pFKXRqDSVOlua_h1fzRrUj7cisvsIVn6EqwUyESd9xLBiuQXgvoYR4DVuz8KyWVnRVGULCiuCY8n3N4X18fHqbf9O0KjGisLULnagKah99biTAaPgHT9NUcyK7X1ALQk_OPnyf3JGjnIVTf9UEoVva8QXnmihgtP1zfkg_Lsbmhtb_UBN6oCoAZj99TKUgfRIuGxP0dWtq16yaxj-nF--rtwRHjzlyLVllajrhU-_LoVqn9ze84pvZiic3bwtA9qRkHTXOlUKC3XcFl2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6330" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rofO6yd0Kh_xwxFtkZvm-7KLAq-vJ_o-0_NeB5qSLw6zjTt2Q0UJzMTQ2IgCthi3zFHix_fv1LZ4Se2YQ9AuQK95B9vHVSdH9Cn9EcE3cIuOwQlfWAka-26wQKKZG3b7UZL30-C2ivSm4QHV8AH8GZ8YEYFxeyhS7JQbY5aQJzlbv3RiIS4-QMPU88cLjEsa0nEKsiLKTrj2sp5Xo6hRLF_ktvmn0pY_reOuZOkOA83yg5FsFKCV9l_Z63g7IjhzSLYW6nqFQCaOHT9mRFDxwGe3TutclPABS9U3yGn-FKpboxdIHN-uQDhVZsNW8FAek_l-l3cwbkPN0AbMmAD-nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpS2ze6OZufN3ICvC416SMaiVf9ca_G8KmI-9iOm-12mpucxGtCZjz9NLyC_73Eqk4JAsNof3VDrLnpL_TkQpM98hXDTjfyqv3lyQA1YDhGv5LOD0TXdL2AAGXum54UnX9n0Fa91XU_1AQ58VgUOtOJLafDEhvXLFNvMj-bxm5W6onR20Ma4UXKOR6AjnBCIfIPW3LcBc4ZquGg9O8C3P8Nf4W-kydgSsPhBd0guEPLdhfAVFXPiPqhGweoBRr_CHtGDkE8XONAIBQ6oXFQn8FKAC6c816Y5NndtneJnSGh3OL8kO8BFXP7UpqRMgGCSmQZztCedTGXMRu6qaukBKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4ZBJx5Q8ehSdCvx40ND1PNMx9WWYOWlPLlvdTnP3E_F-ozIhSHafay7LgIe21tURtkP96f5Gpf9OJmc3e8_cYPKJ120uZidAyZ2Bo0pX5K-9jJ143fpMEaPOOPGD5TkLgT8HusYYxdpl2bAtMLWjnvhJoryE5OMOi2LtvPwoOwqPanPRQ31OCh6iOnFiNDsouEHd-c8Vji0yc4IGO1j5KxNlMMmuVvfrmbtYwspsaST-7PQQPMzaWc4Tbe9xeno0kPzxnPOW2oXg9xA-PTGqQNRhmshwvMRDqCK679_WMKZaJ00EZf2IAE4_L9v56n-NhTIkObtNb3nBWl00Oku8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6324" target="_blank">📅 16:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr93NfhWFB8tXoT1DkqJQBtOK4RSCoQtwmc43f-3jL9jjU8yfS4p7zWP3YQixYxPSXKp5zEJmp7uJhPn3QtmziL8iHXy9CMnKvftVnHkWJYJ_5IIgO1ht0thDs4hUx0hBLZfF7VgnAh7Mks40rLnLH2ZhgHYfX48UXKUY2llCY8OILtBmXCiukGN9vSQkuRHGeJTv07Zbgo-jnFy7XeWH8S7kHHR-4VH4oOVVNK4JAiMd5imV6KN932pdxq2tX4niebn6MZkqkPArkgp6UXBWQKE5XxF7mGuDtO6QOfqp8-vM2p2AdPW-4fmRj2rnIRJOWLKQ9B5RJnaieYFxZ9iYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=iXoc__N-AzexM-bDLdzNqTmcJ2AEQcMdPvGBKFTOvIGDS4sP7sA7m7PJ5aQNkhVisn_W_mEBTcAN5NcQD5LZT5aCLoy-rsmHwoFN51k8iQ5stgKlQS6ZfRHAIx_CsQMdFk4qzTNJ-vFVOeTgXujeTc4aynSnMoLhhUjj5k4MlsalSd0yIVz7_fMQ5_DFD2RcheL6o12_uGRGbsLOiVAMcSj_00dcPyt2Md68e_PUa3CVByBuU6sE-gliNY00SFfa-POHI1VzxxLfh6CAYpG9OI9ujzUVzLjtLxSAN3MFpafP78QKRmtQRLsNpS3ef8DWy3CXX7WwYaaps6tvqwVHSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=iXoc__N-AzexM-bDLdzNqTmcJ2AEQcMdPvGBKFTOvIGDS4sP7sA7m7PJ5aQNkhVisn_W_mEBTcAN5NcQD5LZT5aCLoy-rsmHwoFN51k8iQ5stgKlQS6ZfRHAIx_CsQMdFk4qzTNJ-vFVOeTgXujeTc4aynSnMoLhhUjj5k4MlsalSd0yIVz7_fMQ5_DFD2RcheL6o12_uGRGbsLOiVAMcSj_00dcPyt2Md68e_PUa3CVByBuU6sE-gliNY00SFfa-POHI1VzxxLfh6CAYpG9OI9ujzUVzLjtLxSAN3MFpafP78QKRmtQRLsNpS3ef8DWy3CXX7WwYaaps6tvqwVHSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBC4JrGk0a2V42KliYy3jeMashk4qNpTxWJmtAFOiLtebuVbFMFV2n0vat1E9k1w6rYQMa1vLlwpsu16zEyzlw_ovROyS6Jk9zcykjDTOxv4hxmMn2id41vMAvK5X5Od9qrobp152ydw383LIYnlDuKAQ_pFmXkrZYe48lgXCoN3MU9wugcW7pIZB84SBHnMO5U-BC8oxNIR0i1oLvsVvO3w6k_iySglQVPF0w4q6YCV5to9wHeCYDoKSfzXgEDpjcsHUNDSzgpqF2dXg52EjA86BOwP0wkKmh5nyndOXGaR1nGuAz_U3O0_xChSyY7myVmB9-pKq6vOGiIrJuh-Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت موزیک رایگان
🎧
https://www.musiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6321" target="_blank">📅 14:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O3jXy9KF-vZB3yUh_i6QMWkASr8GCgHLGNf3uEhwN4cSxdJkBfRE4qaX7497NQUEQf60MVW2XqW4FqpJBSy_SrQ8B0EjgCDMU55iWXpPvBk_xN_Xx06rDQ6a80pqX843uGcj9ZuZM0gjLCUaFeIGLRku3Yl0Z2Un2Vc3v7t_vlzlaqo9GO8gUjqC8Dt9SFQsSCQUa_f3Y-deagvk5CK-oxzjBagS5o4hN69nFgufvSNMGNW-rfqky7g80mLerymN_fODcMyYk2p_WFeO4_W8vDqB2iYA590wxzu1_JQxYy_RVHjO6Qywt0MctKmdtJC8nIvQ2TIJ4qNJMk-ey_Jneg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0WjUeH-yN2x77XT_AkumogGBZs5y4sjTViTfRZcY-0ibECS45QgyDl_5mGko1jREzwlLiPwSAxadYmcu66NMa_JuUSZJCMDXo6hml0tnjSAjym42EzkpH3W7kCbcXkiVFJyyER2enW3gEXBfPQgpf18EmtGiioTodAenxLPpUgp5ZkATO5qHfM-aaXiGGOLeQE1KSSaPIsMIUjP5mMNzyiqZjKWE3tfBJkvjQu4nut9APo-ccg2Rvt0XA-JDLYeAhlN5ODAG_hPdupUjH_xkiN1AXpmyqoAAFVyFN1KMZqQje9cyYz5eEEDuFr1NyumwFOGWt_xe_rgeb0YPvF2Qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6319" target="_blank">📅 13:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد
شرکت Anthropic به‌تازگی مدل جدید
Claude Fable 5
را معرفی کرده؛ اولین مدل عمومی از کلاس جدید
Mythos
که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:
• عملکرد بسیار قوی در برنامه‌نویسی، تحلیل، تحقیق و اتوماسیون
• توانایی مدیریت پروژه‌های چندمرحله‌ای و بلندمدت
• پشتیبانی از وظایف پیچیده مهندسی نرم‌افزار و مهاجرت کدهای بزرگ
• استفاده از مکانیزم‌های ایمنی ویژه برای حوزه‌های حساس مانند امنیت سایبری و زیست‌شناسی
📌
طبق اعلام Anthropic، مدل Fable 5 تا 22 ژوئن در برخی پلن‌های اشتراکی در دسترس است و پس از آن استفاده از آن نیازمند اعتبار مصرفی خواهد بود.
این مدل به‌عنوان قدرتمندترین مدل عمومی Anthropic معرفی شده و تمرکز ویژه‌ای روی وظایف طولانی، استدلال پیشرفته و توسعه نرم‌افزار دارد.
با لینک زیر ۵ دلار اعتبار
🎁
نیاز به شماره مجازی
⚠️
(ایران رو چک نکردم ببینم داره یا نه
😂
)
🔗
https://v0.app/ref/94OS6T
🔵
@ArchiveTell
| Bachelor
⚡️
#Anthropic
#ClaudeFable5
#AI
#ArtificialIntelligence
#ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6318" target="_blank">📅 13:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها رو یک جا در اختیار کاربر میده و دیگه لازم نیست درگیر دردسرهای مختلف بشید
🛠️
✨
✅
این بات به شبکه‌های ورزشی محدود نمیشه و حدود ۶۰ هزار شبکه فیلم،سریال،اخبار  و.. را نیز پشتیبانی می‌کنه
آیدی بات:
@Bear_Tvbot
🐻
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6317" target="_blank">📅 12:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPCzDoeqqRQ7YiPLPtz4DpEPRnwj4Vw8vNBq2b3i-OgdvIBSU3mdyb5_lzg3dvH0-cSNJjAUEWZN7zIsmyuZG84rxcg1DinlE1Go_e4K2VqvVWCGN9phzQBa3j3sV8XoZ03p7CdoS5u1I5snz4IDonH_A9cFyiRSWuIUc71uL3TmiDxXcNhmi-kWdg040oWbzXuaLpqtJjnIhZT_aALNH6W58V6oPhHkR43OGvhUDVBJzdk_VPGM_KC9_oabwWP05KsutaVchq6utUmvjZR0W0C0U9JSTSQwglwMWxrJ9JbrjC6CLfcuy-65__kXy3qgDncdkFag0HFRSISLzHpw3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مدل‌های پیشرفته‌ AI به‌صورت رایگان در Notion!
•
🔹
Claude Opus 4.8
•
⚡
Gemini 3.1 Pro
•
🛠️
GPT‑5.5
•
📦
DeepSeek V4
🔗
لینک:
https://app.notion.com/
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6316" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e3-6_KzQtPfxmNOnmrIoV1Yw1cwbwjw-1NR9ICycys-MzEnCC0__faNPfp63NkCnzqhXeELvnV8rF7GuvAbH7LJFUNfc_hTXC4SM6Tw9B-sixpcga8WjdCaT2IkqFnGyTJuLX0ZBdZFjNeRiG7DcAhEkJVyIOhWwwU45hem4iH_8VbH3h53bmvjMp07nCqoy6UfKGFKVE2hjkU3ag_kyUBDYkTkNPcKeIkr_S_eCsNYh5xuKQEl5-14npDZF-YFRJ53bNf2FZZSKFNAggZ6aZjiiIU2qEfweBUQSaX5khy9D4i-iF4kASCS5aW0E6m18j1JUl2_OkZxi1aVPd1QS5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dtQk7n3vgPuqinE63jVK1g03vSX7mY1n3K1Als1o11EbmKL_qQB_mBgSev21EmMoRZfqGOZwwvC6S7zCSerz0_E5zpMumMC6-osv6-5aaevtyY72MqDF4HU6MTJZFSsdCy7TzTcfqqonPZp1sqrUuX2j9bu7TapKqtctrXcW5BVqvzcA5OSmaZO7fkw0fYGm0yXKxzGab-JmMr-M0nfYkVru2MAXV4xIv-XtfXS1shlmr7yOJ8YZrpkmnXfiNyRH8Ldlm93JXrrQTZMHjXsNKmFGA6Xp8qyw8GvY579Ja3Jhjgi3TFhGkXqsmCxlPDAm6aIQCicPtHkZurZ21vPW9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=f9c34-7Yz3QGWMswcrAo8TIYEA9WMSHQCQpn2o9mhBOe0mz0iFCuBcqLBnJeAGQTanJGadhtsaT1-FiLCXi42SI6mhY5mtp8VGIBvaafqTm-TzPMGThhrCrWGg55saOMcImcQa0C5_6ertPGi1RkOxk-7hHnnjEQ50b105GsMsHFCs01Rd1B8BKQYKuJjLwIa-S6vcjA_-dri1hcs1BeHmr_mwB82UunHzPjxE554eY6-Ob4pwJkPQlOxntwGisPMzgfMHlmCaKD--T4O00_pN1QI6jNWF_GRQFAEp4Mynsvx8NjuZ-OtoejHeIrCefectqh9Pt3Q-7RFvdmkGd6RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=f9c34-7Yz3QGWMswcrAo8TIYEA9WMSHQCQpn2o9mhBOe0mz0iFCuBcqLBnJeAGQTanJGadhtsaT1-FiLCXi42SI6mhY5mtp8VGIBvaafqTm-TzPMGThhrCrWGg55saOMcImcQa0C5_6ertPGi1RkOxk-7hHnnjEQ50b105GsMsHFCs01Rd1B8BKQYKuJjLwIa-S6vcjA_-dri1hcs1BeHmr_mwB82UunHzPjxE554eY6-Ob4pwJkPQlOxntwGisPMzgfMHlmCaKD--T4O00_pN1QI6jNWF_GRQFAEp4Mynsvx8NjuZ-OtoejHeIrCefectqh9Pt3Q-7RFvdmkGd6RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
تلگرام به‌روزرسانی شد: پشتیبانی کامل از Markdown و امکانات جدید
✨
قابلیت‌ها:
•
📱
دسترسی در تمام ساعت‌های اندرویدی
•
📝
قالب‌بندی نامحدود برای ربات‌ها (حداکثر ۳۲۷۶۸ کاراکتر)
•
🤖
ربات‌های هوش مصنوعی می‌توانند درخواست‌های عضویت در گروه‌ها را پردازش کنند
•
📊
امکان افزودن لینک به گزینه‌های نظرسنجی
•
🌐
باز کردن سریع لینک‌ها در مرورگر پیش‌فرض
#Telegram
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6311" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
