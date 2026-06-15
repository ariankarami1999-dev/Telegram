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
<img src="https://cdn4.telesco.pe/file/tSSl_Z0Lx-9yWpSxbU4W3CW1FZ8nep-_C2sCvNUjRUppck7dFzkALkDMHPFt7twia05Pqw1SQ90qGVnKJhUfi28m8NKP-0bETY6_SSX0O2KS2ROsBEEnVE4UEdLxt6djuE2lMsGw2l534_7RiCwDv62h6y-B5Tj98wHC1SIVSAQVo8fRkOFeyWhYrGVwbDf2OiRGkvyb9jCBWJ8_iznPd23ymbPHolxFp8t4MTwPnIEKg6ufINymsVTRIHk1zO7LZNn02KKSJB5tP7AyIZmDNLEbYsXCNU3IBWWL1uazJQxvSkNmXC4aFWZXm-GIjHvY5xsk3oxowIuRkghlG0G-mQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.65K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 06:22:01</div>
<hr>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 199 · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: آلمان
🧭
شرط: حداقل 1 دعوت
👥
دریافت‌کنندگان: 9/30
💾
حجم: مخزن
⏰
اعتبار: مخزن
🟢
فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 658 · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
آلمان
🧭
شرط: حداقل 1 دعوت
👥
دریافت‌کنندگان: 9/30
💾
حجم: مخزن
⏰
اعتبار: مخزن
🟢
فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 663 · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6iceBeedAGuZ1KAPsyG7CIQXvlt7SzV5FQdtAc2OhdW81OWK3xQgGRTf6JUuiXL-c_7oO-q39me5CV3eJiwbQo_hnjL4fP1SY34aBhtycqGsds1QQYYHT9WQqrAYnF7ezH38PJRXT77rUPN1NfprdFifAfBCb0-x_85YMJtSsZyCS7F0fE5QD2ZnpyOjspgUtIZcd6Bk66eGeNh9zg8pqGymnQQ2Vynu7eTuBe3caFtjtUUMfZs1WOOxwYUvTweSVeZYm0aXJwL9-bNgPVeCr8a5VckPJgyzwQu3hj4AMlxY42PsyBTmvG09fmNe9FkRGUUif2jBYdMh8-lTnm50A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 894 · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjUp5a_4bZJTpLBmIhGUUk_UojawqM2Rm-a3qUO3w9xlaPBz3PJm7_lJCFPxjGA8RdH3RWTNsmMRW3du4VLFyVjWW2dROPBDhe9_V6G_dSC2_VdNHzcIdGX6qthc3OajYMI4c2NAOVpMLLWTbsABiZ4kKCuLPPvdeanq2klMTm9qnlJVXZfBJ0ioINXrG-t-qH6BLV4SzuO8vycyvdLPOKsyxal6g-WSlGCjrwAt2nKzgRraqwjaHHf4ZX64CuVQintF3kq3byuPNEpw_P4y6Y7ZBWGQSct3raMXm48-04WduYrhjXH0mqGR-_nQSMhTslcLhTpxy2vcjRl3YR7JDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbqTPImMueLyCxTymN9YhWF03AT7MzYUUKIqvy7L7OHzJVFguqAbEETGaAhZwo5mNw9F2KWfecSUCeNZkZ8oSlbdPDUQ4jrQZPK_ywNSmSHpjpZ_AC2A6B29cDvVKop2KpCj-P54Jb38rQBTmDNckJxERJwg5xkmu87WLrdg55CGTL3eydUBoNbGs70DP9MCQ5NDFhbED8qLz74-ibGxxPRaFElC6CYZDd7bknqigztRpM1vZwZKsA8GMxwymbkM5DKpQ-3PQ8Gp_ziAs8HVTFQiLbVLZPJuf_E-UfgucoX4Bwhfx6MJNUate1ZiSOqFlryhNqWe9NkCELsijsLZKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZ1YdhqOPd08WL2ooZXs09wfNKWod0shur6oPS9d1JN1R0THFLOIrJXfGEnrB38HpI9Ub34dk8yLI7UnUUsr4z2Stnr9Z7ZdEIKxvAwrjZyW-IV2mHEXUnTJ9ZqvzM1R-P8Wo7yr4_ROepHNcjAP6apN1tfEEyeC1zLYJbaiqr-LAZlJBaNbNIx3L3MITLuZMwqEZAl3Diwr9GRgIrCziqsoUkZreG8Es12KYrjGu9in97Urm_N6Mkzr79Nt1_jCevQsAo10vKZiZbmh2_E2CL5guKbRlFQMCRcPlr-xxfMIiexVUlGXV3YhV54mf-KGtxF5rY3xbgiGJD9AKSXqGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5E5MttT82gEWfuWLBltRURoswNrn-6SID5VKyfBdNyRNAGZxTqVUBVeUodwPrgmceJ_96rPaYyV9oVGFjbQAwK_Maek6oXu_Kq9YCdYK7pTabaTPMkjs0c7jow32IIr1nHuoH3ggSS8qhNOefDMIfCAeMHpr_wbfMWIV7J3jk8gB6Zrv2_lBLhWMZVPQH1AvZvIXbB8ST3aFO24feu-4eQEeVfvaLPjealQO3fPYP4aqqkUV9B_cTl038rusaFhUVzio3ZABJ-BB8DexpQ0fzZDpAprHpFhAMotmkQw13k9WGA8SKgYWGX1CNJ0FtUUcuNOPIQNiYaVmWrem9oGZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmBfxILFbdHUResqZw3qVFT3kjf3RcTEazo-zsIicC035DABGw5L4Fn95SosqP79QewQd6bLLYS6La_V7uw4rEK1WdDs3Spp1YT5wh1lOlZBA1kQVdPu60jKeBBavYqYqEOWm6_hEyUf3nYtNEHq5IcQOxLM3P4WqonLK87yvpzB7UnT6TH0wL47cBdYZwIOpk3ZTcur8OFSCaVP4DEmXwBDLmaLdD5mZDaleB8lsLsnoErqa1MYwASSt_f-GXeuvGw7Fr_cvRcGgvoGmMz5MZ5F_eGR2c9AY3MYH-Kcc4_CLJbKlo8vRij96MbMIjVkOmyYIWcdvhGvy2VlimIV5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mo6u7WMjr3fxVA0wunLDUTFPFpg9zDQUtjBuqOq9F5baNX9SrfNamsRLGG5070GR5eh3XnSFB7N4DX6Qhz6MqYG0W7tzQn6UOWKfsFahtES5Mt-nABuiaeYvGM59DttDLHXVacgQnkVTIWB9YeRCIiG755tyMWZQzqbx0MXqZOch6OJB8grPVB8yCo7Iph7XvMy8phmD8db1HpL8qajmIChW9nee0H5-0OZPOaxU5npkAjJMHTLAZn6_u39k-i7iF3yeMZiDNOobtDafq_RCqZu_ZeAlz1DpljhPCH3jO_-WdDFJnfUJ_U1R_enNEt7rOdjDr-lO4ML9N7eQMp-ePw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2z8k9AFyH12G1Q6KSHT1qBqUI-cg6WVXxotK9GnTmD9_ZIfAxHOoAaxfHj5DIZYkbFzbOGVYtLZcI7gpaiWqvb3gkA2Oo0_8YgLTCOQoRwW-_K_1MZ4PMFEWH5NJAzP2wgDovLBXNwcYl-jq6r_NZDE8mMDkp6chM8nZr0rHYQji0im-s2IdE9P4DZA0SE6iW273zYMy4AZqJLOmsgDyGAlBCRGtkkN90BIlhdsGKzJbXTblqCod4ygKJyhYC_jAqvgBTnZJGZriXZSuoaLNBsPCR1drED-Xax-1r_sIczWWNTcsrEP7MJcH1-tehhyj3A0UV56KFcyT6SJMFoH6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZnSE99rNdb7GKCkerwWVtg9g1a4tIsVNo1tCtq-H0t3R9_IvIdXMZyiEk1pysiYjRzhDDakRKnGFsGWO2gYKfOX8MbXEtMHDPkwybkXQmlp7ExMaDbsx3Xwo9cNv95_ruQpKKy8yIOSvcnm5kMnFXrlgBo8D4_FvFc_YnkiYtRa57JfxGccU3lK4YgVE1h6ILEnZMrw2FKlAf14ohS7d4Jbz5AGmkNtp8AVliatOQs28xC9M0WXM8QC7Igu0Mz8D-bFVlcsMraWWnkVjfpL8u4KEGaqdWx3OV2SgbfXQlMzeEiZ7-JaPMzqSJxNQ_0VhpgjwuIcboX2f_e5QmReog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=VcnjxlGE4Id09e0PXhEOGDznsQfejzo_mjYzFO6knTXjNw0uM-5M8NVQKL0E-Cbs4FDCUoDqrFagl9HpDXs4WgusHP29X5KQWp7fE-YTJUNqsG7UG_bLJaLAljnMotKWZfOktbK7yOCDVeVFFObOA9NDL-RV4uJ4Jt83SaPv2IEy7d_nYtI9DszMIJUQ5PFNcFxkTb3IaCjv7zzdpjwFk_fqPFQts1Q5Hwrxwd4SDw3KLOI_gdTUuU4Xv01ua4GCyE5FuqaYfULh8ZE_c4vedjeNeG9hWqjMczrnr-WvxE4uzXzHmLgoQd5G0IekDNENjBmsjf9KH_QstQmatj5IOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=VcnjxlGE4Id09e0PXhEOGDznsQfejzo_mjYzFO6knTXjNw0uM-5M8NVQKL0E-Cbs4FDCUoDqrFagl9HpDXs4WgusHP29X5KQWp7fE-YTJUNqsG7UG_bLJaLAljnMotKWZfOktbK7yOCDVeVFFObOA9NDL-RV4uJ4Jt83SaPv2IEy7d_nYtI9DszMIJUQ5PFNcFxkTb3IaCjv7zzdpjwFk_fqPFQts1Q5Hwrxwd4SDw3KLOI_gdTUuU4Xv01ua4GCyE5FuqaYfULh8ZE_c4vedjeNeG9hWqjMczrnr-WvxE4uzXzHmLgoQd5G0IekDNENjBmsjf9KH_QstQmatj5IOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlJhSI_bnXCEp5PkaYby9ldgWgwryoHhZJlbReYLgBd9X1k5I3--6NbnAz1a-pykBQka_Qo-XyZ4098ifFKYjwVFHfTZR1fU8Lo08CrjPzEY1N2BBZTs0ik9108vt-ujHeYSG0QZj1zbDMxHxw4Y2harvjGGRtOPTstaloUUkjUvqP9IXVlcUKRVuGKVRBzvdBAdhdo18Ju5QGXXam8R1T9BG81_16Vzg8oFoGUkyJl5F-1tngAbbe50xYj5WeLLevCrnL-Nf7_0ruiFpD2-nPWk7217zU5v-frcrkPdNtKr-NLvi67eS4orlEBzYB-Wdalz0vDCeCTzpI4afaM3ZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjgJXOpqmVRRMAdIUtpXteC7__pZ_PkezJ5uQA86CTZ6gU-rhFGasDvu_8S_2mRGUWjVlYyRBP9DMmIU9WXhpmEw6w5oH4ITSnnvoOPCbSAcqUCOF8uNmCMyHCiq5lZ834tfenkb98CJYvtp98-TcWC4O65WKtIm-UdBWwHSLHBenzcv1cxMFinn9ImAExFDl6YoxSThHSTpSuNtTxjAOJa4dMiQCPMpMTnu4vF7boNxEv5QGiGwSmkJUDMjchHqoxPYCqXvpOsqFgV5LOIgTAusZ8AKzmZogATEsGoGAck_wTktN1Q-1LmkEDry7XxIJ2hyvdZ1NxBk9MV92xrS6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=bTwHfZyqbG1V6p4H70eAY1onDVIo5_3JltuXovFDqa7rLO7ncNnN6aKEdO6ZVqt-kPIr4-qPE6gJ1k6yp85HmG7welWu9SDVsCuBWFTxofQbwTKW4EdgSoZeA_VLekaDjxwREiifd9XSU4ISJDBLSXxEoeX2E1GjF_05gyPtXW2E9kL8gvaGBHMrVLzH9hYYsxSHtKnLhYLmqIkfd2OkMDzZY-jrazgxbX3q1Tm4aWAAGcg8sUT_2boVGIM0eOgofK8sNPdB99V9F2z_wwNqjpW2JTpUxPVE-RHGv5masBJIcO5cUC8NzPKcr_0k6F1emtA38kCHpy9xwU2_BQYFsbCpi0av06jvf4hPcD1RjOvSllJGxfgf0pGNiqCFL6YZkzLuTUJgD2zvmZMj2BltnZRsw167Cxe71TkCeBbCXi6Xy7___Jcl1Tvvmtcpy44bMV1DCoon3l8--ngLTAgFwqDNjOdD6ARfNRcDrcfBy50vz-O5z4UBWSKc5YFtaGMfXd63Yz2QMKGydE97vyFHN7LqDQ87OZXPreoQCph3YbWLuMAWSYnBiHa6XLKioG_-WNIzj-fYna3TAuyiH-44UhwcjD84aLojAGIvby32hq1ViOvAsku7OYjMFYK7Y1dceL2bnSnKGK8sSz1VGqP5h5BDlCL7gFjelwXVd9E4AGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=bTwHfZyqbG1V6p4H70eAY1onDVIo5_3JltuXovFDqa7rLO7ncNnN6aKEdO6ZVqt-kPIr4-qPE6gJ1k6yp85HmG7welWu9SDVsCuBWFTxofQbwTKW4EdgSoZeA_VLekaDjxwREiifd9XSU4ISJDBLSXxEoeX2E1GjF_05gyPtXW2E9kL8gvaGBHMrVLzH9hYYsxSHtKnLhYLmqIkfd2OkMDzZY-jrazgxbX3q1Tm4aWAAGcg8sUT_2boVGIM0eOgofK8sNPdB99V9F2z_wwNqjpW2JTpUxPVE-RHGv5masBJIcO5cUC8NzPKcr_0k6F1emtA38kCHpy9xwU2_BQYFsbCpi0av06jvf4hPcD1RjOvSllJGxfgf0pGNiqCFL6YZkzLuTUJgD2zvmZMj2BltnZRsw167Cxe71TkCeBbCXi6Xy7___Jcl1Tvvmtcpy44bMV1DCoon3l8--ngLTAgFwqDNjOdD6ARfNRcDrcfBy50vz-O5z4UBWSKc5YFtaGMfXd63Yz2QMKGydE97vyFHN7LqDQ87OZXPreoQCph3YbWLuMAWSYnBiHa6XLKioG_-WNIzj-fYna3TAuyiH-44UhwcjD84aLojAGIvby32hq1ViOvAsku7OYjMFYK7Y1dceL2bnSnKGK8sSz1VGqP5h5BDlCL7gFjelwXVd9E4AGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=tH65ZAU7bQ7roYfF5l5iqN0M9xLQijR20dAIu1_CZ_Q1CrBedpOcLyAHNJ-6KowGmjnSmqGcJS_aLcbo64Br7B7XPQYzw9DZz8pAcyGMaRmI41HX9UlVpvSkPMRBMlsLlPTeYmsshtAyUUllenERqTRzwhv1NBhg44ENqKbiggn4FPth3N9xClvs3o5xCZKYjAaeWvFbzCDd8r8tFJswWNwWGcBvVuqztXBUScrdLIHWWme4SnshM3BUalXtUyvUmKDPSFyn7wuhKHaBFcGmWeiQMayp-wpGV4DqbLXgTkMCAmveO9aO_g2M5usS95JlPd3u453knUiD0BcPZb7uVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=tH65ZAU7bQ7roYfF5l5iqN0M9xLQijR20dAIu1_CZ_Q1CrBedpOcLyAHNJ-6KowGmjnSmqGcJS_aLcbo64Br7B7XPQYzw9DZz8pAcyGMaRmI41HX9UlVpvSkPMRBMlsLlPTeYmsshtAyUUllenERqTRzwhv1NBhg44ENqKbiggn4FPth3N9xClvs3o5xCZKYjAaeWvFbzCDd8r8tFJswWNwWGcBvVuqztXBUScrdLIHWWme4SnshM3BUalXtUyvUmKDPSFyn7wuhKHaBFcGmWeiQMayp-wpGV4DqbLXgTkMCAmveO9aO_g2M5usS95JlPd3u453knUiD0BcPZb7uVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/6348" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_y7KVg0oAX4zB7pT79sA0Gdw3hLM2NdSYpmIDob_Hv3ZdByRyzzNyNNcSiCvnlhbj2Cec9Ao1ssUriK4wpZzPdbzOeL1Fhk1friNPZQBu9hFQ1wWqJBvJE2NeKTeNpLXIMbq1c-ZE10-k73CDVe7uGLZNCehnq3P4sq_TmAA1Ctxr_dKYYp7mzTxgePXmKSyUzGgfkccbXPD3fk_1rCXXfur4Z4eVNiouKizxj4LfPVau3Wz1JKvdbm9BZ0loKb9n8DFhcxpw2Ler5uo0-GbHo8qzRyPASk9J2TWveuzkvh3hufubHcifYMR4qEhrXLsSxjwBlOXF4df0-V9DqvnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکن ای پی کلودفلر 2
نتایج این اسکنر معتبر نیست یعنی ممکنه پیدا کنه بزارید تو کانفیگ بازم کار نکنه
بدون vpn وارد این سایت بشین اگه باز نمیشه واستون از یه
اسکنر دیگه
استفاده کنید
https://cdn-scanner-pro.vercel.app/
لیست رنج کلودفلر که پایین میدم اد کنید و اسکن کنید.
هر کدوم که سبز شد بزارید تو کانفیگای کلودفلر
با پورت 443 تست کنید</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/archivetell/6347" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdQTL8wo90SExEt3Tte3BxjCbt5iybeOj2yQP_QddbH7NU_uZfyb7xf_a8aGslfFNfEx7D-zkGKtXBh1A2EwRHeagy30gWC3zdtaYWgPnWj-MNKgP4kD_GShAptIlecG2R-wWGe2Qq8BDgzqIFYQ3-DYU2g0MfIestp7b3TkH8cCK4PRMTz7v-f7e6TAvxT8AhQLDkUfvN-rkI5DhH5bS9M7n0NcgzwhTJwKbu9dCfbrwrqdWWluuzc8MJjS0Vplh71H9h244XZXS5c-m9oynO9WIdGtr_Eu_67deUFj1uMJjhma_ANgm1WhOiUFuSQtehIkNUNzdbdAWKV_LLEhYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vgbtPSG-9RDb9pkZFxgP3AYsoebMfAQrhEGlP0nBaWDFNCVT8bSKaYeqaAjupZDru0G8M_ovAuTp_fFFmB0GRibhVrwl4EFdJdFx3_yKKpvyDZN6CnnhifrvJkiWJG02Cij3-nHZXvEpbHNPdsLeTXiwjKm7zh4u1tQxojq0dGRiJcybOn0Qo10qFTNotSsiXG1xlXhohHWijShwqxuUTAm2bsfWZy95YLxikkGGvGy4vgrTrhfhO8tL34gy1mNUWJ7bDH97qRF8F8NnLGnMyJjH27lxwfzmvcOJEg3jqKuDUigwR6zE5t66hSrEA7fxKCDHETmu2m3xKpg-bSTBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pYB1AxEV17iVVtlxSCQZA1Nod4GC81n2IMGXCehticCKzMA2QJspxaAg3caC_EYdbZf9Boo_bZ5TpS-_kX7XMbJqH--wLEH4FgtvC41vPZMYf7HMYkjS38Qa0q5LDTeYMGmGu8tLpt1-aafyKtNUXRE65BFR6Q7s1U31Oc1aJYYPJ_YDBbk_9bO3G7QiLd3k0_RAcK87yhclw9iAfRtOgAVQj0aqcn-EpVoizPfT0VhTux8gBKjYOCsaNnlw983QJf3wq4lbyvUKjcBxD4rId69z2wx4o3fAwC9d-DYVRnZS9T0QIpBtLfuWdBCjvLK3zvy_79XSNBtB2D26MfHzvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lOHfnwKLczDnb0vWTvAUumBvE-W2QYsF8-8ht3z8GuzlMez7W_59YwPOmaKbY9dzLAot7fgXktft8iwsN3zY1rpppRWmU3APt4EaOsw0xWggx7nNVbL0u8jgY6IztB536H6RpcwtSCK0KfVz3UktYSTQuJSlql8myNkmW_JPfJvOdLHQzfBfVrOtRNnZq4bm8f80LgWUAKhmxX6fwThesd6zsCRj5YYuJrAPsRMfwyX2LwD5j2Z8zqrVBym-qiBRClJM0k1m9S8aRjYT6u9NfW6ZMcukX5NZHfJTQBmm8-t-qCqE1xEhRP1UnrZ2ABnZNyLpg2Hx5tmcsqlTT2MzbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">7. به صفحه اصلی ورکری که ساختید برگردید و بزنید روی پیجی که ساختین تا باز بشه
این صفحه nginx که اومد یعنی اوکیه اگه ارور 1101 گرفتین یعنی اکانتتون بن شده باید یه اکانت جدید کلودفلیر بسازید
به اخر نوار ادرس یه admin اضافه کنید تا پنل باز بشه و پسورد رو وارد کنید و لینک سابی که میده رو کپی کنید و داخل ویتوری وارد کنید.
کانفیگایی که میده اگه پینگ نداد نیاز به ای پی تمیز کلود فلیر دارید.
مثلا این رو با پورت 443 وارد یکی از کانفیگا بکنید تا وصل بشه
188.114.97.6</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/archivetell/6343" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dw01GjsP_svTyZ7bwO0cYfSKq_AYji7K84an1Ln7CQfxIGa2dOt_nNiGyuXCIEEv62C7JR1aoMRx0Y3bEHhrm5dxqXGEXc-C73yfLqTpWn2YxXT8wZ-efzWycRgR3YTofiARyr7w-azkyw5t79nV8YDRLGk-WAuNIAzj5bmPak8ezjGwsqTyMVNMR4xRU9vn2r5Dd587LYHjf0-6UvbKPpWTuhisEsWg57aO0lRgleXK_g04F5exPjdGcjymcr--ef9q71nk898nfE4k4oAQ2Ejj8rf3Q94n1b8WlXXSM1ACodvWmfAC_KhybvfOT7T93GHnfN_U1w6iM8AoYR0Tfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saHYcLgUziRKRw5kme0952Ep6n5ZrtzToPHDRDWeJP8M_Xse6b1CyhjugG_v-rHSlSkjJjPDcxVgYsra3RthSwzJSnJN-Om6EyQjwtbRlUFIrCUopEaFk7Gmh3a9K3KTvMiy4mMVoFZ_T45O5ENKOq7u5_KR1lTcmqkQ-3ziBBBuph_zGbhQMYT1EGS2HVIPQrOqJYjvXnJ80RDuO8KPFnkhEmOp8XjMLpTPzXbt1hPebzZyAAYVMiMBH4ef16oRt5f7nRoLli5_wSJtk69adYkP5Blz94SmOclkSf5lsxznBpt7axr6qggcGqtr_eVDq-1jJQMf-x02aWiK0LSFlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9IH9_q2itHxlpVGaNelq4FnmENsgMZsRlPerjjaMS2VjTcrDxxUOKIj0prumjp72nX5k4e125yGwVNH8C9UBFzpRVpzvSMvBZMaiYtnIaU6xePgpxIfgQB2TLI6h7_EaOFmCh-IytqNwH3p36A6vhdBRrwbttbTCJmiy4tupbw2ZoJSRGzrigA43Wc8_cuyJmX0cskM8M2VWZDAJiELf2qUm7kEdRkVfhQUju2D_etvuUy2ygixL6GfCO3zZxzJguprG_i8EYY7JSbwZdP91DvrDreeXWy8P_xt0ltZAlWZcuBMAOwK2k5QxBa-BsW6hYR6K4l4l2fT4AGMpEQhVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwBdMYpKX4-wni7PBafXOsADctfrTLPTxbVACd-zrvgvoJ-B96IuhVw9hqsUdJ9al1qp4ofN2o61M6nMM5M0LGDcbf6mFDOJKIdfCI0iiun1WouRb0FLNlo_wZbuy1ABGk6mlI9FhSFSyqLyZBIx-pWnO75L7YJDU3LuS78KJ_OT8m_U7pOQjlBR-fFF45CIkf9ufhbmAqPUTRErKrjfIACFnwI8UqbCZ_dUloO1lWj0V7yQfNvjf5XbL2kzrbR0M4xuiDWpFAtDqODVA2Uq9fTXdhSruwSQVXIwzuRrWCSoY_k_bcbMVX1DtdogjSYWeTM70ZbhFNVf_5-o_5he-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U__SR6aXboUnGrK6yHJAzdxB-sMrZyiL5XhSxfJqY52Y6rzLqSxUEGce0FCyrcRn6y2F8UTVzL2T59Es15_5S4tbvQbv1XlsZsUVSOnrGjACyGCgAwq41chBurIcZovLKegLDtu--GVo-LL7adDW3G9KPFG1HiT3IeyVQRpxevxJgCFwFgH2b17_h3jg9GUAWpxSML0iH3haUgH7d4DY5ZEIxrAXd_7Yf561yQdvfNrKiImUovcxaX2UZngUhYoiemxLJrZobBSZPwCQ8qqEEIA0UbwcV_zOBBhsgTirxHhc1kQPqLGih0_umHJsiIHq-hOcLpm2nDGU-MDv2qqUTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MORGYphYR_SwSdFo71kuQ5F2mksCx1EKRVBTBkg9lWVkmszNPf1Jxu_govYzJ-DVSbdpEyPXIrSBywhDUexedGt09LXX6pSh06f48s1FDT6ZjbfR0zF_APLLjzXft80yAUkWyLenXvVPlVOD-BnTaOG93sgx5w6rVWLzOenpQ7fgMLmpbWaGQwlmafN-hiY0-QJF1ExlfoJ7RwH4gcLhPslVNxvPtvxx3SDZypvMZgG-4SX6meC48G-ZSGyOQh48epOVN7NYYRJ5cMNdG-vbSnBszQSSFtaL025lullVB1NpgY7COisSogBBTomYcvZ5hpWVKevu2pUaN-43y7P2EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbGaJApAKJBQDCoo8Uim6jcTIEbtUa7MzgF1QnfVqXTpRJdNbrN4q4Cy6bX6h7ZrWXwC_o3L_IkYJZSZglnCV6DHYe_A2XOxF9c8HBpVvuV-bm06CDjxkLTs_FxjsJnTS1lsTOnaPewpw8f-8I8FOAHvN1OPz3NmCRQr9E_lF44I0lbJkEfs6eMiOawo2Yd_goVSbhJhr6HBaNb4EP1oTfWoB8_O7ZluZWIfBWAgQYnOVMgIda4nfzhdWTYBd5uRB14Lk9tbHxgZi6Qx0NQG5-3KMA-S1MmrKyxUb08Ez3wyzBfkIbikooywXylrlt658CDovKdqIENk-ycEd43iuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=eUjz1V0VaBSdR1qMhpbvTVguKBu-4CdEOPLbs_GrnDqQhgb4HCiMohOMsWaLROPKcdboo3yycJ2E62eLofc_owtHT_HKWhcPGeXo2JeT4r_74frOUi4WIHnJ9TmguFfO1ebjVaytt3SouaY6TJvAtjcAWtf811ClkFKT3ogHmyIeFKfkpljAuguNJzcuEqUw5-n0Mmw9xQnmD3VPYhpUbr6iKkQfzHuohU1mMHMClMfFnop_ZozELHhdBPFThVGekiJWbABFxjvU6CSjch-SbtK-6sgnX77GtcywP1-b6lJHbgMoUxGKHeJ_5P7k_OQvry2ctQKn8dTpL-RI1tzjFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=eUjz1V0VaBSdR1qMhpbvTVguKBu-4CdEOPLbs_GrnDqQhgb4HCiMohOMsWaLROPKcdboo3yycJ2E62eLofc_owtHT_HKWhcPGeXo2JeT4r_74frOUi4WIHnJ9TmguFfO1ebjVaytt3SouaY6TJvAtjcAWtf811ClkFKT3ogHmyIeFKfkpljAuguNJzcuEqUw5-n0Mmw9xQnmD3VPYhpUbr6iKkQfzHuohU1mMHMClMfFnop_ZozELHhdBPFThVGekiJWbABFxjvU6CSjch-SbtK-6sgnX77GtcywP1-b6lJHbgMoUxGKHeJ_5P7k_OQvry2ctQKn8dTpL-RI1tzjFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
- لینک سایت در مرحله اول  - لینک سایت در مرحله دوم  #GPT5 #AI #API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/archivetell/6335" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKBB96O42jHU173VxcOsyv2vjJWssG0xudOIKDF1Sjh2bIY3C6IHx8At1YU584JzPF_0loq6yFGFW5Npu3DzX2yrXKHEEZBtj_FqZ-vx2libS-KbKMwPC0XsJKKEB-5eBrN02K7yQ4nOjM5HvZanhBcyxU-iy_wgIZGCN5h82nSmpGrLRAL-eif3UXnngQG5XiGQG750YtYgSVD_qMYP2rjjNBcv0N9-U1l-yOpVpmGrMWq4dJ0YBskDtqWKmReYawNhClk0DZpjmitFoMYPXtbDHsPKHE2taYg9Vvm-wPj740VSQqtaZh9fsZijiknPf8OhafOuyWKDmJl1Ca6pCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7HRkaoJmwPLUH16wuV9cFQYy0JXLpkGQaNIc1CKAr2bX4bNXFc-yS20hCgvH6B4l5H7JuX98j9_cXgOZYZXi55kT7Pb6y7hnpfQhPowSmnBb6GbzA6uJaTqJMW7OlDmqEu00fKQKNbeIzlNTDQaoz5N1E8GbqPfwarDj6tko8-8rgkAfg4G6PMWMLHYFtBOZ2UP2B8DxX4eGoOVd3XJe0QQ0AhIHPcNiNK7ZZcgdOgQ1ggrKd_LUuUs8mP8fwxCd4pBao5L_xddggEnjo-jbbLmD8flXq5sGscaJwpL96bDQyDNjyx-BczwkX6JqeUBoDbHc4Nl9OSQEF33Fz_0wA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6333" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNJ4HeEzYphUKVUeWxDAwdvNlQa8aMVji5I4raEgs_Rok7iCVjOMUGszcpCIKxOF-nacq6d6gkry3-STEEJ_ObJLPAkzbhbSi9J-z0ixF5pt9c_agFzyU4KvB6BBLwYmuYMWhKPA_ocyjutR5_gLWdk6H8L67hF851E-kYPd67uLqN4i8FSgOLCTuh9ri2ZSrAM_Qpsq3AeVNOlF_X1_9AWSazM0rtyS2oems3pSk78KiMWbB-pA9Vodvjv0IQ8kU2b_5WOQVEKmOC5tdXXiMujcrPaOJUL4_UWhT5B3VQDKM6htGn4pN2ZvW2d2_zMk5nI6Q96M1PpyqurqzITqEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mREJkHAFNipB2C_IkqvD6LOvOcxy_jX9gjLlsgDfIp4TV-45lAbqN8sebm7fdm6YZtnYjGyTiU3zy-XfqVkQbr26Jspl7hfbeOrUAjkfQ4oBL0oFgTYKQI6sIvHZezk7W6TPFNl2Od-1ks9sqb613fyTWrZVFa6junKikR0XZi5sOiyDDyu4yf4pd43eNv123Lez6oOvHTCpvTCIeAZqOCkTZYHTA1TMARNxThMIkrUBl3Gjaxb8jDBylt0h6np9uMj1dc0MBQTulsh4tFZWc3hjMNKsVrVYoYOydqkePa36m1Pbjzbla08Qo_OJR9pNKk3qi-ciI6YmYmLXZUvvNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6331" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=M9bD-RNen9TtgInNEDBsApOXXwGxk1vvg8vugu-gBdnqmVQuoX9G5yy5QV7asWZ4i4ussFGf7i9jMJAkvqkaKhzdtGiPyEvmIoHS7aRtt_QboFd8X2WizmagmoAzaWI9cM6DnARwx9z4NiclfZMoJoJaA4uzqc2V3RSF_LfKfyHiuoWtSQ6ANQ7og36KXxXzyBmpazOXvaekGgJdJrOB-WF0Fz4zpBMpr76pgLLUd67bZGoIL7i0LJ8E4EVKipOGx5AXDBXzLSoDKYmIEQNfDP7E2mPNgv1fvBGvbJBWqjl51RYa4BcDRcyjEms6hBef6oXVx9580wuS5ddqevn_MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=M9bD-RNen9TtgInNEDBsApOXXwGxk1vvg8vugu-gBdnqmVQuoX9G5yy5QV7asWZ4i4ussFGf7i9jMJAkvqkaKhzdtGiPyEvmIoHS7aRtt_QboFd8X2WizmagmoAzaWI9cM6DnARwx9z4NiclfZMoJoJaA4uzqc2V3RSF_LfKfyHiuoWtSQ6ANQ7og36KXxXzyBmpazOXvaekGgJdJrOB-WF0Fz4zpBMpr76pgLLUd67bZGoIL7i0LJ8E4EVKipOGx5AXDBXzLSoDKYmIEQNfDP7E2mPNgv1fvBGvbJBWqjl51RYa4BcDRcyjEms6hBef6oXVx9580wuS5ddqevn_MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6330" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFKToC504aVN3JIiYLgnKrtvcLD3OSbM8LvhC8whDTeA8eTSoncvwDwNq9xAMRfPnVMwFBMGvuSEdZG8gcaU8MS4DcDpo47U8jqJqouA2S9TMbKeyVH7gd-jl6zz3hx5kI0xdwX84CksOnzTdSY9MGCuKv8-uqR8h02R4kFac9rGhIpl_n949RBaftHKPZtr-_GZUui6iKLa7_G-QyboAzAHz0WdZEyhRJXLSNELhiieTc6a2hLWdo4Sw03-ekYOkU8DRJvF5ZRQj5Ljq34fRScmO7QVg0ICVjG_KG806rWdP-A8IRjUjST-V8Jvi3BPb_joZ2gQkI6-Hrl4GfAvGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6328" target="_blank">📅 21:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6327" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6326" target="_blank">📅 18:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StoUny400gCB9orob-DPBMiR5oiMORYUD7gOTYQNqq-2XucIWB2MgysAJ2IfpyTv2ZQ2pV45w6D9aBKatnjASx6mT6Vv8LSvYR6OAnv30BBGAW01Zk_QL-p3M_0iF1Sf8WjNUhriej56zBLxmL1_yzFrZDuQV317QQLmNWcFL7SVjCISh3U1uwR9ClV9Rb0psAxnDZlaQrPWFLor3tP7WhBA_CUSFnWC6j0WxaYtUzzAA0IzM5V-EJ9K75qbY9Gh1G0EeoZzbysTYCJXN4DpTaVXrEpU4Ha61Dg_4z1dzIhUdfHqQ5UjAbE1H57Gm4JPjFjzfW3GI9W_trXsgNw-Ew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6325" target="_blank">📅 17:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anLHeLeDpurvKmiMpyyPj_z0z7uXmdYBnzKrk91ZvL1b2b5gSfZEJ7wGDg_2M3iVmUpxVbXxfdGBqILyp-QfX3mwfOyjS9qPfsatZVnGha0FJJL0JYg8tiX4FW5vUCQWpz6IQs3cs0R9R_VFKDWMbI-umLgVwFMZhtungPat_CAcvNVOgugCiC7GHvhimzU9gJvF7hekAVAiCytOYSAGtTxQme_Acvd7y4EBLTLvSb9Pe127UldVgdnAIwAz0bI8cbwE_x2HZfJzezfsH3LmCG1FQNzQ8RvtaDn9vImfQgbwJa8D6WdTR8Xqiip8fqjlxLyeXIHud5CZZqMGTf0Hug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6324" target="_blank">📅 16:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHdsELjL1gsYjZG32bV_QveUZf3RNoRT8iIDaSs-leuV9wuc6awd6zMq8btd_A-SgYXxnE3-H4sPlgMH0PzrpUj3M07OclvCu8WwxpKSv7I05kNLbC8Ba4Kbl9SdE79NB9A78AhGVqSI76dmYpf7hykxw9DSTF4JIefYeN6RoSga_Nb-iB9Pz95MFx1i_qIy5gL2SDLeuBbHedzBzsOmnp2VjY17LqHep2wWU6GPhrws4P3nCWjMOj4PQoJCjxnLZvSQUTGz9tq-303nrCpCJuPJ1hyUULM-S4FD9jy7dCzyD3U8u0RNsRo5V3qQmGEwzaVG2ifheBsZ7WBMwLJK7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6323" target="_blank">📅 16:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=E9gCvvoR1Ni5PWoTxXc1ircmO6QvrwWW91x_MOkECxx8L7SHuimop62puRA14DHsvX9IlQ1i67RLE6gxBAlfJZZoUiTm6ICMeHfoZNo_lN435TcPr89Kk5tF2Roixu_xVw2urSPx8St1r8BfztD5p-n6fPZcnaHND4lxSlwqhOKG8oMOoBoTSBlgVk7Hc_d6U-JTZijQfNeNLJrsS4982xeZrIE_ua-FEes4P3ZLy84uG-xMd9W6oxRA_B6STOTIdwSGqpUbhKpERjlORTKZI-S4M-Qda8NVWI8EJufCTf1KTIGwHL_hq_Cr9MHQMBdx4s_LFMucTD4THW0TCBlAVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=E9gCvvoR1Ni5PWoTxXc1ircmO6QvrwWW91x_MOkECxx8L7SHuimop62puRA14DHsvX9IlQ1i67RLE6gxBAlfJZZoUiTm6ICMeHfoZNo_lN435TcPr89Kk5tF2Roixu_xVw2urSPx8St1r8BfztD5p-n6fPZcnaHND4lxSlwqhOKG8oMOoBoTSBlgVk7Hc_d6U-JTZijQfNeNLJrsS4982xeZrIE_ua-FEes4P3ZLy84uG-xMd9W6oxRA_B6STOTIdwSGqpUbhKpERjlORTKZI-S4M-Qda8NVWI8EJufCTf1KTIGwHL_hq_Cr9MHQMBdx4s_LFMucTD4THW0TCBlAVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6322" target="_blank">📅 15:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7RQHYhIs5x3-tsIAJerKcypEk6alsw9FrSmHXXUmgy4PwyA9gLWNTGs19_0HmR-fr7uciVKG0PyZVaDgICTv-J2A0HS9ubHt26j48iIDCUyZzeaF77q_ymdjQyOTk1YFVOkZ3SV6yO-zxbO13mNm2i1-g2VH5ubIKXaU72JSM81I9KxoIqax_3el-CXlt8RMVhNoymiVHb6tYHBAAPUScQwT4DOU1tgxC6kgrgkGbbraNLFn9DG_urnA5puOi3pBVvus4BQLw4k0TRowybGeNDDxnQxk8HPqkx2DkBkDsQuktKZTY8QofGVy5OvgjlrS5tIsmooM4pddHk59L8A2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت موزیک رایگان
🎧
https://www.musiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6321" target="_blank">📅 14:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f4WesxVQfOHCojB52uObBZ8kY66YipIiMO093pK1XnbHtyZFKCUyfd4YZriTLfESa4NLiV_R3fNfoam6vXTqmr-_xefYRLc6wn8O-FsNzSjbFGPDwrLiMGzoPJk-WzxhoL3UjvaaTgtmCmJhn4H7in3FMxIJ9FfMyjQ5IR6LpwwieLo5yX9pnbFPO2py67yYv5rAwlKdVwIkskaBWPUZUB6sDdr6HxWeg-W5-vh3zqrP0PPuK9Ie__FMGvLt3v2tf7TKA4ayNFv6m4P30w4S4K3CmJDyD_5Lm4idcrMFREv3XL0DpKT_gP02m89ihoODoD27qUn_UHsCj0Y0VQEtuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PjgEr8IzOBTQlOH4irmPAzHGbK4PtfJv3nGQHlCo_5ARDWjxlOrhwSrKyN5YIQo_447_CfeynUtrbs3DpanANjtdUKILrIn7o_zOms77LhHcJ6OnJ1WhZAHCAHl5QB3Jb83d9M-xeAcptyc3DoUeXH3miFjGpRe0eg_ujSS9p6E3QYqV0YN2oczHtKqTme8QbzzpymMspkUv6Ow_kPoibaeFPy397QMFhZ42wV9ftNp0ETYPov85AeG8xY19Ol4ma6DIqcGPgcByNRso-GdW9G3ajVKUu3wZF2y9F_sOJ3-7ZdE5AG0h5IIw4trKMiizbVAPob6wfsor0Ht3LySvXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6319" target="_blank">📅 13:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6318" target="_blank">📅 13:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6317" target="_blank">📅 12:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDFPkQTgA-a6TP2BrwYqb307PvNr8WxPfwlR6WHkBuIHehO_ouInP1yDrgzmZnDFD6SzlURExfZRkdAzPTXVfOJWCmIrfVC3GR__2CprunMURKLBDgp3l5zF3CIv9B594NSYYdja3h9K5QxNspWU94gXbzEzO0gOb0ABKmQHUqwUAncTSYU1N3DiGA0cu5NmHRerRGwrarRy3a8nQZw5A9WykXkV2IrEn2c07idvYUm5kCprwzCAdOEo2dnxDDPOpTVCzNBe8JGbvVOPlbW0HRN1uwkBa2EnvplG6mAqCyfTWFKEvD7Lz8fRI-1j7qjJFOE1MvPqBY25IeZ8FrygIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6316" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4PydhkLTOBQ__rO9KYBxq-9OjMM4MZqxgV7QigFt7Y35YPDK92LE4WHv4ANddS1UXUGOJtSgP3R9vxyGGBsJ18-ZMjTJAmBeI4k9k-viIsgCO_ttCUqFEgCEccbP7urw1TkOj6rjFzW6T2DsliIgX4GIQir3Kdg40NQvwg8MzcyMC0qDZ_nfVoWyaZGEtlzKxExjOmVtuU48P4AHw-G4p_XNF0ixxqxlnbBBufolB5yw9w7D9Wm_CRgr-JgBxhH2l5xulBby7oVIBBcXiJvBTWMrYw8bsq5PHM6wHMQQS3Hvx-eJYZCN3Mh8zYVFGnvw9qBTg9-7etHx7LTfh8_6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aE7rPIu_hlJgxgqV-IgKRq5bOpD9CNmqATeeMR3G6dGx82jImDKg89hOBpekpRmhplUZwFYx9-37qok7S29R3zQQqMqlot69BIMPooPzGZbg_as8HG6tR_w-4HpqzZqsYZhWLWxLxdz-g1bdqqzSbLrSSejhY1W_qBdB3pkYyj6LAJ184ZzVYb6OA7TzGSTefSzt-OrS3Czq3DfnqfXrJFdsuEUDov67kuwCkzITz1xgXTZIjb6dy2uaCeqH7GQkZk5hMM9jsd9k4jCYlt9ZyZyjBZ7J3O_QXg5INd0cYGZ_-BxSSgIPkn9oYkPwILyQTQfn5xFU9AD7K_KGpBQK3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=l2QqfyftDf1zOdm0BuRHunVAwWqvybKEE9xhXw8z0guyYbzBq05g8jKJsUo8ajZkb9zBX09W5XkNLMi819CxurQ_F-ajxnkFOwDmTvKg0fZZy-PHWuZCVU-iITDKD50ud21Iq5eYVQa982Vb7R3j437TAKTHc4cBHXR57yNxkOXNWpZJUiNzCuzeiVwh9mWPCOklbLUcv7XhPuDXSsbqI_VbbO9xVxvpRtSaIkrcMWjZcoHzqoAiuVpD9SSudGeAxn3HMi-pdx2Ls96BA85ob_T58ZFRAo5o11DFqy8KSi7LXnhS7SsnjtnjZIjNd57nPPPtI7bFQ8S26EuuVk7vEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=l2QqfyftDf1zOdm0BuRHunVAwWqvybKEE9xhXw8z0guyYbzBq05g8jKJsUo8ajZkb9zBX09W5XkNLMi819CxurQ_F-ajxnkFOwDmTvKg0fZZy-PHWuZCVU-iITDKD50ud21Iq5eYVQa982Vb7R3j437TAKTHc4cBHXR57yNxkOXNWpZJUiNzCuzeiVwh9mWPCOklbLUcv7XhPuDXSsbqI_VbbO9xVxvpRtSaIkrcMWjZcoHzqoAiuVpD9SSudGeAxn3HMi-pdx2Ls96BA85ob_T58ZFRAo5o11DFqy8KSi7LXnhS7SsnjtnjZIjNd57nPPPtI7bFQ8S26EuuVk7vEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6311" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3pxfm2SlQSSZdLspo9emIHlr2MUYJHa-8SNS-7pDwRHkVlWcNiNtJLlhdewN1GiMUehgYor81Ag3iaFzdtrhKVdy60tNlb9770z7g2npiKDTzq0yxVgS-BPAOdf0bKZaTZi19Dmdq1RBak3GtjiSzQ01oy_NmqAvVFy01xrNECmnIYHP3OStM-zVrwoONQy2YGuseZg0bEOHAdyYWEWNooNSlYn5qMg5Tik2U9sUOWzMnCCwDiKcAxF3bCTsMP4zHSpAShmMSizvJayhSnyu1L8NQVMe3C6dfnezQ8I4WfZWVU9UslPJOlvMATOJkPg9NNYXdrMF0Vm2NvjR4PRvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
MemeDepot
کتابخانه‌ای بزرگ از میم‌ها و گیف‌ها برای استفاده در شبکه‌های اجتماعی
✨
قابلیت‌ها:
•
🔹
جستجوی پیشرفته بر پایه دسته‌بندی و محبوبیت
•
⚡
فید و برچسب‌های خودکار برای میم‌های روز
•
🛠️
دانلود بدون واترمارک و ثبت‌نام
•
📦
به‌روزرسانی مداوم محتوا
🔗
لینک:
https://memedepot.com/
#Meme
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6310" target="_blank">📅 11:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔥
دامنه رایگان 1 ساله!
اگه دنبال یه دامنه رایگان هستی، از سایت زیر می‌تونی کاملاً رایگان برای 1 سال دامنه بگیری:
https://domain.stackryze.com/
✅
قابل اضافه کردن به Cloudflare
✅
امکان ست کردن نیم‌سرور دلخواه
✅
مناسب سایت، پنل و انواع پروژه‌ها
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/6308" target="_blank">📅 02:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIkKOJV_CYr7blUsaQJNcznwGATRSHmeNZpuq0aRhCMljEpI15lDmc4SHoHAPX7eyYbH5Ftzzu5x1M_8tlw-DmWegVJ6Z8Jlc9AjRug5eAfBju8bayAjl0Qz_GvhJ80DhhkePGFfDLr7sG87zB_4781d_l9dLJMALx9PI0Fi5yH3zoGPGjylFQOhNQINz290o9TVKtl6ggtd7UtTZky4aekKdPGWyhVDCtF981fzyIlfxeQAJnohtG2f8UevVo9SWhU3n7No-9ggwvjMJxaCyPz_pDv_S287vz0h9khAaHuwHZE2U_GQDQsDskB_UDxk2uQqUY5N6BTOjxjewtMMZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕵️‍♂️
CloakBrowser | مرورگر ضد شناسایی برای اتوماسیون
مرورگر
CloakBrowser
یک مرورگر مبتنی بر Chromium است که برای کاهش شناسایی ابزارهای اتوماسیون طراحی شده و تلاش می‌کند وب‌سایت‌ها آن را مانند یک کاربر عادی تشخیص دهند.
✨
ویژگی‌ها:
• مبتنی بر Chromium با تغییرات در سطح کد منبع
• سازگار با Playwright و Puppeteer
• قابلیت اجرا روی سیستم محلی، Docker و سرور
• مناسب برای تست، اسکرپینگ و اتوماسیون وب
• کاهش احتمال شناسایی توسط سیستم‌های ضدربات
⚠️
توجه:
هیچ ابزاری تضمین نمی‌کند که همیشه از تمام مکانیزم‌های ضدبات عبور کند. استفاده از چنین پروژه‌هایی باید مطابق قوانین، شرایط استفاده سرویس‌ها و ملاحظات اخلاقی انجام شود.
🔗
GitHub: CloakBrowser
#OpenSource
#Chromium
#Playwright
#Puppeteer
#Automation
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/6307" target="_blank">📅 01:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):  Aistudio.google.com  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6306" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مرحله یک طهلیل من به واقعیت پیوست
😝</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6305" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkK0sDgSWT3fUwvLHn3K4b5wwUnBebEINM1GCKnsW3deNsqGWBA8X9UlqIhURdmLCwW7L-qJ-M3J3Tvo57OIvTKuYm1o97rieL81m3nX_LExs3UooDagceAtKaOIxCGRQcVOb8_8d5MKkOO3tC85VLpq6ft8nZQjjDfcbX0AnaaG0jC1lG_hPwZk6UrWEafoIpjGQt7U5UTljm-tsxl9thB3dYTcnQP4tMfQLxs4tOBhwNGqXeQl9bKXy4aSU3E6wzE5quSdrUtu5DSQ0ZTzxJBZX6ID4zDNxVzW7wIjn9Khnfb3ha8O2Dltx27or4V82hCyfAXqXVyhdggrRRYGmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):
Aistudio.google.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6304" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6303" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">📢
جدیدترین قابلیت‌های
ربات وگا
را معرفی می‌کنیم:
📚
حل سوالات درسی در پیوی
🔸️
در بخش سرویس های هوشمند
🔹
امکان ارسال عکس سوال
🔹
جستجو در منابع آنلاین
📝
خلاصه خودکار موضوعات گروه
🔹
هر شب ساعت 21:30 ارسال شدن خلاصه مهم‌ترین مباحث در تمامی گروه ها
🌐
بهبود سیستم جستجوی وب
🔹
نتایج بسیار دقیق‌تر و معتبرتر
🔹
دسترسی به اطلاعات به‌روز تر
📰
آخرین اخبار هوشمند
🔹
هر ۸ ساعت بروزرسانی می‌شود
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
⚡️
Vega Bot
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6302" target="_blank">📅 22:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PP5b-2iGBaiQkdk30IO0mOUbPKWI37hTONNoP3psqd1P4nCt5qZVYZ2ueuJjvuCIeNIEhSBRNEOc2NUDJiHuk7svdKipTaDfAYrRAjBSZ9SwQO9GEH5jgQZQbr_pJF5eQ7z1fC4i3O1eoPxCQghJLRgnuDQMfE_k2MA_k7MTVOJZKYkOJe-1SDgszcm4kyWFWnjXzqhbOc7h_MSmAWr-75JN3Hay8fIviBhBOn5piCa1OH1VhrulM9jTf5c0r5m0gUbIWRG9_bnpZVWlenavpPaNCcvv2kWvFnBoIO0TQikhExznzyi0xs2s-7O7Nr7-VF-STDfzbHs_S688I3twIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
OpenAI برای برخی کاربران API Credits رایگان ارائه می‌کند
اگر از APIهای OpenAI استفاده می‌کنید، می‌توانید با فعال کردن اشتراک‌گذاری داده‌ها برای بهبود مدل‌ها، به سهمیه و اعتبار رایگان دسترسی پیدا کنید.
📌
مزایا:
• سهمیه روزانه برای GPT-5.5 و مدل‌های Mini
• اعتبار رایگان API برای حساب‌های واجد شرایط
• دسترسی مقرون‌به‌صرفه‌تر به مدل‌های هوش مصنوعی
⚠️
توجه:
با فعال‌سازی این گزینه، بخشی از داده‌های ارسالی شما ممکن است برای آموزش و بهبود مدل‌ها استفاده شود. برای پروژه‌های حساس یا حاوی اطلاعات محرمانه، قبل از فعال‌سازی شرایط را به‌دقت بررسی کنید.
مسیر فعال‌سازی:
OpenAI Platform → Data Controls → Sharing
#OpenAI
#API
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6299" target="_blank">📅 22:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran
* دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)
///
* حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)
* کافی است لینک subscription را وارد برنامه v2rayN/v2rayNG کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
* نکات استفاده رو حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/archivetell/6298" target="_blank">📅 20:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=hiJXY3vWZh0wX5OtySa9r2wFBQO0e1omQnSEt5fOEF8VQcChtTnyGb8yJJ-pJNaZ2vGPSd80np_0SGCsoCphWhlS2WAWdnRVwDEiIz0LbwE_O2GZpB-gbGATZ5l41KmjR3VwU5W2kUxDe5_J9aBJpEquf7HUyVrRfAcpYxk2ZqMLkNT6mR91y7uV5I4ku19rdoFqkrfPbjNXl-GKrb8b-W3yGi5o6V95oUMlZc9gngijRx7pw-eIcp35yvO8245uErxl6RSkWFJY1k_61GFCpeseV8PgTtHk3yo1U26g9CH8JpKwbG0rYCstr06os7CFtEs-hEvhD7ffvD-ah1BeJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=hiJXY3vWZh0wX5OtySa9r2wFBQO0e1omQnSEt5fOEF8VQcChtTnyGb8yJJ-pJNaZ2vGPSd80np_0SGCsoCphWhlS2WAWdnRVwDEiIz0LbwE_O2GZpB-gbGATZ5l41KmjR3VwU5W2kUxDe5_J9aBJpEquf7HUyVrRfAcpYxk2ZqMLkNT6mR91y7uV5I4ku19rdoFqkrfPbjNXl-GKrb8b-W3yGi5o6V95oUMlZc9gngijRx7pw-eIcp35yvO8245uErxl6RSkWFJY1k_61GFCpeseV8PgTtHk3yo1U26g9CH8JpKwbG0rYCstr06os7CFtEs-hEvhD7ffvD-ah1BeJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم ملی ۱۹۷۸ ایران، فقط یک تیم فوتبال نبود؛ نماد غرور، اتحاد و جسارت یک ملت بود نسلی که برای اولین‌بار نام ایران را در جام جهانی طنین‌انداز کرد و نشان داد که می‌توان در برابر بزرگان ایستاد.
از ملبورن تا آرژانتین، از صعود تاریخی تا تساوی مقابل اسکاتلند، این تیم برای همیشه در قلب تاریخ فوتبال ایران جاودانه شد
❤️
یادگاری از دورانی که فوتبال، فراتر از بازی بود، یک رؤیای ملی
✨
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6297" target="_blank">📅 20:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZlDGRyzIx4eqUFmPsgJkXJV-rRyIK9ohcdGq-8pADZWZrYxbb7k2tKqDtp0GZpz0rs1OSqvGWipQtO8L0nuRLoijnWrcMTCDvpvWmvqZGizO4dhJiyPESdusB3iK4s8rb03xhSt-tSFXBzbW1NvINQiaep3idTseH-WNXdCFL4LMP2ZtB7jWL8EZJazTD4qYewQV_Kz41jNVjj1m5iz1udUlms0Yu1bWjAqY03lqy8kruzYFUa7TDoHG0oo6_jHJvRfAHJoyKfQLJ8YOUq16_-3Qi9q7lQ1DlDoI-whXGR7MHAqHyU-jUs1ffsawik0QLXS737luhtxuhZ-5D220Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
RuView
با استفاده از سیگنال‌های وای فای، بدون دوربین یا حسگر، موقعیت و علائم حیاتی افراد را حتی پشت دیوارها تشخیص می‌دهد!
✨
قابلیت‌ها:
•
🔹
ردیابی ۱۷ نقطه از بدن انسان
•
⚡
خواندن تنفس (۶‑۳۰ نفس/دقیقه)
•
🛠️
اندازه‌گیری ضربان قلب از راه دور (۴۰‑۱۲۰ bpm)
•
📦
دیدن افراد تا ۵ متر پشت موانع و ردیابی همزمان چند نفر
🔗
لینک:
https://github.com/ruvnet/RuView
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6296" target="_blank">📅 19:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اگه میخواید به سرورتون وصل بشید ولی مشکل وی پی ان و این چیزا دارید و روی cmd و ترمینال و این چیزا وی پی ان سیستمتون کار نمیکنه میتونید از ssh آنلاین تو خود گوگل کروم استفاده کنید.
https://webssh.webhorizon.net/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6295" target="_blank">📅 19:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6293" target="_blank">📅 17:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFkb6GwOUJH5cyyxD2lxJDpyHUeMspyFTXeIAiEv9fLvArPNB_kjfPiEq2BP75n0uVgUafPBLzxnMLZW8D5-VZhky9_Le8FI2BLEgL1osPnDObRbfLbY6fo1OJxUkHiSOLtS3NnGtTJpd6utulZpLXF7G4kpe91sNU9X2DbtrHDOJBftxH8w7-rhsixFIL-j0nG4jNxOCFCP1QIhXjwsZ3hIZaWVS_0qovg1LstpQ-DHSNQ_YQlMA48if5sPThIW0spviiPiqH8r4nSC3K8BbYWoHng8sCW8M4IvtB4Mcy33pJerH12tqQbBo-A7XHrPo7e_5748i3GsCKnOi5AEzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JnV7AFE1bLBbnsWRQWJMC9L-gDmYXytXGDA350K_wywuTfBn7BQVBxrGiKM_42THtJWcbjhhStgc_h6vQB24aqRJguJSWMyTrBX6aU4yebBafaXtS4CXii2YGI3N7b1y15pTgby3-xEAtLGzYpZf-sU7kY2J5q2oxuvFCNLEmNkM0Q2JTbf0utXBrCFxReoXzES1hnlUf1rrSlFlSkqtlQw2QMSw5mGqh0abqyJIjWOzE_2QBmES9I5-IKdrTYr07kS2UCFQwUCqINjtVHZsF-bFTjYfV-nmRKRjIrATRktIrxs5fWURSUhbYShjRcKjWq7DcyCkwRidKfbwio4QIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WDgK8h4bq0yV4PYJtX3Byo1KCoxnCkG-kQuRGD__QxC7ltJd2w3tdEq3K5s9rDS7ipm9lRTCNXXv13ZZyXJjlkUHx1CuVIqYoEAO6FfajgQ9JsB_DoabayxRwZPlQZuAwUZ0Zroj13AEUQ8Nx_1p_utbH18wFQiv2Vd5WGpBj8J4-Jij-14kD2cMEZopfCekn1Bo7jepe8bi9_8pR88HwKPF4Qk6x-nNRF21BMo4C6NHoBrYRID-il05tAdRLVXKe5af9bEycsa4k3SCXdUbgrpWZb0_SG5WTAyDYFwsU01aKUwyP2IIVAjtVGJRXOWA08f0-ISY-e9bSitH2Qn3sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6290" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54834411b8.mp4?token=ToLCxMI8vzuzmSP0mMOHOUx9SE3Sm8KV5Zw53hz7B9B4yGtW1IbVmVsh6CBUmDtqFLEtsGqTLkLsKIlgItq3GW7xxlLmEql-EJ1VW19EDhvfU-XKhOC5JppWeV-Msorzkhmv8T2JJCQlGrgW30K4pYofo7fKk290wy-zh7_HHbLRq2vEmaYFGRIiLMoWqydQahXJk3pN54wQRNLCQZSeAG75c-SnLzWmASxO36ftD1T7uCh21w0qhgIBSlgWB3CUCEw69svg4gQXndSkvwTMeSUpcJhA8Du4xlKiReDGXVuQMWnvUXx4zOtdSUActrkge7qkEYIXWtsIPX9TCuKAKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54834411b8.mp4?token=ToLCxMI8vzuzmSP0mMOHOUx9SE3Sm8KV5Zw53hz7B9B4yGtW1IbVmVsh6CBUmDtqFLEtsGqTLkLsKIlgItq3GW7xxlLmEql-EJ1VW19EDhvfU-XKhOC5JppWeV-Msorzkhmv8T2JJCQlGrgW30K4pYofo7fKk290wy-zh7_HHbLRq2vEmaYFGRIiLMoWqydQahXJk3pN54wQRNLCQZSeAG75c-SnLzWmASxO36ftD1T7uCh21w0qhgIBSlgWB3CUCEw69svg4gQXndSkvwTMeSUpcJhA8Du4xlKiReDGXVuQMWnvUXx4zOtdSUActrkge7qkEYIXWtsIPX9TCuKAKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6289" target="_blank">📅 16:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6288" target="_blank">📅 14:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6287" target="_blank">📅 12:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⚡️
سیم کارت رایگان همراه اول به خاطر جام جهانی (کد تخفیف + پست رایگان)
CUPSIM26
هر کد ملی تا ۳ تا میتونه بگیره (همه رو تو یک سبد بذارید)
لینک خرید
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6286" target="_blank">📅 11:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=BqpnEEPpXd26LB0MeEcT3zKeF_8Cc4hgzTgBnntm06ICmKvTXl_1jF9ysMtDqwcgI9ueRfoU21C32dUky_9zt-88JzX74uFqvXEUepToK1cqDQ9Gc3fIN8aXhpePXeDvLFaPqu37k_Uh3kFAjxoprqPglm3UGMXLwb4QNU5l0UVILmT3NsGnPVcmgi5uL8PuVtqdGgPYAZi3_snSrlGu649Gr-xqMKlvWUZljT2AYtlfsqsNXlI6wOc1EoYwf_PHkTIAlml9T1pxnR7ghiyJplGmRl1w9ovxC_XXrOpwZwlhqullg3iumpzFw41AMhzBs_K0E1wjedaTn5VE9lfEfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=BqpnEEPpXd26LB0MeEcT3zKeF_8Cc4hgzTgBnntm06ICmKvTXl_1jF9ysMtDqwcgI9ueRfoU21C32dUky_9zt-88JzX74uFqvXEUepToK1cqDQ9Gc3fIN8aXhpePXeDvLFaPqu37k_Uh3kFAjxoprqPglm3UGMXLwb4QNU5l0UVILmT3NsGnPVcmgi5uL8PuVtqdGgPYAZi3_snSrlGu649Gr-xqMKlvWUZljT2AYtlfsqsNXlI6wOc1EoYwf_PHkTIAlml9T1pxnR7ghiyJplGmRl1w9ovxC_XXrOpwZwlhqullg3iumpzFw41AMhzBs_K0E1wjedaTn5VE9lfEfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6285" target="_blank">📅 11:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4BBKm4E-ZsiRX9joAO4v8gUk0E375NUo287q4hiejEQLXS9ZdSvT_Cl32YrqwV0U82BH34OLcwvV2B3nig-S--3QOMW8DMiXunKM0XV1s3yrbhLvNn86G9ZvkHvsMPDBzwa-PnUzk3tR_vbb-Vx7o3y1iiC64ZENLo2gv6Tzs1isIzxHZ3idvoTuUUPdvAWnb78g2HRoDgcEDQVyKUs623FEqxpBtQfMaEMxWeCzm3raDwEofRP3y9ihpdmPz60CyPMfq9a5Fsc0FeR-VATBeQqaVkr-R3ZBriOd7sC1qSFE_gXP_GUL0ANsh5tvlsEvN-5v3R2bi-wiWjZR50fqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6284" target="_blank">📅 10:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=IwyGu2RAMjNGKjGjXuhHVq59wB8QMV1ioNln49Q8qsjxJ9b__BQE-ibwlRBbipPQJRKKlxJxx9Y8e639mqpykyG_0w6WQs90UbCsLKonBG_1tv9gWz2RIFQ_J9ri55ALPX5avoDUyHLMwnNu3QY1K7tz1iXlHRJEgqUHUyFXh8J7e8qHUEz4P-ZA9G3txkuCdMr1VameO6z9XkDL5nYBwr0FzYysZ73RiOokjRAKv-mTrwIYfrVKXVb6BrvfMm1hUdPvBonccpneHpcitsK5Pnmpllaeu09z-fOPc9vEKCNtvG-3bz_bT4Kbu7VzKYfOPnTn_koPqBURD5BGTikYqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=IwyGu2RAMjNGKjGjXuhHVq59wB8QMV1ioNln49Q8qsjxJ9b__BQE-ibwlRBbipPQJRKKlxJxx9Y8e639mqpykyG_0w6WQs90UbCsLKonBG_1tv9gWz2RIFQ_J9ri55ALPX5avoDUyHLMwnNu3QY1K7tz1iXlHRJEgqUHUyFXh8J7e8qHUEz4P-ZA9G3txkuCdMr1VameO6z9XkDL5nYBwr0FzYysZ73RiOokjRAKv-mTrwIYfrVKXVb6BrvfMm1hUdPvBonccpneHpcitsK5Pnmpllaeu09z-fOPc9vEKCNtvG-3bz_bT4Kbu7VzKYfOPnTn_koPqBURD5BGTikYqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6283" target="_blank">📅 09:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQ7v6xYjUCbe5vimTM-Y_JW8c3Urd2DAy6PoyqPfOOlHdEmjQGulyM68WSDbd8cF5NcmL0i-f5HP_fr9FAvfi5779Kp_eGWqSUQlB7tQkH_FbiqcjqqEySIsV6wOCsEkTL0NQtYeB1HD42IjVu8DjYlFrKkKE6GpDxRpk5lzfXuPR7LCoalh7VGz2LobLiCcR5qiVVIRXLR-v5HQMdt3Hh-Qe5cO1c7qF7WLjhWhKl4SRG8tV31Yf8pugBhdgZUs3zEIlys8_W9id9RgPtVAwdUUmPKihEHbVqHBheXxqsBOlNJPuz2RVY-yGJtAXDoueqXVu0al7RYaSkwF5gftGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6282" target="_blank">📅 08:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OO182w5Oi3vITnZWCckAv54QXBOfR1_NJDt17PolCF71PFhdMkMdNOcHga5eAq8NbTVUQ64HY_AEKmfpSLQP6mZi-Yf_g4VqGoUWIbKHLGVICFzeLis85-MzoLVrCbQMy_6jHzjcgf5XXLaV2qc6W0ZQqG4jakwCqZ2EF7I9evZp6Mm6tMtKnuWq5g71jha83xW8wHp66sEvkq3Tzd5hico_GsdAOkDUHGJoiJRmDGo-QDbDaoexZPV9fYHNSkfYBNioXf3U7EqqsZaVxckUZNrw_0ZpsE3AOlngMikK_R_xQHgQRrQc_Ef1mfV_S0_cHj0_1FwGEM3GtK_HbPRvDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوتاه اما جالب
❕
به این صورت داخل duckduckgo میتونین qrcode بسازید
🔗
🎁
@Archivetell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6280" target="_blank">📅 03:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6279" target="_blank">📅 01:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚀
راه‌اندازی خودکار 3x-ui با WhiteDNS؛ از صفر تا تحویل کانفیگ در چند دقیقه  اگر حوصله نصب دستی 3x-ui، تنظیم کلادفلر، گرفتن SSL و ساخت کانفیگ‌های Reality و VLESS رو ندارید، WhiteDNS تقریباً همه این مراحل رو به‌صورت خودکار انجام می‌ده.
📋
پیش‌نیازها  قبل از…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6278" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=sWFZVDpX_5EEEEd6eNvoCwHxE_hxJc-PwAe5rMItBcJ31818phBFBmiaxH2c3h_MWuc2J4J5yONOvbjE1sDZgA79rzdgvb6JQ-coV6vBmi_Df7EFkWG_VwqiPmDZqrCTnNcVwCGlfWsGCL0WQwd2MYCJk1r3Z2xOP4x3w5y1Loneg5PyW09-UYfBmhkr1G-4LhZc0S3PVj0c7WkMnuYifkB14pjD72aklOUlEMRdsrV3TxwGG87ORoyTSQgGz6RBaY6CN3SfKAVPq0rOQt0xS4sSctSC_5Oezcwbuxs8hkck0mw4HEL2wQMOIErbeN9E0kkdWh-4z-wmKCoG297xAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=sWFZVDpX_5EEEEd6eNvoCwHxE_hxJc-PwAe5rMItBcJ31818phBFBmiaxH2c3h_MWuc2J4J5yONOvbjE1sDZgA79rzdgvb6JQ-coV6vBmi_Df7EFkWG_VwqiPmDZqrCTnNcVwCGlfWsGCL0WQwd2MYCJk1r3Z2xOP4x3w5y1Loneg5PyW09-UYfBmhkr1G-4LhZc0S3PVj0c7WkMnuYifkB14pjD72aklOUlEMRdsrV3TxwGG87ORoyTSQgGz6RBaY6CN3SfKAVPq0rOQt0xS4sSctSC_5Oezcwbuxs8hkck0mw4HEL2wQMOIErbeN9E0kkdWh-4z-wmKCoG297xAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6277" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=FEpw7d5SeqN1f-YeRgZS51YZaegWO7WEdTMZphwvkop1Tmj06DMzmCX_Lz9zrDpDYtE-4WkY8xFJDU_y00g55zmAIe09ZXcWHPqqCyfGRaXE71Sj5pyXXxF7OYPqOp9PyH_1KskAD82geXOTwt2SgX18zh5p-d_ggXr5U51tOqBp05UjaEJnbuB5ClYqk6s4qNDiEu9rb1Ye_uRAAYlgon2adMZA7ig6WFvtK3FY7UIllBmX93dQXyhyIPT9SSKxhubNJKlOv2LqPY3Duwc0hyxWioyJif3725T6W85e1X8FZ_QctKnr6Pq5IX2SgPYWNJIdP2lmOCVTi-Jl8r-EsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=FEpw7d5SeqN1f-YeRgZS51YZaegWO7WEdTMZphwvkop1Tmj06DMzmCX_Lz9zrDpDYtE-4WkY8xFJDU_y00g55zmAIe09ZXcWHPqqCyfGRaXE71Sj5pyXXxF7OYPqOp9PyH_1KskAD82geXOTwt2SgX18zh5p-d_ggXr5U51tOqBp05UjaEJnbuB5ClYqk6s4qNDiEu9rb1Ye_uRAAYlgon2adMZA7ig6WFvtK3FY7UIllBmX93dQXyhyIPT9SSKxhubNJKlOv2LqPY3Duwc0hyxWioyJif3725T6W85e1X8FZ_QctKnr6Pq5IX2SgPYWNJIdP2lmOCVTi-Jl8r-EsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6276" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=vKmqsMtC3AprcYhjQuFOhV02L_xVL4BbIoa3Dy447F2WWCGOsEAqbEQA9VI5LQxGS36cGaoPddaUTgvDcQzUIJQarFmo1VXAgMjN10MltR6VpdWnT96DyZnfdXSX3epRVDjEFy3PwVRBq3PDOi2hnKdT0vER2ldHp_DCKGrjQpn9ZEl9-RFXaoJksvhTRPm1K31SmA957roVM5MPh6Os8afVFj9ekyeldhiOjWScBQHZs8NcTmjvJUDZNC_JsfrwECwNrcLOib9ZHr2lSB1YFVpDk0ugjG10wDFdn_vd0MWPVXF3_pDgIm9d0HMcxzv_UllR1WENDZkcOwpQu_xkhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=vKmqsMtC3AprcYhjQuFOhV02L_xVL4BbIoa3Dy447F2WWCGOsEAqbEQA9VI5LQxGS36cGaoPddaUTgvDcQzUIJQarFmo1VXAgMjN10MltR6VpdWnT96DyZnfdXSX3epRVDjEFy3PwVRBq3PDOi2hnKdT0vER2ldHp_DCKGrjQpn9ZEl9-RFXaoJksvhTRPm1K31SmA957roVM5MPh6Os8afVFj9ekyeldhiOjWScBQHZs8NcTmjvJUDZNC_JsfrwECwNrcLOib9ZHr2lSB1YFVpDk0ugjG10wDFdn_vd0MWPVXF3_pDgIm9d0HMcxzv_UllR1WENDZkcOwpQu_xkhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6275" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ادم خودشو باید برای هر سناریو اماده کنه و باید تو پیشگیری خوشبین باشه. چون شاید همون ی روش هم جواب داد</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6273" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">همین الاناس که ترامپ میاد میگه:
دقایقی قبل قرار بود دستور حمله رو صادر کنم، ولی آنها گفتند ما مذاکره میکنیم و من برای این حسن نیت آنها ۲ هفته حمله را به تعویق انداختم.
ممنون از توجه شما
دانلد جی ترامپ
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6272" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">برق قطع بشه با کبوتر میخوای پیام بزاری تو تلگرام؟ 🫪</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6271" target="_blank">📅 00:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6270" target="_blank">📅 00:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6269" target="_blank">📅 00:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6268" target="_blank">📅 00:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6267" target="_blank">📅 21:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eS84CI3Kd7xMTVlWOcH5Gxq3zvUASHSdsIg-g-6FGYoQbVAMKTte85mGEjk5dMeIvLIkqnrAc1sJno1iZ4qKACMTmi_wNOrtVhELaM_7DPB9MfeQp05JNa0DZhtwlflDx4oOCFzVJ9Ns-xm8Og8q9Gj5_kP2Vd1vtPJCB50CEON-G5TfCcFCcmYBp82XG7EpEIDZpIXpxU0UD_eJ7dZM1pvn_lSp23oSBWW9JEOEMSPwrS33ztkGadofQp0F58110IEvdBqO-jrOllEtJGw3EC6n-CTDZufDYIpt4A5zckn8gR5SziruhmD_BcaQJ7Oci3qIxQZ0yk8VPTNhaWBUlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6266" target="_blank">📅 20:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1_RMJpsO2N4igZ9BO7aBfSZTflyOTmu9p5cgybC9G9wenk8WJL8N72gtQ5WXZy9cD9ogOZN7BzAT2lRWZPjahmlnQygqzzhhpXKkrR6GB8-ypiR8er_ZpVVySQiFPMWfiUXtFpAS2qUe_mdR2XXtCGbusELHB1-z8SgkZnGL4XyHq54ZNfPkCnlhczBSANa76e1EYlrEbWKfUSXfm_yS42PP1YFp0pig_HDqIyTC-Bzijg8xHURbfUhDAV4bTGsEa_PTE_IRCTcivoJCHd3M_wAa0sCaGrlZ3qskpUwmUz4RtQR7JGarqz2el-VFO7Cc3dfNqGgmqA_or418SlIsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6265" target="_blank">📅 19:31 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
