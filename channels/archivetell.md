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
<img src="https://cdn4.telesco.pe/file/l6CZm4Ux9hx7PQIFTr-k2AyYKQ-vbWgpfswCUHUKmBymnYgbgpefuSvmRuLLFqED-BcxU94hZMGqNn8kUyV48Cu_k0nKlV-MjvU_P4DCmr4_8ZAJ7GIuKNlzVuO6vwuoFsxZr5wM5On1JKV4iVD6fEMH3YzsvD0AJN8JmZytsgI3r9uNTetJ3CDMC0oGGVMXOYV48oW_xWWRsMTFW0zXQPY8xlhmdWiMj3fnLvFbp_vP1I6GqP41jMqlbKH47tvUNWWiplfQh0Yr1rsap6E8lnXKUYe0hCaeYA06P9lGZ8CP-BfuoBQLf4JcLx_k-d3n--it_Ui3lJQIgA_HgV9wPQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 09:00:17</div>
<hr>

<div class="tg-post" id="msg-7752">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⌨️
؛ DeepSeek V4.1 Flash، Muse Spark 1.3 و GLM-5.3 Flash به صورت رایگان در Cline Desktop
​تیم Cline یک برنامه دسکتاپ جداگانه با تمام قابلیت‌های یک عامل مستقل را راه‌اندازی کرده است.
​
📌
امکانات برنامه:
🤔
استفاده از ClinePass یا کلیدهای API شخصی
🤔
انتقال یکپارچه وظایف از Codex، Claude Code و سایر عوامل
🤔
برنامه‌ریز برای اجرای پس‌زمینه عامل
🤔
مدیریت سرورهای MCP، پلاگین‌ها و مهارت‌ها
🤔
مرورگر وب داخلی و ورودی صوتی
​
📌
مدل‌های رایگان موجود:
🤔
DeepSeek V4.1 Flash
🤔
Muse Spark 1.3
🤔
GLM-5.3 Flash
​
📌
نحوه شروع کار:
1⃣
دانلود برنامه:
https://cline.bot/desktop
2⃣
نصب و اجرای Cline Desktop
3⃣
ورود از طریق حساب Cline یا اتصال کلید API خود
4⃣
باز کردن پوشه کاری پروژه
5⃣
انتخاب یکی از مدل‌های رایگان از لیست
6⃣
ایجاد یک جلسه و اختصاص وظیفه به عامل
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 768 · <a href="https://t.me/ArchiveTell/7752" target="_blank">📅 01:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7751">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmwsB4sPTx9EVC7Naz7jsgLoO08T4YBgL1pZ2OUpsGHRnlnjFFkeuR6nE5mYxS0z3jdw1nGqfDybw6bW9uunG6aKasConmMErIaZ1m6ekpQuH3CNxNw6lcD9vBZe4meiNtEuH_h5CAl9vTTma21yxZJ-Q8f4LHRYJb6N-gCCQo8d4Py8jeBMLC2n-Tx-MeUYWQjhR8she2EF34I6JfyIyxM1C7Xg-9WtWETsOcs6-TCVfoLW8eFYDtb5DU_0v6vH_j5paIqq00KLEx-CiPV1VVIoCP6Zwm2IfepsVQ-vYRwdNYDak_FJTx0WCG_HalBRH_rOPSHsWvtqlo7Kez8lzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
؛ LIGHTVELA - یک هوش مصنوعی رایگان که 24 ساعته در دسترس است.
4500 اعتبار و 100 میلیون توکن
مزایای طرح رایگان:
🤖
1 هوش مصنوعی
💳
4500 اعتبار در ماه
🖥
2 پردازنده مجازی + 4 گیگابایت رم (محیط تست)
💾
50 گیگابایت فضای ذخیره‌سازی
🌐
دسترسی 24 ساعته
📱
ادغام با تلگرام و سایر پلتفرم‌ها
نحوه دریافت:
به
lightvela.ai
مراجعه کنید.
یک حساب کاربری ایجاد کنید.
از آن استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/ArchiveTell/7751" target="_blank">📅 22:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7750">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کانفیگ مخصوص چنل -
سرعت خداا
vless://e4b11ac9-46f7-4cc0-92ed-bb9dfaaf3600@94.237.92.65:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=lkMM9FR-o7Z6NwmmQVK8rLhCQR1mbJTgjY_0upeS2SY&security=reality&sid=0436301fb0178b&sni=google.com&spx=%2F442987454d44398&type=tcp#@ArchiveTell
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7750" target="_blank">📅 11:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7748">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BAUjytIBLEg27Olf4-Nkjr-cJXuA4fQunPGLAn-YrHjb_tUiEpSSd2eoiI-iYJ8K67aghglTmaagc8GtMCXMG7yqMEDUMWPBYvdvRvz4dlHvZ_K1I6EzUga9EIDa4jWZeJVliE8K46uhJqjy4l4EroSpEGHeshb1BJCaTd2cImwmMSPULDsSxY5aDRmAUdH03Q9hGD5FreomOCQcV58UDekRqSwoQq5IUvyzB4aiOC0N6p6wxWEh9zeKv_m3vzDmeGFOxGpjf4PZzQgYVba6_ytl1_GgTDO0CTNwmFLyEOU-z7WNxHLMh4LWiHffFD4RnAtEqvJvjKpzJC87Gmf4Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
از تاریخ ۱۴ تا ۱۶ سپتامبر، با ورود به
Z.ai
؛ ۶۰۰ میلیون توکن GLM-5.3 به شما تعلق می‌گیرد، بدون نیاز به اشتراک.
🔗
https://autoclaw.z.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7748" target="_blank">📅 18:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7747">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ZqwunYsRmE7pDltaTy_cum0zywF-CVjTyGJ3AofPCHe-zN6xyhXlI43CnF8Jiu5XfLRbRZqMn129BoYVmi6R5EWlzSWubiI48EQy7apUEj95H3UJwetKgyAciwyxPvJWVveaOstMjNNZmwlsyZmCy1oYwaeGvbQQgBX4Pn8p_-zpPCnjmNNBF1CqvYzp9dqxkQ1mQDJFvGcyW-FnnAaST8eRXiQBA7piuaPAyAlCA0VxXNu1qVeG4qDyeS0iB_O_5h7CdyIQKwGWZU5xVlHLWa8bwKspyiKG3X-0xV6Q0lwuWtVBjicisEqTpLRSL6yVeRqPdgbEZjrf5cNtAz363g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔓
رفع فوری خطای ریجن و تحریم Antigravity
اگر موقع کار با هوش مصنوعی Antigravity گوگل با خطای تحریم ریجن یا گیر کردن روی Eligibility Check روبرو شدید، ابزار متن‌باز
Open AG Patcher
در چند ثانیه این مشکل رو حل می‌کنه:
▫️
رفع محدودیت ریجن:
بدون نیاز به دستکاری یا تغییر کشور اکانت گوگل
▫️
پشتیبانی کامل:
از Antigravity 2 و Antigravity IDE و ترمینال (CLI)
▫️
امن و خودکار:
اجرای پچ با یک کلیک + بکاپ خودکار برای بازگشت به حالت اول
💡
نحوه استفاده:
ابزار رو اجرا کنید و شماره نسخه مورد نظرتون رو بزنید تا پچ در چند ثانیه اعمال بشه (سازگار با ویندوز، مک و لینوکس).
🌐
دریافت ابزار از گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7747" target="_blank">📅 16:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7746">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaBFy_6aYmzZJzneZmEDXORfymB3R-6CUF9-ZsgOWXv_2bSv87xcNuQ4wR34jhq6SY3fpxLdOikp5zNJyeSMvD1I_LWpsRgCx8FhWO6_Do2ED6w99PP8uM1pxO9G9fxmLuI5L5cHB06j_jftPRa-zRQa7YD9iDbFXHGsLzsWQZaMsl_uV8a_5MiD1AZz977y43PfOnXB3uGmhRqcb4Uhflb5UlkbdyBXU2AyzYXG10xN4IKORM9gHVerOQfoR6P7dFS-EgaPkbcFqHrOuiaVkp_Jt6Uh5hEk-AOf595yVnr_X4t78M2uqFxBbP2mN8wnW9rZNQ_P_bmYm1WZYXVN9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نحوه استفاده از Claude Opus 5 و GPT 5.6 Sol
به صورت رایگان
📣
حساب‌های جدید در
Verdent.com
، یک دوره آزمایشی 7 روزه با 100 اعتبار رایگان دریافت می‌کنند
💯
🆓
🎉
✍️
آنچه دریافت می‌کنید:
👀
🔍
☑️
Claude Opus 5 / Sonnet 5
✅
GPT-5.6
☑️
Gemini 3.1 Pro
✅
GLM-5.2
☑️
Kimi K3
📌
نحوه دریافت:
🔥
⚡️
☑️
به
➡️
🔗
https://verdent.ai/
مراجعه کنید.
✔️
برنامه دسکتاپ یا افزونه VS Code را نصب کنید.
☑️
یک حساب کاربری جدید ایجاد کنید
✉️
✅
مدل مورد نظر خود را انتخاب کنید.
☑️
از اعتبارها برای شروع استفاده کنید
🚀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7746" target="_blank">📅 11:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7744">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔥
KiraAI
روزانه ۵۰ میلیون توکن رایگان
🤖
مدل‌های موجود قابل استفاده :
⚡️
kira-3.5-pro
⚡️
kira-3.5-flash
⚡️
kira-3.0-image
🔗
kiraai.vn
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7744" target="_blank">📅 23:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7743">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔎
scite.ai
— موتور جست‌وجوی استنادی برای تحقیق جدی
۷ روز اشتراک رایگان (تریال رسمی سایت)
📑
Smart Citations
نشان می‌دهد هر مقاله توسط مقالات دیگر تأیید شده، رد شده یا فقط اشاره شده — نه فقط تعداد استناد
🧠
Assistant
پرسش پژوهشی‌ات را می‌پرسی و پاسخ با استناد واقعی و لینک به منبع می‌دهد، نه حدس
🤖
دسترسی به مدل‌های تحقیقاتی:
Claude Sonnet 5 | Claude Opus 4.6 | GPT 5.2
🎛
Personalized Feed
فیلتر و شخصی‌سازی حوزهٔ تحقیق ، فقط موضوعات مرتبط با کارت را ببین
🔗
Custom Dashboards
داشبورد اختصاصی برای کلیدواژه، نویسنده یا ژورنال خاص + هشدار مقالهٔ جدید
📊
Analyses & Topic Classification
دسته‌بندی موضوعی، شناسایی روندها و گپ‌های پژوهشی
آموزش فعالسازی
🔗
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7743" target="_blank">📅 22:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7742">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBBaJanCbFvTXwn0BwnhltxIAuejvH5b7BeuqOuffY0UbAKtnWj378i_NbQfwLDZOp2rrLXo_7QGWxwJePm0t_ZQoCbs48QOXAdj2Brk_hyueK0Vj4SP2Ra7XwANfQ4geEBgEh-AHDjrEUGfufhe6M2OMoWCbn6c9I4VG8FdXd54BTwXPBH9mpAQhhTtvfvLD595Um6Ig1flhODRop56pCYrR-XRv88wSSozFaIa6ONhosDM05bfynfMTVLL8LTYDEBdDp29XSxTJErAajvbJxxtNiAu2VrIBVTcJiCv7AKLtToOuZVyWsRXooZ0h81JqD9pO8l8fMPupX4Dy80xjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی به Seedance 2.5 و سایر مدل های تولید ویدیو، عکس و اتوماسیون
آموزش
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7742" target="_blank">📅 22:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7741">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">keys.txt</div>
  <div class="tg-doc-extra">2.7 KB</div>
</div>
<a href="https://t.me/ArchiveTell/7741" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎁
دریافت 20,000,000 توکن رایگان  claude-fable-5 | claude-sonnet-5 |  deepseek-v4-pro | muse-spark-1.2
✅
وارد ربات زیر بشید و api key رو دریافت کنید  @kiro86bot
💡
سازگار با همه سرویس‌های OpenAI-Compatible
🌐
base url: https://api.xpiki.com/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7741" target="_blank">📅 22:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7740">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sz-5TWDl1u1bBo8DjDtnvzJh57BsEH6mrey_xkuY8pcFzqQHZ92DrZFWEPYP__i0bwW70T9qEqno8si72LdA1L6RatEwxRW8PWbw8oLYBVPj0FXMXGfaC87AbDMjuTDAGQB9dn1gE_2lNTW1C2fOhUHB5iTK2T3xkbUBNBFTnx3RcGn_RBVXPEVwHraY5GoGOnKlCzKyM_PnfXltv9lMYYQBXMQ_CBc_W7hXUo5JHFEo1_F6JIRXM2lPmvUiK-48QibcucanGDLqmayHnt2AeVUmkWVGQaEYtktW0iFW-c0ayWLjrlKArHyJ-nXZ57JrfeCYhUCuJrcL7cAnyyP4eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎁
دامنه رایگان همیشگی بدون کارت اعتباری!
‏بچه‌ها این
پروژه گیت‌هاب
با نزدیک ۲۰۰ هزار استار، دامنه‌های رایگان دائمی میده که واسه پروژه‌های تستی و سایدپراجکت‌ها کاملاً خوراکتونه.
🚀
‏•
دامنه‌های متنوع:
پسوندهایی مثل
.us.kg
و
.qzz.io
بدون هزینه فعال می‌شن
‏•
کنترل کامل:
دسترسی کامل به
Custom Nameservers
و تنظیمات
Cloudflare
دارید
‏
💬
نحوه استفاده:
کافیه برید به سایت پروژه، اکانت بسازید، دامنه دلخواهتون رو ثبت کنید و نیم‌سِروِرهای کلادفلر رو ست کنید.
‏
🔗
سایت پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7740" target="_blank">📅 18:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7739">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⌨️
ترجمه سریع و هوشمند، بدون دردسر!
اگه دنبال یک مترجم ساده و کاربردی هستید که فقط به یک سرویس محدود نباشه، پروژه Translator می‌تونه انتخاب خوبی باشه. این پروژه با پشتیبانی از سرویس‌ها و مدل‌های مختلف ترجمه، امکان ترجمه متن، استفاده از قابلیت‌های صوتی و مدیریت تاریخچه ترجمه‌ها رو در یک محیط مدرن و ساده فراهم می‌کنه.
🤖
قابلیت چت با هوش مصنوعی؛
با استفاده از API Key با مدل‌های هوش مصنوعی گفتگو کنید و پاسخ‌های هوشمند دریافت کنید.
🔑
همچنین امکان استفاده از API Key و ترجمه با سرویس‌های هوش مصنوعی مختلف رو داره.
🌐
نسخه آنلاین:
https://codewave4.github.io/Translator/
🔗
سورس پروژه:
https://github.com/codewave4/Translator
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7739" target="_blank">📅 18:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7738">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087627b2c4.mp4?token=mv7X7sF7G6I_u6ekerOYEoCYlaqnEr9RSYjkQoPbt5IL_z7QxXILA84OFliMjP7qBiSjYc0Zxg_mYm51nQn6W3DlZVznqvL9BVS8WsREgCJQAuMrFT731egJgxG1u0K0GoEapMFB-977-sLwMInIsiv-pXdfvDNnctxYrO9svhOaQeba8WZt9rH2HWa9TsyLm81CNgG9I1_MrxtnROXwVQloqfawn4L_ymxKtNhTgfmwbmKgiSYALJ0irw4P01Obd-0HYGnIjvSJ11GalceHmhze_zMyEKJ5WYyPDGswDnOXecbTTu5mIZeK6LNYGxlEYMSt9a5OG7szo_cWCnkx_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087627b2c4.mp4?token=mv7X7sF7G6I_u6ekerOYEoCYlaqnEr9RSYjkQoPbt5IL_z7QxXILA84OFliMjP7qBiSjYc0Zxg_mYm51nQn6W3DlZVznqvL9BVS8WsREgCJQAuMrFT731egJgxG1u0K0GoEapMFB-977-sLwMInIsiv-pXdfvDNnctxYrO9svhOaQeba8WZt9rH2HWa9TsyLm81CNgG9I1_MrxtnROXwVQloqfawn4L_ymxKtNhTgfmwbmKgiSYALJ0irw4P01Obd-0HYGnIjvSJ11GalceHmhze_zMyEKJ5WYyPDGswDnOXecbTTu5mIZeK6LNYGxlEYMSt9a5OG7szo_cWCnkx_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🎬
ساخت موشن‌گرافیک حرفه‌ای با یه پرامپت!
‏این ابزار هوش مصنوعی کل فرآیند ساخت تیزر تبلیغاتی، از استوری‌بورد تا تدوین صدا و انیمیشن رو خودش انجام میده و خروجی رو با بیت موزیک سینک می‌کنه. خوراک بچه‌هاییه‌ که سریع میخوان خروجی باکیفیت بگیرن.
🔥
‏
⚡️
دسترسی به منابع غنی:
۱۵۷ مدل سناریو، ۲۱۴ استایل بصری و کلی الگوریتم انیمیشن آماده
‏
⚡️
شروع سریع:
کلی تمپلیت آماده‌به‌کار داره که کار رو برای پروژه‌های فوری جلو میندازه
‏
⚡️
عملکرد هوشمند:
کافیه ایده‌تون رو متنی بدید تا در لحظه ویدیو تحویل بده
😎
برای دانلود ابزار تولید ویدیو
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7738" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7737">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">1.7B token MINIMAX
url:
api.minimax.io/v1
key:
sk-cp-k8fnOYl1xeWGiSNy7qWxNP3Gu-nkuMKLaAFl7ZoCnGiqA2sabKF30eMTQNurXcyGtgGdbM168WEvBhyTOo2WQaE9RoXzVPAyyG3CYwZuybXzDILyBEBc5nk
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7737" target="_blank">📅 14:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7736">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6agoWhm-yfF8kKuBFHia72PO3Ynfkj39qTMp-xi3-yngr866CWjfkoOTVxyQINnjmWIOrPMeNkeDUL8IRSuSGf8qXKRg3rfzir0iZvggEBGhwql7KzKCnPXmDDlBXsXgXarYDtOAeEU6H1k-YS_9has0iDjmg2QpVyl5KHFu-F5zYVqbV1s4RdR0y8Zjw2m9XEa4ckV-8LojeFwBrk0rAG1PNsDXctmHh4PPP6AcN-Izv6ZN2pHpq3WVofQl4_UNK9DQvc-aRl3XIcMgut2S-W6jIdswl_EEbqiV59s6v1OhE8Ky1x07Ntm8pIfnCa2iWmRO85XoTlzvKTvr8TbSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
مرجع خفن اسکیل‌های ‌Claude Code⁩ و ‌Codex⁩!
‏سایت ‌SkillsMP⁩ یه کاتالوگ تر و تمیز با بیش از ۳۳ هزار اسکیل آماده‌ست که تو کار با هوش مصنوعی کلی جلوتون میندازه.
🤖
‏•
دسته‌بندی جامع:
از برنامه‌نویسی و ماشین‌لرنینگ تا امنیت و کار با ‌API⁩
🔍
‏•
دسترسی سریع:
لینک مستقیم به گیت‌هاب برای هر اسکیل
📂
‏•
کیفیت‌سنجی:
دارای ایندیکاتورهای کیفیت برای انتخاب بهترین ابزارها
⚡️
‏خوراک بچه‌های وایبکودره که بخوان پرقدرت‌تر پروژه‌ها رو ببرن جلو.
🚀
🔗
skillsmp.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7736" target="_blank">📅 14:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7735">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🛡
دیگه ایمیل و پسورد اصلیت رو به هیچ سایتی نده!
حتماً براتون پیش اومده که برای ثبت‌نام در یک سایت مجبور شدید ایمیلتون رو بدید، اما بعد از یه مدت صندوق ایمیلتون پر از پیام‌های تبلیغاتی مزاحم شده یا اون سایت هک شده و رمزهاتون لو رفته!
ابزار جالب
AliasVault
دقیقاً برای حل همین مشکل ساخته شده:
💎
این ابزار براتون چیکار می‌کنه؟
⚡️
ساخت بی‌نهایت ایمیل دائمی:
برخلاف ایمیل‌های موقت که بعد از ۱۰ دقیقه می‌پرن، این ایمیل‌ها
کاملاً دائمی و همیشگی
هستن و برای هر اکانت می‌تونید هر تعداد ایمیل دلخواه که خواستید بسازید!
⚡️
دریافت کد ثبت‌نام داخل خود برنامه:
نیازی نیست برید یه ایمیل دیگه باز کنید؛ ایمیل‌های تایید و کدهای ورود مستقیماً داخل همین برنامه براتون میاد!
⚡️
مچ‌گیری از سایت‌های متخلف:
اگر یه سایت ایمیل شما رو به تبلیغاتچی‌ها بفروشه، دقیقاً می‌فهمید کار کی بوده چون برای هر جا یک ایمیل اختصاصی ساختید.
⚡️
نصب روی گوشی و کامپیوتر:
هم اپلیکیشن برای موبایل داره و هم افزونه برای مرورگر، و خودش پسوردها رو سر جای درست پر می‌کنه.
💬
چرا این ابزار فوق‌العاده‌ست؟
•
ایمیل‌ها هرگز منقضی نمی‌شن:
هر زمان در آینده بخواید وارد سایت بشید یا رمزتون رو بازیابی کنید، پیام‌ها باز هم به همین ایمیل دائمی میاد.
•
سقف تعداد ندارید:
برای ۱۰۰ تا سایت هم می‌تونید ۱۰۰ تا ایمیل مستعار و رمز مجزا بسازید.
•
کاملاً رایگان و امن:
بدون هیچ هزینه‌ای، امنیت و آرامش صندوق ایمیلتون رو تضمین می‌کنه.
🌐
ورود به وب‌سایت AliasVault
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7735" target="_blank">📅 12:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7734">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrupLcIL_HOIcRPcoGXxHw54sjUyIpxDRrMx-LAEj5IfPVuFchZdDOBVvyglEU34MZAKQrdgcrMeK4e3-7R274FrtZw8dFeOqj3OAFTEYo4-7qz_8gR0SRuQfCI92BbVyydr6qClMVp5ZS8ylQ5oK3BArV1QmXzWY8stZa9ll1OUlQVxavTvytxsf2nMnqo2-1jkbn29gOzHFrKyP_37yP6qorr9A5ZC5YFnYVO-7JqKsa8HssRm7_L3qG_umudEkc0eNSiU8qOX6r8Ci2lH7Lljcw6gsGd8N0JIM8t-VAJFUq6HLZsTYoUJfe4ZzqYyndhqDt1qyy9BeCCL4lN2uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک سایت، ده‌ها مدل و ابزار با اعتبار رایگان روزانه
🎁
💬
Multi AI Chat
GPT، Claude، Gemini، DeepSeek، Grok، Qwen ، Llama
همه در یک چت، با امکان مقایسه جواب‌ها
🎨
تولید و ادیت عکس
تولید تصویر از متن (Flux، Stable Diffusion، Ideogram…)
حذف/تغییر پس‌زمینه، حذف اشیاء و متن از عکس
Face Swap، Upscaler، تبدیل اسکچ به تصویر
ویرایش عکس با دستور متنی + تولید تصویر سه‌بعدی
🎬
ویدیو
تولید ویدیو از متن و از عکس
Face Swap روی ویدیو
خلاصه‌سازی، زیرنویس و ترجمه ویدیوهای یوتیوب
🎵
صوت و موسیقی
ساخت آهنگ (Suno، MusicGen…)، Text-to-Speech با صداهای طبیعی
شبیه‌سازی صدا (Voice Clone)، تبدیل ویس به متن، حذف نویز
✍️
نوشتن و تولید محتوا
تولید محتوا، بازنویسی، خلاصه‌سازی، ترجمه، گرامر
تحقیق کلمه کلیدی و تشخیص محتوای AI
🌐
لینک سایت :
app.1min.ai
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7734" target="_blank">📅 12:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7733">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🎁
دریافت 20,000,000 توکن رایگان
claude-fable-5 | claude-sonnet-5 |
deepseek-v4-pro | muse-spark-1.2
✅
وارد ربات زیر بشید و api key رو دریافت کنید
@kiro86bot
💡
سازگار با همه سرویس‌های OpenAI-Compatible
🌐
base url:
https://api.xpiki.com/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7733" target="_blank">📅 11:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7732">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🆓
هوش مصنوعی رایگان  — بدون ثبت‌نام
Kimi K2.6 | GPT 5 mini | DeepSeek V3.2
📌
امکانات:
⚡️
چت هوش مصنوعی نامحدود
⚡️
تولید متن و محتوا
⚡️
بدون ایمیل، بدون رمز عبور، بدون کارت بانکی
📌
نحوه استفاده:
🔗
وارد
این سایت
بشید مدل موردنظر را انتخاب کنید و شروع کنید.
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7732" target="_blank">📅 23:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7731">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QipGrfPOEZnXSn_UsOu-ZozO9sBJxuJBe-wHN9vaOGzaGCW0Rpi8-X79ahPeivxxzJrlziHG2eVJdxf0j0MaOOE6_BbMhg-OzDcvMSXLkhKkl5dKyL8hoaTQPzT6tcIj_sx-h_v1DJK_B-GcT0s6i2Zlbz6-PAPPxSmyDUN3P6-ZLqUnw2RrOC3fp4Fle0TRS15JrT_eILpaTtPNNaRd4DLzlBVOmAftAPAh4pUFoIeczVBqg2SWLPJTT2AprGGQOYvUrrjWGNx3Y91CPdn6QZqBOdLtuZ0c6bam5kFr3RwQ4lf1OpK4IdDZtuOOWsXeJIf_yeDtPVWw0LlgKyOPdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
۵۰۰ مگابایت پروکسی رزیدنتیال رایگان (
proxyma1.io
)
یک سرویس پروکسی رزیدنتیال که با ثبت‌نام از طریق تلگرام ۵۰۰ مگابایت ترافیک رایگان می‌دهد و API هم دارد.
📌
نحوه دریافت:
1️⃣
وارد سایت
proxyma1.io
شوید و ثبت‌نام کنید
2️⃣
پس از ثبت‌نام، یک پیام برای استارت ربات تلگرام نمایش داده می‌شود که داخل آن یک کد هدیه قرار دارد
3️⃣
ربات را استارت بزنید و کد را برای ربات ارسال کنید
4️⃣
۵۰۰ مگابایت به حسابتان اضافه می‌شود
🚀
📌
ویژگی‌ها:
☑️
پروکسی رزیدنتیال (Residential)
☑️
۵۰۰ مگابایت ترافیک رایگان
☑️
پشتیبانی از API
☑️
ثبت‌نام آسان با تلگرام
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7731" target="_blank">📅 23:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7730">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqb8iiPqZlCKg0Sm2qzp0s40mP3axXouLs_3aWXVDl2cXG34ZCRxilG8Jbwr5PiLYXixpgEu-_OyNzRHc0JliLa1jbV6sbtp5U5SRCG6vMT_0flfQ34s6n8EQrl9fWEcnYxbFDJVvVmHJobR87S4yeVnxwclUWwSmsAby6tUXxb63zhQfXV8dEpYmtwrJEr6LKzT5fyV_PxzvNOT9OsnAtJp8f5z6Ppu_BXi9LHPt6v4EZGe1dprSs-JBMMgoqIbhOQ8ou6EGjdCZ5ePt_IT2kH_bvix_8rGuBaaq10GVw_gj4EAv0VkYSuyBAHxKiqYoYmNsXO2XR9x9cQnRmhAkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
۵۰۰۰ اعتبار رایگان برای مدل‌های برتر هوش مصنوعی
پلتفرم جدید در شروع کار ۵۰۰۰ اعتبار به شما هدیه می‌دهد تا با قدرتمندترین شبکه‌های عصبی کار کنید: تولید متن، عکس و ویدیو در یک جا.
📌
امکانات در دسترس:
☑️
چت چندمدلی
☑️
تولید تصویر
☑️
تولید ویدیو
☑️
موجودی اولیه: ۵۰۰۰ اعتبار رایگان
🪙
📌
روش دریافت:
1️⃣
ورود به
getunikey.ai
2️⃣
ثبت‌نام یک حساب کاربری جدید
3️⃣
ایجاد کلید API در تنظیمات پنل
4️⃣
استفاده در رابط چت یا ابزار های واسط
base url:
https://getunikey.ai/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7730" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7729">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔍
Hidden File Hunter — شکارچی فایل‌های مخفی ویندوز
دنبال فایل‌های مخفی و سیستمی توی ویندوز می‌گردی ولی پیدا کردنشون واقعاً دردسره؟ این ابزار دقیقاً برای همین ساخته شده
👇
؛ Hidden File Hunter یک برنامهٔ دسکتاپ ویندوزیه که تمام فایل‌های مخفی و سیستمی درایوهات رو پیدا می‌کنه و توی یه جدول مرتب و قابل مرور نشونت میده.
✨
امکانات:
✔️
پیدا کردن تمام فایل‌های مخفی و سیستمی در همهٔ درایوها
✔️
نمایش نتایج در یک جدول مرتب و خوانا
✔️
خروجی گرفتن از فهرست کامل مسیرها در قالب فایل TXT
✔️
کپی کردن خود فایل‌ها با حفظ ساختار پوشه‌ها در مقصد دلخواهت
✔️
فقط می‌خونه و کپی می‌کنه — هیچ فایلی رو تغییر نمیده، حذف نمی‌کنه و بهش دست نمی‌زنه
✔️
ساخته‌شده با Python و PySide6
✔️
تم تیره و روشن
✔️
رابط دوزبانهٔ فارسی و انگلیسی
یه ابزار ساده، سریع و امن برای وقتی که می‌خوای بدونی توی سیستمت چه چیزهایی از چشم‌ها پنهان مونده.
🔗
لینک گیت‌هاب:
github
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7729" target="_blank">📅 22:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7727">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚀
اپلیکیشن Bifrost (بایفراست)؛ پل ارتباطی فوق‌سبک تلگرام بر بستر ورکر کلادفلر منتشر شد.
بایفراست یک بریج لوکال (Local SOCKS5) مدرن و بهینه برای اندروید است که ترافیک تلگرام رسمی را از طریق پروتکل TWP به ورکر رایگان کلادفلر متصل می‌کند؛ با پینگ پایین، بدون قطعی و با سرعت دانلود فوق‌العاده بالا.
🔒
بدون نیاز به VPN، بدون روت و با مصرف باتری نزدیک به صفر:
این پروژه کاملاً متن‌باز (Open-Source) است و برخلاف فیلترشکن‌ها از VpnService استفاده نمی‌کند (هیچ علامت کلیدی بالای صفحه نمایش داده نمی‌شود و اینترنت سایر برنامه‌ها کاملاً دست‌نخورده و بدون تغییر باقی می‌ماند). مصرف پردازنده در زمان عدم استفاده دقیقاً ۰.۰٪ است و امنیت و رمزنگاری پیش‌فرض تلگرام (MTProto) نیز کاملاً حفظ می‌شود.
📥
دانلود و نصب برنامه (از گیت‌هاب):
https://github.com/Qorvhex/Bifrost/releases
⚡️
کانفیگ تستی برای شروع (بعد از نصب، کپی کنید و داخل برنامه Paste کنید):
twp://telp.qorvhe-x.workers.dev?clean_ip=1music.cc#Bifrost-Test
🛠
سورس‌کد اسکریپت ورکر (TWP):
https://github.com/Qorvhex/TWP
📁
لینک پروژه و سورس‌کد در گیت‌هاب:
https://github.com/Qorvhex/Bifrost
لطفاً تستش کنید و سرعت و عملکردش رو بهم بگید!
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7727" target="_blank">📅 21:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7726">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🖥
مرورگر ضد ردیابی Private Browser Pro؛ هویت جعلی و دور زدن بن شدن اکانت‌ها!
​بچه‌ها اگه نیاز دارید روی یک سایت چند اکانت مجزا بسازید بدون اینکه سیستم‌های امنیتی بفهمن همه‌شون مال یک نفره، یا می‌خواید ردپای دیجیتالی‌تون رو کامل مخفی کنید، این مرورگر اوپن‌سورس ویندوزی دقیقاً همون چیزیه که دنبالشید. این ابزار بر پایه نسخه فوق‌امن Ungoogled Chromium و Electron ساخته شده و از زبان فارسی هم پشتیبانی می‌کنه.
​
🎭
جعل مشخصات سیستم (فینگرپرینت):
شبیه‌سازی کارت‌های گرافیک قدرتمند (مثل RTX 4090، سری RX 7900 و تراشه‌های اپل)، اضافه کردن نویز به Canvas و AudioContext و هماهنگ‌سازی هدرها برای عبور آسان از سد کپچاهای Cloudflare Turnstile، hCaptcha و reCAPTCHA
​
📁
مدیریت و تفکیک کامل پروفایل‌ها:
امکان ساخت محیط‌های دائمی (Persistent) برای ذخیره دیتای هر اکانت در پوشه جداگانه، یا حالت موقت و یک‌بارمصرف (Ephemeral) که با بستن پنجره کل ردپا پاک میشه + دکمه پاک‌سازی آنی
​
✅
پروکسی پیشرفته و ضد نشت اطلاعات:
پشتیبانی از پروکسی‌های SOCKS5 و HTTP (با یوزرنیم و پسورد)، حل آدرس‌ها از داخل پروکسی جهت جلوگیری از DNS Leak و غیرفعال‌سازی WebRTC برای مخفی ماندن کامل IP واقعی
​
✨
محیط کاربری تمیز و دو زبانه:
کرومیوم دست‌نخورده بدون واترمارک‌های تستی، تم دارک با کلیدهای میانبر سریع و پشتیبانی کامل از منوی فارسی و انگلیسی
​
💡
بهترین سناریوی استفاده:
ایده‌آل برای مدیریت چند اکانت در شبکه‌های اجتماعی و پلتفرم‌های حساس، تست وب، ریسرچ‌های OSINT و حفظ حریم خصوصی بدون نیاز به خرید اشتراک‌های گران‌قیمت مرورگرهای ضد ردیابی.
​
🔗
گیت‌هاب
​
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7726" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7725">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">📥
تبدیل فایل‌های تلگرام به لینک مستقیم نیم‌بها با ربات Leecher!
بچه‌ها اگه کندی دانلود از تلگرام یا قطعی فیلترشکن موقع دریافت فایل‌های حجیم کلافتون کرده، یا می‌خواید تورنت و ویدیوهای یوتیوب رو مستقیم به فایل تلگرامی تبدیل کنید، این ربات لیچر ایرانی حسابی به کارتون میاد.
🇮🇷
لینک مستقیم با ترافیک نیم‌بها:
تبدیل آنی فایل‌های تلگرام به لینک دانلود پرسرعت تحت وب (سازگار با دانلود منیجرها) با محاسبه مصرف اینترنت به‌صورت نیم‌بها
🌐
دانلودر همه‌کاره (لینک به فایل):
پشتیبانی از دانلود مستقیم لینک‌های یوتیوب، اینستاگرام، وب‌سایت‌ها و حتی فایل‌های تورنت و تحویل فایل داخل چت
☁️
اتصال ابری به گوگل درایو:
امکان لینک کردن اکانت شخصی Google Drive برای ذخیره و آپلود مستقیم فایل‌ها در فضای ابری بدون مصرف حجم گوشی
🎁
شارژ رایگان روزانه:
۱ گیگابایت حجم رایگان در هر ۲۴ ساعت بدون نیاز به پرداخت هزینه یا خرید اشتراک
💡
نکته کاربردی:
لینک‌های ایجادشده بین ۶ تا ۸ ساعت معتبر هستند؛ کافیه فایل رو به ربات بفرستید، لینک مستقیم سرور ایران رو داخل IDM کپی کنید و با حداکثر پهنای باند خط‌تون دانلود کنید.
🔗
استارت ربات
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7725" target="_blank">📅 20:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7723">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AReojpR8Y66GCM_42iMthsRBVicKE4MMSY-j1-JMx6jkoKXTVao7XEKSUecizwy8Z33-q7web7K_OXh9ned-TrGaXBqWatcIZOu32QjmCxp_A5llNYU2pg6TQ6r_4s3lUADQENAUfhvOSzky5Yywxcl0_c2EB62yy1WMmx0rn8RqCGGHKIIeDIGkK-gKTIl1mOong62ityZrIYGfLZuIUwKfk69zerdIKESFPKE2dRuG1-wYfhCfWVSltWO6H99zFdxqFHk3eEQHAUdENSdBpsFj6GmXXz6eEt03V9jyVECo9Pcn4fTL8szMBFLumYwv3WZLFg3S9KFcxbDqHXdJlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید (1.8.0) برنامه MSN-GUARD منتشر شد :
💢
BOOM
💢
تغییرات :
1- اضافه شدن متد اختصاصی SHARD برای اولین بار
-_-_-_-_-_-_-_-
2- دسترس‌پذیری کامل و پشتیبانی 100% از صفحه‌خوان TalkBack برای عزیزان نابینا و کم‌بینا برای اولین بار
-_-_-_-_-_-_-_-
3- آپدیت هسته
-_-_-_-_-_-_-_-
4- اضافه کردن قابلیت Backup و Restore و Reset Factory از تنظیمات برنامه
-_-_-_-_-_-_-_-
5- برطرف شدن مشکل دکمه Reconnect در نوتیفیکیشن
-_-_-_-_-_-_-_-
6- اضافه شدن Theme کاملا روشن برای استفاده زیر آفتاب
-_-_-_-_-_-_-_-
7- برطرف شدن باگ اتصال خودکار پس از قطعی اینترنت و چند باگ دیگر
-_-_-_-_-_-_-_-
6 روش دسترسی به اینترنت آزاد:
1: متد Masque
2- متد Wireguard
3- متد Warp On Warp
4- متد Psiphon (اختصاصی و اولین)
💯
5- متد Tor (اختصاصی و اولین)
💯
6- متد SHARD (اختصاصی و اولین)
💯
💻
ریپازیتوری گیت‌هاب (متن‌باز):
https://github.com/mbm110/MSN-GUARD
📌
لینک مستقیم دانلود :
برای گوشی های 64 بیت
برای گوشی های  32 بیت
برای تمامی گوشی ها
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7723" target="_blank">📅 18:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7722">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✉️
؛ Turbo Mail ایمیل موقت، سریع و بدون دردسر
اگه برای ثبت‌نام یا دریافت کد تأیید به یه ایمیل موقت نیاز دارید، Turbo Mail یه گزینه ساده و سریع برای شماست.
⚡️
ساخت فوری ایمیل موقت
👌
بدون نیاز به لاگین و ثبت‌نام
⏳
اعتبار ۲۴ ساعته
🔒
مناسب برای دریافت ایمیل و کدهای تأیید
🚀
ساده، سریع و بدون مراحل اضافی
کافیه وارد سایت بشید، ایمیل موقتتون رو بسازید و استفاده کنید.
🔗
https://mail.turbocenter.shop
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7722" target="_blank">📅 18:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7721">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🎧
دستیار هوشمند و همه‌کاره موزیک‌بازها؛ دانلود با کیفیت FLAC با ربات MelodyAddict!
بچه‌ها اگه عشق موسیقی هستید و از دانلود تک‌به‌تک آهنگ‌ها، افت کیفیت یا پیدا نکردن موزیک پس‌زمینه کلیپ‌ها کلافه شدید، این ربات فوق‌العاده با پشتیبانی کامل از زبان فارسی دقیقاً خوراکتونه. همه‌چیز از شزم اختصاصی گرفته تا رصد خودکار پلی‌لیست‌ها رو براتون یکجا جمع کرده.
🔄
سینک خودکار پلی‌لیست‌ها:
زیر نظر گرفتن لایک‌ها و پلی‌لیست‌های Spotify، SoundCloud، YouTube Music و Apple Music و ارسال خودکار ترک‌های جدید با امکان زمان‌بندی ارسال (۳ ساعته، روزانه یا هفتگی با دستور /digest)
🔍
شناسایی جادویی آهنگ:
پیدا کردن نام و فایل موزیک فقط با فرستادن یک وویس کوتاه، زمزمه، فایل ویدیویی یا لینک ریلز اینستاگرام، تیک‌تاک، یوتیوب و توییتر
💎
کیفیت استودیویی FLAC و Lossless:
قابلیت تنظیم کیفیت پیش‌فرض خروجی برای گوش دادن به بالاترین بیت‌ریت ممکن، با سرعت عالی و کاملاً بدون تبلیغات
📂
مدیریت پلی‌لیست‌های ابری:
امکان دسته‌بندی، ساخت و اشتراک‌گذاری مستقیم پلی‌لیست‌های شخصی داخل تلگرام
💡
نحوه استفاده:
ربات رو استارت کنید، زبون رو روی فارسی بذارید و برای شروع کافیه وویس یک آهنگ یا لینک پلی‌لیست موردعلاقتون از اسپاتیفای یا ساندکلاد رو براش بفرستید تا بقیه کارها رو خودش اتوماتیک انجام بده.
🔗
استارت ربات هوشمند
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7721" target="_blank">📅 16:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7720">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jSCBZFcPbnhPFqaprZSpGbQwdHPypFJvbK0IdPOQvACSuQdTEdOdBRlCohTd9iqdZU7bNaGI1Vh3UQqC1yuSEccbst89q1R5YSW9KT4qwwrD1eHMiycKLAB8zCjPDTWF1QlyM6-WKo-gHa0ixXbPD0fR9o80Ad6mgdSMCFKeaPQxZpjhI3Kx5KT6HdR7w13bSSxffOmi3IDwmiRHwFxhdIgbFJPsWSB1o_S7na2RFJcXnED013TPXRqxj468PVHbkhM-3bwghtjPP3azcnNjVmzof61Y9rag9yEYZgUQ0oYP6ZzbcDTAFXsas8xYuASwtDiHmY4sHQQZAI5LRJCOQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید ArasClient منتشر شد!
نسخه جدید با اضافه شدن بخش Free منتشر شد و از این به بعد این بخش به‌صورت مرتب آپدیت میشه.
📱
؛ ArasClient یک کلاینت سبک و کاربردی برای مدیریت و استفاده از کانفیگ‌هاست که تمرکزش روی سرعت، سادگی و اتصال راحت‌تره.
🆕
اضافه شدن بخش Free
⚡️
آپدیت منظم کانفیگ‌ها
📊
تست و مرتب‌سازی هوشمند سرورها
🔄
انتخاب سریع‌تر سرورهای مناسب
📦
پشتیبانی از نسخه‌های مختلف اندروید
🔗
دانلود نسخه جدید:
https://github.com/ArasTey/ArasClient/releases/download/v1.6.8/ArasClient_1.6.8_arm64-v8a.apk
🔗
سورس پروژه:
https://github.com/ArasTey/ArasClient
💬
نظر، انتقاد یا پیشنهادتون رو کامنت کنید.
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7720" target="_blank">📅 15:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7718">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xpn_nL4F2_JnZ7sO9wegojn8M0WuIRjEO0FSOkb5OJ-RKtBFAmpKZKoAVf5tQdNLmhiB4_wkbn6bAeFFCcQhCs6sR_kjQHbzaXa5XUiE0jxNM9lwtCsQaRB5v5l85wjIin9VnxGm966SH1uxCRswgx8GzFoebh615JiKJVQqtYVGHpgmKfBIEG3sXVX7_WYQH0T7u4gjjRSpySZy359GikfrIqteT-r4TZ4XAQPfMcW0wV2AXzS8o1fpfBKn10n-7fuYth1ynAKNUEl7AgYBPAL0H7Foh4JeZ-aEL6T8l-J_wz-WSJULqdhlyav7JXu0ITH9LIMbGNSDGO4Ycx3BHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
اگر می‌خوای شبکه‌های کامپیوتری رو از پایه تا سطح حرفه‌ای یاد بگیری، نت‌داد دقیقاً برای تو ساخته شده.
از مفاهیم بنیادی مثل آدرس‌دهی IP، سوییچینگ، مسیریابی و امنیت گرفته تا شبکه‌های مدرن، همه چیز با پروژه‌های عملی و مثال‌های کاربردی آموزش داده می‌شه.
✔️
۱۰۰٪ پروژه‌محور
✔️
۵۳ درس تخصصی
✔️
۱۴ بخش آموزشی
شروع یادگیری از اینجا:
🔗
https://netdad.vercel.app
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7718" target="_blank">📅 15:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7717">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVid4Z_z_9b88pCZXchKsL_1Zg-PGN3zQj_q5oxlYnCRdnoCz7sMx0AyybBy7wwRapwqMlmK_F9LWbL8dfXfBWDTINs83J_ndmIlNQ_BE1OZS6L7ae17z4sfbcw6II_2U_EopHPxxiIvQwKbsEzFTxdlCejQAq-K4Jq_mDQ_mtL_GpAV8o23BCcJNQjoSVa6isUnphhqurLQTaDqFfn9O1L0w4g6ZxU8of-YplwShTOEZ_lDccafo0bZNszkDvSrU8B2kWapmp21UgPRUM3tCD6rfCM1tSvjlfwW2J4e5iD9qyYas_cH8N8qvU0HP49LVlYcnowCZbMJ7z0wTukwqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
100 میلیون توکن GLM-5.3-Flash با ثبت نام در AutoClaw + ZAI
از تاریخ 14 تا 16 سپتامبر (دوشنبه تا چهارشنبه) 600 میلیون توکن GLM-5.3 و DeepSeek 4.1 بدون نیاز به کارت و همچنین یک کد تخفیف ارائه خواهد شد.
این پیشنهاد در
اینجا
قابل دسترسی است (در حال حاضر شامل ۱۰۰ میلیون توکن می‌شود)
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7717" target="_blank">📅 14:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7716">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lxq92TKefXJ3dkrQo0TWTIZ4tyevvRbt2Oh_ESFw4CqGdLFAgxVaw7l9neIPb3slWLdNzGsmjPrQO4tMXw8WcoVi27XRzV1cSxL3iQ5bKX1GckZbDrWu4OlQB174BLZ1owSuv2F7rVaycfYGiOzb6vYHkIn92YdFAWTo7nKc0MY2s6IpK3DLtD1V6eZI6DGoYt3caoPkiBG37_bcuwnTPDCZLOrL771tb3ltE6ECIPHWUGVPHslnrN7OyY9s6uRlOwLv6kKovX0RQM2VkN87SOBwsWeZwQLFUCszYZJJkcK_8oPKdMBUeu-OK4B0v64FzHRDhxv6GULJKPIJbuzkpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥁
کیبورد لپ‌تاپت رو به یه درامز حرفه‌ای تبدیل کن
پروژه خفن KeyBeat یه استودیوی درامز تحت وب هست که بدون نیاز به هیچ نصبی، مرورگرت رو به یه ساز واقعی تبدیل می‌کنه
🔥
یه پروژه اوپن‌سورس عالی برای برنامه‌نویس‌ها، آهنگسازها و عشقِ موزیکا
🔗
لینک سورس کد و اجرای مستقیم:
https://github.com/faithsaly5-stack/Keybeat
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7716" target="_blank">📅 12:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7715">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H63BBJOjm1GPu-KAhh6C3ZzQ4wmJxSqRJ09S1O2YRuZ_l61xc7Wdxh-33rtYP_pxDUmTIEMjSpOQlCxKmfegTuF9dSIwhF8_gR-mpOJmt3MlN5Hjo8AmvnZGePVKKt-evYngD52n7b5f--iMyO2LqDNyzZE_ow7jWLQc3JI7Qb4mBC1i5pUQozKCRb8m2a74jSXuEFUf4JDLGvYzckabZPaKpF7e5wkhjHGkS1jVi-jSZS1oXBViaxe31EMIYYN2L85V6qto7EQjV1pzk1SnMjyqmY3s83ZfiMEuc6AFNKuMKDH0HoQ0LUbn1qVp1GPGkBGOG4qB82sVbtMriu8l_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
دریافت آیپی رزیندنتال رایگان
💎
با گوگلتون سایت زیر بشید و روی claim offer کلیک کنید.
بعدش برید بخش proxy generator و پرش کنید و بزنین براتون 300 مگ آیپی رزیدنتال میده
🆓
http://rainproxy.io
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7715" target="_blank">📅 10:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7712">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKFCJcBcFjfgfi2yb57p7FGSSXjB-a9eWkzO30sYguUDSAsi3O2KecGWseSep-xawdU-5DnyRuN08QFV5l4RuZJDupIKu3x3YaJ2z1BB8kD3f92eSffNNocT3lhP3BpfUX1_NWxOMVz9CXWXz65cAqUSX7nmf8-Uov-Rem_OI2B-V5rr1eto6DydVhNM31qpV9Ut22qcrGhRI18_RNQm-dReUtqxJKzAET88GTXMtU-9FplOfQdsNXjnjF6vHrQbIN3oP0cCCEwMoeqiPP-L6UvD1-I_9xK3Gwypf9QT33TpRSuKztmq8_OXnlzdCbhal0aSQ2e2KilrGLypoYvrcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
15 دلار اعتبار رایگان برای دسترسی به بهترین مدل‌های هوش مصنوعی
استفاده از مرورگر به شما 15 دلار اعتبار می‌دهد تا مدل‌هایی مانند موارد زیر را امتحان کنید:
• GPT-6 Astra
• DeepSeek V4.1 Flash
• GPT-5.6 Luna
• Claude Opus 5
• Grok 4.5
برای دریافت:
🔗
browser-use.com
با استفاده از حساب گوگل خود ثبت نام کنید و شروع به استفاده کنید.
برای دریافت اعتبار بیشتر، از چندین حساب استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7712" target="_blank">📅 21:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7711">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🧰
جعبه‌ابزار همه‌کاره و فوق‌سریع تلگرام؛ معرفی آپدیت بزرگ بات Amir Tools!
بچه‌ها اگه کلافه شدید از اینکه برای هر کار کوچیک (هوش مصنوعی، استعلام قیمت ارز، دانلود یوتیوب و تبدیل فایل) یک ربات جداگانه استارت کنید، این بات همه‌کاره دقیقاً خوراکتونه. در آپدیت جدیدش کلی ابزار مدرن با رابط شیشه‌ای اضافه شده تا از ده‌ها بات متفرقه بی‌نیاز بشید.
🧠
هوش مصنوعی با حافظه اختصاصی:
مکالمه پیوسته بدون فراموشی کانتکست چت، سوئیچ خودکار روی مدل‌های پشتیبان و امکان ریست سشن
📥
فایل به لینک مستقیم و دانلودر یوتیوب:
تبدیل آنی انواع فایل، ویدیو، آهنگ و ویس به لینک مستقیم پرسرعت + دانلود مدیا از یوتیوب با بالاترین کیفیت
📈
نرخ لحظه‌ای و چارت زنده بازار:
استعلام آنی قیمت دلار، تتر و ارزهای دیجیتال (BTC, ETH, TON و...) همراه با نمودار اختصاصی و باکس High & Low
🤫
پیام ناشناس امن و دوطرفه:
ساخت لینک اختصاصی با آیدی تصادفی برای دریافت متن، ویس و عکس ناشناس با قابلیت پاسخ‌گویی مستقیم
🎁
سیستم قرعه‌کشی خودکار کانال:
ساخت مسابقات و چالش‌های گروهی با دکمه شیشه‌ای و قرعه‌کشی کاملاً خودکار و عادلانه بین اعضا
🛠
میکروابزارهای روزمره:
ساخت بارکد تصویری (QR Code)، پسوردساز غیرقابل‌نفوذ، مبدل ارز به تومان، هواشناسی و مینی‌گیم‌های کوئیز
💡
نحوه استفاده:
وارد ربات بشید، دکمه شیشه‌ای منو رو لمس کنید و بدون نیاز به رجیستر یا مراحل طولانی، به تمامی ابزارها به‌صورت یکپارچه و رایگان دسترسی پیدا کنید.
🔗
استارت ربات هوشمند
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7711" target="_blank">📅 20:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7710">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است.…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7710" target="_blank">📅 19:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7708">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل: ① به https://arena.ai/ مراجعه کنید. ② حالت Direct Mode را انتخاب کنید. ③ در لیست مدل‌ها، GPT-Image-2.5 Sunburst را پیدا کنید. ④ به مدت 72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود.
✈️
…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7708" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7707">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت گیت‌هاب قدیمی داشته باشید و از طریق این لینک وارد شید
✅
🎁
با هر رفرال شما 100 دلار و شخص دریافت کننده…</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7707" target="_blank">📅 12:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7706">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOHFcWEUtBoZ-82W0z3wgr5H8L6v62vTujex1ySSZtPaO3nn7khQpXAU95zZE4LaZ7TH_-se8Of0SdYG8aQi0DA3eNpFYUKbzARNTax3E2fZLmO0mhQq2q2KPa-Je-p3E_YZv5Cc-SW_S9cfY7eIbgLsn1rUszMA8TX65C4mJlrxkTv-4Zb0-13WBa1N7Rh4KWRczex_popyxiZaeg4d67tlKQHmEHpd3ZImLn0wB81FqE8Sbt-LWPzvgCrfvIj7QTTp0t1yefdVux60GFn-FST0t4vjlm5hjpfngTod7vjrCzDP_njATMXn8E33m_bLIXMMmxQVTv_l5B-lS-Rq5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل:
① به
https://arena.ai/
مراجعه کنید.
② حالت
Direct Mode
را انتخاب کنید.
③ در لیست مدل‌ها،
GPT-Image-2.5 Sunburst
را پیدا کنید.
④ به مدت
72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود
.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7706" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7705">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqDZ5ahLH-a_hOBXSQHgzidkSByD933U_QtSGlNSKhfWq5imQmLRB1nTH9BeiyO-td5t63TxXQXC6as0lf-fe0qQ-xGUhkKiIpW_jff8Oht8-LJpgv6m7R8Sia0jRsen54TcNWQ4bPvqgPhuPd2mGF-hNfS3q1QsP0lvL9MtapBgKGSXrzuPXW59qwJ5NYFLIWjfqvlniSBSRJx3d-XykD0k5G_oSqet_MftXTNRuc0xQSuQueKRJK0fLj9MMhst0K4Fhiqm191lQmFA0ABcLUn4nYq4sV2LaTGm4DIg4hw7RGFQnQcbVyTogbjdgKWNmlK6WPq9nZdjUeZ9dGqYwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4.1 Flash به صورت رایگان
💥
🆓
این نسخه ۲ روز پیش منتشر شده است. دارای ۱ میلیون توکن متن، قابلیت‌های بصری پیشرفته و کیفیت مناسب برای استفاده در سیستم‌های هوشمند است.
🚀
🔺
رایگان به صورت روزانه
🔺
پنجره متن با ظرفیت ۱ میلیون توکن
🔺
سهم استفاده روزانه هر روز ریست می‌شود.
هنوز مشخص نیست که این سرویس چه مدت به صورت رایگان باقی خواهد ماند.
‼️
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7705" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7704">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdeQf8dpdyDxXD0foJ2UrI8mG21Zc_zdHH-OvmYYW92D_iIynhU9UvPgI1VWFITlv6KiWs00KyfRqYxwx0ndfXz0OQ9k52n6vKKPjzxDuF8gnLisbNo0Vso9E-ilFXvobCC5CYQYYQfyQLb7alIuhT8qGKnMupUrJmZl5is8UwbSxA_UlefPQo5_IR92D_61YfnpBDc-E--vcF3u4NCMYwkACQ754k6JZh79krU5O42t7cDwiYYvXVtlcZM74JVxHYfWSnfGsHME-shL9YxNd5_PVYWEM4eXo1n42yEWwcY_-1Ih0s09NZrGC-K1s0HUY08_JczDqdyG82xKeZtIQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
با این سایت میتونید 5 دلار اعتبار رایگان برای بهترین مدل ها دریافت کنید همچنین این سایت 3 مدل کاملا رایگان بهتون میده
💵
😎
Kimi K3 | Deepseek 4 Flash | Mimo 2.5
✅
📌
Base URL: https://tokenharbor.ai/v1  با جیمیل…</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7704" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7702">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7eTvHReeRTV4RdfnFYxriXZ0os096ekp3wHXTFi11KpHQUDBLmVfdLYwp2mUra9wta7j4RQBQn0Fe9BlAuXSoNJNJZK7NLL2-lqMXBY-4-UWnD4y5IDUTdsY9z3Rf1g2sYS4zrgunvdqjzHvs1r9c3JCF61nZp0xJzCkt656_LrfeGaV8CzS9OPcJ3NSPkkf-zbH2hziZg-tmbh0S56TJSZrLcac_XhtFKF54t1mrxZLiGNwAGEQfvr8Gofl_l7s0YbPUkIRmjAkgW7k9vPMOcYsnmxC2jePUXc3jQrqWm8pmUjdHbkzgYMl5yL_O396nyFx7mwo24ibQtLwswHuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GPT-6 Astra
1 Day Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=gpt-6-astra-medium
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyq0X3MbdY_YJM-QQv1u1pMi4BIKRVIW9IgS6ROxVHRuYkYBwp-OETLbphnFz77Lqih__rPt50G4Oi3bkB85WzjSKHWXucZjJXf_SUhcFS41ItIsYgjzRgcF7SwlFP-Oc0ME-AqXP3VtSGn6pt1a9hK5U_jjowAigHoXn86eVuZO_Kwfk_Ti0ufkpBQW_zQWvN4-ch5COrQb5I961PajvNWfKyIr2g2ofhriYJDELgtMG-DyZca8N3jjbTUFaWfjBICIEeUmc9nYMjbBvmlN7ZUVOswsAGm0AjeTS0mKkOyhuA5b6Cb7ljcdeteOJCQJ1Oj6_1FqhSeqQC0d_-hNNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">150 میلیون توکن رایگان برای مدل های زیر
💥
🆓
GLM 5.3 Flash | Qwen 3.8 Flash | Mimo 2.5 | GLM 5.3 | Hy 3 | Qwen3.8 27b
✅
وارد سایت زیر بشید با جیمیل ثبت نام کنید سپس از طریق منو 50 میلیون توکن امروز هم دریافت کنید
✅
‼️
نکته :
از مدل های با پسوند Free استفاده کنید و احتمالا این دسترسی شامل محدودیت تعداد ریکوئست در دقیقه باشه ، همچنین ممکن هست هر لحظه اشتراک رایگان بپره
📌
Base URL :
https://kiraai.vn/api/v1
🔗
لینک ثبت نام
🔗
لینک گرفتن کلید
🔗
لینک دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7700">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🧠
پروژه OXYGPT — یه ربات تلگرامی که هوش مصنوعی رو حسابی جدی گرفته!
بچه‌ها این صرفاً یه ربات چت نیست، یه اکوسیستم کامل AI روی تلگرامه: چند مدل هوش مصنوعی، مربی‌های حرفه‌ای تریدینگ، sandbox واقعی لینوکس، اخبار فارکس زنده و داشبورد مدیریتی. خوراک کسایی که می‌خوان یه بات production-grade بسازن نه یه دمو دو ساعته
🔥
↔
مسیریابی چند-مدلی AI
: استخر کلید Gemini + سرویس‌های سازگار با OpenAI، round-robin می‌چرخن و روی خطای 429/503 خودشون فالبک می‌زنن
🪟
پنجره‌های مکالمه مجزا
: هر کاربر تا ۵ چت جدا با تاریخچه و state خودش می‌تونه باز نگه‌داره
🧙‍♂️
مربی‌های تریدینگ (Persona)
: چهار شخصیت آماده (ICT، Quarterly Theory، Matrix/369، Price Action) با یه دستور سریع صدا زده می‌شن
📓
ژورنال معاملات
: ثبت و پیگیری ترید‌ها با قالب‌های اختصاصی، مستقیم داخل تلگرام
📰
اخبار فارکس زنده
: رویدادهای پرتأثیر Forex Factory رو با تحلیل کوتاه AI نشون میده
🖥️
قابلیت Sandbox واقعی لینوکس (E2B)
: مدل می‌تونه کد اجرا کنه، پکیج نصب کنه، ریپو کلون کنه و فایل بفرسته/بگیره
🔑
قابلیت BYOK
: کلید API خودتو وصل کن، از محدودیت پیام و quota عمومی بی‌نیاز شو
👁
مانیتورینگ کانال با AI
: کانال‌های تلگرام رو زیر نظر می‌گیره و پست‌های مهم رو تحلیل و تحویل میده
💡
دیپلوی با یه دستور روی Docker/Railway انجام میشه، و هر ۵ ساعت یه بک‌آپ خودکار از کل دیتابیس‌ها زیپ و برات تو تلگرام ارسال میشه — دیگه نگران از دست رفتن دیتا نباش.
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snrNxbeImXSRmG_YcmK3i6k34bk6VweOdQTSHrFfAf0YhR4YcZeHhOa3McPWvuLexVmNY9ilKW4Jw9HOYW_1ueWTh7lTk1ub9T1crxinHjaJtzdV1dhVHrZR4I_HatRttrBtQkTQWAxmNmsZqqspmZnAro0B689xJ8ezpTTyZBmTimtqAHjkJtCjMnrfpaA_vBUey9hMjmhbg1sSSBDMZidbDknX4ajO-KbpQmaYCRqCtLhXvaVaJlLv55KxvToqcWo6MZBIp_lXLy2rzR_gFZBD7VMDPZFiOycQyJnIzQUJS04mNzyH0Fn7FjlYtIP6nItR1iSRrCTkf1OzE-C55A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTMIgWV3WgrzOuvaLnYzH7u8dgByM37CqudEhurrGC9cbK64M2G6C2SB6Rqqp0lKeF21CpA9h-axd4SerYvcE1MPlYghDRd8nkJpd_S5zlfTYQE7Nj1pKVNgHCk_OCE2tHnEY2dxpgu1puITcMKQsrJEkhTpT9DROlnVLz-Sjf7ldNQucKEUbrUokkW7saO2cHnZD26465uObrNbjF4CqyggpkjrCwSYpbQljS-LSK10Gk7eQb1bn0PKuAUn7CPIyw1XyZ1BJ6mIZskjcK5TgoJEJVdYeFZRH_Y4vG8tRIuCcXKKFOKgM6Ye-nQVrf1pN3zaJbcoDOvxynJoJDxpVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزانه 1 میلیون توکن رایگان برای مدل‌های زیر
💥
🆓
Gemini 3.8 flash | Muse Spark 1.3 |GLM 5.3 Flash | Deepseek V4 Flash | Deepseek V4 Pro | GPT 5.6 Luna | Gemini 3.1 pro
✅
وارد سایت زیر بشید و ثبت نام کنید و یک کلید دریافت کنید
✅
‼️
نکته :
با هر آیپی ۱ بار میشه ثبت نام کرد اگه میخواید چند اکانت بسازید هربار آیپی هارو تعویض کنید
📌
Base URL :
https://apinex.bond/v1
🔗
لینک سایت
🔗
گرفتن کلید
🔗
دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfHLFWamVaZ94xUXxDQjGrQhuTuqgsgloe_dzKuk4Pb7hoLETYBsHFJ5z58kANEAgjw7xKPoelMFV0iueM0Lq21Q42vGxKJpon2XgX8IrMYxuGxRjwIQnBFnZ_4dvmebEg7AhvoFrIvo8E1SvcrIOLkFsUhXkIWjZHtWbWmC_B4HG9s3kyy7b1PyWd0XOHu5Z-MEKQyhYHcM2FHxmGFBqMOtp0aG5f8s0o-EkXcedZYPlv4ZfxhJ-qm7Z8x4vjzUyz3iY7EZZWEyrZQ9jH2XpAEUPEc4faJKecYkqr9yac-7Ww0DoQb3ZL3sr7lUWUNb14tqmYszPkWGz09nIsUG2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 میلیون توکن رایگان 1 ساله
💥
🆓
Fable 5 | Opus 5 | GPT 5.6 Sol | Grok 4.6 | GLM 5.3 | Qwen 3.8 max | Kimi K3 | Deepseek V4 Pro 0813
✅
برید داخل
این سایت
ثبت نام کنید
حالا برید داخل
این بخش
پلن سالانه رو انتخاب کنید و این کد تخفیف رو بزنید :
DEVWEEK
بعد اینکه تخفیف اعمال شد تایید کنید و تمام ، یک api بگیرید و استفاده کنید
✅
📌
Base URL :
https://codecraftapi.com/v1
اکثر مدل های جهان رو داره میتونید از Playground چک کنید ، چون سایت شلوغی هست طول میکشه تا ریکوئست ها جواب بدن
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQQX7caOpapQL650dp3dfOR6CPIFaeX37Aug4Ka_Fb5ksJmvaTih9mGO8u_6hRV8Xr6VwHmYBG3N74hrk0KY8PN7lRb9TfZ2lPQU3lPhQXWDMhlBCWdJAwhoq2OzN_v2UKy3UJ4YwBxSnnhoubMHPK4lZQ9pETnj3VCEP5wYCgikTbjU3BaWbgt6aFxwUtMUxlUURBCdUH-eruUBSj-eoWJWpyv-9EwDFgOPsLcDlkYPf8ju2x45tKQD695MMG9nZ1APWO9TFgwJCHAmTtVBj8ASgJGrBUtEGFhb8_G9rPZxvwsiT2cdawvLfraEF0V9MYyfilJWzsCSinNYFn1y9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
تغییر ریجن گوگل در ۳۰ ثانیه
⏱️
با فیلتر شکن کشور مقصد یکم برین تو گوگل بچرخین،
بعد به لینک زیر بروید، ریجن را انتخاب کنید، دلیل تغییر را بنویسید و ارسال کنید.
https://policies.google.com/country-association-form
حداکثر تا ۲ ساعت ریجن به جایی که میخواهید عوض می‌شود و ایمیلش میاد
✅
بعدش میتونین به راحتی از antigravity و سرویس های دیگه گوگل استفاده کنین.
از توجهتان ممنونم
🙏
✈️
@ArchiveTell
|
#method</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">📌
Model :
gpt-6-astra
📌
Base URL :
https://api.eirouter.ai/openai/v1
sk-e76d452dff7eccef0a1b6bde4f8262c7f628f4f2991676cf3188d0cb68023b3f
sk-778bbaffd07397311260074542e405ab11833bf458e0250363ac1afd7db02297
sk-b028d3f23d96d0b0fc96a24985164437fcaf272276caf33548a664a0df424dc1
sk-1f153c31ccd2448b30c2f56287d5dc8fcc8ddafa579d12a797450321d86e9d29
sk-3334618935b09f67a70938d3379971e3ad350fec1154008d3abbaa07565c00b3
sk-242582ef9fc5e53351eb2fd67178b83033a450a61d048cf66be6aacf98a9e2bc
sk-db726cb7cc5b14160f9d8900455fcd34fd56cbb94f3afac65494a5161eee35b6
sk-7e85fc089be2d58f76c236c8ae1efc6062f68a459bdc9f87bcbe896c2d7307e2
sk-cca857a86f2c62b5d704f2234ed5632f8ef4dfbfcc0da509fe0e021516a0406d
sk-3c3eb497a104328775de0ddb333c7c8d596c20a89e25bbe7e204318f35e2b050
موجودی هر کلید هست 5 دلار ولی نکته اینجاست توی سایت قیمت هر یک میلیون توکن این مدل هست 1 دلار
😁
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=rLDEQugMPxhfiZ_OlhECPwjasGnG-o59Lf4lf_Lv2smeEc2QvvOgbejoQVrVqYWTBebM-Ulo9soCtCrKRuBcogWRP67zzY4UD9c3cSCEr4YDhgHOqfE05J-ETi1YvOffZwc0_ThB7CA4RiE8stqhs2vTOgBlp0DiTsrEwlbr22aOOCx91tcvvg3ZZWif_s6P0klWNO9B25E4vyg5FtlLGIy2jlma4qTKIgEuNfPYDd1FSLxb5qdsnHpIsry-VRa_k4wVhIVLGHh0g15dtGSJp0DQusk8klfgi9CH-5_Js5XCedLH-rZpMrZw2EAL-9hm7rqI4ozOIuzZ6KmC2uJ2u7KQjHXqPjQLwajDJTHGiH8WZNWBR1mk_OZU0mz5DR4LMeJJ_zSha4twyG1NMjjzIBHXK85C2NPJgbB3NXUMVM0gCGfcXML985seGc2HFrj4v7fyL7mKSzEOVqP9VJO-RTFI7IU1HHUttAcwSR_IsiyprM7L5tHqP6CDEHHRFVHDzxlei8kWBEWU4pSqbqZ4h3coSiFw90FGmPzykkZzYy4irfHbIxKW8gt9keP-1M1LK03VjrTty013_4TwCXisxBE8J5qJfUkT78oeAo4aVBNby35wVgtbT6nrGeAcj0xVOBrwTfsj7I7GHZ97RnGV3S-w7y9QqnqKUdmIUXf26Bc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=rLDEQugMPxhfiZ_OlhECPwjasGnG-o59Lf4lf_Lv2smeEc2QvvOgbejoQVrVqYWTBebM-Ulo9soCtCrKRuBcogWRP67zzY4UD9c3cSCEr4YDhgHOqfE05J-ETi1YvOffZwc0_ThB7CA4RiE8stqhs2vTOgBlp0DiTsrEwlbr22aOOCx91tcvvg3ZZWif_s6P0klWNO9B25E4vyg5FtlLGIy2jlma4qTKIgEuNfPYDd1FSLxb5qdsnHpIsry-VRa_k4wVhIVLGHh0g15dtGSJp0DQusk8klfgi9CH-5_Js5XCedLH-rZpMrZw2EAL-9hm7rqI4ozOIuzZ6KmC2uJ2u7KQjHXqPjQLwajDJTHGiH8WZNWBR1mk_OZU0mz5DR4LMeJJ_zSha4twyG1NMjjzIBHXK85C2NPJgbB3NXUMVM0gCGfcXML985seGc2HFrj4v7fyL7mKSzEOVqP9VJO-RTFI7IU1HHUttAcwSR_IsiyprM7L5tHqP6CDEHHRFVHDzxlei8kWBEWU4pSqbqZ4h3coSiFw90FGmPzykkZzYy4irfHbIxKW8gt9keP-1M1LK03VjrTty013_4TwCXisxBE8J5qJfUkT78oeAo4aVBNby35wVgtbT6nrGeAcj0xVOBrwTfsj7I7GHZ97RnGV3S-w7y9QqnqKUdmIUXf26Bc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده:
جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch:
کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی خودش اونو به آرت نهایی تبدیل کنه
🎯
ادیت موضعی دقیق:
امکان هایلایت و تغییر دادن فقط یک نقطه خاص از عکس، بدون دست‌خوردن بقیه جزئیات تصویر
💡
نکته دسترسی:
تعدادی تمپلیت آماده هم برای تسریع کار اضافه شده و این مدل در حال حاضر به‌صورت عمومی داره برای تمام کاربران فعال میشه؛ حتماً حسابتون رو چک کنید.
🔗
ورود و تست در وب‌سایت
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⭐️
۶ پلتفرم برای تست رایگان GPT-6 Astra
دسترسی مستقیم و استفاده از API مدل‌های پرچمدار و سنگینی مثل GPT-6 Astra معمولاً هزینه بالایی داره و اگه حواستون نباشه خیلی سریع اعتبارتون رو صفر می‌کنه!
💸
با این حال، یه سری پلتفرم کاربردی وجود دارند که اعتبار (Credit) اولیه یا سهمیه تست رایگان می‌دن تا بدون نیاز به پرداخت، بتونید قدرت این مدل رو توی چت، کدنویسی، پردازش تصویر یا ساخت ایجنت بسنجید:
1⃣
پلتفرم Vercel AI Gateway
یکی از مطمئن‌ترین گزینه‌ها به‌خصوص برای دولوپرها. این سرویس هر ۳۰ روز حدود
۵ دلار کردیت AI رایگان
به کاربرانی که حساب فعال دارند میده. محیط Playground، پشتیبانی از ایجنت‌ها و سازگاری کامل با فرمت OpenAI API داره و برای ادغام با پروژه‌های شخصی عالیه.
2⃣
پلتفرم Brainbase
اگر دنبال کدنویسی پیشرفته، تحلیل ریپوزیتوری و ایجنت‌های خودکار هستید، اینجا فوق‌العاده‌ست. بعد از ثبت‌نام اولیه،
۲۵ دلار کردیت رایگان بدون نیاز به کارت اعتباری
دریافت می‌کنید تا بتونید تسک‌های سنگین برنامه‌نویسی و اتوماسیون رو با مدل پیش ببرید.
3⃣
ابزار Roboflow Playground
بهترین جا برای محک زدن قابلیت‌های بینایی ماشین و پردازش تصویر (Vision). توی این محیط می‌تونید اسکرین‌شات‌ها، نمودارها و تصاویر پیچیده رو بدون نیاز به کلید API آپلود کنید و دقت تحلیل مدل رو با بقیه ابزارها مقایسه کنید.
4⃣
سرویس CometAPI
اگه مدل رو برای اتصال به ربات تلگرام، افزونه یا اپلیکیشن خودتون می‌خواید، این سرویس کار رو راحت کرده. بعد از ثبت‌نام کردیت رایگان میده و چون ساختارش دقیقاً مشابه API استاندارد اوپن‌ای‌آی هست، بدون تغییرات عجیب غریب توی زیرساخت کارتون راه می‌افته.
5⃣
پلتفرم Imaginode
یک فضای همه‌فن‌حریف با محیط تعاملی Canvas، چت، API و ادغام با پروتکل‌های MCP. بدون کارت بانکی کردیت اولیه میده و هر پیام با این مدل حدود ۱۲ کردیت مصرف می‌کنه؛ بنابراین برای ساخت سناریوهای متصل‌کننده متن، تصویر و اتوماسیون حسابی جوابه.
6⃣
سایت Vibany
ساده‌ترین و دم‌دستی‌ترین راه برای تست تفریحی و سریع. در بدو ورود حدود ۳۰۰ کردیت رایگان می‌گیرید و هر بار اجرای مدل حدود ۱۰۰ کردیت کم می‌کنه. یعنی حداقل ۳ الی ۴ تا پرامپت عمیق و جدی می‌تونید بهش بدید تا خروجی رو با مدل‌های قبلی مقایسه کنید.
✈️
@ArchiveTell
|
#AI
#API</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🧠
شیائومی وارد میدان ایجنت‌ها شد؛ معرفی دستیار همه‌کاره MiMo Desktop!
بچه‌ها شیائومی رسماً وارد قلمرو ایجنت‌های سیستمی شده و یه دستیار دسکتاپی معرفی کرده که مثل ترکیب Codex و قابلیت‌های کنترل کامپیوتر Claude عمل می‌کنه؛ این ابزار خوراک خودکارسازی کارهای روزمره شماست.
🖥
کنترل کامل دسکتاپ و وب:
اجرای خودکار تسک‌ها، کلیک، تایپ، کار با فایل‌ها، پر کردن فرم‌ها و امکان ضبط و اجرای مجدد فعالیت‌ها (Record & Replay)
⚡️
پیش‌نمایش تعاملی و ادیت موضعی:
رندر زنده سایت‌ها، گیم‌ها و داشبوردها با قابلیت هایلایت کردن یک بخش و بازنویسیِ انحصاری همان قسمت
🧠
دسترسی رایگان به مدل‌های نسل بعد:
بهره‌مندی تسترها از دو مدل معرفی‌نشده و پرچم‌دار MiMo-X-Pro-Preview و MiMo-X-Flash-Preview
💾
کشینگ فوق‌سریع تا ۹۹٪:
فناوری بهینه‌سازی توکن برای تغییرات مداوم پروژه‌ها جهت جلوگیری از هزینه‌های اضافی
💡
نحوه ثبت‌نام در نسخه بتا:
ظرفیت بتا کاملاً محدوده و اولویت با کاربران فعال اکوسیستم MiMo Open Platform خواهد بود؛ فرم درخواست رو پر کنید تا لینک دسترسی و مدل‌های جدید زودتر براتون فعال بشه.
🔗
فرم ثبت‌نام در نسخه بتا
🔗
صفحه رسمی معرفی
🔗
صفحه رسمی قابلیت ها
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=Muw8VYsF_6w8u3TCTUvij68uGHhw6uwQKxv3IPUlU9c7I-4whoKYt3C2dNPyodVniL3Fo_ohCqT0OPdhq1Q0j5XYUEBoUCjSxP-XMXI9z6OmtGvUnfG6_VuuQ6vilZhvwQfgWpUmO_u031Fmycr2Ua7gat6fMB_5U6cHV8PrScPTH4yNPtmeI3rDaEzguchVB4zLh30ZMdiD7xgn5jUjLyeAvmAGXqBgp_zGzFj3IGy9XME9r7QzeiB_DSAAjhcvwCbhgDqavzmQZ47BUlodps2FZerMMIRZUAYjUaJJ4ciMMdku1chxlKt0OLBPFUhahDDN4NDeXQsKcpACLnDN7azYQnk6XH4pzhy0YC3YttA4Fkngd66K2RN3ENkSa46XzD2aiK1O4fxjMqrs30BW1w-J65EC6Nhd71OGdngXu1CJWojCwXrJXBE0e6w1EuvJNvF4JNbUZrPIr6EqgyUa7kqLofB_RHUIf-1rs373k_jjiew794chqi6msMQvOZ1H5oSkp1VjD4dy3GJI4RXjb9t05s4OJXKJtiVp2VQ0uzhFI2qObpirWZJmxkJBnnB90-XjOikSOxHHRHfWQ101H3lFM42rE0aPkrlZh76Ooa_i6U7FMhX_KS25OQcH_yMa3E9jdon3Fxh8rKHOlXMgSWIwRjWTAPdwhRNTaw9pPXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=Muw8VYsF_6w8u3TCTUvij68uGHhw6uwQKxv3IPUlU9c7I-4whoKYt3C2dNPyodVniL3Fo_ohCqT0OPdhq1Q0j5XYUEBoUCjSxP-XMXI9z6OmtGvUnfG6_VuuQ6vilZhvwQfgWpUmO_u031Fmycr2Ua7gat6fMB_5U6cHV8PrScPTH4yNPtmeI3rDaEzguchVB4zLh30ZMdiD7xgn5jUjLyeAvmAGXqBgp_zGzFj3IGy9XME9r7QzeiB_DSAAjhcvwCbhgDqavzmQZ47BUlodps2FZerMMIRZUAYjUaJJ4ciMMdku1chxlKt0OLBPFUhahDDN4NDeXQsKcpACLnDN7azYQnk6XH4pzhy0YC3YttA4Fkngd66K2RN3ENkSa46XzD2aiK1O4fxjMqrs30BW1w-J65EC6Nhd71OGdngXu1CJWojCwXrJXBE0e6w1EuvJNvF4JNbUZrPIr6EqgyUa7kqLofB_RHUIf-1rs373k_jjiew794chqi6msMQvOZ1H5oSkp1VjD4dy3GJI4RXjb9t05s4OJXKJtiVp2VQ0uzhFI2qObpirWZJmxkJBnnB90-XjOikSOxHHRHfWQ101H3lFM42rE0aPkrlZh76Ooa_i6U7FMhX_KS25OQcH_yMa3E9jdon3Fxh8rKHOlXMgSWIwRjWTAPdwhRNTaw9pPXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آرشیو ۱۵۰ پرامپت آماده برای خلق ویدیوهای سینمایی با AI!
بچه‌ها اگه با هوش مصنوعی ویدیو می‌سازید ولی خروجی‌ها تخت و مصنوعی میشن، این کالکشن خفن خوراکتونه. یه دیتابیس آماده از ۱۵۰ پرامپت تست‌شده که دقیقاً دستور زبان کارگردانی و سینمایی رو به مدل تزریق می‌کنه.
🎥
کنترل دقیق نور و دوربین:
پرامپت‌های تخصصی برای مدیریت لنز، زوایای حرکت دوربین، نورپردازی و دکوپاژ
🎞
همراه با نمونه ویدیویی:
هر دستور شامل پیش‌نمایش رندر واقعی است تا قبل از خرج توکن، خروجی کار رو ببینید
🎭
تنوع ژانر و اتمسفر:
پوشش کامل انواع سبک‌ها، سناریوها، اکت کاراکترها و فضاسازی‌های سینمایی
💡
نکته استفاده:
تمام پرامپت‌ها آماده Copy/Paste هستند؛ فقط کافیه کپی‌شون کنید داخل ابزارهایی مثل Runway ،Kling یا Luma و المان‌ها یا کاراکتر مدنظرتون رو با کلمات کلیدی دلخواه جایگزین کنید.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIoR1o1J9uRnmAZSrPxd1ieIWR1k4RvkJih4yo4iU3GWTItxvVenfruAFRUPejtW8wMEoWFp1suZd4tQfse01T1vAT1zPYdn-2-UIXQmPHlC8kjymR4q0nWGTKdP_aplmW1DJnGtbqAmENnbSlCVKRfHfSjXpWEi2R3OJfdgTR7N5G13h7kWgfbpXLLfLYoOdTCwQHUkzlLvMNHFedxx_MxiWdzfMIiypWI3ZQvj4EIzUIfZncnpe8ZY9dSH6ldwDGkKUeyTDlFKoihc2rGlcOHq3GIjokqEPp3DzILd1w4lvpzhuhCD2xqZapCwjVZIu_zKAwE6jY6u218jH1YfFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مایکروسافت آفیس رسماً مرخص شد؛ معرفی غول اوپن‌سورس GenOffice!
بچه‌ها اگه از خرید لایسنس آفیس یا برنامه‌های سنگین خسته شدید، این پروژه جدید خوراکتونه. یک جایگزین کاملاً رایگان و متن‌باز برای مایکروسافت آفیس که ایجنت‌های هوش مصنوعی رو مستقیماً آورده داخل اسناد، جداول و ارائه‌هاتون.
📝
پکیج کامل و همه‌کاره:
مدیریت بی‌دردسر داکیومنت‌ها، شیت‌های آماری، ساخت اسلاید و کار با PDF بدون نیاز به ابزارهای متفرقه
🤖
ایجنت‌های تحلیل‌گر:
اتصال مستقیم به مدل‌های قدرتمندی مثل DeepSeek ،Claude و Kimi برای تحلیل داده، نگارش متن و تولید محتوا
💻
آزاد و مولتی‌پلتفرم:
پشتیبانی رسمی و نیتیو از مک، ویندوز و لینوکس بدون نیاز به پرداخت حتی یک ریال
💡
نکته جالب توسعه:
جالبه بدونید نسخه اولیه این پروژه رو فقط یک مهندس، توی مدت یک هفته و با سوزوندن ۱۰ هزار دلار توکن هوش مصنوعی جمع کرده! ریپو تازه پابلیک شده و سرعت استقبال ازش وحشتناک بالاست.
🔗
گیت‌هاب GenOffice
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=XvA88Nth5OYmniPSsfgDR7sgxFoh-uTVX_A1tIG2YdgvqlFgv3yWERVVBDGc6glhlcbq2c7gRi2E5Dq2OXIyL0ewmcN9CRALZGzO-BwYGC1IsYD3dCqazMEg_Sk9PT7yNCV72msoc_sL6dTRWgvxTe9ohbGuyW51YdVhRRftvi-BNw_6_xB_KiE3-h4G2tx1w_t2PHtswo6fh1G9Lcbs5RL2Ua0mqBsUe38TQDIDag1jUoGcNvzn7UYc9BgiirFM8POLqEpZGqEqCkH0undbOPs4gopZsqiKwduVPs_6bNxr0KLPbZAQnIG8u8gTpcIp8WYSKYWLQl6StSGI62zAmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=XvA88Nth5OYmniPSsfgDR7sgxFoh-uTVX_A1tIG2YdgvqlFgv3yWERVVBDGc6glhlcbq2c7gRi2E5Dq2OXIyL0ewmcN9CRALZGzO-BwYGC1IsYD3dCqazMEg_Sk9PT7yNCV72msoc_sL6dTRWgvxTe9ohbGuyW51YdVhRRftvi-BNw_6_xB_KiE3-h4G2tx1w_t2PHtswo6fh1G9Lcbs5RL2Ua0mqBsUe38TQDIDag1jUoGcNvzn7UYc9BgiirFM8POLqEpZGqEqCkH0undbOPs4gopZsqiKwduVPs_6bNxr0KLPbZAQnIG8u8gTpcIp8WYSKYWLQl6StSGI62zAmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت خفن: تبدیل هوش مصنوعی Astra به یک بات بازی‌ساز حرفه‌ای!
🎮
🔥
داستان از این قراره که یه دولوپر، Astra رو طوری شخصی‌سازی کرده که عملاً تبدیل شده به یه ماشین بازی‌سازی. اصلاً هم شوخی یا بازی‌های دوبعدی و پیکسلی دم‌دستی نیست؛ کیفیت کار در حدیه که باورتون نمیشه کل این دموی سه‌بعدی خفن فقط توی
یک ساعت
جمع شده!
👀
⏱
سازوکارش چطوریه؟
🛠
همه‌چیز با یه اسکیل (Skill) جلو میره:
* اول Astra باهاتون گپ می‌زنه و از بین ایده‌هاتون، کانسپت اون بازی رویایی که تو ذهنتونه رو درمیاره.
* بعد طبق همون پلن، توی ده‌ها دور آزمون و خطا پروژه رو قدم‌به‌قدم کدنویسی می‌کنه و می‌سازه.
پرامپت استفاده‌شده برای ساخت این دمو:
📝
Prompt (high effort): /dream-loop Build me a graphics demo: isometric camera, voxel-ish art style with realistic shading and reflective wet floors, a character in an interesting scene. Fantasy setting (think Elden Ring, Diablo). Three.js in browser, >60fps. Don't download assets. Time limit of 1 hour. Controls: click to move the character, camera lazy-follows; drag to rotate camera; scroll to zoom in/out. No gameplay for now. World should feel alive: motion, animations, subtle environmental behaviors. Area around player should look expansive, but only allow movement in a limited space. No need to confirm the art with me or ask questions, just go!
🔗
دموی بازی توی مرورگر
🔗
خود اسکیل Astra
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDwba2sts3CwQdQLg2UrXiSQkuFv05dgmSAXvjqbIokSPCVyz93AXGmyLQam_6IjTlyBvry8VL0m6uQrZvp2zLNdGtdH6rwWbivEW0h3mxwCP0gpsiR9aiuqJrLZwZebN-EJ1YA6JiMMcdKHnBXmoAchXfKqhwr_Fgp90RcH7cNpyZOowF6VQXZMEwPE6dna1tLEpb4JB1xtYWEkbZ3wGS8-NtwSvNEsqcihJ5tn0ARLCSjqP264dHXfbsLGf3qu5VxRDW_5iuQgN0YCRqdpWuhpisRcf6xgZw4yginiONcFX23OjESjjvfnnRTsXIFhrChksrcKQpYSVWJY9kpKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📝
باز کردن بی‌دردسر فایل‌های آفیس روی اندروید با OpenDocument!
بچه‌ها اگه فایل‌های متنی یا اداری دارید و دوست ندارید برای باز کردنشون تو سرورهای ابری آپلود بشن، این اپ خوراکتونه. تمام اسناد OpenOffice و LibreOffice رو کاملاً آفلاین، سریع و بدون نیاز به اکانت باز می‌کنه.
📁
پشتیبانی کامل از فرمت‌ها:
خواندن بی‌نقص ODT ،ODS ،ODP در کنار فایل‌های رایج DOCX ،XLSX ،PPTX و حتی PDF
🔒
حریم خصوصی واقعی:
پردازش کاملاً لوکال، بدون اتصال به اینترنت، بدون ترکرهای تبلیغاتی و بدون نیاز به ثبت‌نام
⚡️
سبک، امن و باسابقه:
یکی از قدیمی‌ترین و پایدارترین پروژه‌های متن‌باز اندروید (فعال از سال ۲۰۱۰)
💡
نکته کاربردی:
بهترین گزینه برای کسایی که با فایل‌های کاری و اسناد حساس سر و کار دارند؛ با خیال راحت می‌تونید حتی در حالت Airplane Mode به تمام داکیومنت‌هاتون دسترسی داشته باشید.
🔗
گیت‌هاب پروژه
🔗
وب‌سایت رسمی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7681" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7680">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=e-Ax4K9RTpCBXN19EWqi1nZOIbLotMsEgU61UakHrWA7YORULzFu5UoIuDfkI7gM7VQ5wuLgCMXx0QcHh7S1ug0uny084f220gePfd_dHZEbEQ-WIhAaevHFJJISkTOjHjvCQUkx52iGpYHt34DIs0mI-jxS433o26gmCVVdejI_qAHsennbBSxUxkm3MlXuheQJjKErav59kvPpmU_tyoLmtGQ8CJVDavNHfcuZ9tGwHr1QjvNg7vZ5EXgIIWCmcKWAGpypA06_80G-LAesC-2kvYsZ0dX9mMmBTh3msqb1L1httK9_TDiZKszD6D2_Kx8c6mdbXxi6SXo2JEnf9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=e-Ax4K9RTpCBXN19EWqi1nZOIbLotMsEgU61UakHrWA7YORULzFu5UoIuDfkI7gM7VQ5wuLgCMXx0QcHh7S1ug0uny084f220gePfd_dHZEbEQ-WIhAaevHFJJISkTOjHjvCQUkx52iGpYHt34DIs0mI-jxS433o26gmCVVdejI_qAHsennbBSxUxkm3MlXuheQJjKErav59kvPpmU_tyoLmtGQ8CJVDavNHfcuZ9tGwHr1QjvNg7vZ5EXgIIWCmcKWAGpypA06_80G-LAesC-2kvYsZ0dX9mMmBTh3msqb1L1httK9_TDiZKszD6D2_Kx8c6mdbXxi6SXo2JEnf9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📍
با GeoSpy لوکیشن دقیق هر عکسی رو دربیار!
بچه‌ها اگه دنبال لوکیشن یه عکس رندومید یا اهل چالش‌های OSINT و ژئوگسرید، این هوش مصنوعی خوراکتونه. حتی اگه متادیتا (EXIF) پاک شده باشه، از روی خط‌کشی خیابون، گیاهان، معماری و تیر چراغ‌برق مختصات رو براتون پیدا می‌کنه.
🌎
جست‌وجوی جهانی (Global):
پیدا کردن چند تا از محتمل‌ترین کشورهای دنیا حتی از روی اسکرین‌شات یا عکس کراپ‌شده
🏙
مود شهری (City Search):
اگه شهر مشخص باشه، با عکس‌های خیابانی مچ می‌کنه و آدرس دقیق پلاک و خیابون رو میده
📸
تحلیل چند زاویه‌ای:
امکان آپلود تا ۴ عکس از یک لوکیشن برای بالا بردن نجومیِ دقتِ حدس
💡
نکته طلایی:
کیفیت عکس اصلاً مهم نیست؛ این ابزار حتی فرم شاخه درختا یا مدل آسفالت رو می‌فهمه! موقع ثبت‌نام اولیه هم یه سهمیه سرچ رایگان بهتون میده تا تستش کنید.
🔗
وب‌سایت ابزار
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5ED6oWalC9QGA_t6N0Uu4A95aMfYAaF_vVdxMJBuoVq3FeaqJNugONbScnLxWKjRkjqu_4HY5Iw1ZnR_1gbhU5_b-Kan1gMvuNs9iiEAwii0evaGC-qHV9ffwcu9T9bClFrTbW32sVLM1iHIejyELj8WJiiCzS9hT0txsWL15XOqjkwib4FGeXLVe4W4czarXf1qYKMJyDRnapGDCAW2xVIE2zVQXpuIs63anTiVUhBiqxtIoyTPycWAzF8icJhbAYgVmvhgdFfjdi-oP9bzQitoMrZIWfZjNBy1YOJPFOznerdhkZMXOl_52O8fYravm17iqUFWK_KUeHMxzc8GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕸
با SpiderFoot ردپای دیجیتال هر چیزی رو توی اینترنت بیرون بکش!
بچه‌ها اگه تو حوزه امنیت، تست نفوذ یا اوسیانت (OSINT) کار می‌کنید، این ابزار دقیقاً خوراکتونه. اسپایدرفوت یه ابزار متن‌باز و بی‌رحمه که کل سطح وب رو شخم می‌زنه تا تمام ردپاهای دیجیتال و آسیب‌پذیری‌های یک هدف رو دربیاره.
🎯
تارگت‌های همه‌جانبه:
جست‌وجو بر اساس شماره تلفن، ایمیل، آیدی توییتر و تلگرام، نام، IP و دامنه‌ها
🤖
اسکن تمام‌خودکار:
جمع‌آوری آنی داده‌ها از بیش از ۱۰۰ منبع اطلاعاتی بدون نیاز به سرچ دستی
📊
نقشه ارتباطات بصری:
تحلیل داده‌ها و نمایش گراف‌های دیداری از اطلاعات لو رفته و پیوندهای مخفی
💡
نکته و اجرای سریع:
راحت‌ترین راه اجرا با داکره؛ کافیه دستور docker run -p 5001:5001 spiderfoot رو بزنید و پنل تحت وب رو باز کنید. (یادتون نره، فقط تست امنیتی قانونی و اهداف آموزشی!)
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdX9UPkDDz6dnHgYWr0uM1tSP_vkqemIy7lGqyrGs9FAnrU0nKqf3BJlizqxeAtd7yKT32IzUeCpO28DqYxpHQdAjB7_hn-ZoQZzKIPPaTGF3eeTPceyfHQlNB1NKEoxMhz9aKzk_dIqeUmvi63E8ZFE3eRzawdMUlMk-R39y0kh6S_tioKXh9LRhP_P00YrFCb4x1Gp1V4DQN1rFLveQipWieN85NYymttAo4F0d-gVOrWcptB97waEqALWg2R8wEegEIEILmY-wsDufkJpH8NRftrHGkjR2cjkfqkodpZLE1kPPmuC30Bw49OPXZ4n-2YwwU8NMfaiJ9c42GylhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توکن‌های نامحدود برای Claude Code با شاهکار مهندسان اسپاتیفای!
🚀
🧠
پلتفرم
Portal
مثل یک مدیر هوشمند عمل می‌کنه و با واگذاری وظایف ساده به مدل‌های ارزان‌تر، تا ۹۰٪ در مصرف منابع و توکن‌های هوش مصنوعی شما صرفه‌جویی می‌کنه!
🔥
🔺
تندخوانی با Gemini (bulk-reader):
فایل‌های حجیم و چند هزار خطی توسط Gemini 2.5 Flash آنالیز شده و فقط یه خلاصه مفید به Claude تحویل داده میشه.
🔺
کدنویس روتین (code-writer):
تولید کدهای استاندارد، تست‌ها و تنظیمات خسته‌کننده به مدل‌های کم‌هزینه سپرده میشه.
🔺
تمرکز روی کارهای حیاتی:
با این روش، Claude فقط درگیر کارهای پیچیده و استدلالی (مثل رفع باگ و طراحی معماری) میشه.
💡
در
نتیجه:
یک ترکیب هوشمندانه از چند مدل AI که باعث میشه هزینه‌های شما ۹۰ درصد کاهش پیدا کنه و خیالتون از بابت محدودیت توکن‌ها راحت باشه!
🔗
لینک دسترسی و پروژه
✈️
@ArchiveTell
|
#TOOLS
#AI</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBu0ofA2UF-tmKIQZKL1gg-Dz0zoz-2zteu0kBg3CNp9gPK7a1TBJPBxAlxi6Pzfv1yzO8LG-oMOHQ0_v2L2gLERyikKK44asYu0MEqoRhYahHu6yyiw_RJyF43hOX_9O7_3UYCCv8tkAOE38GqYSw8Tp6aLIUSlPOp6q1h3mt4MGPMM8jdfBZQVmjTGTU9UwoOmZEHkTgiJ3RyZ2PdRl1qBdM46pyLVUsrIBXPMoRy4726btBbRtna6GD0KQUk5cEiN47Niy701AOHlbnT6Y7gL4Qt0B8q7AvVFHbWJHxUjPw5u-j7jkKDnbpzmjQDYy3q6tf3hExpnjj9vsmvdlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت
یا کاملا رایگان باشه یا فریمیوم
با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم
اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/esmDyrgQDHEq4ZWwsHyybRoNm1lC4cSzzIFeSvrlAXmVkzwMEHsihaS_NzFTWhU-WI5zesVhd5sah3FDoKuJVO2mHz2NX-0YYotBl67YgEd1Inh5s50Rs4iYoSeASa-mqLtu2Z7Lm1Z-q4Yr2Ikc5iPm3zet8Xyg_YRk50cnM2I9RgEDtvKhIlm4GDzRjjeLHjnECQqXmYY57pt1WOJ608FdMcyWP52xlRQn0r6EyxWOQ7tgBKDEqLyNE4MnMCHr7xsTzVje0cAAykAQMt0DqX4I_k-dBTNoyTrc0BhugxmQ2PaWR0YGx0G0WXD5SJpM1lYQHJLiuF_4HCO6ppqf4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qyicT06MhYEDFaUzOdYtNYmuIIVBzpXShGg7Fm6Oa1lL2dftxADgKCkVxnPT_jOF9JAETUkPzWShkSQuPT-MWucmW8biaBd-jizGpy0eK_47s9TRKouEpVkKsN0XNaDJ_73zBxNFiA9mDzwWrBzweJ2hSrIj3skn5gS5Ua6LhmtwmEw8GmPlteDAIji93ur5_0iiCXvlZKCh_dhfxd6mdUn9k48d0GLNA16bpFxFLXOUGCuncjOKSHH5PTVs-5TqW7NPblyvtuZoibu3mnWABd_3SUOYbalbPJSjMTN8BdS7bC0FRohwpe174lMMDIHx9O7OJ0_JKWhzdW0xiBCMog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📌
مدل GPT-6 Astra بازم یه حرکت دیگه ثبت کرد؛
بازی Portal رو تو 23 ساعت و 43 دقیقه تموم کرد!
مدل به طور خودکار شخصیت رو کنترل می‌کرد به طوریکه هوش مصنوعی یه تصمیم می‌گرفت، بازی متوقف می‌شد. GPT-6 Astra با استفاده از تصاویر، موقعیت شخصیت و زاویه دید دوربین، تصمیم می‌گرفت که چه اقدامی انجام بده. بعضی وقتا هم تصمیم گیری هاش تا چند دقیقه هم طول می‌کشید، اما در هر صورت تونست بازی رو به پایان برسونه.
🔥
این کارو آقای "cozyblaze" با کمک اشتراک ۲۰۰ دلاری Codex Pro انجام داد.
🔗
سورس پروژه
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlK1d9nDjbihdTf4c89xC8_YxJ4F8Wk-ATMnGfB9pvixLN86dsR4bDzpg2BRoEHiD6nTOAnJvocEm5QthiNpbAa0s1z6J5JI81_tRCFZD13rZQUjURrR3DEvjs765MXVXDKMwOe1BFBKWC-IpLbXCUSGTOepAWd50Juvlpu75lMIUV5RWNFokeFZgFqg-jEchUFAhlNxJmWh_WNt84VK7RRDh7gsGMveoaa3HJZcTe73i6UcHGb2i9HUJf1oE0y5QVAGZyVngC3q3Wj_SPST6zB34ouQ9JlTzhxGwLqCrtj426YjpHkBAWa8RiLaaguwHyO-UTijF4SOnUrBbOjjUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعبه‌ابزار همه‌کاره برای برنامه‌نویس‌ها با DevToys
💼
اگه خسته شدید از بس برای کارهای روزمره (مثل تبدیل JSON به YAML، تست RegEx یا دکود کردن JWT) مجبور شدید سایت‌های مختلف رو باز کنید،
DevToys
دقیقاً چاقوی سوئیسی شماست!
👍
🔧
بیش از ۳۰ ابزار کاربردی:
انواع کانورترها، انکودر/دکودرها (JWT، Base64، QR)، فرمترهای کد، هش‌ساز و فشرده‌ساز عکس.
📄
تشخیص هوشمند کلیپ‌بورد:
به محض کپی کردن متن، خودش می‌فهمه چیه و ابزار مناسبش رو پیشنهاد میده!
🛡
کاملاً آفلاین و امن:
تمام کارها روی سیستم خودتون انجام میشه و دیتای حساسی سمت سایت‌های ناشناس نمیره.
➕
پشتیبانی از اکستنشن:
میتونید ابزارهای دلخواهتون رو هم بهش اضافه کنید.
📌
لینک مخزن گیت‌هاب پروژه
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=fV530vJKMT5PHIniLYDv10PhqfBXmvUL1ZxwEltJC91Viihqltcs6r7dngf5L-8MCV7UGKXlTFtl_qQPEZHhXJXx0lLjSwz5ZkRQ23S49yzL7aI-oAcmHE2fEDlnmLmldXaoYWYCkN4AcKtGRypos8zN6pyRJj8mnUK06EXTMMMi9mjSBBaaxIj9LrjjDFx_XbFEfnh5I4lnJM7MNFPjmOJgdOwhhWmxDwlH3O--NxUL6eNTGsEQ1NiOvaobiFFVxWQXPVp7LpewC1v89aIOco3_Bdb4K2A0u7HgSHwnKV9XIQ7rf5ZEp6Sst-MQ8xZR1f1HPAyEiVHEOlPvaDAADw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=fV530vJKMT5PHIniLYDv10PhqfBXmvUL1ZxwEltJC91Viihqltcs6r7dngf5L-8MCV7UGKXlTFtl_qQPEZHhXJXx0lLjSwz5ZkRQ23S49yzL7aI-oAcmHE2fEDlnmLmldXaoYWYCkN4AcKtGRypos8zN6pyRJj8mnUK06EXTMMMi9mjSBBaaxIj9LrjjDFx_XbFEfnh5I4lnJM7MNFPjmOJgdOwhhWmxDwlH3O--NxUL6eNTGsEQ1NiOvaobiFFVxWQXPVp7LpewC1v89aIOco3_Bdb4K2A0u7HgSHwnKV9XIQ7rf5ZEp6Sst-MQ8xZR1f1HPAyEiVHEOlPvaDAADw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم 7 برنده خوش شانسمون
🎉
:
1.
@reza1629
2.
@mhti9
3.
@KIING_ZOG
4.
@Gogogrugo
5.
ＮＯＢＯＤＹ
( 6641463426 )
6.
@an_Y008
7.
@AshenOne2077
برای دریافت جایزه به دایرکت مراجعه کنید
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7670" target="_blank">📅 20:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7669">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7669" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7668">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🥇
رکوردشکنی دوباره از GPT 6 Astra
خبر رسیده که GPT-6 Astra تونسته تمام ۴۸ مرحله بازی «I'm Not A Robot» سایت
Neal.fun
رو بدون غلط رد کنه ، خیلیا جوری جو دادن که انگار آخرالزمان امنیت سایبری رسیده!
😂
طبق معمول، ته این هایپ‌های رسانه‌ای خبری نیست. کپچاهای تصویری سال‌هاست که عملاً مرخص هستن و حتی مدل‌های پارسال هم با یه پردازش تصویر ساده دورشون می‌زدن.
سیستم‌های امنیتی واقعی وب الان با تحلیل رفتار موس، کوکی‌ها و الگوی کلیک کار می‌کنن، نه با ۴ تا عکس چراغ راهنمایی و خط‌کشی خیابون
😁
تست کن ببین رباتی یا نه ؟!
🧐
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7668" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7667">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qd5n0Lb6j4UJEZwowRM7Jw6u1OVM5DQEDrn-_uMHRnPdNd7wa-vZODgiatq34Wxw1GjXT2XBtGFCG1sgRlQcx4zbpftm8eDzp_VGAA1852cVccObpKMjwODQ4fiw6QGZD9-YRQREK81z_huss97C1N2ivWWBRoWCRie5mD6Q4FB-bp77suTw0A0mwbgzyTWyOFcnP7UJ1gBXFo5pb8omBHdNzB0qNvxXBZu9v2Hd0XE8dH7V7F-9EYcSQdUfMPKgvjMS3qJrYn-uJ9J8XWRx91bY4pUDYyF1pbshqTi-pUsMEEDuZuonEm7DnVgtM0HwNdaGMTUANDioSCHy-EKocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جداسازی صدای خواننده از موزیک با هوش مصنوعی؛ تمیز و بدون دردسر!
🎤
🎧
بچه‌ها اگه دنبال ساختن نسخه کارائوکه هستید یا می‌خواید صدای خواننده رو برای ریمیکس بردارید، ابزار آنلاین
AI Vocal Remover
دقیقاً همون چیزیه که لازم دارید! با استفاده از مدل‌های صوتی AI، وکال و ساز رو در چند ثانیه مثل آب خوردن از هم سوا می‌کنه.
✅
🔺
پشتیبانی از انواع فرمت‌ها:
هم فایل صوتی (MP3، WAV، FLAC، M4A و...) و هم فایل‌های ویدیویی (MP4، WebM) رو به راحتی قبول می‌کنه.
🔺
بدون نیاز به ثبت‌نام و کاملاً رایگان:
پردازش تماماً در کلاود انجام میشه، قبل دانلود می‌تونید آنلاین پیش‌نمایش رو گوش بدید و تا یک ساعت خروجی MP3 یا WAV بگیرید.
🔺
کیفیت و دقت بالا:
تفکیک دقیق لایه‌های صدا بدون نویز و افت کیفیت محسوس سازها.
💡
نکته:
برای آهنگسازها، تدوین‌گرهای ویدیو و یوتیوبرها برای برداشتن کپی‌رایت یا ساخت بیت‌های بی‌کلام، این ابزار سریع‌ترین میانبر بدون نصب نرم‌افزارهای سنگینه!
🔗
آدرس ابزار
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7667" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7666">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUX1DB14WNAP5caNDl-9Jz2eNBu-twBqtol33ZhBuz5oFg8x-nDcVwnrMW_fH06HSCrDwH9RATK29C94b5fSD2Gih2VE_1wgvxvJT8kKYwGZwYsqy1IzfpN61pUKhssgmQztpn9iG9O41zfV3qXUXMBsdGmH4L4SGlPSeSQkMxGsS4aUrLD_iTtsnl6VmTchX4xOxCcxjFx5ywwbYejLwvZf-WbiKYdGS-wHpbhfNBNHFXlYQzJm6hzpxNAR8t1ZTmcZ5UbkPs8eWKidE7FME4W8PckGU1URaCF2bIJybfjCoWspZ4vjjTQB3CS0bmWq6nxPCuyuDr7bF_6A_GZhog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل گوشی اندرویدی به یک کامپیوتر دسکتاپ کامل با Android DEX!
🖥
📱
اگه از قابلیت محدود سامسونگ دکس خسته شدید یا گوشیتون اصلاً DeX نداره، این ابزار خوراکتونه! نرم‌افزار
Android DEX
با ترکیب جادویی ADB و موتور قدرتمند scrcpy، گوشی اندرویدی شما رو به یک سیستم‌عامل دسکتاپ واقعی با پنجره‌های شناور و کنترل کامل تبدیل می‌کنه.
🚀
🔺
تجربه دسکتاپ چندپنجره‌ای:
اجرای اپلیکیشن‌های اندروید در پنجره‌های تغییر سایزپذیر روی ویندوز، مک و لینوکس با اتصال باسیم یا بی‌سیم (Wi-Fi).
🔺
خوراک گیمرهای موبایل:
کی‌مپینگ حرفه‌ای کیبورد و ماوس، شبیه‌ساز جوی‌استیک WASD، قفل دید ۳۶۰ درجه شوتر (FPS Mouse Lock) و حتی شبیه‌سازی ژیروسکوپ!
🔺
دور زدن شناسایی امولاتور (No Ban):
چون بازی‌ها مستقیماً روی سخت‌افزار واقعی گوشی اجرا میشن، آنتی‌چیت بازی‌ها شما رو شبیه‌ساز تشخیص نمیده و بن نمی‌شید.
🔺
امکانات یکپارچه سیستم:
مدیریت اعلان‌ها، پخش صدا، انتقال فایل با درگ‌اند‌دراپ، رکورد صفحه و تعریف پروفایل‌های اختصاصی برای هر بازی.
💡
نحوه راه‌اندازی:
فقط کافیه گزینه USB Debugging (یا Wireless Debugging) رو توی Developer Options گوشیتون روشن کنید و برنامه رو اجرا کنید؛ بدون نیاز به روت!
🔗
گیت‌هاب پروژه
🔗
سایت پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7666" target="_blank">📅 14:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7665">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3lZ3-g2xnS3BXCpBtJyAEiXcP_HDfDURnEFQcLbqvBywbXzpZD3SNwOkkqDtoSV803VSBrvHhfvxjZun0WVKYtskTjbITG68_e7WWCoDQ5rNwFiGa3Brgzn_tMgccS0qCwyiQ6qGoEoEcNv2aV3VHlDrk1-yvoOeMfcIkaQ5zk-T7kWewbNAUrtXxMhTOPuWBNDFuYYiq2KP9BkGKta-Ep0wan-d6nIH-JelvAf_vcINXprlPIz55pc355DRpcJRa8dWaH4PKj3c3c9JOIf50xx0dLRsG_1hXBIyRAdvDu67Wxi1DzCFO1Yk6nSN0lGV3YVl9sDG8VWe1lLMALtng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معدن مقالات و دیتای آکادمیک اروپا؛ گنجینه‌ای که کمتر کسی می‌شناسه!
🎓
بچه‌ها اگه دنبال مقاله‌های خاص، دیتاست‌های خفن یا پژوهش‌های پروژه‌های اروپایی هستید که جای دیگه پیدا نمیشن، پلتفرم
OpenAIRE Explore
دقیقاً خوراکتونه! یه پایگاه عظیم با بیش از ۱۳۰ میلیون دیتای علمی دسته‌بندی‌شده و رایگان.
✨
🆓
🔺
آرشیو عظیم ۱۳۰ میلیونی:
دسترسی مستقیم به مقالات اوپن‌اکسس، دیتاست‌ها و حتی سورس‌کدهای پژوهشی پروژه‌های اروپایی.
🔺
بدون لاگین و کاملاً رایگان:
بدون دردسر ثبت‌نام، پی‌وال یا محدودیت دانلود، مستقیم به منابع معتبر دسترسی دارید.
🔺
ردیابی شبکه‌ای پژوهش‌ها:
می‌تونید خروجی‌های مختلف یک پروژه (مثلاً مقاله + دیتای خام + کد نرم‌افزاری) رو به‌صورت متصل به هم پیدا کنید.
💡
نکته طلایی:
برای پژوهشگرها، متخصصان هوش مصنوعی که دنبال دیتاست‌های تمیز و رسمی اروپا هستن، یا کسایی که دارن روی مقالات بین‌رشته‌ای کار می‌کنن، این ابزار مثل یک میانبر تمام‌عیار عمل می‌کنه!
🔗
وب‌سایت رسمی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7665" target="_blank">📅 14:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7664">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFxWbzrKzgVgP9PzNIXOk0pFkpoMb4QxW6w9NXufJcmsx11dvP_bOOLu6dVD8ppT3doRuHCN0EhDm2jT6EoS5xVqYewlAUsjJofY9eKPO63JJwCplWak-gqhkqyuEKItucFiZEvIruQ2N-htgl3ivKxCcuK-FNurnJg9NwEhQuadlJPiPKCD4xZZpt9PniuU4rZ2zbH0G9FLfNwi9a9BW0q5bvZ8TEnOdL1XF5kWWuVuT7visu7nz0hyda3DNXBfIyR2PqDa8x9VgsZnZotsOhe14gP0lKVx-y-qYFYEJV6CCL0lgT2DLwhSMIDRDjYjZdY2fy3BjMIs67_tZrhnqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیبورد «شریک جرم»؛ قبل از ارسال پیام حواست به جریمه و حَبسش باشه!
🚨
بچه‌ها براتون یه پروژه به شدت سمی و دارک آوردم! این کیبورد اندرویدی اسمش «Соучастник» (هم‌دست / شریک جرم) هست و کارش اینه که موقع تایپ، متنتون رو آنالیز می‌کنه و آنلاین بهتون می‌گه ممکنه بابت این پیام چقدر جریمه بشید یا چند سال برید آب‌خنک بخورید!
😁
🔺
کاملاً لوکال و آفلاین:
نیازی به اینترنت نداره و داده‌ها از گوشی خارج نمیشن؛ با llama.cpp مدل جمع‌وجور Qwen3.5-0.8B رو آفلاین روی گوشی اجرا می‌کنه.
🔺
سیستم دوسطحی سریع:
اول با یه دیکشنری سریع کلمات حساس رو بررسی می‌کنه و بعد مدل هوش مصنوعی جرم یا تخلف بودن متن رو می‌سنجه.
🔺
پروژه کاملاً اوپن‌سورس:
کد و نحوه کارکردش روی گیت‌هاب قرار گرفته و برای گیک‌هایی که می‌خوان اجرای مدل سبک LLM داخل اپلیکیشن‌های اندرویدی رو یاد بگیرن عالیه.
💡
نکته:
هرچند قوانینش بر اساس مواد قانونی روسیه تنظیم شده، ولی معماری استفاده از مدل‌های فوق‌سبک لوکال برای پردازش آنی متن موقع تایپ، ایده به شدت خفن و قابل شخصی‌سازیه!
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7664" target="_blank">📅 14:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7662">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUgM-RNiJvPRbxrb6kQl4tb_hTeqQr8_iVAb9N9ROjT3wV61SuqHbl4y-cdAaKTqU5dqZNzN8faL6CWA9HbiwCNB4q57H2_tN6yDTvkKTqcKn4gVhPjNMyHySZ5I5MaTB5FP3UltEr_ON4CVjVcgO-eKCxLNrQwxVECHfrQQDLoCvvk0vgIhTt5PLWb09hI44L60JF3QzfU59V_ffyc7WabToxsuU2WLITvKuHpMCKkk1s1b6Aq64E3rM_9XgdfnFuDg9X4uDnfyLPJTW1RQtEr84s7FenePCuKpLHSlC0qWM11yLYvyZcc-TqSJMFUDijpRoPCjlPKnaHfSfgv0vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طراحی و ساخت اپلیکیشن با M3E Canvas
🛠
📱
پلتفرم
M3E Canvas
یه پلتفرم اوپن‌سورس و جدیده که بهتون اجازه می‌ده با درگ‌اند‌دراپ و کمک هوش مصنوعی، برای اندروید و وب رابط کاربری بسازید.
🔺
طراحی سریع:
المان‌های آماده رو می‌چینید، رنگ و فونت رو شخصی‌سازی می‌کنید و همونجا تو مرورگر تست می‌گیرید.
🔺
تولید پرامپت جادویی:
جذاب‌ترین ویژگیش اینه که در نهایت از طراحی شما، یه پرامپت دقیق می‌سازه که می‌تونید مستقیم بدید به ابزارهایی مثل Claude Code یا Codex تا براتون تمیز و بی‌نقص کدنویسیش کنن!
📌
لینک دانلود / گیت‌هاب پروژه
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7659">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه
ArchiveTel
رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد
این ربات
رو استارت کنید
2️⃣
در چنل ربات جوین بشید
3️⃣
با آیپی خوب ترجیحا آمریکا وارد دکمه بشید تا سایت باز بشه و دکمه وریفای رو بزنید
‼️
نکته :
در هر گوشی فقط 1 بار میشه اگه میخواید با یک گوشی تعداد بیشتری بزنید باید هربار کلون های تلگرام رو نصب کنید  ، هر 5 رفرال برابر با 1 اکانت هست ، تمامی کریدیت های جمع شده تبدیل به اکانت میشه و قرعه کشی میشه و لینک فعال‌سازی به شما داده میشه
‼️
شرایط : حتما باید در چنل آرشیوتل عضو باشید
تاریخ برگزاری ، فردا دوشنبه ساعت 20
🚀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkdBpkb-Ek5F3ykyK5yzpH_BUSlcS1OE26FHux3XIIqID-GQnaAYjhmc3kU814tOH6MqrfseQOzPXZ0xH6qujx1AuTGW_5qRqine6f5smGMWriSCcEVRk4XWvIuVyWZUtxItXTtBcPQqXQEI7RaNl6y0N3GooBL4VjTD4PMVWFvuLM2DgCrHQmUnygoOjtuNunlEH-R0aSE_wetrLf62ygJh1GqC32X_SH2o6BpHVOej-U0azflWFPeCG-oH7inMyegZKJeWONezmiKdVJzod2Ra2CktDOaYwG8hIoXLE6XAvJHwkhQbX6-bHYCsbjcHXxNg-KiTIcn01OcpEGvPow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API هوش مصنوعی ها
💥
🆓
DeepSeek-V4-Flash-Vision-Exp | DeepSeek-V4-Flash-0731 | Qwen3.8-Flash-Next
✅
این سایت ثبت نامش کمی آزاردهنده هست بخاطر UI بدی که داره ، باید با گیتهاب لاگین کنید بعدش میره تو داشبورد و به ایمیلتون کد میفرسته و اون کد رو توی مراحل وریفای وارد کنید ( شماره تلفن لازم نیست ) حالا بگردید عقب و از سایت API دریافت کنید
✅
هر روز این سایت 1 PTS بهتون میده که معادل 10 دلار هست و خیلی زیاده برای این مدل ها
🚀
محدودیت هم هست 20 درخواست در دقیقه
‼️
📌
Base URL :
https://developer.amd.com.cn/radeon/api/v1
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL : https://api.b.ai/v1
📌
Model ID : deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید …</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWxSCwW2ezdQkhWaf0nEBbzodb2dOPl5gNP897nYbbECqHm80pGtBTYpByNd54AWpqOtKoieOmo4E6wmtnwoDfT8VyRNSOsxxxYrNjKDPmesLEfQDJAWahTw3SQEg809-33kEzJ5EJSPammufWMlkl4FCnGEq0wHPaNNeSjA3aj9dY1vtcM7zKzbHhK5pWYs7ToLedKKHCKLdNuSdh-6ob685vO7UVH0ylug1MfQTtVosRnRHQk7fSklGW04-Po7I1_S8bQ7m30nzvRtcwvXE_Y0a0uJOrWe3-fpm_rtNWTMB8JvAMRVDUndj18wKEFDK5XdWSS5UD3eSJ1Y8b3LMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به هوش منصوعی های محبوب
💥
🆓
Opus 5 | GLM 5.3 Flash | Deepseek V4 Flash | GLM 5.3 Flash
✅
4 میلیون توکن میده که میتونید استفاده کنید از API هر روز هم ۱ میلیون توکن میده برای opus 5 ( حد مصرف روزانه هر مدل ۱ میلیون توکن هست )
📌
Base URL :
https://helyxai.space/v1
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mefSquEElSxq-wrYiFE_B_NiSSWFDUnVjwRvLnoUPHVMgPnyQSlHli8dUhxM_c5dBKmlKsPMFfFteNsdq-ZtTmBPtN-FYpz7Tt1uJbqQFduGT6aIvSOwVbGdFE84atTvnZQFTww9uhslO0h6fooiLWbwcc3JurvgRxZZ4NldOJgWFDMuP-BXhLUOsYmzyzKbCgY36SxRFDBsYaCkijLKHkLI-MKvtCjO6ovAbpGxJ-T5AowEpVg0ftM5iJwF9qf7ybzuLjl2n4kG9ZH4rEleqUiiBB1Hu6MJozvRHtqajt2_oE71uo70FGeICbhi5rAIvRB4pa0zuNsWAOKaV8L-bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏
اینم لیست مزایایی که داره:
‏• جمنای: ۱ سال رایگان
‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه
‏• جت‌برینز: ۵ سال استفاده از تمام ‌IDE⁩ها
‏• گیت‌هاب: پکیج کامل توسعه‌دهندگان
‏• آفیس ۳۶۵: نسخه کامل ورد، اکسل، پاورپوینت و تیمز
‏• فیگما: نسخه حرفه‌ای مادام‌العمر
‏• نوشن: اکانت پرمیوم مادام‌العمر
‏
برای دیدن آموزش کلیک کن
✅
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlrHrUS1FzZX4FWOBxlnlC_AliA815lAguYzRXSV1WYbRXWecTxdKlQ62mRd4v2VKr3andi1VhG3BHHfoeEE4FMvCleEpAEMeLnZpg-lS_Ywg42g1QoRo0MzUWyD29r28WIEcSJw2Pix5zcXB2PF8I7U-tOm1f52fC859cYJKYXVeDEcoS9UoGqR1hfxoK5K2FK7xWNXbtiq9983Yixrah9cXON18eeqKE1jWVjn4C6gS7SNqVbgY7slDxrljuKXu-JihT0nzTlersGKXCY4435Ay_b683cftHYeQ_6vtgXEUvEAF9rKLHLmd-OJJVzxX3mCZa4fz6ct96-vJG2gZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
داستان GPT-6 چیه؟ انقلاب هوش مصنوعی یا فقط شوآف تبلیغاتی؟
🤔
این روزها همه جا پر شده از اخبار رکوردشکنی GPT-6 Astra و نمره عجیب ۹۹.۹٪ در بنچمارک ARC-AGI-3.
طبق بررسی‌هایی که کردم، این نتیجه تو شرایط کاملاً ایزوله و خاص ثبت شده و توسط منابع مستقل تایید نشده.
قیمت‌گذاریش هم به شدت نجومیه؛ هر یک میلیون توکن ورودی ۱۰ دلار، و خروجی ۵۰ دلارِ ناقابل
😁
(مقایسه کنین با جمینای ۳.۸ که ۳.۷۵ دلاره)
در ازای این هزینه سرسام‌آور، وقتی در کل حساب کنید، برتری خاصی نسبت به رقبای خودش مثل Fable 5 نداره.
یکی از معدود بنچمارک‌هایی که هنوز اشباع نشده و به نظرم بهترین معیار برای ارزیابی مدل‌هاست، بنچمارک Humanity's Last Exam عه
تو این تست، عسترا نمره ۵۷٪ رو ثبت کرده؛ در حالی که Fable 5 با قیمتی مشابه و حتی پایین تر، نمره‌ش نزدیک به ۵۸٪ عه
🔥
با دیدن همین آمار میشه گفت OpenAI با این Gimmick های تبلیغاتی، رسماً داره به شعور کاربراش توهین می‌کنه
😐
من حتی کاربرشم نیستم ولی باز به شعورم توهین شد
#طهلیل_ai
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eukGIs8cYlRCC92mEXtE1l8mAQneq9UTnCoysuOLqbb6iq1h0R2McgpnUEKYl5-kuymoofG3Askp9ydtKJbmb4kN1GRAaxE8qOfpQ_boVE-wxs2NZg-8J8uM29xiPxX1NX_8jXU6hqZCezL6dscSDgYVNGYQ6hGqfeIa7IUP7RoA_HlCKx4AiheGuICMuPPfRsDYvcMO3EHH2oS0zzmvtvr1fYwQpLoTBhYxhrjp59u-i3xGt4VvuElGto7sgRWtsxRnZBsZsed_4TmnyOyrXynXyGF_oZqT00gRAsiSTiGBHr6OvxKCA48pVXg2CaoO6MwVxo0laf5ycHijBL2CEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Free 2k$ model GPT
💵
📌
Base URL:
https://vip.9aws.net/v1
📌
API KEY: sk-g926rIr0SG7pfoD4WextkZwRRAgFOwYZDsG5hnDr8mL2ZH9d
📌
Models:
gpt-5.5
gpt-5.6-sol
gpt-6-astra
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFRmeakAILwLLGXyaRBoBm2J8ifikfCZ9GhHjMQeFLsp-kwkEKqsGFVecYdB3eRUURW8N590w0hBiFU2ry0mbDRU8J_ol3PO-gxaKZw15KUcti4k0fdPMlJS60YvUN-kgNQw2rEHiUpzCZwmVDUAE9xGMO-kC9edrshR2jAXC5BaD0Lii9UwLvN9w1N_w_fsWmjVk6qPFX5nAk2XCnaWWVErAeReO5euKqn7pTq89Z3dLAgWnvb525gxsHnSheqn594YIruK_g8lUP0U9zeFttwncy_pIiQqhxb-7TfBHiEtVfSgaAt7sTSnZEo4wpcFpJt5juv-E8an1L1HdPLtYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی آزمایشی رایگان به مدل‌های پیشرفته هوش مصنوعی
💥
🆓
Opus 5 | GPT 6 Astra
✅
سایت ClickUp فقط یک ابزار مدیریت پروژه نیست؛ ClickUp Brain حالا امکان استفاده از مدل‌های مختلف هوش مصنوعی را در محیط کاری ClickUp فراهم می‌کند. طبق مستندات رسمی، مدل‌های OpenAI، Claude و Gemini در Brain قابل انتخاب هستند و می‌توان بین مدل‌ها حتی در یک گفت‌وگو جابه‌جا شد.
🚀
🎁
سهمیه رایگان
در پلن Free Forever، نسخه آزمایشی Brain شامل ۲۵ استفاده برای هر Workspace تا ۱۰ نفر است. در Workspace های بیش از ۱۰ نفر، این مقدار ۵۰ استفاده است.
✨
⚠️
این سهمیه ریست نمی‌شود و پس از مصرف، برای استفاده گسترده‌تر باید پلن/افزونه پولی تهیه شود.
🤖
حالت Agent هم دارد؟ بله!
دارای دو نوع Agent است:
• Super Agents برای انجام کارهای چندمرحله‌ای، تحقیق، کار با اطلاعات
Workspace و اجرای workflow ها
• Autopilot Agents برای انجام خودکار اقدامات بر اساس trigger و شرایط مشخص
💡
علاوه بر چت معمولی، Brain می‌تواند روی فایل‌ها و اطلاعات Workspace کار کند، جست‌وجو و تحقیق انجام دهد و حتی Task، Doc، گزارش، اسلاید و موارد دیگر ایجاد کند.
🔗
لینک وب سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWAGOB_SoLJhOlLm6BxtPtfJ6HaONvTYUAbtR_in5oJUX66OTtgETjTjkunsaIe9RugK4vww9c090gq3_fHJEjJcDEGh2JwC-iTCpDvArnvWP2qKTtxZPynKb1c5XhxfQpHU2CIWYb7rh8vprVIp_tHjxCrszkmiK3883-Rx1fqGLK4qry7jy9TZQS37ZCClQUrWYFHpYqDd-SyLgyRmLdiR4GJy2pZjEz4IX2yYtdxVZTnVaCGYro5jA6WwzA1FK8UDNa1Yn3sneI88fBYxlwuZLyNPjjQVU1xdWdvelmSkLX64Ul5GIRRQk5IeAK-JLBLw2mWG5y9PrtloVioAXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های هوش منصوعی
🚀
🆓
Opus 5 | Grok 4.6 | Deepseek V4 Flash
✅
برید تو سایت زیر ثبت نام کنید و موقع گرفتن api باید گروه Free رو انتخاب کنید از این گروه این سه مدل بالا رو تست کردم جواب دادن ، بقیه چیزای خوبش کار نکردن این مدل ها رایگان هستن و کریدیت نمی‌خوان
✅
📌
Base URL :
https://kiosapi.com/v1
اینم کلید خودمه اگه دوست داشتید میتونید تست کنید ریت لیمیتش رو نمیدونم
📌
Keys :
sk-ZoCd9hc91if9INutCoTC6zA0wJ2pbrd9a75GQJTyj5V4gIup
🔗
https://kiosapi.com
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqU6bwjp3iygtJd-WNhuCi6YZwpflGp3cZ0yHa5odz5_JQ4Z2evIyPp5t-KkiXG-gXKKe_aMLefSwupgk0jKDVKctuWi_nzkMQPMM5P4WjVAmKYN0LKb5c26d-hd4shOsHWwLAep8V4l0xkEKJqwJgkpqENLDO9478ljJ8g12B5BDnA2J2nx1aA5CT5yZXH1rXFP10kFxmhi3pYz8_DApnrpEeX8xzEuDP7W98W_FdsNGANjXuZki-LF8eKe0OavCKOgr3fgEeKNOtFklmWlF4Ge7xpl_u_8_I00zMJbYOyqJ4o6A2pf4xPXl89izqMPJP_WhzvfxYaGItMtL9Igcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5000
دلار
😎
📌
Base URL :
https://vip.9aws.net/v1
📌
Keys : sk-faNuu4uK9WqIYAiXjdmYxeX6PI1Z5wNLzCsIXKbKVQ67W1rG
📌
Model ID : claude-opus-5
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwPeAPUPtpytMJD3HotftQcKDRKuyR4oJMU_LJYLbY-htIt4v-hx4XsAOctA1s1W7u9ys4qYGWUty2rboK8PGmhXymE870sZk28ndc9mmHg_fosLMZ7AmGUQvqOs3VZjhRp9cuUbi7r-EKhBmUXRH3tFMUG0TSCeu4ruZ7hpd9-CtWSOZyxE8-YCe1cUVDSJxnflCxR4ER_lQQC8E71unvdrTkfdJbcryMfgcLaQPd5p763ugDhSdNFpe_vHd2BGwiQ4fodjf_Ox0F_F0mPdijvhXuVuDU2E_Nfn8bW1dRC0cZ5aojSoh6EsWwfNEoSXihFWMB-mKxf_HFqfXucBUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ساخت وبسایت ۱۰۰٪ رایگان، فقط با یک کلیک!
​سایت شخصی یا پورتفولیو می‌خوای اما حوصله خرید هاست و دردسر کانفیگ رو نداری؟ این پلتفرم اوپن‌سورس رو دقیقاً برای همین ساختم.
​
🔥
چرا ZeroWeb؟
​
💰
بدون هزینه هاست: کاملاً رایگان و مادام‌العمر روی سرورهای کلودفلر.
​
🤖
مدیریت با تلگرام: پیام‌های فرم تماس سایت مستقیم میاد تو تلگرامت و همونجا جواب میدی میاد تو سایت.
​
⚡️
نصب با یک کلیک: فقط روی deploy.bat دابل‌کلیک کن، تو ۱ دقیقه سایتت بالاست.
​کدها و آموزش کاملش رو تو گیت‌هاب گذاشتم. همین الان دانلود کن و سایتت رو بساز
👇
​
🔗
https://github.com/faithsaly5-stack/ZeroWeb
​
⭐️
خوشتون اومد استار بدین
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtR4DhSxlSz9qmhW80sa1oavUtRAb973pPRZtB_FroDwp489npCEjgc3tX6gdBluJRjbaXeFDXDaBEuBdNycncTa9bBxzn6coBAgcRFVRm_GBoSehWPYE6uo4lhRsznPJNU5XJouvzSQp8eo8-hWD49rlOkrmstqznD-n4Oyq7K028tvPP-q0gcEND5tkn9YkwQppwlpEbX836pzv53ph12SD3goBAmCdqIeq5LbbVuB6Eh1Rm_ruot_C2QctZLQNwqZ40UJ1MOftGOCiB9VQFRAgBaM01KKKeKUNr90B3SYusRxqVKmoslbNW2QON3Jd_OBP6hdXItzWZjKy0Stiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM-5.3-Flash به صورت رایگان
💥
🆓
شرکت z.ai کمپین Global Build رو تو اپلیکیشن ZCode راه انداخته — از ۳ تا ۱۸ سپتامبر
🌎
⏰
دسترسی روزانه: ۱۰ ساعت ،  به وقت تهران: ۱۸:۳۰ تا ۰۴:۳۰
👑
کاربران Coding Plan: هر روز، تمام ۱۵ روز، رایگان و کامل
🥚
کاربران جدید…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7645">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lf7ul0Ka3pvFcfokNBHbDc4fV7GpdHj-M77n5oTiY2zCiKu7sVLd3ySXoMgjl3eEZdhBKILncvux_0px0Ok-0MyDgqoxcAj6rS7W3Qgn5dCOiz98Zf2WE-Jd6RgJAMm974iJxfKFJBWNcLGwDIfxRRtReNMv_YAm8wiQhR7OACWaCDmH0ntjqDr1ntzKEgoiOKWv7VrYTXhd44wuwZRioBrHUWPtlAu0QOZDlta7tI3kxaGfg-Z3zhjsZdHjHkJXK7lRDgvwXq-FGdkEcGDwC5eg34Lbc2Bwx2FpBta9Le1FnCkVKRL9HeaS3Ti6pcafU3qxeyU7lepgmoqlZLawCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1,000 دلار
😎
💵
📌
Keys :
sk-ByTi6xCfB7Pt1N8Hp9z7VdsRwGIMM5pdnh4CsorUfflysvbq
📌
Base URL :
https://tabitoken.com/v1
📌
Model ID :
claude-opus-5
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8X7ywmnNnmB34LiCHOZ-PwptK1hRJVtSsEe3dm6DEHXq3NzcTCtTavgDJ-d7XfdEKVJNe78m9p0n0NA1d8BR_ctexY346tdSA2Jli834OWucEajBI9V-b8k83OW-zn9Rj6fejZaG56YF8s7jgPaxXBer1S1BD4fCVjctv-ruT0yWB1Ycky75y8DNfjwa_7laKvsZvTKj7qpkMUjhAawSklTpWrCaCGfIaJXLL902VS3kRJJXvkkX3qxBaoa5sOLkTLGvIxhTmueAg_UkkKR7Le-uY84-7I9SfR3XQN2MZhW9SH6hsGPr3KhyU8VgG9Yp6gbZj4Qhb_IR_Yd6p8zCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqFGN8m9aNimU7zE1tY_xFtL8PFIVRlzeWbYrnwEwSC6LttTVQBy2XxSWAshTbGkn8g_XYZ8U-gBvoZ48e0DXt76mPWshEnzwTb1XOjVymgELOqmak_fK-3mrfh4bhDmAdq6Fo55oikQ4OJPQt3kqpel9QBeBepUnSWAg3q16uJuV8qvd2Ah-RRPSIQ6e0302JZq7cAKNsHDuGZ1kw0KgMxVOH-wVacrSSjA8io71CeaKodiWh30icX4E7R-h86IGxqxvJLjuJSo6NzzGRvfLVypctIfZPLvWrR0ZWEvPmoszFSYbwHa0D-ndpnmIwG-CsRPTsCifEyrqxEqRlptJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت هم به دلایل نامعلومی میاد API مدل های Fable 5.1 و GPT 6 Astra رو میده ایشالا که خیره
📌
Base URL :
https://api.experientiallabs.ai/v1
ماهانه 5 دلار میده و همچنین فکرکنم Fable و Astra کلا رایگانه
تست کردم اوکی بود
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svmfyXeoqHTigxKkFlKYRRFt6EJAf5JA8aaGIU1URrL8fjWpNJ5eXdVswkd-_OImBRsRXhSrCiPIu7mLYcZWr_N9T_2noxH0vrnYP6vB_H5a6LDTktnCU-1rJVzfLxyQ_5TPuNTj04QoWn1A0DJ27v2wECKVCRJirKi-pYlRAwBFF6xpBva_mRqrLBBd1TWjJbYW7zeRxmBXgrY333-G7Xs4hrN9oOcOCQhLlW-8IjGVZTQ6oEQ70pG3up7_LvrH4tG3zDYIVjhJC_A8Xi_Muhk59AZN2wPnSfP0SWmhDs7Ip8uBjFwBBbH-auf-zuSo8gEz9mqos2dbiNiWKew1CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=fCXGQ7AcR_YZojEDxFTkALnaCZ5hQbeZ_66vWF4m67WC_wahgRDzVHiWbM11stOVLuphuXPpDNw405QdLFnMW79u6Xyh_6yAMni5307XQ4i5Us5NaixUIDq5cC-umiHSgu_O1U-fEimFiLa7iv8jUkvL04xXJpkEGTS0Aj8vG9uZNnhbkVfgg-DIUHiNB7FwETWpGNzC0suVM0bEVPRLaO2GNzmD-eBHrFtftc6AnrXjaXw889w6HKT8UnHGVszHS2GjbgAH5qZ-f6nfQ9A-zTkgcNbqUVG7GACpalnSOl8PKhMUwUHxeAVVxO1VPIrlpZS1ABl9-GMa8hzLBgbzZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=fCXGQ7AcR_YZojEDxFTkALnaCZ5hQbeZ_66vWF4m67WC_wahgRDzVHiWbM11stOVLuphuXPpDNw405QdLFnMW79u6Xyh_6yAMni5307XQ4i5Us5NaixUIDq5cC-umiHSgu_O1U-fEimFiLa7iv8jUkvL04xXJpkEGTS0Aj8vG9uZNnhbkVfgg-DIUHiNB7FwETWpGNzC0suVM0bEVPRLaO2GNzmD-eBHrFtftc6AnrXjaXw889w6HKT8UnHGVszHS2GjbgAH5qZ-f6nfQ9A-zTkgcNbqUVG7GACpalnSOl8PKhMUwUHxeAVVxO1VPIrlpZS1ABl9-GMa8hzLBgbzZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هوش مصنوعی حالا می‌تونه با YouTube کار کنه!
یک قابلیت جدید به نام youtube-skills به ایجنت‌های هوش مصنوعی اجازه می‌ده فراتر از باز کردن ساده‌ی ویدیوها، مستقیماً با محتوای YouTube کار کنن.
🤖
🚀
قابلیت‌های اصلی:
🔺
استخراج ترنسکریپت کامل ویدیو همراه با تایم‌کدهای دقیق
🔺
جست‌وجوی ویدیو بر اساس موضوع و پیمایش کانال‌ها
🔺
دسترسی به ویدیوهای جدید و محتوای پلی‌لیست‌ها
🔺
دانلود زیرنویس‌ها
🔺
پردازش گسترده‌ی محتوا؛ از جمع‌آوری ترنسکریپت‌های یک کانال یا پلی‌لیست گرفته تا تحلیل چندین ویدیو
🔺
امکان انجام تحقیقات عمیق با بررسی هم‌زمان چند ویدیو درباره یک موضوع
📊
یعنی ایجنت می‌تونه ویدیوهای مختلف رو جمع‌آوری کنه، متن اون‌ها رو استخراج کنه و برای تحقیق و تحلیل از محتوای YouTube استفاده کنه.
⚡️
مناسب برای ساخت AI Agent، تحقیق، جمع‌آوری اطلاعات و تحلیل خودکار محتوای YouTube.
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAFwLhr5zu3SqvS69kLUVtwpI8nNm69AfYvta3_jp-iIMRyOmf884KKEdm4dUP0Th5FN_9fDjsZbbe1y1Vt7pCOlFqwDJp9l8rGFWmeJvgjPnBn1-904OoiokGCax7RZSiycFUBNSo3XURYCFjBhwoDjAoBD2fKtRjw9u5D00TNz-4RaaNwpLcLv9FgTel6H_7aG4kmtGA2XzRxbpq6V__45Zk3UQAhID2Ob5RKjywJ8SCM1Jv_ZINJGSPYxB-VqyA6VWWZFoKlK66Kx1xVqgI7Ml2gqGCU-TcvgbKRzogOYYH0kuvFIP7JwuJNHWuIwJz2pE6EQqiGGKpjl_jD9mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">200 دلار برای دسترسی به مدل‌های هوش مصنوعی محبوب
💥
🆓
Kimi K3 | Deepseek V4 Pro | Deepseek V4 Flash | Sonnet 4.6 | Haiku 4.5 | GPT OSS 120B
✅
کافیه با جیمیل ثبت نام کنید و یک کلید API دریافت کنید تا 100 دلار دریافت کنید
✅
📌
Base URL :
https://api.you.com/v1
📌
Example Model ID :
kimi-k3
حالا برید بخش تکمیل پروفایل و یک ایمیل با دامنه ناشناخته وارد کنید
مثلا تمپ میل
سپس 100 دلار اضافه دریافت کنید
😎
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🎯
چالشی بزرگ برای وایب کدر ها به همراه جایزه
اون لحظه‌ای که به یه دایره چرخان خیره شدی و منتظر جواب هوش مصنوعی موندی؟ Commons میگه این وضعیت روزانه
۳۰ میلیون ساعت
از وقت آدم‌ها رو می‌بلعه و حالا با پول جدی می‌خواد حلش کنه.
😎
💵
🎮
چالش چیه؟
به‌جای یه پروژه‌ی کلی «چیزی با AI بساز»، این‌بار هدف مشخصه: زمان انتظار برای پاسخ هوش مصنوعی رو به یه تجربه‌ی سرگرم‌کننده تبدیل کن. یه بازی کوچیک، یه تجسم تعاملی، یا هر ایده‌ی تازه‌ای که به ذهنت می‌رسه.
🚀
⚖️
داوری روی زیبایی کد نیست؛ روی کیفیت خود تجربه‌ی انتظار، اصالت ایده، ارتباطش با AI، قابلیت استفاده‌ی دوباره و کیفیت اجرا تمرکز داره.
💰
جوایز:
🥇
نفر اول → 20000$
🥈
نفر دوم → 8000$
🥉
نفر سوم → 4000$
🏅
رتبه‌های ۴ تا ۱۹ → هرکدوم 500$
🔐
+ 20000$ جدا برای بخش ویژه
📌
مراحل شرکت:
ثبت‌نام تو
commonsmade.com
← بخش Hackathons ← Join the hackathon ← ساخت پروژه تو بخش Code ← وقتی آماده شد Publish کن و تو Hackathons ارسالش کن
✅
🗓
مهلت: ۱۷ سپتامبر | کاملا رایگان
اگه مدت‌هاست دنبال بهونه‌ای برای یه پروژه‌ی وایب کدینگ بودی، این هم خلاصه‌ی مشخص داره، هم جای خالی تو نمونه‌کارت رو پر می‌کنه، هم یه جایزه‌ی جدیه
✨
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7635">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbBdXfklLTdH3TMl5x_JyObPdazSAC50VJX5I4sMWgxtZJnQKCo9HWXtRtx1uvN45oeYLhIILQj2mTMcEybsHDiyIZ1pyE3u4cRXDFiOdsNt4So8qSkofmR_dylvYQTRMtrm7RyWPQ5oeXU4-zC5qtSr237rAoEmDndWnhzCnjmwJwox9Z38IY6Mu02bnKcI842ahi2QgILZPqdA3_pUntQOd0TCKm2vvs9MOEpRjkh8MQiLuRIa7lR9r7_8Osd3uT1EB_5TH3gPt-YDbIWJVLldlIFe8rwbS4T0H9GA4RiW7x5--Y6DJpUuUuGFuLrclx1hRWflq88w8Zj0-GZcBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM-5.3-Flash به صورت رایگان
💥
🆓
شرکت
z.ai
کمپین Global Build رو تو اپلیکیشن ZCode راه انداخته — از ۳ تا ۱۸ سپتامبر
🌎
⏰
دسترسی روزانه:
۱۰ ساعت ،  به وقت تهران: ۱۸:۳۰ تا ۰۴:۳۰
👑
کاربران Coding Plan:
هر روز، تمام ۱۵ روز، رایگان و کامل
🥚
کاربران جدید عادی
: یک‌بار ۱۰۰ میلیون توکن رایگان موقع ثبت‌نام (تا پایان کمپین باید مصرف بشه ، با اکانت جدید ثبت نام کنید )
⚠️
توکن‌های رایگان فقط داخل خود اپ ZCode کار می‌کنن، نه از طریق API.
🔗
لینک سایت
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=vOwwAN8qnS8bhoMYUPcgdwoF_K8X9ih5xEFVBE--6k-CDoBjAtPp6nO03wVfH6TluveJ4BlmTLvI6ZUlzE_KIYqYfmvW0Amq1vAGZPPE4EY6zE0IX0iaeYAYcuZEnlaEOEf59Mwic0L6HUAppvNCji8A8xF-bZLfOEWjOgdLc28df9-IprU6KFXkxiStukYUyldxkOS582H7hNMGv_2rlxdBZGsj2N-aIAXvUOOLMA8j1xzBojdfRAZz4Hp97sS1-egohqyB8NWkQYNt86onNbGh4ICMmQLl1VNLkRF3mcKIWqD6teynF0g7L2WEH2YMmJcADQ7XMbBGAgwZXQv8cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=vOwwAN8qnS8bhoMYUPcgdwoF_K8X9ih5xEFVBE--6k-CDoBjAtPp6nO03wVfH6TluveJ4BlmTLvI6ZUlzE_KIYqYfmvW0Amq1vAGZPPE4EY6zE0IX0iaeYAYcuZEnlaEOEf59Mwic0L6HUAppvNCji8A8xF-bZLfOEWjOgdLc28df9-IprU6KFXkxiStukYUyldxkOS582H7hNMGv_2rlxdBZGsj2N-aIAXvUOOLMA8j1xzBojdfRAZz4Hp97sS1-egohqyB8NWkQYNt86onNbGh4ICMmQLl1VNLkRF3mcKIWqD6teynF0g7L2WEH2YMmJcADQ7XMbBGAgwZXQv8cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌍
Pythia — رادار زنده جهان برای هوش مصنوعی
ابزاری متن‌باز که وضعیت لحظه‌ای کل دنیا رو جمع می‌کنه و بهت میگه احتمالاً چه اتفاقی قراره بیفته
🛰
🔺
بیش از ۴۰ منبع خبری و اطلاعاتی رو هم‌زمان رصد می‌کنه (اخبار، درگیری، بلایای طبیعی، هشدار آب‌وهوا و...)
🔺
پیش‌بینی از فردا تا یک سال آینده
🔺
کاملاً رایگان، روی سیستم خودت اجرا میشه — بدون اینترنت، بدون سرویس ابری
🔗
لینک گیت‌هاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
