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
<img src="https://cdn4.telesco.pe/file/hxGTR6gecU4w7fW4D2v93s3rQ7zn-fNhTJqiDUJSXGZNoRFtSJ0MHK-UXQd00YZzDi5IWGK6kS3vvJGzbrwVsRxgYYrWn_ZuC3pc5AsGoKCRjfM0_SperiC3hQmRNQ88Aolv7tcJOWvcyboi4UXhrJP353bX-1aEYi6Ew5qHqS56l5B-25gPRpiy7uwEa_JEWNTTczzfdosOnSkgyGm0ZUNL1Sp74zLIF99ziKy-Zu07v_6Ep1fZGF1f00cIx7gGYxAcMSFR_HBoKvDzOwvfvMkMPhd-dzHL-aMs4HLIwsR0Kth1z65q4gdN7QP6pcENgNUUURXKEWUfYktIkadACQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.67K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 18:28:11</div>
<hr>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEN73MCNmvPRVl-ygIzmj6IV3YcxDEbNEZbmiwbO8KuLEQn50Hp5Wq7XGw4EET7OME6IYLrCHj81BTRH9oKvBawGfLSsa38az91MczFUWjrlZBfk1TPk3mNEIBLsDfWsQC9HJIeLe8CS0FIx-jYwpighfLGFfpN9ig-ne8GJN2ROfgue_VuqtZlSfSz3VEzFHiPM6LlWNnrkEczyQT7yvmmJS0HF9ioA_Ntx8HZF-94Ya9RGIhfd8Np24_4yzgU542901W9NexS1-JvPMQlG8gKoU8KCahyMQKUuFC89gQSKQI7I1gw_BwGtANL4Pw-lsdHQausLKFotitxcnom6PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با افزونه SkipBait میتونید ویدیوهای یوتیوب رو سریع خلاصه کنید و دقیق‌تر داخل محتوا بگردید
🎬
✨
قابلیت‌ها:
•
🔹
خلاصه‌سازی سریع ویدیوهای YouTube
•
⚡
جستجو داخل زیرنویس‌ها و متن ویدیو
•
🤖
پرسش‌وپاسخ با هوش مصنوعی درباره محتوای ویدیو
•
🌐
پشتیبانی از جستجوی وب برای اطلاعات تکمیلی
🔗
لینک
#AI
#ChromeExtension
#YouTube
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 382 · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
گزارش‌های تازه از پیش‌نویس توافق آمریکا و ایران
🇺🇸
طبق گزارش Reuters، پیش‌نویس یک تفاهم‌نامه موقت میان آمریکا و ایران روی چند محور اصلی می‌چرخد: توقف درگیری‌ها، بازگشایی تنگه هرمز، کاهش فشارهای نفتی و آزادسازی بخشی از دارایی‌های مسدودشده ایران. همچنین قرار است درباره پرونده هسته‌ای یک بازه ۶۰ روزه برای مذاکره باز شود.
📌
با این حال، Reuters تأکید کرده که این توافق هنوز نهایی نشده و بعضی جزئیات، از جمله رقم دارایی‌های آزادشده و شکل دقیق رفع تحریم‌ها، در گزارش‌های مختلف متفاوت آمده است.
⚠️
فعلاً باید این خبر را در حد پیش‌نویس و گزارش رسانه‌ای دید، نه توافق قطعی.
#Iran
#US
#MiddleEast
#Reuters
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
متوقف شد
❌
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agwH5BsE0PeBNu3gruyflH2GZxuiABMEfplKEX93ayxDMEWtDiB7Vmbsg29GMKa6JJR2hk0A_dS8fPMHU27IPlSoem85sjKmd9n9vorZjGNYnEXKldOnrHAurLkdZ8ZIlmO9kx--j61unmSSRPvPsaE5YdQc-ulvqfFYR7tgyUA2GOo4D8cbCRt8AYzwE-iLLhhoJ2MuQ18adSnKk2Tj6SmvHgGecTqilrZU7HKE31YbA5W7bg8Nw9Sdku4v323-7mmS1S_JIN8G1vQplJGlGuEaL0kcdbT_pP_nBZDvp5fAjhmgPyp5VtqNW3guF_XUkyPNA_Ct5R2vGx4Q68Z3Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTAiXf6WXLMXYYCNsGEvrNh575Tby50rYQDOj2Q1MSFzWxcEbOtA6yNHMRN_0Ijzw27oo5YOQnuFWIRAHj-aHxiZ6Gp5pmPcXZyOGw4DE4uKNFvQRQHQvzRSsEONhrhve8JysObVE_ahLlOkvp1UR7JCtQViF5yYizGfARRwp96ZhMzzZRPNmueqPv77msJxIlufr4UMohUObQaaM2wOhVSfHcHWPgqHeRhOEYMlAoum-1vqe-pSO2235llfoTnpGi8eTx8mjdBmL7r-pKqaylDsWW6L6hEuv5ufLUBuqlD5KOuWwsi2gteAju4whpMRZyxMIzdqAYSGKz-fmq33Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIy2B-rSXv7dRi26qwrVPrB6F6CQ50RG_o5z2e4h_KeWqREaDOkClUY9eUDTLBQ3TfYVSFsC7RhpHwJHeys0RF4rVtuSTpl6K6j_v-ihQTtYVRpsDvx0CZ3dMNk0d646OddWWEtuVI3oxaNNzWoQ6JRjeWWY4f7ADgS0LvU6XfD9MjL4NknSjiqaWTgDVLhl7f08W2qbGVCHMJ_-GWMkoqLkqnNgxQAFWKaq3nLDFVGvH-GkGmGPujZkNjkwhfjzqJPuvJQo1Kxr-5KUWVUvqMabb7WshNrrG4yjLigBbIlDg4hYUlwMxi_6mBS-JIGM7FAudmrFbS-DnErAfEPePw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-VTJDwdFZnZRAJpPIuKRheCbK8u7oTrenf0hDJT9vDedTWg8s6bXBACsRCnZbo98LuR6GEsxZl55HQ2nWjoRlUPAEh0fKHtN7pZarbwRignxgMmuelgZaqPF4C9aaw6Qk32Eru8sW3as_I2eE8d01M5NTu8eHO3oSChjm1YKmhAV1I6agZz8okIPt2FkAYnSKKjyPPNe9tjIABpdnNeiL7d42FueZxQTOOuNxSbUjMwO38eqrN5iq8uO3IpB9eYBEQwkw40eh-UJwR_ojLg64mHmU7NVOpMMyScJMJYd3rvlFwqcEVPloI6IRM-c3Nliz8a3O-FCyTxdzbV_lswrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jloqZORkXpb47xAi2cxsm9TrIplHq8vxeQLLSr8hnIpvRzlXJjvVeIHskI0uErmlRU5fokK_bGq-OVxNTNSVExspCZOfyTtecxMYpViEFyfjOKarV-Z9LdRCYGP__jZ8OJ8T_m46Jzxp16BQVhIunB8vKzRfxzpoOK6JXo9JEmwuu6jVPaLLzPvDRJy14XZtvCddN8f7jMweGQjskaw5NuO7n6NJpvzSx85oS7aCyDx_NTVh6BWSSdynmg3Pa0mDOCc_lj0gzF839cUEjXreKtR-6qO0Xfgnun9og3pdz1vehvFaJ5Cm-3qneEiKfYECSJfq8X4yDpgexQWKuyp1hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHxEO0rwl_d2EVOB_W9vWQPb5nMDMuPPygVH3LtqM0kot-hOXPRh9TpGc73JB8a0R3wT6APLIFeGXnJ4QgJmh_cgSFKMnh0GKI8Na7DYPVQIJTT91jbxaq0vhdfiVLJQwqGbTWWA6D96FMheLrWVO6nAfp3bJM3G3Ay0msEefhzRted-EHs0E2A8aXLCVFQ_Pg7dqucXleeOH-tqhU_nXg6eSBQ49_LrQDaYueyUmwJ_Y2H6V8ZjcAgtS1sek5xF_HuUsR9uJriB1pdyn-zU_P4nR8gC1ttS-ZRcmsK9tQdYZWl68e3E0RZmlbT4-D4rkm_-uaCXnkgns0pVK80_9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKRoIFXzUvPPxM0UzodpVx7qp9Cy_cM7yas-1OAXCH6pIxAqKqB6M0r7eP2OT5YflD8mtfq3Y5hmhlKRn8jMT8q7enhWXLCl03qPkBsDb1MzI45IdQCNZ-iLRXnFIwryzNM9Eu2b_Dn2NwwVRHIHOJiO9zIiabSHxVv_U0GlBjduiumtVD-MhhWnlMudPpJyLyA6JKJA3CcFgA5869Xw-iayl-oYxZGzxJAz8yAmeHbIlDCJbFwSrIxemr8l0T-kUlyH4nNIORgn-D8Ii-i7Gt03uz_6WYlgaQbdUiCIYXby8vKk9fCePUQsG8Idaozn6JDHQZOT_KaBPhEVhvn9ZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=pwuKsWqMorCnW9e1gI8xWayZ3kHKo2hqXEagsKHpgHYOmhgtXUshE2HgB1M4v7n1UmKPjSVpJj8JMcw8x--oi10UYyCYaedcUnSDLHamqSIi8okIjLFXEO9CdbqjenqTGDZzNpzDn85Pj_NZF6RhbguovgVukYXkLuOLSfuqVbyOzI4BBD8ub_ppu_L7VbEF7TCDgYwVn45aR2-h7WcPvDAnWv9H_z_NTeWkM98WNZBbU_oaXHx4a8U2lz6c1oBcuuBBWZQHWMeam_M3et3LSbkRiXTN-YzcwiVPAm9sQtbdrKULyZX9BIj-IbPTe4qBiPyDJ2yJkR8Ns9pPuc5fDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=pwuKsWqMorCnW9e1gI8xWayZ3kHKo2hqXEagsKHpgHYOmhgtXUshE2HgB1M4v7n1UmKPjSVpJj8JMcw8x--oi10UYyCYaedcUnSDLHamqSIi8okIjLFXEO9CdbqjenqTGDZzNpzDn85Pj_NZF6RhbguovgVukYXkLuOLSfuqVbyOzI4BBD8ub_ppu_L7VbEF7TCDgYwVn45aR2-h7WcPvDAnWv9H_z_NTeWkM98WNZBbU_oaXHx4a8U2lz6c1oBcuuBBWZQHWMeam_M3et3LSbkRiXTN-YzcwiVPAm9sQtbdrKULyZX9BIj-IbPTe4qBiPyDJ2yJkR8Ns9pPuc5fDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exlRVjH6GfFCRgCZInk2vtq3KzCT0w1CwPzJPgylsV1kr7n0UuZKEB6F4jcLDmJf4zojRv5N-ipLguBDbLXEjzMzEujDgNQkdSM6k3CddVeiMOk8QTqivpVfWol-V3CHQaehA_YCr4_LWtAJo_UjipTtsPMZWQk-W0-h-eIZ4g2_LtU9WfGLupeIfGfn9NcNwKn8knOhPNgNEJ7tS2MOMSk80d8W1mm0OM6qbraVkSYhyg2nonYD17cHdHggPvF-8aIFEhZ09ukKjGIvUFNo6J1Z42RsvOS6ObKPDwisqX5S5-CckCWRrvchoW630MMElpAkkLy4la5UBnT4A45lwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2OIFVrskO2dCJZntqiZp3DBNR18neklK11YYU9Kl_MZezT1Pcvrnp488KlxB-2i4xM2noYdlzDi3bk1SdNNfEIcXlxXStD1CZeOHxur0nvx-u2KZem3sBia88itw9QJPo5uWYZEcziiFC_6YAIDemhsjaA4X1b0M-F0zmbdLl5v9Hl7zZTEEvPKyXYnlsF5F5VnKN206JAApV5ov-pXcAQGVwnVu8AfWGoy8z9PJkQfy9-rS59KFdKJ7qpRl-Dq7OxNo49agu-BVKJsPXfyAgfI3oUfMgbkLWL8RHSxSOJQyiIGlc32OcbLkCQ920-LrpoKv_tR1PitI_6ZQnfP1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=covDZeq_NvrQwXdU2R9l8sZqlE4hpTwYXo_sNaIwAZoOw_98Jg6o3pBqa0xYBrAXTN-LuU1xuIdm3GBTFw53LAHtY8lEfJu2hWDlV5r_fmULKsbGcjTZkJHQR6w0-0gQZaWL5N8X7E0nWRwkBqYy0rSO10Nok8oLAHEjzvwIeM8vBEhJ7YCvs1AQF8ycARfaxjKWRmGJ1xRETu647Zpin5fo7_aU9tAKqk6QMglIt1K1eGxkEIy40rFIzWI6Fz9hURf4nkU1mwm_OCbTjyTcB1w7MsEfBNnIHYioVRqMkUZt4IIDiyKf3LAfJ1n5H2___Jvi6ordqZs9OYIXS5_sNUwuwhT1q63fcsJR21cIJBRI13gX7NGEQWFNf3ox0M2c47axPK70V8Lj-5-PP1terlCxhkmNszMHWGo3qMbXKGH95Kuk_knKXPKIbOwqe6CO7RjbMiLGcsRnyD2bEpmrmvaY2rKxso-EfleKvgJ3C6qXTxxc_39f-G73X6z6KZvCjp3nvcTcDIlcdchKQTTU7qo1EpLsAIKxn0Ck-mkGyY6p6O1KinTsebODS_QXXU_ql-GgULXxq2qM2KRkOVK4792YHhhi1UMEx0SwxW15AI4Xhwj-zWmfRk8Ei77CXDnxrHd-MfCJ0wd3JKprJOopxuAyo-ei-XXVoVGi5hUrDtk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=covDZeq_NvrQwXdU2R9l8sZqlE4hpTwYXo_sNaIwAZoOw_98Jg6o3pBqa0xYBrAXTN-LuU1xuIdm3GBTFw53LAHtY8lEfJu2hWDlV5r_fmULKsbGcjTZkJHQR6w0-0gQZaWL5N8X7E0nWRwkBqYy0rSO10Nok8oLAHEjzvwIeM8vBEhJ7YCvs1AQF8ycARfaxjKWRmGJ1xRETu647Zpin5fo7_aU9tAKqk6QMglIt1K1eGxkEIy40rFIzWI6Fz9hURf4nkU1mwm_OCbTjyTcB1w7MsEfBNnIHYioVRqMkUZt4IIDiyKf3LAfJ1n5H2___Jvi6ordqZs9OYIXS5_sNUwuwhT1q63fcsJR21cIJBRI13gX7NGEQWFNf3ox0M2c47axPK70V8Lj-5-PP1terlCxhkmNszMHWGo3qMbXKGH95Kuk_knKXPKIbOwqe6CO7RjbMiLGcsRnyD2bEpmrmvaY2rKxso-EfleKvgJ3C6qXTxxc_39f-G73X6z6KZvCjp3nvcTcDIlcdchKQTTU7qo1EpLsAIKxn0Ck-mkGyY6p6O1KinTsebODS_QXXU_ql-GgULXxq2qM2KRkOVK4792YHhhi1UMEx0SwxW15AI4Xhwj-zWmfRk8Ei77CXDnxrHd-MfCJ0wd3JKprJOopxuAyo-ei-XXVoVGi5hUrDtk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=Rre3_HlR7DGtHTaCgNP5MtOJgsil36gzcxa87OVvRNGu1YhJ-dgaYI3JLWD_y0qJpGjITZaJkXf4luuSniNRHVDI-6Sb1JgID-acu_8AKiBmRQVM4awzj0RxeMfUPAloxK8l1cPmvbWbK4T3vPfvgia8N23LPvnfO9O_YJQTDuhtITFK5i6KYWIQPPzA0_yke6rnaiKiUZJ3QYFw10KLL09UG0fzVVgICLFrMV2q1PJM9F6lHIKICidvPnHNiC0NguDKRq5ttnlekdgtvOw5OgW6yLI3_SMuI9J3e7vo45A85A2XBwEWK1khy-rjaCwPfJOXZZvlB7T7SalQKVOwGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=Rre3_HlR7DGtHTaCgNP5MtOJgsil36gzcxa87OVvRNGu1YhJ-dgaYI3JLWD_y0qJpGjITZaJkXf4luuSniNRHVDI-6Sb1JgID-acu_8AKiBmRQVM4awzj0RxeMfUPAloxK8l1cPmvbWbK4T3vPfvgia8N23LPvnfO9O_YJQTDuhtITFK5i6KYWIQPPzA0_yke6rnaiKiUZJ3QYFw10KLL09UG0fzVVgICLFrMV2q1PJM9F6lHIKICidvPnHNiC0NguDKRq5ttnlekdgtvOw5OgW6yLI3_SMuI9J3e7vo45A85A2XBwEWK1khy-rjaCwPfJOXZZvlB7T7SalQKVOwGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/6348" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSm7bTA4Bn79OXzl_suy9G1atRNAzHkPpEYsGlUBbGjyAtZgJ8WqE3uLkKnheAHVuAwer4Rdtbx1G_ngZLIzTT0cNHqQtiUEHdyWAhmYSij85G_x2Vj4bQKsqdS4V9OlhN5GhDwpTETs17SA_0fV3Hm97vIdoj19223Rjl1puOx5A3uzg-nsLFNmZSK_wGFqOu3mxAhM6GV9UwyKTr708Eu_JIPkk0ZF9vrppTXGGHxLyr947QBXKhFJGXZf66EShb76PH48_4_fYMgiUDLsDCrWcbRplia6m32yB3nWRfLVWDt6DY1M0JtfIgHynU0jeBMfv8kQq2C4fC6F2USNig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکن ای پی کلودفلر 2
نتایج این اسکنر معتبر نیست یعنی ممکنه پیدا کنه بزارید تو کانفیگ بازم کار نکنه
بدون vpn وارد این سایت بشین اگه باز نمیشه واستون از یه
اسکنر دیگه
استفاده کنید
https://cdn-scanner-pro.vercel.app/
لیست رنج کلودفلر که پایین میدم اد کنید و اسکن کنید.
هر کدوم که سبز شد بزارید تو کانفیگای کلودفلر
با پورت 443 تست کنید</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/archivetell/6347" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a47z8EsvRRA-MvJEa_3YdQOXN3_nKLKlTTGDAP4jAn-kWRzrL0YYcYNN9QCKYqgdeTd2sKTdRtvsKb_9pCDY_GM0gFGoq0fc2uND1nda9OXJqOg8q8o6YpuX2RsxzIMo18YgJiimOJt3Qc_27nSQqLAgShnS66u4wHfOKkmdd48X6kDrid481rkwOrKRbopU5ynERhE7FtL1OT5cD6V-yfOQ_oo645Kr-Okr7wBnMS5ylLG-rK-8LWCyqJYIh86MdwmSlTu_zpP8NZ3rHaBvc-ePmot20GiB9Oa4GeNt0AKdD4Y4L1KhHa4WhDd15wL_xH7qlIdWaUZs8hNLKpM1fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YwoCItQtaakCb3OqgBeOJtjXpmmgahapxfIgGdVfXAbVVhHxSfrF0vgaB_9CJSLeFIEj-s6ygIkTwNR9cEb3_oqnPVSbGp3elMae-uZW_hiRpywoscvT5MxKqqYkgmOiqNeYWYmF_E_uRahF3JWcr-JI3XoOYrx_LUZuFZ3EaKInZwvzX42Teu6cUBruzlqOo2n5TqdHzkdOy3GaBWJmvGGna25uQrCBP8JNPs9RdcHZClq02zGh7nAJ1BtRecYxi95lSHSU_BSjgSrar2hAN2gkF-iW0-57HfgMkoY-2MQlSyUWYmMfLAV5w6jcEG1RrPeMqUpkYAxO2sPKvhRqNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T5rcaqiDZlAoROgepQDsKUABKd8kDda-pskLu7-eQWR_eBV7RIkgvfhwP8-UDnWQ_AI7C7C-G3HJMXSV_vDCzuskP9VpBy4v3bU5UeRB4BmAgu52CX9Dt2O0-wjvJ3U5zVF5HIf4dL9qytsVt4A_FB6pvZrD_VS8TAsD4riSLZU0OxTSlfdB3z7EAwH3bU1DO-ZaxF1XX3w-WyEuqPoTHEFeteYrRVrDkykWc16z2FTFzVWjeXgSYaJ801oipYjABT9ph_cULlPIqDsMzng5ZrNdUpcuL4rE3v78uvPQAiYwxIuNwWB6_C_wAqo1HClXrU9k8UiAhbRqPlwjy1evrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CbprQ_eYyDC3l4K1r_0BQZ6E15S4aQ2Lcj8HBwGJUOXNJGsfTdcfhLe1Hu_738oJ-ZJ683nWFBRLHer_dmwUnXP_w0dSoFTSnht9Dqca7PxaML_WEByYxqTtAeTP0b0Q7PuHJqXfisIEUdwyZgYS7xfTQOXlxVMIx2OpMiu1yM98C5BIsyVEFtcgXCvhglRWs02P7sgB4NPT12i179R4JEcYhs6ozPPntNROMr9dZlaX7iqEnlG7_2rCKoA4Obszntqmzn6fiDZq76ToxQL9egoUCyjeR_Pa-sgP_cv8mLlECK0DkWo5W45a8OcMERi2KGCxu5VzVfpeNxFBC0scgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">7. به صفحه اصلی ورکری که ساختید برگردید و بزنید روی پیجی که ساختین تا باز بشه
این صفحه nginx که اومد یعنی اوکیه اگه ارور 1101 گرفتین یعنی اکانتتون بن شده باید یه اکانت جدید کلودفلیر بسازید
به اخر نوار ادرس یه admin اضافه کنید تا پنل باز بشه و پسورد رو وارد کنید و لینک سابی که میده رو کپی کنید و داخل ویتوری وارد کنید.
کانفیگایی که میده اگه پینگ نداد نیاز به ای پی تمیز کلود فلیر دارید.
مثلا این رو با پورت 443 وارد یکی از کانفیگا بکنید تا وصل بشه
188.114.97.6</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/archivetell/6343" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npvzxzGG4JqPzf3zNgdyNifyh8Uqaeh4nOMrPUnyJ6glWul4OStfGzCdFoF3HiJ7ggzT9d3NzagKjM4niG3R0V2Yyb3q53rTmDv0dTnj_GDTEYCzp7NRoTnDZZRA0LC-_VLsdAU3IFaSEeChiOjyTlx8NPM0wnsy3tYwyI-b5SvGznXXXPl3hFmxnzRCDJ-lljQGUSqtohRCIf0jOxr3sJx7o4jYOHqKVOKzPEML9n4-TasavCZMqA0Ki85kYCA9UkkdmryFNHjb7R4VwizQFysuz-Z_YYh2EjDQXKW7BbCwKNx9PB1FBhFVE4pbRsGD6iMbgmg4s45hHh7S2Qn4sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTu99UMs5FbxIM8VEiS4GY6015DUiV-XH7g5C_h2-n__SIOJyLBxPHINbkAGdMGAemfVK28zxSlx9oJttFx6hv1I5MqSXTtjUGvRfWjJ4rJ4W7n2STm9OcB6W9weQ9H5LVvdcJ3j_7neyqjh1FKaFfN6PsD3n2SfSaRcL7KE8pXxF4YJfQ3xw86FAUZBlS6c9l2PeQR0e5OPFJdAm7wSrXGMeyxHXat6DdgV9WrnnHdlHurHnM09zIbgLxQM-ccuFanBYGiA4i9OUbqvmoT3CoxS_C-ysh8XHF2QAV5iyFivwPeJEkbbSY3guWfr2NGxjFTAMM7fxi_OAUhdfqVZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAJWAaD33kDZen4Ot5fa4fjI64UPo1aSHC2r6vSzCqYYDNJs4olmjFvYGsn0yGGbByypb16qnu31sEJ7nxaQBfDvPc8KvQeY_aEIDI7psmHN1MGAl3Jz-5ajc9y4QOnaAWKZPPzPxye_Tow4cSuNfh9vriOTSfBy-QK3mjbb0SLOVfAGFwSjO6VHZX0IBbW2MHeUexZF8pVuYF-n6ob5ealT0y8agRIJS1QoeMo1QjTSBaGRiLepqhwBrgR0Xa3hz9iv6BK8uHm9veERT9UbCD_SvxmqIQjvUpEk11jqZZUUk88WhWdoNN0XFG7uFlfWix9LnO2-SabMZzYb8pSaag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m714JcbxCTUFdCpBEeQm0di8KDPYQDAFW0tCL-Kz6zL7Qiz-3oYW5_spgTvfTX14kU_XBDElStn6o_ZfD1wplKGkGCwIYWMhbYHrNsam0xvCUhmfWzdQwHCvJaohDgX2X4IYDNumRMKwY8TsEhotJFZY08t8MiWbFj2Ij2wHgdgUpOKlPitBMP6uyQTv2T-bIfF6goCM29BZjfH1X_bpLaUJLzSfI7N9Cj4WynN_u_auk8VjEQhVTcdJog0JD9hbl18-smsQSTCU_48Sxjee_q5EHb1sMKOuk1eftTL4uVW5Y8ZHzs49WvFiGwcjXz5lufN2NvsBAfaKoXwBXPNGyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaIbDBJ1iiDGfW54pLZ4Yo0nNYjHKE2wd8Ytk_fI41ERu3C12qJX3UFnMKZMssObr8BKGA3Bh9ugLGiuIZRXRJ2eTh7Sd4MgRKcbaHymPDKSLPLQlKRfhICZE4gT_vYSK4CzNg3rcyLUDpTv_25SFkjBIzH3bib2mHSdTsHgcgjcFK9wad-HEq4lLPgIyUb27QrteQV_QdfeNh6DNkMQ8cUdvsRoIB0bHxs5nVq51HF94RRefmY0quQS271ZlSES0MUSppFX76Hh9JalUG1dy4DlOn85UySsOfrYD7vmT1wZqZYKadoHB-EttQwSblHE1PXifZG7MRb9cuAKYp-SSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3ev6CzJQx1ZOtVHRe34_jHYWQVMHlxnu4CrmYQptSAuIUrR0L6jMT0ZS-_CN3tGS9v_lB8M6WdyLUxyAj5ZaRFjadIvGVjDEKPg4xjbB0G-BndnRvwD9piw30Nf8LRuXrw6GZSyrxZCVRe-7IchZk1eBgn6eXO5-sHkDVQ8a6hl-5cI0EVjz6uIkN3xjYsOULWIjwJlzzxiulfY3tVaBvEz9pLirAuNGrlUt9g7zW6GPEeMPTL7pqNdHf0LJfcKWpUNxRTt_n7tOm-kIaLIztTVmIr0-wwXMqxiwWTmV0Ft-g2Ag1OE659naC61jq-lEVyUN6Rgnd6yxxrAN7SHOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQPxDXhvaTYA4yCb69WaZBE6yCqhKsve5N7AQeCjy52VQC3YWipMF5L6cuetOtL9AcxZJKT-oVwu0dT3cObWZjwDd06qiaiWKBigUpj8YGTRYl4mEIRYOZqu_sj9a3XKQwup3wq0RhSC2cTLtvGBGaXtDuOLynphJxiG5bHgBryjOOoVGqvthkYYAo8MBod9cDGopvmphe3TYjcaTmwd4r14jmWFF9NM2eSaNeCkCuQ3QsdSHdtEQie-3APKM-ajWiNj7_bF7Ijhri9YHWBMXHx6RFD21SAv4T7k0d3KJiqQH8VziKOpQCIYsp3IbPIdyfm5-hRB6hIDqL2YHQOMbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=CryQi41Wsut2X3P903H6Jjt1_VskpYnqdRwHNBDq-y9fbyH7eREHCxxVer4PAWNdiJ6qhekPzb3lWpmFuaPTAm0uvtVn0KFfpMfnnGtq8QbThNBQcpdXZcf_3H2gbO_b7rxYTh8yRj4bfM-Dpjr1LXntJoibGbjoGn4WwYzJa98HeJgQCwX9o3Bw0oVzkWVwFc9DMV0V35YHScUtDyjVkm6wFsVhbGk3k2iHWBgOJS-AlgCGWk8n-i81p4lC0J6OTTKREh_M9E_dbYPwl32ZcBM-zhgwz2n_Ggfa_907uYk9NHS4CN9cHp2SK_i1vXRoLxdBRmENEySxDRCQc1LcoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=CryQi41Wsut2X3P903H6Jjt1_VskpYnqdRwHNBDq-y9fbyH7eREHCxxVer4PAWNdiJ6qhekPzb3lWpmFuaPTAm0uvtVn0KFfpMfnnGtq8QbThNBQcpdXZcf_3H2gbO_b7rxYTh8yRj4bfM-Dpjr1LXntJoibGbjoGn4WwYzJa98HeJgQCwX9o3Bw0oVzkWVwFc9DMV0V35YHScUtDyjVkm6wFsVhbGk3k2iHWBgOJS-AlgCGWk8n-i81p4lC0J6OTTKREh_M9E_dbYPwl32ZcBM-zhgwz2n_Ggfa_907uYk9NHS4CN9cHp2SK_i1vXRoLxdBRmENEySxDRCQc1LcoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
- لینک سایت در مرحله اول  - لینک سایت در مرحله دوم  #GPT5 #AI #API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/archivetell/6335" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nta6M82hOEEEK0wZ-LdPpzmH4vYT9aStEnXY6sjf9GSGv2defWhb1f0ZojB9J1UcO3MOPThOKU4UPrpPgCyhJkJHHHHISntAM4n1h-my2dOQlUyZUOREbH_VY7oK_CRHisK5zaf4D2qOORSV6_x6Ptz5SScERLKTCLm_z06mhlndgLRLJUIA2NMIPLhKNmRTydgdY07Azhong8tK61-xkk1fhR8H2SSBC31Blm6XBJuhBON_3mW07L4Qel1G_uoX-3s0W9kJDrKmeJxMbG5Xu76p1hD-iGuKA-vFeCDupFtxSQ9xlRJVdtx5c25LYTeNTVQbHCjgtEi8Z4OtWXKE9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aw7I35HUuy3Gpl2FjRwXplmN3tDz3-FMhGRnugwz0mXi1FHZ0mGoenwkWFxUe9oNcd4eHscy3ArQ2WAskEd_aVHNnMM7R2s-h7HmjMdnBDI9sdsXMNHgF_Wp90kjmgryb8DV1l-DbT7P8tvmdxHKIGOphDuRitrnbC8h-U9ai7AXLDaWu9sxJ1XzFAyfsOzQAeou9zGUNcgUA-u3KMbTdx_QmqqHPg01goxLJZtK5P4v4MOUBOtyILNVtSRxm7fxHdxFXs2pvnIlVJeu84itRbJjgOMxyPSnDNa1cePTbo-_y92pmfZXfbTnziPwK7cT6Rj6hCxUKhlF-OjIPgIOPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6333" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jL1EyH_rEa3f4lS0tYXafEFzwOzRBg4hKxCdTHZB7J1Cr0X2eyjkThRUGjFSfnfRmOjKAjMlPk6dfYaLcmblXVh3zMl1awH8v98TH3DBc1Ax09sTQv9HeTJkt4hYhw_XQPci7kB82G2QCy9tHgnq3s9ydxMg6s53pwO4HzjD6V31UFdkN4WL3cD1i2nZDzZMNASsgHBBPyybVHKNGCpUmDCLymkXZUovklpdesKJrTn0C5LWkQnonmPlL-yCSY4Eyfg9AX9n_JEVJLRYuFIacbY7_kJKyzUR2NzWw2XXCSccFk8r1iKNOuU99PdgrnToRKBv9lxP1PutG1l3K7OmjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZK6doXvsSIInRexxMVznDeItX6xpAuPZ_p5loiFIs02mkyIcrAcW4i-wfUwT3jnJ2sfqqrpDrqrc3448ArG1uk_csTovDpD603Jdj4iIp_g15ctpTAYEDXyQhpPXgAur4MAIa_j8wdTTM0TrHnWjzi4wTxxjqTeFHhbh8JUGPLnIkiOeSla957ejncMIYXi25_ttnlGNaW8AWQTLOoJoxJw6YGxPlAmonoOGOk2rR5KQVsw_Ai2E-ojau6qtP-aB8Ct-GCXweQ4Wi5kPLVTtbIP6CkQjIiHy-DsoVB6azW7gnl1bMo7RX13ZyxCdToP8dARyssnPVfoEYmVnex1xkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6331" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=L-gmf9oP4y7gS74Dg3Djohb2uKiiu7xMw-U3QhOoAESPrCoIzKR82dgIQHkjo0hV3xWoLtB8ruCsP8JAXYTj0Pz9sJVaXN7cDMGHkjHNo-6pY07PZgqDTN2VJWN41VsoD-XejKtP2IHAt9mgH91jD8NiIXp31p-xYDpwSnRm8aOMFUZC2huXtZHtlaSGqTBWtkGbBw5hZP8GxkPl7vK_OI8TuWoboWZAINETxpNZ9gsLF2Vvsa1iGJ608OLFpPFwmjObDCv6oludgZ7aoybPoHb8CFEJcfqhx4qWo7BduZ85KxnYpWuUXVx2sfFxnz_yVXE3Wedi6IeLWDtt6D21kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=L-gmf9oP4y7gS74Dg3Djohb2uKiiu7xMw-U3QhOoAESPrCoIzKR82dgIQHkjo0hV3xWoLtB8ruCsP8JAXYTj0Pz9sJVaXN7cDMGHkjHNo-6pY07PZgqDTN2VJWN41VsoD-XejKtP2IHAt9mgH91jD8NiIXp31p-xYDpwSnRm8aOMFUZC2huXtZHtlaSGqTBWtkGbBw5hZP8GxkPl7vK_OI8TuWoboWZAINETxpNZ9gsLF2Vvsa1iGJ608OLFpPFwmjObDCv6oludgZ7aoybPoHb8CFEJcfqhx4qWo7BduZ85KxnYpWuUXVx2sfFxnz_yVXE3Wedi6IeLWDtt6D21kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6330" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sqr-5gz6MG5T3oo9vGGFZ4AtdicEtJLgBUutfxelBtGxuLK3cv9ZS6PbOA16ipeLN1RWvtpWtJ8GsOfxZSSldfwwgzx_4vG4Awz51nnN9_1Tf-MsW6J39L4pfLVfoVB3OOahmt5-6BvrPkQL52e8oaUOSJoJGPj5zOANzCZIoWpFriahcq5kDWVvtMGlubmuuzFv1zFEh_59Vb1qsrDlWpKvoslC5W7QvuiavAh3sIQhkfSXBCPH-PBZbgF3JouWbi-I85rOgZDOcx52eyldm0h9u67ZTHTd7deqszGI9mPn1_r4o-ulnCY8l1iDE_EoUCl0M4OMtDBmboWcGwZj4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6328" target="_blank">📅 21:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6327" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBG7kst8LVD7rKACtKFWU90OQDLjoTl6RpSrijyX_17msceslZCdxoIEai9Sy59mM3L1lVO-lfEyyWaSwIl_F2qi4bi3kxZ_I7eKqV4abx8yUxzEk9xTe2B1-kI93YdxRAvoFV4WUBdU3qAWU5FG8804X_rriJo5t0Uhk79vuU24pUwg6FNDLstMufRTAqgMai0OP7zMKwsFIN6BofpbMIhLCZC7YwUyuHTZgBzO8HOTiCG6UTBtNn8xyRSJOW99u7qYpjmsm9pjkJF6X7gFOjJ6sxYJnxSeR72aUicAKrUMI8EFnB8BLLIocWTQpVL-61Eo9ang93k9k0kPyoTWug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5SFvpPzs3zH1dtaaOr92NCMN39gKPV-ps7tFC3yQE8ZTEZsHyHbWU0IG9YxUUdICOzc4AyCdXB7_tuKIx9Hytf_AoKYVeksJKgXFjoWfeYI36nw8r0YBNh0VdWR-QTQiU0_d5C0YxRz01yo4yiwXX9tAZo9sIjLj4vioz4YFIJDxMpFx9uuurjLsRThhk09keURaJ1aE0gPiAxZ2YxVXZ9e60LtyqqDJo5fDWl7YUZYpY5gauf5wg2SVubGiPOc3IvLZv6_oc_WSy7-DcbJFlOL8c1iBg0Zr-AHq_wLIul0XrcwUTfip43HsPmYQnMR4WYo7fawMEn5Xs_mr55m7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApZPKLRmgYDFiJlTZ8XSPX_ngIqGo-sBrq0y0tlCe2I3jbjd-TycJ-pnmu0kvHHF3VRMlmdnR6eP-JwZ7GObdOA6DUZoUCL1c6qNtyaQrwBA2S1doMwXlc-MELFYf526Llt4O4DPVKXomiq8JcZVs-aT7vf446u6LnulOsOXKGpG-bHj_-z0eG2VGs7ZEmCXfrhRaloR6Tr-c7cCn9pjgKredQbL-KrZgwldBB3HsSqVx10jBOCR20Zoo9Q5wwMu2x3B8jPcPrC2p7HjIinR_-XUd_J-S6RvmFaOdHXoZ9EW3Vt3Xu1wjgXGaxxPnaGTje8Vxrgqmat3sz5cXVCJRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=VXDGr-FKhGTesJ4958-47mbrvwTjbmWX18hTNqSSF9pKaXGAa16Vfs4Egu_TzyjDOX685B1PiY00nqdctj2P89eyrbMrz3gFWcYaVAo9voUoacfLf2O46XIbPrCD_zYARTJUj9Quc59cly-VYw7M5aXBmOAioYTkDWEbWmUAxwq56m7oyPizdSiuQy8SISjV8QxixFeHycehyQ5sdcnyRUnLAE8vdkNA1yV_2PAzUYhq35xKqtEUcGpEZdl2SaoNHpp2B7L9-MW5DIURL6ASpKwlSKDAdfLiavr9IpopTTYUH6ywjM3q0pgHecnQVnjopyMhweLBSnLEg3dWfVWpVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=VXDGr-FKhGTesJ4958-47mbrvwTjbmWX18hTNqSSF9pKaXGAa16Vfs4Egu_TzyjDOX685B1PiY00nqdctj2P89eyrbMrz3gFWcYaVAo9voUoacfLf2O46XIbPrCD_zYARTJUj9Quc59cly-VYw7M5aXBmOAioYTkDWEbWmUAxwq56m7oyPizdSiuQy8SISjV8QxixFeHycehyQ5sdcnyRUnLAE8vdkNA1yV_2PAzUYhq35xKqtEUcGpEZdl2SaoNHpp2B7L9-MW5DIURL6ASpKwlSKDAdfLiavr9IpopTTYUH6ywjM3q0pgHecnQVnjopyMhweLBSnLEg3dWfVWpVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6322" target="_blank">📅 15:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0OA8YA421LBYW97Oyr5Pd56FVUVtx3o-5WugKFuIlQxzseXbYFXDo1KB1bQVLfyaNpdbMd_CU97SJGv-nqsJPEr7O08fpsYM8Vq4g55kiNtk8FhU9bQ9wMi9aKqokkQB7ejRq39AVben5Cm1Jg0N9CumAkrLrDoEUzMCZ91q2044cS3r11q8zj7eBdZ7naCVLdFxvogqHzCAY476TzOSBjrAP2rc4ordlvT_1Z80szSSKzRiQHcQlMaTvut17Tzgn97Pfl5yNFWUIqG1jeIVtvSOs6IQzTULsuiySF_UndJCn-lJUqI_3mPnfD_mmXiFSW-zVqK5u53uasRoeBewA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت موزیک رایگان
🎧
https://www.musiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6321" target="_blank">📅 14:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GO5C4b3qRHm6s-h6kzTUfZETjLX7ShmMev3rmSonDVwYaoeZsauULql3NF0sbGmRnw6YJsxmFvUWIFLJuBykjVXCoJNMzVCrl8TAvNwXvcJdJU7WlgMTvN2T9tL32hxxD9uoWGpYH-00Mkz_GHmavn-LGIco8nq0z_FZ69z6OIKK9b90Dj6WNPz-OiPqoba3zkXvjGy_sRTt-nt1SD4ZV0wB1_cltwAsPN6CygvVI4kdGMrGesEaGTnmdnPPqUQyUUwaVTFWrrW7x6VdZz-YPA-isFefmD_tx9ruGh8ToWlb58X3g6xGj4EhiBFLhrd9_vAr4LJDhrlRld4Deb41PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWc8af7owwCSYl4D76UoiOoO7_fx5gKhRryT38r0LMJZqcjEnCrVZNMH_4PLIvIkTY1v3E1BswdH8MbVEqgj_Ltl-JZoPi8PEtRvs5cAU3QzgyjcX1h_podWTt2N0JYLun_WjMF4_MuHPHNULadzgGPJ4cNVFEA9_-zmppX1tTDeX_1QCao_rws2FmpsWkLpdBbY7kb4gU6VTXebq8zwnXPGZ7auSXdQ7pftLqp2VIlZ1S__iHxNxU53oPFnf4_C7Atb7MmUUDFJnacw6TapdrkkFwyNaHwTzCKljTktAk7q_NIeesnhtKfTGRxtDlEy5_Id74Hn_jbZjDFY8mLlJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6319" target="_blank">📅 13:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6318" target="_blank">📅 13:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6317" target="_blank">📅 12:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JycnQR6YwvBuOv3m5vdrYOSFchchOjuJGm_eO4qNf4NW-Sv92j9kPDzO1kzBGBFoIW9TgjCPzKaVCTNGz2K1fQKX9AJjckFbva1Laef8Tp4Z5o23KavV9e9AQsAE-LH6lb7UTYDAStnkEIYP2e7-8xdi1dqi70q5ovQ02YwwZD30xbhHqnJ-ZdBqYoeW_xHz5gOEgYTC9stulaREvnh70jd6gsVaS23lsyD6Ecv2O6-GMLy0dLbOvWYDDX0arStZ3EuiFZl26Hdf-Uj4tqGv3wF7HYcW9CBEHOcQbny10yWWtJYAcAhsgfHJAwI5sH5-7nSfxo_O_2kbLSdF9JKjag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6316" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ra6kwuQNAwd1Ot1Bj2rRBVwwl801JT2Sa6OVBdy8zYTudHBjLt8iJA50Xn6xZwpp9bGSAKOxm8O1XRkQP-erdVDLaARyESOmN6Nnt-S5Y-V2TxmQUHz0vBR-70gMKI7oQSZpoPXuhxKGeSmtYcTxTjUpnrJvxbwgg9RLk6VAjMuIKgjWQtnqAjYNQsC0SNCQ8layEgeMdhzbymeYTnUM7kcfpp2AnFJU8feIBH4G6ljZ6PGWj5QInbyO9FQFG832tHUPCKq-OtV9AeFJJnC_soqYX3Dde1QgF0Ierj8l8i4xOh1t_GL72BWpgYKIHK3ouxqRzzZedPzoIONp2bhf0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1atdsxcio4-BWrqxLxhL5H9a5lWu3i-cr_CqeB4gBWKhkiF4ijOJ07oSxx2ANQLRsUKVz6W5yxj-EfRMGL10HojkFtyy8NdKHUy-MAHVENpRQeD2f5kChrkZ-OVc6CsO8h8TnAUujJ4jShOHJdaj1v--ojKAOhyXDcDfEo8D34sJHAb8_qGWgmt2MGOZX_GvPEYcfF8qEsQzBwYjEmmSMpRyMKUgg79DxELrwFL0SeFegcHv43EYOX85sqGBCUQWo4Bxtd1u88OTwkdU805R-4Ip2mNdvHeSpjtBH22iS4l5K_Dbw-nG1yeYFevJMYLzSrLg4BGu49YEe25Xi4KWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=qyygO2VYXsqBj2xj50ngQ6jbPfzYtR0W7f0vTrzPy4L3dg46vrB9CVDOKRXx7HEy3DcEUOIfW34R9eUEM8BW6s8gdvbC2hIICfJqfGLvB_i-y_EIkXubrEt7XsZcqayMPVh8ujZCim3C_NounDgdGPsgU9YlMbVDuyv50ro8e8bTp-ho5W1DCIGeZu0AEu3gN0aEHMnb9qc4w9JNoA5TQ1l1a87v_ELHxsH7ccxfDYl0pvrAr4feEMIghUi8pnHPi1nU8kOHdPDJNP5wPMv7Q3_vI2k3uP8Xr_ecaI8xMWBum2pkz-NvOgzbHQvJBewRMlxMsiSHt-yiimQFK24Imw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=qyygO2VYXsqBj2xj50ngQ6jbPfzYtR0W7f0vTrzPy4L3dg46vrB9CVDOKRXx7HEy3DcEUOIfW34R9eUEM8BW6s8gdvbC2hIICfJqfGLvB_i-y_EIkXubrEt7XsZcqayMPVh8ujZCim3C_NounDgdGPsgU9YlMbVDuyv50ro8e8bTp-ho5W1DCIGeZu0AEu3gN0aEHMnb9qc4w9JNoA5TQ1l1a87v_ELHxsH7ccxfDYl0pvrAr4feEMIghUi8pnHPi1nU8kOHdPDJNP5wPMv7Q3_vI2k3uP8Xr_ecaI8xMWBum2pkz-NvOgzbHQvJBewRMlxMsiSHt-yiimQFK24Imw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6311" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJbji52Na8-sjYbMmA1Pheenzw_VFFaJl7hJ-JthYyclX6uEoO5S0rjxLixtjoLgYhqpZEO4sW88fTPxCVFzEZX3XuRxJLIeb95O9-mH6HfwFbnxrzkB8p2tGgipvCM0RsbxZ0SPHOvbxq7VFlc-weAVrz-EmjFtaesIZP14NU944iADyb1g8HkZz-utTc6khiVzkbBjQnseS9a5b_-YX8FSfjBrp2Xm0r93MDvyeXMwZeMZlVgUS5hJ4DtTJJq6B2kWy58iMvf0T0iw-sAzvU5xuVhhIiVlLCEq1EQ0aTgvlAk0KVPjFb2ZzDzZzN4kc3arxDS8qNRXtRpkWF4yYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6310" target="_blank">📅 11:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/6308" target="_blank">📅 02:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4IbL9083WZ8gngexubzZdPjMuTA_LWKvqsVaSJEii6uVgkAk9pOcQ5RloAhYAVgZuYKyFX7sy-OIqjBtZnkVODwW-3u8suRy8x7CyPvgIcHhuGENygZiXmoO3X5oEFd8975fVyjw08ihilHPKItvEAaFbNXtkdFkCVUk3MHkuCgPftldEFf43pRw0KZDDxcHKOLtMpk9n6SGVldwI59V41tBolC3VyuSQkH798Ii0-f14e4wzVXPYwxcCUGMynLNBo4kOhpix_MDxsZjCZcdw9bc8WAF_G8GEOU2hth9lSO-dCErr6gkU-SPf_teE4eJxHkOQTnL3oY9GRHaVebKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6307" target="_blank">📅 01:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):  Aistudio.google.com  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6306" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مرحله یک طهلیل من به واقعیت پیوست
😝</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6305" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/deGqf-oJ1OHG70c39kCplxvAKLvj07vZeZSWLxI55IyvZ63r3nBFxsgK5mF449eSL2uODaThTUU_uHWWr0LVdZ4qQWM3Lr6phvg3-XlpTJg0QuVrbptGVHzwt3Mb-JmxJlL2k9QwspM7LRY5zKBUB9w1orCfILo7vVoTJZL9FbmXSlYc2jLhwUqIBimP53O9kFdUysXlWzZGT4d8ygPMbehY2DP7kebYk8PlWFChYloPDJEJgES8YtmQZifcXSrMt2ArUSoKUpLI1LCkhw4DnLR9djtByY4bCkFvKAjKkvxtqoELqTXzhIP1jreDXsUUg1DExsGwiHHpY-LjA9mB4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):
Aistudio.google.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6304" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6303" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjYvVprbGL6AZgiPH_OLMHSarws1DI7qg8f4QdHGq5rjhLj4ch-dYl8y3qowE5ScVFZQW4u9OWlQRlgjvFhrzP_eMsbCXK2KB6_RwSXdGecGR3lbBGuNR9zIed-Sx_T0mvbdKNkNY9Pyu7kMVh1hMmISr0TfjQbizsyp0PCk2uQf7pOUxGW12tWYde3hu6mYFvjNSqJKe1DuZxP_BS_aPj7YmSnFly1ro0vO51MHCDhlrkB-OVpFYAFCErg2uh82mWYunzdjYljoAcBVC5wkYr_sH3cwCt1V0ImW_h28YeLgAs59_kNB_rB9sx7jRk1_eW3EKEznI8-k4UbwsfZ1_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=VSuRqeoN02gJwcdpCtu6wI75DIW8ZnR-GJYj6s5_K6aLiWpRGvBmyka6D5vz30xKomEdav05ZRf223ycuHpD-V0mEr1Y-ZLJXjOTuKacLDmNw_pjv5Lohi17bWMpBvTr7uP7VfwFJjfK7Ql58LMhadwxhkUPw_ZS0cLslpk_fRxJ2x4TC63ZoJBMoUmWQKe8X1pO5phlWCHMq0yyCFO_CJVsEuyo_twsxV3co5AMIADtRGN_OTNdrfvY_fybZDMQ_g5_m30vF4y-7ZJuu-5lOV7FHPxKaTAak_cY58Ahpqnpz4CNWy3yrXhVTxLCOw257T1bKLQ4g3Ube8tKp_SE6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=VSuRqeoN02gJwcdpCtu6wI75DIW8ZnR-GJYj6s5_K6aLiWpRGvBmyka6D5vz30xKomEdav05ZRf223ycuHpD-V0mEr1Y-ZLJXjOTuKacLDmNw_pjv5Lohi17bWMpBvTr7uP7VfwFJjfK7Ql58LMhadwxhkUPw_ZS0cLslpk_fRxJ2x4TC63ZoJBMoUmWQKe8X1pO5phlWCHMq0yyCFO_CJVsEuyo_twsxV3co5AMIADtRGN_OTNdrfvY_fybZDMQ_g5_m30vF4y-7ZJuu-5lOV7FHPxKaTAak_cY58Ahpqnpz4CNWy3yrXhVTxLCOw257T1bKLQ4g3Ube8tKp_SE6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSfs43OzUmTRR8Zc7mMMLxi89gJ2mwyNVRwIfd7k1kL_SYUCGonGgKY0vHDDK5-C-UhvxWQFGReRqrP_4YsGjtp7wgN0xFwaks4ppWkNgTB6vEeJa9GUn02r_M6N2_BWnF1wPb7Etd8FLC-H8si7Y7Vi2G2k8ZdQsWa95jOscIyoXtA_xy8FMitoja-8fkg_JK69kULzI7uQ6ef03GolJ42NFO13S5TD7-JR8r9iJrQxy6y1xyu3T72CjnQvoWwVcND5i3KrwEqNBPuiSgSpjeLH5OsAWSyGDWPOgtFLNu8ryJGuiPWIQWnNKNSmIZwWKQQOaKid4VD6KTTEDM6l4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6296" target="_blank">📅 19:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اگه میخواید به سرورتون وصل بشید ولی مشکل وی پی ان و این چیزا دارید و روی cmd و ترمینال و این چیزا وی پی ان سیستمتون کار نمیکنه میتونید از ssh آنلاین تو خود گوگل کروم استفاده کنید.
https://webssh.webhorizon.net/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6295" target="_blank">📅 19:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6293" target="_blank">📅 17:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UJW-b14Rd4luvEd9oE_KFBdhZc63SO1KulKVycXWBoWOb4j5rP9Fig8V6VKEguAWyueCBq7i73gSaCpr7U781XlL-uwFEmQ1tsgmNe-VTP4hNveCKjPJrfsS_osO5PNdk9M7d2iFT8Heq1AZzZ7ewj6LIWu_x7ISyrB2Csq2cK-mXO3aMFb9v_GYayhVBLx2bgids6bPFg-SOC7IgAlqgIQCrEPrJ0kRwOBaI1qD2a0_Y_LINDNpOvJJN3wye8ESCra8_tRdrJj327in8viZkwhFIiWsO3e0Oii6yT9UOY11EoYoK8LID6EdhYmHj4p-q_r1Hjct_2ZLv2f777tcbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uwasvbVGAPv9pofC7d_hunjmULceTMdPeFZQTWgq551IXduzv6lkPNr8Ba4-4XApSPilguwyuiAOsBE-TY8mDu9Omx6SDSyURdTn1B2PVgLQBxBw2QonuduZQvaEjv5hg1xXxeWtk3Zm0C3CjtGFduN6xhenVUpYRE-xvPJJNGmvFP6K7SOWesXdWKEbvdN4B-C5KERG2GXvrfc5myIAuuIdfFCk2RSAAo3hjzqUm9BWevZnyYijqjdZM9C3MbDz7lqqf_SbdA4v3o7iYxNK_3KHnFOtZSyA0rHRNFXNvvrjAkB7ommlfqladnIQ7sWvuoy4skyhhB7iwG2DHx6Vow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0QygewvCkJDHPEFHTxYkqjCoE180nb_bT_kCUte1FcU-rMVoF2ZkBhAevbcwVNWwsarolbon3qtc3o06mNGgTkUbntvJDrQxB7rhHUxQ3pYu0Kf9Ps0iKA6GYILoW-yfGJjW_M4koafc6AtV3GT9iF3npDSe0UgGf55vIYvJh8RtEwxcQTmLcXnetNj2N2IMws_pV6XgM3WC3kW3KikApmp_gdhZZ-XxVwEHheTMKJZEq0vnJIgrVwHR7Xjuz70wXCeMRVMQH9TTB3U6qWFF6W95C8Qm44ClQxognvBSp21c3Krjf8K887ve1EeHxkgetAqJy848EMl0VsmhgVg5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6290" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54834411b8.mp4?token=InlRwkhsQXJ4D5Bv0YJs6qGiHJzD_7kjm_QMkQtIl1UGhtO-hS2TCbU5pRJJp-x5RkleIjVMUOnd3cXNfcL1j_V9ISkkLiZ3bVk63wwM649ECw8DxEobt3Rol6URmIWnPta2gQfU0bOM4G4XYacPUh3_WC2dI1JVRI2zrr7tITN1UDc8WTDek_x6zOLQ-6rXFRHZ2V3uYtiO6nK0Dm375i_gP04trOt2VZgo5BrlgRW5sjWFANfoSrQIq9rAJs_8lMwoecE7DNAVwbg2OWgcUKILVfCHsdwPf5J2hKfOoWk8KEa__Wcou4GbWBx0V5DbSDM9Lr8N4eX5jrTeXFQeOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54834411b8.mp4?token=InlRwkhsQXJ4D5Bv0YJs6qGiHJzD_7kjm_QMkQtIl1UGhtO-hS2TCbU5pRJJp-x5RkleIjVMUOnd3cXNfcL1j_V9ISkkLiZ3bVk63wwM649ECw8DxEobt3Rol6URmIWnPta2gQfU0bOM4G4XYacPUh3_WC2dI1JVRI2zrr7tITN1UDc8WTDek_x6zOLQ-6rXFRHZ2V3uYtiO6nK0Dm375i_gP04trOt2VZgo5BrlgRW5sjWFANfoSrQIq9rAJs_8lMwoecE7DNAVwbg2OWgcUKILVfCHsdwPf5J2hKfOoWk8KEa__Wcou4GbWBx0V5DbSDM9Lr8N4eX5jrTeXFQeOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6289" target="_blank">📅 16:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6288" target="_blank">📅 14:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6287" target="_blank">📅 12:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⚡️
سیم کارت رایگان همراه اول به خاطر جام جهانی (کد تخفیف + پست رایگان)
CUPSIM26
هر کد ملی تا ۳ تا میتونه بگیره (همه رو تو یک سبد بذارید)
لینک خرید
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6286" target="_blank">📅 11:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=nDdG5jfDeUBwe8D2pzShf_KUfv7DVbI6QQn82FkiD3gaH_LVZOd3cr7-7nrCrgtxFsBhFIVqnk89f0arWcyYJlqqNkT93TP8AlGaSebMGvoZx1e8_QhVTUdfk71y4QSVYojOhDJxMYZSvy38Nnr-jCnLXvnEnwCDwxxop8c4nSWaydkAXeQDNedgglOR05xYqU3VkSuF1pSJNMX83ZEI5mOIchiyy0HyMAGRM4Y-ASbOJur7LFigLnG4yAhFQ2Jr9AnpgGRud8veBAR9y8kOMzVqNpVhPzd5MWMoynLIzhqWksE51wodGWFcxqF9JYkFAMIULi_9dVspyqAKAUHY0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=nDdG5jfDeUBwe8D2pzShf_KUfv7DVbI6QQn82FkiD3gaH_LVZOd3cr7-7nrCrgtxFsBhFIVqnk89f0arWcyYJlqqNkT93TP8AlGaSebMGvoZx1e8_QhVTUdfk71y4QSVYojOhDJxMYZSvy38Nnr-jCnLXvnEnwCDwxxop8c4nSWaydkAXeQDNedgglOR05xYqU3VkSuF1pSJNMX83ZEI5mOIchiyy0HyMAGRM4Y-ASbOJur7LFigLnG4yAhFQ2Jr9AnpgGRud8veBAR9y8kOMzVqNpVhPzd5MWMoynLIzhqWksE51wodGWFcxqF9JYkFAMIULi_9dVspyqAKAUHY0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6285" target="_blank">📅 11:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XogabGMm1wMhalM37EhG7Eqj7ydwWz-sbnqGxftPfM3l7IbL62kN7AqoT9gBUn0HaMAKtkdBUwxXsWUcK1ke0YOA7QONw5xAAKy_OvqjW-zSBqmyyPW0FPZZ89Odt6QzrVN1zVrTNE1i7iycAGyb9CwNMaSqpfbC0PO7pFwiutX9q08pnFcDTeA3WCpf8ALd-vNkKstUYJMrZD-Gmp10fVL59j-Jv2LA8WosQ9WsMEYMT6k96irwBvJO5P0QHeI2_evhS3JQiR3PZJ8M5DFs9NGmDjSSJ9Qw_d1HwvGtTIrka_2GlbtZn6YmVX1rbbTc8h9Z29W9PsERYId2FmHhUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6284" target="_blank">📅 10:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=u0P_aZ87oTrALBL50bpCPEwTRjbBXpg2fvepC-GhsiyI5TDOyyDEcuwqyaEMaFnBL5riLyrEqX3OVcPdYhFdHbe8BGaeZ2DrUNPfG3n0COfc75hd_xIRotxcQhUfME8evWWTQ_LvqXWJ_xT5Y528ttVgi4RghptJdncriR9HmiTOnZn_E3xIOrrRZxp6uDQE0kFKeJCLSmrXpWPYmShcugU6tSb-gla_Lg9jl21rCyXjyX7l871q1m5T-eSdXsgKq0dvbiYxCY1y8sG58ON9O0rgaTDCnK49mxWro9qVexurWdX0x0vA-sWJsTBJ1utMgB9BU53qFkhgiEPoUFmyVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=u0P_aZ87oTrALBL50bpCPEwTRjbBXpg2fvepC-GhsiyI5TDOyyDEcuwqyaEMaFnBL5riLyrEqX3OVcPdYhFdHbe8BGaeZ2DrUNPfG3n0COfc75hd_xIRotxcQhUfME8evWWTQ_LvqXWJ_xT5Y528ttVgi4RghptJdncriR9HmiTOnZn_E3xIOrrRZxp6uDQE0kFKeJCLSmrXpWPYmShcugU6tSb-gla_Lg9jl21rCyXjyX7l871q1m5T-eSdXsgKq0dvbiYxCY1y8sG58ON9O0rgaTDCnK49mxWro9qVexurWdX0x0vA-sWJsTBJ1utMgB9BU53qFkhgiEPoUFmyVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6283" target="_blank">📅 09:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bu1HuLOsVlnpWRPQbLDj02Nwk328ish2y5ZzuuQ8euMsgByTM5X2dstQvYfieKP68Ctx4DDvOLfNq4KfdHvP_p5v_qOl49Kqh5QVa2yRBy4bFzjPa_dLO1G4lTyzmZsvrZ0pPMO3ox8Er8TmdBnyzZ_uuQSq73x4LNEMJdpfPxSUbNSzfoGDj1xjdhbr9eRg4l7GJHB84zHfKHAMu5HDGQAWsTn9iAwRHOoE0MOif1TagCOjXAhLO6Cboqaf0PzaKx4VmhF_sRs5FKBvS4dAazHIdirrVeIN3zZwyG1ORVYRZAMIquyh0MnsGNT31Do-HCiTLG7-KmDwd9ce8BeeVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6282" target="_blank">📅 08:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXw8XDPZXFwq-fz_svLYaSuvMLB1cmNHuv0ZAJxYxEHyKkYaWluKVCJv-Al0ULXqU5Fx75274B8hzngq8ybfpKvX-rsJNqtgWzvtcSLCrgHOM9A04jP9y97znqAKPZoy2PXuEWLKzvtxy0vkAg0Nod2XZ7V2rzSdQoyxsvfsf5AYcpXyqOMQOUIU_Q3R8-X37XFLBz-pMH3JCIDvfNpZlyyYqJoPLYcU5lqSu6K0vPXy2Kb56tyHVNfBfyXQjLvW1ebSgziINiYVAdTViseo7IlSSU8XfXuCMnVoCJoY29r2bzXeOouNHom4S3acXQ3wNOupzpJr76Y4t23yVK8ncQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوتاه اما جالب
❕
به این صورت داخل duckduckgo میتونین qrcode بسازید
🔗
🎁
@Archivetell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6280" target="_blank">📅 03:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6279" target="_blank">📅 01:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚀
راه‌اندازی خودکار 3x-ui با WhiteDNS؛ از صفر تا تحویل کانفیگ در چند دقیقه  اگر حوصله نصب دستی 3x-ui، تنظیم کلادفلر، گرفتن SSL و ساخت کانفیگ‌های Reality و VLESS رو ندارید، WhiteDNS تقریباً همه این مراحل رو به‌صورت خودکار انجام می‌ده.
📋
پیش‌نیازها  قبل از…</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6278" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=rGStRxMWbdMvnX7dN06tlmryLVxtV5o-FeqFMU0Ux7Q3p9XqJl3OyTTsEdUxUL60Mv6iA4D1vhxv4ztfJ-la20SasfkMNNS5DzULc2RuZX9jACMVy61N1C5whxF54J3ECCAOS3ry7iPkJkX6UVHw0Biacn2Pg3hvskGeGZRQ-ncUqMFctoiaFfaLOll7smAaMQtYgsckCYDcQqwKY9Q92l8mmUkR62Fngpx28fI1czpIgSWT8_f7qz7v3HQfwzjINiDLfOdpjw43wHsRQ4RQi05BGFCbzhCZUSv5k4ZiVdmd1k6d8no0DQmD1INTW3Tah24CWhqDWFplVw7IjbzOlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=rGStRxMWbdMvnX7dN06tlmryLVxtV5o-FeqFMU0Ux7Q3p9XqJl3OyTTsEdUxUL60Mv6iA4D1vhxv4ztfJ-la20SasfkMNNS5DzULc2RuZX9jACMVy61N1C5whxF54J3ECCAOS3ry7iPkJkX6UVHw0Biacn2Pg3hvskGeGZRQ-ncUqMFctoiaFfaLOll7smAaMQtYgsckCYDcQqwKY9Q92l8mmUkR62Fngpx28fI1czpIgSWT8_f7qz7v3HQfwzjINiDLfOdpjw43wHsRQ4RQi05BGFCbzhCZUSv5k4ZiVdmd1k6d8no0DQmD1INTW3Tah24CWhqDWFplVw7IjbzOlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6277" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=sftG3n3knIAUlwIKZ_gwHz4MaKwlHVT1Dc6aisOQX4-LKKhtjI2U9tVsV_qZIIUDH1lFQtBKZBiq3OQX8AVwEwtGAgqp4-1LVVodxYEYlZIJh4kXOZ-TOUi55z_3F5rRCGS1xrKi90zpOx1gY_E2MkESsqKzCJGi4gHiKMgdPWFY3-7TjUfn627mOKA9QeiuDzS1dM1Hra5lI4AaW_zuJLS1z0d9X-M7UEcXpzJLP9ETYmeg7GGraOmf5oqEzLRNuo4BWLPO9Bbp3XWhNqHLOHErPCmfsr7t2WisoWd64XS70JOyRJ5AmQp-37YjkpS76puMyzoUAI6Fc0VLqUhP3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=sftG3n3knIAUlwIKZ_gwHz4MaKwlHVT1Dc6aisOQX4-LKKhtjI2U9tVsV_qZIIUDH1lFQtBKZBiq3OQX8AVwEwtGAgqp4-1LVVodxYEYlZIJh4kXOZ-TOUi55z_3F5rRCGS1xrKi90zpOx1gY_E2MkESsqKzCJGi4gHiKMgdPWFY3-7TjUfn627mOKA9QeiuDzS1dM1Hra5lI4AaW_zuJLS1z0d9X-M7UEcXpzJLP9ETYmeg7GGraOmf5oqEzLRNuo4BWLPO9Bbp3XWhNqHLOHErPCmfsr7t2WisoWd64XS70JOyRJ5AmQp-37YjkpS76puMyzoUAI6Fc0VLqUhP3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6276" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=c9owgqdrWwv0SoLeYRXGYWp4s7jZlg-cTAlIDm2dT4qW0oitg7sXKSiUqMJhJJQZEOses5l1MgjqHyPYcwyCcvBOwuOZXUGUZbB4Ht_w6_vDdz948kVAIZagqWTnEVjCQenGnC2uuHjTFP4cAsRiKQEeBacZ-NxJLylblN7A40dtBDtj19YKCb70jBW2VOKyqfbmU284zOrA_AKhknYRxWeIlVhuFVAqKKxZ9z6iGQwFjQOlKLwYfFBeM4ubgyrCwcYpfpYyIDipnYN19s5nXVdGrmnEe2xxbRbel5qqm3hgnXrojeLVPO5IdK1yHVAlTveKOD-HYEJ3h31N5I69ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=c9owgqdrWwv0SoLeYRXGYWp4s7jZlg-cTAlIDm2dT4qW0oitg7sXKSiUqMJhJJQZEOses5l1MgjqHyPYcwyCcvBOwuOZXUGUZbB4Ht_w6_vDdz948kVAIZagqWTnEVjCQenGnC2uuHjTFP4cAsRiKQEeBacZ-NxJLylblN7A40dtBDtj19YKCb70jBW2VOKyqfbmU284zOrA_AKhknYRxWeIlVhuFVAqKKxZ9z6iGQwFjQOlKLwYfFBeM4ubgyrCwcYpfpYyIDipnYN19s5nXVdGrmnEe2xxbRbel5qqm3hgnXrojeLVPO5IdK1yHVAlTveKOD-HYEJ3h31N5I69ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6275" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ادم خودشو باید برای هر سناریو اماده کنه و باید تو پیشگیری خوشبین باشه. چون شاید همون ی روش هم جواب داد</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6273" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">همین الاناس که ترامپ میاد میگه:
دقایقی قبل قرار بود دستور حمله رو صادر کنم، ولی آنها گفتند ما مذاکره میکنیم و من برای این حسن نیت آنها ۲ هفته حمله را به تعویق انداختم.
ممنون از توجه شما
دانلد جی ترامپ
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6272" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">برق قطع بشه با کبوتر میخوای پیام بزاری تو تلگرام؟ 🫪</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6271" target="_blank">📅 00:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6270" target="_blank">📅 00:34 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
