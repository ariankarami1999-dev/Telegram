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
<p>@archivetell • 👥 9.66K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 12:20:57</div>
<hr>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 424 · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A4TJx_LKKgfHazaBY4XvHrqb0hW_D8hA8CYoF5i5LIqjGLhx5T4stUGAuoJFS4Jqd2zJZx4BZoKiHkkRXu3ic6X6YIo9k4KOIwpP6zc-05cK020wzVlnWT8dXrUHCWoeLq80oPhx-DjIK68yg6TizgdbZVRx9oPnV87_pt-3j32-ic7fliavnXHpRptyKQOg0LCmEWJR8xMwSk3qYcd6sXYKkIce2sRqTzxXwvjOOmvDhIATb1igiMbFoUK431I0yFJmocEEtelRHGrTns4P5zG058wYalk7o-rqq4pzwG9MxI2tNGMBgGIPPXsML1peL-Ao_sK5x2vhgEuAL9GpoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت Ponytail هوش مصنوعی را از نوشتن کدهای طولانی نجات می‌دهد
☠
این مهارت عامل‌های هوش مصنوعی را از نوشتن کدهای طولانی و بی‌فایده نجات می‌دهد و به جای ۵۰۰ خط کد، عامل می‌تواند فقط ۵ خط بنویسد.
با Cursor، Windsurf، Cline، Copilot، Antigravity، OpenCode و Claude Code کار می‌کند.
https://github.com/DietrichGebert/ponytail
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 831 · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
متوقف شد
❌
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbqTPImMueLyCxTymN9YhWF03AT7MzYUUKIqvy7L7OHzJVFguqAbEETGaAhZwo5mNw9F2KWfecSUCeNZkZ8oSlbdPDUQ4jrQZPK_ywNSmSHpjpZ_AC2A6B29cDvVKop2KpCj-P54Jb38rQBTmDNckJxERJwg5xkmu87WLrdg55CGTL3eydUBoNbGs70DP9MCQ5NDFhbED8qLz74-ibGxxPRaFElC6CYZDd7bknqigztRpM1vZwZKsA8GMxwymbkM5DKpQ-3PQ8Gp_ziAs8HVTFQiLbVLZPJuf_E-UfgucoX4Bwhfx6MJNUate1ZiSOqFlryhNqWe9NkCELsijsLZKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZ1YdhqOPd08WL2ooZXs09wfNKWod0shur6oPS9d1JN1R0THFLOIrJXfGEnrB38HpI9Ub34dk8yLI7UnUUsr4z2Stnr9Z7ZdEIKxvAwrjZyW-IV2mHEXUnTJ9ZqvzM1R-P8Wo7yr4_ROepHNcjAP6apN1tfEEyeC1zLYJbaiqr-LAZlJBaNbNIx3L3MITLuZMwqEZAl3Diwr9GRgIrCziqsoUkZreG8Es12KYrjGu9in97Urm_N6Mkzr79Nt1_jCevQsAo10vKZiZbmh2_E2CL5guKbRlFQMCRcPlr-xxfMIiexVUlGXV3YhV54mf-KGtxF5rY3xbgiGJD9AKSXqGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKYnqb4rF6U0G9myL2hWHmkICLQVnb1eS6QzQVi-XR5k6TmCUz3u5xZKtXFtSTF5DLnx925cYVmpbGAIpK6Q8tmeJxzvImzZOUl_Gfc14Ta2aFlUvN8-HJRsf0lD4H4H21mkUskgnRwYjCX5rH8G15YRtvuwOPdfHxkjTu3pa6JE64s2ViZxwgLLgfYnzJjkqmPBVPo1dj5IBbCM3IWSzFx0S7qIw9hhOZnrnweEi_WtP4CPBTmCw4FaFpIlsGjACwx02pwEZW8U0kC5kITmaUauUMkt2vMhSTbRPkWoBioVYXWB1LOj4X8-0UinLYdvKfbmp3u47UdSqHXqsWDAtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbyxPSuGsOMMuicqvQnsqgOsZCup0h7uiBTu8KkziIkld1-rf9rx5Fdjgxd5j0CLJbGffb-1e1KGqEq2OuZYb1Ifi35pcVG-Ancp5Zz8jDFG_PBN1nxMqXcm7qncurJC_7KmlM5NT3vUo6yYGkwUGDgIUP3zIAhflJXX_F781qrOB1jTW_dG_j3OIVXxRbzWp5SU5T8xM6zkwaot2NINlqe3yPXQlSBWfGypKAbEWHGDOuNWQkPGsKvLunzavrxjr0Njj2unFSylOwW81mONxYCELqSp9VLN93zNuIJhzXTSxq4QSB_HQLfZP9_eXcgNZTy2vqki5RmSh08O4DJZEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxsIgowAUPTvC9_P1bODCtpnDFmoOg2xKfP2qxvlZWaG9iOXJn3lEDYc1xel79Wk1Rw03JC3SoH04vcNOdmqlMMqjICGmuOGuOdyR76DA75K52e5UYDiR0LGaHvpyS6HNbE9VNorbRI10MBXSv6Wnc1bjpl51FPJpphUaolq3tVVesLGoWEELnYi0gRy8eaXj0TPLwPaud5I7jQFYQM5ibkRzixc8y7Dm7CD6Or8jJvx4Ls5FMueFUIRjsNHEIWYogxsBph5mFDV9cKGIpxvC-lFtwoMq7nBIYbUhLxWefsbs_s9vaG9HaFgXnkhB7-x6azDTjrHLi8PFStG1-YaIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hh3DXehPP8XLz9qs9hYnELheuHa2u7_9q5ra5HgCmr6gNKzp11bJq7s_c-VRwczy9TzTgNsd5nVe9g6JZPrPfxQ1LXmW2sXPwxTvi_ZxwUhhYDirCUYwV9Z1Xt_p67z4abtKD-43A3Hkm89ocq2p8j-U6ewKVFHGuycSZaFWvOHt9siXp73WmjlIVuWxWNVP8i-_VYv6jMuYD4cpGa5cwQP0EVptOu2G91AKtOfl59Tndwjv0-uFKaj9hgwWqUZg2SFbhbcsfs-KtawhoH3xrslNtoVUJ6LQmsl5FHiemHzL9uAo1GPSv9csQECwLMR1kI-r6BZiZTN-yZzEgGkd_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xh7dcMa3QIzGh_QvdryUNbAOjPVAYkuji3e1oYFImGLqHdmFnl_7wrPEgnxKwP2q0k_EKqJ0oPMWtQfyfeogPEEcKKbNxiB_ZZASDEhpGIuMNgC1PBd7HFWGW1BSfmyxG3MPCGJM9p6ohXu_CLN3j7B78afpONe9GxOnktEpvJzYYUbn7LqRrhUEC1CAKhSUtZXEMpBawGKbjvES56XjAgTAN41kovTjUl5Cny-EaJ6qbWbITH5uJZX8DGTYC3rjb_qyP4ATDrJWcgdlGJOLYw5A8O12pAumT87-cr0FKrO28C_5ghBsyZ5FM9SJAD-Aaidadw7NjguN80wQabeZnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=qfBpeu9-bu-OKDAgbP7S_wyDNVn22Pd9TbjeVj1fpIStSNqQuJ8-JZIkTtufXI0daUwiN3-fnHEigJLjVR3-FiczYyEUF5XwadLyCi6dRJr9WSJs6PunHOmVehW-dVHFbHUHT5FhBFkfKIf3ZYas-opYpcSnx_kGynyaNRufNT4X6KeaD37j9T47lJEQ0_DEHffHzy4FX07JczvSf-Z4rpHSkTUG9wVJ5Man75HMwzx3XU_2EcWXRYJVor6sb-R3-5Mzido1u1F8ZhyYzU9n9JjmmLOeU168sO22eq4U7OZ01SfguZvSzh2hktEXVVq5ZKqvp06kNKh3AdtzuU4Rqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=qfBpeu9-bu-OKDAgbP7S_wyDNVn22Pd9TbjeVj1fpIStSNqQuJ8-JZIkTtufXI0daUwiN3-fnHEigJLjVR3-FiczYyEUF5XwadLyCi6dRJr9WSJs6PunHOmVehW-dVHFbHUHT5FhBFkfKIf3ZYas-opYpcSnx_kGynyaNRufNT4X6KeaD37j9T47lJEQ0_DEHffHzy4FX07JczvSf-Z4rpHSkTUG9wVJ5Man75HMwzx3XU_2EcWXRYJVor6sb-R3-5Mzido1u1F8ZhyYzU9n9JjmmLOeU168sO22eq4U7OZ01SfguZvSzh2hktEXVVq5ZKqvp06kNKh3AdtzuU4Rqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pi1IrOHuZrSr0fTKr6SbAXZG15jsVn0aYlDRkixzyLhMq-q6vMm8HsZ-Oex1G15kirgf-BJcro0bkyun1NIb434lfkaxAMzE3dotEUiK6yVoYAiGaGXUFeXLuzZMti2x9gQU37jylePC8UU580_R3d4Ay5KWFU-8VUmsug2CvNaqM7cOqw2B9Us6JA9ys4wQIWZs1n-zBPZp2yS5ppe8zfVHC8Zr3Kciw2fc2mcLqiLbur_XHkBsRVECCS80gMkqwoqytixxl_UVNN4oZTCtkigQK6dTjILEjfNcsGjdynImbpimdPr54s4SskoTtiFThbMYEtlSKVXXFzkri83yxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KymXwN5cjkM5JAEa6v61YkN_Uq3Akaz6BSG06VlnVMO6y0OHZtt4j6qlhxJBR3mHaAfotO0d9BmrncBgJi94G4INgkgjdx0Apeu6_X3h3XCeHVLR3BVfLS6VKuNW-_Mdj1ZgF74mOHk1ltviZCUIMdmVmTA8LinNJ6xbKwuEROvx3pRy-sWNkyHgdtdEwj0-mmQeu7e8rrGFVOGW6w2Ldog8KexHb10grtVDykBOPMW79GfPEbOny5gHraLDFY7ry5EWK4XUR_1oEViSBLzYai1iq6QHDF712gFzRQp4yBKq6-soCH_n2py729e8fNfjVzCXD3UMLG0uFWgSKrD_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=Yca96ayTfkKR8AQgug8UxR57D4tgplG2lrViLXi_MpIDGS8taomH7hWlFP_YxLFQuUPkVumFEXmCwauwmG8lKYStRQhI3s3IrJkwpT1ufAH6kFOvba2zHXRzVLHiXlXhEPoOmcy42W5-iq6keovKnXDn1UaLw1adu3sOMk-v1e3vxs2s7okTyRFHPfO_1v3HisoDpc2sP4lIexBblrugqbAebvFlIsO5qgsLuTWHNliyzDkjVx_KK2_wiVV23t8d9Wri4YYP4bBSN-NEX6AGkCXmiRa4NjP5oy0Awu5tlf2qtRFT_CS8U3g6b80lpckbf2xOw4V_RMVx5L4ajpzBfmKJIEMFWioR-5D0O_g1AIT0YSYY17vhQlJwXV5AV96aIr_dfGfRYkoUwYA11XKhQ1-g_-EJtu2h9jmmEYI5Jt_ztfihZe0Q6_TK5a-dTG3dptIKAfUdJ8TktgxsJXCPnp7fEpqm-g7soy7QBLtHx7JoDptBtHB27FHMwGyoMAkBECLjlWR3Q2RUuoC28ALa1XD4Dao-lMQ85YX4obPUR2UEpns0RfKqMCe3crpX5MT7BURgopvYAl7o55KwTCkmrE1d6-t1pvxPK2nGLGA_bFARI6pbTOFUYviW0dm-SSKHyYCE6WsOsXyEB2fr8YogXXF5gvnUnBYQr_ZNmr3IgL4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=Yca96ayTfkKR8AQgug8UxR57D4tgplG2lrViLXi_MpIDGS8taomH7hWlFP_YxLFQuUPkVumFEXmCwauwmG8lKYStRQhI3s3IrJkwpT1ufAH6kFOvba2zHXRzVLHiXlXhEPoOmcy42W5-iq6keovKnXDn1UaLw1adu3sOMk-v1e3vxs2s7okTyRFHPfO_1v3HisoDpc2sP4lIexBblrugqbAebvFlIsO5qgsLuTWHNliyzDkjVx_KK2_wiVV23t8d9Wri4YYP4bBSN-NEX6AGkCXmiRa4NjP5oy0Awu5tlf2qtRFT_CS8U3g6b80lpckbf2xOw4V_RMVx5L4ajpzBfmKJIEMFWioR-5D0O_g1AIT0YSYY17vhQlJwXV5AV96aIr_dfGfRYkoUwYA11XKhQ1-g_-EJtu2h9jmmEYI5Jt_ztfihZe0Q6_TK5a-dTG3dptIKAfUdJ8TktgxsJXCPnp7fEpqm-g7soy7QBLtHx7JoDptBtHB27FHMwGyoMAkBECLjlWR3Q2RUuoC28ALa1XD4Dao-lMQ85YX4obPUR2UEpns0RfKqMCe3crpX5MT7BURgopvYAl7o55KwTCkmrE1d6-t1pvxPK2nGLGA_bFARI6pbTOFUYviW0dm-SSKHyYCE6WsOsXyEB2fr8YogXXF5gvnUnBYQr_ZNmr3IgL4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=uqUropcxIpQtA-m9mHvjcpS13GTvwE_qH9l4x5GHbkeQk-Sg3CKN4YvCxdhB7K3xK9tGojuyhuvHLfWAF7qFyzS8ckwCXqGHeeHLXyemTYJgbScnJYBr7lIvCDvcv3DN0jzc2BEEexKyPNdovC3BSxWSyqSulOgjq7NCmzCnpCfGQX4AUrgE2kZfT6iAG0J2c5PIuHuN6RCziHCpdBS_ynWX8Af1z7L8lfA6t16oK046THpDM4B0ogycq5z1rSjh2r3czH8Y4caEK1TJrjYDaTA2dRuOe9dhUyAT-X8GLyn-KrGYVQPq8jjQspQ1TCUXIrtS8ECzpwN1peGDW_1MQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=uqUropcxIpQtA-m9mHvjcpS13GTvwE_qH9l4x5GHbkeQk-Sg3CKN4YvCxdhB7K3xK9tGojuyhuvHLfWAF7qFyzS8ckwCXqGHeeHLXyemTYJgbScnJYBr7lIvCDvcv3DN0jzc2BEEexKyPNdovC3BSxWSyqSulOgjq7NCmzCnpCfGQX4AUrgE2kZfT6iAG0J2c5PIuHuN6RCziHCpdBS_ynWX8Af1z7L8lfA6t16oK046THpDM4B0ogycq5z1rSjh2r3czH8Y4caEK1TJrjYDaTA2dRuOe9dhUyAT-X8GLyn-KrGYVQPq8jjQspQ1TCUXIrtS8ECzpwN1peGDW_1MQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/6348" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqDXoQreeuNW6CdnqXg9bCiPbMmqoE7wDwbS4U4g5_pWn4CtStUM8mw7WP7xR-G0ylUJQ54QEUr5Z8_A1WhUHJg_-HyK2V-22DZxiIeTKc9bd50ITbJCzj6rGLkwN2EKQ6nXXpXPbBgFkfYrjRkH9_pZ0M_eS2N0gA68iyZBdOXRXNRX2_l_oEvorT6dnsDINmBqX9wG_-iRhmChyxJSKMLDoB7bYzxPJt2mc24lw1yMQYv483HhJkNAH66CTKWCllmFlVh07NhLrp-ycpOiIsUS-AONOnzWKm6fDsTpgZY-zmiQosEGqGjQ5etdyaB8-Y3SJxtwrwzxFE5I81iojg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکن ای پی کلودفلر 2
نتایج این اسکنر معتبر نیست یعنی ممکنه پیدا کنه بزارید تو کانفیگ بازم کار نکنه
بدون vpn وارد این سایت بشین اگه باز نمیشه واستون از یه
اسکنر دیگه
استفاده کنید
https://cdn-scanner-pro.vercel.app/
لیست رنج کلودفلر که پایین میدم اد کنید و اسکن کنید.
هر کدوم که سبز شد بزارید تو کانفیگای کلودفلر
با پورت 443 تست کنید</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/archivetell/6347" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evLXYRK-v8ViUBCr9cL3nrpakytHYHSL7nrmGX8oxcIwM9WgeruXn-32BTYuKit4G3SAZekTIAAfVpVW7sywLiKf9xuboaPG3aG9pm-J-EAGA29nZhD7I9CcXD5U8Y8CRda3iiujBD35izPx5XbBToHE8eSxfuy9I1v_dlSjzOePhyshIlPJgAZSae7wDY0VR5CmTP3pzHyWaIE77EIag3n-6f8Kxhy57BIhDGXj0D1rr0oWVz3WA8Sz1CdD11swIA3mxCGZrltH0ReVgAzESSw2AnIZMnqwI8dlN0TPkeylQ2_M1cFjxWLNSqQSZTNp4ELLyTGE0xb18J2YeYFIwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hIEyAvMFM8KBZnbm_7pTquC2wALAgV7E6y8zy6_9vDS7xAsLiB0Dw-XvQwTVG_lyayNQXyWV652lUOI8AZJMSe6q5m_UlF5DnoGVnO0ehUr6WzTWyStAqaGflgxqfBcaoMOducYLykLybBi8aJtUK7Y5lJrpzMZD1aB3lPLLrg-YLZ3GFKuZ2d9_dsEN7UcFGY7bcNA3iZAUDzHgqo9bSRa2DVJpHCypyKMUpfrVCEZipiUwDgolPmjNwPt0zMo-U1rIiYDgX2famDfT4Xg_cwQoXfI0S1CICBU0PCGSgNP3UsTo63Q0ekUjh6alBTuxwm-kpGGzQCm3TbkvswsyJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cPdKfeXPRO8XEH_5f1v_4l7GluDCGspfz_808w9JtuGqPQgONeWgnQOkLbZdAn1AsDE7NlFv8lMrY9DuXHQBdinTsgMxkEGdKuNKsjfpdP-iTFBLXfK6Do2YlAJahoRVU0hF8jnZgQZiETMNloQUJ2drGyfduFxMIkHnMO5bUrIjF4ZNHq7gWov6AD5mnjZbnizlU2oPtGCtHl8qPbyBS3TMmNefUCEiQOhVkJ6IAeSS3ZHUUMgnWptDtOcKbhuwNex6Jb6gFuYhOzIj--d6GTCrsCWIu0MwsytJbdBP2swJO6Ur7moesxG5T7LNNtV6AIQS7J2jRwOhcxQBILjYRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ShAqrW5m6ZXqUDSvC8Js9RAEcQvnEZB-POK2LGvqtincRKkmldRvfOEW3A75MrQpVQHeazrNdvmvyZvel37_VGI-3NwwvwFuB2VO0afBRP_Ta_f-kxE4waUnR22vBaKnGkWeh6X7G21Fd4vpfRvJedar_95VXIXw7rQH1GTxqslmI6sQ5WAj9dQ70oRitEhd1EP-AWzcPvCCABrpSyv-BXalcFxf1BibuNWRfQObVkI1bodzL_j6_g8689Em-7LYW8kyOqlUtsWx-fJCIEVum3xzY7uq7RRpX85tvCnoiWqa-qzBLqfw6cSp61WJcweC1ChSkE3qAeXSCLkFFQGx2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">7. به صفحه اصلی ورکری که ساختید برگردید و بزنید روی پیجی که ساختین تا باز بشه
این صفحه nginx که اومد یعنی اوکیه اگه ارور 1101 گرفتین یعنی اکانتتون بن شده باید یه اکانت جدید کلودفلیر بسازید
به اخر نوار ادرس یه admin اضافه کنید تا پنل باز بشه و پسورد رو وارد کنید و لینک سابی که میده رو کپی کنید و داخل ویتوری وارد کنید.
کانفیگایی که میده اگه پینگ نداد نیاز به ای پی تمیز کلود فلیر دارید.
مثلا این رو با پورت 443 وارد یکی از کانفیگا بکنید تا وصل بشه
188.114.97.6</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/archivetell/6343" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpQ6eLhCZdUtg66p7NtvD9fnHXATkAxFC2Ve1giKvFvQw9d9-7780sAikp4g2xbb0HCulcxWD-jinqcH7Rrxcl0pHH65qLkuhVM2NlUDVb2XBxwfSPeHLWBsn3T7Zy5wnesTbbFtKWdYt0lHZuPPkhqaW_0hQKjenma6mvBYci9_gwBolNoiJ6LENwkjByEZXiTCqvmproSyPo0sPQS0rHfFIt7JduZR1MTak1NNq6befz-vqBPA7-cXnunQryPY9mft9fV-vo9GTQcan_KyDp2KVFaTjfqha739-p7TxwzArDZCBmgB7CtSSzbo69xB7XxvUm5p8CfdoZzocXjerQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4ke6fhy1xf31aB32NjEQIv_5J10LE69aBvGgqIv1_b0imbQq9R1_aGbTolat5Z-WgpWsm3o5_4svERW-fTn3E9z80_o0ZTkRdwuKY7vw-PtAPQGE-_VEoADXKa47QiTfjSIo88myujKLnL5wc60PPo2KPnKhw3SllxtwutR5DS1cHfXAkaDGi0NBT24KqEdC0Gj6WZjo6vYz44TPEMSU4udNTi50jqrRJbb-bTP4ZkypexMYPCxDSuh01X7prdytpssryJV36rLt76zu3hJe4ZPBoJYO3MTEZkn0_FptiY4Ff320h6RmDJOhxkAOZeHy3TIJU2iwIBqoRb2KNpX-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1PiIAY3s5z9KWJSRRYQarI2PO_LG1ffhTQSe0d9CoZgnzu4233nfGtWPYUApHLFpH1DBD4x8OWmlYonkPdq5LeMmxxI8jUbQdQxzahpL4A4kRhAyZxwrPpFoSh3BWzSP0sO-JSz42MXTlMMLIUDjuotstyBFJo2hSk6Y1FFsir0KuR2moKk_xKaBctHmgpng80rImLKV3dBkmQs4cWxo69iLvLUCuZ5e_yzvdOIjP38B2mUixnhSAbEn-YoMtTW0JzWbjKSwzMtvzPkfcWM8UmxRs7eGSsEZj3Tn0V1j0yHTdLZeynqjAiC7gNInbvClRKvDRAkAk5p22jpXlLXnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/px7Xy60bQI_YcbrcmqO8Ox82X47ioTuVrp7Rrxh4nnCx6SPUwe47Cwf8SjZi8aM5XAA1vewlSt40o6xf3QQo4Ywuesd5qYsgE5t2obAZcWN8LgiBnzmpKovshVIy6-HIXGCMqvlHjSmirZL9L4H5sVDtEVXqHig2hDDOrpyXw9Nwawj44A3oT8S02KFNmTIsKfeYWFl92RuR7v0smMPgi1xz3Kuy59bNsPw4MefvaPfzNyRn9-7nuzGTrU6VKfJFJyXBGil6yBtLzqtpuPFH8_KOqfZM7wyD3__NeSul34a2vyuWRmKa-Y0EvFXQNi75tSu25T3q3n5YLXn1NR8Irg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_tmSmn3ZDmM2lulhBuYw17zZOquuFEySFMU6OjKuGWsMg7vccMR2gLRNTnPchCJdKLozTttxvD6mER7fKOTTMnzMLWBG7AXB6hyOrXC74vNoFLMcPdA1Vw4elgppOrWVcTV6HJGGmVdzeLUysoxGnJ0Ta8O8TMHp5n1yz8hdDaJdL-eC09PrydmCB30qqBnKJYqcjP0ZRpPjxtaJQxU0pENacuvm6FUTCvVndamF4u3h2LjVNfRWG193IHiiEnNfOw84lpo5JuclN5EZ5e0EB5MdnTXm_0qdiGbBQbi7RQOzsxa9fefIEKEpdejWQBvsaAFrKSaIBQEXZJFXcAglA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF78xRVLBK1n_w59KCg0TSoDsXzK99CXE6yWTidsM9p0yizfjW0bUvXTfVAke0YRfvodNUqaFMr2RpIzgb4wjss3R31cPKtxaZuQxxm1DIFA7FSOvGr8ne0bfFjWyFnGjbnbP-aqvGIg5Q8WoP3FrrIVXY-_MWXZgAE7kEYt3Sf_b4yQP009m86VDEbW7MhDm3tLq_lpCOAYRzqiCNstE6LcK2l3QV_wNKHJegHvB17eOmVypbbFcIV87QxHVBOnqfcyuty8qjOLELUghia8Er5jTCh7yOHOBxQAFSXBF9iVUV6ysAQcix035mW76A2aFIqh9tG3rjKDH_tQwNXY8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoOKxbGjUO_k2fUVj3irgyZrRZYykB6paYVleH5cE2QdhckBp3zl6WFbYw2ekD09WmZEzg4ytF0fGz9UN2q6-IkJoSTJGJWCjvqQrOsJ3r_Cml1mWbyFujeM3TY1w2kCr6bmOK2HtkuiiuaqisUSU_IICdKeEpw-rz04uxYLjZuYYsBg62NsM0RLUO4FvQgqsn1ST3Zeiv5Hw9_ZVAFBD106XXhW3nDNfrywOV0jz8RX_S7bUtI4ScBcgzPU-Rq0roDLaThXsZOlyplEFiSbi0EguG6RYbdO_Vi34tzYGoqmrchFsMitC9MvHtoxAAQAfm7XmDZA_fTZn34jp2dgkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=H0KW3MwmRLdvrkao3V2zwiR3_rTL82BVwI2YbrpTahYWKRwvIb9DWZL-9kLfmoh0pLb9aHOtFUBOU_mcMkz63JxdMEUnuIZHFn2tmBfy98IfRM-cnK4ssvevZaEO26lIvOCO6DPPQ3k0_auR5W-w0hX6YySSd1UTIPbD5xJ7lgyZDVMQuVvm2XQ_w8MJTDyeg7b9WHZl4bLC_dy3qZcKTGr12OVfjXOzUSgQZNuA1MHzvZcrSGvBXZ4B-na72is1KqE6eumbiju39b5H26AwgWlP-ZNGg12GmJnIaw0m6hB8Db2qI1rN0EK8ciXRgLYEhLYjVYFXo8lHJ1q4zRyS9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=H0KW3MwmRLdvrkao3V2zwiR3_rTL82BVwI2YbrpTahYWKRwvIb9DWZL-9kLfmoh0pLb9aHOtFUBOU_mcMkz63JxdMEUnuIZHFn2tmBfy98IfRM-cnK4ssvevZaEO26lIvOCO6DPPQ3k0_auR5W-w0hX6YySSd1UTIPbD5xJ7lgyZDVMQuVvm2XQ_w8MJTDyeg7b9WHZl4bLC_dy3qZcKTGr12OVfjXOzUSgQZNuA1MHzvZcrSGvBXZ4B-na72is1KqE6eumbiju39b5H26AwgWlP-ZNGg12GmJnIaw0m6hB8Db2qI1rN0EK8ciXRgLYEhLYjVYFXo8lHJ1q4zRyS9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
- لینک سایت در مرحله اول  - لینک سایت در مرحله دوم  #GPT5 #AI #API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/6335" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WU2U3emsIh3SFAwkkiSZoNLZ8i0PJR8UnDajmpPQCH6Ce-n71_OJrHLFU11QenRASWF61Mw5JnNonpFK-BCHulbHYBrpIqT2_3n7ck8T__1TgtGXn16c971Rx40wxcTxUz7TGt144Oyh10aaofrvvfvHHONkboFz_xbKnL7jHW1NkVhJpbEZQGcLZLCO4jmFfMeN4u0CpUwBKkcGoA2gI6oKK7iuhkqJVJE85mrE5am4fDIe3bAoqZ9desBtEzQcgmI6cXyhlr9yvTcVpr-s8bjthLSSgin6XSVNiwSy4VwoLnDVVb-VYcmr6KIz-k7a5xeuirkNXLUumj2WeV5XKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArhytzObDtPFWR5yrLvQICa-K9gVl_lCMgdq1FTjwJV6ARCVu1A67HdFsgiJo18Jl6XstbxPgIUUJBhokQetOdoO0mU-MllmhNOsUfKUZQvMSJesy8ZfB9ek5DXZmkasy3lTnk8cynbSU_34LPtS5H8EoO43fKKJJ8QGWQsiefjnvtdNiB2rt_OXETDRDyxoXPNzWYvqAAI5JsjcVZuX93xNJ_45Rq-yUcbjmaSUd22MwmFMxzw1NQIb5H1DNwQJDQcK0CrLIixi1V_2NQPCPsVcQBXsMRHvAaNUgmnDNRNyXB5XO36sR8bF8K7ISB_DFFZ6FcyiuL-ll26UIGycwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6333" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSXK-kE8h1Q31T3JtXcQS2lOO2U_HXPHcnEetjhbbe8AGlyOgyJdScvxH1gK5qfA1GQI9JaQ7b_TUcirVTMwxHLcXNUZiS_QWHuhHiYV79qz3VWaSIj7hZpDQN5k0FxGhiufyCOvd6Ka2NVJV4yszAMc60oHZKIMSsHYComaaeQCNpzjfDcA8k6PQkYAy_gstWeM6yPHUtCXoSuIL6py9NtgyLcAk_9KBuSwU-YasV22WEB9mGLk6mRSZl6yhyyNiaOsxhemsR9u9IiTPtnl_RyJv9pfn869wUbONaMxVz40LWiZZD3gsWKP7RLM0jcHjqIinbpNNLJFS_wjPYYGuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4befQEiDH2YU3oFebkc3Gt1nWcOQfqML-wkwJn59OHvvrSyfqL18-MI3WAdXNoX4yLpS1bsFiHNW81WnCYQCT9FP08nz9GTWN9gUNDUQFanv1aJPwv6vHxcnmEaWhpJrViSVdAAWgXG07DzAjXtRPH97kK7Esyi8lOhGmFD-0TC-6RHec0z6uhU7YlbefYeekGoHtcYjRD0poFAHZ7GKtTN0XzfKi8qw6AlOSbnJ8H1O3bJlYrY_5yC7-858XmW1fxda4TUOjHFva1WK7V5IJRD0SDpoKsqLSZV7u83eMIHDm2xJUxOhSde5UUWA5Qdj-JVRck2HmEZcqNgXfncfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6331" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=qgB_h8I3ISDj7rBi2CZm8uaUV-cVYt8Jg4Lf8d-3wiOaa7t_urb792gMe9g6X36FEBJCJrAhB_awmzpjVRKKKEWonFL3gAqhjWiyXkdytIMBm5zkaSh9LNeq4ybLMyY8mWnJOEA1zLrkH05jw9M8EfJiRzLpzRBX8DFQJP1QKpQBE9bJZduuRRJJ0QMPt_uqmth9uMexBPFjhiPmZWF2NDd9v-7Vt1tFxheu9UCgYGONOsSHVIDzrVJp176HbmvxxxDxewB5HwOMStHWBZdS-M4qQdRMP1DOW9fVH9f7-UMH6TXNSIIcbvoLRmg86Y4_3sniPd9oOJFwKgeY41_QJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=qgB_h8I3ISDj7rBi2CZm8uaUV-cVYt8Jg4Lf8d-3wiOaa7t_urb792gMe9g6X36FEBJCJrAhB_awmzpjVRKKKEWonFL3gAqhjWiyXkdytIMBm5zkaSh9LNeq4ybLMyY8mWnJOEA1zLrkH05jw9M8EfJiRzLpzRBX8DFQJP1QKpQBE9bJZduuRRJJ0QMPt_uqmth9uMexBPFjhiPmZWF2NDd9v-7Vt1tFxheu9UCgYGONOsSHVIDzrVJp176HbmvxxxDxewB5HwOMStHWBZdS-M4qQdRMP1DOW9fVH9f7-UMH6TXNSIIcbvoLRmg86Y4_3sniPd9oOJFwKgeY41_QJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6330" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATNA1iX65IpwUwUdevcPArxbhkxlgjNODxakiEE-zlGJQsva-OOWUfFOMolF5SdiqAnnGb1cC-d8ZzJQj5NCeSnKxz_SvhCbz4Z5Azez85puw1-kNYAFKwxfUG-aLyu30Hm6hnn7hzyOSBZSUs64fN0A6zdMAdBMH0zull_4k-EJD3lNkYnKEc4urs7JAg8dqaUoMYUDuDLZtcPDvCSzZol4h9RdHbxwPdcWz5t-T6iQcw8DhUAP-Ux28O9HrvYs52j0AlmJT19b_ebg1e3fdQ_HMyhfCRiTpGfSB3hwY7f5LFjE8i7sZP3e0RrBxeqi7yOtJH3fWIju3L2HHkd0uA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6328" target="_blank">📅 21:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6327" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6326" target="_blank">📅 18:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tk5XuNhXjl6qeTZiVi5iTD-mNOqMkTvfRXVtuCo3T51Yf0FPPDxxoaJ_sCt94LdLSb3lp_XHI8z09TC_k59E3eCLnH6pGSMn6_3oK6vZstOm49nDBW-8ghtDyhpYsJsiYI7Fkr8Tg-M8_o1Bjt2hx2V-enZXZx0y-3GaIVZkYm9qGrg6RU3RtnK2ZCFrs5nMqPw4ErLDdJD5XwgtDq91BcQczkJD32H6fkGtcJq5qeF4r6-1Rs1Pl8KJO_GRUPX22V4Jj-n9F2KhN7KWKrwCB9f9BSRooGxoGMa5RikTmRENKIUcYMU7onGlmDGAHJBSmsPDsxK_MC9Cr3qgP08qaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6325" target="_blank">📅 17:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQENcZPg5YcI96073mrKeH5uuEBjuNqn4qbCzyIkz-B_4dQ8P8hG9bnXnbS1zGW407PB7s0WWU7fmJCoNIE-tzOKsR5yXe0q8JpJKY1jbyGsJuaqTKtQ3eE_uOPbzaLLAdnovoWPPs4Q66ZmAYja0Tc7Z0PzJnYlr36ymrTwqpL9hToj-luEEBL4L2hyhmEmMwylsyRidW9pgH_67zW42U4CpW7aXn_yG_8is7KxsNsVgyv-_UDW3EcrkfXV7ueOKPCejX1GkSFq1RB-aTNqtscI696sxPxIbDflsxBSDO4z3LXw1EiTgDQFj9g96iaR_gRMh51iOO6AbU587pFQ9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6324" target="_blank">📅 16:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJQJju0LQa0R4R2AAXEMTp64tFvql3m__xNWhbAgfADHDYCA27RJlBP_45PHaUH2Gn-iPVGqPpKBqYOO5UUqd1v6vexSYTJ4uOKoDuD6dX0aaF6rFr4tVSMBZjNZn2fy7SmzInp5Lz8BNYBGUtxjb8JqWozFCbyohmUai6bJlpkVwGV-L8zrMsaZmU2KdOVlf9oufFL0jQk835aRw0scisml-LUYxJedYBOq2mjxNQ8_VOXOjPkbmYcw9aVAw9U76Q1dJmkoG3qxcjtLBnDMtGdTTp1WI37fe5_XYKVR89QniqNESiWOoAIK50xjwrrnciH3UN5r0-SoKnAgVrjF0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6323" target="_blank">📅 16:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=lzyT517pqg9vr8kJcYZG9e8WB2CTr2Dx-v1ir798afHRIQk1ytelwMd3_EZOe7swNAsKvZZTM1nW53O-faDy9skmywL-wHqaFQgfyMXd7n4DFbdp-GsIKzuhmbrQU6AHgJLiDBBumHnV5ld2XYqX4maVwAFjDul_n6Ml21Z0XCEzyeyNB3y7r2DoRbsHt0XhZRkOtRWNdrHSGoIX_JTY8TFKY_s-Wdr5UVtgHFd5xwpUy8Zw9VCxMXVkppN34ngsHQNyia1FHfXgb073XPuM8IyUn6zCislYYSq34gnVy82czerLUk3cA6htX83ZTcICYwLZ6FMTmWlAOG81hqqRGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=lzyT517pqg9vr8kJcYZG9e8WB2CTr2Dx-v1ir798afHRIQk1ytelwMd3_EZOe7swNAsKvZZTM1nW53O-faDy9skmywL-wHqaFQgfyMXd7n4DFbdp-GsIKzuhmbrQU6AHgJLiDBBumHnV5ld2XYqX4maVwAFjDul_n6Ml21Z0XCEzyeyNB3y7r2DoRbsHt0XhZRkOtRWNdrHSGoIX_JTY8TFKY_s-Wdr5UVtgHFd5xwpUy8Zw9VCxMXVkppN34ngsHQNyia1FHfXgb073XPuM8IyUn6zCislYYSq34gnVy82czerLUk3cA6htX83ZTcICYwLZ6FMTmWlAOG81hqqRGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6322" target="_blank">📅 15:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5NLFC8wRSjS3yU2FLJwIsqEgvoBHbXyFU7LEjfy_4lQRngPzfgE0GolxBdnUV5ufd5zriw8Jo0eqMBlJlMQO2NCpYenrdvcZ0t5clST1HE34HVX6yN4QJHyvJXizVIrAVYsBLKhLoQbr8uqQfGZj9siwtp6i2fdK0LyPUT75RrH_pkyoa1c2owvqXlMr5WjYrEVa8XvL4BpNzs2NG2YUtgvRourJT57vRrkpL9NawJRZJ84evQzIOW_tIQoUgb-7_e_TwC5OLRB3WD0P6Da7ZUEpew_B1R1rhWcXEPpKn6XnPZAfpUl8kMookd8FebLRNchQMiTR99pmuaEzk3a_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت موزیک رایگان
🎧
https://www.musiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6321" target="_blank">📅 14:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jwVsb8jydoaOuy-ffPlR4NEi7WNDeYe6SjjMIE74m8x_zPolZvRf1bqoBS-P2PeRGFjcDxByg_-cbODyXPoAIOPPPO3sSBCAN95nuw5pi3uW7d3QEHn9BmetmVlWHxMS1ZG2h47ei3YzIHoKdJkR2kCSil2bcYve9hcy9MPxuW9O4wCH_kVs5UiLbQrB5ZWKnYEcJCwS4Zoe6L5XdKffzECW7e7p3kPTeO0Xuq30rhA4dGLFTKwMBWWcjc7uAv4e4AqZVYdXqnqcBaRIRMjsr1uKdxK19Bdpi_wtqrX9JwNd4MBIdkPsZ7Y61ZqNiDHFEjzBhYwMdZNjlA6OrwJvPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rpPipFRyfCMBZplYQo-hmC4eAIeWz6hH3f0l7h_CI9qeatJMWvUxZynLQfneqrtBrJnXNmAeCfInyNi27-JCKlyByn6XiL6Nq539saW6qpPH3VvlcLDlac0CtRFLmQWe6KqF9l6WtOWDyRBXCFC0KHJhtWDzzxaLI4AgA2H3jEaS4hm3lrP1I474RQME3iZpb0Qyt1DArMTV9dtKPntUYgFoy1BU0TzdkJXJyA4dc11M-MfL8TpFrhSWpJU5jKxVGs2L_5jlTee3nwmX04yN4WaSTVSWQzWK7dzmgC0uyVNNra5KDygAvHMTZI6D49IA_fYoPX32aVQ6LmERven5cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6319" target="_blank">📅 13:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6318" target="_blank">📅 13:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6317" target="_blank">📅 12:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPcVnSlJ9TfqXIbW-YWIwmaJFLHeIiuihMo1TCAS7r7xQGSR4huyoh_IYg4uh2gHn5RX8XWwnenb8ug_0BK1pnpZNbCbVWY33f9te_CLHXRxGesnUfwZL_7RvCwNAf5zkkaP3IP4b23lr6oIyH0N-eZEh7xqESCp40jS0S9gUjZYMPsmFT-DzutCNKgt33VDVlYtgKv8tnAcPbfIotIWnTFIvqC2dlwjnmpIyVQT0ACZV69-rH6yGC5dh3r9Ili8nsW96TxquhO7dpF-E4hQ6qMGpp3wI53N1o6RaYT0NaR2c8N_tiCoQsUsWtClPZrv0sJQk0uaONukijy4dNUvWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6316" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JdNiucf28jOet-1cvz7L-B7iLt64BihMjH72QgcDVEzc7FQwS4Ri3uGFoE-JWrmrsSMvd2ia7wAYhQPDzgoQnPogTX89D-vkv3KOV4XIMM_qjO_PnSqwkkMUqHaGr8IfvB7-8CQoYbdxkAC7ofUr4SgIyQOXVcyK9lbQb6fqwS8RftjynF-plAMd9u0BLecuKCrOMjPwHqDjMV_GXKy4A1gDC84QYVj2wuDYGWpmAo4EqjAO77C0KjALK5l4cF52DdrQvqiYcR7-EkuQae2ohHTUgn9N7WJ4HyAOiMLDAO35liX6zuS82yJfur0tNbFKVondBJLIEGfJeMsT9tY1hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1G_Q_Z1irFO3frNQ-y481_wFiGZ2l2dM5gCwycIt_V6FZuxt97kw7wBbL-mF2aTePdaHV_UjGDNxY0qjDdpVhTtB4EJ_1p1RF1d073RB1_E9-zZLKOSOEMKoamxBNprsMiBECCyvbAxju7E1Ij6QSrjDDxqHMmJZMTY626txTzA__qhB8iP34cGzkNAdK9LsEZUP4ha0Zb6l52V6zGF9Wfb2R0C3Iy65Spml6UKgm9_NqiKyxqNJ5jXnf83Fj_id7AqvdWXNMDgGLyiAhzmkSfek-BpTFEWWY0i8_xMEoa7rM6HxAm7PfyyYc8vEv4FfRcfHyE3YJQhTSbjBlctJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=B_uMHjWAbtGWQ0NKEBJcEmEYmxnkZBcj2lAgQIdIyg7Sw43WgTgMuLnQvXyfIPUHGxCAb6-GiVKdXtUu3o3xvgGYmE84yzyPsO5JsfxvxP8JD_bCM0nTyRdHq2WQMWkdwplL_bCR2Mxyh6r-paRS4S3CKw2pNsXG8k9qzbndPgDFRn8esMKfg8_78scmEtprJ-HT7E_aB4RKEHsRtn79NEccROfCLXK-gHqgAY6f4RBPQEndecHFCnQzRLSeZHsQTxswoJgkZkN3q5TiFN9dBZTz46iaXR-IqMwy0-LNmDt4RWG4WwjBlRZfuS82RDKOUQyM1ZTexZN4IvGPdIxAmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=B_uMHjWAbtGWQ0NKEBJcEmEYmxnkZBcj2lAgQIdIyg7Sw43WgTgMuLnQvXyfIPUHGxCAb6-GiVKdXtUu3o3xvgGYmE84yzyPsO5JsfxvxP8JD_bCM0nTyRdHq2WQMWkdwplL_bCR2Mxyh6r-paRS4S3CKw2pNsXG8k9qzbndPgDFRn8esMKfg8_78scmEtprJ-HT7E_aB4RKEHsRtn79NEccROfCLXK-gHqgAY6f4RBPQEndecHFCnQzRLSeZHsQTxswoJgkZkN3q5TiFN9dBZTz46iaXR-IqMwy0-LNmDt4RWG4WwjBlRZfuS82RDKOUQyM1ZTexZN4IvGPdIxAmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6311" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxm4XnAECPAlJI6wLonffF7BvXmF8a7hs2-nwG1ACKHl2-uW6Ao6KGi173sAdUPWUNOVOlichmuQV77vXc1ufujbh6I8WFdLmQwuchlMMlRvj7pUMOF7nMAWtbfA_zQq7B97FCtcNtEawOECfp4AUkKZHfgc1KEMCf0SC_8fyJPwVxsDOcPPguHyc1fkGB4xAZbhZlvN2bCOz273KlLCZGvOqoO5rNHC9d7PW6CSBQimwBSzKHIxd-EJKEA93jOQGqHFNA5FacSd5t-8qX1FddpTqTcSi2QLmyZIm7AwhenAEWx0NG-Iy5MqGDxny3ImL6mrS0jdx0V7j1V1nznF7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6310" target="_blank">📅 11:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/6308" target="_blank">📅 02:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0XfNdpwKQu0i7FXrhFGlcu4m0leGnvUQO9uWV3flxDIW27v44PbExHqMLjXvPV8MUsLmVBfcsLRjSYi4uM3kKjRJDAOt2ARd63A-lV6PlMAWqe3qMv3U5Ly6ULtOdFO0o7UzfG1CxTk_cr5pykhcEjvBZ9nCKMxOvz-lXKnNBq2nd82n6r8nyGon_bvgnFhJj47nThpXKRyXzAhx0vG-JYPaEoAMV9vbbJtOsCGXR1Fhf1SyyT6hOBfIS5wVH6O_pQdbd2lKR3c0e3yQus437AD0p6TdxVAl84d8-YH67RsDnDpzTvr04gyqZ0XWVJpgasQXXrrETRw2tOiT_7KLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/6307" target="_blank">📅 01:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):  Aistudio.google.com  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6306" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مرحله یک طهلیل من به واقعیت پیوست
😝</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6305" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTkUbKvdpHqZlCKp1tD7JLFNsOG5XvsIDwgTXE3wL5V5de3cQMH-dRctMR0TwRgVViGu-Qf7xzlzms50L2VFE-G3mgiByre1QRCyT9l7QzS_ygjuN_ZK9_a0jdZbnpEDJ9FLKAVtQfRJPuozSYBu7teuE2lwGuOQmYo7tQtJg4pVbrPU0G6cu_LrLB63K5k6ItLX137Lt_7V2xM_i7nxb80CRjOe5rko7gfcIHr1g8vEvzG7e2s5jmzv4I9-3dm2mhe6dlXH9n-rKRdTAo5g8vLb1IhlHu5YvrDK3KymdVYOhCt36i_fd6Eh91XYn_ubm4KM3y97IhFPY7u0bSgW0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):
Aistudio.google.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6304" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6303" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6302" target="_blank">📅 22:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXEojCqtZk_R6_yk8pt52qlFTN1FlhZ8TI4VvHoqpKHJWflQTJcd7BubI64wW4L3G04G6vtL8SiSERPQCt7Gex9SFG4ie80o0q56M71esbKOEQZV7dLjaA9WCPpUFxia_HX5KHm_EDqmqPHfNmOLmuBzPGkJuJtlnIK8ByHgFJ40wAbkPEiDVbKhxURLgK4UcEUwdzpZjG82az3wxJo8PHNqrMTZawRqgc-H4ZUqLwddcWhEt1os6HnN_dESpYxZknzZ0UgyBOol3B1w6DqyyeSTXA8IJXZo8au1L2lDEWj3Y-gAmOcOl5FsSruPrXWrunnZgUioKafXA1Yjx2hFmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6299" target="_blank">📅 22:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran
* دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)
///
* حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)
* کافی است لینک subscription را وارد برنامه v2rayN/v2rayNG کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
* نکات استفاده رو حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/archivetell/6298" target="_blank">📅 20:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=WVFQC3DOoGho1gf68Ubnn-mQYzcTaQh7Lo3ktfDa8DULqrUzyKQXS7LXWeLKoUk-xXbt2fhtmZgC-oDD8W9EnIXsvXIYAi7nhcfiPGxGyf07NafClTws6yWzyYYT7phn1kYlLhAGWG6WbUEIFlZ7OcWLIl0KwZ3lvaIwvn_9zV7HLjjWI0CAC4tsT5V7gce-q7I7VBrcTK2VjWs3tDXFudFFAfNG_vb4XgIKUn7aDuPFUSkf1V_jpWW0pS0SAEECp3JNVgz7lcmlyRcZKPD63avFJyH3d6LX1tvcFKwDu2oTWRyMkjE5WGEPiO4xHlgYkkFOahAoba4xNN8pTWXiug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=WVFQC3DOoGho1gf68Ubnn-mQYzcTaQh7Lo3ktfDa8DULqrUzyKQXS7LXWeLKoUk-xXbt2fhtmZgC-oDD8W9EnIXsvXIYAi7nhcfiPGxGyf07NafClTws6yWzyYYT7phn1kYlLhAGWG6WbUEIFlZ7OcWLIl0KwZ3lvaIwvn_9zV7HLjjWI0CAC4tsT5V7gce-q7I7VBrcTK2VjWs3tDXFudFFAfNG_vb4XgIKUn7aDuPFUSkf1V_jpWW0pS0SAEECp3JNVgz7lcmlyRcZKPD63avFJyH3d6LX1tvcFKwDu2oTWRyMkjE5WGEPiO4xHlgYkkFOahAoba4xNN8pTWXiug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم ملی ۱۹۷۸ ایران، فقط یک تیم فوتبال نبود؛ نماد غرور، اتحاد و جسارت یک ملت بود نسلی که برای اولین‌بار نام ایران را در جام جهانی طنین‌انداز کرد و نشان داد که می‌توان در برابر بزرگان ایستاد.
از ملبورن تا آرژانتین، از صعود تاریخی تا تساوی مقابل اسکاتلند، این تیم برای همیشه در قلب تاریخ فوتبال ایران جاودانه شد
❤️
یادگاری از دورانی که فوتبال، فراتر از بازی بود، یک رؤیای ملی
✨
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6297" target="_blank">📅 20:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssT4-WD0b8DsTO4QEBPDjk9Xpwtj6iNwJSPPpYvKMe2j3aQB3dXUEicVy5ThswA_n2sz_yrXsesiiYnqg70mcVXM8PXi67WBXSnxey3c8Ob1qa-QCszUF_mZ92wozFVzOoOtE6ab50bOvRcLoTOCb76D6s5u6bnUk1SIMfIvFoeplCMuNgpuwH4CIXBizK1PAQpY-mc7G0F3Q_SD-KsPJTB7mQw7C_Juvi1sEo8HoS0pECCXNS_TjU2sV4IEq-vwtAbZtebuhUD2vYr35W64yNFDjg1Zh66iUAgJSLwMtsDPx52mN55HftWK_GJgjLUnaCWxExRWyDYsC1G2peRCng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6296" target="_blank">📅 19:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اگه میخواید به سرورتون وصل بشید ولی مشکل وی پی ان و این چیزا دارید و روی cmd و ترمینال و این چیزا وی پی ان سیستمتون کار نمیکنه میتونید از ssh آنلاین تو خود گوگل کروم استفاده کنید.
https://webssh.webhorizon.net/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6295" target="_blank">📅 19:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6293" target="_blank">📅 17:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A2ZGhOnbr5zZv1eaJfwV0VtDNSjmXavB1vkQ6tmOAde70eWjOh7ZbXB2i9WWpMRDl6xREgNKwETAMGVNs9n1j12654svxH80IAx58gwNJe-26RZDmYDZsHYcJdX9GfYi5RA1JOkAHNXhuDNshaP02llEcY6QEUqxZpAvidte0Y0sxOXWuBUAwHxRH1DHlqFac5v8Sto1mrbC8fSciix-thGTka5TeE4Kyrh6vY_GBWvXZmApZ9n4GBe9-ydCHBC4egDgvQZIaFO-8Er1A5bvDRruWLe6qO59NZU_l7NJNDNlQ_OuCSRiRUCXQjTWwNTeSGs5Z97ZhH23MsyYRl3WUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WALRh9xJ3W_7GXGKDEzRSKQH7rgQsH8qWIBguy4CB6oSsCXjosqC8aO-XuAHtA2m_i7B2a6APrODT-HtiK1PdKr3QaHz3CjXbVxCp_5x4LxpsMakq2Tr3xTXVPA3hZi0boxxrwDsrRtoK_g0kpdRGlOrAC_-h3L0IGfpd5cG9ASOWOHu6ISrm6IqrNV0hliMBkJufN9tueWME1Ku5Ur9eMKfSVQIyawCCziv0m0hlktU9cRkS7dGXRmxRdp9UD2Fv0QxMCSdlID-kXe2sLk6mxjWce77FdT2hfWKTrJcSrJkFGEqevzKcLqV0oiQC1q4FnsYxG8cEuwRgZNtA0bN7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N7X6aZBISPFZl6gmmqfdzh0cgz5tqlzmyQjF-MatQoweFZfhO4Mgip4cCgQrztenTTh9kGM5C-nhKb8u_87b3zgc6Nf3Q1STbuXfy68rDbXUX1eTElSZtuOvY0scbwwMaxtVVUHKXzZFJGbl10-SazqgO2jfk6w5PucJQ9blQ3gK2IIq6LriiLEAavXwiFVZOMeYbr1VPHIbJiXCnrx6I3uz3PTMV0gzBdho4vPU42wU6gOh_FjXTuTFUKl8KOiTHJRZRDbS-ysZbvvohvoTSxIDpBK7AKH7GI6Jkrh6HLQnftsUCzhMyR1W04JhaAbU0Wib5WZOXaaLZFjdwfzr-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6290" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54834411b8.mp4?token=oCbJCb9ERj0jrX6XEVkOakpU5SWJ1wq60BdLA2WhkMmIO2wIp0GrW94IioSvh9Gh9IljXSs8uADR8wltZk4Ang8YXUJjX0u7oj1GKoJaW8qDyN7HE75waR0hCqCLqA_Joe4ocUMLbHviv_dWzzOhg83PJX0n3Nw86OeNmWCWzqFgFBrrgh_dbGi2uQ5HMWQ4EzALf2NPbh3BuKBnwNH61op3tU0UTveEy5aZnJn8XwTna40l87dIM8cc0UJFfpO0clcFyH3gHGMYnnyWCoPl3LGkh_Be2gG43y8cW6nilKBKX0rj6LidTGqpoGn1SXf-Q76CzAlNQf4RRn6dLnX4OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54834411b8.mp4?token=oCbJCb9ERj0jrX6XEVkOakpU5SWJ1wq60BdLA2WhkMmIO2wIp0GrW94IioSvh9Gh9IljXSs8uADR8wltZk4Ang8YXUJjX0u7oj1GKoJaW8qDyN7HE75waR0hCqCLqA_Joe4ocUMLbHviv_dWzzOhg83PJX0n3Nw86OeNmWCWzqFgFBrrgh_dbGi2uQ5HMWQ4EzALf2NPbh3BuKBnwNH61op3tU0UTveEy5aZnJn8XwTna40l87dIM8cc0UJFfpO0clcFyH3gHGMYnnyWCoPl3LGkh_Be2gG43y8cW6nilKBKX0rj6LidTGqpoGn1SXf-Q76CzAlNQf4RRn6dLnX4OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6289" target="_blank">📅 16:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6288" target="_blank">📅 14:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6287" target="_blank">📅 12:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⚡️
سیم کارت رایگان همراه اول به خاطر جام جهانی (کد تخفیف + پست رایگان)
CUPSIM26
هر کد ملی تا ۳ تا میتونه بگیره (همه رو تو یک سبد بذارید)
لینک خرید
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6286" target="_blank">📅 11:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=ts8Rqsyy4cAQ4hVJtARswj-9_v8j4xZBST-xMLxOZNIacAhdKrC6lk_udlWT6GfqKyVW7Xf7V6YJDYWjdMBbvBY3bGvL-c4ZwpuPXat0BroZTIVB54FGhq4FxYTGezWq_x-wuQV97zam5_0adOBltObF_kgRdGh0P_kPXg2nwIyGkOt6BEKnz7v9aqVCgEEhIke99LozK8Db21HNK70Hc0dflqedataW2u5D1PGeB4gTNXhKLuEc1e3QI47lzFJ5DQ05XUNS_FUUyH4KDfcj7ehPudpyJ6_3z37Sxh4qsEKE_WVJXzGIsjW2zMU2viMD5Ya7m4k99dx6TP4LkaLwbg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=ts8Rqsyy4cAQ4hVJtARswj-9_v8j4xZBST-xMLxOZNIacAhdKrC6lk_udlWT6GfqKyVW7Xf7V6YJDYWjdMBbvBY3bGvL-c4ZwpuPXat0BroZTIVB54FGhq4FxYTGezWq_x-wuQV97zam5_0adOBltObF_kgRdGh0P_kPXg2nwIyGkOt6BEKnz7v9aqVCgEEhIke99LozK8Db21HNK70Hc0dflqedataW2u5D1PGeB4gTNXhKLuEc1e3QI47lzFJ5DQ05XUNS_FUUyH4KDfcj7ehPudpyJ6_3z37Sxh4qsEKE_WVJXzGIsjW2zMU2viMD5Ya7m4k99dx6TP4LkaLwbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6285" target="_blank">📅 11:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fW-x5ite0KJssKuB_FXPICNEzfRzjhDjCF40wJn-odpyognYTmCoyZTexj5aOYkYow7y3mfpNob9swx3m4X6ca-Iq8jANRKwPCZZvBeyN4kNWPEwQ9abj8zJd2rfWSyDHo5bxEvOlXjb8pg_03Qwe6d77K4TZ-swwevaXhcdjpBIU7CK39eURV1N7ZbuKJ30YMEohEJCw5OrugZE2H1tr-ColBUaSkZbg8Zl5LrVVPJVVzcNMw2JkOGCFx8m43ZEAT0go-BWgd2PBwvxAfD7OnKiviUSfs1ufKAJ4fkuK4X4E5IdJqj0qhpgLF55hno5FdFUm3K1WxkXdfCmpAZQyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6284" target="_blank">📅 10:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=YhKPKTHqOxMrYjERcAi4gI1dUGmhpUmzOF7hFfuW8GAT5qwL0TxDOefW8ou_c-sZXZhTedZFvwAmwcN9ft7eG_FgF96CKQBNlilTHqyng9v7PjD8cYqnRHmMDyIpWrffvBYObDJy5e9EQaMqJX9PC8o55GtOy-tvr3TjV4Cb7pquEIbgIbo6N6r47DA9PIoQqaVrunXosI3UPCylHiT0C1JYq_Mipmjew1WT9heEyJPKscfrOAz6CrIUiCV8HS1GONaD_Q_DsSLoQpzp5aIvD9VGvAXXqvrZbNGTPii_t9XgmsnA0mMApFNux0K9J6XD9j-QT7OUCy8uiNAdOMUL9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=YhKPKTHqOxMrYjERcAi4gI1dUGmhpUmzOF7hFfuW8GAT5qwL0TxDOefW8ou_c-sZXZhTedZFvwAmwcN9ft7eG_FgF96CKQBNlilTHqyng9v7PjD8cYqnRHmMDyIpWrffvBYObDJy5e9EQaMqJX9PC8o55GtOy-tvr3TjV4Cb7pquEIbgIbo6N6r47DA9PIoQqaVrunXosI3UPCylHiT0C1JYq_Mipmjew1WT9heEyJPKscfrOAz6CrIUiCV8HS1GONaD_Q_DsSLoQpzp5aIvD9VGvAXXqvrZbNGTPii_t9XgmsnA0mMApFNux0K9J6XD9j-QT7OUCy8uiNAdOMUL9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6283" target="_blank">📅 09:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRS8_goGkyr_Nn-P41feJ57NWenNV-EH-9b8lEn8xondvYJSQW1roL2DUtkq0ngMNMWx56M5qsmHrLC1mTTBR_hnyWrEsfqEJI84VSH0wrRGX1s2FgteOVBbkVYUzfLMzAuV6PxuuwCCfjapA9LeCQHkpIQMYaqTu2iMMPXiEaTgIlR_VVnbgXnfLEqiY33tpCftoV7otx9PSMSeGuTtE3i-aTsVoJjo-29j3A_-z6A06I5SycuedzoIQ3Gdrp0I4RpLYt83RptSdJTnm18V18ZwPMgnR4ztr7ceer_ajeuBibIHUXow6bfBAxBFsqcWm2ZkmjoymqUZWRZNK6bsLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6282" target="_blank">📅 08:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ozr9olfpbk-JQwiFZ47LG7zSX176SLaluvfmALtsR3_FkhEQJGHni5CgGydQR_77wA-as3-xFCewsOafWiGwv3oejo0Uh7H6gQTabzeZnGC-FNUvqN798kNcJ59gZjUBi54XrqL5_BJvnhT98yeN8UyTU2IzdUBFdbfiYucM9oajfeAJhboX6-YmBwYoXYp3wCW48ioVEDTmXxIAoiEiXJqW7FnStSVY8jrAndaZ59Iupx0KnvdOkJ5pVzoBvJmGLnPgFLkQ-CGtzxYM5QN_wT2fZ915GGBP0Pdj0o9WrWvgsF8S_SLaG9NEHM4S6kmcyVh0PH1wHJGhi6laGKriDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوتاه اما جالب
❕
به این صورت داخل duckduckgo میتونین qrcode بسازید
🔗
🎁
@Archivetell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6280" target="_blank">📅 03:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6279" target="_blank">📅 01:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚀
راه‌اندازی خودکار 3x-ui با WhiteDNS؛ از صفر تا تحویل کانفیگ در چند دقیقه  اگر حوصله نصب دستی 3x-ui، تنظیم کلادفلر، گرفتن SSL و ساخت کانفیگ‌های Reality و VLESS رو ندارید، WhiteDNS تقریباً همه این مراحل رو به‌صورت خودکار انجام می‌ده.
📋
پیش‌نیازها  قبل از…</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6278" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=nFECu9RpmhQFbiaz3gMRAfkoFa_jBsoKUuAkWcyMK2ti46Se8V30YwVMl1Z5zMnBXEloVLScr33bbIE45N_HGO0rK_TkKvXKeNaebxOGlHGnDKZP5gED6ScjSE9fZm8odw9_WT5JjDdAn2V2jC4CnikTf9ySpgeY2JI6B1YqrhMZaEUxyq7VWVPF9zrMUqUcITmSGFJrhZnbpWde0sczR4rmaYOMCHcn9lXSSjY-BBd4QHxgvb_ITovhsjDV4ha0ZxG2KGkx-k068Y9nkDjS2l-PEryjnJPb5Eu7Y4hyb37Gml-OUCOlf_qXcBQZ2t_RnSfY_BtNhhB0izX2NEh6kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=nFECu9RpmhQFbiaz3gMRAfkoFa_jBsoKUuAkWcyMK2ti46Se8V30YwVMl1Z5zMnBXEloVLScr33bbIE45N_HGO0rK_TkKvXKeNaebxOGlHGnDKZP5gED6ScjSE9fZm8odw9_WT5JjDdAn2V2jC4CnikTf9ySpgeY2JI6B1YqrhMZaEUxyq7VWVPF9zrMUqUcITmSGFJrhZnbpWde0sczR4rmaYOMCHcn9lXSSjY-BBd4QHxgvb_ITovhsjDV4ha0ZxG2KGkx-k068Y9nkDjS2l-PEryjnJPb5Eu7Y4hyb37Gml-OUCOlf_qXcBQZ2t_RnSfY_BtNhhB0izX2NEh6kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6277" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=GJs2lfOGKJO9GmxQgW8RXVMFEvciDUMQkQSBB9MbAo8E3UahFpMaAjf5vVPWwCKgh0Sl6rO2OPGvXv8fdkJKxGc7R0Y8hD6NFsmXrj_23K8eM8_rtaYIhj2AK2yaN_iS4BIvLwIUtDc6N4DdLvm17ycrKuAKopqWMVOAJhRwx2Ke8djNipc6xNculwvqRuxShzuVCKm9C1Q-HMYSKZWjEbU7gAKIWhWjMuLqhgvvhDvMQt-nMwqDJs01kPLQR7nW3DmywgFxU1F4TSejJnxRUqtMKLCbODOO8Yd6JQc0p72j23C1ts_kaMFGIWOhJ2iClUg8yvDTbDyiUBV1AUpDRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=GJs2lfOGKJO9GmxQgW8RXVMFEvciDUMQkQSBB9MbAo8E3UahFpMaAjf5vVPWwCKgh0Sl6rO2OPGvXv8fdkJKxGc7R0Y8hD6NFsmXrj_23K8eM8_rtaYIhj2AK2yaN_iS4BIvLwIUtDc6N4DdLvm17ycrKuAKopqWMVOAJhRwx2Ke8djNipc6xNculwvqRuxShzuVCKm9C1Q-HMYSKZWjEbU7gAKIWhWjMuLqhgvvhDvMQt-nMwqDJs01kPLQR7nW3DmywgFxU1F4TSejJnxRUqtMKLCbODOO8Yd6JQc0p72j23C1ts_kaMFGIWOhJ2iClUg8yvDTbDyiUBV1AUpDRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6276" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=hHSBRVlMckd_PHVGUlBDFm8j9iljRKTtjXWyCOaK9gZDlgtE5Nl-kzxkRyIIZhd1Rhmm47dpmaRoBSTYfcFVnZtgLujroQQo2rqoZWIef1IXzwjRfWxGwEDbNCg-rrDsJ1wVG51zFJ_TnZKFKAfu3TQaFpFCQ3mX5ZXHwpHTaOTKx_pnqELUURuDanUi9gk0TuKOZU2XcLNRZUesNtERRhHB6GKawaXzieJ1RFkze5vt0xoWh4QeqC4cz2IQjqAHbrpE5qDkXDJ462rFgeEr7K_-Bmk6xwITLTx79lvFGHEyuvya7RWEIhE8IF5xxIO6PjuBA5iMO8YV1dSiFOQHkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=hHSBRVlMckd_PHVGUlBDFm8j9iljRKTtjXWyCOaK9gZDlgtE5Nl-kzxkRyIIZhd1Rhmm47dpmaRoBSTYfcFVnZtgLujroQQo2rqoZWIef1IXzwjRfWxGwEDbNCg-rrDsJ1wVG51zFJ_TnZKFKAfu3TQaFpFCQ3mX5ZXHwpHTaOTKx_pnqELUURuDanUi9gk0TuKOZU2XcLNRZUesNtERRhHB6GKawaXzieJ1RFkze5vt0xoWh4QeqC4cz2IQjqAHbrpE5qDkXDJ462rFgeEr7K_-Bmk6xwITLTx79lvFGHEyuvya7RWEIhE8IF5xxIO6PjuBA5iMO8YV1dSiFOQHkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6275" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ادم خودشو باید برای هر سناریو اماده کنه و باید تو پیشگیری خوشبین باشه. چون شاید همون ی روش هم جواب داد</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6273" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">همین الاناس که ترامپ میاد میگه:
دقایقی قبل قرار بود دستور حمله رو صادر کنم، ولی آنها گفتند ما مذاکره میکنیم و من برای این حسن نیت آنها ۲ هفته حمله را به تعویق انداختم.
ممنون از توجه شما
دانلد جی ترامپ
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6272" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">برق قطع بشه با کبوتر میخوای پیام بزاری تو تلگرام؟ 🫪</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6271" target="_blank">📅 00:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6270" target="_blank">📅 00:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6269" target="_blank">📅 00:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6268" target="_blank">📅 00:30 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
