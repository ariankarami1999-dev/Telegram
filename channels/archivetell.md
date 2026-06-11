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
<img src="https://cdn4.telesco.pe/file/qONBb2GlmMX-iD2P1oV46P-1ZMm_88oS-RAaDECW3XL1Gzb8r7UZrbqTg87Tfj3BtAfLyYzmoS55WCdsXcVrUSAXBSAYEJ3-ARawWVXA88Z2n8ecYXWTzIT4vDCV_MRo8G7HgwDnaeyA5H55heQVG6kCYFBlGAoyadI2PuFCW0D3qWldycdJsqoIY0QzG1F64mAAy1Mz_xJuq2d2pxPNJ2Oi8sfpopJdZAgZmFTNiKOzz_xTLb8ZWMs7vfYUNFYJdxg_IPaqUlKua1mAzHZqFrKmnM8K3gAINK8viF5xq9P01VrnAex3lIG4JewPEIAqvPmjcjWDz1vJh7v2BGK21g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.6K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 19:08:14</div>
<hr>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🌐
Javid Mask | ابزار افزایش حریم خصوصی برای کاربران استارلینک
اگر از استارلینک استفاده می‌کنید و به دنبال راهی برای مدیریت بهتر ترافیک شبکه، فیلتر کردن دامنه‌های ناخواسته و افزایش حریم خصوصی هستید، پروژه متن‌باز
Javid Mask
می‌تواند گزینه جالبی باشد.
✨
امکانات اصلی:
• محافظت از حریم خصوصی و کاهش نشت اطلاعات شبکه
• فیلتر کردن دامنه‌ها و وب‌سایت‌های ناخواسته
• راه‌اندازی ساده روی سیستم‌های لینوکسی
• پشتیبانی از Raspberry Pi (از جمله Raspberry Pi 5)
• دریافت به‌روزرسانی‌های جدید از طریق پروژه متن‌باز
📋
پیش‌نیازها:
• سیستم‌عامل Linux
• حداقل ۵۱۲ مگابایت رم
• حدود ۱۰۰ مگابایت فضای خالی
⚙️
راه‌اندازی:
1️⃣
سورس پروژه را دریافت کنید:
git clone https://github.com/rowdy-ff/javid-mask.git
cd javid-mask
2️⃣
فایل‌ها را بررسی و دستورات نصب موجود در پروژه را اجرا کنید.
3️⃣
پس از نصب، تنظیمات موردنیاز را اعمال کرده و دامنه‌های دلخواه خود را برای فیلتر یا مدیریت شبکه مشخص کنید.
💡
این پروژه بیشتر برای کاربران استارلینک در ایران طراحی شده و هدف آن بهبود کنترل شبکه و افزایش حریم خصوصی است.
⭐
متن‌باز و رایگان
🔗
GitHub: rowdy-ff/javid-mask
#Starlink
#Privacy
#Linux
#OpenSource
#ArchiveTell
⚠️
قبل از پیاده سازی و نصب، لطفا کد منبع رو بررسی کنید.
چنل ما هیچ تعهدی در قبال این پروژه ندارد.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 674 · <a href="https://t.me/archivetell/6293" target="_blank">📅 17:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n49BAMwRbDsZJqAVtou4f0alkTvV3gThExWzPIVPjBqpezWXz8newJlaj8LQSjqUCYBz1H-dS7H2JtspLagY-2Gj1jvC8lcBGVuwh_PUKOBHNsbzyDSL3iKjl2m1FAeZhFs3boXxejoMR13w59mxn_n0fhX3vjqiauakiA4W_S0HzNhBTqvVyg3opTHLZzmvoMloWQS63cQgR3N74wD51--VwxXrF1eMV1wep1PmhNUd3iselrtN14P6OZ5TKVjDMbl-x3yB_N4D_ZcMTRn89mQuyollEXu7CY8DdgIQ_65ICGwqWkw9aEEwLXTkePepap2VXU8-NE7DAonSS4vmFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q2Nsi7i-V8kAQxI4SMOHqPKj_c054ghaxTj0siNBmn0xTjrSRulS2j4MQmQdktaTi2movZ4zVR_4jgCbFRybAqeB6cpyVtQhaEsf11qdQbODTV1BU-Kri1kHfPBLev8_fohHd79Ahtt3xaFzKgm1MV8-n5yuDEKraGxIZtECXNLhYteWSsSR2Ba-ZOaKgjqB-cF4EOCGESln3DO74X6OSzSW25_1B5R-cbgO948WnNatLD1p_CgjaFyrWRx-0AItYz1MNA37cHFDstp3aZfoxR3ueT_0iCN_x2k3C0kfENXR-aFr_YiDpagKS-4LVatyx8TpUSPQO6_nO4TJwbh-mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMyrUuh-LQZl0c2vkEzlr4lxRTxvo4r9oIVBANS70uDxR6CIB6bS2mi6wuK9QgIdBdJiBXdqcs77cDOpqpTL2iw1F1ttzMgdB-HXiwHVqK90hFV2t4zEa8eV8QjTBDqs3ApZKMcPBXlIuXhlb_pfR5nRfOOHREV33zRCz45B0EToDzitsyaC6TpE5cyDk4URZDAz10vV729pNcr0I2jld-Eb7erSRuO84aSYjsi7x88B1hcqqbXNA0rs97y_HxqJrlCbHG7UkBgmzKSv9oQSYnH6QIxuB4iZpo0_PdhRSv7b5xjrw0hwctYOu0X_gt6hcO-XeVcc3OWZm4FYLM9sGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
شیائومی MiMo Code: مدل جدید هوش مصنوعی برای برنامه‌نویسان، با هدف پیشی گرفتن از Claude Code.
✨
قابلیت‌ها:
•
🔹
کار با پروژه‌های میلیون‌ها خط کد بدون محدودیت
•
⚡
پردازش مخازن بزرگ بدون از دست دادن داده‌ها
•
🛠️
آموزش مجدد مدل در حین کار روی پروژه
•
📦
تمام این‌ها به‌صورت رایگان و متن‌باز
🔗
لینک:
https://mimo.xiaomi.com/coder
#OpenSource
#Xiaomi
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 771 · <a href="https://t.me/archivetell/6290" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54834411b8.mp4?token=D-MZPSYv6-HW9JLassoioJEKjuz6LUMgQfM8FM_Q5egACrQNw14HWl1NjZNF309Zftg0vDUsr9b9Aa4xsadiiTewHinxsKPM9Jp2IIifofvp4PJoCvbg125OiNPuOMv2i1vTxwl-KPQ4uQSRiMVJ87BAeDsNrlkvZPP7m55RJp8tKL_XWLSBU7Mc7QjmVF-iNI3xEwS2RNQPPAA2l5jkrkhMl46mAYtV6nxFg-fkEHV0g1VLA0M7UNg_cWqN53i8BkQGtZim9j5MKdC_uIre4tpdvE30tTw1AUeiQDlYadrfF-CHnxoWdg4hLLoa7eFhZwtFoXBU35Mz_vst9kZaZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54834411b8.mp4?token=D-MZPSYv6-HW9JLassoioJEKjuz6LUMgQfM8FM_Q5egACrQNw14HWl1NjZNF309Zftg0vDUsr9b9Aa4xsadiiTewHinxsKPM9Jp2IIifofvp4PJoCvbg125OiNPuOMv2i1vTxwl-KPQ4uQSRiMVJ87BAeDsNrlkvZPP7m55RJp8tKL_XWLSBU7Mc7QjmVF-iNI3xEwS2RNQPPAA2l5jkrkhMl46mAYtV6nxFg-fkEHV0g1VLA0M7UNg_cWqN53i8BkQGtZim9j5MKdC_uIre4tpdvE30tTw1AUeiQDlYadrfF-CHnxoWdg4hLLoa7eFhZwtFoXBU35Mz_vst9kZaZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
Every‑PDF
ویرایشگر رایگان PDF با پردازش محلی و بدون ارسال به فضای ابری
✨
قابلیت‌ها:
•
🔹
افزودن متن، امضا، تصویر و واترمارک
•
⚡
تقسیم، ادغام و تغییر ترتیب صفحات
•
🛠️
رمزگذاری
•
📦
کار با فایل‌های بزرگ به‌سرعت
🔗
لینک:
https://github.com/DDULDDUCK/every-pdf
#OpenSource
#PDF
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 895 · <a href="https://t.me/archivetell/6289" target="_blank">📅 16:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">📊
خلاصه یک سال فعالیت گیت‌هاب در چند ثانیه!
توسعه‌دهنده‌ای با نام
PankajKumardev
ابزار جالبی به نام
GitStory
ساخته که فعالیت‌های سالانه کاربران GitHub را به شکل کارت‌های آماری و قابل اشتراک‌گذاری نمایش می‌دهد.
🔹
کافی است نام کاربری GitHub را وارد کنید.
🔹
سرویس اطلاعات عمومی پروفایل را جمع‌آوری می‌کند.
🔹
سپس آمارهایی مثل تعداد کامیت‌ها، ریپازیتوری‌ها، مشارکت‌ها و فعالیت‌های سالانه را در قالب کارت‌های گرافیکی نمایش می‌دهد.
﻿
💡
اگر توسعه‌دهنده هستید یا می‌خواهید نگاهی سریع به عملکرد یک سال گذشته خود در گیت‌هاب داشته باشید، GitStory ابزار جالبی برای بررسی و اشتراک‌گذاری دستاوردهایتان است.
https://github.com/pankajkumardev/gitstory-2025
#GitHub
#Developers
#OpenSource
#Tools
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/archivetell/6288" target="_blank">📅 14:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚀
دریافت ۲۵۰ دلار کریدیت رایگان برای API
اگر دنبال دسترسی رایگان به مدل‌های زیر هستید، می‌تونید با Agent Router API Key اختصاصی بگیرید
👇
🖋️
Claude Opus 4.6
🧠
Deepseek v4 pro
⚡
GLM 5.1
📌
مراحل فعال‌سازی:
1⃣
وارد سایت
Agent Router
شوید
2️⃣
اگر سایت به زبان چینی بود، از بالا سمت راست
🔝
زبان را به English تغییر دهید
🇺🇸
3️⃣
روی Sign up بزنید و با حساب GitHub وارد شوید
🐱
4️⃣
وارد بخش API KEYS شوید
🔑
5️⃣
یک API Key جدید بسازید
➕
6️⃣
طبق راهنمای این سایت، از کلید ساخته‌شده برای اتصال API استفاده کنید
⚙️
💡
با این API می‌توانید:
🤖
ربات تلگرام بسازید
🌐
وب‌سایت طراحی کنید
⚡
ابزارهای اتوماسیون ایجاد کنید
💻
پروژه‌های هوش مصنوعی توسعه دهید
🔥
فرصت عالی برای تست مدل‌ها بدون پرداخت هزینه
💰
﻿
@Archivetell
✨</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/archivetell/6287" target="_blank">📅 12:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⚡️
سیم کارت رایگان همراه اول به خاطر جام جهانی (کد تخفیف + پست رایگان)
CUPSIM26
هر کد ملی تا ۳ تا میتونه بگیره (همه رو تو یک سبد بذارید)
لینک خرید
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6286" target="_blank">📅 11:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=jMgnJfIbe09kinAVPj1Xbfgfz0FllYksXyeAZf76WVbNC17_IXgWcAjSt4CfNljnAG1GSHhNkhFlMDnPInelLjzBogRFUOUbF65KPlzS8krSKtOpt8hEjBRwgVwl0kShW5FP2d1-anVGFsFIa7zcN5lyPao60TsxdeEluvq7Qpimi65_Fey2aJmV7byWJlew_XS2J3vHms7P7Bp0B1HcPx23NxP3MmjVFwefh2xHA94MNKImwS_Z7JSorf8G_46VE04mXS3v6v3y_TBQJFxZ4RomcDo0f1RQaCmoTuIFs6QmelqJT-a-cNMoM_cuy0z3NrehpRuL0tQsHiUsYNYMzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=jMgnJfIbe09kinAVPj1Xbfgfz0FllYksXyeAZf76WVbNC17_IXgWcAjSt4CfNljnAG1GSHhNkhFlMDnPInelLjzBogRFUOUbF65KPlzS8krSKtOpt8hEjBRwgVwl0kShW5FP2d1-anVGFsFIa7zcN5lyPao60TsxdeEluvq7Qpimi65_Fey2aJmV7byWJlew_XS2J3vHms7P7Bp0B1HcPx23NxP3MmjVFwefh2xHA94MNKImwS_Z7JSorf8G_46VE04mXS3v6v3y_TBQJFxZ4RomcDo0f1RQaCmoTuIFs6QmelqJT-a-cNMoM_cuy0z3NrehpRuL0tQsHiUsYNYMzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
OpenAI
تا ۵۰ هزار دلار اعتبار رایگان API میده!
🎉
•
🔹
۲۵۰ هزار توکن در روز برای GPT-5.5
•
⚡️
۲.۵ میلیون توکن در روز برای مینی‌مدل‌ها
•
🛠️
تا ۱۰ میلیون توکن در روز در سطوح ۳ تا ۵
•
💥
در عوض، داده‌های شما برای آموزش مدل‌ها استفاده خواهد شد.
📦
این ویژگی برای همه فعال نمی‌شود، اما ارزش امتحان کردن دارد — وارد OpenAI Platform شوید، Data Controls را باز کنید و به بخش Sharing بروید.
🔗
لینک:
https://platform.openai.com/
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/6285" target="_blank">📅 11:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3JZIRE1RLVNckL6I-n5IL6alp26IFY-954mTQtCRQVd54Bil_vddMkNUggHrSX3PL71GuWo66xgYagjovoPmgAh5tiSmbJmZkSJJFiD05CWBy8tpWoKeJbKUYhMD0kvd6M6Nvh3M9K-0CfNuxr6CMPgkf68w9XTnhUTrwEMgjOJTEe_edYCHbDMcBF8nqC_ItDoNyEcqsrYPquJ0a78Rvwlu8BWm2FP3_nvp0v6wTIPj9wVw3Z9F8jc22MtXDyfOrA4liKyweszCsss_OFV41NXsBwDQjteNxhjBJ1TI_smhgFEGHyf1iKsKh6fXfZr6ZWotfjyKYkCT913AwJabQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
BrowseryTools
مرورگر خود را به یک جعبه‌ابزار قدرتمند تبدیل کنید! 136 ابزار رایگان برای فایل، رسانه و هوش مصنوعی، همه در سمت کلاینت.
✨
قابلیت‌ها:
•
🔹
ویرایش تصویر و ویدئو بدون نصب
•
⚡
مبدل‌های فایل سریع و آنلاین
•
🛠️
ابزارهای توسعه‌دهنده با Next.js + TypeScript
•
📦
هوش مصنوعی محلی: رونویسی، ترجمه، حذف پس‌زمینه با Transformers.js
•
🌐
متن‌باز و قابل میزبانی مستقل
🔗
لینک:
https://github.com/aghyad97/browserytools
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/archivetell/6284" target="_blank">📅 10:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=rsnFdIbQ7EdUW4SriP8UxysERPj82vv61oCmIWG49QZiZLpzKYH9PphtVFC9gImmtZQ_gjg5YtNQrDid1Gno8e9SaN68DCjw-qt2u1IDRxDxRDD3CX_KwqIhw42iANtE5QyuQNZ7xGsfKw9npQaRwjXG9blSkeoUg_X3o23-SvY8xe4suXf2fohJ9vPZY0f25nuwWZDYclSG1x1Dp8qyxm26ckyrxf40eiDBGbRvrn88POlIr9jPoPB5jDMS7OUuZCCfqErO2AwAAtKLA42vgwqjpTJ8Jls-Qnpgk21Ib5pNLxEdwrTZtuiQg4BSm_Z6l39KMA6aUerd2h48NgKV0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=rsnFdIbQ7EdUW4SriP8UxysERPj82vv61oCmIWG49QZiZLpzKYH9PphtVFC9gImmtZQ_gjg5YtNQrDid1Gno8e9SaN68DCjw-qt2u1IDRxDxRDD3CX_KwqIhw42iANtE5QyuQNZ7xGsfKw9npQaRwjXG9blSkeoUg_X3o23-SvY8xe4suXf2fohJ9vPZY0f25nuwWZDYclSG1x1Dp8qyxm26ckyrxf40eiDBGbRvrn88POlIr9jPoPB5jDMS7OUuZCCfqErO2AwAAtKLA42vgwqjpTJ8Jls-Qnpgk21Ib5pNLxEdwrTZtuiQg4BSm_Z6l39KMA6aUerd2h48NgKV0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
افزونه ImageToPrompt تصویر شما را در چند ثانیه تحلیل می‌کنه و یک پرامپت آماده برای مدل‌های تولید تصویر می‌سازه.
✨
قابلیت‌ها:
•
🔹
تشخیص سبک، اشیاء، نورپردازی و ترکیب‌بندی
•
⚡
تولید پرامپت دقیق برای Stable Diffusion، DALL‑E و …
•
🛠️
بدون نیاز به ثبت‌نام یا حساب کاربری
🔗
لینک:
https://chromewebstore.google.com/detail/ImageToPrompt/pgabcjhpgdcgbflabemecpficpknnpfn
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/archivetell/6283" target="_blank">📅 09:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kt-H7owtya1EUVM7_UiAaPX2d2OqGoT4UhBE5bHw5A14XnuKlIdtORwtiZfGK8Vt2k-tQac_N1Wd_rtFAY2TyKM1UfDPc6mB7F5Tnu2X3Sv5zVYFpDalkc36WPujM5OIrCQIcdVhlLaLuQW8skDuFzdWlZoGFFU6LuxshLN8v-se8MdTl4cm3IbXVNaSb2I51wHJVbvshxZpk0La5ihWJvIRkrFoSmcIsG8pjP1UeosjYz3Xr0eO8aBuAbvJlQ3XMLiXMR8nVH8tLjK_Roc4jnWxFALvClVXyJ8bxVxbmvo5MCLqg0dVvFE4SVjB9VrL5UwAH3QnphBBwQCzqKgErw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتقال فایل سریع و پایدار بین دستگاه‌ها با قابلیت ادامه‌دادن پس از قطع
✨
قابلیت‌ها:
•
🔹
انتقال همزمان بین چند دستگاه
•
⚡
ادامه‌دادن خودکار پس از قطع ارتباط
•
🛠️
سازگاری با شبکه‌های پیچیده و متغیر
•
📦
انتقال تطبیقی برای بهینه‌سازی سرعت
🔗
https://shrimpsend.com
دانلود فایل مخصوص ویندوز ، مک و اندروید :
https://github.com/shrimpsend/shrimpsend/releases
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/archivetell/6282" target="_blank">📅 08:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zj1RpKtqk7sKEcEi0Y1GtATFdk2JNaoXaDHJkGN6-yj7ogeqR1UKa8pRxzxqgtsmhc_4V3NmmA48eCzpd3HIDyrOYZutbXFJg4-gMbbLMIgIPQUrpNcjPvHk8islQlqn6vAN9Hlw_-Hw3ehfY3GcmQ2ftRtTcPe9aP9BzdN3QZ3FrFIG4sJ6wUJc4ggKrMZ9NamUZWsOxqakiH-YFgbgoRmyqczvr1AueMG_FMUzKKRGXqzgrniUlzX_mrTWA3bx1JfRxU9JA1dyIn6VEQnavL9YUkFgtxNcnHqRi7xFFxQmOSjmIwYX44C_nJLsUtgof_ol_d4VD8vYVwO01RyXmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوتاه اما جالب
❕
به این صورت داخل duckduckgo میتونین qrcode بسازید
🔗
🎁
@Archivetell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6280" target="_blank">📅 03:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6279" target="_blank">📅 01:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚀
راه‌اندازی خودکار 3x-ui با WhiteDNS؛ از صفر تا تحویل کانفیگ در چند دقیقه  اگر حوصله نصب دستی 3x-ui، تنظیم کلادفلر، گرفتن SSL و ساخت کانفیگ‌های Reality و VLESS رو ندارید، WhiteDNS تقریباً همه این مراحل رو به‌صورت خودکار انجام می‌ده.
📋
پیش‌نیازها  قبل از…</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6278" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=M7joD3iLYAe3PIyECkM94VFXkC4YiqpSn57lp64O1tXz-Hu-ieTnCGvGh0FW6ZAGqFxxNKPN5jU3GY79CgNH9JnykNfhFG1Ch6kyuNTRfB5rp5505z5EC3peRacLNDdtGhWbijfxipI3Oh9K2E5iUaoqeHgNeg9QCAVWGRP73_BF6i_dYEOilJLH06oPGalqbXZ86C651u9_IuLDbKR-jCber0_jxMRmwEbe5E57rqurj0-nBWStpJ-CYOFvAi07Oxwl396GQ9XadLfu5S0BTEH0bkr8CAzQ-0vRMfwhIdHTHmtfrMsFWLYwmyR4yzJGd_yBQBvui1emGymHNnjfKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=M7joD3iLYAe3PIyECkM94VFXkC4YiqpSn57lp64O1tXz-Hu-ieTnCGvGh0FW6ZAGqFxxNKPN5jU3GY79CgNH9JnykNfhFG1Ch6kyuNTRfB5rp5505z5EC3peRacLNDdtGhWbijfxipI3Oh9K2E5iUaoqeHgNeg9QCAVWGRP73_BF6i_dYEOilJLH06oPGalqbXZ86C651u9_IuLDbKR-jCber0_jxMRmwEbe5E57rqurj0-nBWStpJ-CYOFvAi07Oxwl396GQ9XadLfu5S0BTEH0bkr8CAzQ-0vRMfwhIdHTHmtfrMsFWLYwmyR4yzJGd_yBQBvui1emGymHNnjfKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/archivetell/6277" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=vjbR-2-tOp4Evu3Dk2w0q0_961WyAAaikaR7_FADGd-L4REhmtNCWhynKFsDYO7Q6TTLpy0nAieg-av4xJI3JgCNj1MFE_uBO8-wq8MdSvHullpOSn55r-nR0HXqRW5JjiTOwo08K8xgQQI0kpyT_eu5591NMR8mYyJkZgW-znM__FaLZ7wJ_PqVyJvvcJdeDI5ifdnoxu1sUizZxAboylB_OS3_TT8SqH5-PO5Ss6_cugZGqjebeMFxDeQL_tNL8bbUSq8xi6CAMZcq0AFIaKhzAFsBeRgyRPf0Z21qmio4GTSh0fbiIZL3O-0PvAinJnyXQXMk_hQVnZ6c_8Kg_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=vjbR-2-tOp4Evu3Dk2w0q0_961WyAAaikaR7_FADGd-L4REhmtNCWhynKFsDYO7Q6TTLpy0nAieg-av4xJI3JgCNj1MFE_uBO8-wq8MdSvHullpOSn55r-nR0HXqRW5JjiTOwo08K8xgQQI0kpyT_eu5591NMR8mYyJkZgW-znM__FaLZ7wJ_PqVyJvvcJdeDI5ifdnoxu1sUizZxAboylB_OS3_TT8SqH5-PO5Ss6_cugZGqjebeMFxDeQL_tNL8bbUSq8xi6CAMZcq0AFIaKhzAFsBeRgyRPf0Z21qmio4GTSh0fbiIZL3O-0PvAinJnyXQXMk_hQVnZ6c_8Kg_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/6276" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=vH9mjPR-TF2xhBSOMOxTJNKSlXB-4CAklw-c18gQ0Dims--dy8-mD03ekDzbDBDacHMl-PdndFrY8Nj01Ts9odYPWMxhLBemxMHj202WUGNQNMhoKD8PTtVwR34rzzfVLilUgVTXGFZmEg0bZsRoyPAWm2kmWN5b9e0W18xjDl2_epw-lcjGUtw94UrhBXqjmhAXpqO7QxM44MivOJ9pDpBWi3NYq0vfsNSjtt-tNgR1NsX8PW0ajUdiEIZKDQLhzW2P9KfO3ym5rxMN4YfWpcRA6-nXLoGQdnIn4JLG5_iGznJdZZB8b5F2SE65OyS5SoPbT-jUZjDxlfQ2GYKJMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=vH9mjPR-TF2xhBSOMOxTJNKSlXB-4CAklw-c18gQ0Dims--dy8-mD03ekDzbDBDacHMl-PdndFrY8Nj01Ts9odYPWMxhLBemxMHj202WUGNQNMhoKD8PTtVwR34rzzfVLilUgVTXGFZmEg0bZsRoyPAWm2kmWN5b9e0W18xjDl2_epw-lcjGUtw94UrhBXqjmhAXpqO7QxM44MivOJ9pDpBWi3NYq0vfsNSjtt-tNgR1NsX8PW0ajUdiEIZKDQLhzW2P9KfO3ym5rxMN4YfWpcRA6-nXLoGQdnIn4JLG5_iGznJdZZB8b5F2SE65OyS5SoPbT-jUZjDxlfQ2GYKJMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد    @ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6275" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ادم خودشو باید برای هر سناریو اماده کنه و باید تو پیشگیری خوشبین باشه. چون شاید همون ی روش هم جواب داد</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6273" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">همین الاناس که ترامپ میاد میگه:
دقایقی قبل قرار بود دستور حمله رو صادر کنم، ولی آنها گفتند ما مذاکره میکنیم و من برای این حسن نیت آنها ۲ هفته حمله را به تعویق انداختم.
ممنون از توجه شما
دانلد جی ترامپ
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6272" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">برق قطع بشه با کبوتر میخوای پیام بزاری تو تلگرام؟ 🫪</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6271" target="_blank">📅 00:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6270" target="_blank">📅 00:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6269" target="_blank">📅 00:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6268" target="_blank">📅 00:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📝
جنجال جدید در دنیای آفیس‌های متن‌باز
پروژه
Euro-Office
نسخه 1.0 خودش رو به‌عنوان یک جایگزین اروپایی و متن‌باز برای Microsoft Office منتشر کرده، اما این ادعا با واکنش تند تیم
LibreOffice
روبه‌رو شده است
😬
🔹
بنیاد LibreOffice می‌گوید Euro-Office خودش را «اولین مجموعه آفیس متن‌باز اروپایی» معرفی کرده، در حالی که LibreOffice سال‌هاست چنین جایگاهی دارد.
🔹
همچنین توسعه‌دهندگان LibreOffice معتقدند تمرکز Euro-Office روی سازگاری کامل با فرمت‌های مایکروسافت، عملاً آن را به یک «هم‌پیمان غیرمستقیم مایکروسافت» تبدیل کرده است.
⚡️
به نظر می‌رسد رقابت بین پروژه‌های متن‌باز برای جذب کاربران و سازمان‌های اروپایی وارد مرحله جدیدی شده است.
#OpenSource
#LibreOffice
#MicrosoftOffice
#EuroOffice
🐧
📄
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6267" target="_blank">📅 21:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvgmJp61mDFyiklTWVZMGE9ntcQ0Zlos6WZtw4m9TMw9Sc5gmxz6xSgNxz3GPx4A3kvdtmvqDdBQj7e2DlzmkbJp3Ec6uMOJX4-7ZkgVyCwZtr-FMxF2yiR7eV_KQMzHuTsVgjaYsFeyhts0vuiN1XV-p6z5rfucD33SjtJ7yKvuxu9EysnjcGf42ulEN0mOrQ6hwbhMS5DkD9wc2nCLk79Vc6xZ2GnoDN2hzxmVDq3KlSsjVaxOMDZv8Bn1UU2tmZ5UcipQGsKZvzmDveAUdfheb6txRShqhZHEIHSDkrs6Y81MR7mO8rpOP0qMO8nli3Jw97pheuSya_lbY_RKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ZOOOP: همه ابزارهای خلاقیت هوش مصنوعی در یک پلتفرم!
🎨
🤖
✨
قابلیت‌ها:
•
🔹
تولید تصویر، ویدئو و صدا با یک کلیک
•
⚡
کلون حرکتی برای انیمیشن‌های دقیق
•
🛠️
قالب‌ها و مدل‌های محبوب پیش‌ساخته
•
📦
یکپارچه‌سازی ساده و سریع
🔗
لینک:
https://zooop.ai
#OpenSource
#AI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6266" target="_blank">📅 20:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WM68W7YxhY5inPBKQj5OdRe9edFqKbBd5B1pbjVhaAAuNx1E4flM9DRU0-VslcZLoCkSE85aG2xYF06VvR_xa5Cw2eXuY_mIByVLu9O_GtYCD0Ts-RaZrpStBTqqFiLoYBeKDZjIYlblR1kR0s9IGYP3voSr9LhVGKzh4tKTjGbaH9Xc8j8ic9PTGZKmSKQdiDm7HfEaSHIf8rnOzZk5kDDmmC3CnOIyeM8qT4xUdsUNitSkbUIamXZKaH4I7fX7nI1yH8Us3yP5XX89Tn-KBtyddhAljFBRcjG7OXghzx_y__f422r9O_CBHdeJOcGSl3ql2FAExa7MCcEt2NPCLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕵🏻‍♂️
با این ابزار می‌تونید فقط با وارد کردن یک نام کاربری، حضور احتمالی اون رو در سایت‌ها و پلتفرم‌های مختلف بررسی کنید.
✨
قابلیت‌ها:
• جست‌وجوی خودکار در صدها سایت
• بررسی شبکه‌های اجتماعی، انجمن‌ها، پلتفرم‌های بازی و سرویس‌های دیگر
• نمایش تطابق‌های پیدا شده در یک فهرست
• اجرا مستقیم داخل مرورگر، بدون نصب برنامه
• امکانات پایه رایگان
🔗
لینک:
https://whatsmynameapp.net/
#AI
#OSINT
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6265" target="_blank">📅 19:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6263">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581e875845.mp4?token=gaI4CKTEVHfOQq6YRnwTkG3gIK_A5pfF3yPlypBC7pwkqccf9Yg2nJmngdtnv8M9X1PadfCqpMmHS_aTuxVdEor3f_aT0chtETKlL04jWmfbe9v__zRjKTkviztjPJmJAL_Q9GF72p2qmhHoD1IVsj79LKK5_iwZhRmcrkCV2QxpYAfS7gGOg6NEGcm736uRIY8FPQYry3WZxLO2tI6apwcrQNximgXzXe6HSOG7qHHr3Fg8E8R-FCzSeyhEVl2qTXICd8R5GLJ1Za8i8dWAeMRrk-gzdq520CGSlBXuipXGFJK8Bm4a6Kol2MriiOfblDFnS9OZlfca_siEueBOGYolO4kjXzQRpp1PGgiIzf14wNV4H6sMEJV7sBr4IXQtsW77iK5v_NVfJCyDi2K_U9TEStjJEE1zrQAOuzPCsfr4wP6Cqq3dOjza8FdJaUnbo2GsM5XwNQEPD_si0y7WoIYjnzjF8OI8ViNaznjfIUiJDvAl8YxcblOeacUnKV8PIr_oAiqUKIXAgzYdEOfytV0TeYasxs0QnoHZmRKO9cIsAqK9oKriY0UBumANJJRNgb4IlK9BqwCXcb6santHsXj7yh3Gm8B4yodkiVO9Y97iptZ7YmadRboPCgMEjD_EGoy1uKVIMnOFC0rcGJ1xTNs560UFwK2QH-uHevBSdz0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581e875845.mp4?token=gaI4CKTEVHfOQq6YRnwTkG3gIK_A5pfF3yPlypBC7pwkqccf9Yg2nJmngdtnv8M9X1PadfCqpMmHS_aTuxVdEor3f_aT0chtETKlL04jWmfbe9v__zRjKTkviztjPJmJAL_Q9GF72p2qmhHoD1IVsj79LKK5_iwZhRmcrkCV2QxpYAfS7gGOg6NEGcm736uRIY8FPQYry3WZxLO2tI6apwcrQNximgXzXe6HSOG7qHHr3Fg8E8R-FCzSeyhEVl2qTXICd8R5GLJ1Za8i8dWAeMRrk-gzdq520CGSlBXuipXGFJK8Bm4a6Kol2MriiOfblDFnS9OZlfca_siEueBOGYolO4kjXzQRpp1PGgiIzf14wNV4H6sMEJV7sBr4IXQtsW77iK5v_NVfJCyDi2K_U9TEStjJEE1zrQAOuzPCsfr4wP6Cqq3dOjza8FdJaUnbo2GsM5XwNQEPD_si0y7WoIYjnzjF8OI8ViNaznjfIUiJDvAl8YxcblOeacUnKV8PIr_oAiqUKIXAgzYdEOfytV0TeYasxs0QnoHZmRKO9cIsAqK9oKriY0UBumANJJRNgb4IlK9BqwCXcb6santHsXj7yh3Gm8B4yodkiVO9Y97iptZ7YmadRboPCgMEjD_EGoy1uKVIMnOFC0rcGJ1xTNs560UFwK2QH-uHevBSdz0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
تست رایگان Battlefield 6 در استیم شروع شد؛ تا ۱۵ ژوئن می‌توانید این شوتر را بدون پرداخت هزینه تجربه کنید.
✨
قابلیت‌ها:
•
🔹
دسترسی رایگان محدود تا ۱۵ ژوئن
•
⚡
شامل ۵ حالت بازی مختلف
•
🛠️
تجربه ۴ نقشه چندنفره
•
🗺️
بازگشت نقشه‌های کلاسیک مثل بازار قاهره از BF3 و جاده گولماد از BF4
🔗
لینک:
https://store.steampowered.com/app/3028330/Battlefield_REDSEC/
#Battlefield
#Gaming
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6263" target="_blank">📅 18:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سیستم جدیدی به
ربات
افزوده شد.
✨
از این پس، در بخش
سرویس‌های هوشمند >> آخرین اخبار
، امکان دریافت اخبار روز ایران و جهان فراهم شده است
📰
🌍
هر دو ساعت اخبار بروزرسانی خواهد شد
✅</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6262" target="_blank">📅 18:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🦀
Asterinas 0.18 منتشر شد
پروژه Asterinas یکی از جاه‌طلبانه‌ترین پروژه‌های متن‌باز دنیای سیستم‌عامل‌هاست؛ یک جایگزین مدرن برای لینوکس که تقریباً به‌طور کامل با Rust نوشته شده و روی امنیت حافظه، کارایی بالا و سازگاری با اکوسیستم لینوکس تمرکز دارد.
در نسخه 0.18 تمرکز ویژه‌ای روی اجرای Asterinas در محیط‌های کانتینری و مجازی‌سازی بوده و قابلیت‌هایی مانند Namespaces، cgroups و بهبودهای مختلف VirtIO به آن اضافه شده‌اند.
از دیگر تغییرات مهم:
🔹
درایور جدید NVMe
🔹
بازنویسی درایور فایل‌سیستم EXT2
🔹
پشتیبانی بهتر از نرم‌افزارهای لینوکسی
🔹
اجرای برنامه‌هایی مانند Firefox، QEMU و Codex
اگرچه Asterinas هنوز فاصله زیادی تا جایگزینی کامل لینوکس دارد، اما یکی از جدی‌ترین تلاش‌ها برای ساخت یک سیستم‌عامل مدرن، امن و سازگار با لینوکس بر پایه Rust محسوب می‌شود.
#Linux
#Rust
#OpenSource
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6261" target="_blank">📅 17:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کانفیگ ناب
🔥
trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6260" target="_blank">📅 16:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGyUI9tC7_1-b7YU0Ay5z17dvmAAUyYzFRZmDM7xiktkCLEoa7AoLPBcNziXufy33Ph_ZN14SPhxydIdQBxSud-GiStzJBwvmsEBaWzo1AH8VgWC8oOkeSLicl8YZWFwYStZxOS-48Um8KWqqiqdkfBTFYxS4Tlaii05QHJzKJBesHRZEFLkaTmeGO0FAkwIUPOM7s66sm-2vYH7P55tgK6xqjPqDATSC3gWnI1VcXjm8kfd2YpCS4DxUWy2vb_cUHXjIMk8vp4Cqik7s1cEgk-tcPEX1ZUNxS7v879jApGQFl9G8MkfmyVjiYwptAfmyzYhQDXcQaRYvyi77wicRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
یک ویرایشگر ویدیوی رایگان که مستقیم داخل مرورگر اجرا می‌شود و فایل‌هایتان را روی کامپیوتر خودتان پردازش می‌کند؛ بدون آپلود در فضای ابری.
✨
قابلیت‌ها:
•
🔹
ویرایش چندمسیره ویدیو
•
📝
انیمیشن متن برای ساخت محتوای حرفه‌ای
•
🎧
افکت‌های صوتی کاربردی
•
🎨
تصحیح رنگ و بهبود تصویر
•
📦
خروجی با کیفیت 4K
•
🌐
اجرا در Chrome و Edge بدون نصب نرم‌افزار سنگین
🔗
لینک:
https://github.com/Augani/openreel-video
#VideoEditing
#Tools
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6259" target="_blank">📅 16:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=No7XlFRkOOX8JsSTps5YrEcmLbylGoGUQguA5HTvpjoh_iYr0Ju2esyvXlJTI96c4aO_yy76VKBRUug-qTCEDQjqn9WVePFoces-VHLg9K5KXZAimDiir4pzQQWl88kD2pjdMRZC_tX1dEnzYRexYHLTPT75M3gY2nn09QNixRzrcSFP2ObkbaH9PDTf4x8Sk8F1mWxIATi2u5QatKBsqCqxH57zI0uRq9yDHZcGLG0LKv5aCsNn3yvj1TK1ZXhpSzW-qgxhM9eM3ArRDx0mUuEaprLCptqZOKAo_K5-GCBAZjE2Aj0HNlPfhh1BKEANFwjATk2Q7WFPweeijaM4aVnGNX03crf0_VEVEOoDyIUZszScR9tAS1KcpfEQv31YyOM8MDp1cXu3fvEUN9FaZco7L33_1Q88OWg42_KkiSFb8GMyPCOegZeoUPPLWUcHais179wddxT9xZvx5Bz4fsdYzLaTZG63cE-JE4OSUH_eF3HEU6xyJn-EPM0aYQ6DTZudwR-x7o9-Jei92MX6_pu0tTlXMquUS1BhhnUXvreDOfxobZYypfFy79sHQ-yQLjOQbiWOR-MoUFDjxxzsIUF61rP9thw2RSQMcFnNJuWmEj5ojfpofuiDhmZOQYPt3tgoTVm0OjyfShcv_THgMkDfx8jK10bZujwDtEKk4Tk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=No7XlFRkOOX8JsSTps5YrEcmLbylGoGUQguA5HTvpjoh_iYr0Ju2esyvXlJTI96c4aO_yy76VKBRUug-qTCEDQjqn9WVePFoces-VHLg9K5KXZAimDiir4pzQQWl88kD2pjdMRZC_tX1dEnzYRexYHLTPT75M3gY2nn09QNixRzrcSFP2ObkbaH9PDTf4x8Sk8F1mWxIATi2u5QatKBsqCqxH57zI0uRq9yDHZcGLG0LKv5aCsNn3yvj1TK1ZXhpSzW-qgxhM9eM3ArRDx0mUuEaprLCptqZOKAo_K5-GCBAZjE2Aj0HNlPfhh1BKEANFwjATk2Q7WFPweeijaM4aVnGNX03crf0_VEVEOoDyIUZszScR9tAS1KcpfEQv31YyOM8MDp1cXu3fvEUN9FaZco7L33_1Q88OWg42_KkiSFb8GMyPCOegZeoUPPLWUcHais179wddxT9xZvx5Bz4fsdYzLaTZG63cE-JE4OSUH_eF3HEU6xyJn-EPM0aYQ6DTZudwR-x7o9-Jei92MX6_pu0tTlXMquUS1BhhnUXvreDOfxobZYypfFy79sHQ-yQLjOQbiWOR-MoUFDjxxzsIUF61rP9thw2RSQMcFnNJuWmEj5ojfpofuiDhmZOQYPt3tgoTVm0OjyfShcv_THgMkDfx8jK10bZujwDtEKk4Tk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
نسخه ۳.۲ مدل Ray از Luma منتشر شد؛ اما طبق تست‌های اولیه، هنوز با رقبایی مثل Seedance فاصله قابل‌توجهی دارد.
✨
نکات مهم:
•
🔹
پشتیبانی احتمالی از خروجی HDR با فرمت EXR 16-bit
•
⚡
تولید ویدیو تا ۱۰ ثانیه
•
🛠️
ساخت ویدیو بدون صدا
•
📦
ضعف در بافت‌ها، انسجام تصویر، دینامیک حرکت و درک پرامپت
🔗
لینک:
https://lumalabs.ai/ray3-2
#AI
#VideoGeneration
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/archivetell/6258" target="_blank">📅 15:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXOD0caqzz9yqnfaCrxZAv3McqOZTvoUR79h7W58AaRGCEDfzYqt5-7EowzAJafHjx2gLk0_3OTK5ptmAMPpPgQ59cOrEZZYdrJhPgUGhzJRVhPuF4PiZK5kCdLZvjrWsWQJHAY9VqWGH3DCHXEdnWuifR42orOrKRxDH5tuB_JF05-x6JwU5O7qEuSFJPNYMlNeDIk1OrNIVzPgn6jItGhWcTj-Xwsmm2kbQzRxLmVlXeX3K29ORAkiZLQUA2D8bxMiquiDv2IU1tF3_y-x9df4SuxnYhd_Jj3FIRtlJSD_lobgNrYDAqFf-ECVxs5A1kGMYe5kF9kk0B4OsVBdvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vj12_XM95hiu3fDGaQbOygzyFTWEZ1D6vFWqVUXKBJl5rtMs4WY6MGu5IB-zBPsFOloh3yvAocgKqqZ6rBK0kB_oBcNNFsg08apijXZTlYnfi2gqTZr00BGThLDtrlZjw2fW8bZ8V4zl9NG6Fhuto8ZPrpZIQwjMjUFow8r1mu_B_LGNKtQ6nfyj1qxB-jIg7KNL0oMxkzLAZVYt27yfyRXLx39h_vJry9cks93apTc1zr0uxovgB8FOdxxM8uaddSIx95t9D6togg0YWxS-kqMqD8Yy_Bmnz-K6V2xuZIiNhMZ9zKP_pXS5LKbBgGBCizKk6xjJ4VZTwJ_vnmsP9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
CodeWhale
یک عامل ترمینال رایگان و متن‌باز برای کدنویسی با DeepSeek و مدل‌های محلی است.
✨
قابلیت‌ها:
•
🔹
خواندن و ویرایش فایل‌ها داخل ترمینال
•
⚡
اجرای دستورها و کار مستقیم با Git
•
🧠
حفظ زمینه بین جلسات کاری
•
🛠️
پشتیبانی از MCP، مهارت‌ها و ابزارهای اضافه
•
📦
اجرا با DeepSeek، OpenRouter یا Ollama
نصب سریع:
npm install -g codewhale
🔗
لینک:
https://github.com/Hmbown/CodeWhale
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/archivetell/6256" target="_blank">📅 15:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آپدیت جدید
ربات وگا
انجام شد
✨
- اضافه شدن GPT-5.4
🚀
- اضافه شدن Gemini 2.5
⚡️
- اضافه شدن Flux 2 Kelvin
🌡️
- جایگزینی Lucid Origin با Flux 2 در گروه ها
🔄
- حل مشکل هنگ کردن Gemini 3
✅
- رفع سایر مشکلات
🔧
>
آموزش گرفتن API رایگان GPT-5.5
<
ArchiveTel - VegaEnter</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6255" target="_blank">📅 13:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">💵
گوگل اشتراک AI Plus را ارزان‌تر کرد؛ حالا فقط ۴.۹۹ دلار در ماه با ۴۰۰ گیگابایت فضای ابری.
✨
قابلیت‌ها:
•
🔹
دسترسی پیشرفته به Gemini 3.1 Pro
•
🧠
Deep Research برای موضوعات حجیم
•
📒
NotebookLM برای تحلیل و ساخت پادکست
•
🎬
تولید ویدئو با Gemini و Flow
•
☁️
۴۰۰ گیگابایت برای Gmail، Drive و Photos
🔗
لینک:
https://gemini.google.com/app
#AI
#Google
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6254" target="_blank">📅 13:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">📱
اگه حافظه آیفونت زود پر میشه، iMole می‌تونه حسابی به کارت بیاد.
🔍
این ابزار فضای ذخیره‌سازی آیفون رو بررسی می‌کنه و دقیقاً نشون میده کدوم برنامه‌ها و فایل‌ها بیشترین فضا رو اشغال کرده‌اند.
☁️
از بکاپ‌گیری افزایشی هم پشتیبانی می‌کنه و می‌تونه داده‌ها رو با بیش از ۷۰ سرویس ابری مختلف همگام‌سازی کنه. بعد از اطمینان از سلامت بکاپ، فایل‌های اضافی رو هم پاک می‌کنه.
💻
روی ویندوز، لینوکس و مک اجرا میشه و خروجی JSON هم داره که برای ابزارهای هوش مصنوعی و اتوماسیون کاربردیه.
🛠️
پروژه کاملاً متن‌باز و مناسب کاربرهای حرفه‌ای و علاقه‌مندان به CLI است.
https://github.com/chenhg5/imole
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6253" target="_blank">📅 11:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚀
YPtun؛ یک کلاینت VPN متن‌باز جدید برای اندروید  اگر از محدود بودن کلاینت‌های معمولی خسته شدی، YPtun یه گزینه جالب و همه‌فن‌حریفه
👀
🔹
پشتیبانی از VLESS + Reality، XHTTP، Hysteria2 و AmneziaWG
🔹
استفاده از هسته‌های Xray و sing-box در یک اپلیکیشن
🔹
قابلیت…</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6252" target="_blank">📅 10:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYaGHXv5xmhO7ZZD3ks-5rHUqMsHfmI4AhgOts_UcyuMDoc3bORGYQBTa5OaEuw1N82VJbnziYo9K40BjtCAyDcjeiPvXAs2Z9_Wu1IBIlSo-ljpxHK6WCdPZVMBzV2vnucGAoZFscOcNT8H1xtSuulZINyArjpK-FdhByXcQOAPk9V_IC87uZgVhjJWBpANlNqIUXblsnTM4TuyHd0OXWx5zSsNiHyUP6zbgDUdduxEB7xuCSxHm9Sul6JdVo_nO0dzuFceS6yuCWQIS8svg8whJSYiFzi0WyOirvoYMAQM4nqjEhqqHHLoH-lcydjjUxfcvw1nJbOrC6-Bgc98dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Unlimited hotspot shield vpn method! |  7 days trial
/gen 415464440062
trail→
https://get.hotspotshield.com/trial
zip → 1216
Browser any
Ip usa
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6251" target="_blank">📅 10:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwU4IW-vYSgukZOljObV_XHTNEkFcKRl9IxUmmUzv4W9Ha-EvKG9gWbkXrSSdXIJ0ECHQNDjIA9-xEMDEZo8rZ5plzhXKjoi0E7cVX33V3m1LKD4glMmMGtirIthjaV0OJwjOpgE5Md-Dotn9wBL2H2ir97f7_JiFHFyqdI4ycF2sR6IN7Pd6Ewnfa3uB38VNthrDRu8uNDds8WFe88O4NKvjPM0Kg2uKoJmjXKEve3blOS4EToagO7vMAPhNtjodFwSG8fqbF2qFJW_w6DCgf-yChsA0xV5L2TlEEohxhHUJMu8BZH9GMmhG9lvSRGQ1X5hVMJvYInygFOWZGNzDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
با «تحقیقات عمیق محلی» می‌توانید پژوهش‌های محرمانه را روی سیستم خودتان انجام دهید؛ رایگان و متن‌باز.
✨
قابلیت‌ها:
•
🔹
جستجوی خودکار در وب و منابع علمی
•
⚡
پشتیبانی از arXiv و PubMed
•
🛠️
کار با مدل‌های زبانی مثل Ollama و GPT
•
📄
بررسی اسناد شخصی و محلی شما
•
📚
تولید گزارش نهایی همراه با ارجاعات
🔗
لینک:
https://github.com/LearningCircuit/local-deep-research
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/archivetell/6250" target="_blank">📅 10:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgU7Z2ezE0BT5GH5raZjffIr07pQ_sYuhAKRAjDvGcpclbeac0_-2Bqm310EA9vamj0-pn2UgCaXs5Im7Vx8paNylrHEogT_Wd9odbYkS4gNW790Pi94aAJkYGBq8OsFPOJGGOjG4cbU-TrkqBPkHD27bL14oYx9g_lLM8SuEFv31t6kFYi_RvEGditc9rJgIc54K-n_66HTiTnFZ6F3w18w25jd62t5OvrUkDXwOmYXIDXrWJQl0PpwHAsU67zZNGDz0oxJy24d6_Zn1IUCT39tME1XcQF3la7yG6VMGhfrGBO0gYqX-9K79GDNu88BC3D-85ytl6ek0DBm9YsfcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
YPtun؛ یک کلاینت VPN متن‌باز جدید برای اندروید
اگر از محدود بودن کلاینت‌های معمولی خسته شدی، YPtun یه گزینه جالب و همه‌فن‌حریفه
👀
🔹
پشتیبانی از VLESS + Reality، XHTTP، Hysteria2 و AmneziaWG
🔹
استفاده از هسته‌های Xray و sing-box در یک اپلیکیشن
🔹
قابلیت Split Tunnel برای انتخاب برنامه‌هایی که از VPN استفاده می‌کنن
🔹
پشتیبانی از پروفایل‌ها و سابسکریپشن‌ها
🔹
متن‌باز و رایگان
جذاب‌ترین بخشش اینه که از روش‌های پیشرفته عبور از فیلترینگ مثل Hysteria2، AmneziaWG و حتی olcRTC پشتیبانی می‌کنه؛ روشی که ترافیک رو شبیه تماس ویدیویی نشون می‌ده. همچنین توسعه‌دهنده‌ها اعلام کرده‌اند نسخه ویندوز و لینوکس هم در راهه.
⭐
برای کسایی که دنبال جایگزینی متفاوت برای v2rayNG، Exclave یا Hiddify هستن، ارزش یه تست رو داره.
🐱
GitHub:
https://github.com/yanisplugg/olcvpn-client
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/6249" target="_blank">📅 10:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c54422014d.mp4?token=DOvD-vG9uhFNkf8g8I-V7cubSWQIiqbZERFdBg5iFK8zQDPbZoZQtvdQKSAGWuTvmoJRlrE5PcgesHd0yphX41zBNhgWDLK238lpbzFjQZ1B5kYrGKTlVwyJdB9NILs-CWUSx6lms_LmnKJaajdbfi5s2YGzS5iH4dYywUCmgFrWTE2QjQBSYVYUMOoY_C7fbpYBD3rq9TJrFQCfgiSyZJRyopHs5ge24OKIIqGgePiUyAE17Lp2i5u9Y_Tj_jqAV9H-UN88Uagi4PvJ1Y7wXmdKQBvJCHeaLU1yzZ0mcj5NS3nAFpQfDJPNe7l7AY4pRE7AnR48QoF94zEn3TTFbw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c54422014d.mp4?token=DOvD-vG9uhFNkf8g8I-V7cubSWQIiqbZERFdBg5iFK8zQDPbZoZQtvdQKSAGWuTvmoJRlrE5PcgesHd0yphX41zBNhgWDLK238lpbzFjQZ1B5kYrGKTlVwyJdB9NILs-CWUSx6lms_LmnKJaajdbfi5s2YGzS5iH4dYywUCmgFrWTE2QjQBSYVYUMOoY_C7fbpYBD3rq9TJrFQCfgiSyZJRyopHs5ge24OKIIqGgePiUyAE17Lp2i5u9Y_Tj_jqAV9H-UN88Uagi4PvJ1Y7wXmdKQBvJCHeaLU1yzZ0mcj5NS3nAFpQfDJPNe7l7AY4pRE7AnR48QoF94zEn3TTFbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
تلگرام برای اپل واچ
تلگرام به طور رسمی اپلیکیشن خود را برای اپل واچ بازگرداند.
#Telegram
#AppleWatch
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6248" target="_blank">📅 09:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBl3f7rMlVUetovDOvADWpswgvWHN5RIvWYDihVsy-UN_hiXd9EXw8sBw-jVjI2zTSv_OQ5bjkFtVEnqDd4TX2BROH06Aak47rcPQcv6qcZp226Bb3bykBQmNIzaTN_7F0mnpIKhDU6j77apy26UUWMAJMonM8fCddFTvgHFIdB-GAGcG7mP6mBlR8ZtbAsJ66101R5fzBLkjaCVe3IfFaPicbh9EExC4GhycplB_bbxFRHF8KcCbY6gvK4E1HjNq2L9tRHVFSE4fLnAOVGwadvbH69gexGviYtrlFGE5qvIVPHHmnlLs9XT9QMLoY_T6kuRQNertY3UnIULu982rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یک فهرست بزرگ از ابزارهای رایگان هوش مصنوعی برای تست، توسعه و اجرای مدل‌ها
🤖
✨
قابلیت‌ها:
•
🔹
مدل‌های متن‌باز؛ از مدل‌های سبک خانگی تا گزینه‌های قدرتمند
•
⚡
ارائه APIهای رایگان برای توسعه و آزمایش
•
🛠️
اجرای محلی مدل‌ها با تمرکز روی حریم خصوصی
•
💻
دستیارهای کدنویسی رایگان جایگزین Cursor و GitHub Copilot
•
📦
فریم‌ورک‌ها و دیتابیس‌های کاربردی برای ساخت سیستم‌های چندعامله
🔗
لینک:
https://github.com/12britz/awesome-free-models
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6247" target="_blank">📅 09:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">💻
NekoBox 5.11.18 برای ویندوز، لینوکس و مک منتشر شد
🔹
یک کلاینت متن‌باز و قدرتمند مبتنی بر Sing-box برای اتصال به انواع پروتکل‌های ضد فیلترینگ.
🔹
پشتیبانی از VLESS، VMess، Trojan، Shadowsocks، Hysteria، TUIC، WireGuard، SSH، Tor و...
⚡️
🔹
دارای حالت TUN برای هدایت کل ترافیک سیستم.
🔹
سبک، سریع، رایگان و بدون تبلیغات.
🔹
گزینه‌ای مناسب برای کاربران Clash Verge، Hiddify Desktop و v2rayN.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6246" target="_blank">📅 08:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">vless://5dcf2dbf-3e82-4456-8961-287cc732bb0f@85.198.20.217:12817?type=ws&encryption=none&path=%2F&host=Play.google.com&security=none#Germany%20Hetzner-.
10 گیگابایت تانل المان</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6245" target="_blank">📅 03:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eo0phdTXFwv1Riz9UEytK6XuzzEpQOVUF2Y5T76iHTUDsJwyKKcuIMH4y4RPVNp3W4zdqKbZ7rKwMhJxKzoJKCsJ2N76dCLa5Sd3R5DNDkxPuZwSQuZL7cvMlznVorUJH5ObLgapuTxpfK3Dvv6npn6CwcoRcN39o6A0hQQ4fcPdcsE_xbucYyCqZQkH-c-NurMR3D04_H5k58qYE9zPEBc-kG_he3ho2BTqVfv732l9_ZM5l24jNUkYQdF1KM_avqY5g-6ifSiDhQbRcdLqP1QxsFYl9j-6NWaoQhWucqCaRunNZX4VtrVT4yD1hRDZEpnOC7SF5cQVEdIjuL48nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله
😱
💻
اگه با 3X-UI کار می‌کنید، یه پروژه جالب به اسم X-UI-PRO منتشر شده که کلی از تنظیمات REALITY و WebSocket رو خودش انجام میده و دردسر راه‌اندازی رو کمتر می‌کنه.
🚀
🔐
این نسخه Nginx رو هم کنار 3X-UI میاره، SSL رو خودکار تمدید می‌کنه، روی پورت 443 کار می‌کنه و حتی برای مخفی‌تر شدن ترافیک از بیش از ۱۵۰ قالب فیک استفاده می‌کنه.
👀
⚡
از Sing-box، Clash Meta و Cloudflare هم پشتیبانی می‌کنه و برای Ubuntu 24 و Debian 12 آماده شده.
🛠️
اگه دنبال یه پنل کم‌دردسرتر برای REALITY هستید، بد نیست یه نگاه بهش بندازید.
https://github.com/mozaroc/x-ui-pro
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6244" target="_blank">📅 03:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hala Hey _ Live In Concert</div>
  <div class="tg-doc-extra">Armin Zareei _2AFM_</div>
</div>
<a href="https://t.me/archivetell/6243" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">امشب رو با این معما بخوابین
شرکت در کنسرت این شخص، از نظر اخلاقی، غیراخلاقی هست؟
#Moral_Dillema</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6243" target="_blank">📅 02:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🫠</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6242" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyF3QPquaJD_2h6yc4V-YsNTP61eLkAemZJZcog3jjkDDwCW4xrHhtpKJXwTIzx6Jj1I9Q0iLwy65Jqe5w4r29E3Mpf6j8NeXq_LeSm-vRxxFKvUriNbYAd8yvB12HOt_m9VJShEaWL6Ope6tir5t2Xy-gzH-e-w4D74OzLg3OEqbcscrzTM1Pa_DxtkcUe17O13IGkP9uuNWKQzAKZhgzmBw0vem2aO2Mv8Aa5XpMAUesbMMEEM9H6rcP8oJBqTDyDz4FWaH-mSf0PYyuDfcd3Ytv_ILJq_PQssl_wZy0FkhkR0wJKyb_QB3NIBvv7Qsa57YC2b_6VpLvlsHd77Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
Gemma 4 بدون سانسور منتشر شد!
🔹
یه نسخه دستکاری‌شده از Gemma 4 اومده که تقریباً هیچ درخواستی رو رد نمی‌کنه.
🔹
روی سیستم‌های معمولی و حتی آیفون هم اجرا میشه.
📱
💻
🔹
حجمش کمه و با Ollama و LM Studio هم سازگاره.
🔹
جالب اینجاست که با وجود حذف محدودیت‌ها، کیفیت مدل تقریباً مثل نسخه اصلی مونده.
⚠️
طبیعتاً دیگه خبری از فیلترها و محدودیت‌های امنیتی نسخه اصلی نیست.
👀
🫠
..
#Gemma
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6241" target="_blank">📅 01:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
بی رفرال
🤐
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 140 / 140
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6240" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">https://t.me/ArchiveTellNews/212
🤨
🤔</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6239" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6238" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app
بخونید نظرتونو بگید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6237" target="_blank">📅 00:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">StormDNS
a.cyntarix.com
25ffbc77bcfb23b2d4ee225eedcd2466
داشته باشید اگه نت قطع شد</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6236" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این پروژه پایتونی جالب هم برای تشخیص اشیاء توی ناحیه مشخص شده کاربرد داره مثلا طبق مثال خودش که با QWEN ادغامش کرده یه نفر با هودی اومده توی ناحیه مشخص شده تشخیصش داده و به گوشیش نوتیف فرستاده و گفته چه چیزی با چه اطلاعاتی اومده توی ناحیه.
برای دوربین مداربسته خوبه یه ناحیه رو مشخص میکنی هر چیزی اومد توش بهتون خبر میده،کد اصلیش با پایتون نوشته شده و از ابزارهایی مث ffmpeg برای مدیریت استریم‌های ویدیویی استفاده می‌‌کنه.
github.com/roryclear/clearcam
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6233" target="_blank">📅 00:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: نپستر
😎
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6232" target="_blank">📅 00:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">هر کی 99 تا رفرال داشته باشه ی کانفیگ نپستر میدیم بش
😌
🔥</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6231" target="_blank">📅 00:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: نپستر
😎
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6230" target="_blank">📅 00:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
نپستر
😎
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6229" target="_blank">📅 00:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0VOyGtRP8RAK_3vQTk4eu1tFzvhhjmZ7LFbUbyA2q2Hx0VCEndUdjYwFNbYJM0uhCW7zaX2wtDG_yS8GCncd9rm1aeubzrHBXq-jwUrSIKTLdd7RSo9vvLb7nZgpzGxXzKv7QSHMJ3kgUuyuEI8CJVlrkpNgvLIExFk5CCo5dUXMc_pNhxKsYoroLF7vFWVNRVwV2YM2Gilt94mOXOYr6ARtmRkPbq-8DU7tW2WaHGf2D7ZtaXK6bimOjrsbXP3FgulocQxI7gungWVb8GVJpmFs9Kv0doCiPlEDA07biWro5KeRw58jfGtKNq5LORXJpKBiF9j9tz2Nup8r5GYjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Gitdot؛ رقیب متن‌باز GitHub که با Rust ساخته شده
🔹
پروژه Gitdot توجه زیادی جلب کرده و به‌عنوان یک جایگزین مدرن برای GitHub معرفی شده است.
🔹
این پلتفرم از ساخت مخزن، Push/Pull، ریپوهای خصوصی و عمومی و مهاجرت از GitHub پشتیبانی می‌کند.
🔹
رابط کاربری آن با الهام از ابزارهای CLI مانند Vim و fzf طراحی شده و روی سرعت و ناوبری با کیبورد تمرکز دارد.
⚡️
🔹
قابلیت‌هایی مانند Pull Request، Issues و CI هنوز در دست توسعه هستند.
⚠️
با وجود استقبال کاربران، Gitdot هنوز در مراحل اولیه توسعه قرار دارد و فاصله زیادی تا رقابت کامل با GitHub دارد.
🔵
@ArchiveTell
| Bachelor
⚡️
https://gitdot.io/</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6227" target="_blank">📅 23:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🛑
پایان uBlock Origin در Chrome نزدیک است
🔹
گوگل آخرین راه‌های دور زدن محدودیت‌های uBlock Origin را مسدود کرد.
🔹
پشتیبانی از افزونه‌های Manifest V2 به‌طور کامل در حال حذف شدن است.
🔹
فلگ kExtensionManifestV2Disabled نیز از Chromium حذف شده است.
🔹
مرورگر‌ های Edge، Opera و سایر مرورگرهای مبتنی بر Chromium هم این مسیر را دنبال خواهند کرد.
⚠️
نتیجه: نسخه اصلی uBlock Origin به‌تدریج از دسترس کاربران خارج می‌شود و کاربران باید به uBlock Origin Lite مهاجرت کنند.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6226" target="_blank">📅 23:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=DKnDzo1zaDrQGTvUR6JDoj6unepf8b3bIMO8pZz4Kt6Ry7gqVhC6vAJJibIQg7ZLAyrKCbIuCC4WCiMDkhEehwdXLcf6r7DzX9d9qTt2MU4yMOsQf0OWnqiMvSR7IMlB-lAvu6c9jK6TsDv67qYn0nhtDt1JSPDxakbsQ-jk3Zzg0c4ZwlrLKbPBLOAGojYDFVTUbCzwk52Dy0sVAPN5KmywzUav5yRGnVcnvMOf0XoqObKDFA3CMHfZza7p5Dtup0orq3Fpu9Nj-emukwsG7ML52bEC5xG6-v_GppZXEFKtgvo_LBF-AzW5nndi5qKcrrCH1NhJ4TiSH2mYaqeDBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=DKnDzo1zaDrQGTvUR6JDoj6unepf8b3bIMO8pZz4Kt6Ry7gqVhC6vAJJibIQg7ZLAyrKCbIuCC4WCiMDkhEehwdXLcf6r7DzX9d9qTt2MU4yMOsQf0OWnqiMvSR7IMlB-lAvu6c9jK6TsDv67qYn0nhtDt1JSPDxakbsQ-jk3Zzg0c4ZwlrLKbPBLOAGojYDFVTUbCzwk52Dy0sVAPN5KmywzUav5yRGnVcnvMOf0XoqObKDFA3CMHfZza7p5Dtup0orq3Fpu9Nj-emukwsG7ML52bEC5xG6-v_GppZXEFKtgvo_LBF-AzW5nndi5qKcrrCH1NhJ4TiSH2mYaqeDBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6225" target="_blank">📅 22:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaPipgeCRJS0fg4iHwukTtxhIm8Df4lv1ukvRUT1vbjPidsC5n4WfIWcWQBgEJSlrtS0G0pp7F_8Wpu2OjTJTjMQrzR0X2ss2Sxl_-oM_t-PDEtiKspXITxjzxp50gNuvJ1y0IIiDGJLjzlBeYJfgKfMAWVYWEFQv9rAitBg2uL142NjmcAl8XozWv-0fOC52b7LdDPQ2uQhRVKtXUPuDcvouKpvCz_IyXzQuyX0uAQNLip8pmLrewTXPqLX-7R8XIQJXoVNHt3B4-OrrEswtDWDBeVn1d7WIDrlUlD6E-NOtKuZ2BC0oHwFk168OfvECenRe8Vz49_9PdQLRdPVtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یک ویرایشگر ویدیوی کامل که مستقیم داخل مرورگر اجرا می‌شود؛ بدون نیاز به Premiere Pro یا CapCut
🎥
✨
قابلیت‌ها:
•
🔹
پشتیبانی از چندین ترک ویدیو و صدا
•
⚡
رندر سریع با شتاب سخت‌افزاری GPU
•
🛠️
افکت‌ها، ترنزیشن‌ها و ابزارهای تدوین
•
📱
قابل استفاده روی کامپیوتر، تبلت و گوشی
•
🎬
عملکرد پایدار حتی در مرورگر معمولی
🔗
لینک:
https://tooscut.app/
#VideoEditing
#Tools
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6224" target="_blank">📅 22:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">طبق درخواست شما عزیزان
تمامی سرویس هایی که API رایگان هوش مصنوعی در اختیارتون میزارن رو مجدد قرار میدیم
✨
Freemodel.dev
🥇
developers.cloudflare.com
🥈
console.groq.com
🥉
aistudio.google.com
build.nvidia.com
cloud.cerebras.ai
openrouter.ai
console.mistral.ai
llm7.io</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6223" target="_blank">📅 21:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPYp_BupaqzTp_9DH4PCZTMLRdccg7-dY6dHkS60R8GYqpEYoqCcc94pz8k5Tw95CMV5Z_Qupfo7lnG9pY_eXhhWHqU9ZmtnVIxWX6ElcImM9-MDY-nCIFpGG6H0sM7ibkMNuElKqMZq1K-ZnsRTFeU3IGaXYmNua41JEtqM0S8vf7UpiafLxRpO87qdvOrpWJWYYdq0SIuMzne6boL9xOpVkXfx0pMe3f5PC4KpT71-BMMid4sJl6maUxmdO__g9VNWsM4rj4--ZyYEVCl1gaIjeetyq1DK8sTdQ_iYgald1avGkSJ9--fqMJpnBiKeF7b23pO9e9uvPpWjfvS1LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
کاهش بار اضافی روی حافظه در ویندوز ۱۱ — غیرفعال کردن فعالیت پس‌زمینه Edge
😎
این کار از طریق ویرایشگر رجیستری انجام می‌شود:
1️⃣
کلیدهای Win + R را فشار دهید → regedit. را وارد کنید.
2️⃣
به مسیر زیر بروید:
HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Edge
3️⃣
روی فضای خالی کلیک راست کنید → «ایجاد» → پارامتر DWORD → نام آن را «StartupBoostEnabled» بگذارید و مقدار آن را 0 انتخاب کنید.
4️⃣
کامپیوتر را ریستارت کنید.
پس از این کار، Edge دیگر در پس‌زمینه اجرا نمی‌شود و منابع را مصرف نمی‌کند.
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6222" target="_blank">📅 20:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">walf.zip</div>
  <div class="tg-doc-extra">12.9 MB</div>
</div>
<a href="https://t.me/archivetell/6221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ℹ️
فایل سرچ پروتکل و سرور ویندسکرایب
@ArchiveTell
🔥</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6221" target="_blank">📅 19:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚀
برنامه WALF منتشر شد!
اسکنر خودکار سرورهای ویندسکرایب نسخه PC
اگر از عوض کردن دستی سرورها خسته شدی یا دنبال یه راه سریع برای دور زدن فیلترینگ میگردی، این برنامه دقیقا همون چیزیه که نیاز داری.
کار برنامه چیه؟
برنامه WALF کاملا خودکار و بدون اینکه نیاز باشه کاری کنی، تک تک سرورها، شهرها و لوکیشن های ویندسکرایب رو روی پروتکل ها و پورت های مختلف تست میکنه تا بهترین و سریع ترین اتصال رو برات پیدا کنه.
👇
چطور کار میکنه؟ خیلی ساده:
۱. فایل برنامه رو از لینک زیر دانلود کن و از حالت فشرده درش بیار.
۲. فایل walf.exe رو اجرا کن و دکمه Start رو بزن.
۳. تمام! خود برنامه اگر ویندسکرایب بسته باشه بازش میکنه و شروع میکنه به اسکن کردن کل شبکه تا بهترین اتصال رو برات ردیف کنه. (فقط مطمئن باش که قبلا توی ویندسکرایب اکانتت لاگین شده باشه).
لینک دانلود برنامه سرچ خودکار پروتکل پورت و سرور های ویندسکرایب در پست بعدی
⬇️
با تشکر از چنل
@CubicDreams
که زحمت کشیدن ساختن
🙌
@ArchiveTell
🔥</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6220" target="_blank">📅 19:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خب یه پست اختصاصی دیگه داریم این فایل رو خیلی جاها میلیونی میفروختن در حالی که رایگان بودش یکم دیگه پابلیک میکنم
🔥</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6219" target="_blank">📅 18:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKqkt4n-WIiRf1flM14MTfrMQnc-7vcLrUaYDuOnw3QNERFPSmz6xppBKUx3OJ_PkEojN2a4gFqzUZwbxgNmGTiX0OCV0ehpMlJJLBFBbYGiOWM5_JkZRkpcGY_9b4OWLzi3oL3xdmz6c3K2KyrvDUJ_ee8tLkzV-Qw8vXIgQDIkWwcOJ6yQk9RqOg3p7un4FIkNQGGOM8UV41_YOZuGL8jkZI4aWrSMwzfMoYnQJavajdm0abuQFG-lH8FbDOfCqchQ-5SCfJILpNVM2m5Sub15VdmoerPtRZkISMgxf625To9SvuvBF0yELYVN32r36Hqb3dZD7bkSRVyzfy2klA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دریافت API رایگان GPT-5.5 از Freemodel  اگر دنبال دسترسی رایگان به GPT-5.5 هستید، می‌توانید از Freemodel استفاده کنید و API Key اختصاصی دریافت کنید.
👇
📌
مراحل ثبت‌نام:
1️⃣
وارد سایت Freemodel شوید.
2️⃣
با حساب Gmail ثبت‌نام کنید.
3️⃣
پس از ورود، صفحه احراز…</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6218" target="_blank">📅 18:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⚠️
اطلاع رسانی برای افرادی که اشتراک ویندسکرایب پرو خریداری کرده‌اند:
پروتکل
ikev2
روی تمام لوکیشن ها (تقریبا) متصل میشه
✅️
با تست هایی که گرفته شده با فیبرنوری مخابرات  سرعت همه سرور ها دانلود ۲۰۰ مگابیت و اپلود حدود ۵ مگ فعلا قفل هست
(پیش‌بینی میشه پهنای باند ikev2 کم کم محدودیتش برداشته بشه و به قبل شرایط ۱۸ و ۱۹ دی ماه محدودیت شبکه برگرده)
سرعت کانکت شدن به سرور ها و امنیت ، این پروتکل خیلی بهتر از tcp هست حتما استفاده کنید
👌
@ArchiveTell
🔥</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6216" target="_blank">📅 18:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ArchiveTel
pinned «
ArchiveVPN | کانفیگ رایگان
📝
کمپین: نپستر
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/6215" target="_blank">📅 17:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚀
دریافت API رایگان GPT-5.5 از Freemodel
اگر دنبال دسترسی رایگان به GPT-5.5 هستید، می‌توانید از Freemodel استفاده کنید و API Key اختصاصی دریافت کنید.
👇
📌
مراحل ثبت‌نام:
1️⃣
وارد سایت
Freemodel
شوید.
2️⃣
با حساب Gmail ثبت‌نام کنید.
3️⃣
پس از ورود، صفحه احراز هویت نمایش داده می‌شود:
🔹
بخش اول: احراز هویت با شماره تلفن
🔹
بخش دوم: احراز هویت با تلگرام
✅
گزینه احراز هویت با تلگرام را انتخاب کنید.  لینک ربات تلگرام برای شما نمایش داده می‌شود. وارد ربات شوید و استارت را بزنید
🎉
پلن Pro برای شما فعال می‌شود:
هر ۵ ساعت: ۱۰ دلار اعتبار  هر هفته: ۶۶ دلار اعتبار
💰
4️⃣
از منوی سایت وارد بخش API Keys
شوید و یک API Key جدید بسازید.
5️⃣
در بخش Docs می‌توانید مستندات کامل استفاده از API را مطالعه کنید.
🛠
تنظیمات نمونه:
model_provider = "freemodel" model = "gpt-5.5" model_reasoning_effort = "xhigh" disable_response_storage = true preferred_auth_method = "apikey" [model_providers.freemodel] name = "freemodel" base_url = "https://api.freemodel.dev" wire_api = "responses"
🤖
حالا API Key و مشخصات بالا را به هوش مصنوعی موردنظر خود بدهید و از آن بخواهید برایتان کد تولید کند:
✅
JavaScript
✅
HTML
✅
Python
✅
PHP
✅
Node.js
✅
و بسیاری زبان‌های دیگر...
💡
می‌توانید با آن:
🔹
ربات تلگرام بسازید
🔹
وب‌سایت طراحی کنید
🔹
ابزارهای اتوماسیون ایجاد کنید
🔹
پروژه‌های هوش مصنوعی توسعه دهید
🔥
فرصت خوبی برای تست GPT-5.5 بدون پرداخت هزینه است.
@Archivetell
✨</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6214" target="_blank">📅 17:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
نپستر
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6213" target="_blank">📅 17:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کانفیگ ناب اهدایی
💎
hysteria2://5z15av99psrlhdqp@32.195.51.20:39150?alpn=h3%2Chttp%2F1.1%2Ch2&fm=%7B%22udp%22%3A%5B%7B%22settings%22%3A%7B%22password%22%3A%22dlxmzvxvcp3i6v0e%22%7D%2C%22type%22%3A%22salamander%22%7D%5D%7D&fp=chrome&obfs=salamander&obfs-password=dlxmzvxvcp3i6v0e&security=tls&sni=32.195.51.20#usa_hesteria-%40u2vpn-100.00GB%F0%9F%93%8A
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6212" target="_blank">📅 15:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پروکسی‌های اختصاصی آرشیوتل
😎
⚡️
پروکسی ۱
🚀
پروکسی ۲
💥
پروکسی۳
💡
روی لینک بزنید و گزینه Connect را انتخاب کنید.
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6211" target="_blank">📅 13:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcGviuYVHGSRqDBxmmqwj_wlmt-AVfS8tMnyeMbBMMLTdh58DzxlgfB304mRqaaH4FuxZcv63Bo81lL2SynI6vua-b-mCyhWowsNNDiefEigVXb0dKcr08vm7U_11MwA3s2fRrf42bBk5hFotEl9Xz0vXQjpLHTD24xVE6Uqesy6-YsXVQ-77-FJ2EpiCs26aI5Pg0qAhYH52qDGuMOljO80mUVreqAqA01Aeke1nxshdT-WKa-zWPZas2mqEmT1X9UN7pZBgJwCxLZWq0peE5TFgeoxmFZoPdqAEEYJECxlxtlbzPTWTBZOd7cXc9GD-zzUMpYnv_P3P28dSX3l3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب یه روش مخصوص ایرانی‌ها اضافه کرده، رو همه اپراتورها عالی کانکت میشه:
Settings → Connection → Anti-Censorship
گزینه Protocol Tweaks رو روی Enable بذارید، بعد وارد Configuration بشید و یکی از دو گزینه آخر که ایران هست رو انتخاب کنید. گزینه Large TLS رو هم روشن کنید.
پروتکل های udp و tcp رو تست کنید
ایرانسل tcp 587 france
مخابرات همراه اول udp 80
با فیک میل اکانت بسازید
https://windscribe.com/signup
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6210" target="_blank">📅 13:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Syvoe7dCFW8JmBeFtvn9uJ0j9VyQY33IVKEqSyQ2xt5YIO8mZufHrGE5fzy3FJKG4c3Boz-Gb9qeOXb0pyZB8pAD2HlCae78W2ZJmfhWiQnK8ASfOLh_ryKKgGYQZquJ6nRg9YqSLyqNdCR_hEEUgmg6w_aco2ZehwtvKJSbhbF2zPHHiF6mXgeJeHDpA83kj2sf9bdGry7_FvLqsRtlgJ_N4oTXQUdra5Tk_gnY9LqAP1l0GP-xl07eWwcKY_FtysHozGpht2Yq6UYSOVe_c6F57DkUDmcjlGBM1iRtNgTWrsUllGAaGI4IsBwZ3iqfK8ZF65iLJU0dyPc3d_lh4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
Impeccable
‏این ابزار به عامل های هوش مصنوعی کمک می‌کند تا وب‌سایت‌های منحصربفرد و بدون الگوهای استاندارد ایجاد کند
🔥
‏
✨
قابلیت‌ها:
‏•
🔹
آموزش عامل‌های هوش مصنوعی برای ایجاد طراحی‌های منحصربفرد
‏•
⚡
کار به عنوان منتقد، توسعه‌دهنده front-end و نویسنده UX
‏•
📊
آزمایش ماکت‌ها، برطرف کردن خطاها و بهبود طراحی
‏
‏
🔗
لینک:
https://github.com/pbakaus/impeccable
‏
#هوش_مصنوعی
#طراحی
#OpenSource
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6209" target="_blank">📅 13:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oH4B6nbIPheC6k1CBYqmK54aM3B3-lYjD5iS4ENzgUgVB0J7p7ugkEVkQhokeV_lal3liz2p-kXXV9h1Ka77mHf-Afi8tl6NeDIgaqODezBM5K46emxdXN1MjIpoA6zYRfAlHHvILa7F87UDcLiDNbT7C6N-ekhATIB0FkzmQUFVbINBwpv5l7VDIZQmSDkebW90TtR2FWsUx4uSTAp7SvHkI7Ly36NXUh-ZNMJlQHX3QqGk-Ran7v9BZ8TV3XeaypnRg0mNh2nkcup4lQut6FXRv9QU_eaAu9j_8H-RSsugih-0wxJA_zwHrNv_QHtWG9JR2MNQb4EpgZ3l4TmpTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gFr5UK-ECQKva6XgwFHdEQTcRPUjoUIdyGnS1gUe5tkzFS7TIwY0ZAAtHINdHWFg7IVPhI7VuJutsCepZ5QCRfOD7ZNclapNzDJtmyPiQ96_8fzCJSqM8beLTc5QJHKsArneoCSgRze8udxDivDXR7dUvKv_1Qi9kLtmAMQXRrMTzFFWVdQ9axkWbNW9tU-glPWxPXAZZqnWusi9UDCqrkVAHc5PMshKiw705kYKD-uaT6uyHzz-ERS0Gc24GBgl2bkQBmvZcVlzX8m5v7JgT6E03iO23dZXSvo7AdvRrclUUyI0PewKTSG-ogSZ7sA6rMDNDgKbnASDt9UMmzLMxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O1BoZeiwUZyXKL8ChE29Bm_nLiqofpOvEBrj043HClQPY8bbn4ki43lds4F3S5hjxYKxGYfDrbt2IOwR0FyorVje6t-lcyR4gM6xcGnnFHASqFXGX3D1me0HuuzGbAbbEoUJBx4eYq8Y6_T6xnNXzp05clkxe_Cvjfus2KiV3GSo0gFvrNu5_DBpGmSTWXJtbtrbEHOp5MWQfrUplFHlpO618e235Lsnea1ifms2iiooQOrHavOKngaWOgLO60MtFPJjvRu9wMR3GkR3wqxO2t8bZZSpSwmeEDfGvrlGUnimwylY5WJL0VlFDwHPAMuz-bawwsstXRwrCwoMtBZj9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d97888b48f.mp4?token=ToZem2Icc_Y9qzZsXmJmjp5LttcpRsumhCAVsjKCJBJApeQF7GZBPydl5bctxxwSmnMtQ0Vtoy1xxmhQQyauFc8juqW9qTQJ_b3LouAU6iDMZcfIZX422hrZA86sftSUiyaSc0WpFng4sBDoAwzct4OrgUqI1n-CtKKRs7bWATqIaqPzEgfVZhW_uZppKBq-T32LlthJeEFfqwKAAbjT7SJjaTMZV52iu19ucczqxZ_R7jOMAOJTXM4IiZI7LqiAwTPPq43wtulo8YNPSvH3uKzc8g0C-TYklswFlYOZm8ctgCW17qy16DvHJ2F5RwgJu8Mvpxzw5wQfyKa7pYsNiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d97888b48f.mp4?token=ToZem2Icc_Y9qzZsXmJmjp5LttcpRsumhCAVsjKCJBJApeQF7GZBPydl5bctxxwSmnMtQ0Vtoy1xxmhQQyauFc8juqW9qTQJ_b3LouAU6iDMZcfIZX422hrZA86sftSUiyaSc0WpFng4sBDoAwzct4OrgUqI1n-CtKKRs7bWATqIaqPzEgfVZhW_uZppKBq-T32LlthJeEFfqwKAAbjT7SJjaTMZV52iu19ucczqxZ_R7jOMAOJTXM4IiZI7LqiAwTPPq43wtulo8YNPSvH3uKzc8g0C-TYklswFlYOZm8ctgCW17qy16DvHJ2F5RwgJu8Mvpxzw5wQfyKa7pYsNiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮
هوش مصنوعی Siri یاد گرفته است که عکس‌ها را مانند Nano Banana Pro ویرایش کند.
✨
قابلیت‌ها:
‏•
🔹
«بازآفرینی فضایی» برای تغییر ترکیب، زاویه و پرسپکتیو عکس‌ها
‏•
📸
ویرایش پیشرفته برای ایجاد عکس‌های خلاقانه
#Apple
#Siri
#Ai
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6205" target="_blank">📅 12:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrHa8miT6A8n38vuJ_sknKrbyoJ8QRuhePiGsa8tYuD5RCETUYOFfLM9EjtMhyJbCDRtjpevdglE9ueZ9P_rIDG6rsY1voaUdg3IekoJamxgRqMZw4kcqT-EkKr0NSm4dpZkbMVCXMzf5ennkwfWUMx-hzjvyioXxhTfqx22b32adG4iztnnzBhgYtRcstvo9VQX0Ax7Cask2lT6kJDrTYTgbMNKmD6uyo3dCFz4apXPG1rdrMk6sZXGaZL6HFgbwTk0DUMcUYz5E3y16aIKJAavxbOagvrB-zIXt7ucgmpIMTCJ3-aYabJLDehRWVGYyNoF4aVDH7oF5oyxhNsz0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
.FrameCoach معرفی شد!
‏این ابزار هوشمند تنظیمات گرافیکی ایده‌آل را برای هر سخت‌افزاری انتخاب می‌کند و حداکثر FPS را استخراج می‌کند
🎮
‏
‏
✨
قابلیت‌ها:
‏•
🔹
انتخاب کارت گرافیک و پردازنده
‏•
⚡
انتخاب بازی از کاتالوگ
‏•
🛠️
دریافت تنظیمات بهینه برای حداکثر FPS یا بهترین گرافیک
‏•
📊
مشاهده تأثیر هر پارامتر بر عملکرد
‏•
📈
تست تنظیمات و پیش‌بینی فریم بر ثانیه
‏
‏
🔗
لینک:
https://theframecoach.com/
‏
#گیمینگ
#بهینه‌سازی
‏
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6204" target="_blank">📅 12:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">با پلتفرم Cerebras به مدل‌های قدرتمند gpt-oss-120b و glm-4.7 با محدودیت بی‌نظیر ۱ میلیون توکن و ۲۴۰۰ درخواست در روز دسترسی پیدا کنید
🚀
شما می‌توانید کلید API خود را دریافت کرده و پروژه‌های هوش مصنوعی‌تان را با سرعت و دقتی فوق‌العاده پیاده‌سازی کنید
🛠️
. این یک موقعیت عالی برای استفاده از مدل‌های سنگین بدون پرداخت هزینه است
💸
، پس آن را از دست ندهید!
✨
cloud.cerebras.ai
🔗</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6203" target="_blank">📅 11:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32629bb6.mp4?token=r_6n8wXIQajzF6EgFUUswjQ7p35AJCoM_cwJ_GmQkslrdRan3eaCYhewk2pn0FCzr1SxB44kxWraJmYxDyrDONSV3VG6wy4rMqh8jparHTlGc7f_W-FZI4H11GbaJmb3Z9xB0RUzpqhVmk4bMG8vq_4cPAShwFNn_mnMIzUWciJWT7JBHjazKPVolBMEt4eQiUclXaB9YmUKg2F0O3IQBo_Hzr-JVaLCfuxZIhiAM-Mb6swq70o7hYZYHKd_pYAIhrVaDgeekW9mpAVBqysbGzOyeKWRUmiKs8OoYfNmOsqS2oW0InCo1lae19sEC20hZJLCmF3ZFYVfjJ6xUx21bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32629bb6.mp4?token=r_6n8wXIQajzF6EgFUUswjQ7p35AJCoM_cwJ_GmQkslrdRan3eaCYhewk2pn0FCzr1SxB44kxWraJmYxDyrDONSV3VG6wy4rMqh8jparHTlGc7f_W-FZI4H11GbaJmb3Z9xB0RUzpqhVmk4bMG8vq_4cPAShwFNn_mnMIzUWciJWT7JBHjazKPVolBMEt4eQiUclXaB9YmUKg2F0O3IQBo_Hzr-JVaLCfuxZIhiAM-Mb6swq70o7hYZYHKd_pYAIhrVaDgeekW9mpAVBqysbGzOyeKWRUmiKs8OoYfNmOsqS2oW0InCo1lae19sEC20hZJLCmF3ZFYVfjJ6xUx21bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🤖
چینی‌ها یک هیولای هوش مصنوعی با ارتشی از عوامل عرضه کردند — Kimi Work می‌تواند تا صد دستیار را به طور همزمان روی یک دستگاه اجرا کند.
‏
‏
✨
قابلیت‌ها:
‏* تا ۳۰۰ عامل می‌توانند به طور موازی روی وظایف مختلف کار کنند
‏* مرورگر را تقریباً مانند یک انسان کنترل می‌کند
‏* دسترسی به داده‌های مالی را بدون پیچیدگی در تنظیم API فراهم می‌کند
‏* عادت‌ها، زمینه و اقدامات قبلی را به خاطر می‌سپارد
‏* با فایل‌ها و اسناد محلی کار می‌کند
‏* کد پایتون را اجرا می‌کند و فرآیندهای روتین را خودکار می‌کند
‏* کمک می‌کند برنامه‌ریزی کنید و وظایف بزرگ را تقسیم کنید
‏
🔗
https://www.kimi.com/products/kimi-work
#kimi
#ai
‏
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6202" target="_blank">📅 11:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Telegram.apk</div>
  <div class="tg-doc-extra">78.2 MB</div>
</div>
<a href="https://t.me/archivetell/6201" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">12.8.0 (6913)
Directly downloadable from
telegram.org/android
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6201" target="_blank">📅 11:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3qTv69CCTsaROqjbLgYk9eWuvdUSPTyLutbiVGRfMkBrPOKaCnnqn1zEzch4zDoPqr0itQiEEJOqmM76OOd58OEwCZwfswE6pu14wsS-98ZFbne3BETbV6wYMe7gQN4NWs0FrlBAa9AUA3Zr26m6QUfxNP8W0mw7z08pNedIVxVX6lEmz__AiO7zotoyRqfJFY1T1XrHws6Jh733EL4u5XXO9sxOhMZ6-p-XfrDnIlOeZL4ANpw0Ync3-RGuu7nPvNBSklJ_cB7vQg2y6mMSFqQV9WXhNQ4zrh8rNcMftLFqKh-nNNQ9VK00PIJd6R61Vnok_4Eyy1IuPXqAwZ0sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
گوگل NotebookLM را با قابلیت‌های جدید هوش مصنوعی ارتقا داد.
حالا این ابزار از مدل جدید Gemini استفاده می‌کند و می‌تواند فراتر از یادداشت‌برداری عمل کند.
🚀
✨
قابلیت‌ها:
•
🤖
پردازش و تحلیل بهتر اطلاعات با Gemini
•
📊
ساخت نمودار و تحلیل داده‌ها
•
💻
اجرای کد مستقیماً داخل نوت‌بوک
•
📝
تولید اسناد و گزارش‌های مختلف
•
☁️
محیط پردازش ابری اختصاصی برای هر پروژه
🎯
ابزار NotebookLM کم‌کم از یک ابزار یادداشت‌برداری به یک دستیار تحقیق و تحلیل کامل تبدیل می‌شود.
🔗
لینک:
https://notebooklm.google.com
#Google
#Gemini
#AI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6200" target="_blank">📅 10:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee5737315.mp4?token=hlpF2XDlz15V2RQ0Lbxrlszz_8X5JeTOGh6_nGUGdSkUf-YIyDMFdTCxXshe0TnnWJZ_pl3slvvBG_rKO9k6pc3UZ0VQhL0d8qmGi7rkIsfmI-ZtY738d7jOv9M1yhr81eN_vHsFFH_mG8PiNYeZg52e60H3xqVHrrTB9hlYO8Z-1a0W9F3iQiFTZOvj0BnH4StmOuMXVzj7PUCLqgGJEXtvzK8nziD2GXV0thM6HNpF1olT7aoF3vhCoPLg0WL0VEtnu6ZfsLsbwok8YrEQmi05Bl9YWRf9x2cTbRG7B3OOrWCbCnENGXW9T3oh-_O8qcGSxQq3hqTg0t0nvmLzJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee5737315.mp4?token=hlpF2XDlz15V2RQ0Lbxrlszz_8X5JeTOGh6_nGUGdSkUf-YIyDMFdTCxXshe0TnnWJZ_pl3slvvBG_rKO9k6pc3UZ0VQhL0d8qmGi7rkIsfmI-ZtY738d7jOv9M1yhr81eN_vHsFFH_mG8PiNYeZg52e60H3xqVHrrTB9hlYO8Z-1a0W9F3iQiFTZOvj0BnH4StmOuMXVzj7PUCLqgGJEXtvzK8nziD2GXV0thM6HNpF1olT7aoF3vhCoPLg0WL0VEtnu6ZfsLsbwok8YrEQmi05Bl9YWRf9x2cTbRG7B3OOrWCbCnENGXW9T3oh-_O8qcGSxQq3hqTg0t0nvmLzJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔤
پیدا کردن فونت هر سایتی در چند ثانیه
ابزار
Font Stealer
یک ابزار رایگان برای طراحان است که فونت‌های استفاده‌شده در هر وب‌سایت را شناسایی می‌کند.
✨
قابلیت‌ها:
• نمایش فونت‌های به‌کاررفته در صفحه
• دانلود فونت‌ها در فرمت‌های مختلف
• پیشنهاد جایگزین‌های رایگان از Google Fonts برای فونت‌های پولی
🎨
ابزاری کاربردی برای طراحان UI/UX و توسعه‌دهندگان وب.
#Design
#Fonts
#WebDesign
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6198" target="_blank">📅 10:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🌐
اختلال VPNها در روسیه وارد مرحله جدیدی شده است.
گزارش‌ها حاکی از آن است که فیلترینگ در روسیه نیز دیگر فقط بر اساس IP نیست و اکنون الگوی ترافیک و TLS Fingerprint نیز بررسی می‌شود. همین موضوع باعث ناپایداری VPNها، MTProto و پروتکل‌هایی مانند WireGuard و VLESS شده است.
#VPN
#Telegram
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6197" target="_blank">📅 10:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚀
پروکسی محلی برای تلگرام دسکتاپ
TG WS Proxy یک ابزار متن‌باز است که ترافیک Telegram Desktop را از طریق WebSocket عبور می‌دهد تا اتصال پایدارتر و سریع‌تری داشته باشید؛ بدون نیاز به سرور واسط اختصاصی.
✨
قابلیت‌ها:
• اجرای MTProto Proxy به‌صورت محلی روی سیستم
• انتقال ترافیک از طریق WebSocket و TLS
• پشتیبانی از Windows، Linux و macOS
• رابط گرافیکی ساده برای مدیریت تنظیمات
• متن‌باز و رایگان
📥
دانلود و مشاهده سورس:
https://github.com/Flowseal/tg-ws-proxy
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6196" target="_blank">📅 03:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">قابلیت جستجو در وب در ربات هوش مصنوعی وگا اضافه شد.
🔍
همین حالا بیاید و اون رو در پیویتون و گروهاتون تجربه  کنید.
😉
@T_Vegabot</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6190" target="_blank">📅 01:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">موتور جستجوی ربات
Vega
چگونه کار می‌کند؟
🤔
بخش جستجو در وب در Vega از مدل gpt-oss-120b پشتیبانی می‌کند که API آن توسط Groq ارائه شده است.
🌐
همچنین در این سایت انواع مدل‌ها وجود دارند که سرویس‌های جستجوی وب مختلفی را ارائه می‌دهند.
🛠
سایت برای دریافت کلید و تست انواع مدل‌ها
✨
ArchiveTel - VegaEnter</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6188" target="_blank">📅 22:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4acdaced3f.mp4?token=qKA--Q92HZ2SgWGb8uRgDlBIfH3nUHi-R9yAU_4INYT4xRSpKAJJ_EftgdiBPMpPaxEvLLANs7tBY1g6zUET8bwkow-fDFT0--xUTTZqputUIpth8L_N06q2rocNPTC-W6OpVVbGBjdOrlTQms5xiZgsIRX4hJZjsfUndz9T2PmM4xPNOo_w3zfVrLS1FLWREy_iGEHIfoxfV954SnqUKL2KmKYKSOXUUiYAWF4N03ZorknAwyGjnPpPEFxbK7Z6lIDshyyvZG4KdwiWsfCcYBg3d_n2_CeSgVqJGWmlgucb_lSa4EsrliQzZc5pOluFoC3_XG6r4CyxNuZwB5lzgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4acdaced3f.mp4?token=qKA--Q92HZ2SgWGb8uRgDlBIfH3nUHi-R9yAU_4INYT4xRSpKAJJ_EftgdiBPMpPaxEvLLANs7tBY1g6zUET8bwkow-fDFT0--xUTTZqputUIpth8L_N06q2rocNPTC-W6OpVVbGBjdOrlTQms5xiZgsIRX4hJZjsfUndz9T2PmM4xPNOo_w3zfVrLS1FLWREy_iGEHIfoxfV954SnqUKL2KmKYKSOXUUiYAWF4N03ZorknAwyGjnPpPEFxbK7Z6lIDshyyvZG4KdwiWsfCcYBg3d_n2_CeSgVqJGWmlgucb_lSa4EsrliQzZc5pOluFoC3_XG6r4CyxNuZwB5lzgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍎
Siri AI: تحولی در WWDC 2026!
در آخرین حضور تیم کوک، سیری با قدرت گرفتن از Google Gemini به یک چت‌بات هوشمند با اپلیکیشن مستقل و دسترسی کامل به اکوسیستم اپل تبدیل شد.
🤖
این دستیار حالا با دسترسی عمیق به ایمیل‌ها، عکس‌ها و تقویم، می‌تواند کارهای پیچیده و چندمرحله‌ای را به‌صورت کاملاً بومی مدیریت کند.
✨
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6187" target="_blank">📅 21:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/9a53c5a0de.mp4?token=klDJLh-_BSt2sag3xbL-KPulYkS9gYiAiuu3zxs0KcLcMTlg6izO2s89Gl4cH92STobuWI8Vx7H3BflXZwLTS_KkbwUAU_AW5g8BUUpwmZk6PfoDoHQc5E7s4o1BaGZXlF7G_KwVyFD70fnWx0t0QT8hCZih_Iq6QbnVjRbv9w6wmYoCZYqhLbJyL5Li4VSAt_nmsi50OvuiTECvOHM0sY16uoVMEiaf66aM-f3Guzyc8MS1N0n0kY82KyOVqrMSkIv3UWTTOc4ZTr23nEycB8UZLqWOpDIo-SOq2eua1gQFbpe40gYIf6RT5o9SOT-jix-cr2UvULqS7pSjNjNnRg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/9a53c5a0de.mp4?token=klDJLh-_BSt2sag3xbL-KPulYkS9gYiAiuu3zxs0KcLcMTlg6izO2s89Gl4cH92STobuWI8Vx7H3BflXZwLTS_KkbwUAU_AW5g8BUUpwmZk6PfoDoHQc5E7s4o1BaGZXlF7G_KwVyFD70fnWx0t0QT8hCZih_Iq6QbnVjRbv9w6wmYoCZYqhLbJyL5Li4VSAt_nmsi50OvuiTECvOHM0sY16uoVMEiaf66aM-f3Guzyc8MS1N0n0kY82KyOVqrMSkIv3UWTTOc4ZTr23nEycB8UZLqWOpDIo-SOq2eua1gQFbpe40gYIf6RT5o9SOT-jix-cr2UvULqS7pSjNjNnRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Apple
#WWDC26
has started
Watch live:
https://www.youtube.com/watch?v=hF8swzNR1-o
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6186" target="_blank">📅 21:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbC7MkaPbD7p_jp7sO_HC99tmX1ksX3QNcPRnu2_38C_pJ7m1Brn_jD09Ybw7jSDCHdNCvB3-sPeLBk3XNo4atn_spQxdAMgoVCglEDEJie6zkjshKuwWD2WvRbnVNQByayGU9g11ZANTTP1I19-OwgcHgNonaa37jWDP-B8113hh1uP7smMENEmRLu9gldkTbBiEFqnLy7WtsIXH7O2MR7noIxvftvMkWtSUPs3DPM7IqEFjCu-l_9AapU8EA_jMWV923_IgmGMVZ41Onccn6YkMK8G-ILzOGMPz41hvZ6lYSm5riyr50s64YEGbJ0beQ3QC-6kv2dbQBI4bajjTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت ارائه APIهای هوش مصنوعی رایگان
🔥
از مدل‌های چندوجهی شامل متن، تصویر و ویدیو پشتیبانی می‌کند و یک راه‌حل توکن مقرون‌به‌صرفه برای توسعه‌دهندگان ارائه می‌دهد.
🔗
https://agnes-ai.com/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6185" target="_blank">📅 20:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🤖
Kimi Work
دستیار هوش مصنوعی که کارها را خودش انجام می‌دهد
نسخه دسکتاپ Kimi Work منتشر شد؛ یک AI Agent محلی که می‌تواند بخشی از کارهای روزمره را به‌صورت خودکار انجام دهد.
✨
قابلیت‌ها:
• اجرای همزمان تا ۳۰۰ ایجنت هوش مصنوعی روی سیستم
• کنترل مرورگر برای جستجو، کلیک، تایپ و انجام وظایف مختلف
• دسترسی مستقیم به داده‌های مالی از Yahoo Finance و World Bank
• سیستم حافظه برای یادآوری ترجیحات و سابقه کارهای شما
💻
قابل استفاده روی Windows و macOS (Apple Silicon)
🔗
اطلاعات بیشتر
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6184" target="_blank">📅 19:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Er0ydTTByyTyNF-hlbbNFK881pqu_TS39mMKHtXeqC_InQsj84AaGLuq-eL1KAkkC0HKLSconLBp_3G-6Lf4zHGtO6hGCl4IZPKEmlLL4OIAzQ3RtQeDXtmW918sLrFtPBOBjQn_fhpbxPuj7zu9xFK7GzeLWhBv7PwhYhb0O_ZcqFxqqgxZDozTjHFzgNmv_-poRYR7DWOc5xQNJMN48e0hYUez3C0L6USl3d5i0NB6LWi2CKMinKuV7vlaSrWMg8z_dhaZBeUFvS0BD-tSWsk7ByAEJaWtb25fLq_S2z14r3m7AbMRhuIEkCjFdENaF6dgzp4VfZnNucegltyhiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
جعبه ابزار رایگان ویدئو
🔸
فشرده‌سازی ویدئو برای صرفه‌جویی در فضا.
🔸
برش سریع.
🔸
حذف کامل صدا.
🔸
ایجاد GIF از هر ویدئویی.
🔸
تبدیل بین فرمت‌های محبوب.
🔸
کنترل سرعت پخش.
🔸
افزودن واترمارک‌ها.
🔸
ادغام چندین ویدئو در یک فایل.
🔸
همه چیز به صورت محلی روی دستگاه شما انجام می‌شود.
https://www.zipvid.online/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6181" target="_blank">📅 18:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
هکرها با سوءاستفاده از ابزار هوش مصنوعی متا، بیش از ۲۰ هزار حساب اینستاگرام را هک کردند
شرکت Meta اعلام کرد حدود
۲۰٬۲۲۵ حساب اینستاگرام
در جریان سوءاستفاده از ابزار هوش مصنوعی پشتیبانی این شرکت، در معرض تصاحب قرار گرفته‌اند. مهاجمان با فریب چت‌بات پشتیبانی مبتنی بر AI، موفق می‌شدند ایمیل حساب قربانی را تغییر داده و سپس رمز عبور را بازنشانی کنند.
🎯
در میان حساب‌های هدف قرارگرفته، نام حساب‌های مرتبط با
کاخ سفید دوران اوباما، برند Sephora و جان بنتیوگنا (Chief Master Sergeant نیروی فضایی آمریکا)
نیز دیده می‌شود.
🔒
متا می‌گوید این آسیب‌پذیری برطرف شده، لینک‌های بازنشانی رمز عبور نامعتبر شده‌اند و حساب‌های آسیب‌دیده تحت اقدامات امنیتی اضافی قرار گرفته‌اند. این حمله عمدتاً حساب‌هایی را هدف قرار می‌داد که
احراز هویت دومرحله‌ای (2FA)
نداشتند.
💡
این اتفاق بار دیگر نشان می‌دهد که واگذاری فرآیندهای حساس امنیتی به سیستم‌های هوش مصنوعی بدون کنترل‌های کافی می‌تواند پیامدهای جدی داشته باشد.
#Instagram
#Meta
#CyberSecurity
#AI
#Hacking
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6180" target="_blank">📅 18:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFUZcXIB_eZNp95umP1Q_E1pNs1nRqG0_tZHG-pI0Fvrw17pXBjrbRG9jszeJlQmrArZXpoFfNXb_V4LKSclf146DDpJim87_Scb_6uFFQLj-BYk_oBl5kZS9eMNN7j7L43Q4ytBl87Rlx6hS5f8qcEvqv1g7-uwAflDLXoOQyJSGAJDnFG02BAwALdQAZK5oGxkrDhfZlef9x0P9C67UHYRWC4nzY496RahiciIR7R38GsYS2lzsJWrEMSRsWCqmWwdOB4wxB-b9Wsf0BAPgo6fJ6shbm5pt2xPtSExUXC83y0SE1EyJGLBuEsOzCoo1cMnyq-kpYUu0tlqbFZFQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦾
شبکه‌های عصبی اکنون شبکه‌های عصبی دیگری می‌سازند — با عامل هوش مصنوعی خودکار ML Intern آشنا شوید.
⚡️
دیگر نیازی به یادگیری کد ندارید — عامل هوش مصنوعی مقالات علمی را می‌خواند و مدل را برای نیازهای شما می‌سازد
💎
مستندات Hugging Face را مطالعه می‌کند، مجموعه داده ها را جستجو می‌کند، کد می‌نویسد و آموزش را اجرا می‌کند
💥
خطاها را پیدا می‌کند، کد را اشکال‌زدایی می‌کند و شبکه عصبی آماده را مستقر می‌کند
🔗
https://github.com/huggingface/ml-intern
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6179" target="_blank">📅 18:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
کمپانی
OpenAI حالت Lockdown Mode را برای ChatGPT معرفی کرد
🔒
شرکت
OpenAI
قابلیت جدیدی با نام
Lockdown Mode
را برای ChatGPT معرفی کرده که با غیرفعال کردن دسترسی به اینترنت، Deep Research و Agent Mode، خطر نشت اطلاعات محرمانه از طریق حملات Prompt Injection را کاهش می‌دهد.
⚡
این حالت به‌طور کامل جلوی این حملات را نمی‌گیرد، اما آخرین مرحله استخراج داده‌ها را مسدود می‌کند و امنیت بیشتری هنگام کار با اطلاعات حساس فراهم می‌سازد.
💡
با وجود این قابلیت، OpenAI تأکید می‌کند که Prompt Injection همچنان یک چالش حل‌نشده در مدل‌های زبانی است و کاربران باید در استفاده از داده‌های محرمانه احتیاط کنند.
#OpenAI
#ChatGPT
#AI
#CyberSecurity
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6178" target="_blank">📅 17:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کانفیگ ناب اهدایی
💎
ss://2022-blake3-aes-256-gcm:dxzSnG5le2y16bNqdyL2Hj2b9Qjptq2Ust7li7mLR6Q=%3AGZs23OkRjsO4i11hMhke9I48yENOx6VVuL23GKRXTi0=@37.32.8.201:8080#%D8%A2%D8%B1%D8%B4%DB%8C%D9%88%20%D8%AA%D9%84%20%D8%A7%D9%88%D8%B4%D8%A7%D8%AE%D9%84%D8%A7%D8%B1%DB%8C
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/6177" target="_blank">📅 16:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMniPxbj8k4C4kfjJMW0aJcKiWL8D8kHRd09HiGOGh7U7lHpIhBxHArGAQmemeW89DcJQmNWaOGbbFEIn9P0yrsGeX95byvlFC2pe1koATubKjf68OT0Wl9FiwWn0O5FFpC5yN-4qnYqWpmpV-s3jON67NqSw1aswxZjuyEe3DPhtYSaz12M48eT2aM80osMZBCny3EQHkhK2HK-U0htndNGq7nMv5IH8bpGwJglov4oK6T0vRf-StV7oj7DID-6UK0RLb3fOgjoyJLzA6icrBp_sAPQ_GfSqtFxVo5xX3HCzvtie_K956zPmQDtzosIMNTQNuBVHGQ5hNhUDUk8FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخبار تازه و ناب
🔥
@ArchiveTellNews</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6175" target="_blank">📅 14:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🤖
وگا | نسل جدید ربات‌های هوش مصنوعی  وگا فقط یک چت‌بات نیست؛ یک دستیار حرفه‌ای و همه‌فن‌حریفه که بهترین ابزارهای AI دنیا رو کاملا رایگان و بدونه زیرمجموعه در اختیارت می‌ذاره
✨
🧠
گفتگو با قدرتمندترین مدل‌های جهان GPT-4 • GPT-5.5 • Gemini 3 • Llama 4 • Qwen…</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6173" target="_blank">📅 14:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5635b05d63.mp4?token=fwOaoAGbqjww-bvKh2WKOAfsQDnAEEE7Hix5-lz3eJQoteDog_9Q7Fxew2SxzxKXR8wg_cwINtQ-NTgg1xIiI_1Znllb64LzVtX11rBma5GjXkaIBqzHrRvawU3Jj3jMiKM6MIsvLi6Ee-wXZl_MGBGYbuF_GJz69xkM2uyaBAcj5o4CJZ16Pw4Cldot6TfqXYc4jLeiFUY5XrUQM_zpMHs3_SGb8cbqxlAkWQds7KUkxFIN88O4BQvzVNQH5Uw3Z_JARLHIKGAxIkpu4Rq1zfa08u4EI7qcd-D-p9ShnRft_sNvqcd788XquLKAA2J3onQ3IW3A4JiWfEkLQ1s2FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5635b05d63.mp4?token=fwOaoAGbqjww-bvKh2WKOAfsQDnAEEE7Hix5-lz3eJQoteDog_9Q7Fxew2SxzxKXR8wg_cwINtQ-NTgg1xIiI_1Znllb64LzVtX11rBma5GjXkaIBqzHrRvawU3Jj3jMiKM6MIsvLi6Ee-wXZl_MGBGYbuF_GJz69xkM2uyaBAcj5o4CJZ16Pw4Cldot6TfqXYc4jLeiFUY5XrUQM_zpMHs3_SGb8cbqxlAkWQds7KUkxFIN88O4BQvzVNQH5Uw3Z_JARLHIKGAxIkpu4Rq1zfa08u4EI7qcd-D-p9ShnRft_sNvqcd788XquLKAA2J3onQ3IW3A4JiWfEkLQ1s2FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
AlicentAI — هوش مصنوعی برای ایجاد محتوای متنی
💎
این سرویس پست‌ها، توضیحات محصولات و مقالات را بر اساس درخواست‌های متنی تولید می‌کند.
⚡️
از طریق وب کار می‌کند که در آن می‌توانید بلافاصله نتیجه را برای نیازهای خود ویرایش کنید.
🔗
https://alicent.ai/
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6172" target="_blank">📅 13:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">برای مدت کوتاهی اخبار مهم رو منتشر می کنیم
🙏
❤️
کنسل شد نمی کنیم
😂</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6170" target="_blank">📅 12:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
تهران پارکینگ‌های زیرزمینی را به پناهگاه تبدیل می‌کند
بر اساس اعلام شهرداری تهران، در پی افزایش تنش‌ها و حملات اخیر، پارکینگ‌های زیرزمینی در سطح شهر به‌تدریج برای استفاده عمومی به‌عنوان پناهگاه آماده‌سازی و تجهیز خواهند شد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6169" target="_blank">📅 12:47 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
