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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 16:19:14</div>
<hr>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrlqEimApmEYJ6iLCDNnv0YayyHUio0T-CMs1XMmFcsuiXKJQNGhpw_v308YK6nNyKU63-r1Jv0ma3l89391_ZdAickiAlRxd0UN11_IQTd7edUR0uq2a7tYNgWC1R-0RpNG4MJLuTGo2O5YHpY7W4_btcp7rujuffR-K9vNWXS8AMyCpVe-rxBuJ4qq6SC5DuLYUFtNp5ppzhbU2SiG0yWTin5Kd9pzzMWEoBUdVidYUrZGrmagd7Fd3uYBg6En_qiUaWLtJZR4pTD-D9TsahXXX60BrqDEMPn-EV09giIlCoHhnw6NGBAJN2DU6PLx7uYEW9oDfm7u0gSUbeiWcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابلیت ست کردن پراکسی لوکال
خیلیم ساده
مرورگر باحالیه
🔥</div>
<div class="tg-footer">👁️ 313 · <a href="https://t.me/ArchiveTell/6593" target="_blank">📅 15:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQU5qKeBbh7R_VS8stSIC7JUkgA--4rs4epVtHJvRccE_4dvpotoS-jYm1gzRiDJabCFBjcuRRKhnreCOYnofBEQrySZIZZHkI2V-mMrllcBwAkINSt3VZt8zrPKMPtJFgGjpWFObtPyY5ZkvDoN6bJLScMR-0Oc18KFre_3C0CN2mfSXqqVIdCDneZKLKuSYRw9CeRwwMCLvQyvCfA6TJeggwup6dMHJcQl3w2jNABMTFp-vvwa7kHVIV1tRvxa_7j_1Qqgxq4EKxrPYAyz3Mh1nejyb4hrx2IpAsaBYSlpdnU5EuqU_MuOIP_tS5AnG6NVNbBBoivx8Oc3bo7d7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی مرورگر Solipsism؛ وب‌گردی با طراحی منحصربه‌فرد و متمرکز بر حریم خصوصی!
📱
✨
اگر از ظاهر تکراری مرورگرهای موبایل خسته شده‌اید و به دنبال مرورگری خاص، قابل شخصی‌سازی و امن می‌گردید، اپلیکیشن Solipsism یک شاهکار در طراحی رابط کاربری است. این مرورگر اندرویدی…</div>
<div class="tg-footer">👁️ 381 · <a href="https://t.me/ArchiveTell/6591" target="_blank">📅 15:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚀
معرفی مرورگر Solipsism؛ وب‌گردی با طراحی منحصربه‌فرد و متمرکز بر حریم خصوصی!
📱
✨
اگر از ظاهر تکراری مرورگرهای موبایل خسته شده‌اید و به دنبال مرورگری خاص، قابل شخصی‌سازی و امن می‌گردید، اپلیکیشن
Solipsism
یک شاهکار در طراحی رابط کاربری است. این مرورگر اندرویدی با ایده خلاقانه "Rail-first" تمام کنترل‌ها و نوار آدرس را به جای بالا یا پایین، در یک نوار کناری (سمت چپ یا راست) قرار می‌دهد تا کار با گوشی‌های بزرگ با یک دست بسیار راحت‌تر شود.
🔥
ویژگی‌های شگفت‌انگیز این مرورگر:
1️⃣
طراحی نوآورانه (Rail-first):
قرارگیری منوها در نوار کناری با قابلیت تنظیم اندازه (از کوچک تا Super Compact) متناسب با اندازه دست و صفحه نمایش شما.
2️⃣
زبان طراحی Material 3:
رابط کاربری بسیار زیبا با گوشه‌های گرد، انیمیشن‌های روان، سایه‌ها و قابلیت هماهنگ‌سازی رنگ‌ها با تم سیستم‌عامل اندروید.
3️⃣
ابزارهای قدرتمند حریم خصوصی:
دارای مسدودکننده تبلیغات (Ad Blocker)، وب‌گردی ناشناس، کنترل کوکی‌ها و WebRTC، پاک کردن خودکار داده‌ها هنگام خروج، و یک قابلیت بی‌نظیر به نام
Decoy Mode
(تولید تاریخچه وب‌گردی جعلی برای محافظت از حریم خصوصی!).
4️⃣
امکانات کاربردی و سریع:
دارای اسکنر QR داخلی، قابلیت نصب مستقیم وب‌سایت‌ها به عنوان اپلیکیشن (PWA)، پخش تمام‌صفحه و بدون مزاحمت ویدیوها و ابزار دانلود حرفه‌ای.
5️⃣
صفحه خانگی شخصی‌سازی‌شده:
امکان تغییر والپیپر هوم‌پیج یا تنظیم آن روی حالت کاملاً تاریک و بی‌صدا.
﻿
⚡️
این مرورگر سبک که بر پایه WebView اندروید ساخته شده، تجربه‌ای کاملاً متفاوت، سریع و مدرن از وب‌گردی را به شما ارائه می‌دهد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Solipsism
#Android
#Browser
#Privacy
#Material3
#AdBlocker
#WebDevelopment
#MobileApp
#TechTools
──────────────────────────────</div>
<div class="tg-footer">👁️ 377 · <a href="https://t.me/ArchiveTell/6590" target="_blank">📅 15:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 919 · <a href="https://t.me/ArchiveTell/6589" target="_blank">📅 12:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/ArchiveTell/6588" target="_blank">📅 12:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/ArchiveTell/6585" target="_blank">📅 11:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTKvlFoUPBA4nauUNmDr0lyU1y8F_SkQgQsC6nk6xel20NOPzx13-Z3d9Ak8i5XOmIOURr3n2b_xn2xCMkoPpUFFJOaZeO1rxEq47rvt0VYa_8UHOZQ5b5Ovxsa1w8pr3wepHv84-m7YqjxLXVSxKCkxBVEU8inGbOpuwsjQcsE62J9wdYCq8hglXY_R65W_hWHvf-PhQbaH4oi3EUgAO63tc24TyARFZNUCfBqLeTfC_GNzLhOxVqwfZTAQRVU9kEkS7Rp8UOMASklbAzSuTQoqpqFdXny9_TPLaB4ItfHEKQ_LpfHlDC3yDE2ISAxn0M_z2J-nuOtEgDR9SH3T4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه Orcafile دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما…</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/ArchiveTell/6584" target="_blank">📅 09:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/ArchiveTell/6583" target="_blank">📅 09:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/ArchiveTell/6582" target="_blank">📅 09:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/ArchiveTell/6580" target="_blank">📅 08:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6579" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6577">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/6577" target="_blank">📅 22:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/6574" target="_blank">📅 21:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/6573" target="_blank">📅 21:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/6571" target="_blank">📅 20:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/ArchiveTell/6570" target="_blank">📅 20:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/6569" target="_blank">📅 20:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/6568" target="_blank">📅 19:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=v80J5P1_6hMWiYeZLioJT3ZqdXjLCrUK2Z_zNoNahreqU9EkSTS4NQKfzQ8aIK0LFD_S5J2jJMmv_tboZpSWTx65Q8vm5hYQwQzG5j7F0RAmEhXDCGSSMrfCD1nMglaVjAW0pBgxLhaA88kLdRTp0ig7aggTNZJQpEqOZ4Drxhcjm2UlZvRRAOBu0dmavrR2Hhs6gCTOXEVw-aLZ43cJVl8kpQYKa-dXAbdnceTY2fTlceJJGYzU1Nul6Z2i5hSZjOeUWND8ZkY-oBI3yjfed1iiAK5GIcx5n2yWs4uTG7VwMdLa5kRa-gIeQCv_xFn6knDeVLDZHB_SZfRw32oX8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=v80J5P1_6hMWiYeZLioJT3ZqdXjLCrUK2Z_zNoNahreqU9EkSTS4NQKfzQ8aIK0LFD_S5J2jJMmv_tboZpSWTx65Q8vm5hYQwQzG5j7F0RAmEhXDCGSSMrfCD1nMglaVjAW0pBgxLhaA88kLdRTp0ig7aggTNZJQpEqOZ4Drxhcjm2UlZvRRAOBu0dmavrR2Hhs6gCTOXEVw-aLZ43cJVl8kpQYKa-dXAbdnceTY2fTlceJJGYzU1Nul6Z2i5hSZjOeUWND8ZkY-oBI3yjfed1iiAK5GIcx5n2yWs4uTG7VwMdLa5kRa-gIeQCv_xFn6knDeVLDZHB_SZfRw32oX8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/6567" target="_blank">📅 18:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6566" target="_blank">📅 18:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6565" target="_blank">📅 17:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=tUy8MP7af72Qudg2mpIhr6NwHAptwkLhw-usd-WtrEwV_wcAls1Q3pAC50o9PQ2bbi6RYEksGhMhnAbbgHlikXhJDH4W4QNLViQfGQQLp3ir6eZ8QI0W_wkqaCLExOqGMSQZEPKyzAB45DpycPbRoAfjMJK2HyivCAplXLnq6oESwtMpMapBMBXuNl2Vo6-KCgl0Etn3r4y9gOI37wI7xgngAA_JKU72HRcUvzgzpV6NYMU-tH0JfkmstBBJYACvj08OP67GqX2KHqko96fYVay6kYGv-hr5tZW_o0kYVBNYyxY2yFWTCai1pHVmMd5F20XvCtzm0zrvCccIYnuITw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=tUy8MP7af72Qudg2mpIhr6NwHAptwkLhw-usd-WtrEwV_wcAls1Q3pAC50o9PQ2bbi6RYEksGhMhnAbbgHlikXhJDH4W4QNLViQfGQQLp3ir6eZ8QI0W_wkqaCLExOqGMSQZEPKyzAB45DpycPbRoAfjMJK2HyivCAplXLnq6oESwtMpMapBMBXuNl2Vo6-KCgl0Etn3r4y9gOI37wI7xgngAA_JKU72HRcUvzgzpV6NYMU-tH0JfkmstBBJYACvj08OP67GqX2KHqko96fYVay6kYGv-hr5tZW_o0kYVBNYyxY2yFWTCai1pHVmMd5F20XvCtzm0zrvCccIYnuITw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮
Morflax Mesh — تصاویر سه‌بعدی در مرورگر
این سرویس امکان ساخت تصاویر سه‌بعدی را در چند ثانیه فراهم می‌کند. عناصر را بکشید و رها کنید، فرمت‌ها را تغییر دهید، رنگ‌ها و نورپردازی را تنظیم کنید — همه چیز مستقیماً در مرورگر کار می‌کند.
تعرفه پایه رایگان است و دانلودهای نامحدود دارد. با پرداخت ۸ دلار در ماه، به کتابخانه سه‌بعدی، خروجی با کیفیت بالا (.jpg و .png) و قالب‌های آماده دسترسی پیدا می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6564" target="_blank">📅 16:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGGEml-bxUwEwMSdsrVE-UJQUNKwbGQ1m0YQfXAD4rrWr4Aw-tqzFRWEvno5VGeYOJX9JQ-bEQSVP75gFetEetdNrKvnjXb5-uDSqMRPLza-arZigi5QbIotBhdSwf7kOBscTm_nfkPnn7TIh5I2AtpASr7SrSoOO2CoT4syptwJXyZevQ0r_0hUMhBtQPsbNLHuIcmHmFCGdQPDdEjKVfMRH7H1UMEneYLa8YQ6_Gc6UXEHaYuANk7X1c8yRpOyWEDiBEzqtJVk9ugUb0lFoTfzg9kynGQAykmEgMrAYNtBtUv68kFzL6YOrWlRkaGoLSCSNENNmODrpQBCWF5eWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/6563" target="_blank">📅 15:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/6562" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cllaXyCLIdothIVowuQN5mGGXJfdvY09b_mE-TN3xma98MRJvHOE2N1HDRgcz1P4cTlyFi7vpdmsZywq9vonzhF0vpZjzGbY1xnDQTn1Y-4GPPfge992jqsCPlmv3kCViwY_m-1RmQU0SH1FbAp3SNS49IFOXf6_d-PnbYYLMzegzkuTcy2ZM6vFMKC8AMlPbICRIV1NyRBPzriJTGWuIPBpHw3ZOlcvCYwo8gp1tKNIYV_y21aSlaKinIVmi_I0entn2KKghsx4CF4_cwh5fn-Vxbt3gUDXOjE1ulZG48ojdB6a8ScjFAcICo5FbbS5UsrGgsOCccdfQsmH-MwlAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/6561" target="_blank">📅 13:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6560" target="_blank">📅 08:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6559">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9lE9qci0W53hKB6mXfr0uDGxReXHlE4O4O1UvVBH1QI8hSSu4k-fsR94xNYiBj0OwqVeYbDEkQs0WxujDHGWf5xxxU9Z-IRjTTphVf0VJHZlbqjRUzjVl3KP1CuqzJ0DPhGFvYTp7IWPKoES405Zlxh4NiihAvSBXY6tl78LVsy2WFVRK4VHmg4eY_aBK7uo4nV5bopd8tUgpTd1hdV2sfOc2zOBkRRT2NBxkNX5kGqlIUHNJW-wOs1LvTgMB7OW2GUldq5jr3GmZDXs-IgUnHR9PW83r_NNehkgWkENR18nbFNpnB8lljSDeSSzTpc3ycMg4i9dRYmATDYGXPLkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6559" target="_blank">📅 23:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8491578554.mp4?token=cTGOyUNI7L_-isHKnZo2Debp710neVMj7bBHnR-xt2qV0BSUM3hLbS9c2c9-12CFX9e-ftpS7T5Y-hVZDeB3BCX936Bv8rE1aKppLhAPzXyS4sID-xzTcX75bMa14kEJiitskQ9prCHwRGtBoFEqvDmLILabikBJ3py0Jz69NXnVOo0kktn0y4-ktJKwxIeg5Rw3qDx6TmEtj8J5UwRZGJ4XHeqQ9p43VTkRVZqjjuzSl15N8exXgvSIu-wmHf7Bzx3mI7fggEaPN6Ro0MEbsGmAUj442fSjF08U1FLRquRhcwstPwkzQvjBZcHGVJ4ZuumloOUMPSqThUVBbhb6cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8491578554.mp4?token=cTGOyUNI7L_-isHKnZo2Debp710neVMj7bBHnR-xt2qV0BSUM3hLbS9c2c9-12CFX9e-ftpS7T5Y-hVZDeB3BCX936Bv8rE1aKppLhAPzXyS4sID-xzTcX75bMa14kEJiitskQ9prCHwRGtBoFEqvDmLILabikBJ3py0Jz69NXnVOo0kktn0y4-ktJKwxIeg5Rw3qDx6TmEtj8J5UwRZGJ4XHeqQ9p43VTkRVZqjjuzSl15N8exXgvSIu-wmHf7Bzx3mI7fggEaPN6Ro0MEbsGmAUj442fSjF08U1FLRquRhcwstPwkzQvjBZcHGVJ4ZuumloOUMPSqThUVBbhb6cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی افزونه Caveman؛ ابزاری برای کاهش شدید مصرف توکن در هوش مصنوعی!
🧠
✨
اگر زیاد با چت‌بات‌های هوش مصنوعی کار می‌کنید و نگران محدودیت پیام‌ها (Limits) یا هزینه‌های مصرف توکن هستید، افزونه کروم Caveman دقیقاً برای شما ساخته شده است! این افزونه کاربردی با…</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6557" target="_blank">📅 22:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6556">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6556" target="_blank">📅 22:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=SKxcMuxfljXoM9j3ZT7barDFayEL-v74LksY2MMTclHR5smUFchClw8uoiWt_2Lb5Wg7BQeW6bHWezjTB56gafIscDhHyvKyN9Gtu-4Ds115CSUhpjmRdqSS5VgTLJ4ktLSvnNC8tn8madJ1HQOwWguEASy_hUbezS4BhSMI0ElERRwX31XDB3SENxmoYLMA3Zv0zun4P65NT2RpAL2KeR3GUhfEIN9IXSYd6oZcB3_2eozliktiZRwZSWnHULFd8EHf9oDJkr5wTY3C4aRc3CL56r5evghlUm6L4evIoPkpY2GyhksRKWzxOwlwhRIQUYPGnKWe3wFzOgxJUZskuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=SKxcMuxfljXoM9j3ZT7barDFayEL-v74LksY2MMTclHR5smUFchClw8uoiWt_2Lb5Wg7BQeW6bHWezjTB56gafIscDhHyvKyN9Gtu-4Ds115CSUhpjmRdqSS5VgTLJ4ktLSvnNC8tn8madJ1HQOwWguEASy_hUbezS4BhSMI0ElERRwX31XDB3SENxmoYLMA3Zv0zun4P65NT2RpAL2KeR3GUhfEIN9IXSYd6oZcB3_2eozliktiZRwZSWnHULFd8EHf9oDJkr5wTY3C4aRc3CL56r5evghlUm6L4evIoPkpY2GyhksRKWzxOwlwhRIQUYPGnKWe3wFzOgxJUZskuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6555" target="_blank">📅 21:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6554">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcQH2a9WeuGe3IPHmCFQFEU9fSAvgcUNk9XD-cew1L9CaQIxHOr57GsM7ledRiMWr2PAkCxeZOKMXFeH-0M29XO1aO3FlQRWw_D7axugC5IKbkXYQLMCxtVIjMS4J26D3bwNEKLqa9viZoTEOAT4aVbo24Kqh2tvdq3sELR2RerdyyAcDXKerPTwBEo4wwnV76zopcYbtqt571snxkQuCLMpl_gsDbSj7RroRxdceWRPTpJ1hY6V0UurqRwU6AqUpPKRi2tJ9TLXpnV_0aQvISS6w9BXPwOc9zfaE1bRhHGiwba372GMbgnauH8tFqPHt8dwhKbT8TMKw9PV5Ej_2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6554" target="_blank">📅 21:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6553" target="_blank">📅 20:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6552" target="_blank">📅 14:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6550" target="_blank">📅 14:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6549" target="_blank">📅 14:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بیایین با عاباس آشنا بشیم
❤️
دیس وگاس و عاباس
😝</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6548" target="_blank">📅 13:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6547" target="_blank">📅 12:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ظاهرا Claude Fable برگشته
🔥
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/6546" target="_blank">📅 12:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دوستان دقت کنید
تو گیتهاب پروژه ها میتونن ویروسی باشن
بررسی کنید
متن باز هست ولی نیاز به بررسی دارن پروژه ها
ولی تلاش ما بر اینه که معتبر هارو بذاریم اکثرا</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/6545" target="_blank">📅 10:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/6543" target="_blank">📅 09:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/6542" target="_blank">📅 01:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/6541" target="_blank">📅 23:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biFIovH0We9Gk8qVQ2VVDIEFn-W-Sx6faKEWIeNWqv71ZROWd5fqm3A3ZiSmb6nsIvw5eh7dvLRgxUwQ7EEVufh7ZOA_MpqyMPFr3IpCtFnYGgyEQuquR7BeGi5JyJ_XvA-KpaWtF8Yxu64J3Fut5O7BdYXVuKYLa5mBn6knMxaL4FsP5Sm5TCk9pHKFQ1Syhqj_SKA359c-neX61YkW-flaO2RtF1jGW0wNaPQcniMykrSLXClGcS6inR_P4bGSDpGCG7v_BaYgFmj_e57FH03GM8LdhoMypiVAGRU1iWEapyRRcwdUYbvSHx9oZFm7WmycxfEFq_XjFAQhxMemyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QmPrhlPiFipnRev5o4N81PWWvkO0Akz92GIrjXyGEpmKEWdgwm-PgKFiRnbqRb4h-myjqYsmSpQV9lSqtC6-RFjdqvZtBH12icJYrXrRyxdix_jOl_oZItT1TlKIF9RhS9_dsKVBXlzJrHQU93jVABMCi2KOMh8NU6OncvL_IcDvANECLif7kIOY3xSgxYfk0pcl0TRjQswabAWouz0fMJ6LDP7TV6UOcyXm0Fwx2-XWgQeGL0EGKUok1ewxy0DsadgO9mw9-7i53MaZoH3EEsDrBX5ivMr457vCXtKtY8SQgt_kZf_RR9Up5-dTaAckLmQjwxg0vTnXgI4X2uiDMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hYMexkuSYP1djaqu1MIOnBoxeW5yvTWlyw7th5YcmHpN-wZtk30WGjUeAem8D5u1v3s1H1P-jwJtx6ZSgibbU4Wf9Rva5vWCqewjtdx-A-Vejlj6Z_60BHdt94atQ1JiJmN8G4ndDODR7b3j9b4esiLd6xArQN5MCzMNnaIzVfZbHR7_N0RD5WEknnNbZHKgZqWA-G_IqwrbARLpcT3035TwohtggLZRVtnraH0gz6zSxcGzogt4dIBfcpCAGcO-kvzeQyUd2cAxULCaOVItWlOiXeX6TzJVcO0CBPtkYDfsrmo2OwDF067sAQ1tebFG1K40wqsU-G6PXdrwZgPRDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BIbsdewneT8EJxgtWdEm8e6r7jle7GKy2ZH4XtzkhtQJvrDxrYEwScUo-3f0sUkIS8n_q7R1s53PChk4jGWYFiDOgYqDVpSgaM6Vc1BJDE1MQrI1xcLJG0gpvaVNTKYjhcaywKGVnFW0EP33sf4ELaIZ6dewt_RVDoFgVxXDbrjSUvnHeJNffUhIJ-Bn9RiOCFGSbUdPHRcf2I896ksgCFc9brZnd0FSYI7KWEf9qXTbAnI9cJ5WewVWHD96Gz6mARooDtKN2aGrAy5sURIb6gOPCqRtDSJ7DpLmBhYQVgPh3L9dC7c2J-Z6BEMnIDSzRNK85C-p7Pm0oiLUXp9lQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nffm6q0h4jJXQBT5EZNFIF-pva6V91ZwI1z19mfIFdZhelPKEVJeI8GW55LGv4uuGU7N37HNNAHxdLx99fy5oYFlB3b34m7qiWuL_-8aHJsoGio5bZYWf0u7Wp7h0DDb3IEq2CHtOrOcW0TzIplsJJszfiUWspJqgBfMtJxlBixTlUNXw9cWiQPuRHdJRx0kwAbCMIElOCmz2iDU1Yj0kYwYTlrv3nk_7sqcjMDsX6ytD6khGwlpLaYaGAJg2NZ6PoV3zXgUG52WNiikaYs-83Lcnm7OK2T_6NWzHJvmvfBz_9ZILfbY5jApRkpoAZQOgyI8bQowEl5m-mmQX1bwPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/6536" target="_blank">📅 20:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZifYKCKJ-yxN20BADL1ijTa6ssfsMwgnZMbABbzRLAkyjjbwWtVYOeQ9IO2IYrv4a8B8sgj6odxhaGGrba-QEh74_pWzBJp9x9bSGmd1ra88xbpT6vD-GR1-Uj9_5CK1I4aR-IEp8lDSinsAAhpIsgBG1y57UFxWM5S0qsPXHYVaA4YzJ73DX4fr1FASbZ9O22-YZF4_WRL9z3DAIS7Cg6Y9w0zTozh2pcryy4HO4gGTQLJt0XQQxzrlTXipmZhc3NiiHKmwTDoA4PBSuvy-YhVwW4O7wMOSb9WrQKCy6s55P6aOFO6a9DmQgRX5ExQBi9UbUPBdkBc2qIiTbJzCBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BKkQTi_sb0lwTkccUN_6zpPEpxKtxMtEFQyo8nZp-TpiAEgd6wb6vkFAgwEBFQWmLue2oOcnoSIf2GCuJNmIMEJBGSt1J2Hg71tqaWySTaYdIbHiSbsRw5QAwg0AKC8eqXSak4w5yYwOdVnReG1r3YjYE1KsKIRgnyCcQc-JNk25j6bTeK926LmKEMDpqrBig2GRNzCS3s_olMry5rcJB_wR4sLZHUTG2qO3Zp1J0Z-OvwPrcwTXrORYP147HKi_z-RTIjUdiwrHLisUwtklhRuGy0kwE3jf-K0FOBYeeqNbFAobkyMOnkNVxaQBVuf-Gs6xHPjp4oVOdvS4QVmc2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hAxJLzUQUwmRqctbTArerT11j9v8AQ8kxzDCXnbXaBnGsfKKTG8YwIg99EToNs0Dcv_hs_RB1xDoJT9PotE9y0RmSH3IPTucFUvWM-NMrjx8MuFSXiyY7SL0u70qLyti7E7ZuGh3Y-v5KXqie6VMOfWkqCEebTJQ1BAPbe2ApaZnjnhA5A0oWa_VQAUAT24p17u0z3bM3bILws89iCBj8a6C5sfkZITKO2WxKmra_OoN2xH2n4XKt3hph_fKEFYoy9l14mO6n8Sh8kXINU0U_1eEEg8RvMpP-ePXYoRiBUScc4hAFEpy3Dtr--h6LpioXpGL0dLXUgGzlndbi6Jrww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tgJvut8g-P29HwMn0jlm_aO_f_X66QBZfxHrd9QKkjOE_BYcnl5iy5Dc4lZ7PdeH4w-sCAh8nBZxtobOwgbkLq20aevf0exxXnNwpbyKjHR1YBj59ZTe57HK8blhY1H5fJFRX9cko7oXvRzX0VGcWzJjwmBvWhGL2jV7ZobbcQotnPlF3iMyGi_Ca7ZbdFKC1UpPdxyzkNgiR1oVvQSZUhrBAKg2DTqo7hG3FAU_ARxwOKqyV3ZaOHz2DAr7KBI-6LdPAjAUdtRNbjc84wsQ1NTsKRRd6wmz48QSpNHLdlt9Z6jzLlfZYgy8TFRLCUoAFd9AdWb1_DoRnOpvvVhePQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OQI6KxdLDxtJH59KD6YvA3v-qFd0XYZnBjeKpVtq2hc88TQNamJ-jRcQHQvZceQw4I1H11Z5aFJ5nfZ8Wbntj9yMYF6iV3C1NjlGiDPhV8sQ6JCra0YAcGkrxiIG0iDj4yw416VU_VGR-B5wHDPwcku4uw1ld_O4L6VH35Wft_vhpZc_x7pORTz0SxcYlHkFMKHHi55ANGs6NIn3TyYS2uGnM7mhh4dCz0QRiKbdrAL3st4BAQ-E7HD6G34iC3RYeqJXVREQOdpBWoCXujSVKhLXAvufyIS5prG0M9xs2WO6sr8wqcgiM8MKaWDX3ATmYlRq2fJvmyHHTQvG9_IG8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j7_esb5cqMjW0mgg5oUcCLJQqP9Aq2qRsd3q4dKvSadAZP8oAd5smFG-eTI9CGN2pTZW5S83Ipm2_ykwNeIaqUMmn4LAtDSPj9PzY5gWP4zZLu6GTfsCeA3b7Y8Vepb--K5HK7oHychfVVESXYvvdnp0JNBw8pkMwq9_9kmguVdEBiv7oB0rHoOvWZD_9FXPvrm0bB8RLmzAIhfYWPpdy4B93j-tpCE_2m2xyim_onEqwuTn15xpJvr751QH06Ft_QbDtlH37e3Wu79SqykrYh4xsdjHcBIY1kEeNJGDjNO3ditmaQSCuCvSgVzkk-tGRwMb4HKq_aInV-bZjc6koQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jxQ---GzY-QpZdhm553FDLOGU0YmWsB6AFDXbvVEPgl1hdwfiYdm5AvZUlvfo8HIASLQ4C8jkqKHh5spfO23D4v4jTz3wVnK_ieKwi5yrV10FBJqOZMjHvRCmsQjSl_bTLv8_HOtELWBm4EPgzH1YM5vaZauPQEthXHkKpNRyTQiPvRKpE3cuUbkrHXA7fXx3dubpJgip7AUiGyjA2gHdS_LFBJuYS1EPzHINjn_mnp64BVo4TkoGPsqCkuqIr0TeKVxd8YAdJ7kXyE8FJWG2STM0sXjSS_eXjCPyxdxBzI79ctxEsukTc9SHOTmUoOK7I6E4U7yLzoSihvmJBVxsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر منتشر شده از بازی GTA VI</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6527" target="_blank">📅 14:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6526">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpQ4aQ6ezMcGQjvMbgOddhY8ZNzqNxXJKbT2QhkblToaSX27mwpuUnGB3XTBdnh66gN3iaXi-mVYHkR8mPyNXxWYPplO4JGBAd4XGwwHAtgZRU-Lk00YoIvHjGJKywzo9MPg7Taz1f0wHXdeOtWQgI9NI61d3NVbkJPI0906pUBYJZmC42l1xaE8SQALPznFIQ84rl3O1jZrMrcUBAeBJHQ1getUp_SYuGLIMx9Kz5iifriy-S-0QSIbFqWTHczy1UbGnFEam7QV28QUyzV885BfzSxkoDSFLLL8rWRtNts6v4--wz-Jdv2Pa9oq1Eu9S_MsRQbYdWWB1ipjrsniSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/6526" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6525">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6524" target="_blank">📅 07:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡 یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده. این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway  را فراهم می‌کند. از طریق خود ربات می‌توانید:
✅
پنل موردنظر…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6523" target="_blank">📅 00:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=i2a_gPW3k9qIvt6NhsMNYiUjj7vydodbmpBFx_8u4EjvyBzgqqd0Ae1YdT5Ai7d0S8GT2ppQEs4ncCN6iJZgC3n0ttsXTjb8AEG6OF317rqnOMQNfB1LhgU5i5qUVgW33AVV4ooeoexc9BOY93W9Leui69RHIjcPF7A9Ut8EVYWJC5bkAPYc8mxt3UVNSdEG6T5vqbjUiOMD2N_f6uy19Mftk4yZfEPHN13PY5Z4DKVpZHW2Gp3k-z5ZBEPJ93GBEIA52wSk7F9k3k6yuxzU8cpcUclIK8HdY_KPWdyy9_JaJk3S-4GUwPLpxFtgFbxXrZWYw_QdI8WRWx6Lo8Suvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=i2a_gPW3k9qIvt6NhsMNYiUjj7vydodbmpBFx_8u4EjvyBzgqqd0Ae1YdT5Ai7d0S8GT2ppQEs4ncCN6iJZgC3n0ttsXTjb8AEG6OF317rqnOMQNfB1LhgU5i5qUVgW33AVV4ooeoexc9BOY93W9Leui69RHIjcPF7A9Ut8EVYWJC5bkAPYc8mxt3UVNSdEG6T5vqbjUiOMD2N_f6uy19Mftk4yZfEPHN13PY5Z4DKVpZHW2Gp3k-z5ZBEPJ93GBEIA52wSk7F9k3k6yuxzU8cpcUclIK8HdY_KPWdyy9_JaJk3S-4GUwPLpxFtgFbxXrZWYw_QdI8WRWx6Lo8Suvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش ثبت دامنه برای رندر
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/6522" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/6521" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjYt_wHG1AcsmjC3iyN0hvVrl6qs0bnQIuklQlskpMmgHLnyM4LbCLCgQFdS69E80cpo3sduOcXvZb6ocmMqFfLH41wBmdgD33lQ-TOwrkYChJT4RpJ6A7_fgkx9-EtrrVzzxzTfaKa49a3nQvzAMaEPOrEX5fsLWTukliKDxNKiGrtr0nmkRNWCF-LoGp6hmqWmiYWgMosF3BzUIbqjvu5eagfBmg7w8k8LL-vpUCf-OJa48_1hNs9Q4F6GItkvGD7OKXhj9VnZuvw5p_xlgudW6ExGKwMFx6wGTbp4aGJwHxSbv_9AjfWkyEYSVoSp61S6keOCoo_xEyw6bpV7kA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6516" target="_blank">📅 20:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6515">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6514" target="_blank">📅 18:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCFV7kjk7XlhApQQl6eLo2TrUVPQmjAZq2poEQBG5qggo1RJMMlAMplkh7YmmF2r6RA-Q8mkGHwBqsM1Bc8wFBhlOakp4LT9bWiOfGNaqbqtVGQM5pFPa0Y5mJREO78WEB5gUc2qTpUd34j0vU8wjD-4VCAw8v74w6mMVO7T1QQq8Bz4l79j26O7uvsGZOyez43yHORj_PArjOLF0c5WKSlYbfGPKAi4qgRHmpseCXTNliCHGW-JHcQGCzX3_a5d7dvo7o1UVH2R9nxWNQjA5OEDXkblSQ5xTa2MCwCi4yj8uJ-aE3pC6W17v5kk-uwYSxtRhnhG32QfuQ0H0PGhwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6513" target="_blank">📅 17:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyX7d39IOPdmbRXpimU-vNJxrMqjJQvSsU-4oDbjyZAn4fXYVw0SV4sBNeSRsbhdg6YclvxNTURFR1THi600Ztj2azOsa-dElrOxIIGEa8up2gN5-_03aF6OVMV3_BG9E8LVbfQELw9g4izeeSqsWX81uWU4qA1GjirtkJ0G9ENO68Zi8s2KhIHwFbZjV49lDnXg9tjMpJCqRNUqv-q4vDT4caWeAJx8p4FRBPUhqYLx4WpJmPVy3clTufx3yrGOkRkFhMW9k9E0mHXeKn_RNOBd81uW2tW-Wcc1dMPKMiqJcxgAi924xQkjXj-7PKWLH35ITbxjxFu3aS_yJsQ2YA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6512" target="_blank">📅 17:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJWzfkC-j0SwWv5V5GyIGs-XrDBZK7hiLAnbXfPZPs4L2ZhU8xfP8c-Jil5081EKRN3EyHXJG--Tsk79r7u4M58ZWx2EbEBoTvERSTqGMOauSSLNFz4bWUFzsIWMf2wOqO4cwzK4rxgbt5RRUjou2ja4amW80uU4jtdgVaKZy2NwtRcozsay0loVAxBJo6jJddqEnPappcQBcNsOxtEumBDsv7LdejIdGtSKi-pmrfUZdYC_hwPGpEy81HpsKEXbaf3ViM9HRVZBMb7P35GueM-ylkwEqqL9U2j2Zv-UScsd6rsId4kZ_9vExY-0JiYX1pFAh-VqOek-zRRAPM3Twg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
Consensus — جستجو در مقالات علمی
موتور جستجویی برای ۲۰۰ میلیون مقاله علمی. سوال خود را وارد می‌کنید و مجموعه‌ای از تحقیقات مرتبط و خلاصه نتایج آن‌ها را دریافت می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6511" target="_blank">📅 12:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=NsF5sRVc9plZ5aoMuWywIma8Zg_xV6z8F8XU3QFWtCZIDlkvN510CRpkTo6NftpFZh6reo0h5tWOCt3tvFHXPkOGbnWm6V8Lk2ac1qlpuGbc9GTkvVVO9YAdj7QkVxRku5duWpMnEAcMF5OcRiffPjyRQukTM8gRrd5mD20rDzzf1YVKgj4H1CSuBF1L8j8HhU2k2FoFoEes42epIssGAz-HV0sa3VgHiA-kYoDaLjTsztEXaSJpq5XBGGBl_4TtSOnlYGrvun-ikhgBINRXdwMMww6yG0r4gVu1Xod5aJJVLkB2S5zFsdnDvoHsSCQnauWfjyg8TOA0jpXArGVMQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=NsF5sRVc9plZ5aoMuWywIma8Zg_xV6z8F8XU3QFWtCZIDlkvN510CRpkTo6NftpFZh6reo0h5tWOCt3tvFHXPkOGbnWm6V8Lk2ac1qlpuGbc9GTkvVVO9YAdj7QkVxRku5duWpMnEAcMF5OcRiffPjyRQukTM8gRrd5mD20rDzzf1YVKgj4H1CSuBF1L8j8HhU2k2FoFoEes42epIssGAz-HV0sa3VgHiA-kYoDaLjTsztEXaSJpq5XBGGBl_4TtSOnlYGrvun-ikhgBINRXdwMMww6yG0r4gVu1Xod5aJJVLkB2S5zFsdnDvoHsSCQnauWfjyg8TOA0jpXArGVMQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6509" target="_blank">📅 09:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=khXNloLcXHroKRkQjf1omHbyCRPZOoyjXN6oo1-awDc6_btpGjd-vjRJNYoWErcsiED8X_gFQpXxlaaFWF8fHZxEDCLk073-2Ppc3a5VQpGGFrbzoZkGgAvAKZUkmtg6lH-NgoTDEcHDpQrLVAkYatRMjEjaaeWfAolJOQ0sqIupEAauEenIOWB4jThs6An5xVBDuGWoo2536BShp-LOGY5ezyYWs0FgqeoVN6exk9qxL7Z8AEBf0Lk6GPs83-oB0s1qt19nMkg8VuYpkcUfNlSrD9kNW415PkSZWnutpg5EoYCZ4jgjAIirJU8IlTZNdrciPLQoux7dYaeFsiRh9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=khXNloLcXHroKRkQjf1omHbyCRPZOoyjXN6oo1-awDc6_btpGjd-vjRJNYoWErcsiED8X_gFQpXxlaaFWF8fHZxEDCLk073-2Ppc3a5VQpGGFrbzoZkGgAvAKZUkmtg6lH-NgoTDEcHDpQrLVAkYatRMjEjaaeWfAolJOQ0sqIupEAauEenIOWB4jThs6An5xVBDuGWoo2536BShp-LOGY5ezyYWs0FgqeoVN6exk9qxL7Z8AEBf0Lk6GPs83-oB0s1qt19nMkg8VuYpkcUfNlSrD9kNW415PkSZWnutpg5EoYCZ4jgjAIirJU8IlTZNdrciPLQoux7dYaeFsiRh9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9-l8nLu9CqlBICu0h-oDjlwEP43Sd0_F726WDG4_k50RoUz1JKNF78LkZVusjYnz-JzyXQ5R6W8mI_nmHLrJ0EfD2nrXqMsuoJe5MGdvB0DrCV-Ml4c17PuP0NMDDW9uVvQxyGK2itSmSKxxIZ2jQjUUms7g3p-6tqN-aJPfdAlxBSvAOFw6LA55C_UwGyYtzYY1tBw4GO7rUA8UOtFGmoVrlmgOMnu7uAXVnbEwdu9-ER5RU4eRh2KgBI4OEw1Yms7BwfT7pvQWJzpORDm5ttqDPJf1IdCjDrP0fdLlK4CDY3EMiPz2ckbKKvzEI9nzi_KvrKrsFtQ7UNdZy_QNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/6506" target="_blank">📅 23:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452211db9f.mp4?token=kOy5vpvA8xqN-Y0T_dA7SeS2UVfS3QHDxb1lVDUAgOTMZTsqh9Ln2uW8va3xeJ6Mv4Mg0HYnGq9r5dE6RyDUxMBhpWfwehM-OY9KJ5I1ZKn1FBwavLbeQxCBf2Ut9eFHb1zmlIqMpknf6IKHHdus77y0QzmucO3aBC3qPAw2unIC0JtinbXdav7PPS5OZdVsU8s1AeApDYLNsq6eiVu7GSIFbENXS44wHfWSbrSYL9y44DALct4Fx_Lo2MQPOq-q8eIW2U84GAbcQzMtWftrenJnYRot7zXe8nR2we4cL2MwjKelhxWzz78w2xsDeEtjztmnBnlaYYGggdij0l88tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452211db9f.mp4?token=kOy5vpvA8xqN-Y0T_dA7SeS2UVfS3QHDxb1lVDUAgOTMZTsqh9Ln2uW8va3xeJ6Mv4Mg0HYnGq9r5dE6RyDUxMBhpWfwehM-OY9KJ5I1ZKn1FBwavLbeQxCBf2Ut9eFHb1zmlIqMpknf6IKHHdus77y0QzmucO3aBC3qPAw2unIC0JtinbXdav7PPS5OZdVsU8s1AeApDYLNsq6eiVu7GSIFbENXS44wHfWSbrSYL9y44DALct4Fx_Lo2MQPOq-q8eIW2U84GAbcQzMtWftrenJnYRot7zXe8nR2we4cL2MwjKelhxWzz78w2xsDeEtjztmnBnlaYYGggdij0l88tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjijfSF_uGEakMhKxKQ8n5ycDy9E980iB42c0cleCBSIr7c1fH6-EsUmpomQvOn3-YqItHKrYWpN11t30Pc9Zze-EteI_DdgMI4sGKMjzTyo9ROOiTNaLk5MFTAyPvwUHUjAqZd9rZMXgxynoI3FTvk-nZbbvaVwZCMbQFUMJTJbNpZJV893Tt1qu7AKHcP7zW-bXfdvZdM2nH1bAG-rSS1cVhG0_-1u1DJ6cy3EaGRSvi9jDcE5SiEhobeqPQqRZ746NMaydU6ynWekEn6kT4xWyTsGv5xLBN2Sf3_w5g3jXSU9UtAZeWrpPEYyCrkjtz2bHdazU-LlxXHuttKq5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین سایت دزدی دریایی زنده شد — Bookracy در سال ۲۰۲۴ راه‌اندازی شد و به سرعت در شبکه محبوب شد، اما در سال ۲۰۲۵ سایت بسته شد و حالا دوباره بازگشته است.
• درون سایت تعداد زیادی کتاب، کمیک، مانگا و انواع دیگر محتوای چاپی وجود دارد.
• تمام محتوا بسیار سریع دانلود می‌شود. می‌توانید کتاب‌هایی پیدا کنید که حتی در کتابخانه‌ها هم نیستند.
• همچنین امکان ایجاد لیست شخصی برای مطالعه و افزودن هر چیزی که می‌خواهید وجود دارد.
🌐
Site
#Bookracy
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/6504" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBIBwekF3-07ILBAD9wctZtDhHugNZQJXQNXNEnxehq7EyECLOAtRh8Jk1H1C-yDE1ikbwEwXGvo_kiqGgnfZs-byFPVoQIYgWaHiafaWUdWYGIdi1JiMOQte-ug0BcUuaFViIWYgUeYhHaU6W1mT5-up6K9I8Sr3bfWBuHLTDHhfoirpZjKgkai0lgl2n5_FCGVzroEpRRN0ehKjhIjF6wNrusgF-wH4_m46tZ8VYFTG0n1-lOdM6MvkGrn_ilDpK57qIKn_S2qOFw3hPDI04dxyyPVQqRsyOBD2nfMXRn3bQzDxd2fY_34raYQWJCIRukkOsHJl7n4iU1ebTW2-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9ZCLXx8kOAT4uMsMEJW6md989MCZaUQPEhp4wjh16SCt6DvHCMEaJjLzBC-V0CajL0PnEPFN9NICubA0oNBLcK2PTe8TlwUnyWvsxl6o9uGkFNGFk44TX2hjl-KUWVNS7xS6DPAlARyj5vCfnzCRs3umRmvZNB5v2Yz7TXevhOXAXuIOnspfLkKvUr6ui58AdHHiYXCj-TiJTk5cz0SrpZrGLKSUqjWQ33atE3S661-3DeDtuMXTVQx2_A5jzCrjbrV3556s8pqS6jwebdZ9X2IBlLb9BtV5w241q73ueTsEqT_8lUIUnOxtlyWGHYPWzQR9lfJ_8smO8ZLfzk2zw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6502" target="_blank">📅 17:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔗
tiny_computer
یک محیط دسکتاپ کامل لینوکس (Debian 12) رو فقط با نصب یک فایل APK روی گوشی اندروید بالا میاره!
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6499" target="_blank">📅 16:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMX6iAWyr_ThlPI7E_UNNKFTfokffxLZSqaGO8bLhId1HXKSaRyKpy2pfCQ8Nb-EUokqKBCrnaSlDqJpDO5mh7n-xtvBB76U39Eh5B6SpXvFvxhz5laWqoUkG4Wnul9FzgfG3jrIX3bCbmeeZTFHD1MRW66CtqK6S7nqfb3vKY0KjE8otv1kU5mMOaaNfSKjGshksR699F0g6rRMG5b3n8g1OqTKoFIOrPXD3LCDi2ar00-Sou87nyreOqJlE9hVa8UiOUGg6mpfac68Bc3bne1XmGJwPfzY7pLquhZpFihWDuXaHnzXdTv6_queGyHvhLTVyi0We2u_ke5i_8-9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ترسناک بقا که قوانین هر مرحله تغییر میکنه ، در تاریکی از Cobb فرار کن و از سیاه‌چال خارج شو.
🌐
Site
#Game
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/6498" target="_blank">📅 13:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=QxXPSOaXeJmn9EplmrcWKyopyake5FdlRZ7hfmV1SIS9vDpq5cjMT5ldQvY9ZMGCApTKIAyg6Sepneba4SPpCA4gMh-IgzmXjPq3DYvsQGm1-oxbOJhDJLysmPhJ1ZaFrOAavfXuJC3M1KdddpZniYBECYwScNag7fnK4-lr4uHj-Et5VAoQN6-Ujr8HiZnZuI9QcdKUxxNrg-SyH39oOBNueaEiyWq4TI4Nw-n2Bw6EdHsgZXiEWsfHVJjd2Lgu5_rU5xPYz4hIeCWOwpcJE-M_2j7JSw7Z4fT8Upn4k39uOptxnSiJySQ2DPxy33c1JTfdALSQVBns3loKKb7C_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=QxXPSOaXeJmn9EplmrcWKyopyake5FdlRZ7hfmV1SIS9vDpq5cjMT5ldQvY9ZMGCApTKIAyg6Sepneba4SPpCA4gMh-IgzmXjPq3DYvsQGm1-oxbOJhDJLysmPhJ1ZaFrOAavfXuJC3M1KdddpZniYBECYwScNag7fnK4-lr4uHj-Et5VAoQN6-Ujr8HiZnZuI9QcdKUxxNrg-SyH39oOBNueaEiyWq4TI4Nw-n2Bw6EdHsgZXiEWsfHVJjd2Lgu5_rU5xPYz4hIeCWOwpcJE-M_2j7JSw7Z4fT8Upn4k39uOptxnSiJySQ2DPxy33c1JTfdALSQVBns3loKKb7C_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6497" target="_blank">📅 12:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8OuabSFV3En4qmOePkbwbk7aUzbY_0N7pa1Hq_R68eH_AUydDW9F02hHyzVaY8oIEt4hB4THOZ9n51hy7tRhbGdu87T4uAA-evbAuUUp4f5fBOV3sulWMKhGJcMvncF6YKTcfmAJ-gVAP38UT-vxgtRpJA8FWWoPT9p_QZ2v1pYHA8eLhmUsCtK8yAIcmeMXBxhIjOthmOa2eGrXAZzQddFhKC8dddKK_mBBwBhUGDxGNWj-HLHBh25FHQbgYaSvbWsBbM3X62y7liOzltSGhirb1yAefGeaCCLkEPXTH5bNetuPfmpXb8sORAcGbRtvcEn2gnFMUwSjSJlJw8-aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی Sakana Fugu؛ سیستم چندعاملی (Multi-Agent) که GPT-5.4 و Opus 4.6 را شکست داد!
🤖
✨
شرکت ژاپنی پیشرو در هوش مصنوعی یعنی Sakana AI، به‌تازگی از پرچمدار جدید و تجاری خود با نام Sakana Fugu رونمایی کرد و ثبت‌نام نسخه بتای آن را باز کرده است. این سیستم یک…</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/6495" target="_blank">📅 10:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/6494" target="_blank">📅 10:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6493" target="_blank">📅 10:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQV-FM-UL1cGxGMzznQrrMwvOouFFZrw688KV3RWV13WKVyyvxmeoaggwONYQc2geZVynW1mdqu7ywrRKisehEpouVXM3d2G12b6-ssqihMaAlEhsn6iXT5EMIzTxzUyYgFhJnXb3jjVQ7gOTZ07m0mfOLXYgbV4RvIMTpm2FKIphHY-5obXQwucXyh0ccik9I8UySVgy2fITbIElOdlZzhtLL5OKWvccDoa_z6Q0GJUYwMfup1HSEnQDLmSROayPZqdCKCmYyIIG_3ms4YRn8VT138HnJMtyg8ouKCJblfo6dEfhzxFW7ZzERJ0mYqjBCvaGe-fQBkXRqIZ6oInvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/6488" target="_blank">📅 23:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3yxA5tekq8hRHZKJU1RICpk-5howjAo_uvPM6f4u9UpHb1HLGBHbpzu8CeEEFCY_a-NBXCz-_9pe0kQNntF5fvqu9BM1wlp205MvqiKSIMSH1P-PlOJnLC-zBD9CJpA_H6bsY48DaxW__1hN2D0b0c-s2h4Pmwiqr0wYK5QkNB0p7NwlCto4djLE94aN6vRFGXVbt8ZuL1Md5DngZlus3RJZxs8GOLXxY9GZNV-NrRDQDP0oOhpBJV-OEShZd66kBb-Co88-6n-WilD7_GM7lkKNx-pHOhwHYpl2IJ6NeC0DFIdVLSqgjNeGy0JucRdaFTF3GvAS-E9cIkp1LSfTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت What Is This Movie کمک می‌کند با توجه به صحنه‌ها، دیالوگ‌ها، جزئیات داستان یا نشانه‌های بصری دامنه جستجو را محدود کنید و سریع‌تر فیلمی را که نامش را به یاد نمی‌آورید پیدا کنید.
🌐
Site
#Movie
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/6483" target="_blank">📅 19:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTzOv1iHho6RGNND7xqlQVJs_O6lQieFlS0ja-3U-y_5b3jZZogPWzg-JjTUR6G4cqUWsVIgQ14AGJf5GJ9pIhMao18WeWhsPx0-bk3Cy8uvy4a3Z6rnLfEbWzV6THhgHMv9ElubVaq8yE-tKtNhUgQ9Jkjm9cJiWU7ZwNnmksOLvInGBP4_8W39USHRzqnWeXeVGGRdBDpXsYz3ozxKa_SppF7fT_OWgPVkJ83OnScSTb_DUel_fjAMuFoe2aZK4pQlo_FQ3wgFHoFsVbW1ZIIpuSMADtYYR8h9Gho6vxgc2QLyj2TXBQUlEBadeeL7x1EveGmwqNCm7VQfzFc_mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف رایگان واترمارک Gemini آنلاین و بدون نیاز به ثبت نام
🌐
Site
#Gemini
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/6482" target="_blank">📅 17:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1pNxTC1g4g-hF3kBiOVbTFeC8sSsM5SCbzyXnq6G5Uu_Xf1lKPvfkR0MSqlznRYQoCpl-iQ4lk3cAc_z0Kn5JOxwfiNEAkvzbf-oihazsHZZv7Uaq-hd-Ommp_Cyrcu2z_yYJQ6vaIVPTmXKb6TjW-HfX4UV-WI23vqPJBrIjkxMBQcanNxfSZUHLVdgtNoiyEJuYGKwbMYJdajJCOagU83DPUk66dgmcG0sqms8773Vh0IiWLiXgpqW-pOvuZCjQpwSRad6S-K6_Mcsp2HfviAD0A-A3ykeOsJE0YuSHAbvjaYhka9T8A6pW0MCxfOiC8odIb6TxKI81kDLmAruA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/6480" target="_blank">📅 15:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNaMjFWQQH3fImeDPLSEOyEwaWRIMPzEYJ3cBQkKJdk74-PDyKtfgUhvd_jULRfcr0hL10a8dyIPEiS0ZUCUUrCdK3PcUamrne_w1xX7bQ3wB97FAhPq4fYAZI8K2CGbdAy_osOkWOtSqulNkzOq25RC4uNDm3ZvQrsGUG-ILu_M5FWivc16ioJISYCyzoUGVGscEGcX8zSE8fEsZwQi-icEDPAkU2lSvqbCr9YphFNkgvpZbXedeV5YSqqyFypUxXxNhqM18vdu3DyhY6ris-Hm8VaLABv3GgWua2QQGyrCkVdK381_s-i1xxTuM5hByuxWzaJ3d4WJye0r6bNx7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6478" target="_blank">📅 12:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuzrpgOjVvzrqJpf6DhKIA6EjYhvIf_QrAgNwVDJMHI9UHxCCc3WaEQpx-h2fWwQljhqiOARPWleB99KPNA0awmX7e3WdfoAVdISbkIDU3L6JUaGYTsVh5zW-25buyTYEJhKZbk5edLwvcOu3V2IQ7RWSOonC5zXKGCDCFrCTvZA4IqwZabnQwvv1FGoSlCtEz-WSLeFl3pd5UVRM2MNBQJiNOlPWnfnAe9zxpgXJrtYmhJK4kSv4GWCfztN1FBKkHy8-kM_jTSAO_EQeXH-fJO2OngKnLFoVROVUZ1vVX-OrjTNcBsIFm5odEtJ_ACfd8HG6xQtgmedTzkb-YJQXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=faaSaTm2Zg5YsYDJJ5z2ro-a9DySyPkyq3Rm_Q40lkHCkoWXNQdJA4eIcV4eisA1uUKkpgO4sgMEi43mwDkr0qTM1s_esLU3jnHyaW79Dr_HGqGxtc5Ur7wp8ok4SnWG-sXzMcjRj4D9mxL-2oSH4fvImu_w2M1X1j7CoSilvntQH20UsljebJkDxWVGGhQtNwLN8uTwY0UrrqOcn7FgVUpEvlpUxMfDRupDG6RM2dpcEA_iXqWuFpg2_hv7vxJTo002AeELEYw5iLO1x70UBIVsIaL5ROFdJUPzofF2ylLiJgMj22-2pEvW6Z7Vr12HpFegUfOPPuGZRT4HKofHgw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=faaSaTm2Zg5YsYDJJ5z2ro-a9DySyPkyq3Rm_Q40lkHCkoWXNQdJA4eIcV4eisA1uUKkpgO4sgMEi43mwDkr0qTM1s_esLU3jnHyaW79Dr_HGqGxtc5Ur7wp8ok4SnWG-sXzMcjRj4D9mxL-2oSH4fvImu_w2M1X1j7CoSilvntQH20UsljebJkDxWVGGhQtNwLN8uTwY0UrrqOcn7FgVUpEvlpUxMfDRupDG6RM2dpcEA_iXqWuFpg2_hv7vxJTo002AeELEYw5iLO1x70UBIVsIaL5ROFdJUPzofF2ylLiJgMj22-2pEvW6Z7Vr12HpFegUfOPPuGZRT4HKofHgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6476" target="_blank">📅 09:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTkGLL2iDf3xuFCqs-zqaoAr217UGNInmL406NfMi_B6Lm0cawNe-xRG10tufmWri-8WB48UJYQm2qyPdSX4jf4-0RTihW-55yDYxpQ0qpb34HR7L3rvYrvW9Em8RcYG-qlhkf0rxWLZcv4LOmr47tHvRVwQ-YKfB4SSBdRnjfuqivO_vWsRnC0LrqhvUWzuhq08wX2aW5ZqJXaDkhw5ui-8yR57HzJ47CdjONPxLPxVT9Qe8wAXCPKjqGUX3qU28FT51AuQHbgvKtgpNRxup3Lun5yOE9dYWiu_6m-W0eS6mt1FUSlOsUOqoqewWgLUr4XFhDOKglkF5RbytAWSBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/6475" target="_blank">📅 01:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLiqcM_cQXKbIKbDz0KH65fyJEpvoqBhUdMom74CiTG6_paiZSSAFsfiwx8rDTXQvxzjSIzvK08C_xuwE9TMN49mqqULKFUtKnu27z1GAJC1zxR5Sjn-qLD9vrBx-HNMu2QEFkh2Apce__Oh5MQicPhgjivnxenvCKxgZh_FE_rHH9kFnnfL89zSgfp-eI9Fzig903ZwMNCTzDln-pplIeJNaQvGbrLDhSnyjiqA2XPptFFfb1mXsOjyWcaBs55v1R5Fc9NMyQcG7btZQQNDOoX-cdBMiwlG5eh4SaYeGcB_QUkGUPC-PhkWnMrXN5QKA49nACcCDUV9zxQGuOGPkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6473" target="_blank">📅 00:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6472" target="_blank">📅 00:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNWvPXpVLYV2rQIvTL3nzTjYggEBgJDA-BfY-7_v4jORNSfuy6at1mb9tZTtLFdaOwTrCk6mZIuhrqhOk5_w-fz_ExKmaDg5qhESMn4h_1db5sB_MyoHPF12bVOaU3VE7sc0AawuBtMQT0qM-Cemz0wyOEq8kv3D0uPuuWpCGpreIEv-GR-D4Rks3XUAtw6LkgVdj-jovUF5nc8fwz0kw8l7v7keCHtM3OPZkEwCNNWsjNnTkTjS3b6d9MYshzXzzCDVs3A6PTKT5IxZGw2J_GrWG5K_kItEtr8qVbz9hiaD6VWPkknj9WhubYYctCEskkSjmh6U4QgoRTsKrwTe8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6470" target="_blank">📅 19:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odzB17cKRsyuf22W6ven-kAtbnBAVDSepGiV2aftpV8EY-KPKD02q0J4mVGo1x498_TuP3dbPr-M04eL92U8gVDgkVYLFSeDPbK1uptnVQgLANJBjE8m0Y2xM5eY8X2oJFzahaNiwIoMGYbUHeiZtsJdWARHeAF5Q0W5orA-xUw7r7tHouwlVhLwJERPCwRo0B4y0nb2duswS95pTdk_c8sLdNRkxZZUx2NA62mmxjWL7zikr84jZH_2o66XxlETtyz_SLpssMMDdSoDdnQu1JRz1r0hFkXJcOE_n5X_OyHIjz2TBlIpMOASsSPRRHDJ2U46EleOmIQG-yTGMMYyHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6468" target="_blank">📅 17:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a_xkcjfx75Nm_Bl7f-wTu4GkoQOvhAk9wddoAvt0859UYAX5fKHVUkH5PfIRdFBq-Jza_ID77dZ-mjOLDfGmm1zkxT9S8q4r7qEeLQm6dQd1F2Xs5Z102uIFwF4ZmXIX6lrgkrCNoUoKlo68Ryj0nihW4CMtEUxhTXFeu-CUqGeYYJ_oP0NdN3Q0ZmqvV_yhhrnBkvlHKV1qv4Bpf8fGbDsztwvB35iUHU2OKxg5cRFQGcYpFVf2zKVVcwv5VBzKKphSZTGFuVo9UwZAGfXlWKolCRrLWj9S8kBB2zNXMwBhRnpxeBI_R3tNQLKRV7D9WufinTQr7AxoueNs0VWOGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JL5hUqNa0wyfRWQYoMI85vaa9jR6b4aCVt-0qvwOfUCSWwrHnsw6yY8DG061WSia5qsg1sLJU3tFgNrbUuoFCtoCdpwSZ4cVWskblEeAp695Wps7CX7s2isUa4x_CxCEbuLMkJAwnWn4iOrDuZvReSyNUWoscKssSsiGENJp__FLbkBeoUeyqRq-bHXviPJZ3t124VUkvfo9bsHe5yy0hHTGN6VCFxVvyER1UFCBFpNMb8vzBmdbAzxjUCnStlYy5wcwRX7kBfjbz-ka1clrmw4TrsQ-DgyhwOHxjhPgtitn1Uri7Iwu_Yo_ySvXhOV-ZOerMwR21vTfILRW7IPZHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGPRSuwV0rSxCfpPIVWWo56WDpHOj2k184cYtjj1_C0RgQVrpwOXG62TeIANocTvH4L6JhBdXnCkkGidLs4m2kJEhKuVNCtGaxZA_oo51iBx2GSRvxnw9oPDft5SCgcVzToAmERAHDFE4nd90VUPGBT0_lFX7bspezwTD16WJLUpxhr3JupMevdryA-cdtYQV1Tpn6x4a5XyPKsuEvEihl-SG_3ZV4vQE2nAJoSQ16SiEKrtphlvnKbdkU51j84So5vms5beThyYxOS3m6Fx0jU2JlMCs9GmePRVyTBmYnWWPTsbTTTZxiqMod5dE1_5oSfi92RrBsxiZxEyaA9TSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kz9rANc9sDPIG8_KP_CNig7JU2SWjXfj6H_y_z3nuhQWFjP6QRBH_V5j71BPD4cy-k2lFtRwHiFX8Ayfr8KxlwzYMBr4HGgG2l6LROsbX06LEnXu5w9tc4kWR59WU47BaminOZvNXD5RzLQimscMY3Mw_Ei92gKDN3d20SE4QCeSCuBK3LP5yXcltsqyiKYYXvm_zebwSWJOxk6byyrQOWlZtFpDraJJGyzvfJ9gkRkdTcUs8Mj1-sL1d5LBnGqLSLgpH6nSSFIo-h43QtDd65F0hjJfTAZ9pDutk5p6ZNEA9EQs8zL5jyttTAA-gTGJsChw4q8Xa3OPL89FgbUUxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jx1fIXh4PJ58dZopDPeovSUy_ehPeZEzIBwYIyakc8b3tvkBUFOff-bR9D8QHEWa-oPhiMTK9A0lqmHI3zHyK6NU-_0UDo9J5r_cpBkJOeTfo1r5ocnHfRgq877ksuhFWhEyMAiPWkAtrB6oRaYbEFQpqHHgPKDGFlhXHiz4BJZQJgBTl8LUS0iBYseIIPgLSyBtEWB8y36wWAcc9MM1aKuWnYZVVczttVbuiwAJfhwD4sSJFR6DKZhz_MOonpad6jhhx9NmE40tRe6TMxhl04sROkp7SEe6uxXhlwvO7oxvKWyeor2fWoF3KjgQ-TLW5pQkF4c9gNDTGUniEtI0Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AO_yOHJaSIECMkAQuU0TAK9Qbw24ro7PN3sKt0ehxR3Wy2hdteSgqSVL4mXc8MfR2xhRXKhoK_iOG1oQhMKkHU2dX2FQ3vp8fHq18bb14hWnJDzgbUas0nLnHUAZj4pSiC30hU17XEqkyqpSH81lyD3CYzss2VmT5grx_2SKSW4yxs5LW52B0bB4kQXWVWu71y4dxfLKrWPV975wiHiaAzIK9ntkmA5bjNUBNi0oMlAg-HCrVj8nhzhAWzFRAWSIwCZZ9UuAk8fvGDQ8S7tnISjjJ5MKt4vNeJZ7NwcdPDVHdQrN2y3J5WRzblkXuF4L8J5W3z5H8mXj4cueJnf4VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LiXsA-7CEJUZQ23DvQf6IMwJvEcacZQ8lGfa5PfcgpCchkV6BNWthbjA1TgWK15mGGvXvgCyIDLw7cEyqa38NkIkNO3hvNKeRHP1p-N2Het2HMAFAiS7mOP3yECpwCfH4614GivPbMBCBn3fdtoNWuEeYv7guUqjWREmTj73Xxi4u9nYd-bf6PmYGyyfx_kBNAH4I7t_kgO_XuEjbaWpQll678EJSobE9VuS9jH-G3ekr3o_ErpYitrwGjHj8o2NbuppU3GkvT4Oruko3NATU3NcWKewXt2KXcLVIsYjDS8bQcyhRPJ-UIH3HULzCph2MvxRGMfBH5-FJ9meCV-MEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RBnHhNluNJ8qoLk0OQ5_z8JW9R2cWT-B8ApvWc9HXn1NGVzPnjFL8LHz8dix-qsspyxTElS-PjNvsdyw_753U5uOd-KvKnKskEkcscZHqHHvRC_B9nAI8qrKSShdLSDtsst39gHux2I4txPMpgLk-DjCnep_zv0T7ezStCHcJ3tKNSYqjEQLT0J74FFC22ahChQQ9wE7kis6Rgx9LcPPDuXwYL6zDYAQMY-cX5lwYCNcLpj4Q_vb68LiZ-ohGNXuoFrF9p7Z31U0Py__s30HL2uwjcP7QFI5zZ6Ad4vXd-dgsLM19wQ0jFEs7KNBGf51P-dqeqj7LuQlFqoAKf6sGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ded905356.mp4?token=GddofLoIyEBY18NTRxJfJagibSMVVvZEwSJGDH3wrlHIZyUfKpnNAGG5uvdaf2rW5czLSzMm1KLMtIqgE61TawHp5-wmgLWcSVQdx9R3r9l4SkSStgCgKLvBVEPaPXJLQaVTLEP7K2yeBea0v1zLEEYkvrgwpEtxTNYbHubiGfozcLHSsmCeeR-TJoV8fPK0BmPuIcHUkZtQej3dtY5lfKpmEdt8l_aKUsB0TDjHKbA6kPwDYAUUI-y1ud0CviOu0UTbG6sHiRsr_lR1Q6R_krjbNm3GjnrLbSmc2j4V5enfcO9SIBzdG_JduTIHi4jarDRRDo8gdTVPAZqAkrhZRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ded905356.mp4?token=GddofLoIyEBY18NTRxJfJagibSMVVvZEwSJGDH3wrlHIZyUfKpnNAGG5uvdaf2rW5czLSzMm1KLMtIqgE61TawHp5-wmgLWcSVQdx9R3r9l4SkSStgCgKLvBVEPaPXJLQaVTLEP7K2yeBea0v1zLEEYkvrgwpEtxTNYbHubiGfozcLHSsmCeeR-TJoV8fPK0BmPuIcHUkZtQej3dtY5lfKpmEdt8l_aKUsB0TDjHKbA6kPwDYAUUI-y1ud0CviOu0UTbG6sHiRsr_lR1Q6R_krjbNm3GjnrLbSmc2j4V5enfcO9SIBzdG_JduTIHi4jarDRRDo8gdTVPAZqAkrhZRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/6456" target="_blank">📅 10:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWkBJ3hTGj9QKm2ctl8Wx-IZ3F0pAOSGI7GuSQU5YCKw-jWMBn3ZYGS_l01gAyVk3ZFJPzr39x1R80iAW3DXUGgGUwMLlUM-0GfmhMs-_j9M0xQfdfkUSLfBHqShQGBSYtrF_jPCltcPc0ph1DlJvmOkZQyj9prJSVZkTrqxgtfkbeod_4BMoDlXntYvyTkiplGEP7gK8o3Yj6o7p-Mxo8TEWvIDlK2-Qwd5Sk7bGZ6xrO4S0Wi1WHpa1rFEgNXfByPbDk-BQPW452jlxkRl4eECMPkg7Y0QkTMpTz4KXdiDiENy8KQCEDDAJNrsDAz0ShpoMqxlHeHlbJbz29R9AA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/6455" target="_blank">📅 08:38 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
