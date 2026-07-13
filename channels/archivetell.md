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
<img src="https://cdn4.telesco.pe/file/C2YtiL4ktgCx7QuB98TahnZ2EZB5XdU1YMGJx0WaotuLmaof3GaLPdHevQX0FLm4S0jYq8p8x4qTTNNo13yhQKfmKqyt2pgokZm8iuyDiQs1VYTxR5U1BJM66ceOtAatuln7YHK190FLQ-V29FBi2E4x5S0lS2F75_Zjs7K4pFHouZ03cMiBwkFG8IFEmkuM0e1o8HYXQgOc5LTUN4UBkwlR4YamPyMS65dTGhUrI5dZ6S5_II5YlayD-GaubbGK69DrHEMzBr-5FJTF-fR6m72P6UmlvFLi_wnjSfb_UJgVoKEK2n4Ob-BhK6MXrP6joJgcC5aOMBgLYsqBPkhFMw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.8K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐https://www.youtube.com/@ArchiveTelll</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 15:05:09</div>
<hr>

<div class="tg-post" id="msg-6935">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏
🔥
ChatGPT Work
اوپن‌آی با معرفی قابلیت انقلابی Work، آینده هوش مصنوعی را تغییر داد. این سیستم دیگر فقط یک چت‌بات ساده نیست، بلکه یک دستیار هوشمند (Agent) است که کارهای پیچیده و چندمرحله‌ای شما را از صفر تا صد، به‌صورت خودکار انجام می‌دهد.
✨
ویژگی‌ها:
🧠
تکیه بر موتور GPT-5.6 و Codex:
ترکیبی بی‌نظیر برای اجرای کارهای سنگین تحلیلی، برنامه‌نویسی و چیدن خروجی‌ها.
📄
خروجی‌های زنده و واقعی:
ساخت مستقیم ابزارهای کاربردی مانند شیت‌های اکسل، اسلایدهای آماده ارائه، اسناد و حتی وب‌سایت‌های تعاملی.
⏰
اتوماسیون و زمان‌بندی:
هندل کردن خودکار وظایف تکراری در زمان‌های مشخص (مثل چک کردن روزانه قیمت‌ها یا خلاصه‌سازی پیام‌های تیم).
🖥
کنترل مستقیم دسکتاپ (Computer Use):
قابلیت تعامل با سیستم دقیقاً مثل یک انسان؛ کلیک کردن، تایپ و جابه‌جایی فایل‌ها برای انجام کارهای پیچیده.
🧪
نکته:
امنیت این سیستم کاملاً تحت کنترل شماست. دسترسی‌ها را خودتان تنظیم می‌کنید و برای اقدامات حساس، سیستم حتماً از شما تاییدیه (Approval) می‌گیرد.
🔗
وب‌سایت رسمی OpenAI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 339 · <a href="https://t.me/ArchiveTell/6935" target="_blank">📅 14:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6934">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Knrid5yF0W_MvEg21LAwqVHcLu8nlGOjXBfJkhVmTg_O5uNTfyeK7J54DCLpIKLof_cD2TKVmYpWGobb80iWeQ81NzFyBBC45zK7cH7-1t9qijSbWNZiYuHKWJwM0xJZpK47sKJlb4DE5dlY6TZDGazksidNh94hy-UG6M7Ltt5GRMyT78LwMW5fxgM03MTtNDYiX_sF2GlUpuzTd22HgUD3Yc1GELslBSqqsm00AgvxadFHex221j80c8vYOYNT7MT0cUgfWmm-YIwKbytaKlbMgzqwhgYkaTtC9z_BiFCFbUWafyZDHvpm-MLMs8_JDmCa8pUtOWEVqwRlVYDG-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🕵️
3D Investigation Board
یک برد کارآگاهیِ تعاملی و سه‌بعدی (مبتنی بر GPT-5.6 و Fable 5) که به شما اجازه می‌دهد اطلاعات و سرنخ‌ها را دقیقاً مثل فیلم‌های پلیسی روی یک بورد مجازی مدیریت و تحلیل کنید.
✨
ویژگی‌ها:
📸
امکان اضافه‌کردن انواع شواهد، اسناد، یادداشت‌ها و عکس‌ها روی برد
🧵
اتصال بصری سرنخ‌ها به یکدیگر با نخ‌های سه‌بعدی و فیزیک واقع‌گرایانه
🧠
کشف هوشمند ارتباطات پنهان بین داده‌ها به کمک تحلیلگر هوش مصنوعی
🧪
کاربردها:
این ابزار خلاقانه، نه‌تنها برای حل پرونده‌ها و معماها، بلکه برای داستان‌نویسی، ایده‌پردازی و برنامه‌ریزی پروژه‌های پیچیده فوق‌العاده کاربردی است.
🔗
مشاهده ویدیو و آموزش کامل در X
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 580 · <a href="https://t.me/ArchiveTell/6934" target="_blank">📅 13:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6933">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLiDGRJ52EGpvglqRlLYrFiUa3MYX0MLQEEe_pQRuAcPVRoUABfRr1CyAhvJUcxiq4KF7oUo-HBIlGDAPq-XJ2t1QqN8Fhv0WdpWEPMlcxiIoD0u8q9eXywmXbAC6uyb_clqa7avDJWdQvTDoGkFVnK371q_EG9rQ1Kzz59Q8AT8XAPdRWZFwdpDnEustYBYh-00f-710PB5kyT3ErBL7Yloyz2gCcaPg4aGWiUY6T0WJZ5qdjKaq9KoaePDcXLnTlNuB9ysnjkZ8kJ5zUEEntuk1gbV-PRJJtfiWuGAbbcjc2zlBwRdWujx8iQ46W302KLU7E4GXlJYKQ_pFaVP1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤖
OMG-Agent
کلاینت دسکتاپ متن‌بازی که به هوش مصنوعی اجازه می‌دهد گوشی اندرویدی شما را فقط با دستور متنی کنترل کند! (مثلاً: «تلگرام را باز کن و به
⚡
Bachelor پیام بده»).
✨
ویژگی‌ها:
🧠
پشتیبانی از مدل‌های هوش مصنوعی موبایل (مثل AutoGLM) و APIهای OpenAI
📱
اجرای خودکار دستورات با تحلیل لحظه‌ای صفحه گوشی (از طریق ADB)
💻
سازگار با گوشی‌های فیزیکی اندروید و شبیه‌سازها (Emulators)
🧪
نکته:
پیش‌نیاز این ابزار، نصب ADB، کیبورد ADB و فعال‌سازی USB Debugging روی گوشی است.
📥
دانلود و راه‌اندازی از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 601 · <a href="https://t.me/ArchiveTell/6933" target="_blank">📅 13:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6932">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏
🚀
۴۰۰۰ دلار کردیت رایگان API
هدیه‌ای ویژه برای برنامه‌نویس‌ها! دسترسی سریع به قدرتمندترین مدل‌های هوش مصنوعی دنیا برای پیشبرد پروژه‌های کدنویسی شما.
✨
ویژگی‌ها:
🧠
پشتیبانی از مدل‌های برتر جهان (GLM 5.2 ،Qwen 3.7 ،Deepseek 4 Pro ،Minimax M3 و Kimi k2.6)
📧
ثبت‌نام سریع و کاملاً بی‌دردسر با هر نوع ایمیل
💻
سازگاری کامل با انواع کلاینت‌ها
🧪
نکته:
مصرف کردیت در این سرویس‌ها با ضرایب بالایی محاسبه می‌شود؛ پس حتماً در استفاده از توکن‌هایتان دقت و مدیریت لازم را داشته باشید.
🔗
لینک ثبت‌نام
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 666 · <a href="https://t.me/ArchiveTell/6932" target="_blank">📅 13:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6931">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaEmlQrttGLi_GKfC5pFeI9V0TKZbbCfi1u6JpnXPGqyW4ONf6N1xMReGid_WZz8kSagAUaFJuDuUC7eQAczKb-xIqf_u9r1gvFihp11H3-DdgMmFWn_8BojONbJO1AZZ6_62mAIoYJMsuh4dDN4KNYAtoPKDCZzla66yCyDh6kYhRWIoMIffzSYzmTigCIO_7dWiQvxy4QMh4q0Yu-1EWumwdJZmBGanox2qiLtqWetRi0G0sI8sf012BobUAqasDmXccXSBkdCl1okowN1wljVzfLGf9WmURJwnXSzUDIWpmGMe4dR-lxmOtULJDVl1fKlrG_I5plg1JY2wK1HFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⭕️
Colibri
پروژه قدرتمند و متن‌بازی که با C خالص نوشته شده و اجازه می‌دهد مدل‌های عظیم هوش مصنوعی را تنها با اختصاص ۳٪ از حجم کل مدل به رم (RAM) اجرا کنید!
✨
ویژگی‌ها:
🔸
اجرای کامل تنها با یک فایل C (حاوی ۲۴۰۰ خط کد)
🔸
کاملاً مستقل از پایتون، کتابخانه‌های جانبی و کارت گرافیک (GPU)
🔸
ساخت API لوکال سازگار با OpenAI (تنها با دستور coli serve)
🔸
اجرای مدل سنگین 744B (که در حالت عادی ۷۳۰ گیگابایت رم می‌خواهد) تنها با ۲۵ گیگابایت رم!
🧪
نکته:
برای کاربران ویندوز، استفاده از WSL2 پیشنهاد می‌شود. به عنوان مثال، لود یک مدل ۳۷۰ گیگابایتی تنها ۳۰ ثانیه زمان و ۹.۹ گیگابایت رم نیاز دارد (البته به دلیل عدم استفاده از گرافیک، سرعت پردازش حدود ۱ توکن بر ثانیه خواهد بود).
📥
دانلود از گیت‌هاب
⭐️
حمایت از پروژه: ستاره (Star) در گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 797 · <a href="https://t.me/ArchiveTell/6931" target="_blank">📅 12:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6930">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">📈
؛
Vibe-Trading
دستیار هوش مصنوعی شخصی و متن‌باز برای ترید و تحلیل بازار. کافیست ایده‌هایتان را به زبان ساده بنویسید تا خودش برایتان استراتژی معاملاتی بنویسد و بک‌تست بگیرد!
✨
ویژگی‌ها:
🧠
تبدیل مستقیم پرامپت‌های متنی به کد استراتژی، تحلیل بازار و دریافت بک‌تست‌های دقیق
🐝
تشکیل تیم‌های مجازی هوش مصنوعی (ایجنت‌های ریسک، کریپتو و کوانت) برای مشورت و بررسی همه‌جانبه ایده‌های شما
👥
سیستم جالب Shadow Account: ژورنال معاملاتتان را آپلود کنید تا هوش مصنوعی خطاهای احساسی و رفتاری شما را در ترید پیدا کند
📊
پشتیبانی یکپارچه از بازارهای جهانی (کریپتو، سهام و فارکس) با دریافت خودکار دیتا
🧪
نکته:
این ابزار با پایتون توسعه داده شده و به‌راحتی به API مدل‌های مختلف (از جمله Groq ،DeepSeek و OpenAI) متصل می‌شود. برای دیپلوی روی سرور شخصی یا اجرای لوکال فوق‌العاده است.
📥
دانلود و نصب از گیت‌هاب (PyPI / Docker)
⭐️
حمایت از پروژه: ستاره (Star) در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 791 · <a href="https://t.me/ArchiveTell/6930" target="_blank">📅 12:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6929">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏
🐋
Orca
محیط توسعه و هماهنگ‌کننده (Orchestrator) فوق‌العاده قدرتمند برای مدیریت همزمان چندین ایجنت هوش مصنوعی برنامه‌نویس. یک دستیار همه‌چیزتمام برای توسعه‌دهندگان!
✨
ویژگی‌ها:
🤖
اجرای همزمان ایجنت‌های مختلف (مثل Claude، Codex و Grok) روی یک پرامپت و مقایسه خروجی‌ها
📱
دارای اپلیکیشن موبایل (iOS و اندروید) برای کنترل و هدایت ایجنت‌ها از راه دور
🎨
مرورگر توکار (Design Mode) برای انتخاب المان‌های سایت و ارسال مستقیم HTML/CSS آن به هوش مصنوعی
🔗
اتصال بی‌نقص به گیت‌هاب، پشتیبانی از محیط‌های ریموت (SSH) و ترمینال‌های قدرتمند داخلی
🧪
نکته:
این نرم‌افزار متن‌باز است و تقریباً از هر ایجنت مبتنی بر CLI (مثل Cursor ،Copilot و OpenCode) پشتیبانی می‌کند. کلاینت دسکتاپ آن برای ویندوز، مک و لینوکس کاملاً رایگان در دسترس است.
📥
دانلود از گیت‌هاب (بخش Releases) یا سایت رسمی (onOrca.dev)
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 849 · <a href="https://t.me/ArchiveTell/6929" target="_blank">📅 11:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6928">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAX-8pR1-SwwEz0ko59jm_SWiK1Zj8besZwXlK4OHYJ5INT4KCQ_dzQClOcM_13KOEVrFGF-RW7aB5NnvXYky1safliqtO5PPHhb4OFdLyZxra-lA9sIUA6yhRsaycx7L1EA4RhiF_NJCE0sbm4N9ioudy0ZdKTNmMSTyAxVPUxBulSiWaSDUb7VXn-6h0YZLb34kIgz6g6uHYbtDBC_FDlVwUIBB5-gYXnvSiv8B1hOSwAth1DiIZKaMNT0eNoIOCNxCFnyHZZG_4yZan_pT934X1NCINlimtoHFPyR3tc9pEgE11Tihnpf7YT4mt_u4TKU9RaOO2yL429ss3_evA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
هر عکسی رو به پرامپت تبدیل کن!
؛Convly AI Image-to-Prompt تصویرت رو تحلیل می‌کنه و در چند ثانیه یک پرامپت کامل و قابل ویرایش تحویلت میده.
✨
مناسب برای:
• پیدا کردن پرامپت یک AI Art
• بازسازی استایل عکس‌ها
• استفاده در Midjourney، Stable Diffusion و سایر مدل‌های تولید تصویر
✅
بدون ثبت‌نام
✅
بدون واترمارک
🪙
رایگان
https://convly.ai/image-to-prompt/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 815 · <a href="https://t.me/ArchiveTell/6928" target="_blank">📅 11:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6927">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhV827-QG4XnYfv_sCAt565Jb5vZDqdaF8GBYYNu-xrsmomYI02VGV0QJlR4uBoQFJQoYEiyjB44EJhmgUxx6sjvl0JQeHeX4ByURHp3Vx__AkUZI9k2NsijwS7yFwIWuGz_6n0jQQphTZj_mjCJx0zvxUd1mhymgmF7eVWxHv4aIegz9vIw_noOwqZhjAjbmYpLDz0rb4-jSQNt5oe_uvm2OTceq3GZyYJU6T_57j-WybzyPUwidDeVZyW3ng_pkhaaBDIHqZPs5pgb_nncUV7GEIUJ78jMotpWJC8fh2mlWcIsdR0A4KF2FM5J-bZy7rtP_ZxJYeq6sZyzJgLqgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
بازی خودت را با هوش مصنوعی، در چند دقیقه بساز!
فقط ایده‌ات را بنویس؛ هوش مصنوعی بقیه کارها را انجام می‌دهد.
✨
بدون کدنویسی
🌐
اجرا مستقیم در مرورگر
🎯
آماده برای بازی و اشتراک‌گذاری با دوستان
https://codewisp.ai/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 881 · <a href="https://t.me/ArchiveTell/6927" target="_blank">📅 09:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6925">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyiwtXU10IF1KtkwIo5xZyNAD19YUiBXx6P11el2ppA2vJzMxhBrRkBJwsOUeo4GbPqS3NMxHw7RpZG3E7m8ww_D3I_gE5yXCLMXXD5-4XZOy-b0no41UHFeYJrKKRUZc48EMkwu2EgjSz2XAI5M3DK1Gq94nG_6OQY4d3RtyzToIGYRd86BG5o_K0cSw79gp4a1sI5dOKY-ieasqnVOtz_eKNnXG065v94uyDJtAq3ARYdjOJb_-BPEUnWW9rrLLNBeqMJzozLqR1GKPyIpAsGrj7Zff6ZzxFkTOdWTqL2oNvR8FUFW-S4YfAbSdr-AXyRj3hPJaxB1gUGiVxgliQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧩
؛
Hermes Browser Extension
افزونه‌ای حرفه‌ای برای مرورگرهای مبتنی بر کرومیوم که وب‌گردی شما را با رعایت سخت‌گیرانه حریم خصوصی، مستقیماً به محیط هوش مصنوعی Hermes Agent متصل می‌کند.
✨
ویژگی‌ها:
🧠
اتصال یکپارچه به هسته Hermes (محیط لوکال، کلاد یا ریموت)
📄
استخراج هوشمند و ایمن متن صفحات و تب‌های باز برای هوش مصنوعی
🎙
پشتیبانی از دستورات صوتی و رندر حرفه‌ای Markdown
🛡
امنیت حداکثری بدون نیاز به دسترسیِ تاریخچه و کوکی‌ها
🧪
نکته:
افزونه در فاز آلفا است؛ برای استفاده باید فایل‌های نسخه ریلیز را دانلود و به‌صورت دستی (Unpacked) در مرورگر لود کنید. پیش‌نیاز اصلی، نصب بودن خود Hermes Agent است.
📥
دانلود از گیت‌هاب (بخش Releases)
⭐️
حمایت از پروژه: ستاره (Star) در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 935 · <a href="https://t.me/ArchiveTell/6925" target="_blank">📅 08:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6924">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🌐
؛
Omni Browser
مرورگر اندرویدی امن و فوق‌حرفه‌ای (مبتنی بر موتور فایرفاکس) با تمرکز شدید بر حریم خصوصی.
✨
ویژگی‌ها:
🛡
مسدودساز تبلیغات (uBlock) و گاوصندوق بیومتریک فایل‌ها
🧩
پشتیبانی مستقیم از نصب افزونه‌های فایرفاکس
🎬
شکارچی خودکار لینک‌های ویدیو + پلیر اختصاصی
🛠
مترجم ۱۰۰٪ آفلاین و ابزارهای حرفه‌ای دولوپرها (کنسول زنده JS)
🧪
نکته:
برنامه در فاز آزمایشی است؛ فعلاً به عنوان مرورگر اصلی استفاده نکنید و از اطلاعات مهم بکاپ بگیرید.
📥
دانلود از گیت‌هاب (بخش Releases)
⭐️
حمایت از پروژه: ستاره (Star) در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 923 · <a href="https://t.me/ArchiveTell/6924" target="_blank">📅 08:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6923">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2XxSoAbmIX6UbGEL1-oBHwnB1bMigpUEse3XfOPVAbNnSI4Yyf3Btl6-dNWAPMWCo-ghoq0lcgniyyFTOwFvZofwE6GUzaICs_k6oRwhhC0RXU9Piyw_SgmbpCqXGavMauZRN5fNmmOTwGZRpXygkK0N25kEag_pve3eWt2C40GaZMDmZCiC2EQZqxgVsITmG-jg3Cme408hy-XZG6NB62A2fqt5hZutX5fLh49jOQbyPzPKJ1l0bPUrkFDevc9nyCFkcCjOed9ypUocIpuVG-0XuhC1pLYPzkFBjmRtAwBatQFB2Qh1ubpAf0GuQzU6InMUEI90JFfSkah-NKmXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 927 · <a href="https://t.me/ArchiveTell/6923" target="_blank">📅 08:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6922">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">Telegram-X-0.28.10.1791-armeabi-v7a.apk</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/6922" target="_blank">📅 01:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6920">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTelegram X APKs & Build Info</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Telegram-X-0.28.10.1791-arm64-v8a.apk</div>
  <div class="tg-doc-extra">58.4 MB</div>
</div>
<a href="https://t.me/ArchiveTell/6920" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Version
:
0.28.10.1791-arm64-v8a
Changes from 1785
:
4ac597ca...5c907d8b
#arm64
#beta
#apk
(
MD5
,
SHA-1
,
SHA-256
)</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/6920" target="_blank">📅 01:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6919">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚀
آپدیت بزرگ بات منتشر شد: هوشمندتر و سریع‌تر
تغییرات کلیدی برای مدیریت یکپارچه کانفیگ‌ها و عبور از محدودیت‌های دسترسی:
✨
ویژگی‌های جدید:
•
📱
مینی‌اپ اختصاصی:
دسترسی سریع و رابط کاربری مدرن برای مدیریت آسان‌تر.
•
🔗
بخش ترکیب (Merger):
ادغام تمامی کانفیگ‌های Render و Railway در یک ساب‌اسکریپشن واحد (نیازمند توکن Cloudflare).
•
📡
بخش رله (Relay):
اتصال دامنه Render به Cloudflare Workers جهت رفع فیلترینگ بدون نیاز به خرید دامنه پولی.
🛡
نکته فنی (مصرف Cloudflare):
این روش بهینه‌ترین حالت ممکن است؛ با سقف ۱۰۰ هزار درخواست رایگان روزانه، نگران محدودیت نباشید. مصرف فقط در زمان اتصال/قطع صورت می‌گیرد.
⚠️
توجه:
به دلیل ترافیک بالای انتشار، ممکن است در ساعات اولیه با کندی جزئی مواجه شوید که به مرور برطرف خواهد شد.
🤖
شروع استفاده:
@REN_WZA_BOT
@REN_WZA2_BOT
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/6919" target="_blank">📅 00:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6918">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2WF4iE3MyfKahWhiOPSjOxSt8irIhmlBU-WI1LK_PSYbuy78TOhz0BpUE2-7-u74aj6BUD7Yl1-Y_Mqq3FEZCG_Rq2FaSVdjHOgdOLQ2mEzs2Wh1ujdQHJQjlslayFsdRa8gl0iyBDE8ABBffKp62HiNe9IxU9i1aLHHOb7XmvfLHCrIemhpeCq0VOeF9Q78D74sMmRGmJ8oKS6hjSw0BR0_eNzwPMMcdPqMBTKI447eX2ZmY7wSOzciNR90XSgwmmKUEeN3bfl19wJPDM4BliLuxuFep-PIn0dGeTr7g93mbzDrcSTtEnG_ZvAvT7IJZY4A-Fvy2IvZqJCztcJAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به Claude Fable 5 دوباره تمدید شد، شرکت Anthropic این مدل را تا 19 جولای در اشتراک معمولی در دسترس قرار می‌دهد.
محدودیت‌ها همانند قبل هستند: 50 درصد از میزان استفاده هفتگی. پس از یک هفته، Fable 5 به سیستم پرداخت بر اساس توکن از طریق API منتقل خواهد شد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6918" target="_blank">📅 22:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6916">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HP64PNGb3HVcB4KyPRUyCw_Dc139_tgaA7UrWjEFE2fC2UwBsNY-laDiFtPDyLkg4ceNxLgD9tG2SpjJTB33IC3A3d-fZVyA9kmNEPBlqg7BGpu3UrpdnZkoFq1O0fwpu7kSh9j-dB4kL1nQmC2Tr6Dj8HmcW3aPcg9PO-jQEhr_vl1gTr34ZUXN2q18XNSoVyDImjH9oIfwOoDE6j1o3ANayY8APTBiKVAA-tSNcxq3D-KlVsgshtHq1TCqOBZr1xf_YejJRgEjgl3EP1yo5G6E789t51se6Ku_jKFbzZAnVk_-BMme9QVu426WCKY-vIAB6OroT6y6j_kNliuoKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/THxxc_nAC4osl8tq_yKag08PRBfoE7dp35QOZHItQFydiQahmhpcapQSEje0DE6-BQxUqyjtqLPMBYtlzjziOKssHqVZeCa1kouUwoD2rssQa0TdhlqKeamYci7oNE8UvGdw0y_z9wYvX5l2boVI15kRWnTLnLjIeuU_h4Y05tzlG3a1MRWiEM25fG4KxugZe-J-h9CLvIsozuKwQXShMJxerLwK4kaIn72B2DQ0KUCweGG4oHfdgSX4VCEZm_GKppJjOUKenKyeQme9SiDyF6y76zFnn9j2jzNkTIVWWN19TFddGJNutiTLRY0gFCTpc0vsjbZTVbiTOVmrqqAQeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">؛PCLink راهکاری سریع و سبک برای دسترسی از راه دور به رایانه، بدون تنظیمات پیچیده
🖥
• دسترسی کامل به فایل‌ها، اپلیکیشن‌ها، کیبورد و ماوس
• خاموش، روشن و ری‌استارت کردن سیستم از طریق گوشی
• اتصال آنی با اسکن QR Code
• پشتیبانی از Windows و Linux
🔗
لینک مخزن گیت‌هاب پروژه
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/6916" target="_blank">📅 21:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6915">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اپلیکیشن اندروید NipoVPN توی گوگل‌پلی   https://play.google.com/store/apps/details?id=net.sudoer.nipo</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/6915" target="_blank">📅 20:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6914">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMorteza Bashsiz مرتضی باشسیز</strong></div>
<div class="tg-text">اپلیکیشن اندروید NipoVPN توی گوگل‌پلی
https://play.google.com/store/apps/details?id=net.sudoer.nipo</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/ArchiveTell/6914" target="_blank">📅 20:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6913">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@ArchiveTell.json</div>
  <div class="tg-doc-extra">2.4 KB</div>
</div>
<a href="https://t.me/ArchiveTell/6913" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ warp
فقط سامانتل
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/6913" target="_blank">📅 19:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6912">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پروکسی تلگرام
🔥
https://proxybolt.link/
| سایت
@mtpro_xyz_bot
| ربات
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/6912" target="_blank">📅 19:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6911">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⏱
؛
tg-username-clock
یک اسکریپت ساده و جذاب برای شخصی‌سازی پروفایل تلگرام که نام خانوادگی (Last Name) حساب کاربری شما را به‌صورت خودکار و هر یک دقیقه، با زمانِ دقیقِ فعلی به‌روزرسانی می‌کند.
✨
امکانات:
*
⏱
نمایش زنده زمان: تبدیل نام کاربری شما به یک ساعتِ زنده برای مخاطبان.
*
⚙️
به‌روزرسانی خودکار: اجرای اسکریپت در پس‌زمینه و آپدیتِ اتوماتیکِ هر دقیقه‌ای.
*
🚀
سبک و کاربردی: پیاده‌سازی سریع بدون درگیری‌های پیچیده نرم‌افزاری.
📥
دریافت اسکریپت و دسترسی به منبع پروژه.
⚠️
احتیاط یادتون نره!
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/6911" target="_blank">📅 18:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6910">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔐
؛
OfflinePW
یک پسورد منیجر اندرویدیِ فوق‌امن، سبک و کاملاً آفلاین است که از یک دولوپر ایرانی (Cyru55
❤️
) که با الگوریتم‌های نظامی و معماری «دانش صفر» توسعه یافته است.
✨
امکانات:
🚫
آفلاینِ مطلق:
بدون نیاز به هیچ‌گونه دسترسی (Permission) در سیستم‌عامل.
🪚
امنیت TwoFish-256:
قدرتمندتر و ایمن‌تر از استانداردهای رایج AES.
⛏️
ضد Brute-force:
خنثی‌سازی حملات با استفاده از PBKDF2.
📸
حریم خصوصی:
مسدودسازی خودکار اسکرین‌شات و ضبط از صفحه.
⚡️
حجم مینی‌مال:
تنها ۴ مگابایت با رابط کاربری ساده و پوشه‌بندی شده.
🔪
پشتیبانی وسیع:
سازگاری کامل از اندروید ۴.۰ تا نسخه‌های جدید.
🔒
مدل Trust No One (به هیچ‌کس اعتماد نکن)
هیچ‌کدام از پسوردها یا کلیدهای رمزنگاری شما در سیستم ذخیره نمی‌شوند. تنها کلیدِ دسترسی به داده‌ها، رمزی است که منحصراً در ذهن شما قرار دارد.
📥
دانلود فایل نصب (APK) از بخش Releases گیت‌هاب.
⭐️
در صورت رضایت، با Star دادن از پروژه حمایت کنید.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/6910" target="_blank">📅 17:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6909">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OE4_72JhwcZJxQhPUhwySgeXUh2URpTesiwVPmSImpKMx_uWWyiDJ6Pk15nQ6IVEH7rSP11Rn2XBWol2awvViitJl_qMWfvBRCLHqk08qoeOCG2Vz5WXVzbHiKTGObb6a0QC0xl2f8cDHnM73FOkFRyJP7oOxhvpJNpBTPq0U9pTtvGo6hSn5wVPkO9didL3XPyIQsRo4G4NruT9rRjomltK7j8jNRoC_3kAev4TnzHZRxCz8AwdVji3kDEVrjAzOmbFar-IXFhX0XOFc3oRm1aEH0BkqMYJKtrk5iuSwq0rH0kQUcRXKF_CvsgClV684uYmjEfckT7_NHssbkZ-nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌍
؛
OSINT Intelligence Dashboard
داشبورد متن‌باز و کاملاً رایگان برای رصد بلادرنگ رویدادهای امنیتی جهان؛ یک تحلیل‌گر شخصی و جایگزینی قدرتمند برای پلتفرم‌های گران‌قیمتی مثل بلومبرگ ترمینال.
✨
امکانات:
*
📡
رصد جامع:
مانیتورینگ ۲۷ فید اطلاعاتی (پروازهای نظامی، تشعشعات و درگیری‌ها) روی کره سه‌بعدی.
*
🤖
تحلیل هوشمند:
اتصال به مدل‌هایی مثل GPT و Claude برای دریافت لحظه‌ای گزارش‌های امنیتی.
*
📱
مدیریت آسان:
کنترل کامل و دریافت هشدارهای چندسطحی (FLASH تا ROUTINE) از طریق بات تلگرام و دیسکورد.
🔒
اجرای ۱۰۰٪ لوکال
این سیستم کاملاً آفلاین و فاقد هرگونه تله‌متری (Telemetry) است و تمام پردازش‌ها منحصراً روی سیستم شما انجام می‌شود.
📥
دریافت سورس‌کد (با بیش از ۱۰ هزار Star) از گیت‌هاب.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/6909" target="_blank">📅 16:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6907">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🗑
حذف کامل برنامه‌ها و فایل‌های اضافی مک با Uninstally
وقتی برنامه‌ای رو در macOS به سطل زباله منتقل می‌کنید، کلی فایل کش، لاگ و تنظیمات پنهان روی سیستم باقی می‌مونه. این ابزار بومی (Native) و اوپن‌سورس تمام این ردپاها رو برای همیشه پاک می‌کنه.
🔥
ویژگی‌های مهم:
🖱
ادغام با Finder:
امکان حذف سریع برنامه‌ها فقط با یک کلیک‌راست (بدون نیاز به باز کردن خود ابزار).
📦
پشتیبانی از Homebrew:
شناسایی، مدیریت و حذف پکیج‌ها (Casks و Formulae).
🧹
اسکنر فایل‌های یتیم:
پیدا کردن و پاک کردن فایل‌های جا مانده از برنامه‌هایی که قبلاً به صورت دستی پاک کردید.
🔒
کاملاً آفلاین:
بدون جمع‌آوری دیتا (Analytics) و بدون نیاز به ساخت اکانت.
🔗
لینک مخزن گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/ArchiveTell/6907" target="_blank">📅 16:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6906">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🌍
سناریوی جدید AI 2040: Plan A
تیم پژوهشی گزارش معروف AI 2027، سناریوی آینده‌پژوهانه جدیدی را منتشر کرده که مسیر توسعه هوش مصنوعی را در صورت همکاری قدرت‌های جهانی (آمریکا و چین) بررسی می‌کند. بر اساس این سناریو، تا سال ۲۰۳۵ حدود ۸۵٪ کارهای اقتصادی به AI واگذار خواهد شد.
🔥
مهم‌ترین نکات این سناریو:
🤝
توقف رقابت AGI:
توافق آمریکا و چین بر سر کاهش سرعت توسعه، افزایش شفافیت و نظارت‌های سخت‌گیرانه بین‌المللی.
🛡
تمرکز روی ایمنی:
متوقف شدن توسعه مدل‌های پیشرفته، صرفاً تا زمان انجام ارزیابی‌های جامع امنیتی.
💰
درآمد پایه همگانی (UBI):
رشد اقتصادی بی‌سابقه از ۲۰۳۲ و پرداخت یارانه‌های سالانه به شهروندان جهت جبران بیکاری ناشی از اتوماسیون.
🚀
شتاب علمی چشمگیر:
رسیدن AI به سطح برترین متخصصان تا ۲۰۳۵ و افزایش ۱۰ تا ۱۰۰۰ برابری سرعت پیشرفت علمی از ۲۰۳۷.
⚠️
نکته:
این گزارش صرفاً یک سناریوی تحلیلی و آینده‌پژوهانه است و پیش‌بینی قطعی محسوب نمی‌شود.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/ArchiveTell/6906" target="_blank">📅 16:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6905">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بنازم
🔥
🔥
🎁
گیووی اکانت‌های مادام‌العمر Proton VPN!  اکانت رسمی پروتون اعلام کرده که اگر امروز تیم ملی سوئیس بازی رو ببره، اشتراک‌های بسیار نایاب و رایگان مادام‌العمر (Lifetime) هدیه میده!
🔥
جزئیات:  *
🇨🇭
شرط قرعه‌کشی: پیروزی سوئیس در مسابقه امروز مقابل آرژانتین.…</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/ArchiveTell/6905" target="_blank">📅 16:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6904">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بنازم
🔥
🔥
🎁
گیووی اکانت‌های مادام‌العمر Proton VPN!
اکانت رسمی پروتون اعلام کرده که اگر امروز تیم ملی سوئیس بازی رو ببره، اشتراک‌های بسیار نایاب و رایگان مادام‌العمر (Lifetime) هدیه میده!
🔥
جزئیات:
*
🇨🇭
شرط قرعه‌کشی: پیروزی سوئیس در مسابقه امروز مقابل آرژانتین.
*
💎
جایزه: پلن Lifetime پروتون (اشتراکی که در حالت عادی اصلاً فروخته نمیشه و ارزش بسیار بالایی داره).
🔗
[لینک توییت رسمی پروتون]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/6904" target="_blank">📅 16:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6903">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4wqeEfYXf73AjWmrt58ywWtJeOE7DMC9LZmwo1TYbwfTZL7pKIce5RhFyPRK-0R0jAPGqUVgpmoZehiA1a3rUA3OaX8GjLVYjrg8jakxUE6kiK1i2-O6HmGOZDSeISN94hg8wILJy0i9JtUqoaKMTijPDYLtwwxiIMSbxa9h1a79apArON-vXwQu-5j5K72NTDaow6NMErZKyDFDOYnlWfBzxU8iTWPjJQu7Q62yufyKgJ5oyjDWHKchYfmvJ-RalC1N4j1xA--gad9JrcVboFcQTKtRt8cXXTg0qFhxt9AHu7hDMQ46Vojtjsu8VFPm5B1BnxJ7yAvgmvac_FfXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
AIText Detection for X
⁩تشخیص متن تولید شده توسط هوش مصنوعی!
🔍
✨
‏‌این افزونه با هدف شناسایی و تحلیل محتوای تولید شده توسط هوش مصنوعی در توییتر طراحی شده که با یکپارچه‌سازی آسان با فید توییتر، امکان تحلیل توییت‌هایی که کاربران میخونن رو فراهم میکنه.
https://www.tweetdetective.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/ArchiveTell/6903" target="_blank">📅 15:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6902">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVjban9Z3GjLM3DxyJJtB_ajsFHZ67jCIQYjWfDjciPK6ahH7TC4fgb_Bj0jTI8I-RIt2WdLH-wH-6TH0xEtyPnOzSbR2shgvHHGmi0KBGsbLp5kBYpD4u_wv0Y2uc4iyk_Nc_cnut8jQMuOKMha38wN80SUArZNV5sa2Olpu3YWnsE6f_M9MDyIeedWYr4lN1c9iA0NNb7JL-o6OWGZrB-mRBKpM5nvw9glmSw_CsGcoZZlIcT9pLl761Cfu6oGPX6ml0EdOo3k1Zy906l3lVGv4Wg3nWLwRfNgSgAndzut1YnfaLeRBbPpYEth29BRFyttq3vJalWBE_dcRCfeKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
معرفی ‌Gitea⁩؛ جایگزینِ سبک و قدرتمندِ ‌GitHub⁩ برای میزبانیِ شخصی!
🛠
‏با ‌Gitea⁩ می‌توانید در عرض چند دقیقه، سرویسِ گیتِ اختصاصی خودتان را راه‌اندازی کنید. این پلتفرم با وجودِ سادگی، بسیار منعطف است و اجازه می‌دهد به راحتی پروژه‌هایتان را از ‌GitHub⁩ یا ‌Bitbucket⁩ به محیطِ امنِ خودتان منتقل کنید.
‏
✨
ویژگی‌ها:
‏‌
🔹
فوق‌العاده سبک: یک باینریِ واحد که حتی روی سخت‌افزارهای محدود هم کار می‌کند.
‏‌
🔹
سازگاری کامل: پشتیبانی از ‌GitHub Actions⁩ برای اتوماسیونِ حرفه‌ای.
‏‌
🔹
نصبِ سریع: راه‌اندازیِ بی‌دردسر از طریق ‌Docker⁩ و پشتیبانی از دیتابیس‌های مختلف.
🔹
همه‌کاره: شاملِ مدیریتِ تسک‌ها، ویکی، رجیستریِ پکیج و ابزارهای ‌CI/CD⁩.
لینک گیت هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/ArchiveTell/6902" target="_blank">📅 14:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6901">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F10_02CaW6iTN0GsaYl2ihgDUx5E2w9akAlTb4yBfWZ45_B1owbQ-uK-LWYDaR-zZzC4l_G70RbVUNh7wWLDyh3gEDoLJDuH74bcjb-0jb8Ow8fhHe7ZHrPW5tATCusdeox5fy3fOB-H23pBfazx_UDSWG0VVCeihBO3NmJT-F3FAF37X5BP_sMwJlzFwX_p7CN7jF5OpohM7o89n_c6tPhv9AW_lFgZhQeUkLakFd0ILjqAuzZW8D27DQVmrlBvRXD1GeVs8DvThFed2O5IYGBcT0ICqYYCng-tPCE6HVXlBIzraX-LJddrbH9SgbQoMjM3N-vWme3qp4ChPmvEvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📁
فایل منیجر قدرتمند Fast File Explorer؛ جایگزین قاتل برای Windows Explorer!
اگر از کندی سرچ فایل‌ها در ویندوز خسته شده‌اید، این ابزار سریع‌ترین روش برای پیدا کردن فایل‌هاست.
🔥
ویژگی‌های مهم:
🔍
سرعت استثنایی:
سرچ فوق‌سریع که فایل‌ها را در چند ثانیه پیدا می‌کند (بسیار سریع‌تر از جستجوی پیش‌فرض ویندوز).
🌐
امکانات شبکه و امنیت:
اتصال مستقیم به سرورهای ریموت و بررسی سلامت داده‌ها با هش‌های MD5 و SHA.
👁
پیش‌نمایش در لحظه:
نمایش محتوای فایل‌ها و داکیومنت‌ها مستقیماً داخل رابط کاربری برنامه، بدون نیاز به باز کردن آن‌ها.
🖥
چندپلتفرمی:
کاملاً رایگان و قابل اجرا روی ویندوز، لینوکس و مک.
🔗
[
لینک دانلود
]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/ArchiveTell/6901" target="_blank">📅 13:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6900">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یه توضیحی که مدت‌ها تو دلم مونده بود
راستش قصد نداشتم وارد حاشیه بشم، ولی بعضی چیزها وقتی گفته نشن، فقط آدم رو اذیت می‌کنن. حس کردم بهتره تجربه‌ی خودم رو بگم تا بقیه هم در جریان باشن.
ادمین
نتلیفای
و
زئوس
در واقع دوست ما بود...
زمانی که هنوز کانالی نداشت، عضو کانال ما بود. ادمینش بود. از کارهاش حمایت کردیم، پروژه‌هاش رو معرفی کردیم، کانفیگ در اختیارش گذاشتیم و هر جا تونستیم کمکش کردیم. حتی وقتی کانال خودش رو راه انداخت، پست‌هاش رو تو همین کانال فوروارد می‌کرد و طبیعتاً بخشی از ممبرها هم به سمت کانالش رفتن. بابت زحمتی که برای پروژه‌هاش کشید همیشه براش احترام قائل بودم.
اما چیزی که ناراحتم کرد، این بود که این حمایت هیچ‌وقت دوطرفه نبود.
- برای راحت‌تر شدن کار کاربران، با کمک یک دولوپر اپلیکیشن نتلیفای رو ساختیم، اما حتی حاضر نشد نصبش کنه و از همون اول گفت «اپ به چه درد می‌خوره؟» در حالی که هدف فقط ساده‌تر شدن استفاده برای کاربرها بود.
- بعداً یکی از دوستان، یک فورک تمیز و کامل از کانفیگ‌جنریتورش منتشر کرد. درخواست شد داخل کانالش معرفی کنه، اما قبول نکرد. در نهایت خودم اون پروژه رو توی کانال معرفی کردم.
- خودم هم چند بار پروژه‌ش رو فورک کردم و قابلیت‌هایی بهش اضافه کردم و تو توضیحات ازش قدردانی کردم اما برخوردش بیشتر تمسخر و بی‌اهمیتی بود. در حالی که پروژه
Open Source
بود. اگر قرار نیست کسی مشارکت کنه، خب می‌شد پروژه رو کلوزسورس نگه داشت.
- آخرین مورد هم مربوط به اسکنر IP بود. برای معرفی پروژه بهش پیام دادم، اما انقدر برخوردش سرد و آزاردهنده بود که واقعاً حالم گرفته شد. یه بار گفت «مطلب مرتبط نیست»، یه بار گفت «تبلیغ نمی‌کنم». در حالی که این ابزار به نظرم برای جامعه کاربری مفید بود و صرفاً برای کمک به اکوسیستم ساخته شده بود، نه تبلیغات شخصی.
چیزی که برام عجیبه اینه که از همه انتظار حمایت برای مطرح شدن پنل و پروژه‌هاش وجود داره، اما وقتی نوبت به حمایت از دیگران می‌رسه، اون نگاه دیده نمی‌شه.
این متن برای تخریب کسی نیست؛ فقط تجربه شخصی من از همکاری و حمایتیه که انتظار داشتم متقابل باشه، اما نبود...</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/ArchiveTell/6900" target="_blank">📅 13:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6892">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LaxjHPVZ5r8S5jS6rCwHyvWxqiJMb3jnyuJoMHZs1boCzdaHQ1Q6qUy8B2qsTuJ0JSxHrE6-4SjCE33pT20MHu6LEAsN_kOWo0GsbJoCw782s_NZ-8Kxlb9-DVySe7PS3b-XB97np1iSSNiGZAv49-BiH_dBhpGSwxRrChheE2hQDX21BdUW6Xb5ZwIGlXYY0aHPnbGnTCYtPY8L0WlyXVZOe57RyETr_pF3FCwwnAL_6F_mrZeMx2k--mFfte7SZSt1TNpa7whKmDsi4KIvB_gHNNgT3QqYyJ91OeVhlyLBP_q1MCxkIUNgm8SEiesryAeuHJbr8_tQFQT-iKmcug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cITovLD9B8QkswI66RV3Mn_o2X_QQRnoGc7OmdcjYfvzSrGEg5P_WDQJ8vDMskkCpDvZy4trtksdtdhrQu-X-ebWdUcWOxytZKCDSW_at8VKsRJCW7YFZLqXxhveX_Ti8nvIUwRKvZOciCc7KsFlQS5U_59ciEUvoL0gPpAGiJqfYr0PJt7TkYVlMOuCi5hFP_icA8QFGov9WXwHvUQQFvGvQZffChg05herVe1iLN3c5Ho8PRlQgzXq0_tmnqj_i1d06cZ-YlJDw1NWy8tPUj2OIwUTzd6O_LLXPWBRiJRIpGR3Flrrw00E3OUNsapen6WBXFnLpmkE1azOWqEj7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G-7-iwbwxRcIJS-LiLrKAxJ8jae6CIYKLSGXAxRi15PsnJqqWQEz1BjTNqYgGGRf_aR7lHI_hznZhTX4RYfXCsTWhlW40-kditmR_dM6yd3N-tL-dqkG_qlEhSO6Z-XUVqU8S1mNAPbhfO0_9fV_D8dwHaeNo0MEmaRi6_TRnzL0LCFgfmsqCUAeDJTc-dXh-xnf19KYkjkjhX3m_XQNKWuA8fzD-Gpx37cY_JM2EDussN-JG38rKpCuG36O-uLq5utqBHK0YcZ7nFMikLy0ejiHcAcuvI8-DJWokU55JGebAEOZ5eR-YhVUphf82OqIOhoIe7EH3XkpKO99aQVbzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FVA4gqOM0wk73PwbRRfMIm_EsdBmO2w1CgR183qla-Pf82rwrJmBh8SqBnAndPPjE-RtSRf6MCn-uQ1A19S1Aq3uHr4GEfbTDQdNkStQe10kPVrbd7lwmknoYvnBOX6_kJ2NYVJxVth2ufZhzPwbs0x6m0PH6tbNPvo_u2WD0eM24aalhQmgVWl0gaSHKRDaU1my3tqkJexHFsH8zDGf4aju6Rx641zh4Khx8aWaJzp6x8EvsfAckxMtp6C2uw_WdJDrciEdRgX9SiXTih64RKMVnlQ37O8vzYjV8M7xm_fLgB-OOwlc27b8uQZkI28H-lhdclnfhw7xO7Ae35MjfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/ArchiveTell/6892" target="_blank">📅 13:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6887">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سایت‌های Torrent برای دانلود مدل‌های LLM
1.
https://ckpt.cc/
2.
https://huggingbay.xyz/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/6887" target="_blank">📅 12:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6886">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏
🚀
معرفی ‌VoiceTypr⁩؛ تایپ صوتیِ هوشمند و کاملاً آفلاین!
🎙
✨
( از زبان فارسی پشتیبانی میکنه )
‏این ابزارِ فوق‌العاده دقیقاً مثل یک دستیارِ شخصی روی سیستم‌عاملِ شما عمل می‌کنه، کافیه دکمه‌ی میانبر رو بزنید و شروع به صحبت کنید تا متن‌تون دقیقاً همون‌جایی که نشانگرِ موس هست، ظاهر بشه.
‏
🔥
ویژگی‌ها:
🔹
حریم خصوصی مطلق: پردازش‌ها کاملاً آفلاین انجام می‌شه و هیچ داده‌ای از سیستم شما خارج نمی‌شه.
‏‌
🔹
سرعتِ بی‌نظیر: به لطفِ بهینه‌سازی‌های سخت‌افزاری، حتی روی سیستم‌های معمولی هم مثل برق و باد کار می‌کنه.
🔹
‏ پشتیبانی گسترده: بیش از ۹۹ زبانِ مختلف رو پوشش می‌ده تا هیچ محدودیتی نداشته باشید.( شامل زبان فارسی)
🔹
‏ یکپارچگی عالی: قابلیتِ درجِ مستقیمِ متن در هر نرم‌افزاری که باهاش کار می‌کنید.
گیت هاب پروژه
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/6886" target="_blank">📅 11:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6885">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🛡️
؛ungoogled-chromium؛ کرومیوم بدون وابستگی‌های گوگل
اگر به دنبال یک مرورگر سریع، سبک و نزدیک به تجربه اصلی Chromium هستید اما نمی‌خواهید ارتباطات غیرضروری با سرویس‌های گوگل داشته باشید، ungoogled-chromium یکی از گزینه‌های جذاب است.
✨
ویژگی‌های مهم:
🔹
حذف وابستگی‌ها و سرویس‌های اختصاصی گوگل
🔹
کاهش درخواست‌های پس‌زمینه به دامنه‌های گوگل
🔹
حذف کدهای مربوط به سرویس‌های گوگل
🔹
تمرکز بیشتر روی حریم خصوصی، شفافیت و کنترل کاربر
🔹
حفظ ظاهر و تجربه نزدیک به Chromium اصلی
🔹
امکان شخصی‌سازی بیشتر با فلگ‌ها و تنظیمات اضافی
این پروژه در واقع همان Chromium است، اما با تغییراتی برای کسانی که می‌خواهند کنترل بیشتری روی مرورگر خود داشته باشند.
📌
مناسب برای:
✅
کاربران علاقه‌مند به حریم خصوصی
✅
کسانی که مرورگر سبک و بدون سرویس‌های اضافی می‌خواهند
✅
کاربران لینوکس، ویندوز و macOS که دنبال جایگزین Chromium هستند
🔗
پروژه متن‌باز
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6885" target="_blank">📅 11:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6884">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚀
؛Archive Scanner v1.0.3 منتشر شد!  جدیدترین نسخه‌ی Archive Scanner با بهبودهای مهم در دقت، سرعت و امکانات منتشر شده است.
✨
تغییرات مهم:
⚡️
اصلاح کامل تست سرعت دانلود (اندازه‌گیری دقیق‌تر و عبور از فیلترینگ SNI)
📤
اضافه شدن تست سرعت آپلود برای هر IP
🤖
ساخت…</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/6884" target="_blank">📅 11:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6883">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ایپی تمیز کلودفلر
مخابرات
104.19.2.34
104.18.135.100
172.67.80.2
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6883" target="_blank">📅 11:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6881">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شاید من ی مدتی دور باشم
بقیه دوستان هستند
حالم این روزا، حال خوبی نیست
💔
مثل حال عقاب بی‌پرواز</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6881" target="_blank">📅 00:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6880">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✅
آموزش کامل SillyTavern + اتصال API شخصی + استفاده از شخصیت‌های آماده سلام رفقا!
👋
اگر API شخصی داری (مثل OpenRouter، OpenAI، Groq، DeepSeek یا هر سرویس OpenAI-Compatible)، با SillyTavern می‌تونی از شخصیت‌های آماده استفاده کنی و تجربه‌ای بسیار حرفه‌ای‌تر…</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6880" target="_blank">📅 23:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6879">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✅
آموزش کامل SillyTavern + اتصال API شخصی + استفاده از شخصیت‌های آماده
سلام رفقا!
👋
اگر API شخصی داری (مثل OpenRouter، OpenAI، Groq، DeepSeek یا هر سرویس OpenAI-Compatible)، با
SillyTavern
می‌تونی از شخصیت‌های آماده استفاده کنی و تجربه‌ای بسیار حرفه‌ای‌تر از بسیاری از سرویس‌های چت هوش مصنوعی داشته باشی.
🚀
۱) نصب SillyTavern
۱.
آخرین نسخه
Node.js LTS
را نصب کنید.
۲.
آخرین نسخه SillyTavern را از صفحه Releases دریافت کنید:
https://github.com/SillyTavern/SillyTavern/releases
۳.
فایل را استخراج کنید.
۴.
فایل
Start.bat
را اجرا کنید.
۵.
مرورگر به‌صورت خودکار باز می‌شود. اگر نشد، این آدرس را باز کنید:
http://localhost:8000
👤
۲) دانلود شخصیت‌های آماده
یکی از بهترین منابع کارت شخصیت:
https://chub.ai
می‌توانید عباراتی مثل این‌ها را جستجو کنید:
girlfriend
romance
friend
assistant
waifu
anime
fantasy
کارت دلخواه را دانلود کنید.
کارت‌های شخصیت شامل اطلاعاتی مثل شخصیت، پیام آغازین، نمونه مکالمه و تنظیمات نقش‌آفرینی هستند.
📥
۳) وارد کردن کارت به SillyTavern
وارد بخش
Characters
شوید.
روی
Import Character
کلیک کنید.
فایل PNG یا JSON کارت را انتخاب کنید.
یا فایل را مستقیماً داخل برنامه Drag & Drop کنید.
🔌
۴) اتصال API شخصی
از منوی
API Connections
وارد تنظیمات شوید.
تنظیمات:
API Type
Chat Completion
Source
OpenAI Compatible
سپس اطلاعات API خود را وارد کنید.
نمونه Base URL:
OpenRouter
https://openrouter.ai/api/v1
OpenAI
https://api.openai.com/v1
Groq
https://api.groq.com/openai/v1
DeepSeek
https://api.deepseek.com/v1
سپس:
API Key
مدل (Model)
را وارد کرده و روی
Connect
بزنید.
اگر اتصال سبز شد، همه چیز آماده است.
💬
۵) شروع گفتگو
شخصیت موردنظر را انتخاب کنید و گفتگو را آغاز کنید.
کیفیت پاسخ‌ها بیشتر به
مدل هوش مصنوعی
و
کیفیت کارت شخصیت
بستگی دارد، نه خود SillyTavern.
⚙️
تنظیمات پیشنهادی
Temperature:
0.8 - 1.0
Context Size:
تا جای ممکن بیشتر (در صورت پشتیبانی مدل)
Streaming:
روشن
System Prompt:
متناسب با کاربرد خود تنظیم کنید.
💡
نکات
✅
از کارت‌های با دانلود و امتیاز بالا استفاده کنید.
✅
هر API سازگار با استاندارد
OpenAI-Compatible
معمولاً در SillyTavern قابل استفاده است.
✅
مدل‌های مختلف رفتار متفاوتی دارند؛ چند مدل را امتحان کنید تا بهترین نتیجه را بگیرید.(ممکنه یه مدل اصن جواب نده!)
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6879" target="_blank">📅 23:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6878">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✨
وگا — دستیار هوش مصنوعی تلگرام
قدرتمندترین ربات هوش مصنوعی فارسی، برای پیوی، گروه و کانال شما!
🚀
━━━━━━━━━━━━━━
🧠
مدل‌های هوش مصنوعی
از بین قوی‌ترین مدل‌های دنیا، مدل دلخواهت رو برای چت انتخاب کن:
-
🧠
Claude Opus 4.8
-
🔮
Claude Sonnet 4.6
-
🐋
Deepseek 4 Pro
-
🐉
Qwen 3.6
-
💎
GLM 5.2
-
🍃
Gemma 4
-
🦙
Llama 4
-
🚀
GPT-4
-
🧬
Minimax M3
-
🐬
Mimo 2.5
━━━━━━━━━━━━━━
📢
فعال‌سازی در کانال شما
وگا رو زیر پست‌های کانالت فعال کن! کافیه ربات در کانال و گپ متصل به آن ادمین بشه تا زیر هر پست، کامنتی کوتاه و جذاب بذاره — دقیقاً مثل کانال آرشیو تل.
🔍
جستجوی زندهٔ وب
پاسخ‌های به‌روز و دقیق، برگرفته از جدیدترین منابع اینترنتی.
🔗
خواندن لینک‌ها و مخازن گیت‌هاب
لینک بفرست تا محتوای صفحه رو بخونه؛ ریپازیتوری‌های GitHub رو هم مستقیم آنالیز می‌کنه.
📦
👁
تحلیل عکس، ویدیو و PDF
عکس، ویدیو، فایل PDF و فایل صوتی رو می‌بینه، می‌شنوه و به‌طور کامل تحلیل می‌کنه.
━━━━━━━━━━━━━━
📰
اخبار روز
گزیده‌ای از تازه‌ترین اخبار در سه دسته: سیاسی ,  ورزشی , تکنولوژی — با به‌روزرسانی 5 ساعته.
🧮
حل سوالات درسی و علمی
سوال درسی یا علمیت رو به‌صورت متن یا عکس بفرست وگا با استفاده از به‌روزترین منابع، پاسخی کوتاه، دقیق و کامل می‌ده.
❄️
قیمت لحظه‌ای ارز و طلا
قیمت زنده رو در لحظه با نمایش اخرین تغییرات در روز بگیر
━━━━━━━━━━━━━━
📚
وگا ویکی
دستیاری هوشمند برای پرسش‌وپاسخ: سوال‌های عمومی رو خودش جواب می‌ده و برای موضوعات دانشنامه‌ای مقالهٔ مرتبط از ویکی‌پدیای فارسی رو پیدا و بررسی می‌کنه و بر اساس اون پاسخ می‌ده و لینک مقاله رو هم می‌پذیره.
👨‍💻
وگا کد
ابزاری حرفه‌ای برای کدنویسی، مجهز به مدل‌های GLM 5.2، Deepseek 4 Pro و Minimax M3.
همچنین:
🎨
ساخت عکس
🎙
ویس‌چت
🔤
تبدیل صدا به متن و برعکس
🌐
ترجمه به هر زبان
━━━━━━━━━━━━━━
📢
@ArchiveTell
-
@VegaEnter</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6878" target="_blank">📅 22:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6876">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7nK1bvHwKTV0GGtLAZWLsNj1lXLI-K7vNd7SeYysJXrNBo5-6PWgu2z2NvNvVyQIFjmSd71IZNnIQLi1Bc9ekigqmjGUCkewWlVdG0rLNkJviw7yJpxsSYs7cP68UJjztBG6uhaF86CjIql9sEr9ZpRdzcCZgGhHIfN_wEB6PBGKqkMoHGi88bDTYI9vjEHx8RigTeXYx7IRPoEbARtUKzRfBBZFxuaW-eckVEr51a2VHSz4N1LAc1pRxY8ZkuHIfwvhC4Ol3EjqjLtughS-G6vVAbWwrDikFGKADIFOC-ftKqBzu0rh0EQQqaSV9b4OcM0GLN0q8Es_Ki-qc1qqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a77ed13056.mp4?token=WuwZQrhLbSDUeu3mFbOqhHEuZNdP_FIPcwxuSKg6MVtFTeYQbWaaYyLUc1xZzNIIeEXEM1YfDDOu__PcvNfZnfYhLgUZT92zw0SesubJWEcENMhgc56FMThPyw5sRPHf9XPaT6hpbheEfdeOqhixyIbJNBD0O_FM7rDeTGwPFNWNtHnLlvlfjW4oFyIq8rjXQt580tMexSBlRcfmuRUOGKUp3iEjSBxfzFzlaoZwj10St4y224mhvJuOSASG70-_tbU-dSHDhm4VaxU2H5dqBDwBsVzpJD1qMDRiGT29f22DxpVsjuyhJ6o68wdO5xk4yG0M0N7BhDov3tHhkG0BZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a77ed13056.mp4?token=WuwZQrhLbSDUeu3mFbOqhHEuZNdP_FIPcwxuSKg6MVtFTeYQbWaaYyLUc1xZzNIIeEXEM1YfDDOu__PcvNfZnfYhLgUZT92zw0SesubJWEcENMhgc56FMThPyw5sRPHf9XPaT6hpbheEfdeOqhixyIbJNBD0O_FM7rDeTGwPFNWNtHnLlvlfjW4oFyIq8rjXQt580tMexSBlRcfmuRUOGKUp3iEjSBxfzFzlaoZwj10St4y224mhvJuOSASG70-_tbU-dSHDhm4VaxU2H5dqBDwBsVzpJD1qMDRiGT29f22DxpVsjuyhJ6o68wdO5xk4yG0M0N7BhDov3tHhkG0BZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی Hugging Bay؛ دنیای مدل‌های هوش مصنوعی، یک‌جا کنار هم!
🏴‍☠️
✨
دنبال یه مدل AI خاص برای پروژه‌ات هستی ولی بین صدها مخزن و لینک مختلف گم میشی؟ پیدا کردن بهترین LLM، مدل ویدیویی یا حتی Agent مناسب واقعاً می‌تونه وقت‌گیر باشه.
؛Hugging Bay مثل یه Torrent Tracker برای دنیای هوش مصنوعیه که انواع مدل‌های اوپن سورس و حتی مدل‌های منتشرشده رو یکجا جمع کرده. جذاب‌ترین بخشش هم جستجوی هوشمنده؛ فقط نیازت رو به زبان طبیعی بنویس تا بهترین مدل رو بهت پیشنهاد بده.
🔥
ویژگی‌ها:
1️⃣
جستجوی هوشمند: پیدا کردن مدل‌ها با زبان طبیعی مثل «بهترین Embedding Model برای RAG».
2️⃣
آرشیو کامل: دسترسی به LLMها، مدل های ویدئو و صدا و AI Agents در یک مکان.
3️⃣
؛Semantic Re-ranking: نتایج جستجو بر اساس مفهوم و کیفیت، نه فقط کلمات کلیدی.
4️⃣
مناسب توسعه‌دهنده‌ها: پیدا کردن سریع مدل مناسب برای پروژه‌های تجاری یا شخصی.
5️⃣
؛Open-Source Friendly: مرجع جذاب برای کشف و دانلود مدل‌های متن‌باز.
🔗
https://huggingbay.xyz/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/6876" target="_blank">📅 21:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6875">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🌐
کامپیوترت رو به یک هات‌اسپات حرفه‌ای تبدیل کن!
با MyPublicWiFi می‌تونی لپ‌تاپ یا کامپیوتر ویندوزی‌ات رو به یک Wi-Fi Hotspot تبدیل کنی و اینترنت رو با موبایل، لپ‌تاپ و سایر دستگاه‌ها به اشتراک بذاری.
✨
ویژگی‌ها:
🌍
اشتراک‌گذاری اینترنت از طریق Wi-Fi، LAN، VPN، مودم USB و...
🔓
اشتراک‌گذاری اتصال VPN با دستگاه‌های متصل
👥
نمایش و مدیریت دستگاه‌های متصل
🛡️
امنیت با رمزنگاری WPA2 و فایروال داخلی
🚫
مسدودسازی سایت‌ها، سرویس‌ها و برنامه‌های خاص
📶
مدیریت پهنای باند، فیلتر تبلیغات و جلوگیری از Torrent
🏨
ساخت صفحه ورود (Captive Portal) مانند هتل‌ها و کافی‌شاپ‌ها
⚡
اجرای خودکار هات‌اسپات پس از روشن شدن ویندوز
💡
یک ابزار رایگان، سبک و کاربردی برای خانه، محل کار، دانشگاه و سفر.
🔗
دانلود:
https://mypublicwifi.com
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6875" target="_blank">📅 20:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6874">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">100 گیگابایت از خیر گرامی
😛
❤️
محمدامین
vless://86cf09aa-80b7-431f-a1eb-7b95c2b8f122@amin.sylixteam.ir:8443?encryption=none&extra=%7B%22mode%22%3A%22auto%22%2C%22xPaddingBytes%22%3A%22100-1000%22%2C%22xmux%22%3A%7B%22cMaxReuseTimes%22%3A0%2C%22hKeepAlivePeriod%22%3A30%2C%22hMaxRequestTimes%22%3A%222000-2300%22%2C%22hMaxReusableSecs%22%3A%221800-3000%22%2C%22maxConnections%22%3A%2216%22%7D%7D&fp=chrome&host=amin.sylixteam.ir&mode=auto&path=%2Fccc&pbk=v6EuCPV1jYoSkTYuZ3G98xQE_DECYRvaBKZslRWgLCI&security=reality&sid=6ce858de1459bfe5&sni=www.samsung.com&spx=%2FQf36mL3kluzRLYn&type=xhttp&x_padding_bytes=100-1000#Download-Free-100GB
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/6874" target="_blank">📅 20:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6873">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این قسمت Fragment تو برنامه V2rayng و... رو ور برین بهتر میشه اینترنت
در کل ریده شده
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6873" target="_blank">📅 20:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6871">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXpEELKj12Hk-CmC8Dl1Xu_d2ZzU6CmIh0x1i-Yrdx1UHD5udfpl__sqPrpDAIKMVg2oFNEKCJwBGvYgKsZABprzTWJMWigAFQ7XgyE9-MTQipUGD0his7DkefrkZFaofAzA1h6KFQDo42BbVhd0xh4paV_l6QnB2j_EQCJS2bLP9qTKDzN2M0cRyJMWa7BdsIqKjVDhhlQHJGLoeMGXMElNutXoKm5AkCmLmUnCNXCxkTkBs0q3RgoA2juZQYW0IyD8J_OGnSkAmXG2S1CWrj33ItWXoyYGtKyTuwNwMfGEMRF_GI5ltZpyXvrNVljXygCUr7ipFz1OzjSw9jL0Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📚
معرفی ‌CheatReader⁩؛ دستیار مطالعه در محیط کار!
🤫
📖
‏‌CheatReader⁩ یک ابزار عالی برای مطالعه در محیط کار است. با استفاده از این ابزار، می‌توانید کتاب یا رمان مورد علاقه‌تان را در یک پنجره شناور در گوشه دسکتاپ پین کنید و همزمان به کارهای اصلی‌تان برسید.
‏
🔥
ویژگی‌ها:
‏‌1⁩️⃣ پنجره شناور برای مطالعه در محیط کار
‏‌2⁩️⃣ حالت‌های متنوع مطالعه، از جمله حالت شفاف و نمایش تک‌خطی
‏‌3⁩️⃣ پشتیبانی از فرمت‌های مختلف، از جمله ‌TXT⁩، ‌EPUB⁩، ‌PDF⁩، ‌DOCX⁩ و غیره
‏‌4⁩️⃣ شخصی‌سازی، از جمله تنظیم فونت و جستجوی متن
‏
⚙️
مشخصات:
‏• پلتفرم: ویندوز، مک، لینوکس
‏• منبع: رایگان و متن‌باز
‏
🔗
لینک پروژه: ‌
http://github.com/yaoyao2mm/cheatreader
⁩
──────────────────────────────
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6871" target="_blank">📅 17:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6870">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tq88wIvnU98B9raX4WGi3gPWRp42ZzxdZjrsJHQS89NIYsiQI4-7278D__s07dosnEZKEOQe2nqcXcD8bljwIOiurzpeQjhUggshNylqudUr8JPFkfZAqJZm_4LPx-cRYDj5VJGHKRJyg34XdwznjCJqFhYeQnH9kxp6SkSGd40-tjazfMYd3_ZoUbYoLEdNZzDNfSeMbw_63ts9xN44JImSHZ8RAIBST5ZuPBFCNHsAFYZUlV7gPZQzrskZXB_d3kXCgHRFqmyXNkAd-U4zOC4Z_M0RC7Pgqfco4ohQG0m_2By-UpuDqR_7RudeeAwpnycNreCwDoTDjg0yfsIM-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡️
فورت (Fort)
🔥
یک فایروال (Firewall) قدرتمند و متن‌باز برای سیستم‌عامل ویندوز است که با کنترل ترافیک ورودی و خروجی شبکه، امنیت سیستم را افزایش می‌دهد.
✨
امکانات کلیدی:
🔹
کنترل و فیلتر کردن ترافیک شبکه برای برنامه‌ها و سرویس‌های مختلف
🔹
ایجاد و مدیریت قوانین اختصاصی برای دسترسی برنامه‌ها به اینترنت
🔹
مانیتورینگ لحظه‌ای فعالیت‌های شبکه و نمایش جزئیات اتصالات
🔹
سبک، رایگان و دارای رابط کاربری ساده
🔗
https://github.com/tnodir/fort
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6870" target="_blank">📅 16:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6868">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🎬
آرشیو رایگان فیلم و سریال بدون سانسور
اگر دنبال یک مرجع برای تماشا و دانلود فیلم و سریال هستید،
PunkMovie
یکی از گزینه‌های خوب است.
✅
ویژگی‌ها: • آرشیو بزرگ از فیلم و سریال‌های خارجی • نسخه‌های
بدون سانسور
• به‌روزرسانی سریع با انتشار قسمت‌ها و فیلم‌های جدید • امکان تماشای آنلاین و دانلود • اپلیکیشن اختصاصی اندروید
🔗
لینک:
https://punkmovie.top
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6868" target="_blank">📅 15:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6867">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⚡️
آپدیت Archive Scanner v1.0.1
🔧
تست سرعت دانلود درست شد (حل مشکل فیلترینگ SNI) — برای همه، بدون تنظیمات
📤
تست سرعت آپلود اضافه شد
🤖
ساخت خودکار Worker آپلود با یک کلیک (بدون نیاز به خروج از اپ)
🚀
سریع‌تر و کم‌مصرف‌تر  https://github.com/ArchiveTell/archive…</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6867" target="_blank">📅 14:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6865">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K3bb0L7Ofm_j2Qb0Xi92ri0vrSmVejQiTv-XlWrnC87c7ZFB2ZUAmllCgHDGjgeSIKgCp4wXqS2ueDJtqtOp1b6Rq0HtdRO_ETrmXWX5L915fXksRoxYSaXDY_wCuUU7ppGPoIHXFz-CjajB4vMf7qdWkllLW7L0o2QBGqNDLrLdQkEV4zjQNwGGC6qVeFAEw8WzLCKHdTdKkWSwmc9mprMvZi6cLmBel3-TYoXDGcpOptILooyaNAJYpB9MrOJ1TIoUtLBK9ow33KHKipg13pEmIt50SAmpGaUeXRPT3UdyyCK-CGbG829QU349WkBUMC4l-HjG3lR6zBRTLMYSXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H2Pu3jWdbcrOylqHkJ8nrFhm9064i1oPgY1qOqVNErbU1fGo-7eaph-HuIXfFZsYZ2oe0G1me0nZX8K96n6KxLoDEZNRHDsWvk9Oo2gV6qpaDyS9KMJQY8S8snqErK18VjzEjaEk3mnGlCN18K41NH4ESsu_JELpgdif0Qg1AyLW3AryEmhqXQZLhGYi1UygXHBSxsBmXJYj1_NOEKP7TkYf78FC-Rm5gRxT_pWmFaVq8hUUPrstgQ21qaWUMDz67K9QvS-PSOurgdT8R_mEj8rYObQYx3uCarTMLuk2sOhV5TalrTHUpCb_hVKpWU6Z2E2-r_Ejfnx4hm13Ls9lfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
آپدیت Archive Scanner v1.0.1
🔧
تست سرعت دانلود درست شد (حل مشکل فیلترینگ SNI) — برای همه، بدون تنظیمات
📤
تست سرعت آپلود اضافه شد
🤖
ساخت خودکار Worker آپلود با یک کلیک (بدون نیاز به خروج از اپ)
🚀
سریع‌تر و کم‌مصرف‌تر  https://github.com/ArchiveTell/archive…</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6865" target="_blank">📅 13:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6864">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚀
انتشار رسمی Archive Scanner v1.0.0  (اسکنر آیپی تمیز کلودفلر) به عنوان عضوی از کامیونیتی، همیشه جای خالی یک اسکنرِ دقیق، سریع و پایدار را حس می‌کردم. ابزارهای موجود یا بسیار کند بودند، یا با باگ‌های عجیب همراه بودند. تصمیم گرفتم این خلاء را شاید خودم پر…</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/6864" target="_blank">📅 13:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6863">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">📡
وای‌فای؛ دوربین نامرئی آینده؟
محققان نشان داده‌اند روترهای جدید Wi-Fi با کمک هوش مصنوعی می‌توانند تغییرات امواج را تحلیل کنند و بدون نیاز به گوشی یا وسیله همراه، حضور و حتی هویت افراد را تشخیص دهند.
🧠
این فناوری برای خانه‌های هوشمند و امنیت کاربرد دارد، اما می‌تواند نگرانی‌های جدی درباره حریم خصوصی و ردیابی افراد ایجاد کند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/6863" target="_blank">📅 13:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6862">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvgb9FvqLooXxPXCOseUyvLvOBm1r-8mjbOAJaUSO6JIbfjQ4JC59BrZbpa7ysAblNhoNEQlSyzqTROw4lO-zUmA6pYhIeJScRQ5_jvZatnaRCL6mR2ihxrP6Fq3K8WbKKPPcAP38kVjJ9iZSYeE3yNVts-_4erpHkUJZdWvOqTNuT541Pb7RdfBogDpS5KMUnQebwC7gRc5CjW5_a1OQUs5FIfLjhx1yRzO_um5dWOqpyKt2r934DVrTQnJCkVZfg-v7Ste7HjrV5_552NSdGHHkEBMzWMZEgkgIL78RWCskaWp9_yEKcUnB4cItMsrg9DKGmqw_XugBZhFWKbptA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📦
‌RepoStore⁩: فروشگاه اپلیکیشن‌های گیت‌هاب از راه رسید!
🚀
‏دیگه نیازی نیست برای پیدا کردن پروژه‌های جذاب در گیت‌هاب، ساعت‌ها در مخازن مختلف جستجو کنید.
‌RepoStore⁩
دقیقاً مثل یک پلی‌استور اختصاصی برای گیت‌هاب عمل می‌کند.
‏
🌟
چرا باید از آن استفاده کنید؟
‏•
تجربه کاربری آشنا:
محیطی مشابه فروشگاه‌های رسمی که کار با آن بسیار ساده است.
‏•
مدیریت هوشمند:
نصب و آپدیت مستقیم اپلیکیشن‌ها بدون درگیری با فایل‌های ‌APK⁩ پراکنده.
‏•
شفافیت کامل:
امتیازها و تعداد ستاره‌های گیت‌هاب مستقیماً نمایش داده می‌شوند تا بهترین ابزارها را بشناسید.
‏•
دسترسی آزاد:
کاملاً رایگان و متمرکز بر پروژه‌های متن‌باز.
🔗
https://github.com/samyak2403/RepoStore
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6862" target="_blank">📅 13:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6861">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚀
انتشار رسمی Archive Scanner v1.0.0  (اسکنر آیپی تمیز کلودفلر) به عنوان عضوی از کامیونیتی، همیشه جای خالی یک اسکنرِ دقیق، سریع و پایدار را حس می‌کردم. ابزارهای موجود یا بسیار کند بودند، یا با باگ‌های عجیب همراه بودند. تصمیم گرفتم این خلاء را شاید خودم پر…</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6861" target="_blank">📅 13:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6860">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ArchiveTel
pinned «
🚀
انتشار رسمی Archive Scanner v1.0.0  (اسکنر آیپی تمیز کلودفلر) به عنوان عضوی از کامیونیتی، همیشه جای خالی یک اسکنرِ دقیق، سریع و پایدار را حس می‌کردم. ابزارهای موجود یا بسیار کند بودند، یا با باگ‌های عجیب همراه بودند. تصمیم گرفتم این خلاء را شاید خودم پر…
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6860" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6859">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Tr - infinity.npvt</div>
  <div class="tg-doc-extra">1.5 KB</div>
</div>
<a href="https://t.me/ArchiveTell/6859" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">روز خوبیو توی این دوران سخت براتون ارزو میکنم
😜
🥰
Password :
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6859" target="_blank">📅 05:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6858">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔥
دریافت API رایگان بدون ثبت‌نام! اگر برای پروژه‌ها یا ربات‌های خود به یک API رایگان نیاز دارید، این سایت می‌تواند گزینه جالبی باشد.  ؛Dahl Inference بدون نیاز به ثبت‌نام، تنها با چند کلیک یک API Key در اختیارتان قرار می‌دهد که می‌توانید از آن برای استفاده…</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6858" target="_blank">📅 01:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6857">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔥
دریافت API رایگان بدون ثبت‌نام!
اگر برای پروژه‌ها یا ربات‌های خود به یک
API رایگان
نیاز دارید، این سایت می‌تواند گزینه جالبی باشد.
؛
Dahl Inference
بدون نیاز به ثبت‌نام، تنها با چند کلیک یک
API Key
در اختیارتان قرار می‌دهد که می‌توانید از آن برای استفاده از مدل‌های مختلف هوش مصنوعی استفاده کنید.
ویژگی‌ها:
• بدون نیاز به ساخت حساب • دریافت فوری API Key • دسترسی به مدل‌های مختلف • مناسب برای تست، توسعه و پروژه‌های شخصی
هر کلید 100 میلیون توکن رایگان میده
😁
🔗
دریافت API:
https://inference.dahl.global/chatKeys#models
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/6857" target="_blank">📅 01:34 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6856">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">؛
🎨
Lake: اپلیکیشن آرامش‌بخش رنگ‌آمیزی برای بزرگسالان
اگر بعد از یک روز پرمشغله دنبال راهی برای استراحت و دور شدن از استرس هستید،
Lake
یکی از بهترین گزینه‌هاست.
این اپلیکیشن مجموعه بزرگی از طرح‌های رنگ‌آمیزی را که توسط هنرمندان واقعی طراحی شده‌اند در اختیارتان قرار می‌دهد. از
مناظر و طبیعت
گرفته تا
معماری، دکوراسیون، حیوانات و پرتره
، برای هر سلیقه‌ای طرحی پیدا می‌شود.
✨
امکانات: •
🖌️
صدها طرح باکیفیت •
🎯
حالت هوشمند برای جلوگیری از خروج رنگ از خطوط •
🎨
ابزارها و پالت‌های رنگ متنوع
🆓
کلی طرح رایگان برای شروع
اگر به دنبال یک سرگرمی ساده و آرامش‌بخش هستید، Lake ارزش امتحان کردن را دارد.
نکته: فعلا فقط برای آیفون در دسترسه
🔗
سایت:
https://lakecoloring.com
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6856" target="_blank">📅 01:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6854">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EJwQsDjkl_qemT3CXqlKuCeb5KvmDmZc2wguTgaAm7ke2k_SVQBejnCPKT4CQyaqRmZ9v3ZteayqHds2iV-yvfxRYjzArefIOeynvjIOWYpz48wko-PoSzs6io98m-P7AQfksyE6DTkwF58KHnl18ELo3EU76NK9OPkNRnVDhSGXL5qFMCnOmKlL0908vi1GTCn3Rqn1XSN9HbsGEYv5bvPqyXXJiAjnfNfs9LNnG_lKpYqCV5OhFhcVcUezYYAAt4vbb0tAK5u6gg7WpdAR7hcsrfUSIBsi5oTV_Z58w7iow3JqaIS-1uVVHcTzn0sOFK42lhEuI4ryDkNoK6umPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lrmqQRSWFDBmMMwSdAVVpeFVu3XXWvtChGyBr54aHxqSrAp2ad8z8rpSa-soVgXp3pnOQG-oKgtJf1Zri0zwqGxcmIuMmq3_49ItQY_wTBrkr8zW-lw9pYJzZ7rhSpxUSk_a--GYSLQX9dib6A6ehbwi05ULQwkFf8a4wdloa295bItbyyEnaQiA715sv6jrfGttRL7NHZx447nCbwy_dEtFUN4qk8QNHm_VoGHgFu-8qbGkyhV66yM3UJL8mVzZ3ufY5u4V2jubNymwP3xl0wOViO1Qvev6muLLTia5khdDmBC9Y3GLuEHAohjcYTEAADyJWVO81c7DamGBkyhTIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
انتشار رسمی Archive Scanner v1.0.0  (اسکنر آیپی تمیز کلودفلر) به عنوان عضوی از کامیونیتی، همیشه جای خالی یک اسکنرِ دقیق، سریع و پایدار را حس می‌کردم. ابزارهای موجود یا بسیار کند بودند، یا با باگ‌های عجیب همراه بودند. تصمیم گرفتم این خلاء را شاید خودم پر…</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6854" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6853">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚀
انتشار رسمی Archive Scanner v1.0.0
(اسکنر آیپی تمیز کلودفلر)
به عنوان عضوی از کامیونیتی، همیشه جای خالی یک اسکنرِ دقیق، سریع و پایدار را حس می‌کردم. ابزارهای موجود یا بسیار کند بودند، یا با باگ‌های عجیب همراه بودند. تصمیم گرفتم این خلاء را شاید خودم پر کنم. امروز با افتخار نسخه اول
Archive Scanner
را به شما تقدیم می‌کنم.
🔥
قابلیت‌های فنی و تخصصی:
✅
اسکن پیشرفته SNI + TLS:
ما به پینگ ساده اکتفا نکردیم! با شبیه‌سازی کامل TLS Handshake، آی‌پی‌هایی را پیدا می‌کنیم که "واقعاً" کار می‌کنند.
⚡️
سرعتِ خیره‌کننده:
طراحی‌شده برای اسکن‌های فوق‌سریع که زمان شما را هدر نمی‌دهد.
🎯
حذف هوشمندِ آی‌پی‌های مرده (Dead-End Elimination):
فیلتر کردنِ آی‌پی‌هایی که پورتشان باز است اما عملاً ترافیک را رد نمی‌کنند.
✨
طراحی مهندسی‌شده:
طراحی و توسعه کامل توسط
Bachelor
⚡️
با تمرکز بر UI/UX مدرن (Material Design 3).
🛠
شفافیت و آینده پروژه:
من تمام تلاشم را کرده‌ام تا این نسخه در پایدارترین حالت ممکن باشد، اما چون در ابتدای مسیر هستیم (v1.0.0)، ممکن است باگ‌های جزئی وجود داشته باشد. من متعهد هستم که در آپدیت‌های بعدی این موارد را سریعاً برطرف کنم.
💡
خبر خوب:
این نسخه از
آپدیت درون‌برنامه‌ای (In-App Update)
پشتیبانی می‌کند؛ بنابراین به محض انتشار نسخه جدید، شما باخبر خواهید شد و نیاز به دانلودِ دستیِ مجدد نخواهید داشت.
📥
لینک دانلود مستقیم (گیت‌هاب)
این اپلیکیشن حاصل روزها تلاش مستمر من برای ارتقای استانداردهای جامعه شبکه است. اگر باگی دیدید، حتماً اطلاع دهید تا در آپدیت‌های آینده برطرف شود.</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6853" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6847">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Npjaeqf4SdNBPLQPSxXEQSevQqxsbjmWMr9yF0IapsuXWQUB0VnlHqbKnvpCRP_xcoUGozIxnqn3F-AoFbyuJsImzQvID9IxvJbNKhcx_mi7K_ygRThDSDJfyDSWnulQoo_CJSOsgpls6uasI5z9aCEvQl5vpdJfs4FTcyBfm10EmJhAVOHQgnu4ng4u6oQFQ1lnbGO3xScKxJgsYZIg_Wl6eN6v_Ht8YQTH-aluLjawkg1CylrZg-iben00l6xiXf6F87wwVUHZi9AiLwTFnLgKYlfZ6XlM_ZNQOLzc1vtD1ysB00WC2F4A8F2r1SxUtj_5zfjGuJMebCTP2DJgSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">*
‏
🎮
آیا ‌GTA 6⁩ زودتر از موعد به کامپیوترها می‌آید؟**
🖥️
🔥
‏شاید غیرممکن به نظر برسد، اما توسعه‌دهندگان امولاتور ‌SharpEmu⁩ در حال برداشتن قدم‌های بزرگی برای اجرای بازی‌های ‌PS5⁩ روی ویندوز هستند!
🛠️
‏
✅
چه اتفاقی افتاده؟
‏تیم سازنده موفق شده بازی سنگین ‌Demon's Souls⁩ را تا مرحله لودینگ و صفحه اصلی روی کامپیوتر اجرا کند. این یعنی معماری ‌PS5⁩ در حال رمزگشایی است.
‏اگر این روند با همین سرعت پیش برود، برخی امیدوارند که بتوانند ‌GTA 6⁩ را قبل از انتشار رسمی نسخه ‌PC⁩، از طریق این شبیه‌ساز روی سیستم‌های قدرتمند تجربه کنند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6847" target="_blank">📅 22:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6846">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚀
۱۰۰۰ اعتبار رایگان در Flashloop برای ساخت ویدیوهای هوش مصنوعی!
🎥
اگر به ساخت ویدیو با هوش مصنوعی علاقه دارید، می‌توانید با ثبت‌نام در Flashloop، ۱۰۰۰ اعتبار رایگان دریافت کنید.
مراحل دریافت اعتبار:
1️⃣
وارد سایت شوید:
https://www.flashloop.app
2️⃣
با حساب گوگل (یا سایر روش‌ها) ثبت‌نام کنید.
3️⃣
هنگام ثبت‌نام یا در بخش مربوطه، کد زیر را وارد کنید:
Z36ZT9
🎉
با وارد کردن این کد، ۱۰۰۰ اعتبار رایگان به حساب شما اضافه می‌شود.
با Flashloop می‌توانید انواع ویدیوهای AI در سبک‌های مختلف تولید کنید و از ابزارهای ویرایش و افکت‌های متنوع آن استفاده کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6846" target="_blank">📅 20:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6845">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnu5LbujfJLl2CkJUttZslZKH_5dHDvoJzT5lwtOTwtr0zoSTI0L7DfAZKFcx6_ttJeJw8OmAvKCiacxutFNt_ZtLv9GdOP49KxZuqMZB5RDgCwAGwsLqclM8F01FHPBX_LPIIO2phXewFuhn62tqND67glR0bSvf1J2aDRWv17CBEJFph3PPfd4TV33dAE99vrr0AiIFohie4WMLRdseCWb0hcTOm7B-FtXxUi4EfKv0gjC2MTuqYdpyDrRdjTeeqJ6U1gwFxHrsen6aqDF65d5ImHy8-U0SniIMBLKHt4nCIBv3bHsq1pGahjr6yFJH_wJKtsmauRt9B5YWWvXtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐧
GameShell
GameShell
یک پروژه
متن‌باز
برای یادگیری دستورات لینوکس و
Bash
است که به‌جای آموزش سنتی، مفاهیم را در قالب مراحل و مأموریت‌های تعاملی آموزش می‌دهد
🔹
اگر قصد دارید کار با ترمینال و دستورات لینوکس را به‌صورت عملی و سرگرم‌کننده یاد بگیرید،
GameShell
می‌تواند نقطه شروع مناسبی باشد
◾️
🔺
GitHub
✔️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6845" target="_blank">📅 20:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6844">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نامحدود
🫡
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTprMWRCT21PQjRvcWk3VW1wMzdhMWJR@82.38.31.189:8080#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6844" target="_blank">📅 18:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6843">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نامحدود
🔥
vmess://771a590c-5eac-5732-b796-17251132f8d2@47.83.221.185:80?encryption=auto&security=none&type=tcp#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6843" target="_blank">📅 18:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6842">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏
💎
گنجینه‌ای از ۱۰,۰۰۰ پرامپت طلایی!
🍌
✨
‏اگر به دنبال خلق تصاویر خیره‌کننده با هوش مصنوعی هستید، این مخزن دقیقاً همان چیزی است که نیاز دارید!
🎨
🚀
‏
✅
ویژگی‌های این مجموعه:
🔹
بیش از ۱۰ هزار پرامپت منتخب و تست‌شده
‏
🔹
بهینه‌شده برای
‌Nano Banana Pro (Google Gemini)⁩
‏
🔹
سازگاری کامل با ۸ مدل برتر دنیا (از جمله ‌Midjourney⁩، ‌DALL-E⁩ و ‌Flux)⁩
‏
🔹
همراه با پیش‌نمایش تصاویر برای درک بهتر خروجی
‏
🔹
کاملاً متن‌باز (‌Open Source)⁩ و رایگان
‏
🔗
https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6842" target="_blank">📅 16:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6841">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416755798a.mp4?token=h3a7a7Ixai9FjORFIRHt1bJiynYoypWkToOETMVlsjQPNqYGYVHCfkKxtflvsvQbJ7HiuJXdlqZmnRnA4wx1tX3o8eBS1JwaVpX51MSpQFLg2D5RWjOp9sB2Q7iLSVbnK6RyxCIOcd_iqlJl3A6CObxiZBtw3mYtZKze_Diri6G1aQ_NtsB9cm7IO5RsMLAeuZRhyXLxHbn8aVHiqE50N1yMYwZs8JjKXgum9vX0NQFM0dpioTw53cJm9BIY9FHd3ymqt0IRZSAEXphEJf_CvYV1WPX2ZMMsWKANV0KfRMPxfQcP0JmPslZzkttg7rGDr5rzR0aOLpEjU_LRGR_idA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416755798a.mp4?token=h3a7a7Ixai9FjORFIRHt1bJiynYoypWkToOETMVlsjQPNqYGYVHCfkKxtflvsvQbJ7HiuJXdlqZmnRnA4wx1tX3o8eBS1JwaVpX51MSpQFLg2D5RWjOp9sB2Q7iLSVbnK6RyxCIOcd_iqlJl3A6CObxiZBtw3mYtZKze_Diri6G1aQ_NtsB9cm7IO5RsMLAeuZRhyXLxHbn8aVHiqE50N1yMYwZs8JjKXgum9vX0NQFM0dpioTw53cJm9BIY9FHd3ymqt0IRZSAEXphEJf_CvYV1WPX2ZMMsWKANV0KfRMPxfQcP0JmPslZzkttg7rGDr5rzR0aOLpEjU_LRGR_idA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
؛Traycer Desktop App منتشر شد!
رایگان، متن‌باز و ساخته‌شده برای AI Orchestration.
✨
قابلیت‌های جدید:
• استفاده از اشتراک‌های فعلی مثل Claude، Codex، Opencode و...
• ارتباط Agent-to-Agent و Loops
• ؛Workspaceهای دائمی با Tab و Sub-tab
• اشتراک‌گذاری Taskها و همکاری با اعضای تیم
امروز دیگر توانایی مدل‌های هوش مصنوعی چالش اصلی نیست.
چالش واقعی، ساخت محیطی است که Agentها بتوانند به‌صورت هماهنگ با هم کار کنند، حافظه مشترک داشته باشند و از هر جایی ادامه‌ی کار را از سر بگیرند.
؛Traycer دقیقاً برای حل همین مسئله ساخته شده است.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6841" target="_blank">📅 15:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6839">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚀
تبدیل Qwen Chat به API رایگان!
اگر همیشه دوست داشتید از
Qwen
داخل پروژه‌ها، ربات‌ها یا برنامه‌های خود استفاده کنید، این پروژه دقیقاً برای همین ساخته شده است.
؛
FreeQwenApi
سایت
Qwen Chat
را به یک
API رایگان و سازگار با OpenAI
تبدیل می‌کند؛ یعنی می‌توانید بدون تغییر زیاد در کد، از مدل‌های Qwen داخل پروژه‌های خود استفاده کنید.
✨
قابلیت‌ها
✅
تبدیل Qwen Chat به API
✅
سازگار با OpenAI API
✅
پشتیبانی از Streaming
✅
پشتیبانی از فایل، تصویر و Web Search (در مدل‌های پشتیبانی‌شده)
✅
قابل استفاده در Open WebUI، LobeChat، Dify، Claude Code و...
🛠️
آموزش راه‌اندازی
1️⃣
پروژه را دانلود کنید
git clone https://github.com/y13sint/FreeQwenApi cd FreeQwenApi
2️⃣
وابستگی‌ها را نصب کنید
npm install
3️⃣
پروژه را اجرا کنید
npm start
4️⃣
وارد حساب Qwen شوید
توکن (Session Token) اکانت Qwen خود را داخل پروژه قرار دهید؛ از این به بعد می‌توانید از Qwen مثل یک API معمولی استفاده کنید.
⚠️
این پروژه API جدیدی ایجاد نمی‌کند؛ بلکه از دسترسی رایگان حساب Qwen شما استفاده کرده و آن را به یک API سازگار با OpenAI تبدیل می‌کند.
🔗
GitHub:
https://github.com/y13sint/FreeQwenApi
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6839" target="_blank">📅 15:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6838">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">vless://c44c7433-5460-4269-a7de-0af05e27a48f@64.90.7.33:8080?type=kcp&headerType=none&seed=SwbMceiT2H&security=none#%D8%B1%D8%A7%DB%8C%DA%AF%D8%A7%D9%86
نامحدود
اگه دیدید قطع شد ip فیلتر شده
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6838" target="_blank">📅 14:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6837">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6X1YP7CqQYR_d2CUTNRZkjMYMKr5aZ5KZNO8IxeSEnHPnD4qLWgSEDJae1VdWmL3Ze2dyi7in-V4PnXkSi_RbVQM6O9JsoyEOB8SHU4zRwLxfBi7Im17Yl4pee_PBIl5F9O8Ro26SlTNuCnsZCK0uBaAbM3pZpm4HIdoRgBAXFJn_-SwGk_DtzhCy5oVHdLwbdJsld1SqURX0e_KOiHE5XveGjBrDM6Q1Hv2xslkAcCUpKK-1VnnXwJJfaj681XDmdG9m0uQzoL-D9a9qjysh0sOeqLizoD6J_92nAH0UlJUrdD6bm47IAP4yQrNiF4Etvlapj6RyTQU5kkuZ0VSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
✨
یک ابزار جذاب برای کار با ویدیو!
معرفی Frame؛ رابط گرافیکی بومی برای FFmpeg ساخته‌شده با Rust
🦀
؛FFmpeg فوق‌العاده قدرتمنده، اما کار با خط فرمانش برای خیلی‌ها سخت است. Frame همان قدرت را با یک رابط ساده و زیبا در اختیار می‌گذارد.
🔥
امکانات:
⚡
ارتقای کیفیت تصویر با AI (Real-ESRGAN)
🚀
شتاب‌دهی سخت‌افزاری (Apple Silicon و NVIDIA)
📦
مدیریت چند پردازش همزمان
🔒
کاملاً لوکال؛ بدون تله‌متری و بدون نیاز به حساب کاربری
💻
پشتیبانی از macOS، Windows و Linux
﻿
یک انتخاب عالی برای کسانی که با تبدیل، فشرده‌سازی و پردازش ویدیو سروکار دارند.
🎥
github.com/66HEX/frame
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6837" target="_blank">📅 04:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6836">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚀
؛Grok 4.5 رایگان شد!
مدل جدید کدنویسی Grok 4.5 از xAI برای مدت محدودی به‌صورت رایگان در ابزارهای Agent قابل استفاده است.
✨
ویژگی‌ها:
🧠
پنجره متنی 500K برای پروژه‌های بزرگ
⚡️
مناسب برای Agentهای کدنویسی و جلسات طولانی
🔌
سازگار با Hermes، Aider، OpenCode، Cline، Claude Code و تمام ابزارهای سازگار با OpenAI API
⚙️
راه‌اندازی در کمتر از ۲ دقیقه:
curl -fsSL https://x.ai/cli/install.sh | bash
سپس:
• آدرس
localhost:8000/v1
را به ابزار خود معرفی کنید.
• مدل grok-4.5 را انتخاب کنید.
• یا از API Key در کنسول xAI با آدرس پایه
https://api.x.ai/v1
استفاده کنید.
⚠️
این دسترسی محدود و موقتی است و شامل Rate Limit می‌شود. (شاید ۱۲ ساعت مونده باشه ازش) (تست نشده)
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6836" target="_blank">📅 04:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6835">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKvdtqkxj1xkfOA7-PknmIOBp-n7Ncwf3F6aqLqOFLn9_a_dTsFlgMZk1HcARZ619rE4ckWP6fmsTRECua2iUIpuwj1QX15bmxX-p6XuDnmObvuUcaSxIc0AvOYWQLntRdiP1Qj6JS0ltfufGHCn5AHOx0FzZN5POuFEs4OBlcPwxqtEDc0Q-d50-O8HJdGVWws8SBvhH97I2uexYBCpd51Ghqypw0BO4YlbBPAg0NktjVvlO3ddXkMniHWzwToiGg2e9xmnNSBpgWzaKSw2xjeblAsi6hXHMaeynjsvscWcgevqmziZpxyPBNlXpLAZBLBYgzndEKiJz1XMkR7JUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧭
؛MBCompass؛ قطب‌نما و مسیریاب متن‌باز برای اندروید
یک اپلیکیشن سبک و رایگان برای طبیعت‌گردی، کوهنوردی و استفاده روزمره؛ بدون تبلیغات، بدون ردیابی و بدون وابستگی به سرویس‌های گوگل.
✨
امکانات:
🧭
قطب‌نمای دقیق (شمال مغناطیسی و واقعی)
📍
نمایش موقعیت لحظه‌ای روی OpenStreetMap
🗺️
پشتیبانی از نقشه‌های آفلاین و آنلاین
🥾
ضبط مسیر و خروجی GPX
🔋
حجم کم (~۲ مگابایت) و مصرف باتری پایین
🔒
بدون تبلیغات، بدون جمع‌آوری داده‌های شخصی
یک گزینه عالی برای علاقه‌مندان به سفر، طبیعت‌گردی و مسیر‌یابی.
🌿
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6835" target="_blank">📅 03:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6833">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚀
آموزش اجرای Opus 4.8 در ترمینال با Claude Code توسط Agentrouter
1️⃣
ثبت‌نام در Agentrouter وارد سایت Agentrouter شوید با حساب Github ثبت‌نام کنید بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🎉
شما 125 دلار کریدیت گرفتید
2️⃣
ساخت API Key وارد سایت شوید…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6833" target="_blank">📅 00:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6831">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnlnAFGE1pwbDA-GR1UtWJDm8DnisEn-4nY_dh6rlEvm2mo5wBfHKANmQRt2pa2uNBZ_tOsp43MmmyUPEqpBMOBMrC8NKn7a_q_ZP3DwQVPB2s0YeauzxqFZVHmUUViHLEHWGUQa1syuD5WTP3cYN3hbgw4ZTIEtIkj170iWg_cGoA227LAS-le1gYu-fey9GEAqV3Do6iXqRujMaVqYZXPQsh_8BT58KTLAV_MelsUbno2BWBmKE6iXvcOQWCqubyb-ENQNHgQSBz9rGasWv0FPYCbfy3Suiu2R-P3CvHI0gWPqpGJUqW1kuhilPUV9LC6s9DnE-4uk8fWWL2-exQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☁️
🚀
؛Cloudflare Drop؛ انتشار سایت در چند ثانیه!
کافی است پوشه پروژه‌تان را داخل مرورگر Drag & Drop کنید تا سایت فوراً روی شبکه Cloudflare منتشر شود.
✨
ویژگی‌ها:
⚡
بدون نیاز به ثبت‌نام
🌍
دسترسی جهانی با تأخیر بسیار کم
📁
مناسب برای دمو، نمونه‌کار و پروژه‌های آزمایشی
⏳
نسخه‌های بدون حساب تا ۶۰ دقیقه فعال می‌مانند و سپس حذف می‌شوند؛ با ثبت‌نام می‌توانید آن‌ها را دائمی کنید.
https://cloudflare.com/drop/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6831" target="_blank">📅 00:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6829">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSSpKFtAOnW8f8ItGOE7GuPdGV6IIRB6jIgDiExqY_u386hHqIQjpLGACG7VaB8Sqt-_EryH1fCqQ3yFWC1tshXX8paT5qlTWljW_BXNxBxpYz4t8DeDl_GoacFiNteTVtZOPnS8RzGKKdo-WUAEjTIS4xjbeh5NYv6rLdQMRZGRJRnmg8uQO5i12ubc6lzp7r6-aKQqp4lTTetO6gt2GwQQWuBk8rqqAdlXC246__YDTNlMzfS5s1RFUrYg18ny7krASw30PlD1tFEGsTT5VIygE5XZ2Lv81mt1YMwDHS8Ou8WuFX7iaSjmNP_PpxFjQrd1ygIHIcXjFql4unrYiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6829" target="_blank">📅 23:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6828">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🧩
؛CanvasMind | ساخت و استقرار ورک‌فلوهای AI با بوم بصری
✨
یه ابزار متن‌باز و Low-Code برای طراحی و اجرای ورک‌فلوهای هوش مصنوعی! دیگه فقط دمو نیست، مستقیم به پروژه قابل استقرار تبدیلش کن
🚀
⚡
ویژگی‌ها:
🎨
بوم گرافیکی با Drag & Drop
🔀
شرط، حلقه و منطق کنترلی
💻
اجرا محلی یا از راه دور via SSH
🤖
دستیار هوشمند داخلی
🚀
خروجی CLI، API، Docker و Server
🔗
https://github.com/buyaka/canvasmind
#هوش_مصنوعی
#LowCode
#ورک‌فلو
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6828" target="_blank">📅 22:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6827">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">📱
💿
؛EtchDroid؛ ساخت فلش بوتیبل با گوشی اندروید
اگر کامپیوتر در دسترس ندارید، EtchDroid به شما اجازه می‌دهد فایل‌های ISO سیستم‌عامل‌های لینوکسی را مستقیماً از طریق گوشی روی فلش USB رایت کنید و یک فلش بوتیبل بسازید.
✨
ویژگی‌ها:
🔹
متن‌باز و رایگان
🔹
پشتیبانی از اکثر توزیع‌های لینوکس و Raspberry Pi
🔹
مناسب برای مواقعی که سیستم بالا نمی‌آید و فقط گوشی در دسترس است
⚠️
این برنامه از ISO رسمی ویندوز و فایل‌های DMG مک پشتیبانی نمی‌کند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6827" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6826">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🤖
؛Cogny | دستیار هوش مصنوعی بازاریابی
✨
یه ابزار فوق‌العاده که بازاریابی رو با هوش مصنوعی انجام میده! سئو، تبلیغات، تحلیل رقبا و کلی کار دیگه
🚀
⚡
ویژگی‌ها:
🎯
سئو و بهینه‌سازی محتوا
📊
تحلیل کمپین‌های تبلیغاتی
🔍
آنالیز رقبا و بازار
✍️
تولید متن تبلیغاتی
📈
اتصال به ۱۳ کانال بازاریابی
💻
کار با Claude، Cursor و Codex
💰
رایگان برای شروع · ۹ دلار برای استفاده نامحدود
🔗
https://cogny.com
#هوش_مصنوعی
#بازاریابی
#سئو
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6826" target="_blank">📅 21:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6825">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHQtvNhKDK_9u8XN9z4OSc8qYA_udaO55uXWWLTFiqBLuzTTwuldb3SdjAnxaA2eNCuu4dKnOoNhnh3vq6ERi2ygfhsb34SWM7j1uyUbeWwM_MITJYWDK0jlnswSQft9XiqotrtRF3uSjGqj2R4E2mICVTjaCPhYU3ewTLXh4u9sdfRY2uXOG8RrefWcbOAp9ubazGmtdZfXl7RMibWvucgG4YiyvenNYv6IKcppcIs7pJTOD55VLSOSx6bKIqQ8ZEoc5_wtf4WeM8fVNZa3DYHc97lbmq8L_1uAJY-ItrTqgAFurx9YkFVLO-LbsgI4WCereo6IhHAnZxDSxBfKoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6825" target="_blank">📅 20:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6824">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">104.17.14.0
104.25.49.102
ایپی تمیز کلودفلر
تست کنین
❤️
با لایک و دیسلایک و کامنت اعلام کنین
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6824" target="_blank">📅 20:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6821">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kGxeLNKa-C65CR0QRAUc7IstgKbreyxLRQo2rUzCHCmsq4NLEpLPFXK4ArLIatWVCFsaqiTnaCCl-pePkVgoc4dOOUKJeB2-AlTsLJwdvKFn9Y0bssQvWsJHzlxLeOah4g7kBx5eQnq_SG8EvqibpNe2fRklFGUGexFbYUDbJE6J08Y4ddNCWiULTR3uco9zTC0Z_omyMGIS6P4FYfDOeQgDY36cWeyzYDb3XFyzqH-xNLGfOq7lW-hJ0Da3NBOXNhEYiaMBLo86twCfB_h_amgimddSUc6ZZ9kX2Jb1R_Lr9n8fAK_rqdPtE1Ta4jwwOFql8rKbBJUEQLTSTgVBwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pEzYtAT4MsYEWE6s7ppFtp62DiNFfU9z33wXGYFQ8Jl9nxyN9T8wJpQpqgfXloUTAcwaa5dDWm7MLsz32KeoB6QfAAJR1DQlckyiGQKvX9dENYKZ6VPy-o-_UoaZy6TPN8D5pC4QbgeYBqHMhZN9V_4vp4IQsX3xb8uLg9aaUvN252KpweD7EpvqRxwH7c55rkbVkJdLMFJ19aN4zQ3BnynP11vbK2b0B4OPx11LxAiarotbr0DnuLrBWE_clFNnA1ub3-CyEGegPbHDQLVS9GIpgho7yVgQIv0Fno3dnuGgpN6CKvGNtsZ6y3IoSka91kYhbPMqm5H3TKPr9TgFbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏‌
Imgfree⁩: ابزار رایگان تولید تصویر و ویدیو با هوش مصنوعی
🤖
‏
🌐
پلتفرمی که مدل‌های پیشرفته هوش مصنوعی مانند ‌‌Midjourney⁩، ‌GPT-Image⁩ ، ‌Kling⁩ ، Nano Banana و Flux را گرد هم آورده است
📈
‏
✨
تولید تصویر و ویدیو بدون نیاز به تنظیمات پیچیده
📺
‏
🔗
لینک: ‌
https://www.imgfree.co
⁩
‏
💻
دسترسی رایگان و نامحدود برای تولید محتوای با کیفیت
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6821" target="_blank">📅 19:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6820">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxmWzxLM3c2OpSHXabPob4D8p4YMvlhxVdIYQc_GfIMsGNsDGACJmmS_1EN15d8ZGqdsg74SEM1pByhnJTrnV4vK3071kp083J6onTxUMmnoQeh7NGA5ruecOSmT3-eeqjjWJhroZBN4B9ZHt4eu6MdHapcL129QKhUtXlAoMgqxU8MBHmpcbXGzQ_u0aeKg_odg8otXa1poJzcodiD8EFuveOa4YiqII2fxl6CJS7k2nGcXo8XiexOcn4LPKEPKv9gF4qGOlXaoYB3iWmbjOpiFZejB4EKM8frZwSOVYj97o6L1PIddi47th_oVyOeD4rmJH4lOI0tC0VdIwshAFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛
🎬
CapCut Web؛ ادیت ویدیو با هوش مصنوعی
اگر تولید محتوا می‌کنید یا برای شبکه‌های اجتماعی ویدیو می‌سازید،
CapCut Web
یکی از کامل‌ترین ابزارهای آنلاین برای تدوین سریع و حرفه‌ای است.
با قابلیت‌های هوش مصنوعی این پلتفرم می‌توانید:
•
🪄
حذف خودکار پس‌زمینه و نویز صدا
•
📝
ساخت زیرنویس خودکار (حتی برای فارسی)
•
✂️
تبدیل ویدیوهای طولانی به کلیپ‌های کوتاه مناسب ریلز و شورتز
•
🎨
استفاده از افکت‌ها، قالب‌ها و ابزارهای هوشمند ادیت
🔗
سایت:
https://www.capcut.com
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6820" target="_blank">📅 18:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6819">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🌐
دانلود کامل هر وب‌سایت با Website Downloader
اگر می‌خواهید یک وب‌سایت را برای استفاده آفلاین یا بررسی کدهای آن دانلود کنید(فرانت اند)،
Website Downloader
ابزار مناسبی است.
✨
قابلیت‌ها: •
📥
دانلود کامل
HTML، CSS، JavaScript، تصاویر و فونت‌ها
•
🔗
بازنویسی لینک‌ها برای اجرای آفلاین •
📦
خروجی به‌صورت فایل ZIP •
⚡
متن‌باز با لایسنس MIT
این ابزار برای
کلون کردن سایت‌ها، تهیه نسخه آفلاین و یادگیری ساختار پروژه‌های وب
بسیار کاربردی است.
🔗
GitHub
:
https://github.com/AhmadIbrahiim/Website-downloader
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6819" target="_blank">📅 17:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6818">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b961c32eaa.mp4?token=iic00yb8I3yjg_Q0DrGeJl7Ew_qOjywdeZ0ZDvuk9cvRRgOLVQM14OVft-u5YWks1Fw3kv2bbzxbDl74YU3XUSDrC7lK4TRRMZAkDBGYCuYNcW3iMGDcI2ZgBMDuo7yNXQu1y-L8b3AH0ChDFICaLA9zqGXVUVmyZCc42HujmWsNVAqQcLKbd11fHEDHJIDoFvuAnOHciSdX2ipRlR9_vDTwbQY5G3_EqfLXgsza2RgTngtsQ7Zxql62GamHN_3PcCEhxP0vVJpaMg6vX1hbpsO0GRLzpUIwVL073ye26trDC9NttNZcayjXBBDQVi28PY2hbnnQZnpfp5UkTC4TOlYmKF666TWPNynfgaKF5mllS2GSCSXlgI4H7UvWvBM9Vc8D2KvB5BHBRMNpl55ItpVRAAMV1xarbXvTXls3ZerZymmpu19cR6mEFlh5oBy2WamImiQ39HDM4CTSaEsWY6OQegNUdzzG6qsfJJ1nq7OkslYVg7WH6hEvZb6HhbsxI4re9q21gEWwUORAYmcXXiIh5DDTdSllz_2Ztm9UVmAOvknxG0DFRLjkJ1CP4OaJZYe5QF5e6pRJQDuqF3EkU1FGpFH-M99nPupQ0vfMD9771dPC0HBbBjQe05YERnSOT6PYG-auD6aA9HoJkyq_jSEJ2L-B0j3njmxUkpYudqY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b961c32eaa.mp4?token=iic00yb8I3yjg_Q0DrGeJl7Ew_qOjywdeZ0ZDvuk9cvRRgOLVQM14OVft-u5YWks1Fw3kv2bbzxbDl74YU3XUSDrC7lK4TRRMZAkDBGYCuYNcW3iMGDcI2ZgBMDuo7yNXQu1y-L8b3AH0ChDFICaLA9zqGXVUVmyZCc42HujmWsNVAqQcLKbd11fHEDHJIDoFvuAnOHciSdX2ipRlR9_vDTwbQY5G3_EqfLXgsza2RgTngtsQ7Zxql62GamHN_3PcCEhxP0vVJpaMg6vX1hbpsO0GRLzpUIwVL073ye26trDC9NttNZcayjXBBDQVi28PY2hbnnQZnpfp5UkTC4TOlYmKF666TWPNynfgaKF5mllS2GSCSXlgI4H7UvWvBM9Vc8D2KvB5BHBRMNpl55ItpVRAAMV1xarbXvTXls3ZerZymmpu19cR6mEFlh5oBy2WamImiQ39HDM4CTSaEsWY6OQegNUdzzG6qsfJJ1nq7OkslYVg7WH6hEvZb6HhbsxI4re9q21gEWwUORAYmcXXiIh5DDTdSllz_2Ztm9UVmAOvknxG0DFRLjkJ1CP4OaJZYe5QF5e6pRJQDuqF3EkU1FGpFH-M99nPupQ0vfMD9771dPC0HBbBjQe05YERnSOT6PYG-auD6aA9HoJkyq_jSEJ2L-B0j3njmxUkpYudqY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🌎
نقشه آینده زمین برای زندگی!
‏این پروژه خیلی جالب و مهمه! یه نقشه تعاملی به نام ‌Farmland Atlas⁩ ساخته شده که پیش‌بینی می‌کنه مناطق مختلف زمین چقدر برای زندگی مناسب خواهند بود تا سال ‌2100⁩.
🤔
‏این پلتفرم با تحلیل بیش از ‌5⁩ میلیون نقطه، چندین سناریو رو بررسی می‌کنه، از خوش‌بینانه تا بدبینانه. برای هر مکان، پیش‌بینی آب و هوا، ارزیابی کیفیت منابع آب، وضعیت خاک و خطرات اجتماعی رو هم در نظر می‌گیره.
🌟
🔗
https://farmlandatlas.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6818" target="_blank">📅 14:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6817">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">📊
معرفی ابزار CodexBar
اگر از
Claude Code، OpenAI Codex، Cursor، Gemini، OpenRouter، GitHub Copilot
یا سایر ابزارهای AI استفاده می‌کنید، احتمالاً بارها با محدودیت استفاده یا تمام شدن سهمیه مواجه شده‌اید.
؛
CodexBar
یک ابزار متن‌باز برای macOS است که تمام این اطلاعات را مستقیماً در نوار منو نمایش می‌دهد تا همیشه بدانید چقدر از سهمیه‌تان باقی مانده است.
ویژگی‌ها:
• نمایش میزان استفاده و سهمیه باقی‌مانده
• نمایش زمان دقیق ریست شدن محدودیت‌ها
• پشتیبانی از Claude، Codex، Cursor، Gemini، OpenRouter، GitHub Copilot، Groq، Deepgram، MiniMax،
z.ai
و ده‌ها سرویس دیگر
• نمایش هزینه، اعتبار و میزان مصرف API در سرویس‌های پشتیبانی‌شده
• نمایش وضعیت آنلاین سرویس‌ها و اختلالات احتمالی
• حالت تجمیعی برای مدیریت چندین سرویس از یک پنل
• بدون ذخیره رمز عبور؛ از نشست‌ها و لاگین‌های موجود شما استفاده می‌کند.
🔗
GitHub:
https://github.com/steipete/CodexBar
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6817" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6816">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚀
چند ابزار متن‌باز و رایگان برای برنامه‌نویس‌ها و سازنده‌ها:
🎨
Text Effects
افکت‌های جذاب CSS برای طراحی متن و رابط وب.
📧
SESPulse
داشبورد متن‌باز برای مدیریت و بررسی ایمیل‌های Amazon SES.
🔎
API Finder
مخزن APIهای عمومی برای پیدا کردن سرویس‌های آماده.
🛡
Tirreno
فریم‌ورک امنیتی متن‌باز برای شناسایی رفتارهای مشکوک کاربران.
💻
OpenTUI
کتابخانه ساخت رابط‌های کاربری زیبا در ترمینال.
✨
ابزارهای کوچک، کاربردهای بزرگ برای ساخت سریع‌تر پروژه‌ها.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6816" target="_blank">📅 13:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6815">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کانفیگ اهدایی
🔥
vless://ac7e7b41-0dc0-4bec-a285-3266ecbb87c8@ps.aramvpn.kdns.fr:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=QFc4pPuYwGfyKeoSWnxUkPgaDdEPCPPb2ImpxI-njxI&security=reality&sid=0586e9d2d3a6d12d&sni=www.yahoo.com&type=tcp#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6815" target="_blank">📅 13:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6814">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">📸
ساخت عکس پرسنلی ۳×۴ با هوش مصنوعی
اگر یک عکس معمولی از خودتان دارید، می‌توانید با پرامپت زیر آن را به یک
عکس پرسنلی رسمی
تبدیل کنید.
✨
ویژگی‌ها:
✅
پس‌زمینه سفید یا خاکستری ساده
✅
نورپردازی طبیعی و یکنواخت
✅
حذف اشیای اضافی و اکسسوری‌ها
✅
افزایش کیفیت و وضوح تصویر
✅
مناسب برای عکس پرسنلی و پاسپورت
📝
Prompt:
Convert this photo into a professional ID/passport photo.
- Neutral plain background (light gray or white, evenly lit, no texture).
- Centered face and shoulders visible, crop from top of head to chest.
- Natural skin tone, balanced lighting, no shadows.
- Neutral facial expression (slight smile allowed).
- Professional look, no accessories (remove hats, sunglasses, background objects).
- Enhance sharpness and clarity.
- High resolution, suitable for official use.
💡
برای بهترین نتیجه، یک عکس با نور مناسب و کیفیت خوب به مدل بدهید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6814" target="_blank">📅 11:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6813">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">📄
olmOCR | تبدیل هوشمند PDF به Markdown با هوش مصنوعی
یک ابزار متن‌باز برای تبدیل فایل‌های PDF، PNG و JPEG به متن و Markdown تمیز با حفظ ساختار اسناد؛ مناسب برای مقالات، کتاب‌ها و فایل‌های اسکن‌شده.
🚀
⚡
ویژگی‌ها:
📝
تبدیل PDF و تصاویر به Markdown خوانا
📊
پشتیبانی از جدول‌ها، فرمول‌ها، دست‌خط و قالب‌بندی‌های پیچیده
🧹
حذف خودکار هدر و فوتر صفحات
📚
حفظ ترتیب طبیعی متن حتی در اسناد چندستونه و دارای شکل
⚡
دقت بالا با پشتیبانی از پردازش محلی یا سرورهای vLLM
🔓
متن‌باز با لایسنس Apache 2.0
🔗
https://github.com/allenai/olmocr
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6813" target="_blank">📅 10:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6812">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">؛
🛠️
OfficeCLI؛ هوش مصنوعی برای Word، Excel و PowerPoint
؛
OfficeCLI
یک ابزار متن‌باز جدید است که به دستیارهای هوش مصنوعی امکان کار مستقیم با فایل‌های
Word، Excel و PowerPoint
را می‌دهد.
✨
قابلیت‌ها: •
📄
ساخت و ویرایش اسناد Word •
📊
ایجاد و تحلیل فایل‌های Excel •
📽️
ساخت و ویرایش ارائه‌های PowerPoint •
✅
بررسی و اصلاح خودکار خروجی‌ها
نکته جالب اینکه
بدون نیاز به نصب Microsoft Office
کار می‌کند و از محیط‌هایی مثل
Claude Code، Cursor و Codex
نیز پشتیبانی می‌کند.
🔗
GitHub:
https://github.com/iOfficeAI/OfficeCLI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6812" target="_blank">📅 09:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6809">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dae562e36c.mp4?token=uxsFU750fKc-FYRy85ywpdUZS5WCxE2CvlbpnSOV30jFPQIrqsenZHj8wzVMym29b2Yt8ACkD6TmsHI3v5FzXgaLg0eXwhRvOqTfmFaB-kNemuvXbk_1ZzyAuLezYtX1Hvxej8fzqcUCfCyqNFDDdK3EOJi6kfNVzfE82YQIlDw2SOyBjR3Co4vo3YDyKWyQSVFWwHm32-bzIDi7ZZA8lPinEl0A0hTB3BR75howL_E2LGgIjQ16Np98srHua9QRYldu56vfkgneW5-sQGwYqkcF1gLy_kbqQawgeNx_l7yYIg-pPyIv_302x7mv7_vu6PQKNCJFKX7hXwSiAGuRzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dae562e36c.mp4?token=uxsFU750fKc-FYRy85ywpdUZS5WCxE2CvlbpnSOV30jFPQIrqsenZHj8wzVMym29b2Yt8ACkD6TmsHI3v5FzXgaLg0eXwhRvOqTfmFaB-kNemuvXbk_1ZzyAuLezYtX1Hvxej8fzqcUCfCyqNFDDdK3EOJi6kfNVzfE82YQIlDw2SOyBjR3Co4vo3YDyKWyQSVFWwHm32-bzIDi7ZZA8lPinEl0A0hTB3BR75howL_E2LGgIjQ16Np98srHua9QRYldu56vfkgneW5-sQGwYqkcF1gLy_kbqQawgeNx_l7yYIg-pPyIv_302x7mv7_vu6PQKNCJFKX7hXwSiAGuRzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">؛‌OpenAI⁩ مدل جدید ‌GPT-Live-1⁩ رو معرفی کرده که مکالمات صوتی با هوش مصنوعی رو به سطح جدیدی می‌بره!
🎙️
‏این مدل میتونه تغییر لحن بده، بخنده و حتی وقتی که کاربر ناگهان حرفش رو قطع می‌کنه، طبیعی‌تر واکنش نشون بده
🗣️
‏و اما یه قابلیت خیلی جالب دیگه: میتونه به صورت آنی به حرف‌های کاربر واکنش نشون بده و حتی به عنوان مترجم همزمان کار کنه!
🌎
‏همین حالا از طریق ‌
ChatGPT Voice⁩
قابل دسترسه!
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6809" target="_blank">📅 08:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6808">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🎯
RankGrow | دستیار هوش مصنوعی برای سئو
ابزاری هوشمند که با اتصال به Google Search Console، مشکلات سئوی سایت را شناسایی کرده و لیستی از مهم‌ترین کارهایی که باید انجام دهید را ارائه می‌دهد.
🚀
⚡
ویژگی‌ها:
📊
اتصال مستقیم به Google Search Console
🤖
۷ دستیار تخصصی هوش مصنوعی برای سئو
📝
پیشنهاد بهبود محتوا، لینک‌سازی و سئوی فنی
🎯
لیست اولویت‌بندی‌شده از کارهای ضروری SEO
📈
تحلیل رقبا و کشف فرصت‌های رشد
🎁
۵ اعتبار رایگان برای شروع (بدون نیاز به کارت بانکی)
🔗
https://rankgrow.com
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6808" target="_blank">📅 07:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6807">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کد نویسی رایگان با ابزار هوش مصنوعی FREEBUFF
💻
ابتدا به
سایت
بروید و اکانت بسازید سپس ابزار را اجرا کنید
🚀
— نصب آسان با دستور npm install -g freebuff
🛠️
— بدون نیاز به کلید، کارت یا اشتراک ماهانه
🆓
— مدل‌های پیشرفته از جمله DeepSeek V4 pro و Mimo 2.5 pro و Minimax M3
🧠
— دارای یک وب سایت برای تولید و استقرار برنامه‌ها به صورت رایگان
🌐
کد نویسی خود را با هوش مصنوعی و به صورت رایگان انجام دهید!
✨
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6807" target="_blank">📅 04:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6806">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🎉
Claude Opus 4.8 رایگان در
Supercode (فقط یک روز)
به مناسبت لانچ Supercode در Product Hunt، این ابزار دسترسی رایگان یک‌روزه به مدل Claude Opus 4.8 را برای همه کاربران فراهم کرده است.
🚀
⚡
جزئیات:
🆓
دسترسی رایگان به Claude Opus 4.8 برای یک روز
🤖
استفاده از AI Agent در ترمینال
💻
مناسب برای کدنویسی، توسعه و مدیریت پروژه‌ها
📈
؛Supercode
تاکنون به بیش از ۹,۵۰۰ دانلود، ۸۲ ستاره GitHub و ۲۲۰ کاربر رسیده است.
اگر قصد دارید Supercode را امتحان کنید، امروز بهترین فرصت است.
🔗
https://supercode.sh
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6806" target="_blank">📅 02:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSlipNet</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SlipNet-v2.5.5-full-release-arm64-v8a.apk</div>
  <div class="tg-doc-extra">25.7 MB</div>
</div>
<a href="https://t.me/ArchiveTell/6798" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🕊
@SlipNet_app</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6798" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6797">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اقا سرعتی slipnet رو اپدیت کنید
😁
😁</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6797" target="_blank">📅 00:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6796">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🎬
FreeCut | تدوین ویدیو با هوش مصنوعی
یک ابزار متن‌باز که با کمک مدل‌های هوش مصنوعی، ویدیوهای خام را به‌صورت خودکار تدوین می‌کند؛ بدون نیاز به API پولی.
🚀
⚡
ویژگی‌ها:
✂️
حذف مکث‌ها، تپق‌ها و بخش‌های اضافی
🎨
اصلاح رنگ خودکار و افزودن زیرنویس
🎥
ساخت انیمیشن و افکت‌های تصویری
🧠
پشتیبانی از Whisper محلی (بدون API Key)
💻
سازگار با Claude Code، Codex و سایر AI Agentها
🔗
https://github.com/Moh4696/freecut
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6796" target="_blank">📅 23:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6795">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">https://www.youtube.com/@localhost_ir</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6795" target="_blank">📅 23:03 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
