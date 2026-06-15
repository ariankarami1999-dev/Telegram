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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 22:33:11</div>
<hr>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🌍
افزونه Local Translator
؛
افزونه‌ای متن‌باز برای ترجمه صفحات وب بدون ارسال داده‌ها به سرورهای خارجی.
💡
اگر دنبال جایگزینی سبک و خصوصی برای مترجم‌های آنلاین هستید، ارزش امتحان کردن را دارد.
🔹
ترجمه کامل صفحات یا بخش‌های انتخابی متن
🔹
استفاده از Translation API داخلی Chrome
🔹
حفظ حریم خصوصی؛ پردازش روی دستگاه کاربر
🔹
دو حالت نمایش: جایگزینی متن یا نمایش ترجمه زیر متن اصلی
🔹
ذخیره خودکار تنظیمات و فعال‌سازی خودکار
📎
GitHub
#Chrome
#Translation
#Privacy
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
متوقف شد
❌
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRtiuQzOWbgr-BQRVq1XjPeliTlJWMX3Wo_6cc4xTDTBCY1BD9nxZCfCQeMAFN8x5cIhKJLm-pn6DO2-hrp2JUPYEj3_QQIn6GSiwIvG-qPyAu8yE-ORVZDv-7Jyu5Pm1T-7JFBNlo8zFPxg7ie3c1-cIHiZbh9UlkxIr0_E1dYxe87q_jQPZTPLScAY0TuKPP4cN3gzR91d17B2wAPXTs12h7D4BtMUQb2zEniqBzNrxz2oWqkj5zz2dJ5BlINp2vwnB2wsAJnFCZjBsAuB0eDR_led0KMp-zZCU_jpBFfm7u63iLYmrgSaifzS53ICNY-SRUIih8bin410aHEHKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agwH5BsE0PeBNu3gruyflH2GZxuiABMEfplKEX93ayxDMEWtDiB7Vmbsg29GMKa6JJR2hk0A_dS8fPMHU27IPlSoem85sjKmd9n9vorZjGNYnEXKldOnrHAurLkdZ8ZIlmO9kx--j61unmSSRPvPsaE5YdQc-ulvqfFYR7tgyUA2GOo4D8cbCRt8AYzwE-iLLhhoJ2MuQ18adSnKk2Tj6SmvHgGecTqilrZU7HKE31YbA5W7bg8Nw9Sdku4v323-7mmS1S_JIN8G1vQplJGlGuEaL0kcdbT_pP_nBZDvp5fAjhmgPyp5VtqNW3guF_XUkyPNA_Ct5R2vGx4Q68Z3Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvmCgBXD2C0MjG4dmb0NZJzF4sRaHl-8zT2Upi6jwL_xw0Jgnsun1l3OmEFMxhAE4JsBSvAGBzk9xqnChKTwObwtkgJ1FhRRQzT6pnyNhpW6aEN8Vbaj26FFMNfKgTbczDggKX2xJPpoVa1hAxBLejD7o7KvaOZW6r1yhSqnI0VRB1pi_EkBgvP4u5IsKVBvkSvFBKlsT7Wp7WsJTDucrj7ZfaXlr8ifB31SxVu0Y_d2KFzTdeLL1_3eWQf35xZ34zdnjW530tpKwJO9TpEQ8BjZmCK0bFNtk7iwHVmPtBVh4fTWYxUoydHXW0XFi4cp-9PuGoVdSK3mxqQi3LcK7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPSI09B7hxleM7ge9aFchF3YWSzvD-e4V9MyIho4n_Ic0R0YM_e6QkGekDbe_duj7pGBc1ZlFvbC3jIG0kHmjoDAojYXWyZ4lXLJdm8eHCbmd5giEqz3PMPxeuG_F4rIyocZOLP8AQ9gkcXS-gpnGC0D2kUR23vID08CV9M5SGnV5sznIhqcqGJdW7gqkRVsuqQ6Y3LBz5-kcm0xCmgkaFcaU4aLb_cD8cYMpQc90zOWCYf_pl-av5cyOqHkDq-TC9eIWONa1WqHk_waKqoTxT3iehQZrDnbmy_CF2_U0fplxTtvykKskcbu94t5oXGzSEEFL9mNSVMVVrJohlFWrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j99DOniud-y1U4YX6OcdEkl0bXszzXLFoCaflXbLZrhZDiWW1cvk0N4IwzikkI9BGewDnDIzSB50XS0AtDICexhxkH0jKFJiQdDVO7KoP7NtS1X_opx9hNEhhNSSVa9UMStgRSYwT3DzxmrQToarrQn7wVfyQ9gWebcPZQy6RL8q_jU_j-ZbV8xD0L11awhwM1PBAU6MzKveAg9H-aYZD_xHiqeo-QIq286feyl7ptfSv0UMrV3GxxsHWYu2sS1Fm0srRaNhuLwsGnJkYUxvKauYUx_65Qf5KUPmZqReI-FHj5dmz7PfHMru8qynMhoz0g74R9_y6l65qeRgcAqU0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjR2bzHaRm-kbrJYjQ_DcN7Rezh1vu1mVSf_eeZZZWghzDg-WBotfjDRWRk5_GiKPIxHYxvCGKlYqY8KfHoTqDAwG7fRmIquyBfS3jgrC6easaXKOGbg26cpIaBexMx_swm4Io_PNnS567An_rVERglZcv0GXIfGQAwJUoPzVkW_ivYuxNIF5nDqNWQlmqfBosLr5Rh13PT5QOa5gZOpYpXSRMTlXmbBB9g9BwS16ciXGoOJnJ2LvXAAQMe48AmQtw8KhIjGyV_AmJtWY6HRfcMCVYwxu2idGDfj0w-St54gBH3OkBOxb9N3Gr9XcExPZup6YUKqhc8beAbb2KfIWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9Ui_HGa7QzujEaRH7bN9wnMYAeEGHb0mW8TqevsrlVJohro--1RTi2D2g3B_qQ7kuJxZbrHjPWd8qabJwiGW9_oklf7YF9eH1YDSOatC-gF9wPRfK-1BZoF4VJGk44_BnLa5a-e_rBgDSvyWAbmLKzDYW4Lo8kWFI9VlAvyHDLoUkMOBg34UlSo-X2lv8i63o3KBoOOiYYv1cKr9mVoIQDmBeIwF7_DG_sWvSapiPJEY3ZD5BIdj_lmBPAoa7BH3dMgLBc1Q-gMhcoZaTzldw1n2KNH434YMsUlnkNhksfH8V-RsiGWGziY26qV3-DsZIJFZ9807Cu5XlaQjQUWXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9eiRd1U7HyuPip1VxNnkdpxeaWjmqDUH1xWKxmWqrNX0llNrm3abjH3v7bgoVqRvsgh4VaGJ0hJPxsx9NaEhNzP-9I8xZoFKOsVMUoPlE0JOV1OFDxpxM7c6XCoKEnQFFlaBJtHXg9ras8kvnG7Tx3yUqKQOEh3gYVH9umqoUfXklFiLRmDbAeouuM4txQ8Tp3Tb5GGV5oNEmiwLF3R7JeEILJj-kzA8BAHDA7eKTe0mL9yWXsasH6lWfvncOwvNjcSP9jDjObFgRTioqf-tyzPNBA40MoZr7vnIRcNtH2vw_Idm8VuDJf4usuRGeaVigKAPIAf1xIahZxrNi1YCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=bWMZSgjZc4W79J5zYxHCRy2CtnfNi351JStMIva6Pe54tEeWA6NbqiXfm-0O8xJI1jJIDJMA7s1VWHmQpzz0XYHsBvcePNI3LpYCwsDgEx9ebcOqz1s1RJuSkMTXSJBzCbBuMmhoprVB2UGJwjowadaJ7zv9bTSHnf0njv95cZnoPKlkujpF7XF-MD7PBAEMXi29e2e84mAA9dVx6LEIgWaqj37Ut54lyB2J4t_rsZz36BzuEuzU_EfKY3jk3mIvSTgDyGtbLvDkMKRrs423ysERKEiQtqfaqhCvndIJGrhibwwPjplepu1LY4GVYhXGBKfHcCnNhz-BFarBElnOcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=bWMZSgjZc4W79J5zYxHCRy2CtnfNi351JStMIva6Pe54tEeWA6NbqiXfm-0O8xJI1jJIDJMA7s1VWHmQpzz0XYHsBvcePNI3LpYCwsDgEx9ebcOqz1s1RJuSkMTXSJBzCbBuMmhoprVB2UGJwjowadaJ7zv9bTSHnf0njv95cZnoPKlkujpF7XF-MD7PBAEMXi29e2e84mAA9dVx6LEIgWaqj37Ut54lyB2J4t_rsZz36BzuEuzU_EfKY3jk3mIvSTgDyGtbLvDkMKRrs423ysERKEiQtqfaqhCvndIJGrhibwwPjplepu1LY4GVYhXGBKfHcCnNhz-BFarBElnOcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-6q4Oun7khaeN55dBVZ_DklVfGzHDx7XoXNrb_o5fDG4VFjfGK_Nv-sg3j4nhYWXD-qg54DzLQXBs_P__rGMTDU3FdjN6OzJbsanp5vbVHLeE_tOQV8iUe-s5TzXDbgbg95O9G3ufm_VtjX6lfAKD6MvA1dZHzccm4UlkR6YHXVPG7a-Q_OfgftI9_ksKt9vDMAkW7Au1uMVYmyvUUhdfBZEnbifGb38CCT84nQMhkxeZ7cJ5Aaael2FrDGcidDgbILNyRErea61NdD9D9Yqb1Jnr_gcSeXo6gQhTEtRy3ctm9MBhzWK_91xsswFAmCiAHxg4zNLN5khn-l7OBkEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ze0IhBjeNhMrKEsGkUw2w3JncoTb6mnWs9QIrf7RE8QXytVeNuS1GnqsKtWIj3cuH3xRAdhyrnFRsTAtFK7sna_yIksg3F6HBVJ19oO1olomr6UiEfkAh_8T1NprCR06vhS3uzKYH81DUZ_VFH0Id1ZgQfqqiDqo1c5qkhhK_Qnxy_Fp4rYaEundmkOGj3F-U4FyQFeoUnthJSMsAyF7ScGcwNtFJH6jYEWDBDVOJ3drUElxpd0FgArQUburqedAcxRrWDtB9a78y0E4UbEjdvFCsLY_Kt4KZLap2fMZ1cuaxCn8dFakXuhFTCQ_aiPl3-aKAHSKKrgOfBcmV7UF4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=KzSIH1-4xsGLYBeps9-BriTLQeT7QLaIfsrsEDQaq6ZTiUOOYlpL-ndj5NM8Zlc9B9VdmHZ5cQ1Jx33ZiS1awTcgHJHAPcpUizh3iEB0cga-6IJ43a8Roj9fhzd6qVQrbg6qcYnDR9nwqokX8Pf_E4jABSgGhyJ-L1EF6CXsVD7G2ibQx1iF0y9tBBekCWTgTQEDEOrPwali2sqocKgXZSlYicvkiOox8EXwE7rcG0_aDxRgecq4kbqhbwYIbOM8cdzfc88LoxYjEcFjXdM1Z3GCtMifdROIIYHPNgSGou80ZP3g3zV1_IkwzTi5AiatUBpCslx4YajtaLPnZSnf65pXxhSOVfsAu8b912GnWDApCX0Q5wuKkxlZApNGt0gc_KRjS9Mxbgo5h85ziiXD0pTG0K6IGgoZTN-KrAbpXKmfjrebidVr1fOfTFHU61WDidYf4HQaQU06VPtrgzs7x_EpWTTWfSJTZ1U7pVikvCmWwzLC1AGPg69G8epOv1fU53c8Qr2ng2QwiUOdmiDjvw4uY4bK_USB82d2JJk3xd4ZlXncTk5DtnzyFCbpfPugR0Vekasl4uUzqf5lBDCaHM-7nkrAwhLSSvOA5V-TXOrib7dg2faqvZAO1u3lVZGyxse_qyzjQU58Eg4djktMhFxrDWZtlN2Ckio502cdBsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=KzSIH1-4xsGLYBeps9-BriTLQeT7QLaIfsrsEDQaq6ZTiUOOYlpL-ndj5NM8Zlc9B9VdmHZ5cQ1Jx33ZiS1awTcgHJHAPcpUizh3iEB0cga-6IJ43a8Roj9fhzd6qVQrbg6qcYnDR9nwqokX8Pf_E4jABSgGhyJ-L1EF6CXsVD7G2ibQx1iF0y9tBBekCWTgTQEDEOrPwali2sqocKgXZSlYicvkiOox8EXwE7rcG0_aDxRgecq4kbqhbwYIbOM8cdzfc88LoxYjEcFjXdM1Z3GCtMifdROIIYHPNgSGou80ZP3g3zV1_IkwzTi5AiatUBpCslx4YajtaLPnZSnf65pXxhSOVfsAu8b912GnWDApCX0Q5wuKkxlZApNGt0gc_KRjS9Mxbgo5h85ziiXD0pTG0K6IGgoZTN-KrAbpXKmfjrebidVr1fOfTFHU61WDidYf4HQaQU06VPtrgzs7x_EpWTTWfSJTZ1U7pVikvCmWwzLC1AGPg69G8epOv1fU53c8Qr2ng2QwiUOdmiDjvw4uY4bK_USB82d2JJk3xd4ZlXncTk5DtnzyFCbpfPugR0Vekasl4uUzqf5lBDCaHM-7nkrAwhLSSvOA5V-TXOrib7dg2faqvZAO1u3lVZGyxse_qyzjQU58Eg4djktMhFxrDWZtlN2Ckio502cdBsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=T3ahl2h-8rVVrcwVV1IvRMNgCnkaMnFA4g0dzYL9cSIzYYhHm19oqUOIrmjNA-iXShq81tPWkDU94120sl6oUOf9bBR2dKk2U4yWWOqeYb7FA_br197Ng-nzGlWapsdDUsgYFCMjozZN7uD49tCG4KWVEuxqT3I_JBJ0s6OygvhFxQOY9u86DXk8ZHznmUcdmpdVDuF4ehcbCwSkgiHbfQW2ywCO536VfWti2xOxABrslDNIW-QQU-MK1p3NHonmWzGPeO_HMk80k1DnwZX2A04CCsun8g4cjzSwlmFPWHt1lXwlpZw305dpa06RqbrRP4hckks6SKLX5TJ-U1KzpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=T3ahl2h-8rVVrcwVV1IvRMNgCnkaMnFA4g0dzYL9cSIzYYhHm19oqUOIrmjNA-iXShq81tPWkDU94120sl6oUOf9bBR2dKk2U4yWWOqeYb7FA_br197Ng-nzGlWapsdDUsgYFCMjozZN7uD49tCG4KWVEuxqT3I_JBJ0s6OygvhFxQOY9u86DXk8ZHznmUcdmpdVDuF4ehcbCwSkgiHbfQW2ywCO536VfWti2xOxABrslDNIW-QQU-MK1p3NHonmWzGPeO_HMk80k1DnwZX2A04CCsun8g4cjzSwlmFPWHt1lXwlpZw305dpa06RqbrRP4hckks6SKLX5TJ-U1KzpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdbPLKOuyeXAT8rhyuMpH2Ip_Vpa0bBYZbd90_P_grO7yDRrgq9J3Byoq0U04R8JpDI_R2i4B0saKuUcgYI_jF2k7b3kkbYvzi_HqjCGQa6m8kJN1rSXm_OIZGx-AsRYk---ldOSQberAraLzCABxVLPjhSAn04KnHtP0yBkerSYxfez0Pzkuh_mAQOiXdgCEeAa8H-nzfwOiC6p2jO4Z8LQKnPbZ6T7uKm2ED_H9wwJ300jpXga81odE_qlxradG4_BV4s7fOMdocuzHPu5-R45FFGGlDNmBOTc_g2kbh9AS0u1sCgTMck0ER6R7XHLAUNzqoSkFca2i0nz9HmRJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqcaZ4SWGDGLjpnehpaXyLbkd4w0w4HueF0cVrcYVvx4FVzoEUpIJsJNux2gT5n2rwDH6R360Tkzo3u3ZVBtciJ-t96P-0Rs4z51EB-vqsLkvY8gqzwYV67dDfF8g8FQuhsUlCpUDvs01IsWyF8MPAUIwJJIYA3_FOlVfwxrlsf0E0Gb9hpUhQPlDebm92Jzk94-S3sTELWMgl-cijoOLGZ7QkWm_lOcLZ2g4j9UOB7_cxhq8LVh08BIJMzHGBECGsjOcFv7EXqvpztjDGjkUnzV12cRr76mgRerVr0eMH2CCl62an1yp0IxlLICBmkXtV72_XLOXQueYzObKa-uDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M3WZeG4jclQ3AQr-zLB4XX_SlVHYHeXRoyS2FMNMOiOI2JUfq3TdTWg2GUFEBi9cj1Hnd7yeERrW4ug5jek-wESMbWH9OXT9dtZ7ouccRXncJ19TJV6g1w_bYvq1RTTs3jSdHMSGyx8Kn0-GGzTaW8DHKoMUlEvNNRjm4wQZpmmGMco1TGm2cZDdoZ4qeluabINGRMI53YflMTu4XDlo96iP8JbnGxmlO2X4qOo6ZlbGS9z1Br_thlXal85FN6ayZ3uaoym4dQfExxLgavkmH3ZONzNmp6pWaFkKV9BVZyGatreRjaqT3zwl_169uB6J8taJ-oK06vfOmYPbTu3OBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TtdUkz0cDfvTbEVrqmWHFlSewBcwTLzCLZvJrRV50917A1j4VgXOr0thsuAqJ1BEiWIzt4NX8u7-6ZT0DjRkaXWDDtp_bLCkCJ5sBd1nWSMGS6-f5LOLpW-LmNbpGUXPneNKhQ97rldo0s7W9WN5VXNwYULco_NDJs66lUdOdMf6vwOKi3cV6Q5S8eO8WkmamY82v_jzCqi-vzajVWoCP34jJLCBWkDl7QJstmQqshwMNKs_8ygjCxoTl6vM15RrhDdNVUDs0fNJvNMQl1wOzXuzCuk8CGKQZPaCX1vEJMJc8C7AimRzy2RmSCPabcKUe_E3BP2y3Ki3rMvqA0t1dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D2C5tYj-ra-qiwX32dhhcXanGuI5vPHCxX1EqTGbX3Hdl9cI7eavGBOuvywfOXysY9E1Jb8ejU3dh8GAj8v4N04RxuG4CsAXB0CANmhtm60-1do6O_it6xLz7fD-LNBhSbXSMTGecuI4a7QWBUrSVUr7RIDKZe8Z_YWKN6bwTW4vujDdns_3karnVQnQBVczLv2Q8YefRTXQBkytzncRj2vdc8gnlJ8bfiIVF11H0CnW_G53mG-w2rc9-iAvd_Gyms8f0QAzS70EbEN_tqwlOVI-_yaYL311_BDd-mBKeU7Ov-o0ROCw1ELQIp8Y-u_khKgIbHzQn-9h02Ncs-aJOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">7. به صفحه اصلی ورکری که ساختید برگردید و بزنید روی پیجی که ساختین تا باز بشه
این صفحه nginx که اومد یعنی اوکیه اگه ارور 1101 گرفتین یعنی اکانتتون بن شده باید یه اکانت جدید کلودفلیر بسازید
به اخر نوار ادرس یه admin اضافه کنید تا پنل باز بشه و پسورد رو وارد کنید و لینک سابی که میده رو کپی کنید و داخل ویتوری وارد کنید.
کانفیگایی که میده اگه پینگ نداد نیاز به ای پی تمیز کلود فلیر دارید.
مثلا این رو با پورت 443 وارد یکی از کانفیگا بکنید تا وصل بشه
188.114.97.6</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/archivetell/6343" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7r6drbmIU3sBA3-F4eQ0KU9Y92OJa2J13NNz9KWsN8IDRHUrCF4k2DDugGcTZ2MEo94nZ_MGD3uWFioxjKyhRbYdwDy2pyrwTFk9L1y1I51KRJ-VnbYKN11MGc-jJrZ9AIILJaiiYxIKfIXQYLm-7gTxbkQjGh_akNcsnVNWGW0wzIpPRLq9amq3oK31L8zvtU4c-a7jXkvSqlM6veC-wLVe5-y35JEWywaxZcmk6GZhxql_aoCThch2vlABPGLtzLJBfQixnp4HXymv5CD2fFpwBk5Aaj40YswnY-vn8TJzfeH_miMN8txiV4DSm_HUQqbuFeXlwBdxD9EJkejbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKdcomsb6v6khMdHIri1L3LbJ9YL3E6QLC0WDALf3pwrU47oWQeYwE3si63yYSF-veAq4BiR7FcPYQwRNwkE4CxV54_ycj5VsMuxdLB1gXQQzUgCxYdx3rFOntxYPVXi7wkt9X31_C7lDOcJZ-2EujAMjlfLEVbk7WwBBx1Tov6bIIERl4cFgFjJM7N8i2c2BXCutqfoc9ebeVlXVdIaqBB5iujBDQffl1h_92NXmkxbkVq1dn_cW-aNchAp4qffKwPI_LVZB9qcxplrtkqXtObv-Pqk87WqkJfxDpjcSaKrfKXTUnajfoqr_HNhQIJasKYj1JeU3zOwgxMU4dcLdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r88kPoARUY1F8LNT0n_YdNGxzWk99BihZW0cqv7cekmLXiPfnAj0RBLslKYb3d41NMWuvt1ORbAZko9KbUKdAXnrhbUpXTABBflkpWLVZxqKvj5VAFiaLd-xSS5PIHtMiTHCeT0_3SiQctW8eOCx91DP1_x7KkHqg0bdFXMyZJIaCGIGXVGMVKvyTS7SGRFRdTzUzJS1udYJk6y6yLNTIt8oOcRnF9MjyUYwZGsn002Bjt8p-mVJ2jqypnWAygU96tq10pVuasl3akMYBC8h6WqmGZuEevGq8PsF9R2-ajUa36Rv6mLg6aS14cNM-5vTRGoDQRcTvwSbiDntQpmpgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVthjAcEbMa5RNT8HI5xhYs6Nb4sFiFeKbqDorRKwBGE0o06a5bcX4lThcPF5NhZ1-WNdu1TiY6K_-Xl7UyIXZX3g1AIlHy-x-MNLdOn6pjGrP9mGP2Cnp0Ft91G1QmjE7HRjCen7yLJNlbd2PrRYY5o-OMP4yfPX2wIbhFDC59lekzgL67Ts9znpPfHAtOE2xU3ER5ARDGzP_HL44oPRDZ5QQax67VMvWy58KKLOCz1t1M-FlJcQuhFGzn1YcRJQW-4viGfHbQeINeqF2tn1uLJuOo2a4dKYQSvAuIEkviu8lHlQkm9m7Pj25sMnFDywQWKBMmd5ZFMIj-Wix0qJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFagcIzad8AibX8IZU2eSjeO2BW514N5Om9EeGMKIEuRKqX95loFKGEXG9Hc2JrKhhgwyfRV0_6oqEvxm3PGDzwsQ-hES0aTi8DUjzGkGRFFMPn42be2wMkkc17B-Of6-NOh1qJQZATHO9hM-dBAbXjjFhgp2vKJyk4zIMRJNOaYjsxBCyyDEIZQb6rvHzGVybWMZsdaqQRWp2OfC4cmlA9rlgW50NBVu_N8K6jRIEDQXFenGU5zghwo1-As2vecMWrjCVMT7lpk999umZYRomPM7aL8Y6yHsR0K3K3g-Q1CYe3wPqri4WMMv9g-ebw1TUj81eWF9Y_Qf1Muh3GapQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giCuSU0gZquveHOdBmmzzOQjpLDoo8gGHxdhwcutU-MK127RxQboawPlTTI0eJzCYtYnStFiEj5ESfXPKLcFwyevYwjde52AN9RiuUCzPwnqZxCAKP5h2yFPFABg8Dt9P4koLFuNIITdI7qbFTRnJK9_vP5CI9gdD4LI6R5Vi3fu6Eo00Zq5Vta8TH6yb6BoTsDgpFmv79wpYHJSiVnZDBC7r40RmmDdwVkpdOLDZ-BCcYpnN19595qwoT44s3aQB17Bx0V7NbEKU78o_XIN-aO4Z07wVlXCVmydeh1rh46EYbuZDuhciciaoWT1J7o_XOP4NW91Gq_ps2crKFbJjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFDkm-w1VLM2P_oi9SeNXfJXMCxHqI6Jc7LUbvAuR-Pwe9bHad_Kqk2g5GLfBrgLAuw-QIZo9A2amrANxenAzIvFMgIjr9_572O8RhD7UJ11pL6fnq7j82D2SxcgetMy4rBdLffoW9OAPtFj1TG_QxuU5ebXdjKPO7EU7FlZAvIPtl58_ZhAfDk1aZfxn54gzYg9JW7WWYSas9o6Tj77pFiFMcAHQJvEVTkiEGbk7aAeQCO87NUsy9wzPCEiVFYsaHRnwluHJgIshwFy1YBGtGJ1YpLPss4ordax1kw-9oroPo3tzivjL54BM0p78-Khu2A5ICT9tx992gfBj5oDLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=hqdU35Az3P6slWabAOiAeCNIpjHNKTx_5eIoRxOYTrdIsHm5zTplTXDDVIK1nNQslY5QwNgphtGBOXITMLc0F55uN8DRSzePVo_G1fDYq1wdDbRHqjDn0MZmFJuJYwwFdCzFiETRsa9W462GVdtZhvJgI4fqEZg9gfnEUpf0RWt1tWBVZ5zQ89TLS8lZ46saUNFhcfmjVRczDbN6Ese8d-UJ4aPgm8bwHucN4gj6sMY5A-7ENzttnbsiYLQyteR1sGceZ2Ir13M6fBtpQRQah9HcfxLMPVNuGwdDjxKOFr6_CeGOZOD0ke7KZvGg4ymZI2AxFD36Vs3htMfavCkziQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=hqdU35Az3P6slWabAOiAeCNIpjHNKTx_5eIoRxOYTrdIsHm5zTplTXDDVIK1nNQslY5QwNgphtGBOXITMLc0F55uN8DRSzePVo_G1fDYq1wdDbRHqjDn0MZmFJuJYwwFdCzFiETRsa9W462GVdtZhvJgI4fqEZg9gfnEUpf0RWt1tWBVZ5zQ89TLS8lZ46saUNFhcfmjVRczDbN6Ese8d-UJ4aPgm8bwHucN4gj6sMY5A-7ENzttnbsiYLQyteR1sGceZ2Ir13M6fBtpQRQah9HcfxLMPVNuGwdDjxKOFr6_CeGOZOD0ke7KZvGg4ymZI2AxFD36Vs3htMfavCkziQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
- لینک سایت در مرحله اول  - لینک سایت در مرحله دوم  #GPT5 #AI #API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/6335" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8jxU0m4aBuRG6SuSP5yWTq1Du9MTWYwGED-8Xm2KQcYMTlHyZfg_7iS8izhb8i-x72brPrne3ArZxsLVYwP3URXkyM6oOfTy7tqdUjyDdpcpBx5ygSxofhf0pA4ymRPN6O4clRNF3Ncbl2LFl7fwl0zxnuopUVKL5pSy4RCNs4EtwRNxtypRaD3arnl56sAtH5qiTDN2UEt9mtfyoDDdhYItzlItM7GgzdzNmlS9ficMrY-1xm_ltvAMyannkcPI7j2IQxKK0U7Hhh_GfUUWXS-vNDvYBzJZi9nVylcz5DThgi5MKVTakqJlh6_sWSw3puKn7Pu_xopJoOEbHN7KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsFH6dX1cdTHAnbMSRRaCwH6DTnYUEuu-eXH3AViYDVrJyAUxdMx6y5uxqOItpF2OtC_ibr_Z7ceTnlMBQo_khJtSOpDJrgwGoDdls9CfXcS8SjqWYZuGgKNNEmFM9TCesIOoxdBAY3wiNMK0lx3LOEjxuJJxG_aM3zS6z57U4oDZ7FFbAXIrZosKBf56jYNftRAsBpXyO1nY7p8_aJQoauZUBq89s3BlmuiZzYFOSNygWy16tOF15t1O5ud_UZolYdcJFiEbvHrZaiKNn70bhvJDhVl_jM-bkLUfntbHbic_mI6uBDMPLczrgNIljVs0wkrXDQa7_rXSwODfXnDCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6333" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXJx5GBBM1wwKC6sxRacsvsdhztimS3v8Gu9_L6xlS0MoHACE2IbekBPnj7pshAI_2UxoE6PJNV-2032bAvouG7Gatx_mx-QcvKj4sN093DqtOvMe_3VGHyCqdfbybTMV5d8FFUmFii6mHsY9EYBGt2Sc9CJwW3GBbwjudtbGVrU2eGOP8wSgR3uvwLfPG55JfxG5PvwfEsfAGG7Cg7nNhYX3a2NjkwNxtwuY9hO-6cfTFzhmcMtAVpIrxJiMhqgLyeYpExaWR63PYOiSaSZBB3DYuJxQPuCZMaReUiXb2-bSZLd_YWDx-og0feqnmDIX4tQoUodU2lx8yfKSpelFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHAfLkgxMlOY-FWugYvvqTTkFQeBtiSWRs5rtf_Q80_swUKv-BgNGIaH0lMigcvwTJPzt7Z-sf88v9PkeIxk9v209WfX5EECuJ6fTFChj9NIezNw1lMB2k__XNo6OdYolhropuKi5GNb8PU73iza8S46lFVws21v8zcbV9irMfDH1BY43KX4u1x6-ynZqA2Hm9DIpgkfEnoZplM4rkoMSG6feiugup9h-cRLVhPtEHgbe2o3wtxXFoPUlSpygIJBPGXmBSTepde1febXmnNa2aQPocMWW0gy2ZZlz_6Kz8p41WUrkxWkCQ-OD1brpTcJw8OcqiK5SsPbsbI0ndwc_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6331" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=WMRblL_AzhLi_M4gmEUdZp4v9Jf90L0w5oPtAHENVr82-6IPdthYp5qlTBOPhDMsR6jyB7y7_HB_eC6DFRke0peFOgs4spGxFD52BQiKwZ377fHczQM1xKA5lKjzaVcAikIgv8zcaV3dVaRQqRn4ZocLi064ueLqL7QY-vLgIV9rphSoY_ftB9Hr6ng-w8FprmdDTs7xXTrsTfbqJC64p-7xNlAU82YkE6Q5FL6oLAge1ws_TJwEMnjOZO5yiu_G6iRO0Xh3q2rIPjsyBKxZl9SKnaBzgmcwuxB0kG7qVds1B4fV978A036bXCWijc2TtfGQDYeNpRJkvzC1CPnPOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=WMRblL_AzhLi_M4gmEUdZp4v9Jf90L0w5oPtAHENVr82-6IPdthYp5qlTBOPhDMsR6jyB7y7_HB_eC6DFRke0peFOgs4spGxFD52BQiKwZ377fHczQM1xKA5lKjzaVcAikIgv8zcaV3dVaRQqRn4ZocLi064ueLqL7QY-vLgIV9rphSoY_ftB9Hr6ng-w8FprmdDTs7xXTrsTfbqJC64p-7xNlAU82YkE6Q5FL6oLAge1ws_TJwEMnjOZO5yiu_G6iRO0Xh3q2rIPjsyBKxZl9SKnaBzgmcwuxB0kG7qVds1B4fV978A036bXCWijc2TtfGQDYeNpRJkvzC1CPnPOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6330" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzTFpqYBj_5H3hfe89u-2iJh0-UuM3lHue9M64godacF1tzUCWE07sWnTnhFYzD8od5k38EEnaR562HNSJOxz0Iw42P2a5RNpeLNUaQZH924m-xgc3RyMkMTw8OQEOUrzUZggt412vV0FdpstoVnZVvczwTKPMDywX49uJhgbUdUPjsAEsfu02BeJmw8KicU3S19IhqNsgqJ3umPpRk2uLRT43z_LJQPfb_F_CGApTvrjXPLNDuM2I9X1gfcHbA7Pf_-8_MDaxp9tYwwPK_bvZ-GGfmu6NGvc9heqU_brtgTb1ybMv4QC5NABr1HvRjJ7S6MLPdG7sqBiMUOiU-Pqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6326" target="_blank">📅 18:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LP8AGosBi5-37h9w0i8wB6fc9qv1jys-10j5CPPSsaJcALZWUEAZhFSCLCNWVKKJuylnFSpSoPrTNEygvXTacSXAhO9J_ussgbk6NnYVLpxMWVsQwTJduk3lXwoQZTKRATpgPQNvYy83QR1drXyJ1McKfKhQaFmnvTxDCq0UpM-wTMwitHMmiQ0D-zO6L1dKHLC7vGvekiZDdKHU6Dn-1i71YT01efavKyebp3dApO6TTI4Boyndj1VyX3v8H9vx2VxUnYDA3aW3TNjQsuWkc8gUgzkWf2SLR1ZGNreIXdWarWSY72EhLE_k6MkPfZKyS7BLljrOQxNrWGoNj8sP4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6325" target="_blank">📅 17:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M60mT1S9zBASQMPPYKYcF1gbwe5weJRUy8CVHOzd7Udz5FPZPrGCWviwuakAIEvc4t1UA1x8RLPqV3AkHskX3iYrLAx6VVeKwGMTrMyRqPEILWui_efglKXoocbotjEammBfs2lvftdJOIS0rg3FZAQxklvYuY_ZyZUdNxdmdMz1vyzJpCZRA1WmgOIcZ5LEJE-jPXcdG41T08nc4zRn5duk9V3Bp1Y1CqNe83At0vuxc4sgDLxlqdRWjISnpeTeghS-pY1TpPxE7CcD4kyOATfYobJ_idZPNJBoSM9Bpa8X6BD7o1BNvwdhi_Yrdc-Atrc4V_9Q_invgmoMmtsQCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfOb1vBeeN36Z0qk4jzSF3bmIkUPv4T9gCgheoACwbEKL-jC4aZBnOH1yQB3m-4Hh1Ta9ESBPZyBuEe2jNP7T3d7_GCQwGRTBfUsNQTqrYfncjPw11L7keYKgOBdhsK5LCBv-68zc8hyiMLKjO3fL-A4fp0xh2HgbsNKXTyVwvBJb294sNVcjzEx7SH3Sxz42iY69FonSKzeZXDMVpIjuIgFhk97p-6pQqmLIrrSsTp6bsvS4s7TSqVk59ZT2R9jrB-PB8O5Pxo4_JmeLzwJYCqRckxgV9_ZT3WZfL3i0oMRrfsgACtsvFBai3fE_Bq-6qaRdXSc7Ljw9lAYrGaaZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6323" target="_blank">📅 16:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=MQ5A7isnht1ahFcfVQKpZzIRsEgbX5ZL7cVIpTfBo6V0O0n0ukcwug7xHYddvZNRQVd-VPDHl_bVEY6bRLsNwUBYgOhcCMxagQ5SjsHhyv0WxHx6AcoTwqFb0H4frL2s4C2MmZl0g_lssHtzlR5TzpZMZUHnEZbVZ63cbYKGnQ5Qn9WGrNH9zCumD6vGRFaeyzQwoPKcmJLp1eErT5e4XYz7soReXtpoYBxVRbzKUbEVfiddziA2kAdk0pqS-y1XToDuyGBS7Jc_adxvjva8k8O6o4Po3CkMyI5B2xRq9XxHjE1fT6PHX6oindupkk9D8IUOJ6QsAC0-foxDeIOu_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=MQ5A7isnht1ahFcfVQKpZzIRsEgbX5ZL7cVIpTfBo6V0O0n0ukcwug7xHYddvZNRQVd-VPDHl_bVEY6bRLsNwUBYgOhcCMxagQ5SjsHhyv0WxHx6AcoTwqFb0H4frL2s4C2MmZl0g_lssHtzlR5TzpZMZUHnEZbVZ63cbYKGnQ5Qn9WGrNH9zCumD6vGRFaeyzQwoPKcmJLp1eErT5e4XYz7soReXtpoYBxVRbzKUbEVfiddziA2kAdk0pqS-y1XToDuyGBS7Jc_adxvjva8k8O6o4Po3CkMyI5B2xRq9XxHjE1fT6PHX6oindupkk9D8IUOJ6QsAC0-foxDeIOu_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6322" target="_blank">📅 15:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h74ICE0BK3K2mpEaf8P6WwS2XZ4YJ8I3qv056zQ5YKBiE88HyRC4GrRgOMjMUfhWQBz9IxvKbCC8d2CpibjV0vC8L7qZscJJ1FEaUzItFSpalAseYZZPmR--ZOeiydI0NEz1QVvpqON5-lhB3IER_oMnUqhwNMgjgbhB9rogfqqQrRcnDpK0XqWptz5KDUApUah2uWbwFEAA5ynIz2MGhyHD4ujEe1iMa4adyc3pTei5wPE98xaR3f9vR8SwvybNOLCLh0m1jZf1YN18Hgu3HLJpR_YnlBho0Rzr_e9x2vjx_YXzo43D0r9I0_ON-22TbdO4TXojCU0HV61Bi-6xHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت موزیک رایگان
🎧
https://www.musiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6321" target="_blank">📅 14:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tqpyDQlsOYAJKp1W5ojOQKKZEgKsEmWNE6PgDxzvo9p0byASNIhT6-HAnyL-EumS3BIx6J849L8qMIM5l_BYiOjqwDD446NTRkAp8-C548d93Agd98Al3CDExZlv8VmuZzz3P9PspkAjazjduvmZKVPwSlFSdBCgb7IJ2DNM6IV-aiAzei7HzACTg8FYoO1O333I2LyIOXFshQXp1FOKzrW_Qi_Gx4mCZUTHMS-aQz6lNv47EtDKXsxaucGDNqj-Q0jvCBoUERHGAFBybyIUKLElnl8HRdZblumxMwFS-pq7OnNYNKWBYmN7vifRh4UHjmT6u24bmW8w6aXmuV6I_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fov0u74ra8kyGRs9YTcGwsG5xE_5Bp2II_Dw654rdK3O9gum7qpd4vEfNHP6B64UWgUa5O1GsKK9GcW6eAm6K5hN5cS1jyLpky-uh9jRAZ5qno8zCgM2y8blxZ8rzZ2suYh12LmkuUf1IiGZhct4gqlOH5SzJHcrC5q64aO7bHEOdN11JdlBQQ5MYOC1FnIoyrZlpFIJRyI_SSt0c9-E8EGY0kFDHSVhiplZXnUNWcIvR0LYXfgXSnYaqlpVnld1Om7DEsHYtQSmV_4NnbsCYZZ0L7R1xPUx1CJ8OLFBnpFw8cjMkKoEPGkAU8Bpb1txDeB3GLaSysvgs72aLy-9Ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6319" target="_blank">📅 13:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6318" target="_blank">📅 13:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6317" target="_blank">📅 12:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_HjrfagqJUVgLkHzwX4RVijlFLf-x-2YOiRRyVVdzgorhSdqzBctiHBBPklW4f6ofvfb11c81ktI201gsFE8JwhvBY3tdhldqJ-_4HdVWD_C_6IayPymqMegBctMUsAOlxgKc4bKRLs-SYlFB8UmUE3IiL2IJKZ9JrG1nfWg8vErNbVQNSYJd2wdL80-WAV1UrFlELRQxL6Op_X8NiDMPbH52tLV7fxLzfWd9eoeTWiVkWPEiNKF2wXzJpk2jDVmEOKUGiwyT8-UIH9Pt9WWPNJ6vqaKfFYXF9DlsAY8O3Vir4-0aRaPkxPeKbxs7tpWnOK0RFWz1yRKOlInTX6Mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6316" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oriOeO4TKQnaoTZSRFhfIQu8asAKiA87dB2fozXXLPDk5o_inVhb4jCjeZ8TwF1mnjQesjeVXPcLZw2lphyDQ1CKBqrmrEUOlt6KPoqhoGD3698jOTI1XdHHLc6lDLct14wwVexMiwpFxltfwQgm-RMZs8oL1ETBjBjjwE7RspqALFJkkLm1DigeE4UGX14hrISyYsEPq-eMmgje5PgfE-Cxa8D9cO6qWlZyHTKOZvZoyd6Uw4TNTv4ozzL7m-FxZKSBphrHgL4a29_rGbay_m-4Gfmn5eI3UV_PGDQkfX6zmHcK4NkTqrM68-DNgzmR7oUq-7jGDsbDLVAPw_-bVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iT77j9q_JRV40-2eqr6orCT3ACEdF57xeXA6Suc1bt0yiOhIsu80qysfyHJrlJoVtfnlr9JBl7Rwdot-nsAVC8a5gy7H6hTjMb6QeFzgPpD_n0R70R7KUtxo2CVZ3h4-0BpetfR1P9wS0TB5c3hYvsTYwPSpfL47jR27TeOi2bKpZEhyFgjJC-Nnnk_kkoPlwO6FrndDEMe-nwTcMxptm2r2VjRDQUY01XAnySrT4Yt-fyXb0fuUPFaZWDJULNk2eSOOGfhh61Husww-Teg2qW6jZMynjIohwojyl8PHBIFajrAoyYcWkfm0Gu_CxiiN1s85z45o_rvR7hw52Vyvzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=Ix9xkPiGp_QkjL7TiUHo4eQIwqegDTu50y2sHTShFSFCEQ-MQbiQPPHSvWGzo4Jvi6GuaXNeiZbNQHNGPF2g4y4TFy_IAkmCN-3qXYG2PyGvOUmNQXY-7UU0d3-FDaeWm4wyw30HCrDi2ABt2QrRslocTrRkXqYNUcwohZuupow1-a8oJYeMjzQYebV4pQj750AT3mrFCjxXiXENfHKUp6e3alVvJbonQxSQuCg_agInKvpI-Rw5AC3tMTkZx8HmykGYJWQsKlMwSEChTWb-jFzZP9WRuh7qMWfmErUIwkq_vEkaK2DEblhHmlJDwXErWcLg9w2lZl9AC7szEfCOEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=Ix9xkPiGp_QkjL7TiUHo4eQIwqegDTu50y2sHTShFSFCEQ-MQbiQPPHSvWGzo4Jvi6GuaXNeiZbNQHNGPF2g4y4TFy_IAkmCN-3qXYG2PyGvOUmNQXY-7UU0d3-FDaeWm4wyw30HCrDi2ABt2QrRslocTrRkXqYNUcwohZuupow1-a8oJYeMjzQYebV4pQj750AT3mrFCjxXiXENfHKUp6e3alVvJbonQxSQuCg_agInKvpI-Rw5AC3tMTkZx8HmykGYJWQsKlMwSEChTWb-jFzZP9WRuh7qMWfmErUIwkq_vEkaK2DEblhHmlJDwXErWcLg9w2lZl9AC7szEfCOEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6311" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDvj0z49JSiA808xoydr0LU_wW9QZVNEfCwWScjXti6Ht3jhOoPEVjgKYrTwgEF9VOdBCa4V3d5gNjARxs_m1bcIB7TEP9kS-eR1XlyzfFB5SyjLxklwOeNl7y7ik1_UNohqUGC4IgenZGpLwHloHP3gaYZYuxeoI94nbSZwJxmDgIj3ARgdVY266qp0jLgHJsZn41mbYBGm-3yYHtZOnNmjappPZcbUHikUJupK0L_A_A-8HKVo0CgcQ8zeaifAYz-6-GpPFtI7g8m7_pBNeiJLGtBcVBhYpzGimAbqaEaLU25jlSbe_uYP6YdPPFGouIc2T2pBa9MrfA38NRtdwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6310" target="_blank">📅 11:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/archivetell/6308" target="_blank">📅 02:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JabDfXFWzm7lrIVM5jsalLR9DBnUFHGMzPymDGCwvm_0D7NxYM-R2kA67gGxiRzdIseKtvFiopDi0cExmMrxOgM_cwYH2SWf10bT_fGEfLGAPoPS_Jz401QC4PjZtrbGrdPuaWZh-O_0SjPuCOUvn-Ek4Z0-tNGvk5ZM5MfubD5XixiYb66VE-2KnOkZQtqmTd3VSbLz4jJ7KkbnqTBSy0R9VRnOZmup7ivPEt-06mmDxHKMflErNRtFL6PAA34gFiL1vrX8IBXhIRSNQDnVPA5tb-L8LN5-4i2PhtE7Qqqzk5rFffzuN4OlPtR_oF-NP6-IzWbNbNc_Dw-ibAUKrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/6307" target="_blank">📅 01:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):  Aistudio.google.com  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6306" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مرحله یک طهلیل من به واقعیت پیوست
😝</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6305" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRKJ2YDZwjiI3_VrvJUMykqbXqeML7fds5MAwYr4XweqCHNceMH0bdGIMkk7xxX-wNO75zPob3tgP_t784dcylwV1unw13pC72zxQ5QIrvP1gOAwWudmHIvnX5kcNwfiSGm3QIGHw9mLz2PM88Bd01IcKMQxoI96q2uMk5AU1WzTDWUhLEQZeeL5aLOnBG750VjimqA7_8XNtu9mdnsU7HYmhDtrldS_aiyEw2ODO2MXNII_4euVYUqddwzc-XJ4T4f3wbOM_zcDcLtQ7ivKahxDjMJXKfSZOtKnDGflBskoyB28WdzC3GDkb7ph64qWYMqKsvAYFVgWLLqeQ4xpbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):
Aistudio.google.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6304" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6303" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6302" target="_blank">📅 22:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_XPgDf0n-Eyng3RAMF4l079SfNqtV1XUw7PzyvXMWjCn3WbFLqtqvzUtqVjFJkKGoMfReh6ZEwENE220R362pA3UUJSX5YZhyqjzpuQOVUtl1Zb67wvab_GIQEU8nRljxS_P23u8Y3D8VDUt8Qo4AK2jaKUpgWGALcEG_9CVvTlYob51nSEAsmiiVwPOgzSmnxLXaNaYo8jQHqlPOmTpNpW2p8OPABne9_sBdkTOkMhEDnqSU-B3FvkP4swz4bSOmiMjmDCTxplKvIZPNuHMhbNed7-z1zHgjh2bsdEQ_7ER3ruwFdj_ACruKQ9Zwvi7riXtlQSyhTK12aqmAG6cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6299" target="_blank">📅 22:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran
* دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)
///
* حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)
* کافی است لینک subscription را وارد برنامه v2rayN/v2rayNG کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
* نکات استفاده رو حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/archivetell/6298" target="_blank">📅 20:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=DIOD61E4aeVE7D1-7p3F8pmWvYeeCl_9s7ivdp6RKRWySKVUwVQCOKrCKvVU_VwNeE995ahQuF2vI0G-a4RWHd__FfIO3_A3sPQvmDOn9imEZu4Fr-8oQ2FrUrGsE_fUyZF1CZPrZAs4koWYxzjmZkKuXJ7MWKlqdgE0e9MJZQq6-V32fSRUWWMQH0-0ru04pEjgytNYt3PisBDj8yesZIUotNmdzO5jOGUihdyh6fxgRFD9aO_xgW7dFBd9OuI3Myo1cVXXGam5qwVbusCZR6CbOT5nPCbWc4Zft1u3pCe2y9evYROTQfO2agP6F6ikZkmCC-3rsj_4CAjtp3FtQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=DIOD61E4aeVE7D1-7p3F8pmWvYeeCl_9s7ivdp6RKRWySKVUwVQCOKrCKvVU_VwNeE995ahQuF2vI0G-a4RWHd__FfIO3_A3sPQvmDOn9imEZu4Fr-8oQ2FrUrGsE_fUyZF1CZPrZAs4koWYxzjmZkKuXJ7MWKlqdgE0e9MJZQq6-V32fSRUWWMQH0-0ru04pEjgytNYt3PisBDj8yesZIUotNmdzO5jOGUihdyh6fxgRFD9aO_xgW7dFBd9OuI3Myo1cVXXGam5qwVbusCZR6CbOT5nPCbWc4Zft1u3pCe2y9evYROTQfO2agP6F6ikZkmCC-3rsj_4CAjtp3FtQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOY54iz5Zk2PQRb0tlF2UISgTuAD6o0109-G0fN36dG8Tz2bHkN9pOCTtgJSicZOfIVr4BvrFsn6VNorlxALK8jxFQOPQLHfSebbEUUUosvA8acVszGE4eQ8C-T-mrdRR7ZqPJfYsAYm9Vx2H4S0NaoR0brOzhk8ybEtwBN_BDUDtXYXnErWaNV33SocZy4J0nslfHwXpxWGvfdEXKhUxqoVSZr_HlfTitZLrhJLOFAT6djTlksogKi00g9QTIWalUzZeFxw8cX0nlGbPe428C3o9BYumcCKmBDo3fXhdEc0Nc6Q_OOpUFzhBhdM-i52hHd23xL73FYNydfMKo-l9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اگه میخواید به سرورتون وصل بشید ولی مشکل وی پی ان و این چیزا دارید و روی cmd و ترمینال و این چیزا وی پی ان سیستمتون کار نمیکنه میتونید از ssh آنلاین تو خود گوگل کروم استفاده کنید.
https://webssh.webhorizon.net/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6295" target="_blank">📅 19:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6293" target="_blank">📅 17:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FyY61lnIcHRZf58uHd0kPodG_olhQWf4lwM61uJPrgddqy6s9Ao949FcHy1uAIygZZiQB5JtQLrobYXz6wfzSbhCsjnIKxiMLC42V4pIrWy_y0T5T9N1l9LzM5LuleBJ3xt2RUFV-yoF2HZA7SrgPNFWRTj82SlIpYCtPLDtmqQGnZ8DKj5Sjg5dXuz6gtRfFflmliJLTsXbRu-9ldHTE0nY_oPKHG8jVduaYOZyxAif3pIlRi1sts3n2gv_dGQp6yEZcZTDGmBPyb2_MzYLlBJCESPV6A7SJlO9lvIbh-EigGBlNxnUayrE4BxmCUXxMXAYykrnyUj8pwf7YScXPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m_QRcvMLY_ufwATl6_SkBmTCm4XGvp9XNUwf2Js0n3rS4VyO_iMpg2LbbQn2Dkg1PYqJMGbROkyz7uvCUPPu-7axcMTFy9FsnP-RlgTFt0AQaQlFyREi6zYEsOrvrHAWJSIO6m2067AchAEHE3J-H-01N_5nEOd8N73mvO4wpbWiB7tSsfZgsvnKkHqDGTCvTj1bWpSPUXpddcrU_NH8h1d9FYUxnrAdLRY4PwH1rhzXBZiuZtKFvh2uNFTIfAzdCzGzR7rogfADMK5pnhGZx7wvt97q_RVG60yK-m8IiZwCnIaSrIBg8VvBjtWH5JgSY70QOMWcmboutB5nTTfpCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HUSXrvHdJlyjF0QCdihjxATkNAXlh4YoLDpI67dJi8OPdrRlaD0qKxCw52KRP0pSQH2OtJskfdaoyB9FzNRKokTNXBc1nj8R_iaGujBJIFzjQX-1KC9jQG0KSsiq9Q9KO-vFBSx9LX_gT4wthtW9UYIWmbs5Q3fkeOJ-EP878exe5ODPdtUEnVp8Erou8PifF9DwiuN5_6aehX-K38QxqORQNsxbszDTlst1E7hIwCmifLvM27Ourno-dIdBGXiNPhkrfjNR-zQHnRlkkZEIdd3lzl2lAYPjtQn6ybJ-Z6XWcXr-iW8tR6SKGbV9TwDoRvlpTCsHdNxRKHqP6LW0xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6290" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54834411b8.mp4?token=MljHZRF062B_KW9mwh8Id4xCQ6MNIYqhtrMeOlOJOfXLlM7ykNrh_npe3ZIZUIz2VgAZ1koDBYxz4x-itUQDWKC5nZpc6H7Pb2UEK92ymB3dEgkMABdFzLbOnHmIcr3hVGf20DOXf9P6tN6gr9NeN0ZRQCKmY04XRabhO8XDl415dA7MmWYSR-jZLV51ip4XO7BgQ4wUlrjuk9UK0aZqOw2DUWQEZTpO6XjivOM-Z92Pt4oNg12OMFQfLZOx3XEBZnxC_cdiLZmUHo-A9K8mYYSVN6UBo-Ym8SpKQOT3aF4rUUhcPNZq_E1ojg7E2WXGsAsvdfhlZr3xP6anQphVSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54834411b8.mp4?token=MljHZRF062B_KW9mwh8Id4xCQ6MNIYqhtrMeOlOJOfXLlM7ykNrh_npe3ZIZUIz2VgAZ1koDBYxz4x-itUQDWKC5nZpc6H7Pb2UEK92ymB3dEgkMABdFzLbOnHmIcr3hVGf20DOXf9P6tN6gr9NeN0ZRQCKmY04XRabhO8XDl415dA7MmWYSR-jZLV51ip4XO7BgQ4wUlrjuk9UK0aZqOw2DUWQEZTpO6XjivOM-Z92Pt4oNg12OMFQfLZOx3XEBZnxC_cdiLZmUHo-A9K8mYYSVN6UBo-Ym8SpKQOT3aF4rUUhcPNZq_E1ojg7E2WXGsAsvdfhlZr3xP6anQphVSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6289" target="_blank">📅 16:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6288" target="_blank">📅 14:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6287" target="_blank">📅 12:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⚡️
سیم کارت رایگان همراه اول به خاطر جام جهانی (کد تخفیف + پست رایگان)
CUPSIM26
هر کد ملی تا ۳ تا میتونه بگیره (همه رو تو یک سبد بذارید)
لینک خرید
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/6286" target="_blank">📅 11:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=WcqJ8etod0NiN_2xxnUh5I9Ld-UgYHp2IDU1C2e_y6UrnVL79G8L6ltM3Vuz5t-7b6kewMC7TKCO3p81YN-7h-CyCU-N0x3SJ593uxNVQ41gc_4c_gl4Ou5uFAcn0ICXGRd-q_e3g1bBALTu1U9C195R_pmxuJJ99g-xxJBASxEHEjptAQtCocYcqnESrQc0x3Lsvf4Oj3SniN8vuIYcVtSoN4TWyM0AtFU2pT6zRwT5V19FEGn-QzU9x86rz5xVQEdLTej36SacY042289zD0rRzgQu7yvYnMDl7fXnwOlWww_s3kOJGcaz6Lh8EP5fs2BJO1lwzaBIMgFp25Fv9g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=WcqJ8etod0NiN_2xxnUh5I9Ld-UgYHp2IDU1C2e_y6UrnVL79G8L6ltM3Vuz5t-7b6kewMC7TKCO3p81YN-7h-CyCU-N0x3SJ593uxNVQ41gc_4c_gl4Ou5uFAcn0ICXGRd-q_e3g1bBALTu1U9C195R_pmxuJJ99g-xxJBASxEHEjptAQtCocYcqnESrQc0x3Lsvf4Oj3SniN8vuIYcVtSoN4TWyM0AtFU2pT6zRwT5V19FEGn-QzU9x86rz5xVQEdLTej36SacY042289zD0rRzgQu7yvYnMDl7fXnwOlWww_s3kOJGcaz6Lh8EP5fs2BJO1lwzaBIMgFp25Fv9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1nKRkL0OTCUhd_FQH3K3jRVQSn4FVSKFGTZL9JpXq6ln4vSfcY77o5t0PX2XLHu5ye9cAolTn7t_xyRWhfF4jPkhAICoBiYkssw5_IJ_Y2ObmvfokEWpEGJ_zFMFan7ZZIRkzlhwuxf3virXdZ-odlU5Aht7R7IvfWY7Ezb3b7UAN5bFVDCDB-eAC-ItocAnRr1S_h877cWXeO9jfJB-UvFDhvNbJmMrZ7LoOQDeVLHnKfblWsrMO_rxWz_81jNXDoAUL-4gBweJ8djzt38C0Sb9xZjRs4-18o5rbuE9n8DnGdac5F1bPN0PhyR8vMHu7OwzR8L7UwlrrzuuRKkWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=BzMDeh150w0bRT-td8VhcnHSqR6S76zIiPqQ1ilYD-RE6h2A09LKqcN4WRDW4D6UOBM-WL2yXOTrjWOvtuZcs8i7fZa6jp7sgBG9Tm0WRSY09pEt5udBdarwgN7fy8teLz4M4OBPui6Qs6DuotkXHQyI3W_vYpPqGoEkvnpiz2bZ6IBdSyrmqC6k-reKSRyKV-slg_t1iZQHzkYWao4eJJ6Q_8qG2hhj9CfABqOkLdOqcKbli503v4rJRU2ia8dqPvSg1LHwrqpkPfrgSfBPS_z94AyKcNWNy33w2EmCmgRWOqD0Di0mzZqgxXVBE98z35b6Xu9qNRUeovnvlOXOMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=BzMDeh150w0bRT-td8VhcnHSqR6S76zIiPqQ1ilYD-RE6h2A09LKqcN4WRDW4D6UOBM-WL2yXOTrjWOvtuZcs8i7fZa6jp7sgBG9Tm0WRSY09pEt5udBdarwgN7fy8teLz4M4OBPui6Qs6DuotkXHQyI3W_vYpPqGoEkvnpiz2bZ6IBdSyrmqC6k-reKSRyKV-slg_t1iZQHzkYWao4eJJ6Q_8qG2hhj9CfABqOkLdOqcKbli503v4rJRU2ia8dqPvSg1LHwrqpkPfrgSfBPS_z94AyKcNWNy33w2EmCmgRWOqD0Di0mzZqgxXVBE98z35b6Xu9qNRUeovnvlOXOMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvlNxsOrJbuN7YUA0s1KDPG308GbAnjJVXAF5_bWp7y9VoXmo1_DOXfnB8f9s0wh6Bj8mFeNtCPvPhGWb8cKro6zJLnfxuGSv8nxizTpW9c05uVlU3Vu1dDlXm4EKNoSCkm3_xB0rjla0mJSaCK2ydPTG17w4yYvb35hlKwxkcfMmHhWowUdgKmGOgK6X0906U9ORGgGsJh-61Ho3jbrezW8Q5Dqy2qLTgLctvJh7pW0GMwDU2LEDl7rSTAo6kidKmrcfdTugfulAmhX-c0qJQwURmxQy31S7hp5SpUghlvcOGQfKCvm8jQ18uXGEEchRLVVb0Vgi_EdPwYsSlC-EQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6282" target="_blank">📅 08:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJ-wm10wMb6k6pPF5du1yN_l3fuE2eAzMJjaXEYWoIPFfOljdIBHa7cU5B9hh1GrnfF9eVsnc35vJYda6hfX4jxb5NOJUutJ3VzUMk2_emOMCWSbFZMTx0MLKmwZBJHcuiV9VSX9Xnuf5o_7GDZFiBIf6Efz50csP0TnR5d9dvtkrdFYCbazAZ3Ei-fu5Ip9FuLmFwGmUBYmeiyuACAIt6JX-XfAtlcmTbOgnJ7zqg7umwpw9M6_Q1gepzyzLYjTdusyj1ljld7byfQGBnzrpYtW-OAlXwodnfZzx1s2AD5oXtdsBCKoo8eUN9Ccxen9pp8KIY5E-9FQXn4EFBH-sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوتاه اما جالب
❕
به این صورت داخل duckduckgo میتونین qrcode بسازید
🔗
🎁
@Archivetell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6280" target="_blank">📅 03:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6279" target="_blank">📅 01:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚀
راه‌اندازی خودکار 3x-ui با WhiteDNS؛ از صفر تا تحویل کانفیگ در چند دقیقه  اگر حوصله نصب دستی 3x-ui، تنظیم کلادفلر، گرفتن SSL و ساخت کانفیگ‌های Reality و VLESS رو ندارید، WhiteDNS تقریباً همه این مراحل رو به‌صورت خودکار انجام می‌ده.
📋
پیش‌نیازها  قبل از…</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6278" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=H5-V_R_xZl8a4fk-Z_bI0z4xWSkEKKf_U65Eio6DWdPV2X_oKRe_OiK5XtHIfFMKuMdRHSrG8qvCSVGRN2BIbEhzmOup2jCMdKySp5D4Ty8l7zFdDGo7rsqrz7hPuGt16Ju7Q3lbTZv4l7Vp4sSHFaze2GVCwxtILWmOzh5k1zWVebrKRS3IfnT_b_WLzeFjQ9si21yUjfusBP5WGXLJJyWb19gzogiOHk99r8UonmAhgFafrK6gJB4wyn7NfDmii64Dy2eiThlGhmUHvtFR-CDnTL2eoZVlE_38AKkciXX45olOmXNxUX8Echv9cBnyxl5tvdnQCMHswZkwi1zk2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=H5-V_R_xZl8a4fk-Z_bI0z4xWSkEKKf_U65Eio6DWdPV2X_oKRe_OiK5XtHIfFMKuMdRHSrG8qvCSVGRN2BIbEhzmOup2jCMdKySp5D4Ty8l7zFdDGo7rsqrz7hPuGt16Ju7Q3lbTZv4l7Vp4sSHFaze2GVCwxtILWmOzh5k1zWVebrKRS3IfnT_b_WLzeFjQ9si21yUjfusBP5WGXLJJyWb19gzogiOHk99r8UonmAhgFafrK6gJB4wyn7NfDmii64Dy2eiThlGhmUHvtFR-CDnTL2eoZVlE_38AKkciXX45olOmXNxUX8Echv9cBnyxl5tvdnQCMHswZkwi1zk2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6277" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=fqXcKkIT-nmz0b5mAV8xQGW2SYhnSA2vZgJ9Lh-kZtjyILnoNU4M5CjI0t5HzOpfuYelNAaMyB13vwpgf9n_GJtyw63fi8iV5yftdIEfqEraHKjMfiJpk8yuJziifpoHubB-RvNkPtw1AacALao9Vbx7zYLPOHaFxhITjnjIA_KOu4EPOpT8RJ53qA0JNaMSIFxnj0laQVLs3FXCeqfyYo8Ix5yVzUzqsLgqV4J4smtA74PJsM0f_dRGkJ5_rhsHGWjR4G-6AKc-YvsLSWKoV_SVzmOfHzKnZj2THS_l63kRc17nsjGHxw24RcvAW02xpaQol-m_SeNLFFKDl5ikrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=fqXcKkIT-nmz0b5mAV8xQGW2SYhnSA2vZgJ9Lh-kZtjyILnoNU4M5CjI0t5HzOpfuYelNAaMyB13vwpgf9n_GJtyw63fi8iV5yftdIEfqEraHKjMfiJpk8yuJziifpoHubB-RvNkPtw1AacALao9Vbx7zYLPOHaFxhITjnjIA_KOu4EPOpT8RJ53qA0JNaMSIFxnj0laQVLs3FXCeqfyYo8Ix5yVzUzqsLgqV4J4smtA74PJsM0f_dRGkJ5_rhsHGWjR4G-6AKc-YvsLSWKoV_SVzmOfHzKnZj2THS_l63kRc17nsjGHxw24RcvAW02xpaQol-m_SeNLFFKDl5ikrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6276" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=sWqrayEMhOoLnviqwUichqOHM4HDaAJN3ntONBKpr1GOQKzJUVXuRRHSCu976tdEE2oupMMe5AVpp18KPJCW0eAyW8cqZ_inPEXRVvoimRbDDS4da7kSxjp6n5BFO_sHS0Dtp2J7KaAdAYWyXbnc4QcvzQBYkHfnurOqs1oHpYM5alSUIjRwFhDB4kbXUdSckqsNBjaNU42TWRII4l1P8iBFq7ltSGlqMhwSj8A-9yh4ULSdzQlbwS94y6dnWligZ-zrenb7m2uh2qHLdqQcyHLDC5dWdLY6qn4E1QqJ4uLrSGaPadYWB9ZMiy7r_WRzFKolSpSVimtC-7mjGqT6MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=sWqrayEMhOoLnviqwUichqOHM4HDaAJN3ntONBKpr1GOQKzJUVXuRRHSCu976tdEE2oupMMe5AVpp18KPJCW0eAyW8cqZ_inPEXRVvoimRbDDS4da7kSxjp6n5BFO_sHS0Dtp2J7KaAdAYWyXbnc4QcvzQBYkHfnurOqs1oHpYM5alSUIjRwFhDB4kbXUdSckqsNBjaNU42TWRII4l1P8iBFq7ltSGlqMhwSj8A-9yh4ULSdzQlbwS94y6dnWligZ-zrenb7m2uh2qHLdqQcyHLDC5dWdLY6qn4E1QqJ4uLrSGaPadYWB9ZMiy7r_WRzFKolSpSVimtC-7mjGqT6MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6275" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ادم خودشو باید برای هر سناریو اماده کنه و باید تو پیشگیری خوشبین باشه. چون شاید همون ی روش هم جواب داد</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6273" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">همین الاناس که ترامپ میاد میگه:
دقایقی قبل قرار بود دستور حمله رو صادر کنم، ولی آنها گفتند ما مذاکره میکنیم و من برای این حسن نیت آنها ۲ هفته حمله را به تعویق انداختم.
ممنون از توجه شما
دانلد جی ترامپ
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6272" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
