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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 19:33:43</div>
<hr>

<div class="tg-post" id="msg-7750">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کانفیگ مخصوص چنل -
سرعت خداا
vless://e4b11ac9-46f7-4cc0-92ed-bb9dfaaf3600@94.237.92.65:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=lkMM9FR-o7Z6NwmmQVK8rLhCQR1mbJTgjY_0upeS2SY&security=reality&sid=0436301fb0178b&sni=google.com&spx=%2F442987454d44398&type=tcp#@ArchiveTell
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 994 · <a href="https://t.me/ArchiveTell/7750" target="_blank">📅 11:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7748">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BAUjytIBLEg27Olf4-Nkjr-cJXuA4fQunPGLAn-YrHjb_tUiEpSSd2eoiI-iYJ8K67aghglTmaagc8GtMCXMG7yqMEDUMWPBYvdvRvz4dlHvZ_K1I6EzUga9EIDa4jWZeJVliE8K46uhJqjy4l4EroSpEGHeshb1BJCaTd2cImwmMSPULDsSxY5aDRmAUdH03Q9hGD5FreomOCQcV58UDekRqSwoQq5IUvyzB4aiOC0N6p6wxWEh9zeKv_m3vzDmeGFOxGpjf4PZzQgYVba6_ytl1_GgTDO0CTNwmFLyEOU-z7WNxHLMh4LWiHffFD4RnAtEqvJvjKpzJC87Gmf4Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
از تاریخ ۱۴ تا ۱۶ سپتامبر، با ورود به
Z.ai
؛ ۶۰۰ میلیون توکن GLM-5.3 به شما تعلق می‌گیرد، بدون نیاز به اشتراک.
🔗
https://autoclaw.z.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7748" target="_blank">📅 18:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7747">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7747" target="_blank">📅 16:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7746">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7746" target="_blank">📅 11:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7744">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7744" target="_blank">📅 23:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7743">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7743" target="_blank">📅 22:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7742">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rk3VyAt_mlvh9RPn9h2c8Ajm2YkBXp-bFtV7U3OQj6Mpt74pXrhgvC25KRPITyuz2d53E05vH43bK5sy23HyIGo6iAjz2Oq2SxfUthqrNx3y8s4iNatXk16s0G1fRHoWrri4B1zlz-J04WO4MUmA6LRfkZARWtP0M7nmP3hD3M6c0mmOaFipDEzY0PNcwDyBlhAynUb1UgQKtZnM2vKu2wJYEpP-MAjqmfrEo0I2pnmug2A4XQRF7wmwEorWf-Gdh7e3Xy5t2HMndvPt_lifIFgWA8Yo61cRq9OiLRw5hCjwmuUoG-HU47ZIJq6855dJnkSCzTi-fpNP5J7XWeZ1_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی به Seedance 2.5 و سایر مدل های تولید ویدیو، عکس و اتوماسیون
آموزش
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7742" target="_blank">📅 22:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7741">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7741" target="_blank">📅 22:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7740">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7740" target="_blank">📅 18:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7739">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7739" target="_blank">📅 18:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7738">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7738" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7737">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">1.7B token MINIMAX
url:
api.minimax.io/v1
key:
sk-cp-k8fnOYl1xeWGiSNy7qWxNP3Gu-nkuMKLaAFl7ZoCnGiqA2sabKF30eMTQNurXcyGtgGdbM168WEvBhyTOo2WQaE9RoXzVPAyyG3CYwZuybXzDILyBEBc5nk
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7737" target="_blank">📅 14:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7736">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7736" target="_blank">📅 14:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7735">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7735" target="_blank">📅 12:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7734">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7734" target="_blank">📅 12:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7733">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7733" target="_blank">📅 11:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7732">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7732" target="_blank">📅 23:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7731">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0_o8ImP2b_E-QjaUid1oAgsNU_ekbuPqqhXD5sBQ9_UR3fJ7RkQIJtPv5UNaWCW6cdU08h8eWQ5maY6_QbsGUan0hJy3fCg0d8Jht0jz463dF7yMJoPS-E5UccMhRZ7QpnkLxc6LHFtjwznn7xnRO2egDy0cpu921vMKSGlA7Gxx24qr3oWxq9SULqgvvKdPec0CACAkRFN84gyh0373fRVUQFc0kx9eEBfEn0ISWOPBTpRxCvqTcDPwZAOBnKJsYQW_R8R2f_hn5TWUcZ_r1w6oEObwmLWnU9f9kbc1WrBFzvto2XfLEXxcWMl2LPjIynd8OA1PDGw2TR6BiQIAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7731" target="_blank">📅 23:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7730">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WooyhMVaBFbntO6QZaogpdniArwgG6MAv_w6wtpjs3f7G9ltuJJzZ1H6SqKIN8ChcmD3sdG0lyNjXopNO6SkmEnPaY9tFAzD040l7r1HaMt2wiW5GedDegD0skdyDwR6mrambXSLGGVNILIgJKevFPilHyfT87536VFWVNtpFLBpfDzYX5in_wfFMsl9HMGZPFrJWCp5fU7sBT0q4ZnAF-vLE4Yvl5Rn42lohMYN-9TYGKEThSPfRvsgF5vlcDuA_BDk6s46gEQxSi_PpRTkJ4kIYnZCWKeIo9xohdzGMrOmsMvEb2P8QFEfHnC8wzHm2fFpRSJT_2-AphmAR_E0oQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7730" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7729">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7729" target="_blank">📅 22:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7727">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7727" target="_blank">📅 21:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7726">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7726" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7725">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7725" target="_blank">📅 20:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7723">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AB40MeZcId-jUWG7s71cg6pBVzGpJHub8orqwWuAbXLKxcypm5nzrFOkJKJkYeL3zW65GHJIzAKtTTaV9qBjjUuEn1DVUIHQ26j1qQEk2cGxRK3M6aFSEsqBSO1H5-CJVTWZlbGDErTgyj95MopN4RT_EtqOaQhw4A7f6KZyFFUPY5tBc53NcucoYQxdH41rsu2sdzDmirThjVc-Y_RBK1tp_1kEFoSMQXfToMRpeqNWt28YOSQwXmeS0SrJ6nkC6oW1I0LWc_HHMYSX0XjaSTtF98iGRjUmqV_-ykwyUl9UDAVzwNDSA5y15lGH_CFCtztDAgTmGnBnVpEprgFCdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7723" target="_blank">📅 18:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7722">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7722" target="_blank">📅 18:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7721">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7721" target="_blank">📅 16:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7720">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J6woofoz5iha7-vBIEsD9VAJoB1qtPWFlYal8WBEht4W9KHvFfPXL61FKQ8x_IgG2_cc9t1uBvMJHuAGtxF7N8WYIS40--4-9VqiGJc-69ZNiCQcX1eZeXNw3RlpgHBw14xrVk9P2Zal6kqvnJoVldEoufRv3DwtfKPOJ1IQEQ8tq0B5a5lrlgUL5ep3BayxvmbChy8Sg6PeZrKR0SkmsVVOEdmS8yzwnEOhxGuYGaJCnGj6KG9yHlQzvJx3vNLtg7Z008rz_D5b6mMH0PxPJtFdYG-6M8r_1i1_RBRmjMyBmRcs-17_XbghL8cNezGrnHtr6b_RPQ6XdHtLMuDXPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7720" target="_blank">📅 15:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7718">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9GpdxQiigrZ3OBAMFzKzfGBBOcx1nT1aVzaCJMr8W8RVvsDXN1n8nxzpL5OvV8KwrCqScn0rIWyPsRuf5stB9mIeTmMCbosxwAD1CQD6HGzjA_Ap79XXStp-jKvC57CxgM2dS7qWuOdfsvs0QpusXYeYWXSzNf7ru_68bX-QRSRuE0q-36GgrHcjsj4RktfSIne0fe5S67le6EZjSnk5fpLC59hVLxuP9lxXRy-htfqVZguUYs-S7kRUs6VfHcZSwpAuBRCggXdOzLuIcB9273bQDbRNmisPdqEqlmbpjZlNujdeAgttSUfiFFUGqP6LEK-5BnwbGmQh6SkDQxlCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7718" target="_blank">📅 15:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7717">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0lfXm7E-F_y4k3R4S79Ox8MWLZeYHgmo8_IBBsrbAusvXh48BHP7JqdGSs_LB-Zno6daPzLhHkZ4F2iKOHfchTCq7isl3lH_06-c_xSHguc341JqULAmfjySLx7ZkDHAKl-j4P3XVOuB21JhkU0k712bRJdU_TgkTbmHkTcSh5rnnANbFFFhxmuX0lLU95UAWkvAsiqshF2I-lNQeL3d2kgguYU9FaTXLu_5FdaVE3WnYLy11pQGiosNB4RX12f4UEOZ3duS85WrzYn4ixbZb2-Yqgc-najD8YSgyz4c0ZrWJfmFMswWTlfihVcnLVTlABxVGr2ooArabjAzNdv8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
100 میلیون توکن GLM-5.3-Flash با ثبت نام در AutoClaw + ZAI
از تاریخ 14 تا 16 سپتامبر (دوشنبه تا چهارشنبه) 600 میلیون توکن GLM-5.3 و DeepSeek 4.1 بدون نیاز به کارت و همچنین یک کد تخفیف ارائه خواهد شد.
این پیشنهاد در
اینجا
قابل دسترسی است (در حال حاضر شامل ۱۰۰ میلیون توکن می‌شود)
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7717" target="_blank">📅 14:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7716">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shtuC5p6FCPIj3zDfTab2QY3hZbwXLab4lvNGQVgT2G67hYHVI4OlvxukC2TSBKNH52nmQZKJdEDDyb7qIEVrf4r2RsVs74QvrxJdDlLS5GtusvFLUUUrcCIZJ2qEBgkVEcdLcaSnyDs11qx4dGklqkfdxw57ORE-6VIEb1xAFgd71jduXfHxDNAwPgSd0OwL6gNwe6u4HnNCTS5Xh1jZdTUpPp4YsM8rPdtjbTT9yCWsnbxz_if4eDZJwhMdhyLROWSOM2bDviA1g5tswJMJeRsuUo5wjTS-JCipEOf6yw2P2caG2rHMVDc0JH9s28Rta8cTjAvLFkHIO5onEnZJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7716" target="_blank">📅 12:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7715">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seVPmMBW1iuIhFjAfLj_BwbpCOYGpG9KgWD6DoA272OAwXbfxE3S_a3D2_CVbqGWICEsMZBazuWjtm5Fyxt5dnd3zHoAwmbLJxfLGv9RegVAobzq1Qmro9NZtCzqCT-g6LAV8UznAUL3yP79zIXcOGuywleO5KMPat57YvchPUKN-cFVVY3FV6UKJqlYlraMegyZN49_e8DLyJZdSSvv7OgljEqQFO-y3IjlJv2BE8hcFxwQ1VslcAI0Q3ocjNw-8zsQYS7bLP62z9_3_lI2GLFoZv4TiyJQycfrG_5eNAYhihrHzyLUm_wkx4DpruSDj_5PJi43ONP0FKEN6SlktQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7715" target="_blank">📅 10:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7712">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCbNuK7YyyEzHHhVAguOjrB6tpAMibxtY_fSrES8C04W2eFo6W0V0zfX2GQ3gEhFP1VZFcumtv5RjFiEPvD8rkVCtnwQr-8BSV4d3DAliCIkCB54DjKMfCFFYoOM0hIdVjhGZLtQ2bYS_GHG6DRCxhbd-MjU19eqrR3fVZ_e01QW1TWkzOt4ybT4GBR-B4OOJi_uxFlI8P2fSVNO0bFlAu4fZFNf_XLsyFYS_NlxGLk3yztE8_pVTGR6jDhtYvmCCNHTEPaEH3-9pxXJYhETGbrHtCoO___l4WRaJu6Y37rAnPcDW4k1-S-tdQE3OS8pYnfMKbL9wogv6KDufaemVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7712" target="_blank">📅 21:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7711">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7711" target="_blank">📅 20:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7710">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است.…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7710" target="_blank">📅 19:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7708">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل: ① به https://arena.ai/ مراجعه کنید. ② حالت Direct Mode را انتخاب کنید. ③ در لیست مدل‌ها، GPT-Image-2.5 Sunburst را پیدا کنید. ④ به مدت 72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود.
✈️
…</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7708" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7707">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت گیت‌هاب قدیمی داشته باشید و از طریق این لینک وارد شید
✅
🎁
با هر رفرال شما 100 دلار و شخص دریافت کننده…</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7707" target="_blank">📅 12:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7706">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sde6z4JfmgxMF9tY4UPYuExm7AO-Z1LaIqV-RPRHesIxsPG4Z629EEP_D6NiSx8UUTogqsKocc8sji1dqlUtRgI1NoNe3NeZS3JPSm4jBWdfJ2m_WtXm80eEX4G4ORFu6enejW_3DuL4iLOyltYL7-BaX5Ff20hLJgg0A_pFfAfq3AmLoB11VG7TWRhNNGWOAnmoGuK6prP97IjAKIu9QrKxXL_uA219zVPPRlSsIRK7lN474jJD5gsbES2k_jFnOmbWefeey7AeOFGjuP6_OjoOs4GkPjYmzDpIsw4mg-v6v3Q0LWMi7a5OYy328KSt4ldFgoKKgc78VxCL06SgWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7706" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7705">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5AYts7M4gs_ejoiJopFwB1p6cM8HLyDl_xKfIgSEY4jShShhfE4eSlvuqO3ChM0q0vIyZnFF3OkUbv0oCmTOFfPA2fXQjW8ymq6I5AlgLoI1TWDl8pWJXNPNRX_WuJBDm6zPLly9J4r6TXhg419J9VXQwUH2ihq3V4WPORNhh7TqPQvzJG77gDo6OU2MT6ObI7mSA0yqk8KyYsK1FaqL50H0s7NgamOXO7UOHVRVr8E_HmAPBSHQ_L4nIbjtgcXJbjyNBqaee-09bN374HB3YpPxjYlz83o0lQvoRUZIY0VpwChd3cT4ZVME5AuyyWFnBW_JVHUTVt-6uv7C_NnFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7705" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7704">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apqXnCgMfDvASocX0qPLcgx7SS7kjqnKC3zakAZ8w0xTa32p2mwiOq1jGyNFmnFNr3pqk30RGerdhDzHIDg7wIblka9Q2L_gQfa_6Ir9mVAk2x6TbqCmP4knhs1fTZbctt2BoABSCkkzv1g7IZW9jtvkSROMGlU6DNvR9ywAnwEeI0YwYPUQHAnfhBUTZxAPinvWLLcUdwWNCzr8-b-WOC_CnAPJiWBwCNNT6eFQAS4GvN_F6OrIsGlSpZkUcRLGKK9cg0TEDHWfjFsgn3mOKkrIAdP6-KEnHICkxIPcZg8TbJOZasX4aVrN5bhXHClWHlhjrtIP0xT2uBbTOlX1YQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7704" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7702">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5avpldFKodDfuOlph9OWzBUqyIZRAebHFhv-IPUJClzpVxZ7PZKI7tl_B3zRkE5yJFnYSrACv_lbt6m4PLBzLl8GThv0LPaszeles20RJc50lcmKOBnqSjTtQ1m5OO7ant8bJJ-wD5MuJPOSupTeu4VTVJp0Irpko0C3NiyAhC8vJjpOxGtxU8q-jq0skCajaUfy7dDQju1iMHM8yKH51_wKIeaeKJQcAQFjrAqec1RR1_z4kVv51ldnRPDzljldHoWSfsy7YzfCLv06lGi7IOqNJDRSAUTEpytiTQz0DyO-BQWMFVUneIIoWA0vULa6-RcyYjjJW_C_OiAvf9l_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GPT-6 Astra
1 Day Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=gpt-6-astra-medium
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcpjbJuvX2mcVGGkVBbQwrdTKkzLzWmel2Njxii3bbsHNU59d3vvulgPez_c_zPBP4nvm1CeWgqCD6HCPO2PqlGjW6JYrcb4dROyEygcIx09jVvFXzUe1pYeECFNyJER3zhWkw5In6P-iDu4yyyrYmdDqxo7Z0zRobOilcVR5X6H1mVUN6sXFCcpJM4X1TLvZJp-gkvymziE7MI7UubPb06hGaPXxsRVaxHW91Z1d7Xip9Rd42cBBRCO0jyN7DaLnnXSvUGVLI7m3ML82cPXXQcDPeJZE4XONpjtYaRyRYEI605TpXnUmvPdAns3HdCmMICmgwW8TTCfGpIX-1DQTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7700">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgLo3hWh0cZRQQHFIOSgUTqVvgHOWx_EqCDYFuW0PXOkgjIIxkGFAiJgOmrdtKrUAIKdVixwXiezJFMoxdwz-zfRrliJfelqM0gfx_jSTGWvEgEsnUlf2B5JhvIV_dTCK9H5lzmhoyiqh9IAW4Cqj7gkvXq0n80Lp_I4-JYAG6cXqz4RGjFnr_xfWlPdlYVrHovxrX3dJ_ddU8RW64v1mF-XMfuPMH9VZxG1sokCMmFTLSegOZnzB6wRFTcqLQm8xg5UFTDlTsW6kp8IbWrxky2tY3FX3lnqAdKb_9VJ8y4XAJtUDpuSqAxxgFtaBlA72Sq3IrIKs0F9lJFEQSiIgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEOkQ_6hTlFaWlicc3dguJ5gZLLTbX5UxnR1TEmy3WVQZ4afbc2wleUpQvD14tcvCnlCL9RmhiEIxop8OxtVPLdOV75Te0Xl_HezX7DZ-6h8pixqRVLMsgt2ms8Du3VphpARWFzqmMEvVJBLsSpbP_PjGKFrt0RBRUaI_yx8gFpaXai8zbKzGqVff5jENuFjhwJmR9jzGlJhJl5RLfuJxqACPpzbiNeiiV-cs_AnyCIHDG_V3ljTBWYaMOXndE3GbjL8Mw69vtvi6VhOvTR4H8_9DySH6bmBKn4xwFpP6gH5LUbLl_y0NoR11ueTm-YFTvr4RaZcWl82OlW8UCEVIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIfDxV_yu4E5TQ1NFQFmRdlSXv_kJwA_y3nDqP9t4vEG65Yb66TlGQBo22e8nNfwSaOT2juMOdT94zPCVBsPtB_vRgQ3p16UXODdG9Z-yvS5nA1QgoSSj92R8SXZKi0NejllPxxjffxXy9LN9cI3z_aGdcAg7IPSmHB-Cs3jV3d9zG2P-aPOV3-QJb3uzl8JZ3MqNb8crO0ntuzVJ4AMFsZ0wvjIoEZ-ioko5JvlNDatoDnRocQZ6yz9-H7-EA4XYX-oeixrZX57j2hiWrUsjbmEv7xDFaf4RNEQn1rdCfLQjs3KkKjsKuclJSyDgTfpmup-OFTUHIMLO1OGHj7H7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGIdiDqEkHABPNuOkDspX-iCzvB4DBuxTsyTU6gikuhsSdXbUO3Yqoc4LVN7KsVquKIh0QHdiNLZSptW1Px5OTqnNd_Tw4I3fOWRzvafJ0xV3GafeUqALJxAMEtzvHujki5YQRxklkeOzcnnzSeEHc5ePeTn3YabYZFIOUjuPA8cnc3Ize_m0vl9nvT9r_5iZcpi7k_3M5Y58zc3i4qLkMD3xVNZxNGSV2Wawib277wkIY0gYHb1_vPXXdPjjdxpJJlmG73BvFLGc3NdrGPIU7vI4vZfkz7VkgEnpyG6sxatnspBKBK0ZoGllukuMFi1iFafMAsxQ8KRSEzZdeEBvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=nOQE1qcVwMTYPPuyYLk82U9iMqP7LMW4nc9ndjpjyAqjNMigTSsDg8pNsRTDFSaaXdCMueQ9luKjebvyB7gY85VUeNMqkkp9UrLrTxnZjh_OW_hTLbrBjATvRoSZ79d9Xyxf7EYhebO0MUjTkbug4NTW30U7fHxHJFLFQWPnS8qZvcDBmbvbA6eefnR7vwZuTVxwQ53x3oR5BrHFI3GrdNRBVkmixAti5T6u30Wjja7jTooAXtrtt48l-WzS1XJl8StkO8a3cSFfHVyp83E5YWfD_wgtXytJ7QHOW54VaeuK4WLSE01kARrzPocu3XhBLpA-fCO1UWo_kPx5IsDnCBg-jwgA1fMnXKqOXRiLp19PdLI57XO6PTm7hYqcdxX1LKk1MswwUPHtVeXRE1WLV3lkxThVOZBTj2Bv01-QjnDSyAPmrDf6381rhZsVxSTUhvOlRMSGTE02gIPSbdf1fkNt_MNu1O_HzAKMJVgWVlxxZPwjbHxATYDBWeV9twuFvmmWgpMB21fQOR7SrjsLgBXBed4KiXEf9t2EDU3vzdUXuvYcF0ahrMtQZUdgprYHKrBFunRrZgMOL4F3C8GSPGOOidhdYWQHguOj0YyMWZfStq-QVDBSKgBPp4vkQ4ORC55Jxl3LywAqxGbL4rrDCUU2KBekSXbpSKqCA597nZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=nOQE1qcVwMTYPPuyYLk82U9iMqP7LMW4nc9ndjpjyAqjNMigTSsDg8pNsRTDFSaaXdCMueQ9luKjebvyB7gY85VUeNMqkkp9UrLrTxnZjh_OW_hTLbrBjATvRoSZ79d9Xyxf7EYhebO0MUjTkbug4NTW30U7fHxHJFLFQWPnS8qZvcDBmbvbA6eefnR7vwZuTVxwQ53x3oR5BrHFI3GrdNRBVkmixAti5T6u30Wjja7jTooAXtrtt48l-WzS1XJl8StkO8a3cSFfHVyp83E5YWfD_wgtXytJ7QHOW54VaeuK4WLSE01kARrzPocu3XhBLpA-fCO1UWo_kPx5IsDnCBg-jwgA1fMnXKqOXRiLp19PdLI57XO6PTm7hYqcdxX1LKk1MswwUPHtVeXRE1WLV3lkxThVOZBTj2Bv01-QjnDSyAPmrDf6381rhZsVxSTUhvOlRMSGTE02gIPSbdf1fkNt_MNu1O_HzAKMJVgWVlxxZPwjbHxATYDBWeV9twuFvmmWgpMB21fQOR7SrjsLgBXBed4KiXEf9t2EDU3vzdUXuvYcF0ahrMtQZUdgprYHKrBFunRrZgMOL4F3C8GSPGOOidhdYWQHguOj0YyMWZfStq-QVDBSKgBPp4vkQ4ORC55Jxl3LywAqxGbL4rrDCUU2KBekSXbpSKqCA597nZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=MgSQUJ7p8ZPdj-aTHheyNfsnZSwTHnsQGTLRgxgipPv1of5b2YcxTt0RzxqG8xTn2Ucn2e0lYOmHgK4UwNcfqcT4tr1SjzqzmgCsC-JMISj18RnCFklryvpO2R62eBpPOzVha2vLqxoHPlRNjy5rNCn8vV9E23rfaNCgqhSA_x3tYIgJJOp5eH4wOKtrZe9B2HfkuDz01271KM6nTnB8arV91vgcraKumb14OlQIVTFWECpgPRt5Tz7rJm5xplFQFvRg9r-Q_Jw1Bsw8wtwxxAtK-Az5LXzmIdVjVrGpiRt_TqNiPiEX30Fgkyf_Xpoz49jUlm4DEtT-mz3n9BDCNXRT1gITbKoo8ZTXpglRracWR_CPapUUPi-zXlwfEeYDcGT-GRjUzq9GjAYAL6MdDLLzUvY0XuF8U0IONVGVaqJ637dn6bNk4Aj5T7VZK8bzHtWeMgw9XMVm5GUHvugsfbbDP5aS6NRZWyU4G5gSjfQ6eTllDOdnRT6njH5FlcU_HNdf9Kv-O8rJF-cjEMpSb_9t5SSfFqwZd1H4XpuxXFbUnhkb63HAKA_UO6Rbt7UyQRiQdMBegsFGhS-vrm0TjtjzjIkUSHGVwnTuy7T-UsVSVxxq9REOGYresVGQqWWm7QM7MSpkVdoduLkBnYcm3AQSOjFwR8ZdwMOQ8MwBj6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=MgSQUJ7p8ZPdj-aTHheyNfsnZSwTHnsQGTLRgxgipPv1of5b2YcxTt0RzxqG8xTn2Ucn2e0lYOmHgK4UwNcfqcT4tr1SjzqzmgCsC-JMISj18RnCFklryvpO2R62eBpPOzVha2vLqxoHPlRNjy5rNCn8vV9E23rfaNCgqhSA_x3tYIgJJOp5eH4wOKtrZe9B2HfkuDz01271KM6nTnB8arV91vgcraKumb14OlQIVTFWECpgPRt5Tz7rJm5xplFQFvRg9r-Q_Jw1Bsw8wtwxxAtK-Az5LXzmIdVjVrGpiRt_TqNiPiEX30Fgkyf_Xpoz49jUlm4DEtT-mz3n9BDCNXRT1gITbKoo8ZTXpglRracWR_CPapUUPi-zXlwfEeYDcGT-GRjUzq9GjAYAL6MdDLLzUvY0XuF8U0IONVGVaqJ637dn6bNk4Aj5T7VZK8bzHtWeMgw9XMVm5GUHvugsfbbDP5aS6NRZWyU4G5gSjfQ6eTllDOdnRT6njH5FlcU_HNdf9Kv-O8rJF-cjEMpSb_9t5SSfFqwZd1H4XpuxXFbUnhkb63HAKA_UO6Rbt7UyQRiQdMBegsFGhS-vrm0TjtjzjIkUSHGVwnTuy7T-UsVSVxxq9REOGYresVGQqWWm7QM7MSpkVdoduLkBnYcm3AQSOjFwR8ZdwMOQ8MwBj6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twp1a7IFi71CNKDgTFLhmYHbPi-ROKw_vlIiDNggaESWG9CDGRQYQaTQJMa4__JzUPlinatlSzNgGrD8EqttRWTauCxtnazKA-g3F_In0C9_AYtS35pSyP106TWklFsewxLcwB5Viyc1e47yZF6iiB-iwpgtirwEGAAgSDfMYE_swosY9oPer2Dy4-WpwuD5LVIR_f5HGASy2pRhrIma4ETGlwCPROo5ksk-aW0Rl3aMTNLJKZoU74yN1OeY7mcfA009cOJpMtwqJ716qp7v1kXGd8yxxbj_006TbGwrnaotWQkiHgdffZ09l7DDGKE9CshbM-_M2ADxofOIvuLflw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=K7BNfCnWuXtnKmMoot2I24oRPFIdCFMHXzdlc5-ER1o4gBXVB-a0JfhgF2x869lrC2UPAmYPKsnE2lAtxFo0RaTiKRL4_DYdy85wB8dCREHLUyIV8qYx0NUfWHakqCJ6D_68MG_ohLYLH1sZTWHdwDSxdY9MN8sVRsig5FZBoZ1qw0rKx3E2x7DlGz7oUbtszkL4yJ5XtVroJE9VJ7OHU4AJGk-2yS0fkp2Fk5bUm3jK0MBh_Y5emeE83SPPc5t8hxkzFwfEB2idN5-eJrZE60GvF7da4LnnhfbFd-Uy_UWApRvK6J4sAjBnZ-VoIzNNSxdkdqmDuyKgdLyLYrLblg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=K7BNfCnWuXtnKmMoot2I24oRPFIdCFMHXzdlc5-ER1o4gBXVB-a0JfhgF2x869lrC2UPAmYPKsnE2lAtxFo0RaTiKRL4_DYdy85wB8dCREHLUyIV8qYx0NUfWHakqCJ6D_68MG_ohLYLH1sZTWHdwDSxdY9MN8sVRsig5FZBoZ1qw0rKx3E2x7DlGz7oUbtszkL4yJ5XtVroJE9VJ7OHU4AJGk-2yS0fkp2Fk5bUm3jK0MBh_Y5emeE83SPPc5t8hxkzFwfEB2idN5-eJrZE60GvF7da4LnnhfbFd-Uy_UWApRvK6J4sAjBnZ-VoIzNNSxdkdqmDuyKgdLyLYrLblg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uf7BWbFRq3jDMXOc-eO0aynckvbEVxzGE3VIaiRibr5gXN7IdTuYb0BdfXNx2CDp5IrolOY8sSTcXv6mTkL3SxrhcIeYBPIwXW6U85OYv_xALekbUn2tQQkPpMpvTI5DItS-rXQfmupap7moxTEO3hI0_oK2_ldTBdbsABZCVrRUkDxeWxQLkfFuIIRwTwIjHGyCrS0DnlvmYOU0V0GTjzZvtSDDIy-Xsn_VALoMenMP2Gy3ROqzQTB-WVA2c8xT1JsdpPYDWsB47ha36Ow2WiEdpqorwNvWPE1J3QLbbTuijkML1sfOGvZ_xuJyy53Q2J-JwAQg8QUf2aBA6uX2Pg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7681" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7680">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=rIm4D14pVpSAykNw5tlGHwuXqzOtD0w4pcWbK_Z3fKBbF13fCPTLpve5i57do_OaP8c6hXDKpPCMTM2cPHEz3bbh-mCKDF5Vq44D18EVy-_bCHH5lX7-jwF9bXDirlzIyJS6xQ21B4oQex0nvZ3XbRi3ymCLCcUe1GyOddfAl30v0i8LMB33pKproCt16HB6D7LwGOoI17kpohdZpMyA_K2OrrMPv6csxw1CgVFALKa0fOA3UMLp4LbojAvQwqZYDp0XdXReedud53WlzF-J8EukwMKURsRzhXJsDZCTFz2tJF1UzOwaPyM6K7uMWK2dKx3BOcIq20WdT92Bb4txKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=rIm4D14pVpSAykNw5tlGHwuXqzOtD0w4pcWbK_Z3fKBbF13fCPTLpve5i57do_OaP8c6hXDKpPCMTM2cPHEz3bbh-mCKDF5Vq44D18EVy-_bCHH5lX7-jwF9bXDirlzIyJS6xQ21B4oQex0nvZ3XbRi3ymCLCcUe1GyOddfAl30v0i8LMB33pKproCt16HB6D7LwGOoI17kpohdZpMyA_K2OrrMPv6csxw1CgVFALKa0fOA3UMLp4LbojAvQwqZYDp0XdXReedud53WlzF-J8EukwMKURsRzhXJsDZCTFz2tJF1UzOwaPyM6K7uMWK2dKx3BOcIq20WdT92Bb4txKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwOxjwxpkuTppSAYRmQXP_OQUXXWQFJeuqsTG5FFpujwCS3xCurrPP4xhVFxJiPWkWnzmR0K36JFdp31bzbKSnjjKHBhPhanOJv_bOEvEtBo64e0bDzKwCxPms31gJRoOlEeFgHdr3UcJVP3rheEqS5pvFfN3N4TmUMlFAfZuNF8_xJRFGzkRiK_TXgEtResYb3lADP51IZiNZCparyW0H0KEq8Zx0c0SJwQrYZYcO3kNPwEjZuGY3tvSqFx7xBkzWVCu7tnaxT8xSlQx6-rGaPwaaETYdepR9ro0O1HzgdMSzWfG7RydoaBtECryiBk8Xh8FCmwXTQayXntLJoH-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFJ3PNjQoxYfErk7wr48X1kSx8xC7Cd6ztLKW3WFlXhIQrjL-T4XiPLKqGlcNSQ6BwSL6Apm69hC5CJj888dkQkpcaTpk08XCluexS_28KqDcZXrvlT1GXpghy7PW_A4AmN0DsdQSfecVlYzPNZP7u4OcxswFOylfUHZJnIdpq3P5T9SJbELsesfqIcTIcHPVUTwNPSJ-1_csUY99qzA-dhnG2uxWkSY0XUcasMEgBVnLWo7MhjvQs01PZoXSFQ8v6mUCCfOC1lbErR2QrdkUnCo8Qykd1LbjJlye8Y3yDdD_-fWRqAaTVHAAw6b1UnppsGdu8vlWRVN_TD9im6acA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZmPpk9Hwgffwo-GvsQjMXhDNz2WVKxFKhX0LjlVBW3zmjYvTkmoun8fl77s1nQyPAML-KUh-ETpP7BjYbYFCgFqDnnhIi3MDIo7jKCO44wp1rjJzhOOm0s4aGxLMxXgezhMHjJQ1xETUlLCAPDQCJkYesLnPEdDFoUn4I3LRiYmNAoimpNnbH1OXsin0dEhBspSjFob82XHm4hQlht-7cMRc9DiH8inSojgU1GiAH_WXV4-jH9IBtZ33ER6Fe6YsQLJM6_GNP2AfbyDYst2QBHdSYcx5hDOq1Io9Pp-3vRmyqVqQRv5IyAolvgluLeZqtWpSHMBA0yXyzgqBMfpsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت
یا کاملا رایگان باشه یا فریمیوم
با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم
اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lOQfXkauPBWip8-tKJ1letchQprFWQgVmYcP63kdIlsG4R1s6TwZW9vjFT8oiLBYSdOZCMmZV_YtTASvOQ3xemTRhHJ2Y1mRO7xMSbY8mqf4jJn4SNQ_t0mu2SQsLdMZR6aNgV3Z7KKAAbaMkOEUmmIsKYzMgLR3I5m_pCBF_YXyVBTa086WKgnpr1ZxXmWvq1yrp62RoGUxvzl2U9Y4oy0WgeEhDaDTq_2Cu_CNFBzjYvzDH7LQihosJwq4DwKXD6P-d3Es8X7yVX6XpgLEcZJlwwMBGjJjZn9cYgQXA0FDjDNBo48oFjjsyNxeFkSh-Sg9ZM_jxp8Ouj70Aglzjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s5h_PhgLuA8irZcwYyYqB8NGIxczj2KkIB6Qk8zMN-9Vwj6LG4qVQkJWfvxEj-Aev_kwzWwb77MpKlMKiyYxfDqxCPfE9QpaJbiMw8HiOEf--t7kaF92sSVEEOLV0HEl1Zrc0nH7nD4Tkw4xdHOwOFINB1nvlOaoFGpSwcBGXBLABEEPtQ9a4snnMvE1zO1t5CCKxiGd_JUnKs8USbACYfdwGO-MO3QcuZIyXPHc9Rs1iDKUfXGIggzHaiMZsEjLN1z3inYp3B3VaSHEtafURPWEuYutsdtBEviRL2TJB0lipZc2YT-esnVGEaf2lncfDjFInVIppdGuW67RJor_kA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIJ6JBoAwuTAfUgdpwqImGsBJKv7bhl4EqhLWVLu08V7QcdscP9IliTawKsgUrJHXx7T7MURafZ0CJ2Hgn6MYvjVe3SYF9vkeHhmAi2bwx1V981Rx0OD87-H8froDiElK6eASq3hZtJ0zCxXghYFbERPLwAeLorZi_6PNHTTKxTvdSRTG4pNIrwg_MfmMcMtMYbf1VWidJCiDMCgQIluZ3tiH2Vy8PGyx5t0GqQClQBS_AepNQUBknCYwjBGsw17QH9rVhRAIUuMYFPLV78fJHZwpQR8DVFW2esuBRtMdEAP38Zt-0qtlRx_-qkbMsbAwBRuiFgH_ArMoMERsfLSOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=NgholP3UxYk_lgB_3XXjBuwaTTteu-iNtwb2lL64LqEx4mK-LKPSorGSdsV-6QsZGrGQIOpsLeIG_McItXK2Atz6zV9Gi9GOrXEDLGuUSafwr9IKpsRg0q5Nag9souxLJegTxkCa2QdjxRvr7yueo22bhZ5PtU2IcOiRRMjb0NGSoT4jPCoJUCHXbTL9ILgvAfz2NiJRbABeBRMJnAmv4cXOFeBcWpxjVKPRebbfA_fUYkLX6XCrBFnwz2PVY45ShpQ1hbOqfCFvf-JsUwn-pylTAI2cFjsijye8vyeGhrHIBSY0BIevIchCMzRONMDDEQIUa0CaImn3WacqgwHvew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=NgholP3UxYk_lgB_3XXjBuwaTTteu-iNtwb2lL64LqEx4mK-LKPSorGSdsV-6QsZGrGQIOpsLeIG_McItXK2Atz6zV9Gi9GOrXEDLGuUSafwr9IKpsRg0q5Nag9souxLJegTxkCa2QdjxRvr7yueo22bhZ5PtU2IcOiRRMjb0NGSoT4jPCoJUCHXbTL9ILgvAfz2NiJRbABeBRMJnAmv4cXOFeBcWpxjVKPRebbfA_fUYkLX6XCrBFnwz2PVY45ShpQ1hbOqfCFvf-JsUwn-pylTAI2cFjsijye8vyeGhrHIBSY0BIevIchCMzRONMDDEQIUa0CaImn3WacqgwHvew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7670" target="_blank">📅 20:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7669">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7669" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7668">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7668" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7667">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkBFUuZqI1gjSNtDM4rs8EXPNB3UViofEVp1n3ybh_zQUpXKhg4Xt_F_Q5MErdj0B1wssh-3mZKUuEAsZ8ct8_uMNroRbIxeRimAD86ovRWf8o4nxNVa6v4Dbv7_VBc7k1Un-RUUf3tERzxU46bdXDdGJ9qXWKaj3ka1BwSgK6KcPWCy38M65hYVV81KXkcVQJkYxTaN9TcDKQ628IH63gjUr9D9hD6DqXz4cBuQA4EtLceTy3QRNKGDfIBc7onEE-8eb5CFQXEVIPzVPtpDQN8MejTcwRPuRFmLGMNbj4o03NNc9gcvukcQAb9TmJDx1Rx8O2O9BxrjCF-B8EtcAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7667" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7666">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeMKGLYfK2zjGN8Bl9StTXhi09gEktVaMl1fv3o_4c4qQldyRPa14tzIJ_I6_2cG0-KtH1F5hUrcNw6iDdcxXYQ98oFUnkVv-hhpbM2JAvdCvxqvjkFZdCl4AxV6BaJfTwcwpDi5XFbVZHLe-ZhwAjE1aN02Kg3wL6vP723nu2cv4TFlPnUUEHdbkGVaFmDytyqC61xDBwWqt4bvuOZ6kQ-QuwZetIH9GMnoCdZmILIJsqxST_r0c_hhO6BYv-inXneUctLqPy80BavIzPeZcYhXgL82G-FnVakjNnJNRop424FQ5fCzmcGGb58UyZzK80XYP4pTGmXpcR7LP7InLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7666" target="_blank">📅 14:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7665">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sblzbUNke3ezFDnHWGaBlCnTL3okZE7VkTnL5e0lJfOl3HcXisS_nnjAhKbkGF9wNW0MykwiC8FtaEsZOQlSUraFOkw3gOm2fMV2kKAyZAThFkFsME-WmzLXyL3F1KfPRRnSbXHuUGNtbet2dMgKeI8JEAAffHDPR11xWeVmOwDcLR70RNPpOIcVw5MbzRyG-wTNPAECf_ItgoSjg4HuyCdC3yr4v-9sr0eaU_mMGFlwHvYojQtKn_63rZVM8FqVzh_BGJvi6ZQC19wUpPrvEDFIMUhAqUugbpjMMCmRXA4c1yod0eF-PUF1yuAArlDuH5MZUbNN92nu4i8sQ2Rt6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7665" target="_blank">📅 14:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7664">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W75XPvJmYXrKrf_WfLQW0mqOOPZ_Y6jskT97_W4BgzFzmdW5bdRhJnMTgRLNzJVV6KbxvdaaGRs7ncS--9yNgVsbIaxX1WfcG-Dkvij9ZvmGVVG650LhTsGsglBBG8q6_aZjTyR7PNj9lGXaYxFRB6S7rFEVv1KquyKm6oqj_TdpYQxzXWrxvymY0A13uezXx4PvRZ4Nk9CDE_dmMw4sQ4y19q7brwMErtKMVQUuR3RAXXy_89cVbA2k5ygyuLsMdufcayws0zHNpLMGvRrQLz1P-UgCUC8QmQnpCPRQIB2JPieN8CYqlO0EWSAUljtOvXL1hQY4No6Nfqy9EPbXZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7664" target="_blank">📅 14:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7662">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ve5dVVsMYAweBtUlRtyMj5CuEjA2UcVAFdk4H7dFLyZy2jp6zZj6XUCJAbAonvMMixBMoqiofWbH9DNGHdaELQNC5oaEGldAppNEN29vMFPl0pBvb1EZ9x5el8RZnCpavx9YHEULnRic85eN5UT1eZBcBbgNk1Vc5UpHPG1_aaIQoWeFV8Q_ENVVCynpwhpoMYbn2jiWyHQja0R4OY8oLGMhc2zc_qW6nUNI6uk2yj-og9bAqxIr-uye9eYQaBB1WhBWWvuLhFiK00tayOSyaQYMqqbckcrkLN716Yk1-Ge75RYPO0yDsIdd7UyHPPsFiVU8eR729QgRztaHxRDuFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piPojktoXrgCDqi98Qw9J5oqktVsCIzKdZCZkzD9XlnP3RJLpORLzSRga3PnhQdAUxJSm7GxH4qNWVFRvmZbOt1fgJ3ahq8bi3Nds6_E-yHacxW3rmgFc5-Ohg75gaUO7uMiIldoIIDdH26cZ88YDjOR8tg08vemTOArRnEmEkqKgEjHWhhLR0kbfA_dZtdc1xx0o_BOlEJ6522bxlORfD8vxgvuObvDrKO3W8w9X2yNQwkxS2bP2DadohloWBFCYoAFWZBoPumJuYnxUkq895HrcsUrkPsf7j3piGw32CAphWphiLFUmEZbio-ukxXmosHIyFamij4woSpyM4xGzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLkzvmKsf_Q206G3drVXyBsy-8Fs0KRNcMmwRDDHxtzVAM5NpQ0vRlVfVBEbEy2SI3i8oJEWnpUeLaLG36H3YAHXb6sYPqzFu5vo_nZF66zeqkcAXjVK6IK3Q4z_vrfAyVUkyL1SfKVNpDqEpmexFjoaDiMrDeKQQiZZ72nLjVo7q0ZtMczY4WbaNX3PowaAiYg_kL7V8Yc67GHCMfrlTlQ9Hb0u8AAuD12l-moTbiJ0bLPWdYyUFEVMQOrJMFSDPUEp_0_NnI0iScYurpJCLHmeF6LHlyXzS9fHc2vz3mXUbkdKU2fluIHFfyUGISvLoFVxckQBHCbMJ89DzQVakw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bg8QvcXyPi-oXuPfMBfh_wQjYS8iDJUmbH-NFEnl1rgPIEhO50vqGrFaLtHDTwM0cAgDjisFzcZkTwIk-3lfaepNpNBEDoM2cdX1psSV9hkw1AE3xNl3hAHJ07qQHUdcaKNe8v7HSa0PiegMvWdcTQNgdpHMsnJwS-XZ1sMnFQY4nyv9TsBXjQ_aVTmTHuYM0AA7A-CA8Uy4AuUQr9A_Q37sOY2-EO8KrebwHo1WdHGxhZ0pZUZ1oKM-cvK7aFt-fuLkphDRxax3CjTKIGosKvQZd0kcr4XebpafraR3jkzHUgYzhq7zMa0sBT40afUXA4nWaT2qQn9MpJJcd5CRLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlVHlJlFevqm4BkyuQusyuwfU7jlW9-pD81adZOtf3FpJtPy6eJQVQmoypV7wzCeregweHA7RH5bILwH0B8Df3ERqim61kmnL4_2DNMM9B_PTkUJvmt3a574hYi91Oewv0HwEpvYi4WQvJIO9azvddkWeKrd7Mzf0AmtrLgk-xuRBTCYZ3ic8eSL3Ivc8bp8_utDmvO16sxgqRpgZYvhin8e2htRH8I2Czt7va5UTquL60QY3Ea4d4tU6xunmF3Q6kea_BZCc9dgyUuw-5n4W9bHt7uYI2tFhRR27aghEJd8x9g3V76I1MmaWxKsOQjVMMbsbvDfcaNM7wL0_EX4SQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O12HUpIKgftxFdKSXsRX1phOnv46GiFzhToKLJ9-MXPg54ZiW7k-mLTk9zaBEEGTyyGTy7KECWf5YL47ehqE-kc5Xh6aCtnvobVO6AQ4RziGSAy_Ec44ll-p0fU9SjzZXilXUDSXsbrfftPK_ZnVDS8sizLHXfjWSDir9Kwfq-pfTTYWAwlDD4VKEOF3UFIk8-QIXz_4Ad3DpQXkxU25x879IhlrAYv_BnaVtsGfhp33svfqhpVrQAkK5MhX5kfxj106JLu0U37PejUnPZhkj0MGUv5Fn4jxMc5KZ8a899l_MWiZOiSbmTEe_IW1ESYKyw1s8XmggnEoMIF5rOXQog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoqbknAfbRWngV1_raGS6S7HTSJt1VCuLxRJs3Y1YQpz-KLuxMcUHR9rAxFEs7XICWU4NXWj25nkU9vjbYu3TTPn_TP95EeUDTAb1EPFKutFun820_saJ-7deIz9fhNXimLmd_1RPLyZGdeqILu-sm2ujRW67-uQJX38TlyrD9p3qEnEJ2F8I3JkT8Ct3IACe6q2CCZjNNq8P4IeCZNbJhXsh-J2dlXi1NBkiW6IWXW_TD8eUKdYhQu_ma8_pJ1gsdVsAnO9tvOWuj7cAhUoYVP7K5E0aOS-fa97o7mgNQTLrkE56fyekV4-lIqoR7d2xEzFoUJnMqUukUEnimPSpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEQm6OBHdJCynOlHmTs7XlsaV9TwsUyhae-NUnbC2QoV-KQ_WUpp8L8Wl_9jcvFCnu8yIaoEJnpnSYr0zOjUj5-BxPn-sf6hItSOjtzAAiMN_D1JoaPfAkqRPaowKCbUHVp-qmR5ylxwGYfMhmCbRW4BTEmyGu79ocX2vvDK6kStAS397STQlL5L8eniy7YlnZCdO8KwCAd4DWQdHzNxZXBr84nklid1wWICcaF6edERMWep7bEmrdT6ExuYBgtJ_e75k_IOrC-QEbEaueJUyO9F8E-FfSlXACGddJgdAwVEyBJH1ELtdSAOpzssgr159z8OquePZpVVcPhOiFX30w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3dvDse6E9FgSOMxYUSVX6OkWceSn8Gu8vhQkNKMrlYLen4E-5pCH8jbHC85jno_p2g2pzCYnQv_AQMjUgw5Xyg55d6nrHhfwq3BPZls5m6rdUB9LGCMFvnW8FC6DB_H9_XEsy8wUIl7cVt-fZFnin0SWQyrhVSt0K37RCUNrRKDuD-xEwKHw-RyWl9Si9FO_8QsmmmYr4UOS0cd_KopOrHhEQ9V8RDTqSM_fbN1yGCSvv7TUI2_skb3VPzxqNC5jsFHc1_93HVpPP8Cyt-4abX_0Ra5b2usIYhqBNdYi4aQ2BsFq2GY3YV0RkRUoDrJp4klfqaOn5orkgsKaHcD7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsQA4_7xC1wtKrzhZBatAjnRR7Z54Arn1OuEDPb9M_4nJIz1Lq13WbDZxm9HCbg1ON4GKNFTfwwdI9L3ce9s7L3wR6BidqZ2xBetH7pYqGYZBodDBs3Mqg-n0Yt8INzAqV7bxJ_sHI1yaEbZ1WH_MQ9NvXYZQTQAP_fJ_HzbcDeX4gMS7t1kxJ9TA7BLoDii6FvP8v5Xt6zqT6g-h734auBG_N-D51mBZG294vf4mAIHsFlnqAFrsBpTd53EaBM5OVGnR5cy90UyddrUR_vHCqv_slQSuO9AOdrshJDAH1MCext6W0E_GSM1NZbfp8hAkwRoSD1wsjYXUXr2Cf7QRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9DK-21F20A7WsB7_Cfj7JxB-czuF--xoe1r323e-eh0NsgwKpYF0DeSErGPAD-YDBoyO8PEjnbD6Wlp94_Y5jYg1OG-dSt_kP-GP8vFJd--3ptrIWWOOeceJqqbZKTORzPIEHR8RcItP88WN5_HEBU7ZMi97EzYy9FUDgzROqpqQQvd2NwHeD6LQGJlz4zsTnXpybauriGcAnvInWB-O8347V_mwx9lFXf126giECp_6c7tHaoYN1rhC-W_e559Ir813GQKYtGaHb511pKmuHsEhHfUrqywEJLTdqfp8etlH4rP0pV1v1X4Q92J_DlUrvkEr0BF6k1sr_wa96qOhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7645">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyYjlo4EI8r8ybI0IKryAVihBj4LAb7aoeBePfTMeiozVLTvwbuf_J74Wf-Bu84yfR4MEXLrGS8BqYHndpE9nfwt2lEhoDaTnP_6hF6Aw_3RVFj007uC4fwfFpG7LlIJOu03UnLYNwUjMLls8eJ6KQS3JBxvkgg-SWSZWKoO6E3tkxfQWvu8BRatimnIhWHfqBP21HKE1iCZGyEHPgZnAubsnYWHQNWt5Q2mbd3aYMxDZe24v0VECPK2wFgS4NGj0Wosv0L5bp9p_C8t9mWMCXnME_BBfLffj8wMZnfBL1q-ysT3TqmJwNX9wvb5D0z-6-HdMp8WxQQExbx1JHw_Bg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WruKhqoMrvFodpw8ErCTKoaiw49z8Bb8cGNlBoYIjjoMxhVFmkZwlkPIoV5O2tzGuZ2F5Rs-vI7GX-iDpGbl4cdG_gceOPtCdFruynQDRSfoBtI3ulxbAyldzFTNCu8MULRBU5OFVvTe-eBdgx1mJ1CVIfiWXXbCXdm-roj1za0oO5VnGqm0DvMuoqMqbcI5Y5lEvbYvmvw04AWfBHtj0sw1vM_Z86rduj_rAQMjKnYxRdm-pcrLVcoLB1-qxA6Phf_5CUkXAIBClakoQyIe8tBt_bER2kQ402P5dWUNun_yp3kXr5swlaQnvIzOPuKKG4bThnxcsycX1xdE5jli5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rdeld1odSpMBF9ranTCDlx5as7L0BaU3TeampJGcpFv-XEFSMqNWL3NCiEj2-XpwS--_FCIFaNiDFjjwZHSuAKf_W5ZBvqsnT6SkP-L7KSu_fS4PJjaAbTeEWB0icR4h1RIZrD0N29SsSRHHK9WVKm--3j6BGKZHaztvGl753mLAR3c2xkIWQAhXGSOO64YdRdT1BVbgFCg0steQO8EeAp94kPgB33rGMxPTuZ5G7XH-54m3KY2X4qvppvm39S0PYf7b1WRbuYSxBuXG3UG6y8B0hcQO7XaX7IjfTmWReCtndkOVkZNFZvaWrWlZFfGH4dtQpzPK8WmDvGGqIDlllA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAyFEzDScwKyIf8XHc5epazm4i1QZvcz1PrM2PHw0i_-FWRO9ZOcVzKsY0pC0fjvPbtWqrH9BzDYFM0DuEdbag1RgBctnIA60MeqDhk8wXl9x4e-gTMoGeT7QaYSpFXAkAR9CG0EXHZ5U2eT2RRG9UCGbZLxRSOF0TjkWxF3wdyKUCoEG9yoJwlF_GK3yizQsNp6q73dTuLUeZJdk1d0_VEhDBxILpXuHbdQVSDwziFMNPsmHxF8v6e3RTag2f8H2boGVfEOLeTYWKg6Wz7Mx2Hl60aX1iJGRmKLcVnqwRrqA4JCK8g4sLyd65kmvp9I6dRqC5U-K1R9CT02yPXoTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=fdp3_WZXD3qx9sW64KgR6TbMWwTAOBYbB4Tr7OWhNknpvWsmJQ5lSmtAtxHE8Lc_s-roo06zGz6UzDcd8dT-DyDjcbGk-tVJ7r4UZiutoTrv7GM1dBjHy-KYePupGs7I-17xt_AGplhm4mBH1Ld0FoeFEdL-L5zcbyagDvg364d0IU6j0hQgcaLdmFfrqR58KXi_uvfg3acN77BQwmZRDB2WsI2597G75_2e4qhyIVE184r0mdXphlWpBhJ2iIddFJx_sPIcJTNfvyLcm4R2IgaKLe0aqsknQGBbypUzTJhuuLp_rmpH_6mFG4pLaE53ZMoA5p0q73Vy8CDxR9LYbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=fdp3_WZXD3qx9sW64KgR6TbMWwTAOBYbB4Tr7OWhNknpvWsmJQ5lSmtAtxHE8Lc_s-roo06zGz6UzDcd8dT-DyDjcbGk-tVJ7r4UZiutoTrv7GM1dBjHy-KYePupGs7I-17xt_AGplhm4mBH1Ld0FoeFEdL-L5zcbyagDvg364d0IU6j0hQgcaLdmFfrqR58KXi_uvfg3acN77BQwmZRDB2WsI2597G75_2e4qhyIVE184r0mdXphlWpBhJ2iIddFJx_sPIcJTNfvyLcm4R2IgaKLe0aqsknQGBbypUzTJhuuLp_rmpH_6mFG4pLaE53ZMoA5p0q73Vy8CDxR9LYbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9Sc0aN62RQrp4YUnoZZw1n0H8XUV-VfIPHneV55Qh0kAs-2JxKgCpIxEYRnrqe9iX2H-ml6w77MTjoxpcYLLDW-VL9VliqhPWQDaBETq_pPGGonoc35ZqRzLfNmiZ5c6CDitz69lK_aGnMp85uXoBHXDLgoCmZANFjUrk4U-XdOelJXULBMd_2SMPTvGDrcoFpdRt7gUpRORSR1HTwJjfJYfRp2MqNXxTjlQqt7iRxPWYVl0zXjBPEQICSJr9qX9r-8TfdOLAZNasXch0TZ0_98wEPXyffuHiZE7oLOzDePvp6nvEZmKTWxrT72mbxei8LUuC0PZAUQbpze12DWqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7635">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNOF32L-_jkq4wdgrCMETDW6N5DYzm96DstM1-0RWAqQ_tbGJsg-1fLZn5sNwOWAfcASI0xizKPgF4qGZmseye2qXYXPOYrlOT3m5SzciLne_3-DByxJ8RI4r3pkEFARB0BgfqtMUQCC6h1uaJEMTuURi6p0pA-ny_ZX62CFjwi7wuiXz4lp5N6JOSEdJZVutx0AK58JA6GcqVHMhcYXQaKnDedyoz-fT8FrWnk3WJ4wAdaGi55fuR41CtE4Sw_8o4xzwJ3MpnaZo9jSVgzJY9zbiCcCvIR3djje8-KKxxYPuN3uvM-zlqj2h2aS49G8NMEui1F7_jpNT8334-gHgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=TIY9X63eE9Kiwz1yNZPl1YiGG-m-nVZ8FPg3tS6cltcjDpz_QZX_YmQsB_NLkAdzIpgru7uD5USiDOBZaw3ifu5JH6FaSkKcELFNzdKB1ZZvxIHSKo006f_03DLZo-uf6pVfsqz4HgQW5udo8Y9WOkd93sVpmd0T_pGlZo1Pb1uj8973PAo0VB8G7-IeXvzpvwOfGhS3wCsMxxT3K0RFFdW8QL721ebnW9vRI186Aols6e2s3E4SUteLej8YM0LpcYKR49Ivz0OZIhPrIPOmUTIB57gtIC4Zw771UsI3i9GMpRH_FEecnWjFXKQI7IGYbkJxMItQS1UAd_Rlibs-WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=TIY9X63eE9Kiwz1yNZPl1YiGG-m-nVZ8FPg3tS6cltcjDpz_QZX_YmQsB_NLkAdzIpgru7uD5USiDOBZaw3ifu5JH6FaSkKcELFNzdKB1ZZvxIHSKo006f_03DLZo-uf6pVfsqz4HgQW5udo8Y9WOkd93sVpmd0T_pGlZo1Pb1uj8973PAo0VB8G7-IeXvzpvwOfGhS3wCsMxxT3K0RFFdW8QL721ebnW9vRI186Aols6e2s3E4SUteLej8YM0LpcYKR49Ivz0OZIhPrIPOmUTIB57gtIC4Zw771UsI3i9GMpRH_FEecnWjFXKQI7IGYbkJxMItQS1UAd_Rlibs-WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=bRGmDIkrYAmecSZl75rydPgHPMfhdFFWrBf5XmbsbMsx9qmmX6KBkmeaj6Re5RJRQXo4y4bxYAr5xuCArQRUqQ07mCEb_nw2k0EmF4ZiHDqD6h707A5iJ9i4c8fZ1fjlL6zm2IXihDuEecX6ASLMcgP3dZBclBafBgQ75-02mfmJCua0O0-z5K3aSBA8QKnjeLO6WPBbk37e5jl3oD41uIkW9wJrecoFJfBLNz9mM8x9kMrNoUUIWvx5auorSlmWnuCAY8GwzDLBY1BvHW93WbVfefQMxvFEFFsq-0Vljt8lJ55kwLS4EZW5-xXRsvdP4ovbItCJ1g5QDdt-1ZQsYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=bRGmDIkrYAmecSZl75rydPgHPMfhdFFWrBf5XmbsbMsx9qmmX6KBkmeaj6Re5RJRQXo4y4bxYAr5xuCArQRUqQ07mCEb_nw2k0EmF4ZiHDqD6h707A5iJ9i4c8fZ1fjlL6zm2IXihDuEecX6ASLMcgP3dZBclBafBgQ75-02mfmJCua0O0-z5K3aSBA8QKnjeLO6WPBbk37e5jl3oD41uIkW9wJrecoFJfBLNz9mM8x9kMrNoUUIWvx5auorSlmWnuCAY8GwzDLBY1BvHW93WbVfefQMxvFEFFsq-0Vljt8lJ55kwLS4EZW5-xXRsvdP4ovbItCJ1g5QDdt-1ZQsYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
شرکت Anthropic ابزار رسمی بررسی محتوای Claude رو منتشر کرده
راهی برای فهمیدن اینکه یه فایل با Claude ساخته یا ویرایش شده — مستقیم تو مرورگر، بدون آپلود
🔒
📎
دنبال یه نشونه امضاشده (C2PA Content Credential) می‌گرده که Claude موقع تولید عکس، ویدیو یا صدا داخلش می‌ذاره.
🖼
فرمت‌ها: عکس، ویدیو و صدا (تا ۱۰۰ مگابایت)
⚠️
محدودیت‌ها:
🔺
فقط نشونه Claude رو تشخیص میده، نه هوش‌مصنوعی‌های دیگه
🔺
نتیجه «پیدا نشد» یعنی نامشخص، نه «قطعاً انسانی» — این نشونه با ادیت یا اسکرین‌شات پاک میشه
🔺
هیچ اطلاعاتی درباره سازنده فایل نشون نمیده
🔗
لینک ابزار
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=dKp8yq55ussAWNiwsEWs6r9nUVJdah5Y1IuKJTF5SAdjYPgIgXBWicjLWAp_2w1wWggMh5oFZdzBS2DFJnB-D0qz2UigZ1b3FXks7d7bqg2m7s4YcZiQooczOueB9Fo1mXULDL2goZCUszVXL3y26n_fL32rYYBAVV7hP_6tjkQ889dALclsdzZZcIa5HxWuptjX2fVksiJlXNtZ-RxQhoEnTXi21niHZEkYNze6MhA2yW7SF8gd-1KnmgpWbzXW-Ef4uY2ieTL1lyWnbRfyeWFsX_Y_LWVP4_Jx2M1mtjnVojnY-rJQEk3kmspwqLAt73UWHYLTFYW0kTejmsk12g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=dKp8yq55ussAWNiwsEWs6r9nUVJdah5Y1IuKJTF5SAdjYPgIgXBWicjLWAp_2w1wWggMh5oFZdzBS2DFJnB-D0qz2UigZ1b3FXks7d7bqg2m7s4YcZiQooczOueB9Fo1mXULDL2goZCUszVXL3y26n_fL32rYYBAVV7hP_6tjkQ889dALclsdzZZcIa5HxWuptjX2fVksiJlXNtZ-RxQhoEnTXi21niHZEkYNze6MhA2yW7SF8gd-1KnmgpWbzXW-Ef4uY2ieTL1lyWnbRfyeWFsX_Y_LWVP4_Jx2M1mtjnVojnY-rJQEk3kmspwqLAt73UWHYLTFYW0kTejmsk12g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساخت رایگان ویدیو با مدل قدرتمند Seedance 2.5
🎬
🆓
خبر خوب برای علاقه‌مندان به هوش مصنوعی! سایت Dola مدل Seedance 2.5 رو به خودش اضافه کرده و حالا می‌تونید هر روز به‌صورت رایگان با این مدل ویدیوهای جذاب بسازید و لذت ببرید.
🍸
🎉
✨
ویژگی‌ها:
🔺
تولید ویدیو به صورت…</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
