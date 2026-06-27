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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 20:29:13</div>
<hr>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سلام
دوستان اگر به وایب کدینگ علاقه دارید یه نگاهی به این سایت بندازید:
https://risman.pro
برای ساخت محصولات فنی میتونه خیلی کمکتون کنه. (بدون نیاز به هیچ دانش نرم‌افزاری و برنامه‌نویسی)
امکان انتشار در دامنه خودتون هم بهتون میده.
با اولین لاگین حدود ۱۰۰ هزار تومان توکن هدیه میگیرید و اگر خواستید توکن بیشتری مصرف کنید میتونید از کد تخفیف welcome برای ۵۰% تخفیف تا سقف ۱ میلیون تومان استفاده کنید.</div>
<div class="tg-footer">👁️ 607 · <a href="https://t.me/ArchiveTell/6596" target="_blank">📅 19:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrlqEimApmEYJ6iLCDNnv0YayyHUio0T-CMs1XMmFcsuiXKJQNGhpw_v308YK6nNyKU63-r1Jv0ma3l89391_ZdAickiAlRxd0UN11_IQTd7edUR0uq2a7tYNgWC1R-0RpNG4MJLuTGo2O5YHpY7W4_btcp7rujuffR-K9vNWXS8AMyCpVe-rxBuJ4qq6SC5DuLYUFtNp5ppzhbU2SiG0yWTin5Kd9pzzMWEoBUdVidYUrZGrmagd7Fd3uYBg6En_qiUaWLtJZR4pTD-D9TsahXXX60BrqDEMPn-EV09giIlCoHhnw6NGBAJN2DU6PLx7uYEW9oDfm7u0gSUbeiWcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابلیت ست کردن پراکسی لوکال
خیلیم ساده
مرورگر باحالیه
🔥</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/ArchiveTell/6593" target="_blank">📅 15:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQU5qKeBbh7R_VS8stSIC7JUkgA--4rs4epVtHJvRccE_4dvpotoS-jYm1gzRiDJabCFBjcuRRKhnreCOYnofBEQrySZIZZHkI2V-mMrllcBwAkINSt3VZt8zrPKMPtJFgGjpWFObtPyY5ZkvDoN6bJLScMR-0Oc18KFre_3C0CN2mfSXqqVIdCDneZKLKuSYRw9CeRwwMCLvQyvCfA6TJeggwup6dMHJcQl3w2jNABMTFp-vvwa7kHVIV1tRvxa_7j_1Qqgxq4EKxrPYAyz3Mh1nejyb4hrx2IpAsaBYSlpdnU5EuqU_MuOIP_tS5AnG6NVNbBBoivx8Oc3bo7d7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی مرورگر Solipsism؛ وب‌گردی با طراحی منحصربه‌فرد و متمرکز بر حریم خصوصی!
📱
✨
اگر از ظاهر تکراری مرورگرهای موبایل خسته شده‌اید و به دنبال مرورگری خاص، قابل شخصی‌سازی و امن می‌گردید، اپلیکیشن Solipsism یک شاهکار در طراحی رابط کاربری است. این مرورگر اندرویدی…</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/ArchiveTell/6591" target="_blank">📅 15:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/ArchiveTell/6590" target="_blank">📅 15:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/ArchiveTell/6589" target="_blank">📅 12:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6588" target="_blank">📅 12:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/ArchiveTell/6585" target="_blank">📅 11:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTKvlFoUPBA4nauUNmDr0lyU1y8F_SkQgQsC6nk6xel20NOPzx13-Z3d9Ak8i5XOmIOURr3n2b_xn2xCMkoPpUFFJOaZeO1rxEq47rvt0VYa_8UHOZQ5b5Ovxsa1w8pr3wepHv84-m7YqjxLXVSxKCkxBVEU8inGbOpuwsjQcsE62J9wdYCq8hglXY_R65W_hWHvf-PhQbaH4oi3EUgAO63tc24TyARFZNUCfBqLeTfC_GNzLhOxVqwfZTAQRVU9kEkS7Rp8UOMASklbAzSuTQoqpqFdXny9_TPLaB4ItfHEKQ_LpfHlDC3yDE2ISAxn0M_z2J-nuOtEgDR9SH3T4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه Orcafile دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما…</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/6584" target="_blank">📅 09:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/ArchiveTell/6583" target="_blank">📅 09:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/6582" target="_blank">📅 09:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/6580" target="_blank">📅 08:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6579" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6577">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6577" target="_blank">📅 22:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6574" target="_blank">📅 21:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/6573" target="_blank">📅 21:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAssa</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=Qp3gj0Z76YCqaQ9ENOu8Qu9MSr3sKLB__XTrG7sPn0J9m7AhIllD1Xil_rCNS-laxf2sEWVvm1_B6FWF2gSBkqVN741TW2xGycmgxa5VGTXYGMbz7-utV_5ZCaQF_glgsZZ3g8ybhSokfk1hg4JSIpTFAOuPX-yoE_IQTx0c7zpVbzl9VzyDKo7cXQlGy5gYBhAq_b7jIaKVR1Px97NysFc70GWWuoiRHINzb1iAz_0qt_2tDBSucKHF6Ym19qGhtDF2m1gyBZqlTRiLSjX79p3k5ZUX0f5nUlOZxAyt0wBwEqs8lP01_9jg0Bg7FHPqrS95gZzkBG8f3YniWXUAg0BJcOLVljXvbZ19nZM8yBCzM4hArhJ6k9H7zm-hEAfoFwxfSzFQWy1oveQRMZECZHWJOWZEsKvzcs-fIImEn3pW4OW0iZ3B69MyOcI1lZL0hW4dXaBT5_zB_TZko4tN7YTrV-2iWDXT9j-WDy99eRarb6kECEiRq3lQceXNSB22mfKahuUi0kF3SJ_DAuzGP2YPdKQkfZVNDaEHZseA7fsVu9AIDE2hfWFE-tdpASzDODyUTkU5XtTBSiyvTd3RZN1pgrgCx6VAHSK6OTy2es_rqKj4_Pvc3Ph_VnI82sOjHB7sE-RO5Y9CRn21rXMuwhkziDJvFTzjhGyMz-BgHnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=Qp3gj0Z76YCqaQ9ENOu8Qu9MSr3sKLB__XTrG7sPn0J9m7AhIllD1Xil_rCNS-laxf2sEWVvm1_B6FWF2gSBkqVN741TW2xGycmgxa5VGTXYGMbz7-utV_5ZCaQF_glgsZZ3g8ybhSokfk1hg4JSIpTFAOuPX-yoE_IQTx0c7zpVbzl9VzyDKo7cXQlGy5gYBhAq_b7jIaKVR1Px97NysFc70GWWuoiRHINzb1iAz_0qt_2tDBSucKHF6Ym19qGhtDF2m1gyBZqlTRiLSjX79p3k5ZUX0f5nUlOZxAyt0wBwEqs8lP01_9jg0Bg7FHPqrS95gZzkBG8f3YniWXUAg0BJcOLVljXvbZ19nZM8yBCzM4hArhJ6k9H7zm-hEAfoFwxfSzFQWy1oveQRMZECZHWJOWZEsKvzcs-fIImEn3pW4OW0iZ3B69MyOcI1lZL0hW4dXaBT5_zB_TZko4tN7YTrV-2iWDXT9j-WDy99eRarb6kECEiRq3lQceXNSB22mfKahuUi0kF3SJ_DAuzGP2YPdKQkfZVNDaEHZseA7fsVu9AIDE2hfWFE-tdpASzDODyUTkU5XtTBSiyvTd3RZN1pgrgCx6VAHSK6OTy2es_rqKj4_Pvc3Ph_VnI82sOjHB7sE-RO5Y9CRn21rXMuwhkziDJvFTzjhGyMz-BgHnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو بخش انتخاب پنل ۴ تا انتخاب وجود داره
طبق تجربه نوا و زئوس پنل های خوبین</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/6571" target="_blank">📅 20:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/6570" target="_blank">📅 20:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=RLYGoNZpiTs2nVsNsmqO9YBugiu0XnoLj28Y1GukCdETfJz8u456sKYSEx0UxDXnUCJxzgUoxeMo7mJ_09BODxeE1TLqIQaHJTql08O0qhnOXQMZXk1yGk_zo-vWF8Zul_poUabtCzWg0E7iscA3SdtPoJYLKd3-qfUxzy16QXFwTZasUUZiFMgeKVeUSifC5pbVbRpF5qAudvsU5zW7aZ17EIN9yP9bMxxfWZjFGUXJwLqUQd1mBT8RWM8ARm-9gReCTS3TzZSWwULLhOHIatA8QRALIwowNhQixEru7Im9tKMyHI9UNdnCql7ouj4f7I3wzL1Vy-ef0jdhUr4HZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=RLYGoNZpiTs2nVsNsmqO9YBugiu0XnoLj28Y1GukCdETfJz8u456sKYSEx0UxDXnUCJxzgUoxeMo7mJ_09BODxeE1TLqIQaHJTql08O0qhnOXQMZXk1yGk_zo-vWF8Zul_poUabtCzWg0E7iscA3SdtPoJYLKd3-qfUxzy16QXFwTZasUUZiFMgeKVeUSifC5pbVbRpF5qAudvsU5zW7aZ17EIN9yP9bMxxfWZjFGUXJwLqUQd1mBT8RWM8ARm-9gReCTS3TzZSWwULLhOHIatA8QRALIwowNhQixEru7Im9tKMyHI9UNdnCql7ouj4f7I3wzL1Vy-ef0jdhUr4HZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/6569" target="_blank">📅 20:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSRLLs3lycTX4KhUgzEN1CQ8zIqGx9GZrCZheD7eshL6GFDNktULA8VjRuC106Fz1GBifJeqPHbvHwVP8amZioG9ir9EQpyHQTXzT1HeSFhK9FDOOejXseXj-TMCGZLJCeGNno8nWG-e1HAN2hIHCKCLWZp-n-EA9kn4W1b953TPBufOnUvy7W-LpMzK8FG_Rnuw7Yk6Y2K6A8s7w2bVcP7T711mIEywHdlmcA6xa3JeWh2S94yPyKED3On3eZEu20qn30i-hH0CNmKIyWvn_zLM0FzRNiyrR9iE4nafJz3fXHDBVfHM3f4sjW3PhAzJSwUq1xP3m2ZGsnxoJemCOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/6568" target="_blank">📅 19:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=U88oQnE2ZxhGCSqu2g1Mi0Ha2ZVP6Kj-nV0mL3urrQbfRo17Uk1AGCMmqkPylFB8ynR-ZwU6WRU11b8ACe0dO6Q-P42cK4YFmqa0eMst9WcBE-7oYovZi8QNEcAaMbvKGWObxoF7htSmxWYIQH6QkBhup3M_UIJj6zTUTfamvlG4rpP2s3zrKykbNDJWtO7PcIzp0wpuUB9Gn583tIvuplDDfuOR7TO0FJLtX7tE0aaEsyn9rocrHnW1z58zFt7AGM7jQCac_yOCnUHThE92s_S57Z3FVY8Dqahw2RtfQFDhth1u71ggImI_WaHMiq8YXG1dxspH4t34AJC12Wecbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=U88oQnE2ZxhGCSqu2g1Mi0Ha2ZVP6Kj-nV0mL3urrQbfRo17Uk1AGCMmqkPylFB8ynR-ZwU6WRU11b8ACe0dO6Q-P42cK4YFmqa0eMst9WcBE-7oYovZi8QNEcAaMbvKGWObxoF7htSmxWYIQH6QkBhup3M_UIJj6zTUTfamvlG4rpP2s3zrKykbNDJWtO7PcIzp0wpuUB9Gn583tIvuplDDfuOR7TO0FJLtX7tE0aaEsyn9rocrHnW1z58zFt7AGM7jQCac_yOCnUHThE92s_S57Z3FVY8Dqahw2RtfQFDhth1u71ggImI_WaHMiq8YXG1dxspH4t34AJC12Wecbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/6567" target="_blank">📅 18:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6566" target="_blank">📅 18:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6565" target="_blank">📅 17:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=qtETRUswbGCDHXUJwF4jLXi3KUGzytzO4can-89XvS8_nuhnUmehhpVu1EtSI1mFy9kKtuRgWaqLuX75rHQbR9JOcr_ozkyM-AoUCjpVDiDhktAFjQrJ-69nKAaAxGPG6rNwMmWn7oApmK5u5dgod02WcnXwNgnA5X_7v4cCdTXRdbCaNPmOSgEmOqEBl6u_GkXU3POoaruS7q5ph_L1orKk8zLyKKyayTuE1i7wAAg8kewwOiHldwZjV1nD9QIB55lVLpImGI_C-hL6Bsce-yJf8ATFOj1L2Z3GPiyiiGOKsMT0aQFL85INynYpB9uj4jb4WyA_WEuUTuFXsgs7Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=qtETRUswbGCDHXUJwF4jLXi3KUGzytzO4can-89XvS8_nuhnUmehhpVu1EtSI1mFy9kKtuRgWaqLuX75rHQbR9JOcr_ozkyM-AoUCjpVDiDhktAFjQrJ-69nKAaAxGPG6rNwMmWn7oApmK5u5dgod02WcnXwNgnA5X_7v4cCdTXRdbCaNPmOSgEmOqEBl6u_GkXU3POoaruS7q5ph_L1orKk8zLyKKyayTuE1i7wAAg8kewwOiHldwZjV1nD9QIB55lVLpImGI_C-hL6Bsce-yJf8ATFOj1L2Z3GPiyiiGOKsMT0aQFL85INynYpB9uj4jb4WyA_WEuUTuFXsgs7Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮
Morflax Mesh — تصاویر سه‌بعدی در مرورگر
این سرویس امکان ساخت تصاویر سه‌بعدی را در چند ثانیه فراهم می‌کند. عناصر را بکشید و رها کنید، فرمت‌ها را تغییر دهید، رنگ‌ها و نورپردازی را تنظیم کنید — همه چیز مستقیماً در مرورگر کار می‌کند.
تعرفه پایه رایگان است و دانلودهای نامحدود دارد. با پرداخت ۸ دلار در ماه، به کتابخانه سه‌بعدی، خروجی با کیفیت بالا (.jpg و .png) و قالب‌های آماده دسترسی پیدا می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6564" target="_blank">📅 16:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZGcDdYhFNS0v3mlFJ4hoEeCwLZw3u2bvVpEMSm68YEqi4-dWO2QhOiPoeW4vDxcFdS5KKxXjiPmeF3_TYA-NwLBZE231uk9DfyaXk9NrE9U7_4zW2F9ne2j4EyNjKGHER4Uv50w0JjXO7-VCvBclACpSH93pTpM9iYxpSEzubh5XYwppDDYetbvS981oRkNzrnnYfnPOr-kkTCaLcCTwhd-UaBx4f9PrprZA4175IruTPBaez6aNi26_SRMlo33PUDW9JmtSEvdldPUWNtuL5AoT6LjhEMTXXCF4WO1VBNZDOmIN6h6qgEMPdi9HMKXF4h83TFO53TWmvtHLfIsPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/6563" target="_blank">📅 15:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6562" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bd0T1cbpdhrdHSoi8newpzC6c7CmA4Ss0fH66fLqf6ANuSPWNPQOs5uMGSf-EwLdJBnGE3VpaDvKTdg7puPUfs458NWnk9ukUYcvIAzn9k2E9eB6RjXjIJy6x4YALryDTCLDQd-jrENgTFCXe4ERB6AydKCBnK8JJCPD2_d3UP2Hz4E1yoYSfQe39jKXqAOvItwKOGyWhBXTkitpmjPJPzgbOIxHas-kBauZQGd2fLGogyK7SxfrMTW31w8My1e9T6aWq2Obbq7q4QtdzlxG6-07nFq3uZGcJL19fcuiYwFSlYLbFQC42oipcfB6XI6u8GqTuTEYEEqcachZKG9FDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6561" target="_blank">📅 13:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6560" target="_blank">📅 08:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6559">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ky36f34n3H6F9z_qKDqAmgd17JFT5Jg1XbAUv4aNrP1D1xukncGxbeOxf1nlVqEqGH-x9bktYw4SpfV_-qnNk6_I3qqoqiaJRP2CbNXMQImKJt4L6zs4zi9bsTRFa4MNVrhnQ-X9Nhs-LnMw5ON6dVVNe5XU243ewR1sqtZZNg0jtJ4eq1Ek7kmF9VJeUPLReQvHUSVIrOF_JP8LxDxAstR5z-6nmLQrdGZ4g5yA0CyqAfFRSpYTurIWKsV2UqC6t1EdMAZJQ_7hrggIAaGxRnIzTc2vHBkC4NehJOUU2q89aak3gHRrtJrK1twUDYfnSiF0alPz5eC5FZM_mbULqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6559" target="_blank">📅 23:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8491578554.mp4?token=M6zwTV2ldfqGAQQVH1atTRCx-c-2rdc1UgQAFi4GzQ_OBIm1qN0fGJeJvdVjas6cazBVpaLMp-NQ3a5EPpqXmf4e4oibPX9qVjzkeP2zW6HWkjGldnQ7iJv0BJHPdiFaONQZd9jAWzQFlgqXBSQ0bf8DVICP3BNBSAUdfbtwFZrTd0bTx6frmFrXM9suGVv7W5xTwB_OQzatLjGrlsL6dLDFIM3p5PS_KymCJRjtAfQqlpsxHxtPA4xtOdetCSdR3TTeE8pEktyETqDaeXuQkN4BCGWcHC94UCAMddd6aRhotm_elxqiVbyi0w3gaMpyRSFO-J9Xtk_5NbgEvoTm8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8491578554.mp4?token=M6zwTV2ldfqGAQQVH1atTRCx-c-2rdc1UgQAFi4GzQ_OBIm1qN0fGJeJvdVjas6cazBVpaLMp-NQ3a5EPpqXmf4e4oibPX9qVjzkeP2zW6HWkjGldnQ7iJv0BJHPdiFaONQZd9jAWzQFlgqXBSQ0bf8DVICP3BNBSAUdfbtwFZrTd0bTx6frmFrXM9suGVv7W5xTwB_OQzatLjGrlsL6dLDFIM3p5PS_KymCJRjtAfQqlpsxHxtPA4xtOdetCSdR3TTeE8pEktyETqDaeXuQkN4BCGWcHC94UCAMddd6aRhotm_elxqiVbyi0w3gaMpyRSFO-J9Xtk_5NbgEvoTm8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی افزونه Caveman؛ ابزاری برای کاهش شدید مصرف توکن در هوش مصنوعی!
🧠
✨
اگر زیاد با چت‌بات‌های هوش مصنوعی کار می‌کنید و نگران محدودیت پیام‌ها (Limits) یا هزینه‌های مصرف توکن هستید، افزونه کروم Caveman دقیقاً برای شما ساخته شده است! این افزونه کاربردی با…</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6557" target="_blank">📅 22:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6556">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6556" target="_blank">📅 22:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=t-z2FSvOO6luliHfakdNXP2tM9Of2A4T2eP1nubPVh0_zngKnIpzL-cY3U4_iFjqy-_rBPjQoo-fTealNLcANl7ZEovk44DFBbwKvNIQarZH-9rcMy1wzdcsSi0UE3_nzgnGclPStx_yWOTZKpOA98neAMBvsGzvYJXx3fk8rreM9I835a2Ohd6m9UxBm_cZasYpW2TTJ7EIGBDgss6wfcn-646PIDTvQykuEGrQ1-8I7nrudsm9lEH7K1IF628KND-GK-b2xDhC6PatxuV0T4VIDwS-XPs29n9YKToxc78BV8PszXzAWRhMRtTBjNjahQso8IhYfyA1XEk7g6MxtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=t-z2FSvOO6luliHfakdNXP2tM9Of2A4T2eP1nubPVh0_zngKnIpzL-cY3U4_iFjqy-_rBPjQoo-fTealNLcANl7ZEovk44DFBbwKvNIQarZH-9rcMy1wzdcsSi0UE3_nzgnGclPStx_yWOTZKpOA98neAMBvsGzvYJXx3fk8rreM9I835a2Ohd6m9UxBm_cZasYpW2TTJ7EIGBDgss6wfcn-646PIDTvQykuEGrQ1-8I7nrudsm9lEH7K1IF628KND-GK-b2xDhC6PatxuV0T4VIDwS-XPs29n9YKToxc78BV8PszXzAWRhMRtTBjNjahQso8IhYfyA1XEk7g6MxtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6555" target="_blank">📅 21:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6554">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExEbi2mBdIKcDnP42Hb-4cUR0XdT_m55j_uVK1S4T71tEe_mrN3MiPFlo15RLa4C2sY5SzKhX-pBWcq-jFkxGLh_awgYlhalmcDj2ay0YeKz1YFNnsGmi3lnGeGsUYszFbW7pZWIuPJ3_tONUKgnak9ZTgD-JqcO5kKLJqksS2KkvAlYWL8-utHdOa5ZrbBFjTz9C1j93atrfDG2Qkc99OXGg-k-YQUlQe2afudv_yiUTDFaWy1YdZ0Omz19a3jkEl2zPF07whPeY-j13zEusrmBtYI8_iCxMeh7II23DgFaAYnwsMagKn5nnTlci_ysiNNQMM-8rI2KoDv-AhSyXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6554" target="_blank">📅 21:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6553" target="_blank">📅 20:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6552" target="_blank">📅 14:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/6550" target="_blank">📅 14:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6549" target="_blank">📅 14:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بیایین با عاباس آشنا بشیم
❤️
دیس وگاس و عاباس
😝</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6548" target="_blank">📅 13:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6547" target="_blank">📅 12:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ظاهرا Claude Fable برگشته
🔥
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/6546" target="_blank">📅 12:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دوستان دقت کنید
تو گیتهاب پروژه ها میتونن ویروسی باشن
بررسی کنید
متن باز هست ولی نیاز به بررسی دارن پروژه ها
ولی تلاش ما بر اینه که معتبر هارو بذاریم اکثرا</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/6545" target="_blank">📅 10:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/ArchiveTell/6543" target="_blank">📅 09:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/6542" target="_blank">📅 01:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0Vukg65IGkRKBETtJV6a5UnM-1G5iGb1HxY6dks4ViCnko8ZQoJr7IE9x6dtbCv_sywf0Ev0BSsQvxrWWiIIhuoikQTBqn4DmyZajejIAu8alI9Vm0El2qwJe3R7S_gfEgHNzprbLOOmZBQDQ8QLaeS93N0kFn_ZqVdcPQ7mEZEA3CIz5-4DoN7nkO-egITsay5qE6jGdiXF1Ch4AHDTUwfQmE0B1sp7Sxq5owWEtitlG9qFhddOALF2z0XoPnGWhu7coB8x1oygMkl6N2QrnCz0ESIeC5u1BppnDbGYz85YmQGMK_4qQgTgL13GT5LlHWeRSCqnIzC_jUo97K2Bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/6540" target="_blank">📅 21:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6536">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzx-OjXpVyBbV9mHG_zfzN8_qR5bkV39HYnyuj7NZakAwySoy_aqSuolAIzArVUy1Hx-1mh4RNmqRvy4gyg396wdOwbxPaR9492QLerVuTHiUWceD629_nKsTE3TvzXKRWHsLjPPkaXgQaeDBuN-gyq42rOnF4pfwIMI0s2nShgE3Z549nJKyzaI_Bskfg0mP05ni9rREeoZmz-nDYK6Lh78WDP5gfTssDxKCqmAciHVzg197HQ8l-2bYGmZj4m4ZO_PTuw6M7ih_3qYjVtDhfoLZ-YYL6M2z-sFC8LaZ2aeKeWi-YZD-KxftL4ysXwLsH7gpUSOrQJ1pm40Owvj5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/seFw-VSt1Z5_hswSZbdo_v6CtViFtAlK9bhf2Ik8nElyhllXn832wzZhFj7xrsI8T4HfoFOW-indPSKi3ubNTHhQV8kdm8hXjSkgPMteIevEIiLJV7iZsZGqhtV_icBTFmFwDYa05rF0CLMopCaXiNuU-Pq3iheKEih-IHEKUKthmw8d1AhiaZWbhx-v7gq1NyV9ZgFNS1o6L39reAlLlZrw6vqTYlZjN7WRxLlbcimCyCd3LaiAPJZFoWaVNQpEfLVFLU700pKoDUYOTsCgdfSCyZkQr5aB2Hr93YvgpFWUcBLvUXnocbCy0ue7nR6MKkC7DSnIdsia45xRppS8Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BE47C9lgQ86IiySwUKIzxaWkcyIRBHCojGi60ZAG5gd12fvunNhYSP-2UV7QKIhHNrgPt4svG_xUQS5QJfPnfJvTH_rKd43MjtKKEns7a0mx2ghm__chuK46CZu92nJJLcZyW4LZWDU8g55gQSP4D6peeiQzd0YG6EGhEMTC3U_CprdFhROIZqbROrKKN0-JHWtngaOR3i3ccilMNcsrIvPD43aqGpLk0K62FXpIsJFINHANsSqOUmiMwxZ2J61i6yGVw4mL0yBScSS3GCfCBeK5DM3fXWnmEnlVRnid1BXB7T6t42ut0NBrw9wvu4VMIrPXC4TSF4LezfREBcP89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NyE91oPzdzmRrl3aHWElAA-GsGVku0ug9eovcs5uT84feBN81tI_PGQkP3f7RMJuBb8lz1hcrSWj5DIZgSWwda-y0bHHcFfkaIzXnr4ISOOyW4U_l01hLQCJGiRKMznEwJvRbGc9eSRWc-GaPlGhTMit_DzVcDnl57L_ipm_eNit2Ic_vsmF4uSbdmfQXwIhoqoZiqrzz0cNNfcdn2CuGjBFwu6mr4aQ5a5ojyh9rWBAp3vsblQjvY_O4fYpepbz8NqJ9WBVEwsY4hgwg_vk99qODcAEfflqkjmTyuYiMV6QMlGQ0ef7VkD7at5e_H_G4nuTV8CqiolHdgoRW3lJEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/6536" target="_blank">📅 20:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6535" target="_blank">📅 18:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6534" target="_blank">📅 17:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIPaq80t8quYuYQ4eeEXWGfyxstNb4VTpwnns3wbZs-ALqFnr5GJGGXxLC6z5qxrSboKtxTmDRu4ovdTDTUeLFCURrx3zYr0cPrmDSC6owSlZsQOYNRVxhfc-lF6ImxPHRIqwlOV5h_Hyxqg2YPDNKQKeWBcvN6-Ok9JnQqi0T1fTdarO7jF7Tb4F8OJI8Fnq2x3iX3s_-ADxblcPwTTHNrG10pMt5hhSDoJDHDwxrN1D4BeZr62sIkn0a5pMZyHa6D72Itx5qcmvlVY0NJVMM6MAJp2VZHOqU5mi_U9aJPvZVp7GuJD46RfnnyBwmQyrywv10OFe-f_ozLlghOEtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6533" target="_blank">📅 16:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f-NaRqA6azOmW9hQ-ADzvhvU7wlMZuw2C_kjQAaVNcOgy6FwokZ_G9MCzEpfTVYQNJP6D8T5o465l-gF1Q4HZGpClq4RKj7SP6VUEjw2NBUDS1mxr6uyerObFZAstydlj6UJzehbOPcZyWiRZqMXNlQrFZydtT7Hb45CA_5sgkDRKbOdMZPTpp8wdlbzWUsJtVgLd2uHky-PAXLp-hZl3tqdSNvWs0eF4bpzY57tNJ-0YFyki3wtoJEFXRzxpPhvxcGW2ThOlpiTBbKpqG0Q6fFFd4ZLxpowzQGAKf8m-AI6NMEtFoJHZ2PRTg_vNvb9IEeh26pRI8nrnskfZj3zKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fAC6qO0VSiVEzN-5628YeS8A1wiWF6b1bX1sHoKbdek1vSiCFrn7bWJc8fc3q40kiTOEwMV33lNeowlgnnE45YKFN3hW4Xy_bFDBMzpH1i0tAJjiueFUoeu2TUI1jNlOzJASZrnRn9BIodKl5ZX-RoQ2w5oHKqNHRJTuOthMr3NpDI3xgS5kL_B44EbTegNI1OBnRr23bvq8WIyhQ1qDSNtD0iu10jr3NNQKr9eSsKkCD7U6HV4xWyMKhb7iPvCZ6NzlBsQzn3M46dUXNW2CMLjMSgDd0bKcl6YmKjto85ybXZUIaxN6_BX8HdMOXJu0UFqcWtjLzo_Xg-c2IDbgUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XkBADp8aAgbqbdLJr6ZrJsNED_mTqu25VaDLr7TU1cCUPZsg-rP-k3Rgc5phCpT8JKM-eKLFKl2w2bApWdcDp5PofjXfJW5572AzUuFeKS3bgxFAJfd6nK4SO3mvq8blMTzOrvwh4JbMyDnfFKkVSibuYqbjprETYcXWCzhcqZkKAbdj7BxtB-wLm-jufk9o1TBZk2EcujRw733VqhwMnDJ6ecqzCGP5MZEBdVefHt-1koipXJ39_IBj45AmdbU5DuuT0UYfQoN4pySnONvJBggqXdyY2zOPaFHbv8cgEKKtLj-OFHSfsvD8BbSqWeLR8y2wTJUfyJ3ldvvOW-nw-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WvD6Tns3oZJOReh8DHw7WGDBv4jkd7eYg8EtvpFsnT5bWPV_cZZT0vgRVK1bfau5FcQiFxFgsIiDNEpVhckaGimqKlP57EjTdEGIqQsRfg3Pw3yKzEkZMJmS3iNtFfqlPqfnyRJOctZzcyi9w2J-Fx1CcAkEsm8sqQf3fb1a2FtbpvpQ3nOFMlDO0ZE2BUiq7YTYsZCVAfnBPl3RM3_z8PiAy4XUOi_toaQOaOoT8Boqjr0WXoVQGgViAsUqhUWICbgBRbGGHkl9X0JKo6lJqO4l_whhtlw9irVFcSDZBQ-omh8W64DlvnVoTKi088PNAUsBLE0by-uGiO67d1qIWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e3aENY9qhrlbgTED-rUNMPt_2Ly7W4DUBLaVd05i6O0aQpVV0KzW-0H8Nt_Owl8Onv_4REMGAGdWxM-jsz-iBgljZ9rA2VJ_Tci8IZouGTTWmVbexsQOZDRTPZ7sMHHH6f-MdvuKJghkM3Ubj5t3E2eSD6U9uIBdfBpTXUf6fNuuJd-RfZ75WP9_D7VjYmAXHDAhS9C6JY6NY9gnaOneDV1oon4WZdXoTnugcfJbO_BA9gHk-MqngzEFjn_54YkJEPMdx_OH_ykN_SBVQModvjsaI5PXbB3iegTQK1M8VpN-SyOLrtcaxN4HdQgTw8D36yuFTXP-dTE22SRce23w9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lNCsUPLm7BClhAn9mY9uxN1gyPTFMkry66uUBGAOJRSt7MW5K9ieX3I2-8-KZr5lDfY2QYNRZpEPUeBHNz6S41ZTbklt3fAQccHIjIFu4QSYsQi3Ni3QxnUUYVTOUpY7ZWQkBfKZ6AcAAbR20pYi4MjM_QGzWAmv51szUOorHDyO855OKuYlzPNvEKZzdOZBJXKic1sDat5M6XW2eyIFEkU9W0cvpbDis_cOUCA4tz175ewIpvpKFphbMqTXnt8UT8dl8X9wjPZwrHSRkS_wT5gQZz7F40ST8emejKHkX4Jc9GzA83e8hy8hQoiXa283FerMhx33Mav8uPQ3S6hOwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر منتشر شده از بازی GTA VI</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/6527" target="_blank">📅 14:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6526">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hj8fnuabXJcX92MScM-LIBuZVm88xj-F7g69UMQweUf2WvEAbaYMA0Z3W8KlQym8fv_1QAKbTx5cYnvS7gfUkBM5aIpv922wm7SNLSpfyOH-58Yn15_Eg7mWzC1MPe1ZzFFKXuDRmLztF0xPueoJRe9tyhUDGsk-fiHcD71XvUi0NT_tdakB-B0-UrroEEGWgxlY5E31fGnYu3GSKyMWWpenFl5h_hiSyevzYvyF4hGZMcH__3nsIEWGmTajsqSYFqTm9T57-BktbY4PYm-sd3h9dOX8NFB_Im1AO6MWoeFM8g3Z2p1NY33LJCBDQByTCFVNlRERrcz5YPywN2zHZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/6526" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6525">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6525" target="_blank">📅 11:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6524" target="_blank">📅 07:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡 یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده. این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway  را فراهم می‌کند. از طریق خود ربات می‌توانید:
✅
پنل موردنظر…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6523" target="_blank">📅 00:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=A41CoxSvGuo5hfmDzSVji1fg_c1kBDVhJsQGU3efgQ_KhR1mpSPXX7I5XLwtweByffmkbHEJk0d_hqBkBNNte-ZNAp5YF6VpBYFi8kONWA7HypUgFHw-5CWis_P-YDYPqA3uGM12sKDdhpYLYEquzNliQ42Mo0uJUWGg67Te1xS-hYI7yAhheK71YZnaAELD-C4Er_c-vr6EaXhR3ENUYAcg4qjQL-g4UX_C5MY-QsplznpQSYXcJ-lH7KcMOt9w6Gxe3hTEDRrMXmWpFiS5yphAaJvVjzgzseIAEDZ5uVlwl0r8XNUrC0DCjx8zQ_nwHFNEYGQtMCtX9lbOGVeXfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=A41CoxSvGuo5hfmDzSVji1fg_c1kBDVhJsQGU3efgQ_KhR1mpSPXX7I5XLwtweByffmkbHEJk0d_hqBkBNNte-ZNAp5YF6VpBYFi8kONWA7HypUgFHw-5CWis_P-YDYPqA3uGM12sKDdhpYLYEquzNliQ42Mo0uJUWGg67Te1xS-hYI7yAhheK71YZnaAELD-C4Er_c-vr6EaXhR3ENUYAcg4qjQL-g4UX_C5MY-QsplznpQSYXcJ-lH7KcMOt9w6Gxe3hTEDRrMXmWpFiS5yphAaJvVjzgzseIAEDZ5uVlwl0r8XNUrC0DCjx8zQ_nwHFNEYGQtMCtX9lbOGVeXfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش ثبت دامنه برای رندر
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/6522" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6521" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Drz2WdwdeqLia_2NAoTL8ITzvwKq1lp_FHbxpAyWpDReXLNCFFYFhkhAsoNFfbwISmUvBA9dExfS7UgwSArPZRzgaPs9-D0X3ZoWJzzNxcU6wbxHpF9h156svbzVt_ergFPF_-A-iYGJXc64SOqhYewKrzg6jiMtTmXAH9QRNg2Hs1BQ8iLvnzj0rsFO7_oIAlf3BE1ZbWyrKLaCBnQViezFL_JBtBtxx0x7il9fRLYVcT8WlxEMdCiMCEKdvAkNYlsYFfprDhvqXlVwbcUU3zlWXtLwfAdDN_ctVqEbgcHc8MkU1sDOTNqjdIvb7YmCU0NvSU3h8QAPqBcAPbnyiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6518" target="_blank">📅 21:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6516" target="_blank">📅 20:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6515">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6515" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6514" target="_blank">📅 18:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GP1UeimD1nu_wLHqUn0vLnnSGVpImZSNz7z1YnC0Mfvt_7E_YesGuGngo76Q_YWBNFUu474F7fbYehNPWKSIxyrdrjeSmeCCrUa2_398jdRjmm3YnOoiHcIdO6xQAirI_GNnmCaz3NAZd5Cc5WwigBG1BSWkDXTY1XwYV50MVE2QMWgKOSZvEO3UQ_IQqN4t-o1Y6nVr2uJHp4GXxcAOEGxygGy4RbAgGRlIKYgWIZSBz08l9RVTaOd189BDbR_LL28e1G0Kc2U6ojdSO5E_3ENwycSdAIutk8F9sbM4oL0FHJRNJf3vvrxOTN-zETRYKlUU-HkIGYOTOnQ4sQygPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6513" target="_blank">📅 17:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLo-ApJh0_1Mkf_H0noEhbFpSYr42l2xMNhufytMwMrSSNvqzTUMpPrUDyKp3fu7ueEDpC4jMSlO8bmnVgf3UCQ_m4Z5tiLjccc0-asFzJa8i54tiqaK1D4BdkDZDDLTd-ZOZ6oT6kebtDcz-p1BqnqvamrUwqHhamdnKZjVCiQDihe3zLZSI45JVDzvMPZAoSU8SlbJ170F-YuNv3W8K3OrF92oXiY0Wpowo9mBe_Brho2Zo_Nwrkwi1yHseRSCuqbbcSkwUjyPzQJgAw4Jzm9BcpLwITknrRNjHlQhlmMcxD92u3keomzaLbR0vydFOwUsj9jxQL3JDfOcsSj_yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sdg71cZcQtPlTdAr-G4eYfuh-qnLGf6DdZN3Wv6WDT3b82iDQci_bK-JPvnAWpj6OL5nMDe2W_JYJDt_TEmrxgXCpz-peTljY5b6VDp2uw1I762l8iuuUgPBH0CiwLcCU8zUCiAHxvwquwlw44skRptUGBFhs4qpf4q2p2Q11JH0TcYi9ofG01T9AoiqiaYS70jfwZ6K6m73k_-kVR6ma7rspgH5-8KwfsPN37dZyW4jEo1ZnDFcejfQ3V46FKh8D45JfyXpX5OtNHpPl2W9zGqw0eou76F0-E1Q2aYlcPsWTJ2kTL8LczjQmkicX1utOm9UreThRZ-o35Wuho11xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
Consensus — جستجو در مقالات علمی
موتور جستجویی برای ۲۰۰ میلیون مقاله علمی. سوال خود را وارد می‌کنید و مجموعه‌ای از تحقیقات مرتبط و خلاصه نتایج آن‌ها را دریافت می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/6511" target="_blank">📅 12:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=ptKJTJOLRCzWeMmX6XPrYBK2H6PiRV4xYnVkhE2agYIlj4Jy8W8xXmidtXAh5HZvuXwgTFhBGBBPRxDV1_akRgM_SR7WTH4H0-22ymhBzSiptikfvXi0l9UkhRlhFVzDJByRU5HTi14UkuurvgWxLENK_kDrHxg-fpBWiQwxTkkk1yULfkFwfHU5WP_ZtpzqpLYIMJMHVaN1RMkk2YEIxtHSpVT_th0UYV28uDvDccOgoXo7IMesI2C-mflGx4sqylQO5ZnQ2QK6OF83IFkrYCyQUwiuZklIxtufGfWHz8pHM8NgaATAPEPJ6XvtgcQaAfq6lixEVy5OiZFTSog8PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=ptKJTJOLRCzWeMmX6XPrYBK2H6PiRV4xYnVkhE2agYIlj4Jy8W8xXmidtXAh5HZvuXwgTFhBGBBPRxDV1_akRgM_SR7WTH4H0-22ymhBzSiptikfvXi0l9UkhRlhFVzDJByRU5HTi14UkuurvgWxLENK_kDrHxg-fpBWiQwxTkkk1yULfkFwfHU5WP_ZtpzqpLYIMJMHVaN1RMkk2YEIxtHSpVT_th0UYV28uDvDccOgoXo7IMesI2C-mflGx4sqylQO5ZnQ2QK6OF83IFkrYCyQUwiuZklIxtufGfWHz8pHM8NgaATAPEPJ6XvtgcQaAfq6lixEVy5OiZFTSog8PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6510" target="_blank">📅 11:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/6509" target="_blank">📅 09:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=Km1XQRhrFI3IuFJ4OHNZzVU0iCVe0sq_rcAAjRTAiXuGPLBQJXVxiDySEv_XIims_XEKBHDXOB0qWU8pmHNhFoVIdbzt5PN4IpGrJoYBHGpQBf9PLgeNXyLcT5kAdm1lRqfKMXRJzWtWZba9fFdwPexFD32rj6fgqBJVYE1rvk5RIkqnqWwHzCJpgNDUekBdrcLBKh70xetoZ_m2PaJTEYVWx7LUYVfNzzcDgQm3Bpe_eS9lE-l_LotBgbBSfjX5R4Uv4jFJkPdpjOLhB0FCaN2BUeWA_5IEshfJkndFrvHdE4AsF8TlCiGzA6wv9oZGwEUvF2MwPCEA_Vb_KMcgoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=Km1XQRhrFI3IuFJ4OHNZzVU0iCVe0sq_rcAAjRTAiXuGPLBQJXVxiDySEv_XIims_XEKBHDXOB0qWU8pmHNhFoVIdbzt5PN4IpGrJoYBHGpQBf9PLgeNXyLcT5kAdm1lRqfKMXRJzWtWZba9fFdwPexFD32rj6fgqBJVYE1rvk5RIkqnqWwHzCJpgNDUekBdrcLBKh70xetoZ_m2PaJTEYVWx7LUYVfNzzcDgQm3Bpe_eS9lE-l_LotBgbBSfjX5R4Uv4jFJkPdpjOLhB0FCaN2BUeWA_5IEshfJkndFrvHdE4AsF8TlCiGzA6wv9oZGwEUvF2MwPCEA_Vb_KMcgoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6508" target="_blank">📅 09:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oX2SqcLROvyKzGbUr2SqfWnyrchFhOFCGfBazOFNCzBiwAf6XRG5RfK44F8UcJKPQfdYvSLX259HU-QPdqoFg0AJwM_5J40Rmc9Onpr6Gp9EDkZoTSDBoceC0kIZ_cjHpHZUwJCEjtOZESY0gP8MgJWBrKV5Kjn1MgzWRHoHczKuwbedgRJwbfPnqZq8UA_Z9sYjgrZUkaclmOCIDwJsjA6eQG2GDQtwC-TFp1l5NP2rOJ862QTz0Fuz0drF5fccQqWPudOoiyE38fnO7kY3bQrObjZxgS6QNwdGspLhsx5NCLQKjVJ3Hpu2lag9SP9ajsBX3iH9shPLA1Y0YMwucA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452211db9f.mp4?token=bvQHqWSmgkhI3jzYjAl884NWyWyjfI2dFY_GDphehtB5YJsnnxo_dzHplkq5v6ts-XL46YBbOPBIblO4HHxPeSMbQzNj3Ri2LQzMfF3Z1rjdlpF-zmFohwk3UP8LEbfwRDKe8iNQ9zv4QCP9vPzUK-taGYwLCVH1L3jYvjkJuna89XmdBiePm1yGRqly5Fz2Y8uTlT46d0woqpJREnt8dlAmzBQLZGzgtRPr5s8scUoNvxQKAMIT3-9nzFHVYYlH-gKYBcq2lxJO7LBjIDU2QAZ6XfFgT2egZWaRG4N4-mMmD9WtKoCIePCHZSD7Jkb13frG8iEiMt_IUZJlvqdB9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452211db9f.mp4?token=bvQHqWSmgkhI3jzYjAl884NWyWyjfI2dFY_GDphehtB5YJsnnxo_dzHplkq5v6ts-XL46YBbOPBIblO4HHxPeSMbQzNj3Ri2LQzMfF3Z1rjdlpF-zmFohwk3UP8LEbfwRDKe8iNQ9zv4QCP9vPzUK-taGYwLCVH1L3jYvjkJuna89XmdBiePm1yGRqly5Fz2Y8uTlT46d0woqpJREnt8dlAmzBQLZGzgtRPr5s8scUoNvxQKAMIT3-9nzFHVYYlH-gKYBcq2lxJO7LBjIDU2QAZ6XfFgT2egZWaRG4N4-mMmD9WtKoCIePCHZSD7Jkb13frG8iEiMt_IUZJlvqdB9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/6505" target="_blank">📅 21:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njafDbh9rvFFuQ8h3NV_UXzD5Nf5JpWUdaWOp4PEn5-KqtPLs4b7LRECTz1oP7xZLvkr-k2KBC7o_wd_DL2dUTiM7taTreBDxk4DBdlx0gE-UAK0Kp3AQnYp4ECTIol1_5_Y06tsBaDnLnRsZ1-Z-ZuHguHXpSnASdsbWI_7EDEK_oSIBmkiOSR1o6M13Y_kgSeCuOeyXZ7TdjUXnrjcg2BT9tbWBw9KV0koFPmQu-Kl65IHtUdyyYDP9ExlI-cqW3BRkUtBGDBzUHrXgqGyxWHjPQQCbzupVMdfX8GNaGelswgqpiADqT9K4B5EmnbQWSB71qgb90LoJZzx96kU_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین سایت دزدی دریایی زنده شد — Bookracy در سال ۲۰۲۴ راه‌اندازی شد و به سرعت در شبکه محبوب شد، اما در سال ۲۰۲۵ سایت بسته شد و حالا دوباره بازگشته است.
• درون سایت تعداد زیادی کتاب، کمیک، مانگا و انواع دیگر محتوای چاپی وجود دارد.
• تمام محتوا بسیار سریع دانلود می‌شود. می‌توانید کتاب‌هایی پیدا کنید که حتی در کتابخانه‌ها هم نیستند.
• همچنین امکان ایجاد لیست شخصی برای مطالعه و افزودن هر چیزی که می‌خواهید وجود دارد.
🌐
Site
#Bookracy
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/6504" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQF4SDFbW1i3Uvz1ct-1fJgfNXnc9r4hxPzXL_6Bc1i5BCRHlXgNPAhYcEFe7Rxd2nVcqhDKAay_54y0HiGFkeJo0r9g7wP_71bvusCBXXHfLbqdWInpQHfPB7zg0ziDoKqvf1Q3Jgitt5Tx_mV4Io0t_I7pF75oPLInWtJcJzU9HqtMLu1nxaEMALaaylwC8HFV-3aQtrG0SfCCzdMZUny97FoLCmQQFOQxffittkmM0z_RFcqfE2DIm-nwIrEMI-ISDjFGiLUVJiphRUAq4HexQ7B0mBC-sQTJfG-b6IPqIPcuK6WcvbaYt4wu93KGZNjj-DvT0o2u8DcgKwHlBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6503" target="_blank">📅 19:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAJBE0OCldFcNqaMMT5W87Akk30TzbzOk2rv7AQBy3TNOhANud0hCzFrw88mwAYKqmSPqNwCDUUTwxq_9kb3EWnkGkWtWEfvmDHfY_pg6CLOsOPpwxLKtvSSKyjnUA0FlGfhySsEJAaPT3FWoQDVvmkwJR04wMwHDI7Y5Avb7cp2n_hARR3rMA1HcD-ExR4wqyV_fcNGH6-Hyj1xoGxszfxz9JK0HECIc__0H8Y7FFjeO2cJWDTF9qylpfi80CkLGMgC24teUsEEmHWxaDx4Dyh-A8QF33XA_8PW8Ho0Y-GqxUn0C1jyrK6OcbWNmZouOx4Vf9eIdtMUNd3qMc5tmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔗
tiny_computer
یک محیط دسکتاپ کامل لینوکس (Debian 12) رو فقط با نصب یک فایل APK روی گوشی اندروید بالا میاره!
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6499" target="_blank">📅 16:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Szv9oa8ydEZMgtORc2Bbw08zidH6bDdOjOiR9Tzt3bURqoxJlBXU3ZVyf8xFTGuoNa4acjhcaX2qg8faEQ27LFZulFq7Owul7DSXDPPb1U37eBrB-Jt_D4wLAEZSGYZ65tGtGieRdBpaJc7Iq4pw5yymvTfgc-QGSkJ7zv1PxCQsTeDXsQvU-t8pbSXlinrEpHRdRvG5pMi1_wqvGbdmiflRC7NGlnaZFEBzMxZaV0X2-7BEppo_ShQeZMON9B9F2QvK3JD00EA8_sGpN8NP24CsFHMJ0zElb60F7jkzuQTlmffGZLtefsPbN4nOtkWyl6XFGfFEreW-805o4tfTZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ترسناک بقا که قوانین هر مرحله تغییر میکنه ، در تاریکی از Cobb فرار کن و از سیاه‌چال خارج شو.
🌐
Site
#Game
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/6498" target="_blank">📅 13:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=vpVshafpkrwoSS0Ci0uhn-2dMlUVl3iUO45_v0EjVfuS_xNPDIHRw0g-TTWLYxTIRtY2AXpz6J8OswatzH1WCIhaxesFIhFKZ0Yn7jQKRn1jAwBDrPJ7OKVQwfZRbx91BhRmIZ5l0OZJGsY5BC_RLqYcMXP4BX12MN89UP4yRDfHFf_knkNYj7V3q9Ai5z_KwpwtUuat3gXZSbyZXmoC35SF7JYuQQgBIeu72fPwLgIdsNClMvsWMH0ed0iCnOMhN3mL8SVfpG_O7QEqBG9anJAHpjDquNeOyXGPi6xRppglk8C5xT3lltB_Dq86jH7LQc29sK1HxN-OKyzOgS1PuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=vpVshafpkrwoSS0Ci0uhn-2dMlUVl3iUO45_v0EjVfuS_xNPDIHRw0g-TTWLYxTIRtY2AXpz6J8OswatzH1WCIhaxesFIhFKZ0Yn7jQKRn1jAwBDrPJ7OKVQwfZRbx91BhRmIZ5l0OZJGsY5BC_RLqYcMXP4BX12MN89UP4yRDfHFf_knkNYj7V3q9Ai5z_KwpwtUuat3gXZSbyZXmoC35SF7JYuQQgBIeu72fPwLgIdsNClMvsWMH0ed0iCnOMhN3mL8SVfpG_O7QEqBG9anJAHpjDquNeOyXGPi6xRppglk8C5xT3lltB_Dq86jH7LQc29sK1HxN-OKyzOgS1PuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZuwMzJfrmlyH9PI9dd53Zhzvlb3kkCYxvrssD7jXufDKLZOMpgmPhnZPRI792HlrKEJsl8rlWtB7ACpZVtS4vVrESX_6-wNYBLvGiBwf3MbnHKc2DlXR2y6qUIVCUe8WfOjm5PWn_UFlDQiuGJ8FlIeQlPoF1zo7CxQWAbkUacqF7NKum5czjHf54Ge_lTekBOI9WkL7r6fpl-PSug5cavKvOOxscX159VQfqFu7BWUdSQYjlR9r9ziimYJ71UnhA1djRaTdMyLHOCMvwV-NNROkBGFMpk-xX2Vzp0phB89j70HODu-aTpTFtiOKxc_TOQnk2fGzsNeqn-ofr1i_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی Sakana Fugu؛ سیستم چندعاملی (Multi-Agent) که GPT-5.4 و Opus 4.6 را شکست داد!
🤖
✨
شرکت ژاپنی پیشرو در هوش مصنوعی یعنی Sakana AI، به‌تازگی از پرچمدار جدید و تجاری خود با نام Sakana Fugu رونمایی کرد و ثبت‌نام نسخه بتای آن را باز کرده است. این سیستم یک…</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/6495" target="_blank">📅 10:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vR8Sd4c9Aor-YKtE8AjQLKuRWvYAePeFBlaOSnAYbQBI3NQ-DLbkJ3YvLbqT7BQhkX0IyCmsZmb43CJcgPbTFnP6sI3YTA0jOPCmQATuQMdMFdoWJ_VnTZyrdn_igwmqnbhG1d8gC6u77DmBfrZzwfCMKl5lQS11xe2WlWds0Bl6p0TZ0uGMw6TkqIiP_97DR4euvZ0k_sHvnSTSn3tPMJPUzKiWfHEsWLyr0HDPj3tmTS4UIb6FCoCwKhVII5JchlEXfI8mBg7p0iuJBPMYrXX9rZJGu6FKqQQqUw21hL9SJj6nV3CQgbP-Vowh-5kXUEdrxylM1nO4n09SZU63Vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/6492" target="_blank">📅 09:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/6489" target="_blank">📅 23:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6488">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/6487" target="_blank">📅 21:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEB6IkT1aUgaFELXXACqL2SocHPg6ymCUGsEXvwXWse1XYLVpPjq1upEIwYarcofRntihqH0bHMxxAie7-CmArlN9DPZ1srDYhuyFm1zubO7Z9ZpCFbbH_nZ7_qfi9nL5tHQgUOCkhAVP4-Zp-NRvQ6uMrIW0FyTqaIBH5paO469NR9XtgT4qxLEn-Lt9TAGarY6S1C5PKt3hwZEJCzxkdDrbLGnfSQrNUYAFTpN31IjtjodtWByu_nRYj1SA8SZgzrFsmePmBPneCU0lzu9ibR0d95vPzL4O_TD2uMD1-XH8KOiHY1oVM9huIrh0LZw2ZtZ4wMn6Oox3WTw3ldDBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت What Is This Movie کمک می‌کند با توجه به صحنه‌ها، دیالوگ‌ها، جزئیات داستان یا نشانه‌های بصری دامنه جستجو را محدود کنید و سریع‌تر فیلمی را که نامش را به یاد نمی‌آورید پیدا کنید.
🌐
Site
#Movie
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/6483" target="_blank">📅 19:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsmW1i_hILskIZc1bBd-n3byJzAGceQOyf0AWNP11EDjRGrwSug-p-Yomk-RaVETGi0ZPCLjCRBEBoBLyV4cT49s4r_LTfMPuZM-ZRBIIJdA6-yyuFdXlTIZRYMTa7z9kpuNrEDQw8p_33fCkqYfdLw80c_OGZ0lXbPcnRH9Wr4l2qru5kZi365INnyGFiaEgSBpa-FYefUpypcbFnIk5NkBW0y7YkdmsTfRslw3zykBepWGDTbaZfPyRiakWosjJYCTg0hblOeIC1O5bBoUV7xMSms5vDuUJDMMItclddwK6jQiwfN272yfH0MbIBifyxN9_SAkSrGopgNNT2NAmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف رایگان واترمارک Gemini آنلاین و بدون نیاز به ثبت نام
🌐
Site
#Gemini
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/6482" target="_blank">📅 17:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/6481" target="_blank">📅 16:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFFv3JD71aMQPQdg2qWtYF7KvbJNiS9EzySw9ISYhOBeGFbj3SKU5sJhKP2Ix1YvRF_Uw1nkRA7P5bJV0HwJMq8YcERjIFK0QufMjn_mkFYRfyePGjjYTNxt4Blgir67YOxWt7KHAfiKbVrWUXn_kiYUvw9RjbrH6IVlGrrfp8K5xpOn5pTTttOU83z8arrfcK43eO2128zFEBuvFf_l-jaFBqUB1fXO5LqrtJ0VeP86_SQGFVQUvWDehDNHOg9Fx88yK_1sObGIYCOzZD8P7atVONoiCXYhtAOcQLkrPvnOPPRkLgRIgZY2P2ujt7NP-RVk_c_MmyCeg2uXwR0ZMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXuODXRLZpRci8hDwtNWBalDOLg6hEo7o6wxd80tx3OAgRM1GJz4C8v1tTwhbYgd5Vg7qvA_kpntsgO_LRv8HRmOOKT83_EsOxMtJKAtUQ2L_IgwNC_wEFGt8VY27NHSKV7dQS4qRr9M7FA1TJM8lplZEnQzbUCCj35bl--DqGDwO-G-UrcamltTK0NHz0HdSmTgyXc5E5CJ3MMTz0-Rv19u7RJFA7ObkBQWkvE9xv5oqPapx1YiKFMFObyalqlQSUrdL5rQtu9ud4qygGxUNBUy_N8f8HNYUbH6xP1OZtFxEGLcnxhej5ZAcVK1ehHgZasrY8uWGbyU2Zl-RB2QDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyjdNCRhv3au-5bkPN1Nred1QWrUcBjsmHTW5L4i6hbIj6MJvyJn7UqZoDrQHtOL6bgyTbMnRttoJIXMrpf2gjlZHNSvl-Dv7X_pX41lh982jpvIyX1g7r8A1S-fqa7fb6BirWJ5J6_u-IXmqNk5KjVrRKxDPNlydlrQFo-dKoeri1I4UqmFWy6sAcv4u_TcJHx0Faym2IhOXo03O5f5wK3ZAjn8xrdGhl2qspCtT_FA527FlP0lyyID416gX0i9kXM5xP_Lts_mk-Dia6xRdc0qul4KQUcFofjufGaZGs3kvvAYvgDprsn0xcSjnur4Or1gxwLYOhqPnFM6HP9UPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/6477" target="_blank">📅 10:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6476">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=bQErmhyoxmglg1vGO36fU7ONVBtN5079DimEPGkiCAUyADpHaveacfhYvzYxfsozY15gnr6vh1FMV-CcpEhIi3uRvYPuWevIAJ1IcMp_82_hn9I-QxduzNQVvQtEdQuuaDMbSlpiBBudnlwinQoSb-4LoI8J1zk5kif6xkRugHZdARuTcDsyrvbR44keFt4qr0LDQWGqSWXh1Tmh--k8K_6oF2p59HUT0W6X1kP62nOw4bWs2If7OJsLtZr9WheDNoqQjnD92CBj_CH2dgz_2FLdFPiU1H6l-6K1XaHD8ELyjme6FMm7fe11IjRLjmf9M8FbCYWRYGpbBzqt7O-nDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=bQErmhyoxmglg1vGO36fU7ONVBtN5079DimEPGkiCAUyADpHaveacfhYvzYxfsozY15gnr6vh1FMV-CcpEhIi3uRvYPuWevIAJ1IcMp_82_hn9I-QxduzNQVvQtEdQuuaDMbSlpiBBudnlwinQoSb-4LoI8J1zk5kif6xkRugHZdARuTcDsyrvbR44keFt4qr0LDQWGqSWXh1Tmh--k8K_6oF2p59HUT0W6X1kP62nOw4bWs2If7OJsLtZr9WheDNoqQjnD92CBj_CH2dgz_2FLdFPiU1H6l-6K1XaHD8ELyjme6FMm7fe11IjRLjmf9M8FbCYWRYGpbBzqt7O-nDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ih4Adt4ABMI5fp8kMrynBSdpW7g2F_PKK3MAVLXLmcey4CohLFeYMjpVxORewn8rYhM8t09QaY-caQ-I30ZT1B1i7EdwWvp1y9oAx1dw-WrQMwCzdOAlY2oNq_O-Ne454KUe_zXq-6uX3jSIkU11HUwaaOuSohNh1bj55Vso1VQwOitEVpUGdUGSPbKwAnP0fSrq5R6qhEBOrVUBscNAqJhoBvilD-ogdmZy52XQ_d0dEXvbTYLl-q2RwMjPtGgP1E65DGgDdQIQDGmX2_GpF6N-XGtkBB_0FTb-fqz8PXecPdFvoGku-BJ8XzKT9l19aUdz8Npf1u2bg4sQYcyZxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRlur940HjQuZkHVjrV8HftcDwsVXXRZ-4cCJleSVIe9d4B18kbv72kK82X0s7JQVXCJKXkahXGeV89mu9ctfNBQM_gWgAGVbNXDcdAeLBwESMC-WjkquUqttUqK3RdeiRXBha5US_L6yP4u6WRfgXI0Nz-iVI7cPjFRO1QimqsECsCMlhfG0AcShsu07xtM77nkYXhIZvDiQYHfOR-IK7fKQVcFFOMzzkMhWvbkrmM2pkcd5_erGzhtuiCEjNP3-rfELjgeuz_BWq8TGP_oWtJ3wjM-GW-YCsOso8kfy_EgRFugDlt-RCx26PGY7nvfGlRRMZp8KxpZpB0azGJ8Ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mx5XjskH6ZhMGom5x53tjPobdijSo1Sg7-rQiANLJ6v3Q-B_Gj2UckdBf6OccwAsGneUVGzdlL3dA842HIZBswR56mdhdTmN8EiJbjpOXiMOrCRnw7Dfu3x60yVY9SdmnPqdF0zOK-CWEvH5TaAIvz229JV-0Ndi8jzy_YAK0NLvjg6Cc-BhPKhI-Xc9WKQseQFb3Xup8W1mGjgFh4iPJ0znyLxpiz34IngQHy-qordaRT9mYbq5pN_yOMB5SuKqxcfx1ffW5byCI8ou2oM8SNKQ3TV1ZzsPvta946xCvGlmQa3EgywbJ0X58aVFAz7tUFXAsONhcJBztiOyUGZKKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/6471" target="_blank">📅 23:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBxeYuGrQTjqw79-yWeK6Ovb94RdZTJHomK7fR6W7tKvS69YxpYfqJiYtKrZRCdzUBKbXZowquifFEVs9-jHnVX_LoBGZMv2aSg7_xOh4lLEx9_UXJgVI-jgfhbGOYtq80rkf2x9Xm6ZsE19T0suVaoDBu_-9PL_H94-zSYWJdcOLwVlBvpoLfo3_HPbVFIpa-OzRLuVeEBJyQz5vso3ufn2J_tgOx1RNAtJJalEwztVTBhNh46CjepTMB5g80Y9kpQZz8p7WeBdyEw9vEvXKkYkCW43r7ny5WfnWjyOD3baOYMgpsq8zihK2IDZCHdbXv4Qe15kvuZH5N0aIYeEhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6469" target="_blank">📅 19:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AXfq0qfSosASksS56ohbDQ9XCMFdzfcN49hu-lL7dYNtc9jEbqpOc9pLAU15yiN7BqhVNmRTXqEZjvCjIrHy9Fc4uY1Q9vdCfHzzDQ52cc0ettm6GHcAAr4SMYl_Jz8ysVV5F0dBgGb7bOeOXrM8cAlC7bdDTguMjJyNpl8uNzb_jcw0COd4TErlas5kwZKtKuUWfy3itOvNsucM9vHAYBLm6XYYRKZGjPtKiScRI9DAH5oY9WidVwxLR9QxrczjBF2WMSvNjOFwl_FhuhPQu0AnKFUcfBUUp-tdyg7L_DGkjKfe6aje_acfhD1PrHTepimQ_EZ2b31GPED8erA-EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgZ2lo5WnvjXgswnLRZaJMDsLktDHzZFdOuHMrQfSsj-1GrgUEU56oUDRpDnd_8XfC-uXWKkjnnJHiINQNrvh5YsRMUjguEFJGNO8U9TvLWTvWTIoz1GILiky9eO6HUUvTt8GaNFetKQ7kOaUzqnZCEIB5l2OmhUpgFLuT3cslt6Un_pRmotAw99_HfVh5CmKSztB89F9C9BkICTBVDFIesq5o7UU2XV9COq2aVT3k2FbcjG1IZLWee_iR9gr1vFX5kNIOxSDG8tb-QViSMnckHNmnO_3coeEa9gXhCxT7PunghzER_oYL5zUW67AXli6XchwffmItCwklm8ZEWk2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvMwJXKdH7roLiPcNpwVrHeYR_nVUgvuPPtzPxovf2m1vYH6jn28-jAKWuuRxJSft7vkb8KJFmbNeoa-TREhf9W5fNPHj3nEq9-FQddmOvsxFWQnR2aRdeRpelAW37fFk1GRQmFexaDrvE_N7pRiHSNoYA8ODy-i0Vf0G4e4sYK-RwRzvGSeWsxpYTKpJ-d8ufBLh9toh9QjMCs7mz8ckgCrn6i-RZmDNRNdhoC0hMLo9cc9krObJDyg1jsomijRtDLVrzQ0J4y3f64xbI9xXRWYF2rpEX9_HH3LTLnUi-ixzWL49ywbPCi_eJY70hnG_l_5QX5ZXeGjX7rzkEArqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qpdZWUeBYwe_dSZozOgNmdPU7wYZRt9DyZG9w5BKt8J7YvkXOwfCaWYdNqbJBC6NN3lK5slWnKkZ7bAIgdwAE9pMDEeMb0LupaTxPrM0cbYR8fCFrTs1SZMsCrFyZGDh3I8AVvmp3kmBymm9nnJ_g9jygX2vXPbREOtnzYnAG78-hXldis4rac0ce-ny_RfrQV20QgkEVNx8Jn5NxfbhEA92-FvKNIXk7Ha2eOXosq9GAQT6nSCpsOoF-fRATAhzPeBugda_6ZBwH8xwS9TNSM8NS8c8Eubh653TIZw3K3QZslFz2IPkmaBe_SW4NBsQWb9qTKINZaNF3uJ5i0sbkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AMELI2xf4OHSYW62TjB2r-56rhnhhqb-cP-JuPaR64VlkrsSCRJ6LdfG--j6cVEzS2RaW6jqsyU7jyVNu73luKtQkpo-3fHrwe9RzLTU3wsJYAnAbbXvcOXWmknoR89iTJwU_Ryn4tzhHxd3I0Uibqv8putHrsCuaLt06y-xfe42suYykSLQsDxpLUoLkZoVP9GRw74_-ahlXKycUneObojVuECUgvgH8LL_pnTZYvdtbHJyAF7SOyAwZ3mJDf5FBJpSfYpNvbAPRlFLuj_sEDo-a5IJgOQ3gkf5ab6kAR4TpkdnBTANvn4bG3E2DW8FBWf_ofYJqiewFaPUzbeEhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fbF0-ARVsp2nLHkMyvjiPOhDxJgIF_p-d2otU9wUIasbutIG4iJGr05d1nV5tJSlsrPsayd45ONqiE85nKHUGOOCED98iKAvPahBOANebVS4z1UCodo9lH_Myp_0QhvPJrlLTmBo9kvw5R7J1tBQsepgKhyzZdffe1aRn5KxTFfGGJhuAfI7DacTcQhvAUvd1S8-9i_JzfUaqTVRhWytnGl3O91luP-t4-Ay6dyvRXXCGSYqj6tZK-9JxllsaNucDmxlsh4rJ72w4VE7sATbmHTw3RI-vP7lAOW81zGAofrAOqSa3bW_mL7b6FySGiFfR1pSq-4Vt6j69nlazm4sAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CP80mbCBfwA57lQIcb9649CrZvZ7_NxGBbIqc23KNDDBWu3vsymJZgChOw0--kM1oYu24kWvvARmp_z3hhD49Qxhxi1qDtRLGGsbqRDp9YwaY3x1UPLFQlYbut2MbhZfWXR-wc-Bhfbcjwdf9ufDQ8bgZYtbIRlhQQqpc4iW6gyf8D4ung8vuu-GE07pvkwerbsIyBWgfRPfPxi24nD5KNSlrYXBQV129O6Be3H3Ie-YjVm24vzhUO7z7dBvv2P6vk5jH4mMSd3xYd9IgPFbq_8RlRspR9mFJIht8SLI2_xeOM2v0-dQWw-xMYue_yhEWzYKyRQ_kCn4gSdfAxGBow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fgdT9cW8tx9prLcVLZbsI44fHnez86ktHnsVZ35rq44p6Eee1I5ydUrvdEsTZky2CnLVQuplL6ux-7E6A_Ytf7HUIu1uCZFhgm8_db_nm4HlqjNf7s32xJuTRlYe-5nIUIjMAAYxO3doBkoSmfMS9dtCrHWQgFvWmDfJi0ZSp2ihcYUfYmJhhr7MKRYvHvjPti5EVEdet-mdC9f9wxoDZtDGFt2qGNHN1cWdOEwVEF2Z8kVB0WoA8n4NqEELnkmorG84dbcWXMLor2Gux9iWaZuzxcKaxHZSJnUiRrPWevKhuYMSho-Cs2pUsQY-Cxhe3FoZTPbvJYhVIaQTUr-NNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ded905356.mp4?token=lisED_oGhdQBDzuRT408por8NHeAYzD_NjAPggBGVVKDCzPOo6Lg7lzjyzDFwvwxkxRS2Q2RMiF796BWEce4jyOj844nsIGOunerqoxLFqnFW5oUIRU7mhgg3qmPyqfFBjZSZqfmorS0ST2j6_78B0_ORmWGjAoCym1C1fhP-n4TyujHInSdiRLy9F-hoeVvgg0A_QvUssDh7YGoOlVGnFUMkHbGLkaBLZ2a9JzJU51uRsFXzPF90COWMNISMSeBR70hJ2EhEoqMGgW46dTQKw9Cajemtr00MJMWQS5B9lXzsTluOWHsxsm2x0ZxLHu2-YibeqNVX_4AR3sIaXaYWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ded905356.mp4?token=lisED_oGhdQBDzuRT408por8NHeAYzD_NjAPggBGVVKDCzPOo6Lg7lzjyzDFwvwxkxRS2Q2RMiF796BWEce4jyOj844nsIGOunerqoxLFqnFW5oUIRU7mhgg3qmPyqfFBjZSZqfmorS0ST2j6_78B0_ORmWGjAoCym1C1fhP-n4TyujHInSdiRLy9F-hoeVvgg0A_QvUssDh7YGoOlVGnFUMkHbGLkaBLZ2a9JzJU51uRsFXzPF90COWMNISMSeBR70hJ2EhEoqMGgW46dTQKw9Cajemtr00MJMWQS5B9lXzsTluOWHsxsm2x0ZxLHu2-YibeqNVX_4AR3sIaXaYWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/6457" target="_blank">📅 12:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #1</div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
