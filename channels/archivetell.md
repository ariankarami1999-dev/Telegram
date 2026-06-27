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
<img src="https://cdn4.telesco.pe/file/gtFqI5YO2RXYSd5RJsTvuDpKQwGzVP1QXS8MCF67go86CPGAy_mIJQgF8Pfhuyq3jAiHkkiFaOtC2sOO_yD7GYjZt6wsOXJPqKn5REM2eoxJhh7b_VcOdyvoi9O1h0C_TG_vcwdpeAnHHD5gMIzZ9PJwRNKyyi3oGq1Kb6pkkDtJApBFTRyoe95rETEIQjxW9onGWASx2mOA0bdU0-rWRlgmco_-2ee0QHtUXcAqhNxfeowpTiKL3IiHTKwzL7guDy3Ic6aeOB2mjRZJBImJ9PblAuCZnUjFdZNDnb3J3pE525J_jmkJm8pizi1wF5jquINs1q5eMJwGM2lUTKdnag.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.62K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 14:39:06</div>
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
<div class="tg-footer">👁️ 664 · <a href="https://t.me/ArchiveTell/6589" target="_blank">📅 12:31 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 941 · <a href="https://t.me/ArchiveTell/6588" target="_blank">📅 12:10 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 900 · <a href="https://t.me/ArchiveTell/6585" target="_blank">📅 11:00 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 977 · <a href="https://t.me/ArchiveTell/6584" target="_blank">📅 09:43 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 943 · <a href="https://t.me/ArchiveTell/6583" target="_blank">📅 09:41 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 918 · <a href="https://t.me/ArchiveTell/6582" target="_blank">📅 09:16 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/ArchiveTell/6580" target="_blank">📅 08:56 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6579" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/6577" target="_blank">📅 22:06 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/6574" target="_blank">📅 21:44 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/6573" target="_blank">📅 21:01 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/6571" target="_blank">📅 20:41 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/ArchiveTell/6570" target="_blank">📅 20:40 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/ArchiveTell/6569" target="_blank">📅 20:00 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/ArchiveTell/6568" target="_blank">📅 19:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=PyFJoMnug5Amn1C9KEwtlpiMsswG6MPa_WDs6O1h4AMukm98CvB28MIq4hcDXuVrXba33JNz-Eyhvm7lvH-1s6B2DWE_UWuNUVSinQq6cBgs8FGsWD7g2VzCckiwx-xv2bN5-0L5W_tPuCeqeAsyBQ65p5DXEWyL7oewRDgBIzE1vIT2cix0AoheaABMF1WGMhPyccubVQPV2oVIfaXYhx_3U4kJu1g0BAIkBS9NMXLCUHlBeR2j5IFKhhMA-4VGratmrtBBJty9rAR0bNxo2zrHUf19kCVoBJxmrG5VP9gN5h7jDnRI0cLaFMt6VJxkCaaC4vkicrQvNucdJRRtRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=PyFJoMnug5Amn1C9KEwtlpiMsswG6MPa_WDs6O1h4AMukm98CvB28MIq4hcDXuVrXba33JNz-Eyhvm7lvH-1s6B2DWE_UWuNUVSinQq6cBgs8FGsWD7g2VzCckiwx-xv2bN5-0L5W_tPuCeqeAsyBQ65p5DXEWyL7oewRDgBIzE1vIT2cix0AoheaABMF1WGMhPyccubVQPV2oVIfaXYhx_3U4kJu1g0BAIkBS9NMXLCUHlBeR2j5IFKhhMA-4VGratmrtBBJty9rAR0bNxo2zrHUf19kCVoBJxmrG5VP9gN5h7jDnRI0cLaFMt6VJxkCaaC4vkicrQvNucdJRRtRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/6567" target="_blank">📅 18:42 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6566" target="_blank">📅 18:00 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6565" target="_blank">📅 17:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=hgV84XQWc69xbYhopBNLML6fxCzeCeMyHoR8xmG5RGwXs9CM81lEMbmMZgGlbAzbCL9lXK3aFT7lNIdRo17kFn4nJcs-wh86dmYzGL7IY7rkbEGjnjPNsEX5wmb5Qfbs0RYr_EfZFuJRc7jN3edsieTd4R74H7LbgLnXiJxBtPLvKYLgDzrADhAoC4BKtgsF6CcjEr3AXWK3Iknoef1WDx9oycXkWDPc7rsMdSMTtk5pVweZDWvTGONBl4QYzuco6Wcd6zVSAz3iSPReG6QUJyqx2_D3rY71E12Ct4rOCarhC6zyLiIEY6hk4Z85Op1jTi2V8fA7OwKYMFls9NkVgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=hgV84XQWc69xbYhopBNLML6fxCzeCeMyHoR8xmG5RGwXs9CM81lEMbmMZgGlbAzbCL9lXK3aFT7lNIdRo17kFn4nJcs-wh86dmYzGL7IY7rkbEGjnjPNsEX5wmb5Qfbs0RYr_EfZFuJRc7jN3edsieTd4R74H7LbgLnXiJxBtPLvKYLgDzrADhAoC4BKtgsF6CcjEr3AXWK3Iknoef1WDx9oycXkWDPc7rsMdSMTtk5pVweZDWvTGONBl4QYzuco6Wcd6zVSAz3iSPReG6QUJyqx2_D3rY71E12Ct4rOCarhC6zyLiIEY6hk4Z85Op1jTi2V8fA7OwKYMFls9NkVgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮
Morflax Mesh — تصاویر سه‌بعدی در مرورگر
این سرویس امکان ساخت تصاویر سه‌بعدی را در چند ثانیه فراهم می‌کند. عناصر را بکشید و رها کنید، فرمت‌ها را تغییر دهید، رنگ‌ها و نورپردازی را تنظیم کنید — همه چیز مستقیماً در مرورگر کار می‌کند.
تعرفه پایه رایگان است و دانلودهای نامحدود دارد. با پرداخت ۸ دلار در ماه، به کتابخانه سه‌بعدی، خروجی با کیفیت بالا (.jpg و .png) و قالب‌های آماده دسترسی پیدا می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/6564" target="_blank">📅 16:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbUo7gNJcg80hSohzeFc7ntOaOyg0AByr3PXMkhNgyi_NjfsK5cBcqCTU83cWgcdHN7Q4GEJqiaQr7_9YbuI4GCoxumhofUx_qcJyHMSnBRZXaC0Qu4HKn6nik4SVW_fLXERMrv3RDJnYGqoc9yNHCfUqvlGdOmZtM8bqTHcZiXi0eS68t6DByjjHzu9XbOP8lZ27acJP4Pg7voJA_0WNp12G-0Hhzls3woe52n9P9z04DdUo_WqceTk2lOLARCb-ApLjqYouF8efAY3HItA-Oa_THvNbI-t1TKU-7qdqWahIqgLLqNxgeWwympt3Zfqu0JnDomPXSgOf72VZoPKsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/6563" target="_blank">📅 15:42 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/6562" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzJ4ZiPzrk6-2QGkua7cda2K3pRUYYgWCuNpw46YsjK2aIbnsQANGzmvu_gUWN415mttO6yB6vE65TISG9TqRW_j-pgDVpoKzTcrbgVGr9R26iejMCPvcar7xELkUB4-Q6UgZNC_uCEkGIyU_bprrwMr5-I8XZsYcqPAt3ckr8__LaYcwXFHlsorqgVRgCszW3uVoq6Psd4MkPdBMznFhj9G7wvu9FNAmA3SMAfpCav7qy41vewxepErQWp0gOqLTT4YKxDYQrB-QsgLmmN5Ky23qyvTMhjEbfZF0s9BrQibiSRZB40hp2Sq1cWAa7R8l-BiKR71FM8kFR0KSmClFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6561" target="_blank">📅 13:43 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6560" target="_blank">📅 08:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6559">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRB-K27Vp85c1hBSv_fwqq1ld2ql2xwTYnW4DWZl2c7O_MLR1yXMNbfooaVlYUzlm8D28tBSVgQl6qnwYVGGnD4ixaMJgvGMV_Vg1rFPk14U8mCOpv4bUQ2LjPSCEDolYqCyKkSKtCT4xZnJ-sbFGLfaGAkEGCa3Hsqm85vca47RtrT--Nqu3uzA_he_Ljggg_4s_zWB6Lt4iV8XrjHq6DsHo_aww3NsKGHAn7s2QKvzO14ZdTjFxs6JAgVvHXHECFZNZ2TNSSO-73_wzwLnzx2V2JHVAYEuBVE6ygd4xzDHwRi6zlf-YPIFTCweBFJPxMjGFCQlhaMEMgh6GApmlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6559" target="_blank">📅 23:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8491578554.mp4?token=TFjk-7kzwF5vfsRQp2CXCzOOEHFM950WNUyQCEjnGA0w-gOOL-Vawry7AbqPl_W0nuRuALFhabWBX5htiDBYfKlp9kJuqAS1tUKOnF4MXcOCJ6GqO-zwBGrgofjREXYdWoULpCPQX8w0JGl8IxiS2MD-7zzzt3JXD0CGCzUtxPm2qQMx3Vy3lSp_niffaGrAuHEb0jtmGG1uPdb_7VGz2h6DVH6n62PN0jbUiZhKiO9zem5YdBtDq_Pkj_aKZCO7s3a30pbBUycvesCr947tbVQAld3eygNdeaU5D9p9_pcIkg82_x0hX-wjQkrZUK4JDu-r_wW70fqTVxmoYjBw-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8491578554.mp4?token=TFjk-7kzwF5vfsRQp2CXCzOOEHFM950WNUyQCEjnGA0w-gOOL-Vawry7AbqPl_W0nuRuALFhabWBX5htiDBYfKlp9kJuqAS1tUKOnF4MXcOCJ6GqO-zwBGrgofjREXYdWoULpCPQX8w0JGl8IxiS2MD-7zzzt3JXD0CGCzUtxPm2qQMx3Vy3lSp_niffaGrAuHEb0jtmGG1uPdb_7VGz2h6DVH6n62PN0jbUiZhKiO9zem5YdBtDq_Pkj_aKZCO7s3a30pbBUycvesCr947tbVQAld3eygNdeaU5D9p9_pcIkg82_x0hX-wjQkrZUK4JDu-r_wW70fqTVxmoYjBw-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی افزونه Caveman؛ ابزاری برای کاهش شدید مصرف توکن در هوش مصنوعی!
🧠
✨
اگر زیاد با چت‌بات‌های هوش مصنوعی کار می‌کنید و نگران محدودیت پیام‌ها (Limits) یا هزینه‌های مصرف توکن هستید، افزونه کروم Caveman دقیقاً برای شما ساخته شده است! این افزونه کاربردی با…</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6557" target="_blank">📅 22:28 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6556" target="_blank">📅 22:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=GvEG3QjuOmvHwd6x78qkX2qZYaQcK243WKES_EZUyWQe5ZMRfk5V9UyIePoHfckwmHg89gEUqKKAu0rjAMdA4WIx-RWEgUvN6GnLF-ydqxHZBbEaAn2WaovsLn6h_jjHOboshjmyJBEWRll5lTRzx5953362qKlKu7JJLAdaeNe_uxlRbTfdF6KMQh2PIgci5Iqr7xZLTCt_n8PPLpNCDxsbTXLJxpOlaq0WWZU4a9Uru-syT3xzdALF_6XAs_zTIGpD3whJj-yywQQyj-iGfZv0MPQ8onJSsB_kUnNqjvW0oASYv2lFbo7X_og27TwCC9b9Wb-o97mTtuSv84RKJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=GvEG3QjuOmvHwd6x78qkX2qZYaQcK243WKES_EZUyWQe5ZMRfk5V9UyIePoHfckwmHg89gEUqKKAu0rjAMdA4WIx-RWEgUvN6GnLF-ydqxHZBbEaAn2WaovsLn6h_jjHOboshjmyJBEWRll5lTRzx5953362qKlKu7JJLAdaeNe_uxlRbTfdF6KMQh2PIgci5Iqr7xZLTCt_n8PPLpNCDxsbTXLJxpOlaq0WWZU4a9Uru-syT3xzdALF_6XAs_zTIGpD3whJj-yywQQyj-iGfZv0MPQ8onJSsB_kUnNqjvW0oASYv2lFbo7X_og27TwCC9b9Wb-o97mTtuSv84RKJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6555" target="_blank">📅 21:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6554">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZK2gUx36fn8_t9mb_Gp1hL2PJPJ10rnHHHJoBsrvCoGs1YwWzsMk359nDe9Q9jAQwa4e3ea8xv_jjslYDbnWxBUGRfG9i-WaromEZGcRsrf8A1EoOW2ptXGr2oG4bsl4KxtZa325VkEYue57B-dqTQcY3OOAhC7plLFTbCo97MK7iqmh1rbPrP4peOlc92Vt-U7U1LqKzRTaVE5Cy4MSW7vZgkHK6rjGDxf23PVT8ChHCkZ-ll3s69xdGWxiPzcC15qqq_lKp3cAyFasVUE7hKF_jFAnJ6a1is6Zn-71rvEmFLtr_axYsam7wxB8cgliD8ZB6QtM03LzwfC3UQcGzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6554" target="_blank">📅 21:10 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6553" target="_blank">📅 20:36 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6552" target="_blank">📅 14:51 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6550" target="_blank">📅 14:40 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6549" target="_blank">📅 14:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بیایین با عاباس آشنا بشیم
❤️
دیس وگاس و عاباس
😝</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6548" target="_blank">📅 13:30 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/6546" target="_blank">📅 12:07 · 04 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8NvaK6zhFAUS0T-jRG17j85NaQNZ0sALd4Bkv_t60fBSc68ajUYxGFfxamiMZcCmxoCFGCu8y_p8d3NcfApZfR5UFoW3nCN2JG9Qmubuai6A7nxodb4nz2txYitwSVeoQvw6GN5XICwmsFght3VsigwveYb10rdLgnyrnxC9KkqbZwnY6xp_yWXO12MxzArH0V-3T6ycrAcnv5dIqmAJSE5XoS7O-u1d_ezVALVJ8AxxX_B1pxkl_s2R27VEUU1Zv7HSbAJ7wP5mMT1XSZNc2GwSLxxOdB1je8Hu4BBMjO7ko8ye6A1zYsXd1fdvJO2rQEKemEZDtI6k1SHo2KMmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/6540" target="_blank">📅 21:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6536">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ORNE14wA-AVQYgyeC4s4YXfRCHp7HlrljxJitM0KxIKzOV1uKbNu7GQ9UW_yqbTRkHkNqpUBVnQtz4QdFmMJ-Z2HhAX0U-EUP3WviQ9CPe-g6RrKXhMh24sEdzGlH2XuWhfOPmnGtUrd0ZYr4wfHe3lEo5JD-dEjuSSwd996YmKVzyguKo18AMstM0NbwGwahWxzHmn8f6SyyDNON5WsbibKDSl-RMXDe0onOFPYbHORudQze9TJhbvCp_w_xvpOhkxIJJBhilKnZ4q61IdBXgVg369fUxwcodRTWqqY1LRLrXQhhVpTuc8Y8p--Kg115F_BoAVH3tpqqxAcx_4gtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jgD3cg26Lpt6HOwhOtegCcDsP8811ahRSBFA_Kp9DP5CSHAusgkZPspILWZ_JGEKqSjLToq0KNEuzJc0udjqrOVkUqaEuz-jPmZ0_W05VB6w867XCPBMSuQYtDU40pjm8IZ4s0wqpki8p32-bAIvEMW1SIXpvVZ3vZ-pHATZWcbx-JkJOcfl6GAajK5ZGC3mKHb0IufKLhPVgu6TwdjvPWCKx7Q0x_uSrVpiNRMG0MJfnMegJGhEWQfy8IEP-be831GdGdf6MEdHCXsyqSa2RDfGF4tdlmJ1IUG2OhGAtFlc-nt8cq4VloMzAN_pK5Uaxx1j86JispwepNSvPDzmAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_BvoGBrYxhdmNFKzeFcy5pNglx5M6NzcGUIjZsTWSzXMnBIOJpLdmj8m-aALI2zCZ7JG8wKJmkIzfD382LNGA58Je8tfZ96DjtMGLtGfqcd-9a3GGGmy1n0bBDK2TPJJaa2ulrtYhkoYipzMoper9Ja-gBBguwocW8hhumRgjlOj787TrxeFglEuHiixrwnYxYWyVhH7IupV-m6NivM9n6c7C0d0Js9sXCcBB3NA2c1RR2rh9xG648waCkR_XK_xFsHO3EVNsF9NtsQeZ_K4RATa-ImysNf9T4UxIXT8E_iy_KOeZuOCH-17FjbRmXnKx7Di6-eOT-YR1QhhT0XHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aA3AvEpGCz8-XSfw1RmX_ERXsfSXR5zc0kFuocxltxts7BhV7D5kZTZ88fMgX8hul10C5q_343T3TH5XYq1nR_pQUMBSFfyn3EMOGXitk3opMy1qkVP0EOhFQRJid05la5ZLwWr7uM9Ii7PE4Q3RObGWhYD0ftzcrpxRBfETj9gNjdk4ddzUU7CIh7jedu1PXd0Z3q8wdCI4GJNW4Osfpg4ahMVzq1iQqiTseQ6VDUhKRwZErl-DoyiknnZCHHiNvgxtKLsqHwCJo9LprLqwIEl58EzVXIyc_KJ_WA079T3Gn7i-g9TVCHHcjmWVcAQFGWcEvMLjQvRpCI6lqKoYDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6535" target="_blank">📅 18:00 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6534" target="_blank">📅 17:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsFYzuS4xqygZ6quY9896Jg4GRWDWrz0WJPbNALYSkMDMEE5y7R68SLtG15IxQ_WFme2sJ-v8P_XrmCvUzr2J8unuPNlWahQCk2bmCw9iumkVf1R7j-_Su-Q21hMJHZcPE_LBFipovWXZ_uZ2Ep6l86VCLxXLpTEc-hGkTuWT803a1r8UbNiu_gmWf69Ot0Zs6F5RP6Jes5n0kJWRXbyjtrhgXrT-MpR6v6Pf7y6Jk5iymN0iTSt9sh9AXsEfwhBIMtiecGvp8jbdiTIyNIM_LznKb61-D9v6eXjPmoC54udXZKFyWskSLSWOVnXkfAmswJhWB0OQY-ha_2AghrJdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XuW0EVamLR5sxIuVLMzYc5uBnMSUVoAUANRvy2jeucphjQ2hVxrioC7b1M8y7ZiEuJzy9t8EDdsPcISoOzF__teK3GFoXmdmWwF21ZcVqy0520M3V74XyGkCos9KqaTKm49IVBaHpA-GCHokR7zVqYrqgHwymxcCvF4s_9V67X6mxJ5G6hwVKihp9q6QYEeP-l9tB5WTihs2NAdGxAx649mvf5OijZ0gHM6D_5LdNxTIEKT4N_BtIWq2XwWYSnArmvfZS1cnC4TpitMfRmnXJ-6P5y4O00gLibiQn8H2OMAuPYtCPhqKJFF38je0QLS9q4BIWlPm739Bl6-S_x18ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WidES10eHU86k-uW6_oP-wMMq-vzbvW8E3V7KWlvlqAiU2fQsdyB18jpv18JG7pwsVoO2McU6lnE2_wHKjz53jTJsotuEYyEId04uRS8d4-4XHSbV-fh-l_STdYdeZGgbOXyDKTe5V-i2hcDni_cEgbwXAyfmeqW6FWsxHtARwcu0N0YYqbwLVLSaqIv9RtlbmqdmRgTwsQh5gxWQc0FR5D3-zUoAYNAxTE3tjY6QsDgsC9sl3lxIlAwOUUDQZjnY7fajjUo86lKvNCjPCKUozqjvb5yLl6AyRIXi8vlXYD2FQMw_rvBNQcYTUxKX_A6GX_DxUPkApJYO9N8kVg--g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lRhgOrj9wG8_3X9M06gPWizuzukErAcxOvHB5SrbamcqI82K3VScEab-wLQluY5uup91-3keaMk_HeIqylwLV0Eh9pOo81fx2PJiyC1J8RkQyzwITJV5kBUEPP8U_xm2SZmpmWZzdu6bDHiekDAfZ6aShjx6Ic6mZXuFgheambQ2Gft9MNLi1MjWaBEB8zyoeIORGc23qpSPeTzd3RRaXS3NKrlMOkZMXmmWJmlN7FR-peMC5_jWptRhA-A-dAtvFk8gp5iO3L0zcMhJixltH_IRjsTbrHbENVw59MuZUIey62hTG8HguZSazpPc5g8BXy-5D9EYXaXbDx1Ds6hEpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iiVLiecVCXUPRiyGY089Z7suHvfvHBuJjNXwor976FdjC_K5e-ItN6WzVSTOtLCG7UYYXHZuH-nVAroNrleePqqFHy_1m7cgxW-jUF7NUfvGRkH-wCx_B9iwNGBoxBJF5uh63S7duQ33VsDJ665RDaMovJ6Aig4ybBHvxZNIFqqTEV_l0JcVtO6zlMS85XShEpCVXaj3COqNuoxl6rMtmv0Do9kmgIQ2qt5K4Zxxgl1yYCyj0jN3faPPDFMF1ftlgQnLIW06Q7AjjIpesGMnlTnkbujTxyNbzK_obIQ3nEfIpQFwQAxkVwLSCICfLWqPUmAh-fN5WwZ4JYz0TKC66g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X-K9vYJhneB5ESifkmdM2ajrAGsb6Y9XxYNQzNc2nFyrtCB6aTG5kMDvgvR08yimJHi1yiYFxU4HuHmKFOZMfFjryFIwSochzwO_Iza-bxREXW7meCyGPsm2EcTkhium-hxKSY3JQE1s-_d6CcfQF5yUG-fBpvQCmloEr8EeXUCNuzpMCS8-j7mORHRs3P5PlLaVHSrylwhxceag6qrnE8go_74Ffg--EH93xryFRluBjVouSrKOSmgaIb-AhjCvzhIMdohidnZMdTXTo0cpEuehCQfwsWfA66ACC-qBoXn-mXN8rn-0FiXRSsklGGXjszWijxhu2QFUzMFZpBETNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hJ7uYjWqVIUxig1B6Fxff1zWN6aZenbk8JlRsqY2HLDD9iqeLAGainTXUsZpDatEgppcYwg6CeXimQEJsdez3B3IJirmo9RHrW94ixUecxLO0zY1EGzKhG5L41bBN3IjBoyJMT_eCj_ksCCfZGVGqEZQi-AOOd1-WTwW6lkidylp8kJoJuUQkUYZ-fqNm65HXkJAw_56CgmwuHQkg5Gc_ocCMA3cu2f656kud-vV4uCEDoAiKxYH5R0f40wQwvoGxkIMOu3u-TW5N_gFC427xnJ1pizl-7kaXWGvWnEjEzLArl0sDMdtpRjpS_lHPVRPJTMBf1Ha34Ma0VfRfz5eqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر منتشر شده از بازی GTA VI</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6527" target="_blank">📅 14:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6526">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktdONV3uEWIJiXZKFC5HM06Yez3M4EsecaQsNDYZXekxOMGBPy7Hczm5_HcbblsvE7mxw3TPIzmd539lHQj5A83cUn-tqNI2At57Yn5bqg_m7Jo6zRFLl647wYfiBiJAHljjhgWvHK4v5bwOOOZeOeQyAyyhUbfNVgAmlDRfkWRiXlizj1ZP39lxSeHc8VMQ1ougSKzkh1TX_xifTqveH4LIgO9gp3eJZ_5SbtMtkCGYT5Gemzjqq4I5Rp3lnQgU_JX3N17wDe1iA179l-wrK66yshGQDqHC4t_uRGUQD1g5fC2SmT7zLBDXMH4xqW8tJ0d6G6_KNnI9Pjp_L6F2qg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6526" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6523" target="_blank">📅 00:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=a2M9jr09d0lSLu_c5_tjxLYBokJ5oFP-U8-88ciaGuubauny1NCdomgYjf-sc-YTrn8xGDu9rL4jeScQfH6riuEz2VS_XYGUm-0aCVdJoDg1nBy79cmx6zhQEplRi3PB3yI6pCW2RDbKe8CGXoqdxSvjxF0ZH8-lmiv5xN2S9voA4dO0VtibOTJLd-P_8B8o9k7QNq_tQgQrnd25VV0ipM_iM_Op0PvFlMeE0trMqkKNKxeSa_AKRfcqL0HFtk0Dx4PU3Ps6FbtjAOtXStCUPmb0QCh-TWbIRrzHaP_QWU3jvawwEJhLI9oP_XL1ftnl7vDyCm7RGDGf7egK_z6u2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=a2M9jr09d0lSLu_c5_tjxLYBokJ5oFP-U8-88ciaGuubauny1NCdomgYjf-sc-YTrn8xGDu9rL4jeScQfH6riuEz2VS_XYGUm-0aCVdJoDg1nBy79cmx6zhQEplRi3PB3yI6pCW2RDbKe8CGXoqdxSvjxF0ZH8-lmiv5xN2S9voA4dO0VtibOTJLd-P_8B8o9k7QNq_tQgQrnd25VV0ipM_iM_Op0PvFlMeE0trMqkKNKxeSa_AKRfcqL0HFtk0Dx4PU3Ps6FbtjAOtXStCUPmb0QCh-TWbIRrzHaP_QWU3jvawwEJhLI9oP_XL1ftnl7vDyCm7RGDGf7egK_z6u2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش ثبت دامنه برای رندر
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6522" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6521" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUPRZ4COZqkOeYrmwkt6Ixyh9kiYePpVSEodw5yBdT-VtB_tzei3_WG2ypREQE_cDO8lnpHiflxO8j0k1uHE_3CxNapP1eRxQnw0w4hICKcyAobwSN_uZl47F7mK7xpCUnoyRF--ZreX64kfbdEw7S3dFw6vn2fhfUefjDzThb_lN3RoLhD6tGeCiAQ3lRXZX5bUyeSfku0ir-LBKAw3Rjcknt93a-eLfDAc_mSQfahO76cibvR-6EiaDnLmjObzv5K3-mSvUE43KXmxw0ZaUbERjLZmTWcHgWkWWM685tzjgfpy3NiN-ch8QyJNKyry2O8Uc8yBFt_CFGuv0dzCxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6518" target="_blank">📅 21:29 · 02 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_zvDJaIj5i_UG3ZsLkqir2Dgg6eYh21KWV0RrRC9cxoxNQQXTCc0xCfNtayE-a6QouqDLwLldA_fS9EVcFq3cMvpdmzcpiLOQh50m9fXCm_NqZXPgel5XTcPWDTkyUMf7ocoRfLw66fitNrlrg_FRgtupPKl32drA64MF5sekRJGO2GkWg9RxlET71TaByTkzkWe8D5N_cyvjpKqGlnr6NfljutYeTgpqk2GZqAGvALrr-OCIzFsEcpulTWmeDpbl3fXlNovf8PALH7MVz7HTLLJJrrj6EOC3JvgFKAKwwh0ILoJNuHVtpkiCfokLt9LlLeBIHs3IQJ69nkjZgtwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6513" target="_blank">📅 17:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4O1ftkbjltqCvIF9TGc1SWsCmYZ_5GayDgRrgKHwuRCE-ZEQwovGSBFX9V28DsPxtfycwpFkh9dJ7Fh2VvfLibadiKRyE2wvXUmIYPGbBTEfwbgBX1iRNc4YDnmNrRpQRUxNmXedQ3py9WCq9jrNU92w7ZP1RAbCHBkz3VNvsKBll_g2xFYYkmtB_8zHPY-OEBy9OKXbcEJ9ecHTz_q_mQ5weOW0clLVIijAl9A_h7sQtvYFeRFAXpsM-7xoBLk0xXlWgG2KE8wPL4GpEv-DtLUtEuAh3uIXDy8am3k2qyJmFXZ6v_rST0Jol-xUWrO24zZj713Q4KkfECd7zilzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/6512" target="_blank">📅 17:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXWeShBGfkXzS0xXfrj9uOUTCijr1e766EKZ-tx-WqX5epm5Q9RCgzQsJkIClOtrTadhFcJ3P1TLxr6EVjbs9PWgSFcyaHINikiVvPF48fp2upwL00ecOtuP43UB2oNA7R5Tkvq-luD4QRihbcrTO1JOr8c6Yx-7wH2i5ppJFYNNYfDqZxnvLWeGl5KB2yh1NBtILrN0xbhX997AUiMFfglVvKxeyUgPS0BNqk7lnez39c8ErKtvNRbMLT5Rk3z-qY1rphZvpiBl8_OfsJor7XcxcqQW5aMr5T-tfwMberDB2tVKRbQ4kLSbJQi8NSXzYMzOrS_-89Umwqh6d8AnIA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=ToHwH271peQOd-PIkGrArVws6J4FjGY0uLzi5mCZO7pFhVBgGxoCVPfjpzyy9LZnUDDMs5HHclD-fUn3e2vPgPpftslfO-RRfumuPHDVAmnGJcXvfIQ5yyDOA1yUJdUkz4BMjkinDE2wd2maVJCkG62LWOWJnKc2yuY9UJMqcvtdK_T-CyDR_Spi10emLNwJ4-jsnL1GRxSdBde-2YFIUJVhfC6r705-kcVETk9hOVzUM-1jzDorkDOcLecexS8Po1hpCSZ__4ORBWNvnwVkb0_3rzHVkuz3qGCXsaDD0Vvedr_NVGaI6ecCO3C7H8JqhZq2ychzYPDperY2k7RiiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=ToHwH271peQOd-PIkGrArVws6J4FjGY0uLzi5mCZO7pFhVBgGxoCVPfjpzyy9LZnUDDMs5HHclD-fUn3e2vPgPpftslfO-RRfumuPHDVAmnGJcXvfIQ5yyDOA1yUJdUkz4BMjkinDE2wd2maVJCkG62LWOWJnKc2yuY9UJMqcvtdK_T-CyDR_Spi10emLNwJ4-jsnL1GRxSdBde-2YFIUJVhfC6r705-kcVETk9hOVzUM-1jzDorkDOcLecexS8Po1hpCSZ__4ORBWNvnwVkb0_3rzHVkuz3qGCXsaDD0Vvedr_NVGaI6ecCO3C7H8JqhZq2ychzYPDperY2k7RiiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6510" target="_blank">📅 11:09 · 02 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=Nf2aTjC-baWDBNcwSkXTJzGNEHUYHf00aK4LVXO7dKudtbvNdRpIBnMM9QbaIgJ-y-397Qao92J5p6NS467MOFgqN-7JyPAal8odSaJrDVZK5cR2P2fzLTo95GtmNnlZuPIho94RlcHJjmaghYoXbH7-TPUzwxjxjbTCzYAfSEM7uKsUMWfXlmbJ8DddNWRg2bhMGDkafJ86z30pOIoW7thwA3Zgp5RasmeC3GOnE7kDG3SfGl9QlBYrPyXanlrFCNryIPGFpmqxNtWQyQjG-WH-5VbpLk5oyvm3lbbZswo5jKA4Mwl0yzF_kr8-iEoKXdcG0eETWACmVCy8urp-vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=Nf2aTjC-baWDBNcwSkXTJzGNEHUYHf00aK4LVXO7dKudtbvNdRpIBnMM9QbaIgJ-y-397Qao92J5p6NS467MOFgqN-7JyPAal8odSaJrDVZK5cR2P2fzLTo95GtmNnlZuPIho94RlcHJjmaghYoXbH7-TPUzwxjxjbTCzYAfSEM7uKsUMWfXlmbJ8DddNWRg2bhMGDkafJ86z30pOIoW7thwA3Zgp5RasmeC3GOnE7kDG3SfGl9QlBYrPyXanlrFCNryIPGFpmqxNtWQyQjG-WH-5VbpLk5oyvm3lbbZswo5jKA4Mwl0yzF_kr8-iEoKXdcG0eETWACmVCy8urp-vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6508" target="_blank">📅 09:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOx1CnryvRYhdhj9RbH77waPtKRVulBkL6CyMWuf8fcNWeCCsPxf1Do7n5SGsrx071Nq-kwGiq73w5IRpv6u9g3q_TIzZkmDpsHWhWywheh6cvV5kSuJ5ZXt_tI_5jfz-5OWGj8gictKItXvBnXBlq7DqgNCt4IsnTk78mOxGNR73xEy-4uBskLmEFX4N7D8fMfqlqILoOQUhIf6hB6D8whWSYoWT2IY9ksB6es4x-PDimL1ZtoeDZ5diXzDPQjCZDBjwLAru74Wqv9t6X5tiePTRGn_xtiw4gsoc7lmpfZYqjZZrE2NFscDEM40mlekbtB7BzW2ZmE1QxqF5qIXwA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/452211db9f.mp4?token=k8NktzxBTFSoTwU7f9V5gPrg7xjvfCkXVKCWRyjC4oF2Yqs4DN3g5tzTCm197f_ps32bxYeF_FckE_KObM0zngz-eKbenD6A6QqWtHit1ChCba6d1yIBpxzUNJyZDY7kGKy0K06ALJsKEEMMMZtOqf2jo4BxyjAn4rVx3PDIvzGfxrGMtufwgLVwlEFeX4RytKp9kw3itU5rW_-MNTg9rBTK-EtGYMBUfOkdDsret8CjG8msBsi-gVk0bu1E332IJuYMUSaqhi3xXuyfcV3Do-SG2Av9p7mTNF_nx5R1PMnuJ_MQJ7K-WRovojRMPTBNQi1IV8vRM87haAeT4kCmaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452211db9f.mp4?token=k8NktzxBTFSoTwU7f9V5gPrg7xjvfCkXVKCWRyjC4oF2Yqs4DN3g5tzTCm197f_ps32bxYeF_FckE_KObM0zngz-eKbenD6A6QqWtHit1ChCba6d1yIBpxzUNJyZDY7kGKy0K06ALJsKEEMMMZtOqf2jo4BxyjAn4rVx3PDIvzGfxrGMtufwgLVwlEFeX4RytKp9kw3itU5rW_-MNTg9rBTK-EtGYMBUfOkdDsret8CjG8msBsi-gVk0bu1E332IJuYMUSaqhi3xXuyfcV3Do-SG2Av9p7mTNF_nx5R1PMnuJ_MQJ7K-WRovojRMPTBNQi1IV8vRM87haAeT4kCmaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhyM_AXbe45KPxLlK8WiLbEyWs1ksQsoEr-ntBuSum-uvytgOIN7-hl4oUxC71F0GgSHBB9xJ9Gg-6YaLEn60WrD2NZ5-EDgjz04t0mZ-tJJY_5fOt9P_ohTy1fairoIWo7iVMwlJSMllHA9YAzTG6qRm1MgJTB5tQ6gx4DGSOkfn1XVehCV0Sr_UdfyMW3Yy0c8ggPjCYHv9sJttz78SMVYHI8wAcXazskYYZrJnea_hqq88mbC0plaWkj0zCIz6DTw0gMDTdHZI0Iv7K7BSy5_HKfIXKjeMYo0zpaP3Pb8cF4ngqJ_08R7BSWAkecs9h6cz_1niE5AuYtHDlgYog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mes4uP8j4Y7z80UcXofYzDZ_IlUbxUXb1lUelJ62q-N6QHzvCQBhgiMMntLzISZkappiXJv4nMvZCbrkTwjNndK988x64xmqTevOUDT4N7UVmuOCUfSiUEV7lafYCHLG88O2O20iKGxUYHj_SS5eDkGx3RHiAIK57HjghOEkyP9RYlnJiLd-dVxRvLoqpE5KHnl3bKd7Zg91Afz23ktv9f3WtpZUz7AXM-XiZidimslYVS9-oD3f-SSkUprRYYrIBIVtmzwKKzlQxQKj5aftZIXzFeLShAI-oTQZ3WuvL_ou9SjuEwLcXbIWcz6aZ1qWgSv70vwdfT_mIvx-9zxl5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6503" target="_blank">📅 19:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TP72lRtC6pmMFVfAlfkE9zc8PIzYPCdRn6nXtEZX8FnlALh8TMlTnwcrg7GBb-XhYH7LafS23nExGDvHHnlNfUcNx8BYR5MBE3Prz45C0KUkhF40YLJGqJFLVewVch2gF_u7on9liyT5RRvUy_vOi3wbdhEAl65ankPfkJwIQf7e4geZ0i2BIW0OCF3j9XBARsMZyTdcOcqu6_hOpjeQpa1a8Ilox5i2CWxLlle6Hf1q1n2C8jxugmEBps4NmhYeNX-2rdA56acb6PDhFxwq2ef5FcBCca1WP_BYvukO08KdeiOD9xZY_uVvtxit8VCfVTkoMdEvVrmFiTTWzVWTJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vM-Tje4p1Ed-SaHxW1t2IOhuylDXML0Gw9EMKCwhRJoDP7qek-6SS0A6P4M-8eh51SeS_WdKt8zWB870TCCXcwzpBFZOFjocrtkmoTTJyi6vRbP85X8VByfiQ-4aoS63rRZj8oOx1VVdrm8tFBUzMo0nwo2r89N81SzPvMJ5McHvPeSVy1DenzEZiAPXM8QWXnqaEZ5P3mOoTrKIfe8pahVviuA-PqtRTpISROZJUoDYr6-5-Am_-fwxJ-knaFRP75pYTl8634iwd4rd6iCfBW1ELOOvcq84-Lv-xUbhQWN7-kWQawKGogUeb9mQnaQBKxEMYtasQtR3rHr1uKdKKA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=Pn8-SZHOE0OmzmAUkE2wnACxcIMmLy-j67EgLKiRcnncq7fvNyAejNKmb_yx1owI1k8SMV0CLmB08DRs6cvZWvxxpX_v3t9XmHMFZ1v00mLAP0CmyM5B2J-Og2cXvn5L-y7ibMSEI4GQ-ohQ7aTlnTsG0-0h9pfKAeDR1jSkyP5--CCnp7xOfWOiQjVWXCpoUpH3LM7Qa-k3eBch4j2_uMeyIr2ulUseOoYY2ZqWXxDzsFYUvo2TM5XLBOi5YhMEAfmgs2eAFA0MOBXizc2z_jxsDi6MlGBg6k2rw8lUaxykRSev_lmyWkiw1ZqAfMoqTpM-ZLSeIINZ6HcNMcaVIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=Pn8-SZHOE0OmzmAUkE2wnACxcIMmLy-j67EgLKiRcnncq7fvNyAejNKmb_yx1owI1k8SMV0CLmB08DRs6cvZWvxxpX_v3t9XmHMFZ1v00mLAP0CmyM5B2J-Og2cXvn5L-y7ibMSEI4GQ-ohQ7aTlnTsG0-0h9pfKAeDR1jSkyP5--CCnp7xOfWOiQjVWXCpoUpH3LM7Qa-k3eBch4j2_uMeyIr2ulUseOoYY2ZqWXxDzsFYUvo2TM5XLBOi5YhMEAfmgs2eAFA0MOBXizc2z_jxsDi6MlGBg6k2rw8lUaxykRSev_lmyWkiw1ZqAfMoqTpM-ZLSeIINZ6HcNMcaVIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnpGrhxIYabmj-nLGjEJ6c15z7erON8dZiJhzsrCMCwnGFQu333u9zx_ka8mdYFtG-msYwaIdBQ1eu8AYz8zbKCYaikhh95iL9AjBHDAxgjcXLK3rdxe7TbY2gBZXUHN_lwLTYUDnQhSR5MIXDzEVC073lg3-ZKH6vI4VwsnFPdkyTbxUFU5wu9Unra5cmdStkDwsmOPRvqNuDq4JAHKh7pAYzDOzTHQesqBjJ9XmuUquOdcOFHvWKpiNVOp8LkSA6UvLBLh59vHYmC8KGYLLQHSOAp1Wz66wd5uruie8gZ6xuB1TEEOwBUuwd8T9a_iotv80t30WekudutkBeAudQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی Sakana Fugu؛ سیستم چندعاملی (Multi-Agent) که GPT-5.4 و Opus 4.6 را شکست داد!
🤖
✨
شرکت ژاپنی پیشرو در هوش مصنوعی یعنی Sakana AI، به‌تازگی از پرچمدار جدید و تجاری خود با نام Sakana Fugu رونمایی کرد و ثبت‌نام نسخه بتای آن را باز کرده است. این سیستم یک…</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/6495" target="_blank">📅 10:53 · 01 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTDeCo3y3R7VoZGZP_LRnz1ljzrfKelqFGzsugskJBxPWMPGnpX6JwGB5QmXjprSY6q8Uf2uv1z5ugvY_Fdf8cGlytqHSs9AiySkSkDyO9GdkASUUmVUG9v5h8RLTjkqzvQbvDf9vBoDMnAN8hCUXTToo7kMp5rekuPXHfzAKDBHrfWkLur0vN6fWP4MVwzt6jaC8xi61abIt0X_QmOoX2nYx9NSrn-jnHzDmHl8kf3j22D_QYubnvhDaGEBRIzlIQ38DqZuQa5JIM9A8qKwSjQa6NHwiVjVAI7ucn3ow6joF_EFOas8iixNXICrsvcYA34aQx-Z1tEQLScPTd8igg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/6487" target="_blank">📅 21:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OE0dpVYA02o-TlE5HjYRLAOjdibtCHxTtM4r7C7Qj1MjN7MjibYadls-mNSJHZrQl_qHA7lKBp2Q5crNRlIK_lEGt32vuw08ikQFGM9-NvTA3NzS7U-VPy7kBcm24ngEITLHPzL5o_MCW37_oKRbbsmsAsM6wJiafgkipcoCg53Zw01LhGmJ8V_ZHG4sujLqgsYs5d669NqgWpaaHlQWiGcy5FeWfyPWcdsNabEtRz15pAFcdKHZEOjmnmk-eukTW029aF6KlrjoQa-7DRqV8UNC1ylobYivY2mjE7bXA6dydid2HazUFKtwe7pxxaR7zx75NkXd7rt8KauAcgUezA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت What Is This Movie کمک می‌کند با توجه به صحنه‌ها، دیالوگ‌ها، جزئیات داستان یا نشانه‌های بصری دامنه جستجو را محدود کنید و سریع‌تر فیلمی را که نامش را به یاد نمی‌آورید پیدا کنید.
🌐
Site
#Movie
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/6483" target="_blank">📅 19:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6Wjo_f-UoeDQWReHU1fr2_Fn1uLCeTz_OwSm9V7-qnzwcd6QutDWqCiAuw-YjhbPo1DslCcZIxzmpYwPceeI0d1YnCiyTPh9Wx_nWUQngG9fg7htjvIIAjQlSlIJb6YmV-FN_JRBEVJQ5Gxl_M0GMfjUcng1MqINZ7zIBGCFfoJW4N-A6CGGLDKaIErlEYYiYVoPFVcwZ_e833Cn-Kickk14XzD3CrzA42mpADLTAPeNexu6uM04rtyuFo2mqkQ6DXTCQiL33CJy02MSFTS1N21hg3Q8tkp23ZH-y-DduBSJkPo-ns3ee1ZCR5crRWkKsnGAS2HNbREx7qXK_Rq6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLHvxfTlgIFx2D0NlxGlYeAvBfTYCVaJpvu5R9T6EfN65O0milUbzKYcboLyWFwLOaOozS0DYA4KsK4Dp1JgBmtHHoohkBtbT4m7gPnuRBfGE8sdjeWi0iMsCBN6NbRHIeCo23C3sfGOYMXDX9jJsEPk0FyxNNSnqpjkTdktONJo-SZMdVrg-S49dU9NwKkx9R6JX-uXJ1SFSbcEoQI-ln7TzZV5y-2ouhs16_iPNKJ9PMNeeK98PRG3XLe5q8My_tNBBRToMpP5z4ZDRkl22QxSRwjKRgv46U8Ov76kyJ15RZWcjr9Y2UxfqFS5PLrsKjKIbOOqbUsQMYsGToGAyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCog4zgTPd0HGwhm_sjZlvG-ANFAH7CeAIPFTtHuwM5c0zXc1A4JoqX4cRC95PRnmiI0aA2Y6Z2YbEkaGhxKVfJhNGjW4yDjKR7kmcyoDa-ihaN3toyfqBFke5_hLa4UJirA22etID8gtKWBNlKfuq3qX6yBtttlIChOLBTVp9GYAywGmqXB8b4fwvvizjp7G6o1d2dmOQjzAf-gdiu-eY4fUgJG4SXkzER6CsU2XhlmseCK1FNQdZHpuNVCRPqunWncyc_d3FAw4Ll3EnJKXaWoRSCp1X2GSYSfpI01tjqOdznyhfiK7fOz8vPB4gRlXvls808ZtN1WL8ntPwaB7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_-5Yfka8Tv5_WpeO0Zbi8dOmUB5zJ5G7MkFeA5rE0oeuRL4-aap2Xh5s3mgoinrbhgcHR1gD0_Zobjgr8SrdEZrVvMIHmFMqmulkOp85GPcGigrugiYSpDc2EtfE9DM8HLVagUvV4FNVA_Gc1yI_YwkSuhxjTHSuxbRVHcE89cmERNRXr1TAlWLbXrU2zWqj7Ws3-ShgK08cuiJhacBR6fXyINGTdEICbFZgmh8nR6T98zXnr_nIPmCHd5BsET3lVb7tmgl4Q4AmRSpb0nM31fcIiUaMswefyhzVKuGNBUdSIrpjLd9tCWfUkLb55tIQEXvo6jVbH7RFvZFcMNnCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/6477" target="_blank">📅 10:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6476">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=Nl_NRMjnylTM-1Fs5nBg_qO-OSkTs2HY9JMm8Xxxe75I9QM2Ljs1xJ8oKJxVW2CAQxm-qm8odTktU66Ihwx7LVRBz5dJlNq5kAxmCyGAyyimjyRE9EAHEwEErVhNf_pqoxqshlhvC4__Rj-CE-inAMPxtjlCXNHUFf5cb69l0KyZ4DHYAHrLL_DqZCoRVcNJYYlzdLax5AZbCs96cbS6F9qB1Z-b0LRJdtUqsTThO2ZgIdVFMmYL0x0tmZ7szQfMhKDlJNvGS6-me7wEGu5JiAFMXH3QeXXyVs_HDIcYp4wqUQUULuOlscCvz50sOj21lVZKq_vrFUHH4HYfno22VA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=Nl_NRMjnylTM-1Fs5nBg_qO-OSkTs2HY9JMm8Xxxe75I9QM2Ljs1xJ8oKJxVW2CAQxm-qm8odTktU66Ihwx7LVRBz5dJlNq5kAxmCyGAyyimjyRE9EAHEwEErVhNf_pqoxqshlhvC4__Rj-CE-inAMPxtjlCXNHUFf5cb69l0KyZ4DHYAHrLL_DqZCoRVcNJYYlzdLax5AZbCs96cbS6F9qB1Z-b0LRJdtUqsTThO2ZgIdVFMmYL0x0tmZ7szQfMhKDlJNvGS6-me7wEGu5JiAFMXH3QeXXyVs_HDIcYp4wqUQUULuOlscCvz50sOj21lVZKq_vrFUHH4HYfno22VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_THsbPsT75Mj-thtOF_px6cU7KZ40L2_Jq82fPc5oBI2knwsm-GcGkJJjuPPXCPXLSHuk0OVouDA5A_hlE0rBnbHJitYKR2Nf6dyT2z_0K9UQeQq1p5zQdEy0pjfPVo-K8Su5n7v9B_ie3MbtgODJArBnP1OGCHfJJwZ7pTty5pOXsH4zA2zmAgOSC3FOBtva-ICup7DfFA5zBN-scD_obFQwTFBrqSAhuK6PAsRx9QrqtqUNCEVPPnSDDZscmpdlYrsYc-jl3rfvMzQgU-Ea1fEIKPaMY44vRmhBvul7EWUmjNpMHoYDbKh9IYVSYQl0SIuHwJ4nSerAfOgH98Vw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjG9_21DLS_FRIfhpMGbIPR_PUM2lf0zR-HfeF3DffAj_mRQ3-EsXJLYUFqk0CQFyn_lCRF2uAIvuKgUyxXKz7lhOaXgkoEd-dcGLyhJBnJAlulm1s6tgfMn8LwBDMU8SeQfJOfK5AkXw2xdXZV1ODb-HmTUc37WAeCfMCED3PFtKGQuhh59WzEX7LgJbSZQiS0b0XqKFkWAmkAb1uTkNXKubB3cuA4Brkhc5FZhoish1oXyTw1Wm3XjD7kHmtpaRtnBwvroK_DnzCb1lHNdtyoLIM485Bw6dCYXEPXnQFcc6LhWGkt9qvhfw4ZPbjgvLQa9A2Ay1C6OfcPn56dsTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zd76Z5KN4HA4l-SCEQY-NeXMEXmTkJKVtwUXPhDkWagYDqRU-8tU65vK2pUm57vMDY4q9f3sPjndDA3A8EnOLJ1ze6RxZptwLc2Mh1JKIiWx-rt1sh4KsddCCb0p5GjcIPJiZxN-Tk-TslEVbI_TMyTdRa2mj8eDzR8VZZhx_eOOVt5hJ09wEI8jmpJkLg78BwWWM-GNoFSbBen7M1p6LdgfAQdUz2jZQ-9hl_xUHzE4V4dNJSFz7e1h31RqCEzI81VvFzJPC3hDHlBbq_8Bb7rO0jiF3D9PWXm62R6JmL9V4aLHd-raD0uUQ1mI-mxpO7B-Ted8Z73vXXTqf_Pgjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePGlbRppHS3c-H6TzXiFPCwu5HJsNHSRjHw43h72TScaREWqIQdlIBR-qRy5n6qXfuBrgQLZGjmRjNww4Cokl82Va0_X9v8N5ggOknRC7p8wXNc8poNnqx0D8GBGvCuhvZkVCgTqlHazZE0nNNEFI4JLC3dIn0mVYPqN_8N55V6k-oq1RuxEBgXp3AvBffWnXLX_JvzLC5_MDPc7BFOrOLCI2Vfs2f8slvVtyn-ya7Kl7BV05ZMwjhqy6oxxrIpa2j-xsfuxnNep3opI55IdgGMXw2Z-OA9vUplSerCZ4mRiUOx-F_683zhl-q0JL9PIwpy6kVtNtjPSLo0WxfQkVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tlaai_U7SqtZu0l6hNhMG_wlvnrgs2K3U3fQxqfARnHK-myIRB3yM2dmG0QfITLOmxssin3HvbKGOeMlO3alIODZ0h-tXflka0NuxK7tiEpCTkY9l6VBkOVCF6cXydpkXvaAxYQkgTJonwhn00HsbFejg5pVpEMoiO8Bw5u1c91ElKQ24-wPRA-WWK5z1HkyGxotnOJtiHXvK4I5BlRrdapeL8msmQ74vQtyIhdovSg-xUDcgTim1ZRRjaY4dTZF0SzFUcknLyC0lIEFAGPiGDYLnQiGckfXYHBg-sVNpRNIhSPK5y0G5CKdvij9vONA_VzB87OWXPuZEHfHItc8cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QlApr_SdrMb90Yk2Th35IkB3_xEuo0edwbS77mKF58zgjmNJ-6c3rJB-oyI9wtUazl6M-zpcRwnWJYi-rxRR2D_96r1x_fNGrBfJiqTYxQyyExlaaWv5cjD2XepFBdMwhMrQbx8XRFf1tpJJRu6GNFwJOsI1ZUy7m8dkvHRbqboo_Hzv8iQUlfYd4IfMVE-WQuMAR7E_kbhkxaeu80cBlir6eC_ffKAXEGC9rxBD6uzC0QNkQAA1QkefmObFWkJNJP45NkFZfkCvo2K-F49klOYyKqNx8Uw81l7OaleMLuJOZAd6AnWcei3PzAV-XmpG_TDFBBvdeE2AtFFAKjQ_nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pA1vmUZfsz7xAPZopCnyTcjAU2isnu2-yHWM4k01ZTu9cXXPWrXvrJV3B3BvCVdVsnkiWhEa2FSviOaNBUmCfMY4ViT-a7wOo4zanEAyhTvEHjdyEbR56dhsdJGOM14G2kXc_JcOhCHRoJ1K1EYwZ8vivZGXXFV9pMVjrEALW4NYiFEErNracz_Hpkg9AApYaQ0VEQqi74stUtyKIuuDRkRM4g4WUKaufx5DYIiJPyNLGdnjQIaHRtxH9LD5qn9jDfEaVRRROtYsbkUk1XIBbWKOO4gTD2pRC33j61eGSMztP0EmEc9e6jvTG3_orrl-ODF60I6C7cNuzt-aN9EoxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ENremuiHR3xwSJQHlAoQtOxsc9wdniyYm4dYysGvodwGNIVopwXCOPq3a6ESBpy49NLRWOTBraLdv-BNkJ6mAkNxOM86MnZShS9dHl6dgRJEfIr4aa9lBsdCjt7R-q-24ojP7nBUjAbA3-W6JTN8stBgwdNo9B-NLtjhhBmcG6rjXCrtRmSrlGJ5VPvZDI0lFicru5NsBOCWp86cmQZS8Jkl6o7h_2rC_vBdDnv-C1EXcyk4y3PeNvASqR-pZb6nBWxVRj70HmyV6-_DnI49NKbqmiL4BWmqZhyQXC0H0r4po-UdmgUsZXCh4Hop5OPmU69mtBn_ObBm3NJKHBxopQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/6463" target="_blank">📅 16:31 · 30 Khordad 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iVleYkLWp8c2qkbC5f0oN7gJ4taCVa-T6pgq9xTmH7WJ71YgrJqt7rHO-UiFDV_eNGSqYBLGLOa2zGLAk5Px1eafChWMpjEuWmpS7pednzBX5jE5KaaFQUTmwv9RLplBCRVjnVGosw08TW7caGT9bMNn85bbqf9dx6ZKJj3210ZDlHuHaXEEvszaqT2ecOf_XrBeM-4WhlX6lup01X-EI6UZ-EO2lgEw8U3j8bHnFegeL9o7IPopkTbJStGMQCFlin_HsY7I_8G55cP8eSvoopJEsYbdju2Hi1soWXmAOvCUDGbYawn3I7dp-PpBgExuRwJ5aLC7I4nZPHh9AMn4iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IiYpgh80uadVKqRAMRMSv1NlCTZFdpnREMHo_PNikI7udHyaYxykJjh1j_fEjvkgfFZtZnPzFlIYlIcPGrPFHFYatK7PqyTrRApBYWFQ1yVbORpLirzRxtVNfVnOpB-Ylk2uU5wx2NfeetvGQFdwvk9Wfo0Cwsr23WUAN6qvbZdFgUc8JEVEg8SCuBjU-1tmmIH7zNK3nSoBZNc3XMrFGl1Lya1B27iw1pK9HB7cGDwnLdzSErN_RPDJ14rJoHLjuNjD-a_cimDMKdsr30ZwKJfFWDFvPykEqMTydSo38WSVfU-0gkwJVrQ4tbbZm_pbECAexyPsdu9fluLERUiigQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rk4hnqVorzAwVAiQ3AEa66_Iy9BO5-5N_Yiax_eurLwtFZ9xPVCpizmZtTsfp6cCawo1KfiXXQ5tlW7CudkJuVCQvhV_C12OHclyjHqy5Zi8DE_VNYYZiUTAMpZpz0pt8rRYgs7smTrpAj_BFNeFd4kglBFhAh8CygsOsjcLKuv5HvVBUoPGP4VdyHDxv77H0nTiY_ndm2YV3ReX_weHuW2AkW6SwzJV1wn4zn31QPNohl7V09UVSdEjW8bBa9xQ8TvwhleRhRquRM6RAf7hUvVYSLVQHj2OzthQbIQ6uaQ-I9OZGRDmOgfjO7VVqzQ6h43OgpY8ufQs97AevSZY9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qOsA88_PWuVM6o6GNfUo-lUjbDxmZrS5h9dJrKi6qH9JyS36ukDRrMMeOAlWIefgt1yMMjeeebxBTFMX3lhFuniR5AUj-77wJtUNsPXFZym7kyrbiKPJEsu4M0to4IGo_IQNoLI_MUIzix0X9wCFy6Aj1f4ztgM72w8hDStynikNsolVb5VV6e5V6nFy11LvOIXEs89fn5tLCAyRqgA5ZjaSCjKbXjnSA-QKqlK5vj6QR9czJe_kTa8D3NOosqyRcN_vmOmZ8wrzG-8F9XJErft-ysGfTKDdkbIUIbd5l3AmQHEZlQGa0YGKbuTFHIQU8h02Qpf2Jmup4qhNHSbLOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ded905356.mp4?token=BKAXrs9ClBfshNsDtIHFJcvwKeX4ajMtOh1zAUl1npttzSngVCYhipiP-6PkfeKJ1yNnX-uWtAHdHYnbsmxyPJoGLemEKzhPzceyXPiFTa49NcQBKpzpuAYDKa832Ead-XrIsEo7jaq0vUttMPMPFMzES5ULWSl75yXB_FrEL71fNxf1SLJtNFpqmfXhd28V3XFht1lMHinG8OeEknS1P1xCqzgbq4Yw4tI-W0le55gbLCCyfOqLskNLqEiBmATYpU-5ILhlS9zLvKQhU2h9DhBncleq3-YyNXuHyosWXRkBZ21jwgJoi-SajB7MRnAarfGqQNJTHMngjffXgm7ccg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ded905356.mp4?token=BKAXrs9ClBfshNsDtIHFJcvwKeX4ajMtOh1zAUl1npttzSngVCYhipiP-6PkfeKJ1yNnX-uWtAHdHYnbsmxyPJoGLemEKzhPzceyXPiFTa49NcQBKpzpuAYDKa832Ead-XrIsEo7jaq0vUttMPMPFMzES5ULWSl75yXB_FrEL71fNxf1SLJtNFpqmfXhd28V3XFht1lMHinG8OeEknS1P1xCqzgbq4Yw4tI-W0le55gbLCCyfOqLskNLqEiBmATYpU-5ILhlS9zLvKQhU2h9DhBncleq3-YyNXuHyosWXRkBZ21jwgJoi-SajB7MRnAarfGqQNJTHMngjffXgm7ccg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFMWuki_-Prk9qJEmwKcOnHF3t69A59xUPkPIWQQS9KMx-q5biIcRy-52mZgi4DzFD5FL_r6SwUzXFL4bfm-yFv8oYdtmcT39Vo8gQ13BY6kSMDlYQvYxsOfgL15SCnyY6PRvHgqEEps7lZ4cJ1nmoErA9I-LsKBRwwO9rzhK2SVdHBvYtnacHnO_WaVgUbGl4i49q8aDdu4BTaKpWL3aBTtgLO9Dd6Ea8EuBvlh8m7KO_qJwCxvNmc90h0VLntkStLLh3ZuG8m9yohtMlkMa9kIUzhUZVr3Tv8E0BxdMbk-Z7YXQlIEaFeOb6VyrAzxRHpwol3qa-YDEhBqMFKLPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7scGDhLZTzqXKs7l5wg1NX37MkLF7Oo1CAwLi2wd6bu09ufxZvi9Z1ql6kVE_S2ZvMlYkD-ckSWvAXbWwos4aFFqGZ6MA4856I6N2inTZaYTKL5hRD8iyfwifWrqWouwIK2OJViNuF6VhOuSXcrZR5_SzApAcJHbIAq9OpD_OG7-sGEp514pJOXqwak_1woxKEab16xNzDcJMto93JBHKwcuhuMRAZ1ATPJmWceQMt1dts8G7-NH5q-xHP133Qh3UZmJhV9yPElD5dWBKgj2BE5SSbdsAZLchBev8EErCltHuZGPIL8niGPdIqbPTQvBYh09sIXNmA-oW9NaRekLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q7GVd88h-tUTnHecWQu1nxR0rdyzqocCOeStDTgok4C3nnFQb8L1BhJ2TXIHsFx736HLGbOA4kh4J1eToWZ_MCsLZATj7DnfXLQxX3012Mp59C19v9ovlH7e3loUD6x6YMjHcVT2O1qIktRQMk85tctwpDvm-J8OAoqjWJVM4t2_UphrumRWKa5BPxDHWKYh6cB03zRmZ6JyvQV8wFHPUvRkDqoqDYZxQ0V-Hn9DFN0cB3i4q2hpvK707lGoFe2cWgNsHgYe7qpCnQYPEqbl-tKexS2qOvW9SLoKeDb1euy3CYFJzvVhraRR4Y5P29L-fHdAkf0hxiQjYqnW8jOyVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jm71mr8DoVjlHT3fk9CEkxxlrJFV902Xt_H3vfX5waQx7iqURLB6DWpxE8cGcvGwEvRuBbNQEzSewrvAhix7Nzt5th255vj2kWtIYFp6DOf8yIcvyZWTfYGjPbJXQdzw7A9yXOablZYzQ4Z0YuvrkrByOaei3peAsxrWNXumCkkFZCfCovtbJ82gkE3BOdRBDmZwHW1npUxKAx1ZwM9pvcOzuKmiDRRW9SUjJbrH0L6AlXGpghtH7V-AUh-3erEf0fS_heKrsn2KfDnP9Ph-bA2lcEIC2vrW9JUT70wYX_30_fqIPqySrisx7ZAEEIvYqfh9RF4kHPUKNhdpxbbMHQ.jpg" alt="photo" loading="lazy"/></div>
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
