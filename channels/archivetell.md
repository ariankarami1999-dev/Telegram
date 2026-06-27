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
<img src="https://cdn4.telesco.pe/file/jc1kuLOHnH7CtxhYJt8QonIhPrYWYfpKqnjfGKWQMbcaBayuH2Yvoe_-56KGilW73mCg8upAhFQKOOW9WIui5pSnIL3JOP__BGpoBDQXKFa5zBIH5U1COmn-1Re6Dz8I3YudN-WW6JAMC3FT2s4lYRtuX-Mxxj5a1qzipGzW55VCgtpfWrgJe_Nkez1MvAIByOYTQXu545VnX1G3u9bFqTaXjgXb972Viq1bwS5JOuCDmFilsfe_cdEJDtGu5GhoU39AYJwu_xERIhB2otrxHRu27AJcYmH_N7lpT_Z20QiWBN2Ev24pAtoHSh-fsWV2xg64dvF46XDX_ASaS-yDUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.62K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 12:39:33</div>
<hr>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚀
هوش مصنوعی دیگر کدهای شما را فراموش نمی‌کند؛ دستیار حافظه دائمی برای ایجنت‌های برنامه‌نویسی!
🧠
✨
اگر از پریدن کانتکست (Context) در چت با هوش مصنوعی و توضیح دادن‌های تکراری خسته شده‌اید، این ابزار جدید مشکل شما را حل می‌کند! به تازگی یک دستیار هوشمند برای مدل‌هایی مثل Claude، Codex و Cursor منتشر شده که دانش و اطلاعات پروژه شما را بین سشن‌های (Sessions) کاری مختلف حفظ می‌کند.
🔥
این دستیار چه کارهایی انجام می‌دهد؟
1️⃣
حفظ همیشگی کانتکست:
اطلاعات جلسات کاری شما را ذخیره می‌کند تا با بستن پنجره، کدهای شما فراموش نشوند.
2️⃣
یادگیری ساختار پروژه:
معماری، دایرکتوری‌ها و ویژگی‌های خاص کدبیس (Codebase) شما را کاملاً به خاطر می‌سپارد.
3️⃣
بسته‌بندی خودکار دانش:
اطلاعات جمع‌آوری‌شده را به صورت خودکار و هوشمند بایگانی و بهینه‌سازی می‌کند.
4️⃣
بازخوانی در کسری از ثانیه:
هر زمان که ایجنت به اطلاعات قدیمی نیاز داشته باشد، در کمتر از یک ثانیه آن را فراخوانی می‌کند.
5️⃣
پشتیبانی بسیار گسترده:
سازگاری کامل با
Claude Code
،
Cursor
،
Codex
،
LangGraph
،
CrewAI
و سایر ایجنت‌های هوش مصنوعی.
🔗
لینک دریافت و راه‌اندازی پروژه
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#CodingAgents
#Claude
#Cursor
#Codex
#LLM
#Memory
#ProgrammingTools
#DevTools</div>
<div class="tg-footer">👁️ 206 · <a href="https://t.me/ArchiveTell/6589" target="_blank">📅 12:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuYSXGMEQbGaysQGNnozBAcZvJZseVZRa5XU9c-Tu3x5Y-OlTDRAUW6G8-KSgpVIdzFY2wWL1l697i1U1jT46yptvH2xOheK6xGkQ4u230UXzuYzc5yTyE1-xhTASQsBdNcp7hh-RKWdNwgwdg8GygxTGMHyP6vE60N2Gh8YoYK7UOmyB8eZM5S2VmnLRe9rUiXtCFRlhmyuTODIEUtEubEAyot_Ai5owuh9XywuaqZuWs3qoylO3G0_EMa-x4zFOuUB4R3h_2GxR8Vii-a3CS-W7Ox1AiI095A9G0WiCkPmRPG229lMOJF4rlyVMt3K1QIYWg2-fJLJ9qizFEY5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت 1T کانفیگ شخصی
🔑
🟢
از لینک زیر میتونین شروع به ساخت اکانت کنید :
➡️
sign up
بعد از ثبت نام وارد اکانت بشید و روی
Quick Subscription
کلیک کنید و داخل اپ هایی مثل :
Nekobox,hiddify,singbox و ...
اکسپورت کنین .
به دلیل نوع پروتکل یعنی AnyTls بودن فقط داخل اپ های ذکر شده میتونین اکسپورت کنین و داخل اپ هایی مثل V2ray کار نمیکنن
😬
خط های تست شده :
🛜
🛜
💬
@Archivetell</div>
<div class="tg-footer">👁️ 445 · <a href="https://t.me/ArchiveTell/6588" target="_blank">📅 12:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P3QPcu489bNMZcv-46YB7wmf127Xz1_Smpx0Dg69cZDwLG_9r9ooMTdATh6gzs457bETlsb7-ZKOE7HYTgIwRr2D1Gr9he7Igq_MK-Xh7xxNrehySv6Rz-LOv5BnTYB2lBR6c2BwmvclK8B00sesVfdBTmPBo1NR5ZmWgnOb1nLRNmb6e-DQJdU7PX_a5nykOtMDUhdU6Azv9dW8X6cMWnignp20t5Qvi6m7nU2mTzbtqaUCtFhC4LKGwIOH_16Nca2sipzxwnniMA6JlWXXSY0q-1IzKvd497kJUG1e0_H94CFhLEhR24TQrtRHlRfrwbt-FjIeIYz3QTOVfP8D5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A2ktMJw6YMzpXJ5-IwZNFZLcbzy7NArpeZaubySzK08L_nA6R6Z_32JlI1U0wBF5LXouPJ2c64YdVId5Qq3odUtQYO0p28f10PS7whSxmSqylsHgK2QyZsTeepBBPl7dei4gwXJC6uBrF2roZthVqpsbt1D651NMVs0ZB3Y2FKLrZEh2PglkxbKI7BNyprN2I79b0kNVplmMLXcPf4346MDYMNbVlZC3A9aaT-Nra3kHiUPnzZXb1vn-H0RShH4PXIiS96Yg7YPi42FECkVWbDssRd1ystLiFjq1A15G13ACkLc-MXDSHeVmlE2zEL2cBIwnM5EKFg-MhpnX9xOoBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I9Y_mn3itR9tcPFnt9CJuH5_i62zqjewPxNZhRRWjMrwNKMP-TIyZRSvy9uPVMp4dF7fd5uMish-mFcb91qd-pvrD6SZVCSsYEilWh8Z5rknLrWFxXEChBg-bgh79UsVxWp2s_Vf9SEBvBYcg-P8S191TF6UKOEP8ECw0mTaY4E2xVvuhvgySqvPT5PYOuiQKZD1rKKvsxm6lq2-BkUPDoRIK72ZsTpiyOlsYRk2VofAWUae3U5ndZl16PsTaYIAuTBgLUWPQpaMD3vNYBpjb10QkqJFvNSbrZjf6MBqgC1PlsDZ3mF4swjprEsFza4k4d0kv5Be7b7bHSJGOVCToA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تبدیل عکس‌های معمولی به شاهکارهای هنری با هوش مصنوعی
🔥
✨
قابلیت‌ها:
•
🎨
انتقال سبک هنری (مثل ون‌گوگ) به تصاویر شما
•
🪄
انتقال سبک بصری یک عکس به عکس دیگر
•
⚡
مبتنی بر شبکه‌های عصبی کانولوشنی و الگوریتم‌های پیشرفته
•
🛠️
رابط کاربری ساده و سریع برای ویرایش آنلاین
•
📦
بدون نیاز به نصب نرم‌افزار سنگین
🌐
Site
#AI
#Art
#Tech
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 666 · <a href="https://t.me/ArchiveTell/6585" target="_blank">📅 11:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTKvlFoUPBA4nauUNmDr0lyU1y8F_SkQgQsC6nk6xel20NOPzx13-Z3d9Ak8i5XOmIOURr3n2b_xn2xCMkoPpUFFJOaZeO1rxEq47rvt0VYa_8UHOZQ5b5Ovxsa1w8pr3wepHv84-m7YqjxLXVSxKCkxBVEU8inGbOpuwsjQcsE62J9wdYCq8hglXY_R65W_hWHvf-PhQbaH4oi3EUgAO63tc24TyARFZNUCfBqLeTfC_GNzLhOxVqwfZTAQRVU9kEkS7Rp8UOMASklbAzSuTQoqpqFdXny9_TPLaB4ItfHEKQ_LpfHlDC3yDE2ISAxn0M_z2J-nuOtEgDR9SH3T4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه Orcafile دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما…</div>
<div class="tg-footer">👁️ 824 · <a href="https://t.me/ArchiveTell/6584" target="_blank">📅 09:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه
Orcafile
دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما را مجبور کند پوشه به پوشه بگردید، کل یک دایرکتوری (یا حتی یک درایو کامل) را اسکن کرده و تمام فایل‌ها را بر اساس پسوندشان (Extension) گروه‌بندی می‌کند.
🔥
ویژگی‌های کلیدی Orcafile:
1️⃣
اسکن فوق‌سریع:
قابلیت اسکن بیش از ۱۰۰ هزار فایل در پس‌زمینه بدون افت عملکرد سیستم.
2️⃣
مشاهده لحظه‌ای پیشرفت (Real-time):
نمایش لحظه به لحظه وضعیت اسکن فایل‌ها.
3️⃣
جستجو و فیلترینگ هوشمند:
جستجوی آنی نام فایل‌ها و فیلتر کردن دقیق بر اساس فرمت و پسوند.
4️⃣
دسترسی سریع:
امکان باز کردن مستقیم فایل‌های پیدا شده در فایل اکسپلورر ویندوز.
⚡️
مشخصات فنی و
پلتفرم:
توسعه‌یافته با ترکیب قدرتمند
Python
و
PyQt6
.
نسخه اجرایی (App) در حال حاضر فقط برای
ویندوز
منتشر شده است، اما از آنجا که پروژه متن‌باز است، با استفاده از سورس‌کد و دستورالعمل‌ها می‌توانید آن را در هر سیستم‌عاملی (مثل لینوکس و مک) اجرا کنید.
🔗
سایت پروژه
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#Orcafile
#Python
#PyQt6
#OpenSource
#FileManagement
#WindowsApp
#Github
#Tools
#Productivity
──────────────────────────────</div>
<div class="tg-footer">👁️ 794 · <a href="https://t.me/ArchiveTell/6583" target="_blank">📅 09:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93c42b223.mp4?token=GeF_WUyEjb_ZWWGBwMjW-KkNYCVspU_5qvAT-b1c5NmYVMK1J1AaqsHDjy9zJA5UdSUnfXiK5BL8Nsi2QPKlkd7zji2lkO_TwReRAqVq-5ByMeZcJJQ2ztdCKPtyz3aOzp5JoH3hiNIYU7Ec2YVyfc3JQP7xaA-W58TFbceLJ-siMlWlV34MOF5k_0eML6d9-5TDEH289sTfPTC-TUp9pWQAJA4Hx87YTBvDgKmH6rpE9-iSFKZPHrU9fcxRLyjWGXVoeH3kILLtoN1wiF3DltDCgdVQwlaKAZMPLHwbtkiHZKfjKFhtmXTQQ5EcRyrgDfx66D4pFqXatb2UuFJhQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93c42b223.mp4?token=GeF_WUyEjb_ZWWGBwMjW-KkNYCVspU_5qvAT-b1c5NmYVMK1J1AaqsHDjy9zJA5UdSUnfXiK5BL8Nsi2QPKlkd7zji2lkO_TwReRAqVq-5ByMeZcJJQ2ztdCKPtyz3aOzp5JoH3hiNIYU7Ec2YVyfc3JQP7xaA-W58TFbceLJ-siMlWlV34MOF5k_0eML6d9-5TDEH289sTfPTC-TUp9pWQAJA4Hx87YTBvDgKmH6rpE9-iSFKZPHrU9fcxRLyjWGXVoeH3kILLtoN1wiF3DltDCgdVQwlaKAZMPLHwbtkiHZKfjKFhtmXTQQ5EcRyrgDfx66D4pFqXatb2UuFJhQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💻
JanAi
جایگزین محلی ChatGPT
این برنامه مستقیماً روی کامپیوتر اجرا می‌شود و نیازی به اتصال به اینترنت ندارد. می‌توان از مدل‌های زبانی مختلف برای متون، برنامه‌نویسی و سایر وظایف استفاده کرد.
🌐
Site
#AI
#OpenSource
#LocalLLM
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/ArchiveTell/6582" target="_blank">📅 09:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u3EiScSDhquj1VFA2M54F3uWSPZKH6F07mfiisRItkP5NbbCxjkzDYRBr2MZ5VVVwkVV7Xy9qlf9Cyv3m6Jzh6OOcC-XH-7m2QAoeFHkCINRATIgvrpPU44gydrHjEJTtLHqHMQGfBnEn3dr6t8-eRR0O6O5zQ86fBupO_Uh7gThTMtpLmCKCmg4F_moZzXDZcMxQWsj27CWvpVRUCrQQedGvqLBMBCxXSyzBNG__pIXCFxjWivhgXloAWnQT-Vru70AYesrjvw7EK_fZkujuNbU1xntqZgl7m2wjh-6XWYXq3ad1Klf8RvTtIo4SixRmxWnD9mwxcAdiBV26FWp5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JLMjAVLvi27SwrQQYJcmVlP6Ei7ZPwMa04d1zZDeK1_Ra8V9bZlX8YqnmE8Tv0a0-DZHf3IA4PaBn2mGcrUkUPahBipDZ0h0PCA9ag3VqyymJwvxl4Amg8xdfv3D6Brcv8uo1ErHFJ07zeM_EXGR9FBkXOeLpaNs_o3mhHd13g6s_GxrdnXeRGDIX4pKZQdhn02ktMAExe7NgSxeQYLzi4ckaefaJfnypYBl-sTnm0VurGYThAQN1iJNgOLFjHV5Q8Tt0wZ9dX1MSGlTDxvXpsBUYBmAIJWHtf1FaIucNhOhFDudoPGDTasIXD0-XfTc1OOTfUbQY5J5CGd-ZxtnAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
«انجمن‌ها» به تلگرام اضافه می‌شوند — در نسخه آزمایشی برنامه چند ویژگی جدید پیدا شده که عملاً پیام‌رسان را به دیسکورد تبدیل می‌کند.
• در انجمن‌ها می‌توان چند گروه را در یک فضا ادغام کرد، چت‌های عمومی و خصوصی اضافه کرد و همچنین دعوت‌نامه‌ها را به آنجا ارسال کرد.
• همچنین می‌توان کانال‌ها را به انجمن‌ها اضافه کرد، اما این ویژگی هنوز فعال نشده است.
تاریخ انتشار به‌روزرسانی بعدی هنوز اعلام نشده است.
#Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 921 · <a href="https://t.me/ArchiveTell/6580" target="_blank">📅 08:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">طراحی وب و اپلیکیشن در یک ثانیه با ابزار جدید GenSpark
🚀
✨
قابلیت‌ها:
•
🔹
تحلیل مستقیم فایل‌های Figma، عکس و کد
•
⚡
تولید طرح نهایی بدون نیاز به کدنویسی دستی
•
🛠️
دسترسی به قالب‌های آماده برای وب و موبایل
•
📦
ساخت رایگان نمونه‌کار برای فریلنسرها
🌐
Site
#AI
#WebDesign
#GenSpark
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/6579" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6577">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5afGLPxXref98BtKieKJBZffyKJ_xEJ0vQbdBwA1MN0jxMAxu1ZsxEmzTuiboyOCSvh-VVhJThfhoO61Arj7rSwGZzeSukYpC0NZp1m7GlI2tT7GtAR32UdKtZeSKc4gWQCNBTlz76cHs-hgs0UtG6gy3Te3wrbFX54GCyMuC0M936Shq7Do6VuvVjLcNvaaBGqMRTl90J1gbsNuyJ5G9eY5GeCVqjlb1qBlmFYaFqQ4OtotLzwrPGfGcDwOcrkYnLFkF_DYygM34P0paXC6yxHAO0ZLo4Uljx7Wki0K_yLb-_8O92F_N92VEdZ5QtUFD1qKtSf6Mzc6eYVWe5HsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
انگلیسی رو تو حرکت، باشگاه یا پیاده‌روی تقویت کن!
با این ۵ پادکست، بدون کتاب‌های خسته‌کننده به گفتار زنده عادت می‌کنی:
•
🇺🇸
American English Podcast
: انگلیسی آمریکایی، فرهنگ ایالات متحده و مکالمات واقعی.
•
🧠
English Learning for Curious Minds
: داستان‌های جذاب درباره علم، کسب‌وکار و زندگی.
•
⏰
6 Minute English (BBC)
: قسمت‌های کوتاه با واژگان جدید، اصطلاحات و موضوعات روز.
•
🗣️
The English We Speak
: عبارات مدرن، زبان عامیانه و اصطلاحات مکالمه‌ای.
•
🇬🇧
Luke's English Podcast
: تحلیل زبان و فرهنگ بریتانیایی، یکی از معروف‌ترین‌ها.
#EnglishLearning
#Podcast
#Language
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/6577" target="_blank">📅 22:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRS0kcwBDOPNrjueSW0v9pfAtdBKpZhdvEebQ-t3rVjlFfs0ckKvMwVJg-4LOIMiyxKVX7l6H1T60NHTNeB1Ur0PEsYZLrqEW67J433OnGeBtGiQ-H12yEOJoA77krk2-vt4MDUPZZkOBQEJZB_jwioz0dE0h9c6NoHZUSFkVhhboDpwxx0b9berEC0ZiCd6s5y9mCJXK-QjlCL4_moaXhnjvPFC-TQveiJl6PySBr8ViWNhAtc51wylTHAHQxH1pUGksuCuaCECHM-3ydyOBIVLjU0786iVm3laLSRAvbxEQYU0g6TOsNN-2MwupkEecP7l-kTMshmVnFRhl1kBZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oFqufkFzekGsYQktT0ebsU7CD3saKqIYlE0Bb2YCy4upfnaIME-N2yD2XkQUTo-cQg6HTitxsSkLPKShEYaJJtRuZvvyP7bA3mPs868bgCv50FQTXwvz3H19FWxZ9zYNO582VnHY1yJIOd_Og8ZjHcuVjKqcrfqwBWe4n93AOQV8sDs6P4tYxoWOwQIVFyE0ryOFjninqOH5VPWFCbL-5_Rsk4Z_xs7KDJkaro6BpQ_4TAYQJhDo3MgsFX1tcHrjs_V5onaODyHypZxTn9ugq6dVWg5ZfqwyRMiNw7H74wcWOJBXfYkGjb907Q1bjhYRQxw_U04e9Y87TWm79ISTbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phpA2_2X596bfFA335dSrY9nZTWDYC5IyzfpPasN0EjDs7iby-wVozUi8dVEmlAjfCTelk0SZiZ4Cju5GJrzUOwGQxziBOShpGhFrEOs-GBOE34lZs7VFnOjD_m9sdurFkuuWqPfhOtzcUebven7RLBOHPK1Vk0wH2eiijs1u5UYg9BOK38BQn0RqV8jKi2or8gLbuOSZdrMol_xdIWbjTRc1YxShlpMEo_-IKlvF1zCeI7cX0XvdZeKDnNoAelrgra0Pra-dOopnOCMSNVfyTwmN2t4D-9J-LygAvo-9-a3dSuZd3YDSrlxfIguYGv8jiYpf9mreqvpKPsI-PjA8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
OpenAI
مدل جدید GPT-5.6 Sol را معرفی کرد؛ مدلی که در چند بنچمارک مهم، حتی از رقبای مطرح هم جلو زده و تمرکز اصلی‌اش روی کارهای پیچیده و توسعه نرم‌افزار است.
💻
🧠
•
🔹
عملکرد بهتر در بنچمارک‌هایی مثل Terminal-Bench 2.1
•
⚡
توانایی کار مداوم روی پروژه‌ها برای ساعت‌های طولانی
•
🛠️
مناسب‌ برای توسعه نرم‌افزار با دخالت کمتر انسان
•
📦
معرفی مدل‌های سبک‌تر و ارزان‌تر Terra و Luna در کنار Sol
🌐
Site
#AI
#OpenAI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/6574" target="_blank">📅 21:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">الان برای API بهترین
aerolink
هست که بهتون
opus 4.8
میده
خیلی ساده
لینک ثبت نام
نحوه ثبت نامش دقیقا مثل
freemodel
هست طبق این
پست
نحوه اجراش روی
claude code
هم همونه فقط تنظیمات رو این بزنید
هر ورژنی از claude code هم بزنید قبوله
{
"env": {
"ANTHROPIC_API_KEY": "کلید",
"ANTHROPIC_BASE_URL": "https://capi.aerolink.lat/",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلید'"
}
لیمیتش هم دقیقا مثل
freemodel
هست
فقط مشکل اینه هر ip ایی تو claude code قبول نمیکنه باید تست کنید
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/ArchiveTell/6573" target="_blank">📅 21:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAssa</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=Uiw779kySIPIWjUv-RKVdjk0LaKIJz7KBrZwegoNGDhSIrLrOLdfSZarTX1_C0v7yrtlCAqq9-_wfA9VaPPKZCHWdDsHXgcx6fKAKUyDb9YZuE3sUcnhLDE1OcB2BAVQm3II3CifQiSsRlAvBiMsUpAaXeHJVjWmKrIzyaPl8QbP9gRDsJ9aoYTKhdA_WMmLP0KVpIpkEWCEzC7QQrbKycdWUoSpRqrfeLYD5zKzfYGHJW_7WKpB3DAADQyxUsQuCO2We8ikWdyTMCrlIH-qNF0Xk3GdD3OMU7pSH3bwHHqE3X5mmSPYUUzEUaltMnnI9BbaGxMnA99yeeC4Ybj7jlup3HPeBlvGziengiWGQ7IdC3e7oR7ZEErLMH2KlN8WysowY7bdGhPxLJ9_q1sGsch6m-sudbOJw3qqDh9XVTtjPnk0JZcCWrsn4cirsUegwPvELqUhUwHiStf-3jDnI_Jc18tO2QGHIXI3BDTWiYaLPXEf9C9K5xEs5PUu6RdP46gI5DsuBes0xGcIxg3w3dR6ueTiibatbWw1l-RV390ah-6GcW5wpPXXeJigYyFUYC9dqgB1h6SNOtqRHagzyGTdIzYkH8YLpGXJcp-LpivXzk2Q05BQHB1Eb2EhcSrs8AclL7diyaUE8zoFSbnpyzP5x5sMJkZ7_wV-vM3_H1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=Uiw779kySIPIWjUv-RKVdjk0LaKIJz7KBrZwegoNGDhSIrLrOLdfSZarTX1_C0v7yrtlCAqq9-_wfA9VaPPKZCHWdDsHXgcx6fKAKUyDb9YZuE3sUcnhLDE1OcB2BAVQm3II3CifQiSsRlAvBiMsUpAaXeHJVjWmKrIzyaPl8QbP9gRDsJ9aoYTKhdA_WMmLP0KVpIpkEWCEzC7QQrbKycdWUoSpRqrfeLYD5zKzfYGHJW_7WKpB3DAADQyxUsQuCO2We8ikWdyTMCrlIH-qNF0Xk3GdD3OMU7pSH3bwHHqE3X5mmSPYUUzEUaltMnnI9BbaGxMnA99yeeC4Ybj7jlup3HPeBlvGziengiWGQ7IdC3e7oR7ZEErLMH2KlN8WysowY7bdGhPxLJ9_q1sGsch6m-sudbOJw3qqDh9XVTtjPnk0JZcCWrsn4cirsUegwPvELqUhUwHiStf-3jDnI_Jc18tO2QGHIXI3BDTWiYaLPXEf9C9K5xEs5PUu6RdP46gI5DsuBes0xGcIxg3w3dR6ueTiibatbWw1l-RV390ah-6GcW5wpPXXeJigYyFUYC9dqgB1h6SNOtqRHagzyGTdIzYkH8YLpGXJcp-LpivXzk2Q05BQHB1Eb2EhcSrs8AclL7diyaUE8zoFSbnpyzP5x5sMJkZ7_wV-vM3_H1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو بخش انتخاب پنل ۴ تا انتخاب وجود داره
طبق تجربه نوا و زئوس پنل های خوبین</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/ArchiveTell/6571" target="_blank">📅 20:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚀
معرفی Cloud WZA
با Cloud WZA مدیریت سرور و ساخت کانفیگ‌های کلود ساده‌تر از همیشه شده است!
🤖
یک ربات تلگرامی قدرتمند برای ساخت کانفیگ و مدیریت سرویس‌ها، با امکان دیپلوی سریع پنل‌های محبوب:
⚡
Nova
⚡
Zeus
⚡
BPB
⚡
Nahan
فقط با یک دکمه پنل موردنظر خودت را دیپلوی کن و بدون دردسر شروع به استفاده کن
✅
✨
امکانات Cloud WZA:
🔹
ساخت و مدیریت کانفیگ کلود
🔹
دیپلوی خودکار پنل‌ها
🔹
مشاهده میزان مصرف کاربران
🔹
ساخت کاربر جدید
🔹
مدیریت کاربران
🔹
تغییر رمز عبور
🔹
مدیریت آسان و سریع از داخل تلگرام
Cloud WZA؛ راهی ساده، سریع و هوشمند برای مدیریت سرویس‌های کلود
☁️
🚀
🤖
ربات:
@nova_wzabot
ــــــــــــــــــــــ
توسعه داده شده توسط AssA
✨
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/ArchiveTell/6570" target="_blank">📅 20:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=Yz7fSgeo65wsH--YcIrjrZ8cQlVk5BK0J4j_Ryn7WPBiBBZAaeens52LHoCjt95kxQ15usMgIubhqJaazY0-kB3_a4D_uHIxcBTfMR1aGa5LEJNtpqFV9TFUqmj3PdFcpQjBzDP6hmYg9sD14BCieyfS-suJypyfrMwmE4iPfWOt89x8LDzgREvGr5CJQu0-xnStGEDuscg4rm0ziw_r5bnNbHEvRoyzONh-ahH91u5s32VIjznHXRmO3uRGW1wsVV2ZkNLqutWut5nZe48M4j8xUbNJcx81l18kC3e695Xmk3f2JBh-CQiSZoCEl8izFn9hNNMCLjkL0_ZSDPgDEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=Yz7fSgeo65wsH--YcIrjrZ8cQlVk5BK0J4j_Ryn7WPBiBBZAaeens52LHoCjt95kxQ15usMgIubhqJaazY0-kB3_a4D_uHIxcBTfMR1aGa5LEJNtpqFV9TFUqmj3PdFcpQjBzDP6hmYg9sD14BCieyfS-suJypyfrMwmE4iPfWOt89x8LDzgREvGr5CJQu0-xnStGEDuscg4rm0ziw_r5bnNbHEvRoyzONh-ahH91u5s32VIjznHXRmO3uRGW1wsVV2ZkNLqutWut5nZe48M4j8xUbNJcx81l18kC3e695Xmk3f2JBh-CQiSZoCEl8izFn9hNNMCLjkL0_ZSDPgDEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">KREA.AI
Enhancer
تصاویر پیکسلی را تا 22K ارتقا دهید!
دیگر نگران کیفیت پایین عکس‌هایتان نباشید؛
KREA.AI
با ابزار قدرتمند Enhancer خود، تصاویر بی‌کیفیت را به وضوح خیره‌کننده تبدیل می‌کند.
🖼️
✨
✨
قابلیت‌ها:
•
🔹
ارتقاء کیفیت تصاویر تا وضوح 22K
📈
•
⚡
تبدیل پیکسل‌های بی‌کیفیت به جزئیات واضح و شارپ
🔍
•
🛠️
استفاده آسان و سریع برای نتایج حرفه‌ای
🚀
🌐
Site
#AI
#ImageEnhancement
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/ArchiveTell/6569" target="_blank">📅 20:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxRifyTOfXnvkXMG8zFljjynpoGGq_yzvkuduTORaxOK-LU_hSsZucSKSa5zusf109Ad1ETq3p2xoTrFfwKYcYl4efrn4x6Jfvk0P9M5bDVrkJyFSa2xTMhiuCqh69ijOJHhRoC742BgL21mtXGFTbr8lqWXjX8BnjcBWsSUsBkZ7nAoeGHQplzyVPzC5cWJLexHrB1v00MlmTh9HVCtv4fbxH8e5xc3sPTi81YZZnvRq0gLu7g46vemS_-c_PTcxoAxG5izsnx60tHe9z5D6y-hhmBEOxzis_Y1f12ltW6o_j36CfggtjsJ4fhN5OmR8wa0qKFL9lTjWZgF-tFLWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1000 برنامه رایگان برتر برای آیفون و کل اکوسیستم اپل: یک دانشنامه واقعی از نرم‌افزارهای مفید در گیت‌هاب ساخته شده است!
🍏
در این مجموعه همه موارد ضروری پیدا خواهید کرد: از پیام‌رسان‌های امن گرفته تا ابزارهایی برای تماشای فیلم از طریق تورنت.
🎬
🔐
🌐
GitHub
#Apple
#iPhone
#FreeApps
#GitHub
#OpenSource
#Productivity
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/ArchiveTell/6568" target="_blank">📅 19:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=PmEUMmvRpMVTDxN5LLLhnAdeq_3JZ1bJSyTGkpTV4BA6h7agIkS7H0DRAL72Nk_d89igNrRrxa3Xu7D_6_Fn4JUeM0bZ_sprX-9ueqpSVLyNL6RLuB7hq01AlZuoAIC-ui8_2mGzOlpW-R_0ctiJEnMIZ5Dcrvnxa7oxChW43BfaSw8bfvhXSkJzw1z2jngdWtsjv0_EV3Vdcrtw9NPd16lZ0hqSE5MMv70HYQRAVd13I4xn1DiJaStMduPauQE50k_xYUBux8pBFvKc8_29mhr_I0UdYEUBFUkYy37o3JVunp4ca5DWP87GBP_8GgWjbFWffVEmvjvOdsmdYMOWcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=PmEUMmvRpMVTDxN5LLLhnAdeq_3JZ1bJSyTGkpTV4BA6h7agIkS7H0DRAL72Nk_d89igNrRrxa3Xu7D_6_Fn4JUeM0bZ_sprX-9ueqpSVLyNL6RLuB7hq01AlZuoAIC-ui8_2mGzOlpW-R_0ctiJEnMIZ5Dcrvnxa7oxChW43BfaSw8bfvhXSkJzw1z2jngdWtsjv0_EV3Vdcrtw9NPd16lZ0hqSE5MMv70HYQRAVd13I4xn1DiJaStMduPauQE50k_xYUBux8pBFvKc8_29mhr_I0UdYEUBFUkYy37o3JVunp4ca5DWP87GBP_8GgWjbFWffVEmvjvOdsmdYMOWcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک برنامه‌نویس جوان توانست با ترکیب علاقه و مهارتش، درختی که با پایتون کدنویسی کرده بود را به قیمت 8 هزار دلار بفروشد. این پروژه از 100 دلار شروع شد و در چند روز به این قیمت رسید
🤯
#Python
#Programming
#Business
#DigitalArt
#Success
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/6567" target="_blank">📅 18:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚀
آموزش اجرای Opus 4.8 در ترمینال با Claude Code توسط Agentrouter
1️⃣
ثبت‌نام در Agentrouter
وارد سایت
Agentrouter
شوید
با حساب Github ثبت‌نام کنید
بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🎉
شما 125 دلار کریدیت گرفتید
2️⃣
ساخت API Key
وارد سایت شوید
از منو بروید به بخش
API Token
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
"ANTHROPIC_BASE_URL": "https://agentrouter.org/",
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
حالا آماده استفاده است
🚀
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/6566" target="_blank">📅 18:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚀
دسترسی رایگان به API غول‌های هوش مصنوعی!
با لینک زیر به جدیدترین مدل‌ها دسترسی پیدا کنید:
🔹
GPT 5.4
🔹
Claude Sonnet 4.6
✅
سازگار با همه پلتفرم‌ها:
ربات تلگرام ، وب‌سایت ، Codex و Claude Code
🔗
zyloo.io
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/6565" target="_blank">📅 17:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=isfPBAtoxgq1SwOjY1GGkYky1PmQwyNGrkqebc9OI7FNOlkiUreKU7DIzWU3dzVx1E-sB7bdgNrBmT7m4xRzcdwFH-QssWJmpixTD-f_0GbK5CMCoCShAwAH-ZIm1XGg34JfUZ3KwOmb2Xr2Uc3Qba_vKuTxP4ng1La7Y5epw1TkIKuh_82K0oZnZa4zycsiw6nT8K7XxJKlnhMUb3Jbw12doD1g2GTCTDdSoHiNbE0NbsVEL2SokAUKvRdVc4wIbMD2fBGs_MfXWpB5mIBY4tdmguDAvxa1jgAHYSJTws9TKJOoj-NfGZnVSaYhHKsdu19sQLDVGU0ys4l6S3Wkcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=isfPBAtoxgq1SwOjY1GGkYky1PmQwyNGrkqebc9OI7FNOlkiUreKU7DIzWU3dzVx1E-sB7bdgNrBmT7m4xRzcdwFH-QssWJmpixTD-f_0GbK5CMCoCShAwAH-ZIm1XGg34JfUZ3KwOmb2Xr2Uc3Qba_vKuTxP4ng1La7Y5epw1TkIKuh_82K0oZnZa4zycsiw6nT8K7XxJKlnhMUb3Jbw12doD1g2GTCTDdSoHiNbE0NbsVEL2SokAUKvRdVc4wIbMD2fBGs_MfXWpB5mIBY4tdmguDAvxa1jgAHYSJTws9TKJOoj-NfGZnVSaYhHKsdu19sQLDVGU0ys4l6S3Wkcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮
Morflax Mesh — تصاویر سه‌بعدی در مرورگر
این سرویس امکان ساخت تصاویر سه‌بعدی را در چند ثانیه فراهم می‌کند. عناصر را بکشید و رها کنید، فرمت‌ها را تغییر دهید، رنگ‌ها و نورپردازی را تنظیم کنید — همه چیز مستقیماً در مرورگر کار می‌کند.
تعرفه پایه رایگان است و دانلودهای نامحدود دارد. با پرداخت ۸ دلار در ماه، به کتابخانه سه‌بعدی، خروجی با کیفیت بالا (.jpg و .png) و قالب‌های آماده دسترسی پیدا می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/6564" target="_blank">📅 16:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nC3w9LV5cvUXwOBMCnN6T0GV-NwnPKPM2tKyze4UBr3U-d-siOD7ROqPlPCuJhSIhuAGql5d8p2RFrpg5q4pHpOAJjdVgyvP8oTtGWN55DXWyXGCQ3zvtm3p4zjHg_7JLfl9i3-vAWquHk5OvTj9OaSuGBS6IL_XV8veoX8hegcR_jIV4JHa-9mKNvrviLdRrJq7KB1HJ6YIt-FqtUBXsIxxosvReZwyRqTm3rJlyyrhtHqLC_3Unyib9u7tb-EtjxD3SfjNI3nhG3GT2evhppftmgSf-UhF0hOgbrp5aIuwwLyrZu3g4QsqVlk_BJPL6ThP1be72HC60Rvpso5vCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یه ترفند خفن برای چند برابر کردن سرعت گوشی‌های سامسونگ!
احتمالاً شما هم فکر می‌کنید هرچی مقدار RAM بیشتر باشه سرعت گوشی بالاتره، اما یه گزینه‌ای تو گوشی‌های سامسونگ هست به اسم RAM Plus که به صورت پیش‌فرض روی همه مدل‌ها فعاله و برخلاف اسمش، تو خیلی از مواقع باعث لگ و کندی اعصاب‌خردکن میشه!
🤦‍♂️
🧐
اما چرا این اتفاق میفته؟
قابلیت Ram Plus در واقع میاد بخشی از حافظه داخلی گوشی رو به عنوان «رم مجازی» اشغال می‌کنه تا برنامه‌های بیشتری تو پس‌زمینه باز بمونن. از اونجایی که سرعت حافظه داخلی به مراتب از رم فیزیکی (سخت‌افزاری) خود گوشی پایین‌تره، وقتی سیستم می‌خواد اطلاعات رو بین این دو جابجا کنه، پردازنده بی‌دلیل درگیر میشه و گوشی کُند میشه.
🛠
چطوری غیرفعالش کنیم تا گوشی پرواز کنه؟
کافیه وارد تنظیمات گوشی بشید و دقیقاً این مسیر رو برید:
⚙️
Settings > Device Care > Memory > RAM Plus
(اگر منوی گوشیتون فارسیه: تنظیمات > مراقبت از دستگاه > حافظه > رم پلاس)
گزینه بالای صفحه رو روی حالت Off (خاموش) قرار بدید.
بعد از این کار گوشی ازتون می‌خواد که یک بار ری‌استارت بشه)
✅
🆔
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/6563" target="_blank">📅 15:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚀
معرفی MinerU؛ استخراج جادویی و سریع متن از انواع فایل‌ها!
📄
✨
اگر برای پروژه‌های هوش مصنوعی (مثل RAG)، کارهای تحقیقاتی یا روزمره نیاز به استخراج متنِ تمیز از فایل‌های مختلف دارید، ابزار رایگان و متن‌باز
MinerU
یک شاهکار به تمام معناست!
🔥
ویژگی‌های شگفت‌انگیز این ابزار:
1️⃣
پشتیبانی همه‌جانبه:
تبدیل فایل‌های PDF، Word، Excel، PowerPoint و حتی اسناد اسکن‌شده به متن خالص و بدون به هم ریختگی.
2️⃣
سرعت پردازش خیره‌کننده:
می‌تواند یک فایل PDF دویست صفحه‌ای را در کمتر از ۱.۵ دقیقه پردازش کرده و متن آن را استخراج کند!
3️⃣
اجرای کاملاً محلی (Local):
بدون نیاز به اینترنت و سرورهای ابری روی کامپیوتر خودتان اجرا می‌شود که برای حفظ حریم خصوصی فایل‌های حساس بی‌نظیر است.
4️⃣
بهترین دوست هوش مصنوعی:
پشتیبانی از پردازش گروهی فایل‌ها (Batch) و قابلیت ادغام و همگام‌سازی بی‌نقص با ایجنت‌های هوش مصنوعی مانند
Claude
،
Cursor
و سایر LLMها.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#MinerU
#PDFExtractor
#OCR
#AI
#Claude
#Cursor
#OpenSource
#Github
#Tools
#RAG
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/6562" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHmheYtldWd-O7vkYB8qWVfZ7RzmHN9HzG0D8BtINzeujmtGAMf7iE9hDedDAxJuRINpqonKOTpueEjF622hiCkdlYdu4qByESbmIobDR9y8A_3wQ6BlgXe36gwdsWeY_X9vxcCzi0tHURGrTLfPUBmfj6g4UaQKrbdvWWGfC8HCQfoZyycMkj2BhSh-q2ACO6TN13PuQWeFSwXlroLxLIXxd-iJhOBQmddiLL0km2umd7lGZl5pDAfiUz0pZaHL4kmGgzUL3l30NbcRBTT07IWTkVeQEt1qxsWHL6_EbeeZTbjhsVSZSQ_9Vw-72yiKwVg5QJxb300V8L4R5vqQ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Popit Music: ساخت موسیقی با هوش مصنوعی و مالکیت کامل اثر
🎵
✨
قابلیت‌ها:
•
🔹
انتخاب ژانر و حالت برای تولید سریع ترک
•
⚡
ورود خودکار به پلی‌لیست و رقابت با آثار دیگر
•
🛠️
مالکیت کامل حقوق موسیقی متعلق به شماست
•
📦
دو بار تولید رایگان برای شروع
🌐
Site
#AI
#Music
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6561" target="_blank">📅 13:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚀
معرفی droidMirroring-mac؛ تجربه اکوسیستم اپل برای کاربران اندروید در مک!
📱
💻
✨
اگر از گوشی اندرویدی استفاده می‌کنید اما کامپیوتر شما Mac (سیستم‌عامل macOS) است، احتمالاً همیشه حسرت قابلیت یکپارچگی عمیق اکوسیستم اپل (مثل iPhone Mirroring و Handoff) را خورده‌اید. پروژه جدید و متن‌باز
droidMirroring-mac
دقیقاً برای حل همین مشکل و پر کردن این خلأ توسعه یافته است!
🔥
ویژگی‌های جذاب این ابزار:
1️⃣
انعکاس صفحه (Screen Mirroring):
مشاهده و کنترل کامل گوشی اندرویدی مستقیماً از روی صفحه نمایش مک (دقیقاً شبیه به قابلیت جذاب iPhone Mirroring در نسخه‌های جدید macOS).
2️⃣
کلیپ‌بورد مشترک (Universal Clipboard):
همگام‌سازی بی‌وقفه کلیپ‌بورد بین گوشی و مک؛ متنی را در اندروید کپی کنید و در مک Paste کنید (و بالعکس).
3️⃣
رایگان و متن‌باز:
این پروژه کاملاً Open-Source است و بدون نیاز به خرید اشتراک یا برنامه‌های تجاری گران‌قیمت، ارتباطی عمیق بین دو اکوسیستم متفاوت ایجاد می‌کند.
اگر به تازگی از آیفون به اندروید مهاجرت کرده‌اید ولی نمی‌خواهید راحتیِ کار با مک را از دست بدهید، این پروژه گیت‌هابی یک معجزه برای شماست!
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Android
#macOS
#ScreenMirroring
#Productivity
#OpenSource
#Github
#Tools
#Handoff
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6560" target="_blank">📅 08:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6559">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYwVVaxqt9xotZNYbf3aZkaqHoZkJBeYszMtJ9mU3FT5CSLWc3fBL93GStq8ebRnRzLhueBFnNi3pAX5zuTwuP9B_V25adF9oPAlTNXodfi4C_N741zxCXarezb1Irzd5F6_RlFQ6bCOMtUjo6YOBGFWJFxLkk1imWG75m6worMxMFwyH3KkkALB7kokHSH4hc3fmBcXRgWCULBlmRak5BqzV7FUX2ePLg7CtuviNRy-S4tPUtGUYN7i-zdruuO4BoEuTIHkSTL8RnWib2jRnq5nNmuIverw5aMbDMU9wc_Q9Sry0vFYZZ8rAf1AR6QsW-fLjtevqgEOA9H0UuWb3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">> توسعه‌دهنده‌ای با نام مستعار slqnt نسخه وب بازی افسانه‌ای Half-Life 2 را معرفی کرد.
اکنون می‌توانید این شوتر افسانه‌ای را مستقیماً در مرورگر اجرا کنید، بدون نیاز به نصب برنامه‌ها یا راه‌اندازها.
بازی پایداری شگفت‌انگیزی را نشان می‌دهد و کاربران در حال آزمایش پروژه‌هایی مانند
Ravenholm
و
City-17
در مرورگر هستند!
🌐
Site
#HalfLife2
#WebGame
#Gaming
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6559" target="_blank">📅 23:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8491578554.mp4?token=aqXn-hxuINPoRj9ghe78UjuS-XXRa8iAU1hxaRDWBcycqqubKv4d9NdtBoMiLuqnhpagmgQpryx1342kbAOA2OP8WXgiq6PKZoL__f0Egt6TPppZiVxJW2n8b-rTmvy-JMrE7Uw81iazf6F5S2TC0mBKBCeSf-FUJ4YneNrS0dOhlJEoz0__pm6lF_Acm67sRCtzLwF6OA9UQASKTwrgKMXcXBppBwinqi4OadmHbXr3CydX1BzcYWQDdsDVbPeHCW9c8oWH3ijzo_I_7Q3XHPZHbJrsPBt--8KbmRk4ZyLfbf-cPwKWK7hoxa-lojWYztFQu1b9nQpO24Mt08S3VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8491578554.mp4?token=aqXn-hxuINPoRj9ghe78UjuS-XXRa8iAU1hxaRDWBcycqqubKv4d9NdtBoMiLuqnhpagmgQpryx1342kbAOA2OP8WXgiq6PKZoL__f0Egt6TPppZiVxJW2n8b-rTmvy-JMrE7Uw81iazf6F5S2TC0mBKBCeSf-FUJ4YneNrS0dOhlJEoz0__pm6lF_Acm67sRCtzLwF6OA9UQASKTwrgKMXcXBppBwinqi4OadmHbXr3CydX1BzcYWQDdsDVbPeHCW9c8oWH3ijzo_I_7Q3XHPZHbJrsPBt--8KbmRk4ZyLfbf-cPwKWK7hoxa-lojWYztFQu1b9nQpO24Mt08S3VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی افزونه Caveman؛ ابزاری برای کاهش شدید مصرف توکن در هوش مصنوعی!
🧠
✨
اگر زیاد با چت‌بات‌های هوش مصنوعی کار می‌کنید و نگران محدودیت پیام‌ها (Limits) یا هزینه‌های مصرف توکن هستید، افزونه کروم Caveman دقیقاً برای شما ساخته شده است! این افزونه کاربردی با…</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6557" target="_blank">📅 22:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6556">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚀
معرفی افزونه Caveman؛ ابزاری برای کاهش شدید مصرف توکن در هوش مصنوعی!
🧠
✨
اگر زیاد با چت‌بات‌های هوش مصنوعی کار می‌کنید و نگران محدودیت پیام‌ها (Limits) یا هزینه‌های مصرف توکن هستید، افزونه کروم
Caveman
دقیقاً برای شما ساخته شده است! این افزونه کاربردی با بهینه‌سازی کلمات، مصرف توکن را در سرویس‌هایی مثل
ChatGPT
،
Claude
،
Gemini
و سایر مدل‌ها به حداقل می‌رساند.
🔥
این افزونه چطور کار می‌کند و چه ویژگی‌هایی دارد؟
1️⃣
صرفه‌جویی تا ۷۵ درصد:
این ابزار پرامپت‌های شما و پاسخ‌های هوش مصنوعی را به صورت خودکار بازنویسی می‌کند و با حذف کلمات اضافه، مصرف توکن‌های خروجی را تا
۷۵٪
کاهش می‌دهد.
2️⃣
حفظ معنای اصلی:
با وجود کوتاه شدن جملات (شبیه به لحن انسان‌های اولیه!)، پیام اصلی و محتوای علمی/فنی به هیچ وجه از بین نمی‌رود.
3️⃣
پاسخ‌های بدون حاشیه:
به جای خواندن پاراگراف‌های طولانی و خسته‌کننده، هوش مصنوعی را مجبور می‌کند تا جواب‌هایی کاملاً خلاصه، سرراست و پرمحتوا به شما بدهد.
4️⃣
پشتیبانی گسترده:
این افزونه برای تمامی سرویس‌های معروف LLM قابل استفاده است.
💡
نکته کاربردی:
ای
ن ابزار مخصوصاً برای کاربران نسخه‌های رایگان Claude و ChatGPT که زود به سقف محدودیت پیام می‌رسند، یک ترفند طلایی محسوب می‌شود!
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#ChatGPT
#Claude
#Gemini
#ChromeExtension
#Caveman
#PromptEngineering
#Tools
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6556" target="_blank">📅 22:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=JSyl9QOQv--YfMQzLeDaIMiQDJPVUs05_2dc8jiC-3kW8E_NZivBju1QG5DHOeZH0-BqXla1gZbc0-Js66UmdlAA1r7ZAuTuAkn1WmtVJJq1HawZ6eqQ0AckrBVo_Gj8A8Z_X7h3X6UkdVJmIRNsKVTS8zZCYKJmBQA-eX5HqxPNRZUPv2p3-KUB-drjq7QCNf4Q-xWhZo-xdqLLUIxXXyu_apqXjozoEtSxFJV32MbJalQ0oHrgCMHRp2a4gPzWOm5yszFafyhvFIIuMexhMvGqQHUhDCRxaMmnfPnoZoWvfT7Qw4KT3KrwZDtX0AXqTd2a_vBJzOVRsgTM2a7BIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=JSyl9QOQv--YfMQzLeDaIMiQDJPVUs05_2dc8jiC-3kW8E_NZivBju1QG5DHOeZH0-BqXla1gZbc0-Js66UmdlAA1r7ZAuTuAkn1WmtVJJq1HawZ6eqQ0AckrBVo_Gj8A8Z_X7h3X6UkdVJmIRNsKVTS8zZCYKJmBQA-eX5HqxPNRZUPv2p3-KUB-drjq7QCNf4Q-xWhZo-xdqLLUIxXXyu_apqXjozoEtSxFJV32MbJalQ0oHrgCMHRp2a4gPzWOm5yszFafyhvFIIuMexhMvGqQHUhDCRxaMmnfPnoZoWvfT7Qw4KT3KrwZDtX0AXqTd2a_vBJzOVRsgTM2a7BIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎓
ساخت دوره‌های آموزشی شخصی‌سازی شده با Gemini
🚀
✨
قابلیت‌ها:
•
🔹
طراحی مسیر یادگیری بر اساس هدف (مصاحبه، پروژه یا تحصیل)
•
⚡
تولید خودکار ساختار شامل سخنرانی، تصویر و کد نمونه
•
🛠️
شامل آزمون‌های سنجش یادگیری
•
📦
دسترسی رایگان و فوری برای همه کاربران
🌐
Site
#AI
#Education
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6555" target="_blank">📅 21:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6554">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXjE7sl6nGXWaZypZhPrenG98atQImQm65vGdHgznU2wgEoSiJJYwaBApYEBGYht39XbjS7OVDfjhzmo76cUtczciJ4Q5t8yYrI9r3_CuQtZ_GjrGNtJkl2Td8QlVcHQSAyALWk7J7e62HaVbePh910FnsF3o6Hz7eG0xelCWt-6A-Sq0OGw7CC0BQPs2HDs6eMPNlqOYXd3F641eaJYEO8V-EtXf04XkGriQZxmWEA5HF0Dteabc65A5xf78jLrOgwlZV21vvl8iirkZiVe6dfrEjNcT2NJjzlokhzR4aIw5EVoz7KFwSfwWmx9zPLRlx7U6n-3fRY3DFWAwFccPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
ویدیوهای یوتیوب را تا کیفیت 8K و بدون محدودیت دانلود کنید
🚀
✨
قابلیت‌ها:
•
🔹
دانلود ویدیوهای تکی و پلی‌لیست‌های کامل
•
⚡
پشتیبانی از کیفیت 144p تا 8K
•
🎧
خروجی MP4 و MP3
•
🛠️
ذخیره تنظیمات دلخواه کاربر
•
📦
دانلود دسته‌ای با سرعت کامل
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6554" target="_blank">📅 21:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚀
Vibe
ابزار آفلاین تبدیل صوت و ویدیو به متن
🎙
✨
وایب برنامه کراس‌پلتفرم مبتنی بر
OpenAI Whisper
برای پیاده‌سازی متن فایل‌های صوتی و ویدیویی به صورت کاملاً
آفلاین
و با حفظ حریم خصوصی است.
🔥
ویژگی‌ها:
1️⃣
پشتیبانی از زبان‌های متنوع با قابلیت ترجمه به انگلیسی.
2️⃣
خروجی‌های متنوع: زیرنویس (SRT, VTT)، متنی (DOCX, PDF, TXT)، HTML و JSON.
3️⃣
پردازش گروهی، استخراج متن از لینک‌ها و ضبط مستقیم صدا.
4️⃣
بهره‌گیری از GPU برای سرعت بالا و پشتیبانی از CLI.
﻿
⚡️
مشخصات:
* زبان: TypeScript / JavaScript
* پلتفرم: ویندوز، مک، لینوکس
🔗
لینک
🔵
@ArchiveTell
| Bachelor
⚡️
#Vibe
#AI
#OpenAI
#Transcription
#Privacy
─────────────────────────────</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6553" target="_blank">📅 20:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپخش کانفیگ رایگان🔥</strong></div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
:
60GB
🧭
: حداقل 1 دعوت
👥
: 0/60
💾
: 60 GB
⏰
: 5 روز
🟢
فعال</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6552" target="_blank">📅 14:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🌐
دامنه رایگان
eu.cc
با GNAME! (فیلتر شده ظاهرا)
فرصتی عالی برای ثبت دامنه رایگان
eu.cc
که برای ساخت سایت‌های سبک، تست یا پروژه‌های شخصی عالیه!
✨
ویژگی‌ها:
•
🆓
ثبت دامنه رایگان
•
🔄
تمدید رایگان سالانه
•
☁️
پشتیبانی از میزبانی Cloudflare (CF)
•
🎯
هر کاربر تا ۳ دامنه می‌تواند ثبت کند
•
💡
مناسب برای سایت‌های سبک، تست و پروژه‌های کوچک
همین الان دامنه رایگان خودت رو ثبت کن!
👇
🌐
Site
#دامنه_رایگان
#GNAME
#Cloudflare
#وبسایت
#هاستینگ
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6550" target="_blank">📅 14:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚀
معرفی 1Hosts؛ سپر دفاعی پیشرفته شما در برابر تبلیغات و ردیاب‌ها!
🛡
✨
اگر به دنبال یک لایه امنیتی قوی برای مسدودسازی تبلیغات مزاحم، ردیاب‌ها (Trackers) و بدافزارها هستید، پروژه متن‌باز
1Hosts
یکی از بهترین و بهینه‌ترین فیلترهای DNS و لیست‌های مسدودسازی (Blocklists) در گیت‌هاب است. این ابزار از سال ۲۰۱۷ به‌طور مداوم در حال توسعه بوده و با وجود حجم کم، عملکردی بسیار قدرتمندتر از جایگزین‌های سنگین‌تر دارد.
🔥
نسخه‌های موجود در این پروژه:
🟢
نسخه Lite (متعادل):
ایده‌آل برای استفاده روزمره. این نسخه با کمترین میزان خطای مسدودسازی (False Positives)، تجربه‌ای روان از وب‌گردی به شما می‌دهد (نصب کنید و فراموش کنید).
🔴
نسخه Xtra (تهاجمی / Beta):
طراحی‌شده برای کاربرانی که به بالاترین سطح حریم خصوصی نیاز دارند. این نسخه به شدت سخت‌گیر است و هرچند بالاترین سطح امنیت را فراهم می‌کند، اما ممکن است عملکرد برخی سایت‌ها را دچار اختلال کند.
⚙️
پشتیبانی و سازگاری گسترده:
شما می‌توانید لینک‌های 1Hosts را به راحتی در طیف وسیعی از نرم‌افزارها و سرویس‌ها اضافه کنید:
مرورگر و شبکه:
uBlock Origin, AdGuardHome, Pi-hole
اندروید و iOS:
AdAway, Blokada, InviZible Pro, DNSCloak
سرویس‌های DNS:
همگام‌سازی آسان با NextDNS, ControlD و RethinkDNS
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6549" target="_blank">📅 14:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بیایین با عاباس آشنا بشیم
❤️
دیس وگاس و عاباس
😝</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6548" target="_blank">📅 13:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚀
ارتقای رتبه هر سایتی در نتایج جستجو با کمک هوش مصنوعی!
🔝
✨
ابزار جدید و متن‌بازی پیدا کردیم که وب‌سایت شما را به صورت دقیق آنالیز کرده و به شما کمک می‌کند تا جایگاه آن را در نتایج جستجوی گوگل (SEO) بهبود ببخشید. پروژه
open-seo
یک دستیار هوشمند و همه‌کاره برای کارهای سئو است.
🔥
قابلیت‌های کلیدی این ابزار:
1️⃣
**تحلیل خودکار:** سایت شما را بررسی کرده و توصیه‌ها و پیشنهادات عملی برای بهبود سئو ارائه می‌دهد.
2️⃣
**رصد دامنه و رتبه‌ها:** وضعیت سلامت دامنه را بررسی و جایگاه سایت شما را در کلمات کلیدی مختلف ردیابی می‌کند.
3️⃣
**نظارت بر منشن‌ها:** اشاره‌ها و منشن‌های نام برند شما را در موتورهای جستجو زیر نظر می‌گیرد.
4️⃣
**اتصال به ایجنت‌های هوش مصنوعی:** پشتیبانی کامل از اتصال به Claude Code، Codex و سایر ایجنت‌ها از طریق پروتکل **MCP** (Model Context Protocol).
5️⃣
**اتوماسیون سئو:** دارای سناریوهای آماده برای خودکارسازی کارهای تکراری و زمان‌بر سئو.
6️⃣
**راه‌اندازی سریع:** به سادگی و تنها در عرض چند دقیقه از طریق **Docker** اجرا می‌شود.
🔗
لینک مخزن گیت‌هاب برای دانلود و نصب
🔵
@ArchiveTell
| Bachelor
⚡️
#SEO
#AI
#OpenSource
#Docker
#WebDevelopment
#Github
#Tools
#MCP
#SEO_Automation</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6547" target="_blank">📅 12:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ظاهرا Claude Fable برگشته
🔥
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/6546" target="_blank">📅 12:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دوستان دقت کنید
تو گیتهاب پروژه ها میتونن ویروسی باشن
بررسی کنید
متن باز هست ولی نیاز به بررسی دارن پروژه ها
ولی تلاش ما بر اینه که معتبر هارو بذاریم اکثرا</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/6545" target="_blank">📅 10:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔥
🔥
ویژه
ساخت اکانت جیمیل بدون محدودیت سیم کارت، وریفای و ...
(تست نشده)
فقط روی ویندوز
github.com/ShadowHackrs/gmail-account-creator
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/ArchiveTell/6543" target="_blank">📅 09:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ویژه
🔥
🔥
🚀
تبدیل گوشی‌های قدیمی اندروید به سرور لینوکس یا هاب خانه هوشمند!
🐧
📱
اگه تو خونه یه گوشی اندرویدی قدیمی دارید که گوشه‌ای خاک می‌خوره، پروژه
Linux-Android
دقیقاً همون چیزیه که بهش نیاز دارید! این ابزار که به تازگی در گیت‌هاب ترند شده، یک اسکریپت ساده و قدرتمند است که بدون نیاز به روت (Root)، گوشی اندرویدی شما رو از طریق اپلیکیشن Termux به یک دسکتاپ کامل لینوکس یا سرور خانه هوشمند تبدیل می‌کنه.
🔥
امکانات و کاربردهای بی‌نظیر این پروژه:
1️⃣
نصب خودکار و بدون دردسر:
بدون نیاز به دانش فنی پیچیده، فقط با اجرای یک اسکریپت، لینوکس با محیط دسکتاپ دلخواه شما (مثل XFCE، KDE، MATE یا LXQt) نصب میشه.
2️⃣
تبدیل به سرور خانه هوشمند (Home Assistant):
می‌تونید گوشیتون رو به یک هاب مرکزی (Home Assistant Hub) تبدیل کنید تا وسایل هوشمند مثل لامپ‌ها و پریزهای وای‌فای رو کنترل کنه.
3️⃣
پشتیبانی از شتاب‌دهنده گرافیکی (GPU Acceleration):
با استفاده از درایورهای Turnip، گوشی‌های دارای پردازنده اسنپدراگون گرافیک بسیار روانی روی دسکتاپ لینوکس به شما میدن.
4️⃣
نصب ابزارهای کاربردی:
ابزارهایی مثل مرورگر دسکتاپ (Firefox)، پخش‌کننده ویدیو (VLC)، سرور SSH و حتی اجرای برنامه‌های ویندوزی با استفاده از Wine (به‌صورت اختیاری) قابل نصب هستن.
5️⃣
کاملاً ایمن و بدون نیاز به کلود:
تمام پردازش‌ها روی گوشی انجام میشه و نیازی به سرور ابری ندارید.
⚡️
این پروژه برای آموزش لینوکس، توسعه با پایتون و ساخت سرورهای خانگی فوق‌العاده است.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Linux
#Android
#Termux
#HomeAssistant
#OpenSource
#Github
#Python
#Tools
#TechHack</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/6542" target="_blank">📅 01:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚀
آموزش اجرای MiMo Code یک AI و ابزار کد نویسی کاملا رایگان و بی محدودیت
1️⃣
نصب Termux
اگر روی موبایل هستی
اول Termux را نصب کن
📱
2️⃣
دستورات داخل Termux
1) آپدیت Termux
pkg update -y && pkg upgrade -y
2) نصب ابزارهای لازم
pkg install -y proot-distro nano
3) نصب Ubuntu
proot-distro install ubuntu
4) ورود به Ubuntu
proot-distro login ubuntu --user root
3️⃣
دستورات داخل Ubuntu
1) آپدیت Ubuntu
apt update && apt upgrade -y
2) نصب پیش‌نیازها
apt install -y curl bash ca-certificates wget git nano gnupg lsb-release software-properties-common build-essential python3 make g++
3) نصب MiMo Code
curl -fsSL https://mimo.xiaomi.com/install | bash
4) اجرای MiMo Code
در یک پوشه اجرا کنید
مثال :
cd /storage/emulated/0/Download
سپس :
mimo
4️⃣
اگر خواستی بعداً دوباره وارد Ubuntu شوی
proot-distro login ubuntu
5️⃣
اگر MiMo Code را نصب کرده‌ای و فقط می‌خواهی اجراش کنی ، قبلش وارد پوشت شو
mimo
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/6541" target="_blank">📅 23:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWYI93ZPOmcsZ7jbWjiSQpO9uXc2KbphKy4Mwi-W0DxF9-Z29wohwyqRfLOmGTyMWxnVU9eaNlS5tP4yyMZ85NgUEl-8kcVMBahAm0wQSjQPd4GXVg7S66IwTdZ_n2uvlxpHK7cGEMTBg5W_4obqS2UWUMsO35vs7Q3CKgGb5rwsIhC7RfZXimftRXXpxrI3ImBzyGmZ0vyMWrrjZ70ALzBP-7sN8X2T0BIujAxvn4sM5FBpxEvlNnzntT46QxOUQouxfbNu_d2MB_FLHpYHq-tZ-oLfwIWRRCv1LRQ18y73KRoJ6RjOnnx1XT63yZtYxDKMhZBHSUWwPjyA5lLqTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
کتابخونه‌ای به وسعت ۱۱ هزار کتاب!  هوشمندانه جستجو کن و دنیای جدیدی از کتاب‌ها رو کشف کن.
✨
قابلیت‌ها:
•
📖
دسترسی به ۱۱ هزار کتاب با رتبه‌بندی و توصیه‌ها
•
🧠
جستجوی معنایی: «کتابی برای توسعه فردی» یا «متا فیزیک»
•
🔄
مشاهده نسخه‌های مشابه برای هر کتاب
•
🌟
مجموعه‌های پیشنهادی از افراد مشهور
•
📊
جمع‌آوری داده‌ها از کتابخانه‌ها، شبکه‌های اجتماعی و رسانه‌ها
🌐
Site
#کتاب
#کتابخوانی
#معرفی_کتاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/6540" target="_blank">📅 21:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6536">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C5Qac2F1rJ6IbckKu0TSYbCQg25W3MPvzpZy5swiz-9e283li4sFUkzONlR8gzwPRQDZoK4VMaZjG1ZGwUXC1l8L__TN5hCxPn-eUn3TuzgNSXWKNPodaeNGU5AgKcyuEwYpPFPJ79VUV0JHncVoCbHsXHNns8pI34QGwf3x5xqh61LnypIpt0RT5McjECtqT_vEvbp2o_dBy-HKBWcCvvdJ8bA-u9RIyUHUOqeegH9Q15ZXQYyJZwZFrevDNUuLdtWbAi80scRUI1oWXFLUrQLC7vF7oBOguXhpBwkz494t0O8fv3IQ2BVaHHdVxZHUEwoFpuVcvi7xowUjnpuUlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VXLO_Y_hxYCHO4t_z25vQudTO7j42TKAaRVdCH9ZhyRHCbMoHhiQoU_kyJELUqJjxjiE_bPK9-8w_4h8x5STM-Q88kIN9eC4hV80P3BFzmD1JZdE_BLFSgXgHjGg4vog8mWls-p3WdYB3GqMOYTeyTFWM6bU-71xdeK0WKCOraeZbLQL4k8_FyLbYorEwKFXOCMV2s_NJSILGj6aeR8Xdin7OOjZUGlTSHW0RXY7QGvFuNbBE__LfnqeONdA4TI0r0CUYILYD6oMFjBNmlADUf_jB2Ke_tY5kcl5n3AfFV45IzYpF2gQnu4KwddtJ3OCoiZadjVsBLqIeuD55QkOlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UViuLCLhKh5hhXQL578WBrj6UQd5BIRVKbWK3GzH6VWBAB0iW5tM27FCyF9vrC-zSxe13_qizGQjMkUr5bNAFlssPSBVDMtjGfnfQTg_60fBihHoXcmrS44hUL3HKrPTA7PfUKSiuuvLbij_0s-Z3Vdgms4ZQE7zkZffWnGWvGljXQvSFtLJ6KxlwMHBn1UlYMbYMTpbniQo2tx9uBeF758gbDnQREyn9Ro6ydw0Duwn9o2bQOitBedtPLly2GoTwR5Gj1NsYVU5ldrwh1tV5_R7oySwN4KEnciJU9J2Fjkt4qD66sbTIqLBqlGthOWnST2emzCNOV_S5PD84mXP7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MmUToGbdnjBCuuRqRRSkPZ8yVttAUd9RlcwXLmSWeKKaC826hbDx5cVw-yQJf8XFd67Tew7iOeqB5il9IjD1Pnqu3DlU8enXpXFuXshRHgGtV6II19FraUKpn6dlVP6XWFKoirCk1UrkMH-BUf05hjBnvTIzhHRf3oap3nHkXBiPioSN4F9sxdLj4gSuRZXY085-C_QiXuJWRevCQxx4xNE-DFZAdfPOQ8u5OCdLaYafsRhcwlrQWrwQ202jiTTFqFC5ShpiAj5OM79yOvguC5o_En4173Cd7lZINmRUEwDmF3iIRHHZGu0ihlqAHgFzr_mBisQLiQljj_f4DVZ1bA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🍿
نتفلیکس خود را بسازید — یک برنامه رایگان و متن‌باز برای تماشای فیلم‌ها، سریال‌ها و انیمه بدون تبلیغات مزاحم پیدا کردیم.
🔹
بسیار سریع‌تر از اکثر سرویس‌های مرورگر کار می‌کند.
🔹
امکان دانلود محتوا مستقیماً روی دستگاه را فراهم می‌کند.
🔹
از زیرنویس‌های فارسی پشتیبانی می‌کند.
🔹
بر اساس علایق شما توصیه‌ها و مجموعه‌هایی را ایجاد می‌کند.
🔹
برای راه‌اندازی فقط به یک توکن رایگان
TMDB
نیاز دارید که در چند دقیقه تهیه می‌شود.
🌐
GitHub
#OpenSource
#Streaming
#Entertainment
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/6536" target="_blank">📅 20:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">worker.js</div>
  <div class="tg-doc-extra">23.5 KB</div>
</div>
<a href="https://t.me/ArchiveTell/6535" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سورس کد ربات تلگرامی برای چت با هوش مصنوعی بر بستر کلودفلر
🌐
ویژگی‌ها:
- گفتگو با مدل‌های GLM 5.2، Kimi k2.7، Gemma 4، GPT 4 و Llama
💬
- تولید تصویر با مدل‌های Lucid origin و Flux 2
🖼️
- تبدیل صدا و موزیک به متن با مدل whisper-large-v3-turbo
🎤
راهنمای اجرای این سورس در بخش کامنت های این پست ارائه شده است
👇
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6535" target="_blank">📅 18:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚀
معرفی Save to Yaps؛ ابزاری برای ذخیره هوشمند و خصوصی مطالب وب!
🌐
✨
اگر از آن دسته افرادی هستید که همیشه ده‌ها تب (Tab) باز در مرورگر خود دارید، یا لینک‌های مهم را برای خود ایمیل می‌کنید و دیگر هرگز سراغشان نمی‌روید، افزونه
Save to Yaps
دقیقاً همان راهکاری است که نیاز دارید!
این افزونه یک "Web Clipper" فوق‌العاده است که هر صفحه وب را به یک یادداشت Markdown تمیز و خصوصی در کامپیوتر شخصی شما تبدیل می‌کند.
🔥
چرا Save to Yaps متفاوت است؟
*
تبدیل هوشمند محتوا:
مقالات را از شر تبلیغات، منوها، بنرها و پاپ‌آپ‌ها پاکسازی کرده و فقط متن اصلی را به عنوان یک یادداشت تمیز ذخیره می‌کند.
*
ذخیره سریع تصاویر:
با قابلیت Hover-to-save (نگه داشتن موس روی تصویر)، می‌توانید عکس‌ها را به سادگی به یادداشت‌های خود اضافه کنید.
*
حریم خصوصی مطلق (Private by Design):
برخلاف سرویس‌هایی مثل Pocket یا Evernote، در این ابزار هیچ اطلاعاتی به سرورهای ابری ارسال نمی‌شود. همه چیز به صورت محلی (Local) روی کامپیوتر شما ذخیره می‌شود.
*
کارکرد آفلاین:
حتی زمانی که به اینترنت دسترسی ندارید، می‌توانید یادداشت‌های خود را ذخیره و مدیریت کنید.
*
سازگاری:
روی تمام مرورگرهای مبتنی بر کرومیوم از جمله کروم، اج، بریو و آرک قابل نصب است.
💡
نحوه استفاده:
برای شروع، کافی است اپلیکیشن دسکتاپ رایگان Yaps (برای مک یا ویندوز) را از
اینجا
دریافت کنید، افزونه را روی مرورگر نصب کرده و با یک کلیک، مطالب مهم را به "Second Brain" یا همان پایگاه دانش شخصی خود منتقل کنید.
🔵
@ArchiveTell
| Bachelor
⚡️
#Yaps
#WebClipper
#Privacy
#Productivity
#Markdown
#KnowledgeManagement
#TechTools</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6534" target="_blank">📅 17:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwySkjFWAFpqqxscKnWQKrn-jQhA-k2XQUlf4r6SQzHBYBXBEcN3ljiOeBvBZsK70Ftg_ZHfflEJ1daOKWEFXAsoznw8KsziZO4Z0eoahK8cfsQKEs_h0mh6HFyai1l3kAPqfa6Pj4CA6hZm2Mnr9Ab9f5Q6Sv3SaDBNiyq5a7ngefleYGVN4YN9nnXu28_7dVkm9rjQtXIT7BKDhPbdLK4bwlUcoijzkkYA36uB82QKW554t2bPTDERX-_bxMZHoW17kToncGGbLO68qquT2fZNLbe3qbWiTwQ9VJQb2EY2SmhuLxUrg0yK31VlRxsJ1r9jK5TRlEEsDuGoTyUJFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش در سطح MIT و هاروارد رو رایگان تجربه کن!
🎓
بیش از ۱۷۰۰ دوره از بهترین دانشگاه‌های جهان حالا در دسترس شماست.
✨
قابلیت‌ها:
•
🔹
دسترسی رایگان به دوره‌های برتر جهانی
•
📚
شامل برنامه‌نویسی، ریاضیات، طراحی، کسب‌وکار، فلسفه و علوم دیگر
•
📹
محتوای کامل: ویدئو، جزوه، تمرین و امتحان
•
💡
مناسب برای یادگیری از صفر تا پیشرفته
•
🔸
یکی از بزرگترین آرشیوهای باز آموزشی
🌐
Site
#Education
#FreeCourses
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6533" target="_blank">📅 16:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eWi-6Pzi3viD2T-fU9djdBkSlSQrW96VaOkLuyOh8wZwxX8sh51x4j7gGnGD5LFw_ZmRU3f4MpYgxwKHCxUkM0RnZRhwsAI9Kp1xy6CMWpTRKR5HbauOT2bJjKi7KgHofav5QrHYNrXBxr-ihNmI_q4vBTt4zypB7GKeL41_ocIgYhUophNVuM1R3lnH3uHqSMyjqaCFPBEWaPc3meF1bPfrxKMn6F10leZPiPGGBiCB_OqmNWfjnqNvJfCxgN85rGUXJ8g9gk85JVEQcxp-H7Y38hYQNK7cIUapzWTulen3HlYyAGeJzhr_7RO90XuttX07JODcThV1OAR3r5oE2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GY_q4eSwZerdqkdbgPv2vYHnUCrFLFzbYhX0_59p4VZb1lzzPRgx3eME14e_ZFPOdqVv7Gw1o3UopZUessdEoWEZTJQHlVf6DXvF6HA5DkyvawTu2X_P8C5fgP4NAkFUAymf0JluO6RquztoAYjJDyrGfLCzXL_Kx8SSJpXG3gW0yfYqRv-M6SlMIX-lPqY45_ZsWJVHYje75MnhEKf1v4zNth7SdgQYiJJxc8IiSokckneZgohUiDZAJPQcbOqcaci-QyrZtipAnroUuFehCbxL-v2_7dfYNQZoPShch3pbiQj6kc0nlHJyBTNn7tInTVTni8Xd2F89-miFQdlyFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E77t8uboPWa0E2FtyuRaUZMQlQNFy0yjUd_yrZi_jhWdh9eQ4Cc9awqyU8cti8kLOOf2nG1LqkSQIMWA48vP3w2qgaBHYOPQSN9kG0JDJJybnFKqUdgGbI17hHoiPV74Tm-sWf539VaxmEUeeOA9LK7bhV3Pl8kG5g3JOMPQf3XcJ-kC8fP4AUxB-OeGVMB_EqNDJpb6T9ArrpS60gj4m-JyVl7ZmQw1kraL01M6b7q93PCpVWij37Nsl3zHUsVNhqCLtcH_RavGK2dcl_LJSpm_e3suh2wWBqrapMLdtC3w4_CUXCOJtI5qwdJlw4oADxOQAb_ixXPivvds0llQBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jTkoW-o-gYHxYIJgkqSogtaMIyffpVhQCOHm0eSGUEthw5hKdP3WF2tez9UCaDIX5Tg1gGAJ2s-az9-TaPfUefi3fe1Gm2Cb0MEBuAu2n7B-P6h-Mmm4rEJXG-b-oUfuzruvf1NgqAGhXZRGhi-W50vCuj2fU5roVaE7xJNbpOh0dd679qiJl5tWqTerXtg8cVZ2C6vujtN-cr5R0hXjOp466nszt8EOcIDiW5wwXMfPl9NpKL1UCr6ba0YaSbM9LMDgUEIZh-wTiOKfgtBrZNNlxVs5YIG3o6PyScVHbvEOhw56vMqPKS0nF8HnhHafG46KUnVrCvp81cz_1hmX6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IBby4xSfBcdMQJnzq0nGcDKPzkwWzNeUWHcGp2x8WSMzOmC6QLWYZmWNBvrDW-uyVKwAXR0Vs29AKRQikavmn89FX80G1iB3n4lzOww3ZLYT6GH6XcZVimzKOAFbXjErF3aNbT9t6vWxD3Dkn-uTwyNg-jf9LCyXS0pl-s13Tt2sQdlfv8U8-1WEnzA2wknIYY0tB7AUohMaSQuN8U838_fH054SYzJ4VSI2kaPI5yaioczqGBbdQOuzH0vS8adrtKu0nZaP0U4Wz4yDKwpYCS6vmB-T4Laq75hZsCY6OyIxHcoQmCn0VpNUj1kvaoNm635awhas0ybRLgpjWemEZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYkH3D6TeVaRktFTL0qni7Fu_z7aRCUlG26rnzH_D32-hgEA1jnAzpghqoNBDukHE7EI-2nOP0Fx7MNIjwvbiQGBx357FynPfYC7SRsoZpSYtotufe_hmYqKJJLntKEqKbQTSli1W0cJ6MtG1UAOV5hDICEKq1--S2eLqFGctNJ3QzZfU1pmxrSGj7_YGduLUmfp_aEwN5ZU-UkgCqKlghhU1ZnOhNhLntIgK0L_yBE5aBiNWAALLHf_lHNasB6gVkDt_Bu3biH6tASDA2Sxdg7qcrR6twFPPisgebh0NuhQ-xlJwEwzUI30R-o4UAKIgPW_sfCtxvclphzUlLHFgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر منتشر شده از بازی GTA VI</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6527" target="_blank">📅 14:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6526">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AI2NrcGiQl3Tk88SqcZEZNxeyeUyiv8zWJPgfLD0BzmFluFqB8PLQnGA9FatEDLH2DcFWdy8HCS7Giqnf2Y6NFZX7kZhiAKw1ObT8S9RE7_aVX0N5ysJKLjy7lujVeh0m6NAojXgCFeuCrisCMWmQQd24Af7lXc0WPzcq_cGd-La0SIbhV51QPTRzVleV7b2rbcCNqdvE6XzsT4lWGIHJKznIaW3W50smmW8CwDc0x8lzCFqjiz5dWmX9vI84XQp3OzHylB3wJR-43-S_MVGIBlNXKVtY7rbPm9-zA5jNkQkiA__vzHXhdjSXilL7KqTNTaya_bESzXz1h562fuWdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر تورنتی که بخوای رو پیدا کن!  با "EXT Torrents"، یک موتور جستجوی قدرتمند و رایگان، به دنیایی از محتوا دسترسی پیدا کنید.
✨
قابلیت‌ها:
•
🔹
آرشیو عظیمی از فیلم، سریال، انیمه، موسیقی، بازی و نرم‌افزار
•
⚡
جستجوی سریع و دقیق با کلمات کلیدی
•
📂
مرور دسته‌بندی شده و رتبه‌بندی محبوب
•
🔗
پشتیبانی از کپی مستقیم مگنت و دانلود فایل تورنت
•
🆓
رابط کاربری ساده و بدون نیاز به ثبت‌نام
🌐
Site
#Torrent
#SearchEngine
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6526" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6525">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚀
معرفی winpodx؛ اجرای اپلیکیشن‌های ویندوز در کانتینرهای لینوکس!
🐧
✨
اگر نیاز دارید برنامه‌های ویندوزی را در محیط لینوکس اجرا کنید اما نمی‌خواهید درگیر سنگینی و کندی ماشین‌های مجازی (VM) شوید،
winpodx
راه‌حل جایگزین و هوشمندانه شماست. این ابزار به شما اجازه می‌دهد برنامه‌های ویندوزی را درون کانتینرهای ایزوله در لینوکس اجرا کنید.
🔥
ویژگی‌های کلیدی:
*
بدون نیاز به ماشین مجازی:
اجرای مستقیم و ایزوله در کانتینر با عملکرد بسیار بالاتر.
*
پشتیبانی منعطف:
اجرای نسخه‌های مختلف ویندوز در محیط کانتینری.
*
توسعه‌یافته با Python:
ابزاری سبک و قابل سفارشی‌سازی برای سناریوهای مختلف.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#winpodx
#Linux
#Windows
#Docker
#Python
#Containers
#DevOps
#OpenSource</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6525" target="_blank">📅 11:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚀
معرفی AI Website Cloner Template
این پروژه یک قالب حرفه‌ای برای
تبدیل هر وب‌سایتی به کد مدرن (Next.js 16 + React 19 + Tailwind)
با کمک ایجنت‌های هوش مصنوعی است.
قابلیت‌ها:
*
مهندسی معکوس هوشمند:
تحلیل سایت، استخراج توکن‌های طراحی (رنگ، فونت) و ساخت کامپوننت‌های دقیق.
*
سازگاری بالا:
پشتیبانی از ایجنت‌های معروف مثل Claude Code، Cursor، Windsurf و Gemini.
*
تکنولوژی روز:
خروجی تمیز با Tailwind CSS v4 و استانداردهای strict TypeScript.
کاربرد:
بازسازی پروژه‌های قدیمی خود یا یادگیری نحوه ساخت کامپوننت‌های پیچیده وب‌سایت‌های حرفه‌ای.
🔗
مشاهده در گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6524" target="_blank">📅 07:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡 یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده. این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway  را فراهم می‌کند. از طریق خود ربات می‌توانید:
✅
پنل موردنظر…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6523" target="_blank">📅 00:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=Hxkeg_TP4tirDGNoN6Fzq3cGpgSUyfvj0tKyFVavV80ucrzkCpyUNJ6WAdA30KNtVlz5mrYT6zMtEjBapdROYBxfzI-J4hdzQopwc1weIg-dGjGr-Y3HMsophQ8YALxZZYlwNYuYlAssBiMv94xh5y3xMH2F5crDTWrXyYVmGzBhqTejT8VI1k2k_AfLaogegmMNytriOWr6LMg_oZ32Zq1V1SfN6wU5uIVaBdw06fSrWvareKf4Y4-fUd8C5u2IDcEsaWeLjwud5X7A8XEQ-Ga2ulGW7jo1DLAh8uYz-uHgm-eRzSHh51N-m3X7-BSur3GxtrQoFXu1f0GGSMeKfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=Hxkeg_TP4tirDGNoN6Fzq3cGpgSUyfvj0tKyFVavV80ucrzkCpyUNJ6WAdA30KNtVlz5mrYT6zMtEjBapdROYBxfzI-J4hdzQopwc1weIg-dGjGr-Y3HMsophQ8YALxZZYlwNYuYlAssBiMv94xh5y3xMH2F5crDTWrXyYVmGzBhqTejT8VI1k2k_AfLaogegmMNytriOWr6LMg_oZ32Zq1V1SfN6wU5uIVaBdw06fSrWvareKf4Y4-fUd8C5u2IDcEsaWeLjwud5X7A8XEQ-Ga2ulGW7jo1DLAh8uYz-uHgm-eRzSHh51N-m3X7-BSur3GxtrQoFXu1f0GGSMeKfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش ثبت دامنه برای رندر
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/6522" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡
یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده.
این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway
را فراهم می‌کند.
از طریق خود ربات می‌توانید:
✅
پنل موردنظر خود را بسازید
✅
مصرف و وضعیت منابع را مشاهده کنید
✅
دامنه شخصی خود را برای پروژه متصل کنید
✅
آی‌پی تمیز را مستقیماً از طریق ربات دریافت کنید
هدف 𝗥𝗘𝗡 ایجاد یک روند ساده‌تر و خودکار برای مدیریت پروژه‌ها و سرویس‌هاست.
🤖
ربات
💻
سورس پروژه
━━━━━━━━━━━━━━
👨‍💻
توسعه داده شده توسط 𝗔𝘀𝘀𝗔
دوستان اضافه کنم اگر رندر شما ساسپند شد اکانت رو حذف کنید و دوباره با همون ایمیل یا گیت هابی که داشتین ثبت نام کنین مصرفتون ریست میشه
برای حمایت از پروژه star بدین
❤️
(در گیتهاب ترجیحا
😂
)
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6521" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7v5VdPaUHYUG91DG5XVOBwV7AwaTJERLBGf59CMh7ZlUfi-rnmpKhRNvLMXGmIn_IrSzsAjXSAAIx-4FP2vcViAGP_-GnC0wIssyd0_UiFQSSIt59m0RuqmYezKLLeL4BaVKAvzjz1IL7cig2eblEWUDONejsMW5oCCw9bqVIQDvDdo7Jv1UbasavZ2avJBsbi9E79cw9E91BeWn4Bx8pzw8oa6CVrlf-rNtxwlsL29X1p6VYlyX1Bqoj1sxG4dNF3gmx3JMxVEJRNiNuWdSmrFP7WOKppDf8oI-4wPqDnn5xQZpLdye12bqoTln947nvnYkCQFURgVdZ0yJaVG3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی shadPS4؛ سریع‌ترین شبیه‌ساز کنسول پلی‌استیشن ۴ برای کامپیوتر!
🎮
✨
اگر به دنبال اجرای بازی‌های PS4 روی سیستم خود هستید، پروژه
shadPS4
یکی از فعال‌ترین و سریع‌ترین پروژه‌های متن‌باز (Open-Source) در دنیای شبیه‌سازی است که با زبان C++ نوشته شده و با سرعت خیره‌کننده‌ای در حال پیشرفت است.
🔥
چرا shadPS4 در حال حاضر ترند شده است؟
1️⃣
توسعه روزانه:
این شبیه‌ساز تقریباً هر روز آپدیت می‌شود و بیلد‌های جدیدی برای سازگاری با بازی‌های بیشتر منتشر می‌کند.
2️⃣
پشتیبانی چندپلتفرمی:
به راحتی روی
ویندوز
،
لینوکس
و
macOS
اجرا می‌شود.
3️⃣
رشد سریع:
در تاریخ اخیر شبیه‌سازهای کنسول، shadPS4 سریع‌ترین روند بلوغ و افزایش سازگاری با بازی‌های بزرگ (Major Titles) را داشته است.
4️⃣
جامعه کاربری فعال:
با بیش از ۳۱ هزار ستاره در گیت‌هاب، این پروژه به یکی از محبوب‌ترین ابزارهای گیمینگ در اکوسیستم متن‌باز تبدیل شده است.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#PS4
#Emulator
#Gaming
#OpenSource
#Github
#Cplusplus
#RetroGaming</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6518" target="_blank">📅 21:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚀
معرفی OpenSERP؛ دسترسی رایگان به API موتورهای جستجو (جایگزین SerpAPI)!
🌐
✨
اگه برای پروژه‌های هوش مصنوعی، سئو (SEO) یا اتوماسیون خودتون به دیتای موتورهای جستجو نیاز دارید و نمی‌خواید هزینه‌های سنگین برای خرید API بپردازید، ابزار
OpenSERP
دقیقاً همون چیزیه که دنبالشید! این پروژه متن‌باز (Open-Source) دسترسی کاملاً رایگان به نتایج Google, Yandex, Bing, Baidu, DuckDuckGo و Ecosia رو از طریق API فراهم می‌کنه.
🔥
چرا این ابزار فوق‌العاده است؟
1️⃣
بهترین جایگزین سلف‌هاست:
یک جایگزین رایگان و قدرتمند (Self-Hosted) برای سرویس‌های پولی و معروفی مثل SerpAPI, DataForSEO و Tavily.
2️⃣
خروجی مارک‌داون (Markdown):
قابلیت استخراج دیتا از سایت‌ها و نمایش نتایج جستجو به فرمت Markdown (که برای پروژه‌های RAG، ایجنت‌های هوش مصنوعی و LLMها یک ویژگی طلایی محسوب می‌شه).
3️⃣
جستجوی ترکیبی (Megasearch):
این قابلیت به شما اجازه می‌ده تا یک کوئری رو به‌طور همزمان در تمام موتورهای جستجو سرچ کنید و نتایج تجمیع‌شده رو تحویل بگیرید.
4️⃣
کاربردی برای همه:
ابزاری بی‌نظیر برای متخصصین سئو، توسعه‌دهندگان، برنامه‌نویسان وب‌اسکریپینگ و فعالان حوزه هوش مصنوعی.
⚙️
این ابزار رو هم می‌تونید خودتون هاست کنید و هم از نسخه تحت وب و آماده‌ی اون استفاده کنید.
🔗
لینک مخزن گیت‌هاب
🔗
نسخه آماده و تحت وب
🔵
@ArchiveTell
| Bachelor
⚡️
#OpenSERP
#API
#SEO
#WebScraping
#LLM
#RAG
#OpenSource
#Github
#Tools</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6516" target="_blank">📅 20:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6515">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚀
آموزش دریافت یک ماه اشتراک رایگان Duolingo Super!
🦉
✨
اگه از برنامه دولینگو برای یادگیری زبان استفاده می‌کنید، الان می‌تونید با یه ترفند خیلی ساده و جذاب، یک ماه اشتراک پریمیوم (Super) این برنامه رو کاملاً رایگان دریافت کنید و از شر تبلیغات و محدودیت‌های جون (Heart) خلاص بشید!
🔥
مراحل دریافت اشتراک:
1️⃣
نصب اپلیکیشن:
ابتدا
اپلیکیشن Webtoon
را دانلود کرده و یک اکانت جدید در آن بسازید.
2️⃣
جستجو:
در نوار جستجوی برنامه، عبارت
Duo Leveling
را سرچ کنید (این کمیک مشترک دولینگو و وبتون است).
3️⃣
اسکرول کردن:
سه قسمت (اپیزود) از این کمیک را باز کنید. (اصلاً نیازی به خواندن نیست، فقط کافیه صفحات را تا انتها به پایین اسکرول کنید!).
4️⃣
دریافت کد:
بلافاصله بعد از انجام این کار، یک کد فعال‌سازی رایگان Duolingo Super به شما داده می‌شود.
👏
5️⃣
فعال‌سازی:
حالا وارد لینک زیر بشید، وارد اکانت دولینگوی خودتون بشید و کد را وارد (Redeem) کنید:
🔗
ورود
🎉
تبریک! اشتراک یک‌ماهه شما فعال شد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Duolingo
#DuolingoSuper
#Webtoon
#FreeAccount
#LanguageLearning
#Tricks
#Education</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6515" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚀
تبدیل عکس شما به مینی‌فیگور واقعی لگو (LEGO) با هوش مصنوعی!
🧱
✨
دوست دارید بدانید اگر یک کاراکتر لگو بودید چه شکلی می‌شدید؟ با استفاده از تولیدکننده‌های تصویر هوش مصنوعی و یک پرامپت (دستور) مهندسی‌شده، می‌توانید هر عکسی را به یک رندر سه‌بعدی و فوق‌العاده جذاب از مینی‌فیگور لگو تبدیل کنید!
🔥
ویژگی‌های این استایل جذاب:
1️⃣
حفظ هویت و جزئیات:
لباس‌ها، مدل مو، رنگ مو، حالت چهره و حتی اکسسوری‌ها کاملاً شبیه عکس اصلی شما بازسازی می‌شوند.
2️⃣
رندر فوق‌واقع‌گرایانه (Photorealistic):
اعمال بافت پلاستیک براق لگو، درزهای قالب‌گیری و نورپردازی استودیویی که باعث می‌شود تصویر کاملاً شبیه یک اسباب‌بازی واقعی به نظر برسد.
3️⃣
رعایت دقیق تناسبات:
سر استوانه‌ای، دست‌های گیره‌ای کلاسیک و بدن بلوکی شکلِ استاندارد لگو.
👇
پرامپت (دستور) برای استفاده در Midjourney یا DALL-E 3:
کافی است عکس خود را در هوش مصنوعی آپلود کنید و دستور زیر را به آن بدهید:
>
Turn the person in the uploaded image into a realistic LEGO minifigure, preserving their individuality, clothing, hairstyle, hair color, facial expression, and accessories as much as possible. The character must match the proportions of a LEGO minifigure: a cylindrical head, simple facial features, a blocky torso with printed clothing details, standard LEGO arms and hands, and a molded plastic hairpiece. Use realistic LEGO plastic texture with a glossy sheen, molded seams, and studio lighting. Plain white background, full body photorealistic 3D render from head to toe.
💡
نکته کاربردی:
این ترفند برای ساخت عکس پروفایل‌های بامزه، آواتارهای تیمی و پست‌های خلاقانه شبکه‌های اجتماعی بی‌نظیر است!
🔵
@ArchiveTell
| Bachelor
⚡️
#LEGO
#AI
#Midjourney
#DALLE3
#Prompt
#PromptEngineering
#3DRender
#Avatar</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6514" target="_blank">📅 18:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkxQ23Da-Dm1teo1sm2UhmwSbxQh6O4oQ5TAF49aXVLY7RRTJa_xxXJzbzppnsKifz4yvBa4UDIOkFoeWdhS75wqw6A9sfpJv4QREP4oK2ff9D6dxYmvQHB2pSPORrgdCCEnvJv3noGYrqmWmsES8ppR1cIOZYKn1CdjKNCHE6HVQ2IUVsQtkL_L_mKtC_MIdZSRWWogRqCPEBre_qfuNRFjvPYJzTZfJz6cZwUAcauRK4XN91FujBDT8ZHLQqXH_57j2_g1Y-69PRrml_fkdwcS29LsyrmfRo24K11FQ_aKCWyl7aw8n68IESdvAttRY4Z0JtzSKGVrXQHoNBIh3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل‌های هوش مصنوعی پریمیوم با مرورگر tabbit
🤯
ChatGPT 5.5 Pro
Gemini 3.5 Flash
Claude Opus 4.8
و بیشتر
در دسترس برای
macOS
و
ویندوز
مرورگر را نصب کنید و استفاده از جدیدترین مدل‌های هوش مصنوعی را به صورت رایگان شروع کنید!
🌐
Site
#Ai
#ChatGPT
#Gemini
#Claude
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6513" target="_blank">📅 17:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCtwkz4y0dNMGW2fwypa_PRi6_znhFhjbrDw-j_9wIegQZ6TU63J-4kKIkOygjlKvehRXQgzOerTIcWqGzxK9Dq0Up9qYuiHipSa59t3EY2x_oduM38Fgvte8QKh-lMDq7Ppmco2h0k9_tlAOKRRqAnvPs6DsYmaMjmJ4Vpg95YucjWntXBMKLJPnKnsTy0rHuvQ2i9-XfEkG7RAmgzRQxnMN3igyyJU8lRha2zIrJu7TJKvLo_QAs_cLQvdOP8CCqoH74kJ3jk1gS7vR1jcZ0ASbyJV8sHHV8pHi6BHtkQg53or7hr0n8TYGSHSni1fAGgQZwOxd6e537YLbo3TPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چینی‌ها مدل Qwythos-9B-Claude-Mythos-5 را معرفی کردند که بر پایه Qwen3.5-9B است و قابلیت پردازش ۱ میلیون توکن را دارد!
🤯
✨
قابلیت‌ها:
•
🧠
تنظیم دقیق بر اساس ترکیبی از Claude Mythos و Claude Fable.
•
📚
پنجره متنی گسترده تا ۱,۰۰۰,۰۰۰ توکن!
•
🌐
انتشار کاملاً متن‌باز
•
✍️
همه‌کاره برای کار با متن، کد و اسناد طولانی.
🌐
Site
#OpenSource
#AI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6512" target="_blank">📅 17:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lufbum7XRAgBTHSa18oqeSj50Q7ValyLlEFQjntf6wo3e0SOs6QP2_tTKhpub4fbE5lLyMByBZyx0DwIywuzn9sxXVSCcOFjq-yrFvO77mI2_dfwlU2GdT-w5RqXT-73MQjVQkkC7AXsBBWt_15aV4YNoN6OzFUhP5mlBtBrGkJke1SCjMqsCcal3As7HP3fz69QmKUsFxKl2ylb1SQY46DXu6s19FHy-GvpBCSJ_VP48bKe1DjGKgDdFNU1YX51Yg_ExEBfw675LQ1LDfB15SZA0bbwmwFGkWlXbEQ8zOYe1-mo28oPPdudEWChFvUGu85LhW9DtBPCNSsefa11xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
Consensus — جستجو در مقالات علمی
موتور جستجویی برای ۲۰۰ میلیون مقاله علمی. سوال خود را وارد می‌کنید و مجموعه‌ای از تحقیقات مرتبط و خلاصه نتایج آن‌ها را دریافت می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6511" target="_blank">📅 12:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=eQJsxM7smtIVBjgeVR6Jco-So5KwUWRCKWoKVJUPrGJyG2RUHPszMNKIXqIyBg6k5RJHVbSsSBS7z7RHa-1Vx1gS7TLVLlGfA3_97ib5IVLBfQo1stTvJ0DznnrywVfsYYf4cDhA90QjrmXttctBJhBcnf_IQ_OhZnqxPWojgjanki7u5uVhmgKoQLexO9NPxrZpRFVTsSBl_nmXf7F7m65V0rMgciHUmrJ7lAbjcbD1rWDd0uQEIghIY5DJYJ9TctrlxlPGg3aB3JjgJZQHdKG77XX8kclh2TgxF4eN-W2Pq30pwZihLLEu5Z91QO2vK1K3SbUyTJgTgBGv1vaMfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=eQJsxM7smtIVBjgeVR6Jco-So5KwUWRCKWoKVJUPrGJyG2RUHPszMNKIXqIyBg6k5RJHVbSsSBS7z7RHa-1Vx1gS7TLVLlGfA3_97ib5IVLBfQo1stTvJ0DznnrywVfsYYf4cDhA90QjrmXttctBJhBcnf_IQ_OhZnqxPWojgjanki7u5uVhmgKoQLexO9NPxrZpRFVTsSBl_nmXf7F7m65V0rMgciHUmrJ7lAbjcbD1rWDd0uQEIghIY5DJYJ9TctrlxlPGg3aB3JjgJZQHdKG77XX8kclh2TgxF4eN-W2Pq30pwZihLLEu5Z91QO2vK1K3SbUyTJgTgBGv1vaMfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗿
افزونه Caveman پرامپت‌ها و پاسخ‌های هوش مصنوعی را فشرده می‌کند
به‌طور خودکار کلمات اضافی را از درخواست‌ها و پاسخ‌ها حذف می‌کند و در عین حال معنی را حفظ می‌کند. با ChatGPT، Claude و Gemini کار می‌کند.
نویسنده ادعا می‌کند که این افزونه می‌تواند مصرف توکن‌ها را تا ۷۵٪ کاهش دهد. ایده ساده است: کلمات کمتر یعنی هزینه کمتر، و معنی باقی می‌ماند.
🌐
افزونه
#Caveman
#ChatGPT
#Gemini
#Claude
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6510" target="_blank">📅 11:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚀
معرفی Firecrawl؛ قدرتمندترین API برای جستجو، استخراج و تعامل با وب در مقیاس بزرگ!
🔥
✨
اگه توسعه‌دهنده، محقق هوش مصنوعی یا دیتا ساینتیست هستید و نیاز دارید اطلاعات سایت‌ها (حتی سایت‌های پیچیده و مبتنی بر جاوا اسکریپت) رو برای مدل‌های زبانی (LLM) یا دیتابیس خودتون استخراج کنید، پروژه
Firecrawl
که اخیراً تو گیت‌هاب ترند شده رو از دست ندید!
🔥
امکانات بی‌نظیر این ابزار:
1️⃣
استخراج هوشمند (Scrape):
تبدیل هر URL به فرمت‌های تر و تمیز مثل Markdown، HTML، اسکرین‌شات یا JSON ساختاریافته در سریع‌ترین زمان ممکن (میانگین ۳.۴ ثانیه).
2️⃣
پوشش ۹۶ درصدی وب:
به راحتی از پس سایت‌های سنگین JS-heavy برمی‌آید.
3️⃣
خزش و نقشه‌برداری (Crawl & Map):
کشف آنی تمام لینک‌های یک سایت و استخراج کل صفحات آن فقط با یک درخواست (Single Request) یا به صورت گروهی (Batch).
4️⃣
عامل هوش مصنوعی (Agent & Interact):
فقط کافیه به زبان ساده توصیف کنید چه دیتایی نیاز دارید تا Agent این ابزار سایت رو بگرده، باهاش تعامل کنه و دیتای مورد نظر رو جمع‌آوری کنه.
5️⃣
متن‌باز و خوش‌ساخت:
هم به صورت سلف‌هاست (Open-Source) و هم سرویس ابری قابل استفاده است و پکیج‌های آماده برای Python و Node.js دارد.
🔗
لینک سایت رسمی:
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#Firecrawl
#WebScraping
#API
#AI
#OpenSource
#Github
#Python
#Nodejs
#DeveloperTools</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6509" target="_blank">📅 09:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=s5Wd-I_-WnvcHf0y9zdUd1agp-aDitpM31GsrheH5X7nTE292_0a9vXiTo7ed0-2ltgWTL4Ovc5YB_GT_e3DY1lGUtVUhAix3LVpM8kH0UPDhXpoXh3Uy5EVQPuhurgTkp_QkeDNJHk-1KLL5KQMpbNH80mwgt_Q_piAE07RYkyUDehlV5zeenvzE8jHn_MeLnfvaVcqs4EfS04S9S3C1CXo1JM9-cbe5QV0ZKssVPZxyPQukRG1Nb2hGlDWL1Ub2oZeF04mSBwDTsY_JovueROrXo_Ku_bs3p2BSctQJ48n5X7RBMbkPRnm7T8KIq4Myqc3xvbO2T2MjmoXbVwJsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=s5Wd-I_-WnvcHf0y9zdUd1agp-aDitpM31GsrheH5X7nTE292_0a9vXiTo7ed0-2ltgWTL4Ovc5YB_GT_e3DY1lGUtVUhAix3LVpM8kH0UPDhXpoXh3Uy5EVQPuhurgTkp_QkeDNJHk-1KLL5KQMpbNH80mwgt_Q_piAE07RYkyUDehlV5zeenvzE8jHn_MeLnfvaVcqs4EfS04S9S3C1CXo1JM9-cbe5QV0ZKssVPZxyPQukRG1Nb2hGlDWL1Ub2oZeF04mSBwDTsY_JovueROrXo_Ku_bs3p2BSctQJ48n5X7RBMbkPRnm7T8KIq4Myqc3xvbO2T2MjmoXbVwJsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی KanaiAI؛ چیدمان مجازی مبلمان در خانه شما بدون نیاز به حدس و گمان!
🛋
✨
اگه از اندازه‌گیری‌های دستی و خسته‌کننده برای خرید مبل و وسایل دکوراسیون کلافه شدید،
KanaiAI
دقیقاً همون چیزیه که بهش نیاز دارید! این ابزار هوش مصنوعی به شما نشون می‌ده که هر وسیله‌ای دقیقاً چطور در فضای خانه شما قرار می‌گیره.
🔥
چرا این ابزار فوق‌العاده است؟
1️⃣
مدل‌سازی دقیق:
اسکنر هوشمند این سرویس، یک مدل کاملاً دقیق و سه‌بعدی از اتاق یا محیط خانه شما می‌سازد.
2️⃣
خداحافظی با متر و اندازه‌گیری:
دیگه نیازی به محاسبات و درگیری با ابعاد نیست؛ هوش مصنوعی خودش پارامترهای وسایل مورد نظرتون رو با فضای خالی اتاق تطبیق می‌ده.
3️⃣
تجسم واقعی پیش از خرید:
مبلمان و وسایل جدید را قبل از اینکه پولی بابتشان پرداخت کنید، مستقیماً در دکوراسیون منزل خود ببینید!
🔗
لینک ورود به سایت
🔵
@ArchiveTell
| Bachelor
⚡️
#KanaiAI
#AI
#InteriorDesign
#TechNews
#SmartHome
#Architecture</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6508" target="_blank">📅 09:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if4UqugDTommimpBlZAFKmEvEg6N9UFBkCTBG3ivCv-hr0pjthX7M2ndEJZIczs0JZ9azUDWeunSZBldqQe2427fDqFzsJu1f59zwcYEegGFEq7VXuVf8nFPdICrB7-WPCNWL5mQh59dIVoNUD3_hPox9PeVgXzG9Pct_Q3XOAWTQ_VhrMqklLoHL9flDsYOPO-83KgF_nGcU8oSD1qAp3rQpXuoD409weoKfsviRJ8R9GEIdMp9RKuNkZWs-YQ1l_7XA_glI7wvhkB7SiJMUIAI4_nFFhuxFq6SQDLCixAELncdC8I0eLUT7kcTivAGgg16m5A5c8nh2WVTeexClA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎵
Navidrome — اسپاتیفای شخصی خودت رو بساز!
سرور موسیقی رایگان و متن‌باز که کامپیوترت رو به یک مرکز پخش موسیقی خصوصی تبدیل می‌کنه.
☁️
✨
چرا عالیه:
•
🏠
رایانه شخصی = مرکز موسیقی خصوصی
•
📱
دسترسی از هر دستگاه: اندروید، iOS، وب، پلیرها
•
☁️
پشتیبانی از فضای ابری — لازم نیست PC همیشه روشن باشه
•
🍓
اجرا روی سخت‌افزار ضعیف
•
🎚️
کنترل کامل — بدون سانسور، بدون محدودیت
•
💸
کاملاً رایگان — بدون اشتراک
🌐
Site
#Navidrome
#Music
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/6506" target="_blank">📅 23:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452211db9f.mp4?token=C-T4cykUa4JLmZz5iojQTGS1L5G4CpNFpaU8jZNcHPHdHUD2sZlX658lTBNIyouzFiEAPD9C70zmEMTj6y_3-SyD22kfoE2-UYQkbdvTioeO-gptVV8iAFcybCO1Hqd0gcWFwu5TZowh4tNYMkVzAJU84xTS71vIsxAaQTLLeMY5aI8_-Ii1_3lYBjdjUAJuoRW-KoDcnobTDSdew7X8tiQN7L2a1iiub4x3gQdN_xCveyf9riC3nVjVmCyMN7ozzJJW-itCxunn2p4OeZcx_fucKX6WJABm6ZivdlHSnUN2VnoQ1uLO6ElKnwCkeJCm3OosAa-M4HvIe-IrwoRgpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452211db9f.mp4?token=C-T4cykUa4JLmZz5iojQTGS1L5G4CpNFpaU8jZNcHPHdHUD2sZlX658lTBNIyouzFiEAPD9C70zmEMTj6y_3-SyD22kfoE2-UYQkbdvTioeO-gptVV8iAFcybCO1Hqd0gcWFwu5TZowh4tNYMkVzAJU84xTS71vIsxAaQTLLeMY5aI8_-Ii1_3lYBjdjUAJuoRW-KoDcnobTDSdew7X8tiQN7L2a1iiub4x3gQdN_xCveyf9riC3nVjVmCyMN7ozzJJW-itCxunn2p4OeZcx_fucKX6WJABm6ZivdlHSnUN2VnoQ1uLO6ElKnwCkeJCm3OosAa-M4HvIe-IrwoRgpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
OpenScreen — ضبط صفحه نمایش، سینمایی و حرفه‌ای
✨
قابلیت‌ها:
•
🖱
حرکت روان و طبیعی موس
•
🎨
پس‌زمینه شیک و حرفه‌ای
•
✏️
ویرایشگر داخلی: زوم، سایه، گرد کردن گوشه‌ها
•
💻
سازگار با ویندوز و مک‌اواس
•
💸
رایگان و متن‌باز — رقبا ماهی ۲۰$ می‌گیرند!
🌐
Site
#OpenScreen
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6505" target="_blank">📅 21:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGWL8DVj3MQNDHXYMLI24NtlHOjgGoC2lsUl7CMT2_hkwX0xPeXSb045Zfk0Anvad5MwPtKa3TBrzhZoWiG4-bi35oOYmemmqQNcNyCGyIHJTZcR838wgD0XFgnE5bVvHcmsGQriHr8lHQ3_aVQvO93cHvfk6iZnUVscBGXIjBqRFqBMgKp0oVI2_tfzfDPuy8AErDXPzaue-9sQEN7qN3mXP0l46gYkRUE-JADJfXMfOgWja-Ydogy6GNp9gF3pZTDDQfCVnenhxyQMbMXTGWA0BsOAkSJ2Mohqyf8ZUJPX-giulK15PEZMQaHwGTSmaO-J5-iP3Ueky6mauh3NgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین سایت دزدی دریایی زنده شد — Bookracy در سال ۲۰۲۴ راه‌اندازی شد و به سرعت در شبکه محبوب شد، اما در سال ۲۰۲۵ سایت بسته شد و حالا دوباره بازگشته است.
• درون سایت تعداد زیادی کتاب، کمیک، مانگا و انواع دیگر محتوای چاپی وجود دارد.
• تمام محتوا بسیار سریع دانلود می‌شود. می‌توانید کتاب‌هایی پیدا کنید که حتی در کتابخانه‌ها هم نیستند.
• همچنین امکان ایجاد لیست شخصی برای مطالعه و افزودن هر چیزی که می‌خواهید وجود دارد.
🌐
Site
#Bookracy
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/6504" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgseCDhUhCk9mtULsMV0CtT1yl5hcdO4kndNzyrauwF5ig0coio18-fOlAE2C7dbyi9JLWw9FpRQ-1HjBBdfa-O_TOa844-4BaNVUHrvFidMHrHZESpe8pjy8FZNMAwlQwld2iHmdKm3mjP-zo748XvNA0pecFh0YGsqtQe9KnTYe2-JWzRoYQOrQnKVsCaIjvdAJmdqgGEYNOBM-7U8aEwfJawOCUVi3F5CbxMwi_XGHvDPQ1hmfOoY3Brgh7lXowOwyAqdrJJxSnI6qwhL6We4vjmNf2_3kkqOxG_3I4n0Nus2mdvcg3lAt3558T7T1_NB9KIFJrNhYmUvmn7YYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗂
PostKeeper
این افزونه توییتر یا X را به آرشیو شخصی شما تبدیل می‌کند
✨
قابلیت‌ها:
•
🔹
خروجی پست‌ها، لایک‌ها، بوک‌مارک‌ها و لیست‌ها
•
📥
دانلود فایل‌های ساختاریافته برای پشتیبان و مرجع
•
🔒
آرشیو محلی و خصوصی روی دستگاه خودتان
•
🧭
جستجو و دسترسی آسان به تاریخچه حساب
•
🛠
متن‌باز با تمرکز بر حریم خصوصی
🌐
سایت
🌐
افزونه
#Twitter
#X
#OpenSource
#Privacy
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6503" target="_blank">📅 19:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoYezHJaH0Iu9f1rsETpEMccIOFvrwFCh6pZdWfM7ImwC4v4PjqbZ4xBFMN-EhnUlP-D4Fe_OmXdckE0mki3-wO7Mqtr-DxN7_lXxtRmI3W1jz79SBDXGoXkesRwhQ3TSkoHxCv8W02hBMTHEsKV1bOhXKlGhSLftmpctfGq1VjDv2yB4CGoZqMPYe0VYBarGLJx5_dXFGkOjfmqifQOSJM8rXljTZYXWEYGhok0jUix8RYQv3usvOljsmSjairA0IHZoggggcBK4v7mQHfhOGYO1cakbDGLd-2OJ9AMPFmi8RAMCj51bP-97hvxr6wOtPZ5RThcGQGqWSlZ0XRa4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
80 کریدیت رایگان برای دسترسی به برترین مدل‌های جهان مثل Opus، Fable و GPT
✨
همین حالا وارد سایت
kie.ai
شوید
📝
ثبت‌نام کنید و از امکانات فوق‌العاده آن لذت ببرید
🔑
همچنین می‌توانید API Key اختصاصی دریافت کنید
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6502" target="_blank">📅 17:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔗
tiny_computer
یک محیط دسکتاپ کامل لینوکس (Debian 12) رو فقط با نصب یک فایل APK روی گوشی اندروید بالا میاره!
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/6499" target="_blank">📅 16:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvdyRJuONrzCPK-XlCEmxpibKahmGNWnfwBcXgBtp7ht8ei9qWNFnokgYgtplE3C4eGagSuGJ0sBdRcpl8jzdxi2FblKt_cMXWlC0BVdTWrKm-adrlLVjePzpO7mwLkPh36MmwmhGatQJjiqwkCUTu6zyZ3in3aHZ-Lr0UxMII3keZ8rb9FHkiAVb05NiLJfoUj8QgvhXTdkRCj2B7jHx4BMguojCB9-edwjflABLKXhpEoxwTQj2GB3BuUtlt_0OY4zrXYNANmp7R8aS7zBRX0FhN_KBW7i01EZMh5bm_oh9ib-IZtcLhnJrqayieLbUHoBN15mXFKX1oEQ04gwoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ترسناک بقا که قوانین هر مرحله تغییر میکنه ، در تاریکی از Cobb فرار کن و از سیاه‌چال خارج شو.
🌐
Site
#Game
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/6498" target="_blank">📅 13:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=miDk8s6yyvp091T5Ps58I_qmzQPkl5S-EOg9L_4uThd9UP4sVlusE3CDAxJkwSxL_XN1LIF1JtwtD5K2tZx613b3TEgV2BEFqpu0k1YP9vS1cd6Ms8FXaPFRjPt6cYtVWd7u4K9q3ZSkBDofTPq8qOiCRjQuZF8P3KXAYO8MHcYri3BVzHKBcuEbrCHFWOT4LXOO9Z5kg2dvtQJFBFcyynlXmYJZmiyzS929uzk9zHEjyoCfJtprybPDw5OuQwfwakf_wRg5w0l-vJIUqeMZmHj0Ot2KqlSNlypKVSPVHxnS2W3LNLc2ohzJ_OmaUc8BpulgX9dgYyt_fmHoMJZdeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=miDk8s6yyvp091T5Ps58I_qmzQPkl5S-EOg9L_4uThd9UP4sVlusE3CDAxJkwSxL_XN1LIF1JtwtD5K2tZx613b3TEgV2BEFqpu0k1YP9vS1cd6Ms8FXaPFRjPt6cYtVWd7u4K9q3ZSkBDofTPq8qOiCRjQuZF8P3KXAYO8MHcYri3BVzHKBcuEbrCHFWOT4LXOO9Z5kg2dvtQJFBFcyynlXmYJZmiyzS929uzk9zHEjyoCfJtprybPDw5OuQwfwakf_wRg5w0l-vJIUqeMZmHj0Ot2KqlSNlypKVSPVHxnS2W3LNLc2ohzJ_OmaUc8BpulgX9dgYyt_fmHoMJZdeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">MagicVideoAI
تبدیل متن به ویدیو
🔥
شرکت ByteDance (تیک‌تاک) ابزار جدیدی برای تبدیل متن به ویدیو ارائه کرده است .
این مدل از نظر پارامترها از Pika 1.0 و Stable Diffusion-XT پیشی گرفته و ویدیوهای فوق‌العاده‌ای بر اساس متن تولید می‌کند.
🌐
Site
#AI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6497" target="_blank">📅 12:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJO4mHbSJbli6kXCqccxFU5pqdGAzOoNPDW8QQUpTHNednB98XqcbU-t0zB4qZhDa4Qshbba3j4TFbmOyHguAUoF7diDXUtuhmVDRYaf5CaLKhOzkT7tL3UVu9KQwc0mWXq2amXqb1JX5_SGgOOVSjt6_cTMAsvebr4N_h7dssqV7Jiw8g65Qu2yDv3Ai9mrwFBygjG4mZ0pkU43PY8kOG52IZjZoWHj7nh658i5Bf5Rs93tZ_zaLDZpMsFxBNClOi9aD6YXQoFLXiFbAP-3TkFZ5FtJxuZ_qcXwOCw9u740Ruv6_gutsnETSUevZixNlU4sP0_RcYTOhhXhNJgH4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی Sakana Fugu؛ سیستم چندعاملی (Multi-Agent) که GPT-5.4 و Opus 4.6 را شکست داد!
🤖
✨
شرکت ژاپنی پیشرو در هوش مصنوعی یعنی Sakana AI، به‌تازگی از پرچمدار جدید و تجاری خود با نام Sakana Fugu رونمایی کرد و ثبت‌نام نسخه بتای آن را باز کرده است. این سیستم یک…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6495" target="_blank">📅 10:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚀
معرفی Sakana Fugu؛ سیستم چندعاملی (Multi-Agent) که GPT-5.4 و Opus 4.6 را شکست داد!
🤖
✨
شرکت ژاپنی پیشرو در هوش مصنوعی یعنی Sakana AI، به‌تازگی از پرچمدار جدید و تجاری خود با نام
Sakana Fugu
رونمایی کرد و ثبت‌نام نسخه بتای آن را باز کرده است. این سیستم یک پلتفرم هماهنگ‌کننده چندعاملی (Multi-Agent) است که در قالب یک API واحد (سازگار با فرمت OpenAI) ارائه می‌شود.
🔥
ویژگی‌های شگفت‌انگیز این سیستم:
1️⃣
دو نسخه متفاوت:
نسخه
Fugu Mini
(با تمرکز بر تاخیر بسیار کم و سرعت بالا) و نسخه
Fugu Ultra
(برای پردازش تسک‌های فوق‌العاده سنگین و پیچیده).
2️⃣
معماری کاملاً پویا (Dynamic):
برخلاف سیستم‌های قبلی که نقش‌های ایجنت‌ها از پیش تعیین می‌شد، هسته Fugu یک مدل زبان سبک و خودران است که بسته به میزان سختی تسک، مدل‌های «کارگر» (Worker) را به‌طور خودکار فراخوانی کرده و کار را بین آن‌ها تقسیم می‌کند.
3️⃣
خوداصلاحی و Test-Time Scaling:
این سیستم قابلیت بازگشتی (Recursive) دارد؛ یعنی می‌تواند خروجی‌های قبلی خود را بخواند، اشتباهاتش را تشخیص دهد و یک گردش کار جدید برای اصلاح آن‌ها ایجاد کند.
4️⃣
پادشاهی در بنچمارک‌ها:
نسخه
Fugu Ultra
در تست‌های به‌شدت سخت استدلال و کدنویسی طوفان به پا کرده است! این مدل در تست‌های GPQAD (۹۵.۱)، LCBv6 (۹۳.۲) و SWEPro (۵۴.۲) توانسته مدل‌های پرچمداری مثل
GPT-5.4
،
Gemini 3.1
و
Claude Opus 4.6
را به‌طور کامل شکست دهد.
🔵
@ArchiveTell
| Bachelor
⚡️
#SakanaAI
#Fugu
#MultiAgent
#AI
#GPT
#Gemini
#Claude
#TechNews</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/6494" target="_blank">📅 10:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚀
معرفی یک راهنمای جامع و فوق‌العاده برای یادگیری زبان انگلیسی!
🇬🇧
✨
اگه دنبال یه نقشه راه اصولی، متفاوت و البته رایگان برای تقویت زبان انگلیسی می‌گردید، ریپازیتوری
English-level-up-tips
که اخیراً تو گیت‌هاب ترند شده رو از دست ندید. این راهنما با یه رویکرد قدم‌به‌قدم، یادگیری زبان رو از یه غول ترسناک به یه پروسه لذت‌بخش و طبیعی تبدیل می‌کنه!
🔥
ویژگی‌های برجسته این راهنما:
1️⃣
پوشش تمامی مهارت‌ها:
از درک مطلب و دایره لغات گرفته تا لیسنینگ، ریدینگ، اسپیکینگ و رایتینگ؛ همه‌چیز در این آموزش گنجانده شده.
2️⃣
یادگیری با قدرت هوش مصنوعی:
یکی از جذاب‌ترین بخش‌های این راهنما، آموزش نحوه استفاده از ابزارهای هوش مصنوعی مثل
ChatGPT
و
Gemini
برای تسریع و بهبود فرآیند یادگیریه.
🤖
3️⃣
مناسب برای همه سطوح:
فرقی نمی‌کنه مبتدی هستید یا پیشرفته، دانشجو هستید یا یک متخصص؛ این مخزن ترفندهای جذابی برای همه داره.
4️⃣
جامعه کاربری پویا:
یک مسیر ساختاریافته که به شما یاد می‌ده یادگیری زبان یک مسیر پیوسته است، نه یک مقصد نهایی!
🔗
لینک مخزن در گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#English
#Learning
#Github
#AI
#ChatGPT
#Gemini
#Roadmap
#Education</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6493" target="_blank">📅 10:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-ASBnVM2OfNMJFUM-Ea5PcvijJpP0vgOuQB9W7gbcZWg6O6WdUc0T3P-JCPcxfd2OFQHk2IgqmXpJ-ilMlm6JZDeEvM2227nsecvSQ6q-qAf82tRWxVd449_cDipCzE29VrQo0ja5OuCSAWe6_4D_rwCmuhrSxauR1GvbpTOssRZEy1ltsJzq93Fk7J8Rqt1KMUfxz9O3Z4dtCR3p7DhNJ4FFxI4P1g5KqBayBCvm2-NkKRNIEtOXtsGhulY8JTxMkulRvUfUZ06a2c7zrRes54L7X1nEcG4cx-lVAt5COADO_tgaSg7QD1kOXnm2SRHhsK4UFvogIJR3535pdtPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
ساخت آرشیو اینترنتی شخصی
ابزاری به نام Monolith می‌تواند کل سایت‌ها را در یک فایل HTML مستقل ذخیره کند.
دیگه نیازی نیست نگران باشید که مقاله، دستورالعمل یا مستندات مورد نیاز روزی ناپدید شوند.
✨
قابلیت‌ها:
•
🔹
ذخیره کل صفحه در یک فایل HTML مستقل
•
🖼
نگهداری تصاویر، استایل‌ها و منابع صفحه
•
⚡️
استفاده ساده بدون تنظیمات پیچیده
•
🛠
اجرا روی ویندوز، لینوکس و مک‌اواس
•
📦
رایگان و متن‌باز
🌐
GitHub
#OpenSource
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6492" target="_blank">📅 09:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚀
معرفی OpenPencil؛ رقیب متن‌باز و رایگان فیگما مجهز به هوش مصنوعی!
🎨
✨
اگه به دنبال یک ابزار طراحی جایگزین هستید که هزینه‌ای براتون نداشته باشه، با
OpenPencil
آشنا بشید! این ویرایشگر طراحیِ متن‌باز (Open-Source) با قابلیت‌های شگفت‌انگیز هوش مصنوعی منتشر شده و تمام ابزارهای پولی رو به چالش کشیده.
🔥
چه کارهایی می‌تونه انجام بده؟
1️⃣
پشتیبانی از فایل‌های فیگما:
می‌تونید فایل‌های با فرمت
.fig
رو مستقیماً توش باز و ویرایش کنید.
2️⃣
اجرای محلی (Local):
کاملاً آفلاین و روی سیستم شخصی شما اجرا می‌شه، بنابراین حریم خصوصی پروژه‌هاتون کاملاً حفظ می‌شه.
3️⃣
دستیار هوشمند (Agentic AI):
دارای قابلیت‌ها و ایجنت‌های هوش مصنوعی داخلی برای کمک به پروسه طراحی.
4️⃣
خروجی مستقیم کد (جادوی فرانت‌اند!):
طرح‌های شما رو با یک کلیک به کدهای تمیز و آماده‌ی
Tailwind
و
JSX
تبدیل می‌کنه!
⚛️
5️⃣
یکپارچگی عالی:
قابلیت اتصال و هماهنگی کامل با ابزارهای برنامه‌نویسی محبوبی مثل Claude Code و Cursor.
🔗
لینک دریافت پروژه:
🔵
@ArchiveTell
| Bachelor
⚡️
#OpenPencil
#AI
#Figma
#Design
#OpenSource
#Tailwind
#JSX
#FrontEnd
#DeveloperTools</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6490" target="_blank">📅 04:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">📰
خلاصه اخبار مهم سایبری و تکنولوژی هفته:
🚨
✨
🔹
آمریکا و توقیف AI:
دولت آمریکا برای اولین بار در تاریخ، انتشار یک مدل هوش مصنوعی (
Claude Fable 5
) را به دلیل خطرات امنیت ملی ممنوع کرد.
🔹
هک بانکی در ایران:
یک حمله سایبری سنگین، سیستم ۴ بانک ایرانی را فلج کرد.
🔹
شنود تلگرام:
پاول دورف اپراتور بزرگ هندی (Reliance) را به رهگیری ترافیک کاربران تلگرام متهم کرد.
🔹
خطای مرگبار هوش مصنوعی:
یک سیستم AI در برزیل با رد درخواست بستری اورژانسی، باعث مرگ یک بیمار شد.
🔹
فریب موتورهای جستجو:
محققان ثابت کردند موتورهای جستجوی پیشرفته AI به‌راحتی با یک کامنت هدفمند در ردیت (Reddit) فریب می‌خورند!
🔹
ابطال گواهی‌های SSL:
شرکت GlobalSign به دلیل تحریم‌ها، گواهی امنیتی هزاران سایت روسی را باطل کرد.
🔵
@ArchiveTell
| Bachelor
⚡️
#CyberNews
#AI
#Telegram
#Security</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/6489" target="_blank">📅 23:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6488">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚀
معرفی Prompts.chat؛ خفن‌ترین و جامع‌ترین کتابخانه پرامپت برای هوش مصنوعی!
🤖
✨
اگه می‌خواید از مدل‌های هوش مصنوعی (مثل ChatGPT، Claude، Gemini، Llama، Mistral و...) خروجی‌های تخصصی و بی‌نقص بگیرید، سایت
Prompts.chat
کامل‌ترین مرجع برای شماست!
🔥
چه چیزهایی تو این سایت پیدا می‌شه؟
1️⃣
قالب‌های آماده و کاربردی:
نیاز به نوشتن یه رزومه‌ی حرفه‌ای دارید؟ یا می‌خواید یه قرارداد پیچیده رو تحلیل کنید؟ پرامپتِ آمادش دقیقاً همینجاست.
2️⃣
پوشش تمام نیازها:
از ایده‌پردازی برای کسب‌وکار و تولید محتوای مارکتینگ گرفته تا خلاصه‌نویسی دروس و برنامه‌ریزی تمرینات ورزشی.
3️⃣
خروجی‌های سطح متخصص:
با استفاده از این پرامپت‌های مهندسی‌شده، هوش مصنوعی طوری جواب می‌ده که انگار یه متخصص حرفه‌ای اون متن رو نوشته!
🏆
اعتبار این مجموعه چقدره؟
این فقط یه لیست ساده نیست! این دیتاسِت
رتبه اول بیشترین لایک در Hugging Face
رو داره، بیش از ۴۰ بار در مقالات علمی معتبر بهش ارجاع (Citation) داده شده و حتی در رسانه‌های بزرگی مثل Forbes و دانشگاه‌های تراز اولی مثل هاروارد و کلمبیا هم ازش نام برده شده!
🔗
لینک ورود به مرجع پرامپت‌ها
🔵
@ArchiveTell
| Bachelor
⚡️
#Prompts
#AI
#ChatGPT
#Claude
#Gemini
#HuggingFace
#Tools
#Productivity</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/6488" target="_blank">📅 23:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚀
معرفی Upscayl؛ افزایش بی‌نظیر کیفیت تصاویر با قدرت هوش مصنوعی!
🖼
✨
اگه عکس‌های بی‌کیفیت، تار یا سایز کوچکی دارید و می‌خواید رزولوشن اون‌ها رو بدون افت کیفیت به شدت بالا ببرید،
Upscayl
دقیقاً همون ابزاریه که نیاز دارید! این نرم‌افزار کاملاً رایگان و متن‌باز (Open-Source) با استفاده از پیشرفته‌ترین مدل‌های هوش مصنوعی، معجزه می‌کنه.
🔥
ویژگی‌های کلیدی:
1️⃣
پردازش گروهی (Batch Processing):
می‌تونید یه پوشه پر از عکس رو بهش بدید تا همه رو با هم و به صورت خودکار باکیفیت کنه.
2️⃣
افزایش وضوح و شارپنس:
رفع تاری، نویز و پیکسلی بودن عکس‌ها به طبیعی‌ترین شکل ممکن.
3️⃣
مدل‌های سفارشی:
امکان اضافه کردن و استفاده از مدل‌های هوش مصنوعی دلخواه برای رسیدن به بهترین نتیجه ممکن.
4️⃣
پشتیبانی کامل:
سازگاری با سیستم‌عامل‌های ویندوز، لینوکس و مک‌اواس (macOS).
⚙️
نکات فنی:
* این برنامه با زبان قدرتمند TypeScript توسعه داده شده است.
* برای اجرای پردازش‌های این ابزار، سیستم شما به یک کارت گرافیک (GPU) سازگار با Vulkan 1.3 نیاز دارد.
🔗
لینک دریافت و گیت‌هاب پروژه:
🔵
@ArchiveTell
| Bachelor
⚡️
#Upscayl
#AI
#OpenSource
#ImageUpscaling
#Tools
#TypeScript
#Github</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/6487" target="_blank">📅 21:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oA-6uvCITSRBkqgDBw9PAIMv0Y5rlDoQw7PiGVw26-FKtabc3tSuVsxTq7w_O9xWsNnNtjRkgubMGOzt33P1xkSsVJQ7FJKH1VaPxl1_C7Vdym1BDRsOvuYeOvKa2-kP2DxqWTB7WztNttpyqR8-WIjvYkGODeKw-RXnvDTq2y6lLbTLRw3PBk7vSv04Z233izMdm8AparmXh564RpK73R6T9mpEOj-_rmIefIdX6piHnGxLlN40t9ynenhzO4Nh0xp55bS4yKX-j6VIBHmUPIo_SCSQA10IygT-0p6U5Wxu90KWGbFEPMIx48U1PjRJbDCWO30WF15HRE1LpJCueQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت What Is This Movie کمک می‌کند با توجه به صحنه‌ها، دیالوگ‌ها، جزئیات داستان یا نشانه‌های بصری دامنه جستجو را محدود کنید و سریع‌تر فیلمی را که نامش را به یاد نمی‌آورید پیدا کنید.
🌐
Site
#Movie
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/6483" target="_blank">📅 19:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3j5DxRxUSm1UvcwBmAA3s5UgEoTqRDIyyrNV0w1sTkCTVFfJsftt_3h80RmCNdz2KyWY3diX_8WY3F9r64AtgwgGsrTQcEgdVZd8O0p7n-Un0OIhSJuVbdw1JeZCpNHpDuWigv-Fy1ZQKKMaseHLMC5xh1jLrPOhdhqhSh1FZWMX2sa3U5-u46GYIwfR2JDyOtZ0lG7Cxpf1DVZuiDOlMiBLSCmOUTHpIZ9nWtZKFirqcNKbZoaEjZjtq7ghqMVKSLbcM-19-jzaArEJxIO-OYe4rH893EcQ1PbF0ZZwgBLc27WD713v4OH15GUjRI-gzhzSJI7wlmZ-29RZNQRqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف رایگان واترمارک Gemini آنلاین و بدون نیاز به ثبت نام
🌐
Site
#Gemini
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/6482" target="_blank">📅 17:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚀
معرفی Lift؛ هوش مصنوعی رایگان برای استخراج و پارس کردن فایل‌های PDF!
📄
✨
تیم Datalab به‌تازگی مدل هوش مصنوعی قدرتمندی به نام
Lift
رو منتشر کرده که می‌تونه داده‌ها و اطلاعات رو از فایل‌های PDF و تصاویر بخونه و در نهایت یک خروجی کاملاً ساختاریافته و تمیز با فرمت
JSON
بهتون تحویل بده.
🔥
ویژگی‌های کلیدی و برجسته:
1️⃣
دقت و کیفیت شگفت‌انگیز:
توسعه‌دهندگان این مدل ادعا می‌کنن که کیفیت خروجی Lift به‌شدت نزدیک به مدل قدرتمند Gemini Flash هست و از خیلی از مدل‌های متن‌باز (Open-Source) فعلی بهتر و دقیق‌تر عمل می‌کنه.
2️⃣
خروجی ساختاریافته (JSON):
این مدل دقیقاً خوراک برنامه‌نویس‌هاست! داده‌های خام، جداول و متن‌های به‌هم‌ریخته رو می‌گیره و یه دیتای مرتب و آماده‌ی استفاده تحویل می‌ده.
3️⃣
کاملاً رایگان و در دسترس:
این شبکه عصبی صددرصد رایگان و متن‌باز منتشر شده و می‌تونید بدون هیچ هزینه‌ای ازش تو پروژه‌هاتون استفاده کنید.
🔗
لینک‌های دسترسی و دانلود:
گیت‌هاب پروژه
مدل در هاگینگ‌فیس
🔵
@ArchiveTell
| Bachelor
⚡️
#Lift
#AI
#PDF
#JSON
#OpenSource
#DataExtraction
#DeveloperTools</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/6481" target="_blank">📅 16:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjKMp7-rpNQMu7YT6hZ5qxMDt6e4CRaDKfmACnx_c6McdXZecDIbYgZ54R6T_ZP4uYGSpp89pdvFRdwYXYLkqM80GtDakA2Yx_gsQgohmbV0g9CNabwxMPyYr6-L43GFtUiNDqMYCj08y38sCTXsrjrd1x70wIlvMHXFUi0FWJ_XtRFTbdqcfIzAe2gNfHk-LdkzhuFlAxm_Y6PPNE5S_lbC4I0pjrJgzNkeL0THuuIGIFUIaK_3rfqqcLS7TG3tdzffaxbVq2xFWjSOkRo1-Q-Y5kXghpQsLiYIYk_dBOehp3QMi7N9Rd3XY6uEu9-nzWxLdIhpRfuWnYYVP462kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
مدل Gemini 3.5 Pro احتمالاً ۹ تیر (۳۰ ژوئن) منتشر می‌شود!
🚀
✨
🔹
شایعات داغ:
کاربران شبکه X پیش‌بینی می‌کنند که این مدل قدرتمند دقیقاً در آخرین روز از مهلت وعده داده‌شده توسط مدیرعامل گوگل (۳۰ ژوئن) منتشر شود.
🔹
سوتی عجیب گوگل:
در حین آماده‌سازی بک‌اند برای این آپدیت جدید، رابط کاربری تحت وب Gemini باگ داده و اشتباهاً پاپ‌آپ معرفی نسخه‌های قدیمی (2.0) رو برای کاربران نمایش داده!
🔹
نتیجه‌گیری:
این گاف فنی نشون داد که نسخه وب جمنای هنوز پر از کدهای قدیمی (Legacy) و باگ‌های پیش‌پاافتادست.
🔵
@ArchiveTell
| Bachelor
⚡️
#Gemini
#Google
#AI
#TechNews</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6480" target="_blank">📅 15:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6479" target="_blank">📅 12:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRM-ujBjdzM45-rqQkSxJs07K9gsYJGcUdfZ8TsB_ALGXZ2jSvi_se5iEloannl7sRWefSfdqIt_f_O0nxqCHnM2yb0xiZUppTH5SrpnG2nOXKq8hC__d17XGYQIg5pf32B9GXIrznk1E0vSune_8zC69z_JbsBypVrAPyxPjoR9Fc24SXElkcAXGMA_XfgpqAfuw3jiSG0bzGNakd-oxOuDR4KPQ5v9UTNf3hGaE9RH95kyvFtf8HOEhMWKTxx_OjC3AQNXB7Ab9xPUm0GTfw9Dip4mIy71kF2sfmLs5YgXjCFezFh7eodEo9uh017-WwAJXKiyF6o4Se0CKHgxeQ.jpg" alt="photo" loading="lazy"/></div>
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
🏞
دقت بالاتر در مناظر طبیعی و معماری خاص
🔗
لینک:
Site
#AI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6478" target="_blank">📅 12:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckRDHoHmY8ihLbwSINIAtLPdFeuq6QC0ZvdOlUGiz3162LIdQ_55Fs77FJ1wV0IAn_aO38e1QuPdYnZ_H36gt8tjTtvQq6BVMjFfl92jPVkt079i5gICrElSpv0HUyboufqxJXAVrTT-EWMrmlt0LSp4PHg-BTqYMFRgenigwjQYWRKNcKEBaGJeQh11KehkkFLTIJ30sg1cqkiEr1_uPvoqC3eDS1GQgq3-q4oXx4BvIO0-tsrsy5m_eRl6VgUGHOj-b1iY3c_8FL-RHLYDroHch9Etpy1xyvLC0-plz8HxxPgNNS7LvYZ1DzTw4tsERXZhh9ULt4K1GMx820rR3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/6477" target="_blank">📅 10:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6476">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=mzmmW-FuxBhW-ed055wFRxRY_07Ct8NDpz_Cq4bWg2Qw8PFq5sCt414RP_aHIyRRShAi1fTRF9hyR2cx9r3GKlRAQx1B1U6A5RQei1ZqgJ5bJntYS8uQ0xNPe-26x5ws21abZtNrAoTlmD74HYzNijQHtUiaVxq6nPAoweVA-gDaXr8dhmmGuG4cxEAayY4o2C6AFfdvgBzf20gaE04oO4EzYW8EEKpotcdGeYu7danjwgLNcdBECYclOkANf7un2zvWp3MVGefJ2c9Zt71M7M01_uEbhDs1-rATdOD_mSlyzhkvJMBECSv796tnKUpX0AWYv-8wxXitj0B7aKkV8g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=mzmmW-FuxBhW-ed055wFRxRY_07Ct8NDpz_Cq4bWg2Qw8PFq5sCt414RP_aHIyRRShAi1fTRF9hyR2cx9r3GKlRAQx1B1U6A5RQei1ZqgJ5bJntYS8uQ0xNPe-26x5ws21abZtNrAoTlmD74HYzNijQHtUiaVxq6nPAoweVA-gDaXr8dhmmGuG4cxEAayY4o2C6AFfdvgBzf20gaE04oO4EzYW8EEKpotcdGeYu7danjwgLNcdBECYclOkANf7un2zvWp3MVGefJ2c9Zt71M7M01_uEbhDs1-rATdOD_mSlyzhkvJMBECSv796tnKUpX0AWYv-8wxXitj0B7aKkV8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
گوشی‌تان را به کنسول رترو تبدیل کنید؛ صدها بازی کلاسیک مستقیم در مرورگر.
•
🕹
بازی‌های PS1، Game Boy، Sega و پلتفرم‌های نوستالژیک
•
⚡️
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
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6476" target="_blank">📅 09:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A48GJ0TbCPygSNjpxsbBMjMyVEyzOK4D1eiftYsj32R2R5z-YxGpEym5zcu4nwfh3kInWHwOPXQckfj9mutUT2MQyl4bkuFO_YMCWGKJz4Sn2_sPr2c1kWskuDFebPNIAy5wOmIBHM4lHuxamE86dtLlMrIai1M221urjQWcr8PfyD0WiLjadgD93WGrkl3L1-c1pC_VhfSe43RIW2fEx-jLjIGL83NFsBsfjPMvnUwbbhsVJ8IuYwztVm9wxQKcYTiJpzlO35GRyMFb_kPxN-mvcPeZ7czp3DJRjmhqdV6CgS6AE30j2nFwKHLv6x2dy6L9lCMHsUYKbqZPLesWmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/6475" target="_blank">📅 01:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDSZrp1Fgv1W5LzspjpQUXna2r3pRXAp0d6ZzQRVcUj6U1balOud6CYHOw_J6mtGHSKtaCHBfRAkIh_zMC-iI5v37jvWf-_WVedLUQfMmOnd4LJBpjaK1M18ArhiCqdDGg7_3Seohiy5wZZldT8gk0vQh4Ec95Vm_DT1vJsf0dP0MtM5KB3YUKWr9C5GZ20JM4wuwKFG-BN1X65Vo5Vwz1BtJZukJFYJYhkL8IXWyxUHdsQwtEVtgo7EtEz0DfVnLBWX6QZBGtz0LFx2JFEVe3oj3ka9c-cHgDcu7xfMIhCjD4sy4XNIn2qE2L9yYg7ex0RDppSfUJYFnXgs2Lqfww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6473" target="_blank">📅 00:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6472" target="_blank">📅 00:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQPmL6vurfHrMJ0JwFyBJWbz5WBXBaYimoJ39yLJP3J8UAQdfzlyNpK5WPoMHYPkkK3r5b9rU_-AQzrUcz7lXbZDhL4Ok-pVTrMONzOX9fS_RwCHRL6WnUz-GuhSGNK-caCKW8-L122ywUXz6H3mzIiJ56FqYyvRwLH013qybqPubCydBmpjJW8yZEELS4n3GQ39BD_PaXAzrHhDI2qVZ72RBeX-_VLgHGMHIHhJswxqXiNMR1UDZGRNgvZxM2kKyxB-mDAXUoiB6HauarhJ9vrUyIIbHyE2JeYGXQ4Fvfkg-NMY_PaAoAH3FvyUhIg3WcvTLDoMCJZ4wt5xlGcXuQ.jpg" alt="photo" loading="lazy"/></div>
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
⚡️
قابل استفاده رایگان در AI Studio
•
🗂
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6471" target="_blank">📅 23:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6470" target="_blank">📅 19:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRfQIA7uW8OdJWmg7-Tx3ztviy8UafeZ0tSqTdOjZWNF_GnNBaqDfSYyBBAc_n82KAKIWNPsfMotY9xvFkyJFO2gWnuRcZLmebw7KX5XuL8LWPRNYnKhx1k3_05bHSZTSMIjomSaCrhMbvTYr5UMbPVVRNbx5CMVRvDrh-9u_J5Z28L2ROAfpOBAocFktzMx-GHST6JpeAJkZprJ9zsxUNbC5iP6rxaJLasjYZxhbY0IBHM7kADRxpDZ68zN8wmgtNkjtSXCwXjbm3_J3iHRYnPpui2xEpXsGT-H-Qj-PkSuPWrrBgAUTZ3sYf4dF6o7IalpMfgpepvv1vbNnYqkdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6469" target="_blank">📅 19:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6468" target="_blank">📅 17:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IHE3NiZYhaQX86uox2ja7yk0PcSlePosltwDYOjkCmoJ1xesYPmuXvnZdFQxUzuiQcFjFk_VKhwnZgUsO7Qx3n093Uc4HU12NXvRmjpK2yvzP2nelXSm57g6bnvs9HnSRj8R9QyFHXYO9FSuUtOtOlC2makMRu33Hj8LhxE6N9nF8WWahYfhwnSHh3rUj8o4jYJSButZuuWiTP1fwk5VlQLt68XwiraMP0HbcSh5xLfPFvbHr5HoFkrQh8_N2wDQ-bBkjc7z09Ycggsx2KqFBiFpzD1pSsY81FtEb8DS3N5-WxRIs27AwGA3avTHz2o-lnONTX4ru2K3vzjv1n0qsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cfBypgu4oKvQsCfXIgn0TLzUVbWzAkOBvA3G7ubK9G1H9H3wcFCe1iL_24lMShjh8I84BgLAhDsfLHxHQgVbebk25-RgLDpdfbISRTfjFd70bPtZQ_lIPMxXBsHQKFcaVJ5jjYCpMDgtPZefU8V_V01Mhrd-mQdzlSp5uJKQ5nlcV4gNucKjSJy6xgT-E8-5poTJch1Brf3tOK9sjMf33G6WpwzM7HYIvNE9yizYanVCcBHAZsYlfB_Me9z2gq0xN3m5yonONyTXDy3P4EVMLn-jj6SnEO7NEIWJTgO19H2QcvNjC27E_M7QK8TQLYe4bMoYCO0qE8QcyfIINDnKrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k_Q4aB7zWpbLFl9gbBTX9Y5AOwbXimIqa2UtLNImC2iTVDsYq9gziy-Tf6BuLlv9MNSWZQLVE3vERi_CppaFt8mEuAPiKCWRrgnJou4u5FjnagnUXtkbgPAPvIKFrBRcWw-xdxU877IXyyicq5_uLcwfalONZjnZAVOGKNDlUSnSUbHatx6Sf-XOi9pnn3OLngcFEropFyup2bf8EDdwI6tZZVTSJ1J_LcojjcWckRwMczYmbT5TrOF5SCi_tkROcgZh1HF5nOTYhPcT6-vgt8Jd4qvo-qYJmiCkMFl5Rh1FFw2UQU9ITi2qyuFCzadswpMhIkz8Bb-QLXmMsnLFTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AlHqne3agMvIm82nsTQiiJMvK2Vzz-x8k_Ba7680ktQrE85bg9IwyC2pSlNS2lnaPgp5xtVKc9L7VmFmmDo8w-fTSZYWrl8KpZ0Zd0J35MGPs3PsYTCG2-KulUgpe6qHnfkC6wo0aIASUZDPOflWONmUNa4YgnAwlcgCRZ6y71jRXmM-iRX3ciPUZ2APnVquZ19BC5QvHJ47SgiUHXdnXaG4fJJFPWUCbUQCv7JllRAqYWLh5HBIjo_gkju6qVdG8GRdkXF62uYTI4CuI645Retcl9YCcY41hgrkgGNc7cQILCTuRRYEtH6gBjKX-rx1zsz4HUiREj2SSMARX4fN_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/6463" target="_blank">📅 16:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6462" target="_blank">📅 13:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TnsBEQPmfPTDrRsa1NjqxhrRvwwskOMSEqNQCicwQZcrRWbBn510bpvzJn9Zaitu110tkUM69Vv89aLSt7Q3S71kOJGshd1LBJT2aioJXxb8L_xUvQNtt69VsU_BYS_oqum6Qmi94g4LPACEaUOYv8FzjwKgVh4n_W2znePM_NNIX-SgzWHhbSqORZ86fMT7huWnFq6qZsDmYAhhROfUIfVpzI-P8qT0ziEcO3IkJilMKFyk4JgWLULs-2jOPvp7anzeFsMxkPme4H_Mns1h67xg2_KJ9wJ8qb9uNFZdExzYpxzNMS1aaSX-T2rBMlF3vUXn9CCqLQkRt2fVjfnjJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H6JFVVN0bG5S5bCG6bOHyubGVX-pWriJw6SK_txuqz-eLvN8h29qGoZK257fvfXoFlFJPT73YdRGidX74Q4MHnysHn8ZocbRcW6Ome5yNquJFGrTAsK7a0tfbr7ircFQvhTZkgGsRS620St6nYxMCxDYqp8hrYuWhuzuRHlv9-MDLfCrMMSYBSzAI74zQ2IcDhdXbUprc_ToWPLOEbZtlcjJdk-S8bYkFzY3t0_moU5SqKPliagVClwN1txwPote0z9BxHJVeziI9rJdPvXnAkKkVg0KG4eSdYUEAl2N7kq8zmXbPdinZOSJNzOv1LJNKpC3Gl7Na37UI_81ndZO1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wi_1pF5xSG8keg-uOa8sm23s50okhjqY5rD_8YOWKHESB7qdlC0NOy2qxRA8_EDjMroOWJt1YiFW2tfuE_ys9l2MUIJDpc0nKQ6E8L7F9djDfAs9Bi8f-nYtoDF3cT5F0m-HI0KaIzmWJXwjtghp1Jd7K8UMqcbvFITtdrsWa46uZ0nbAyEFXh_-rF9RmphFk_YfT_hzRLGvpanOCwq3MeGKlt3cVJc2C0iDTf-c71w3UrLB9LOFHXIGyvyZdt6nc0DVFIuL42wjuJWb-KHOdETVUS9rn3u0EDCylmf7KVqgs7MfssGIhM7NS9Mwhlwx8UPYh6BK2LDSLqDezOYhDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rKzj248Jo_RW1c0n_LN7UUF_EyUUqat-enKp0rVfl-JWT8TKQqChj7L1FbV7_c08rYX82kHG_blzm-jTKE-9uHBTGx_fVXt_NmthQ0OoUTF-zvrYXI8vAQmSQRyvbJAvmxDQWOiKC3CYYJ3b7vtc1ngYsi8qIVPaaCroVXVJTDYEHOYQpVt-4wp43U8_epzqNw01cMoSiYcRzWcis-pL8MIzBFVGEtfzG77W6vfhn2wXqVPyN7r1uVU3dhdcUrQeS8duXHDVWMhdKp1Ius5O3b0TZcAZ7bWXeuSca8pAWBfqoS2zA9m44nIV6dKqDMtNn_95AasMDLMYwoW840zJ3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ded905356.mp4?token=XbPy7kYNMfws8fVatyRsCJe2cQird8A5ODiH0f07me5iOQBaJdvvUVmgPvb1KMQzn7G3VaPV2OQi_FoNO9QrESERKWJG9--E7PcMmW201pVqIVqKnILIyVNxW3JGO90AqUvwSuiplol0qht281Nq55qDrOOtYR7CjbgLxLUrAPTn9gBVrvhV-iQRSh7kG94bPlB0fnLu2sZrqU_KwxBBIpz-2u4pqoRSlR2Nmq1b7CQwxUEVsRclpCACD2VE7kLUodlljjtKxRtKgtSgvRgBzqhBlOPiIvxNPkRZVvofsBhG9gl4N6NKWxcch9HC-R7b92gnFex2Lp9YVM3rqNXq4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ded905356.mp4?token=XbPy7kYNMfws8fVatyRsCJe2cQird8A5ODiH0f07me5iOQBaJdvvUVmgPvb1KMQzn7G3VaPV2OQi_FoNO9QrESERKWJG9--E7PcMmW201pVqIVqKnILIyVNxW3JGO90AqUvwSuiplol0qht281Nq55qDrOOtYR7CjbgLxLUrAPTn9gBVrvhV-iQRSh7kG94bPlB0fnLu2sZrqU_KwxBBIpz-2u4pqoRSlR2Nmq1b7CQwxUEVsRclpCACD2VE7kLUodlljjtKxRtKgtSgvRgBzqhBlOPiIvxNPkRZVvofsBhG9gl4N6NKWxcch9HC-R7b92gnFex2Lp9YVM3rqNXq4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
⚡️
اجرای سریع‌تر و مصرف رم کمتر
•
🛠
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/6457" target="_blank">📅 12:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/6456" target="_blank">📅 10:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9UkYQBxz0kpExTWHG9Fp-2GNeSU3lvnc6LEOJ6O3inksS8wcaOMV0g_a-Ucs8hLMVjJHyEQvFZJr8s2C66XK_CGsccabF4qEGrModm9vzR-Ez2kqyOIURsEqu2Y3DUhXY3d_VRe82cek06ZLgikMGb7KNjx2BwK7CYXPIpEiDI6Yg77-SFZfQ7mZXYIF3XqOMFvEdpDZ76KnvDVJzg5iZtQIBHlShpUwenObsiDXXo_JkpMF82IKxQvi-Lfn_PIlONl2lYA_jSWgvp0cBRJiQvYutvwxwMMU9v5ToJaXGRKj61iarOSagFNXRU7LZe_3S8eeXgpeURX0T8lk-VH9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/6455" target="_blank">📅 08:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/6454" target="_blank">📅 02:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L2aaIH-jv5WaWt17Sctv-0AFFbo3z8MdPpd_6euMTELMi9cewPFqLdpBHhDN2EGlfe3RF92jOrAlhot_8iEsblGZ4KkCc9vQRGcVrlA0XlWqJuH_ARmoM_KO9Q2vfiUlVh-cYX-EGkicS71iOZMIf49XeEmovMmwgX4RA2_83-jY1Z8BjoA_nMkQh3GYnxpKLVuYEqZDtyE8JUvl2Ivt7A3CPlBzpa-SykRfJoS-B_C_5TvtcqJrTzTeCmwn-lcnM7nHTUk_g2NVnb3XEybdzXkfbaBo-_h_zskZbDkXM4C46IhnMAXKfyr0zFWkN4dVz1Tw4k8TRcX1e-78EuvoNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uPSbwS8lsYVhH6fj4ItUylOxenQUx6oU6o2ckr2Phhnmh8NVpix0BV95WxJ-Dh4k7GIUT70dBWSH4GsNi4XdQNYuRw_FN_B5a85X-ViDR16GqFk_3QuLJyPREfK2TGfiZH04XbBJGnPEjaQ0PLpwTgMDZlsMVBOht4gmijFjK22pf9Xjl69lFNorySN0fRaB2j5ghje9xOXKW1KspM4zsT8IWI0v4JJljcsjUr5vJlVUkk0SDg1MEXuHmLKU7l_dWTNt_-5oDGayUkAgM-bJGarydPt1yH0PaKSZFCHuTsz2317vOCHmIqjVUzmCgzX2NQCqageZtrTHHaDx1CHAeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Product photography on a solid sky-blue background, soft studio lighting, no shadows.Product photography on a solid sky-blue background, soft studio lighting, no shadows.
Two thick, fluffy, plush terry towels are neatly folded and stacked one on top of the other, deep soft folds, thick looped pile texture. Top towel: white with thin blue stripes. Bottom towel: solid cream. [product from uploaded photo] rests nestled inside a deep fold of the white-striped towel, partially sunken into the fluffy fabric. [product from uploaded photo] lies diagonally inside a fold of the cream towel below.
Water droplets cover both products, fresh just-rinsed look. Top-down angle, empty blue space above for text. Photorealistic, high resolution, sharp focus, no text, no logos, no people.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6452" target="_blank">📅 02:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lem9b4JQCK1lrccJIjASDk8hSh4l8QtUBD56UtfG14kXn-KbGbckqWC-48z4dovZORcNSC_yF9Fimpu4bAyTxq-TtAljFUvNwxZOl4IF3vHcHPyHlJcKDVH7SOwCtZsefOwgXJFIu0kMl96LdqizFC1Z0za_-YqQs8BsjVvIbMcGbsXe-9cnyvZEQlIzQmUEUc-vMb0uFISv31JXiwedgloZhmeoD-__H83VxQeohLjUWoqVhl3PXBiX3RORozYrZPczhjI0MiaGQ1vh2XjGL56PY7JwmV4-_l-RtNzpM-epE6wPXptyM4znfxdqbUTFAmlKaNU3WeKGQc9HxWevqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/6451" target="_blank">📅 23:55 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
